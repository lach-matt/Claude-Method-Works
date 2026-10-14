"""Shared pieces for the (s, x) formulation."""
import pickle, numpy as np, sympy as sp
from core_sy import bary_D, radau01, lobatto01, bary_interp
names = ["T", "S", "A", "B", "F"]
tags = ["", "_s", "_x", "_ss", "_xx", "_sx"]
s, x = sp.symbols("s x", real=True)
th = sp.Symbol("theta", real=True)
_raw = pickle.load(open("eqs_sx.pkl", "rb"))
E = {k: sp.sympify(eval(v, {**sp.__dict__})) for k, v in _raw["E"].items()}
PHI = sp.sympify(eval(_raw["phi"], {**sp.__dict__}))
ORDER = ["tt", "thth", "ss", "xx", "sx"]
RES = [E[k] for k in ORDER]
VARS = [sp.Symbol(n + t) for n in names for t in tags]
for e in RES:
    assert not e.atoms(sp.Derivative) and th not in e.free_symbols
def lam(exprs):
    return sp.lambdify([s, x] + VARS, exprs, "numpy", cse=True)
