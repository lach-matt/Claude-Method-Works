# F-P-K82: fix round for proofs/P-K82.md (the radial pair of chapter 82)

Input: reviews/R-P-K82.md (NOT CONFIRMED: 1 Major, 11 minor, 9 nits), plus four coordinator inputs received while
working: F3-81 §"Chapter 82's proof project" (five items), R3-82's new Major in prop:vlasov-uniform-n, F4-82 §"For the
P-K82 merge" (four items; F4-82 repaired that Major in chapter 82), and F4-81 §"Consequence for proofs/P-K82.md" (three
items and one optional). All four are applied (section "Coordinator inputs applied").

File changed: `research/warp-drive/paper/reader/proofs/P-K82.md` only (578 → 741 lines). No chapter edited, nothing
committed. Private checks: `scratchpad/reader/f_pk82/` (c1_identities.py, c2b_kappa.py, c2c_control.py, contract.py,
anchors.py, reflow.py; pre-reflow copies P-K82.before-reflow*.md).

Shell note: every Bash call longer than about 25 characters failed with E2BIG (the harness adds a 128 KB argument).
Scripts ran through a one-line launcher `/tmp/claude-0/k8.sh` (Claude's temp directory, outside the repository), which
runs `scratchpad/reader/f_pk82/run.sh`.

## Outcome

- **Major M1: fixed by localising the labels only.** The n-dust developments (part (a)(1) of
  prop:vlasov-radial-background) are now "the proof of prop:vlasov-uniform-n, run on the adapted domain": the labels are
  localised as in parts (i)–(iii) of the proof of lem:vlasov-local-stability ((H1′), (H2′) of that lemma by (V1), (V2);
  eikonals on their tubes only); the radial pair is not localised (ζ′_𝔨 := 1, P̃_𝔨 := P_𝔨), satisfies (H1) of
  thm:class-stability-off-axes and (H2′) of thm:class-stability, and Step 10 gives its phases as eikonals on the whole
  adapted domain. prop:vlasov-radial-step is restated in the setting of sec:vlasov-n (S_A, 𝒱_A, 𝒯_A, item (v)), with the
  pair as two further families, S_𝔨 := Σ_τ0 ∩ Ω, 𝒱_𝔨 = Ω, (v) holding for it trivially. The four sites the review names
  (old 322–326, 417–419, 428–431, 529–530) are rewritten; see the table below.
- **All four gaps are closed by written proofs** (section "The four gaps").
- **Statements that changed:**
  - prop:vlasov-radial-step: hypotheses now in sec:vlasov-n's setting; its own item renamed (vi).
  - prop:vlasov-radial-background (b): labels eikonal on their tubes only, pair eikonal on the whole adapted domain; per-
    family clause added; the n-dust datum is that of g_ε on Σ_τ0 ∩ Ω₂^𝔡 (𝔡 and Ω₂^𝔡 now fixed in the setting).
  - cor:vlasov-two-dust: "on Ω₂′ it is a weak limit" (m5); a′ − a < δ0/4, V′ ∈ (V − δ0/4, V) (m7); threshold renamed
    ε_* (ε1 is the admissibility margin in chapter 82); g_ε is "the solution of prop:vlasov-radial-background (a)", no
    uniqueness claimed (the uniqueness of prop:vlasov-cauchy is narrowed to ε2 and is not used).
  - lem:vlasov-radial-wave (c), lem:vlasov-axis-smooth, lem:vlasov-axis-commutator: same content, new notation.

## Findings, one by one

| Finding | What changed |
|---|---|
| M1 (a) old 428–431 | (a)(1) rewritten as above. Taken from the review's text, with additions: the two new changes of thm:class-stability (Step 3 with the tube of T_(τ0,U)(S_A); Step 6 cut-offs vanishing on 𝒰_(r_B)), how the labels' transport fields keep dF > 0 on the adapted boundaries, the joint Gronwall of Step 10 for (D, label defects on 𝒯′_A, pair defects on thm:class-stability's sets), the residual E_n(P̊_𝔨, P̊_𝔨) in the pair's Raychaudhuri equations, and the sentence that the changes of the proof of prop:vlasov-uniform-n (weighted norm, each family alone, cut-offs) concern the labels only. |
| M1 (b) old 417–419 | (b) now gives Ric(g^(n)) = Σ_A q_A du_A ⊗ du_A + Σ_𝔨 q_𝔨^(n) dϕ_𝔨^(n) ⊗ dϕ_𝔨^(n), u_A eikonal on 𝒯_A as in prop:vlasov-uniform-n, ϕ_𝔨^(n) eikonal on the whole adapted domain (review's text). |
| M1 (c) old 322–326 | prop:vlasov-radial-step's opening is the review's text (setting of sec:vlasov-n plus two further families, S_𝔨 := Σ_τ0 ∩ Ω, 𝒱_𝔨 = Ω), with a first proof sentence showing 𝒱_𝔨 = Ω from (i) and that (v) holds for the pair trivially. |
| M1 (d) old 529–530 | Corollary proof: "The setting of sec:vlasov-n, (iii), (iv), (iii′) and (vi)" paragraph, the review's text, with S_A := S″_(α_A), u_A extended by a cut-off (which changes neither Ric nor the amplitude transport), (iv) with δ/2 (lem:vlasov-open halves δ). |
| m1 (O4) | Block 3 no longer replaces the remark. It makes two local edits: (O1) gains the radial-pair clause; (O4)'s last clause becomes "the waves of the labels are torus-polarised; those of the radial pair have an orbit part, a multiple of q̂ ⊗ q̂ on Σ_τ0, and leave no such term because their phases are radial there". The narrowed (O4) stays verbatim. |
| m2 block 1 anchor | Block 1 anchors on the sentence "The last section shows … ([[lem:vlasov-open]], [[prop:vlasov-nonempty]])." (present once in chapter 82), with "of [[cor:class-two-dust]]" after "the adapted domain". |
| m3 n vs 𝔫 | The unit normal is 𝔫 throughout (𝔫0 for g0). |
| m4 (a) (v) | prop:vlasov-radial-step's item is (vi), at all uses. |
| m4 (b) (H2′) | "(H2′) of [[thm:class-stability]]" or "(H1′) and (H2′) of [[lem:vlasov-local-stability]]" at every use. |
| m5 | "and on Ω₂′ it is a weak limit of class vacuum metrics". |
| m6 radial kernel | Gap 1 below. Step (0) of the proof of prop:vlasov-radial-step, and the optional Block 4b. |
| m7 width | Gap 2 below. |
| m8 outer boundary | Gap 3 below. |
| m9 varying domains | Gap 4 below. |
| m10 du(∂_R) | "(proof of [[cor:class-two-dust]]: dϕ_out(∂_R) = (1 − R_v)/R_u with R_v ≤ ½, and R_u < 0 by [[prop:two-dust-background]] (c))" — checked against cor:class-two-dust's proof (81:1644 ff.). |
| m11 u twice | ϕ_out for the outgoing phase everywhere after the setting; "(below, u denotes the labels)". |
| nit 1 | "𝔢_ϑ ≤ −1/√3 everywhere, the axes included, since cos(π𝔷/3) ≥ ½ …". |
| nit 2 | 𝔊 := γ0 + α dr ⊗ dr. |
| nit 3 | Template 𝒳 (not 𝒯); torus curvatures named once as "the torus curvatures κ_i of [[prop:class-structure]] (not the parts κ1_A of a second fundamental form)"; Q1, Q2 dropped (the forms are written out); E only the energy (as in lem:vlasov-separation); s only an integration variable (chapter practice); H the Hessian with "(as in [[lem:vlasov-no-shear]])", as the chapter does; σ_i the planar shear with "(not the shift of the spheres)". |
| nit 4 | "≤ C (sup 𝒩_k + ε) ≤ C (ε + n⁻²)". |
| nit 5 | Not taken as written (see departures). |
| nit 6 | "… is annihilated by its own generator and is trace-free". |
| nit 7 | Block 2: "the weak limit then holding on domains of the type [[eq:omega]] inside the adapted domain of [[cor:class-two-dust]]". |
| nit 8 | 𝒯̊_in, 𝒯̊_out throughout (as cor:class-two-dust writes them). |
| nit 9 | "after the replacement of the labels made there/in [[lem:vlasov-open]]" at both sites. |

## Departures from the reviewer, with reasons

1. **nit 3, symbol of the template.** The review suggests 𝒵 for the template. But the polarisation 𝒫 clashes with the
   mollifier 𝒫 of chapter 82 (thm:vlasov-n-uniform: "𝒫 is the mollifier of [[lem:mollifier]]"), which the new step (0)
   uses in the same proof. So the polarisation is 𝒵 (𝒵0, 𝒵_𝔨) and the template 𝒳.
2. **nit 5.** "The identity agrees with lem:two-dust-commutator … up to the grouping of the terms of first order" was not
   verified, so it is not stated. The text says what is verified: on the round background σ_i = 0 and a = 2Θ_h = 2L(R)/R
   is the coefficient of lem:two-dust-commutator (cor:vlasov-commutator states a = 2L(R)/R there).
3. **m7.** The review's change is applied, and the text states also that the lemmas of ch:inequalities then hold with
   eq:lambda-one read with δ0/2 (λ1 = min(1, δ0/2)/10): with δ0/2 in the width bound but the old λ1, the bound
   λ/(b − a) ≤ 1/20 of lem:shift-map can fail for δ0 ∈ (2/3, 2).
4. **m8.** Applied, but 𝔡 (the review's ι) is now fixed in the setting of the corollary (needed by the statement of (b)),
   with the three conditions 2𝔡 ≤ min(a′ − a, V − V′), 𝒯̊_out ⊂ {R ≥ a + 2𝔡}, 𝔡 < V + 1 − v_end − η.
5. **m9.** The review's text presupposed that the limit of the maps is T_(τ,U) for the limit U, citing
   lem:class-leaf-differences (b), which bounds planar shears, not leaves. The written proof (gap 4) instead identifies
   the limit leaf through the Volterra equation and the uniqueness in lem:class-volterra.
6. **M1 (a).** Besides the review's text, the labels' Step 9 transport fields are no longer called "future causal": after
   F4-82, prop:vlasov-uniform-n's Step 9 field P̃_A^♮ need not be causal off the tubes; the text says only what both
   versions give (transverse, P̃_A(τ) ≥ c/2, dF(P̃_A) ≥ c′/2, and c′/4 on the adapted boundaries).

## The four gaps and their proofs

1. **The mollifier needs a radial kernel.** Step (0) of the proof of prop:vlasov-radial-step: ρ is taken radial (allowed:
   (M1)–(M6) hold for every admissible ρ). The shift map Φ of eq:mollifier is radial, so for R ∈ O(4)
   𝒫(f∘R)(x) = ∫ρ(z) f(RΦ(x) − λRz) dz = ∫ρ(z′) f(Φ(Rx) − λz′) dz′ = (𝒫f)(Rx). T² and both reflections act by elements
   of O(4) fixing τ. The phase shifts solve the coupled linear transports ℓ_B·dφ_B = ½ 𝒫 s_B(w − Σ_C φ_C Y_C) with zero
   data; ℓ_B, Y_C and w = g − g_app are invariant, so the system commutes with the action and, by Picard uniqueness, every
   φ_B (labels and pair) is invariant. Step (2) then applies lem:vlasov-axis-commutator, which needs φ invariant. Block 4b
   (optional, one sentence before thm:vlasov-n-uniform) closes the same gap for the labels in step (4) of that proof.
2. **Ω₂′'s slices narrower than 1 + δ0.** With a′ − a < δ0/4 and V − V′ < δ0/4, the outer radius of Ω₂′ is
   b(τ) − (V − V′) > a′ + 1 + δ0/2, since b(τ) − a ≥ 1 + δ0 (lem:two-dust-domain (f)); so the slices satisfy the bound of
   lem:domain (f) with δ0/2, on which the lemmas of ch:inequalities rest, with eq:lambda-one read with δ0/2.
   rem:vlasov-radial-scope notes that the restriction costs nothing (Ω₂′ grows as a′ ↓, V′ ↑).
3. **𝔡 at the outer boundary of Ω₂^𝔡.** There v = V − 𝔡 + 1 + τ_end − τ ≥ V − 𝔡 + 1 > v_end + η because
   𝔡 < V + 1 − v_end − η, positive as V + 1 > v_end + η (proof of cor:class-two-dust). The inner side: 𝒯̊_out compact and
   off {R = a}, so 𝒯̊_out ⊂ {R ≥ a + 2𝔡} for 𝔡 small; and μ ≥ μ0 > (a + 𝔡)² at R = a + 𝔡 since a + 𝔡 < a′ < √μ0.
4. **The limit on varying domains.** Part (a)(3), two paragraphs:
   - Pull back by Φ_n(τ, x) := (τ, T_(τ,U_n)(x)). The U_n are bounded in every C^j(Ω_n) uniformly in n (clause on m′ of
     prop:vlasov-uniform-n; Sobolev on the slices of Ω_n with a uniform constant through the extension 𝔼 of the proof of
     thm:class-stability), and the Φ_n in every C^j(Ω₂) (bound of def:class-adapted at every order and for τ-derivatives).
     Arzelà–Ascoli: Φ_n → Φ = (τ, T_τ), U_n∘Φ_n → U_Φ in every C^j(Ω₂). DT − I ≤ ½ passes to the limit, so Φ is a
     diffeomorphism onto Ω_∞ and U := U_Φ∘Φ⁻¹ is smooth there. The bi-Lipschitz bound gives
     |T_n⁻¹(y) − T⁻¹(y)| ≤ 2 sup|T_n − T|, hence U_n(y_n) → U(y) with derivatives whenever y_n → y, and convergence in
     every C^j on compact subsets of Ω_∞ off its lateral boundary.
   - Ω_∞ is the adapted domain of U: the axis points z_B(τ) of the U_n converge to that of U (same datum phase, integral
     curves in the axis converge, monotonicity of the axis phase); the leaves h_B of the U_n are bounded in every C^j and
     lie in the lateral boundaries of the Ω_n, so a subsequence converges to h on the lateral boundary of Ω_∞; the
     coefficients of eq:class-leaf-volterra converge, so h solves the equation of U (for any smooth extension of U) with
     h(0) = z_B(τ), and by the uniqueness of lem:class-volterra h is U's leaf; d_B converges (Stein's operator and the O(2)
     average are linear and bounded on W^(j,∞)); so T_(τ,U_n) → T_(τ,U) = T_τ. The pair of U: closed null limits of the
     dϕ^(n)_𝔨, hence dϕ^ε_𝔨 on the simply connected Ω_ε.

## Further changes not asked for, with reasons

- **Notation clashes with chapter 82 and the contract:** template entries λ_ϑ, λ_1, λ_2 → 𝔢_ϑ, 𝔢_1, 𝔢_2 (λ is the
  wavelength only); ζ (the chapter's cut-offs ζ′_A, ζ_A, ζ(k), the ζ of lem:vlasov-constraint-coefficient (c)) → 𝔷;
  s(y) → 𝔥(y) and chart coordinates (s, y) → (x′, y) (s is the contraction s_A(h)); the auxiliary t → c_𝔷, s_𝔷; ν0 → 𝔯
  (ν is a frequency); ν̂ removed (ℓ̄ := E⁻¹𝔫 − (2E²)⁻¹ℓ, checked equal); V (vector field) → 𝔙 (V is the domain constant);
  Y → 𝔜; S_r → 𝕊_r and π → 𝔭 (S and π are used); ι → 𝔡 (ι is an isometry in chapter 82 and ι⁺ is reserved); the lapse
  N removed (N is reserved: the κ1 identity is now derived from κ = ½ 𝓛_𝔫 g, re-checked, see below); the class 𝓔 of
  lem:vlasov-axis-smooth → 𝔄 (𝓔 is an energy in chapter 82); c_σ → c_vu and the formula −e^(−2σ) removed (σ, ψ of
  chapter 80 clash with chapter 82's ψ := ψ1 + ψ2); the round-slice function G of lem:two-dust-slice not written (G is
  the group); F_𝔨 kept for the pair's amplitudes, with one disclaimer that it is not the phase derivative written F_𝔨 in
  ch:two-dusts; threshold ε1 → ε_*.
- **The κ1 identity** moved into step (3) of the proof of prop:vlasov-radial-step, for family 𝔨, with a lapse-free
  derivation (fast derivative of λW in 𝔫^c∂_c g; ∂_i𝔫 = ∂_i𝔫0 + O(λ) because every W_B(g0⁻¹dτ, ·) vanishes on Σ_τ0 for
  every θ: labels by the torus part, pair by (iii′), gauge parts by construction).
- **Ω₂′ as a domain of dependence.** The corollary's proof now says why the fields restrict to Ω₂′ (and part (b) to
  Ω_ε^𝔡): rays from points of S_α outside never enter, and leaving rays never return; (V1), (V2), (V2′) restrict with
  S ∩ ((Σ_τ0 ∩ Ω₂′) × S¹), whose sections are invariant.
- **Label–radial separation** rewritten as an explicit ray comparison: rays and covectors of g^(n) and g0 with the same
  data differ by C(ε + C_k n^(−k)) (Gronwall for the geodesic equations, |g^(n) − g0|_(C¹(Ω₂′)) ≤ C(ε + C_k n^(−k))); y is
  then in D_(α_A)(S′) ∩ 𝒯̊_𝔨 for g0, (V2′) applies at y, and the covector errors are C(ε + C_k n^(−k)).
- **Stage data at the axes:** "onto at every point of Σ_τ0 ∩ Ω, the axes included … its right inverse commuting with the
  symmetries" (lem:stage-data's Pol is onto pointwise everywhere; Pol⁺ is the Euclidean pseudo-inverse).
- **Amplitudes of the pair:** transported by eq:vlasov-amplitude, now proved directly (ℓ_𝔨(ϕ_𝔨) = 0 and
  □5 ϕ_𝔨 = 3ℓ_𝔨(R)/R from the formula for □_(g0) in the proof of lem:two-dust-commutator).

## Coordinator inputs applied

- **F3-81 (five items).** 1: header now describes d_B (O(2)-averaged Stein extension of h_B − h̊_B from D_B), the datum on
  W_0 or on Σ_τ0 ∩ Ω, and the normalisation. 2: (a)(2) invokes the last paragraph of def:class-adapted and the last
  sentence of cor:class-two-dust. 3: (a)(3) builds the maps from the integral curves of P_𝔨 in the axes and the leaves
  through z_B(τ) over D_B, extended by the averaged Stein operator (and gap 4 proves the convergence). 4: (b) says "in the
  sets 𝒰_(2δ_B) … the level sets of ϕ_in^ε and ϕ_out^ε at the values c_B(τ) …, these sets serving as the 𝒱_B". 5: (b)
  gives the reason T_(τ0,·) is the identity. All checked against chapter 81 (1,666 lines, after F4-81).
- **R3-82 Major / F4-82.** P-K82's part (a) runs the existence part of prop:vlasov-cauchy at d(D_ε) ≤ Cε > 0, which is
  exactly the case R3-82 found broken. It is written so that it holds with the repaired proposition (now in chapter 82:
  𝒩^∞, change (5), Step 9 change (6) with the scaled unknowns and the cut-off P̃_A^♮, and the statement's clause on each
  family alone): the pair enters every norm with weight one as one of a fixed number of families, the bound on each label
  alone holds as it is, and the labels' terms in the pair's equations are bounded "as the Ricci terms of (2) of that
  proof are". (b) and the diagonal use d = 0. No argument of P-K82 uses the weighted norm to bound a single family.
- **F4-82 (four items, reports/F4-82.md "For the P-K82 merge").** 1: (a)(1) now says "The changes (1)–(6) of the proof
  of prop:vlasov-uniform-n concern the labels only" and names them (weighted norm; 𝒩^∞ of each label alone in the
  bootstrap; in Step 9 the label unknowns scaled by (2π/n)^(1/2) with the cut-off on their covectors), the pair entering
  every norm with weight one, unscaled. 2: the pair's Ricci terms are bounded "by C times the weighted family norm plus
  C (𝒩^∞)²", as the Ricci terms of (2). Step 9 on the adapted domain: a sentence states that the threshold argument of
  (6) carries over (block-diagonal A^0 with the pair's transports unscaled and with their own cut-off, Sobolev constant
  independent of the number of components, the extension 𝔼 of thm:class-stability acting componentwise with a uniform
  bound, r_b set by the wave block). 3: the field's S is stated with invariant sections (as (V1) and lem:vlasov-open now
  ask); its restriction to Ω₂′, Ω₂^𝔡 keeps them; the pair is O(4)-invariant. 4: (b) cites the clause of
  prop:vlasov-uniform-n on each family alone, and (a)(1) ends with "each label is bounded alone, uniformly in n, as in
  the statement of prop:vlasov-uniform-n". Checked against chapter 82 at 1,774 lines.
- **F4-81 (three items and the optional fourth).** Header: normalisation at "a fixed point of Σ_τ0 ∩ Ω outside the 𝒱_B",
  "normalised phases", the support condition supp q_A ∩ Σ_τ0 ∩ Ω_U ⊂ T_(τ0,U)(S_A) and its T = id form. (a)(2): the
  normalisation is trivial, the normalised radial phases take the values c_B(τ0), T_(τ0,U) = id, the datum on Σ_τ0 ∩ Ω₂
  suffices, and supp q_A ∩ Σ_τ0 ∩ Ω₂ ⊂ S_A is stated and checked (radial densities in S_in, S_out; label densities in
  S_(α_A), off the axes). (b): the same on Σ_τ0 ∩ Ω₂^𝔡. (a)(1): the new Step 3 (tube of T_(τ0,U)(S_A) = S_A here) and
  Step 6 (cut-offs of families other than A(B) vanishing on 𝒰_(r_B), r_B ≤ δ_B ≤ δ/4) are recorded; the labels' ζ′_A
  (vanishing within δ of the axes) and the pair's cut-offs (packet hypothesis) meet them.

## Dependencies (for checking later changes quickly)

**Chapter 82 (as after F4-82, 1,774 lines).** Anchors, each present exactly once (whitespace-normalised):
"We prove the five-dimensional counterpart"; "The last section shows that the hypotheses are open and that an explicit
family on Tangherlini meets them ([[lem:vlasov-open]], [[prop:vlasov-nonempty]])."; "No smallness of g or of the field
is assumed."; "Radial null dusts reaching the axes, added to T_V: [[pending:issue-82-radial]]."; "**Remark
{#rem:vlasov-obstructions}** (What the hypotheses avoid.)"; "([[lem:vlasov-axis-phases]]): the labels are kept off the
axes."; "([[lem:vlasov-constraint-coefficient]] (c)): the waves are torus-polarised."; "its smallness at each n being λ
alone."; "### Openness, stability and an explicit family {#sec:vlasov-open}"; "Let s_A(h) := h(ℓ_A, ℓ_A)"; "𝒫 is the
mollifier of [[lem:mollifier]]."

Hypotheses and items: (Ω) (including its statement on rays), (V1) (neighbourhood 𝒲 of 𝒟(S) uniform in the label;
S with invariant sections), (V2), (V3); sec:vlasov-n's setting (S_A, 𝒱_A, 𝒯_A) and items (i), (ii′) (with m*, Ē),
(iii), (iv), (v) *Localisation* (a)–(c); (H1′), (H2′) of lem:vlasov-local-stability, its cut-offs ζ′_A vanishing within
δ of the axes, its parts (i), (ii), (iii) and eq:vlasov-localised; prop:vlasov-uniform-n: its proof's changes (1)–(6)
(weighted norm, matter identity and Ricci terms (2), residuals (4), each family alone (5), Step 9 (6)), the clause on m′,
the clause on each family alone, the residual ζ′_A E_n(P̊_A, P̊_A), the definition of a datum in label form and of the
n-dust datum before it; prop:vlasov-cauchy, existence part only (n-dust limit, eikonals u^(n)_α, Riemann sums, gauge);
lem:vlasov-open (after the replacement of the labels: (V1) with margins halved, (V2) with δ/2); thm:vlasov's proof (the
comparison of rays, (ii′), (iii), (iv), S′, S″, the diagonal, the wave bound); thm:vlasov-n-approximant (stage 0),
thm:vlasov-n-uniform (steps (1)–(5), the mollifier 𝒫), thm:vlasov-n-data (Pol_A, stage data, phase corrections zero on
Σ_τ0); def:vlasov-label (rays, tubes, branch), def:vlasov-wave, lem:vlasov-wave (and T0 in its proof),
lem:vlasov-constraint-coefficient (a)–(c), lem:vlasov-leaf-curvature (its H̃, σ, σ0, ν, ν_U² = ν² + α),
lem:vlasov-no-shear, cor:vlasov-commutator (𝔐′, 𝔐, 𝔑, a = 2□3 u), sec:vlasov-scaled (class [h], (C0), 𝔏, 𝔓),
lem:vlasov-structure, lem:vlasov-symmetrizer, prop:vlasov-scaled-correction, lem:vlasov-trapezoid, lem:vlasov-separation
(and eq:vlasov-mixed-angle), lem:vlasov-hierarchy, eq:vlasov-symbol, lem:vlasov-axis-phases, eq:vlasov-amplitude,
eq:vlasov-dust, eq:vlasov-box, eq:vlasov-class (ψ_i, ψ), prop:vlasov-nonempty (d(D_ε) ≤ Cε argument).

**Chapter 81 (1,666 lines, after F4-81).** def:class-admissible (a)–(c); thm:class-stability-off-axes (H1), Steps 1–10;
lem:class-transport; prop:class-augmented (b); prop:class-structure (a), (b); prop:class-axis (a), (d) (a_⊥ positive,
planar shear σ := Θ_h − κ2 extending by 0); def:class-adapted (𝒱_B within δ of the axes, δ_B, C_L, 𝒰_(2δ_B), W_0,
normalisation outside the 𝒱_B, axis phase and z_B(τ) with monotonicity, d_B, T_(τ,U) and its W^(k,∞) bound with
τ-derivatives, T − id with derivative ≤ ½, the paragraph on determination by U on the closure of Ω_U, the T = id
paragraph); thm:class-stability ((H2′), the support condition, Steps 3, 6, 9, 10, the extension 𝔼, uniqueness not
used); cor:class-two-dust (adapted boundaries, c_B, η, S_in, S_out, its last sentence, its proof for (H1), du(∂_R) and
V + 1 > v_end + η); lem:class-leaf-differences (last statement: leaves are level sets); lem:class-volterra (uniqueness;
the contraction); eq:class-leaf-volterra.

**Other chapters.** 80: thm:two-dusts, def:two-dust-data, prop:two-dust-background (a)–(c), lem:two-dust-domain (a)–(f),
eq:two-dust-omega, sec:two-dust-phases, lem:two-dust-commutator (formula for □_(g0)), lem:two-dust-facts (L6),
lem:two-dust-transport, lem:two-dust-slice. 05: eq:mollifier, lem:mollifier, lem:shift-map (via the width), lem:sobolev,
eq:lambda-one. 09: lem:past-mollifier. 02: eq:omega, lem:domain (f). 07: lem:stage-data, lem:constraints-evolution.
03: lines 360–361 (block 5's old text, present verbatim once).

## Contract results

- Lines: maximum 121 (Python len) in the whole file.
- Wrapped lines: none starts with "+ ", "- ", "* ", "> ", "#", "=" or "|"; the only "- " lines after a non-blank line are
  the list items (iii′), (vi) and (V2′).
- Labels: 13 new labels, all lowercase, none present elsewhere in the chapters; all 69 distinct references resolve.
- Proofs: 7 *Proof.*, 7 ∎, each before the next header.
- Words: no file, program, code or AI words in any block; no process words ("now", "pass" removed); "profile" only in
  its mathematical sense.
- Notation: λ only the wavelength; ϰ and N not used; 𝔪 not used; no clash with n, (v), (H2′), 𝒫, ζ, ι, ε1, ψ, G, S.
- lint.py on the file: only the quoted old marker inside block 2's comment, and single-file "undefined label" hits.

## Private re-derivations (sympy 1.14)

- c1_identities.py: template entries from the definition equal the c_𝔷, s_𝔷 forms; trace 0, norm² 2 symbolically;
  values (−1, 2, −1)/√3 and (−1, −1, 2)/√3 at 𝔷 = ±1; max 𝔢_ϑ = −1/√3; 𝔥(0) = π/3; ℓ̄ := E⁻¹𝔫 − (2E²)⁻¹ℓ null with
  g(ℓ, ℓ̄) = −1 and equal to the old (2E)⁻¹(𝔫 − ν̂); Sherman–Morrison for 𝔊⁻¹ and 𝔊𝔯 = (1 + αγ0^(rr))dr (three random
  exact cases, defect 0); □v = 3ℓ_in(R)/R, □u = 3ℓ_out(R)/R and 2ℓ_𝔨(F_𝔨) + F_𝔨 □ϕ_𝔨 = 0 on a general round double-null
  background; the width slack w + x1 + x2 > 0.
- c2b_kappa.py: the order-one oscillating part of ½𝓛_𝔫 g on TΣ_0, for g = g0 + λW(X, νϕ/λ) with W(g0⁻¹dτ, ·) = 0 on
  {τ = 0}, equals ½ ν dϕ(𝔫0) ∂_θW exactly (2+1 twice and 3+1, general ADM g0, exact rationals, defect 0).
  c2c_control.py: with W not vanishing on g0⁻¹dτ the defect is nonzero (0.455 sin θ − 0.304 cos 2θ, …).
- The commutator identity eq:vlasov-axis-commutator is unchanged except for the form of ℓ̄; its proof was re-checked by
  hand line by line (the review re-derived it at 40 digits).

## For the coordinator

- Block 4b is optional for P-K82 but closes R-P-K82 m6 for the labels (step (4) of thm:vlasov-n-uniform applies
  cor:vlasov-commutator, written for invariant functions, to φ_A); recommended with block 4.
- P-K82 now cites thm:class-stability and def:class-adapted from chapter 82 (R3-82 noted chapter 82 cited neither).
- The label table of chapter 82 needs 13 rows (block 6).
