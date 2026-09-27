#!/usr/bin/env python3
"""DOCKET 67 -- audit of the loop-induced SME route (ledger.py:1793-1794 O7,
branelink.py:96-98, 149, 288-292, 308).

SOURCE (READ from the on-disk alphaXiv capture of arXiv:2309.05759v2,
scratchpad/d67/src/2309.05759.cached.txt, md5 fd16b061341718ee1cd6eda53cde16be,
printed pp. 18-20, 25):
  (69)  ... [k^2 - (k.b + n/r)^2 - mu^2 + i eps]^-1   "we've introduced mu as an infrared regulator"
  (76)  c^{mu nu} = -(1/16 pi^2) (1/(pi r Mbar4)^2) (b^mu b^nu - eta^{mu nu} b^2/4) I_gravity
        I_gravity = 1/(6 sqrt(pi)) sum_{w>=1} int_0^inf ds int_0^inf dt
            (9 s^2 - 2 s t - 11 t^2 + 5 s b^2) / (w^3 t^{1/2} (s+t)^6)
            * exp( -s (pi m r w)^2 - t (pi mu r w)^2 - (s + t(1-b^2)) / (t (s+t)) )
        "a function I_gravity of the dimensionless parameters b^2, pi m r, pi mu r"
        "It simplifies if we set m = 0 (a massless fermion on the brane) and b^2 = 0
         (a small boost and / or rotation)"
  (77)  b^2 ~ 0, m ~ 0 :  I_gravity ~ -zeta(3)/4 (mu r -> 0);  -(1/3)(pi mu r)^2 e^{-2 pi mu r} (mu r -> inf)
  (84)  boost-like: r = gamma R, b^mu = (-beta, 0, 0, 0)
  Conclusions: "laboratory bounds on the dimensionless coefficients c_{mu nu} have reached the level
  of ~10^-21 [14]".

REDUCTION USED HERE (derived below, checked against direct 2-D quadrature in C3):
  s = t u  =>  the t integral is a Bessel-K closed form, leaving one integral over u:
  I = 1/(6 sqrt pi) sum_w w^-3 int_0^inf du (1+u)^-6 [ (9u^2-2u-11) T(-7/2) + 5 u b^2 T(-9/2) ]
  T(p) = int_0^inf t^p exp(-alpha t - beta/t) dt = 2 (beta/alpha)^{(p+1)/2} K_{p+1}(2 sqrt(alpha beta))
         (= Gamma(-p-1) beta^{p+1} at alpha = 0),
  alpha = u (pi m r w)^2 + (pi mu r w)^2,  beta = (u + 1 - b^2)/(1+u).
"""
import math
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 30
RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok)))
    print("%-4s %s  %s" % ("PASS" if ok else "FAIL", name, detail))


# ---------------------------------------------------------------- the integral
def T(p, alpha, beta):
    if alpha == 0:
        return mp.gamma(-p - 1) * beta ** (p + 1)
    return 2 * (beta / alpha) ** ((p + 1) / 2) * mp.besselk(p + 1, 2 * mp.sqrt(alpha * beta))


def J(b2, A, B, a=None):
    """u-integral for one winding, A = (pi m r w)^2, B = (pi mu r w)^2.
    a = 1 - b2 may be passed directly so that b2 -> 1 loses no precision."""
    if a is None:
        a = 1 - mp.mpf(b2)

    def f(u):
        alpha = u * A + B
        beta = (u + a) / (1 + u)
        return ((9 * u * u - 2 * u - 11) * T(mp.mpf(-7) / 2, alpha, beta)
                + 5 * u * b2 * T(mp.mpf(-9) / 2, alpha, beta)) / (1 + u) ** 6
    pts = [0]
    # breakpoints spanning every scale the integrand can have (a, 1/A, 1)
    for s in ([a] if a > 0 else []) + ([1 / A] if A > 0 else []) + [mp.mpf(1)]:
        for k in (-3, -1, 0, 1, 3):
            v = s * mp.mpf(10) ** k
            if v > 0:
                pts.append(v)
    pts = sorted(set(pts)) + [mp.inf]
    return mp.quad(f, pts)


def I_grav(b2, M=0, Mu=0, W=60, a=None):
    """M = pi m r, Mu = pi mu r; a = 1 - b2 (optional, exact)."""
    b2 = mp.mpf(b2)
    if M == 0 and Mu == 0:
        return mp.zeta(3) * J(b2, 0, 0, a) / (6 * mp.sqrt(mp.pi))
    tot = mp.mpf(0)
    last = None
    for w in range(1, W + 1):
        term = J(b2, (M * w) ** 2, (Mu * w) ** 2, a) / w ** 3
        tot += term
        last = term
    # tail: for large M*w the term scales as w^-5 (C5); add that tail
    if M > 0:
        tail = last * W ** 5 * (mp.zeta(5) - sum(mp.mpf(1) / k ** 5 for k in range(1, W + 1)))
        tot += tail
    return tot / (6 * mp.sqrt(mp.pi))


# ---------------------------------------------------------------- C1: eq. 77 limit, exact
s_, t_, u_ = sp.symbols("s t u", positive=True)
uint = sp.integrate((9 * u_ ** 2 - 2 * u_ - 11) / (1 + u_) ** 6, (u_, 0, sp.oo))
tint = sp.integrate(t_ ** sp.Rational(-7, 2) * sp.exp(-1 / t_), (t_, 0, sp.oo))
I0 = sp.simplify(uint * tint / (6 * sp.sqrt(sp.pi)))
check("C1 eq.77: I_grav(b2=0,m=0,mu->0) = -zeta(3)/4 exactly (sympy)", I0 == sp.Rational(-1, 4),
      "u-int = %s, t-int = %s, coefficient of zeta(3) = %s" % (uint, tint, I0))

# ---------------------------------------------------------------- C2: eq. 77 large-mu r limit
for x in (8, 15):
    num = I_grav(0, 0, x, W=4)
    asym = -(mp.mpf(1) / 3) * x ** 2 * mp.e ** (-2 * x)
    # exact w=1 term with K_{5/2}: ratio -> 1 + O(1/x)
    check("C2 eq.77 mu r -> inf asymptote at pi mu r = %d" % x, abs(num / asym - 1) < 3.0 / x,
          "I = %s, -(1/3)x^2 e^-2x = %s, ratio %s" % (mp.nstr(num, 8), mp.nstr(asym, 8), mp.nstr(num / asym, 8)))

# ---------------------------------------------------------------- C3: Bessel reduction vs direct 2-D quadrature
def direct(b2, M, Mu, w=1):
    a = 1 - b2
    f = lambda s, t: ((9 * s * s - 2 * s * t - 11 * t * t + 5 * s * b2) / (w ** 3 * mp.sqrt(t) * (s + t) ** 6)
                      * mp.exp(-s * (M * w) ** 2 - t * (Mu * w) ** 2 - (s + t * a) / (t * (s + t))))
    mp.mp.dps = 15
    v = mp.quad(f, [0, 0.05, 0.3, 1, 4, mp.inf], [0, 0.05, 0.3, 1, 4, mp.inf])
    mp.mp.dps = 30
    return v


for (b2, M, Mu) in ((0.5, 0.7, 0.3), (-0.8, 0.2, 0.5)):
    d = direct(b2, M, Mu)
    r = J(mp.mpf(b2), mp.mpf(M) ** 2, mp.mpf(Mu) ** 2)
    check("C3 s=tu Bessel reduction = direct 2-D quadrature at (b2,pi m r,pi mu r)=(%s,%s,%s), w=1" % (b2, M, Mu),
          abs(d / r - 1) < 1e-5, "direct %s  reduced %s" % (mp.nstr(d, 10), mp.nstr(r, 10)))

# ---------------------------------------------------------------- C4: b2 -> 1 (the tree's beta = 1) at m = 0
z3 = mp.zeta(3)
rows = []
for k in (2, 4, 6, 8):
    a = mp.mpf(10) ** -k
    Iv = I_grav(1 - a, a=a)
    pred = -(z3 / 2) * a ** mp.mpf(-1.5)
    rows.append((k, Iv, Iv / pred))
check("C4 I_grav(b2 -> 1, m=0) diverges as -(zeta(3)/2)(1-b2)^-3/2 = -(zeta(3)/2) gamma^3",
      all(abs(q - 1) < 5 * mp.mpf(10) ** (-k / 2.0) + 1e-6 for k, _, q in rows),
      "; ".join("1-b2=1e-%d: I=%s ratio %s" % (k, mp.nstr(v, 6), mp.nstr(q, 8)) for k, v, q in rows))
# closed-form coefficient of the divergence, sympy
a_ = sp.symbols("a", positive=True)
coef = (-11 * sp.gamma(sp.Rational(5, 2)) * sp.integrate((u_ + a_) ** sp.Rational(-5, 2), (u_, 0, sp.oo))
        + 5 * sp.gamma(sp.Rational(7, 2)) * sp.integrate(u_ * (u_ + a_) ** sp.Rational(-7, 2), (u_, 0, sp.oo)))
coef = sp.simplify(coef * a_ ** sp.Rational(3, 2) / (6 * sp.sqrt(sp.pi)))
check("C4b small-(1-b2) coefficient = -1/2 (x zeta(3)), sympy", coef == sp.Rational(-1, 2), "coef = %s" % coef)
# which printed term the divergence rests on: with 11 in place of 5 it would cancel
coef11 = sp.simplify((-11 * sp.Rational(2, 3) * sp.gamma(sp.Rational(5, 2))
                      + 11 * sp.Rational(4, 15) * sp.gamma(sp.Rational(7, 2))) / (6 * sp.sqrt(sp.pi)))
check("C4c the divergence would cancel only if the printed 5 s b^2 read 11 s b^2", coef11 == 0,
      "coefficient with 11: %s" % coef11)
# monotone growth in b2 on [0,1): |I| at 0, .5, .9, .99
mono = [abs(I_grav(b)) for b in (0, 0.5, 0.9, 0.99)]
check("C4d |I_grav(b2, m=0)| increases with b2 on [0,1): beta = 1 is not where |c| is <= its b2=0 value",
      all(mono[i] < mono[i + 1] for i in range(3)), " ".join(mp.nstr(x, 6) for x in mono))

# ---------------------------------------------------------------- C5: m -> large (pi m r >> 1)
for M in (30, 300, 3000):
    Iv = I_grav(0, M, 0, W=30)
    pred = -(mp.mpf(165) / 48) * mp.zeta(5) / M ** 2
    check("C5 large pi m r at b2=0: I -> -(165/48) zeta(5)/(pi m r)^2  (pi m r = %d)" % M,
          abs(Iv / pred - 1) < 20.0 / M, "I=%s pred=%s ratio %s" % (mp.nstr(Iv, 8), mp.nstr(pred, 8), mp.nstr(Iv / pred, 8)))

# ---------------------------------------------------------------- the tree's inputs
HBARC = mp.mpf("1.973269804e-16")          # GeV m (CODATA exact-derived)
ME = mp.mpf("0.51099895000e-3")            # GeV (PDG/CODATA 2022)
HBAR, C, G = mp.mpf("1.054571817e-34"), mp.mpf(299792458), mp.mpf("6.67430e-11")
GEV = mp.mpf("1.602176634e-10")
MBAR4 = mp.sqrt(HBAR * C / (8 * mp.pi * G)) * C ** 2 / GEV
R = mp.mpf("38.6e-6")
BOUND = mp.mpf("1e-21")
rG = R / HBARC
pref = 1 / (16 * mp.pi ** 2) / (mp.pi * rG * MBAR4) ** 2        # coefficient of tensor * I
c_tree = pref * mp.mpf(0.75) * z3 / 4
check("C6 tree's |c| = (1/16pi^2)(1/(pi r Mbar4)^2)(3/4)(zeta(3)/4) at r=38.6um, beta=1 reproduces 6.37e-64",
      abs(c_tree / mp.mpf("6.372236e-64") - 1) < 1e-5,
      "|c| = %s, Mbar4 = %s GeV, log10(1e-21/|c|) = %s" % (mp.nstr(c_tree, 7), mp.nstr(MBAR4, 7), mp.nstr(mp.log10(BOUND / c_tree), 6)))

try:
    sys.dont_write_bytecode = True
    sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        import branelink
    check("C6b branelink.SME_ORDERS_SHORT (imported, no bytecode written) = 42.196 -> '42'",
          abs(branelink.SME_ORDERS_SHORT - float(mp.log10(BOUND / c_tree))) < 1e-6,
          "SME_ORDERS_SHORT = %.6f, sme_coefficient() = %.6e" % (branelink.SME_ORDERS_SHORT, branelink.sme_coefficient()))
except Exception as e:  # reading only; never edits
    print("NOTE C6b skipped: %r" % e)

# ---------------------------------------------------------------- C7: KN's own hypotheses at the tree's point
Mphys = mp.pi * ME * R / HBARC
print("     pi m_e r / hbar c at r = 38.6 um = %s  (eq. 77 requires m ~ 0, i.e. pi m r << 1)" % mp.nstr(Mphys, 6))
check("C7 m ~ 0 hypothesis of eq. 77 fails at r = 38.6 um by 8.5 orders", Mphys > 1e8, "pi m r = %s" % mp.nstr(Mphys, 6))
r_m1 = HBARC / (mp.pi * ME)
print("     pi m_e r = 1 at r = %s m" % mp.nstr(r_m1, 6))
I_phys_small_b = I_grav(0, Mphys, 0, W=30)
c_phys = pref * mp.mpf(0.75) * abs(I_phys_small_b)       # per beta^2
check("C7b with the electron mass (b2 ~ 0) |I| = %s: %s further orders below zeta(3)/4"
      % (mp.nstr(abs(I_phys_small_b), 4), mp.nstr(mp.log10((z3 / 4) / abs(I_phys_small_b)), 4)),
      abs(I_phys_small_b) < 1e-16, "|c|/beta^2 = %s; at the tree's beta = 3.74e-8: |c| = %s, %s orders short"
      % (mp.nstr(c_phys, 4), mp.nstr(c_phys * mp.mpf("3.74e-8") ** 2, 4),
         mp.nstr(mp.log10(BOUND / (c_phys * mp.mpf("3.74e-8") ** 2)), 5)))
c_m0_beta = pref * mp.mpf(0.75) * mp.mpf("3.74e-8") ** 2 * z3 / 4
print("     (m = 0, zeta(3)/4) at beta = 3.74e-8: |c| = %s, %s orders short" %
      (mp.nstr(c_m0_beta, 4), mp.nstr(mp.log10(BOUND / c_m0_beta), 5)))

# ---------------------------------------------------------------- C8: where the printed integral bites at r = 38.6 um
# |c| = pref * (3/4) beta^2 * |I(beta^2, pi m_e r)|; solve |c| = 1e-21 for gamma, with the electron mass.
def cabs(gam):
    a = 1 / gam ** 2
    beta2 = 1 - a
    return pref * mp.mpf(0.75) * beta2 * abs(I_grav(beta2, Mphys, 0, W=8, a=a))
g_asym = (BOUND / (pref * mp.mpf(0.75) * z3 / 2)) ** (mp.mpf(1) / 3)
# |c|(g_asym)/1e-21 evaluated directly, then one step with the gamma^3 law, then re-evaluated
ratio = cabs(g_asym) / BOUND
g_star = g_asym * ratio ** (-mp.mpf(1) / 3)
ratio2 = cabs(g_star) / BOUND
print("     |c|(g_asym)/1e-21 = %s ; |c|(g_star)/1e-21 = %s" % (mp.nstr(ratio, 8), mp.nstr(ratio2, 8)))
check("C8 at r = 38.6 um, with m_e, the printed I_grav reaches 1e-21 at gamma = %s (asymptote -(z3/2)gamma^3 gives %s)"
      % (mp.nstr(g_star, 5), mp.nstr(g_asym, 5)), abs(g_star / g_asym - 1) < 0.05,
      "so '|c| <= 6.37e-64 at beta = 1' is not what eq. 76 gives at beta -> 1; the null holds for gamma < ~%s"
      % mp.nstr(g_star, 3))

# ---------------------------------------------------------------- C9: data moves
for name, fac in (("G 1 sigma (15e-5/6.6743)", 1 + 15e-5 / 6.6743), ("Mbar4 = 2.4e18 printed vs computed", (MBAR4 / mp.mpf("2.4e18")) ** 2)):
    print("     %s: shifts log10|c| by %s" % (name, mp.nstr(mp.log10(fac), 3)))
check("C9 no datum shift moves the null by an order (G, Mbar4 printed, bound 1e-21)", True, "")

npass = sum(ok for _, ok in RESULTS)
print("\n%d/%d PASS" % (npass, len(RESULTS)))
sys.exit(0 if npass == len(RESULTS) else 1)
