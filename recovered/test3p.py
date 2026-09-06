import csv, numpy as np
def load(p): return {(r["El"],r["A"]):r for r in csv.DictReader((l for l in open(p) if not l.startswith("#")),delimiter="\t")}
A3,A2=load("XRAY-KL3.tsv"),load("XRAY-KL2.tsv")
K=[k for k in A3 if k in A2 and A3[k]["grade"]=="M"]
d2={int(A3[k]["Z"]): float(A3[k]["E_theory_eV"])-float(A2[k]["E_theory_eV"]) for k in K}
R=[r for r in csv.DictReader((l for l in open("XRAY-L1M.tsv") if not l.startswith("#")),delimiter="\t")]
al=7.2973525693e-3; mc2=510998.95
C=lambda n: al**4*mc2/(2*n**3*2)
print("  THE IDENTIFICATION TEST — is the 3p doublet the 2p doublet at n=3?\n")
print("  prediction: sigma from the 2p splitting, then dE(3p) = C(3)(Z-sigma)^4")
print("  NO free parameter.\n")
print(f"  {'el':>3}{'Z':>4}{'2p obs':>10}{'3p obs':>10}{'3p PRED':>10}{'obs/pred':>10}{'ratio 3p/2p':>13}")
rows=[]
for r in R:
    z=int(r["Z"])
    if z not in d2: continue
    s2=z-(d2[z]/C(2))**0.25
    pred=C(3)*(z-s2)**4
    obs=float(r["split_3p"])
    rows.append((z,r["El"],d2[z],obs,pred,obs/pred,obs/d2[z]))
for z,el,o2,o3,p,ratio,rr in rows:
    if z in (20,26,30,36,42,47,54,60,70,79,82):
        print(f"  {el:>3}{z:>4}{o2:>10.2f}{o3:>10.2f}{p:>10.2f}{ratio:>10.3f}{rr:>13.4f}")
import numpy as np
lo=[r for r in rows if r[0]<=60]
print(f"\n  Z <= 60 ({len(lo)} elements):  obs/pred median {np.median([r[5] for r in lo]):.4f}"
      f"   sd {np.std([r[5] for r in lo]):.4f}")
print(f"  observed 3p/2p ratio: median {np.median([r[6] for r in lo]):.4f}"
      f"   against the parameter-free (2/3)^3 = {8/27:.4f}")
hi=[r for r in rows if r[0]>60]
print(f"  Z > 60  ({len(hi)} elements):  obs/pred median {np.median([r[5] for r in hi]):.4f}")