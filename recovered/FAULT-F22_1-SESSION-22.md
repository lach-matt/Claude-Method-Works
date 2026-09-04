F22.1 (s22, registered before any repaired result was read): the Latter clamp min(V,-q/r) is applied to the local potential of channels that also
carry a PZ orbital-SIC term (t7a_sic_all.py, t7a_sic_dec.py, t7c_sic.py, t7c_corr.py, and the s22 t7c_corr_all.py that reuses t7c_corr).
PZ-81 Sec. II: SIC supplies -1/r by construction; no tail is applied. Symptom: H 1s half-occupied exchange-SIC eps -0.533 not -0.500 (s21);
one-orbital correlation self-term removed to 0.0014 not 1e-4 (PX1 second clause). Repair: t7c_corr2.py SIC_NOCLAMP=1. Status: repaired in the
new object; banked rows NOT regenerated (needs a full pass, ruled open s22, budget-limited); ruling on regeneration order owed.