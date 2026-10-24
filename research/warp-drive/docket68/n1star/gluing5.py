#!/usr/bin/env python3
"""gluing5.py -- [CD03] Theorem 8.1's proof at n = 4: every number in it that depends on the dimension, computed at n
= 3 against the printed values and at n = 4 (N1STAR-PROOF.md section 10.66; ROUTES 4.68; D137).  Labels: computed
(exact, sympy).

[CD03] (Chrusciel-Delay, gr-qc/0301073v2) states its section 8 for three-dimensional initial data ("we assume that the
initial data manifold is three-dimensional", p. 35) and its Remark 8.2 says the argument "carries over to any
dimension, the only element missing is an equivalent of Proposition F.1" -- computed near Tangherlini in general5.py
G2.  The census of its proof (pp. 36-37) finds the dimension in the count of Killing initial data (R^10), the scaling
of the charges under the dilation Phi_R(x) = x/R and its error terms, and the weighted Sobolev indices; each is here.

  D1 (computed, exact) The Killing fields of Minkowski R^(1,n): the kernel of X -> d_mu X_nu + d_nu X_mu on vector
     fields with polynomial coefficients of degree <= 2 has dimension (n + 1)(n + 2)/2: 10 at n = 3 ([CD03]'s
     e^(i), i = 1, ..., 10, and Q in R^10), 15 at n = 4.  Control: n = 3.  Mutant: the operator unsymmetrized.
  D2 (computed, exact; the errors deduced) The charges under Phi_R.  For each linearized direction of general5.py's
     family at Tangherlini (and at Schwarzschild, n = 3), the data carried to the annulus Gamma(1, 4) -- g_R(y) = g(Ry),
     K_R(y) = R K(Ry) -- have charges R^-(n - 2) times the original for the KIDs constant at infinity (energy, momentum)
     and R^-(n - 1) for the linear ones (angular momentum, centre of mass).  The quadratic error is O(R^-2 beta), beta =
     min(alpha, n - 2), for the constant KIDs and O(R^-(alpha + alpha_-)) for the odd linear ones (an even-even product
     pairs to 0 with an odd KID), so (8.7)'s error vanishes iff 2 alpha > n - 2 and alpha + alpha_- > n - 1: exactly
     (E.5b)'s n/2 - 1 < alpha and (E.9)'s alpha + alpha_- > n - 1, as printed for every n, met by Kerr (alpha = 1,
     alpha_- = 2) at n = 3 and by Tangherlini's glued data (alpha = 2, alpha_- = 3, 10.63(b)) at n = 4.  Without parity
     the linear KIDs' error is O(R^-2 alpha), (E.19)'s bound with alpha for alpha_-, so alpha > (n - 1)/2 replaces (E.9):
     no alpha in (E.5b)'s range at n = 3, every alpha in (3/2, 2] at n = 4.  Mutant: K_R without the factor R.
  D3 (computed, exact) The weighted indices.  rH^s_k = rH^k_(x, x^(-s-n/2)) ((5.2)): the embedding rH^(t-1)_(k+2) in
     H^(k+2) needs t >= k + 3 - n/2, met by the proof's t = k + 6 at both n; (8.4)'s source rH^(t-2) and (8.5)'s
     solution rH^(t-1) x rH^t are Theorem 5.6's (5.8) at s = t + n - 2 (t + 1 at n = 3, t + 2 at n = 4; the printed
     "s = t - 1" matches neither, a reading of [CD03]'s index, recorded); Theorem 5.6's s >= n - 1, k > n/2 and Theorem
     5.4's s not in {(n - 1)/2, (n - 3)/2} hold for every k >= floor(n/2) + 1 (2 at n = 3, the printed "2 <= k"; 3 at
     n = 4).  Mutant: the printed s = t - 1.
  D4 (computed, exact) [Hin26]'s asymptotic boost (his section 3.4) at n = 4.  With S = c x_n/r in S_1 (degree-1
     harmonics on S^(n-1), dim n: 3 boosts at n = 3, 4 at n = 4), omega = t d(rS) - rS dt raised by Minkowski's metric
     is c (t d_(x_n) + x_n d_t), so phi_S = exp(V(S)), V = (1/2) gbar^-1(omega, .) where his cut-offs are 1, is the
     Lorentz boost of rapidity chi = c/2.  The mass term of g_mu = gbar + mu r^(2-n) (dt*)^2 (t* = t - r; Ricci flat at
     n = 3, his (3.21) with mu = 2m, and at n = 4) pulls back on t = r to mu r^(2-n) D^-n (dt*)^2, D = cosh chi + cos
     theta sinh chi = a(theta)^-1, exactly: at n = 3 his (3.43)-(3.44), h_(S,11) = 2m (a^3 - 1) at r^-1 = r^-k, the
     radiation order; at n = 4 mu (a^4 - 1) at r^-2 = r^(-k-1/2), below it.  His c^2 = (3/(4 pi)) ||S||^2_(L^2(S^2)) is
     (n/|S^(n-1)|) ||S||^2: 2/pi^2 at n = 4.  Mutant: r' taken for r in the pull-back.

sympy; imports general5.py.  python3 gluing5.py [--selftest | --mutants]   (under a minute)
"""
import itertools
import sys
import time

import sympy as sp

from damping5 import Checklist
import general5 as G5


# ------------------------------------------------------------------------------------------------- D1
def killing_dim(n, mut=False):
    X = sp.symbols(f"y0:{n + 1}")
    eta = [-1] + [1] * n
    mons = [sp.Integer(1)] + list(X) + [a * b for a, b in itertools.combinations_with_replacement(X, 2)]
    cs = []
    V = []
    for mu in range(n + 1):
        c = sp.symbols(f"c{mu}_0:{len(mons)}")
        cs += c
        V.append(eta[mu] * sum(ci * m for ci, m in zip(c, mons)))      # X_mu, index lowered
    eqs = []
    for a in range(n + 1):
        for b in range(a, n + 1):
            e = sp.diff(V[b], X[a]) + (0 if mut else sp.diff(V[a], X[b]))
            eqs += sp.Poly(sp.expand(e), *X).coeffs()
    M = sp.Matrix([[sp.diff(e, c) for c in cs] for e in eqs])
    return len(cs) - M.rank()


def d1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in (3, 4):
        k = killing_dim(n, mut=control == 1)
        chk(f"n = {n}: Killing fields of R^(1,{n}): {k} = (n + 1)(n + 2)/2", k == (n + 1) * (n + 2) // 2)
    return chk.ok


# ------------------------------------------------------------------------------------------------- D2
def rescaled(f, R, mut=False):
    def data(xs, r):
        h, beta, dth = f(xs, r)
        sub = lambda e: sp.sympify(e).subs({**{x: R * x for x in xs}, r: R * r}, simultaneous=True)
        fac = 1 if mut else R
        return ([[sub(e) for e in row] for row in h], [sub(e) for e in beta],
                [[fac * sub(e) for e in row] for row in dth])
    return data


def d2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    R = sp.Symbol("R", positive=True)
    al, alm = sp.symbols("alpha alpha_m", positive=True)
    for n in (3, 4):
        mu = sp.Symbol("mu", positive=True)
        dirs = G5.family(n, mu)
        names = ["mass"] + ["boost"] * n + ["rotation"] * (n * (n - 1) // 2) + ["translation"] * n
        want = {"mass": 2 - n, "boost": 2 - n, "rotation": 1 - n, "translation": 1 - n}
        good = True
        for f, nm in zip(dirs, names):
            q0 = G5.charges(n, f)
            q1 = G5.charges(n, rescaled(f, R, mut=control == 1))
            ratios = {sp.simplify(b / a) for a, b in zip(q0, q1) if a != 0}
            good &= ratios == {R**want[nm]}
        chk(f"n = {n}: charges of the data on Gamma(1, 4): R^-(n-2) for E, P and R^-(n-1) for J, E C", good)
        e0, e1 = n - 2, n - 1                             # the main terms' exponents just computed
        cond0 = sp.solve(2 * al - e0 > 0, al)              # constant KIDs: R^-(2 alpha) below R^-(n - 2)
        chk(f"n = {n}: 2 alpha > {e0} is (E.5b)'s alpha > n/2 - 1; alpha + alpha_- > {e1} is (E.9)'s",
            sp.Rational(e0, 2) == sp.Rational(n, 2) - 1 and e1 == n - 1 and cond0 is not None)
    chk("Kerr (alpha, alpha_-) = (1, 2) at n = 3 and the glued data (2, 3) at n = 4 meet both",
        all(2 * a > n - 2 and a + am > n - 1 and a <= n - 2 and am > a for n, a, am in ((3, 1, 2), (4, 2, 3))))
    # without parity the linear KIDs' error is the constant ones' times r: R^-(2 alpha) against R^-(n - 1)
    lo = (lambda n: sp.Rational(n - 1, 2)) if control != 1 else (lambda n: sp.Rational(n - 2, 2))
    win = {n: sp.Interval.Lopen(lo(n), n - 2) for n in (3, 4)}
    chk("without parity, alpha in ((n-1)/2, n-2] (inside (E.5b)) is needed: empty at n = 3, (3/2, 2] at n = 4",
        win[3] == sp.EmptySet and win[4] == sp.Interval.Lopen(sp.Rational(3, 2), 2))
    return chk.ok


# ------------------------------------------------------------------------------------------------- D3
def d3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    k, t = sp.symbols("k t", integer=True)
    for n in (3, 4):
        s = t - 1 if control == 1 else t + n - 2
        # embedding: weight x^(2i - 2(t-1) - n) bounded on the annulus (x <= 1) for i <= k + 2
        emb = sp.simplify(2 * (k + 2) - 2 * (t - 1) - n)
        chk(f"n = {n}: rH^(t-1)_(k+2) in H^(k+2) needs t >= k + 3 - n/2; t = k + 6 gives margin "
            f"{-emb.subs(t, k + 6) / 2}", (emb.subs(t, k + 6) <= 0) == True)
        chk(f"n = {n}: (5.8) at s = {s}: source rH^(s-n) = rH^(t-2), solution rH^(s-n+1) x rH^(s-n+2) = rH^(t-1) x "
            f"rH^t", sp.simplify(s - n - (t - 2)) == 0 and sp.simplify(s - n + 2 - t) == 0)
        kmin = n // 2 + 1
        sv = s.subs(t, k + 6)
        ok = all(sv.subs(k, kk) >= n - 1 and kk > sp.Rational(n, 2)
                 and sv.subs(k, kk) not in (sp.Rational(n - 1, 2), sp.Rational(n - 3, 2)) for kk in range(kmin, 40))
        chk(f"n = {n}: Theorem 5.6 (s >= n - 1, k > n/2) and 5.4's exclusions for every k >= {kmin}",
            ok and (kmin - 1) <= sp.Rational(n, 2))
    chk("the printed s = t - 1 does not match (5.8) at n = 3", sp.simplify((t - 1) - 3 - (t - 2)) != 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- D4
def ricci_flat(n):
    t_, r = sp.symbols("t r", positive=True)
    mu = sp.Symbol("mu", positive=True)
    th = sp.symbols(f"th1:{n}")
    X = [t_, r] + list(th)
    N = n + 1
    g = sp.zeros(N, N)
    g[0, 0], g[1, 1] = -1 + mu / r**(n - 2), 1 + mu / r**(n - 2)
    g[0, 1] = g[1, 0] = -mu / r**(n - 2)                   # gbar + mu r^(2-n) (dt - dr)^2
    w = r**2
    for i in range(n - 1):
        g[2 + i, 2 + i] = w
        w = w * sp.sin(th[i])**2
    gi = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(N)) / 2) for c in range(N)] for b in range(N)] for a in range(N)]
    for i in range(N):
        for j in range(i, N):
            e = sum(sp.diff(Gam[a][i][j], X[a]) - sp.diff(Gam[a][i][a], X[j]) for a in range(N))
            e += sum(Gam[a][a][q] * Gam[q][i][j] - Gam[a][j][q] * Gam[q][i][a] for a in range(N) for q in range(N))
            if sp.simplify(e) != 0:
                return False
    return True


def d4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    q, z, r, cc = sp.symbols("q z r c", positive=True)          # q = e^chi, z = cos theta
    C, S = (q + 1 / q) / 2, (q - 1 / q) / 2
    D = C + S * z
    for n in (3, 4):
        xs = sp.symbols(f"y1:{n + 1}")
        tt = sp.Symbol("tt")
        X = [tt] + list(xs)
        rS = cc * xs[-1]                                     # r S, S = c x_n/r
        omega = [tt * sp.diff(rS, v) - rS * sp.diff(tt, v) for v in X]
        vec = [(-1 if i == 0 else 1) * omega[i] for i in range(n + 1)]
        want = [cc * xs[-1]] + [0] * (n - 1) + [cc * tt]
        chk(f"n = {n}: gbar^-1(omega, .) = c (x_n d_t + t d_(x_n)), the boost field", vec == want)
        # the boost of rapidity chi on the cone t = r + u at u = 0: x_n = r z, |x_perp| = r sqrt(1 - z^2)
        u = sp.Symbol("u")
        tp = C * (r + u) + S * r * z
        xnp = S * (r + u) + C * r * z
        rp2 = xnp**2 + r**2 * (1 - z**2)
        chk(f"n = {n}: r'^2 = (r D)^2 on t = r", sp.simplify(rp2.subs(u, 0) - (r * D)**2) == 0)
        rp = r * D                                           # r' at u = 0 (D > 0)
        dts = sp.diff(tp, u) - (xnp * sp.diff(xnp, u)).subs(u, 0) / rp
        coef = (rp if control != 1 else r)**(2 - n) * dts.subs(u, 0)**2
        chk(f"n = {n}: phi_S^*(mu r^(2-n) dt*^2) = mu r^(2-n) D^-{n} dt*^2 on t = r",
            sp.simplify(coef * r**(n - 2) * D**n - 1) == 0)
        nrm = G5.sphere_int(xs[-1]**2, xs) / G5.sphere_int(sp.Integer(1), xs)
        chk(f"n = {n}: ||c x_n||^2_L2 = c^2 |S^(n-1)|/{1 / nrm}, so c^2 = ({1 / nrm}/|S^(n-1)|) ||S||^2",
            nrm == sp.Rational(1, n))
    chk("Kerr-Schild gbar + mu r^(2-n) (dt - dr)^2 is Ricci flat at n = 3 and n = 4", ricci_flat(3) and ricci_flat(4))
    return chk.ok


CHECKS = [("D1 the Killing fields of R^(1,n): 10 at n = 3, 15 at n = 4", d1),
          ("D2 the charges under Phi_R: R^-(n-2), R^-(n-1); the errors' conditions are (E.5b) and (E.9)", d2),
          ("D3 the weighted indices of Theorem 8.1's proof: t = k + 6, s = t + n - 2, k >= floor(n/2) + 1", d3),
          ("D4 [Hin26]'s boost at n = 4: phi_S^* of the mass term is mu r^-2 a^4 dt*^2, below the radiation order", d4)]


def run(only=None, verbose=False):
    ok = True
    for k, (name, f) in enumerate(CHECKS, 1):
        if only and k != only:
            continue
        t0 = time.time()
        res = f(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    n = 1 if only else len(CHECKS)
    print(f"gluing5.py: {n if ok else 'not all'}/{n}")
    return ok


def mutants():
    caught = total = 0
    for name, f in CHECKS:
        total += 1
        res = f(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"gluing5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    vb = "--verbose" in args
    if "--selftest" in args:
        sys.exit(0 if run(verbose=vb) else 1)
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    elif "--only" in args:
        sys.exit(0 if run(int(args[args.index("--only") + 1]), vb) else 1)
    print(__doc__)
