# Evaluating λ1 and δ: methods, the reduction, and the programme

*Status.* Begun D338 (M, 2026-10-30: "deep research this for possible methods of evaluating/calculating/deriving such
numbers, and then prove them"). Section 2's reduction has been read seven times.

- *Verifier 155 (D338).* Proposition 2.1 correct; Proposition 2.2 incomplete (two major findings, five minor, six
  nits).

- *Verifier 156 (D339).* Every finding of 155 repaired; one major finding (the thresholds Proposition 1.2 imports),
  two minor, four nits.

- *Verifier 157 (D339).* The repairs correct; three more cited thresholds missing from the enumeration.

- *Verifier 158 (D339).* The chain to λ1 and δ correct; the definitions of δ_K and ε_dat by suprema ill-posed (joint
  hypotheses; U-thresholds that depend on the data); three minor, five nits.

- *Verifier 159 (D341).* The pair's definition sound; its existence argued from the wrong lines (one major, one
  minor, five nits).

- *Verifier 160 (D342).* The existence argument nearly valid: δ's uniform lower bound unstated (one major), one
  minor, three nits. Seated.

- *Verifier 161 (D342).* No major finding; one minor clause and two nits, seated (D343).

- *Now (D343).* Proposition 2.2 fixes an admissible pair (ε_dat, δ_K), which III.K's proof shows exists, and keeps the
  enumeration as an inventory not claimed complete. To be read.

Nothing else here is proved. Labels as in the record: computed, deduced, READ.

## 0. Summary

- *What λ1 and δ are.* Theorem 4 (proof5 Part VII Theorem 0.2) holds for λ ≤ λ1 and data within δ. Both are fixed in
  Part VII section 4.

- *What they reduce to.* Section 2 shows (to be read) that they are explicit formulas (minima, ratios, Proposition
  2.1's θ0) in a finite list of named quantities:
  - the tame constants of III.K's map and of its right inverses, and the smoothing constants;
  - the loss d of the right inverses, with k'' and d1 = N + k'';
  - A_2d and the threshold ε_NM^G of Part VII's G-invariant run;
  - an admissible pair (ε_dat, δ_K): a data size and a radius in U at which every other smallness hypothesis of
    III.K holds;
  - the record's threshold λ_1.1 at order J, and the gluing's η_gl and C_R, which depend on the chosen R;
  - the given ε_m and ε_t (through the α of VI.C row w2) and VI.C's threshold ε_K (PART-VII-ASSEMBLY.md:397-401).
  - *What this does not give.* (ε_dat, δ_K) are defined by III.K's own hypotheses, not computed: for them the reduction
    says only that III.K's thresholds exist, and lists the parts found so far (an inventory, not claimed complete).

- *The Nash–Moser step is already effective.* II.G's threshold is an explicit formula in those constants (Proposition
  2.1 below).

- *Where the numbers are lost.* In the linear theory (through the right inverses, through III.J's inverse operators
  inside the map, and through Part IV's exterior and slab solutions), in the gluing, and in the local quasilinear
  theory; the record's threshold at order J is not yet checked. The arguments are of four kinds (section 3), and
  EFFECTIVE-LEDGER.tsv lists the sites.

- *Methods exist for each kind* (section 4, READ). Turning them into numbers is a programme of the size of a second
  write-out of the linear theory, with certified computation at Tangherlini. Section 5 states it.

- *What a number would look like.* Any number it produces will be extremely small, of the order of θ0^−(8d+2) with θ0
  built from products of the linear constants, and d itself a sum of losses not yet added up. It would answer "how
  small is small enough" in the proof's own terms, not physically.

## 1. Methods found (READ)

1. **Verified inverse-operator norms.**
   - *What it replaces.* The step "injective and Fredholm, hence bounded below".
   - *The idea.* Computer-assisted proofs for PDEs bound ‖L⁻¹‖ by splitting off a finite-dimensional part. That part is
     handled by verified linear algebra, and the rest by explicit projection-error constants.
   - *READ.* Sekine, Nakao and Oishi (arXiv:1910.00759v1) write the inverse as an operator matrix through a Schur
     complement S. Their Theorem 2.1 (p. 5) gives L⁻¹ explicitly once T (finite-dimensional) and S are nonsingular, and
     their Lemma 2.2 (p. 6) bounds ‖S⁻¹‖ ≤ 1/(1 − κ) when κ < 1. They state that "the evaluation of ||L⁻¹|| is the
     major task in the verification procedures" (p. 3).
   - *The literature.* It goes back to Plum (1991) and Nakao–Hashimoto–Watanabe (2005), with the monograph of Nakao,
     Plum and Watanabe (2019) (references [7], [12]-[20] there).
2. **Proof mining.**
   - *What it replaces.* Compactness used through convergent subsequences.
   - *The idea.* Replace sequential compactness by Heine–Borel compactness, which yields computable bounds.
   - *READ.* Ferreira, Leuştean and Pinto (arXiv:1810.01508v4, abstract, p. 1): sequential weak compactness arguments
     "can be replaced by Heine/Borel compactness arguments", which "trivializes under the so-called bounded functional
     interpretation", so that "the proof mining program of extracting computational bounds" applies. They also observe
     that Heine–Borel compactness "can be removed from arguments whose conclusion is a quantitative statement. This is
     emphatically not the case with sequential compactness arguments" (p. 2).
   - *What this means here.* An argument "by contradiction with sequences (σ_j, b_j) → (σ_*, b_*)" is to be rewritten
     as a finite cover of the parameter set with explicit radii.
3. **Computer-assisted proofs in general relativity.**
   - *READ.* Goldstein and Jejjala (arXiv:2609.21797v2) prove existence of a non-Schwarzschild black hole in
     Einstein–Weyl gravity. Their tools are a convergent horizon series, a "compact core enclosed by a parameter
     dependent Taylor model with directed rounding", and a tail "treated as a centered stable manifold fixed point
     problem", joined by a Poincaré–Miranda certificate (abstract, p. 1).
   - *Precision.* The core's endpoint derivatives are of order 10¹⁴ and the tail tolerance of order 10⁻³⁰, handled with
     512-bit MPFR intervals (pp. 2, 33).
   - *What this means here.* Separated radial ODEs on a black-hole exterior, with a regular singular horizon and an
     irregular end, are within the reach of validated Taylor models. That is the shape of the Tangherlini mode problems
     here.
4. **Explicit Nash–Moser.**
   - *Here.* The record's II.G proof is explicit: section 2 below extracts the formula.
5. **Large constants are to be expected.**
   - *Where.* When trapping is present, the semiclassical resolvent cut off to a region far from the trapped set can
     still be exponentially large in the inverse semiclassical parameter (Datchev–Jin, "Exponential lower resolvent
     bounds far away from trapped sets", J. Spectral Theory, title and abstract READ through the search index only).
   - *What this means here.* Making the high-energy estimates explicit will not give small constants. That is a
     reason to keep the explicit high-energy work on Tangherlini, where the dynamics are explicit.

## 2. The reduction (Proposition 2.1 confirmed; Proposition 2.2 repaired D342)

**Proposition 2.1 (II.G's threshold, explicitly).**

- *Setting.* In II.G Theorem 2.1 (PART-II-G-NASHMOSER.md), write its support parameter η_G and its radius δ_G (there
  η0 and δ). Put α := 8d+2 and N := 21d+6, and define the K's below.

- *Constants.*
  - K1 := C_d(1+δ_G)
  - K2 := C_{N−2d}(C_{N−d} + 1)
  - K3 := C_{3d,d} K1
  - K4 := 2 C_{N,N−2d} K2
  - K5 := 2 C_{3d,N−2d} K2

- *The parameter.*
  - θ0 := max{ 16, 16 η_G⁻², (4K3/δ_G)^{1/(6d+2)}, 1 + K4, C1 K5 + ½ C2 K3² }.
  - II.G takes η_G ≤ 1, so the entry 16 is implied by the second; III.K takes η_G := 1.

- *Conclusion.* ε_NM := θ0^−α satisfies the conclusion of the theorem: if ‖Φ(0)‖_{2d} < ε_NM, there is u ∈
  B^∞_{η_G/2} with |u|_{3d} < δ_G and Φ(u) = 0.

*Proof.* These are the conditions on θ0 imposed in the theorem's proof (PART-II-G-NASHMOSER.md:101-155), collected.

- (2.6) is used with γ = ½ and γ = 6d+2, which needs θ0^{1/4} ≥ 2, so θ0 ≥ 16. This also gives θ0 ≥ 2, θ_j ≥ 1 (so
  ‖e_j‖_{2d} ≤ 1 and θ_j^β ≥ 1) and θ > 1 for S_θ, which the proof uses without comment.

- *Supports.* These need θ0 ≥ 16 η_G⁻².

- *(a_{j+1}).* This needs 2K3 θ0^{−6d−2} ≤ ½δ_G.

- *(c_{j+1}).* This needs θ0 ≥ 1 + K4.

- *(b_{j+1}).* This needs θ0 ≥ C1 K5 + ½ C2 K3².

- *The K's.* They are the constants of the bounds on v_j and w_j there:
  - |v_j|_d ≤ C_d(1+δ_G)‖e_j‖_{2d};
  - |v_j|_{N−2d} ≤ C_{N−2d}(C_{N−d}(1+|u_j|_N) + |u_j|_N) ≤ K2(1+|u_j|_N);
  - the three smoothing bounds (2.8), with |v_j|_{N−2d} ≤ 2K2 θ_j^β.

- *Nothing else.* The paragraphs on the higher norms and on convergence (PART-II-G-NASHMOSER.md:157-173) put conditions
  on j only. Every condition above is a lower bound on θ0, so the max meets them all.

The proof sets its ε := θ0^−α. Verifier 155 checked the identities (2.5), 5d − N + β = −κα − 1, α − 2d = 6d+2 and
3d ≤ N − 2d for d = 1, ..., 7, and (2.6) at θ0 = 16 (D338). □

**Proposition 2.2 (the chain to λ1 and δ).**

- *δ.* Part VII section 4 puts δ := ε/2, where ε is the data threshold of III.K Theorem 4.3 as run there. It is
  ε = ε(ε_m, ε_t): the constants below are those of the spaces at the α chosen in VI.C row w2
  (PART-VII-ASSEMBLY.md:397-402).

- *ε.* Any ε with
  - ε ≤ min{ 1, ε_NM / A_2d, ε_NM^G / A_2d, ε_dat }
  - is admissible, for any admissible pair (ε_dat, δ_K), with these quantities:
    - *Admissible pairs.* (ε', r) ∈ (0, 1]² is admissible if, for all data with ‖(γ̃, k̃)‖_{H^{d1}} < ε' and all U with
      |U|_{3d} < r, every hypothesis of smallness that III.K sections 1-4 take, directly or through the statements
      they apply, holds, on the data, on U, on |S| (through |S| ≤ |U|_{3d}) or on them jointly. The Nash–Moser
      conditions ε_NM and ε_NM^G are excepted, and treated below.
    - *There is one.* This follows from the quantifiers of III.K's proof. Theorem 3.2 applies II.G on the domain
      {U ∈ B^∞ : |U|_{3d} < δ_G} (III.K:387-388), and II.G uses Lemmas 2.2 and 2.3 at every point of its domain, so
      their thresholds on U exceed δ_G there; that includes III.C Proposition 4.4's threshold, which depends on S
      through g_1 (PART-III-C-EXTERIOR.md:340-341) and enters through III.C Corollary 5.3 (476-487) inside Lemmas 2.2
      and 2.3 (III.K:253, 300). The proof takes ε_NM uniform over the small data (III.K:410-412). The tame constants
      may be taken ≥ 1, since enlarging the constant of an upper bound keeps it, so K3 ≥ 1, and Proposition 2.1's θ0
      contains (4K3/δ_G)^{1/(6d+2)}. A uniform ε_NM = θ0^−α therefore bounds θ0 above and so δ_G below:
      δ_G ≥ 4 ε_NM^{(6d+2)/α} for every datum below some size. One radius then serves them all: a product set. The
      joint conditions of Proposition 4.2 (III.K:457-458) hold after shrinking both entries further. Every data
      hypothesis is on a norm of order at most d1, because Theorems 3.2 and 4.3 are stated and proved for data small
      in H^{d1} (III.K:383, 465-469); a hypothesis above d1 would leave that proof incomplete.
    - *Where U ranges.* Over B^∞ (III.K's class with tails). Lemma 2.3's support clause and II.G (iii) hold at level
      η for U ∈ B^∞_η (III.K:324, 407-408), which is all II.G's proof uses.
    - *Down-closed.* Shrinking either entry keeps a pair admissible, so a pair can be fixed before anything below.
    - *A choice it contains.* Statements of the form "for every k and ε > 0 there are k_1 and ε_1"
      (PART-III-C2-POLYHOM.md:96-98, 143-145; PART-IV3-NM.md:322, 328-329) give a threshold only once their ε is
      fixed. III.K Proposition 1.2 (3) (III.K:131-132) does not fix it. Any fixed choice (for instance 1) is made
      first, and the pair, Proposition 1.2 (3)'s C_k and hence A_2d are relative to it.
    - *Choices that do not enter.* The cut-off's c (III.K:147-148) and the gauge parameters γ and e_Υ (III.K:49-53)
      are fixed before, and bind neither U nor the data.
    - ε_NM: Proposition 2.1's threshold for III.K's spaces, with η_G := 1 and δ_G := min(δ_K, ε_m), and with C_k, C1,
      C2 their bounds over the data ball (III.K:411), so that ε_NM does not depend on the datum it bounds.
    - A_2d: III.K Lemma 2.2 (d)'s constant, ‖P5(Ψ(0))‖_{F^{2d}} ≤ A_2d ‖(γ̃, k̃)‖_{H^{2d+k''}}.
    - ε_NM^G: the threshold of Part VII Proposition 3.2's run of II.G on G-fixed spaces, on ‖P5(Ψ(0))‖ in the G-sup
      norm (PART-VII-ASSEMBLY.md:386). It is Proposition 2.1 with the constants of the G-sup norms, which carry the
      constants of their equivalence with the original norms (369-371), and its radius is min(δ_K, ε_m) in those
      norms. For G-invariant data P5(Ψ(0)) is G-fixed (Part VII Lemma 3.1 at U = 0), so its G-sup norm is its norm,
      and ε_NM^G / A_2d is the data threshold (402-404).
  - III.K Theorem 3.2's smallness paragraph bounds the constants once the data norm is at most 1 (III.K:410-411).
    Lemma 2.3 needs more: the data below its thresholds, which an admissible pair includes. That is a looseness of
    the paragraph's wording, not a gap in the theorem, which asks only for some ε; it is why the "1" alone does not
    suffice.

- *λ1.* The order of choices is k := d1 + 5, then R, then c0 and Ω', then J := k + 5, then λ1
  (PART-VII-ASSEMBLY.md:404-405).
  - Lemma 1.1 at that J gives C_J and a threshold λ_1.1 together (PART-VII-ASSEMBLY.md:106).
  - Corollary 2.3's C_R depends on C_J and R, and is the largest of its three constants (PART-VII-ASSEMBLY.md:258-266).
    λ_1.1 depends on Ω', hence on R (PART-VII-ASSEMBLY.md:151-153).
  - Any λ1 with λ1 ≤ λ_1.1, C_R λ1 ≤ η_gl (the gluing's smallness, Part VII Proposition 2.2) and C_R λ1 < ε/2 is
    admissible; for instance λ1 := min(λ_1.1, η_gl/C_R, ε/(4C_R)). Theorem 0.2 then holds for every 0 < λ ≤ λ1.

*Proof.* This is a reading of Part VII section 4 (PART-VII-ASSEMBLY.md:395-410): "λ1 so small that C_R λ1 < ½ε. Put
δ := ½ε". The thresholds it takes:

- *For ε.* III.K Theorem 4.3's ε as run there. Its smallness conditions are those of an admissible pair, and Theorem
  3.2's: "‖P5(Ψ(0))‖_{F^{2d}_ex} < ε_NM for data small in H^{d1}" through Lemma 2.2 (d) (III.K:410-413). That is
  ‖P5(Ψ(0))‖ ≤ A_2d ‖data‖_{H^{2d+k''}} ≤ A_2d ‖data‖_{H^{d1}} < A_2d ε ≤ ε_NM, as 2d + k'' ≤ d1. The G-run goes the
  same way.

- *Part VII section 4's own conditions* (PART-VII-ASSEMBLY.md:397-406). Given ε_m, VI.C runs through ε_K; ε_t < ε_K
  and α > 4 + ε_t in row w2; II.G's radius becomes min(δ_K, ε_m); the data are below ε(ε_m, ε_t); in (i), below the
  threshold of Proposition 3.2's run; k := d1 + 5; R ≥ max(R_gl, R_3); c0 and Ω' by Lemma 1.2; J := k + 5; C_R λ1 < ½ε;
  δ := ½ε. Of these only the data bounds, the radius and the condition on λ1 are smallness conditions, and all three
  are in the statement.

- *For λ1.* Corollary 2.3's "for λ small" is η ≤ η_gl against Proposition 2.2 (PART-VII-ASSEMBLY.md:193-197, 258), and
  Lemma 1.1 has its own threshold. The other conditions in Part VII section 2 are on R and η_gl, not on λ.

Each condition is an upper bound on the data norm, on U or on λ. The Nash–Moser conditions are ε_NM and ε_NM^G, read
through A_2d; Part VII section 4's own conditions are those just listed; every other condition III.K takes holds on an
admissible pair by its definition, joint ones included. So the minima meet them all. □

**The inventory of an admissible pair (found by three reads, D338-D339; not claimed complete).** The definitions above do
not depend on this list. It records the parts found, so that E1'' can make each explicit. Each read found more: the
first draft's keyword reading missed hits of its own keywords (verifier 155), five hypotheses that no keyword marks
(verifier 156), and three more in statements III.K applies (verifier 157). E1'' is to finish it statement by
statement.

- *On U.* The definition of Ψ and Lemma 2.2 (PART-III-K-NONLINEAR.md:214, 219); Lemma 2.3's ε_0 (273) and its base
  point (281); Proposition 4.2 (457-458); Part VII Lemma 3.1's equivariance (PART-VII-ASSEMBLY.md:317), inside Ψ's
  domain.

- *On |S|.* III.K Lemma 1.1 (d) (77, 90); III.B Lemma 5.2's own threshold w_0, under which its constant C holds
  (PART-III-B-FAMILY.md:379, 385), applied at 113 and 322; Proposition 1.2's C|S| ≤ ½c_ν (114) and its use of II.C
  Lemma 3.2 (2) (158); Lemma 2.3's supports paragraph (320); the exterior's ε_2 and C|S| < 1/24
  (PART-III-C3-BOOSTDATA.md:84-88) and "S small, depending only on b_0, ℓ♭_0 and ℓ♭_I" (95-96); the slab's
  (PART-IV4-SLAB.md:86).

- *On the data, through Proposition 1.2.*
  - The data map, III.C'' Proposition 4.1: γ̃ small in H³_b, (h_0, h_1) "depending continuously" on the data
    (PART-III-C3-BOOSTDATA.md:166-168), in a topology the statement does not name; E1'' is to fix it.
  - The exterior, III.C'' Theorem 3.1 (PART-III-C3-BOOSTDATA.md:91), through III.C' Theorem 2.1's ε_0 at
    H^{k_0, ℓ♭_0}_b (PART-III-C2-POLYHOM.md:89-92), which is Part IV'' Theorem 3.1's ε_0 at H^{14, ℓ♭_0}_b
    (PART-IV3-NM.md:321-324, its own d := 7): a Nash–Moser threshold, ε_ext.
  - The exterior's higher-order bounds, one threshold per order: III.C' (3.2) (PART-III-C2-POLYHOM.md:143-148), III.C'
    Theorem 2.1's ε_1(k, ε) (96-98) and Part IV'' Theorem 3.1's ε_1 (PART-IV3-NM.md:322, 328-329), at the orders
    III.K uses (Proposition 1.2 (3) through III.K:205).
  - The slab, Part IV''' Theorem 2.2: ‖h_j‖_{H^{2d, ℓ♭_0}_b} + ‖k_j‖_{H^{2d}(Σ_c)} < ε_0 (PART-IV4-SLAB.md:128-132),
    a second Nash–Moser threshold, ε_slab, with (k_0, k_1) from the compact part through its Cauchy stability; and
    its higher-order bounds (134-135, 148-150). Its proof is Part IV'' Theorem 3.1's (PART-IV4-SLAB.md:137), so
    d := 7 and 2d = 14 (PART-IV3-NM.md:321), not Theorem 2.1's d = 4 (PART-IV4-SLAB.md:89).
  - The compact part's local quasilinear theory (III.K:158, 184-186).

- *On the data, elsewhere in III.K.* III.C Corollary 5.3's smallness "as in Proposition 4.4", with its own ε_0
  depending on k, a_0, a_I and g_1 (PART-III-C-EXTERIOR.md:340-341, 476-477), applied with g_1 = φ_{−S}^* g_b0 to
  χ_−h_{−S} + h̃ at III.K:253 and for e_S at 300; Lemma 2.3's base point in III.I's class (281), its boost defect e_S
  (305-309) and G_S − g_b0 (320); Proposition 4.2's h_{−S} (457-458).

**What is not explicit.** In Propositions 2.1-2.2, every quantity is a formula except:

- the loss d, with k'' and d1 = N + k''. III.J''' gives d only as the sum of the losses of the parts it composes
  (PART-III-J3-TAME.md:288-292), and the sum has not been added up; so α = 8d+2 and N = 21d+6 are not yet numbers;

- the tame constants C_k (k ≤ N), C1 and C2 of III.K's map and right inverses, and the smoothing constants C_{s,t};

- the admissible pair (ε_dat, δ_K), among whose parts are the two Nash–Moser thresholds ε_ext and ε_slab with their
  higher-order thresholds and the data map's modulus of continuity; and A_2d;

- the constants of the equivalence of the G-sup norms in ε_NM^G;

- ε_m and ε_t, which are given, and VI.C's ε_K;

- the record's C_J and λ_1.1 at order J;

- the gluing's η_gl and C_R.

Of these, the smoothing constants, the Moser parts of the map's estimates, c_ν (III.K:114), the comparisons of norms
and the compact part's local theory (energy estimates and Cauchy stability on a compact domain) are explicit in
principle. None of the others is yet shown explicit. Section 3's arguments enter:

- the map's constants and A_2d, through III.J's inverse operators N_ι+(z)⁻¹ and S_λ0 (PART-III-J-PARAM.md:95,
  225-232), and through h_{−S}, whose bounds come from the compact part's local theory and from the exterior and slab
  solutions (III.K:184-186, 205-206);

- the right inverses' constants, δ_K and Lemma 2.3's and Proposition 4.2's parts of ε_dat, through the linear theory;

- ε_ext and ε_slab, through the linear theory of Parts IV-IV''' (the ledger finds no N-site there; its one N-site in
  Part IV, PART-IV7-TFACE.md:383, is in Part IV''''''s constraint damping, which enters III.K through III.E's
  parameters, III.K:49);

- the data map's modulus of continuity: not yet examined (E1'');

- η_gl and C_R, through [CD03]'s implicit function theorem (E5).

C_J and λ_1.1 are not yet checked (E5), and ε_NM^G's equivalence constants are explicit once the action's derivatives
are bounded.

## 3. Where the numbers are lost: four kinds of argument

A text count over proof5's 75 PART files (D338, case-insensitive) finds contradiction 19 times, compactness 44,
Rellich 5, compact inclusion or embedding 5, Fredholm 74 and subsequence 28, in 35 files. (D337's count of 51 and 36 was
not reproducible.) Read in context, the arguments that produce a constant without a number are of four kinds.

- **N1: a compact error removed by injectivity.**
  - *The pattern.* ‖u‖ ≤ C(‖Pu‖ + ‖u‖_weak) with a compact inclusion, and a trivial kernel, gives ‖u‖ ≤ C′‖Pu‖ by
    contradiction.
  - *Examples.* PART-I-C-LOWENERGY.md:494-498 (zero energy), the same in I.A and II.F.
  - *What it hides.* C′ hides a lower bound for P on the complement of a finite-dimensional space.

- **N2: uniformity in parameters by sequences.**
  - *The pattern.* An estimate at each point of a compact parameter set, made uniform by contradiction with
    (σ_j, b_j) → (σ_*, b_*).
  - *Examples.* PART-III-H3-UNIFORM.md:189 (I.A Lemma 3.1 for c/2 ≤ |σ| ≤ C0), PART-I-C-LOWENERGY.md:686 and 1421
    (local constancy of the index; Corollary 5.2 (b)), PART-II-F-IOTA.md:1063 and 1329.
  - *What it hides.* The modulus of continuity in the parameters, and a finite cover.

- **N3: semiclassical absorption at trapping.**
  - *The pattern.* The high-energy estimates near the trapped set close by contradiction against the dynamics.
  - *Examples.* PART-I-B-HIGHENERGY.md:2047-2052 (Propositions 6.4 and 6.7 (a)), made uniform in b by the same device.
  - *What it hides.* The constant of the trapping estimate.

- **N4: finite covers of compact parameter sets.**
  - *The pattern.* "By compactness of 𝓑, finitely many suffice" (PART-I-B-HIGHENERGY.md:2047).
  - *Why it is minor.* It is effective once each local neighbourhood has an explicit radius.

Geometric compactness used only to show that a set is closed or a curve extends (for instance PART-II-F-IOTA.md:259)
produces no constant and needs nothing.

**The ledger (E1, D338).** EFFECTIVE-LEDGER.tsv reads each occurrence in context and classes the site. Its columns are
file, line, class, the statement it serves, the constant it hides, and an excerpt (an ASCII rendering of the LaTeX).

| class | meaning | rows |
|---|---|---|
| N1 | compact error removed by injectivity | 6 |
| N2 | uniformity in parameters by sequences | 15 |
| N3 | semiclassical absorption at trapping | 1 |
| N4 | finite cover of a compact parameter set | 13 |
| F | the Fredholm property used qualitatively (index, meromorphy), no constant | 41 |
| G | geometric or weak compactness, no constant | 37 |
| X | a mention, heading, citation or continuation of a row above | 52 |

- *The 35 N-rows.* They lie mostly in the linear theory's foundations: I.B 7, I.C 5, I.A 5, II.F 3, III.H''' 2, and
  one or two in each of nine other parts.

- *How it was built, and what is checked.* A reading pass by an extraction agent (D338) built it. A script then checked
  that each of the 165 rows names an existing file and has one of the words above within two lines of the cited line;
  all do. The classes are a reading, not checked row by row, and the ledger is not claimed complete.

## 4. The effective replacements

| kind | replacement | where the number comes from | READ |
|---|---|---|---|
| N1 | verified inverse norm: finite-dimensional part by interval linear algebra, remainder by explicit projection errors and a Neumann series | at Tangherlini the operators separate over the harmonics of S³: low harmonics by validated ODE integration (Taylor models), high harmonics by explicit coercivity | Sekine–Nakao–Oishi Thm 2.1, Lemma 2.2; Goldstein–Jejjala |
| N2 | Neumann series about certified base points on an explicit finite grid, with Lipschitz bounds of the operators in (σ, b) | the base bounds of N1 at the grid points, and explicit derivatives of the explicit Myers–Perry metrics | Ferreira–Leuştean–Pinto (Heine–Borel in place of sequences) |
| N3 | an explicit trapping estimate at Tangherlini by physical-space multipliers (separable dynamics, explicit photon sphere), carried to nearby b by N2 | explicit multiplier positivity, of the kind the record already computes in five dimensions (rungs5.py's Sturm count) | Datchev–Jin (expect large constants) |
| N4 | explicit radii from N2 | as N2 | as N2 |

## 5. The programme, and its size

- **E1. The ledger (done, D338).** Every site of N1-N4 in proof5, with the constant it hides (EFFECTIVE-LEDGER.tsv,
  section 3).

- **E1'. The loss d.** Add up III.J''''s losses part by part, with k'' and d1, so that α and N become numbers. Done as
  far as the record allows (LOSS-D.md, D347): d is a finite sum whose step losses are explicit in the chosen weights
  except five, so E1' is not bookkeeping but three tasks: E1'a (numbers for the weights from the index sets at n = 4),
  E1'b (the five losses), E1'c (the level and round counts). k'' is now defined (LOSS-D.md LD1). At the record's
  parameter point two counts are already known to be large (LD3, D348): the d this proof produces exceeds 1.3 × 10⁶
  from one chain of decay levels alone, and a loop nested inside it runs about 5 × 10¹⁰ rounds. No admissible choice
  of the damping parameters helps by more than a factor of about ten (LD5, D353).

- **E1''. The inventory.** Finish section 2's inventory of δ_K and ε_dat statement by statement, and unfold each
  part (ε_ext, ε_slab and their higher orders, the data map, III.C's and III.B's thresholds) into its own proof's
  constants, as section 2 does for III.K.

- **E2. Tangherlini, mode by mode.**
  - *The problem.* The operators of III.D, III.F and IV at b0, separated over the harmonics of S³, give radial ODE
    families with a regular singular point at the horizon and an irregular one at infinity, as in Goldstein–Jejjala.
  - *What is needed.* Certified lower bounds at each harmonic up to an explicit cut-off, and explicit coercivity
    beyond it.
  - *What it replaces.* The N1 constants at b0.

- **E3. Near b0.**
  - *What is needed.* Explicit Lipschitz bounds of the Myers–Perry operators in b, and the Neumann series.
  - *What it replaces.* The N2 and N4 constants.

- **E4. High energy.** An explicit trapping estimate at Tangherlini (N3).

- **E5. The data side.**
  - *The record's threshold λ_1.1 and C_J at order J.* Its proof is energy estimates on a compact domain; whether it
    contains arguments of kinds N1-N4 is still to be checked (E1 covered proof5 only).
  - *The gluing's η_gl and C_R.* These come through [CD03]'s implicit function theorem, whose linearised operator's
    invertibility is an N1 step.
  - *ε_dat.* The compact part's local quasilinear theory (energy estimates and Cauchy stability) is explicit in
    principle. The exterior and slab thresholds are Nash–Moser runs over Part IV's linear theory (E2-E4 apply there
    too), and Lemma 2.3's and Proposition 4.2's parts go through III.I's class and the right inverses.
  - *ε_NM^G.* The norm-equivalence constants of a compact group acting smoothly: explicit once the action's
    derivatives are bounded.

- **E6. Assemble.** Feed the numbers through section 2's formulas.

*Size.* E2-E4 rewrite, with numbers, the parts of the linear theory that the right inverses and III.J's inverse
operators rest on (Parts I, II.F, III.D-III.H'', III.J, IV). That is comparable to the original write-out of those parts,
plus certified computation. It is not one session's work. E1 is done; E1' is reduced to E1'a-E1'c (LOSS-D.md); E2
at one operator is the first real test.

## 6. Sources

- READ:
  - Sekine, Nakao, Oishi, arXiv:1910.00759v1 (abstract; pp. 3, 5-6);
  - Ferreira, Leuştean, Pinto, arXiv:1810.01508v4 (abstract; pp. 1-2);
  - Goldstein, Jejjala, arXiv:2609.21797v2 (abstract; pp. 2, 9-15, 33).

- Through the search index only: Datchev–Jin (title, abstract).

- The proof: PART-II-G-NASHMOSER.md:101-173; PART-III-K-NONLINEAR.md sections 1-4; PART-III-J3-TAME.md:288-292;
  PART-III-J-PARAM.md:95, 225-232; PART-VII-ASSEMBLY.md:104-108, 256-266, 317, 366-371, 386 and 395-410; for the
  inventory, PART-III-C3-BOOSTDATA.md, PART-III-C2-POLYHOM.md, PART-IV3-NM.md, PART-IV4-SLAB.md, PART-III-C-EXTERIOR.md,
  PART-III-B-FAMILY.md and PART-IV7-TFACE.md at the lines cited; the sites of section 3 and EFFECTIVE-LEDGER.tsv.

- Verifier 155 (D338), read of section 2: Proposition 2.1 confirmed; M1 (three smallness thresholds missing), M2 (the
  loss d, ε_G's constants, the map's inverse operators), m1-m5 and n1-n6, all seated (D338).

- Verifier 156 (D339): MAJ-1 (the exterior, slab and data-map thresholds Proposition 1.2 imports), MIN-1 (ε_G is a
  threshold on ‖P5(Ψ(0))‖, now ε_NM^G / A_2d), MIN-2 (the "rest" made exhaustive), NIT-1 to NIT-4, all seated (D339).

- Verifier 157 (D339): the D339 repairs correct, ε_NM^G / A_2d correct; MAJ-1 (three more cited thresholds: the
  higher-order exterior and slab bounds, III.C Corollary 5.3's, III.B Lemma 5.2's w_0), MIN-1 (the Part IV N-site's
  role), NIT-1 to NIT-5. Seated by defining δ_K and ε_dat instead of enumerating them, and keeping the enumeration
  as an inventory not claimed complete.

- Verifier 158 (D340): MAJ-1 (the suprema ill-posed), MIN-1 (section 0 overstated), MIN-2 (orders; the ε-choice in
  Proposition 1.2 (3)), MIN-3 (g_1), NIT-1 to NIT-5; seated by admissible pairs (D340).

- Verifier 159 (D341): MAJ-1 (existence argued from K:410-411's wording rather than the proof's quantifiers), MIN-1
  (ε_m, ε_t, ε_K omitted from the lists), NIT-1 to NIT-5; seated (D341).

- Verifier 161 (D342): no major; MIN-1 (the tame constants taken ≥ 1, so the lower bound on δ_G is uniform),
  NIT-1 (III.C Corollary 5.3 named), NIT-2 (δ_G); seated (D343).

- Verifier 160 (D342): MAJ-1 (δ's uniform lower bound, from the uniform ε_NM through θ0), MIN-1 (III.C 4.4's
  threshold is inside Lemmas 2.2-2.3, not a shrink), NIT-a to NIT-c; seated (D342).
