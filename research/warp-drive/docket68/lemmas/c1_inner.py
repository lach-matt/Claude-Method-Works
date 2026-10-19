#!/usr/bin/env python3
"""c1_inner.py -- item 444 (1), C1 of BOUNCE-RESEARCH.md: the inner trapping horizon of the README's delivery spread over
its quanta's wavelength, at both ends.  M approved C1-C3 ("1 - yes").  C2, Barcelo et al.'s growth equations, needs an
inner horizon that lingers; this instrument asks whether the delivery has one.  Labels: computed (sympy, exact where
marked), imported (the record's instruments named), estimate (marked), deduced.  Worked in the conversation; not
verified; not seated.  2026-10-16.

  K0 (read) M's words: 444 (1).
  K1 (computed, exact) A null delivery has no inner apparent horizon.  For radial null inflow (Vaidya, the delivery
     the math requires, b4d_large K12) the outgoing expansion has the sign of f = 1 - 2m(v)/r at the large end and
     f = 1 - mu(v)/r^2 at the small; at each v, f rises with r (df/dr > 0) and tends to -infinity at r -> 0 once any
     mass has arrived, so f = 0 has exactly one root: the outer horizon.  The trapped region reaches r = 0, its inner
     boundary the central singularity -- there is no inner trapping horizon at r > 0, lingering or not.
  K2 (computed, exact; the record's) When the singular onset is naked.  Outgoing rays r = x v from a self-similar onset
     obey 2x^2 - x + 2 mu = 0 (4D, m = mu v): a ray escapes iff mu <= 1/16, so a linear arrival is naked from
     w = 16 M (arrival_large A3); and 2x^3 - x^2 + lambda = 0 (5D, mu = lambda v^2): iff lambda <= 1/27, so the
     order-2 smoothstep (lambda = 3/w^2) is naked from w = 9 r_h (b4d_small D2, arrival_small V3).
  K3 (computed, exact) The quanta's width passes both.  bounce_scope B3: the bit's wavelength is 4 pi^2 r0/ln2 =
     113.9 M at the large end (mu = 1/113.9 < 1/16) and 8 pi^2 r_h/(3 ln2) = 37.97 r_h at the small (lambda = 2.1e-3
     < 1/27).  A delivery spread so is naked at its onset at both ends: the singular centre is seen before the face.
  K4 (estimate, flat-space counting) If instead the inflow passes through a regular centre and leaves.  A pulse of
     width w and energy M (geometric units) puts at most 2 r M/w inside radius r at any moment.  At the large end
     2m/r <= 4M/w: no sphere is ever trapped when w > 4M, and the quanta's width gives 0.035.  At the small end
     mu(r)/r^2 <= 2 r_h^2/(w r), so only the core r < 2 r_h^2/w = 0.053 r_h can be trapped.
  K5 (deduced) What C1 settles.  Neither model has the lingering inner horizon C2 asks of the classical background:
     absorbed at the centre, the spread delivery shows a naked singular onset (K2, K3); passing through it, it forms
     no face at the large end and at most a core 0.05 r_h across at the small (K4).  So C2 is re-posed, not run as
     written: an inner horizon can come only from the quantum fields themselves -- the renormalized stress tensor of
     the collapse's "in" vacuum, multiplied on the plane by c = 2.93e59, making the centre untrapped (a regular core,
     which closing a trapped region formed by null shells requires, prior_art CTH) -- and that is put to M before it
     runs (414).

python3 c1_inner.py [--selftest | --mutants]
"""
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ("2 - no, reassess after the Answer 2, the deeper research computations.",)
v, r, x = sp.symbols("v r x", positive=True)


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def k1():
    """one positive root of f at each v; f -> -oo at r -> 0 once m > 0; df/dr > 0"""
    m, mu = sp.symbols("m mu", positive=True)
    out = {}
    for name, f in (("4D", 1 - 2 * m / r), ("5D", 1 - mu / r ** 2)):
        if "inner" in MUT and name == "4D":                             # a positive tidal charge: an inner horizon
            f = f + sp.Symbol("q", positive=True) / r ** 2
        roots = [s for s in sp.solve(sp.Eq(f, 0), r) if s.is_positive is not False]
        rising = sp.simplify(sp.diff(f, r)).is_positive
        to_minus = sp.limit(f, r, 0, "+") == -sp.oo
        out[name] = (len(roots) == 1 and bool(rising) and bool(to_minus), roots)
    return out


def k2():
    """the naked-onset thresholds: 1/16 (4D linear) and 1/27 (5D self-similar), so w = 16 M and the smoothstep's 9"""
    mu, lam = sp.symbols("mu lam", positive=True)
    disc4 = sp.discriminant(2 * x ** 2 - x + 2 * mu, x)                 # real roots iff disc >= 0
    crit4 = sp.solve(sp.Eq(disc4, 0), mu)[0]
    g = 2 * x ** 3 - x ** 2
    xm = [s for s in sp.solve(sp.diff(g, x), x) if s > 0][0]
    crit5 = -g.subs(x, xm)
    w = sp.symbols("w", positive=True)
    w9 = sp.solve(sp.Eq(3 / w ** 2, crit5), w)[0]
    return crit4, crit5, sp.simplify(1 / crit4), w9


def k3():
    """the quanta's width in clocks: 4 pi^2/ln2 r0 = 113.9 M at 4D; 8 pi^2/(3 ln2) r_h at 5D"""
    w4_r0 = 4 * math.pi ** 2 / math.log(2)
    w4_M = 2 * w4_r0                                                   # r0 = 2M
    w5 = 8 * math.pi ** 2 / (3 * math.log(2))
    if "narrow" in MUT:
        w4_M, w5 = 4.0, 2.0
    mu4 = 1 / w4_M                                                     # linear arrival of M over w
    lam5 = 3 / w5 ** 2                                                 # smoothstep's onset coefficient
    return w4_M, mu4, w5, lam5


def k4(w4_M, w5):
    """flat counting: 2m/r <= 4M/w at 4D; trapped core r < 2 r_h^2/w at 5D (r_h = 1)"""
    return 4.0 / w4_M, 2.0 / w5


def report():
    print("K0 M's words:", words())
    a = k1()
    print("K1 one root of f, f rising, f -> -oo at the centre: 4D %s %s; 5D %s %s" % (a["4D"][0], a["4D"][1], a["5D"][0],
                                                                                     a["5D"][1]))
    c4, c5, w16, w9 = k2()
    print("K2 naked onset iff mu <= %s (4D: w >= %s M), lambda <= %s (5D smoothstep: w >= %s r_h)" % (c4, w16, c5, w9))
    w4, mu4, w5, lam5 = k3()
    print("K3 quanta's width %.1f M (mu = %.4f vs 1/16), %.2f r_h (lambda = %.2e vs 1/27): naked at both ends"
          % (w4, mu4, w5, lam5))
    b4, core5 = k4(w4, w5)
    print("K4 passing through: 4D 2m/r <= %.3f (no face); 5D trapped only inside r < %.3f r_h" % (b4, core5))


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r1 = words(); ok.append(r1); say("K0 words: %s" % r1)
    a = k1(); r1 = a["4D"][0] and a["5D"][0]; ok.append(r1); say("K1 no inner apparent horizon at r > 0: %s" % r1)
    c4, c5, w16, w9 = k2()
    r1 = c4 == sp.Rational(1, 16) and c5 == sp.Rational(1, 27) and w16 == 16 and w9 == 9; ok.append(r1)
    say("K2 thresholds 1/16 and 1/27, widths 16 M and 9 r_h: %s" % r1)
    w4, mu4, w5, lam5 = k3()
    r1 = abs(w4 - 113.9) < 0.1 and mu4 < 1 / 16 and abs(w5 - 37.97) < 0.01 and lam5 < 1 / 27; ok.append(r1)
    say("K3 the quanta's width naked at both ends: %s" % r1)
    b4, core5 = k4(w4, w5)
    r1 = b4 < 1 and abs(b4 - 0.0351) < 1e-3 and abs(core5 - 0.0527) < 1e-3; ok.append(r1)
    say("K4 passing through: no face at 4D (0.035), a core under 0.053 r_h at 5D: %s" % r1)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    for m in ("inner", "narrow"):
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-7s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/2 caught" % caught)
    return caught == 2


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
