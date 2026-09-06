import sys; sys.path.insert(0,"/home/claude/work")
from merged_triples import subshells, opR
import importlib.util as iu
sp=iu.spec_from_file_location("_g","ground.py"); g=iu.module_from_spec(sp); sp.loader.exec_module(g)
cells={(z,n,l,k) for z,(s,c,t) in g.GROUND.items() for n,l,k in subshells(c)}
def rep(lab,X,names):
    d=len(names); box=1
    for i in range(d): box*=len({x[i] for x in X})
    R=opR(X,d); E=len(R)-len(X)
    print(f"  {lab:<34} cells {len(X):>5} · box {box:>8} · density {len(X)/box:.4f} · E = {E}")
    return E,R
print("  DROPPING THE NON-AXES — c is flat, Ne is Z renamed (A.derived)\n")
E4,R4=rep("(Z, n, l, k)",cells,["Z","n","l","k"])
# and the sub-indexes, to see where the defect lives
rep("(n, l, k) — the subshell alone",{(n,l,k) for z,n,l,k in cells},["n","l","k"])
rep("(Z, n, l) — drop occupancy",{(z,n,l) for z,n,l,k in cells},["Z","n","l"])
rep("(Z, l, k)",{(z,l,k) for z,n,l,k in cells},["Z","l","k"])
rep("(Z, n, k)",{(z,n,k) for z,n,l,k in cells},["Z","n","k"])
print("\n  WHAT ℛ ADMITS AND THE TABLE DOES NOT — the defect's shape")
extra=R4-cells
from collections import Counter
print(f"      {len(extra)} cells. by l:", dict(sorted(Counter(x[2] for x in extra).items())))
print(f"      by n:", dict(sorted(Counter(x[1] for x in extra).items())))
print(f"      by k:", dict(sorted(Counter(x[3] for x in extra).items())))
ex=sorted(extra)[:6]
print("      first few:", ", ".join(f"Z={a} {b}{'spdfghi'[c]}{d}" for a,b,c,d in ex))