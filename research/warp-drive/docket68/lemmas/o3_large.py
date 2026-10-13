#!/usr/bin/env python3
"""o3_large.py -- item 356: the O3 row at the family's large end, re-posed as O3s was at the small end (o3_hold O3e):
the corridor survives its hold, the hold being the face standing (M-HOLD-IS-THE-FACE, 334) through the hole's life
(M-ENERGY-STAYS, 336).  O3e's own large-end paragraph left two things open, M1 there and position 2's open period;
both are now computed (m1_large, close_large).  Worked beside the interior's build (360, the board's reading (a)).
Worked in the conversation (computed with sympy, exact where marked; READ where marked; deduced where marked; not
verified by a separate session; not seated); 2026-10-13.

  Q0 (read) The words the row rests on, verbatim in the rulings file: 334, "For you — one reading to confirm or
     overrule - confirmed"; 336, "I think it is B"; 358, "Once everything that doesn't rely on SOURCE is resolved and
     green"; 360, "I agree. Option 1 please"; and O3e's own large-end paragraph, verbatim in o3_hold.py: "the large
     end's open period on position 2's face is not computed -- OPEN with M1 there".
  Q1 (computed, imported) The hold at the large end: the face stands the large hole's life, at least 2.417 N clocks,
     3.3e10 times the write's floor at the example README (close_large L3), the write running within it (write_large
     X1-X2: T_O3 data in all five languages).
  Q2 (computed, imported; READ where marked) Our face survives any hold, for the scalar wave on the plane: S6's
     identity at kappa = 1/(4M) damps every transverse derivative one e-fold per four clocks of GM/c^3 (bulk/
     stability.py S6, its large end, imported); the tangential derivative's bound is Schlue's for n >= 3 spatial
     dimensions (READ in stability S6; the plane reads four-dimensional Schwarzschild, n = 3, C3).  Figueras and
     Wiseman (READ): "Our numerical solutions indicate the RSII black holes are dynamically stable for axisymmetric
     perturbations for all radii" -- for the static family, beyond the small end's mode stability.
  Q3 (computed, imported) Position 2's face: its blueshift bounded over its open period -- at most e at its own sigma,
     at most e^(6.7e-4) on 139 (1)'s quarter at r0 = 10 ell (close_large L4) -- against the small end's e^33.6; the
     bath 72 orders below Barcelo's 0.28 E (m1p2x_large Y3).
  Q4 (deduced) The row.  O3 at the large end, for the scalar wave on the plane as O3s for Wall E's: the face standing
     from the opening through the large hole's life (334, 336), our face damped, position 2's bounded.  It rests on
     WRITE, as O3s rests on WRITEs; the record's ARRIVAL was its eq. (17) hold timed by the write (158 (2)), which 336
     gave up.

What this does not claim: gravitational perturbations beyond Figueras and Wiseman's statement for the static family;
the bulk scalar wave on their five-dimensional hole beyond S6's damping (Schlue's theorem is for Schwarzschild-
Tangherlini); the interior (O1b, O1c).

Imports o3_hold.py, close_large.py, write_large.py, m1p2x_large.py and bulk/stability.py by path.  Stdlib + sympy.
python3 o3_large.py [--selftest | --mutants]
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
O3E = "the large end's open period on position 2's face is not computed -- OPEN with M1 there"
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


def compute():
    cl = _load(os.path.join(HERE, "close_large.py"), "o3l_cl")
    l3, l4 = cl.l3(), cl.l4()
    wl = _load(os.path.join(HERE, "write_large.py"), "o3l_wl")
    w = wl.compute()
    st = _load(os.path.join(D68, "bulk", "stability.py"), "o3l_st")
    x = st.nonextremal()
    M = sp.Symbol("M", positive=True)
    kap = x["ends"]["large"]["kappa"] if not MUT.get("kappa_small") else 1 / (2 * M)
    damped = sp.simplify(x["bh"]["damp"] + x["bh"]["syms"][0]) == 0
    mx = _load(os.path.join(HERE, "m1p2x_large.py"), "o3l_mx")
    y3 = mx.y3()
    o3e = " ".join(open(os.path.join(HERE, "o3_hold.py"), encoding="utf-8").read().split())
    ratio = l3["ratio_ex"] if not MUT.get("hold_short") else 0.5
    return dict(ratio=ratio, kappa=kap, damped=damped, clocks_per_efold=sp.simplify((1 / kap) / M),
                t_o3=w["inn"][1], langs=w["langs"], blue_own=y3["blue_own"], blue_q=y3["blue_q"], margin=y3["margin"],
                o3e=(O3E in o3e))


def report(o):
    print("o3_large.py -- O3 at the large end (item 356)\n")
    print("Q1 the hold the life: %.3g writes at the example README; T_O3 met by %s" % (o["ratio"], o["t_o3"]))
    print("Q2 our face damped at kappa = %s, one e-fold per %s clocks of GM/c^3: %s" % (
        o["kappa"], o["clocks_per_efold"], o["damped"]))
    print("Q3 position 2's face: blueshift <= %.3g (own sigma), %.5g (139 (1)'s quarter); bath %d orders below 0.28 E"
          % (o["blue_own"], o["blue_q"], round(o["margin"])))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("Q0 334, 336, 358 and 360 verbatim, each inside its own item; O3e's large-end paragraph verbatim in o3_hold",
        all(" ".join(w.split()) in _item(n) for n, w in WORDS) and o["o3e"])
    add("Q1 the hold, the face standing the life, 3.3e10 writes at the example README; T_O3 met by the large end's "
        "hole in all five languages", "%.2g" % o["ratio"] == "3.3e+10" and o["t_o3"] == ["large-end-hole"]
        and all(b for _, b in o["langs"].values()))
    M = sp.Symbol("M", positive=True)
    add("Q2 our face damped at kappa = 1/(4M), one e-fold per four clocks; Figueras-Wiseman's stability READ",
        o["damped"] and sp.simplify(o["kappa"] - 1 / (4 * M)) == 0 and o["clocks_per_efold"] == 4
        and FW_STABLE.startswith("Our numerical"))
    add("Q3 position 2's face bounded: e at its own sigma, 1.0007 on 139 (1)'s quarter; the bath 72 orders below",
        "%.3g" % o["blue_own"] == "2.72" and "%.5g" % o["blue_q"] == "1.0007" and round(o["margin"]) == 72)
    return res


MUTANTS = {"kappa_small": "the large face's damping read at 1/(2M), half its clocks per e-fold (Q2)",
           "hold_short": "the hold read as ending before the write (Q1)"}


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
        MUT[kk] = True
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-12s %-66s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
