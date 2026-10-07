#!/usr/bin/env python3
"""doors.py -- wall D worked as mathematics after M's rulings 139-149.

First written claiming a white-hole allowance, that "any 5D censorship theorem whose global premises hold forbids the
passage", and that only global premises remain; the verifier showed the first has no source in a nonsingular corridor,
the second is unsupported by the theorems READ, and generic-condition and smoothness premises also remain
(DOORS.md History).

READ: Friedman, Schleich & Witt, gr-qc/9305017v2 ("FSW"): p.3 Theorem 1, "If an asymptotically flat, globally hyperbolic
spacetime (M, g_ab) satisfies the averaged null energy condition, then every causal curve from J- to J+ is deformable to
gamma_0 rel J"; p.4, Lemma 2 is stated per component J_alpha of a disconnected J; p.6, a non-deformable curve unwraps
to one joining "different copies of the asymptotic region".

  K1  five-dimensional null energy on the face-to-face composite: summed tension +1 gives S_kk = lambda_RS k_y^2 >= 0
      (static.py S4) -- CONDITIONAL on H-COMPOSITE-SURFACE (the sheets coincide exactly).  Control: position 2's sheet
      alone, -1/3, reads -(1/3) lambda_RS k_y^2 < 0
  K2  along the passage (a ray tangent to the plane, k_y = 0) the surface term vanishes for EITHER sign of tension and
      the bulk gives 0: 5D averaged null energy = 0 there (UMBILIC.md U2's result again, STRUCTURAL)
  K3  FSW with plane.py P1 forces the plane's negative reading: P1's corridor is nonsingular and one-way between two
      asymptotically flat regions -- a curve of the kind FSW's Lemma 2 excludes -- so on the plane either the averaged
      null energy fails or global hyperbolicity does.  coin.py reads -0.826 E/m: the first.  The negative reading is a
      consequence of the geometry, not an accident (the extension to genuinely distinct ends is the board's, per FSW's
      Lemma 2 per component)
  K4  entanglement alone carries nothing (the no-communication theorem; standard, not READ); with unlimited shared
      entanglement a sent qubit carries at most 2 bits (superdense coding, Holevo), so an N-bit README needs >= N/2
      qubits through a causal channel between the corridor's two asymptotic regions (STRUCTURAL)
Imports static.py, positivity.py and censor.py by path.  Stdlib + sympy.  python3 doors.py [--selftest]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
EXAMPLE_N = 2742570311524972


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def compute():
    st = _load(os.path.join(HERE, "static.py"), "dr_static")
    pos = _load(os.path.join(HERE, "positivity.py"), "dr_positivity")
    cs = _load(os.path.join(HERE, "censor.py"), "dr_censor")
    coin = _load(os.path.join(D68, "copy", "coin.py"), "dr_coin")
    s4, q3, c1 = st.s4(), pos.q3(), cs.c1()
    ky = sp.Symbol("k_y", real=True)
    return {"s4_ok": s4["S_ok"], "S_total": s4["S_total"], "S_pair_alone": q3["S_pair_alone"],
            "passage_S": sp.simplify(c1["S_kk"].subs(ky, 0)), "bulk_kk": c1["bulk_kk"],
            "plane_anec": float(coin.anec_closed(1, 2)),
            "qubits_with_ent": math.ceil(EXAMPLE_N / 2), "qubits_without": EXAMPLE_N}


def report(d):
    print("doors.py -- wall D after rulings 139-149\n")
    print("K1 composite: %s (static.py S4 %s; conditional on H-COMPOSITE-SURFACE); control, position 2's sheet alone: %s"
          % (d["S_total"], d["s4_ok"], d["S_pair_alone"]))
    print("K2 along the passage (k_y = 0): surface %s, bulk %s -> 5D averaged null energy 0, for either sign"
          % (d["passage_S"], d["bulk_kk"]))
    print("K3 the plane's averaged null energy along the passage: %.6f E/m per leg (coin.py) -- the reading FSW plus P1 "
          "require" % d["plane_anec"])
    print("K4 no channel: 0 bits; with unlimited entanglement an N = %d bit README needs >= %d qubits sent causally "
          "(%d without)" % (EXAMPLE_N, d["qubits_with_ent"], d["qubits_without"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    lrs, ky = sp.Symbol("lambda_RS", positive=True), sp.Symbol("k_y", real=True)
    chk("K1: on the face-to-face composite the null energy is non-negative for every null vector", d["s4_ok"])
    chk("K1 control: position 2's sheet alone reads -(1/3) lambda_RS k_y^2, negative",
        sp.simplify(d["S_pair_alone"] + lrs * ky**2 / 3) == 0)
    chk("K2 (STRUCTURAL): along a ray tangent to the plane, surface and bulk terms both vanish",
        d["passage_S"] == 0 and d["bulk_kk"] == 0)
    chk("K3: the plane's averaged null energy along the passage is negative, as FSW with P1 requires", d["plane_anec"] < 0)
    chk("K4 (STRUCTURAL, standard bound): N/2 qubits with entanglement, N without",
        d["qubits_with_ent"] * 2 >= EXAMPLE_N and d["qubits_without"] == EXAMPLE_N)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
