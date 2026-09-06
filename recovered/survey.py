import numpy as np

def audit(name, x, y, sigma_abs, note=""):
    """x: channel index, y: values, sigma_abs: 1-sigma absolute measurement error (scalar or array)"""
    y=np.array(y,float); x=np.array(x,float); s=np.full(len(y),sigma_abs,float) if np.isscalar(sigma_abs) else np.array(sigma_abs,float)
    mono = np.all(np.diff(y)>0) or np.all(np.diff(y)<0)
    viol = int(np.sum(np.diff(y)<=0)) if y[-1]>y[0] else int(np.sum(np.diff(y)>=0))
    rs=[]; widths=[]; interp_err=[]
    for i in range(1,len(y)-1):
        step=min(abs(y[i]-y[i-1]),abs(y[i+1]-y[i]))
        rs.append(step/s[i])
        widths.append(abs(y[i+1]-y[i-1]))
        p=np.interp(x[i],[x[i-1],x[i+1]],[y[i-1],y[i+1]])
        interp_err.append(abs(p-y[i]))
    rs=np.array(rs); widths=np.array(widths); interp_err=np.array(interp_err)
    V = widths.mean()/max(interp_err.mean(),1e-12)
    print(f"\n{name}")
    print(f"  monotone: {'yes' if mono else f'NO ({viol} reversals)'}   interior cells: {len(rs)}   range: {y.max()/y.min() if y.min()>0 else float('nan'):.3g}x")
    print(f"  r = step/sigma : min {rs.min():.3g}  median {np.median(rs):.3g}  -> admission (>=5): {'PASS' if rs.min()>=5 else 'FAIL at some cells' if rs.max()>=5 else 'FAIL'}")
    print(f"  mean bracket width {widths.mean():.4g}   mean interp error {interp_err.mean():.4g}   V = width/err = {V:.3g}")
    if note: print(f"  {note}")
    return rs,V

C=np.arange(4,15)
# --- n-alkane transition temperatures (K), handbook values; sigma taken as 0.3 K
bp=[272.7,309.2,341.9,371.6,398.8,424.0,447.3,469.1,489.5,508.6,526.7]
mp=[134.9,143.4,177.8,182.6,216.4,219.7,243.5,247.6,263.6,267.8,279.0]
audit("n-alkane BOILING points, C4-C14 (sigma 0.3 K)",C,bp,0.3)
audit("n-alkane MELTING points, C4-C14 (sigma 0.3 K)",C,mp,0.3,
      "steps alternate: "+", ".join(f"{d:.1f}" for d in np.diff(mp)))
# melting point below C4 breaks monotonicity
audit("n-alkane MELTING points, C1-C6 (sigma 0.3 K)",np.arange(1,7),[90.7,90.4,85.5,134.9,143.4,177.8],0.3,
      "C2->C3 decreases: propane melts below ethane")
# --- enthalpy of vaporisation 298 K, kJ/mol, sigma 0.2
audit("n-alkane dHvap(298), C5-C12 (sigma 0.2 kJ/mol)",np.arange(5,13),
      [26.4,31.6,36.6,41.5,46.6,51.4,56.6,61.5],0.2)
# --- nuclear: total binding energy along the tin isotopic chain, approx B = A*(B/A)
# B/A near 8.5 MeV; use representative Sn A=112..124, B/A from AME ~8.514..8.467 MeV
A=np.arange(112,125); BA=np.array([8.5144,8.5227,8.5228,8.5145,8.5140,8.5045,8.5040,8.4936,8.4926,8.4816,8.4788,8.4674,8.4673])
audit("Sn isotopic chain, TOTAL binding energy (sigma 5 keV)",A,A*BA*1000,5.0,
      "AME2020 typical sigma 0.1-100 keV; 5 keV used")
# --- in-domain reference
print("\nRydberg reference (Ba I 6s-nf, from the paper)")
print("  r = step/sigma : neighbour spacing ~400 cm-1 / sigma 1e-3 cm-1 -> r ~ 4e5  PASS")
print("  mean bracket width 397 cm-1   Ritz point-estimate rms 20.5 cm-1   V = 19.4")
print("\nOH + n-alkane kinetics (section 10.2)")
print("  r = 0.7-5.4  -> FAIL for C>=9;   V: width 95% of value vs interp error 3.2%  -> V = 30")