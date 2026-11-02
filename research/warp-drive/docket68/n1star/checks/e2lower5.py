#!/usr/bin/env python3
"""e2lower5.py -- a certified LOWER bound for the E2 norm ||chi_I R_l(sigma) chi_I|| (verifier 259's item 4, D605).

E2-PILOT.md's operator (checks/e2high5.py): five-dimensional Tangherlini of mass 1, f = 1 - 1/r^2, r_* with dr_*/dr =
1/f, P_l = -d^2/dr_*^2 + V_l, V_l = f ((l (l + 2) + 3/4)/r^2 + 9/(4 r^4)), R_l(sigma) = (P_l - sigma^2)^-1 the outgoing
resolvent, I = {1.2 <= r <= 4}, chi_I its indicator, the norm of L^2(dr_*). The paper's 9.5-22 compares the certified
upper bound with this norm computed in floating point (checks/e2meas5.py); here the norm is bounded below rigorously.

The bound. If u is in H^2 with compact support in I (u and u' vanish at the ends), (P_l - sigma^2) u = g is supported in
I and u is the outgoing solution of (P_l - sigma^2) v = g (it vanishes near both ends of the line, and for real sigma !=
0 the outgoing solution is unique), so u = R_l(sigma) g = chi_I R_l chi_I g and

    ||chi_I R_l(sigma) chi_I|| >= ||u|| / ||(P_l - sigma^2) u||        (deduced; the equality u = R g is standard).

The test functions are u = (r - a)^2 (b - r)^2 q(r), [a, b] inside I, q a polynomial of degree K - 1 whose coefficients
(in Legendre polynomials of the variable mapped to [-1, 1]) are chosen in floating point to make the quotient large (the
least generalized eigenvalue of the two Gram matrices), then rounded to rationals: the certificate uses only those
rationals. With N(r) := r^6 (P_l - sigma^2) u = -(r^2 - 1)^2 r^2 u'' - 2 (r^2 - 1) r u' + ((r^2 - 1)(L r^2 + 9/4) -
sigma^2 r^6) u (u' = du/dr, L = l (l + 2) + 3/4), both norms are integrals of polynomials times decreasing weights:
||u||^2 = int u^2 r^2/(r^2 - 1) dr and ||g||^2 = int N^2 r^-10/(r^2 - 1) dr; on each of M subintervals the weight is
bracketed by its end values and the polynomial integrated exactly (integer arithmetic), so the quotient is bounded below
by a rational, whose square root is taken downward.

  E1 (certified, exact arithmetic) At sigma = 3, 6, 12, 24, 48, 96 and the harmonic l the measurement found extremal (or
     a neighbour), the lower bound below; with the certified upper bound of the same band (E2-PILOT.md), the certified
     bound lies at most U/L times above the norm, U/L printed beside the floating-point ratio.
  Control: a test function vanishing only to first order at the ends, u = (r - a)(b - r) q, is not in H^2 on the line
     (its extension by zero has a jump in u'), and the check refuses it.

Labels: computed (exact; the floating point only chooses the test function).

Run: python3 checks/e2lower5.py   (about ten minutes)
"""
import math
import os
import sys
from fractions import Fraction as Fr

import numpy as np
from numpy.polynomial import legendre as Lg

# (sigma, l, a, b, K): the band of each measured sigma; U the certified upper bound there (E2-PILOT.md)
CASES = [(3, 6, Fr(6, 5), Fr(4), 40, Fr("11.086"), Fr("1.132")),          # U: checks/e2trapband5_384.out:42-47
         (6, 11, Fr(6, 5), Fr(4), 60, Fr("5.8726"), Fr("0.61801")),       # measured: e2high5.py H3, e2meas5.py
         (12, 23, Fr(6, 5), Fr(4), 160, Fr("3.7719"), Fr("0.33551")),
         (24, 47, Fr(6, 5), Fr(4), 120, Fr("2.3724"), Fr("0.18101")),
         (48, 95, Fr(6, 5), Fr(4), 120, Fr("1.5222"), Fr("0.097196")),
         (96, 191, Fr(6, 5), Fr(4), 160, Fr("0.99697"), Fr("0.051938"))]
MSUB = 200


# ---- exact polynomials (lists of Fractions, index = power) ------------------------------------------------------------
def padd(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]


def pmul(p, q):
    out = [Fr(0)]*(len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                out[i + j] += a*b
    return out


def pscale(p, c):
    return [c*a for a in p]


def pder(p):
    return [i*p[i] for i in range(1, len(p))] or [Fr(0)]


def peval(p, x):
    acc = Fr(0)
    for a in reversed(p):
        acc = acc*x + a
    return acc


def pint_exact(p, x0, x1):
    """int_x0^x1 p exactly, with integer arithmetic for speed"""
    ant = [Fr(0)] + [a/(i + 1) for i, a in enumerate(p)]
    den = 1
    for a in ant:
        den = den*a.denominator//math.gcd(den, a.denominator)
    ints = [int(a*den) for a in ant]

    def ev(x):
        num, d = x.numerator, x.denominator
        n = len(ints) - 1
        acc = 0
        for k in range(n, -1, -1):
            acc = acc*num + ints[k]*d**(n - k) if k < n else ints[k]
        return Fr(acc, den*d**n)
    return ev(x1) - ev(x0)


def legendre_in_r(K, a, b):
    """P_k((2 r - a - b)/(b - a)) as exact polynomials in r, k < K"""
    t = [-(a + b)/(b - a), Fr(2)/(b - a)]
    P = [[Fr(1)], t]
    for k in range(1, K - 1):
        P.append(padd(pscale(pmul(t, P[k]), Fr(2*k + 1, k + 1)), pscale(P[k - 1], Fr(-k, k + 1))))
    return P[:K]


# ---- the floating-point choice of q ---------------------------------------------------------------------------------
def choose(sig, l, a, b, K, nq=1600):
    x, wq = Lg.leggauss(nq)
    a_, b_ = float(a), float(b)
    r = (a_ + b_)/2 + (b_ - a_)/2*x
    f, fp = 1 - 1/r**2, 2/r**3
    w = (r - a_)**2*(b_ - r)**2
    wp = 2*(r - a_)*(b_ - r)**2 - 2*(r - a_)**2*(b_ - r)
    wpp = 2*(b_ - r)**2 - 8*(r - a_)*(b_ - r) + 2*(r - a_)**2
    dt = 2/(b_ - a_)
    B, Bp, Bpp = [], [], []
    for k in range(K):
        c = np.zeros(k + 1)
        c[k] = 1
        P0, P1, P2 = Lg.legval(x, c), Lg.legval(x, Lg.legder(c))*dt, Lg.legval(x, Lg.legder(c, 2))*dt**2
        B.append(w*P0)
        Bp.append(wp*P0 + w*P1)
        Bpp.append(wpp*P0 + 2*wp*P1 + w*P2)
    B, Bp, Bpp = map(np.array, (B, Bp, Bpp))
    Lv = l*(l + 2) + 0.75
    A = -f**2*Bpp - f*fp*Bp + (f*(Lv/r**2 + 2.25/r**4) - sig**2)*B
    meas = wq*(b_ - a_)/2/f
    G, M = (B*meas) @ B.T, (A*meas) @ A.T
    Lc = np.linalg.cholesky(G)
    Li = np.linalg.inv(Lc)
    ev, vec = np.linalg.eigh(Li @ M @ Li.T)
    return 1/math.sqrt(ev[0]), Li.T @ vec[:, 0]


# ---- the certificate ------------------------------------------------------------------------------------------------
def certify(sig, l, a, b, K, coeffs, order=2):
    P = legendre_in_r(K, a, b)
    q = [Fr(0)]
    for k, ck in enumerate(coeffs):
        q = padd(q, pscale(P[k], Fr(ck).limit_denominator(10**12)))
    w = pmul([-a, Fr(1)], [b, Fr(-1)])
    w_ = [Fr(1)]
    for _ in range(order):
        w_ = pmul(w_, w)
    u = pmul(w_, q)
    u1, u2 = pder(u), pder(pder(u))
    ends_ok = all(peval(p_, e) == 0 for p_ in (u, u1) for e in (a, b))
    if not ends_ok:
        return None
    s2 = Fr(sig)**2
    Lv = Fr(l*(l + 2)) + Fr(3, 4)
    rr = [Fr(0), Fr(1)]
    r2m1 = [Fr(-1), Fr(0), Fr(1)]
    N = padd(padd(pscale(pmul(pmul(pmul(r2m1, r2m1), pmul(rr, rr)), u2), -1), pscale(pmul(pmul(r2m1, rr), u1), -2)),
             pmul(padd(pmul(r2m1, [Fr(9, 4), Fr(0), Lv]), pscale([Fr(0)]*6 + [Fr(1)], -s2)), u))
    u_sq, N_sq = pmul(u, u), pmul(N, N)
    lo_u, hi_g = Fr(0), Fr(0)
    pts = [a + (b - a)*Fr(j, MSUB) for j in range(MSUB + 1)]
    for x0, x1 in zip(pts, pts[1:]):
        h0_lo = x1*x1/(x1*x1 - 1)                                   # r^2/(r^2 - 1), decreasing
        h_hi = 1/(x0**10*(x0*x0 - 1))                               # r^-10/(r^2 - 1), decreasing
        lo_u += h0_lo*pint_exact(u_sq, x0, x1)
        hi_g += h_hi*pint_exact(N_sq, x0, x1)
    q2 = lo_u/hi_g
    s = math.isqrt(q2.numerator*q2.denominator*10**24//q2.denominator**2)      # floor(sqrt(q2) 10^12)
    return Fr(s, 10**12)


def e1(control=False):
    if control:
        sig, l, a, b, K = CASES[0][:5]
        _, c = choose(sig, l, a, b, 12)
        return certify(sig, l, a, b, 12, c, order=1) is not None
    ok = True
    for sig, l, a, b, K, U, meas in CASES:
        fl, c = choose(sig, l, a, b, K)
        L = certify(sig, l, a, b, K, c)
        ok &= L is not None and L > 0 and float(L) <= fl*1.0001
        ratio = "U/L = %.1f against the floating U/norm %.2f" % (float(U/L), float(U/meas))
        print("  E1: sigma = %s, l = %d, u on [%s, %s], K = %d: ||chi R chi|| >= %.6f (floating %.6f; measured norm "
              "%.5f) %s" % (sig, l, a, b, K, float(L), fl, float(meas), ratio), flush=True)
    return ok


CHECKS = [("E1", e1)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
