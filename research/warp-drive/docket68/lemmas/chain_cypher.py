#!/usr/bin/env python3
"""chain_cypher.py -- the Warp Theorem's chain after the green-the-chain round, through the cypher (items 192, 196).
A PROPOSAL for seating, never applied here: warptheorem.py is read, not edited (nothing is seated without M's word).

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
  o1c_complete.py  O1c PROVED for eq. (17)'s geometry (curvature bounded; every geodesic crosses the throat in finite
                   affine parameter and is unbounded at both ends); on M1.  Not verified by a separate session.
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

INPUTS = {
    "M1": "the plane's reading of the corridor's mouth (replaces F1; OPEN)",
    "M1P2": "position 2's side reads eq. (17)'s other leg (OPEN)",
    "FAR": "a far boundary consistent with (Z), (G), 139 (1), 166 (OPEN)",
    "WRITE": "the static bulk held through the whole write, >= 2.0e5 clocks (OPEN; R1-COVER pending)",
    "ARRIVAL": "the README forms the corridor as it comes in, no partner (198, M's guess; README-HELD's 4D models; formation in the bulk OPEN, 179)",
    "CLOSE": "the closing's negative null flux: ending the horizon and moving the hold need its area to shrink (README-HELD; area theorem; OPEN)",
    "SIGMA": "the plane's tension, k's scale (200 (3): ours to solve, through the cypher; OPEN)",
}
GREEN = {"PROVED", "DERIVED", "AXIOM"}
RANK = {"OPEN": 0, "NATURE": 1, "READING": 1, "DEFINITION": 2, "DERIVED": 3, "PROVED": 4}
# (row, status, inputs, the warptheorem.py row it refines)
ROWS = [
    ("G1", "DERIVED", "M1", "G1"), ("G2", "PROVED", "", "G2"), ("G3", "PROVED", "M1", "G3"), ("H1", "PROVED", "", "H1"),
    ("H2", "DERIVED", "", "H2"), ("H2t", "DERIVED", "M1 M1P2", "H2"),
    ("O1a", "DERIVED", "", "O1"), ("O1b", "PROVED", "M1", "O1"), ("O1c", "PROVED", "M1", "O1"), ("O2", "PROVED", "M1", "O2"),
    ("O3", "OPEN", "WRITE ARRIVAL", "O3"),
    ("Z1q", "PROVED", "", "Z1"), ("Z1t", "PROVED", "M1", "Z1"), ("Z2r", "PROVED", "M1", "Z2"),
        ("Z3a", "DERIVED", "", "Z3"), ("Z3b", "OPEN", "FAR WRITE ARRIVAL CLOSE", "Z3"), ("Z3c", "DERIVED", "", "Z3"),
    ("B1", "PROVED", "", "B1"), ("B2", "PROVED", "", "B2"), ("B2t", "PROVED", "M1", "B2"),
    ("B3", "OPEN", "M1 FAR WRITE ARRIVAL", "B3"), ("B4a", "PROVED", "", "B4a"), ("B4c", "READING", "FAR", "B4c"),
    ("B4b", "READING", "M1 WRITE", "B4b"), ("B4d", "OPEN", "M1 WRITE ARRIVAL CLOSE", "B4d"),
    ("B5a", "DERIVED", "", "B5"), ("B5p", "OPEN", "", "B5"), ("B5b", "OPEN", "", "B5"),
    ("B6", "PROVED", "", "B6"), ("B6'", "OPEN", "SIGMA", "B6'"), ("B7", "DERIVED", "WRITE ARRIVAL CLOSE", "B7"),
    ("I1", "DERIVED", "", "I1"), ("I2", "PROVED", "", "I2"), ("E1u", "DERIVED", "", "E1"), ("E2u", "DERIVED", "", "E2"), ("E1x", "DERIVED", "CLOSE", "E1"), ("E2x", "DERIVED", "CLOSE", "E2"),
    ("E3", "DERIVED", "", "E3"), ("E4r", "PROVED", "M1", "E4"),
    ("R0", "DEFINITION", "", "R0"), ("R1", "DEFINITION", "", "R1"), ("R2", "DEFINITION", "", "R2"),
    ("R3", "PROVED", "", "R3"), ("R4", "DERIVED", "", "R4"), ("R5", "DERIVED", "", "R5"),
]


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
        r = [(a, b, "M1P2" if a == "B6" else c, d) for a, b, c, d in r]
    if MUT.get("e12_close_free"):
        r = [(a, b, "" if a in ("E1x", "E2x") else c, d) for a, b, c, d in r]
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
    for k in range(len(INPUTS) + 1):
        hits = [S for S in itertools.combinations(INPUTS, k) if all(green(r, set(S)) for r in target)]
        if hits:
            out["smallest"] = hits
            break
    out["with"] = {S: sum(green(r, set(S)) for r in R) for S in (("M1",), ("M1", "CLOSE"), ("M1", "M1P2", "CLOSE"))}
    return out


def current_table():
    """warptheorem.py's own rows (read only) and the rows this proposal changes."""
    wt = _load(os.path.join(D68, "warptheorem.py"), "cc_warptheorem")
    cur = {n.split()[0]: st for _, n, st, _ in wt.LEMMAS}
    changed = {}
    for a, b, c, parent in rows():
        if parent in cur and (a != parent or b != cur[parent] or c):
            changed.setdefault(parent, []).append((a, b, c))
    return cur, changed


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
    cur, changed = current_table()
    main = cypher(*index())
    # control: CLOSE made a copy of M1 in every row -> information must report one of them determined by the other
    def dup(coords, cells):
        i, j = coords.index("CLOSE"), coords.index("M1")
        return coords, [c[:i] + [c[j]] + c[i + 1:] for c in cells]
    ctrl = cypher(*index(extra=dup))
    return {"tally": t, "current": cur, "changed": changed, "cy": main, "ctrl": ctrl}


def checks(d):
    t, res = d["tally"], []
    add = lambda name, ok: res.append((name, bool(ok)))
    add("C1 green now: 20 of 45 (strict), 23 of 45 (audit rule); B6 green on item 200 (1), Z3c DERIVED (nature_rows.py)",
        len(t["strict"]) == 20 and len(t["audit"]) == 23 and t["n"] == 45 and "B6" in t["strict"] and "Z3c" in t["strict"])
    add("C2 the smallest input set greening every green-status lemma: {M1, M1P2, WRITE, ARRIVAL, CLOSE}",
        t["smallest"] == [("M1", "M1P2", "WRITE", "ARRIVAL", "CLOSE")])
    add("C3 M1 alone greens 29 of 45; with CLOSE 31; with M1P2 too 32",
        t["with"][("M1",)] == 29 and t["with"][("M1", "CLOSE")] == 31 and t["with"][("M1", "M1P2", "CLOSE")] == 32)
    add("C4 no row is never-greenable after item 200 (2); 9 rows non-green by their own status, B6' OPEN (200 (3))",
        t["excluded"] == [] and len(t["own_status"]) == 9 and t["own_status"].get("B6'") == "OPEN")
    ch = d["changed"]
    add("C5 every proposal row refines one of warptheorem.py's 34 rows, and at least 14 of them change",
        len(d["current"]) == 34 and set(r[3] for r in rows()) <= set(d["current"]) and len(ch) >= 14)
    cy = d["cy"]
    add("C6 cypher: information reports ARRIVAL, FAR, WRITE as adding nothing; M1, M1P2, CLOSE, SIGMA are the "
        "independent axes on this encoding", {"ARRIVAL", "FAR", "WRITE"} <= cy["adds_nothing"]
        and not ({"M1", "M1P2", "CLOSE", "SIGMA"} & cy["adds_nothing"]))
    add("C7 cypher: five operator-bearing languages speak with E > 0; documentary silent",
        all(cy[l][0] is not None and cy[l][0] > 0 for l in ("order", "algebra", "geometry", "information", "statistics"))
        and cy["documentary_silent"])
    add("C8 control: CLOSE made a copy of M1 -> information reports one of them as adding nothing (the test can fail)",
        bool({"CLOSE", "M1"} & d["ctrl"]["adds_nothing"]) and not ({"CLOSE", "M1"} & d["cy"]["adds_nothing"]))
    return res


MUTANTS = {"e12_close_free": "E1x, E2x (between universes) read as resting on no closing flux", "b6_on_count": "B6 read as still resting on an open premise", "g1_f1_free": "G1, G3 read F1-free (the item-192 list)",
           "definition_strict": "DEFINITION counted green under the strict rule"}


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
    print("chain_cypher.py -- the chain after the green-the-chain round (a proposal; nothing seated)\n")
    print("green now: %d of %d strict, %d audit rule" % (len(t["strict"]), t["n"], len(t["audit"])))
    print("  green:", " ".join(t["strict"]))
    print("  non-green by own status:", t["own_status"])
    print("  never greenable as stated:", t["excluded"])
    print("  smallest input set:", t["smallest"], " with:", t["with"])
    print("\nwarptheorem.py rows this proposal changes:")
    for p, v in d["changed"].items():
        print("  %-4s %-10s -> %s" % (p, d["current"][p], "; ".join("%s %s%s" % (a, b, (" on " + c) if c else "") for a, b, c in v)))
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
