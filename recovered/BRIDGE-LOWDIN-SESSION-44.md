# BRIDGE — THE LÖWDIN SESSION 44 (2026-08-19)
Successor to BRIDGE-LOWDIN-SESSION-43.md. Bank restore-point-2_13 (R 1700) UNCHANGED.
HANDOFF-43 verified **ok=923 bad=0 extra=0** — the FIRST verify to run both halves.
Gates 1-71 at open: **283 lines, diff = 0, BYTE-IDENTICAL to GATES-43-OPEN.log**, gate 6's
sec field included. PT8 pass (2.78e-17 / 0 / 0). Gates 72, 73 SKIP. Gate 77: 37 scored,
20 drops, 0 UNSAFE. Gate 78: 35/37, FIRST DIVERGENCE 25. Gates 79 and 80 PASS through a
NEW DRIVER and can-fail in both directions (F44.1). Gate 81 PASS, can-fail exhibited.
**THE WALK MOVED: chain 37 -> 47 of 107 steps. THE 4d ROW IS CLOSED.**

## 1 · Rulings (M, s44)
(1) "**B**" — F44.1's remedy takes form (b): a driver in pack44, sealed pack files imported
    and never patched, README gate text corrected in the NEW README, not in the sealed one.
(2) "**Go**", "**Continue**" — the gate sequence, then the 4d row, then the seal.
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 flags; comparison decides; no
scans; no constant beyond c; residue is not closure; T4 LAST; the n+l walk is the solution
format; Delta is a scored column only.
**NEW GENERAL, adopted this session:** a margin is never quoted without the channel it is a
margin against (F44.2); a gate is a script that runs and can return non-zero, not a sentence
in a README (F44.1).

## 2 · Findings (pack44)
(1) **THE 4d ROW GOES 10/10 ON THE FIELD.** 4d is the entrant at every one of Z=39..48, the
    runner-up is 5p at all ten and never changes identity, the margin widens monotonically
    0.04367 -> 0.41607, and no winning channel failed to converge. Chained **42/47**.
(2) **10 CLAIMS HELD, 1 CONSISTENT-BY-FLAG, 0 FAILED.** Second clean sweep in a row, on the
    hardest row in the table.
(3) **THE n+l TIE-BREAK HOLDS ON A THIRD PAIR.** Clause 2 (smaller n first) held 10/10 on
    4s/3d, 6/6 on 4p/5s, and now **10/10 on 4d/5p**. 26 steps, three unrelated pairs, no
    exception. It is not a property of any pair it was found on.
(4) **THE ROW'S REAL RESULT: THE SCOREBOARD MEASURES THE WRONG OBJECT.** Configuration
    agrees at **4/10** (Z=39,40,43,48). `ok` reports **7/10**. They disagree at **SEVEN of
    ten — 41,42,43,44,45,46,48 — the exact set filed in advance**. At Tc(43) and Cd(48) the
    chain's configuration equals the record's character for character AND `ok` is False:
    `rectag` reads the record's STEP, the walk produces a STATE, and where the record's
    previous element is anomalous the two are not comparable.
(5) **PC4P-7's TRIGGER IS MET SEVEN TIMES OVER. THE CONFIGURATION COLUMN IS NOW BLOCKING.**
    s42 §4(3) is upgraded from OWED to BLOCKING. **42/47 must not be quoted as a
    configuration score again until the column exists.**
(6) **THE 4d ANOMALIES ARE NOT IN THE ENTRANT CHANNEL.** Nb, Mo, Ru, Rh, Pd, Ag are all
    s->d promotions of ALREADY-PLACED electrons. A one-electron-at-a-time walk cannot
    express them and does not attempt to. **What fails at Nb is not the n+l rule; it is the
    walk's format.** The sharpest statement the row produces, and it is about the SOLUTION
    FORMAT.
(7) **THE HALF-SHELL IS THERE AND IS FOUR ORDERS TOO SMALL.** Predicted in advance and found
    where predicted: second difference changes sign at 41->42, per-proton step minimum at
    Z=42, chain config `[Kr]4d5 5s2` at Z=43. Magnitude **6e-5** against anomalies living at
    1e-2. **Exchange stabilisation at 4d5 cannot be the mechanism for Nb/Mo/Ru/Rh/Pd/Ag.**
(8) **PD-6's argmax|Delta| EXCEPTION SET IS STILL EMPTY** with ten new steps in, and
    **PC3D-10's expected first break at Z=39..41 DID NOT ARRIVE** — predicted against, held.
    PD-5's 4f trace extends to Z=48 at |Delta| <= 1.2e-4.
(9) **argmin n IS UNCHANGED AT {19,20,37,38} ACROSS THE WHOLE ROW — AND THIS WAS FILED AS ITS
    OWN NEGATIVE.** 4d carries n=4 and beats 5p and 6s; no smaller-n candidate is open, so n
    and n+l agree at all ten. **THIS ROW DOES NOT DISCRIMINATE THE ORDERING VARIABLE.** Saying
    so before the run is what stops a null being read as support. The evidence for n+l over n
    still rests on FOUR elements — K, Ca, Rb, Sr — from two rows.
(10) **THE d-CHANNEL FAILURES ARE SYSTEMATIC AND NOW DIAGNOSABLE.** 5d and 6d fail at all ten
    steps; 5g joins at exactly Z=46. 23 failures, none touching a winner, `nfail` explicitly
    unpredicted. The 5g onset at Z=46 is stated and NOT explained.

## 3 · Faults registered this session
**F44.1 — TWO GATES WERE SPECIFIED AGAINST MODULES WITH NO ENTRY POINT, AND ONE EXITED 0
  WHILE COMPUTING NOTHING.** Gate 79 was `python3 t7e_probe.py`; that module has no
  `__main__`, so it imported its dependencies and exited 0 having compared nothing —
  **a pass that was never a check, carried through two sessions**, adopted in s42
  specifically to protect the instrument that produced that session's finding. Gate 80 named
  `D_of`/`run`/`CFG_CA` on `t7g_exc`, where they do not exist (they are in `t7f_rep`); it
  failed loudly and was therefore harmless. **R 1671's class reaching the gate ledger: a
  module with no entry point does not fail its gate, it fails to be a gate.** Remedied under
  M's ruling (b) — see §4(0). **Sub-finding: under `--fail 80` the ITERATION-COUNT clause did
  not trip on a subclass shifting every eigenvalue by 1e-4. `it` is not evidence of inertness
  on its own**; D and eps_ent are the discriminating clauses.
**F44.2 — s43 ATTRIBUTED THE 4p MARGIN NARROWING TO 4d; THE SAME SEALED ROWS SAY THE
  RUNNER-UP IS 5p.** `margin` is winner-minus-runner-up and does not name the runner-up;
  `order` does. At Z=37 the runner-up is 4d, at Z=38 it is **5p**, with 4d pushed to third.
  **The two numbers s43 compared are gaps between different pairs of channels.** The 5s-4d
  gap actually moved 0.07991 -> 0.07799, a narrowing of 0.00192 against the 0.02352 reported.
  Same class as F43.2 — a cause asserted without reading the column that carries it — and
  worse in one respect: **it was filed as a MEASURED APPROACH, exempt from R 1449 scoring, so
  nothing was set up to catch it.** Every number in the 4p row is untouched; §2(4) of s43,
  the argmin-n finding, stands. Per H.4 the sealed files are not rewritten.

## 4 · Next chat, in order
(0) **DONE THIS SESSION, recorded so it is not re-owed:** the verifier's completeness half
    (F43.1) was already in verify43.sh at the seal — run, and can-fail exhibited by planting
    a file (extra=1, exit 1). **Gate 81 is a standing gate.** Gates 79/80 likewise, via
    `gate7980.py`.
(1) **THE nlchain CONFIGURATION COLUMN — NOW BLOCKING (F44.2 §5, finding 5).** Seven
    disagreements in one row. Write **PREDICTION-CONFIG-COLUMN** first. The column must carry
    the chain's own state and compare it to the record's STATE, beside the existing `ok`
    which compares STEPS. Both stay; comparison decides which is the score.
(2) **EXTEND THE CHAIN Z=49..54 — THE 5p ROW.** Write **PREDICTION-CHAIN-5p** BEFORE pointing
    nlchain at Z=49. Regular row, no recorded anomaly, tests the 5p/6s tie-break — the
    FOURTH pair.
(3) **NAME THE 23 CHANNEL FAILURES THROUGH `t7g_exc.HFCN`** — inert, bit-identical to the
    parent, and it carries (Z, n, l, e, nd, target). No new physics, and the 5g onset at
    Z=46 gets an eigenvalue and a node target instead of a count.
(4) PV-3 frozen-vs-relaxed — Ac 5f positive Delta only.
(5) Z=55..108, then Z=109..120 under the s40 ruling.
(6) Reverse derivation to Schrodinger. (7) T4 LAST: R 1701-1966.

## 5 · Figures (§H.6)
MEASURED: the ten chain rows of §2(1); the per-proton steps and second differences; the
runner-up identity at all ten steps; the 4d/5p promotion 0.09903 vs 0.03376 across 38->39;
PD-6's two exception sets; the 23 `nfail` channels; gate 80's D1 pair (-0.266643, it [30,35]);
PP-0's |de| = 6.67e-10 and log(nrm) = -2.825e-09.
RECALLED-NOT-ENTERED: record ground configurations Z=39..48 (comparison column only) — and
they were placed UNDER PREDICTION before the run and match `ground.py` character for character.
CHOSEN: unchanged from s43 (seed, candidate rule, grid 4000/2e-5, qtail 1/2, HF maxit 100,
frozen avg-of-config). DERIVED: rest. **No constant entered beyond c = 137.035999.**
TIMING-FLAGGED (R 1449): Z=39's D_ent magnitude only — s42's probe value -0.195614 was read at
this session's open. The run returned -0.19561. Scored CONSISTENT, never HELD.

## 6 · Files (pack44)
PREDICTION-CHAIN-4d.md · FINDING-CHAIN-4d.md · FAULT-F44-1.md · FAULT-F44-2.md ·
gate7980.py · nlchain.jsonl (47 rows) · this bridge · CENSUS-SESSION-44-{OPEN,POSTGATE}.txt ·
GATES-44-OPEN.log.
**GATE 79+80 (standing, driver adopted)**: `python3 gate7980.py` -> PASS, exit 0, 14 clauses.
Can-fail: `--fail 79` (PP-0a trips at 9.93e-08 vs bound 1e-8) and `--fail 80` (3 clauses trip
on a subclass shifting e by 1e-4), both exit 1. ~4 min for both gates.
**GATE 81 (standing)**: `bash verify44.sh` -> ok=N bad=0 extra=0. Can-fail by planting one
unlisted file -> extra=1, exit 1.
**GATE 82 (proposed)**: the 4d row reproduces — `python3 nlchain.py show | tail -3` gives
42/47 and FIRST DIVERGENCE 25, and the Z=48 chain config is `...4d105s2`. Can-fail.

## 7 · Unread / owed
Unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Grüneis-Kresse 2009 / Ren 2013).
Owed: T4; PR3; PN-3; La 4f+corr; PN4 s' channels; PV-3; **the nlchain configuration column
(BLOCKING)**; naming the 23 channel failures.
Known: bash egress DENIES network. Known: ground.py caps at Z=108 (R 1426).
Known: nlchain's reference is the previous NEUTRAL's configuration on the CURRENT nucleus
(F40.1). Known: shell order in `occ` is load-bearing — build configs via `nlchain.add`
(F42.2). Known (s43): `bad=0` alone does NOT establish the tree is the sealed tree (F43.1) —
**closed s44: verify44.sh runs both halves.**
Known (s44): `D_of`, `run` and `CFG_CA` live in `t7f_rep.py`, NOT in `t7g_exc.py` (F44.1).
Known (s44): `margin` does not name its runner-up; read `order[1]` (F44.2).
