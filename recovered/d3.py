import csv, numpy as np
def load(p): return {(r["El"],r["A"]):r for r in csv.DictReader((l for l in open(p) if not l.startswith("#")),delimiter="\t")}
A3,A2=load("XRAY-KL3.tsv"),load("XRAY-KL2.tsv")
K=[k for k in A3 if k in A2]
Z=np.array([int(A3[k]["Z"]) for k in K])
D=np.array([float(A3[k]["E_theory_eV"])-float(A2[k]["E_theory_eV"]) for k in K])
g=np.array([A3[k]["grade"] for k in K])
al=7.2973525693e-3; mc2=510998.95; C=al**4*mc2/32
sel=(g=='M')&(Z<=36)
print(f"scan sigma on measured Z<=36, {sel.sum()} rows")
print(f"{'sigma':>7}{'mean ratio':>12}{'rel scatter':>13}")
best=None
for s in np.arange(0.0,6.01,0.25):
    r=D[sel]/(C*(Z[sel]-s)**4.0)
    rel=np.std(r)/np.mean(r)
    if s in (0.0,1.0,2.0,3.0,3.5,4.0,5.0,6.0):
        print(f"{s:>7.2f}{np.mean(r):>12.4f}{rel:>13.4f}")
    if best is None or rel<best[0]: best=(rel,s)
# refine
lo,hi=best[1]-0.3,best[1]+0.3
for s in np.arange(lo,hi,0.005):
    r=D[sel]/(C*(Z[sel]-s)**4.0); rel=np.std(r)/np.mean(r)
    if rel<best[0]: best=(rel,s)
rel,sig=best
r=D[sel]/(C*(Z[sel]-sig)**4.0)
print(f"\nBEST  sigma = {sig:.3f}   mean ratio = {np.mean(r):.4f}   relative scatter = {rel:.4f}")
print(f"\n{'Z':>4}{'observed eV':>13}{'C(Z-s)^4':>12}{'ratio':>8}")
for z in (10,15,20,26,30,36,50,70,80,92,100):
    i=int(np.argmin(abs(Z-z))); p=C*(Z[i]-sig)**4
    print(f"{Z[i]:>4}{D[i]:>13.3f}{p:>12.3f}{D[i]/p:>8.4f}")
for lab,mask in (("Z<=36",(g=='M')&(Z<=36)),("Z 37-69",(g=='M')&(Z>36)&(Z<70)),
                 ("Z>=70",(g=='M')&(Z>=70))):
    rr=D[mask]/(C*(Z[mask]-sig)**4)
    print(f"   {lab:<9} mean ratio {np.mean(rr):.4f}   n={mask.sum()}")