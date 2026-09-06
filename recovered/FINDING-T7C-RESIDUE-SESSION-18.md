# FINDING — SR re-probe of the relativistic corridor residues (session 18, 2026-08-16)
Bridge-17 s3(2)b, ruled by M. Object = T0b probe (tfd.potential(Z,Z-N), eigen zeta=2, pair d = E(second)-E(first)); only the
kinetic language changes: eigen_fix (nonrel) -> t7c_kernel.eigen_sr (c = 137.035999). Gate: c = 1e6 regenerates T0b baseline
d exactly (Ra II -0.0018, Th IV -0.0436, Sr II -0.0022). Frozen kernel: DIRECT relativistic effect only, no self-consistent
screening (no indirect effect), no spin-orbit. Predictions PR1-PR3 written in t7c_residue.py before the run.
## Result (RUN-T7C-RESIDUE-SESSION-18.txt)
Ra II 6d-7s : meas +0.055 | nonrel -0.0018 | SR +0.0451 (7s -0.0625, 6d -0.0157) -> PR1 HOLDS. Order corrected; 82 % of meas.
Th IV 5f-6d : hold        | nonrel -0.0436 | SR -0.0376                            -> PR2 HOLDS (hold preserved).
Lr I  7p-6d : 7p<6d       | nonrel +0.1812 | SR +0.2088 (6d -0.0655, 7p -0.0379)   -> PR3 FAILS: moves AWAY. Scalar + frozen
              cannot reach 7p<6d; needs spin-orbit (7p1/2) and self-consistency: Eliav 1995 / Sato 2015 boundary stands, now
              located: nonrel TFD is 0.18 Ha wrong on Lr, an R 1578-class boundary of the one-electron object, not a residue.
Sr II 4d-5s : meas +0.070 | nonrel -0.0022 | SR +0.0087 (control)                  -> Sr II residue is not relativistic.
## Reading
The Ra II residue is closed to within 0.010 Ha by relativity alone (no constant), consistent with T7c owning the 4f offset.
Next derivable step (candidate, ruling owed): SELF-CONSISTENT SR re-probe (scf_occ_sr exists in t7c_kernel.py) of Ra II, Th IV,
Sr II, Ce IV, Pr V, Lr I — adds the indirect (screening) effect; and a spin-orbit (two-component / j-resolved) kernel for Lr I.
Sr II / Ce IV / Pr V remain the nonrelativistic onset residues (T0 family, closed negative in sessions 12-16).
## Files: t7c_residue.py RUN-T7C-RESIDUE-SESSION-18.txt FINDING-T7C-RESIDUE-SESSION-18.md