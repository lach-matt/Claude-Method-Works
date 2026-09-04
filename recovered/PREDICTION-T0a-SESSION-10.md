# PREDICTION — T0 option (a′): the self-interaction-free object (session 10, stated BEFORE the run)
Ruling (M, this session): T0 = run BOTH (a′) and (d); every answer is an answer.
Object (a′), as defined for the record: Test-E object of session 9 (spin-polarised, Slater/Janak half-electron
transition state, Dirac exchange, Latter tail, observed Z−1 core) + Perdew–Zunger 1981 self-interaction
correction, orbital by orbital, exchange-only, no constant.  Code: hfs_sic.py.  Baseline: hfs_sic(sic=False)
reproduces Test-E Ca 3d −0.13076 exactly.

FLAG (R 1449): the build smoke test printed Ca 3d under SIC (−0.1483) BEFORE this document existed. The direction
(deeper) was the reasoning below, but was not on record first. Everything after this line is stated first.

Mechanism expected: PZ-SIC removes residual self-Hartree of the entrant half-electron (and of every core
orbital); for a localised orbital the removed repulsion exceeds the restored LDA self-exchange, so localised
channels (d, f) move DOWN more than diffuse ones (s, p).  Therefore:

PS1  Ca I 3d: SIC moves the TS eigenvalue AWAY from the measured −0.113 (deeper than −0.131).  [already seen: held]
PS2  Collapse-onset misses La, Ac, Th (f too deep under Test E by 0.051/0.017/0.153): all three REMAIN misses and
     their gaps GROW.  Falsifier: any of the three flips to a hit.
PS3  Ce, Pr (Test-E hits at f): stay hits (f deepens further, same sign).
PS4  Pairing class Tc, Gd, Cm (Test-E misses by 0.003/0.101/0.217): Gd, Cm gaps GROW (down-f entrant loses its
     self-repulsion, no Hund partner to compensate); Tc undetermined (0.003 hair).  Falsifier: Gd or Cm flips.
PS5  Mn (Test-E hit by 0.057, 4s below 3d-down): stays a hit; margin shrinks.
PS6  Whole walk (only run if the diagnostic set does not already falsify the object as an improvement):
     rule B ≤ 99/106; the recovered timing steps Sr, Ce, Pr, Ra of Test E stay; onset misses stay; Lr stays.
     Falsifier of PS6 (i.e. (a′) is an IMPROVEMENT): ≥ 101/106.

Decision rule stated now: if PS2 and PS4 hold, (a′)-as-SIC is scored as an answer ("no": self-interaction is not
the missing coordinate; the f over-binding of the orbital language is not self-repulsion), the walk is still run
once so the count is on record, and (d) opens.
