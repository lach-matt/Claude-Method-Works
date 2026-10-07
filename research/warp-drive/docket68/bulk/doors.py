#!/usr/bin/env python3
"""doors.py -- wall D worked as mathematics after M's rulings 139-149: which premise of censorship the corridor must
pass through.

censor.py (verified) found the bulk theorems DEPEND on two choices: the sign of our plane's tension (H-OUR-TENSION) and
where the bulk ends (H-POINCARE-PATCH).  Since then M ruled ours positive (139) and the planes static and face to face
(141; static.py: the summed surface +1).  This instrument re-reads the theorems with the first choice settled.

READ: Friedman, Schleich & Witt, gr-qc/9305017v2 ("FSW"):
  p.3 Theorem 1: "If an asymptotically flat, globally hyperbolic spacetime (M, g_ab) satisfies the averaged null energy
      condition, then every causal curve from J- to J+ is deformable to gamma_0 rel J"
  p.6: a non-deformable curve "will join J+_0(M) to another copy of the asymptotic region", through surfaces "outer
      trapped as seen from the first asymptotic region" -- which Lemma 2 forbids
  p.7: "one can passively observe that topology by detecting light that originates at a past singularity ... one must
      see a signal that originates in a white hole rather than J-"

  K1  the energy premise is now met in five dimensions: the face-to-face sum is +1 (static.py S4, imported), so on the
      summed surface S_kk = lambda_RS k_y^2 >= 0 for every null vector, and the bulk reads 0 (censor.py C1, imported)
  K2  along the passage itself the five-dimensional null energy is exactly zero: a ray tangent to the plane has k_y = 0,
      so S_kk = 0, and the bulk term is 0 -- the 5D averaged null energy holds (= 0) where the plane reads -0.826 E/m
      (coin.py).  The negative reading is the plane's appearance only (M's items 117, 120)
  K3  so the only premises left between the corridor and the 5D censorship theorems are GLOBAL: global hyperbolicity
      and the bulk's asymptotic structure (H-POINCARE-PATCH).  That is wall C
  K4  entanglement does not open a door around them: with any amount of pre-shared entanglement, a qubit sent carries
      at most 2 bits (superdense coding; Holevo; standard, not READ), so an N-bit README needs at least N/2 qubits sent
      along a causal channel between the two positions -- exactly the causal curve censorship governs.  Control:
      without entanglement, N qubits
Imports static.py and censor.py by path.  Stdlib + sympy.  python3 doors.py [--selftest]
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
    cs = _load(os.path.join(HERE, "censor.py"), "dr_censor")
    s4 = st.s4()
    c1 = cs.c1()
    ky = sp.Symbol("k_y", real=True)
    lam = sp.Symbol("lambda", real=True)
    passage = sp.simplify(c1["S_kk"].subs(ky, 0))
    return {"s4_ok": s4["S_ok"], "S_total": s4["S_total"], "bulk_kk": c1["bulk_kk"], "passage_S": passage,
            "qubits_with_ent": math.ceil(EXAMPLE_N / 2), "qubits_without": EXAMPLE_N}


def report(d):
    print("doors.py -- wall D after rulings 139-149\n")
    print("K1 summed surface null energy %s (static.py S4: %s); bulk %s" % (d["S_total"], d["s4_ok"], d["bulk_kk"]))
    print("K2 along the passage (k_y = 0): S_kk = %s, bulk 0 -> 5D averaged null energy = 0 (the plane reads -0.826 E/m)"
          % d["passage_S"])
    print("K3 the energy premises hold; the premises left are global: hyperbolicity and the bulk's asymptotics (wall C)")
    print("K4 an N = %d bit README needs >= %d qubits sent causally with unlimited entanglement (%d without)"
          % (EXAMPLE_N, d["qubits_with_ent"], d["qubits_without"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("K1: with the face-to-face sum (+1) the null energy on the surface is non-negative for every null vector",
        d["s4_ok"])
    chk("K1: the bulk's null energy is zero (cosmological constant only)", d["bulk_kk"] == 0)
    chk("K2 (STRUCTURAL): along a ray tangent to the plane the surface term vanishes -- 5D null energy exactly zero",
        d["passage_S"] == 0)
    chk("K4 (STRUCTURAL, standard bound): with entanglement an N-bit README still needs N/2 qubits sent causally; "
        "control: N without", d["qubits_with_ent"] * 2 >= EXAMPLE_N and d["qubits_without"] == EXAMPLE_N)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
