# PREDICTION — T7c-CORR2: 4a repair (no Latter clamp on SIC channels; PZ-81) + GB exact constants (iii). Ruled s22. BEFORE run.
t7c_corr2.py = t7c_corr.py + env switches SIC_NOCLAMP=1 (Vtot = unclamped local + full unmasked SIC on SIC channels) and GB_EXACT=1
(B_U -0.046908, B_P -0.025725: Hoffman eps0^a + Onsager eps0^b, Loos-Gill Table I). Both off -> byte-identical behaviour to t7c_corr.
 PR1 Gate: H, one electron, half-occupied 1s, SIC on, corr None: eps -> -0.5000 within 2e-4 with NOCLAMP (was -0.533 clamped/masked; s21).
     With corr='P' and NOCLAMP: self-term removed to <= 2e-4 (was 0.0014, PX1 second clause).
 PR2 La 5d, NOCLAMP, corr None: sr_sic moves by |d| <= 0.004 vs banked -0.2202 (clamp step is small on a compact entrant).
 PR3 La 5d, GB_EXACT (clamp as banked): U shifts by +0.0008..+0.0014, P by +0.0009..+0.0015 (shallower), i.e. bracket narrows by ~0.
Fault F22.1 (registered before reading): Latter clamp applied to SIC-corrected channels (t7a_sic_all/t7a_sic_dec/t7c_sic/t7c_corr) -- double
asymptote; PZ-81 prescribes no clamp with SIC. Repaired in t7c_corr2 (switch). Banked SIC/GB rows stand as the clamped object until regenerated.