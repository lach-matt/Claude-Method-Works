"""N-APP1 certification prototype (computed in ball arithmetic, python-flint arb/acb; every number below is an enclosure,
none a floating-point sample).  Method of P-APPC, the interpolation-and-polyellipse bound, on one element box:

 g = (f_ab of the element's own polynomial approximant F = F_seed + (v - 1/2)^4 G), f_lx and f_nx divided by
     sqrt(1 - x^2) (the axis-regular scheme, regform.py), as a function of the element coordinates (t, sigma, x).
 1. M >= sup |g| on the distinguished boundary of the polyellipse E_rho1 x E_rho2 x E_rho3 (complex balls on a
    covering of the torus by arcs);
 2. the values of g at the (N1+1)(N2+1)(N3+1) Chebyshev-Lobatto points, in ball arithmetic, and the coefficients c of
    the interpolant p (exact discrete Chebyshev transform, ball arithmetic);
 3. for every multi-index alpha, |alpha| <= 3:  sup_box |d^alpha g| <= sum |c^(alpha)| + E_alpha,
    E_alpha = 16 M sum_d S_d^{>N_d}(alpha_d) prod_{d' != d} S_{d'}(alpha_{d'}),   S(l) = sum_i rho^-i T_i^(l)(1).
usage: cert.py case i j [N1 N2 N3] [rho1 rho2 rho3] [arcs] [prec]"""
import sys, json, time, math, numpy as np
import flint
from flint import arb, acb, arb_mat, acb_mat, fmpq
import rep
from regform import regular_components

FN = rep.FIELDS


def deriv_coeffs_int(c, axis):
    """exact derivative map (eq:tl5-cheb-derivative) on an integer (object) array along axis"""
    c = np.moveaxis(c, axis, 0)
    n = c.shape[0]
    out = np.zeros_like(c)
    # c'_{i} = (2/(1+delta_i0)) sum_{i'>i, i'-i odd} i' c_{i'}   (integers: for i = 0 the factor 1)
    acc_odd = np.zeros_like(c[0]); acc_even = np.zeros_like(c[0])
    for i in range(n - 1, -1, -1):
        # sum over i' > i with i' - i odd
        s = acc_odd if (i % 2 == 0) else acc_even
        out[i] = (2 if i > 0 else 1) * s
        # add term i to the accumulators for smaller indices
        if i % 2 == 1:
            acc_odd = acc_odd + i * c[i]
        else:
            acc_even = acc_even + i * c[i]
    return np.moveaxis(out, 0, axis)


def affine_matrix(n, c, h):
    """exact rational matrix A with T_j(c + h tau) = sum_k A[j][k] T_k(tau), j, k < n (c, h Fractions)"""
    from fractions import Fraction as Fr
    def mul_tau(vec):            # tau * sum v_k T_k  =  sum v_k (T_{k+1} + T_{|k-1|})/2
        out = [Fr(0)] * (len(vec) + 1)
        for k, a in enumerate(vec):
            if a == 0:
                continue
            out[k + 1] += a / 2
            out[abs(k - 1)] += a / 2
        return out
    rows = [[Fr(1)], [c, h]]
    for j in range(1, n - 1):
        t1 = mul_tau(rows[j])
        nxt = [Fr(0)] * (j + 2)
        for k in range(len(rows[j])):
            nxt[k] += 2 * c * rows[j][k]
        for k in range(len(t1)):
            nxt[k] += 2 * h * t1[k]
        for k in range(len(rows[j - 1])):
            nxt[k] -= rows[j - 1][k]
        rows.append(nxt)
    A = [[Fr(0)] * n for _ in range(n)]
    for j in range(n):
        for k, a in enumerate(rows[j][:n]):
            A[j][k] = a
    return A


def reexpand(C, axis, c, h):
    """coefficients of the same polynomial in tau, where the old variable is c + h tau (exact, object arrays)"""
    C = np.moveaxis(C, axis, 0)
    n = C.shape[0]
    A = affine_matrix(n, c, h)
    out = np.zeros_like(C, dtype=object)
    for j in range(n):
        for k in range(j + 1):
            if A[j][k] != 0:
                out[k] = out[k] + A[j][k] * C[j]
    return np.moveaxis(out, 0, axis)


def lobatto(N):
    return [arb(fmpq(l, N)).cos_pi() for l in range(N + 1)]


def vander(pts, n):
    """V[l][k] = T_k(pts[l]) for k < n (arb)"""
    V = []
    for x in pts:
        row = [arb(1), x]
        for k in range(2, n):
            row.append(2 * x * row[-1] - row[-2])
        V.append(row[:n])
    return V


def _q(e):
    from fractions import Fraction as Fr
    if isinstance(e, Fr):
        return arb(fmpq(e.numerator, e.denominator))
    return int(e)


def tensor_eval(C, V1, V2, V3):
    """values[l1][l2][l3] = sum C[a,b,k] V1[l1][a] V2[l2][b] V3[l3][k];  C integer (object) array"""
    n1, n2, n3 = C.shape
    N1, N2, N3 = len(V1), len(V2), len(V3)
    A = arb_mat([[_q(C[a, b, k]) for k in range(n3)] for a in range(n1) for b in range(n2)])
    B3 = arb_mat([[V3[l][k] for l in range(N3)] for k in range(n3)])
    M1 = A * B3                                          # (n1 n2) x N3
    M1l = M1.entries()                                    # row-major
    # rows (a, b), cols l3 -> matrix (n2) x (n1 N3): entry [b, a*N3 + l3]
    R2 = [[M1l[(a * n2 + b) * N3 + l3] for a in range(n1) for l3 in range(N3)] for b in range(n2)]
    B2 = arb_mat([[V2[l][b] for b in range(n2)] for l in range(N2)])
    M2 = B2 * arb_mat(R2)                                 # N2 x (n1 N3)
    M2l = M2.entries()
    R3 = [[M2l[l2 * (n1 * N3) + a * N3 + l3] for l2 in range(N2) for l3 in range(N3)] for a in range(n1)]
    B1 = arb_mat([[V1[l][a] for a in range(n1)] for l in range(N1)])
    M3 = B1 * arb_mat(R3)                                 # N1 x (N2 N3)
    return M3.entries(), (N1, N2, N3)


def _krawczyk(H, is_c, eps0=None):
    """unique root R of G(R) := 2R + log((R-1)/(R+1)) = H in a ball, for a ball H (arb or acb); None if not shown"""
    import cmath
    Hm = H.mid() if not is_c else acb(H.real.mid(), H.imag.mid())
    h0 = complex(Hm) if is_c else float(Hm)
    r = h0 / 2 + 0.6
    for _ in range(80):
        g = 2 * r + (cmath.log((r - 1) / (r + 1)) if is_c else math.log((r - 1) / (r + 1)))
        r = r - (g - h0) / (2 * r * r / (r * r - 1))
    rc = acb(r.real, r.imag) if is_c else arb(r)
    for _ in range(3):
        rc = rc - (2 * rc + ((rc - 1) / (rc + 1)).log() - Hm) / (2 + 2 / (rc * rc - 1))
        rc = rc.mid() if not is_c else acb(rc.real.mid(), rc.imag.mid())
    radH = (float(H.real.rad()) + float(H.imag.rad())) if is_c else float(H.rad())
    eps = 1e-30 * (abs(complex(r)) if is_c else abs(r)) + 0.6 * radH + 1e-35
    Gc = 2 * rc + ((rc - 1) / (rc + 1)).log()
    for _ in range(12):
        X = (rc + acb(arb(0, eps), arb(0, eps))) if is_c else arb(rc.mid(), eps)
        Nx = rc - (Gc - H) / (2 + 2 / (X * X - 1))
        if X.contains(Nx) and (Nx.real.lower() if is_c else Nx.lower()) > 1.5:
            return Nx
        eps *= 1.4
    return None


def seed_R(H, is_c, depth=0):
    """enclosure of R_seed = G^-1(H) over the ball H, splitting H when one interval Newton step does not contract"""
    R = _krawczyk(H, is_c)
    if R is not None:
        return R
    if depth > 8:
        raise RuntimeError('interval Newton for the seed did not contract')
    if is_c:
        a, b = H.real, H.imag
        parts = []
        for sa in (-1, 1):
            for sb in (-1, 1):
                ra, rb = a.rad() / 2, b.rad() / 2
                parts.append(acb(arb(a.mid() + sa * ra, ra * 1.0000001), arb(b.mid() + sb * rb, rb * 1.0000001)))
        Rs = [seed_R(p, True, depth + 1) for p in parts]
        out = Rs[0]
        for q in Rs[1:]:
            out = out.union(q)
        return out
    ra = H.rad() / 2
    R1 = seed_R(arb(H.mid() - ra, ra * 1.0000001), False, depth + 1); R2 = seed_R(arb(H.mid() + ra, ra * 1.0000001), False, depth + 1)
    return R1.union(R2)


def seed_jets(u, v):
    """R_seed and the derivatives of R_seed, W_seed to order 2 at a point or ball (arb or acb), and
    Omega_seed^2 = f(R)/(2 f(-u)): R_seed by interval Newton on G(R) = H := v - 2u + log((u+1)/(u-1)), Re R > 3/2
    (G is injective with G' != 0 there), then the exact derivative formulas of lem:tl5-seed."""
    is_c = isinstance(u, acb)
    H = v - 2 * u + ((u + 1) / (u - 1)).log()
    R = seed_R(H, is_c)
    T = acb if is_c else arb
    X = R
    f = 1 - 1 / (R * R); fp = 2 / (R * R * R); fpp = -6 / (R * R * R * R)
    g = 1 - 1 / (u * u); gp = 2 / (u * u * u); gpp = -6 / (u * u * u * u)
    Rv = f / 2; Ru = -f / g
    Rvv = fp * Rv / 2; Ruv = fp * Ru / 2
    Ruu = -fp * Ru / g + f * gp / (g * g)
    OM2s = f / (2 * g)
    Wv = fp * Rv / (2 * f); Wu = (fp * Ru / f - gp / g) / 2
    Wvv = (fpp * Rv * Rv + fp * Rvv) / (2 * f) - (fp * Rv) ** 2 / (2 * f * f)
    Wuv = (fpp * Ru * Rv + fp * Ruv) / (2 * f) - (fp * Ru) * (fp * Rv) / (2 * f * f)
    Wuu = ((fpp * Ru * Ru + fp * Ruu) / f - (fp * Ru / f) ** 2 - (gpp / g - (gp / g) ** 2)) / 2
    z = T(0)
    return ({'': R, 'u': Ru, 'v': Rv, 'x': z, 'uu': Ruu, 'uv': Ruv, 'vv': Rvv, 'ux': z, 'vx': z, 'xx': z},
            {'': z, 'u': Wu, 'v': Wv, 'x': z, 'uu': Wuu, 'uv': Wuv, 'vv': Wvv, 'ux': z, 'vx': z, 'xx': z}, OM2s, X)


DER = {'': (0, 0, 0), 't': (1, 0, 0), 's': (0, 1, 0), 'x': (0, 0, 1), 'tt': (2, 0, 0), 'ts': (1, 1, 0),
       'ss': (0, 2, 0), 'tx': (1, 0, 1), 'sx': (0, 1, 1), 'xx': (0, 0, 2)}


def deriv_arrays_tau(c, th, sh):
    """derivative arrays in (t, sigma, x) of a polynomial given in the box variables tau (t = tc + th tau1, ...):
    d/dt = (1/th) d/dtau1, d/dsigma = (1/sh) d/dtau2 (exact)"""
    out = {}
    for name, a in DER.items():
        cc = c
        for ax in range(3):
            for _ in range(a[ax]):
                cc = deriv_coeffs_int(cc, ax)
        fac = (1 / th) ** a[0] * (1 / sh) ** a[1]
        out[name] = cc * fac
    return out


def deriv_arrays(z):
    out = {}
    for name, a in DER.items():
        c = z.astype(object)
        for ax in range(3):
            for _ in range(a[ax]):
                c = deriv_coeffs_int(c, ax)
        out[name] = c
    return out


def node_jets(Gd, chart, seedJ, vq, x, scale):
    """2-jets in (u, v, x) of the five fields at one point; Gd[k][name] the (t, sigma, x)-derivatives of G^k there
    (already times scale = 10^-p); chart = (phi1, phi2, 1/h'); vq = v - 1/2."""
    p1, p2, iv = chart
    J = {}
    v2 = vq * vq; v3 = v2 * vq; v4 = v2 * v2
    for k in FN:
        g = Gd[k]
        G_ = g['']; Gu = p1 * g['t']; Gv = iv * g['s']; Gx = g['x']
        Guu = p1 * p1 * g['tt'] + p2 * g['t']; Guv = p1 * iv * g['ts']; Gvv = iv * iv * g['ss']
        Gux = p1 * g['tx']; Gvx = iv * g['sx']; Gxx = g['xx']
        Q = {'': v4 * G_, 'u': v4 * Gu, 'v': 4 * v3 * G_ + v4 * Gv, 'x': v4 * Gx, 'uu': v4 * Guu,
             'uv': 4 * v3 * Gu + v4 * Guv, 'vv': 12 * v2 * G_ + 8 * v3 * Gv + v4 * Gvv, 'ux': v4 * Gux,
             'vx': 4 * v3 * Gx + v4 * Gvx, 'xx': v4 * Gxx}
        if k in ('R', 'W'):
            S = seedJ[0] if k == 'R' else seedJ[1]
            J[k] = {d: S[d] + Q[d] for d in Q}
        else:
            J[k] = Q
    # W enters only through its derivatives and Omega^2 = e^{2W} = (f(R_s)/(2 f(-u))) e^{2 (v-1/2)^4 G_W}
    OM2 = seedJ[2] * (2 * J['W']['']).exp()
    return J, OM2


def residual_at(JO, x, one):
    J, OM2 = JO
    S = ((1 + x) * J['m'][''] + (1 - x) * J['n']['']) / 3
    f = regular_components(x, J, S.exp(), OM2, one=one)
    rho = (J['R'][''] ** 2) ** 2 / arb(72).sqrt()
    return {ab: rho * f[ab] for ab in f}


def Tl1(n, l):
    out = 1
    for r in range(l):
        out = out * (n * n - r * r) / (2 * r + 1)
    return max(out, 0)


def Ssum(rho, l, start, nmax=4000):
    """sum_{i >= start} rho^-i T_i^(l)(1), with an explicit geometric tail beyond nmax (ratio test bound)"""
    s = 0.0
    for i in range(start, nmax):
        s += rho ** (-i) * Tl1(i, l)
    # tail: T_n^(l)(1) <= n^(2l)/(1*3*...*(2l-1)) =: b_n, and b_(n+1)/(rho b_n) = ((n+1)/n)^(2l)/rho decreases in n
    c = 1.0
    for r in range(l):
        c *= (2 * r + 1)
    q = ((nmax + 1) / nmax) ** (2 * l) / rho
    assert q < 1
    tail = rho ** (-nmax) * nmax ** (2 * l) / c / (1 - q)
    return (s + tail) * (1 + 1e-12)


def certify(case, i, j, N=(40, 48, 32), rho=(2.0, 2.0, 2.0), arcs=(12, 12, 12), prec=128, source='prov', verbose=True, sub=None, K=3):
    flint.ctx.prec = prec
    t0 = time.time()
    meta = json.load(open('%s_%s.json' % (source, case))); p = meta['p']
    Z = dict(np.load('%s_%s.npz' % (source, case), allow_pickle=True))
    L = rep.layout(case, enlarge=True) if source == 'prov2' else rep.layout(case, enlarge=True, clip=(rep.xi_of_u(-10), 0.5, 3.5))
    mx, hx = L['xi'][i]; mv, hv = L['v'][j]
    if sub is None:
        sub = use_region(L, i, j)
    tc, th, sc, sh = (arb(fmpq(q.numerator, q.denominator)) for q in sub)
    mx_a, hx_a, mv_a, hv_a = (arb(fmpq(q.numerator, q.denominator)) for q in (mx, hx, mv, hv))
    a_ch = arb(fmpq(1, 500))
    scale = arb(10) ** (-p)
    from fractions import Fraction as Fr
    Gt = {}
    for k in FN:
        c = Z['%d_%d_%s' % (i, j, k)].astype(object)
        c = reexpand(c, 0, Fr(sub[0]), Fr(sub[1])); c = reexpand(c, 1, Fr(sub[2]), Fr(sub[3]))
        Gt[k] = c
    G = {k: deriv_arrays_tau(Gt[k], Fr(sub[1]), Fr(sub[3])) for k in FN}
    n1, n2, n3 = G['R'][''].shape
    # ---- step 2: values at the Lobatto points
    P1, P2, P3 = lobatto(N[0]), lobatto(N[1]), lobatto(N[2])
    V1, V2, V3 = vander(P1, n1), vander(P2, n2), vander(P3, n3)
    P1 = [tc + th * q for q in P1]; P2 = [sc + sh * q for q in P2]       # node positions in (t, sigma)
    vals = {}
    for k in FN:
        vals[k] = {}
        for name, c in G[k].items():
            e, shp = tensor_eval(c, V1, V2, V3)
            vals[k][name] = e
    t1 = time.time()
    NN = (N[0] + 1) * (N[1] + 1) * (N[2] + 1)
    g = {ab: [None] * NN for ab in ('ll', 'ln', 'nn', 'lx', 'nx', 'xx', '11', '22')}
    one = arb(1)
    for l1 in range(N[0] + 1):
        t_ = P1[l1]; xi = mx_a + hx_a * t_
        u = -1 + a_ch * xi.sinh()
        ch = xi.cosh(); p1 = 1 / (ch * hx_a * a_ch); p2 = -(p1 * p1) * (xi.sinh() / ch) * hx_a
        for l2 in range(N[1] + 1):
            v = mv_a + hv_a * P2[l2]
            seedJ = seed_jets(u, v)
            chart = (p1, p2, 1 / hv_a)
            for l3 in range(N[2] + 1):
                idx = (l1 * (N[1] + 1) + l2) * (N[2] + 1) + l3
                Gd = {k: {name: vals[k][name][idx] * scale for name in DER} for k in FN}
                J = node_jets(Gd, chart, seedJ, v - one / 2, P3[l3], scale)
                f = residual_at(J, P3[l3], one)
                for ab in g:
                    g[ab][idx] = f[ab]
    t2 = time.time()
    # ---- interpolant coefficients: c = (2/N)'' sums, per direction (Lobatto, DCT-I), as matrix products
    def dct_mat(Nd):
        rows = []
        for kk in range(Nd + 1):
            r = []
            for l in range(Nd + 1):
                w = arb(1) if 0 < l < Nd else arb(1) / 2
                c = w * arb(fmpq(kk * l, Nd)).cos_pi() * 2 / Nd
                if kk == 0 or kk == Nd:
                    c = c / 2
                r.append(c)
            rows.append(r)
        return arb_mat(rows)
    D1, D2, D3 = dct_mat(N[0]), dct_mat(N[1]), dct_mat(N[2])
    def transform(vlist):
        N1, N2, N3 = N[0] + 1, N[1] + 1, N[2] + 1
        A = arb_mat([[vlist[(a * N2 + b) * N3 + c] for c in range(N3)] for a in range(N1) for b in range(N2)])
        M1 = (A * D3.transpose()).entries()           # (N1 N2) x K3
        R2 = [[M1[(a * N2 + b) * N3 + c] for a in range(N1) for c in range(N3)] for b in range(N2)]
        M2 = (D2 * arb_mat(R2)).entries()            # K2 x (N1 N3)
        R3 = [[M2[b * (N1 * N3) + a * N3 + c] for b in range(N2) for c in range(N3)] for a in range(N1)]
        M3 = (D1 * arb_mat(R3)).entries()            # K1 x (K2 K3)
        out = np.empty((N1, N2, N3), dtype=object)
        for a in range(N1):
            for b in range(N2):
                for c in range(N3):
                    out[a, b, c] = M3[a * (N2 * N3) + b * N3 + c]
        return out
    coef = {ab: transform(g[ab]) for ab in g}
    t3 = time.time()
    # ---- step 1: M on the distinguished boundary of the polyellipse (acb on arcs)
    import majorant
    M, minfo = majorant.majorant_M(Z, p, L, i, j, sub, rho)
    rmin, nHb, Hrect, MR = minfo['ReRs_min'], minfo['H_balls'], None, minfo['ReRs_min'] - minfo['maxQR']
    t4 = time.time()
    # ---- step 3: bounds for |alpha| <= 3
    alphas = [(a1, a2, a3) for a1 in range(K + 1) for a2 in range(K + 1) for a3 in range(K + 1) if a1 + a2 + a3 <= K]
    S_all = [[Ssum(rho[d], l, 0) for l in range(K + 1)] for d in range(3)]
    S_gt = [[Ssum(rho[d], l, N[d] + 1) for l in range(K + 1)] for d in range(3)]
    out = {}
    for ab, c in coef.items():
        out[ab] = {}
        for al in alphas:
            cd = c
            for ax in range(3):
                for _ in range(al[ax]):
                    cd = deriv_coeffs_arb(cd, ax)
            main = arb(0)
            for e in cd.flat:
                main += abs(e)
            Ea = 16 * M * sum(S_gt[d][al[d]] * np.prod([S_all[e][al[e]] for e in range(3) if e != d]) for d in range(3))
            # derivatives in tau -> in (t, sigma, x): divide by th^a1 sh^a2
            B = (main + arb(Ea)) / (th ** al[0] * sh ** al[1])
            out[ab][al] = float(B.upper())
    t5 = time.time()
    res = dict(case=case, element=[i + 1, j + 1], sub=[str(q) for q in sub], N=list(N), rho=list(rho), arcs=list(arcs), prec=prec, M=M,
               ReRseed_min=rmin, H_balls=nHb, H_rect=Hrect, min_ReR_torus=MR,
               times=dict(fields=t1 - t0, residual_nodes=t2 - t1, transform=t3 - t2, polyellipse=t4 - t3, bounds=t5 - t4),
               nodes=NN, bounds={ab: {''.join(map(str, al)): b for al, b in d.items()} for ab, d in out.items()})
    if verbose:
        b0 = max(out[ab][(0, 0, 0)] for ab in out)
        print('%s element (%d,%d): N = %s, rho = %s, M = %.3e; sup_box max_ab |f_ab| <= %.3e; times %s' %
              (case, i + 1, j + 1, N, rho, M, b0, {k: round(v, 1) for k, v in res['times'].items()}), flush=True)
    return res


def deriv_coeffs_arb(c, axis):
    c = np.moveaxis(c, axis, 0)
    n = c.shape[0]
    out = np.empty_like(c)
    zero = np.vectorize(lambda _: arb(0), otypes=[object])(c[0])
    acc_odd = zero.copy(); acc_even = zero.copy()
    for i in range(n - 1, -1, -1):
        s = acc_odd if (i % 2 == 0) else acc_even
        out[i] = s * (2 if i > 0 else 1)
        if i % 2 == 1:
            acc_odd = acc_odd + c[i] * i
        else:
            acc_even = acc_even + c[i] * i
    return np.moveaxis(out, 0, axis)


def ellipse_arcs(rho, n):
    """complex balls covering the ellipse {(w + 1/w)/2 : |w| = rho} in n arcs, and the arcs' T_k enclosures"""
    out = []
    for q in range(n):
        th0, th1 = 2 * math.pi * q / n, 2 * math.pi * (q + 1) / n
        thc = 0.5 * (th0 + th1); dth = 0.5 * (th1 - th0)
        out.append((thc, dth))
    return out


def T_on_arc(rho, thc, dth, nmax):
    """balls containing T_k(tau) for tau on the arc theta in [thc - dth, thc + dth] of the ellipse of parameter rho:
    T_k = (rho^k e^{ik theta} + rho^-k e^{-ik theta})/2; centre at thc, radius k dth (rho^k + rho^-k)/2 (mean value)"""
    res = []
    for k in range(nmax):
        c = 0.5 * (rho ** k * complex(math.cos(k * thc), math.sin(k * thc)) +
                   rho ** (-k) * complex(math.cos(k * thc), -math.sin(k * thc)))
        r = k * dth * 0.5 * (rho ** k + rho ** (-k)) * (1 + 1e-12) + 1e-300
        res.append(acb(arb(c.real, r), arb(c.imag, r)))
    return res


def use_region(L, i, j):
    """the element's use region (where its partition function is positive, intersected with D) in its (t, sigma):
    returns (tc, th, sc, sh) as fractions (rounded outward to 1/1000)"""
    from fractions import Fraction as Fr
    def one(ms, cuts, d, lo, hi, k):
        m, h = ms[k]
        a = lo if k == 0 else float(cuts[k - 1]) - float(d)
        b = hi if k == len(ms) - 1 else float(cuts[k]) + float(d)
        ta = Fr(math.floor((a - float(m)) / float(h) * 1000)) / 1000; tb = Fr(math.ceil((b - float(m)) / float(h) * 1000)) / 1000
        ta, tb = max(ta, Fr(-1)), min(tb, Fr(1))
        return (ta + tb) / 2, (tb - ta) / 2
    tc, th = one(L['xi'], L['cxi'], L['dxi'], L['xlo'], L['xhi'], i)
    sc, sh = one(L['v'], L['cv'], L['dv'], 0.5, 3.5, j)
    return (tc, th, sc, sh)


def polyellipse_M(case, i, j, G, scale, rho, arcs, box, sub):
    """sup |g| on the torus prod_d {tau_d on the ellipse E_rho_d}: each piece (product of arcs) is a product of complex
    balls; the fields and their derivatives there by the exact coefficient arrays and T_k enclosures; g by the regular
    scheme in complex ball arithmetic.  Returns a float upper bound (rounded up)."""
    mx_a, hx_a, mv_a, hv_a = box
    tc, th, sc, sh = sub
    a_ch = arb(fmpq(1, 500))
    n1, n2, n3 = G['R'][''].shape
    A = [ellipse_arcs(rho[d], arcs[d]) for d in range(3)]
    TAU = []
    for d in range(3):
        L_ = []
        for (thc, dth) in A[d]:
            # ball containing the arc: centre at thc, radius = arc half-chord bound
            w = rho[d]
            cpt = 0.5 * complex((w + 1 / w) * math.cos(thc), (w - 1 / w) * math.sin(thc))
            r = dth * 0.5 * (w + 1 / w) * (1 + 1e-12)
            L_.append(acb(arb(cpt.real, r), arb(cpt.imag, r)))
        TAU.append(L_)
    TA = [[T_on_arc(rho[d], thc, dth, (n1, n2, n3)[d]) for (thc, dth) in A[d]] for d in range(3)]
    TAU[0] = [tc + th * q for q in TAU[0]]; TAU[1] = [sc + sh * q for q in TAU[1]]     # positions in (t, sigma)
    # field derivative values on all pieces: tensor contraction with acb matrices
    vals = {}
    for k in FN:
        vals[k] = {}
        for name, c in G[k].items():
            vals[k][name] = tensor_eval_c(c, TA[0], TA[1], TA[2])
    Mx = 0.0; MR = 1e300
    one = acb(1)
    for q1 in range(arcs[0]):
        t_ = TAU[0][q1]; xi = mx_a + hx_a * t_
        u = -1 + a_ch * xi.sinh()
        ch = xi.cosh(); p1 = 1 / (ch * hx_a * a_ch); p2 = -(p1 * p1) * (xi.sinh() / ch) * hx_a
        for q2 in range(arcs[1]):
            v = mv_a + hv_a * TAU[1][q2]
            seedJ = seed_jets(u, v)
            for q3 in range(arcs[2]):
                idx = (q1 * arcs[1] + q2) * arcs[2] + q3
                Gd = {k: {name: vals[k][name][idx] * scale for name in DER} for k in FN}
                J = node_jets(Gd, (p1, p2, 1 / hv_a), seedJ, v - one / 2, TAU[2][q3], scale)
                vq = v - one / 2
                MR = min(MR, float(J[0]['R'][''].real.lower()))      # least Re R on the torus pieces
                f = residual_at(J, TAU[2][q3], one)
                for ab in f:
                    Mx = max(Mx, float(abs(f[ab]).upper()))
    return Mx, MR


def filled_boxes(rho, n):
    """complex balls covering the filled ellipse E_rho (an n x n grid of squares over its bounding rectangle, kept
    when they meet the ellipse)"""
    a = 0.5 * (rho + 1 / rho); b = 0.5 * (rho - 1 / rho)
    out = []
    for p in range(n):
        for q in range(n):
            x0, x1 = -a + 2 * a * p / n, -a + 2 * a * (p + 1) / n
            y0, y1 = -b + 2 * b * q / n, -b + 2 * b * (q + 1) / n
            # nearest point of the square to the origin-centred ellipse test: keep if some corner or the centre is inside,
            # or the square straddles an axis (conservative: keep when the inner corner is inside)
            xn = 0.0 if x0 <= 0 <= x1 else min(abs(x0), abs(x1)); yn = 0.0 if y0 <= 0 <= y1 else min(abs(y0), abs(y1))
            if (xn / a) ** 2 + (yn / b) ** 2 > 1:
                continue
            out.append(acb(arb(0.5 * (x0 + x1), 0.5 * (x1 - x0) * (1 + 1e-12)), arb(0.5 * (y0 + y1), 0.5 * (y1 - y0) * (1 + 1e-12))))
    return out


def analytic_checks(box, rho, n=24, nH=0.08):
    """on the filled polyellipse in (t, sigma): (i) Re cosh xi > 0, Re((u+1)/(u-1)) > 0 and Re u < -1 on a covering of
    the filled t-ellipse; (ii) the range of H = v - 2u + log((u+1)/(u-1)) lies in the rectangle covered by balls on each
    of which interval Newton gives a unique root of G(R) = H with Re R > 3/2, where G is injective and G' != 0, so that
    R_seed = G^-1 o H is holomorphic.  Returns the least lower bound of Re R_seed, or raises."""
    mx_a, hx_a, mv_a, hv_a = box
    a_ch = arb(fmpq(1, 500))
    Tb = filled_boxes(rho[0], n); Sb = filled_boxes(rho[1], n)
    Ks = []
    for tb in Tb:
        xi = mx_a + hx_a * tb
        if not xi.cosh().real > 0:
            raise RuntimeError('cosh xi may vanish')
        u = -1 + a_ch * xi.sinh()
        q = (u + 1) / (u - 1)
        if not (q.real > 0 and (u.real < -1)):
            raise RuntimeError('log((u+1)/(u-1)) or 1 - u^-2 not controlled')
        Ks.append(-2 * u + q.log())
    Vs = [mv_a + hv_a * sb for sb in Sb]
    lo_r = min(float(k.real.lower()) for k in Ks) + min(float(w.real.lower()) for w in Vs)
    hi_r = max(float(k.real.upper()) for k in Ks) + max(float(w.real.upper()) for w in Vs)
    lo_i = min(float(k.imag.lower()) for k in Ks) + min(float(w.imag.lower()) for w in Vs)
    hi_i = max(float(k.imag.upper()) for k in Ks) + max(float(w.imag.upper()) for w in Vs)
    rmin = 1e9; cnt = 0
    nr = int(math.ceil((hi_r - lo_r) / nH)); ni = int(math.ceil((hi_i - lo_i) / nH))
    for p in range(nr):
        for q_ in range(ni):
            Hb = acb(arb(lo_r + (p + 0.5) * nH, 0.5 * nH * 1.000001), arb(lo_i + (q_ + 0.5) * nH, 0.5 * nH * 1.000001))
            R = seed_R(Hb, True)
            rmin = min(rmin, float(R.real.lower())); cnt += 1
    return rmin, cnt, (lo_r, hi_r, lo_i, hi_i)


def T_ball(z, n):
    """enclosures of T_k(z), k < n, for a complex ball z: T_k(z) = cos(k arccos z) evaluated as (w^k + w^-k)/2 with
    w = z + sqrt(z^2 - 1) is not ball-friendly near [-1, 1]; use the recurrence with a centred correction: T_k(z) =
    T_k(z0) + (z - z0) T_k'(zeta), |T_k'| <= k U-bound; here simply the three-term recurrence in ball arithmetic"""
    out = [acb(1), z]
    for k in range(2, n):
        out.append(2 * z * out[-1] - out[-2])
    return out[:n]


def tensor_eval_c(C, V1, V2, V3):
    n1, n2, n3 = C.shape
    N1, N2, N3 = len(V1), len(V2), len(V3)
    A = acb_mat([[_q(C[a, b, k]) for k in range(n3)] for a in range(n1) for b in range(n2)])
    B3 = acb_mat([[V3[l][k] for l in range(N3)] for k in range(n3)])
    M1l = (A * B3).entries()
    R2 = [[M1l[(a * n2 + b) * N3 + l3] for a in range(n1) for l3 in range(N3)] for b in range(n2)]
    B2 = acb_mat([[V2[l][b] for b in range(n2)] for l in range(N2)])
    M2l = (B2 * acb_mat(R2)).entries()
    R3 = [[M2l[l2 * (n1 * N3) + a * N3 + l3] for l2 in range(N2) for l3 in range(N3)] for a in range(n1)]
    B1 = acb_mat([[V1[l][a] for a in range(n1)] for l in range(N1)])
    return (B1 * acb_mat(R3)).entries()


if __name__ == '__main__':
    case, i, j = sys.argv[1], int(sys.argv[2]) - 1, int(sys.argv[3]) - 1
    N = tuple(int(q) for q in sys.argv[4:7]) if len(sys.argv) > 6 else (40, 48, 32)
    rho = tuple(float(q) for q in sys.argv[7:10]) if len(sys.argv) > 9 else (2.0, 2.0, 2.0)
    arcs = tuple(int(q) for q in sys.argv[10:13]) if len(sys.argv) > 12 else (12, 12, 12)
    prec = int(sys.argv[13]) if len(sys.argv) > 13 else 128
    src = sys.argv[14] if len(sys.argv) > 14 else 'prov'
    K = int(sys.argv[15]) if len(sys.argv) > 15 else 3
    r = certify(case, i, j, N, rho, arcs, prec, source=src, K=K)
    json.dump(r, open('cert_%s_%d_%d.json' % (case, i + 1, j + 1), 'w'), indent=1)
