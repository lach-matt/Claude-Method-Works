# PREDICTION — second-order chain correlation on Cs/Gd in (a'). s27, bridge-26 §3(4). Written BEFORE any run.
Object (hfc2.py): HFSR 'hf' (c=C0, integer occ, avg-of-config) with the chain-Z correlation potential added self-consistently per shell,
v_a = v_c[n_up,n_dn](sigma_a) - v_c[n_a,0] (PZ orbital SIC, chain mode "all"; spin assignment as hfdscf: shells filled up first), total energy
E = E_HF[P] (kinetic from eps minus the FULL local potential incl. v_a) + E_c^SIC[P] = E_c[n_up,n_dn] - sum_a q_a E_c[P_a^2/4pi r^2, 0], eps_c as
v_gbz (GB high-density form, zero where eps_c>=0). D_2 = E_ion - E_neu; obj_2 = -D_2. Second-order piece := obj_2 - obj_s26 (obj_s26 = -D_HF + Delta_c).
No constant beyond c. meas RECALLED-NOT-ENTERED. Rows: Cs (s26 resid +0.012), Gd (+0.018), Y as like-for-like control (s26 +0.005).
PC1  Consistency gate: with the correlation potential and E_c switched OFF the code reproduces s26 D_HF for Cs (0.14... as hfdscf.jsonl) to 1e-5.
PC2  The second-order piece is NEGATIVE (deepens the removal energy) on Cs and Gd: relaxation under v_c lowers the N-electron state more.
PC3  Cs: |resid_2| < |resid_s26| = 0.012, sign unchanged; second-order magnitude in [0.001, 0.010] Ha.
PC4  Gd: |resid_2| < 0.018.
PC5  Y control: |obj_2 - obj_s26| < 0.005 (the like-for-like class result of s26 is not spoiled).
Failure of PC1 -> stop. Failure of PC2/PC3 -> the Cs/Gd shortfall is not second-order local correlation; report and stop, no scan.
