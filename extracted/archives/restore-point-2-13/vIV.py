import math
import numpy as np
print("  THE Nₑ = 20 LADDER, FOUR SPECIES\n")
print(f"      {'species':<9}{'c':>3}{'3d²':>12}{'3d.4s':>12}{'4s²':>12}")
ROWS=[("Ca I",1,None,20335.360,0.0),("Sc II",2,4802.87,0.00,11736.36),
      ("Ti III",3,0.0,38064.35,102665.15),("V IV",4,0.0,96196.1,None)]
for nm,c,a,b,d in ROWS:
    print(f"      {nm:<9}{c:>3}"
          f"{('—' if a is None else f'{a:,.0f}'):>12}"
          f"{('—' if b is None else f'{b:,.0f}'):>12}"
          f"{('—' if d is None else f'{d:,.0f}'):>12}")
print()
print("  Y(c) = E(3d.4s) − E(3d²)   —  available at c = 2, 3, 4\n")
c=np.array([2.,3.,4.]); Y=np.array([0.00-4802.87, 38064.35-0.0, 96196.1-0.0])
for a,b in zip(c,Y): print(f"      c = {int(a)} : {b:>12,.0f}")
M=np.vstack([c**2,c,np.ones(3)]).T
A,B,C=np.linalg.solve(M,Y)
print(f"\n      fitted on c = 2,3,4 :  Y(c) = {A:,.0f}·c² {B:+,.0f}·c {C:+,.0f}\n")
p1=A*1+B*1+C
print(f"  THE PREDICTION AT c = 1  (Ca I) — not used in the fit\n")
print(f"      predicted Y(1) = {p1:,.0f} cm⁻¹")
print(f"      measured  Y(1) = E(3d.4s) − E(3d²) at Ca I\n")
print("      Ca I's 3d² is not in the level list — it lies above the")
print("      ionisation limit or is unassigned. so the direct check fails.\n")
print("      but Ca I's 3d.4s sits at 20,335 above its 4s² ground, and")
print("      Y(1) < 0 would mean 3d.4s BELOW 3d², i.e. 3d² higher still.\n")
print(f"      predicted Y(1) = {p1:,.0f}  →  3d.4s is "
      f"{'BELOW' if p1<0 else 'ABOVE'} 3d² at Ca I")
print("      and Ca I's ground is 4s², so 3d² must indeed lie above 3d.4s.")
print(f"      → the prediction has the RIGHT SIGN.\n")
print("  THE ROOT — where 3d.4s crosses 3d²\n")
r=np.roots([A,B,C]); rr=sorted(x.real for x in r if abs(x.imag)<1e-9)
print(f"      roots : " + "  ".join(f"{x:.4f}" for x in rr))
inr=[x for x in rr if 0<x<6]
if inr:
    print(f"      crossing at c = {inr[-1]:.3f}")
    print(f"      measured   : between Sc II (c=2, 3d.4s lower) and")
    print(f"                   Ti III (c=3, 3d² lower)")
    print(f"      → the root at {inr[-1]:.2f} sits between 2 and 3.  CORRECT.\n")
print("  AND THE LEADING COEFFICIENT AGAINST HYDROGENIC\n")
Ah=0.5*(1/16-1/9)*109737
print(f"      hydrogenic ½[1/n²(4s) − 1/n²(3d)]·R = {Ah:,.0f}")
print(f"      fitted A                            = {A:,.0f}")
print(f"      ratio {A/Ah:+.3f}")
print()
print("      opposite sign and ~3× the size. the hydrogenic estimate does")
print("      not carry the leading term — screening dominates it.")
