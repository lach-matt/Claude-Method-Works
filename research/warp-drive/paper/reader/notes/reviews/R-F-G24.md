# R-F-G24: review of the G2/G4 fix in chapter 33 (constraint damping)

Base 0b0ec307, fix 003371f6 (the working tree equals 003371f6 for both files). Read: every new or changed statement and
proof of the diff, the old text at 0b0ec307, the chapter 20 and chapter 32 results now cited, and the crosswalk.

**Verdict: NOT CONFIRMED. No Major issue. Two minor issues (G2 attribution; one wrong coefficient in lem:iv4-1-2),
six nits.** Every proof checks: every step, sign and constant. Both minor issues are fixed by editing text; no
argument changes.

## Judgment on the G2 finding

**The paper changes no statement, and the new proofs are correct. But the finding as reported is not a finding:
the old text described the hypothesis of [Hin26a, Lemma 5.14 / Corollary 5.15] correctly.**

I read those results in the preprint (arXiv:2606.27658v2, pp. 58–60):

- [Hin26a, Lemma 5.14] assumes exactly "ℓ(ζ) > 0 for all future causal ζ ≠ 0" and a past timelike ν. Its conclusion
  (5.62) is positivity of the form only on tensors ν ⊗ e + ν′ ⊗ f with ν′ ⊥ ν, not on all of T* ⊗ E. Its proof is
  valid. S± = I ± X > 0 forces spec X ⊂ (−1, 1), so I − X² > 0.
- [Hin26a, Corollary 5.15] is a coercivity estimate *integrated over a time slice*, with an L² error term
  C′∫|ω|². It is proved by Fourier transform in x. For constant coefficients and each frequency ξ, the integrand is
  the form at dt ⊗ e + (ξ·dx) ⊗ f, which is the case of (5.62). Variable coefficients are then handled by a partition
  of unity. This is the Legendre–Hadamard situation: an integrated Gårding-type estimate needs positivity only on
  those tensors, not pointwise positivity of 𝒬.

So under causal positivity alone, both cited results are true, in every dimension. The old chapter applied
Corollary 5.15 slice by slice ("integrated over {r ≥ r_♯, 0 ≤ τ ≤ T_0} twice … with φ²"), which is the use the
preprint makes. Its sentence "The hypothesis on ℓ, positive definite on future causal covectors, is [[lem:iv5-0-4]]"
was accurate.

The writer's counterexample is correct (verified below). It shows that the hypothesis does not give *pointwise*
positivity of 𝒬_(G,η,ℓ) on all of V* ⊗ E. It does not touch the preprint. The counterexample tensor is
f⁰ ⊗ u + f¹ ⊗ sJ₁u + f² ⊗ sJ₂u, which is not of the form ν ⊗ e + ν′ ⊗ f. On tensors of that form the
counterexample's 𝒬 is ≥ (1 − s)(|e|² + |θ|²|f|²) > 0, as (5.62) says.

What the writer did is a **different route**: a pointwise divergence identity (cor:iv5-6-energy (i)) plus pointwise
positivity of 𝒬 for the actual damping symbol (lem:iv5-6-tform (b)). The route is correct and self-contained, and it
avoids the Fourier/partition-of-unity argument. Its price is the extra hypothesis 0 < e < 2/D, which the preprint's
route does not need. That price is real: numerically, at D = 5, 𝒬 has a negative eigenvalue at e = 0.41 for null η
(−0.053) and for the timelike η = dt + ½dx¹-direction (−0.039). The paper's e = 1/102400 < 2/5 meets the condition
with a wide margin, so prop:iv5-6-1 and thm:iv6-2-1 stand as stated.

Consequences:
1. No statement of the paper changes, and every use is valid.
2. The report's "the cited lemma's hypothesis was misdescribed" should not be recorded as a finding about the old
   text or about [Hin26a] (in STATUS, notes or a corrigendum). The correct record: "replaced the slice-wise use of
   [Hin26a, Corollary 5.15] by a pointwise route; it needs e < 2/D, which holds".
3. The headers and crosswalk rows that call the new lemma and corollary "[Hin26a, …] in dimension 4 + 1" are
   inaccurate. These results replace the preprint's; they do not transcribe them (finding m1).

## Findings

### m1 (minor): lem:iv5-6-tform and cor:iv5-6-energy attributed to [Hin26a] as if transcribed

33:1759–1760, current:

    **Lemma {#lem:iv5-6-tform}** (The form T_(G,η,ℓ) and its positivity; [Hin26a, (5.61) and Lemma 5.14] in dimension
    4 + 1.) Let g be a time-oriented Lorentzian inner product on a real vector space V of dimension D ≥ 3, with ⟨·, ·⟩ and

33:1831–1833, current:

    **Corollary {#cor:iv5-6-energy}** (The energy identity and the integrated inequality; [Hin26a, Corollary 5.15] in
    dimension 4 + 1.) Let N ⊂ ℝ_t × (ℝ⁴ ∖ 0) be open, with the coordinates z⁰ = t, z^i = x^i and r = |x|, a Lorentzian
    metric g, a timelike 1-form c, g being time-oriented so that c is past timelike, and e ∈ (0, 2/5). Let ℓ := ℓ_(g,c,e)

What is wrong: "[Hin26a, Lemma 5.14] in dimension 4 + 1" tells the reader that the lemma is the preprint's result
transcribed. It is not. Part (a) is weaker than [Hin26a, (5.62)]. Part (b) is a different statement, pointwise on
all of V* ⊗ E, with the extra hypothesis e < 2/D. The corollary is a pointwise identity with a pointwise lower bound,
whereas [Hin26a, Corollary 5.15] is a slice-integrated coercivity estimate. The headers sit beside the counterexample
paragraph (33:1822, "the hypothesis of (a) alone does not give it"), whose hypothesis is that of [Hin26a, Lemma 5.14].
Read together, they suggest that the preprint's lemma is insufficient, which is false (see the judgment above). The
crosswalk rows repeat the attribution.

Replacement, 33:1759–1760 (the rest of the paragraph unchanged):

    **Lemma {#lem:iv5-6-tform}** (The form T_(G,η,ℓ) of [Hin26a, (5.61)] and its positivity, in place of [Hin26a, Lemma
    5.14].) Let g be a time-oriented Lorentzian inner product on a real vector space V of dimension D ≥ 3, with ⟨·, ·⟩ and

Replacement, 33:1831–1833 (this also carries nit n5; the rest of the paragraph unchanged):

    **Corollary {#cor:iv5-6-energy}** (The energy identity and the integrated inequality, in place of [Hin26a, Corollary
    5.15].) Let N ⊂ ℝ_t × (ℝ⁴ ∖ 0) be open, with the coordinates z⁰ = t, z^i = x^i and r = |x|, a smooth Lorentzian metric
    g, a smooth timelike 1-form c, g being time-oriented so that c is past timelike, and e ∈ (0, 2/5). Let ℓ := ℓ_(g,c,e)

(Line lengths 115, 118, 116, 118, 117. No line starts with a marker.) The intro at 33:1755–1757 is accurate as it
stands ("They are stated and proved here in the form the proofs below use").

Crosswalk, row lem:iv5-6-tform, field 3. Current: `[Hin26a] (5.61) and Lemma 5.14, stated and proved in 4 + 1 (every
D >= 3)`. Replacement: `[Hin26a] (5.61); in place of [Hin26a] Lemma 5.14 (which gives positivity on eta x e + eta' x f
only, enough for its slice-integrated Corollary 5.15): pointwise positivity of Q for l_(g,c,e), 0 < e < 2/D (every
D >= 3)`.

Crosswalk, row cor:iv5-6-energy, field 3. Current: `[Hin26a] Corollary 5.15, stated and proved in 4 + 1`.
Replacement: `in place of [Hin26a] Corollary 5.15 (a coercivity estimate integrated over time slices): divergence
identity with a pointwise lower bound, in 4 + 1`.

### m2 (minor): lem:iv4-1-2 proof, wrong coefficient

33:1096, current:

    ∂_(t_*)∂_ρ-coefficient is 2 Id, there is no ∂_(t_*) times a tangential derivative, and S̄^C is r/2 times the

What is wrong: in −2∂_(t_*)ρ(ρ∂_ρ − …), the ∂_(t_*)∂_ρ-coefficient is −2ρ², not 2. [[prop:np-10-21]] (i), which the
sentence cites, says "the coefficient of ∂_(t_*)∂_r is 2 Id", since −2ρ²∂_ρ = 2∂_r. The line was inherited, but it
sits in the rewritten proof.

Replacement:

    ∂_(t_*)∂_r-coefficient is 2 Id, there is no ∂_(t_*) times a tangential derivative, and S̄^C is r/2 times the

### n1 (nit): prop:iv5-6-1, the δ-weights lack a factor ½

33:1948, current:

    the parts of −a da with the weights 𝔛a² + ρ_sf^(−2α_sf−4)e^(−2𝔛τ)δ(T_0 − τ) and ρ_sf^(−2α_sf−4)e^(−2𝔛τ)δ(r − r_♯).

What is wrong: a = wH(T_0 − τ)H(r − r_♯), so a² = w²H(T_0 − τ)H(r − r_♯) and −a da = −½d(a²). The boundary parts
are ½w²δ(T_0 − τ)dτ and −½w²δ(r − r_♯)dr. This matches the ½ in front of the boundary terms of [[eq:iv5-6-energy]]
against the bulk weight w². The sentence is only an identification and positivity is unaffected, but as written it
disagrees with the corollary by a factor 2. (The weights were the old text's φ², now presented as the weights of
−a da.)

Replacement:

    the parts of −a da = −½d(a²) with the weights 𝔛a² + ½w²δ(T_0 − τ) and ½w²δ(r − r_♯).

### n2 (nit): prop:iv6-1-1 uniformity, propagation constants

33:2379–2380, current:

    [[rem:i-a-5-2-uses]] (ii) for the absorption (Im σ)Re T. Their constants are uniform for σ ∈ I + i[0, ν], I a compact
    interval about ±1 not containing 0, the orders being admissible at every real σ₀ ∈ I with uniform margins, as the

What is wrong: uniformity in σ ∈ I + i[0, ν] is part of the statement of [[prop:i-a-4-6]]. [[prop:i-a-5-2]] is stated
for a single operator P. Chapter 20 gets the uniformity of its constants over σ in the proof of [[thm:i-a-7-2]] (1):
symbols continuous in σ, and finite coverings that serve for nearby σ₀. The sentence should point there.

Replacement (2379 unchanged; 2380 replaced by two lines; 2381–2382 unchanged):

    interval about ±1 not containing 0 (for [[prop:i-a-5-2]] by the argument of the proof of [[thm:i-a-7-2]] (1)), the
    orders being admissible at every real σ₀ ∈ I with uniform margins, as the

### n3 (nit): uniformity at R_out, the size of supp χ₂ against the threshold margin

33:2372, current:

    cut-offs for every σ ∈ e^(i[0,π]), gives the main term (2ℓ + 1)(1 − κξ)a² with 1 − κξ ∈ [¾, 5/4] on supp a, and

What is wrong: when 2ℓ + 1 > 0 (allowed: the threshold is −½ + h⁻¹(1 − e)(1 − v)), the factor 1 − κξ ≤ 5/4 can make
(2ℓ + 1)(1 − κξ) − 2h⁻¹S̄ positive on part of supp a for ℓ close to the threshold. Then the sign is not settled on
supp χ₂ ⊂ [−¼, ¼]. The fix is standard and uniform in σ (|κ| ≤ 1): shrink supp χ₂, which lem:iv6-0-flow (c) already
allows. The real-σ step says "near the zero section", but the uniformity paragraph quotes the [¾, 5/4] range as if
it sufficed. (The case ℓ = −½ used in thm:iv6-3-1 is unaffected.)

Replacement (2372 replaced by three lines; 2373 unchanged):

    cut-offs for every σ ∈ e^(i[0,π]), gives the main term (2ℓ + 1)(1 − κξ)a², where |κξ| ≤ δ₂ on supp a if
    supp χ₂ ⊂ [−δ₂, δ₂]. Take δ₂ with δ₂|2ℓ + 1| < m, m := 2h⁻¹(1 − e)(1 − v) − (2ℓ + 1) > 0 the margin of ℓ at R_out;
    then (2ℓ + 1)(1 − κξ) − 2h⁻¹S̄ ≤ −(m − δ₂|2ℓ + 1|) < 0 on supp a for every σ; and it gives

### n4 (nit): lem:iv5-0-4 statement at 𝗌𝖿

33:1361, current:

    dimension 4 + 1.) At every point of M^♭, [[lem:iv4-1-1]] and [[lem:iv4-1-causal]] hold for (g, c, e), with

What is wrong: c ∈ ρ_sf C^∞(M^♭; 𝒯*) vanishes at 𝗌𝖿 ([[lem:iv5-0-2]] (d)). There (g, c) is not a timelike pair and
G(c)⁻¹c♯ ⊗ c♯ is undefined. The proof (33:1366–1367) applies the lemmas "at K⁺ ∪ 𝗌𝖿 to the rescaled data", that is
to (g, rc), which gives the same B and ℓ_(g,rc,e) = rℓ_(g,c,e). The statement should say so. (The old statement had
the same looseness.)

Replacement:

    dimension 4 + 1.) At every point of M^♭, [[lem:iv4-1-1]] and [[lem:iv4-1-causal]] hold for (g, rc, e), with

### n5 (nit): cor:iv5-6-energy, regularity of g and c not stated

33:1832–1833 ("a Lorentzian metric g, a timelike 1-form c"). Part (i) uses ∇B, ∇ℓ and the curvature, and the
divergence theorem needs Z ∈ C¹. So g and c must be at least C² and C¹, and the text does not say so. Fixed by the
m1 replacement above ("a smooth Lorentzian metric g, a smooth timelike 1-form c").

### n6 (nit): crosswalk row lem:iv6-0-flow

Field 3, current: `[Hin26a] (B.15)-(B.18), (B.16) and (B.23), written out in 4 + 1`. (B.16) lies inside
(B.15)–(B.18), and the chapter header (33:2257) says "[Hin26a, (B.15)–(B.18) and (B.23)]". Replacement:
`[Hin26a] (B.15)-(B.18) and (B.23), written out in 4 + 1`.

## Checked and found correct

**G4.4: lem:iv4-1-1, lem:iv4-1-causal, lem:iv5-0-4 and the eight use sites.**
- lem:iv4-1-1. The quadratic ν² − (3 − e)G(c)ζ_0ν + 2(1 − e)G(c)²ζ_0² + eG(c)G(ζ) is [[prop:np-10-13]] (i) with
  ⟨c, ζ⟩ = G(c)ζ_0, and (ν − G(c)ζ_0)^(D−2) = (…)³ at D = 5. It is the characteristic polynomial of the 2 × 2 block of
  [Hin26a, (3.8)]: I recomputed det = (2 − e)G(c)²ζ_0² + eG(c)G(ζ′) = 2(1 − e)G(c)²ζ_0² + eG(c)G(ζ).
- lem:iv4-1-causal (a). ⟨c, ζ⟩ > 0 on the future causal cone. The discriminant (3 − e)²a² − 4(2(1 − e)a² +
  eG(c)G(ζ)) = (1 + e)²a² − 4eG(c)G(ζ) ≤ (1 + e)²a². Both roots are ≥ (1 − e)a, so λ_min(ℓ(ζ)) ≥ 2(1 − e)a.
- lem:iv4-1-causal (b). The real and imaginary parts of B((G − iℓ)ω, ω), with ℓ real and B-self-adjoint, give the
  conclusion.
- lem:iv4-1-causal (c), (d). F is compact. The continuity of λ_min and the 2ε step (|ζ̂ − ζ̂′| ≤ 2ε from
  |ζ − ζ′| ≤ ε|ζ|) are right. On Γ_0, B(ℓ²ω, ω) = B(ℓω, ℓω) ≥ c₁²B(ω, ω) by Cauchy–Schwarz. The constant
  C = 2(M + 1)c₁⁻² gives ≥ 1 on Γ_δ, the bound off Γ_δ is ≥ δ, and c₂ = min(1, δ).
- The statements agree with [Hin26a, Lemma 3.5, Corollary 3.6, Lemma 3.7] as printed, and (a) adds the explicit bound.
- lem:iv5-0-4. The rescaling ρ_sf⁻²G(ζ) = G(ζ̂) and ρ_sf⁻²ℓ_(g,c,e)(ζ) = ℓ_(g,rc,e)(ζ̂) holds (ℓ bilinear in (c, ζ);
  B invariant under c ↦ λc). The pairs (g, rc) are continuous on the compact Ω, rc is past timelike
  ([[lem:iv5-0-5]] (1)), and at 𝗌𝖿 ĉ = dt − v dr is η-past timelike.
- Use sites checked: lem:iv4-1-5 (horizon conormals future null, c_C past timelike there by [[prop:np-10-14]] (i));
  lem:iv5-1-1; prop:iv5-1-3 (conic neighbourhood of the light cone, (d) via the compact family of lem:iv5-0-4);
  prop:iv5-5-3; prop:iv5-6-1 ((5.77): ρ_sf a d(ρ_sf a) future timelike for 𝔛 large, δ-parts future timelike);
  lem:iv5-8-1; thm:iv6-2-1 (b_cf, e_τ, via lem:iv5-0-4).

**G4.3: lem:iv4-1-2.**
- In the frame dt_*, dx^i: A = dt_* ⊗_s · is constant. D_gk = −k(·, g⁻¹(dt_*, ·)), and Δ_g, δ^(0)_g ∈ ρDiff¹_b.
- The differences lie in ρ³Diff⁰_b, ρ²C^∞, ρ²C^∞ and ρ³Diff¹_b; I checked each term.
- The expansion of □^C into ∂_(t_*)², ∂_(t_*) and 0-th order parts is right. 2D_gG_gA = −G(dt_*) Id, which vanishes for
  ḡ (ḡ⁻¹(dt_*, dt_*) = 0, with t_* = t̄ − |x| exactly; chapter 32, sec:iii-d-2). So R = −g_b^00 Id ∈ ρ²C^∞.
- Q ∈ ρ³Diff¹_b; P^C_b ∈ ρ²Diff²_b and P^C_b − P̄^C ∈ ρ⁴Diff²_b. S̃ = 0 is consistent with eq:iv4-1-1.
- lem:iii-d2-2-1 and eq:iii-d2-2-3 (chapter 32) exist with the content used.

**G2: lem:iv5-6-tform.**
- 𝒬 is symmetric (T symmetric in (ζ, ζ′), with B-self-adjoint values). The basis formula and the rank-one value are
  right.
- (a): T(ζ) = ℓ(μ), G(μ) = G(ζ)²G(η) ≤ 0, and ⟨μ, η⟩ = s²G(η)² − G(ζ′)G(η) > 0, so μ is future causal.
- (b), checked symbolically with sympy for D = 3, 4, 5, 6, 7, every display computed from the definitions:
  - b(ζ; ω, ω′) with G(c) = −1;
  - the splitting ½𝒬 = 2Σ⟨η, f^μ⟩β(ξ_μ) − Σε_μ b(η; ξ_μ, ξ_μ);
  - β(w), b(c; ω, ω) and b(n; ω, ω);
  - ½𝒬_(G,c,ℓ) and ½𝒬_(G,n,ℓ);
  - the sum of squares for ½𝒬_(G,c+n,ℓ).
  All coefficients are positive for 0 < e < 2/D ≤ 2/3. The equality case gives the nullspace η ⊗ V*. The timelike
  case is a positive combination of two non-proportional null covectors, with trivial intersection of nullspaces.
  The reduction to η = c + n by scaling and linearity is right.
- Counterexample, verified: ℓ(ζ) has eigenvalues α ± s|θ| > 0, and 𝒬_(G,f⁰,ℓ) = 1 + 2s² − 4s² = 1 − 2s² < 0.
- (c): the minimum is continuous and positive by (b). The complex extension is right.
- Numerically at D = 5, e = 1/102400: the least B-normalised eigenvalue of 𝒬 over 200 random past timelike η is
  ≥ 0.10.

**G2: cor:iv5-6-energy.**
- (i), the pointwise identity, re-derived by hand. B(□ω, Y) = −∇^μ(B(∇_μω, Y)) + (∇^μB)(∇_μω, Y) + B(∇_μω, ∇^μY).
  The second-derivative term is ½∇_λJ^λ − ½(∇_λ(Bℓ^λ))(∇_μω, ∇^μω), by the symmetry of Bℓ^λ and ∇g = 0. This gives
  Z^μ and 𝓡 exactly as printed.
- 𝒬_(G,η,ℓ)(∇ω) = 2⟨dz^μ, η⟩B(∇_μω, ℓ⟨∇ω⟩) − η_λJ^λ. (df_i)_μZ^μ = −½w²𝒬_(G,df_i,ℓ)(∇ω).
- The divergence theorem with outward conormal df_i on {f_i ≤ 0} and |dg| = |df_i| ⊗ σ_i gives eq:iv5-6-energy.
- (ii): scaling 𝒬 = r⁻⁴|rη|𝒬_(G,η̂,ℓ_(g,rc,e))(rξ). The compact set of triples satisfies the hypotheses of (c)
  (⟨ĉ, η̂⟩ ≤ 0 with both timelike means the same cone). ½𝒬_(G,2w²η_0,ℓ) = w²𝒬_(G,η_0,ℓ).
- (iii): the orders O(r⁻¹) for Γ, ∇B and ℓ, and O(r⁻²) for Rm, ∇ℓ and ∇(Bℓ), give |𝓡| ≤ Cr⁻⁴(…). Second derivatives
  along r∂ are needed for Rm, as stated. The −ℓ case follows by c ↦ −c.

**Applications.**
- prop:iv5-6-1, (5.66): the pairing convention (linear in the first slot, as (5.70)'s −h⁻¹‖aL_hω‖² requires) and
  L_h = −ihℓ⟨∇·⟩ + 2ih𝒩 (from M^μ = −½ℓ^μ in [[prop:np-10-13]] (ii)) give the main part h²∫_R B(□_gω, w²ℓ⟨∇ω⟩), with
  the right sign against the symbol aT_(G,da,ℓ).
- −d(w²) = 2w²(𝔛dτ + (α_sf + 2)dρ_sf/ρ_sf). f_1 = τ − T_0 and f_2 = r_♯ − r have independent differentials.
- r η_0 = 𝔛(dt − τ dr) − (α_sf + 2)dr, r dτ = dt − T_0 dr (G ≤ −¾) and −r dr (G ≤ −½|r dr|²) satisfy (ii) with one
  κ for 𝔛 large.
- K₀ is compact, e < 2/5, and (iii) holds with components in C^∞(M^♭). Density handles R ∩ supp ω not compact.
- (5.68), (5.67), (5.69) as stated.
- thm:iv6-2-1: k = 1, the components of η and rc = dt − v x̂ · dx are bounded with their r∂-derivatives,
  η⁻¹(r dτ, r dτ) = −(1 − τ²) ≤ −¾, and r dρ_sf/ρ_sf and r dρ_cf/ρ_cf are bounded.

**G4.1, G4.2: lem:iv6-0-flow and prop:iv6-1-1.**
- eq:iv6-0-flow re-derived from P = ρ⁻²ξ and W = ρ⁻¹η. The ±2ρξ(∂_ξp)∂_ξ terms cancel. At ρ = 0 it agrees with
  [[eq:i-a-4-4]] under ξ ↦ −ξ (dρ/ρ² = −dr).
- σ⁻¹G_σ = p_σ − iq_σ, with q_σ ≥ 0 for Im σ ≥ 0.
- (a) holds.
- (b): p_σ = σG_σ, the sphere (ξ − σ)² + |η|² = 1, and 𝖧 = 2(σξ − 1)(ρ∂_ρ + η·∂_η) − 2σ|η|²∂_ξ + σH_(|η|²). The zeros
  are exactly R_in ∪ R_out. With y = σξ − 1, ẏ = −2(1 − y²) and y = −tanh(2(s − s_0)), so |η| = sech(2(s − s_0)). The
  ω-speed 2|η| is integrable. ρ⁻¹𝖧ρ = ±2.
- The directions match [[lem:i-a-4-5]] for both signs of σ.
- (c): all four terms of 𝖧_(p_σ)a, |κ| ≤ 1, and the signs from χ_0χ_0′ ≤ 0 and χ₁χ₁′ ≤ 0.
- prop:iv6-1-1. The conjugation identity holds: t_* ∘ Φ = −t_* − 2r, Φ*(e^(−iσt_*)u) = e^(iσt_*)e^(2iσr)Φ*u, hence
  e^(2iσr)(□^C)^(σ)e^(−2iσr) = Φ*(□′)^(−σ)Φ*⁻¹.
- The model satisfies (H1)–(H2) of [[sec:i-a-1-3]] near ρ = 0: T = 2iρ(ρ∂_ρ − 3/2 − h⁻¹S̄), Q = 0, P₂ = 0, and
  ρ⁻²(□^C)^(0) − ((ρD_ρ)² + Δ_(𝕊³)) Id ∈ Diff¹_b.
- ϑ_in of [[eq:s14-theta-in]] gives the threshold −½ − h⁻¹(1 − e)(1 + v). The thresholds agree with def:iv6-0-2 and
  with (O3) of chapter 20 (S̄ = h⁻¹(1 − e)(1 − v)).
- The lines "(2ℓ + 1)(σ − ξ)" and "(−1)(−2(−h⁻¹)S̄_(−v))" are inherited, and they are right at σ = 1 and for the
  reversed operator.

**Chapter 20 (re-sourced, F-G5), current text.**
- prop:i-a-4-6: radial estimate at R_(Re σ,in), constants uniform on I + i[0, ν], threshold 𝗋 > (−1 + ϑ_in)/2.
- prop:i-a-5-2: propagation for a general P with hypotheses (a)–(d).
- rem:i-a-5-2-uses (ii): boundary face, σ₁ ≥ 0, absorption σ₁Re_hT.
- lem:i-a-7-1: orders admissible on a neighbourhood J of σ_* with a margin independent of σ₀.
- prop:i-a-4-9: R_out, uniform on compact 𝒟 ⊂ {Im σ ≥ 0}.
- eq:i-a-4-4, sec:i-a-1-3 (H1)–(H2), and (O2) "orders for complex σ are those for σ₀". This settles the writer's
  open point 2 in the reading the proof uses.
- All exist with the content used.

**Other.**
- The hunk "which [[lem:iv4-1-4]] restates" (33:554): correct. lem:iv4-1-4 lists conditions (1)–(6) of
  [Hin26a, Proposition 5.1] in 4 + 1.
- No other chapter cites [Hin26a, Lemma 5.14 / Corollary 5.15] or the new labels. Chapter 36's "Corollary 5.15" is
  [Hin26], a different paper.

**Form.**
- Crosswalk: 181 rows, 181 labels, same order as the chapter, 4 tab-separated fields per row, labels lowercase.
- `python3 lint.py --chapters`: 62 files, 4593 labels, 0 hits. `python3 assemble.py --check`: 0 problems.
- Chapter 33 after label resolution: 0 lines over 121 characters, no wrapped line starting with "+ ", "- ", "* ",
  "> ", "#", "=" or "|", no backslash.
- Every proposed replacement line above is ≤ 121 characters before and after resolution and starts with no marker.
