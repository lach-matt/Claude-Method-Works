#!/usr/bin/env python3
"""calculator.py -- items 286-287: the cypher as a calculator.  M (286): "it not just an index tool, it is a
calculator, a brain... You need all 7 languages for it to work to it fullest potential. The input/question enters the
cypher in binary form, it is evaluated through the math languages in order of the hierarchy law and then logic will
output the answer in a binary form statement."  M (287): broadest first; analysis both ways; documentary citations
only; logic takes the last language's answer, the earlier ones narrowing what it can say.  Worked in the conversation
(computed; the protocol M's, its encoding the board's as named, 192); 2026-10-12.

  C0 (read) M's item-286 and item-287 words, verbatim in the rulings file.
  C1 The input.  A question is a cell over binary coordinates -- its attributes -- with its answer coordinate open,
     entered beside the known cells, each carrying its answer (ring_cypher's protocol, items 207-208).  The encoding of
     any question is the board's, named as such (192).
  C2 The order.  Roster 1173's own listing -- order, algebra, analysis, geometry, information, statistics,
     documentary -- broadest first in the hierarchy law's partial order (287 (a)).
  C3 The languages.  Each closure language (tools/cypher.py's operators, imported) admits the question's attributes with
     answer 0, 1, both or neither under its closure of the cells; narrowing (287 (b)): it chooses only among the
     answers the languages before it left open.  Analysis gives both binaries (288): it never narrows; where the
     question carries a continuous law, declared with its witness, each binary carries a signed magnitude -- log10 of
     the magnitude over its threshold, positive on the binary the law supports, negative on the other (item 25's
     "negative and positive" magnitudes); none where it carries no law.  [First built (287) with analysis returning one
     binary and narrowing to it -- M, item 288: "I said the analysis gives both binaries."]  Documentary returns
     citations only, no binary.  A silent closure language leaves the answers open and its
     silence is the finding.
  C4 Logic.  The answer is what the last closure language leaves: 1 or 0 when one answer remains, "both" when two
     (undecided -- then analysis's magnitudes rank the two, 288 (c)), "refused" when none.  Every language's output is kept in the trace.
  C5 The controls.  (i) The question entered both ways -- its cell with answer 0, then with answer 1 -- every language
     admits the cell it was handed (extensivity), so a refusal is the question's, not the index's (ring_cypher R7).
     (ii) The hierarchy law's seven lawful containments (research/warp-drive/hlaw.py's LAWFUL, imported) checked on the
     run's admitted sets, the question's cell included.
  C6 (computed) The fixtures are the corpus's own recorded decisions: ring_cypher's R5 (the ring entered as the fold --
     order, algebra, geometry and information leave both answers open, statistics decides 'not matter') and R4 (the
     ring as computed -- refused), reproduced through the protocol; beside them an OR fixture (answer 1, learnable) and
     an AND fixture whose one positive is the question itself, never seen -- answer 0: the calculator cannot learn a
     positive it was never shown, which any question's encoding must carry in mind; and a narrowing fixture (found by
     search over small indexes, computed) where statistics alone would admit 0 but information, before it, admits
     neither -- refused: narrowing decides.

What this does not do.
  - Choose a question's encoding: the instrument that asks names its own.
  - Pick a statistics order beyond the cypher's default (2); the trace gives the higher orders beside it.  [Item 289:
    the trace does not -- ask() runs the one order it is handed; c4_oneway P9 runs orders 1-3 for C4's question,
    order 4 refused at four coordinates (reg 1175).]

Imports tools/cypher.py and research/warp-drive/hlaw.py by path.  Stdlib.  python3 calculator.py [--selftest |
--mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
ROOT = os.path.dirname(os.path.dirname(WD))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M286 = "it is evaluated through the math languages in order of the hierarchy law"
M287 = '"Last in the order"'
ORDER = ["order", "algebra", "analysis", "geometry", "information", "statistics", "documentary"]
U = 2                                                       # the open answer, ordered after 0 and 1
_C = {}


def _load(path, key):
    if key in _C:
        return _C[key]
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    _C[key] = mod
    return mod


def cy():
    return _load(os.path.join(ROOT, "tools", "cypher.py"), "calc_cy")


def closure(coords, cells, lang, k=2):
    """the language's admitted set over the cells (decoded tuples), or None when silent"""
    c = cy()
    cl = sorted(set(cells))
    vo = {name: sorted({x[i] for x in cl}) for i, name in enumerate(coords)}
    ix = c.Index("calc", coords, [list(x) for x in cl], value_order=vo)
    out, _ = c.ADMISSION[lang][0](ix, {"statistics_order": k} if lang == "statistics" else {})
    if out is None:
        return None
    return {tuple(ix.decode[i][x[i]] for i in range(len(coords))) for x in out}


def ask(coords, known, attrs, analysis=None, citations=(), k=2):
    """known: cells (attrs..., answer); attrs: the question's attributes; analysis: None (silent) or a dict with
    witness, magnitude, threshold.  Returns the answer and the trace."""
    cells = list(known) + [tuple(attrs) + (U,)]
    order = list(ORDER)
    if MUT.get("tightest_first"):
        order = ["statistics", "information", "geometry", "analysis", "algebra", "order", "documentary"]
    open_ = {0, 1}
    trace, last = [], None
    for lang in order:
        if lang == "documentary":
            trace.append((lang, "citations", list(citations)))
            continue
        if lang == "analysis":
            # item 288: analysis gives both binaries, each with a signed magnitude where a continuous law is declared
            if analysis is None:
                mags = {0: None, 1: None}
                note = "both binaries; no continuous law declared, no magnitudes"
            else:
                L = math.log10(analysis["magnitude"] / analysis["threshold"])
                mags = {1: L, 0: -L}
                note = "both binaries; %s: 1 at %+.3g, 0 at %+.3g decades" % (analysis["witness"], L, -L)
            if MUT.get("analysis_narrows") and analysis is not None:
                open_ = {int(analysis["magnitude"] >= analysis["threshold"])} & open_    # the item-287 build
            trace.append((lang, "both", note + "; open after it: %s" % sorted(open_)))
            continue
        cl = closure(coords, cells, lang, k)
        if cl is None:
            trace.append((lang, "silent", "the language does not speak on this index"))
            continue
        said = {a for a in (0, 1) if tuple(attrs) + (a,) in cl}
        if MUT.get("no_narrowing"):
            trace.append((lang, sorted(said), ""))
            open_ = said
        else:
            open_ = said & open_
            trace.append((lang, sorted(open_), "of %s admitted" % sorted(said)))
        last = lang
    ans = {(0,): 0, (1,): 1, (0, 1): "both", (): "refused"}[tuple(sorted(open_))]
    mags = locals().get("mags", {0: None, 1: None})
    ranked = None
    if ans == "both" and mags[1] is not None:
        ranked = 1 if mags[1] > mags[0] else 0 if mags[0] > mags[1] else None
    return dict(answer=ans, by=last, trace=trace, magnitudes=mags, ranked=ranked)


def controls(coords, known, attrs, k=2):
    """C5 (i) both ways, extensive in every closure language; (ii) the lawful containments on the run's sets"""
    HL = _load(os.path.join(WD, "hlaw.py"), "calc_hl")
    ext = {}
    for a in (0, 1):
        cells = list(known) + [tuple(attrs) + (a,)]
        for lang in ("order", "algebra", "geometry", "information", "statistics"):
            cl = closure(coords, cells, lang, k)
            ext[(lang, a)] = cl is None or tuple(attrs) + (a,) in cl
    cells = list(known) + [tuple(attrs) + (U,)]
    sets = {lang: closure(coords, cells, lang, k) for lang in ("order", "algebra", "geometry", "information",
                                                                 "statistics")}
    law = {(a, b): sets[a] is None or sets[b] is None or sets[a] <= sets[b] for a, b in HL.LAWFUL}
    return dict(extensive=all(ext.values()), law=law, lawful=all(law.values()))


def ring():
    """the corpus's own recorded decisions (ring_cypher, items 207-208): R5, the ring entered as the fold -- statistics
    decides 'not matter'; R4, the ring as computed -- refused"""
    rc = _load(os.path.join(HERE, "ring_cypher.py"), "calc_rc")
    out = {}
    for desc in ("reading", "computed"):
        cells, attrs = rc.index_a(desc)
        out[desc] = ask(rc.CA, [c for c in cells if c[-1] != rc.U], attrs)
    return out


def compute():
    coords = ["x", "y", "ans"]
    OR = [(0, 0, 0), (0, 1, 1), (1, 0, 1)]                  # the answer the OR of two attributes: learnable
    AND = [(0, 0, 0), (0, 1, 0), (1, 0, 0)]                 # the AND: its one positive is the question, never seen
    r_or = ask(coords, OR, (1, 1))
    r_and = ask(coords, AND, (1, 1))
    an_lo = ask(coords, OR, (1, 1), analysis={"witness": "a fixture's magnitude below threshold", "magnitude": 0.5,
                                              "threshold": 1.0}, citations=["fixture"])
    # a fixture where narrowing decides (found by search, computed): statistics alone admits 0, information neither
    NARROW = [(0, 0, 0, 0), (0, 0, 0, 1), (0, 1, 0, 0), (0, 1, 1, 0), (1, 0, 1, 0)]
    r_nar = ask(["x", "y", "z", "ans"], NARROW, (0, 0, 1))
    return dict(ring=ring(), r_or=r_or, r_and=r_and, an_lo=an_lo, r_nar=r_nar, ctl=controls(coords, OR, (1, 1)))


def report(o):
    print("calculator.py -- the cypher as a calculator (items 286-287)\n")
    rows = [("ring R5 (the fold)", o["ring"]["reading"]), ("ring R4 (computed)", o["ring"]["computed"]),
            ("OR fixture", o["r_or"]), ("AND fixture", o["r_and"]), ("OR, analysis below threshold", o["an_lo"]),
            ("narrowing fixture", o["r_nar"])]
    for tag, r in rows:
        print("  %s: answer %s (by %s)" % (tag, r["answer"], r["by"]))
        print("      " + "; ".join("%s %s" % (t[0], t[1]) for t in r["trace"]))
    print("  controls: extensive both ways %s; the seven lawful containments %s" % (o["ctl"]["extensive"],
                                                                                  o["ctl"]["lawful"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("C0 M's item-286 and item-287 words verbatim in the rulings file", M286 in rul and M287 in rul)
    order_seen = [t[0] for t in o["r_or"]["trace"]]
    add("C2 the languages run in roster 1173's order, broadest first", order_seen == ORDER)
    rd = dict((t[0], t[1]) for t in o["ring"]["reading"]["trace"])
    ok = o["ring"]["reading"]["answer"] == 0 and o["ring"]["reading"]["by"] == "statistics"
    ok &= all(rd[L] == [0, 1] for L in ("order", "algebra", "geometry", "information")) and rd["statistics"] == [0]
    ok &= o["ring"]["computed"]["answer"] == "refused"
    add("C3 the corpus's recorded decisions reproduced: ring_cypher R5 -- the broad languages leave both open, "
        "statistics decides 'not matter' (0); R4 -- refused", ok)
    la = dict((t[0], t[1]) for t in o["an_lo"]["trace"])
    ok = o["r_or"]["answer"] == 1 and o["r_and"]["answer"] == 0 and o["an_lo"]["answer"] == 1
    ok &= la["analysis"] == "both" and o["an_lo"]["magnitudes"][1] < 0 < o["an_lo"]["magnitudes"][0]
    ok &= dict((t[0], t[1]) for t in o["r_or"]["trace"])["analysis"] == "both" and la["documentary"] == "citations"
    tn = dict((t[0], t[1]) for t in o["r_nar"]["trace"])
    ok &= o["r_nar"]["answer"] == "refused" and tn["information"] == [] and tn["geometry"] == [0, 1]
    add("C4 logic takes what the last closure language leaves: the OR fixture 1, the AND fixture 0 (its positive never "
        "seen); analysis gives both binaries, never narrowing -- below its threshold it signs them, 1 negative, 0 "
        "positive, and the OR's 1 stands; documentary citations only; narrowing decides where information excludes what "
        "statistics alone would admit (refused, not 0)", ok)
    add("C5 the controls: extensive both ways; the hierarchy law's seven containments hold on the run",
        o["ctl"]["extensive"] and o["ctl"]["lawful"])
    return res


MUTANTS = {"tightest_first": "the order reversed, tightest first",
           "analysis_narrows": "analysis returning one binary and narrowing (the item-287 build)",
           "no_narrowing": "each language deciding afresh, not narrowing"}


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
        print("  mutant %-15s %-44s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
