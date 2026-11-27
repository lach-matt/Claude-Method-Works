"""P-APPC's certification of one element (prop:appc-element-bound) from the printed integers, for tables of the real
sizes (blocks of ~10^6 integers of ~30 digits): N-APP1's procedure (cert.py, majorant.py), with every exact operation
on the printed integers done in FLINT integer matrices --
  * the affine re-expansion on the use box (lem:appc-reexpand) as integer matrix products with a rational scale;
  * the derivative coefficients (eq:tl5-cheb-derivative) exactly in integers;
  * the values at the Lobatto nodes by ball-arithmetic contractions, t first (slabs), then sigma and x;
  * the interpolant's coefficients by the exact discrete transform in balls; the derivative bounds for |alpha| <= K by
    sum |c_ijk| T_i^(a1)(1) T_j^(a2)(1) T_k^(a3)(1) + E_alpha (eq:appc-ealpha), M from the majorant (lem:appc-majorant)
    evaluated on the exact polynomial (v - 1/2)^4 G re-expanded on the box.
usage: cert3.py case tables_z.pkl i j N1 N2 N3 rho1 rho2 rho3 prec K out.json [layout]"""
import sys, os, json, time, math, pickle, numpy as np
from fractions import Fraction as Fr
NAPP1 = os.environ.get('NAPP1', '/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/napp1')
sys.path.insert(0, NAPP1)
import flint
from flint import arb, arb_mat, fmpq, fmpz_mat
import cert, rep, majorant
from regform import regular_components
FN = rep.FIELDS

def lcm_den(frs):
    d = 1
    for q in frs: d = d * q.denominator // math.gcd(d, q.denominator)
    return d

def reexp_int(Z, axis, c, h):
    """exact: Z' with sum Z_j T_j(c + h tau) = (1/D) sum Z'_k T_k(tau); returns (Z', D)"""
    Z = np.moveaxis(Z, axis, 0); n = Z.shape[0]; rest = Z.shape[1:]
    A = cert.affine_matrix(n, Fr(c), Fr(h))
    D = lcm_den([A[j][k] for j in range(n) for k in range(n) if A[j][k] != 0])
    At = fmpz_mat(n, n, [int(A[j][k] * D) for k in range(n) for j in range(n)])      # transpose: row k, col j
    m = int(np.prod(rest)) if rest else 1
    X = fmpz_mat(n, m, [int(q) for q in Z.reshape(n, m).ravel()])
    Y = At * X
    out = np.array([int(q) for q in Y.entries()], dtype=object).reshape((n,) + rest)
    return np.moveaxis(out, 0, axis), D

def mul_lin_int(Z, alpha, beta):
    """exact: (alpha + beta tau2) * sum Z T (axis 1), alpha, beta rationals; returns (Z', D) with D the common factor"""
    D = lcm_den([Fr(alpha), Fr(beta) / 2])
    a = int(Fr(alpha) * D); b2 = int(Fr(beta) / 2 * D)
    Z = np.moveaxis(Z, 1, 0); n = Z.shape[0]
    out = np.zeros((n + 1,) + Z.shape[1:], dtype=object)
    for k in range(n):
        out[k] = out[k] + a * Z[k]
        out[k + 1] = out[k + 1] + b2 * Z[k]
        out[abs(k - 1)] = out[abs(k - 1)] + b2 * Z[k]
    return np.moveaxis(out, 0, 1), D

def deriv_int(Z, a):
    for ax in range(3):
        for _ in range(a[ax]): Z = cert.deriv_coeffs_int(Z, ax)
    return Z

def prepare(zs, case, i, j, sub):
    """G^F on the use box: integer arrays and rational scales for the 10 derivative names (in tau), and
    Q^F = (v - 1/2)^4 G^F likewise (for the majorant)"""
    L = rep.layout(case)
    mx, hx = L['xi'][i]; mv, hv = L['v'][j]
    tc, th, sc, sh = (Fr(q) for q in sub)
    alpha = Fr(mv) + Fr(hv) * sc - Fr(1, 2); beta = Fr(hv) * sh
    G, Q = {}, {}
    for F in FN:
        p, z = zs['%d_%d_%s' % (i, j, F)]
        Z, D1 = reexp_int(z, 0, tc, th); Z, D2 = reexp_int(Z, 1, sc, sh)
        scale = Fr(1, 10 ** p * D1 * D2)
        G[F] = {name: (deriv_int(Z, a), scale / (th ** a[0] * sh ** a[1])) for name, a in cert.DER.items()}
        Zq, sq = Z, scale
        for _ in range(4):
            Zq, Dq = mul_lin_int(Zq, alpha, beta); sq = sq / Dq
        Q[F] = (Zq, sq)
    return G, Q

def majorant_from(Q, case, i, j, sub, rho, nbox=24, nH=0.08):
    """majorant.majorant_M with the polynomial parts given exactly (integer arrays and scales)"""
    flint.ctx.prec = 128
    L = rep.layout(case)
    mx, hx = L['xi'][i]; mv, hv = L['v'][j]
    tc, th, sc, sh = (Fr(q) for q in sub)
    def csum(Z, s):
        num, den = s.numerator, s.denominator      # exact integer division to float (integers may exceed 1e308)
        a = np.abs(np.array([int(q) * num / den for q in Z.ravel()]).reshape(Z.shape))
        w = np.multiply.outer(np.multiply.outer(rho[0] ** np.arange(a.shape[0]), rho[1] ** np.arange(a.shape[1])), rho[2] ** np.arange(a.shape[2]))
        return float((a * w).sum()) * (1 + 1e-10)
    BQ = {F: {name: csum(deriv_int(Q[F][0], a), Q[F][1]) for name, a in cert.DER.items()} for F in FN}
    box = (arb(fmpq(mx.numerator, mx.denominator)), arb(fmpq(hx.numerator, hx.denominator)), arb(fmpq(mv.numerator, mv.denominator)), arb(fmpq(hv.numerator, hv.denominator)))
    a_ch = arb(fmpq(1, 500))
    Tb = cert.filled_boxes(rho[0], nbox)
    p1m = p2m = 0.0; umax = 0.0; umin = 1e300
    thA, tcA = arb(fmpq(th.numerator, th.denominator)), arb(fmpq(tc.numerator, tc.denominator))
    for tb in Tb:
        xi = box[0] + box[1] * (tcA + thA * tb); ch = xi.cosh()
        if not ch.real > 0: raise RuntimeError('cosh')
        p1 = 1 / (ch * box[1] * a_ch); p2 = -(p1 * p1) * (xi.sinh() / ch) * box[1]
        p1m = max(p1m, float(abs(p1).upper())); p2m = max(p2m, float(abs(p2).upper()))
        u = -1 + a_ch * xi.sinh(); umax = max(umax, float(abs(u).upper())); umin = min(umin, float(abs(u).lower()))
    rmin, nHb, Hrect = cert.analytic_checks((box[0] + box[1] * tcA, box[1] * thA, box[2] + box[3] * arb(fmpq(sc.numerator, sc.denominator)),
                                            box[3] * arb(fmpq(sh.numerator, sh.denominator))), rho, n=nbox, nH=nH)
    lo_r, hi_r, lo_i, hi_i = Hrect
    Hmod = max(abs(complex(lo_r, lo_i)), abs(complex(lo_r, hi_i)), abs(complex(hi_r, lo_i)), abs(complex(hi_r, hi_i)))
    Rmax = Hmod / 2 + 1.175
    QR = BQ['R']['']
    if not rmin - QR > 0: raise RuntimeError('Re R not bounded below: %g - %g' % (rmin, QR))
    Rlo = rmin - QR; Rup = Rmax + QR
    Maj = majorant.Maj
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
    it = 1 / float(th); iv = 1 / (float(hv) * float(sh))
    P1, P2 = p1m * it, p2m * it
    J = {}
    for F in FN:
        b = BQ[F]
        q = {'': Maj(b['']), 'u': Maj(P1 * b['t']), 'v': Maj(iv * b['s']), 'x': Maj(b['x']),
             'uu': Maj(P1 * P1 * b['tt'] + P2 * b['t']), 'uv': Maj(P1 * iv * b['ts']), 'vv': Maj(iv * iv * b['ss']),
             'ux': Maj(P1 * b['tx']), 'vx': Maj(iv * b['sx']), 'xx': Maj(b['xx'])}
        if F == 'R':
            for d in seedR: q[d] = q[d] + seedR[d] if d else Maj(Rup, Rlo)
        if F == 'W':
            for d in seedW: q[d] = q[d] + seedW[d]
        J[F] = q
    xm = 0.5 * (rho[2] + 1 / rho[2])
    Sb = ((1 + xm) * BQ['m'][''] + (1 + xm) * BQ['n']['']) / 3
    ES = Maj(math.exp(Sb), math.exp(-Sb))
    O2 = O2s * Maj(math.exp(2 * BQ['W']['']), math.exp(-2 * BQ['W']['']))
    fm = regular_components(Maj(xm), J, ES, O2, one=Maj(1.0, 1.0))
    M = max(fm[ab].up for ab in fm) * Rup ** 4 / math.sqrt(72) * (1 + 1e-12)
    return M, dict(ReRs_min=rmin, maxQR=QR, H_balls=nHb, Rmax=Rup)

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

def certify(case, zfile, i, j, N, rho, prec=192, K=4, chunk=6, verbose=True):
    flint.ctx.prec = prec
    t0 = time.time()
    zs = pickle.load(open(zfile, 'rb'))
    L = rep.layout(case)
    mx, hx = L['xi'][i]; mv, hv = L['v'][j]
    sub = cert.use_region(L, i, j)
    tc, th, sc, sh = (arb(fmpq(q.numerator, q.denominator)) for q in sub)
    mx_a, hx_a, mv_a, hv_a = (arb(fmpq(q.numerator, q.denominator)) for q in (mx, hx, mv, hv))
    a_ch = arb(fmpq(1, 500))
    G, Q = prepare(zs, case, i, j, sub)
    t1 = time.time()
    if verbose: print('  prepared (exact re-expansion, derivatives) in %.0f s' % (t1 - t0), flush=True)
    M, minfo = majorant_from(Q, case, i, j, sub, rho)
    flint.ctx.prec = prec
    t2 = time.time()
    if verbose: print('  majorant M = %.3e (Re R_seed >= %.3f) in %.0f s' % (M, minfo['ReRs_min'], t2 - t1), flush=True)
    shp = {F: G[F][''][0].shape for F in FN}
    n1, n2, n3 = (max(shp[F][d] for F in FN) for d in range(3))
    N1, N2, N3 = N[0] + 1, N[1] + 1, N[2] + 1
    P1, P2, P3 = cert.lobatto(N[0]), cert.lobatto(N[1]), cert.lobatto(N[2])
    V1, V2, V3 = cert.vander(P1, n1), cert.vander(P2, n2), cert.vander(P3, n3)
    B2f = {F: arb_mat([[V2[l][b] for b in range(shp[F][1])] for l in range(N2)]) for F in FN}
    B3tf = {F: arb_mat([[V3[l][k] for l in range(N3)] for k in range(shp[F][2])]) for F in FN}
    P1t = [tc + th * q for q in P1]; P2s = [sc + sh * q for q in P2]
    comps = ('ll', 'ln', 'nn', 'lx', 'nx', 'xx', '11', '22')
    D1, D2, D3 = dct_mat(N[0]), dct_mat(N[1]), dct_mat(N[2]); D3t = D3.transpose()
    S = {ab: [] for ab in comps}
    one = arb(1)
    # the integer arrays as fmpz matrices (n1 x n2 n3), scales as balls
    ZM = {F: {name: (fmpz_mat(shp[F][0], shp[F][1] * shp[F][2], [int(q) for q in Z.ravel()]), arb(fmpq(s.numerator, s.denominator))) for name, (Z, s) in G[F].items()} for F in FN}
    del G, Q                                                    # the Python integer copies (memory)
    for l1a in range(0, N1, chunk):
        l1b = min(N1, l1a + chunk)
        vals = {}
        for F in FN:
            vals[F] = {}
            m1, m2, m3 = shp[F]
            B1c = arb_mat([[V1[l][a] for a in range(m1)] for l in range(l1a, l1b)])
            for name, (Zm, s) in ZM[F].items():
                T1 = (B1c * arb_mat(Zm)).entries()                  # (c) x (m2 m3), row-major
                per = []
                for q in range(l1b - l1a):
                    Sl = arb_mat([[T1[q * m2 * m3 + b * m3 + k] for k in range(m3)] for b in range(m2)])
                    per.append((B2f[F] * Sl * B3tf[F] * s).entries())     # N2 x N3 values
                vals[F][name] = per
        for l1 in range(l1a, l1b):
            q = l1 - l1a
            xi = mx_a + hx_a * P1t[l1]; u = -1 + a_ch * xi.sinh(); ch = xi.cosh()
            p1 = 1 / (ch * hx_a * a_ch); p2 = -(p1 * p1) * (xi.sinh() / ch) * hx_a
            g = {ab: [[None] * N3 for _ in range(N2)] for ab in comps}
            for l2 in range(N2):
                v = mv_a + hv_a * P2s[l2]
                seedJ = cert.seed_jets(u, v)
                for l3 in range(N3):
                    idx = l2 * N3 + l3
                    Gd = {F: {name: vals[F][name][q][idx] for name in cert.DER} for F in FN}
                    J = cert.node_jets(Gd, (p1, p2, 1 / hv_a), seedJ, v - one / 2, P3[l3], 1)
                    f = cert.residual_at(J, P3[l3], one)
                    for ab in comps: g[ab][l2][l3] = f[ab]
            for ab in comps: S[ab].append((D2 * arb_mat(g[ab]) * D3t).entries())
        if verbose: print('  slabs %d..%d of %d, %.0f s' % (l1a, l1b - 1, N1, time.time() - t0), flush=True)
    t3 = time.time()
    coef = {}
    for ab in comps:
        ent = (D1 * arb_mat(S[ab])).entries()
        coef[ab] = np.array([float(abs(e).upper()) for e in ent]).reshape(N1, N2, N3)
    alphas = [(a1, a2, a3) for a1 in range(K + 1) for a2 in range(K + 1) for a3 in range(K + 1) if a1 + a2 + a3 <= K]
    S_all = [[cert.Ssum(rho[d], l, 0) for l in range(K + 1)] for d in range(3)]
    S_gt = [[cert.Ssum(rho[d], l, N[d] + 1) for l in range(K + 1)] for d in range(3)]
    W = [[np.array([float(cert.Tl1(n, l)) for n in range(N[d] + 1)]) for l in range(K + 1)] for d in range(3)]
    thl, shl = float(th.lower()), float(sh.lower())
    out = {}
    for ab in comps:
        out[ab] = {}
        for al in alphas:
            w = np.multiply.outer(np.multiply.outer(W[0][al[0]], W[1][al[1]]), W[2][al[2]])
            main = float((coef[ab] * w).sum()) * (1 + 1e-12)
            Ea = 16 * M * sum(S_gt[d][al[d]] * np.prod([S_all[e][al[e]] for e in range(3) if e != d]) for d in range(3))
            out[ab][''.join(map(str, al))] = dict(main=main / (thl ** al[0] * shl ** al[1]) * (1 + 1e-12),
                                                   tail=Ea / (thl ** al[0] * shl ** al[1]) * (1 + 1e-12))
    t4 = time.time()
    res = dict(case=case, element=[i + 1, j + 1], sub=[str(q) for q in sub], N=list(N), rho=list(rho), prec=prec, K=K, M=M,
               ReRseed_min=minfo['ReRs_min'], maxQR=minfo['maxQR'], times=dict(prepare=t1 - t0, majorant=t2 - t1, nodes=t3 - t2, bounds=t4 - t3),
               nodes=N1 * N2 * N3, degrees={F: [q - 1 for q in shp[F]] for F in FN}, bounds=out)
    if verbose:
        for l in range(K + 1):
            b = max(max(v['main'] + v['tail'] for kk, v in out[ab].items() if sum(map(int, kk)) == l) for ab in comps)
            bm = max(max(v['main'] for kk, v in out[ab].items() if sum(map(int, kk)) == l) for ab in comps)
            print('  |alpha| = %d: sup_box max_ab |d^alpha f~_ab| <= %.3e  (interpolant part %.3e)' % (l, b, bm), flush=True)
        print('%s element (%d,%d): N = %s, rho = %s, M = %.3e, %d nodes; times %s' % (case, i + 1, j + 1, N, rho, M, N1 * N2 * N3,
              {k: round(v) for k, v in res['times'].items()}), flush=True)
    return res

def majorant_only(case, zfile, i, j, rhos):
    zs = pickle.load(open(zfile, 'rb')); L = rep.layout(case); sub = cert.use_region(L, i, j)
    G, Q = prepare(zs, case, i, j, sub)
    for rho in rhos:
        try:
            M, info = majorant_from(Q, case, i, j, sub, rho); print('rho', rho, 'M = %.3e' % M, flush=True)
        except Exception as ex:
            print('rho', rho, 'failed:', ex, flush=True)

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == '--majorant':
        rhos = [tuple(float(q) for q in r.split(',')) for r in a[5:]]
        majorant_only(a[1], a[2], int(a[3]) - 1, int(a[4]) - 1, rhos); sys.exit(0)
    r = certify(a[0], a[1], int(a[2]) - 1, int(a[3]) - 1, tuple(int(q) for q in a[4:7]), tuple(float(q) for q in a[7:10]), int(a[10]), int(a[11]))
    json.dump(r, open(a[12], 'w'), indent=1)
