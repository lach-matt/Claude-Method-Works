#!/usr/bin/env python3
"""DOCKET 67 audit: 'planck-cosmological-parameters-via-2604.01047'.

The tree (linstab.py:318-319) carries GMMPS 5.3's printed Lambda = 7.15e-121 M_P^2
and Omega_Lambda = 0.685, and uses them (linstab.py:630-633) to invert
Lambda = 6 Omega alpha (m/M_P)^4 M_P^2 for m, as a CONTROL that GMMPS's
m ~ 7.8e-3 eV is reproduced with alpha = 1/(64 pi^2) and not with (64 pi)^-1,
and to set eps = (m/M_P)^2 for the selftest brackets.

PRIMARY SOURCE (READ via alphaXiv, arXiv:1807.06209v4 p.17 eq.(15)):
  Omega_Lambda = 0.6847 +- 0.0073 (68%, TT,TE,EE+lowE+lensing)
  Lambda = (4.24 +- 0.11) e-66 eV^2 = (2.846 +- 0.076) e-122 m_Pl^2, m_Pl the PLANCK mass
  H0 = 67.36 +- 0.54 km/s/Mpc (eq.(14)); base-LCDM, flat, one 0.06 eV neutrino.
GMMPS (READ, arXiv:2604.01047v1 pp.62-63) says M_P is the REDUCED Planck mass.

Checks:
 C1  2.846e-122 m_Pl^2 * 8 pi (m_Pl^2 = 8 pi M_P^2) = 7.15e-121 M_P^2  (exact factor, sympy)
 C2  Lambda = 3 Omega_L H0^2 from Planck's H0, Omega_L and CODATA constants
     reproduces 4.24e-66 eV^2 and 2.846e-122 m_Pl^2 and 7.15e-121 M_P^2
 C3  Omega_Lambda CANCELS in the GMMPS inversion (sympy): m^4 = H0^2 M_P^2/(2 alpha);
     the tree's m depends on H0 = sqrt(Lambda/(3 Omega)) alone
 C4  m from printed values, alpha = 1/(64 pi^2) and (64 pi)^-1; H0 implied by the printed pair
 C5  sensitivity: H0 window keeping the tree's 2% control and 20% typo test; eps brackets
     re-run at eps scaled by H0 ratios over a wide window (0.8 .. 1.25)
Stdlib + sympy + mpmath; imports linstab READ-ONLY with bytecode writing disabled.
"""
import sys, math
sys.dont_write_bytecode = True
import sympy as sp

WD = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, WD)
import linstab            # noqa: E402  read-only
import mpmath as mp       # noqa: E402

ok_all = True
def chk(name, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("   " + detail if detail else ""))

# ---- constants (CODATA 2018 exact/recommended; same as achievable.py) ----
HBAR, C, G, E = 1.054571817e-34, 299792458.0, 6.67430e-11, 1.602176634e-19
MPC = 3.0856775814913673e22     # m (IAU 2015 pc = 648000/pi au exactly, au exact)
mPl_eV = math.sqrt(HBAR * C / G) * C**2 / E
MP_eV = mPl_eV / math.sqrt(8 * math.pi)
chk("reduced Planck mass agrees with linstab.reduced_planck_ev()",
    abs(MP_eV / linstab.reduced_planck_ev() - 1) < 1e-12, "%.6e eV" % MP_eV)

# ---- C1 ----
x = sp.Symbol('x', positive=True)
conv = sp.Rational(2846, 1000) * sp.Rational(1, 10**122) * 8 * sp.pi
val = float(conv)
chk("C1 Planck 2.846e-122 m_Pl^2 -> %.4e M_P^2 (reduced) rounds to 7.15e-121" % val,
    round(val / 1e-121, 2) == 7.15)
lo, hi = float((2.846 - 0.076) * 8 * sp.pi) * 1e-122, float((2.846 + 0.076) * 8 * sp.pi) * 1e-122
print("     Planck 68%% band in M_P^2: [%.3e, %.3e]" % (lo, hi))
chk("C1' misreading M_P as the unreduced mass would be off by 8 pi (m by (8pi)^(1/4) = %.3f)"
    % (8 * math.pi) ** 0.25, True)

# ---- C2 ----
def lam_eV2(H0, OL):
    H = H0 * 1e3 / MPC                 # s^-1
    return 3 * OL * (HBAR * H / E) ** 2
L = lam_eV2(67.36, 0.6847)
chk("C2 Lambda = 3 Omega_L H0^2 = %.4e eV^2 (Planck prints 4.24 +- 0.11 e-66)" % L,
    abs(L / 4.24e-66 - 1) < 0.005)
chk("C2 in m_Pl^2: %.4e (Planck prints 2.846e-122)" % (L / mPl_eV**2),
    abs(L / mPl_eV**2 / 2.846e-122 - 1) < 0.003)
chk("C2 in M_P^2: %.4e (GMMPS prints 7.15e-121)" % (L / MP_eV**2),
    abs(L / MP_eV**2 / 7.15e-121 - 1) < 0.003)
chk("C2 Omega_L h^2 = %.4f (Planck prints 0.3107)" % (0.6847 * 0.6736**2),
    abs(0.6847 * 0.6736**2 - 0.3107) < 5e-4)

# ---- C3 ----
Om, H, a, m, MPs = sp.symbols('Omega H alpha m M_P', positive=True)
Lam = 3 * Om * H**2
m4 = sp.solve(sp.Eq(Lam, 6 * Om * a * (m / MPs)**4 * MPs**2), m**4)[0]
chk("C3 Omega cancels: m^4 = H^2 M_P^2/(2 alpha)", sp.simplify(m4 - H**2 * MPs**2 / (2 * a)) == 0,
    str(m4))
chk("C3 same as GMMPS's -b0/b1 = -16 pi G alpha m^4, H^2 = -gamma (kappa = 1/M_P^2 = 8 pi G)",
    sp.simplify(2 * a * m**4 / MPs**2 - 16 * sp.pi * (1 / (8 * sp.pi * MPs**2)) * a * m**4) == 0)

# ---- C4 ----
m_thm, eps_thm = linstab.gmmps_mass_ev(1 / (64 * math.pi**2))
m_typ, _ = linstab.gmmps_mass_ev(1 / (64 * math.pi))
print("     m (1/(64 pi^2)) = %.4e eV, eps = %.4e ; m (1/(64 pi)) = %.4e eV" % (m_thm, eps_thm, m_typ))
chk("C4 m with Thm 3.6 alpha within 2%% of printed 7.8e-3 (rel %.4f)" % (m_thm / 7.8e-3 - 1),
    abs(m_thm / 7.8e-3 - 1) < 0.02)
chk("C4 m with 5.1's alpha is > 20%% off (rel %.4f); ratio = pi^(1/4) = %.4f exactly"
    % (m_typ / 7.8e-3 - 1, math.pi ** 0.25), abs(m_typ / 7.8e-3 - 1) > 0.2
    and abs(m_thm / m_typ - math.pi ** 0.25) < 1e-12)
H_implied_eV = math.sqrt(7.15e-121 / (3 * 0.685)) * MP_eV
H_implied = H_implied_eV * E / HBAR * MPC / 1e3
chk("C4 printed pair implies H0 = %.3f km/s/Mpc (Planck 67.36)" % H_implied,
    abs(H_implied - 67.36) < 0.1)

# ---- C5 ----
# m proportional to H0^(1/2): window keeping |m/7.8e-3 - 1| < 0.02
r_lo, r_hi = (0.98 * 7.8e-3 / m_thm) ** 2, (1.02 * 7.8e-3 / m_thm) ** 2
print("     2%%-control H0 window: [%.2f, %.2f] km/s/Mpc" % (r_lo * H_implied, r_hi * H_implied))
r_typ = (0.8 * 7.8e-3 / m_typ) ** 2
print("     typo test (m_typ > 20%% below the FIXED printed 7.8e-3) would stop discriminating only"
      " at an H0 ratio >= %.4f, i.e. H0 >= %.2f; the alpha-to-alpha ratio pi^(1/4) is data-free"
      % (r_typ, r_typ * H_implied))
for H0x, lab in ((67.66, "Planck+BAO (READ, Table 2)"), (67.36 - 3 * 0.54, "Planck -3 sigma"),
                 (67.36 + 3 * 0.54, "Planck +3 sigma")):
    r = H0x / H_implied
    print("     H0 = %.2f (%s): m = %.4e eV, rel to 7.8e-3 = %+.4f" % (H0x, lab, m_thm * r**0.5,
                                                                    m_thm * r**0.5 / 7.8e-3 - 1))
brk = True
for r in (0.8, 0.9, 1.1, 1.25):
    for xi in (0, sp.Rational(1, 3)):
        lo_, hi_, _g = linstab.s_root_bracket(mp, eps_thm * r, xi, 10 ** 100)
        brk &= (lo_ > 0 and hi_ < 0)
chk("C5 selftest brackets (xi = 0, 1/3; |b2|<=1e100) still fire with eps scaled 0.8..1.25", brk)
print("\nALL PASS" if ok_all else "\nSOME FAIL")
sys.exit(0 if ok_all else 1)
