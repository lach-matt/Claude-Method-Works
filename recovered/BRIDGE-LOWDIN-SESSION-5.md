# BRIDGE — THE LÖWDIN SESSION 5 (2026-08-16)
Successor to LOWDIN-HANDOFF-4.md (read in full). Bank restore-point-2_13 (R 1700) UNCHANGED; nothing
written to register/index/store. Pack-4 verified 22/22. Context at handoff ~88%. Written under §H.10.
Everything this session produced is in LOWDIN-PACK-5.tar.gz (manifest MANIFEST-PACK-5.txt).

## 1 · M ruled this session, in order
1. Step 3 core rule: (c) BOTH — closed core (rule A) and charge 1 (rule B) — report disagreements.
2. Work in small batches; snapshot to outputs each batch so any point is a handoff point.
3. No bridge until 90% (§H.10 reserve).
4. A "miss" whose subshell opens at a neighbouring Z is a step offset, not a miss: score the OPENING
   SEQUENCE. (Applied: Step 3 misses reclassified timing / sequence.)
5. α (core polarisation) is NOT relevant to finishing the solution; it is accuracy work, later and
   separately ruled. Not run.
6. The solution is local — neutral to any one corridor, triggered at each step — with global reach in the
   diagonal skeleton; Löwdin asked for something that WORKS globally, not one formula. The claim is
   ASSEMBLY of published pieces, not novelty; the aim is to show the pieces were already found.
7. **NEXT TASK: an outside literature and art search for attributions** — who stated each rung, and
   whether the assembly itself has been stated — before any "first" is written. Needs network.

## 2 · Done (bridge-4 §3 Steps 2–4), all gated
- Kernel: TFD gate reproduced byte-identical (0.143/-0.010). Relaxed tolerances (rtol 1e-7, 40 shooting
  iters, npts 3000) gate 0.1427/-0.0103. C Numerov shoot (shoot.c, bit-identical) → eigenvalues free.
  n_used = n0+4, n0 by Madelung fill of N=Z-charge (matches gate hand-table 39/39; δ insensitive to offset
  0.141–0.146 over n0+2..+6, so no ordering enters the values). RECORDED CHOICE, not measurement.
- **Step 2**: `computed` grade regenerated for all 103,545 cells (56,929 (Z,charge,l) triples, Z 2–120)
  from TFD, parameter-free → COMPUTED-TFD.tsv (n_used, E, delta_tfd per row). Diagnostics separate,
  never merged: DIAG-Qfinal-minus-TFD.tsv (rms 0.359, mean -0.153; largest where the fit was unmeasured:
  charges 8–11 s/p, Z 119–120 s where Q.final=0 and TFD 5.7, Th/Pa ch1 f Qf 3.2 vs TFD 1.0);
  DIAG-measured-minus-TFD.tsv (60 overlapping cells: rms 0.086, mean -0.001).
- **Step 3** (step3.py, 106 brack.py steps, held out): rule A = core is the full subshells of Z-1's config
  minus any s beyond the last full p, charge Z-N_core (reproduces K I, Ca II, Sc III, Rb I, Y III, La III,
  Ce IV, Ac III, Th IV, Pa V, Lr III); rule B = charge 1 over Z-1's config. Entrant = argmin TFD E over
  brack.py candidates. **A 96/106, B 87/106, agree 90, disagree 16.** Record: fitted 99 (inadmissible),
  honest walk 92, Madelung 96. A gets La 5d and Ac 6d right.
  A misses: timing (Sr, Ce, Pr, Ra, Th — same subshell ≤2 Z away); sequence (Mn 4s, Tc 5s, Gd 5d, Cm 6d
  many-electron; Lr 7p relativistic). B's extra misses are the collapse openings 10–24 Z late (4p before
  3d, 6p before 5d/4f): the neutral-core object under-binds the collapsing orbital (R 1416, R 1457).
  → the entrant is read at the closed-core ion.
- **Opening sequence** (ruling 4): rule A 17/17 openings in the observed order 2s…6d 5f, incl. both
  inversions; offsets 4d −1, 6d −1, 5f −1, 4f +2, rest 0; 7p (Lr) not reached. B has 4p<3d, 6p<5d<4f.
- **Step 4** (step4.py): A's openings partition into n+l diagonals M=2..8 completing strictly in order,
  electrons 2,8,8,18,18,32; only within-diagonal departures from n-rule = the two collapses. Pairwise over
  ALL candidate energies: A lower-M binds first 1001/1148, violations 0 at charge 1 → ~40% by charge 12+
  (ion → hydrogenic; collapsed nd/nf outbinds (n+2)s); B 1137/1148 cross but 154/424 within-diagonal
  violations. → the diagonal is a threshold object read where the entrant is read, not a property of the
  spectrum at arbitrary charge (R 1626, R 1416 anticipated).
- **Reading**: chapter 34 is at R 1350 state (withdrawn form, "exceptionless 106", no assembly, no prior
  workers beyond Löwdin/Madelung/Janet/Seaton). Physics Compendium has Janet 1928 < Madelung 1936,
  Klechkovsky–Hakala, Löwdin named. Spectra Compendium has the Janet collapse coordinate (thresholds at
  block boundaries, 0.637 vs 0.036) and the charge→hydrogenic statement, unattributed. Latter, D-O,
  Belokolos, Goeppert-Mayer, GAC, Desclaux–Fricke, Eliav, TIM, Scerri, Bjerg–Solovej are in the REGISTER
  and LOWDIN-ASSEMBLY.md only. Not found in what I reached: Ostrovsky (own papers), Schwarz, Allen &
  Knight, Wang & Schwarz, Kitagawara & Barut. Read ~4k of 380k words, targeted; the bank (694 files) was
  not available.

## 3 · Next chat's work, in order
1. OUTSIDE LITERATURE/ART SEARCH FOR ATTRIBUTIONS (ruling 7). Per rung of LOWDIN-ASSEMBLY.md §1 plus:
   held-out leak test (any prior statement?), Helly-emptiness of one-parameter forms, exhaustive scoring
   of Latter/TFD entrants, the charge boundary of the diagonal. Candidates to check first: Ostrovsky
   1981/2001; Schwarz (& Wang) 2010 "aufbau"; Allen & Knight 2002; Kitagawara & Barut 1983; Scerri 2020
   review + refs; Bjerg & Solovej 2024; Belokolos 2017; Latter 1955 tables (still unread at source);
   Ac III 6d–5f at source; Ra II nf. Output: attribution table, one row per claim, with "already stated
   by / partly / not found", before any "first" is written.
2. Chapter 34 rewrite around the assembly in ruling 6's frame, with the compendia's pieces brought in
   and every prior worker named. Uses §2 of this bridge + LOWDIN-ASSEMBLY.md + Session 4 SOLVER-FINDING.
3. Register entries (below) and the index write (COMPUTED-TFD as the computed grade, under R 1715's
   ruling), each write regenerating all artefacts and both gates.

## 4 · Owed to the writing chat (cumulative)
R 1701–1715 (Sessions 1–4, unchanged) · R 1716 core ruling + rule A definition · R 1717 kernel (relaxed
tolerances, C shoot, gate held; n0 choice) · R 1718 Step 2 tables + diagnostics · R 1719 Step 3 A 96 / B 87,
disagreements = collapse steps, boundaries named · R 1720 opening-sequence ruling, 17/17 · R 1721 Step 4
skeleton and its charge boundary · R 1722 α ruling (not relevant to the solution) · R 1723 the local-law
frame + assembly claim (ruling 6) · R 1724 chapter 34 stale to R 1350; where the pieces sit · FLAG 2 ·
allocation ruling R 1701–1709 · CHAPTER-LOWDIN rewrite (now whole chapter). Still owed outside: Ra II nf;
Ac III 6d–5f at source; Latter's tables read.

## 5 · Faults / flags this session (R 1671 shape: recorded, not hidden)
- Detached background jobs DIE between turns; the container only advances during a tool call. Batching
  must be foreground, ≤~275 s per call (two calls exceeded the limit; one killed the job; checkpoints held).
- out/ was wiped once between turns; my snapshot then OVERWROTE the larger archive (Z 47–96 recomputed,
  ~30 min). snap.sh now refuses to shrink. Rule: a snapshot must never replace a larger one.
- An unexplained file DIAG-QFINAL-MINUS-TFD.tsv (03:50, schema not mine) appeared; set aside, unused.
- brentq for the TFD slope: no gain (1.63→1.51 s); not adopted.
- Rb I, Y III still absent from index measured grade (FLAG 1). Project files Löwdin_Challenge /
  Three-Body_Problem: generic, removal still M's call.

## 6 · Files
LOWDIN-PACK-5.tar.gz: this bridge · step2_run.py step3.py step4.py snap.sh shoot.c libshoot.so ground.py
· out/Z002..Z120.tsv · COMPUTED-TFD.tsv · DIAG-Qfinal-minus-TFD.tsv · DIAG-measured-minus-TFD.tsv ·
step3.json step3_rows.jsonl · step2.log · MANIFEST-PACK-5.txt. Bring with LOWDIN-HANDOFF-4.md,
LOWDIN-PACK-4, CODE-LOWDIN-2_13.txt, COORDINATES-2_13.csv, register, compendia. Resume any step:
python3 step2_run.py 5 120 (skips complete Z) · python3 step3.py 3 108 (skips done) · python3 step4.py.
