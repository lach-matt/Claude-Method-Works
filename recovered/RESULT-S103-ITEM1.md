# RESULT-S103-ITEM1 -- analytic rot_k law, row 58, four <=1e-10 shells. Prediction be23917c.
# Instrument pack103/w103a.py; receipt w103a-58.json. Scored vs SEALED w102b-58.json rot.

## SCORE:
P103.1  MISS 0/4 (value+sign). rot_AN vs rot_w102b:
        5s: -6.42e-6 vs +8.02e-5 (WRONG SIGN) | 5p: +1.82e-6 vs +1.86e-5 (10x deficit)
        5d: +1.34e-6 vs +1.81e-6 (26% low)    | 6s: +4.22e-6 vs +1.46e-4 (35x deficit)
P103.2  MISS (3/4). Dominant-partner sign holds at 5p/5d/6s, fails at 5s.
CAN-FAIL not run: with a 0/4 MISS the skew lever is uninformative (would MISS regardless);
        deferred to the repaired law.

## FAULT F103.1 (severity: PREDICTION -- law falsified as filed; instrument ran clean, no
## bookkeeping error found on read-back). The first-order claim
##   rot_k = (q_k/dq2) sum s_kk' [F(m)+F(p)]_{k'k}
## does NOT reproduce the sealed rot: deficits are 10-35x at s-channels and non-uniform
## (5d nearly reproduces at 26% low), so this is not a missing constant factor. The mechanism
## by which the rotation carries energy is NOT first-order overlap x Fock off-diagonal content
## evaluated at the endpoint hybrids.

## MECHANISM STATUS: OPEN. Named diagnostic (next lever, not run -- context):
##   D1: epsilon-linearity test -- [F(Pm + eps*Dr) - F(Pm)]/eps at eps in {1e-3, 1e-2, 0.1, 1}
##       inside the w102b F() machinery at 6s. If nonlinear in eps at eps->1, rot is
##       second-order (Hessian) dominated and the analytic law must be quadratic:
##       rot_k ~ (1/dq2)[<Dr|g> + 1/2<Dr|H_avg|Dr> asymmetry], with the Hessian difference
##       H(Pp)-H(Pm) = O(dq) supplying the missing magnitude. 5d's near-hit (smallest |s|,
##       most linear regime) is consistent with this hypothesis; the s-channel giants
##       (|s| ~ 2.4e-3, deficits 35x) are where quadratic content would dominate.
## Hypothesis filed as hypothesis, not result. No sealed file touched.
