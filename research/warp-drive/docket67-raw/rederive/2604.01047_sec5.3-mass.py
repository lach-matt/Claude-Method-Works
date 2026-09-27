#!/usr/bin/env python3
"""DOCKET 67 re-derivation: GMMPS (arXiv:2604.01047 v1) sec. 5.3 matching to Lambda.
Published (p.62-63): gamma~ ~= -b0/b1 = -16 pi G alpha~S1 m^4; H = sqrt(-gamma~);
Lambda = 3 Omega_L H^2 = 6 Omega_L alpha~S1 (m/M_P)^4 M_P^2; with Omega_L ~= 0.685,
Lambda ~= 7.15e-121 M_P^2 (Planck 2018, their [1]) they obtain m ~= 7.8e-3 eV.
Independent of research/warp-drive/linstab.py (constants re-typed from CODATA 2018)."""
import math, sympy as sp

ok = True
def chk(label, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + label)

# ---- 1. symbolic: the published chain, from (5.2) -------------------------
al, m, G, xi, Om, g = sp.symbols('alpha m G xi Omega gamma', positive=True)
kap = 8*sp.pi*G
b0 = -al*4*m**4/(6*(sp.Rational(1, 6)-xi)**2)          # (5.2)
b1 = -(2/kap)/(6*(sp.Rational(1, 6)-xi)**2)             # (5.2)
gt = sp.simplify(-b0/b1)
chk("-b0/b1 = -16 pi G alpha m^4 (xi-independent)", sp.simplify(gt + 16*sp.pi*G*al*m**4) == 0)
H2 = -gt
MP2 = 1/kap                                             # reduced Planck mass^2 = 1/kappa
Lam = 3*Om*H2
chk("3 Omega H^2 = 6 Omega alpha (m/M_P)^4 M_P^2", sp.simplify(Lam - 6*Om*al*(m**2/MP2)**2*MP2) == 0)
# the full linear root with the b2 gamma^2 term: gamma = root of b0 + b1 g + b2 g^2
b2 = sp.symbols('b2', real=True)
root = (-b1 - sp.sqrt(b1**2 - 4*b2*b0))/(2*b2)          # branch -> -b0/b1 as b2 -> 0
ser = sp.series(root.subs(xi, 0), b2, 0, 2).removeO()
chk("b2 -> 0 limit of the quadratic root = -b0/b1", sp.simplify(ser.subs(b2, 0) - gt.subs(xi, 0)) == 0)
rel = sp.simplify((sp.diff(ser, b2)*1)/gt.subs(xi, 0))  # relative first-order b2 correction per unit b2
print("  first-order relative b2 correction coefficient (xi=0):", sp.simplify(rel))

# ---- 2. numeric inversion with the printed data ----------------------------
HBAR, C, GN, E = 1.054571817e-34, 299792458.0, 6.67430e-11, 1.602176634e-19
MP_eV = math.sqrt(HBAR*C/(8*math.pi*GN))*C**2/E          # reduced Planck mass in eV
mPl_eV = math.sqrt(HBAR*C/GN)*C**2/E                     # non-reduced
print("  M_P (reduced) = %.6e eV ; m_Pl = %.6e eV" % (MP_eV, mPl_eV))
a_thm36 = 1/(64*math.pi**2); a_sec51 = 1/(64*math.pi)
def m_of(Lam_MP2, Om_, a):
    return (Lam_MP2/(6*Om_*a))**0.25*MP_eV
m_pr = m_of(7.15e-121, 0.685, a_thm36)
m_ty = m_of(7.15e-121, 0.685, a_sec51)
print("  m (printed Lambda, Omega, alpha=1/64pi^2) = %.4e eV ; printed 7.8e-3" % m_pr)
print("  m (alpha=(64pi)^-1 as printed in 5.1)     = %.4e eV (%.1f%% off)" % (m_ty, 100*(m_ty/7.8e-3-1)))
chk("printed 7.8e-3 eV reproduced within 2% with Thm 3.6's alpha", abs(m_pr/7.8e-3-1) < 0.02)
chk("5.1's (64 pi)^-1 does NOT reproduce it (>20% off)", abs(m_ty/7.8e-3-1) > 0.20)
print("  unrounded value %.3f meV -> 2-sig-fig rounding gives %.1f meV; printed 7.8 (truncation, %.1f%%)"
      % (m_pr*1e3, round(m_pr*1e3, 1), 100*(m_pr/7.8e-3-1)))

# ---- 3. is the printed Lambda consistent with Planck 2018? ----------------
MPC = 3.0856775814913673e22
def H_eV(H0):
    return HBAR*(H0*1e3/MPC)/E
def Lam_MP2(H0, Om_):
    return 3*Om_*H_eV(H0)**2/MP_eV**2
L_pl = Lam_MP2(67.36, 0.6847)
print("  Planck 2018 (67.36, 0.6847): Lambda = %.4e M_P^2 ; = %.3e eV^2 (Planck quotes 4.24e-66)"
      % (L_pl, L_pl*MP_eV**2))
print("  Planck quote 2.846e-122 m_Pl^2 x 8 pi = %.4e M_P^2" % (2.846e-122*8*math.pi))
chk("printed 7.15e-121 is Lambda in REDUCED Planck units (Planck's 2.846e-122 m_Pl^2 x 8pi)",
    abs(2.846e-122*8*math.pi/7.15e-121-1) < 0.005)
chk("printed 7.15e-121 equals 3 Omega H0^2 / M_P^2 from Planck Table 2 within 0.5%", abs(L_pl/7.15e-121-1) < 0.005)

# ---- 4. Lambda/Omega = 3 H0^2: m depends on H0 alone ------------------------
H0_impl = math.sqrt(7.15e-121/(3*0.685))*MP_eV  # eV
H0_kms = H0_impl*E/HBAR*MPC/1e3
print("  implied H0 from printed (Lambda, Omega): %.2f km/s/Mpc" % H0_kms)
def m_from_H0(H0, a=a_thm36):
    return (H_eV(H0)**2*MP_eV**2/(2*a))**0.25
for lab, H0 in [("Planck18 TT,TE,EE+lowE+lensing", 67.36), ("Planck18 +BAO", 67.66),
                ("SH0ES R22 baseline", 73.04), ("SH0ES R22 +TRGB", 72.53)]:
    print("  %-32s H0=%.2f -> m = %.3f meV" % (lab, H0, m_from_H0(H0)*1e3))
chk("m identical whether from (Lambda,Omega) or from H0 alone", abs(m_from_H0(H0_kms)/m_pr-1) < 1e-9)
spread = m_from_H0(73.04)/m_from_H0(67.36)-1
print("  Hubble-tension spread in m: +%.2f%% (m ~ H0^(1/2))" % (100*spread))
chk("Hubble tension moves m by < 5% (order of magnitude unmoved)", spread < 0.05)
# Planck 1-sigma: H0 +-0.54 -> m +-0.4%
print("  Planck 1-sigma on H0 (0.54) -> dm/m = %.2f%%" % (100*0.5*0.54/67.36))

# ---- 5. hypothesis variants (named, not adjudicated) -----------------------
m_omega1 = m_of(7.15e-121, 1.0, a_thm36)
print("  identification H = sqrt(Lambda/3) (asymptotic de Sitter, Omega->1): m = %.3f meV (factor Omega^(1/4)=%.3f)"
      % (m_omega1*1e3, 0.685**0.25))
m_nonred = (7.15e-121/(6*0.685*a_thm36))**0.25*mPl_eV
print("  if M_P were read as non-reduced m_Pl with Lambda unchanged: m = %.3f meV (x (8pi)^(1/4) = %.3f)"
      % (m_nonred*1e3, (8*math.pi)**0.25))

# ---- 6. neglected terms at the matched point --------------------------------
eps = (m_pr/MP_eV)**2
Jcorr = eps/(288*math.pi**2)
print("  kappa m^2 = (m/M_P)^2 = %.3e ; J correction kappa m^2/(288 pi^2) = %.3e" % (eps, Jcorr))
chk("dropping J(z) (the 1/(1+kappa m^2/288pi^2) factor) is negligible at the matched m", Jcorr < 1e-50)
gam_MP = 7.15e-121/(3*0.685)                          # |gamma0|/M_P^2
b1_MP = 12.0                                          # xi=0: b1 = 2/(kappa*6*(1/6)^2) = 12 M_P^2
print("  b2-term valid iff |b2| << b1/|gamma0| = %.2e (M_P units, xi=0)" % (b1_MP/gam_MP))
print("ALL PASS" if ok else "SOME FAIL")
raise SystemExit(0 if ok else 1)
