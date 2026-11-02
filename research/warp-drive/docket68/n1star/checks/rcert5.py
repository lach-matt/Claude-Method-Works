#!/usr/bin/env python3
"""rcert5.py -- CERTIFY-10L5-RESULT.md round 2 (R): a certified bound on the Einstein residual of a smoothed
three-dimensional approximant, the one resid5.py computed in floating point.  Labels: certified (Arb ball arithmetic,
python-flint) for the bound; computed (floating point) for the fit that defines the approximant.

The approximant g_app (resid5.py's, exactly): on the box u in [-4, -1.1], v in [0.55, 1.6] (outside the seed's horizon
generator, converged, CERTIFY-10L5.md D399-D432), every field F of (R, m, n, W, s) is the polynomial
    F(t, sig, x) = sum_{i <= 24, j <= 30, k < 16} C_ijk T_i(t) T_j(sig) T_k(x),
t = (2 xi - xi_a - xi_b)/(xi_b - xi_a), xi = arcsinh((u + 1)/a) (a = 0.002, the run's own coordinate), sig affine in v,
C_ijk the floating-point least-squares fit in (t, sig) of resid5.py at each angular node, converted in x to Chebyshev
coefficients of the run's 16-node interpolant.  The C_ijk are floats, hence exact rationals: g_app is an explicit
metric of the class, and its Ricci tensor is enclosed rigorously.

The certified quantity: the eight null-orthonormal frame components of Ric[g_app] (resid5.py's frame: l = d_v,
nhat = e^{-2W}(d_u + beta d_x)/2, e_x, e_phi1, e_phi2), each divided by the curvature scale sqrt(K_0) = sqrt(72)/R^4,
over t, sig in [-1, 1] and x in [-x_1, x_1], x_1 = cos(pi/32) the outermost angular node: the two axis caps
|x| > x_1, where the frame's 1/(1 - x^2) factors cancel only analytically, are not covered.

The method: Taylor models of order Q = 3 in (t, sig, x).  On each box B of a tensor grid, with centre c and half-widths
h: every field's Taylor coefficients up to order Q + 2 are enclosed at c (points) and over B (balls; Chebyshev
derivatives T_i^(a) by the exact differentiation matrix at the centre, plus Markov's bound |T_n^(a+1)| <= T_n^(a+1)(1)
times h for the variation over the box); the u-derivatives by the chain rule through dt/du and d2t/du2 (themselves
Taylor jets); the frame components, generated from dnsolve5's exact symbolic Ricci tensor and printed as code on
truncated Taylor jets (exp, sqrt and reciprocals by their series), give the coefficients f_alpha (|alpha| <= Q) at c
and over B; and by Taylor's theorem with the Lagrange remainder
    sup_B |f| <= sum_{|alpha| < Q} |f_alpha(c)| h^alpha + sum_{|alpha| = Q} sup_B |f_alpha| h^alpha.

  K1 (certified) per frame component, the sup over the covered box of |Ric(e_a, e_b)|/sqrt(K_0), the largest over
     boxes of that bound; and the certified values at the box centres (max), against resid5.py's computed figures at
     the run's cell midpoints (the largest 2.46e-3, the ll component).  Pass: every bound finite and below 0.1, and the
     certified centre values within a factor 2 of resid5.py's computed maxima (the same function).
  Control: the same certificate for the approximant with W replaced by W + 0.01 v (a lapse off the solution, resid5.py's
     control): its certified centre values must exceed the approximant's tenfold.

  python3 checks/rcert5.py RUNDIR run [Nt Nsig Nx]        (run: l1_M16_800, the run resid5.py fits)
"""
import os, sys, time, math, importlib.util, itertools
import numpy as np
import sympy as sp
from flint import arb, arb_mat, ctx

ctx.prec = 128
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resid5 as RS                                                              # noqa: E402
import bondisph5 as B                                                            # noqa: E402

Q = 3
MONO = [m for d in range(Q + 1) for m in itertools.product(range(d + 1), repeat=3) if sum(m) == d]
IDX = {m: i for i, m in enumerate(MONO)}
NM = len(MONO)
PAIRS = [(i, j, IDX[tuple(a + b for a, b in zip(mi, mj))]) for i, mi in enumerate(MONO) for j, mj in enumerate(MONO)
         if sum(mi) + sum(mj) <= Q]
ZERO = arb(0)


class TJ:
    """a truncated Taylor jet of order Q in three variables, coefficients arb (f_alpha = D^alpha f / alpha!)"""
    __slots__ = ('c',)

    def __init__(self, c):
        self.c = c

    @staticmethod
    def const(a):
        return TJ([a if isinstance(a, arb) else arb(a)] + [ZERO] * (NM - 1))

    def __add__(s, o):
        if isinstance(o, TJ):
            return TJ([p + q for p, q in zip(s.c, o.c)])
        c = list(s.c); c[0] = c[0] + o; return TJ(c)
    __radd__ = __add__

    def __sub__(s, o):
        if isinstance(o, TJ):
            return TJ([p - q for p, q in zip(s.c, o.c)])
        c = list(s.c); c[0] = c[0] - o; return TJ(c)

    def __rsub__(s, o):
        c = [-p for p in s.c]; c[0] = c[0] + o; return TJ(c)

    def __neg__(s):
        return TJ([-p for p in s.c])

    def __mul__(s, o):
        if not isinstance(o, TJ):
            return TJ([p * o for p in s.c])
        a, b = s.c, o.c
        out = [ZERO] * NM
        for i, j, k in PAIRS:
            out[k] = out[k] + a[i] * b[j]
        return TJ(out)
    __rmul__ = __mul__

    def __truediv__(s, o):
        if not isinstance(o, TJ):
            return TJ([p / o for p in s.c])
        return s * trecip(o)

    def __rtruediv__(s, o):
        return trecip(s) * o

    def __pow__(s, n):
        assert isinstance(n, int)
        if n < 0:
            return trecip(s ** (-n))
        r = TJ.const(1)
        b = s
        while n:
            if n & 1:
                r = r * b
            n >>= 1
            if n:
                b = b * b
        return r


def _series(s, coefs):
    """sum_k coefs[k] N^k, N the nilpotent part of s (k <= Q)"""
    N = TJ([ZERO] + list(s.c[1:]))
    out = TJ.const(coefs[0]); Nk = TJ.const(1)
    for k in range(1, Q + 1):
        Nk = Nk * N
        out = out + Nk * coefs[k]
    return out


def trecip(s):
    if not isinstance(s, TJ):
        return 1 / (s if isinstance(s, arb) else arb(s))
    a0 = s.c[0]; r = 1 / a0
    return _series(s, [r * (-r) ** k for k in range(Q + 1)])


def texp(s):
    if not isinstance(s, TJ):
        return (s if isinstance(s, arb) else arb(s)).exp()
    e = s.c[0].exp()
    return _series(s, [e / math.factorial(k) for k in range(Q + 1)])


def tsqrt(s):
    if not isinstance(s, TJ):
        return (s if isinstance(s, arb) else arb(s)).sqrt()
    a0 = s.c[0]; r = a0.sqrt()
    co = []
    for k in range(Q + 1):
        b = arb(1)
        for j in range(k):
            b = b * (arb(1) / 2 - j) / (j + 1)
        co.append(r * b / a0 ** k)
    return _series(s, co)


# ------------------------------------------------------------------ the frame components as code on jets
class JetPrinter(sp.printing.str.StrPrinter):
    def _print_Integer(self, e):
        return 'arb(%d)' % int(e)

    def _print_Rational(self, e):
        return '(arb(%d)/arb(%d))' % (e.p, e.q)

    def _print_Float(self, e):
        raise ValueError('float in expression')

    def _print_Pow(self, e, rational=False):
        b, ex = e.as_base_exp()
        if ex == sp.Rational(1, 2):
            return 'tsqrt(%s)' % self._print(b)
        if ex == -sp.Rational(1, 2):
            return 'trecip(tsqrt(%s))' % self._print(b)
        if ex.is_Integer:
            return '(%s)**%d' % (self._print(b), int(ex))
        raise ValueError('power %s' % e)

    def _print_exp(self, e):
        return 'texp(%s)' % self._print(e.args[0])

    def _print_Function(self, e):
        raise ValueError('function %s' % e)


def frame_code():
    d5 = RS.d5
    Ric = d5.dn.ricci(d5.g, d5.C)
    R8 = [d5.tosym(Ric[i, j]) for (i, j), _ in RS.COMPS]
    x = d5.x
    R, W, m, n, s = [sp.Symbol(k) for k in ('R', 'W', 'm', 'n', 's')]
    P = (2 * (1 + x) * m - (1 - x) * n) / 3; Qq = (2 * (1 - x) * n - (1 + x) * m) / 3
    Gx = R ** 2 * sp.exp(-2 * (P + Qq)) / (4 * (1 - x ** 2)); be = (1 - x ** 2) * s
    isG = 2 * sp.sqrt(1 - x ** 2) * sp.exp(P + Qq) / R                     # 1/sqrt(Gx)
    g11 = R ** 2 * (1 + x) / 2 * sp.exp(2 * P); g22 = R ** 2 * (1 - x) / 2 * sp.exp(2 * Qq)
    Ruu, Ruv, Rux, Rvv, Rvx, Rxx, R11, R22 = R8
    e2 = sp.exp(-2 * W) / 2
    fr = [Rvv, e2 * (Ruv + be * Rvx), e2 ** 2 * (Ruu + 2 * be * Rux + be ** 2 * Rxx), Rvx * isG,
          e2 * (Rux + be * Rxx) * isG, Rxx / Gx, R11 / g11, R22 / g22]
    sc = R ** 4 / sp.sqrt(72)
    exprs = [f * sc for f in fr]
    syms = sorted(set().union(*[e.free_symbols for e in exprs]), key=str)
    rep, red = sp.cse(exprs, optimizations='basic')
    pr = JetPrinter()
    lines = ['def _frame(%s):' % ', '.join(str(a) for a in syms)]
    for v_, e in rep:
        lines.append('    %s = %s' % (v_, pr.doprint(e)))
    lines.append('    return [%s]' % ', '.join(pr.doprint(e) for e in red))
    ns = {'arb': arb, 'tsqrt': tsqrt, 'trecip': trecip, 'texp': texp}
    exec('\n'.join(lines), ns)
    return ns['_frame'], [str(a) for a in syms]


# ------------------------------------------------------------------ the approximant and its Taylor coefficients
def cheb_dmat(n):
    """exact Chebyshev differentiation in coefficient space (as dnsolve5.cheb_gauss's Dc), an arb_mat"""
    D = [[0] * n for _ in range(n)]
    for k in range(n):
        for l in range(k - 1, -1, -2):
            D[l][k] = 2 * k
        if k % 2 == 1:
            D[0][k] = k
    return arb_mat(D)


def markov(nmax, a):
    """T_n^(a)(1) = prod_{j < a} (n^2 - j^2)/(2j + 1), the sup of |T_n^(a)| on [-1, 1]"""
    out = []
    for nn in range(nmax):
        v = arb(1)
        for j in range(a):
            v = v * arb(nn * nn - j * j) / (2 * j + 1)
        out.append(v)
    return out


def basis_jets(centres, half, n, order):
    """for each centre: enclosures over [c - half, c + half] of T_i^(a)(.)/a!, a <= order, as lists [a][i]; and the
    point values at c (half = 0 gives points)"""
    D = cheb_dmat(n)
    DT = D.transpose()
    out = []
    mk = [markov(n, a + 1) for a in range(order + 1)]
    for c in centres:
        th = arb(c).acos()
        T = arb_mat([[(th * k).cos()] for k in range(n)])
        vecs = [T]
        for a in range(order + 1):
            vecs.append(DT * vecs[-1])
        per = []
        for a in range(order + 1):
            f = arb(math.factorial(a))
            row = []
            for i in range(n):
                val = vecs[a][i, 0]
                if half:
                    val = val + arb(0, 1) * mk[a][i] * arb(half)
                row.append(val / f)
            per.append(row)
        out.append(per)
    return out


def contract(C, Tt, Ss, Xx, order):
    """F_abc over the tensor grid: C (n_t, n_s, n_x) floats; Tt[p][a][i] etc.  Returns dict (a,b,c) -> array of arb
    shaped (Nt, Ns, Nx)"""
    nt, ns_, nx = C.shape
    Cm = arb_mat([[float(C[i, j, k]) for j in range(ns_) for k in range(nx)] for i in range(nt)])
    out = {}
    Nt, Ns, Nx = len(Tt), len(Ss), len(Xx)
    S_mats = {b: arb_mat([[Ss[q][b][j] for j in range(ns_)] for q in range(Ns)]) for b in range(order + 1)}
    X_mats = {c: arb_mat([[Xx[r][c][k] for r in range(Nx)] for k in range(nx)]) for c in range(order + 1)}
    for a in range(order + 1):
        Ta = arb_mat([[Tt[p][a][i] for i in range(nt)] for p in range(Nt)])
        TC = Ta * Cm                                          # (Nt, ns*nx)
        for p in range(Nt):
            Mp = arb_mat([[TC[p, j * nx + k] for k in range(nx)] for j in range(ns_)])
            for b in range(order + 1 - a):
                SM = S_mats[b] * Mp                           # (Ns, nx)
                for c in range(order + 1 - a - b):
                    V = SM * X_mats[c]                        # (Ns, Nx)
                    arr = out.setdefault((a, b, c), np.empty((Nt, Ns, Nx), dtype=object))
                    for q in range(Ns):
                        for r in range(Nx):
                            arr[p, q, r] = V[q, r]
    return out


def field_jet(Fc, p, q, r):
    """the order-(Q + 2) Taylor jet of a field at one box (or point): dict alpha -> arb"""
    return {al: Fc[al][p, q, r] for al in Fc}


def dshift(J, axis):
    """derivative along axis of a jet given as dict alpha -> coefficient (f_alpha = D^alpha f/alpha!)"""
    out = {}
    for al, v in J.items():
        if al[axis] == 0:
            continue
        b = list(al); b[axis] -= 1
        out[tuple(b)] = v * al[axis]
    return out


def to_tj(J):
    return TJ([J.get(m, ZERO) for m in MONO])


def inputs(jets, geo, tc, sc, xc, box):
    """the named inputs of the frame code (fields and their u, v, x derivatives up to second order) as TJ jets"""
    hxi, a, psi = geo['hxi'], geo['a'], geo['psi']
    xi0 = geo['xa'] + (tc + 1) * hxi
    lin = lambda c0, ax: TJ([c0] + [arb(1) if MONO[i] == tuple(int(k == ax) for k in range(3)) else ZERO
                                    for i in range(1, NM)])
    xiJ = lin(xi0, 0) * 1
    xiJ = TJ([xiJ.c[0]] + [cc * hxi for cc in xiJ.c[1:]])
    eP, eM = texp(xiJ), texp(-xiJ)
    ch = (eP + eM) * (arb(1) / 2); shh = (eP - eM) * (arb(1) / 2)
    phi1 = trecip(ch * (hxi * a))
    phi2 = -(phi1 * phi1) * (shh * trecip(ch)) * hxi
    out = {'x': lin(xc, 2)}
    for f, J in jets.items():
        Dt, Ds, Dx = dshift(J, 0), dshift(J, 1), dshift(J, 2)
        out[f] = to_tj(J)
        out[f + '_u'] = phi1 * to_tj(Dt)
        out[f + '_v'] = to_tj(Ds) * psi
        out[f + '_x'] = to_tj(Dx)
        out[f + '_uu'] = phi1 * phi1 * to_tj(dshift(Dt, 0)) + phi2 * to_tj(Dt)
        out[f + '_uv'] = phi1 * to_tj(dshift(Dt, 1)) * psi
        out[f + '_ux'] = phi1 * to_tj(dshift(Dt, 2))
        out[f + '_vv'] = to_tj(dshift(Ds, 1)) * (psi * psi)
        out[f + '_vx'] = to_tj(dshift(Ds, 2)) * psi
        out[f + '_xx'] = to_tj(dshift(Dx, 2))
    return out


def certify(Z, frame, names, Nt, Ns, Nx, wshift=0.0, log=None):
    args = [-4.0, -1.1, 0.55, 1.6, 24, 30]
    coef, err, geo = RS.fit(Z, *args)
    M = len(Z['x'])
    xn = Z['x']
    Tm = np.cos(np.outer(np.arange(M), np.arccos(xn)))
    Tinv = np.linalg.inv(Tm.T)
    C3 = {}
    for f in RS.NAMES:
        C3[f] = np.einsum('km,ijm->ijk', Tinv, coef[f])
    hv = (args[3] - args[2]) / 2
    if wshift:                                   # W + wshift v, v = va + (sig + 1) hv: exact in the Chebyshev basis
        C3['W'] = C3['W'].copy()
        C3['W'][0, 0, 0] += wshift * (args[2] + hv); C3['W'][0, 1, 0] += wshift * hv
    g = dict(hxi=(geo['xb'] - geo['xa']) / 2, a=RS.A_GRID, psi=1 / hv, xa=geo['xa'])
    x1 = float(np.cos(np.pi / (2 * M)))
    order = Q + 2
    ht, hs, hx = 1.0 / Nt, 1.0 / Ns, x1 / Nx
    tcs = [-1 + (2 * p + 1) * ht for p in range(Nt)]
    scs = [-1 + (2 * q + 1) * hs for q in range(Ns)]
    xcs = [-x1 + (2 * r + 1) * hx for r in range(Nx)]
    t0 = time.time()
    fld_box, fld_pt = {}, {}
    for which, store, hh in (('box', fld_box, (ht, hs, hx)), ('pt', fld_pt, (0, 0, 0))):
        Tt = basis_jets(tcs, hh[0], C3['R'].shape[0], order)
        Ss = basis_jets(scs, hh[1], C3['R'].shape[1], order)
        Xx = basis_jets(xcs, hh[2], M, order)
        for f in RS.NAMES:
            store[f] = contract(C3[f], Tt, Ss, Xx, order)
    if log:
        log('  enclosures of the fields\' Taylor coefficients on %d boxes: %.0f s' % (Nt * Ns * Nx, time.time() - t0))
    hpow = {m: arb(ht) ** m[0] * arb(hs) ** m[1] * arb(hx) ** m[2] for m in MONO}
    sup = [arb(0)] * 8; cen = [arb(0)] * 8
    t1 = time.time()
    for p, q, r in itertools.product(range(Nt), range(Ns), range(Nx)):
        jb = {f: field_jet(fld_box[f], p, q, r) for f in RS.NAMES}
        jp = {f: field_jet(fld_pt[f], p, q, r) for f in RS.NAMES}
        ib = inputs(jb, g, arb(tcs[p], ht), scs[q], arb(xcs[r], hx), True)
        ip = inputs(jp, g, arb(tcs[p]), scs[q], arb(xcs[r]), False)
        fb = frame(*[ib[k] for k in names])
        fp = frame(*[ip[k] for k in names])
        for k8 in range(8):
            bnd = arb(0)
            for i, m in enumerate(MONO):
                cc = fp[k8].c[i] if sum(m) < Q else fb[k8].c[i]
                bnd = bnd + abs(cc) * hpow[m]
            up = arb(bnd.mid() + bnd.rad())
            if not up.is_finite():
                sup[k8] = arb('inf')
            elif up > sup[k8]:
                sup[k8] = up
            cv = abs(fp[k8].c[0]); cu = arb(cv.mid() + cv.rad())
            if cu > cen[k8]:
                cen[k8] = cu
    if log:
        log('  Taylor models on the boxes: %.0f s' % (time.time() - t1))
    return sup, cen, err


def main():
    rundir, run = sys.argv[1], sys.argv[2]
    Nt, Ns, Nx = (int(a) for a in sys.argv[3:6]) if len(sys.argv) > 5 else (16, 16, 8)
    t0 = time.time()
    log = lambda s: print(s, flush=True)
    frame, names = frame_code()
    log('frame code generated (%.0f s); Taylor order %d, %d boxes (%d x %d x %d) in (t, sig, x)' % (
        time.time() - t0, Q, Nt * Ns * Nx, Nt, Ns, Nx))
    Z = B.load(os.path.join(rundir, run + '.npz'))
    labs = [lab for _, lab in RS.COMPS]
    frl = ['ll', 'ln', 'nn', 'lx', 'nx', 'xx', '11', '22']
    sup, cen, err = certify(Z, frame, names, Nt, Ns, Nx, log=log)
    log('  fit error per field (computed): %s' % ', '.join('%s %.1e' % (k, e) for k, e in err.items()))
    log('K1 certified sup over the box of |Ric(e_a, e_b)|/sqrt(K_0), and the certified max at the box centres:')
    for k, a, c in zip(frl, sup, cen):
        log('     %s: sup <= %s; at the centres <= %s' % (k, a.str(3), c.str(3)))
    resid_comp = {'ll': 2.46e-3, 'ln': 1.53e-4, 'nn': 7.46e-5, 'lx': 4.25e-4, 'nx': 2.47e-5, 'xx': 2.02e-4,
                  '11': 6.24e-5, '22': 2.14e-4}
    good = all(a < arb('0.1') for a in sup) and all(
        arb(resid_comp[k]) / 2 < c < arb(resid_comp[k]) * 2 for k, c in zip(frl, cen) if resid_comp[k] > 1e-4)
    log('K1 %s (every bound below 0.1; centre values within a factor 2 of resid5.py\'s computed maxima where those '
        'exceed 1e-4)' % ('PASS' if good else 'FAIL'))
    supc, cenc, _ = certify(Z, frame, names, max(Nt // 2, 2), max(Ns // 2, 2), max(Nx // 2, 2), wshift=0.01)
    worst, worstc = max(cen), max(cenc)
    ctl = worstc > 10 * worst
    log('  control (W + 0.01 v): certified centre values up to %s against %s -> %s' % (
        worstc.str(3), worst.str(3), 'fails (good)' if ctl else 'passed (bad)'))
    ok = good and ctl
    log('rcert5: %s (%.0f s)' % ('all checks pass' if ok else 'FAILURES', time.time() - t0))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
