#!/usr/bin/env python3
"""em_compose.py -- does the electromagnetic index mediate composability?

Register 629: composability is 22.7% within one element and 85.2% across the
table. Matthew's question is what carries the exchange — charge, or frequency.

The book's electromagnetic quotient (§12.11.8) is a filter on these same cells:
|dl| = 1 for a dipole transition, dS = 0 for spin, and parity. If EM mediates
composition, EM-allowed cells should compose at a different rate from forbidden
ones.

COMMITTED (§2.13): EM-allowed cells compose at a HIGHER rate, because the
selection rules pick out transitions the shell structure actually connects.
"""
import importlib.util as iu, sys
from collections import Counter
from zeno import State, step

_sp=iu.spec_from_file_location("_cl","close_L118.py"); _m=iu.module_from_spec(_sp)
_o=sys.exit; sys.exit=lambda *a: None
try: _sp.loader.exec_module(_m)
except Exception: pass
sys.exit=_o
ELEMENTS, LMAP = _m.C, _m.L

def run():
    occ={Z:{(n,LMAP[s]):k for (n,s,k) in sh} for Z,(sym,sh) in ELEMENTS.items()}
    cells=[]
    for Z,sub in occ.items():
        for (n,l),k in sub.items():
            for (e,f),_ in sub.items():
                if (n,l)==(e,f): continue
                for q in range(1,k+1):
                    for g in range(1,min(q,4*f+2)+1):
                        cells.append((Z,n,l,k,q,e,f,g))
    X=set(cells)
    dip = lambda c: abs(c[6]-c[2])==1                    # |dl| = 1
    par = lambda c: (c[6]-c[2])%2==1                     # parity changes
    dn  = lambda c: c[5]!=c[1]                           # the shell changes
    S_all={(c[1],c[2],c[3]) for c in X}
    def rate(sub, S):
        if not sub: return 0,0,0.0
        c=sum(1 for x in sub if (x[5],x[6],x[7]) in S)
        return len(sub),c,c/len(sub)
    out={}
    for lbl,pred in (("ALL cells",lambda c: True),
                     ("EM-allowed  |dl| = 1",dip),
                     ("EM-forbidden |dl| != 1",lambda c: not dip(c)),
                     ("parity-changing",par),
                     ("parity-conserving",lambda c: not par(c)),
                     ("shell-changing  dn != 0",dn),
                     ("same shell  dn = 0",lambda c: not dn(c))):
        sub=[c for c in X if pred(c)]
        out["across "+lbl]=rate(sub,S_all)
        w=0
        for Z in occ:
            SZ={(c[1],c[2],c[3]) for c in X if c[0]==Z}
            w+=sum(1 for c in sub if c[0]==Z and (c[5],c[6],c[7]) in SZ)
        out["within "+lbl]=(len(sub),w,w/len(sub) if sub else 0.0)
    return out

with State("em_compose") as st:
    O=step(st,"does EM mediate composability",run,budget=1500)

print(f"  {'population':<26}{'cells':>8}{'within':>9}{'rate':>8}{'across':>9}{'rate':>8}")
for lbl in ["ALL cells","EM-allowed  |dl| = 1","EM-forbidden |dl| != 1",
            "parity-changing","parity-conserving","shell-changing  dn != 0","same shell  dn = 0"]:
    n,w,wr=O["within "+lbl]; _,a,ar=O["across "+lbl]
    print(f"  {lbl:<26}{n:>8,}{w:>9,}{wr:>8.3f}{a:>9,}{ar:>8.3f}")