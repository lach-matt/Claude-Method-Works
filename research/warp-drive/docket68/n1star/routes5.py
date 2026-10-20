#!/usr/bin/env python3
"""routes5.py -- the two computed facts behind ROUTES-OPEN.md's route for the mass at past null infinity (D36).
Labels: computed (exact, sympy), READ.

  Q1 (computed, exact) Five-dimensional ingoing Vaidya, -(1 - mu(v)/r^2) dv^2 + 2 dv dr + r^2 dOmega_3^2, has
     R_vv = 3 mu'/(2 r^3) and every other Ricci component zero.  With Proposition 2.3's quadratic part of R_vv,
     -2 (P1_v^2 + P1_v P2_v + P2_v^2), the averaged equation is mu' = (4/3) r^3 <P1_v^2 + P1_v P2_v + P2_v^2>.
     Control: the coefficient 1 in place of 3/2.
  Q2 (computed, exact) Tanabe, Tanahashi and Shiromizu's five-dimensional Bondi form (READ below, (5)) with D1 = D2
     = D3 = 0 is the class's angular metric, hf_theorem5.py's ansatz diag(e^(-2(P1+P2)), c^2 e^(2P1), s^2 e^(2P2)),
     exactly, under theta_T = pi/2 - theta, C1 = -2(P1 + P2), C2 = 2 P1, C3 = 2 P2; and their mass-loss density
     (1/3)(C11,u^2 + C11,u C21,u + C21,u^2), run backwards in time (u -> -v), is (4/3)(p1_v^2 + p1_v p2_v + p2_v^2),
     p_i the r^(3/2) coefficients of P_i: the density of Q1 and of past5.py P7.  Control: C1 not traceless.

READ (alphaXiv, 2026-10-20).  [TTS09] K. Tanabe, N. Tanahashi and T. Shiromizu, arXiv:0909.0426v2, p. 2 (4)-(5), p. 4
(28): "dM(u, x^A)/du = -(1/3)((C11,u)^2 + C11,u C21,u + (C21,u)^2 + (D11,u)^2 + (D21,u)^2 + (D31,u)^2)", with
V = r^2 + V1 r^(1/2) - M + O(r^(-1/2)) (26), so that M is the Tangherlini mu.

sympy.  python3 routes5.py [--selftest | --mutants]
"""
import sys

import sympy as sp


def ricci(g, x):
    n = len(x)
    gi = g.inv()
    G = [[[sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
               for d in range(n))/2 for c in range(n)] for b in range(n)] for a in range(n)]
    return lambda b, c: sp.simplify(sum(sp.diff(G[a][b][c], x[a]) - sp.diff(G[a][b][a], x[c])
                                        + sum(G[a][a][d]*G[d][b][c] - G[a][c][d]*G[d][b][a] for d in range(n))
                                        for a in range(n)))


def q1(control=0):
    v, r, th, p1, p2 = sp.symbols("v r theta phi1 phi2", real=True)
    mu = sp.Function("mu")(v)
    g = sp.zeros(5)
    g[0, 0] = -(1 - mu/r**2); g[0, 1] = g[1, 0] = 1
    g[2, 2] = r**2; g[3, 3] = r**2*sp.cos(th)**2; g[4, 4] = r**2*sp.sin(th)**2
    R = ricci(g, [v, r, th, p1, p2])
    coef = 1 if control == 1 else sp.Rational(3, 2)
    vv = sp.simplify(R(0, 0) - coef*sp.diff(mu, v)/r**3) == 0
    rest = all(R(i, j) == 0 for i in range(5) for j in range(i, 5) if (i, j) != (0, 0))
    return bool(vv and rest)


def q2(control=0):
    th, P1, P2, a, b = sp.symbols("theta P1 P2 a b", real=True)
    c, s = sp.cos(th), sp.sin(th)
    ours = sp.diag(sp.exp(-2*(P1 + P2)), c**2*sp.exp(2*P1), s**2*sp.exp(2*P2))          # (theta, phi1, phi2)
    C2, C3 = 2*P1, 2*P2
    C1 = (2*P1 - 2*P2) if control == 1 else -(C2 + C3)
    thT = sp.pi/2 - th                                                                  # TTS's (theta, phi, psi)
    tts = sp.diag(sp.exp(C1), sp.exp(C2)*sp.sin(thT)**2, sp.exp(C3)*sp.cos(thT)**2)
    same = sp.simplify(ours - tts) == sp.zeros(3)
    # the density, with C_i,u -> 2 p_i,v (the squares are blind to u -> -v); C1 traceless at leading order
    c21, c31 = 2*a, 2*b                                                                 # C21 <-> 2 p1, C31 <-> 2 p2
    c11 = (c21 - c31) if control == 1 else -(c21 + c31)
    dens = sp.expand(sp.Rational(1, 3)*(c11**2 + c11*c21 + c21**2) - sp.Rational(4, 3)*(a**2 + a*b + b**2)) == 0
    return bool(same and dens)


CHECKS = [("Q1 five-dimensional Vaidya: R_vv = 3 mu'/(2 r^3), all else zero", q1, 1),
          ("Q2 [TTS09]'s Bondi form is the class's ansatz with C = 2P; its mass density is (4/3)(p-form)", q2, 1)]


def selftest():
    ok_all = True
    for name, f, nc in CHECKS:
        good = f()
        control = any(f(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<100} {state}" + ("" if not control else "  (control passed: vacuous)"), flush=True)
    print(f"routes5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, f, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            m = f(control=k)
            caught += (not m)
            print(f"mutant {k} of {name[:2]}: {'caught' if not m else 'NOT caught'}")
    print(f"routes5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
