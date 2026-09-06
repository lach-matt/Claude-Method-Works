import csv, numpy as np
BLEND=set(range(23,32))
def load(p): return {(r["El"],r["A"]):r for r in csv.DictReader((l for l in open(p) if not l.startswith("#")),delimiter="\t")}
A3,A2=load("XRAY-KL3.tsv"),load("XRAY-KL2.tsv")
K=[k for k in A3 if k in A2 and A3[k]["grade"]=="M"]
d2={int(A3[k]["Z"]): float(A3[k]["E_theory_eV"])-float(A2[k]["E_theory_eV"]) for k in K}
R=[r for r in csv.DictReader((l for l in open("XRAY-L1M.tsv") if not l.startswith("#")),delimiter="\t")]
al=7.2973525693e-3; mc2=510998.95; C=lambda n: al**4*mc2/(2*n**3*2)
rows=[]
for r in R:
    z=int(r["Z"]); o3=float(r["split_3p"])
    if z in BLEND or z not in d2 or o3<=0: continue
    rows.append((z,r["El"], (z-(o3/C(3))**0.25)-(z-(d2[z]/C(2))**0.25)))
print("  THE OFFSET, ELEMENT BY ELEMENT — looking for the region boundary\n")
print(f"  {'el':>3}{'Z':>4}{'offset':>9}     {'el':>3}{'Z':>4}{'offset':>9}")
h=(len(rows)+1)//2
for i in range(h):
    a=rows[i]; b=rows[i+h] if i+h<len(rows) else None
    s=f"  {a[1]:>3}{a[0]:>4}{a[2]:>9.3f}"
    if b: s+=f"     {b[1]:>3}{b[0]:>4}{b[2]:>9.3f}"
    print(s)
Z=np.array([r[0] for r in rows]); o=np.array([r[2] for r in rows])
print("\n  scanning for the cleanest two-region split:")
best=None
for cut in range(20,60):
    lo,hi=Z<cut,Z>=cut
    if lo.sum()<4 or hi.sum()<4: continue
    score=o[lo].std()+o[hi].std()
    if best is None or score<best[0]: best=(score,cut,o[lo].mean(),o[lo].std(),o[hi].mean(),o[hi].std(),lo.sum(),hi.sum())
_,cut,m1,s1,m2,s2,n1,n2=best
print(f"     boundary at Z = {cut}")
print(f"     Z < {cut:<3} n={n1:<3} offset {m1:.3f} ± {s1:.3f}")
print(f"     Z >= {cut:<2} n={n2:<3} offset {m2:.3f} ± {s2:.3f}")
print(f"\n  is that a JANET BLOCK BOUNDARY?  Q.collapse names 21, 57, 89.")
print(f"     n+l=5 opens at Z=21 (3d) · n+l=6 at 39 (4d) · n+l=7 at 57 (4f)")