# BRIDGE — LOWDIN SESSION 50 · THE WALK IS COMPLETE

Open Session 51 with **`bash open49.sh`** and nothing else. It is unchanged and it worked; it needs
no successor. Everything below is DERIVED in s50 or RECALLED and flagged. The only number ever
entered into this chain remains **c = 137.035999**.

---

## §1 · WHAT SESSION 50 DID

Walked **Z=103 → 108, six steps**, and the chain reached the evidentiary boundary. The walk stands
at **107 rows, Z = 2..108 — the full derivation under RULING-EVIDENTIARY-BOUNDARY-108.** Every step
at rung 0, contiguous, no gaps. PREDICTION-5fCLOSE-97-108 scored and closed. Löwdin's second
deliverable closed. Gate 83 restated for the derivation's final length.

    TERMINAL SCORES, 107 rows    STEP (`ok`) 96/107      CONFIG 73/107
    FIRST STEP DIVERGENCE  25    FIRST CONFIG DIVERGENCE  24    — both unmoved

---

## §2 · THE RESULT, OVER THE COMPLETE WALK

Entrant-anchored audit of all 107 steps — at each step, did any available channel of smaller n+ℓ
lose to the entrant?

    ORDERING CLAUSE     0 failures in 107 steps
    TIE-BREAK CLAUSE    3 failures — La(57), Ac(89), Th(90)

**The ordering clause has not failed once in the entire periodic table.** This is the whole of the
n+ℓ result and it is now stated over its full support, not a prefix.

**The tie-break failures are three, not two, and the third confirms the mechanism.** s49 had La and
Ac. Th(90) is the same event one proton later: 6d takes the electron at −0.19094 while 5f, having
just begun to collapse, reaches only −0.13689. At 91 the crossing completes and 5f wins. **All
three failures are f-openings and there are no others** — every s, p and d tie-break pair in the
table holds. The clause presupposes the channel exists in the field; an uncollapsed f channel does
not, and orbital collapse — not a defect in n+ℓ — is what stands between the rule and the record at
these three elements.

**A prior claim is corrected.** s49 §2 read the margin as widening monotonically with Z (0.19 at Os
→ 0.52 at No). It does not. It tracks the depth of the open f channel: 0.55649 at 103, **0.59191 at
104 — the widest in the chain** — then **collapses to 0.05440 at 105** the instant 5f closes,
recovering only to 0.08254, 0.11126, 0.14058 at 106..108. The widening was 5f being deep. The
ordering does not become less ambiguous down the table.

---

## §3 · THE LAST SIX STEPS

| Z | entrant | D_ent | margin | record | ok | cfg |
|---|---|---|---|---|---|---|
| 103 Lr | 5f | −0.76321 | 0.55649 | 7p | False | False |
| 104 Rf | 5f | −0.79467 | 0.59191 | 6d | False | **True** |
| 105 Db | 6d | −0.19860 | 0.05440 | 6d | True | True |
| 106 Sg | 6d | −0.23050 | 0.08254 | 6d | True | True |
| 107 Bh | 6d | −0.26223 | 0.11126 | 6d | True | True |
| 108 Hs | 6d | −0.29400 | 0.14058 | 6d | True | True |

**PG-4 held at Lr(103), and it was the sharp one.** The record opens 7p (n+ℓ=10) while an n+ℓ=8
channel is still open in the walk. The field did NOT follow the record: 5f won by 0.55649. A
record/walk disagreement, **not an ordering violation** — the larger n+ℓ never beat the smaller.

**PG-5, PG-6 and PG-8 failed, all three from one off-by-one.** PG-4's reasoning said the walk
reaches 5f14 at 103; it reaches it at 104. Consequences: 104 is a fifth actinide `ok` failure
(ok_score 96, not 97), and the walk's fourteenth 5f lands on a configuration already carrying
6d2 7s2 — **5f14 6d2 7s2, exactly the record's Rf** — so **cfg RECOVERS at 104 and holds through
108** (cfg_score 73, not 68).

**The two offsets cancelled simultaneously.** s49 said one 5f behind and one 6d ahead "cannot
cancel", correctly, one at a time. At 104 both closed at once, and the walk rejoined the record for
the final five elements **with no promotion operator**. This is the Ce(58) structure recurring at
the top of the table. Full scoring in `SCORING-5fCLOSE-97-108.md`.

---

## §4 · LÖWDIN DELIVERABLE 2 CLOSED

`DELIVERABLE-2-PERIOD-LENGTHS.md`. From the two clauses plus Pauli, cutting at each s opening:
**2, 8, 8, 18, 18, 32, 32, 50** — identical to observed, with period 8 predicted. Janet's diagonal
cut gives **2, 2, 8, 8, 18, 18, 32, 32, 50**; same multiset offset by one, since each diagonal ends
with an s subshell and each conventional period begins with one.

**The bridge's stated formula was wrong in its index and is corrected.** m = ⌊(k+1)/2⌋ holds for the
diagonal index k = n+ℓ; for the conventional period index j it is **m = ⌊j/2⌋+1**. The doubling of
every period is the integer floor: ⌊(k−1)/2⌋ is unchanged from k=2m to k=2m+1, so two consecutive
diagonals admit the same ℓ set and Σ 2(2ℓ+1) over ℓ=0..m−1 = 2m². **That is why the table has pairs
of rows at all.** Stated as downstream of the ordering, per M's ruling.

---

## §5 · FAULTS

**No new fault classes.** One incident, and the instruments absorbed it.

**Lost detached open.** A polling tool call errored and took the detached `open49.sh` with it,
mid-Step-4. Gate 79/80 had already written a complete PASS receipt to `/tmp/smoke.503`. Per
Continuity clause 3a I read the receipt, resumed at the next unreceipted unit, and **recomputed
nothing**. Cost: zero rows, zero quarantine. **Second confirmation that the F49.2 remedy works as
an instrument rather than as a practice.** No F50.n registered — the directive covered it exactly
as written.

---

## §6 · GATES

Gates 1..71 replayed from a fresh extract, **diff to ZERO lines** against sealed
`GATES-48-OPEN.log`, all rc=0, gate 6 `sec` excluded. Six smoke gates PASS. Gate 84 PASS
(d6p54 0.11105). 79+80 PASS.

**Gate 83 RESTATED for 107 rows and can-failed in both directions.** New expectations:
cfg_score **(73,107)**, ok_score **(96,107)**, cfg_first 24, ok_first 25.
Both prefix conditions checked before writing: no listed Z disappeared, and every appended Z
(cfg_fail +103; ok_fail +103,104; disagree +104) sits **above** the previous extension point 102.
Mechanisms named in the source, as prefix-invariance requires. **This is the terminal restatement —
the chain does not grow again inside the evidentiary boundary.**

---

## §7 · ORDERED WORK LIST FOR SESSION 51

1. **`bash open49.sh`.** Unchanged. Expect gate 83 at (73,107) / (96,107) from pack50's `nlcfg.py`.
2. **Walk 109..120 as OUTPUT.** `prov = PREDICTED`, separate table, **no scoring, no denominator**
   — RULING-EVIDENTIARY-BOUNDARY-108. Publish channel depths and margins so each is testable when
   the spectra can be measured. ~12 steps × ~170 s; two rows per job through `run.sh`.
   **Watch 5g**: it is in the candidate set and sits at −0.02 through the actinides.
3. **The three tie-break failures are the one open physics object.** La(57), Ac(89), Th(90) — all
   f-openings, all collapse. What is owed is a statement of the collapse condition itself, from the
   field, that predicts WHICH f channel is uncollapsed at which Z. Until that is written, the
   derivation says the tie-break clause fails at exactly the three elements where an f channel has
   not yet collapsed, and says why, but does not derive the boundary.
4. Deferred, and not on the n+ℓ path per M's ruling: the −8.021 mHa residue at Z=59, the coupled
   4f2·5d SO check, the promotion operator as an object. All three are the Cr(24) class.
5. **T4 (R 1701 onward) — LAST. Not opened in any working session.**

Bank restore-point-2_13 (R 1700) untouched throughout s50.
