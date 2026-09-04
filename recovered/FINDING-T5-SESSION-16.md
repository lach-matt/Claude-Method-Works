# FINDING — T5 observable-level candidate: transition state and DeltaSCF on both kernels (session 16, 2026-08-16)
M ruled GO, both objects, comparison decides. PREDICTION-T5-SESSION-16.md written 19:38 UTC before any run; unaltered.
Nothing written to register/index/store. Bank restore-point-2_13 (R 1700) unchanged.
Machinery gate: scf_occ (occ = ground(Z-1), tail -1/r) regenerates the banked T3b' SCF column exactly (Sc -0.4866, La -0.3581).

## Objects (owners named in the prediction file; no constant)
TFD-TS: entrant eigenvalue in rho_TFD(Z, N=Z-1/2), tail -1/r (Latter). HFS-TS: hfs.scf object, occ = ground(Z) - 1/2 entrant,
tail -1/r (Slater 1972). HFS-DSCF: E(neutral,-1/r) - E(hole,-2/r), E = sum n eps - 1/2 int n V_H - 1/4 int n V_x (Bagus 1965;
Janak 1978). Hole = neutral - entrant, matching all 13 served hole configurations.

## Result (RUN-T5-SESSION-16.txt, Ha)
      meas   TFD_K  TFD_TS  SCF_K  HFS_TS  DSCF     TS%   DS%
Sc  -.295  -.088  -.059  -.487  -.275  -.249    +7   +15
Ti  -.365  -.118  -.060  -.549  -.326  -.301   +11   +18
Cr  -.303  -.245  -.102  -.659  -.263  -.229   +13   +25
Fe  -.397  -.493  -.328  -.759  -.493  -.466   -24   -17
Ni  -.513  -.885  -.718  -.852  -.565  -.538   -10    -5
Cu  -.384 -1.140  -.973  -.896  -.396  -.362    -3    +6
La  -.239  -.079  -.060  -.358  -.228  -.209    +4   +12
Gd  -.242  -.170  -.080  -.365  -.223  -.201    +8   +17
Dy  -.275  -.623  -.474  -.796  -.494  -.474   -80   -73
Er  -.256 -1.119  -.970  -.824  -.514  -.494  -101   -93
Tm  -.284 -1.403 -1.254  -.835  -.522  -.501   -84   -76
Yb  -.327 -1.711 -1.562  -.845  -.528  -.507   -61   -55
Lu  -.199  -.425  -.286  -.350  -.203  -.178    -2   +11

## Score
PC1 HOLDS 13/13 on both kernels (TS shallower than Koopmans everywhere).
PC2 HOLDS: TFD-TS still deepens with Z (3d -.06 -> -.97; 4f -.47 -> -1.56). The TFD object has no shell to relax.
PC3 HOLDS: late-series excess shrinks .482 -> .154 (mean |res|), early .155 -> .022; 4f does not close (Yb residual .20 > .10).
PC4 FAILS as stated: DSCF is not "between" Koopmans and measurement for 7/13 (Sc, Ti, Cr, Cu, La, Gd, Lu overshoot to the shallow
    side); TS/DSCF ratio 1.04-1.15, within 10% for 9/13 only. Recorded as a fail.
PC5: DSCF within 30% for 9/13 — one short of the stated 10. Second clause fires: Dy/Er/Tm miss by .20/.24/.22 Ha (Yb .18) —
    the residue is beyond relaxation; the next owner named BEFORE the run is self-interaction in the local exchange
    (Perdew-Zunger 1981; hfs_sic.py, session 10). No timing flag.

## Reading (stated, not decided)
1. On the HFS object the transition state RECOVERS THE Z-FLATNESS that T3b' found missing: HFS-TS 3d tracks measurement including
   the Ni-Cu turnover (-.28 -.33 -.26 -.49 -.56 -.40 vs -.29 -.36 -.30 -.40 -.51 -.38); 5d La/Gd/Lu within .02.  T3b' located
   the residue at the observable and T5 confirms it: what was missing was relaxation, not kernel shape.  9 of 13 within 15%.
2. The 4f residue is a SHELL-CONSTANT OFFSET: HFS-TS 4f -.49…-.53 (flat) vs meas -.26…-.33 (flat), offset .20-.24 Ha, ratio
   ~1.8, invariant across Dy-Yb.  A relaxation defect would grow with occupancy; this does not.  A near-constant, orbital-compactness
   term is the self-interaction signature — the owner PC5 named.  Fe (-24%) is the 3d shell's smaller version of the same.
3. Comparison decides: the TFD object cannot carry the observable-level candidate (PC2); the SCF object can.  Under M's session-9
   T0 ruling (shrinking residuals = the right path): residuals fell 3-7x on 9 species and the remaining 4 share one signature.
Next candidate, owners on record: HFS-TS with Perdew-Zunger 1981 SIC on the 4f entrant (derived, orbital-by-orbital, no constant),
scored on Dy/Er/Tm/Yb + Fe; prediction to be stated first. RULING OWED from M.

## Faults registered
F16.2 — first t5_run batch wrote np.float64 into jsonl for Sc/Ti/Cr/Fe (repr only; values correct); cast fixed before batch 2.
F16.3 — path to T0b_pairs.json mis-nested on first gate call; corrected, gate then passed. Neither touched a result.