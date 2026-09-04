import numpy as np
# AME2020 (Wang et al. 2021), BINDING ENERGY/A in keV with 1-sigma, read from mass_1.mas20
# Ni chain (Z=28), experimental values only (no '#' estimates)
rows=[(56,8642.7811,0.0071),(57,8670.9364,0.0099),(58,8732.0621,0.0060),(59,8736.5912,0.0060),
      (60,8780.7769,0.0059),(61,8765.0281,0.0058),(62,8794.5555,0.0069),(63,8763.4955,0.0068),
      (64,8777.4637,0.0072),(65,8736.2424,0.0074),(66,8739.5086,0.0212),(67,8695.7505,0.0431),
      (68,8682.4667,0.0438),(69,8623.0998,0.0540),(70,8604.2917,0.0306),(71,8543.1564,0.0315),
      (72,8520.2118,0.0311),(73,8457.6529,0.0332)]
A=np.array([r[0] for r in rows],float)
B=np.array([r[0]*r[1] for r in rows])          # total binding energy, keV
sB=np.array([r[0]*r[2] for r in rows])         # 1-sigma on total, keV

print("Ni isotopic chain, AME2020 — total binding energy")
print(f"  monotone increasing: {np.all(np.diff(B)>0)}   n = {len(A)}   interior cells = {len(A)-2}")
print(f"  B spans {B[0]/1e3:.1f} -> {B[-1]/1e3:.1f} MeV;  sigma {sB.min():.2f}-{sB.max():.2f} keV")
Sn=np.diff(B)
print(f"  one-neutron separation energies S_n (MeV): "+" ".join(f"{v/1000:.2f}" for v in Sn))
print(f"  odd-even staggering: even-N mean {np.mean(Sn[0::2])/1000:.2f}  odd-N mean {np.mean(Sn[1::2])/1000:.2f} MeV")

r=[];w=[];e=[]
for i in range(1,len(A)-1):
    step=min(abs(B[i]-B[i-1]),abs(B[i+1]-B[i]))
    r.append(step/sB[i]); w.append(abs(B[i+1]-B[i-1]))
    e.append(abs(np.interp(A[i],[A[i-1],A[i+1]],[B[i-1],B[i+1]])-B[i]))
r=np.array(r);w=np.array(w);e=np.array(e)
print(f"\n  r = step/sigma : min {r.min():.3g}  median {np.median(r):.3g}   admission (>=5): {'PASS' if r.min()>=5 else 'FAIL'}")
print(f"  mean bracket width {w.mean()/1000:.2f} MeV   mean interp error {e.mean()/1000:.3f} MeV")
print(f"  V = width/interp error = {w.mean()/e.mean():.2f}")
print(f"\n  per-cell V: "+" ".join(f"{a:.0f}:{ww/ee:.1f}" for a,ww,ee in zip(A[1:-1],w,e)))