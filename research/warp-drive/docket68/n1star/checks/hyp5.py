#!/usr/bin/env python3
"""hyp5.py -- the envelope hypotheses of Theorem L_1E'' proved, not sampled (EQUALITY5-LAYER.md, Round 8, R8.2).

Put x := v - v_s, ell := log env and A_j(x) := x^(j+1) ell^(j)(x).  For the envelopes of H1, H2 every A_j is
real-analytic on [0, x0] (x = 0 included) with A_1(0) > 0.  env^(k)/env is the complete Bell polynomial Y_k(ell', ...,
ell^(k)), which is graded, so env^(k)/env = x^(-2k) Q_k with

    Q_k := x^k Y_k(A_1/x, ..., A_k/x),     Q_0 = 1,   Q_(k+1) = sum_(i=0..k) C(k, i) x^i A_(i+1) Q_(k-i)

(from Y_(k+1) = sum_i C(k, i) L_(i+1) Y_(k-i); checked exactly against sympy's Bell polynomials for k <= 12, H0), a
polynomial in x and the A_j with Q_k(0) = A_1(0)^k.  So kappa := ell' = A_1/x^2, kappa_k := (log env^(k))' = R_k/x^2
with R_k := Q_(k+1)/Q_k, kappa_k' = -(2 R_k - x R_k')/x^3, and every hypothesis is a statement about functions
analytic on [0, x0]:

    env^(k) > 0                         <=>  Q_k > 0;
    kappa_k/kappa in [1/2, 2]           <=>  R_k/A_1 in [1/2, 2];
    env^(k) log-concave                 <=>  P_k := 2 R_k - x R_k' > 0;
    |kappa_k'| <= c_R kappa_k^(3/2)     <=>  P_k/R_k^(3/2) <= c_R                (alpha = 1/2);
    |kappa'| >= c_t kappa^(3/2)         <=>  (2 A_1 - x A_1')/A_1^(3/2) >= c_t;
    |env^(j)| <= c_j kappa^j env        <=>  |Q_j|/A_1^j <= c_j                  (L.16 (c)'s first bound);
    kappa (v - v_s)^2 >= c_*            <=>  A_1 >= c_*                          ((H_rho*)'s first half).

(H_t) follows from the c_t bound and log-concavity: kappa - kappa_(N-1) = sum_(k<N-1) |kappa_k'|/kappa_k >=
|kappa'|/kappa >= c_t kappa^(1/2), since kappa_(k+1) = kappa_k + kappa_k'/kappa_k.

  H0 (exact) the recursion equals x^k Y_k(A_1/x, ...) for k <= 12 (sympy.bell).  Control: the recursion without C(k, i).
  H1 (certified: interval arithmetic, mpmath.iv at 40 digits, outward rounding) exp(-1/x): A_j = (-1)^(j+1) j! exactly.
     On [0, 1/200] cut into 400 closed intervals (x = 0 included): Q_k > 0 for k <= 17; R_k/A_1 in [1/2, 2], P_k > 0 and
     the c_R bound for k <= 16 (so (H_N) to N = 16, (H_N+2) to N = 14, i.e. K <= 11); the c_t bound; |Q_j|/A_1^j for j
     <= 16; A_1 >= c_*.  The certified constants are printed.  (On [0, 1/100] kappa_16/kappa leaves [1/2, 2] near x =
     0.0096; the theorem needs the hypotheses on some (v_s, v_s + x0] only.)  Control: the same on [0, 1/40], where Q_17
     has its first root at 0.01868 (Q_15 at 0.02166): the certification fails, as it must.
  H2 (certified, as H1) the record's C_c^inf envelope (CONSTANTS5.md R2.2 (a), envelope5.py: env = c cos^12(pi y/2)
     exp(-y^2/(1 - y^2)), y = (2v - 4)/3, v_s = 1/2), whose log at its left edge, t := 2x/3 = 1 + y, is log c + 12 log
     sin(pi x/3) + 1 - 1/(t(2 - t)), so ell = -(3/4)/x - (3/4)/(3 - x) + 12 log x + 12 g(pi x/3) + const, g(z) := log(sin
     z/z) = sum_(n>=1) g_n z^(2n), g_n = (-1)^n 2^(2n-1) B_(2n)/(n (2n)!) exact for n <= 30, the tail enclosed by |g_n| =
     zeta(2n)/(n pi^(2n)) <= 2/(n pi^(2n)); hence A_j = (3/4)(-1)^(j+1) j! - (3/4) j! (x/(3 - x))^(j+1) + 12 (-1)^(j-1)
     (j-1)! x + 12 (pi/3)^j x^(j+1) g^(j)(pi x/3), analytic on |x| < 3, and A_j' likewise.  The checks of H1 on [0,
     1/200] in 400 intervals.  Control: the solver's sin^4 envelope (log env = 4 log sin(pi x/3) + const, A_1(0) = 0)
     through the same certifier: it fails on the first interval.
  H3 (exact values at x = 0; deduced for every K) every check is strict at x = 0: Q_k(0) = A_1(0)^k > 0, R_k(0) = A_1(0),
     P_k(0) = 2 A_1(0) > 0 (R_k'(0) finite), P_k/R_k^(3/2) and the c_t ratio -> 2 A_1(0)^(-1/2), Q_j/A_1^j -> 1; computed
     exactly from the recursion with the exact A_j(0), A_j'(0) of both envelopes for k <= 40.  The quantities being
     analytic at 0, for every K there is x0(K) > 0 on which (H_N+2), (H_t), L.16 (c) and (H_rho*)'s first half hold, for
     both envelopes.  Control: the sin^4 edge, A_1(0) = 0: Q_k(0) = 0, nothing strict.
  H4 (exact limits) (H_D): kappa(y/2) kappa(4y)^c env(4y) -> 0 as y -> 0 for every c > 0: exp(-1/x) exactly, (4/y^2)(16
     y^2)^(-c) e^(-1/(4y)); the record's envelope through the bound 1.33 M (4/y^2)(M/(16 y^2))^c e^(1 - 3/(16y)) (y <=
     x0/4; env <= c_env e^(1 - 3/(4x)), its peak c_env <= 1.3241035 (CONSTANTS5.md); M := max A_1 on [0, x0] from H2's
     intervals); sympy's limit with c a positive symbol, and at c = 30.  Control: the sin^4 edge, exactly, at c = 30:
     the limit is oo.
  H5 (exact) the solver's sin^4 envelope (the paper's section 6 numerics) is outside the hypotheses and outside Theorem
     1's class: env^(4) jumps at v_s (env^(4)(v_s+) = 8 pi^4/27, env = 0 below), kappa_3/kappa -> 1/4 < 1/2 and env^(5)
     < 0 just above v_s (env^(5)/x -> -160 pi^6/243): (H_N) fails for every N >= 3, and (H_D) fails (H4's control).
     Control: exp(-1/x) through the same test (kappa_3/kappa -> 1): not flagged.

Labels: H0, H3, H4, H5 exact (sympy); H1, H2 certified (interval arithmetic).
Run: python3 checks/hyp5.py   (about eight minutes)
"""
import sys
import textwrap
import time

import mpmath as mp
import sympy as sp

iv = mp.iv
iv.dps = 40
T0 = time.time()
KQ = 17                        # Q_k > 0 for k <= KQ; (H_N) checks for k <= KQ - 1; L.16 (c) for j <= KQ - 1
NSUB = 400
X0 = sp.Rational(1, 200)


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


def ivq(r):
    r = sp.Rational(r)
    return iv.mpf(int(r.p))/iv.mpf(int(r.q))


# ------------------------------------------------------------------------------------------------------------ algebra
def q_rec(A, Ad, X, kmax, binom=True):
    """Q_k, Q_k' for k <= kmax by the recursion; A[j], Ad[j] for j = 1..kmax (index 0 unused); intervals or sympy"""
    Q, Qd = [1], [0]
    for k in range(kmax):
        q = qd = 0
        for i in range(k + 1):
            c = int(sp.binomial(k, i)) if binom else 1
            xi = X**i if i else 1
            q += c*xi*A[i + 1]*Q[k - i]
            qd += c*((i*X**(i - 1) if i else 0)*A[i + 1]*Q[k - i] + xi*Ad[i + 1]*Q[k - i] + xi*A[i + 1]*Qd[k - i])
        if isinstance(q, sp.Basic):
            q, qd = sp.expand(q), sp.expand(qd)
        Q.append(q)
        Qd.append(qd)
    return Q, Qd


def h0(control=False):
    xs = sp.Symbol('x', positive=True)
    As = (None,) + sp.symbols('A1:14')
    Ls = sp.symbols('L1:14')
    Q, _ = q_rec(As, [0]*14, xs, 12, binom=not control)
    good = True
    for k in range(1, 13):
        Y = sum(sp.bell(k, p, Ls[:k - p + 1]) for p in range(1, k + 1))
        ref = sp.expand(xs**k*Y.subs({Ls[j]: As[j + 1]/xs for j in range(13)}))
        good &= sp.expand(Q[k] - ref) == 0
    if not control:
        out("  H0 the recursion for Q_k equals x^k Y_k(A_1/x, ...) exactly, k <= 12: %s" % good)
    return good


# ------------------------------------------------------------------------------------------------------------ envelopes
GN = [None] + [sp.Rational((-1)**n*2**(2*n - 1))*sp.bernoulli(2*n)/(n*sp.factorial(2*n)) for n in range(1, 31)]
GNI = [None] + [ivq(GN[n]) for n in range(1, 31)]


def ff(m, j):
    """m!/(m - j)!"""
    return int(sp.ff(m, j))


def g_deriv(j, Z):
    """g^(j)(Z) for an interval Z in [0, pi/300]: the exact series to n = 30 plus an enclosure of the tail.  Tail:
    |g_n (2n)!/(2n-j)! z^(2n-j)| <= t_n := 2/(n pi^(2n)) (2n)!/(2n-j)! (pi/300)^(2n-j); summed for 31 <= n <= 79; for
    n >= 79, t_(n+1)/t_n <= (160/(160 - j))^2/300^2 < 10^(-4) (j <= 20), so the rest is at most 2*10^(-4) t_79"""
    assert j <= 20
    tot = iv.mpf(0)
    for n in range(1, 31):
        if 2*n >= j:
            tot += GNI[n]*ff(2*n, j)*Z**(2*n - j)
    zr = iv.pi/300
    tail = iv.mpf(0)
    for n in range(31, 80):
        tail += 2/(n*iv.pi**(2*n))*ff(2*n, j)*zr**(2*n - j)
    tail = (tail*(1 + iv.mpf('2e-4'))).b
    return tot + iv.mpf([-tail, tail])


def A_exp(j, X):
    return iv.mpf((-1)**(j + 1)*int(sp.factorial(j))), iv.mpf(0)


def A_rec(j, X, coef=sp.Rational(3, 4), logc=12):
    f = int(sp.factorial(j))
    cf = ivq(coef)
    Z = iv.pi*X/3
    y = X/(3 - X)
    a = cf*((-1)**(j + 1)*f) - cf*f*y**(j + 1) + logc*((-1)**(j - 1))*int(sp.factorial(j - 1))*X \
        + logc*(iv.pi/3)**j*X**(j + 1)*g_deriv(j, Z)
    ad = -cf*f*(j + 1)*y**j*3/(3 - X)**2 + logc*((-1)**(j - 1))*int(sp.factorial(j - 1)) \
        + logc*(iv.pi/3)**j*((j + 1)*X**j*g_deriv(j, Z) + X**(j + 1)*(iv.pi/3)*g_deriv(j + 1, Z))
    return a, ad


def A_sin4(j, X):
    return A_rec(j, X, coef=sp.Integer(0), logc=4)


# ------------------------------------------------------------------------------------------------------------ certifier
def interval(i, x0, nsub):
    return iv.mpf([ivq(sp.Rational(i, nsub)*x0).a, ivq(sp.Rational(i + 1, nsub)*x0).b])


def certify(Afun, x0=X0, nsub=NSUB, kq=KQ):
    """(True, constants) if every check holds on every closed interval of [0, x0]; else (False, the first failure)"""
    cR = ct = cj = cs = lo = hi = M = None
    for i in range(nsub):
        X = interval(i, x0, nsub)
        AA = [None] + [Afun(j, X) for j in range(1, kq + 1)]
        A = [None] + [a for a, _ in AA[1:]]
        Ad = [None] + [ad for _, ad in AA[1:]]
        Q, Qd = q_rec(A, Ad, X, kq)
        A1, A1d = A[1], Ad[1]
        if not A1.a > 0:
            return False, "A_1 > 0 fails on interval %d" % i
        cs = A1.a if cs is None else min(cs, A1.a)
        M = A1.b if M is None else max(M, A1.b)
        for k in range(1, kq + 1):
            if not Q[k].a > 0:
                return False, "Q_%d > 0 fails on interval %d, x in [%s, %s]" % (k, i, mp.nstr(X.a, 6), mp.nstr(X.b, 6))
        for k in range(kq):
            R = Q[k + 1]/Q[k]
            Rd = (Qd[k + 1]*Q[k] - Q[k + 1]*Qd[k])/Q[k]**2
            rat = R/A1
            if not (rat.a >= iv.mpf(1)/2 and rat.b <= 2):
                return False, "kappa_%d/kappa in [1/2, 2] fails on interval %d" % (k, i)
            lo = rat.a if lo is None else min(lo, rat.a)
            hi = rat.b if hi is None else max(hi, rat.b)
            P = 2*R - X*Rd
            if not P.a > 0:
                return False, "log-concavity of env^(%d) fails on interval %d" % (k, i)
            cr = P/(R*iv.sqrt(R))
            cR = cr.b if cR is None else max(cR, cr.b)
        t = (2*A1 - X*A1d)/(A1*iv.sqrt(A1))
        if not t.a > 0:
            return False, "the c_t bound fails on interval %d" % i
        ct = t.a if ct is None else min(ct, t.a)
        for j in range(1, kq):
            c_ = abs(Q[j])/A1**j
            cj = c_.b if cj is None else max(cj, c_.b)
    return True, dict(cR=cR, ct=ct, cj=cj, cs=cs, lo=lo, hi=hi, M=M)


def up(p, d=5):
    """an upper bound of the point interval p, rounded up to d decimals"""
    with mp.workdps(40):
        return mp.nstr(mp.ceil(mp.mpf(p._mpi_[1])*10**d)/10**d, 12)


def dn(p, d=5):
    with mp.workdps(40):
        return mp.nstr(mp.floor(mp.mpf(p._mpi_[0])*10**d)/10**d, 12)


def report(tag, name, ok, res, x0):
    if not ok:
        out("  %s %s on [0, %s]: not certified: %s" % (tag, name, x0, res))
        return
    out("  %s %s on [0, %s] (%d closed intervals, x = 0 included), on every interval: env^(k) > 0 for k <= %d;"
        " kappa_k/kappa in [%s, %s] (within [1/2, 2]), env^(k) log-concave and |kappa_k'| <= c_R kappa_k^(3/2) with"
        " c_R = %s, for k <= %d; |kappa'| >= c_t kappa^(3/2) with c_t = %s; |env^(j)| <= c_j kappa^j env with"
        " max_(j<=%d) c_j = %s; kappa x^2 in [c_*, M] = [%s, %s].  So (H_N) to N = %d, (H_N+2) to N = %d, (H_t),"
        " L.16 (c) to j = %d and"
        " (H_rho*)'s first half hold on (v_s, v_s + %s]"
        % (tag, name, x0, NSUB, KQ, dn(res['lo']), up(res['hi']), up(res['cR']), KQ - 1, dn(res['ct']), KQ - 1,
           up(res['cj']), dn(res['cs']), up(res['M']), KQ - 1, KQ - 3, KQ - 1, x0))


RES = {}


def h1(control=False):
    x0 = sp.Rational(1, 40) if control else X0
    ok, res = certify(A_exp, x0=x0)
    report("H1", "exp(-1/x)" + (" [control]" if control else ""), ok, res, x0)
    return ok


def h2(control=False):
    ok, res = certify(A_sin4 if control else A_rec)
    if ok and not control:
        RES['rec'] = res
    report("H2", "the solver's sin^4 envelope [control]" if control else "the record's C_c^inf envelope", ok, res, X0)
    return ok


def h3(control=False):
    """the exact values at x = 0, k <= 40"""
    K3 = 40
    rows = []
    ok = True
    if control:
        cases = (("sin^4 edge", lambda j: sp.Integer(0), lambda j: 4*(-1)**(j - 1)*sp.factorial(j - 1)),)
    else:
        cases = (("exp(-1/x)", lambda j: (-1)**(j + 1)*sp.factorial(j), lambda j: sp.Integer(0)),
                 ("record", lambda j: sp.Rational(3, 4)*(-1)**(j + 1)*sp.factorial(j),
                  lambda j: 12*(-1)**(j - 1)*sp.factorial(j - 1)))
    for nm, a0, ad0 in cases:
        A = [None] + [a0(j) for j in range(1, K3 + 2)]
        Ad = [None] + [ad0(j) for j in range(1, K3 + 2)]
        Q, Qd = q_rec(A, Ad, sp.Integer(0), K3 + 1)
        A10 = A[1]
        good = bool(A10 > 0) and all(Q[k] == A10**k for k in range(K3 + 2))
        if good:
            good &= all(Q[k + 1]/Q[k] == A10 for k in range(K3 + 1))
            Rd0 = [(Qd[k + 1]*Q[k] - Q[k + 1]*Qd[k])/Q[k]**2 for k in range(K3 + 1)]
            good &= all(d.is_finite for d in Rd0)
            rows.append("%s: A_1(0) = %s; Q_k(0) = A_1(0)^k, R_k(0) = A_1(0), R_k'(0) finite (R_%d'(0) = %s) for"
                        " k <= %d; so P_k(0) = %s, the c_R and c_t ratios -> %s"
                        % (nm, A10, K3, Rd0[K3], K3, 2*A10, sp.nsimplify(2*A10/A10**sp.Rational(3, 2))))
        ok &= good
    if not control:
        out("  H3 at x = 0, exact: " + "; ".join(rows) + ".  Every check is strict at x = 0, hence on some (0, x0(K)]"
            " for every K: %s" % ok)
    return ok


def h4(control=False):
    y = sp.Symbol('y', positive=True)
    c = sp.Symbol('c', positive=True)
    if control:
        x = sp.Symbol('x', positive=True)
        env = sp.sin(sp.pi*x/3)**4
        kap = sp.diff(env, x)/env
        q = kap.subs(x, y/2)*kap.subs(x, 4*y)**30*env.subs(x, 4*y)
        return sp.limit(q, y, 0, '+') == 0
    M = sp.Rational(up(RES['rec']['M']))
    q_exp = (4/y**2)*(1/(16*y**2))**c*sp.exp(-1/(4*y))
    q_rc = sp.Rational(133, 100)*M*(4/y**2)*(M/(16*y**2))**c*sp.exp(1 - sp.Rational(3, 16)/y)
    rows = []
    ok = True
    for nm, q in (("exp(-1/x)", q_exp), ("the record's envelope (bound, M = %s)" % M, q_rc)):
        l_c = sp.limit(q, y, 0, '+')
        l_30 = sp.limit(q.subs(c, 30), y, 0, '+')
        rows.append("%s: limit %s for c > 0 symbolic, %s at c = 30" % (nm, l_c, l_30))
        ok &= l_c == 0 and l_30 == 0
    out("  H4 (H_D): kappa(y/2) kappa(4y)^c env(4y) -> 0: " + "; ".join(rows) + ": %s" % ok)
    return ok


def h5(control=False):
    x = sp.Symbol('x', positive=True)
    env = sp.exp(-1/x) if control else sp.sin(sp.pi*x/3)**4
    d = [sp.diff(env, x, k) for k in range(6)]
    r3 = sp.limit((d[4]/d[3])/(d[1]/d[0]), x, 0, '+')
    if control:
        return bool(r3 < sp.Rational(1, 2))
    j4 = sp.limit(d[4], x, 0, '+')
    d5 = sp.limit(d[5]/x, x, 0, '+')
    ok = bool(j4 != 0 and r3 < sp.Rational(1, 2) and d5 < 0)
    out("  H5 the solver's sin^4 envelope: env^(4)(v_s+) = %s != 0 (C^3, not C^4), kappa_3/kappa -> %s < 1/2,"
        " env^(5)/x -> %s < 0: (H_N) fails for every N >= 3: %s" % (j4, r3, d5, ok))
    return ok


def main():
    ok = True
    for name, f in (("H0", h0), ("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4), ("H5", h5)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL",
                         " (control passed)" if ctl else " (control detected)"))
        ok &= good and not ctl
    out("hyp5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    sys.stderr.write("hyp5: %.0f s\n" % (time.time() - T0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
