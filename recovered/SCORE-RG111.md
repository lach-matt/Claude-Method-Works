# SCORE — PREDICTION-RG111. Session 73. R 1971.
# Prediction sha256 20ffe3c7c776a5773339d40767a1ee17232291e6e75589e673c77ff720d23c1a,
# filed and hashed BEFORE rg.py existed. Instrument pack73/rg.py · rows pack73/rg111.json.
# Z=111 IS BEYOND THE SEAL. OUTPUT ONLY. NO SCORE. NO DENOMINATOR. Not entered in any gate.

## RG-1  CALIBRATION — **FAILED**
    Cu 29   E(d10s1) - E(d9s2) =   +2.23 mHa   lower = d9 s2    *** WRONG SIDE ***
    Ag 47   E(d10s1) - E(d9s2) = -142.00 mHa   lower = d10 s1   agrees
    Au 79   E(d10s1) - E(d9s2) =  -68.73 mHa   lower = d10 s1   agrees
The clause required all three. **Two of three is a FAIL, not a pass with a caveat.**
The margin at Cu is 2.23 mHa against total energies of order 1.6e3 Ha. It is still the
wrong side of zero, and the question asked is an ORDERING question, where sign is the
whole answer.

## RG-2  LEVER — **PASSED**
c moved the Z=111 gap by 300.67 mHa. The lever is alive and was demonstrated by direct
measurement, not by source-tracing. F54.2 standing law satisfied.

## RG-3 and RG-4 — **NOT SCORED. WITHHELD BY THE PREDICTION'S OWN CLAUSE.**
RG-1 as filed reads: "IF RG-1 FAILS AT ANY ROW, RG-3 AND RG-4 ARE UNINTERPRETABLE AND WILL
NOT BE SCORED. An instrument wrong at every case that can be checked carries no weight at
the case that cannot. This clause exists so that outcome cannot be talked around afterwards."
It failed. The clause binds.

**THE NUMBERS ARE RECORDED, UNSCORED, AND MUST NOT BE CITED AS A RESULT:**
    Z=111  c = 137.035999   E(d10s1) - E(d9s2) =   +71.38 mHa   lower = d9 s2
    Z=111  c = 1e6          E(d10s1) - E(d9s2) =  -229.30 mHa   lower = d10 s1
**THEY POINT EXACTLY WHERE THE PREDICTION GUESSED THEY WOULD.** That is precisely why the
calibration clause was written before they were read. A result that arrives in the shape you
hoped for, from an instrument that just failed its calibration, is not a result. It is
recorded here so that it cannot be quietly rediscovered later as though it had been earned.
**NO CLAIM IS MADE that relativity breaks the group-11 pattern at Rg.** The question stays
open. Re-running it requires an instrument that first passes RG-1 at all three rows.

## NO BULK CLAIM WAS MADE AND NONE IS MADE NOW
Per the prediction: there is no lattice, no band structure and no conductivity operator in
this project. Nothing about Rg's conductivity follows from anything computed here.

## WHAT THE FAILURE IS WORTH — IT IS NOT A WASTED RUN
1. **Cu is independently confirmed as the hardest row in group 11, by a SECOND route.**
   s73 already showed configuration mixing at Cu is EXACTLY ZERO by the 2S/2D selection rule,
   so the 2x2 cannot repair it. Now the term-corrected AOC comparison also fails at Cu, and
   ONLY at Cu, while getting Ag and Au right. **Two independent instruments, two independent
   failures, same row.** Cu 29 is the sharp case of the configuration column.
2. **The 2.23 mHa Cu gap matches the s73 CI table exactly**, where E_B - E_A at Cu was
   -2.23 mHa. The two instruments are consistent with each other while both being wrong.
3. **The seal boundary is enforced by the runtime, not only by ruling.** ground_occ() is a
   TABLE and raises KeyError at Z=111. Registered as an observation, not a fault: the
   derivation's Z=2..108 boundary is physically present in the code.

## TIMING
Prediction hashed before rg.py existed. RG-1 was written as a blocking clause before any
energy was read. No clause was altered after any number was seen.