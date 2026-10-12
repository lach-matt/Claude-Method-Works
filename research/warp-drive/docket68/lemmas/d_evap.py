#!/usr/bin/env python3
"""d_evap.py -- item 272's owed item (d): C5's "eternal versus evaporating" (item 267 (5)) re-read on the one-way bounce
object of items 270 and 273.  C5's verifier: "the lifetime is an evaporating, collapse-formed hole's, which has no
second exterior; the eternal hole that carries the bridge sits in a bath and loses no mass".  Worked in the conversation
(computed, exact where marked; estimates marked; deduced where marked; not verified by a separate session; not seated);
2026-10-12.

  D0 (read) M's item-273 words, verbatim in the rulings file.
  D1 (deduced) On the bounce the two spacetimes are no longer needed together.  Our side is the collapse-formed black
     hole -- the README forming it (115 (c); b_bounce Q5) -- which evaporates and has no second exterior of its own;
     position 2's side is reached through the quantum region (b_bounce Q1, H-BOUNCE-TO-P2), not through the eternal
     manifold.  C1's eternal bridge stays as the local model of the slice the isometry fixes (T = 0 through the throat),
     not as the global spacetime.
  D2 (computed; estimates from b_bounce Q3) The hole bounces long before it evaporates.  Its life on our side is 8.57e14
     clocks (hold_small L5: greybody 0.93, bulk 0.6%); the bounce comes at (r_h/l5)^p clocks times an order-one
     coefficient, 7.28e4 (p = 1) to 1.96e7 (p = 3/2) -- 1.2e10 to 4.4e7 times sooner.  The energy radiated before the
     bounce is t_bounce/(2 t_life): 4.2e-11 to 1.1e-8 of E -- quasi-static through the hold, as C6's S4 found for the
     write.
  D3 (computed, exact; deduced) The hold against the bounce.  On the bounce the hold runs from formation to the bounce,
     and must last at least the write's floor, 66,980 clocks = 0.921 (r_h/l5) (b_bounce Q3, exact).  At p = 3/2 the
     estimate exceeds it 293-fold; at p = 1 it exceeds it only if the order-one coefficient is at least 0.921 -- not
     fixed by the rule.  Under 158 (2), "exactly as long as the write needs", the board's reading is H-BOUNCE-AFTER-WRITE:
     the bounce comes when the write is done; at p = 1 both scale as N^(1/3), so the reading is consistent in scaling,
     its coefficient unproved.
  D4 (computed) In seconds at ell = 13.964 um: the write's floor 2.50e-24 s, the bounce 2.72e-24 to 7.33e-22 s (times
     the coefficient), the life 3.20e-14 s, position 2's white hole at most 33.6 clocks = 1.26e-27 s (c_junction J1).

What this does not show.
  - The bounce's order-one coefficient (D3) -- the 5D quantum-gravity computation Haggard and Rovelli leave open.
  - C6's S4 and C5's L4 stand on reading (i) as verified; D2-D3 are their re-reading on the bounce, not a repair.

Imports write_small.py, hold_small.py and p2_gravity.py by path.  Stdlib.  python3 d_evap.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M273 = "Quantum bounce to pos 2 (Recommended)"
N_EX = 2742570311524972


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def compute():
    H = _load("hold_small.py", "de_hold")
    l5c = H.l5_checks()
    life = l5c["life_clocks"]
    WS = _load("write_small.py", "de_ws")
    floor = WS.head_clocks()
    rl = (2 * N_EX * math.log(2) / math.pi ** 2) ** (1 / 3)
    p1, p32 = rl, rl ** 1.5
    if MUT.get("bounce_late"):
        p1, p32 = 2 * life, 3 * life                        # the mutant puts the bounce after the evaporation
    PG = _load("p2_gravity.py", "de_pg")
    l5 = (PG.HBAR * PG.G * PG.ELL_MAX / PG.C ** 3) ** (1 / 3)
    clock = rl * l5 / PG.C
    return dict(life=life, floor=floor, p1=p1, p32=p32, sooner=(life / p1, life / p32),
                radiated=(p1 / (2 * life), p32 / (2 * life)), coeff_needed=floor / rl, over_floor=p32 / floor,
                sec=dict(floor=floor * clock, p1=p1 * clock, p32=p32 * clock, life=l5c["life"], white=33.6 * clock))


def report(o):
    print("d_evap.py -- eternal versus evaporating, re-read on the bounce (item 272 (d))\n")
    print("D2 life %.3g clocks; bounce %.3g (p = 1) to %.3g (p = 3/2) clocks: %.2g to %.2g times sooner; radiated before "
          "it %.2g to %.2g of E" % (o["life"], o["p1"], o["p32"], o["sooner"][0], o["sooner"][1], o["radiated"][0],
                                    o["radiated"][1]))
    print("D3 the write's floor %.0f clocks = %.4f (r_h/l5); at p = 3/2 the bounce exceeds it %.0f-fold" % (
        o["floor"], o["coeff_needed"], o["over_floor"]))
    s = o["sec"]
    print("D4 seconds: floor %.3g, bounce %.3g to %.3g, life %.3g, position 2's white hole at most %.3g" % (
        s["floor"], s["p1"], s["p32"], s["life"], s["white"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("D0 M's item-273 words verbatim in the rulings file", M273 in rul)
    ok = "%.3g" % o["life"] == "8.57e+14" and "%.2g" % o["sooner"][0] == "1.2e+10" and "%.2g" % o["sooner"][1] == "4.4e+07"
    ok &= "%.2g" % o["radiated"][0] == "4.2e-11" and "%.2g" % o["radiated"][1] == "1.1e-08"
    add("D2 the hole bounces 1.2e10 to 4.4e7 times sooner than it evaporates, radiating 4.2e-11 to 1.1e-8 of E first", ok)
    ok = "%.3f" % o["coeff_needed"] == "0.921" and "%.0f" % o["over_floor"] == "293"
    add("D3 the write's floor is 0.921 (r_h/l5); the p = 3/2 bounce exceeds it 293-fold; at p = 1 a coefficient >= 0.921 "
        "is needed", ok)
    s = o["sec"]
    ok = "%.3g" % s["floor"] == "2.5e-24" and "%.3g" % s["p1"] == "2.72e-24" and "%.3g" % s["p32"] == "7.33e-22"
    ok &= "%.3g" % s["life"] == "3.2e-14" and "%.3g" % s["white"] == "1.26e-27"
    add("D4 in seconds: floor 2.50e-24, bounce 2.72e-24 to 7.33e-22, life 3.20e-14, white hole <= 1.26e-27", ok)
    return res


MUTANTS = {"bounce_late": "the bounce put after the evaporation"}


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
        print("  mutant %-12s %-40s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
