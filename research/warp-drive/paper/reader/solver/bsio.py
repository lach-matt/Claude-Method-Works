"""Readers for the solver's outputs (.elem, .jets) and the element-node geometry.  Values are double-double pairs;
read_* return (hi, lo) float64 arrays, or with exact=True mpmath-free Python Fractions are not produced here (use hi+lo
for float diagnostics, or the pair for exact work)."""
import numpy as np, struct

def _vec(f, dtype, count_bytes):
    n = struct.unpack('<q', f.read(8))[0]
    return np.frombuffer(f.read(n * count_bytes), dtype=dtype, count=n * (count_bytes // np.dtype(dtype).itemsize))

def read_elem(fn):
    """returns list of dict(Nt, Ns, filled, hi, lo) with arrays shaped (5, Nt+1, Ns+1, M+1) (fields R, m, n, W, s; node
    t_a = -cos(pi a/Nt) ascending, sigma_b likewise, x_k = cos(pi k/M)) holding G = (F - F_seed)/(v - 1/2)^4"""
    out = []
    with open(fn, 'rb') as f:
        assert f.read(6) == b'BSOLE1'
        ne, NX = struct.unpack('<ii', f.read(8))
        for e in range(ne):
            nt, ns = struct.unpack('<ii', f.read(8)); nd = struct.unpack('<q', f.read(8))[0]
            n = struct.unpack('<q', f.read(8))[0]
            a = np.frombuffer(f.read(n * 16), dtype='<f8').reshape(5, nt + 1, ns + 1, NX, 2)
            out.append(dict(Nt=nt, Ns=ns, filled=nd, hi=a[..., 0].copy(), lo=a[..., 1].copy()))
    return out

def read_jets(fn):
    """per side (0: u >= -10, 1: u <= -10): list over first-row cells of (xi nodes, array (9, nA, 5, M+1, 2)): the Taylor
    coefficients c_j of G in (v - 1/2) at v = 1/2, j = 0..8 (so c_j is the coefficient of (v - 1/2)^(4+j) in F)"""
    res = []
    with open(fn, 'rb') as f:
        assert f.read(6) == b'BSOLJ1'
        nA, NX = struct.unpack('<ii', f.read(8))
        for s in range(2):
            n = struct.unpack('<q', f.read(8))[0]
            J = np.frombuffer(f.read(n * 16), dtype='<f8').reshape(-1, 9, nA, 5, NX, 2) if n else np.zeros((0, 9, nA, 5, NX, 2))
            nc = struct.unpack('<i', f.read(4))[0]
            xs = []
            for c in range(nc):
                m = struct.unpack('<q', f.read(8))[0]
                xs.append(np.frombuffer(f.read(m * 16), dtype='<f8').reshape(m, 2))
            res.append((xs, J))
    return res

def element_nodes(lo, hi, N):
    return 0.5 * (lo + hi) - 0.5 * (hi - lo) * np.cos(np.pi * np.arange(N + 1) / N)
