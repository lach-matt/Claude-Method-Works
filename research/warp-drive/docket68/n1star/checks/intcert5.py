#!/usr/bin/env python3
"""intcert5: interval-arithmetic certificates for the margins of Theorem Q and Theorem L'' (FAMILIES5-R7.md section
R7.3; FAMILIES5-R8.md section R8.2).

Round 8 (the round-7 reader's r7-m1): every step is in interval arithmetic (mpmath iv, 80 bits). The spline's piece
coefficients enter as the floats that define the stated interpolant, and its derivative coefficients are formed in
iv; the cell ends are floats whose differences are taken in iv; the bump's edge branch is a bound; phi' and phi are
enclosed by interval Taylor sums of the closed-form phi'' (no pad). The bend's moment constants l1, l2 are exact up to
outward rounding (the lobes are dilates of one even bump, class Bend). Three kinds of statement are certified:

  C1 (the computed background) Gamma > 0 on the whole seed region, R in [0.70, 1.861] (region III on Sigma_tau0):
     Gamma = E^2 (Gamma/E^2), E^2 > 0, Gamma/E^2 qsign5's closed form in (R, mu0, psi_P, psi_P', psi_P''), psi_P the
     spline psi_III(tau0 + R) in its piecewise-polynomial form; cells cut at the knots in vhat; the polynomial and two
     derivatives enclosed with interval coefficients. Certified at n = 80 and 160. Controls (must fail): Gamma's sign
     flipped; Gamma without its 4 nu E^2 term.
  C1d (robustness) the same with psi_P, psi_P', psi_P'' each widened by d = (1e-3, 1e-3, 1e-2): Gamma > 0 for every
     background whose psi_III is within d of the computed spline in C^2 (the n = 80 and n = 160 splines differ by far
     less, printed). Control: d = (0.5, 0.5, 5) is not certified.
  C2 (the computed background) kappa' K'^l_l < 0 on the whole bent slice Sigma' (racslice5, A = 0.01), between its
     grid crossings, the inputs (E, f, psi_R, psi_vhat, f_R, f_vhat) linear between crossings (the stated
     interpolant), V'' and V' = 1 + phi' enclosed from phi''. Certified at n = 80 and 160. Controls (must fail):
     A = 0.001 (the round-6 verifier's mutation) and A = 0.
  C2d (robustness) on R < R_* (the seed and packet regions, where Sigma' = Sigma_tau0) the same with every input
     widened by 1e-3 of its size plus 1e-6. Control: a widening of 0.5 is not certified.
  C3 (the background itself) on R >= R_*, where the background is ingoing Vaidya. On {u <= u1} (B = 0) the mass
     depends on v alone and psi = 0 (twobg5 G1 (a)-(b)), so the background is g0 = -f dvhat^2 + 2 dvhat dR +
     R^2 dOmega_3^2 with f = 1 - mu(vhat)/R^2, mu(vhat) fixed by the data on N = {u = 0}: R'' = -A/(3 R^2), R(0) = 5,
     R'(0) = 1/2, and Q = R_u with Q' = -(1/2 + 2 Q R')/R, Q(0) = (1.5/25 - 1)/2 (e^(2s) = 1/2 on N; twodomain5),
     mu = R^2 (1 + 4 Q R'), vhat' = -1/(2 Q), mu'(vhat) = (8/3) A Q^2. Before the shell (v <= 3) this is exact:
     R = 5 + v/2, Q = 0.75/R^2 - 1/2, mu = 1.5, vhat in closed form; on the shell, v in [3, 4.5], it is enclosed by a
     validated integrator (Taylor order one with an a priori enclosure and a second-order remainder over the step
     box); after it mu is constant. The outgoing ray u = u1 starts on N' = {v = 0} at R = 5 + 5.7 R_u(0) = 2.321 (B = 0
     for u < 5.7: R linear on N') and before the shell is a null ray of Tangherlini (mu = 1.5), vhat = 2 R +
     sqrt(mu) ln((R - sqrt mu)/(R + sqrt mu)) + const: its crossing R_* with Sigma_tau0 is enclosed, and every point
     of Sigma' with R >= R_* is in {u <= u1} (checked: printed). Certified, for the background defined by the stated
     characteristic data: kappa' > 0 and K'^l_l < 0 on Sigma' from R_* to 5.75 (beyond, Sigma' = Sigma_tau0 in
     Tangherlini of mass mu_end, where Nk = (mu/R^3)(f - 3) < 0 exactly); and on Sigma_tau0 the band: Nk = (mu/R^3)
     (f - 3) + mu'/(2 R^2) is certified negative outside two enclosures of its edges and positive between them.
     Controls (must fail): a float integration (scipy DOP853) of the same ODE lies inside the enclosures, and does
     not when its initial Q is shifted by 1e-6; A = 0 (Sigma_tau0) is not certified hyperbolic.

Labels: certified (interval arithmetic). C1, C1d, C2, C2d concern the computed background; C3 concerns the background
itself on R >= R_*. The background itself on R < R_* is certified by truebg5.py. Run: python3 checks/intcert5.py
(about half an hour under load).
"""
import bisect
import importlib.util
import math
import os
import sys

import mpmath
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


def hull(*xs):
    return iv.mpf([min(x.a for x in xs), max(x.b for x in xs)])


def widen(x, d):
    return iv.mpf([x.a - d, x.b + d])


# ---------------------------------------------------------------- the C-infinity bump in interval arithmetic
def bump_parts(X, a, b):
    """(b, b') of the bump exp(1 - 1/(1 - y^2)), y = (2 X - a - b)/(b - a), enclosed on the interval X"""
    c, h = (I(a) + I(b)) / 2, (I(b) - I(a)) / 2
    Y = (X - c) / h
    lo, hi = Y.a, Y.b
    if hi <= -1 or lo >= 1:
        return I(0.0), I(0.0)
    if lo > -1 and hi < 1:
        Y2 = Y * Y
        G = I(1.0) / (I(1.0) - Y2)
        B = iv.exp(I(1.0) - G)
        return B, B * (I(-2.0) * Y * G * G) / h
    # the cell meets an edge: on the part inside, x = 1/(1 - y^2) >= X0, with b = e^(1 - x) <= e^(1 - X0) and
    # b x^2 <= e^(1 - X0) X0^2 when X0 >= 2 (decreasing there), <= 4/e otherwise
    ylo, yhi = max(lo, I(-1.0).a), min(hi, I(1.0).b)
    ym = I(0.0) if (ylo <= 0 <= yhi) else iv.mpf([min(abs(ylo), abs(yhi)), min(abs(ylo), abs(yhi))])
    if ym.a >= 1:
        return I(0.0), I(0.0)
    X0 = I(1.0) / (I(1.0) - ym * ym)
    bmax = iv.exp(I(1.0) - X0).b
    bx2 = (iv.exp(I(1.0) - X0) * X0 * X0).b if X0.a >= 2 else (I(4.0) / iv.exp(I(1.0))).b
    ymax = max(abs(ylo), abs(yhi))
    dmax = (I(2.0) * I(ymax) * I(bx2) / h).b
    return iv.mpf([0, bmax]), iv.mpf([-dmax, dmax])


# ---------------------------------------------------------------- the bend phi, enclosed
class Bend:
    """phi'' = A (b_P - l1 b_L - l2 b_R) and its two integrals phi', phi from the left end of the support.

    The three lobes are translates and dilates of one even bump, so int b_X = h_X K and int x b_X = c_X h_X K (h_X the
    half-width, c_X the centre, K the bump's integral over (-1, 1)); the two moment conditions int phi'' = int x phi''
    = 0 are l1 h_L + l2 h_R = h_P and l1 c_L h_L + l2 c_R h_R = c_P h_P, with K cancelled. l1, l2 are their solution
    in interval arithmetic, exact up to outward rounding (racslice5 solves the same system by trapezoid quadrature)."""

    def __init__(self, rs, A, ncell=22500):
        self.A = A
        self.P, self.L, self.Rv = rs.P_IV, rs.L_IV, rs.R_IV
        hc = {}
        for nm, (a, b) in (('P', self.P), ('L', self.L), ('R', self.Rv)):
            hc[nm] = ((I(b) - I(a)) / 2, (I(a) + I(b)) / 2)
        (hP, cP), (hL, cL), (hR, cR) = hc['P'], hc['L'], hc['R']
        self.l1 = hP / hL * (cR - cP) / (cR - cL)
        self.l2 = hP / hR * (cP - cL) / (cR - cL)
        # interval Taylor sums for phi' and phi over float cell edges r_k, widths w_k = r_(k+1) - r_k in iv
        self.x0, self.x1 = self.L[0], self.Rv[1]
        self.n = ncell
        self.r = [self.x0 + k * (self.x1 - self.x0) / ncell for k in range(ncell)] + [self.x1]
        p1 = [I(0.0)]
        p0 = [I(0.0)]
        for k in range(ncell):
            X = I(self.r[k], self.r[k + 1])
            w = I(self.r[k + 1]) - I(self.r[k])
            pp = self.phi2(X)
            p1.append(p1[-1] + w * pp)                    # phi'(r_(k+1)) = phi'(r_k) + w phi''(xi)
            p0.append(p0[-1] + w * p1[-2] + w * w / 2 * pp)  # phi(r_(k+1)) = phi(r_k) + w phi'(r_k) + w^2/2 phi''(xi)
        self.p1, self.p0 = p1, p0
        self.end1, self.end0 = p1[-1], p0[-1]

    def phi2(self, X):
        bP, _ = bump_parts(X, *self.P)
        bL, _ = bump_parts(X, *self.L)
        bR, _ = bump_parts(X, *self.Rv)
        return I(self.A) * (bP - self.l1 * bL - self.l2 * bR)

    def at(self, X):
        """enclosures of (phi, phi', phi'') on the interval X"""
        if X.b <= self.x0 or X.a >= self.x1:
            return I(0.0), I(0.0), I(0.0)
        k = max(0, min(bisect.bisect_right(self.r, max(float(X.a), self.x0)) - 1, self.n - 1))
        while self.r[k] > X.a and k > 0:                       # r_k <= X.a (or r_0 = x0), exactly
            k -= 1
        rk = self.r[k]
        Xc = iv.mpf([min(X.a, rk), X.b])
        pp = self.phi2(Xc)
        d = iv.mpf([0, (iv.mpf(X.b) - I(rk)).b])
        p1 = self.p1[k] + d * pp
        p0 = self.p0[k] + d * self.p1[k] + d * d / 2 * pp
        if X.a < self.x0:                                       # phi = phi' = 0 left of the support
            p1, p0 = hull(p1, I(0.0)), hull(p0, I(0.0))
        return p0, p1, pp


# ---------------------------------------------------------------- C1, C1d
def ppoly_enclose(pp, i, VH):
    """the piece i of the piecewise polynomial pp and its first two derivatives, enclosed on the interval VH"""
    c = pp.c[:, i]
    k = len(c) - 1
    X = VH - I(float(pp.x[i]))
    vals = []
    for d in range(3):
        acc = I(0.0)
        for j in range(k - d + 1):
            coef = I(float(c[j])) * I(math.factorial(k - j)) / I(math.factorial(k - j - d))
            acc = acc + coef * X**(k - j - d)
        vals.append(acc)
    return vals


def c1_run(bg, fGt, dlt=(0.0, 0.0, 0.0), depth=14, ncell=600, lo=0.70, hi=1.861):
    from scipy.interpolate import PPoly
    tau0, mu0 = bg['tau0'], bg['mu0']
    pp = PPoly.from_spline(bg['sp_psi']._eval_args)
    T0 = I(tau0)
    va, vb = float((I(lo) + T0).a), float((I(hi) + T0).b)      # the vhat range, outward-rounded
    knots = [float(x) for x in pp.x if va < float(x) < vb]
    cuts = sorted({va, vb} | set(knots))
    cells = []
    for a, b in zip(cuts[:-1], cuts[1:]):
        n = max(1, int(math.ceil((b - a) / (vb - va) * ncell)))
        e = np.linspace(a, b, n + 1)
        e[0], e[-1] = a, b
        cells += list(zip(e[:-1], e[1:]))
    least, worst_cell, failed, nev = None, None, 0, 0
    stack = [(a, b, 0) for a, b in cells]
    while stack:
        a, b, d = stack.pop()
        i = int(np.searchsorted(pp.x, 0.5 * (a + b), side='right') - 1)
        assert pp.x[i] <= a and b <= pp.x[i + 1]
        VH = I(a, b)
        p0, p1, p2 = ppoly_enclose(pp, i, VH)
        p0, p1, p2 = widen(p0, dlt[0]), widen(p1, dlt[1]), widen(p2, dlt[2])
        Rr = VH - T0
        val = fGt(Rr, I(mu0), p0, p1, p2)
        nev += 1
        lb = float(val.a)
        if lb > 0:
            if least is None or lb < least:
                least, worst_cell = lb, (float(Rr.a), float(Rr.b))
            continue
        if d >= depth:
            failed += 1
            continue
        m = 0.5 * (a + b)
        stack += [(a, m, d + 1), (m, b, d + 1)]
    return failed == 0, least, worst_cell, failed, nev


def c1(bgs):
    print("C1, C1d (interval arithmetic) Gamma > 0 on the whole seed region R in [0.70, 1.861]: the computed background,"
          " and every background within d of it")
    q = load('qsign5')
    _, Gt, _ = q.gamma_formula()
    args = [q.R, q.MU] + list(q.PP)
    f = sp.lambdify(args, Gt, modules=MODS)
    fneg = sp.lambdify(args, -Gt, modules=MODS)
    fdrop = sp.lambdify(args, Gt - 4 * q.R**3, modules=MODS)
    ok = True
    for n, bg in bgs.items():
        good, least, cell, failed, nev = c1_run(bg, f)
        print("   C1, n = %d: certified on every cell: %s (%d interval evaluations; least lower bound of Gamma/E^2 = "
              "%.4f on R in [%.5f, %.5f])" % (n, good, nev, least or float('nan'), *(cell or (0, 0))))
        ok &= good
    dl = (1e-3, 1e-3, 1e-2)
    for n, bg in bgs.items():
        good, least, cell, failed, nev = c1_run(bg, f, dlt=dl)
        print("   C1d, n = %d, d = %s: certified on every cell: %s (least lower bound %.4f)" % (n, dl, good,
                                                                                               least or float('nan')))
        ok &= good
    # the scale of the computed background's error: the n = 80 and n = 160 splines and derivatives, sampled
    Rs = np.linspace(0.70, 1.861, 2001)
    s80, s160 = bgs[80]['sp_psi'], bgs[160]['sp_psi']
    t0 = bgs[160]['tau0']
    diffs = [float(np.max(np.abs(s80.derivative(k)(t0 + Rs) - s160.derivative(k)(t0 + Rs)) if k else
                         np.abs(s80(t0 + Rs) - s160(t0 + Rs)))) for k in range(3)]
    print("   the n = 80 and n = 160 splines differ by at most %.1e, %.1e, %.1e (psi_P, psi_P', psi_P'', sampled): far "
          "inside d" % tuple(diffs))
    bg = bgs[160]
    g1, _, _, f1, _ = c1_run(bg, fneg, depth=0)
    g2, _, _, f2, _ = c1_run(bg, fdrop, depth=0)
    g3, _, _, f3, _ = c1_run(bg, f, dlt=(0.5, 0.5, 5.0), depth=0)
    print("   controls: Gamma with its sign flipped not certified (%d cells fail; rejected): %s; without its 4 nu E^2 "
          "term not certified (%d fail; rejected): %s; d = (0.5, 0.5, 5) not certified (%d fail; rejected): %s" %
          (f1, not g1, f2, not g2, f3, not g3))
    return ok and not g1 and not g2 and not g3 and max(diffs) < 1e-3


# ---------------------------------------------------------------- C2, C2d
def c2_run(rs, tb, bgd, A, fk, fK, nsub=4, depth=8, rel=0.0, absd=0.0, rmax=None):
    o = rs.crossing(tb, bgd, A)
    o = o[np.argsort(o[:, 0])]
    bend = Bend(rs, A, ncell=2250) if A != 0 else None
    worst, failed, nev = None, 0, 0
    for i in range(len(o) - 1):
        ra, rb = o[i, 0], o[i + 1, 0]
        if rb <= ra or (rmax is not None and ra >= rmax):
            continue
        stack = [(k / nsub, (k + 1) / nsub, 0) for k in range(nsub)]
        while stack:
            s0, s1, d = stack.pop()
            Xr = I(ra) + I(s0, s1) * (I(rb) - I(ra))
            ins = []
            for j in range(1, 7):                                       # E, f, psi_R, psi_v, f_R, f_v
                va = I(o[i, j]) + I(s0) * (I(o[i + 1, j]) - I(o[i, j]))
                vb = I(o[i, j]) + I(s1) * (I(o[i + 1, j]) - I(o[i, j]))
                x = hull(va, vb)
                if rel or absd:
                    x = widen(x, rel * max(abs(float(x.a)), abs(float(x.b))) + absd)
                ins.append(x)
            if bend is None:
                V1, V2 = I(1.0), I(0.0)
            else:
                _, p1, pp = bend.at(Xr)
                V1, V2 = I(1.0) + p1, pp
            kap = fk(*ins, V1, V2, Xr)
            Kl = fK(*ins, V1, V2, Xr)
            nev += 1
            ub = float((kap * Kl).b)
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


def c2(rstar):
    print("C2, C2d (interval arithmetic) kappa' K'^l_l < 0 on the bent slice between its samples: the computed "
          "background, and every background within a widening of it on R < R_*")
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
        print("   C2, n = %d, A = %.3f: %d crossings; kappa' > 0 and K'^l_l < 0 certified on every sub-cell: %s (%d "
              "interval evaluations; largest upper bound of kappa' K'^l_l = %.4e)" %
              (n, rs.A_DEF, npts, good, nev, worst))
        ok &= good
    for n in (80, 160):
        good, worst, failed, nev, _ = c2_run(rs, tb, bgds[n], rs.A_DEF, fk, fK, rel=1e-3, absd=1e-6,
                                             rmax=float(rstar.b))
        print("   C2d, n = %d, R < R_* = %.4f, inputs widened by 1e-3 of their size + 1e-6: certified: %s (largest "
              "upper bound %.4e)" % (n, float(rstar.b), good, worst))
        ok &= good
    g1, w1, f1, _, _ = c2_run(rs, tb, bgds[160], 0.001, fk, fK, depth=1)
    g0, w0, f0, _, _ = c2_run(rs, tb, bgds[160], 0.0, fk, fK, depth=1)
    g5, w5, f5, _, _ = c2_run(rs, tb, bgds[160], rs.A_DEF, fk, fK, depth=1, rel=0.5, rmax=float(rstar.b))
    print("   controls: A = 0.001 not certified (%d sub-cells fail, largest upper bound %.3e; rejected): %s; A = 0 not "
          "certified (%d fail; rejected): %s; a widening of 0.5 on R < R_* not certified (%d fail; rejected): %s" %
          (f1, w1, not g1, f0, not g0, f5, not g5))
    return ok and not g1 and not g0 and not g5


# ---------------------------------------------------------------- C3: the background itself on R >= R_*
MU_OUT = 1.5
R_N0, P_N = 5.0, 0.5
QN0 = (I(MU_OUT) / I(R_N0 * R_N0) - I(1.0)) / I(2.0)               # R_u on N and on N' at the corner: -0.47, enclosed


def vhat_before(Rn):
    """vhat on N before the shell (v <= 3), as a function of R = 5 + v/2: int_5^R 2 r^2/(r^2 - 1.5) dr"""
    m = iv.sqrt(I(MU_OUT))
    F = lambda r: I(2.0) * r + m * iv.log((r - m) / (r + m))                        # noqa: E731
    return F(Rn) - F(I(R_N0))


def amp_parts(V):
    b, db = bump_parts(V, 3.0, 4.5)
    return I(3.6) * b, I(3.6) * db


def Fode(V, Y):
    R, P, Q, W = Y
    A, _ = amp_parts(V)
    return [P, -A / (I(3.0) * R * R), -(I(0.5) + I(2.0) * Q * P) / R, I(-1.0) / (I(2.0) * Q)]


def DFode(V, Y):
    R, P, Q, W = Y
    A, dA = amp_parts(V)
    Pp = -A / (I(3.0) * R * R)
    Qp = -(I(0.5) + I(2.0) * Q * P) / R
    return [Pp, -dA / (I(3.0) * R * R) + I(2.0) * A * P / (I(3.0) * R**3),
            -(I(2.0) * Qp * P + I(2.0) * Q * Pp) / R + (I(0.5) + I(2.0) * Q * P) * P / (R * R), Qp / (I(2.0) * Q * Q)]


def validated_N(h=1e-3, q_shift=0.0):
    """enclosures of (R, P, Q, vhat) on v in [3, 4.5] (step boxes and node values)"""
    R3 = I(6.5)
    Y = [R3, I(P_N), I(0.75) / (R3 * R3) - I(0.5) + I(q_shift), vhat_before(R3)]
    v = 3.0
    steps = []
    nst = int(round(1.5 / h))
    for k in range(nst):
        t0, t1 = 3.0 + k * h, 3.0 + (k + 1) * h
        T = I(t0, t1)
        H = I(t1) - I(t0)
        # a priori enclosure: B = Y + [0, h] F(T, B)
        F0 = Fode(I(t0), Y)
        B = [widen(y + I(0.0, 1.0) * H * f, 1e-6) for y, f in zip(Y, F0)]
        for _ in range(30):
            FB = Fode(T, B)
            Bn = [y + I(0.0, 1.0) * H * f for y, f in zip(Y, FB)]
            if all(bn.a >= b.a and bn.b <= b.b for bn, b in zip(Bn, B)):
                break
            B = [widen(hull(b, bn), 2 * float(bn.delta) + 1e-12) for b, bn in zip(B, Bn)]
        else:
            raise RuntimeError("no a priori enclosure at v = %g" % t0)
        D = DFode(T, B)
        Y = [y + H * f + H * H / I(2.0) * d for y, f, d in zip(Y, F0, D)]
        steps.append((t0, t1, B, Y))
    return steps


def mu_enclosure(B, T):
    R, P, Q, W = B
    A, _ = amp_parts(T)
    return R * R * (I(1.0) + I(4.0) * Q * P), I(8.0) / I(3.0) * A * Q * Q


def ray_tau(Rr):
    """tau = vhat - R along the outgoing ray u = u1 of Tangherlini (mu = 1.5) from (vhat, R) = (0, 2.321)"""
    m = iv.sqrt(I(MU_OUT))
    F = lambda r: I(2.0) * r + m * iv.log((r - m) / (r + m))                        # noqa: E731
    Rp = I(R_N0) + QN0 * I(5.7)                                         # R on N' at u1 (B = 0 before u1: linear)
    return F(Rr) - F(Rp) - Rr


def c3():
    print("C3 (interval arithmetic, the background itself) R >= R_*: hyperbolicity of Sigma' and the band on Sigma_tau0")
    rs = load('racslice5')
    tb = load('twobg5')
    tau0 = -tb.AA + 0.02
    T0 = I(tau0)
    # R_*: tau_ray increasing; bracket the crossing tau_ray = tau0
    lo, hi = 3.0, 4.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        t = ray_tau(I(mid))
        if t.b < tau0:
            lo = mid
        elif t.a > tau0:
            hi = mid
        else:
            break
    rstar = I(lo, hi)
    ok_br = ray_tau(I(lo)).b < tau0 and ray_tau(I(hi)).a > tau0
    vh3 = vhat_before(I(6.5))
    before = (I(hi) + ray_tau(I(hi))).b < vh3.a                    # the crossing is before the shell (mu = 1.5)
    print("   R_* in [%.6f, %.6f] (tau along the ray brackets tau0: %s; the crossing has vhat < vhat(v = 3) = %.5f: %s)"
          % (lo, hi, ok_br, float(vh3.a), before))
    steps = validated_N()
    W = max(max(float(y.delta) for y in st[3]) for st in steps)
    vh_end = steps[-1][3][3]
    mu_end, _ = mu_enclosure(steps[-1][3], I(4.5))
    print("   N's data on the shell, v in [3, 4.5]: %d validated steps, widest node enclosure %.1e; vhat(4.5) in [%.6f, "
          "%.6f]; mu_end in [%.6f, %.6f]" % (len(steps), W, float(vh_end.a), float(vh_end.b), float(mu_end.a),
                                             float(mu_end.b)))
    # control: a float integration lies inside the enclosures; with Q shifted by 1e-6 it does not
    from scipy.integrate import solve_ivp

    def fl(v, y):
        R, P, Q, Wv = y
        A = 3.6 * float(tb.sbump(np.array([v]), 3.0, 4.5)[0])
        return [P, -A / (3 * R * R), -(0.5 + 2 * Q * P) / R, -1 / (2 * Q)]
    y0 = [6.5, 0.5, 0.75 / 42.25 - 0.5, float(vhat_before(I(6.5)).mid)]
    inside_ok = []
    for shift in (0.0, 1e-6):
        y0s = list(y0)
        y0s[2] += shift
        sol = solve_ivp(fl, (3.0, 4.5), y0s, method='DOP853', rtol=1e-13, atol=1e-13, dense_output=True)
        ins = True
        for (t0, t1, B, Y) in steps[::50]:
            yv = sol.sol(t1)
            ins &= all(float(Yc.a) - 1e-12 <= yy <= float(Yc.b) + 1e-12 for Yc, yy in zip(Y, yv))
        inside_ok.append(ins)
    print("   control: DOP853 inside the enclosures: %s; with Q(3) shifted by 1e-6 it leaves them (rejected): %s" %
          (inside_ok[0], not inside_ok[1]))
    wlo = np.array([float(st[2][3].a) for st in steps])                # the step boxes' vhat ranges (increasing)
    whi = np.array([float(st[2][3].b) for st in steps])
    menc = [mu_enclosure(st[2], I(st[0], st[1])) for st in steps]

    def mu_on(VH):
        """enclosures of mu and mu'(vhat) for vhat in VH (region I)"""
        outs = []
        if VH.a < vh3.b:
            outs.append((I(MU_OUT), I(0.0)))
        if VH.b > vh_end.a:
            outs.append((mu_end, I(0.0)))
        if VH.b >= vh3.a and VH.a <= vh_end.b:
            k0 = max(0, int(np.searchsorted(whi, float(VH.a))) - 2)
            k1 = min(len(steps), int(np.searchsorted(wlo, float(VH.b))) + 2)
            for k in range(k0, k1):
                Wb = steps[k][2][3]
                if Wb.b < VH.a or Wb.a > VH.b:
                    continue
                outs.append(menc[k])
            assert k0 == 0 or steps[k0 - 1][2][3].b < VH.a
            assert k1 == len(steps) or steps[k1][2][3].a > VH.b
        return hull(*[o[0] for o in outs]), hull(*[o[1] for o in outs])
    kap, Kll = rs.slice_formulas()
    fk = sp.lambdify(rs.SYMS, kap, modules=MODS)
    fK = sp.lambdify(rs.SYMS, Kll, modules=MODS)
    bend = Bend(rs, rs.A_DEF)
    # Sigma' with R >= R_* lies in {u <= u1}: tau = vhat - R increases along the ray u = u1 wherever it is untrapped
    # (d tau/dR = 2/f - 1 > 0), the ray is untrapped there (R^2 > mu_end >= mu, mu nondecreasing in vhat), and on the
    # bend's support tau0 + phi stays below tau_ray(3.5) <= tau_ray(R); so the ingoing ray through each point of
    # Sigma' meets the ray u1 at a smaller R, that is, the point has u <= u1
    phmax = max(float(bend.at(I(bend.r[k], bend.r[k + 1]))[0].b) for k in range(0, bend.n, 1))
    t35 = ray_tau(I(bend.x0))
    r_ok = (float(rstar.a) ** 2 > float(mu_end.b) and phmax < float((t35 - T0).a) and (I(bend.x0) + t35).b < vh3.a
            and (vh_end - T0).b < bend.x1)
    print("   Sigma' (R >= R_*) in {u <= u1}: R_*^2 > mu_end: %s; phi < tau_ray(%.2f) - tau0 = %.4f on the support "
          "(phi <= %.1e): %s; the ray reaches R = %.2f before the shell: %s; the shell ends on Sigma_tau0 at R < %.4f "
          "< %.2f: %s" % (float(rstar.a) ** 2 > float(mu_end.b), bend.x0, float((t35 - T0).a), phmax,
                          phmax < float((t35 - T0).a), bend.x0, (I(bend.x0) + t35).b < vh3.a,
                          float((vh_end - T0).b), bend.x1, (vh_end - T0).b < bend.x1))

    def cert(A_on, rlo, rhi, ncell=2300, depth=10):
        worst, failed, nev = None, 0, 0
        e = np.linspace(rlo, rhi, ncell + 1)
        stack = [(a, b, 0) for a, b in zip(e[:-1], e[1:])]
        while stack:
            a, b, d = stack.pop()
            Xr = I(a, b)
            if A_on:
                p0, p1, pp = bend.at(Xr)
            else:
                p0, p1, pp = I(0.0), I(0.0), I(0.0)
            VH = T0 + Xr + p0
            mu, mup = mu_on(VH)
            f = I(1.0) - mu / (Xr * Xr)
            ins = [I(1.0), f, I(0.0), I(0.0), I(2.0) * mu / Xr**3, -mup / (Xr * Xr)]
            k_ = fk(*ins, I(1.0) + p1, pp, Xr)
            K_ = fK(*ins, I(1.0) + p1, pp, Xr)
            nev += 1
            ub = float((k_ * K_).b)
            if float(k_.a) > 0 and float(K_.b) < 0:
                worst = ub if worst is None or ub > worst else worst
                continue
            if d >= depth:
                failed += 1
                worst = ub if worst is None or ub > worst else worst
                continue
            m = 0.5 * (a + b)
            stack += [(a, m, d + 1), (m, b, d + 1)]
        return failed == 0, worst, failed, nev
    good, worst, failed, nev = cert(True, float(rstar.b), 5.75)
    print("   Sigma' (A = %.2f) on R in [R_*, 5.75]: kappa' > 0 and K'^l_l < 0 certified on every cell: %s (%d interval "
          "evaluations; largest upper bound of kappa' K'^l_l = %.4e); beyond 5.75, Sigma' = Sigma_tau0 in Tangherlini "
          "of mass mu_end, Nk = (mu/R^3)(f - 3) < 0 exactly" % (rs.A_DEF, good, nev, worst))
    g0, w0, f0, _ = cert(False, float(rstar.b), 5.75, depth=3)
    print("   control: Sigma_tau0 (A = 0) not certified (%d cells fail; rejected): %s" % (f0, not g0))
    # the band on Sigma_tau0: the sign of Nk = (mu/R^3)(f - 3) + mu'/(2 R^2), cell by cell
    e = np.linspace(4.0, 4.8, 8001)
    signs = []
    for a, b in zip(e[:-1], e[1:]):
        Xr = I(a, b)
        mu, mup = mu_on(T0 + Xr)
        Nk = mu / Xr**3 * (I(1.0) - mu / (Xr * Xr) - I(3.0)) + mup / (I(2.0) * Xr * Xr)
        signs.append(1 if Nk.a > 0 else (-1 if Nk.b < 0 else 0))
    und = [i for i, sgn in enumerate(signs) if sgn == 0]
    pos = [i for i, sgn in enumerate(signs) if sgn == 1]
    groups = []
    for i in und:
        if groups and i == groups[-1][-1] + 1:
            groups[-1].append(i)
        else:
            groups.append([i])
    edges = [(e[g[0]], e[g[-1] + 1]) for g in groups]
    band_ok = (len(groups) == 2 and pos and min(pos) > groups[0][-1] and max(pos) < groups[1][0] and
               all(sgn == -1 for sgn in signs[:groups[0][0]]) and all(sgn == -1 for sgn in signs[groups[1][-1] + 1:]))
    print("   the band on Sigma_tau0, the background itself: Nk < 0 certified on [4.0, 4.8] outside the edge enclosures "
          "%s, Nk > 0 certified between them: %s" %
          (", ".join("[%.4f, %.4f]" % ed for ed in edges), band_ok))
    ok = ok_br and before and W < 1e-6 and inside_ok[0] and not inside_ok[1] and good and not g0 and band_ok and r_ok
    return ok, rstar


def main():
    q = load('qsign5')
    res = {}
    res['C3'], rstar = c3()
    print('C3', 'PASS' if res['C3'] else 'FAIL', flush=True)
    bgs = {80: q.background(80), 160: q.background(160)}
    res['C1'] = c1(bgs)
    print('C1', 'PASS' if res['C1'] else 'FAIL', flush=True)
    res['C2'] = c2(rstar)
    print('C2', 'PASS' if res['C2'] else 'FAIL', flush=True)
    return 0 if all(res.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
