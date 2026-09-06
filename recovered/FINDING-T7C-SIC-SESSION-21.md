# FINDING — T7c-SIC: PZ-SIC on the SR spin-polarised TS object, 5d rows + Y/Sc controls (session 21). Files: t7c_sic.py (t7a_sic_dec
verbatim + numerov_wf_sr kernel swap), t7c_sic_run.py, t7c_sic.jsonl, RUN-T7C-SIC-SESSION-21.txt, PREDICTION-T7C-SIC-SESSION-21.md.
Gates exact: c=1e6 mode=all Fe -0.3854 (t7a_all); c=C0 mode=none La -0.2079 (t7c_pol). Fault F21.2 (build): loop variable `c` shadowed
the light-speed argument in the kernel-swapped copy -> TypeError before any number was read; renamed `cl`. Registered here; closed.
## Result
PC1  HELD: SIC shift under SR equals nonrel within 0.0015 on every row (La 0.0000, Gd 0.0009, Lu 0.0015, Y 0.0001, Sc 0.0002).
     SIC is a property of the entrant's own density and commutes with SR to the object's precision. Direct/indirect split unchanged.
PC2  HELD: on ONE object chain (SR-pol TS -> +SIC -> +SO 5d3/2 with banked zeta), the 5d edge is +0.0138 / +0.0141 / +0.0112 Ha
     (La/Gd/Lu) shallow vs measured, spread 0.003 -- FLAT.
## Standing after (C): the 5d residual is now stated once, on one object, with every derivable term in the exchange / self-interaction /
relativistic sector applied and its magnitude on record: SR (+0.027 indirect, s20), Hund/pol (banked), SIC (-0.011..-0.012, direct only),
SO (-0.005..-0.008). What remains is +0.011..+0.014 Ha, flat La -> Lu, ~5-7 % of the 5d removal energy. Nonrel exact exchange moved
5d by <= 0.005 (s20 (i)); SR-HF is predicted (s20) not to. Y 4d carries the same +0.013 after SIC (nonrel).
The remaining term has NO candidate inside the one-electron local/exact-exchange object class. Interpretation offered for M's ruling (D),
not claimed: it is the correlation contribution to the entrant removal energy, which this object class does not contain by construction.
Faults: F21.2 (build, closed). Predictions failed: none. No constant, no measured input; c = 137.035999; measured 5d rows comparison only.