#!/usr/bin/env python3
"""bfam5.py -- the family below the top at the horizon: b4 and b5 of R7.3 computed (EQUALITY5-LAYER.md, Round 8, R8.1).

The first-degree profiles of Theorem 1's solution are H_j = sum_k env^(k)(v) c_(j,k)(r, r0, th), r0 = v - tau0 (L.13
(b)); H_(j+1) solves T(H_(j+1)) + R_X(H_j) = 0 along ell with the data i Pol^+(D_X H_j) at r = r0 (Lemma 6.2 (i)),
and d_v acts on r0: d_v (c E^(k)) = (d_(r0) c) E^(k) + c E^(k+1) (R7.3).  Here everything at mu0 = 1 (the horizon r =
1), every T^2 x Z2 x Z2-invariant component, for every angular profile a(th), b(th) of the wave H1 = A E r^(1/2)
diag(-(a + b), cos^2 a, sin^2 b) (layerlin5 N3).

Method.  The operators are taken once from layerlin5.ops on the general profile (eight free functions of (v, r, th)):
the lam^-1 and lam^0 parts of dRic^H and dD, each a list of (coefficient, component, derivative); applied to a family
vector with d_v as above.  The angle is t := tan(th/2) (th in (0, pi/2) <-> t in (0, 1); d_th = (1 + t^2)/2 d_t), so
every coefficient is rational in t, and every profile is kept in a canonical form: a sum over (wave factor a^(k),
b^(k); powers of r, log r, r0, log r0) of reduced rational functions of t.  A zero is then a zero (no trigonometric
identity left to find).  The transports: (r^(3/2) H_rr)' = -i r^(3/2) R_rr, (r^(3/2) H_vr)' = r^(3/2) (-i R_vr - H_rr/r^3),
(r^(3/2) H_vv)' = r^(3/2) (-i R_vv - 2 H_vr/r^3), (r^(1/2) H_rth)' = -i r^(1/2) R_rth, (r^(1/2) H_vth)' = r^(1/2) (-i
R_vth - H_rth/r^3), (r^(-1/2) H_kk)' = -i r^(-1/2) R_kk, integrated from r0 termwise (powers of r and log r).

  B1 (exact) H2 = c_(2,0) E: family 1 of R_X(H1), D_X(H1) vanishes; T(H2) + R_X(H1) = 0 (8 components) and i Pol(H2) +
     D_X(H1) = 0 (3), everywhere; H2 in S (no vv, vr, rr, sigma-trace).
  B2 (exact) H3 = c_(3,1) E' + c_(3,0) E with d_v acting on r0: c_(3,1) = i c_(2,0) (L.13 (b)); c_(3,0)'s vv at r = 1 is
     A d K(r0), K = -(2 r0^3 - 3 r0^2 - 2)^2/(36 r0^6) (layerlin5 N5, now with the r0-motion: L.13 (c) holds); the
     transport and gauge equations, family by family.
  B3 (exact) H4: c_(4,2) = -c_(2,0), c_(4,1) = 2i c_(3,0) (L.13 (b)'s top two families, with the r0-motion); c_(4,0)
     computed; the equations.
  B4 (exact) H5's family 1, c_(5,1): its vv, vr, rr components (all c_(5,1)_vv needs) and the equations there.
  B5 (exact, then certified) b4(r0, th) := c_(4,0),vv(1; r0, th)/(A d), b5 := c_(5,1),vv(1; r0, th)/(i A d) (so that
     the stage family below the top contributes lam (b4 + i T0 b5 + ...) to sigma, R7.3), at rho* = 1.80644... (the
     real root of 2 rho^3 - 3 rho^2 - 2); their form for every wave and for the paper's wave T = T^G - i T^F (N6); for the
     paper's wave, b4(th) on th in [0, pi/2] by interval arithmetic: where it is real, and its sign there.
  Controls: (i) the vv transport with its mass coupling 2 H_vr/r^3 halved: B2's K and the vv equation fail; (ii) d_v
     not acting on r0 (r0 frozen): c_(4,0),vv at the horizon differs (printed), so the r0-motion matters at this family.

Labels: B1-B4 and B5's forms computed (exact, sympy); B5's decision certified (interval arithmetic, mpmath.iv).
Run: python3 checks/bfam5.py
"""
import os
import sys
import textwrap
import time

import sympy as sp
from sympy.core.function import AppliedUndef

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layerlin5 as L                                                             # noqa: E402

v, r, th, r0, A, mu0, lam = L.v, L.r, L.th, L.r0, L.A, L.mu0, L.lam
I = sp.I
t = sp.Symbol('t', positive=True)
AF, BF = sp.Function('a'), sp.Function('b')
at, bt = AF(t), BF(t)
SIN, COS = 2*t/(1 + t**2), (1 - t**2)/(1 + t**2)
LOGR, LOGR0 = sp.log(r), sp.log(r0)
COMPS = [(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2), (3, 3), (4, 4)]
NAMES = {(0, 0): 'Hvv', (0, 1): 'Hvr', (1, 1): 'Hrr', (0, 2): 'Hvt', (1, 2): 'Hrt', (2, 2): 'Htt', (3, 3): 'H11',
         (4, 4): 'H22'}
BYNAME = {nm: ij for ij, nm in NAMES.items()}
T0 = time.time()
OPT = {'r0': True, 'halfmass': False}


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


def to_t(e):
    """a trigonometric expression in th as a rational function of t = tan(th/2)"""
    e = sp.expand_trig(e)
    return e.xreplace({sp.tan(th): SIN/COS, sp.cot(th): COS/SIN}).xreplace({sp.sin(th): SIN, sp.cos(th): COS})


def dth(f, n=1):
    for _ in range(n):
        f = (1 + t**2)/2*sp.diff(f, t)
    return f


# ------------------------------------------------------------------------------------------------------------ canon
def is_wave(f):
    if isinstance(f, AppliedUndef):
        return f.func in (AF, BF)
    return isinstance(f, sp.Derivative) and isinstance(f.expr, AppliedUndef) and f.expr.func in (AF, BF)


def canon(e):
    """the canonical form: sum over (wave factor, powers of r, log r, r0, log r0) of reduced rational functions of t"""
    e = sp.expand(e)
    acc = {}
    for term in sp.Add.make_args(e):
        if term == 0:
            continue
        w, rp, lr, r0p, lr0, rest = sp.Integer(1), sp.Integer(0), 0, sp.Integer(0), 0, []
        queue = list(sp.Mul.make_args(term))
        while queue:
            fac = queue.pop()
            base, ex = fac.as_base_exp()
            if base not in (r, r0, LOGR, LOGR0) and not is_wave(fac) and (fac.has(r) or fac.has(r0)):
                f2 = sp.Mul.make_args(sp.factor(fac))
                assert len(f2) > 1 or f2[0] != fac, fac
                queue.extend(f2)
                continue
            if is_wave(fac):
                assert w == 1, term
                w = fac
            elif base == r:
                rp += ex
            elif base == LOGR:
                lr += ex
            elif base == r0:
                r0p += ex
            elif base == LOGR0:
                lr0 += ex
            else:
                rest.append(fac)
        key = (w, rp, lr, r0p, lr0)
        acc.setdefault(key, []).append(sp.Mul(*rest))
    res = []
    for (w, rp, lr, r0p, lr0), cos_ in acc.items():
        co = sp.cancel(sp.together(sp.Add(*cos_)))
        if co != 0:
            res.append(co*w*r**rp*LOGR**lr*r0**r0p*LOGR0**lr0)
    return sp.Add(*res)


# ------------------------------------------------------------------------------------------------------------ operators
def parse(expr):
    expr = sp.expand(expr).subs(mu0, 1)
    reps = {}
    for d in expr.atoms(sp.Derivative):
        cnt = dict((var, n) for var, n in d.variable_count)
        reps[d] = (d.expr.func.__name__, (cnt.get(v, 0), cnt.get(r, 0), cnt.get(th, 0)))
    for f in expr.atoms(AppliedUndef):
        if f.func.__name__ in BYNAME:
            reps[f] = (f.func.__name__, (0, 0, 0))
    syms = {k: sp.Symbol('Z%d' % i) for i, k in enumerate(reps)}
    e = sp.expand(expr.xreplace(syms))
    terms = []
    for k, s_ in syms.items():
        co = e.coeff(s_)
        if co != 0:
            terms.append((canon(to_t(co)), reps[k][0], reps[k][1]))
    assert sp.expand(e.subs({s_: 0 for s_ in syms.values()})) == 0
    return terms


TAB = {}


def build_table():
    Hg = L.general_H()
    Rg, Dg = L.ops(Hg)
    for (i, j) in COMPS:
        e = sp.expand(Rg[i, j])
        TAB[('R', i, j)] = (parse(e.coeff(lam, -1)), parse(e.coeff(lam, 0)))
    for k in range(3):
        e = sp.expand(Dg[k])
        TAB[('D', k)] = (parse(e.coeff(lam, -1)), parse(e.coeff(lam, 0)))
    assert all(m == 0 for key in TAB for co, nm, (m, p, q) in TAB[key][0])      # the lam^-1 parts carry no d_v


def dd(e, var, n):
    return e if n == 0 or e == 0 else sp.diff(e, var, n)


def apply_op(terms, fam, want=None):
    """{k: expr} of the operator on H = sum_k c_k E^(k) (fam = {k: {comp: c_k}}), d_v (c E^(k)) = d_r0 c E^(k) + c
    E^(k+1); only the families in want"""
    acc = {}
    for co, nm, (m, p, q) in terms:
        comp = BYNAME[nm]
        for k, prof in fam.items():
            c = prof.get(comp, 0)
            if c == 0:
                continue
            base = None
            for i in range(m + 1):
                if want is not None and k + i not in want:
                    continue
                if not OPT['r0'] and m - i > 0:
                    continue
                if base is None:
                    base = dth(dd(c, r, p), q)
                term = sp.binomial(m, i)*dd(base, r0, m - i)
                if term != 0:
                    acc.setdefault(k + i, []).append(co*term)
    return {k: canon(sp.Add(*es)) for k, es in acc.items()}


def ops_fam(fam, want=None, comps=None, dcomps=None):
    comps = COMPS if comps is None else comps
    dcomps = range(3) if dcomps is None else dcomps
    R = {ij: apply_op(TAB[('R',) + ij][1], fam, want) for ij in comps}
    D = {k: apply_op(TAB[('D', k)][1], fam, want) for k in dcomps}
    return R, D


def lam_m1(prof):
    """T(H) and i Pol(H) (the lam^-1 parts) of a single profile"""
    T = {ij: apply_op(TAB[('R',) + ij][0], {0: prof}).get(0, 0) for ij in COMPS}
    P = {k: apply_op(TAB[('D', k)][0], {0: prof}).get(0, 0) for k in range(3)}
    return T, P


# ------------------------------------------------------------------------------------------------------------ transport
def antider(alpha, m, s, logs):
    if alpha == -1:
        return logs**(m + 1)/(m + 1)
    res = 0
    for i in range(m + 1):
        res += (-1)**i*sp.ff(m, i)*logs**(m - i)/(alpha + 1)**(i + 1)
    return s**(alpha + 1)*res


def integ(f, w):
    """int_(r0)^r f(s) s^w ds, f a canonical form"""
    e = sp.expand(f*r**w)
    res = []
    for term in sp.Add.make_args(e):
        if term == 0:
            continue
        alpha, m, rest = sp.Integer(0), 0, []
        for fac in sp.Mul.make_args(term):
            base, ex = fac.as_base_exp()
            if base == r:
                alpha += ex
            elif base == LOGR:
                m += int(ex)
            else:
                assert not fac.has(r), fac
                rest.append(fac)
        res.append(sp.Mul(*rest)*(antider(alpha, m, r, LOGR) - antider(alpha, m, r0, LOGR0)))
    return canon(sp.Add(*res))


ZSYM = None


def data(Dk):
    global ZSYM
    if ZSYM is None:
        Z, _ = L.polplus(sp.Matrix([L.Vv, L.Vr, L.Vt, 0, 0]))
        ZSYM = Z.subs(mu0, 1).applyfunc(to_t)
    sub = {L.Vv: Dk[0].subs(r, r0), L.Vr: Dk[1].subs(r, r0), L.Vt: Dk[2].subs(r, r0)}
    return (I*ZSYM.subs(r, r0)).subs(sub).applyfunc(canon)


def transport(R, Z, comps=None):
    comps = COMPS if comps is None else comps
    H = {}
    h = canon
    half = sp.Rational(1, 2) if OPT['halfmass'] else 1
    if (1, 1) in comps or (0, 1) in comps or (0, 0) in comps:
        H[(1, 1)] = h(r**sp.Rational(-3, 2)*(r0**sp.Rational(3, 2)*Z[1, 1] - I*integ(R[(1, 1)], sp.Rational(3, 2))))
        H[(0, 1)] = h(r**sp.Rational(-3, 2)*(r0**sp.Rational(3, 2)*Z[0, 1]
                                             + integ(-I*R[(0, 1)] - H[(1, 1)]/r**3, sp.Rational(3, 2))))
        H[(0, 0)] = h(r**sp.Rational(-3, 2)*(r0**sp.Rational(3, 2)*Z[0, 0]
                                             + integ(-I*R[(0, 0)] - 2*half*H[(0, 1)]/r**3, sp.Rational(3, 2))))
    if (1, 2) in comps or (0, 2) in comps:
        H[(1, 2)] = h(r**sp.Rational(-1, 2)*(r0**sp.Rational(1, 2)*Z[1, 2] - I*integ(R[(1, 2)], sp.Rational(1, 2))))
        H[(0, 2)] = h(r**sp.Rational(-1, 2)*(r0**sp.Rational(1, 2)*Z[0, 2]
                                             + integ(-I*R[(0, 2)] - H[(1, 2)]/r**3, sp.Rational(1, 2))))
    for k in (2, 3, 4):
        if (k, k) in comps:
            H[(k, k)] = h(r**sp.Rational(1, 2)*(r0**sp.Rational(-1, 2)*Z[k, k]
                                                - I*integ(R[(k, k)], sp.Rational(-1, 2))))
    return H


def next_profile(fam, want, comps=None):
    """H_(j+1)'s families in want from H_j = fam; with comps, only those components of the result (and the R, D
    components they need: vv, vr, rr need R_vv, R_vr, R_rr and D_r)"""
    if comps is None:
        R, D = ops_fam(fam, want)
    else:
        R, D = ops_fam(fam, want, comps=[(0, 0), (0, 1), (1, 1)], dcomps=[0, 1, 2])
    new = {}
    for k in want:
        Rk = {ij: sp.sympify(R[ij].get(k, 0)) for ij in R}
        Dk = [sp.sympify(D[kk].get(k, 0)) for kk in range(3)]
        new[k] = transport(Rk, data(Dk), comps)
    return new, R, D


def equations(new, R, D, k, comps=None):
    """T(c_(j+1,k)) + [R_X H_j]_k = 0 and i Pol(c_(j+1,k)) + [D_X H_j]_k = 0, exactly"""
    T, P = lam_m1(new[k])
    comps = COMPS if comps is None else comps
    eR = all(canon(T[ij] + R[ij].get(k, 0)) == 0 for ij in comps)
    eD = all(canon(P[kk] + D[kk].get(k, 0)) == 0 for kk in (range(3) if comps is COMPS else (1,)))
    return eR, eD


def same(p1, p2, factor=1, comps=None):
    comps = COMPS if comps is None else comps
    return all(canon(p1.get(ij, 0) - factor*p2.get(ij, 0)) == 0 for ij in comps)


# ------------------------------------------------------------------------------------------------------------ the wave
def wave_d():
    """d = (cos sin)^-1 d_th (cos sin tau), tau = ((a - b) - 3 (a + b) cos 2th)/sin 2th - (a + b)'"""
    tau = ((at - bt) - 3*(at + bt)*(COS**2 - SIN**2))/(2*SIN*COS) - dth(at + bt)
    return canon(dth(COS*SIN*tau)/(COS*SIN))


def H1prof():
    sq = sp.sqrt(r)
    return {(2, 2): canon(-A*sq*(at + bt)), (3, 3): canon(A*sq*COS**2*at), (4, 4): canon(A*sq*SIN**2*bt)}


def log(msg):
    sys.stderr.write("%s  [%.0f s]\n" % (msg, time.time() - T0))
    sys.stderr.flush()
