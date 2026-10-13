#!/usr/bin/env python3
"""m1p2x_large.py -- item 356: M1P2x at the family's large end, on C3's large brane hole and the glued one-way object,
as c8_level.py (claim C8, verified at 341) posed it at the small end; with H2tx, which rests on it.  Worked beside the
interior's build (360, the board's reading (a)).  Worked in the conversation (computed with sympy, exact where marked;
READ where marked; deduced where marked; not verified by a separate session; not seated); 2026-10-13.

  Y0 (read) The words the row rests on, verbatim in the rulings file: 270, "You are forgetting that the passage is
     one-way only"; 132, "the passage is one way by nature, a black hole in and a white hole out"; 275, "Coincident
     everywhere"; 276, "The passage is one-way in all aspects"; 282, "Re-pose them one-way (Recommended)"; 358, "Once
     everything that doesn't rely on SOURCE is resolved and green"; 360, "I agree. Option 1 please".
  Y1 (computed, imported) The glued object exists at the large end: the bounce's map (U, V) -> (-U, -V) is an isometry
     of the large hole's Kruskal form, Figueras and Wiseman's dr dx cross term included (m1_large M6).  Our face is the
     black-hole face (V > 0), position 2's the white-hole face (V < 0), joined through the interiors and 273's region.
  Y2 (computed, exact; imported) The junctions, end-independent: the law mu' = -[lambda] concerns tensions only.  On
     our face the interior carries our tension, so no junction; on position 2's face it rises on every reading of
     position 2's side -- 5 sigma/4 on its own plane at 139 (1)'s -sigma/4, sigma/2 as the side total S1 + 2 S2 and on
     J2's split (c8_level V3, imported); at position 2's own sigma (226's 2a-2c; 218; 219) there is none (c8_level V2).
  Y3 (computed; imported; READ where marked) The open period and the blueshift at the large end (close_large L4): at
     position 2's own sigma, Barcelo, Carballo-Rubio and Garay's short scale, (Delta u)* <~ 2 r_s (READ in c_junction
     J2), is one e-fold of 1/kappa = 2 r0/c -- the blueshift of anything hugging the face at most e = 2.72; on 139 (1)'s
     quarter, at most ln(1 + (ell/r0)^2/15) = 6.7e-4 e-folds at r0 = 10 ell -- at most 1.0007.  A blackbody bath of
     position 2 at 1e10 K onto the face's sphere over the open period, blueshifted by e, delivers 8.1e-57 J at the
     example README, 72 orders below Barcelo's 0.28 E (E = 2.41e16 J) (computed) -- the small end's (a) closed the
     same way with e^33.6.
  Y4 (computed; imported) (d) Our face stands the large hole's life, at least 3.3e10 times the write's floor at the
     example README (close_large L3, write_large X1), on reading (i), the hole standing through the write (264 (1)).
     Reading (ii), the README's compact arrival, is the large end's ARRIVAL, which rests on SOURCE.
  Y5 (computed; imported) (e) Positivity where the rays cross position 2's plane (284, 285): the side total sigma/2 =
     (2/3) lambda_RS > 0 with no matter (m1_large M8; tau_share T4), the large end's route (the README's own density
     inside r0 is at most 0.02 of sigma/4 there).
  Y6 (computed; imported) Warp order: the plane reads four-dimensional Schwarzschild with corrections O((ell/r0)^2),
     the horizon area 0.062 (ell/r0)^2 above 4 pi r0^2 -- 6.2e-4 at r0 = 10 ell (m1_large M4), where the small end's
     entered at O(r_h/ell).  Items 320-328 are end-independent; position 2's offset x+ = 2.625e-10 J/m^3 against
     sigma/4 is smaller still at the large end, where ell is smaller and sigma larger (c8_level V7's ratio at the
     example, 7.1e-63, an upper bound).
  Y7 (computed; deduced) What remains is the README's emergence within position 2's open period, and that is how the
     README comes in -- the large end's ARRIVAL, SOURCE's (358, reading (a); reported under (c), not forced).  It is
     not idle: at the small end the README crosses within 4.79 clocks (arrival_small V2, a reading on the null-dust
     model); at the large end position 2's face is open at most one e-fold (4 clocks) at its own sigma, and at most
     2.7e-3 clocks at r0 = 10 ell on 139 (1)'s quarter, falling as (ell/r0)^2 -- there the junction outweighs the
     README long before a crossing of the small end's compactness, in clocks, could complete (computed; deduced).
  Y8 (computed, imported) H2tx: position 2's face holds the README's N bits at its own bit area, its size r0,2/r0 =
     (G2/G)^(1/2) and its capacity N exactly (copy_p2 C1, the large end's by its item-338 note; 240 (b)) -- with
     226's M-P2-OWN-G and 218/219's G2 = G, r0,2 = r0.  It rests on M1P2x for position 2's side one-way.
  Y9 (deduced) The rows.  M1P2x at the large end: Y1-Y6 hold on the glued one-way object; the emergence's timing is
     ARRIVAL's -- M1P2x stays OPEN, resting on ARRIVAL, reported.  H2tx: Y8 holds; it rests on M1P2x.

Imports c8_level.py, close_large.py, m1_large.py and copy_p2.py by path.  Stdlib + sympy.
python3 m1p2x_large.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((270, "You are forgetting that the passage is one-way only"),
         (132, "the passage is one way by nature, a black hole in and a white hole out"), (275, "Coincident everywhere"),
         (276, "The passage is one-way in all aspects"), (282, "Re-pose them one-way (Recommended)"),
         (358, "Once everything that doesn't rely on SOURCE is resolved and green"), (360, "I agree. Option 1 please"))
N_EX = 2742570311524972
SIGMA_SB, C_LIGHT, L_P = 5.670374419e-8, 2.99792458e8, 1.616255e-35
_MOD = {}


def _load(name, key):
    if key in _MOD:
        return _MOD[key]
    saved = list(sys.path)
    sys.path[:0] = [HERE, D68]
    try:
        spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
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


def y1():
    return dict(isometry=_load("m1_large.py", "mx_ml").m6()["isometry"] and not MUT.get("no_glue"))


def y2():
    c8 = _load("c8_level.py", "mx_c8")
    b = c8.v2()
    j = c8.v3(b["law"])
    return dict(j=j)


def y3():
    cl = _load("close_large.py", "mx_cl")
    l4 = cl.l4()
    blue_own = math.e ** (1 if not MUT.get("open_long") else 33.6)    # the mutant: the small end's 33.6 e-folds
    blue_q = math.exp(l4["at10"]["own"])
    r0 = math.sqrt(N_EX * math.log(2) / math.pi) * L_P
    E = 459404002.42356985 * math.sqrt(N_EX)
    dt = 2 * r0 / C_LIGHT
    bath = SIGMA_SB * 1e10 ** 4 * 4 * math.pi * r0 ** 2 * dt * blue_own
    return dict(blue_own=blue_own, blue_q=blue_q, bath=bath, E=E, margin=math.log10(0.28 * E / bath), r0=r0,
                q_clocks=l4["clocks10"])


def y4():
    cl = _load("close_large.py", "mx_cl")
    l3 = cl.l3()
    return dict(ratio=l3["ratio_ex"])


def y5():
    m8 = _load("m1_large.py", "mx_ml").m8()
    return dict(side_pos=m8["share_pos"], at10=m8["at10"])


def y6():
    m4 = _load("m1_large.py", "mx_ml").m4()
    return dict(rel=m4["rel"], at10=m4["rel"] / 100)


def y8():
    cp = _load("copy_p2.py", "mx_cp")
    return dict(c1=cp.c1())


def compute():
    return dict(y1=y1(), y2=y2(), y3=y3(), y4=y4(), y5=y5(), y6=y6(), y8=y8())


def report(o):
    print("m1p2x_large.py -- M1P2x and H2tx at the large end (item 356)\n")
    print("Y1 the glued object's isometry at the large end: %s" % o["y1"]["isometry"])
    for k, v in o["y2"]["j"].items():
        print("Y2 %-24s position 2's face mu' = %s (rising %s); a junction on our face: %s" % (
            k, v["mu_prime"], v["rising"], v["ours"]))
    c = o["y3"]
    print("Y3 blueshift <= %.3g (own sigma), %.5g (139 (1)'s quarter, r0 = 10 ell); the bath at 1e10 K %.2g J, %.0f "
          "orders below 0.28 E = %.3g J" % (c["blue_own"], c["blue_q"], c["bath"], c["margin"], 0.28 * c["E"]))
    print("Y4 life/floor %.3g; Y5 side total positive %s; Y6 the horizon area's excess at r0 = 10 ell %.2g" % (
        o["y4"]["ratio"], o["y5"]["side_pos"], o["y6"]["at10"]))
    print("Y7 position 2's face on 139 (1)'s quarter open <= %.2g clocks against the small end's crossing in 4.79" % (
        c["q_clocks"]))
    c1 = o["y8"]["c1"]
    print("Y8 copy_p2 C1: capacity matched to the README, in units of N: %s" % (
        sorted({v["cap_readme"] for v in c1.values()}),))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("Y0 270, 132, 275, 276, 282, 358 and 360 verbatim, each inside its own item",
        all(" ".join(w.split()) in _item(n) for n, w in WORDS))
    add("Y1 the bounce's map an isometry of the large hole's Kruskal form (m1_large M6)", o["y1"]["isometry"])
    j = o["y2"]["j"]
    add("Y2 position 2's face's junction rises on every reading -- 5 sigma/4 on its own plane, sigma/2 as the side "
        "total and on J2's split; none on our face",
        all(v["rising"] and not v["ours"] for v in j.values())
        and {str(v["mu_prime"]) for v in j.values()} == {"5/4", "1/2"})
    c = o["y3"]
    add("Y3 the blueshift at most e at position 2's own sigma and 1.0007 on 139 (1)'s quarter; the bath 72 orders "
        "below Barcelo's 0.28 E at the example README", "%.3g" % c["blue_own"] == "2.72" and "%.5g" % c["blue_q"]
        == "1.0007" and round(c["margin"]) == 72 and "%.3g" % c["E"] == "2.41e+16")
    add("Y4 our face stands 3.3e10 writes (reading (i)); Y5 the side total positive; Y6 warp order 6.2e-4 at "
        "r0 = 10 ell", "%.2g" % o["y4"]["ratio"] == "3.3e+10" and o["y5"]["side_pos"]
        and "%.2g" % o["y6"]["at10"] == "0.00062")
    add("Y7 on 139 (1)'s quarter position 2's face is open at most 2.7e-3 clocks at r0 = 10 ell, against the small "
        "end's crossing in 4.79 clocks", "%.2g" % c["q_clocks"] == "0.0027" and c["q_clocks"] < 4.79)
    c1 = o["y8"]["c1"]
    add("Y8 copy_p2 C1 (imported): matched to the README the capacity at position 2 is N exactly at its own bit area, "
        "in every position 2", bool(c1) and all(v["cap_readme"] == 1 for v in c1.values()))
    return res


MUTANTS = {"no_glue": "the large hole's Kruskal form read without the bounce's isometry (Y1)",
           "open_long": "the small end's 33.6 e-folds carried to position 2's face at the large end (Y3)"}


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
        print("  mutant %-10s %-72s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
