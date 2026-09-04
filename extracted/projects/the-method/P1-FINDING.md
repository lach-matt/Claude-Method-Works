# P1 — WHAT THE CORRIDOR IS AN INSTRUMENT OF

Computed by `p1.py`. Answers the open item in `CHAPTER-LOWDIN.md` §8:
*"the question is no longer 'what is a' but what class of problem the corridor
measures."* R 1517 answered it halfway; R 1621 tested one candidate (the
Demkov–Ostrovsky focusing degeneracy) and the conjecture was not supported.

## 1 · The test that could fail

A one-parameter ordering functional of the form **ν = A(n,ℓ) − a·B(n,ℓ)** turns each
step into one linear inequality in a, hence one interval. Vary B over many candidate
forms on the SAME observed order. If the verdict is invariant, the corridor measures
the atom. If it moves, the corridor measures the form.

**It moves — and it moves by CLASS, not by function.** With p = n − ℓ − 1:

    B = f(p) strictly concave, increasing    0 steps refuted    clique 3
    B = f(p) linear or convex                6 steps refuted    clique 2

Tested across p^β for β ∈ [0.05, 1.01], ln(1+p), 1−e^(−p), atan(p), p/(1+p).
**The boundary is exactly β = 1**: every β < 1 is feasible at all 106 steps, every
β ≥ 1 is refuted at 6. Clique 2 is not the better result — those forms are refuted
outright, and the clique is computed on what survives.

## 2 · The answer, AFTER A SELF-CORRECTION

**First statement, now WITHDRAWN.** From the named forms alone I wrote that strict
concavity in p is NECESSARY and that clique 3 is invariant across feasible forms.
Both are false, and the test that broke them is the one that should have come first.

Because the constraints evaluate B only at integer p ∈ {0…7}, and translation and
scaling cancel in the differences, a candidate form IS an increasing 8-vector.
The class is finite-dimensional and can be sampled rather than named.

    30,000 increasing 8-vectors, uniform     2,206 feasible
      of those, clique 3 / 4 / 5             1,843 / 354 / 9
     5,000 vectors from the CONCAVE cone     5,000 feasible, clique 3 in ALL 5,000

- **Concavity is SUFFICIENT, not necessary.** No concave vector was ever refuted, and
  2,928 non-concave vectors were feasible. My necessity claim came from testing seven
  named functions and generalising — P5 exactly, and §2.14's most-violated protocol.
- **Clique 3 is an invariant of the CONCAVE CONE, not of feasibility.** Off the cone
  the parameter count reaches 4 and 5.
- **A second reading was raised and also refuted.** Feasible vectors are enriched for
  negative second differences precisely at p = 2, 3, 5 — the three canonical band
  indices — at 0.760, 0.655, 0.770 against an infeasible baseline near 0.48, while
  p = 1, 4, 6 run BELOW baseline. Tested as a condition, local concavity at {2,3,5}
  admits 1,702 infeasible and misses 1,394 feasible. **It is a correlation, not the
  condition.** The condition is not yet characterised.

**WHAT SURVIVES.** *If the ordering functional is concave in the node count, the table
is representable and requires exactly three parameter values.* Sufficiency at
5,000/5,000 and the clique pinned at 3 throughout; a proof is owed and not attempted
here. The corridor is therefore an instrument of the candidate form's SHAPE — it is
not an instrument of the atom, and R 1621 already showed it is not one of the
Demkov–Ostrovsky degeneracy.

**What belongs to ν alone:** the stabbing points. Under √p they are 0.7071, 1.7071,
2.4409; under p/(1+p), 1.5, 7.5, 24.0; under 1−e^(−p), 1.157, 8.546, 171.6. The
surds are ν's coordinates for the number three, never the content of it.

## 3 · THE SIX, AND THEY ARE ONE OBJECT SEEN TWICE

The steps that refute a linear or convex form are

    Z= 57 La  enters 5d  p=2      Z= 89 Ac  enters 6d  p=3
    Z= 64 Gd  enters 5d  p=2      Z= 90 Th  enters 6d  p=3
                                  Z= 96 Cm  enters 6d  p=3
                                  Z=103 Lr  enters 7p  p=5

**These are exactly the members of the three upper canonical bands of
`CLIQUE3-FINDING.md` §2** — p=2 {La, Gd}, p=3 {Ac, Th, Cm}, p=5 {Lr}. Two unrelated
computations, one set of six. The bands whose disjointness FORCES clique 3 are the
same steps that FORCE concavity.

And they are the named anomalies. **La and Ac are the two elements at which Madelung
is false** (§2, the chapter's firmest result, R 1594). Gd and Cm are the half-filled-f
contests. Th and Lr are the remaining d/f and p anomalies. *The exceptions are not
noise around the rule — they are the entire measurement. They are what forces the
ordering functional's shape, and everything else in the table is silent about it.*

This meets Schwarz's objection on its own terms (failures concentrated in d and f,
`LOWDIN-LITERATURE.md` §7) — the concentration is not a symptom, it is the signal.

## 4 · What this does NOT do

It does not derive the filling order from the Schrödinger equation. Concavity in the
node count is a NECESSARY CONDITION on the form, established by refutation, not a
mechanism producing one. **Löwdin's challenge stands.** What is now closed is the
account of what the instrument measures.
