#!/usr/bin/env python3
"""gdix5.py -- GAUGEDECAY5.md Round 3, task 1: the 1-form wave operator Box on the repaired domain of Part IX (D610).
Computed.

Part IX's repair poses the comparison on U# := M o {t_IVP > -1}, Omega# := D_{U#}(Sigma o) and its future half
N+ = M o {t_IVP >= 0}; a source given on N+ only (smooth up to Sigma o) is extended across Sigma o (Seeley) and the
Cauchy problem is solved on Omega#.  Round 3 uses this for Box := 2 delta G delta^* (round 1's harmonic-gauge vector,
Proposition 2.1 (a)), and needs that the restriction to N+ of the solution does not depend on the extension: the
difference of two solutions has Box d = 0 on N+ and zero Cauchy data on Sigma o, and Part IX Theorem 2.2's Step 3
(infinite-order vanishing at a noncharacteristic Sigma o, extension by zero, [BGP] Corollary 3.2.4) applies to it if
Sigma o is noncharacteristic for Box with the leading coefficient of Part IX Lemma 2.1 (a).

  P1 (exact identities decided at random rational points to 60 digits, as in ix5.py) On the curved three-dimensional
     metric of ix5.py (g_{0i} != 0 at Sigma = {t = 0}; the identity is pointwise and dimension-free):
     (a) for w = f(t) W, f arbitrary and W a 1-form with every component an arbitrary function of (x, y), no
     derivative of f above the second occurs in Box w and the coefficient of f'' is -g^tt W.  With f = t^m this gives
     the coefficient of t^(m-2) at t = 0 as -m (m-1) g^tt W, so Box d = 0 with d = O(t^m) forces W = 0 (g^tt < 0):
     d vanishes to infinite order at Sigma.  (b) The example m = 2 with a remainder t^3 V: Box w at t = 0 is -2 g^tt W.
     Control: 2 delta delta^* (G dropped) fails in (a) and (b) -- the trace term of G is what makes the leading
     coefficient scalar.
Labels: computed (P1 by polynomial identity testing at 60 digits, as ix5.py).
Run: python3 checks/gdix5.py
"""
import sys

import sympy as sp

from ix5 import RANGES, christoffel, curved_setting, fails, holds, theta


def box1(w, g, X):
    """Box w := 2 delta G delta^* w = Theta(L_w g), Theta(k) = delta G k (ix5.theta)"""
    n = len(X)
    Gm, _ = christoffel(g, X)
    Dw = [[sp.diff(w[b], X[a]) - sum(Gm[c][a][b]*w[c] for c in range(n)) for b in range(n)] for a in range(n)]
    lie = sp.Matrix(n, n, lambda a, b: Dw[a][b] + Dw[b][a])
    return theta(lie, g, X)


def box1_noG(w, g, X):
    """2 delta delta^* w (the trace term of G dropped): -nabla^a (nabla_a w_m + nabla_m w_a)"""
    n = len(X)
    Gm, gi = christoffel(g, X)
    Dw = [[sp.diff(w[b], X[a]) - sum(Gm[c][a][b]*w[c] for c in range(n)) for b in range(n)] for a in range(n)]
    k = [[Dw[a][b] + Dw[b][a] for b in range(n)] for a in range(n)]
    Dk = [[[sp.diff(k[a][b], X[c]) - sum(Gm[d][c][a]*k[d][b] + Gm[d][c][b]*k[a][d] for d in range(n))
            for b in range(n)] for a in range(n)] for c in range(n)]
    return [-sum(gi[a, c]*Dk[c][a][m] for a in range(n) for c in range(n)) for m in range(n)]


def p1(control=False):
    X, g, _ = curved_setting()
    t = X[0]
    gi = g.inv()
    op = box1_noG if control else box1
    W = [sp.Function('W%d' % a)(X[1], X[2]) for a in range(3)]
    V = [sp.Function('V%d' % a)(X[1], X[2]) for a in range(3)]
    f = sp.Function('f')(t)
    F0, F1, F2, F3 = sp.symbols('F0 F1 F2 F3')
    rep = {sp.Derivative(f, (t, 3)): F3, sp.Derivative(f, (t, 2)): F2, sp.Derivative(f, t): F1}
    E = [e.subs(rep).subs(f, F0) for e in op([f*Wa for Wa in W], g, X)]
    no_high = all(sp.diff(e, F3) == 0 for e in E)
    want = [-gi[0, 0]*Wa for Wa in W]
    if control:
        ra = not fails([sp.diff(e, F2) - wv for e, wv in zip(E, want)], ranges=RANGES)
    else:
        ra = no_high and holds([sp.diff(e, F2) - wv for e, wv in zip(E, want)], ranges=RANGES)
    w2 = [t**2*Wa + t**3*Va for Wa, Va in zip(W, V)]
    E2 = op(w2, g, X)
    want2 = [-2*gi[0, 0].subs(t, 0)*Wa for Wa in W]
    if control:
        rb = not fails([e.subs(t, 0) - wv for e, wv in zip(E2, want2)], ranges=RANGES)
    else:
        rb = holds([e.subs(t, 0) - wv for e, wv in zip(E2, want2)], ranges=RANGES)
    print("  P1%s (a) w = f(t) W: no f''' and the coefficient of f'' in Box w is -g^tt W: %s; (b) m = 2, w = t^2 W + "
          "t^3 V: Box w at t = 0 is -2 g^tt W: %s" % (" control (2 delta delta^*, G dropped)" if control else "",
                                                      ra, rb), flush=True)
    return ra and rb


CHECKS = [("P1", p1)]


def main():
    only = sys.argv[1:]
    ok = True
    for name, fn in CHECKS:
        if only and name not in only:
            continue
        good = fn()
        ctl = fn(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    print("EXIT %d" % (0 if ok else 1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
