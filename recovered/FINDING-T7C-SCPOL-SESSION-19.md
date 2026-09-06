# FINDING — SC-SR spin-polarised TRANSITION-STATE re-probe of the corridor residues (session 19, bridge-18 s3(1'), ruled by M: all three, writability order)
Bank restore-point-2_13 (R 1700) unchanged. Findings only. Instrument t7c_scpol.py (scf_pol_sr of t7c_pol.py on the ion core, tail q=Z−N_core, 1-based charge).
## PP0 — derived, then gated
Bare-probe pol on a closed core is IDENTICAL to SC-SR: V_x^pol = −(6ρ_σ/π)^{1/3} with ρ_σ=ρ/2 equals V_x = −(3ρ/π)^{1/3}. Ce IV bare-pol SR
d = −0.42268 = t7c_scres −0.42268 to five digits. So bridge-18 s3(1') as a bare probe is vacuous; the non-vacuous object is the ion analogue of the
line that closed the neutral 4f offset (T5 TS → T6 pol → T7c SR): probe shell at occupation ½ in the SCF, spin-polarised, SR, each pair member in its
own SCF. R 1449 timing: the object was NAMED in bridge-18 before this session; its SPECIFICATION as TS was made in this session after PP0 — flagged.
## Result (RUN-T7C-SCPOL-SESSION-19.txt; d = E(second)−E(first), Ha; no constant, no measured input)
Ce IV 4f−5d : meas −0.227 | bare SR −0.423 | TS-SR −0.252 (residue −0.025). TS share +0.178 (nr), SR share on TS +0.114.  PP1 HOLDS.
Pr V  4f−5d : meas −0.524 | bare SR −0.745 | TS-SR −0.553 (residue −0.029). TS share +0.198, SR share +0.135.               PP1 HOLDS.
Ra II 6d−7s : meas +0.055 | bare SR +0.041 | TS-SR +0.070 (residue +0.015, order kept). TS +0.052, SR +0.060.              PP2 FAILS (|Δd| 0.029 > 0.02).
Sr II 4d−5s : meas +0.070 | bare SR +0.022 | TS-SR +0.079 (residue +0.009). nr TS ALONE +0.067; SR adds +0.012.             PP3 FAILS (|Δd| 0.057 > 0.03) — CLOSES.
Th IV 5f−6d : hold | −0.155 → −0.058 : hold preserved.
Lr I  7p−6d : 7p<6d | +0.068 → +0.010 : the scalar TS object brings 7p to within 0.010 Ha of 6d; the spin-orbit gap left is 0.010, not 0.068.
## Reading (after the run, flagged)
1. All four measured residues are within 0.03 Ha of measurement on one object, with no constant: Ce IV, Pr V, Ra II, Sr II.
2. Sr II is an OBJECT fault, not a physics residue: the bare-probe object (T0b) was the wrong object; the TS object closes it nonrelativistically (+0.067
   vs +0.070). Sessions 12–16 "closed negative" was correct for the object they tested and wrong about the residue. Same for the "T0 family" label on
   Ce IV / Pr V: they are TS + relativistic (shares 0.18/0.11 and 0.20/0.13), neither alone.
3. Both prediction FAILS are under-predictions of the TS effect on s/d pairs; recorded as fails, not reinterpreted.
4. Lr I: the two-component build (s3(2)) is now needed for 0.010 Ha, not 0.068. Its scope shrinks; whether it is still worth building is M's.
## Files: t7c_scpol.py t7c_scpol.jsonl RUN-T7C-SCPOL-SESSION-19.txt FINDING-T7C-SCPOL-SESSION-19.md
