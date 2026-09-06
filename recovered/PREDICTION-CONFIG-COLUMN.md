# PREDICTION-CONFIG-COLUMN (s45, item 1 — BLOCKING per s44 §2(5))

Filed BEFORE any edit to nlchain.py and before any run. R 1449.

## 0 · WHAT THE COLUMN IS

`ok` compares **STEPS**: `rectag == win`, where `rectag` is the shell whose occupancy rose
between the record's Z−1 and the record's Z. The walk produces a **STATE**: the cumulative
multiset of its own entrants from the seed 1s at Z=1.

The new column compares STATES:

    cfg_chain(Z) = seed + entrants of steps 2..Z            (nlchain.cfg_from_chain)
    cfg_ok(Z)    = ( cfg_chain(Z) == G.expand(Z) )          as a normalised multiset

Both columns stay. Comparison decides which is the score (M, standing).

**PCC-0 — THE COLUMN COSTS NO PHYSICS.** It is computable from sealed `nlchain.jsonl`
plus `ground.py` alone. **No SCF is re-run, no channel is re-solved, no eigenvalue is
recomputed.** Predicted: the column is deterministic and idempotent — computing it twice
gives byte-identical output, and `D_ent`, `margin`, `order`, `nfail`, `ok` are all unchanged
in every row. If any of those five move, the column has touched the field and the claim fails.

**PCC-0a — COMPARISON IS BY NORMALISED MULTISET, NOT BY STRING.** F42.2 says shell order in
`occ` is load-bearing. `G.expand` returns `(n,l,k)` sorted by `(n,l)` with int occupancies
(checked at open, not predicted). `cfg_from_chain` sorts the same way. Predicted: string
comparison and multiset comparison agree on all 47 rows — but the multiset is what is
implemented, because a format change in either producer must not read as a physics
disagreement.

## 1 · THE REAL PREDICTION — Z = 2..38, WHERE NOTHING HAS BEEN COMPUTED

This range has never had a configuration column. Nothing in the s44 bridge states it.

**PCC-1 — FIRST CONFIG DIVERGENCE IS Z = 24, EARLIER THAN `ok`'s Z = 25.**
Record: Cr(24) = [Ar]3d⁵4s¹. Chain at 24 carries [Ar]3d⁴4s². **cfg_ok(24) = False while
ok(24) = True** — the record's *step* into 24 raised 3d and the walk also enters 3d, so the
step agrees while the state does not.

**PCC-2 — AND IT RECOVERS AT Z = 25, WHERE `ok` FAILS.**
Record: Mn(25) = [Ar]3d⁵4s². Chain adds 3d to [Ar]3d⁴4s² → [Ar]3d⁵4s² = the record.
**cfg_ok(25) = True while ok(25) = False.** The two columns are predicted to be *exactly
inverted* across 24→25.

**PCC-3 — THE SAME INVERSION REPEATS AT Cu/Zn.** cfg_ok(29) = False (chain [Ar]3d⁹4s²
against record [Ar]3d¹⁰4s¹) with ok(29) = True; cfg_ok(30) = True with ok(30) = False.

**PCC-4 — THE CONFIG FAILURE SET OVER Z = 2..38 IS EXACTLY {24, 29}.** No other Z in that
range fails. In particular 21–23, 26–28, 31–38 all agree. **This is falsifiable by a single
extra element.**

**PCC-5 — THE `ok` FAILURE SET OVER Z = 2..38 IS EXACTLY {25, 30}.** Cross-check, not a new
claim: with the four 4d-row failures known to be {43, 47, 48} this gives 5 failures in 47
steps, i.e. **42/47** — which is gate 78's standing value. If PCC-5 is wrong, gate 78's
number and this analysis cannot both be right.

**PCC-6 — THE MECHANISM, STATED SO IT CAN FAIL.** A record anomaly that is a **transient
one-electron promotion** — present at Z=a, reverted at Z=a+1 — costs the STATE column one
row (a) and the STEP column one row (a+1), and they are different rows. A **persistent**
promotion costs the state column every row until the promoted shell fills. Predicted
consequence: **the state column can recover; the step column cannot be recovered by
anything the walk does, only by the record returning.**

## 2 · THE 4d ROW — RECALLED, TIMING-FLAGGED (R 1449)

s44 §2(4) states the agreement set {39, 40, 43, 48} and the disagreement set
{41,42,43,44,45,46,48}. **I read that at this session's open, before writing this file.**
Everything in this section is therefore **CONSISTENT-AT-BEST, NEVER HELD**, per R 1645.

Derived (not recalled): cfg failures {41, 42, 44, 45, 46, 47}; cfg passes {39, 40, 43, 48};
ok failures {43, 47, 48}. Z=47 is predicted **both-False**, which is why it is absent from
s44's seven-element disagreement set — and that absence is the one thing in this section
the recall does not already contain.

## 3 · THE SCORE

**PCC-7 — CONFIG SCORE = 39/47, FIRST CONFIG DIVERGENCE = 24.**
Failures {24, 29, 41, 42, 44, 45, 46, 47} = 8.

**PCC-8 — THE TWO COLUMNS DISAGREE AT 11 OF 47 STEPS:**
{24, 25, 29, 30, 41, 42, 43, 44, 45, 46, 48}. Z=47 agrees by both being False, and every
other step agrees by both being True.

**PCC-9 — NEITHER SCORE IS THE OTHER'S UPPER BOUND.** 39 < 42, but not because the state
column is stricter: it is False at 24 where the step column is True, and True at 25 where
the step column is False. **Predicted: neither failure set contains the other.** If one
contains the other, the two columns are measuring the same object with a shift and the
BLOCKING finding of s44 §2(5) is weaker than stated.

## 4 · WHAT WOULD FALSIFY THE WHOLE ITEM

Any of: a config column that changes a `D_ent`; a first divergence other than 24; a failure
set over Z≤38 other than {24,29}; string and multiset comparison disagreeing; or the two
failure sets nesting. **Each is checkable in one run of the new column.**

## 5 · UNPREDICTED, DECLARED AS UNPREDICTED

The *magnitude* of any disagreement (no metric on configurations is defined here), and
whether the record configurations for Z=2..38 match `ground.py` — that is the record
against itself and is not this column's business.
