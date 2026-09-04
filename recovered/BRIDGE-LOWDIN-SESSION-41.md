# BRIDGE — THE LÖWDIN SESSION 41 (2026-08-18)
Successor to BRIDGE-LOWDIN-SESSION-40.md. Bank restore-point-2_13 (R 1700) UNCHANGED. HANDOFF-40 verified ok=875 bad=0.
Runtime layered 5 → 18 → 19..40 with .json (F38.1). Gates 1-71 at open: **283 lines, diff = 0, BYTE-IDENTICAL to
GATES-40-OPEN.log including gate 6's sec field.** PT8 pass (2.78e-17 / 0 / 0); 72, 73 SKIP as filed. Gates 74, 75, 76
all REPRODUCE and are ADOPTED. Census open ok=272 bad=0 nopack=3. No fault at open. No fault registered this session.

## 1 · Rulings (M, s41)
(1) "2 only needs to be done if it furthers n+l" — THE RULING THAT SHAPED THE SESSION. F39.2 repair is admitted
    only on the standing test of s40 ruling (3). TESTED, NOT ARGUED: all three s40 instances drop a channel whose
    n+ℓ EXCEEDS the winner's, so none could have outranked it. **F39.2 REPAIR: NOT BUILT.** Replaced by
    f392_guard.py, a read-only audit that marks a step UNSAFE iff nfail>0 and a dropped channel has
    n+ℓ ≤ n+ℓ(winner). Repair is now CONDITIONAL ON THE GUARD FIRING — triggered by n+ℓ, not by judgement.
(2) "Continue" — proceed to item (1), the walk.
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 flags; comparison decides; no scans; no constant
beyond c; residue is not closure; T4 LAST; the n+ℓ walk is the solution format; Δ is a scored column only.

## 2 · Findings (pack41) — 9 HELD · 1 FAILED · 0 rescored. Chain 19 → **29 of 107 steps.**
(1) **THE 3d COLLAPSE IS PRODUCED BY THE FIELD.** g := D(4p) − D(3d) was −0.03556 at Z=19 and −0.03090 at Z=20
    (both clause-2 violations), drifting +0.0047/proton. **g(21) = +0.09763 — a swing of +0.12853 in one proton,
    27× the drift.** 3d deepens 0.169 Ha while 4p moves 0.041. The canonical Madelung crossover, no record input.
(2) **CLAUSE 2 RESTORED AND STAYS RESTORED — 10/10, monotone 9/9**, g rising +0.0976 → +0.3413. The s39/s40
    clause-2 violations at K and Ca are a **THRESHOLD effect that switches off when 3d becomes the entrant**,
    not a standing defect of the tie-break. Threshold located between Z=20 and Z=21; mechanism named (3d collapse).
    This closes s40's only n+ℓ-bearing residue, in the affirmative.
(3) **UNPREDICTED IDENTITY, TIMING-FLAGGED (R 1449): g(Z) EQUALS THE MARGIN AT ALL TEN STEPS.** 4p is runner-up
    throughout, so the margin law and the clause-2 measurement are ONE quantity. The margin IS the tie-break's
    distance from failure in this row.
(4) MARGIN LAW HELD 9/9 with the declared Cr/Cu allowance UNUSED. Now 2p 6/6, 3p 6/6, 3d 9/9.
(5) **PC3D-7 FAILED, AND THE FAILURE IS THE RESULT.** Predicted entrant 10/10 + config 8/10; measured
    **entrant 8/10 (False at 25, 30) and config 8/10 (wrong at 24, 29) — DISJOINT SETS.** `rectag` counts only
    occupancy INCREASES, so Cr scores RIGHT with a WRONG config (3d⁴4s²) and Mn scores WRONG with a RIGHT config
    (3d⁵4s², matching the record by another route); identically Cu/Zn. **Each record anomaly produces a paired
    scoring artefact one element LATER, inverted.** FIRST DIVERGENCE = **Z=25**, an artefact of the scoring key.
(6) PC3D-8 HELD: entrant is 3d at all ten steps. Cr and Cu are not ordering errors — the chain cannot VACATE 4s.
    Madelung fails at the same two elements for the same reason: **neither is a filling-ORDER statement.** The
    anomalies are exchange-driven occupancy transfers, outside what any n+ℓ ordering claims. Limit of the
    ADD-ONLY CHAIN, declared in advance.
(7) PC3D-10 HELD 10/10 (entrant == argmax|Δ|); PC3D-11 HELD 4/4 (centrifugal gate, 5g at Z=21..24). Δ still has
    never made a call D did not make; NOT promoted.
(8) **F39.2 GUARD VINDICATED ON THE HARDER CASE.** Drops rose from 3 steps to **13 of 29** (4d, 5d, 5g) —
    four times more frequent — and **0 UNSAFE on all 29.** Repair stays unbuilt.

## 3 · Next chat, in order
(1) **EXTEND THE CHAIN Z=31 UPWARD. NOTHING ELSE OPENS UNTIL THE WALK MOVES** (s40 ruling 3, standing).
    Cost measured: **~45 s/step across the whole 3d row**, flat — cheaper than the ~55 s at Z=20 and far below
    the feared 300 s. Segment 3 steps per call. Near targets: **Z=36/37 (4p→5s) and the 4d/5s crossover at
    Z=39..41**, where PC3D-10 (argmax|Δ|) is expected to make its first break and the hydrogenic term begins to
    decide. Write PREDICTION-CHAIN-4d BEFORE pointing nlchain at Z=37.
(2) **A CONFIGURATION COLUMN IS NOW REQUIRED IN nlchain**, not optional: finding (5) proves the `ok` flag and the
    configuration disagree at four of ten elements in a row. Score BOTH, always, and never report the entrant
    score alone as "the chain reproduces the row."
(3) PV-3 frozen-vs-relaxed — still owed, still load-bearing for the Ac 5f positive Δ (s40 §2b(11)).
(4) Z=109..120 under the s40 ruling. (5) Reverse derivation to Schrödinger — light end anchored, 3d row now anchored.
(6) T4 LAST: R 1701-1966.

## 4 · Figures (§H.6) MEASURED: none entered. RECALLED-NOT-ENTERED: record ground configurations Z=21..30
(comparison column only). CHOSEN: unchanged from s40 (seed, candidate rule, grid 4000/2e-5, qtail 1/2, HF maxit 100,
frozen avg-of-config). DERIVED: rest, including the hydrogenic reference −1/(2n²), which is arithmetic.

## 5 · Files (pack41): PREDICTION-CHAIN-3D · FINDING-CHAIN-3D · f392_guard.py · nlchain.jsonl (29 rows) · this
bridge · CENSUS-SESSION-41-OPEN · GATES-41-OPEN.log.
GATE 77 proposed: `python3 f392_guard.py` → 29 scored, 13 drops, 0 UNSAFE, exit 0, ~0 s.
GATE 78 proposed: `python3 nlchain.py show` → chained score 27/29, FIRST DIVERGENCE 25, ~0 s.

## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Grüneis-Kresse 2009 / Ren 2013).
Owed: T4; PR3; PN-3; La 4f+corr; PN4 s' channels; PV-3. DISCHARGED this session: the F39.2 repair module (closed
as NOT REQUIRED by ruling, with a guard in its place).
Known: bash egress DENIES network; web_search/web_fetch work. Known: ground.py caps at Z=108 (COLLECTION's limit,
R 1426). Known: nlchain's reference is the previous NEUTRAL's configuration on the CURRENT nucleus (F40.1).
Known (s41): nlchain scores the ENTRANT CHANNEL via rectag, which sees only occupancy increases — see finding (5).
