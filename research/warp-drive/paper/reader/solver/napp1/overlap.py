"""The overlap correction of prop:appc-overlap at level 0 (rigorous; outward-rounded floating bounds and ball arithmetic):
on each transition strip inside an element's use interval,
    |f~_ab(F_e + dF) - f~_ab(F_e)| <= Lambda_ab = sum_q L_q D_q,
D_q bounding the q-th 2-jet component of dF = (v - 1/2)^4 sum_{e' != e} w_e' (G_e' - G_e) on the strip (Leibniz with
the bounds phi_k of the partition and exact coefficient sums of the difference polynomials re-expanded on the strip),
L_q bounding |d f~_ab / d J_q| over the jets of F_e + theta dF on the strip (forward-mode majorants).
usage: overlap.py case i j"""
import sys, json, math, itertools, numpy as np
from fractions import Fraction as Fr
import flint
from flint import arb, fmpq
import rep, cert
from regform import regular_components

ONLY = {}
PHI = [1.0, 2.0, 9.853, 111.3, 2345.0, 8.527e4, 7.565e6]        # lem:appc-pou (a)
D2 = ('', 'u', 'v', 'x', 'uu', 'uv', 'vv', 'ux', 'vx', 'xx')
BETA = {'': (0, 0, 0), 'u': (1, 0, 0), 'v': (0, 1, 0), 'x': (0, 0, 1), 'uu': (2, 0, 0), 'uv': (1, 1, 0),
        'vv': (0, 2, 0), 'ux': (1, 0, 1), 'vx': (0, 1, 1), 'xx': (0, 0, 2)}
IDX = {(k, d): n for n, (k, d) in enumerate((k, d) for k in rep.FIELDS for d in D2)}
NQ = len(IDX)
U = 1 + 1e-13


class MD:
    """an upper bound 'up' of |value|, a lower bound 'lo', and upper bounds 'g' of |d value/d J_q|"""
    __slots__ = ('up', 'lo', 'g')
    def __init__(self, up, lo=0.0, g=None):
        self.up = up; self.lo = lo; self.g = np.zeros(NQ) if g is None else g
    @staticmethod
    def c(o):
        if isinstance(o, MD):
            return o
        a = abs(float(o)); return MD(a, a)
    def __add__(self, o):
        o = MD.c(o); return MD((self.up + o.up) * U, 0.0, (self.g + o.g) * U)
    __radd__ = __add__
    __sub__ = __add__
    def __rsub__(self, o):
        return MD.c(o) + self
    def __neg__(self):
        return self
    def __mul__(self, o):
        o = MD.c(o)
        return MD(self.up * o.up * U, self.lo * o.lo / U, (self.up * o.g + o.up * self.g) * U)
    __rmul__ = __mul__
    def __truediv__(self, o):
        o = MD.c(o)
        if not o.lo > 0:
            raise ZeroDivisionError
        return MD(self.up / o.lo * U, 0.0, (self.g / o.lo + self.up * o.g / o.lo ** 2) * U)
    def __rtruediv__(self, o):
        return MD.c(o) / self


def strips(L, i, j):
    """the parts of element (i, j)'s use interval where other partition functions are positive: pure xi-transition
    rectangles (only the xi-neighbour), pure v-transition rectangles (only the v-neighbour), and corner squares (all
    three neighbours).  Returns (xr, vr, kind, neighbours) with rational ends."""
    nx, nv = len(L['xi']), len(L['v'])
    sub = cert.use_region(L, i, j)
    mx, hx = L['xi'][i]; mv, hv = L['v'][j]
    ux = (Fr(mx) + Fr(hx) * (sub[0] - sub[1]), Fr(mx) + Fr(hx) * (sub[0] + sub[1]))
    uv = (Fr(mv) + Fr(hv) * (sub[2] - sub[3]), Fr(mv) + Fr(hv) * (sub[2] + sub[3]))
    xt = [((Fr(L['cxi'][k]) - Fr(L['dxi']), Fr(L['cxi'][k]) + Fr(L['dxi'])), k + 1 if k == i - 1 else k + 1, i - 1 if k == i - 1 else i + 1)
          for k in (i - 1, i) if 0 <= k < nx - 1]
    vt = [((Fr(L['cv'][k]) - Fr(L['dv']), Fr(L['cv'][k]) + Fr(L['dv'])), j - 1 if k == j - 1 else j + 1)
          for k in (j - 1, j) if 0 <= k < nv - 1]
    out = []
    # complement of the v-transitions inside uv, and of the xi-transitions inside ux
    def minus(rng, cuts):
        pieces = [rng]
        for (a, b) in cuts:
            new = []
            for (p, q) in pieces:
                if b <= p or a >= q:
                    new.append((p, q)); continue
                if p < a:
                    new.append((p, a))
                if b < q:
                    new.append((b, q))
            pieces = new
        return pieces
    for (xr, _, i2) in xt:
        for vr in minus(uv, [t[0] for t in vt]):
            out.append((xr, vr, 'xi', [(i2, j)]))
    for (vr, j2) in vt:
        for xr in minus(ux, [t[0] for t in xt]):
            out.append((xr, vr, 'v', [(i, j2)]))
    for (xr, _, i2) in xt:
        for (vr, j2) in vt:
            out.append((xr, vr, 'corner', [(i2, j), (i2, j2), (i, j2)]))
    return out, None


def reexp_strip(Z, p, L, e, k, xr, vr):
    """G^k_e re-expanded in the strip variables tau (xi = xc + xh tau1, v = vc + vh tau2): exact"""
    i, j = e
    mx, hx = L['xi'][i]; mv, hv = L['v'][j]
    xc, xh = (xr[0] + xr[1]) / 2, (xr[1] - xr[0]) / 2; vc, vh = (vr[0] + vr[1]) / 2, (vr[1] - vr[0]) / 2
    c = Z['%d_%d_%s' % (i, j, k)].astype(object) * Fr(1, 10 ** p)
    c = cert.reexpand(c, 0, (xc - Fr(mx)) / Fr(hx), xh / Fr(hx))
    c = cert.reexpand(c, 1, (vc - Fr(mv)) / Fr(hv), vh / Fr(hv))
    return c


def dsum(c, a):
    cc = c
    for ax in range(3):
        for _ in range(a[ax]):
            cc = cert.deriv_coeffs_int(cc, ax)
    return float(np.abs(np.array(cc, dtype=float)).sum()) * (1 + 1e-10)


def pad(a, b):
    shp = tuple(max(x, y) for x, y in zip(a.shape, b.shape))
    A = np.zeros(shp, dtype=object); B = np.zeros(shp, dtype=object)
    A[tuple(slice(0, n) for n in a.shape)] = a; B[tuple(slice(0, n) for n in b.shape)] = b
    return A, B


def overlap(case, i, j, source='prov2'):
    flint.ctx.prec = 128
    meta = json.load(open('%s_%s.json' % (source, case))); p = meta['p']
    Z = dict(np.load('%s_%s.npz' % (source, case)))
    L = rep.layout(case, enlarge=True)
    S, _ = strips(L, i, j)
    a = 1 / 500
    res = []
    only = ONLY.get('kind')
    for (xr, vr, kind, nb) in S:
        if only and kind != only:
            continue
        xh = float(xr[1] - xr[0]) / 2; vh = float(vr[1] - vr[0]) / 2
        # chart bounds on the strip: xi < 0, so cosh xi is smallest at the upper end
        xu = float(xr[1]); ch = math.cosh(xu) / U
        xiu = 1 / (a * ch) * U; xiuu = 1 / (a * ch) ** 2 * U                  # |d xi/du|, |d2 xi/du2|
        tu, tuu = xiu / xh, xiuu / xh                                     # derivatives of tau1 in u (tau1 affine in xi)
        # sup over the strip of derivatives (in (u, v, x)) of a polynomial in tau from its tau-coefficient sums
        def chain(sm):
            return {'': sm[(0, 0, 0)], 'u': tu * sm[(1, 0, 0)], 'v': sm[(0, 1, 0)] / vh, 'x': sm[(0, 0, 1)],
                    'uu': tu * tu * sm[(2, 0, 0)] + tuu * sm[(1, 0, 0)], 'uv': tu * sm[(1, 1, 0)] / vh,
                    'vv': sm[(0, 2, 0)] / vh ** 2, 'ux': tu * sm[(1, 0, 1)], 'vx': sm[(0, 1, 1)] / vh, 'xx': sm[(0, 0, 2)]}
        al = [BETA[d] for d in D2]
        # (v - 1/2)^4 and its v-derivatives on the strip
        vmax = float(vr[1]) - 0.5; vmin = max(float(vr[0]) - 0.5, 0.0)
        V4 = {0: vmax ** 4, 1: 4 * vmax ** 3, 2: 12 * vmax ** 2}
        # weights: chi in xi (via u), psi in v; bounds of their (u, v)-derivatives on the strip
        dxi_ = float(L['dxi']); dv_ = float(L['dv'])
        def wbound(bu, bv):
            cu = [1.0, PHI[1] / (2 * dxi_) * xiu, PHI[2] / (2 * dxi_) ** 2 * xiu ** 2 + PHI[1] / (2 * dxi_) * xiuu]
            cv = [1.0, PHI[1] / (2 * dv_), PHI[2] / (2 * dv_) ** 2]
            if kind == 'xi':
                cv = [1.0, 0.0, 0.0]
            if kind == 'v':
                cu = [1.0, 0.0, 0.0]
            return cu[bu] * cv[bv]
        Dq = np.zeros(NQ)
        for k in rep.FIELDS:
            Ge = reexp_strip(Z, p, L, (i, j), k, xr, vr)
            for e2 in nb:
                Gd = reexp_strip(Z, p, L, e2, k, xr, vr)
                A_, B_ = pad(Gd, Ge)
                Dl = A_ - B_
                sm = {b: dsum(Dl, b) for b in set(al) | {(1, 0, 0), (0, 1, 0)}}
                dD = chain(sm)
                # Leibniz for (v - 1/2)^4 w Delta, derivatives beta = (bu, bv, bx)
                for d in D2:
                    bu, bv, bx = BETA[d]
                    tot = 0.0
                    for su in range(bu + 1):
                        for sv in range(bv + 1):
                            for sv2 in range(bv - sv + 1):
                                # split bv into (v^4 part sv, weight part sv2, Delta part rest); bu into (weight su, Delta rest)
                                rv = bv - sv - sv2; ru = bu - su
                                mult = math.comb(bu, su) * math.factorial(bv) // (math.factorial(sv) * math.factorial(sv2) * math.factorial(rv))
                                key = {(0, 0, 0): '', (1, 0, 0): 'u', (0, 1, 0): 'v', (2, 0, 0): 'uu', (1, 1, 0): 'uv', (0, 2, 0): 'vv'}
                                kd = key.get((ru, rv, 0)) if bx == 0 else {(0, 0): 'x', (1, 0): 'ux', (0, 1): 'vx'}.get((ru, rv)) if bx == 1 else ('xx' if (ru, rv) == (0, 0) else None)
                                if kd is None:
                                    continue
                                tot += mult * V4[sv] * wbound(su, sv2) * dD[kd]
                    Dq[IDX[(k, d)]] += tot * U
        # jets of F_e on the strip (seed + polynomial part), widened by D (theta in [0, 1])
        Jb = {}
        # seed enclosures on a subdivision of the strip (a single wide ball loses positivity of R^3 by dependency);
        # keep, for every jet, the largest modulus, and for R and Omega_s^2 the least value
        class _B:
            pass
        nu_, nv_ = 48, 8
        upR = {d: 0.0 for d in D2}; upW = {d: 0.0 for d in D2}; loR = 1e300; loO = 1e300; upO = 0.0
        for q1 in range(nu_):
            x0 = float(xr[0]) + (float(xr[1]) - float(xr[0])) * q1 / nu_; x1 = float(xr[0]) + (float(xr[1]) - float(xr[0])) * (q1 + 1) / nu_
            ub = arb(-1 + a * math.sinh(x0)).union(arb(-1 + a * math.sinh(x1)))
            for q2 in range(nv_):
                v0 = float(vr[0]) + (float(vr[1]) - float(vr[0])) * q2 / nv_; v1 = float(vr[0]) + (float(vr[1]) - float(vr[0])) * (q2 + 1) / nv_
                vb = arb(v0).union(arb(v1))
                tR, tW, tO, _ = cert.seed_jets(ub, vb)
                for d in D2:
                    upR[d] = max(upR[d], float(abs(tR[d]).upper())); upW[d] = max(upW[d], float(abs(tW[d]).upper()))
                loR = min(loR, float(tR[''].lower())); loO = min(loO, float(tO.lower())); upO = max(upO, float(tO.upper()))
        for k in rep.FIELDS:
            Ge = reexp_strip(Z, p, L, (i, j), k, xr, vr)
            # (v - 1/2)^4 G_e: bound by Leibniz as above with w = 1
            sm = {b: dsum(Ge, b) for b in set(al) | {(1, 0, 0), (0, 1, 0)}}
            dG = chain(sm)
            qb = {}
            for d in D2:
                bu, bv, bx = BETA[d]
                tot = 0.0
                for sv in range(bv + 1):
                    rv = bv - sv
                    key = (bu, rv, bx)
                    nm = [n for n, b in BETA.items() if b == key]
                    if nm:
                        tot += math.comb(bv, sv) * V4[sv] * dG[nm[0]]
                qb[d] = tot * U
            for d in D2:
                seedv = 0.0
                if k == 'R':
                    seedv = upR[d]
                if k == 'W' and d:
                    seedv = upW[d]
                Jb[(k, d)] = seedv + qb[d] + Dq[IDX[(k, d)]]
        Rlo = loR - (Jb[('R', '')] - upR[''])                                       # R_s,min - |Q^R| - D_R
        Rup = Jb[('R', '')]
        O2lo = loO * math.exp(-2 * Jb[('W', '')]) / U; O2up = upO * math.exp(2 * Jb[('W', '')]) * U
        J = {}
        for k in rep.FIELDS:
            J[k] = {}
            for d in D2:
                g = np.zeros(NQ); g[IDX[(k, d)]] = 1.0
                J[k][d] = MD(Jb[(k, d)], 0.0, g)
        J['R'][''].lo = Rlo
        X = MD(1.0, 0.0)
        S_ = (2 * J['m'][''] + 2 * J['n']['']) / 3
        ES = MD(math.exp(S_.up) * U, math.exp(-S_.up) / U, math.exp(S_.up) * U * S_.g)
        gW = np.zeros(NQ); gW[IDX[('W', '')]] = 2 * O2up
        OM2 = MD(O2up, O2lo, gW)
        f = regular_components(X, J, ES, OM2, one=MD(1.0, 1.0))
        Rr = J['R']['']
        rho = (Rr * Rr) * (Rr * Rr) / math.sqrt(72) * U
        lam = {}
        for ab, e in f.items():
            E = rho * e
            lam[ab] = float((E.g * Dq).sum()) * U
        res.append(dict(strip=[[str(q) for q in xr], [str(q) for q in vr]], kind=kind, Lambda=max(lam.values()),
                        Dmax=float(Dq.max()), Rlo=Rlo))
        print('%s element (%d,%d) strip %s xi %s v %s: max_q D_q %.2e, Lambda = %.3e (R >= %.2f)' %
              (case, i + 1, j + 1, kind, [round(float(q), 4) for q in xr], [round(float(q), 4) for q in vr], Dq.max(), max(lam.values()), Rlo), flush=True)
    return res


if __name__ == '__main__':
    case, i, j = sys.argv[1], int(sys.argv[2]) - 1, int(sys.argv[3]) - 1
    if len(sys.argv) > 4:
        ONLY['kind'] = sys.argv[4]
    r = overlap(case, i, j)
    json.dump(r, open('overlap_%s_%d_%d%s.json' % (case, i + 1, j + 1, '_' + sys.argv[4] if len(sys.argv) > 4 else ''), 'w'), indent=1)
