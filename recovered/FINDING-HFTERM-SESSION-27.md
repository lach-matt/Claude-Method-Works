# FINDING — term-resolved exact-exchange DSCF on 3d/4f: the term-average error was PART of the 3d residual and NONE of the 4f one.  s27, bridge-26 §3(3)
Files: hfterm.py hfterm.jsonl hfterm_table.py TABLE-HFTERM-SESSION-27.txt PREDICTION-HFTERM-SESSION-27.md (written before any run).
No constant beyond c; meas RECALLED-NOT-ENTERED (TABLE-JANAK-24), comparison only. Not a closure.
## Gate: PT0 HELD to 1e-16 (d2, f2, d3, d1s1): the highest-weight-determinant machinery reproduces Slater's average of configuration exactly.
   Sc control (PT4 HELD): D_term == D_avg == s26 gate-26 value 0.26664. Δ_c identical to s26 on all rows.
## Result 1 (3d, first order in relaxation, HF F^k): resid_HFterm  Sc -0.009 · Ti -0.014 · Cr +0.021 · Fe +0.048 · Ni +0.044 · Cu +0.065
   against s26 avg-of-config  -0.008 · +0.022 · +0.078 · -0.077 · -0.023 · +0.061  and the chain resid_J  -0.044 · -0.036 · -0.039 · -0.043 · -0.044 · -0.019.
   Ti and Cr are REPAIRED by the term (Cr +0.078 -> +0.021, PT3 HELD 0.059 in [0.05,0.12]); Fe's magnitude falls (0.077 -> 0.048) but crosses zero;
   Ni is made worse (the ion 3d7 4F is stabilised 0.066 more than the neutral 3d8 3F); Cu is not a term row (3d10 -> 3d9 4s1 3D, 0.004).
## Result 2 (4f): resid_HFterm  Dy +0.076 · Er +0.103 · Tm +0.099 · Yb +0.093 (s26: -0.032 · +0.044 · +0.070 · +0.093). WORSE on every term row.
   Yb 4f14 -> 4f13 (2F) HAS NO TERM CORRECTION and shows the same +0.093: the 4f residual is not term-average error at all. With the term resolved,
   the four 4f rows collapse to ONE number, +0.09..+0.10 Ha too shallow -- a systematic 4f under-binding of exact exchange + first-order local
   correlation, term-independent, that the term correction merely uncovers (Dy/Er/Tm were being partly cancelled by term over-stabilisation of the ion).
## Result 3 (predictions): PT0 HELD · PT1 FAILED (5/10, not 7) · PT2 FAILED (Cr yes, Yb no -- Yb has no term) · PT3 HELD · PT4 HELD ·
   PT5 partly FAILED: Fe- Ni- Cr+ as predicted; Cu- and Tm- against prediction (my sign argument ignored that the NEUTRAL of Cu/Tm has a single
   term, so only the ion is stabilised); Ti+ Dy- Er- not predicted, stated. Timing flag (R 1449): the "collapse to one number" reading of the 4f rows
   was made after seeing the table, not predicted.
## What stands. On single-entrant s/d rows (s26): exact exchange + first-order chain correlation closes to <= 0.009. On compact multi-electron shells,
   term-resolved exact exchange + the SAME correlation leaves +0.02..+0.07 (3d) and +0.09..+0.10 (4f), all POSITIVE (removal energy too shallow),
   while the chain (SIC-LSD) leaves -0.02..-0.09, all NEGATIVE. The two derived objects bracket the measurement from opposite sides on every
   compact row; the bracket is a two-sided corridor and per M's ruling does not close -- no constant is chosen here and none is proposed.
   The remaining pieces, in order of size, are the FIRST-ORDER-ONLY treatment of correlation on compact shells (Δ_c -0.03..-0.065 is the local
   potential's expectation on HF orbitals; the differential correlation between an N- and an (N-1)-electron compact shell is second order and is
   what HF is known to lack) and the UNSCREENED HF F^k in the term energies (Fe overshoot). Orbital relaxation of the term (second order) is not
   computed. Which of these is opened is a ruling; the smallest test is the one bridge-26 §3(4) already names for Cs, applied to Yb (no term
   ambiguity, largest residual): the entrant's SECOND-ORDER correlation, computed WITHOUT a scan as in s26's M_resp derivation.
## Open, stated: relaxation of the Hund term (needs a term-resolved SCF, a build); F^k screening; the 4f +0.09 as a single object.
