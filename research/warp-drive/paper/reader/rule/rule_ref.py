#!/usr/bin/env python3
"""rule_ref.py -- an exact reference implementation of the rule of P-APPC2 (proofs/P-APPC2.md, sec:appc-rule), for
small runs.

Written from the text as directly as possible.  A number x of 𝔽 is the Python int X = 2^320 x; a number of 𝔻 (the
short arithmetic, def:appc-short) is a Python float, whose operations +, -, *, / are the binary64 operations with
rounding to nearest, ties to even, each rounded once (CPython uses the platform's IEEE doubles; no fused multiply-add
is involved), and rd of an exact rational is Python's correctly rounded int/int division.  Choices the text leaves open
are marked [Pn] (rule/README.md lists them).

usage:  rule_ref.py CONFIG OUTPREFIX
writes OUTPREFIX.dump (spot values, the computed cells' G, the hand-off digests) and, when the run covers the whole
grid and the config has elements, OUTPREFIX.txt (the canonical string) and OUTPREFIX.digests.

The right-hand side (eq:appc-rhs) is read from solver/rhs_gen.h, which tests/rhs_vs_text.py shows to be the printed
sequence definition by definition, in the same order: its C++ text is valid Python, and each product a*b is rewritten
as (a*b) >> 320 for 𝔽 (Python parses a*b*c as (a*b)*c, as the text reads it), or as a value-and-tangent pair in 𝔻.
"""
import sys, os, re, ast, math, hashlib
from fractions import Fraction as Fr

B = 320
ONE = 1 << B
HALF = 1 << (B - 1)
HERE = os.path.dirname(os.path.abspath(__file__))
RHS_PATH = os.environ.get('RULE_RHS', os.path.join(HERE, '..', 'solver', 'rhs_gen.h'))

# ------------------------------------------------------------------------------------------- def:appc-arith
def fl(q):                      # ⌊q⌋_B: the integer floor(2^B q)
    q = Fr(q); return (q.numerator << B) // q.denominator
def mul(x, y): return (x * y) >> B              # x ⊙ y (>> is the floor for negative values too)
def div(x, y):                                  # x ⊘ y
    if y == 0: raise ZeroDivisionError('⊘ by 0')
    return (x << B) // y
def divi(x, n): return x // n                   # x ⊘ n
def fsqrt(x): assert x >= 0; return math.isqrt(x << B)
def dot(a, g): return sum(p * q for p, q in zip(a, g)) >> B
def rd(X, e=0):                 # rd of the exact rational 2^e X / 2^B (X an int): correctly rounded int/int division
    s = B - e
    return (X << -s) / 1 if s <= 0 else X / (1 << s)
def dotd(a, g):                 # ⟨a, g⟩_𝔻: ((a1 g1 ⊕ a2 g2) ⊕ ...), in the order of the index
    s = a[0] * g[0]
    for i in range(1, len(a)): s = s + a[i] * g[i]
    return s
def floor_scaled(d, nu):        # ⌊2^(−ν) d⌋_B as an integer X (d a float, 2^(−ν) d an exact rational)
    n, den = d.as_integer_ratio(); s = B - nu
    return (n << s) // den if s >= 0 else n // (den << -s)

# ------------------------------------------------------------------------------------------- def:appc-functions
def kz(y):                      # the least k >= 0 with 8|y| <= 2^k, and z := y ⊘ 2^k
    k = 0
    while 8 * abs(y) > (ONE << k): k += 1
    return k, y >> k
def expF(y):                    # (a)
    k, z = kz(y)
    E = ONE
    for n in range(45, 0, -1): E = ONE + divi(mul(z, E), n)
    for _ in range(k): E = mul(E, E)
    return E
def sincosF(y):                 # (b)
    k, z = kz(y)
    u = mul(z, z); S = ONE; C = ONE
    for j in range(22, 0, -1):
        S = ONE - divi(mul(u, S), 2 * j * (2 * j + 1))
        C = ONE - divi(mul(u, C), (2 * j - 1) * 2 * j)
    s, c = mul(z, S), C
    for _ in range(k): s, c = 2 * mul(s, c), mul(c, c) - mul(s, s)
    return s, c
L2 = 2 * sum(ONE // ((2 * j + 1) * 3 ** (2 * j + 1)) for j in range(111))
def logF(y):                    # (c)
    assert y > 0
    m = y.bit_length() - 1 - B                             # 2^m <= y < 2^(m+1)
    w = y >> m if m > 0 else y << (-m)                     # y ⊘ 2^m; the exact product for m <= 0
    if w >= 3 * HALF: w = w >> 1; m += 1                   # w >= 3/2: w := w ⊘ 2
    t = div(w - ONE, w + ONE); u = mul(t, t)
    P = ONE // 141
    for j in range(69, -1, -1): P = ONE // (2 * j + 1) + mul(u, P)
    return m * L2 + 2 * mul(t, P)
def machin_A(q, J):             # (d)
    s = 0
    for j in range(J + 1):
        t = ONE // ((2 * j + 1) * q ** (2 * j + 1))
        s += -t if j % 2 else t
    return s
PI = 16 * machin_A(5, 70) - 4 * machin_A(239, 20)
def chat(j, n):                 # (e) ĉ(j, n), standing for cos(π j/n)
    j %= 2 * n
    if j == 0: return ONE
    if j == n: return -ONE
    if j > n: j = 2 * n - j
    return sincosF(divi(j * PI, n))[1]
def sinhcosh(y):                # (f)
    e1, e2 = expF(y), expF(-y)
    return divi(e1 - e2, 2), divi(e1 + e2, 2)
XI0 = -logF(4500 * ONE + fsqrt(20250001 * ONE))          # (g)
AH = fl(Fr(1, 500))

# ------------------------------------------------------------------------------------------- def:appc-nodes
def lobatto(p): return [-chat(j, p) for j in range(p + 1)]
def radau(p): return [chat(2 * (p - j), 2 * p + 1) for j in range(p + 1)]
def xnodes(M): return [chat(k, M) for k in range(M + 1)]
def pmul_lin(c, r):
    out = [0] * (len(c) + 1)
    for m, cm in enumerate(c): out[m + 1] += cm; out[m] -= r * cm
    return out
def horner(c, t):
    s = 0
    for cm in reversed(c): s = s * t + cm
    return s
def lagrange_int(T):            # integer polynomials Ñ_j(X) = Π_{i≠j} (X − T_i), d_j = Π_{i≠j} (T_j − T_i)
    out = []
    for j in range(len(T)):
        c = [1]; d = 1
        for i in range(len(T)):
            if i != j: c = pmul_lin(c, T[i]); d *= T[j] - T[i]
        out.append((c, d))
    return out
def Dmat(T, order=1):           # ℓ'_j(τ_i) = 2^B Ñ_j'(T_i)/d_j, ℓ''_j(τ_i) = 2^(2B) Ñ_j''(T_i)/d_j, by Horner
    LP = lagrange_int(T); out = []
    for i in range(len(T)):
        row = []
        for (c, d) in LP:
            dc = [m * c[m] for m in range(1, len(c))]
            if order == 2: dc = [m * dc[m] for m in range(1, len(dc))]
            row.append(fl(Fr(horner(dc, T[i]) * ONE ** order, d)))
        out.append(row)
    return out
def basis_frac(nodes):          # Lagrange basis as Fraction coefficient lists
    polys = []
    for j in range(len(nodes)):
        c = [Fr(1)]; d = Fr(1)
        for i in range(len(nodes)):
            if i != j: c = pmul_lin(c, nodes[i]); d *= nodes[j] - nodes[i]
        polys.append([cm / d for cm in c])
    return polys
def Qmat(T):                    # Q_ij = ∫_{-1}^{τ_i} ℓ_j
    nodes = [Fr(t, ONE) for t in T]; out = []
    polys = basis_frac(nodes)
    for i in range(len(T)):
        row = []
        for c in polys:
            I = [Fr(0)] + [cm / (m + 1) for m, cm in enumerate(c)]
            row.append(fl(horner(I, nodes[i]) - horner(I, Fr(-1))))
        out.append(row)
    return out
def WV(T):                      # σ_i := (τ_i + 1)/2 exactly, λ_j(σ) := ℓ_j(2σ − 1)
    sig = [(Fr(t, ONE) + 1) / 2 for t in T]; W = []; V = []
    polys = basis_frac(sig)                                # λ_j is the Lagrange basis of the σ_i
    for i in range(len(T)):
        rw, rv = [], []; si = sig[i]
        for c in polys:
            c3 = [Fr(0)] * 3 + c; c2 = [Fr(0)] * 2 + c
            I3 = [Fr(0)] + [a / (m + 1) for m, a in enumerate(c3)]
            I2 = [Fr(0)] + [a / (m + 1) for m, a in enumerate(c2)]
            rw.append(fl(horner(I3, si) / si ** 4))
            rv.append(fl((si * horner(I2, si) - horner(I3, si)) / si ** 4))
        W.append(rw); V.append(rv)
    return W, V
def dotsq(A):
    n = len(A); cols = [[A[l][j] for l in range(n)] for j in range(n)]
    return [[dot(A[i], cols[j]) for j in range(n)] for i in range(n)]
def lagr_values(nodes, t):      # ⌊ℓ_j(t)⌋_B, exactly
    out = []
    for j in range(len(nodes)):
        num, den = 1, 1
        for i in range(len(nodes)):
            if i != j: num *= t - nodes[i]; den *= nodes[j] - nodes[i]
        out.append(fl(Fr(num, den)))
    return out
def cheb_t(N):                  # Ĉ^N_na = ⌊2 ω_n ω_a ĉ(n(N − a), N)/N⌋_B
    w = lambda q: Fr(1, 2) if q in (0, N) else Fr(1)
    return [[fl(2 * w(n) * w(a) * Fr(chat(n * (N - a), N), ONE) / N) for a in range(N + 1)] for n in range(N + 1)]
def cheb_x(M):                  # Ĉ^(x,M)_nk = ⌊2 ω_n ω_k ĉ(nk, M)/M⌋_B
    w = lambda q: Fr(1, 2) if q in (0, M) else Fr(1)
    return [[fl(2 * w(n) * w(k) * Fr(chat(n * k, M), ONE) / M) for k in range(M + 1)] for n in range(M + 1)]
def resample(L, M, M2):         # def:appc-resample
    c = [dot(row, L) for row in cheb_x(M)]
    return [dot([chat(n * k2, M2) for n in range(M + 1)], c) for k2 in range(M2 + 1)]

# ------------------------------------------------------------------------------------------- def:appc-rule-seed
def seed(xi, v):
    sh, ch = sinhcosh(xi)
    u1 = mul(AH, sh); u = u1 - ONE
    H = v - 2 * u + logF(div(u1, u1 - 2 * ONE))
    r0 = ONE + (1 << (B - 32)); r1 = divi(max(H, 0), 2) + 3 * ONE
    for _ in range(80):
        q = divi(r0 + r1, 2)
        if 2 * q + logF(div(q - ONE, q + ONE)) < H: r0 = q
        else: r1 = q
    R = r0
    for _ in range(6):
        R = R - div(2 * R + logF(div(R - ONE, R + ONE)) - H, 2 * ONE + div(2 * ONE, mul(R, R) - ONE))
    f = ONE - div(ONE, mul(R, R)); g = ONE - div(ONE, mul(u, u))
    return dict(R=R, Rv=divi(f, 2), Ru=-div(f, g), OM2=div(f, 2 * g), Wv=div(ONE, 2 * mul(mul(R, R), R)),
                uxi=mul(AH, ch))

# ------------------------------------------------------------------------------------------- the right-hand side
def load_rhs(path):
    txt = open(path).read()
    jets = re.findall(r'"([^"]+)"', re.search(r'RHS_JET\[\] = \{(.*?)\};', txt).group(1))
    knum = [int(a) for a in re.search(r'RHS_KNUM\[\] = \{(.*?)\};', txt).group(1).split(',')]
    kden = [int(a) for a in re.search(r'RHS_KDEN\[\] = \{(.*?)\};', txt).group(1).split(',')]
    body = re.findall(r'^\s*const auto (\w+) = (.*);\s*$', txt, re.M)
    # 𝔽: every product floored
    class FloorProducts(ast.NodeTransformer):
        def visit_BinOp(self, node):
            self.generic_visit(node)
            return ast.BinOp(left=node, op=ast.RShift(), right=ast.Constant(B)) if isinstance(node.op, ast.Mult) else node
    lines = ['def rhs(J, K, x):', '    ' + ', '.join(jets) + ' = J']
    for name, expr in body:
        lines.append('    %s = %s' % (name, ast.unparse(ast.fix_missing_locations(FloorProducts().visit(ast.parse(expr, mode='eval'))))))
    lines.append('    return (Xm, Xn, XR, XW, Svv)')
    # 𝔻 pairs: value and tangent; a ⊙ b -> (ā b̄, ȧ b̄ + ā ḃ); sums from the left; constants and x carry tangent 0
    pl = ['def rhs_pair(Jv, Jt, Kd, xd):', '    ' + ', '.join(j + '_v' for j in jets) + ' = Jv',
          '    ' + ', '.join(j + '_t' for j in jets) + ' = Jt']
    cnt = [0]
    def emit(node):
        if isinstance(node, ast.Name):
            return (node.id + '_v', node.id + '_t') if node.id != 'x' else ('xd', '0.0')
        if isinstance(node, ast.Subscript):                  # K[i]
            return ('Kd[%d]' % node.slice.value, '0.0')
        if isinstance(node, ast.UnaryOp):
            v, t = emit(node.operand); cnt[0] += 1; n = '_u%d' % cnt[0]
            pl.append('    %s_v = -%s; %s_t = -%s' % (n, v, n, t)); return (n + '_v', n + '_t')
        if isinstance(node, ast.BinOp):
            av, at = emit(node.left); bv, bt = emit(node.right); cnt[0] += 1; n = '_b%d' % cnt[0]
            if isinstance(node.op, ast.Mult): pl.append('    %s_v = %s * %s; %s_t = %s * %s + %s * %s' % (n, av, bv, n, at, bv, av, bt))
            elif isinstance(node.op, ast.Add): pl.append('    %s_v = %s + %s; %s_t = %s + %s' % (n, av, bv, n, at, bt))
            elif isinstance(node.op, ast.Sub): pl.append('    %s_v = %s - %s; %s_t = %s - %s' % (n, av, bv, n, at, bt))
            else: raise ValueError(node.op)
            return (n + '_v', n + '_t')
        raise ValueError(node)
    for name, expr in body:
        v, t = emit(ast.parse(expr, mode='eval').body)
        pl.append('    %s_v = %s; %s_t = %s' % (name, v, name, t))
    pl.append('    return (Xm_t, Xn_t, XR_t, XW_t, Svv_t)')
    ns = {}
    exec('\n'.join(lines), ns); exec('\n'.join(pl), ns)
    K = [fl(Fr(a, b)) for a, b in zip(knum, kden)]
    Kd = [a / b for a, b in zip(knum, kden)]                 # rd q
    return jets, K, Kd, ns['rhs'], ns['rhs_pair']
JETS, KC, KD, RHS, RHS_PAIR = load_rhs(RHS_PATH)

# ------------------------------------------------------------------------------------------- configuration
class Case:
    def __init__(self, fn):
        self.elems = []; self.run_cols = None; self.run_rows = None; self.NRay = 40; self.segs = []
        for line in open(fn):
            t = line.split('#')[0].split()
            if not t: continue
            k = t[0]
            if k == 'seed': self.seed = int(t[1])
            elif k == 'xi_e': self.xi_e = Fr(t[1])
            elif k == 'v_e': self.v_e = Fr(t[1])
            elif k == 'ncol': self.nc = int(t[1])
            elif k == 'nrow': self.nr = int(t[1])
            elif k == 'pxi': self.pxi = int(t[1])
            elif k == 'pv': self.pv = int(t[1])
            elif k == 'segment': self.segs.append(tuple(int(a) for a in t[1:6]))      # c0 c1 M No Ni
            elif k == 'NRay': self.NRay = int(t[1])
            elif k == 'p': self.p = int(t[1])
            elif k == 'run_cols': self.run_cols = int(t[1])
            elif k == 'run_rows': self.run_rows = int(t[1])
            elif k == 'elem': self.elems.append((int(t[1]), int(t[2])) + tuple(Fr(a) for a in t[3:7]) + (int(t[7]), int(t[8])))
            elif k in ('threads', 'batch', 'ckpt_minutes', 'out'): pass
            else: raise ValueError('unknown key ' + k)
        if self.run_cols is None: self.run_cols = self.nc
        if self.run_rows is None: self.run_rows = self.nr
    def seg_of(self, i):
        for s, sg in enumerate(self.segs):
            if sg[0] <= i < sg[1]: return s
        raise ValueError(i)

# ------------------------------------------------------------------------------------------- the run
def main():
    cs = Case(sys.argv[1]); out = sys.argv[2]
    lam = ONE if cs.seed == 1 else fsqrt(fl(Fr(1, 10)))
    NF = 5; FR_, FM_, FN_, FW_, FS_ = range(5)
    XB = [XI0 + divi(i * (fl(cs.xi_e) - XI0), cs.nc) for i in range(cs.nc + 1)]          # def:appc-grid
    VB = [HALF + divi(j * (fl(cs.v_e) - HALF), cs.nr) for j in range(cs.nr + 1)]
    nA, nB = cs.pxi + 1, cs.pv + 1
    TL, TV, TR = lobatto(cs.pxi), lobatto(cs.pv), radau(cs.pv)
    Dxi, Qxi = Dmat(TL), Qmat(TL)
    DvL, QvL = Dmat(TV), Qmat(TV); QQ = dotsq(QvL)
    DvR, QvR = Dmat(TR), Qmat(TR); W, V = WV(TR)
    xcache = {}
    def xmats(M):
        if M not in xcache:
            X = xnodes(M); xcache[M] = (X, Dmat(X, 1), Dmat(X, 2))
        return xcache[M]
    spot = {'pi': PI, 'log2': L2, 'xi0': XI0, 'a': AH, 'lambda': lam, 'Rs(xi0,1/2)': seed(XI0, HALF)['R'],
            'exp 1': expF(ONE), 'log 3': logF(3 * ONE), 'sin 1': sincosF(ONE)[0]}
    log = []

    def vnodes(j):
        hv = divi(VB[j + 1] - VB[j], 2)
        return hv, [VB[j] + mul(hv, t + ONE) for t in (TR if j == 0 else TV)]
    def epowers(vs):
        eps = [v - HALF for v in vs]; e2 = [mul(e, e) for e in eps]
        e3 = [mul(a, e) for a, e in zip(e2, eps)]; e4 = [mul(a, e) for a, e in zip(e3, eps)]
        return eps, e2, e3, e4

    # def:appc-rule-data
    M0 = cs.segs[0][2]; X0 = xmats(M0)[0]
    def n1_row(j, prev):
        hv, vs = vnodes(j); first = j == 0
        Dv = DvR if first else DvL; Qv = QvR if first else QvL
        eps, e2, e3, e4 = epowers(vs); ihv = div(ONE, hv)
        sd = [seed(XI0, v) for v in vs]
        NX = M0 + 1
        if not first: eta = VB[j] - HALF; eta4 = mul(mul(mul(eta, eta), eta), eta); Gam, Ups = prev
        Gm = [[0] * NX for _ in range(nB)]; Gn = [[0] * NX for _ in range(nB)]; sig6 = [[0] * NX for _ in range(nB)]
        GR = [[0] * NX for _ in range(nB)]
        for b in range(nB):
            r = sd[b]['R']; e = eps[b]
            z = divi(mul(PI, e), 3); sz, cz = sincosF(z)
            q1 = mul(divi(PI, 3), div(sz, z)); q2 = mul(q1, q1); q3 = mul(q2, q1); q4 = mul(q2, q2)
            st, ct = sincosF(div(vs[b], lam))
            fr = ONE - div(ONE, mul(r, r))
            a1 = -mul(mul(div(divi(3 * fr, 4), r), e), q4)
            a2 = mul(mul(divi(4 * PI, 3), q3), cz)
            a3 = div(mul(e, q4), lam)
            for k in range(NX):
                x = X0[k]
                h = fsqrt(div(2 * ONE, ONE + mul(x, x)))
                kap = mul(divi(mul(h, lam), 2), div(ONE, mul(r, fsqrt(r))))
                Gm[b][k] = mul(mul(kap, q4), ct); Gn[b][k] = mul(mul(kap, q4), st)
                m3 = mul(kap, mul(a1 + a2, ct) - mul(a3, st)); n3 = mul(kap, mul(a1 + a2, st) + mul(a3, ct))
                P3 = divi(mul(2 * (ONE + x), m3) - mul(ONE - x, n3), 3)
                Q3 = divi(mul(2 * (ONE - x), n3) - mul(ONE + x, m3), 3)
                sig6[b][k] = mul(P3, P3) + mul(Q3, Q3) + mul(P3 + Q3, P3 + Q3)
                if not first: GR[b][k] = div(mul(eta4, Gam[k]) + mul(vs[b] - VB[j], Ups[k]), e4[b])
        rho = None
        for it in range(cs.NRay):
            rho = [[0] * NX for _ in range(nB)]
            for b in range(nB):
                for k in range(NX):
                    g = mul(dot(Dv[b], [GR[bb][k] for bb in range(nB)]), ihv)
                    Dl = 4 * mul(e3[b], GR[b][k]) + mul(e4[b], g)
                    Rt = sd[b]['R'] + mul(e4[b], GR[b][k])
                    rho[b][k] = 2 * mul(sd[b]['Wv'], Dl) - divi(mul(mul(mul(Rt, sig6[b][k]), e4[b]), e2[b]), 3)
            new = [[0] * NX for _ in range(nB)]
            ie2 = [div(ONE, a) for a in e2]
            for b in range(nB):
                for k in range(NX):
                    if first: new[b][k] = dot(V[b], [mul(rho[bb][k], ie2[bb]) for bb in range(nB)])
                    else: new[b][k] = div(mul(eta4, Gam[k]) + mul(vs[b] - VB[j], Ups[k]) + mul(mul(hv, hv), dot(QQ[b], [rho[bb][k] for bb in range(nB)])), e4[b])
            GR = new
        Gam2 = [GR[nB - 1][k] for k in range(NX)]
        Ups2 = [(0 if first else Ups[k]) + mul(hv, dot(Qv[nB - 1], [rho[bb][k] for bb in range(nB)])) for k in range(NX)]
        return [GR, Gm, Gn, [[0] * NX for _ in range(nB)]], (Gam2, Ups2)

    # def:appc-cell, def:appc-iteration
    def solve_cell(i, j, left, low):
        sg = cs.segs[cs.seg_of(i)]; M, No, Ni = sg[2], sg[3], sg[4]
        X, D1, D2 = xmats(M); NX = M + 1; first = j == 0
        hxi = divi(XB[i + 1] - XB[i], 2); xis = [XB[i] + mul(hxi, t + ONE) for t in TL]
        hv, vs = vnodes(j)
        Dv = DvR if first else DvL; Qv = QvR if first else QvL
        eps, e2, e3, e4 = epowers(vs)
        ihxi, ihv = div(ONE, hxi), div(ONE, hv)
        ie2 = [div(ONE, a) for a in e2]; ie3 = [div(ONE, a) for a in e3]
        sd = [[seed(xis[a], vs[b]) for b in range(nB)] for a in range(nA)]
        iux = [[div(ONE, sd[a][b]['uxi']) for b in range(nB)] for a in range(nA)]
        Bt = [[[[0] * NX for _ in range(nB)] for _ in range(nA)] for _ in range(NF)]
        if not first: eta = VB[j] - HALF; eta4 = mul(mul(mul(eta, eta), eta), eta)
        for f in range(NF):
            for a in range(nA):
                for b in range(nB):
                    for k in range(NX):
                        if first: val = left[f][b][k] if f < 4 else 0
                        elif f < 4: val = div(mul(eta4, low['T'][f][a][k]) + mul(e4[b], left[f][b][k]) - mul(eta4, low['T'][f][0][k]), e4[b])
                        else: val = div(mul(eta4, low['T'][f][a][k]) + mul(vs[b] - VB[j], low['s'][a][k]), e4[b])
                        Bt[f][a][b][k] = val
        def jets(a, b, k, Dj):
            s = sd[a][b]; x = X[k]
            R = s['R'] + Dj['D'][FR_]
            S = divi(Dj['D'][FM_] + mul(x, Dj['D'][FM_]) + Dj['D'][FN_] - mul(x, Dj['D'][FN_]), 3)
            J = [R, div(ONE, R), expF(S), expF(-S), mul(s['OM2'], expF(2 * Dj['D'][FW_])),
                 mul(div(ONE, s['OM2']), expF(-2 * Dj['D'][FW_])),
                 s['Ru'] + Dj['Du'][FR_], s['Rv'] + Dj['Dv'][FR_], Dj['Dx'][FR_], Dj['Dxx'][FR_], Dj['Dvx'][FR_],
                 s['Wv'] + Dj['Dv'][FW_], Dj['Dx'][FW_], Dj['Dxx'][FW_], Dj['Dvx'][FW_]]
            for f in (FM_, FN_): J += [Dj['D'][f], Dj['Du'][f], Dj['Dv'][f], Dj['Dx'][f], Dj['Dxx'][f], Dj['Dvx'][f]]
            J += [Dj['D'][FS_], Dj['Dv'][FS_], Dj['Dx'][FS_], Dj['Dvx'][FS_]]
            return J
        zero = {q: [0] * 5 for q in ('D', 'Du', 'Dv', 'Dx', 'Dxx', 'Dvx')}
        Xs = [[[RHS(jets(a, b, k, zero), KC, X[k]) for k in range(NX)] for b in range(nB)] for a in range(nA)]

        def P(G):                  # P(G) = B + I(G), Φ, and the jets J(G) rounded by rd
            Psi = [[[[0] * NX for _ in range(nB)] for _ in range(nA)] for _ in range(4)]
            Phi = [[[0] * NX for _ in range(nB)] for _ in range(nA)]
            Jbar = [[[None] * NX for _ in range(nB)] for _ in range(nA)]
            for a in range(nA):
                for b in range(nB):
                    Gv = [[mul(dot(Dv[b], [G[f][a][bb][k] for bb in range(nB)]), ihv) for k in range(NX)] for f in range(NF)]
                    Gxi = [[mul(dot(Dxi[a], [G[f][aa][b][k] for aa in range(nA)]), ihxi) for k in range(NX)] for f in range(3)]
                    for k in range(NX):
                        Dj = {q: [0] * 5 for q in ('D', 'Du', 'Dv', 'Dx', 'Dxx', 'Dvx')}
                        for f in range(NF):
                            g = G[f][a][b][k]; gx = dot(D1[k], G[f][a][b]); gvx = dot(D1[k], Gv[f])
                            Dj['D'][f] = mul(e4[b], g); Dj['Dx'][f] = mul(e4[b], gx)
                            Dj['Dv'][f] = 4 * mul(e3[b], g) + mul(e4[b], Gv[f][k])
                            Dj['Dvx'][f] = 4 * mul(e3[b], gx) + mul(e4[b], gvx)
                            if f < 4: Dj['Dxx'][f] = mul(e4[b], dot(D2[k], G[f][a][b]))
                            if f < 3: Dj['Du'][f] = mul(mul(e4[b], Gxi[f][k]), iux[a][b])
                        J = jets(a, b, k, Dj); Jbar[a][b][k] = [rd(q) for q in J]
                        o = RHS(J, KC, X[k]); os_ = Xs[a][b][k]; u = sd[a][b]['uxi']
                        Psi[FR_][a][b][k] = mul(u, o[2] - os_[2]); Psi[FM_][a][b][k] = mul(u, o[0] - os_[0])
                        Psi[FN_][a][b][k] = mul(u, o[1] - os_[1]); Psi[FW_][a][b][k] = mul(u, o[3] - os_[3])
                        Phi[a][b][k] = o[4] - os_[4]
            I = [[[[0] * NX for _ in range(nB)] for _ in range(nA)] for _ in range(NF)]
            for f in range(4):
                if first: T = [[[dot(W[b], [mul(Psi[f][a][bb][k], ie3[bb]) for bb in range(nB)]) for k in range(NX)] for b in range(nB)] for a in range(nA)]
                else: T = [[[dot(Qv[b], [Psi[f][a][bb][k] for bb in range(nB)]) for k in range(NX)] for b in range(nB)] for a in range(nA)]
                for a in range(nA):
                    for b in range(nB):
                        for k in range(NX):
                            t = dot(Qxi[a], [T[aa][b][k] for aa in range(nA)])
                            I[f][a][b][k] = mul(hxi, t) if first else div(mul(mul(hxi, hv), t), e4[b])
            for a in range(nA):
                for b in range(nB):
                    for k in range(NX):
                        if first: I[FS_][a][b][k] = dot(V[b], [mul(Phi[a][bb][k], ie2[bb]) for bb in range(nB)])
                        else: I[FS_][a][b][k] = div(mul(mul(hv, hv), dot(QQ[b], [Phi[a][bb][k] for bb in range(nB)])), e4[b])
            PG = [[[[Bt[f][a][b][k] + I[f][a][b][k] for k in range(NX)] for b in range(nB)] for a in range(nA)] for f in range(NF)]
            return PG, Phi, Jbar

        # the cell's numbers in 𝔻 (def:appc-iteration (iv))
        rdm = lambda A: [[rd(q) for q in row] for row in A]
        Dvd, Qvd, Dxid, Qxid, D1d, D2d = rdm(Dv), rdm(Qv), rdm(Dxi), rdm(Qxi), rdm(D1), rdm(D2)
        Wd, Vd, QQd = rdm(W), rdm(V), rdm(QQ)
        hxid, hvd, ihxid, ihvd = rd(hxi), rd(hv), rd(ihxi), rd(ihv)
        e2d, e3d, e4d, ie2d, ie3d = [rd(q) for q in e2], [rd(q) for q in e3], [rd(q) for q in e4], [rd(q) for q in ie2], [rd(q) for q in ie3]
        uxd = [[rd(sd[a][b]['uxi']) for b in range(nB)] for a in range(nA)]
        iuxd = [[rd(iux[a][b]) for b in range(nB)] for a in range(nA)]
        Xd = [rd(q) for q in X]

        def Ilin(d, Jbar):         # I_𝔻(d)
            Psid = [[[[0.0] * NX for _ in range(nB)] for _ in range(nA)] for _ in range(4)]
            Phid = [[[0.0] * NX for _ in range(nB)] for _ in range(nA)]
            for a in range(nA):
                for b in range(nB):
                    dv = [[dotd(Dvd[b], [d[f][a][bb][k] for bb in range(nB)]) * ihvd for k in range(NX)] for f in range(NF)]
                    dxi = [[dotd(Dxid[a], [d[f][aa][b][k] for aa in range(nA)]) * ihxid for k in range(NX)] for f in range(3)]
                    for k in range(NX):
                        Dd = [0.0] * 5; Dx = [0.0] * 5; Dxx = [0.0] * 5; Dvv = [0.0] * 5; Dvx = [0.0] * 5; Du = [0.0] * 5
                        for f in range(NF):
                            g = d[f][a][b][k]; gx = dotd(D1d[k], d[f][a][b]); gvx = dotd(D1d[k], dv[f])
                            Dd[f] = e4d[b] * g; Dx[f] = e4d[b] * gx
                            Dvv[f] = 4 * (e3d[b] * g) + e4d[b] * dv[f][k]
                            Dvx[f] = 4 * (e3d[b] * gx) + e4d[b] * gvx
                            if f < 4: Dxx[f] = e4d[b] * dotd(D2d[k], d[f][a][b])
                            if f < 3: Du[f] = (e4d[b] * dxi[f][k]) * iuxd[a][b]
                        Jv = Jbar[a][b][k]; xb = Xd[k]
                        Sdot = (((Dd[FM_] + xb * Dd[FM_]) + Dd[FN_]) - xb * Dd[FN_]) / 3.0
                        Jt = [Dd[FR_], -((Jv[1] * Jv[1]) * Dd[FR_]), Jv[2] * Sdot, -(Jv[3] * Sdot),
                              Jv[4] * (2 * Dd[FW_]), -(Jv[5] * (2 * Dd[FW_])),
                              Du[FR_], Dvv[FR_], Dx[FR_], Dxx[FR_], Dvx[FR_], Dvv[FW_], Dx[FW_], Dxx[FW_], Dvx[FW_]]
                        for f in (FM_, FN_): Jt += [Dd[f], Du[f], Dvv[f], Dx[f], Dxx[f], Dvx[f]]
                        Jt += [Dd[FS_], Dvv[FS_], Dx[FS_], Dvx[FS_]]
                        o = RHS_PAIR(Jv, Jt, KD, xb); u = uxd[a][b]
                        Psid[FR_][a][b][k] = u * o[2]; Psid[FM_][a][b][k] = u * o[0]
                        Psid[FN_][a][b][k] = u * o[1]; Psid[FW_][a][b][k] = u * o[3]; Phid[a][b][k] = o[4]
            I = [[[[0.0] * NX for _ in range(nB)] for _ in range(nA)] for _ in range(NF)]
            for f in range(4):
                if first: T = [[[dotd(Wd[b], [Psid[f][a][bb][k] * ie3d[bb] for bb in range(nB)]) for k in range(NX)] for b in range(nB)] for a in range(nA)]
                else: T = [[[dotd(Qvd[b], [Psid[f][a][bb][k] for bb in range(nB)]) for k in range(NX)] for b in range(nB)] for a in range(nA)]
                for a in range(nA):
                    for b in range(nB):
                        for k in range(NX):
                            t = dotd(Qxid[a], [T[aa][b][k] for aa in range(nA)])
                            I[f][a][b][k] = hxid * t if first else ((hxid * hvd) * t) / e4d[b]
            for a in range(nA):
                for b in range(nB):
                    for k in range(NX):
                        if first: I[FS_][a][b][k] = dotd(Vd[b], [Phid[a][bb][k] * ie2d[bb] for bb in range(nB)])
                        else: I[FS_][a][b][k] = ((hvd * hvd) * dotd(QQd[b], [Phid[a][bb][k] for bb in range(nB)])) / e4d[b]
            return I

        G = [[[list(r) for r in pl] for pl in fld] for fld in Bt]
        lastPhi = None; rmax = []
        idx = [(f, a, b, k) for f in range(NF) for a in range(nA) for b in range(nB) for k in range(NX)]
        for o in range(No):
            PG, Phi, Jbar = P(G); lastPhi = Phi
            r = {t: PG[t[0]][t[1]][t[2]][t[3]] - G[t[0]][t[1]][t[2]][t[3]] for t in idx}
            R = max(abs(v) for v in r.values()); rmax.append(R)
            if R == 0: continue
            nu = 321 - R.bit_length()                         # 2^(−ν) <= max|r| < 2^(1−ν)
            rt = {t: rd(v, nu) for t, v in r.items()}
            d = [[[[rt[(f, a, b, k)] for k in range(NX)] for b in range(nB)] for a in range(nA)] for f in range(NF)]
            for it in range(Ni):
                Id = Ilin(d, Jbar)
                d = [[[[rt[(f, a, b, k)] + Id[f][a][b][k] for k in range(NX)] for b in range(nB)] for a in range(nA)] for f in range(NF)]
            for (f, a, b, k) in idx: G[f][a][b][k] += floor_scaled(d[f][a][b][k], nu)
        right = [[[G[f][nA - 1][b][k] for k in range(NX)] for b in range(nB)] for f in range(4)]
        sv = [[(0 if first else low['s'][a][k]) + mul(hv, dot(Qv[nB - 1], [lastPhi[a][bb][k] for bb in range(nB)])) for k in range(NX)] for a in range(nA)]
        top = {'T': [[[G[f][a][nB - 1][k] for k in range(NX)] for a in range(nA)] for f in range(NF)], 's': sv}
        return dict(G=G, right=right, top=top, rmax=rmax, M=M)

    # the march, with segments and their hand-offs
    n1 = []; prev = None
    for j in range(cs.run_rows):
        e, prev = n1_row(j, prev); n1.append(e)
    hv0, vs0 = vnodes(0)
    spot['Rs(first node of cell (0,0))'] = seed(XB[0] + mul(divi(XB[1] - XB[0], 2), TL[0] + ONE), vs0[0])['R']
    spot['G_m(N1, row 0, v_0, x_0)'] = n1[0][FM_][0][0]; spot['G_R(N1, row 0, v_0, x_0)'] = n1[0][FR_][0][0]
    spot['G_m(N1, row 0, v_pv, x_0)'] = n1[0][FM_][nB - 1][0]; spot['G_R(N1, row 0, v_pv, x_0)'] = n1[0][FR_][nB - 1][0]
    cells = {}; handoffs = []
    for i in range(cs.run_cols):
        for j in range(cs.run_rows):
            if i == 0: left = n1[j]
            else:
                left = cells[(i - 1, j)]['right']
                Mp, Mi = cells[(i - 1, j)]['M'], cs.segs[cs.seg_of(i)][2]
                if Mp != Mi: left = [[resample(left[f][b], Mp, Mi) for b in range(nB)] for f in range(4)]
            cells[(i, j)] = solve_cell(i, j, left, cells[(i, j - 1)]['top'] if j else None)
            print('cell', i, j, 'done', file=sys.stderr)
        s = cs.seg_of(i)
        if i == cs.segs[s][1] - 1 and cs.run_rows == cs.nr:                # def:appc-handoff
            txt = ''.join('edge %d %d %s %s\n' % (j, b, 'RmnW'[f], ' '.join(str(v) for v in cells[(i, j)]['right'][f][b]))
                          for j in range(cs.nr) for f in range(4) for b in range(nB))
            handoffs.append((s, hashlib.sha256(txt.encode()).hexdigest()))
    for o, R in enumerate(cells[(0, 0)]['rmax']): spot['max|r| cell (0,0) outer %d' % (o + 1)] = R
    spot['G_m(p_xi,p_v,0) cell (0,0)'] = cells[(0, 0)]['G'][FM_][nA - 1][nB - 1][0]
    if (0, 1) in cells: spot['G_m(p_xi,p_v,0) cell (0,1)'] = cells[(0, 1)]['G'][FM_][nA - 1][nB - 1][0]
    with open(out + '.dump', 'w') as fo:
        for k_, v_ in spot.items(): fo.write('spot %s %d\n' % (k_, v_))
        for s, h in handoffs: fo.write('handoff %d sha256 %s\n' % (s, h))
        for (i, j) in sorted(cells):
            G = cells[(i, j)]['G']; NX = cells[(i, j)]['M'] + 1
            txt = ''.join('%d %d %d %d %d\n' % (f, a, b, k, G[f][a][b][k]) for f in range(NF) for a in range(nA) for b in range(nB) for k in range(NX))
            sv = cells[(i, j)]['top']['s']
            fo.write('cell %d %d sha256 %s sv %s\n' % (i, j, hashlib.sha256(txt.encode()).hexdigest(),
                     hashlib.sha256(''.join('%d\n' % sv[a][k] for a in range(nA) for k in range(NX)).encode()).hexdigest()))
    if cs.run_cols < cs.nc or cs.run_rows < cs.nr or not cs.elems: return

    # def:appc-element-values, def:appc-canonical, def:appc-digest
    FNAMES = 'RmnWs'; text = []; digests = []; case_hash = hashlib.sha256(); first_value = None
    for (ii, jj, lo, hi, vlo, vhi, Nt, Ns) in cs.elems:
        mi, hi_ = fl((lo + hi) / 2), fl((hi - lo) / 2); mj, hj = fl((vlo + vhi) / 2), fl((vhi - vlo) / 2)
        xn = [mi - mul(hi_, chat(a, Nt)) for a in range(Nt + 1)]
        vn = [mj - mul(hj, chat(b, Ns)) for b in range(Ns + 1)]
        def owner(t, br, n):
            for c in range(n):
                if t <= br[c + 1]: return c
            return n - 1
        ic = [owner(t, XB, cs.nc) for t in xn]; jc = [owner(t, VB, cs.nr) for t in vn]
        Me = max(cs.segs[cs.seg_of(i)][2] for i in set(ic))
        Gam = [[[[0] * (Me + 1) for _ in range(Ns + 1)] for _ in range(Nt + 1)] for _ in range(NF)]
        for a in range(Nt + 1):
            i = ic[a]; hxi = divi(XB[i + 1] - XB[i], 2); taus = div(xn[a] - XB[i], hxi) - ONE
            lx = lagr_values(TL, taus)
            for b in range(Ns + 1):
                j = jc[b]; hv = divi(VB[j + 1] - VB[j], 2); vs_ = div(vn[b] - VB[j], hv) - ONE
                lv = lagr_values(TR if j == 0 else TV, vs_)
                c = cells[(i, j)]; G = c['G']; M = c['M']
                for f in range(NF):
                    val = [dot(lx, [dot(lv, [G[f][a2][b2][k] for b2 in range(nB)]) for a2 in range(nA)]) for k in range(M + 1)]
                    if M != Me: val = resample(val, M, Me)
                    Gam[f][a][b] = val
        if first_value is None: first_value = Gam[FM_][0][0][0]
        Cx, Cs, Ct = cheb_x(Me), cheb_t(Ns), cheb_t(Nt)
        for f in range(NF):
            c1 = [[[dot(Cx[n], Gam[f][a][b]) for n in range(Me + 1)] for b in range(Ns + 1)] for a in range(Nt + 1)]
            c2 = [[[dot(Cs[m], [c1[a][b][n] for b in range(Ns + 1)]) for n in range(Me + 1)] for m in range(Ns + 1)] for a in range(Nt + 1)]
            z = [[[(10 ** cs.p * dot(Ct[l], [c2[a][m][n] for a in range(Nt + 1)]) + HALF) >> B for n in range(Me + 1)] for m in range(Ns + 1)] for l in range(Nt + 1)]
            lines = ['block %d %d %s %d %d %d %d' % (ii, jj, FNAMES[f], cs.p, Nt, Ns, Me)]
            S1 = S2 = S0 = nnz = 0
            for a in range(Nt + 1):
                for b in range(Ns + 1):
                    row = z[a][b]; K = max((k for k in range(Me + 1) if row[k] != 0), default=-1)
                    for k in range(Me + 1):
                        if row[k]:
                            nnz += 1; S1 += row[k]; S2 += row[k] * (-1) ** (a + b + k)
                            if a % 2 == 0 and b % 2 == 0 and k % 2 == 0: S0 += row[k] * (-1) ** ((a + b + k) // 2)
                    if K >= 0: lines.append('%d %d %s' % (a, b, ' '.join(str(row[k]) for k in range(K + 1))))
            blk = ''.join(l + '\n' for l in lines); text.append(blk); case_hash.update(blk.encode())
            get = lambda a, b, k: z[a][b][k] if a <= Nt and b <= Ns and k <= Me else 0
            digests.append('block %d %d %s sha256 %s nonzero %d S1 %d S2 %d S0 %d z000 %d z100 %d z010 %d z001 %d' %
                           (ii, jj, FNAMES[f], hashlib.sha256(blk.encode()).hexdigest(), nnz, S1, S2, S0,
                            get(0, 0, 0), get(1, 0, 0), get(0, 1, 0), get(0, 0, 1)))
    open(out + '.txt', 'w').write(''.join(text))
    with open(out + '.digests', 'w') as fo:
        fo.write('case sha256 %s\n' % case_hash.hexdigest())
        for s, h in handoffs: fo.write('handoff %d sha256 %s\n' % (s, h))
        for d_ in digests: fo.write(d_ + '\n')
        for k_, v_ in spot.items(): fo.write('spot %s %d\n' % (k_, v_))
        fo.write('spot Gamma^m_000 first element %d\n' % first_value)

if __name__ == '__main__':
    main()
