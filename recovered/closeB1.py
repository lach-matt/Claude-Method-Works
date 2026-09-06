#!/usr/bin/env python3
"""closeB1.py -- O3, O13, O28 into the book."""
import re, sys
from zeno import State, step

P = "The Method 1.4.md"
s = open(P, encoding="utf-8").read()
N = []
def after(a, t, n):
    global s
    assert s.count(a) == 1, f"{n}: {s.count(a)}"
    i = s.index(a); j = s.index("\n\n", i)
    s = s[:j] + "\n\n" + t.strip("\n") + s[j:]; N.append(n)

# ------------------------------------------------------------ O3, the preface
def preface():
    after("**The claim.** An index that is *closed*",
"""
 **Stated exactly, after every mechanism was scrutinised one at a time.** A closed index is a fixed
 point of ℛ. **Being one gives six things and no others**: its alphabet, its bounds, the totality of
 its membership test, which cells may be added, which axes may be adjoined, and which constraints may
 be imposed. **Three further mechanisms are available and none is a consequence of closure** — the
 order is recovered only across a tree, a wrong value only from outside the index, a wrong derivation
 only along a second route. **And what closure never gives at any price is that the coordinates refer
 to anything**, which is why Chapter 16 carries six defences rather than three and why one of them
 cannot be run by this book at all.

 **And an index that is not a fixed point is not thereby defective.** Where a certificate exhibits an
 operation on the coordinate system reaching a fixed point, E measures the drawing; where none
 exists, E measures the world. **Openness is a measurement, and closure is the case where the
 measurement is zero.** Chapter 15's thesis and §18.4.1's law are one operator read in two
 directions, which is why neither could be sharpened from inside the other. Register 428.
""", "INSERT preface  the thesis, restated")

# ---------------------------------------------------------- O3, Chapter 15
def ch15():
    after("    A closed index contains its own definition.",
"""
 **Across a tree.** S1 and S3 hold of any closed index; **S2 does not**, and above d = 2 the converse
 of §15.3's lemma fails. The unqualified sentence above is exact for the alphabet and the bounds and
 conditional for the order, which §15.5 states and the preface now states with it.
""", "INSERT §15  the qualification the opening line needs")

# ---------------------------------------------------------------- O13
def p9():
    after("**Seven are operations** — P3, P4, P5, P6, P11, P14, P15",
"""
 **And P9 has a second instance, which this book produced without recognising it.** Its only computed
 case was rank(log q) = 1 over fifteen Rydberg observables — and that is a tautology once §24.1's
 assembly rule makes every observable a power of ν, so it measures the rule and not the principle.
 **The second case is E itself.** E measures whether an index can carry a constraint, and it is read
 three ways: **forward** as a diagnosis, which of two modes produced the defect and whether it is
 repairable; **backward** as a prohibition, that a minimal failing support of three admits no repair
 by any operation on coordinates; and **as an outcome**, §16.7.1's test of whether E is removable.
 The three were obtained separately and their identity had to be computed, so unlike the Rydberg case
 it is not a tautology. **One definition, three dimensions, each a perspective of it** — which is
 what P9 says. Register 429.
""", "INSERT §1  P9's second instance")

# ---------------------------------------------------------------- O28 + registers
def reg():
    after("427. **The two sources of the tick were double-counted.**",
"""
 428. **The thesis restated after scrutiny.** *Cannot help containing* was exact for six of the nine
 mechanisms and conditional for three — S2 needs a tree, D1 an outside measurement, D2 a second
 derivation — and §14.4's count of *two requiring something constructed* was three, D1 having been
 counted among the six against §16.7.3. The restatement adds what no count could: **closure never
 gives that the coordinates refer to anything**, and joins Chapter 15's thesis to §18.4.1's law as
 one operator read in two directions.

 429. **P9's second instance, and the first was a tautology.** rank(log q) = 1 follows from §24.1's
 assembly rule, so it measures the rule. E read as diagnosis, as prohibition and as removability is a
 second case in which one definition carries three perspectives, and the three had to be computed
 identical rather than assumed.

 430. **The press will silently drop a figure whose neighbour shares its dimensions**, and this book
 contains the case: Figures 16.3 and 16.4 are distinct and both 1560 × 660, so the pairing pass that
 collapses duplicates would keep one and fail its own assertion at twenty-seven. The heuristic
 assumes *equal dimensions implies duplicate* and has never fired because the original figure
 directory carried both members of every genuine pair. **A rule that has never been shown capable of
 being wrong**, which is §4.6, found by rebuilding the figures from the artefact rather than by
 reading the press. The pairing now tests ink variance as well as dimension.

 431. **Two of the six build-time readouts cannot run.** §2.21 requires a withdrawn figure to be
 represented by the law that generates it, by a stable structure, or **by a computation the artefact
 performs** — and E(G) is of the third kind. *The Method 1.4 numbers-index.py* and *densities.py* are
 named in the manifest as supporting sources and are absent, so the press prints a failure notice
 where the readout belongs. **A readout that cannot run is a figure with no representation at all**,
 which is the state §2.21 exists to forbid.
""", "INSERT §26.7  registers 428-431")

with State("closeB1") as st:
    for f in (preface, ch15, p9, reg):
        step(st, f.__name__, f, budget=30)

open(P, "w", encoding="utf-8").write(s)
print(f"  {len(N)} edits")
for x in N: print(f"    {x}")
