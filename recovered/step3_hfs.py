#!/usr/bin/env python3
"""step3_hfs.py -- Session 8. step3 (rule A closed core / rule B charge 1) rerun with the self-consistent
orbital-density kernel (hfs.scf), same candidate lists, same held-out scoring. Resumable: step3_hfs.jsonl."""
import sys, json, os, numpy as np, warnings; warnings.filterwarnings("ignore")
import ground as G
from hfs import scf, numerov_wf, L
from step3 import steps, coreA
def pick(Z,ch,cand):
    Vf,Es,hist,_=scf(Z,ch); E={}
    for n,l in cand: E[(n,l)]=float(numerov_wf(Vf,l,n,1.0,Z)[3])
    return min(E,key=E.get),E,len(hist),hist[-1]
done={}
if os.path.exists('step3_hfs.jsonl'):
    for line in open('step3_hfs.jsonl'): r=json.loads(line); done[r['Z']]=r
zlo,zhi=int(sys.argv[1]),int(sys.argv[2])
for Z,pr,obs,cand in steps():
    if Z in done or not (zlo<=Z<=zhi): continue
    NA=coreA(pr); chA=Z-NA
    try:
        eA,EsA,itA,dA=pick(Z,chA,cand); eB,EsB,itB,dB=pick(Z,1,cand)
    except Exception as ex:
        open('step3_hfs.jsonl','a').write(json.dumps(dict(Z=Z,el=G.GROUND[Z][0],error=str(ex)))+'\n'); print(Z,"ERR",ex,flush=True); continue
    r=dict(Z=Z,el=G.GROUND[Z][0],obs=f"{obs[0]}{L[obs[1]]}",chargeA=chA,A=f"{eA[0]}{L[eA[1]]}",B=f"{eB[0]}{L[eB[1]]}",
           hitA=eA==obs,hitB=eB==obs,itA=itA,itB=itB,dA=dA,dB=dB,
           EA={f"{n}{L[l]}":round(v,5) for (n,l),v in EsA.items()},EB={f"{n}{L[l]}":round(v,5) for (n,l),v in EsB.items()})
    open('step3_hfs.jsonl','a').write(json.dumps(r)+'\n')
    print(f"{Z:3d} {r['el']:3s} obs {r['obs']:3s} A[{chA:2d}] {r['A']:3s} {'✓' if r['hitA'] else '✗'}  B {r['B']:3s} {'✓' if r['hitB'] else '✗'}",flush=True)