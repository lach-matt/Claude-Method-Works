#!/usr/bin/env python3
"""b4d_stage6.py -- Warp Theorem lemma B4d, stage 6: the two planes together (M-RULINGS item 165).  Computed and
deduced; not verified; not seated.

M's words (verbatim in the rulings file): item 165 "Of course. Continue" (on the board's next step: the negative-tension
plane and a positive-tension plane together, as one object); item 139 (1) "yes" (position 2's plane negative, a quarter
of ours in magnitude, ours positive -- multiplane.py M4's +4/3 and -1/3 of the one-plane value); item 127 (1) "yes" (the
planes coincide, the extra dimension included); item 141 (the planes are static); items 117/120 ("the NEC only ever
appears to break, but never does"); clause (B) (the plane carries no matter); item 138 (the bulk is multi-universal;
each universe under its own laws).

Stage 5 (b4d_stage5.py, verified once) found: with eq. (17) on a plane the bulk is singular within 8-16 clocks on the
side where the warp decays (positive tension, both sides), and regular on the evidence on the side where it grows
(negative tension, F6).  This stage asks which of those the rulings allow.

  J1 WHAT A MATTER-FREE PLANE CARRYING EQ. (17) CAN BE (computed, exact).  On each side the extrinsic curvature is
     K^a_b = a delta^a_b + Pi^a_b, Pi traceless (diagonal, static).  Eq. (17) has R4 = 0, so the Gauss constraint on
     each side is K^2 - K_ab K^ab = 12/ell^2, i.e. 12 a^2 - Pi.Pi = 12/ell^2 (computed): |a| >= 1/ell, with equality only
     when Pi = 0.  No matter on the plane (clause (B)) means the jump is pure tension: Pi_L = -Pi_R.  The tension is
     sigma = -3 (a_L + a_R)/kappa^2, so in units of the one-plane value lambda_RS = 6/(kappa^2 ell):
        sigma/lambda_RS in {0} or {+-s : s = sqrt(1 + Pi.Pi ell^2/12) >= 1}   (same ell both sides).
     Control: Pi = 0, a = -1/ell on both sides is Randall-Sundrum's plane, sigma = +lambda_RS.  The sign of a is which
     side: a < 0 the warp decays away from the plane (stage 5 F2, singular), a > 0 it grows (F6, regular on the evidence).
  J2 THE COINCIDENT PAIR IS A POSITIVE PLANE, AND BOTH ITS SIDES DECAY (computed).  By 127 the two planes are at one
     place, and the junction sees only their summed tension: +4/3 - 1/3 = +1 lambda_RS (139; b5_positive.py B5a).  By J1,
     +1 forces Pi.Pi = 0 and a_L = a_R = -1/ell: on both sides the decaying bulk -- stage 5 F2's singular surface within
     8-16 clocks.
  J3 NEITHER SHEET STANDS ALONE AT ITS OWN TENSION AS THE REGULAR SIDE (computed).  Position 2's sheet alone, -1/3, is
     not in J1's set -- a matter-free plane with eq. (17) cannot carry it.  The regular configuration of stage 5 F6 (both
     sides growing, Pi = 0) is exactly sigma = -1 lambda_RS, three times 139's.
  J4 SEPARATING THE SHEETS COSTS NEC-BREAKING MATTER (computed; exact at small separation).  To keep the growing side
     regular, put eq. (17) on a negative plane at y = 0 and bound the slab with a positive plane at y = d (Randall-
     Sundrum I's orientation).  That plane must carry rho + p_r = -A_y/(2A) + B_y/(2B) at y = d (b4d_stage1.py D3's
     junction): exactly R4_kk (d - 3 d^2/ell) + O(d^3), R4_kk < 0 (rational at r = 3m; stage 5 F5 under y -> -y,
     e -> -e); and numerically negative at r = 2.15m and 3m for d from 0.1m to 4m at ell = 2m and m, two Padé orders
     agreeing in sign, falling off with d; its tension tends to +lambda_RS.  So the bounding plane carries real matter
     breaking the NEC (117/120), however far it is put; and the separation is against 127, and is a modulus -- the radion
     b5_positive.py B5c rules out only because the separation is zero (standard, not READ).
  J5 WITH EACH UNIVERSE'S OWN ell (138) THE SIGN STAYS (computed, STRUCTURAL).  With ell_L != ell_R, sigma = -3 (a_L +
     a_R)/kappa^2 still, so if the trace part grows on every side (a_L, a_R > 0) the tension is negative, whatever the
     radii and the anisotropy.  139's positive composite therefore has a decaying trace part on some side.
  VERDICT (deduced).  On the rulings as they stand the corridor's bulk is not regular through the write: the coincident
     pair (127, 139) is a positive plane whose bulk decays on both sides, and stage 5 F2 makes that bulk singular within
     8-16 clocks; the regular side needs a negative total tension (J1, J5) that 139 does not give, or the sheets apart
     (against 127) with NEC-breaking matter on the bounding plane (against 117/120).  The conjunction: 127, 139, 117/120,
     clause (B) -- M's; eq. (17) on the plane through the write (H-EQ17-ON-PLANE-THROUGH-HOLD), a vacuum bulk, B4b's
     locally analytic class, the column r = 2.15m and the ell tested, and stage 5's -- the board's.  M's inclination 161
     does not hold on it.  Open, each a way it could: (a) anisotropic junction data with each universe's own ell (138):
     J5 forces a decaying trace part somewhere but leaves Pi free, and the regularity of a bulk from Pi != 0 data is not
     computed; (b) a non-vacuum bulk (158 (4); b5_positive.py B5b's smooth wall is one -- it has a bulk scalar); (c) the
     plane's geometry not eq. (17) while the README passes; (d) a bulk outside the analytic class.

Imports lemmas/b4d_stage5.py (and through it b4_static.py) by path.  Needs python-flint, sympy, numpy, mpmath.
python3 b4d_stage6.py [--selftest]   (selftest about 2 min)
"""
import contextlib
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
    """rho + p_r and the tension rho (units 2/kappa^2) at a closing plane at y = d, two Padé orders."""
    mp.mp.dps = 40
    W = S5.warped(B4.series(rc, N, e_neg), e_neg, N)
    ee = mp.mpf(e_neg.numerator) / e_neg.denominator
    out = []
    for o in S5.orders(N)[:2]:
        F = {X: S5._clean(*S5._approx(W[X][0], o)) for X in "ABC"}

        def ev(X, t):
            pp, qq, dz = F[X]
            v = mp.polyval(pp, t) / mp.polyval(qq, t)
            for pole, zero in dz:
                v *= (t - pole) / (t - zero)
            return mp.exp(-2 * ee * t) * mp.re(v)
        row = []
        for d in DS:
            dd = mp.mpf(d)
            L = {X: mp.diff(lambda t, X=X: ev(X, t), dd) / ev(X, dd) for X in "ABC"}
            Kt, Kr, Kq = (-L[X] / 2 for X in "ABC")
            row.append((float(-L["A"] / 2 + L["B"] / 2), float(Kt - (Kt + Kr + 2 * Kq))))
        out.append(row)
    return out


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
            "rs": sigma_over_rs(-e, -e),
            "j5": j5(),
            "exact": {en: bound_exact(en) for en in (Fr(-1, 2), Fr(-1), Fr(-2))},
            "num": {(en, rc): bound_numeric(en, rc) for en in (Fr(-1, 2), Fr(-1)) for rc in ("43/20", "3")}}


def report(d):
    print("b4d_stage6.py -- B4d stage 6: the two planes together\n")
    print("J1 Gauss on each side: K^2 - K.K - (12 a^2 - Pi.Pi) = %s; sigma/lambda_RS over the sign choices: %s" % (
        d["gauss"], d["allowed"]))
    print("   control: Randall-Sundrum (a = -1/ell both sides): sigma/lambda_RS = %s" % d["rs"])
    print("J2 +1 (127's coincident pair, 139): %s" % d["plus1"])
    print("J3 -1/3 (position 2 alone): %s; -1 (stage 5 F6): %s; +4/3 (ours alone): %s" % (
        d["minus_third"] or "not attainable", d["minus1"], d["plus_four_thirds"]))
    print("J4 bounding plane, exact at r = 3m: (d^0, d^1 - R4_kk, d^2 - 3 e R4_kk):")
    for en, w in d["exact"].items():
        print("   ell = %s: %s, %s, %s (R4_kk = %s)" % (str(-1 / en), *w))
    for (en, rc), rows in d["num"].items():
        print("   ell = %s, r = %s: rho + p_r at d = %s: %s; tension rho -> %s (3/ell = %.2f)" % (
            str(-1 / en), rc, DS, " ".join("%.2e/%.2e" % (x[0], y[0]) for x, y in zip(*rows)),
            "/".join("%.4f" % r[-1][1] for r in rows), 3 * abs(float(en))))
    print("J5 both sides growing, each its own ell: tension (units 6/kappa^2) = %s, negative: %s" % d["j5"])


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    ep = d["e"]
    chk("J1: with R4 = 0 the Gauss constraint on each side is 12 a^2 - Pi.Pi = 12/ell^2 (exact); control: Randall-"
        "Sundrum's plane (Pi = 0, a = -1/ell both sides) has sigma = +lambda_RS", d["gauss"] == 0 and d["rs"] == 1)
    nz = [v for v in d["allowed"] if v != 0]
    chk("J1: a matter-free plane carrying eq. (17) has sigma/lambda_RS = 0 or +-sqrt(1 + Pi.Pi ell^2/12) -- never strictly "
        "between 0 and 1 in size", len(d["allowed"]) == 3 and 0 in d["allowed"] and len(nz) == 2
        and all(sp.simplify(v**2 - (1 + Q / (12 * ep**2))) == 0 for v in nz))
    chk("J2: +1 lambda_RS (127's coincident pair, 139's +4/3 - 1/3) forces Pi.Pi = 0 and a_L = a_R = -1/ell: the bulk "
        "decays on both sides (stage 5 F2: singular within 8-16 clocks)",
        len(d["plus1"]) >= 1 and all(q == 0 for _, q in d["plus1"]))
    chk("J3: -1/3 (position 2's sheet alone) is not attainable by a matter-free plane carrying eq. (17); -1 (stage 5 F6's "
        "regular plane) needs Pi = 0", d["minus_third"] == [] and all(q == 0 for _, q in d["minus1"]))
    chk("J4 (exact, r = 3m): at a bounding plane d above the negative plane rho + p_r = R4_kk (d - 3 d^2/ell) + O(d^3), "
        "R4_kk < 0, at ell = 2m, m, m/2",
        all(w[0] == 0 and w[1] == 0 and w[2] == 0 and w[3] < 0 for w in d["exact"].values()))
    num_neg = all(x[0] < 0 for rows in d["num"].values() for row in rows for x in row)
    tens = all(abs(rows[0][-1][1] / (3 * abs(float(en))) - 1) < 0.02 for (en, _), rows in d["num"].items())
    chk("J4: rho + p_r < 0 at r = 2.15m and 3m for every d from 0.1m to 4m at ell = 2m and m, both Padé orders; the "
        "bounding plane's tension tends to +lambda_RS (within 2% at d = 4m)", num_neg and tens)
    chk("J5 (STRUCTURAL): with each universe's own ell and any anisotropy, a plane whose trace part grows on both sides "
        "has tension -(sqrt(1/ell_L^2 + Pi.Pi/12) + sqrt(1/ell_R^2 + Pi.Pi/12))/2 < 0", d["j5"][1] is True)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
