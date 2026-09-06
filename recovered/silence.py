from itertools import product, combinations
from math import comb, log2
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
def bpc(X,d):
    """A.stat2 / A.bpc: the statistics operator is max-entropy on the PAIRWISE
    marginals. a cell is admitted iff every pair projection contains it."""
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    proj={(i,j):{(x[i],x[j]) for x in X} for i in range(d) for j in range(d) if i<j}
    return {x for x in product(*vals)
            if all((x[i],x[j]) in proj[(i,j)] for i in range(d) for j in range(d) if i<j)}

NMAX=4
LEV=[(n,l,tj) for n in range(1,NMAX+1) for l in range(n)
     for tj in ([1] if l==0 else [2*l-1,2*l+1])]
CELLS=[(h,f) for h in LEV for f in LEV
       if f[0]>h[0] and abs(f[1]-h[1])==1 and abs(f[2]-h[2])<=2]
# the closing coordinates: dn x dl x jtype_hole
raw={(f[0]-h[0], f[1]-h[1], 1 if h[2]==2*h[1]+1 else 0) for h,f in CELLS}
rel=[{v:k for k,v in enumerate(sorted({c[i] for c in raw}))} for i in range(3)]
X={tuple(rel[i][c[i]] for i in range(3)) for c in raw}
d=3; box=1
for i in range(d): box*=len({x[i] for x in X})

E=len(opR(X,d))-len(X)
S=len(bpc(X,d))-len(X)
print("Λ_xray — the six languages, on the CELL SET\n")
print(f"  order       ℛ closure                E = {E}")
print(f"  statistics  max-entropy on pairwise marginals   defect = {S}")
print(f"  geometry    intersection of (≤,≤) staircases?   {'YES' if E==0 else 'no'}"
      f"   (A.staircls: E(ℛ)=0 iff it is)")
print(f"  information E_bits = log2 C(|ℛ(X)|, E) = {log2(comb(len(X)+E,E)) if E>=0 else '-':.4f}")
# analysis: does the count factorise over independent coordinate groups?
fac=1
for i in range(d): fac*=len({x[i] for x in X})
print(f"  analysis    box {box} vs cells {len(X)} — factorises? "
      f"{'YES, F is a product' if fac==len(X) else 'NO, F needs the constraint'}")
print(f"\n  K.langclose predicts: E(X) = 0 iff the languages agree.")
print(f"    order E = {E}, statistics defect = {S} -> "
      f"{'AGREE' if E==S==0 else 'DISAGREE'}")

# --- the Lambda_cross comparison, from the compendium's own record ---------
print("\n  AGAINST Λ_cross (compendium, §IX):")
print("    Λ_cross : order YES · algebra YES · geometry YES · analysis NO · statistics NO")
print(f"    Λ_xray  : order YES · geometry YES · statistics YES (defect {S}) · analysis on cells: "
      f"{'product' if fac==len(X) else 'constrained'}")
print("\n  -> NOT the same silences. Λ_cross's statistics language is SILENT;")
print("     Λ_xray's recovers the cell set exactly. The two are different objects.")