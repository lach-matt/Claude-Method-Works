# PREDICTION-CHAIN-5p (s45, item 2) — Z = 49..54, THE FOURTH TIE-BREAK PAIR

Filed BEFORE nlchain is pointed at Z=49. R 1449. Nothing below is read from a run.

## 0 · THE SETTING

Chain state at Z=48 is `...4d10 5s2`, and **cfg_ok(48) = True** — the chain enters this row
carrying the record's configuration exactly. No inherited defect.
Open candidates at Z=49 (from the sealed Z=48 `order`): 5p, 6s, 6p, 4f, 5f, 6f, 6g, with
5d, 5g, 6d failing.

## 1 · THE ORDERING

**PC5P-1 — 5p IS THE ENTRANT AT ALL SIX STEPS.** n+ℓ = 6 for 5p and 6 for 6s: a TIE, broken
by clause 2 (smaller n first). This is the **FOURTH distinct pair** to test that clause —
after 4s/3d (10/10), 4p/5s (6/6) and 4d/5p (10/10). Predicted 6/6, taking the clause to
**32 steps across four unrelated pairs with no exception**.

**PC5P-2 — THE RUNNER-UP IS 6s AT ALL SIX, AND ITS IDENTITY NEVER CHANGES.** Per F44.2 the
margin is quoted against a named channel or not at all.

**PC5P-3 — THE MARGIN AGAINST 6s WIDENS MONOTONICALLY, FROM ~0.09–0.11 AT Z=49 TO ~0.30–0.36
AT Z=54.** Banded on the 4p row's shape (0.10012 → 0.35190, second differences smooth at
~0.003). A band, not a value; falsified by non-monotonicity or by landing outside it.

**PC5P-4 — D_ent DEEPENS MONOTONICALLY, ≈ −0.20 ± 0.02 AT Z=49 TO ≈ −0.50 ± 0.06 AT Z=54**,
at roughly 0.05–0.06 per proton. Same basis, same status.

## 2 · THE CLAIM THAT MATTERS — THIS ROW DISCRIMINATES THE ORDERING VARIABLE

s44 §2(9) filed the 4d row's null in advance: 4d carries n=4, no smaller-n candidate was
open, so **n and n+ℓ agreed at all ten steps and the row could not discriminate**. The
evidence for n+ℓ over plain n has therefore rested on **four elements — K, Ca, Rb, Sr**.

**PC5P-5 — THE 5p ROW DISCRIMINATES AT ALL SIX STEPS.** 4f is open, is a candidate, and
converged at Z=48 (D = −0.03128). It carries **n = 4**; the winner 5p carries **n = 5**. So a
plain-`argmin n` rule selects **4f at every one of Z=49..54**, and n+ℓ selects 5p.
**Predicted: the field selects 5p at all six, so argmin-n is WRONG at six consecutive
elements while n+ℓ is right at six.**

**PC5P-6 — THE EVIDENCE BASE FOR n+ℓ OVER n GOES FROM 4 ELEMENTS TO 10**, and for the first
time it is carried by two different mechanisms — a tie-break (4s/3d, Rb/Sr) and an outright
loss by the smaller-n channel. Stated as the row's purpose so a pass is not read as routine.

**PC5P-7 — 4f STAYS FOUR TIMES TOO SHALLOW TO COMPETE.** |D_4f| < 0.10 at all six steps, and
D_4f > D_5p (less bound) at all six. 4f deepens with Z but does not approach the winner.
**If 4f ever wins, PC5P-1, 5, 6 and 7 all fail together and this row becomes a part-3
problem — the f-opening arriving 8 elements early.** That is the failure mode worth naming.

## 3 · THE CONFIGURATION COLUMN

**PC5P-8 — cfg_ok = True AT ALL SIX AND ok = True AT ALL SIX.** The record has no anomaly in
this row: In 5p¹, Sn 5p², Sb 5p³, Te 5p⁴, I 5p⁵, Xe 5p⁶ on `[Kr]4d¹⁰5s²`.
*Record configurations quoted from RECALL, placed under prediction before the run per R 1639
and R 1645; scored against `ground.py`.*

**PC5P-9 — THE SCORES GO 39/47 → 45/53 AND 42/47 → 48/53**, both columns gaining six, the
disagreement set unchanged at 11, and **FIRST CONFIG DIVERGENCE 24, FIRST STEP DIVERGENCE 25
both unmoved.** Gate 83's expectations must then be restated — the s45 note on gate 77.

## 4 · A PREDICTION AGAINST

**PC5P-10 — NO HALF-SHELL SIGNATURE AT Sb(51) AT THE 1e-3 LEVEL.** 5p³ is a half-filled p
shell. The 4p row's margin second differences run 0.00302, 0.00327, 0.00334, 0.00336 —
smooth, monotone, **no kink at As(33), the corresponding half-shell**. Predicted: the same
here, no sign change and no minimum at Z=51. s44 §2(7) found the 4d⁵ signature real and four
orders too small to matter; this predicts the p-shell analogue is **not detectable at all**.

## 5 · UNPREDICTED, DECLARED

`nfail` exactly. Predicted only that the failing set ⊆ {5d, 5g, 6d, 6f, 6g} and that **no
winning or runner-up channel fails at any step** — the clause that has held on every row.
Iteration counts. The `sec` field.
