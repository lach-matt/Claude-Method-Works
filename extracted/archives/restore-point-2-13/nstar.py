import math
import numpy as np
from itertools import product
src=open("/tmp/cross.py",encoding="utf-8").read()
src=src[:src.index('print("  PLUGGING δ INTO')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]; op_R=g["op_R"]; delta=g["delta"]
cells=[]
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5: continue
    if par(cfg(ne-1,c))>1: continue
    p=cp_(ne-1,l,c); n0=p+l+1
    cells.append((Z,c,l,S,delta(Z,c,l),n0-delta(Z,c,l),n0))
print(f"  {len(cells)} channels\n")
X4={t[:4] for t in cells}; R4=op_R(X4,4)
E4=len(R4)-len(X4)
print(f"      4 coordinates alone : E = {E4}\n")
print(f"      {'5th coordinate':<26}{'bins':>6}{'E':>9}{'ΔE':>9}{'vs random':>11}")
rng=np.random.default_rng(7)
for nb in (4,8,16):
    Xr={t[:4]+(int(rng.integers(0,nb)),) for t in cells}
    Er=len(op_R(Xr,5))-len(Xr)
    for lab,idx in (("δ  (falls with c)",4),("n* = n₀ − δ  (rises)",5),
                    ("n₀ alone",6)):
        vals=[t[idx] for t in cells]
        qs=np.quantile(vals,np.linspace(0,1,nb+1)[1:-1])
        X5={t[:4]+(int(np.searchsorted(qs,t[idx])),) for t in cells}
        E5=len(op_R(X5,5))-len(X5)
        print(f"      {lab:<26}{nb:>6}{E5:>9}{E5-E4:>9}{(E5-E4)/max(Er-0,1):>11.3f}")
    print(f"      {'random':<26}{nb:>6}{Er:>9}{Er-E4:>9}{1.0:>11.3f}")
    print()
print("  READING\n")
print("      the ratio is the cost of the coordinate as a fraction of noise.")
print("      0 means fully derived — a relabelling. 1 means it carries no")
print("      order relation to its parents at all.")
