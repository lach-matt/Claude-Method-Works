# RESULT-S104-ITEM1-A -- rot in the core-projected basis, row 58. Prediction 8f01bbae.
# Instrument pack104/w104.py; receipt w104-58.json. Scored vs sealed w102b-58.json / w103a-58.json.

## SCORE:
PA.1  MISS 4/6 as filed -- but see F104.1: the two s-overlap clauses were unscoreable as written.
      Chords reproduce sealed 4/4 (worst |d| = 4e-11). Fresh overlaps vs sealed receipt at FULL
      precision: s_5s(6s) ds = 0.0, s_6s(5s) ds = 0.0 -- reproducibility is exact; the miss is
      entirely the prediction's truncated constants.
PA.2  HIT 2/2 (sign-exact). rot_val(6s) = +7.438e-6 (+), rot_val(5s) = -4.654e-6 (-).
      THE 5s SIGN FLIPS as predicted: sealed contaminated rot_w102b(5s) = +8.019e-5 -> negative
      in the clean basis, matching the law term. D1 mechanism confirmed at sign level.
PA.3  MISS 0/2 (value-exact 2e-6). d_law(5s) = +3.19e-6 (rot_val = 0.59 x law);
      d_law(6s) = +3.38e-6 (rot_val = 1.83 x law). Residuals are near-equal magnitude, same
      direction (+), in the two-shell 5s<->6s system -- Hessian-asymmetry scale, consistent with
      the S103 D1 quadratic hypothesis (filed there as hypothesis; still not scored).
PA.4  HIT 4/4 (identity <= 1e-12). Declared zero-partner clause CONFIRMED (5p, 5d exact 0).
CAN-FAIL not run: with PA.3 MISS the 6s lever is uninformative (S103 precedent); deferred.

## FAULT F104.1 (severity: HYGIENE -- prediction drafting). PREDICTION-S104-ITEM1 PA.1 filed
## reference overlaps at 4 significant figures against a 1e-9 tolerance -- internally inconsistent,
## clause unscoreable as written. Cause: constants transcribed from a formatted survey print
## instead of the receipt (F79.1 species: label read instead of source). The underlying physical
## check passes exactly against the sealed receipt. No result depends on the faulted clause.

## HEADLINE: core projection removes the bulk of the rot contamination --
##   rot(6s): 1.456e-4 -> 7.44e-6 (20x down, now law-scale); rot(5s): +8.02e-5 -> -4.65e-6
##   (sign flip TO the law). The linear law is sign-correct and scale-correct in the clean basis
##   but a ~3.2-3.4e-6 residual survives above the cubic-remainder bound.
## NOTED (instrument observable, not scored): worst I-matrix asymmetry = 1.4e-4 PERSISTS in the
## valence-only basis -- the F102.3 asymmetry species is not exclusively a core phenomenon.
## Whether the 3.3e-6 residual is instrument (symmetrization of that asym) or physics (Hessian
## asymmetry) is exactly what branch B decides.

## PER FILED PROTOCOL: PA.3 MISS -> branch B runs. Comparison decides.
