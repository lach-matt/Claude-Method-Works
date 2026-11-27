"""The jets on N0+ carried by an approximant against the transport hierarchy (floating diagnostics, 40-digit):
a_(4+j)(u, x) = sum_i chi_i(xi) d_v^j G_(i,1)(t, sigma(1/2), x) / j!   (kappa = 4) versus jets.cpp's a_(4+j).
usage: jetcheck.py case blocks hier.bin jmax     blocks: a .coef file (unquantized) or a tables _z.pkl (printed)"""
import sys, os, pickle, numpy as np, mpmath as mp
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import approx, bsio
sys.path.insert(0, os.environ.get('NAPP1', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'napp1')))
import rep
mp.mp.dps = 45

def cheb_derivs(n, t, jmax):
    """T_k^(j)(t) for k < n, j <= jmax (mpf)"""
    T = [[mp.mpf(0)] * n for _ in range(jmax + 1)]
    T[0][0] = mp.mpf(1)
    if n > 1:
        T[0][1] = t
        if jmax >= 1: T[1][1] = mp.mpf(1)
    for k in range(1, n - 1):
        T[0][k + 1] = 2 * t * T[0][k] - T[0][k - 1]
        for j in range(1, jmax + 1):
            T[j][k + 1] = 2 * j * T[j - 1][k] + 2 * t * T[j][k] - T[j][k - 1]
    return T

def main():
    case, src, hf, jmax = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
    L = rep.layout(case)
    if src.endswith('.pkl'):
        zs = pickle.load(open(src, 'rb'))
        get = lambda i, j, F: np.vectorize(lambda q, p=zs['%d_%d_%s' % (i, j, F)][0]: mp.mpf(int(q)) / mp.mpf(10) ** p, otypes=[object])(zs['%d_%d_%s' % (i, j, F)][1])
    else:
        C = approx.read_coef(src)
        def get(i, j, F):
            parts = C[i * len(L['v']) + j][approx.FN.index(F)]
            return np.vectorize(lambda *q: mp.mpf(0), otypes=[object])(parts[..., 0]) + sum(
                np.vectorize(lambda q: mp.mpf(float(q)), otypes=[object])(parts[..., w]) for w in range(parts.shape[-1]))
    H = bsio.read_hier(hf)
    M = H['NX'] - 1
    worst = {}
    for i, (mx, hx) in enumerate(L['xi']):
        mv, hv = L['v'][0]
        s0 = (mp.mpf(1) / 2 - mp.mpf(Fr(mv).numerator) / Fr(mv).denominator) / (mp.mpf(Fr(hv).numerator) / Fr(hv).denominator)
        a0, a1, _, _ = approx.use_box(case, i, 0)
        nodes = [n for n in H['nodes'] if a0 + 0.06 < float(n[2][0]) < a1 - 0.06]     # away from the xi-transitions
        for F_i, F in enumerate(approx.FN):
            Cb = get(i, 0, F)
            n1, n2, n3 = Cb.shape
            Ts = cheb_derivs(n2, s0, jmax)
            Hj = [np.array([[mp.fsum(Cb[a, b, k] * Ts[j][b] for b in range(n2)) for k in range(n3)] for a in range(n1)], dtype=object) for j in range(jmax + 1)]
            for nd in nodes[::4]:
                xi = sum(mp.mpf(float(q)) for q in nd[2])
                t = (xi - mp.mpf(Fr(mx).numerator) / Fr(mx).denominator) / (mp.mpf(Fr(hx).numerator) / Fr(hx).denominator)
                Tt = cheb_derivs(n1, t, 0)[0]
                for j in range(jmax + 1):
                    if 4 + j >= H['K']: continue
                    coefx = [mp.fsum(Hj[j][a, k] * Tt[a] for a in range(n1)) for k in range(n3)]
                    for kx in range(0, M + 1, 8):
                        x = mp.cos(mp.pi * kx / M)
                        Tx = cheb_derivs(n3, x, 0)[0]
                        val = mp.fsum(c * q for c, q in zip(coefx, Tx)) / (mp.factorial(j) * (mp.mpf(Fr(hv).numerator) / Fr(hv).denominator) ** j)
                        ref = sum(mp.mpf(float(q)) for q in nd[3][j, F_i, kx])
                        key = (4 + j, F)
                        w = worst.setdefault(key, [0, 0])
                        w[0] = max(w[0], abs(val - ref)); w[1] = max(w[1], abs(ref))
    for (order, F) in sorted(worst):
        d, s = worst[(order, F)]
        print('order %d %s: max |carried - hierarchy| = %.2e  (max |a| = %.2e, relative %.1e)' % (order, F, float(d), float(s), float(d / s) if s else 0))

main()
