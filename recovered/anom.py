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
HELD={t for z,(s,c,tm) in g.GROUND.items() for t in subsh(c)}
EX=sorted(opR(HELD,3)-HELD)

# --- MADELUNG: what the n+l rule says each atom should hold ------------------
def madelung(Ne):
    order=sorted(((n,l) for n in range(1,9) for l in range(0,min(n,5))),
                 key=lambda t:(t[0]+t[1], t[0]))
    cfg={}; left=Ne
    for n,l in order:
        if left<=0: break
        take=min(left,2*(2*l+1)); cfg[(n,l)]=take; left-=take
    return cfg
PRED={t for z in g.GROUND for t in
      ((n,l,k) for (n,l),k in madelung(z).items())}

print("  WHAT IS LEFT — the 58 admitted-and-absent cells\n")
by_pred = [t for t in EX if t in PRED]
print(f"  of the {len(EX)} absent cells, {len(by_pred)} ARE predicted by the n+l rule")
print(f"  and never observed — i.e. they are exactly where Madelung is WRONG.\n")
print(f"  {'cell':>6}  {'Madelung says':<22}{'observed instead':<24}")
for n,l,k in by_pred:
    zs=[z for z in g.GROUND if madelung(z).get((n,l))==k]
    for z in zs[:1]:
        sym,cfg,_=g.GROUND[z]
        got=dict(((a,b),c) for a,b,c in subsh(cfg)).get((n,l),0)
        print(f"  {n}{LSYM[l]}{k:<3}  Z={z:<3} {sym:<3} predicted"
              f"{'':<4}{n}{LSYM[l]}{got} observed")
rest=[t for t in EX if t not in PRED]
print(f"\n  the other {len(rest)} are absent from BOTH the observed table and the")
print(f"  n+l prediction — never reached by either:")
print("     " + ", ".join(f"{a}{LSYM[b]}{c}" for a,b,c in rest[:18]))