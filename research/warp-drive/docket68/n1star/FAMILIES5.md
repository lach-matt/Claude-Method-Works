# FAMILIES5 -- more matter families: several null dusts, angular separation, Vlasov

Status: scoping note (D361); proposed, nothing proved. To be read.

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

## 2. Several null dusts

- **Published (READ: abstract of [Tou24], arXiv:2402.17530v2).** For a regular solution of Einstein-null dusts "without
  restriction on the number of dusts", families of vacuum solutions are built "based on a multiphase geometric optics
  ansatz", working "in a generalised wave gauge" and controlling "the interaction of waves propagating in different
  null directions, relying crucially on the non-linear structure of the Einstein vacuum equations". That is in 3 + 1
  dimensions, without symmetry, on a regular background. Our setting has five dimensions, the class, and a black-hole
  background.
- **In the class.** A phase must be a function of the orbit space (τ, r, θ). The two radial null phases of g0 are v
  (ingoing) and u (outgoing, along the outgoing null direction of the background). A θ-dependent null phase solves the
  eikonal equation in the orbit space with angular momentum; its rays focus, and it is not proposed first.
- **The natural first case** is two families, the ingoing shell (phase v) and an outgoing wave packet (phase u) given
  on Σ_τ0 outside the hole. The two crossing at an angle is what "angular separation" requires. dv and du are
  transversal null covectors, so d(v ± u) is timelike or spacelike. The quadratic interactions at (v ± u)/λ are then
  non-resonant: the two-scale operator acts on them through the non-zero symbol g0⁻¹(d(v ± u), d(v ± u)), so the
  approximant solves for them by division, with no transport.
- **The limit** is Einstein with two null dusts, ingoing and outgoing, in the class: a crossing-dust generalisation of
  Vaidya. Each dust's energy obeys its own Isaacson law, and the dusts couple only through the metric.

## 3. Vlasov

- **Published (READ: abstract of [HL25], arXiv:2506.21779v1).** "Given suitable small, localized, U(1)-symmetric
  solutions to the Einstein-massless Vlasov system in an elliptic gauge, we prove that they can be approximated by
  high-frequency vacuum spacetimes". The proof first approximates Vlasov by multiple null dusts and then dusts by
  vacuum, "In the process, we take the number of families of dusts to infinity."
- **Here.** The background is large (a black hole), not small and localized. So the route would need sections 1-2
  with constants uniform in the number of families, on the record's domain. That is beyond the two-family step and is
  not proposed yet.

## 4. The first computable step (proposed)

Stage 0 of a two-phase ansatz in the class:

    G = g0^(2) + λ(W_in(X, θ_1) + W_out(X, θ_2)) + λ² ĝ_2(X, θ_1, θ_2),     θ_1 = v/λ, θ_2 = u/λ,

on the exact two-dust background g0^(2). The aim is to compute, as `lead5.py` does for one phase:

- (a) R^(−1) = 0;
- (b) the θ-means of R^(0) give two Isaacson laws, one for each dust;
- (c) the mixed harmonics e^(i(θ_1 ± θ_2)) of R^(0) are solved algebraically by ĝ_2, the symbol being non-zero where
  the packets cross;
- (d) the second harmonics of each family are handled as in one-phase Stage 0 (the χ dv² term and its outgoing twin).

The analytic step after that is the energy estimate with two large couplings and their cross terms (section 1), as in
[Tou24].

## 5. Sources

READ (abstracts): [Tou24] A. Touati, "The reverse Burnett conjecture for null dusts", arXiv:2402.17530v2; [HL25] C.
Huneau, J. Luk, "High-frequency backreaction for the Einstein equations under U(1) symmetry: from Einstein-dust to
Einstein-Vlasov", arXiv:2506.21779v1. The record: RESPONSE-HL-5D.md sections 2.4, 4, 5.1-5.2 and 9.
