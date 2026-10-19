"""the P3 s-chart metric's jets, its Kretschmann scalar on a slice, and slice geometry"""
import numpy as np
import sympy as sp
import sys
sys.path.insert(0, "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p3e")
from kretsch import kretschmann

t, s, x, th, ph = sp.symbols("t s x theta phi")
CO = [t, s, x, th, ph]
NAMES = "TABFS"
FN = {n: sp.Function(n)(s, x) for n in NAMES}
BT = 2


def metric(bt=BT):
    T, A, B, F, S = [FN[n] for n in NAMES]
    f, gx = 1 - s, 2 - x**2
    w = (bt * f / (f + bt * (1 - x**2)))**2
    g = sp.zeros(5)
    g[0, 0] = -w * s * T
    g[1, 1] = w * A / (s * f**4)
    g[2, 2] = w * 4 * B / (f**2 * gx)
    g[1, 2] = g[2, 1] = w * x * F / (2 * f**3)
    g[3, 3] = w * x**2 * gx * S / f**2
    g[4, 4] = g[3, 3] * sp.sin(th)**2
    return g


JS = ["", "_s", "_x", "_ss", "_sx", "_xx"]
SYM = {n + j: sp.Symbol(n + j) for n in NAMES for j in JS}


def to_jets(e):
    rep = {}
    for n in NAMES:
        F = FN[n]
        rep[sp.Derivative(F, s, s)] = SYM[n + "_ss"]
        rep[sp.Derivative(F, s, x)] = SYM[n + "_sx"]
        rep[sp.Derivative(F, x, s)] = SYM[n + "_sx"]
        rep[sp.Derivative(F, x, x)] = SYM[n + "_xx"]
    e = e.subs(rep)
    rep = {}
    for n in NAMES:
        F = FN[n]
        rep[sp.Derivative(F, s)] = SYM[n + "_s"]
        rep[sp.Derivative(F, x)] = SYM[n + "_x"]
    e = e.subs(rep)
    return e.subs({FN[n]: SYM[n] for n in NAMES}).subs(th, sp.pi / 2)


_F = {}
def evaluator():
    if "f" in _F:
        return _F["f"]
    g = metric()
    dG = [[[to_jets(sp.diff(g[a, b], c)) for b in range(5)] for a in range(5)] for c in CO]
    ddG = [[[[to_jets(sp.diff(g[a, b], c, e)) for b in range(5)] for a in range(5)] for e in CO] for c in CO]
    G = [[to_jets(g[a, b]) for b in range(5)] for a in range(5)]
    args = [s, x] + [SYM[n + j] for n in NAMES for j in JS]
    _F["f"] = tuple(sp.lambdify(args, M, "numpy", cse=True) for M in (G, dG, ddG))
    return _F["f"]


def bcast(arr, shape):
    return np.broadcast_to(np.asarray(arr, dtype=float), shape)


def slice_K(sv, xv, jets, ricci=False):
    """sv scalar, xv (n,), jets dict name -> (n,) arrays for the 30 jet symbols"""
    fG, fd, fdd = evaluator()
    n = len(xv)
    a = [np.full(n, sv), xv] + [jets[nm + j] for nm in NAMES for j in JS]
    G = fG(*a); dG = fd(*a); ddG = fdd(*a)
    g = np.stack([np.stack([bcast(G[i][k], (n,)) for k in range(5)], -1) for i in range(5)], -2)
    dg = np.stack([np.stack([np.stack([bcast(dG[c][i][k], (n,)) for k in range(5)], -1) for i in range(5)], -2)
                   for c in range(5)], 1)
    ddg = np.stack([np.stack([np.stack([np.stack([bcast(ddG[c][e][i][k], (n,)) for k in range(5)], -1)
                                        for i in range(5)], -2) for e in range(5)], 1) for c in range(5)], 1)
    return kretschmann(g, dg, ddg, ricci), g


def jets_from_slice(V0, V1, V2, De, D2e):
    """V0, V1, V2: (6, n) values and s-derivatives of T A B F S P at the even x nodes"""
    J = {}
    for m, nm in enumerate(NAMES):
        J[nm] = V0[m]; J[nm + "_s"] = V1[m]; J[nm + "_ss"] = V2[m]
        J[nm + "_x"] = De @ V0[m]; J[nm + "_xx"] = D2e @ V0[m]; J[nm + "_sx"] = De @ V1[m]
    return J


if __name__ == "__main__":
    # check on the reference fields T = A = B = S = 1, F = 0 against a direct sympy evaluation
    g = metric()
    sub = {FN[n]: (0 if n == "F" else 1) for n in NAMES}
    gr = g.subs(sub).doit()
    import itertools
    xs = np.array([0.3, 0.7, 0.95])
    J = {nm + j: np.zeros(3) for nm in NAMES for j in JS}
    for nm in "TABS":
        J[nm] = np.ones(3)
    K, _ = slice_K(-0.4, xs, J)
    # direct: numeric engine on the explicit reference metric
    dG = [[[sp.diff(gr[a, b], c) for b in range(5)] for a in range(5)] for c in CO]
    ddG = [[[[sp.diff(gr[a, b], c, e) for b in range(5)] for a in range(5)] for e in CO] for c in CO]
    f1 = sp.lambdify(CO, gr, "numpy"); f2 = sp.lambdify(CO, dG, "numpy"); f3 = sp.lambdify(CO, ddG, "numpy")
    pts = [(0, -0.4, xv, np.pi / 2, 0) for xv in xs]
    gg = np.array([np.array(f1(*p), float) for p in pts]); d1 = np.array([np.array(f2(*p), float) for p in pts])
    d2 = np.array([np.array(f3(*p), float) for p in pts])
    print("reference K via jets:", K, " direct:", kretschmann(gg, d1, d2))
