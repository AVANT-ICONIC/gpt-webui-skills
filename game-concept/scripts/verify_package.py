#!/usr/bin/env python3
"""Offline S4 copy verification against independent Git blobs and SHA-256 manifest.

Optional --source-dir compares a real paired S3 checkout. No network or writes.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

PIN = "76f4aaf2540ad5620fd6a0e7fd252646e12901a5"
SRC = "game-studio/references/concept-core"
CORE = Path(__file__).resolve().parent.parent / "references" / "concept-core"
BLOBS = {
    "coverage.json": "b494cb7f5d2657a0f8b0c6c983425aedd0677bfc",
    "framing.md": "53e57a5708439a7ec4b378e0fc0f1d4b74562f11",
    "mechanism-synthesis.md": "e6715b059e55720f6c7a5b4a402dfd0f5f518f43",
    "player-interaction.md": "0fc4f057e66ad57bdb225eddf00d37629e7b74de",
    "systems-and-economy.md": "0c9f139a9e3565d53a986438eb25613f1697659b",
    "progression-and-variation.md": "b2555010c6ff9ca948b97029b25bdc747b8eadbc",
    "experience-and-game-feel.md": "04080fc9806e97adb9b2d87dfad89d998c1cf7c6",
    "pitch-market-and-scope.md": "ba12cc646845ec8e025cb2ccb4f145eeb34a52c2",
    "reality-check-and-playtest.md": "18359215f272b1b6778a3a92fc41966146df40e4",
    "existing-game-rescue.md": "602096a767ca2d4af1f9e248c0f89ed82a7fd485",
}
MANIFEST = "package-manifest.json"

def blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\x00" + data).hexdigest()

def verify(package: Path = CORE, source: Path | None = None, required_revision: str = PIN) -> list[str]:
    """Check all package inputs; fail closed on any mismatch."""
    errors: list[str] = []
    if package.is_symlink() or not package.is_dir():
        return ["snapshot root unavailable or symlink"]
    got = {p.name for p in package.iterdir()}
    allowed = set(BLOBS) | {MANIFEST}
    errors += [f"unexpected: {x}" for x in sorted(got - allowed)]
    errors += [f"missing: {x}" for x in sorted(allowed - got)]
    target = package / MANIFEST
    if target.is_symlink() or not target.is_file():
        return errors + ["manifest is missing or unsafe"]
    try:
        doc = json.loads(target.read_text(encoding="utf-8"))
    except (OSError, ValueError, UnicodeError):
        return errors + ["manifest is not valid JSON"]
    if not isinstance(doc, dict):
        return errors + ["manifest must be object"]
    for k, expected in (("source_revision", PIN), ("schema_version", 1), ("source_root", SRC),
                        ("generator_version", "1.0.0")):
        if doc.get(k) != expected:
            errors.append(f"manifest {k} mismatch")
    if doc.get("source_revision") != required_revision:
        errors.append("requested source revision mismatch")
    entries = doc.get("files")
    if not isinstance(entries, list) or len(entries) != len(BLOBS):
        return errors + ["manifest must list ten files"]
    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("non-object manifest entry")
            continue
        name = entry.get("generated_path")
        if not isinstance(name, str) or name not in BLOBS or name in seen:
            errors.append(f"unknown or duplicate path {name!r}")
            continue
        seen.add(name)
        if set(entry) != {"bytes", "generated_path", "sha256", "source_path"}:
            errors.append(f"unexpected manifest keys: {name}")
        if entry.get("source_path") != SRC + "/" + name:
            errors.append(f"source path mismatch: {name}")
        path = package / name
        if path.is_symlink() or not path.is_file():
            errors.append(f"unsafe or missing file: {name}")
            continue
        data = path.read_bytes()
        if entry.get("bytes") != len(data) or entry.get("sha256") != hashlib.sha256(data).hexdigest():
            errors.append(f"manifest bytes/hash drift: {name}")
        if blob(data) != BLOBS[name]:
            errors.append(f"pinned source blob drift: {name}")
    if seen != set(BLOBS):
        errors.append("manifest missing or duplicate entries")
    if source is not None:
        if source.is_symlink() or not source.is_dir():
            errors.append("paired source directory invalid")
        else:
            extra = {p.name for p in source.iterdir()} - set(BLOBS)
            if extra:
                errors.append(f"unexpected paired source: {sorted(extra)}")
            for name in BLOBS:
                src = source / name
                dst = package / name
                if src.is_symlink() or not src.is_file():
                    errors.append(f"unsafe paired source: {name}")
                else:
                    raw = src.read_bytes()
                    if blob(raw) != BLOBS[name]:
                        errors.append(f"paired source no longer pinned: {name}")
                    if dst.is_file() and not dst.is_symlink() and raw != dst.read_bytes():
                        errors.append(f"paired source differs: {name}")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--package-dir", type=Path, default=CORE)
    parser.add_argument("--require-source-revision", default=PIN)
    args = parser.parse_args()
    errors = verify(args.package_dir, args.source_dir, args.require_source_revision)
    if errors:
        print("SNAPSHOT_DRIFT\n" + "\n".join(errors), file=sys.stderr)
        return 1
    print(f"SNAPSHOT_MATCH ({len(BLOBS)} byte-exact source files; revision {PIN})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
