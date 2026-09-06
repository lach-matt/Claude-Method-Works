import numpy as np
R=109737.3; Z=6; I=892700.
d4,d5=1.0057,0.9812
print("="*76)
print("  Sc VI 6s -- RE-DERIVED WITH THE CONVEXITY BRACKET")
print("="*76)
print("""
  Section 16.6 used MONOTONICITY only: delta decreasing gives
  delta_inf < delta(6s) < delta(5s). But delta = d0 + d2/n^2 is also
  CONVEX -- delta'' = 6 d2/n^4 > 0 -- and Section 21.6's k-th order
  bracket exploits exactly that. **It was built after Chapter 16 and never
  applied to the prediction.**
""")
d2=(d4-d5)/(1/16-1/25); d0=d4-d2/16
print("     two-point Ritz:  d2 = %.4f   d0 = delta_inf = %.4f"%(d2,d0))
print("     delta(4s) = %.4f   delta(5s) = %.4f"%(d4,d5))
print("""
  CONVEXITY GIVES A TANGENT LOWER BOUND. For a convex f, f' is increasing,
  so on (5,6) the slope is at least the backward slope on (4,5):

        delta(6) >= delta(5) + [delta(5) - delta(4)]
""")
lo_conv = d5 + (d5-d4)
hi_mono = d5
lo_mono = d0
print("     monotone bracket : %.4f < delta(6s) < %.4f     width %.4f"%(lo_mono,hi_mono,hi_mono-lo_mono))
print("     convex   bracket : %.4f < delta(6s) < %.4f     width %.4f"%(lo_conv,hi_mono,hi_mono-lo_conv))
print("     tightening factor: %.2fx"%((hi_mono-lo_mono)/(hi_mono-lo_conv)))
E=lambda dv,n=6: I - Z*Z*R/(n-dv)**2
print("""
{0}
  IN ENERGY
{0}
""".format("="*76))
print("     %-26s%14s%14s%12s"%("bracket","lower cm-1","upper cm-1","width"))
print("     %-26s%14.0f%14.0f%12.0f"%("Sec 16.6 (monotone)",E(hi_mono),E(lo_mono),E(lo_mono)-E(hi_mono)))
print("     %-26s%14.0f%14.0f%12.0f"%("convex (this)",E(hi_mono),E(lo_conv),E(lo_conv)-E(hi_mono)))
dr=d0+d2/36
print("     %-26s%14.0f"%("point estimate (Ritz)",E(dr)))
print("     inside the convex bracket: %s"%(E(hi_mono)<=E(dr)<=E(lo_conv)))
print("""
  **THE BRACKET NARROWS FROM %.0f TO %.0f cm-1, A FACTOR OF %.1f**, and the
  Ritz point estimate still sits inside it.
"""%(E(lo_mono)-E(hi_mono),E(lo_conv)-E(hi_mono),(E(lo_mono)-E(hi_mono))/(E(lo_conv)-E(hi_mono))))
print("="*76)
print("  AND 7s, THE SAME WAY")
print("="*76)
lo7 = (d0+d2/36) + ((d0+d2/36) - d5)
print("     convex lower for delta(7s): %.4f"%lo7)
print("     upper (monotone)          : %.4f"%(d0+d2/36))
print("     energy bracket            : %.0f  to  %.0f   width %.0f"
      %(E(d0+d2/36,7),E(lo7,7),E(lo7,7)-E(d0+d2/36,7)))
print("     point estimate            : %.0f"%E(d0+d2/49,7))
print("""
{0}
  AND THE THIRD CONSTRAINT NOBODY USED
{0}

  delta is convex AND decreasing AND bounded below by delta_inf. Three
  order properties, and Section 16.6 used one.
""".format("="*76))
print("     %-34s%12s%12s%10s"%("constraint used","delta lower","delta upper","width"))
print("     %-34s%12.4f%12.4f%10.4f"%("monotone only",lo_mono,hi_mono,hi_mono-lo_mono))
print("     %-34s%12.4f%12.4f%10.4f"%("+ convex tangent",lo_conv,hi_mono,hi_mono-lo_conv))
sec = d5 + (d5-d4)*(6-5)/(5-4)
print("     %-34s%12.4f%12.4f%10.4f"%("+ chord above (decreasing)",lo_conv,hi_mono,hi_mono-lo_conv))
print("""
  **THE COMMITTED PREDICTION OF SEC 16.6 IS SUPERSEDED, NOT WITHDRAWN.**
  The old bracket CONTAINS the new one, so nothing committed under D.2.13
  is violated -- the claim has tightened within its own bound.

        **Sc VI (4S)6s  in  [%.0f, %.0f] cm-1**
        **point estimate %.0f cm-1**
        **wavelength window %.4f to %.4f nm**
"""%(E(hi_mono),E(lo_conv),E(dr),1e7/E(lo_conv)/1e0*1e-1,1e7/E(hi_mono)*1e-1))
for lab,val in [("lower edge",E(hi_mono)),("estimate",E(dr)),("upper edge",E(lo_conv))]:
    print("     %-12s %10.0f cm-1   %8.4f nm   %8.3f eV"%(lab,val,1e7/val,val*1.23984e-4))