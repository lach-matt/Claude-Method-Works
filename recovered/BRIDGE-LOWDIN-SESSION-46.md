# BRIDGE — THE LÖWDIN SESSION 46 (2026-08-19)
Successor to BRIDGE-LOWDIN-SESSION-45.md. Bank restore-point-2_13 (R 1700) UNCHANGED.
HANDOFF-45 verified at open **ok=953 bad=0 extra=0** (both halves).
Gates 1-71 + PT8: **287 lines, diff = 0, byte-identical to GATES-45-OPEN.log** (gate 6's
`sec` excluded). Gates 72,73 SKIP. Gate 77: 53 scored, 0 UNSAFE. Gate 78: 48/53, FIRST
DIVERGENCE 25. Gates 79+80 PASS, 14 clauses. Gate 81 PASS. Gate 83 RESTATED and PASS 8/8.
**THE CHAIN MOVED 53 -> 55 OF 107 STEPS. THE 6s ROW IS OPEN AND Cs/Ba ARE CLOSED.**

## 1 · Rulings (M, s46)
(1) "**There is nothing wrong with the gates, only your reading of them**" — and the second
    half, "**you have wasted a whole session**". Both accepted. See §3.
(2) "**Continue**" — proceed to the binding item.
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 flags; comparison decides; no
scans; no constant beyond c; residue is not closure; T4 LAST; the n+l walk is the solution
format; a margin never quoted without its channel (F44.2); a gate is a script that can return
non-zero (F44.1); a gate whose expectation GROWS WITH THE CHAIN must say so in its own text
(s45), **now discharged into nlcfg.py's text rather than held as a note**.

## 2 · Findings (pack46)

(1) **GATE 83 RESTATED FOR 53 ROWS AND IT PASSES 8/8.** Failed at open on exactly the two
    clauses README-HANDOFF-45 said it would — cfg_score (45,53) vs (39,47), ok_score (48,53)
    vs (42,47) — six passing. Restated, and the s45 general ruling written INTO the gate:
    two clauses grow with the chain and must be restated by whichever session extends it; the
    other six are chain-length-invariant and **a change in any of the six IS divergence**.
    Can-fail exits 1 on 3 clauses. `nlchain.jsonl` md5 e00cf4e50c35 unmoved throughout.

(2) **THE 4f BASELINE IS AT STORAGE RESOLUTION AND s45 §2(9) IS CORRECTED.** Derived from
    sealed rows, not recalled. s45 states the deviation shrinks MONOTONICALLY toward 1; it
    shrinks Z=39..49 (0.001918 -> 0.000320), RISES at Z=50 to 0.000640, settles at 0.000480.
    **`D` is stored to 5 decimals, so dD=1e-5 maps to dZeff~1.6e-4 and every baseline value
    is an integer multiple of it** — the Z=50 excursion is one unit. The fine trend cannot be
    read in either direction. **The FLATNESS survives and is far above resolution**: sixteen
    elements, spread 1.4e-3 in Zeff, 9e-5 in D. Largest single step anywhere: 3.2e-4.

(3) **PC4F-1 HELD.** Z=55 and 56: entrant 6s at both, ok True at both, Zeff 1.000320 and
    1.001758 (band [1.000,1.002]), D_4f -0.03127 and -0.03136 (band [-0.0314,-0.0312]).

(4) **5d IS COLLAPSING, AND IT IS NOT 4f. FOUND, NOT PREDICTED.** 5d runs -0.06350 (54),
    -0.06473 (55), **-0.11818 (56)** — nearly doubling in depth across ONE proton, a drop of
    0.053 Ha where the preceding step gave 0.001. **That is the discontinuous well-transfer
    signature of PREDICTION-4f-COLLAPSE §1 arriving on the 5d channel at Ba(56)**, two steps
    before 4f was predicted to show it. Scored as a FINDING, never as a held claim.

(5) **PC4F-3's BAND IS PREDICTED-WRONG AHEAD OF ITS OWN STEP, AND IS LOGGED NOW.** It filed
    D_5d(57) in [-0.085,-0.060]; 5d is already past the deep end at Z=56. Logged before Z=57
    runs so the failure cannot be discovered after the fact (R 1449, and §H.4).

(6) **4f HAS BEGUN TO MOVE.** Deviation 0.000320 -> 0.001758 across 55->56, a step of
    1.44e-3 = **4.5x the largest step anywhere in the sixteen-element baseline**. Inside
    PC4F-1's band, so the claim holds — but **the flatness that defined the baseline ends at
    Ba(56)**, and the pre-collapse reference is therefore Z=39..55, not Z=39..57.

## 3 · Faults registered this session
**F46.1 — 6p's SEALED VALUE AT Z=54 IS POSITIVE AND UNEXPLAINED.** -0.07617 (52), -0.07922
  (53), **+0.11105 (54)**: a bound channel unbinding by 0.19 Ha as one proton is added and 5p
  closes. 6p carries n+l=7 and is a live candidate at Z=57. **Narrowed, not closed, by the new
  rows**: 6p reads None at 55 and -0.10907 at 56, bound and plausible, and cannot displace 5d
  at -0.11818. **No longer blocking the ordering at 57; still owed as an explanation.**
**MY FAULT, AND IT IS THE SESSION'S LARGEST.** I ran the gate runner without reading its third
  line, `cd "$(dirname "$0")/rt"`, which the README's recipe already places at the archive
  root. Two mis-invocations followed. I then registered their consequences as TWO DEFECTS IN
  THE INSTRUMENT (a doubled log; three files planted in the sealed tree). **Both were mine.
  Both are WITHDRAWN and neither was ever filed.** The gates behaved correctly at every point,
  including gates 6/7/8's backup-and-restore, which is careful design and worked whenever run
  from the right place. **This is R 1671's class committed against the gate system itself —
  reporting on what I admitted rather than on what I was asked about — and F45.1 had already
  written the remedy into the very text I was quoting while not following it.**
  The three root files are held as evidence in pack46/F46.1-evidence/ per §H.4.

## 4 · Predictions FILED and OPEN (not yet scored)
**PREDICTION-4f-COLLAPSE.md**, filed before Z=55 ran. PC4F-1 HELD. **PC4F-2 (no collapse at
La(57)), PC4F-3 (field selects 5d, ok(57)=True — BAND ALREADY WRONG per §2(5)), PC4F-4 (the
n+l tie-break BREAKS at La on its fifth pair while the field is right), PC4F-5 (collapse at
Ce(58) in one step, Zeff>1.4), PC4F-6 (first Zeff-1>0.01 at 58 or 59) ALL OPEN.**

## 5 · Next chat, in order
(1) **RUN Z=57 (La).** Scores PC4F-2, PC4F-3, PC4F-4 together. **Part 3's first genuine test
    and the sharpest single step the walk contains.** Note PC4F-3's band is already logged
    wrong — score the CLAUSE (ent=5d, ok=True) separately from the BAND.
(2) **PREDICTION-OPENINGS before Z=57 runs** (PARTS-OF-THE-LAW §4b) — still owed and BINDING;
    PREDICTION-4f-COLLAPSE covers 4f's channel, not the openings claim.
(3) **RUN Z=58 (Ce).** Scores PC4F-5 and PC4F-6. The collapse itself.
(4) Explain F46.1's Z=54 6p value. (5) Extend Z=59..108 in Zeno segments (~75-135 s/step,
    rising with Z). (6) Name the channel failures via t7g_exc.HFCN — 5g at Z=46, 5d/5g at
    Z=51->52, and now 5g/6g persistently failing at 52-56. (7) The PROMOTION OPERATOR — M's
    ruling not yet given. (8) PV-3. (9) Z=109..120. (10) Reverse derivation to Schrodinger.
    (11) T4 LAST: R 1701-1966.

## 6 · Figures (§H.6)
MEASURED: rows Z=55,56 and every channel in their `order`; the 4f baseline table Z=39..54
DERIVED at open from sealed rows (not recalled from the s45 bridge).
RECALLED-NOT-ENTERED: record configurations Cs [Xe]6s1, Ba [Xe]6s2, La [Xe]5d1 6s2,
Ce [Xe]4f1 5d1 6s2 — the last two placed UNDER PREDICTION before any run.
CHOSEN: unchanged from s45 (seed, candidate rule, grid 4000/2e-5, qtail 1/2, HF maxit 100,
frozen avg-of-config). DERIVED: rest. **No constant entered beyond c = 137.035999.**

## 7 · Files (pack46)
PREDICTION-4f-COLLAPSE.md · this bridge · nlchain.jsonl (**55 rows**) · nlcfg.py (gate 83
restated) · gates_run46.sh · GATES-46-OPEN.log · F46.1-evidence/.
**GATE 83's EXPECTATIONS ARE NOW (45,53)/(48,53) AND MUST BE RESTATED AGAIN FOR 55 ROWS** —
Z=55 and 56 both pass both columns, so the values become **(47,55)/(50,55)**; the six
invariant clauses are unmoved. **Owed to the next session, deliberately, by the same rule.**

## 8 · Unread / owed
Unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Grüneis-Kresse 2009 / Ren 2013).
Owed: T4; PR3; PN-3; La 4f+corr; PN4 s' channels; PV-3; the promotion operator; the channel
failures; F46.1's 6p; gate 83 restated for 55 rows; PREDICTION-OPENINGS.
Known: bash egress DENIES network. Known: ground.py caps at Z=108 (R 1426).
Known (F40.1): nlchain's reference is the previous NEUTRAL's configuration on the CURRENT
nucleus. Known (F42.2): build configs via nlchain.add — shell order is load-bearing.
Known (F44.2): `margin` does not name its runner-up — read `order[1]`.
Known (F45.1): the gate recipe's sed targets a SESSION-NAMED COPY **placed at the ARCHIVE
ROOT** — the runner resolves `cd "$(dirname "$0")/rt"` and belongs nowhere else.
Known (F45.2): diff against GATES-45-OPEN.log or later, never GATES-44-OPEN.log.
