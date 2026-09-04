# PREDICTION — T7: the three 4f candidates, ALL THREE, comparison decides (M's ruling, session 16). Written BEFORE any build/run.
Target: the shell-constant 4f offset (HFS-TS_pol − meas): Dy .139, Er .216, Tm .213, Yb .192 Ha (served_prime.tsv; t6.jsonl).
Constraint on every candidate: the 3d/5d results (all served species within ~15% under HFS-TS) must NOT break.
Each candidate is derivable and constant-free; owners named; each has a gate that reduces it to a banked column.

## T7a — orbital-resolved Perdew–Zunger 1981 SIC (owner PZ 1981 eqs 33–35). BUILD: each 4f orbital its own radial function and
V_SIC; f_i = ½ for the half hole, 1 for the full dn orbitals, 1 for the up shell (spherical average only where a shell is closed).
Gate: on a CLOSED-shell channel the orbital-resolved and channel-averaged SIC coincide → reproduce hfs_sic on Zn I 3d (TS in 4s
entrant, sic=True) to 1e-4. Then run Dy/Er/Tm/Yb (+Fe).
PA1  Orbital-resolved SIC DEEPENS all four 4f TS values (self-Hartree of a compact 4f orbital dominates its self-exchange when
     f_i = 1 for the full neighbours), by ≥ .10 Ha, moving AWAY from measurement.  PA2  Fe shift < .03 Ha.
PA3  If PA1 holds, self-interaction is EXCLUDED as owner of the 4f offset (the T6 non-result is closed).

## T7b — exact exchange (Fock 1930) on the entrant channel: HF-TS and HF-ΔSCF (owner Froese Fischer 1977, numerical HF).
BUILD: Fock exchange operator on the log mesh (Slater Y^k integrals; hfs.numerov_wf as inner solver; occupied set = same
occupation as scf_occ). Gate: He 1s HF ε = −0.91796, Ne 2p ε = −0.85041 (Fischer 1977 tables; entered as MEASURED-STANDARD
values, not fitted); with the Fock term switched to Dirac local, regenerate the T5 HFS-TS column.
PB1  HF-ΔSCF 4f removal lies within 30% of measurement for ≥ 3 of Dy/Er/Tm/Yb — the offset is the exchange LANGUAGE (local
     Dirac over-binds the compact shell's removal).  PB2  HF-TS agrees with HF-ΔSCF within 10%.
PB3  3d/5d under HF-TS stay within 15% (relaxation was already the operative correction there).
PB4  If PB1 holds AND PA1 holds AND PC1 (below) gives < half the offset, the comparison decides for exact exchange, and the
     next Zeno step is the full-index run of HF-TS as the observable-level law candidate.

## T7c — scalar-relativistic kernel (owner Koelling & Harmon 1977; Desclaux 1973 for the indirect 4f destabilisation).
BUILD: scalar-relativistic radial equation (mass-velocity + Darwin, no spin-orbit) replacing numerov_wf inside scf_occ.
Gate: c → ∞ (set c = 1e6) regenerates the T5 HFS-TS column to 1e-4; H 1s at c = 137.036 gives −0.5000067 (Dirac scalar).
PC1  Relativity moves 4f TS SHALLOWER (indirect: s/p contraction screens 4f) by .02–.08 Ha at Yb, growing Dy→Yb, i.e.
     ≤ HALF the offset.  Direction right, magnitude short: relativity alone does not close.
PC2  5d (La, Gd, Lu) deepens slightly (direct effect small for d), staying within 15%.  PC3  3d shift < .02 Ha.

## Comparison rule (stated now): the candidate that moves ALL FOUR 4f species toward measurement, uniformly, without breaking
3d/5d, is the direction. Two candidates each partly right ⇒ their SUM is tested next (both derived; no constant), and the
timing flag R 1449 applies to that sum because it is formulated after the runs.