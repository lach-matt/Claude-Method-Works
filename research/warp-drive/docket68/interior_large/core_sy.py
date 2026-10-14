"""Shared pieces for the (s, y) formulation: equations, nodes, differentiation."""
import pickle, numpy as np, sympy as sp
names = ["T", "S", "A", "B", "F"]
tags = ["", "_s", "_y", "_ss", "_yy", "_sy"]
s, y = sp.symbols("s y", real=True)
th = sp.Symbol("theta", real=True)
_raw = pickle.load(open("eqs_sy.pkl", "rb"))
E = {k: sp.sympify(eval(v, {**sp.__dict__})) for k, v in _raw["E"].items()}
PHI = sp.sympify(eval(_raw["phi"], {**sp.__dict__}))
ORDER = ["tt", "thth", "ss", "yy", "sy"]          # equation e is solved for field e: T, S, A, B, F
RES = [E[k] for k in ORDER]
VARS = [sp.Symbol(n + t) for n in names for t in tags]
for e in RES:
    assert not e.atoms(sp.Derivative) and th not in e.free_symbols

def lam(exprs):
    return sp.lambdify([s, y] + VARS, exprs, "numpy", cse=True)

def bary_D(xn):
    """differentiation matrix on arbitrary distinct nodes (barycentric)"""
    n = len(xn); w = np.array([1 / np.prod([xn[j] - xn[k] for k in range(n) if k != j]) for j in range(n)])
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                D[i, j] = (w[j] / w[i]) / (xn[i] - xn[j])
        D[i, i] = -D[i].sum()
    return D

def radau01(N):
    """Chebyshev-Gauss-Radau nodes on [0, 1], including 1 and excluding 0, ascending"""
    xc = np.cos(2 * np.pi * np.arange(N + 1) / (2 * N + 1))
    return np.sort((1 + xc) / 2)

def lobatto01(N):
    return np.sort((1 - np.cos(np.pi * np.arange(N + 1) / N)) / 2)

def bary_interp(xn, vals, xt):
    """barycentric interpolation of nodal values (along axis 0) to targets xt"""
    n = len(xn); w = np.array([1 / np.prod([xn[j] - xn[k] for k in range(n) if k != j]) for j in range(n)])
    xt = np.atleast_1d(xt); out = []
    for t in xt:
        d = t - xn
        if np.any(np.abs(d) < 1e-15):
            out.append(vals[np.argmin(np.abs(d))]); continue
        c = w / d
        out.append(np.tensordot(c, vals, axes=(0, 0)) / c.sum())
    return np.array(out)
