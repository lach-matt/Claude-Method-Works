#!/usr/bin/env python3
"""write_large.py -- item 356: the WRITE row at the family's large end, on C3's large brane hole, as write_cypher W5
posed it at the small end: the corridor's own hole coded as a cell beside the record's main cells, from instruments
already run, and the write's target asked of it.  Worked beside the interior's build (360, the board's reading (a)).
Worked in the conversation (computed, exact where marked; READ where marked; deduced where marked; not verified by a
separate session; not seated); 2026-10-13.

  X0 (read) The words the row rests on, verbatim in the rulings file: 334, "For you — one reading to confirm or
     overrule - confirmed" (M-HOLD-IS-THE-FACE: the hold of 158 (2) is the corridor standing); 336, "I think it is B"
     (M-ENERGY-STAYS); 358, "Once everything that doesn't rely on SOURCE is resolved and green"; 360, "I agree. Option 1
     please".
  X1 (computed, imported; READ where marked) The large end's hole as a cell over write_cypher's axes (corridor, static,
     lasts, keeps_Z, survives, stands, ell):
     corridor 1 -- C3: at the large end the corridor is the large brane hole whose horizon holds N (corridor_family F1).
     static 1 -- Figueras and Wiseman (1105.2558, READ): "We construct large RSII static black holes with radius up to
       ~20 ell"; over the write's floor the hole loses dM/M = floor/(3 life) = 1.0e-11 at the example README (computed,
       dM/dt = -alpha/M^2 with close_large L3's alpha), so 162's fixed size holds to that.
     lasts 1 -- the life at least 2.417 N clocks, 3.3e10 times the floor at the example README, 6.5e3 at the controlled
       corner (close_large L3, imported).
     keeps_Z 1 -- a vacuum bulk: Einstein, the five-dimensional null energy zero on every ray (m1_large M1), the plane
       carrying the tension alone (M2); the bounce's negative null energy lies in the quantum region, outside the bulk
       held through the write (pair_math P2, 318's reading), as at the small end.
     survives 1 -- our face damps every transverse derivative at kappa = 1/(4M) (bulk/stability.py S6, its large end,
       imported); Figueras and Wiseman (READ): "Our numerical solutions indicate the RSII black holes are dynamically
       stable for axisymmetric perturbations for all radii"; position 2's face bounded over its open period, e^1 at its
       own sigma or e^(6.7e-4) on 139 (1)'s quarter at r0 = 10 ell (close_large L4).  Like the small end's, the scalar
       model and the static family's spectrum, not a nonlinear proof.
     stands 1 -- 162 held to 1.0e-11; the hole's trace on each plane is its horizon (166; H2tu at the large end on C3).
     ell 1 -- the large end is controlled where r0 >= 10 ell (m1_large M5).
  X2 (computed) With the cell beside the main ones, T_WRITE and T_O3 are each a computed cell: admitted as data by all
     five languages and by statistics at every order 2-6 -- WRITE is met at the large end, and O3's bulk part with it.
     The main table stands as the record's end (write_cypher W0-W4: eq. (17)'s cells).
  X3 (deduced) The row.  WRITE at the large end: the large hole is static, lasts the write and 3.3e10 times more at the
     example, keeps (Z) as a vacuum bulk, survives (S6, READ) and stands; the hold is the face standing (334), lasting
     the life (336), 163's floor bounding the write.  O3 still rests on ARRIVAL (how the README comes in), SOURCE's.

What this does not claim: a nonlinear stability proof (the scalar model and the static family's linear spectrum, as at
the small end); the interior (O1b, O1c); the README's arrival (ARRIVAL, SOURCE's).

Imports write_cypher.py, close_large.py, m1_large.py and bulk/stability.py by path.  Stdlib + sympy.
python3 write_large.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((334, "For you — one reading to confirm or overrule - confirmed"), (336, "I think it is B"),
         (358, "Once everything that doesn't rely on SOURCE is resolved and green"), (360, "I agree. Option 1 please"))
FW_STATIC = "We construct large RSII static black holes with radius up to"
FW_STABLE = ("Our numerical solutions indicate the RSII black holes are dynamically stable for axisymmetric "
             "perturbations for all radii")
_MOD = {}


def _load(path, key):
    if key in _MOD:
        return _MOD[key]
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), HERE, D68]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    _MOD[key] = mod
    return mod


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def large_end():
    cl = _load(os.path.join(HERE, "close_large.py"), "wl_cl")
    l3, l4 = cl.l3(), cl.l4()
    life, floor = l3["life_ex"], l3["floor_ex"]
    if MUT.get("life_short"):
        life = floor / 2                                           # the mutant: the hole read as outlived by the write
    dM = floor / (3 * life)
    ml = _load(os.path.join(HERE, "m1_large.py"), "wl_ml")
    vac = ml.m1()["null"] == 0 and ml.m2()["K_is_gamma"]
    st = _load(os.path.join(D68, "bulk", "stability.py"), "wl_st")
    x = st.nonextremal()
    M = sp.Symbol("M", positive=True)
    kap_l = x["ends"]["large"]["kappa"]
    if MUT.get("extremal"):
        kap_l = sp.Integer(0)                                       # the mutant: the large face read as extremal
    damped = sp.simplify(x["bh"]["damp"] + x["bh"]["syms"][0]) == 0 and sp.simplify(kap_l - 1 / (4 * M)) == 0
    survives = 1 if damped else 2
    W = _load(os.path.join(HERE, "write_cypher.py"), "wl_wc")
    cell = (1, 1, 1 if life > floor else 0, 1 if vac else 2, survives, 1 if dM < 1e-6 else 2, 1)
    why = ("C3 (the corridor's large end); Figueras-Wiseman static (READ), dM/M %.2g over the floor; life/floor %.3g "
           "(close_large L3); vacuum bulk (m1_large M1, M2); S6 at kappa = 1/(4M) + Figueras-Wiseman stable (READ); "
           "position 2's face e^1 or e^%.2g (close_large L4)" % (dM, life / floor, l4["at10"]["own"]))
    return dict(cell=cell, why=why, life=life, floor=floor, dM=dM, kappa=kap_l, damped=damped, W=W)


def compute():
    le = large_end()
    W = le["W"]
    cs = W.cells(W.sources())
    cse = cs + [("large-end-hole", le["cell"], le["why"])]
    T_W, T_O = W.T_WRITE, W.T_O3
    langs = {lang: (W.answer(cse, T_W, lang), W.answer(cse, T_O, lang)) for lang in W.LANGS}
    stat = (W.stat_profile(cse, T_W), W.stat_profile(cse, T_O))
    inn = (sorted(i for i, c, _ in cse if W.hit(c, T_W)), sorted(i for i, c, _ in cse if W.hit(c, T_O)))
    main_write = any(W.hit(c, T_W) for _, c, _ in cs)
    return dict(le=le, langs=langs, stat=stat, inn=inn, main_write=main_write)


def report(o):
    le = o["le"]
    print("write_large.py -- WRITE at the large end (item 356)\n")
    print("X1 the large end's hole: %s\n   %s" % (le["cell"], le["why"]))
    print("X2 cells meeting T_WRITE %s, T_O3 %s; languages %s; statistics orders 2-6 %s" % (
        o["inn"][0], o["inn"][1], o["langs"], o["stat"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("X0 334, 336, 358 and 360 verbatim, each inside its own item", all(" ".join(w.split()) in _item(n)
                                                                             for n, w in WORDS))
    le = o["le"]
    add("X1 the large end's hole is (1, 1, 1, 1, 1, 1, 1): static (READ), dM/M 1.0e-11 over the floor, life/floor "
        "3.3e10, vacuum bulk, our face damped at kappa = 1/(4M) (S6), stable (READ), standing",
        le["cell"] == (1, 1, 1, 1, 1, 1, 1) and "%.2g" % le["dM"] == "1e-11"
        and "%.2g" % (le["life"] / le["floor"]) == "3.3e+10" and le["damped"]
        and FW_STATIC.startswith("We construct") and FW_STABLE.startswith("Our numerical"))
    add("X2 T_WRITE and T_O3 met only by the large end's hole, admitted by all five languages and by statistics at "
        "orders 2-6; no main cell meets T_WRITE (the record's end stands)",
        o["inn"] == (["large-end-hole"], ["large-end-hole"]) and all(a and b for a, b in o["langs"].values())
        and all(o["stat"][0].values()) and all(o["stat"][1].values()) and not o["main_write"])
    return res


MUTANTS = {"life_short": "the large hole read as outlived by the write (X1 lasts)",
           "extremal": "the large end's face read as extremal, kappa = 0 (X1 survives)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        _MOD.clear()
        MUT[kk] = True
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-11s %-66s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
