#!/usr/bin/env python3
"""testA.py -- session 9. Fixed-outer-shell row scan under the SCF kernel. Resumable: testA.jsonl."""
import sys, json, os, numpy as np, warnings; warnings.filterwarnings("ignore")
import hfs, ground as G
L="spdfg"
CORE={"Ar":[(1,0,2),(2,0,2),(2,1,6),(3,0,2),(3,1,6)],
      "Kr":[(1,0,2),(2,0,2),(2,1,6),(3,0,2),(3,1,6),(3,2,10),(4,0,2),(4,1,6)],
      "Xe":[(1,0,2),(2,0,2),(2,1,6),(3,0,2),(3,1,6),(3,2,10),(4,0,2),(4,1,6),(4,2,10),(5,0,2),(5,1,6)],
      "Rn":[(1,0,2),(2,0,2),(2,1,6),(3,0,2),(3,1,6),(3,2,10),(4,0,2),(4,1,6),(4,2,10),(5,0,2),(5,1,6),(4,3,14),(5,2,10),(6,0,2),(6,1,6)]}
ROWS=[("3d","Ar",21,29,(4,0,1)),("4d","Kr",39,47,(5,0,1)),("4f","Xe",57,70,(6,0,2)),("5f","Rn",89,102,(7,0,2))]
def occ_for(sh,core,Z,zlo,outer):
    n,l=int(sh[0]),L.index(sh[1]); N=Z-zlo; base=CORE[core]+[outer]
    tot=sum(k for *_,k in base)+N
    assert tot==Z-1,(sh,Z,tot)
    return base+([(n,l,N)] if N>0 else [])
done={(r["sh"],r["Z"]) for r in map(json.loads,open("testA.jsonl"))} if os.path.exists("testA.jsonl") else set()
zlo,zhi=int(sys.argv[1]),int(sys.argv[2])
for sh,core,a,b,outer in ROWS:
    for Z in range(max(a,zlo),min(b,zhi)+1):
        if (sh,Z) in done: continue
        occ=occ_for(sh,core,Z,a,outer)
        G_expand=G.expand; G.expand=lambda N,_o=occ:_o
        try:
            Vf,Es,hist,(r,dr,Vg)=hfs.scf(Z,1)
        finally: G.expand=G_expand
        n,l=int(sh[0]),L.index(sh[1])
        rr,drr,u,E,nd=hfs.numerov_wf(Vf,l,n,1.0,Z)
        row=dict(sh=sh,Z=Z,N=Z-a,E=round(float(E),5),nodes=int(nd),it=len(hist),conv=hist[-1])
        open("testA.jsonl","a").write(json.dumps(row)+"\n"); print(row,flush=True)