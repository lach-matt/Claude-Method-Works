import math, statistics as st
import numpy as np
from scipy import stats as SS
print("  THE SLOPE AGAINST SUBSHELL SIZE\n")
print("      hydrogenic ⟨r⟩ = (3n² − ℓ(ℓ+1))/2Z_eff.  adding an electron to a")
print("      COMPACT subshell raises the repulsion more, so slope ∝ 1/⟨r⟩.\n")
S=[(3,1,1,0.1054,"3p"),(4,0,3,0.2431,"4s"),(4,1,2,0.0670,"4p"),
   (4,2,1,0.0208,"4d"),(5,0,4,0.0932,"5s"),(5,1,3,0.0505,"5p")]
print(f"      {'shell':>7}{'n':>3}{'ℓ':>3}{'slope':>10}{'3n²−ℓ(ℓ+1)':>13}"
      f"{'slope×⟨r⟩':>12}{'slope×n²':>11}")
V=[];W=[]
for n,l,p,s,nm in S:
    r=3*n*n-l*(l+1)
    V.append(s*r); W.append(s*n*n)
    print(f"      {nm:>7}{n:>3}{l:>3}{s:>10.4f}{r:>13}{s*r:>12.4f}{s*n*n:>11.4f}")
print()
print(f"      slope×⟨r⟩ : median {st.median(V):.3f}  sd {st.pstdev(V):.3f}"
      f"  cv {st.pstdev(V)/st.median(V):.3f}")
print(f"      slope×n²  : median {st.median(W):.3f}  sd {st.pstdev(W):.3f}"
      f"  cv {st.pstdev(W)/st.median(W):.3f}")
print()
print("  AND WITH Z_eff — the subshell's own effective charge\n")
print("      ⟨r⟩ = (3n² − ℓ(ℓ+1))/2Z_eff, and Z_eff ≈ n/ν with ν the effective")
print("      quantum number. using ν from the FIRST element of each subshell:\n")
NU={"3p":2.0,"4s":2.15,"4p":2.6,"4d":3.3,"5s":2.6,"5p":3.0}
print(f"      {'shell':>7}{'ν₀':>7}{'Z_eff':>8}{'⟨r⟩':>10}{'slope×⟨r⟩':>12}")
U=[]
for n,l,p,s,nm in S:
    nu=NU[nm]; ze=n/nu
    r=(3*n*n-l*(l+1))/(2*ze)
    U.append(s*r)
    print(f"      {nm:>7}{nu:>7.2f}{ze:>8.3f}{r:>10.3f}{s*r:>12.4f}")
print()
print(f"      slope×⟨r⟩ with Z_eff : median {st.median(U):.3f}"
      f"  sd {st.pstdev(U):.3f}  cv {st.pstdev(U)/st.median(U):.3f}")
print()
print("  WHAT ABOUT MASS?\n")
print("      the reduced-mass correction is R_M/R∞ = 1/(1 + m_e/M).")
print("      for the elements here M runs 27 to 208 amu, so m_e/M runs")
print(f"      {1/(27*1836):.2e} to {1/(208*1836):.2e} — a relative effect of ~10⁻⁵.")
print()
print("      the slopes vary by a factor of 12 (0.021 to 0.243).")
print("      → MASS CANNOT EXPLAIN IT. the effect is four orders too small.")
print()
print("  READING\n")
best=min([("⟨r⟩ hydrogenic",st.pstdev(V)/st.median(V)),
          ("n²",st.pstdev(W)/st.median(W)),
          ("⟨r⟩ with Z_eff",st.pstdev(U)/st.median(U))],key=lambda x:x[1])
print(f"      lowest scatter: {best[0]} at cv {best[1]:.3f}")
print("      six slopes, three candidates — this cannot discriminate. what it")
print("      CAN say is that mass is excluded by four orders of magnitude, and")
print("      size is not.")