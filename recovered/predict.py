import math
import numpy as np
print("  THE PREDICTION  —  does G/F give the crossing charge?\n")
print("      the amplitude a is the coefficient of √p in ν = n − a√p.")
print("      the ordering flips when a falls through a_cross.")
print("      if a is set by the electron-electron term, then a ∝ (F − G) or")
print("      similar, and its DESCENT with charge is the screening's fall.\n")
GF={4:0.298021,5:0.362562,6:0.403148,7:0.430391}
AC={4:0.5773503,5:1.0000000,6:1.2168450,7:1.3938270}
CC={4:2,5:2,6:2,7:3}      # crossing charge, first of each pair
CC2={6:3,7:5}             # the SECOND ladder at the same pair (Ne=70, 102)
print(f"      {'pair':>8}{'G/F':>10}{'a_cross':>10}{'a_cross/(G/F)':>16}"
      f"{'a_cross·(1−G/F)':>18}")
for n in (4,5,6,7):
    g=GF[n]; a=AC[n]
    print(f"      {f'{n}s/{n-1}d':>8}{g:>10.4f}{a:>10.4f}{a/g:>16.4f}"
          f"{a*(1-g):>18.4f}")
print()
print("  THE DESCENT MODEL  —  a(c) = a₁ · (screening ratio)^(c−1)\n")
print("      hydrogenic screening falls as 1/Z_eff, and along an isoelectronic")
print("      ladder Z_eff ≈ Z − σ with σ fixed, so a(c) ∝ 1/(c + s) for some s.")
print("      the crossing charge is then c* = a₁·(1+s)/a_cross − s.\n")
print("      solve for a₁ and s from the two ladders that share a pair:\n")
print("      6s/5d : Nₑ=56 crosses at c=2, Nₑ=70 at c=3, same a_cross=1.2168")
print("      7s/6d : Nₑ=88 crosses at c=3, Nₑ=102 at c>4, same a_cross=1.3938\n")
print("      → the SAME a_cross with DIFFERENT crossing charges means a(c)")
print("        differs between the two ladders. so a depends on Nₑ as well as c.")
print("        a is a(Nₑ, c), and G/F depends only on the PAIR.\n")
print("  SO G/F CANNOT PREDICT THE CROSSING CHARGE ALONE\n")
print("      Nₑ=56 and Nₑ=70 have identical pairs, identical G/F, identical")
print("      a_cross — and cross at different charges. no function of the pair")
print("      can distinguish them.\n")
print("  WHAT G/F DOES PREDICT — test it on a_cross instead\n")
x=np.array([GF[n] for n in (4,5,6,7)]); y=np.array([AC[n] for n in (4,5,6,7)])
from scipy import stats as SS
for nm,X in (("G/F",x),("1/(1−G/F)",1/(1-x)),("−ln(1−2·G/F)",-np.log(np.maximum(1-2*x,1e-9))),
             ("G/F/(1−G/F)",x/(1-x))):
    r=SS.linregress(X,y)
    print(f"      a_cross vs {nm:<16}r² {r.rvalue**2:.5f}   {r.intercept:+.4f} {r.slope:+.4f}x")
print()
print("      but a_cross is ALREADY exact — (Δn)/(√pᵣ−√p_g) — so a correlation")
print("      here would be a coincidence of two things both rising with n,")
print("      not a prediction. the honest test was the crossing CHARGE, and")
print("      that test FAILS for the reason above.")