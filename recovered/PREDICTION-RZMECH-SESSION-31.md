# PREDICTION — are R and Z two parts of one mechanism, triggered per subshell? (M, s31)  Written before the run.
Structure known before any number: Z is R's small-r_s limit (gate: r_s 0.001 R -0.26164 Z -0.26161); both carry the SAME bare E0B. So R = Z + D_ring(r_s,zeta),
D_ring = the resummed ring beyond the leading log + eps0a. They are one UEG object evaluated to two orders, not two objects. What differs per row is the
r_s WINDOW the entrant density samples. Two questions, three predictions:
PM1 (r_s map): the class-resolved R/Z ratio (3d 1.18, 4f 1.16, nd>=4 1.41, 6s 2.32) is a monotone function of the entrant's correlation-weighted <r_s>
    (weight n eps_c^Z over the shell): the four classes order 3d ~ 4f < nd>=4 < 6s in <r_s>_w with no crossing. Bound: <r_s>_w 3d/4f < 1.5, nd>=4 1.5-3, 6s > 3.
PM2 (defect map, both forms against the benchmark UEG at zeta=0 and 1, RECALLED Ceperley-Alder/PW92 values, NOT ENTERED): at r_s <= 1 both within 10 % of
    the benchmark with Z UNDER (less negative) and R OVER; the sign of (form - exact) is fixed for each form over r_s in [0.5, 10] (Z always under, R always over)
    -> the exact local ε_c lies BETWEEN Z and R at every r_s: the two forms bracket the same one object from opposite sides everywhere, and the missing part
    of BOTH is the same diagram class (exchange beyond second order, screened), whose r_s-dependence sets the per-subshell trigger.
PM3 (mechanism test on the rows): if the object is one local ε_c, then (R - exact) weighted by each row's entrant density predicts the R-side excess ordering
    Sc < La < Lu ~ Y; FINDING-RING says an exact local form would NOT remove the nd>=4 object. Prediction: PM3's local estimate of the nd>=4 excess is
    <= 0.002 (i.e. the ~0.004-0.005 object stays non-local); if it reaches 0.004 the s30 statement is falsified and the d-row object IS the RPA overbinding.
Numerics: corr_ring.eps_R and t7c_cuaudit chain form on r_s grid; entrant radial densities from the standing SIC/corr SCF (scf_sic_corr.last) per row; no scans, no constant.