#!/usr/bin/env python3
"""hf_mirror5.py -- item 498: the exact mirror-symmetric vacuum sequence for the whole round shell, constructed.

M, 498: "... that is beyond what I can compute here. - why? You have computed so much and are capable of so much
more. I absolutely believe you can do it."  Labels: computed (exact unless marked), deduced, READ, M's.  Held against
the exclusions first (481, 484): no inner or Cauchy horizon enters, and no bounce.

What is computed.  Five-dimensional vacuum, R_ab = 0, with T^2 symmetry and both reflections phi_i -> -phi_i (the
mirror allows no homogeneous squashing, hf_limit5 H6, so the solutions vary across the sphere: cohomogeneity three).
Ingoing Bondi coordinates, compactified at past null infinity:
    ds^2 = -e^{2b'} W dv^2 + 2 e^{2b'} dv dr + r^2 [ e^{-2(P1+P2)} (dth - U dv)^2 + cos^2 th e^{2 P1} dphi1^2
           + sin^2 th e^{2 P2} dphi2^2 ],   r = y^-2,  x = cos 2 th,
    P1 = y^3 (2 c^2 G - s^2 F)/3,  P2 = y^3 (2 s^2 F - c^2 G)/3,  beta = y^6 b,  x-shift V = y^5 (1 - x^2) q,
    W = 1 + y^3 w.
Every equation is regular at past null infinity (y = 0) and on both axes (x = +-1); the regularized forms are stored in
data/hf_mirror5_eqs.json.gz (hf_mirror5_derive.py regenerates them from the metric).  The incoming wave is free data
at y = 0: F = lam A env(v) h(x) sin(v/lam), G = lam A env(v) h(x) cos(v/lam), h = sqrt(2/(1 + x^2)) -- the two
polarizations a quarter turn apart, so the averaged energy (P1v^2 + P1v P2v + P2v^2) = A^2 env^2/6 is exactly round.
A seed hole of mass 1 sits inside; the slice is excised at y = 1.15 (r = 0.756), inside the horizon throughout.

  X0 (read) M's words, verbatim in the rulings file: 498.
  X1 (computed) Tangherlini is reproduced exactly: every hypersurface field and every rate vanishes.
  X2 (computed) Regular at infinity and on the axes; the radial operators have the structure Bondi's construction
     needs: beta: -12 (6 b + y b_y) (nonsingular); shift: (y^2 q'' + 3 y q' - 15 q)/16 (roots -5, 3: the y^3
     amplitude is the angular-momentum aspect); W: (3/2)(y w' - w) (the y^1 amplitude is the mass aspect).
  X3 (computed) Bondi's lemma on a generic slice: once the main equations hold, E_vx/y^3 is constant in y and, with
     the aspect rates the code determines, E_vx and E_vv vanish everywhere; the trivial equation E_vy vanishes.
  X4 (computed) Linear stability of the full scheme about the seed hole: no growing mode.
  X5 (computed) The sequence lam = 0.1, 0.05, 0.025 at A = 1, seed 1 (pinned in data/hf_mirror5_runs.json, written
     by --run): every departure from 5D Vaidya with Isaacson's mu' = (2/9) A^2 env^2 falls as lam falls.  After the shell
     the mass aspect's spread over the sphere is 2.6e-2, 2.7e-4, 1.5e-5 and its offset from mu 5.4e-3, 1.16e-3, 2.9e-4
     (second order); |W - (1 - mu y^4)| is 1.5e-2, 5.3e-3, 2.2e-3 after and 0.37, 0.18, 0.072 over the passage; the
     shift 0.20, 0.14, 0.059; P ~ lam, beta ~ lam^2.  A finer grid at lam = 0.05 agrees to 1e-5 in M.
  X6 (computed live) A short low-resolution run reproduces its pinned row; X6b it gains the predicted mass to 3 %, stays
     round to 11 % at lam = 0.1, and keeps the seed horizon.
  X7 (computed) The shell as three quarters of the final mass (seed 0.25, lam = 0.05, 0.025): spread 2.6e-3, 3.7e-4;
     offset 4.7e-3, 1.16e-3 (0.16 % of the shell); |W - W_V| over the passage 1.17, 0.52.
  Item 501 ("Continue"): what of 498's qualifications computation removes.
  X8 (computed) A fourth wavelength, lam = 0.0125 (32 x 16): every departure falls again -- spread 5.9e-6, offset 7.2e-5,
     |W - W_V| 9.6e-4 after and 0.037 over the passage, P 0.018.  P halves with lam (first order); the offset of the
     mean mass from mu quarters at each halving, 5.4e-3, 1.16e-3, 2.9e-4, 7.2e-5 (second order).
  X9 (computed) The shell as fifteen sixteenths of the final mass (seed 1/16, A = 6/sqrt 7 so that the shell brings
     15/16 and the final mass is 1; excision y = 2.2, r = 0.21, inside the seed's horizon r = 1/4): lam = 0.025,
     0.0125.  The hole grows sixteenfold about a fixed excision, so the step is held to the excision's outgoing speed
     y^3 |W|/4 (evolve's cfl); with the fixed step lam = 0.025 lost stability at v ~ 1.8.  At lam = 0.05 the excision
     is not in the high-frequency regime (lam A r^-3/2 ~ 1.2 there): it stopped being trapped at v ~ 1.25 -- the
     regime boundary, recorded.  After the shell: spread 8.8e-3, 1.0e-3; offset from mu 1.75e-3, 3.8e-4 (second order;
     0.04 % of the shell); |W - W_V| 0.72, 0.35 after and 2.55, 1.16 over the passage (|W| reaches 22 at the
     excision); the excision stays trapped (W_ex <= -0.16, -0.42).  The late spread at lam = 0.025 drifts upward after
     the shell; the scheme's near-zero modes about the final hole at this excision fall with Ny (0.023 + 0.081i,
     0.015 + 0.045i, 0.009 + 0.027i at Ny = 28, 32, 36), and the drift falls ninefold to lam = 0.0125 at Ny = 32.
  X10 (computed) The hole formed.  For the slices' round spheres, k = d_v + W/2 d_r + U d_th is the outgoing null
     normal and the area form is r^3 cos sin exactly, so 2r/3 Theta_k = W + (2/3) y^3 d_x((1 - x^2) q).  In every run
     and at every sample it has one zero per column: spheres below the least zero are trapped, above the greatest
     untrapped, and at the extremes of a marginally trapped surface r = R(x) on the slice the Laplacian's sign holds
     R between them.  The bracket closes onto Vaidya's apparent horizon sqrt(mu) at first order in lam: after the
     shell, at seed 1 its width is 6.8e-3, 3.3e-3, 1.7e-3, 8.4e-4 and its furthest point from sqrt(mu) 5.4e-3, 2.2e-3,
     9.7e-4, 4.5e-4 (lam = 0.1 to 0.0125); at seed 1/4, 2.0e-2, 1.0e-2; at seed 1/16, 1.3e-2, 6.5e-3.
  Not proved: convergence for every lam (shown over a sequence); the shell falls onto a seed; the core inside the
  horizon is excised.

python3 hf_mirror5.py [--selftest | --mutants | --run i | --merge]
"""
import sys, os, json, gzip, time, warnings
import numpy as np
import sympy as sp

warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
EQS = os.path.join(HERE, "data", "hf_mirror5_eqs.json.gz")
RUNS = os.path.join(HERE, "data", "hf_mirror5_runs.json")
RULINGS = os.path.join(HERE, "..", "M-RULINGS-2026-10-03.md")
MUT = set()
YEX = 1.15

NAMES = ["F", "F_y", "F_yy", "F_x", "F_xx", "F_xy", "F_xyy", "F_xxy", "G", "G_y", "G_yy", "G_x", "G_xx", "G_xy", "G_xyy",
         "G_xxy", "b", "b_y", "b_yy", "b_x", "b_xx", "b_xy", "q", "q_y", "q_yy", "q_yyy", "q_x", "q_xx", "q_xy", "q_xyy",
         "w", "w_y", "w_yy", "w_x", "w_xx", "w_xy", "F_vy", "G_vy", "F_v", "G_v", "F_vx", "G_vx", "F_vxx", "G_vxx",
         "w_v", "w_vy", "q_v", "q_vy", "q_vyy", "q_vyyy", "q_vx", "b_v", "b_vy", "b_vx"]


def phi1(z):
    """(e^z - 1)/z, the remainder function that makes the exponentials' cancellations at infinity exact"""
    z = np.asarray(z, dtype=float)
    small = np.abs(z) < 1e-4
    zs = np.where(small, 1.0, z)
    return np.where(small, 1 + z/2 + z*z/6 + z**3/24, np.expm1(zs)/zs)


_E = {}
def eqs():
    if not _E:
        raw = json.loads(gzip.open(EQS).read())
        ns = {k: getattr(sp, k) for k in dir(sp)}
        y, x = sp.symbols("y x", real=True)
        S = [y, x] + [sp.Symbol(n) for n in NAMES]
        lam = lambda e: sp.lambdify(S, e, modules=[{"phi1": phi1}, "numpy"], cse=True)
        for k, s in raw.items():
            e = eval(s, ns)
            _E[k] = lam(e)
            if k in LINEAR:                              # each equation is affine in its unknowns: split it once
                us = [sp.Symbol(n) for n in LINEAR[k]]
                _E[k + "_zero"] = lam(e.xreplace({u: 0 for u in us}))
                _E[k + "_lin"] = [lam(sp.diff(e, u)) for u in us]
    return _E


LINEAR = {"Eb": ["b", "b_y"], "Eq": ["q", "q_y", "q_yy"], "EW": ["w", "w_y"], "Evx": ["q_v", "q_vy"], "Evv": ["w_v", "w_vy"]}
def split(k, d):
    """the equation k at d with its unknowns set to zero, and its coefficients of them"""
    E = eqs(); a = args(d); one = np.ones_like(d["y"])
    return E[k + "_zero"](d["y"], d["x"], *a)*one, [f(d["y"], d["x"], *a)*one for f in E[k + "_lin"]]


def cheb(N):
    t = np.cos(np.pi*np.arange(N + 1)/N)
    c = np.hstack([2, np.ones(N - 1), 2])*(-1)**np.arange(N + 1)
    T = np.tile(t, (N + 1, 1)).T
    D = np.outer(c, 1/c)/(T - T.T + np.eye(N + 1))
    return D - np.diag(D.sum(axis=1)), t


class Grid:
    def __init__(s, Ny, Nx, yex=YEX):
        D, t = cheb(Ny)
        s.y = yex*(1 - t)/2                              # y[0] = 0 is past null infinity, y[-1] = yex the excision
        s.Dy = -D*2/yex
        s.Dy2 = s.Dy @ s.Dy
        s.Dy3 = s.Dy2 @ s.Dy
        M = s.Dy.copy(); M[0, :] = 0; M[0, 0] = 1
        s.Iy = np.linalg.inv(M); s.Iy[:, 0] = 0          # (Iy f)(y) = int_0^y f
        s.Dx, s.x = cheb(Nx)                             # x[0] = 1 and x[-1] = -1 are the two axes
        s.Dx2 = s.Dx @ s.Dx
        s.Y, s.X = np.meshgrid(s.y, s.x, indexing="ij")
        s.Ny, s.Nx, s.yex = Ny, Nx, yex

    def dx(s, A, k=1):
        return A @ (s.Dx if k == 1 else s.Dx2).T

    def axis_div(s, N, j0):
        """N(x)/(x - x[j0]) for the interpolant with N(x[j0]) removed: exact for polynomials (the on-shell axis zero)"""
        if "pointwise_axis" in MUT:
            return N/(s.X - s.x[j0]), N[:, j0]
        Q = np.empty_like(N)
        for j in range(s.Nx + 1):
            Q[:, j] = N @ s.Dx[j0, :] if j == j0 else (N[:, j] - N[:, j0])/(s.x[j] - s.x[j0])
        return Q, N[:, j0]


def null_solve(Lm, rhs):
    """particular solution (pseudo-inverse) and the one-dimensional null vector of a collocation operator"""
    U, S, Vt = np.linalg.svd(Lm)
    return Vt[:-1].T @ ((U[:, :-1].T @ rhs)/S[:-1]), Vt[-1]


class Data:
    """incoming data at past null infinity"""
    def __init__(s, lam, A, v1=0.5, v2=3.5, m0=1.0):
        s.lam, s.A, s.v1, s.v2, s.m0 = lam, A, v1, v2, m0

    def env(s, v, k=0):
        u = (v - s.v1)/(s.v2 - s.v1)
        if u <= 0 or u >= 1:
            return 0.0
        a, w = np.pi*u, np.pi/(s.v2 - s.v1)
        return [np.sin(a)**4, 4*np.sin(a)**3*np.cos(a)*w, (12*np.sin(a)**2*np.cos(a)**2 - 4*np.sin(a)**4)*w*w][k]

    def h(s, x):
        return np.sqrt(2/(1 + x**2))

    def FG(s, v, x, k=0):
        L, A = s.lam, s.A
        e0, e1, e2 = s.env(v), s.env(v, 1), s.env(v, 2)
        sn, cs = np.sin(v/L), np.cos(v/L)
        if "in_phase" in MUT:                            # the mutant: both polarizations in phase
            cs = sn
        if k == 0:
            f, g = L*A*e0*sn, L*A*e0*cs
        elif k == 1:
            f = A*(L*e1*sn + e0*np.cos(v/L))
            g = A*(L*e1*cs - e0*sn) if "in_phase" not in MUT else f
        else:
            f = A*(L*e2*sn + 2*e1*np.cos(v/L) - e0*sn/L)
            g = A*(L*e2*cs - 2*e1*sn - e0*cs/L) if "in_phase" not in MUT else f
        hx = s.h(x)
        return f*hx, g*hx

    def mu_pred(s, v):
        """5D Vaidya of the averaged flux: G_vv = 3 mu'/(2 r^3) = 8 pi T_vv(Isaacson) gives mu' = (2/9) A^2 env^2"""
        u = np.linspace(s.v1, min(max(v, s.v1), s.v2), 4001)
        return s.m0 + (2/9)*s.A**2*np.trapezoid(np.array([s.env(t)**2 for t in u]), u)


def args(d):
    return [d.get(n, 0.0) for n in NAMES]


def lin_coeffs(f, d, names):
    z = dict(d)
    for n in names:
        z[n] = 0.0
    s0 = f(d["y"], d["x"], *args(z))
    co = []
    for n in names:
        o = dict(z); o[n] = 1.0
        co.append(f(d["y"], d["x"], *args(o)) - s0)
    return s0, co


def slice_fields(g, st, v, data):
    """the hypersurface equations on one ingoing null slice: b, q, w from F, G and the two pinned amplitudes"""
    PF, PG, Wex, Qex = st
    E = eqs()
    F0, G0 = data.FG(v, g.x)
    d = {"y": g.Y, "x": g.X}
    for nm, A0, PA in (("F", F0, PF), ("G", G0, PG)):
        A = A0[None, :] + g.Iy @ PA
        d[nm] = A; d[nm + "_y"] = PA; d[nm + "_yy"] = g.Dy @ PA
        d[nm + "_x"] = g.dx(A); d[nm + "_xx"] = g.dx(A, 2); d[nm + "_xy"] = g.dx(PA)
        d[nm + "_xyy"] = g.dx(d[nm + "_yy"]); d[nm + "_xxy"] = g.dx(PA, 2)
    Z = np.zeros_like(g.Y)
    s0, (cb, cby) = split("Eb", d)
    b = np.empty_like(Z)
    for j in range(g.Nx + 1):
        b[:, j] = np.linalg.solve(np.diag(cb[:, j]) + np.diag(cby[:, j]) @ g.Dy, -s0[:, j])
    d.update(b=b, b_y=g.Dy @ b); d["b_yy"] = g.Dy @ d["b_y"]
    d["b_x"] = g.dx(b); d["b_xx"] = g.dx(b, 2); d["b_xy"] = g.dx(d["b_y"])
    s0, (c0, c1, c2) = split("Eq", d)
    q = np.empty_like(Z); qh = np.empty_like(Z)
    for j in range(g.Nx + 1):
        Lm = np.diag(c0[:, j]) + np.diag(c1[:, j]) @ g.Dy + np.diag(c2[:, j]) @ g.Dy2
        if "spike" in MUT:                               # the mutant: the y^3 amplitude imposed by a third derivative
            A_ = np.vstack([Lm, 1e4*g.Dy3[0, :]/6]); b_ = np.concatenate([-s0[:, j], [1e4*Qex[j]]])
            q[:, j] = np.linalg.lstsq(A_, b_, rcond=None)[0]; qh[:, j] = g.y**3
            continue
        qp, hn = null_solve(Lm, -s0[:, j])
        hn = hn/hn[-1]
        q[:, j] = qp + (Qex[j] - qp[-1])*hn; qh[:, j] = hn
    d["q"] = q; d["q_y"] = g.Dy @ q; d["q_yy"] = g.Dy @ d["q_y"]; d["q_yyy"] = g.Dy @ d["q_yy"]
    d["q_x"] = g.dx(q); d["q_xx"] = g.dx(q, 2); d["q_xy"] = g.dx(d["q_y"]); d["q_xyy"] = g.dx(d["q_yy"])
    s0, (cw, cwy) = split("EW", d)
    w = np.empty_like(Z); wh = np.empty_like(Z)
    for j in range(g.Nx + 1):
        wp, hn = null_solve(np.diag(cw[:, j]) + np.diag(cwy[:, j]) @ g.Dy, -s0[:, j])
        hn = hn/hn[-1]
        w[:, j] = wp + (Wex[j] - wp[-1])*hn; wh[:, j] = hn
    d["w"] = w; d["w_y"] = g.Dy @ w; d["w_yy"] = g.Dy @ d["w_y"]
    d["w_x"] = g.dx(w); d["w_xx"] = g.dx(w, 2); d["w_xy"] = g.dx(d["w_y"])
    d["qh"], d["wh"] = qh, wh
    return d


def evolve_rhs(g, d):
    """the evolution equations: (A1 + 2 A2) and (2 A1 + A2) are regular after exact division by (x -+ 1)"""
    E = eqs(); a = args(d); out = []
    for k, j0 in (("EFn", 0), ("EGn", g.Nx)):
        ct = E[k + "_c"](d["y"], d["x"], *a)*np.ones_like(g.Y)
        Q, res0 = g.axis_div(E[k + "_r"](d["y"], d["x"], *a)*np.ones_like(g.Y), j0)
        out.append((-Q/ct, res0))
    return out


VDER = {"F": ["F", "F_x", "F_y", "F_xx"], "G": ["G", "G_x", "G_y", "G_xx"], "b": ["b", "b_y", "b_x"],
        "q": ["q", "q_y", "q_yy", "q_yyy", "q_x"], "w": ["w", "w_y"]}
def with_vders(dm, d0, dp, h):
    d = dict(d0)
    for base, names in VDER.items():
        for n in names:
            tail = n.split("_")[1] if "_" in n else ""
            d[base + "_" + "".join(sorted("v" + tail))] = (dp[n] - dm[n])/(2*h)
    return d


def aspect_rates(g, st, v, data, d0, Fv, Gv, h=1e-5, ycut=0.35):
    """rates of the two pinned amplitudes from E_vx = 0 and E_vv = 0 in the interior.  By Bondi's lemma these are the
    conservation laws at past null infinity; no high derivative at infinity is needed."""
    E = eqs()
    rows = np.where(g.y >= ycut*g.yex)[0]
    zero = np.zeros(g.Nx + 1)
    def vfields(k):
        dm = slice_fields(g, [a - h*b for a, b in zip(st, k)], v - h, data)
        dp = slice_fields(g, [a + h*b for a, b in zip(st, k)], v + h, data)
        return with_vders(dm, d0, dp, h)
    dd = vfields([Fv, Gv, zero, zero])
    R0, (aq, aqy) = split("Evx", dd)
    R0 = R0 + aq*dd["q_v"] + aqy*dd["q_vy"]
    Rh = aq*d0["qh"] + aqy*(g.Dy @ d0["qh"])
    Qv = -np.sum(R0[rows]*Rh[rows], axis=0)/np.sum(Rh[rows]**2, axis=0)
    resx = np.abs(R0[rows] + Qv*Rh[rows]).max()
    dd2 = vfields([Fv, Gv, zero, Qv])
    D0, (aw, awy) = split("Evv", dd2)
    D0 = D0 + aw*dd2["w_v"] + awy*dd2["w_vy"]
    Dh = aw*d0["wh"] + awy*(g.Dy @ d0["wh"])
    Wv = -np.sum(D0[rows]*Dh[rows], axis=0)/np.sum(Dh[rows]**2, axis=0)
    resv = np.abs(D0[rows] + Wv*Dh[rows]).max()
    if "no_mass_law" in MUT:
        Wv = 0*Wv
    return Wv, Qv, dict(resx=resx, resv=resv)


def rhs(g, st, v, data):
    d = slice_fields(g, st, v, data)
    (Fv, rF), (Gv, rG) = evolve_rhs(g, d)
    Wv, Qv, info = aspect_rates(g, st, v, data, d, Fv, Gv)
    d["info"], d["axis"] = info, max(np.abs(rF).max(), np.abs(rG).max())
    return [Fv, Gv, Wv, Qv], d


def filters(g, drop=2, alpha=36.0, p=32):
    """drop the top two Chebyshev modes in x; a gentle exponential filter in y (modes below 0.8 N untouched to 3 %)"""
    T = np.cos(np.outer(np.arccos(np.clip(g.x, -1, 1)), np.arange(g.Nx + 1)))
    s = np.ones(g.Nx + 1); s[g.Nx + 1 - drop:] = 0
    Fx = T @ np.diag(s) @ np.linalg.inv(T)
    t = 1 - 2*g.y/g.yex
    Ty = np.cos(np.outer(np.arccos(np.clip(t, -1, 1)), np.arange(g.Ny + 1)))
    Fy = Ty @ np.diag(np.exp(-alpha*(np.arange(g.Ny + 1)/g.Ny)**p)) @ np.linalg.inv(Ty)
    return (lambda A: Fy @ A @ Fx.T), (lambda a: Fx @ a)


def horizon(g, d):
    """the round spheres' outgoing expansion, 2r/3 Theta_k = W + (2/3) y^3 d_x((1 - x^2) q), with k = d_v + W/2 d_r + U d_theta
    (the area form is r^3 cos sin exactly); its zero in each column.  Where Theta_k < 0 in every column the sphere is trapped;
    at the extremes of a MOTS r = R(x) on the slice the Laplacian's sign puts R between the least and greatest zero"""
    T = 1 + g.Y**3*d["w"] + (0 if "horizon_w_only" in MUT else (2/3)*g.Y**3*g.dx((1 - g.X**2)*d["q"]))
    t, tt = np.cos(np.pi*np.arange(g.Ny + 1)/g.Ny), np.linspace(-1, 1, 4001)
    r, n = [], 0
    for j in range(g.Nx + 1):
        c = np.polynomial.chebyshev.chebfit(t, T[:, j], g.Ny); c1 = np.polynomial.chebyshev.chebder(c)
        f = np.polynomial.chebyshev.chebval(tt, c)
        i = np.nonzero(np.sign(f[1:]) != np.sign(f[:-1]))[0]
        n = max(n, len(i))
        if len(i):
            k = i[0]; t0 = tt[k] - f[k]*(tt[k + 1] - tt[k])/(f[k + 1] - f[k])
            for _ in range(3):
                t0 -= np.polynomial.chebyshev.chebval(t0, c)/np.polynomial.chebyshev.chebval(t0, c1)
            r.append((g.yex*(1 - t0)/2)**-2)
    return (min(r), max(r), n) if len(r) == g.Nx + 1 else (np.nan, np.nan, n)


def diag(g, st, d, v, data):
    W = 1 + g.Y**3*d["w"]
    r_lo, r_hi, nz = horizon(g, d)
    Mas = -d["w_y"][0]                                   # the mass aspect at past null infinity
    mu = data.mu_pred(v)
    return dict(v=round(v, 6), M_min=float(Mas.min()), M_max=float(Mas.max()), M_mean=float(Mas.mean()), mu=float(mu),
                dW=float(np.abs(W - (1 - mu*g.Y**4)).max()), P=float(max(np.abs(d["F"]).max(), np.abs(d["G"]).max())),
                b=float(np.abs(d["b"]).max()), q=float(np.abs(d["q"]).max()), W_ex=float(W[-1].max()),
                axis=float(d["axis"]), resx=float(d["info"]["resx"]), resv=float(d["info"]["resv"]),
                r_lo=float(r_lo), r_hi=float(r_hi), nz=int(nz))


def evolve(lam, A, Ny, Nx, m0=1.0, yex=YEX, cfl=None, v_end=4.5, dvf=0.125, every=0.25, log=None):
    """RK4 at dv = lam dvf; with cfl, dv is also held to cfl x (the end spacing in y)/(the excision's outgoing speed
    y^3 |W|/4) and lands on every sample time -- a deep excision in a growing hole is otherwise stiff"""
    g = Grid(Ny, Nx, yex); data = Data(lam, A, m0=m0); fb, fa = filters(g)
    dv = dv0 = lam*dvf
    Z = np.zeros((Ny + 1, Nx + 1))
    st = [Z.copy(), Z.copy(), np.full(Nx + 1, -m0*yex), np.zeros(Nx + 1)]   # seed: W = 1 - m0 y^4, U = 0
    v, hist, nxt = 0.0, [], 0.0
    for i in range(10**7):
        k1, d = rhs(g, st, v, data)
        if v >= nxt - 1e-9:
            hist.append(diag(g, st, d, v, data)); nxt += every
            if log: log(hist[-1])
        if (cfl is None and i == int(round(v_end/dv0))) or (cfl is not None and v >= v_end - 1e-9):
            break
        if cfl is not None:
            speed = max(1.0, yex**3*np.abs(1 + yex**3*st[2]).max()/4)
            dv = min(dv0, cfl*(g.y[1] - g.y[0])/speed, nxt - v)
        s2 = [a + 0.5*dv*b for a, b in zip(st, k1)]; k2 = rhs(g, s2, v + dv/2, data)[0]
        s3 = [a + 0.5*dv*b for a, b in zip(st, k2)]; k3 = rhs(g, s3, v + dv/2, data)[0]
        s4 = [a + dv*b for a, b in zip(st, k3)]; k4 = rhs(g, s4, v + dv, data)[0]
        st = [a + dv/6*(b1 + 2*b2 + 2*b3 + b4) for a, b1, b2, b3, b4 in zip(st, k1, k2, k3, k4)]
        st = [fb(st[0]), fb(st[1]), fa(st[2]), fa(st[3])]
        v += dv
        if not np.all(np.isfinite(st[0])) or np.abs(st[3]).max() > 1e3:
            raise FloatingPointError("blew up at v = %.3f" % v)
    return hist


SEQUENCE = [(0.1, 1.0, 20, 16), (0.05, 1.0, 24, 16), (0.025, 1.0, 28, 16), (0.05, 1.0, 32, 20)]
LIVE = (0.1, 1.0, 16, 10)
SMALL_SEED = [(0.05, 2.0, 24, 16, 0.25, 1.6), (0.025, 2.0, 28, 16, 0.25, 1.6)]    # the shell is 3/4 of the final mass
FOURTH = (0.0125, 1.0, 32, 16)                                                      # item 501: a fourth wavelength
A16 = 6/np.sqrt(7)                                    # (2/9) A^2 x 3 x 35/128 = 15/16: the shell is 15/16 of the final mass 1
SEED16 = [(0.025, A16, 28, 16, 1/16, 2.2, 2.0), (0.0125, A16, 32, 16, 1/16, 2.2, 2.0)]   # the 7th entry: cfl
ALL = SEQUENCE + [LIVE] + SMALL_SEED + [FOURTH] + SEED16
key = lambda cfg: "_".join("%g" % c_ for c_ in cfg)


def run_one(i):
    """one row of the pinned sequence (--run i; i = 4 is the live row); about an hour for the finest"""
    cfg = ALL[i]
    t0 = time.time()
    hist = evolve(*cfg, log=lambda h: print(h, flush=True))
    json.dump({key(cfg): hist}, open(RUNS.replace(".json", "_%d.json" % i), "w"))
    print(cfg, "%.0fs" % (time.time() - t0), flush=True)


def merge():
    out = json.load(open(RUNS)) if os.path.exists(RUNS) else {}
    for i in range(len(ALL)):
        f = RUNS.replace(".json", "_%d.json" % i)
        if os.path.exists(f):
            out.update(json.load(open(f)))
    json.dump(out, open(RUNS, "w"), indent=1)


def words():
    s = open(RULINGS).read()
    return "498. **Construct the mirror-symmetric sequence" in s and "I absolutely believe you can do it." in s


def x1():
    g = Grid(20, 8); data = Data(0.1, 0.0)
    Z = np.zeros_like(g.Y); st = [Z, Z, np.full(9, -YEX), np.zeros(9)]
    k, d = rhs(g, st, 1.0, data)
    return dict(w_err=float(np.abs(d["w"] + g.Y).max()), q=float(np.abs(d["q"]).max()), b=float(np.abs(d["b"]).max()),
                rates=float(max(np.abs(a).max() for a in k)), M=float(-d["w_y"][0].mean()))


def test_slice(g):
    Y, X = g.Y, g.X
    PF = 0.02*np.sin(2*Y)*(1 + 0.3*X); PG = 0.015*Y**2*(1 - 0.2*X**2)
    return [PF, PG, -YEX*(1 + 0.01*np.cos(np.pi*g.x)), 0.003*(1 - g.x**2)], Data(0.3, 0.3, 0.0, 6.0), 1.7


def x2():
    g = Grid(20, 10); st, data, v = test_slice(g); E = eqs()
    d = slice_fields(g, st, v, data)
    finite = all(np.all(np.isfinite(E[k](d["y"], d["x"], *args(d)))) for k in E if callable(E[k]))
    yv, xv = 1e-3, 0.2
    def co(k, names):
        dd = {n: 0.1 for n in NAMES}; dd.update(y=yv, x=xv)
        return lin_coeffs(E[k], dd, names)[1]
    cb, cby = co("Eb", ["b", "b_y"]); c0, c1, c2 = co("Eq", ["q", "q_y", "q_yy"]); cw, cwy = co("EW", ["w", "w_y"])
    return dict(finite=bool(finite), beta=(float(cb), float(cby/yv)), shift=(float(16*c2/yv**2), float(16*c1/yv), float(16*c0)),
                W=(float(cwy/yv), float(cw)))


def x3():
    g = Grid(24, 24); st, data, v = test_slice(g); E = eqs()
    d0 = slice_fields(g, st, v, data); (Fv, _), (Gv, _) = evolve_rhs(g, d0)
    Wv, Qv, info = aspect_rates(g, st, v, data, d0, Fv, Gv)
    h = 1e-5; k = [Fv, Gv, Wv, Qv]
    dm = slice_fields(g, [a - h*b for a, b in zip(st, k)], v - h, data)
    dp = slice_fields(g, [a + h*b for a, b in zip(st, k)], v + h, data)
    dd = with_vders(dm, d0, dp, h)
    Rx = E["Evx"](dd["y"], dd["x"], *args(dd))*np.ones_like(g.Y)
    Rv = E["Evv"](dd["y"], dd["x"], *args(dd))*np.ones_like(g.Y)
    Ry = E["Evy"](dd["y"], dd["x"], *args(dd))*np.ones_like(g.Y)
    k0 = [Fv, Gv, 0*Wv, 0*Qv]                            # without the rates: E_vx/y^3 is still constant in y
    dm0 = slice_fields(g, [a - h*b for a, b in zip(st, k0)], v - h, data)
    dp0 = slice_fields(g, [a + h*b for a, b in zip(st, k0)], v + h, data)
    d00 = with_vders(dm0, d0, dp0, h)
    R0 = E["Evx"](d00["y"], d00["x"], *args(d00))*np.ones_like(g.Y)
    C = R0[g.Ny//3:]/g.Y[g.Ny//3:]**3
    scale = max(np.abs(E[k](dd["y"], dd["x"], *args(dd))).max() for k in ("Eb",)) + np.abs(R0).max()
    return dict(bondi_spread=float(np.abs(C - C[-1]).max()/np.abs(C).max()), C=float(np.abs(C).max()),
                Evx=float(np.abs(Rx).max()), Evv=float(np.abs(Rv).max()), Evy=float(np.abs(Ry).max()),
                Evx_off=float(np.abs(R0).max()), resx=float(info["resx"]), resv=float(info["resv"]), scale=float(scale))


def x4(Ny=12, Nx=6):
    g = Grid(Ny, Nx); data = Data(0.1, 0.0); fb, fa = filters(g)
    sh = (Ny + 1, Nx + 1); n1 = sh[0]*sh[1]; n = Nx + 1
    def unflat(z): return [z[:n1].reshape(sh), z[n1:2*n1].reshape(sh), z[2*n1:2*n1 + n], z[2*n1 + n:]]
    def R(z):
        st = unflat(z); st = [fb(st[0]), fb(st[1]), fa(st[2]), fa(st[3])]
        k = rhs(g, st, 1.0, data)[0]
        return np.concatenate([fb(k[0]).ravel(), fb(k[1]).ravel(), fa(k[2]), fa(k[3])])
    z0 = np.concatenate([np.zeros(2*n1), -YEX*np.ones(n), np.zeros(n)]); f0 = R(z0)
    J = np.empty((z0.size, z0.size))
    for k in range(z0.size):
        z = z0.copy(); z[k] += 1e-6; J[:, k] = (R(z) - f0)/1e-6
    ev = np.linalg.eigvals(J)
    return dict(max_re=float(ev.real.max()), max_abs=float(np.abs(ev).max()))


def end_stats(hist, v_after=3.75):
    late = [h for h in hist if h["v"] >= v_after - 1e-9]
    return dict(spread=max(h["M_max"] - h["M_min"] for h in late), offset=max(abs(h["M_mean"] - h["mu"]) for h in late),
                dW=max(h["dW"] for h in late), dW_all=max(h["dW"] for h in hist), q_all=max(h["q"] for h in hist),
                P=max(h["P"] for h in hist), b=max(h["b"] for h in hist),
                q_late=max(h["q"] for h in late), W_ex=max(h["W_ex"] for h in hist), mu=late[-1]["mu"],
                M_end=late[-1]["M_mean"], resx=max(h["resx"] for h in hist), resv=max(h["resv"] for h in hist),
                r_lo=late[-1]["r_lo"], r_hi=late[-1]["r_hi"], nz=max(h["nz"] for h in hist), nz_min=min(h["nz"] for h in hist),
                dr=max(max(abs(h["r_lo"] - h["mu"]**0.5), abs(h["r_hi"] - h["mu"]**0.5)) for h in late),
                width=max(h["r_hi"] - h["r_lo"] for h in late),
                inside=all(h["r_lo"] <= h["mu"]**0.5 <= h["r_hi"] for h in late))


def x5():
    R = json.load(open(RUNS))
    st = {k: end_stats(v) for k, v in R.items()}
    return st


def x6():
    hist = evolve(*LIVE)
    pinned = json.load(open(RUNS)).get(key(LIVE))
    return dict(stats=end_stats(hist), match=(max(abs(a["M_mean"] - b["M_mean"]) + abs(a["dW"] - b["dW"])
                                                 + abs(a["r_lo"] - b["r_lo"]) + abs(a["r_hi"] - b["r_hi"])
                                                 for a, b in zip(hist, pinned)) if pinned else None))


def compute(live=True):
    o = dict(words=words(), x1=x1(), x2=x2(), x3=x3(), x4=x4(), x5=x5())
    if live:
        o["x6"] = x6()
    return o


def checks(o):
    c = {}
    c["X0 words of 498"] = o["words"]
    a = o["x1"]
    c["X1 Tangherlini exact"] = a["w_err"] < 1e-11 and a["q"] < 1e-12 and a["b"] < 1e-12 and a["rates"] < 1e-8 and abs(a["M"] - 1) < 1e-11
    a = o["x2"]
    c["X2 regular; radial structure"] = (a["finite"] and np.allclose(a["beta"], (-72, -12), atol=1e-6)
                                         and np.allclose(a["shift"], (1, 3, -15), atol=1e-3) and np.allclose(a["W"], (1.5, -1.5), atol=1e-3))
    a = o["x3"]
    c["X3 Bondi's lemma; constraints vanish"] = (a["bondi_spread"] < 1e-5 and a["C"] > 1e-2 and a["Evx"] < 1e-6*a["scale"]
                                                  and a["Evv"] < 1e-5*a["scale"] and a["Evy"] < 1e-6*a["scale"])
    a = o["x4"]
    c["X4 no growing mode"] = a["max_re"] < 0.05
    s = o["x5"]
    k1, k2, k3, kh = [key(c_) for c_ in SEQUENCE]
    falls = all(s[k1][q] > s[k2][q] > s[k3][q] for q in ("spread", "offset", "dW", "dW_all", "q_all", "P", "b"))
    c["X5 the sequence converges to 5D Vaidya"] = (falls and s[k3]["spread"] < 0.25*s[k1]["spread"]
                                                   and s[k3]["dW"] < 0.25*s[k1]["dW"] and s[k3]["P"] < 0.4*s[k1]["P"]
                                                   and max(s[k]["W_ex"] for k in s) < 0
                                                   and abs(s[kh]["M_end"] - s[k2]["M_end"]) < 0.5*s[k2]["offset"] + 1e-4)
    a5, a6 = s[key(SMALL_SEED[0])], s[key(SMALL_SEED[1])]
    c["X7 the shell as three quarters of the mass"] = (all(a5[q] > a6[q] for q in ("spread", "offset", "dW", "dW_all", "P", "b"))
                                                        and a6["W_ex"] < 0 and a6["offset"] < 0.01*(a6["mu"] - 0.25)
                                                        and a6["spread"] < 0.01*(a6["mu"] - 0.25))
    k4 = key(FOURTH)
    c["X8 a fourth wavelength: the fall goes on, the mass at second order"] = (
        all(s[k3][q] > s[k4][q] for q in ("spread", "offset", "dW", "dW_all", "q_all", "P", "b"))
        and all(0.4 < s[b_]["P"]/s[a_]["P"] < 0.6 for a_, b_ in ((k2, k3), (k3, k4)))            # the amplitude ~ lambda
        and all(s[b_]["offset"] < 0.3*s[a_]["offset"] for a_, b_ in ((k1, k2), (k2, k3), (k3, k4)))   # ~ lambda^2
        and s[k4]["W_ex"] < 0)
    b5, b6 = s[key(SEED16[0])], s[key(SEED16[1])]
    c["X9 the shell as fifteen sixteenths of the mass"] = (all(b5[q] > b6[q] for q in ("spread", "offset", "dW", "dW_all", "P", "b"))
                                                          and b6["W_ex"] < 0 and b6["offset"] < 0.01*(b6["mu"] - 1/16)
                                                          and b6["spread"] < 0.01*(b6["mu"] - 1/16))
    fam = [[key(c_) for c_ in SEQUENCE[:3] + [FOURTH]], [key(c_) for c_ in SMALL_SEED], [key(c_) for c_ in SEED16]]
    c["X10 the hole formed: one zero per column, its horizon onto Vaidya's sqrt(mu) at first order"] = (
        all(t["nz_min"] == t["nz"] == 1 for t in s.values())
        and all(s[b_]["dr"] < 0.6*s[a_]["dr"] and s[b_]["width"] < 0.6*s[a_]["width"] for f in fam for a_, b_ in zip(f, f[1:]))
        and s[k4]["dr"] < 1e-3*s[k4]["mu"]**0.5 and s[k4]["inside"])
    if "x6" in o:
        a = o["x6"]
        c["X6 live row reproduces its pinned row"] = a["match"] is not None and a["match"] < 1e-8
        c["X6b live row: mass gained, round, horizon kept"] = (abs(a["stats"]["M_end"] - a["stats"]["mu"]) < 0.1*(a["stats"]["mu"] - 1)
                                                               and a["stats"]["spread"] < 0.3*(a["stats"]["mu"] - 1)
                                                               and a["stats"]["W_ex"] < 0)
    return c


def report(o=None):
    o = o or compute()
    for k, v in checks(o).items():
        print("%-50s %s" % (k, "PASS" if v else "FAIL"))
    s = o["x5"]
    for k in sorted(s, key=lambda k: (-float(k.split("_")[0]), k)):
        t = s[k]
        print("  run %-16s spread %.2e  offset %.2e  |W-W_V| %.2e  max P %.2e  max b %.2e  M_end %.5f  mu %.5f" %
              (k, t["spread"], t["offset"], t["dW"], t["P"], t["b"], t["M_end"], t["mu"]))
    return o


MUTANTS = {"spike": "the y^3 amplitude imposed by a third derivative at infinity (X4: a growing mode)",
           "pointwise_axis": "the axis division done pointwise instead of exactly (X1)",
           "no_mass_law": "the mass aspect's rate set to zero (X6b: no mass gained)",
           "in_phase": "the two polarizations in phase: the averaged energy is not round (X6b)",
           "horizon_w_only": "the spheres' expansion read from W alone, the shift's divergence dropped (X6: the pinned horizon)"}


def selftest(quiet=False):
    o = compute()
    c = checks(o)
    if not quiet:
        report(o)
    print("%s: %d/%d" % (os.path.basename(__file__), sum(c.values()), len(c)))
    return all(c.values())


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            c = checks(compute(live=m_ in ("no_mass_law", "in_phase", "horizon_w_only")))
            failed = [k for k, v in c.items() if not v]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-16s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--run" in sys.argv:
        run_one(int(sys.argv[sys.argv.index("--run") + 1])); sys.exit(0)
    if "--merge" in sys.argv:
        merge(); sys.exit(0)
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
