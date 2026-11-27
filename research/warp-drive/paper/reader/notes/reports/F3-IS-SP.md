# F3-IS-SP: fix round on P-U71-IS and P-U71-SP (from R3-IS-SP)

Started from b571483c (md5 545148…/f2461a…). Snapshot commits 24cecedf and 912d83d3, made during the round by
another process, already hold these edits; the diff is against b571483c. No number moved.

## P-U71-IS
- IS-F1 (minor), l. 653-660: reviewer's text verbatim. (SP) is now settled by [[cor:sp-lstar]] (a), and c_b is the
  one undetermined item. Only the tail of the remark is re-wrapped.
- IS-N1, l. 532: reviewer's text verbatim.
- IS-N2, l. 228-235: reviewer's text verbatim, re-wrapped to the same 8 lines.

## P-U71-SP
- SP-F1 (minor), l. 549-553: the reviewer's option, ε_+ < δ_50 < 2·10⁻⁸ ([[eq:iii-i9-1-1]], [[def:ec-point]]).
  The words are the reviewer's; the line breaks are hand-chosen. The proof already uses this bound and is unchanged.
  Checked: δ_50 = 1.94137056846·10⁻⁸ and ι_v(2) = 3.00000499998 > 3 + 4·10⁻⁶.
- SP-N1 (i), l. 25-28: reviewer's declaration ("we write c for the weight μ there …").
- SP-N1 (ii), l. 320-330: μ_0…μ_3 → ν_0…ν_3 (24 occurrences). The only other ν in the section is the moment vector
  of [[prop:sp-visible]], the same kind of object, so there is no clash.
- SP-N2, l. 342-343: "(proof of [[prop:gap-sums]])".

Departures: none in substance.

## Uses of cor:sp-lstar (d)
No text cites (d). Each citation is for l_* = 50 or for pole orders 1, that is part (a), and each still holds:
- SP, l. 19 and l. 602;
- P-U71-close, l. 14, 319, 416 and 539;
- P-U71-assembly, l. 619.

The evaluation's ε_+ = 1.9·10⁻⁸ < δ_50 (close l. 363) meets the new hypothesis of (d).

## Lint
- 249 hits, all "reference to undefined label" (cross-chapter keys). There were 247 before; the two new hits are the
  citations that (d) adds.
- Maximum line length 121; no wrapped line has a forbidden start; 58 labels, unchanged.

## Left for the coordinator
- prop:is-logs (a): the steps at m = 1 (the first step of (1), and the class 1 − l at l = 2) are not written out.
  They have order 0 at 1, 1 + 𝔡₀ and 1 + 𝔡₁, below the 3 that (c2) attains there.
- In SP, c_i stands both for weights (proof of [[thm:sp-reduction]]) and for coefficients ([[lem:sp-exceptional]]).
