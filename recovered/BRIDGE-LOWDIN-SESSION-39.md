# BRIDGE — THE LÖWDIN SESSION 39 (2026-08-18)
Successor to BRIDGE-LOWDIN-SESSION-38.md. Bank restore-point-2_13 (R 1700) UNCHANGED. HANDOFF-38 verified 842/842. Runtime layered
5 -> 18 -> 19..38 with .json (F38.1). Gates 1-71 at open: **71/71 BYTE-IDENTICAL to GATES-38-OPEN.log, diff = 0 lines**, including
gate 6's sec field which differed at s38. PT8, 72, 73 as filed. Census open ok=268 bad=0; post-gate ok=271 bad=3 (derive_P{,2,3}.json,
gate-1-regenerated, as s37/s38). No fault at open.

## 1 · Rulings (M, s39)
(1) "run it as a feasibility interval" — F^k scale taken as feasibility, never as an adopted value.
(2) "What are we not adopting the attributed math?" — intermediate coupling preferred over a ζ/F² threshold diagnostic, on the
    ground that a threshold is a selection rule chosen here and therefore a fitted constant in a diagnostic's coat.
(3) "How does any of this help us reach the n+l lowdin solution?" — THE CORRECTION THAT REDIRECTED THE SESSION. The 13 rows are
    the exceptions; a rule cannot be derived from the set of its counterexamples. IC dropped.
(4) "Doing 1 first answers 2 which then defines 3" — walk to completion FIRST; the ordering mechanism follows from it; Th's
    status is then defined by the margin distribution, not fixed by a mechanism.
(5) "everything above 108 will be identified as theoretically predicted based on measured NIST values" — PROVENANCE RULE for the
    Janet-120 extension. NOT YET IMPLEMENTED; it is s40's first object. See §3(1).
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 flags; comparison decides; no scans; no constant beyond c;
residue is not closure; T4 LAST; the n+l walk is the solution format.

## 2 · Findings (pack39)
(1) FINDING-FK-SCALE. Interval FEASIBLE: 13/13 on lam in (0.2145, 0.5298), verified by crossing algebra AND by direct evaluation
    on a 1001-point grid (315 points). Rounding-robust: worst case (0.2158, 0.5288). Bound below by Th 0.2145, above by U 0.5298;
    ordering Th < U < Pa < Hf < Cm predicted exactly, 5/5. AND REFUSED ON THE CONSISTENCY LEG: physical band 0.70-0.90 (Cowan 0.85;
    measured Sn11+/12+ FIT/HFR F2 0.857, F4 0.884/0.877; localized actinides/rare earths 70-80% of HF). NO OVERLAP. At the physical
    scale the table scores 10/13 at lam = 0.70, 0.85 and 0.90 alike — WORSE than plain HF's 12/13. The linear-in-F^k family is
    closed entirely: the row-differential residual is NOT a multipole-magnitude problem. Failed: PF-3 magnitude (0.39+-0.08 vs
    0.5298) — I estimated U's gapHF from the CLASS-C MEAN when U's own shift is the table's extreme. F39.1, caught in scoring.
(2) FINDING-WALK-25. THE RULING FIELD COVERED ONLY 10-13 OF 25 FRONTIER Z. Twelve never walked on it (K Ca Ga Rb Sr In Cs Ba Tl
    Fr Ra Lr) now run: 12/12 — AND THE SCORE IS MOSTLY VACUOUS. 8 of 12 returned a SINGLE channel: the competitor (n-1)d is EMPTY,
    so the removal walk cannot see it. R 1671's fault one level up: the instrument narrowed its own input. PW-2 (Lr) is UNTESTED,
    not falsified — 6d never entered the removal list. PW-4 HELD where testable: margins Ga 0.210, In 0.188, Tl 0.247, Lr 0.163 Ha
    against the 13 exceptional rows' 0.0002-0.0914 — two to three orders. UNPREDICTED AND REGISTERED: the field reproduces the
    relativistic reversal at the bottom of groups 1 and 2 from the SR contraction alone, no fitted input — Fr -0.13186 more bound
    than Cs -0.12779, Ra -0.16021 more bound than Ba -0.15732, both matching the record's IE ordering.
(3) FINDING-CHAN-AUFBAU — THE SESSION'S RESULT. PE-0 machinery gate passed 4/4 before any result was read (ns reproduces
    nlwalk_hf D_rel to 5 dp). PE-1 HELD 4/4: ns binds deeper than (n-1)d at K 0.0897, Rb 0.0799, Cs 0.0631, Fr 0.0684 Ha.
    **n+l's ORDERING CLAUSE IS DERIVED on a parameter-free SR-HF field, at the elements where the rule holds, with the competitor
    channel empty.** PE-2 partly FAILED: K > Rb > Cs monotone, Fr REVERSES (0.0684 > 0.0631) — the same 7s contraction, mechanism
    named. PE-3 HELD: at Cs 5d -0.06473 binds twice as deep as 4f -0.03127; at Fr 6d -0.06345 against 5f -0.03128. THE n+l
    TIE-BREAK (lower n first, so 4f before 5d) IS VIOLATED AT THE CHANNEL LEVEL. The f channel is hydrogenic and inert until
    collapse — Cs and Fr agree to 5 dp across 32 protons.
(4) FINDING-CHAN-LIGHT. PL-1 HELD at Li (2s -0.19629 vs 2p -0.12862). **PL-2 HELD AT K: 4p -0.09363 binds DEEPER than 3d -0.05807.**
    PL-3 THEREFORE STANDS AND IS THE GENERAL STATEMENT: the tie-break fails at n+l=5 (K, no f shell in reach), at n+l=7 (Cs) and
    at n+l=8 (Fr). THE f COLLAPSE IS A SYMPTOM, NOT THE CAUSE.

### THE STATEMENT THE SESSION REACHED — n+l IS TWO LAWS, NOT ONE
CLAUSE 1 (order by n+l) is INSTANTANEOUS and DERIVABLE: it is a true statement about channel depths at the atom, produced by the
ruling field with no input. CLAUSE 2 (within equal n+l, lower n first) is NOT: it cannot be read off channel energies at any block
where the tie appears, and is recovered only along the FILLING SEQUENCE. Löwdin's problem resisted because the two clauses were
treated as one law. Th's 0.016 Ha residual sits against 0.06-0.09 Ha margins where the rule holds — a factor of 4-6 — so Th is
in the zero-crossing region the exceptions occupy by construction, NOT a defect in the field (M's item 3, now defined).

## 3 · Next chat, in order
(1) RULING (5) IMPLEMENTED: extend the walk to Janet-120. ground.py is the OBSERVED configurations Z = 1..108 (NIST ASD 5.12,
    R 1306) and RAISES KeyError above 108. Past 108 the entrant cannot be derived from a record that does not exist, so the driver
    must PREDICT the configuration — a change of operation, not a longer run. Everything above 108 carries the PREDICTED label.
    Design the predicted-configuration source and its provenance flag BEFORE any Z > 108 is run.
(2) F39.2 REPAIR: Na 3p fails the node check (nd=0, expected 1 — SCF fell to a 2p-like solution). Na 3p/3d unbanked. Blocks the
    light-end anchor that a reverse derivation to Schrodinger needs.
(3) Complete the empty-channel aufbau across every Janet block edge Z <= 108: Li Na Al Sc Y Ce Lu Th and the untested tie-breaks.
    Clause 1 is derived on 4 alkalis; it is not yet derived on the table.
(4) The f-collapse trace (Cs -> Ba -> La -> Ce on the 4f channel) — the mechanism clause 2 needs.
(5) PV-3 frozen-vs-relaxed, still untested; the frozen convention is USED and its bound NOT measured.
(6) Reverse derivation to Schrodinger — after (1)-(4). (7) T4 writing chat LAST: R 1701-1966.
DROPPED BY RULING: intermediate coupling; the zeta/F^2 threshold diagnostic; any adopted F^k scale.

## 4 · Figures (§H.6) MEASURED: none entered. RECALLED-NOT-ENTERED: record first-ionised subshells (25 rows); Cowan 0.85, Sn FIT/HFR
0.857/0.884/0.877, actinide/rare-earth 70-80% (all comparison only, sources in FINDING-FK-SCALE §3). CHOSEN: grid/tolerance
(4000 pts, 2e-5), qtail 1/2, HF maxit 100, channel rule, frozen avg-of-config (bound NOT measured). DERIVED: rest.

## 5 · Files (pack39): PREDICTION-FK-SCALE · FINDING-FK-SCALE · TABLE-FK · fkscale.py · PREDICTION-WALK-25 · TABLE-WALK25 ·
PREDICTION-CHAN-AUFBAU · TABLE-CHAN · PREDICTION-CHAN-LIGHT · this bridge · CENSUS-SESSION-39-{OPEN,POSTGATE} · GATES-39-OPEN.log.
Data appended: nlwalk_hf.jsonl (+12 Z, ruling-field coverage now 22 of 25), hf_chan.jsonl (6 -> 20 rows).
GATE 74 proposed: `python3 fkscale.py` -> FEASIBLE, interval (0.2145, 0.5298), 315 grid points, ~1 s.

## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Gruneis-Kresse 2009 / Ren 2013). Owed: T4; PR3;
PN-3; La 4f+corr; PN4 s' channels; PV-3. Known (s39): bash egress DENIES network but web_search/web_fetch DO work — that is how
the F^k source debt was paid. Known: ground.py caps at Z=108. Known: hf_chan.py takes one common ion reference per Z, which is
what makes its channels comparable — do not compare across Z without restating the reference.
