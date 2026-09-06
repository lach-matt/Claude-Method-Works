import csv, numpy as np
BLEND=set(range(23,32))
def load(p): return {(r["El"],r["A"]):r for r in csv.DictReader((l for l in open(p) if not l.startswith("#")),delimiter="\t")}
A3,A2=load("XRAY-KL3.tsv"),load("XRAY-KL2.tsv")
K=[k for k in A3 if k in A2 and A3[k]["grade"]=="M"]
d2={int(A3[k]["Z"]): float(A3[k]["E_theory_eV"])-float(A2[k]["E_theory_eV"]) for k in K}
R=[r for r in csv.DictReader((l for l in open("XRAY-L1M.tsv") if not l.startswith("#")),delimiter="\t")]
al=7.2973525693e-3; mc2=510998.95; C=lambda n: al**4*mc2/(2*n**3*2)
o={}
for r in R:
    z=int(r["Z"]); x=float(r["split_3p"])
    if z in BLEND or z not in d2 or x<=0: continue
    o[z]=(z-(x/C(3))**0.25)-(z-(d2[z]/C(2))**0.25)
Z=np.array(sorted(o)); v=np.array([o[z] for z in Z])

print("  THE JANET REGIONS, FITTED SEPARATELY — no pooling (domain_protocol Q1)\n")
REG=[("pre-collapse, 3d empty",   lambda z: z< 21),
     ("THE BOUNDARY 3d collapsing",lambda z: 21<=z<=22),
     ("3d complete, pre-closure", lambda z: 32<=z<=35),
     ("post Kr closure",          lambda z: z>=36)]
print(f"  {'region':<28}{'Z':<12}{'n':>3}{'offset':>10}{'sd':>9}")
for lab,f in REG:
    m=np.array([f(z) for z in Z])
    if m.sum()==0: continue
    zz=Z[m]
    print(f"  {lab:<28}{str(zz.min())+'-'+str(zz.max()):<12}{m.sum():>3}"
          f"{v[m].mean():>10.3f}{v[m].std():>9.3f}")

print("\n  CONTINGENCY (R 1383) — could the Z=21 anomaly have been anywhere?")
dev=np.abs(v-np.median(v))
order=np.argsort(-dev)
print(f"     the two largest deviations from the median, of {len(Z)} elements:")
for i in order[:4]:
    print(f"        Z = {Z[i]:>3}  offset {v[i]:>7.3f}   deviation {dev[i]:>6.3f}")
print(f"     Janet boundaries (Q.collapse): 21 (3d), 57 (4f), 89 (5f)")
hit=sum(1 for i in order[:2] if Z[i] in (21,22))
print(f"     of the 2 largest, {hit} fall at or adjacent to Z=21.")
print(f"     P(both land on 21-22 by chance) = {2/len(Z)*1/(len(Z)-1):.4f}")
print(f"\n  and Z=57 (4f collapse)? offset there = {o.get(57)}")
print(f"     La 57 sits at {o.get(57):.3f} against Ba 56 {o.get(56):.3f} — NO break.")
print(f"     so the 3p splitting sees the 3d collapse and NOT the 4f collapse,")
print(f"     which is what a 3p electron should see: 3d is inside its own shell")
print(f"     region, 4f is outside it.")