# PREDICTION — T6: HFS-TS + Perdew–Zunger 1981 SIC on the entrant (session 16; M ruled GO). Written BEFORE any run.
Object: hfs_sic.scf_sic (pack10; spin-polarised Test-E object, per-orbital PZ SIC, exchange-only) with occ = hole configuration
(ground(Z) minus one entrant) and entrant=(n,l) → occupation = ground(Z) − ½ entrant, the entrant half in ONE orbital (f_i=½),
tail −1/r (charge=1). Species: Dy Er Tm Yb (4f) + Fe (3d). Three columns: spin-averaged TS (T5, on record), spin-polarised TS
(sic=False), spin-polarised TS+SIC. Gate: scf_sic(20,1,entrant=(3,2),sic=False) must return Ca 3d −0.13076 (session-10 gate).
F16.4 stated now: FINDING-T5 reading #2 attributed the 4f shell-constant offset to self-interaction; the recorded sign of PZ-SIC
in this project (session 10, Ca 3d) is a DEEPENING, and the 4f TS is already too deep. The attribution was made with the wrong sign.
PD1  SIC deepens the 4f TS by ≥ 0.15 Ha (self-Hartree of a compact 4f orbital), moving AWAY from measurement. The candidate FAILS
     to close the 4f offset.
PD2  SIC deepens Fe 3d too, by less than the 4f shift (3d less compact), same sign.
PD3  Spin-polarised TS (sic=False) differs from the spin-averaged T5 TS by < 0.05 Ha on the 4f species (closed shell in the dn
     channel except the half hole; polarisation small).
PD4  (decisive) If PD1 holds, self-interaction is EXCLUDED as owner of the 4f offset. The offset then sits in the exchange
     language of the compact shell — Dirac local exchange versus Fock 1930 exact exchange — and the next derived candidate is
     exact-exchange (HF) ΔSCF/TS on the entrant channel (owner: Froese Fischer 1977, numerical HF). No constant.