# PREDICTION — item (3): F^k convention (TS-orbital vs own-orbital) re-tested on the SIC-noclamp and Z-corrected 4f orbitals, s23. Before the run.
Ruled (M, s23): test both densities; if own-orbital is better it is marked NEW, BASED ON THE SLATER FORM (Slater 1960 / Condon-Shortley 1935)
until a better attribution is found; if none, PROPOSED, REQUIRING VERIFICATION BY OTHERS. Rows Dy Er Tm Yb; meas comparison only.
Object t7c_fkdens.py: orbitals from t7c_corrz.scf_sic_corr (corr=None -> SIC; corr="Z" -> Z), 4f minority channel, k = 0 (neu) / 0.5 (TS) / 1 (ion).
Hund-II shift = ci(holes_n,F_n) - ci(holes_i,F_i) with F from the named orbital(s); metric = resid_Z0 with the banked (pol, own) Hund shift replaced.
PF1 F^2(4f) on the SIC orbital differs from the pol-chain value by < 2 % on all four rows (SIC contracts 4f slightly -> F^2 larger); on Z by < 2 %.
PF2 On each density the two conventions remain TIED: |rms_TS - rms_own| < 0.001 Ha, and the ordering (own <= TS) holds on both.
PF3 Dy stays the lone exception under every combination (|resid| > 0.04); Er/Tm/Yb move together.
Pre-named alternative: a density breaks the tie by > 0.001 -- then the numbers decide, and the winner is recorded with that density named.