#!/usr/bin/env python3
"""truebg5: the background itself on Sigma_tau0 below R_*, certified (FAMILIES5-R8.md section R8.2).

intcert5 C3 certifies the background itself on {u <= u1}, which holds Sigma' for R >= R_*. This program does the rest
of Sigma' (R < R_* < 3.5, where Sigma' = Sigma_tau0), so that with C3 the two margins are certified for the background
defined by the stated characteristic data, not only for its computed approximation.

The reduction (deduced; checked here). On Sigma_tau0, R < R_* means vhat = tau0 + R < tau0 + R_* < vhat(v = 3), so the
whole of it lies in {v < 3}, where the ingoing shell's source A vanishes. There G1 (a) gives mu_v = 0, and the
v-Raychaudhuri equation gives d_v (e^(-2s) R_v) = 0: the mass mu and lambda := e^(-2s) R_v are constant along each
outgoing ray and equal their values on N' = {v = 0}. With f = 1 - mu/R^2 = -2 e^(-2s) R_u R_v (the mass function),
R_u = -f/(2 lambda) at every point. So along each ingoing ray (v fixed) R(u) solves the ODE

    dR/du = G(u, R) := -(1 - mu(u)/R^2)/(2 lambda(u)),   mu(u), lambda(u) from N',

which is regular wherever lambda > 0 (checked on [u1, u2]). On N' (e^(2s) = 1/2): R'' = -B/(3 R^2), B = 1.7 b(u; 5.7,
7.2), R(0) = 5, R'(0) = (1.5/25 - 1)/2; Qv = R_v with Qv' = -(1/2 + 2 Qv R')/R, Qv(0) = 1/2; mu = R^2 (1 + 4 Qv R'),
lambda = 2 Qv, mu' = -(4/3) B Qv (all exact before u1, where R is linear). The ingoing ray with label vhat meets the
outgoing ray u1 at R1(vhat), F(R1) = vhat + F(R_N'(u1)), F(R) = 2 R + sqrt(1.5) ln((R - sqrt 1.5)/(R + sqrt 1.5))
(Tangherlini of mass 1.5 in region I, intcert5 C3). With J, K, L the first three derivatives of R(u) in R1, and
r1', r1'', r1''' those of R1 in vhat, every input of the margins is closed-form in (R, J, K, L) and the N' data:

  in the packet (u1 < u < u2):  e^psi = 2 J r1'/f,  psi_R = B/(3 R^2 G^2),  f_R = 2 mu/R^3 - mu'/(R^2 G),
      f_vhat = mu' J r1'/(R^2 G),  psi_vhat = K r1'/J + r1''/r1' - 2 mu J r1'/(R^3 f) - (J r1'/G) B/(3 R^2 G);
  in region III (u >= u2, vacuum of mass mu3 = mu(u2)): psi = psi_III(vhat) = ln(2 J2 r1'/f3(R2)) from the ray's
      values at u2, psi_III' = K2 r1'/J2 + r1''/r1' - 2 mu3 J2 r1' h(R2), h = 1/(R^3 - mu3 R), and psi_III'' its
      derivative (with L2, r1''').

(e^psi = d U/d vhat at fixed R, U the outgoing Vaidya time with U' = 1/lambda; in region I these give e^psi = 1,
psi_vhat = 0, checked symbolically.) Region III's psi_III is fixed at u2, where the ray is untrapped (f > 0 checked),
so it holds at the trapped points of the seed region too.

Validated integration (mpmath iv, 80 bits): the N' data and each ray (R, J, K, L), Taylor order one with an a priori
enclosure over the step box and a second-order remainder (the total derivative, computed symbolically), h = 1e-3 in
u, cells in vhat of 0.01 (bisected where needed), point rays at the cell ends.

  T1  the N' data on [u1, u2] enclosed; lambda > 0; mu3; checked against a float integration (scipy DOP853), which a
      shifted B amplitude (1.7 -> 1.7017) leaves (control, must fail).
  T2  Gamma > 0 on the seed region R in [0.70, 1.861] for the background itself (Theorem Q's margin), on T3's cells
      clipped to the region: every cell lies in region III (R2 >= R on the slice, f3 > 0 at u2), and a posteriori the
      computed spline (qsign5, n = 160) is within intcert5 C1d's tube of the true psi_III: certified bounds on
      sup |psi_spline^(k) - psi_III^(k)|, k = 0, 1, 2 (point rays at the cell ends, centred forms with the cells'
      enclosures for k = 0, 1, the cells' enclosures for k = 2) and on |mu3 - mu0|, all within C1d's d and d mu. C1d
      certifies Gamma > 0 for every background in the tube, so for this one. Control: with B's amplitude x 1.001 in
      the reduction, the spline is farther from it than that agreement.
  T3  kappa K^l_l < 0 on Sigma_tau0 for R in [0.68, R_*] (vhat in [0, tau0 + R_*]: the part of Sigma' in the
      development of the data below R_*) for the background itself (Theorem L''s margin; Sigma' = Sigma_tau0 there),
      with the region I, packet and region III formulas on every cell according to where the slice point can lie.
      Control: with every packet input widened by half its size the step boxes are not all certified.
  T4  a posteriori in the packet: the computed background's slice inputs (twobg5 n = 160, racslice5's crossing
      data) against the true ones, certified upper bounds on the deviation; informational (sanity bound 0.2 of the
      input's size), since T3 does not use the computed background.

Labels: certified (interval arithmetic) for T2-T4; the reduction is deduced, its region I limit checked exactly, and
its packet and region III values agree with the computed background to its discretisation level (T2, T4). Order of
the run: T1, T3, T2, T4. Run: python3 checks/truebg5.py   (one to two hours under load)
"""
import importlib.util
import math
import os
import sys
import time

import numpy as np
import sympy as sp
from mpmath import iv

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
iv.prec = 80


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


ic = load('intcert5')
tb = load('twobg5')
I, hull, widen, bump_parts, MODS = ic.I, ic.hull, ic.widen, ic.bump_parts, ic.MODS
U1, U2 = tb.U1P, tb.U2P
MU1, R00 = tb.MUC, tb.R0
TAU0 = -tb.AA + 0.02
T0 = I(TAU0)
QN0 = (I(MU1) / I(R00 * R00) - I(1.0)) / I(2.0)                 # R_u at the corner, -0.47 enclosed
HSTEP = 1e-3
NST = int(round((U2 - U1) / HSTEP))
UE = [U1 + k * (U2 - U1) / NST for k in range(NST)] + [U2]      # float step edges in u, exactly U1 and U2 at the ends


def mag(x):
    return max(abs(float(x.a)), abs(float(x.b)))


def sub(x, y):
    """x intersected with y (both intervals); None if empty"""
    lo, hi = max(x.a, y.a), min(x.b, y.b)
    return iv.mpf([lo, hi]) if lo <= hi else None


# ---------------------------------------------------------------- a validated step
def vstep(F, DF, Y, H, cn, cb):
    """Y at t0 -> (box over [t0, t1], Y at t1): F(Y, c) the field, DF(Y, c) its total derivative; cn the
    coefficients at t0, cb over the step"""
    F0 = F(Y, cn)
    B = [widen(y + I(0.0, 1.0) * H * f, 1e-12 + 1e-9 * mag(y)) for y, f in zip(Y, F0)]
    for _ in range(40):
        FB = F(B, cb)
        Bn = [y + I(0.0, 1.0) * H * f for y, f in zip(Y, FB)]
        if all(bn.a >= b.a and bn.b <= b.b for bn, b in zip(Bn, B)):
            break
        B = [widen(hull(b, bn), 2 * float(bn.delta) + 1e-12) for b, bn in zip(B, Bn)]
    else:
        raise RuntimeError("no a priori enclosure")
    D = DF(B, cb)
    return B, [y + H * f + H * H / I(2.0) * d for y, f, d in zip(Y, F0, D)]


# ---------------------------------------------------------------- the data on N'
def amp(T, bamp):
    b, db = bump_parts(T, U1, U2)
    return I(bamp) * b, I(bamp) * db


def Fn(Y, c):
    R, P, Qv = Y
    B = c
    return [P, -B / (I(3.0) * R * R), -(I(0.5) + I(2.0) * Qv * P) / R]


def DFn(Y, c):
    R, P, Qv = Y
    B, dB = c
    Pp = -B / (I(3.0) * R * R)
    Qp = -(I(0.5) + I(2.0) * Qv * P) / R
    return [Pp, -dB / (I(3.0) * R * R) + I(2.0) * B * P / (I(3.0) * R**3),
            -(I(2.0) * Qp * P + I(2.0) * Qv * Pp) / R + (I(0.5) + I(2.0) * Qv * P) * P / (R * R)]


def nprime_data(bamp=1.7):
    """the N' data on [u1, u2]: node enclosures and step boxes; and the ray coefficients (mu, lam, mu', lam', B)"""
    R1 = I(R00) + QN0 * I(U1)
    Y = [R1, QN0, (I(MU1) / (R1 * R1) - I(1.0)) / (I(4.0) * QN0)]
    nodes, boxes = [Y], []
    for k in range(NST):
        T = I(UE[k], UE[k + 1])
        H = I(UE[k + 1]) - I(UE[k])
        Bn, _ = amp(I(UE[k]), bamp)
        box, Y = vstep_n(Y, H, Bn, amp(T, bamp))
        nodes.append(Y)
        boxes.append(box)
    return nodes, boxes


def vstep_n(Y, H, Bn, BT):
    F0 = Fn(Y, Bn)
    B = [widen(y + I(0.0, 1.0) * H * f, 1e-12 + 1e-9 * mag(y)) for y, f in zip(Y, F0)]
    for _ in range(40):
        FB = Fn(B, BT[0])
        Bx = [y + I(0.0, 1.0) * H * f for y, f in zip(Y, FB)]
        if all(bn.a >= b.a and bn.b <= b.b for bn, b in zip(Bx, B)):
            break
        B = [widen(hull(b, bn), 2 * float(bn.delta) + 1e-12) for b, bn in zip(B, Bx)]
    else:
        raise RuntimeError("no a priori enclosure on N'")
    D = DFn(B, BT)
    return B, [y + H * f + H * H / I(2.0) * d for y, f, d in zip(Y, F0, D)]


def coeffs(Y, B):
    """(mu, lam, mu', lam') from (R, R_u, R_v) on N' and the source B"""
    R, P, Qv = Y
    return (R * R * (I(1.0) + I(4.0) * Qv * P), I(2.0) * Qv, -I(4.0) / I(3.0) * B * Qv,
            -I(2.0) * (I(0.5) + I(2.0) * Qv * P) / R)


# ---------------------------------------------------------------- the ray system, symbolically
def ray_system():
    R, J, K, L, mu, lam, mup, lamp = sp.symbols('R J K L mu lam mup lamp')
    G = (mu / R**2 - 1) / (2 * lam)
    GR, GRR, GRRR = [sp.diff(G, R, k) for k in (1, 2, 3)]
    Fv = [G, GR * J, GR * K + GRR * J**2, GR * L + 3 * GRR * J * K + GRRR * J**3]
    ys = [R, J, K, L]
    DFv = [sp.diff(Fi, mu) * mup + sp.diff(Fi, lam) * lamp + sum(sp.diff(Fi, y) * Fj for y, Fj in zip(ys, Fv))
           for Fi in Fv]
    args = ys + [mu, lam, mup, lamp]
    fF = sp.lambdify(args, Fv, modules=MODS, cse=True)
    fD = sp.lambdify(args, DFv, modules=MODS, cse=True)
    # check: the first three are the derivatives in R1 of the first (J, K, L the variations): d/dR1 of R' = G R_R1
    return fF, fD


FF, FD = ray_system()


def Fr(Y, c):
    mu, lam, mup, lamp = c
    return FF(*Y, mu, lam, mup, lamp)


def DFr(Y, c):
    mu, lam, mup, lamp = c
    return FD(*Y, mu, lam, mup, lamp)


class NData:
    def __init__(self, bamp=1.7):
        self.bamp = bamp
        self.nodes, self.boxes = nprime_data(bamp)
        self.cn = [coeffs(self.nodes[k], amp(I(UE[k]), bamp)[0]) for k in range(NST + 1)]
        self.cb = [coeffs(self.boxes[k], amp(I(UE[k], UE[k + 1]), bamp)[0]) for k in range(NST)]
        self.Bb = [amp(I(UE[k], UE[k + 1]), bamp)[0] for k in range(NST)]
        self.mu3 = self.cn[-1][0]
        self.lam_min = min(float(c[1].a) for c in self.cb)


def ray(nd, R1, keep=False):
    """integrate (R, J, K, L) from u1 to u2 for the ingoing rays starting at R1 (an interval)"""
    Y = [R1, I(1.0), I(0.0), I(0.0)]
    boxes = []
    for k in range(NST):
        H = I(UE[k + 1]) - I(UE[k])
        box, Y = vstep(Fr, DFr, Y, H, nd.cn[k], nd.cb[k])
        if keep:
            boxes.append(box)
    return Y, boxes


# ---------------------------------------------------------------- region I: R1(vhat) and its derivatives
SQ = iv.sqrt(I(MU1))


def Ff(r):
    return I(2.0) * r + SQ * iv.log((r - SQ) / (r + SQ))


RP = I(R00) + QN0 * I(U1)
CF = Ff(RP)                                                     # F(R_N'(u1))


def r1_enclose(VH):
    """R1 for vhat in VH: F(R1) = vhat + F(R_N'(u1)), F increasing on R > sqrt(1.5)"""
    tg = VH + CF

    def solve(y):                                                # float bisection for F(r) = y
        lo, hi = 1.3, 10.0
        for _ in range(200):
            m = 0.5 * (lo + hi)
            if float(Ff(I(m)).mid) < y:
                lo = m
            else:
                hi = m
            if hi - lo <= 4e-16 * hi:
                break
        return 0.5 * (lo + hi)
    lo = solve(float(tg.a))
    step = 1e-15
    while not (Ff(I(lo)).b < tg.a):                              # F(lo) < every target: R1 > lo
        lo -= step
        step *= 2
    hi = solve(float(tg.b))
    step = 1e-15
    while not (Ff(I(hi)).a > tg.b):                              # F(hi) > every target: R1 < hi
        hi += step
        step *= 2
    return I(lo, hi)


def rstar_enclose():
    """R_*: the crossing of the ray u = u1 with Sigma_tau0 (as in intcert5 C3)"""
    lo, hi = 3.0, 4.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        t = ic.ray_tau(I(mid))
        if t.b < TAU0:
            lo = mid
        elif t.a > TAU0:
            hi = mid
        else:
            break
    assert ic.ray_tau(I(lo)).b < TAU0 and ic.ray_tau(I(hi)).a > TAU0
    return I(lo, hi)


def r1_derivs(R1):
    """r1', r1'', r1''' (derivatives of R1 in vhat) on R1: inverse-function rule with F', F'', F'''"""
    m = I(MU1)
    D = R1 * R1 - m
    F1 = I(2.0) * R1 * R1 / D
    F2 = -I(4.0) * R1 * m / (D * D)
    F3 = I(4.0) * m * (I(3.0) * R1 * R1 + m) / D**3
    return I(1.0) / F1, -F2 / F1**3, (I(3.0) * F2 * F2 - F1 * F3) / F1**5


# ---------------------------------------------------------------- the inputs
def psi3(R1, Y2, mu3):
    """psi_III, psi_III', psi_III'' at vhat from the ray's values at u2"""
    R2, J2, K2, L2 = Y2
    a1, a2, a3 = r1_derivs(R1)
    D = R2**3 - mu3 * R2
    h = I(1.0) / D
    hp = -(I(3.0) * R2 * R2 - mu3) / (D * D)
    f3 = I(1.0) - mu3 / (R2 * R2)
    p0 = iv.log(I(2.0) * J2 * a1 / f3)
    p1 = K2 * a1 / J2 + a2 / a1 - I(2.0) * mu3 * J2 * a1 * h
    p2 = ((L2 * a1 * a1 + K2 * a2) / J2 - K2 * K2 * a1 * a1 / (J2 * J2) + (a3 * a1 - a2 * a2) / (a1 * a1)
          - I(2.0) * mu3 * (K2 * a1 * a1 * h + J2 * a2 * h + J2 * J2 * a1 * a1 * hp))
    return p0, p1, p2, f3


def packet_inputs(R, J, K, c, B, a1, a2):
    mu, lam, mup, _ = c
    f = I(1.0) - mu / (R * R)
    G = -f / (I(2.0) * lam)
    E = I(2.0) * J * a1 / f
    fR = I(2.0) * mu / R**3 - mup / (R * R * G)
    fv = mup * J * a1 / (R * R * G)
    pR = B / (I(3.0) * R * R * G * G)
    pv = K * a1 / J + a2 / a1 - I(2.0) * mu * J * a1 / (R**3 * f) - (J * a1 / G) * B / (I(3.0) * R * R * G)
    return [E, f, pR, pv, fR, fv], f


def symbolic_checks():
    """region I limit of the packet formulas (J = 1, K = 0, B = 0, mu' = 0, R = R1): E = 1, psi_vhat = 0, f_R = 2 mu/R^3;
    and the u2 limit (B = 0) of psi_vhat is psi_III'"""
    R, mu, lam = sp.symbols('R mu lam', positive=True)
    f = 1 - mu / R**2
    F1 = 2 * R**2 / (R**2 - mu)
    F2 = sp.diff(F1, R)
    a1, a2 = 1 / F1, -F2 / F1**3
    G = -f / (2 * lam)
    E = 2 * a1 / f
    pv = a2 / a1 - 2 * mu * a1 / (R**3 * f)
    ok1 = sp.simplify(E - 1) == 0 and sp.simplify(pv) == 0
    # the inverse-function derivatives against a direct differentiation of the inverse (a numeric spot check)
    import mpmath
    Fn_ = lambda r: 2 * r + mpmath.sqrt(1.5) * mpmath.log((r - mpmath.sqrt(1.5)) / (r + mpmath.sqrt(1.5)))  # noqa
    mpmath.mp.dps = 30
    y0 = Fn_(mpmath.mpf(2.6))
    inv = lambda y: mpmath.findroot(lambda r: Fn_(r) - y, 2.6)                 # noqa: E731
    d1, d2, d3 = [mpmath.diff(inv, y0, n) for n in (1, 2, 3)]
    mpmath.mp.dps = 15
    e1, e2, e3 = r1_derivs(I(2.6))
    ok2 = all(abs(float(d) - float(e.mid)) < 1e-10 * (1 + abs(float(d))) for d, e in ((d1, e1), (d2, e2), (d3, e3)))
    del G
    return ok1, ok2


# ---------------------------------------------------------------- T1
def t1():
    print("T1 the data on N' over the packet, u in [5.7, 7.2], enclosed (validated, %d steps of %g)" % (NST, HSTEP))
    t = time.time()
    nd = NData()
    W = max(max(float(y.delta) for y in Y) for Y in nd.nodes)
    print("   widest node enclosure %.1e; lambda = 2 R_v >= %.4f > 0 on every step: %s; mu3 = mu(u2) in [%.8f, %.8f];"
          " R_N'(u2) in [%.6f, %.6f] > sqrt(mu3): %s (%.0f s)" %
          (W, nd.lam_min, nd.lam_min > 0, float(nd.mu3.a), float(nd.mu3.b), float(nd.nodes[-1][0].a),
           float(nd.nodes[-1][0].b), nd.nodes[-1][0].a ** 2 > nd.mu3.b, time.time() - t))
    from scipy.integrate import solve_ivp

    def fl(u, y, bamp):
        R, P, Qv = y
        B = bamp * float(tb.sbump(np.array([u]), U1, U2)[0])
        return [P, -B / (3 * R * R), -(0.5 + 2 * Qv * P) / R]
    r1 = 5.0 - 0.47 * U1
    y0 = [r1, -0.47, (1.5 / r1**2 - 1) / (4 * -0.47)]
    ins = []
    for bamp in (1.7, 1.7017):
        sol = solve_ivp(fl, (U1, U2), y0, args=(bamp,), method='DOP853', rtol=1e-13, atol=1e-14, dense_output=True)
        ok = True
        for k in range(0, NST + 1, 50):
            yv = sol.sol(UE[k])
            ok &= all(float(Yc.a) - 1e-12 <= yy <= float(Yc.b) + 1e-12 for Yc, yy in zip(nd.nodes[k], yv))
        ins.append(ok)
    syms = symbolic_checks()
    print("   control: DOP853 inside the enclosures: %s; with B's amplitude 1.7 -> 1.7017 it leaves them (rejected): %s"
          % (ins[0], not ins[1]))
    print("   the reduction's region I limit (exact): e^psi = 1 and psi_vhat = 0: %s; the inverse-function derivatives "
          "r1', r1'', r1''' against a 30-digit differentiation of the inverse: %s" % syms)
    ok = W < 1e-5 and nd.lam_min > 0 and nd.nodes[-1][0].a ** 2 > nd.mu3.b and ins[0] and not ins[1] and all(syms)
    return ok, nd


# ---------------------------------------------------------------- T2
def spline_enclose(bg, VH):
    from scipy.interpolate import PPoly
    pp = PPoly.from_spline(bg['sp_psi']._eval_args)
    lo, hi = float(VH.a), float(VH.b)
    i0 = int(np.searchsorted(pp.x, lo, side='right') - 1)
    i1 = int(np.searchsorted(pp.x, hi, side='right') - 1)
    outs = []
    for i in range(i0, i1 + 1):
        a, b = max(lo, float(pp.x[i])), min(hi, float(pp.x[i + 1]))
        if a > b:
            continue
        outs.append(ic.ppoly_enclose(pp, i, I(a, b)))
    return [hull(*[o[k] for o in outs]) for k in range(3)]


def t2(nd, bgs, cache, lo=0.70, hi=1.861):
    print("T2 Gamma > 0 on the seed region R in [%.2f, %.3f] for the background itself: the computed spline is within "
          "intcert5 C1d's tube of psi_III (certified a posteriori), and C1d certifies Gamma > 0 on the tube" % (lo, hi))
    d, dmu = ic.D_C1D, ic.DMU_C1D
    va, vb = float((I(lo) + T0).a), float((I(hi) + T0).b)
    cells = sorted(k for k in cache if k[1] > va and k[0] < vb)
    assert cells[0][0] <= va and cells[-1][1] >= vb and all(x[1] == y[0] for x, y in zip(cells[:-1], cells[1:]))
    t = time.time()
    sp160 = bgs[160]
    # point rays at the cell ends (clipped to the region): e^(k) := spline^(k) - psi_III^(k) enclosed there
    pts = [va] + [a for a, b in cells if va < a < vb] + [vb]
    pe = {}
    for x in pts:
        VH = I(x)
        R1 = r1_enclose(VH)
        Y2, _ = ray(nd, R1)
        tr = psi3(R1, Y2, nd.mu3)[:3]
        sv = spline_enclose(sp160, VH)
        pe[x] = [sv[k] - tr[k] for k in range(3)]
    reg3, sup, cellw = True, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]
    for a, b in cells:
        a_, b_ = max(a, va), min(b, vb)
        Rs = I(a_, b_) - T0
        R1, Y2 = cache[(a, b)]
        p0, p1, p2, f3 = psi3(R1, Y2, nd.mu3)
        reg3 &= bool(Y2[0].a >= Rs.b) and bool(f3.a > 0)
        svc = spline_enclose(sp160, I(a_, b_))
        ec = [svc[k] - y for k, y in enumerate((p0, p1, p2))]       # e^(k) on the cell (cell variation included)
        h = float((I(b_) - I(a_)).b)
        # centred forms from both ends: |e(x)| <= |e(end)| + h sup|e'|, |e'(x)| <= |e'(end)| + h sup|e''|
        b0 = min(mag(pe[a_][0]), mag(pe[b_][0])) + h * mag(ec[1])
        b1 = min(mag(pe[a_][1]), mag(pe[b_][1])) + h * mag(ec[2])
        b2 = mag(ec[2])
        for k, v in enumerate((b0, b1, b2)):
            sup[k] = max(sup[k], v)
        for k in range(3):
            cellw[k] = max(cellw[k], mag(ec[k]))
    perr = [max(mag(pe[x][k]) for x in pts) for k in range(3)]
    dmu_ = mag(nd.mu3 - I(bgs[160]['mu0']))
    inside = all(sup[k] <= d[k] for k in range(3)) and dmu_ <= dmu
    print("   every cell in region III (R2 >= R on the slice, f3 > 0 at u2): %s (%d cells, %d point rays; %.0f s)"
          % (reg3, len(cells), len(pts), time.time() - t))
    print("   a posteriori, the computed spline (n = 160) against psi_III, certified: |e^(k)| <= %.1e, %.1e, %.1e "
          "(k = 0, 1, 2) at the %d cell ends; on the whole region sup |e^(k)| <= %.1e, %.1e, %.1e (centred forms for "
          "k = 0, 1, the cell enclosure for k = 2); |mu3 - mu0| <= %.1e" % (*perr, len(pts), *sup, dmu_))
    print("   within intcert5 C1d's tube d = %s, |d mu| <= %.0e, on which C1d certifies Gamma > 0: %s -- so Gamma > 0 "
          "on the seed region for the background itself" % (d, dmu, inside))
    t0, Rs_ = bgs[160]['tau0'], np.linspace(lo, hi, 2001)
    s80, s160 = bgs[80]['sp_psi'], bgs[160]['sp_psi']
    d8 = [float(np.max(np.abs(s80.derivative(k)(t0 + Rs_) - s160.derivative(k)(t0 + Rs_)))) if k else
          float(np.max(np.abs(s80(t0 + Rs_) - s160(t0 + Rs_)))) for k in range(3)]
    print("   (the n = 80 and 160 splines differ by %.1e, %.1e, %.1e, sampled: the discretisation error is larger than "
          "the n-convergence suggested, and inside the tube)" % tuple(d8))
    # control: B's amplitude shifted by 0.1 %: the spline is farther from that psi_III than the agreement above
    nd2 = NData(bamp=1.7 * 1.001)
    cerr = 0.0
    for x in pts[::10]:
        VH = I(x)
        R1 = r1_enclose(VH)
        Y2, _ = ray(nd2, R1)
        dd = spline_enclose(sp160, VH)[0] - psi3(R1, Y2, nd2.mu3)[0]
        cerr = max(cerr, 0.0 if dd.a <= 0 <= dd.b else min(abs(float(dd.a)), abs(float(dd.b))))
    print("   control: with B's amplitude x 1.001 in the reduction the spline is at least %.1e from it at the points, "
          "more than the agreement %.1e above (rejected): %s" % (cerr, perr[0], cerr > perr[0]))
    return reg3 and inside and cerr > perr[0]


# ---------------------------------------------------------------- T3
def t3(nd, rstar, cache):
    print("T3 kappa K^l_l < 0 on Sigma_tau0, R in [0.68, R_*], for the background itself (cells of 0.01 in vhat)")
    rs = load('racslice5')
    kap, Kll = rs.slice_formulas()
    fk = sp.lambdify(rs.SYMS, kap, modules=MODS)
    fK = sp.lambdify(rs.SYMS, Kll, modules=MODS)
    va, vb = 0.0, float((I(rstar.b) + T0).b)
    ncell = int(math.ceil((vb - va) / 0.01))
    e = np.linspace(va, vb, ncell + 1)
    worst, failed, nev, nray = None, 0, 0, 0
    counts = {'I': 0, 'packet': 0, 'III': 0}
    ctl_fail = 0
    t = time.time()

    def test(ins, R):
        k_ = fk(*ins, I(1.0), I(0.0), R)
        K_ = fK(*ins, I(1.0), I(0.0), R)
        return float(k_.a) > 0 and float(K_.b) < 0, float((k_ * K_).b)

    stack = [(a, b, 0) for a, b in zip(e[:-1], e[1:])]
    while stack:
        a, b, d = stack.pop()
        VH = I(a, b)
        Rs = VH - T0
        R1 = r1_enclose(VH)
        a1, a2, _ = r1_derivs(R1)
        Y2, boxes = ray(nd, R1, keep=True)
        if d == 0:
            cache[(a, b)] = (R1, Y2)
        nray += 1
        good, cell_worst = True, None
        # region I part: slice points with u <= u1 (R on the slice >= R1)
        if Rs.b >= R1.a:
            R = sub(Rs, iv.mpf([R1.a, Rs.b]))
            ins = [I(1.0), I(1.0) - I(MU1) / (R * R), I(0.0), I(0.0), I(2.0) * I(MU1) / R**3, I(0.0)]
            g, w = test(ins, R)
            good &= g
            cell_worst = w
            counts['I'] += 1
        # packet: every step whose box meets the slice's R
        for k, box in enumerate(boxes):
            R = sub(box[0], Rs)
            if R is None:
                continue
            ins, f = packet_inputs(R, box[1], box[2], nd.cb[k], nd.Bb[k], a1, a2)
            g, w = test(ins, R)
            if not (f.a > 0):
                g = False
            good &= g
            cell_worst = w if cell_worst is None else max(cell_worst, w)
            counts['packet'] += 1
            if not test([widen(x, 0.5 * mag(x)) for x in ins], R)[0]:     # control: inputs widened by half
                ctl_fail += 1
        # region III: slice points with u >= u2 (R2 >= R on the slice)
        if Y2[0].b >= Rs.a:
            R = sub(Rs, iv.mpf([Rs.a, Y2[0].b]))
            p0, p1, _, _ = psi3(R1, Y2, nd.mu3)
            ins = [iv.exp(p0), I(1.0) - nd.mu3 / (R * R), I(0.0), p1, I(2.0) * nd.mu3 / R**3, I(0.0)]
            g, w = test(ins, R)
            good &= g
            cell_worst = w if cell_worst is None else max(cell_worst, w)
            counts['III'] += 1
        nev += 1
        if good:
            worst = cell_worst if worst is None else max(worst, cell_worst)
            continue
        if d >= 3:
            failed += 1
            worst = cell_worst if worst is None else max(worst, cell_worst)
            continue
        m = 0.5 * (a + b)
        stack += [(a, m, d + 1), (m, b, d + 1)]
    print("   certified on every cell: %s (%d rays; slice pieces tested: region I %d, packet %d step boxes, region III "
          "%d; largest upper bound of kappa K^l_l = %.4e; %.0f s)" %
          (failed == 0, nray, counts['I'], counts['packet'], counts['III'], worst, time.time() - t))
    print("   control: every packet input widened by half its size, %d of %d step boxes not certified (rejected): %s"
          % (ctl_fail, counts['packet'], ctl_fail > 0))
    return failed == 0 and ctl_fail > 0 and counts['packet'] > 0 and counts['III'] > 0


# ---------------------------------------------------------------- T4
def t4(nd, rstar, n=160, every=6):
    print("T4 a posteriori in the packet: the computed background's slice inputs (twobg5 n = %d, racslice5's crossing "
          "data, A = 0) against the background itself" % n)
    rs = load('racslice5')
    o = rs.crossing(tb, tb.run(n), 0.0)
    o = o[np.argsort(o[:, 0])]
    names = ('E', 'f', 'psi_R', 'psi_vhat', 'f_R', 'f_vhat')
    dev = [0.0] * 6
    scale = [0.0] * 6
    npt = 0
    for row in o[::every]:
        R = float(row[0])
        if not (1.0 < R < float(rstar.a)):
            continue
        VH = I(R) + T0
        R1 = r1_enclose(VH)
        a1, a2, _ = r1_derivs(R1)
        Y2, boxes = ray(nd, R1, keep=True)
        if not (Y2[0].b < R < R1.a):                             # strictly inside the packet
            continue
        enc = None
        for k, box in enumerate(boxes):
            Rx = sub(box[0], I(R))
            if Rx is None:
                continue
            ins, _ = packet_inputs(Rx, box[1], box[2], nd.cb[k], nd.Bb[k], a1, a2)
            enc = ins if enc is None else [hull(x, y) for x, y in zip(enc, ins)]
        npt += 1
        for j in range(6):
            dev[j] = max(dev[j], mag(enc[j] - I(float(row[1 + j]))))
            scale[j] = max(scale[j], mag(enc[j]))
    print("   %d crossings in the packet: max |computed - true| (certified upper bound) / max |true|: %s" %
          (npt, ", ".join("%s %.1e/%.2f" % (nm, d_, s_) for nm, d_, s_ in zip(names, dev, scale))))
    print("   (the computed inputs are linear interpolants of grid differences; their error is what C2's robustness "
          "widening would have to cover, and T3 does not need it)")
    return npt > 5 and max(d_ / s_ for d_, s_ in zip(dev, scale)) < 0.2


def main():
    q = load('qsign5')
    res = {}
    res['T1'], nd = t1()
    print('T1', 'PASS' if res['T1'] else 'FAIL', flush=True)
    rstar = rstar_enclose()
    print("   R_* in [%.9f, %.9f] (intcert5 C3's bisection)" % (float(rstar.a), float(rstar.b)))
    cache = {}
    res['T3'] = t3(nd, rstar, cache)
    print('T3', 'PASS' if res['T3'] else 'FAIL', flush=True)
    bgs = {80: q.background(80), 160: q.background(160)}
    res['T2'] = t2(nd, bgs, cache)
    print('T2', 'PASS' if res['T2'] else 'FAIL', flush=True)
    res['T4'] = t4(nd, rstar)
    print('T4', 'PASS' if res['T4'] else 'FAIL', flush=True)
    return 0 if all(res.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
