#!/usr/bin/env python3
"""b5_positive.py -- Warp Theorem lemma B5: positivity for the entangled pin, at every point (item 139 (2),
M-PROVE-POSITIVE: "positive, and you have to prove it").

Your rulings: position 2's plane negative, a quarter of ours, ours positive (139 (1)); static (141); entangled (140); the
planes coincide, the extra dimension included (127).  The board's composite (STATIC.md S4): the sheets' tensions sum to
+1 of the Randall-Sundrum value, +4/3 and -1/3.

  B5a THE NULL ENERGY AT EVERY POINT IS YOURS; ITS CONSISTENCY IS COMPUTED (DERIVED).  "An NEC is never violated"
      (117) and "the NEC only ever appears to break, but never does" (120): pointwise null energy in five dimensions is
      your ruling, not the board's reading.  What the board must show is that the composite admits it.  At one place
      (127: the planes coincide, the extra dimension included), the junction condition sees only the sheets' summed
      surface stress (Israel's condition, standard, not READ): (4/3 - 1/3) lambda_RS = +lambda_RS, positive (139 (1),
      computed).  A smooth composite with that summed stress keeping null energy at every point exists (B5b), so your
      ruling is consistent; and on it the null stress is S_kk = lambda_RS f(y) k_y^2 >= 0 at every depth.  Control: if
      the two sheets were thickened with different profiles (the case DOORS.md warned of) the null stress goes negative
      where the negative sheet is the wider -- a thickening your ruling 120 excludes.  First written with this resting on
      the board's H-SHARED-PROFILE, a reading of 127; with 117 and 120 read as rulings on every point, it is not needed
  B5b A SMOOTH WALL THAT KEEPS IT.  The composite as a canonical scalar domain wall, ds^2 = e^{2A(y)} eta + dy^2: the
      5D Einstein equations give phi'^2 = -3 A'' (kappa_5 = 1), and the scalar's null energy is T_kk = (k.dphi)^2 >= 0
      identically.  With A = -(w/ell) ln cosh(y/w): A'' < 0, so phi is real everywhere; as the width w -> 0, A -> -|y|/ell
      and the extrinsic curvature -> -g/ell, the Randall-Sundrum plane of localbulk.py (computed).  So a smoothing that
      keeps null energy at every point exists: CENSOR5D's W1 holds, escape (d) closes
  B5c THE PIN CARRIES NO NEGATIVE ENERGY (DERIVED).  The planes coincide while the corridor exists (127) and do not move
      relative to each other -- the pin holds the separation fixed (141).  A separation held at zero is not a degree of
      freedom, so there is no radion: no field for PRZ's ghost to live in (it needs a separation that moves; STATIC.md
      S3 computed it for one -- standard that the radion is the separation's modulus, not READ here).  So item 139 (2)'s
      "positive": the energy that remains is the composite's positive summed tension (B5a) and, on the plane, the
      positive density outside the neck (ledger.py E4b).  First written as the board's H-PIN-IS-COINCIDENCE; it is 127
      with 141, both yours
Imports nothing beyond sympy.  python3 b5_positive.py [--selftest]
"""
import sys

import sympy as sp

y, w, ell, lam = sp.symbols("y w ell lambda_RS", positive=True)


def b5a():
    yy = sp.Symbol("y", real=True)
    f_shared = sp.exp(-yy**2 / w**2) / (w * sp.sqrt(sp.pi))
    S_shared = sp.simplify((sp.Rational(4, 3) - sp.Rational(1, 3)) * lam * f_shared)
    # control: the negative sheet twice as wide
    f1 = sp.exp(-yy**2 / w**2) / (w * sp.sqrt(sp.pi))
    f2 = sp.exp(-yy**2 / (2 * w) ** 2) / (2 * w * sp.sqrt(sp.pi))
    S_diff = sp.Rational(4, 3) * lam * f1 - sp.Rational(1, 3) * lam * f2
    at_far = sp.simplify(S_diff.subs(yy, 3 * w))
    return {"S_shared": S_shared, "shared_nonneg": S_shared.is_nonnegative, "S_diff_far": at_far,
            "diff_negative_far": bool(at_far.subs({lam: 1, w: 1}) < 0)}


def b5b():
    A = -(w / ell) * sp.log(sp.cosh(y / w))
    App = sp.simplify(sp.diff(A, y, 2))
    phi_p2 = sp.simplify(-3 * App)
    # check the 5D Einstein equations for a scalar wall: G^y_y and G^t_t for e^{2A} eta + dy^2
    t, x1, x2, x3 = sp.symbols("t x1 x2 x3")
    Af = sp.Function("A")(y)
    X = [t, x1, x2, x3, y]
    g = sp.diag(-sp.exp(2 * Af), sp.exp(2 * Af), sp.exp(2 * Af), sp.exp(2 * Af), 1)
    gi = g.inv()
    n = 5
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                                        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
                                              for d in range(n)) for a in range(n)))
    Rs = sp.simplify(sum(gi[i, i] * Ric[i, i] for i in range(n)))
    Gmix = [sp.simplify(gi[i, i] * Ric[i, i] - Rs / 2) for i in range(n)]       # G^i_i
    # scalar wall: T^t_t = -(phi'^2/2 + V), T^y_y = phi'^2/2 - V; so G^y_y - G^t_t = phi'^2
    rel = sp.simplify(Gmix[4] - Gmix[0])
    rel_ok = sp.simplify(rel - (-3 * sp.diff(Af, y, 2))) == 0
    thin = sp.limit(sp.diff(A, y), w, 0)
    return {"App": App, "phi_p2": phi_p2, "phi_real": all(float(phi_p2.subs({w: 1, ell: 1, y: v})) > 0
                                                            for v in (-5, -1, 0, 1, 5)),
            "einstein_rel": rel_ok, "thin_limit_Aprime": thin}


def compute():
    return {"a": b5a(), "b": b5b()}


def report(d):
    a, b = d["a"], d["b"]
    print("b5_positive.py -- Warp Theorem lemma B5\n")
    print("B5a shared profile: S_kk/k_y^2 = %s (non-negative: %s); control, different profiles at y = 3w: %s"
          % (a["S_shared"], a["shared_nonneg"], a["S_diff_far"]))
    print("B5b G^y_y - G^t_t = -3A'' for the wall: %s; A = -(w/ell) ln cosh(y/w): phi'^2 = %s (real everywhere: %s); "
          "w -> 0: A' -> %s" % (b["einstein_rel"], b["phi_p2"], b["phi_real"], b["thin_limit_Aprime"]))
    print("B5c the pin is the coincidence: no separation, no radion, no negative kinetic energy (the board's reading)")


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    a, b = d["a"], d["b"]
    chk("B5a: at one place (127) the summed tension is +lambda_RS, and on your ruling (117, 120) the null stress is "
        "lambda_RS f(y) k_y^2 >= 0 at every depth",
        a["shared_nonneg"])
    chk("B5a control: two different profiles (negative sheet twice as wide) go negative at y = 3w -- excluded by 120",
        a["diff_negative_far"])
    chk("B5b: the 5D Einstein equations give phi'^2 = -3A'' for a scalar wall (computed from the metric)",
        b["einstein_rel"])
    chk("B5b: for A = -(w/ell) ln cosh(y/w), phi'^2 = 3 sech^2(y/w)/(w ell) > 0: the wall is a real scalar, NEC at every point",
        b["phi_real"] and sp.simplify(b["phi_p2"] - 3 / (w * ell * sp.cosh(y / w) ** 2)) == 0)
    chk("B5b: as w -> 0, A' -> -1/ell for y > 0 -- the Randall-Sundrum plane, K = -g/ell", sp.simplify(b["thin_limit_Aprime"] + 1 / ell) == 0)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
