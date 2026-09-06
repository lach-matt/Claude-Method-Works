# PREDICTION — RUNG 3/4 SEED-INDEPENDENCE (WARM-START) AGAINST THE ORDERING
# FILED 2026-08-20T17:23:10Z, SESSION 61, BEFORE ANY CODE OF THIS TEST WAS WRITTEN OR RUN.
# R 1449. Scored only after the sha of this file is verified against the pre-run record.

## THE OBLIGATION (s53 §7, carried to s60 ladder Rung 3, item 1 of the s61 work list)
Rung 3 says exchange is exact HF on the converged answer and the Gaspar-Kohn-Sham
alpha=2/3 form is SEED-ONLY (t7c_kernel.py:105, reached via t7b_hf.py:33-34 seed ->
t5_scf.scf_occ). Rung 4 says the TFD starting potential and the Latter tail are seed-side.
**Both defences are worth nothing until a converged SCF is shown to forget its seed.**
s53: "our TFD start is a guess too, and the defence -- that it is iterated away and does
not survive convergence -- has never been demonstrated, only assumed. Starting from a
different potential and recovering the same depths IS that demonstration."

## THE CONSTRUCTION
The ruling path is untouched: NG.run_guarded -> HFC.run2 (hfc2.py:39), CORR=False,
c=137.035999, chained cfg_prev taken from the sealed nlchain.jsonl. The ONLY thing varied
is `HF.seed` (t7b_hf.py:33), which run2 calls at line 40 and which is the sole entry point
of TFD, the Latter clamp and alpha=2/3 into the walk.

    SEED-A  BASELINE, as sealed: scf_occ(Z, occ, qtail=1) -> TFD start, Latter tail -1/r.
    SEED-B  SAME FAMILY, DIFFERENT TAIL: qtail=6. A different starting potential produced
            by the same generator. Isolates the Latter clamp.
    SEED-C  DIFFERENT POTENTIAL ENTIRELY: bare Coulomb V(r) = -Z/r. No TFD, no Latter
            clamp, no exchange of any form, NO SCREENING AT ALL, and no chosen constant.
            This is s53's "different potential" in its strongest available form.

## WHAT IS PREDICTED

P1 — THE SWITCH IS LIVE (can-fail; Standing 7). At Z=19 the seed eigenvalues differ
     between A and B, and between A and C, by more than 1e-6 Ha in at least one channel;
     C differs from A in the valence channel by more than 0.05 Ha. **If any variant
     reproduces A's seed, this test is VOID and reports VOID, not PASS** — that is
     F59.3's signature and the reason this clause is written first.

P2 — THE CONVERGED ENERGY FORGETS THE SEED. For a FIXED configuration, the converged
     total energy E from run2 agrees across SEED-A / SEED-B / SEED-C to better than
     1 mHa (0.001 Ha), at both a light row (Z=19) and a mid row (Z=39).

P3 — THE ORDERING IS UNMOVED. At every row tested, under every seed that converges, the
     entrant `ent` is IDENTICAL to the sealed nlchain.jsonl entrant, and the full channel
     ORDER is identical. Rows to be tested, chosen as the tightest affordable margins in
     the sealed chain (the only rows where a seed effect could plausibly flip anything):
         Z=19  margin 0.05411 Ha  4s over 4p
         Z=20  margin 0.06058 Ha  4s over 4p
         Z=39  margin 0.04367 Ha  4d over 5p   (the n+l tie-break pair)
     Predicted margin displacement |dmargin| < 5 mHa at every row, i.e. under one tenth
     of the tightest margin in the ENTIRE sealed chain (Z=89, 0.03233 Ha).

P4 — THE LATTER CLAMP IS SEED-SIDE ONLY (Rung 4, "UNVERIFIED, do not assert either way").
     Read receipt: hfc2.py:45 and :64 build Vloc with no np.minimum(...,-qtail/r); the
     clamp appears at t7b_hf.py:119 inside run(mode='hfs') and inside the seed's own SCF,
     never in run2. **Prediction, which is what makes it more than a reading:** because
     run2 takes qtail ONLY as the seed argument, SEED-B's converged energy must agree with
     SEED-A's to the same 1 mHa as P2. If the clamp were live inside run2's iteration, a
     tail of -6/r rather than -1/r would move the converged energy by far more than that.
     A large SEED-B shift therefore FALSIFIES this reading and Rung 4 stays open.

P5 — CONVERGENCE-FLOOR SPILLOVER, DECLARED IN ADVANCE, NOT CLAIMED AS THE MEASUREMENT.
     The A/B/C spread at a fixed configuration is a LOWER bound on the walk's numerical
     floor: it is the size of the answer's memory of where it started. It is NOT the
     Rung 7 floor (item 2 of the work list), which is a different measurement over grid
     and tolerance, and this file does not offer it as one. Whatever spread is found is
     recorded so that item 2 may not later contradict it.

## WHAT WOULD FALSIFY, ROW BY ROW
  * Any entrant change under any converging seed  -> Rung 3 FAILS. The KS form is NOT
    seed-only in effect, the walk remembers its guess, and the ordering result is
    contaminated by an unbounded approximation. This would be the largest single fault
    in the chain and must be reported as such, immediately, before anything else.
  * dE > 1 mHa but entrant unchanged -> Rung 3 PARTIAL: bounded but not negligible; the
    bound must then be carried explicitly into every margin statement in Deliverable 1.
  * SEED-C fails to converge at a row -> that row is NOT evidence either way. It is
    reported as NO-DATA. A non-converging seed is not a passing seed (F59.3 discipline).
  * P1 fails -> VOID, as above.

## SCOPE, STATED SO IT CANNOT BE OVERCLAIMED LATER
Three rows are not 107. This tests the tightest-margin rows available at affordable cost,
which is where a seed effect would show FIRST if it existed anywhere. A PASS bounds the
seed effect at those rows and nowhere else; the wording of any resulting claim must say
so. The rows are CHAINED-mode references (Rung 8 DERIVED), not restart rows, so nothing
empirical enters the comparison on either side.
