# PREDICTION-STAGE23 (s37) — written BEFORE any run (R 1449). Rulings (M, s37): (1) do (a) AND (b), comparison decides; (2) read bridge-35 §3(3) then reweigh
the walk-field question; (3) record read after 1 and 2; (4)(5) held unless needed. Read done: FINDING-B2, FINDING-XSEAM, FINDING-LWALK, R 1436/1439, beta_nl law.
Nothing entered; no constant; no measured input. Record first-ionised subshells (PN5 target) are RECALLED-NOT-ENTERED and enter the comparison column only:
s-first: Sc Y La Ce Gd Th · d-first: Lu Hf Ac Rf Pa U Cm (Pa U Cm remove 6d).
LOCAL relaxed d-minus-s depth (Stage 1, TABLE-NLWALK; positive = d deeper): La 0.048 Ce 0.039 Gd 0.020 Th 0.076 | Lu -0.016 Hf 0.025 Ac 0.042 Pa 0.038 U 0.038 Cm 0.039 Rf 0.062.
READ (pre-run): the two record classes OVERLAP in local gap (Gd 0.020 s-first vs Hf 0.025 d-first; Th 0.076 s-first vs Rf 0.062 d-first). Consequence: NO UNIFORM
SHIFT of the local point can separate them; only a row-differential term can. That is the test both stages are asked.

## (a) Stage 2 — SR HF (hfc2, no corr) DSCF frontier pairs: rows Hf Ac Th Rf Pa U Cm Gd (+ Ce if budget). nlwalk_hf.py.
PH1  HF puts the d partner SHALLOWER (d leaves first) on Hf, Ac, Rf: HELD if >= 2 of 3 (mechanism: Lu precedent, HF 6s deeper by 0.051; SR 7s at Ac).
PH2  HF keeps s shallower on Th and Gd (record s-first): HELD if both; the named risk row Th by < 0.05.
PH3  On Pa U Cm (record removes 6d) HF puts 6d shallower than 7s: HELD if >= 2 of 3 (same seam as Ce 4f in HF).
PH4  Size bound: on every d-first row |D_s - D_d|(HF) <= 0.06 (only precedent Lu 0.051).
PH5  COMPARISON: HF scores >= 6/8 on these rows where local scores 2/8 (Th Gd). Over the 13 d/s rows (Sc Y La Lu + 9): HF >= 10/13, local 7/13.
PH6  Ac 5f is NOT needed for (a) (removals are of occupied 6d/7s) — item 4 stays held; if any HF SCF hits maxit the value is a bound and is said so.

## (b) Stage 3 — SR local walk (KH kernel numerov_wf_sr in SCF and orbitals; SIC in the energy only, as Stage 1), 25 rows, both SIC conventions on ONE orbital set.
BUILD GATE (not a prediction): at c = 1e6 the SR walk reproduces Stage 1 Sc 3d D_rel -0.34175 / swap4s -0.26903 within 1e-3.
PS1  SR moves the relaxed d/s gap toward s-DEEPER on every d row (SR contracts s more than d): period 4 0.005-0.02, period 5 0.01-0.03, period 6 0.03-0.06,
     period 7 0.05-0.10 Ha. Sign HELD on all d rows; windows scored per period.
PS2  Because the shift is monotone within a period and the record interleaves, SR local does NOT separate the classes: no threshold on the SR relaxed gap
     separates s-first from d-first rows, and the PN5 count moves by at most +-3 from 16/22 (gains among Hf Ac Pa U Cm, losses among Gd Ce La Th).
PS3  The local (n-2)f collapse survives SR: La 4f remains the deepest relaxed channel by > 0.05 (SR shifts 4f shallower by < 0.03).
PS4  SIC convention (per-electron on P^2 vs f_orb): f_orb removes most of the SIC of a single d/f electron (f = 1/5, 1/7: (2l+1)f^2 E_H + (2l+1)f^{4/3} E_x can be
     NEGATIVE), so under f_orb every open d/f channel is SHALLOWER by 0.1-0.3 Ha than under per-electron while s channels (f = 1) do not move: f_orb turns the
     walk s-deeper on EVERY d row — the reversal becomes two-sided the OTHER way (passes Hf Ac Rf Pa U Cm, fails Sc Y La Ce Gd Th). Score(f_orb) <= score(per-e).
     Neither convention gets both classes; the comparison decides which is carried, and the prediction is that it decides for per-electron on P^2 (the physical
     one-electron self-density) — with the classes still unseparated.
PS5  Cs/Ba/Fr/Ra: SR does not change PN2's f-shallowest ordering (4f/5f still the shallowest channel on the s rows).

## Comparison rule (stated before results): the object that separates the record classes on the d/s frontier with the fewer failures is the walk's field;
## if HF separates and SR-local does not, ruling 2's question is answered by comparison and the local kernel is a comparison column. If neither separates,
## the "other mechanism" is row-differential and outside both fields — read against R 1436 (five of the eight handshakes are on these rows: La/Ce, Th/Pa,
## Gd/Tb-adjacent, Cm/Bk-adjacent, Lr/Rf) and beta_nl (SIC sibling law: N_sib differs across the interleaved rows).
