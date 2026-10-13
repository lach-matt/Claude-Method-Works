"""Shared pieces for FW's RSII problem in (s, x)."""
import pickle, numpy as np, sympy as sp
from core_sy import bary_D, radau01, lobatto01, bary_interp
names = ["T", "S", "A", "B", "F"]
tags = ["", "_s", "_x", "_ss", "_xx", "_sx"]
s, x = sp.symbols("s x", real=True)
bt = sp.Symbol("bt", positive=True)
th = sp.Symbol("theta", real=True)
_raw = pickle.load(open("eqs_fw.pkl", "rb"))
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
