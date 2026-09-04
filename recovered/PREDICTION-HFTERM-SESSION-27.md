# PREDICTION — term-resolved (Hund ground term) exact-exchange DSCF + chain correlation, 3d/4f. s27, bridge-26 §3(3). Written BEFORE any run.
Object (hfterm.py): s26 hfdscf (HFSR 'hf', c=C0, integer occ, avg-of-config, neutral & ion) + Hund-term correction to FIRST ORDER in orbital
relaxation: ΔE_term = E[highest-weight determinant of the Hund term (max S, then max L)] − E[average of configuration], both evaluated with the
same avg-of-config HF orbitals of that state, over open-shell spin-orbitals only (closed shells cancel exactly). J/K from Gaunt c^k (sympy 3j)
× radial F^k/G^k of the HF orbitals. D_term = D_avg + ΔE_term(ion; ion orbitals) − ΔE_term(neu; neu orbitals). Δ_c as s26 (unchanged).
resid_HFterm = −D_term + Δ_c + SO_chain − meas, where SO_chain is the chain's spin-orbit part ONLY (3d: so_n−so_i of t7c_3dhund; 4f: soh −
(stab_n−stab_i) of t7c_mult); the chain's Hund stabilisation is NOT added (it is what the term resolution replaces). No constant beyond c.
meas RECALLED-NOT-ENTERED (TABLE-JANAK-24), comparison only. Rows: Sc Ti Cr Fe Ni Cu (3d), Dy Er Tm Yb (4f) = 10.
PT0  Coefficient gate: the determinant-averaged pair energy over all C(4l+2,N) determinants equals N(N−1)/2·[F^0 − (2l+1)/(4l+1)·Σ_{k>0} c3j0²(l,k,l)F^k]
     to 1e-10 for d^2 and f^2 (t7b_hf's w) — the machinery reproduces Slater's average before it is used. Cross-shell: F^0 − ½Σ c3j0² G^k.
PT1  (bridge-26 prediction, carried) |resid_HFterm| < |resid_J| on >= 7 of the 10 rows.
PT2  On Cr and Yb (s26 worst: +0.078, +0.093) the term correction moves obj TOWARD meas: |resid_HFterm| < |resid_HFc(avg)| on both.
PT3  Cr term correction magnitude |D_term − D_avg| in [0.05, 0.12] Ha (Cr 3d5 4s1 7S -> 3d4 4s1 6D loses more exchange than the average).
PT4  Sc unchanged (3d1 -> 3d0: ΔE_term = 0 both states) to 1e-5: a control that the code adds nothing where there is no term.
PT5  Sign pattern: for rows where the ion has the MORE stabilised Hund term relative to average (Fe 3d6->3d5 6S, Ni 3d8->3d7), the correction
     is negative (deepens obj); for Cr/Cu/Tm/Yb (neutral more stabilised or ion less) positive. Stated so the sign is predicted, not read.
Failure of PT0 -> stop; nothing downstream is admissible. Failure of PT1 with PT0 held -> the term-average error was not the 3d/4f residual;
report the per-row split (relaxation second-order not computed) and stop; no scan.
