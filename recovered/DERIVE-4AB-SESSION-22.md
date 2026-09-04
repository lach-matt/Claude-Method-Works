# 4a / 4b — session 22 (bridge-21 s3(4a) "what does the established math say"; (4b) "derive or drop"). No run for 4a; 4b from banked data only.
## 4a  Tail-clamp asymmetry in orbital SIC (F21 gate: H 1s half-occupied SIC left 0.0014, not 1e-4; banked exchange SIC H 1s half -0.533).
ESTABLISHED MATH: Perdew & Zunger PRB 23, 5048 (1981) Sec. II: the orbital-SIC potential v_i = v_eff - u[n_i] - v_xc[n_i,0] is asymptotically -1/r
for the outermost orbital of a NEUTRAL atom BY CONSTRUCTION (the Hartree self-term supplies the -1/r); PZ therefore apply NO Latter tail -- SIC
is the replacement for it (Fermi-Amaldi 1934 is the same statement one level cruder). Latter (1955) is a fix for a local potential that lacks SIC.
Applying both -- clamping min(V, -q/r) to a potential that already goes as -1/r through its SIC term -- double-counts the asymptote wherever
the clamp engages before the SIC potential has reached -1/r; on a one-electron system PZ-SIC is EXACT (H: eps = -0.5 exactly, any occupation),
so the residual 0.0014 (H 1s half) is the clamp's step, and the exchange-only value -0.533 (0.033 too deep) is the same double count on the
un-corrected exchange asymptote. THE ESTABLISHED PRESCRIPTION: on the SIC-corrected channel, drop the Latter clamp (qtail = 0); keep the clamp
only on channels that carry no SIC. Gate for the repair: H 1s at any occupation -> -0.5000 to 1e-4 with corr and exchange SIC.
CONSEQUENCE IF REPAIRED: every SIC/GB row (t7a_all, t7a_dec, t7c_sic, t7c_corr, t7c_corr_all) is regenerated; magnitude of change bounded by the
tail-mask step (order 0.001-0.003 on d/f, larger on s). This is a REPAIR (fault to register: F22.x, "clamp applied to a SIC channel"), not a
convention -- because the two fixes have a shared owner and the owner applies one. Needs M's ruling to open (it moves banked rows).
## 4b  "TS(-1/r) == dSCF(untailed)" on localised entrants -- DERIVE OR DROP.
Derived (from Janak + Taylor, checked on all 15 banked untailed rows, DERIVE-4B-KAPPA-SESSION-22.txt):
   kappa := eps(1/2) - int_0^1 eps dq = -eps''(1/2)/24 + O(eps'''')/1920, i.e. kappa = -(1/24) d^3E/dq^3 at half occupation.
   Holds to 1 % on every d/f row (3d 0.0058-0.0070, 4d 0.0037, 5d 0.0024-0.0037, 4f 0.0056-0.0057); on Cs 6s both sides are ~0 (0.0002).
   So the exact untailed dSCF is eps_ut(1/2) + eps''/24: the TS step's whole error is one-24th of the third derivative of the functional.
The observed identity eps_tailed(1/2) ~= dSCF_ut requires  T := <phi_1/2 | min(V,-1/r) - V | phi_1/2>  = -kappa = eps''/24.
   T is a FIRST-ORDER expectation of the tail region (weight of the half-electron beyond the Latter crossing); kappa is a THIRD-ORDER
   occupation derivative of the total energy. No relation between them follows from the functional; and the s row is the counter-example:
   Cs T = -0.014, kappa = 0.000. On d/f the two are both ~0.005 because both are small self-interaction remainders of a compact half-electron --
   a numerical coincidence bounded to localised entrants, NOT an identity.
RESULT: DROPPED as a law; kept as an OBSERVATION with the derived form of kappa (which is new and stands: kappa = -eps''/24) and the named
counter-example. Bridge-21 s2(2) "offered not claimed" -> now "not a claim". No constant, no measured input, no run.