"""The solution on the line where a checkpointed column ends, read from a solver checkpoint (quad-double BSOLQ1 or
double-double BSOLV1), with the node coordinates.

    python3 ckptline.py RUN.cfg RUN.ckpt OUT.npz

The checkpoint holds, after column c of the quadrant being marched, the right edge of that column for every row j: G of
R, m, n, W (G = (F - F_seed)/(v - 1/2)^4, F_seed = 0 for m and n) at xi = xi_c, the row's v-nodes and the x-nodes
x_k = cos(pi k/M), k = 0..M. (s is not on it: its equation has no u-derivative, and each column integrates it in v from
N0.) OUT.npz holds:
  G      float64 (nrow, 4, nB, M+1, NW): the NW double parts of each value (their exact sum is the value);
         fields in the order R, m, n, W; rows and v-nodes as in v below
  v      str (nrow, nB): the v-nodes to 40 digits, in the solver's order: rows from v = 1/2 outward, nodes from the
         corner side outward (descending v in Q3, Q4); row 0: Radau nodes, excluding v = 1/2; others: Chebyshev-Lobatto
  x      str (M+1,): the x-nodes to 40 digits
  xi     str: xi_c to 40 digits (the quadrant's own breakpoints: toward xi_lo in Q2, Q4; explicit 'xibreaks' honoured);
         u = -1 + sinh(xi)/500
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
    xi_lo, xi_hi, v_lo, v_hi = (mp.mpf(q) for q in C['domain'][0][:4])
    nc = [int(q) for q in C['cells'][0]]                       # ncol[0], ncol[1], nrow[0], nrow[1]
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
    # geometry, as the solver builds it (solver.cpp main: breaks(), the quadrant's sides, make_geom): side 0 of xi runs
    # from xi(-10) toward xi_hi (Q1, Q3), side 1 toward xi_lo (Q2, Q4); side 0 of v from 1/2 toward v_hi (Q1, Q2), side 1
    # toward v_lo (Q3, Q4); explicit 'xibreaks'/'vbreaks' lines (side n b_0 .. b_(n-1), from the corner outward)
    # replace the equal division of that side
    a = mp.mpf(1) / 500
    xi0 = mp.asinh(mp.mpf(-9) / a); v0 = mp.mpf(1) / 2
    def breaks(start, end, n, key, side):
        for e in C.get(key, []):
            if int(e[0]) == side:
                b = [mp.mpf(q) for q in e[2:2 + int(e[1])]]
                assert len(b) == int(e[1]), (key, e)
                return b
        return [start + (end - start) * i / n for i in range(n + 1)]
    xb = [breaks(xi0, xi_hi, nc[0], 'xibreaks', 0), breaks(xi0, xi_lo, nc[1], 'xibreaks', 1)]
    vb2 = [breaks(v0, v_hi, nc[2], 'vbreaks', 0), breaks(v0, v_lo, nc[3], 'vbreaks', 1)]
    quads = C['quadrants'][0][0] if 'quadrants' in C else '1234'
    if nl == 0 or qi >= len(quads):
        sys.exit('no line state in this checkpoint (written at the end of a quadrant: quadrant index %d, column %d)' % (qi, col))
    q = int(quads[qi]) - 1                                     # 0: Q1 (+xi, +v), 1: Q2 (-xi, +v), 2: Q3 (+xi, -v), 3: Q4 (-xi, -v)
    sx, sv = (1 if q in (1, 3) else 0), (1 if q >= 2 else 0)
    xic = xb[sx][col]
    vb = vb2[sv]
    assert len(vb) - 1 == nl, ('rows', len(vb) - 1, nl)
    lob = [-mp.cos(mp.pi * b / pv) for b in range(pv + 1)]
    rad = sorted(mp.cos(2 * mp.pi * b / (2 * pv + 1)) for b in range(pv + 1))
    V = []
    for j in range(nl):
        t = rad if j == 0 else lob
        h = (vb[j + 1] - vb[j]) / 2                            # signed: the nodes run from the corner side outward
        V.append([mp.nstr(vb[j] + h * (t[b] + 1), 40) for b in range(nB)])
    X = [mp.nstr(mp.cos(mp.pi * k / M), 40) for k in range(NX)]
    info = 'quadrant Q%d (index %d of %s), column %d of %d, cells %d, solver seconds %.0f; config %s' % (
        q + 1, qi, quads, col, len(xb[sx]) - 1, cells, secs, cf)
    np.savez_compressed(out, G=G, v=np.array(V), x=np.array(X), xi=mp.nstr(xic, 40), info=info)
    print(info); print('xi_c =', mp.nstr(xic, 30), ' u_c =', mp.nstr(-1 + mp.sinh(xic) * a, 30))
    print('G shape', G.shape, ' max|G| per field', [float(np.abs(G[:, q, ..., 0]).max()) for q in range(4)])

if __name__ == '__main__':
    main()
