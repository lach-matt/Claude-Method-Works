#!/usr/bin/env python3
"""corridor_p2.py -- item 455, the corridor's second rung P2 (BOUNCE-RESEARCH section 22): one charged hole on the plane.
M: "1 - yes, likely (iii)" -- the bulk U(1) of 446 (1) with a field term on the plane, -(lam/16 pi G5) F^2 (Dvali,
Gabadadze and Shifman hep-th/0010071, READ), lam a parameter from lam = 0.  The hole is Figueras and Wiseman's localized
Randall-Sundrum hole (1105.2558, READ) in their chart (9), Lorentzian static, ell = 1, X = r, u = x:
  ds^2 = (1/Delta^2)[-r^2 T dt^2 + 4A dr^2/f^4 + 4B dx^2/(f^2 g) + 2 r x F dr dx/f^3 + x^2 g S dOmega^2/f^2],
  f = 1 - r^2, g = 2 - x^2, Delta = (f + bt (1 - x^2))/(bt f),
with the bulk potential A_t = P(r, x).  Rows (Figueras, Lucietti and Wiseman 1104.4489 section 4, READ): the horizon
r = 0 smooth in r^2 with T = A, P = 0; the axis x = 0 smooth in x^2 with S = B; the Poincare horizon r = 1 at the
reference, P = mu; the plane x = 1 Israel's three conditions with the field term (Kaus and Reall's stress with lam),
xi^x = 0, F = 0, and the Maxwell jump P_x = (lam/2) sqrt(g_xx) g_tt D_i F^it.  Einstein-DeTurck-Maxwell by
deturck2d.py (seated), Chebyshev collocation, Newton with the complex-step Jacobian.  Labels: READ (quoted), computed,
deduced, estimate.  Worked in the conversation; not verified; not seated.  2026-10-17.

  Q0 (read) M's words: 455.
  Q1 (computed) The bulk field: on 5D Reissner-Nordstrom-AdS with A_t = kappa q/r^2 the Maxwell equation holds and
     every Einstein-DeTurck component is proportional to 4 kappa^2 - 3, so kappa = sqrt(3)/2 (446 (1)'s normalisation).
  Q2 (computed) The chart: every boundary row vanishes on the reference metric (T = A = B = S = 1, F = 0, P = 0) at
     sample points, the plane's three Israel rows exactly.  Its horizon has kappa_t = 1/2, so the period is 4 pi bt
     on the plane's far region: beta = 4 pi bt ell, as Figueras and Wiseman state (READ).  [Their footnote's
     "T = 4A" belongs to a time rescaled by ell bt; with (9) as printed and this reference the row is T = A.]
  Q3 (computed) Their hole: uncharged, bt = 1, R4 = bt sqrt(S(0, 1)) = 1.130 at N = 12 against their R4/ell = 1.13
     (READ, Fig. 4).  Off the selftest, N = 16 and 20 give 1.1293 and 1.1288, and bt = 5 gives 5.037 against 5.04.
  Q4 (computed) Einstein, not a soliton: xi^2 off the fictitious boundaries falls from N = 10 to N = 12.
  Q5 (computed) The soft direction: the smallest row-equilibrated singular value is isolated, over 30 times below the
     next, and its rows are the plane's Israel rows at the far corner -- the near-null direction the record's own
     solver carries (items 406-407, about N^-4.8).  It moves R4 by about 0.3% between resolutions; A_H/R4^2 holds
     to 2e-4.
  Q6 (computed) The charged hole at lam = 0 (bt = 1, mu to 0.06): Newton converges, the electric flux through every
     interior row agrees to 1%, and the hole shrinks at fixed temperature.
  Q7 (computed) The far tail: approaching r = 1 on the plane, (mu - P)/f is fitted by a/(c + ln 1/f) better than
     by a + b f (3 times at N = 12; 5 to 8 times at N = 20, section 22), with a in proportion to mu -- the field
     does not reach the Poincare horizon at a power, as Figueras, Lucietti and Wiseman's smooth condition
     X = 1 + (1 - r) X1 requires (READ (4.11)).
  Q8 (computed) A field term: at lam = 1 the total charge, the bulk flux plus the plane's share 4 pi lam B, is the same
     through every interior row to 1%, while the bulk flux alone moves by more than 10%.
  Q9 (computed) The lam = 0 family at bt = 2 turns at mu_max = 0.145 at N = 12 by pseudo-arclength; recorded from
     --family, 0.166 at N = 16 and above 0.1675 at N = 20.  The turn moves with resolution: not a result.
  Q10 (computed) The plane's field: at lam = 64 (the bulk's share of the field energy about 1/lam, an estimate) the
     potential on the plane is four-dimensional Coulomb, P = mu (1 - R4/rho) to 2%, and the charge shrinks the hole
     at fixed temperature by most of Reissner-Nordstrom's amount, (1 - R4/R4(0))/mu_phys^2 between 0.6 and 1.
     Physical units: on the plane's far region g_tt -> -bt^2, so t_phys = bt t, T = 1/(4 pi bt) and
     mu_phys = mu/bt; with mt = sqrt(lam) mu_phys the 4D charge over the radius, Reissner-Nordstrom at fixed T gives
     R4/R4(0) = 1 - mt^2.  Off the selftest (N = 16): 0.59, 0.75, 0.85, 0.98, 1.06, 1.07 of it at
     R4 = 1.13, 1.61, 2.10, 3.08, 4.06, 4.59 -- four-dimensional from R4 ~ 3 ell, the excess the bulk's own share
     of the coupling (estimate).
  Q11 (deduced) The reading: with the bulk U(1) alone the computed family stays far from extremality (4 pi T R4 from
     1.05 to 1.01 at mu_phys <= 0.07, N = 16 and 20 within 0.2%), and beyond that the chart cannot follow it: the
     bulk U(1)'s zero mode is not localized (Pomarol, READ; u1_bulk's running coupling, 446), its field falls as
     1/(D ln D), and the chart's Poincare-horizon rows assume a power.  With the field held on the plane (lam = 64)
     the family follows Reissner-Nordstrom toward extremality; N = 16 and 20 agree within 0.5% down to
     4 pi T R4 = 0.89 (mt = 0.84) and part beyond it: extremality is approached, not reached, at N <= 20.

python3 corridor_p2.py [--selftest | --mutants | --family]
"""
import os
import re
import sys
import time
import warnings
import importlib.util

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ("1 - yes, likely (iii)",)
FW_R4 = {1.0: 1.13, 5.0: 5.04}                       # Figueras and Wiseman, R4/ell (READ, Fig. 4 and text)
FAMILY_RECORD = {12: 0.1450, 16: 0.16609, 20: 0.16751}   # mu at the turn (20: still rising when stopped), --family

_spec = importlib.util.spec_from_file_location("p2_dt", os.path.join(HERE, "deturck2d.py"))
DT = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(DT)
X, u, th = DT.X, DT.u, DT.th
FUNCS = ["T", "A", "B", "F", "S", "P"]
COMPS = ((0, 0), (1, 1), (2, 2), (1, 2), (3, 3))
bt, mu, lam = sp.symbols("bt mu lam", positive=True)
warnings.simplefilter("ignore")


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def maxwell_parts(g, gi, D, PX, Pu, comps):
    """F = dA with A = P dt: 2(F F - g F^2/6) on comps (the trace-reversed Biggs-Santos source) and the Maxwell
    scalar d_i(W F^it)/W, W = sqrt(-g) without sin(theta)"""
    F = sp.zeros(5)
    F[1, 0], F[0, 1] = PX, -PX
    F[2, 0], F[0, 2] = Pu, -Pu
    Fup = gi * F * gi
    F2 = sum(F[a, b] * Fup[a, b] for a in range(5) for b in range(5))
    FF = F * gi * F.T
    src = {ab: (0 if "src_off" in MUT else 2 * (FF[ab] - g[ab] * F2 / 6)) for ab in comps}
    W = sp.sqrt(-g[0, 0] * (g[1, 1] * g[2, 2] - g[1, 2]**2)) * g[3, 3]
    if "flat_maxwell" in MUT:
        mx = D(PX, 1) + D(Pu, 2)
    else:
        mx = (D(W * Fup[1, 0], 1) + D(W * Fup[2, 0], 2)) / W
    return src, F2, mx


def fw_metric(J, ref=False):
    """Figueras and Wiseman's chart (1105.2558 (9)), Lorentzian static, ell = 1: X is their r, u their x"""
    T, A, B, F, S = [sp.Integer(1) if ref else J[n] for n in "TABFS"]
    if ref:
        F = sp.Integer(0)
    f, gx = 1 - X**2, 2 - u**2
    w = 1 / ((f + bt * (1 - u**2)) / (bt * f))**2
    g = sp.zeros(5)
    g[0, 0] = -w * X**2 * T
    g[1, 1] = w * 4 * A / f**4
    g[2, 2] = w * 4 * B / (f**2 * gx)
    g[1, 2] = g[2, 1] = w * X * u * F / f**3
    g[3, 3] = w * u**2 * gx * S / f**2
    g[4, 4] = g[3, 3] * sp.sin(th)**2
    return g


def system():
    """the interior rows, the boundary rows by region, and the diagnostics' integrands, symbolically"""
    J = DT.jetsyms(FUNCS)
    g, gb = fw_metric(J), fw_metric(J, ref=True)
    E, xi_up, J = DT.operator(g, gb, FUNCS, COMPS, Lam=4)
    gi = DT.inverse(g)
    D = DT.make_D(FUNCS, J)
    src, F2, mx = maxwell_parts(g, gi, D, J["P_X"], J["P_u"], COMPS)
    inner = [(E[(0, 0)] - src[(0, 0)]) / g[0, 0], (E[(1, 1)] - src[(1, 1)]) / g[1, 1],
             (E[(2, 2)] - src[(2, 2)]) / g[2, 2], (E[(1, 2)] - src[(1, 2)]) / sp.sqrt(g[1, 1] * g[2, 2]),
             (E[(3, 3)] - src[(3, 3)]) / g[3, 3], mx * (-g[0, 0])]
    T, A, B, F, S, P = [J[n] for n in FUNCS]
    jt = lambda n, d: J[n + d]
    nu_ = 1 / sp.sqrt(g[2, 2])
    K = {k: sp.Rational(1, 2) * nu_ * D(g[k], 2) for k in ((0, 0), (1, 1), (3, 3))}
    E2 = -J["P_X"]**2 / (g[0, 0] * g[1, 1])                 # the orthonormal field squared on the plane
    s = -1 if "israel_sign" in MUT else 1
    israel = [K[(0, 0)] / g[0, 0] - s + lam * E2 / 2, K[(1, 1)] / g[1, 1] - s + lam * E2 / 2,
              K[(3, 3)] / g[3, 3] - s - lam * E2 / 2]
    sqh = sp.sqrt(-g[0, 0] * g[1, 1]) * g[3, 3]
    div4 = D(sqh * J["P_X"] / (g[1, 1] * g[0, 0]), 1) / sqh
    maxb = J["P_u"] - (lam / 2) * sp.sqrt(g[2, 2]) * g[0, 0] * div4
    kh = 4 if "horizon_4A" in MUT else 1
    rows = dict(brane=[israel[0], israel[1], xi_up[2], F, israel[2], maxb],
                horizon=[T - kh * A, jt("A", "_X"), jt("B", "_X"), jt("F", "_X"), jt("S", "_X"), P],
                axis=[jt("T", "_u"), jt("A", "_u"), jt("B", "_u"), jt("F", "_u"), S - B, jt("P", "_u")],
                c_ha=[T - kh * A, jt("A", "_X"), jt("B", "_X"), jt("F", "_X"), S - B, P],
                c_hb=[T - kh * A, jt("A", "_X"), jt("B", "_X"), F, jt("S", "_X"), P])
    xi2 = sum(g[a, b] * xi_up[a] * xi_up[b] for a in range(5) for b in range(5) if g[a, b] != 0)
    W = sp.sqrt(-g[0, 0] * (g[1, 1] * g[2, 2] - g[1, 2]**2)) * g[3, 3]
    FXt = gi[0, 0] * (gi[1, 1] * J["P_X"] + gi[1, 2] * J["P_u"])
    diag = dict(xi2=xi2, flux=W * FXt, share=sqh * J["P_X"] / (g[1, 1] * g[0, 0]))
    sub = lambda e: e.subs(th, sp.pi / 3) if hasattr(e, "subs") else e
    inner = [sub(e) for e in inner]
    rows = {k: [sub(e) for e in v] for k, v in rows.items()}
    diag = {k: sub(v) for k, v in diag.items()}
    return J, inner, rows, diag


_CACHE = {}


def compiled():
    """lambdified rows, cached per mutant set (the symbolic build takes about 10 s)"""
    key = tuple(sorted(MUT))
    if key not in _CACHE:
        J, inner, rows, diag = system()
        args = [X, u, bt, mu, lam] + [sp.Symbol(f + j) for f in FUNCS for j in DT.JETS]
        lf = lambda e: sp.lambdify(args, e, "numpy", cse=True)
        _CACHE[key] = dict(inner=[lf(e) for e in inner], rows={k: [lf(e) for e in v] for k, v in rows.items()},
                           diag={k: lf(e) for k, e in diag.items()}, sym=(J, inner, rows, diag), args=args)
    return _CACHE[key]


def cheb01(N):
    i = np.arange(N + 1)
    xc = np.cos(np.pi * i / N)
    c = np.hstack([2, np.ones(N - 1), 2]) * (-1) ** i
    Xm = np.tile(xc, (N + 1, 1)).T
    Dc = np.outer(c, 1 / c) / (Xm - Xm.T + np.eye(N + 1))
    Dc = Dc - np.diag(Dc.sum(axis=1))
    return (1 - xc) / 2, -2 * Dc


def ccw(N):
    """Clenshaw-Curtis weights on cheb01's nodes, for integrals over [0, 1]"""
    t = np.pi * np.arange(N + 1) / N
    w = np.zeros(N + 1)
    for i in range(N + 1):
        s = sum((1.0 if 2 * k == N else 2.0) * np.cos(2 * k * t[i]) / (4 * k * k - 1) for k in range(1, N // 2 + 1))
        w[i] = (1 - s) * (1.0 if i in (0, N) else 2.0) / N
    return w / 2


class Solver:
    def __init__(self, N):
        self.N = N
        self.r, Dr = cheb01(N)
        self.x, Dx = cheb01(N)
        I = np.eye(N + 1)
        self.D = {"": np.kron(I, I), "_X": np.kron(Dr, I), "_u": np.kron(I, Dx), "_XX": np.kron(Dr @ Dr, I),
                  "_Xu": np.kron(Dr, Dx), "_uu": np.kron(I, Dx @ Dx)}
        R, Xx = np.meshgrid(self.r, self.x, indexing="ij")
        self.rg, self.xg = R.ravel(), Xx.ravel()
        self.n = len(self.rg)
        self.c = compiled()
        e = 1e-12
        rr, xx = self.rg, self.xg
        d, h0, a0, b1 = rr > 1 - e, rr < e, xx < e, xx > 1 - e
        self.mask = {"dir": d, "c_ha": h0 & a0 & ~d, "c_hb": h0 & b1 & ~d, "horizon": h0 & ~a0 & ~b1 & ~d,
                     "axis": a0 & ~h0 & ~d, "brane": b1 & ~h0 & ~d, "inner": ~(d | h0 | a0 | b1)}

    def jets(self, U):
        n = self.n
        return [self.D[j] @ U[m * n:(m + 1) * n] for m in range(6) for j in DT.JETS]

    def residual(self, U, p, jac=True):
        n = self.n
        Jv = self.jets(U)
        Rv = np.zeros(6 * n)
        Jm = np.zeros((6 * n, 6 * n)) if jac else None
        funs = dict(self.c["rows"], inner=self.c["inner"])
        for reg, fl in funs.items():
            idx = np.where(self.mask[reg])[0]
            if len(idx) == 0:
                continue
            a = [self.rg[idx], self.xg[idx], p["bt"], p["mu"], p["lam"]] + [jv[idx] for jv in Jv]
            for k, fk in enumerate(fl):
                Rv[k * n + idx] = np.real(np.broadcast_to(fk(*a), idx.shape))
                if not jac:
                    continue
                for jj in range(36):
                    ac = list(a)
                    ac[5 + jj] = a[5 + jj] + 1e-30j
                    cf = np.broadcast_to(np.imag(fk(*ac)) / 1e-30, idx.shape)
                    if np.any(cf):
                        m, j = divmod(jj, 6)
                        Jm[k * n + idx, m * n:(m + 1) * n] += cf[:, None] * self.D[DT.JETS[j]][idx]
        idx = np.where(self.mask["dir"])[0]
        for k, v in enumerate([1.0, 1.0, 1.0, 0.0, 1.0, p["mu"]]):
            Rv[k * n + idx] = U[k * n + idx] - v
            if jac:
                Jm[k * n + idx, :] = 0.0
                Jm[k * n + idx, k * n + idx] = 1.0
        return Rv, Jm

    def guess(self, p):
        U = np.concatenate([np.full(self.n, v, dtype=float) for v in (1, 1, 1, 0, 1)] + [p["mu"] * self.rg**2])
        return U

    def solve(self, U, p, tol=1e-10, maxit=40):
        hist = []
        for _ in range(maxit):
            R, Jm = self.residual(U, p)
            r = np.max(np.abs(R))
            hist.append(r)
            if r < tol:
                break
            dU = np.linalg.solve(Jm, -R)
            s = 1.0
            for _ in range(20):
                Rn, _ = self.residual(U + s * dU, p, jac=False)
                if np.max(np.abs(Rn)) < (1 - 1e-4 * s) * r or s < 1e-3:
                    break
                s /= 2
            U = U + s * dU
        return U, hist

    def arc(self, U, m, Uk, mk, tU, tm, ds, p, tol=1e-10, maxit=30):
        """pseudo-arclength Newton in (U, mu): the residual and <tU, U - Uk>/n + tm (mu - mk) = ds"""
        n6 = len(U)
        idx = np.where(self.mask["dir"])[0] + 5 * self.n
        hist = []
        for _ in range(maxit):
            R, Jm = self.residual(U, dict(p, mu=m))
            a = np.dot(tU, U - Uk) / n6 + tm * (m - mk) - ds
            r = max(np.max(np.abs(R)), abs(a))
            hist.append(r)
            if r < tol:
                break
            JA = np.zeros((n6 + 1, n6 + 1))
            JA[:n6, :n6] = Jm
            JA[idx, n6] = -1.0
            JA[n6, :n6] = tU / n6
            JA[n6, n6] = tm
            d = np.linalg.solve(JA, -np.concatenate([R, [a]]))
            s = 1.0
            for _ in range(20):
                Rn, _ = self.residual(U + s * d[:n6], dict(p, mu=m + s * d[n6]), jac=False)
                an = np.dot(tU, U + s * d[:n6] - Uk) / n6 + tm * (m + s * d[n6] - mk) - ds
                if max(np.max(np.abs(Rn)), abs(an)) < (1 - 1e-4 * s) * r or s < 1e-3:
                    break
                s /= 2
            U, m = U + s * d[:n6], m + s * d[n6]
        return U, m, hist

    def _eval(self, key, U, p):
        a = [self.rg, self.xg, p["bt"], p["mu"], p["lam"]] + self.jets(U)
        return np.real(np.broadcast_to(self.c["diag"][key](*a), (self.n,)))

    def diag(self, U, p):
        """xi^2 off the fictitious boundaries and r = 1 (it carries 1/g_tt there), R4, and the full horizon area"""
        n, N = self.n, self.N
        xi2 = self._eval("xi2", U, p)
        keep = (self.rg > 1e-12) & (self.rg < 1 - 1e-12) & (self.xg > 1e-12)
        Sg = U[4 * n:5 * n].reshape(N + 1, N + 1)
        Bg = U[2 * n:3 * n].reshape(N + 1, N + 1)
        x = self.x
        gx = 2 - x**2
        Dl = (1 + p["bt"] * (1 - x**2)) / p["bt"]
        AH = 2 * np.dot(ccw(N), 4 * np.pi * x**2 * gx * Sg[0] * 2 * np.sqrt(Bg[0] / gx) / Dl**3)
        return dict(xi2=np.max(np.abs(xi2[keep])), R4=p["bt"] * np.sqrt(Sg[0, -1]), AH=AH)

    def flux(self, U, p):
        """the bulk flux, both sides, through each interior r row (the first and last rows dropped: 1/g_tt there)"""
        q = self._eval("flux", U, p).reshape(self.N + 1, self.N + 1)
        return (2 * 4 * np.pi * q @ ccw(self.N))[2:-2]

    def charge(self, U, p):
        """the conserved total: the bulk flux plus the plane's share 4 pi lam B (the Maxwell row integrated)"""
        b = self._eval("share", U, p).reshape(self.N + 1, self.N + 1)[2:-2, -1]
        return self.flux(U, p) + (0.0 if "no_plane_share" in MUT else 4 * np.pi * p["lam"] * b)

    def tail(self, U, p, col):
        """(mu - P)/f near r = 1 on column col: the worst errors of a + b f and of a/(c + ln 1/f), and that a"""
        n, N = self.n, self.N
        P = U[5 * n:].reshape(N + 1, N + 1)[:, col]
        f = 1 - self.r**2
        m = (f > 1e-12) & (f < 0.5)
        y, L = (p["mu"] - P[m]) / f[m], np.log(1 / f[m])
        A1 = np.vstack([np.ones_like(y), f[m]]).T
        e1 = np.max(np.abs(A1 @ np.linalg.lstsq(A1, y, rcond=None)[0] - y))
        best = (np.inf, 0.0)
        for c in np.linspace(0.1, 20, 400):
            b = 1 / (c + L)
            a = np.dot(y, b) / np.dot(b, b)
            best = min(best, (np.max(np.abs(a * b - y)), a))
        return e1, best[0], best[1]

    def soft(self, U, p):
        """the row-equilibrated singular values' bottom two and where the smallest one's rows sit"""
        _, Jm = self.residual(U, p)
        Js = Jm / np.abs(Jm).max(axis=1)[:, None]
        Uu, s, _ = np.linalg.svd(Js)
        k = np.argmax(np.abs(Uu[:, -1]))
        node = k % self.n
        return s[-1], s[-2], k // self.n, self.rg[node], self.xg[node]


def rn_check():
    """5D Reissner-Nordstrom-AdS through the same operator and source: the Maxwell scalar and every component"""
    m, q, kap = sp.symbols("m q kappa", positive=True)
    f = 1 + X**2 - m / X**2 + q**2 / X**4
    g = sp.diag(-f, 1 / f, X**2, X**2 * sp.sin(u)**2, X**2 * sp.sin(u)**2 * sp.sin(th)**2)
    E, _, J = DT.operator(g, g, [], COMPS, Lam=4)
    gi = DT.inverse(g)
    D = DT.make_D([], J)
    Phi = kap * q / X**2
    src, _, mx = maxwell_parts(g, gi, D, sp.diff(Phi, X), sp.diff(Phi, u), COMPS)
    res = [sp.factor(sp.simplify(E[ab] - src[ab])) for ab in COMPS]
    prop = all(r == 0 or sp.simplify(r.subs(kap, sp.sqrt(3) / 2)) == 0 for r in res)
    nonzero = any(sp.simplify(r.subs(kap, 1)) != 0 for r in res)
    return sp.simplify(mx) == 0 and prop and nonzero


def reference_check():
    """every boundary row on the reference metric at sample points, and the reference horizon's kappa_t"""
    c = compiled()
    vals = {"T": 1.0, "A": 1.0, "B": 1.0, "F": 0.0, "S": 1.0, "P": 0.0}
    worst = 0.0
    for reg, xs in (("brane", [(0.3, 1.0), (0.7, 1.0)]), ("horizon", [(0.0, 0.4)]), ("axis", [(0.5, 0.0)]),
                    ("c_ha", [(0.0, 0.0)]), ("c_hb", [(0.0, 1.0)])):
        for (r0, x0) in xs:
            a = [r0, x0, 1.7, 0.0, 0.0] + [vals[fn] if j == "" else 0.0 for fn in FUNCS for j in DT.JETS]
            for fk in c["rows"][reg]:
                worst = max(worst, abs(complex(fk(*a))))
    J, inner, rows, diag = c["sym"]
    gref = fw_metric(None, ref=True)
    kap = sp.limit(sp.sqrt(-gref[0, 0] / (X**2 * gref[1, 1])), X, 0)
    h = sp.Symbol("h", positive=True)                       # X = sqrt(1 - h): inside the domain, 1 - X^2 > 0
    exact = {sp.Symbol(fn + j): (sp.Integer(int(vals[fn])) if j == "" else 0) for fn in FUNCS for j in DT.JETS}
    israel = [sp.simplify(e.subs(exact).subs(u, 1).subs(X, sp.sqrt(1 - h))) for e in [rows["brane"][i]
                                                                                     for i in (0, 1, 4)]]
    return worst, sp.simplify(kap), israel


def run(quiet=False, gate=None, family=False):
    say = (lambda *a: None) if quiet else print
    res = {}
    res["q1"] = rn_check()
    if gate and not gate("q1", res):
        return res
    res["q2"] = reference_check()
    if gate and not gate("q2", res):
        return res
    t0 = time.time()
    S10, S12 = Solver(10), Solver(12)
    p = dict(bt=1.0, mu=0.0, lam=0.0)
    U10, h10 = S10.solve(S10.guess(p), p)
    U12, h12 = S12.solve(S12.guess(p), p)
    d10, d12 = S10.diag(U10, p), S12.diag(U12, p)
    res["q3"] = (h12[-1], d12["R4"])
    say("  bt = 1: N = 12 |R| %.1e R4 %.5f xi2 %.1e (N = 10: %.1e), %.0f s" % (h12[-1], d12["R4"], d12["xi2"],
                                                                              d10["xi2"], time.time() - t0))
    if gate and not gate("q3", res):
        return res
    res["q4"] = (h10[-1], d10["xi2"], d12["xi2"])
    if gate and not gate("q4", res):
        return res
    res["q5"] = S12.soft(U12, p)
    say("  soft direction: sigma %.1e, next %.1e, rows block %d at r = %.3f x = %.3f" % res["q5"])
    if gate and not gate("q5", res):
        return res
    U, out = U12, {}
    for m in (0.02, 0.04, 0.06):
        p = dict(bt=1.0, mu=m, lam=0.0)
        U, h = S12.solve(U, p)
        q = S12.flux(U, p)
        out[m] = (U, h[-1], S12.diag(U, p)["R4"], q.mean(), np.ptp(q) / abs(q.mean()))
        say("  mu %.2f |R| %.1e R4 %.5f Q %.4f spread %.1e" % (m, *out[m][1:]))
    res["q6"] = (d12["R4"], out)
    if gate and not gate("q6", res):
        return res
    res["q7"] = {m: S12.tail(out[m][0], dict(bt=1.0, mu=m, lam=0.0), S12.N) for m in (0.02, 0.06)}
    say("  tail on the plane: " + "; ".join("mu %.2f analytic %.1e log %.1e a %.4f" % (m, *v)
                                            for m, v in res["q7"].items()))
    if gate and not gate("q7", res):
        return res
    p = dict(bt=1.0, mu=0.06, lam=1.0)
    U8, h8 = S12.solve(out[0.06][0].copy(), p)
    qb, qt = S12.flux(U8, p), S12.charge(U8, p)
    res["q8"] = (h8[-1], np.ptp(qb) / abs(qb.mean()), np.ptp(qt) / abs(qt.mean()), qt.mean())
    say("  lam = 1: |R| %.1e bulk flux spread %.1e, total spread %.1e, total %.4f" % res["q8"])
    if gate and not gate("q8", res):
        return res
    res["q9"] = fold(S12, quiet)
    if gate and not gate("q9", res):
        return res
    res["q10"] = large_lambda(S12)
    say("  lam = 64: " + "; ".join("mt %.3f R4 %.4f Coulomb within %.1e, shrink/RN %.3f" % o for o in res["q10"][1]))
    if gate:
        gate("q10", res)
    if family:
        for N in (16, 20):
            fold(Solver(N), quiet=False, steps=40)
    return res


def fold(S, quiet=True, steps=12):
    """the lam = 0 family at bt = 2 by mu to 0.14, then pseudo-arclength through the turn; mu at the turn"""
    say = (lambda *a: None) if quiet else print
    p = dict(bt=2.0, mu=0.0, lam=0.0)
    U, _ = S.solve(S.guess(p), p)
    hist, prev = [], None
    for m in np.arange(0.02, 0.1401, 0.02):
        Ug = U if prev is None else 2 * U - prev                  # the secant predictor in mu
        prev = U
        U, h = S.solve(Ug, dict(p, mu=m))
        hist.append((m, U, h[-1]))
    (m0, U0, _), (m1, U1, _) = hist[-2], hist[-1]
    top = m1
    for k in range(steps):
        tU, tm = U1 - U0, m1 - m0
        nrm = np.sqrt(np.dot(tU, tU) / len(tU) + tm**2)
        tU, tm = tU / nrm, tm / nrm
        U2, m2, h = S.arc(U1 + 0.15 * tU, m1 + 0.15 * tm, U1, m1, tU, tm, 0.15, p)
        say("  N = %d arclength step %d: mu %.5f |R| %.1e R4 %.5f" % (S.N, k, m2, h[-1],
                                                                     S.diag(U2, dict(p, mu=m2))["R4"]))
        if h[-1] > 1e-8:
            break
        top = max(top, m2)
        if m2 < top - 0.003:
            break
        U0, m0, U1, m1 = U1, m1, U2, m2
    return top, max(e for _, _, e in hist)


def large_lambda(S, lam_t=64.0):
    """the bt = 2 hole charged to mu = 0.1 at lam = 0, lam to 8 at that mu, to lam_t at fixed sqrt(lam) mu, then
    charged at lam_t to mt = sqrt(lam) mu/bt = 0.2, 0.3, 0.4: the plane's potential against Coulomb and the hole's
    shrinkage against Reissner-Nordstrom at fixed temperature, 1 - mt^2"""
    bt_ = 2.0
    p = dict(bt=bt_, mu=0.0, lam=0.0)
    U, _ = S.solve(S.guess(p), p)
    R40 = S.diag(U, p)["R4"]
    path = ([(0.0, m) for m in (0.02, 0.04, 0.06, 0.08, 0.1)] + [(l, 0.1) for l in (1.0, 2.0, 4.0, 6.0, 8.0)]
            + [(l, 0.1 * np.sqrt(8.0 / l)) for l in (12.0, 18.0, 27.0, 40.0, lam_t)]
            + [(lam_t, m) for m in (0.0375, 0.05, 0.0625, 0.075, 0.0875, 0.1)])
    prev, worst, out = None, 0.0, []
    for k, (l, m) in enumerate(path):
        Ug = U if prev is None or k in (5, 10, 15) else 2 * U - prev
        prev = U
        q = dict(bt=bt_, mu=m, lam=l)
        U, h = S.solve(Ug, q)
        worst = max(worst, h[-1])
        mt = np.sqrt(l) * m / bt_
        if l == lam_t and min(abs(mt - t) for t in (0.2, 0.3, 0.4)) < 1e-9:
            n, N = S.n, S.N
            Sg, P = U[4 * n:5 * n].reshape(N + 1, N + 1)[:, -1], U[5 * n:].reshape(N + 1, N + 1)[:, -1]
            f = 1 - S.r**2
            j = (f > 1e-12) & (S.r > 0.2)
            rho = bt_ * np.sqrt(Sg[j]) / f[j]
            R4 = S.diag(U, q)["R4"]
            out.append((mt, R4, np.max(np.abs(P[j] / m - (1 - R4 / rho))), (1 - R4 / R40) / mt**2))
    return worst, out


def _check(stage, res):
    if stage == "q1":
        r = res["q1"]
        return r, "Q1 Reissner-Nordstrom-AdS: Maxwell holds, every component vanishes at kappa = sqrt(3)/2: %s" % r
    if stage == "q2":
        worst, kap, israel = res["q2"]
        r = worst < 1e-12 and kap == sp.Rational(1, 2) and all(e == 0 for e in israel)
        return r, ("Q2 every row vanishes on the reference (worst %.1e), Israel's exactly, kappa_t = %s: %s" %
                   (worst, kap, r))
    if stage == "q3":
        h, R4 = res["q3"]
        r = h < 1e-9 and abs(R4 - FW_R4[1.0]) < 0.005
        return r, "Q3 their hole at bt = 1: R4 = %.4f against 1.13 (READ): %s" % (R4, r)
    if stage == "q4":
        h10, x10, x12 = res["q4"]
        r = h10 < 1e-9 and x12 < x10 / 2 and x12 < 1e-4
        return r, "Q4 xi^2 falls with N, %.1e to %.1e (Einstein, not a soliton): %s" % (x10, x12, r)
    if stage == "q5":
        s1, s2, blk, r0, x0 = res["q5"]
        r = s1 < s2 / 30 and blk in (0, 1, 4) and x0 > 1 - 1e-12 and r0 > 0.9
        return r, "Q5 the soft direction, isolated (%.0fx), on the plane's Israel rows at the far corner: %s" % (
            s2 / s1, r)
    if stage == "q6":
        R40, out = res["q6"]
        r = (all(v[1] < 1e-9 and v[4] < 0.01 for v in out.values())
             and R40 > out[0.02][2] > out[0.04][2] > out[0.06][2])
        return r, "Q6 the charged hole at lam = 0: converged, flux constant to %.1e, R4 shrinking: %s" % (
            max(v[4] for v in out.values()), r)
    if stage == "q7":
        t = res["q7"]
        r = all(v[0] > 2 * v[1] for v in t.values()) and 2.5 < t[0.06][2] / t[0.02][2] < 3.5
        return r, "Q7 the far tail is logarithmic (fits %.1fx and %.1fx better), amplitude in proportion to mu: %s" % (
            t[0.02][0] / t[0.02][1], t[0.06][0] / t[0.06][1], r)
    if stage == "q8":
        h, sb, st, qt = res["q8"]
        r = h < 1e-9 and st < 0.01 and sb > 0.1
        return r, "Q8 the field term: total charge constant to %.1e where the bulk flux moves %.2f: %s" % (st, sb, r)
    if stage == "q9":
        top, err = res["q9"]
        r = err < 1e-8 and abs(top - FAMILY_RECORD[12]) < 0.002 and top < FAMILY_RECORD[16] < FAMILY_RECORD[20]
        return r, "Q9 the lam = 0 turn moves with N (%.4f, recorded %.4f, %.4f+; |R| <= %.0e): not a result: %s" % (
            top, FAMILY_RECORD[16], FAMILY_RECORD[20], err, r)
    worst, out = res["q10"]
    r = (worst < 1e-8 and all(o[2] < 0.02 and 0.6 < o[3] < 1.0 for o in out)
         and out[0][1] > out[1][1] > out[2][1])
    return r, "Q10 at lam = 64 the plane's field is Coulomb and the hole shrinks as %.2f-%.2f of RN's: %s" % (
        min(o[3] for o in out), max(o[3] for o in out), r)


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words()
    ok.append(r)
    say("Q0 words: %s" % r)

    def gate(stage, res):
        r, line = _check(stage, res)
        ok.append(r)
        say(line)
        return r or not quiet
    run(quiet, gate)
    ok.append(all(ok))
    say("Q11 (deduced) the reading follows from Q6-Q10: %s" % ok[-1])
    say("%d/%d" % (sum(ok), 12))
    return len(ok) == 12 and all(ok)


def mutants():
    caught = 0
    names = ("src_off", "israel_sign", "horizon_4A", "flat_maxwell", "no_plane_share")
    for m in names:
        MUT.clear()
        MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-14s %s" % (m, "caught" if bad else "MISSED"), flush=True)
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    run(family="--family" in sys.argv)
