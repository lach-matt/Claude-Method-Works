# FINDING-FK-SCALE (s39, item 1) — the F^k feasibility interval, measured, and the candidate refused on its second leg.
Object: gap(lam) = gapHF + lam*(gapTERM - gapHF), lam = F^k_phys / F^k_HF. Arithmetic on the banked s38 table (fkscale.py); no SCF.
The linearity is EXACT, not an approximation: a term energy relative to the average of configuration is a linear combination of the
F^k with k >= 2 and contains no F^0, so scaling every F^k by lam scales the whole term correction by lam.

## 1 · THE INTERVAL EXISTS. PF-1 HELD.
Per-row crossings lam* = -gapHF / (gapTERM - gapHF):
  GAIN  (wrong -> right):  Th 0.2145
  LOSS  (right -> wrong):  U 0.5298 · Pa 0.5490 · Hf 0.6242 · Cm 0.9809
  NO CROSSING (8 rows):    Sc Y La Ce Gd (s-first throughout) · Lu Ac Rf (d-first throughout)
FEASIBLE. 13/13 on lam in (0.2145, 0.5298). Verified twice and independently: by the crossing algebra, and by direct
evaluation of all 13 rows on a 1001-point grid (13/13 at 315 consecutive points, [0.215, 0.529]).
Score curve: 12/13 -> 13/13 at 0.22 -> 12/13 at 0.53 -> 11/13 at 0.55 -> 10/13 at 0.63 -> 9/13 at 0.99.
Rounding sensitivity (table is 4 dp, +-5e-5 per gap): worst-case window (0.2158, 0.5288). The width survives; nothing here is
an artefact of the printed precision.

## 2 · THE WINDOW IS BOUNDED BY U, NOT BY Cm — AND THE ORDERING WAS PREDICTED EXACTLY
Predicted ordering Th < U < Pa < Hf < Cm: HELD, 5/5. Cm's near-tie at lam=1 (-0.0009) made it look like the binding constraint
and it is the LOOSEST of the four (0.98). The binding row is U, whose shift -0.0504 is the largest in the table.

## 3 · AND THE CANDIDATE DIES ON THE CONSISTENCY LEG. PF-5 HELD.
The source debt PF-5 owed is PAID, with primaries, and the recalled figure was on the optimistic side of the literature:
 · Cowan (1981)'s standing recommendation for Slater integrals is a scale of 0.85.
 · A MEASURED ratio, not a convention: Sn(11+) / Sn(12+) fitted-against-HFR electrostatic parameters give
   F^2(4d,4d) FIT/HFR = 0.857 and 0.857, F^4(4d,4d) = 0.884 and 0.877 (EBIT optical spectroscopy).
 · For LOCALIZED systems — explicitly actinides and rare earths, i.e. exactly the rows that break — the Coulomb and exchange
   parameters typically require scaling to 70-80% of the HF value, to account for configurations omitted from the calculation.
 · EXCLUDED as a different physical environment: solid-state values near 0.75 (dd) reflect crystal screening, not a free atom.
PHYSICAL BAND lam_phys ~ 0.70 .. 0.90. REQUIRED BAND lam_req = 0.215 .. 0.529. THE TWO DO NOT OVERLAP AND ARE NOT CLOSE:
the table needs F^k cut by 47-79%, where screening supplies 10-30%. The gap at the nearest edges is 0.53 against 0.70.
VERDICT: FEASIBLE BUT INCONSISTENT. A uniform F^k scale is REFUSED as the mechanism. Nothing is adopted; no lam enters any field.

## 4 · WHAT THE REFUSAL MEASURES — this is the point of running it
The interval is not a failed fit, it is a number about the residual's SHAPE, and it says: to put all 13 rows right by shrinking
the multipole interaction uniformly, one must shrink it about THREE TIMES harder than the physics allows. Equivalently, at the
physical scale lam ~ 0.85 the table stands at 10/13 — WORSE than the plain HF field's 12/13. THE HONEST F^k CORRECTION MAKES THE
WALK WORSE. This is the same verdict s38 reached at lam = 1 (9/13, not adopted), now shown to hold across the whole physical band
rather than at one point, and it closes the linear-in-F^k family entirely: no member of it is both correct and physical.
CONSEQUENCE FOR THE CHAIN: the row-differential residual is NOT a multipole-MAGNITUDE problem. Magnitude is the one thing a
uniform scale can address and it has now been swept. What remains unswept is the ANGULAR side — whether the term the diagonal-sum
picks is the right object for the four rows where LS coupling is weakest (Hf 5d; Pa, U, Cm 5f). SO was eliminated as a companion
(PS-1, s38) but SO was applied as a first-order ADDITIVE Lande shift, which is not the same operation as intermediate-coupling
diagonalisation, where zeta and F^k compete inside one matrix and the ground level is NOT the LS term plus a correction.

## 5 · Failed predictions (logged, not suppressed)
PF-3 MAGNITUDE FAILED: predicted lam_U = 0.39 +- 0.08, measured 0.5298 — outside the bracket. The row identity was right and the
ordering was right; the number was wrong for a reason worth naming. I estimated U's gapHF from the CLASS-C MEAN shift (-0.0389)
when U's own shift is -0.0504, the table's extreme. THAT IS THE PER-ELEMENT-FROM-CLASS-MEAN FAULT, committed against a table
already in the bank one line away. Registered as F39.1 — caught in scoring, affects no result; the run reads per-row throughout.
PF-2 held at 0.2145 vs 0.214 +- 0.002 and is NOT counted as a success: it was flagged at filing as arithmetic on banked Th figures.
PF-5's stated reduction band (60-80%) was NARROWER than measured (47-79%); the verdict it predicted is unaffected, the interval
being more permissive than expected and still nowhere near the physical band.
HELD: PF-1, PF-4 (all 8 non-crossers, Ac included, survive the whole of [0,1]), PF-5 verdict, PF-3 ordering clause.
Timing flags: none. PF-6 not reached (the interval is non-empty).

## 6 · Open, in the order the finding leaves them
(1) Intermediate coupling as the angular question §4 leaves: diagonalise zeta against F^k for the four rows rather than adding
    a first-order Lande shift to an LS term. This is NOT a re-run of s38's SO — it is a different operator ordering, and PS-1's
    sign argument explicitly does not settle it (PREDICTION-SO-SIGN, Held).
(2) PV-3 frozen-vs-relaxed, still untested; the frozen avg-of-config convention is USED and its bound is NOT measured.
(3) Whether the four broken rows share anything beyond weak LS coupling — Hf and Rf are both class B 5d/6d and Rf is fine.
