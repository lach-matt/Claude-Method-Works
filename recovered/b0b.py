import sys, re, math; sys.path.insert(0,"/home/claude/work")
import ground as G
from itertools import product
LS="spdfghi"; cap=lambda l:2*(2*l+1)
NOBLE={"[He]":"1s2","[Ne]":"1s2 2s2 2p6","[Ar]":"1s2 2s2 2p6 3s2 3p6",
 "[Kr]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6",
 "[Xe]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6",
 "[Cd]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2",
 "[Hg]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2",
 "[Rn]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2 6p6"}
def subsh(cfg):
    for k,v in NOBLE.items(): cfg=cfg.replace(k,v+" ")
    return [(int(m.group(1)),LS.index(m.group(2)),int(m.group(3) or 1))
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
HELD={t for z,(s,c,tm) in G.GROUND.items() for t in subsh(c)}
EX=sorted(opR(HELD,3)-HELD)
MAD=sorted(((n,l) for n in range(1,9) for l in range(0,min(n,5))),
           key=lambda t:(t[0]+t[1],t[0]))
def min_Ne(n,l,k):
    tot=0
    for a,b in MAD:
        if (a,b)==(n,l): return tot+k
        tot+=cap(b)
    return 10**9
print("  B0b — Λ_spectra's LIMIT RECOUNTED AGAINST 120\n")
print(f"  {'limit Z':>9}{'beyond':>9}{'within':>9}   what the within-limit cells are")
for LIM,lab in ((108,"R 1395's edge — the last SYNTHESISED element then"),
                (118,"oganesson, the last synthesised today"),
                (120,"the INDEX's edge — Janet's block 8 complete")):
    ins=[t for t in EX if min_Ne(*t)<=LIM]
    print(f"  {LIM:>9}{len(EX)-len(ins):>9}{len(ins):>9}   {lab}")
print()
for LIM in (108,118,120):
    ins=[t for t in EX if min_Ne(*t)<=LIM]
    print(f"  at limit {LIM}: " + ", ".join(f"{a}{LS[b]}{c}" for a,b,c in ins))
print("\n  the cells that ENTER as the limit rises from 108 to 120:")
a108={t for t in EX if min_Ne(*t)<=108}; a120={t for t in EX if min_Ne(*t)<=120}
for t in sorted(a120-a108):
    print(f"      {t[0]}{LS[t[1]]}{t[2]}   needs Nₑ = {min_Ne(*t)}")