#!/usr/bin/env python3
"""lamL5b.py -- lam_L at P* updated (EQUALITY5-LAYER.md, Round 4, R4.5): CONSTANTS5's lambda0 < 0.0024433, C_Phi in
terms of C1, and the window's hypothesis term under Lemma L.4' (Round 4, R4.3), with interpolation constants on
Chebyshev-Lobatto nodes to order 4.

The point P* of CONSTANTS5.md (READ): mu0 = A = 1, the C_c^inf envelope env = c beta((2v - 4)/3), c <= 1.3241034918,
mu in [1, 227/192]; Theorem L's p = 14, N = 9, M* = 26, m = 56 M* = 1456; M_m^(1/m) <= 10^(8573.893584/1456) (lamL5
L2, recomputed here).

  M1 (READ, located by content; md5 printed) CONSTANTS5.md Round 4: lambda0 < 0.0024433 (operator norm), g0's least
     absolute eigenvalue on Omega in [0.030768559, 0.030768560].  Control: the pin with its last digit mutated
     (0.0024432) is found nowhere.
  M2 (certified, interval arithmetic) B := 1 + sup |r_q'| <= 1 + c^2/18 (r_q' = mu0^(1/4) mu^(-3/4) mu'/4, mu' =
     (2/9) env^2, mu >= mu0 = 1), and C_Phi = C1 max_(|beta| <= B) ((1 - beta)^2 + beta^2) = C1 ((1 + B)^2 + B^2): the
     constant of EQUALITY5 section 0 for the covectors dr - beta dv, |dr - beta dv|_e^2 = (1 - beta)^2 + beta^2 in the
     Cartesian components (dv = dtau + dr, dr = xhat . dx).  Control: the maximum taken at beta = +B instead (a
     mutation) is smaller, so it is not the constant.
  M3 (computed) Duffin-Schaeffer: on the Chebyshev-Lobatto nodes cos(k pi/n) the i-th derivative at the endpoint of the
     Lagrange basis has row sum sum_k |l_k^(i)(1)| = T_n^(i)(1) = prod_(j<i) (n^2 - j^2)/(2j + 1) (signs alternating):
     exact to 50 digits at n = 6, 10, 16, 24 and i <= 4, and at n = 1455, i <= 4, in floating point (relative error
     below 1e-9).  Hence C^DS_(i,m) := min_kappa [T_(m-1)^(i)(1) (2/kappa)^i + kappa^(m-i)/(m-i)!] serves in Lemma L.5
     (Round 3, A15's argument with this row sum; the general n is the Duffin-Schaeffer inequality, not re-derived).
     Control: equally spaced nodes do not have that row sum.
  M4 (certified) The hypothesis of Lemma L.4' at the window, eps_4(v1) <= lam with y = lam^14: each term i = 1..4,
     C_(i,m) (5/4)^(1-i/m) M_m^(i/m) lam^(14(1-i/m)) <= lam/5, gives Lam_5' = min_i [5 C_(i,m) (5/4)^(1-i/m)
     M_m^(i/m)]^(-1/(14(1-i/m)-1)); printed for C*_(i,m) (equal nodes, Round 3) and C^DS_(i,m).  The certified upper
     bound of lam_L (no constant of Theorem 1) is then min(lambda0 < 0.0024433, Lam_4(0) = 1.2519e-12 (lamL5 L4),
     Lam_5').  And C_eps (the 26-derivative envelope cost of the error terms Lam_8b-d) with C^DS at every i <= 26.
     Control: at 1.01 Lam_5' the binding term's inequality fails.

Labels: M1 READ; M2, M4 certified (mpmath interval arithmetic, outward); M3 computed (exact digits at small n, floating
point at n = 1455).  Every bound is on the threshold the proof delivers, not on the largest lam for which Theorem L
holds (CONSTANTS5 V-M2).  Run: python3 checks/lamL5b.py   (about two minutes; imports lamL5.py)
"""
import hashlib
import math
import os
import sys
import textwrap
import time
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
from mpmath import iv

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lamL5 as LL                                                                # noqa: E402

T0 = time.time()
iv.prec = 120
P_, MM = 14, 1456
LAM4_0 = mp.mpf('1.2519e-12')          # lamL5 L4 (Chebyshev at i = 1), READ from lamL5.out
LAMBDA0 = mp.mpf('0.0024433')          # CONSTANTS5 Round 4 (READ, M1)


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


# ------------------------------------------------------------------------------------------------------------ M1
def m1(control=False):
    path = os.path.join(HERE, '..', 'CONSTANTS5.md')
    raw = open(path, 'rb').read()
    lines = raw.decode('utf-8').split('\n')
    r4 = next(i for i, ln in enumerate(lines) if ln.startswith('## Round 4'))
    if control:
        return any('lambda0 < 0.0024432' in ln for ln in lines[r4:])          # a mutated pin: must not be found
    hits = [i + 1 for i, ln in enumerate(lines) if i >= r4 and 'lambda0 < 0.0024433' in ln]
    eig = [i + 1 for i, ln in enumerate(lines) if i >= r4 and '[0.030768559, 0.030768560]' in ln]
    out("  M1 CONSTANTS5.md md5 %s: Round 4 at line %d; 'lambda0 < 0.0024433' at lines %s; the eigenvalue interval at"
        " %s" % (hashlib.md5(raw).hexdigest(), r4 + 1, hits, eig))
    return bool(hits) and bool(eig)


# ------------------------------------------------------------------------------------------------------------ M2
def m2(control=False):
    c = LL.C_HI
    B = 1 + c**2/18
    if control:
        Bm = B
        val_m = (1 - Bm)**2 + Bm**2                       # at beta = +B
        return val_m.b >= ((1 + B)**2 + B**2).a
    ratio = (1 + B)**2 + B**2
    lam6 = (iv.mpf(288)/25*ratio)                     # Lam_6 = (lam6 C1)^(1/27)
    thr = (iv.mpf('0.0024433')**27)/lam6
    out("  M2 B <= %s; C_Phi = C1 ((1 + B)^2 + B^2) <= %s C1; Lam_6 = (288 C_Phi/25)^(1/27) <= (%s C1)^(1/27), which"
        " is below lambda0's bound 0.0024433 only if C1 < %s" % (
            mp.nstr(mp.mpf(B.b), 8), mp.nstr(mp.mpf(ratio.b), 8), mp.nstr(mp.mpf(lam6.b), 6), mp.nstr(mp.mpf(thr.b), 4)))
    return ratio.b < 6


# ------------------------------------------------------------------------------------------------------------ M3
def T_der(n, i):
    v = Fr(1)
    for j in range(i):
        v *= Fr(n*n - j*j, 2*j + 1)
    return v


def rowsums_mp(n, imax, nodes="cheb"):
    mp.mp.dps = 50
    if nodes == "cheb":
        x = [mp.cos(k*mp.pi/n) for k in range(n + 1)]
    else:
        x = [1 - mp.mpf(2)*k/n for k in range(n + 1)]
    w = []
    for k in range(n + 1):
        p = mp.mpf(1)
        for j in range(n + 1):
            if j != k:
                p *= (x[k] - x[j])
        w.append(1/p)
    D = [[mp.mpf(0)]*(n + 1) for _ in range(n + 1)]
    for a in range(n + 1):
        for b in range(n + 1):
            if a != b:
                D[a][b] = w[b]/w[a]/(x[a] - x[b])
        D[a][a] = -mp.fsum(D[a][b] for b in range(n + 1) if b != a)
    row = [mp.mpf(1) if k == 0 else mp.mpf(0) for k in range(n + 1)]
    res = []
    for _ in range(imax):
        row = [mp.fsum(row[a]*D[a][b] for a in range(n + 1)) for b in range(n + 1)]
        alt = all((row[k] > 0) == ((-1)**k*row[0] > 0) for k in range(n + 1))
        res.append((mp.fsum(abs(z) for z in row), alt))
    mp.mp.dps = 40
    return res


def rowsums_np(n, imax):
    k = np.arange(n + 1)
    x = np.cos(k*np.pi/n)
    cw = np.ones(n + 1)
    cw[0] = cw[-1] = 2
    w = (-1.0)**k/cw                                    # barycentric weights of the Chebyshev-Lobatto points
    X = x[:, None] - x[None, :]
    np.fill_diagonal(X, 1.0)
    D = (w[None, :]/w[:, None])/X
    np.fill_diagonal(D, 0.0)
    np.fill_diagonal(D, -D.sum(axis=1))
    row = np.zeros(n + 1)
    row[0] = 1.0
    res = []
    for _ in range(imax):
        row = row @ D
        alt = bool(np.all(np.sign(row) == np.sign(row[0])*(-1.0)**k))
        res.append((float(np.abs(row).sum()), alt))
    return res


LFAC = {k: iv.log(iv.mpf(math.factorial(k))) for k in range(MM - 5, MM)}


def cds(i, m):
    """C^DS_(i,m) = min_kappa [T_(m-1)^(i)(1) (2/kappa)^i + kappa^(m-i)/(m-i)!], certified at the grid minimiser"""
    Tn = T_der(m - 1, i)
    Ti = iv.mpf(Tn.numerator)/Tn.denominator
    best = None
    for k10 in range(1, 3000):
        kap = iv.mpf(k10)/4
        val = Ti*(2/kap)**i + iv.exp((m - i)*iv.log(kap) - LFAC[m - i])
        if best is None or val.b < best[0].b:
            best = (val, kap)
    return best


def m3(control=False):
    if control:
        r = rowsums_mp(10, 3, nodes="eq")
        return all(abs(s - mp.mpf(T_der(10, i + 1).numerator)/T_der(10, i + 1).denominator) < mp.mpf(10)**-30
                   for i, (s, _) in enumerate(r))
    ok = True
    for n in (6, 10, 16, 24):
        r = rowsums_mp(n, 4)
        for i, (s, alt) in enumerate(r):
            Ti = mp.mpf(T_der(n, i + 1).numerator)/T_der(n, i + 1).denominator
            ok &= abs(s/Ti - 1) < mp.mpf(10)**-40 and alt
    big = rowsums_np(MM - 1, 4)
    rel = [abs(s/float(T_der(MM - 1, i + 1)) - 1) for i, (s, _) in enumerate(big)]
    altb = all(a for _, a in big)
    ok &= max(rel) < 1e-9 and altb
    out("  M3 row sums = T_n^(i)(1), signs alternating, n = 6, 10, 16, 24 and i <= 4 (50 digits): %s; n = 1455: relative"
        " errors %s, alternating: %s; log10 T_1455^(i)(1), i = 1..4: %s  [%.0f s]" % (
            ok, ", ".join("%.1e" % e for e in rel), altb,
            ", ".join("%.4f" % math.log10(float(T_der(MM - 1, i))) for i in range(1, 5)), time.time() - T0))
    return ok


# ------------------------------------------------------------------------------------------------------------ M4
def m4(control=False):
    lb, _ = LL.best_B(MM)
    lMm = iv.mpf(lb)/MM                                  # log10 M_m^(1/m) (upper)
    if 'eq' not in CACHE:
        lam = LL.lam_eq([1, 2, 3, 4], MM)
        CACHE['eq'] = {i: LL.cstar(lam[i], i, MM)[0] for i in (1, 2, 3, 4)}
        CACHE['ds'] = {i: cds(i, MM)[0] for i in (1, 2, 3, 4)}
    res = {}
    for kind in ('eq', 'ds'):
        terms = {}
        for i in (1, 2, 3, 4):
            Ci = CACHE[kind][i]
            lC = iv.log(iv.mpf(Ci) if kind == 'eq' else Ci)/iv.log(10)
            lbase = iv.log(iv.mpf(5))/iv.log(10) + lC + (1 - iv.mpf(i)/MM)*iv.log(iv.mpf(5)/4)/iv.log(10) + i*lMm
            expo = P_*(1 - iv.mpf(i)/MM) - 1
            terms[i] = (-lbase/expo, lbase, expo)
        ib = min(terms, key=lambda i: terms[i][0].b)
        res[kind] = (terms[ib][0], ib, terms)
    if control:
        lthr, ib, terms = res['ds']
        lam = mp.mpf(10)**mp.mpf(lthr.b)*mp.mpf('1.01')
        lbase, expo = terms[ib][1], terms[ib][2]
        return mp.mpf(lbase.a) + mp.mpf(expo.a)*mp.log10(lam) <= 0          # the inequality at 1.01 Lam_5': must fail
    bound = min(LAMBDA0, LAM4_0, mp.mpf(10)**mp.mpf(res['ds'][0].b))
    # C_eps = sum_(i<=26) C_(i,m) (5/4)^(1-i/m) M_m^(i/m) with the Duffin-Schaeffer constants (round 3: 10^613.2166)
    if 'ceps' not in CACHE:
        tot = iv.mpf(5)/4
        for i in range(1, 27):
            tot += cds(i, MM)[0]*(iv.mpf(5)/4)**(1 - iv.mpf(i)/MM)*iv.mpf(10)**(i*lMm)
        CACHE['ceps'] = iv.log(tot)/iv.log(10)
    lce = CACHE['ceps']
    G = iv.mpf(3)*iv.mpf(196)/15625*(iv.mpf(8)/3)/32                      # G = 3 A nu_* d_*/32 (lamL5 L4)
    lG = iv.log(G)/iv.log(10)
    l8b = (lG - lce)*iv.mpf(4)/3
    l8c = (lG - 2*lce)/iv.mpf('11.5')
    out("  M4 log10 M_m^(1/m) <= %s.  Lam_5' (L.4' hypothesis eps_4 <= lam at y = lam^14): with C*_(i,m) (equal nodes)"
        " log10 Lam_5' <= %s (binding i = %d); with C^DS_(i,m) log10 Lam_5' <= %s (binding i = %d); log10 C^DS_(i,m),"
        " i = 1..4: %s.  Certified: lam_L <= min(lambda0 < 0.0024433, Lam_4(0) = 1.2519e-12, Lam_5') = %s.  With"
        " C^DS at every i <= 26: log10 C_eps <= %s (round 3: 613.2166), so Lam_8b, Lam_8d <= 10^(%s) min(C_L11,"
        " C_L4)^(-4/3) and Lam_8c <= 10^(%s) C_L11^(-1/11.5)"
        % (mp.nstr(mp.mpf(lMm.b), 8), mp.nstr(mp.mpf(res['eq'][0].b), 6), res['eq'][1],
           mp.nstr(mp.mpf(res['ds'][0].b), 6), res['ds'][1],
           ", ".join(mp.nstr(mp.mpf((iv.log(CACHE['ds'][i])/iv.log(10)).b), 6) for i in (1, 2, 3, 4)),
           mp.nstr(bound, 5), mp.nstr(mp.mpf(lce.b), 7), mp.nstr(mp.mpf(l8b.b), 6), mp.nstr(mp.mpf(l8c.b), 6)))
    return bound <= LAM4_0


CACHE = {}


def main():
    ok = True
    for name, f in (("M1", m1), ("M2", m2), ("M3", m3), ("M4", m4)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("lamL5b: %s  [%.0f s]" % ("all checks pass, every control fails" if ok else "FAILURES", time.time() - T0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
