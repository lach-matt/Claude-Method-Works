# TRACE-S104-R1 -- the signed orientation trace. Closes Item 1 / G5b as DERIVED.
# Paper algebra on the S104 Derivation-1 identity; verified by receipt arithmetic only
# (w104c-58.json; no solve). Rulings granted at S104 ("Continue").

## THE TRACE (three lines, as owed):
Let M[u,v] = <P_u|(T_v - Z/r)|P_v> with T_v from v's own eigen-relation, and let
asym(u,v) := M[u,v] - M[v,u]  (orientation: T-on-v minus T-on-u).
(1) The instrument's quadratic form uses M_sym = (M + M^T)/2, so the one-body content of
    F(P_endpoint +- Dr) carries the cross element M_sym[endpoint, partner]
    = M[partner-oriented] + (1/2) asym(endpoint, partner).
(2) The filed law evaluated its one-body element with T on the ENDPOINT (the <=1e-10 gate),
    i.e., the M[partner-oriented] term alone... with the orientation convention fixed:
    law element = T-on-endpoint; instrument element = symmetrized. Their difference is
    (1/2) asym per endpoint, oriented (T-on-partner - T-on-endpoint).
(3) Occupancy q_k multiplies the one-body functional term, and the two endpoints average:

    T1 - law  =  (q_k s_k / dq2) * [asym_m + asym_p] / 2,   asym = (T-on-partner) - (T-on-endpoint)

## VERIFICATION (receipt arithmetic, w104c-58.json):
  6s: measured +3.188398e-6, trace +3.188373e-6  (ratio 0.999992)
  5s: measured +3.185439e-6, trace +3.185766e-6  (ratio 1.000103)
Residuals 2.5e-11 / 3.3e-10 are the two-body-part orientation content, three orders below the
object. The sign at 5s resolves correctly: s < 0 and trace-asym < 0 compose to +.

## G5b -- CLOSED AS DERIVED. The complete decomposition of the one-shell rotation, every term
## a closed-form object of the sealed operators, no unexplained numeric content:
##   rot = [linear law] + (q s / dq2)<asym> + [endpoint-Hessian difference, exact quartic]
##         + [O(|Dr|^3), exact quartic]
##   with asym = (Deps)S - <u|DVloc|v> + DX   (Derivation 1, machine-exact 4/4)
## and the core-M content REMOVED by projection and RECLASSIFIED (F102.3 ruling) as the same
## identity at core Deps scale.

## R2 STATEMENT (perp_k, for the order file -- statement only, no evaluation):
## perp_k is the first-order perturbed-HF orbital response confined to the orthogonal
## complement of the occupied same-l space: with Q = 1 - sum_occ |P><P|,
##   |dP_k> = Q (F_k - eps_k)^{-1} Q (dV_k/dq) |P_k>   (Gerratt-Mills 1968 form, radial gauge)
## and perp_k = the chord content along |dP_k> -- one evaluation of a stated formula, executable
## only on ruling.
