# FINDING — T7a: orbital-resolved Perdew–Zunger SIC (session 17). Owner PZ 1981, PRB 23, 5048, eqs 33–35.
Bank 2_13 (R 1700) untouched; findings only. Scored against PREDICTION-T7-SESSION-16.md (not rewritten). Data: t7a.jsonl.
## Build (t7a_sic.py) — hfs_sic.scf_sic verbatim, every channel split into orbital groups with their OWN radial function and OWN V_SIC:
integer-occupied orbitals f_i = 1 (open or closed), the half-hole entrant f_i = ½. Gate PASSED: Zn I 4s-TS entrant and both 3d channels
identical to hfs_sic to the last digit (−0.323941; −0.915922; −0.914734). Second, unplanned exact check: Fe 3d (kc = 0) reproduces the
T6 ts_sic value −0.3854 exactly, as it must.
## Score (nonrel spin-polarised TS; entrant TS eigenvalue vs t6 ts_pol)
Dy −0.4233 (shift −0.0096) · Er −0.4755 (−0.0040) · Tm −0.4979 (−0.0012) · Yb −0.5182 (+0.0016) · Fe −0.3854 (−0.0074).
PA1  FAILS on magnitude: |shift| ≤ 0.010 Ha (predicted ≥ 0.10 deepening); direction not uniform (Yb +0.002).
PA2  HOLDS: Fe shift 0.007 < 0.03.
PA3  Written as conditional on PA1; PA1 did not hold. The exclusion nevertheless follows, by a different route than the file anticipated
     (reading, flagged as such): SIC has NO leverage on the transition-state 4f eigenvalue — ≤ 5 % of the 0.14–0.22 Ha offset.
## Why (Yb diagnostic, ⟨φ| · |φ⟩ over the entrant orbital): f = 1 4f: ⟨vH_self⟩ +1.31, ⟨vx_self⟩ −0.75, ⟨V_SIC⟩ −0.56 Ha (large, deepens
the integer-occupied 4f to −1.02/−1.04). f = ½ entrant: ⟨vH_self⟩ +0.618, ⟨vx_self⟩ −0.564, ⟨V_SIC⟩ −0.054 Ha — self-Hartree ∝ f, Dirac
self-exchange ∝ f^{4/3}: at f = ½ they nearly cancel, and sibling relaxation removes the rest. Structural: PZ SIC is near-self-cancelling
on the Slater/Janak half-electron observable, so it cannot own a shell-constant offset on that observable. The T6 channel-averaged column
(−0.33 … −0.85, tracking mean f) is confirmed an artefact of the mean-f weighting; T6's "untestable" verdict is now closed as "tested: null".
## Comparison rule: T7a moves none of the four toward measurement. Combined with T7c: relativity owns the offset; self-interaction does not.
Faults: none. (f_orb left in t7a_sic.py as dead code, unused — cosmetic, noted.)