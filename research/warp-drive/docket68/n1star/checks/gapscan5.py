#!/usr/bin/env python3
"""gapscan5.py -- E1'a's first question (LOSS-D.md LD5): how large can the indicial gap of box^C near lam = 2 be over
the admissible constraint-damping parameters (v, e, h)?  Labels: computed (numerical; mpmath polyroots at 60 digits).

The scalar indicial polynomial is damping5.py's (polys(4, 2/3), the trace weight 2/3), in kappa = l(l+2).  The gap is
min over 1 <= l <= 12 of Re(lam) - 2 over its roots with Re > 3/2, the exceptional root lam = 2 at l = 1 (U3) set aside
(the root nearest 2 there).  The admissible region used: e <= e_0(v) (semiclass5.py's W4, the interior saddle, which
returns e_0/v^2) and h <= e (damping5.py U6: the roots stay above 2 only there).

  G1 (computed) The record's point (1/2, 1/102400, 10^-6): gap 2.93e-6 at l = 2 (PART-III-F2-INDICIAL.md:133-136).
  G2 (computed) For h << e the gap is linear in h, about c(v) h with c(0.5) ~ 3.06; it does not grow with e.
  G3 (computed) Over v in {0.3, ..., 0.55} and h/e_0 in {0.3, ..., 0.999} at e = e_0(v), the largest gap is about
     3.07e-5 (v ~ 0.45, h -> e_0).  Control: at v = 0.9 and h = 0.999 e_0 the gap is negative (a root below 2).
"""
import sys
import sympy as sp
import mpmath as mpm
sys.path.insert(0, __file__.rsplit('/checks/', 1)[0])
sys.setrecursionlimit(10000)
import damping5 as d5      # noqa: E402
import semiclass5 as s5    # noqa: E402

pk, p0, pv = d5.polys(4, sp.Rational(2, 3))
CO = [sp.lambdify((d5.e, d5.v, d5.h, d5.K), c, 'mpmath') for c in sp.Poly(pk, d5.lam).all_coeffs()]
mpm.mp.dps = 60


def gap(ev, vv, hv, lmax=12):
    best, arg = mpm.inf, None
    for lv in range(1, lmax + 1):
        rs = list(mpm.polyroots([c(ev, vv, hv, lv * (lv + 2)) for c in CO], maxsteps=800, extraprec=600))
        if lv == 1:
            rs.remove(min(rs, key=lambda z: abs(z - 2)))
        for z in rs:
            if mpm.re(z) > 1.5 and mpm.re(z) - 2 < best:
                best, arg = mpm.re(z) - 2, lv
    return best, arg


def main():
    g1, l1 = gap(mpm.mpf(1) / 102400, mpm.mpf(1) / 2, mpm.mpf(10)**-6)
    r1 = abs(g1 - mpm.mpf('2.93e-6')) < mpm.mpf('0.01e-6') and l1 == 2
    print('G1 record point: gap %s at l = %d ->' % (mpm.nstr(g1, 4), l1), 'PASS' if r1 else 'FAIL')
    ga, _ = gap(mpm.mpf('1e-5'), mpm.mpf(1) / 2, mpm.mpf('1e-7'))
    gb, _ = gap(mpm.mpf('1e-4'), mpm.mpf(1) / 2, mpm.mpf('1e-7'))
    gc, _ = gap(mpm.mpf('1e-4'), mpm.mpf(1) / 2, mpm.mpf('1e-6'))
    r2 = abs(gb / ga - 1) < 0.01 and abs(gc / gb - 10) < 0.2
    print('G2 linear in h, flat in e: gap(1e-5, 1e-7) = %s, gap(1e-4, 1e-7) = %s, gap(1e-4, 1e-6) = %s ->'
          % (mpm.nstr(ga, 4), mpm.nstr(gb, 4), mpm.nstr(gc, 4)), 'PASS' if r2 else 'FAIL')
    best = (mpm.mpf(0), None, None)
    for vv in (0.3, 0.4, 0.45, 0.5, 0.55):
        e0 = mpm.mpf(s5.e0_numeric(4, vv) * vv**2)
        for fr in ('0.5', '0.8', '0.95', '0.999'):
            g, _ = gap(e0, mpm.mpf(vv), e0 * mpm.mpf(fr))
            if g > best[0]:
                best = (g, vv, fr)
    r3 = mpm.mpf('2.9e-5') < best[0] < mpm.mpf('3.3e-5')
    e09 = mpm.mpf(s5.e0_numeric(4, 0.9) * 0.81)
    gneg, _ = gap(e09, mpm.mpf('0.9'), e09 * mpm.mpf('0.999'))
    print('G3 largest admissible gap %s at v = %s, h = %s e_0 (control v = 0.9: %s) ->'
          % (mpm.nstr(best[0], 4), best[1], best[2], mpm.nstr(gneg, 3)), 'PASS' if r3 and gneg < 0 else 'FAIL')
    ok = r1 and r2 and r3 and gneg < 0
    print('gapscan5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
