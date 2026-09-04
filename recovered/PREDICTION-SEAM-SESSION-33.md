# PREDICTION-SEAM (s33) — M: open candidates (iv) the eigenvalue/observable seam (R 1578) and (v) the frachf-path convention, run against (a). Written before the read.
Criteria c1-c3 as PREDICTION-CAND. Both candidates are read FROM RECORD (frachf.jsonl s28-29 five-point path: DEc_sc endpoint, Delta_c_sc_mid TS-midpoint, gap_sc,
janak_gap_corr, eps_mid_corr, D_HF; t7c_corrS.jsonl EF; frachf_ring.py meas/so). TIMING FLAG F33.2: EF(S), meas and so were already in this session's context when
these predictions were written (the seam's rough size on Y was visible); the frachf.jsonl fields were not read beyond Y's first row.
Objects. Target T = meas + so (chain IE the row must deliver). Path O (observable, frachf): IE_O = -(D_HF + DEc), resid_O = T - IE_O (+ = short). Path E (eigenvalue,
local-exchange TS): IE_E = -EF_S, resid_E = T - IE_E. Seam_iv = IE_E - IE_O. Convention gap (v): g_v = Delta_c_sc_mid - DEc_sc (midpoint minus endpoint, on the sc path).
Janak seam on the O path itself: janak_gap_corr = D_tot - Simpson∫eps (should be small); TS-vs-integral seam: eps_mid_corr - D_tot_corr.
  P-iv-1: seam_iv is NOT small — 0.005-0.015 on nd rows and larger on Sc — and of one sign (E deeper than O). P-iv-2: the object (resid_O) does not equal the seam or half
  the seam row by row (|resid_O - seam_iv/2| > 0.002 on at least two nd rows) -> the seam is a second object, not the home; the object lives on the O side by R 1578.
  P-iv-3: janak_gap_corr <= 0.001 on all rows (the O path is internally Janak-consistent) — the O path's own eigenvalue/observable seam cannot hold 0.005.
  P-v-1: g_v is of ONE sign on all class rows and scales with |DEc| (Sc largest, Cs smallest), 0.002-0.008 -> fails c2/c3 -> (v) refused; if instead g_v is nd-only ~0.005 with
  Sc <= 0.002, (v) wins. P-v-2: |g_v| on Y/La/Lu within 0.003 of each other.
Decision rule: (a) survives unless a candidate meets c1-c3. Tool: seam_table.py (record only, no SCF).