#!/usr/bin/env python3
"""b4d_stage7.py -- Warp Theorem lemma B4d, stage 7: the corridor across both planes (M-RULINGS item 166).  Computed and
deduced; verified once (findings applied, B4D-STAGE7.md History); not seated.  First headed "... not verified; not
seated" -- and first leaving one arrangement open (ours growing, position 2's plane curved), which its verifier showed
rests on an undefined unit and leaves out that the slab is itself stage 5's singular case.

M's words (verbatim in the rulings file): item 166 "Both planes at once" (the corridor is one object across both planes,
the bulk between them its throat); item 139 (1) "yes" (ours positive, +4/3; position 2's negative, -1/3 -- multiplane.py
M4's figures); item 152 (1) "two separate positions connected by/reached through a dimension"; item 127 (1) "yes"; item
138 (each universe its own laws); item 141 (the planes static); clause (B) (the planes free of matter).

The arrangement: eq. (17) on one plane (ours at y = 0; K4 shows the placement does not matter at small d); the slab
between the planes, AdS radius ell_s, 152's dimension and the throat; position 2's plane at y = d; beyond each plane
its own universe's bulk, ell_1 ours, ell_2 position 2's.  "Parallel" means the surface y = d (eq. (17)'s slices are not
intrinsically flat).  Stage 5 (verified): pure-trace data give a singular bulk within 8-16 clocks where the warp decays
(F2, tested ell = 2m-m/4 on r = 2.15m), a regular one on the evidence where it grows (F6).  Stage 6 (verified):
sigma = -3 (a_L + a_R)/kappa^2, a each side's trace part (a < 0 decaying), K diagonal.

  K1 THE SLAB (computed, exact; deduced bound).  The slab is our plane's decaying side with pure-trace eq. (17) data:
     stage 5 F2's case, singular at y_s(ell_s, r) (about 1.0m at ell_s = m, 0.67m at m/2, 0.43m at m/4, r = 2.15m), so
     every arrangement needs d < y_s at every r.  Below it, the slab's trace part at position 2's plane (normal into the
     slab) is
        a_s(d, r) = 1/ell_s + (R_ab R^ab/12) d^3 (1 + 5 d/ell_s) + O(d^5),
     R_ab eq. (17)'s Ricci tensor (R = 0; R_ab R^ab = 2(3r^2 - 8r + 6)/(r^4 (2r - 3)^4) > 0 for every r, its verifier's
     closed form; 2/729 at 3m), exact at r = 3m for ell_s = 2m, m, m/2 and matched at 2.15m and 5m (ell_s = m).  At every
     d < y_s, a_s >= 1/ell_s (deduced, Raychaudhuri: with b = -a_s, b' = 1/ell_s^2 - b^2 - Pi.Pi/4 and b(0) = -1/ell_s,
     b cannot rise above -1/ell_s since b' = -Pi.Pi/4 <= 0 there -- Pi.Pi >= 0 needs K diagonal), rising without bound
     at y_s.  a_s depends on r for all small d, and generically for every d < y_s.
  K2 NO PARALLEL MATTER-FREE POSITION-2 PLANE EXISTS AT ANY NONZERO TENSION (computed, exact).  Both sides share the
     induced metric, so Gauss on each gives, pointwise, a_2^2 = a_s^2 + 1/ell_2^2 - 1/ell_s^2 (a_2^2 >= 1/ell_2^2, so its
     sign cannot change along the plane).  A pure tension is constant (D_a S^a_b = 0), so a_s + a_2 is constant, which
     with the Gauss relation forces a_s constant -- false (K1) -- unless ell_2 = ell_s and a_2 = -a_s, zero tension.  So
     position 2's plane, at 139's tension, must curve (y = d + f(x)) or carry matter.
  K3 THE OUTER SUM (computed, an exact identity; its sign deduced).  With the planes' tensions constant,
        a_1 + a_2 = -kappa^2 (sigma_1 + sigma_2)/3 - (a_s(d) - 1/ell_s),
     negative for 139's positive total at every d < y_s (K1's bound) -- on the parallel surface.  On a curved plane a_s
     gains embedding terms and the sign is not derived here.
  K4 EVERY SMALL-d BRANCH HAS A DECAYING OUTER BULK (computed, exact arithmetic).  At small d the outer data are nearly
     pure trace (Pi ~ Ric d), so a_1 = +-1/ell_1, a_2 = +-1/ell_2, a_s = 1/ell_s, and the tensions fix the rest.  The
     unit of 139's figures is a choice: multiplane.py M4 normalises to the curvature beyond position 2 (ell_2).
     Enumerated over both units and both counts of position 2's tension (139's -1/3; -1/6, K5):
       unit ell_2, -1/3:  ell_s = 3 ell_2/5, both outer bulks decay (ell_1 = ell_2);
       unit ell_2, -1/6:  ell_s = ell_1 = 3 ell_2/4, both decay -- M4's own geometry (control);
       unit ell_1, -1/3:  ours grows with ell_s = 3 ell_1/11 and position 2's decays (ell_2 = ell_1/3), or both decay;
       unit ell_1, -1/6:  ours grows with ell_s = 3 ell_1/11 and position 2's decays (ell_2 = 3 ell_1/10), or both decay.
     The placement of eq. (17) (ours, position 2's, or both) does not change this system at small d.  So every branch
     has an outer bulk that decays with pure-trace data (ours, stage 5 F2: singular) or with an O(d) perturbation of
     them (position 2's: F2 slightly perturbed -- singular by continuity, a reading, H-F2-STABLE).
  K5 139'S -1/3 COUNTS POSITION 2'S PLANE TWICE (deduced; recorded, not repaired).  PRZ's jump condition (hep-th/0004028
     p.3, its verifier's reading) gives a single sheet 12 M^3 (k_R - k_L); PRZ print 24 M^3 (k_R - k_L), counting both
     images on the covering space, which the "sum to the one-plane value" rule also needs.  Under stage 6's per-plane
     formula M4's geometry gives -1/6 lambda_RS(ell_2), and K4's unit-ell_2 branch with -1/6 reproduces M4 exactly.  The
     stage-6 route J3 then reads ell_2 = 6 ell, not 3 ell.  The "quarter of ours" is a covering-space count.
  VERDICT (deduced).  With the corridor across both planes and eq. (17) on either, at small separation every branch has
     an outer bulk that decays, with data pure trace or nearly so: singular (F2), directly on our side or by continuity
     on position 2's.  Robust: no parallel matter-free position-2 plane exists (K2); our outer side decays unless ell_s <
     3 ell/8 (a_1 = 1/ell_s - 8/(3 ell)); the slab is itself F2's case (d < y_s).  Left open: d close to the slab's own
     singular surface, where a_s deviates by order one (the slab's curvature there is 1e3-1e4 times the black string's,
     stage 5 F2); anisotropic data at the plane carrying eq. (17); curved planes beyond leading order; outer bulks not
     anti-de Sitter (138); the unit of 139 (K4) and its image count (K5), M's.  Conjunction: M's 139, 152/127, 138, 141,
     clause (B), 166; the board's diagonal K, Lambda < 0 on every side, a vacuum bulk, pure-trace data at the plane
     carrying eq. (17), B4b's analytic class, H-F2-STABLE, and stage 5's tested ell range and column.

Imports lemmas/b4_static.py by path.  Needs python-flint, sympy.  python3 b4d_stage7.py [--selftest]  (about 15 s)
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


def ricci_squared_closed():
    """Its verifier's closed form for eq. (17): R_ab R^ab = 2 (3r^2 - 8r + 6)/(r^4 (2r - 3)^4); the quadratic has a
    negative discriminant, so it is positive for every r."""
    r = sp.Symbol("r", positive=True)
    return 2 * (3 * r**2 - 8 * r + 6) / (r**4 * (2 * r - 3) ** 4), sp.discriminant(3 * r**2 - 8 * r + 6, r)


def branches():
    """K4: a_1 = u - 8/(3L), a_2 = -2 s_2/L - u (139's +4/3 and s_2 in units of lambda_RS(L) = 6/(kappa^2 L)), u = 1/ell_s
    > 0; with unit L = ell_1, |a_1| = 1/L; with L = ell_2, |a_2| = 1/L.  L = 1."""
    out = []
    for s2 in (Fr(-1, 3), Fr(-1, 6)):
        for unit in ("ell_1", "ell_2"):
            for sg in (1, -1):
                if unit == "ell_1":
                    a1 = Fr(sg)
                    u = a1 + Fr(8, 3)
                    a2 = -2 * s2 - u
                else:
                    a2 = Fr(sg)
                    u = -2 * s2 - a2
                    a1 = u - Fr(8, 3)
                if u > 0:
                    out.append({"s2": s2, "unit": unit, "ell_s": 1 / u, "a1": a1, "a2": a2})
    return out


def compute():
    Rs, RR3 = ricci_squared(3)
    _, RR215 = ricci_squared(sp.Rational(43, 20))
    _, RR5 = ricci_squared(5)
    traces = {(e, rc): slab_trace(e, rc) for e in (Fr(1, 2), Fr(1), Fr(2)) for rc in ("3",)}
    others = {rc: slab_trace(Fr(1), rc) for rc in ("43/20", "5")}
    j = junction()
    o = outer_sum()
    return {"R": Rs, "RR3": RR3, "RR215": RR215, "RR5": RR5, "traces": traces, "others": others, "junction": j,
            "outer": o, "closed": ricci_squared_closed(), "branches": branches()}


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
    print("K4 small-d branches (units of the chosen ell):")
    for br in dd["branches"]:
        print("   s_2 = %s, unit %s: ell_s = %s; ours a_1 = %s (%s), position 2's a_2 = %s (%s)" % (
            br["s2"], br["unit"], br["ell_s"], br["a1"], "grows" if br["a1"] > 0 else "decays", br["a2"],
            "grows" if br["a2"] > 0 else "decays"))


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
    chk("K3 (identity, a rearrangement of the two tension definitions): a_1 + a_2 = -kappa^2 (sigma_1 + sigma_2)/3 - "
        "(a_s - 1/ell_s); a_1 = 1/ell_s - kappa^2 sigma_1/3", dd["outer"][0] == 0)
    RRc, disc = dd["closed"]
    rr = sp.Symbol("r", positive=True)
    chk("K1: R_ab R^ab = 2(3r^2 - 8r + 6)/(r^4 (2r - 3)^4) matches the computed 2/729 (3m) and 0.08742 (2.15m); its "
        "quadratic's discriminant is negative, so it is positive at every r",
        sp.simplify(RRc.subs(rr, 3) - dd["RR3"]) == 0 and abs(float(RRc.subs(rr, sp.Rational(43, 20)) - dd["RR215"])) < 1e-12
        and disc < 0)
    brs = dd["branches"]
    m4 = [b_ for b_ in brs if b_["s2"] == Fr(-1, 6) and b_["unit"] == "ell_2"]
    chk("K4: every small-d branch, both units, both counts, has an outer bulk that decays; with unit ell_2 both decay; "
        "ours grows only with unit ell_1 and ell_s = 3 ell_1/11 (a_1 = 1/ell_s - 8/(3 ell)); control: unit ell_2 with "
        "-1/6 reproduces multiplane.py M4, ell_s = ell_1 = 3 ell_2/4",
        len(brs) == 6 and all(min(b_["a1"], b_["a2"]) < 0 for b_ in brs)
        and all(b_["a1"] < 0 and b_["a2"] < 0 for b_ in brs if b_["unit"] == "ell_2")
        and all(b_["ell_s"] == Fr(3, 11) for b_ in brs if b_["a1"] > 0)
        and len(m4) == 1 and m4[0]["ell_s"] == Fr(3, 4) and m4[0]["a1"] == Fr(-4, 3))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
