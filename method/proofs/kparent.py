"""E-012's two remaining items: register 434's paired populations, and K's parents.

DEFERRED's chat-76 line files three sites against §12.11.1, "for R3, no withdrawal":

  12q-03  register 434's "12.7 % against 31.4 %" pairs two populations.
  12s-02  register 241's "the two-thirds §12.11.1 states as nominal" -- SEATED at
          register 1874, and not re-opened here.
  12q-04  register 1790's edge count reads K with TWO parents.
  12s-04  the main volume's "K's parents are J_c and f" is the same reading inside
          §12.11.1.

WHAT THE VOLUME ALREADY SAYS, WHICH IS WHY THIS IS A CONTRADICTION AND NOT A DOUBT.
§12.11.1's own vocabulary block defines the term:

    "f_max -- the cap on f under section 7.4, NOT the cell's own f.  The distinction
     is the whole of section 12.11.5: the bound 2K <= 2J_c + 2f_max HAS ONE PARENT
     and preserves the tree and the cylinder; the same bound written with the cell's
     f has two parents and breaks the factorisation."

So the book states which reading is right.  Two places then use the other one.

WHAT IS MEASURED
  1. The three sites, located by CONTENT and not by the line numbers the chat-76
     note carries, which the volume has moved past.
  2. The constraint graph under both readings, built by the seated cgraph
     instrument with only its axis-12 edge list changed -- nothing else touched.
  3. What survives the correction and what does not.

INPUT
  method/proofs/cgraph.py -- imported by path for the graph; the edge model is
  substituted, never rewritten.
  method/members/The_Method_1_6-2.md and ...___The_Register-2.md.

REFUSALS
  It does not decide whether register 1790 should be corrected by an appended
  entry or whether Figure 21.1 should be redrawn.  1790 itself says the figure is
  "owed at the prose pass"; this measures the edge and stops.

  It does not touch the triangle.  2S'-g-v is untouched by either reading, so
  section 21.5.1's one-level shortfall -- R at level 2 against strong
  3-consistency -- stands under both, and the program says so rather than letting
  a reader infer that a falling cycle rank weakens it.

  It offers no verdict on register 434's underlying densities.  Whether 12.7 % is
  the right numerator is section 12.11.5's question; what is measured here is that
  the two percentages 434 pairs are computed over different populations, and that
  the volume's own sentence pairs the like-for-like ones.

  Nothing is repaired.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, importlib.util, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")
MAIN = os.path.join(MEM, "The_Method_1_6-2.md")
REG = os.path.join(MEM, "The_Method_1_6___The_Register-2.md")
STAGES = (8, 9, 10, 11, 12, 13)


def load_cgraph():
    spec = importlib.util.spec_from_file_location("cgraph", os.path.join(HERE, "cgraph.py"))
    m = importlib.util.module_from_spec(spec)
    sys.modules["cgraph"] = m
    spec.loader.exec_module(m)
    return m


def find(path, needle):
    """Line numbers carrying a string -- located by content, never by a stale number."""
    return [i for i, l in enumerate(open(path, encoding="utf-8").read().split("\n"), 1)
            if needle in l]


def entry(n):
    t = open(REG, encoding="utf-8").read()
    i = t.index("### %d\n" % n)
    return t[i:t.index("\n### ", i + 1)]


def shape(m):
    """nodes, edges, cycle rank, triangles, girth at each stage of the tower."""
    out = []
    for st in STAGES:
        V, E, adj = m.graph(st)
        out.append({"stage": st, "nodes": len(V), "edges": len(E),
                    "cycle_rank": len(E) - len(V) + m.components(V, adj),
                    "triangles": len(m.triangles(V, adj)), "girth": m.girth(V, adj),
                    "deg": {v: len(adj[v]) for v in V}})
    return out


def both_readings():
    m = load_cgraph()
    two = shape(m)
    m.EDGES_BY_STAGE[12] = [("2Jc", "2K")]      # f_max is a cap, so K has ONE parent
    one = shape(m)
    return m, two, one


def report():
    print("E-012's TWO REMAINING ITEMS")
    print()
    print("12q-03  REGISTER 434 PAIRS TWO POPULATIONS")
    e = entry(434)
    print("   434 prints        : %s" % ("12.7% against 31.4%" if "12.7% against 31.4%" in e
                                         else "(not found as written)"))
    for ln in find(MAIN, "12.7% against 30.8%"):
        print("   the volume prints : main L%d, 12.7%% against 30.8%%, 'an eighteen-point gap'" % ln)
    for ln in find(MAIN, "31.4% over"):
        print("   and 31.4%% is       : main L%d, the value over the stage below -- the STATED value" % ln)
    print("   30.8 - 12.7 = %.1f, which is the eighteen points the volume names." % (30.8 - 12.7))
    print("   31.4 - 12.7 = %.1f, which is what 434's pairing gives." % (31.4 - 12.7))
    print("   The numerator is the double-charged figure over one population; 31.4 %% is the")
    print("   density over another. The volume pairs like with like and 434 does not.")
    print()

    print("12q-04 / 12s-04  K's PARENTS")
    for ln in find(MAIN, "the cap on f under"):
        print("   the definition    : main L%d -- f_max is the cap, NOT the cell's own f" % ln)
    for ln in find(MAIN, "has one parent"):
        print("   and it says       : main L%d -- the bound 'has one parent'" % ln)
    for ln in find(MAIN, "K's parents are J_c and"):
        print("   the other reading : main L%d -- \"K's parents are J_c and f\"  (12s-04)" % ln)
    e = entry(1790)
    print("   register 1790     : second cycle 2Jc-2K-f-g-q-k present: %s  (12q-04)"
          % ("2Jc–2K–f–g–q–k" in e))
    print()

    m, two, one = both_readings()
    print("   THE GRAPH UNDER BOTH READINGS")
    print("   stage   two parents (as 1790 counts)      one parent (as the volume defines)")
    for a, b in zip(two, one):
        print("   L%-4d  %2d nodes %2d edges rank %d tri %d   %2d nodes %2d edges rank %d tri %d"
              % (a["stage"], a["nodes"], a["edges"], a["cycle_rank"], a["triangles"],
                 b["nodes"], b["edges"], b["cycle_rank"], b["triangles"]))
    print()
    print("   register 1790 prints %d nodes, %d edges, cycle rank %s"
          % (m.PRINTED_1790["nodes"], m.PRINTED_1790["edges"],
             m.PRINTED_1790["cycle_rank_by_stage"]))
    print("   -- which is the TWO-parent column exactly.")
    print()
    print("   WHAT THE CORRECTION COSTS AND WHAT IT DOES NOT")
    print("   edges at L13                  : %d -> %d" % (two[-1]["edges"], one[-1]["edges"]))
    print("   cycle rank by stage           : %s -> %s"
          % (tuple(x["cycle_rank"] for x in two), tuple(x["cycle_rank"] for x in one)))
    print("   triangles by stage            : %s -> %s   UNCHANGED"
          % (tuple(x["triangles"] for x in two), tuple(x["triangles"] for x in one)))
    print("   hub k / g degree              : %d, %d -> %d, %d   UNCHANGED"
          % (two[-1]["deg"]["k"], two[-1]["deg"]["g"], one[-1]["deg"]["k"], one[-1]["deg"]["g"]))
    moved = {v: (two[-1]["deg"][v], one[-1]["deg"][v])
             for v in two[-1]["deg"] if two[-1]["deg"][v] != one[-1]["deg"][v]}
    print("   degrees that move at all      : %s" % moved)
    print("   So the SECOND CYCLE falls and nothing else does: the triangle 2S'-g-v,")
    print("   the treewidth of 2 and section 21.5.1's one-level shortfall all stand.")
    print()
    print("RECORDED, NOT REPAIRED.")


def selftest():
    ok = 0

    def chk(name, got, want):
        nonlocal ok
        assert got == want, "%s: got %r, want %r" % (name, got, want)
        print("  ok  %-58s %s" % (name, want))
        ok += 1

    # 12q-03, both sites located by content.
    chk("434 pairs 12.7 with 31.4", "12.7% against 31.4%" in entry(434), True)
    chk("the volume pairs 12.7 with 30.8", len(find(MAIN, "12.7% against 30.8%")), 1)
    chk("and calls that gap eighteen points", len(find(MAIN, "an eighteen-point gap")), 1)
    chk("30.8 - 12.7 rounds to eighteen", round(30.8 - 12.7), 18)
    chk("31.4 is the density over the stage below", len(find(MAIN, "31.4% over")), 1)

    # 12s-04 and the definition it contradicts, in the same chapter.
    chk("the volume defines f_max as the cap", len(find(MAIN, "the cap on f under")), 1)
    chk("and says the bound has one parent", len(find(MAIN, "has one parent")), 1)
    chk("and elsewhere gives K two parents", len(find(MAIN, "K's parents are J_c and")), 1)
    d = find(MAIN, "the cap on f under")[0]
    p = find(MAIN, "K's parents are J_c and")[0]
    chk("the two are in that order, definition first", d < p, True)

    # 12q-04: 1790's second cycle is the two-parent reading.
    chk("1790 names the second cycle through f", "2Jc–2K–f–g–q–k" in entry(1790), True)

    m, two, one = both_readings()
    chk("the two-parent graph is what 1790 prints",
        (two[-1]["nodes"], two[-1]["edges"]), (m.PRINTED_1790["nodes"], m.PRINTED_1790["edges"]))
    chk("and its cycle rank by stage is 1790's",
        tuple(x["cycle_rank"] for x in two), m.PRINTED_1790["cycle_rank_by_stage"])
    chk("the one-parent graph has one edge fewer", one[-1]["edges"], two[-1]["edges"] - 1)
    chk("its cycle rank by stage", tuple(x["cycle_rank"] for x in one), (0, 0, 1, 1, 1, 1))
    chk("the triangle count is the same under both",
        tuple(x["triangles"] for x in two), tuple(x["triangles"] for x in one))
    chk("and it is 1790's triangle count",
        tuple(x["triangles"] for x in one), m.PRINTED_1790["triangles_by_stage"])
    chk("only 2K and f change degree",
        sorted(v for v in two[-1]["deg"] if two[-1]["deg"][v] != one[-1]["deg"][v]),
        ["2K", "f"])
    chk("the hub k keeps degree 4", (two[-1]["deg"]["k"], one[-1]["deg"]["k"]), (4, 4))
    chk("Lambda_8 is a tree under both", (two[0]["edges"], one[0]["edges"]), (7, 7))

    # 12s-02 is seated and is not re-opened.
    chk("12s-02's successor, register 1874, is seated",
        "### 1874\n" in open(REG, encoding="utf-8").read(), True)

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    selftest() if a.selftest else report()
