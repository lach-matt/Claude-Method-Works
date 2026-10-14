#!/usr/bin/env python3
"""b4d_stage6.py -- Warp Theorem lemma B4d, stage 6: the two planes together (M-RULINGS item 165).  Computed and
deduced; verified once (findings applied, B4D-STAGE6.md History); not seated.  First headed "... not verified; not
seated" -- and first concluding that the rulings leave no regular corridor, before its verifier showed that under 138
position 2's plane carries exactly 139's -1/3 with the warp growing on both sides.

M's words (verbatim in the rulings file): item 165 "Of course. Continue" (on the board's next step: the negative-tension
plane and a positive-tension plane together); item 139 (1) "yes" (position 2's plane negative, a quarter of ours in
magnitude, ours positive -- multiplane.py M4's +4/3 and -1/3); item 127 (1) "yes" (the planes coincide, the extra
dimension included), read by item 152 (1) "two separate positions connected by/reached through a dimension"; item 141
(the planes are static); items 117/120 ("the NEC only ever appears to break, but never does"); item 138 (the bulk is
multi-universal, each universe under its own laws); the theorem's clause (B) ("A vacuum five-dimensional bulk carries
the corridor. The plane is free of matter, at the Randall-Sundrum tension").

Stage 5 (verified once): with eq. (17) on a plane and pure-trace data, the bulk is singular within 8-16 clocks on a side
where the warp decays (F2) and regular on the evidence on a side where it grows (F6).  This stage asks which the
rulings allow.  Throughout: K diagonal (no flux or rotation across the plane), Lambda < 0 on every side.

  J1 WHAT A MATTER-FREE PLANE CARRYING EQ. (17) CAN BE, ONE ell (computed, exact).  On each side K^a_b = a delta +
     Pi^a_b, Pi traceless.  Eq. (17) has R4 = 0, so the Gauss constraint is 12 a^2 - Pi.Pi = 12/ell^2 (an identity of
     the parametrisation; its verifier checked the constraint on b4_static.py's series): |a| >= 1/ell.  No matter means
     Pi_L = -Pi_R (own-normal convention), and sigma = -3 (a_L + a_R)/kappa^2, so with one ell
        sigma/lambda_RS in {0} or {+-sqrt(1 + Pi.Pi ell^2/12)}.
     Control: Randall-Sundrum's plane, sigma = +lambda_RS.  The sign of a says which side only at Pi = 0 (stage 5 used
     pure-trace data): a < 0, decaying (F2, singular); a > 0, growing (F6, regular on the evidence).
  J2 READ AS ONE PLACE, THE COINCIDENT PAIR IS A POSITIVE PLANE DECAYING ON BOTH SIDES (computed, one ell).  At a
     coincidence the junction sees the summed tension, +4/3 - 1/3 = +1 lambda_RS (b5_positive.py B5a; as M4's composite
     at zero separation).  By J1, +1 forces Pi = 0 and decay on both sides: F2's singular bulk.  Under 152 the positions
     are separate, joined through the dimension, and J2 is one reading of 127, not the only one.
  J3 POSITION 2'S PLANE, ALONE, AT 139'S TENSION (computed).  With one ell, -1/3 is not attainable by a matter-free plane
     carrying eq. (17).  With each universe's own ell (138), a mirrored sheet whose own ell_2 = 3 ell, growing on both
     sides, carries exactly -1/3 lambda_RS(ell) at Pi = 0 -- a stage 5 F6 plane, regular on the evidence (for ell_2 in
     F6's tested range, 2m-m/2).
  J4 A MIRRORED PLANE BOUNDING A GROWING SLAB CARRIES NEC-BREAKING MATTER (computed; exact at small d; linear order at
     every d).  Eq. (17) on a negative plane at y = 0, the slab closed by a mirrored positive plane at y = d (Randall-
     Sundrum I's arrangement).  It must carry rho + p_r = R4_kk (d - 3d^2/ell) + O(d^3) (exact; R4_kk < 0); at linear
     order in the 4D curvature, (R4_kk ell/2)(e^(-2d/ell) - e^(-4d/ell)), negative at every d, peaked at d = (ln 2/2)
     ell (derived by the verifier; checked here: it solves the background equation and expands to the exact terms).  Raw
     Padé at r = 2.15m and 3m, d = 0.1-4m, ell = 2m and m: negative, within 50% of the linear form (two orders; the third
     breaks down at ell = m, r = 2.15m, d = 4m); its tension tends to +lambda_RS.  Nonlinear corrections beyond Padé are
     not computed.  So a mirrored bounding plane breaks the NEC (117/120); under 138 the far side need not be a mirror,
     and a matter-free junction then passes anisotropic data, Pi_beyond = -Pi_slab, into another bulk -- an escape.
  J5 GROWING ON EVERY SIDE MEANS NEGATIVE TENSION (STRUCTURAL).  With each universe's own ell and any anisotropy, a plane
     whose trace part grows on both sides has tension -(sqrt(1/ell_L^2 + Pi.Pi/12) + sqrt(1/ell_R^2 + Pi.Pi/12))/2 < 0.
  J6 EVERY POSITIVE-TENSION PLANE HAS A DECAYING SIDE (STRUCTURAL).  sigma = -3 (a_L + a_R)/kappa^2 two-sided and
     -3 a/kappa^2 one-sided, for any ell on any side (the Israel condition holds no Lambda); so sigma > 0 needs some a < 0.
  VERDICT (deduced).  On M's rulings together with the board's readings:
     * our plane -- positive by 139, at the Randall-Sundrum tension by clause (B) -- cannot carry eq. (17) with a regular
       bulk: it has a decaying side (J6), which F2 makes singular within 8-16 clocks (premise: a decaying side inside the
       hold's cone makes the corridor's bulk not regular; Pi = 0; one ell or two);
     * position 2's plane can: with its own ell_2 = 3 ell (138) both its sides grow at exactly 139's -1/3 (J3) -- F6's
       regular bulk.  That is the live route for 161: eq. (17) on position 2's plane, not ours (H-EQ17-ON-P2), with 152's
       reading of 127.  It needs clause (B)'s "at the Randall-Sundrum tension" not to apply to the corridor's plane, and
       leaves open what our plane carries and how the two bulks join, the data at the bulk's edge (F6), and item 165's
       own question, whether gravity stays four-dimensional.
     The conjunction: M's 127/152, 138, 139, 117/120 and clause (B); the board's diagonal K, Lambda < 0 on every side,
     Pi = 0 for the regularity link, a mirrored closing plane (J4), eq. (17) on the plane through the write, a vacuum
     bulk, B4b's locally analytic class, Padé as evidence, the column and ell values of stage 5.  Also open:
     anisotropic data (Pi != 0, including a non-mirrored far side), off-diagonal K (141's internal motion, the inflow --
     its verifier found static radial flux likely singular at the throat), a non-vacuum bulk (158 (4); against clause
     (B) as written), and a bulk outside the analytic class.

Imports lemmas/b4d_stage5.py (and through it b4_static.py) by path.  Needs python-flint, sympy, numpy, mpmath.
python3 b4d_stage6.py [--selftest]   (selftest about 2 min)
"""
import contextlib
import math
import importlib.util
import io
import os
import sys
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
ORDER = 28
DS = (0.1, 0.5, 1.0, 2.0, 3.0, 4.0)


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


S5 = _load(os.path.join(HERE, "b4d_stage5.py"), "b4d6_stage5")
B4 = S5.B4

a, aL, aR, e, eL, eR = sp.symbols("a a_L a_R e e_L e_R", real=True)
pr, pq = sp.symbols("p_r p_q", real=True)
Q = sp.Symbol("Q", nonnegative=True)


# ------------------------------------------------------------------------------------------------ J1 the junction
def gauss():
    """K^a_b = a delta + diag(p_t, p_r, p_q, p_q), p_t = -p_r - 2 p_q: K^2 - K.K against 12 a^2 - Pi.Pi."""
    pt = -pr - 2 * pq
    K = [a + pt, a + pr, a + pq, a + pq]
    lhs = sp.expand(sum(K)**2 - sum(k**2 for k in K))
    PiPi = pt**2 + pr**2 + 2 * pq**2
    return sp.simplify(lhs - (12 * a**2 - PiPi)), PiPi


def a_on_side(e_side):
    """The two roots of 12 a^2 - Q = 12 e^2 (Q = Pi.Pi, shared by both sides since Pi_L = -Pi_R)."""
    return sp.solve(sp.Eq(12 * a**2 - Q, 12 * e_side**2), a)


def sigma_over_rs(aL_, aR_, e_=e):
    """sigma = -3 (a_L + a_R)/kappa^2, lambda_RS = 6 e/kappa^2."""
    return sp.simplify(-(aL_ + aR_) / (2 * e_))


def allowed():
    """sigma/lambda_RS over the four sign choices, same ell both sides (e > 0)."""
    ep = sp.Symbol("e", positive=True)
    roots = sp.solve(sp.Eq(12 * a**2 - Q, 12 * ep**2), a)
    return ep, sorted({sp.simplify(sigma_over_rs(x, y, ep)) for x in roots for y in roots}, key=str)


def attainable(target):
    """Is sigma/lambda_RS = target reachable with Q >= 0 (same ell)?"""
    ep, vals = allowed()
    sols = []
    for v in vals:
        if v == target:
            sols.append(("any Q", None))
            continue
        if v.is_number:
            continue
        for q in sp.solve(sp.Eq(v, target), Q):
            if q.is_real and q >= 0:
                sols.append((v, q))
    return sols


# ------------------------------------------------------------------------------------------------ J4 the bounding plane
def bound_exact(e_neg, rc="3", N=6):
    """rho + p_r at a closing plane at y = d on the negative side, as an exact series in d: its d and d^2 coefficients
    against R4_kk and -3 R4_kk/ell (e_neg < 0)."""
    d = sp.Symbol("d")
    S = B4.series(rc, N, e_neg)
    A = sum(sp.Rational(c.numerator, c.denominator) * d**k for k, c in enumerate(S["A"][0]))
    B = sum(sp.Rational(c.numerator, c.denominator) * d**k for k, c in enumerate(S["B"][0]))
    ser = sp.series(-sp.diff(A, d) / (2 * A) + sp.diff(B, d) / (2 * B), d, 0, 3).removeO()
    r = sp.Rational(rc)
    R4 = -2 * (r - 2) / (r**2 * (2 * r - 3) ** 2)
    ee = sp.Rational(e_neg.numerator, e_neg.denominator)
    return ser.coeff(d, 0), sp.simplify(ser.coeff(d, 1) - R4), sp.simplify(ser.coeff(d, 2) - 3 * ee * R4), R4


def bound_numeric(e_neg, rc, N=ORDER):
    """rho + p_r and the tension rho (units 2/kappa^2) at a closing plane at y = d, raw Padé of the warp-divided
    series at three orders (no doublet removal: here the near pole-zero pairs belong to the function -- the raw Padé
    equals the partial sum to 12 digits at small y, its verifier's check), and the linear-order closed form."""
    mp.mp.dps = 40
    W = S5.warped(B4.series(rc, N, e_neg), e_neg, N)
    ee = mp.mpf(e_neg.numerator) / e_neg.denominator
    ell = -1 / ee
    r = sp.Rational(rc)
    R4 = float(-2 * (r - 2) / (r**2 * (2 * r - 3) ** 2))
    out = {"pade": [], "tension": [], "linear": [float(linear_bound(R4, float(ell), d)) for d in DS]}
    for o in S5.orders(N):
        F = {X: B4.pade(W[X][0], *o) for X in "ABC"}

        def ev(X, t):
            pp, qq = F[X]
            v = (mp.polyval([mp.mpf(c.numerator) / c.denominator for c in reversed(pp)], t)
                 / mp.polyval([mp.mpf(c.numerator) / c.denominator for c in reversed(qq)], t))
            return mp.exp(-2 * ee * t) * v
        row, ten = [], []
        for d in DS:
            dd = mp.mpf(d)
            L = {X: mp.diff(lambda t, X=X: ev(X, t), dd) / ev(X, dd) for X in "ABC"}
            Kt, Kr, Kq = (-L[X] / 2 for X in "ABC")
            row.append(float(-L["A"] / 2 + L["B"] / 2))
            ten.append(float(Kt - (Kt + Kr + 2 * Kq)))
        out["pade"].append(row)
        out["tension"].append(ten)
    return out


def linear_bound(R4kk, ell, d):
    """Linear order in the 4D curvature: on the pure-trace growing background K = +(1/ell) delta, the anisotropy obeys
    D' = R4_kk e^(-2y/ell) - (4/ell) D, D(0) = 0, so rho + p_r = (R4_kk ell/2)(e^(-2d/ell) - e^(-4d/ell)) -- negative
    for every d > 0, peaked at d = (ln 2/2) ell; its expansion is R4_kk (d - 3 d^2/ell) (derived by stage 6's verifier;
    the expansion is checked against the exact series)."""
    return R4kk * ell / 2 * (math.exp(-2 * d / ell) - math.exp(-4 * d / ell))


def linear_ode_check():
    """The closed form solves D' = R e^(-2y/l) - (4/l) D, D(0) = 0, and expands to R (d - 3 d^2/l)."""
    R, l, yv = sp.symbols("R l y", real=True)
    D = R * l / 2 * (sp.exp(-2 * yv / l) - sp.exp(-4 * yv / l))
    ode = sp.simplify(sp.diff(D, yv) - (R * sp.exp(-2 * yv / l) - 4 / l * D))
    ser = sp.series(D, yv, 0, 3).removeO()
    return ode, sp.simplify(D.subs(yv, 0)), sp.simplify(ser - R * (yv - 3 * yv**2 / l))


def j3_two_ell():
    """138: a mirrored sheet whose own ell_2 = 3 ell, warp growing on both sides, Pi = 0: sigma = -6/(kappa^2 ell_2)
    against lambda_RS(ell) = 6/(kappa^2 ell)."""
    l = sp.Symbol("ell", positive=True)
    l2 = 3 * l
    return sp.simplify((-3 * (1 / l2 + 1 / l2)) / (6 / l))


def j6():
    """STRUCTURAL: sigma = -3 (a_L + a_R)/kappa^2 two-sided, -3 a/kappa^2 one-sided, for any ell on any side; so sigma > 0
    needs some a < 0.  Checked by exhausting signs on a grid of (a_L, a_R)."""
    grid = [x / 4 for x in range(-8, 9)]
    two = all(not (-(aL_ + aR_) > 0) or min(aL_, aR_) < 0 for aL_ in grid for aR_ in grid)
    one = all(not (-a_ > 0) or a_ < 0 for a_ in grid)
    return two and one


def j5():
    """Each universe its own ell (138): the growing root on each side, a = +sqrt(e_side^2 + Q/12), and the tension
    -(a_L + a_R)/2 in units of 6/kappa^2 -- negative for every e_L, e_R > 0 and Q >= 0."""
    eLp, eRp = sp.symbols("e_L e_R", positive=True)
    grow = lambda es: max(sp.solve(sp.Eq(12 * a**2 - Q, 12 * es**2), a), key=lambda x: x.subs({Q: 1, es: 1}))
    tension = sp.simplify(-(grow(eLp) + grow(eRp)) / 2)
    return tension, tension.is_negative


def compute():
    g, PiPi = gauss()
    ep, vals = allowed()
    return {"gauss": g, "allowed": vals, "e": ep,
            "plus1": attainable(sp.Integer(1)), "minus1": attainable(sp.Integer(-1)),
            "minus_third": attainable(sp.Rational(-1, 3)), "plus_four_thirds": attainable(sp.Rational(4, 3)),
            "rs": sigma_over_rs(-e, -e), "two_ell": j3_two_ell(), "j5": j5(), "j6": j6(),
            "ode": linear_ode_check(),
            "exact": {en: bound_exact(en) for en in (Fr(-1, 2), Fr(-1), Fr(-2))},
            "num": {(en, rc): bound_numeric(en, rc) for en in (Fr(-1, 2), Fr(-1)) for rc in ("43/20", "3")}}


def report(d):
    print("b4d_stage6.py -- B4d stage 6: the two planes together\n")
    print("J1 (one ell, diagonal K) Gauss: K^2 - K.K - (12 a^2 - Pi.Pi) = %s; sigma/lambda_RS: %s" % (
        d["gauss"], d["allowed"]))
    print("   control: Randall-Sundrum (a = -1/ell both sides): sigma/lambda_RS = %s" % d["rs"])
    print("J2 +1 (the coincident pair, one ell): %s" % d["plus1"])
    print("J3 one ell: -1/3 %s; -1 %s; +4/3 %s" % (d["minus_third"] or "not attainable", d["minus1"],
                                                     d["plus_four_thirds"]))
    print("   each its own ell (138): a mirrored sheet with ell_2 = 3 ell, growing both sides: sigma/lambda_RS(ell) = %s"
          % d["two_ell"])
    print("J4 bounding plane, exact at r = 3m: (d^0, d^1 - R4_kk, d^2 - 3 e R4_kk):")
    for en, w in d["exact"].items():
        print("   ell = %s: %s, %s, %s (R4_kk = %s)" % (str(-1 / en), *w))
    print("   linear form: ODE residual %s, D(0) = %s, expansion residual %s" % d["ode"])
    for (en, rc), v in d["num"].items():
        print("   ell = %s, r = %s, d = %s:" % (str(-1 / en), rc, DS))
        print("      Padé  %s" % " ".join("/".join("%.2e" % row[k] for row in v["pade"]) for k in range(len(DS))))
        print("      linear %s; tension at d = 4m %s (3/ell = %.2f)" % (
            " ".join("%.2e" % x for x in v["linear"]), "/".join("%.4f" % t[-1] for t in v["tension"]),
            3 * abs(float(en))))
    print("J5 both sides growing, each its own ell: tension (units 6/kappa^2) = %s, negative: %s" % d["j5"])
    print("J6 every positive-tension plane has a decaying side (one- or two-sided, any ell): %s" % d["j6"])


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    ep = d["e"]
    chk("J1: with R4 = 0 the Gauss constraint on each side is 12 a^2 - Pi.Pi = 12/ell^2 (exact, an identity of the "
        "parametrisation); control: Randall-Sundrum's plane (Pi = 0, a = -1/ell both sides) has sigma = +lambda_RS",
        d["gauss"] == 0 and d["rs"] == 1)
    nz = [v for v in d["allowed"] if v != 0]
    chk("J1 (one ell, diagonal K): a matter-free plane carrying eq. (17) has sigma/lambda_RS = 0 or "
        "+-sqrt(1 + Pi.Pi ell^2/12) -- never strictly between 0 and 1 in size",
        len(d["allowed"]) == 3 and 0 in d["allowed"] and len(nz) == 2
        and all(sp.simplify(v**2 - (1 + Q / (12 * ep**2))) == 0 for v in nz))
    chk("J2 (one ell): +1 lambda_RS forces Pi.Pi = 0 and a_L = a_R = -1/ell -- the warp decays on both sides",
        len(d["plus1"]) >= 1 and all(q == 0 for _, q in d["plus1"]))
    chk("J3: with one ell, -1/3 is not attainable and -1 needs Pi = 0; with each universe's own ell (138), a mirrored "
        "sheet with ell_2 = 3 ell growing on both sides carries exactly -1/3 lambda_RS(ell) at Pi = 0",
        d["minus_third"] == [] and all(q == 0 for _, q in d["minus1"]) and d["two_ell"] == sp.Rational(-1, 3))
    chk("J4 (exact, r = 3m): a mirrored plane bounding the slab d above the negative plane needs rho + p_r = "
        "R4_kk (d - 3 d^2/ell) + O(d^3), R4_kk < 0, at ell = 2m, m, m/2",
        all(w[0] == 0 and w[1] == 0 and w[2] == 0 and w[3] < 0 for w in d["exact"].values()))
    ode, d0, ex = d["ode"]
    lin_neg = all(x < 0 for v in d["num"].values() for x in v["linear"])
    chk("J4 (linear order, derived): rho + p_r = (R4_kk ell/2)(e^(-2d/ell) - e^(-4d/ell)) solves the background "
        "equation, expands to R4_kk (d - 3d^2/ell), and is negative at every d", ode == 0 and d0 == 0 and ex == 0
        and lin_neg)
    pade_neg = all(x < 0 for v in d["num"].values() for row in v["pade"][:2] for x in row)
    agree = all(abs(v["pade"][1][k] / v["linear"][k] - 1) < 0.5 for v in d["num"].values() for k in range(len(DS)))
    tens = all(abs(v["tension"][1][-1] / (3 * abs(float(en))) - 1) < 0.02 for (en, _), v in d["num"].items())
    chk("J4 (computed): raw Padé gives rho + p_r < 0 at r = 2.15m and 3m for d = 0.1-4m at ell = 2m and m (two orders; "
        "the third agrees except at ell = m, r = 2.15m, d = 4m, where it breaks down), within 50% of the linear form; the bounding plane's tension tends to +lambda_RS", pade_neg and agree and tens)
    chk("J5 (STRUCTURAL): with each universe's own ell and any anisotropy, a plane whose trace part grows on both sides "
        "has negative tension", d["j5"][1] is True)
    chk("J6 (STRUCTURAL): sigma > 0 needs a decaying trace part on some side, one- or two-sided, any ell", d["j6"])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
