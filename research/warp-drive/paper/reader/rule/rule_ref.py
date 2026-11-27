#!/usr/bin/env python3
"""rule_ref.py -- an exact-integer reference implementation of the rule of S-RULE §3, for small runs.

Written from S-RULE §3 as directly as possible, with Python's unbounded integers and no floating point anywhere.  A
number x of the model is the Python int X = 2^320 x.  Every choice the text leaves open is marked "[Qn]" with the
number of the question in rule/README.md (and in the report I-RULE.md); the C++ production code makes the same choices.

usage:  rule_ref.py CONFIG OUTPREFIX      (writes OUTPREFIX.dump: spot values and the cells' G, and, when the
                                           config's run covers every cell, OUTPREFIX.txt and OUTPREFIX.digests)

The right-hand side is the solver's generated straight-line program, read from solver/rhs_gen.h and evaluated with
every product floored (S-RULE §3.6): the C++ expression text is valid Python, and every product a*b is rewritten as
(a*b) >> 320, which keeps the C++ order of evaluation (left to right) because Python parses a*b*c as (a*b)*c.
"""
import sys, os, re, ast, math, hashlib
from fractions import Fraction as Fr

B = 320
ONE = 1 << B
HALF = 1 << (B - 1)
HERE = os.path.dirname(os.path.abspath(__file__))
RHS_PATH = os.environ.get('RULE_RHS', os.path.join(HERE, '..', 'solver', 'rhs_gen.h'))

# ------------------------------------------------------------------------------------------- §3.1 the arithmetic
def fl(q):                      # ⌊q⌋_B of a rational q: the integer floor(2^B q)
    q = Fr(q); return (q.numerator << B) // q.denominator
def mul(x, y): return (x * y) >> B              # x ⊙ y  (>> is the floor for negative values too)
def div(x, y):                                  # x ⊘ y
    if y == 0: raise ZeroDivisionError
    return (x << B) // y                        # // is the floor
def divi(x, n): return x // n                   # x ⊘ n
def fsqrt(x): assert x >= 0; return math.isqrt(x << B)
def dot(a, b): return sum(p * q for p, q in zip(a, b)) >> B   # exact sum of exact products, one floor
def power(x, n):                                # x^n as the left-to-right product chain  [Q1]
    r = x
    for _ in range(n - 1): r = mul(r, x)
    return r

# ------------------------------------------------------------------------------------------- §3.2 functions, constants
def machin_A(n, J):
    s = 0
    for j in range(J + 1):
        t = ONE // ((2 * j + 1) * n ** (2 * j + 1))         # ⌊1/((2j+1) n^(2j+1))⌋_B, then the sign
        s += -t if j % 2 else t
    return s
PI = 16 * machin_A(5, 70) - 4 * machin_A(239, 20)
L2 = 2 * sum(ONE // ((2 * j + 1) * 3 ** (2 * j + 1)) for j in range(101))

def kz(y):                      # the least k >= 0 with |y| <= 2^(k-3), and z = y ⊘ 2^k
    k = 0
    while abs(y) > (1 << (B + k - 3)): k += 1
    return k, y >> k

def expF(y):
    k, z = kz(y)
    E = ONE
    for n in range(45, 0, -1): E = ONE + divi(mul(z, E), n)
    for _ in range(k): E = mul(E, E)
    return E

LOGC = [ONE // (2 * j + 1) for j in range(71)]            # ⌊1/(2j+1)⌋_B
def logF(y):
    assert y > 0
    m = y.bit_length() - 1 - B                             # 2^m <= y < 2^(m+1), i.e. 1 <= w := 2^-m y < 2
    if y >= 3 << (B + m - 1): m += 1                       # w >= 3/2: w := w/2, m := m + 1
    assert B + m >= 1
    p2 = 1 << (B + m)                                      # 2^m as a number
    t = div(y - p2, y + p2)                                # t := (w - 1) ⊘ (w + 1) with w exact  [Q3]
    t2 = mul(t, t)
    P = LOGC[70]
    for j in range(69, -1, -1): P = LOGC[j] + mul(t2, P)   # Horner in t ⊙ t  [Q5]
    return m * L2 + 2 * mul(t, P)

SINC = [fl(Fr((-1) ** ((n - 1) // 2), math.factorial(n))) if n % 2 else 0 for n in range(46)]
COSC = [fl(Fr((-1) ** (n // 2), math.factorial(n))) if n % 2 == 0 else 0 for n in range(45)]
def sincosF(y):                 # (sin y, cos y)
    k, z = kz(y)
    S = SINC[45]
    for n in range(44, -1, -1): S = SINC[n] + mul(z, S)    # Horner in z over every coefficient  [Q4]
    C = COSC[44]
    for n in range(43, -1, -1): C = COSC[n] + mul(z, C)
    for _ in range(k): S, C = mul(2 * S, C), mul(C, C) - mul(S, S)   # (2S) ⊙ C  [Q2]
    return S, C
def chat(r): return sincosF(mul(PI, fl(r)))[1]             # ĉ(r) = cos(π̂ ⊙ ⌊r⌋_B)  [Q6]
def sinhcosh(y):
    e1, e2 = expF(y), expF(-y)
    return divi(e1 - e2, 2), divi(e1 + e2, 2)

XI0 = -logF(4500 * ONE + fsqrt(20250001 * ONE))          # ξ̂₀ = −log(4500 + √(4500² + 1))
AH = fl(Fr(1, 500))                                      # â

# ------------------------------------------------------------------------------------------- §3.3 nodes, matrices
def lobatto(p): return [-chat(Fr(j, p)) for j in range(p + 1)]
def radau(p): return sorted(chat(Fr(2 * j, 2 * p + 1)) for j in range(p + 1))
def xnodes(M): return [chat(Fr(k, M)) for k in range(M + 1)]

def pmul_lin(c, r):             # (sum c_m T^m) (T - r)
    out = [0] * (len(c) + 1)
    for m, cm in enumerate(c): out[m + 1] += cm; out[m] -= r * cm
    return out
def lagrange_int(T):            # integer polynomials Ñ_j(T) = Π_{k≠j} (T − T_k) and d̃_j = Π_{k≠j} (T_j − T_k)
    out = []
    for j in range(len(T)):
        c = [1]; d = 1
        for k in range(len(T)):
            if k != j: c = pmul_lin(c, T[k]); d *= T[j] - T[k]
        out.append((c, d))
    return out
def horner(c, t):
    s = 0
    for cm in reversed(c): s = s * t + cm
    return s

def Dmat(T):                    # D_ij = ℓ'_j(τ_i) = 2^B Ñ_j'(T_i) / d̃_j   (T: the nodes as integers X)
    LP = lagrange_int(T); out = []
    for i in range(len(T)):
        row = []
        for (c, d) in LP:
            dc = [m * c[m] for m in range(1, len(c))]
            row.append(fl(Fr(horner(dc, T[i]) * ONE, d)))
        out.append(row)
    return out
def Qmat(T):                    # Q_ij = ∫_{-1}^{τ_i} ℓ_j, in the node variable τ = T / 2^B
    nodes = [Fr(t, ONE) for t in T]; out = []
    polys = []
    for j in range(len(T)):
        c = [Fr(1)]; d = Fr(1)
        for k in range(len(T)):
            if k != j: c = pmul_lin(c, nodes[k]); d *= nodes[j] - nodes[k]
        polys.append([cm / d for cm in c])
    for i in range(len(T)):
        row = []
        for c in polys:
            I = [Fr(0)] + [cm / (m + 1) for m, cm in enumerate(c)]
            row.append(fl(horner(I, nodes[i]) - horner(I, Fr(-1))))
        out.append(row)
    return out
def W4V4(T):                    # on σ = (τ + 1)/2 exactly  [Q9]
    sig = [(Fr(t, ONE) + 1) / 2 for t in T]; W4 = []; V4 = []
    polys = []
    for j in range(len(T)):
        c = [Fr(1)]; d = Fr(1)
        for k in range(len(T)):
            if k != j: c = pmul_lin(c, sig[k]); d *= sig[j] - sig[k]
        polys.append([cm / d for cm in c])
    for i in range(len(T)):
        rw, rv = [], []
        si = sig[i]
        for c in polys:
            c3 = [Fr(0)] * 3 + c; c2 = [Fr(0)] * 2 + c              # s^3 ℓ_j, s^2 ℓ_j
            I3 = [Fr(0)] + [a / (m + 1) for m, a in enumerate(c3)]
            I2 = [Fr(0)] + [a / (m + 1) for m, a in enumerate(c2)]
            rw.append(fl(horner(I3, si) / si ** 4))
            rv.append(fl((si * horner(I2, si) - horner(I3, si)) / si ** 4))
        W4.append(rw); V4.append(rv)
    return W4, V4
def dotsq(A):                   # the dot-product square: entries <A_i·, A_·j>
    n = len(A); cols = [[A[l][j] for l in range(n)] for j in range(n)]
    return [[dot(A[i], cols[j]) for j in range(n)] for i in range(n)]
def dct(N):                     # C_nm = ⌊(2/N) ε_n ε_m ĉ((nm mod 2N)/N)⌋_B
    eps = lambda q: Fr(1, 2) if q in (0, N) else Fr(1)
    ch = {}
    out = []
    for n in range(N + 1):
        row = []
        for m in range(N + 1):
            r = (n * m) % (2 * N)
            if r not in ch: ch[r] = chat(Fr(r, N))
            row.append(fl(Fr(2, N) * eps(n) * eps(m) * Fr(ch[r], ONE)))
        out.append(row)
    return out
def lagr_values(nodes, t):      # ⌊ℓ_j(t)⌋_B on the given node coordinates, exactly  [Q10]
    out = []
    for j in range(len(nodes)):
        num, den = 1, 1
        for k in range(len(nodes)):
            if k != j: num *= t - nodes[k]; den *= nodes[j] - nodes[k]
        out.append((num * ONE) // den if den > 0 else (-num * ONE) // (-den))
    return out

# ------------------------------------------------------------------------------------------- §3.4 the seed
def seed(xi, v):
    sh, ch = sinhcosh(xi)
    up1 = mul(AH, sh); u = up1 - ONE; dudxi = mul(AH, ch)
    H = v - 2 * u + logF(div(up1, u - ONE))
    r0 = ONE + (1 << (B - 32)); r1 = divi(max(H, 0), 2) + 3 * ONE
    for _ in range(80):
        mid = divi(r0 + r1, 2)
        if 2 * mid + logF(div(mid - ONE, mid + ONE)) < H: r0 = mid
        else: r1 = mid
    R = r0
    for _ in range(6):
        R = R - div(2 * R + logF(div(R - ONE, R + ONE)) - H, 2 * ONE + div(2 * ONE, mul(R, R) - ONE))
    f = ONE - div(ONE, mul(R, R)); g = ONE - div(ONE, mul(u, u))
    return dict(R=R, Rv=divi(f, 2), Ru=-div(f, g), OM2=div(f, 2 * g), Wv=div(ONE, mul(mul(2 * R, R), R)),
                dudxi=dudxi)                                            # R_u := −(f ⊘ g)  [Q24]

# ------------------------------------------------------------------------------------------- the right-hand side
def load_rhs(path):
    txt = open(path).read()
    jets = re.findall(r'"([^"]+)"', re.search(r'RHS_JET\[\] = \{(.*?)\};', txt).group(1))
    knum = [int(a) for a in re.search(r'RHS_KNUM\[\] = \{(.*?)\};', txt).group(1).split(',')]
    kden = [int(a) for a in re.search(r'RHS_KDEN\[\] = \{(.*?)\};', txt).group(1).split(',')]
    body = re.findall(r'^\s*const auto (\w+) = (.*);\s*$', txt, re.M)

    class FloorProducts(ast.NodeTransformer):
        def visit_BinOp(self, node):
            self.generic_visit(node)
            if isinstance(node.op, ast.Mult):
                return ast.BinOp(left=node, op=ast.RShift(), right=ast.Constant(B))
            return node
    lines = ['def rhs(J, K, x):', '    ' + ', '.join(jets) + ' = J']
    for name, expr in body:
        tree = FloorProducts().visit(ast.parse(expr, mode='eval'))
        lines.append('    %s = %s' % (name, ast.unparse(ast.fix_missing_locations(tree))))
    lines.append('    return (Xm, Xn, XR, XW, Svv)')
    ns = {}
    exec('\n'.join(lines), ns)
    K = [fl(Fr(a, b)) for a, b in zip(knum, kden)]                     # constants enter as ⌊q⌋_B
    return jets, K, ns['rhs']
JETS, KC, RHS = load_rhs(RHS_PATH)
assert JETS == ['R', 'iR', 'ES', 'iES', 'OM2', 'iOM2', 'R_u', 'R_v', 'R_x', 'R_xx', 'R_vx', 'W_v', 'W_x', 'W_xx',
                'W_vx', 'm', 'm_u', 'm_v', 'm_x', 'm_xx', 'm_vx', 'n', 'n_u', 'n_v', 'n_x', 'n_xx', 'n_vx', 's', 's_v',
                's_x', 's_vx']

# ------------------------------------------------------------------------------------------- configuration
def parse_rat(s):
    return Fr(s)
class Case:
    def __init__(self, fn):
        self.elems = []; self.run_cols = None; self.run_rows = None; self.NRay = 40; self.dump = []
        for line in open(fn):
            t = line.split('#')[0].split()
            if not t: continue
            k = t[0]
            if k == 'seed': self.seed = int(t[1])
            elif k == 'xi_e': self.xi_e = fl(parse_rat(t[1]))
            elif k == 'v_e': self.v_e = fl(parse_rat(t[1]))
            elif k == 'ncol': self.nc = int(t[1])
            elif k == 'nrow': self.nr = int(t[1])
            elif k == 'pxi': self.pxi = int(t[1])
            elif k == 'pv': self.pv = int(t[1])
            elif k == 'M': self.M = int(t[1])
            elif k == 'NP': self.NP = int(t[1])
            elif k == 'NRay': self.NRay = int(t[1])
            elif k == 'p': self.p = int(t[1])
            elif k == 'run_cols': self.run_cols = int(t[1])
            elif k == 'run_rows': self.run_rows = int(t[1])
            elif k == 'elem': self.elems.append((int(t[1]), int(t[2])) + tuple(fl(parse_rat(a)) for a in t[3:7]) + (int(t[7]), int(t[8])))
            elif k in ('segment', 'Me', 'threads', 'batch', 'ckpt_minutes', 'out', 'svphi'): pass   # C++ only
            else: raise ValueError('unknown key ' + k)
        if self.run_cols is None: self.run_cols = self.nc
        if self.run_rows is None: self.run_rows = self.nr

# ------------------------------------------------------------------------------------------- the run
def main():
    cs = Case(sys.argv[1]); out = sys.argv[2]
    lam = ONE if cs.seed == 1 else fsqrt(fl(Fr(1, 10)))
    NF = 5; FR_, FM_, FN_, FW_, FS_ = range(5)
    # grids (§3.6): breakpoints, node sets
    XB = [XI0 + divi((cs.xi_e - XI0) * i, cs.nc) for i in range(cs.nc + 1)]
    VB = [HALF + divi((cs.v_e - HALF) * j, cs.nr) for j in range(cs.nr + 1)]
    TL = lobatto(cs.pxi); TV = lobatto(cs.pv); TR = radau(cs.pv); X = xnodes(cs.M)
    nA, nB, NX = cs.pxi + 1, cs.pv + 1, cs.M + 1
    Dxi, Qxi = Dmat(TL), Qmat(TL)
    DvL, QvL = Dmat(TV), Qmat(TV); QQ = dotsq(QvL)
    DvR, QvR = Dmat(TR), Qmat(TR); W4, V4 = W4V4(TR)
    D1x = Dmat(X); D2x = dotsq(D1x)
    spot = {'pi': PI, 'log2': L2, 'xi0': XI0, 'lambda': lam, 'Rs(xi0,1/2)': seed(XI0, HALF)['R']}

    def vnodes(j):
        hv = divi(VB[j + 1] - VB[j], 2)
        return hv, [VB[j] + mul(hv, t + ONE) for t in (TR if j == 0 else TV)]

    # §3.5 the data on N1
    def mn_data(v, x, r):
        eps = v - HALF
        z = divi(mul(PI, eps), 3)
        sz, cz = sincosF(z)
        sc = mul(divi(PI, 3), div(sz, z))
        h = fsqrt(div(2 * ONE, ONE + mul(x, x)))
        st, ct = sincosF(div(v, lam))
        r32 = div(ONE, mul(r, fsqrt(r)))
        pre = mul(mul(mul(h, lam), HALF), r32)                 # h ⊙ λ̂ ⊙ ½ ⊙ (1 ⊘ (r ⊙ √r))  (amp = 1)
        sc2 = mul(sc, sc); sc3 = mul(sc2, sc); sc4 = mul(sc2, sc2)   # as mn_data  [Q1]
        f = ONE - div(ONE, mul(r, r))
        gm = mul(mul(pre, sc4), ct); gn = mul(mul(pre, sc4), st)
        a1 = mul(mul(div(mul(-3 * (ONE >> 2), f), r), eps), sc4)
        a2 = mul(mul(divi(4 * PI, 3), sc3), cz)
        a3 = div(mul(eps, sc4), lam)
        mv3 = mul(pre, mul(a1 + a2, ct) - mul(a3, st))
        nv3 = mul(pre, mul(a1 + a2, st) + mul(a3, ct))
        return gm, gn, mv3, nv3

    def n1_row(j, bot):
        hv, vs = vnodes(j); first = j == 0
        Dv = DvR if first else DvL; Qv = QvR if first else QvL
        E = [v - HALF for v in vs]; E4 = [power(e, 4) for e in E]
        sd = [seed(XI0, v) for v in vs]
        eb = VB[j] - HALF; eb4 = power(eb, 4)
        Gm = [[0] * NX for _ in range(nB)]; Gn = [[0] * NX for _ in range(nB)]
        sh6 = [[0] * NX for _ in range(nB)]; GR = [[0] * NX for _ in range(nB)]
        for b in range(nB):
            for k in range(NX):
                x = X[k]
                gm, gn, mv3, nv3 = mn_data(vs[b], x, sd[b]['R'])
                Gm[b][k] = gm; Gn[b][k] = gn
                Pv = divi(mul(2 * (ONE + x), mv3) - mul(ONE - x, nv3), 3)
                Qv_ = divi(mul(2 * (ONE - x), nv3) - mul(ONE + x, mv3), 3)
                sh6[b][k] = mul(Pv, Pv) + mul(Qv_, Qv_) + mul(Pv + Qv_, Pv + Qv_)
                if not first: GR[b][k] = div(mul(eb4, bot[0][k]) + mul(vs[b] - VB[j], bot[1][k]), E4[b])
        rhs = None
        for it in range(cs.NRay):
            rhs = [[0] * NX for _ in range(nB)]
            for b in range(nB):
                for k in range(NX):
                    gv = div(dot(Dv[b], [GR[bb][k] for bb in range(nB)]), hv)
                    DRv = mul(mul(mul(4 * E[b], E[b]), E[b]), GR[b][k]) + mul(E4[b], gv)
                    Rt = sd[b]['R'] + mul(E4[b], GR[b][k])
                    rhs[b][k] = mul(2 * sd[b]['Wv'], DRv) - divi(mul(mul(mul(mul(Rt, sh6[b][k]), E4[b]), E[b]), E[b]), 3)
            new = [[0] * NX for _ in range(nB)]
            for b in range(nB):
                for k in range(NX):
                    if first:
                        new[b][k] = dot(V4[b], [div(rhs[bb][k], mul(E[bb], E[bb])) for bb in range(nB)])
                    else:
                        s1 = dot(QQ[b], [rhs[bb][k] for bb in range(nB)])
                        new[b][k] = div(mul(eb4, bot[0][k]) + mul(vs[b] - VB[j], bot[1][k]) + mul(mul(hv, hv), s1), E4[b])
            GR = new
        topGR = [GR[nB - 1][k] for k in range(NX)]
        topRv = [(0 if first else bot[1][k]) + mul(hv, dot(Qv[nB - 1], [rhs[bb][k] for bb in range(nB)])) for k in range(NX)]
        return {FR_: GR, FM_: Gm, FN_: Gn, FW_: [[0] * NX for _ in range(nB)]}, (topGR, topRv)

    # §3.6-3.7 one cell
    def solve_cell(i, j, left, bottom):
        first = j == 0
        hxi = divi(XB[i + 1] - XB[i], 2); xis = [XB[i] + mul(hxi, t + ONE) for t in TL]
        hv, vs = vnodes(j)
        Dv = DvR if first else DvL; Qv = QvR if first else QvL
        eps = [v - HALF for v in vs]; e2 = [mul(e, e) for e in eps]; e3 = [mul(a, e) for a, e in zip(e2, eps)]
        e4 = [mul(a, e) for a, e in zip(e3, eps)]
        ihxi, ihv = div(ONE, hxi), div(ONE, hv)
        sd = [[seed(xis[a], vs[b]) for b in range(nB)] for a in range(nA)]
        # boundary terms
        Bt = [[[[0] * NX for _ in range(nB)] for _ in range(nA)] for _ in range(NF)]
        elo = VB[j] - HALF; elo4 = power(elo, 4)
        for f in range(NF):
            for a in range(nA):
                for b in range(nB):
                    for k in range(NX):
                        if first: val = left[f][b][k] if f < 4 else 0
                        elif f < 4:
                            val = div(mul(elo4, bottom['G'][f][a][k]) + mul(e4[b], left[f][b][k]) - mul(elo4, bottom['G'][f][0][k]), e4[b])
                        else:
                            val = div(mul(elo4, bottom['G'][f][a][k]) + mul(vs[b] - VB[j], bottom['sv'][a][k]), e4[b])
                        Bt[f][a][b][k] = val
        # the right-hand side at the seed (D = 0)
        def jets_full(a, b, k, Dj):
            s = sd[a][b]; x = X[k]
            R = s['R'] + Dj['D'][FR_]
            S = divi(mul(ONE + x, Dj['D'][FM_]) + mul(ONE - x, Dj['D'][FN_]), 3)
            OM2s = s['OM2']
            J = [R, div(ONE, R), expF(S), expF(-S), mul(OM2s, expF(2 * Dj['D'][FW_])),
                 mul(div(ONE, OM2s), expF(-2 * Dj['D'][FW_])),
                 s['Ru'] + Dj['Du'][FR_], s['Rv'] + Dj['Dv'][FR_], Dj['Dx'][FR_], Dj['Dxx'][FR_], Dj['Dvx'][FR_],
                 s['Wv'] + Dj['Dv'][FW_], Dj['Dx'][FW_], Dj['Dxx'][FW_], Dj['Dvx'][FW_]]
            for f in (FM_, FN_):
                J += [Dj['D'][f], Dj['Du'][f], Dj['Dv'][f], Dj['Dx'][f], Dj['Dxx'][f], Dj['Dvx'][f]]
            J += [Dj['D'][FS_], Dj['Dv'][FS_], Dj['Dx'][FS_], Dj['Dvx'][FS_]]
            return RHS(J, KC, x)
        zero = {'D': [0] * 5, 'Du': [0] * 5, 'Dv': [0] * 5, 'Dx': [0] * 5, 'Dxx': [0] * 5, 'Dvx': [0] * 5}
        Xs = [[[jets_full(a, b, k, zero) for k in range(NX)] for b in range(nB)] for a in range(nA)]

        def evaluate(G):               # Ψ (fields R, m, n, W) and Φ at every node
            Psi = [[[[0] * NX for _ in range(nB)] for _ in range(nA)] for _ in range(4)]
            Phi = [[[0] * NX for _ in range(nB)] for _ in range(nA)]
            for a in range(nA):
                for b in range(nB):
                    Gv = [[mul(dot(Dv[b], [G[f][a][bb][k] for bb in range(nB)]), ihv) for k in range(NX)] for f in range(NF)]
                    Gxi = [[mul(dot(Dxi[a], [G[f][aa][b][k] for aa in range(nA)]), ihxi) for k in range(NX)] for f in range(3)]
                    idu = div(ONE, sd[a][b]['dudxi'])
                    for k in range(NX):
                        Dj = {'D': [0] * 5, 'Du': [0] * 5, 'Dv': [0] * 5, 'Dx': [0] * 5, 'Dxx': [0] * 5, 'Dvx': [0] * 5}
                        for f in range(NF):
                            g = G[f][a][b][k]
                            gx = dot(D1x[k], G[f][a][b])
                            gvx = dot(D1x[k], Gv[f])
                            Dj['D'][f] = mul(e4[b], g)
                            Dj['Dx'][f] = mul(e4[b], gx)
                            Dj['Dv'][f] = mul(4 * e3[b], g) + mul(e4[b], Gv[f][k])          # [Q2]
                            Dj['Dvx'][f] = mul(4 * e3[b], gx) + mul(e4[b], gvx)             # [Q11]
                            if f < 4: Dj['Dxx'][f] = mul(e4[b], dot(D2x[k], G[f][a][b]))
                            if f < 3: Dj['Du'][f] = mul(mul(e4[b], Gxi[f][k]), idu)
                        o = jets_full(a, b, k, Dj); os_ = Xs[a][b][k]; du = sd[a][b]['dudxi']
                        Psi[FR_][a][b][k] = mul(du, o[2] - os_[2]); Psi[FM_][a][b][k] = mul(du, o[0] - os_[0])
                        Psi[FN_][a][b][k] = mul(du, o[1] - os_[1]); Psi[FW_][a][b][k] = mul(du, o[3] - os_[3])
                        Phi[a][b][k] = o[4] - os_[4]
            return Psi, Phi

        def integrate(Psi, Phi):
            I = [[[[0] * NX for _ in range(nB)] for _ in range(nA)] for _ in range(NF)]
            if first:
                ie3 = [div(ONE, e) for e in e3]; ie2 = [div(ONE, e) for e in e2]
                for f in range(4):
                    T = [[[dot(W4[b], [mul(Psi[f][a][bb][k], ie3[bb]) for bb in range(nB)]) for k in range(NX)] for b in range(nB)] for a in range(nA)]
                    for a in range(nA):
                        for b in range(nB):
                            for k in range(NX):
                                I[f][a][b][k] = mul(hxi, dot(Qxi[a], [T[aa][b][k] for aa in range(nA)]))
                for a in range(nA):
                    for b in range(nB):
                        for k in range(NX):
                            I[FS_][a][b][k] = dot(V4[b], [mul(Phi[a][bb][k], ie2[bb]) for bb in range(nB)])
            else:
                hh = mul(hxi, hv); hv2 = mul(hv, hv)
                for f in range(4):
                    T = [[[dot(Qv[b], [Psi[f][a][bb][k] for bb in range(nB)]) for k in range(NX)] for b in range(nB)] for a in range(nA)]
                    for a in range(nA):
                        for b in range(nB):
                            for k in range(NX):
                                I[f][a][b][k] = div(mul(hh, dot(Qxi[a], [T[aa][b][k] for aa in range(nA)])), e4[b])
                for a in range(nA):
                    for b in range(nB):
                        for k in range(NX):
                            I[FS_][a][b][k] = div(mul(hv2, dot(QQ[b], [Phi[a][bb][k] for bb in range(nB)])), e4[b])
            return I

        G = [[[list(r) for r in pl] for pl in fld] for fld in Bt]          # G^0 = B
        for n in range(cs.NP):
            Psi, Phi = evaluate(G)
            I = integrate(Psi, Phi)
            Gn = [[[[Bt[f][a][b][k] + I[f][a][b][k] for k in range(NX)] for b in range(nB)] for a in range(nA)] for f in range(NF)]
            G = Gn
        Psi, Phi = evaluate(G)                                              # Φ of the final iterate  [Q15]
        sv = [[(0 if first else bottom['sv'][a][k]) + mul(hv, dot(Qv[nB - 1], [Phi[a][bb][k] for bb in range(nB)]))
               for k in range(NX)] for a in range(nA)]
        right = [[[G[f][nA - 1][b][k] for k in range(NX)] for b in range(nB)] for f in range(4)]
        top = {'G': [[[G[f][a][nB - 1][k] for k in range(NX)] for a in range(nA)] for f in range(NF)], 'sv': sv}
        return G, right, top, xis, vs

    # the march (columns outward, rows upward)
    n1 = []; bot = None
    for j in range(cs.run_rows):
        e, bot = n1_row(j, bot); n1.append(e)
    spot['Gm(N1, row 0, first node)'] = n1[0][FM_][0][0]
    cells = {}; tops = {}
    for i in range(cs.run_cols):
        for j in range(cs.run_rows):
            left = n1[j] if i == 0 else cells[(i - 1, j)][1]
            G, right, top, xis, vs = solve_cell(i, j, left, tops.get((i, j - 1)))
            cells[(i, j)] = (G, right, xis, vs); tops[(i, j)] = top
            print('cell', i, j, 'done', file=sys.stderr)
    G00 = cells[(0, 0)][0]
    for f in range(NF): spot['G00 last node field %d' % f] = G00[f][nA - 1][nB - 1][NX - 1]

    with open(out + '.dump', 'w') as fo:
        for k_, v_ in spot.items(): fo.write('spot %s %d\n' % (k_, v_))
        for (i, j) in sorted(cells):
            G = cells[(i, j)][0]
            txt = ''.join('%d %d %d %d %d\n' % (f, a, b, k, G[f][a][b][k]) for f in range(NF) for a in range(nA)
                          for b in range(nB) for k in range(NX))
            fo.write('cell %d %d sha256 %s\n' % (i, j, hashlib.sha256(txt.encode()).hexdigest()))
            fo.write(txt)
            sv = tops[(i, j)]['sv']
            fo.write('sv %d %d %s\n' % (i, j, hashlib.sha256(''.join('%d\n' % sv[a][k] for a in range(nA) for k in range(NX)).encode()).hexdigest()))

    if cs.run_cols < cs.nc or cs.run_rows < cs.nr or not cs.elems: return
    # §3.8 element values and coefficients
    FNAMES = ['R', 'm', 'n', 'W', 's']
    Cx = dct(cs.M)
    text = []; digests = []; blocksum = []
    case_hash = hashlib.sha256()
    first_value = None
    for (ii, jj, XL, XH, VL, VH, Nt, Ns) in cs.elems:
        xn = [divi(XL + XH, 2) - mul(divi(XH - XL, 2), chat(Fr(a, Nt))) for a in range(Nt + 1)]
        vn = [divi(VL + VH, 2) - mul(divi(VH - VL, 2), chat(Fr(b, Ns))) for b in range(Ns + 1)]
        def owner(t, br, n):                                               # [Q17]
            for c in range(n):
                if br[c + 1] >= t: return c
            return n - 1
        V = [[[[0] * NX for _ in range(Ns + 1)] for _ in range(Nt + 1)] for _ in range(NF)]
        for a in range(Nt + 1):
            ci = owner(xn[a], XB, cs.nc)
            for b in range(Ns + 1):
                cj = owner(vn[b], VB, cs.nr)
                G, _, xis, vs = cells[(ci, cj)]
                lx = lagr_values(xis, xn[a]); lv = lagr_values(vs, vn[b])
                for f in range(NF):
                    for k in range(NX):
                        inner = [dot(lv, [G[f][aa][bb][k] for bb in range(nB)]) for aa in range(nA)]
                        V[f][a][b][k] = dot(lx, inner)
        if first_value is None: first_value = [V[f][0][0][0] for f in range(NF)]
        Ct, Cs = dct(Nt), dct(Ns)
        for f in range(NF):
            c1 = [[[dot([Ct[n][Nt - a] for a in range(Nt + 1)], [V[f][a][b][k] for a in range(Nt + 1)]) for k in range(NX)]
                   for b in range(Ns + 1)] for n in range(Nt + 1)]                                     # [Q18]
            c2 = [[[dot([Cs[m][Ns - b] for b in range(Ns + 1)], [c1[n][b][k] for b in range(Ns + 1)]) for k in range(NX)]
                   for m in range(Ns + 1)] for n in range(Nt + 1)]
            z = [[[(10 ** cs.p * dot(Cx[l], c2[n][m]) + HALF) >> B for l in range(NX)] for m in range(Ns + 1)] for n in range(Nt + 1)]
            lines = ['block %d %d %s %d %d %d %d' % (ii, jj, FNAMES[f], cs.p, Nt, Ns, cs.M)]
            S1 = S2 = S0 = nnz = 0
            for a in range(Nt + 1):
                for b in range(Ns + 1):
                    row = z[a][b]; K = max((k for k in range(NX) if row[k] != 0), default=-1)
                    for k in range(NX):
                        if row[k]:
                            nnz += 1; S1 += row[k]; S2 += row[k] * (-1) ** (a + b + k)
                            if (a + b + k) % 2 == 0 and a % 2 == 0 and b % 2 == 0: S0 += row[k] * (-1) ** ((a + b + k) // 2)
                    if K >= 0: lines.append('%d %d %s' % (a, b, ' '.join(str(row[k]) for k in range(K + 1))))
            blk = ''.join(l + '\n' for l in lines)
            text.append(blk); case_hash.update(blk.encode())
            get = lambda a, b, k: z[a][b][k] if a <= Nt and b <= Ns and k < NX else 0
            digests.append('block %d %d %s sha256 %s S1 %d S2 %d S0 %d nonzero %d z000 %d z100 %d z010 %d z001 %d' %
                           (ii, jj, FNAMES[f], hashlib.sha256(blk.encode()).hexdigest(), S1, S2, S0, nnz,
                            get(0, 0, 0), get(1, 0, 0), get(0, 1, 0), get(0, 0, 1)))
    open(out + '.txt', 'w').write(''.join(text))
    with open(out + '.digests', 'w') as fo:
        fo.write('case sha256 %s\n' % case_hash.hexdigest())
        for d in digests: fo.write(d + '\n')
        for k_, v_ in spot.items(): fo.write('spot %s %d\n' % (k_, v_))
        for f in range(NF): fo.write('spot first element node value field %d %d\n' % (f, first_value[f]))

if __name__ == '__main__':
    main()
