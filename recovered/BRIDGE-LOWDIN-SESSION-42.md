# BRIDGE — THE LÖWDIN SESSION 42 (2026-08-18)
Successor to BRIDGE-LOWDIN-SESSION-41.md. Bank restore-point-2_13 (R 1700) UNCHANGED. HANDOFF-41 verified
ok=891 bad=0. Runtime layered 5 -> 18 -> 19..41 with .json (F38.1). Gates 1-71 at open: **283 lines,
diff = 0, BYTE-IDENTICAL to GATES-41-OPEN.log** including gate 6's sec field. PT8 pass (2.78e-17 / 0 / 0);
72, 73 SKIP as filed. Gates 74 (fkscale FEASIBLE, 13/13 on lam in [0.215,0.529], 315 pts), 76 (PD-4 37/37,
PD-6 exception set EMPTY, PD-1 175/176 sole failure Ac 5f +0.00188), 77 (29 scored, 13 drops, 0 UNSAFE),
78 (27/29, FIRST DIVERGENCE 25) all REPRODUCE. Census open ok=274 bad=0 nopack=3; post-gate ok=278 bad=3
(derive_P{,2,3}.json, gate-1-regenerated, as s37-s41). **Chain UNCHANGED at 29 of 107 steps** — no row run.

## 1 · Rulings (M, s42)
(1) "Prob first" — item (0) before the walk.
(2) "Test all three candidates and let the comparison decide" — no a priori selection among the repairs.
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 flags; comparison decides; no scans; no constant
beyond c; residue is not closure; T4 LAST; the n+l walk is the solution format; Delta is a scored column only.

## 2 · Findings (pack42) — the session's result is a REMOVAL, not an addition
(1) **PP-0 machinery gate passed BEFORE any 4d number was read**: probe root -0.3808072844 vs parent
    -0.3808072853, |de| = **8.4e-10**; log(nrm) at parent e = -2.8e-09. The probe IS the parent kernel.
(2) **BOTH BRIDGE-41 ALTERNATIVES REFUTED.** (a) "4d unbound": tail is **V*r = -1.000000** at r = 30, 60,
    100, 200, 298; `_ceff = Q-1 = 0` on a q=1 shell; the well holds nd = 1, 2, 3, 5 states at e < 0.
    (b) "outside the bracket's reach": the it2 seed **eh = -0.040180 has nd = 1 — the bracket STARTS ON THE
    CORRECT STATE** and then walks DOWN out of the node window because log(nrm) > 0 throughout it.
(3) **THE THIRD MECHANISM, UNPREDICTED, TIMING-FLAGGED (R 1449).** it1: e = -0.047224, **nd = 1, correct**.
    it2: e = -0.092513, nd = 0, raise. **The solution EXISTS at it1 and is GONE at it2.** 421-point scan of
    it2's node-1 window: **zero sign changes; min log(nrm) = +0.892, norm 2.44x too large — structural.**
    This positively diagnoses s41's failed repair: t7d_node moved the SEED, but the root was absent from
    THE FIELD, not from the seed's neighbourhood.
(4) **ALL THREE REPAIRS FAIL D2. The comparison decided AGAINST all three.** (i) NodeGated fails loudly and
    for its predicted reason (`minlog=+0.9083`); (ii) mixing damping fails at beta = 0.20, 0.10, 0.05, 0.02
    — **so it is not a step-size problem** and PR-2's reason is refuted; (iii) ChannelHold's pass is
    **SPURIOUS** — at its own fixed point the UNMODIFIED parent returns e = -0.083545, nd = 0, and raises;
    one root in (-0.12,-0.015), nd 0->0. **It converged by not solving the channel.** Caught ONLY because
    D3's cross-check was fixed in advance.
(5) **THE FOURTH OUTCOME IS TRUE AND IT IS NOT A FAULT.** The self-consistent field of [Ar]4s^2 4d^1 at
    Z=21 has no normalisable 1-node solution. **Neutral Sc has no self-consistent 4d channel — the field is
    answering correctly, through the wrong exception.** Consistent with s41's own 3d-collapse finding.
(6) **THEREFORE F39.2 IS NOT A BLOCKER — MEASURED.** DIAGNOSTIC, config RECALLED-NOT-ENTERED:
    **Z=39 [Kr]5s^2 + 4d: D = -0.195614, eps(4d) = -0.231503, converged it=34, NO RAISE.**
    **4d CONVERGES CLEANLY WHERE IT MUST WIN.** s41's promotion rested on "drops 10/10 since Z=21, so it
    cannot win at Z=39" — refuted: the field at Z=39 is a different field. Same per-element-to-universal
    fault as R 1675, committed against a census of my own drops. **NO REPAIR REQUIRED. WALK NOT BLOCKED.**
(7) **PV-3 IS NOT THE PREREQUISITE FOR THE 4d ROW.** Still owed, still load-bearing for the Ac 5f positive
    Delta only. s41 §2b(11) is superseded.

## 3 · Faults registered this session
**F42.1** — an `&&` chain misfired and re-ran gates 1-8, APPENDING to GATES-42-OPEN.log (283 -> 312).
  Caught before anything was read from it. Repaired by splitting: OPEN restored to 283 lines, **diff = 0**
  vs s41; the re-run filed as GATES-42-CLOSE-1-8.log, **byte-identical to the open segment**, 8/8 rc=0.
  No result affected. Failure mode named: an append-mode log is not idempotent under re-run.
**F42.2** — **SHELL ORDER IN `occ` IS LOAD-BEARING AT FINITE TOLERANCE.** `nlchain.candidates` returns
  (n,l) PAIRS and `nlchain.add` SORTS; a hand-built config that appends instead of sorting shifts D by
  **2.9e-4 Ha**. Caught in D1 BEFORE any candidate was scored. Any future harness MUST build configs
  through `nlchain.add`, never by list concatenation.

## 4 · Next chat, in order
(1) **THE WALK MOVES: EXTEND THE CHAIN Z=31..38** (s40 ruling 3, standing; nothing else opens until it
    moves). ~45 s/step measured flat across the 3d row; segment 3 steps per call. Write
    **PREDICTION-CHAIN-4p** BEFORE pointing nlchain at Z=31. Near targets: Z=36/37 (4p->5s) and the
    4d/5s crossover at Z=39..41, where PC3D-10 (argmax|Delta|) is expected to make its first break.
(2) **M's RULING OWED: adopt (i) NodeGated's EXCEPTION ONLY?** Not its bracket. It is inert on every
    healthy channel (D1 identical to 5 dp) and it names the condition where the parent says "nodes 0".
    Diagnostic upgrade; opens no row, changes no number. NOT adopted without the ruling.
(3) **A CONFIGURATION COLUMN IS REQUIRED IN nlchain** (s41 finding 5, still owed): the `ok` flag and the
    configuration disagree at 4 of 10 elements in the 3d row. Score BOTH, always.
(4) PV-3 frozen-vs-relaxed — owed for Ac 5f positive Delta only, no longer gating the 4d row.
(5) Z=109..120 under the s40 ruling. (6) Reverse derivation to Schrodinger. (7) T4 LAST: R 1701-1966.

## 5 · Figures (§H.6)
MEASURED: 4d probe quantities at Z=21 (tail V*r, node spectrum, it1/it2 eigenvalues, min log(nrm));
D1 reference -0.266643; the three candidates' D1/D2 outcomes; Z=39 diagnostic D = -0.195614.
RECALLED-NOT-ENTERED: the Z=39 [Kr]5s^2 configuration (DIAGNOSTIC ONLY — **not a chain row, must not be
scored as one**); record ground configurations Z=21..30 (comparison column only, from s41).
CHOSEN: unchanged from s41 (seed, candidate rule, grid 4000/2e-5, qtail 1/2, HF maxit 100, frozen
avg-of-config). **beta is CHOSEN-CONVERGENCE-CONTROL** — varied 0.4/0.2/0.1/0.05/0.02 in this session's
comparison and NO adopted number depends on it. DERIVED: rest.

## 6 · Files (pack42)
PREDICTION-PROBE-4D · FINDING-PROBE-4D · PREDICTION-REPAIR-4D · FINDING-REPAIR-4D · t7e_probe.py ·
t7f_rep.py · this bridge · CENSUS-SESSION-42-{OPEN,POSTGATE} · GATES-42-OPEN.log · GATES-42-CLOSE-1-8.log.
**GATE 79 proposed**: `python3 -c "import t7e_probe,t7f_rep"` then the PP-0 gate -> probe root vs parent
|de| < 1e-8 on Z=21 3d. Can-fail, ~5 s. It protects the instrument that produced this session's finding.

## 7 · Unread / owed
Unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Grüneis-Kresse 2009 / Ren 2013).
Owed: T4; PR3; PN-3; La 4f+corr; PN4 s' channels; PV-3; nlchain config column.
**DISCHARGED this session: F39.2 — closed as NOT A FAULT by measurement at Z=39, and the three candidate
repairs closed as NOT ADOPTED by comparison.** t7d_node.py (s41) remains sealed as an attempt with a
negative result, now positively diagnosed.
Known: bash egress DENIES network; web_search/web_fetch work. Known: ground.py caps at Z=108 (R 1426).
Known: nlchain's reference is the previous NEUTRAL's configuration on the CURRENT nucleus (F40.1).
Known (s42): shell order in `occ` is load-bearing — build configs via `nlchain.add` (F42.2).
