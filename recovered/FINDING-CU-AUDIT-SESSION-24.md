# FINDING — bridge-23 s3(1) Cu audit, session 24. Files: t7c_cuaudit.py (t7c_corrz.py VERBATIM + env FENT), t7c_cuaudit_run.py,
t7c_cuaudit.jsonl, PREDICTION-CU-AUDIT-SESSION-24.md. No constant, no measured input; Cs/Y comparison values RECALLED-NOT-ENTERED.
## Fault F24.1 (registered before results were read): the standing Cu Z-row SCF (t7c_corrz, SIC_NOCLAMP=1, corr=Z) hits maxit=100
in a period-5 limit cycle of the potential residual d (0.00141, 0.00099, 0.00730, 0.00288, 0.00202, repeating) against tol 2e-5.
The s23 jsonl did not record `it`. Amplitude test: E(3d,ent) at maxit 96..100 = -0.37349 at every iterate (stable to 1e-5).
The cycle is in the residual metric (max |r dV|, r<60), not in the eigenvalue. EZ = -0.3735 STANDS. Every other row in this
item converged (Cs 35, Sc 37 iterations). Owed: record `it` in future rows; audit which other s23 rows hit maxit (not done here).
## A. Lande SO on the Cu row (t7c_so.zeta on the TS-SR-pol potential, exactly as the 5d rows)
zeta_3d(Cu) = 0.00420 Ha (Ni 0.00362, Cr 0.00124, Ti 0.00077 -- for the flagged consequence, not applied). Cu I 3d10 has no SO;
the hole state Cu II 3d9 4s 3D_3 (meas level) is the j=5/2-hole level, zeta*l/2 = +zeta below the term centre; the chain average
is shifted +zeta_3d to compare with it. Cu resid_Z: +0.0104 -> +0.0146. PC1 HELD (range and direction), PC2 HELD (0.0042 vs the
recalled 3D interval 0.0033, ratio 1.27). SO does not explain Cu's shortness; it enlarges it by 0.004.
CONSEQUENCE (flag, not run): the 3d rows carry no SO/Hund column while the 4f/5d rows do; both the neutral ground level (Sc 2D3/2,
Ti 3F2, Fe 5D4, Ni 3F4) and the ion hole level (Ti 2D3/2, Cr 6D1/2, Ni 4F9/2, Cu 3D3) enter meas, and Ni's hole 4F is one term of
the quartet manifold (Hund-II vs the polarised average). This is a class item for (2), not a Cu item.
## B. Entrant SIC weight (the named candidate). PS0 HELD: FENT=0.5 reproduces Cu -0.3735, Cs -0.1428, Sc -0.3211 exactly.
FENT=1.0 (occupation-independent orbital SIC potential): Cu -0.7445 (dE -0.371, resid -0.361); Cs -0.2068 (dE -0.064, resid -0.064);
Sc -0.5407 (dE -0.220, resid -0.246).
PS1: direction and overshoot HELD; the magnitude bound [-0.010,-0.045] FAILED by 8x. Reason (formed after the run, R 1449, and it is
  algebra, not a fit): the entrant SIC potential is -f v_H[n] - f^(1/3) v_x[n]; at f=1/2 this is -0.50 v_H + 0.79 |v_x|, and for a
  one-orbital LDA density |v_x| ~ 0.6 v_H, so the TS half-weight CANCELS the entrant self-term almost exactly (Cu: V_SIC(ent) at
  r_mean -0.046 vs -0.40 on the f=1 siblings, ratio 8.7). At f=1 nothing cancels. The prediction scaled the net, not the components.
PS2 HELD: Cs leaves the closed class by -0.064 (>> 0.003). PS3 HELD: Sc further over by 0.220 (>= 0.010).
RESULT: the alternative weight is REJECTED as a rule (every row collapses); Cu's shortness is not a weight artefact. The standing
PZ-81 fractional weighting stays. STRUCTURAL FINDING carried to item (2): under TS half-occupation the entrant's own SIC is ~1/9 of
a sibling's by cancellation, so the SIC that acts on the entrant is the siblings' (indirect, beta*N_sib) -- which is exactly the
own-shell-class shape (Sc Ti Cr Fe Ni Er) and the Cu-short shape (N_sib=9, indirect +0.065).
STANDING AFTER (1): Cu SHORT +0.0146 (with its derivable SO term); no candidate left in this item. Item (1) CLOSED.
Predictions failed: PS1 (magnitude). Faults: F24.1 (residual limit cycle, eigenvalue unaffected).
