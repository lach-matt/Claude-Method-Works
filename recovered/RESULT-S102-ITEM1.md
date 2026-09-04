# RESULT S102 ITEM 1 -- du/dx ISOLATION + ONE-SHELL ROT/PERP SPLIT (row 58). Predictions b1835f91 (1),
# a82e88d0 (1B), both hash-gated before arithmetic. Receipts w102-58.json, w102b-58.json.
## SEVERITY LINE: two prediction faults (F102.1 P3-as-written, F102.4 P6-as-written), two instrument
##   faults (F102.2 incommensurate gap columns; F102.3 T-table core non-hermiticity, caught by own
##   diagnostic). VERIFIED beneath them: two exact split identities and the rotation-dominance finding.
##   No sealed number touched.
## VERIFIED (w102.py, P1 HIT 26/26 at 0.0 residual): symmetrized exact split of every full-relaxation
##   endpoint difference du = du_wf + du_pot, dx = dx_wf + dx_pot, per shell, algebraic telescoping.
##   Bookkeeping: sum q(deps - du + dx) = +7.243947 = N1 exactly (i101 cross-check).
## F102.1 SEVERITY prediction: P3 falsified as written -- q(deps - du + dx) is the N1 partition, not dE;
##   N2 is not contained in the per-shell columns. Wrong-object species (recurring).
## F102.2 SEVERITY instrument: w102 gap columns compared a101's net slot terms to gross du_pot/dx_pot;
##   populations incommensurate; P2 rescored MISS (vacuous HIT retracted in-run).
## FRAME FINDING (from receipts, Standing-6): a101's law is a DIFFERENT GAUGE -- per-shell parts O(1) vs
##   R2_parts O(1e-5); its -1.6119e-3 total gap rides on O(1) inter-shell cancellations. d101's R2_parts
##   (one-shell-frozen E_one chords) is the commensurate gauge: additive to 1% (sum +1.0699e-4 vs R2
##   +1.0588e-4), every shell individually at defect scale. R3 (sqrt(M)-1)X projection fails per shell
##   (ratios -5.25..+0.02), worst at same-l valence pairs {5s -5.25, 5p -3.43, 6s -2.90, 5d -2.41};
##   path overlap <dP_5s', P_6s> = -1.2e-2.
## VERIFIED (w102b.py, P5 HIT 13/13 exact): chord split rot_k + perp_k == chord_k, symmetrized exact;
##   F reproduces d101 R2_parts at <= 1e-10 on {4s, 5s, 5p, 5d, 6s} (and 1e-8-1e-6 at core, see F102.3).
##   CAN-FAIL non-vacuous both instruments (levers break at the perturbed cell only).
## F102.3 SEVERITY instrument (caught by own asymmetry diagnostic): eigen-relation T-table inherits SCF
##   convergence residuals at core-orbital scale (asym up to 23 Ha); P4 (1e-8, 13/13) MISS 5/13 -- the
##   route is exact at valence, noise-limited at core. Repair route named: tighter SCF rung or
##   residual-corrected T-action; NOT run (context budget).
## F102.4 SEVERITY prediction: P6 falsified as written -- at the clean shells rotation OVERSHOOTS:
##   rot/R2p = +7.09 (5s), +4.14 (6s), +1.51 (4s), +0.56 (5p), +0.43 (5d); perp cancels the excess.
##   Core clause untestable at current instrument precision (F102.3 contamination ~10%).
## STATE OF G5b AFTER ITEM 1: the per-shell law target is now sharply named in the commensurate gauge:
##   R2p[k] = rot_k + perp_k with both measured; the s-channel valence defect is occupied-rotation
##   (overlap-Pulay) dominated. OPEN: analytic values of rot_k (overlap x Fock off-diagonal content) and
##   perp_k (operator-difference content restricted to the orthogonal complement). This is the residue
##   carried forward; zero-residue standard unchanged.
