# RESULT-S103-ITEM2 -- defect(q) derived as ONE function at the ts93 5pt Gauss nodes, rows 58/90/91.
# Prediction 2542083a hash-gated before all arithmetic. Receipts w103-{58,90,91}.json (+ caches).
# ~22 fresh SCF solves per row; g(q_i) read from SEALED ts93-*-5pt receipts; g5 drift 0.0 all rows.

## SCORE (Rule B lines as filed):
P1 SUM        HIT 3/3. Gauss5(defect) > 0 and within +-3e-5 of -T1 at every row:
              90: +3.701e-5 vs +5.9e-5 (d=-2.20e-5) | 91: +5.144e-5 vs +4.1e-5 (d=+1.04e-5)
              | 58: +8.961e-5 vs +9.5e-5 (d=-5.4e-6). Non-vacuous can-fail satisfied: fresh
              solves through derivative stencils reproduced sealed numbers they never read.
P2 MIDPOINT   HIT 3/3, value-exact: +3.329e-5 / +5.774e-5 / +9.014e-5 vs d101 fresh (tol 2e-5;
              actual agreement <=5e-8).
P3 CROSSING   MISS (severity: prediction-granularity, no fault; instrument clean). Strict
              all-nodes-positive holds at 58 (5/5) and 90 (5/5); at 91 node 5 (q=0.95309)
              defect = -5.862e-6 -- NEGATIVE but inside the declared FD-noise indeterminate band
              (-2e-5, 0). The real-crossing falsifier (< -2e-5) did NOT fire. Crossing NOT
              established; strict clause NOT met. Entered as MISS, no reinterpretation.
P4 SHAPE      HIT 2/2. 90-A sum>mid with lower-edge node above mid (+5.567e-5 > +3.329e-5);
              91-A sum<mid with upper-edge node below mid (-5.9e-6 < +5.774e-5).

## FINDING (answers RULING-M-S102-POST-SEAL):
The integrated-vs-pointwise "sign flip" is DERIVED as a sign convention, not an interior crossing:
T1 = quad - D = -Gauss5(defect) + O(<1e-7). One function defect(q), positive across the interval
at rows 58 and 90 and at 4/5 nodes at 91, reproduces BOTH sealed exposures: the midpoint
pointwise positives AND (with orientation) the sealed negative integrated column. OBS-S103-1
confirmed in substance. The s101 pattern holds: one root, two exposures.

## OPEN (named, bounded): row 91 upper-node resolution. defect(0.953) = -5.9e-6 sits inside FD
noise; whether defect(q) genuinely crosses zero in q in (0.9, 1] at row 91 is unresolved at
h=0.1 Richardson precision. Resolution lever: h=0.05 stencil or tighter SCF rung at that node
only. Until resolved this is residue under the ruling's zero-question standard.

## PROCESS NOTE: this item was executed before Item 1 by the pre-context-loss segment of s103
(ruling's Rule B line filed at open); resumed from cache after segment loss; cache-resume
discipline held, no work lost, no sealed file touched.
