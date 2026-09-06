#!/usr/bin/env python3
"""closeB2.py -- the twelve intake defects in Transitions, and O23's caveat.

C1  §6.4's 'Unchecked by coordinate' row sums to 48, not 32 — it is the TOTAL
C2  §4.4 says decay is 'roughly 1.9 per atom'; the figure says 2.57; fit 2.51
C3  Part X titled 'Six more indices'; §10.1 lists five
C4  §10.1 says everything outside V1 closes, in the table showing the charger
    index open at E = 25
C5  §10.7's table has no header separator and does not render
C6  Part XIII lists 'the 32 unchecked term pairs' twice
C7  §12.2c titled 'four blind spots', carries eight audits, and audit 26 is absent
C8  section numbers run 11.1, 11.2, 12.2b, 12.2d, 12.2c, 11.3, 11.4, 12.1
C9  source says v3.0; the artefact's footer says v2.0
C10 the abstract states the BFV derivation twice
C11 §8.2's '30, 30, 20, 20, 10' has no table behind it
C12 §8.5 and §8.7 are live analysis on a partition §8.4 derives away
O23 Reeh-Schlieder is a theorem in Minkowski and a PROPERTY in curved spacetime
"""
import re, sys
from zeno import State, step

P = "Transitions.md"
s = open(P, encoding="utf-8").read()
N = []
def swap(a, b, n):
    global s
    assert s.count(a) == 1, f"{n}: {s.count(a)}"
    s = s.replace(a, b); N.append(n)
def after(a, t, n):
    global s
    assert s.count(a) == 1, f"{n}: {s.count(a)}"
    i = s.index(a); j = s.index("\n\n", i)
    s = s[:j] + "\n\n" + t.strip("\n") + s[j:]; N.append(n)

def c1():
    swap("Unchecked by coordinate: X 8, Sc 4, IC 6, U 8, NEC 7, L 4, SD 5, DNc 4, DNd 2 — of which",
         "Pairs by coordinate: X 8, Sc 4, IC 6, U 8, NEC 7, L 4, SD 5, DNc 4, DNd 2 — **these are "
         "the 48 term-sharing pairs, not the 32 unchecked**, and the row was mislabelled: it sums "
         "to 48. Of them", "C1 the mislabelled row")

def c2():
    swap("Decay is geometric at roughly 1.9 per atom.",
         "Decay is geometric at **2.51 per atom** — a log-linear fit over all seven points, against "
         "the 2.57 the figure carries. *An earlier draft read 1.9, which neither the fit nor the "
         "figure supports.*", "C2 the decay factor")

def c3():
    swap("## Part X · Six more indices, and what the null case is",
         "## Part X · Five more indices, and what the null case is", "C3 six -> five")
    swap("Part I's thesis needs instances that are not the two it was built from. Six were built.",
         "Part I's thesis needs instances that are not the two it was built from. **Five were "
         "built** — V3 geometry, V6 solution, the local null surface, the ANEC proofs and the "
         "charger index — and §10.2's measure is a comparison, not a sixth index.",
         "C3 the count in the text")

def c4():
    swap("**Everything built outside V1 closes.** The defect is in V1, on the V1–V3 edge, and in the partition\nitself — nowhere else.",
         "**Every VOCABULARY index closes; the charger index does not.** The defect is in V1, on the "
         "V1–V3 edge, in the charger index at E = 25, and in the partition itself — nowhere else. "
         "*An earlier draft read* everything built outside V1 closes, *in the same table that shows "
         "the charger index open.*", "C4 the contradiction with its own table")

def c5():
    swap("| instance | what changes across the scope |\n| Buniy |",
         "| instance | what changes across the scope |\n|---|---|\n| Buniy |",
         "C5 the missing table separator")

def c6():
    swap("| the 32 unchecked term pairs | IC has six and has never been checked once |\n| the six undocumented values |",
         "| the six undocumented values |", "C6 the duplicated open item")

def c7():
    swap("### 12.2c The audit suite has four blind spots, not one",
         "### 12.2c The audit suite has eight audits beyond the twenty-one, and two blind spots",
         "C7 the heading against its table")
    swap("| 27 possibility bound |",
         "| 26 — | *unassigned; the numbering runs 22–25 and 27–30* | — | — |\n| 27 possibility bound |",
         "C7 the absent audit 26")

def c8():
    """renumber Part XII/XIII's sections into sequence."""
    for a, b in [("### 11.1 The promotion ledger", "### 12.1 The promotion ledger"),
                 ("### 11.2 Withdrawals", "### 12.2 Withdrawals"),
                 ("### 12.2b Withdrawn since v2.0", "### 12.3 Withdrawn since v2.0"),
                 ("### 12.2d The numeric debt, discharged and marked",
                  "### 12.4 The numeric debt, discharged and marked"),
                 ("### 12.2c The audit suite has eight audits beyond the twenty-one, and two blind spots",
                  "### 12.5 The audit suite has eight audits beyond the twenty-one, and two blind spots"),
                 ("### 11.3 The recurring class", "### 12.6 The recurring class"),
                 ("### 11.4 The seven propositions", "### 12.7 The seven propositions"),
                 ("### 12.1 The join, and why it stays open", "### 13.1 The join, and why it stays open")]:
        swap(a, b, f"C8 {a[4:28]}")
    # and the in-text references to the old numbers
    for a, b in [("§12.2b as a defect", "§12.3 as a defect"),
                 ("logs as* TRANS gates the trace", "logs as* TRANS gates the trace"),
                 ("withdrawn in §11.2 had", "withdrawn in §12.2 had")]:
        if s.count(a) == 1: swap(a, b, f"C8 ref {a[:22]}")

def c9():
    swap("Draft v3.0. Prepared with a computing collaborator under the protocols of The Method v1.4.",
         "Draft v3.0. Prepared with a computing collaborator under the protocols of The Method v1.4. "
         "**The artefact accompanying this source carries a v2.0 running footer on all 46 pages and "
         "predates it**; the source is the record and the artefact is stale until rebuilt.",
         "C9 the version mismatch, disclosed")

def c10():
    swap("""Finally the vocabulary partition is derived rather than chosen: it is the **Brunetti–Fredenhagen–Verch
functor** read as a list of its parts, and the terms that refuse to place are *relations* between them.
The self-consistent achronal ANEC is one such relation, which is why no coordinate of a law index can
carry it — and the gap it names turns out to be a **modular theory** gap, with a target one cell from
where it is proved.""",
         """The self-consistent achronal ANEC is one such relation, which is why no coordinate of a law
index can carry it — and the gap it names turns out to be a **modular theory** gap, with a target one
cell from where it is proved.""", "C10 the repeated abstract paragraph")

def c11():
    swap("The defect is **largest at exactly one scope condition** — 30, 30, 20, 20, 10 as conditions\nare added.",
         "The defect is **largest at exactly one scope condition**. The table above prints the "
         "measured values — 0 at arity 2, then 30, 30 and 30 — and the descending sequence an "
         "earlier draft gave for further conditions is **withdrawn: no table stands behind it**.",
         "C11 the unbacked sequence")

def c12():
    after("### 8.5 The system graph",
"""
> **This section and §8.7 are HISTORY, not current analysis.** Both are built on the
> seven-vocabulary partition that §8.4 derives away and §12.3 withdraws. They are retained because
> §8.6's correction is only legible against what it corrects, and because the trade they name —
> connected or acyclic — survives the partition change. **Every V1…V7 label below belongs to the
> withdrawn partition.** The current partition is T, M, A, S, and on it the graph is complete.
""", "C12 the withdrawn partition marked as history")

def o23():
    after("| T0 | Reeh-Schlieder | the vacuum is cyclic and separating for local algebras | the physical input that makes the rest applicable |",
"""
**A fifth caveat, and it is on T0.** Reeh–Schlieder is a **theorem** in Minkowski space, proved from
the analyticity of vacuum correlation functions, the spectrum condition and the action of the
Poincaré group on the vacuum. **In curved spacetime it is a property**, established for free massive
scalar fields and elsewhere assumed as an axiom. The chain above needs it for **interacting** fields
on an isolated horizon, where none of the three Minkowski ingredients is available and no proof is
known. T0 is therefore an assumption of the same standing as T2, and the chain has two open links
rather than one.
""", "O23 the Reeh-Schlieder caveat")

with State("closeB2") as st:
    for f in (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, o23):
        step(st, f.__name__, f, budget=30)

open(P, "w", encoding="utf-8").write(s)
print(f"  {len(N)} edits to Transitions.md")
for x in N: print(f"    {x}")
