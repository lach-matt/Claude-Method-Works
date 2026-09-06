"""Screening Bracket calculator — every conversion pre-computed.
Model: lambda(m) = C * exp(-2G0/sqrt(m)), m = effective screening coordinate (units m_e).
Molecular-barrier WKB scaling: 2G proportional to sqrt(mu_nuclear / m_screening).
Calibration anchors (provenance in annex): d-d lambda(1)=3e-64 /s [verified to source];
second anchor (a) KN threshold m=10 <-> watt-scale, (b) muonic m=207 <-> ~1e9 /s [recalled].
p-d: same barrier scaling x sqrt(mu_pd/mu_dd)=sqrt(2/3); prefactor pinned at lambda_pd(1)=1e-55 [recalled, flag].
"""
import math
eV=1.602176634e-19; NA=6.022e23; PAIRS=NA/2
lam_dd_1=3e-64; lam_pd_1=1e-55
# --- calibration of 2G0 (d-d) from two independent second anchors ---
wattscale_perpair = (1/(3.651e6*eV)*0.5*2)/PAIRS   # ~1.9e12/s/W total dd events per mol -> per pair at 1 W
a_kn  = math.log((1.9e12/PAIRS)/lam_dd_1)/(1-1/math.sqrt(10))
a_mu  = math.log(1e9/lam_dd_1)/(1-1/math.sqrt(207))
G2 = (a_kn+a_mu)/2; dG = abs(a_kn-a_mu)/2
G2_pd = G2*math.sqrt(2/3); dG_pd = dG*math.sqrt(2/3)
def lam(m, base, g2): return base*math.exp(g2*(1-1/math.sqrt(m)))
def m_star(target_perpair, base, g2):
    x = 1 - math.log(target_perpair/base)/g2
    return 1/x**2
# --- targets ---
det_floor = 10/PAIRS                       # 10 events/s in a mole-scale sample
watt_pd   = (1/(5.493e6*eV))/PAIRS
watt_dd   = (1.9e12)/PAIRS
U1 = 27.0  # eV, molecular screening at m=1 [recalled; flag] -> U_e ~ m*U1
rows=[]
for label, base, g2, dg2, wt in [("p+d", lam_pd_1, G2_pd, dG_pd, watt_pd),
                                 ("d+d", lam_dd_1, G2,   dG,   watt_dd)]:
    md  = m_star(det_floor, base, g2)
    mdl = m_star(det_floor, base, g2+dg2); mdh = m_star(det_floor, base, g2-dg2)
    mw  = m_star(wt, base, g2)
    rows.append((label, g2, dg2, md, mdl, mdh, md*U1, mw, mw*U1))
print(f"2G0(dd) from KN anchor: {a_kn:.1f}   from muonic anchor: {a_mu:.1f}   adopted {G2:.1f} ± {dG:.1f}")
print(f"2G0(pd) scaled: {G2_pd:.1f} ± {dG_pd:.1f}")
for r in rows:
    print(f"{r[0]}: m*_detect = {r[3]:.2f} (env {r[4]:.2f}–{r[5]:.2f})  -> U_e ≈ {r[6]:.0f} eV ;  m*_watt = {r[7]:.1f} -> U_e ≈ {r[8]:.0f} eV")
# sanity: muonic check for dd
print(f"model at m=207 (dd): {lam(207,lam_dd_1,G2):.1e} /s  (measured muonic ~1e9)")
# --- signal chain ---
print("\nExposure table (p+d), gamma eff=1e-2, continuum b=0.05 c/s in window, 3He MS floor 1e-12 mol:")
print(f"{'P (W)':>8} {'γ det/day':>12} {'5σ live-time':>14} {'days to 3He':>12}")
for P in [1e-11,1e-9,1e-7,1e-5,1e-3,1e-1]:
    r_src=P/(5.493e6*eV); r_det=r_src*1e-2
    # 5 sigma over continuum: r_det*t >= 5*sqrt(b*t) -> t = 25 b / r_det^2
    t5 = 25*0.05/r_det**2
    t_he = 1e-12/(1.63e-7*P)
    print(f"{P:8.0e} {r_det*86400:12.3e} {t5:12.2e} s {t_he:10.2e}")
# --- bound formula ---
print("\nnull at sensitivity s (events/s, mole-scale): eta_max = s / (base*PAIRS)")
for s,label,base in [(10,"p+d",lam_pd_1),(10,"d+d",lam_dd_1)]:
    print(f"  {label}: s={s}/s -> eta_max = {s/(base*PAIRS):.1e}  ({math.log10(s/(base*PAIRS)):.1f} orders)")