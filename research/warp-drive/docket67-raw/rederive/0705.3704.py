#!/usr/bin/env python3
"""DOCKET 67 -- audit of arXiv:0705.3704v2 (Flambaum, 'Variation of fundamental
constants: theory and observations', 21 Jun 2007) as used by
research/warp-drive/address.py and excite.py.  READ-ONLY on the tree.

Two results live under this key:
  R1  p.4: 'The proton mass is proportional to Lambda_QCD (M_p ~ 3 Lambda_QCD)'
      -> the tree's H2, f = d ln m_p/d ln v = S.
  R2  p.5 eq. (9): 'A rough estimate ... dw/w ~ 10^5 (2 da/a + 0.5 dX_q/X_q
      - 5 dX_s/X_s) (7 eV/w)'  -> TH229_* in address.py section 8.

Every external number below carries its source and read status.
"""
import sys, math
from fractions import Fraction
import sympy as sp

sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import address as A  # read-only import

ok_all = True
def chk(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + label)

print("=== R2: eq. (9) transcription, READ at 0705.3704v2 p.5 ===")
PUB = {"enh": 1e5, "alpha": 2.0, "X_q": 0.5, "X_s": -5.0, "omega_norm_eV": 7.0}
chk("TH229_ENHANCEMENT == 1e5 (eq. 9)", A.TH229_ENHANCEMENT == PUB["enh"])
chk("TH229_COEFFS == {2, 0.5, -5} (eq. 9)",
    A.TH229_COEFFS == {"alpha": 2.0, "X_q": 0.5, "X_s": -5.0})
chk("TH229_OMEGA_EV == 7 eV normalisation (eq. 9)", A.TH229_OMEGA_EV == 7.0)

print("\n=== R2: the tree's coefficient re-derived from eq. (9) ===")
def coeff(k_alpha, kx, omega=7.0, enh=1e5, cq=0.5, cs=-5.0, ca=2.0):
    return enh * (ca * k_alpha + cq * kx + cs * kx) * (7.0 / omega)
kx_H1 = 1 - 2/9
c_H1 = coeff(A.K_alpha("H1"), kx_H1)
c_H2 = coeff(0.0, 1.0)
print("  H1 coeff %.6e  (tree %.6e)" % (c_H1, A.th229_coefficient("H1")))
print("  H2 coeff %.6e  (tree %.6e)" % (c_H2, A.th229_coefficient("H2")))
chk("H1 coefficient reproduced", abs(c_H1 / A.th229_coefficient("H1") - 1) < 1e-12)
chk("H2 coefficient reproduced", abs(c_H2 / A.th229_coefficient("H2") - 1) < 1e-12)
alpha_share = abs(2 * A.K_alpha("H1") / (2 * A.K_alpha("H1") - 4.5 * kx_H1))
print("  share of |inner| carried by the alpha term under H1: %.3e" % alpha_share)
xs_share = 5 * kx_H1 / (5 * kx_H1 + 0.5 * kx_H1)
print("  X_s term / (|X_q|+|X_s|) terms: %.4f  -> the X_s coefficient dominates" % xs_share)

print("\n=== R2 DATA: transition energy ===")
# Flambaum 2007 p.5: 3.5+-1 eV [Helmer-Reich], 5.5+-1 [Guimaraes-Filho], 7.6+-0.5 [Beck 2007].
# Now: nu = 2 020 407 384 335(2) kHz  (Zhang et al. 2024, READ via 2407.17300 p.1-2);
#      Delta E = 8.355 733 554 021(8) eV (READ as quoted in 2407.17526 p.2).
h_eVs = 4.135667696923859e-15   # exact SI h/e, eV s
nu = 2020407384335e3
omega_now = h_eVs * nu
print("  omega from nu (exact h/e): %.9f eV" % omega_now)
chk("nu and quoted Delta E agree to 1e-9", abs(omega_now - 8.355733554021) < 1e-8)
f_omega = 7.0 / omega_now
print("  (7 eV / omega) at the measured omega = %.6f ; tree uses 1 (omega=7)" % f_omega)
for hyp in ("H1", "H2"):
    c7 = A.th229_coefficient(hyp)
    cnow = A.th229_coefficient(hyp, omega_ev=omega_now)
    print("  %s coeff at 7 eV %.4e -> at %.4f eV %.4e ; eps_det(1e-18) %.4e -> %.4e"
          % (hyp, c7, omega_now, cnow, 1e-18 / abs(c7), 1e-18 / abs(cnow)))
print("  1998-2007 range 3.5..7.6 eV spanned a factor %.2f in (7eV/omega)"
      % ((7 / 3.5) / (7 / 7.6)))

print("\n=== R2 DATA: alpha sensitivity now MEASURED ===")
K_eq9_now = PUB["enh"] * PUB["alpha"] * f_omega
dEC_eq9 = PUB["enh"] * PUB["alpha"] * 7.0 / 1e6   # MeV
print("  eq.(9) implied K_alpha at measured omega: %.4e" % K_eq9_now)
print("  eq.(9) implied Delta E_C = 2e5 * 7 eV = %.3f MeV" % dEC_eq9)
# Beeks et al. 2024 (2407.17300 p.3, eqs 8-10): Delta E_C = 0.049(19) MeV, K = 5900(2300)
K_meas, dK = 5900.0, 2300.0
dEC_meas = 0.049
print("  Beeks 2024: K = %.0f +- %.0f ; Delta E_C = %.3f MeV" % (K_meas, dK, dEC_meas))
print("  check K = dE_C/omega: %.0f" % (dEC_meas * 1e6 / omega_now))
chk("Beeks K consistent with its own dE_C/omega (within 3%)",
    abs(dEC_meas * 1e6 / omega_now / K_meas - 1) < 0.03)
r = K_eq9_now / K_meas
print("  eq.(9)/measured = %.1f  (1-sigma range %.1f .. %.1f)"
      % (r, K_eq9_now / (K_meas + dK), K_eq9_now / (K_meas - dK)))
print("  Beeks model caveat (p.4): a 1% differential octupole change moves K by 2850")

print("\n=== R2 LATER: X_q coefficient estimates, all normalised to omega_now ===")
# eq.(9): 0.5e5 at 7 eV.  Flambaum-Wiringa 0807.4943 p.3 eq.(7): 1.5e5 at 7.6 eV;
# they quote Ref.[3] (Flambaum 2006) as 0.4e5 and He-Ren 2007 as 0.7e5 at 7.6 eV.
ests = {"eq.9 (this paper)": 0.5e5 * 7.0,
        "Flambaum 2006 via FW": 0.4e5 * 7.6,
        "He-Ren 2007 via FW": 0.7e5 * 7.6,
        "Flambaum-Wiringa 2008": 1.5e5 * 7.6}
for k, v in ests.items():
    print("  %-24s K_Xq = %.3e" % (k, v / omega_now))
spread = max(ests.values()) / min(ests.values())
print("  spread of published X_q coefficients: factor %.2f" % spread)
print("  X_s coefficient (-5e5 at 7 eV): no independent later estimate read here;"
      " FW 0807.4943 p.1 excludes it ('larger uncertainty')")

print("\n=== R2 SCENARIOS on the tree's figure (tree claims section 9 does not"
      " depend on it; NOT re-verified here) ===")
elec = 1e-18   # tree's electronic-courier eps_det (coefficient 1 at 1e-18)
rows = []
for label, enh, cq in (("eq.9 as used", 1e5, 0.5),
                       ("eq.9, FW X_q", 1e5, 1.5e5 * 7.6 / 7.0 / 1e5),
                       ("enh 1e4 (Caputo 'order 1e4')", 1e4, 0.5)):
    c = coeff(A.K_alpha("H1"), kx_H1, omega=omega_now, enh=enh, cq=cq)
    e = elec / abs(c)
    rows.append((label, c, e))
    print("  %-30s H1 coeff %.3e  eps_det %.3e  gain over electronic %.2e"
          % (label, c, e, 1e-18 / e))
chk("in every scenario the nuclear courier still beats the electronic one by >1e3",
    all(1e-18 / e > 1e3 for _, _, e in rows))

print("\n=== R1: M_p ~ Lambda_QCD and the tree's H2, symbolic ===")
Lam, v, S = sp.symbols("Lambda v S", positive=True)
c = sp.symbols("c", positive=True)
F = sp.Function("F")
x = sp.symbols("x", positive=True)
# m_p = Lambda * F(m_q/Lambda), m_q = c v, Lambda held fixed (H2)
mp = Lam * F(c * v / Lam)
dln = sp.simplify(sp.diff(sp.log(mp), v) * v)
# Feynman-Hellmann: S = m_q dm_p/dm_q / m_p = x F'(x)/F(x) at x = m_q/Lambda
Sfh = (x * sp.diff(F(x), x) / F(x)).subs(x, c * v / Lam)
chk("H2: d ln m_p/d ln v == Feynman-Hellmann S exactly",
    sp.simplify(dln - sp.simplify(Sfh.doit())) == 0)
# Flambaum's statement is the chiral limit F = const: then S = 0 and mu <-> X_e exactly.
Kmu = lambda s: s - 1
chk("Flambaum's mu == X_e identity is the S -> 0 limit of the tree's K_mu = S - 1",
    Kmu(0) == -1 and A.K_mu(Fraction(0), "H2") == -1)

print("\n=== R1 DATA: S = sum sigma_q / m_p ===")
mp_MeV = 938.27208816
sig = {"RS 2015 sigma_piN (1506.04142, READ)": 59.1,
       "RS isospin-limit, as quoted in 2303.08741 (READ)": 55.9,
       "Mainz lattice 2023 sigma_piN (2303.08741, READ)": 43.7}
sig_s = 28.6   # Mainz 2023 sigma_s, READ; +-9.3
for k, sv in sig.items():
    print("  %-50s S_light = %.4f ; +sigma_s %.4f" % (k, sv / mp_MeV, (sv + sig_s) / mp_MeV))
Smin, Smax = 43.7 / mp_MeV, (59.1 + sig_s) / mp_MeV
rho06 = A.COURIER_SOURCE_KG_M3["H2"]
print("  S span (light only low .. light+strange high): %.4f .. %.4f ; tree scan 0.0096/0.06/0.09"
      % (Smin, Smax))
print("  H2 stable-matter density at eps=1e-18: tree %.4e ; over the S span %.3e .. %.3e kg/m^3"
      % (rho06, rho06 * 0.06 / Smax, rho06 * 0.06 / Smin))
chk("over the whole S span the H2 density stays > 1e7 x osmium (22590 kg/m^3)",
    rho06 * 0.06 / Smax / 22590 > 1e7)

print("\n=== R1: the '~3' (scheme-dependent ratio), 2-loop MSbar, inputs NAMED-NOT-READ ===")
def b0(nf): return (33 - 2 * nf) / (12 * math.pi)
def b1(nf): return (153 - 19 * nf) / (24 * math.pi ** 2)
def run(a, mu0, mu1, nf, n=4000):
    t0, t1 = math.log(mu0 ** 2), math.log(mu1 ** 2)
    h = (t1 - t0) / n
    f = lambda a: -(b0(nf) * a ** 2 + b1(nf) * a ** 3)
    for _ in range(n):
        k1 = f(a); k2 = f(a + h * k1 / 2); k3 = f(a + h * k2 / 2); k4 = f(a + h * k3)
        a += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return a
def lam2(a, mu, nf):
    B0, B1 = b0(nf), b1(nf)
    return mu * math.exp(-1 / (2 * B0 * a) - (B1 / (2 * B0 ** 2)) * math.log(B0 * a / (1 + B1 * a / B0)))
aZ, mZ, mb, mc = 0.1180, 91.1876, 4.18, 1.27   # NAMED-NOT-READ (PDG-style inputs)
a_b = run(aZ, mZ, mb, 5); a_c = run(a_b, mb, mc, 4)
L3 = lam2(a_c, mc, 3) * 1000
print("  2-loop Lambda^(3) ~ %.0f MeV ; m_p/Lambda^(3) ~ %.2f" % (L3, mp_MeV / L3))
chk("m_p / Lambda^(3) is O(3) (between 2 and 4) at 2 loops", 2 < mp_MeV / L3 < 4)

print("\nALL CHECKS PASS" if ok_all else "\nSOME CHECK FAILED")
sys.exit(0 if ok_all else 1)
