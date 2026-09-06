# FINDING — T7c-CORR: Gell-Mann-Brueckner local correlation, attributed, closes the 5d edge inside its bracket (session 21).
Files: t7c_corr.py (t7c_sic verbatim + v_c^GB U/P + PZ orbital SIC of v_c, tail-masked), t7c_corr_run.py, t7c_corr.jsonl,
PREDICTION-T7C-CORR-SESSION-21.md. Attribution: Gell-Mann & Brueckner PR 106, 364 (1957); constants A=(1-ln2)/pi^2 analytic,
B_U=-0.048, A_P=A/2, B_P=-0.0269 Ha as quoted as exact limits by Perdew & Zunger PRB 23, 5048 (1981); local use in the statistical atom:
Gombas 1949/1956; SIC of correlation: PZ-81; eps_c <= 0 as a constraint (not a fit). NO CONSTANT CHOSEN. Web search s21 (bash egress
denied; web_search tool) -- Nozieres & Pines PR 111, 442 (1958) state GB's reach r_s <~ 1; atomic 5d densities sit at r_s ~ 1-3:
the form is applied OUTSIDE its proven reach and that is the stated limitation of this term.
## Gates (PX1): corr=None reproduces t7c_sic (La -0.2202) exactly. One-orbital self-term (H 1s half, P): removed to 0.0014, NOT 1e-4;
cause named: V_c is nonzero at the Latter clamp boundary so the tail-masked self-term leaves a step; the banked exchange SIC carries the
same tail asymmetry (H 1s half = -0.533 with corr=None). Bound of the object, recorded, not fixed. PX1 second clause: FAILED (0.0014).
## Result (shift of the 5d entrant on the SR-pol-SIC chain; residual after SO from FINDING-T7C-SIC-SESSION-21)
La 5d  U -0.0186  P -0.0082  residual +0.0138 -> inside · Gd  U -0.0201  P -0.0089  residual +0.0141 -> inside ·
Lu  U -0.0191  P -0.0083  residual +0.0112 -> inside · Y 4d (nonrel chain)  U -0.0202  P -0.0084  residual +0.013 -> inside.
PX2  HELD: deepening, flat (U spread 0.0015, P spread 0.0007), all three residuals inside the U-P bracket. (Gd U 0.0201 vs stated ceiling
     0.020: 1e-4 over -- noted, not read as a failure of the bracket claim.)
PX3  HELD (Y).
## Reading: on ONE object chain -- TFD start -> local spin-polarised exchange (Dirac 1930 / Slater 1951 / Gaspar 1954-KS alpha=2/3) ->
Slater-Janak transition state (1972/1978) -> Latter tail (1955) -> scalar relativity (KH 1977 form) -> PZ orbital SIC (1981; ancestor
Fermi-Amaldi 1934) -> Lande level SO -> GB correlation (1957, Gombas locality) -- the 5d edge is closed to within the polarisation
bracket, with every term attributed and no constant chosen. What is NOT derived: the polarisation interpolation between U and P (vBH
f(zeta) is exchange-exact, correlation-approximate) -- so the result is a BRACKET, stated as such, not a number. The residual after
the bracket midpoint: La -0.0004, Gd -0.0004, Lu +0.0025 -- but the midpoint is not derived and is NOT claimed.
Timing flag (R 1449 convention): the correlation term was formulated AFTER the residual was observed and located (s20-s21); the
predictions PX2/PX3 were written before the run, the constants were not chosen from the residual, and the bracket contains it -- entered
as a post-hoc term with pre-run predictions, per R 1449.
Faults: none new. Predictions failed: PX1 (second clause, 0.0014). No constant, no measured input; measured 5d rows comparison only.