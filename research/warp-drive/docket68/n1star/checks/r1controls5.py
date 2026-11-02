"""r1controls5.py -- SETTLE-GLAM5 round 2: failing controls for the round-1 checks that had none or had one that
cannot fail (verifier's nit at a378adc: T2 and W1 had no control; T6c and T8g could not fail). tail5.py and wedge5.py
are left as the verifier read them; the controls are here.

  C1 (T2) the ODE of T2a, (s - s^2/2) F'' + (p - 1/2)(1 - s) F' - (p^2 - 2p - kappa) F/2 = 0, is solved by
     2F1(p + l, p - l - 2; p - 1/2; s/2) (T2b, residual < 1e-20) and NOT by 2F1(p + l, p - l - 2; p + 1/2; s/2) (the
     third parameter moved by 1): the control's residual exceeds 1e-3 at p = 5/2, l = 0..6.
  C2 (W1) the identity (5.1), d_a(g^ab T_bc X^c) = (box phi) X phi + T(grad w, d_t), at four points (mu = 1, 3;
     a = 1/3, 3/4; analytic gradients of a random cubic phi, mpmath at 40 digits for the outer derivative): it holds,
     and the identity WITHOUT the bulk term T(grad w, d_t) fails at every point (the control).
  C3 (T6c) a wrong subtraction is caught: rho^(-l0)(rho^(5/2) - (1/2) rho^(5/2)) is not in L^2(drho/rho) near 0 at
     l0 = 13/4 (the integral from eps diverges), so the claim "the remainder is in the class" is rejected.
  C4 (T8g) the claim "ehat_b(0) = 0" for the bump itself is rejected (int env_b = 0.33...), while env_b' does have
     zero time integral: the record's waves are of the first kind.
Labels: computed (sympy exact; mpmath 30-40 digits).

    python3 checks/r1controls5.py
"""
import random
import sys

import mpmath as mp
import sympy as sp

FAIL = []


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


def c1():
    print("C1  T2's ODE: the hypergeometric solution and a wrong one")
    mp.mp.dps = 30
    pp = mp.mpf(5)/2
    good, bad = mp.mpf(0), mp.mpf(10)
    for l in range(0, 7):
        kk = l*(l + 2)
        for cpar, store in ((pp - mp.mpf(1)/2, "good"), (pp + mp.mpf(1)/2, "bad")):
            f = lambda x: mp.hyp2f1(pp + l, pp - l - 2, cpar, x/2)
            worst = mp.mpf(0)
            for x in (mp.mpf("0.3"), mp.mpf("0.9"), mp.mpf("1.4")):
                res = (x - x**2/2)*mp.diff(f, x, 2) + (pp - mp.mpf(1)/2)*(1 - x)*mp.diff(f, x) - (pp**2 - 2*pp - kk)*f(x)/2
                worst = max(worst, abs(res))
            if store == "good":
                good = max(good, worst)
            else:
                bad = min(bad, worst)
    check("C1a the T2b solution: residual < 1e-20", good < mp.mpf(10)**-20, mp.nstr(good, 3))
    check("C1b control: third parameter p + 1/2: residual > 1e-3 for every l <= 6", bad > mp.mpf(10)**-3, mp.nstr(bad, 3))


def c2():
    print("C2  W1's identity (5.1) and the same identity without its bulk term")
    X = sp.symbols("t x1 x2 x3 x4", real=True)
    random.seed(21)
    mons = [(1, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 1, 0), (1, 0, 0, 0, 1), (1, 2, 0, 0, 0), (0, 0, 1, 1, 1),
            (3, 0, 0, 0, 0), (0, 0, 0, 0, 2), (1, 1, 0, 1, 0)]
    phi = sum(sp.Rational(random.randint(-5, 5), random.randint(1, 4))*sp.Mul(*[X[i]**m[i] for i in range(5)])
              for m in mons)
    grad = sp.lambdify(X, [sp.diff(phi, x) for x in X], "mpmath")
    mp.mp.dps = 40
    eta = [-1, 1, 1, 1, 1]
    worst_full, best_cut = mp.mpf(0), mp.mpf(10)**10
    for m in (1, 3):
        for aa in (mp.mpf(1)/3, mp.mpf(3)/4):
            def geo(y):
                rr = mp.sqrt(sum(c*c for c in y[1:]))
                k = [mp.mpf(1)] + [c/rr for c in y[1:]]
                g = [[(eta[i] if i == j else 0) + m/rr**2*k[i]*k[j] for j in range(5)] for i in range(5)]
                K = [eta[i]*k[i] for i in range(5)]
                gi = [[(eta[i] if i == j else 0) - m/rr**2*K[i]*K[j] for j in range(5)] for i in range(5)]
                return g, gi

            def w(y):
                return (mp.sqrt(sum(c*c for c in y[1:])) - y[0])**(2*aa)

            def P(y, a):
                g, gi = geo(y)
                d = grad(*y)
                up = [sum(gi[i][j]*d[j] for j in range(5)) for i in range(5)]
                nrm = sum(d[i]*up[i] for i in range(5))
                T0 = [d[b]*d[0] - g[b][0]*nrm/2 for b in range(5)]
                return w(y)*sum(gi[a][b]*T0[b] for b in range(5))

            def flux(y, a):
                g, gi = geo(y)
                d = grad(*y)
                return sum(gi[a][j]*d[j] for j in range(5))
            pt = [mp.mpf(c) for c in random.choice(([1, 3, 2, 5, 4], [-2, 7, 1, 1, 3], [0, 4, 4, 2, 1]))]
            div = sum(mp.diff(lambda z: P(pt[:a] + [z] + pt[a + 1:], a), pt[a]) for a in range(5))
            box = sum(mp.diff(lambda z: flux(pt[:a] + [z] + pt[a + 1:], a), pt[a]) for a in range(5))
            g, gi = geo(pt)
            d = grad(*pt)
            up = [sum(gi[i][j]*d[j] for j in range(5)) for i in range(5)]
            nrm = sum(d[i]*up[i] for i in range(5))
            dw = [mp.diff(lambda z: w(pt[:i] + [z] + pt[i + 1:]), pt[i]) for i in range(5)]
            gw = [sum(gi[i][j]*dw[j] for j in range(5)) for i in range(5)]
            bulk = sum(gw[b]*(d[b]*d[0] - g[b][0]*nrm/2) for b in range(5))
            worst_full = max(worst_full, abs(div - box*w(pt)*d[0] - bulk)/(1 + abs(div)))
            best_cut = min(best_cut, abs(div - box*w(pt)*d[0])/(1 + abs(div)))
    check("C2a (5.1) holds at four points (relative residual < 1e-25)", worst_full < mp.mpf(10)**-25,
          mp.nstr(worst_full, 3))
    check("C2b control: without T(grad w, d_t) the identity fails at every point (relative defect > 1e-3)",
          best_cut > mp.mpf(10)**-3, mp.nstr(best_cut, 3))


def c3():
    print("C3  T6c's control: a wrong subtraction is not in the class")
    rho, eps = sp.symbols("rho epsilon", positive=True)
    l0 = sp.Rational(13, 4)
    I = sp.integrate((rho**(-l0)*(rho**sp.Rational(5, 2) - sp.Rational(1, 2)*rho**sp.Rational(5, 2)))**2/rho,
                     (rho, eps, 1))
    check("C3a with coefficient 1/2 the integral from eps diverges as eps -> 0", sp.limit(I, eps, 0) == sp.oo, str(I))


def c4():
    print("C4  T8g's control: the bump has nonzero time integral")
    mp.mp.dps = 30

    def bump(x):
        y = (x - 2)/(mp.mpf(3)/2)
        return mp.mpf(0) if abs(y) >= 1 else mp.exp(-1/(1 - y*y))
    e0 = mp.quad(bump, [mp.mpf(1)/2, 2, mp.mpf(7)/2])
    d0 = mp.quad(lambda x: mp.diff(bump, x), [mp.mpf(1)/2, 2, mp.mpf(7)/2])
    check("C4a the claim 'ehat_b(0) = 0' is rejected: int env_b > 0.3", e0 > mp.mpf("0.3"), mp.nstr(e0, 8))
    check("C4b env_b' has zero time integral (T8g's statement)", abs(d0) < mp.mpf(10)**-20, mp.nstr(d0, 3))


def main():
    for f in (c1, c2, c3, c4):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
