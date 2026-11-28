"""The solution on the line where a checkpointed column ends, read from a solver checkpoint (quad-double BSOLQ1 or
double-double BSOLV1), with the node coordinates.

    python3 ckptline.py RUN.cfg RUN.ckpt OUT.npz

The checkpoint holds, after column c of the quadrant being marched, the right edge of that column for every row j: G of
R, m, n, W (G = (F - F_seed)/(v - 1/2)^4, F_seed = 0 for m and n) at xi = xi_c, the row's v-nodes and the x-nodes
x_k = cos(pi k/M), k = 0..M. (s is not on it: its equation has no u-derivative, and each column integrates it in v from
N0.) OUT.npz holds:
  G      float64 (nrow, 4, nB, M+1, NW): the NW double parts of each value (their exact sum is the value);
         fields in the order R, m, n, W; rows from v = 1/2 outward; v-nodes ascending
  v      str (nrow, nB): the v-nodes to 40 digits (row 0: Radau nodes, excluding v = 1/2; others: Chebyshev-Lobatto)
  x      str (M+1,): the x-nodes to 40 digits
  xi     str: xi_c to 40 digits; u = -1 + sinh(xi)/500
  info   str: quadrant index, column, cells, configuration
Run the reader on a copy; it reads only the header and the edges (the first few tens of MB)."""
import sys, struct, numpy as np, mpmath as mp
mp.mp.dps = 60

def cfg(fn):
    c = {}
    for line in open(fn):
        p = line.split()
        if not p or p[0].startswith('#'): continue
        c.setdefault(p[0], []).append(p[1:])
    return c

def main():
    cf, ck, out = sys.argv[1:4]
    C = cfg(cf)
    pxi, pv, M = int(C['pxi'][0][0]), int(C['pv'][0][0]), int(C['M'][0][0])
    ncol, _, nrow, _ = (int(q) for q in C['cells'][0])
    xi_hi, v_hi = mp.mpf(C['domain'][0][1]), mp.mpf(C['domain'][0][3])
    f = open(ck, 'rb'); mg = f.read(6)
    NW = {b'BSOLQ1': 4, b'BSOLV1': 2}[mg]
    qi, col = struct.unpack('<ii', f.read(8)); cells, secs, sweeps = struct.unpack('<ddd', f.read(24))
    nl = struct.unpack('<i', f.read(4))[0]
    NX, nB = M + 1, pv + 1
    G = np.zeros((nl, 4, nB, NX, NW))
    for j in range(nl):
        n = struct.unpack('<q', f.read(8))[0]
        assert n == 4 * nB * NX, (n, 4 * nB * NX)
        G[j] = np.frombuffer(f.read(n * 8 * NW), dtype='<f8').reshape(4, nB, NX, NW)
        m = struct.unpack('<q', f.read(8))[0]; f.seek(m * 8 * NW, 1)          # sv (empty on these edges)
    # geometry, as the solver builds it (quadrant 1: from the corner (xi(-10), 1/2) toward +xi, +v)
    a = mp.mpf(1) / 500
    xi0 = mp.asinh(mp.mpf(-9) / a)
    xic = xi0 + (xi_hi - xi0) * col / ncol
    vb = [mp.mpf(1) / 2 + (v_hi - mp.mpf(1) / 2) * j / nrow for j in range(nrow + 1)]
    lob = [-mp.cos(mp.pi * b / pv) for b in range(pv + 1)]
    rad = sorted(mp.cos(2 * mp.pi * b / (2 * pv + 1)) for b in range(pv + 1))
    V = []
    for j in range(nl):
        t = rad if j == 0 else lob
        h = (vb[j + 1] - vb[j]) / 2
        V.append([mp.nstr(vb[j] + h * (t[b] + 1), 40) for b in range(nB)])
    X = [mp.nstr(mp.cos(mp.pi * k / M), 40) for k in range(NX)]
    info = 'quadrant index %d (order %s), column %d of %d, cells %d, solver seconds %.0f; config %s' % (
        qi, C['quadrants'][0][0], col, ncol, cells, secs, cf)
    np.savez_compressed(out, G=G, v=np.array(V), x=np.array(X), xi=mp.nstr(xic, 40), info=info)
    print(info); print('xi_c =', mp.nstr(xic, 30), ' u_c =', mp.nstr(-1 + mp.sinh(xic) * a, 30))
    print('G shape', G.shape, ' max|G| per field', [float(np.abs(G[:, q, ..., 0]).max()) for q in range(4)])

if __name__ == '__main__':
    main()
