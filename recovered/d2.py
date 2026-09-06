import csv, numpy as np
def load(p): return {(r["El"],r["A"]):r for r in csv.DictReader((l for l in open(p) if not l.startswith("#")),delimiter="\t")}
A3,A2=load("XRAY-KL3.tsv"),load("XRAY-KL2.tsv")
K=[k for k in A3 if k in A2]
Z=np.array([int(A3[k]["Z"]) for k in K])
D=np.array([float(A3[k]["E_theory_eV"])-float(A2[k]["E_theory_eV"]) for k in K])
g=np.array([A3[k]["grade"] for k in K]); m=(g=='M')
al=7.2973525693e-3; mc2=510998.95
C=al**4*mc2/32          # Dirac n=2 fine structure: dE = (Z a)^4 mc^2 / 32
print(f"DIRAC coefficient  a^4 mc^2/32 = {C:.6e} eV   (my earlier a^2 Ry/24 was 2/3 of this)")
# fit sigma in  dE = C (Z - sigma)^4  , low-Z where relativity is small
best=None
for s in np.arange(0,8,0.001):
    lo=m&(Z<=30)&(Z>s+2)
    r=D[lo]/(C*(Z[lo]-s)**4)
    v=np.std(r)
    if best is None or v<best[0]: best=(v,s,np.mean(r))
v,sig,mean=best
print(f"\nFIT  dE = C (Z - sigma)^4   on measured Z <= 30")
print(f"   sigma = {sig:.3f}   mean ratio = {mean:.4f}   scatter {v:.4f}")
print(f"   (2p screening: the K hole plus 1s2 leaves ~3-4 units screened)")
print(f"\n{'Z':>4}{'observed':>12}{'C(Z-s)^4':>12}{'ratio':>8}")
for z in (10,15,20,30,40,60,80,92,100):
    i=int(np.argmin(abs(Z-z)))
    p=C*(Z[i]-sig)**4
    print(f"{Z[i]:>4}{D[i]:>12.2f}{p:>12.2f}{D[i]/p:>8.4f}")
lo=m&(Z<=30)
print(f"\n   Z <= 30 : mean ratio {np.mean(D[lo]/(C*(Z[lo]-sig)**4)):.4f}")
hi=m&(Z>=70)
print(f"   Z >= 70 : mean ratio {np.mean(D[hi]/(C*(Z[hi]-sig)**4)):.4f}"
      f"  <- relativistic excess, same direction as Moseley and the hydrogenic test")