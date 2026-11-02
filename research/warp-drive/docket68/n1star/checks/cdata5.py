#!/usr/bin/env python3
"""cdata5.py -- CERTIFY-10L5-RESULT.md section 2: a certified bound on the Raychaudhuri constraint for an explicit
approximant of the characteristic data on dnsolve5.py's outgoing data cone u = -R0 = -10, at both seeds.
Labels: certified (Arb ball arithmetic, python-flint) where stated; computed (floating point) for the fit.

The data cone.  dnsolve5 prescribes on u = -10: m = y^3 G/2, n = y^3 F/2 (y = r^(-1/2), r Tangherlini's areal radius
along the cone, F = lam A env(v) h(x) sin(v/lam), G = ... cos, h = sqrt(2/(1 + x^2)), env = sin^4(pi (v - 1/2)/3) on
(1/2, 7/2), A = 1), W = Tangherlini's, (1/2) ln(f(r)/(2 f(10))), f = 1 - 1/r^2, and solves the Raychaudhuri
constraint Ric_vv = 0 (sectexp5.py X1) for R.  Along the cone r is a smooth parameter with dr/dv = f/2 and
v(r) = 2(r - 10) + ln(11 (r - 1)/(9 (r + 1))) exactly, W_v = 1/(2 r^3), and Ric_vv = 0 reads
    R_rr = -(4/(3 f^2)) R s(r, x),   s := P_v^2 + Q_v^2 + (P_v + Q_v)^2,   P_v = (f/2) d_r P, ...,
    Ric_vv = -(3/R) (f/2)^2 R_rr - s.
The approximant R_app:  R = r where v <= 1/2 (there s = 0 and Tangherlini is exact); on v in [1/2, 7/2] a tensor
Chebyshev series in (r, x) of degrees (Dr, Dx), fitted to a floating-point solution of the ODE and corrected by an
affine function of r so that R = r and R_r = 1 at v = 1/2; for v >= 7/2 (s = 0 again) the affine continuation
R = R(r_e, x) + R_r(r_e, x)(r - r_e), which solves R_rr = 0 exactly.  So g_app on the cone is C^1 in r with a jump in
R_rr at v = 1/2 and 7/2 as small as the fit, and Ric_vv[g_app] = 0 exactly outside [1/2, 7/2].

  C1 (certified) sup over v in [1/2, 7/2], x in [-1, 1] of |Ric_vv[g_app]| <= delta, by the mean-value form on a grid
     of boxes: Ric_vv(box) is enclosed by its value at the box's centre (ball arithmetic) plus its gradient, enclosed
     over the box by forward-mode jets in ball arithmetic, times the box's half-widths; Chebyshev polynomials over an
     interval by Markov's inequality |T_k'| <= k^2.  Also certified: sup of s over the cone (the size of the terms
     that cancel in Ric_vv).
  C2 (certified; added in round 2, the verifier having found the claim made but not computed) the jumps of R_rr at
     the two ends, v = 1/2 and 7/2: sup over x of |R_app,rr(r_s, x)| and |R_app,rr(r_e, x)| (R_rr = 0 on the other
     side of each end), enclosed on 256 boxes in x by the same Markov bound, beside the certified sup of |R_app,rr|
     over the cone (from C1's boxes).  Control: the perturbed approximant of C1's control has jumps at least 100 times
     larger.
     The enclosure is of second order in the box size (the mean-value form; measured: halving both box widths divides
     the bound by 4.0), so the certified sup is far above the residual itself, which the certified point values at
     the box centres show.
  Control: the same certificate for R_app with its fitted coefficients perturbed by 1e-6 (a non-solution), on a
     coarser box grid, must give a bound at least 100 times larger, so the bound sees the approximant.

  python3 checks/cdata5.py [seed]        (seed 1: lam = 1; seed 2: lam = 10/sqrt(1000) = 1/sqrt(10); default both)
"""
import sys, time, warnings
import numpy as np
import sympy as sp
from sympy.printing.pycode import PythonCodePrinter
from flint import arb, ctx
from numpy.polynomial import chebyshev as Ch
from scipy.integrate import solve_ivp
warnings.filterwarnings('ignore')
ctx.prec = 128
R0 = 10


class J:
    """a forward-mode jet: value and gradient in (r, x), all arb balls"""
    __slots__ = ('v', 'a', 'b')

    def __init__(s, v, a=None, b=None):
        s.v = v if isinstance(v, arb) else arb(v)
        s.a = arb(0) if a is None else a
        s.b = arb(0) if b is None else b

    @staticmethod
    def c(o):
        return o if isinstance(o, J) else J(arb(o) if not isinstance(o, arb) else o)

    def __add__(s, o):
        o = J.c(o); return J(s.v + o.v, s.a + o.a, s.b + o.b)
    __radd__ = __add__

    def __sub__(s, o):
        o = J.c(o); return J(s.v - o.v, s.a - o.a, s.b - o.b)

    def __rsub__(s, o):
        return J.c(o) - s

    def __neg__(s):
        return J(-s.v, -s.a, -s.b)

    def __mul__(s, o):
        o = J.c(o); return J(s.v * o.v, s.a * o.v + s.v * o.a, s.b * o.v + s.v * o.b)
    __rmul__ = __mul__

    def __truediv__(s, o):
        o = J.c(o); q = s.v / o.v
        return J(q, (s.a - q * o.a) / o.v, (s.b - q * o.b) / o.v)

    def __rtruediv__(s, o):
        return J.c(o) / s

    def __pow__(s, k):
        if isinstance(k, J) or not float(k).is_integer():
            raise ValueError('integer powers only')
        k = int(k)
        if k < 0:
            return J(arb(1)) / (s ** (-k))
        out = J(arb(1))
        for _ in range(k):
            out = out * s
        return out


def jfun(f, df):
    def g(z):
        if isinstance(z, J):
            d = df(z.v)
            return J(f(z.v), d * z.a, d * z.b)
        return f(z if isinstance(z, arb) else arb(z))
    return g


jsin = jfun(lambda t: t.sin(), lambda t: t.cos())
jcos = jfun(lambda t: t.cos(), lambda t: -t.sin())
jlog = jfun(lambda t: t.log(), lambda t: 1 / t)
jsqrt = jfun(lambda t: t.sqrt(), lambda t: 1 / (2 * t.sqrt()))


def data_exprs(lam_sym):
    """P_r and Q_r on the cone as sympy expressions in (r, x) for v in (1/2, 7/2); also v(r)"""
    r, x = sp.symbols('r x', positive=True)
    v = 2*(r - R0) + sp.log(sp.Integer(11)*(r - 1)/(sp.Integer(9)*(r + 1)))
    w = (v - sp.Rational(1, 2))/3
    env = sp.sin(sp.pi*w)**4
    h = sp.sqrt(2/(1 + x**2))
    Fd = lam_sym*env*h*sp.sin(v/lam_sym); Gd = lam_sym*env*h*sp.cos(v/lam_sym)
    y3 = r**sp.Rational(-3, 2)
    m = y3*Gd/2; n = y3*Fd/2
    P = (2*(1 + x)*m - (1 - x)*n)/3; Q = (2*(1 - x)*n - (1 + x)*m)/3
    return r, x, v, sp.diff(P, r), sp.diff(Q, r)


class ArbPrinter(PythonCodePrinter):
    def _print_Rational(self, e):
        return 'arb(%d)/arb(%d)' % (e.p, e.q)

    def _print_Integer(self, e):
        return 'arb(%d)' % e.p

    def _print_Pi(self, e):
        return 'arb.pi()'

    def _print_Pow(self, e, rational=False):
        b, ex = e.as_base_exp()
        if ex == sp.Rational(1, 2):
            return 'jsqrt(%s)' % self._print(b)
        if ex == -sp.Rational(1, 2):
            return '(arb(1)/jsqrt(%s))' % self._print(b)
        if ex.is_Rational and ex.q == 2:
            return '(jsqrt(%s)**%d)' % (self._print(b), ex.p)
        if ex.is_Integer:
            return '(%s)**%d' % (self._print(b), int(ex))
        raise ValueError('power %s' % e)

    def _print_Function(self, e):
        name = {'sin': 'jsin', 'cos': 'jcos', 'log': 'jlog'}[e.func.__name__]
        return '%s(%s)' % (name, ', '.join(self._print(a) for a in e.args))

    _print_sin = _print_cos = _print_log = _print_Function


def compile_arb(expr, args):
    code = 'def _f(%s):\n    return %s\n' % (', '.join(str(a) for a in args), ArbPrinter().doprint(expr))
    ns = {'arb': arb, 'jsin': jsin, 'jcos': jcos, 'jlog': jlog, 'jsqrt': jsqrt}
    exec(code, ns)
    return ns['_f']


def r_of_v(vv):
    """Tangherlini r along u = -10 at advanced time v (float, Newton on v(r))"""
    r = R0 + 0.5 * vv
    for _ in range(60):
        g = 2 * (r - R0) + np.log(11 * (r - 1) / (9 * (r + 1))) - vv
        r -= g / (2 / (1 - 1 / r ** 2))
    return r


def fit(lam_f, Pr, Qr, Dr, Dx, rs, re):
    """floating-point solution of R_rr = -(4/(3 f^2)) R s at Chebyshev nodes in (r, x); tensor Chebyshev coefficients"""
    r, x = sp.symbols('r x', positive=True)
    fP = sp.lambdify((r, x), Pr, 'numpy'); fQ = sp.lambdify((r, x), Qr, 'numpy')
    xn = np.cos((np.arange(Dx + 1) + 0.5) * np.pi / (Dx + 1))
    rn = 0.5 * (rs + re) + 0.5 * (re - rs) * np.cos((np.arange(Dr + 1) + 0.5) * np.pi / (Dr + 1))
    vals = np.zeros((Dr + 1, Dx + 1))
    for k, xx in enumerate(xn):
        def rhs(rr, Y):
            f = 1 - 1 / rr ** 2
            Pv, Qv = f / 2 * fP(rr, xx), f / 2 * fQ(rr, xx)
            s = Pv ** 2 + Qv ** 2 + (Pv + Qv) ** 2
            return [Y[1], -4 / (3 * f ** 2) * Y[0] * s]
        sol = solve_ivp(rhs, (rs, re), [rs, 1.0], rtol=1e-13, atol=1e-15, dense_output=True, method='DOP853')
        vals[:, k] = sol.sol(rn)[0]
    tr = (2 * rn - rs - re) / (re - rs)
    Vr = Ch.chebvander(tr, Dr); Vx = Ch.chebvander(xn, Dx)
    C = np.linalg.solve(Vr, np.linalg.solve(Vx, vals.T).T)
    return C


def arb_coeffs(C):
    return [[arb(float(C[i, j])) for j in range(C.shape[1])] for i in range(C.shape[0])]


def cheb_der(Ca, axis, scale):
    """exact (ball) Chebyshev derivative of a coefficient table along axis, times scale"""
    Cn = [row[:] for row in Ca] if axis == 0 else [[c for c in row] for row in Ca]
    if axis == 1:
        Cn = [list(col) for col in zip(*Cn)]
    n = len(Cn)
    out = [[arb(0)] * len(Cn[0]) for _ in range(max(n - 1, 1))]
    for j in range(len(Cn[0])):
        d = [arb(0)] * (n + 1)
        for k in range(n - 1, 0, -1):
            d[k - 1] = d[k + 1] + 2 * k * Cn[k][j]
        d[0] = d[0] / 2
        for k in range(n - 1):
            out[k][j] = d[k] * scale
    if axis == 1:
        out = [list(col) for col in zip(*out)]
    return out


def tvec(t, t_rad, n):
    """balls enclosing T_k over [t - t_rad, t + t_rad], t an arb ball (Markov: |T_k'| <= k^2 on [-1, 1]), k < n"""
    t = t if isinstance(t, arb) else arb(t)
    vals = [arb(1), t]
    for k in range(2, n):
        vals.append(2 * t * vals[-1] - vals[-2])
    vals = vals[:n]
    if t_rad == 0:
        return vals
    return [vals[k] + arb(0, min(k * k * t_rad, 2.0) * (1 + 1e-12)) for k in range(n)]


def ser(Ca, A, Bv):
    s = arb(0)
    for i, row in enumerate(Ca):
        if i >= len(A):
            break
        acc = arb(0)
        for j, c in enumerate(row):
            if j >= len(Bv):
                break
            acc += c * Bv[j]
        s += A[i] * acc
    return s


def certify(seed, Dr, Dx, Nr, Nx, perturb=0.0):
    lam = sp.Integer(1) if seed == 1 else 1 / sp.sqrt(10)
    lam_f = float(lam)
    r, x, vexpr, Pr, Qr = data_exprs(lam)
    rs, re = r_of_v(0.5), r_of_v(3.5)
    C = fit(lam_f, Pr, Qr, Dr, Dx, rs, re)
    if perturb:
        C = C + perturb * np.random.default_rng(1).standard_normal(C.shape) * (np.arange(Dr + 1)[:, None] > 2)
    fPr = compile_arb(Pr, [r, x]); fQr = compile_arb(Qr, [r, x])
    # exact interval endpoints as balls: rs, re are floats (exact dyadics); the box grid is built on them
    hr = (arb(re) - arb(rs)) / 2
    Ca = arb_coeffs(C)
    # affine correction so that R = r and R_r = 1 at r = rs (t = -1)
    Tm1 = [arb((-1) ** k) for k in range(Dr + 1)]
    Cr = cheb_der(Ca, 0, 1 / hr)
    Crr = cheb_der(Cr, 0, 1 / hr)
    Crrr = cheb_der(Crr, 0, 1 / hr)
    Crrx = cheb_der(Crr, 1, arb(1))
    Cx = cheb_der(Ca, 1, arb(1))
    # value and slope at r = rs as Chebyshev series in x: c0(x) = sum_i C_i(x) (-1)^i
    c0 = [sum((Ca[i][j] * Tm1[i] for i in range(Dr + 1)), arb(0)) for j in range(Dx + 1)]
    c1 = [sum((Cr[i][j] * Tm1[i] for i in range(len(Cr))), arb(0)) for j in range(Dx + 1)]
    c0x = cheb_der([c0], 1, arb(1))[0]
    c1x = cheb_der([c1], 1, arb(1))[0]
    # R_app = series + a(x) + b(x) (r - rs),  a = rs - c0(x),  b = 1 - c1(x): R_rr unchanged
    t0 = time.time()
    delta, smax, n, cmax, rrmax = arb(0), arb(0), 0, arb(0), arb(0)
    worst_at = None
    rr_edges = [arb(rs) + 2 * hr * arb(k) / Nr for k in range(Nr + 1)]
    for ir in range(Nr):
        r_lo, r_hi = rr_edges[ir], rr_edges[ir + 1]
        rc = (r_lo + r_hi) / 2; rrad = (r_hi - r_lo) / 2
        rc = arb(rc.mid()); rrad_up = arb(rrad.mid()) * (1 + 1e-10) + rrad.rad() * 2
        tc = (rc - (arb(rs) + hr)) / hr
        trad = rrad_up / hr
        A_pt = tvec(tc, 0, Dr + 1)
        A_bx = tvec(tc, float(trad.mid()) * (1 + 1e-9) + float(trad.rad()) * 2, Dr + 1)
        for ix in range(Nx):
            x_lo, x_hi = -1 + 2 * ix / Nx, -1 + 2 * (ix + 1) / Nx
            xc, xrad = 0.5 * (x_lo + x_hi), 0.5 * (x_hi - x_lo)
            B_pt = tvec(xc, 0, Dx + 1); B_bx = tvec(xc, xrad, Dx + 1)

            rrbox = abs(ser(Crr, A_bx, B_bx))
            rru = arb(rrbox.mid() + rrbox.rad())
            rrmax = rru if rru > rrmax else rrmax

            def ric(Aa, Bb, rj, xj, point):
                """Ric_vv as a jet: point -- at the centre (gradient unused); else over the box (value and gradient
                enclosures over the box)"""
                cx0 = sum((c0[j] * Bb[j] for j in range(Dx + 1)), arb(0))
                cx1 = sum((c1[j] * Bb[j] for j in range(Dx + 1)), arb(0))
                Rv = ser(Ca, Aa, Bb) + (arb(rs) - cx0) + (1 - cx1) * (rj.v - arb(rs))
                Rrr = ser(Crr, Aa, Bb)
                if point:
                    Rj, Rrrj = J(Rv), J(Rrr)
                else:
                    Rr = ser(Cr, Aa, Bb) + (1 - cx1)
                    Rx = (ser(Cx, Aa, Bb) - sum((c0x[j] * Bb[j] for j in range(len(c0x))), arb(0))
                          - sum((c1x[j] * Bb[j] for j in range(len(c1x))), arb(0)) * (rj.v - arb(rs)))
                    Rj = J(Rv, Rr, Rx)
                    Rrrj = J(Rrr, ser(Crrr, Aa, Bb), ser(Crrx, Aa, Bb))
                f = 1 - 1 / (rj * rj)
                Pv = f / 2 * fPr(rj, xj); Qv = f / 2 * fQr(rj, xj)
                s = Pv * Pv + Qv * Qv + (Pv + Qv) * (Pv + Qv)
                return -(3 / Rj) * (f / 2) * (f / 2) * Rrrj - s, s
            rj_pt, xj_pt = J(rc), J(arb(xc))
            val, s_pt = ric(A_pt, B_pt, rj_pt, xj_pt, True)
            rj_bx = J(arb(rc.mid(), rrad_up.mid()), arb(1), arb(0))
            xj_bx = J(arb(xc, xrad), arb(0), arb(1))
            gb, s_bx = ric(A_bx, B_bx, rj_bx, xj_bx, False)
            cv = abs(val.v)
            cmax = arb(cv.mid() + cv.rad()) if cv > cmax else cmax
            encl = abs(val.v) + abs(gb.a) * rrad_up + abs(gb.b) * arb(xrad)
            up = arb(encl.mid() + encl.rad())
            if up > delta:
                delta, worst_at = up, (float(rc.mid()), xc)
            sb = abs(s_bx.v)
            su = arb(sb.mid() + sb.rad())
            smax = su if su > smax else smax
            n += 1
    # C2: the jumps of R_rr at t = -1 (r = rs) and t = +1 (r = re), certified over x on 256 boxes
    jumps = []
    for sgn in (-1, 1):
        row = [sum((Crr[i][j] * arb(sgn ** i) for i in range(len(Crr))), arb(0)) for j in range(Dx + 1)]
        jm = arb(0)
        for ix in range(256):
            xc, xrad = -1 + (2 * ix + 1) / 256, 1 / 256
            val = abs(sum((row[j] * b for j, b in enumerate(tvec(xc, xrad, Dx + 1))), arb(0)))
            up = arb(val.mid() + val.rad())
            jm = up if up > jm else jm
        jumps.append(jm)
    return dict(delta=delta, smax=smax, cmax=cmax, boxes=n, seconds=time.time() - t0, worst_at=worst_at, rs=rs, re=re,
                lam=lam_f, jumps=jumps, rrmax=rrmax)


def main():
    seeds = [int(a) for a in sys.argv[1:]] or [1, 2]
    ok = True
    for seed in seeds:
        Dr, Dx = (40, 28) if seed == 1 else (64, 28)
        Nr, Nx = (192, 64) if seed == 1 else (288, 64)
        res = certify(seed, Dr, Dx, Nr, Nx)
        print('seed %d (lam = %.6f): r in [%.6f, %.6f] (v in [1/2, 7/2]), degrees (%d, %d), %d boxes, %.0f s'
              % (seed, res['lam'], res['rs'], res['re'], Dr, Dx, res['boxes'], res['seconds']), flush=True)
        print('  C1 certified: sup |Ric_vv[g_app]| <= %s' % res['delta'].str(4), flush=True)
        print('     sup s <= %s (the terms that cancel); worst box near (r, x) = (%.4f, %.3f)'
              % (res['smax'].str(4), *res['worst_at']), flush=True)
        print('     certified pointwise at the %d box centres: max |Ric_vv| <= %s' % (res['boxes'], res['cmax'].str(4)),
              flush=True)
        good = res['delta'] < res['smax'] * arb('0.05')
        ctl = certify(seed, Dr, Dx, Nr // 4, Nx // 4, perturb=1e-6)
        fails = ctl['delta'] > 100 * res['delta']
        print('  control (coefficients perturbed by 1e-6): bound %s -> %s' % (
            ctl['delta'].str(4), 'fails (good)' if fails else 'passed (bad)'), flush=True)
        ok &= good and fails
        print('  C1 %s (bound below 5e-2 of the terms)' % ('PASS' if good else 'FAIL'), flush=True)
        j0, j1 = res['jumps']
        jgood = j0 < res['rrmax'] * arb('1e-3') and j1 < res['rrmax'] * arb('1e-3')
        jctl = min(ctl['jumps'][0], ctl['jumps'][1]) > 100 * max(j0, j1)
        print('  C2 certified: jump of R_rr at v = 1/2: <= %s; at v = 7/2: <= %s; sup |R_rr| on the cone <= %s -> %s'
              % (j0.str(3), j1.str(3), res['rrmax'].str(3), 'PASS (below 1e-3 of sup |R_rr|)' if jgood else 'FAIL'),
              flush=True)
        print('     control (perturbed approximant): jumps %s, %s -> %s' % (
            ctl['jumps'][0].str(3), ctl['jumps'][1].str(3), 'fails (good)' if jctl else 'passed (bad)'), flush=True)
        ok &= jgood and jctl
    print('cdata5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
