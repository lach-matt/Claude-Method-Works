#!/usr/bin/env python3
"""area_law5.py -- item 251, second step: clause (H)'s area law for the localized five-dimensional hole.  Clause (H) as
seated: "the throat holds exactly the README: 4 pi r0^2 = N x 2hG ln2/(pi c^3), 4 ln2 Planck areas per bit" -- the
four-dimensional Bekenstein-Hawking count, which with r0 = 2GE/c^4 gives clause (G)'s E = sqrt(N h c^5 ln2/(8 pi^2 G)).
For the hole of item 251 (localized_hole.py) the count can be read two ways; both are computed.  Worked in the
conversation (computed, exact where marked; not verified by a separate session; not seated); 2026-10-11.

  A1 (computed, exact) Reading 5D: the hole's own horizon holds the README by the five-dimensional Bekenstein-Hawking
     count, N ln2 = A5 / (4 l5^3), l5^3 = hbar G5 / c^3, A5 the horizon's 3-sphere area -- 2 pi^2 r_h^3 over both sides
     of the plane, pi^2 r_h^3 over one (the plane's mirror identifies the sides).  Then r_h = (2 N ln2 / pi^2)^(1/3) l5
     (both sides) or (4 N ln2 / pi^2)^(1/3) l5 (one side): fixed by N alone in the bulk's own Planck units, as the
     theorem's head asks of the corridor -- in SI it depends on ell through G5 = G ell.  With r_h^2 = 8 G5 M / 3 pi c^2,
     E = M c^2 = (3 pi / 8) (r_h / l5)^2 (hbar^2 c^4 / G5)^(1/3): E grows as N^(2/3) and falls as ell^(-1/3).
  A2 (computed, exact) Reading 4D on the plane: the plane's throat 2-sphere holds it, 4 pi r_h^2 = N A_bit, so r_h = r0
     and E = 3 pi c^4 r0^2 / (8 G ell), proportional to N / ell.  This is the four-dimensional count applied to a
     five-dimensional hole; it is not the hole's entropy.
  A3 (computed) The example README (N = 2,742,570,311,524,972), against the record's E = 2.4059e16 J: reading 5D, at
     ell = 13.964 um, r_h = 1.120e-20 m (both sides) or 1.411e-20 m (one side), E = 1.281e9 J or 2.033e9 J -- about
     1e-7 of the record's -- temperature 3.2e16 or 2.6e16 K; r_h / l5 = 7.3e4 or 9.2e4 at every ell (semiclassical), and
     r_h / ell = 8e-16 (the flat limit holds better than in step 1).  Reading 4D: E = 1.6e-6 J.
  A4 (deduced, standard) Far from the hole, r >> ell, the plane recovers four-dimensional gravity (Randall-Sundrum):
     there it reads a 1/r pull with the hole's mass, 2GM/c^2 = 2GE/c^4 for A1's E.  The 1/r tail D2 found missing at
     r << ell is the plane's reading at r >> ell.

What this does not show.
  - Which reading M takes (A1 or A2), and on A1, one side or both.
  - The ripple: clause (G)'s E, m and r0, the capacity bounds, the README-matched copy (copy_p2), T3's ledger, the hold
    -- each re-read once M fixes the count.

Imports p2_gravity.py by path.  Stdlib + sympy.  python3 area_law5.py [--selftest | --mutants]
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
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
N_EX = 2742570311524972
M251 = "Localized hole, README only"


def _pg():
    spec = importlib.util.spec_from_file_location("al_pg", os.path.join(HERE, "p2_gravity.py"))
    PG = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(PG)
    return PG


def symbolic():
    N, G5, hb, c, rh = sp.symbols("N G5 hbar c r_h", positive=True)
    l5 = (hb * G5 / c ** 3) ** sp.Rational(1, 3)
    out = {}
    for side, fac in (("both", 2 * sp.pi ** 2), ("one", sp.pi ** 2)):
        if MUT.get("area_4d"):
            fac = 4 * sp.pi
        sol = sp.solve(sp.Eq(N * sp.log(2), fac * rh ** 3 / (4 * l5 ** 3)), rh)
        r = [s for s in sol if s.is_positive][0] if sol else None
        ratio = sp.simplify(r / l5)
        E = sp.simplify(3 * sp.pi * c ** 4 * r ** 2 / (8 * G5))
        out[side] = dict(rh=r, ratio=ratio, E=E, exps=(sp.degree(sp.simplify(E ** 3), N) if E else None))
    return out


def numbers():
    PG = _pg()
    G, c, hbar, kB, h = PG.G, PG.C, PG.HBAR, 1.380649e-23, PG.H
    L2 = math.log(2)
    A_bit = 2 * h * G * L2 / (math.pi * c ** 3)
    r0 = math.sqrt(N_EX * A_bit / (4 * math.pi))
    E4 = r0 * c ** 4 / (2 * G)
    rows = {}
    for ell in (PG.ELL_MAX, 1e-6, 1e-9):
        G5 = G * ell
        l5 = (hbar * G5 / c ** 3) ** (1 / 3)
        row = {}
        for side, fac in (("both", 2 * math.pi ** 2), ("one", math.pi ** 2)):
            rh = (4 * G5 * hbar * N_EX * L2 / (fac * c ** 3)) ** (1 / 3)
            M = 3 * math.pi * c ** 2 * rh ** 2 / (8 * G5)
            row[side] = dict(rh=rh, E=M * c ** 2, T=hbar * c / (2 * math.pi * kB * rh), over_l5=rh / l5, over_ell=rh / ell)
        row["4d"] = dict(E=3 * math.pi * c ** 4 * r0 ** 2 / (8 * G5))
        rows[ell] = row
    return dict(r0=r0, E4=E4, rows=rows, ell_max=PG.ELL_MAX)


def compute():
    return dict(sym=symbolic(), num=numbers())


def report(o):
    print("area_law5.py -- clause (H)'s count for the localized 5D hole (item 251, step 2)\n")
    for side, s in o["sym"].items():
        print("A1 reading 5D, %s side(s): r_h / l5 = %s; E = %s" % (side, s["ratio"], s["E"]))
    n = o["num"]
    print("A3 the record (4D): r0 = %.4e m, E = %.4e J" % (n["r0"], n["E4"]))
    for ell, row in n["rows"].items():
        for side in ("both", "one"):
            x = row[side]
            print("   ell %.3e  5D %-4s r_h %.3e m  E %.4e J (%.1e of 4D)  T %.2e K  r_h/l5 %.1e  r_h/ell %.1e" % (
                ell, side, x["rh"], x["E"], x["E"] / n["E4"], x["T"], x["over_l5"], x["over_ell"]))
        print("   ell %.3e  4D on the plane: E %.4e J" % (ell, row["4d"]["E"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("A0 M's item-251 words verbatim in the rulings file", M251 in rul)
    s = o["sym"]
    N = sp.symbols("N", positive=True)
    ok = sp.simplify(s["both"]["ratio"] - (2 * N * sp.log(2) / sp.pi ** 2) ** sp.Rational(1, 3)) == 0
    ok &= sp.simplify(s["one"]["ratio"] - (4 * N * sp.log(2) / sp.pi ** 2) ** sp.Rational(1, 3)) == 0
    ok &= s["both"]["exps"] == 2
    add("A1 reading 5D: r_h = (2 N ln2/pi^2)^(1/3) l5 (both sides), (4 N ln2/pi^2)^(1/3) l5 (one side) -- fixed by N in "
        "the bulk's Planck units; E grows as N^(2/3)", ok)
    n = o["num"]
    x = n["rows"][n["ell_max"]]
    ok = "%.3e" % x["both"]["rh"] == "1.120e-20" and "%.3e" % x["one"]["rh"] == "1.411e-20"
    ok &= "%.3e" % x["both"]["E"] == "1.281e+09" and "%.3e" % x["one"]["E"] == "2.033e+09"
    ok &= all(abs(row["both"]["over_l5"] - x["both"]["over_l5"]) < 1e-6 * x["both"]["over_l5"] for row in n["rows"].values())
    ok &= "%.1e" % x["both"]["over_l5"] == "7.3e+04" and "%.1e" % x["4d"]["E"] == "1.6e-06"
    add("A3 example README at ell = 13.964 um: r_h 1.120e-20 m (both) / 1.411e-20 m (one), E 1.281e9 / 2.033e9 J; "
        "r_h/l5 = 7.3e4 at every ell; reading 4D E = 1.6e-6 J", ok)
    return res


MUTANTS = {"area_4d": "the 5D count taken with a 2-sphere area"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


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
        print("  mutant %-9s %-44s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
