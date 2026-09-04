import math, statistics as st
import numpy as np
from scipy import stats as SS
print("  IS a A STATISTIC OF THE CORE'S CHARGE DENSITY?\n")
print("      the descent's algebra should be the two-electron integrals.")
print("      hydrogenic Slater integrals scale as F^k, G^k ∝ Z_eff — LINEAR in")
print("      charge — while one-electron energies go as Z_eff². so the ratio")
print("      (two-electron)/(one-electron) falls as 1/Z_eff.\n")
print("      a is the coefficient of √p in ν = n − a√p, and √p is a length in")
print("      node number. if a measures (repulsion)/(binding), then a ∝ 1/Z_eff.\n")
NE=np.array([20.,38.,56.,88.]); LB=np.array([0.577,1.000,1.217,1.394])
print("  TEST — a_min(c=1) AGAINST CANDIDATE STATISTICS OF THE CORE\n")
print(f"      {'model':<34}{'r²':>9}{'rms':>9}")
CAND=[("ln Nₑ", np.log(NE)),
      ("Nₑ^(1/3)  (TF radius^-1)", NE**(1/3)),
      ("Nₑ^(2/3)  (TF area)", NE**(2/3)),
      ("√Nₑ", np.sqrt(NE)),
      ("Nₑ", NE),
      ("1 − Nₑ^(-1/3)", 1-NE**(-1/3)),
      ("ln Nₑ / Nₑ^(1/3)", np.log(NE)/NE**(1/3))]
for nm,X in CAND:
    r=SS.linregress(X,LB)
    res=LB-(r.intercept+r.slope*X)
    print(f"      {nm:<34}{r.rvalue**2:>9.4f}{float(np.sqrt(np.mean(res**2))):>9.5f}")
print()
print("  AND WITHOUT AN INTERCEPT  —  a pure statistic has no offset\n")
print(f"      {'model':<34}{'coef':>10}{'rms':>10}")
for nm,X in CAND:
    k=float(np.sum(X*LB)/np.sum(X*X)); res=LB-k*X
    print(f"      {nm:<34}{k:>10.4f}{float(np.sqrt(np.mean(res**2))):>10.5f}")
print()
print("  THE SHELL COUNT — a is per √p, and p counts SHELLS\n")
print("      at c = 1 the outermost s subshell has p = n − 1 with n the period.")
print(f"      {'Nₑ':>4}{'period':>8}{'p(s)':>6}{'√p':>8}{'a_min':>9}{'a_min/√p':>11}")
PS={20:(4,3),38:(5,4),56:(6,5),88:(7,6)}
V=[]
for ne in (20,38,56,88):
    per,p=PS[ne]; i=[20,38,56,88].index(ne)
    print(f"      {ne:>4}{per:>8}{p:>6}{math.sqrt(p):>8.4f}{LB[i]:>9.4f}"
          f"{LB[i]/math.sqrt(p):>11.4f}")
    V.append(LB[i]/math.sqrt(p))
print(f"\n      a_min/√p : median {st.median(V):.4f}  sd {st.pstdev(V):.4f}"
      f"  range {min(V):.4f}–{max(V):.4f}")
print()
print("  AND a_min AGAINST THE PERIOD ITSELF\n")
PER=np.array([4.,5.,6.,7.])
for nm,X in (("period n",PER),("√(n−1)",np.sqrt(PER-1)),("ln n",np.log(PER)),
             ("1 − 1/n",1-1/PER)):
    r=SS.linregress(X,LB)
    print(f"      a_min vs {nm:<12}r² {r.rvalue**2:.4f}   "
          f"{r.intercept:+.4f} {r.slope:+.4f}·{nm}")