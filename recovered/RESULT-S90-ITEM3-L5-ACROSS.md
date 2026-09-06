# RESULT S90 ITEM 3 -- THE ACROSS CLAUSE AT THE s->d COLLAPSE, READ AT L5 (sealed eigenvalues, no runs)
Prediction ee74c4c1..ed58 hashed before the read. Series (5s,4d) Z=34..38, (6s,5d) Z=52..56.
Identity used: g(d)-g(s) = 1 - (nu_d - nu_s); clause <=> nu_d > nu_s <=> eps(s) < eps(d).

## Table (n* = 1/sqrt(-2D) from rt/nlchain.jsonl)
 Z   n*_s   n*_d   dn*_s   dn*_d   nu_d-nu_s        Z   n*_s   n*_d   dn*_s   dn*_d   nu_d-nu_s
 34  2.019  3.025                   +1.006          52  2.103  2.860                   +0.758
 35  1.971  2.899  -0.048  -0.126   +0.928          53  2.056  2.832  -0.047  -0.028   +0.777
 36  1.929  2.895  -0.042  -0.004   +0.966          54  2.014  2.806  -0.041  -0.026   +0.792
 37  1.892  2.893  -0.037  -0.002   +1.001          55  1.978  2.779  -0.036  -0.027   +0.801
 38  1.692  2.275  -0.200  -0.618   +0.583          56  1.783  2.057  -0.195  -0.722   +0.274

## Scoring
P1 SHAPE HELD, SIZE FALSIFIED: plateau 36-37 (|dn*_d| <= 0.004) and 53-55 (<= 0.028); single-
   proton transit at 37->38 and 55->56 -- but of size 0.62 and 0.72, NOT > 0.8 as filed.
P2 HELD: s has no transit, max |dn*_s| = 0.200.
P3 HELD: nu_d - nu_s > 0 at all 10 rows; minimum 0.2741 at Z=56, as filed.
P4 HELD: post-transit n*_s < n*_d - 0.2 at 38 (0.58) and 56 (0.27). Can-fail did not occur.

## The statement (D3 form, regime from the derivative, nothing fitted)
 margin after collapse = plateau gap - d transit + s co-descent:
   Z=38: 1.001 - 0.618 + 0.200 = 0.583 (exact to 1e-3)     Z=56: 0.801 - 0.722 + 0.195 = 0.274
The across clause at 37 and 55 holds on the PLATEAU (the d is hydrogenic-outer, nu_d - nu_s ~ 1,
s90 Item 1 P2: delta_outer(d) < 0.011). At 38 and 56 it holds because the d's one-proton
transit (0.62, 0.72) is smaller than the plateau gap plus the s's own co-descent at the same
step (1.20, 1.00). Z=56 is the tightest row in the table because 5d's transit is the largest
of the two and its plateau gap the smaller.

## STATUS OF L3-ACROSS dl=2
CLOSED AS COMPUTED AT L5 (10/10 rows, value-exact). REMAINDER NAMED: the transit width --
why the d falls 0.62 / 0.72 in n* in one proton and not more. THIS IS THE SAME REMAINDER
D3 §6 ALREADY OWES FOR THE f OPENINGS (lag one proton at 4f, two at 5f). The chain now has
ONE named residue for both failure classes (tie-break at f, across at d): the transit width.
Deliverable 4 (THE-TRANSIT-WIDTH) is on disk and is the next thing to read, not to rewrite.