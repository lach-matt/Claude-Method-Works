# PREDICTION — F25.1 (Ti) / F24.1 (Cu) period-5 limit-cycle audit, s27 (bridge-26 §3(1),(2)). Written BEFORE any run.
Object: t7c_cuaudit.scf_sic_corr(Z,1,occ=minus(ground_occ,3,2,1),entrant=(3,2),corr="Z",mode="all"), SIC_NOCLAMP=1, FENT=FOCC=0.5 (standing),
beta=0.3, tol=2e-5, maxit=100. Standing: Ti E_ref_half -0.38063 it 100 (frozen_scan.jsonl); Cu EZ -0.3735 it 100 (bridge-24 §2(1)).
Convergence, not physics: the ONLY admissible outcome that changes anything is a repaired `it`; E is not allowed to move.
PL1  The residual history hist[] on Ti at beta=0.3 shows a non-decaying tail with period 5 (autocorrelation peak at lag 5 over the last 40 iterations)
     and terminal amplitude in [1e-4, 1e-2] (i.e. above tol=2e-5, below anything that moves E at 1e-4).   [audit]
PL2  Reducing beta to 0.15 (no other change) converges Ti below tol in <= 100 iterations.   [repair candidate: linear mixing only]
PL3  Ti E from the converged run equals -0.38063 to 1e-4 (|dE| < 1e-4).   [bridge-25 s3(4) prediction, carried]
PL4  The same repair (beta=0.15) converges Cu below tol in <= 100 iterations, and Cu E equals the standing value to 1e-4.
PL5  On a converged control row (Sc, Z=21, standing it 37) beta=0.15 changes E by < 1e-4 — the repair is inert where nothing was wrong.
Failure of PL2/PL4 (still cycling at beta=0.15) -> the cycle is not a mixing-damping artefact; report and STOP on this item (no scan over beta).
