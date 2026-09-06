# FINDING — Route P (object property of the local form?) on the six class rows.  s30. Files: PREDICTION-DROW-SESSION-30.md (adopted, ruling B),
# drow_p.py, drow_p.jsonl (six SCF pairs f=1/f=0 on the s28 sc path, SUBCELL=1, SIC_NOCLAMP=1). No constant; no re-derived DEc; F30.1/F30.2 on record.
## Table (Ha). DEc = DEc_frachf on every row (path reproduced). A = Δ total-density GB; B = Δ entrant PZ self-corr (subtracted, >0); R = Δ non-entrant self-corr.
row  DEc       A         B        R        | r_cut r_peak(p) Q_in  Q_mid | excess   g=excess/Q_mid  B/excess
Sc  -0.026011 -0.030770 +0.011046 -0.006287 | 4.05  0.972(3p) 0.979 0.752 | 0.00140  0.00186   7.9
Y   -0.020192 -0.022304 +0.006098 -0.003986 | 4.23  1.246(4p) 0.922 0.819 | 0.01019  0.01244   0.60
La  -0.018297 -0.019729 +0.004420 -0.002988 | 4.42  1.584(5p) 0.901 0.800 | 0.00716  0.00895   0.62
Lu  -0.019484 -0.020809 +0.005246 -0.003920 | 4.20  1.203(5p) 0.885 0.816 | 0.00831  0.01019   0.63
Cs  -0.002430 -0.001941 +0.000010 -0.000500 | 3.77  1.775(5p) 0.128 0.104 | -0.00043 —         —
Gd  -0.017207 -0.018606 +0.005167 -0.003769 | 4.30  1.363(5p) 0.906 0.818 | 0.02184  0.02669   0.24  (4f-adjacent; set aside)
## Predictions scored
PP0 HELD: A+B+R-DEc = 0 to 1e-7 on all six; DEc == frachf DEc_sc to 1e-6.
PP1 HELD on sign (B>0 all six) and on Cs (B 1e-5 < 0.001); magnitude window [0.003,0.010] HELD on Y La Lu Gd, FAILED on Sc by margin (0.0110): the
    compact 3d self-density gives the largest B — the direction predicted in PP2, overshooting the window by 10 %. Chosen threshold, stated.
PP2 HELD: B(Sc)/B(Y) = 1.81 >= 0.7. B does NOT track the excess (excess Sc/Y = 0.14). P1's condition fails on shape. Reading (no fit): on the three
    n>=4 d rows B/excess is 0.60-0.63, flat; on Sc it is 7.9. B is proportional to the excess where the excess exists and dominates it where it does not.
PP3 FAILED on every d row: |R| 0.003-0.006 (Sc 0.0063, Y 0.0040, La 0.0030, Lu 0.0039, Gd 0.0038); Cs 0.0005 HELD. Mechanism: R is the ns2 (and
    inner) self-correlation change on ionisation — the outer s pair contracts when the d electron leaves and its own PZ term moves. R ~ -0.65 B on
    every d row (Sc 0.57, Y 0.65, La 0.68, Lu 0.75, Gd 0.73): the entrant's own SIC change is partly cancelled by the shells that relax against it.
    Consequence: A and B may not be quoted against the excess without R; the frozen picture is 35 % wrong on the SIC side. Reported, not repaired.
PP4 HELD: Q_mid in [0.6,0.9] on all four (0.75-0.82); g(Sc) = 0.15 g(Y) < 0.4. P2 FAILS as a single number: g is 0.0090-0.0124 on Y La Lu (±16 %
    about 0.0105) and 0.0019 on Sc. Not geometric across the four; flat across the three n>=4 rows. -> Route N decides.
## Statement
Route P does not say "domain of the form": the excess is not the entrant's self-correlation term (wrong shape, PP2), and is not a geometric ratio (PP4).
Two structural readings carried, unfitted: (i) B/excess ~ 0.6 and g ~ 0.0105 are each flat on Y La Lu and each fail on Sc — the excess is a property of the
n>=4 d rows as a class, absent at 3d, which is the shape a core-valence (n s2p6 against nd) term would have; (ii) R ~ -0.65 B: relaxation of the outer
s pair is not negligible on the sc path (PP3 failed) and any object-property claim must carry it. Foreign drow_p.jsonl NOT admitted (differs on Q_mid by F30.2;
SCF columns identical on all five rows). Failed predictions this item: PP1 (Sc, window), PP3 (d rows). Timing flag: F30.2 (definition repair after Sc read).
Gate for HANDOFF-30: python3 drow_p.py 21 39 57 71 55 64 -> must SKIP all six; if a row is deleted it reprints (Sc A -0.03077 B 0.011046 R -0.006287).