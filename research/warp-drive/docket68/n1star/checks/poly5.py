"""poly5.py -- SETTLE-GLAM5 round 3, (Poly): the powers of lam in the record's fixed-lam expansion at past null
infinity (Lemma 11.0, Lemma 11.2, Proposition 11.1 of N1STAR-PROOF.md), carried through every step.

Notation. A profile is f(X, th) at phase th = v/lam (N1STAR-PROOF.md:80-85); "order" of a bound = the exponent e in
C lam^(-e); u_1 := g_lam - g0 - r^(-3/2) G_3 on the far region t >= T = lam^-2; K_0 := 6 (Theorem P at K = 6 serves
every K, g_lam being unique, (P-v)).

  P1 (exact) the two-scale chain rule: for F = lam^j A(X) sin th, every Cartesian derivative costs exactly one
     power of lam (D^alpha F has lowest order lam^(j - |alpha|), attained), and a rotation costs none (Omega v = 0);
     the two-scale formula agrees with the true derivative of A(X) sin(v(X)/lam). Control: x1 d_2 + x2 d_1 (not a
     rotation, it moves v) costs lam^-1.
  P2 (exact) the coefficients of Lemma 11.0's energy identity: d(lam [W]) has order 0 (lam-free sup, so the
     kernel ||d g_n|| <= C t^(-3/2) is lam-free); and S(u) of (11.4) contains -(1/2) lam^-1 u(ell, ell) [d_th^2 W]
     exactly at order -1, because (g^-1 - g0^-1)(dv, dv) = -u(ell, ell) + O(u^2) (5D Kerr-Schild g0): a term of F_1
     linear in u_1 with coefficient lam^-1 t^(-3/2), at the top order of the induction, which Lemma 9.5's kernel must
     absorb. Control: the d_t d_t component of (g^-1 - g0^-1) is not -u(ell, ell).
  P3 (exact) the Gronwall factors: on t >= lam^-2, exp(int C t^(-3/2)) = exp(2 C lam) and exp(int C lam^-1 t^(-3/2))
     = exp(2 C): lam-free. Control: the same lam^-1 kernel over the near region [1, lam^-2] gives exp(2C(lam^-1 - 1)),
     which beats every lam^-M.
  P4 (exact) the data constants C(lam, j) of Lemma 11.0: in a 1+1 model of the record's equation for w_n
     (oscillating coefficients g^-1 - g0^-1 in lam E, the 1/lam coupling of (3.2), quadratic terms, residual
     lam^(N-1) [R]), with w = d_tau w = 0 on the initial slice, d_tau^m w there has order exactly N + 1 - m
     (m = 2..6, N = 6): one lam^-1 per derivative, polynomial. Control: "order N - 1 at every m" fails at m = 3.
  P5 (exact, integer recursion) Lemma 11.0 as written: energies at order n carry lam^-P(n), pointwise bounds
     lam^-Q(n); Theorem P (K_0 = 6, k = 6) gives P(n) = n (n <= 6), Q(n) = n - 1 (n <= 4); the data P = n; the
     sources are products with the highest-order factor in L^2 and the others in sup, Q(n) = P(n + 2) by Lemma 9.3
     (the cost of three). P(N) is finite at every N and grows: computed to N = 40 (P(40) and the doubling recorded).
     The record's split inequality floor((N + 2)/2) <= max(4, N - 3) holds for N >= 1. Control: the reverse split
     (the high factor in sup) needs a pointwise order not yet controlled, at every N >= 6.
  P6 (exact, integer recursion) the sharp reading: u_1 = a + w, a := g_app - g0 - r^(-3/2) G_3 explicit (order
     n - 1 at derivative order n, no Sobolev), w at order -(K'_0 - 2) + n (Proposition 9.8 read at order k, as 10.51
     reads section 4; lam <= lam_F(k)): the same recursion closes at P(N) = N, Q(N) = N - 1 for every N <= 40.
     Control: with K'_0 = 5 the scaled bootstrap's quadratic term lam^(2K'-5) does not beat lam^K'.
  P7 (exact, integer recursion) Lemma 11.2 and Proposition 11.1: e(G_3) = -1, e(G_4) = 0 and the monomial bound give
     e(G_k) <= k - 4 (k = 4..30, a fixed point of the recursion); the remainder u_J then has pointwise order
     M(J, n, m) at n Cartesian/rotation derivatives and m ell-derivatives; the recursion is run for J <= 24, n <= 12,
     m <= 4 and M(J, n, m) <= n + m + (J^2 + 3J)/2 - 9 holds there (computed bound; equality recorded where it is).
     Control: no bound linear in J with slope 3 holds (M(24, 0, 0) exceeds 3 * 24).
  P8 (exact) smallness with commutations: on N, Z = r ell; below R = lam^-s the record's lam-uniform bounds
     |d^i e| <= C lam^(K'-3-i) r^-2 (no ell-gain) and above R (11.7) at order J' with its ell-gains: the weighted
     flux of Z^j d(e's remainder) is at most C(lam^(2(K'-3-j) - s(2a + 2j - 2)) + lam^(2(-M) + s(J' - 1 - 2a))), so it
     tends to 0 once K' > 3 + j + s(a + j - 1) with s = (2M + 1)/(J' - 1 - 2a); sampled exactly. Control: above R
     without the ell-gain the flux of Z^j d e diverges for j >= 1 at a = 11/4.
Labels: computed (exact; sympy and integer arithmetic).

    python3 checks/poly5.py
"""
import sys
from functools import lru_cache

import sympy as sp

FAIL = []


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


lam = sp.Symbol("lambda", positive=True)
Li = sp.Symbol("Li", positive=True)  # stands for 1/lam in the two-scale derivatives
t, x1, x2, x3, x4, th = sp.symbols("t x1 x2 x3 x4 theta", real=True)
XS = [t, x1, x2, x3, x4]
R = sp.sqrt(x1**2 + x2**2 + x3**2 + x4**2)
V = t + R


def lam_order(expr, B=40):
    """lowest power of lam in a Laurent polynomial in lam (coefficients free of lam)"""
    e = sp.expand(expr*lam**B)
    if e == 0:
        return sp.oo
    P = sp.Poly(e, lam)
    degs = [m[0] for m, c in zip(P.monoms(), P.coeffs()) if sp.simplify(c) != 0]
    if not degs:
        return sp.oo
    return min(degs) - B


def D(expr, a, vfield=None):
    """two-scale derivative along a coordinate (a int) or along a vector field (list of 5 coefficients);
    Li stands for 1/lam"""
    if vfield is None:
        return sp.diff(expr, XS[a]) + sp.diff(V, XS[a])*Li*sp.diff(expr, th)
    return sum(c*(sp.diff(expr, XS[i]) + sp.diff(V, XS[i])*Li*sp.diff(expr, th)) for i, c in enumerate(vfield)
               if c != 0)


PTS = [{t: sp.Rational(1, 3), x1: sp.Rational(7, 5), x2: sp.Rational(-2, 3), x3: sp.Rational(5, 4),
        x4: sp.Rational(1, 2), th: sp.Rational(3, 7)},
       {t: sp.Rational(-2, 5), x1: sp.Rational(1, 2), x2: sp.Rational(9, 4), x3: sp.Rational(-1, 3),
        x4: sp.Rational(6, 5), th: sp.Rational(11, 5)}]


def nonzero(c):
    """a coefficient is nonzero if it is nonzero at one of two rational points (30 digits)"""
    return any(abs(sp.N(c.subs(p), 30)) > 1e-20 for p in PTS)


def order_L(expr, j=0):
    """lam-order of lam^j * expr, expr a polynomial in Li = 1/lam: j - (top Li-degree with nonzero coefficient)"""
    P = sp.Poly(sp.expand(expr), Li)
    degs = [m[0] for m, c in zip(P.monoms(), P.coeffs()) if nonzero(c)]
    return j - max(degs) if degs else sp.oo


def top_L(expr):
    P = sp.Poly(sp.expand(expr), Li)
    d = P.degree()
    return d, P.coeff_monomial(Li**d)


def p1():
    print("P1  the two-scale chain rule: one lam^-1 per Cartesian derivative, none per rotation")
    A = 1 + t*x1 + x2**2*x3 + x4*t**2  # an explicit slow amplitude
    j = 1
    F = A*sp.sin(th)  # times lam^j
    ok = True
    for alpha in ((0,), (1,), (0, 2), (0, 1, 3), (1, 1, 4)):
        e = F
        for a in alpha:
            e = D(e, a)
        o = order_L(e, j)
        ok = ok and o == j - len(alpha)
    check("P1a D^alpha (lam A sin th) has order 1 - |alpha| exactly (five multi-indices up to order 3)", ok)
    Om = [0, -x2, x1, 0, 0]  # x1 d_2 - x2 d_1
    e = D(D(F, None, Om), None, Om)
    check("P1b two rotations: order still 1 (Omega v = 0)", order_L(e, 1) == 1)
    # validate the two-scale formula against the true derivative of A sin(v/lam)
    true = sp.diff(A*sp.sin(V/lam), x1, t)
    two = D(D(A*sp.sin(th), 0), 1).subs({th: V/lam, Li: 1/lam})
    lv = {lam: sp.Rational(1, 7)}
    diffs = [abs(sp.N((true - two).subs(lv).subs({k: v for k, v in p.items() if k != th}), 30)) for p in PTS]
    check("P1c the two-scale formula equals the true d_1 d_t of A sin(v/lam) (two points, lam = 1/7)",
          max(diffs) < 1e-25)
    Nr = [0, x2, x1, 0, 0]  # x2 d_1 + x1 d_2: not a rotation
    e = D(F, None, Nr)
    check("P1d control: x2 d_1 + x1 d_2 (not a rotation) costs lam^-1: order 0", order_L(e, 1) == 0)


def ks():
    eta = sp.diag(-1, 1, 1, 1, 1)
    k = sp.Matrix([1, x1/R, x2/R, x3/R, x4/R])
    mu = sp.Symbol("mu", positive=True)
    g0 = eta + mu/R**2*k*k.T
    g0i = eta - mu/R**2*(eta*k)*(eta*k).T
    return g0, g0i, mu


def p2():
    print("P2  the coefficients of Lemma 11.0's energy identity")
    W = 1 + x1*x3 + t**2
    e = D(W*sp.sin(th), 0)
    check("P2a d_t (lam W sin th) has order 0: the kernel ||d g|| <= C t^(-3/2) is lam-free", order_L(e, 1) == 0)
    g0, g0i, mu = ks()
    check("P2b g0 g0^-1 = 1 (5D Kerr-Schild, det g0 = -1)",
          sp.simplify(g0*g0i - sp.eye(5)) == sp.zeros(5, 5) and sp.simplify(g0.det() + 1) == 0)
    eps = sp.Symbol("epsilon")
    us = sp.symbols("u0:15")
    U = sp.zeros(5, 5)
    idx = 0
    for i in range(5):
        for jj in range(i, 5):
            U[i, jj] = U[jj, i] = us[idx]
            idx += 1
    dv = sp.Matrix([1, x1/R, x2/R, x3/R, x4/R])  # dv = dt + dr = k
    ell = g0i*dv
    # first-order variation of the inverse: (g0 + eps U)^-1 = g0^-1 - eps g0^-1 U g0^-1 + O(eps^2)
    first = -(g0i*U*g0i)
    lhs = sp.simplify((dv.T*first*dv)[0, 0])
    rhs = sp.simplify(-(ell.T*U*ell)[0, 0])
    check("P2c (g^-1 - g0^-1)(dv, dv) = -u(ell, ell) + O(u^2), ell = g0^-1 dv", sp.simplify(lhs - rhs) == 0)
    # the quasilinear term of (11.4) on lam [W]: its lam^-1 part is (1/2)(g^-1 - g0^-1)^(ab) d_a v d_b v (-W sin th)
    Wf = 2 + t*x2 + x1**2
    Y = Wf*sp.sin(th)  # times lam
    hess = sp.Matrix(5, 5, lambda a, b: D(D(Y, a), b))
    Hm = sp.Matrix(5, 5, lambda a, b: sp.Symbol(f"H{min(a, b)}{max(a, b)}"))
    q = sp.expand(sum(Hm[a, b]*hess[a, b] for a in range(5) for b in range(5))/2)
    deg, lead = top_L(q)  # lam * Li^deg: order 1 - deg
    target = -sp.Rational(1, 2)*Wf*sp.sin(th)*sum(Hm[a, b]*sp.diff(V, XS[a])*sp.diff(V, XS[b])
                                                  for a in range(5) for b in range(5))
    hv = {sp.Symbol(f"H{a}{b}"): sp.Rational(a + 2*b + 1, 5) for a in range(5) for b in range(a, 5)}
    check("P2d (1/2) H^ab d_a d_b (lam [W]) = -(1/2) lam^-1 H(dv, dv) [W] + O(lam^0): with H(dv, dv) = -u(ell, ell)"
          " the term is +(1/2) lam^-1 u_1(ell, ell) [W], linear in u_1, at order -1",
          1 - deg == -1 and not nonzero((lead - target).subs(hv)))
    tt = sp.simplify((sp.Matrix([1, 0, 0, 0, 0]).T*first*sp.Matrix([1, 0, 0, 0, 0]))[0, 0] - rhs)
    check("P2e control: the dt dt component of (g^-1 - g0^-1) is not -u(ell, ell)", tt != 0)


def p3():
    print("P3  the Gronwall factors")
    C, tt, M = sp.symbols("C tt M", positive=True)
    k1 = sp.integrate(C*tt**sp.Rational(-3, 2), (tt, lam**-2, sp.oo))
    k2 = sp.integrate(C/lam*tt**sp.Rational(-3, 2), (tt, lam**-2, sp.oo))
    check("P3a far region: int C t^(-3/2) = 2 C lam, int C lam^-1 t^(-3/2) = 2 C (lam-free factors)",
          sp.simplify(k1 - 2*C*lam) == 0 and sp.simplify(k2 - 2*C) == 0, f"{k1}, {k2}")
    k3 = sp.integrate(C/lam*tt**sp.Rational(-3, 2), (tt, 1, lam**-2))
    lim = sp.limit(sp.exp(k3.subs(C, 1))*lam**M, lam, 0, "+")
    check("P3b control: over the near region [1, lam^-2] the lam^-1 kernel gives exp(2C(1/lam - 1)), beating every "
          "lam^-M", sp.simplify(k3 - 2*C*(1/lam - 1)) == 0 and lim == sp.oo, str(sp.simplify(k3)))


def p4():
    print("P4  the data constants: d_tau^m w on the initial slice (1+1 model, N = 6)")
    tau, x, q = sp.symbols("tau x q", real=True)
    N = 6
    thf = (tau + x)/lam
    a1, a2, a3, kap, beta, rho = [sp.Rational(c, 7) for c in (3, 2, 5, 4, 6, 1)]
    gtt = -1 + lam*a1*sp.cos(thf)
    gtx = lam*a2*sp.sin(thf)
    gxx = 1 + lam*a3*sp.cos(thf)
    Rres = lam**(N - 1)*rho*sp.sin(thf)
    cs = {0: sp.Integer(0), 1: sp.Integer(0)}
    orders = {}
    for m in range(2, 7):
        Wm = sum(cs[i]*tau**i/sp.factorial(i) for i in range(m))
        wx, wxx, wt, wtx = sp.diff(Wm, x), sp.diff(Wm, x, 2), sp.diff(Wm, tau), sp.diff(Wm, tau, x)
        rhs = (Rres + q*(wx**2 + Wm*wxx) - kap/(2*lam)*sp.cos(thf)*Wm - beta*sp.cos(thf)*wx
               + gtx*wtx + gxx*wxx/2)
        phi = -2*rhs/gtt
        cm = sp.diff(phi, tau, m - 2).subs(tau, 0)
        cs[m] = sp.simplify(cm.subs(q, 1))
        e = sp.simplify(cs[m].subs(x, lam*th))
        # order in lam: e is rational in lam with trig(th) coefficients; find the lowest power by series
        ser = sp.series(e, lam, 0, N + 2).removeO()
        orders[m] = lam_order(ser)
    print("     orders of d_tau^m w on the slice, m = 2..6:", [orders[m] for m in range(2, 7)])
    check("P4a d_tau^m w has order exactly N + 1 - m (one lam^-1 per derivative): polynomial",
          all(orders[m] == N + 1 - m for m in range(2, 7)))
    check("P4b control: the claim 'order N - 1 at every m' fails (m = 3)", orders[3] != N - 1)


# ---------------------------------------------------------------- integer recursions for Lemma 11.0

def partitions(total, parts, lo):
    """non-decreasing tuples of `parts` integers >= lo summing to total"""
    if parts == 1:
        if total >= lo:
            yield (total,)
        return
    for a in range(lo, total//parts + 1):
        for rest in partitions(total - a, parts - 1, a):
            yield (a,) + rest


def lemma110(Nmax, Pbase, Qbase, Qsup, sobolev=True, reverse=False):
    """energy exponents P(N) and pointwise exponents Q(n) of Lemma 11.0's induction.

    A source term at order N is a product of factors of u (explicit lam[W] or u_1) with derivative orders d_i,
    sum d_i = N + 2, the highest d_top <= N in L^2 (energy of order d_top - 1) and the others in sup; terms with
    d_top >= N + 1 or a factor with d <= 1 multiplying the top order are the kernel terms (lam-free on the far
    region, P3).  Qsup(d, Q) gives the sup exponent of a factor of order d."""
    P = dict(Pbase)
    Q = dict(Qbase)
    for N in range(max(P) + 1, Nmax + 1):
        best = N  # the data
        for parts in (2, 3, 4):
            for ds in partitions(N + 2, parts, 0):
                ds = sorted(ds)
                top = ds[-1]
                if top >= N + 1 or top < 1:
                    continue
                sups = ds[:-1]
                if reverse:
                    top, sups = ds[0], ds[1:]
                    if top < 1:
                        continue
                    need = max(sups)
                    if need not in Q:
                        return P, Q, ("uncontrolled", N, need)
                    val = sum(Qsup(d, Q) for d in sups) + P.get(top - 1, 0)
                else:
                    if any(d not in Q for d in sups):
                        return P, Q, ("uncontrolled", N, max(sups))
                    val = sum(Qsup(d, Q) for d in sups) + P[top - 1]
                best = max(best, val)
        P[N] = best
        n = N - 2
        if sobolev and n >= 0 and n not in Q:
            Q[n] = max(P[n + i] for i in range(0, 3))  # Lemma 9.3: d_r^i, i <= 3, energies of order <= n + 2
    return P, Q, None


def p5():
    print("P5  Lemma 11.0 as written: the exponent recursion")
    ok = all((N + 2)//2 <= max(4, N - 3) for N in range(1, 200))
    check("P5a the record's split: floor((N + 2)/2) <= max(4, N - 3) for N = 1..199", ok)
    Pbase = {n: n for n in range(0, 7)}
    Qbase = {n: n - 1 for n in range(0, 5)}
    P, Q, err = lemma110(40, Pbase, Qbase, lambda d, Qd: Qd[d])
    print("     P(N), N = 7..16:", [P[N] for N in range(7, 17)])
    print("     P(40) =", P[40], "; P(N+1)/P(N) at N = 39:", round(P[40]/P[39], 3))
    check("P5b finite at every order N <= 40 (polynomial in lam^-1 at each order, K-independent)",
          err is None and all(isinstance(P[N], int) for N in range(41)))
    grows = P[40] > 40 and P[40] > 2*P[34]
    check("P5c the exponent of the written bookkeeping is not linear (P(40) > 40, more than doubling per 6 orders)",
          grows, f"P(34) = {P[34]}, P(40) = {P[40]}")
    P2_, Q2_, err2 = lemma110(40, Pbase, Qbase, lambda d, Qd: Qd[d], reverse=True)
    check("P5d control: the reverse split asks for a pointwise order not yet controlled", err2 is not None,
          str(err2))


def p6():
    print("P6  the sharp reading u_1 = a + w (Proposition 9.8 at order k): natural exponents")
    K0p = 17  # K'_0 = K_0 + 3 + ceil(4 beta0) >= 6 + 3 + 8
    Pbase = {n: n for n in range(0, 7)}
    Qbase = {n: n - 1 for n in range(0, 5)}

    def qsharp(d, Qd):
        return max(d - 1, -(K0p - 2) + d)   # explicit a (no Sobolev), or w by Lemma 9.3 on (9.8) at order d + 3

    P, Q, err = lemma110(40, Pbase, {n: n - 1 for n in range(0, 41)}, qsharp, sobolev=False)
    check("P6a the recursion closes at P(N) = N for N <= 40 (Q(n) = n - 1 from a and w)",
          err is None and all(P[N] == N for N in range(41)))
    K = sp.Symbol("K", positive=True)
    ok = (2*K0p - 5 > K0p) and not (2*5 - 5 > 5)
    check("P6b the scaled bootstrap closes at K'_0 = 17 (2K' - 5 > K'); control: at K' = 5 it does not", ok)


# ---------------------------------------------------------------- Lemma 11.2 and Proposition 11.1

def eG(kmax):
    """lam-orders of the coefficients: e(G_3) = -1 (lam A env h sin), e(G_4) = 0 (2 int S_3); G_k = c int S_(k/2+1),
    whose monomials are a linear term on G_(k-2) with at most one d_v (Gamma[g0] d_v, coefficient r-gain 2) or none
    (the flat part, Delta-ring and ell ell), or products of 2 or 3 factors G_(k_i), 3 <= k_i <= k - 1,
    sum k_i <= k + 2, with at most two d_v (each d_v costs one power, an integral over [v_start, v] none)."""
    e = {3: -1, 4: 0}
    for k in range(5, kmax + 1):
        cands = [e[k - 2] + 1, e[k - 2]]
        for parts in (2, 3):
            for tot in range(3*parts, k + 3):
                for ks_ in partitions(tot, parts, 3):
                    if max(ks_) <= k - 1:
                        cands.append(sum(e[ki] for ki in ks_) + 2)
        e[k] = max(cands)
    return e


def stages(Jmax, e):
    """base orders B_J of the remainders u_J (pointwise order at n derivatives and m ell-derivatives is B_J + n + m).

    Stage J -> J + 1 is Lemma 11.2 at q = (J + 3)/2 on u~ = u_J:
      S~ (pointwise): terms linear in u_J with explicit coefficients, lam^-1 u_J(ell, ell) [W''] and d u_J d(lam W):
          B_J + 1; terms quadratic in u_J, one factor taken crudely, |d u_J| <= lam^-(crude + 1) r^-2 with
          crude = max(-1, e(G_k), k <= J): B_J + crude + 2; explicit G-monomials beyond order q: 2J - 6;
      S' adds (g^-1 - g0^-1) d^2 (r^(1-q) G_(J+1)): e(G_(J+1)) + 1, and box~(r^(1-q) G_(J+1)) - r^-q S_q: e(G_(J+1));
      energy (Lemma 9.5, lam-free Gronwall on the far region, P3; commutators natural, P6): the order of S';
      pointwise (Lemma 9.3): energies of two more orders, + 2;
      the ell-gain (transport (11.6), lam-free factor): f contains d_v u~~, + 1 per ell.
    u_3 = u_1 has B_3 = -1 (P6)."""
    B = {3: -1}
    for J in range(3, Jmax):
        crude = max([-1] + [e[k] for k in range(4, J + 1)])
        stil = max(B[J] + 1, B[J] + crude + 2, 2*J - 6)
        sprime = max(stil, e[J + 1] + 1, e[J + 1])
        B[J + 1] = sprime + 2
    return B


def p7():
    print("P7  Lemma 11.2 and Proposition 11.1: the coefficients and the remainders")
    e = eG(40)
    check("P7a e(G_k) = k - 4 for k = 4..40 (e(G_3) = -1): the monomial recursion's fixed point",
          all(e[k] == k - 4 for k in range(4, 41)), str([e[k] for k in range(3, 12)]))
    B = stages(40, e)
    closed = lambda J: (J*J - J)//2 - 1 if J >= 4 else -1
    print("     B_J, J = 3..12:", [B[J] for J in range(3, 13)])
    check("P7b B_J = (J^2 - J)/2 - 1 for J = 4..40: M(J, n, m) = B_J + n + m, polynomial, K-independent",
          all(B[J] == closed(J) for J in range(4, 41)))
    check("P7c control: no bound linear in J with slope 3 (B_24 > 72)", B[24] > 72, f"B_24 = {B[24]}")


# ---------------------------------------------------------------- M1: e's coefficients by interpolation

def p8():
    print("P8  the interpolation lemma: e's expansion coefficients from (P-iii) and (Poly)")
    # Lemma: P(s) = sum_(i<=d) c_i s^i with |P| <= eta on [sigma/2, sigma] has |c_i| <= L_d sigma^-i eta,
    # L_d := max_i ||row i of V^-1||_1 for the nodes 1/2 + j/(2d) (exact rationals).
    ok = True
    Ls = {}
    for d in (1, 2, 3, 4, 5):
        nodes = [sp.Rational(1, 2) + sp.Rational(j, 2*d) for j in range(d + 1)]
        Vm = sp.Matrix(d + 1, d + 1, lambda i, j: nodes[i]**j)
        Vi = Vm.inv()
        Ls[d] = max(sum(abs(Vi[i, j]) for j in range(d + 1)) for i in range(d + 1))
        # check on random polynomials, scaled to [sigma/2, sigma]
        import random
        random.seed(d)
        for _ in range(20):
            cs = [sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for _ in range(d + 1)]
            sig = sp.Rational(random.randint(1, 9), 10)
            vals = [sum(cs[i]*(sig*y)**i for i in range(d + 1)) for y in nodes]
            eta = max(abs(vv) for vv in vals)
            ok = ok and all(abs(cs[i]) <= Ls[d]*sig**(-i)*eta for i in range(d + 1))
    check("P8a |c_i| <= L_d sigma^-i max|P(nodes)| on 100 random polynomials (d = 1..5), L_4 = " + str(Ls[4]), ok)
    # optimisation: |c_(k)| <= 2 L (eps + B sigma^(J'-3)) sigma^-(k-4), sigma^(J'-3) = eps/B
    K, Mx, Jp = sp.symbols("K M Jp", positive=True)
    th_ = lambda k, J: sp.Rational(k - 4, J - 3)
    eps = lam**(K - 3)
    Bb = lam**(-Mx)
    sig = (eps/Bb)**(sp.Integer(1)/(Jp - 3))
    for k in (5, 6, 7, 8):
        bound = sp.powsimp(sp.expand_power_base(eps*sig**(-(k - 4)), force=True), force=True)
        expo = sp.simplify(sp.log(bound.subs(Jp, 8))/sp.log(lam))
        target = (K - 3)*(1 - th_(k, 8)) - Mx*th_(k, 8)
        ok = ok and sp.simplify(sp.expand(expo - target)) == 0
    check("P8b with J' = 8: |e_k| <= C lam^((K-3)(1 - th_k) - M th_k), th_k = (k - 4)/5, k = 5..8", ok)
    # sigma must lie in the far region: sigma <= s_0 = (2 lam^-2)^(-1/2)
    check("P8c sigma = lam^((K - 3 + M)/(J' - 3)) <= lam/sqrt(2) once K - 3 + M > J' - 3 (lam small)",
          sp.limit((lam**(sp.Rational(10 + 1, 5)))/(lam/sp.sqrt(2)), lam, 0, "+") == 0)
    # control: at a fixed radius (sigma fixed) the coefficient bound is only lam^-M
    fixed = sp.limit(lam**(-5)*(lam**(17) + lam**(-5)), lam, 0, "+")
    check("P8d control: without the optimisation (sigma fixed) the bound lam^-M (eps + B) does not tend to 0",
          fixed == sp.oo)


def kstar(a, Jp, Mx, j):
    """least K with every exponent of the commuted flux of e's remainder (subtraction through p = 4, k <= 8)
    positive, R = lam^-s, s = max(2, (2M + 1)/(J' - 1 - 2a)).
      (i)   e below R, j commutations (Z = r ell costs r):   2(K - 4 - j) - s(2a + 2j) > 0
      (ii)  coefficient e_k with i <= j + 1 d_v's, up to R:   2[(K - 3 - i)(1 - th_k) - (M + i) th_k]
                                                               - s max(0, 2a + 2 - k) > 0
      (iii) above R, (11.7) with ell-gains:                   -2M + s(J' - 1 - 2a) > 0 (holds by the choice of s)"""
    s = max(sp.Integer(2), (2*Mx + 1)/(Jp - 1 - 2*a))
    need = [4 + j + s*(a + j)]
    for k in range(4, 9):
        thk = sp.Rational(k - 4, Jp - 3)
        for i in range(0, j + 2):
            # (K - 3 - i)(1 - th) - (M + i) th > (s/2) max(0, 2a + 2 - k)
            rhs = s*max(0, 2*a + 2 - k)/2
            if thk == 1:
                continue
            need.append(3 + i + (rhs + (Mx + i)*thk)/(1 - thk))
    return s, max(need)


def p9():
    print("P9  the threshold K* for the commuted flux of e's remainder below and above R (replaces R2.10's K)")
    rr = sp.Symbol("rr", positive=True)
    ok = True
    for a, Jp, Mx, j in ((sp.Rational(11, 4), 8, 3, 0), (sp.Rational(29, 10), 8, 12, 2),
                         (sp.Rational(31, 11), 9, 20, 4)):
        s, Ks = kstar(a, Jp, Mx, j)
        K = int(sp.floor(Ks)) + 1
        terms = []
        Rr = lam**(-s)
        terms.append(sp.integrate(rr**(2*a)*(lam**(K - 4 - j)*rr**(j - 2))**2*rr**3, (rr, 1, Rr)))
        for k in range(4, 9):
            thk = sp.Rational(k - 4, Jp - 3)
            for i in range(0, j + 2):
                ek = lam**((K - 3 - i)*(1 - thk) - (Mx + i)*thk)
                terms.append(sp.integrate(rr**(2*a)*(ek*rr**(-sp.Rational(k, 2) - 1))**2*rr**3, (rr, 1, Rr)))
        terms.append(sp.integrate(rr**(2*a)*(lam**(-Mx)*rr**(-sp.Rational(Jp + 3, 2)))**2*rr**3, (rr, Rr, sp.oo)))
        lim = sp.limit(sp.simplify(sum(terms)), lam, 0, "+")
        ok = ok and lim == 0
        print(f"     a = {a}, J' = {Jp}, M = {Mx}, j = {j}: s = {s}, K* = {sp.nsimplify(Ks)} ~ {float(Ks):.2f}, "
              f"K = {K}: flux -> {lim}")
    check("P9a at K = floor(K*) + 1 every term of the commuted flux tends to 0 (three sampled cases)", ok)
    # control: R2.10's K - 4 > a s holds but K < K*: the e_6 term up to R does not tend to 0
    a, Jp, Mx, j = sp.Rational(29, 10), 8, 1, 0
    s_old = (2*Mx + 1)/(Jp - 1 - 2*a)
    s, Ks = kstar(a, Jp, Mx, j)
    K = int(sp.floor(4 + a*s_old)) + 1
    th6 = sp.Rational(2, Jp - 3)
    e6 = lam**((K - 3 - 1)*(1 - th6) - (Mx + 1)*th6)
    t6 = sp.integrate(rr**(2*a)*(e6*rr**-4)**2*rr**3, (rr, 1, lam**(-s)))
    lim6 = sp.limit(t6, lam, 0, "+")
    check(f"P9b control: a = 29/10, J' = 8, M = 1: R2.10's K = {K} satisfies K - 4 > a s, but K < K* = "
          f"{float(Ks):.2f} and the e_6 term (one d_v) does not tend to 0", K - 4 > a*s_old and K < Ks and lim6 != 0,
          f"limit {lim6}")


def main():
    for f in (p1, p2, p3, p4, p5, p6, p7, p8, p9):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
