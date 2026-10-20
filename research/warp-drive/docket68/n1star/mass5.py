#!/usr/bin/env python3
"""mass5.py -- the mean-mass rate: after the shell, the mass of every sphere {v, r = const} of the metrics of Theorem 1
is mu + O(lam^2).  The exact facts the deduction uses (N1STAR-PROOF.md section 8, Proposition 8.2).

The mass of a 3-sphere S in a five-dimensional metric is its Hawking-type mass
    M[S] := R^2 (1 + (R^2/9) <Theta>),   Theta := 2 theta+ theta- / (-g(n+, n-)),   R := (Area(S)/(2 pi^2))^(1/3),
<.> the mean over S, n+-, the future null normals, theta+- their expansions; Theta does not depend on how n+- are
normalised.  M is natural: an isometry carrying S to itself leaves it unchanged.

  M1 (computed, exact) For five-dimensional Vaidya and S = S_(v,r) (tau = v - r, |x| = r):
     theta+ theta- / (-g(n+, n-)/2) = -9 (1 - mu/r^2)/r^2 and R = r, so M[S] = mu(v).  Control: the normalisation
     g(n+, n-) in place of -g(n+, n-)/2 gives a different value.
  M2 (computed, exact) The symmetry S'.  With sigma the isometry th -> pi/2 - th, phi1 <-> phi2 of S^3 (it swaps
     c = cos th and s = sin th, and fixes zeta = cos 2th up to sign, h(zeta) = h(-zeta)), and the phase reflection
     s -> 3 pi/2 - s, the record's first-order wave is odd: W_TT(sigma X, 3 pi/2 - s) = -W_TT(X, s) for
     P1 = A E H y^3 (2 c^2 cos s - s^2 sin s)/3, P2 = A E H y^3 (2 s^2 sin s - c^2 cos s)/3 (lead5.py's form),
     W_TT = r^2 diag(-2 (P1 + P2), 2 c^2 P1, 2 s^2 P2) on (th, phi1, phi2).  This is where the quarter turn between the
     two polarizations enters.  Controls: one quadrature alone (G = 0), and the two in phase, are not odd.
  M3 (computed, exact) The two-scale operator is equivariant: for any profile G(X, th), with G~(X, th) := G(X, c0 - th),
     Ric with d_a -> d_a + lam^-1 (d_a v) d_th satisfies R[G~](X, th; -lam) = R[G](X, c0 - th; lam).  Checked on a
     three-dimensional metric with a sample profile.  Control: c0 - th replaced by c0 + th breaks it.
  M4 (computed, exact) sigma is an isometry of g0 fixing tau, r and v, so it maps every S_(v,r) to itself.  Control:
     th -> pi/2 - th without exchanging phi1 and phi2 is not an isometry.

python3 mass5.py [--selftest | --mutants]
"""
import sys

import sympy as sp

tau, r, th, p1, p2 = sp.symbols("tau r theta phi1 phi2", real=True)
X = [tau, r, th, p1, p2]
v = tau + r


def g0_of(mu):
    m = mu/r**2
    g = sp.zeros(5)
    g[0, 0], g[0, 1], g[1, 0], g[1, 1] = -1 + m, m, m, 1 + m
    g[2, 2], g[3, 3], g[4, 4] = r**2, r**2*sp.cos(th)**2, r**2*sp.sin(th)**2
    return g


def theta_k(g, k):
    """expansion of S_(v,r) along n = g^-1 k, k in span{dtau, dr}: -gamma^AB Gamma^c_AB k_c"""
    gi = g.inv()
    A = [2, 3, 4]
    gami = sp.Matrix([[g[a, b] for b in A] for a in A]).inv()
    tot = 0
    for i, a in enumerate(A):
        for j, b in enumerate(A):
            if gami[i, j] == 0:
                continue
            for c in range(5):
                if k[c] == 0:
                    continue
                Gam = sum(gi[c, d]*(sp.diff(g[d, b], X[a]) + sp.diff(g[d, a], X[b]) - sp.diff(g[a, b], X[d]))
                          for d in range(5))/2
                tot += -gami[i, j]*Gam*k[c]
    return sp.simplify(tot)


def m1(control=False):
    mu = sp.Function("mu")(v)
    g = g0_of(mu)
    gi = g.inv()
    m = mu/r**2
    kp = [(m - 1)/(m + 1), 1, 0, 0, 0]                         # outgoing, n+ = g^-1 kp future directed
    km = [-1, -1, 0, 0, 0]                                     # -dv: n- = -g^-1 dv = L0, future directed
    tp, tm = theta_k(g, kp), theta_k(g, km)
    kpv, kmv = sp.Matrix(kp), sp.Matrix(km)
    gnn = sp.simplify((kpv.T*gi*kmv)[0, 0])                    # g(n+, n-) = g^-1(kp, km)
    norm = gnn if control else -gnn/2
    Theta = sp.simplify(tp*tm/norm)
    ok = sp.simplify(Theta + 9*(1 - mu/r**2)/r**2) == 0
    R = r                                                      # area of S_(v,r) is 2 pi^2 r^3 for g0
    M = sp.simplify(R**2*(1 + R**2*Theta/9))
    return bool(ok and sp.simplify(M - mu) == 0)


def wave(F, G, c, s_):
    y3 = r**sp.Rational(-3, 2)
    P1 = y3*(2*c**2*G - s_**2*F)/3
    P2 = y3*(2*s_**2*F - c**2*G)/3
    return sp.diag(-2*(P1 + P2), 2*c**2*P1, 2*s_**2*P2)*r**2


def m2(control=0):
    """control 1: one quadrature (G = 0); 2: the two in phase (both sin)"""
    ph = sp.Symbol("s", real=True)
    A, E = sp.symbols("A E", positive=True)
    z = sp.cos(2*th)
    H = sp.sqrt(2/(1 + z**2))
    F = A*E*H*sp.sin(ph)
    G = A*E*H*(0 if control == 1 else (sp.sin(ph) if control == 2 else sp.cos(ph)))
    c, s_ = sp.cos(th), sp.sin(th)
    W = wave(F, G, c, s_)
    # the transformed wave: (sigma^* W)(X, 3 pi/2 - s); sigma swaps c and s, the th-th component keeps its slot
    # (d th -> -d th, squared), and the phi1-phi1 and phi2-phi2 slots are exchanged
    sub = {th: sp.pi/2 - th, ph: 3*sp.pi/2 - ph}
    Wt = W.subs(sub, simultaneous=True)
    Ws = sp.diag(Wt[0, 0], Wt[2, 2], Wt[1, 1])
    return all(sp.simplify(sp.expand_trig(Ws[i, i] + W[i, i])) == 0 for i in range(3))


def m3(control=False):
    """R[G~](X, th; -lam) = R[G](X, c0 - th; lam) for the two-scale Ricci tensor of a 3-metric"""
    t, x, y, TH, lam, c0 = sp.symbols("t x y Theta lambda c0", real=True)
    Y = [t, x, y]
    vv = t + x                                                 # a null phase of the base metric is not needed here

    def D(e, a, lm):
        return sp.diff(e, Y[a]) + sp.diff(vv, Y[a])/lm*sp.diff(e, TH)

    def ric(g, lm):
        n = 3
        gi = g.inv()
        G = [[[sum(gi[a, m]*(D(g[m, b], c, lm) + D(g[m, c], b, lm) - D(g[b, c], m, lm)) for m in range(n))/2
               for c in range(n)] for b in range(n)] for a in range(n)]
        R = sp.zeros(n)
        for b in range(n):
            for c in range(n):
                R[b, c] = (sum(D(G[a][b][c], a, lm) - D(G[a][b][a], c, lm) for a in range(n))
                           + sum(G[a][a][m]*G[m][b][c] - G[a][c][m]*G[m][b][a] for a in range(n) for m in range(n)))
        return R
    g = sp.diag(-1, 1, 1) + sp.Matrix([[t*x/7, sp.sin(TH)*y/5, 0], [sp.sin(TH)*y/5, sp.cos(2*TH)*t/3, x/11],
                                       [0, x/11, sp.sin(TH)*sp.cos(TH)*x/4]])
    arg = c0 + TH if control else c0 - TH
    gt = g.subs(TH, arg)
    lhs = ric(gt, -lam)
    rhs = ric(g, lam).subs(TH, c0 - TH)
    pt = {t: sp.Rational(1, 5), x: sp.Rational(1, 3), y: sp.Rational(2, 7), TH: sp.Rational(3, 7),
          lam: sp.Rational(1, 9), c0: sp.Rational(11, 13)}
    return all(abs(sp.N((lhs[i, j] - rhs[i, j]).subs(pt), 30)) < 1e-25 for i in range(3) for j in range(3))


def m4(control=False):
    mu = sp.Symbol("mu", positive=True)
    g = g0_of(mu)
    gs = g.subs(th, sp.pi/2 - th)
    # sigma: th -> pi/2 - th, phi1 <-> phi2: swap the phi1 and phi2 rows and columns (the control does not swap)
    P = sp.eye(5)
    if not control:
        P[3, 3] = P[4, 4] = 0
        P[3, 4] = P[4, 3] = 1
    gpull = P*gs*P
    return sp.simplify(gpull - g) == sp.zeros(5)


CHECKS = [("M1 the mass of the Vaidya spheres S_(v,r) is mu(v)", m1, 1),
          ("M2 the record's wave is odd under sigma and s -> 3 pi/2 - s (the quarter turn)", m2, 2),
          ("M3 the two-scale operator: R[G(., c0 - th)](-lam) = R[G](c0 - th; lam)", m3, 1),
          ("M4 sigma (th -> pi/2 - th, phi1 <-> phi2) is an isometry of g0 fixing each S_(v,r)", m4, 1)]


def selftest():
    ok_all = True
    for name, f, nc in CHECKS:
        good = f()
        control = any(f(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<100} {state}" + ("" if not control else "  (control passed: vacuous)"), flush=True)
    print(f"mass5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, f, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            m = f(control=k)
            caught += (not m)
            print(f"mutant {k} of {name[:2]}: {'caught' if not m else 'NOT caught'}")
    print(f"mass5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
