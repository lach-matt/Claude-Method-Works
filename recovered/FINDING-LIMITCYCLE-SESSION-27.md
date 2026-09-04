# FINDING — F25.1 (Ti) / F24.1 (Cu) are ONE fault: the hard eps_c >= 0 cutoff in v_gbz stepping across a grid point.  s27, bridge-26 §3(1)+(2)
Files: limitcycle.py limitcycle.jsonl (Ti beta 0.3 / 0.15), lc_diag.py (t7c_cuaudit.py + per-channel residual location; diagnostic only, not a solver
change), PREDICTION-LIMITCYCLE-SESSION-27.md (written before any run). No constant, no measured input. Convergence audit, not physics.

## Result 1 (Ti, standing beta=0.3, maxit=100): E_ent -0.38063 == frozen_scan E_ref_half exactly. Residual tail is an EXACT cycle of period 7
   (0.005331 0.015057 0.008253 0.005774 0.004039 0.015961 0.007621 repeating), amplitude 0.004-0.016 (r*dV). Autocorrelation peak lag 7 (0.83).
   PL1 FAILED as written (period 7 not 5; amplitude above the predicted ceiling 1e-2) -- the cycle itself is confirmed.
## Result 2 (Ti, beta=0.15): still cycling, now period 4, SAME amplitude 0.004-0.015; E -0.38063 unchanged. PL2 FAILED, PL3 HELD.
   Amplitude independent of beta => not a linear-mixing instability. Stop rule fired: no beta scan; PL4/PL5 not run as designed.
## Result 3 (diagnosis, lc_diag): the whole residual sits in ONE channel at ONE radius. Ti: SIC potential of 4s-up (integer channel) at r=3.63;
   V_up/V_dn total potentials converged (residual ~0). 4s-up eigenvalue jitters +-4e-6 only. Not a node (u^2 = 0.28 there; 4s nodes at 0.091,
   0.391, 1.231). At r=3.63 the one-orbital r_s of 4s-up = 5.23 and v_gbz's polarised correlation potential steps -0.00531 -> 0.0 exactly:
   `return np.where(eps<0, v, 0.0)` -- the GB high-density form eps_c = lam0 ln r_s + e0a + e0b (+lam1 r_s ln r_s) crosses zero near r_s ~ 5.2
   and the potential is hard-cut there. Step * r = 0.019 == cycle amplitude. As the density moves by ~1e-6 the crossing hops one log-mesh point,
   so d = |step| at fixed size, forever: the "limit cycle" is the crossing point walking back and forth, its period set by how many iterations the
   hop takes at a given beta (7 at 0.3, 4 at 0.15).
   Cu (F24.1): identical anatomy in the 3s-up SIC channel at r=1.54 (r_s 5.03->5.43 across 1.524-1.559, v_c -0.00518 -> 0.0), tail 0.001-0.007,
   E_ent -0.37349 (standing EZ -0.3735). Period-5 there.
   Why E is untouched: the step lives in the SIC potential of a CORE/valence-s integer channel, ~5 mHa over one mesh cell; the entrant 3d
   eigenvalue does not resolve it at 1e-4. This is why every s23-s26 gate reproduced despite it=100.

## What this is and is not. It is a numerical-analysis fault in the CONVERGENCE MEASURE meeting a non-smooth point of the derived correlation
   object; the derived object itself (GB high-density eps_c, parameter-free) is being used at r_s ~ 5 where its expansion is not valid and turns
   positive -- the cutoff is the honest sign of that. It is NOT a mixing/damping problem (beta-independent) and NOT a physics residual on any row.
   F24.1/F25.1 keep their names; the fault is now located and mechanised. Every affected row so far is a diffuse s-orbital's SIC (4s in Ti, 3s in
   Cu); rows without such a crossing inside r<60 converge (Sc it 37).

## Repair candidates -- each is a RULING, not taken here (bridge-25 s3(4) allowed only "convergence, not physics"; two of three touch the object):
   (A) Report `it` and E-stability as the convergence certificate for rows whose residual is a located v_c step (measure the residual on the total
       potentials V_up/V_dn only, or exclude the one-cell step): no change to any number; makes F24.1/F25.1 a documented property, not a fault.
   (B) Smooth the cutoff (e.g. C1 taper of v_c to zero over the crossing): CHANGES the correlation-SIC object at ~5 mHa over ~1 cell in core-s SIC
       channels. Prediction if ruled: entrant E unchanged to 1e-4 on Ti/Cu; must be gated on all 15 rows before it stands. Needs a stated form.
   (C) Leave both open as faults with the mechanism on record. Zero risk; `it=100` remains in every table.
   Recommendation stated, not decided: (A). It is the only option that is convergence-only.
## Predictions: PL1 FAILED (period/amplitude), PL2 FAILED, PL3 HELD, PL4 PL5 NOT RUN (stop rule). Timing flag (R 1449): the v_gbz cutoff mechanism
   was found by diagnosis AFTER PL2 failed, not predicted.
