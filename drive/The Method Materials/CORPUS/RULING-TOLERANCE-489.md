# RULING — Tolerance for the 489-row bracket run

Issued by M (The Method Löwdin project), 2026-08-24, accompanying
`spectra_levels_store.zip` (sha256 08a6a78c…, cut from restore-point-2_13,
bank sha 80577094…, 708 files).

## The ruling

1. **Test.** The bracket test runs at STRICT INTERVAL MEMBERSHIP, exactly as
   the sealed instrument defines it (`bracket.py`, register 796):
   E(n) ∈ [E_lo, E_hi], where the interval is the energy span implied by the
   two neighbours' defects. No statistical tolerance. No k. No σ band.
   This is the condition the run itself stated — "the same test as the 107" —
   and the sealed test carries no tolerance to reproduce.

2. **Boundary guard (the only ε permitted).** Comparisons at the interval
   edges are guarded by the QUOTATION FLOOR: half a unit in the last quoted
   decimal place of the measured level. This is data quantization read off the
   source, not a fitted parameter, and it satisfies the standing floor rule
   (F104.1/F104.2: value-exact comparisons must state and exceed the
   floating-point floor).

3. **Admissibility replaces tolerance.** A cell where the measurement cannot
   distinguish pass from fail is REFUSED, not passed with slack:
   r = 2·Z²R/(ν³σ) ≥ 5 (Method §22.5). Refusals are counted and reported as
   their own column, separate from pass/fail.

4. **Option B (2·σ(δ) per channel, k = 2) is REJECTED**, on four registered
   grounds:
   a. It is a different test than the sealed 930-cell run — violating the
      run's own stated requirement.
   b. It grafts the inferential σ (Rule 4) onto the deductive bracket,
      collapsing Rule 3's separation; a deduction becomes an estimate
      (Method §22.2, §23.3: "V contains no σ").
   c. A tolerance-widened bracket is the registered fault species of a check
      that admits inputs incapable of failing it (registers 777, 782, 784).
   d. The σ it would be built from is measured untrustworthy where it would
      be used: quoted-decimal error estimates drive an 89% result to 55%
      with non-overlapping intervals (register 822); 44 of 49 species carry
      no uncertainty column (register 807); and per-channel σ(δ) computed
      from the data under test is register 781's circularity.

## Execution notes for the receiving chat

- Column updated row by row; count line rewritten; refusal count printed as
  its own line; this ruling's number registered where the note stands;
  Spectra and main re-pressed and sampled at the changes — per the plan
  already stated there.
- Flag standing: "844 of 844 on 107 tested rows" matches no figure in this
  bank's register (789/789 T-bracket, 546/789 δ-bracket, 930 cells /
  128 channels tested). Confirm its provenance in the receiving project's
  own record before attributing it to this bank's instrument.

## Derivation sources

bracket.py docstring (R 796) · Method §22.2 Rules 1–4 · §22.5 admissibility ·
§23.2 Prop. 14.1 (V > 2) · §23.3 (V contains no σ) · §23.14 capacity vs
resolution · registers 777, 781, 782, 784, 796, 803, 807, 822 ·
F104.1/F104.2 standing rule.
