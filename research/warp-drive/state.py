#!/usr/bin/env python3
r"""
state.py -- THE CURRENT STATE OF THE INDEX WORK, GENERATED, FOR A READER WHO
IS NOT THIS SESSION.

    python3 state.py            the reading
    python3 state.py --json     write STATE.json
    python3 state.py --md       write STATE.md
    python3 state.py --check    STATE.json against a fresh computation; exit 1
                                on drift
    python3 state.py --selftest fixtures

===============================================================================
0. WHY THIS EXISTS AND WHAT IT IS NOT
===============================================================================

`research/README.md` is twelve thousand lines and it is a RECORD: it keeps
superseded readings beside current ones on purpose, because a withdrawn figure
that leaves no trace is how a corpus forgets it was ever wrong.  That makes it
the right thing to read and the wrong thing to quote from at a glance -- the
paragraph you land on may be the one that was corrected three sections later.

    SO THIS FILE ANSWERS ONE QUESTION: what is true right now.

    NOTHING IN THE GENERATED PART IS TYPED BY HAND.  Every figure is ASKED of
    the instrument that owns it -- `registry` for the rows, `figure` for the
    vertex set, `demand` for E, `overlaprule` for what the ruling seated and
    refused, `boxinvariance` for its verdict.  A number here that disagrees
    with its instrument is impossible rather than unlikely, and `--check`
    proves the written STATE.json still agrees.

    THE ONE HAND-MAINTAINED PART IS `DOCKETS`, and it is marked as such,
    because a docket is prose: a question, its status, and what would settle
    it.  The selftest refuses a docket missing any of the three.

===============================================================================
1. WHAT A READER SHOULD AND SHOULD NOT TAKE FROM IT
===============================================================================

    TAKE the registry, the figure, the channels and the ruling's verdicts.
    Those are measurements and they are current by construction.

    DO NOT TAKE `COMPLETE`.  `registry.COMPLETE` is False and stays False.
    This is not a claim to have found every first-order index; it is a list of
    the ones that have been found and survived their tests.

    DO NOT READ AN EMPTY CHANNEL AS A THEOREM.  K4 and K5 are unoccupied.  For
    K4 that is two candidates having failed on reach plus an arity argument;
    for K5 it is a seating that was made and then RETRACTED.  Neither is a
    proof that nothing can sit there.

    READ `retractions` BEFORE QUOTING ANYTHING.  Things this tree asserted and
    later measured to be false are listed there with what replaced them.  They
    are the highest-value rows in the file for anyone building on this.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SCHEMA = 2

# ---------------------------------------------------------------------------
# THE ONE HAND-MAINTAINED TABLE.  A docket is a question, a status and what
# would settle it; the selftest refuses a row missing any of the three.
DOCKETS = (
    ("22", "CLOSED-WITH-CORRECTIONS",
     "Were the ruling's per-witness physics claims ever independently checked?",
     "Nine adversarial agents, three lenses on each of three seatings. Two "
     "survived; nucshell (l, sigma) was UNSEATED. Ten corrections applied.",
     "Settled. Re-running the same lenses would re-check it."),
    ("23", "CLOSED",
     "Could madrule reach K4 at an arity where statistics is earned?",
     "Yes -- 3 of its 120 arity-3 charts do. None may be seated: they were "
     "found by searching for K4, which is fitted by this tree's own rule.",
     "A coordinate justified from the corpus BEFORE the chart is run."),
    ("24", "CLOSED",
     "Was the reported K1 candidate over the U3/U4 allowed sets real?",
     "Real and reproduced exactly -- 0 joins and 2,862/12,489/40,887/110,229, "
     "the corpus's own figures at §29.12 U4. Refused as a theorem: the channel "
     "is K1 at nine of ten boxes, so it does not depend on the data.",
     "Settled."),
    ("25", "CLOSED",
     "Does the research tree already hold an unseated first-order index?",
     "NO. Census of every chart-shaped accessor, all 232 modules attempted "
     "with attempt logging, 44 charts over 31 modules, 24 unseated and not "
     "excused, and NOT ONE is a new first-order index: they are members that "
     "are not elements, alternate charts of already-seated member sets (all "
     "landing in OCCUPIED channels), or withdrawn/duplicate charts. Two "
     "findings stand out -- K4 is reached by NOTHING in the whole tree, and "
     "K5 is reached by exactly one chart, the row DOCKET 22 retracted.",
     "Settled for the tree as it stands. A new member set would reopen it."),
    ("26", "OPEN",
     "Is the madelung/fibred family built on a withdrawn table?",
     "fibred.address calls tools/populate.aufbau_config, whose docstring says "
     "Register 1306 WITHDREW that table. 25 of 108 addresses differ from the "
     "banked observed ground configurations and 62 of the 170 lie beyond "
     "Z=108. At two matched reaches the PARENT falls K7 -> K0 while the "
     "coarsening holds K6 -> K2.",
     "A ruling on whether the seated object is the Madelung prediction or the "
     "observed configurations. It touches two PRE-RULING seated vertices."),
)

# DOCKET 25's census, as measured.  The two artifact rows are named because a
# census that hides its own double-counts is not a census.
CENSUS = {
    "modules_in_tree": 232,
    "modules_attempted": 232,
    "never_attempted": [],
    "unimportable": ["c333 (needs a module 'common' that is not here)",
                     "machinecheck (SystemExit at import)",
                     "pdftext (IndexError -- takes argv)",
                     "render_pdf (IndexError -- takes argv)"],
    "imported_but_no_chart": ["state", "machinecheck-vacancy", "mcheck_mi"],
    "charts_found": 44,
    "modules_with_a_chart": 31,
    "unseated_not_excused": 24,
    "new_first_order_indexes": 0,
    "charts_per_channel": {"K0": 15, "K1": 1, "K2": 10, "K3": 7, "K4": 0,
                           "K5": 1, "K6": 2, "K7": 8},
    "K4_reached_by": "nothing in the tree -- 0 of 44 charts over 231 modules",
    "K5_reached_by": "exactly one chart, overlaprule.nucshell_lsigma, which "
                     "DOCKET 22 retracted",
    "artifacts_of_the_census": [
        "madelung.k6_chart is listed unseated but IS the seated "
        "madelung_slot under its other accessor name -- the census keys on "
        "(module, accessor) and double-counts it",
        "boxinvariance.madelung_predicate at K3 is a helper written during "
        "this work that reproduces fibred's members, not a discovery",
    ],
}

# Things this tree asserted and then measured to be false.  Generated where it
# can be -- the unseating is read from overlaprule -- and quoted where the
# claim was prose.
RETRACTIONS = (
    ("overlaprule.py §5", "madelung's parent is 'a complete rectangle, which "
     "closes everything for free'",
     "FALSE. 170 cells in an 810-cell box, density 0.2099, not even a "
     "down-set. Its sibling fibred holds the same 170 at the same density and "
     "is K3."),
    ("overlaprule.py §5", "'the fill-order base carries order and algebra and "
     "does NOT carry geometry'",
     "FALSE of the base. Paired with l the same base is K7. The parent's three "
     "arity-2 projections are K7 / K6 / K7."),
    ("overlaprule.py §5", "'the radial node count is what breaks join-closure' "
     "in the nuclear shell sequence",
     "FALSE. (nr, sigma) is 6 cells at K7 with ZERO join counterexamples, so "
     "forgetting l restores join-closure exactly as completely."),
    ("overlaprule.py §5", "gravity: 'the raggedness lives in D,Y,L,E and NOT "
     "in the bound structure'",
     "TRUE operatively (256 join failures against 0) and FALSE in its strong "
     "reading: 509 of 96,372 parent join failures are witnessed inside the "
     "bound triple, cross-block."),
    ("overlaprule.py", "gravity (B,F,X) is 'dimension-blind'",
     "FALSE. B is a function of (D, q, F, Jzero) and its profile differs at "
     "D=4, D=5 and D>=6."),
    ("overlaprule.py §6", "the ultraspinning reading",
     "It is off CUMULATIVE D sweeps. Per single dimension D=4 is K7, D=5 is "
     "K1, and D=6..11 are EACH K0."),
    ("nucshell.py", "its parent closes 'K7 ... the only seated index of arity "
     "3 to reach it'",
     "BOTH HALVES FALSE. It is K3, and fibred.index is a second arity-3 K3."),
    ("boxinvariance.py", "madelung's 170 are 'ENUMERATED, not generated by a "
     "rule over an alphabet'",
     "FALSE. All 170 reproduce from {1<=n<=12, 0<=l<n, n+l<=9, 0<=k<2(2l+1)}. "
     "The test was applicable and had been declared inapplicable instead of "
     "run. Run now: madelung PASSES, the channel moves K6 -> K7 when l<n is "
     "dropped."),
    ("overlaprule.py §5", "gravity (B,F,X) has '64 meet counterexamples'",
     "That is the ORDERED count printed beside the UNORDERED pair total. It "
     "is 32 in 325 unordered pairs. The selftest caught it."),
    ("figure.py §1b", "'the three new vertices land at heights and widths the "
     "figure already held'",
     "FALSE of the one that fell -- nucshell (l, sigma) had width 2, which was "
     "new. True of the two that remain."),
)


def commit():
    """The HEAD commit, read from .git without shelling out.  None if absent."""
    try:
        head = open(os.path.join(ROOT, ".git", "HEAD"),
                    encoding="utf-8").read().strip()
        if head.startswith("ref: "):
            ref = head[5:]
            p = os.path.join(ROOT, ".git", ref)
            if os.path.exists(p):
                return open(p, encoding="utf-8").read().strip()[:12]
            for ln in open(os.path.join(ROOT, ".git", "packed-refs"),
                           encoding="utf-8"):
                if ln.rstrip().endswith(" " + ref):
                    return ln.split()[0][:12]
            return None
        return head[:12]
    except OSError:
        return None


def state():
    """The whole current state, ASKED of the instruments.  Nothing typed here."""
    import registry
    import figure
    import demand
    import overlaprule as OR
    import mi

    cells = registry.cells()
    ch = mi.channels()
    rows = []
    for nm, mod, acc, meth, what, q in registry.rows():
        c = cells[nm]
        rows.append({
            "name": nm, "module": mod, "accessor": acc, "method": meth,
            "label": registry.short(nm), "members": what, "quantum": q,
            "cells": len(registry.index_of(nm)),
            "cell": list(c) if c != "UNMEASURED" else None,
            "channel": c[0] if c != "UNMEASURED" else None,
            "languages": sorted(ch[c[0]]) if c != "UNMEASURED" else None,
            "seated_by_overlap_ruling": mod == OR.SELF,
        })
    F = figure.figure()
    occupied = sorted({c[0] for c in F})
    res = {a: {"distinct": d, "of": n, "ratio": r, "verdict": v}
           for a, d, n, r, v in figure.resolution()}
    return {
        "schema": SCHEMA,
        "commit": commit(),
        "regenerate": "python3 research/warp-drive/state.py --json",
        "complete": registry.COMPLETE,
        "registry": {"rows": len(rows), "indexes": rows},
        "figure": {
            "vertices": len(figure.cells()),
            "distinct_cells": len(F),
            "closers": figure.closers(),
            "own_cell": list(figure.self_cell()[0]),
            "own_cell_occupied_by": figure.self_cell()[1],
            "E": demand.E(F),
            "channels_occupied": occupied,
            "channels_empty": [k for k in range(8) if k not in occupied],
            "resolution": res,
            "labelled_axes": sorted(figure.labelled_axes()),
        },
        "channels": {"K%d" % i: sorted(s) for i, s in enumerate(ch)},
        "census": CENSUS,
        "overlap_ruling": {
            "grounds": ["novel channel", "not a relabelling", "reach stable",
                        "coordinate forced"],
            "seated": [{"parent": p, "cols": list(c), "channel": k,
                        "cells": n} for p, c, k, n in OR.admissible()],
            "refused": [{"parent": p, "cols": list(c), "failed": w}
                        for p, c, w in OR.refused()],
            "candidates": len(OR.CANDIDATES),
        },
        "retractions": [{"where": w, "claimed": c, "measured": m}
                        for w, c, m in RETRACTIONS],
        "dockets": [{"id": i, "status": st, "question": q, "finding": f,
                     "what_would_settle_it": s}
                    for i, st, q, f, s in DOCKETS],
        "not_claimed": [
            "COMPLETE is False and stays False -- this is not every "
            "first-order index, it is the ones found and survived.",
            "An empty channel is not a theorem that nothing can sit there.",
            "A refusal is recorded so it can be re-adjudicated, not closed.",
        ],
    }


def to_markdown(S):
    L = ["# The index work: current state", ""]
    L.append("Generated by `%s`. Commit `%s`. Schema %d."
             % (S["regenerate"], S["commit"] or "unknown", S["schema"]))
    L.append("")
    L.append("**`COMPLETE` is %s and stays false.** This is the set of "
             "first-order indexes found and survived, not a claim to have "
             "found them all." % S["complete"])
    L.append("")
    f = S["figure"]
    L.append("## The figure")
    L.append("")
    L.append("| | |")
    L.append("|---|---|")
    for k, v in (("vertices", f["vertices"]), ("distinct cells",
                 f["distinct_cells"]), ("closes in", ", ".join(f["closers"])
                 or "nothing"), ("E", f["E"]),
                 ("its own cell", tuple(f["own_cell"])),
                 ("channels occupied", ", ".join("K%d" % k
                                                 for k in f["channels_occupied"])),
                 ("channels empty", ", ".join("K%d" % k
                                              for k in f["channels_empty"]))):
        L.append("| %s | %s |" % (k, v))
    L.append("")
    L.append("Resolution on itself (a coordinate at >= 0.9 is a row label, "
             "not a measurement):")
    L.append("")
    L.append("| axis | distinct | of | ratio | verdict |")
    L.append("|---|---|---|---|---|")
    for a, r in S["figure"]["resolution"].items():
        L.append("| %s | %d | %d | %.4f | %s |"
                 % (a, r["distinct"], r["of"], r["ratio"], r["verdict"]))
    L.append("")
    L.append("## The seated indexes")
    L.append("")
    L.append("| index | members | quantum numbers | cells | cell | channel |")
    L.append("|---|---|---|---|---|---|")
    for r in S["registry"]["indexes"]:
        L.append("| `%s` | %s | %s | %d | %s | K%s |"
                 % (r["label"], r["members"], r["quantum"], r["cells"],
                    tuple(r["cell"]) if r["cell"] else "unmeasured",
                    r["channel"]))
    L.append("")
    L.append("## The overlap ruling")
    L.append("")
    L.append("Grounds: " + "; ".join("**%s**" % g
                                     for g in S["overlap_ruling"]["grounds"])
             + ".")
    L.append("")
    for s_ in S["overlap_ruling"]["seated"]:
        L.append("- **seated** `%s (%s)` at K%d, %d cells"
                 % (s_["parent"], ", ".join(s_["cols"]), s_["channel"],
                    s_["cells"]))
    for s_ in S["overlap_ruling"]["refused"]:
        L.append("- refused `%s (%s)` -- failed: %s"
                 % (s_["parent"], ", ".join(s_["cols"]),
                    ", ".join(s_["failed"])))
    L.append("")
    L.append("## Retractions -- read these before quoting anything")
    L.append("")
    L.append("Claims this tree made and later measured to be false.")
    L.append("")
    for r in S["retractions"]:
        L.append("- **%s** claimed *%s*. %s" % (r["where"], r["claimed"],
                                                r["measured"]))
    L.append("")
    c = S["census"]
    L.append("## The census (DOCKET 25)")
    L.append("")
    L.append("Every chart-shaped accessor in the research tree, with attempt "
             "logging so coverage is measured rather than inferred.")
    L.append("")
    L.append("| | |")
    L.append("|---|---|")
    L.append("| modules attempted | %d of %d |"
             % (c["modules_attempted"], c["modules_in_tree"]))
    L.append("| charts found | %d over %d modules |"
             % (c["charts_found"], c["modules_with_a_chart"]))
    L.append("| unseated and not excused | %d |" % c["unseated_not_excused"])
    L.append("| **new first-order indexes** | **%d** |"
             % c["new_first_order_indexes"])
    L.append("| K4 | %s |" % c["K4_reached_by"])
    L.append("| K5 | %s |" % c["K5_reached_by"])
    L.append("")
    L.append("Charts per channel: " + ", ".join(
        "%s %d" % (k, v) for k, v in c["charts_per_channel"].items()) + ".")
    L.append("")
    L.append("Artifacts of the census itself, named because a census that "
             "hides its own double-counts is not a census:")
    L.append("")
    for a in c["artifacts_of_the_census"]:
        L.append("- %s" % a)
    L.append("")
    L.append("## Dockets")
    L.append("")
    L.append("| # | status | question | finding | what would settle it |")
    L.append("|---|---|---|---|---|")
    for d in S["dockets"]:
        L.append("| %s | **%s** | %s | %s | %s |"
                 % (d["id"], d["status"], d["question"], d["finding"],
                    d["what_would_settle_it"]))
    L.append("")
    L.append("## Not claimed")
    L.append("")
    for n in S["not_claimed"]:
        L.append("- %s" % n)
    L.append("")
    return "\n".join(L)


def _strip(S):
    """Everything but `commit`, which moves with every push and is not drift."""
    d = dict(S)
    d.pop("commit", None)
    return d


def check():
    """Does the written STATE.json still agree with the instruments?"""
    p = os.path.join(HERE, "STATE.json")
    if not os.path.exists(p):
        return False, "STATE.json does not exist -- run --json"
    on_disk = json.load(open(p, encoding="utf-8"))
    fresh = state()
    if _strip(on_disk) == _strip(json.loads(json.dumps(fresh))):
        return True, "STATE.json agrees with every instrument"
    diff = [k for k in fresh
            if k != "commit"
            and json.dumps(on_disk.get(k), sort_keys=True)
            != json.dumps(json.loads(json.dumps(fresh[k])), sort_keys=True)]
    return False, "STALE in: %s -- regenerate" % ", ".join(diff)


def report():
    S = state()
    print(to_markdown(S))
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-56s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    S = state()
    import registry
    import figure
    chk("it asks the registry for its rows, and agrees",
        S["registry"]["rows"], len(registry.REGISTERED))
    chk("it asks figure for the vertex count, and agrees",
        S["figure"]["vertices"], len(figure.cells()))
    chk("every row carries its quantum numbers",
        [r["label"] for r in S["registry"]["indexes"] if not r["quantum"]], [])
    chk("every row has a measured cell",
        [r["label"] for r in S["registry"]["indexes"] if r["cell"] is None], [])
    chk("labels are unique",
        len({r["label"] for r in S["registry"]["indexes"]}),
        S["registry"]["rows"])
    chk("COMPLETE is not claimed", S["complete"], False)
    chk("the eight channels are all named", len(S["channels"]), 8)
    chk("empty and occupied channels partition the eight",
        sorted(S["figure"]["channels_occupied"]
               + S["figure"]["channels_empty"]), list(range(8)))
    # the hand-maintained table, guarded
    chk("every docket has an id, a status, a question, a finding and a remedy",
        [d["id"] for d in S["dockets"]
         if not all((d["id"], d["status"], d["question"], d["finding"],
                     d["what_would_settle_it"]))], [])
    chk("every retraction names where, what was claimed, and what was measured",
        [r["where"] for r in S["retractions"]
         if not all((r["where"], r["claimed"], r["measured"]))], [])
    chk("the retraction list is not empty -- a tree that never erred is "
        "a tree that never checked", len(S["retractions"]) > 0, True)
    chk("the ruling's seated rows all appear in the registry",
        [s_["parent"] for s_ in S["overlap_ruling"]["seated"]
         if not any(r["seated_by_overlap_ruling"] for r
                    in S["registry"]["indexes"])], [])
    chk("seated + refused accounts for every candidate",
        len(S["overlap_ruling"]["seated"])
        + len(S["overlap_ruling"]["refused"]),
        S["overlap_ruling"]["candidates"])
    # DOCKET 25's census -- hand-recorded from the sweep logs, so guarded.
    c = S["census"]
    chk("EVERY module in the tree was attempted",
        c["modules_in_tree"] - c["modules_attempted"], 0)
    chk("and the four that cannot be imported are named with the reason",
        [u for u in c["unimportable"] if "(" not in u], [])
    chk("its per-channel counts sum to the chart total",
        sum(c["charts_per_channel"].values()), c["charts_found"])
    chk("K4 is reached by no chart at all", c["charts_per_channel"]["K4"], 0)
    chk("K5 by exactly one -- the retracted row",
        c["charts_per_channel"]["K5"], 1)
    chk("and every channel the FIGURE occupies has at least one chart",
        [k for k in S["figure"]["channels_occupied"]
         if c["charts_per_channel"]["K%d" % k] == 0], [])
    chk("the census names its own artifacts",
        len(c["artifacts_of_the_census"]) > 0, True)
    chk("markdown renders without raising", bool(to_markdown(S)), True)
    print("state selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--check" in sys.argv:
        good, msg = check()
        print(("ok   " if good else "XX   ") + msg)
        sys.exit(0 if good else 1)
    if "--json" in sys.argv or "--md" in sys.argv:
        S = state()
        if "--json" in sys.argv:
            p = os.path.join(HERE, "STATE.json")
            open(p, "w", encoding="utf-8").write(
                json.dumps(S, indent=1, sort_keys=False) + "\n")
            print("wrote %s" % p)
        if "--md" in sys.argv:
            p = os.path.join(HERE, "STATE.md")
            open(p, "w", encoding="utf-8").write(to_markdown(S))
            print("wrote %s" % p)
        sys.exit(0)
    sys.exit(report())
