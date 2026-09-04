#!/usr/bin/env python3
"""z_index.py -- what happens when the periodic table's own numbers enter Λ.

Register 628: Λ's eight axes are internal to one atom. There is no Z. Matthew's
point is that the mathematics is controlled by the real atomic numbers, so the
test is what an index over (Z, transition) does that an index over transitions
alone cannot.

Built from the 118 real ground-state configurations already used for the 18,288
constraint tests: a cell is (Z, n, l, k, q, e, f, g) where the source subshell
(n,l) really holds k in element Z, and the target (e,f) really exists in Z.

COMMITTED (§2.13): E stays 0 because Z is a free coordinate no constraint
references; composability RISES, because a target that no transition in one
element can start may be a legal source in another.
"""
import itertools, importlib.util as iu, sys
from collections import Counter
from zeno import State, step

_sp=iu.spec_from_file_location("_cl","close_L118.py"); _m=iu.module_from_spec(_sp)
_old=sys.exit; sys.exit=lambda *a: None
try: _sp.loader.exec_module(_m)
except Exception: pass
sys.exit=_old
ELEMENTS, LMAP = _m.C, _m.L

def clos(X,d):
    X=list(X); A=[sorted({c[i] for c in X}) for i in range(d)]
    def e(a,b):
        m={}
        for c in X: m[c[b]]=max(m.get(c[b],-99),c[a])
        z=-99;o={}
        for t in sorted(m): z=max(z,m[t]); o[t]=z
        return o
    ph={(a,b):e(a,b) for a in range(d) for b in range(d) if a!=b}
    return {x for x in itertools.product(*A)
            if all(x[a]<=ph[(a,b)][x[b]] for a in range(d) for b in range(d) if a!=b)}

def run():
    # every element's occupied subshells
    occ={Z:{(n,LMAP[s]):k for (n,s,k) in sh} for Z,(sym,sh) in ELEMENTS.items()}
    cells=[]
    for Z,sub in occ.items():
        for (n,l),k in sub.items():
            for (e,f),gcap in sub.items():
                if (n,l)==(e,f): continue
                for q in range(1,k+1):
                    for g in range(1,min(q,4*f+2)+1):
                        cells.append((Z,n,l,k,q,e,f,g))
    X=set(cells)
    out={"cells":len(X),"elements":len(occ)}
    # E with Z, and E on the same cells with Z stripped
    out["E with Z"]=len(clos(X,8))-len(X)
    Y={c[1:] for c in X}
    out["cells without Z"]=len(Y)
    out["E without Z"]=len(clos(Y,7))-len(Y)
    # composability: target (e,f,g) is some cell's source (n,l,k)
    #   WITHIN one element, and ACROSS all elements
    within=0
    for Z in occ:
        S={(c[1],c[2],c[3]) for c in X if c[0]==Z}
        within+=sum(1 for c in X if c[0]==Z and (c[5],c[6],c[7]) in S)
    across_S={(c[1],c[2],c[3]) for c in X}
    across=sum(1 for c in X if (c[5],c[6],c[7]) in across_S)
    out["composable within one element"]=within
    out["composable across elements"]=across
    return out

with State("z_index") as st:
    O=step(st,"the periodic table's numbers as a coordinate",run,budget=1500)

n=O["cells"]
print(f"  {O['elements']} elements → {n:,} cells (Z, n, l, k, q, e, f, g)\n")
print(f"  {'E with Z as a coordinate':<36}{O['E with Z']:>10,}")
print(f"  {'cells with Z stripped':<36}{O['cells without Z']:>10,}")
print(f"  {'E without Z':<36}{O['E without Z']:>10,}\n")
w,a=O["composable within one element"],O["composable across elements"]
print(f"  {'composable WITHIN one element':<36}{w:>10,}   {w/n:.4f}")
print(f"  {'composable ACROSS elements':<36}{a:>10,}   {a/n:.4f}")
print(f"  {'gained by allowing another element':<36}{a-w:>10,}   {(a-w)/n:+.4f}")
