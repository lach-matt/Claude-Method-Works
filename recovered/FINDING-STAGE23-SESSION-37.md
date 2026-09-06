# FINDING-STAGE23 (s37) — the n+l walk, Stage 2 (SR HF no-corr DSCF frontier pairs, 13 d/s rows: nlwalk_hf.py/.jsonl + s35 lwalk_hf rows) and Stage 3
(SR local walk, KH kernel in SCF and orbitals, SIC in the energy only, TWO SIC conventions on one orbital set: nlwalk_sr.py/.jsonl, 122 entries = Stage 1's count).
Build gates: nlwalk_hf Lu 5d -0.15979 / 6s -0.21137 = lwalk_hf (s35); nlwalk_sr at CLIGHT=1e6 = Stage 1 Sc 3d -0.34175 / swap4s -0.26903 exactly.
Ruling (s37): (a) and (b) both run, comparison decides. Nothing entered; no constant; no measured input; record first-ionised subshells RECALLED-NOT-ENTERED
(comparison column only). All HF SCFs converged (Ac 5f never needed: item 4 stays held). Tables: TABLE-STAGE2-HF, TABLE-STAGE3-SR (pack37).
gap := D_d - D_s on the relaxed pair (positive: d shallower -> d leaves first). Record classes: s-first Sc Y La Ce Gd Th; d-first Lu Hf Ac Rf Pa U Cm.

## Stage 2 (SR HF, no correlation) — SCORE 12/13 (local Stage 1: 7/13); ruled 8 rows 7/8 (local 2/8)
gapHF: Sc -0.064 Y -0.003 La -0.034 Ce -0.031 Gd -0.0002 Th +0.008 | Lu +0.052 Hf +0.028 Ac +0.024 Pa +0.024 U +0.027 Cm +0.046 Rf +0.091.
THE THRESHOLD IS ZERO: gapHF < 0 on every s-first row and > 0 on every d-first row, EXCEPT Th at +0.008 (record s-first). Gd is a tie (0.2 mHa).
Pa/U (5f entrant): the shallowest HF removal is 6d (record removes 6d), 5f deeper by 0.015/0.055.
PH1 HELD 3/3 (Hf Ac Rf d-first) · PH2 HALF: Gd held (tie), Th FAILED (HF puts 6d shallower by 8 mHa — the named risk row, inside the no-corr margin)
· PH3 HELD 3/3 (Pa U Cm 6d shallowest) · PH4 FAILED (Rf 0.091 > 0.06; the others 0.024-0.052) · PH5 HELD (7/8; 12/13) · PH6 HELD.

## Stage 3 (SR local, per-electron SIC) — SCORE 9/13; f_orb SIC 7/13
gapSR(pe): Sc -0.064 La -0.008 Ce +0.003 Y +0.021 Th +0.032 Gd +0.036 || Ac +0.052 Hf +0.059 Pa +0.067 U +0.072 Lu +0.088 Cm +0.090 Rf +0.125.
THE SR LOCAL WALK ALSO SEPARATES THE CLASSES — the six s-first rows are the six smallest gaps and the seven d-first rows the seven largest, with the boundary
between Gd +0.036 and Ac +0.052 — BUT NOT AT ZERO: at threshold 0 it scores 9/13 (gains Hf Ac Pa U Cm Rf, loses Y Ce Gd Th). Its separating threshold is ~0.044.
POST-RESULT READING (analysis of the two tables, no new design): gapSR - gapHF = Y +0.024 La +0.026 Ce +0.034 Gd +0.036 Lu +0.037 Hf +0.031 Ac +0.028 Th +0.024
Pa +0.043 U +0.045 Cm +0.044 Rf +0.033: mean +0.034, sd 0.007 on the twelve n>=4 rows — and 0.000 at Sc (3d). The two fields differ on the d/s pair by a UNIFORM
offset on the nd/5d/6d rows and by nothing at 3d. That is the exchange seam of s34 (FINDING-XSEAM) seen on the pair, and the same size as the ~0.025-0.03
uniform 5d-row residual already on the record: the local kernel's d/s ordering is HF's plus a class-flat additive term of the local exchange treatment.
PS1 sign HELD 13/13 (SR moves every d row toward s-deeper); windows HELD 6/13 (periods 4-6 in window; Lu/Hf 0.073/0.083 just above 0.06; period 7
0.094-0.187 vs 0.05-0.10: sizes underestimated by ~1.5-2x on period 7 — mechanism below).
PS2 HALF: the count moved +2 (within +-3: held); "no threshold separates" FAILED — one does, at 0.044.
PS3 FAILED, AND THE FAILURE IS THE LARGER FINDING: SR lifts La 4f from -0.375 to -0.231 (shift +0.144), so 5d (-0.245) is now deeper than 4f at La. Across the
f rows the SR shift on the (n-2)f channel is La +0.14 Ce +0.15 Gd +0.19 Ac +0.20 Th +0.25 Pa +0.26 U +0.27 Cm +0.33 — 5-10x the < 0.03 predicted. Mechanism:
the direct SR term on an f orbital is small, but the SR CONTRACTION of the s/p shells inside the f radius completes their screening — the indirect
relativistic expansion of d and f — and it scales with Z. Consequence for PN2: under SR the local kernel puts f deepest ONLY where the record has f
occupied/entering (Ce Gd Pa U Cm) and puts d deeper than f where the record enters d (La 4f -0.231 vs 5d -0.245; Ac 5f -0.103 vs 6d -0.248; Th 5f -0.238 vs
6d -0.275); Cs Ba Fr Ra keep f shallowest. THE (n-2)f COLLAPSE OF STAGE 1 WAS A NON-RELATIVISTIC ARTEFACT OF THE LOCAL KERNEL, NOT AN EXCHANGE FAULT: SR local
now reproduces the record's f onset (4f at Ce not La; 5f at Pa not Ac/Th) on all 12 f-frontier rows — the local field agrees with HF (s36) on this frontier.
PS4 HELD: f_orb SIC removes most of a single d/f electron's SIC; every open d/f channel moves shallower by 0.10-0.20 (Sc 3d +0.103) while s does not; every
gap goes positive; f_orb scores 7/13 (all d rows right, all s rows wrong) <= per-electron 9/13. THE COMPARISON DECIDES FOR PER-ELECTRON ON P^2; f_orb retired
for the walk (stated: it is the spherically-averaged fractional partition, not a one-electron self-density). PS5 HELD (Cs Ba Fr Ra: f shallowest under SR).

## Comparison (rule stated pre-run in PREDICTION-STAGE23): the field that separates the record classes on the d/s frontier with fewer failures at NO CHOSEN
## THRESHOLD is the walk's field. HF (SR, no corr) separates at zero with one 8 mHa exception (Th); SR-local separates completely but only at a threshold of
## ~0.044 that is not derived here — it is the exchange seam (uniform +0.034 +- 0.007 vs HF on n>=4 d rows, zero at 3d). So the comparison decides for HF as the
## walk's field, with the local kernel as the comparison column WHOSE DEFECT IS NOW A MEASURED, CLASS-FLAT NUMBER — and on the f frontier the two fields agree
## once the local one is SR. Ruling 2 reweighed below (bridge). Failed predictions: PH2(Th) PH4 PS1(windows) PS2(threshold) PS3 — reasons above. Timing flags: none
## (all designs pre-run; the local-minus-HF uniformity is a reading of the two tables, marked post-result). Faults: none.
Owed to T4: R 1950 nlwalk_hf built, gate held · R 1951 HF separates the d/s classes at threshold 0, 12/13, Th +0.008 · R 1952 nlwalk_sr built, c=1e6 gate exact
· R 1953 SR local separates the classes at ~0.044, not 0; local-minus-HF pair offset +0.034 +- 0.007 on n>=4, 0 at 3d · R 1954 SR removes the (n-2)f collapse:
indirect expansion 0.14-0.33 Ha, record f onset reproduced · R 1955 f_orb SIC retired by comparison (7/13 vs 9/13) · R 1956 PS3 failed: indirect SR 5-10x direct.
Files (pack37): PREDICTION-STAGE23 · nlwalk_hf.py/.jsonl · nlwalk_sr.py/.jsonl (+ nlwalk_sr_gate.jsonl) · TABLE-STAGE2-HF · TABLE-STAGE3-SR · this finding.
