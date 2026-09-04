import math, statistics as st
import numpy as np
Rinf=109737.31568; mp=1836.15267343
RM=Rinf/(1+1/(40.078*mp)); lim=49305.92; c=1
S={0:{5:31539.495,6:40474.241,7:43980.767,8:45738.684,9:46748.283,10:47382.048,11:47806.20},
   1:{5:36547.688,6:42514.845,7:44955.67,8:46284.12,9:47085.38,10:47604.75},
   2:{4:37748.197,5:42743.002,6:45049.073,7:46301.973,8:47036.225,9:47752.655},
   3:{4:42170.214,5:44762.620,6:46164.644,7:47006.194,8:47550.214,9:47921.87}}
PM={0:4,1:3,2:0,3:0}
L="spdf"
print("  Ca I   Nₑ = 20   limit 49305.92   —  the crossing point\n")
print(f"      {'ℓ':>3}{'p':>3}{'n':>4}{'δ (top 3)':>12}{'σ':>9}{'  all δ'}")
OUT={}
for l in sorted(S):
    d=S[l]
    n=np.array(sorted(d),float); E=np.array([d[int(x)] for x in n])
    ns=c*np.sqrt(RM/(lim-E)); dd=n-ns
    use=dd[-3:]
    OUT[l]=st.median(use)
    print(f"      {L[l]:>3}{PM[l]:>3}{len(n):>4}{st.median(use):>12.4f}{st.pstdev(use):>9.4f}"
          f"   " + " ".join(f"{v:.3f}" for v in dd))
print()
print("  THE MEASUREMENT THE GENERATOR NEEDED\n")
print(f"      δ(nd) at Ca I = {OUT[2]:.4f}   with p = 0")
print(f"      the generator assumed δ = a√p = 0 when p = 0.\n")
print("      n* for each ℓ, with the measured δ:")
for l in sorted(S):
    n0=PM[l]+l+1
    print(f"          {L[l]} : n₀ = {n0}   δ = {OUT[l]:.4f}   n* = {n0-OUT[l]:.4f}")
print()
lo=min(range(4),key=lambda l:(PM[l]+l+1)-OUT[l])
print(f"      lowest n* : {L[lo]}   →  the next electron goes to "
      f"{PM[lo]+lo+1}{L[lo]}")
print(f"      truth at Z = 21 (Sc I) : 3d\n")
print("  AND THE SAME WITH δ(nd) SET TO ZERO, AS THE GENERATOR HAD IT\n")
for l in sorted(S):
    n0=PM[l]+l+1; dv=OUT[l] if PM[l]>0 else 0.0
    print(f"          {L[l]} : n* = {n0-dv:.4f}")
