#!/usr/bin/env python3
"""e2bandtop5.py -- E2-PILOT section 3j (D567): the band bound of e2trapband5 on single intervals [sigma - 1/20, sigma].

The σ ≤ 384 run (`checks/e2trapband5.py 768 0.05 384`, saved as checks/e2trapband5_384.out) certifies the whole band.
It prints the interval bound at its sample points only up to σ = 192. This script recomputes the bound on the interval
ending at each requested σ the way e2trapband5's B2 does: take the eight largest l_1 ≤ LMAX1 with max V_(l_1 - 1) < σ_a²;
at each one pick e2trap5's best multiplier of the subfamily at σ_(l_1) and certify it (B1's certify); then take the
least of max(E2.7(l_1 - 1, σ_a), B_(l_1)(σ_b)) over them. It only certifies the l_1 it needs, so the admissible table
is built for those l alone. Its rows do not depend on which other l are in the table, so the multipliers chosen are
B1's.

  P0 (control) the interval ending at σ = 192 gives 0.66429 at l_1 = 378, as checks/e2trapband5_192.out and
     checks/e2trapband5_384.out print.
  P1 (certified, as B1 and B2) the intervals ending at σ = 256, 320 and 384, with their l_1.

Labels: certified, as e2trapband5's B1-B2 (interval arithmetic, e2trapcert5's functions).

  P2 (certified, the same) with the WIN largest admissible l_1 in place of B2's eight (WIN = 24): at σ = 320 and 384
     B2's least is at the lowest of its eight, so a wider window can only lower the bound;
     it lowers 384 to 0.43792 (l_1 = 759) and leaves 320 at 632 (D574). The saved checks/e2bandtop5.out predates the
     "candidates a to b" print; its values agree on a rerun (verifier 248).

    python3 checks/e2bandtop5.py [LMAX1 [SIGMAS [WIN]]]   (defaults 768, 192,256,320,384 and 8; seven minutes)
"""
import sys
import time
from fractions import Fraction

import numpy as np
from mpmath import iv

_argv, sys.argv = sys.argv, sys.argv[:1]
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import e2trapband5 as BD  # noqa: E402
import e2trapcert5 as C  # noqa: E402
import e2trap5 as T  # noqa: E402
sys.argv = _argv
E = C.E

LMAX1 = int(sys.argv[1]) if len(sys.argv) > 1 else 768
SIGMAS = [Fraction(x) for x in (sys.argv[2].split(",") if len(sys.argv) > 2 else ("192", "256", "320", "384"))]
H = Fraction(1, 20)
WIN = int(sys.argv[3]) if len(sys.argv) > 3 else 8                # B2 takes the eight largest


def main():
    t0 = time.time()
    fam = T.family()
    G = T.grid()
    vmax = {l: C.vmax(l) for l in range(0, LMAX1 + 1)}
    allowed = [j for j, (a_, b_, c_, d_, e_) in enumerate(fam)
               if abs(a_ - 0.98) < 1e-12 and abs(c_ - 0.5) < 1e-12 and abs(e_ - 1.0) < 1e-12
               and 1 / d_ - (1 / b_ + (1 / a_ - 1 / b_) / 2) > 1e-2]
    lam = C.xr(iv.log(iv.mpf(3))) - C.xr(iv.log(iv.mpf("0.2")))
    need = {}
    for sb in SIGMAS:
        sa = BD.q(sb - H)
        need[sb] = sorted(l1 for l1 in range(5, LMAX1 + 1) if (vmax[l1 - 1] - sa**2).b < 0)[-WIN:]
    ls = sorted({l for v in need.values() for l in v})
    adm, wI, m1, M1 = T.admissible_table(ls, fam, G)
    row = {l: i for i, l in enumerate(ls)}
    print("  admissible table for %d l_1 (%.0f s)" % (len(ls), time.time() - t0), flush=True)
    cert = {}
    for l1 in ls:
        sref = float(iv.sqrt(vmax[l1]).a)
        best = None
        for j in allowed:
            i = row[l1]
            if adm[i, j] and wI[i, j] > 0:
                b_ = np.sqrt((2 / m1[j] + (M1[j] + 2 * sref)**2 / wI[i, j]) / wI[i, j])
                if best is None or b_ < best[0]:
                    best = (b_, j)
        if best is None:
            print("    l_1 = %d: no admissible multiplier in the subfamily" % l1, flush=True)
            continue
        sL_, sR_, ks_, sc_, k_ = fam[best[1]]
        sc = Fraction(round(sc_ * 10000), 10000)
        sR = Fraction(sR_).limit_denominator(10)
        ok, m, M, w, n = BD.certify(l1, sR, sc)
        if ok:
            cert[l1] = (m, M, w)
        print("    l_1 = %d: s_R = %s, s_c = %s, %s, %d enclosures (%.0f s)"
              % (l1, sR, sc, "certified" if ok else "FAILED", n, time.time() - t0), flush=True)
    ok = {}
    res = {}
    for sb in SIGMAS:
        sa_f = sb - H
        sa, sbi = BD.q(sa_f), BD.q(sb)
        best, bl = None, None
        for l1 in need[sb]:
            if l1 not in cert:
                continue
            m, M, w = cert[l1]
            e27 = (lam * sa / (sa**2 - vmax[l1 - 1])).b
            val = max(e27, BD.bfun(m, M, w, sbi).b)
            if best is None or val < best:
                best, bl = val, l1
        res[sb] = (best, bl)
        print("    sigma = %s: on [%s, %s] <= %s (l_1 = %s; candidates %d to %d)"
              % (sb, float(sa_f), float(sb), "none" if best is None else E.up(best, 5), bl, need[sb][0], need[sb][-1]),
              flush=True)
    if Fraction(192) in res:
        b, l = res[Fraction(192)]
        ok['P0'] = b is not None and E.up(b, 5) == "0.66429" and l == 378
    ok['P1'] = all(res[s][0] is not None for s in SIGMAS) and len(cert) == len(ls)
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    print("  (%.0f s)" % (time.time() - t0))
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
