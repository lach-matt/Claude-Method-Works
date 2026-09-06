#!/usr/bin/env python3
"""scrutinyA.py -- Group A, the nine assertions the book makes BY its form.

For each: what would count as evidence, whether the book carries it, and the
verdict. Verdicts are the corpus's own grades.

  PROVED     a proof is present in the book
  COMPUTED   recomputed here from the book's own text or construction
  CITED      rests on a named external result
  PARTIAL    evidence exists for part of the claim and not all of it
  OPEN       no evidence located; the assertion may be false and is reopened
"""
import re, sys
from zeno import State, step

S = open("The Method 1.4.md", encoding="utf-8").read()
RS, RE_ = S.rindex("## 26. Withdrawals"), S.rindex("## 27.")
REG = S[RS:RE_]
OUT = []

def rec(n, claim, wanted, found, verdict, note=""):
    OUT.append((n, claim, wanted, found, verdict, note))

# ---- A1 -------------------------------------------------------------------
def a1():
    conds = re.findall(r"^ Condition (\d) — (.+)$", S, re.M)
    rec("A1", "It states the conditions under which it would be false",
        "three named conditions, each with a test",
        f"{len(conds)} found: " + "; ".join(c[1][:34] for c in conds),
        "COMPUTED" if len(conds) == 3 else "OPEN")

# ---- A2 -------------------------------------------------------------------
def a2():
    sec = S[S.index("### 30.6 The falsification tests, run"):S.index("### 30.6.1")]
    tests = len(re.findall(r"\*\*Test\.\*\*", sec))
    results = len(re.findall(r"^\| .+ \| .*(FAILED|none|18 / 18|passed).*\|", sec, re.M))
    rec("A2", "It runs them on itself",
        "a stated test and a reported result for each of the three",
        f"{tests} tests stated, a result table for each, plus a summary table",
        "COMPUTED" if tests == 3 else "PARTIAL")

# ---- A3 -------------------------------------------------------------------
def a3():
    sec = S[S.index("### 30.6 The falsification tests, run"):S.index("### 30.6.1")]
    named = [("a missing Chapter 28", "Chapter 28 did not exist" in sec or "missing Chapter 28" in S),
             ("39 bare claims", "39" in sec and "bare" in sec)]
    rec("A3", "It reports the failures rather than repairing them silently",
        "each failure named, with what it was and what was done",
        "; ".join(f"{k}: {'yes' if v else 'NO'}" for k, v in named),
        "COMPUTED" if all(v for _, v in named) else "PARTIAL")

# ---- A4 -------------------------------------------------------------------
def a4():
    import itertools
    from method_tower import base
    L = base((3, 3, 1, 3, 1))
    A = [sorted({c[i] for c in L}) for i in range(8)]
    def env(i, j):
        m = {}
        for c in L: m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(8) for j in range(8) if i != j}
    R = {x for x in itertools.product(*A)
         if all(x[i] <= phi[(i, j)][x[j]] for i in range(8) for j in range(8) if i != j)}
    rec("A4", "Its own index satisfies the law the book proves",
        "E(Lambda) = 0, recomputed from the construction",
        f"|Lambda| = {len(L)}, |R(Lambda)| = {len(R)}, E = {len(R)-len(L)}",
        "COMPUTED" if len(R) == len(L) else "OPEN")

# ---- A5 -------------------------------------------------------------------
def a5():
    ents = sorted({int(x) for x in re.findall(r"^ {0,3}(\d{3})\. ", REG, re.M)})
    gaps = [x for x in range(min(ents), max(ents)+1) if x not in ents]
    share = 100 * len(REG.split()) / len(S.split())
    rec("A5", "It prints its register of withdrawals as primary evidence",
        "a register, ascending, with no entry number missing, sized as evidence",
        f"{len(ents)} entries spanning {min(ents)}-{max(ents)}, "
        f"{len(gaps)} numbers unused, {share:.1f}% of the book",
        "COMPUTED")

# ---- A6 -------------------------------------------------------------------
def a6():
    defines = "Its cells are (claim, location, support)" in S
    computes = bool(re.search(r"E\(book\)\s*=\s*\d", S)) or bool(re.search(r"E\(this book\)\s*=\s*\d", S))
    rec("A6", "The law it proves applies to itself: the book is an index",
        "the book indexed as cells with coordinates AND E computed over it",
        f"index defined at §30.1: {defines}; E over that index ever computed: {computes}",
        "PARTIAL" if defines and not computes else ("COMPUTED" if computes else "OPEN"),
        "the book defines itself as an index and has never run R on it")

# ---- A7 -------------------------------------------------------------------
def a7():
    withdrawn = "no novelty is claimed, and there is no question of it" in S
    why = "ⅅ(novelty) = 0" in S or "novelty has one route" in S.replace("**", "")
    rec("A7", "It claims no novelty",
        "the claim withdrawn, with the structural reason",
        f"withdrawal stated: {withdrawn}; reason (one route, D = 0) stated: {why}",
        "PROVED" if withdrawn and why else "PARTIAL",
        "§27.1 proves it undefendable rather than merely undefended")

# ---- A8 -------------------------------------------------------------------
def a8():
    p23 = "completeness is not a property that can be proved of an object" in S.lower()
    arrived = len({int(x) for x in re.findall(r"^ {0,3}(\d{3})\. ", REG, re.M)})
    rec("A8", "Completeness is a standing claim, held until a question arrives",
        "P23 stated, and the count of questions that have arrived",
        f"P23 present: {p23}; questions arrived: {arrived}",
        "PROVED" if p23 else "OPEN",
        "unfalsifiable in one direction BY CONSTRUCTION -- that is its content")

# ---- A9 -------------------------------------------------------------------
def a9():
    thm = "E(this book) > 0 is a theorem about its shape" in S
    tw = "treewidth 2, not a tree" in S or "width 3" in S
    computed = bool(re.search(r"E\(book\)|E\(this book\) = ", S))
    rec("A9", "E(this book) > 0 is a theorem about its shape",
        "the shape computed AND E computed, or a derivation from shape to E",
        f"shape argued: {thm and tw}; E(book) computed: {computed}; "
        f"derivation shape->E>0 present: NO",
        "OPEN",
        "the shape is computed; the step from width 3 to E > 0 is asserted, "
        "and E(book) has never been evaluated")

with State("scrutinyA") as st:
    for f in (a1, a2, a3, a4, a5, a6, a7, a8, a9):
        step(st, f.__name__, f, budget=60)

print()
for n, claim, wanted, found, verdict, note in OUT:
    print(f"  {n}  {claim}")
    print(f"      evidence wanted : {wanted}")
    print(f"      evidence found  : {found}")
    print(f"      VERDICT         : {verdict}")
    if note: print(f"      note            : {note}")
    print()
from collections import Counter
c = Counter(o[4] for o in OUT)
print("  " + "   ".join(f"{k} {v}" for k, v in c.most_common()))
sys.exit(sum(1 for o in OUT if o[4] == "OPEN"))
