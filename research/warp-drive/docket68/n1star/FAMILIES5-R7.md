# FAMILIES5-R7 -- round 7: the round-6 verifier seated; Theorem Q at the axes; E defined; two margins certified

Status (2026-11-06, workstream C, round 7). The independent verifier of round 6 found no major gap: all six theorems
of FAMILIES5-R6.md hold, some with corrections, and all nine programs reproduce byte for byte. This note seats its 9
minor findings and 13 nits, each re-derived first (R7.0). It certifies by interval arithmetic the two margins round 6
had only sampled (R7.3). It gives a new section 9 block (R7.6), which supersedes R6 section 8's. Earlier notes keep
their text; bracketed [R7 …] notes mark each affected line in FAMILIES5-R6.md and FAMILIES5-VLASOV.md. Nothing in
the paper or in N1STAR-PROOF.md is edited.

**Verdict.**

1. **Theorem Q holds for seeds that reach the axes** (R7.1). A smooth seed has ψ = sin²θ cos²θ F(R, cos 2θ) and s1
   smooth in cos 2θ. For this class the θ boundary terms vanish, because ψ = O(sc²). The identity is computed over the
   whole of [0, π/2] (qsign5 Q7). Its control, ψ = O(sc), fails as it must.
2. **The charge and E are defined once** (R7.2). With the record's pairing, Q(δ) = 2∫G^(2)[δ](ξ, n) dvol =: −E(δ).
   That E is the Hollands–Wald canonical energy is standard; it is not READ here and nothing uses it. M_b is stated
   for this E.
3. **Two margins are certified**, for the computed background in a stated interpolant (intcert5). C1 certifies Γ > 0
   on the whole of region III, R ∈ [0.70, 1.861] (least lower bound of Γ/E² is 0.4475). C2 certifies κ′K′^l_l < 0 on
   the whole bent slice Σ′, between its samples (upper bound −3.03 × 10⁻⁴ at n = 160). Each has controls that fail,
   among them the verifier's two mutations. The discretisation error of the background is converged, not certified.
4. **Lemma O is restated with its topology** (R7.4, Lemma O′). It gives openness for perturbations whose supports stay
   in a fixed compact neighbourhood; this is the case Proposition NE uses.
5. **The other minors (m4-m9) and all nits are repaired** (R7.0, R7.5). The new paper block (R7.6) carries the
   perturbative qualifier and separates deduced openness from the computed test family. It says "minus the canonical
   energy (the identification not proved here)", states the radial dusts' adapted boundaries, and labels "no foliation"
   as deduced.

Labels as in the record: **computed** (a program `checks/<name>5.py` with a `.out` and a control it must reject),
**deduced** (argued here), **certified** (interval arithmetic over a stated interpolant of the computed background,
with a control that fails), **READ** (verbatim at source). New program, with its `.out`, PASS: `checks/intcert5.py`
(C1-C2). Changed and rerun in full, `.out` regenerated, all PASS:
- `checks/qsign5.py`: Q7 new; Q3 on [0.70, 1.861]; Q5 (c′) for any ψ_P; Q5's point count.
- `checks/nfamily5.py`: N4's second control and its print; N5's interior statement made exact.
- `checks/racslice5.py`: docstring only.
- `checks/racglobal5.py`: R2's labels.
- `checks/katonl5.py`, `checks/twobg5.py`, `checks/vlasovhf5.py`: labels and a docstring.

The verifier's three mutants, rerun from its scratch copies, fail as they must: `racslice5_mA` (S2 FAIL), `qsign5_mGam`
(Q1-Q4 FAIL) and `nfamily5_mV2`'s N4 (False). The same mutations now sit inside intcert5 (C1's flipped sign, C2's A =
0.001) and nfamily5 N4 as permanent controls.

---

## R7.0 The round-6 verifier: findings and dispositions

- **m1 (Theorem Q on the axes).** *Re-derived* (R7.1); a band U may contain axis points. *Accepted:* the smooth class
  is stated; "every pair" means pairs of that class; the boundary terms vanish; the axis case is computed (qsign5 Q7,
  re-implemented independently of the verifier's scripts).
- **m2 (Q = −E: sign, factor, support).** *Re-derived:* with N_sH + 2Y_s^R M_R = 2G(ξ, n) (Q5 (b)), the ε² term of
  ½⟨(N_s, 2Y_s), Φ(bg + εδ)⟩ is 2∫G^(2)[δ](ξ, n); R6's parenthetical read literally gave Q = +2∫G^(2). *Accepted:*
  R7.2 is the definition, and the identification is labelled.
- **m3 (Lemma O's topology).** *Re-derived:* a C¹-small bump of q placed elsewhere can meet a caustic or an axis, so
  (V1), (V2) and (V2′) are not open in C² × C¹ when the supports are free. *Accepted:* Lemma O′ (R7.4).
- **m4 (Lemma 2.4_N).** *Re-derived:* N5's interval [−1, (r² − μ)/(r² + μ)] is Kerr–Schild Tangherlini's. For general
  g the outer flux coefficient is b′ − dr(ℓ)/dτ(ℓ) on {v + τ = const} (b′ = −2), negative because d(v + τ)(ℓ) =
  ℓ(τ)(2 + dr/dτ) > 0 by (Ω). The inner coefficient is dr(ℓ)/dτ(ℓ) < 0 because r decreases along future causal curves
  at r = a. *Accepted:* R6 §4.1 (v) now cites (Ω); N5 is the instance for g0.
- **m5, m6 (VLASOV markers).** *Accepted:* "[R6: withdrawn inside the horizon; Theorem Q′ …]" at VLASOV section 4's
  dust sentence. VLASOV section 3 gets pointers to Theorem L″ (Proposition L superseded) and to Theorem K′ (the
  Cauchy stability).
- **m7 (the new block's four overclaims).** *Accepted:* all four repaired in R7.6.
  - (a) "near Part I's data, …, for small amplitude".
  - (b) openness deduced; the test family computed.
  - (c) "minus the canonical energy (the identification not proved here)".
  - (d) "the radial dusts having adapted lateral boundaries at the axes".
- **m8.** *Accepted:* "no foliation of that slice is hyperbolic (deduced from Rácz's characteristic equation)"; the rest
  is computed or certified.
- **m9 (Q′'s T(ξ, n)).** *Re-derived:* with E = e^(ψ_P), ξ = e^(−ψ_P)∂_v̂, ℓ_out = ∂_v̂ + (Ef/2)∂_R and n_a = −(1, −1)
  /√(2/E − f), one gets g(ℓ_out, ξ) = −Ef/2 and ℓ_out·n = −(2 − Ef)/(2√(2/E − f)). So T(ξ, n)/q = E f (2 − E f)/(4√(2/E
  − f)), whose sign is f's. *Accepted:* computed exactly as qsign5 Q5 (c′); at E = 1 it is R6's f√(2 − f)/4.
- **Certification request.** *Done* (R7.3): intcert5 C1-C2, with controls.
- **Nits.**
  - n1: "a convex bend, V″ > 0"; the bend has φ ≤ 0, so Σ′ lies to the past (R6 §2, racslice5 docstring).
  - n2: racslice5's docstring band is now [4.29, 4.53].
  - n3: L″'s margin reads "sampled at the grid crossings, converged; certified between them (C2)".
  - n4: racglobal5 R2 is relabelled "exact identities; signs over the tilts deduced, illustrated on 400 draws". N5's
    interior statement is now exact (the null condition's two roots are monotone in √(1 − w²(1 + f)) ∈ [0, 1]); the
    15 samples are an illustration.
  - n5: qsign5 prints "three points".
  - n6: "certified" for twobg5 G3 is replaced by "independently checked (DOP853, floating point)".
  - n7: Γ is sampled and certified on [0.70, 1.861]; the ratio range is now [0.715, 2.12].
  - n8: "(M1)" in R6 §4.1 is FULL's mollifier bound.
  - n9: the `docket68/n1star/` prefixes are restored in R7.6.
  - n10: katonl5 prints "violates (K1) and (K2)".
  - n11: N4 prints each comparison's truth value.
  - n12: vlasovhf5 notes that H4_NOHIER is caught by the resonant configuration only; the random trials are not resonant.
  - n13: nfamily5.out was completed after R6 was written; round 7 reran it with N4-N5 changed.
- **Confirmed by the verifier and unchanged:** the Theorem Q identity (its Euler operator vanishes identically for
  generic G, κ0, Y0, ν), Γ = 4μ/R where ψ_P = 0, Theorem Q′'s construction, D₂_N, (V2′), Theorem K′ line by line, the
  M_b dichotomy, and the [HL25] and [Rac16] readings.

## R7.1 Theorem Q at the axes (deduced; computed qsign5 Q7)

**The smooth class.** In the T² × Z2 × Z2 class a smooth invariant function on S³ is a smooth function of (R, cos 2θ):
cos 2θ = (ρ2² − ρ1²)/R², and an O(2)-invariant smooth function of a plane is a smooth function of the squared radius
(Whitney's even-function theorem; standard, not READ). A smooth invariant one-form's θ-component vanishes like
sin 2θ at the axes, since d(cos 2θ) = −2 sin 2θ dθ. So for a smooth momentum seed:
- Kt and s1 are smooth in cos 2θ;
- p̂ = sc · (smooth in cos 2θ);
- the stream function, with compact support in R, is ψ = ∫ ψ_R dR = (R-integral of sc² × smooth), that is
  **ψ = sin²θ cos²θ F(R, cos 2θ)** with F smooth and compactly supported in R. Then Kt = E(2 cos 2θ F − 4 sc² ∂F/∂c),
  c := cos 2θ, which is smooth and in general nonzero on the axes.

"Every pair is one" (R6 §1.1) is to be read for pairs (ψ, s1) of this class. Each such pair solves the linearised
constraints with finite Q. Whether its s2 meets the axis compatibility of a smooth tensor is not needed: Theorem Q is
a statement about smooth seeds, which are of this class.

**The boundary terms.** The integrations by parts in θ of R6 §1.2 produce, at θ = 0 and θ = π/2, the three terms
2νE·βE ψψ_θ/sc ((i)), 2νE ψ s1 ((ii)) and νE²(cos 2θ/sc²)ψ² ((iii)). For ψ = sc²F each is O(sc²) and vanishes. The
remaining integrands are bounded: Z − Eψ/(2sc²), s1 − 2EX/(3sc), and Γψ²/sin 2θ = O(sc³). So **Theorem Q holds for
every smooth momentum seed supported in U, whether or not U meets an axis.**

*Computed (Q7).* On Tangherlini's slice in Part I's chart (ψ_P = 0, μ = 0.82), six seeds of the class were used:
random F and s1 polynomial in cos 2θ, two bands of which one is inside the horizon, and Kt/E ≥ 2.464 on the axis.
Q equals the decomposition integrated over the whole of [0, π/2], to 2.2 × 10⁻¹⁶ of Q and 5.1 × 10⁻¹² of its Γ
term (60-point Gauss–Legendre in each variable, closed forms). Q < 0 and Q ≤ −∫∫Γψ²/sin 2θ. Controls:
- Γ → ¾Γ misses Q by 0.2500 of the Γ term.
- Seeds with ψ = O(sin θ cos θ), which are not axis-regular, miss it by at least 0.13 of the Γ term (the axis boundary
  terms do not vanish).

## R7.2 The charge and E, defined once

Let Φ = (H, M) be the record's constraint map (bandconst5: H = R + (tr K)² − |K|², M_i = D_jK^j_i − D_i tr K). Let
(N_s, 2Y_s) be the static KID (qsign5 Q5 (a)). On the data of any metric, N_s H + 2Y_s^R M_R = 2G(ξ, n), ξ = e^(−ψ_P)
∂_v̂ (Q5 (b) checks it on Vaidya, where G = T). For a compactly supported seed δ supported in U:

    Q(δ) := ½ d²/dε²|₀ ∫_U (N_s H + 2Y_s^R M_R)(bg + εδ) dvol = 2 ∫_U G^(2)[δ](ξ, n) dvol =: −E(δ),

where G^(2)[δ] is the ε² coefficient of G on the data bg + εδ. At δγ = 0 this is R6's Q = ∫N_s((tr δK)² − |δK|²) dvol.
Exact data with matter stress T in U need ε²Q/2 + O(ε³) = ∫_U T(ξ, n) dvol, as in R6 §1.4.

That E is, for compactly supported perturbations, the canonical energy of Hollands and Wald relative to ξ is standard;
it is not READ here, and nothing here uses it. **M_b** (R6 §1.5) is the statement "E(δ) > 0 for every non-gauge,
compactly supported, invariant linearised vacuum solution δ supported in U", with E as defined here. The parallel
attempt on M_b (FAMILIES5-MB.md) is to use this definition.

## R7.3 Two margins certified (checks/intcert5.py)

Both margins are properties of the record's computed background (twobg5). What is certified is the statement about
that background in a stated interpolant. Its discretisation error is converged between n = 80 and 160 (qsign5 Q3,
racslice5 S2), not certified.

- **C1: Γ > 0 on the whole seed region, R ∈ [0.70, 1.861] (region III on Σ_τ0).**
  - Method: Γ = E²·(Γ/E²) with E² > 0, and Γ/E² is qsign5's closed form in (R, μ0, ψ_P, ψ_P′, ψ_P″). ψ_P is the
    spline ψ_III(τ0 + R) in its piecewise-polynomial form. The interval is cut at the knots and into 600 cells. On each
    cell the polynomial and its first two derivatives are enclosed by interval evaluation, and the closed form is then
    enclosed by interval evaluation (mpmath, 80 bits).
  - Result: certified at n = 80 and n = 160. The least lower bound of Γ/E² is 0.4475, on R ∈ [0.700, 0.702]; the
    sampled minimum is 0.6247 there.
  - Controls: Γ with its sign flipped (the verifier's mutation) and Γ without its 4νE² term both fail on every cell.
- **C2: κ′K′^l_l < 0 on the whole of Σ′ (racslice5, A = 0.01), not only at its 434 (n = 80) and 867 (n = 160) grid
  crossings.**
  - Method: between consecutive crossings the background inputs (E, f, ψ_R, ψ_v̂, f_R, f_v̂) are the linear
    interpolant of their crossing values, so on each sub-cell they lie in the hull of their end values. V″ = φ″ is
    enclosed from its closed form (the C^∞ bumps in interval arithmetic). V′ is enclosed as 1 + φ′(R_a) + [0, R − R_a]
    φ″ (with ±10⁻⁶ for the quadrature of φ′). Each interval is cut into four sub-cells, bisected further if needed.
  - Result: on every sub-cell κ′ > 0 and K′^l_l < 0 are certified, at n = 80 and n = 160. The largest upper bound of
    κ′K′^l_l is −2.99 × 10⁻⁴ (n = 80) and −3.03 × 10⁻⁴ (n = 160); the sampled maximum is −3.08 × 10⁻⁴.
  - Controls: A = 0.001 (the verifier's mutation; 221 sub-cells fail, largest upper bound +4.9 × 10⁻⁵) and A = 0
    (Σ_τ0 itself; 314 fail) are not certified.

So Theorem L″'s hyperbolicity of Σ′ and Corollary Q's Γ > 0 on the seed region are certified for the computed
background in the stated interpolant. Every other number in them is computed or deduced as before.

## R7.4 Lemma O′: the hypotheses are open in the right topology (deduced)

**Lemma O′.** Fix a compact S ⊂ (Σ_τ0 ∩ Ω) × S¹ such that supp q lies in its interior, and suppose (V1), (V2) and
(V2′) hold, with margins J0, 2δ and η, for the tubes of **all** points of S (not only of supp q). Then there is a
neighbourhood of (g, u|Σ, ∂u|Σ) in C² × C¹ such that every (g′, q′, u′) with g′, u′ in it and supp q′ ⊂ S satisfies
(V1), (V2) and (V2′) with margins J0/2, δ and η/2. (Ω) and (V3) are open in C² × C¹ as before. Equivalently,
openness holds for supports that vary, in the Hausdorff metric, inside such an S.

*Proof.* Lemma O's argument, applied to the tubes of S. These are fixed by S and g′ and depend continuously on g′ in C²
(continuous dependence of rays and Jacobi fields), uniformly on the compact S̄ × [τ0, τ_end]. ∎

Proposition NE satisfies this. Its data have a fixed initial support, the ball × the label intervals, at amplitude ε.
S is the ball enlarged by 20 % × the intervals, and vlasovex5 X2 checked the conditions on the tubes of all of S. The
coupled solutions' fields keep that initial support for every ε. Their tubes are those of S for the metric g_ε, which
is C²-close to g0.

## R7.5 The remaining corrections (applied as [R7] notes)

- R6 §1.3: Γ is sampled on [0.70, 1.861], ratio range [0.715, 2.12], and certified there (C1).
- R6 §1.4: T(ξ, n) holds for any ψ_P (m9).
- R6 §1.5: E is defined as in R7.2 (m2).
- R6 §2:
  - "convex bend" (n1);
  - the margin is sampled, converged and certified (n3, C2).
- R6 §3: Lemma O′ (m3).
- R6 §4.1:
  - "(M1)" is FULL's (n8);
  - Lemma 2.4_N's signs come from (Ω) (m4).
- R6 §8: superseded by R7.6.
- VLASOV §§3-4: the markers (m5, m6).

## R7.6 Proposed replacement for the paper's section 9 bullet "More families"

The old text is the paper's current bullet. It occurs exactly once in `paper/RESPONSE-HL-5D.md` (section 9, "What is
not proved"). This block supersedes R6 section 8's new text and every earlier proposal.

Old:

```
- **More families.** Angular separation and the passage to Vlasov matter are not attempted. Two crossing null dusts are
  scoped and taken through the leading orders (supplement `docket68/n1star/FAMILIES5.md`): the cross coupling of the two
  families is a gauge artefact at leading order (deduced; stage 0 computed, `docket68/n1star/checks/stage0two5.py`), and
  with two families the core estimate of section 5, its approximant to every order and its lemma on the domain are
  deduced (the lemma's form for the two-dust background computed, `docket68/n1star/checks/twodomain5.py`), the last given
  the two-dust background on the whole domain. That background's existence is deduced with one step sketched, given its
  characteristic data (the outgoing family's are open; the dusts' stress in the characteristic constraints computed,
  `checks/chardust5.py`), and computed on a region that does not reach the initial slice (`checks/twodust5.py` B5,
  floating point). With the outgoing family's characteristic data moved to an earlier cone (a choice, those data being
  open), it is computed on a rectangle reaching Σ_−1.5, every outgoing ray from the inner boundary leaving it at τ ≤
  −1.78, the constraint residuals converging at second order away from the steep inner boundary and the inner boundary
  trapped (computed, floating point, `docket68/n1star/checks/twodomainx5.py`, which also computes the earlier rectangle's
  exit range, τ from −0.960 to −0.702). The linearised constraint map at the approximant's slice data has no 1/λ
  coefficient with both families, on flat space, on Vaidya with an outgoing phase that is not null there, and on a static
  background with both phases null (computed, exactly, `checks/data5two.py`), and with both families' second harmonics as
  well (computed exactly on flat space and on Vaidya; with them the constraint system's principal coefficients are the
  background's, computed), and a wave with a trace on the spheres gives one. Not done: the background on the whole
  domain, the constraints' solution on its slice, the dynamic outgoing null phase, and the proof written out at the level
  of sections 5 and 6. No statement about several families is proved.
```

New:

```
- **More families.** Two crossing radial null dusts, one ingoing and one outgoing, are carried through the record's
  argument: the two-dust background on the whole domain, the approximant to every order, the uniform estimate and the
  data (deduced, the identities computed; supplement `docket68/n1star/FAMILIES5-FULL.md` Part I). In the T² class each
  family's null second fundamental form is diag(θ_h, κ1, κ2), the torus terms first order, and at an axis the planar
  shear is recovered elliptically from the expansion, so the class Einstein–null-dust system is Cauchy-stable on compact
  domains of the record's type, without smallness, for caustic-free dusts whose lateral boundaries are adapted (one
  family) where they meet an axis (deduced; `docket68/n1star/FAMILIES5-AXIS.md`). A massless Vlasov limit in the class
  is restricted (computed); a smooth restricted field never reaches an axis off the axial directions, its density
  growing like 1/ρ2 there (computed, `docket68/n1star/checks/vlasovhf5.py` H7), and at an axis point at most one
  ingoing and one outgoing family are separated (computed, `docket68/n1star/checks/axisphase5.py`). Every smooth class
  Einstein–restricted massless Vlasov solution whose field is a family of dusts labelled by initial direction,
  caustic-free, off the axes and at an angle from the radial dusts where it meets them, the radial dusts having adapted
  lateral boundaries at the axes, on a domain of the record's type whose initial spheres have positive mean curvature
  and a hyperbolic momentum system, is a weak limit of class vacuum metrics along odd N (deduced: N-dust approximants
  uniform in N; torus-polarised waves at frequencies 1, Λ, …, Λ^(N−1), which leave no combination of phases resonant up
  to the order the scheme uses; data with overlapping families, whose only divisors are spacetime symbols; the N-family
  energy estimate by the two-family ledger applied family by family; a diagonal choice of λ_N, as Huneau and Luk do;
  `docket68/n1star/FAMILIES5-VLASOV.md`, `docket68/n1star/FAMILIES5-R6.md`, `docket68/n1star/FAMILIES5-R7.md`, the
  identities, divisors and data step computed). These hypotheses are open for perturbations with supports in a fixed
  neighbourhood (deduced), and an explicit test family on Tangherlini meets them (computed,
  `docket68/n1star/checks/vlasovex5.py`). Data localised in an angle exist on cones exactly (computed) and, near Part
  I's data, on all of Part I's slice in a band widened by a computed amount (deduced): Rácz's split is hyperbolic on the
  slice except a band inside the shell (computed, `docket68/n1star/checks/racglobal5.py`), where no foliation of that
  slice is hyperbolic (deduced from Rácz's characteristic equation) and a slice bent by 0.0015 is hyperbolic everywhere
  (certified by interval arithmetic for the computed background, `docket68/n1star/checks/racslice5.py`,
  `docket68/n1star/checks/intcert5.py`). Near Part I's data, exactly localised vacuum data whose first-order part
  perturbs the extrinsic curvature alone do not exist for small amplitude: their charge is minus a sum of squares minus
  a term carrying the mass, at the axes too (deduced; the identity computed and the last term's sign certified,
  `docket68/n1star/checks/qsign5.py`, `docket68/n1star/checks/intcert5.py`); with matter obeying the dominant energy
  condition such data do not exist outside the horizon, and inside it they exist with outgoing null dust (deduced; the
  sign computed). For first-order parts that perturb the metric the charge is minus the canonical energy (the
  identification not proved here), whose sign is not decided: that is the one missing input, and nothing weaker settles
  exact vacuum localisation at second order.
```

## Files

`FAMILIES5-R7.md` (this note). New: `checks/intcert5.py` (C1-C2, certified, with controls; several minutes under
load), with its `.out`. Changed and rerun in full, `.out` regenerated, PASS:
- `checks/qsign5.py`: Q1-Q7, about a quarter of an hour under load;
- `checks/nfamily5.py`: N1-N5, about 75 minutes under load;
- `checks/racslice5.py`, `checks/racglobal5.py`, `checks/katonl5.py`, `checks/twobg5.py`, `checks/vlasovhf5.py`.

Bracketed [R7] notes are in FAMILIES5-R6.md and FAMILIES5-VLASOV.md.
