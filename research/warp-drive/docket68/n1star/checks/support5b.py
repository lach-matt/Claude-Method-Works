#!/usr/bin/env python3
"""support5b.py -- C10: supplement Lemma 3.2's identity (3.3), at w = 0, in every component (the paper's section 5.2,
"the equation for h has bounded coefficients except one"; verifier 259's census, row 3; support5.py C3 checked the
ell (x) ell component only).

(3.3) at w = 0, for phi(X) without the phase: the linearised gauge-fixed operator applied to phi [d_th g1],

    P(phi G1) = -lam^-1 (ell . d phi) G2 + lam^-1 phi T(d_th g1) - (1/2) (box~ phi) G1 + B1 . d phi + C1 phi,

G1 = [d_th g1], G2 = [d_th^2 g1], ell = g0^-1 dv, box~ = g0^ab d_a d_b, B1, C1 bounded. Computed exactly on lead5.py's
stage-0 profile (g1 = W = W_TT + chi dv^2, chi generic, th the phase s), with phi = phi(v, r, theta) generic, through
support5.py's linearisation of Ric^H in its gauge, every lam order from -3 to 0 kept:

  C10 (exact) in every one of the 15 components: (a) no term of order lam^-2 or lower; (b) the lam^-1 part equals
      -(ell . d phi) [d_s^2 W] + phi T(d_s W), T(d_s W) the lam^-1 part of P([d_s W]) (support5.py C2's T); (c) at
      lam^0 the second derivatives of phi enter only as -(1/2) (g0^ab d_a d_b phi) [d_s W].
      (b) does not need W(ell, ell) = 0: the term g^-1(dv, dv) = -lam W(ell, ell) brings to the lam^-1 part is
      (1/2) W(ell, ell) phi [d_s^3 W], proportional to phi and so inside phi T(d_s W) (C10b: C10 with an oscillating
      dr dr component added to W, so that W(ell, ell) != 0).
  Controls (mutant identities, each must be rejected): (b) with -2 (ell . d phi) in place of -(ell . d phi); (c) with
      -(box~ phi) in place of -(1/2)(box~ phi). Also printed: in how many components (ell . d phi)[d_s^2 W] is nonzero.

Labels: computed (exact, sympy).

Run: python3 checks/support5b.py   (a few minutes)
"""
import os
import sys
import time

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import support5 as S5                                                           # noqa: E402
import lead5 as L                                                               # noqa: E402


def c10(control=False, rr=False):
    t0 = time.time()
    W = L.wave(with_chi=True)
    if rr:                                                                        # W(ell, ell) != 0
        W[1, 1] = L.A*L.Ef*L.Hf*L.r**sp.Rational(-3, 2)*sp.cos(L.s)
    phi = sp.Function("phi")(L.v, L.r, L.th)
    Ws = W.applyfunc(lambda e: sp.diff(e, L.s))
    Wss = W.applyfunc(lambda e: sp.diff(e, L.s, 2))
    Q, _ = S5._lin_ricH(W, Ws.applyfunc(lambda e: phi*e), sp.Integer(1))        # P(phi [d_s W])
    T, _ = S5._lin_ricH(W, Ws, sp.Integer(1))                                     # P([d_s W]); T = its lam^-1 part
    g0, g0i = L.background()
    X = L.X
    ell = [sum(g0i[a, b]*sp.diff(L.v, X[b]) for b in range(5)) for a in range(5)]
    elld = sum(ell[a]*sp.diff(phi, X[a]) for a in range(5))
    box = sum(g0i[a, b]*sp.diff(phi, X[a], X[b]) for a in range(5) for b in range(5))
    cl, cb = (2, 1) if control else (1, sp.Rational(1, 2))                        # mutants: -2 (ell.d phi), -(box phi)
    low = all(sp.simplify(Q[k][j]) == 0 for k in Q for j in (-3, -2))
    ident = all(sp.simplify(Q[k][-1] - (-cl*elld*Wss[k] + phi*T[k][-1])) == 0 for k in Q)
    live = sum(1 for k in Q if sp.simplify(elld*Wss[k]) != 0)
    second = True
    for k in Q:
        e0 = sp.expand(Q[k][0])
        d2 = {d for d in e0.atoms(sp.Derivative) if d.expr == phi and d.derivative_count == 2}
        part = sum(e0.coeff(d)*d for d in d2)
        second &= sp.simplify(part - sp.expand(-cb*box*Ws[k])) == 0
        second &= not any(d.expr == phi and d.derivative_count > 2 for d in e0.atoms(sp.Derivative))
    if control:
        print("  C10%s control: mutant (b) holds: %s; mutant (c) holds: %s" % ("b" if rr else "", ident, second),
              flush=True)
        return ident or second
    print("  C10%s: P(phi [d_s W]) in all %d components: no order below lam^-1: %s; lam^-1 part = -(ell . d phi)"
          " [d_s^2 W] + phi T(d_s W): %s (the ell term nonzero in %d components); at lam^0 the second derivatives of phi"
          " only in -(1/2)(box~ phi) [d_s W]: %s [%.0fs]" % ("b (W(ell, ell) != 0)" if rr else "", len(Q), low,
                                                              ident, live, second, time.time() - t0), flush=True)
    return low and ident and second


CHECKS = [("C10", c10), ("C10b", lambda control=False: c10(control, rr=True))]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
