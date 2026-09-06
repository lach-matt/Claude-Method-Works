# SPEC — the d-row excess (~0.009 Y La Lu, ~0.001 Sc; Cs settled as one object twice-named): BOTH routes, comparison decides.  Ruled M s29.
# For session 30. Rulings in force: SUBCELL=1 standing; correlation term = I on the sc path; adiabatic A closed (FINDING-COREPOL). Predictions BEFORE runs.
Order: (0) gates 1-40. (1) write PREDICTION-DROW-SESSION-30.md covering both routes with numbers committed. (2) Route P (object property) — cheap, first.
(3) Route N (non-adiabatic second order) — build. (4) COMPARE-DROW-SESSION-30.md: comparison decides; no scan; no constant.
## Route P — is the deficit a property of the local correlation form (like the cut)? Test without a new form:
  P1 On the six class rows, decompose the delivered correlation DEc_sc into (a) the total-density GB term restricted to r < r_cut, (b) the entrant PZ SIC
     term, (c) what the cut removes (r > r_cut, from cutfrac). If (b) on the d rows is comparable to the excess (~0.009) and its shape tracks it
     (Y La Lu ~equal, Sc small), the deficit is the SIC of the entrant's own correlation over-subtracting inside the core: an object property, statable.
  P2 Row-invariance test: excess/(entrant charge inside r_cut but OUTSIDE the (n-1)p peak) — a geometric ratio; if it is a single number on Y La Lu Sc
     to within 20 %, the deficit is geometric (form-domain), state it in the book; if not, it is physics -> Route N decides.
  Predictions to commit: sign of (b) on each row; whether P2 ratio is constant. Runs: recompute from cutfrac densities (six SCFs already in cutfrac.py;
  extend it, do NOT re-derive DEc).
## Route N — non-adiabatic entrant-core second-order correlation (the honest A). Build on the shooter (t7c_kernel eigen_sr / numerov_wf_sr):
  N1 spectrum: for the ion HFS(-SR) local potential, bound states l=0..3 up to n=n_max where eps>-1e-3, plus a discretised continuum on the log mesh
     (box states in the same potential: solve h_l on the mesh as a banded eigenproblem, keep eps<+3 Ha; state the box). This is the chain's own basis.
  N2 E2 = - sum_{i in closed core} sum_{a,b unocc} |<i e|1/r12|a b>|^2 / (eps_a+eps_b-eps_i-eps_e), dipole (k=1) Slater integral only, direct term
     (exchange next), entrant e = the HFS entrant orbital, i over the closed core ((n-1)s2p6 and inward; ns2 excluded and reported separately).
     Adiabatic limit check: dropping eps_b-eps_e in the denominator and summing over b closes to the s29 corepol E2 (gate: Cs within 10 %).
  N3 predictions to commit before running: E2(closed) on Y La Lu within [0.005,0.015], Sc <= 0.003, Cs in [0.008,0.02] (one object with B, s29 PC3);
     ratio Sc/Y < 0.3. Failure with mechanism reported. Budget: one row ~ minutes; six rows in batches <= 2 (Zeno; per-row rows written to drow_n.jsonl).
## Comparison: P says "domain of the form" if P1/P2 hold; N says "missing physics" if N3 holds. Both holding = the SAME 0.009 named twice (as Cs);
  neither = new object; one = that one. Write COMPARE-DROW with the decision, then bridge-30 §3 carries: 4f Yb as one object (needs second radial function),
  term-resolved SCF Fe/Ni conditional, T4 writing chat LAST (R 1701-1872 + s29 R 1873-1876).
Files owed by s30: PREDICTION-DROW, drow_p.py/drow_p.jsonl, drow_n.py/drow_n.jsonl, COMPARE-DROW, bridge-30, README-30/HANDOFF-30 superset.