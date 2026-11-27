"""Spectral constants for the solver, computed in 50-digit arithmetic (mpmath) and written as double-double pairs.
usage: consts.py pxi pv M out.bin
Records (name, rows, cols, then rows*cols (hi, lo) pairs, row-major):
  L{p}_t, L{p}_Q, L{p}_D, L{p}_w  Chebyshev-Lobatto nodes on [-1, 1] ascending; integration from -1; derivative;
                                   barycentric weights
  R{p}_t, R{p}_Q, R{p}_D, R{p}_w  Radau nodes tau_j = -cos(2 pi j/(2p+1)) reflected: they include +1 and exclude -1
  R{p}_W4, R{p}_V4                 on sigma = (tau + 1)/2: q -> sigma^-4 int_0^sigma s^3 q, phi -> sigma^-4 int_0^sigma
                                   (sigma - s) s^2 phi (exact on polynomials of degree p)
  R{p}_TT                          Taylor coefficients at sigma = 0 of the interpolant, orders 0..8 (in sigma)
  X{M}_x, X{M}_D1, X{M}_D2, X{M}_C  x_k = cos(pi k/M), k = 0..M; derivative matrices; values -> Chebyshev coefficients"""
import sys, struct, mpmath as mp
mp.mp.dps = 50

def cheb_T(n, t):
    T = [mp.mpf(1), t]
    for k in range(2, n + 1):
        T.append(2 * t * T[-1] - T[-2])
    return T[:n + 1]

def lagrange_poly_coeffs(nodes):
    """monomial coefficients (in the variable of nodes) of each Lagrange basis polynomial"""
    n = len(nodes)
    out = []
    for j in range(n):
        c = [mp.mpf(1)]
        den = mp.mpf(1)
        for k in range(n):
            if k == j:
                continue
            c = [mp.mpf(0)] + c
            for i in range(len(c) - 1):
                c[i] -= nodes[k] * c[i + 1]
            den *= nodes[j] - nodes[k]
        out.append([ci / den for ci in c])
    return out

def peval(c, t):
    s = mp.mpf(0)
    for ci in reversed(c):
        s = s * t + ci
    return s

def pint(c):
    return [mp.mpf(0)] + [ci / (i + 1) for i, ci in enumerate(c)]

def pder(c):
    return [ci * i for i, ci in enumerate(c)][1:] or [mp.mpf(0)]

def bary(nodes):
    w = []
    for j in range(len(nodes)):
        p = mp.mpf(1)
        for k in range(len(nodes)):
            if k != j:
                p *= nodes[j] - nodes[k]
        w.append(1 / p)
    mx = max(abs(a) for a in w)
    return [a / mx for a in w]

def node_set(nodes, tag, radau):
    L = lagrange_poly_coeffs(nodes)             # in tau
    n = len(nodes)
    recs = {}
    recs[tag + '_t'] = [[t] for t in nodes]
    Q = [[mp.mpf(0)] * n for _ in range(n)]; D = [[mp.mpf(0)] * n for _ in range(n)]
    for j in range(n):
        Ij = pint(L[j]); Dj = pder(L[j])
        base = peval(Ij, mp.mpf(-1))
        for i in range(n):
            Q[i][j] = peval(Ij, nodes[i]) - base
            D[i][j] = peval(Dj, nodes[i])
    recs[tag + '_Q'] = Q; recs[tag + '_D'] = D
    recs[tag + '_w'] = [[a] for a in bary(nodes)]
    if radau:
        sig = [(t + 1) / 2 for t in nodes]
        Ls = lagrange_poly_coeffs(sig)
        W4 = [[mp.mpf(0)] * n for _ in range(n)]; V4 = [[mp.mpf(0)] * n for _ in range(n)]
        for j in range(n):
            c3 = [mp.mpf(0)] * 3 + Ls[j]                      # s^3 l_j
            c2 = [mp.mpf(0)] * 2 + Ls[j]                      # s^2 l_j
            I3 = pint(c3); I2 = pint(c2); I2s = pint([mp.mpf(0)] + c2)   # int s^2 l, int s^3 l
            for i in range(n):
                si = sig[i]
                W4[i][j] = peval(I3, si) / si ** 4
                V4[i][j] = (si * peval(I2, si) - peval(I2s, si)) / si ** 4
        recs[tag + '_W4'] = W4; recs[tag + '_V4'] = V4
        TT = [[Ls[j][k] if k < len(Ls[j]) else mp.mpf(0) for j in range(n)] for k in range(9)]
        recs[tag + '_TT'] = TT
    return recs

def lobatto(p):
    return [-mp.cos(mp.pi * j / p) for j in range(p + 1)]

def radau(p):
    t = [mp.cos(2 * mp.pi * j / (2 * p + 1)) for j in range(p + 1)]   # includes +1, excludes -1
    return sorted(t)

def xset(M):
    xs = [mp.cos(mp.pi * k / M) for k in range(M + 1)]
    # values -> coefficients (DCT-I)
    C = [[mp.mpf(0)] * (M + 1) for _ in range(M + 1)]
    for a in range(M + 1):
        for k in range(M + 1):
            ck = mp.mpf(0.5) if k in (0, M) else mp.mpf(1)
            C[a][k] = 2 * ck * mp.cos(mp.pi * a * k / M) / M
        if a in (0, M):
            for k in range(M + 1):
                C[a][k] /= 2
    # derivative in coefficient space
    def dcoef(c):
        n = len(c); d = [mp.mpf(0)] * n
        for i in range(n - 2, -1, -1):
            d[i] = (d[i + 2] if i + 2 < n else 0) + 2 * (i + 1) * c[i + 1]
        d[0] /= 2
        return d
    Tm = [cheb_T(M, x) for x in xs]          # Tm[k][a] = T_a(x_k)
    D1 = [[mp.mpf(0)] * (M + 1) for _ in range(M + 1)]; D2 = [[mp.mpf(0)] * (M + 1) for _ in range(M + 1)]
    for j in range(M + 1):
        c = [C[a][j] for a in range(M + 1)]
        d1 = dcoef(c); d2 = dcoef(d1)
        for k in range(M + 1):
            D1[k][j] = mp.fsum(d1[a] * Tm[k][a] for a in range(M + 1))
            D2[k][j] = mp.fsum(d2[a] * Tm[k][a] for a in range(M + 1))
    return {'X%d_x' % M: [[x] for x in xs], 'X%d_D1' % M: D1, 'X%d_D2' % M: D2, 'X%d_C' % M: C}

def write(recs, fn):
    with open(fn, 'wb') as f:
        for name, A in recs.items():
            r, c = len(A), len(A[0])
            f.write(name.encode().ljust(16, b'\0')); f.write(struct.pack('<ii', r, c))
            for row in A:
                for a in row:
                    hi = float(a); lo = float(a - mp.mpf(hi))
                    f.write(struct.pack('<dd', hi, lo))

if __name__ == '__main__':
    pxi, pv, M = (int(a) for a in sys.argv[1:4])
    recs = {}
    for p in sorted({pxi, pv}):
        recs.update(node_set(lobatto(p), 'L%d' % p, False))
    recs.update(node_set(radau(pv), 'R%d' % pv, True))
    recs.update(xset(M))
    write(recs, sys.argv[4])
    print('written', sys.argv[4], len(recs), 'records')
