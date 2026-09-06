# PREDICTION S94 ITEM 1 -- LAW B: SPIN-ORBIT SPLITTING OF THE ENTRANT vs THE CHAIN MARGIN, ALL ROWS. Written at s93 close, hashed, NOT RUN.
## Instrument to build (pack94/so94.py) from pack19/t7c_so.py: for each row Z=2..120 take the sealed entrant (n,l) and its SCF potential
##   in the sealed field (nlchain reference cfg(Z-1)+entrant), compute zeta_nl = (alpha^2/2)<P|(1/r)dV/dr|P>, Delta_SO = zeta*(2l+1)/2,
##   and r(Z) = Delta_SO / m(Z) with m(Z) the sealed margin (rt/nlchain.jsonl). s entrants: Delta_SO = 0 by construction (l=0): report, don't score.
## Rule B declarations:
B1 SIGN-exact: zeta > 0 on every l>0 row (dV/dr > 0 for an attractive potential).
B2 VALUE: r(Z) < 1 on every scored row Z <= 108 with l>0 (the hidden condition holds throughout the evidentiary region).
B3 VALUE, bound-direction UP: the first row with r(Z) >= 1 lies in 109..120 and is a 7p entrant (the Eliav/Sato boundary, now derived).
B4 VALUE: r(Z) at the 5f/6d rows 89-103 <= 0.5 (the actinide tie-break rows are decided with spin-orbit a minority of the margin).
B5 HYGIENE: zeta reproduces pack19/t7c_so.jsonl at Lr (7p 0.035, 6d 0.01122) and La/Gd 5d to 3 significant figures (same formula, same field).
## Can-fails: A lever-dead: c -> 1e6 must send every zeta below 1e-9 (rc=4 if not). B control: Lr reproduction perturbed by 10% -> B5 fires rc=4.
## Mechanism if B2 fails: the hidden condition fails INSIDE the scored region at the failing row; the ordering clause at that row is
##   conditional on a splitting larger than its margin and T4 must say so row by row. Mechanism if B3 fails low: same. If B3 fails high
##   (no crossing by 120): Law B does not set the boundary; Z=108 remains a choice.
## Bars: m(Z) floor 5e-5 Ha (F93.4); zeta precision from pack19 ~1e-5 Ha.