#!/usr/bin/env python3
"""e2trapband5.py -- E2-PILOT section 3j (D506, D528): section 3j's bound certified for every sigma in [3, SMAX] and
every l (SMAX = 96 by default, 192 in D528's run).

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
     (max V_(l_1))^(1/2), at which l_1's barrier top is sigma^2: beta > 0, w_(l_1) >= 0 on t in [-120, ln 119] by
     bisection, both tail ratios < 1, and m', M', w_I on I over 8000 pieces.
  B2 (certified) the band: [3, SMAX] cut at step H; on each interval [sigma_a, sigma_b] the least, over the eight largest
     certified l_1 with max V_(l_1 - 1) < sigma_a^2, of max(E2.7(l_1 - 1, sigma_a), B_(l_1)(sigma_b)) (E2.7 increases
     with l, max V_l doing so, so its max below l_1 is at l_1 - 1), in intervals, rounded up.
  B3 (computed) against e2trap5's float sup at every tenth point of its grid of step 0.01 (T3: at most 11.35 over [3,
     96], at sigma = 3.2): the band bound lies above it there, as expected (not a necessity: the float sup is not a
     bound; D511).

Measured (D506, corrected D511): B1 certifies every l_1 = 5 ... 190 (95 to 187 enclosures each, 187 at l_1 = 5); B2
over 1860 intervals of width 1/20: <= 11.477, the largest on [3.2, 3.25] (l_1 = 5); at sigma = 6, ..., 96 the values
of D503, at sigma = 3 the interval [3, 3.05] gives 11.086 (D497's point value is 10.989); B3 above e2trap5's float
sup at every 0.1 by 1.001 to 1.188 (on the full 0.01 grid 1.001 to 1.265, verifier 217); 47 minutes. (The run
predates tail_left_valid in B1, D505's guard, which holds for every multiplier here: only the flank's g enters,
between -60.86 and -60.81 at t = -120; verifier 217 re-ran B1 with it, all 186 certified.) Verifier 217 re-certified
the band independently in Arb: sup 11.4635.

Run to SMAX = 192 (D528; `python3 checks/e2trapband5.py 384 0.05 192`, saved as checks/e2trapband5_192.out): B1
certifies every l_1 = 5 ... 384 (93 to 145 enclosures at the printed l_1 = 20, 40, ..., 380); B2 over 3780 intervals of
width 1/20: <= 11.477, again on [3.2, 3.25] (l_1 = 5); on the intervals ending at sigma = 128, 160 and 192, 0.83951,
0.73083 and 0.66429 (l_1 = 251, 314, 378); B3 above e2trap5's float sup at every 0.1 of [3, 192] by 1.0010 to 1.1882; 98
minutes.

Run to SMAX = 384 (D567; `python3 checks/e2trapband5.py 768 0.05 384`, saved as checks/e2trapband5_384.out): B1
certifies every l_1 = 5 ... 768 (93 to 145 enclosures at the printed l_1 = 20, 40, ..., 760); B2 over 7620 intervals of
width 1/20: <= 11.477, again on [3.2, 3.25] (l_1 = 5), the printed points to 192 unchanged; B3 above e2trap5's float sup
at every 0.1 of [3, 384] by 1.0010 to 1.2294; 194 minutes. That run printed points only to 192 (256, 320 and 384 are printed from D567 on, so the saved output is
not byte-exact to this code); checks/e2bandtop5.py gives the intervals ending there: 0.56257, 0.49119 and 0.47635 (l_1 = 505,
632, 760), and 0.43792 at 384 (l_1 = 759) with a window of 24 l_1 in place of B2's eight.

Labels: B1, B2 certified (the lemmas as in e2trapcert5); B3 computed. Together with sections 3f-3g (0 < |sigma| <= 3)
this covers every real 0 < |sigma| <= SMAX, 96 by default, 192 in D528's run and 384 in D567's (the bounds are even in
sigma), with the
constant 275.2 on 0 < |sigma| < 3, set by l = 0 (section 3g).

    python3 checks/e2trapband5.py [LMAX1 [H [SMAX]]]       (defaults 190, 0.05 and 96: the band is [3, SMAX])
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
SMAX = Fraction(sys.argv[3]) if len(sys.argv) > 3 else Fraction(96)


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
    good = good and rl.b < 1 and el.a > 0 and rr.b < 1 and mr.a > 0 and C.BETA.a > 0 and C.tail_left_valid(tL)
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
        if best is None:                                   # no admissible multiplier of the subfamily at l_1
            bad.append(l1)
            print("    l_1 = %d: no admissible multiplier in the subfamily" % l1, flush=True)
            continue
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
    while sig_a < SMAX:
        sig_b = min(sig_a + H, SMAX)
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
    print("  B2 %s: [3, %s] in %d intervals of width %s: every one bounded; sup of the band bound %s on [%s, %s] "
          "(l_1 = %d)" % ("PASS" if okB2 else "FAIL", SMAX, len(rows), H, E.up(worst, 5), float(where[0]),
                          float(where[1]), where[2]), flush=True)
    for s_ in [x for x in (3, 6, 12, 24, 48, 96, 128, 160, 192, 256, 320, 384) if x <= SMAX]:
        r = next(x for x in rows if x[0] <= s_ <= x[1])
        if r[2] is None:
            continue
        print("    sigma = %s: on [%s, %s] <= %s (l_1 = %d)" % (s_, float(r[0]), float(r[1]), E.up(r[2], 5), r[3]))
    # B3: against e2trap5's float sup on its grid
    sigs = np.round(np.arange(3.0, float(SMAX) + 1e-9, 0.01), 2)
    Lall = list(range(0, LMAX1 + 1))
    okB3, fails, ratio = True, 0, []
    for s_ in sigs[::10]:
        B, _ = T.bstar(float(s_), adm, wI, m1, M1)
        fl = max(min(T.e27(l, float(s_)), B[l - 1] if l >= 1 else np.inf) for l in Lall)
        r = next(x for x in rows if float(x[0]) <= s_ <= float(x[1]))
        if r[2] is None or not float(r[2]) >= fl:
            okB3, fails = False, fails + 1
        ratio.append(float(r[2]) / fl)
    print("  B3 %s: the band bound lies above e2trap5's float sup at every 0.1 of [3, %s] (%d failures); ratio %.4f "
          "to %.4f" % ("PASS" if okB3 else "FAIL", SMAX, fails, min(ratio), max(ratio)), flush=True)
    ok = okB1 and okB2 and okB3
    print("  %s: for every sigma in [3, %s] and every l >= 0, ||chi_I R_l(sigma) chi_I|| <= %s (%.0f s)"
          % ("CERTIFIED" if ok else "NOT certified", SMAX, E.up(worst, 5), time.time() - t0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
