#!/usr/bin/env python3
"""c7_oneway.py -- item 282: claim C7 (the chain's rows that rested on M1 alone, re-read at the small end) re-posed on
the glued one-way object.  C7 as verified (rows_small.py, items 263, 271) is kept as written with its item-281 note;
this is its one-way form, after C1's, C4's and C5's.  Worked in the conversation (computed with sympy, exact where
marked; STRUCTURAL where marked; deduced where marked; not verified by a separate session; not seated); 2026-10-12.

  V0 (read) M's item-282 words, verbatim in the rulings file.
  V1 (computed, exact; kept, rows_small G1s) One exact energy: E(N) = 3 pi c^4 r_h(N)^2/(8 G5), the Komar mass at
     r_h(N) (C4 N1), with the C7 verifier's figures (the example's E 5.32e-8 of the record's; T3/E3 flipping at the
     small end).  Re-posed: the README is held on the horizon's 3-sphere at r_h (C2 R1) -- the sphere where the faces lie
     -- not on "the bridge's least sphere".
  V2 (STRUCTURAL; G3s re-posed) "Both holds at least size": at the small end the hold is the horizon at r_h, on our
     face from the opening and on position 2's to its closing (c1_oneway K2), 2 pi^2 r_h^3 = 4 N ln2 l5^3.  The throat as
     the narrowest sphere of the eternal hole's t = 0 slice is dropped (282); there is no static throat (the C1 and C7
     verifiers), and r_h takes r0 = 2m's place without the relation carrying (2 G E/c^4 = 1.89e-15 r_h, kept).
  V3 (computed, exact; H2tu-s re-posed) The horizon's trace on each plane is r = r_h.  Position 2's plane reads the same
     f because the bounce's map (U, V) -> (-U, -V) is an isometry of the Kruskal form (b_bounce Q1) -- position 2's
     reading of its own side, nothing passing back -- not because the eternal solution's two exteriors are isometric.
     The 2-area reading, 7.9e14 N at the example, is kept with the verifier's qualification (a 4D-G reading).
  V4 (computed; O1b/O1c re-posed, c5_oneway U1) The passage runs through the bounce, each part of the README falling to
     the quantum region in at most one clock; the interior's r = 0 is where the quantum region stands (273), not a
     singularity admitted outside a slice.
  V5 (computed, exact; O2s kept and re-read, i_oneway I3) The horizon is not extremal, kappa = c^2/r_h.  The C7
     verifier's qualification (3) -- the exponential white-hole blueshift returning at O1a's exit, e^66980 over the
     write's floor -- is carried by inflow from position 2 onto its face, which the one-way object excludes: nothing from
     position 2's exterior meets its white-hole face.  The threat is closed by 270, not by a mitigation; the results
     that rested on kappa = 0 (stability S5b, o3_hold O3c, write_cypher W4, marked at 281) stay as marked.
  V6 (computed, exact; kept) Z1t-s, Z2r-s, B2t-s and E4r-s, outside the hole: the 5D null energy zero on the radial ray,
     the plane's traceless G^a_b = (r_h^2/r^4) diag(1, 1, -1, -1), the Weyl reading's sign and size with the verifier's
     qualifications (rows_small's own checks).
  V7 (the cypher NOT-RUN, stated) V1-V6 re-post rows and their figures; the object's causal order is c1_oneway K6's run.

What this does not show.
  - The rows resting on more than M1 (M1P2x, WRITE, ARRIVAL, CLOSE), as in rows_small.
  - The O3 row's figures re-derived without kappa = 0 (marked at 281, not re-posed here).

Imports rows_small.py, b_bounce.py, c1_oneway.py, c5_oneway.py and i_oneway.py by path.  Stdlib + sympy.
python3 c7_oneway.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M282 = "Re-pose them one-way (Recommended)"


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [HERE]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def checks_of(name, key, mut=None):
    m = _load(name, key)
    if mut:
        m.MUT[mut] = True
    try:
        return {n.split()[0]: ok for n, ok in m.checks(m.compute())}
    finally:
        m.MUT.clear()


def compute():
    rs = checks_of("rows_small.py", "c7o_rs")
    bb = checks_of("b_bounce.py", "c7o_bb")
    c1 = checks_of("c1_oneway.py", "c7o_c1", "opens_at_bifurcation" if MUT.get("faces_at_bifurcation") else None)
    c5 = checks_of("c5_oneway.py", "c7o_c5")
    io_ = checks_of("i_oneway.py", "c7o_io", "inflow_allowed" if MUT.get("inflow") else None)
    return dict(rs=rs, bb=bb, c1=c1, c5=c5, io=io_)


def report(o):
    print("c7_oneway.py -- claim C7 re-posed on the one-way object (item 282)\n")
    for k in ("rs", "bb", "c1", "c5", "io"):
        print("  %s %s" % (k, o[k]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("V0 M's item-282 words verbatim in the rulings file", M282 in rul)
    rs = o["rs"]
    add("V1 E(N) the Komar mass at r_h(N), with the C7 verifier's figures (rows_small G1s, R1)",
        rs.get("G1s") and rs.get("R1"))
    add("V2 the hold is the horizon at r_h, on both faces, V = 0 on neither (rows_small G3s/H2tu-s, c1_oneway K2)",
        rs.get("G3s/H2tu-s") and o["c1"].get("K2"))
    add("V3 position 2 reads the same f by the bounce's isometry (b_bounce Q1)", o["bb"].get("Q1"))
    add("V4 the passage through the bounce (c5_oneway U1)", o["c5"].get("U1"))
    add("V5 kappa = c^2/r_h (rows_small O2s); nothing from position 2 meets its white-hole face (i_oneway I3)",
        rs.get("O2s") and o["io"].get("I3"))
    add("V6 Z1t-s/Z2r-s and E4r-s, outside the hole (rows_small)", rs.get("Z1t-s/Z2r-s") and rs.get("E4r-s"))
    return res


MUTANTS = {"faces_at_bifurcation": "our face opened at U = V = 0 (through c1_oneway)",
           "inflow": "position 2's inflow let meet its white-hole face (through i_oneway)"}


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
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-20s %-58s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
