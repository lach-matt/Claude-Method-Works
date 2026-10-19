"""the reference-free Einstein residual max |R^a_b + 4 delta^a_b| (vacuum bulk, ell = 1)"""
import numpy as np, sys
sys.path.insert(0, "."); import p3m
from p3curv import slice_K, jets_from_slice, NAMES, JS


def einres_slice(sv, xv, J):
    (Rm), g = slice_K(sv, xv, J, ricci="mixed")
    E = Rm + 4 * np.eye(5)[None]
    return np.abs(E).reshape(len(xv), -1).max(axis=1)


if __name__ == "__main__":
    which = sys.argv[1]
    if which == "global":
        fn, Ns = sys.argv[2], int(sys.argv[3])
        G = p3m.Global(Ns, 20, -0.30); U = np.load(fn)
        jet = {"": "", "_s": "_X", "_x": "_u", "_ss": "_XX", "_sx": "_Xu", "_xx": "_uu"}
        n = G.n
        Jall = {nm + j: G.D[jet[j]] @ U[m * n:(m + 1) * n] for m, nm in enumerate(NAMES) for j in JS}
        cols = [k for k in range(len(G.x)) if G.x[k] > 1e-9]
        for i in range(0, G.Ns + 1, 3):
            sv = G.s[i]
            if abs(sv) < 1e-3 or sv > 0.97:
                continue
            idx = [i * (G.Nx + 1) + k for k in cols]
            e = einres_slice(sv, G.x[cols], {k: v[idx] for k, v in Jall.items()})
            print("s %+.3f  max|R^a_b + 4 d| = %.1e  (axis side %.1e, plane %.1e)" % (sv, e.max(), e[0], e[-1]))
    else:
        sl = np.load(which, allow_pickle=True)
        Np = sl[0][1].shape[1]
        xe, De, D2e = p3m.even_grid(Np)
        for row in sl:
            V = [np.vstack([v, np.zeros((1, Np))]) for v in row[1:4]]
            e = einres_slice(row[0], xe, jets_from_slice(V[0], V[1], V[2], De, D2e))
            print("s %+.3f  max|R^a_b + 4 d| = %.1e  by x: %s" % (row[0], e.max(), " ".join("%.0e" % v for v in e[::max(1, Np // 7)])))
