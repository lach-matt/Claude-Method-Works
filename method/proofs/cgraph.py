#!/usr/bin/env python3
"""cgraph.py — the tower's constraint graph, stage by stage, and what it decides about §21.5.1's
one-level shortfall. R3 completion item A5, on M's "complete R3 please".

WHY. Figure 21.1's caption says the shortfall "holds for the whole tower and not only for a K3".
Register 1790 measured the graph and recorded that the caption is wrong in four other places at the
same time — 12 nodes for 13, 13 edges for 14, girth 5 for 3, "no triangle at any stage" against one
triangle from L10 — and scoped the figure and 21.5.3's table to the prose pass. What 1790 did NOT
state, because it was measuring L13, is the consequence FOR THE CAPTION'S OWN SENTENCE: it prints
its own refutation two lines above, in the cycle-rank sequence.

WHAT IS MEASURED HERE. The graph is built from the axis bounds tower-2.py implements, not from the
drawing: an edge for every bound that ties one coordinate to another. Per stage it reports nodes,
edges, connectivity, cycle rank, girth, triangles, and TREEWIDTH computed exactly by minimum
elimination ordering over all orderings the graph is small enough to admit.

THE RULE THAT MAKES IT DECIDE ANYTHING. Freuder's bound: strong (w*+1)-consistency on induced width
w* gives a globally consistent network, and the Mathematical Compendium states the corollary that
treewidth 1 is exact closure under R. R gives level 2. So the shortfall is one level exactly where
treewidth is 2, and there is NO shortfall where treewidth is 1.

stdlib only.  --selftest asserts register 1790's own recorded numbers.
"""
import argparse, itertools, sys

# §12.11.1's axis bounds, as tower-2.py implements them. (a, b) = b is bounded by a.
EDGES_BY_STAGE = {
    8:  [("n", "l"), ("l", "k"), ("k", "q"), ("e", "f"), ("f", "g"), ("q", "g"), ("k", "2S")],
    9:  [("g", "2S'")],
    10: [("2S'", "v"), ("g", "v")],
    11: [("k", "2Jc")],
    12: [("2Jc", "2K"), ("f", "2K")],
    13: [("2K", "2J")],
}
NEW_NODE = {8: None, 9: "2S'", 10: "v", 11: "2Jc", 12: "2K", 13: "2J"}
PRINTED_1790 = {"nodes": 13, "edges": 14, "cycle_rank_by_stage": (0, 0, 1, 1, 2, 2),
                "triangles_by_stage": (0, 0, 1, 1, 1, 1), "girth": 3, "hub": ("k", 4)}
CAPTION = {"nodes": 12, "edges": 13, "girth": 5, "triangles": 0, "cycle_rank": 2, "treewidth": 2}


def graph(upto):
    E = []
    for s in sorted(EDGES_BY_STAGE):
        if s <= upto:
            E += EDGES_BY_STAGE[s]
    V = sorted({x for e in E for x in e})
    adj = {v: set() for v in V}
    for a, b in E:
        adj[a].add(b); adj[b].add(a)
    return V, E, adj


def components(V, adj):
    seen, n = set(), 0
    for v in V:
        if v in seen: continue
        n += 1; stack = [v]
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen.add(x); stack += [y for y in adj[x] if y not in seen]
    return n


def triangles(V, adj):
    return [(a, b, c) for a, b, c in itertools.combinations(sorted(V), 3)
            if b in adj[a] and c in adj[a] and c in adj[b]]


def girth(V, adj):
    best = None
    for s in V:                                  # BFS from every node; smallest cycle through it
        dist = {s: 0}; par = {s: None}; q = [s]
        while q:
            x = q.pop(0)
            for y in adj[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1; par[y] = x; q.append(y)
                elif y != par[x]:
                    c = dist[x] + dist[y] + 1
                    best = c if best is None else min(best, c)
    return best


def treewidth(V, adj):
    """exact, by branch and bound over elimination orderings (13 nodes at most here)."""
    best = [len(V)]
    def rec(remaining, adjc, width):
        if width >= best[0]: return
        if not remaining:
            best[0] = width; return
        cand = sorted(remaining, key=lambda v: len(adjc[v] & remaining))
        for v in cand:
            nb = adjc[v] & remaining
            if len(nb) >= best[0]: continue
            a2 = {x: set(adjc[x]) for x in remaining if x != v}
            for x in nb:
                a2[x] |= (nb - {x})
                a2[x].discard(v)
            rec(remaining - {v}, a2, max(width, len(nb)))
    rec(set(V), {v: set(adj[v]) for v in V}, 0)
    return best[0]


def rows():
    out = []
    for s in range(8, 14):
        V, E, adj = graph(s)
        c = components(V, adj)
        tr = triangles(V, adj)
        out.append(dict(stage=s, nodes=len(V), edges=len(E), comps=c,
                        rank=len(E) - len(V) + c, tris=len(tr), tri=tr[0] if tr else None,
                        girth=girth(V, adj), tw=treewidth(V, adj)))
    return out


def report():
    R = rows()
    print("The tower's constraint graph, built from the axis bounds tower-2.py implements\n")
    print(f"  {'stage':>6} {'nodes':>6} {'edges':>6} {'cycle rank':>11} {'triangles':>10} "
          f"{'girth':>6} {'treewidth':>10}   shortfall?")
    for r in R:
        short = "ONE LEVEL" if r["tw"] >= 2 else "none — R is exact"
        g = r["girth"] if r["girth"] else "-"
        print(f"  Λ{r['stage']:<5} {r['nodes']:6} {r['edges']:6} {r['rank']:11} {r['tris']:10} "
              f"{str(g):>6} {r['tw']:10}   {short}")
    last = R[-1]
    print(f"\n  cycle rank by stage {tuple(r['rank'] for r in R)} "
          f"— register 1790 prints {PRINTED_1790['cycle_rank_by_stage']}")
    print(f"  triangles by stage  {tuple(r['tris'] for r in R)} "
          f"— register 1790 prints {PRINTED_1790['triangles_by_stage']}")
    print(f"  the triangle, first at Λ10: {R[2]['tri']}  — register 1790 names 2S'-g-v")
    print(f"  at Λ13: {last['nodes']} nodes, {last['edges']} edges, girth {last['girth']}, "
          f"treewidth {last['tw']} — register 1790 prints 13, 14, 3, 2")

    print("\nWHAT THIS DECIDES ABOUT FIGURE 21.1's CAPTION")
    print("  The caption prints: 'Twelve nodes, thirteen edges, cycle rank 2, girth 5, treewidth 2,")
    print("  and no triangle at any stage' and then '- the shortfall of one level holds for the whole")
    print("  tower and not only for a K3.'")
    print(f"  MEASURED: {last['nodes']} nodes, {last['edges']} edges, cycle rank {last['rank']}, "
          f"girth {last['girth']}, treewidth {last['tw']}, {last['tris']} triangles at Λ13.")
    tw1 = [r["stage"] for r in R if r["tw"] < 2]
    print(f"  AND: treewidth is 1 at Λ{', Λ'.join(str(s) for s in tw1)}, so R closes those stages")
    print("  exactly and there is no shortfall there. The caption's own cycle-rank sequence says so")
    print("  two lines above the sentence: the first cycle, and so the first K3, arrives at Λ10.")
    print("  'The whole tower' is false at Λ8 and Λ9; from Λ10 the sentence is right.")
    k8, k13 = len(graph(8)[2]["k"]), len(graph(13)[2]["k"])
    print(f"\n  A FIFTH CAPTION ERROR, measured here and not in register 1790, which was measuring Λ13:")
    print(f"  the caption says 'the base Λ8 is a caterpillar with k as its hub at degree {PRINTED_1790['hub'][1]}'.")
    print(f"  At Λ8 k has degree {k8} — l, q and 2S. It reaches {k13} only at Λ11, when 2Jc arrives.")
    print("\n  Register 1790 scopes Figure 21.1 and §21.5.3's table to the prose pass. This is the")
    print("  measurement that pass needs; nothing is repaired here.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    R = rows()
    last = R[-1]
    eq("Λ13 nodes (register 1790)", last["nodes"], PRINTED_1790["nodes"])
    eq("Λ13 edges (register 1790)", last["edges"], PRINTED_1790["edges"])
    eq("Λ13 girth (register 1790)", last["girth"], PRINTED_1790["girth"])
    eq("Λ13 treewidth (register 1790)", last["tw"], 2)
    eq("cycle rank by stage (register 1790)", tuple(r["rank"] for r in R),
       PRINTED_1790["cycle_rank_by_stage"])
    eq("triangles by stage (register 1790)", tuple(r["tris"] for r in R),
       PRINTED_1790["triangles_by_stage"])
    eq("the triangle is 2S'-g-v", tuple(sorted(R[2]["tri"])), tuple(sorted(("2S'", "g", "v"))))
    V, E, adj = graph(8)
    eq("Λ8 is a tree: 8 nodes, 7 edges", (len(V), len(E)), (8, 7))
    eq("Λ8 treewidth", treewidth(V, adj), 1)
    eq("Λ13 hub k has degree 4 (register 1790)", len(graph(13)[2]["k"]), PRINTED_1790["hub"][1])
    eq("Λ8 hub k has degree 3, NOT the caption's 4", len(adj["k"]), 3)
    V9, E9, adj9 = graph(9)
    eq("Λ9 treewidth", treewidth(V9, adj9), 1)
    eq("Λ10 treewidth", R[2]["tw"], 2)
    eq("stages with no shortfall", tuple(r["stage"] for r in R if r["tw"] < 2), (8, 9))
    eq("the caption's node count is not the graph's", CAPTION["nodes"] == last["nodes"], False)
    eq("the caption's girth is not the graph's", CAPTION["girth"] == last["girth"], False)
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
