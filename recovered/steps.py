import re
from itertools import product
LSYM="spdfghi"
NOBLE={"[He]":"1s2","[Ne]":"1s2 2s2 2p6","[Ar]":"1s2 2s2 2p6 3s2 3p6",
 "[Kr]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6",
 "[Xe]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6",
 "[Cd]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2",
 "[Hg]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2",
 "[Rn]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2 6p6"}
def occ(cfg):
    for k,v in NOBLE.items(): cfg=cfg.replace(k,v+" ")
    d={}
    for tok in cfg.replace("."," ").split():
        m=re.fullmatch(r"(\d)([spdfghi])(\d*)",tok)
        if m: d[(int(m.group(1)),LSYM.index(m.group(2)))]=int(m.group(3) or 1)
    return d
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
G={z:occ(c) for z,(s,c,t) in g.GROUND.items()}
steps=[]; anom=[]
for z in range(2,max(G)+1):
    if z not in G or z-1 not in G: continue
    a,b=G[z-1],G[z]
    gain=[(k,b[k]-a.get(k,0)) for k in b if b[k]>a.get(k,0)]
    loss=[(k,a[k]-b.get(k,0)) for k in a if a[k]>b.get(k,0)]
    if len(gain)==1 and not loss:
        (n2,l2),d=gain[0]
        steps.append((z,None,None,n2,l2,b[(n2,l2)]))     # simple entry
    else:
        anom.append((z,g.GROUND[z][0],gain,loss))
        for (n2,l2),d in gain:
            steps.append((z,None,None,n2,l2,b[(n2,l2)]))
print(f"  steps built: {len(steps)}   ANOMALOUS (a shell also emptied): {len(anom)}")
for z,s,gn,ls in anom[:6]:
    fmt=lambda t:", ".join(f"{a}{LSYM[b]}{'+' if c>0 else ''}{c}" for (a,b),c in t)
    print(f"      Z={z:>3} {s:<3} gains {fmt(gn):<16} loses {fmt(ls)}")
print(f"\n  THE STEP INDEX — the cell is a MOVE, not a state")
S={(n2,l2,k2) for z,_,_,n2,l2,k2 in steps}
for lab,X,d in (("(n, l, k) of the subshell ENTERED",S,3),
                ("(Z, n, l) of the entry",{(z,n2,l2) for z,_,_,n2,l2,k2 in steps},3),
                ("(Z, n, l, k)",{(z,n2,l2,k2) for z,_,_,n2,l2,k2 in steps},4)):
    box=1
    for i in range(d): box*=len({x[i] for x in X})
    print(f"      {lab:<36} cells {len(X):>4} · box {box:>7} · E = {len(opR(X,d))-len(X)}")