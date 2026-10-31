# FAMILIES5 -- more matter families: several null dusts, angular separation, Vlasov

Status: scoping note (D361); proposed, nothing proved. Read by verifier 167 (D362), findings seated. Section 1's two
deductions on the cross coupling added (D363-D364).

The paper's open item "more families" (RESPONSE-HL-5D.md section 9): "Several dusts, angular separation, and the passage
to Vlasov matter are not attempted." This note sets out what each would need, given what the record's proof uses of
having a single family. It names the published work closest to each, read at its abstract, and proposes a first
computable step.

## 1. What the proof uses of one family

- **The phase.** v is an exact eikonal of g0 (paper section 4: "The phase is v, an exact eikonal of g0"), and
  g0⁻¹(dv, dv) = 0 makes the λ⁻¹ term of the expansion vanish (Stage 0).
- **The averaged stress.** It is one null dust along dv, and the θ-mean of the leading equation fixes dμ/dv (2.6)
  (Proposition 2.3).
- **The one large coefficient.** In the linearization (5.1) the only λ⁻¹ coefficient couples s = w(ℓ, ℓ) to the wave
  (section 5.1). The phase-shift identity (Lemma 5.1) comes from the single translation θ ↦ θ + c.
- **The decomposition.** w = h + φ [∂_θ g1], with φ transported along ℓ (5.2). Contracting with ℓ ⊗ ℓ kills every λ⁻¹
  term, because [∂_θ g1](ℓ, ·) = 0 (section 5.2).

With families k = 1, …, N, phases φ_k and generators ℓ_k, the ansatz becomes a profile in (X, θ_1, …, θ_N). (4.1) holds
for each θ_k separately, so there are N phase-shift identities, N large couplings λ⁻¹ s_k [∂²_(θ_k) g1^(k)] with
s_k := w(ℓ_k, ℓ_k), and N transported phases φ_k. Contracting with ℓ_k ⊗ ℓ_k kills family k's coupling but not family
j's: [∂²_(θ_j) g1^(j)](ℓ_k, ℓ_k) is not zero in general. These cross couplings are the new analytic difficulty.

**Where the cross coupling sits in the class (deduced from the record's Stage 0; to be computed in step 4).** The
record's first-order wave is W = W_TT + χ dv² (`lead5.py`). W_TT has components only on the block of the S³
angles, so W_TT(ℓ, ·) = 0 for every vector ℓ in the (τ, r) plane, and χ dv² is the second harmonic's gauge term.

- For an outgoing family the analogue is W'_TT + χ' du².
- So [∂²_(θ_2) g1^(out)](ℓ_in, ℓ_in) = ∂²_(θ_2) χ' (du(ℓ_in))², and [∂²_(θ_1) g1^(in)](ℓ_out, ℓ_out) = ∂²_(θ_1) χ
  (dv(ℓ_out))².
- Since du(ℓ_in) ≠ 0 ≠ dv(ℓ_out) away from the horizon (in ingoing coordinates du degenerates there; verifier 168's
  F2), the cross couplings are present. They enter only through the second-harmonic gauge terms χ and χ', not
  through the transverse-traceless waves.
- A gauge or an ansatz that removes χ and χ' at first order, or moves them to higher order, would remove the cross
  couplings at leading order. Whether one exists in the class is the first analytic question of the two-family case.

**χ dv² is pure gauge, and a generalised wave gauge removes it (deduced, D364; to be computed in step 4).**
Write k := dv, null and geodesic for g0 (k = ∇v, so ∇_k k = ½∇|k|² = 0). Take ∂ for the derivative in X at fixed θ.

- *Pure gauge.* For Z := λ² Φ(X, v/λ) k^♯, ∂_a Φ = Φ_(,a) + λ⁻¹ ∂_θΦ k_a gives
  L_Z g0 = 2λ ∂_θΦ k ⊗ k + λ²(2Φ_(,(a) k_(b)) + 2Φ ∇_a k_b). With ∂_θΦ = χ/2, which exists since χ has θ-mean zero
  (`lead5.py`:149), χ dv² is L_Z g0 at order λ, with an order-λ² completion.
- *Why the record carries it.* In the wave-map gauge relative to g0 (RESPONSE-HL-5D.md:238) the reduced operator's
  principal part is −½ g^(ab) ∂_a ∂_b, whose symbol vanishes at k. So no λ² term can meet a λ⁰ second harmonic; only
  g1's transport −(k·∇ + ½□v) ∂_θ g1 can. The vv second harmonic of R^(0) is therefore met by χ's transport along ℓ
  (RESPONSE-HL-5D.md:439-442; `lead5.py`:19-20).
- *A generalised wave gauge.* Solve instead Ric(g) − δ*_g(Υ(g) − H) = 0 with a fixed gauge source H := λ h(X, v/λ) k.
  Then δ*H = ∂_θh k ⊗ k + O(λ), so the vv second harmonic S k ⊗ k of R^(0) is met algebraically by ∂_θh = −S,
  periodic since S has mean zero. Then χ = 0. Likewise H' := λ h'(X, u/λ) du gives χ' = 0.
- *The cross couplings.* With χ = χ' = 0, g1^(in) = W_TT and g1^(out) = W'_TT are purely angular. So
  [∂² g1^(j)](ℓ_k, ℓ_k) = 0 for all j, k, and contracting the linearization with ℓ_k ⊗ ℓ_k kills both families' large
  terms, as for one family (section 5.2). The cross coupling of section 1 is then a gauge artefact of the record's
  gauge.
- *What it costs, still open.* H is fixed, so it does not enter the linearization. But the constraint Υ − H must be
  propagated, and the solution compared with the record's gauge (by the diffeomorphism exp Z, O(λ²) in C⁰). Step 4
  must also check that no other λ⁻¹ coefficient appears in the two-family linearization; in one family (5.1) there is
  exactly one. [Tou24]'s abstract names "a generalised wave gauge" for the interaction of the waves. Whether it is
  this one is not read: abstract only.

## 2. Several null dusts

- **Published (READ: abstract of [Tou24], arXiv:2402.17530v2).** For a regular solution of Einstein-null dusts "without
  restriction on the number of dusts", families of vacuum solutions are built "based on a multiphase geometric optics
  ansatz", working "in a generalised wave gauge" and controlling "the interaction of waves propagating in different
  null directions, relying crucially on the non-linear structure of the Einstein vacuum equations". That is in 3 + 1
  dimensions, without symmetry. Its theorem also assumes the background close to Minkowski, as the repository's own
  reading records (N1STAR-STATUS.md:81-82; lemmas/BOUNCE-RESEARCH.md:3120-3121). That is the decisive contrast here:
  our setting has five dimensions, the class, and a black-hole background.
- **In the class.** A phase must be a function of the orbit space (τ, r, θ). The two radial null phases of g0 are v
  (ingoing) and u (outgoing, along the outgoing null direction of the background). A θ-dependent null phase solves the
  eikonal equation in the orbit space with angular momentum; its rays focus, and it is not proposed first.
- **The natural first case** is two families, the ingoing shell (phase v) and an outgoing wave packet (phase u) given
  on Σ_τ0 outside the hole. The two crossing at an angle is what "angular separation" requires. dv and du are
  transversal null covectors, so d(v ± u) is timelike or spacelike, and more generally k_1 dv + k_2 du is non-null
  whenever k_1 k_2 ≠ 0. The quadratic interactions at (v ± u)/λ are then non-resonant (deduced, in the wave-map gauge of
  the paper's section 2.5, where the principal part of Ric^H is −½ g^(ab) ∂_a ∂_b). The two-scale operator acts on them
  through the non-zero symbol g0⁻¹(d(v ± u), d(v ± u)), so the approximant solves for them by division, with no
  transport. "Angular separation" is meant in the sense of [HL18] Definition 4.1, as in the paper (RESPONSE-HL-5D.md:96).
- **The limit** is expected to be Einstein with two null dusts, ingoing and outgoing, in the class: a crossing-dust
  generalisation of Vaidya, each dust's energy obeying its own Isaacson law and the dusts coupling only through the
  metric. This is to be shown by step 4 (b). The background stays round, of Vaidya type, only if the outgoing packet's
  averaged stress is round. For the ingoing wave that needed the profile identity h²(c⁴ + s⁴) = 1 (paper section 2.4).

## 3. Vlasov

- **Published (READ: abstract of [HL25], arXiv:2506.21779v1).** "Given suitable small, localized, U(1)-symmetric
  solutions to the Einstein-massless Vlasov system in an elliptic gauge, we prove that they can be approximated by
  high-frequency vacuum spacetimes". "The proof proceeds by first approximating solutions to the Einstein-massless
  Vlasov system by solutions to the Einstein-(multiple) null dust system, then approximating solutions to the
  Einstein-null dust system by vacuum solutions. In the process, we take the number of families of dusts to infinity."
- **Here.** The background is large (a black hole), not small and localized. So the route would need sections 1-2
  with constants uniform in the number of families, on the record's domain. That is beyond the two-family step and is
  not proposed yet.

## 4. The first computable step (proposed)

Stage 0 of a two-phase ansatz in the class:

    G = g0^(2) + λ(W_in(X, θ_1) + W_out(X, θ_2)) + λ² ĝ_2(X, θ_1, θ_2),     θ_1 = v/λ, θ_2 = u/λ,

on an exact two-dust background g0^(2). It is not explicit: u and v are its double-null coordinates, and the record's
explicit Vaidya computations (domain, foliation) would all need redoing on it. The aim is to compute, as `lead5.py`
does for one phase:

- (a) R^(−1) = 0;
- (b) the θ-means of R^(0) give two Isaacson laws, one for each dust;
- (c) the mixed harmonics e^(i(θ_1 ± θ_2)) of R^(0) are solved algebraically by ĝ_2, the symbol being non-zero wherever
  dv and du are independent;
- (d) the second harmonics of each family are handled as in one-phase Stage 0 (the χ dv² term and its outgoing twin).

The analytic step after that is the energy estimate with two large couplings and their cross terms (section 1), as in
[Tou24].

## 5. Sources

READ (abstracts, fetched from arxiv.org on 2026-10-31 and quoted from those pages): [Tou24] A. Touati, "The reverse
Burnett conjecture for null dusts", arXiv:2402.17530v2; [HL25] C. Huneau, J. Luk, "High-frequency backreaction for
the Einstein equations under U(1) symmetry: from Einstein-dust to
Einstein-Vlasov", arXiv:2506.21779v1. The record: RESPONSE-HL-5D.md sections 2.4, 4, 5.1-5.2 and 9.
