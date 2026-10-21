#!/usr/bin/env python3
"""bondi5.py -- the Bondi mass at past null infinity in five dimensions, in the class, as series in s = r^(-1/2)
(N1STAR-PROOF.md section 11, Theorem M; D37).  Labels: computed (exact, sympy, unless marked numerical), READ.

Every quantity is a truncated Laurent series in s with coefficients that are functions of (v, theta); products and
derivatives are taken termwise, so nothing is expanded that is not needed; an r-derivative raises the s-order by two and
v- and theta-derivatives preserve it, and which coefficients each equation's s^6 coefficient contains is checked, not
assumed (B1's `funcs`).

  B1 (computed, exact) The hierarchy.  First the orders below the waves': with b, U and W - 1 general from s^1 and P1, P2
     from s^3, R_rr at s^5 and s^6 (R_ss = 4 s^-6 R_rr at s^-1, s^0) read -12 b1, -24 b2, and R_rth at s^1, s^2
     (R_sth = -2 s^-3 R_rth at s^-2, s^-1) read -(7/4) u1 and 3 b1 u1 - 3 u2: so b1 = b2 = u1 = u2 = 0 for a vacuum
     metric with these expansions, and the chart's b_2 = d_v C4/4 (B2) vanishes by the equations, not by assumption.
     Then, with P1, P2, b, U, W - 1 general series from s^1 (W) and s^3 (the rest) to s^K, the vacuum equations give,
     in order: from R_rr, b3 = b4 = b5 = 0 and
     b6 = -(1/4)(p3^2 + p3 q3 + q3^2); from R_rth, u3 = u4 = 0 and u5 = (12/5)(p3 + q3) tan th - (8 p3 + 16 q3)/(5 sin
     2th) - (4/5) d_th (p3 + q3), u6 the same in the s^4 coefficients (p4, q4) with 4/3 for 4/5 (and 8/3, 16/3); from
     R_vr,
     w1 = w2 = 0 and w3 = -(2/3) (sin th cos th)^-1 d_th (u5 sin th cos th), a divergence; from the traceless part of
     R_AB at s^2, d_v p4 = d_v q4 = 0; R_vv at s^5 is then an identity, and at s^6 it is the mass law
         d_v M = (4/3)(p3_v^2 + p3_v q3_v + q3_v^2) + (2/3) (sin th cos th)^-1 d_th (sin th cos th d_v u6),   M := -w4,
     whose divergence vanishes when d_v p4 = d_v q4 = 0: the pointwise law of [TTS09] (28), time-reversed, in the
     class.  The s^6 coefficient of R_vv contains no coefficient of order above s^6.
     Controls: the law with coefficient 1 in place of 4/3 fails; the law without its divergence term is not an identity
     while p4, q4 are free.
  B2 (computed, exact) The chart.  For g0 + sum_{k=3}^{6} s^k G_k with G_3 = lam W_TT (angular, traceless, transverse)
     and G_4, G_5, G_6 general in the class, the eikonal equation g^-1(dv_B, dv_B) = 0 with v_B = v + sum s^k ů_k is
     solvable order by order: ů_2 = -C4/2, ů_3 = -C5/3, ů_4 = -C6/4 + C4 d_v C4/8 (C_k the s^k coefficients of
     u(ell, ell)); th_B = th + sum s^k ϑ_k with ϑ_4 = -E4/2 - d_th C4/4 (E_k from u(e_th, ell) r^-1) solves
     g^-1(dv_B, dth_B) = 0; the areal radius r_B = r (1 + sum s^k rho_k) has rho_4 = (F4 + G4 + H4)/6 - (1/3) div ϑ_4
     (the trace of G_4 on the sphere, and the Jacobian of the angular shift).  In the chart, g^{v_B v_B} = g^{v_B th_B}
     = 0 to the computed order, e^{2 P1_B} = 1 + 2 p1 s^3 + O(s^4) (the leading angular coefficient is the wave's), and
     e^{-2 b_B} = 1 - (C4_v/2) s^2 - (C5_v/3) s^3 + ...: so the hierarchy's b3 = b4 = 0 forces C4 = C5 = 0 for a vacuum
     metric (they vanish on the seed), as Lemma 11.3's argument predicts.  Control: with ů = 0 (no eikonal correction)
     g^{v_B v_B} is C4 s^4 + ... and not zero.
  B3 (computed, exact) The Hawking mass M[S] = R^2 (1 + (R^2/9) <Theta>) of section 8 for the Bondi spheres S = {v, r}
     in (11.1): R = r exactly, Theta = -(9/r^2) e^{-2b} (W + (2r/3)(sin cos)^-1 d_th (U sin cos)), and r^2 (1 - <...>) =
     -s^-1 <w3 + (2/3) div u5> - <w4 + (2/3) div u6> + O(s), whose divergences have zero mean: M[S] -> <M>.
     Control: the normalisation g(n+, n-) in place of -g(n+, n-) gives a different limit.
  B4 (computed, numerical) The numerics (hf_core5_runs.json, lemmas/data).  The offset of the solver's mean mass aspect
     from mu after the shell, divided by lam^2, at mu0/l5^2 = 100: 0.4589, 0.4577, 0.4568 (lam = 0.05, 0.025, 0.0125);
     at 1000: 0.4578, 0.4569 (lam = 0.025, 0.0125); the law's coefficient for the solver's envelope sin^4(pi (v - 1/2)/3)
     on [1/2, 7/2] with A = 1 is (2/9) int env'^2 = (2/9)(5 pi^2/24) = 5 pi^2/108 = 0.45693: within 0.05 % at lam =
     0.0125 and converging as O(lam).  Control: a sin^2 envelope would give pi^2/27 = 0.3655.

READ (alphaXiv, 2026-10-20).  [TTS09] K. Tanabe, N. Tanahashi and T. Shiromizu, arXiv:0909.0426v2: (4)-(5) p. 2 the
Bondi form; p. 3 "C behaves as ~ 1/r^{3/2} near null infinity"; (20)-(21) p. 4 B = B1/r^3, B1 = -(C11^2 + C11 C21 +
C21^2 + D^2 terms)/8; (26)-(27) p. 4 V = r^2 + V1 r^{1/2} - M + O(r^{-1/2}), V1 = -(2/3)(sin th cos th)^-1 (U_th1 sin th
cos th)_,th + ...; (28) p. 4 "dM(u, x^A)/du = -(1/3)((C11,u)^2 + C11,u C21,u + (C21,u)^2 + (D11,u)^2 + (D21,u)^2 +
(D31,u)^2)"; (35)-(36) p. 5 dA/du = 0 and A = 0.  In the class C1 = -2(P1 + P2), C2 = 2 P1, C3 = 2 P2, B = 2 b.

sympy, numpy.  python3 bondi5.py [--selftest | --mutants | --K N]
"""
import json
import os
import sys
import time

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "..", "lemmas", "data", "hf_core5_runs.json")
v, th = sp.symbols("v theta", real=True)
cs, sn = sp.cos(th), sp.sin(th)
NC = 16                                                     # powers of s kept (set per phase: see set_nc)
K_DEFAULT = 7                                               # the ansatz is carried to s^K


def set_nc(n):
    """the truncation order of every product and sum from here on; lower it once the factors are known to the order
    the next quantity needs (a product is exact to n when each factor is exact to n minus the other's lowest power)"""
    global NC
    NC = n


class Ser:
    """a truncated Laurent series in s: {power: coefficient}, coefficients expanded sympy expressions in (v, theta)"""
    __slots__ = ("c",)

    def __init__(self, c=None):
        self.c = {}
        if c:
            for k, e in c.items():
                e = sp.expand(e)
                if e != 0 and k <= NC:
                    self.c[k] = e

    @staticmethod
    def const(e):
        return Ser({0: e})

    @staticmethod
    def mono(k, e=1):
        return Ser({k: e})

    def __add__(self, o):
        if not isinstance(o, Ser):
            o = Ser.const(o)
        c = dict(self.c)
        for k, e in o.c.items():
            c[k] = c.get(k, 0) + e
        return Ser(c)

    __radd__ = __add__

    def __neg__(self):
        return Ser({k: -e for k, e in self.c.items()})

    def __sub__(self, o):
        return self + (-o if isinstance(o, Ser) else Ser.const(-o))

    def __rsub__(self, o):
        return (-self) + o

    def __mul__(self, o):
        if not isinstance(o, Ser):
            return Ser({k: e*o for k, e in self.c.items()})
        c = {}
        for k1, e1 in self.c.items():
            for k2, e2 in o.c.items():
                if k1 + k2 <= NC:
                    c[k1 + k2] = c.get(k1 + k2, 0) + e1*e2
        return Ser(c)

    __rmul__ = __mul__

    def d(self, x):
        """derivative in v or theta (termwise) or in s"""
        if x == "s":
            return Ser({k - 1: k*e for k, e in self.c.items() if k != 0})
        return Ser({k: sp.diff(e, x) for k, e in self.c.items()})

    def subs(self, rules):
        return Ser({k: e.subs(rules).doit() for k, e in self.c.items()})

    def coeff(self, k):
        return self.c.get(k, sp.S(0))

    def lo(self):
        return min(self.c) if self.c else None

    def inv(self, n=6):
        """1/self for self = a s^m (1 + z), z = O(s): a^-1 s^-m sum (-z)^j"""
        m = self.lo()
        a = self.c[m]
        z = Ser({k - m: e/a for k, e in self.c.items() if k != m})
        out, term = Ser.const(1), Ser.const(1)
        for _ in range(n):
            term = term*(-z)
            out = out + term
        return out*Ser.mono(-m, 1/a)


def texp(z, n=6):
    """exp of a series z = O(s)"""
    out, term = Ser.const(1), Ser.const(1)
    for j in range(1, n + 1):
        term = term*z*sp.Rational(1, j)
        out = out + term
    return out


def F(name, k):
    return sp.Function(f"{name}{k}")(v, th)


def mean(e):
    """the mean over S^3 of a function of theta: weight cos sin dth on [0, pi/2], normalised"""
    return 2*sp.integrate(sp.expand(e)*cs*sn, (th, 0, sp.pi/2))


def divergence(u):
    """(sin cos)^-1 d_th (u sin cos): the divergence of the vector field u d_th on S^3 in the class"""
    return sp.diff(u*sn*cs, th)/(sn*cs)


def christoffel(g, gi, coords):
    n = len(coords)

    def D(e, c):
        return e.d(coords[c]) if coords[c] is not None else Ser()

    dg = [[[D(g[i][j], c) for c in range(n)] for j in range(n)] for i in range(n)]
    Gam = [[[Ser() for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b_ in range(n):
            for c in range(b_, n):
                e = Ser()
                for d in range(n):
                    if gi[a][d].c:
                        t_ = dg[d][b_][c] + dg[d][c][b_] - dg[b_][c][d]
                        if t_.c:
                            e = e + gi[a][d]*t_
                Gam[a][b_][c] = Gam[a][c][b_] = e*sp.Rational(1, 2)
    return Gam, D


def ricci(Gam, D, i, j, n=5):
    e = Ser()
    for a in range(n):
        e = e + D(Gam[a][i][j], a) - D(Gam[a][i][a], j)
        for c in range(n):
            if Gam[a][a][c].c and Gam[c][i][j].c:
                e = e + Gam[a][a][c]*Gam[c][i][j]
            if Gam[a][j][c].c and Gam[c][i][a].c:
                e = e - Gam[a][j][c]*Gam[c][i][a]
    return e


def bondi_metric(P1, P2, b, U, W):
    """(11.1) in the coordinates (v, s, theta, phi1, phi2), r = s^-2, and its inverse (checked in b1)"""
    e2b, em2b = texp(2*b), texp(-2*b)
    Sx, Sxi = texp(-2*(P1 + P2)), texp(2*(P1 + P2))
    r2 = Ser.mono(-4)
    drds, dsdr = Ser.mono(-3, -2), Ser.mono(3, -sp.Rational(1, 2))
    g = [[Ser() for _ in range(5)] for _ in range(5)]
    g[0][0] = -(e2b*W) + r2*Sx*U*U
    g[0][1] = g[1][0] = e2b*drds
    g[0][2] = g[2][0] = -(r2*Sx*U)
    g[2][2] = r2*Sx
    g[3][3] = r2*texp(2*P1)*cs**2
    g[4][4] = r2*texp(2*P2)*sn**2
    gi = [[Ser() for _ in range(5)] for _ in range(5)]
    gi[0][1] = gi[1][0] = em2b*dsdr
    gi[1][1] = em2b*W*dsdr*dsdr
    gi[1][2] = gi[2][1] = U*em2b*dsdr
    gi[2][2] = Ser.mono(4)*Sxi
    gi[3][3] = Ser.mono(4)*texp(-2*P1)*(1/cs**2)
    gi[4][4] = Ser.mono(4)*texp(-2*P2)*(1/sn**2)
    return g, gi


def identity_defect(g, gi, upto=8):
    bad = []
    for i in range(5):
        for j in range(5):
            e = Ser()
            for k in range(5):
                if g[i][k].c and gi[k][j].c:
                    e = e + g[i][k]*gi[k][j]
            e = e - (1 if i == j else 0)
            bad += [(i, j, kk) for kk, ee in e.c.items() if kk <= upto and sp.simplify(ee) != 0]
    return bad


class Checklist:
    """accumulates named boolean checks; prints each when verbose, the failures otherwise, nothing in a control run"""

    def __init__(self, verbose=False, quiet=False):
        self.ok, self.verbose, self.quiet = True, verbose, quiet

    def __call__(self, name, cond):
        cond = bool(cond)
        self.ok &= cond
        if not self.quiet and (self.verbose or not cond):
            print(f"      [{'ok' if cond else 'FAIL'}] {name}", flush=True)
        return cond


def trig0(e):
    """is e identically zero?  simplify, then a numerical probe at generic points"""
    e = sp.simplify(e)
    if e == 0:
        return True
    probe = {th: sp.Rational(3, 7)}
    return abs(complex(sp.N(e.subs(probe)))) < 1e-9 if not e.free_symbols - {th} else False


# ---------------------------------------------------------------------------------------------------------- B1
_RICCI = {}


def hierarchy_ricci(K, verbose=False):
    """the Ricci tensor of (11.1) with general coefficients to s^K, computed once: the metric and its inverse to s^16,
    the Christoffel symbols to s^10 (their lowest power is -3, so this is what R to s^6 needs), R_vv, R_vs, R_sth, R_ss
    to s^6 and the angular components to s^3"""
    if K in _RICCI:
        return _RICCI[K]
    t0 = time.time()
    set_nc(16)
    P1 = Ser({k: F("p", k) for k in range(3, K + 1)})
    P2 = Ser({k: F("q", k) for k in range(3, K + 1)})
    b = Ser({k: F("b", k) for k in range(3, K + 1)})
    U = Ser({k: F("u", k) for k in range(3, K + 1)})
    W = Ser.const(1) + Ser({k: F("w", k) for k in range(1, K + 1)})
    g, gi = bondi_metric(P1, P2, b, U, W)
    defect = identity_defect(g, gi)
    set_nc(10)
    Gam, D = christoffel(g, gi, [v, "s", th, None, None])
    assert min(G.lo() for a in Gam for row in a for G in row if G.c) >= -3
    if verbose:
        print("   Gamma %.0fs" % (time.time() - t0), flush=True)
    set_nc(6)
    R = {key: ricci(Gam, D, *key) for key in [(1, 1), (1, 2), (0, 1), (0, 0)]}
    set_nc(3)
    R.update({key: ricci(Gam, D, *key) for key in [(2, 2), (3, 3), (4, 4)]})
    set_nc(16)
    if verbose:
        print("   Ricci %.0fs" % (time.time() - t0), flush=True)
    _RICCI[K] = (R, defect)
    return _RICCI[K]


def low_orders(verbose=False):
    """the orders below the waves': b, U, W - 1 from s^1, P1, P2 from s^3; R_ss at s^-1, s^0 and R_sth at s^-2, s^-1"""
    if "low" in _RICCI:
        return _RICCI["low"]
    t0 = time.time()
    set_nc(16)
    P1 = Ser({k: F("p", k) for k in range(3, 5)})
    P2 = Ser({k: F("q", k) for k in range(3, 5)})
    b = Ser({k: F("b", k) for k in range(1, 5)})
    U = Ser({k: F("u", k) for k in range(1, 5)})
    W = Ser.const(1) + Ser({k: F("w", k) for k in range(1, 5)})
    g, gi = bondi_metric(P1, P2, b, U, W)
    set_nc(8)
    Gam, D = christoffel(g, gi, [v, "s", th, None, None])
    set_nc(0)
    R = {key: ricci(Gam, D, *key) for key in [(1, 1), (1, 2)]}
    set_nc(16)
    if verbose:
        print("   low orders %.0fs" % (time.time() - t0), flush=True)
    _RICCI["low"] = R
    return R


def b1(control=0, K=K_DEFAULT, verbose=False):
    t0 = time.time()
    chk = Checklist(verbose, quiet=control != 0)
    Rl = low_orders(verbose)
    b1_, b2_, u1_, u2_ = F("b", 1), F("b", 2), F("u", 1), F("u", 2)
    chk("below the waves' order: R_ss at s^-1, s^0 read -12 b1, -24 b2",
        sp.simplify(Rl[(1, 1)].coeff(-1) + 12*b1_) == 0 and sp.simplify(Rl[(1, 1)].coeff(0) + 24*b2_) == 0)
    chk("below the waves' order: R_sth at s^-2, s^-1 read -(7/4) u1, 3 b1 u1 - 3 u2",
        sp.simplify(Rl[(1, 2)].coeff(-2) + sp.Rational(7, 4)*u1_) == 0
        and sp.simplify(Rl[(1, 2)].coeff(-1) - 3*b1_*u1_ + 3*u2_) == 0)
    R, defect = hierarchy_ricci(K, verbose)
    chk("g g^-1 = 1 to s^8", not defect)
    sol = {}

    def solve_for(e, k, unknown):
        c = sp.expand(e.coeff(k).subs(sol).doit())
        cm = sp.solve(sp.Eq(c, 0), unknown)
        assert len(cm) == 1, (k, unknown, c)
        sol[unknown] = sp.simplify(cm[0])
        return sol[unknown]

    p3, q3, p4, q4 = F("p", 3), F("q", 3), F("p", 4), F("q", 4)
    # R_rr (R_ss = 4 s^-6 R_rr): b3, b4, b5, b6
    for k, name in ((1, 3), (2, 4), (3, 5), (4, 6)):
        solve_for(R[(1, 1)], k, F("b", name))
    chk("b3 = b4 = b5 = 0", all(sol[F("b", k)] == 0 for k in (3, 4, 5)))
    chk("b6 = -(1/4)(p^2 + pq + q^2)", sp.simplify(sol[F("b", 6)] + sp.Rational(1, 4)*(p3**2 + p3*q3 + q3**2)) == 0)
    # R_rth (R_sth = -2 s^-3 R_rth): u3, u4, u5, u6
    for k, name in ((0, 3), (1, 4), (2, 5), (3, 6)):
        solve_for(R[(1, 2)], k, F("u", name))
    chk("u3 = u4 = 0", sol[F("u", 3)] == 0 and sol[F("u", 4)] == 0)
    u5 = (sp.Rational(12, 5)*(p3 + q3)*sp.tan(th) - (8*p3 + 16*q3)/(5*sp.sin(2*th))
          - sp.Rational(4, 5)*sp.diff(p3 + q3, th))
    chk("u5 formula", trig0(sol[F("u", 5)] - u5))
    u6 = 4*(p4 + q4)*sp.tan(th) - (8*p4 + 16*q4)/(3*sp.sin(2*th)) - sp.Rational(4, 3)*sp.diff(p4 + q4, th)
    chk("u6 formula (in the s^4 coefficients)", trig0(sol[F("u", 6)] - u6))
    # R_vr (R_vs = -2 s^-3 R_vr): w1, w2, w3
    for k, name in ((2, 1), (3, 2), (4, 3)):
        solve_for(R[(0, 1)], k, F("w", name))
    chk("w1 = w2 = 0", sol[F("w", 1)] == 0 and sol[F("w", 2)] == 0)
    chk("w3 = -(2/3) div u5", trig0(sol[F("w", 3)] + sp.Rational(2, 3)*divergence(u5)))
    # the traceless angular equations at s^2: d_v p4 = d_v q4 = 0
    ang = [sp.expand(R[key].coeff(2).subs(sol).doit()) for key in ((2, 2), (3, 3), (4, 4))]
    p4v, q4v = sp.symbols("p4v q4v")
    angs = [sp.expand(e.subs({sp.Derivative(p4, v): p4v, sp.Derivative(q4, v): q4v})) for e in ang]
    lin = all((sp.Poly(e, p4v, q4v).total_degree() <= 1 if e != 0 else True) and e.subs({p4v: 0, q4v: 0}) == 0
              for e in angs)
    rank = sp.Matrix([[sp.diff(e, p4v), sp.diff(e, q4v)] for e in angs]).subs(th, sp.Rational(3, 7)).rank()
    chk("angular equations at s^2 are linear homogeneous in (d_v p4, d_v q4) of rank 2", lin and rank == 2)
    if verbose:
        print("      angular s^2:", [sp.simplify(e) for e in angs])
    # R_vv: s^5 an identity, s^6 the mass law
    chk("R_vv at s^5 is an identity", trig0(R[(0, 0)].coeff(5).subs(sol).doit()))
    w4v = sp.Symbol("w4v")
    c6 = sp.expand(R[(0, 0)].coeff(6).subs(sol).doit())
    funcs = {f.func.__name__ for f in c6.atoms(sp.core.function.AppliedUndef)}
    chk(f"R_vv at s^6 involves only p3, q3, p4, q4, w4 (found {sorted(funcs)})", funcs <= {"p3", "q3", "p4", "q4", "w4"})
    rate = sp.solve(sp.Eq(c6.subs(sp.Derivative(F("w", 4), v), w4v), 0), w4v)
    chk("R_vv at s^6 is linear in d_v w4", len(rate) == 1)
    Mv = -rate[0]
    quad = sp.Rational(4, 3)*(sp.diff(p3, v)**2 + sp.diff(p3, v)*sp.diff(q3, v) + sp.diff(q3, v)**2)
    coef = 1 if control == 1 else sp.Rational(4, 3)
    quadc = coef*(sp.diff(p3, v)**2 + sp.diff(p3, v)*sp.diff(q3, v) + sp.diff(q3, v)**2)
    div = sp.Rational(2, 3)*divergence(sp.diff(u6, v))
    if control == 2:
        div = 0
    chk("d_v M = (4/3)(p_v^2 + p_v q_v + q_v^2) + (2/3) div d_v u6", trig0(Mv - quadc - div))
    if verbose:
        print("      d_v M - (4/3)(...) =", sp.simplify(Mv - quad), "%.0fs" % (time.time() - t0))
    return chk.ok


# ---------------------------------------------------------------------------------------------------------- B2
def b2(control=0, verbose=False):
    """the wave-gauge expansion to Bondi form, order by order"""
    K = 6
    mu = sp.Function("mu")(v)
    p1, p2 = F("p", 1), F("p", 2)

    def ser(name, lo):
        return Ser({k: F(name, k) for k in range(lo, K + 1)})
    drds, dsdr = Ser.mono(-3, -2), Ser.mono(3, -sp.Rational(1, 2))
    # u in the (v, r, th) basis (orthonormal classes carry r per theta index), then to (v, s, th)
    uvv, uvr, urr = ser("A", 4), ser("B", 4), ser("C", 4)
    uvt, urt = Ser.mono(-2)*ser("D", 4), Ser.mono(-2)*ser("E", 4)
    utt = Ser.mono(-4)*(Ser.mono(3, -2*(p1 + p2)) + ser("F", 4))
    u11 = Ser.mono(-4)*(Ser.mono(3, 2*p1) + ser("G", 4))*cs**2
    u22 = Ser.mono(-4)*(Ser.mono(3, 2*p2) + ser("H", 4))*sn**2
    g0 = [[Ser() for _ in range(5)] for _ in range(5)]
    g0[0][0] = Ser.const(-1) + Ser.mono(4, mu); g0[0][1] = g0[1][0] = drds
    g0[2][2] = Ser.mono(-4); g0[3][3] = Ser.mono(-4, cs**2); g0[4][4] = Ser.mono(-4, sn**2)
    u = [[Ser() for _ in range(5)] for _ in range(5)]
    u[0][0] = uvv; u[0][1] = u[1][0] = uvr*drds; u[1][1] = urr*drds*drds
    u[0][2] = u[2][0] = uvt; u[1][2] = u[2][1] = urt*drds; u[2][2] = utt; u[3][3] = u11; u[4][4] = u22
    g = [[g0[i][j] + u[i][j] for j in range(5)] for i in range(5)]
    g0i = [[Ser() for _ in range(5)] for _ in range(5)]
    g0i[0][1] = g0i[1][0] = dsdr; g0i[1][1] = (Ser.const(1) - Ser.mono(4, mu))*dsdr*dsdr
    g0i[2][2] = Ser.mono(4); g0i[3][3] = Ser.mono(4, 1/cs**2); g0i[4][4] = Ser.mono(4, 1/sn**2)

    def mat(A, B):
        return [[sum((A[i][k]*B[k][j] for k in range(5) if A[i][k].c and B[k][j].c), Ser()) for j in range(5)]
                for i in range(5)]
    h = mat(g0i, u)
    gi = [[Ser.const(1 if i == j else 0) for j in range(5)] for i in range(5)]
    term = [[Ser.const(1 if i == j else 0) for j in range(5)] for i in range(5)]
    for _ in range(4):
        term = mat(term, h)
        term = [[-term[i][j] for j in range(5)] for i in range(5)]
        gi = [[gi[i][j] + term[i][j] for j in range(5)] for i in range(5)]
    gi = mat(gi, g0i)
    chk = Checklist(verbose, quiet=control != 0)
    chk("g g^-1 = 1 to s^7", not identity_defect(g, gi, upto=7))

    def ginv(a, b_):
        return sum((gi[i][j]*a[i]*b_[j] for i in range(5) for j in range(5) if gi[i][j].c and a[i].c and b_[j].c), Ser())

    def grad(f, one=None):
        """covector of f(v, s, th) (a Ser) plus the unit covector d(one) if given"""
        out = [f.d(v), f.d("s"), f.d(th), Ser(), Ser()]
        if one is not None:
            out[one] = out[one] + 1
        return out
    sol = {}
    # the eikonal, v_B = v + ů
    uk = {k: F("us", k) for k in range(2, 5)}
    ust = Ser({k: uk[k] for k in uk})
    if control == 1:
        ust = Ser()
    dvB = grad(ust, 0)
    eik = ginv(dvB, dvB)
    if control != 1:
        for m in range(4, 7):
            c = sp.expand(eik.coeff(m).subs(sol).doit())
            cm = sp.solve(sp.Eq(c, 0), uk[m - 2])
            if len(cm) != 1:
                chk(f"eikonal at s^{m} solvable", False)
                return False
            sol[uk[m - 2]] = sp.simplify(cm[0])
    C4, C5, C6, E4 = F("C", 4), F("C", 5), F("C", 6), F("E", 4)
    if control != 1:
        chk("ů_2 = -C4/2, ů_3 = -C5/3", sol[uk[2]] == -C4/2 and sol[uk[3]] == -C5/3)
        chk("ů_4 = -C6/4 + C4 C4_v/8", sp.simplify(sol[uk[4]] - (-C6/4 + C4*sp.diff(C4, v)/8)) == 0)
    eik_s = eik.subs(sol)
    chk("g^-1(dv_B, dv_B) = 0 to s^6", all(sp.simplify(eik_s.coeff(k)) == 0 for k in range(0, 7)))
    # the angular coordinate th_B = th + ϑ
    tk = {k: F("ts", k) for k in range(4, 7)}
    tst = Ser({k: tk[k] for k in tk})
    dtB = grad(tst, 2)
    dvBs = [e.subs(sol) for e in dvB]
    ang = ginv(dvBs, dtB)
    for m in range(6, 9):
        c = sp.expand(ang.coeff(m).subs(sol).doit())
        cm = sp.solve(sp.Eq(c, 0), tk[m - 2])
        if len(cm) != 1:
            chk(f"angular transport at s^{m} solvable", False)
            return False
        sol[tk[m - 2]] = sp.simplify(cm[0])
    chk("ϑ_4 = -E4/2 - d_th C4/4", sp.simplify(sol[tk[4]] - (-E4/2 - sp.diff(C4, th)/4)) == 0)
    dtBs = [e.subs(sol) for e in dtB]
    chk("g^-1(dv_B, dth_B) = 0 to s^8", all(sp.simplify(ginv(dvBs, dtBs).coeff(k)) == 0 for k in range(0, 9)))
    # the areal radius r_B = r (1 + rho): det g_B^-1 = det g^-1 (det J)^2 and the Bondi form's determinant
    rk = {k: F("rs", k) for k in range(4, 7)}
    rho = Ser({k: rk[k] for k in rk})
    rB = Ser.mono(-2)*(Ser.const(1) + rho)
    drB = grad(rB)
    J = [[dvBs[0], dvBs[1], dvBs[2]], [drB[0], drB[1], drB[2]], [dtBs[0], dtBs[1], dtBs[2]]]
    detJ = (J[0][0]*(J[1][1]*J[2][2] - J[1][2]*J[2][1]) - J[0][1]*(J[1][0]*J[2][2] - J[1][2]*J[2][0])
            + J[0][2]*(J[1][0]*J[2][1] - J[1][1]*J[2][0]))
    # det g^-1 = -s^18/(4 cos^2 sin^2) (1 + ...) and det J = -2 s^-3 (1 + ...): scale each factor to O(1) first, so
    # that no product falls outside the truncation
    B = [[Ser.mono(-3)*gi[i][j] for j in range(3)] for i in range(3)]              # entries now O(1) at least
    detB = (B[0][0]*(B[1][1]*B[2][2] - B[1][2]*B[2][1]) - B[0][1]*(B[1][0]*B[2][2] - B[1][2]*B[2][0])
            + B[0][2]*(B[1][0]*B[2][1] - B[1][1]*B[2][0]))                          # = s^-9 det(block)
    detgi_s = detB*(Ser.mono(-4)*gi[3][3])*(Ser.mono(-4)*gi[4][4])                 # = s^-17 det g^-1 ... check below
    detJ_s = Ser.mono(3)*detJ                                                        # O(1)
    rB_s = Ser.mono(2)*rB                                                            # 1 + rho
    gBvr = ginv(dvBs, drB)
    thB = tst.subs(sol)                                     # th_B - th
    cs2 = Ser.const(cs**2*sn**2) + Ser.const(sp.diff(cs**2*sn**2, th))*thB  # to first order in ϑ (O(s^4))
    # r_B^6 cs2 det g^-1 det J^2 + e^{-4b} = 0 with e^{-2b} = g_B^{vr}; the powers of s: -12 + 17 + 1 - 6 = 0 -> the
    # remaining s^1 is carried by detgi_s (det g^-1 = s^18 ...: s^-17 det g^-1 = O(s))
    areal = (rB_s*rB_s*rB_s*rB_s*rB_s*rB_s*cs2*(Ser.mono(-1)*detgi_s)*detJ_s*detJ_s + gBvr*gBvr)
    for m in range(0, 7):
        c = sp.expand(areal.coeff(m).subs(sol).doit())
        if m < 4:
            chk(f"areal equation at s^{m} holds identically", sp.simplify(c) == 0)
            continue
        cm = sp.solve(sp.Eq(c, 0), rk[m])
        if len(cm) != 1:
            chk(f"areal equation at s^{m} solvable", False)
            return False
        sol[rk[m]] = sp.simplify(cm[0])
    F4, G4, H4 = F("F", 4), F("G", 4), F("H", 4)
    rho4 = (F4 + G4 + H4)/6 - sp.Rational(1, 3)*divergence(sol[tk[4]])   # the trace of G_4 and the angular shift's
    chk("rho_4 = (F4 + G4 + H4)/6 - (1/3) div ϑ_4", trig0(sol[rk[4]] - rho4))
    if verbose:
        print("      rho_4 =", sol[rk[4]])
    # the Bondi functions from the pushed-forward inverse metric
    rBs = rB.subs(sol)
    e2P1 = (rBs*rBs*gi[3][3]*cs**2).inv()                    # 1/(r_B^2 cos^2 g^11), th_B = th + O(s^4)
    chk("e^{2 P1_B} = 1 + O(s^3)", all(sp.simplify(e2P1.coeff(k) - (1 if k == 0 else 0)) == 0 for k in range(3)))
    chk("the s^3 coefficient of e^{2 P1_B} is 2 p1", sp.simplify(e2P1.coeff(3) - 2*p1) == 0)
    gB_vr = ginv(dvBs, [e.subs(sol) for e in drB])
    chk("e^{-2 b_B} -> 1", sp.simplify(gB_vr.coeff(0) - 1) == 0)
    if verbose:
        print("      e^{-2 b_B}:", {k: sp.simplify(gB_vr.coeff(k)) for k in range(1, 5)})
    return chk.ok


# ---------------------------------------------------------------------------------------------------------- B3
def b3(control=0, K=6):
    P1 = Ser({k: F("p", k) for k in range(3, K + 1)})
    P2 = Ser({k: F("q", k) for k in range(3, K + 1)})
    b = Ser({k: F("b", k) for k in range(6, K + 1)})
    U = Ser({k: F("u", k) for k in range(5, K + 1)})
    W = Ser.const(1) + Ser({k: F("w", k) for k in range(3, K + 1)})
    g, gi = bondi_metric(P1, P2, b, U, W)
    # S = {v, s}: n- = -d_r (future ingoing), theta- = -3/r (area form r^3 cos sin exactly);
    # n+ = k = d_v + (W/2) d_r + U d_th, theta+ = 3 W/(2 r) + div U; g(n+, n-) = -e^{2b}
    e2b = texp(2*b)
    r = Ser.mono(-2)
    rinv = Ser.mono(2)
    divU = Ser({k: divergence(e) for k, e in U.c.items()})
    thp = W*rinv*sp.Rational(3, 2) + divU
    thm = rinv*(-3)
    gpm = -e2b
    norm = -gpm if control == 0 else gpm
    Theta = thp*thm*2*norm.inv()
    # M[S] = R^2 (1 + (R^2/9) <Theta>), R = r
    inner = Ser.const(1) + r*r*Theta*sp.Rational(1, 9)
    M = r*r*inner
    # expect: s^-1 coefficient a divergence (mean zero), s^0 coefficient -w4 + divergence
    c_m1 = sp.simplify(M.coeff(-1))
    c_0 = sp.simplify(M.coeff(0))
    neg = all(sp.simplify(M.coeff(k)) == 0 for k in range(-4, -1))
    m1 = sp.simplify(c_m1 + sp.Rational(2, 3)*divergence(F("u", 5)) + F("w", 3))
    m0 = sp.simplify(c_0 + sp.Rational(2, 3)*divergence(F("u", 6)) + F("w", 4))
    return bool(neg and m1 == 0 and m0 == 0)


# ---------------------------------------------------------------------------------------------------------- B4
def b4(control=0):
    R = json.load(open(RUNS))
    rows = {"100_0.05_1_24_16_1_1.36118_2": 0.05, "100_0.025_1_28_16_1_1.36118_2": 0.025,
            "100_0.0125_1_32_16_1_1.36118_2": 0.0125, "1000_0.025_1_36_20_1_1.81517_2": 0.025,
            "1000_0.0125_1_40_20_1_1.81517_2": 0.0125}
    c = {}
    for k, lam in rows.items():
        late = [h["M_mean"] - h["mu"] for h in R[k] if h["v"] >= 3.75 - 1e-9]
        c[k] = float(np.mean(late))/lam**2
    n = 2 if control == 1 else 4                              # the envelope's power
    Delta = 3.0
    vv = np.linspace(0.5, 3.5, 400001)
    env = np.sin(np.pi*(vv - 0.5)/Delta)**n
    pred = (2/9)*np.trapezoid(np.gradient(env, vv)**2, vv)
    fine = [c["100_0.0125_1_32_16_1_1.36118_2"], c["1000_0.0125_1_40_20_1_1.81517_2"]]
    close = all(abs(x/pred - 1) < 5e-3 for x in fine)
    seq = [c["100_0.05_1_24_16_1_1.36118_2"], c["100_0.025_1_28_16_1_1.36118_2"], c["100_0.0125_1_32_16_1_1.36118_2"]]
    converging = all(abs(seq[i] - pred) > abs(seq[i + 1] - pred) for i in range(2)) and all(x > pred - 1e-3 for x in seq)
    return bool(close and converging)


CHECKS = [("B1 the hierarchy in the class: b, U, W from R_rr, R_rth, R_vr; d_v a = 0; the mass law from R_vv at s^6",
           b1, 2),
          ("B2 the chart: eikonal, angular and areal corrections order by order; the Bondi form; p_B = p", b2, 1),
          ("B3 the Hawking mass of the Bondi spheres tends to the mean of the mass aspect", b3, 1),
          ("B4 the numerics' mean-mass offset is (2/9) lam^2 int env'^2 = 5 pi^2/108 lam^2 to 0.5 %", b4, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, f, nc in CHECKS:
        t0 = time.time()
        good = f(verbose=verbose) if "verbose" in f.__code__.co_varnames else f()
        control = any(f(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<110} {state}  ({time.time() - t0:.0f}s)" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"bondi5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, f, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            m = f(control=k)
            caught += (not m)
            print(f"mutant {k} of {name[:2]}: {'caught' if not m else 'NOT caught'}", flush=True)
    print(f"bondi5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--K" in sys.argv:
        K = int(sys.argv[sys.argv.index("--K") + 1])
        print("B1 at K =", K, b1(K=K, verbose=True))
        sys.exit(0)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest("--verbose" in sys.argv) else 1)
