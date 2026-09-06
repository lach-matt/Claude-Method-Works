import re
from itertools import product
LSYM="spdfghi"
NOBLE={"[He]":"1s2","[Ne]":"1s2 2s2 2p6","[Ar]":"1s2 2s2 2p6 3s2 3p6",
 "[Kr]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6",
 "[Xe]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6",
 "[Cd]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2",
 "[Hg]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2",
 "[Rn]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2 6p6"}
def subshells(cfg):
    for k,v in NOBLE.items(): cfg=cfg.replace(k,v+" ")
    out=[]
    for tok in cfg.replace("."," ").split():
        m=re.fullmatch(r"(\d)([spdfghi])(\d*)",tok)
        if m: out.append((int(m.group(1)),LSYM.index(m.group(2)),int(m.group(3) or 1)))
    return out
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
# --- parse check FIRST: Pauli must hold, 18,288 tests already say so ---------
bad=[(z,n,l,k) for z,(s,c,t) in g.GROUND.items() for n,l,k in subshells(c)
     if k>2*(2*l+1) or l>=n]
print(f"  PARSE CHECK — Pauli k <= 2(2l+1) and l <= n-1 : "
      f"{'clean' if not bad else str(len(bad))+' VIOLATIONS'}")
if bad: print("   ",bad[:5]); raise SystemExit
tot=sum(len(subshells(c)) for z,(s,c,t) in g.GROUND.items())
print(f"  subshells across 108 elements: {tot}")

# --- THE QUESTION: does ONE coordinate system close EACH species? -----------
print("\n  PER SPECIES — no pooling, no Z. does (n, l, k) close for each?\n")
res={}
for z,(sym,cfg,term) in sorted(g.GROUND.items()):
    X={(n,l,k) for n,l,k in subshells(cfg)}
    E=len(opR(X,3))-len(X); res[z]=(sym,len(X),E)
closed=[z for z in res if res[z][2]==0]
print(f"      E = 0 for {len(closed)} of {len(res)} elements")
open_=[(z,)+res[z] for z in res if res[z][2]>0]
if open_:
    print(f"      the {len(open_)} that do not close:")
    for z,sym,n,E in open_[:14]:
        print(f"         Z={z:>3} {sym:<3} cells {n:>2}  E = {E}")
    from collections import Counter
    print(f"      E values: {dict(sorted(Counter(o[3] for o in open_).items()))}")