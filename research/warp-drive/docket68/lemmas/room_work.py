#!/usr/bin/env python3
"""room_work.py -- item 442, phase 2: R6 and 284, the room.  R6: "the copy takes room by displacing what is there and
stays as the new whole of position 2" (284 (2)-(3), 285).  prior_art.py found no work in the literature that bears on
it beyond conservation; phase2.py named its remainder: the work of displacement inside the build's energy.  Labels:
computed, standard (the thermodynamics of a quasi-static displacement; copper's cohesive energy and atom density, as
tabulated in solid-state texts, standard-not-READ), deduced.  Worked in the conversation; not verified; not seated.

  W0 (read) M's words: 284's "Content displaces" and 285's "displacing".
  W1 (computed) The work.  Taking room V quasi-statically against an ambient pressure p costs W = p V (standard); in
     vacuum nothing.  The copy's room is the original's volume times arrival_small V7's ratio, which is 1 at every
     destination of our matter law; for the 1 cm^3 copper example, W = 0 in vacuum, 0.101 J at one atmosphere,
     101 J at a thousand.
  W2 (computed) The budget.  The build's energy is the README's E (111; ledger E3): 2.04 J for the perfect block's
     174 bits at the small end (encode_labels C5), and for the real 99.99 % piece's ~1.3e21 bits, E(N) by the same
     law (computed here).
  W3 (computed) Inside solid matter.  Displacing a solid takes at least its cohesive energy: copper's 3.49 eV per atom
     at 8.49e28 atoms per m^3 is 4.75e10 J/m^3 (standard), 4.75e4 J per cm^3.
  W4 (deduced) R6 proved realizable: in vacuum, in a gas and in a liquid at ordinary pressure the displacement fits
     inside the perfect block's E with room to spare (0.101 J of 2.04 J at one atmosphere).  A finding, recorded: a
     landing site inside solid matter asks 4.75e4 J per cm^3, more than the perfect block's README carries, though not
     more than the real piece's.  "Stays" asks nothing further: once the room is taken, the new whole is static and
     no work holds it.

python3 room_work.py [--selftest | --mutants]
"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ("Content displaces", "displacing")
ATM = 101325.0                                   # Pa, standard
EV = 1.602176634e-19                             # J, SI exact
CU_COH_EV, CU_N_M3 = 3.49, 8.49e28               # standard (solid-state tables): cohesive energy per atom, density
V_CM3 = 1e-6                                     # the example's volume, m^3


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def work_fluid(p, V=V_CM3, ratio=1.0):
    return (2.0 if "double" in MUT else 1.0) * p * V * ratio


def work_solid(V=V_CM3):
    return CU_COH_EV * EV * CU_N_M3 * V


def budget():
    el = _load(os.path.join(HERE, "encode_labels.py"), "rw_el")
    n_perfect = len(el.copper_block()[1])
    e_perfect = el.e_small(n_perfect)
    n_real = 1.3e21
    e_real = el.e_small(n_real)
    if "no_budget" in MUT:
        e_perfect = 0.01
    return n_perfect, e_perfect, n_real, e_real


def report():
    print("W0 M's words:", words())
    print("W1 W = p V: vacuum %.3g J, 1 atm %.4g J, 1000 atm %.4g J" % (work_fluid(0), work_fluid(ATM),
                                                                       work_fluid(1000 * ATM)))
    n1, e1, n2, e2 = budget()
    print("W2 the budget: perfect block %d bits, E = %.3g J; real piece %.2g bits, E = %.3g J" % (n1, e1, n2, e2))
    print("W3 inside copper: %.3g J per cm^3" % work_solid())
    print("W4 fits in vacuum, gas and liquid at ordinary pressure (%.3f of E at 1 atm); inside a solid: perfect block "
          "%s, real piece %s" % (work_fluid(ATM) / e1, work_solid() <= e1, work_solid() <= e2))


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("W0 words: %s" % r)
    r = work_fluid(0) == 0 and abs(work_fluid(ATM) - 0.101325) < 1e-9; ok.append(r)
    say("W1 W = p V (0 in vacuum, 0.101 J at 1 atm): %s" % r)
    n1, e1, n2, e2 = budget()
    r = abs(e1 - 2.04) < 0.01 and e2 > 1e6; ok.append(r); say("W2 the budget (2.04 J; the real piece's): %s" % r)
    r = abs(work_solid() - 4.75e4) / 4.75e4 < 0.01; ok.append(r); say("W3 copper's cohesive work 4.75e4 J: %s" % r)
    r = work_fluid(ATM) < e1 and work_solid() > e1 and work_solid() < e2; ok.append(r)
    say("W4 fits in fluids, not inside a solid for the perfect block, inside for the real piece: %s" % r)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    for m in ("double", "no_budget"):
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-10s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/2 caught" % caught)
    return caught == 2


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
