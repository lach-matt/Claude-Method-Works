import numpy as np
R=1.0
def V(nus):
    nus=np.array(nus,float); T=R/nus**2
    return abs(T[0]-T[2])/abs(T[1]-0.5*(T[0]+T[2]))
print("Rydberg channel: V against sampling stride p  (V = w/e at the middle cell)")
print(f"{'nu':>5}" + "".join(f"{('p='+str(p)):>9}" for p in [1,2,3,5,8,12,16]))
for nu in [4,8,12,21,30,50]:
    row=f"{nu:>5}"
    for p in [1,2,3,5,8,12,16]:
        row += f"{V([nu-p,nu,nu+p]):9.2f}" if nu-p>0.5 else f"{'--':>9}"
    print(row)
print("\nfloor of Prop 14.1 = 2.000 ; Rydberg stride-1 floor (Prop 14.3) = 2.909")
print("\n--- the paper's own gappy predictions (Ba I 6snf, delta=0.16) ---")
d=0.16
for lo,mid,hi,lab in [(7,8,9,"6s8f  (gap of 1)"),(12,13,17,"6s13f (gap of 4)"),
                      (12,14,17,"6s14f"),(12,15,17,"6s15f"),(12,16,17,"6s16f"),
                      (16,17,18,"6s17f (contiguous, for scale)")]:
    v=[lo-d,mid-d,hi-d]; print(f"  {lab:32s} V = {V(v):6.2f}")
print("\n--- Sc VI (4S) ns, Z_eff=6, the paper's own Z_eff=6 prediction ---")
dd=(1.0057+0.9812)/2
print(f"  5s cell (4s,5s,6s): V = {V([4-dd,5-dd,6-dd]):.2f}")
print("\n--- fixed-budget scaling over a fixed range ---")
print("  bracket width  w ~ 2h|y'|      -> falls as 1/B")
print("  interp error   e ~ h^2|y''|/2  -> falls as 1/B^2")
print("  so V ~ 1/h ~ B : halving the budget halves V and doubles w")
for B in [4,8,16,32]:
    h=32/B; nu=21.0
    print(f"   budget B={B:3d} (stride {h:4.1f}): V={V([nu-h,nu,nu+h]):6.2f}  bracket width (arb) {abs(R/(nu-h)**2-R/(nu+h)**2)*1e4:7.2f}")