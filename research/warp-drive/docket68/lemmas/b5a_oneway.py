#!/usr/bin/env python3
"""b5a_oneway.py -- items 281-282: theorem row B5a (positivity for the entangled pin at coincidence, 127) re-posed
one-way.  b5_positive.py B5a read the coincident sheets through one composite junction, (4/3 - 1/3) lambda_RS -- the
auditing agent's finding (281, W4): position 2's tension entering our junction, against 276 (a).  B5a is kept as
written with its item-281 note; this is its one-way form, sheet by sheet.  Worked in the conversation (computed with
sympy, exact where marked; deduced where marked; not verified by a separate session; not seated); 2026-10-12.

  B0 (read) M's item-282 words, verbatim in the rulings file.
  B1 (computed, exact; j_readings J2) Our sheet's junction carries our stress alone (chi = 0, which 276 forces): a ray
     crossing our plane at angle a picks up (lambda_1 + rho_1) sin a + (rho_1 + p_1) cos^2 a / sin a, with lambda_1 =
     sigma > 0 and our matter's rho_1 >= 0, rho_1 + p_1 >= 0 -- positive on every ray, whatever position 2 carries.
  B2 (computed, exact; e_positive E7, item 284) Position 2's sheet carries tau of ours, received (j_readings J2), and
     its own stress, -sigma/4 plus its matter.  Where the README lands its own total is positive (E7: above sigma/4
     within 2.0e-15 m), so the share on rays crossing it there is positive for every tau in [0, 1]: tau sigma >= 0 only
     adds.  Positivity is owed there (284).
  B3 (deduced) B5'a's composite condition, (lambda_sum + rho_1 + rho_2) k_y^2 + sum (rho + p) |k_space|^2 >= 0, is the
     chi = 1 reading -- one junction both sheets act on -- and is the record of the two-way reading.  Its null-stress
     expression is direction-neutral (the auditing agent's note); what was two-way is the junction.  The one-way form of
     B5a is B1 and B2: our sheet positive alone, position 2's positive where the README lands.

What this does not show.
  - B5c's pin (no radion at coincidence): not re-read here.
  - Position 2's sheet away from the landing (not owed, 284).

Imports j_readings.py and e_positive.py by path.  Stdlib + sympy.  python3 b5a_oneway.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M282 = "Re-pose them one-way (Recommended)"


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def shares():
    sig, s, rho1 = sp.symbols("sigma s rho_1", positive=True)        # s = sin a
    c2, w1, tau = sp.symbols("c2 w_1 tau", nonnegative=True)         # c2 = cos^2 a; w1 = rho_1 + p_1; tau in [0, 1]
    S2 = sp.Symbol("S_2", real=True)                                  # position 2's own total
    chi = sp.Integer(1) if MUT.get("composite") else sp.Integer(0)    # the mutant: one junction both sheets act on
    e1 = sig + rho1 + chi * S2                                        # our junction's surface energy
    ours = e1 * s + w1 * c2 / s
    ours_free = sp.diff(ours, S2) == 0
    ours_pos = bool(ours.subs(S2, 0).is_positive) and ours_free
    S2pos = sp.Symbol("S2p", positive=True)                           # where the README lands, E7
    theirs = (tau * sig + S2pos) * s + w1 * c2 / s
    return dict(ours_free=ours_free, ours_pos=ours_pos, theirs_pos=bool(theirs.is_positive))


def compute():
    JR = _load("j_readings.py", "b5o_jr")
    j = {n.split()[0]: ok for n, ok in JR.checks(JR.compute())}
    EP = _load("e_positive.py", "b5o_ep")
    x = EP.example()
    return dict(sh=shares(), J2=j.get("J2", False), R=x["R"])


def report(o):
    print("b5a_oneway.py -- theorem row B5a re-posed one-way (items 281-282)\n")
    print("B1 our share free of position 2's stress: %s, positive: %s (j_readings J2: %s)" % (
        o["sh"]["ours_free"], o["sh"]["ours_pos"], o["J2"]))
    print("B2 position 2's share where the README lands (within %.3g m), every tau: positive %s" % (
        o["R"], o["sh"]["theirs_pos"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("B0 M's item-282 words verbatim in the rulings file", M282 in rul)
    add("B1 our sheet's share is free of position 2's stress and positive on every ray (chi = 0, j_readings J2)",
        o["sh"]["ours_free"] and o["sh"]["ours_pos"] and o["J2"])
    add("B2 position 2's share where the README lands is positive for every tau (E7: within 2.0e-15 m)",
        o["sh"]["theirs_pos"] and "%.2g" % o["R"] == "2e-15")
    return res


MUTANTS = {"composite": "one junction both sheets act on (chi = 1)"}


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
        print("  mutant %-10s %-44s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
