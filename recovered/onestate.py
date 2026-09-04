import csv, numpy as np
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
    if z not in d2 or o3<=0: continue
    s2=z-(d2[z]/C(2))**0.25
    s3=z-(o3/C(3))**0.25
    rows.append((z,r["El"],s2,s3,s3-s2))
print("  ONE STATEMENT:  dE = (Z - sigma(n,l))^4 · a^4 mc^2 / (2 n^3 l(l+1))")
print("  sigma extracted separately per shell. is the OFFSET constant?\n")
print(f"  {'el':>3}{'Z':>4}{'sigma_2p':>10}{'sigma_3p':>10}{'offset':>9}")
for z,el,s2,s3,d in rows:
    if z in (16,20,26,30,36,42,47,54,60,70,79,82):
        print(f"  {el:>3}{z:>4}{s2:>10.3f}{s3:>10.3f}{d:>9.3f}")
o=np.array([r[4] for r in rows]); Z=np.array([r[0] for r in rows])
lo=Z<=54
print(f"\n  offset sigma_3p - sigma_2p")
print(f"     all {len(o)} elements : mean {o.mean():>7.3f}  sd {o.std():.3f}")
print(f"     Z <= 54  ({lo.sum():>2})      : mean {o[lo].mean():>7.3f}  sd {o[lo].std():.3f}")
print(f"     Z >  54  ({(~lo).sum():>2})      : mean {o[~lo].mean():>7.3f}  sd {o[~lo].std():.3f}")
sl,ic=np.polyfit(Z,o,1)
print(f"     linear in Z: slope {sl:+.5f} per unit Z, intercept {ic:.3f}")
print(f"     -> the offset {'IS' if abs(sl)<0.005 else 'is NOT'} constant across the table")
# Slater's rules give a DERIVED offset. 2p sees 1s(hole:1)*0.85 + own-shell*0.35;
# 3p sees 1s*1.00 + n=2 shell(hole:7)*0.85 + own-shell*0.35.
print(f"\n  SLATER'S RULES, no fitting: the extra screening a 3p sees over a 2p")
print(f"     3p: 1s2 at 1.00 = 2.00 ; 2s2p with the L1 hole, 7 at 0.85 = 5.95")
print(f"     2p: 1s with the K hole, 1 at 0.85 = 0.85")
print(f"     difference from the inner shells alone = {2.00+5.95-0.85:.2f}")
print(f"     measured mean offset at Z <= 54 = {o[lo].mean():.2f}")