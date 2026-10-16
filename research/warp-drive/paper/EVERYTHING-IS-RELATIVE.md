---
title: "Everything Is Relative"
subtitle: "One theorem on how quantum physics stands to relativity: whatever can exist keeps the one light cone, and the leading quantum correction to gravity's second-order law is held to zero"
author: "Matthew Lach · Independent Researcher"
date: "16 October 2026 · draft 2"
---

**Status of this draft.** A draft for review. Every statement below carries one of five labels:

- **computed**: exact unless marked, and re-run for this paper;
- **deduced**: follows from the statements it cites;
- **READ**: quoted verbatim from the source, re-read at source for this paper, with page and equation;
- **estimate**;
- **postulate**: assumed, named, and never derived.

Nothing labelled READ is used beyond its source's own hypotheses. The machine check `qr_paper_check.py` asserts every
computed number printed here. Its run is in Appendix C.

---

## Abstract

We prove one statement and mark where it stops. Whatever can exist carries energy and momentum. It is then subject to
relativity in three senses, each stronger than the last:

1. its invariants are Lorentz invariants, so it moves on or inside the light cone (*special*);
2. it couples to one metric with one strength, so everything falls alike and everything gravitates (*general*);
3. it keeps the one light cone. Every front of every field, gravity's own included, lies on or inside the null cone of
   that metric, at every point of every background that can exist (*one cone*).

Senses (1) and (2) are proved kind by kind. They use exact computation and the theorems of Lovelock, Deser, and Peres
and Terno, and they are tested to the precision of GW170817, MICROSCOPE and Cassini. Sense (3) is a postulate, the
one-cone principle. It is stated as a postulate and never derived.

The relation to quantum physics runs through three results:

- **Quantum information lives inside the causal structure.** Measurement cannot violate relativistic causality, and no
  local operation on one half of an entangled pair changes what the other half can observe. We compute the second fact
  for every two-qubit pure state.
- **The one constant classical relativity leaves open is the leading quantum correction.** Lovelock's theorem leaves
  gravity's second-order law exactly Einstein's in four dimensions. In five it admits one more coupling, the
  Gauss–Bonnet α, which the string effective action reads as "the leading order quantum correction". We compute, from
  the field equations, that with α ≠ 0 gravity's own waves leave the light cone, for either sign of α. On a black hole
  the cones obey the sum rule 2(c_T − 1) + 2(c_V − 1) + (c_S − 1) = 0, and on a plane gravitational wave the
  displacements sum to zero. The four-dimensional route by which the same term acts, a scalar coupled to the
  Gauss–Bonnet density, fails the same test for every coupling with f′ ≠ 0. Under the postulate, α = 0 exactly.
- **Quantum corrections begin where one dimensionless number reaches one.** Buckingham's theorem on {G₅, ħ, c, ℓ, R}
  leaves two numbers, and only x = l₅² R carries ħ. Under four named premises the two-derivative law is exact where
  x ≪ 1 and fails where x reaches one.

The limits are part of the result:

- the experiments bound departures only to their precision;
- the cone splitting is computed on named families of backgrounds, and is generic by Reall, Tanahashi and Way;
- the scattering argument of Camanho, Edelstein, Maldacena and Zhiboedov corroborates only for |α| ≫ l_P5²;
- theories with field equations beyond second order (Einsteinian cubic gravity, f(R)) are not tested;
- nothing here is a theory of quantum gravity.

What is proved is compatibility, a single causal structure that quantum physics and gravity share, and not
unification.

---

## 1 · Introduction

### 1.1 The question

Quantum physics and relativity are usually said to be incompatible. The sentence means several different things. One
reading is that quantum measurement seems to act instantaneously at a distance. Another is that gravity resists
quantisation as an ordinary field theory. A third is that the classical field equations must fail at high curvature,
and no one knows the law that replaces them.

This paper poses the question differently:

> Everything that exists, with or without mass, is subject to relativity.

Asked this way, the question is not whether one theory can be derived from the other. It asks whether there is anything
that can exist and is not subject to relativity, and whether quantum physics supplies such a thing.

### 1.2 What is proved, and what is postulated

We prove the statement in senses (1) and (2) of the abstract, kind by kind (§§4–8, Theorem 1). We then ask what
relativity still leaves free. The answer is one constant: the Gauss–Bonnet coupling α of the five-dimensional
second-order law. That constant is exactly the place where the quantum correction enters gravity's law.

Under the postulate that everything keeps the one light cone, we show that constant is zero (§10, Theorem 2).
We also show that its four-dimensional scalar realisation is excluded (§11). Last, we derive where the classical law
stops: the boundary at which quantum corrections must begin (§12).

The postulate is named as such wherever it is used. Without it, Theorem 1 still stands. Theorem 2 then
becomes a conditional: if α ≠ 0, gravity has fronts outside the light cone.

### 1.3 A single theorem, and whether it is a law

The paper presents a single theorem: one statement proved through a chain of lemmas. Lemmas 1–5 give Theorem 1 (the statement in senses (1)–(2)). Lemmas 6–7 with the postulate give Theorem 2 (the
statement in sense (3), and α = 0). Proposition 8 gives its boundary.

Whether it can be called a law is answered in §14. In short, it is a theorem relative to stated premises. Its law-like
content is the postulate, together with the experiments that bound departures from it. No proof can make an empirical
universal into a law. What a proof can do, and what this paper does, is show what that universal forces.

### 1.4 Scope

The paper is built from first principles and established results only. Each step is either computed here, deduced
here, or taken from a published theorem or measurement with its hypotheses stated. Nothing else is needed to follow
it.

---

## 2 · Postulates, definitions, premises

**Definition 1 (a kind).** A *kind* is anything that can exist and acts on or carries anything else. It is represented
by a symmetric stress–energy tensor T_ab, or carried by something that has one. Its *mass* m is defined by
p_a p^a = −m²c² where it has a four-momentum. *With or without mass* means m ≥ 0, with m = 0 admitted.

**Definition 2 (subject to relativity).** A kind is

- *subject to special relativity* if its invariants are Lorentz invariants, so that it moves on (m = 0) or inside
  (m > 0) the light cone in every inertial frame;
- *subject to general relativity* if it couples to a single metric g with a universal strength, both falling and
  gravitating;
- *one-cone* if every characteristic front of its field equations, on every background, is on or inside the null cone
  of g. A front is *characteristic* when its normal ξ makes the principal symbol of the field equations degenerate on
  physical polarisations (Reall, Tanahashi and Way, §2.2, READ).

**Postulate O (the one-cone principle).** Everything that can exist keeps the one light cone: every front of every
field, gravity's own included, at every point, on every background that can exist, lies on or inside the null cone of
the one metric.

It strengthens what Lemmas 2–3 establish. Local Lorentz invariance and universal coupling fix one cone for signals in
flat space and in the weak field. Postulate O asks the same of the characteristic fronts on every background. It is
not derived anywhere below, and every result that uses it says so.

**Premises of the outside theorems.** These are used only where named:

- **(PL) Lovelock.** The field equations of the metric are given by a symmetric, divergence-free, natural (0,2)-tensor
  depending on the metric and its first and second derivatives (locality, second order).
- **(PD) Deser.** A massless spin-2 field coupled to a conserved source must, for consistency, couple to the total
  stress tensor, its own included.
- **(PT) Peres and Terno.** Lorentz transformations are implemented in quantum theory by unitary transformations.
- **(EEP)** The Einstein equivalence principle, as tested.

---

## 3 · The method

The proof is kind by kind. Each lemma carries its own evidence, of one of three types:

- an exact computation, done in sympy and re-run for this paper (module named in Appendix A);
- a theorem from the literature, applied only on its hypotheses (READ, quoted);
- an experiment, quoted with its bound (READ), which bounds a departure and never fixes a value.

---

## 4 · What can exist (Lemma 1)

**Lemma 1.** Every kind the statement concerns carries energy and momentum:

- matter, massive or massless: particles, scalar fields, gauge fields;
- vacuum energy;
- the tension of an extended object (a sheet);
- geometry itself (gravitational waves);
- information, through its carrier.

*Evidence.*

- Matter, vacuum and tension each have a stress tensor. A vacuum has T_ab = −ρ g_ab, and a sheet of tension τ has
  T_ab = −τ h_ab on its world-volume, with h its induced metric (deduced).
- For particles, `E^2 = p^2 c^2 + m^2 c^4`, which at m = 0 is E = pc (computed).
- Information is not a separate substance. Peres and Terno (quant-ph/0212023, §I.A, p. 1, READ): signal speeds are
  bounded "because information needs a material carrier, and the latter must obey the laws of physics. Information is
  physical (Landauer, 1991)."
- Again (§III.C, p. 13, READ): "information has to be carried by material objects, quantized or not."

*Scope.* Something with no energy and momentum at all would act on nothing and carry nothing. It is outside the
statement and is not claimed.

---

## 5 · Special relativity for every kind (Lemma 2)

**Lemma 2.** Let Λ be a Lorentz boost of rapidity y. Then:

- Λ^T η Λ = η;
- a massless four-momentum stays null and future-pointing (its energy becomes E e^y > 0);
- a massive one keeps p·p = −μ² and its speed stays below c (1 − v′² = μ²/E′²);
- a scalar's Lagrangian −½ ∂φ·∂φ − V, the gauge invariants F_ab F^ab and ε^abcd F_ab F_cd, a vacuum's stress −ρη_ab,
  and a sheet's Nambu–Goto density √(−det h) (for boosts along the sheet) are each unchanged.

All of this is computed, exact, for every y.

*Test (READ).* GW170817 with GRB 170817A (LIGO–Virgo, Fermi-GBM, INTEGRAL, arXiv:1710.05834, abstract and eq. (1), pp.
1 and 6) constrain "the difference between the speed of gravity and the speed of light to be between −3 × 10⁻¹⁵ and
+7 × 10⁻¹⁶ times the speed of light". Will (arXiv:1403.7377, abstract, READ): the Einstein equivalence principle "is
well supported by experiments such as the Eötvös experiment, tests of local Lorentz invariance and clock experiments."

*What the test does and does not show.* The bound is on one speed over a near-flat path. It says nothing about the
characteristic cones of a strongly curved background (§9, qualification Q1).

*Check of the computation.* Replacing the Lorentz boost by a Galilean one makes the null-cone and metric checks fail,
which is the instrument's first mutant.

---

## 6 · The universality of gravitation (Lemma 3)

**Lemma 3.** Gravitation couples to every kind through one metric with one strength, with mass or without.

*Evidence.*

- **Metric theories (READ, Will, arXiv:1403.7377, §2.1, p. 6).** "it is possible to argue convincingly that if EEP is
  valid, then gravitation must be a "curved spacetime" phenomenon", and "the only theories of gravity that can fully
  embody EEP are those that satisfy the postulates of "metric theories of gravity"". Will calls this an argument, not a
  theorem, and it is used here as such.
- **Universal coupling from consistency (READ, Deser, gr-qc/0411023, *Gen. Rel. Grav.* 1 (1970) 9, p. 4).** The
  massless spin-2 field, coupled to a source, "must actually be coupled to the total stress-tensor including that of
  the φ-field itself" (p. 1), and "Consistency has therefore led us to universal coupling, which implies the
  equivalence principle." This holds under (PD). Deser notes that consistency and linearity "may also be reconciled if
  locality is abandoned" (p. 1, footnote 2), so locality is a premise.
- **Geodesics carry no mass (computed).** For any static spherical metric, the Euler–Lagrange equations of
  ½ m g_ab ẋ^a ẋ^b are m times those of ½ g_ab ẋ^a ẋ^b, so the paths are independent of m. Light follows the same law
  with g_ab ẋ^a ẋ^b = 0. A force that knows the body's mass makes the check fail (mutant).
- **Light bending (computed).** Light is bent by (1 + γ) 2GM/(c²b). This is 1.751 arcsec at the Sun's limb with γ = 1.

*Tests (READ).*

- MICROSCOPE (arXiv:2209.15487, eq. (5), p. 5): η(Ti, Pt) = [−1.5 ± 2.3 (stat) ± 1.5 (syst)] × 10⁻¹⁵.
- Cassini, as quoted in arXiv:1710.05834, p. 7: γ_EM − 1 = (2.1 ± 2.3) × 10⁻⁵, "from the measurement of the Shapiro
  delay (at radio wavelengths) with the Cassini spacecraft (Bertotti et al. 2003)".
- Gravity's own waves feel the same Shapiro delay as light (arXiv:1710.05834, eq. (4), p. 7):
  −2.6 × 10⁻⁷ ≤ γ_GW − γ_EM ≤ 1.2 × 10⁻⁶.

So the massless are gravitated as the massive are, and so is gravity itself, to these precisions.

---

## 7 · The law of the one metric (Lemma 4)

**Lemma 4 (Lovelock's theorem, READ; the count computed).** Under (PL), the symmetric, divergence-free, second-order
natural (0,2)-tensors of a metric in n dimensions are spanned by the Lovelock tensors L₀, …, L_p, with
p = ⌊(n − 1)/2⌋. In Navarro and Navarro's statement (arXiv:1005.2386, Theorem 2.6, p. 9, READ):

> "Let (X, g) be a pseudo-riemannian manifold of dimension n and let p be the integer part of (n − 1)/2. The Lovelock
> tensors: L₀, . . . , L_p are a basis for the R-vector space of second-order natural (0,2)-tensors on X that are
> symmetric and divergence-free."

Here L₀ is the metric and L₁ is Einstein's tensor (p. 9). The count gives p(4) = 1 and p(5) = 2 (computed), so:

- **In four dimensions** the only field equations are Einstein's with a cosmological constant.
- **In five** there is exactly one more term, Lanczos's tensor. It is "quadratic on the second derivatives of the
  metric, but only exists if X is of dimension strictly greater than 4" (Navarro and Navarro, p. 1, READ).

The theorem is Lovelock's (1970–72). Lanczos found the quadratic tensor in 1938. Both are named through Navarro and
Navarro's short proof, which is the text re-read here; the original papers were not re-read.

**The one constant, and why it is the quantum correction.** Charmousis and Dufaux (hep-th/0202107) write the
five-dimensional second-order action as R + 12k² + α(R_abcd R^abcd − 4R_ab R^ab + R²) (eq. (2), p. 4), with
Λ = −6k². They say it "is the most general action that will yield second order partial differential equations with
respect to the metric components in 5 dimensions" (p. 5, READ). Of α they write (p. 3, READ):

> "Furthermore in an effective action approach of string theory, the Gauss-Bonnet term corresponds to the leading
> order quantum correction to gravity in particular in the case of the heterotic string [15]."

They cite Gross and Sloan, 1987, not re-read here. Their conclusion repeats it: the coupling "provides a window to the
leading quantum gravity correction coming from string theory" (§V, p. 16, READ).

The Gauss–Bonnet term is the Euler density of four dimensions. It "yields in D = 4 a boundary term hence a topological
and not dynamical contribution" (p. 3, READ). So:

- in four dimensions the term acts only if something varies its coefficient, a scalar f(φ) (§11);
- in five it acts directly through α (§10).

*Qualification carried.* The phrase "leading order quantum correction" is Charmousis and Dufaux's reading inside the
string effective action. This paper uses it as their identification and does not derive it. Lovelock's theorem fixes
the law up to α. Deser's consistency argument does not require α (it builds Einstein's equations). So the one freedom
relativity leaves gravity's second-order law is the one place a quantum correction enters it.

---

## 8 · Information and entanglement (Lemma 5)

**Lemma 5.** Quantum measurement, and every local operation on one part of an entangled system, transmits nothing
outside the light cone.

*READ.* Peres and Terno (quant-ph/0212023, §III.C, p. 13):

> "Therefore quantum measurements do not allow any information to be transmitted faster than the characteristic
> velocity that appears in the Green's functions of the particles emitted in the experiment. In a Lorentz invariant
> theory, this limit is the velocity of light. In summary, relativistic causality cannot be violated by quantum
> measurements. The only physical assumption that is needed to prove this assertion is that Lorentz transformations of
> the spacetime coordinates are implemented in quantum theory by unitary transformations of the various operators."

*Computed (this paper).* Take an arbitrary two-qubit pure state |ψ⟩ = Σ a_i |i⟩, with four symbolic complex
coefficients. Let Alice either apply an arbitrary local unitary U(θ, φ) ⊗ 1, or make a non-selective projective
measurement in the basis U|0⟩, U|1⟩. In both cases Bob's reduced density matrix ρ_B is unchanged, identically in a_i,
θ, φ. A non-local gate (CNOT) passed off as Alice's local operation does change ρ_B, and the check catches it (mutant
`signal`). Entanglement therefore correlates without signalling. Whatever it carries, it carries through the causal
structure of Lemmas 2–3.

*What is not claimed.* Peres and Terno also show that "Quantum entropy is not a Lorentz covariant concept" (abstract,
READ). The relativity of information is that of its carrier, not an invariance of every information-theoretic quantity.

---

## 9 · The statement in senses (1)–(2) (Theorem 1), and why no index is run

**Theorem 1.** Every kind that can exist, with mass or without, satisfies the following:

1. It carries energy and momentum (Lemma 1).
2. Its invariants are Lorentz invariants. It moves on the light cone if massless and inside it if massive, in every
   inertial frame (Lemma 2).
3. It couples to one metric with one strength, falling alike and gravitating (Lemma 3).
4. It carries information only through its carrier and signals nothing outside the light cone (Lemma 5).
5. The one metric obeys Einstein's law in four dimensions, and Einstein's law with at most one constant more, α, in
   five (Lemma 4).

The theorem is deduced from Lemmas 1–5. It is exact on the premises of the outside theorems, and tested to the
experiments' precision.

*Scope (qualification Q1 of the first verification, §13).* What Theorem 1 proves of "keeping the light cone" is
special-relativistic. It covers flat-space boost invariance, together with GW170817's near-flat equality of speeds. It
proves nothing about the characteristic cones of a curved background. That stronger statement is Postulate O, and only
Theorem 2 uses it.

*A finding about Theorem 1 itself.* Read together with Postulate O, the two halves of Theorem 1 hold together only at
α = 0. Its fifth clause allows a constant that, if nonzero, puts gravity's fronts off the light cone (§10). So the statement fixes
the one constant it seemed to leave open.

*No index is run.* A table of (kind, Lorentz-invariant, couples universally, falls alike) would carry the value 1 in
every cell. That is a constant column on every axis, from which nothing can be measured, and it would hold the answer
as its own column. Universality is proved kind by kind instead.

---

## 10 · The coupling evaluated by the one light cone (Lemma 6, Theorem 2)

### 10.1 The instrument

In five dimensions, write the field equations as E = G + Λ + αH. The Einstein and Gauss–Bonnet tensors are written
with the generalised Kronecker delta in an orthonormal frame: G = −(1/4) δ⁽³⁾ R, H = −(1/8) δ⁽⁵⁾ R R.

The normalisation is checked before use, against two exact solutions:

- **Tangherlini.** The five-dimensional Schwarzschild–Tangherlini metric f = 1 − m/r² comes out Ricci-flat, with
  Kretschmann scalar 72 m²/r⁸.
- **Boulware–Deser–Cai.** The hole f = κ + r²(1 − q)/(4α), with q² = 1 + 8αm/r⁴ + 4αΛ/3, solves E = 0 exactly for
  κ = 1 and κ = 0, with α, m, Λ and r left symbolic. The solution is Boulware and Deser's (1985) and Cai's (2002); it is
  quoted as Reall, Tanahashi and Way's eq. (5.15), READ, and Charmousis and Dufaux's eq. (17), READ.

The principal symbol, the part of the linearised equations that decides where waves can go, is

P(ξ)·t = −½ [δ⁽³⁾ ξξ t + α δ⁽⁵⁾ ξξ t R].

It is computed to be gauge invariant (it kills ξX + Xξ), divergence-free (ξ·P = 0) and symmetric. A front with normal ξ
is characteristic when P(ξ) has a non-gauge kernel. On transverse tensors this is the vanishing of a determinant, a
polynomial in ξ₀ (Reall, Tanahashi and Way, §§2.2 and 3.1, READ). Doubling the Gauss–Bonnet part of the symbol against
the field equation is caught (mutant).

### 10.2 Lemma 6: the cones split from the light cone when α ≠ 0

**(a) Einstein's law.** At α = 0, every characteristic front is null, on any background (computed). Reall, Tanahashi and
Way (arXiv:1406.3379, §1, p. 2, READ): "For the Einstein equation, a hypersurface is characteristic if, and only if,
it is null: "gravity travels at the speed of light"."

**(b) Any static, spherical or planar background.** Let the pair curvatures be K₁ = R^{tr}\_{tr},
K₂ = R^{ti}\_{ti} = R^{ri}\_{ri} and K₃ = R^{ij}\_{ij}. A front moving along the sphere is characteristic at
ξ₀² = c|ξ|². The graviton's five polarisations fall on three cones:

- c₁ = (1 + 4αK₁)/(1 + 4αK₂), twice;
- c₂ = (1 + 4αK₂)/(1 + 4αK₃), twice;
- c₃ = (3 + 32αK₂ + 64α²K₂² − 4α(K₁ + K₃) − 16α²K₁K₃) / (3(1 + 4αK₂)(1 + 4αK₃)), once.

Radially every front is null. Every c is 1 when K₁ = K₂ = K₃, that is on anti-de Sitter space, which has curvature but
no Weyl curvature. All of this is computed, exact.

**(c) On the Boulware–Deser hole, exactly.** With A = (1 + 4αΛ/3)/q², the cones are

c_T = 3 − 2A (twice), c_V = A (twice), c_S = 2A − 1 (once),

for the spherical (κ = 1) and the planar (κ = 0) hole alike. These are Reall, Tanahashi and Way's tensor, vector and
scalar cones (their eqs. (5.13) and (5.17) at d = 5, pp. 24–25, READ), here obtained from the field equations
directly. Two routes give one answer.

Moreover A − 1 = −8αm/(r⁴q²), so

**2(c_T − 1) + 2(c_V − 1) + (c_S − 1) = 0** (computed).

The cones fan out about the light cone and cannot all lie inside it:

- for αm > 0 the tensors are outside it;
- for αm < 0 the vectors and the scalar are.

The fastest exceeds light by 16|α|m/(r⁴q²) (computed), at every radius outside the horizon. Reall, Tanahashi and Way
(p. 22, READ): "If c_A(r) > 1 then the outermost graviton cone lies outside the light cone: gravity travels faster than
light. We will see below that this is often the case, including arbitrarily far from the black hole."

**(d) On gravity's own wave.** A plane gravitational wave (Weyl type N, profile diag(2, −1, −1)ε) solves the
Gauss–Bonnet law exactly (computed). Reall, Tanahashi and Way (§4.1, p. 13, READ): "It is easy to see that any such
spacetime is a solution of Lovelock theory with Λ = 0."

A graviton crossing it is characteristic at ξ² = −(l·ξ)² ω, with

ω = 8αε (once), 4αε (twice), −8αε (twice),

which sum to zero (computed). These agree with Reall, Tanahashi and Way's ω_I = −32 k₂ ν_I (eq. (4.11), p. 17, READ)
with k₂ = −α/8. Some ω is positive for either sign of α, which is a front outside the light cone. RTW (p. 14, READ): "there
is generically at least one positive ω_I and so this outermost cone lies outside the light cone".

On the anti-de Sitter background the wave solves the law with Λ = −6k²(1 − 2αk²), and every ω is divided by 1 − 4αk²
(computed). On the stable branch 1 − 4αk² = √(1 − 8αk_CD²), where Λ = −6k_CD² (computed). This is positive inside the
existence range and vanishes at its endpoint 8αk_CD² = 1, where the linearised graviton degenerates (qualification Q3).

### 10.3 Theorem 2

**Theorem 2 (under Postulate O).** In five dimensions, under (PL), the Gauss–Bonnet coupling is zero: α = 0, and
gravity's second-order law is Einstein's exactly.

*Proof (deduced).* The five-dimensional law can carry gravity's own waves and holds black holes, whose Weyl curvature is
not zero (Tangherlini's Kretschmann 72 m²/r⁸ ≠ 0). On either background, α ≠ 0 puts a polarisation of gravity outside
the light cone, whatever α's sign or size within the existence range (Lemma 6 (c), (d)). Postulate O forbids any front
outside the one light cone. At α = 0 every front is null (Lemma 6 (a)). ∎

*Corroboration, within its range.* Camanho, Edelstein, Maldacena and Zhiboedov (arXiv:1407.5597, READ) give a
scattering argument. A graviton crossing a shock wave in Gauss–Bonnet theory gets a time advance: "by choosing
different polarizations we can get time advance for b² ∼ |λ_GB| for any sign of λ_GB" (§2.4, p. 12). So "the purely
Gauss-Bonnet theory (2.17) is acausal" (p. 13). The violation "cannot be fixed by adding conventional particles with
spins J ≤ 2. But, it can be fixed by adding an infinite tower of extra massive particles with higher spins, J > 2"
(abstract), and "a finite number of higher spin particles does not fix the problem" (§4.4, p. 33).

Their result holds only "For α ≫ l_p²" (§1, p. 3). Of order-one coefficients they write: "then we have nothing to say".
It is also a tree-level statement. It corroborates Theorem 2 only for |α| ≫ l_P5² (qualification Q2). Theorem 2 itself
does not use it: Lemma 6 is local and pointwise, not an asymptotic-causality argument.

*What Theorem 2 does not say.*

- It does not say gravity has been seen to keep the light cone in five dimensions. The effect at α ≠ 0 near a hole is
  16|α|m/(r⁴q²), and no measurement reaches it. α = 0 is deduced, not measured.
- It does not say no world could hold an infinite tower of higher spins. Such a tower would take the law outside (PL),
  which Lemma 4 used.
- The split is computed on the families named: static pair-diagonal backgrounds and type N waves. It is generic by
  Reall, Tanahashi and Way (abstract: "characteristic hypersurfaces are generically all non-null"). It is not proved at
  every point where the Weyl curvature is nonzero (qualification Q4).
- It is computed at d = 5. Reall, Tanahashi and Way's statements hold for Lovelock theories in general d (READ), but
  this paper computes only d = 5.

---

## 11 · The four-dimensional scalar–Gauss–Bonnet route excluded (Lemma 7)

In four dimensions the Gauss–Bonnet density is topological. The leading correction can act only through a coupling
that varies, in the theory

S = ∫√(−g) [R/2 − (∇φ)²/2 − V(φ) + f(φ) L_GB].

Here f is any function: exponential for the dilaton, linear for the shift-symmetric case. A constant f does nothing, so
the theory's distinct content needs f′ ≠ 0.

**Field equations (computed, exact).** Varying the action gives the metric equation
G^a\_b + 2 δ^{acde}\_{bghk} (∇\_c ∇^g f) R\_{de}^{hk} = T^a\_b, and the scalar equation □φ − V′ + f′ L_GB = 0. They were
checked against a cosmology's reduced action: the Euler–Lagrange equations in N, a and φ are −a³, −3a² and a³ times the
covariant ones, for every f. Reading the Gauss–Bonnet term's factor 2 as 1 is caught (mutant).

A cosmology is conformally flat, so this check cannot see the Weyl part. The first verification (§13) closed that gap
with a static-spherical reduction (coefficient −8 from both the tt and rr equations) and with the Bianchi identity at
−8, which fails at −4 and −16.

**The principal symbol (computed)** of the coupled system (t, ψ) is gauge invariant and divergence-free. It is
symmetric as an action's must be: the scalar row's coupling to t is −½ the metric row's coupling to ψ. With f′ = 0
every front is null.

**Lemma 7.** Let f′(φ₀) ≠ 0 at a point where V(φ₀) = V′(φ₀) = 0. Then the four-dimensional scalar–Gauss–Bonnet theory
has fronts outside the light cone.

**(a) On gravity's own wave.** A plane gravitational wave (type N, profile diag(1, −1)ε) with φ = φ₀ constant solves the
theory exactly (L_GB = 0 on it) (computed). The purely gravitational polarisation keeps the light cone. The two
graviton–scalar polarisations are characteristic at

ξ₀² = |ξ|²/(1 ∓ 8√2 f′ε),

so one lies outside the light cone for either sign of f′ (computed). The symmetry about the light cone is the symmetry
of ω, equivalently of 1/ξ₀², not of ξ₀² (qualification Q8).

**(b) In a weakly coupled cosmology.** The tensor fronts run at c_T² = (1 + 8f̈)/(1 + 8Hḟ), twice (computed). This is
the null cone of Reall's effective metric Cᵃᵇ = gᵃᵇ − β′ ∇ᵃ∇ᵇΦ − β″ ∇ᵃΦ ∇ᵇΦ (arXiv:2101.11623, eq. (91), p. 18,
READ), here with β = 8f. Two routes give one answer.

At exact solution points (V = 0, linear f, H = 1, φ̇ = ±12/5, f′ = ∓1/480, with the Friedmann equation holding exactly
and 8|Hḟ| = 1/25), c_T² = 537/461 > 1 (computed). The two points are one point under the reflection φ → −φ, f′ → −f′.
The sign of c_T² − 1 = 8(f̈ − Hḟ)/(1 + 8Hḟ) = 76/461 is set by f̈ and ḟ, with 8f̈ = 1363/11525 (computed;
qualification Q6).

**Corroboration (READ).** Serra, Serra, Trincherini and Trombetta (arXiv:2205.08551) treat "a massless (shift-symmetric)
scalar coupled to the Gauss-Bonnet (GB) invariant" (p. 1). The scalar–graviton mixing gives "a non-diagonal transition
amplitude between graviton and scalar, such that one of the propagation eigenmodes travels faster than what is allowed
by the causal structure of the asymptotic spacetime" (§2, p. 2). The delays are ∆t_± = 2r_s(log(b₀/b) ± √2|α̂|/b²)
(eq. (12), p. 5). They find the time advance avoidable only if the effective theory's cutoff obeys |α̂| ≲ log(b₀Λ)/Λ²
(eq. (13)), that is, by new physics at that scale.

**Corollary (under Postulate O).** The four-dimensional scalar–Gauss–Bonnet theory is excluded wherever its
backgrounds have V(φ₀) = V′(φ₀) = 0: every point when V = 0, the shift-symmetric and massless-dilaton cases. This
holds whether its scalar is read as part of gravity or as matter, because matter must keep the cone too (Lemma 1,
Postulate O). Theories built on it keep their own findings as findings about that theory. Nothing about them is
repaired here.

*Not shown.* The case V ≠ 0 at φ₀ (for example V = m²φ²/2 with f = λφ²) is not shown (qualification Q5). Theories with
field equations beyond second order in four dimensions, such as Einsteinian cubic gravity and f(R), lie outside (PL);
their cone tests are not run.

---

## 12 · Where quantum corrections begin (Proposition 8)

Where the classical law stops is not assumed here. Proposition 8 derives it, under named premises.

**The premises**, each named so it can be refused:

- **P1.** The constants of the five-dimensional law are G₅, ħ and c, with a classical Λ₅ = −6/ℓ² and no other scale.
- **P2.** The classical part is Einstein's law, exact at two derivatives (Theorems 1–2). Everything beyond it carries ħ
  and vanishes as ħ → 0.
- **P3 (decoupling).** Where the curvature is far above 1/ℓ², the corrections do not grow with ℓ.
- **P4 (no free number).** No pure number is chosen.

**Proposition 8.** Under P1–P4, classical general relativity holds exactly where x ≪ 1 and fails where x reaches order
one, with x = l₅² √K, l₅³ = G₅ħ/c³, and K the Kretschmann scalar (the curvature's scale). The boundary is x = 1.

*Proof.*

1. **Two groups (computed).** By Buckingham's theorem, the dimension matrix of {G₅, ħ, c, ℓ, R} in (mass, length, time)
   has rank 3. So exactly two independent dimensionless numbers exist: l₅²R and ℓ²R.
2. **Only one carries ħ (computed).** l₅²R carries ħ (as ħ^{2/3}); ℓ²R does not, and it enters only through the
   classical Λ term (P2).
3. **The size of every correction (deduced, with qualification Q2′).** Against the Einstein term, every correction is
   then a function F of x alone, with F(0) = 0 (P2, P3). Taking each term as a positive power of x, a correction is
   small exactly when x is.
4. **The boundary (P4).** With no coefficient chosen, the boundary is x = 1. ∎

*What P4 adds.* The 1. Nature's own order-one factor, the unknown coefficients of the higher-curvature terms, is not
derived here, and none is chosen.

*Four dimensions (computed, this paper).* With {G, ħ, c, R} the matrix again has rank 3, leaving one group,
l_P² R. The same argument puts the boundary at l_P² R = 1.

*What P3 excludes (computed; corrected).* If a term l₅ℓR were admitted, growing with ℓ against P3, it would reach one
at R* = 1/(l₅ℓ). There x = l₅/ℓ, far before x = 1 whenever ℓ ≫ l₅.

The earlier instrument printed (l₅/ℓ)^{1/2} for this value. The second verification refuted that figure: it is
l₅√R*, not x (qualification Q1′). The conclusion holds a fortiori.

*Relation to Haggard and Rovelli's criterion (READ; relation computed, this paper).* Haggard and Rovelli
(arXiv:1407.0989, eqs. (11)–(13), p. 4) argue "on dimensional grounds" that a process of duration τ stays classical
only while q = l_P R τ ≪ 1. They also say: "Since this heuristic argument is not very strong, we leave b undetermined".
Their criterion adds the elapsed time to the local curvature.

Evaluated on the local curvature time τ = R^{−1/2}, it becomes q = (l_P² R)^{1/2}. So their q is small exactly where
the local group is, and the two criteria order the same onset up to an order-one factor. The second verification found
the corresponding factor on a black-hole interior to be x ≈ 31 q² in four dimensions and 34 q² in five (qualification
Q3′). Only x decides at the onset by that argument, not by a comparison of times. Haggard and Rovelli's bounce time
τ ∼ m²/l_P (eq. (2), p. 2, READ) is the long-time effect their q adds. Proposition 8 does not need it.

*What Proposition 8 does not prove.*

- P1–P3 are premises of effective field theory, not theorems.
- "Each term a positive power of x" is an assumption about the expansion's form (Q2′).
- A bound on K is not a bound on every curvature component, because the Lorentzian K is not positive-definite (Q4′).
- Which invariant measures the scale moves the boundary by an order-one factor.

### 12.1 What this says about the relation

Theorems 1–2 and Proposition 8 together give the relation the paper set out to state:

- **Where x ≪ 1:** the law is Einstein's exactly. Its one possible quantum correction at second order is zero, and
  quantum matter and information live inside the one light cone (Lemma 5).
- **Where x → 1:** the classical law stops, and nothing proved here says what replaces it. Postulate O says only that
  whatever replaces it keeps the one cone.

---

## 13 · Verification

The work was verified twice, independently, before this paper. Each verification was done by one verifier working
read-only. The second also re-derived the claims with code that imports nothing from the instruments.

**First verification: Lemmas 6–7 and Theorem 2.** Confirmed, with qualifications; no sub-claim refuted. It
re-derived:

- the Boulware–Deser solution at κ = 1 and 0 (with 2α and −α failing);
- the three cones from the explicit E_ab in a temporal gauge;
- c_T = 3 − 2A, c_V = A and c_S = 2A − 1, with the sum rule;
- the tensor cone by direct linearisation;
- the plane-wave ω against Reall, Tanahashi and Way (4.11)–(4.12);
- the anti-de Sitter wave's ω divided by 1 − 4αk², exactly;
- the scalar–Gauss–Bonnet equations (as in §11);
- c_T² and c_S² on the cosmology, and ω = ±8√2 f′ε analytically on the wave.

It also re-read the quotations of the outside sources. Its qualifications, each carried at its claim above:

- **Q1.** "From relativity alone" means under Postulate O. Theorem 1's cone statement is flat-space only (§9).
- **Q2.** CEMZ constrain α ≫ l_P² only, at tree level (§10.3).
- **Q3.** The divisor of Lemma 6 (d) vanishes at 8αk_CD² = 1. "For either sign" holds within the existence range
  (§10.2).
- **Q4.** The split is proved on the families computed and is generic per RTW, not proved wherever the Weyl curvature
  is nonzero (§10.3).
- **Q5.** Lemma 7 needs V(φ₀) = V′(φ₀) = 0 (§11).
- **Q6.** "Either sign of f′" in cosmology is a reflection; the sign of c_T² − 1 is set by f̈ and ḟ (§11).
- **Q7.** The cosmology check is blind to the Weyl part, and the verifier's own checks close the gap (§11).
- **Q8.** Minor points. Transversality is RTW's §3.1 (not §3.3), and the symmetry in Lemma 7 (a) is ω's.

**Second verification: Proposition 8.** Confirmed, with qualifications; one computed value refuted. It re-derived the rank and null space of Buckingham's matrix and read Haggard and Rovelli in full.
Qualifications carried in §12:

- **Q1′.** The counterfactual onset is x = l₅/ℓ, and the instrument's value was refuted.
- **Q2′.** The form of the expansion is an assumption.
- **Q3′.** Haggard and Rovelli's criterion is q = l_P R τ, and "only x decides" stands by x ∼ 31 q².
- **Q4′.** A bound on K is not a bound on all curvature.

**This paper's own check.** `qr_paper_check.py` imports the instruments by path. It requires each instrument's own
checks to pass, asserts each computed number printed here, and asserts that each printed form appears in this text. Its
five mutants each change one thing:

- `paper_drift` changes one printed number;
- `signal` passes off a non-local gate as local;
- `onset_sqrt` uses the refuted value;
- `sum_weights` miscounts the polarisations;
- `inst_gb_double` runs an instrument with its own mutant.

Each must be caught by the claim it targets. Results are in Appendix C.

**The verification of this paper.** One independent verifier, after the draft and its check pass. Its report is
recorded in Appendix D when it returns.

---

## 14 · Is it a law?

A theorem is true relative to its premises. A physical law is a universal statement that experiment supports and can
refute. This paper's chain has three kinds of links:

- **Exact computations** (Lemmas 2, 6, 7, parts of 1, 3, 5 and 8). They hold unconditionally as mathematics.
- **Outside theorems** (Lovelock, Deser, Peres–Terno), exact on their premises: locality, second order, consistency,
  unitary implementation of the Lorentz group.
- **One universal statement, Postulate O,** and the experiments bounding departures from it to 10⁻¹⁵ (speed and free
  fall) and 10⁻⁶–10⁻⁵ (Shapiro delays).

So the honest answer is this. The statement *everything is relative*, in sense (3), is not proved as a law and cannot
be: no finite set of experiments establishes a universal. It is proved as a theorem in the following form.

> **If** everything that can exist keeps the one light cone, **then**:
>
> - gravity's second-order law is Einstein's exactly in four and five dimensions;
> - its one quantum-correction coupling is zero;
> - its four-dimensional scalar realisation is excluded;
> - quantum information signals nothing outside that cone;
> - the classical law is exact until x = l₅²√K reaches one.

The law-like content is the antecedent. What makes it a candidate for a law is that every experiment quoted bounds a
departure from it and none has found one.

---

## 15 · What is not proved

- Anything beyond the experiments' precision.
- Postulate O. It is assumed, never derived.
- The cone splitting at every point of nonzero Weyl curvature. It is proved on the families computed and generic per
  RTW.
- α = 0 below |α| ∼ l_P5² by scattering alone. Theorem 2 needs Postulate O there.
- The scalar–Gauss–Bonnet exclusion where V(φ₀) ≠ 0 or V′(φ₀) ≠ 0.
- The causal behaviour of theories beyond second order (Einsteinian cubic gravity, f(R)), and of theories with an
  infinite tower of higher spins.
- The form of the correction expansion, nature's order-one factor at x = 1, and what law replaces Einstein's there.
- Any theory of quantum gravity, and any unification. The result is one shared causal structure.

---

## 16 · References

Each was re-read at source for this paper (alphaXiv PDF text, 2026-10-16), with page numbers as printed, except where
marked "named, not re-read".

1. A. Peres and D. R. Terno, *Quantum Information and Relativity Theory*, Rev. Mod. Phys. 76 (2004) 93;
   arXiv:quant-ph/0212023v2. pp. 1, 13 and abstract.
2. LIGO Scientific and Virgo Collaborations, Fermi GBM and INTEGRAL, *Gravitational Waves and Gamma-Rays from a Binary
   Neutron Star Merger: GW170817 and GRB 170817A*, ApJL 848 (2017) L13; arXiv:1710.05834v2. Abstract, eq. (1) p. 6,
   eq. (4) and the Cassini bound p. 7.
3. C. M. Will, *The Confrontation between General Relativity and Experiment*, Living Rev. Rel. 17 (2014) 4;
   arXiv:1403.7377v1. Abstract; §2.1 p. 6; §3.1.1 p. 26.
4. S. Deser, *Self-Interaction and Gauge Invariance*, Gen. Rel. Grav. 1 (1970) 9; arXiv:gr-qc/0411023v3. pp. 1, 4.
5. P. Touboul et al. (MICROSCOPE), *MICROSCOPE mission: final results of the test of the Equivalence Principle*,
   Phys. Rev. Lett. 129 (2022) 121102; arXiv:2209.15487v1. Eq. (5) p. 5.
6. A. Navarro and J. Navarro, *Lovelock's theorem revisited*, J. Geom. Phys. 61 (2011) 1950; arXiv:1005.2386v4.
   Theorem 2.6 p. 9; p. 1. D. Lovelock (1970–72) and C. Lanczos (1938) are named through it, not re-read.
7. C. Charmousis and J.-F. Dufaux, *General Gauss-Bonnet brane cosmology*, Class. Quant. Grav. 19 (2002) 4671;
   arXiv:hep-th/0202107v3. pp. 3, 4, 5, 9, 16. D. G. Boulware and S. Deser (1985) and D. J. Gross and J. H. Sloan
   (1987) are named through it, not re-read.
8. H. S. Reall, N. Tanahashi and B. Way, *Causality and Hyperbolicity of Lovelock Theories*, Class. Quant. Grav. 31
   (2014) 205005; arXiv:1406.3379v2. Abstract; pp. 2, 13, 14, 17, 22, 24–25. R.-G. Cai (2002) is named through it.
9. X. O. Camanho, J. D. Edelstein, J. Maldacena and A. Zhiboedov, *Causality Constraints on Corrections to the Graviton
   Three-Point Coupling*, JHEP 02 (2016) 020; arXiv:1407.5597v1. Abstract; §1 p. 3; §2.4 pp. 12–13; §4.4 p. 33.
10. H. S. Reall, *Causality in gravitational theories with second order equations of motion*, Phys. Rev. D 103 (2021)
    084027; arXiv:2101.11623v2. Abstract; eq. (91) p. 18.
11. F. Serra, J. Serra, E. Trincherini and L. G. Trombetta, *Causality Constraints on Black Holes beyond GR*, JHEP 08
    (2022) 157; arXiv:2205.08551v2. Eq. (1) p. 1; §2 p. 2; eqs. (12)–(13) p. 5.
12. H. M. Haggard and C. Rovelli, *Black hole fireworks: quantum-gravity effects outside the horizon spark black to
    white hole tunneling*, Phys. Rev. D 92 (2015) 104020; arXiv:1407.0989v2. Eq. (2) p. 2; eqs. (11)–(13) p. 4.
13. E. Buckingham, *On physically similar systems*, Phys. Rev. 4 (1914) 345. Named, not re-read; the theorem is used
    in its standard form, and the rank is computed.
14. F. R. Tangherlini (1963), the five-dimensional Schwarzschild metric; Y. Nambu and T. Goto, the area action; the
    Lorentz transformation (Lorentz, Poincaré, Einstein). Standard, named, not re-read.

Journal references are given as commonly cited and were not re-read; the arXiv versions above are the texts read.

---

## Appendix A · Every computation, with its instrument and check

The computation modules are imported by path by `qr_paper_check.py`; each also runs on its own.

| claim | where | instrument · entry | check |
|---|---|---|---|
| `E^2 = p^2 c^2 + m^2 c^4`, E = pc at m = 0 | §4 | relativity.py U1 | L1 |
| boost invariants of every kind | §5 | relativity.py U2 | L2 |
| geodesics independent of m; bending 1.751 arcsec | §6 | relativity.py U3 | L3 ×2 |
| p = ⌊(n − 1)/2⌋: p(4) = 1, p(5) = 2 | §7 | relativity.py U4 | L4 |
| ρ_B is unchanged under any local operation of Alice | §8 | this paper | L5 |
| Einstein's law: every characteristic front is null | §10 | gb_cone.py C2 | L6 |
| three cones on a static background | §10 | gb_cone.py C3 | L6 |
| c_T = 3 − 2A, c_V = A, c_S = 2A − 1; sum rule; excess 16\|α\|m/(r⁴q²) | §10 | gb_cone.py C4 + this paper | L6 ×2 |
| ω = 8αε, 4αε, −8αε; sum zero; ÷ (1 − 4αk²) on anti-de Sitter | §10 | gb_cone.py C5, C10 | L6 ×2 |
| sGB field equations, symbol | §11 | sgb_cone.py S1–S2 | I3 |
| (1 + 8f̈)/(1 + 8Hḟ), Reall's (91) | §11 | sgb_cone.py S3 | L7 |
| 537/461; 8\|Hḟ\| = 1/25; 76/461; 1363/11525 | §11 | sgb_cone.py S3 + this paper | L7 ×2 |
| \|ξ\|²/(1 ∓ 8√2 f′ε) | §11 | sgb_cone.py S4 | L7 |
| rank 3, two groups; ħ^{2/3} in l₅²R only | §12 | quantum_onset.py Q1–Q2 | Q1, I4 |
| four dimensions: one group l_P² R | §12 | this paper | Q1 |
| x = l₅/ℓ at the counterfactual onset (corrected) | §12 | this paper | Q6 |
| q = (l_P² R)^{1/2} at τ = R^{−1/2} | §12 | this paper | HR |

Instrument suites, re-run for this paper (Appendix C):

- relativity.py: 6/6 selftest, 4/4 mutants;
- gb_cone.py: 10/10, 5/5;
- sgb_cone.py: 7/7, 3/3;
- quantum_onset.py: 5/5, 3/3.

---

## Appendix B · Source map

| claim | rests on |
|---|---|
| Lemma 1 | computed (L1); READ Peres–Terno pp. 1, 13 |
| Lemma 2 | computed (L2); READ GW170817 eq. (1), Will abstract |
| Lemma 3 | READ Will p. 6, Deser pp. 1, 4; computed (L3); READ MICROSCOPE eq. (5), GW170817 eq. (4) and p. 7 |
| Lemma 4 | READ Navarro–Navarro Thm 2.6, p. 1; computed count (L4); READ Charmousis–Dufaux pp. 3, 5, 16 |
| Lemma 5 | READ Peres–Terno p. 13; computed (L5) |
| Theorem 1 | deduced from Lemmas 1–5; qualification Q1 |
| Lemma 6 | computed (L6, gb_cone.py); READ RTW pp. 2, 13, 14, 17, 22, 24–25 |
| Theorem 2 | deduced from Lemma 6 + Postulate O + (PL); corroborated, READ CEMZ, within Q2 |
| Lemma 7 | computed (L7, sgb_cone.py); READ Reall eq. (91), SSTT eqs. (1), (12)–(13); Q5–Q8 |
| Proposition 8 | computed (Q1, Q6, HR); premises P1–P4; READ Haggard–Rovelli eqs. (2), (11)–(13); Q1′–Q4′ |
| §13 | the two independent verifications |

---

## Appendix C · Reproduction and md5

From `research/…/paper/`:

```
pip install sympy z3-solver           # sympy 1.14.0 used
export PYTHONDONTWRITEBYTECODE=1
python3 qr_paper_check.py --selftest
python3 qr_paper_check.py --mutants
for f in relativity gb_cone sgb_cone quantum_onset; do
  python3 ../$f.py --selftest; python3 ../$f.py --mutants; done
```

Files relied on, md5 at the start of the work (unchanged at its end; see the closing run):

| file | md5 |
|---|---|
| relativity.py | c2727eda529fb97c6086e460a64ceab9 |
| gb_cone.py | 6a6da20ca31f91b6a459c44a7e731792 |
| sgb_cone.py | bd787b985e6cad05587f39a2a2b8816b |
| quantum_onset.py | 6d00f28026d4dfe606515c1532deea76 |

The check's run is recorded below.

RUN-RECORD

---

## Appendix D · The verification of this paper

VERIFIER-RECORD
