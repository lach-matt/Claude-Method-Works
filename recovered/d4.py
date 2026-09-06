import csv, numpy as np
def load(p): return {(r["El"],r["A"]):r for r in csv.DictReader((l for l in open(p) if not l.startswith("#")),delimiter="\t")}
A3,A2=load("XRAY-KL3.tsv"),load("XRAY-KL2.tsv")
K=[k for k in A3 if k in A2]
Z=np.array([int(A3[k]["Z"]) for k in K])
D=np.array([float(A3[k]["E_theory_eV"])-float(A2[k]["E_theory_eV"]) for k in K])
g=np.array([A3[k]["grade"] for k in K])
al=7.2973525693e-3; mc2=510998.95; C=al**4*mc2/32
# NIST flags Ne and Na as BLEND "KL2,3" — the two lines are not resolved there,
# so their difference is not a measurement. Excluded on the database's own flag.
ok=(g=='M')&(Z>=12)
print("Ne(10) and Na(11) EXCLUDED — NIST Blend column reads KL2,3 (unresolved).")
sel=ok&(Z<=36)
best=None
for s in np.arange(0.0,6.0,0.005):
    r=D[sel]/(C*(Z[sel]-s)**4.0); rel=np.std(r)/np.mean(r)
    if best is None or rel<best[0]: best=(rel,s)
rel,sig=best
print(f"\nsigma fitted on measured, unblended, Z 12-36  ({sel.sum()} rows)")
print(f"   sigma = {sig:.3f}   mean ratio = {np.mean(D[sel]/(C*(Z[sel]-sig)**4)):.4f}"
      f"   relative scatter = {rel:.4f}")
print(f"\n{'Z':>4}{'observed eV':>13}{'C(Z-s)^4':>12}{'ratio':>8}")
for z in (12,15,20,26,30,36,50,70,80,92,100):
    i=int(np.argmin(abs(Z-z))); p=C*(Z[i]-sig)**4
    print(f"{Z[i]:>4}{D[i]:>13.3f}{p:>12.3f}{D[i]/p:>8.4f}")
for lab,mask in (("Z 12-36",ok&(Z<=36)),("Z 37-69",ok&(Z>36)&(Z<70)),("Z>=70",ok&(Z>=70))):
    rr=D[mask]/(C*(Z[mask]-sig)**4)
    print(f"   {lab:<9} mean ratio {np.mean(rr):.4f}  sd {np.std(rr):.4f}  n={mask.sum()}")