# PREDICTION S97 -- core-core term at row 89, non-perturbative closure (written before any arithmetic)
Bound-direction: VALUE (estimate); sign-exact claims PR2, PR3.
PR1 Consistency can-fail (external to v5: uses the CORE object's own 6p-7s pair as reference, no 6d anywhere in core):
    |ent(61-70)/core(61-70) - 1| < 0.15 under (1-f) [PASS expected]; > 0.30 under exclusion [FAIL expected]. Decides the slot rule.
PR2 Two-state resummation of the ent 7s^2 -> 6d^2 block (E_PT = ent_own - ent_excl for 70-70; Delta = |2eps7s - 2eps6d| ~ 0.47 filed):
    E_exact = -(Delta/2)(sqrt(1+4|E_PT|/Delta) - 1). |E_exact| < |E_PT| (sign-exact, convexity) and the ratio lies in [0.85, 0.95].
PR3 Core-core differential (v5e, rows 89): dcc = [E2w_run - E2w_core] - [E2w_ent - E2w_core] over core pairs, after replacing the ent 70-70 own-slot piece by E_exact: dcc stays POSITIVE (margin widens), and the change from the PT value (+0.066 filed) is < 0.01 Ha.
PR4 Total dm2(89) including core-core (resummed) lies in [+0.08, +0.12] Ha; no flip (margin 0.03233).