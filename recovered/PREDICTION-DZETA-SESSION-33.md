# PREDICTION-DZETA (s33) — the spin-differential correlation table (bridge-32 §3(2)); written BEFORE any run
Ruling carried (M, s33, "Carry S"): S is the chain correlation form (bridge-32 §3(1)); R held only as comparison. Nothing entered; bench RECALLED (rz_mech.py B0/B1, s31), comparison only.
Object: per row, on the corr='S' SCF densities of the hole state (same call as rz_mech, FORM=S), entrant-weighted (W = n_ent(r) dr, radial density, ∫W = 1):
  A = ∫ W [eps_B(n_ent, zeta=1) - eps_S(n_ent, zeta=1)]        (the PZ-SIC one-orbital line, fully polarised)
  B = ∫ W [eps_B(n_tot, zeta_tot) - eps_S(n_tot, zeta_tot)]     (the total-density line)
  D = A - B   [Ha].  By the SIC-cancellation law (FINDING-SOSEX), a bench-ward change of form moves the entrant eigenvalue by ~ B - A = -D at the eps level;
  D > 0 deepens the entrant (larger IE).  Window: 1 <= r_s <= 10 on each line separately (below r_s 1 the recalled table has no anchor); frac_win reported per line;
  a second column D2 uses the stricter 2 <= r_s <= 10 window on the zeta=1 line (its anchors are r_s 2,5,10 only).
Predictions (numbers chosen before the run):
  PD-1: nd>=4 rows Y, La, Gd, Lu: D in [+0.003, +0.007] Ha (the d-row object 0.004-0.006, sign = deepening).
  PD-2: 3d rows (Sc,Ti,Cr,Fe,Ni,Cu) and 4f rows (Dy,Er,Tm,Yb): |D| <= 0.002 Ha; Cs |D| <= 0.002.
  PD-3: the ORDER of D across the four nd>=4 rows tracks the s31/s32 shortfall order (La >= Gd ~ Lu > Y within 0.001).
  PD-4: D and D2 agree to within 0.001 on nd rows (the zeta=1 line's held-end error is not what carries the effect).
Failure meaning: PD-1 failing with |D| <= 0.002 on nd rows => the d-row object lies OUTSIDE local correlation (bridge-32 corollary, second horn); PD-2 failing => the
zeta-dependence is class-uniform, not the d-row object. Timing flag: none (design precedes run). Tool: pack33/dzeta.py -> dzeta.jsonl (append, done-set, <=3 rows/call).