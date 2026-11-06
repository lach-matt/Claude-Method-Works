#!/usr/bin/env python3
"""intcert5: interval-arithmetic certificates for two sampled margins (FAMILIES5-R7.md section R7.3; the round-6
verifier's request "certify, do not sample").

Both margins live on the record's computed background (twobg5's double-null solution), so what is certified is a
statement about that computed background in a stated interpolant; its discretisation error is converged between n = 80
and 160 (qsign5 Q3, racslice5 S2), not certified.

  C1 (mpmath interval arithmetic) Gamma > 0 on the whole seed region, R in [0.70, 1.861] (region III on Sigma_tau0;
     qsign5 Q3 sampled it). Gamma = E^2 (Gamma/E^2) with E^2 > 0, and Gamma/E^2 is qsign5's closed form in (R, mu0,
     psi_P, psi_P', psi_P''), psi_P(R) = psi_III(tau0 + R) the spline of qsign5/racglobal5 R4 in its piecewise-polynomial
     form. [0.70, 1.861] is cut at the spline's knots and into cells; on each cell the polynomial piece and its first two
     derivatives are enclosed by interval evaluation, and Gamma/E^2 is enclosed by interval evaluation of the closed
     form, cells whose lower bound is not positive being bisected (to a depth limit). Certified: the lower bound is
     positive on every cell, at n = 80 and 160 (the least lower bound printed). Controls (must fail): Gamma with its sign flipped
     (the round-6 verifier's mutation), and Gamma without its 4 nu E^2 term, fail on some cell.
  C2 (mpmath interval arithmetic) Theorem L''s margin: kappa' K'^l_l < 0 on the whole of the bent slice Sigma'
     (racslice5, A = 0.01), not only at its grid crossings. Between consecutive crossings the background inputs (E, f,
     psi_R, psi_vhat, f_R, f_vhat) are taken as the linear interpolant of their crossing values (the stated interpolant),
     so on a sub-cell each lies in the hull of its interpolated end values; V'' = phi'' is enclosed from its closed form
     (C-infinity bumps evaluated in interval arithmetic) and V' = 1 + phi' by phi'(R_a) + [0, R - R_a] phi''(cell), with
     a margin 1e-6 for the quadrature of phi'; R is the cell. Each crossing interval is cut into sub-cells (bisected
     further if needed), and kappa' and K'^l_l are enclosed by interval evaluation of racslice5's closed forms.
     Certified: kappa' > 0 and K'^l_l < 0 on every sub-cell, so kappa' K'^l_l < 0 on all of Sigma' in Omega_2, at n =
     80 and 160 (the largest upper bound of kappa' K'^l_l printed). Controls (must fail): A = 0.001 (the round-6 verifier's
     mutation) and A = 0 (Sigma_tau0 itself) are not certified.

Labels: certified (interval arithmetic, for the computed background in the stated interpolant). Run:
python3 checks/intcert5.py   (several minutes under load)
"""
import importlib.util
import math
import os
import sys

import numpy as np
import sympy as sp
from mpmath import iv

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
iv.prec = 80
MODS = [{'exp': iv.exp, 'sqrt': iv.sqrt, 'log': iv.log, 'mpf': iv.mpf}, 'mpmath']


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def I(a, b=None):
    return iv.mpf([a, a if b is None else b])


# ---------------------------------------------------------------- C1
def ppoly_enclose(pp, xa, xb):
    """enclosures of the piecewise polynomial pp and its first two derivatives on [xa, xb] inside one piece"""
    i = int(np.searchsorted(pp.x, xa, side='right') - 1)
    i = min(max(i, 0), len(pp.x) - 2)
    assert pp.x[i] <= xa + 1e-15 and xb <= pp.x[i + 1] + 1e-15, (xa, xb, pp.x[i], pp.x[i + 1])
    c = pp.c[:, i]
    k = len(c) - 1
    X = I(xa, xb) - I(float(pp.x[i]))
    vals = []
    for d in range(3):
        acc = I(0.0)
        for j in range(k - d + 1):
            coef = float(c[j]) * math.factorial(k - j) / math.factorial(k - j - d)
            acc = acc + I(coef) * X**(k - j - d)
        vals.append(acc)
    return vals


def c1_run(bg, fGt, label, depth=14, ncell=600):
    from scipy.interpolate import PPoly
    tau0, mu0 = bg['tau0'], bg['mu0']
    pp = PPoly.from_spline(bg['sp_psi']._eval_args)
    lo, hi = 0.70, 1.861
    cuts = sorted({lo, hi} | {float(x) - tau0 for x in pp.x if lo < float(x) - tau0 < hi})
    cells = []
    for a, b in zip(cuts[:-1], cuts[1:]):
        n = max(1, int(math.ceil((b - a) / (hi - lo) * ncell)))
        e = np.linspace(a, b, n + 1)
        cells += list(zip(e[:-1], e[1:]))
    least, worst_cell, failed, nev = None, None, 0, 0
    stack = [(a, b, 0) for a, b in cells]
    while stack:
        a, b, d = stack.pop()
        p0, p1, p2 = ppoly_enclose(pp, tau0 + a, tau0 + b)
        val = fGt(I(a, b), I(mu0), p0, p1, p2)
        nev += 1
        lb = float(val.a)
        if lb > 0:
            if least is None or lb < least:
                least, worst_cell = lb, (a, b)
            continue
        if d >= depth:
            failed += 1
            continue
        m = 0.5 * (a + b)
        stack += [(a, m, d + 1), (m, b, d + 1)]
    return failed == 0, least, worst_cell, failed, nev


def c1(bgs):
    print("C1 (interval arithmetic) Gamma > 0 on the whole seed region R in [0.70, 1.861]")
    q = load('qsign5')
    _, Gt, _ = q.gamma_formula()
    f = sp.lambdify([q.R, q.MU] + list(q.PP), Gt, modules=MODS)
    # the mutants: sign flipped; the 4 nu E^2 term dropped (Gamma/E^2 - 4 R^3)
    fneg = sp.lambdify([q.R, q.MU] + list(q.PP), -Gt, modules=MODS)
    fdrop = sp.lambdify([q.R, q.MU] + list(q.PP), Gt - 4 * q.R**3, modules=MODS)
    ok = True
    for n, bg in bgs.items():
        good, least, cell, failed, nev = c1_run(bg, f, 'Gamma')
        print("   n = %d: certified on every cell: %s (%d interval evaluations; least lower bound of Gamma/E^2 = %.4f "
              "on R in [%.5f, %.5f])" % (n, good, nev, least if least is not None else float('nan'), cell[0], cell[1]))
        ok &= good
    bg = bgs[160]
    g1, _, _, f1, _ = c1_run(bg, fneg, 'neg', depth=0)
    g2, _, _, f2, _ = c1_run(bg, fdrop, 'drop', depth=0)
    print("   controls: Gamma with its sign flipped is not certified (%d cells fail; rejected): %s; Gamma without its "
          "4 nu E^2 term is not certified (%d cells fail; rejected): %s" % (f1, not g1, f2, not g2))
    return ok and not g1 and not g2


# ---------------------------------------------------------------- C2
def bump_iv(X, a, b):
    """the C-infinity bump exp(1 - 1/(1 - y^2)) on (a, b), enclosed on the interval X"""
    c, h = 0.5 * (a + b), 0.5 * (b - a)
    Y = (X - I(c)) / I(h)
    lo, hi = float(Y.a), float(Y.b)
    if hi <= -1 or lo >= 1:
        return I(0.0)
    if lo <= -1 or hi >= 1:                         # the cell meets the bump's edge: enclose by [0, sup on the part]
        ylo, yhi = max(lo, -1.0), min(hi, 1.0)
        ym = 0.0 if ylo <= 0 <= yhi else min(abs(ylo), abs(yhi))
        return I(0.0, math.exp(1 - 1 / (1 - ym**2)) * (1 + 1e-15)) if abs(ym) < 1 else I(0.0)
    return iv.exp(I(1.0) - I(1.0) / (I(1.0) - Y * Y))


def phi2_iv(X, rs, A, lam):
    return I(A) * (bump_iv(X, *rs.P_IV) - I(float(lam[0])) * bump_iv(X, *rs.L_IV)
                   - I(float(lam[1])) * bump_iv(X, *rs.R_IV))


def c2_run(rs, tb, bgd, A, fk, fK, nsub=4, depth=8):
    o = rs.crossing(tb, bgd, A)
    o = o[np.argsort(o[:, 0])]
    x, p0, p1, pp, lam = rs.make_phi(A)
    worst, failed, nev = None, 0, 0
    for i in range(len(o) - 1):
        ra, rb = o[i, 0], o[i + 1, 0]
        if rb <= ra:
            continue
        stack = []
        for k in range(nsub):
            s0, s1 = k / nsub, (k + 1) / nsub
            stack.append((s0, s1, 0))
        while stack:
            s0, s1, d = stack.pop()
            a = ra + s0 * (rb - ra)
            b = ra + s1 * (rb - ra)
            ins = []
            for j in range(1, 7):                                       # E, f, psi_R, psi_v, f_R, f_v
                va = o[i, j] + s0 * (o[i + 1, j] - o[i, j])
                vb = o[i, j] + s1 * (o[i + 1, j] - o[i, j])
                ins.append(I(min(va, vb), max(va, vb)))
            Xr = I(a, b)
            V2 = phi2_iv(Xr, rs, A, lam)
            ph1a = float(np.interp(a, x, p1))
            V1 = I(1.0) + I(ph1a - 1e-6, ph1a + 1e-6) + I(0.0, b - a) * V2
            kap = fk(*ins, V1, V2, Xr)
            Kl = fK(*ins, V1, V2, Xr)
            prod = kap * Kl
            nev += 1
            ub = float(prod.b)
            if float(kap.a) > 0 and float(Kl.b) < 0:
                worst = ub if worst is None or ub > worst else worst
                continue
            if d >= depth:
                failed += 1
                worst = ub if worst is None or ub > worst else worst
                continue
            m = 0.5 * (s0 + s1)
            stack += [(s0, m, d + 1), (m, s1, d + 1)]
    return failed == 0, worst, failed, nev, len(o)


def c2():
    print("C2 (interval arithmetic) kappa' K'^l_l < 0 on the whole of the bent slice, between its samples")
    rs = load('racslice5')
    tb = load('twobg5')
    kap, Kll = rs.slice_formulas()
    fk = sp.lambdify(rs.SYMS, kap, modules=MODS)
    fK = sp.lambdify(rs.SYMS, Kll, modules=MODS)
    ok = True
    bgds = {}
    for n in (80, 160):
        bgds[n] = tb.run(n)
        good, worst, failed, nev, npts = c2_run(rs, tb, bgds[n], rs.A_DEF, fk, fK)
        print("   n = %d, A = %.3f: %d crossings; kappa' > 0 and K'^l_l < 0 certified on every sub-cell: %s (%d "
              "interval evaluations; largest upper bound of kappa' K'^l_l = %.4e)" %
              (n, rs.A_DEF, npts, good, nev, worst))
        ok &= good
    g1, w1, f1, _, _ = c2_run(rs, tb, bgds[160], 0.001, fk, fK, depth=1)
    g0, w0, f0, _, _ = c2_run(rs, tb, bgds[160], 0.0, fk, fK, depth=1)
    print("   controls: A = 0.001 not certified (%d sub-cells fail, largest upper bound %.3e; rejected): %s; A = 0 "
          "(Sigma_tau0) not certified (%d fail; rejected): %s" % (f1, w1, not g1, f0, not g0))
    return ok and not g1 and not g0


def main():
    q = load('qsign5')
    bgs = {80: q.background(80), 160: q.background(160)}
    res = {}
    res['C1'] = c1(bgs)
    print('C1', 'PASS' if res['C1'] else 'FAIL', flush=True)
    res['C2'] = c2()
    print('C2', 'PASS' if res['C2'] else 'FAIL', flush=True)
    return 0 if all(res.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
