# PREDICTION — T5 observable-level candidate (session 16; M ruled GO, both objects, comparison decides)
Owners: Slater 1972 (transition state), Slater & Wood 1971, Bagus 1965 (DeltaSCF), Janak 1978 (dE/dn_i = eps_i),
Latter 1955 (tail rule: an electron sees Z minus the others). No constant chosen. Written BEFORE any run.
Objects: TFD-TS = entrant eigenvalue in rho_TFD(Z, N=Z-1/2), tail -1/r (T0(b) machinery, gated).
         HFS-TS = hfs.scf object with occ = ground(Z) minus 1/2 entrant, tail -1/r.  Gate: occ=ground(Z-1) regenerates
         the T3b' SCF column (T0b_pairs.json).  HFS-DSCF = E(neutral,-1/r) - E(hole,-2/r), E = sum n eps - 1/2 int n V_H
         - 1/4 int n V_x.  Species: the 13 served in served_prime.tsv; hole = neutral minus entrant (matches 13/13).
PC1  TS moves every entrant shallower (toward measurement) on BOTH kernels vs the T3b' Koopmans columns (more screening).
PC2  TFD-TS does NOT recover Z-flatness: the deepening with Z persists, at most uniformly shifted (no shell in TFD).
PC3  HFS-TS shrinks the late-series excess (Fe, Ni, Cu, Dy-Yb) more than the early one (Sc, Ti, La, Gd) — relaxation grows
     with occupancy — but does NOT close within 30% for the 4f species (Yb residual > 0.10 Ha).
PC4  HFS-DSCF lies between Koopmans and measurement; HFS-TS agrees with HFS-DSCF within ~10% (Slater's second-order claim).
PC5  (decisive) If HFS-DSCF is within 30% of measurement for >= 10 of 13, the observable level is the closure direction.
     If late-4f still misses by > 0.2 Ha, the residue is beyond relaxation and the next owner is self-interaction in the
     local exchange (Perdew-Zunger 1981), already on record as hfs_sic.py (session 10).
Machinery notes stated now: the Latter min makes the total energy non-variational in the tail region; the effect is common
to both configurations and is not repaired here (would be a choice).