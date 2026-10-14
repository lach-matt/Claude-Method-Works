#!/usr/bin/env python3
"""arrival_large.py -- item 384, first step of the approved order: the ARRIVAL row at the family's large end, from M's
rulings, on the large brane hole whose plane reads four-dimensional Schwarzschild to O(ell^2/r0^2) (C3; m1_large M4).
The small end's is arrival_small.py (ARRIVALs, verified 348).  No tests run (M-NO-TESTS-UNTIL-NEEDED): what follows is
the theorem's own algebra and three short integrations of one ray each.  Worked in the conversation (computed with
sympy and a stdlib integrator, exact where marked; deduced where marked; not verified by a separate session; not
seated); 2026-10-14.

  A0 (read) M's words, verbatim in the rulings file: 198, "My guess would be 1." (the README comes in while the corridor
     forms, no partner); 163, "All together, one whole"; 109, "A horizon cannot exist without the object of which it
     needs to exist"; 340, "C, but my guess is A"; 358, "Once everything that doesn't rely on SOURCE is resolved and
     green"; 384, "start proving mine".
  A1 (computed, exact) The flux and the one E.  On the plane's ingoing form ds^2 = -(1 - 2m(v)/r) dv^2 + 2 dv dr +
     r^2 dOmega^2 the only Einstein component is G_vv = 2 m'(v)/r^2: an arrival that only adds energy (m' >= 0) has
     non-negative null energy on every ray, forms our face with no partner (198) and keeps (Z) classically.  After it the
     mass is the README's E/c^2, one E (G1; 136 G's "the README is the energy").
  A2 (computed, exact) Held only whole.  The face's capacity goes as its area, (2m)^2, so at a fraction e of E the
     trapping horizon r = 2m holds e^2 N bits, short of the e N that have come in (on the bits-with-energy reading,
     RBITS) for every e < 1: the README is held only as one whole, M's 163, here at the large end.
  A3 (computed, exact; a ray integrated) The face before the README, and the onset hidden.  A thin arrival puts the
     face's birth 4 clocks (of GM/c^3) before the README's first part, at r = 0 in the flat region (exact: the outgoing
     ray r = 2M + v/2).  A linear arrival of width w clocks -- m = M v/w -- shows its onset to our exterior only if
     2x^2 - x + 2M/w has a real root, i.e. w >= 16 clocks (exact; the four-dimensional 1/16).  Integrated back from the
     face at the arrival's end, a linear arrival is born before its onset at w = 0.0027, 1 and 4 clocks.
  A4 (computed, exact; imported formula) What the README must fit.  Position 2's face at the large end is open at most
     ln(1 + (ell/r0)^2/15) e-folds on 139 (1)'s quarter, at 4 clocks per e-fold: 2.67e-3 clocks at r0 = 10 ell, falling
     as (ell/r0)^2; at most 4 clocks with position 2's plane at its own sigma (close_large L4, its formula restated).
     The README emerges within it only if its arrival onto the bounce lasts less than that.
  A5 (deduced) What the rulings fix and what they leave.  A1-A3 hold for every arrival width below 16 clocks, so every
     width position 2's open period allows meets them: the conditions are consistent, not vacuous.  But the width
     itself is how the README comes in -- 163 rules it one whole, not an instant -- and nothing in the rulings or in the
     corridor's geometry sets it.  It is SOURCE's: the README written on our plane and coming in (344-346).  So ARRIVAL
     at the large end relies on SOURCE, on one number -- the arrival's width below position 2's open period, 2.67e-3
     (10 ell/r0)^2 clocks on 139 (1)'s quarter -- and under 358 (c) it is reported so, not forced green.
     [Item 387: M ruled that position 2's plane carries its own sigma, which at 218's destination is ours. So A4's bound
     is the 4 clocks (close_large L4 (a), the short phase with no junction; READ, an order), not the quarter's 2.67e-3
     (10 ell/r0)^2. A5's consistency stands: 4 < 16. Kept as written.]
     [Item 388: the 4 clocks covers only destinations at our sigma with G2 = G. In the theorem the bound depends on the
     destination. Wherever its own sigma differs from ours the junction binds: about (ell/r0)^2/(3 (G2/G)^(3/2)
     |1 - sigma2/sigma|) clocks, 1.57e-3 at 2P at r0 = 10 ell (junction_own G5, G7). A5 stands: every such bound is
     under 16.]
  A6 (deduced) The rows that wait only on it.  M1P2x (all but the README's emergence within position 2's open period),
     E1x (the README's crossing against that period) and H2tx (resting on M1P2x) rely on SOURCE through A5 alone, and
     reach the small end's state with ARRIVAL: readings on SOURCE once M finalizes.  Z3b, B3 and B4d rest on ARRIVAL and
     on work of their own, next in the order.

Stdlib + sympy.  python3 arrival_large.py [--selftest | --mutants]
"""
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((198, "My guess would be 1."), (163, "All together, one whole"),
         (109, "A horizon cannot exist without the object of which it needs to exist"), (340, "C, but my guess is A"),
         (358, "Once everything that doesn't rely on SOURCE is resolved and green"), (384, "start proving mine"))
WIDTHS = (0.0027, 1.0, 4.0)
CLOCKS_PER_EFOLD = 4.0                    # 1/kappa = 2 r0 = 4 GM/c^3 (close_large L4)


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def vaidya_gvv():
    """G_vv of the ingoing Vaidya form, and every other component of G_ab"""
    v, r, th, ph = sp.symbols("v r theta phi", positive=True)
    m = sp.Function("m")(v)
    f = 1 - 2 * m / r
    g = sp.zeros(4)
    g[0, 0], g[0, 1], g[1, 0] = -f, 1, 1
    g[2, 2], g[3, 3] = r ** 2, r ** 2 * sp.sin(th) ** 2
    x = (v, r, th, ph)
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
                 for d in range(4)) / 2 for c in range(4)] for b in range(4)] for a in range(4)]
    def ric(b, c):
        return sp.simplify(sum(sp.diff(Gam[a][b][c], x[a]) - sp.diff(Gam[a][b][a], x[c])
                               + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(4))
                               for a in range(4)))
    R = sp.Matrix(4, 4, lambda b, c: ric(b, c))
    Rs = sp.simplify(sum(gi[a, b] * R[a, b] for a in range(4) for b in range(4)))
    G = sp.simplify(R - Rs * g / 2)
    target = 2 * sp.diff(m, v) / r ** 2
    others = all(sp.simplify(G[a, b]) == 0 for a in range(4) for b in range(4) if (a, b) != (0, 0))
    return sp.simplify(G[0, 0] - target) == 0, others


def selfsimilar():
    """outgoing rays r = x v in m = mu v: 2 x^2 - x + 2 mu = 0; a real root iff mu <= 1/16"""
    x, mu = sp.symbols("x mu", positive=True)
    eq = 2 * x ** 2 - x + 2 * mu
    disc = sp.discriminant(eq, x)
    crit = sp.solve(sp.Eq(disc, 0), mu)[0]
    return sp.simplify(disc - (1 - 16 * mu)) == 0, crit


def born_before(w, M=1.0, n=40000):
    """the event horizon traced back from r = 2M at v = w through a linear arrival m = M v/w: r at v = 0 (> 0: the face
    is born before the onset); then the flat region's ray back to r = 0 gives the birth time"""
    f = lambda v, r: 0.5 * (1 - 2 * (M * v / w if v > 0 else 0.0) / r)
    h = -w / n
    v, r = w, 2 * M
    for _ in range(n):
        k1 = f(v, r)
        k2 = f(v + h / 2, r + h / 2 * k1)
        k3 = f(v + h / 2, r + h / 2 * k2)
        k4 = f(v + h, r + h * k3)
        r += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        v += h
    return r, -2 * r                                                  # flat region: r = r(0) + v/2, born at v = -2 r(0)


def compute():
    gvv_ok, gvv_only = vaidya_gvv()
    ss_ok, crit = selfsimilar()
    w_naked = 16.0 / (2 if MUT.get("ss_r0_units") else 1)          # M/w = 1/16 -> w = 16 M (M = 1)
    born = {w: born_before(w) for w in WIDTHS}
    thin = born_before(1e-7)
    open_q = lambda q: CLOCKS_PER_EFOLD * math.log(1 + q ** -2 / (6.0 if MUT.get("side_total") else 15.0))
    e = sp.symbols("e", positive=True)
    whole = sp.simplify(e ** 2 - e)                                    # capacity minus bits come in, in units of N
    return dict(gvv_ok=gvv_ok, gvv_only=gvv_only, ss_ok=ss_ok, crit=crit, w_naked=w_naked, born=born,
                thin_birth=thin[1], open10=open_q(10.0), open100=open_q(100.0), open_own=4.0,
                whole_neg=all(whole.subs(e, k) < 0 for k in (sp.Rational(1, 10), sp.Rational(1, 2),
                                                           sp.Rational(99, 100))),
                whole_zero=whole.subs(e, 1) == 0)


def report(o):
    print("arrival_large.py -- ARRIVAL at the large end, from M's rulings (item 384, step 1)\n")
    print("A1 G_vv = 2 m'/r^2: %s; every other component zero: %s" % (o["gvv_ok"], o["gvv_only"]))
    print("A2 capacity minus bits come in, e^2 - e: negative below e = 1 (%s), zero at it (%s)"
          % (o["whole_neg"], o["whole_zero"]))
    print("A3 thin arrival: face born %.4f clocks before the onset; self-similar root iff mu <= %s (%s): naked only for "
          "w >= %.0f clocks" % (-o["thin_birth"], o["crit"], o["ss_ok"], o["w_naked"]))
    for w, (r0, b) in o["born"].items():
        print("A3 linear arrival w = %g clocks: face at the onset r = %.4f M, born %.4f clocks before it" % (w, r0, -b))
    print("A4 position 2's open period: %.3e clocks at r0 = 10 ell, %.3e at 100 ell; %g at its own sigma"
          % (o["open10"], o["open100"], o["open_own"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("A0 198, 163, 109, 340, 358 and 384 verbatim in their items",
        all(" ".join(t.split()) in _item(n) for n, t in WORDS))
    add("A1 G_vv = 2 m'(v)/r^2 and every other Einstein component zero", o["gvv_ok"] and o["gvv_only"])
    add("A2 at a fraction e < 1 of E the face holds e^2 N < e N: held only whole", o["whole_neg"] and o["whole_zero"])
    born = o["born"]
    add("A3 thin arrival born 4 clocks early; naked only for w >= 16 clocks; linear arrivals of 0.0027, 1 and 4 clocks "
        "born before their onset", abs(-o["thin_birth"] - 4) < 1e-5 and o["ss_ok"] and o["crit"] == sp.Rational(1, 16)
        and abs(o["w_naked"] - 16) < 1e-12 and all(born[w][0] > 0 for w in WIDTHS))
    add("A4 position 2's open period 2.67e-3 clocks at r0 = 10 ell, 100 times less at 100 ell; 4 at its own sigma",
        "%.3g" % o["open10"] == "0.00267" and abs(o["open10"] / o["open100"] - 100) < 0.05 and o["open_own"] == 4)
    add("A5 every width position 2's open period allows is below the 16 clocks A3 needs: consistent, not vacuous",
        max(o["open10"], o["open_own"]) < o["w_naked"] and all(born[w][0] > 0 for w in WIDTHS if w <= o["open_own"]))
    return res


MUTANTS = {"ss_r0_units": "the naked-onset width read in clocks of r0/c, not GM/c^3 (A3)",
           "side_total": "position 2's open period on the side total (6) for the junction's own 15 (A4)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-12s %-66s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
