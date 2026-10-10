#!/usr/bin/env python3
"""chain_cypher.py -- the Warp Theorem's chain after the green-the-chain round, through the cypher (items 192, 196).
Seated on item 206: the rows are read from warptheorem.py (the theorem of record); this file classifies them.

Each row is a lemma or a part of one, with the status its owner note earned and the foundational inputs it still rests
on (the board's reading of each dependency, sourced per row).  Green rule (the board's, item 192): GREEN only if
PROVED, DERIVED or AXIOM with no non-green input; DEFINITION is counted apart (the strict rule) and with green (the
audit rule).  The cypher (tools/cypher.py, roster 1173) then classifies the index: it says which inputs are independent
axes and which are determined by the others ('adds nothing', register 1356) -- a statement about this encoding
(H-CYPHER-CHAIN, the board's), not a physical derivation.

Sources of this round's changes (each checked by two separate AI sessions in this project unless marked):
  B1-MATTER.md     B1 -> B1' PROVED (planes with matter); B2 -> B2' PROVED, B2t on M1; Z3 -> Z3'a DERIVED, Z3'b OPEN,
                   Z3'c NATURE (w >= -1); B5 -> B5'a DERIVED (conditional), B5'p and B5'b OPEN
  F1-AUDIT.md      F1 replaced by M1 (OPEN); G1, G3 rest on M1; H2 DERIVED from 132; O1 -> O1a DERIVED, O1b on M1, O1c
                   OPEN; Z1 -> Z1q PROVED, Z1t on M1; Z2r, E4r on M1; Z2, E4 as stated need M1-global (excluded);
                   H2t on M1 and M1-P2
  ITEM197          M1's single-plane clause moot (facing, our plane needs no added matter); M1 stays OPEN (bridge =
                   SIM2-FACING phase 2b-i).  Not verified by a separate session.
  B6P-SCALE.md     B6' stays NATURE (B6'' as one lemma OPEN; in the chain's configuration NATURE)
  B4C-FAR.md       B4c READING, cannot turn green on H-FAR-MODEL; needs a far boundary consistent with (Z), (G), 139 (1), 166
  COUNT-CYPHER.md  no status moves; the board reads B6's k_R = 3k_L/4 as resting on the doubled count, a premise
                   (deduced here, not verified by a separate session)
  README-HELD.md   'held, not crossing' fails in every computed model; the README forms the horizon it crosses
                   (H-ARRIVAL-FORMS-THE-HORIZON); 198 (M's guess) takes that way in: ARRIVAL replaces F5's pair for the
                   README.  New OPEN: the closing's negative flux (CLOSE), on which E1 and E2 now rest ('(a) with OPEN')
  CLOSE-FLUX.md    CLOSE splits by trajectory class: within one universe no event horizon, no negative-flux demand
                   (E1u, E2u DERIVED, no input); between universes it stands (E1x, E2x on CLOSE).  Not verified by a
                   separate session.
  item 200         (1) position 2's plane counts once: B6 restated k_R = k_L/2, PROVED (b6_once.py), no input;
                   (2) Z2 and E4 restated within the reach (Z2r, E4r); (3) Z3c and B6' are ours to solve: NATURE -> OPEN
  nature_rows.py   Z3c DERIVED: the plane's dark energy has w >= -1 (seated (Z) via TS, SMS READ); B6' OPEN: sigma is an
                   axis no clause determines (the cypher), one relation missing.  Not verified by a separate session.
  item 201         B6' a DEFINITION: our universe is defined by its plane's tension and its dark-energy offset
                   (sigma_defines.py T1-T4 show it consistent)
  o1c_complete.py  O1c PROVED for eq. (17)'s geometry (curvature bounded; every geodesic crosses the throat in finite
                   affine parameter and is unbounded at both ends); on M1.  Not verified by a separate session.
  item 204         the B5'p and M1P2 splits HELD: tallied beside the chain (HELD, held_tally), never in it
python3 chain_cypher.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
MUT = {}

GREEN = {"PROVED", "DERIVED", "AXIOM"}
RANK = {"OPEN": 0, "NATURE": 1, "READING": 1, "DEFINITION": 2, "DERIVED": 3, "PROVED": 4}


def _load_wt():
    path = os.path.join(D68, "warptheorem.py")
    spec = importlib.util.spec_from_file_location("cc_wt_table", path)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


# The chain IS the seated theorem (item 206): its rows are warptheorem.py's lemmas, its inputs warptheorem.py's clause-N
# rows, and what each row rests on is warptheorem.py's RESTS_ON.  (row, status, inputs, the row it refines)
_WT = _load_wt()
INPUTS = {n.split()[0]: n.split(" ", 1)[1] for c, n, st, w in _WT.LEMMAS if c == "N"}
ROWS = [(n.split()[0], st, _WT.RESTS_ON.get(n.split()[0], ""), n.split()[0]) for c, n, st, w in _WT.LEMMAS if c != "N"]


# Proposals HELD by M (item 204), then SEATED on item 206: the list is empty while nothing is held.
HELD = []


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, os.path.dirname(D68)]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[key] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def rows():
    r = list(ROWS)
    if MUT.get("b6_on_count"):
        r = [(a, b, "M1P2x" if a == "B6" else c, d) for a, b, c, d in r]
    if MUT.get("e12_close_free"):
        r = [(a, b, "" if a in ("E1x", "E2x") else c, d) for a, b, c, d in r]
    if MUT.get("unseat_z3b"):
        r = [(a, "OPEN" if a == "Z3b" else b, c, d) for a, b, c, d in r]
    if MUT.get("g1_f1_free"):
        r = [(a, b, "" if a in ("G1", "G3") else c, d) for a, b, c, d in r]
    return r


def green(row, greened, definition=False):
    rule = GREEN | ({"DEFINITION"} if definition or MUT.get("definition_strict") else set())
    return row[1] in rule and all(d in greened for d in row[2].split())


def tally():
    R = rows()
    out = {"n": len(R), "strict": [r[0] for r in R if green(r, set())],
           "audit": [r[0] for r in R if green(r, set(), True)],
           "excluded": [r[0] for r in R if "EXCLUDED" in r[2]],
           "own_status": {r[0]: r[1] for r in R if r[1] not in GREEN | {"DEFINITION"}}}
    target = [r for r in R if r[1] in GREEN and "EXCLUDED" not in r[2]]
    out["smallest"] = []
    for k in range(len(INPUTS) + 1):
        hits = [S for S in itertools.combinations(INPUTS, k) if all(green(r, set(S)) for r in target)]
        if hits:
            out["smallest"] = hits
            break
    out["with"] = {S: sum(green(r, set(S)) for r in R) for S in (("M1",), ("M1", "CLOSE"), ("M1", "M1P2x", "CLOSE"),
                                                                  tuple(INPUTS))}
    return out


def held_rows(held=None):
    held = HELD if held is None else held
    R, ren = [], {}
    for h in held:
        ren.update(h["inputs"])
    rep = {k: v for h in held for k, v in h["replace"].items()}
    for r in ROWS:
        for a, b, c, d in rep.get(r[0], [r]):
            R.append((a, b, " ".join(ren.get(x, x) for x in c.split()), d))
    inputs = [ren.get(k, k) for k in INPUTS]
    return R, inputs


def held_tally():
    """the chain as it would read with every HELD proposal seated -- beside the chain, not in it"""
    R, inputs = held_rows()
    out = {"n": len(R), "strict": [r[0] for r in R if green(r, set())],
           "audit": [r[0] for r in R if green(r, set(), True)], "inputs": inputs}
    out["with_M1"] = sum(green(r, {"M1"}) for r in R)
    return out


def current_table():
    """the seated theorem, read afresh from warptheorem.py: its lemma rows, its inputs, and whether every name a lemma
    rests on is one of its inputs"""
    wt = _load(os.path.join(D68, "warptheorem.py"), "cc_warptheorem")
    lem = {n.split()[0]: st for c, n, st, _ in wt.LEMMAS if c != "N"}
    inp = [n.split()[0] for c, n, st, _ in wt.LEMMAS if c == "N"]
    rests_ok = all(x in inp for v in wt.RESTS_ON.values() for x in v.split())
    return {"lemmas": lem, "inputs": inp, "rests_ok": rests_ok,
            "same": [(r[0], r[1]) for r in rows()] == list(lem.items()) and inp == list(INPUTS)}


def index(R=None, extra=None):
    R = R or rows()
    F = list(INPUTS)
    coords = ["status"] + F + ["excluded"]
    cells = [[RANK[r[1]]] + [1 if f in r[2].split() else 0 for f in F] + [1 if "EXCLUDED" in r[2] else 0] for r in R]
    if extra:
        coords, cells = extra(coords, cells)
    return coords, cells


def cypher(coords, cells):
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "cc_cypher")
    uniq = sorted(set(tuple(c) for c in cells))
    ix = cy.Index("chain", coords, [list(c) for c in uniq])
    out = {}
    for lang in ("order", "algebra", "geometry", "information", "statistics"):
        adm, note = cy.ADMISSION[lang][0](ix, {})
        out[lang] = (None if adm is None else len(adm) - len(ix.cells), note)
    rws, keys = cy.coordinate_report(ix)                     # what the CLI appends to information's note
    out["adds_nothing"] = {r["coordinate"] for r in rws if r["adds_nothing"]}
    out["keys"] = list(keys)
    out["documentary_silent"] = "documentary" not in cy.ADMISSION or cy.ADMISSION["documentary"][0](ix, {})[0] is None
    return out


def compute():
    t = tally()
    cur = current_table()
    main = cypher(*index())
    # control: CLOSE made a copy of M1 in every row -> information must report one of them determined by the other
    def dup(coords, cells):
        i, j = coords.index("CLOSE"), coords.index("M1")
        return coords, [c[:i] + [c[j]] + c[i + 1:] for c in cells]
    ctrl = cypher(*index(extra=dup))
    return {"tally": t, "current": cur, "cy": main, "ctrl": ctrl, "held": held_tally()}


def checks(d):
    t, res = d["tally"], []
    add = lambda name, ok: res.append((name, bool(ok)))
    add("C1 green now (seated, item 206): 21 of 47 (strict), 25 of 47 (audit rule); B5pu among them; B6 on 200 (1), Z3c "
        "DERIVED, B6' a DEFINITION (201)", len(t["strict"]) == 21 and len(t["audit"]) == 25 and t["n"] == 47
        and "B5pu" in t["strict"] and "B6" in t["strict"] and "Z3c" in t["strict"] and "B6'" in t["audit"])
    add("C2 the smallest input set greening every green-status lemma is all six inputs: {M1, M1P2x, FAR, WRITE, ARRIVAL, "
        "CLOSE} (FAR enters through Z3b, now DERIVED)", t["smallest"] == [("M1", "M1P2x", "FAR", "WRITE", "ARRIVAL", "CLOSE")])
    add("C3 M1 alone greens 31 of 47; with CLOSE 33; with M1P2x too 34; with every input 36 (the other 11: 7 non-green "
        "by their own status, 4 definitions under the strict rule)", t["with"][("M1",)] == 31
        and t["with"][("M1", "CLOSE")] == 33 and t["with"][("M1", "M1P2x", "CLOSE")] == 34 and t["with"][tuple(INPUTS)] == 36)
    add("C4 no row is never-greenable; 7 rows non-green by their own status (O3, B3, B4c, B4b, B4d, B5px, B5b)",
        t["excluded"] == [] and sorted(t["own_status"]) == sorted(["O3", "B3", "B4c", "B4b", "B4d", "B5px", "B5b"]))
    cu = d["current"]
    add("C5 the chain is the seated theorem: its rows and statuses are warptheorem.py's lemma rows, its inputs "
        "warptheorem.py's clause-N rows, and every name a lemma rests on is an input", cu["same"] and cu["rests_ok"]
        and len(cu["lemmas"]) == 47 and len(cu["inputs"]) == 6)
    cy = d["cy"]
    add("C6 cypher: information reports which inputs add nothing on this encoding; M1 and CLOSE stay independent axes",
        not ({"M1", "CLOSE"} & cy["adds_nothing"]))
    add("C7 cypher: five operator-bearing languages speak with E > 0; documentary silent",
        all(cy[l][0] is not None and cy[l][0] > 0 for l in ("order", "algebra", "geometry", "information", "statistics"))
        and cy["documentary_silent"])
    add("C8 control: CLOSE made a copy of M1 -> information reports one of them as adding nothing (the test can fail)",
        bool({"CLOSE", "M1"} & d["ctrl"]["adds_nothing"]) and not ({"CLOSE", "M1"} & d["cy"]["adds_nothing"]))
    add("C9 nothing is held (item 206 seated the 204 splits): the held view equals the chain", d["held"]["n"] == t["n"]
        and len(d["held"]["strict"]) == len(t["strict"]) and HELD == [])
    return res


MUTANTS = {"e12_close_free": "E1x, E2x (between universes) read as resting on no closing flux", "b6_on_count": "B6 read as still resting on an open premise", "g1_f1_free": "G1, G3 read F1-free (the item-192 list)",
           "definition_strict": "DEFINITION counted green under the strict rule",
           "unseat_z3b": "Z3b put back to OPEN (pass 2's correction undone)"}


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
        failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-18s %-48s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    t = d["tally"]
    print("chain_cypher.py -- the chain, read from the seated theorem (warptheorem.py, item 206)\n")
    print("green now: %d of %d strict, %d audit rule" % (len(t["strict"]), t["n"], len(t["audit"])))
    print("  green:", " ".join(t["strict"]))
    print("  non-green by own status:", t["own_status"])
    print("  never greenable as stated:", t["excluded"])
    print("  smallest input set:", t["smallest"], " with:", t["with"])
    h = d["held"]
    print("held beside the chain: %s (item 206 seated the 204 splits)" % ("none" if not HELD else len(HELD)))
    for p in HELD:
        print("  %s  %s" % (p["id"], p["source"]))
    print("\nthe chain is the seated theorem (warptheorem.py):", d["current"]["same"], " inputs:", d["current"]["inputs"])
    print("\ncypher (roster 1173):")
    for l in ("order", "algebra", "geometry", "information", "statistics"):
        print("  %-12s E=%s  %s" % (l, d["cy"][l][0], d["cy"][l][1]))
    print("  information: adds nothing:", sorted(d["cy"]["adds_nothing"]), " KEY not axis:", d["cy"]["keys"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
