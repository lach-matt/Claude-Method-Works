#!/usr/bin/env python3
"""asym_junction.py -- item 213: the two bulks that meet at the corridor are not mirror images; position 1 contains a
geometric object position 2 does not, until the corridor is closed.  What that leaves a static corridor.  Computed and
deduced where marked; the conclusion reached by two independent routes; seated under 206; 2026-10-10.

  A1 (computed, rim_profile's traces on the exact inner columns) along every seated corridor the lapse A of the bulk
     carrying the object runs from below 1e-5 at the throat end (r = 2.00002m) to 1 - 2m/r_rim at the rim (to 1e-3; the march stops at y = 0.01): a
     factor of 4.4e4 to 8.4e4 over the sheet
  A2 (deduced; Israel's first junction condition and 'a static vacuum lapse vanishes only on a Killing horizon', both
     standard-not-READ) a STATIC sheet needs the induced metric to agree from both sides -- the lapse up to one constant
     rescaling of time.  A side without the object has no horizon, so its lapse stays bounded away from zero where ours
     falls toward it: no static sheet joins the two along a corridor that reaches the throat.  A side whose lapse does
     follow ours vanishes where ours does -- a horizon, the object's field on that side
  A3 (computed, second route: m1p2_junction J5) where the sheet crosses the horizon the near-horizon radii must agree
     from both sides, and only equal masses match: mass ratio 0 (no object on position 2's side) has no horizon to match
     at all, and every ratio but 1 fails
So, on the board's reading of 213 that 'contains' means the object's field on that side, the corridor cannot be static
while position 2 lacks the object: it is the transfer itself -- in line with o3_write W4 (ii) (the write is the opening,
non-static by construction), 160 (the corridor and the opening are the same object) and 198 (the README forms the
corridor as it comes in).  On the other reading -- the object's field reaches position 2's side during the hold, as 132's
'a black hole in and a white hole out, side views of the same corridor object' -- a static sheet needs the same field on
both sides (A3: equal mass), which, mirror images excluded by 213, is one smooth bulk (two_sided T1); the asymmetry 213
names then lives in time (ingoing at position 1, outgoing at position 2), which no static field carries either.  Either
way the asymmetry is not carried by any static configuration: what 213 asks is the dynamic transfer, where (Z) is to be
computed (B4d's evolution; CLOSE's five-dimensional ending).
What this sets aside or narrows (records, no status moves): two_sided T3 (the two bulks as flat-order mirror images) by
M's words; the static readings of the rim -- open_mouth's joint, ring_consistent's balance, two_sided's
H-CORRIDOR-IS-OUR-BRANE -- describe a corridor whose two sides carry the same field, which 213 excludes before the
closing on reading (b); in M1P2x's refuted conjunction (m1p2_junction) the member that gives way is the static class.
What this does not show: the dynamic transfer itself (not computed); the flat limit; the sheet thin.
Imports rim_profile.py (and through it corridor_shape.py) and m1p2_junction.py by path.  Stdlib + sympy.
python3 asym_junction.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = {}
M213 = ("they are not mirror images of each other. The whole need for warp travel is that position 1 contains a geometric "
        "object that is not contained at position 2. We want position 2 to contain the geometric object after the corridor "
        "is closed")


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), os.path.dirname(os.path.dirname(path))]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def a1():
    rp = _load(os.path.join(HERE, "rim_profile.py"), "aj_rim_profile")
    cs, ks, bulk = rp.shape()
    inner = rp._C["inner"]
    out = {}
    for (d, s0), rows in rp.joint().items():
        r_in, Y_in = rows[-1][0], rows[-1][1]
        R = cs.marginal(ks, bulk, d, 0.0, s0, rmax=12.0)
        r_out, Y_out = R["rows"][-1][:2]
        out[(d, s0)] = {"r_in": r_in, "A_in": inner.at(r_in, Y_in)["A"][0], "r_out": r_out,
                        "A_out": bulk.at(r_out, max(Y_out, 1e-6))["A"][0]}
    return out


def a2(lapses):
    """the matching test: a static match needs A_2 = A_1 / kappa^2 along the sheet for one constant kappa.  Side 2 without
    the object: a static lapse with no horizon -- modelled by the least case, constant (flat limit, no mass).  The test
    asks whether one kappa fits both ends of every corridor."""
    out = {}
    for k, v in lapses.items():
        A2_in, A2_out = (1.0, 1.0) if not MUT.get("side2_follows") else (v["A_in"], v["A_out"])
        k_in, k_out = v["A_in"] / A2_in, v["A_out"] / A2_out
        out[k] = abs(k_in / k_out - 1) < 1e-6                         # one constant fits both ends?
    return out


def a3():
    mj = _load(os.path.join(HERE, "m1p2_junction.py"), "aj_m1p2_junction")
    rows = mj.ode()
    Lf = [2 * math.sqrt(r[1]) for r in rows]
    Rf = [math.sqrt(r[2]) for r in rows]
    found = []
    for mu in (2.0, 1.5, 0.5, 0.1):
        for i in range(0, len(rows), 25):
            for j in range(0, len(rows), 25):
                if abs(Lf[i] - mu * Lf[j]) < 1e-2 and abs(Rf[i] - mu * Rf[j]) < 1e-2:
                    found.append((mu, i, j))
    return {"unequal_match": found}


def compute():
    lap = a1()
    return {"a1": lap, "a2": a2(lap), "a3": a3()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rulings = open(os.path.join(os.path.dirname(HERE), "M-RULINGS-2026-10-03.md")).read().replace("\n    ", " ")
    add("A0 M's 213 verbatim in the rulings file", M213 in rulings)
    lap = d["a1"]
    add("A1 along every seated corridor the lapse runs from below 1e-5 at the throat end to exactly 1 - 2m/r_rim at the rim "
        "(to 1e-3: the march stops at y = 0.01; a factor above 4e4)", len(lap) >= 3 and all(v["A_in"] < 1e-5 and abs(v["A_out"] - (1 - 2 / v["r_out"])) < 1e-3
                                                     and v["A_out"] / v["A_in"] > 4e4 for v in lap.values()))
    add("A2 no single time rescaling makes a horizonless side's lapse follow ours along any seated corridor: no static "
        "sheet joins the bulk with the object to a bulk without it", not any(d["a2"].values()))
    add("A3 second route (m1p2_junction J5): no unequal mass ratio (2, 1.5, 0.5, 0.1) matches both near-horizon radii",
        not d["a3"]["unequal_match"])
    return res


MUTANTS = {"side2_follows": "position 2's side given our lapse profile (the object's field on both sides)"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-14s %-72s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("asym_junction.py -- the corridor between a bulk with the object and one without (item 213)\n")
    for k, v in sorted(d["a1"].items()):
        print("A1 member %s: lapse %.3e at r = %.6f .. %.4f at the rim r = %.3f (ratio %.1e)"
              % (k, v["A_in"], v["r_in"], v["A_out"], v["r_out"], v["A_out"] / v["A_in"]))
    print("A2 a static match exists:", d["a2"])
    print("A3 unequal mass ratios that match:", d["a3"]["unequal_match"] or "none")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
