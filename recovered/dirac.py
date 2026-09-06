from math import sqrt
import numpy as np
R=109737.31568160; AL=7.2973525693e-3
IE={1:109678.77174307,2:438908.878840,3:987661.0139,4:1756018.8100,5:2744107.933,
6:3952061.7464,7:5380089.932,8:7028394.947,9:8897242.908,10:10986877.95,
11:13297680.72,12:15829951.83,13:18584145.30,14:21560634.27,15:24759946.70,
16:28182531.02,17:31828989.8,18:35699904.7,19:39795795.4,20:44117425.0,
21:48665527.6,22:53440763.5,23:58443949.6,24:63675879.6,25:69137474.7,
26:74829605.3,30:99923562.0,36:144665536.0,40:179351180.0,50:283846660.0,
54:333106090.0,60:415502800.0,70:577288300.0,79:752149200.0,80:773471100.0,
82:817335600.0,92:1063169000.0,110:1648550000.0}

# DOMAIN PROTOCOL: one cell (hydrogenic, Ne=1). carrier (Z*alpha)^2. 38 points,
# 2 parameters -> count satisfied. no pooling. a fit is admissible here.
Z=np.array(sorted(IE)); d=np.array([1-z*sqrt(R/IE[z]) for z in Z]); x=(Z*AL)**2
m=Z>=3                                    # drop H,He: reduced mass dominates there
A=np.vstack([x[m],x[m]**2]).T
coef,*_=np.linalg.lstsq(A,d[m],rcond=None)
pred=A@coef; ss=1-((d[m]-pred)**2).sum()/((d[m]-d[m].mean())**2).sum()
print("FIT  delta = A(Za)^2 + B(Za)^4   on Z>=3, 36 points, 2 parameters")
print(f"   A = {coef[0]:.6f}      B = {coef[1]:.6f}      R^2 = {ss:.8f}")
print(f"   DERIVED prediction from the Dirac 1s energy:  A = 1/8 = 0.125000")
print(f"   ratio measured/derived = {coef[0]/0.125:.4f}   ({100*(coef[0]/0.125-1):+.2f}%)")
print(f"   max |residual| = {np.abs(d[m]-pred).max():.2e}   at Z = {Z[m][np.abs(d[m]-pred).argmax()]}")
# reduced mass, the two dropped points
print("\nTHE TWO DROPPED POINTS — reduced mass, not relativity")
for z,M in ((1,1836.15267343),(2,7294.29954)):
    print(f"   Z={z}: observed {1-z*sqrt(R/IE[z]):+.6f}   reduced-mass prediction "
          f"{1-sqrt(1/(1/(1+1/M))):+.6f}")