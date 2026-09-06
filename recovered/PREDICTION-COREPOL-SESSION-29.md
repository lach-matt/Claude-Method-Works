# PREDICTION — mechanism A build: adiabatic core polarisation of the entrant, cutoff-free, no constant.  s29. Written BEFORE any code.
Object: E_A = int P_e(r_e)^2 E2(r_e) dr_e, E2(r_e) = -(1/3) sum_i N_i sum_{l'} (l_>/(2l+1)) <P_i| v |y_il'>, (h_l' - eps_i) y = Q v P_i, v(r;r_e) = r_</r_>^2
(the l=1 multipole of the entrant's Coulomb field; finite everywhere, so no r_c). Large-r_e limit -> -alpha/(2 r_e^4) with alpha the uncoupled dipole
polarisability of the same orbitals. Uncoupled Sternheimer in the chain's own HFS local potential of the ion (t5_scf.scf_occ; nonrelativistic; stated);
occupied-l' components projected out (Q). Response of the CLOSED core only ((n-1)s2p6 and inward, incl. 4f14 for Lu); the ns2 pair is EXCLUDED
(adiabatic is invalid for a slow outer pair polarised by a faster inner entrant) and reported separately as A_ns for the record. Dipole only.
PC0 (gates) H 1s in V=-1/r: alpha = 4.500 +- 0.5 %.  He HFS: alpha in [1.2, 1.7] (exact 1.383).
PC1 alpha of the closed cores orders Sc-core(Ar-like) < Y-core(Kr) < Lu-core <= La-core <= Cs-core(Xe); Cs+ in [12, 24] (uncoupled overestimates the 15.8).
PC2 E_A(closed core) on Y La Lu in [0.006, 0.014] Ha and on Sc <= 0.003: the size and the 3d/4d-5d split of the s29 excess (0.009 / 0.001).
PC3 E_A(closed core) on Cs in [0.010, 0.020]: on Cs, A and B are ONE object seen twice — the local form's cut region is where the core-valence term lives.
    (If PC3 holds, Cs is not double-counted: it is the same 0.013 named twice; stated.)
PC4 A_ns (the ns2 pair, adiabatic) is larger than E_A(closed) on every d row and is NOT reported as a term (excluded by construction).
Stop rule: gates, then six rows, one pass; no scan of any parameter (there is none); failed predictions reported with mechanism.