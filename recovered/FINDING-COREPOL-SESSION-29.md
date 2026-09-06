# FINDING — mechanism A build (adiabatic, cutoff-free dipole core polarisation): the object is admissible on Cs and INADMISSIBLE on every d row.  s29.
# Files: PREDICTION-COREPOL-SESSION-29.md (before any code), corepol.py, corepol.jsonl. No constant; no measured input. Not a closure.
## Build: uncoupled Sternheimer on the chain's log mesh (y = r^1/2 g, banded solve), chain HFS local potential of the ion, occupied-l' projected out,
##   E2(r_e) from the l=1 multipole r_</r_>^2 of a unit charge at r_e (finite everywhere: no r_c), E_A = int P_e^2 E2. Large-r_e tail == alpha (checked, every row).
PC0 H 1s alpha 4.5001 HELD (after fixing y = r^{+1/2} g; the H gate caught it, on record).  He HFS alpha 2.50 FAILED ([1.2,1.7]; exact 1.38):
    uncoupled response in a Slater-Xalpha local potential is inflated ~1.8x (its eigenvalues are too shallow: He eps -0.57 vs HF -0.92). Every
    absolute alpha and E_A below carries roughly this factor; orderings and ratios are what the build can state.
PC1 HELD (order): alpha_closed  Sc-core 3.7 < Y-core 7.3 < Lu-core 9.2 < La-core 15.2 < Cs-core 29.2 (uncoupled-HFS scale; Cs+ exp 15.8 -> ~1.85x, as He).
    Window [12,24] on Cs FAILED by the same factor.
PC3 HELD in kind: E_A(Cs) = -0.030 on the inflated scale, i.e. ~-0.016 corrected by the He/Cs+ factor, against B's 0.013 -- on Cs, A and B are one
    object seen twice: the local form's cut region IS where the core-valence term lives. Cs is not double-counted; it is named twice. (Correction
    factor is a reading, not a term: nothing enters the object.)
PC2 FAILED, and not narrowly: E_A(closed core) Sc -0.217 · Y -0.130 · La -0.151 · Lu -0.173 · Gd -0.167 Ha against 0.001 / 0.009 needed -- 20-200x
    too large, and LARGEST on Sc where the excess is smallest. Mechanism: the adiabatic (static point-charge) form is valid only for an entrant
    OUTSIDE the responding shell; a 3d/4d/5d entrant sits inside the (n-1)s2p6 region (<r> 1.7-2.8 vs r_cut ~4), and there the correct second-order
    term carries the entrant's own excitation energies in its denominators, which the adiabatic form drops. On Cs (<r> 6.0, outside everything) the
    form is admissible and gives the right size; on the d rows it is not a test of A at all. PC4 mixed and moot (A_ns ~ E_A on Y, smaller elsewhere).
## Standing
A cannot be tested by an adiabatic build on the d rows. What survives: (i) Cs's 0.013 is one object with two names (cut region == core-valence region);
(ii) the d-row excess ~0.009 (Y La Lu), ~0.001 (Sc) remains the open object, now with the adiabatic route closed by prediction. The admissible next test
of A is non-adiabatic second order: entrant-core pair correlation with entrant excitations in the denominators (a build on the shooter's spectrum,
bound + continuum) -- or the recognition that on the d rows this IS the correlation the local form is meant to carry, and the deficit is the local
form's, i.e. an object property like the cut, to be stated in the book rather than repaired. That is a ruling.
Failed predictions s29 (this item): PC0 (He), PC1 (Cs window), PC2 (all d rows), PC4. Timing flags: none -- prediction preceded code; two build
errors (r^{-1/2} vs r^{+1/2}; outer-s2 selection took 3s not 4s on Sc) were caught by gate / by absurd alpha before any reading; both on record.
Gate for HANDOFF-29: python3 corepol.py gate -> H 4.5001, He 2.5036;  python3 corepol.py 55 -> must SKIP.