#!/usr/bin/env python3
"""b4d_stage7.py -- Warp Theorem lemma B4d, stage 7: the corridor across both planes (M-RULINGS item 166).  Computed and
deduced; not verified; not seated.

M's words (verbatim in the rulings file): item 166 "Both planes at once" (the corridor is one object across both planes,
ours and position 2's, the bulk between them its throat); item 139 (1) "yes" (ours positive, +4/3; position 2's
negative, -1/3, in units of the one-plane value); item 152 (1) "two separate positions connected by/reached through a
dimension"; item 127 (1) "yes" (the planes coincide); item 138 (each universe its own laws); clause (B) (the planes free
of matter).

The configuration: eq. (17) on our plane (y = 0); the slab between the planes, of AdS radius ell_s, the throat 152
describes; position 2's plane at y = d; beyond each plane its own universe's bulk -- ours beyond y = 0 (ell_1), position
2's beyond y = d (ell_2).  Stage 5 (verified): with pure-trace data, a side whose warp decays is singular within 8-16
clocks (F2), a side whose warp grows is regular on the evidence (F6).  Stage 6 (verified): the tension is
sigma = -3 (a_L + a_R)/kappa^2 with a each side's trace part (a < 0 decaying), K diagonal.

  K1 THE SLAB'S TRACE PART AT POSITION 2'S PLANE (computed, exact).  Evolving eq. (17)'s data across the slab,
        a_s(d, r) = 1/ell_s + (R_ab R^ab/12) d^3 (1 + 5 d/ell_s) + O(d^5),
     R_ab the Ricci tensor of eq. (17) (computed: R = 0, R_ab R^ab = 2/729 at r = 3m), exact at r = 3m for ell_s = 2m, m,
     m/2 and matched at 2.15m and 5m.  It depends on r, and R_ab R^ab >= 0 (a sum of squares, K and R diagonal).
  K2 A FLAT POSITION-2 PLANE CANNOT CARRY 139'S TENSION WITHOUT MATTER (computed, exact).  Both sides of position 2's
     plane share its induced metric, so the Gauss constraint on each (K^2 - K.K = 12/ell^2 + R4, its stage-6 verifier's
     sign) gives, with Pi_beyond = -Pi_slab (no matter), pointwise a_2^2 = a_s^2 + 1/ell_2^2 - 1/ell_s^2.  The tension
     -3 (a_s + a_2)/kappa^2 then changes with a_s unless ell_2 = ell_s and a_2 = -a_s, which is zero tension.  Since
     a_s depends on r at every d > 0 (K1), a flat position-2 plane at 139's -1/3 must carry matter, or curve.
  K3 THE TWO OUTER BULKS CANNOT BOTH GROW (computed, exact identity).  With the planes' tensions constant,
        a_1 + a_2 = -kappa^2 (sigma_1 + sigma_2)/3 - (a_s(d) - 1/ell_s),
     a_1 ours beyond y = 0, a_2 position 2's beyond y = d.  139's total is +1 lambda_RS and a_s - 1/ell_s >= 0 (K1), so
     a_1 + a_2 < 0 at every d: one outer bulk at least decays.  At d = 0 (127 read as one place) it is stage 6 J2.
     Which one: a_1 = 1/ell_s - (8/3)/ell (139's +4/3, Pi_1 = 0), so ours grows iff ell_s < 3 ell/8; then ours grows
     and position 2's decays, with anisotropic data Pi_2 = -Pi_slab(d) whose bulk is not computed; with ell_s > 3 ell/8
     ours decays (Pi_1 = 0: stage 5 F2, singular).
  VERDICT (deduced).  The corridor across both planes, with flat matter-free planes at 139's tensions, cannot be
     regular on every side: the outer bulks' trace parts sum negative at every separation (K3), and our side, if it is
     the one that decays, is singular (F2).  The only arrangement left has our outer bulk growing (ell_s < 3 ell/8),
     position 2's plane curved (K2 forbids it flat), and position 2's outer bulk decaying in its trace but built from
     anisotropic data -- whose regularity stage 5's evidence does not cover.  That bulk, and the curved plane that
     carries it, are B4d's next computation.  Conjunction: M's 139, 152/127, 138, clause (B), 166; the board's diagonal K,
     a negative cosmological constant on every side, a vacuum bulk, eq. (17) on our plane, B4b's analytic class, and
     stage 5's Pi = 0 link between decay and singularity.

Imports lemmas/b4_static.py by path.  Needs python-flint, sympy.  python3 b4d_stage7.py [--selftest]  (about 1 min)
"""
import contextlib
import importlib.util
import io
import os
import sys
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)


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


B4 = _load(os.path.join(HERE, "b4_static.py"), "b4d7_b4static")
d = sp.Symbol("d")


def ricci_squared(rv):
    """Eq. (17): F = 1 - 2/r, H = (1 - 2/r)^2/(1 - 3/(2r)); R and R_ab R^ab (diagonal) at r = rv."""
    t, r, th, ph = sp.symbols("t r theta phi")
    F = 1 - 2 / r
    H = (1 - 2 / r) ** 2 / (1 - sp.Rational(3, 2) / r)
    g = sp.diag(-F, 1 / H, r**2, r**2 * sp.sin(th) ** 2)
    X = [t, r, th, ph]
    gi = g.inv()
    Gam = [[[sum(gi[a, k] * (sp.diff(g[k, b], X[c]) + sp.diff(g[k, c], X[b]) - sp.diff(g[b, c], X[k]))
                 for k in range(4)) / 2 for c in range(4)] for b in range(4)] for a in range(4)]

    def ric(b, c):
        return sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                               + sum(Gam[a][a][k] * Gam[k][b][c] - Gam[a][c][k] * Gam[k][b][a] for k in range(4))
                               for a in range(4)))
    mixed = [sp.simplify(gi[i, i] * ric(i, i)) for i in range(4)]
    Rs = sp.simplify(sum(mixed))
    RR = sp.simplify(sum(m**2 for m in mixed))
    return Rs, RR.subs(r, rv)


def slab_trace(e, rc, N=10):
    """a_s(d): the slab's trace part at position 2's plane (normal into the slab, -d_y): K^X = -(1/2) X_y/X, averaged
    over t, r, theta, theta; as a series in d."""
    S = B4.series(rc, N, e)
    X = {k: sum(sp.Rational(c.numerator, c.denominator) * d**j for j, c in enumerate(S[k][0])) for k in "ABC"}
    L = {k: sp.series(sp.diff(X[k], d) / X[k], d, 0, 5).removeO() for k in "ABC"}
    return sp.expand(-(L["A"] + L["B"] + 2 * L["C"]) / 8)


def junction():
    """Position 2's plane: Gauss on both sides with one induced R4 and Pi_beyond = -Pi_slab; the tension's slope in a_s."""
    a_s, l2, ls = sp.symbols("a_s ell_2 ell_s", positive=True)              # a_s ~ 1/ell_s > 0 (K1)
    a2, R4, PP = sp.symbols("a_2 R4 PiPi", real=True)
    slab = sp.Eq(12 * a_s**2 - PP, 12 / ls**2 + R4)
    beyond = sp.Eq(12 * a2**2 - PP, 12 / l2**2 + R4)
    diff = sp.simplify((beyond.lhs - beyond.rhs) - (slab.lhs - slab.rhs))           # 12 a_2^2 - 12 a_s^2 - 12/l2^2 + 12/ls^2
    roots = sp.solve(sp.Eq(diff, 0), a2)
    slopes = [sp.simplify(sp.diff(-(a_s + rt), a_s)) for rt in roots]                 # d sigma/d a_s, units 3/kappa^2
    return diff, roots, slopes, (a_s, l2, ls)


def outer_sum():
    """a_1 + a_2 from the two planes' tensions: sigma_1 = -3 (a_1 + a_slab1)/k^2, a_slab1 = -1/ell_s (pure-trace data
    at our plane, into the slab); sigma_2 = -3 (a_s + a_2)/k^2."""
    a1, a2, a_s, s1, s2, ls, k2 = sp.symbols("a_1 a_2 a_s sigma_1 sigma_2 ell_s kappa2", real=True)
    sol1 = sp.solve(sp.Eq(s1, -3 * (a1 - 1 / ls) / k2), a1)[0]
    sol2 = sp.solve(sp.Eq(s2, -3 * (a_s + a2) / k2), a2)[0]
    return sp.simplify(sol1 + sol2 - (-k2 * (s1 + s2) / 3 - (a_s - 1 / ls))), sol1


def compute():
    Rs, RR3 = ricci_squared(3)
    _, RR215 = ricci_squared(sp.Rational(43, 20))
    _, RR5 = ricci_squared(5)
    traces = {(e, rc): slab_trace(e, rc) for e in (Fr(1, 2), Fr(1), Fr(2)) for rc in ("3",)}
    others = {rc: slab_trace(Fr(1), rc) for rc in ("43/20", "5")}
    j = junction()
    o = outer_sum()
    return {"R": Rs, "RR3": RR3, "RR215": RR215, "RR5": RR5, "traces": traces, "others": others, "junction": j,
            "outer": o}


def _expected(e, RR):
    ee = sp.Rational(e.numerator, e.denominator)
    return ee + RR / 12 * d**3 + 5 * ee * RR / 12 * d**4


def report(dd):
    print("b4d_stage7.py -- B4d stage 7: the corridor across both planes\n")
    print("K1 eq. (17): R = %s; R_ab R^ab = %s at 3m, %.4g at 2.15m, %.4g at 5m" % (
        dd["R"], dd["RR3"], float(dd["RR215"]), float(dd["RR5"])))
    for (e, rc), a_s in dd["traces"].items():
        print("   ell_s = %s, r = %sm: a_s(d) = %s" % (str(1 / e), rc, a_s))
    for rc, a_s in dd["others"].items():
        print("   ell_s = m, r = %sm: a_s(d) = %s" % (rc, sp.N(a_s, 6)))
    diff, roots, slopes, _ = dd["junction"]
    print("K2 Gauss beyond minus slab: %s = 0; a_2 = %s; d sigma_2/d a_s (units 3/kappa^2): %s" % (diff, roots, slopes))
    print("K3 a_1 + a_2 - [-kappa^2 (sigma_1 + sigma_2)/3 - (a_s - 1/ell_s)] = %s; a_1 = %s" % dd["outer"])


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    dd = compute()
    chk("K1: eq. (17) has R = 0 and R_ab R^ab = 2/729 at r = 3m (computed from its metric)",
        dd["R"] == 0 and dd["RR3"] == sp.Rational(2, 729))
    chk("K1 (exact, r = 3m): the slab's trace part at position 2's plane is a_s = 1/ell_s + (R_ab R^ab/12) d^3 "
        "(1 + 5 d/ell_s) + O(d^5) at ell_s = 2m, m, m/2",
        all(sp.simplify(a_s - _expected(e, dd["RR3"])) == 0 for (e, _), a_s in dd["traces"].items()))
    chk("K1: the same form at r = 2.15m and 5m (to 1e-6), so a_s depends on r through R_ab R^ab -- control: the d^3 "
        "coefficients at 2.15m, 3m, 5m differ",
        all(abs(float(a_s.coeff(d, 3) - dd[k] / 12)) < 1e-6 and abs(float(a_s.coeff(d, 4) - 5 * dd[k] / 12)) < 1e-6
            for (rc, a_s), k in zip(dd["others"].items(), ("RR215", "RR5")))
        and len({round(float(v), 9) for v in (dd["RR215"], dd["RR3"], dd["RR5"])}) == 3)
    diff, roots, slopes, (a_s, l2, ls) = dd["junction"]
    zero_slope = [sp.solve(sp.Eq(sl, 0), a_s) for sl in slopes]
    chk("K2: across position 2's plane a_2^2 = a_s^2 + 1/ell_2^2 - 1/ell_s^2 (Gauss both sides, one induced metric), and "
        "the tension's slope in a_s vanishes nowhere unless ell_2 = ell_s (then a_2 = -a_s, zero tension)",
        len(roots) == 2 and all(sp.simplify(rt**2 - (a_s**2 + 1 / l2**2 - 1 / ls**2)) == 0 for rt in roots)
        and all(z == [] for z in zero_slope)
        and any(sp.simplify(sl.subs(l2, ls)) == 0 for sl in slopes))
    chk("K3 (exact identity): a_1 + a_2 = -kappa^2 (sigma_1 + sigma_2)/3 - (a_s - 1/ell_s); with 139's positive total and "
        "a_s >= 1/ell_s (K1) the two outer trace parts sum negative at every d", dd["outer"][0] == 0)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
