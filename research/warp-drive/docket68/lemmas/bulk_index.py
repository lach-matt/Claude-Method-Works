#!/usr/bin/env python3
"""bulk_index.py -- item 216: where the two cells of the everything bulk index meet (203), and how the object comes to be
contained at position 2 (213), put through the cypher (196) on exact counts (209), the index audited first (208, 211).
Computed by tools/cypher.py; worked in the conversation; seated under 206; 2026-10-10.

THE INDEX (M's own account of the transfer; every cell and coordinate from M's words):
  cells, the stages: before (213: the object at position 1, not at 2); opening (106 (b): 'horizon position 1 only as the
  corridor opens'); realized (106 (b): 'held on both horizons simultaneously'; 115 (b): position 2's horizon arises 'when
  fully realized'); closing (106 (b): 'held only at the horizon of position 2'; 115 (a): position 1's horizon 'ends;
  energy moved'); after (213: 'position 2 to contain the geometric object after the corridor is closed'; 136 (2):
  released at position 2 at the closing of the horizon; 110: 'Into position 2')
  coordinates: held_1, held_2 (the object held or contained at that position), horizon_1, horizon_2 (that position's
  horizon stands)
  I1 (computed) the audit: no key, no redundant group (index_audit); held_1 and held_2 each add nothing to telling the
     stages apart (the horizons with either one suffice), and neither can be dropped with the other.  A first design
     carried (Z) as a coordinate: it duplicated horizon_2 exactly -- (Z) is computed kept only at stages without
     position 2's horizon, and is unknown at both stages with it -- so it was dropped, and that is I5's finding
  I2 (computed; statistics, coding-free) the index is closed at order 3 (E = 0); at order 2 it admits three cells beyond
     the stages, all with the object held at both positions and fewer than both horizons -- an over-reach assembled from
     pairs, refused at order 3
  I3 (computed) WHERE THE TWO CELLS MEET: with the realized stage left out, statistics admits no cell with the object
     held at both positions (0 of 4, orders 2 and 3; blocked by (held_1, held_2), (held_1, horizon_2), (held_2,
     horizon_1), (horizon_1, horizon_2)).  The two positions share the object only in the realized stage, and no
     combination of the other stages assembles it: the meeting is that stage, M's 'the corridor builds position 2 with
     the bits in mind' (106 (b)).  Forced by those unseen pairs, which are its content
  I4 (computed) HOW THE OBJECT COMES TO BE AT POSITION 2: (a) statistics never admits the object held nowhere (orders 2
     and 3): the transfer passes through the stage where both hold it, never through one where neither does; (b) with
     the after stage left out, statistics refuses it (orders 2 and 3), blocked by (held_1, horizon_2) and (held_2,
     horizon_2): no transit stage has position 1 empty, or position 2 holding the object, with position 2's horizon
     gone.  The release -- position 2's horizon ending with the object kept (136 (2), 110) -- is a step of its own,
     not assembled from the transit.  Replacement test: every novel cell carrying (held_1 0, horizon_2 0) is refused
     alike (forced by that pair, which is its content)
  I5 (computed, the first design) (Z) is computed kept at before, opening and after, and is unknown at realized and
     closing -- exactly the stages where position 2's horizon stands (Z3b for the hold, CLOSE for the closing, both
     OPEN).  In the index (Z) is then a duplicate of horizon_2, so the cypher cannot decide it: it is the open
     computation, the dynamic transfer
  I6 (computed) the four ordinal languages, over all 16 codings: order and algebra admit 'held nowhere' under 8 of 16
     and the after stage (left out) under 4 of 16, geometry under none, information under 4 and 2 -- they move with the
     coding (an artefact), so the coding-free statistics carries the verdicts; algebra's E is 3-11, so no single added
     cell closes the index under every coding
So, through the cypher, M's account reads as four steps, none assembled from the others: held at position 1; held at
both (the meeting, where the two cells share the object); held at position 2; released at position 2 -- and the object
is never held nowhere.  Every verdict is forced by a named unseen projection (five cells; 211): what the cypher adds is
that each step is irreducible, that pairs alone over-reach, and where (Z) is uncomputed.
What this does not show: the index is M's account, not a computed geometry; it orders no times; within one universe and
between universes are not told apart (no recorded difference in the stages).
Imports tools/cypher.py and index_audit.py by path.  Stdlib.  python3 bulk_index.py [--selftest | --mutants]
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
U = "U"
C = ["held_1", "held_2", "horizon_1", "horizon_2"]
STAGES = {"before": (1, 0, 0, 0), "opening": (1, 0, 1, 0), "realized": (1, 1, 1, 1), "closing": (0, 1, 0, 1),
          "after": (0, 1, 0, 0)}
Z = {"before": 1, "opening": 1, "realized": U, "closing": U, "after": 1}
BOX = list(itertools.product([0, 1], repeat=4))
LANGS = ("order", "algebra", "geometry", "information")
WORDS = ["horizon position 1 only as the corridor opens", "the bits are held on both horizons simultaneously",
         "the bits are then held only at the horizon of position 2", "We want position 2 to contain the geometric object",
         "I agree. Run those questions through the cypher here please"]


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def stages():
    st = dict(STAGES)
    if MUT.get("both_at_opening"):
        st["opening"] = (1, 1, 1, 0)
    if MUT.get("nowhere_in_transit"):
        st["closing"] = (0, 0, 0, 1)
    return st


def cy():
    return _load(os.path.join(ROOT, "tools", "cypher.py"), "bi_cypher")


def stat(c, cells, k):
    cl = sorted(set(cells))
    ix = c.Index("bulk", C, [list(x) for x in cl])
    inv = [{v: kk for kk, v in ix.code[i].items()} for i in range(len(C))]
    a, _ = c.op_statistics(ix, {"statistics_order": k})
    return {tuple(inv[i][x[i]] for i in range(len(C))) for x in a}


def ordinal(c, cells, t):
    cl = sorted(set(cells))
    out = {}
    for lang in LANGS:
        hit = n = 0
        for orders in itertools.product(*[list(itertools.permutations([0, 1])) for _ in C]):
            ix = c.Index("bulk", C, [list(x) for x in cl], value_order={C[i]: list(orders[i]) for i in range(len(C))})
            inv = [{v: kk for kk, v in ix.code[i].items()} for i in range(len(C))]
            a, _ = c.ADMISSION[lang][0](ix, {})
            n += 1
            hit += t in ({tuple(inv[i][x[i]] for i in range(len(C))) for x in a} if a is not None else set())
        out[lang] = (hit, n)
    return out


def blocks(cells, t, k):
    return [tuple(C[i] for i in s) for s in itertools.combinations(range(len(C)), k)
            if tuple(t[i] for i in s) not in {tuple(x[i] for i in s) for x in cells}]


def compute():
    c = cy()
    ia = _load(os.path.join(HERE, "index_audit.py"), "bi_index_audit")
    st = stages()
    full = list(st.values())
    ix = c.Index("bulk", C, [list(x) for x in sorted(set(full))])
    rows, keys = c.coordinate_report(ix)
    # the first design, with (Z): its audit
    C5 = C + ["z_kept"]
    full5 = [st[k] + (Z[k],) for k in st]
    d2, d3 = stat(c, full, 2), stat(c, full, 3)
    wo = [v for k, v in st.items() if k != "realized"]
    wa = [v for k, v in st.items() if k != "after"]
    both = [x for x in BOX if x[0] == 1 and x[1] == 1]
    nowhere = [x for x in BOX if x[0] == 0 and x[1] == 0]
    wo2, wo3 = stat(c, wo, 2), stat(c, wo, 3)
    wa2, wa3 = stat(c, wa, 2), stat(c, wa, 3)
    rep = [x for x in BOX if x not in wa and x[0] == 0 and x[3] == 0]
    alg = []
    for orders in itertools.product(*[list(itertools.permutations([0, 1])) for _ in C]):
        ix2 = c.Index("bulk", C, [list(x) for x in sorted(set(full))], value_order={C[i]: list(orders[i]) for i in range(len(C))})
        a, _ = c.ADMISSION["algebra"][0](ix2, {})
        alg.append(len(a) - len(set(full)))
    return {"audit": ia.audit_index(C, full), "adds_nothing": [r["coordinate"] for r in rows if r["adds_nothing"]],
            "keys": keys, "audit5": ia.audit_index(C5, full5),
            "E2": len(d2) - len(set(full)), "E3": len(d3) - len(set(full)), "over2": sorted(d2 - set(full)),
            "meet": {"admitted2": [x for x in both if x in wo2], "admitted3": [x for x in both if x in wo3],
                     "blocks": blocks(wo, (1, 1, 1, 1), 2)},
            "nowhere": {"2": [x for x in nowhere if x in d2], "3": [x for x in nowhere if x in d3],
                        "ordinal": ordinal(c, full, (0, 0, 0, 0))},
            "after": {"2": st["after"] in wa2, "3": st["after"] in wa3, "blocks": blocks(wa, st["after"], 2),
                      "replacement": sum(x in wa2 for x in rep), "n_rep": len(rep), "ordinal": ordinal(c, wa, st["after"])},
            "z_unknown_where_h2": all((Z[k] == U) == (STAGES[k][3] == 1) for k in STAGES), "alg": (min(alg), max(alg))}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    text = open(os.path.join(os.path.dirname(HERE), "M-RULINGS-2026-10-03.md")).read().replace("\n    ", " ")
    add("I0 M's words for every cell verbatim in the rulings file (106 (b), 213, 216)", all(w in text for w in WORDS))
    add("I1 audit: no key, no redundant group; held_1 and held_2 each add nothing alone; the first design's (Z) "
        "duplicated horizon_2 (a redundant pair)", not d["audit"]["keys"] and not d["audit"]["onehot"] and not d["keys"]
        and sorted(d["adds_nothing"]) == ["held_1", "held_2"] and ("horizon_2", "z_kept") in d["audit5"]["onehot"])
    add("I2 closed at order 3 (E = 0); order 2 admits three both-held cells with fewer than both horizons",
        d["E3"] == 0 and d["E2"] == 3 and all(x[0] == 1 and x[1] == 1 and x[2] + x[3] < 2 for x in d["over2"]))
    m = d["meet"]
    add("I3 without the realized stage statistics admits no cell with the object at both positions (orders 2 and 3): "
        "the meeting is that stage, not assembled from the others", not m["admitted2"] and not m["admitted3"]
        and ("held_1", "held_2") in m["blocks"])
    n, a = d["nowhere"], d["after"]
    add("I4 statistics never admits the object held nowhere; without the after stage it refuses it, blocked by "
        "(held_1, horizon_2) and (held_2, horizon_2) -- the release is its own step; every novel cell with (held_1 0, "
        "horizon_2 0) refused alike", not n["2"] and not n["3"] and not a["2"] and not a["3"]
        and sorted(a["blocks"]) == [("held_1", "horizon_2"), ("held_2", "horizon_2")] and a["replacement"] == 0)
    add("I5 (Z) is unknown exactly at the stages with position 2's horizon (realized, closing)", d["z_unknown_where_h2"])
    o1, o2 = n["ordinal"], a["ordinal"]
    add("I6 the ordinal languages move with the coding (order/algebra 8/16 on 'held nowhere', 4/16 on the after stage; "
        "geometry 0); algebra's E 3-11", o1["order"] == (8, 16) and o1["geometry"] == (0, 16) and o2["order"] == (4, 16)
        and o2["geometry"] == (0, 16) and d["alg"] == (3, 11))
    return res


MUTANTS = {"both_at_opening": "the object entered as held at both positions already at the opening",
           "nowhere_in_transit": "the closing entered with the object held nowhere"}


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
        print("  mutant %-19s %-68s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("bulk_index.py -- the transfer through the cypher (item 216)\n")
    print("I1 audit:", d["audit"], "adds nothing:", d["adds_nothing"], "| first design:", d["audit5"])
    print("I2 E order 2 = %d (over-reach %s), order 3 = %d" % (d["E2"], d["over2"], d["E3"]))
    print("I3 meeting:", d["meet"])
    print("I4 nowhere:", d["nowhere"]["2"], d["nowhere"]["3"], d["nowhere"]["ordinal"], "| after:", d["after"])
    print("I5 (Z) unknown exactly where position 2's horizon stands:", d["z_unknown_where_h2"], "| algebra E:", d["alg"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
