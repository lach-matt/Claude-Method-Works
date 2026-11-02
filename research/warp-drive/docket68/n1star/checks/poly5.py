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
t, x1, x2, x3, x4, th = sp.symbols("t x1 x2 x3 x4 theta", real=True)
XS = [t, x1, x2, x3, x4]
R = sp.sqrt(x1**2 + x2**2 + x3**2 + x4**2)
V = t + R


def lam_order(expr):
    """lowest power of lam in a Laurent polynomial in lam (coefficients free of lam)"""
    e = sp.expand(expr)
    if e == 0:
        return sp.oo
    pw = set()
    for term in sp.Add.make_args(e):
        c, p = term.as_coeff_exponent(lam)
        if sp.simplify(term/lam**p).has(lam):
            raise ValueError("not a Laurent polynomial in lam")
        pw.add(p)
    lo = min(pw)
    coeff = sp.simplify(sum(term for term in sp.Add.make_args(e) if term.as_coeff_exponent(lam)[1] == lo))
    return lo if coeff != 0 else sp.oo


def D(expr, a, vfield=None):
    """two-scale derivative along a coordinate (a int) or along a vector field (list of 5 coefficients)"""
    if vfield is None:
        return sp.diff(expr, XS[a]) + sp.diff(V, XS[a])/lam*sp.diff(expr, th)
    return sum(c*(sp.diff(expr, XS[i]) + sp.diff(V, XS[i])/lam*sp.diff(expr, th)) for i, c in enumerate(vfield)
               if c != 0)


def p1():
    print("P1  the two-scale chain rule: one lam^-1 per Cartesian derivative, none per rotation")
    A = sp.Function("A")(*XS)
    j = 1
    F = lam**j*A*sp.sin(th)
    ok = True
    for alpha in ((0,), (1,), (0, 2), (0, 1, 3), (1, 1, 4)):
        e = F
        for a in alpha:
            e = D(e, a)
        o = lam_order(e)
        ok = ok and o == j - len(alpha)
    check("P1a D^alpha (lam A sin th) has order 1 - |alpha| exactly (five multi-indices up to order 3)", ok)
    Om = [0, -x2, x1, 0, 0]  # x1 d_2 - x2 d_1
    e = D(D(F, None, Om), None, Om)
    check("P1b two rotations: order still 1 (Omega v = 0)", lam_order(e) == 1)
    # validate the two-scale formula against the true derivative of A sin(v/lam)
    true = sp.diff(A*sp.sin(V/lam), x1, t)
    two = D(D(A*sp.sin(th), 0), 1).subs(th, V/lam)
    check("P1c the two-scale formula equals the true d_1 d_t of A sin(v/lam)", sp.simplify(true - two) == 0)
    Nr = [0, x2, x1, 0, 0]  # x2 d_1 + x1 d_2: not a rotation
    e = D(F, None, Nr)
    check("P1d control: x2 d_1 + x1 d_2 (not a rotation) costs lam^-1: order 0", lam_order(e) == 0)


def ks():
    eta = sp.diag(-1, 1, 1, 1, 1)
    k = sp.Matrix([1, x1/R, x2/R, x3/R, x4/R])
    mu = sp.Symbol("mu", positive=True)
    g0 = eta + mu/R**2*k*k.T
    g0i = eta - mu/R**2*(eta*k)*(eta*k).T
    return g0, g0i, mu


def p2():
    print("P2  the coefficients of Lemma 11.0's energy identity")
    W = sp.Function("W")(*XS)
    e = D(lam*W*sp.sin(th), 0)
    check("P2a d_t (lam W sin th) has order 0: the kernel ||d g|| <= C t^(-3/2) is lam-free", lam_order(e) == 0)
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
    Wf = sp.Function("Wf")(*XS)
    Y = lam*Wf*sp.sin(th)
    hess = sp.Matrix(5, 5, lambda a, b: D(D(Y, a), b))
    Hm = sp.Matrix(5, 5, lambda a, b: sp.Symbol(f"H{min(a, b)}{max(a, b)}"))
    q = sp.expand(sum(Hm[a, b]*hess[a, b] for a in range(5) for b in range(5))/2)
    lead = sum(term for term in sp.Add.make_args(q) if term.as_coeff_exponent(lam)[1] == -1)
    target = -sp.Rational(1, 2)/lam*Wf*sp.sin(th)*sum(Hm[a, b]*sp.diff(V, XS[a])*sp.diff(V, XS[b])
                                                       for a in range(5) for b in range(5))
    check("P2d (1/2) H^ab d_a d_b (lam [W]) = -(1/2) lam^-1 H(dv, dv) [W] + O(lam^0): with H(dv, dv) = -u(ell, ell)"
          " the term -(1/2) lam^-1 ... is lam^-1 u_1(ell, ell) [d_th^2 W]/2, linear in u_1",
          sp.simplify(lead - target) == 0)
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
    e = {3: -1, 4: 0}
    for k in range(5, kmax + 1):
        cands = []
        # linear terms: Gamma[g0] d_v on G_(k-2) (coefficient r-gain 2, one d_v)
        cands.append(e[k - 2] + 1)
        # flat linear part (no d_v) on G_(k-2)
        cands.append(e[k - 2])
        # products with up to two d_v, factors k_i >= 3, sum k_i <= k + 2 (r-gains make up the rest)
        for parts in (2, 3):
            for ks_ in partitions(k + 2, parts, 3):
                for extra in range(0, 3):
                    pass
                if all(ki <= k - 1 for ki in ks_):
                    cands.append(sum(e[ki] for ki in ks_) + 2)
            for tot in range(3*parts, k + 2):
                for ks_ in partitions(tot, parts, 3):
                    if all(ki <= k - 1 for ki in ks_):
                        cands.append(sum(e[ki] for ki in ks_) + 2)
        e[k] = max(cands)
    return e


def stages(Jmax, nmax, mmax, e):
    """pointwise orders M(J, n, m) of u_J (n Cartesian/rotation derivatives, m ell-derivatives)."""
    M = {}
    # u_3 = u_1: natural (P6): order n - 1; ell does not hit the phase (ell v = 0)
    for n in range(nmax + 8):
        for m in range(mmax + 1):
            M[(3, n, m)] = n - 1
    for J in range(3, Jmax):
        crude = max([0] + [e[k] + 1 for k in range(4, J + 1)])  # |d u_J| <= lam^-crude r^-2 (one factor)
        for n in range(nmax + 8 - 3*(J - 2)):
            # S~ of u_J's equation at order n: linear terms in u_J (order +1), quadratic (+ crude), explicit
            # G-monomials beyond the leading order (e <= 2 J - 6 at this r-order)
            sres = max(M[(J, n, 0)] + 1, M[(J, n + 1, 0)], M[(J, n, 0)] + crude + 1, 2*J - 6 + n)
            # S' adds (g^-1 - g0^-1) d^2 (r^(1-q) G_(J+1)) and the box~ remainder
            spr = max(sres, e[J + 1] + 1 + n, e[J + 1] + n)
            if (J, n + 3, 0) not in M:
                break
            # energies of order n + 2 feed the pointwise bound at order n (Lemma 9.3), commutators natural
            sp_n2 = max(M[(J, n + 2, 0)] + 1, M[(J, n + 3, 0)], M[(J, n + 2, 0)] + crude + 1, 2*J - 6 + n + 2,
                        e[J + 1] + 1 + n + 2)
            base = sp_n2
            for m in range(mmax + 1):
                # ell-gain by transport: f contains d_v of the previous ell-level: one more power per ell
                M[(J + 1, n, m)] = base + m
    return M


def p7():
    print("P7  Lemma 11.2 and Proposition 11.1: the coefficients and the remainders")
    e = eG(40)
    check("P7a e(G_k) <= k - 4 for k = 4..40 (e(G_3) = -1, e(G_4) = 0)", all(e[k] <= k - 4 for k in range(4, 41)),
          str([e[k] for k in range(3, 12)]))
    M = stages(24, 12, 4, e)
    bound = lambda J, n, m: n + m + (J*J + 3*J)//2 - 9
    rows = [(J, n, m) for (J, n, m) in M if J <= 24 and n <= 12 and m <= 4]
    ok = all(M[k] <= bound(*k) for k in rows)
    worst = max(M[k] - bound(*k) for k in rows)
    print("     M(J, 0, 0), J = 3..12:", [M.get((J, 0, 0)) for J in range(3, 13)])
    check("P7b M(J, n, m) <= n + m + (J^2 + 3J)/2 - 9 on every computed (J <= 24, n <= 12, m <= 4)", ok,
          f"{len(rows)} rows, max(M - bound) = {worst}")
    check("P7c control: no bound 3J + n + m (M(24, 0, 0) > 72)", M[(24, 0, 0)] > 72, f"M(24,0,0) = {M[(24, 0, 0)]}")


def p8():
    print("P8  smallness of the commuted data on N from (Poly)")
    rr = sp.Symbol("rr", positive=True)
    ok = True
    for a, Jp, Mx, j, Kp in ((sp.Rational(11, 4), 8, 12, 0, 80), (sp.Rational(11, 4), 8, 12, 3, 140),
                             (sp.Rational(29, 10), 9, 20, 2, 400)):
        s = (2*Mx + 1)/sp.Integer(Jp - 1 - 2*a)
        Rr = lam**(-s)
        low = sp.integrate(rr**(2*a)*(lam**(Kp - 3 - j)*rr**(j - 2))**2*rr**3, (rr, 1, Rr))
        high = sp.integrate(rr**(2*a)*(lam**(-Mx)*rr**(-sp.Rational(Jp + 3, 2)))**2*rr**3, (rr, Rr, sp.oo))
        cond = Kp > 3 + j + s*(a + j - 1)
        lim = sp.limit(sp.simplify(low + high), lam, 0, "+")
        ok = ok and cond and lim == 0
        print(f"     a = {a}, J' = {Jp}, M = {Mx}, j = {j}, K' = {Kp}: s = {s}, condition {cond}, flux -> {lim}")
    check("P8a the split flux of Z^j d e tends to 0 in the sampled cases satisfying K' > 3 + j + s(a + j - 1)", ok)
    a = sp.Rational(11, 4)
    div = sp.integrate(rr**(2*a)*(rr**(1 - sp.Rational(11, 2)))**2*rr**3, (rr, 1, sp.oo))
    check("P8b control: above R without the ell-gain (|Z d e| ~ r^(j - (J'+3)/2), J' = 8, j = 1) the flux diverges",
          div == sp.oo)


def main():
    for f in (p1, p2, p3, p4, p5, p6, p7, p8):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
