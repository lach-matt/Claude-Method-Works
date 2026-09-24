#!/usr/bin/env python3
r"""
fewsterteo.py -- O2: FEWSTER & TEO ON THE CORRIDOR.  OPEN, NARROWED.  71.256 STANDS.

DOCKET 62 worked O2 and every figure it produced lived in a scratch directory.
The ruling on DOCKET 62 said the first fault of step 3 was that NOTHING WAS
SEATED -- the exact way S5's four figures died -- and this file is the seating of
what the ruling says survives.  It is not a re-run of the docket's proposal: the
proposal (a 1.343-order tightening, 72.599 orders, O2 closed) is REFUSED here, and
the refusal is computed rather than asserted.

    python3 fewsterteo.py             the reading
    python3 fewsterteo.py --selftest  every figure re-derived; sympy + mpmath, < 1 min

Run from research/warp-drive (recovered/struct.py shadows stdlib struct from
directories that can see recovered/).

===============================================================================
1. WHAT SURVIVES, AND IS SEATED
===============================================================================

(a) THE PREFACTOR OF F&T (2.12)/(2.13) IS EXACTLY 1.  THEOREM, two routes, both
    symbolic: from their legible (2.10)+(2.11) by a Leibniz identity and the
    field equation, and from their printed Minkowski form (3.2).  The PDF text
    layer drops it; nothing here trusts the text layer.

(b) THE 9/64 IS EXACT, AND IT MUST NOT BE APPLIED TO C_F.  F&T's flat massless
    bound with Ford-Roman's Lorentzian sampler is exactly 9/64 of Ford-Roman's
    (their (6.9) at alpha = 5/2, exact rationals).  The tempting move is to
    tighten DOCKET 55's persistence refusal by log10(64/9) = 0.851937 orders.
    REFUSED: C_F = mu_1^4/(16 pi^2) IS ALREADY the Fewster-Teo family's constant
    at the OPTIMAL COMPACTLY SUPPORTED sampler.  Applying 64/9 to it would count
    the same tightening twice.  The ruling calls this the best thing in the
    docket, and it is recorded here as a refusal with its number computed.

(c) THE C_F IDENTIFICATION, BY THE PARSEVAL ROUTE.  F&T (5.6) at spectral gap
    C = 0 is (1/16 pi^3) INT_0^oo u^4 |ghat(u)|^2 du.  u^4|ghat|^2 = |FT(g'')|^2
    for a clamped sampler, Parseval turns the integral into pi INT (g'')^2, and
    for the clamped-beam fundamental INT (g'')^2 = mu_1^4 INT g^2 by the identity
    (g g''' - g' g'')' = g g'''' - (g'')^2 with every boundary term clamped to
    zero.  So (5.6) at C = 0 returns mu_1^4/(16 pi^2) = C_F exactly.
      NOT AN INDEPENDENT CONFIRMATION.  achievable.FEWSTER_C is literally
      mu_1^4/(16 pi^2), so a 41-digit agreement is two evaluations of one closed
      form.  What is new is the ROUTE, not a check.

(d) F&T SEC. 7 IS NOT TRANSPLANTABLE TO M < 0.  Their Schwarzschild bound is
    built on Candelas' outgoing/ingoing mode sums, whose basis is DEFINED BY
    HORIZON BOUNDARY CONDITIONS.  With m < 0 there is no horizon: the horizon is
    not a caveat on Sec. 7, it is Sec. 7's mode-defining surface.  Continuing
    (7.10) to M < 0 would be failure mode (4).  NOT DONE, and pinned False.

(e) THE CORRIDOR'S OWN MODE FUNCTIONS ARE NOT-FOUND.  The massless radial
    equation on -F dt^2 + dr^2/F + r^2 dOmega^2 has regular singular points at
    r = 0 and r = 2M and an IRREGULAR one at infinity (Q -> omega^2 != 0): the
    confluent Heun class, with no closed form in named special functions.  For
    M < 0 the second regular point sits at r = 2M < 0, off the domain, and the
    class is unchanged.  A property of the equation, derived here by sympy.

===============================================================================
2. WHY IT DOES NOT CLOSE -- THE SPECTRAL-GAP SWEEP
===============================================================================

The docket evaluated F&T (5.6) on the static open Robertson-Walker universe
(ultrastatic, slices H^3 of radius a_c), matched so |rho| equals the corridor's
demand.  It got a ratio 0.0454 to the flat bound -- 1.343 orders tighter -- and
proposed 72.599.  The ruling swept the one parameter that produces the number:
the lower limit C of (5.6), which on H^3 is the spectral gap 1/a_c.

    ratio(C) = 1 - [ INT_0^C u^4|ghat|^2 du
                     + INT_C^oo u^4|ghat|^2 (1 - Q_3(u/C)) du ] / (pi mu_1^4)

with Q_3(x) = 4 x^-4 INT_1^x y^2 sqrt(y^2-1) dy in closed form (F&T (3.5), n = 3,
as READ by the DOCKET 62 O2 pass; the closed form is verified here by symbolic
differentiation).  MEASURED here, stdlib, composite 20-point Gauss-Legendre over
unit panels to u = 2e4, converged to 1e-10 against panel halving and u = 1e5:

    C = 35.355 (witness)  0.0453939       C = 1      0.974321
    C = 10                0.165631        C = 0.1    0.999753886522
    C = 5                 0.469090        C = 0.01   0.999997542191
                                          C = 0      1   (exactly: Q_3 -> 1)

THE CORRIDOR IS ASYMPTOTICALLY FLAT.  HYPOTHESIS, named: an asymptotically flat
complete spatial slice has Laplace spectrum running continuously down to zero, so
w_min = 0, C = 0, ratio = 1, and (5.6) returns the flat bound exactly.  Even the
most generous gap the corridor's own geometry could supply -- a cavity at
concentric.py's compensating shell R_s = 200 b, C = 0.005 in units of c/b --
leaves the ratio at 0.999999.  The three properties the witness was chosen for
(rho < 0, m(R) < 0 with m(0) = 0, NEC violated) are INERT: ratio() takes C and
nothing else.  71.256 STANDS, UNMOVED IN EITHER DIRECTION.  72.599 and 72.247 are
REFUSED -- computed below only so the refusal names what it refuses.

A SECOND, INDEPENDENT REASON NOT TO CLOSE.  ledger.py's own answering condition
for O2 is "evaluate it once the corridor's scalar mode functions are determined".
(e) shows they cannot be; the docket evaluated on a third spacetime.

===============================================================================
3. THE RIGHT INSTRUMENT IS FEWSTER & SMITH, NOT FEWSTER & TEO
===============================================================================

Fewster & Smith, "Absolute quantum energy inequalities", gr-qc/0702056v3, READ at
source by the DOCKET 62 ruling.  Their eq. (5) bounds INT f^2 <v^a v^b T^ren_ab>
from below by B_A, which depends ONLY ON LOCAL GEOMETRY and no reference state,
for the minimally coupled Klein-Gordon field of mass >= 0 on ANY four-dimensional
globally hyperbolic spacetime.  The corridor is in that class.  Their flat
massless check, eq. (88), -(1/16 pi^3) INT |fhat|^2 eta^4, has the same form and
constant as F&T (5.6) at C = 0.  RESTATED O2: evaluate the ABSOLUTE QEI on the
corridor.  Still blocked on the same mode functions, and it additionally carries
C_ab, the state-independent conserved local curvature term that vanishes in
Minkowski.  Fewster 1208.5399 on this point: NOT-SEARCHED.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

    IT DOES NOT CLOSE O2.  O2 stays OPEN, narrowed.
    IT DOES NOT MOVE 71.256.  It imports achievable.py's figure and leaves it.
    IT DOES NOT APPLY 64/9.  Section 1(b).
    IT DOES NOT QUOTE THE 41-DIGIT AGREEMENT AS CONFIRMATION.  Section 1(c).
    IT DOES NOT EVALUATE SEC. 7 AT M < 0.  Section 1(d).
"""

import cmath
import math
import sys

import achievable
import concentric

# ---------------------------------------------------------------------------
# The ruling, as data.  Booleans and strings are what ledger.py asks; every
# number below is either computed at import (stdlib, cheap) or a FIXTURE that
# --selftest reproduces with the code in this file.
# ---------------------------------------------------------------------------

O2_STATUS = "OPEN (narrowed) -- NOT CLOSED"
O2_CLOSED = False

#: (a) THEOREM, two routes; --selftest re-derives both in sympy.
PREFACTOR_212 = 1

#: (b) THEOREM (exact rationals through F&T (6.9)); --selftest reproduces it.
NINE_64 = (9, 64)
NINE_64_APPLIES_TO_C_F = False          # the anti-double-counting refusal
#: The void adjustment, COMPUTED so the refusal names its size.  NOT SEATED.
VOID_ADJUSTMENT_ORDERS = math.log10(NINE_64[1] / NINE_64[0])

#: (c) the Parseval route is new; the 41-digit agreement is not a check.
C_F_IS_FT_CONSTANT_AT_OPTIMAL_SAMPLER = True
C_F_AGREEMENT_IS_INDEPENDENT = False

#: (d) and (e)
SEC7_TRANSPLANTABLE_TO_NEGATIVE_M = False
CORRIDOR_MODE_FUNCTIONS = "NOT-FOUND -- confluent Heun (a property of the equation)"

#: Section 2.  The corridor is asymptotically flat, so its spectral gap is zero.
CORRIDOR_SPECTRAL_GAP = 0.0
GAP_HYPOTHESIS = ("an asymptotically flat complete spatial slice has Laplace "
                  "spectrum running continuously to zero")
WITNESS_PROPERTIES_INERT = True         # ratio() is a function of C alone
FLAT_FIGURE_STANDS = True               # 71.256, achievable.py's, unmoved

#: Section 3.
RIGHT_INSTRUMENT = ("Fewster & Smith, absolute QEI, gr-qc/0702056 eq. (5) -- "
                    "minimally coupled KG, mass >= 0, any 4D globally "
                    "hyperbolic spacetime; READ at source by the DOCKET 62 ruling")
O2_ANSWERED_BY = ("evaluate Fewster & Smith's ABSOLUTE QEI on the corridor -- "
                  "blocked on the corridor's scalar mode functions (NOT-FOUND, "
                  "confluent Heun), and carrying C_ab, the conserved local "
                  "curvature term that vanishes in Minkowski")
FEWSTER_1208_5399_ON_THIS = "NOT-SEARCHED"

#: C (units of c/b) -> ratio.  MEASURED by ratio() below; the ruling's own
#: script (/tmp/rulework/fast2.py) printed these, and ratio() reproduces every
#: one to the digits printed.
GAP_SWEEP = ((20.0, 0.0807201), (10.0, 0.165631), (5.0, 0.469090),
             (1.0, 0.974321), (0.1, 0.999753886523), (0.01, 0.999997542191))
#: the witness ratio and its orders.  MEASURED; three evaluations (the O2 pass
#: at 40 dps mpmath, the ruling's numpy, this file's stdlib) agree to 1e-6.
WITNESS_RATIO = 0.0453939
WITNESS_ORDERS = 1.343002


# ============================================================ the geometry
def witness_gap():
    """C = b/a_c for the H^3 witness matched to achievable.py's demand at b = 1.

    3 c^4/(8 pi G a_c^2) = required_density(b).  The sampler length is also b,
    so C is scale-free (b cancels) -- in units of c/b."""
    b = 1.0
    a_c = math.sqrt(3.0 * achievable.C_SI ** 4
                    / (8.0 * math.pi * achievable.G_SI
                       * achievable.required_density(b)))
    return b / a_c


def cavity_gap():
    """The most generous gap the corridor's own geometry could supply: a cavity
    at concentric.py's compensating shell, C = b/R_s in units of c/b."""
    return 1.0 / concentric.R_SHELL


# ============================================================ the sampler
_MU = achievable.FEWSTER_MU1            # imported, never recomputed here


def _sampler():
    """The clamped-beam fundamental on [0,1] as sum_k c_k exp(a_k t)."""
    mu = _MU
    sig = (math.cosh(mu) - math.cos(mu)) / (math.sinh(mu) - math.sin(mu))
    a = (mu, -mu, 1j * mu, -1j * mu)
    c = (0.5 - 0.5 * sig, 0.5 + 0.5 * sig, -0.5 - 0.5j * sig, -0.5 + 0.5j * sig)
    return a, c


def _gl_nodes(n):
    """Gauss-Legendre nodes and weights by Newton on P_n.  STDLIB ONLY."""
    xs, ws = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1.0)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-16:
                break
        xs.append(x)
        ws.append(2.0 / ((1.0 - x * x) * dp * dp))
    return tuple(zip(xs, ws))


_GL20 = _gl_nodes(20)


def _panels(fn, a, b, width=1.0, nodes=_GL20):
    n = max(1, int(math.ceil((b - a) / width)))
    tot = 0.0
    for k in range(n):
        lo = a + (b - a) * k / n
        hi = a + (b - a) * (k + 1) / n
        h, m = 0.5 * (hi - lo), 0.5 * (hi + lo)
        tot += h * sum(w * fn(m + h * x) for x, w in nodes)
    return tot


def _norm():
    a, c = _sampler()

    def g(t):
        return sum(ck * cmath.exp(ak * t) for ak, ck in zip(a, c)).real
    return _panels(lambda t: g(t) ** 2, 0.0, 1.0, 0.02)


_N = None


def u4ghat2(u):
    """u^4 |ghat(u)|^2 = |FT(g'')(u)|^2 for the normalised clamped sampler.

    Written through g'' rather than g: g'' has a 1/u transform, g a 1/u^3 one,
    and the direct form loses every digit to cancellation at large u."""
    global _N
    if _N is None:
        _N = _norm()
    a, c = _sampler()
    s = 0j
    for ak, ck in zip(a, c):
        z = ak - 1j * u
        s += ck * ak * ak * (cmath.exp(z) - 1.0) / z
    return (s.real ** 2 + s.imag ** 2) / _N


def Q3(x):
    """F&T (3.5) at n = 3: 4 x^-4 INT_1^x y^2 sqrt(y^2-1) dy, closed form."""
    if x <= 1.0:
        return 0.0
    return ((x * (2 * x * x - 1) * math.sqrt(x * x - 1) - math.acosh(x))
            / (2 * x ** 4))


def flat_total():
    """INT_0^oo u^4|ghat|^2 du = pi INT (g'')^2 = pi mu_1^4 (Parseval + clamping)."""
    return math.pi * _MU ** 4


def ratio(C, u_max=2.0e4, width=1.0):
    """|bound|_(5.6), gap C / |bound|_flat, same sampler.  C in units of 1/tau."""
    if C <= 0.0:
        return 1.0
    d = _panels(u4ghat2, 0.0, C, width)
    d += _panels(lambda u: u4ghat2(u) * (1.0 - Q3(u / C)), C, u_max, width)
    return 1.0 - d / flat_total()


def refused_figures():
    """The two figures the docket proposed, COMPUTED so the refusal names them.

    72.599 = 71.256 - log10(witness ratio).  72.247 is that less the |g_tt|^2
    redshift loosening at the core surface, |g_tt| = 1 + 2(M/b)/(a/b).  BOTH
    REFUSED: the witness's gap is a property the corridor lacks."""
    flat = math.log10(achievable.persistence_shortfall(1.0))
    curved = flat - math.log10(ratio(witness_gap()))
    gtt = 1.0 + 2.0 * achievable.M_OVER_B / achievable.A_OVER_B
    return flat, curved, curved - math.log10(gtt ** 2)


# COMPUTED AT IMPORT (cheap): the witness gap and the flat figure that stands.
#: ratio() itself is ~0.7 s a call, so the witness RATIO is the pinned fixture
#: WITNESS_RATIO above, reproduced by --selftest, not recomputed on import.
WITNESS_GAP = witness_gap()
CAVITY_GAP = cavity_gap()
FLAT_SHORTFALL_ORDERS = math.log10(achievable.persistence_shortfall(1.0))


# ============================================================ symbolic
def verify_symbolic(sp):
    """Every derivation the ruling kept, redone in sympy.  Returns rows
    (label, got, want)."""
    rows = []
    # (a) route 1 -- Leibniz + field equation turn (2.10)'s bracket into 2x (2.12)'s
    x = sp.symbols('x', real=True)
    A = sp.Function('A', real=True)(x)
    B = sp.Function('B', real=True)(x)
    K = sp.symbols('K', real=True)
    U, Uc = A + sp.I * B, A - sp.I * B
    lap = sp.diff(sp.expand(Uc * U), x, 2)
    grad = sp.expand(sp.diff(Uc, x) * sp.diff(U, x))
    leib = sp.simplify(sp.expand(lap - (sp.diff(Uc, x, 2) * U + Uc * sp.diff(U, x, 2)
                                        + 2 * grad)))
    rows.append(("(a) Leibniz residual", leib, 0))
    fe = {sp.diff(A, x, 2): -K * A, sp.diff(B, x, 2): -K * B}
    onshell = sp.simplify(sp.expand((grad - (lap / 2 + K * Uc * U)).subs(fe)))
    rows.append(("(a) on-shell grad U*.grad U = lap|U|^2/2 + K|U|^2", onshell, 0))
    W2, MU2, LAP, M2 = sp.symbols('W2 MU2 LAP M2')
    b210 = sp.expand(W2 * M2 + (LAP / 2 + (W2 - MU2) * M2) + MU2 * M2)
    b212 = W2 * M2 + LAP / 4
    P = sp.Rational(1, 2) * sp.simplify(b210 / b212)
    rows.append(("(a) route 1: prefactor of (2.12)", P, PREFACTOR_212))
    # route 2 -- the printed Minkowski (3.2) carries -(1/2) INT w_k/(2pi)^n,
    # and (2.12) with |U_k|^2 = 1/((2pi)^n 2 w_k) gives -(P/2) of the same.
    rows.append(("(a) route 2: prefactor from printed (3.2)",
                 sp.Rational(1, 2) / sp.Rational(1, 2), PREFACTOR_212))

    # (b) the 9/64, exact rationals through F&T (6.9) at alpha = 5/2
    t0 = sp.Symbol('t_0', positive=True)
    al = sp.Rational(5, 2)
    I69 = 2 ** (2 * al - 3) * t0 ** (-2 * al) * sp.gamma(al) ** 4 / sp.gamma(2 * al)
    ft = sp.simplify(1 / (16 * sp.pi ** 3) * (4 * t0 / sp.pi) * I69)
    fr = sp.Rational(3) / (32 * sp.pi ** 2 * t0 ** 4)
    r964 = sp.nsimplify(sp.simplify(ft / fr))
    rows.append(("(b) F&T flat massless / Ford-Roman, exact", r964,
                 sp.Rational(*NINE_64)))

    # (c) the Parseval route: the clamped-beam mode, its ODE, and the
    # integration-by-parts identity whose boundary terms clamping kills.
    t, k, s = sp.symbols('t k sigma', real=True)
    g = (sp.cosh(k * t) - sp.cos(k * t)) - s * (sp.sinh(k * t) - sp.sin(k * t))
    rows.append(("(c) g'''' - k^4 g", sp.simplify(sp.diff(g, t, 4) - k ** 4 * g), 0))
    f = sp.Function('f')(t)
    ibp = sp.simplify(sp.diff(f * sp.diff(f, t, 3) - sp.diff(f, t) * sp.diff(f, t, 2), t)
                      - (f * sp.diff(f, t, 4) - sp.diff(f, t, 2) ** 2))
    rows.append(("(c) (f f''' - f'f'')' - (f f'''' - f''^2)", ibp, 0))
    mu = sp.Symbol('mu', positive=True)
    rows.append(("(c) (5.6) at C=0 = pi mu^4/(16 pi^3) - mu^4/(16 pi^2)",
                 sp.simplify(sp.pi * mu ** 4 / (16 * sp.pi ** 3)
                             - mu ** 4 / (16 * sp.pi ** 2)), 0))

    # section 2 -- Q_3's closed form, by differentiating the antiderivative
    y = sp.Symbol('y', positive=True)
    anti = (y * (2 * y ** 2 - 1) * sp.sqrt(y ** 2 - 1) - sp.acosh(y)) / 8
    rows.append(("Q_3: d/dy antiderivative - y^2 sqrt(y^2-1)",
                 sp.simplify(sp.diff(anti, y) - y ** 2 * sp.sqrt(y ** 2 - 1)), 0))
    rows.append(("Q_3: antiderivative at y = 1", sp.simplify(anti.subs(y, 1)), 0))
    xq = sp.Symbol('x', positive=True)
    q3 = 4 * xq ** -4 * anti.subs(y, xq)
    rows.append(("Q_3(x) -> 1 as x -> oo, i.e. C -> 0 returns the flat bound",
                 sp.limit(q3, xq, sp.oo), 1))

    # (e) the corridor's radial equation, from the metric, and its singular points
    r, Mm, w, l = sp.symbols('r M omega l', real=True)
    F = 1 - 2 * Mm / r
    R = sp.Function('R')(r)
    # box phi for -F dt^2 + dr^2/F + r^2 dOmega^2, phi = R(r) Y_lm e^{-i w t}:
    # sqrt(-g) = r^2 sin(theta); g^tt = -1/F, g^rr = F
    box = (sp.diff(r ** 2 * F * sp.diff(R, r), r) / r ** 2
           + w ** 2 / F * R - l * (l + 1) / r ** 2 * R)
    E = sp.expand(box)
    c2 = E.coeff(sp.Derivative(R, (r, 2)))
    c1 = E.coeff(sp.Derivative(R, r))
    c0 = sp.expand(E - c2 * sp.Derivative(R, (r, 2)) - c1 * sp.Derivative(R, r)).coeff(R)
    Pc, Qc = sp.cancel(c1 / c2), sp.cancel(c0 / c2)
    reg0 = all(sp.limit(e, r, 0).is_finite for e in (r * Pc, r ** 2 * Qc))
    reg2M = all(sp.limit(sp.cancel(e), r, 2 * Mm).is_finite
                for e in ((r - 2 * Mm) * Pc, (r - 2 * Mm) ** 2 * Qc))
    irr_inf = sp.simplify(sp.limit(Qc, r, sp.oo) - w ** 2) == 0
    rows.append(("(e) r = 0 regular singular", reg0, True))
    rows.append(("(e) r = 2M regular singular", reg2M, True))
    rows.append(("(e) r = oo irregular (Q -> omega^2 != 0): confluent Heun",
                 irr_inf, True))
    return rows


def ft69_quadrature(mp):
    """F&T (6.9) against direct quadrature of INT u^(2a-1) K_0(u)^2, 30 dps.
    `mp` is the mpmath MODULE; precision lives on its context, mp.mp."""
    mp.mp.dps = 30
    out = []
    for av in (mp.mpf(1), mp.mpf(3) / 2, mp.mpf(5) / 2):
        lhs = mp.quad(lambda u: u ** (2 * av - 1) * mp.besselk(0, u) ** 2,
                      [0, 1, 10, 100, mp.inf])
        rhs = mp.mpf(2) ** (2 * av - 3) * mp.gamma(av) ** 4 / mp.gamma(2 * av)
        out.append((float(av), float(abs(lhs - rhs) / abs(rhs))))
    return out


def clamped_boundary(mp):
    """g, g' at both ends of the clamped mode at mu_1, 30 dps -- the boundary
    terms the Parseval route needs to vanish."""
    mp.mp.dps = 30
    mu = mp.findroot(lambda m: mp.cos(m) * mp.cosh(m) - 1, mp.mpf('4.73'))
    sg = (mp.cosh(mu) - mp.cos(mu)) / (mp.sinh(mu) - mp.sin(mu))
    g = lambda t: mp.cosh(mu * t) - mp.cos(mu * t) - sg * (mp.sinh(mu * t) - mp.sin(mu * t))
    return max(abs(v) for v in (g(0), mp.diff(g, 0), g(1), mp.diff(g, 1)))


# ============================================================ report / selftest
def report():
    print(__doc__.split("=====", 1)[0].strip())
    Cw = witness_gap()
    print("\nWITNESS GAP  C = b/a_c = %.10f  (units of c/b; scale-free)" % Cw)
    print("\nRATIO AS THE GAP CLOSES  (F&T (5.6), same sampler)")
    for C in (Cw, 20.0, 10.0, 5.0, 1.0, 0.1, 0.01, cavity_gap(), 0.0):
        r = ratio(C)
        print("   C = %-12.6g ratio = %.12f   (%.8f orders tighter)"
              % (C, r, abs(math.log10(r))))
    flat, c1, c2 = refused_figures()
    print("\n71.256 STANDS:        flat shortfall at 1 m  = %.6f orders (achievable.py)" % flat)
    print("REFUSED, NOT SEATED:  witness-gap shortfall  = %.6f" % c1)
    print("REFUSED, NOT SEATED:  ... less |g_tt|^2      = %.6f" % c2)
    print("REFUSED, NOT SEATED:  64/9 adjustment        = %.7f orders" % VOID_ADJUSTMENT_ORDERS)
    print("\nO2: %s" % O2_STATUS)
    print("RESTATED: %s" % O2_ANSWERED_BY)
    return 0


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-60s %s" % ("ok" if good else "XX", label,
                                   got if good else "%s != %s" % (got, want)))

    def near(label, got, want, tol):
        nonlocal ok
        d = abs(got - want) / max(1e-300, abs(want))
        good = d <= tol
        ok &= good
        print("  [%s] %-60s %.12g (rel %.1e)" % ("ok" if good else "XX", label, got, d))

    try:
        import sympy as sp
        import mpmath as mp
    except ImportError as exc:                       # pragma: no cover
        raise SystemExit("fewsterteo.py --selftest needs sympy/mpmath: %s" % exc)

    print("1. THE SYMBOLIC DERIVATIONS THE RULING KEPT (sympy)")
    for lab, got, want in verify_symbolic(sp):
        if isinstance(got, bool):
            chk(lab, got, want)
        else:
            chk(lab, sp.simplify(got - want) == 0, True)

    print("\n2. THE 9/64 NUMERICALLY, AND THE REFUSAL")
    for av, rel in ft69_quadrature(mp):
        chk("F&T (6.9) matches quadrature at alpha = %.1f (rel < 1e-20)" % av,
            rel < 1e-20, True)
    near("the void adjustment log10(64/9), COMPUTED", VOID_ADJUSTMENT_ORDERS,
         0.8519374645, 1e-9)
    chk("and it is NOT applied to C_F", NINE_64_APPLIES_TO_C_F, False)

    print("\n3. THE PARSEVAL ROUTE, NUMERICALLY -- AND WHY IT IS NOT A CHECK")
    chk("clamped mode: g = g' = 0 at both ends (30 dps, < 1e-20)",
        clamped_boundary(mp) < 1e-20, True)
    near("sampler normalised: INT_0^1 g^2", _norm(), 1.0, 1e-12)
    near("(5.6) at C=0: pi mu_1^4/(16 pi^3) against achievable.FEWSTER_C",
         flat_total() / (16 * math.pi ** 3), achievable.FEWSTER_C, 1e-13)
    part = _panels(u4ghat2, 0.0, 2.0e4)
    a, c = _sampler()
    g2 = [sum((ck * ak * ak * cmath.exp(ak * t0)).real
              for ak, ck in zip(a, c)) for t0 in (0.0, 1.0)]
    tail = (g2[0] ** 2 + g2[1] ** 2) / _N / 2.0e4        # INT_U^oo avg/u^2
    near("Parseval: INT_0^oo |FT g''|^2 du (quadrature + 1/u^2 tail) = pi mu^4",
         part + tail, flat_total(), 1e-5)
    chk("the 41-digit agreement is NOT independent (one closed form, twice)",
        C_F_AGREEMENT_IS_INDEPENDENT, False)

    print("\n4. THE GAP SWEEP -- AND ITS CONTROLS FIRE BOTH WAYS")
    Cw = witness_gap()
    near("witness gap C = b/a_c = 1/0.0282842712", Cw, 35.35533905932738, 1e-12)
    rw = ratio(Cw)
    near("witness ratio (MEASURED)", rw, WITNESS_RATIO, 1e-5)
    near("witness orders tighter", -math.log10(rw), WITNESS_ORDERS, 1e-5)
    chk("CONTROL: the instrument CAN report a tightening (ratio < 0.05)", rw < 0.05, True)
    for C, want in GAP_SWEEP:
        near("ratio at C = %g" % C, ratio(C), want, 1e-5 if C > 0.5 else 1e-11)
    chk("CONTROL: C = 0 returns the flat bound exactly", ratio(0.0), 1.0)
    chk("ratio monotone in C over the sweep",
        all(ratio(x) > ratio(y) for x, y in ((0.01, 0.1), (0.1, 1.0), (1.0, 5.0),
                                             (5.0, 10.0), (10.0, 20.0))), True)
    near("convergence: panel halving moves the witness ratio by < 1e-9",
         ratio(Cw, width=0.5), rw, 1e-8)
    rc = ratio(cavity_gap())
    chk("cavity at R_s = 200 b: C = 0.005", cavity_gap(), 0.005)
    chk("... leaves the ratio at 0.999999 (6 d.p.)", round(rc, 6), 0.999999)
    chk("the corridor's gap is zero, so its ratio is 1",
        ratio(CORRIDOR_SPECTRAL_GAP), 1.0)

    print("\n5. 71.256 STANDS; THE PROPOSED FIGURES ARE REFUSED")
    flat, c1, c2 = refused_figures()
    near("flat shortfall imported from achievable.py", flat, 71.256, 1e-4)
    near("REFUSED 72.599 (flat + witness orders), computed not seated", c1, 72.599, 1e-5)
    near("REFUSED 72.247 (less |g_tt|^2 = 2.25 at the core surface)", c2, 72.247, 1e-5)
    chk("the flat figure stands", FLAT_FIGURE_STANDS, True)
    chk("the witness properties are inert", WITNESS_PROPERTIES_INERT, True)

    print("\n6. WHAT THE ROW IS NOW")
    chk("O2 is not closed", O2_CLOSED, False)
    chk("Sec. 7 is not transplanted to M < 0", SEC7_TRANSPLANTABLE_TO_NEGATIVE_M, False)
    chk("the corridor's mode functions are NOT-FOUND",
        CORRIDOR_MODE_FUNCTIONS.startswith("NOT-FOUND"), True)
    chk("the right instrument is Fewster & Smith's absolute QEI",
        "0702056" in RIGHT_INSTRUMENT, True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
