# PREDICTION S91 ITEM 1 -- THE COLLAPSE-SWING SIZE, DECOMPOSED. Filed before any solve.
Object. D(c;Z) = E[Z; cfg(Z-1)+c] - E[Z; cfg(Z-1)]  (sealed chain instrument, nlchain.step).
Control. D_fr(c;Z*) = E[Z*; cfg(Z*-2)+c] - E[Z*; cfg(Z*-2)]  -- entrant shell held at Z*-1 occupancy.
Identity (exact, by construction):  swing := D(Z*) - D(Z*-1) = P + S
   P := D_fr(Z*) - D(Z*-1)   one proton, core fixed      S := D(Z*) - D_fr(Z*)   entrant electron's screening
Rows: (37,38) 4d,5s | (55,56) 5d,6s | (57,58) 4f,5d | (89,90) 6d,5f | (90,91) 5f,6d.

RULE B. Inequality: S > 0 and P < 0 at every collapsing channel; |P| > |swing|. DIRECTION: the
entrant electron OPPOSES the swing (screening takes back part of the proton collapse). SIGN-exact for
P1,P2; VALUE-exact for P4 (identity to 1e-5) and P5 (|P_f| vs D4 shortfall).
FLAG AT FILING: the order words the swing as "what the d gains when the entrant screening is removed",
i.e. swing = -S with S<0 . I predict the OPPOSITE sign for S. If S>0 the order item is wrong-sided as
worded (cf. F90.1) and the derived quantity is P, not S. Either way the data rules; filed before seeing it.

P1 (sign) S > 0 for every (row, channel) listed, including the rival channel.
P2 (sign+ratio) P < 0 and 0.10 < S/|P| < 0.60 for the collapsing channel (4d@38, 5d@56, 4f@58, 5f@90, 5f@91).
P3 (lever) with entrant occupancy 0.5 in the reference, S(0.5) lies strictly between 0 and S(1). rc=4 if
   |S(1)| < 1e-4 Ha at any row (lever dead).
P4 (identity) P + S reproduces the sealed swing to 1e-5 at every row (rung 0 reproduction).
P5 (D4 link) at 58 and 91, |P_f| exceeds the D4 shortfall (0.10029, 0.05405) -- the proton alone overshoots;
   at 38 and 56, S_d < S_s + |P_d - P_s| is NOT asserted; instead: the across margin at Z* equals
   (D(s)-D(d)) at Z* as sealed (0.07799 @38, 0.03914 @56), and P_s < 0 with |P_s| < |P_d| (s co-descends less).
P6 (stop) Z=90 entrant remains 6d in every control solve touching 90. If it flips: STOP.
Can-fails, run first: (A) lever-dead injection (occupancy held at sealed value) must return rc=4;
(B) wrong-shell freeze (freeze 4p at 38 instead of 5s) must break the P+S identity (>1e-3). Both must fail.