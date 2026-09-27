#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for arXiv:2309.10848 (Fliss, Freivogel, Kontou, Pardo Santos 2023),
as the warp board uses it (candidates.py:180-243, 407-441; overturn.py:291-307; specthm.py:2154-2164).

Checks, each printed PASS/FAIL or as a MEASURED number (no verdict implied):
  A  the tree's arithmetic: shortfall = rho_needed / (hbar c/(l_UV^2 R^2)) == (l_UV/l_P)^2/Lambda
     exactly (sympy), scale-free in R, and the selftest numbers 0.100175, 10.0175, 3.159514,
     1.0018e5, 3.83e32 (numeric, CODATA 2022 via scipy.constants when available).
  B  SI conversion of FFKP eq. (91) at n = 4: N/(l_UV^2 delta^2) in hbar=c=1 is hbar c/(l^2 d^2) J/m^3.
  C  FFKP eq. (94) and the assembly of Q_0, Q_2 in eq. (96) from eq. (93) + (97) (sympy).
  D  FFKP eqs. (80),(93) as PRINTED carry  int d(x-) d^2_-(f^2)  without an absolute value: that
     integral is identically 0 for any decaying f (sympy) -- so the printed xi-term is a
     DISCREPANCY (the bound needs int |d^2_-(f^2)|, and the state class needs |<:phi^2:>| <= phi^2_max,
     which Sec. V states but (79) does not).  Recorded, not a refutation.
  E  N_4 is NOT schematic for the massless SNEC form (93): for unit-L2 Gaussian smearing of width
     delta, N_4 = p_4/2 + K |xi| phi~^2_max with p_4 = 2/pi^2 and K = 4 sqrt(2/pi) e^{-1/2} (exact),
     and the crossover sqrt(N_4 Lambda) l_P for several |xi| phi~^2_max.
  F  the paper's OWN Sec. V field bound, phi^2_max = eps/(8 pi G |xi|) with eps << 1 (EFT regime),
     makes the xi-term l_UV- and xi-independent: eps K c^4/(8 pi G delta^2).  Against
     rho_needed = c^4/(G Lambda R^2) it closes only for eps >= 8 pi/(K Lambda).
  G  T_-- is not rho: with l_- = d_- = (d_t - d_x)/2 (FFKP conventions, eq. 5), T_-- =
     (T_tt - 2 T_tx + T_xx)/4; a stress tensor with rho -> -infinity and T_-- = 0 exists (sympy).
"""
import math, sys
import sympy as sp

ok = True
def chk(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

# ---------------------------------------------------------------- constants
try:
    import scipy.constants as sc
    HBAR, C, G = sc.hbar, sc.c, sc.G
    lP_codata = sc.physical_constants["Planck length"][0]
    src = "scipy %s (CODATA 2022)" % __import__("scipy").__version__
except Exception:
    HBAR, C, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
    lP_codata = None
    src = "hard-coded CODATA 2018 = 2022 values"
TREE = dict(HBAR=1.054571817e-34, C=2.99792458e8, G=6.67430e-11)
LAMBDA = 9.982529174194637          # overturn.py:397, internal model coefficient (not external data)
print("constants from", src, "; tree uses", TREE)
chk("CODATA 2022 hbar, c, G equal the tree's values (G = 6.67430e-11 unchanged 2018 -> 2022)",
    abs(HBAR - TREE["HBAR"]) < 1e-43 and C == TREE["C"] and abs(G - TREE["G"]) < 1e-18)
lP = math.sqrt(HBAR * G / C**3)
print("l_P = %.12e m  (CODATA listed: %s)" % (lP, lP_codata))

# ---------------------------------------------------------------- A
hb, c, g, lam, l, R, lp = sp.symbols("hbar c G Lambda l_UV R l_P", positive=True)
rho_needed = c**4 / (g * lam * R**2)
allowed = hb * c / (l**2 * R**2)
short = sp.simplify(rho_needed / allowed)
closed = (l / sp.sqrt(hb * g / c**3))**2 / lam
chk("A1 shortfall == (l_UV/l_P)^2/Lambda identically, R cancels (sympy)",
    sp.simplify(short - closed) == 0 and sp.diff(short, R) == 0)
chk("A2 hbar c / l_P^2 == c^4/G identically (why no measured constant enters the crossover in l_P units)",
    sp.simplify(hb * c / (hb * g / c**3) - c**4 / g) == 0)
def shortfall(l_m, R_m=1.0):
    return (C**4 / (G * LAMBDA * R_m**2)) / (HBAR * C / (l_m**2 * R_m**2))
vals = [shortfall(10 * lP, r) for r in (1e-9, 1.0, 1e6)]
chk("A3 scale-free: shortfall at 10 l_P identical at R = 1e-9, 1, 1e6 m", max(vals) - min(vals) <= 1e-12 * max(vals))
for lab, lm, want, tol in (("l_P", lP, 0.100175, 1e-5), ("10 l_P", 10 * lP, 10.0175, 1e-4),
                           ("1e3 l_P", 1e3 * lP, 1.0018e5, 1e-4), ("1e-18 m", 1e-18, 3.83e32, 1e-2)):
    v = shortfall(lm)
    chk("A4 shortfall at %-8s = %.6g (tree %g)" % (lab, v, want), abs(v - want) <= tol * want)
chk("A5 crossover sqrt(Lambda) = %.6f l_P (tree 3.159514)" % math.sqrt(LAMBDA), abs(math.sqrt(LAMBDA) - 3.159514) < 1e-6)

# ---------------------------------------------------------------- B  (units)
from sympy.physics import units as u
expr = u.hbar * u.speed_of_light / (u.meter**2 * u.meter**2)
si = u.convert_to(expr, [u.joule, u.meter])
chk("B1 hbar c / (length^2 length^2) has units J/m^3 (energy density): %s" % si,
    sp.simplify(si / (u.joule / u.meter**3)).free_symbols == set())

# ---------------------------------------------------------------- C  (eqs 94, 96)
x = sp.symbols("x", real=True)
L = sp.symbols("ell", positive=True)
# (94): int f'^2 = -int f f'' <= int |f||f''| <= eps ||f||^2 + ||f''||^2/(4 eps), eps = 1/(2 ell^2)
eps = 1 / (2 * L**2)
chk("C1 eq.(94) coefficients: eps = 1/(2 l^2) gives 1/(2 l^2) ||f||^2 + (l^2/2)||f''||^2",
    sp.simplify(eps - 1 / (2 * L**2)) == 0 and sp.simplify(1 / (4 * eps) - L**2 / 2) == 0)
# numeric test of (94) on three test functions
for name, f in (("gaussian", sp.exp(-x**2)), ("x e^-x^2", x * sp.exp(-x**2)), ("sech", 1 / sp.cosh(x))):
    lhs = sp.Integral(sp.diff(f, x)**2, (x, -sp.oo, sp.oo)).evalf(30)
    n0 = sp.Integral(f**2, (x, -sp.oo, sp.oo)).evalf(30)
    n2 = sp.Integral(sp.diff(f, x, 2)**2, (x, -sp.oo, sp.oo)).evalf(30)
    worst = min(n0 / (2 * lv**2) + lv**2 / 2 * n2 - lhs for lv in (0.1, 0.5, 1, 2, 10))
    chk("C2 eq.(94) holds for %s at l in {0.1..10} (min slack %.4g)" % (name, float(worst)), worst >= -1e-20)
# (96): p/l^(n-2) int f'^2 + |xi| phi^2 (2 int f'^2 + 2 int |f f''|), phi^2 = phit/l^(n-2)
n, p, a, N0, N2 = sp.symbols("n p_n a N0 N2", positive=True)   # a = |xi| phi~^2_max
fp2 = N0 / (2 * L**2) + L**2 / 2 * N2        # bound on int f'^2  (94)
ffpp = eps * N0 + N2 / (4 * eps)             # bound on int |f||f''|  (97)
tot = sp.expand((p * fp2 + a * (2 * fp2 + 2 * ffpp)) / L**(n - 2))
Q0 = (p / 2 + 2 * a) / L**n
Q2 = (p / 2 + 2 * a) / L**(n - 4)
chk("C3 eq.(96) Q_0 = (p_n/2 + 2|xi|phi~^2)/l^n and Q_2 = (...)/l^(n-4) reassembled exactly (sympy)",
    sp.simplify(tot.coeff(N0) - Q0) == 0 and sp.simplify(tot.coeff(N2) - Q2) == 0)
p_n = 4 / (n - 2) * sp.pi**(-n / 2) / sp.gamma((n - 2) / 2)
p4 = sp.simplify(p_n.subs(n, 4))
chk("C4 p_4 = 2/pi^2 = %.6f" % float(p4), sp.simplify(p4 - 2 / sp.pi**2) == 0)

# ---------------------------------------------------------------- D  (the total derivative)
d = sp.symbols("delta", positive=True)
fg = (sp.pi * d**2)**sp.Rational(-1, 4) * sp.exp(-x**2 / (2 * d**2))     # unit L2 Gaussian
chk("D1 unit normalisation int f^2 = 1", sp.simplify(sp.integrate(fg**2, (x, -sp.oo, sp.oo)) - 1) == 0)
tdv = sp.integrate(sp.diff(fg**2, x, 2), (x, -sp.oo, sp.oo))
chk("D2 PRINTED xi-term of (80)/(93): int d^2_-(f^2) dx- = %s identically (needs |.|: DISCREPANCY)" % tdv, tdv == 0)

# ---------------------------------------------------------------- E  (N_4 computed, not schematic)
fp2g = sp.simplify(sp.integrate(sp.diff(fg, x)**2, (x, -sp.oo, sp.oo)))
chk("E1 int f'^2 = 1/(2 delta^2) for the unit Gaussian", sp.simplify(fp2g - 1 / (2 * d**2)) == 0)
uu = sp.symbols("u", real=True)
h = sp.exp(-uu**2) * (4 * uu**2 - 2) / sp.sqrt(sp.pi)       # delta^2 (f^2)'' in u = x/delta
a0 = 1 / sp.sqrt(2)
K = sp.simplify(2 * sp.integrate(-h, (uu, -a0, a0)))       # positive part = negative part
import mpmath as mp
mp.mp.dps = 30
hf = sp.lambdify(uu, sp.Abs(h), "mpmath")
Knum = mp.quad(hf, [-mp.inf, -1/mp.sqrt(2), 0, 1/mp.sqrt(2), mp.inf])   # split at the kinks
chk("E2 K = delta^2 int |(f^2)''| = 4 sqrt(2/pi) e^-1/2 = %.10f (split quadrature %.10f)" % (float(K), float(Knum)),
    abs(float(K) - float(Knum)) < 1e-12 and sp.simplify(K - 4 * sp.sqrt(2 / sp.pi) * sp.exp(-sp.Rational(1, 2))) == 0)
Kf = float(K)
N4 = lambda a_: float(p4) / 2 + Kf * a_
print("   N_4(Gaussian, massless, eq. 93) = 1/pi^2 + %.6f |xi| phi~^2_max" % Kf)
print("   %-26s %10s %14s %20s" % ("|xi| phi~^2_max", "N_4", "crossover/l_P", "shortfall @10 l_P"))
for lab, a_ in (("0 (minimal term only)", 0.0), ("1/6 (xi=1/6, phi~^2=1)", 1 / 6),
                ("0.4642 (N_4 = 1, tree)", (1 - float(p4) / 2) / Kf), ("1", 1.0)):
    NN = N4(a_)
    print("   %-26s %10.5f %14.6f %20.6f" % (lab, NN, math.sqrt(NN * LAMBDA), shortfall(10 * lP) / NN))
chk("E3 tree's N=1 corresponds to |xi| phi~^2_max = %.4f under Gaussian smearing" % ((1 - float(p4) / 2) / Kf),
    abs(N4((1 - float(p4) / 2) / Kf) - 1) < 1e-12)
chk("E4 minimal-coupling term alone closes at sqrt(Lambda)/pi l_P = %.6f l_P" % (math.sqrt(LAMBDA) / math.pi),
    abs(math.sqrt(0.5 * float(p4) * LAMBDA) - math.sqrt(LAMBDA) / math.pi) < 1e-12)

# ---------------------------------------------------------------- F  (Sec. V field bound)
e_, xi_ = sp.symbols("epsilon xi", positive=True)
phi2max = e_ / (8 * sp.pi * g * xi_)            # hbar = c = 1 form of 8 pi G |xi| phi^2_max = eps
xiterm_nat = xi_ * phi2max * K / d**2           # |xi| phi^2_max * delta^-2 * int|(f^2)''| delta^2
chk("F1 xi-term = eps K /(8 pi G delta^2): independent of xi and of l_UV (sympy)",
    sp.simplify(xiterm_nat - e_ * K / (8 * sp.pi * g * d**2)) == 0 and sp.diff(xiterm_nat, xi_) == 0)
eps_close = 8 * math.pi / (Kf * LAMBDA)
print("   xi-term alone meets rho_needed = c^4/(G Lambda R^2) at delta = R iff eps >= 8 pi/(K Lambda) = %.6f" % eps_close)
chk("F2 closure by the xi-term alone needs eps = 8 pi G|xi|phi^2_max >= %.4f > 1: past (8 pi G xi)^-1,"
    " the value at which FFKP Sec. V.B put semiclassical breakdown for xi > 0" % eps_close, eps_close > 1)
for ev in (0.01, 0.1, 0.5):
    # both terms: 1/pi^2 hbar c/(l^2 d^2) + eps K c^4/(8 pi G d^2) >= c^4/(G Lambda d^2)
    need = 1 / LAMBDA - ev * Kf / (8 * math.pi)
    lmax = math.sqrt(1 / (math.pi**2 * need)) if need > 0 else float("inf")
    print("   eps = %-4s : closes only for l_UV <= %.6f l_P" % (ev, lmax))

# ---------------------------------------------------------------- G  (T_-- is not rho)
Ttt, Ttx, Txx, A = sp.symbols("T_tt T_tx T_xx A", real=True)
lm = sp.Matrix([sp.Rational(1, 2), -sp.Rational(1, 2)])     # d_- = (d_t - d_x)/2
T = sp.Matrix([[Ttt, Ttx], [Ttx, Txx]])
Tmm = sp.expand((lm.T * T * lm)[0])
chk("G1 T_-- = (T_tt - 2 T_tx + T_xx)/4 (index position immaterial for the tt,xx diagonal in Minkowski)",
    sp.simplify(Tmm - (Ttt - 2 * Ttx + Txx) / 4) == 0)
chk("G2 rho = -A, p_x = +A, T_tx = 0 gives T_-- = 0 for every A: a null bound does not bound rho",
    sp.simplify(Tmm.subs({Ttt: -A, Txx: A, Ttx: 0})) == 0)
chk("G3 static dust-like source (T_tt = rho, others 0): T_-- = rho/4 -- a factor 4 the tree's |rho| ~ |T_--| drops",
    sp.simplify(Tmm.subs({Ttx: 0, Txx: 0}) - Ttt / 4) == 0)

print("\nREDERIVE", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
