#!/usr/bin/env python3
"""bfam5.py -- the family below the top at the horizon: b4 and b5 of R7.3 computed (EQUALITY5-LAYER.md, Round 8, R8.1).

The first-degree profiles of Theorem 1's solution are H_j = sum_k env^(k)(v) c_(j,k)(r, r0, th), r0 = v - tau0 (L.13
(b)); H_(j+1) solves T(H_(j+1)) + R_X(H_j) = 0 along ell with the data i Pol^+(D_X H_j) at r = r0 (Lemma 6.2 (i)), and
d_v acts on r0: d_v (c E^(k)) = (d_(r0) c) E^(k) + c E^(k+1) (R7.3).  Everything at mu0 = 1 (the horizon r = 1), every
T^2 x Z2 x Z2-invariant component, for every angular profile a(th), b(th) of the wave H1 = A E r^(1/2) diag(-(a + b),
cos^2 a, sin^2 b) (layerlin5 N3).

Method.  The operators are taken once from layerlin5.ops on the general profile (eight free functions of (v, r, th)):
the lam^-1 and lam^0 parts of dRic^H and dD, each a list of (coefficient, component, derivative), applied to family
vectors with d_v as above.  The angle is t := tan(th/2) (th in (0, pi/2) <-> t in (0, 1); d_th = (1 + t^2)/2 d_t), so
every coefficient is rational in t, and every profile is kept in a canonical form: a sum over (wave factor a^(k),
b^(k); powers of r, log r, r0, log r0) of reduced rational functions of t, so that a zero test is an exact
cancellation.  The transports, integrated from r0 termwise in powers of r and log r: (r^(3/2) H_rr)' = -i r^(3/2) R_rr,
(r^(3/2) H_vr)' = r^(3/2) (-i R_vr - H_rr/r^3), (r^(3/2) H_vv)' = r^(3/2) (-i R_vv - 2 H_vr/r^3), (r^(1/2) H_rth)' = -i
r^(1/2) R_rth, (r^(1/2) H_vth)' = r^(1/2) (-i R_vth - H_rth/r^3), (r^(-1/2) H_kk)' = -i r^(-1/2) R_kk.

  B1 (exact) H2 = c_(2,0) E: family 1 of R_X(H1), D_X(H1) vanishes; T(H2) + R_X(H1) = 0 (8 components) and i Pol(H2) +
     D_X(H1) = 0 (3), everywhere; H2 in S (no vv, vr, rr, sigma-trace).
  B2 (exact) H3 = c_(3,1) E' + c_(3,0) E with d_v acting on r0: c_(3,1) = i c_(2,0) (L.13 (b)); both equations in both
     families; c_(3,0)'s vv at r = 1 is A d K(r0), K = -(2 r0^3 - 3 r0^2 - 2)^2/(36 r0^6) (layerlin5 N5's closed form,
     now with the r0-motion).
  B3 (exact) H4: c_(4,2) = -c_(2,0), c_(4,1) = 2i c_(3,0) (L.13 (b)'s top two families, with the r0-motion); both
     equations in families 0 and 1; c_(4,0) computed.
  B4 (exact) H5's family 1, c_(5,1): its vv, vr, rr components (all c_(5,1),vv needs) and the equations there.
  B5 (exact, then certified) the horizon values as combinations of d = div div T and Lap d (Lap the Laplacian of S^3),
     exactly, for every angular profile: c_(3,0),vv = A K d; c_(4,0),vv = A (alpha4 d + beta4 Lap d) with beta4 = -i (r0
     - 1) K/(2 r0); c_(5,1),vv = 3i c_(4,0),vv.  So b4 := c_(4,0),vv(1; r0, th)/(A d) = alpha4 + beta4 Lap d/d and b5 :=
     c_(5,1),vv/(i A d) = 3 b4 (the stage family below the top contributes lam (b4 + i T0 b5 + ...) to sigma, R7.3);
     at rho* = 1.80644... (the real root of 2 rho^3 - 3 rho^2 - 2, K's double root) beta4 = 0, so b4(rho*, th) =
     alpha4(rho*) for every th and every wave: exact in Q(rho*), enclosed by interval arithmetic, purely imaginary and
     nonzero; and for the paper's wave T = T^G - i T^F (N6) b4 avoids [0, oo) on all of th in [0, pi/2] (interval
     arithmetic in zeta = cos 2th, where b4 = N(zeta)/((1 + zeta^2)^2 |P|^2) with N polynomial).
  B6 (exact; round 9, the reader of round 8's nit 5) the chain B1-B4 at mu0 = 16 (the horizon r = 4, mu0^(1/4) = 2,
     every coefficient rational; H4's families 0 and 1), both equations in every family computed, and at the horizon,
     for every angular profile: c_(3,0),vv/A = 2^-7 K(r0/4) d, c_(4,0),vv/A = 2^-9 (alpha4(r0/4) d + beta4(r0/4) Lap d)
     and c_(5,1),vv/(i A) = 3 c_(4,0),vv/A, with alpha4, beta4 those of B5 (mu0 = 1).  So b4(4 rho*, th) = 16^(-9/4)
     b4(rho*, th)|_(mu0=1): a positive factor, the scaling mu0^(-1/4 - j/2 + k/2) of c_(j,k),vv at fixed rho = r0/sqrt
     mu0, computed at mu0 = 16; b5 = 3 b4 there too.
  Controls: (i) the vv transport with its mass coupling 2 H_vr/r^3 halved: B2's K and the vv equation fail (detected);
     (ii) d_v not acting on r0 (r0 frozen): c_(4,0),vv at the horizon differs (printed at rho*), so the r0-motion
     matters at this family; (iii) (round 9) at mu0 = 16 the transports' mass couplings left at mu0 = 1: B2's vv
     equation fails (detected).

Labels: B1-B6's forms computed (exact, sympy); B5's values at rho* and the paper's-wave decision certified (interval
arithmetic, mpmath.iv).  Run: PYTHONHASHSEED=0 python3 checks/bfam5.py   (about eighty minutes under load)
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
OPT = {'r0': True, 'halfmass': False, 'mu0': sp.Integer(1), 'tmu0': None}


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


def split(term):
    """a monomial as (wave factor, power of r, of log r, of r0, of log r0, the rest); a factor mixing r or r0 with t is
    factored first"""
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
    return w, rp, lr, r0p, lr0, sp.Mul(*rest)


def canon(e):
    """the canonical form: sum over (wave factor, powers of r, log r, r0, log r0) of reduced rational functions of t"""
    e = sp.expand(e)
    acc = {}
    for term in sp.Add.make_args(e):
        if term == 0:
            continue
        w, rp, lr, r0p, lr0, rest = split(term)
        acc.setdefault((w, rp, lr, r0p, lr0), []).append(rest)
    res = []
    for (w, rp, lr, r0p, lr0), cos_ in acc.items():
        co = sp.cancel(sp.together(sp.Add(*cos_)))
        if co != 0:
            res.append(co*w*r**rp*LOGR**lr*r0**r0p*LOGR0**lr0)
    return sp.Add(*res)


# ------------------------------------------------------------------------------------------------------------ operators
def parse(expr):
    expr = sp.expand(expr).subs(mu0, OPT['mu0'])
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
RAW = {}


def build_table():
    """the operator table at OPT['mu0'] (layerlin5's ops taken once, then specialised)"""
    if not RAW:
        Hg = L.general_H()
        Rg, Dg = L.ops(Hg)
        for (i, j) in COMPS:
            RAW[('R', i, j)] = sp.expand(Rg[i, j])
        for k in range(3):
            RAW[('D', k)] = sp.expand(Dg[k])
    TAB.clear()
    for key, e in RAW.items():
        TAB[key] = (parse(e.coeff(lam, -1)), parse(e.coeff(lam, 0)))
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
        wv, alpha, m, r0p, lr0, rest = split(term)
        res.append(wv*r0**r0p*LOGR0**lr0*rest*(antider(alpha, int(m), r, LOGR) - antider(alpha, int(m), r0, LOGR0)))
    return canon(sp.Add(*res))


ZSYM = {}


def data(Dk):
    key = OPT['mu0']
    if key not in ZSYM:
        Z, _ = L.polplus(sp.Matrix([L.Vv, L.Vr, L.Vt, 0, 0]))
        ZSYM[key] = Z.subs(mu0, key).applyfunc(to_t)
    sub = {L.Vv: Dk[0].subs(r, r0), L.Vr: Dk[1].subs(r, r0), L.Vt: Dk[2].subs(r, r0)}
    return (I*ZSYM[key].subs(r, r0)).subs(sub).applyfunc(canon)


def transport(R, Z, comps=None):
    comps = COMPS if comps is None else comps
    H = {}
    h = canon
    half = sp.Rational(1, 2) if OPT['halfmass'] else 1
    mu = OPT['mu0'] if OPT['tmu0'] is None else OPT['tmu0']        # the mass couplings mu0 H/r^3
    if (1, 1) in comps or (0, 1) in comps or (0, 0) in comps:
        H[(1, 1)] = h(r**sp.Rational(-3, 2)*(r0**sp.Rational(3, 2)*Z[1, 1] - I*integ(R[(1, 1)], sp.Rational(3, 2))))
        H[(0, 1)] = h(r**sp.Rational(-3, 2)*(r0**sp.Rational(3, 2)*Z[0, 1]
                                             + integ(-I*R[(0, 1)] - mu*H[(1, 1)]/r**3, sp.Rational(3, 2))))
        H[(0, 0)] = h(r**sp.Rational(-3, 2)*(r0**sp.Rational(3, 2)*Z[0, 0]
                                             + integ(-I*R[(0, 0)] - 2*half*mu*H[(0, 1)]/r**3, sp.Rational(3, 2))))
    if (1, 2) in comps or (0, 2) in comps:
        H[(1, 2)] = h(r**sp.Rational(-1, 2)*(r0**sp.Rational(1, 2)*Z[1, 2] - I*integ(R[(1, 2)], sp.Rational(1, 2))))
        H[(0, 2)] = h(r**sp.Rational(-1, 2)*(r0**sp.Rational(1, 2)*Z[0, 2]
                                             + integ(-I*R[(0, 2)] - mu*H[(1, 2)]/r**3, sp.Rational(1, 2))))
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


# ------------------------------------------------------------------------------------------------------------ analysis
def lap(f):
    """the Laplacian of S^3 on functions of th: (cos sin)^-1 d_th (cos sin d_th f)"""
    return canon(dth(COS*SIN*dth(f))/(COS*SIN))


def coeff_of(expr, atom):
    res = 0
    for term in sp.Add.make_args(sp.expand(expr)):
        w, rp, lr, r0p, lr0, rest = split(term)
        if w == atom:
            res += rest*r**rp*LOGR**lr*r0**r0p*LOGR0**lr0
    return res


def fit(q, basis):
    """q = sum_i c_i(r0) b_i exactly, b_i = (scalar, its highest derivative order of a); (None, the failed ratio) if
    a coefficient depends on the angle"""
    rem, cs = q, []
    for bi, order in reversed(basis):
        atom = sp.Derivative(at, (t, order)) if order else at
        c = sp.cancel(sp.together(coeff_of(rem, atom)/coeff_of(bi, atom)))
        if c.has(t):
            return None, c
        cs.append(c)
        rem = canon(rem - c*bi)
    return list(reversed(cs)), rem


# ------------------------------------------------------------------------------------------------------------ certified
import mpmath as mp                                                               # noqa: E402

iv = mp.iv
iv.dps = 50


def ivq(x):
    x = sp.Rational(x)
    return iv.mpf(int(x.p))/iv.mpf(int(x.q))


def ev(e, env):
    """(re, im) interval enclosure of a sympy expression; env maps symbols to intervals"""
    if e in env:
        return env[e], iv.mpf(0)
    if e is sp.I:
        return iv.mpf(0), iv.mpf(1)
    if e.is_Rational:
        return ivq(e), iv.mpf(0)
    if e is sp.pi:
        return iv.pi, iv.mpf(0)
    if e.is_Add:
        re_, im_ = iv.mpf(0), iv.mpf(0)
        for a_ in e.args:
            x, y = ev(a_, env)
            re_, im_ = re_ + x, im_ + y
        return re_, im_
    if e.is_Mul:
        re_, im_ = iv.mpf(1), iv.mpf(0)
        for a_ in e.args:
            x, y = ev(a_, env)
            re_, im_ = re_*x - im_*y, re_*y + im_*x
        return re_, im_
    if e.is_Pow:
        base, ex = e.args
        x, y = ev(base, env)
        if ex.is_Integer:
            n = int(ex)
            if n < 0:
                den = x*x + y*y
                x, y, n = x/den, -y/den, -n
            re_, im_ = iv.mpf(1), iv.mpf(0)
            for _ in range(n):
                re_, im_ = re_*x - im_*y, re_*y + im_*x
            return re_, im_
        assert ex.is_Rational and y == 0 and x.a > 0, e                       # a positive real base
        return iv.exp(ivq(ex)*iv.log(x)), iv.mpf(0)
    if isinstance(e, sp.log):
        x, y = ev(e.args[0], env)
        assert y == 0 and x.a > 0
        return iv.log(x), iv.mpf(0)
    raise ValueError(e)


def rho_star():
    """the real root of 2 rho^3 - 3 rho^2 - 2, enclosed by bisection (the polynomial increases on [1.8, 1.81])"""
    lo, hi = mp.mpf('1.8'), mp.mpf('1.81')
    f = lambda x: 2*x**3 - 3*x**2 - 2                                            # noqa: E731
    with mp.workdps(60):
        for _ in range(170):
            mid = (lo + hi)/2
            if f(iv.mpf(mid)).b < 0:
                lo = mid
            elif f(iv.mpf(mid)).a > 0:
                hi = mid
            else:
                break
    assert f(iv.mpf(lo)).b < 0 and f(iv.mpf(hi)).a > 0
    return iv.mpf([lo, hi])


Z = sp.Symbol('zeta', real=True)
PZ = -2*Z**5 - sp.Rational(20, 3)*Z**3 - sp.Rational(20, 3)*Z**2 - sp.Rational(38, 3)*Z + sp.Rational(4, 3)


def lapz(f):
    return 4*(1 - Z**2)*sp.diff(f, Z, 2) - 8*Z*sp.diff(f, Z)


def wave_polys():
    """the paper's wave in zeta = cos 2th (N6): d^F = sqrt2 P(zeta) w^-5, d^G = sqrt2 P(-zeta) w^-5, w^2 = 1 + zeta^2;
    Lap d^X = sqrt2 R_X w^-9 with R_X polynomials; returns (P_F, P_G, R_F, R_G)"""
    w2 = 1 + Z**2
    PF, PG = PZ, PZ.subs(Z, -Z)
    RF, RG = [sp.expand(sp.simplify(lapz(PX*w2**sp.Rational(-5, 2))*w2**sp.Rational(9, 2))) for PX in (PF, PG)]
    assert RF.is_polynomial(Z) and RG.is_polynomial(Z)
    return PF, PG, RF, RG


def decide(alpha, beta, depth=40):
    """b = alpha + beta Lap d/d for the paper's wave, as N(zeta)/((1 + zeta^2)^2 |P|^2): N = U + i V with U = a_r M +
    b_r X_r - b_i X_i, V = a_i M + b_r X_i + b_i X_r, M = (1 + zeta^2)^2 (P_G^2 + P_F^2) > 0, X = (R_G - i R_F)(P_G + i
    P_F).  Certifies on [-1, 1] that at every zeta V != 0 or U < 0 (b is never a non-negative real), by bisection with
    interval arithmetic; returns (ok, the zeta-intervals where V changes sign with U's enclosure there)"""
    PF, PG, RF, RG = wave_polys()
    M = sp.expand((1 + Z**2)**2*(PG**2 + PF**2))
    Xr, Xi = sp.expand(RG*PG + RF*PF), sp.expand(RG*PF - RF*PG)
    (ar, ai), (br, bi) = alpha, beta
    polys = [[ivq(c) for c in sp.Poly(p_, Z).all_coeffs()] for p_ in (M, Xr, Xi)]

    def hor(cs, x):
        acc = iv.mpf(0)
        for c in cs:
            acc = acc*x + c
        return acc

    def UV(x):
        m, xr, xi = (hor(cs, x) for cs in polys)
        return ar*m + br*xr - bi*xi, ai*m + br*xi + bi*xr
    stack, bad, signs = [(ivq(-1), ivq(1), 0)], [], []
    while stack:
        lo, hi, dep = stack.pop()
        U, V = UV(iv.mpf([lo.a, hi.b]))
        if V.a > 0 or V.b < 0 or U.b < 0:
            continue
        if dep >= depth:
            bad.append((lo, hi, U, V))
            break
        mid = ivq(sp.Rational(1, 2))*(lo + hi)
        mid = iv.mpf(mid.a)
        stack += [(lo, mid, dep + 1), (mid, hi, dep + 1)]
    # where V changes sign (b real): the sign of U there
    n = 2000
    prev = None
    for k in range(n + 1):
        x = ivq(sp.Rational(2*k - n, n))
        U, V = UV(x)
        sv = 1 if V.a > 0 else (-1 if V.b < 0 else 0)
        if prev is not None and sv != prev[0] and sv != 0 and prev[0] != 0:
            Ul, _ = UV(iv.mpf([prev[1].a, x.b]))
            signs.append((prev[1], x, Ul))
        prev = (sv, x)
    return not bad, bad, signs


# ------------------------------------------------------------------------------------------------------------ checks
def sizes(prof):
    return sum(len(sp.Add.make_args(e)) for e in prof.values())


def horizon(prof):
    return canon(prof.get((0, 0), 0).subs(r, sp.sqrt(OPT['mu0'])))


def at_rho(e, rs):
    """(re, im) enclosure of a function of r0 at rho*"""
    return ev(sp.expand(e), {r0: rs})


def chain(record):
    """B1-B4: H2, H3, H4 and H5's family 1; record collects the printed rows and the pass flags"""
    H1 = {0: H1prof()}
    H2, R1, D1 = next_profile(H1, [0, 1])
    b1 = all(e == 0 for e in H2[1].values()) and all(equations(H2, R1, D1, 0))
    b1 &= all(H2[0].get(ij, 0) == 0 for ij in ((0, 0), (0, 1), (1, 1))) and canon(
        H2[0][(2, 2)] + H2[0][(3, 3)]/COS**2 + H2[0][(4, 4)]/SIN**2) == 0
    H2 = {0: H2[0]}
    record['B1'] = b1
    log("B1 %s" % b1)
    H3, R2, D2 = next_profile(H2, [0, 1])
    d = wave_d()
    K = -(2*r0**3 - 3*r0**2 - 2)**2/(36*r0**6)
    b2 = same(H3[1], H2[0], I) and all(equations(H3, R2, D2, 0)) and all(equations(H3, R2, D2, 1))
    kok = canon(horizon(H3[0]) - A*d*K) == 0
    record['B2'] = b2 and kok
    record['K'] = kok
    record['R2'] = (R2, D2)
    log("B2 %s %s" % (b2, kok))
    H4, R3, D3 = next_profile(H3, [0, 1, 2])
    b3 = same(H4[2], H2[0], -1) and same(H4[1], H3[0], 2*I)
    log("B3 top families %s" % b3)
    b3 &= all(equations(H4, R3, D3, 0)) and all(equations(H4, R3, D3, 1))
    record['B3'] = b3
    log("B3 %s" % b3)
    fam = {0: H4[0], 1: H4[1]}
    cv = [(0, 0), (0, 1), (1, 1)]
    H5, R4, D4 = next_profile(fam, [1], comps=cv)
    b4 = all(equations(H5, R4, D4, 1, comps=cv))
    record['B4'] = b4
    log("B4 %s" % b4)
    return H2, H3, H4, H5


def b6(a4, b4, d, Ld):
    """B6: the chain at mu0 = 16, and the horizon values against B5's at mu0 = 1 (r0 -> r0/4, factors 2^-7, 2^-9)"""
    OPT['mu0'] = sp.Integer(16)
    build_table()
    H1 = {0: H1prof()}
    H2, R1, D1 = next_profile(H1, [0, 1])
    ok = all(e == 0 for e in H2[1].values()) and all(equations(H2, R1, D1, 0))
    H2 = {0: H2[0]}
    H3, R2, D2 = next_profile(H2, [0, 1])
    ok &= same(H3[1], H2[0], I) and all(equations(H3, R2, D2, 0)) and all(equations(H3, R2, D2, 1))
    log("B6 H3 %s" % ok)
    H4, R3, D3 = next_profile(H3, [0, 1])
    ok &= same(H4[1], H3[0], 2*I) and all(equations(H4, R3, D3, 0)) and all(equations(H4, R3, D3, 1))
    log("B6 H4 %s" % ok)
    cv = [(0, 0), (0, 1), (1, 1)]
    H5, R4, D4 = next_profile({0: H4[0], 1: H4[1]}, [1], comps=cv)
    ok &= all(equations(H5, R4, D4, 1, comps=cv))
    log("B6 H5 %s" % ok)
    c3, rem3 = fit(canon(horizon(H3[0])/A), [(d, 2), (Ld, 4)])
    c4, rem4 = fit(canon(horizon(H4[0])/A), [(d, 2), (Ld, 4)])
    c5, rem5 = fit(canon(horizon(H5[1])/(I*A)), [(d, 2), (Ld, 4)])
    K1 = -(2*r0**3 - 3*r0**2 - 2)**2/(36*r0**6)
    s4 = r0/4
    fits = c3 is not None and c4 is not None and c5 is not None and rem3 == 0 and rem4 == 0 and rem5 == 0
    scal = fits and sp.cancel(c3[0] - K1.subs(r0, s4)/2**7) == 0 and c3[1] == 0
    scal = scal and sp.cancel(c4[0] - a4.subs(r0, s4)/2**9) == 0 and sp.cancel(c4[1] - b4.subs(r0, s4)/2**9) == 0
    three = fits and sp.cancel(c5[0] - 3*c4[0]) == 0 and sp.cancel(c5[1] - 3*c4[1]) == 0
    ratio = sp.cancel(c4[0]/a4.subs(r0, s4)) if fits else None
    # control (iii): the transports' mass couplings left at mu0 = 1 while the operators are at mu0 = 16
    OPT['tmu0'] = sp.Integer(1)
    Rk = {ij: sp.sympify(R2[ij].get(0, 0)) for ij in COMPS}
    Dk = [sp.sympify(D2[kk].get(0, 0)) for kk in range(3)]
    H3m = {0: transport(Rk, data(Dk))}
    OPT['tmu0'] = None
    ctl = equations(H3m, R2, D2, 0)[0]
    OPT['mu0'] = sp.Integer(1)
    build_table()
    return ok, fits, scal, three, ratio, ctl


def nstr(p, n=16):
    with mp.workdps(50):
        return mp.nstr((mp.mpf(p.a._mpi_[0]) + mp.mpf(p.b._mpi_[1]))/2, n)


def in_rho(e):
    """an expression rational in r0, at rho* exactly: its representative of degree <= 2 in Q(rho*)"""
    x = sp.Symbol('x')
    pr = 2*x**3 - 3*x**2 - 2
    num, den = sp.fraction(sp.together(e.subs(r0, x)))
    return sp.expand(sp.rem(sp.expand(num*sp.invert(den, pr, x)), pr, x)), x


def main():
    record = {}
    ok = True
    build_table()
    H2, H3, H4, H5 = chain(record)
    d = wave_d()
    Ld = lap(d)
    out("  B1 H2 = c_(2,0) E: family 1 vanishes, T(H2) + R_X(H1) = 0 (8), i Pol(H2) + D_X(H1) = 0 (3), H2 in S: %s"
        % record['B1'])
    out("  B2 H3 with the r0-motion: c_(3,1) = i c_(2,0), both equations in families 0 and 1 (all components), and"
        " c_(3,0),vv(r = 1) = A d K(r0), K = -(2 r0^3 - 3 r0^2 - 2)^2/(36 r0^6): %s" % record['B2'])
    out("  B3 H4: c_(4,2) = -c_(2,0), c_(4,1) = 2i c_(3,0), both equations in families 0 and 1: %s" % record['B3'])
    out("  B4 H5's family 1: c_(5,1)'s vv, vr, rr and both equations there (vv, vr, rr; D_r): %s" % record['B4'])
    ok &= record['B1'] and record['B2'] and record['B3'] and record['B4']
    # B5: the fits, rho*, the paper's wave
    c3, rem3 = fit(canon(horizon(H3[0])/A), [(d, 2), (Ld, 4)])
    c4, rem4 = fit(canon(horizon(H4[0])/A), [(d, 2), (Ld, 4)])
    c5, rem5 = fit(canon(horizon(H5[1])/(I*A)), [(d, 2), (Ld, 4)])
    K = -(2*r0**3 - 3*r0**2 - 2)**2/(36*r0**6)
    good = c3 is not None and rem3 == 0 and sp.cancel(c3[0] - K) == 0 and c3[1] == 0
    good &= c4 is not None and rem4 == 0 and c5 is not None and rem5 == 0
    a4, b4 = [sp.factor(c) for c in c4]
    good &= sp.cancel(b4 + I*(r0 - 1)*K/(2*r0)) == 0
    good &= sp.cancel(c5[0] - 3*c4[0]) == 0 and sp.cancel(c5[1] - 3*c4[1]) == 0
    rep, x = in_rho(a4/I)
    rs = rho_star()
    al, be = ev(sp.expand(a4), {r0: rs}), ev(sp.expand(b4), {r0: rs})
    good &= in_rho(b4/I)[0] == 0
    mpoly = sp.minimal_polynomial(rep.subs(x, sp.CRootOf(2*x**3 - 3*x**2 - 2, 0)), x)
    okw, bad, _ = decide(al, be)
    good &= okw and al[0].a == 0 and al[0].b == 0 and al[1].b < 0
    out("  B5 at the horizon, for every angular profile: c_(3,0),vv/A = K d; c_(4,0),vv/A = alpha4 d + beta4 Lap d with"
        " alpha4 = %s, beta4 = %s = -i (r0 - 1) K/(2 r0); c_(5,1),vv/(i A) = 3 alpha4 d + 3 beta4 Lap d, so b5 = 3 b4"
        " (the fits' remainders zero).  At rho* = %s (K's double root) beta4 = 0 exactly, so b4(rho*, th) = alpha4(rho*)"
        " = i (%s) = %s i for every th and every wave with d != 0 (-i b4 a root of %s), and b5 = 3 b4 = %s i; for the"
        " paper's wave b4 avoids [0, oo) on all of th in [0, pi/2] (interval arithmetic in zeta = cos 2th): %s"
        % (a4, b4, nstr(rs, 12), rep.subs(x, sp.Symbol('rho*')), nstr(al[1]), mpoly, nstr(3*al[1]), okw))
    record['B5'] = good
    ok &= good
    out("B1-B5 %s" % ("PASS" if ok else "FAIL"))
    # control (i): the vv transport's mass coupling halved
    R2, D2 = record['R2']
    OPT['halfmass'] = True
    Rk = {ij: sp.sympify(R2[ij].get(0, 0)) for ij in COMPS}
    Dk = [sp.sympify(D2[kk].get(0, 0)) for kk in range(3)]
    H3m = {0: transport(Rk, data(Dk))}
    OPT['halfmass'] = False
    kmut = canon(horizon(H3m[0]) - A*d*K) == 0
    eqmut = equations(H3m, R2, D2, 0)[0]
    ctl1 = kmut or eqmut
    out("  control (i) the vv transport with its mass coupling halved: B2's K holds: %s, the vv equation holds: %s"
        % (kmut, eqmut))
    # control (ii): d_v not acting on r0
    OPT['r0'] = False
    H3n, _, _ = next_profile(H2, [0, 1])
    H4n, _, _ = next_profile(H3n, [0], comps=[(0, 0), (0, 1), (1, 1)])
    OPT['r0'] = True
    c4n, remn = fit(canon(horizon(H4n[0])/A), [(d, 2), (Ld, 4)])
    if c4n is None or remn != 0:
        differs = True
        out("  control (ii) r0 frozen (d_v not acting on r0): c_(4,0),vv is not of the form alpha d + beta Lap d")
    else:
        aln, bln = ev(sp.expand(c4n[0]), {r0: rs}), ev(sp.expand(c4n[1]), {r0: rs})
        differs = sp.cancel(c4n[0] - c4[0]) != 0 or sp.cancel(c4n[1] - c4[1]) != 0
        out("  control (ii) r0 frozen (d_v not acting on r0): c_(4,0),vv/A = alpha4' d + beta4' Lap d with alpha4' = %s,"
            " beta4' = %s; at rho*: alpha4' = %s + %s i, beta4' = %s + %s i; differs from B5: %s"
            % (sp.factor(c4n[0]), sp.factor(c4n[1]), nstr(aln[0]), nstr(aln[1]), nstr(bln[0]), nstr(bln[1]),
               differs))
    out("controls %s" % ("PASS (control (i) detected; (ii) differs)" if not ctl1 and differs else "FAIL"))
    ok &= not ctl1 and differs
    # B6 (round 9): mu0 = 16
    e6, fits6, scal6, three6, ratio6, ctl6 = b6(a4, b4, d, Ld)
    good6 = e6 and fits6 and scal6 and three6
    out("  B6 at mu0 = 16 (horizon r = 4): H2, H3, H4 (families 0, 1) and H5's family 1 with both equations as in B1-B4:"
        " %s; at the horizon, for every angular profile, c_(3,0),vv/A = 2^-7 K(r0/4) d and c_(4,0),vv/A = 2^-9"
        " (alpha4(r0/4) d + beta4(r0/4) Lap d), alpha4, beta4 of B5, exactly: %s (c_(4,0)'s alpha over alpha4(r0/4): %s);"
        " c_(5,1),vv/(i A) = 3 c_(4,0),vv/A: %s.  So b4(4 rho*, th) = 16^(-9/4) b4(rho*, th)|_(mu0 = 1) = %s i and b5 ="
        " 3 b4: a positive factor, the phase unchanged" % (e6, scal6, ratio6, three6, nstr(al[1]/512)))
    out("  control (iii) at mu0 = 16 with the transports' mass couplings left at mu0 = 1: B2's vv equation holds: %s"
        % ctl6)
    out("B6 %s" % ("PASS (control (iii) detected)" if good6 and not ctl6 else "FAIL"))
    ok &= good6 and not ctl6
    out("bfam5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
