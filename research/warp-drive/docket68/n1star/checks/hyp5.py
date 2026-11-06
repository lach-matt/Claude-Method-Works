#!/usr/bin/env python3
"""hyp5.py -- the envelope hypotheses of Theorem L_1E'' proved, not sampled (EQUALITY5-LAYER.md, Round 8, R8.2).

For an envelope whose log has the form ell(x) = sum of a flat part, x := v - v_s, put u := 1/x and A_j(x) := x^(j+1)
ell^(j)(x).  For the two envelopes below each A_j is real-analytic on [0, x0] (x = 0 included), with A_1(0) > 0.  Since
env^(k)/env is the complete Bell polynomial Y_k(ell', ..., ell^(k)), env^(k)/env = u^(2k) Q_k with

    Q_k := x^k Y_k(A_1/x, ..., A_k/x),

a polynomial in x and the A_j (integer coefficients; the partition with p parts carries x^(k-p)), and Q_k(0) =
A_1(0)^k.  So kappa_k = u^2 R_k, R_k := Q_(k+1)/Q_k, kappa_k' = -u^3 (2 R_k - x R_k'), kappa = u^2 A_1, and every
quantity of the hypotheses is a function analytic on [0, x0]:

    env^(k) > 0                 <=>  Q_k > 0;
    kappa_k/kappa in (1/2, 2)   <=>  R_k/A_1 in (1/2, 2);
    env^(k) log-concave         <=>  P_k := 2 R_k - x R_k' > 0;
    |kappa_k'| <= c_R kappa_k^(3/2)   <=>  P_k/R_k^(3/2) <= c_R           (alpha = 1/2);
    |kappa'| >= c_t kappa^(3/2)       <=>  (2 A_1 - x A_1')/A_1^(3/2) >= c_t   (which gives (H_t), R7.2 (b));
    |env^(j)| <= c_j kappa^j env      <=>  Q_j/A_1^j <= c_j                (L.16 (c)'s first bound).

  H1 (certified, interval arithmetic) exp(-1/x): A_j = (-1)^(j+1) j!, exactly.  On [0, 1/100], cut into 200 intervals
     (x = 0 included), every check above for k <= 14 (positivity to k <= 15, L.16 (c) to j <= 15) holds on every
     interval; the certified bounds c_R, c_t, max c_j are printed.
  H2 (certified, interval arithmetic) the record's C_c^inf envelope, log env = 12 log sin(pi x/3) + 1 - 1/(t(2 - t)),
     t = 2x/3 (the envelope of CONSTANTS5's P* at its left edge): ell = -(3/4)/x - (3/4)/(3 - x) + 12 log x + 12
     g(pi x/3) + 1, g(z) := log(sin z/z) = sum_(n>=1) g_n z^(2n), g_n = (-1)^n 2^(2n-1) B_(2n)/(n (2n)!) (exact,
     n <= 30) with the tail bounded by |g_n| <= 2/(n pi^(2n)); so A_j = (3/4)(-1)^(j+1) j! - (3/4) j! (x/(3 - x))^(j+1)
     + 12 (-1)^(j-1) (j-1)! x + 12 (pi/3)^j x^(j+1) g^(j)(pi x/3), analytic on [0, x0], A_j' likewise.  The same checks
     on [0, 1/100] in 200 intervals.
  H3 (deduced, with a computed limit) every K: at x = 0 every check is strict (Q_k(0) = A_1(0)^k > 0, R_k/A_1 -> 1,
     P_k -> 2 A_1(0), P_k/R_k^(3/2) -> 2 A_1(0)^(-1/2), (2 A_1)/A_1^(3/2) -> 2 A_1(0)^(-1/2), Q_j/A_1^j -> 1), so for
     every K there is x0(K) > 0 on which (H_N+2), (H_t) and L.16 (c) hold, for both envelopes; printed: the limits for
     k <= 30 from the exact polynomials (exp(-1/x) and the record's A_j(0)).
  H4 (deduced, with a computed limit) (H_D): kappa(y/2) kappa(4y)^c env(4y) -> 0 for every c, both envelopes (env <=
     C x^12 e^(-3/(4x)), kappa <= C x^-2 on (0, x0]); sympy's limit at c = 30.

Controls: H1/H2 for the solver's sin^4 envelope (log env = 4 log sin(pi x/3) + const, an edge of finite order): A_1(0) =
0, and the certification fails on the first interval; H3: the exponent 3/2 of c_R replaced by 1 (alpha = 0) makes the
limit infinite.

Labels: H1, H2 certified (interval arithmetic, mpmath.iv, outward rounding); H3, H4 deduced, with exact limits.
Run: python3 checks/hyp5.py   (a few minutes)
"""
import sys
import textwrap
import time

import mpmath as mp
import sympy as sp

iv = mp.iv
iv.dps = 40
T0 = time.time()
KMAX = 15                      # positivity and L.16 (c) to j <= 15; (H_N) checks to k <= 14
X0 = sp.Rational(1, 100)
NSUB = 200


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


# ------------------------------------------------------------------------------------------------------------ algebra
XS = sp.Symbol('x')
AS = sp.symbols('A1:%d' % (KMAX + 3))
ADS = sp.symbols('Ad1:%d' % (KMAX + 3))


def bell_Q(kmax):
    """Q_k = x^k Y_k(A_1/x, ...), and Q_k' (in x, A_j, A_j'), as sympy Polys"""
    Ls = sp.symbols('L1:%d' % (kmax + 2))
    Y = [sp.Integer(1)]
    for _ in range(kmax):
        y = Y[-1]
        dy = sum(sp.diff(y, Ls[j])*Ls[j + 1] for j in range(kmax))
        Y.append(sp.expand(dy + Ls[0]*y))
    gens = (XS,) + AS[:kmax + 1] + ADS[:kmax + 1]
    Q, Qd = [], []
    for k, y in enumerate(Y):
        q = sp.expand(XS**k*y.subs({Ls[j]: AS[j]/XS for j in range(kmax + 1)}))
        qd = sp.expand(sp.diff(q, XS) + sum(sp.diff(q, AS[j])*ADS[j] for j in range(kmax + 1)))
        Q.append(sp.Poly(q, *gens))
        Qd.append(sp.Poly(qd, *gens))
    return Q, Qd


def peval(P, vals):
    tot = iv.mpf(0)
    for mon, co in P.terms():
        t = iv.mpf(int(co))
        for e, val in zip(mon, vals):
            if e:
                t = t*val**e
        tot += t
    return tot


# ------------------------------------------------------------------------------------------------------------ envelopes
def g_coeffs(nmax):
    return [None] + [sp.Rational((-1)**n*2**(2*n - 1))*sp.bernoulli(2*n)/(n*sp.factorial(2*n)) for n in range(1, nmax + 1)]


GN = g_coeffs(30)


def g_deriv(j, Z):
    """g^(j)(Z) for an interval Z in [0, pi/300], with the tail beyond n = 30 bounded"""
    tot = iv.mpf(0)
    for n in range(1, 31):
        if 2*n >= j:
            tot += iv.mpf(sp.Rational(GN[n]).p)/iv.mpf(sp.Rational(GN[n]).q)*iv.mpf(int(sp.factorial(2*n)/sp.factorial(2*n - j)))*Z**(2*n - j)
    zmax = iv.pi/300
    tail = iv.mpf(0)
    for n in range(31, 80):
        tail += 2/(n*iv.pi**(2*n))*iv.mpf(int(sp.factorial(2*n)/sp.factorial(2*n - j)))*zmax.b**(2*n - j)
    tail += tail*iv.mpf('1e-10') + iv.mpf(10)**-100      # the rest of the geometric tail
    return tot + iv.mpf([-tail.b, tail.b])


def A_exp(j, X):
    return iv.mpf((-1)**(j + 1)*int(sp.factorial(j))), iv.mpf(0)


def A_rec(j, X, coef=sp.Rational(3, 4), logc=12):
    f = int(sp.factorial(j))
    Z = iv.pi*X/3
    y = X/(3 - X)
    a = iv.mpf(coef.p)/coef.q*((-1)**(j + 1)*f) - iv.mpf(coef.p)/coef.q*f*y**(j + 1) \
        + logc*((-1)**(j - 1))*int(sp.factorial(j - 1))*X + logc*(iv.pi/3)**j*X**(j + 1)*g_deriv(j, Z)
    ad = -iv.mpf(coef.p)/coef.q*f*(j + 1)*y**j*3/(3 - X)**2 + logc*((-1)**(j - 1))*int(sp.factorial(j - 1)) \
        + logc*(iv.pi/3)**j*((j + 1)*X**j*g_deriv(j, Z) + X**(j + 1)*(iv.pi/3)*g_deriv(j + 1, Z))
    return a, ad


def A_sin4(j, X):
    return A_rec(j, X, coef=sp.Integer(0), logc=4)


# ------------------------------------------------------------------------------------------------------------ checks
QP, QDP = None, None


def certify(Afun, x0=X0, nsub=NSUB, kmax=KMAX, power=sp.Rational(3, 2)):
    global QP, QDP
    if QP is None:
        QP, QDP = bell_Q(kmax + 1)
    ok = True
    cR = ct = cj = None
    worst_ratio = None
    for i in range(nsub):
        X = iv.mpf([sp.Rational(i, nsub)*x0, sp.Rational(i + 1, nsub)*x0])
        X = iv.mpf([iv.mpf(sp.Rational(i, nsub)*x0).a, iv.mpf(sp.Rational(i + 1, nsub)*x0).b])
        As = [Afun(j, X) for j in range(1, kmax + 3)]
        vals = [X] + [a_ for a_, _ in As] + [ad for _, ad in As]
        vals = vals[:1] + vals[1:kmax + 3] + vals[kmax + 3:]
        Q = [peval(QP[k], vals) for k in range(kmax + 1)]
        Qd = [peval(QDP[k], vals) for k in range(kmax + 1)]
        A1, A1d = As[0]
        for k in range(kmax + 1):
            ok &= Q[k].a > 0
        if not ok:
            return False, None, None, None, None
        for k in range(kmax):
            R = Q[k + 1]/Q[k]
            Rd = (Qd[k + 1]*Q[k] - Q[k + 1]*Qd[k])/Q[k]**2
            rat = R/A1
            ok &= rat.a > iv.mpf(1)/2 and rat.b < 2
            P = 2*R - X*Rd
            ok &= P.a > 0
            if not ok:
                return False, None, None, None, None
            cr = P/R**power
            cR = cr.b if cR is None else max(cR, cr.b)
            worst_ratio = (min(worst_ratio[0], rat.a), max(worst_ratio[1], rat.b)) if worst_ratio else (rat.a, rat.b)
        t = (2*A1 - X*A1d)/A1**power
        ct = t.a if ct is None else min(ct, t.a)
        ok &= t.a > 0
        for jj in range(kmax + 1):
            c_ = Q[jj]/A1**jj
            cj = c_.b if cj is None else max(cj, c_.b)
    return ok, cR, ct, cj, worst_ratio


def h12(which, control=False):
    Af = A_sin4 if control else (A_exp if which == 'exp' else A_rec)
    ok, cR, ct, cj, wr = certify(Af)
    if control:
        return ok
    out("  %s %s on [0, 1/100] (200 intervals, x = 0 included): env^(k) > 0 (k <= %d), kappa_k/kappa in [%s, %s] within"
        " (1/2, 2), env^(k) log-concave, k <= %d: %s; certified c_R = sup P_k/R_k^(3/2) <= %s; (H_t): |kappa'| >= %s"
        " kappa^(3/2); L.16 (c): max_(j<=%d) Q_j/A_1^j <= %s  [%.0f s]"
        % ("H1" if which == 'exp' else "H2", "exp(-1/x)" if which == 'exp' else "the record's C_c^inf envelope",
           KMAX, mp.nstr(wr[0], 6), mp.nstr(wr[1], 6), KMAX - 1, ok, mp.nstr(cR, 6), mp.nstr(ct, 6), KMAX,
           mp.nstr(cj, 6), time.time() - T0))
    return ok


def h1(control=False):
    return h12('exp', control)


def h2(control=False):
    return h12('rec', control)


def h3(control=False):
    """the limits at x = 0 of the checked quantities, k <= 30, both envelopes"""
    QPz, QDz = bell_Q(30)
    power = 1 if control else sp.Rational(3, 2)
    ok = True
    rows = []
    for nm, A10, A1d0 in (("exp(-1/x)", 1, 0), ("record", sp.Rational(3, 4), 12)):
        # at x = 0 only the all-ones partition survives in Q_k: Q_k(0) = A_1(0)^k; R_k -> A_1(0); x R_k' -> 0
        q0 = [QPz[k].as_expr().subs(XS, 0).subs(AS[0], A10) for k in range(31)]
        good = all(sp.simplify(q0[k] - sp.Integer(A10)**k) == 0 for k in range(31))
        lim_cR = 2*A10/sp.Integer(A10)**power if power != 1 else 2*A10/A10
        lim_ct = 2*A10/sp.Integer(A10)**power
        good &= sp.Integer(A10) > 0
        if control:
            # alpha = 0: |kappa_k'|/kappa_k = u (2 R_k - x R_k')/R_k is unbounded as x -> 0
            return sp.limit((2*A10)/A10/XS, XS, 0, '+').is_finite
        rows.append("%s: Q_k(0) = A_1(0)^k for k <= 30: %s; lim c_R ratio = %s, lim c_t ratio = %s"
                    % (nm, good, lim_cR, lim_ct))
        ok &= good
    out("  H3 at x = 0 (every K): " + "; ".join(rows) + "; so each check holds strictly at x = 0 and, the quantities"
        " being analytic there, on some (0, x0(K)]: %s" % ok)
    return ok


def h4(control=False):
    y = sp.Symbol('y', positive=True)
    c = 30
    ok = True
    rows = []
    for nm, ell in (("exp(-1/x)", lambda x: -1/x),
                    ("record", lambda x: 12*sp.log(sp.sin(sp.pi*x/3)) + 1 - 1/((2*x/3)*(2 - 2*x/3)))):
        kap = lambda x: sp.diff(ell(XS), XS).subs(XS, x)                          # noqa: E731
        q = kap(y/2)*kap(4*y)**c*sp.exp(ell(4*y))
        if control:
            q = kap(y/2)*kap(4*y)**c                                               # without the envelope: infinite
        lim = sp.limit(q, y, 0, '+')
        good = lim == 0
        rows.append("%s: limit %s" % (nm, lim))
        ok &= good
    if control:
        return ok
    out("  H4 (H_D) at c = 30: kappa(y/2) kappa(4y)^c env(4y) as y -> 0: " + "; ".join(rows) + ": %s" % ok)
    return ok


def main():
    ok = True
    for name, f in (("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("hyp5: %s  [%.0f s]" % ("all checks pass, every control fails" if ok else "FAILURES", time.time() - T0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
