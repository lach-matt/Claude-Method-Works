# Report P-G24b: the remaining preprint steps of chapter 33

The output is `research/warp-drive/paper/reader/proofs/P-G24b.md`, 1559 lines, not committed. No chapter or crosswalk was
edited.

## The base text

Every old text was copied from the current working-tree chapter 33, md5 007858d84d3f7b2ba03c0c84d0338749. That file
includes the F2-G24 fix round and the P-LB merge, so it is not the file at 003371f6. The coordinator's note was followed:

- Every region the fix round changed was re-copied from the current file.
- Each old text occurs exactly once, and no two overlap. A script checked both.
- The withdrawn G2 claim is not repeated anywhere.

## The classification

Chapter 33 has 247 bracketed citations: [Hin26a] 208, [Hin26] 28, [Hin26c] 4, [Hin26d] 3, [Hin23d] 2, [Mel93] 1 and
[Shu92] 1. The proof file's section 2 gives the full table, by line.

- **(a), steps used and not proved:** about 60 uses.
  - The preprint displays (5.70)–(5.78) and (B.20), (B.21), (B.24)–(B.26), (B.28), (B.29) and pp. 89–90, which were on
    the given list.
  - Symbols defined only in the preprint: "the b_0, b_R, e and f of [Hin26a]" in prop:iv5-2-1, iv5-3-1, iv5-4-1,
    iv5-5-1 and thm:iv6-2-1.
  - Undefined cut-offs: (5.35) and (B.36).
  - The adjoint pairing (5.49), and (5.47)–(5.48) with the h^(1/2) iteration.
  - (5.28) and (5.30) in prop:iv5-1-3.
  - (B.34)–(B.41), which thm:iv6-2-1 used as names but never displayed.
  - "[Hin26a, (2.13)–(2.14)], with the same proof" and "∂_z ∈ ρ_sf𝒱_3b by [Hin26a, §2]".
  - The classical Cauchy theory, cited as "[Hin26a, p. 42]".
- **(a-G1):** 9 sites of the 3b-calculus, left to P-G1: §2.3 ×3, p. 45, (5.44)–(5.46), and prop:np-10-65-a with [Hin23d],
  [Shu92] and [Hin26d].
- **(c):** the relative index theorem [Mel93, Thm 6.5], quoted in Appendix A as thm:std-relative-index.
- **(b):** everything else, including all 28 [Hin26] citations and the four [Hin26c] citations.

## What was proved

T1–T43 give exact old and new texts, with 16 new labels and crosswalk rows. The new results and replacements are these.

- **lem:iv5-2-symbols.** An exact Leibniz identity for aH_(−ℓ+j)a ∓ Sa² when a is a product commutant. It comes with
  conventions for the cut-offs (smooth (±χχ′)^(1/2)), including a proof that such cut-offs exist. Every symbol
  decomposition in sec:iv5-2 to sec:iv5-5 and at the cone face is now written out from it.
- **eq:iv5-2-adj.** The adjoint pairing.
- **eq:iv5-2-iter.** The estimate before the iteration; the iteration itself is written out in words.
- **lem:iv5-6-transport.** An integrated identity for 2B(Aω, ω), with boundary terms, which replaces (5.77). It also
  gives |𝒩|, |S| = O(r⁻²).
- **lem:iv5-6-core.** An energy estimate for h²□_g + 2hA + hY, built from cor:iv5-6-energy and the transport identity.
  It allows boundary pieces of both signs. Its constants are explicit:
  - λ_* = max(1, 2(2C_Y² + C_R)/c₀, 8C_N/c₁, 4C₂^(1/2)/c₁);
  - C_* = (32c₁⁻² + 4c₀⁻¹)(1 + C₂C_ℓ/c₁ + C_Q) + 2C_ℓ/c₁, with C₂ = 2C_Y² + 4C_N² + C_R.
- **A new proof of prop:iv5-6-1.** All four estimates and eq:iv5-6-1 follow from lem:iv5-6-core, for every h ∈ (0, 1].
  The proof includes:
  - P_h* = h²□_g + 2h(−A) + h(2S + hZ), with □_g* = Θ⁻¹□_gΘ;
  - an explicit cone lemma (∗) with constants;
  - the four weights, regions and boundary signs.
- **prop:iv6-1-1.**
  - The dual estimate is displayed (eq:iv6-1-3).
  - The shift is defined.
  - The estimate (eq:iv6-1-4, with error term in H^(−M,(−M,−M))) follows from chapter 20's boundary-face estimates and
    chapter 22's proof of thm:i-c-4-3, through lem:iv6-0-1 (d), with the thresholds identified.
  - Complex σ follows from prop:i-a-4-9.
- **thm:iv6-2-1.** eq:iv6-2-e1, eq:iv6-2-e2 and eq:iv6-2-ap are displayed. The symbols at the cone face are explicit,
  and the forward and backward cone estimates are defined.
- **thm:iv5-7-3 (b).** The smooth-data Cauchy problem now goes through thm:std-bgp-development and thm:std-bgp-cauchy (5),
  with f taken in C_c^∞(Ω°).
- **def:iv6-0-2.**
  - At complex σ, only the condition at R_out is asked.
  - Admissibility is now defined at every real σ₀ ≠ 0.
  - "Admissible on a set" requires admissibility at Re σ too, which is chapter 20's convention.
  - Every use was checked: prop:iv6-1-1 (statement, estimates, uniformity, index 0), thm:iv6-3-1, thm:iv6-4-1 and the
    orders of chapter 22. No other chapter cites the definition.

## Findings for the coordinator

1. **The second estimate of prop:iv5-6-1 (1) is false as stated.** It says "without support condition", but it needs ω
   supported at Σ^♯.
   - The counterexample: a backward solution of P_h*ω = 0 fed by data entering through the final surface Σ^♯ near
     X_0 ∩ Σ^♯.
   - The only use, prop:iv5-7-2 (x), satisfies the condition, so nothing downstream changes.
   - T19 adds the condition. This should go to the author. The same gap is in [Hin26a, (5.67)].
2. **Two harmless adjustments.**
   - T3 adds δ_r < 1/5 to lem:iv5-0-5. Every condition there survives a decrease of δ_r.
   - T8 takes χ_K in prop:iv5-3-1 supported in [0, 2δ_r). With the support ending at (3/2)δ_r, b_0 would vanish on
     part of WF′(B_0) as stated.

## Not proved here

- **The relative index step in the index-0 part of prop:iv6-1-1.** The theorem quoted in Appendix A is for compact
  b-manifolds, but the operator is scattering at r = ∞. The proof file's section 6 sketches the proof, about a page. It
  needs a multiplicity count for the sector indicial polynomials that the paper does not contain. This is a published
  theorem applied beyond its stated hypotheses, not a preprint step.
- **The G1 calculus facts.** Left to P-G1.

## Overlap with P-G1

proofs/P-G1.md exists.

- **C33-11 overlaps T41.** T41 is given in two variants: one for the current text, and variant A for after C33-11.
  Variant A's old text occurs exactly once in C33-11's new text.
- **C33-20's anchor sentence is T34's old text.** Insert C33-20's paragraph before T34's new text.
- **Adjacent, with no shared characters:** C33-10 with T5, and C33-12 with T7.
- **No other overlap.**

## Check outputs (scratch copy at /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pg24b/)

Before:

    $ python3 lint.py --chapters
    chapters: 62 file(s), 4609 label(s) defined, 0 hit(s)
    $ python3 assemble.py --check
    labels 4609, computations cited 0, problems 0

After applying T1–T43 and the 16 crosswalk rows:

    $ python3 lint.py --chapters
    chapters: 62 file(s), 4625 label(s) defined, 0 hit(s)
    $ python3 assemble.py --check
    labels 4625, computations cited 0, problems 0

Further checks:

- **Resolved lines.** No line of chapter 33 in the assembled PAPER.md exceeds 121 characters. The conservative test, with
  each new label resolved as "Proposition 49.999", also finds none.
- **Crosswalk.** 197 rows for 197 labels, in chapter order.
- **Typography.** No backslash.
- **The proof file.** Applying its 43 old/new pairs to the current chapter reproduces the checked scratch chapter
  exactly.

The preprint was read from the alphaXiv full text of arXiv:2606.27658v2, saved at
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/sources/hin26a-v2-fulltext.txt.
The proofs in the paper do not depend on it.
