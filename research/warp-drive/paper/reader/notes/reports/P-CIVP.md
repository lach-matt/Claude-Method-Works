# Report: P-CIVP (Tier 1 of the characteristic initial value problem)

File written: `research/warp-drive/paper/reader/proofs/P-CIVP.md`, 1188 lines,
md5 aa08312166da99581416a9753bad3c98. No chapter, crosswalk, Appendix A entry, bibliography file or
proofs/P-CIVP2.md was edited. Nothing under method/, drive/, extracted/ or recovered/ was read. Nothing was committed.
`assemble.py` was not run.

Checks run on the final file: every line is at most 121 characters, measured with Python len, both raw and with each
label replaced by a worst-case resolution ("Proposition 99.99", "(99.999)", "Section 99.99.9"); no wrapped line starts
with "+ ", "- ", "* ", "> ", "#", "=" or "|"; no backslash; labels lowercase; no label defined twice or colliding with a
chapter label; every [[...]] reference resolves to a chapter label or a label of this file. `python3 lint.py
proofs/P-CIVP.md` reports only "reference to undefined label" for chapter labels, which a single-file run cannot see
(proofs/P-K.md gives the same kind of output). 18 proofs, 18 end marks.

## 1. Structure

Block A (goes into sec:loc-cones after the proof of prop:loc-cones):

- lem:loc-cone-in (T2): the 𝒞_in analogue of prop:loc-cones in the gauge b = 0, with eq:loc-cone-in.
- thm:loc-cone-development (T3): cone data from S, near the background's in C^m, m = 6k + 21, band away from the axes.
  (a) a class solution in the gauge eq:loc-double-null on G_* = {uv ≤ δ_*²} ∩ [0, u_1] × [0, v_1], inducing the data;
  (b) equal to the background where ϑ < ϑ_a′ − 2C_0√(uv), ϑ > ϑ_b′ + 2C_0√(uv), or u < u_K and v < v_K, in particular
  where ϑ ≤ ϑ_a − η or ϑ ≥ ϑ_b + η; (c) estimate Cε in C^(k−4); (d) uniqueness near the background off the axes, and on
  all of G_* among solutions equal to the background near the axes.
- rem:loc-cone-scope: what the theorem does not give (smallness, axes, regularity with [LR20, Theorem 4.6] quoted, the
  domain).

Block B (a new section right after sec:loc-cones), the proof:

- sec:loc-cone-setting: corners, edges, the collar 𝒮 (eq:loc-cone-collar), backgrounds on 𝒮, class solutions in the
  gauge; def:loc-cone-data (cone data in any gauge, Ω free on both edges, b free on N_i, corner values free, the size in
  C^(m_0), m_0 = 6k + 18; cone data *of any sign*); lem:loc-cone-strips (the background of the chapter near the cones,
  including R ≥ 5 on 𝒞_out and R > 1.5 on 𝒞_in ∩ {u ≤ 7.2}).
- sec:loc-cone-equations-frame: eq:loc-cone-quantities, lem:loc-cone-frame (connection table), lem:loc-cone-ricci (frame
  Ricci components eq:loc-cone-frame-ricci, dust divergence, Bianchi identities eq:loc-cone-bianchi).
- sec:loc-cone-formal: lem:loc-cone-borel (Borel extension from two edges with a corner), lem:loc-cone-jets (all
  derivatives across the edges by linear ODEs along the generators, Goursat form eq:loc-cone-goursat, corner
  compatibility), prop:loc-cone-formal (the formal solution; constraints propagated to all orders by Bianchi).
- sec:loc-cone-reduced: time τ and chart (eq:loc-cone-time), region 𝒰 (eq:loc-cone-region), cut-offs, reference states,
  the new paragraph "The reference metric in case (II)", the modified system eq:loc-cone-modified;
  lem:loc-cone-system, lem:loc-cone-energy, lem:loc-cone-cauchy, lem:loc-cone-past, lem:loc-cone-support,
  lem:loc-cone-constraints, lem:loc-cone-gauge, lem:loc-cone-unique; then lem:loc-cone-extension (new),
  prop:loc-cone-local (rewritten as T1), rem:loc-cone-local-scope; then the proof of thm:loc-cone-development.
- Placement (items 1–10) and Crosswalk rows (Rows 1–36).

## 2. Status of each result

All proved in full in the file, in the paper's style:

lem:loc-cone-in, thm:loc-cone-development (a)–(d), lem:loc-cone-strips, lem:loc-cone-frame, lem:loc-cone-ricci,
lem:loc-cone-borel, lem:loc-cone-jets, prop:loc-cone-formal, lem:loc-cone-system, lem:loc-cone-energy,
lem:loc-cone-cauchy, lem:loc-cone-past, lem:loc-cone-support, lem:loc-cone-constraints, lem:loc-cone-gauge,
lem:loc-cone-unique, lem:loc-cone-extension, prop:loc-cone-local.

rem:loc-cone-scope and rem:loc-cone-local-scope are remarks (no proof claimed); the change of angle in
rem:loc-cone-local-scope is a stated reduction, not a separate result.

## 3. The Tier 2 interface (coordinator notes 1, 3 and 4; review R-P-CIVP2 §A)

Which labels discharge Tier 2's pending markers:

| Tier 2 marker | Label here | What it gives |
|---|---|---|
| [[pending:civp-tier1-theorem]] | thm:loc-cone-development | T3 |
| [[pending:civp-tier1-cin-cones]] | lem:loc-cone-in | T2 |
| [[pending:civp-tier1-local]] | prop:loc-cone-local | T1 |
| "the regularity index m of [[pending:civp-tier1-local]]" | m_1 := 2m_0 + 6 = 12k + 42 (k ≥ 6) | T4 |

T1 (prop:loc-cone-local). Stated as Tier 2's prop:civp-large-corner asks: a background on an open set 𝒪 (round two-dust
solution of eq:two-dust-limit), Q ⊂ 𝒪 with its 4d-neighbourhood Q′ compact in 𝒪; σ depends only on k, η, Λ, d and
bounds for σ_e, R_e, 1/R_e and their derivatives of order ≤ m_1 + 2 on Q′. For every rectangle
R = [u_c, u_c + λ_u] × [v_c, v_c + λ_v] ⊂ Q (corner anywhere in Q, any lengths), edge data with Ω arbitrary on both
edges, b arbitrary on N_o, b = 0 on N_i, q_in, q_out ≥ 0, agreeing on the corner sphere, satisfying Ric(∂_v, ∂_v) = q_in,
Ric(∂_v, ∂_ϑ) = 0 on N_o and Ric(∂_u, ∂_u) = q_out on N_i, equal to the background's off [2η, π/2 − 2η], with C^(m_1)
norms of the differences ≤ Λ and no smallness, there is a class solution in the gauge on
[u_c, u_c + min(λ_u, σ)] × [v_c, v_c + min(λ_v, σ)] × S³ inducing the data and equal to the background off
[η, π/2 − η]. σ is the same for every corner and independent of λ_u, λ_v. The proof is written in four steps, and Step 3
says explicitly where the smallness of the rectangle replaces the smallness of the data (residual R_II = O(σ) in H^k
about the formal solution Û, closeness O(σ^(1/(4k))) to Û).

Notation differences for the coordinator: Tier 2 writes l_u, l_v for the rectangle; prop:loc-cone-local writes λ_u, λ_v,
because l_u, l_v are the collar lengths of sec:loc-cone-setting. Tier 2 measures ln γ_ϑ, this file ϰ_1 = ½ ln γ_ϑ (a
factor 2 in Λ). With these, Tier 2's prop:civp-large-corner is prop:loc-cone-local with Q = Q1, and its written proof
(Tier 2 lines 404–418, the "three changes") can be replaced by a citation. Tier 2's m is m_1.

The gap reported by the Tier 2 writer (coordinator note 4: the old prop:loc-cone-local needed edge data δ_1 past the
rectangle with δ_1 ≤ min(l_u, l_v)/2 and σ depending on δ_1) is closed by **lem:loc-cone-extension**: the constraint
ODEs (Raychaudhuri as a linear equation for y = e^ϕ, and the Ric(∂_v, ∂_ϑ) equation for ∂_v b) are solved along each
edge beyond its end, after a Borel extension of the free functions at the end point with a fixed cut-off scale 1/4,
over a fixed length a_0 = a_0(Λ, η, k, background), with positivity of y kept by a Gronwall bound and the size of the
extended data bounded by C(Λ). In prop:loc-cone-local, δ_1 := min(d, a_0/3, δ_2) is fixed in terms of Λ, η, k, d and
the background, and every edge is cut or extended to length 3δ_1. The extended densities may be negative beyond the
given edges (a smooth nonnegative function on [0, l] need not have a nonnegative smooth extension, e.g. l − v), so the
file introduces "cone data of any sign" (def:loc-cone-data), checks that the Cauchy theory of chapter 81 does not use
the sign, and proves in lem:loc-cone-constraints that q_in ≥ 0 where u_in ≤ λ_v and q_out ≥ 0 where u_out ≤ λ_u
(densities are transported along P_A with a positive factor and P_A(u_A) = 0). So the solution is a class solution on
the rectangle.

T2 (lem:loc-cone-in): free data (ℓ_1, ℓ_2, ℓ_3, q_out) on 𝒞_in in the gauge b = 0, Ω the background's; the constraint
determines ϕ on every generator where e^ϕ stays positive; the background's off the band.

T3 (thm:loc-cone-development): (a) on G_* = {uv ≤ δ_*²} ∩ Q1, a past set; (b) equal to (g0, q̊_in, q̊_out) where
ϑ ≤ ϑ_a − η or ϑ ≥ ϑ_b + η, so off [η′, π/2 − η′] with η′ = 3η; (c) the estimate; (d) uniqueness only near the
background. Its data (Ω the background's) are cone data in Tier 2's sense.

T4: m_1 = 2m_0 + 6 = 12k + 42 is defined in the statement of prop:loc-cone-local ("the regularity index of this
proposition"); for k = 6, m_1 = 114. The theorem keeps m = 6k + 21.

General gauge (coordinator note 2): def:loc-cone-data, lem:loc-cone-jets and prop:loc-cone-formal hold for Ω given on
both edges, b given on N_i and any corner values. prop:loc-cone-local requires b = 0 on N_i (as T1 asks); a b given on
N_i is reduced to that case by the change of angle named in rem:loc-cone-local-scope. The dependence of σ is stated in
prop:loc-cone-local and explained in rem:loc-cone-local-scope.

## 4. Deviations from the outline (S-CIVP) and why

1. The CP12 wave-gauge data route (L1) was replaced by a double-null formal solution and a wave-map gauge whose
   reference metric is the formal solution's extension Ĝ, so that D(Ĝ) = 0 identically. This removes the re-derivation
   of [CP12, §3.1] in 4+1 with dust (risk R2) and makes the jets linear ODEs along the generators (no smallness).
2. The collar is built by a Borel extension from two edges (lem:loc-cone-borel) instead of a Whitney extension.
3. Uniqueness (L10) is proved off the axes near the background (lem:loc-cone-unique), and on all of G_* only among
   solutions equal to the background near the axes; no uniqueness is stated for prop:loc-cone-local.
4. Two cases share one proof: (I) small data on the long rectangle (the theorem) and (II) data of any size on a small
   rectangle (T1), the latter with the centre Û and the residual O(σ).
5. Regularity: m_0 = 6k + 18 (jets of order j in C^(m_0 − 4j), Ĝ in C^(k+3)); the theorem's m = 6k + 21; T1's
   m_1 = 12k + 42 because the extension of lem:loc-cone-extension loses half the derivatives.
6. Placement: the statements go into sec:loc-cones (Block A) and the proof becomes a new section of chapter 83
   immediately after sec:loc-cones (Block B), not a new chapter between 82 and 83: the proof uses chapter 83's gauge
   eq:loc-double-null, its background and prop:loc-cones throughout, and Tier 2 expects to follow it in the same chapter.

## 5. A gap found and closed in this pass

In case (II), with data of any size, the old draft took for granted that A^0 of the first-order system is positive
definite at the centre Û. That needs ∂_τ timelike for Ĝ, and 4Ĝ(∂_τ, ∂_τ) = −4Ω̂²(u + δ_c)(v + δ_c) + γ̂_ϑ b̂²(u + δ_c)²
can be positive for a large shift. The new paragraph "The reference metric in case (II)" in sec:loc-cone-reduced
proves, for b = 0 on N_i (so b = 0 at the corner), |b̂| ≤ C_b(|u| + |v|) and |b̂| ≤ C_b|v| where u ≥ 2δ_e, with C_b
independent of δ_e and δ_c (from the explicit form of the Borel sums), and hence 4Ĝ(∂_τ, ∂_τ) ≤ −2Ω̂²(u + δ_c)(v + δ_c)
once δ_1 ≤ δ_2(Λ, η, background). The faces of 𝒰 are spacelike for metrics close to Ĝ because dτ, du + κdv and dv + κdu
are timelike for every metric of the form eq:loc-double-null (sentence added to "Constants, coordinates and regions").
This is also why the old claim "any b on the ingoing edge" in prop:loc-cone-local was withdrawn: with a large b on N_i
the chart's ∂_τ fails to be timelike along N_i, and the reduction is the change of angle instead. A small fix in
prop:loc-cone-formal: γ_0 := min(1, the size), as lem:loc-cone-borel needs γ_0 ≤ 1.

## 6. Risks of S-CIVP §5

- R1 (jets, corner compatibility): resolved by lem:loc-cone-jets, Goursat form and induction in j + k.
- R2 (wave-gauge data with dust): avoided by the gauge relative to Ĝ (deviation 1).
- R3 (uniqueness on the past region with null boundary): lem:loc-cone-past, energy on a Lipschitz domain
  (lem:loc-cone-energy) with null faces, whose boundary terms are nonnegative.
- R4 (finite speed and explicit δ_*): δ_* = √c_+/2 with c_+ = (min(δ_1, η/C_0)/4)², C_0 = 2√2/R_min; angular faces
  ϑ = ϑ′_a − 2C_* e^(τ/2) spacelike since C_* ≥ e^(σ_e)/R_e. δ_1 itself is not given as a number.
- R5 (regularity count): m_0 = 6k + 18, m = 6k + 21, m_1 = 12k + 42, all stated.
- R6 (uniqueness by conversion): done through a wave map to Ĝ (lem:loc-cone-unique), off the axes.
- R7 (smallness and axes are real restrictions): stated in rem:loc-cone-scope and in the new texts of items 3, 4, 6, 7.
- R8 (chapter 81 consistency): only thm:class-kato-stability (a) (whole space) with rem:class-kato-local, thm:class-kato
  (a), lem:class-kato-linear, lem:class-composition and the energy argument of thm:class-kato (b)(i) are used; the
  domain form (b) is not used as a black box. The sign of the densities is not a hypothesis there (checked).
- R10 (literature): see §8.

## 7. Not closed

1. Uniqueness near the axes for general solutions (needs an axis theory); and no uniqueness statement for
   prop:loc-cone-local.
2. σ of prop:loc-cone-local depends on the background (bounds on Q′), as rem:loc-cone-local-scope explains: the solution
   is the background near the axes, the frozen part of the modified system uses it, and the angular localisation uses
   C_*. A background-free statement needs a local theory at the axes.
3. δ_1, δ_*, ε_0, σ are not numerically explicit.
4. A shift given on N_i in T1 is handled by a stated change of angle (rem:loc-cone-local-scope), not by a separate
   proved lemma; Tier 2 does this change itself in its corner step, so T1 does not depend on it.
5. Low-regularity densities (bounded or measure-valued) are not covered (rem:loc-cone-scope (iii)).

## 8. Citations verified

- [Ren90] A. D. Rendall, Proc. Roy. Soc. London Ser. A 427 (1990), no. 1872, 221–239, doi:10.1098/rspa.1990.0009:
  bibliographic data and the quoted opening sentence of the abstract checked against ADS and JSTOR listings (the
  reference-checking service was refused by the proxy). Quoted only as "[Ren90, p. 221]" for the method; no lemma
  number of it is cited. New bibliography entry given in Placement item 10.
- [LR20, Theorem 4.6, p. 29]: wording checked against the arXiv text (version 1), quoted in rem:loc-cone-scope (iii)
  for comparison only.
- [CTG23, Theorem 1.1] (thm:std-ctg-neighbourhood): already in the paper; used in prose only.
- No new Appendix A entry (Placement item 9).

## 9. Placement texts that must be merged with Tier 2

Items 3 (chapter 83 opening, lines 8–9) and 4 (the paragraph at lines 593–600) are also replaced by Tier 2; the
coordinator merges the two new texts. Item 6's line numbers were re-measured: the bullet's last lines are now 373–374 of
chapter 03 (another agent edits that chapter).
