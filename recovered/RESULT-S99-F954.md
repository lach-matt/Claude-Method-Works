# RESULT S99 -- ITEM 3 (F95.4 locus test; prediction ea56c5e9, hashed before build). Non-gating hygiene. No sealed file touched.
## SEVERITY LINE: VALUE-EXACT diagnostic; F95.4 remains OPEN, candidate field NARROWED by comparison.
Probe pack99/f954probe.py (v5a build verbatim, row-89 core, l=0/7s):
- Grid check: max|dr/(r*h)-1| = 0 exactly -> the h quadrature weight is EXACT on the sealed log grid. QUADRATURE HYPOTHESIS RETIRED.
- sym (filed): dE +1.835e-4, rel 1.104e-3 (PR1 HELD, reproduces the s96 order).
- unsym (sqrt(M_i/M_j) restored, general eig): dE +1.781e-4, rel 1.071e-3 -- 3% effect. M-SYMMETRISATION HYPOTHESIS RETIRED (PR2 falsified, F99.6).
## STANDING HYPOTHESIS (not tested, declared): the residual is the discretisation mismatch between the sealed shooting kernel (libshoot Numerov integration) and the dense Numerov matrix (f^{-1}D2 with boundary truncation) -- two representations of the same operator at the same h. Test would be h-refinement scaling of the dense eigenvalue toward the sealed eps; not run this session (non-gating, cost > remaining-budget priority).
## F95.4: OPEN. s96 candidate locus sentence SUPERSEDED (both named candidates retired by measurement).