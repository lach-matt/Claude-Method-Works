# BRIDGE — THE LÖWDIN SESSION 45 (2026-08-19)
Successor to BRIDGE-LOWDIN-SESSION-44.md. Bank restore-point-2_13 (R 1700) UNCHANGED.
HANDOFF-44 verified at open **ok=939 bad=0 extra=0**. Gates 1-71: **283 lines, diff = 0,
byte-identical to GATES-44-OPEN.log** (gate 6's `sec` excluded). PT8 values exact
(3F/3H/4I, dsum 2.78e-17/0/0). Gates 72,73 SKIP. Gate 77: 47 scored, 30 drops, 0 UNSAFE.
Gate 78: 42/47, FIRST DIVERGENCE 25. Gates 79+80 PASS, 14 clauses. Gate 81 PASS.
Post-gate census **byte-identical to CENSUS-SESSION-44-POSTGATE.txt**.
**THE BLOCK IS LIFTED. THE WALK MOVED 47 -> 53 OF 107 STEPS. THE 5p ROW IS CLOSED.**

## 1 · Rulings (M, s45)
(1) "**Go**" — item 1 (the BLOCKING configuration column), then item 2 (the 5p row).
(2) "**Continue**" — the three-part structure of the law is REGISTERED (PARTS-OF-THE-LAW.md),
    the count stated as a FLOOR with the parts-2/3 merge left open pending the collapse test.
(3) **Not ruled, and it is no longer a question:** "which column is the score" was withdrawn
    by me as badly posed. The 1969 challenge names BOTH — item 1 (Madelung, filling order)
    and item 3 (Aufbau, ground configurations). **Both columns are load-bearing; neither is
    retired; neither is quoted alone.**
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 flags; comparison decides; no
scans; no constant beyond c; residue is not closure; T4 LAST; the n+l walk is the solution
format; a margin never quoted without its channel (F44.2); a gate is a script that can
return non-zero (F44.1).
**NEW GENERAL, adopted this session:** a gate whose expectation GROWS WITH THE CHAIN must say
so in its own text, or growth reads as divergence (the gate-77 note, now binding on gate 83).

## 2 · Findings (pack45)
(1) **THE CONFIGURATION COLUMN EXISTS AND COST NO PHYSICS.** `nlcfg.py` imports sealed
    `nlchain.py` and never patches it. No SCF re-run; `nlchain.jsonl` md5 unchanged across
    every invocation; two `show` runs byte-identical. **9 claims filed, 9 HELD, 0 FAILED.**
(2) **CONFIG 39/47 · STEP 42/47 AT Z=48; 45/53 · 48/53 AT Z=54.** FIRST CONFIG DIVERGENCE
    **24**, FIRST STEP DIVERGENCE **25**. The columns disagree at **11 of 53**.
(3) **NEITHER FAILURE SET CONTAINS THE OTHER** (cfg⊆ok False, ok⊆cfg False). Z=47 is the only
    step both fail. **The two columns are not one measurement with an offset**, and s44's
    BLOCKING call is vindicated rather than weakened.
(4) **THE INVERSION IS EXACT AND IT REPEATS.** At Cr(24) the step agrees and the state does
    not; at Mn(25) the state agrees and the step does not. Same signs at Cu(29)/Zn(30), at
    Tc(43), at Cd(48). A TRANSIENT promotion costs each column one row, and they are
    DIFFERENT rows. A PERSISTENT one (Nb->Ag) costs the state column every row until the
    shell fills.
(5) **EVERY CONFIGURATION FAILURE IN THE WHOLE CHAIN IS ONE DEFECT: `d-1 s+1`.** Eight
    failures, eight instances, magnitude 1 except Pd(46) where it is 2. **Never an f, never a
    p, never a wrong principal quantum number, never a wrong count.** s44 §2(6) lifted off the
    4d row onto the whole table: **what fails is not the n+l ordering and not the channel
    energetics — a one-electron-at-a-time walk has no PROMOTION OPERATOR.**
(6) **THE 5p ROW GOES 6/6 ON THE FIELD.** 5p entrant at all six, runner-up **6s** at all six
    with the identity never changing, margin 0.09460 -> 0.30462 monotone.
(7) **THE TIE-BREAK HOLDS ON A FOURTH PAIR.** 4s/3d 10/10, 4p/5s 6/6, 4d/5p 10/10,
    **5p/6s 6/6**. **32 steps, four unrelated pairs, no exception.**
(8) **THE 5p ROW DISCRIMINATES THE ORDERING VARIABLE — s44 §2(9)'s NEGATIVE IS REPAIRED.**
    The smallest-n open candidate is **4f (n=4)** at every step; the winner carries n=5. Plain
    `argmin n` is **wrong at six consecutive elements** where n+l is right at six. **The
    evidence for n+l over n goes from FOUR elements to TEN**, and for the first time rests on
    two mechanisms: a tie-break at equal n+l, AND an outright loss by the smaller-n channel.
(9) **4f IS HYDROGENIC. Zeff = 1.0005 ± 0.0010 ACROSS Z=39..54**, sixteen elements and
    sixteen added protons, flat to 1e-5 across the whole 5p row, and the deviation shrinks
    MONOTONICALLY toward 1 as Z rises. Hydrogenic 4f at unit charge is exactly -1/32 =
    -0.03125; measured -0.03128. **Inert to nuclear charge because perfectly screened.**
    Nothing fitted, no input but c. **FOUND, NOT PREDICTED — scored as a finding, never held.**
(10) **PC5P-10 HELD AS A PREDICTION AGAINST:** no half-shell signature at Sb(51) at the 1e-3
    level. Margin second differences 0.00183/0.00209/0.00220/0.00223, smooth and monotone.

## 3 · Faults registered this session
**F45.1 — THE README'S OWN GATE RECIPE BREAKS GATE 81.** The prescribed `sed` of the log name
  mutates root `gates_run.sh`, which is MANIFEST-LISTED (47bcbdd…). Run after the gate
  sequence, verify44.sh reports **ok=938 bad=1 extra=2**. Confirmed, then restored to
  47bcbdd… and re-verified bad=0. **A procedure that mutates a sealed file cannot precede the
  gate that checks sealed files.** Remedy adopted and carried into README-HANDOFF-45: sed into
  a SESSION-NAMED COPY (`gates_run45.sh`, sealed in pack45), root file untouched. Sub-fault:
  my stray `rt/gates_run.sh` put a 4th BAD in the post-gate census; removed, census then
  byte-identical to s44's. Caught before any scoring.
**F45.2 — GATES-44-OPEN.log's PT8 BLOCK IS NOT THE SCRIPT'S OUTPUT.** The sealed log carries a
  hand-condensed one-liner; `nlterm.py gate` emits three lines with sum_dets/sum_terms/
  mean-Eavg. **Every value agrees exactly** — but the block cannot be DIFFED, only read.
  R 1670's class: a summary standing where a run's output belongs. Per H.4 the sealed log is
  not rewritten; GATES-45-OPEN.log carries the script's true stdout and is the diff baseline
  from here.

## 4 · Predictions that FAILED, logged not suppressed
**PC5P-4 FAILED at the far end.** Filed D_ent ≈ -0.50 ± 0.06 at Z=54 and 0.05-0.06/proton;
  measured **-0.42783**, outside by 0.012, at 0.045-0.051/proton — below range at 5 of 5 steps.
  *Mechanism: the band was extrapolated from the 4p row. **The 5p row deepens ~15% more
  slowly, and the difference is the intervening 4d10 shell.** A band imported across a row
  that gained a filled d shell is a band imported across a change of screening.*
**PC5P-7 FAILED on one clause.** The bound held (|D_4f| < 0.10, 4f less bound than 5p at all
  six); **"4f deepens with Z" is FALSE** — see §2(9). The failure IS the finding.

## 5 · Next chat, in order
(1) **PREDICTION-4f-COLLAPSE, BEFORE Z=55 RUNS.** State where Zeff is expected to leave 1.
    The pre-collapse baseline is sixteen elements wide and the collapse must be MEASURED as a
    departure from it, not asserted. **BINDING, and it is the first thing the session does.**
(2) **PREDICTION-OPENINGS, BEFORE Z=57 RUNS** (PARTS-OF-THE-LAW §4b). La and Ac are the ONLY
    two elements where the step column can fail for a reason that is not a promotion. Same
    before Z=89. Sharpest single test the walk contains.
(3) **EXTEND THE CHAIN Z=55..108**, in Zeno segments. ~90-110 s per step at this width.
(4) **NAME THE CHANNEL FAILURES THROUGH `t7g_exc.HFCN`** — now owed on TWO unexplained onset
    boundaries: 5g at Z=46 (s44) and the 5d/5g exchange at Z=51->52 (s45).
(5) The PROMOTION OPERATOR — required by challenge item 3, defect shape `d-1 s+1` known,
    eight instances. Build now or after Z=120: **M's ruling, not yet given.**
(6) PV-3 frozen-vs-relaxed — Ac 5f positive Delta only. (7) Z=109..120 under the s40 ruling.
(8) Reverse derivation to Schrodinger. (9) T4 LAST: R 1701-1966.

## 6 · Figures (§H.6)
MEASURED: the six chain rows of §2(6); D_4f at Z=39..54 and the Zeff column; margin first and
second differences; the failing channel sets; the misplaced-electron table of
FINDING-CONFIG-COLUMN §2.
RECALLED-NOT-ENTERED: record ground configurations Z=49..54, placed UNDER PREDICTION before
the run and matching `ground.py` character for character. The 4d row's agree/disagree sets
were read from the s44 bridge at open — **PREDICTION-CONFIG-COLUMN §2 is TIMING-FLAGGED
(R 1449) and CONSISTENT-AT-BEST, NEVER HELD**; §1 (Z<=38) and §3 are the real prediction and
they held exactly.
CHOSEN: unchanged from s44 (seed, candidate rule, grid 4000/2e-5, qtail 1/2, HF maxit 100,
frozen avg-of-config). DERIVED: rest. **No constant entered beyond c = 137.035999.**

## 7 · Files (pack45)
PREDICTION-CONFIG-COLUMN.md · FINDING-CONFIG-COLUMN.md · nlcfg.py · PARTS-OF-THE-LAW.md ·
PREDICTION-CHAIN-5p.md · FINDING-CHAIN-5p.md · nlchain.jsonl (53 rows) · gates_run45.sh ·
this bridge · CENSUS-SESSION-45-{OPEN,POSTGATE}.txt · GATES-45-OPEN.log.
**GATE 83 (NEW, standing)**: `python3 nlcfg.py gate` -> PASS, exit 0, **8 clauses**, <5 s, no
SCF. Can-fail: `python3 nlcfg.py gate --fail` -> exit 1, 3 clauses trip (step 30's entrant
forced to 5s IN MEMORY; jsonl md5 verified unchanged). **Its expectations are the Z<=48
values and MUST be restated now that the chain reads 53 rows — see §1(NEW GENERAL).**
**Stated limit of the can-fail:** `ok_fail` is unchanged under `--fail` **BY CONSTRUCTION**,
not by insensitivity — the driver reads `ok` from the sealed field. Not evidence of anything.

## 8 · Unread / owed
Unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Grüneis-Kresse 2009 / Ren 2013).
Owed: T4; PR3; PN-3; La 4f+corr; PN4 s' channels; PV-3; the promotion operator; the channel
failures at two onset boundaries; **gate 83's expectations restated for 53 rows**.
Known: bash egress DENIES network. Known: ground.py caps at Z=108 (R 1426).
Known: nlchain's reference is the previous NEUTRAL's configuration on the CURRENT nucleus
(F40.1). Known: shell order in `occ` is load-bearing — build configs via `nlchain.add`
(F42.2). Known: `margin` does not name its runner-up; read `order[1]` (F44.2).
Known (s45): the gate recipe's sed must target a session-named copy (F45.1).
Known (s45): GATES-44-OPEN.log's PT8 block is not diffable; use GATES-45-OPEN.log (F45.2).
