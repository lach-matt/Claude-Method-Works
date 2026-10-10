#!/usr/bin/env python3
"""close_object.py -- CLOSE within one universe: does position 1's horizon end, and what does the ending still need?
Pass 2 of the cycle (items 204-206); put to the cypher (computed, deduced, READ; not verified by a separate session;
not seated; 2026-10-10).

close_cypher.py: statistics refuses "position 1's horizon ended, with (Z) kept and no partner" because nothing
computed ends position 1's horizon (the unseen pair (side 1, ends 1)); setting A1's unknown ending (one universe,
positive focusing, close_flux K2/K3) to 1 flips it.  Its F8 (Hayward, READ) left the one-universe route standing only
for a degenerate or non-outer horizon.

  O1 (M's words, verbatim, checked in the rulings file) 115 (a), on what happens to position 1's horizon at the
     closing: "It ends; energy moved" (H-P1-HORIZON-ENDS, M's).  109: "A horizon cannot exist without the object".
     132: "side views of the same corridor object".  The ending is M's word, not a deduction of the board's
  O2 (imported; deduced) warptheorem.py's O2, PROVED: the horizon is extremal (surface gravity 0) -- degenerate, so it
     is not a future OUTER trapping horizon, and Hayward's second law (READ in close_cypher F8: "Future outer trapping
     horizons have non-decreasing area form") does not bind it.  Within one universe it is no event horizon (close_flux
     K3), so the area theorem does not bind it either, and positive focusing from theta = 0 shrinks it (K2, computed).
     So the one-universe closing needs no negative null flux: F8's objection is answered
  O3 (READ, secondary; the board's reading H-MOUTH-FLUX; computed bookkeeping) the wormhole mouth-mass rule: "if a mass
     M passes through a wormhole mouth, the entrance mouth has its mass increased by M, and the exit mouth has its mass
     reduced by" M (J. Cramer, Analog/Alternate View 69, npl.washington.edu/av/altvw69.html, search excerpt -- the
     primary, Frolov and Novikov, NAMED-NOT-READ).  Applied to the plane's far zone (4D gravity beyond ell), within one
     universe: once the README's E has passed from position 1 to position 2 the mouths read (+E, -E) and the total
     stays E (computed).  Both horizons ending with E released at position 2 (115 (a), 109, 136 (2)) then needs the
     +E and -E mouths to dissolve together -- one object, one ending (132), which is what conservation demands.  Whether
     that joint ending keeps (Z) is NOT computed: in four dimensions a -E mouth needs negative energy; on the board's
     appearance reading (117/120; Z1: the plane's deficit is the bulk's pull) it may be the bulk's field read on the
     plane with the 5D null energy kept.  That is the decisive computation this pass leaves
  O4 (cypher) close_cypher's cells with the ending entered from 115 (a): (i) on O1-O2 alone, position 1's positive
     focusing ending (A1, ends 1) makes the one-universe target DATA -- all five admit it under every coding; (ii) with
     H-MOUTH-FLUX carried, the joint ending's (Z) is unknown: statistics over-reaches at order 2 and refuses at order 3,
     blocked by (side, area, z_kept) and (side, z_kept, ends_horizon) -- the block has moved from (side 1, ends 1) to
     (Z) on the joint ending.  Control: the joint ending's (Z) set kept -- admitted again.  Between universes nothing
     moves: order 3 refuses, blocked by (side, class, ends_horizon), the area theorem's ground (close_cypher F3-F4)
Proposal, for seating after this pass (206): CLOSE splits into CLOSEu -- within one universe the closing needs no
negative null flux (O2; DERIVED) -- and a new OPEN input MOUTHFLUX -- the joint ending of the (+E, -E) mouths keeps
(Z) -- with CLOSEx (between universes) keeping CLOSE's old wording.  No row turns green on it alone.
Imports close_cypher.py (and through it close_flux.py, chain_cypher.py, tools/cypher.py) and warptheorem.py's lemma
table by path.  Stdlib + sympy.  python3 close_object.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
MUT = {}
_M = {}


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, os.path.dirname(D68)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def cc():
    if not _M:
        _M["cc"] = _load(os.path.join(HERE, "close_cypher.py"), "co_close_cypher")
    return _M["cc"]


def _norm(t):
    return re.sub(r"\s+", " ", t)


# ---------------------------------------------------------------------------------------------------------- O1, O2
def words():
    t = _norm(open(os.path.join(D68, "M-RULINGS-2026-10-03.md")).read())
    q = {"115a": '"It ends; energy moved"', "109": "A horizon cannot exist without the",
         "132": "side views of the same corridor object"}
    if MUT.get("misquote"):
        q["115a"] = '"It ends; nothing moved"'
    return {k: v in t for k, v in q.items()}


def degenerate():
    src = open(os.path.join(D68, "warptheorem.py")).read()
    m = re.search(r'\("O", "O2 the horizon is extremal \(surface gravity 0\)", "(\w+)"', src)
    status = m.group(1) if m else None
    if MUT.get("o2_open"):
        status = "OPEN"
    ph = cc().physics()
    one = ph["one"]
    return {"o2": status, "shrinks": cc()._area(ph["ray"]["positive"]) == 2, "one_universe_event": one}


# ---------------------------------------------------------------------------------------------------------- O3
def mouths():
    E = sp.Symbol("E", positive=True)
    rule_exit = -1 if not MUT.get("exit_gains") else +1
    m1, m2, out = 0, 0, E                                        # README outside at position 1
    states = [(m1, m2, out)]
    m1, out = m1 + E, out - E                                     # it enters mouth 1: the entrance gains E
    states.append((m1, m2, out))
    m2, out = m2 + rule_exit * E, out + E                         # it leaves mouth 2: the exit loses E
    states.append((m1, m2, out))
    totals = [sp.simplify(a + b + c) for a, b, c in states]
    return {"final": states[-1], "conserved": all(sp.simplify(t - E) == 0 for t in totals), "E": E}


# ---------------------------------------------------------------------------------------------------------- O4
def cypher():
    c = cc()
    ph = c.physics()
    base = c.cells(ph)
    key = "A1 one universe, positive focusing (K2's surface)"
    o1 = dict(base)
    o1[key] = base[key][:5] + (1,)                               # ends: 115 (a), M's word
    o2 = dict(o1)
    zj = c.U if not MUT.get("joint_kept") else 1
    o2[key] = base[key][:3] + (zj,) + base[key][4:5] + (1,)     # H-MOUTH-FLUX: the ending is the joint ending; (Z) unknown
    ctrl = dict(o2)
    ctrl[key] = base[key][:3] + (1,) + base[key][4:5] + (1,)
    runs = {"o1": c.run_all(o1.values()), "o2": c.run_all(o2.values()), "ctrl": c.run_all(ctrl.values())}
    t1u = "T1_0"
    out = {}
    for name, r in runs.items():
        out[name] = {lang: all(v[lang] is not None and v[lang][t1u] for v in r.values()) for lang in c.LANGS}
        out[name + "_none"] = {lang: not any(v[lang] is not None and v[lang][t1u] for v in r.values()) for lang in c.LANGS}
    out["base_unseen"] = c.unseen_pairs(list(base.values()), c.T1[0])

    def blocking(cs, t, k):
        cs = list(cs)
        return [tuple(c.C[i] for i in S) for S in itertools.combinations(range(len(c.C)), k)
                if not any(all(x[i] == t[i] for i in S) for x in cs)]

    def stat(cs, t, k):
        cy = c.owners()["cy"]
        cl = sorted(set(cs))
        vo = {name: sorted({x[i] for x in cl}) for i, name in enumerate(c.C)}
        ix = cy.Index("close_object", c.C, [list(x) for x in cl], value_order=vo)
        adm, _ = cy.ADMISSION["statistics"][0](ix, {"statistics_order": k})
        return t in {tuple(ix.decode[i][x[i]] for i in range(len(c.C))) for x in adm}
    out["o2_stat2"], out["o2_stat3"] = stat(o2.values(), c.T1[0], 2), stat(o2.values(), c.T1[0], 3)
    out["o2_block3"] = blocking(o2.values(), c.T1[0], 3)
    out["btw_stat2"], out["btw_stat3"] = stat(o1.values(), c.T1[1], 2), stat(o1.values(), c.T1[1], 3)
    out["btw_block3"] = blocking(o1.values(), c.T1[1], 3)
    return out


def compute():
    return {"words": words(), "deg": degenerate(), "mouths": mouths(), "cy": cypher()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("O1 M's words verbatim in the rulings file: 115 (a) 'It ends; energy moved', 109, 132", all(d["words"].values()))
    g = d["deg"]
    add("O2 warptheorem O2 is PROVED (extremal, surface gravity 0): degenerate, so Hayward's outer-horizon law does not "
        "bind; within one universe no event horizon, and positive focusing shrinks the area (close_flux K2, K3)",
        g["o2"] == "PROVED" and g["shrinks"] and not g["one_universe_event"]["event_horizon"]
        and not g["one_universe_event"]["needs_negative"])
    mo = d["mouths"]
    E = mo["E"]
    add("O3 the mouth-mass rule within one universe: after the passage the mouths read (+E, -E), E released, total E "
        "conserved throughout", mo["conserved"] and mo["final"][0] == E and mo["final"][1] == -E and mo["final"][2] == E)
    cy = d["cy"]
    add("O4 (i) on O1-O2 alone the one-universe target is data: all five admit it under every coding", all(cy["o1"].values()))
    add("O4 (ii) with H-MOUTH-FLUX the joint ending's (Z) is unknown: statistics over-reaches at order 2 and refuses at "
        "order 3, blocked by (side, area, z_kept) and (side, z_kept, ends_horizon) -- the block has moved from "
        "(side 1, ends 1) to (Z)", (("side", 1), ("ends_horizon", 1)) in cy["base_unseen"] and cy["o2_stat2"]
        and not cy["o2_stat3"] and cy["o2_block3"] == [("side", "area", "z_kept"), ("side", "z_kept", "ends_horizon")])
    add("O4 control: the joint ending's (Z) set kept -- all five admit the target again", all(cy["ctrl"].values()))
    add("O4 between universes nothing moves: statistics over-reaches at order 2 and refuses at order 3, blocked by "
        "(side, class, ends_horizon) -- no side-1 ending between universes", cy["btw_stat2"] and not cy["btw_stat3"]
        and cy["btw_block3"] == [("side", "class", "ends_horizon")])
    return res


MUTANTS = {"misquote": "115 (a) misquoted", "o2_open": "the extremal horizon not proved (O2 OPEN)",
           "exit_gains": "the exit mouth made to gain mass", "joint_kept": "the joint ending's (Z) entered as kept"}


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
        print("  mutant %-11s %-46s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("close_object.py -- CLOSE within one universe\n")
    print("O1", d["words"], " O2", d["deg"], " O3", d["mouths"]["final"])
    for k, v in d["cy"].items():
        print("O4", k, v)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
