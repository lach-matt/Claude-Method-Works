"""Shared pieces for FW's RSII problem in (s, x).  The environment variable PROB (default "fw") names the problem:
eqs_<PROB>.pkl is loaded, so gen_eqs_cm.py's AdS4 C-metric (item 367 step 3) runs through the same code."""
import pickle, os, numpy as np, sympy as sp
from core_sy import bary_D, radau01, lobatto01, bary_interp
names = ["T", "S", "A", "B", "F"]
tags = ["", "_s", "_x", "_ss", "_xx", "_sx"]
s, x = sp.symbols("s x", real=True)
bt = sp.Symbol("bt", positive=True)
th = sp.Symbol("theta", real=True)
PROB = os.environ.get("PROB", "fw")
_raw = pickle.load(open("eqs_%s.pkl" % PROB, "rb"))
ev = lambda v: sp.sympify(eval(v, {**sp.__dict__}))
E = {k: ev(v) for k, v in _raw["E"].items()}
PHI = ev(_raw["phi"]); BC = {k: ev(v) for k, v in _raw["bc"].items()}
ORDER = ["tt", "thth", "ss", "xx", "sx"]
RES = [E[k] for k in ORDER]
BCORDER = ["Ktt", "Kthth", "Kss", "xix"]       # brane rows for T, S, A, B; F = 0 for F
BCS = [BC[k] for k in BCORDER]
VARS = [sp.Symbol(n + t) for n in names for t in tags]
for e in RES + BCS:
    assert not e.atoms(sp.Derivative) and th not in e.free_symbols
def lam(exprs):
    return sp.lambdify([s, x, bt] + VARS, exprs, "numpy", cse=True)

def static_file(b, Ns, Nx):
    """the static solution's file: fw_bt<b>_<Ns>_<Nx>.npy for FW, <PROB>_e<b>_<Ns>_<Nx>.npy otherwise"""
    return "fw_bt%g_%d_%d.npy" % (b, Ns, Nx) if PROB == "fw" else "%s_e%g_%d_%d.npy" % (PROB, b, Ns, Nx)
if "metric" in _raw:
    _gm = sp.lambdify([s, x, bt] + [sp.Symbol(n) for n in names], [ev(_raw["metric"][k]) for k in
                                                                       ("gss", "gsx", "gxx")], "numpy", cse=True)
def metric_sx(sv, xv, b, Xg):
    """g_ss, g_sx, g_xx at nodes xv from the fields Xg (5 rows)"""
    if "metric" in _raw:
        return [np.asarray(v, dtype=float) * np.ones(len(xv)) for v in _gm(sv, xv, b, *Xg)]
    f = 1 - sv; Dl = 1 / b + (1 - xv ** 2) / f; g = 2 - xv ** 2
    return (Xg[2] / (f ** 4 * sv) / Dl ** 2, xv * Xg[4] / (2 * f ** 3) / Dl ** 2, 4 * Xg[3] / (f ** 2 * g) / Dl ** 2)
