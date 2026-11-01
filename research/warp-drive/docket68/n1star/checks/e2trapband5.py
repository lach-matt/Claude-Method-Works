#!/usr/bin/env python3
"""e2trapband5.py -- E2-PILOT section 3j (D506): section 3j's bound certified for every sigma in [3, 96] and every l.

D497 and D503 certify the bound at six frequencies. The pieces of e2trapcert5's certificate are of two kinds: those that
do not involve sigma (the multiplier's admissibility at l_1, C1-C3, and the constants m' = min_I phi', M' = max_I phi',
w_I = min_I w_(l_1) of C4) and two explicit functions of sigma,

    B_(l_1)(sigma) = ((2/m' + (M' + 2 sigma)^2/w_I)/w_I)^(1/2),   increasing in sigma > 0,
    E2.7(l, sigma) = Lambda sigma/(sigma^2 - max V_l),           decreasing in sigma where sigma^2 > max V_l.

So once a multiplier is certified at l_1, every sigma in an interval [sigma_a, sigma_b] with max V_l < sigma_a^2 for
every l < l_1 has, for every l >= 0,

    ||chi_I R_l(sigma) chi_I|| <= max(max_(l < l_1) E2.7(l, sigma_a), B_(l_1)(sigma_b)).

  B1 (certified, interval arithmetic, e2trapcert5's functions) for every l_1 = 5, ..., LMAX1: the multiplier e2trap5
     finds best at l_1, within the core-and-flank subfamily the certificate handles (s_L = 49/50, kappa_s = 1/2, kappa
     = s_c, beta > 0; s_R and s_c from e2trap5's family, s_c rational to four digits), at the frequency sigma_(l_1) =
     (max V_(l_1))^(1/2) where l_1 is the trapped harmonic: beta > 0, w_(l_1) >= 0 on t in [-120, ln 119] by
     bisection, both tail ratios < 1, and m', M', w_I on I over 8000 pieces.
  B2 (certified) the band: [3, 96] cut at step H; on each interval [sigma_a, sigma_b] the least, over the eight largest
     certified l_1 with max V_(l_1 - 1) < sigma_a^2, of max(E2.7(l_1 - 1, sigma_a), B_(l_1)(sigma_b)) (E2.7 increases
     with l, max V_l doing so, so its max below l_1 is at l_1 - 1), in intervals, rounded up.
  B3 (computed) against e2trap5's float sup on its grid of step 0.01 (T3: at most 11.35 over [3, 96], at sigma = 3.2):
     the band bound lies above it at every grid point, as it must.

Labels: B1, B2 certified (the lemmas as in e2trapcert5); B3 computed. Together with sections 3f-3g (0 < |sigma| <= 3)
this covers every real 0 < |sigma| <= 96 (the bounds are even in sigma).

    python3 checks/e2trapband5.py [LMAX1 [H]]       (defaults 190 and 0.05)
"""
import sys
import time
from fractions import Fraction

import numpy as np
from mpmath import iv, mpf

_argv, sys.argv = sys.argv, sys.argv[:1]
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import e2trapcert5 as C  # noqa: E402
import e2trap5 as T  # noqa: E402
sys.argv = _argv
E = C.E

LMAX1 = int(sys.argv[1]) if len(sys.argv) > 1 else 190
H = Fraction(sys.argv[2]) if len(sys.argv) > 2 else Fraction(1, 20)


def q(x):
    f = Fraction(x)
    return iv.mpf(f.numerator) / f.denominator


def set_mult(sR, sc):
    """e2trapcert5's module constants for the multiplier (s_L = 49/50, kappa_s = 1/2, kappa = s_c)"""
    C.SL, C.SR, C.KS, C.SC = q("49/50"), q(sR), q("1/2"), q(sc)
    C.DD = 1 / C.SL - 1 / C.SR
    C.BETA = 1 / C.SC - (1 / C.SR + C.DD / 2)
    C.KC = C.SC


def certify(l1, sR, sc):
    """B1 at l_1: (ok, m', M', w_I, enclosures)"""
    set_mult(sR, sc)
    a = C.A_(l1)
    tL, rR = -120, 120
    tR = iv.log(iv.mpf(rR) - 1).b
    good, n, _ = C.certify_positive(a, tL, tR)
    rl, el = C.tail_left(a, tL)
    rr, mr = C.tail_right(a, rR)
    good = good and rl.b < 1 and el.a > 0 and rr.b < 1 and mr.a > 0 and C.BETA.a > 0
    m1lo, M1hi = E.enclose_I(lambda tt: C.mult(C.xr(tt))[1], pieces=8000)
    wlo, _ = E.enclose_I(lambda tt: C.w_of(tt, a), pieces=8000)
    good = good and m1lo > 0 and wlo > 0
    return good, iv.mpf(m1lo), iv.mpf(M1hi), iv.mpf(wlo), n


def bfun(m, M, w, sig):
    return iv.sqrt((2 / m + (M + 2 * sig)**2 / w) / w)


def main():
    t0 = time.time()
    fam = T.family()
    G = T.grid()
    ls = list(range(1, LMAX1 + 1))
    adm, wI, m1, M1 = T.admissible_table(ls, fam, G)
    print("  e2trap5's admissible table, l = 1 ... %d (%.0f s)" % (LMAX1, time.time() - t0), flush=True)
    vmax = {l: C.vmax(l) for l in range(0, LMAX1 + 1)}
    # the subfamily the certificate handles: s_L = 0.98, kappa_s = 1/2, kappa = s_c (k = 1), beta clearly positive
    allowed = [j for j, (a_, b_, c_, d_, e_) in enumerate(fam)
               if abs(a_ - 0.98) < 1e-12 and abs(c_ - 0.5) < 1e-12 and abs(e_ - 1.0) < 1e-12
               and 1 / d_ - (1 / b_ + (1 / a_ - 1 / b_) / 2) > 1e-2]
    lam = C.xr(iv.log(iv.mpf(3))) - C.xr(iv.log(iv.mpf("0.2")))
    # B1
    cert, bad = {}, []
    for l1 in range(5, LMAX1 + 1):
        sref = float(iv.sqrt(vmax[l1]).a)
        best = None
        for j in allowed:
            if adm[l1 - 1, j] and wI[l1 - 1, j] > 0:
                b_ = np.sqrt((2 / m1[j] + (M1[j] + 2 * sref)**2 / wI[l1 - 1, j]) / wI[l1 - 1, j])
                if best is None or b_ < best[0]:
                    best = (b_, j)
        sL_, sR_, ks_, sc_, k_ = fam[best[1]]
        sc = Fraction(round(sc_ * 10000), 10000)
        sR = Fraction(sR_).limit_denominator(10)
        ok, m, M, w, n = certify(l1, sR, sc)
        if ok:
            cert[l1] = (m, M, w, sR, sc)
        else:
            bad.append(l1)
        if l1 % 20 == 0 or not ok:
            print("    l_1 = %d: s_R = %s, s_c = %s, %s, %d enclosures, m' >= %s, w_I >= %s (%.0f s)"
                  % (l1, sR, sc, "certified" if ok else "FAILED", n, E.dn(m.a, 5), E.dn(w.a, 5), time.time() - t0),
                  flush=True)
    okB1 = not bad
    print("  B1 %s: multipliers certified at every l_1 = 5 ... %d%s" % ("PASS" if okB1 else "FAIL", LMAX1,
                                                                      "" if okB1 else " except %s" % bad), flush=True)
    # B2
    sig_a = Fraction(3)
    worst, where, rows, okB2 = mpf(0), None, [], True
    while sig_a < 96:
        sig_b = min(sig_a + H, Fraction(96))
        sa, sb = q(sig_a), q(sig_b)
        best, bl = None, None
        cands = sorted(l1 for l1 in cert if (vmax[l1 - 1] - sa**2).b < 0)[-8:]
        for l1 in cands:
            m, M, w, sR, sc = cert[l1]
            e27 = (lam * sa / (sa**2 - vmax[l1 - 1])).b          # E2.7 increases in l: its max below l_1 is at l_1 - 1
            val = max(e27, bfun(m, M, w, sb).b)
            if best is None or val < best:
                best, bl = val, l1
        if best is None:
            okB2 = False
            rows.append((sig_a, sig_b, None, None))
        else:
            rows.append((sig_a, sig_b, best, bl))
            if best > worst:
                worst, where = best, (sig_a, sig_b, bl)
        sig_a = sig_b
    print("  B2 %s: [3, 96] in %d intervals of width %s: every one bounded; sup of the band bound %s on [%s, %s] "
          "(l_1 = %d)" % ("PASS" if okB2 else "FAIL", len(rows), H, E.up(worst, 5), float(where[0]), float(where[1]),
                          where[2]), flush=True)
    for s_ in (3, 6, 12, 24, 48, 96):
        r = next(x for x in rows if x[0] <= s_ <= x[1])
        print("    sigma = %s: on [%s, %s] <= %s (l_1 = %d)" % (s_, float(r[0]), float(r[1]), E.up(r[2], 5), r[3]))
    # B3: against e2trap5's float sup on its grid
    sigs = np.round(np.arange(3.0, 96.0 + 1e-9, 0.01), 2)
    Lall = list(range(0, LMAX1 + 1))
    okB3, fails, ratio = True, 0, []
    for s_ in sigs[::10]:
        B, _ = T.bstar(float(s_), adm, wI, m1, M1)
        fl = max(min(T.e27(l, float(s_)), B[l - 1] if l >= 1 else np.inf) for l in Lall)
        r = next(x for x in rows if float(x[0]) <= s_ <= float(x[1]))
        if not float(r[2]) >= fl:
            okB3, fails = False, fails + 1
        ratio.append(float(r[2]) / fl)
    print("  B3 %s: the band bound lies above e2trap5's float sup at every 0.1 of [3, 96] (%d failures); ratio %.4f to "
          "%.4f" % ("PASS" if okB3 else "FAIL", fails, min(ratio), max(ratio)), flush=True)
    ok = okB1 and okB2 and okB3
    print("  %s: for every sigma in [3, 96] and every l >= 0, ||chi_I R_l(sigma) chi_I|| <= %s (%.0f s)"
          % ("CERTIFIED" if ok else "NOT certified", E.up(worst, 5), time.time() - t0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
