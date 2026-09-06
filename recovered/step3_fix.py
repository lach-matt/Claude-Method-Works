#!/usr/bin/env python3
"""step3_fix.py -- Session 8. Recompute the rule-B (charge 1) column of step3 with the adaptive floor.
E_A rows are untouched by the repair (0 at floor in pack-5; bracket unchanged => bit-identical), so only
E_B is recomputed. Output step3B_fixed.jsonl (resume per Z); compare against pack-5 step3_rows.jsonl.
"""
import sys, json, os, tfd, ground as G
import step2_run; import eigen_fix; from eigen_fix import eigen
from step3 import steps, L
old={}
for line in open('step3_rows.jsonl'): r=json.loads(line); old[r['Z']]=r
done={}
if os.path.exists('step3B_fixed.jsonl'):
    for line in open('step3B_fixed.jsonl'): r=json.loads(line); done[r['Z']]=r
zlo,zhi=int(sys.argv[1]),int(sys.argv[2])
for Z,pr,obs,cand in steps():
    if Z in done or not (zlo<=Z<=zhi): continue
    V,x0=tfd.potential(Z,1); Es={}; deep={}
    for n,l in cand:
        Es[(n,l)]=eigen(V,l,n,1,Z); deep[(n,l)]=eigen.last_deepened
    eB=min(Es,key=Es.get); o=old[Z]
    r=dict(Z=Z,el=o['el'],obs=o['obs'],B=f"{eB[0]}{L[eB[1]]}",hitB=eB==obs,
           EB={f"{n}{L[l]}":round(v,5) for (n,l),v in Es.items()},
           deepened={f"{n}{L[l]}":d for (n,l),d in deep.items() if d},
           EB_old=o['EB'],B_old=o['B'],changed=any(abs(Es[(n,l)]-o['EB'][f"{n}{L[l]}"])>1e-4 for n,l in cand))
    open('step3B_fixed.jsonl','a').write(json.dumps(r)+'\n')
    print(f"{Z:3d} {r['el']:3s} B {r['B']:3s}{'✓' if r['hitB'] else '✗'} old {o['B']:3s} {'CHANGED '+str(r['deepened']) if r['changed'] else ''}",flush=True)