# RESULT-S104-ITEM1-B -- branch B, row 58. Prediction 0c470ded. Instrument pack104/w104b.py;
# receipt w104b-58.json. Scored vs sealed w102b-58.json chords / w103a-58.json law terms.

## SCORE:
PB.1  MISS 0/2. Cross-asym UNCHANGED under 1000x SCF tightening (2e-9): 1.35e-4 / 1.33e-4 vs
      loose 1.36e-4. The (endpoint|partner) asymmetry is NOT SCF-residual content -- it is
      tol-independent (grid-level eigen-relation extraction / X-Vloc partition content).
      The SCF-content hypothesis for the asymmetry is falsified.
PB.2  MISS (sign 2/2 HIT, value 0/2). d_law(6s) = +3.4e-6, d_law(5s) = +3.2e-6 -- IDENTICAL to
      branch A's loose-tol residuals to 3 figures. The +3.3e-6 residual is STABLE under SCF
      tightening: it is not noise.
PB.3  HIT 2/2 (chords stable, worst |d| = 5e-7).
PB.4  HIT. B2 direct-quadrature chord off by -2.0e-2 Ha (>> 1e-8 gate): the non-relativistic
      quadrature is the wrong operator for the sealed scalar-relativistic kernel, as predicted.
      B2 EXCLUDED by comparison.
CAN-FAIL deferred (PB.2 primary MISS -> lever uninformative; S103 precedent).

## COMPARISON VERDICT (branches A and B1 agree; B2 out):
The clean-basis rot restatement stands with a reproducible, tol-stable residual:
  rot_val(6s) = +7.44e-6 = law + 3.4e-6;  rot_val(5s) = -4.65e-6 = law + 3.2e-6.
SCF content is RULED OUT (PB.1 + PB.2 stability). Two candidate mechanisms remain OPEN:
  (i)  physical Hessian-asymmetry content (S103 D1 quadratic hypothesis, still unscored);
  (ii) symmetrization ambiguity of the tol-independent cross element: the +-asym/2 orientation
       freedom reaches the quadratic form through the 2 c_m c_partner M[m,partner] channel;
       back-of-receipt scale 2 x 2.4e-3 x 6.6e-5 / 0.2 ~ 1.6e-6 -- same order, factor ~2 short.
NAMED NEXT LEVER (not run -- ruling): orientation-spread probe: recompute rot_val with the
unsymmetrized cross element in each orientation (T-on-row vs T-on-column). The spread BOUNDS
mechanism (ii)'s contribution; residual excess above the spread is then (i) physical, and the
quadratic law becomes the object. No new solves needed beyond the standard three.

## G5b STATUS AFTER S104 ITEM 1: rot decomposes as [valence linear law, sign- and scale-exact]
## + [+3.3e-6 tol-stable residual, mechanism (i) vs (ii) undecided] + [core-M content, removed
## by projection]. No sealed file edited. F104.1 (hygiene) registered in RESULT-S104-ITEM1-A.
