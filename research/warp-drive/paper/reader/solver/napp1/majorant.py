"""The polyellipse bound M by a majorant (rigorous; floating upper bounds with outward rounding margins):
every ingredient of the regular formula is bounded in modulus on the whole polyellipse E_rho1 x E_rho2 x E_rho3 (in the
box variables tau), using |T_n| <= rho^n there; the formula is evaluated with every operation replaced by the bound of
its result (|a +- b| <= |a| + |b|, |ab| = |a||b|, |a/b| <= |a| / lower(|b|)), divisions being only by R, Omega^2,
e^S and integers.  The fields' polynomial parts are the exact products Q^F = (v - 1/2)^4 G^F in tau."""
import math, numpy as np
from fractions import Fraction as Fr
import flint
from flint import arb, acb, fmpq
import cert, rep
from regform import regular_components

class Maj:
    __slots__ = ('up', 'lo')
    def __init__(self, up, lo=0.0):
        self.up = float(up); self.lo = float(lo)
    @staticmethod
    def c(o):
        if isinstance(o, Maj):
            return o
        a = abs(float(o)); return Maj(a, a)
    def __add__(self, o):
        o = Maj.c(o); return Maj((self.up + o.up) * (1 + 1e-14))
    __radd__ = __add__
    def __sub__(self, o):
        return self + o
    def __rsub__(self, o):
        return Maj.c(o) + self
    def __neg__(self):
        return self
    def __mul__(self, o):
        o = Maj.c(o); return Maj(self.up * o.up * (1 + 1e-14), self.lo * o.lo * (1 - 1e-14))
    __rmul__ = __mul__
    def __truediv__(self, o):
        o = Maj.c(o)
        if not o.lo > 0:
            raise ZeroDivisionError('majorant: divisor not bounded below')
        return Maj(self.up / o.lo * (1 + 1e-14), self.lo / o.up * (1 - 1e-14) if o.up > 0 else 0.0)
    def __rtruediv__(self, o):
        return Maj.c(o) / self

def mul_vq(c, alpha, beta):
    """c (array, axis 1 = tau2) times (alpha + beta tau2), exact"""
    c = np.moveaxis(c, 1, 0); n = c.shape[0]
    out = np.zeros((n + 1,) + c.shape[1:], dtype=object)
    for k in range(n):
        out[k] = out[k] + alpha * c[k]
        out[k + 1] = out[k + 1] + beta * c[k] / 2
        out[abs(k - 1)] = out[abs(k - 1)] + beta * c[k] / 2
    return np.moveaxis(out, 0, 1)

def coef_sum(c, rho):
    a = np.abs(np.array(c, dtype=float))
    w = np.multiply.outer(np.multiply.outer(rho[0] ** np.arange(a.shape[0]), rho[1] ** np.arange(a.shape[1])), rho[2] ** np.arange(a.shape[2]))
    return float((a * w).sum()) * (1 + 1e-10)

def majorant_M(Zp, p, L, i, j, sub, rho, nbox=24, nH=0.08):
    """returns M (bound of max_ab |f~_ab| on the polyellipse), the least Re R_s, max |Q^R|, and the ingredient bounds"""
    flint.ctx.prec = 128
    mx, hx = L['xi'][i]; mv, hv = L['v'][j]
    tc, th, sc, sh = (Fr(q) for q in sub)
    alpha = Fr(mv) + Fr(hv) * sc - Fr(1, 2); beta = Fr(hv) * sh          # v - 1/2 = alpha + beta tau2
    scale = Fr(1, 10 ** p)
    Q = {}
    for k in rep.FIELDS:
        c = Zp['%d_%d_%s' % (i, j, k)].astype(object) * scale
        c = cert.reexpand(cert.reexpand(c, 0, tc, th), 1, sc, sh)
        for _ in range(4):
            c = mul_vq(c, alpha, beta)
        Q[k] = c
    # derivative bounds in tau: names as cert.DER (t -> tau1, s -> tau2)
    BQ = {}
    for k in rep.FIELDS:
        BQ[k] = {}
        for name, a in cert.DER.items():
            cc = Q[k]
            for ax in range(3):
                for _ in range(a[ax]):
                    cc = cert.deriv_coeffs_int(cc, ax)
            BQ[k][name] = coef_sum(cc, rho)
    # chart and seed on the filled (tau1, tau2) polyellipse: coverings
    box = (arb(fmpq(mx.numerator, mx.denominator)), arb(fmpq(hx.numerator, hx.denominator)),
           arb(fmpq(mv.numerator, mv.denominator)), arb(fmpq(hv.numerator, hv.denominator)))
    a_ch = arb(fmpq(1, 500))
    Tb = cert.filled_boxes(rho[0], nbox)
    p1m = p2m = 0.0; umax = 0.0; umin = 1e300
    thA, tcA = arb(fmpq(th.numerator, th.denominator)), arb(fmpq(tc.numerator, tc.denominator))
    for tb in Tb:
        xi = box[0] + box[1] * (tcA + thA * tb)
        ch = xi.cosh()
        if not ch.real > 0:
            raise RuntimeError('cosh')
        p1 = 1 / (ch * box[1] * a_ch); p2 = -(p1 * p1) * (xi.sinh() / ch) * box[1]
        p1m = max(p1m, float(abs(p1).upper())); p2m = max(p2m, float(abs(p2).upper()))
        u = -1 + a_ch * xi.sinh()
        umax = max(umax, float(abs(u).upper())); umin = min(umin, float(abs(u).lower()))
    rmin, nHb, Hrect = cert.analytic_checks((box[0] + box[1] * tcA, box[1] * thA, box[2] + box[3] * arb(fmpq(sc.numerator, sc.denominator)),
                                            box[3] * arb(fmpq(sh.numerator, sh.denominator))), rho, n=nbox, nH=nH)
    # an upper bound for |R_s|: from the H-rectangle, |R_s| <= (|H| + |log((R-1)/(R+1))|)/2 <= (|H|max + 1)/2 + ...; use the
    # covering itself: re-run the Newton enclosures and take the largest modulus
    lo_r, hi_r, lo_i, hi_i = Hrect
    Rmax = 0.0
    nr = int(math.ceil((hi_r - lo_r) / nH)); ni = int(math.ceil((hi_i - lo_i) / nH))
    for pp in range(0, nr, max(1, nr // 60)):
        pass
    # |R_s| <= (|H| + 2.35)/2 for Re R_s > 3/2: (R-1)/(R+1) lies in the disc with diameter [1/5, 1], so |log| <= log 5 + arcsin(2/3) < 2.35
    Hmod = max(abs(complex(lo_r, lo_i)), abs(complex(lo_r, hi_i)), abs(complex(hi_r, lo_i)), abs(complex(hi_r, hi_i)))
    Rmax = Hmod / 2 + 1.175
    QR = BQ['R']['']
    if not rmin - QR > 0:
        raise RuntimeError('Re R not bounded below: %g - %g' % (rmin, QR))
    Rlo = rmin - QR; Rup = Rmax + QR
    # seed jets majorants: f = 1 - R^-2, g = 1 - u^-2
    Rs = Maj(Rmax, rmin); um = Maj(umax, umin)
    flo = 1 - 1 / rmin ** 2; fup = 1 + 1 / rmin ** 2; glo = 1 - 1 / umin ** 2; gup = 1 + 1 / umin ** 2
    f = Maj(fup, flo); g = Maj(gup, glo); fp = 2 / (Rs * Rs * Rs); fpp = 6 / (Rs * Rs * Rs * Rs)
    gp = 2 / (um * um * um); gpp = 6 / (um * um * um * um)
    Rv = f / 2; Ru = f / g; Rvv = fp * Rv / 2; Ruv = fp * Ru / 2; Ruu = fp * Ru / g + f * gp / (g * g)
    Wv = fp * Rv / (2 * f); Wu = (fp * Ru / f + gp / g) / 2
    Wvv = (fpp * Rv * Rv + fp * Rvv) / (2 * f) + (fp * Rv) * (fp * Rv) / (2 * f * f)
    Wuv = (fpp * Ru * Rv + fp * Ruv) / (2 * f) + (fp * Ru) * (fp * Rv) / (2 * f * f)
    Wuu = ((fpp * Ru * Ru + fp * Ruu) / f + (fp * Ru / f) * (fp * Ru / f) + (gpp / g + (gp / g) * (gp / g))) / 2
    O2s = f / (2 * g)
    seedR = {'': Maj(Rmax, rmin), 'u': Ru, 'v': Rv, 'uu': Ruu, 'uv': Ruv, 'vv': Rvv}
    seedW = {'u': Wu, 'v': Wv, 'uu': Wuu, 'uv': Wuv, 'vv': Wvv}
    # polynomial parts in (u, v, x): d/du = (phi1/th_t) d/dtau1, d2/du2 = (phi1/th_t)^2 d2 + (phi2/th_t) d, d/dv = (1/(hv sh)) d
    it = 1 / (float(hx) * 0 + float(th)); iv = 1 / (float(hv) * float(sh))
    P1, P2 = p1m * it, p2m * it
    J = {}
    for k in rep.FIELDS:
        b = BQ[k]
        q = {'': Maj(b['']), 'u': Maj(P1 * b['t']), 'v': Maj(iv * b['s']), 'x': Maj(b['x']),
             'uu': Maj(P1 * P1 * b['tt'] + P2 * b['t']), 'uv': Maj(P1 * iv * b['ts']), 'vv': Maj(iv * iv * b['ss']),
             'ux': Maj(P1 * b['tx']), 'vx': Maj(iv * b['sx']), 'xx': Maj(b['xx'])}
        if k == 'R':
            for d in seedR:
                q[d] = q[d] + seedR[d] if d else Maj(Rup, Rlo)
        if k == 'W':
            for d in seedW:
                q[d] = q[d] + seedW[d]
        J[k] = q
    xm = 0.5 * (rho[2] + 1 / rho[2])
    X = Maj(xm)
    Sb = ((1 + xm) * BQ['m'][''] + (1 + xm) * BQ['n']['']) / 3
    ES = Maj(math.exp(Sb), math.exp(-Sb))
    O2 = O2s * Maj(math.exp(2 * BQ['W']['']), math.exp(-2 * BQ['W']['']))
    fm = regular_components(X, J, ES, O2, one=Maj(1.0, 1.0))
    rho_up = Rup ** 4 / math.sqrt(72)
    M = max(fm[ab].up for ab in fm) * rho_up * (1 + 1e-12)
    return M, dict(ReRs_min=rmin, maxQR=QR, H_balls=nHb, Rmax=Rup, p1=p1m, p2=p2m, umin=umin, umax=umax)

if __name__ == '__main__':
    import sys, json
    case = sys.argv[1]; i, j = int(sys.argv[2]) - 1, int(sys.argv[3]) - 1
    rho = tuple(float(q) for q in sys.argv[4:7])
    meta = json.load(open('prov2_%s.json' % case)); Zp = dict(np.load('prov2_%s.npz' % case))
    L = rep.layout(case, enlarge=True)
    sub = cert.use_region(L, i, j)
    M, info = majorant_M(Zp, meta['p'], L, i, j, sub, rho)
    print(case, (i + 1, j + 1), rho, 'M = %.3e' % M, info)
