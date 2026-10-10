#!/usr/bin/env python3
"""far_cypher.py -- the chain input FAR put to the cypher: is there a far boundary consistent with (Z), (G), 139 (1)
and 166?  (computed by import, deduced, READ, STRUCTURAL; the cypher classifies, it does not derive; not verified by a
separate session; not seated; 2026-10-10)

DRAFT -- measurements being taken; the claims below are filled in from the run.
Imports tools/cypher.py, lemmas/b4c_far.py, lemmas/b4d_stage7.py, lemmas/kequality_scratch/two-sided/modelc.py,
lemmas/p2_full.py, lemmas/chain_cypher.py and lemmas/forming_rim.py by path.  Stdlib + sympy + mpmath + z3 (through
b4c_far).  python3 far_cypher.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import re
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
ROOT = os.path.dirname(os.path.dirname(WD))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
_MOD = {}
_FIX = {}


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[key] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


_PATHS = {"cypher": os.path.join(ROOT, "tools", "cypher.py"), "b4c_far": os.path.join(HERE, "b4c_far.py"),
          "stage7": os.path.join(HERE, "b4d_stage7.py"),
          "modelc": os.path.join(HERE, "kequality_scratch", "two-sided", "modelc.py"),
          "p2_full": os.path.join(HERE, "p2_full.py"), "chain": os.path.join(HERE, "chain_cypher.py")}


def mod(name):
    if name not in _MOD:
        _MOD[name] = _load(_PATHS[name], "farcy_" + name)
    return _MOD[name]


# ------------------------------------------------------------------------------------------------ the cells
C = ["model", "corridor", "untrapped", "z", "g", "p139", "c166"]
U = 2                                              # not computed (a distinct code, never a guess)
NAMES = ["COL-ROUND", "COL-ELLIPSE", "COL-POWER", "COL-FIELD", "NOCOL", "BULKFIELD", "SLAB", "BRIDGE-NEG"]
MAIN = [
    # H-FAR-MODEL (b4_global.py; the board's), the join column a = 2 on our plane, round T (W = U), and every W < sqrt3 U
    (0, 1, 0, 0, 0, 0, 0),
    # H-FAR-MODEL, ellipse W >= sqrt3 U: untrapped at every ell and N (b4c_far X2 C4 z3, X4 C5)
    (1, 1, 1, 0, 0, 0, 0),
    # H-FAR-MODEL with a power-law column A = a (z/ell)^p (b4c_far X9 (d), C10 'column scans')
    (2, 1, 1, 0, 0, 0, 0),
    # H-FAR-MODEL with the on-plane conformal far field gamma = 5/4 (b4c_far X8, C9), k above k*(U)
    (3, 1, 1, 0, 0, 0, 0),
    # no column, a = 0: Poincare AdS5 with the RS plane (b4c_far X11 C12; C10 'a = 0 is AdS5'; censor5d C1)
    (4, 0, 1, 1, 1, 0, 0),
    # a = 0 with a bulk-centred conformal test field at w_c = U/2 (b4c_far X11 C12, H-FAR-FIELD-EXTENSION)
    (5, 1, 1, U, 1, 0, 0),
]
EXT = [
    # B4d stage 7: the slab between our plane and position 2's (b4d_stage7.py K1-K4); far model not built (B4D-STAGE1 D4)
    (6, 1, U, U, 0, 1, 1),
    # model C, the two-sided bridge, on its negative-P2 branch (modelc.py C6 off-convention, P2 = -1/4 of ours)
    (7, 1, U, U, 1, 1, 1),
]


def cells(which="ext"):
    cs = list(MAIN) + (list(EXT) if which == "ext" else [])
    return cs


# ------------------------------------------------------------------------------------------------ the cypher
LANGS = ("order", "algebra", "geometry", "information", "statistics")


def t_far(h):
    return tuple(h[1:]) == (1, 1, 1, 1, 1, 1)


def t_zg(h):
    return tuple(h[1:5]) == (1, 1, 1, 1)


def ask(cs, tests, model_order=None, unk_low=False, coords=None):
    """Put the index to the five languages; per test, the decoded admitted cells that pass it (None if silent)."""
    cy = mod("cypher")
    coords = coords or C
    vo = {}
    for i, name in enumerate(coords):
        present = {c[i] for c in cs}
        if name == "model":
            vo[name] = [m for m in model_order if m in present]
        else:
            vo[name] = [x for x in ([U, 0, 1] if unk_low else [0, 1, U]) if x in present]
    ix = cy.Index("far", coords, [list(c) for c in cs], value_order=vo)
    res = {}
    for lang in LANGS:
        out, _ = cy.ADMISSION[lang][0](ix, {})
        if out is None:
            res[lang] = None
            continue
        dec = {tuple(ix.decode[i][c[i]] for i in range(len(coords))) for c in out}
        res[lang] = {k: sorted(h for h in dec if t(h)) for k, t in tests.items()}
    return res


def codings(n):
    """The nominal model axis's dihedral codings: every rotation of 0..n-1 and its reverse (2n orders)."""
    base = list(range(n))
    out = []
    for k in range(n):
        rot = base[k:] + base[:k]
        out += [rot, rot[::-1]]
    return out


def sweep(cs, tests):
    models = sorted({c[0] for c in cs})
    runs = {}
    for unk_low in (False, True):
        for order in codings(len(models)):
            mo = [models[i] for i in order]
            runs[(unk_low, tuple(mo))] = ask(cs, tests, mo, unk_low)
    return runs


if __name__ == "__main__":
    t0 = time.time()
    for which in ("main", "ext"):
        runs = sweep(cells(which), {"far": t_far, "zg": t_zg})
        for key, r in list(runs.items())[:3]:
            print(which, key, {l: (None if v is None else {k: len(x) for k, x in v.items()}) for l, v in r.items()})
        for lang in LANGS:
            for tk in ("far", "zg"):
                adm = sum(1 for r in runs.values() if r[lang] and r[lang][tk])
                inv = sorted({h for r in runs.values() if r[lang] for h in r[lang][tk]})
                print("  %s %-11s %s admits %d/%d  invented models %s" % (which, lang, tk, adm, len(runs),
                                                                          sorted({NAMES[h[0]] for h in inv})))
    print("secs", time.time() - t0)
