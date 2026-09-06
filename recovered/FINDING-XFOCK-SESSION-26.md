# FINDING — item (2), s26: is the DE_J residual the functional's over-binding of the compact entrant? Ruling: (a) and (b) both run; comparison decides.
Files: xfock.py, xfock.jsonl (15), xfock_table.py, TABLE-XFOCK-SESSION-26.txt, PREDICTION-XFOCK-SESSION-26.md (GA0, PA1–PA4 + comparison rule, written before the run).
No constant, no measured input; resid columns from TABLE-JANAK-24 (Cs, Y RECALLED-NOT-ENTERED).
## (a) as built: first-order replacement, at the standing f=1/2 chain-Z orbitals, of the entrant's LSD exchange <n_ent|v_x[n_s]−v_x[f n_ent]> by exact
Fock exchange with the other same-spin occupied electrons (spherical average, coefficient 1). GA0 HELD (G^0 self == <n|v_H[n]> to 1e-6: pipeline sound).
## Result: PA1–PA4 ALL FAILED. Delta_x is small and positive only where the entrant has NO same-spin siblings (Sc +0.032, Fe +0.044); wherever
same-spin siblings exist it is large and NEGATIVE (Cr −0.48, Ni −0.31, Cu −0.68, Er −0.58, Tm −0.78, Yb −0.98, Dy −0.22, Ti −0.09), and it is
negative even for the diffuse rows (Cs −0.069, Y −0.041, La −0.076, Gd −0.105, Lu −0.071). Spread of resid_J goes 0.081 -> 1.02. Comparison rule -> (b).
## Why — registered as a fault of the test's DESIGN, F26.1: <psi|K_others|psi> at frozen orbitals is a KOOPMANS quantity (unrelaxed), while the chain's
TS/Janak eigenvalue is a RELAXED, DSCF-type quantity (Slater 1972, Janak 1978). The difference between them is the orbital relaxation that exact
exchange lacks, and for localised d/f shells that is tenths of a Hartree, carried by the same-shell G^k(3d,3d), G^k(4f,4f) sibling terms
(HF 3d eigenvalues of Cu are ~0.3 Ha deeper than the 3d removal energy for exactly this reason). So Delta_x does not measure exchange over-binding;
it measures relaxation. The candidate was not like-for-like. (b) therefore stands BY DEFAULT, not by defeat: the residual remains the object's bound.
## Standing after item (2): the residual under DE_J (−0.002 s .. −0.05 3d/4f, Dy −0.09) is NOT reduced by any first-order in-chain exchange term;
it is not touched by this test. Item (2) closes as (b) with the caveat above.
## Candidate carried forward, NOT opened (needs a ruling and a build): (a') the like-for-like object exists in the bank — the scalar-relativistic HF
entrant at f=1/2 (t7c_hfsr, gate 13: Sc −0.2686, La −0.2017 vs chain-Z TS −0.3211/−0.2330). From banked numbers HF-TS UNDER-binds Sc by
+0.026 (meas RECALLED via resid_TS) where chain-Z-J over-binds by −0.0435; the chain's own derived correlation on the HF-TS entrant would be a
comparison with no constant. Prediction if opened: HF-TS + chain-Z correlation lands within ±0.015 of meas on Sc and La. Size: a build (HF+corr Janak), not a check.
Failed: PA1 PA2 PA3 PA4. Held: GA0. Fault: F26.1 (design). Not a closure.
