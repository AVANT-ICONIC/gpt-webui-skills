---
name: video-watch
description: Watch and analyze videos in ChatGPT WebUI from a video URL or uploaded/local video by extracting real visual frames, timestamped contact sheets, and available captions. Use when the user asks to watch, inspect, review, summarize, reverse-engineer, or answer questions about what happens visually in a video.
---

# Video Watch

Actually inspect the video.

A transcript is useful evidence, but it is not a substitute for seeing the video. Do not claim to have watched a video unless you inspected visual frames from it.

This skill adapts the useful idea behind `claude-watch` to ChatGPT WebUI. The WebUI-specific optimization is to combine many timestamped frames into contact sheets so the model can inspect dozens of frames with a small number of image-tool calls.

## Core pipeline

```text
video URL or uploaded file
        |
        +--> yt-dlp when needed --> video + native/auto captions
        |
        +--> ffmpeg
              |
              +--> scene-change frames
              +--> uniform coverage frames
              +--> dense first-10s frames
                         |
                         v
                timestamped contact sheets
                         |
                         v
                 inspect every sheet
                         |
             transcript + visual evidence
                         |
                         v
                    answer user
```

The sampling is deliberately hybrid:

- **scene frames** catch cuts and shot changes;
- **coverage frames** prevent static videos, screen recordings, slides, or talking heads from becoming nearly invisible;
- **hook frames** sample the opening 10 seconds at 2 fps;
- **contact sheets** pack up to 12 frames into one image so WebUI tool usage stays practical.

## Trigger

Use this skill when the user:

- pastes a YouTube, Vimeo, TikTok, X, Loom, Twitch, or other downloadable video URL and asks about the video;
- uploads or references a local video and asks you to inspect it;
- asks you to watch, review, summarize, critique, reverse-engineer, or explain a video;
- asks what is visually happening at a timestamp or range;
- explicitly asks for frame-aware analysis rather than transcript-only analysis.

Do not invoke it merely because a page happens to contain a decorative video.

## Evidence rule

Use three evidence classes distinctly:

1. **visual evidence** - what is visible in inspected frames;
2. **transcript evidence** - what captions say;
3. **inference** - motion, editing intent, causal interpretation, or events between sampled frames.

Never convert an inference into a visual fact.

If frame extraction fails and only transcript evidence is available, say that the result is transcript-based rather than pretending the video was watched. Humanity already has enough summaries written by people who clearly did not read the thing.

## Runtime assets

Canonical helper:

```text
https://raw.githubusercontent.com/AVANT-ICONIC/gpt-webui-skills/main/video-watch/scripts/video_watch.py
```

Cache it inside the current WebUI container at:

```text
/mnt/data/gpt-webui-video-watch/video_watch.py
```

If the cached helper is already present during the conversation, reuse it.

When the helper is missing:

1. open/fetch the canonical raw URL with an available web or GitHub read tool;
2. materialize/download it into the path above using an available container/file-download tool;
3. make it executable if needed;
4. do not copy it from an unrelated mirror.

The helper requires:

- Python 3;
- `ffmpeg` and `ffprobe`;
- Pillow for timestamped contact sheets;
- `yt-dlp` only for URL sources.

## Source resolution

### Uploaded or local video

Prefer the real mounted file.

If a current-conversation attachment is already available to the container, use that path directly.

If the user references a prior/library file that is not mounted, use the file tools to locate/materialize it first. Do not invent a `/mnt/data` path from a filename.

### Video URL

Use `yt-dlp` to acquire a maximum-720p working copy and any native/auto captions.

Check for `yt-dlp` first.

If it is absent, obtain the current standalone binary only from the official `yt-dlp/yt-dlp` GitHub release and cache it under:

```text
/mnt/data/gpt-webui-video-watch/yt-dlp
```

Use the container/file-download capability rather than trying to install packages through an environment that has no outbound package-network access. Mark the downloaded binary executable.

If the source site blocks download or requires authentication that the WebUI environment does not have, do not fake success. Ask for an uploaded video file or another directly accessible source only when that is genuinely required to proceed.

## Run

For a whole-video pass:

```bash
python3 /mnt/data/gpt-webui-video-watch/video_watch.py "<source>" \
  --max-frames 72
```

For URL sources, add the cached binary when needed:

```bash
python3 /mnt/data/gpt-webui-video-watch/video_watch.py "<url>" \
  --yt-dlp /mnt/data/gpt-webui-video-watch/yt-dlp \
  --max-frames 72
```

For a specific range:

```bash
python3 /mnt/data/gpt-webui-video-watch/video_watch.py "<source>" \
  --start 02:15 --end 02:45 \
  --max-frames 72
```

Accepted time forms are `SS`, `MM:SS`, and `HH:MM:SS`.

The default output location is deterministic per source:

```text
/mnt/data/video-watch/<source-hash>/
```

The helper emits JSON pointing to:

- `manifest.json`;
- `manifest.md`;
- timestamped contact sheets;
- `transcript.txt` when captions exist;
- individual source frames for zoom-ins.

## Inspect

After a successful run:

1. read `manifest.md`;
2. inspect **every contact sheet** with the image-view tool;
3. read `transcript.txt` when present;
4. answer from both evidence streams.

Do not stop after generating the contact sheets. Generating JPEGs is not the same intellectual achievement as looking at them.

Each contact-sheet tile is labeled with:

```text
#frame-number  timestamp  sampling-kind
```

Use those labels to align the visuals with the transcript and to cite relevant timestamps in the answer.

## Zoom when needed

Contact sheets are the overview, not a magical microscope.

Open an individual frame from the manifest when:

- on-screen text is too small;
- the user asks about a specific visual detail;
- two adjacent frames are ambiguous;
- a UI, chart, code sample, slide, or object needs closer inspection.

If a whole-video pass is too sparse for the user's question, rerun only the relevant range with `--start` and `--end`.

For long videos, prefer:

```text
whole-video overview
        |
transcript/question locates relevant region
        |
focused range rerun
        |
individual-frame zoom if required
```

Do not blindly increase the whole-video frame cap until the WebUI drowns in JPEGs like a security guard staring at 96 CCTV monitors.

## Transcript behavior

The helper prefers captions already exposed by the video source.

Default subtitle language expression:

```text
en.*,de.*,.*orig.*
```

A missing transcript does not block visual analysis.

If captions are absent and an already-connected transcription tool can transcribe the extracted audio without creating a new paid dependency, it may be used as an optional enhancement. Do not require a paid API key merely to use this skill.

## Reuse

When the same video is referenced again in the same conversation:

- inspect the existing deterministic work directory first;
- reuse the downloaded video, manifest, frames, and transcript when still present;
- rerun only if the source, requested focus range, or required resolution changed materially.

## Failure states

Report the concrete failure:

- missing `ffmpeg` / `ffprobe`;
- missing Pillow;
- URL acquisition blocked;
- unsupported video codec;
- corrupt media;
- no captions.

Do not silently fall back from "watch the video" to "read a search snippet."

## Definition of done

A video request is complete only when:

- the source is resolved;
- visual frames were actually extracted;
- every generated contact sheet relevant to the pass was inspected;
- available transcript evidence was considered;
- requested focused reruns or zoom-ins were performed where needed;
- the answer distinguishes observed visuals from transcript content and inference;
- important claims can be tied to timestamps.

## Credits

The scene-change idea was inspired by the MIT-licensed `claude-watch` / `claude-video` family. This WebUI implementation is independent and changes the runtime strategy around hybrid coverage and timestamped contact sheets to fit ChatGPT WebUI tool constraints.
