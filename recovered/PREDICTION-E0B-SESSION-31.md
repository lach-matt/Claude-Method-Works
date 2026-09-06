# PREDICTION — E0B(zeta): the spin dependence of the second-order exchange constant (bridge s30 §3 (1)(i)).  s31, before any run.
Object: the chain carries E0B = ln2/6 - 3 zeta(3)/(4 pi^2) Ha (OMS 1966) as zeta-INDEPENDENT in both form Z (t7c_cuaudit/t7c_corrz v_gbz) and form R (corr_ring E).
FINDING-RING owed its zeta-dependence as a derivable refinement (Cs cut 31 % at zeta~1 was attributed to E0B being zeta-independent).
PE1 (derivation, no numerics): E0B(zeta) = E0B(0) for all zeta. Argument: the bare second-order exchange diagram couples SAME-SPIN pairs only; for one
    spin species of Fermi wavevector k_F it is a 9-dimensional Fermi-sea integral whose scaling is Omega^3 k_F^9 x (e^4/Omega^2) k_F^-4 x (m/hbar^2) k_F^-2
    = (Omega k_F^3) e^4 m/hbar^2 ~ N_species x const: a density-INDEPENDENT constant per particle OF THAT SPECIES. Summing species: (N_up + N_dn) x const / N = const.
    Hence Upsilon_0^b(zeta) = 1, and the chain's constant is already exact in zeta. Prediction: no code change; the owed refinement resolves to zero.
PE2: the chain's eps0a_table.json agrees with the literature RPA constants eps_0^a(0), eps_0^a(1) to < 2e-4 Ha (in-project ring table vs Hoffman 1992).
PE3 (consequence): the Cs 31 % cut under form R is a property of form R itself (bare second-order exchange added to a resummed ring at large r_s), NOT a missing
    zeta-dependence; the R/Z comparison on Cs is fair as the forms stand. A screened second-order exchange would be a DIFFERENT candidate (not opened; M's).
Timing flag F31.1 (R 1449): PE1's scaling argument was reasoned before, but this file was written AFTER, one literature read (Loos-Gill PRB 84 033103 2011,
    arXiv 1104.0498, Table I) that states the same result. Entered as a check on the derivation, not as a prediction of it.
Numerics: none beyond reading eps0a_table.json and evaluating E0B.