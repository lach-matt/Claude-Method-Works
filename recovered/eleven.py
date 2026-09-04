import re
from itertools import product
LSYM="spdfghi"
NOBLE={"[He]":"1s2","[Ne]":"1s2 2s2 2p6","[Ar]":"1s2 2s2 2p6 3s2 3p6",
 "[Kr]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6",
 "[Xe]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6",
 "[Cd]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2",
 "[Hg]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2",
 "[Rn]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2 6p6"}
def subsh(cfg):
    for k,v in NOBLE.items(): cfg=cfg.replace(k,v+" ")
    return [(int(m.group(1)),LSYM.index(m.group(2)),int(m.group(3) or 1))
            for m in (re.fullmatch(r"(\d)([spdfghi])(\d*)",t) for t in cfg.replace("."," ").split()) if m]
def opR(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
import importlib.util as iu
sp=iu.spec_from_file_location("_g","ground.py"); g=iu.module_from_spec(sp); sp.loader.exec_module(g)
HELD={t for z,(s,c,tm) in g.GROUND.items() for t in subsh(c)}

# THE LIMIT: no atom exists past Z = 108, so a cell needing more electrons than
# the heaviest species holds is BEYOND THE LIMIT, not a defect. The smallest
# electron count that reaches (n,l,k) is the Madelung position of that subshell
# plus k. Cap at max(Z) = 108.
def madelung_order():
    return sorted(((n,l) for n in range(1,9) for l in range(0,min(n,5))),
                  key=lambda t:(t[0]+t[1], t[0]))
ORD=madelung_order()
def min_Ne(n,l,k):
    tot=0
    for a,b in ORD:
        if (a,b)==(n,l): return tot+k
        tot+=2*(2*b+1)
    return 10**9
LIM=max(g.GROUND)
EX=sorted(opR(HELD,3)-HELD)
inside=[t for t in EX if min_Ne(*t)<=LIM]
beyond=[t for t in EX if min_Ne(*t)> LIM]
print(f"  E before the limit is applied : {len(EX)}")
print(f"     beyond Z = {LIM} (no atom can hold them) : {len(beyond)}")
print(f"     WITHIN the limit — the true defect       : {len(inside)}\n")
print(f"  {'cell':>6}{'needs Ne':>10}   the named cause")
CAUSE={(3,2,4):"Cr 3d5 4s1 — half-filled d, Hund exchange",
 (3,2,9):"Cu 3d10 4s1 — filled d",
 (4,2,3):"Nb 4d4 5s1 — d-block, s donates",
 (4,2,6):"Ru 4d7 5s1 — d-block, s donates",
 (4,2,9):"Ag 4d10 5s1 — filled d",
 (4,3,2):"Ce 4f1 5d1 — f-block opening, d preferred",
 (4,3,8):"Gd 4f7 5d1 — half-filled f, Hund exchange",
 (5,2,8):"Pt 5d9 6s1 — d near-filled",
 (5,3,1):"Ac 6d1, no 5f — f-block opening (Q.collapse Z=89)",
 (5,3,5):"Np 5f4 6d1 — f-block, d preferred",
 (5,3,8):"Cm 5f7 6d1 — half-filled f, Hund exchange"}
for t in inside:
    print(f"  {t[0]}{LSYM[t[1]]}{t[2]:<4}{min_Ne(*t):>10}   {CAUSE.get(t,'UNACCOUNTED')}")
un=[t for t in inside if t not in CAUSE]
print(f"\n  accounted: {len(inside)-len(un)} of {len(inside)}   unaccounted: {len(un)}")
from collections import Counter
kind=Counter("half/full shell (Hund)" if t in ((3,2,4),(3,2,9),(4,2,9),(4,3,8),(5,3,8),(5,2,8)) else
             "block opening (d preferred)" for t in inside)
print(f"  by mechanism: {dict(kind)}")