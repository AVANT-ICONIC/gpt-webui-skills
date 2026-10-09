#!/usr/bin/env node
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
const root=dirname(fileURLToPath(import.meta.url));
const digest=s=>createHash('sha256').update(s).digest('hex');
const fail=(code,message)=>{const e=new Error(message);e.code=code;throw e};
export function verifyRuleSync(canonicalPath=null){
 const m=JSON.parse(readFileSync(join(root,'sync-manifest.json'),'utf8'));
 if(m.schema!=='geometric-design-rule-sync/1'||m.policyVersion!=='geometry-policy/1')fail('MANIFEST_INVALID','Unsupported synchronization schema');
 if(m.canonicalRepository!=='AVANT-ICONIC/skills'||m.canonicalPath!=='geometric-design/references/geometry-policy.md'|| !/^[a-f\d]{40}$/.test(m.canonicalCommit))fail('SOURCE_UNPINNED','Canonical repo commit must be immutable 40-digit git SHA');
 if(!/^[a-f\d]{64}$/.test(m.canonicalSha256)||m.snapshotSha256!==m.canonicalSha256)fail('MANIFEST_INVALID','Expected identical 64-hex SHA-256');
 const vendored=readFileSync(join(root,'references/geometry-policy.md'),'utf8');
 if(digest(vendored)!==m.snapshotSha256)fail('RULE_DRIFT','WebUI snapshot has changed');
 if(canonicalPath){const upstream=readFileSync(resolve(canonicalPath),'utf8');if(digest(upstream)!==m.canonicalSha256||upstream!==vendored)fail('SOURCE_DRIFT','Portable canonical source differs from vendored rules');}
 return {status:'PASS',canonicalCommit:m.canonicalCommit,policySha256:m.canonicalSha256,canonicalCompared:Boolean(canonicalPath)};
}
if(process.argv[1]&&resolve(process.argv[1])===resolve(fileURLToPath(import.meta.url))){
 try{console.log(JSON.stringify(verifyRuleSync(process.argv[2]??null)))}catch(e){console.error(JSON.stringify({status:'FAIL',code:e.code??'INVALID_INPUT',message:e.message}));process.exitCode=1}
}
