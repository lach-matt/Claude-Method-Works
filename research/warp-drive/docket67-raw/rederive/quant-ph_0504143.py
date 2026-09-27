#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of Sopova & Ford, quant-ph/0504143 eq. (15):

    T_xx ~ (1/2) U ~ (sqrt2 omega_p / (128 pi)) / z^3,   z -> 0,

(Heaviside-Lorentz, hbar = c = 1), and of the tree's use of it in tolman.py
(K_SF_COEFF = sqrt2/(128 pi); crossover coefficient 60 sqrt2 pi/128; a_c/lambdabar_p).

Sections
  1. sympy: the leading asymptotic of eq. (35) of quant-ph/0204125 (the one-interface U),
     done in closed form for a GENERAL eps(i zeta):  U ~ I/(16 pi^2 z^3),
     I = INT_0^inf dzeta (eps-1)/(eps+1).  Plasma model: I = pi omega_p/(2 sqrt2).
  2. sympy: T_xx (eq. 14, a -> inf) = U/2 exactly at the position-dependent level.
  3. numeric: the EXACT one-interface integral, z^3 U/omega_p as omega_p z -> 0.
  4. Drude damping: I(gamma) closed form and the fractional shift of K.
  5. The tree's numbers: K_SF/A_EM, a_c/lambdabar_p, gold/aluminium a_c; and a_c under the
     measured film plasma energies of Svetovoy et al. 0801.1384 Table II.
  6. The curvature step the tree RECONSTRUCTS: p_t = K/eps^3 with the spherical conservation
     law gives p_r = K/(a eps^2); cross-checked against the SAME step in the non-dispersive
     case, where Li 2411.07911 eq. (38a,b) computed both components explicitly.
Stdlib + sympy + scipy.  Exits 1 on any failed check.
"""
import math, sys
import sympy as sp
from scipy import integrate

fails = []
def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("   " + detail if detail else ""))
    if not ok:
        fails.append(name)

# ------------------------------------------------------------------ 1. general-eps asymptotic
y, w, u, z, g = sp.symbols("y omega u z gamma", positive=True)
# near-wall: r' -> (eps-1)/(eps+1) with eps = eps(i u t), t = cos theta; sin^3 -> 1 at grazing;
# INT_0^1 dt (1-t^2) r' -> (1/u) INT_0^inf dy (eps(iy)-1)/(eps(iy)+1)
eps_pl = 1 + w**2 / y**2
I_pl = sp.integrate(sp.simplify((eps_pl - 1) / (eps_pl + 1)), (y, 0, sp.oo))
check("1a plasma I = pi omega_p/(2 sqrt2)", sp.simplify(I_pl - sp.pi * w / (2 * sp.sqrt(2))) == 0,
      str(sp.simplify(I_pl)))
radial = sp.integrate(u**3 * sp.exp(-2 * u * z) / u, (u, 0, sp.oo)) / (4 * sp.pi**2)
check("1b (1/4pi^2) INT u^2 e^{-2uz} du = 1/(16 pi^2 z^3)",
      sp.simplify(radial - 1 / (16 * sp.pi**2 * z**3)) == 0)
U_coef = sp.simplify(I_pl * radial * z**3)
check("1c U z^3 -> sqrt2 omega_p/(64 pi)   [0204125 eq. (37)]",
      sp.simplify(U_coef - sp.sqrt(2) * w / (64 * sp.pi)) == 0, str(U_coef))
Txx_coef = U_coef / 2
check("1d T_xx z^3 -> sqrt2 omega_p/(128 pi)  [0504143 eq. (15)]",
      sp.simplify(Txx_coef - sp.sqrt(2) * w / (128 * sp.pi)) == 0, str(Txx_coef))

# ------------------------------------------------------------------ 2. T_xx = U/2 (a -> inf)
r, rp, k, kap = sp.symbols("r rp k kappa", real=True)
# a->inf, near z=0: e^{-kappa a} cosh[kappa(2z-a)] -> e^{-2 kappa z}/2, denominators -> 1,
# the r^2/(r^2-e^{2 kappa a}) terms -> 0.
posU = (1 / (2 * sp.pi**2)) * (k / kap) * k**2 * (r + rp) * sp.Rational(1, 2)
posT = -(1 / (4 * sp.pi**2)) * (k**3 / kap) * (-(r + rp)) * sp.Rational(1, 2)
check("2  eq.(14) integrand = eq.(8) integrand / 2 in the one-wall limit",
      sp.simplify(posT - posU / 2) == 0)

# ------------------------------------------------------------------ 3. exact numeric integral
def inner(uu):
    """INT_0^1 dt (1-t^2)(r + r'), omega_p = 1 (0204125 eqs. 34-35)."""
    s = math.sqrt(uu * uu + 1.0)
    rr = (uu - s) / (uu + s)
    def f(t):
        a = uu * uu * t * t + 1.0
        b = uu * t * t * s
        return (1 - t * t) * (rr + (a - b) / (a + b))
    pts = sorted({min(1.0, x / uu) for x in (0.3, 1.0, 3.0, 10.0)})
    val, _ = integrate.quad(f, 0.0, 1.0, points=pts, limit=400, epsabs=0, epsrel=1e-11)
    return val

def z3U(zz):
    f = lambda v: v**3 * math.exp(-2 * v) * inner(v / zz)
    val, _ = integrate.quad(f, 0.0, 60.0, limit=400, epsabs=0, epsrel=1e-10)
    return val / (4 * math.pi**2 * zz)

target = math.sqrt(2) / (64 * math.pi)
print("   target sqrt2/(64 pi) = %.10f" % target)
rows = []
for zz in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5):
    v = z3U(zz)
    rows.append((zz, v))
    print("   omega_p z = %-7g  z^3 U/omega_p = %.10f   ratio to target %.8f" % (zz, v, v / target))
# the correction must vanish as z -> 0 (next term ~ z^-2, i.e. relative O(omega_p z))
rel = [abs(v / target - 1) for _, v in rows]
check("3a exact z^3 U converges to sqrt2/(64 pi) (rel. dev < 1e-3 at omega_p z = 1e-5)",
      rel[-1] < 1e-3, "rel dev %.3e" % rel[-1])
check("3b the deviation shrinks monotonically as omega_p z -> 0",
      all(rel[i + 1] < rel[i] for i in range(len(rel) - 1)))
# subleading: 0204125 eq. (38b) <B^2> ~ -5 omega_p^2/(96 pi z^2) -> U gets a z^-2 term; slope check
slope = (rows[-2][1] - rows[-1][1]) / (rows[-2][0] - rows[-1][0])
print("   empirical d(z^3 U)/d(omega_p z) near 0 = %.6f  (the O(z^-2) subleading term)" % slope)

# ------------------------------------------------------------------ 4. Drude damping
def I_drude(wp, gm):
    """I = INT_0^inf dzeta (eps-1)/(eps+1), eps(i zeta) = 1 + wp^2/(zeta(zeta+gm)), by quadrature."""
    f = lambda yy: wp * wp / (2 * yy * (yy + gm) + wp * wp)
    v1, _ = integrate.quad(f, 0.0, 50 * wp, limit=400, epsabs=0, epsrel=1e-12)
    # tail: f ~ wp^2/(2 y^2) beyond 50 wp; exact tail of the gm=0 form is adequate to 1e-9
    return v1 + wp * wp / (2 * 50 * wp)
check("4a I_drude(gamma=0) reproduces pi wp/(2 sqrt2)",
      abs(I_drude(9.0, 0.0) / (math.pi * 9.0 / (2 * math.sqrt(2))) - 1) < 1e-6)
for label, wp, gm in (("Lambrecht-Reynaud gold 9.0 eV / 35 meV", 9.0, 0.035),
                      ("Svetovoy sample 5 8.38 eV / 37.1 meV", 8.38, 0.0371),
                      ("Svetovoy sample 3 7.84 eV / 49.0 meV", 7.84, 0.0490)):
    shift = I_drude(wp, gm) / (math.pi * wp / (2 * math.sqrt(2))) - 1
    print("   Drude damping, %-40s  K shift = %+.4f %%   (approx -sqrt2 g/(pi wp) = %+.4f %%)"
          % (label, 100 * shift, -100 * math.sqrt(2) * gm / (math.pi * wp)))
check("4  Drude damping moves K by < 0.5 % for gold film parameters",
      abs(I_drude(7.84, 0.049) / (math.pi * 7.84 / (2 * math.sqrt(2))) - 1) < 5e-3)

# ------------------------------------------------------------------ 5. the tree's numbers
K_SF = math.sqrt(2) / (128 * math.pi)
A_EM = 1 / (60 * math.pi**2)
coef = K_SF / A_EM
check("5a crossover coefficient K_SF/A_EM = 60 sqrt2 pi/128 = 2.0826013773",
      abs(coef - 60 * math.sqrt(2) * math.pi / 128) < 1e-14 and abs(coef - 2.0826013773) < 1e-9,
      "%.10f" % coef)
check("5b a_c / lambdabar_p = 0.4801687020", abs(1 / coef - 0.4801687020) < 1e-9, "%.10f" % (1 / coef))
HBARC_eVnm = 197.3269804  # CODATA 2018 hbar c in eV nm
for label, E in (("gold 9.0 eV (tree / Lambrecht-Reynaud)", 9.0), ("aluminium 15.3 eV (tree)", 15.3),
                 ("gold film 8.38 eV (Svetovoy s5)", 8.38), ("gold film 6.82 eV (Svetovoy s1)", 6.82),
                 ("aluminium 14.8 eV (Sopova-Ford 2002)", 14.8)):
    lb = HBARC_eVnm / E
    print("   %-40s lambdabar_p = %8.4f nm   a_c = %8.4f nm" % (label, lb, lb / coef))
check("5c tree gold a_c = 10.5278 nm", abs(HBARC_eVnm / 9.0 / coef - 10.5278) < 1e-3)
check("5d tree aluminium a_c = 6.19283 nm", abs(HBARC_eVnm / 15.3 / coef - 6.19283) < 1e-4)
# the component: had K been read off U instead of T_xx, the coefficient doubles
print("   if U's coefficient sqrt2/(64 pi) were used: a_c/lambdabar_p = %.10f (factor 2)"
      % (A_EM / (2 * K_SF)))

# ------------------------------------------------------------------ 6. the curvature step
e, a, K, C = sp.symbols("epsilon a K C", positive=True)
pr = sp.Function("p_r")
# inside a sphere, r = a - eps; conservation p_r' + 2(p_r - p_t)/r = 0, leading order in eps/a:
# d p_r/d eps = -2 p_t / a  (p_t dominant over p_r near the wall)
sol = sp.integrate(-2 * (K / e**3) / a, e)
check("6a p_t = K/eps^3  =>  p_r = K/(a eps^2)  (same sign; the tree's K a/A form)",
      sp.simplify(sol - K / (a * e**2)) == 0, str(sol))
sol4 = sp.integrate(-2 * (C / e**4) / a, e)
check("6b p_t = C/eps^4  =>  p_r = 2C/(3 a eps^3)", sp.simplify(sol4 - 2 * C / (3 * a * e**3)) == 0)
# Li 2411.07911 eq. (38a,b), case I TE, leading terms: T_rr = -1/(48 pi^2 a z^3), T_tt = -1/(32 pi^2 z^4)
Li_ratio = sp.Rational(1, 48) / sp.Rational(1, 32)
check("6c Li 2024's explicit sphere: |T_rr| a z^3 / (|T_tt| z^4) = 2/3, same sign -- the conservation "
      "step reproduces an explicit spherical computation (non-dispersive case only)", Li_ratio == sp.Rational(2, 3))

print()
print("FAILED: %s" % fails if fails else "ALL CHECKS PASS")
sys.exit(1 if fails else 0)
