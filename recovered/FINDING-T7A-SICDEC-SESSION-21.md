# FINDING — T7a-SICDEC: the SIC shift is DIRECT(shell,Z) + beta_shell * N_sib (session 21). Files: t7a_sic_dec.py (banked scf_sic_orb
verbatim + mode switch), t7a_sicdec_run.py, t7a_dec.jsonl, RUN-T7A-SICDEC-SESSION-21.txt, PREDICTION-T7A-SICDEC-SESSION-21.md.
Gate: mode=all reproduces t7a_all ts_sic, mode=none reproduces ts_pol (Fe -0.3854/-0.378) exactly.
## Decomposition (direct = e(entrant-only SIC) - e(none); indirect = e(all) - e(entrant-only)); N_sib = shell electrons besides the entrant
Cs 6s  0  -0.0049 -0.0001 · Sc 3d 0 -0.0281 +0.0024 · Ti 1 -0.0309 +0.0089 · Cr 4 -0.0311 +0.0309 · Fe 5 -0.0369 +0.0295 · Ni 7 -0.0427
+0.0415 · Cu 9 -0.0415 +0.0649 · Y 4d 0 -0.0159 +0.0007 · La/Gd/Lu 5d 0 -0.0119/-0.0143/-0.0159 -0.0004/+0.0029/+0.0038 ·
Dy/Er/Tm/Yb 4f 9/11/12/13 -0.0498/-0.0529/-0.0544/-0.0559 +0.0402/+0.0489/+0.0532/+0.0575.
## Score
PB1  HELD: direct deepening on every row, compactness-ordered 4f (0.050-0.056) > 3d (0.028-0.043) > 4d/5d (0.012-0.016) > 6s (0.005),
     and monotone in Z within a shell (self-interaction of an orbital that contracts with Z).
PB2  HELD: indirect ~0 with no shell siblings (Cs, Sc, Y, La, Gd, Lu: |ind| <= 0.004, from core/6s SIC only), largest at Cu (+0.065) and
     Yb (+0.058). AND STRONGER THAN PREDICTED: indirect / N_sib is a SHELL CONSTANT -- 4f 0.0045/0.0044/0.0044/0.0044 (four rows to
     1e-4), 3d 0.006-0.009 (mean 0.007). Not fitted: read off the run.
PB3  HELD: 5d indirect <= 0.004; the 5d SIC shift is the entrant's own half-electron self-term, -0.012 to -0.016, La < Gd < Lu.
## Law (derived structure, no constant chosen): shift_SIC = direct(nl; Z) + beta_nl * N_sib, where direct = <-(v_H + v_x)[n_ent/2]>
relaxed, and beta_nl is the per-sibling destabilisation from each sibling's own V_SIC contracting it onto the entrant. Both terms are
computable from the object with no input; beta_4f = 0.0044 Ha/sibling and beta_3d ~ 0.007 are OUTPUTS, to be checked against a
frozen-orbital estimate (candidate, not done). This explains every sign change in FINDING-T7A-SIC-ALL: the shift crosses zero where
N_sib = |direct|/beta (3d ~ 5-6, 4f ~ 12-13), i.e. at Cr/Fe and Tm/Yb -- which is where the s17 rows sat, which is why s17 read SIC as
"no leverage".
## Bearing on the SHELL finding: SIC's contribution on 5d is DIRECT ONLY, -0.012..-0.016, growing La -> Lu. Residual after SIC on
the pol object: La/Gd/Lu +0.014/+0.014/+0.010 (bridge-20 shallowness + shift), Y +0.013. Nonrel HF moved 5d by <= 0.005 (bridge-20 (i))
and SR-HF is predicted (FINDING-T7C-SHELL) not to move it. Interpretation offered, not claimed: the remaining ~0.01-0.014 Ha flat on
5d/4d after exchange, self-interaction, SR and SO are exhausted is CORRELATION, which a one-electron TFD/HFS object does not contain,
and every LDA correlation functional carries fitted constants (excluded by the derivability rule). This is a bound on the object
class, for M's ruling, not a result.
Faults: none. Predictions failed: none (PB2 stronger than stated). No constant, no measured input.