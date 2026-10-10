#!/usr/bin/env python3
"""belongs_cypher.py -- what in the seated theorem does not belong, and what is missing, asked of the cypher on its exact
counts (items 208, 209).  Computed by import of warptheorem.py and tools/cypher.py; deduced where marked; not verified by
a separate session; not seated; 2026-10-10.

M, 208: "We have too much information in the cypher. Something doesn't belong. Ask the cypher what the ring is supposed to
be, and what in the current theorem doesn't belong or what is missing".  M, 209: "Normalizing suggests that we are allow
for broad coefficients instead of exact evaluated values" -- so every count here is the cypher's exact E (admitted cells
less held cells), never a ratio.

  B1 (computed) the theorem as an index: each of warptheorem.py's 53 rows (47 lemmas, 6 inputs) a cell over (status OPEN <
     READING < DEFINITION < DERIVED < PROVED, the six inputs it rests on (RESTS_ON), scope -- general, within one
     universe, between universes -- and whether it is an input row).  No per-cell key: 20 distinct cells.  Exact E:
     order 748, algebra 748, geometry 114, information 312, statistics 52 -- 1974 cells admitted that the theorem does
     not hold.  The theorem is not a closed index
  B2 (computed) what does not belong: each distinct cell left out, the exact fall in E.  B4c falls most (1974 -> 1168,
     -806), then B4b (-638), then E1x and E2x together (-615).  Statistics alone, which no coding moves: B4c 52 -> 26,
     B4b -> 30, E1x/E2x -> 33 -- the same order
  B3 (computed, by text) the two rows that fall most carry broad coefficients in their own records -- approximate
     calibrations ("~"), ranges, a Pade heuristic, the flat limit: B4c (the far boundary, READING, "calibrated to the
     static window's ~11.3-clock reach") and B4b (the static bulk regular for holds "below ~11.3 clocks", READING).  Both
     describe a hold of ~11.3 clocks; the hold is the write, >= 2.0e5 clocks (O3, item 160), and both records already say
     "re-read with B4d".  B4d's record carries a range too ("8-16 clocks at every finite ell tested") -- the first
     version of this file said only B4c and B4b; the item-208 critic refuted that, and it is corrected here.  209's
     reading H-BROAD-DOES-NOT-BELONG is supported, not decided: B4b and B4c together lower E with no language rising on
     every coding the critics tried, but six other pairs do the same
  B4 (computed) what is missing: 15 cells every language admits that the theorem does not hold.  Each, added, lowers E
     by exactly one in every language: they are the excess every language shares, not cells whose absence keeps the index open.  Among
     them the join of B3 and B4d -- a row OPEN on M1, FAR, WRITE, ARRIVAL and CLOSE together, the theorem's own conclusion
     -- and between-universe DERIVED rows resting on nothing, on M1, and on M1 with CLOSE
  B5 (computed) controls: the input rows (five share one cell) left out lower the exact E by 557 -- 4th; a row seated
     twice changes nothing (cells are a set)
  B6 (computed) item 208's correction seated -- Z3b OPEN on the ring -- lowers the theorem's exact E from 1974 to 1938
     (geometry 114 -> 90, statistics 52 -> 40); B4c, B4b, E1x/E2x still head the leave-one-out
  B7 (computed; the critics' check) B4b and B4c left out together lower E with no language rising
Item-208 critics (an independent rebuild, 74 design-and-coding jobs and 382 more codings): every count here reproduces;
no single row closes any design; which row falls most depends on the design; no "missing" cell survives a change of
coding -- B4 is the shared excess, nothing more.
So, on the exact counts: what falls most is B4c, then B4b -- the two READINGs calibrated to a hold that does not happen;
the cypher does not single them out uniquely (not decided); nothing is missing that survives a change of coding.  The ring is not a row of the theorem: it sits inside M1's record, and is put to the cypher in
ring_cypher.py and in this file's R rows.
Imports warptheorem.py and tools/cypher.py by path.  Stdlib.  python3 belongs_cypher.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
_C = {}
LANGS = ("order", "algebra", "geometry", "information", "statistics")
INPUTS = ["M1", "M1P2x", "FAR", "WRITE", "ARRIVAL", "CLOSE"]
STATUS = {"OPEN": 0, "READING": 1, "DEFINITION": 2, "DERIVED": 3, "PROVED": 4}
CO = ["status"] + INPUTS + ["scope", "input"]
BROAD = re.compile(r"~|\bheuristic\b|\bcalibrat|\bPade\b|\bflat limit\b|\d\.\d+\s*-\s*\d\.\d+|\b\d+\s*-\s*\d+\s+clocks")
AS_ASKED = {"Z3b": "DERIVED"}            # the table as it stood when M asked (item 208); item 208's seating set Z3b OPEN


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def cy():
    if "cy" not in _C:
        _C["cy"] = _load(os.path.join(ROOT, "tools", "cypher.py"), "belongs_cy")
    return _C["cy"]


def wt():
    if "wt" not in _C:
        _C["wt"] = _load(os.path.join(D68, "warptheorem.py"), "belongs_wt")
    return _C["wt"]


# ================================================================================================= B0 M's words
WORDS = {"208": "We have too much information in the cypher. Something doesn't belong. Ask the cypher what the ring is",
         "209": "Normalizing suggests that we are allow for broad coefficients instead of exact evaluated values"}


def words():
    text = open(RULINGS, encoding="utf-8").read()
    w = dict(WORDS)
    if MUT.get("misquote"):
        w["209"] = "Normalizing is fine"
    return {k: v in text for k, v in w.items()}


# ======================================================================================================= B1 cells
def rows(table="as_asked"):
    out = []
    for clause, name, status, where in wt().LEMMAS:
        key = name.split()[0]
        if table == "as_asked":
            status = AS_ASKED.get(key, status)
        text = name.lower()
        ins = wt().RESTS_ON.get(key, "").split()
        if MUT.get("drop_b4c_input") and key == "B4c":
            ins = []
        scope = 1 if "within one universe" in text else (2 if "between universes" in text or key == "M1P2x" else 0)
        st = STATUS[status] if not (MUT.get("b4c_derived") and key == "B4c") else STATUS["DERIVED"]
        cell = tuple([st] + [int(i in ins) for i in INPUTS] + [scope, int(clause == "N")])
        out.append({"name": key, "cell": cell, "broad": bool(BROAD.search(name + " " + where))})
    return out


def E(cells):
    cl = sorted(set(cells))
    ix = cy().Index("theorem", CO, [list(c) for c in cl])
    out = {}
    for lg in LANGS:
        a, _ = cy().ADMISSION[lg][0](ix, {})
        out[lg] = None if a is None else len(a) - len(ix.cells)
    return out, ix


def total(e):
    return sum(v for v in e.values() if v is not None)


def common_missing(cells):
    cl = sorted(set(cells))
    ix = cy().Index("theorem", CO, [list(c) for c in cl])
    common = None
    for lg in LANGS:
        a, _ = cy().ADMISSION[lg][0](ix, {})
        dec = {tuple(ix.decode[i][x[i]] for i in range(len(CO))) for x in a}
        common = dec if common is None else common & dec
    return sorted(common - set(cl))


def measure(table):
    rs = rows(table)
    cells = [r["cell"] for r in rs]
    names = {}
    for r in rs:
        names.setdefault(r["cell"], []).append(r["name"])
    e0, ix = E(cells)
    drops = []
    for c in sorted(set(cells)):
        e1, _ = E([x for x in cells if x != c])
        drops.append((total(e1) - total(e0), names[c], e1))
    drops.sort(key=lambda x: x[0])
    stat = sorted(((E([x for x in cells if x != c])[0]["statistics"], names[c]) for c in sorted(set(cells))))
    miss = common_missing(cells)
    add_one = [tuple(E(cells + [m])[0][lg] - e0[lg] for lg in LANGS) for m in miss]
    broad = sorted(r["name"] for r in rs if r["broad"])
    pair = E([x for x in cells if x not in {r["cell"] for r in rs if r["name"] in ("B4b", "B4c")}])[0]
    return {"n": len(rs), "distinct": len(set(cells)), "E": e0, "box": ix.box, "drops": drops, "stat": stat,
            "missing": miss, "add_one": add_one, "broad": broad, "names": names, "pair": pair}


def compute():
    d = measure("as_asked")
    d["seated"] = measure("seated")
    d["words"] = words()
    return d


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("B0 M's words verbatim in the rulings file: 208, 209", all(d["words"].values()))
    add("B1 53 rows, 20 distinct cells, no key; exact E order 748, algebra 748, geometry 114, information 312, statistics "
        "52 (1974): not closed", d["n"] == 53 and d["distinct"] == 20
        and d["E"] == {"order": 748, "algebra": 748, "geometry": 114, "information": 312, "statistics": 52})
    top = [(x[0], x[1]) for x in d["drops"][:3]]
    add("B2 left out one at a time, B4c lowers the exact E most (-806), then B4b (-638), then E1x/E2x (-615); statistics "
        "alone the same order (26, 30, 33)",
        top == [(-806, ["B4c"]), (-638, ["B4b"]), (-615, ["E1x", "E2x"])]
        and [s[1] for s in d["stat"][:3]] == [["B4c"], ["B4b"], ["E1x", "E2x"]] and [s[0] for s in d["stat"][:3]] == [26, 30, 33])
    add("B3 the rows whose own record carries broad coefficients are B4b, B4c (calibrated to ~11.3 clocks) and B4d (a "
        "range over the family tested); the counts single out B4c and B4b first",
        d["broad"] == ["B4b", "B4c", "B4d"] and {tuple(x[1]) for x in d["drops"][:2]} == {("B4c",), ("B4b",)})
    add("B4 15 cells every language admits are missing; each, added, lowers the exact E by exactly one in every "
        "language", len(d["missing"]) == 15 and set(d["add_one"]) == {(-1, -1, -1, -1, -1)})
    inp = [x[0] for x in d["drops"] if x[1] == ["M1", "FAR", "WRITE", "ARRIVAL", "CLOSE"]]
    add("B5 control: the input rows left out lower the exact E by 557, fourth", inp == [-557]
        and [x[1] for x in d["drops"]].index(["M1", "FAR", "WRITE", "ARRIVAL", "CLOSE"]) == 3)
    se = d["seated"]
    add("B6 on the table as corrected by item 208 (Z3b OPEN): exact E order 748, algebra 748, geometry 90, information "
        "312, statistics 40 (1938, 36 less than as asked); B4c, B4b, E1x/E2x still lower it most",
        se["E"] == {"order": 748, "algebra": 748, "geometry": 90, "information": 312, "statistics": 40}
        and [x[1] for x in se["drops"][:3]] == [["B4c"], ["B4b"], ["E1x", "E2x"]])
    no_rise = lambda m: all(m["pair"][lg] <= m["E"][lg] for lg in LANGS) and total(m["pair"]) < total(m["E"])
    add("B7 B4b and B4c left out together lower the exact E with no language rising, as asked and as corrected (the "
        "critics: on every coding tried, and not unique -- six other pairs do it too)", no_rise(d) and no_rise(se))
    return res


MUTANTS = {"misquote": "M's 209 misquoted",
           "b4c_derived": "B4c entered as DERIVED instead of READING",
           "drop_b4c_input": "B4c entered as resting on nothing"}


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
        _C.pop("wt", None)
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-15s %-45s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("belongs_cypher.py -- what does not belong, what is missing (items 208, 209)\n")
    print("as asked (item 208): rows %d, distinct cells %d, box %d, exact E %s (total %d)" % (d["n"], d["distinct"], d["box"], d["E"], total(d["E"])))
    print("as corrected (Z3b OPEN): exact E %s (total %d)" % (d["seated"]["E"], total(d["seated"]["E"])))
    print("left out one at a time (exact fall in total E):")
    for dd, nm, e in d["drops"]:
        print("  %5d  %-40s %s" % (dd, ",".join(nm), e))
    print("rows carrying broad coefficients:", d["broad"])
    print("missing (every language admits, not held): %d" % len(d["missing"]))
    for m in d["missing"]:
        print("  ", dict(zip(CO, m)))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
