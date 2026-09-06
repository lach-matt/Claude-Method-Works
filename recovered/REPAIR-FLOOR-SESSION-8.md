# REPAIR — THE PACK-5 BISECTION FLOOR — SESSION 8 (2026-08-16)
Bridge-7 §2(b), M ruled: repair NOW. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to
register/index/store. Pack-5 artefacts left VERBATIM; the repair is new named files in pack5fix/.

## 0 · Rulings received this session (in order)
(a) T2 closure: **NO — the derived law at 100/106 does not meet ruling 1.** Not closed.
(b) Pack-5 floor: **repair now.** Done, below.

## 1 · The fault, sharpened
step2_run.eigen brackets E in [−0.6ζ², 0). At charge 1 the floor is −0.6 Ha; deep shells lie below it and
the bisection returns the bracket edge silently. 24/106 step-3 E_B rows carry −0.6 exactly (bridge-7 list).
NEW this session: Os 5d in the pairing class was SOLVED at the floor (derive_P.json E = −0.6, E_at_floor
true), so its u(r), F^k, J_H and P — not only its window — were computed at a wrong eigenvalue.

## 2 · The repair (eigen_fix.py) — adaptive bracket, no new constant
Start at the pack-5 floor. Test whether the shoot at Elo says "E too high" (the bisection's own test); if so
Elo is not below the eigenvalue → deepen ×4, capped at the rigorous bound −Z²/2 (V ≥ −Z/r). Where the old
floor already bracketed, Elo is untouched → bit-identical to pack-5. Deepening is on demand only, so
Session 4 fault (ii) (spurious nodes at deep E, ζ ≥ 9) is not re-exposed. Bridge-7's suggested
−0.6·max(ζ,3)² was NOT used: it is another chosen constant, and it would still clip (Yb 4f sits at −1.71).
Self-test: H 1s −0.500027 deepened 0 (unchanged) · Os 5d −0.6 → −0.77272 deepened 1.

## 3 · step3 rule-B column recomputed (step3_fix.py → step3B_fixed.jsonl), 106/106 rows
- Exactly the 24 flagged rows changed; each deepened once. Shifts −0.6 → −0.62 (Zn 4s, W 5d, Dy 4f) …
  −1.71 (Yb 4f). The other 82 rows are BIT-IDENTICAL to pack-5 (bracket unchanged ⇒ same bisection).
- No rule-B verdict moved: B hits 87/106 = 87/106. E_A rows: not recomputed — 0 at floor in pack-5 and
  the repair leaves an unclipped bracket unchanged, so they are identical by construction.

## 4 · Windows and the derivation chain rerun (derive_P_fix / P2_fix / P3_fix, WIN_fixed.json)
Ten class EB gaps recomputed from the repaired rows: nine identical to four decimals; **Os 0.3766 → 0.5494**.
Chain rerun with the repaired eigen and the repaired Os window:
| | held (pack-7) | repaired | verdict |
|---|---|---|---|
| Os E(5d) | −0.600 (floor) | −0.7727 | — |
| Os J_H | 0.0402 | 0.0377 | — |
| Os K(5d,6p) | 0.0067 | 0.0077 | — |
| Os P_i | 0.2010 | 0.1885 | IN (top 0.5494) |
| Os P_ii = P_iii | 0.1678 | 0.1502 | IN |
All nine other species: unchanged to the digit in all three JSONs. **P_iii 10/10 stands; 100/106 stands**
(only class steps can move under the clause; none did). No E_at_floor remains anywhere in the chain.

## 5 · What this does and does not change
- The standing derived result of session 7 is UNCHANGED in every number except Os, which moves toward the
  middle of a wider window. The result was not resting on the fault.
- The 24 clipped E_B rows in pack-5 step3_rows.jsonl are now superseded by step3B_fixed.jsonl for any
  future use of E_B magnitudes/gaps. Pack-5 file itself untouched (verbatim, per protocol).
- COMPUTED-TFD.tsv (step 2, 103,545 cells) was built with the SAME eigen and the same −0.6ζ² floor. Its
  cells are indexed by (Z, charge, l) over charge 1..Z; the floor binds only where |E| > 0.6ζ² — i.e. LOW
  charge, deep shells. NOT audited this session. FLAG, owed: scan COMPUTED-TFD.tsv for cells at the floor
  before the index write of R 1715's ruling proceeds (bridge-6 T4). A δ computed at a floor energy is a
  false value with the appearance of a measurement — the §2.9 shape.

## 6 · Figures (§H.6)
MEASURED (kernel): 24 repaired E_B; Os F^k/J_H/K/P. CHOSEN: none — the ×4 step and −Z²/2 cap are bracket
mechanics; the cap is a bound, not a fit; results are invariant to the step size (any factor >1 reaches the
same bisection root). INHERITED: everything in bridge-7 §4.