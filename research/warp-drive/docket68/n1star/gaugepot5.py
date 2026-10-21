#!/usr/bin/env python3
"""gaugepot5.py -- the gauge potential wave operator box^Ups = 2 delta_E G delta* of [Hin26] section 6 in five
dimensions: its indicial roots, its zero energy kernel and cokernel on Tangherlini, and the pairings that its
modification E^Ups near the horizon needs ([Hin26] Lemmas 6.6, 6.10, 6.11 and (6.26)) (N1STAR-PROOF.md section 10.15;
ROUTES-OPEN.md 4.16; D57).  Labels: computed (exact, sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) makes box^Ups mode stable at every frequency in the closed upper half plane, zero included,
by a modification E^Ups = E^Ups_infinity + E^Ups_{H+} of the divergence (Proposition 6.12): near infinity E h = -gam (2
iota_{c#} h - (1 - e) c tr h), c = r^-1 dt ((6.5)); near the horizon E_{H+,1} h = 2 iota_{c_H#} h - c_H tr h with c_H
compactly supported ((6.22)).  The proof is perturbative and its inputs are: the indicial roots (Lemma 6.6); the zero
energy kernel and cokernel of the unmodified operator box = 2 delta G delta*, omega_(0) and delta(r - r_+) dr (Lemma
6.10, from [AHW24]); and two pairings, <[box, t_*] omega_(0), omega*> = 4 pi (6.21) and <2 E_{H+,1} G delta* omega_(0),
omega*> in (3 pi, 5 pi) (6.23), which make <f, omega*> = 4 pi (-i sigma^ + c_b gamma^) != 0 (6.26).  Here the
five-dimensional counterparts, on 4+1 Minkowski and on Tangherlini, f = 1 - mu/r^2, r_h = mu^(1/2), with the trace
weight m = 2/(D - 2) = 2/3 in E (damping5.py U2: E G h = -gam (2 iota_c h - e c tr h) in any dimension iff m = 2/(D-2)).

  G1 (computed, exact) The indicial roots of box^Ups on 4+1 Minkowski, from the definitions, on r^-lam (a S dt + b S dr
     + c r dS) and r^(1-lam) V: s0: lam (lam - 3)(lam^2 - lam - 2 - z) = 0, z = 4 e gam^2; vl: (lam + l)(l + 2 - lam) =
     0; sl: (l + 3 - lam)(l + lam - 1) Q = 0, Q = s^2 - (2 + 2 kappa + z) s + kappa (kappa + 1) + z kappa, s = lam (lam
     - 1), kappa = l (l + 2).  At gam = 0 the roots are -1, 0, 2, 3 | -l - 1, -l, 1 - l, l + 1, l + 2, l + 3 | -l, l +
     2: the indicial gap of box is (0, 2) (his (0, 1)); for z > 0 the root 2 moves up in s0 and s1, 2 < lam_s1,2 <
     lam_s0, so (0, lam_s1,2) is an indicial gap (his (6.17b)).  Four-dimensional control: his Lemma 6.6 (s0 0, 2, +-(1
     + z)^(1/2); vl -l, l + 1; sl -l + 1, l + 2 and the four roots +-lam_sl,l, +-lam_sl,l+1 of his formula).  Control:
     the weight 1 in five dimensions, where the s0 root 2 moves down into (1, 2) for small e.
  G2 (computed, exact) The stationary mode equations of box on Tangherlini, static coordinates, symbolic l (S = cos^l th
     cos l p1, V the record's vector harmonic): the dt part and the spatial part decouple (the time reflection); A S dt:
     -r^2 (box)_t = (f/r)(r^3 A')' - kappa A; B S dr + C dS: -r^3 f (box)_r/S = (r^3 f^2 B')' - r f (kappa + 3 - 3
     mu/r^2) B + 2 kappa f C, -kappa r (box)_th/S_th = kappa (r f C')' - kappa^2 C/r + 2 kappa f B; V: -r (box)/V = (r f
     V')' - (kappa + 1) V/r.  Control: 2 delta delta* (without G), whose r equation is not this one (on A S dt the
     divergence vanishes and the two operators agree).
  G3 (computed, exact) The identities behind the kernel for l >= 1: at r_h the A equation reads -kappa r_h A(r_h) = 0; A
     (r^3 A')' = (r^3 A A')' - r^3 A'^2; B (r^3 f^2 B')' + kappa C (r f C')' = (r^3 f^2 B B' + kappa r f C C')' - r^3
     f^2 B'^2 - kappa r f C'^2, with the zeroth-order matrix [[r f (kappa + 3 - 3 mu/r^2), -2 kappa f], [-2 kappa f,
     kappa^2/r]] of determinant kappa^2 f (kappa - 1 + mu/r^2), positive definite for r > r_h, l >= 1; V (r f V')' = (r
     f V V')' - r f V'^2.  Control: at l = 0 (kappa = 0) the A equation leaves A(r_h) free.
  G4 (computed, exact) l = 0: A = a + b/r^2, B = c/(r^3 f) + d r/f; smooth at the future horizon (A and B - A/f smooth,
     the ingoing chart) and decaying, the kernel is the span of W* = dt/r^2 + mu^(1/2) dr/(r^3 f) (wavegauge5.py W2), in
     the space of shifted weight alpha + 2 < 2.  Control: dt/r^2 alone, not smooth.
  G5 (computed, exact) The cokernel functional omega* = delta(r - r_h) dr, in ingoing coordinates (v, r): g^-1(box u,
     dr) at r_h vanishes identically for every stationary u = a(r) dv + b(r) dr, and for the scalar type at any l >= 1
     it is a multiple of S, whose integral over S^3 vanishes; the vector type has no dv or dr component.  So omega*
     annihilates the range of box(0).  Four-dimensional control: the same for Hintz's omega* at a = 0.  Control: delta(r
     - 2 r_h) dr, which does not.
  G6 (computed, exact) The pairings, ingoing coordinates, |dg_X| = r^3 cos th sin th |dr dth dp1 dp2|, t_* = v near the
     horizon: <[box, t_*] W*, omega*> = 4 pi^2 (his (6.21), 4 pi; the four-dimensional control reproduces it); a change
     t_* -> t_* + F(r) does not change it (F = r^2 checked); W* is divergence-free; eta := iota_{grad r} delta* W* =
     -mu^(-3/2) (dv + (3/2) dr) at r_h, nonzero; <2 E_{H+,1} G delta* W*, omega*> = -12 pi^2 c_v - 8 pi^2 c_r for c_H =
     c_v dv + c_r dr at r_h (four-dimensional control -16 pi c_v - 8 pi c_r, so that c_H = -(1/2) dr gives his 4 pi), so
     c_H = -(1/2) chi(r) dr, chi = 1 near r_h, gives 4 pi^2 and (6.26) reads 4 pi^2 (-i sigma^ + gamma^) != 0 for Im
     sigma^ >= 0, gamma^ >= 0, not both 0.  Control: c_H = +(1/2) dr, where it vanishes at (sigma^, gamma^) = (i, 1).
  G7 (computed, exact) The first term of his f, d_sigma box(0) W* = -i [box, t_*] W*, t_* = t - r* for large r: i r^-3
     dt + O(r^-4); in four dimensions -i [box, t - r*] omega_(0) = O(r^-3) as well, by his cancellation ((rho d_rho - 1)
     annihilates rho; his footnote 69), while in five dimensions (rho d_rho - 3/2) rho^2 = rho^2/2 and the order rho^3
     is the dimension's.  Control: the four-dimensional cancellation claimed in five dimensions (no r^-3 term).

Deduced, not computed here: that the kernel of box(0) on the five-dimensional weighted spaces is exactly the span of W*
-- l = 0 by G4, every l >= 1 by G3's energy identities, the boundary terms vanishing at r_h (f = 0, smooth) and at
infinity (decaying exponents >= 2) -- and that delta(r - r_h) dr spans the cokernel once the index is 0 ([Hin26c]'s
Fredholm theory in five dimensions, OPEN).  With these, Step 1 of his proof of Proposition 6.12 has its five-dimensional
inputs; its estimates, and Step 2, are [Hin26c]'s in five dimensions (OPEN).

READ (alphaXiv, 2026-10-21).  [Hin26] pp. 25-26 (section 1.4.1), 82 ((4.6), Definition 4.2), 113 (section 6,
(6.1)-(6.6)), 117-118 (Lemma 6.6, (6.17a)-(6.17b), Remark 6.7, Lemma 6.8), 119-124 (section 6.4: Proposition 6.9, Lemmas
6.10-6.11, Proposition 6.12 and its proof, (6.20)-(6.28), footnotes 65-69).

sympy.  python3 gaugepot5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import sympy as sp

from damping5 import Checklist

D = sp.diff
mu = sp.Symbol("mu", positive=True)
lam, gam, e, m = sp.symbols("lam gamma e m")
L = sp.Symbol("l", positive=True, integer=True)
z = sp.Symbol("z", positive=True)
SQ = sp.sqrt(mu)


# ------------------------------------------------------------------------------------------------- geometry
def chart(n, kind):
    """kind 'mink' (Minkowski, polar), 'static' (Schwarzschild / Tangherlini), 'ingoing' (v, r, angles)."""
    t, r = sp.symbols("t r", positive=True)
    if n == 3:
        th, ph = sp.symbols("theta phi", real=True)
        X, ang = [t, r, th, ph], [th, ph]
        f = 1 - mu/r
        A = sp.diag(r**2, r**2*sp.sin(th)**2)
        vol = r**2*sp.sin(th)
    else:
        th, p1, p2 = sp.symbols("theta p1 p2", real=True)
        X, ang = [t, r, th, p1, p2], [th, p1, p2]
        f = 1 - mu/r**2
        A = sp.diag(r**2, r**2*sp.cos(th)**2, r**2*sp.sin(th)**2)
        vol = r**3*sp.cos(th)*sp.sin(th)
    N = len(X)
    g = sp.zeros(N, N)
    g[2:, 2:] = A
    if kind == "mink":
        f = sp.Integer(1)
        g[0, 0], g[1, 1] = -1, 1
    elif kind == "static":
        g[0, 0], g[1, 1] = -f, 1/f
    else:
        g[0, 0], g[0, 1], g[1, 0] = -f, 1, 1
    gi = g.inv().applyfunc(sp.simplify)
    Gam = [[[sp.simplify(sum(gi[a, d]*(D(g[d, b], X[c]) + D(g[d, c], X[b]) - D(g[b, c], X[d])) for d in range(N))/2)
             for c in range(N)] for b in range(N)] for a in range(N)]
    return dict(X=X, ang=ang, f=f, g=g, gi=gi, Gam=Gam, vol=vol, N=N, t=t, r=r)


_CH = {}


def ch(n, kind):
    if (n, kind) not in _CH:
        _CH[(n, kind)] = chart(n, kind)
    return _CH[(n, kind)]


def dstar(C, w):
    X, Gam, N = C["X"], C["Gam"], C["N"]
    nab = [[D(w[a], X[b]) - sum(Gam[k][b][a]*w[k] for k in range(N)) for b in range(N)] for a in range(N)]
    return sp.Matrix(N, N, lambda a, b: (nab[a][b] + nab[b][a])/2)


def trace(C, T):
    return sum(C["gi"][a, b]*T[a, b] for a in range(C["N"]) for b in range(C["N"]))


def Gop(C, T):
    return T - C["g"]*trace(C, T)/2


def delta(C, T):
    """(delta T)_a = -g^{kq} T_{ak;q}"""
    X, gi, Gam, N = C["X"], C["gi"], C["Gam"], C["N"]
    out = []
    for a in range(N):
        s = 0
        for k in range(N):
            for q in range(N):
                if gi[k, q] != 0:
                    s += gi[k, q]*(D(T[a, k], X[q]) - sum(Gam[j][q][a]*T[j, k] + Gam[j][q][k]*T[a, j] for j in range(N)))
        out.append(-s)
    return out


def E_inf(C, T, weight):
    """E h = -gam (2 iota_{c#} h - weight (1 - e) c tr h), c = r^-1 dt ([Hin26] (6.5))"""
    N, gi, r = C["N"], C["gi"], C["r"]
    c = [1/r] + [0]*(N - 1)
    cs = [sum(gi[k, j]*c[j] for j in range(N)) for k in range(N)]
    trT = trace(C, T)
    return [-gam*(2*sum(cs[k]*T[k, a] for k in range(N)) - weight*(1 - e)*c[a]*trT) for a in range(N)]


def box(C, w, weight=None, useG=True):
    """2 (delta + E) G delta* w (E only when weight is given)"""
    T = dstar(C, w)
    if useG:
        T = Gop(C, T)
    out = [2*x for x in delta(C, T)]
    if weight is not None:
        out = [a + 2*b for a, b in zip(out, E_inf(C, T, weight))]
    return out


def red(x):
    return sp.simplify(sp.powsimp(sp.expand_trig(sp.expand(x)), force=True))


def harmonic(n, ang, l):
    return sp.sin(ang[0])**l*sp.cos(l*ang[1]) if n == 3 else sp.cos(ang[0])**l*sp.cos(l*ang[1])


def vector_harmonic(n, ang, l):
    if n == 3:
        S = harmonic(3, ang, l)
        return [-D(S, ang[1])/sp.sin(ang[0]), sp.sin(ang[0])*D(S, ang[0])]
    return [0, sp.sin(ang[0])**(l - 1)*sp.cos((l - 1)*ang[2])*sp.cos(ang[0])**2, 0]


# ------------------------------------------------------------------------------------------------- G1
_IND = {}


def indicial(n, weight):
    key = (n, weight)
    if key in _IND:
        return _IND[key]
    C = ch(n, "mink")
    r, ang = C["r"], C["ang"]
    a, b, c = sp.symbols("a b c")
    out = []
    for l in (0, L):
        S = harmonic(n, ang, l)
        w = [r**-lam*a*S, r**-lam*b*S] + [r**(1 - lam)*c*D(S, x) for x in ang]
        R = [sp.expand(sp.powsimp(sp.expand(x*r**(lam + 2)), force=True)) for x in box(C, w, weight)]
        rows, var = [red(R[0]/S), red(R[1]/S)], (a, b)
        if l != 0:
            rows.append(red(R[2]/(r*D(S, ang[0]))))
            var = (a, b, c)
        out.append(sp.Matrix([[sp.expand(q).coeff(x) for x in var] for q in rows]).applyfunc(sp.simplify).det())
    V = vector_harmonic(n, ang, L)
    w = [0, 0] + [r**(1 - lam)*x for x in V]
    R = [sp.expand(sp.powsimp(sp.expand(x*r**(lam + 2)), force=True)) for x in box(C, w, weight)]
    k = [i for i, x in enumerate(V) if x != 0][0]
    out.append(red(R[2 + k]/(r*V[k])))
    _IND[key] = [sp.factor(x) for x in out]
    return _IND[key]


def proportional(p, q, var):
    """p = const * q as polynomials in var, const != 0"""
    P, Q = sp.Poly(sp.expand(p), var), sp.Poly(sp.expand(q), var)
    if P.degree() != Q.degree():
        return False
    k = sp.simplify(P.LC()/Q.LC())
    return k != 0 and sp.expand(p - k*q) == 0


def roots_in(P, lo, hi, var=lam):
    return sp.Poly(sp.expand(P), var).count_roots(lo, hi)


def g1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    kap = L*(L + 2)
    if control == 1:                                       # control: the weight 1 in five dimensions
        s0, sl, vl = indicial(4, 1)
        P = s0.subs({e: 0, gam: sp.Rational(1, 10)})
        chk("weight 1 in five dimensions: no s0 root in (1, 2) at e = 0, gam = 1/10", roots_in(P, 1, 2) == 0)
        return chk.ok
    # four-dimensional control: his Lemma 6.6
    s0, sl, vl = indicial(3, 1)
    zz = 4*e*gam**2
    A4 = L*(L + 1) + sp.Rational(1, 2) + 2*e*gam**2
    B4 = L*(L + 1) + (sp.Rational(1, 2) + 2*e*gam**2)**2
    chk("n = 3: s0 det ~ lam (lam - 2)(lam^2 - 1 - 4 e gam^2), his roots 0, 2, +-lam_s0,1",
        proportional(s0, lam*(lam - 2)*(lam**2 - 1 - zz), lam))
    chk("n = 3: vl ~ (lam + l)(l + 1 - lam), his -l, l + 1", proportional(vl, (lam + L)*(L + 1 - lam), lam))
    chk("n = 3: sl det ~ (l + 2 - lam)(l + lam - 1)(lam^4 - 2 A lam^2 + A^2 - B), A, B his: the roots -l + 1, l + 2, "
        "+-lam_sl,l, +-lam_sl,l+1",
        proportional(sl, (L + 2 - lam)*(L + lam - 1)*(lam**4 - 2*A4*lam**2 + A4**2 - B4), lam))
    # five dimensions
    s0, sl, vl = indicial(4, sp.Rational(2, 3))
    s = lam*(lam - 1)
    Q = s**2 - (2 + 2*kap + zz)*s + kap*(kap + 1) + zz*kap
    chk("n = 4: s0 det ~ lam (lam - 3)(lam^2 - lam - 2 - 4 e gam^2)",
        proportional(s0, lam*(lam - 3)*(lam**2 - lam - 2 - zz), lam))
    chk("n = 4: vl ~ (lam + l)(l + 2 - lam)", proportional(vl, (lam + L)*(L + 2 - lam), lam))
    chk("n = 4: sl det ~ (l + 3 - lam)(l + lam - 1) Q, Q = s^2 - (2 + 2 kappa + z) s + kappa (kappa + 1) + z kappa",
        proportional(sl, (L + 3 - lam)*(L + lam - 1)*Q, lam))
    Q0 = sp.factor(Q.subs({e: 0}))
    chk("n = 4, gam = 0: Q = (lam + l)(lam + l + 1)(lam - l - 1)(lam - l - 2); the roots -1, 0, 2, 3 | -l - 1, -l, "
        "1 - l, l + 1, l + 2, l + 3 | -l, l + 2: the gap (0, 2)",
        sp.expand(Q0 - (lam + L)*(lam + L + 1)*(lam - L - 1)*(lam - L - 2)) == 0)
    ok = True
    for zv in (sp.Rational(1, 1000), sp.Rational(1, 10)):
        P0 = (lam**2 - lam - 2 - zv)
        P1 = sp.expand(sp.expand(Q.subs(L, 1)).subs(e, zv/(4*gam**2)))
        ok &= roots_in(P0, 0, 2) == 0 and roots_in(P1, 0, 2) == 0
        r1 = min(x for x in sp.Poly(P1, lam).real_roots() if x > 0)
        r0 = min(x for x in sp.Poly(P0, lam).real_roots() if x > 0)
        ok &= bool(2 < r1 < r0)
        for lv in (2, 3, 7):
            Pl = sp.expand(sp.expand(Q.subs(L, lv)).subs(e, zv/(4*gam**2)))
            ok &= roots_in(Pl, 0, 2) == 0
    chk("n = 4 at z = 4 e gam^2 in {1/1000, 1/10}: no root in (0, 2] in s0, s1, s2, s3, s7; 2 < lam_s1,2 < lam_s0", ok)
    zs = sp.Symbol("zs", positive=True)
    kk = L*(L + 2)
    s_minus = 1 + kk + zs/2 - sp.sqrt((1 + zs/2)**2 + kk)
    chk("n = 4, every z > 0, every l: Q's roots in s = lam (lam - 1) are 1 + kappa + z/2 +- ((1 + z/2)^2 + "
        "kappa)^(1/2); s_- increases in z from s_-(0) = l (l + 1); at l = 1, 2 < s_- < 2 + z (the s0 value) since "
        "(2 + z/2)^2 - (1 + z/2)^2 - 3 = z and (2 - z/2)^2 - (1 + z/2)^2 - 3 = -3z; so 2 < lam_s1,2 < lam_s0 and "
        "lam >= 3 for l >= 2",
        sp.expand(sp.expand((s_minus - 1 - kk - zs/2)**2) - ((1 + zs/2)**2 + kk)) == 0
        and sp.expand((L + 1)**2 - (1 + kk)) == 0 and sp.expand(1 + kk - (L + 1) - L*(L + 1)) == 0
        and sp.expand((2 + zs/2)**2 - (1 + zs/2)**2 - 3) == zs and sp.expand((2 - zs/2)**2 - (1 + zs/2)**2 - 3) == -3*zs
        and sp.simplify(sp.diff(s_minus, zs)*2*sp.sqrt((1 + zs/2)**2 + kk)
                        - (sp.sqrt((1 + zs/2)**2 + kk) - 1 - zs/2)) == 0
        and sp.expand(Q.subs(4*e*gam**2, zs) - (s**2 - (2 + 2*kk + zs)*s + kk*(kk + 1) + zs*kk)) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- G2-G3
_MODES = {}


def modes(useG=True):
    if useG in _MODES:
        return _MODES[useG]
    C = ch(4, "static")
    r, ang, f = C["r"], C["ang"], C["f"]
    A, B, Cf, V = [sp.Function(nm)(r) for nm in ("A", "B", "C", "V")]
    S = harmonic(4, ang, L)
    RA = box(C, [A*S, 0, 0, 0, 0], useG=useG)
    RS = box(C, [0, B*S] + [Cf*D(S, x) for x in ang], useG=useG)
    Vh = vector_harmonic(4, ang, L)
    RV = box(C, [0, 0] + [V*x for x in Vh], useG=useG)
    out = dict(A=A, B=B, C=Cf, V=V, r=r, f=f, S=S, Vh=Vh,
               EA=red(RA[0]/S), A_spatial=[sp.simplify(x) for x in RA[1:]],
               S_t=sp.simplify(RS[0]), E1=red(RS[1]/S), E2=red(RS[2]/D(S, ang[0])),
               EV=red(RV[3]/Vh[1]), V_other=[sp.simplify(RV[i]) for i in (0, 1, 2, 4)])
    _MODES[useG] = out
    return out


def g2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    M = modes(useG=(control != 1))
    A, B, Cf, V, r, f = M["A"], M["B"], M["C"], M["V"], M["r"], M["f"]
    kap = L*(L + 2)
    chk("-r^3 f (box)_r/S = (r^3 f^2 B')' - r f (kappa + 3 - 3 mu/r^2) B + 2 kappa f C",
        sp.simplify(-r**3*f*M["E1"] - (D(r**3*f**2*D(B, r), r) - r*f*(kap + 3 - 3*mu/r**2)*B + 2*kap*f*Cf)) == 0)
    if control == 1:
        return chk.ok
    chk("the A equation: -r^2 (box (A S dt))_t / S = (f/r)(r^3 A')' - kappa A",
        sp.simplify(-r**2*M["EA"] - ((f/r)*D(r**3*D(A, r), r) - kap*A)) == 0)
    chk("the dt part and the spatial part decouple (A S dt has no spatial component, B S dr + C dS no dt component)",
        all(x == 0 for x in M["A_spatial"]) and M["S_t"] == 0)
    chk("-kappa r (box)_th/S_th = kappa (r f C')' - kappa^2 C/r + 2 kappa f B",
        sp.simplify(-kap*r*M["E2"] - (kap*D(r*f*D(Cf, r), r) - kap**2*Cf/r + 2*kap*f*B)) == 0)
    chk("the vector type: -r (box V)/V = (r f V')' - (kappa + 1) V/r, no other component",
        sp.simplify(-r*M["EV"] - (D(r*f*D(V, r), r) - (kap + 1)*V/r)) == 0 and all(x == 0 for x in M["V_other"]))
    return chk.ok


def g3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    M = modes()
    A, B, Cf, V, r, f = M["A"], M["B"], M["C"], M["V"], M["r"], M["f"]
    kap = 0 if control == 1 else L*(L + 2)
    rh = SQ
    at_h = sp.simplify(sp.expand(f*D(r**3*D(A, r), r) - kap*r*A).subs(r, rh))
    chk("at r_h the A equation f (r^3 A')' = kappa r A reads -kappa r_h A(r_h) = 0, so A(r_h) = 0 for l >= 1",
        sp.simplify(at_h + kap*rh*A.subs(r, rh)) == 0 and kap != 0)
    if control == 1:
        return chk.ok
    chk("A (r^3 A')' = (r^3 A A')' - r^3 A'^2",
        sp.simplify(A*D(r**3*D(A, r), r) - (D(r**3*A*D(A, r), r) - r**3*D(A, r)**2)) == 0)
    lhs = B*D(r**3*f**2*D(B, r), r) + kap*Cf*D(r*f*D(Cf, r), r)
    rhs = D(r**3*f**2*B*D(B, r) + kap*r*f*Cf*D(Cf, r), r) - r**3*f**2*D(B, r)**2 - kap*r*f*D(Cf, r)**2
    chk("B (r^3 f^2 B')' + kappa C (r f C')' = (r^3 f^2 B B' + kappa r f C C')' - r^3 f^2 B'^2 - kappa r f C'^2",
        sp.simplify(lhs - rhs) == 0)
    Mz = sp.Matrix([[r*f*(kap + 3 - 3*mu/r**2), -2*kap*f], [-2*kap*f, kap**2/r]])
    xk = sp.Symbol("x", positive=True)
    det = sp.simplify(Mz.det() - kap**2*f*(kap - 1 + mu/r**2))
    m11 = sp.expand((kap + 3 - 3*mu/r**2).subs(mu, xk*r**2))
    chk("the zeroth-order form has the matrix [[r f (kappa + 3 - 3 mu/r^2), -2 kappa f], [-2 kappa f, kappa^2/r]] of "
        "determinant kappa^2 f (kappa - 1 + mu/r^2), and M_11 - r f kappa = 3 r f (1 - mu/r^2): positive definite for "
        "r > r_h (0 < x = mu/r^2 < 1) and kappa >= 3",
        det == 0 and sp.expand(m11 - kap - 3*(1 - xk)) == 0)
    chk("V (r f V')' = (r f V V')' - r f V'^2, and the decaying exponents at infinity: A ~ r^-(l+2), V ~ r^-(l+1), B ~ "
        "r^-lam, C ~ r^(1-lam) with lam >= 2 (G1): the boundary terms r^3 A A', r f V V', r^3 f^2 B B', r f C C' vanish "
        "at infinity (checked at the slowest, l = 1, lam = 2) and, f = 0, at r_h",
        sp.simplify(V*D(r*f*D(V, r), r) - (D(r*f*V*D(V, r), r) - r*f*D(V, r)**2)) == 0
        and sp.limit(r**3*r**-3*D(r**-3, r), r, sp.oo) == 0 and sp.limit(r*r**-2*D(r**-2, r), r, sp.oo) == 0
        and sp.limit(r**3*(r**-2)*D(r**-2, r), r, sp.oo) == 0 and sp.limit(r*(r**-1)*D(r**-1, r), r, sp.oo) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- G4
def g4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    C = ch(4, "static")
    r, f = C["r"], C["f"]
    a, b, c, d = sp.symbols("a b c d")
    Ag, Bg = a + b/r**2, c/(r**3*f) + d*r/f
    R = [sp.simplify(x) for x in box(C, [Ag, Bg, 0, 0, 0])]
    chk("l = 0: box (A dt + B dr) = 0 for A = a + b/r^2, B = c/(r^3 f) + d r/f (four constants)", all(x == 0 for x in R))
    if control == 1:                                       # control: dt/r^2 alone
        num = sp.factor(sp.cancel(-Ag/f + Bg).subs({a: 0, b: 1, c: 0, d: 0}))
        chk("dt/r^2 alone is smooth at the future horizon (B - A/f smooth)", sp.limit(num*(r - SQ), r, SQ) == 0)
        return chk.ok
    # decaying: a = 0 (A), d = 0 (B ~ d r); smooth: B - A/f has no pole at r_h
    res = sp.limit(sp.cancel((Bg - Ag/f).subs({a: 0, d: 0}))*(r - SQ), r, SQ)
    sol = sp.solve(res, c)
    W = [1/r**2, SQ/(r**3*f)]
    chk("decaying forces a = d = 0, and smoothness of B - A/f at r_h forces c = mu^(1/2) b: the kernel at l = 0 is the "
        "span of W* = dt/r^2 + mu^(1/2) dr/(r^3 f)",
        sol == [b*SQ] and sp.simplify(Ag.subs({a: 0, b: 1}) - W[0]) == 0
        and sp.simplify(Bg.subs({a: 0, b: 1, d: 0, c: SQ}) - W[1]) == 0)
    chk("W* in ingoing coordinates: dv/r^2 - dr/(r (r + mu^(1/2))), smooth; |W*| ~ r^-2: in the space iff alpha + 2 < 2",
        sp.simplify(W[1] - 1/(r**2*f) - (-1/(r*(r + SQ)))) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- G5
def g5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in (4, 3):
        C = ch(n, "ingoing")
        r, gi, X, ang = C["r"], C["gi"], C["X"], C["ang"]
        rh = SQ if n == 4 else mu
        at = 2*rh if control == 1 else rh
        a, b = sp.Function("a")(r), sp.Function("b")(r)
        BU = box(C, [a, b] + [0]*(n - 1))
        val = sp.simplify(sum(gi[1, k]*BU[k] for k in range(C["N"])).subs(r, at))
        chk("n = %d: g^-1(box u, dr) at r = %s vanishes for every u = a(r) dv + b(r) dr" % (n, at), val == 0)
        if control == 1:
            return chk.ok
        if n == 3:
            continue
        A, B, Cf = [sp.Function(nm)(r) for nm in ("A", "B", "C")]
        S = harmonic(4, ang, L)
        BU = box(C, [A*S, B*S] + [Cf*D(S, x) for x in ang])
        val = sp.simplify(sum(gi[1, k]*BU[k] for k in range(C["N"])).subs(r, rh)/S)
        chk("n = 4, scalar type at any l: g^-1(box u, dr) at r_h is (a function of l alone) times S, whose integral "
            "over S^3 vanishes for l >= 1", not (val.free_symbols & set(ang)))
        Vh = vector_harmonic(4, ang, L)
        V = sp.Function("V")(r)
        BU = box(C, [0, 0] + [V*x for x in Vh])
        chk("n = 4, vector type: box u has no dv or dr component", sp.simplify(BU[0]) == 0 and sp.simplify(BU[1]) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- G6
def pairing_data(n):
    C = ch(n, "ingoing")
    r, gi, X, N, vol = C["r"], C["gi"], C["X"], C["N"], C["vol"]
    v = X[0]
    rh = SQ if n == 4 else mu
    area = 2*sp.pi**2 if n == 4 else 4*sp.pi
    W = [1/r**2, -1/(r*(r + SQ))] + [0]*3 if n == 4 else [1/r, -1/r, 0, 0]
    BW = box(C, W)

    def pair(w):                                            # <w, delta(r - r_h) dr>
        return sp.simplify(area*rh**(n - 1)*sum(gi[1, k]*w[k] for k in range(N)).subs(r, rh))

    def comm(F):
        return [sp.simplify(x - F*y) for x, y in zip(box(C, [F*q for q in W]), BW)]
    P21 = pair(comm(v))
    P21F = pair(comm(v + r**2))
    divW = sp.simplify(sum(D(vol*sum(gi[a, k]*W[k] for k in range(N)), X[a]) for a in range(N))/vol)
    T = dstar(C, W)
    eta = [sp.simplify(sum(gi[1, k]*T[k, b] for k in range(N)).subs(r, rh)) for b in range(N)]
    cv, cr = sp.symbols("c_v c_r")
    c = [cv, cr] + [0]*(n - 1)
    cs = [sum(gi[k, j]*c[j] for j in range(N)) for k in range(N)]
    GT = Gop(C, T)
    wt = 1 if n == 3 else sp.Rational(2, 3)
    EGT = [2*sum(cs[k]*GT[k, j] for k in range(N)) - wt*c[j]*trace(C, GT) for j in range(N)]
    P23 = sp.expand(pair([2*x for x in EGT]))
    return dict(BW=BW, P21=P21, P21F=P21F, divW=divW, eta=eta, P23=P23, cv=cv, cr=cr)


def g6(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    P5, P4 = pairing_data(4), pairing_data(3)
    cv, cr = P5["cv"], P5["cr"]
    chk("box W* = 0 (n = 4) and box omega_(0) = 0 (n = 3), omega_(0) = dv/r - dr/r his a = 0 form",
        all(sp.simplify(x) == 0 for x in P5["BW"] + P4["BW"]))
    chk("<[box, t_*] W*, delta(r - r_h) dr> = 4 pi^2, and 4 pi in four dimensions (his (6.21)); t_* + r^2 changes "
        "neither",
        P5["P21"] == 4*sp.pi**2 and P4["P21"] == 4*sp.pi and P5["P21F"] == P5["P21"] and P4["P21F"] == P4["P21"])
    chk("W* is divergence-free (as his omega_(0)), so E_{H+,1} G = 2 iota_c and the trace weight drops out",
        P5["divW"] == 0 and P4["divW"] == 0)
    chk("eta = iota_{grad r} delta* W* at r_h = -mu^(-3/2) (dv + (3/2) dr) != 0",
        [sp.simplify(x) for x in P5["eta"][:2]] == [-mu**sp.Rational(-3, 2), -sp.Rational(3, 2)*mu**sp.Rational(-3, 2)]
        and all(x == 0 for x in P5["eta"][2:]))
    chk("<2 E_{H+,1} G delta* W*, omega*> = -12 pi^2 c_v - 8 pi^2 c_r (n = 3: -16 pi c_v - 8 pi c_r)",
        sp.expand(P5["P23"] + 12*sp.pi**2*cv + 8*sp.pi**2*cr) == 0
        and sp.expand(P4["P23"] + 16*sp.pi*P4["cv"] + 8*sp.pi*P4["cr"]) == 0)
    crv = sp.Rational(1, 2) if control == 1 else -sp.Rational(1, 2)
    P23 = P5["P23"].subs({cv: 0, cr: crv})
    sh, gh = sp.symbols("sh gh")
    F = -sp.I*sh*P5["P21"] + gh*P23
    chk("c_H = %s chi(r) dr: (6.23) = %s; -i sigma^ (6.21) + gamma^ (6.23) vanishes with Im sigma^ >= 0, gamma^ >= 0 "
        "only if (6.21) and (6.23) differ in sign, as at (sigma^, gamma^) = (i, 1) for the opposite c_H" % (crv, P23),
        P23 == 4*sp.pi**2 and P5["P21"] > 0 and sp.simplify(F.subs({sh: sp.I, gh: 1})) != 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- G7
def g7(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    res = {}
    for n in (4, 3):
        C = ch(n, "static")
        r, f, X, N = C["r"], C["f"], C["X"], C["N"]
        t = X[0]
        W = [1/r**2, SQ/(r**3*f), 0, 0, 0] if n == 4 else [1/r, mu/(r**2*f), 0, 0]
        R = sp.Function("R")(r)
        u = t - R
        BW = box(C, W)
        Cm = [sp.simplify(sp.simplify(x - u*y).subs(D(R, r, 2), D(1/f, r)).subs(D(R, r), 1/f))
              for x, y in zip(box(C, [u*q for q in W]), BW)]
        res[n] = [sp.series(x, r, sp.oo, 5).removeO() for x in Cm[:2]]
    lead5, lead4 = res[4], res[3]
    want3 = 0 if control == 1 else -1
    chk("n = 4: [box, t - r*] W* = -r^-3 dt + O(r^-4): d_sigma box(0) W* = i r^-3 dt + ..., order rho^3",
        sp.limit(lead5[0]*r**3, r, sp.oo) == want3 and sp.limit(lead5[1]*r**3, r, sp.oo) == 0)
    if control == 1:
        return chk.ok
    chk("n = 3: [box, t - r*] omega_(0) = O(r^-3), the r^-2 term cancelled (his footnote 69)",
        sp.limit(lead4[0]*r**2, r, sp.oo) == 0 and sp.limit(lead4[1]*r**2, r, sp.oo) == 0
        and sp.limit(lead4[0]*r**3, r, sp.oo) == -mu)
    rho = sp.Symbol("rho", positive=True)
    chk("the Minkowski reason: (rho d_rho - 1) rho = 0 at n = 3, (rho d_rho - 3/2) rho^2 = rho^2/2 at n = 4",
        sp.simplify(rho*D(rho, rho) - rho) == 0
        and sp.simplify(rho*D(rho**2, rho) - sp.Rational(3, 2)*rho**2 - rho**2/2) == 0)
    return chk.ok


CHECKS = [("G1 the indicial roots of box^Ups on 4+1 Minkowski, the weight 2/3: the gap (0, 2), (0, lam_s1,2) for z > 0",
           g1, 1),
          ("G2 the stationary mode equations of box on Tangherlini, symbolic l: dt and spatial parts decouple", g2, 1),
          ("G3 the identities behind the kernel for l >= 1: A(r_h) = 0 and three energy identities, positive", g3, 1),
          ("G4 l = 0: the kernel on the space smooth at the horizon and decaying is the span of W*", g4, 1),
          ("G5 delta(r - r_h) dr annihilates the range of box(0) at every l (four-dimensional control his)", g5, 1),
          ("G6 the pairings: (6.21) = 4 pi^2 (his 4 pi), eta != 0, (6.23) = 4 pi^2 for c_H = -(1/2) dr, (6.26)", g6, 1),
          ("G7 d_sigma box(0) W* = i r^-3 dt + O(r^-4): rho^3 by the dimension, by cancellation at n = 3", g7, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"gaugepot5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"gaugepot5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
