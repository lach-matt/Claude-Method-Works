# FINDING — T6: HFS-TS + Perdew–Zunger SIC on the entrant (session 16). M ruled GO. PREDICTION-T6 written 19:45 UTC, unaltered.
Gate PASSED: scf_sic(20,1,entrant=(3,2),sic=False) = −0.13076 (session-10 gate); SIC −0.1483 matches session-10 −0.148.
Nothing written to register/index/store. Bank 2_13 (R 1700) unchanged.

## Result (RUN-T6-SESSION-16.txt, Ha)          meas   TS_avg  TS_pol  TS_SIC   pol%  sic%   f_avg
Fe 3d  −.397  −.493  −.378  −.385    +5   +3   .50 | Dy 4f −.275 −.494 −.414 −.330  −51 −20  .33
Er 4f  −.256  −.514  −.472  −.564   −84 −121   .56 | Tm 4f −.284 −.522 −.497 −.703  −75 −148  .69
Yb 4f  −.327  −.528  −.520  −.854   −59 −161   .83
## Score
PD1 FAILS as stated: Dy moves SHALLOWER (+.083, toward); Er deepens .09 (< .15); Tm/Yb deepen .21/.33 (away). Mixed, not uniform.
PD2 HOLDS: Fe shift −.007, smaller than every 4f shift, same sign as Er/Tm/Yb.
PD3 FAILS on Dy (pol−avg = .080 > .05); Er .042, Tm .025, Yb .008 hold.
PD4 NOT REACHED cleanly: PD1 mixed. The SIC shift is a monotone function of f_avg, the occupancy-averaged per-orbital weight
    hfs_sic assigns to the entrant channel (.33 → +.08, .56 → −.09, .69 → −.21, .83 → −.33). Small f: the LDA self-exchange
    (∝ f^{1/3}) exceeds the self-Hartree (∝ f) and the SIC turns positive. This is the AVERAGING RULE speaking, not
    Perdew–Zunger: the object shares one radial function and one V_SIC across the whole (n,l,spin) shell and cannot give the
    half-hole orbital its own f_i = ½ while its full neighbours have f_i = 1. PZ SIC on a partially filled shell is NOT
    testable in this object. Self-interaction is therefore NEITHER confirmed NOR excluded as owner of the 4f offset.
## What T6 did establish (robust — the sic=False column is not affected by the averaging rule)
1. Spin-polarised HFS-TS closes Fe: −.378 vs −.397 (5%). With T5, every 3d and 5d served species now sits within ~15% under
   HFS-TS (Sc 7, Ti 11, Cr 13, Fe 5, Ni 10, Cu 3, La 4, Gd 8, Lu 2). Z-flatness recovered across both series.
2. The 4f offset SURVIVES polarisation: TS_pol −.41…−.52 vs meas −.26…−.33; residual .14–.19 Ha, still shell-constant
   (it shrinks Dy→Yb from .14 to .19? no — Dy .139, Er .216, Tm .213, Yb .192: flat within .08). Not relaxation (T5),
   not polarisation (T6), SIC untestable here.
## Faults
F16.4 (stated before the run) — FINDING-T5 reading #2 attributed the offset to SIC with the wrong recorded sign; the run shows
      the sign itself is object-dependent, so the attribution was premature on both counts. Reading #2 is WITHDRAWN.
F16.5 — first RUN-T6 table printed Fe f_avg = .36; correct value .50 (kc = 0). Corrected in the run file, noted there.
## Next candidates, owners on record, RULING OWED (no run without prediction):
(i) orbital-resolved PZ SIC (each 4f orbital its own radial function and V_SIC; f_i = ½ for the half hole, 1 for the rest) —
    a build; tests SIC properly.  (ii) exact exchange (Fock 1930) for the entrant channel — HF-TS/ΔSCF, owner Froese Fischer
    1977 — tests the exchange language.  (iii) relativistic indirect destabilisation of 4f (Desclaux 1973) — the offset's
    sign is right for it (measured shallower); magnitude to be predicted before running.  Comparison should decide among the
    three; each is derivable and constant-free.