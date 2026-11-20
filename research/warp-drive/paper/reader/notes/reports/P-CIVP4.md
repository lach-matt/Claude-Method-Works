# Report: P-CIVP4, fix round (Tier 4: data of any size reaching the axes)

File: `research/warp-drive/paper/reader/proofs/P-CIVP4.md`, 1292 lines, md5 0e0ef24b527d9ae78536e0208f86b9b5 (was
436d17be962a9c34358832bfce3c00b9). Review applied: notes/reviews/R-P-CIVP4.md (5 Major, 13 minor, 16 nits). Old texts of
the Placement are taken from the chapters at HEAD 481f86a1 (Tiers 1, 2, 3 and the null-shell section merged). No chapter,
crosswalk, review or other proof file was edited; nothing under method/, drive/, extracted/ or recovered/ was read;
nothing was committed; assemble.py was run without --check only in the scratch tree.

## Labels

No label of this file is renamed or removed; none is added. The 31 labels are those of the first version
(lem:class-leaf-reference, eq:class-leaf-lipschitz, eq:class-leaf-wise; sec:civp-axes and its 28 labels). proofs/P-CIVP5.md
(Tier 5) cites none of them. The three pending markers are resolved: [[pending:tier3-section]] -> [[sec:loc-axis]],
[[pending:tier3-theorem]] -> [[thm:loc-axis]] (a) (theorem (c), its proof, rem:civp-axes-scope (i)),
[[pending:tier3-theorem-general]] -> [[thm:loc-axis]] in the rewritten Corollary P, which is now unconditional.

## The term "class solution in double-null form"

Defined once, in sec:civp-axes-data (file line 246 ff., the paragraph after eq:civp-axes-raychaudhuri), worded as P-SHELL's
definition, with a sentence that on sets D ⊂ F these are Tier 3's "class solutions in the gauge through the axes"
(def:loc-axis-data). The paragraph after eq:civp-axes-form now proves the equivalence of the two forms (a smooth invariant
metric of the form eq:loc-double-null off the axes is in natural double-null form, Ω² > 0 and γ > 0 at the axes by
nondegeneracy). All 21 occurrences of "class solution(s) in the gauge" in Block B now read "in double-null form", except
the two that name Tier 1's term. Since sec:civp-axes precedes sec:loc-shells, Placement item 10 turns P-SHELL's second
definition (83:3282–3286 at HEAD) into a reference to sec:civp-axes-data with the same content.

## Major findings

1. Shift across N_i: applied as written (lem:civp-axes-jets statement, the "On N_i" paragraph, prop:civp-axes-formal (d)).
   Added: (i) says the shift of the exchanged form solves a linear ODE; the "Vanishing to infinite order" step says why
   E(L̲, ·) = 0 on N_i.
2. Time chart: applied (y := e^(v−μu)ω, 4μΩ² > γ(b, b) on R_ε). Changed: the extension now also carries the densities and
   keeps 4μΩ_e² > γ_e(b_e, b_e) by the choice of ε_1 ≤ ε; Φ's image is stated to contain the set 𝒲 of points within
   ε_1/2 of R′, where Ũ and U are defined (needed for the localisation of Major 3).
3. Non-local term: applied with W := U + χ_𝒩(Ũ − U) and (b′) for (U, W), D := D_t; covers both cases. Changed where the
   replacement was not quantitative: the cut-off χ_𝒩 has derivatives O(η_2^(−i)), so I use Taylor's formula at order
   k + 2 (Ũ − U = O(s^(k+2−j)) near R′ ∩ {t ≤ t*}) to get W − U = O(η_2²) in C^k; the displacement of the leaves of W from
   those of U is then C″η_2² ≤ η_2/4, which is what puts them where W = Ũ. D_t lies within η_2/8 (not /4) of
   R′ ∩ {t ≤ t*}; η′ := η_2/8. Time steps renamed θ, θ_1, θ′ -> η_1, η_2, η′ (nit 11); minor 13 folded in.
4. Criterion: applied with the replacement's structure. Changed: uniqueness is applied on D_max ∩ 𝒬 ∩ {u < λ_u, v < λ_v}
   (relatively open in the rectangle of the extended edges, which may pass the far sides of Q) and extended by
   continuity; the relative openness of D_max ∪ 𝒬 gets its reason. Also changed, against the review's parenthesis: part
   (b) of lem:civp-axes-extension bounds the mixed derivatives ∇̊^i∂_s^j with i, j ≤ m separately (total order 2m + 1),
   and part (d) raises the total order by one, so the hypothesis of the criterion and of thm:civp-axes (d) is now
   "derivatives of total order at most 12k + 46" (was 6k + 26). Faces Step 0/3 were made consistent (K′ over
   i + j ≤ 2m + 8, K″ over i, j ≤ m + 3, L(η) for ∇̊^i∂_u^(m+4)).
5. Block A complete without chapter 81's base proof: (a) is "the proof of lem:class-leaf-differences (a) with changes
   (i)–(vii)", (vi) the zero-order bound by the radial form (δh(0) = 0, step One leaf with (U, V)), (vii) the integration
   over axis points; (b) is proved as (b′) with D := Σ_τ. P-CLD.md does not exist yet; when it reports, (vi)–(vii) can
   cite its labels instead. No chapter 81 placement item for the base proof.
   Added for (b′) to apply in the corner and uniqueness proofs, where states are defined only near the region: the lemma
   now fixes r_* ∈ (0, ρ1(p)/4] and takes all bounds on 𝒰_(r_*) (r_V ≤ r_*/2, δ_𝔐 ≤ r_*/16); (a), (b) hold for
   δ ≤ δ_V := min(r_V/8, δ_𝔐 for 2𝔐_V and c/2). Corner Step 2 and uniqueness Step 4 choose r_* and δ accordingly.

## minor findings and nits

All applied. Where I changed a replacement: minor 3 and 4 rebased on HEAD with Tier 3 and the null shells merged (items
4–9 keep the Tier 3 and null-shell clauses; item 4 drops only the false clause "No development is asserted for cone data
that differ from the background's near an axis and are not near the background's" and says what thm:civp-axes adds);
minor 5: item 2 is now "no change" (Tier 3's merged clause is the one copy), and the line-9 clause was reverted since Tier 3
is placed; minor 10: the constant in |X_0 − X| is 2Λ′, and the points with |u|, |v| ≤ d are within √2 d of N; minor 12:
"have a neighbourhood in F contained in G" replaces "at positive distance from the boundary of G" (that wording allowed
Q_0 to touch the side v = V1 of Q, where the margin fails), and the finite-union part is proved (slightly larger
rectangles, interiors relative to the least containing rectangle). Nit 14 also fixes κ′ := κ/(4Λ²). Lemma
civp-axes-extension (c) now asks extensions on [λ, λ + 1/2] and gives ℓ ≤ 1/2, matching what (b) supplies. Nit 11: the
rectangle sides are a_R, b_R in the uniqueness proof, the criterion, thm:civp-axes (d), (e) and cor:civp-axes-cones.
rem:civp-axes-scope (iv) now points to thm:loc-shells for null shells.

## Placement (13 items)

1 Block A after rem:class-leaf-numerics; 2 no change to lem:class-leaf-differences; 3 Block B after sec:loc-axis, before
sec:loc-shells; 4 ch83 last sentence of the paragraph after rem:loc-cone-scope (83:728–730); 5 ch83 opening (83:16);
6 ch90 (90:219–221); 7 ch03 More families (03:381–383); 8 rem:loc-cone-local-scope (83:1656–1660); 9 rem:civp-large-domain
(83:2403–2404); 10 sec:loc-shells definition -> reference (83:3282–3286); 11 optional pointer in rem:loc-axis-scope (i)
(83:3237–3238); 12 unchanged; 13 Appendix A (no entry; Stein's operator now only in the corner proof). Crosswalk: 31 rows,
tab-separated, source "paper/reader/proofs/P-CIVP4.md@PENDING:N", plus notes for the existing rows touched.

## Checks (scratch merge of `git archive` HEAD 481f86a1 with all 13 items applied)

Every old text found exactly once as whole lines. `lint.py --chapters`: 62 files, 4864 labels, 0 hits.
`assemble.py --check`: labels 4864, problems 0. Full assembly (scratch only): 0 problems, no line of PAPER.md over 121
characters; the section is 53.7, lem:class-leaf-reference is Lemma 51.30; `lint.py --paper`: 0 hits. `lint.py` on the
proof file: only cross-file labels, file names and long lines in the Crosswalk section. Own checker: no line of Blocks A,
B or the Placement over 121 characters raw or with labels resolved, no bad wrapped starts, no backslashes, 14 proofs and
14 ∎. All 31 crosswalk rows give the line of their label.
