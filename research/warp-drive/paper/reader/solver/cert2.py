"""P-APPC's certification of one element of a printed approximant (prop:appc-element-bound), in ball arithmetic
(python-flint), from the printed integers: N-APP1's cert.py restructured for the tables' sizes --
  * every block carries its own quantum 10^-p (exact rationals z 10^-p);
  * the node values are formed slab by slab in t (the contractions over sigma and x are done once and kept);
  * the interpolant's coefficients are the exact discrete transform (ball arithmetic), and the derivative bound for
    each |alpha| <= K is  sum |c_ijk| T_i^(a1)(1) T_j^(a2)(1) T_k^(a3)(1) + E_alpha  (|T_n^(l)| <= T_n^(l)(1) on
    [-1, 1], lem:tl5-rounding), with E_alpha of eq:appc-ealpha and M from the majorant (lem:appc-majorant).
usage: cert2.py case tables_z.pkl i j N1 N2 N3 rho1 rho2 rho3 prec K out.json"""
import sys, os, json, time, math, pickle, numpy as np
from fractions import Fraction as Fr
NAPP1 = os.environ.get('NAPP1', '/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/napp1')
sys.path.insert(0, NAPP1)
import flint
from flint import arb, arb_mat, fmpq
import cert, majorant, rep

FN = rep.FIELDS

def load(zfile):
    zs = pickle.load(open(zfile, 'rb'))
    return {k: np.vectorize(lambda q, p=p: Fr(int(q), 10 ** p), otypes=[object])(z) for k, (p, z) in zs.items()}

def fr_arb(q):
    return arb(fmpq(q.numerator, q.denominator)) if isinstance(q, Fr) else arb(int(q))

def contract_sx(C, V2, V3):
    """R[a][l2 * N3 + l3] = sum_{b,k} C[a,b,k] V2[l2][b] V3[l3][k]  as an arb_mat (n1 x N2 N3)"""
    n1, n2, n3 = C.shape; N2, N3 = len(V2), len(V3)
    A = arb_mat([[fr_arb(C[a, b, k]) for k in range(n3)] for a in range(n1) for b in range(n2)])
    B3 = arb_mat([[V3[l][k] for l in range(N3)] for k in range(n3)])
    M1 = (A * B3).entries()                                   # (n1 n2) x N3, row (a, b)
    B2 = arb_mat([[V2[l][b] for b in range(n2)] for l in range(N2)])
    rows = []
    for a in range(n1):
        Ma = arb_mat([[M1[(a * n2 + b) * N3 + l3] for l3 in range(N3)] for b in range(n2)])
        rows.append((B2 * Ma).entries())                      # N2 x N3, row-major
    return arb_mat(rows)

def T_deriv_at_1(n, l):
    return cert.Tl1(n, l)

def certify(case, zfile, i, j, N, rho, prec=192, K=4, nbox=24, chunk=8, verbose=True):
    flint.ctx.prec = prec
    t0 = time.time()
    Z = load(zfile)
    L = rep.layout(case)
    mx, hx = L['xi'][i]; mv, hv = L['v'][j]
    sub = cert.use_region(L, i, j)
    tc, th, sc, sh = (arb(fmpq(q.numerator, q.denominator)) for q in sub)
    mx_a, hx_a, mv_a, hv_a = (arb(fmpq(q.numerator, q.denominator)) for q in (mx, hx, mv, hv))
    a_ch = arb(fmpq(1, 500))
    G = {}
    for k in FN:
        c = Z['%d_%d_%s' % (i, j, k)]
        c = cert.reexpand(c, 0, Fr(sub[0]), Fr(sub[1])); c = cert.reexpand(c, 1, Fr(sub[2]), Fr(sub[3]))
        G[k] = cert.deriv_arrays_tau(c, Fr(sub[1]), Fr(sub[3]))
    n1, n2, n3 = G['R'][''].shape
    P1, P2, P3 = cert.lobatto(N[0]), cert.lobatto(N[1]), cert.lobatto(N[2])
    V1, V2, V3 = cert.vander(P1, n1), cert.vander(P2, n2), cert.vander(P3, n3)
    t1 = time.time()
    Rk = {k: {name: contract_sx(G[k][name], V2, V3) for name in cert.DER} for k in FN}
    t2 = time.time()
    P1t = [tc + th * q for q in P1]; P2s = [sc + sh * q for q in P2]
    N1, N2, N3 = N[0] + 1, N[1] + 1, N[2] + 1
    comps = ('ll', 'ln', 'nn', 'lx', 'nx', 'xx', '11', '22')
    # slab values -> (sigma, x) transforms, rows of S[comp] (N1 x N2 N3)
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
    D1, D2, D3 = dct_mat(N[0]), dct_mat(N[1]), dct_mat(N[2])
    D3t = D3.transpose()
    S = {ab: [] for ab in comps}
    one = arb(1)
    for l1a in range(0, N1, chunk):
        l1b = min(N1, l1a + chunk)
        B1c = arb_mat([[V1[l][a] for a in range(n1)] for l in range(l1a, l1b)])
        vals = {k: {name: (B1c * Rk[k][name]).entries() for name in cert.DER} for k in FN}
        for l1 in range(l1a, l1b):
            xi = mx_a + hx_a * P1t[l1]; u = -1 + a_ch * xi.sinh(); ch = xi.cosh()
            p1 = 1 / (ch * hx_a * a_ch); p2 = -(p1 * p1) * (xi.sinh() / ch) * hx_a
            g = {ab: [[None] * N3 for _ in range(N2)] for ab in comps}
            for l2 in range(N2):
                v = mv_a + hv_a * P2s[l2]
                seedJ = cert.seed_jets(u, v)
                for l3 in range(N3):
                    idx = (l1 - l1a) * N2 * N3 + l2 * N3 + l3
                    Gd = {k: {name: vals[k][name][idx] for name in cert.DER} for k in FN}
                    J = cert.node_jets(Gd, (p1, p2, 1 / hv_a), seedJ, v - one / 2, P3[l3], 1)
                    f = cert.residual_at(J, P3[l3], one)
                    for ab in comps: g[ab][l2][l3] = f[ab]
            for ab in comps:
                Sl = D2 * arb_mat(g[ab]) * D3t                       # (N2 x N3) coefficients in (sigma, x)
                S[ab].append(Sl.entries())
        if verbose: print('  slabs %d..%d of %d, %.0f s' % (l1a, l1b - 1, N1, time.time() - t0), flush=True)
    t3 = time.time()
    coef = {}
    for ab in comps:
        Cm = D1 * arb_mat(S[ab])                                     # N1 x (N2 N3)
        a = np.array([[float(abs(e).upper()) for e in row] for row in Cm.tolist()]) if hasattr(Cm, 'tolist') else None
        if a is None:
            ent = Cm.entries(); a = np.array([float(abs(e).upper()) for e in ent]).reshape(N1, N2 * N3)
        coef[ab] = a.reshape(N1, N2, N3)
    t4 = time.time()
    Zp = {k: v for k, v in Z.items()}
    M, minfo = majorant.majorant_M(Zp, 0, L, i, j, sub, rho)
    t5 = time.time()
    alphas = [(a1, a2, a3) for a1 in range(K + 1) for a2 in range(K + 1) for a3 in range(K + 1) if a1 + a2 + a3 <= K]
    S_all = [[cert.Ssum(rho[d], l, 0) for l in range(K + 1)] for d in range(3)]
    S_gt = [[cert.Ssum(rho[d], l, N[d] + 1) for l in range(K + 1)] for d in range(3)]
    W = [[np.array([float(T_deriv_at_1(n, l)) for n in range(N[d] + 1)]) for l in range(K + 1)] for d in range(3)]
    thf, shf = float(th.upper()), float(sh.upper())
    thl, shl = float(th.lower()), float(sh.lower())
    out = {}
    for ab in comps:
        out[ab] = {}
        for al in alphas:
            w = np.multiply.outer(np.multiply.outer(W[0][al[0]], W[1][al[1]]), W[2][al[2]])
            main = float((coef[ab] * w).sum()) * (1 + 1e-12)
            Ea = 16 * M * sum(S_gt[d][al[d]] * np.prod([S_all[e][al[e]] for e in range(3) if e != d]) for d in range(3))
            out[ab][''.join(map(str, al))] = (main + Ea) / (thl ** al[0] * shl ** al[1]) * (1 + 1e-12)
    res = dict(case=case, element=[i + 1, j + 1], sub=[str(q) for q in sub], N=list(N), rho=list(rho), prec=prec, K=K, M=M,
               ReRseed_min=minfo['ReRs_min'], maxQR=minfo['maxQR'],
               times=dict(setup=t1 - t0, contract=t2 - t1, nodes=t3 - t2, transform=t4 - t3, majorant=t5 - t4),
               nodes=N1 * N2 * N3, bounds=out)
    b0 = max(out[ab]['000'] for ab in comps)
    if verbose:
        bK = {l: max(max(v for kk, v in out[ab].items() if sum(map(int, kk)) == l) for ab in comps) for l in range(K + 1)}
        print('%s element (%d,%d): N = %s, rho = %s, M = %.3e; level 0: %.3e; by |alpha|: %s; times %s' %
              (case, i + 1, j + 1, N, rho, M, b0, {l: '%.2e' % b for l, b in bK.items()}, {k: round(v) for k, v in res['times'].items()}), flush=True)
    return res

if __name__ == '__main__':
    a = sys.argv[1:]
    case, zf = a[0], a[1]; i, j = int(a[2]) - 1, int(a[3]) - 1
    N = tuple(int(q) for q in a[4:7]); rho = tuple(float(q) for q in a[7:10]); prec = int(a[10]); K = int(a[11])
    r = certify(case, zf, i, j, N, rho, prec, K)
    json.dump(r, open(a[12], 'w'), indent=1)
