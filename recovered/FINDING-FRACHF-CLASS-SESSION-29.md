# FINDING — (a') table on the ONE function, all six class rows.  s29. Files: PREDICTION-FRACHF-CLASS-SESSION-29.md (before any run), frachf.jsonl
# (Cs Sc La Lu appended; Y Gd from s28), TABLE-FRACHF-CLASS-SESSION-29.txt. No constant beyond c; no measured input; RECALLED-NOT-ENTERED unchanged. Not a closure.
Rulings in force: SUBCELL=1 standing (s29, adopted); correlation term = I = int eps(f) df on the sc path (s28, carried — s29 re-asked it in error, on record).
## Results (see TABLE)   I(Cs Sc La Lu) = 0.1301 0.2924 0.2237 0.1788;  with Y 0.2154, Gd 0.2082.
PA0 HELD: Cs endpoints == hfc2 obj_2 (2e-6) and D_HF (1.0e-4); Sc/La/Lu D_HF == s26 hfdscf to 1e-4.
PA1 FAILED on Sc only: Janak gap -0.00119 corr / -0.00073 HF (stated 6e-4 / 4e-4); Cs La Lu HELD (3e-5 .. 4e-4). Mechanism: the gap is Simpson
    quadrature error, not a Janak violation — Sc's eps(f) spans 0.092 over the path (Y 0.045, Lu 0.035) with eps(0) linearly extrapolated; the
    error scales with the fourth derivative of a function twice as steep. The five-point ladder is uniform for every row; Sc needs the f=0
    slope computed, not extrapolated, or one more point. Not repaired in-session (stop rule).
PA2 HELD all four: gap_sc Sc -0.0010 La -0.0007 Lu -0.0008 (in [-0.0012,0]); Cs -9e-5. The correlation midpoint-vs-integer gap on the sc path is
    curvature order on every class row; the s26/s27 0.008 sits between orbital sets on every row, inside neither form.
PA3 FAILED on Sc only: -eps(1/2) - I = 0.0041 (stated [0.0015,0.0030]); La 0.0017 Lu 0.0019 Cs 0.0000 HELD. Same cause as PA1: the HF-path
    curvature is set by the eps span, and Sc 3d is the compact shell (span 0.10 HF).
PA4 HELD on Cs (short 0.0130), La (short 0.0149) and Sc (I 0.2924, within 0.0022 of 0.2946 — the only class row within 0.005, as predicted);
    FAILED on Lu: short 0.0206, outside 0.010-0.016. Mechanism: my calibration error — the frozen s26 shortfall on Lu was already 0.0129, so
    frozen + 0.008 relaxation = 0.021, exactly what came out; the prediction range was read off La/Y, not Lu. On record.
## Standing
The (a') table stands on ONE function for all six class rows. Under it the class-row shortfall against measurement is 0.013 (Cs, Y), 0.015 (La),
0.021 (Lu), 0.034 (Gd) — and 0.002 on Sc, where the frozen form had over-bound by 0.008. Sc is therefore the row where relaxation of E_c^SIC
(first-order, ~0.008-0.010) is the whole of the frozen-vs-measured discrepancy; on the 5d/6s rows the same relaxation moves the number the wrong way,
so the remaining 0.013-0.021 is not orbital response of the correlation-SIC. That remainder is the open object.
Failed predictions s29: PA1 (Sc), PA3 (Sc), PA4 (Lu). Timing flags: none — the prediction file preceded every run. Overrun: batch 2 (La Lu) exceeded
the tool budget after La wrote; Lu rerun alone (234 s), Zeno as designed. Gate for HANDOFF-29: python3 frachf.py 55 21 57 71 -> must SKIP all four.