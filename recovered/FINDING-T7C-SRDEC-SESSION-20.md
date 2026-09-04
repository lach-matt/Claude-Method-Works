# FINDING — T7C SR DECOMPOSITION (candidate (b) of bridge-19 s6) — session 20, 2026-08-16
(b1) BOUND FROM BANKED ROWS (t7b.jsonl), no run: TS-dSCF split on the 5d TS row is nonrel -0.0193/-0.0218/-0.0250 (La/Gd/Lu), SR -0.0201/-0.0234/-0.0298,
     HF +0.0022/+0.0027/+0.0033. The split is a property of the LOCAL-EXCHANGE object (absent under exact exchange), present nonrel; SR adds only
     -0.0008/-0.0016/-0.0048. PB1 HELD: the split does not enter at the SR step; it cannot be the missing relaxation of the edge (+0.026/+0.025/+0.022).
(b2) DECOMPOSITION (t7c_srdec.py: c chosen per orbital inside scf_pol_sr; gate mode all == banked -0.2079 La). Shift of E_5d vs nonrel pol TS:
       La: all +0.0266 | 5d-only -0.0083 | not5d +0.0335 | 6s-only +0.0172 | core-only(no 6s,no 5d) +0.0174   (6s+core = +0.0346 ~ not5d: additive)
       Lu: all +0.0398 | 5d-only -0.0159 | not5d +0.0512 | 6s-only +0.0333
     PB2: sign of the direct term HELD (negative); its magnitude FAILED the <0.005 clause (0.008 La, 0.016 Lu). Indirect > 0.020 HELD (0.0335 La = 126 % of
     the total; the direct term partly cancels it).
STANDING: the SR destabilisation of 5d in this kernel is ENTIRELY INDIRECT — the contracted 6s and the contracted 5s5p/core each supply about half at La;
at Lu the 6s share is 0.033 of 0.051. The measured 5d removal energy sits within 0.004 (La) of the NONREL pol TS: the edge is the size of the net SR shift.
So the question for (a) is sharpened: does relativistic exchange (MacDonald-Vosko) reduce the core/6s contraction enough to take ~0.02-0.025 off the indirect
term without moving the 4f/Ra II gates? Prediction for (a) is owed before it runs. Faults: none. Gates: none moved.