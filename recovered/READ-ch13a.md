# READ-ch13a.md — Phase R2 read of main §12.11.3.1 "Where each bound comes from, and why 9, 10 and 11 differ" (L3409–3456), chat 78

Instrument: r2-ch13a.py (golden r2-ch13a.out). No repairs (chat 67 hold).

## A — deviations (both texts)

**13a-01 — the withdrawn 2,475 standing at two further sites, one with a failed citation.**
L3477 (§12.11.5): "recomputed; **the 2,475 previously printed here is withdrawn**." Yet L3434 (this range) prints "§A.15 and register 230 record what it costs, 2,475 cells of the cylinder", and L914 prints "The tight K has two parents and costs the cylinder 2,475 cells." The L3434 citation fails both ways: **A.15's printed text (L10054–10071) contains no 2,475** — it is the two-bands result (B_k a sublattice, C not) — and **register 230's printed body is the kind-coordinate entry** ("APPENDIX D'S KIND COORDINATE DISAGREES WITH PART III'S TITLE"), also without it. Measured: the tight-K cuts are 15,150 (Λ₁₂ 70,905 → 55,755) and 45,450 (Λ₁₃ 199,130 → 153,680) — the figures L3477 prints as the recompute — and no natural cut equals 2,475. Joins 12q-06's sites (L3067's "3.5 %", the L2533 Figure 12.4 caption); the residue set for R3 is L914, L2533, L3067, L3434, with L3477's withdrawal governing (the later line). For R3; no withdrawal of the recorded texts.

**13a-02 — "the largest 2J" for "the largest 2J_c": the main's sentence false as printed, the MC's correct.**
L3439–3440: "φ̂ = {1: 3, 2: 4, 3: 5}, and **the largest 2J actually realised at each occupancy** is {1: 3, 2: 4, 3: 5}." Measured: the largest **2J** per k over Λ₁₃ is **{1: 6, 2: 7, 3: 8}** — not φ̂ — while the largest **2J_c** per k over Λ₁₁ is {1: 3, 2: 4, 3: 5}, exactly φ̂. MC L1264 prints "the largest 2J_c the set actually realises" — correct. A coordinate-name slip that falsifies the printed sentence while the intended identity (φ̂ = the envelope of the realised 2J_c extent) is exact. For R3; no withdrawal.

## B — verified (measured, r2-ch13a.py)

- L3413–3428 the thirteen bounds "verified against the construction, cell by cell": all thirteen hold at every cell of Λ₁₃ (199,130 cells; zero violations per bound).
- L3428–3429 "The provenance column has three values, not two": tabulated — law × 11 (D1–10, D13), extent × 1 (D11), law-weakened × 1 (D12).
- L3435–3436: **39,375** of Λ₁₂'s 70,905 cells sit at f below the cap — exact.
- L3439–3442 φ̂ observed = {1: 3, 2: 4, 3: 5} = tower-2.py's PHI = the realised 2J_c maxima (see 13a-02 for the wording).
- L3433–3434 the tight two-parent K: cuts measured at 15,150 / 45,450; 15,150 = 21.4 % of 70,905 and 45,450 = 22.8 % of 199,130, matching L3477's "of the product" percentages — the section-product identity (product of the tight set's sections = the weak stage's count) is §12.11.5's segment to verify formally.
- **12j-01 settled.** The tower table's grading column (L2937–2942: Λ₉, Λ₁₀ exact; Λ₁₁–Λ₁₃ envelope) against this section's provenance column: the boxed rule (L3444–3445, "A bound taken from the law closes exactly ...") read **per axis** predicts D13 exact (its provenance is law) against the printed envelope grading — the one failure; read **per chain**, with L3436–3437's "Dimension 13 inherits the weakening through K without adding to it", all five gradings agree (grading = law-chain intact vs extent/weakened at or below; provenance refines where). Instrument prints the five-row comparison. The residual defect is the shared vocabulary — 12z-02's sites grow by L3444–3445 and by A.15's L10070–10071 ("the last coupling step is carried exactly", the band-sublattice sense). Register 326's one-directional strength ("an extent-bound gives an envelope, no exception") is consistent with the per-chain reading.
- L3411/L3447 §22 pointers resolve: "a deduction, not a prediction ... a fit says where a level probably is" (L5951); "Presume the next bracket from the law that generates the widths, never from the pattern the widths make" (L6027) — L3448 carries the operative clause verbatim. Register 325 (L1205) resolves L3455's pointer (the bracket rule beside the tiers ruling).
- L3436–3437 "Dimension 13 inherits the weakening through K without adding to it": verified in the parent sense — D13's bound adds no second parent and no extent-taking; its own coupling-envelope aspect (the bound admits 2J = 2K, parity-excluded) is the standard per-axis envelope behind the 64.4 % density, not an added weakening.

## C — incidental

- Census row 1073 (C9, L3448 "never"): the flagged token is the cited section's own rule, verbatim at L6027 — regex artefact, closed not a defect (precedent 678, 680–687, 1067, 1069 class).
- Numeral near-collision for R3's care: A.15's one-sided band C = {|a−b| ≤ c} fails **12,654** meets at cap 8 (L10065) while §12.11.2's two-sided T fails **12,489** at cap 8 (measured, r2-ch12y) — adjacent triangle variants, distinct regions, near-colliding counts; neither corrects the other. A.15's own figures belong to Appendix A's segment.
- L3410–3411 "the same distinction §22 draws between a deduction and a fit" — the analogy holds as read; no figure.
