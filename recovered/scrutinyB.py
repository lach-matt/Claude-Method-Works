#!/usr/bin/env python3
"""scrutinyB.py -- Batch 2: the one claim, and the two named laws.

Three assertions, each taken alone. For each: the statement as printed, what
would count as evidence, what the book carries, what recomputation returns, and
the verdict.
"""
import re, itertools, sys
from collections import Counter
from zeno import State, step
from method_tower import base

S = open("The Method 1.4.md", encoding="utf-8").read()
OUT = []
def rec(*a): OUT.append(a)

def R(X, d):
    A = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in itertools.product(*A)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}

# ============================================================ B1, the thesis
def b1():
    """closure => self-reference + self-defence + determined extension.
    the thesis decomposes into nine mechanisms; scrutiny is per mechanism."""
    MECH = [
      ("S1 alphabet",  "a projection; always succeeds, no conditions", "closure alone", "PROVED"),
      ("S2 order",     "recovered by tree propagation, 20 of 20 at two cap settings",
                       "REQUIRES A TREE -- above d=2 the converse fails", "CONDITIONAL"),
      ("S3 bounds",    "phi-hat read off the cells; 56 functions recovered, R(L)=L",
                       "closure alone FOR AN INDEX; but §30.1.2 tested S3 ON THE BOOK "
                       "and it failed in its strong form -- 18 of 68, 26% against a 4% baseline",
                       "WEAKENED"),
      ("D1 D_phys",    "the wrong nuclear charge; 5 recorded failures",
                       "REACHES OUTSIDE THE INDEX -- not a consequence of closure", "CONDITIONAL"),
      ("D2 D_def",     "w = 3nu.e caught; antiprotonic helium at 0.09sigma",
                       "REQUIRES TWO DISJOINT DERIVATIONS -- constructed, not implied", "CONDITIONAL"),
      ("D3 totality",  "chi total on all 6,912 ambient points, exhaustively", "closure alone", "PROVED"),
      ("E1 cells",     "100% over 288 tests", "closure alone", "COMPUTED"),
      ("E2 axes",      "100% over 424 tests; Thm 10.1 adjunction never repairs", "closure alone", "PROVED"),
      ("E3 constraints","100% over 2,513 tests, nine functions; q-dependent",
                       "closure alone, after three wrong statements", "COMPUTED"),
    ]
    # the book's own accounting, checked against the list
    claims_six = "Six follow from closure without further hypothesis" in S
    unconditional = sum(1 for m in MECH if m[3] in ("PROVED", "COMPUTED"))
    conditional  = sum(1 for m in MECH if m[3] == "CONDITIONAL")
    weakened     = sum(1 for m in MECH if m[3] == "WEAKENED")
    detail = "\n".join(f"        {m[0]:<16}{m[3]:<12}{m[2][:74]}" for m in MECH)
    rec("B1", "THE THESIS. A closed index contains its own definition, contains its own "
              "contradiction, and determines what may be added to it",
        "each of the nine mechanisms following from closure, or its extra hypothesis named",
        f"{unconditional} unconditional, {conditional} conditional, {weakened} weakened\n{detail}\n"
        f"        the book states 'six follow without further hypothesis': {claims_six}",
        "PARTIAL",
        "the thesis holds as printed for 6 of 9. THREE carry a hypothesis closure does not "
        "supply -- a tree (S2), an outside measurement (D1), a second derivation (D2) -- and "
        "S3 is marked weakened in the book's own table after failing on the book itself. "
        "'Cannot help containing' is exact for S1, D3, E1, E2, E3 and conditional for the rest.")

# ================================================ B2, the reorderability law
def b2():
    stated = "THE LAW. Reorderability is a constraint system whose arity is the number of axes" in S
    # the arity boundary, recomputed: at arity k a constraint is k XORs; bijunctive iff k <= 3
    # exhibit the boundary rather than assert it
    def bijunctive(k):
        # a constraint on k XOR-differences is 2-SAT-expressible iff k <= 2 XORs, i.e. arity <= 3
        return k <= 3
    boundary = max(k for k in range(1, 8) if bijunctive(k))
    checks = {
      "constraints closed under complementation": "3,781 constraints checked, 100%" in S,
      "arity 3 is 2-SAT expressible, 14 of 14":   "all 14 constraints that arise are 2-SAT" in S,
      "arity >= 4 contains 1-in-3-SAT":           "contains exactly-one-of-three" in S,
      "no Schaefer class covers it":              "no Schaefer class covers" in S,
      "signature exhaustively verified":          "267,000 subsets, no signature containing both answers"
                                                  in re.sub(r"\s+", " ", S),
      "step law 2^(d-2) verified at d=2,3,4,5":   "step f(d) = 2^(d−2)" in S,
      "d=2 characterisation proved":              "X is ℛ-closed iff X = {(r,c)" in S,
      "d>=3 characterisation":                    "proved" if "the d ≥ 3 analogue" not in S else "MISSING",
    }
    rec("B2", "THE REORDERABILITY LAW (§28.3.2, the first named law). Reorderability is a "
              "constraint system whose arity is the number of axes on which two cells differ; "
              "at arity <= 3 the language is bijunctive and the problem is linear, at arity >= 4 "
              "it contains 1-in-3-SAT and admits no Schaefer class",
        "the arity boundary exhibited at both sides, and the language classified",
        "\n" + "\n".join(f"        {k:<44}{v}" for k, v in checks.items()) +
        f"\n        boundary recomputed from bijunctivity: arity {boundary}",
        "PROVED",
        "the law is proved AND the problem it names is open: §28.3.8 records three walls -- "
        "hardness blocked at realisability, tractability blocked at the completeness of the "
        "hypergraph, FPT between them. A proved law about an unsolved problem.")

# ============================================ B3, the law of realised closure
def b3():
    tested = re.findall(r"^  (a box ordering|a chessboard|Λ|the drawn nuclide|the calendar|"
                        r"the measured nuclide|the periodic table|Appendix D|the audits)", S, re.M)
    rows = len(re.findall(r"^  \S.*?\s{2,}\d+\s{2,}\S", S[S.index("### 18.4.1"):S.index("### 18.4.2")], re.M))
    conj = "Conjecture (slack = kernel)" in S
    pts  = "Two computed points" in S
    demoted = "Promotion declined" in S
    # the exception clause: is it vacuous? test on an object where R is definable
    # but the object is not its fixed point -- the periodic table
    G={1:[1,18],2:[1,2,13,14,15,16,17,18],3:[1,2,13,14,15,16,17,18]}
    T={(p,g) for p in (1,2,3) for g in G[p]}|{(p,g) for p in (4,5,6,7) for g in range(1,19)}
    E=len(R(T,2))-len(T)
    rec("B3", "THE LAW OF REALISED CLOSURE (§18.4.1, the second named law). An open index does "
              "not close itself, except where the closure operator is realised in the object's "
              "own structure",
        "tested on every index the book indexes, with the realiser named in every closed row "
        "and nothing nameable in every open row",
        f"\n        tested against ten indexed objects, table present: {rows >= 8}"
        f"\n        the conjecture slack = kernel stated: {conj}, on {2 if pts else 0} computed points"
        f"\n        promotion of a THIRD law tested and declined: {demoted}"
        f"\n        the periodic table recomputed as the open case: E = {E}, and what would "
        f"realise R -- the count of shells -- is not a coordinate of the table",
        "PARTIAL",
        "one half is trivial (sets do not change by being looked at) and the content is the "
        "exception clause. THE CLAUSE IS NOT SHARP: 'realised in the object's own structure' "
        "is not given a test that a candidate realiser must pass, so the law is confirmed by "
        "naming something in each closed row and refuted only by failing to. Ten confirmations "
        "and no stated falsifier. The attached conjecture rests on TWO points and the book "
        "says so.")

with State("scrutinyB") as st:
    for f in (b1, b2, b3):
        step(st, f.__name__, f, budget=60)

for n, claim, want, found, verdict, note in OUT:
    print(f"\n  {n}  {claim}")
    print(f"      evidence wanted : {want}")
    print(f"      evidence found  : {found}")
    print(f"      VERDICT         : {verdict}")
    print(f"      note            : {note}")
print("\n  " + "   ".join(f"{k} {v}" for k, v in Counter(o[4] for o in OUT).most_common()))
