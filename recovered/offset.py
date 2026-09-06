import csv, numpy as np
# NIST flags L1M2,3 as BLENDED for V(23) through Ga(31) — unresolved, so the
# difference is not a measurement. Excluded on the database's own flag, exactly
# as Ne and Na were excluded from the Ka doublet (R 1385).
BLEND=set(range(23,32))
def load(p): return {(r["El"],r["A"]):r for r in csv.DictReader((l for l in open(p) if not l.startswith("#")),delimiter="\t")}
A3,A2=load("XRAY-KL3.tsv"),load("XRAY-KL2.tsv")
K=[k for k in A3 if k in A2 and A3[k]["grade"]=="M"]
d2={int(A3[k]["Z"]): float(A3[k]["E_theory_eV"])-float(A2[k]["E_theory_eV"]) for k in K}
R=[r for r in csv.DictReader((l for l in open("XRAY-L1M.tsv") if not l.startswith("#")),delimiter="\t")]
al=7.2973525693e-3; mc2=510998.95
C=lambda n: al**4*mc2/(2*n**3*2)
rows=[]
for r in R:
    z=int(r["Z"]); o3=float(r["split_3p"])
    if z in BLEND or z not in d2 or o3<=0: continue
    s2=z-(d2[z]/C(2))**0.25; s3=z-(o3/C(3))**0.25
    rows.append((z,r["El"],s2,s3,s3-s2))
Z=np.array([r[0] for r in rows]); o=np.array([r[4] for r in rows])
print(f"  blend-flagged Z 23-31 excluded on NIST's own flag. {len(rows)} elements remain,"
      f" Z {Z.min()}-{Z.max()}\n")
print(f"  offset sigma_3p - sigma_2p : mean {o.mean():.4f}  sd {o.std():.4f}"
      f"  min {o.min():.3f}  max {o.max():.3f}")
sl,ic=np.polyfit(Z,o,1)
print(f"  linear in Z: slope {sl:+.5f}/unit  ->  {'CONSTANT' if abs(sl)<0.005 else 'still drifting'}")
for lab,m in (("Z<=40",Z<=40),("Z 41-60",(Z>40)&(Z<=60)),("Z>60",Z>60)):
    print(f"     {lab:<9} n={m.sum():>2}  mean {o[m].mean():.4f}  sd {o[m].std():.4f}")

print("\n  IS 5.3 A COUNT?  Slater's rules, no fitting.")
print("     a 3p electron is screened by 1s2 at 1.00 and by the n=2 shell at 0.85")
print("     a 2p electron (K hole) is screened by the ONE remaining 1s at 0.85")
for nL1 in (7,8):
    val=2*1.00 + nL1*0.85 - 0.85
    print(f"     n=2 shell holding {nL1}: 2.00 + {nL1}x0.85 - 0.85 = {val:.2f}")
print(f"     measured {o.mean():.2f}")
print(f"\n  the DERIVED count that matches: which integer combination gives {o.mean():.2f}?")
best=[]
for a in range(0,3):
    for b in range(0,9):
        for c_ in range(0,9):
            v=a*1.00+b*0.85+c_*0.35
            if abs(v-o.mean())<0.09: best.append((abs(v-o.mean()),a,b,c_,v))
for d,a,b,c_,v in sorted(best)[:4]:
    print(f"     {a}x1.00 + {b}x0.85 + {c_}x0.35 = {v:.2f}   (off by {d:.3f})")