#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the screened (Yukawa) Green's function as
excite.py D16 uses it.  Independent of the owner: nothing is imported from
research/warp-drive.  sympy for the closed forms, stdlib numerics for controls.

Rows (each prints PASS/FAIL; exit 1 on any FAIL):
 Y1  (-lap + m^2) G = 0 for r > 0, G = e^{-mr}/(4 pi r)
 Y2  delta normalisation: flux -4 pi r^2 G'(r) -> 1 as r -> 0
 Y3  INT G d^3r = INT_0^inf r e^{-mr} dr = 1/m^2  (m > 0)
 Y3c CONTROL m -> 0: INT diverges (hypothesis m^2 > 0 is load-bearing)
 Y3d CONTROL m = i k (tachyonic / m^2 < 0): INT_0^R r cos(kr) dr has no limit
 Y4  Fourier transform  INT G e^{-i xi.x} d^3x = 1/(m^2 + xi^2)
 Y4b 3-D convolution with J = cos(z/L): response = cos/(m^2 + 1/L^2)
 Y5  cos response ratio 1/(1+s^2), error s^2/(1+s^2), leading term s^2 (s = lambda/L)
 Y6  exact remainder identity G*J = J/m^2 + G*(lap J)/m^2  (checked on a Gaussian J)
     => |delta phi + J/m^2| <= ||lap J||_inf / m^4 (absolute form of the O((lambda/L)^2))
 Y7  COUNTER-CONTROL: multiplicative form delta phi = -J/m^2 [1 + O(s^2)] fails
     pointwise at zeros of J (J = a + cos(z/L)): relative error unbounded there
 Y8  n-dimensional check (Ishii-Tanaka Lemma 3.1): ||k||_1 = 1 for n = 1..6, so
     INT G = 1/m^2 holds in every dimension; the e^{-mr}/(4 pi r) FORM is n = 3 only
 Y9  Simpson reproduction of the owner's numeric fixture (INT G m^2 = 1 to 1e-9, m = 1,2,3)
 Y10 lambda_h = hbar c / m_h at 125.13 (PDG-2026 capture), 125.20 +- 0.11 (PDG 2024)
"""
import math
import sys

import sympy as sp

FAILS = []


def row(name, ok, detail=""):
    print("%-4s %-70s %s" % ("PASS" if ok else "FAIL", name, detail))
    if not ok:
        FAILS.append(name)


r, m, k, L, x, z, a = sp.symbols("r m k L x z a", positive=True)
G = sp.exp(-m * r) / (4 * sp.pi * r)

# Y1
res = sp.simplify(-sp.diff(r * G, r, 2) / r + m ** 2 * G)
row("Y1  (-lap + m^2) G = 0 for r > 0", res == 0, str(res))

# Y2
flux = sp.limit(-4 * sp.pi * r ** 2 * sp.diff(G, r), r, 0)
row("Y2  flux -4 pi r^2 G' -> 1 at r -> 0 (unit point source)", flux == 1, str(flux))

# Y3
I3 = sp.integrate(4 * sp.pi * r ** 2 * G, (r, 0, sp.oo))
row("Y3  INT G d^3r = 1/m^2", sp.simplify(I3 - 1 / m ** 2) == 0, str(I3))
row("Y3b INT 4 pi r^2 G = INT r e^{-mr} dr (owner's middle form)",
    sp.simplify(4 * sp.pi * r ** 2 * G - r * sp.exp(-m * r)) == 0)

# Y3c control m = 0
R = sp.symbols("R", positive=True)
I0 = sp.integrate(r, (r, 0, R))
row("Y3c CONTROL m = 0: INT_0^R r dr = R^2/2 -> oo", sp.limit(I0, R, sp.oo) == sp.oo, str(I0))

# Y3d control m^2 < 0 (G = cos(kr)/(4 pi r) or e^{ikr}/(4 pi r)); partial integral oscillates unboundedly
Ik = sp.integrate(r * sp.cos(k * r), (r, 0, R))
vals = [float(Ik.subs({k: 1, R: Rv})) for Rv in (100 * math.pi, 100 * math.pi + math.pi / 2,
                                                 100 * math.pi + math.pi)]
row("Y3d CONTROL m^2 = -k^2 < 0: INT_0^R r cos(kr) dr has no limit",
    max(vals) - min(vals) > 100, "partial sums %s" % ["%.1f" % v for v in vals])

# Y4 Fourier transform (radial): INT 4 pi r^2 G sin(xi r)/(xi r) dr
xi = sp.symbols("xi", positive=True)
FT = sp.integrate(4 * sp.pi * r ** 2 * G * sp.sin(xi * r) / (xi * r), (r, 0, sp.oo), conds="none")
row("Y4  FT[G](xi) = 1/(m^2 + xi^2)", sp.simplify(FT - 1 / (m ** 2 + xi ** 2)) == 0, str(sp.simplify(FT)))

# Y4b convolution with cos(z/L) = FT at xi = 1/L times cos(z/L)
resp = FT.subs(xi, 1 / L)
row("Y4b G * cos(z/L) = cos(z/L)/(m^2 + 1/L^2)",
    sp.simplify(resp - 1 / (m ** 2 + 1 / L ** 2)) == 0)

# Y5 ratio and error, s = lambda/L = 1/(m L)
s = sp.symbols("s", positive=True)
ratio = sp.simplify((resp * m ** 2).subs(L, 1 / (m * s)))
row("Y5  exact/algebraic = 1/(1+s^2), s = lambda/L", sp.simplify(ratio - 1 / (1 + s ** 2)) == 0, str(ratio))
err = sp.simplify(1 - ratio)
row("Y5b fractional error = s^2/(1+s^2)", sp.simplify(err - s ** 2 / (1 + s ** 2)) == 0, str(err))
row("Y5c leading term s^2 = (lambda/L)^2", sp.series(err, s, 0, 4).removeO() == s ** 2)
# the owner's code variable is sigma = s^2 and returns sigma/(1+sigma): the same number
sig = sp.symbols("sigma", positive=True)
row("Y5d owner form sigma/(1+sigma) with sigma = s^2 equals s^2/(1+s^2)",
    sp.simplify((sig / (1 + sig)).subs(sig, s ** 2) - s ** 2 / (1 + s ** 2)) == 0)
# the canonical-entry paraphrase 's^2/(1+s^2), s = (lambda/L)^2' would be (lambda/L)^4/(1+(lambda/L)^4)
row("Y5e DISCREPANCY-CHECK canonical paraphrase with s=(lambda/L)^2 differs from the exact error",
    sp.simplify((sig ** 2 / (1 + sig ** 2)).subs(sig, s ** 2) - s ** 2 / (1 + s ** 2)) != 0,
    "(paraphrase in canonical.json, not in excite.py code)")

# Y6 exact remainder on a Gaussian source J = exp(-r^2/(2 w^2)) (radial), via Fourier space
w = sp.symbols("w", positive=True)
# FT of Gaussian in 3D: (2 pi w^2)^{3/2} exp(-w^2 xi^2/2); FT of lap J = -xi^2 FT[J]
FJ = (2 * sp.pi * w ** 2) ** sp.Rational(3, 2) * sp.exp(-w ** 2 * xi ** 2 / 2)
lhs = FJ / (m ** 2 + xi ** 2)                             # FT[G*J]
rhs = FJ / m ** 2 + (-xi ** 2 * FJ) / (m ** 2 + xi ** 2) / m ** 2   # FT[J/m^2 + G*lapJ/m^2]
row("Y6  G*J = J/m^2 + G*(lap J)/m^2 (exact, Fourier side, Gaussian J)",
    sp.simplify(lhs - rhs) == 0)
# numeric sup-norm bound check at centre for m=1, w=5 (L ~ w): |G*J - J/m^2| <= ||lapJ||/m^4
mm, ww = 1.0, 5.0
f = lambda q: (2 * math.pi * ww ** 2) ** 1.5 * math.exp(-ww ** 2 * q ** 2 / 2)
# inverse FT at r=0: (1/(2 pi^2)) INT q^2 F(q) dq
def inv0(F, n=20000, qmax=4.0):
    h = qmax / n
    return sum((4 if i % 2 else 2) * (i * h) ** 2 * F(i * h) for i in range(1, n)) * h / 3 / (2 * math.pi ** 2)
GJ0 = inv0(lambda q: f(q) / (mm ** 2 + q ** 2))
J0 = 1.0
lapJ_sup = 3 / ww ** 2        # |lap J| max is at r=0: 3/w^2 for this Gaussian
row("Y6b |G*J - J/m^2| <= ||lap J||_inf/m^4 at r=0 (m=1, w=5)",
    abs(GJ0 - J0 / mm ** 2) <= lapJ_sup / mm ** 4,
    "|diff| = %.6e, bound = %.6e" % (abs(GJ0 - J0), lapJ_sup))

# Y7 counter-control: J = a + cos(z/L); at a zero of J the algebraic answer is 0, exact is not
exact = -(a / m ** 2 + sp.cos(z / L) / (m ** 2 + 1 / L ** 2))
alg = -(a + sp.cos(z / L)) / m ** 2
at_zero = sp.simplify((exact - alg).subs(sp.cos(z / L), -a))
row("Y7  at J = 0 (cos = -a, 0<a<1) exact - algebraic = a(1/m^2 - 1/(m^2+1/L^2)) != 0",
    sp.simplify(at_zero) != 0, "abs err there = %s; relative error unbounded (alg = 0)" % sp.simplify(at_zero))
# ... but the absolute bound of Y6 holds: |err| <= ||lapJ||/m^4 = (1/L^2)/m^4
row("Y7b absolute form survives: a(1/m^2-1/(m^2+L^-2)) <= L^-2/m^4 for 0<a<=1",
    sp.simplify(1 / (L ** 2 * m ** 4) - sp.Abs(at_zero.subs(a, 1))) == sp.simplify(1 / (L ** 2 * m ** 4) - 1 / (m ** 2 * (L ** 2 * m ** 2 + 1)))
    and all(float((1 / (L ** 2 * m ** 4) - sp.Abs(at_zero.subs(a, 1))).subs({m: mv, L: Lv})) > 0
            for mv in (0.5, 1, 3) for Lv in (0.1, 1, 10, 1e3)))

# Y8 n-dimensional normalisation of Ishii-Tanaka G(|x|) = (2pi)^{-n/2} |x|^{1-n/2} K_{n/2-1}(|x|)
ok8 = True
det = []
for n in range(1, 7):
    nu = sp.Rational(n, 2) - 1
    Gn = (2 * sp.pi) ** (-sp.Rational(n, 2)) * r ** (-nu) * sp.besselk(nu, r)
    area = 2 * sp.pi ** sp.Rational(n, 2) / sp.gamma(sp.Rational(n, 2))
    # numeric integral (sympy symbolic can be slow for some n)
    val = sp.Integral(area * r ** (n - 1) * Gn, (r, 0, sp.oo)).evalf(20)
    det.append("n=%d:%.12f" % (n, float(val)))
    ok8 = ok8 and abs(float(val) - 1) < 1e-10
    if n == 3:
        form = sp.simplify(sp.expand_func(Gn) - sp.exp(-r) / (4 * sp.pi * r))
        row("Y8a n=3 Ishii-Tanaka kernel = e^{-r}/(4 pi r)", form == 0, str(form))
row("Y8  ||k||_1 = 1 in n = 1..6 (so INT G = 1/m^2 is dimension-free)", ok8, " ".join(det))

# Y9 Simpson reproduction of owner fixture
def green_integral(mv, rmax_in_ranges=60.0, n=200001):
    rmax = rmax_in_ranges / mv
    h = rmax / (n - 1)
    s_ = rmax * math.exp(-mv * rmax)
    for i in range(1, n - 1):
        rr = i * h
        s_ += (4.0 if i % 2 else 2.0) * rr * math.exp(-mv * rr)
    return s_ * h / 3.0
d9 = [abs(green_integral(mv) * mv * mv - 1) for mv in (1.0, 2.0, 3.0)]
row("Y9  Simpson INT G d^3r * m^2 = 1 to 1e-9 at m = 1,2,3", max(d9) < 1e-9,
    "max |dev| = %.2e" % max(d9))

# Y10 lambda_h
HBARC_MEV_FM = 197.3269804           # CODATA 2018/2022 exact-SI derived
for label, mh in (("PDG-2026 capture 125.13", 125.13), ("PDG-2024 125.20", 125.20),
                  ("PDG-2024 -1 sigma 125.09", 125.09), ("PDG-2024 +1 sigma 125.31", 125.31)):
    lam_m = HBARC_MEV_FM / (mh * 1000.0) * 1e-15
    print("     lambda_h at m_h = %-28s = %.6e m" % (label, lam_m))
lam13 = HBARC_MEV_FM / 125130.0
lam20 = HBARC_MEV_FM / 125200.0
row("Y10 lambda_h moves by %.3f %% between 125.13 and 125.20 (conclusion is m-free)"
    % (100 * (lam13 / lam20 - 1)), abs(lam13 / lam20 - 1) < 1e-3)

print("\n%d FAIL" % len(FAILS))
sys.exit(1 if FAILS else 0)
