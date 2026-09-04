# PREDICTION-PT-SO (s48) — FILED BEFORE `pb4_so.py` EXISTS

Binding under R 1449. Target: the **3.844 mHa residual at Z=59** left by PT-3, which is the
origin of the entire 59..70 configuration divergence and of the label failures at 64 and 71.

## 1 · WHY SPIN-ORBIT, AND WHY IT IS RUN ON A NEW INSTRUMENT

PT-2 established that Hund-I exchange closes 45.148 of the 48.991 mHa gap at Pr — 92% — and
PT-3 established that it does not close the rest. The chain's remaining differentiators are
relaxation, correlation, and spin-orbit. **Relaxation is already spent**: each configuration
in `pb4_terms.py` was run through its OWN hfc2 SCF, so average-of-configuration relaxation is
already in dAVG. **Correlation is ruled class-flat and row-non-differential** (s37), so it is
not expected to differentiate two configurations of the SAME atom — but that ruling was
established for ionization classes, NOT for configuration competition, so it is NOT assumed
here and is left open as its own object. **Spin-orbit is untested on this object** and its
scale is right: a first-order estimate at 4f gives a level shift of order 10 mHa against a
3.8 mHa residual.

**INSTRUMENT NOTE, DECLARED BEFORE THE RUN.** `t7c_so.py` computes zeta on the **SR-pol TS**
field (`scf_pol_sr`). The PB-4 numbers are on the **hfc2 SR HF** field. Reading one against
the other would mix instruments, which is the fault class this project exists to avoid.
`pb4_so.py` therefore recomputes zeta **on the hfc2 converged potential itself**, from the
same P and the same grid that produced E_A and E_B, using the same formula
zeta_nl = (alpha^2 / 2) * INTEGRAL P^2 (1/r)(dV/dr) dr with alpha = 1/c and c = 137.035999.
No new constant.

**APPROXIMATION, DECLARED NOT HIDDEN.** For A = 4f2 5d1 6s2 the two open shells are treated
**shell-additively in the LS limit** — each open shell contributes its own lowest-J shift and
the shifts are summed. A fully coupled 4f2·5d treatment is NOT done here. This is an
approximation and any clause it decides is scored as provisional.

Single-shell lowest-J shift, standard LS result, no fitting:
    A_so = +zeta/(2S) if N < 2l+1 ; -zeta/(2S) if N > 2l+1 ; lowest J = |L-S| or L+S resp.
    E_SO = (A_so/2) * [ J(J+1) - L(L+1) - S(S+1) ]
with (S,L) taken from the term ALREADY COMPUTED by the diagonal-sum rule, not asserted.
A closed shell contributes zero. A single electron (5d1) is the N<2l+1 case with S=1/2.

## 2 · THE CLAUSES

**PS-1 — SO LOWERS BOTH CONFIGURATIONS AT Z=59.** E_SO(A) < 0 and E_SO(B) < 0. Falsified by
either being non-negative; that would indicate a sign error in the level formula, not physics.

**PS-2 — SO LOWERS B MORE THAN A: dSO = E_SO(A) - E_SO(B) > 0.** B is 4f3 with three aligned
f electrons (S=3/2, L=6, lowest 4I9/2); A spreads three electrons over 4f2 and 5d1 and cannot
assemble as large a J. Falsified by dSO <= 0.

**PS-3 — THE SHARP ONE: SO CLOSES THE RESIDUAL OUTRIGHT, dTOT + dSO > 0 at Z=59.**
This requires dSO > 3.844 mHa. If it holds, the record's promotion at Pr is fully accounted
for by exchange plus spin-orbit on the walk's own field with no constant beyond c, and the
whole 59..70 divergence closes at its origin. Falsified by dTOT + dSO <= 0 — a real outcome,
to be logged, leaving correlation or coupled-shell SO as the remaining candidates.

**PS-4 — SO DOES NOT DISTURB Gd. At Z=64, dTOT + dSO < 0.** The Gd margin is 168.6 mHa and
SO is of order 10 mHa, so the element the field currently gets right must stay right.
Falsified by dTOT + dSO >= 0, which would mean SO breaks Gd while fixing Pr — a net loss.

**PS-5 — NO CONSTANT INTRODUCED.** alpha = 1/c, c = 137.035999, already the sole entered
number. Falsified by any swept or fitted parameter.

## 3 · NOT PREDICTED

Magnitudes (no bands; signs and the one threshold in PS-3 are the claims). Whether the
shell-additive approximation survives a coupled treatment. Correlation's behaviour on
configuration competition. Lu(71). Any J-level other than the lowest of each configuration.
