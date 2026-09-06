import math, statistics as st
import numpy as np
from itertools import product
src=open("/tmp/uidx.py",encoding="utf-8").read()
src=src[:src.index('print(f"  Λ_spectra RE-INDEXED')]
g={}; exec(src,g)
R=g["R"]; u=g["u"]; opR=g["opR"]
def E(cells,d): return len(opR(cells,d))-len(cells)
print("  IS E = 9 STRUCTURE OR BINNING?\n")
rng=np.random.default_rng(17)
for nb in (8,12,16):
    q=np.quantile(u,np.linspace(0,1,nb+1)[1:-1])
    ub=[int(np.searchsorted(q,v)) for v in u]
    real=E({(ub[i],r["l"],r["S"]) for i,r in enumerate(R)},3)
    # shuffle the u-band labels across channels, keeping the same band sizes
    sh=[]
    for _ in range(40):
        perm=rng.permutation(ub)
        sh.append(E({(perm[i],r["l"],r["S"]) for i,r in enumerate(R)},3))
    print(f"      {nb:>2} bands : real E = {real:>4}   shuffled "
          f"{st.median(sh):>6.1f} ± {st.pstdev(sh):.1f}"
          f"   (min {min(sh)}, max {max(sh)})")
print()
print("      → if real ≪ shuffled, u carries order the labels do not.")
print()
print("  AND THE SAME FOR THE OLD COORDINATE\n")
for nb in (8,12):
    q=np.quantile(u,np.linspace(0,1,nb+1)[1:-1])
    ub=[int(np.searchsorted(q,v)) for v in u]
    cb=[min(r["c"]-1,nb-1) for r in R]
    print(f"      {nb:>2} bands : u-banded E = "
          f"{E({(ub[i],r['l'],r['S']) for i,r in enumerate(R)},3):>4}"
          f"   ·   c-banded E = "
          f"{E({(cb[i],r['l'],r['S']) for i,r in enumerate(R)},3):>4}")
print()
print("  WHAT SURVIVES\n")
print("      the comparison that matters is not E against noise — it is whether")
print("      the SAME channels stay together under u and under c. that is a")
print("      question about the partition, not about the defect.")
q=np.quantile(u,np.linspace(0,1,9)[1:-1])
ub=[int(np.searchsorted(q,v)) for v in u]
from collections import defaultdict
byu=defaultdict(set); byc=defaultdict(set)
for i,r in enumerate(R):
    byu[ub[i]].add((r["ne"],r["c"])); byc[r["c"]].add((r["ne"],r["c"]))
print(f"\n      species per u-band : " + " ".join(f"{len(v)}" for k,v in sorted(byu.items())))
print(f"      species per charge : " + " ".join(f"{len(v)}" for k,v in sorted(byc.items())))
print()
print("      u-bands mix charges; charge bands mix u. neither refines the other.")