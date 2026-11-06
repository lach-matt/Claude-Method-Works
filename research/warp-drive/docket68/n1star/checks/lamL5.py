#!/usr/bin/env python3
"""lamL5.py -- lam_L of Theorem L made explicit (EQUALITY5-LAYER.md, Round 3, R3.3; open item O4 of rounds 1-2).

The point P* of CONSTANTS5.md (READ): mu0 = 1, A = 1, tau0 = -2, v_s = 1/2, r0(v_s) = 5/2, K = 6 (N = 9), tau_end -
tau0 <= 5.937209 (certified there); Theorem L's parameters (rounds 1-2): p = 14, M = 2N + 8 = 26, m = 56 M = 1456.

  L1 (exact) The paper's envelope sin^4(pi (v - 1/2)/3) is not flat at its edge: on v > v_s its derivatives at v_s+
     are 0, 0, 0, 0, 24 (pi/3)^4, 0, -480 (pi/3)^6, on v < v_s all zero: env^(4) jumps by 24 (pi/3)^4 = 28.86..., so
     env is C^3 and not C^4, M_m := sup |env^(m)| is infinite for m >= 5 (env^(5) carries a Dirac mass), and Theorem
     1 and Theorem L do not apply to it; one-sided, sup_(v > v_s) |env^(m)| <= (pi/3)^m (4^m + 4 2^m)/8.  Control: the
     record's C_c^inf envelope (CONSTANTS5 R2.2 (a)) has |env^(4)| < 1e-100 at v_s + 1e-3 (flat).
  L2 (certified, interval arithmetic) For that C_c^inf envelope, env = c beta((2v - 4)/3), beta = cos^12(pi y/2)
     exp(-y^2/(1 - y^2)): by Cauchy's estimate on the disc of radius theta (1 - |y0|) about y0,
         M_m <= B(m) := c (2/3)^m m! e^(3/4) min_(0<theta<1) cosh(pi theta/2)^12 (2 (1 + theta) m/(e theta))^m,
     (|cos z| <= cosh Im z; exp(-z^2/(1 - z^2)) = e exp(-1/(1 - z^2)) with 1/(1 - z^2) = (1/u + 1/(2 - u))/2, u = 1 - z,
     Re 1/u >= 1/((1 + theta) d) and Re 1/(2 - u) >= 1/2 on the disc, which gives e^(3/4) [Round 4, verifier of
     round 3: Re 1/w >= 1/(w0 + rho) alone gives e^1]; sup_d d^-m e^(-a/d) = (m/(a e))^m).
     log10 B(1456) = 8574.0..., M_1456^(1/1456) <= 7.75e5.  Cross-checks: B(k) >= e_k/2 for k <= 14 (CONSTANTS5's
     sampled lower values); at m = 400 a power-series value of |beta^(400)| at one point, stable to 100 digits between
     two precisions, lies below B (the bound is within a factor about 1.5^m).  Control: B without its factor m! lies
     below that computed value (refuted).
  L3 (exact rationals; certified sums) Lemma L.5's constant.  Round 1: C_(i,m) = Lambda_(i,m) + (m - 1)^(m - i) on
     the nodes 0, -1, ..., -(m - 1), Lambda_(1,m) = H_(m-1) + sum_k binom(m-1, k)/k (checked against layerwin5's values
     at m = 6, 8); log10 C_(1,1456) = 4601.9..., log10 C_(26,1456) = 4523.2....  Amended (deduced: the remainder f - P
     has m - i zeros of its i-th derivative in an interval of length (m - 1) h, so |(f - P)^(i)(u)| <= M_m ((m - 1)
     h)^(m - i)/(m - i)!): C*_(i,m) = min_kappa [Lambda_(i,m) kappa^-i + ((m - 1) kappa)^(m - i)/(m - i)!].  With the
     Chebyshev-Lobatto nodes on [u - H, u] for i = 1: C^Ch_(1,m) = min_kappa [2 (m - 1)^2 kappa^-1 + kappa^(m-1)/(m -
     1)!] (the first row of the differentiation matrix sums to n^2, n = m - 1, certified).  Each new constant checked
     as W1 was, on exp(-1/x) at (i, m) = (1, 6), (3, 6), (2, 8).  Control: the bound without interpolation (exponent 1
     on E) fails near the edge.
  L4 (exact and certified) lam_L assembled at P*.  nu(5/2) = -196/15625 and |nu| increases on rho > rho* (d nu/d rho =
     -(rho^2 + 2)(2 rho^3 - 3 rho^2 - 2)/(6 rho^7)), so nu_* := min |nu| on W_lam = 196/15625 and no modulus condition on
     nu is needed at P*; d_* = min |d| = 8/3 (at zeta = 0; the real critical points of |d|^2 found exactly); C_m0 =
     (A^2/(9 mu0)) (1 + mu_end^(1/4)) bounds m0 by C_m0 (int env^2 + env^2) (D3).  The thresholds of the conditions of
     Theorem L that involve no constant of Theorem 1 are computed: Lam_4(C1) (Lemma L.6's hypothesis; its value at C1 =
     0 is an upper bound), Lam_5 (L.4's hypothesis eps_M <= lam^3), Lam_8a (the margin against the signal), for the
     round-1 constants and the amended ones; and the rest are printed as formulas in C1, C_Phi, C_L11, C_L4 and lam0.
     Control: at 1.01 times each computed threshold its inequality fails.
     [Round 4, verifier of round 3 (M2): Lam_4, Lam_5 and Lam_8b-d decrease in M_m, and B is an UPPER bound of M_m, so
     the thresholds printed here are LOWER bounds of the thresholds the proof delivers (values of lam below which each
     condition certainly holds), not upper bounds; certified upper bounds use a lower bound of M_m and are in
     lamL5b.py M5.]

Labels: computed (exact rationals and integers; mpmath interval arithmetic, outward rounded, for B(m), the Chebyshev
sum and the thresholds; the m = 400 series value in floating point at 200 and 280 digits).  Every bound on lam_L here is
on the threshold this proof delivers (CONSTANTS5 V-M2), not on the largest lam for which Theorem L holds.
Run: python3 checks/lamL5.py   (about a minute)
"""
import math
import sys
import textwrap
import time
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp
from mpmath import iv

iv.prec = 120
mp.mp.dps = 40
T0 = time.time()
C_HI = iv.mpf('1.3241034918')          # CONSTANTS5 envelope5 E1: c in [1.32407110621, 1.3241034918]
E_K = [1.324, 3.077, 18.6, 95.75, 739.5, 5166.0, 4.611e4, 3.841e5, 3.78e6, 3.539e7, 3.733e8, 3.796e9, 4.214e10,
       4.552e11, 5.248e12]                # envelope5 E2 (certified upper bounds, within a factor 2 of sampled values)
P_, M_, MM = 14, 26, 1456
N_ = 9
DTAU = iv.mpf('5.937209')                 # tau_end - tau0 at P*, CONSTANTS5 1.4 (certified upper bound)


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


def lg(x):
    """log10 of a positive Fraction or int, in interval arithmetic"""
    x = Fr(x)
    return iv.log(iv.mpf(x.numerator))/iv.log(10) - iv.log(iv.mpf(x.denominator))/iv.log(10)


def hi(x):
    return mp.mpf(x.b) if hasattr(x, 'b') else mp.mpf(x)


# ------------------------------------------------------------------------------------------------------------ L1
def l1(control=False):
    x = sp.Symbol('x', positive=True)
    if control:
        mp.mp.dps = 60
        t = mp.mpf(2)/3*mp.mpf('1e-3')
        beta = lambda tt: mp.sin(mp.pi*tt/2)**12*mp.exp(1 - 1/(tt*(2 - tt)))          # noqa: E731
        d4 = mp.diff(beta, t, 4, h=t**2/1000)*(mp.mpf(2)/3)**4*mp.mpf('1.3241')
        mp.mp.dps = 40
        return abs(d4) > mp.mpf('1e-100')
    env = sp.sin(sp.pi*x/3)**4
    ders = [sp.limit(sp.diff(env, x, k), x, 0, '+') for k in range(7)]
    want = [0, 0, 0, 0, 24*(sp.pi/3)**4, 0, -480*(sp.pi/3)**6]
    exact = all(sp.simplify(a - b) == 0 for a, b in zip(ders, want))
    u = sp.Symbol('u')
    expand = sp.simplify(sp.sin(u)**4 - (3 - 4*sp.cos(2*u) + sp.cos(4*u))/8) == 0
    out("  L1 sin^4 edge: one-sided derivatives at v_s+ (k = 0..6) %s; = 0, 0, 0, 0, 24 (pi/3)^4, 0, -480 (pi/3)^6: %s;"
        " jump of env^(4): %s; sin^4 = (3 - 4 cos 2u + cos 4u)/8: %s" % (ders, exact, sp.N(want[4], 8), expand))
    return exact and expand


# ------------------------------------------------------------------------------------------------------------ L2
def log10_B(m, theta):
    th = iv.mpf(theta)
    lfac = iv.log(iv.mpf(math.factorial(m)))
    cosh = (iv.exp(iv.pi*th/2) + iv.exp(-iv.pi*th/2))/2
    val = (iv.log(C_HI) + m*iv.log(iv.mpf(2)/3) + lfac + iv.mpf(3)/4 + 12*iv.log(cosh)
           + m*iv.log(2*(1 + th)*m/(iv.exp(1)*th)))
    return val/iv.log(10)


def best_B(m):
    cands = [1 - mp.mpf(2)**-k for k in range(1, 40)] + [mp.mpf(k)/100 for k in range(5, 100, 5)]
    vals = [(hi(log10_B(m, th)), th) for th in cands]
    return min(vals)


def series_value(m, t0, dps):
    """|beta^(m)| at t = 1 + y = t0 by power-series arithmetic (beta = sin^12(pi t/2) exp(1 - 1/(t (2 - t))))"""
    mp.mp.dps = dps
    t0 = mp.mpf(t0)
    G = [-(((-1)**k)/t0**(k + 1) + 1/(2 - t0)**(k + 1))/2*t0**k for k in range(m + 1)]
    G[0] += 1
    F = [mp.e**G[0]] + [mp.mpf(0)]*m
    for n in range(1, m + 1):
        F[n] = mp.fsum(k*G[k]*F[n - k] for k in range(1, n + 1))/n
    w = mp.pi/2
    S = [(mp.sin(w*t0) if k % 2 == 0 else mp.cos(w*t0))*(-1)**(k//2)*(w*t0)**k/mp.factorial(k) for k in range(m + 1)]

    def mul(A, B):
        return [mp.fsum(A[k]*B[n - k] for k in range(n + 1)) for n in range(m + 1)]
    S2 = mul(S, S)
    S4 = mul(S2, S2)
    S12 = mul(mul(S4, S4), S4)
    c = mp.fsum(S12[k]*F[m - k] for k in range(m + 1))
    res = abs(c)/t0**m*mp.factorial(m)
    mp.mp.dps = 40
    return res


def l2(control=False):
    m0 = 400
    if 'ser' not in CACHE:
        a = series_value(m0, mp.mpf(1)/(4*m0), 200)
        b = series_value(m0, mp.mpf(1)/(4*m0), 280)
        mp.mp.dps = 150
        CACHE['ser'] = (a, abs(a/b - 1))
        mp.mp.dps = 40
    ser, stab = CACHE['ser']          # stab: relative difference of the two precisions, compared at 150 digits
    lser = mp.log10(ser*mp.mpf('1.3240711')*(mp.mpf(2)/3)**m0)          # |env^(400)| at that point, lower c
    lb400, th400 = best_B(m0)
    if control:
        nofac = lb400 - hi(iv.log(iv.mpf(math.factorial(m0)))/iv.log(10))
        return nofac >= lser
    lb, th = best_B(MM)
    cross = all(mp.mpf(10)**best_B(k)[0] >= mp.mpf(E_K[k])/2 for k in range(1, 15))
    ok = cross and lser <= lb400 and stab < mp.mpf(10)**-100
    CACHE['logB'] = lb
    thtxt = "1 - 2^-%d" % int(round(-mp.log(1 - th, 2))) if th > mp.mpf('0.99') else mp.nstr(th, 8)
    out("  L2 log10 B(1456) <= %s (theta = %s), so M_1456^(1/1456) <= %s; B(k) >= e_k/2 for k = 1..14: %s; at m = 400:"
        " log10 B = %s, the series value log10 |env^(400)| = %s (200 and 280 digits agree, relative difference %s at"
        " 150 digits): below B: %s  [%.0f s]"
        % (mp.nstr(lb, 10), thtxt, mp.nstr(mp.mpf(10)**(lb/MM), 5), cross, mp.nstr(lb400, 8),
           mp.nstr(lser, 8), mp.nstr(stab, 3), lser <= lb400, time.time() - T0))
    return ok


# ------------------------------------------------------------------------------------------------------------ L3
def lam_eq(i_list, m):
    """Lambda_(i,m) = sum_k |l_k^(i)(0)| on the nodes 0, -1, ..., -(m-1), exactly"""
    p = [1]
    for j in range(m):
        q = [0]*(len(p) + 1)
        for n, c in enumerate(p):
            q[n] += j*c
            q[n + 1] += c
        p = q
    res = {i: Fr(0) for i in i_list}
    imax = max(i_list)
    for k in range(m):
        if k == 0:
            qc = p[1:imax + 2]
        else:
            qc, prev = [], 0
            for n in range(imax + 1):
                val = p[n] - prev
                prev = val//k
                qc.append(prev)
        den = math.factorial(k)*math.factorial(m - 1 - k)
        for i in i_list:
            res[i] += Fr(math.factorial(i)*abs(qc[i]), den)
    return res


def cstar(lam_i, i, m, kind="eq"):
    """min over kappa of Lam kappa^-i + ((m - 1) kappa)^(m - i)/(m - i)! ('eq') or kappa^(m-1)/(m-1)! ('ch', i = 1)"""
    mp.mp.dps = 60
    L = mp.mpf(lam_i.numerator)/lam_i.denominator if isinstance(lam_i, Fr) else mp.mpf(lam_i)
    if kind == "eq":
        f = lambda lk: L*mp.e**(-i*lk) + mp.e**((m - i)*(mp.log(m - 1) + lk) - mp.loggamma(m - i + 1))   # noqa: E731
    else:
        f = lambda lk: L*mp.e**(-lk) + mp.e**((m - 1)*lk - mp.loggamma(m))                              # noqa: E731
    grid = [mp.mpf(k)/200 for k in range(-2000, 2000)]
    best = min(grid, key=f)
    val = f(best)*(1 + mp.mpf(10)**-30)
    mp.mp.dps = 40
    return val, mp.e**best


def w1_check(const_fn, control=False):
    ok = True
    for (i, m) in ((1, 6), (3, 6), (2, 8)):
        C = const_fn(i, m)
        grid = [mp.mpf(k)/400 for k in range(4, 121)]
        Mm, worst, sup_i = mp.mpf(0), mp.mpf(0), mp.mpf(0)
        for x in grid:
            Mm = max(Mm, abs(mp.diff(lambda y: mp.e**(-1/y), x, m)))
            sup_i = max(sup_i, abs(mp.diff(lambda y: mp.e**(-1/y), x, i)))
            E = mp.e**(-1/x)
            rhs = C*E if control else C*E**(1 - mp.mpf(i)/m)*Mm**(mp.mpf(i)/m)
            worst = max(worst, sup_i/rhs)
        ok &= worst <= 1
    return ok


def ch_const(m):
    n = m - 1
    s = iv.mpf(2*n**2 + 1)/6 + iv.mpf(1)/2
    for j in range(1, n):
        s += 2/(1 - iv.cos(j*iv.pi/n))
    return s


def l3(control=False):
    small = {m: lam_eq([1, 2, 3], m) for m in (6, 8)}
    closed = all(small[m][1] == sum(Fr(1, j) for j in range(1, m)) + sum(Fr(math.comb(m - 1, k), k)
                                                                         for k in range(1, m)) for m in (6, 8))
    r1 = small[6][1] + 5**5 == Fr(47131, 15) and small[6][3] + 5**3 == 213 and small[8][2] + 7**6 == Fr(5302829, 45)

    def eq_star(i, m):
        return cstar(lam_eq([i], m)[i], i, m)[0]

    def ch_star(i, m):
        return cstar(hi(2*ch_const(m)), 1, m, "ch")[0] if i == 1 else eq_star(i, m)
    if control:
        return w1_check(eq_star, control=True) or w1_check(ch_star, control=True)
    w_eq, w_ch = w1_check(eq_star), w1_check(ch_star)
    big = lam_eq(list(range(0, M_ + 1)), MM) if 'big' not in CACHE else CACHE['big']
    big[0] = Fr(1)
    CACHE['big'] = big
    c1_r1 = lg(big[1] + (MM - 1)**(MM - 1))
    cM_r1 = lg(big[M_] + (MM - 1)**(MM - M_))
    c_star = {i: cstar(big[i], i, MM) for i in (1, M_)}
    chs = ch_const(MM)
    cheb_exact = (MM - 1)**2 in chs
    c_ch = cstar(hi(2*chs), 1, MM, "ch")
    CACHE['C1'] = {'r1': mp.mpf(10)**hi(c1_r1), 'eq': c_star[1][0], 'ch': c_ch[0]}
    CACHE['Ci'] = {i: {'r1': mp.mpf(big[i].numerator)/big[i].denominator + mp.mpf(MM - 1)**(MM - i),
                       'eq': cstar(big[i], i, MM)[0] if i > 0 else mp.mpf(1)} for i in range(0, M_ + 1)}
    CACHE['Ci'][0] = {'r1': mp.mpf(1), 'eq': mp.mpf(1)}
    out("  L3 Lambda_(1,m) closed form (m = 6, 8): %s; round 1's C at (1,6), (3,6), (2,8) reproduced: %s; W1 with the"
        " amended constants (equal nodes, Chebyshev at i = 1): %s, %s.  m = 1456: log10 Lambda_(1,m) = %s, log10"
        " Lambda_(26,m) = %s; round 1: log10 C_(1,m) = %s, log10 C_(26,m) = %s; amended: log10 C*_(1,m) = %s, log10"
        " C*_(26,m) = %s; Chebyshev first-row sum = n^2 = %d (certified): %s, log10 C^Ch_(1,m) = %s  [%.0f s]"
        % (closed, r1, w_eq, w_ch, mp.nstr(hi(lg(big[1])), 8), mp.nstr(hi(lg(big[M_])), 8), mp.nstr(hi(c1_r1), 8),
           mp.nstr(hi(cM_r1), 8), mp.nstr(mp.log10(c_star[1][0]), 6), mp.nstr(mp.log10(c_star[M_][0]), 6),
           (MM - 1)**2, cheb_exact, mp.nstr(mp.log10(c_ch[0]), 6), time.time() - T0))
    return closed and r1 and w_eq and w_ch and cheb_exact


# ------------------------------------------------------------------------------------------------------------ L4
def l4(control=False):
    rho, z = sp.symbols('rho z', positive=True)
    nu = -(2*rho**3 - 3*rho**2 - 2)**2/(36*rho**6)
    nus = nu.subs(rho, sp.Rational(5, 2))
    dnu = sp.factor(sp.diff(nu, rho))
    mono = sp.simplify(dnu + (rho**2 + 2)*(2*rho**3 - 3*rho**2 - 2)/(6*rho**7)) == 0
    zz = sp.Symbol('zeta', real=True)
    P = -2*zz**5 - sp.Rational(20, 3)*zz**3 - sp.Rational(20, 3)*zz**2 - sp.Rational(38, 3)*zz + sp.Rational(4, 3)
    d2 = 2*(P**2 + P.subs(zz, -zz)**2)/(1 + zz**2)**5
    crit = [rt for rt in sp.real_roots(sp.Poly(sp.numer(sp.together(sp.diff(d2, zz))), zz)) if -1 <= rt <= 1]
    vals = [sp.nsimplify(d2.subs(zz, rt)) if rt == 0 else sp.N(d2.subs(zz, rt), 30) for rt in crit]
    vals += [d2.subs(zz, 1), d2.subs(zz, -1)]
    dmin2 = min(vals, key=lambda q: sp.N(q, 30))
    d_star = sp.sqrt(dmin2)
    mu_end = sp.Rational(227, 192)
    c_m0 = (1 + mu_end**sp.Rational(1, 4))/9
    Ks, ds, cm = mp.mpf(sp.N(-nus, 30)), mp.mpf(sp.N(d_star, 30)), mp.mpf(sp.N(c_m0, 30))
    p, M, m, N = P_, M_, MM, N_
    Mm1m = mp.mpf(10)**(CACHE['logB']/m)
    res = {}
    for kind in ('r1', 'eq', 'ch'):
        C1m = CACHE['C1'][kind if kind != 'ch' else 'ch']
        # Lam_4(C1): lam^(1 - p/m) (4 pi + 2 C1 dtau) 4 2^(1-1/m) C_(1,m) M_m^(1/m) <= 1; at C1 = 0 an upper bound
        base4 = 4*2**(1 - mp.mpf(1)/m)*C1m*Mm1m*4*mp.pi
        lam4 = base4**(-mp.mpf(m)/(m - p))
        # Lam_5: sum_(i<=M) C_(i,m) (5/4)^(1-i/m) M_m^(i/m) lam^(p (1 - i/m)) <= lam^3, each term <= lam^3/(M+1)
        ck = 'eq' if kind == 'ch' else kind
        lam5 = min(((M + 1)*CACHE['Ci'][i][ck]*(mp.mpf(5)/4)**(1 - mp.mpf(i)/m)*Mm1m**i)
                   ** (-1/(p*(1 - mp.mpf(i)/m) - 3)) for i in range(0, M + 1))
        ceps = sum(CACHE['Ci'][i][ck]*(mp.mpf(5)/4)**(1 - mp.mpf(i)/m)*Mm1m**i for i in range(0, M + 1))
        res[kind] = (lam4, lam5, ceps)
    # Lam_8a: the margin, m0 <= C_m0 (25/16) y^2 (1 + 1) with v1 - v_s <= 1, against an eighth of lam^3 A (3y/4) nu_* d_*
    lam8a = (3*Ks*ds/(32*cm*mp.mpf(25)/8))**(1/mp.mpf(p - 3))
    if control:
        bad = False
        for kind in ('r1', 'eq', 'ch'):
            lam4, lam5, _ = res[kind]
            C1m = CACHE['C1'][kind]
            x = lam4*mp.mpf('1.01')
            bad |= x**(1 - mp.mpf(p)/m)*4*2**(1 - mp.mpf(1)/m)*C1m*Mm1m*4*mp.pi <= 1
        x = lam8a*mp.mpf('1.01')
        bad |= cm*mp.mpf(25)/8*x**(2*p) <= 3*Ks*ds*x**(3 + p)/32
        return bad
    ok = mono and abs(sp.N(dmin2 - sp.Rational(64, 9), 30)) < 1e-25 and nus == sp.Rational(-196, 15625)
    gain = 3*Ks*ds/32
    out("  L4 nu(5/2) = %s; d nu/d rho = %s (so |nu| increases on rho > rho*): %s; d_*^2 = %s at zeta = 0 (critical"
        " points %d); C_m0 = %s.  Thresholds (no constant of Theorem 1; with B >= M_m, so lower bounds of the"
        " proof's thresholds): Lam_4(C1 = 0), Lam_5, round 1's L.5: %s, %s;"
        " amended L.5: %s, %s; with Chebyshev nodes at i = 1: Lam_4(0) = %s; Lam_8a = %s.  Formulas: Lam_4(C1) ="
        " Lam_4(0) (1 + C1 dtau/(2 pi))^(-m/(m - p)), dtau <= 5.937209; Lam_6 = (288 mu0 C_Phi/(25 A^2))^(1/27);"
        " Lam_8b = (G/(C_L11 C_eps))^(4/3), Lam_8c = (G/(C_L11 C_eps^2))^(1/11.5), Lam_8d = (G/(C_L4 C_eps))^(4/3), G :="
        " 3 A nu_* d_*/32 = %s, log10 C_eps = %s (round 1), %s (amended)"
        % (nus, dnu, mono, dmin2, len(crit), sp.N(c_m0, 8), mp.nstr(res['r1'][0], 5), mp.nstr(res['r1'][1], 5),
           mp.nstr(res['eq'][0], 5), mp.nstr(res['eq'][1], 5), mp.nstr(res['ch'][0], 5), mp.nstr(lam8a, 6),
           mp.nstr(gain, 6), mp.nstr(mp.log10(res['r1'][2]), 7), mp.nstr(mp.log10(res['eq'][2]), 7)))
    CACHE['L4'] = res, lam8a
    return ok and all(res[k][0] < 1 and res[k][1] < 1 for k in res) and lam8a < 1


CACHE = {}


def main():
    ok = True
    for name, f in (("L1", l1), ("L2", l2), ("L3", l3), ("L4", l4)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("lamL5: %s  [%.0f s]" % ("all checks pass, every control fails" if ok else "FAILURES", time.time() - T0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
