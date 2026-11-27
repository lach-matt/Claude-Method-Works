"""prop:appc-overlap for the derivatives of order <= K (P-APPC: "the same holds for the derivatives of order at most K,
with (K + 2)-jets"), rigorous (outward-rounded floating majorants and ball arithmetic):
on each transition strip of an element's use interval, for every alpha with |alpha| <= K,
  sup |d^alpha (f~_ab(F_e + dF) - f~_ab(F_e))| <= Lambda_ab,alpha = sum_q sum_{beta <= alpha} C(alpha, beta)
        sup|d^beta L_q| sup|d^(alpha - beta) dJ_q|,      L_q = d f~_ab/d J_q over the hull of F_e + theta dF,
the derivatives in (xi, v, x) and converted to the element's (t, sigma, x) at the end.  sup|d^beta L_q| comes from a
derivative-majorant arithmetic (each quantity carries upper bounds of all its derivatives of order <= K and of those of
its partial derivatives in the 2-jet inputs; products by Leibniz, reciprocals and exponentials by their recursions).
Ingredients: the strip coefficients of every G_e and of the differences G_e' - G_e, exact in ball arithmetic (the
polynomials evaluated at the strip's Lobatto points and transformed); the partition's derivative bounds phi_k
(lem:appc-pou (a), k <= 6, so K <= 4); the seed's derivatives to order K + 2 by bivariate Taylor arithmetic in balls.
usage: overlapK.py case tables_z.pkl i j K out.json [prec]"""
import sys, os, json, math, time, pickle, itertools, numpy as np
from fractions import Fraction as Fr
NAPP1 = os.environ.get('NAPP1', '/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/napp1')
sys.path.insert(0, NAPP1)
import flint
from flint import arb, arb_mat, fmpq
import cert, rep, overlap
from regform import regular_components

PHI = [1.0, 2.0, 9.853, 111.3, 2345.0, 8.527e4, 7.565e6]
U = 1 + 1e-12
FN = rep.FIELDS
JD = {'': (0, 0, 0), 'u': (1, 0, 0), 'v': (0, 1, 0), 'x': (0, 0, 1), 'uu': (2, 0, 0), 'uv': (1, 1, 0), 'vv': (0, 2, 0),
      'ux': (1, 0, 1), 'vx': (0, 1, 1), 'xx': (0, 0, 2)}       # the 2-jet multi-indices (here in (xi, v, x))

class MI:
    def __init__(self, K):
        self.K = K
        self.L = [b for n in range(K + 1) for b in itertools.product(range(n + 1), repeat=3) if sum(b) == n]
        self.L = sorted(set(self.L), key=lambda b: (sum(b), b))
        self.ix = {b: k for k, b in enumerate(self.L)}; self.n = len(self.L)
        T, I1, I2, C = [], [], [], []
        for b in self.L:
            for g in itertools.product(*[range(q + 1) for q in b]):
                r = tuple(bi - gi for bi, gi in zip(b, g))
                T.append(self.ix[b]); I1.append(self.ix[g]); I2.append(self.ix[r])
                C.append(math.comb(b[0], g[0]) * math.comb(b[1], g[1]) * math.comb(b[2], g[2]))
        self.T, self.I1, self.I2, self.C = (np.array(a) for a in (T, I1, I2, C))
        self.C = self.C.astype(float)
    def conv(self, a, b):
        return np.bincount(self.T, weights=self.C * a[self.I1] * b[self.I2], minlength=self.n) * U
    def convmat(self, a):          # matrix of x -> conv(a, x)
        Mt = np.zeros((self.n, self.n)); np.add.at(Mt, (self.T, self.I2), self.C * a[self.I1]); return Mt * U

class DM:
    """upper bounds d[beta] of sup|d^beta Q| (|beta| <= K), a lower bound lo of |Q|, and g[q, beta] for dQ/dJ_q"""
    mi = None; NQ = 0
    __slots__ = ('d', 'lo', 'g')
    def __init__(self, d, lo=0.0, g=None):
        self.d = d; self.lo = lo; self.g = g
    @classmethod
    def const(cls, c):
        d = np.zeros(cls.mi.n); d[0] = abs(float(c)); return DM(d, abs(float(c)))
    @staticmethod
    def c(o):
        return o if isinstance(o, DM) else DM.const(o)
    def __add__(self, o):
        o = DM.c(o)
        g = None if (self.g is None and o.g is None) else (self.g if o.g is None else o.g if self.g is None else self.g + o.g) * U
        return DM((self.d + o.d) * U, 0.0, g)
    __radd__ = __add__; __sub__ = __add__
    def __rsub__(self, o): return DM.c(o) + self
    def __neg__(self): return self
    def __mul__(self, o):
        o = DM.c(o); mi = DM.mi
        d = mi.conv(self.d, o.d)
        g = None
        if self.g is not None: g = self.g @ mi.convmat(o.d).T
        if o.g is not None: g2 = o.g @ mi.convmat(self.d).T; g = g2 if g is None else (g + g2) * U
        return DM(d, self.lo * o.lo / U, g)
    __rmul__ = __mul__
    def inv(self):
        mi = DM.mi
        if not self.lo > 0: raise ZeroDivisionError('divisor not bounded below')
        w = np.zeros(mi.n); w[0] = 1 / self.lo * U
        for k in range(1, mi.n):
            s = 0.0
            for t, i1, i2, c in zip(mi.T, mi.I1, mi.I2, mi.C):
                if t == k and i2 != k: s += c * self.d[i1] * w[i2]
            w[k] = s / self.lo * U
        W = DM(w, 1 / self.d[0] / U if self.d[0] > 0 else 0.0)
        if self.g is not None: W.g = -(self.g @ mi.convmat(mi.conv(w, w)).T)
        if W.g is not None: W.g = np.abs(W.g)
        return W
    def __truediv__(self, o):
        if isinstance(o, DM): return self * o.inv()
        return self * DM.const(1.0 / abs(float(o)))
    def __rtruediv__(self, o): return DM.c(o) * self.inv()

def dmexp(S):
    mi = DM.mi; E = np.zeros(mi.n); E[0] = math.exp(S.d[0]) * U
    for k in range(1, mi.n):
        b = mi.L[k]; i = next(q for q in range(3) if b[q] > 0)
        bm = tuple(bb - (1 if q == i else 0) for q, bb in enumerate(b))
        s = 0.0
        for g in itertools.product(*[range(q + 1) for q in bm]):
            r = tuple(bb - gg for bb, gg in zip(b, g))
            s += math.comb(bm[0], g[0]) * math.comb(bm[1], g[1]) * math.comb(bm[2], g[2]) * E[mi.ix[g]] * S.d[mi.ix[r]]
        E[k] = s * U
    out = DM(E, math.exp(-S.d[0]) / U)
    if S.g is not None: out.g = S.g @ mi.convmat(E).T
    return out

# ---------------------------------------------------------------- univariate / bivariate series in balls
def s_mul(a, b, n): return [sum((a[i] * b[k - i] for i in range(k + 1)), arb(0)) for k in range(n)]
def s_inv(a, n):
    r = [1 / a[0]]
    for k in range(1, n): r.append(-sum((a[j] * r[k - j] for j in range(1, k + 1)), arb(0)) * r[0])
    return r
def b_mul(A, B, n):
    C = [[arb(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n - i):
            if A[i][j] == 0: continue
            for k in range(n - i):
                for l in range(n - i - k - j):
                    C[i + k][j + l] += A[i][j] * B[k][l]
    return C
def b_inv(A, n):   # 1/A by Newton-free recursion on the total degree
    a0 = A[0][0]; R_ = [[arb(0)] * n for _ in range(n)]; R_[0][0] = 1 / a0
    for tot in range(1, n):
        for i in range(tot + 1):
            j = tot - i; s = arb(0)
            for k in range(i + 1):
                for l in range(j + 1):
                    if k == 0 and l == 0: continue
                    s += A[k][l] * R_[i - k][j - l]
            R_[i][j] = -s / a0
    return R_

def seed_bounds(xb, vb, n):
    """bounds of |d_xi^a d_v^b X| (a + b < n) on the ball (xb, vb), X in (R_s, W_s, Omega_s^2), and min R_s"""
    a_ch = arb(fmpq(1, 500))
    sh, ch = xb.sinh(), xb.cosh()
    # series in s of sinh(xb + s), cosh(xb + s)
    SH = [sh if k % 2 == 0 else ch for k in range(n)]; CH = [ch if k % 2 == 0 else sh for k in range(n)]
    fac = [arb(math.factorial(k)) for k in range(n)]
    SH = [SH[k] / fac[k] for k in range(n)]; CH = [CH[k] / fac[k] for k in range(n)]
    u = [a_ch * q for q in SH]; u[0] = u[0] - 1
    iu = s_inv(u, n); g = s_mul(iu, iu, n); g = [-q for q in g]; g[0] = g[0] + 1      # g = 1 - u^-2
    ig = s_inv(g, n)
    H = vb - 2 * u[0] + ((u[0] + 1) / (u[0] - 1)).log()
    R0 = cert.seed_R(H, False)
    # R(s, 0): dR/ds = -a cosh f(R)/g
    Rs = [R0] + [arb(0)] * (n - 1)
    for _ in range(n + 1):
        iR = s_inv(Rs, n); f = [-q for q in s_mul(iR, iR, n)]; f[0] = f[0] + 1
        rhs = s_mul(s_mul([-a_ch * q for q in CH], f, n), ig, n)
        Rs = [R0] + [rhs[k - 1] / k for k in range(1, n)]
    # bivariate: R(s, t) with dR/dt = f(R)/2
    B = [[arb(0)] * n for _ in range(n)]
    for i in range(n): B[i][0] = Rs[i]
    for _ in range(n + 1):
        iR = b_inv(B, n); f = b_mul(iR, iR, n); f = [[-q for q in row] for row in f]; f[0][0] = f[0][0] + 1
        Bn = [[arb(0)] * n for _ in range(n)]
        for i in range(n): Bn[i][0] = Rs[i]
        for i in range(n):
            for j in range(1, n - i): Bn[i][j] = f[i][j - 1] / (2 * j)
        B = Bn
    iR = b_inv(B, n); f = b_mul(iR, iR, n); f = [[-q for q in row] for row in f]; f[0][0] = f[0][0] + 1
    G = [[arb(0)] * n for _ in range(n)]
    for i in range(n): G[i][0] = ig[i] / 2
    O = b_mul(f, G, n)                                           # Omega_s^2 = f/(2g)
    # W_s = (1/2) log O: dW = dO/(2 O); coefficients via W_s - log of the constant: use series log
    iO = b_inv(O, n)
    # d_s W = (d_s O)/(2O), d_t W = (d_t O)/(2O): integrate the s-part on t = 0, then t
    dsO = [[(i + 1) * O[i + 1][j] if i + 1 < n else arb(0) for j in range(n)] for i in range(n)]
    dtO = [[(j + 1) * O[i][j + 1] if j + 1 < n else arb(0) for j in range(n)] for i in range(n)]
    Ws = b_mul(dsO, iO, n); Wt = b_mul(dtO, iO, n)
    W = [[arb(0)] * n for _ in range(n)]
    W[0][0] = O[0][0].log() / 2
    for i in range(1, n): W[i][0] = Ws[i - 1][0] / (2 * i)
    for i in range(n):
        for j in range(1, n - i): W[i][j] = Wt[i][j - 1] / (2 * j)
    out = {}
    for nm, S_ in (('R', B), ('W', W), ('O', O)):
        out[nm] = {(i, j): float(abs(S_[i][j]).upper()) * math.factorial(i) * math.factorial(j) for i in range(n) for j in range(n - i)}
    return out, float(R0.lower()), float(O[0][0].lower()), float(O[0][0].upper())

def series_p(xb, n):
    """bounds of the xi-derivatives (orders < n) of p1 = dxi/du = 1/(a cosh xi) and p2 = d2xi/du2 = -sinh/(a^2 cosh^3)"""
    a_ch = arb(fmpq(1, 500)); sh, ch = xb.sinh(), xb.cosh()
    fac = [math.factorial(k) for k in range(n)]
    SH = [(sh if k % 2 == 0 else ch) / fac[k] for k in range(n)]; CH = [(ch if k % 2 == 0 else sh) / fac[k] for k in range(n)]
    iC = s_inv([a_ch * q for q in CH], n)
    p2 = s_mul(s_mul(s_mul(iC, iC, n), iC, n), [-a_ch * q for q in SH], n)
    return [float(abs(q).upper()) * fac[k] for k, q in enumerate(iC)], [float(abs(q).upper()) * fac[k] for k, q in enumerate(p2)]

# ---------------------------------------------------------------- strip coefficients (exact, balls)
def lob(N): return [arb(fmpq(l, N)).cos_pi() for l in range(N + 1)]
def dct_mat(Nd):
    rows = []
    for kk in range(Nd + 1):
        r = []
        for l in range(Nd + 1):
            w = arb(1) if 0 < l < Nd else arb(1) / 2
            c = w * arb(fmpq(kk * l, Nd)).cos_pi() * 2 / Nd
            if kk == 0 or kk == Nd: c = c / 2
            r.append(c)
        rows.append(r)
    return arb_mat(rows)

def strip_coeffs(C, box, el_box, ndeg):
    """coefficients in the strip variables of the polynomial with element coefficients C (Fractions), the strip box
    (xc, xh, vc, vh) and the element box (mx, hx, mv, hv) (Fractions); ndeg the degrees per direction (>= C's)"""
    xc, xh, vc, vh = box; mx, hx, mv, hv = el_box
    n1, n2, n3 = C.shape; N1, N2, N3 = ndeg
    P1, P2, P3 = lob(N1), lob(N2), lob(N3)
    t = [(arb(fmpq(xc.numerator, xc.denominator)) + arb(fmpq(xh.numerator, xh.denominator)) * q - arb(fmpq(mx.numerator, mx.denominator))) / arb(fmpq(hx.numerator, hx.denominator)) for q in P1]
    s = [(arb(fmpq(vc.numerator, vc.denominator)) + arb(fmpq(vh.numerator, vh.denominator)) * q - arb(fmpq(mv.numerator, mv.denominator))) / arb(fmpq(hv.numerator, hv.denominator)) for q in P2]
    V1, V2, V3 = cert.vander(t, n1), cert.vander(s, n2), cert.vander(P3, n3)
    A = arb_mat([[arb(fmpq(C[a, b, k].numerator, C[a, b, k].denominator)) if isinstance(C[a, b, k], Fr) else arb(int(C[a, b, k])) for k in range(n3)] for a in range(n1) for b in range(n2)])
    M1 = (A * arb_mat([[V3[l][k] for l in range(N3 + 1)] for k in range(n3)])).entries()
    B2 = arb_mat([[V2[l][b] for b in range(n2)] for l in range(N2 + 1)])
    vals = []
    for a in range(n1):
        Ma = arb_mat([[M1[(a * n2 + b) * (N3 + 1) + l3] for l3 in range(N3 + 1)] for b in range(n2)])
        vals.append((B2 * Ma).entries())
    R3 = arb_mat(vals)                                                       # n1 x (N2+1)(N3+1)
    Vals = arb_mat([[V1[l][a] for a in range(n1)] for l in range(N1 + 1)]) * R3   # (N1+1) x (N2+1)(N3+1)
    D1, D2, D3 = dct_mat(N1), dct_mat(N2), dct_mat(N3)
    X = (D1 * Vals).entries()                                                # transform in tau1
    out = np.zeros((N1 + 1, N2 + 1, N3 + 1))
    D3t = D3.transpose()
    for i in range(N1 + 1):
        S = arb_mat([[X[i * (N2 + 1) * (N3 + 1) + l2 * (N3 + 1) + l3] for l3 in range(N3 + 1)] for l2 in range(N2 + 1)])
        Ci = (D2 * S * D3t).entries()
        out[i] = np.array([float(abs(e).upper()) for e in Ci]).reshape(N2 + 1, N3 + 1)
    return out

def coef_bounds(absC, mi, scale):
    """B[beta] >= sup over the strip of |d^beta p| in (xi, v, x), from |coefficients| in the strip variables;
    scale = (1/xh, 1/vh, 1); T_n^(l)(1) weights; beta over mi (orders <= mi.K)"""
    N = absC.shape
    W = [[np.array([float(cert.Tl1(nn, l)) for nn in range(N[d])]) for l in range(mi.K + 1)] for d in range(3)]
    B = np.zeros(mi.n)
    for k, b in enumerate(mi.L):
        w = np.multiply.outer(np.multiply.outer(W[0][b[0]], W[1][b[1]]), W[2][b[2]])
        B[k] = float((absC * w).sum()) * scale[0] ** b[0] * scale[1] ** b[1] * U
    return B

def overlapK(case, zfile, i, j, K, prec=256, nsub=(6, 3)):
    flint.ctx.prec = prec
    zs = pickle.load(open(zfile, 'rb'))
    Z = {k: np.vectorize(lambda q, p=p: Fr(int(q), 10 ** p), otypes=[object])(z) for k, (p, z) in zs.items()}
    L = rep.layout(case)
    S, _ = overlap.strips(L, i, j)
    miB = MI(K + 2); mi = MI(K); DM.mi = mi
    dxi, dv = float(L['dxi']), float(L['dv'])
    res = []
    for (xr, vr, kind, nb) in S:
        t0 = time.time()
        xc, xh, vc, vh = (xr[0] + xr[1]) / 2, (xr[1] - xr[0]) / 2, (vr[0] + vr[1]) / 2, (vr[1] - vr[0]) / 2
        sc = (1 / float(xh), 1 / float(vh), 1.0)
        # polynomial parts: bounds of d^beta G_e and of d^beta (G_e' - G_e), |beta| <= K + 2
        BG, BD = {}, {}
        for F in FN:
            Ce = Z['%d_%d_%s' % (i, j, F)]
            nd = list(Ce.shape)
            others = [Z['%d_%d_%s' % (a, b, F)] for (a, b) in nb]
            for o in others: nd = [max(p, q) for p, q in zip(nd, o.shape)]
            nd = [max(q - 1, 1) for q in nd]
            el = lambda a, b: (L['xi'][a][0], L['xi'][a][1], L['v'][b][0], L['v'][b][1])
            ce = strip_coeffs(Ce, (xc, xh, vc, vh), el(i, j), nd)
            BG[F] = coef_bounds(ce, miB, sc)
            BD[F] = []
            for (a, b), Co in zip(nb, others):
                # the difference: exact strip coefficients of G_e' minus those of G_e (both as balls) -> transform jointly
                A_, B_ = overlap.pad(Co, Ce)
                cd = strip_coeffs_diff(A_, B_, (xc, xh, vc, vh), el(a, b), el(i, j), nd)
                BD[F].append(coef_bounds(cd, miB, sc))
        # (v - 1/2)^4 and its derivatives on the strip; the weights' derivative bounds
        emax = max(abs(float(vr[0]) - 0.5), abs(float(vr[1]) - 0.5))
        E4 = [24 / math.factorial(4 - k) * emax ** (4 - k) if k <= 4 else 0.0 for k in range(K + 3)]
        def wb(a, b):        # |d_xi^a d_v^b (chi psi)| for the strip kind
            cu = PHI[a] / (2 * dxi) ** a if kind in ('xi', 'corner') else (1.0 if a == 0 else 0.0)
            cv = PHI[b] / (2 * dv) ** b if kind in ('v', 'corner') else (1.0 if b == 0 else 0.0)
            return cu * cv
        def leib_e4(Bp, wfun):
            out = np.zeros(miB.n)
            for k, (b1, b2, b3) in enumerate(miB.L):
                s = 0.0
                for a1 in range(b1 + 1):
                    for c2 in range(b2 + 1):
                        for d2 in range(b2 - c2 + 1):
                            r2 = b2 - c2 - d2
                            m = math.comb(b1, a1) * math.factorial(b2) // (math.factorial(c2) * math.factorial(d2) * math.factorial(r2))
                            s += m * E4[c2] * wfun(a1, d2) * Bp[miB.ix[(b1 - a1, r2, b3)]]
                out[k] = s * U
            return out
        BQ = {F: leib_e4(BG[F], lambda a, b: 1.0 if a == 0 and b == 0 else 0.0) for F in FN}
        BdF = {F: sum(leib_e4(B, wb) for B in BD[F]) for F in FN}
        # seed bounds on a subdivision of the strip
        nsx, nsv = nsub
        sR = {}; sW = {}; sO = {}; Rmin = 1e300; Omin = 1e300; Omax = 0.0; p1b = None; p2b = None
        for q1 in range(nsx):
            x0 = float(xr[0]) + float(xr[1] - xr[0]) * q1 / nsx; x1 = float(xr[0]) + float(xr[1] - xr[0]) * (q1 + 1) / nsx
            xb = arb((x0 + x1) / 2, (x1 - x0) / 2 * U)
            pa, pb = series_p(xb, K + 3)
            p1b = pa if p1b is None else [max(a, b) for a, b in zip(p1b, pa)]; p2b = pb if p2b is None else [max(a, b) for a, b in zip(p2b, pb)]
            for q2 in range(nsv):
                v0 = float(vr[0]) + float(vr[1] - vr[0]) * q2 / nsv; v1 = float(vr[0]) + float(vr[1] - vr[0]) * (q2 + 1) / nsv
                vb = arb((v0 + v1) / 2, (v1 - v0) / 2 * U)
                bnd, rmin, omin, omax = seed_bounds(xb, vb, K + 3)
                for key, val in bnd['R'].items(): sR[key] = max(sR.get(key, 0.0), val)
                for key, val in bnd['W'].items(): sW[key] = max(sW.get(key, 0.0), val)
                for key, val in bnd['O'].items(): sO[key] = max(sO.get(key, 0.0), val)
                Rmin = min(Rmin, rmin); Omin = min(Omin, omin); Omax = max(Omax, omax)
        # field derivative bounds (orders <= K + 2) on the hull of F_e + theta dF
        BF = {}
        for F in FN:
            b = BQ[F] + BdF[F]
            if F in ('R', 'W'):
                sd = sR if F == 'R' else sW
                b = b + np.array([sd.get((bb[0], bb[1]), 0.0) if bb[2] == 0 else 0.0 for bb in miB.L])
            BF[F] = b * U
        # the 2-jet inputs as DMs with gradients
        qidx = {(F, d): n for n, (F, d) in enumerate((F, d) for F in FN for d in JD)}
        DM.NQ = len(qidx)
        def jet(F, d):
            dd = JD[d]
            arr = np.array([BF[F][miB.ix[tuple(a + b for a, b in zip(bb, dd))]] for bb in mi.L])
            g = np.zeros((DM.NQ, mi.n)); g[qidx[(F, d)], 0] = 1.0
            return DM(arr, 0.0, g)
        Jx = {F: {d: jet(F, d) for d in JD} for F in FN}
        Rlo = Rmin - BQ['R'][0] - BdF['R'][0]
        Jx['R'][''].lo = Rlo
        P1 = DM(np.array([p1b[bb[0]] if bb[1] == 0 and bb[2] == 0 else 0.0 for bb in mi.L]))
        P2 = DM(np.array([p2b[bb[0]] if bb[1] == 0 and bb[2] == 0 else 0.0 for bb in mi.L]))
        J = {}
        for F in FN:
            jx = Jx[F]
            J[F] = {'': jx[''], 'u': P1 * jx['u'], 'v': jx['v'], 'x': jx['x'], 'uu': P1 * P1 * jx['uu'] + P2 * jx['u'],
                    'uv': P1 * jx['uv'], 'vv': jx['vv'], 'ux': P1 * jx['ux'], 'vx': jx['vx'], 'xx': jx['xx']}
        X = DM(np.array([1.0 if bb == (0, 0, 0) else (1.0 if bb == (0, 0, 1) else 0.0) for bb in mi.L]))
        Sx = (DM.const(2) * J['m'][''] + DM.const(2) * J['n']['']) / 3
        ES = dmexp(Sx)
        Om = DM(np.array([sO.get((bb[0], bb[1]), 0.0) if bb[2] == 0 else 0.0 for bb in mi.L]), Omin)
        PW = DM(np.array([(BQ['W'] + BdF['W'])[miB.ix[bb]] for bb in mi.L]), 0.0, None)
        gW = np.zeros((DM.NQ, mi.n)); gW[qidx[('W', '')], 0] = 1.0; PW.g = gW
        OM2 = Om * dmexp(DM.const(2) * PW)
        OM2.lo = Omin * math.exp(-2 * PW.d[0]) / U
        f = regular_components(X, J, ES, OM2, one=DM.const(1))
        Rr = J['R']['']
        rho = (Rr * Rr) * (Rr * Rr) / math.sqrt(72)
        # Lambda_alpha = sum_q sum_{beta <= alpha} C(alpha, beta) g[q, beta] sup|d^(alpha - beta) dJ_q|
        dJ = np.zeros((DM.NQ, mi.n))
        for (F, d), q in qidx.items():
            dd = JD[d]
            dJ[q] = [BdF[F][miB.ix[tuple(a + b for a, b in zip(bb, dd))]] for bb in mi.L]
        lam = {}
        for ab, e in f.items():
            E = rho * e
            G = E.g if E.g is not None else np.zeros((DM.NQ, mi.n))
            tot = np.zeros(mi.n)
            for q in range(DM.NQ): tot += mi.conv(G[q], dJ[q])
            lam[ab] = tot
        mx_, hx_ = L['xi'][i]; mv_, hv_ = L['v'][j]
        conv = np.array([float(hx_) ** bb[0] * float(hv_) ** bb[1] for bb in mi.L])      # to (t, sigma, x)
        lam_tsx = {ab: (v * conv).tolist() for ab, v in lam.items()}
        byord = {k: max(max(lam_tsx[ab][mi.ix[bb]] for bb in mi.L if sum(bb) == k) for ab in lam_tsx) for k in range(K + 1)}
        res.append(dict(strip=[[str(q) for q in xr], [str(q) for q in vr]], kind=kind, Lambda_by_order=byord,
                        Dmax=float(max(BdF[F][0] for F in FN)), Rlo=Rlo, secs=time.time() - t0))
        print('%s element (%d,%d) strip %s xi [%.4f, %.4f] v [%.4f, %.4f]: max|dF| %.2e; Lambda by order (t, sigma, x): %s (R >= %.2f, %.0f s)' %
              (case, i + 1, j + 1, kind, float(xr[0]), float(xr[1]), float(vr[0]), float(vr[1]), res[-1]['Dmax'],
               ' '.join('%d: %.2e' % (k, v) for k, v in byord.items()), Rlo, res[-1]['secs']), flush=True)
    return res

def strip_coeffs_diff(A_, B_, box, el_a, el_b, nd):
    """strip coefficients (absolute upper bounds) of the polynomial (A_ in element el_a) - (B_ in element el_b)"""
    ca = strip_coeffs_signed(A_, box, el_a, nd); cb = strip_coeffs_signed(B_, box, el_b, nd)
    out = np.zeros(ca.shape)
    it = np.nditer(out, flags=['multi_index'])
    flat_a, flat_b = ca.ravel(), cb.ravel()
    return np.array([float(abs(x - y).upper()) for x, y in zip(flat_a, flat_b)]).reshape(ca.shape)

def strip_coeffs_signed(C, box, el_box, ndeg):
    """as strip_coeffs, returning the balls (object array)"""
    xc, xh, vc, vh = box; mx, hx, mv, hv = el_box
    n1, n2, n3 = C.shape; N1, N2, N3 = ndeg
    P1, P2, P3 = lob(N1), lob(N2), lob(N3)
    q = lambda f: arb(fmpq(f.numerator, f.denominator))
    t = [(q(xc) + q(xh) * p - q(mx)) / q(hx) for p in P1]
    s = [(q(vc) + q(vh) * p - q(mv)) / q(hv) for p in P2]
    V1, V2, V3 = cert.vander(t, n1), cert.vander(s, n2), cert.vander(P3, n3)
    A = arb_mat([[q(C[a, b, k]) if isinstance(C[a, b, k], Fr) else arb(int(C[a, b, k])) for k in range(n3)] for a in range(n1) for b in range(n2)])
    M1 = (A * arb_mat([[V3[l][k] for l in range(N3 + 1)] for k in range(n3)])).entries()
    B2 = arb_mat([[V2[l][b] for b in range(n2)] for l in range(N2 + 1)])
    vals = []
    for a in range(n1):
        Ma = arb_mat([[M1[(a * n2 + b) * (N3 + 1) + l3] for l3 in range(N3 + 1)] for b in range(n2)])
        vals.append((B2 * Ma).entries())
    Vals = arb_mat([[V1[l][a] for a in range(n1)] for l in range(N1 + 1)]) * arb_mat(vals)
    D1, D2, D3 = dct_mat(N1), dct_mat(N2), dct_mat(N3)
    X = (D1 * Vals).entries(); D3t = D3.transpose()
    out = np.empty((N1 + 1, N2 + 1, N3 + 1), dtype=object)
    for i in range(N1 + 1):
        S_ = arb_mat([[X[i * (N2 + 1) * (N3 + 1) + l2 * (N3 + 1) + l3] for l3 in range(N3 + 1)] for l2 in range(N2 + 1)])
        Ci = (D2 * S_ * D3t).entries()
        for l2 in range(N2 + 1):
            for l3 in range(N3 + 1): out[i, l2, l3] = Ci[l2 * (N3 + 1) + l3]
    return out

if __name__ == '__main__':
    a = sys.argv[1:]
    r = overlapK(a[0], a[1], int(a[2]) - 1, int(a[3]) - 1, int(a[4]), int(a[6]) if len(a) > 6 else 256)
    json.dump(r, open(a[5], 'w'), indent=1)
