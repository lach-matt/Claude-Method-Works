#!/usr/bin/env python3
"""horizon5.py -- part (iii) for lam > 0: the outgoing expansion of the spheres {v, r = const} for the metrics of
Theorem 1 has one zero per column, within O(lam) of sqrt(mu).  The exact facts the deduction uses (N1STAR-PROOF.md
section 8).

Coordinates (tau, r, th, p1, p2), v = tau + r; g0 = -dtau^2 + dr^2 + r^2 (dth^2 + cos^2 th dp1^2 + sin^2 th dp2^2)
+ (mu(v)/r^2) dv^2, five-dimensional Vaidya in ingoing Kerr-Schild form (ks5.py K1).  S_(v,r) := {tau = v - r, r} is a
round 3-sphere; its future null normals are g^-1 k for the null covectors k in span{dtau, dr}.  The expansion along
n = g^-1 k is theta_k = -gamma^AB Gamma[g]^c_AB k_c (gamma the induced metric; tangential coordinate fields).

  H1 (computed, exact) For g0 the null covectors in span{dtau, dr} are dv (ingoing) and dr + ((m - 1)/(m + 1)) dtau,
     m = mu/r^2 (outgoing); with the latter, theta_k = 3 (1 - mu/r^2)/(2 r) times a factor with no zero or pole for
     r > 0 and positive (it is 2 r^2/(r^2 + mu)), the normal n = g0^-1 k being future directed with n(tau) = 1; the zero
     r = sqrt(mu) is simple, d/dr [3 (1 - mu/r^2)/(2 r)] = 3/mu there.  The future ingoing normal -g0^-1 dv = L0 has
     expansion -3/r < 0.  Control: the ingoing root in place of the outgoing (its ratio has a pole at sqrt(mu)).
  H2 (computed, exact; two-scale) For g = g0 + lam W(X, v/lam) with W any profile tangent to the spheres and traceless
     on them (W(ell, .) = 0 and tr_g0 W = 0: lead5.py L5 for the record's wave) plus chi dv^2, chi arbitrary, the
     expansion has no term of order lam^0 beyond g0's: theta_k(g) = theta_k(g0) + O(lam), the O(lam) a profile.  The
     reason is one line: the fast derivative enters only through d_c of the tangential components, as
     (1/2) k(ell) d_th(tr_S W), and tr_S W = tr_g0 W = 0 when W(ell, .) = 0.  Control: a W with a trace on the spheres
     gives an O(1) oscillation.
  H3 (computed, exact) Along a column (v and the angles fixed, r varying) the phase v/lam is constant, so the
     r-derivative of a profile term [f] = f(X, v/lam) is [d_r f] with no 1/lam.  Control: along a line of fixed tau the
     phase is not constant.

python3 horizon5.py [--selftest | --mutants]
"""
import sys

import sympy as sp

tau, r, th, p1, p2 = sp.symbols("tau r theta phi1 phi2", real=True)
X = [tau, r, th, p1, p2]
v = tau + r
lam, TH = sp.symbols("lambda Theta", positive=True)


def g0_of(mu):
    m = mu/r**2
    g = sp.zeros(5)
    g[0, 0], g[0, 1], g[1, 0], g[1, 1] = -1 + m, m, m, 1 + m
    g[2, 2], g[3, 3], g[4, 4] = r**2, r**2*sp.cos(th)**2, r**2*sp.sin(th)**2
    return g


def D(e, a):
    """two-scale derivative: d_a + lam^-1 (d_a v) d_Theta, profiles depending on (X, Theta)"""
    return sp.diff(e, X[a]) + sp.diff(v, X[a])/lam*sp.diff(e, TH)


def theta_of(g, alpha, gi=None, gami=None):
    """theta_k = -gamma^AB Gamma^c_AB k_c for k = alpha dtau + dr, A, B over (th, p1, p2); gi, gami may be passed as
    truncated series"""
    gi = g.inv() if gi is None else gi
    k = [alpha, 1, 0, 0, 0]
    A = [2, 3, 4]
    if gami is None:
        gami = sp.Matrix([[g[a, b] for b in A] for a in A]).inv()
    tot = 0
    for i, a in enumerate(A):
        for j, b in enumerate(A):
            if gami[i, j] == 0:
                continue
            for c in range(5):
                if k[c] == 0:
                    continue
                Gam = sum(gi[c, d]*(D(g[d, b], a) + D(g[d, a], b) - D(g[a, b], d)) for d in range(5))/2
                tot += -gami[i, j]*Gam*k[c]
    return tot


def roots_g0(mu):
    """the two null covectors k = alpha dtau + dr of S_(v,r) for g0: alpha = -1 (k = dv - ... ) and the outgoing one"""
    g = g0_of(mu)
    gi = g.inv()
    al = sp.Symbol("al")
    k = sp.Matrix([al, 1, 0, 0, 0])
    sol = sp.solve(sp.expand((k.T*gi*k)[0, 0]), al)
    return [sp.simplify(s) for s in sol]


def h1(control=False):
    mu = sp.Symbol("mu", positive=True)
    g = g0_of(mu)
    sols = roots_g0(mu)
    # the ingoing null covector is dv (alpha = 1); the other is outgoing, with n = g^-1 k future directed, n(tau) = 1
    out = [s for s in sols if sp.simplify(s - 1) != 0]
    inn = [s for s in sols if sp.simplify(s - 1) == 0]
    if len(out) != 1 or len(inn) != 1:
        return False
    al = inn[0] if control else out[0]
    th0 = sp.simplify(theta_of(g, al))
    target = 3*(1 - mu/r**2)/(2*r)
    ratio = sp.simplify(th0/target)
    ok = sp.simplify(ratio - 2*r**2/(r**2 + mu)) == 0               # positive, no zero or pole for r > 0
    d = sp.simplify(sp.diff(target, r).subs(r, sp.sqrt(mu)))
    ok = ok and sp.simplify(d - 3/mu) == 0
    # n(tau) = 1 for the outgoing normal: future directed everywhere
    gi = g.inv()
    ok = ok and sp.simplify(gi[0, 0]*al + gi[0, 1] - 1) == 0 if not control else ok
    # the future ingoing normal is -g^-1 dv = L0; its expansion, -theta_(dv) = -3/r, is negative everywhere
    thin = -sp.simplify(theta_of(g, inn[0]))
    ok = ok and sp.simplify(thin + 3/r) == 0
    return bool(ok)


def h2(control=False):
    """g0 + lam W(X, Theta) with W tangent to the spheres and traceless on them, plus chi dv^2; explicit profiles with
    every argument present, the expansion taken exactly to order lam^0 (inverses to first order in lam suffice)"""
    mu = sp.Integer(1)
    s1 = sp.sin(TH)*(1 + r*tau) + th
    s2 = sp.cos(2*TH)*r + tau*th
    s3 = sp.sin(TH + th)*r**2
    chi = sp.cos(2*TH)*(r + tau**2)
    g0 = g0_of(mu)
    W = sp.zeros(5)
    # traceless on the sphere metric diag(r^2, r^2 c^2, r^2 s^2): two diagonal modes and an off-diagonal (th, p1) one
    W[2, 2] = r**2*(s1 + s2)
    W[3, 3] = -r**2*sp.cos(th)**2*s1
    W[4, 4] = -r**2*sp.sin(th)**2*s2
    W[2, 3] = W[3, 2] = r**2*sp.cos(th)*s3
    if control:
        W[2, 2] += r**2*s3                             # a trace on the spheres
    dvv = sp.Matrix([1, 1, 0, 0, 0])
    W = W + chi*dvv*dvv.T
    g = g0 + lam*W
    g0i = g0.inv()
    gi = g0i - lam*g0i*W*g0i
    A = [2, 3, 4]
    gam0i = sp.Matrix([[g0[a, b] for b in A] for a in A]).inv()
    Ws = sp.Matrix([[W[a, b] for b in A] for a in A])
    gami = gam0i - lam*gam0i*Ws*gam0i
    al0 = [s_ for s_ in roots_g0(mu) if sp.simplify(s_ - 1) != 0][0]
    al = sp.Symbol("al")
    k = sp.Matrix([al, 1, 0, 0, 0])
    a1 = sp.Symbol("a1")
    q1 = sp.expand((k.T*gi*k)[0, 0].subs(al, al0 + lam*a1))
    a1s = sp.solve(sp.expand(sp.series(q1, lam, 0, 2).removeO()).coeff(lam, 1), a1)
    alpha = al0 + lam*a1s[0]
    th_g = theta_of(g, alpha, gi=gi, gami=gami)
    th_0 = theta_of(g0, al0)
    pt = {tau: sp.Rational(1, 3), r: sp.Rational(7, 5), th: sp.Rational(2, 7), TH: sp.Rational(5, 11)}
    diff0 = sp.expand(th_g - th_0)
    lead = [sp.N(diff0.coeff(lam, n).subs(pt), 30) for n in (-1, 0)]
    return all(abs(x_) < 1e-20 for x_ in lead)


def h3(control=False):
    """d/dr of v at fixed v along a column is 0; along fixed tau it is 1"""
    s = sp.Symbol("s")
    v0 = sp.Symbol("v0")
    col = {tau: (s if control else v0 - s), r: s}
    return sp.simplify(sp.diff(v.subs(col), s)) == 0


CHECKS = [("H1 theta_out(g0) = 3 (1 - mu/r^2)/(2r) up to a positive factor; simple zero at sqrt(mu); ingoing < 0", h1),
          ("H2 a wave tangent and traceless on the spheres adds no O(1) term to the expansion", h2),
          ("H3 along a column the phase v/lam is constant", h3)]


def selftest():
    ok_all = True
    for name, f in CHECKS:
        good, control = f(), f(control=True)
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<100} {state}" + ("" if not control else "  (control passed: vacuous)"), flush=True)
    print(f"horizon5.py: {sum(1 for _ in CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    """each control, run as a mutant, must be caught"""
    caught = 0
    for name, f in CHECKS:
        m = f(control=True)
        caught += (not m)
        print(f"mutant of {name[:3]}: {'caught' if not m else 'NOT caught'}")
    print(f"horizon5.py mutants: {caught}/{len(CHECKS)}")
    return caught == len(CHECKS)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
