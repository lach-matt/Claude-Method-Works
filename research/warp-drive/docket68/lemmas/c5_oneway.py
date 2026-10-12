#!/usr/bin/env python3
"""c5_oneway.py -- item 282: claim C5 (O1b/O1c at the small end, and the hold against the hole's temperature)
re-posed on the glued one-way object.  C5 as verified (hold_small.py, items 262, 267) is kept as written with its
item-281 note; this is its one-way form, after C1's and C4's.  Worked in the conversation (computed with sympy, exact
where marked; READ where marked through the instruments imported; deduced where marked; not verified by a separate
session; not seated); 2026-10-12.

  U0 (read) M's item-282 words, verbatim in the rulings file.
  U1 (computed, exact; hold_small L5, i_oneway I2) L1 re-posed: the passage is the README's route on the object --
     our black-hole face, our future interior, the bounce, position 2's past interior and white-hole face
     (c1_oneway K3) -- not a crossing "as information across the bridge's slice".  Any radial fall from the horizon
     reaches the quantum region in r_h/(c (1 + E~)) of proper time, E~ the specific energy -- at most one clock --
     hold_small's own tau and i_oneway's closed form agreeing; the README emerges through position 2's interior in as
     long again.  The interior's r = 0, admitted by item 259 as the classical interior outside the passage, is where
     the bounce's quantum region stands (273): the passage runs through it, paired per ray by the README (b_bounce Q5).
  U2 (computed, exact; kept, hold_small L2) The capture radius for the plane's fields: photon sphere at sqrt2 r_h,
     critical impact parameter 2 r_h, cross-section 4 pi r_h^2 -- outside the hole, unchanged.
  U3 (estimate, kept; hold_small L3/L5 with the C5 verifier's figures) The hole radiates mainly into the plane's own
     fields, greybody 0.93, the bulk graviton 0.6% of the power; its life 3.2e-14 s, 8.57e14 clocks.  On the one-way
     object this emission is negative energy going in at our face and positive energy leaving from outside it --
     nothing exits the face (item 277's check), so it is not a reverse passage.
  U4 (computed; kept, hold_small L4 against write_small S3) The hold is the write: the hole outlives the write's floor,
     66,980 clocks, 1.28e10-fold (i_oneway I5: 3.9e-11 of E lost over the floor), on reading (i) of items 264 and 267.
  U5 (deduced) The C5 verifier's qualification (5), "the most serious" -- the lifetime is an evaporating,
     collapse-formed hole's with no second exterior, while the eternal hole carrying the bridge loses no mass, so L1's
     bridge and L3/L4's life described different spacetimes -- resolves on the one-way object: it opens (270 (c)), so
     it is formed and evaporates, and the same formed hole carries the passage, through its interior and the bounce,
     with no second exterior of the eternal kind.  The lifetime and the passage now describe one spacetime.
  U6 (the cypher NOT-RUN, stated) U1-U5 re-post a construction and its figures; the object's causal order is
     c1_oneway K6's run.

What this does not show.
  - The quantum region's duration and the order-one coefficient of any bounce time (b_bounce Q3 is the two-way
    object's; item 277).
  - Species beyond the Standard Model (H-SPECIES-FINITE), as in hold_small.

Imports hold_small.py, i_oneway.py and c1_oneway.py by path.  Stdlib + sympy.  python3 c5_oneway.py [--selftest |
--mutants]
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
    saved = list(sys.path)
    sys.path[:0] = [HERE]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def hold():
    H = _load("hold_small.py", "c5o_hold")
    o = H.compute()
    res = {n.split()[0]: ok for n, ok in H.checks(o)}
    l5 = H.l5_checks()
    tau = l5["tau"]
    rh, Et = sorted(tau.free_symbols, key=str)[::-1] if len(tau.free_symbols) == 2 else (None, None)
    life_clocks = l5["life_clocks"]
    if MUT.get("eternal"):
        life_clocks = float("inf")                         # the mutant reads the hole as eternal, losing no mass
    return dict(checks=res, tau=tau, life=l5["life"], life_clocks=life_clocks, over=life_clocks / 66980)


def crossing_agrees(h):
    IO = _load("i_oneway.py", "c5o_io")
    cr = IO.crossing()
    syms = {s.name: s for s in h["tau"].free_symbols}
    rh, Et = syms.get("r_h"), syms.get("E_t")
    eps = sp.Symbol("epsilon", nonnegative=True)
    rh2 = sp.Symbol("r_h", positive=True)
    same = sp.simplify(h["tau"].subs({rh: rh2, Et: eps}) - rh2 / (1 + eps)) == 0 if rh is not None else False
    return dict(same=same, closed=cr["closed"])


def route():
    C1 = _load("c1_oneway.py", "c5o_c1")
    if MUT.get("slice_passage"):
        C1.MUT["slice_route"] = True                       # the mutant restores the slice's join of the exteriors
    res = {n.split()[0]: ok for n, ok in C1.checks(C1.compute())}
    C1.MUT.clear()
    return dict(K3=res["K3"], K4=res["K4"])


def compute():
    h = hold()
    return dict(h=h, x=crossing_agrees(h), rt=route())


def report(o):
    h = o["h"]
    print("c5_oneway.py -- claim C5 re-posed on the one-way object (item 282)\n")
    print("U1 hold_small's tau %s agrees with i_oneway's r_h/(1 + eps): %s; the route (c1_oneway K3): %s" % (
        h["tau"], o["x"]["same"], o["rt"]["K3"]))
    print("U2-U4 hold_small's own checks %s" % h["checks"])
    print("U3/U4 life %.3g s = %.3g clocks; the write's floor outlived %.3g-fold" % (h["life"], h["life_clocks"],
                                                                                    h["over"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("U0 M's item-282 words verbatim in the rulings file", M282 in rul)
    h = o["h"]
    add("U1 the fall to the quantum region takes r_h/(c (1 + E~)), hold_small and i_oneway agreeing; the passage is the "
        "route through the bounce (c1_oneway K3)", o["x"]["same"] and o["x"]["closed"] and o["rt"]["K3"])
    add("U2 the capture cross-section 4 pi r_h^2 (hold_small L2)", h["checks"].get("L2", False))
    ok = h["checks"].get("L3/L4", False) and h["checks"].get("L5", False) and "%.3g" % h["life_clocks"] == "8.57e+14"
    add("U3 the life 3.2e-14 s, 8.57e14 clocks, greybody 0.93, bulk 0.6% (hold_small L3/L5)", ok)
    add("U4 the hole outlives the write's floor 1.28e10-fold (hold_small L4)",
        h["checks"].get("L3/L4", False) and "%.3g" % h["over"] == "1.28e+10")
    add("U5 the object's regularity outside, where the life is computed (c1_oneway K4)", o["rt"]["K4"])
    return res


MUTANTS = {"eternal": "the hole read as eternal, losing no mass",
           "slice_passage": "the passage restored to the slice's join of the exteriors"}


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
        print("  mutant %-14s %-56s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
