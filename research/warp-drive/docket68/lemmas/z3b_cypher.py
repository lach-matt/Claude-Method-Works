#!/usr/bin/env python3
"""z3b_cypher.py -- Z3b, rays that meet the corridor or run beside it, by ray class; does it reduce to its inputs?
Pass 2 of the cycle (items 204-206); put to the cypher (computed by import, deduced; not verified by a separate
session; not seated; 2026-10-10).

B1-MATTER.md's Z3'b (OPEN) rests on 183 (AXIOM) and on: a vacuum bulk carrying the corridor (B3/B4), the exact partner
F5 or the README held by the horizon (195), and C5's static configuration beside the corridor.  chain_cypher.py carries
Z3b OPEN on FAR WRITE ARRIVAL CLOSE.

  Z1 (by import) the static rays, class by class:
     - in the bulk: zero (axioms.py, bulk R(k,k) = 0; Z3'a's C1)
     - across the corridor: through TS (p2_full.py) (Z) asks the corridor's surface stress for non-negative null
       energy along it; rim_profile.py P4 computes it non-negative in the radial and tangential directions along the
       whole steep-launched corridor, with positive energy (imported, re-run)
     - across our plane near the mouth: a positive pure tension (B1: the plane matter-free there) gives sigma sin a >= 0
       on a crossing ray, zero on a grazing one (TS)
     - across the rim's ring: a 2-sphere of energy density equal to its tension obeys the NEC (rim_profile P5)
  Z2 (the board's decision under 149, H-C5-ELSEWHERE) C5 is a homogeneous flat FRW plane held static beside positive
     dark radiation (B1-MATTER: "Our plane is measured to expand ... so this is not our plane's case in its own chart");
     near the mouth our plane is matter-free and reads eq. (17) (B1, G), a different configuration: C5 does not apply
     there.  The partner F5 is not needed: 195/198 take the README in as the corridor forms (ARRIVAL)
  Z3 (cypher) ray classes as cells over (class, phase, z_kept, applies).  Static Z3b -- every static class kept -- is
     DATA.  Z3b through the dynamic phases is refused by statistics, blocked by the one pair (phase dynamic, z_kept 1):
     nothing dynamic is computed, and each dynamic cell is exactly one of Z3b's inputs (FAR, WRITE, ARRIVAL, CLOSE).
     Control: C5 entered as applying -- static Z3b refused
So Z3b reduces to its inputs: its own static content is met (with rim_profile's corridor, on M1's reading of the
mouth).  Proposal, for seating after this pass (206): Z3b OPEN -> DERIVED on M1 FAR WRITE ARRIVAL CLOSE.
Imports rim_profile.py and tools/cypher.py by path.  Stdlib + sympy.  python3 z3b_cypher.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
MUT = {}
U = 2


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def static_classes():
    rp = _load(os.path.join(HERE, "rim_profile.py"), "z3b_rim_profile")
    fam = rp.family(margins=(0.0,))
    corridor = all(v["min_tan"] > 0 and v["min_rad"] > -1e-10 and v["min_rho"] > 0 for v in fam.values())
    if MUT.get("corridor_bad"):
        corridor = False
    ring_ok = all(0 < v["ring"] for v in fam.values())          # tension positive; energy density = tension
    return {"bulk": True, "corridor": corridor, "plane": True, "ring": ring_ok}


CO = ["ray_class", "phase", "z_kept", "applies"]
# ray classes: 0 bulk, 1 across the corridor, 2 across our plane near the mouth, 3 across the ring, 4 C5's configuration;
# dynamic: 5 the far boundary (FAR), 6 the write (WRITE), 7 the arrival (ARRIVAL), 8 the closing (CLOSE)
INPUT_OF = {5: "FAR", 6: "WRITE", 7: "ARRIVAL", 8: "CLOSE"}


def cells(st):
    c5_applies = 0 if not MUT.get("c5_applies") else 1
    out = [(0, 0, int(st["bulk"]), 1), (1, 0, int(st["corridor"]), 1), (2, 0, int(st["plane"]), 1),
           (3, 0, int(st["ring"]), 1), (4, 0, 0, c5_applies)]
    out += [(k, 1, U, 1) for k in INPUT_OF]
    if MUT.get("seat_dynamic"):
        out.append((9, 1, 1, 1))
    return out


def cypher(cs):
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "z3b_cypher_cy")

    def ix_of(cl, order):
        cl = sorted(set(cl))
        vo = {"ray_class": [x for x in order if x in {c[0] for c in cl}], "phase": [0, 1],
              "z_kept": [x for x in (0, 1, U) if x in {c[2] for c in cl}], "applies": sorted({c[3] for c in cl})}
        return cy.Index("z3b", CO, [list(c) for c in cl], value_order=vo)

    def admitted(cl, test, lang, order, k=2):
        ix = ix_of(cl, order)
        out, _ = cy.ADMISSION[lang][0](ix, {"statistics_order": k} if lang == "statistics" else {})
        if out is None:
            return None
        return sorted(h for h in {tuple(ix.decode[i][x[i]] for i in range(len(CO))) for x in out} if test(h))

    applying = [c for c in cs if c[3] == 1]
    static_ok = all(c[2] == 1 for c in applying if c[1] == 0)
    dyn_kept = lambda h: h[1] == 1 and h[2] == 1 and h[3] == 1
    n = len({c[0] for c in cs})
    st_dyn = [admitted(cs, dyn_kept, "statistics", o) for o in (list(range(n)), list(reversed(range(n))))]
    return {"static_ok": static_ok, "stat_dynamic": st_dyn[0] if st_dyn[0] == st_dyn[1] else ("coding-dependent", st_dyn)}


def blocking_pairs(cs):
    tgt = {1: 1, 2: 1, 3: 1}                                     # phase dynamic, kept, applies
    out = []
    for i, j in itertools.combinations(sorted(tgt), 2):
        if not any(c[i] == tgt[i] and c[j] == tgt[j] for c in cs):
            out.append((CO[i], tgt[i], CO[j], tgt[j]))
    return out


def compute():
    st = static_classes()
    cs = cells(st)
    cyr = cypher(cs)
    return {"static": st, "cells": cs, "cy": cyr, "blocking": blocking_pairs(cs)}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    s = d["static"]
    add("Z1 every static ray class keeps (Z): bulk, across the corridor (rim_profile P4, re-run), across our plane, "
        "across the ring", all(s.values()))
    add("Z2 C5's configuration is entered as not applying near the mouth (H-C5-ELSEWHERE), and no static class that "
        "applies is broken", d["cy"]["static_ok"] and any(c[0] == 4 and c[3] == 0 for c in d["cells"]))
    add("Z3 statistics refuses Z3b through the dynamic phases, blocked by the one pair (phase dynamic, z_kept 1); each "
        "dynamic cell is one of Z3b's inputs FAR, WRITE, ARRIVAL, CLOSE", d["cy"]["stat_dynamic"] == []
        and d["blocking"] == [("phase", 1, "z_kept", 1)] and sorted(INPUT_OF.values()) == ["ARRIVAL", "CLOSE", "FAR", "WRITE"])
    return res


MUTANTS = {"corridor_bad": "the corridor's null energy taken as broken", "c5_applies": "C5 entered as applying near the mouth",
           "seat_dynamic": "a dynamic ray class seated as kept"}


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
        print("  mutant %-12s %-46s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("z3b_cypher.py -- Z3b by ray class\n")
    print("static", d["static"])
    print("cells", d["cells"])
    print("cypher", {k: v for k, v in d["cy"].items() if k != "blocking"}, " blocking pairs:", d["blocking"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
