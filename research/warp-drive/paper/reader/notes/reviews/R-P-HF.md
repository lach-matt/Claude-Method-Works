# R-P-HF: independent reading of proofs/P-HF.md (L3-L5, the weighted bootstrap, thm:tl5-hf)

File read: proofs/P-HF.md, md5 f5d9cd38747813f55dd114bba8707e27, 1271 lines (chapter text 1-971, Placement 973-1176,
crosswalk rows 1178-1271); writer's report notes/reports/P-HF.md. All line numbers below are lines of that file unless
marked "87:". Chapter 87 read at HEAD ea33ac6a and rechecked at caaab92d (its md5 eeaa48e1b1082b332cca6b38255cb0da is the same as
at 8d583306 and edafc288: P-H29 is merged, sec:tl5-wg 87:1947-2758, sec:tl5-dn 87:2759-3047, sec:tl5-beyond 87:3049). Also read for the
coordinator's questions: notes/reports/N-APP1.md section 8 (2), and the statements of lem:tl5-xt-seed-jets and
lem:tl5-xt-order of proofs/P-XT.md (md5 a9e3d284...), which I have not reviewed and use only as stated.

## Verdict

**NOT CONFIRMED.** 2 Major, 10 minor, 10 nits.

The analysis re-derives: every identity of L3 and L4, the expansion of -2Ric^W, the commutator with its D𝓡̂ term, the
null structure, the recovery constants, Lemma G's majorant 𝔠_n, the face Sobolev constants, the bounds at a point, the
quasilinear current and the bootstrap inequality, with three independent computer-algebra checks (below). The two
Majors are (M1) hypothesis (a) of thm:tl5-hf, which no explicitly given background can meet and which asks one order
more than the estimate uses, and (M2) the persistence lemma, which applies lemmas at levels where their hypotheses
fail. Both have the same repair: the data on N₀ are carried as data, as the energy identity already does. Exact texts
for every change are in the last part of this review. They are applied together in a scratch merge, and the merge
passes lint.py --chapters, assemble.py --check, assemble.py and lint.py --paper with 0 hits and no line over 121.

## The three questions put to this reading

### 1. The level N (the key deviation)

**Conclusion: the writer is right that the plan's level-3 closing does not work, and right that the file's own scheme
needs N ≥ 5 for the estimate. Level 3 cannot be repaired. Level 4 is reachable, but only with product estimates the file
does not contain. N ≥ 6 is needed only by the file's way of proving (H2), not by the estimate.**

(a) *Level 3 is insufficient for the theorem as the paper uses it, by a counting argument no choice of method avoids.*
The last statement of thm:tl5-hf, the passage to the double-null gauge, needs |D̂²h| bounded at every point:
thm:tl5-dn needs the C² distance ε on the slice (eq:tl5-dn-eps, |α| ≤ 2), and
lem:tl5-hf-conversions (b) bounds ε by sup max(|h|, |D̂h|, |D̂²h|). A level-3 energy controls Ψ_I, |I| ≤ 3, in H¹ of
the four-dimensional faces. With the equation, that puts h in H⁴ of the faces and D̂²h in H². In four dimensions H²
does not embed in L^∞; this is the borderline case. So no pointwise bound of D̂²h follows from level-3 energies,
whatever commutators, null structure or traces are used. This is the plan's claim (G0's C_S, |∇²h|_∞ from level-3
fluxes), and it is false. The writer's finding 1 is correct in its conclusion. (The existence part alone, the reduced
solution on D^κ, does not need |D̂²h| at a point, but at level 3 it needs the L⁴ estimate of (d).)

(b) *The writer's stated reasons are not the operative ones in this file.* The report gives three reasons for level 3
failing: the transverse derivative of the top level on null cones, the twist π^T(ê₄, f) ≠ 0 with the orbit-leaf block
of π^K, and the quasilinear H^uu term. The faces of this file are not null cones. They are the tilted faces, and on
them ε₁ = (e_o + κ′e_i)/(1 − κκ′) controls every first derivative, the transverse one with weight κ′ (𝔨₁, 𝔨₂ of
lem:tl5-hf-sobolev and lem:tl5-hf-linfty). The linear bulk, which is where the twist and the null structure matter, is
absorbed pointwise by the rates whatever its size. So the null structure (verified: lem:tl5-hf-fields (c), with
π^T(ê₄, ∂_x) = c e^(2ζ) ∂_v b̂, the twist) neither causes nor cures anything at the level of the count. A different
commutator set (∂_u, ∂_v or E₁ added to Γ) removes the recovery step but not the Sobolev loss. The operative count is
the one in rem:tl5-hf-level: Ψ_B is bounded at a point for |B| ≤ N − 2 (two rotations), D̂Ψ_B for |B| ≤ N − 3 and
D̂²Ψ_B for |B| ≤ N − 4 (each transverse derivative recovered from one more commutation). Because of the axes, two
rotations cannot be lowered: near an axis a G-invariant function is radial in a plane, and radial H¹ functions in the
plane are unbounded. T²-invariance does not help either, since the Ψ_B with letters K₁₃, …, K₂₄ are not invariant.

(c) *Within the file's scheme N ≥ 5 is sharp.* The file bounds every product by one factor at a point and the other
factors in L² (lem:tl5-hf-quadratic). A product D̂Ψ_B D̂Ψ_(B′) with |B| = |B′| = 2 at N = 4 has neither factor bounded
at a point. In four dimensions D̂Ψ_2 is in H² of the face and not in L^∞, so this is not a weakness of the S³ route.
lem:tl5-hf-quadratic's "at most one high factor" needs 2N − 4 > N, so N ≥ 5.

(d) *Level 4 closes with a standard estimate the writer did not use: an anisotropic Hölder split on the faces.* On a
face Σ₁(t, b) put one factor in L²_v L^∞_ω and the other in L^∞_v L²_ω. The first uses the file's own S³ inequality
(lem:tl5-hf-sphere) on the leaves. The second uses the file's own trace along the face, the 𝔈-argument of
lem:tl5-hf-sobolev without the rotations. At N = 4 the products that the pointwise scheme cannot handle are:

- D̂Ψ₂ · D̂Ψ₂. Here K′K D̂Ψ₂ ~ D̂Ψ₄ is in L² of the face, and ∂_γ D̂Ψ₂ ~ D̂²Ψ₂ is recovered from D̂Ψ₃.
- ℒ³H · D̂²Ψ₁. Here ∂_γΨ₃ is in the flux, and K′K D̂²Ψ₁ ~ D̂²Ψ₃ is recovered from D̂Ψ₄.

The other products have a factor bounded at a point: Ψ_B for |B| ≤ 2, D̂Ψ_B for |B| ≤ 1, D̂²h. |H| and |D̂H| are bounded
at a point, which the recovery and the current 𝔟 need. D̂²h is bounded at a point, which thm:tl5-dn needs. So a level-4
version is possible. It needs a mixed-norm Lemma G and a bootstrap whose smallness quantity contains mixed norms, and
both are new written mathematics. At level 3 the split ℒ²H · D̂²Ψ₁ would need in addition an L⁴ inequality on S³
(H¹(S³) ⊂ L⁴, with a published sharp constant). Level 3 still fails at (a).

(e) *N ≥ 6 is an artefact of the proof of (H2).* lem:tl5-hf-persistence wants each monomial at level m to be linear in
the quantities not yet bounded by level m − 1, and that needs m ≥ 7. (H2) is qualitative. A Grönwall argument, or the
mixed norms of (d), gives it at the level of the estimate. As written, the file's statement at N ≥ 6 is correct (after
M2).

*Consequence for the plan.* Accepting N = 6 is legitimate mathematically, but it is the expensive choice. There are
Σ_(j≤6) 7^j = 137,257 words. 𝔠_6 involves F₆ = 4683, 𝔤₀^7 and (Λ + 1)^6. Then 𝔤_N, μ^(−N/2), the jets of ĝ to order
N + 3 = 9, and 4(N + 1) = 28 rows of 𝔅_N; N-APP1's table shows the coefficient count growing by 8-12 % a level. Whether
to invest in a level-4 version is the coordinator's and the author's decision. The file never claims that lower levels
are impossible. rem:tl5-hf-level should say that its counts belong to the method; that is minor m6.

### 2. Hypothesis (a) of thm:tl5-hf (raised by N-APP1 and P-XT)

**Judgement: (a) is a true hypothesis but not one any explicitly given background meets. It also asks one order more
than the estimate uses. The theorem should carry the data on N₀ as data (repair (i) as the form of the statement), and
the background should carry the development's v-jets of orders 4..N + 1 on N₀⁺, enclosed like the N₁ data (repair (ii),
which makes those data small). The coordinator's expectation is right, with one order less than (a) would demand.**

- *What (a) demands.* G^♯ − ĝ is to vanish to order N + 1 on N₀. By lem:tl5-xt-order (c), that holds when ĝ − g′
  vanishes to order N + 2 on N₀⁺, g′ being the double-null development. My own derivation from lem:tl5-wg-tension and
  lem:tl5-wg-wavemap gives the same loss of one order: Υ(g′) loses one derivative, and dΨ loses one more against the
  gain of the transport. By lem:tl5-xt-seed-jets (b) and N-APP1, g′'s fourth v-derivatives on N₀⁺ are not the seed's.
  They and the higher ones solve linear transport equations along N₀⁺, and the env term (π/3)⁴(v − 1/2)⁴ makes them
  of order one. So (a) holds exactly only for a background that reproduces those transported jets of orders 4..N + 2
  exactly. A background printed from finitely many coefficients reproduces them only up to an enclosure error. A
  background seed + (v − 1/2)^κ G gives G^♯ − ĝ only to order 2. That fails (a) for every N ≥ 2, so at level 3 too.
- *What the estimate uses.* Only derivatives of G^♯ − ĝ of order at most N on N₀. Ψ_I, |I| ≤ N, enters the flux on
  N₀, and the low quantities (order ≤ N − 2) enter the start of the face trace. Order N + 1 enters only the step
  m = N + 1 of lem:tl5-hf-persistence, where no smallness is needed.
- *Repair (i) alone, with the raw mismatch, cannot close.* The order-3 and order-4 derivatives of G^♯ − ĝ on N₀ would
  be of order one, while 𝔰₁ ≤ c_* κ_m/2 ≤ 1/16 and A_w must satisfy 8A_w S_F < 1.
- *Repair (ii) alone is not a statement P-HF can use, since no enclosure is exact.* The enclosure error has to enter
  the theorem somewhere.
- *The right statement* replaces (a) by "η₀ < 𝔰₁" and keeps the N₀ terms. Here η₀ := sup over N₀ of max(𝔰,
  |Ψ_C| (|C| ≤ N), |D̂Ψ_C| (|C| ≤ N − 1)), computed from G^♯ on N₀ (derivatives of order at most N). The flux of the Ψ_I
  and of 𝔟 through N₀ is added to δ_w², and C_(∞,0)η₀ is added to 𝔰_* and to 𝔯_w. These are exactly the terms the
  energy identity and the face trace produce when the vanishing is dropped. The identity already contains
  ∫_(N₀∩Q) e^(−φ) e_i, and the trace acquires its value at v = 1/2.
- *What this gives.* With the jets of orders 4..N + 1 carried exactly, lem:tl5-xt-order (c) with m = N + 1 makes every
  N₀ term zero. With enclosed jets, the N₀ terms are of the size of the enclosure error, beside δ_w. This is N-APP1's
  (ii) with κ = N + 2; the original (a) would have required κ = N + 3.
- *Uses of (a), all repaired below.* The data term of the bootstrap (δ_w, M1.17). The flux through N₀
  (prop:tl5-hf-linear, cor:tl5-hf-level0, prop:tl5-hf-linear-n, Step 2 of the bootstrap). The start of the face trace
  (lem:tl5-hf-sobolev, eq:tl5-hf-cs-r, lem:tl5-hf-linfty). The start of Step 1 (𝔰 = 0 on N₀ becomes 𝔰 ≤ η₀).
  lem:tl5-hf-persistence (M2). lem:tl5-hf-conversions does not use (a): its bound is on the slice over B ∩ M_σ, from
  the low quantities, and needs no change.

### 3. Placement anchors at HEAD

Every old text of items 2-7 occurs exactly once, as whole lines, in chapters/87-ten-l5.md at HEAD (ea33ac6a, and caaab92d, same chapter). **No item
needs re-quoting.** The line numbers in items 1-7 are stale; the items say the numbers only help to find the place, but
they should be updated (nit n10):

- item 1: after 87:3145;
- item 2: 87:3051-3053;
- item 3: 87:3055-3071;
- item 4: 87:3073-3084;
- item 5: 87:3086-3112;
- item 6: 87:3114-3117;
- item 7: 87:3119-3129.

The scratch merge was made from a git archive of HEAD in
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/rphf/. It
applies items 1-7 and the 84 crosswalk rows, and gives:

- lint.py --chapters at HEAD caaab92d: "62 file(s), 5040 label(s) defined, 0 hit(s)", where clean HEAD has 4956, so 84
  new labels;
- assemble.py --check: "labels 5040, computations cited 0, problems 0";
- assemble.py: clean;
- lint.py --paper: "PAPER.md: 0 hit(s)".

The same four checks pass, with the same counts, when all the replacement texts below (including item 8) are applied
on top.

No line of P-HF's chapter text or placement texts exceeds 121 characters, and no wrapped line starts with a marker.
The only such starts in the merged chapter are the pre-existing lists at 87:367 and 87:2944. One placement item is
missing: item 6 deletes the paragraph that defined G, ε_r and "the closing condition 4F²G ε_r < 1", but
rem:tl5-constants (87:3143-3145) still uses them. See minor m8, which gives an item 8.

## Major

### M1. Hypothesis (a) cannot be met by an explicit background, and the vanishing on N₀ is built into four lemmas (lines 264, 274, 287-288, 305, 497, 505-506, 562-592, 695-743, 813-838, 845-886, 934, 958-964)

*What is wrong.* See question 2 above. thm:tl5-hf (a) and the identical hypothesis of prop:tl5-hf-bootstrap
(lines 835-836) require G^♯ − ĝ to vanish to order N + 1 on N₀. The lemmas the bootstrap uses assume the corresponding
vanishing: prop:tl5-hf-linear "each vanishing on N₀", cor:tl5-hf-level0, prop:tl5-hf-linear-n "partial derivatives of
order at most N vanish on N₀", lem:tl5-hf-sobolev "A = 0 on N₀", eq:tl5-hf-cs-r, and lem:tl5-hf-linfty "of order at
most N + 1 vanish on N₀". The theorem is correct as stated, but its hypothesis (a) is not attainable for the
backgrounds the paper needs, so it cannot be applied. A raw relaxation would not close either.

*Repair.* Replacements M1.1-M1.27 below. They:

1. drop the vanishing from prop:tl5-hf-linear, cor:tl5-hf-level0 and prop:tl5-hf-linear-n, putting the N₀ flux into
   Y_d (already present in eq:tl5-hf-identity);
2. give lem:tl5-hf-sobolev and eq:tl5-hf-cs-r the term at v = 1/2, an integral over the leaf S_a := {a} × {1/2} × S³,
   with constant C_(S,0)² = 6C_(S³)² 𝔭₂ 𝔴⁴ sup_(S_a) 𝔳⁴;
3. define η₀ in lem:tl5-hf-linfty and add C_(∞,0)η₀ to eq:tl5-hf-linfty, with C_(0,0)² = 86π² C_(S,0)² and
   C_(1,0)² = 516π² C_(S³)² 𝔭₃ 𝔴⁶ sup_(S_a) 𝔳⁶ (1 + 6Λ)²;
4. add the N₀ flux to δ_w², and C_(∞,0)η₀ to 𝔯_w and 𝔰_*;
5. replace (a) by η₀ < 𝔰₁, and add η₀ < 𝔰₁ to eq:tl5-hf-smallness.

Each new constant is derived as in the existing proofs:

- 43 words J times ∫_(S_a) dω = 2π², times 6 C_(S³)² 𝔭_r 𝔴^(2r) 𝔳^(2r);
- |ℒ^J D̂Ψ_B| ≤ (1 + 6Λ)η₀ on S_a by (ii) of the proof of lem:tl5-hf-quadratic;
- 𝔰 ≤ 𝔧 ≤ η₀ on N₀ starts Step 1;
- the densities of J̃ on N₀ are at most e_i[Ψ_I] + 2Ω̂²|dv(𝔟)|.

When every Ψ_I vanishes on N₀ the new terms are zero and the old statements return.

### M2. lem:tl5-hf-persistence applies prop:tl5-hf-linear and lem:tl5-hf-linfty outside their hypotheses (lines 917-923)

*What is wrong.* The induction step for P(m), m ≥ N + 1, cites [[prop:tl5-hf-linear]] for the level-m energies and
[[lem:tl5-hf-linfty]] for L_m. Both assume that the fields vanish on N₀. Even under (a) as stated, this vanishing holds
only up to order N + 1, while for m ≥ N + 2 the Ψ_I with |I| = m involve derivatives of order m ≥ N + 2. So the step is
unproved from m = N + 2 on.

Two smaller faults are in the same lines:

- prop:tl5-hf-linear is stated for J, not for J̃ = J − 𝔟.
- The admissibility matrix "(1 − ϑ)⁻¹ 𝔅_m + 𝔊 diag(E_o + E_i)" has the constant outside (1 − ϑ)⁻¹, where absorbing
  𝔊(e_o + e_i) needs (1 − ϑ)⁻¹(𝔅_m + 𝔊(E_o^m + E_i^m)). The size is also wrong: it needs the m + 1 diagonal blocks.

*Repair.* With M1's lemmas, which carry the N₀ terms in general, replacement M2 below states the step correctly.
The N₀ fluxes at level m are fluxes of derivatives of G^♯ of order at most m + 1, and need no smallness. The rest of
the persistence lemma's last paragraph is minor m9.

## minor

- **m1** (lines 3-5). The lead says the estimate gives "the hypotheses (H1)–(H3)". It gives (H1), (H2) and (H4). (H3)
  is the closing condition, assumed in (c) and not proved, and the file rightly says it proves no closing (lines
  960-963). So the lead overclaims. Replacement m1.
- **m2** (lines 45-46, used at 353-354). "T is the static Killing field ∂_v + (f(−u)/2) ∂_u of [[lem:tl5-seed]]":
  that lemma does not state it, and its proof gives the field only as ∂_t in other coordinates. Replacement m2 proves
  it from lem:tl5-seed (b) and its proof of (c). I checked it: T(R) = 0, T(e^(2W)) = −c′e^(2W), ℒ_T(du dv) = c′ du dv.
- **m3** (lines 24, 543). "b̂ = (1 − x²) s" is not proved for a general background, and "s" is used in three other
  senses: D^κ_s, the source s of prop:tl5-hf-linear and s_N. It is used only in 𝔴², where c²(1 − x²)s²/(2|T|²) =
  2c²|b̂∂_x|²_(γ₀)/|T|², which is smooth because b̂∂_x is the shift vector field (lem:tl5-cip-form (a)).
  Replacements m3a, m3b.
- **m4** (lines 724-725). "𝔧 ≤ max(𝒥₁, M₂)" is false: 𝔧 contains |H|, and |H| ≤ 2|h| ≤ 2𝒥₁ only. The conclusion
  M₂ ≤ 2(k₁ + 1)𝒥₁ + 2k₂ max|ℒ^J(2R̂ic)| survives exactly with 2𝒥₁ + M₂ in its place (the bootstrap, line 872, already
  uses 2𝒥₁ + M₂). Replacement m4.
- **m5** (lines 234-235). "rates that satisfy [eq:tl5-hf-admissible] with κ = κ′ = 0 satisfy it for all κ, κ′ ≥ 0":
  false for non-monotone rates, because the arguments τ₁(p) and τ₂(p) move with the tilt. It is true for
  nondecreasing rates. It is unused, but stated. Replacement m5.
- **m6** (lines 966-971). "at the next level the same count, with the bounds of level N − 1 only, needs N ≥ 6": at
  level N + 1 the bounds used are those of level N, and the count is 2(m − 3) > m with m = N + 1 ≥ 7. With bounds of
  level N − 1 the count would need N ≥ 8. "each using two rotations or one face derivative" misstates the loss. The
  remark should also say that its counts belong to this way of bounding products (question 1). Replacement m6.
- **m7** (Placement item 4, lines 1060-1061 and 1065). Two errors:
  - "C^(1,1)-distance": thm:tl5-dn's ε is the C² distance (eq:tl5-dn-eps, |α| ≤ 2), and the theorem itself says
    "C²-distance". The crosswalk row lem:tl5-hf-conversions (line 1255) says "C^(1,1)" too; it should say "C^2".
  - "Of the regions D^κ_s it uses only that they increase with s and that a solution … restricts": the proof also uses
    that D^κ_(s̄) is the closure and that limits pass ("I is closed"), as rem:tl5-wg-continuation lists.
  Replacements m7a, m7b.
- **m8** (missing Placement item; 87:3143-3145). After item 6, rem:tl5-constants still says "the closing condition
  4F²G ε_r < 1 asks a residual ε_r of order 10⁻⁶⁸/G", but G and ε_r are no longer defined anywhere. Add an item 8 with
  replacement m8. Item 1's anchor, "after the last line of rem:tl5-constants", is unaffected.
- **m9** (lines 925-928). "apply [[lem:tl5-hf-recovery]] to D̂^(k−2)Ψ_B in place of Ψ": that lemma is stated for
  symmetric 2-tensors and the operator L̂. The equation for □̂D̂^(k−2)Ψ_B is not derived, and "P(k + 4)" does not
  match an induction in k. Replacement m9 writes the argument out.
- **m10** (line 667). "[Lie differentiation] of one with Ψ_B two": a monomial with two background factors and Ψ_B gives
  three monomials. The recursion m_k ≤ 4m_(k−1) + 7, and with it β₂ and 𝔠_n, stays true. With a_k, b_k, c_k the
  numbers of monomials of the three kinds, m_k = 4a + 2b + 3c + 7 ≤ 4m_(k−1) + 7. The justification as written is
  false. Replacement m10.

## Nits

- **n1** (lines 526, 531). Since 1 + n(n + 2) = (n + 1)², C_(S³)² = Σ_(m≥1) 1/(2π²m²) = 1/12 exactly (numerically
  0.0833333). This removes an enclosure from L7's list. Replacements n1a, n1b.
- **n2** (line 674). ℒ^B ĝ = ℒ^(B′)π^Z holds for B = (B′, Z), the last letter acting first, not for B = (Z, B′). The
  bound is unaffected.
- **n3** (line 314). In rem:tl5-hf-weight φ must be a function of (τ₁, τ₂); otherwise dφ(J) has angular terms.
- **n4** (lines 217-218). "if T is Killing … the principal term vanishes": the first-order blocks from 𝔇 remain,
  because E₀ is accelerated. Say which term vanishes.
- **n5** (lines 763-764). "𝔮_H is the sum of the six remaining terms": there are six, plus the commutator term, which
  the bound does include.
- **n6** (line 793). "with r = 2 and c ≤ 1" should read "c ≥ c_*".
- **n7** (line 562). lem:tl5-hf-sobolev should assume A of class C¹. This is included in M1.7.
- **n8** (line 948). lem:tl5-continuation needs A > 0, and A_w = 0 is possible (R̂ic = 0, data equal to ĝ). In that
  case ĝ is the solution. Replacement n8.
- **n9** (line 701). ‖𝔄_CJ‖ and ‖𝔔_CJ‖ are used but not defined; def:tl5-hf-coupling defines only ℭ and 𝔮.
  Replacement n9.
- **n10** (Placement items 1-7). The line numbers are stale; the HEAD numbers are under question 3.

## Observations (no change required)

- In the proof of prop:tl5-hf-linear (line 297) the Cauchy-Schwarz step gives ℰ(a′, b′) ≤ Y_d² + Y𝒮, not 2Y𝒮.
  The stated bound is true, but the sharp one gives Y ≤ Y_d + 𝒮. Carried through Step 3 of the bootstrap (line 883,
  "2Y_s ε_w"), it would give A_w = √2δ_w + 2ε_w in place of √2δ_w + 4ε_w. I report it because the closing is
  numerical; changing it is the coordinator's call.
- The writer's report finding 3 says (X), (T) and (W4) are hypotheses about the background. They are hypotheses of
  thm:tl5-wg-data, correctly not claimed in P-HF.

## What I checked and found correct

- **L3.** I re-derived the following and found them correct:
  - |T|, E₀, E₁ and eq:tl5-hf-null-pair, and lem:tl5-hf-khat (boost with e^β = c^(−1/2));
  - eq:tl5-hf-dk with D_i, 𝔇_V (k⁻¹ = ĝ⁻¹ + 2E₀ ⊗ E₀), and lem:tl5-hf-densities with eq:tl5-hf-coercive;
  - lem:tl5-hf-divergence: every term of eq:tl5-hf-bulk, including the tensor commutator term and both 𝔇 terms;
  - lem:tl5-hf-identity: the determinant −4Ω̂⁴e^(2ζ), the volume 2Ω̂² dμ du dv, Stokes on P × S³ with no axis term,
    face densities ε₁ and ε₂, and dφ(J);
  - rem:tl5-hf-blocks, all four lines and div 𝒵;
  - copositivity ⇔ PSD for nonpositive off-diagonals, and lem:tl5-hf-allocation;
  - prop:tl5-hf-linear, including Y ≤ Y_d + 2𝒮 and y_sep ≤ F(δ + 2𝒮₀);
  - cor:tl5-hf-level0 and rem:tl5-hf-weight (with n3).
- **L4.** lem:tl5-hf-fields:
  - (a): ΣK_ab ⊗ K_ab = γ₀⁻¹, checked by computer algebra; λ_M from eq:tl5-radii; ‖C‖ = λ_M^(−1/2).
  - (b), with m2.
  - (c): the null structure, checked by computer algebra for a general background of the class with b̂ ≠ 0. For all
    seven fields π^Z(ê₄, ê₄) = π^Z(ê₃, ê₃) = 0. For the six rotations π^K(ê₄, leaf) = 0. π^T(ê₄, ∂_x) = c e^(2ζ)∂_v b̂.
  - The counting remark after lem:tl5-hf-fields.

  The rest of L4:
  - lem:tl5-hf-commutator with eq:tl5-hf-k, D𝓡̂ included, verified exactly by computer algebra at a generic point,
    with nonzero 𝒦;
  - eq:tl5-hf-lie-d, eq:tl5-hf-lie, and 𝔏_W with its three coefficients;
  - lem:tl5-hf-system: induction, J(k, S) and the regularity count;
  - lem:tl5-hf-recovery, every constant: (√3 + 8/3), 4/3, 8/3, √2, K_rec and 𝔷_Z;
  - def:tl5-hf-coupling and 𝔅_N: the factor √c Ω̂³ μ^((j−j′)/2) and the symmetrisation 𝔒 + 𝔒ᵀ;
  - prop:tl5-hf-linear-n.
- **Sobolev.**
  - lem:tl5-hf-sphere: dimension (n + 1)², kernel (n + 1)²/(2π²), Δ = ΣK_abK_ab, the factor 6, C² = 1/12.
  - lem:tl5-hf-components: 𝔳, 𝔴, the index action of K_ab with norm 1, [K_ab, W_c] = ΣB_cd W_d.
  - lem:tl5-hf-sobolev: 𝔭₂ = 2353 from the four-term square, |B|² + |ℒ_(∂_γ)B|² ≤ (1 + 8|D̂∂_γ|²)|B|² + 2|D̂_(∂_γ)B|²,
    𝔨₁ and dω dv = R⁻³dμ dτ₂/(1 − κκ′).
  - eq:tl5-hf-cs-r with 𝔭_r = 1 + 12r² + 144r⁴.
- **L5.**
  - lem:tl5-hf-reduced: −2Ric^W(g) = −2R̂ic + L̂h + N(h) with 𝔠 and 𝔮 exactly as printed, verified exactly by computer
    algebra for a generic metric and a non-small h; 𝔠(ĝ⁻¹)h = −𝓡̂h; and the coefficient count 3/2, 1/2, 3/4, 9/4, 3/2,
    3/2, giving 16.
  - lem:tl5-hf-quadratic: (i)-(iv), the Fubini numbers F₀..F₅, b_g, b_H with the telescoping, β₁ (m′_k = 2^(k+1) − 2)
    and β₂ (with m10); the four terms of 𝔠_n; the "at most one high factor" counts for N ≥ 5.
  - lem:tl5-hf-linfty: k₁, k₂, k₃ (6/5, 8/5), the 43 words, 258 = 6·43, C₁ and C_(1,ϱ) (the factor 32 is safe; 16
    suffices), the low second order, C_∞ and C_(∞,ϱ).
  - lem:tl5-hf-quasilinear: (a) all seven terms and ϰ_H; (b) |du|, |dv|, dτ₁(T), dτ₂(T) and θ_H.
  - lem:tl5-hf-conversions: (a) with n6; (b) the ten terms, ε_𝔰, and |∂_ϑ| = R e^(−(P+Q)).
- **Bootstrap.**
  - def:tl5-hf-norm: dependence on D^κ_σ only, continuity, Y_(1/2) = 0.
  - prop:tl5-hf-bootstrap:
    - Step 1: closed and open in σ, with 𝔰 ≤ 𝔰_* and the tilt.
    - Step 2: densities of J̃, the admissibility for (1 − ϑ)⁻¹𝔅_N, the 𝔤_N term with 7^(j′/2), 2Ω̂²𝒥₁(√e_o + √c√e_i),
      and 2Ω̂²|𝔮_H| giving the first two terms of 𝔞_o and 𝔞_i.
    - Step 3: the cubic inequality and Y ≤ A_w + B_wY².
  - thm:tl5-hf: the proof and the citations of thm:tl5-wg (F1_W)-(F4_W), thm:tl5-dn (c), lem:tl5-wg-norms (a), (b) and
    lem:tl5-wg-domains (d).
  - Placement items 3 and 5: the new lem:tl5-continuation and its proof, with (H4) used where (F3_W) needs the strict
    tilt and Lorentzian limits by lem:tl5-wg-norms (b).
- **Cited labels.** Every label in the writer's list exists and says what is used. Among them, from chapter 87:
  def:tl5-wg-background, eq:tl5-wg-khat, eq:tl5-wg-def, eq:tl5-wg-lin with its curvature convention, def:tl5-wg-domains
  (κ, κ′ ≤ 1/4, so 1 − κκ′ ≥ 15/16), lem:tl5-wg-norms, def:tl5-wg-data (W1)-(W4), def:tl5-wg-solution,
  prop:tl5-wg-vacuum (b), thm:tl5-wg-data (X) and (T), lem:tl5-cip-form (b), eq:tl5-radii, lem:tl5-connection and
  lem:tl5-seed. From chapter 2: lem:warped-ricci, whose Christoffel list gives Γ^(φi)_ab = 0.
- **Self-containedness.** No statement claims the numerical closing (lines 958-964 disclaim it). There are no pending
  markers, no forbidden words (lint), and no narration.

Computer-algebra scripts are in
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/tools/:

- ricw_check.py: −2Ric^W, difference 0;
- comm_check2.py: eq:tl5-hf-comm with eq:tl5-hf-k, difference 0;
- null_check.py: null structure and ΣK ⊗ K.

The replacement texts are machine-checked against the file:

- rphf_pairs.py and m8_pair.py, applied by apply_pairs.py: each old text occurs once;
- P-HF-fixed.md: P-HF with all replacements applied.

## Replacement texts

Each block quotes the current text exactly, as whole lines, and gives the new text that replaces it. Lines are shown
indented by four spaces here; the indentation is not part of the text. A new text may end in a short line before the
unchanged next line.

### M1.1 (P-HF.md:264-264)

Old:

    be a finite family of C² symmetric 2-tensor fields on Q(a, b), each vanishing on N₀ ∩ Q(a, b), and m_ι > 0 weights; write

New:

    be a finite family of C² symmetric 2-tensor fields on Q(a, b) and m_ι > 0 weights; write

### M1.2 (P-HF.md:274-274)

Old:

        Y² := sup {ℰ(a′, b′) : −10 ≤ a′ ≤ a, 1/2 ≤ b′ ≤ b},      Y_d² := ∫_(N₁ ∩ Q(a,b)) e^(−φ) e_o dμ dv,

New:

        Y² := sup {ℰ(a′, b′) : −10 ≤ a′ ≤ a, 1/2 ≤ b′ ≤ b},
        Y_d² := ∫_(N₁ ∩ Q(a,b)) e^(−φ) e_o dμ dv + ∫_(N₀ ∩ Q(a,b)) e^(−φ) e_i dμ du,

### M1.3 (P-HF.md:287-288)

Old:

    *Proof.* Fix a′ ≤ a and b′ ≤ b. [[lem:tl5-hf-identity]] for each Ψ_ι on Q(a′, b′), summed with the weights, has no
    contribution from N₀, since each Ψ_ι vanishes there, and its N₁-term is at most Y_d², as e_o ≥ 0. By [[eq:tl5-hf-hyp]]

New:

    *Proof.* Fix a′ ≤ a and b′ ≤ b. [[lem:tl5-hf-identity]] for each Ψ_ι on Q(a′, b′), summed with the weights, has terms
    on N₁ and on N₀ whose sum is at most Y_d², as e_o, e_i ≥ 0; the term on N₀ is zero if every Ψ_ι vanishes on N₀ ∩ Q(a,
    b). By [[eq:tl5-hf-hyp]]

### M1.4 (P-HF.md:305-305)

Old:

    2-tensor field on Q(a, b) vanishing on N₀ ∩ Q(a, b). Then [[eq:tl5-hf-hyp]] holds for the family (Ψ) with weight 1 and s

New:

    2-tensor field on Q(a, b). Then [[eq:tl5-hf-hyp]] holds for the family (Ψ) with weight 1 and s

### M1.5 (P-HF.md:497-497)

Old:

    Q(a, b) whose partial derivatives of order at most N vanish on N₀ ∩ Q(a, b), 𝔤 := L̂h, and let a_o, a_i be admissible

New:

    Q(a, b), 𝔤 := L̂h, and let a_o, a_i be admissible

### M1.6 (P-HF.md:505-506)

Old:

    *Proof.* Each Ψ_I is a combination of partial derivatives of h of order at most |I| with smooth coefficients, so it
    vanishes on N₀ ∩ Q(a, b). At a point, let n^(j)_ϰ := (Σ_(|I|=j) |ξ_ϰ[Ψ_I]|²)^(1/2) and ñ^(j) := μ^(j/2) n^(j). Since 𝔅

New:

    *Proof.* At a point, let n^(j)_ϰ := (Σ_(|I|=j) |ξ_ϰ[Ψ_I]|²)^(1/2) and ñ^(j) := μ^(j/2) n^(j). Since 𝔅

### M1.7 (P-HF.md:562-567)

Old:

    A be a symmetric 2-tensor field on Q(a, b), with ℒ_(K)A and ℒ_(K′)ℒ_K A of class C¹ for all rotations K, K′, and A = 0 on
    N₀ ∩ Q(a, b). Then, with ε₁ the face density [[eq:tl5-hf-faces]] and the sums over words J of length at most two in the
    six rotations,
    
        |A(p)|² ≤ C_S(p)² Σ_(|J|≤2) ∫_(Σ₁(a,b)) ε₁[ℒ^J A] dμ dτ₂,
        C_S(p)² := 6 C_(S³)² 𝔭₂ 𝔴(p)⁴ sup_(Σ₁(a,b)) 𝔳⁴ R⁻³ ((1 + 8|D̂∂_γ|²)/(2Ω̂² z̲) + 2𝔨₁),                 {#eq:tl5-hf-cs}

New:

    A be a C¹ symmetric 2-tensor field on Q(a, b), with ℒ_(K)A and ℒ_(K′)ℒ_K A of class C¹ for all rotations K, K′, and
    let S_a := {a} × {1/2} × S³, the leaf of N₀ in which the face Σ₁(a, b) begins. Then, with ε₁ the face density
    [[eq:tl5-hf-faces]] and the sums over words J of length at most two in the six rotations,
    
        |A(p)|² ≤ C_S(p)² Σ_(|J|≤2) ∫_(Σ₁(a,b)) ε₁[ℒ^J A] dμ dτ₂ + C_(S,0)(p)² Σ_(|J|≤2) ∫_(S_a) |ℒ^J A|² dω,
        C_S(p)² := 6 C_(S³)² 𝔭₂ 𝔴(p)⁴ sup_(Σ₁(a,b)) 𝔳⁴ R⁻³ ((1 + 8|D̂∂_γ|²)/(2Ω̂² z̲) + 2𝔨₁),                 {#eq:tl5-hf-cs}
        C_(S,0)(p)² := 6 C_(S³)² 𝔭₂ 𝔴(p)⁴ sup_(S_a) 𝔳⁴;
    
    the last term is zero if A = 0 on N₀ ∩ Q(a, b).

### M1.8 (P-HF.md:575-577)

Old:

    ≤ 𝔴(p)⁴ |A(p)|²_e ≤ 6C_(S³)² 𝔴(p)⁴ Σ 𝔈(A_(VV′))(v_p), the sum over the 36 components. These vanish at v = 1/2, as A and
    its derivatives along N₀ do, so 𝔈(A_(VV′))(v_p) = ∫ ∂_v 𝔈 dv ≤ ∫_(1/2)^(v_p) (𝔈(A_(VV′)) + 𝔈(∂_γ A_(VV′))) dv, by 2|f ∂_γ
    f| ≤ f² + (∂_γ f)²; here ∂_γ commutes with the K and with the index actions, so ∂_γ(K′K A_(VV′)) = K′K((ℒ_(∂_γ)A)_(VV′)).

New:

    ≤ 𝔴(p)⁴ |A(p)|²_e ≤ 6C_(S³)² 𝔴(p)⁴ Σ 𝔈(A_(VV′))(v_p), the sum over the 36 components. Here 𝔈(A_(VV′))(v_p) =
    𝔈(A_(VV′))(1/2) + ∫ ∂_v 𝔈 dv ≤ 𝔈(A_(VV′))(1/2) + ∫_(1/2)^(v_p) (𝔈(A_(VV′)) + 𝔈(∂_γ A_(VV′))) dv, by 2|f ∂_γ f| ≤ f² +
    (∂_γ f)²; here ∂_γ commutes with the K and with the index actions, so ∂_γ(K′K A_(VV′)) = K′K((ℒ_(∂_γ)A)_(VV′)).

### M1.9 (P-HF.md:584-584)

Old:

    z̲), by [[lem:tl5-hf-densities]]. Finally dω dv = R⁻³ dμ dτ₂/(1 − κκ′) on the face, and (e_o + κ′e_i)/(1 − κκ′) = ε₁. ∎

New:

    z̲), by [[lem:tl5-hf-densities]]. Finally dω dv = R⁻³ dμ dτ₂/(1 − κκ′) on the face, and (e_o + κ′e_i)/(1 − κκ′) = ε₁.
    The terms at v = 1/2 are integrals over S_a, and the bound for B = A gives Σ_(VV′) 𝔈(A_(VV′))(1/2) ≤ 𝔭₂ sup_(S_a) 𝔳⁴
    Σ_(|J|≤2) ∫_(S_a) |ℒ^J A|² dω; they are zero if A = 0 on N₀ ∩ Q(a, b), as A and its derivatives along N₀ then vanish. ∎

### M1.10 (P-HF.md:586-592)

Old:

    The same proof, with r slots in place of two, gives for a tensor field A of rank r on Q(a, b) vanishing on N₀ ∩ Q(a, b),
    with 𝔭_r := 1 + 12r² + 144r⁴,
    
        |A(p)|² ≤ 6 C_(S³)² 𝔭_r 𝔴(p)^(2r) Σ_(|J|≤2) ∫_(Σ₁(a,b)) 𝔳^(2r) R⁻³ ((1 + 2r²|D̂∂_γ|²) |ℒ^J A|²
                  + 2|∂_γ|² |D̂ ℒ^J A|²) dμ dτ₂/(1 − κκ′),                                                  {#eq:tl5-hf-cs-r}
    
    using |D̂_(∂_γ)B| ≤ |∂_γ| |D̂B| in place of the densities.

New:

    The same proof, with r slots in place of two and 𝔭_r := 1 + 12r² + 144r⁴, gives for a tensor field A of rank r on
    Q(a, b)
    
        |A(p)|² ≤ 6 C_(S³)² 𝔭_r 𝔴(p)^(2r) (Σ_(|J|≤2) ∫_(Σ₁(a,b)) 𝔳^(2r) R⁻³ ((1 + 2r²|D̂∂_γ|²) |ℒ^J A|²
                  + 2|∂_γ|² |D̂ ℒ^J A|²) dμ dτ₂/(1 − κκ′)
                  + sup_(S_a) 𝔳^(2r) Σ_(|J|≤2) ∫_(S_a) |ℒ^J A|² dω),                                       {#eq:tl5-hf-cs-r}
    
    using |D̂_(∂_γ)B| ≤ |∂_γ| |D̂B| in place of the densities; the last term is zero if A = 0 on N₀ ∩ Q(a, b).

### M1.11 (P-HF.md:695-698)

Old:

    **Lemma {#lem:tl5-hf-linfty}** (The low quantities at a point.) Let N ≥ 5, g a solution of the reduced problem on D^κ_s,
    h := g − ĝ, and suppose that all partial derivatives of h of order at most N + 1 vanish on N₀ ∩ D^κ_s. For p ∈ D^κ_s put
    a := τ₁(p), b := τ₂(p), let ℰ⁰_N(p) := Σ_(|I|≤N) ∫_(Σ₁(a,b)) ε₁[Ψ_I] dμ dτ₂, the unweighted face energy of all words of
    length at most N, and ϱ(p) := sup over Q(a, b) of max_(|J|≤N−1) |ℒ^J(2R̂ic)|. At points of D^κ_s let

New:

    **Lemma {#lem:tl5-hf-linfty}** (The low quantities at a point.) Let N ≥ 5, g a solution of the reduced problem on D^κ_s
    and h := g − ĝ. For p ∈ D^κ_s put a := τ₁(p), b := τ₂(p), let ℰ⁰_N(p) := Σ_(|I|≤N) ∫_(Σ₁(a,b)) ε₁[Ψ_I] dμ dτ₂, the
    unweighted face energy of all words of length at most N, ϱ(p) := sup over Q(a, b) of max_(|J|≤N−1) |ℒ^J(2R̂ic)|, and
    η₀(p) := sup over N₀ ∩ Q(a, b) of max(𝔰, |Ψ_C| (|C| ≤ N), |D̂Ψ_C| (|C| ≤ N − 1)), a bound for derivatives of h of order
    at most N on N₀. At points of D^κ_s let

### M1.12 (P-HF.md:708-714)

Old:

        𝔰(p) ≤ C_∞(p) ℰ⁰_N(p)^(1/2) + C_(∞,ϱ)(p) ϱ(p),                                                    {#eq:tl5-hf-linfty}
    
    with 𝔐 := Σ_(j≤N−3) 7^j the number of words of length at most N − 3, C_∞ := 2 max(2C_S, C₁, k₁(p) (2𝔐)^(1/2) max(C_S,
    C₁)), C_(∞,ϱ) := 2 max(C_(1,ϱ), k₁(p) (2𝔐)^(1/2) C_(1,ϱ) + k₂(p)), C_S of [[eq:tl5-hf-cs]] and
    
        C₁² := 258 C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(Σ₁(a,b)) 𝔳⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + 6Λ)² + 4|∂_γ|² (72Λ² + 8(k₁ + 1)²)),
        C_(1,ϱ)² := 258 C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(Σ₁(a,b)) (𝔳⁶ R⁻³ 32 |∂_γ|² k₂²) · ∫_(Σ₁(a,b)) dμ dτ₂/(1 − κκ′).

New:

        𝔰(p) ≤ C_∞(p) ℰ⁰_N(p)^(1/2) + C_(∞,ϱ)(p) ϱ(p) + C_(∞,0)(p) η₀(p),                              {#eq:tl5-hf-linfty}
    
    with 𝔐 := Σ_(j≤N−3) 7^j the number of words of length at most N − 3, C_∞ := 2 max(2C_S, C₁, k₁(p) (2𝔐)^(1/2) max(C_S,
    C₁)), C_(∞,ϱ) := 2 max(C_(1,ϱ), k₁(p) (2𝔐)^(1/2) C_(1,ϱ) + k₂(p)), C_(∞,0) := 2 max(2C_(0,0), C_(1,0), k₁(p) (2𝔐)^(1/2)
    max(C_(0,0), C_(1,0))), C_S and C_(S,0) of [[eq:tl5-hf-cs]], S_a as in [[lem:tl5-hf-sobolev]], and
    
        C₁² := 258 C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(Σ₁(a,b)) 𝔳⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + 6Λ)² + 4|∂_γ|² (72Λ² + 8(k₁ + 1)²)),
        C_(1,ϱ)² := 258 C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(Σ₁(a,b)) (𝔳⁶ R⁻³ 32 |∂_γ|² k₂²) · ∫_(Σ₁(a,b)) dμ dτ₂/(1 − κκ′),
        C_(0,0)² := 86π² C_(S,0)(p)²,      C_(1,0)² := 516π² C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(S_a) 𝔳⁶ (1 + 6Λ)².

### M1.13 (P-HF.md:718-719)

Old:

    𝔔_CJ ℒ^J(2R̂ic) − Σ_(J≠C) 𝔔_CJ ℒ^J N(h) − (ℒ^C N(h) − H^(αβ)D̂_αD̂_βΨ_C). Each Ψ_I, |I| ≤ N, and each low quantity
    vanishes on N₀, being built from derivatives of h of order at most N + 1.

New:

    𝔔_CJ ℒ^J(2R̂ic) − Σ_(J≠C) 𝔔_CJ ℒ^J N(h) − (ℒ^C N(h) − H^(αβ)D̂_αD̂_βΨ_C).

### M1.14 (P-HF.md:729-730)

Old:

    *Zeroth order.* [[lem:tl5-hf-sobolev]] for A := Ψ_B, |B| ≤ N − 2, gives |Ψ_B(p)| ≤ C_S(p) ℰ⁰_N(p)^(1/2), since ℒ^J Ψ_B =
    Ψ_(JB) and the words JB are distinct for distinct J; and |H(p)| ≤ 2|h(p)| by [[lem:tl5-wg-norms]] (a).

New:

    *Zeroth order.* [[lem:tl5-hf-sobolev]] for A := Ψ_B, |B| ≤ N − 2, gives |Ψ_B(p)| ≤ C_S(p) ℰ⁰_N(p)^(1/2) + C_(0,0)
    η₀(p), since ℒ^J Ψ_B = Ψ_(JB), the words JB are distinct for distinct J, there are 43 words J and ∫_(S_a) dω = 2π²,
    and the bound |H(p)| ≤ 2|h(p)| holds by [[lem:tl5-wg-norms]] (a).

### M1.15 (P-HF.md:737-737)

Old:

    on Σ₁(a, b); inserting the bound for M₂, with (x + y)² ≤ 2x² + 2y², gives |D̂Ψ_B(p)| ≤ C₁ ℰ⁰_N(p)^(1/2) + C_(1,ϱ) ϱ(p).

New:

    on Σ₁(a, b); inserting the bound for M₂, with (x + y)² ≤ 2x² + 2y², and bounding the term on S_a by |ℒ^J A| ≤ (1 + 6Λ)
    η₀(p) there, gives |D̂Ψ_B(p)| ≤ C₁ ℰ⁰_N(p)^(1/2) + C_(1,ϱ) ϱ(p) + C_(1,0) η₀(p).

### M1.16 (P-HF.md:741-741)

Old:

    by L := (Σ_(|C|≤N−3) (|Ψ_C|² + |D̂Ψ_C|²))^(1/2) ≤ (2𝔐)^(1/2) (max(C_S, C₁) ℰ⁰_N^(1/2) + C_(1,ϱ) ϱ), as all words involved

New:

    by L := (Σ_(|C|≤N−3) (|Ψ_C|² + |D̂Ψ_C|²))^(1/2) ≤ (2𝔐)^(1/2) (max(C_S, C₁) ℰ⁰_N^(1/2) + C_(1,ϱ) ϱ + max(C_(0,0),
    C_(1,0)) η₀), as all words involved

### M1.17 (P-HF.md:814-818)

Old:

    be data in the wave gauge, and on N₁ let Ψ_I := ℒ^I(G^♯ − ĝ) and H := (G^♯)⁻¹ − ĝ⁻¹, computed from the derivatives of G^♯
    on N₁. Put, with s_N of [[eq:tl5-hf-sn]], ϱ the function of [[lem:tl5-hf-linfty]] for p with τ₁(p) = u*, τ₂(p) = v*, and
    the constants of [[lem:tl5-hf-linfty]] and [[lem:tl5-hf-quasilinear]],
    
        δ_w² := Σ_(|I|≤N) μ^|I| ∫_(N₁) e^(−φ) (e_o[Ψ_I] + 2Ω̂² |du(𝔟[Ψ_I])|) dμ dv,

New:

    be data in the wave gauge, and on N = N₀ ∪ N₁ let Ψ_I := ℒ^I(G^♯ − ĝ) and H := (G^♯)⁻¹ − ĝ⁻¹, computed from the
    derivatives of G^♯ on N. Put, with s_N of [[eq:tl5-hf-sn]], ϱ and η₀ the functions of [[lem:tl5-hf-linfty]] for p with
    τ₁(p) = u*, τ₂(p) = v*, and the constants of [[lem:tl5-hf-linfty]] and [[lem:tl5-hf-quasilinear]],
    
        δ_w² := Σ_(|I|≤N) μ^|I| (∫_(N₁) e^(−φ) (e_o[Ψ_I] + 2Ω̂² |du(𝔟[Ψ_I])|) dμ dv
                  + ∫_(N₀) e^(−φ) (e_i[Ψ_I] + 2Ω̂² |dv(𝔟[Ψ_I])|) dμ du),

### M1.18 (P-HF.md:826-826)

Old:

        𝔯_w := ∫_(−10)^(u*) sup_(Σ₁(t,v*)) (𝔞_o C_(∞,ϱ) ϱ) dt + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) (𝔞_i C_(∞,ϱ) ϱ) dt,

New:

        𝔯_w := ∫_(−10)^(u*) sup_(Σ₁(t,v*)) (𝔞_o (C_(∞,ϱ) ϱ + C_(∞,0) η₀)) dt
                  + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) (𝔞_i (C_(∞,ϱ) ϱ + C_(∞,0) η₀)) dt,

### M1.19 (P-HF.md:829-829)

Old:

    where C_∞, C_(∞,ϱ), k₁, k₂ are evaluated at the point of the supremum, and, for a fixed ϑ ∈ (0, 1/4],

New:

    where C_∞, C_(∞,ϱ), C_(∞,0), k₁, k₂ are evaluated at the point of the supremum, and, for a fixed ϑ ∈ (0, 1/4],

### M1.20 (P-HF.md:832-832)

Old:

        𝔰₁ := min(𝔰₀/2, c_* κ_m/2, 𝔰_θ),   𝔰_* := sup_(p∈D^κ) (2 C_∞(p) μ^(−N/2) e^(φ(p)/2) A_w + C_(∞,ϱ)(p) ϱ(p)).

New:

        𝔰₁ := min(𝔰₀/2, c_* κ_m/2, 𝔰_θ),
        𝔰_* := sup_(p∈D^κ) (2 C_∞(p) μ^(−N/2) e^(φ(p)/2) A_w + C_(∞,ϱ)(p) ϱ(p) + C_(∞,0)(p) η₀).

### M1.21 (P-HF.md:835-838)

Old:

    that G^♯ − ĝ vanishes together with its partial derivatives of order at most N + 1 at every point of N₀, that the rates
    a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N), and that
    
        𝔯_w ≤ 1/4,      𝔰_* < 𝔰₁.                                                                      {#eq:tl5-hf-smallness}

New:

    that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N), and that
    
        𝔯_w ≤ 1/4,      η₀ < 𝔰₁,      𝔰_* < 𝔰₁.                                                       {#eq:tl5-hf-smallness}

### M1.22 (P-HF.md:845-847)

Old:

    *Proof.* By [[thm:tl5-wg]] (F4_W), g is vacuum and has on N ∩ D^κ_s the derivatives of all orders of G^♯; so h and its
    derivatives of order at most N + 1 vanish on N₀ ∩ D^κ_s, and the quantities of [[def:tl5-hf-constants]] on N₁ are those
    of g. In particular 𝔰 = 0 on N₀ ∩ D^κ_s, the low quantities being built from such derivatives.

New:

    *Proof.* By [[thm:tl5-wg]] (F4_W), g is vacuum and has on N ∩ D^κ_s the derivatives of all orders of G^♯; so the
    quantities of [[def:tl5-hf-constants]] on N are those of g. In particular 𝔰 ≤ η₀ < 𝔰₁ on N₀ ∩ D^κ_s.

### M1.23 (P-HF.md:859-860)

Old:

    [[lem:tl5-hf-quasilinear]], its face densities are at least (1 − ϑ) ≥ 3/4 times ε₁[Ψ_I] and ε₂[Ψ_I]; on N₀ they vanish,
    as Ψ_I and H do; on N₁ they are at most e_o[Ψ_I] + 2Ω̂²|du(𝔟)|. By [[lem:tl5-hf-divergence]] and (a) of

New:

    [[lem:tl5-hf-quasilinear]], its face densities are at least (1 − ϑ) ≥ 3/4 times ε₁[Ψ_I] and ε₂[Ψ_I]; on N₁ and on N₀
    they are at most e_o[Ψ_I] + 2Ω̂²|du(𝔟)| and e_i[Ψ_I] + 2Ω̂²|dv(𝔟)|. By [[lem:tl5-hf-divergence]] and (a) of

### M1.24 (P-HF.md:886-886)

Old:

    e^(φ/2) Y_s + C_(∞,ϱ) ϱ at every point. So for every a′ ≤ u*, b′ ≤ s,

New:

    e^(φ/2) Y_s + C_(∞,ϱ) ϱ + C_(∞,0) η₀ at every point. So for every a′ ≤ u*, b′ ≤ s,

### M1.25 (P-HF.md:934-934)

Old:

    (a) G^♯ − ĝ vanishes together with its partial derivatives of order at most N + 1 at every point of N₀;

New:

    (a) the quantity η₀ of [[def:tl5-hf-constants]], computed from the derivatives of G^♯ − ĝ of order at most N on N₀,
    satisfies η₀ < 𝔰₁;

### M1.26 (P-HF.md:958-959)

Old:

    The constants of [[thm:tl5-hf]] are explicit in the jets of ĝ of order at most N + 3, in c, z, z̲, κ, κ′, μ and ϑ, and in
    the data G^♯ on N₁: the rates enter through the weight φ, the amplification from the data to each point being e^(φ/2) ≤

New:

    The constants of [[thm:tl5-hf]] are explicit in the jets of ĝ of order at most N + 3, in c, z, z̲, κ, κ′, μ and ϑ, and in
    the data G^♯ on N: the rates enter through the weight φ, the amplification from the data to each point being e^(φ/2) ≤

### M1.27 (P-HF.md:962-964)

Old:

    inequalities (b) and (c) for a background at 10 l5 requires enclosures of those functions, of the residual Ric(ĝ) and of
    the data on N₁, which this paper does not provide. The condition (a), the hypotheses (X) and (T) of [[thm:tl5-wg-data]]
    that give G^♯, and those of [[thm:tl5-dn]], are conditions on the background of the same kind.

New:

    inequalities (a)–(c) for a background at 10 l5 requires enclosures of those functions, of the residual Ric(ĝ) and of
    the data on N, which this paper does not provide. The hypotheses (X) and (T) of [[thm:tl5-wg-data]] that give G^♯, and
    those of [[thm:tl5-dn]], are conditions on the background of the same kind. The derivatives of G^♯ − ĝ on N₀ transverse
    to N₀ need not vanish, so η₀ and the terms on N₀ in δ_w are small only for a background whose transverse derivatives on
    N₀ of order at most N are close to those of G^♯.

### M2 (P-HF.md:917-923)

Old:

    than j only, besides H^(αβ)D̂_αD̂_βΨ_B, which the lemma absorbs. Hence the nonlinear terms of the identities for J[Ψ_I] −
    𝔟[Ψ_I], |I| ≤ m, weights 1, are bounded pointwise by a constant times (e_o + e_i) + ϱ (√e_o + √c √e_i), the 𝔟-terms as in
    the proof of [[prop:tl5-hf-bootstrap]]. Choose constant rates admissible for ((1 − ϑ)⁻¹ 𝔅_m + 𝔊 diag(E_o + E_i), E_o^m,
    E_i^m), with 𝔊 that constant: they exist by [[lem:tl5-hf-allocation]], all entries being bounded on D^κ.
    [[prop:tl5-hf-linear]] then bounds the level-m energies by the data, which are those of G^♯, and the residual, so E_m
    exists; and [[lem:tl5-hf-linfty]], whose proof at level m uses smallness only to absorb the nonlinear part, which is now
    bounded by known factors, gives L_m. So P(m) holds for every m.

New:

    than j only, besides H^(αβ)D̂_αD̂_βΨ_B, which the lemma absorbs. Hence the nonlinear terms of the identities for J[Ψ_I] −
    𝔟[Ψ_I], |I| ≤ m, weights 1, are bounded pointwise by a constant 𝔊 times e_o + e_i plus a constant times
    ϱ (√e_o + √c √e_i), the 𝔟-terms as in the proof of [[prop:tl5-hf-bootstrap]]. Choose constant rates admissible for
    ((1 − ϑ)⁻¹ (𝔅_m + 𝔊 (E_o^m + E_i^m)), E_o^m, E_i^m): they exist by [[lem:tl5-hf-allocation]], all entries being bounded
    on D^κ. Steps 2 and 3 of the proof of [[prop:tl5-hf-bootstrap]] with these rates, and the argument of
    [[prop:tl5-hf-linear]], then bound the level-m energies by the fluxes through N₁ and N₀, which are fluxes of derivatives
    of G^♯ of order at most m + 1 ([[thm:tl5-wg]] (F4_W)), and by the residual; so E_m exists. And the proof of
    [[lem:tl5-hf-linfty]] at level m, which uses smallness only to absorb the nonlinear part, now bounded by known factors,
    gives L_m, its terms on N₀ being bounded by derivatives of G^♯ on N₀. So P(m) holds for every m.

### m1 (P-HF.md:4-5)

Old:

    background ĝ, in a norm Y built from characteristic energies with an exponential weight, and with it the hypotheses
    (H1)–(H3) of [[lem:tl5-continuation]] in the wave gauge, every constant being an explicit function of the jets of ĝ. The

New:

    background ĝ, in a norm Y built from characteristic energies with an exponential weight, and with it the hypotheses
    (H1), (H2) and (H4) of [[lem:tl5-continuation]] in the wave gauge and (H3) under an explicit closing condition, every
    constant being an explicit function of the jets of ĝ, of the data and of the weights. The

### m2 (P-HF.md:45-46)

Old:

    For the seed of [[lem:tl5-seed]], T is the static Killing field ∂_v + (f(−u)/2) ∂_u of [[lem:tl5-seed]], since there b̂ =
    0. The norm k is the norm k̂ of [[eq:tl5-wg-khat]] with E₀ in place of the vector e₀ = (ê₃ + ê₄)/(2Ω̂) used there.

New:

    For the seed of [[lem:tl5-seed]], b̂ = 0 and T = ∂_v + c ∂_u is a Killing field, the static one: T(R) = f(R)/2 −
    f(−u) e^(2W) = 0 by ∂_vR = f(R)/2 and e^(2W) = f(R)/(2f(−u)) ([[lem:tl5-seed]] (b)) and ∂_uR = −2e^(2W) (its proof of
    (c)); hence T(e^(2W)) = −c′ e^(2W), and ℒ_T(−4e^(2W) du dv + R² γ₀) = −4(T(e^(2W)) + c′ e^(2W)) du dv + T(R²) γ₀ = 0.
    The norm k is the norm k̂ of [[eq:tl5-wg-khat]] with E₀ in place of the vector e₀ = (ê₃ + ê₄)/(2Ω̂) used there.

### m3a (P-HF.md:24-24)

Old:

    with ζ, A and B as in [[eq:tl5-radii]] for its fields R, P, Q and with b̂ = (1 − x²) s; then ê₃ = ∂_u + b̂ ∂_x, ê₄ = ∂_v,

New:

    with ζ, A and B as in [[eq:tl5-radii]] for its fields R, P, Q and with b̂ the shift β; then ê₃ = ∂_u + b̂ ∂_x, ê₄ = ∂_v,

### m3b (P-HF.md:543-543)

Old:

    c²)/|T|² + c² (1 − x²) s²/(2|T|²) + R⁻² (e^(2(P+Q)) + e^(−2P) + e^(−2Q)), all smooth on D̄.

New:

    c²)/|T|² + 2c² |b̂ ∂_x|²_(γ₀)/|T|² + R⁻² (e^(2(P+Q)) + e^(−2P) + e^(−2Q)), all smooth on D̄, as b̂ ∂_x is the shift
    vector field of ĝ, smooth on each leaf ([[lem:tl5-cip-form]] (a)).

### m4 (P-HF.md:724-725)

Old:

    ≤ |H| |D̂²Ψ_J| + 𝔠_(|J|) 𝔰𝔧 ≤ (𝔠_(|J|) + 1) 𝔰 𝔧 for |J| ≤ N − 1, with 𝔧 ≤ max(𝒥₁, M₂). Hence M₂ ≤ k₁ 𝒥₁ +
    k₂ |ℒ^(≤N−1)(2R̂ic)| + k₃ 𝔰 max(𝒥₁, M₂), and with k₃𝔰 ≤ 1/2,

New:

    ≤ |H| |D̂²Ψ_J| + 𝔠_(|J|) 𝔰𝔧 ≤ (𝔠_(|J|) + 1) 𝔰 𝔧 for |J| ≤ N − 1, with 𝔧 ≤ 2𝒥₁ + M₂, as |H| ≤ 2|h| by
    [[lem:tl5-wg-norms]] (a). Hence M₂ ≤ k₁ 𝒥₁ + k₂ |ℒ^(≤N−1)(2R̂ic)| + k₃ 𝔰 (2𝒥₁ + M₂), and with k₃𝔰 ≤ 1/2,

### m5 (P-HF.md:234-235)

Old:

    denoting the vector of absolute values. The condition is monotone in the tilt: rates that satisfy
    [[eq:tl5-hf-admissible]] with κ = κ′ = 0 satisfy it for all κ, κ′ ≥ 0.

New:

    denoting the vector of absolute values. The condition is monotone in the tilt: for fixed values of a_o and a_i its left
    side does not decrease when κ or κ′ increases, so nondecreasing rates that satisfy it with κ = κ′ = 0 at every point of
    D̄ satisfy it for all κ, κ′ ≥ 0, as τ₁ ≥ u and τ₂ ≥ v on D̄.

### m6 (P-HF.md:966-971)

Old:

    **Remark {#rem:tl5-hf-level}** (The level N.) Each monomial of ℒ^I N(h) has at least two solution factors and needs all
    but one of them bounded at the point; the bounds at a point of [[lem:tl5-hf-linfty]] reach Ψ_B for |B| ≤ N − 2, D̂Ψ_B
    for |B| ≤ N − 3 and D̂²Ψ_B for |B| ≤ N − 4, by the Sobolev inequality on S³ and the trace along the faces, each using two
    rotations or one face derivative. A product D̂Ψ_B D̂Ψ_(B′) with |B| + |B′| = N then has a bounded factor exactly when N ≥
    5, which is the condition of [[lem:tl5-hf-quadratic]]; at the next level the same count, with the bounds of level N − 1
    only, needs N ≥ 6, which is the condition of [[lem:tl5-hf-persistence]].

New:

    **Remark {#rem:tl5-hf-level}** (The level N.) In the proof of [[lem:tl5-hf-quadratic]] each monomial of ℒ^I N(h) has at
    least two solution factors, and all but one of them are bounded at the point; the bounds at a point of
    [[lem:tl5-hf-linfty]] reach Ψ_B for |B| ≤ N − 2, D̂Ψ_B for |B| ≤ N − 3 and D̂²Ψ_B for |B| ≤ N − 4: the Sobolev inequality
    on S³ uses two rotations, and each further derivative transverse to the leaves is recovered from one more commutation.
    A product D̂Ψ_B D̂Ψ_(B′) with |B| + |B′| = N then has a factor bounded at the point exactly when N ≥ 5, which is the
    condition of [[lem:tl5-hf-quadratic]]; at level N + 1, with the bounds of level N only, the same count needs N + 1 ≥ 7,
    that is N ≥ 6, which is the condition of [[lem:tl5-hf-persistence]]. These conditions belong to this way of bounding
    the products, with one factor at a point and the others in the energies.

### m7a (P-HF.md:1060-1061)

Old:

    solution on D^κ_(s′) for some s′ ∈ (s, v*]. Of the regions D^κ_s it uses only that they increase with s and that a
    solution on D^κ_s restricts to solutions on D^κ_σ for σ < s ([[rem:tl5-wg-continuation]]); (H4) is the strict tilt that

New:

    solution on D^κ_(s′) for some s′ ∈ (s, v*]. Of the regions D^κ_s it uses only the properties listed in
    [[rem:tl5-wg-continuation]]; (H4) is the strict tilt that

### m7b (P-HF.md:1065-1065)

Old:

    C^(1,1)-distance of g to ĝ on the slice. For the problem of [[def:tl5-problem]] with u* < u₀ the data of the first stage

New:

    C²-distance of g to ĝ on the slice. For the problem of [[def:tl5-problem]] with u* < u₀ the data of the first stage

### m9 (P-HF.md:925-928)

Old:

    Finally, every covariant derivative D̂^k h is bounded by the quantities of P(k + 4): apply [[lem:tl5-hf-recovery]] to
    D̂^(k−2)Ψ_B in place of Ψ, inductively in k, with [[eq:tl5-hf-lie-d]] to commute ℒ_Z with D̂. Since ĝ is smooth on the
    compact set D̄, the components of g = ĝ + h in the charts and their partial derivatives of order at most k are
    polynomials in the components of D̂^j h, j ≤ k, with bounded coefficients. ∎

New:

    Finally, every covariant derivative D̂^k Ψ_B, for every k and every word B, is bounded, by induction on k and, for fixed
    k, on |B|; for k ≤ 2 this is P(m) for m large. The proof of [[lem:tl5-hf-recovery]] applies verbatim to a tensor field A
    of any rank in place of Ψ, with □̂ in place of L̂, 𝓡̂ replaced by 0 and 𝒞 acting on every slot: it bounds |D̂²A| at a
    point by |D̂ℒ_Z A| (Z ∈ Γ), |D̂A|, |A| and |□̂A + H^(αβ) D̂_αD̂_β A|. Take A := D̂^(k−2)Ψ_B, k ≥ 3. By
    [[eq:tl5-hf-lie-d]], ℒ_Z A is D̂^(k−2)Ψ_(ZB) plus contractions of derivatives of Γ′[π^Z] with D̂^j Ψ_B, j ≤ k − 3;
    commuting D̂ with □̂ gives
    □̂A = D̂^(k−2) □̂Ψ_B plus contractions of derivatives of R̂ with D̂^j Ψ_B, j ≤ k − 2; and □̂Ψ_B + H^(αβ) D̂_αD̂_β Ψ_B is
    given by the equation in the proof of [[lem:tl5-hf-linfty]], whose k − 2 derivatives contain derivatives of order k only
    of Ψ_(B′), |B′| < |B|, or in H^(αβ) D̂_αD̂_β A up to terms of lower order. So the induction bounds D̂^k Ψ_B by bounded
    quantities. Since ĝ is smooth on the compact set D̄, the components of g = ĝ + h in the charts and their partial
    derivatives of order at most k are polynomials in the components of D̂^j h, j ≤ k, with bounded coefficients. ∎

### m10 (P-HF.md:667-667)

Old:

    solution factor D̂Ψ_B gives at most four monomials, by ℒ_Z D̂Ψ_B = D̂Ψ_(ZB) − Γ′ ⋆ Ψ_B, and of one with Ψ_B two; so the

New:

    solution factor D̂Ψ_B gives at most four monomials, by ℒ_Z D̂Ψ_B = D̂Ψ_(ZB) − Γ′ ⋆ Ψ_B, and of one with Ψ_B at most
    three (two if it has one background factor); so the

### n1a (P-HF.md:526-526)

Old:

        C_(S³)² := Σ_(n≥0) (n + 1)²/(2π² (1 + n(n + 2))²).                                                {#eq:tl5-hf-sphere}

New:

        C_(S³)² := Σ_(n≥0) (n + 1)²/(2π² (1 + n(n + 2))²) = 1/12.                                         {#eq:tl5-hf-sphere}

### n1b (P-HF.md:531-531)

Old:

    the Cauchy–Schwarz inequality over n and Parseval's identity, |f(ω)| ≤ Σ_n (n + 1)(2π²)^(−1/2) ‖f_n‖ ≤ C_(S³) ‖(1 − Δ)f‖,

New:

    the Cauchy–Schwarz inequality over n and Parseval's identity, |f(ω)| ≤ Σ_n (n + 1)(2π²)^(−1/2) ‖f_n‖ ≤ C_(S³) ‖(1 − Δ)f‖,
    where, as 1 + n(n + 2) = (n + 1)², C_(S³)² = Σ_(m≥1) 1/(2π² m²) = 1/12,

### n2 (P-HF.md:674-674)

Old:

    with r blocks, F_k in all. Here ℒ^B g = ℒ^B ĝ + Ψ_B with ℒ^B ĝ = ℒ^(B′) π^(Z) for B = (Z, B′), of norm at most Λ. So ℒ^J

New:

    with r blocks, F_k in all. Here ℒ^B g = ℒ^B ĝ + Ψ_B with ℒ^B ĝ = ℒ^(B′) π^(Z) for B = (B′, Z), of norm at most Λ. So ℒ^J

### n3 (P-HF.md:314-314)

Old:

    dφ(J) dominates the bulk, and any C¹ function φ ≥ 0 with ∂_(τ₁)φ ≥ 0, ∂_(τ₂)φ ≥ 0 and [[eq:tl5-hf-admissible]] at every

New:

    dφ(J) dominates the bulk, and any C¹ function φ = φ(τ₁, τ₂) ≥ 0 with ∂_(τ₁)φ ≥ 0, ∂_(τ₂)φ ≥ 0 and
    [[eq:tl5-hf-admissible]] at every

### n4 (P-HF.md:217-218)

Old:

    −|T|(𝒞_(j0))_j/2, and ℬ₀₀ is zeroth order. In particular, if T is a Killing field of ĝ, as for the seed, the principal
    term vanishes. The formula for div 𝒵 follows from div(fV) = f div V + V(f) and from the coordinate density Ω̂²R³/2 of the

New:

    −|T|(𝒞_(j0))_j/2, and ℬ₀₀ is zeroth order. In particular, if T is a Killing field of ĝ, as for the seed, the term
    −(1/2) π^(αβ) 𝕋_αβ vanishes, and the first-order blocks come from 𝔇 alone. The formula for div 𝒵 follows from div(fV) =
    f div V + V(f) and from the coordinate density Ω̂²R³/2 of the

### n5 (P-HF.md:763-764)

Old:

    D̂_γΨ). The two terms with T^δ and two derivatives of Ψ differ by H^(αβ) T^δ ⟨D̂_βΨ, 𝒞_αδ Ψ⟩. So 𝔮_H is the sum of the
    six remaining terms. Bounding each: a contraction of different tensors by the product of their norms, the trace

New:

    D̂_γΨ). The two terms with T^δ and two derivatives of Ψ differ by H^(αβ) T^δ ⟨D̂_βΨ, 𝒞_αδ Ψ⟩. So 𝔮_H is the sum of the
    six remaining terms and of this one. Bounding each: a contraction of different tensors by the product of their norms,
    the trace

### n6 (P-HF.md:793-793)

Old:

    *Proof.* (a) is [[lem:tl5-hf-khat]] with r = 2 and c ≤ 1. (b) The components are h_μν = h(∂_μ, ∂_ν), and ∂_λ(h_μν) =

New:

    *Proof.* (a) is [[lem:tl5-hf-khat]] with r = 2 and c ≥ c_*. (b) The components are h_μν = h(∂_μ, ∂_ν), and ∂_λ(h_μν) =

### n8 (P-HF.md:948-948)

Old:

    *Proof.* Apply [[lem:tl5-continuation]] with y_σ := Y_σ, A := A_w and B := B_w. By [[def:tl5-hf-norm]], Y_σ depends only

New:

    *Proof.* If A_w = 0, then R̂ic = 0 on D^κ and G^♯ = ĝ at the points of N, so ĝ is the solution, with Y_σ(ĝ) = 0.
    Otherwise apply [[lem:tl5-continuation]] with y_σ := Y_σ, A := A_w and B := B_w. By [[def:tl5-hf-norm]], Y_σ depends only

### n9 (P-HF.md:705-705)

Old:

    with the maps of [[def:tl5-hf-coupling]] and 𝔠_n of [[eq:tl5-hf-cn]], and 𝔨₂ := (1/z̲ + max(1/c, 1/κ′))/(2Ω̂²). If 𝔰 ≤ 𝔰₀

New:

    with the maps of [[def:tl5-hf-coupling]], their operator norms ‖·‖ taken with the norm (|D̂Ψ|² + |Ψ|²)^(1/2) on the jets,
    and 𝔠_n of [[eq:tl5-hf-cn]], and 𝔨₂ := (1/z̲ + max(1/c, 1/κ′))/(2Ω̂²). If 𝔰 ≤ 𝔰₀

### m8 (new Placement item 8: chapter 87 at HEAD, 87:3143-3145)

Old:

    complement estimate on the high angular modes does not lower the constant at any angular resolution. At F² = 10^66.9
    the closing condition 4F²G ε_r < 1 asks a residual ε_r of order 10⁻⁶⁸/G, against the bounds 3.73 × 10⁻⁵ at points and
    5.0 × 10⁻⁴ on sub-boxes of [[prop:tl5-points]] and [[prop:tl5-boxes-second]]. No proof uses these observations.

New:

    complement estimate on the high angular modes does not lower the constant at any angular resolution. At F² = 10^66.9
    a closing condition of the form 4F²G ε_r < 1, with ε_r the size of the residual and G the constant of a quadratic
    remainder, asks a residual ε_r of order 10⁻⁶⁸/G, against the bounds 3.73 × 10⁻⁵ at points and 5.0 × 10⁻⁴ on sub-boxes
    of [[prop:tl5-points]] and [[prop:tl5-boxes-second]]. No proof uses these observations.
