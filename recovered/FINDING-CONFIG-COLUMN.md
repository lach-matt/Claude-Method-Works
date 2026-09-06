# FINDING-CONFIG-COLUMN (s45, item 1) — THE COLUMN EXISTS, THE BLOCK IS LIFTED, AND EVERY CONFIGURATION FAILURE IN THE WHOLE CHAIN IS ONE DEFECT

## 0 · THE TWO COLUMNS

    Z   ent  rec     ok  cfgok   cfg_chain(state)          rec_cfg(state)
    24   3d   3d   True  False   ...3d4 4s2                ...3d5 4s1
    25   3d   4s  False   True   ...3d5 4s2                ...3d5 4s2
    29   3d   3d   True  False   ...3d9 4s2                ...3d10 4s1
    30   3d   4s  False   True   ...3d10 4s2               ...3d10 4s2
    41   4d   4d   True  False   ...4d3 5s2                ...4d4 5s1
    42   4d   4d   True  False   ...4d4 5s2                ...4d5 5s1
    43   4d   5s  False   True   ...4d5 5s2                ...4d5 5s2
    44   4d   4d   True  False   ...4d6 5s2                ...4d7 5s1
    45   4d   4d   True  False   ...4d7 5s2                ...4d8 5s1
    46   4d   4d   True  False   ...4d8 5s2                ...4d10
    47   4d   5s  False  False   ...4d9 5s2                ...4d10 5s1
    48   4d   5s  False   True   ...4d10 5s2               ...4d10 5s2

All 35 rows not listed are True in both columns.

**CONFIG 39/47 · STEP 42/47 · FIRST CONFIG DIVERGENCE 24 · FIRST STEP DIVERGENCE 25.**

## 1 · SCORING — 9 CLAIMS HELD, 0 FAILED, 0 CONSISTENT-ONLY

**PCC-0 HELD.** No SCF ran. `nlchain.jsonl` md5 is unchanged across every invocation
including the can-fail run. `D_ent`, `margin`, `order`, `nfail`, `ok` are untouched in all 47
rows: the column is a pure function of the sealed file and `ground.py`. Two consecutive
`show` runs are **byte-identical**.
**PCC-0a HELD.** `str_mismatch = []` — string and normalised-multiset comparison agree on all
47 rows. The multiset is what the gate reads.

**PCC-1 HELD.** cfg_ok(24) = False, ok(24) = True. **PCC-2 HELD.** cfg_ok(25) = True,
ok(25) = False. The inversion across 24→25 is exact.
**PCC-3 HELD.** The same inversion at 29/30, with the same signs.
**PCC-4 HELD.** The config failure set over Z ≤ 38 is exactly **{24, 29}** — nothing else in
37 steps.
**PCC-5 HELD.** The `ok` failure set over Z ≤ 38 is exactly **{25, 30}**, so total step
failures are {25, 30, 43, 47, 48} and the score is 42/47 — gate 78's standing number,
re-derived rather than recited.
**PCC-6 HELD** in both directions. Cr(24) and Tc/Cd are transient promotions and cost the
state column exactly one row each, recovering at the next step. Cu(29) reverts at Zn(30) and
recovers likewise. Nb→Ag is a persistent promotion and the state column fails **every** row
from 41 to 47 except 43, recovering only at 48 where 4d fills.
**PCC-7 HELD EXACTLY.** 39/47, first divergence 24, failure set {24,29,41,42,44,45,46,47}.
**PCC-8 HELD EXACTLY.** The columns disagree at **11 of 47**: {24,25,29,30,41,42,43,44,45,46,48}.
**PCC-9 HELD.** `cfg_fail ⊆ ok_fail` is **False** and `ok_fail ⊆ cfg_fail` is **False**.
Neither set contains the other; 47 is the only step both columns fail. **The two columns are
not the same measurement with an offset, and s44 §2(5)'s BLOCKING call is vindicated rather
than weakened.**

## 2 · THE ROW THE PREDICTION DID NOT CONTAIN — AND IT IS THE RESULT

Declared UNPREDICTED in §5 of the prediction ("no metric on configurations is defined here").
Measured after the fact, and labelled as measured-after:

    Z    misplaced   the difference
    24       1       3d−1 4s+1
    29       1       3d−1 4s+1
    41       1       4d−1 5s+1
    42       1       4d−1 5s+1
    44       1       4d−1 5s+1
    45       1       4d−1 5s+1
    46       2       4d−2 5s+2
    47       1       4d−1 5s+1

**EVERY CONFIGURATION FAILURE IN THE ENTIRE 47-STEP CHAIN IS THE SAME DEFECT: ONE ELECTRON
SITTING IN ns WHERE THE RECORD PUTS IT IN (n−1)d.** Eight failures, eight instances of
`d−1 s+1`, magnitude one everywhere except Pd(46) where it is two. **Not once is the defect
an f, a p, a wrong principal quantum number, or a wrong count.** The walk's placement is
correct in every other respect at every one of 47 steps.

This is s44 §2(6) generalised off the 4d row and onto the whole table: what the walk gets
wrong is **not the n+ℓ ordering and not the channel energetics — it is that a
one-electron-at-a-time walk has no promotion operator.** The n+ℓ rule names which channel
the *entrant* takes; the record's anomalies are about where an *already-placed* electron
sits. The state column measures precisely the gap between those two, and the gap has exactly
one shape.

## 3 · WHAT THE CAN-FAIL RUN SHOWED, INCLUDING ITS OWN LIMIT

`--fail` forces step 30's entrant to 5s in memory (`nlchain.jsonl` md5 verified unchanged
after). Three clauses trip, exit 1. The config failure set becomes
{24, 29, 30, 31 … 48} — **one wrong entrant contaminates 19 subsequent states and never
recovers**, which is PCC-6's cumulative clause exhibited rather than argued.

**Stated so it is not overclaimed: `ok_fail` is unchanged under `--fail` BY CONSTRUCTION,
not by insensitivity.** The perturbation edits `ent_nl`, which builds the state; `ok` is read
from the sealed field of the row and is not recomputed by this driver. A reader could take
the unchanged `ok_fail` as evidence the step column is robust. It is not evidence of
anything. R 1671's class, caught in the demonstration rather than in the instrument.

## 4 · STATUS OF THE BLOCK

s44 §2(5) made the configuration column BLOCKING and forbade quoting 42/47 as a
configuration score. **The column now exists.** The two scores are stated together and never
substituted: **CONFIG 39/47, STEP 42/47.** Comparison decides which is *the* score, and the
comparison is now runnable rather than owed. Recommendation for M's ruling, not adopted here:
the STATE column is the one the law must satisfy, because the law is a statement about
configurations, and the STEP column is the instrument that tests the walk. The BLOCK is
lifted; the choice of scoreboard is M's.

## 5 · NEW STANDING GATE (proposed, gate 83)

`python3 nlcfg.py gate` → PASS, exit 0, **8 clauses** (cfg_score, ok_score, cfg_first,
ok_first, cfg_fail, ok_fail, disagree, str_mismatch).
Can-fail: `python3 nlcfg.py gate --fail` → exit 1, 3 clauses trip.
Runtime under 5 s; no SCF. **Its expectations are fixed values and will move when the chain
is extended past Z=48 — the s45 note on gate 77 applies: a gate whose expectation grows with
the chain must have that stated, or growth reads as divergence.**
