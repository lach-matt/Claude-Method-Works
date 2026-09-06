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

## 2 · The answer

**The corridor is an instrument of CONCAVITY IN THE NODE COUNT, and it returns the
number of parameter values that class requires.** It is not an instrument of the atom
and not of ν. Two things separate cleanly:

- **What belongs to the world.** Strict concavity in p is NECESSARY — a linear or
  convex form cannot order the observed table at any value of a. And given concavity,
  the piercing number is 3, invariantly.
- **What belongs to ν.** The stabbing points. Under √p they are 0.7071, 1.7071,
  2.4409; under p/(1+p) they are 1.5, 7.5, 24.0; under 1−e^(−p), 1.157, 8.546, 171.6.
  **The surds are ν's coordinates for the number 3, not the content of it.**

This is R 1517 made exact: *the index forecloses a family rather than supplying a
mechanism, and it returns the number three.* The family is now named — strictly
concave increasing functions of the node count — and the number is its invariant.

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