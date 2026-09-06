# PREDICTION-A (s34) — bridge-33 §3(1)(A): the observable-path class spread. Written BEFORE any run. Ruling (M, s34): "B first, then A".
Object: resid_O(S, Gd seam applied) = IE_O - T: Sc -0.0040 · Gd -0.0004 · La +0.0016 · Lu +0.0040 · Y +0.0051 · Cs +0.0084 (FINDING-GDS s33).
Lead (bridge-33): a sign change INSIDE the class. Record consulted before predicting (timing flag F34.2, stated): rz_mech.jsonl entrant-weighted
r_s (rs_w) Sc 1.68 · Y 2.64 · Gd 2.67 · La 2.83 · Lu 3.11 · Cs 10.2; the s31 RZMECH reading that Sc is over "under any local form" and that the exact-UEG
local eps_c would move nd rows toward closure but Sc further over; bridge-33's three A-candidates: (a1) Sc term-resolved D_HF — VOID from record (3d1 4s2 2D ->
4s2 1S has no d-term, no run needed); (a2) 5s/6s-d exchange in the average of configuration — VOID (closed s2); (a3) Cs large-r_s tail.
Hypothesis to test (decomposition, no constant): the class spread is TWO derived pieces on one mechanism, the local UEG correlation form: (I) the S form's
shortfall against the exact UEG eps_c(r_s,zeta) inside 1<=r_s<=10 (RECALLED bench, comparison only, as rz_mech), entrant-weighted, which is short (bench
deeper) on every row; (II) what remains after (I) is the LOCALITY error, non-zero on the compact 3d only.
Run: rz_mech_S.py = rz_mech.py verbatim with corr="S" and eS = corr_sosex.eps_S (nothing else); rows Sc Y La Gd Lu Cs; write dS_loc, and also the
tail weight frac_tail = sum W[r_s>10]/sum W. Then TABLE-A: resid_O, dS_loc, resid_O - dS_loc (sign convention: dS_loc<0 means bench deeper = the O
path would go DEEPER by |dS_loc| if S were exact-UEG, i.e. resid_O_corrected = resid_O + dS_loc).
PA-1: dS_loc is NEGATIVE on all six rows, |dS_loc| smaller than |dR_loc| of record (S is between R and bench): nd rows -0.002..-0.004, Cs -0.002..-0.004,
      Sc -0.001..-0.003.
PA-2: resid_O + dS_loc (the O path under an exact-UEG local eps_c, window-limited) on the nd/6s rows moves TOWARD zero and lands within +/-0.003 of it
      on La/Gd/Lu (Y/Cs within +/-0.005; both RECALLED); Sc moves AWAY, to -0.005..-0.007.
PA-3: ordering. resid_O is monotone in rs_w on Sc<Gd<La<Lu<Cs (Y the exception, and Y sits at rs_w 2.64 between Sc and Gd yet reads +0.005): the ONE row out
      of order is a recalled-value row. After PA-2 the residual is NOT monotone in rs_w: it is ~flat on nd/6s and negative on Sc alone.
PA-4 (reading if PA-1..3 hold): the class spread is (I) the S form's own UEG shortfall (derivable form incomplete: beyond SOSEX; bounded by the bench, not
      corrected by it — bench is not derivable) plus (II) a locality object on Sc alone of ~-0.006: LDA-type correlation of a compact 3d over-delivers its
      removal. (II) is the object to close next, and its home is not the UEG (any UEG form makes it worse).
Failure: PA-1 fails on any positive row; PA-2 fails if any 5d row lands outside +/-0.003 or Sc moves toward zero; PA-3 fails if the post-(I) residual is
still monotone in rs_w with spread > 0.004 across the 5d rows.
Nothing entered; bench PW92/Loos-Gill RECALLED comparison only; Cs/Y RECALLED-NOT-ENTERED. Files: this file · rz_mech_S.py · rz_mech_S.jsonl · TABLE-A.