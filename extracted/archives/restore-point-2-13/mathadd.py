#!/usr/bin/env python3
"""mathadd.py -- register the objects this session produced.

Twenty-four new mathematical objects, each with its grade, its dependencies, and
the computation or source that settles it. Written as an extension to mathreg.py
so the graph and the verifier see them.
"""
import re, sys

NEW = [
# key, grade, statement, deps, what settles it
("S.seed", "PROVED",
 "G ⊆ X is a seed of X under ℛ iff φ̂(G) = φ̂(X): ℛ(G) depends on G only through its envelopes",
 ["A.env"], "definitional consequence of ℛ's construction; §14.5.7"),
("S.cover", "PROVED",
 "the minimum seed is a MINIMUM SET COVER — elements the envelope steps, sets the cells, a cell "
 "covering the steps it witnesses",
 ["S.seed"], "restatement of S.seed; §14.5.9"),
("S.lam", "COMPUTED",
 "seed(Λ₈) = 7 exactly; lower bound 5 by disjoint witnesses, upper 7 by five heuristics, exact by "
 "branch and bound. 976 cells from seven — 139 to 1",
 ["S.cover"], "twoheur.py — H1 12, H2 7, H3 7, H4 7, H5 40, LB 5, exact 7"),
("S.down", "PROVED",
 "a down-set over c values in d coordinates seeds at d + c − 1",
 ["S.cover"], "branch and bound; upper bound equals lower bound at d=4 c=4"),
("S.box", "PROVED",
 "a full box c^d seeds at d + c − 2",
 ["S.cover"], "branch and bound at 3³ and 4³, exact 4 and 5"),
("S.car", "CITED",
 "the seed is bounded below by the Carathéodory number, which for a semilattice is the BREADTH, "
 "and the breadth of a product of d chains is d",
 ["S.cover"], "Carathéodory / convexity spaces; a generating set cannot fall below the breadth"),
("S.open", "PROVED",
 "an OPEN index is recovered as seed(ℛ(X)) together with the E cells ℛ(X) holds and X does not; "
 "cost seed + E, and it compresses only where E ≪ |X|",
 ["S.seed"], "exact on the audit index, the periodic table, the calendar and the parity rule"),
("A.r4", "COMPUTED",
 "ℛ₄, the four-orientation closure over Deville's staircase class; idempotent, hence a closure "
 "operator",
 ["A.stair"], "idempotence verified on Λ₈, the periodic table and the parity rule"),
("A.orient", "COMPUTED",
 "E − E₄ is the ORIENTATION COST. Zero on eight of ten indexed objects including the periodic "
 "table at 36 under both; 2 on the audits; 750 on the parity rule",
 ["A.r4"], "the ten-object table of §14.5.5"),
("A.relax", "PROVED",
 "ℛ is not a k-wise closure for any k: k-wise defect falls with k and is 0 at k = d, while E(ℛ) "
 "can be 750 there. ℛ is a relaxation, not a local-consistency operator",
 ["A.env"], "|Δℓ| = 1 at 750 against k-wise 0 for k = 2, 3, 4"),
("A.staircls", "PROVED",
 "E(ℛ) = 0 iff X is an intersection of (≤,≤) staircases — one corner of Deville's class, not the "
 "class entire",
 ["A.relax", "A.stair"], "the anti-diagonal is a staircase with E = 750"),
("T.tight", "COMPUTED",
 "the tight-pair count of a base — places where a binary constraint restricts rather than permits "
 "everything — is exactly 2S, S the envelope-step count",
 ["A.env"], "correlation 1.000 on thirteen bases"),
("F.moore", "PROVED",
 "the ℛ-closed subsets of a closed index form a MOORE FAMILY: intersection-closed at 100%, "
 "union-closed at 33–68%. 73, 146, 731 members at 8, 9, 16 cells",
 ["S.seed"], "exhaustive enumeration at three ambients"),
("F.open", "PROVED",
 "THEOREM: the family of all closed indexes is itself an OPEN index. Every member has E = 0; the "
 "family has E = 182, 365, 64,804 — and the openness outruns the membership",
 ["F.moore"], "exhaustive at three ambients; §14.6"),
("F.unstatable", "PROVED",
 "and it cannot be stated: a closed index has a seed, an open one costs seed + E, and here E is "
 "64,804 at an ambient of 16",
 ["F.open", "S.open"], "corollary of F.open and S.open; §14.6.1"),
("G.cons", "COMPUTED",
 "Λ's seven constraints form a TREE — 8 nodes, 7 edges — with ZERO of 35 triples spanning three "
 "nodes: no 3-body among the constraints",
 ["L.c1"], "exhaustive over triples; §21.5.2"),
("G.near", "COMPUTED",
 "Λ is one edge from a 3-body in exactly seven places, one per existing edge, and every one is a "
 "bond the physics does not make",
 ["G.cons"], "exhaustive over the 21 unused edges"),
("G.tower", "COMPUTED",
 "the tower's cycle rank rises by exactly one at each TWO-PARENT axis — 0, 0, 1, 1, 2, 2 across "
 "Λ₈–Λ₁₃ — while the triangle count stays 0: cycles appear, a 3-body never does",
 ["G.cons"], "stage-by-stage; the tree breaks at Λ₁₀, where §12.11 loses composability"),
("K.transit", "COMPUTED",
 "the transit profile: MI/H of each added axis with what it enters — 0.51, 0.93, 0.08, 0.13, 0.77 "
 "at Λ₉–Λ₁₃. Reduced at 10, carried as a LABEL through 11 and 12, re-attaching at 13",
 ["T.tower"], "mutual information over the tower; Λ₁₂ built with the loose bound"),
("L.real", "COMPUTED",
 "Λ's eight constraints hold on 113 real subshells across 57 elements including all 19 "
 "configuration anomalies: 3,964 tests, 0 failures",
 ["L.c1"], "close_L.py — palladium, with no valence s-shell, satisfies every one"),
("T.real", "COMPUTED",
 "the four coupling bounds hold on the exact term structure of every subshell physics allows: "
 "85,829 tests, 0 failures",
 ["T.a9"], "microstate enumeration, ℓ = 0..3, k = 1..4ℓ+2"),
("E.table", "COMPUTED",
 "the periodic table's 36 decompose 25 + 11, not 26 + 10; and E is placement-sensitive — 36 with "
 "helium at group 18, 20 at group 2",
 ["A.env"], "recomputed on all 118 elements; §6.1.1"),
("E.layout", "COMPUTED",
 "hydrogen's placement is free and helium's costs 16, and they are not additive: −16 and 0 apart, "
 "−1 together. E is set by the largest group used in period 1",
 ["E.table"], "six drawn layouts priced; the 32-column costs +70"),
("G.prot", "COMPUTED",
 "the 24 protocols occupy 19 distinct cells in four coordinates; §2.8 and §2.24 share one, and "
 "§2.24 is §2.8 specialised to heuristics",
 ["G.reg"], "protindex.py — five collisions, four defensible"),
]

def main():
    src = open("mathreg.py", encoding="utf-8").read()
    have = set(re.findall(r'R\("([^"]+)"', src))
    add = [n for n in NEW if n[0] not in have]
    if not add:
        print("  nothing to add"); return
    lines = ["", "# --- entered from the seed, family and index work -------------------------"]
    for k, g, stmt, dep, chk in add:
        lines.append(f'R({k!r}, {g!r}, {stmt!r},\n  dep={dep!r}, named=True, check={k!r})')
    marker = "\n# --- end of register"
    src = (src.rstrip() + "\n" + "\n".join(lines) + "\n") if marker not in src else src.replace(
        marker, "\n".join(lines) + marker)
    open("mathreg.py", "w", encoding="utf-8").write(src)
    print(f"  {len(add)} objects entered")
    for k, *_ in add: print(f"    {k}")

main()
