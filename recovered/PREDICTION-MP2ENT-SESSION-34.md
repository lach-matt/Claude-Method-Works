# PREDICTION-MP2ENT (s34) — ruling (M): "(i)": build the second-order (pair) correlation of the entrant with the core ONCE, run the six class rows and Yb.
Written BEFORE any code. Object: E2_ent(Z) = sum_b E2closed(a,b)/(2(2l_a+1)) [+ (2/N_a) E2closed(a,a) for Yb 4f14, N_a=14], a = entrant shell, b = every closed
core shell, second order in 1/r12 on the chain's own spin-averaged HFS neutral orbitals (t5_scf.scf_occ potential, qtail=1), virtuals = the discretised
spectrum of the SAME local potential in a box (radial eigenproblem on the log mesh, generalized symmetric form), all l_r,l_s <= LMAX, all box states.
Pair energies in LS-coupled pair states: M = D + (-1)^(l_r+l_s+L+S) E', D = sum_k (-1)^(l_a+l_s+L) {l_a l_b L; l_s l_r k} <l_a||C^k||l_r><l_b||C^k||l_s> R^k(ab,rs),
E' the same with r<->s; E2closed(a,b) = -(1/2)(1/(1+delta_ab)) sum_LS (2L+1)(2S+1) sum_{rs} M^2/(eps_r+eps_s-eps_a-eps_b), a=b restricted to L+S even.
Derived, no constant, no measured input. Gates (comparison only, RECALLED): He 1s^2 total second-order on HF orbitals is -0.0374 Ha; on the local HFS
orbitals of the same box the number is expected within [-0.045,-0.028] and its k-partial-wave series 1/(2k+1) R_k^2 form is exact by construction (checked
against the closed formula for a=b=1s). H: no correlation (single electron) — trivially zero. Any factor discrepancy is REPORTED, not tuned.
Bounds stated in advance: LMAX truncation (l^-4 tail) and the box (r_max) make every absolute E2 a LOWER bound in magnitude by ~10-20 %; orderings and
row-to-row differences at fixed LMAX are what the build states. Timing: nothing of this object is on record; the residual pattern (TABLE-A) IS in context.
PN-1: |E2_ent| ordering follows the entrant's compactness, opposite to the O-path residual: 3d Sc > 4d Y > 5d (Gd, La, Lu) > 6s Cs; 4f Yb (with 13 siblings)
      largest of all. Sizes: Sc 0.04-0.08, Y 0.03-0.05, 5d 0.02-0.04, Cs 0.008-0.015, Yb 0.10-0.20 Ha (LMAX 4).
PN-2 (the test): the EXCESS of second-order over the local chain correlation, X = |E2_ent| - |DEc_S| (frachf_S / t7c_corrS record for DEc), is NOT the residual
      in absolute size (both terms are bulk); but its class shape ranks with the residual: X/|E2_ent| (the fraction of the entrant's pair correlation the local
      form does not deliver) grows with rs_w: Sc smallest, 5d/4d middle, Cs largest. Failure: Cs fraction not the largest, or Sc not the smallest.
PN-3: the radial location of the pair correlation density (E2 partitioned by the entrant's r) puts, on Cs, >= 30 % of E2_ent beyond r_s = 10 (frac_tail 0.37 of
      density) — the local form's tail region — and < 5 % on Sc. Failure: Cs share < 20 %.
PN-4 (Yb, horizon (3)): the sibling term (2/14) E2closed(4f,4f) is >= 0.5 of E2_ent(Yb): the 4f +0.09 shortfall's candidate lives in the same-shell pair
      correlation that the local SIC-corrected form removes with the SIC (E_c[n_ent] self-correlation subtracted while the sibling correlation is real).
      Size stated as a bound only; no closure claimed at second order on local orbitals.
Files: this file · mp2_ent.py · mp2_ent.jsonl · TABLE-MP2ENT-SESSION-34.txt · FINDING-MP2ENT.