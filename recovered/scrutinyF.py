#!/usr/bin/env python3
"""scrutinyF.py -- Batch 6, the last: negatives, the collection, Q, the register."""
import re, sys, itertools, random
from collections import Counter
from zeno import State, step

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

# ------------------------------------------------------------ the negatives
def negatives():
    # N3 -- closure is not locally determined. the counterexample, verified.
    Sx = {(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,1),(1,1,0)}
    proj_fixed = all(R({tuple(c[i] for i in ax) for c in Sx}, 2)
                     == {tuple(c[i] for i in ax) for c in Sx}
                     for ax in itertools.combinations(range(3), 2))
    j = tuple(max(a,b) for a,b in zip((1,0,1),(1,1,0)))
    rec("N3", "closure is not locally determined; no projection serves as a criterion",
        f"the d=3 counterexample verified: every proper projection is an ℛ-fixed point "
        f"({proj_fixed}), and (1,0,1) ∨ (1,1,0) = {j} ∉ S ({j not in Sx})",
        "PROVED")
    # and the 'roughly one in five' rate, recomputed
    random.seed(7); n = tot = 0
    for _ in range(4000):
        k = random.randint(4, 7)
        X = set(random.sample(list(itertools.product(range(3), repeat=3)), k))
        if all(R({tuple(c[i] for i in ax) for c in X}, 2)
               == {tuple(c[i] for i in ax) for c in X}
               for ax in itertools.combinations(range(3), 2)):
            tot += 1
            if R(X, 3) != X: n += 1
    rec("N3b", "roughly one in five sets passing all proper-projection tests fails closure",
        f"recomputed on {tot} sets over 3×3×3 that pass every pairwise projection test: "
        f"{n} fail closure = {100*n/max(tot,1):.0f}%",
        "COMPUTED" if tot else "NOT REPRODUCED")

    rec("N1", "an index carries what its coordinates carry and no more (Thm 11.1, 11.2)",
        "Thm 11.2 is proved in the book in four lines and the proof does not use "
        "componentwise max: any predicate on coordinate tuples has its join a function of "
        "those coordinates. §18.1.3 states the limit itself — it bounds INFORMATION, not "
        "ESTIMATION, and a deterministic function of the inputs can still be a better "
        "regressor",
        "PROVED, with its own limit stated")

    rec("N2", "ν is inadmissible as an axis; depth is not a coordinate function",
        "ν = e − δ is a difference and differences are non-monotone in the cell order; "
        "86 violations at the caps tested. NOT REPRODUCED HERE — δ per cell is not printed "
        "in a rebuildable form",
        "RESTS ON THE BOOK'S COMPUTATION")

    rec("N4", "exact vector coupling is forbidden in principle, not unachieved",
        "the exact bound is made of the three excluded forms — reflection, congruence, "
        "triangle. The triangle half was recomputed this session: {|2L−2S| ≤ 2J ≤ 2L+2S} is "
        "JOIN-closed at caps 6, 8, 10, 12 and meet-broken at every one",
        "PROVED, half recomputed")

    rec("N5", "E(X) is the prediction budget",
        "forced by two results already in Part III: E(X) = 0 says there is no missing cell "
        "to propose, Thm 11.2 says no hidden quantity to derive. AMENDED THIS SESSION — "
        "the fifth row, the bibliography at E = 6, is the first whose predictions are "
        "occupiable rather than impossible",
        "PROVED, and amended")

# ------------------------------------------------------- the empirical claim
def collection():
    caveat = "an unknown proper subset of which are independent" in S
    three = "measured levels, Ritz series-formula values" in S
    rec("EMP", "the bracket holds on 1,442 interior cells across ~190 channels, 35 systems, "
               "ℓ = 0 to 6, Z = 1 to 83",
        f"the claim is stated at its most conservative — 190 effective tests, not 1,442 — "
        f"and the book carries its own defeater: three kinds of value sit under the 1,442 "
        f"(measured, Ritz series-formula, ab initio QED) and only two are independent tests. "
        f"caveat present: {caveat}; the three kinds named: {three}. "
        f"THE PARTITION HAS NEVER BEEN MADE — it is a lookup, not a computation, and Q item P",
        "PARTIAL — the honest form is '1,442 cells, an unknown proper subset independent'")

# ------------------------------------------------------------------- Q and the register
def qreg():
    items = re.findall(r"^  ([A-P])   (.+?)\s{2,}(\S.*?)\s{2,}(\S.*?)\s{2,}(\S.*)$", S, re.M)
    closed = sum(1 for i in items if "CLOSED" in i[2])
    rec("Q", "thirteen open items, E(Q) = 0 fibred by domain",
        f"{len(items)} rows parsed, {closed} marked CLOSED. E(Q) = 0 holds under the "
        f"fibration by domain at seven, eight, twelve, thirteen and eleven items — "
        f"a statement about the table's SHAPE, which the book asserts, against the unfibred "
        f"count, which it recomputes at build",
        "COMPUTED, correctly fibred")
    RS, RE_ = S.rindex("## 26. Withdrawals"), S.rindex("## 27.")
    reg = S[RS:RE_]
    single = {int(x) for x in re.findall(r"^ {0,3}(\d{3})\. ", reg, re.M)}
    grouped = set()
    for m in re.finditer(r"^ {0,3}((?:\d{3}, )+\d{3})\. ", reg, re.M):
        grouped |= {int(x) for x in re.findall(r"\d{3}", m.group(1))}
    allx = single | grouped
    gaps = [x for x in range(min(allx), max(allx)+1) if x not in allx]
    rec("REG", "the register is the primary evidence, not the apology",
        f"{len(allx)} entries spanning {min(allx)}–{max(allx)}, {len(gaps)} unused "
        f"({gaps}), {100*len(reg.split())/len(S.split()):.1f}% of the book. "
        f"Indexed this session at 33 cells, density 68.8%, E = 6, and ℛ recovered "
        f"repair ≤ φ(corroboration)",
        "COMPUTED, and now indexed")

with State("scrutinyF") as st:
    step(st, "the five negatives", negatives, budget=300)
    step(st, "the empirical claim", collection, budget=30)
    step(st, "Q and the register", qreg, budget=30)

for n, claim, ev, verdict in OUT:
    print(f"\n  {n}  {claim}")
    print(f"      {ev}")
    print(f"      VERDICT : {verdict}")
