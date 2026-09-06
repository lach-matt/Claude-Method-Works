#!/usr/bin/env python3
"""step3.py -- Session 5. Entrants from TFD, two core rules, held out. M's ruling (c): both, report.
Step: Z-1 -> Z where exactly one subshell gains (brack.py definition; 106 steps).
Candidates: per l, lowest n with occ < cap in Z-1's configuration (brack.py cand).
Rule A (closed core, rung C generalised): core = full subshells of Z-1 config minus its outermost s;
        charge = Z - N_core.  Reproduces Sc III, Y III, La III, Ce IV, Ac III, Th IV, Lr III.
Rule B (charge 1): core = all Z-1 electrons; charge = 1.
Entrant = argmin over candidates of the TFD one-electron eigenvalue E(n,l) at (Z, charge).
Held out: nothing from the observed entrant enters the prediction.
Kernel = step2_run.py (gate-checked relaxed tolerances).
"""
import sys, json, numpy as np, ground as G, tfd
from step2_run import eigen   # patches tfd tolerances on import
L="spdfg"; cap=lambda l:2*(2*l+1)
def steps():
    for Z in range(3,109):
        pr={(n,l):o for n,l,o in G.expand(Z-1)}; cu={(n,l):o for n,l,o in G.expand(Z)}
        got=[k for k in cu if cu[k]>pr.get(k,0)]
        if len(got)!=1: continue
        cand=[]
        for l in range(5):
            for n in range(l+1,9):
                if pr.get((n,l),0)>=cap(l): continue
                cand.append((n,l))
                if pr.get((n,l),0)==0: break
        if got[0] not in cand or len(cand)<2: continue
        yield Z,pr,got[0],cand
def coreA(pr):
    full=[(n,l,o) for (n,l),o in pr.items() if o>=cap(l)]
    outer_s=max((n for n,l,o in full if l==0),default=None)
    return sum(o for n,l,o in full if not (l==0 and n==outer_s))
def pick(Z,ch,cand):
    V,x0=tfd.potential(Z,ch); Es={}
    for n,l in cand: Es[(n,l)]=eigen(V,l,n,ch,Z)
    return min(Es,key=Es.get),Es
if __name__=="__main__":
    res=[]
    for Z,pr,obs,cand in steps():
        NA=coreA(pr); chA=Z-NA; chB=1
        eA,EsA=pick(Z,chA,cand); eB,EsB=pick(Z,chB,cand)
        r=dict(Z=Z,el=G.GROUND[Z][0],obs=f"{obs[0]}{L[obs[1]]}",chargeA=chA,A=f"{eA[0]}{L[eA[1]]}",B=f"{eB[0]}{L[eB[1]]}",
               hitA=eA==obs,hitB=eB==obs,agree=eA==eB,cand=[f"{n}{L[l]}" for n,l in cand],
               EA={f"{n}{L[l]}":round(v,5) for (n,l),v in EsA.items()},EB={f"{n}{L[l]}":round(v,5) for (n,l),v in EsB.items()})
        res.append(r); print(f"{Z:3d} {r['el']:3s} obs {r['obs']:3s} A[{chA:2d}] {r['A']:3s} {'✓' if r['hitA'] else '✗'}  B[1] {r['B']:3s} {'✓' if r['hitB'] else '✗'}  {'' if r['agree'] else 'DISAGREE'}",flush=True)
    n=len(res); print(f"\nsteps {n}  A hits {sum(r['hitA'] for r in res)}  B hits {sum(r['hitB'] for r in res)}  A=B on {sum(r['agree'] for r in res)}  disagree {n-sum(r['agree'] for r in res)}")
    json.dump(res,open('step3.json','w'),indent=0)