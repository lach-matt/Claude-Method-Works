# FINDING — item (1) regeneration of the 15-row chain under F22.1 repair (SIC_NOCLAMP=1), s23
Object t7c_corr2 (SIC_NOCLAMP=1, GB_EXACT=0). Driver t7c_regen.py; rows t7c_regen.jsonl (15); table TABLE-CHAIN-15-REGEN-SESSION-23.txt.
La reproduces s22 noclamp:None -0.2161 exactly. No constant, no measured input entered; meas column recalled for comparison only.
RESULT: every SIC base moves shallower by +0.0034 (Cr) .. +0.0070 (Cu), median +0.0056. GB increments unchanged (|d| <= 2e-4 on 14 rows; Cu dU -0.0007).
Containment re-scored (SO/Hund and U/P carried from s22): CONTAINED 9 / OVER 4 / SHORT 2  (s22: 9/5/1).
  Cs 6s  OVER -> CONTAINED  (resid -0.0023 -> +0.0034, inside [|P| 0.0022, |U| 0.0038])
  Yb 4f  CONTAINED -> SHORT (resid +0.0371 -> +0.0429 > |U| 0.0378)
  Tm 4f  resid +0.0374 == |U| 0.0374 to 4 dp: ON THE BOUNDARY, scored CONTAINED by the rule's strict >; flagged.
  Cu 3d  SHORT and worse (+0.0381 -> +0.0451); the largest F22.1 shift is on Cu.
PREDICTIONS: PR1 HELD (all 15 positive). PR2 HELD (Gd +0.0046, Lu +0.0052, La +0.0041 reproduced).
  PR3 FAILED: no channel ordering. 3d 0.0034-0.0070, 4d 0.0048, 5d 0.0041-0.0052, 4f 0.0056-0.0058, 6s 0.0057. The F22.1 shift is a near-uniform
      offset ~+0.005-0.006 across all channels, not a diffuseness-ordered tail effect. Entered per R 1449 (interpretation formed after the run).
  PR4 FAILED on 1 of 15 (Cu dshiftU -0.0007 vs threshold 5e-4); held on 14.
  PR5 FAILED: score moved by TWO rows. "A 4f row crossing to SHORT" (Yb) was pre-named; Cs crossing to CONTAINED was NOT.
STANDING: the F22.1-repaired chain brackets 9 of 15, over-shoots 4 (Sc Ti Cr Dy), falls short on 2 (Cu Yb), Tm on the edge. Not a closure;
the repair moved the whole chain shallower by one nearly constant amount and the score is a re-partition of the same failure, not a change in its shape.
Owed cleared: bridge-22 s6 "regeneration under F22.1" DONE. Not run: GB_EXACT=1 variants (s22 (iii): immaterial at 3e-4).
Note s23-1: my first scorer inverted the resid sign (meas-chain); caught before any reading was stated, corrected to s22's chain-meas; no result depended on the faulty pass.