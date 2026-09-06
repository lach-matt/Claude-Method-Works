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

print("  THE LIMIT — the index runs to the last available species and stops.\n")
print("  Λ is complete at 976 because its coordinates are bounded by the physics.")
print("  Λ_spectra is infinite unless capped. Cap it at what EXISTS.\n")
U={t for z,(s,c,tm) in g.GROUND.items() for t in subsh(c)}
for lab,X,d in (("(n, l, k) — every subshell any atom holds", U, 3),
                ("(n, l)    — the subshells themselves", {(a,b) for a,b,_ in U}, 2)):
    box=1
    for i in range(d): box*=len({x[i] for x in X})
    R=opR(X,d); E=len(R)-len(X)
    print(f"  {lab:<44} cells {len(X):>3} · box {box:>5} · E = {E}")
    if E and d==3:
        ex=sorted(R-X)
        print(f"      ℛ admits and no atom holds: "
              + ", ".join(f"{a}{LSYM[b]}{c}" for a,b,c in ex[:10])
              + (f" ... +{len(ex)-10}" if len(ex)>10 else ""))
        # are they excluded by PAULI, or genuinely absent?
        pauli=[t for t in ex if t[2]>2*(2*t[1]+1) or t[1]>=t[0]]
        print(f"      of those, {len(pauli)} violate Pauli or l<=n-1 — i.e. they")
        print(f"      are cells Λ's OWN CONSTRAINTS already refuse, not defects")
        rest=[t for t in ex if t not in pauli]
        print(f"      genuinely admitted-and-absent: {len(rest)}")
        if rest: print("        ", ", ".join(f"{a}{LSYM[b]}{c}" for a,b,c in rest[:12]))