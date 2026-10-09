import test from 'node:test';
import assert from 'node:assert/strict';
import { copyFileSync, cpSync, mkdtempSync, readFileSync, writeFileSync, rmSync } from 'node:fs';
import { join } from 'node:path';
import { tmpdir } from 'node:os';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { verifyRuleSync } from '../verify-sync.mjs';
const root=fileURLToPath(new URL('..',import.meta.url));
test('WebUI snapshot is self-contained, SHA-pinned, with no local runner claims',()=>{
 const r=verifyRuleSync();assert.equal(r.status,'PASS');assert.match(r.canonicalCommit,/^[a-f0-9]{40}$/);
 const text=readFileSync(join(root,'SKILL.md'),'utf8');assert.match(text,/local-agent handoff/i);
 assert.match(text,/never a fabricated/i);
});
test('snapshot tampering fails with RULE_DRIFT',async()=>{
 const dir=mkdtempSync(join(tmpdir(),'geom-sync-'));try{
  cpSync(root,dir,{recursive:true});const policy=join(dir,'references/geometry-policy.md');writeFileSync(policy,readFileSync(policy,'utf8')+'\nTAMPER\n');
  const mod=await import(pathToFileURL(join(dir,'verify-sync.mjs')).href+'?tamper=1');
  assert.throws(()=>mod.verifyRuleSync(),e=>e.code==='RULE_DRIFT');
 }finally{rmSync(dir,{recursive:true,force:true})}
});
test('valid local external canonical source matches, changed source is rejected',()=>{
 const dir=mkdtempSync(join(tmpdir(),'geom-canonical-'));try{
  const p=join(dir,'policy.md');copyFileSync(join(root,'references/geometry-policy.md'),p);
  assert.equal(verifyRuleSync(p).canonicalCompared,true);writeFileSync(p,'fake policy');
  assert.throws(()=>verifyRuleSync(p),e=>e.code==='SOURCE_DRIFT');
 }finally{rmSync(dir,{recursive:true,force:true})}
});
test('manifest pinned source commit cannot be a floating branch',async()=>{
 const dir=mkdtempSync(join(tmpdir(),'geom-repin-'));try{
  cpSync(root,dir,{recursive:true});const path=join(dir,'sync-manifest.json');const m=JSON.parse(readFileSync(path,'utf8'));m.canonicalCommit='main';writeFileSync(path,JSON.stringify(m));
  const mod=await import(pathToFileURL(join(dir,'verify-sync.mjs')).href+'?repin=1');
  assert.throws(()=>mod.verifyRuleSync(),e=>e.code==='SOURCE_UNPINNED');
 }finally{rmSync(dir,{recursive:true,force:true})}
});
