# PREDICTION-OPENINGS-89 (s49) — FILED BEFORE nlchain IS POINTED AT Z=89

Binding under R 1449. Clause-only. This file discharges the s48 obligation that
PREDICTION-OPENINGS be refiled before Z=89; no prior file covers past Z=88. Record
configurations are the comparison column, read from `ground.py`, RECALLED-NOT-ENTERED.

## 1 · STATE ENTERING

Sealed row Z=88: walk cfg **...6p6 7s2**, entrant 7s, both columns pass. Walk and record are
REALIGNED in state, as they were entering 81. The 6p block and the 7s pair are closed with no
failure in either column at any of 81..88.

## 2 · WHAT IS ACTUALLY BEING TESTED AT Z=89 — AND THE CORRECTION IT FORCES

5f and 6d both carry **n+ℓ = 8**. The record opens **6d at Ac(89)** and does not open 5f until
**Pa(91)**. The tie-break clause — lower n first within equal n+ℓ — demands 5f BEFORE 6d.

**So Z=89 is not an ordering test. It is a TIE-BREAK test, and so was La(57).** At 57 the walk
chose 5d over 4f, and 5d and 4f both carry n+ℓ = 7. The chain's single standing failure has been
described in earlier sessions as "the ordering failing at La". That description is wrong and is
corrected here before the run: **the ordering clause has never failed anywhere in 87 rows.** The
tie-break clause has failed once, at the 4f opening.

The tie-break clause now stands at four pairs held — 4s/3d, 4p/5s, 4d/5p, 6p/7s — and one pair
failed, 4f/5d. Every pair it has held on is s, p or d. The one it failed on is the f opening.

## 3 · THE CLAUSES

**PF-1 — THE ENTRANT AT Z=89 IS 6d, NOT 5f.** The field puts Ac in 6d, agreeing with the record
and DISAGREEING with the tie-break clause. Falsified if 5f wins at 89.

**PF-2 — BOTH COLUMNS PASS AT 89.** ok = True (record entrant 6d) and cfg_ok = True (walk
reaches 6d1 7s2, which IS the record's Ac). Falsified by either failing.

**PF-3 — THE TIE-BREAK CLAUSE FAILS AT EXACTLY THE TWO f OPENINGS AND NOWHERE ELSE.** 4f/5d at
57 and 5f/6d at 89, and at no s, p or d pair anywhere in the chain. This is the session's
structural claim and it is the one worth breaking. Falsified by a tie-break failure at any
non-f pair, or by the clause holding at 89.

**PF-4 — 5f BECOMES THE ENTRANT AT Z=91, NOT 90 AND NOT 92.** The record gives Th(90) 6d2 7s2
and Pa(91) 5f2 6d1 7s2. Falsified by 5f entering at any other Z.

**PF-5 — THE La(57) DESCENT REPEATS: THE WALK RUNS ONE 5f BEHIND FROM 91.** Having spent 89 and
90 on 6d and having no operator to vacate them, the walk's cfg must part from the record inside
the 5f block exactly as it did inside the 4f block from Z=59. Predicted: cfg fails from 92
onward within 89..96, ok continues to pass while the record's entrant is 5f. Falsified by cfg
passing throughout 92..96.

**PF-6 — NO ORDERING FAILURE ANYWHERE IN 89..96.** No channel of larger n+ℓ beats one of smaller
n+ℓ. FIRST STEP DIVERGENCE stays at 25. Falsified by any crossing.

**PF-7 — NO CONSTANT INTRODUCED.** Only c = 137.035999.

## 4 · NOT PREDICTED

All magnitudes — no bands. Which channels fail on node count. The rung of any step. Whether the
6d/5f margin at 89 is small or large. Anything past Z=96; a further file is owed before Z=97.
