import numpy as np
R=109737.3; Z=6; I=892700.
d4,d5=1.0057,0.9812
T=lambda dv,n: Z*Z*R/(n-dv)**2
T4,T5=T(d4,4),T(d5,5)
print("="*76)
print("  SQUEEZE 1 -- BRACKET T DIRECTLY, NOT delta")
print("="*76)
print("""
  T(n) = Z^2 R / (n-delta)^2 is itself a convex decreasing sequence in n.
  Convexity of the SEQUENCE gives  T(4) - 2T(5) + T(6) >= 0, hence

        T(6) >= 2 T(5) - T(4)

  a bound that uses NO assumption about delta's form at all.
""")
print("     T(4s) = %12.2f cm-1"%T4)
print("     T(5s) = %12.2f cm-1"%T5)
T6_lo = 2*T5-T4
print("     2T(5)-T(4) = %.2f   -> T(6) >= %.2f"%(T6_lo,T6_lo))
print("     monotone:    T(6) <= T(5) = %.2f"%T5)
print("\n     T bracket : [%.2f, %.2f]   width %.2f"%(max(T6_lo,0),T5,T5-max(T6_lo,0)))
E_from_T=lambda t: I-t
print("     E bracket : [%.0f, %.0f]   width %.0f"%(E_from_T(T5),E_from_T(max(T6_lo,0)),
                                                    T5-max(T6_lo,0)))
print("="*76)
print("  SQUEEZE 2 -- COMPARE ALL ROUTES")
print("="*76)
d2=(d4-d5)/(1/16-1/25); d0=d4-d2/16
lo_mono,hi=d0,d5
lo_conv=2*d5-d4
Ed=lambda dv,n=6: I - Z*Z*R/(n-dv)**2
ROUTES=[("delta, monotone only",Ed(hi),Ed(lo_mono)),
        ("delta, + convex",Ed(hi),Ed(lo_conv)),
        ("T, convex sequence",E_from_T(T5),E_from_T(max(T6_lo,0)))]
print("\n  %-28s%14s%14s%12s"%("route","lower","upper","width"))
for nm,a,b in ROUTES:
    print("  %-28s%14.0f%14.0f%12.0f"%(nm,a,b,b-a))
best=min(ROUTES,key=lambda r:r[2]-r[1])
lo_all=max(r[1] for r in ROUTES); hi_all=min(r[2] for r in ROUTES)
print("\n  **INTERSECTION OF ALL ROUTES : [%.0f, %.0f]   width %.0f**"%(lo_all,hi_all,hi_all-lo_all))
print("="*76)
print("  SQUEEZE 3 -- THE INTERSECTION IS THE POINT")
print("="*76)
print("""
  Every route is a DEDUCTIVE bound, so the true value lies in ALL of them.
  **The answer is their intersection, and no single route gives it.**

  Chapter 9's D says two disjoint routes CHECK a claim. Here two disjoint
  routes TIGHTEN it -- the same mechanism used for a different purpose,
  and the book never states that use.
""")
dr=d0+d2/36
print("     point estimate (Ritz two-point) : %.0f"%Ed(dr))
print("     inside the intersection          : %s"%(lo_all<=Ed(dr)<=hi_all))
print("     intersection width               : %.0f cm-1"%(hi_all-lo_all))
print("     as a fraction of T(6s)           : %.4f%%"%(100*(hi_all-lo_all)/(I-Ed(dr))))
print("     wavelength window                : %.4f to %.4f nm"%(1e7/hi_all,1e7/lo_all))
print("="*76)
print("  SQUEEZE 4 -- WHAT WOULD TIGHTEN IT FURTHER, AND BY HOW MUCH")
print("="*76)
print("""
  With two measured levels the order properties are exhausted: monotone
  and convex are both used, and the third difference needs a third level.
""")
print("  %-40s%16s%14s"%("if this became available","bracket width","factor"))
print("  "+"-"*70)
print("  %-40s%16.0f%14s"%("nothing further (now)",hi_all-lo_all,"1.0"))
d6g=dr
T6g=Z*Z*R/(6-d6g)**2
lo3 = 3*T6g-3*T5+T4
print("  %-40s%16.0f%14.1f"%("a measured 6s (then 7s bracket)",abs(lo3-T6g),(hi_all-lo_all)/max(abs(lo3-T6g),1)))
sig=0.4
print("  %-40s%16.0f%14s"%("the limit to +-0.001 instead of +-400",hi_all-lo_all,"unchanged"))
print("""
  **THE LIMIT'S UNCERTAINTY DOES NOT ENTER.** Every bound above is a
  difference of measured levels; I cancels identically. That is Section
  13.3's limit-freedom doing real work on the one prediction the book
  makes.

  **SO THE COMMITTED PREDICTION TIGHTENS AGAIN, AND STAYS INSIDE ITS
  ORIGINAL BOUND:**
""")
print("     original  §16.6 : [735860, 738547]   width 2687")
print("     convex    delta : [735860, 737380]   width 1520")
print("     **all routes    : [%.0f, %.0f]   width %.0f**"%(lo_all,hi_all,hi_all-lo_all))
print("     estimate        :  %.0f cm-1   %.4f nm   %.3f eV"%(Ed(dr),1e7/Ed(dr),Ed(dr)*1.23984e-4))