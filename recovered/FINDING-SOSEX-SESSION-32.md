# FINDING-SOSEX (s32) — candidate S built, all gates passed, PS-1/PS-3 held, PS-2b/PS-4 FAILED; and the SIC-cancellation law behind PS-4
Object built (SPEC-SOSEX-SESSION-32, no constant beyond c): eps_c^S = eps_ring/2 + eps_2x^scr, the second-order exchange with one line screened by
Maxwell's eps of the medium (Lindhard, the ring's own, static, coupling-averaged S(Pi) = 2[Pi - ln(1+Pi)]/Pi^2 in closed form).
Reduction (PREDICTION-SOSEX design; sox_qres.py): the SOX integrand depends on k1,k2 only via P = k1+k2, so eps_2b = ∫dq g_2b(q); g_2b from the
pair density rho_q(P) = |L_q ∩ (P-L_q)| (2-D integral over the lens, azimuthal measure analytic, lens edges exact; ball autoconvolution check
3e-4). g_2b(q~) is r_s- and zeta-independent, so the whole 41x11 table (sox_table.json) costs one tabulation (100 log-spaced q~, ~10 min).
Numerical fault found and fixed BEFORE the table (not a registered fault: caught in the convergence study, no result read): a uniform P_perp^2 grid
leaves 1/|q+P|^2 unresolved near P_par -> -q; a per-column grid uniform in ln(w_q^2 + v) absorbs it exactly (was 1 % low; now 3e-4 converged).
GATES (all before any row): G-S4 f-sum, G-S5 compressibility (open, FINDING-SUMRULES) PASS. G-S1: ∫g_2b dq = 0.0241943 Ha vs E0B 0.0241792,
+1.5e-5, zeta 0 AND 1 (bookkeeping s^3/2 exact) PASS — the reduction reproduces Onsager-Mittag-Stephen 1966 to 0.06 % and fixes the prefactor
3/(16 pi^5). G-S2: screened -> E0B within 1.2e-5 at r_s 1e-3 PASS. G-S3: brute 9-D Monte Carlo (8e6, Gamma(3,1) q proposal, ball k1,k2) vs reduced:
bare z +0.98, screened (2,0) +0.81, (2,1) +0.81 PASS (sox_mc.py). H-atom chain gate under corr='S': -0.5.
g_2b peaks at q~ 1.45 (25/50/75 % mass at 0.94/1.45/1.80): the exchange momenta sit at the Fermi scale, where the medium's static Pi ~ 0.5 at r_s 2.
PREDICTIONS: PS-0a/0b HELD (open). PS-1 HELD: ratio eps_2x^scr/E0B (2,0) = 0.6747 in [0.60,0.80]. PS-2a HELD (reduction monotone in r_s, every zeta).
PS-2b FAILED at every r_s: zeta = 1 screens LESS (ratio 0.80 at (2,1)); reason (stated after the read): one sphere has N(E_F) smaller by 2^(-2/3)
(the G-S5 factor 0.63) and the same-spin exchange momenta sit at 2^(1/3) q~ — both weaken screening; s31's "a single sphere screens harder" was wrong.
PS-3 HELD: max |S - RECALLED bench| = 0.0018 Ha on r_s in [1,5] both spins (comparison only, nothing entered; sox_bench_compare.json): R's
underbinding +0.005..+0.010 collapses to -0.0001..-0.0018 (zeta 0) and +0.0006..+0.0012 (zeta 1). FAULT-F31.2's "both forms underbind" now reads:
R underbinds by exactly the screening of the exchange line; S does not.
PS-4 FAILED on its central clause (t7c_corrS.jsonl, 15 rows SUBCELL=1; COMPARE-RZS): nd>=4 rows deepen only 0.0004-0.0007 vs R (predicted
0.004-0.006); 3d |S-R| <= 0.0011 except Cr +0.0019 (shallower; the only row inside its bracket); 4f <= 0.0002; Cs +0.0003. Class ratios shift_S/shift_Z
= 3d 1.17-1.25 · 4f 1.13-1.18 · nd 1.41-1.47 · 6s 2.23 — where R/Z sat (s31: 1.18/1.16/1.41/2.32). The d-row object is NOT closed; PS-4's Sc clause moot.
THE MECHANISM (diagnostic on Y, La, run after PS-4 read — timing flag F32.2 on the diagnostic, not on PS-4): the entrant-weighted LOCAL <eps_S - eps_R>
on the total density is -0.0081 (Y) / -0.0085 (La) Ha — RZMECH's expectation; but the PZ SIC of correlation subtracts the same form on the
one-orbital, fully-polarised density: -0.0073 / -0.0077; net -0.0008 / -0.0008 at the eps level, -0.0005 / -0.0004 at the potential level = the SCF -0.0006 / -0.0007.
SIC-CANCELLATION LAW (derived, no constant): the entrant IE responds to a change of correlation form only through
   Delta_ent ≈ <Delta eps_c(n_tot, zeta_tot)>_ent - <Delta eps_c(n_ent, zeta=1)>_ent,
so any form change that is nearly the same at the entrant's r_s at zeta_tot and at zeta=1 is cancelled to ~10 % by the SIC. Screened SOX is such a
change (its zeta-dependence is weak: ratio 0.67 vs 0.80). COROLLARY: the d-row object (0.004-0.006 Ha, nd>=4) cannot be closed by ANY correlation
form whose UEG correction is spin-flat; it must be spin-DIFFERENTIAL (Delta eps_c(zeta=1) - Delta eps_c(zeta_tot) at r_s ~ 2, i.e. ~0.005 Ha of
zeta-dependence beyond the ring's) or lie outside the local-correlation trunk altogether. FINDING-RZMECH's "(at least mostly) the local form's
missing screened exchange" is WITHDRAWN; its trigger (entrant r_s window) and one-mechanism reading stand.
COMPARE-RZS DECISION (comparison decides): S is ADMISSIBLE (no constant, all gates, closes the UEG bench) and is the CORRECT local form of the
chain's electrostatic-trunk correlation; on the 15 rows it is NOT DECISIVE against R (|S-R| <= 0.001 on 14/15). Carry S as the chain form
(it is the derived object; R was S with the exchange line in vacuum), record that the rows do not distinguish, and redirect the d-row question to
the spin-differential correlation (open item for the bridge).
Files (pack32): sox_qres.py/.jsonl · sox_table.py/.json · sox_mc.py · sox_bench_compare.json · corr_sosex.py · t7c_corrz.py (corr='S' hook, this thread)
· t7c_corrRZ_run.py (FORM=S) · t7c_corrS.jsonl · PREDICTION-SOSEX · this finding · FAULT-F32.1 · FINDING-SUMRULES · sumrule_gates.py.
Timing flags: F32.2 (the SIC-cancellation diagnostic was designed after PS-4 was read; the law it states is a consequence of the chain's existing
SIC line 128, not a new choice). Failed predictions s32: PS-2b, PS-4 (both are the findings).
Prior art: Onsager-Mittag-Stephen 1966; Lindhard 1954; Gruneis-Kresse-Harl-Schimka 2009, Ren-Rinke-Scheffler 2013 (SOSEX); Perdew-Zunger 1981
(the SIC that cancels); the RECALLED bench: Ceperley-Alder/PW92, Loos-Gill 2011 Tab.II.