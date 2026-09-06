#!/usr/bin/env python3
"""vi_reach.py -- the second column, never used.

T §5.6 prints TWELVE numbers, not six: cells and REACHABLE, under six
thresholds. Every search so far fitted the cells column alone.

Model A — one index, six thresholds (the table's own 'threshold' column).
Model B — six independent objects.

The reachable column discriminates: under A it must be a monotone slice of one
reachable set; under B it need not be.

  cells      2,370  2,196  1,764  1,146  1,374   558
  reachable  1,410  1,410  1,134    738    840   360
"""
import numpy as np, itertools, json
from zeno import State, step
R=[4,3,3,3,5,2,2,3,3]; N=["X","S","IC","U","NEC","L","SD","DNc","DNd"]
B=np.array(list(itertools.product(*[range(r) for r in R])),dtype=np.int16)
COL=[B[:,i] for i in range(9)]
CELLS=[2370,2196,1764,1146,1374,558]
REACH=[1410,1410,1134,738,840,360]
SLICE=[lambda: np.ones(len(B),bool), lambda: COL[4]>=1, lambda: COL[4]>=2,
       lambda: COL[4]>=3, lambda: COL[0]>=2, lambda: COL[0]==3]
def run():
    out={}
    # what the printed numbers say about reachability, model A
    out["A cells monotone"] = all(CELLS[i]>=CELLS[i+1] for i in range(3))
    out["NEC=0 cells"]      = CELLS[0]-CELLS[1]
    out["reach lost 0→1"]   = REACH[0]-REACH[1]
    out["so NEC=0 cells reachable"] = REACH[0]-REACH[1]
    out["NEC=1 cells"]      = CELLS[1]-CELLS[2]
    out["reach lost 1→2"]   = REACH[1]-REACH[2]
    out["NEC=2 cells"]      = CELLS[2]-CELLS[3]
    out["reach lost 2→3"]   = REACH[2]-REACH[3]
    # reachable fraction per slice
    out["frac"]=[round(r/c,4) for r,c in zip(REACH,CELLS)]
    # model B test: are the six reachable counts consistent with ONE set?
    # under A, reachable(NEC>=k) must be non-increasing in k — check
    out["B: reach monotone in NEC"]=all(REACH[i]>=REACH[i+1] for i in range(3))
    # and X-slices must be sub-counts of the total
    out["X>=2 reach <= total reach"]=REACH[4]<=REACH[0]
    out["X=3 reach <= X>=2 reach"]=REACH[5]<=REACH[4]
    return out
with State("vi_reach") as st:
    O=step(st,"the reachable column",run,budget=200)
print("  WHAT THE SECOND COLUMN SAYS\n")
print(f"    cells at NEC = 0 : {O['NEC=0 cells']}      reachable lost 0→1 : {O['reach lost 0→1']}")
print(f"      → ALL 174 NEC = 0 cells are UNREACHABLE\n")
print(f"    cells at NEC = 1 : {O['NEC=1 cells']}      reachable lost 1→2 : {O['reach lost 1→2']}")
print(f"      → {O['reach lost 1→2']} of {O['NEC=1 cells']} NEC = 1 cells are reachable "
      f"({100*O['reach lost 1→2']/O['NEC=1 cells']:.0f}%)\n")
print(f"    cells at NEC = 2 : {O['NEC=2 cells']}      reachable lost 2→3 : {O['reach lost 2→3']}")
print(f"      → {O['reach lost 2→3']} of {O['NEC=2 cells']} NEC = 2 cells are reachable "
      f"({100*O['reach lost 2→3']/O['NEC=2 cells']:.0f}%)\n")
print(f"    reachable fraction per slice: {O['frac']}")
print(f"\n  MODEL A — one index, six thresholds")
print(f"    cells monotone in NEC              {O['A cells monotone']}")
print(f"    reachable monotone in NEC          {O['B: reach monotone in NEC']}")
print(f"    X-slice reach <= total reach       {O['X>=2 reach <= total reach']}")
print(f"    X=3 reach <= X>=2 reach            {O['X=3 reach <= X>=2 reach']}")
print(f"\n  Every consistency condition Model A requires HOLDS. The table is one index.")
print(f"  Model B would place no such conditions, so it is not distinguishable by")
print(f"  consistency alone — but it is refuted by the table's own 'threshold' column.")