# RESULT S89 UNIT 1a — L3 AT THE PAIR. 12 rows (38-41, 55-57, 88-92), width-4 frontier, both wells.
Prediction 585e6d93...f875 hashed before chain89.py existed. Can-fail gate PASS after F89.1.
Sealed J reproduced at every previously sealed channel (4d 2.2337/2.2731/2.0763; 5d 1.0358|1.8605,
2.4407, 1.9850; 6d 2.0201, 1.9062; 5f 2.1018, 2.0456) to 4 dp. No new number at Z=90 travels.

## Scoring
P1  LEVER LIVE: region count {1,2} seen; the 2 comes from Z=55 (5d, 6d, 4f all two-well) -> Z=56
    one-well. 38-41 all one-well as filed. The 88-92 half of P1 is UNTESTED: 5f is outside the
    width-4 frontier at Z=88, 89 (not in the top four by nu). Part-pass, part-untested.
P2  S7 rule agrees 11/12; the single disagreement is Z=56, the row named in the filing.
    F89.2: the filing said "12 of 13" — the row count is 12, a miscount in the prediction file.
    The named-exception clause holds exactly; the count clause was ill-formed.
P3  HELD: no two-well channel has J_outer >= 2. J >= 2 appears only after the merge.
P4  HELD 12/12 — but see the timing flag below; the filed "unless J1 < 1.3" clause decided ONE
    row (Z=56) and is a one-point clause. Informative fraction 1/12.
P5  Z=90, 91 reproduced; Z=92 5f J = 1.9981 < 2.0456 HELD and CROSSES BACK UNDER 2.
    Z=88, 89 5f not testable at width 4.

## The finding (L3 at the pair)
1. THE MERGE DOES NOT FIX THE SIGN. Two merge rows place the merged J>=2 candidate at rank 2:
   Z=56 (5d 2.441, banked +) and Z=90 (5f 2.102, banked -). Same configuration, opposite sign.
   The note's hypothesis is FALSIFIED as a sufficient condition.
2. What differs is the RANK-1 channel: Z=56 rank-1 is 6s (J=1.191, dg/dl=+0.81, the s-anchor);
   Z=90 rank-1 is 6d (J=1.906, dg/dl=+0.094). The sign of the PAIR is carried by both.
3. **TIMING FLAG (R 1449).** After reading the table I noticed that s84's own magnitude
   estimator — the trapezoid Delta g ~ Delta l * (dg/dl_1 + dg/dl_2)/2, which gave the
   "-0.004 at Z=90" recorded in s84 §S7 — also gives the SIGN at all 12 rows here, including
   Z=56 (+0.18) and Z=90 (-0.004), with no ad hoc clause. This is the mean-value form of L2:
   Delta g = integral of dg/dl over l between the two candidates. It was NOT filed as the
   sign rule before the run. It is recorded as an observation and goes to a widening test
   with its own hashed prediction (Unit 1a-w) before it may enter the chain.
4. Post-merge J >= 2 is a TRANSIENT of 1-3 rows in every block: 4d Z=38-40 (3 rows; 41 = 1.957),
   5d Z=56 only (57 = 1.985), 6d Z=88-89 (90 = 1.906), 5f Z=90-91 (92 = 1.998). The five open
   rows of L3 are exactly the rows inside these transients where the channel is at the frontier.

## Status of L3 after Unit 1a
One-channel L3 (J<2) stays OPEN at the five rows; it cannot close (s88 T1). The two-channel
statement has a candidate closed form (the trapezoid of L2) that is 12/12 here but post hoc.
Pending Unit 1a-w. If it widens, L3 at the pair is: sign(Delta g) = sign(mean dg/dl over the
pair) with each dg/dl = 2 - J from L2, and the five rows close as PAIR statements.