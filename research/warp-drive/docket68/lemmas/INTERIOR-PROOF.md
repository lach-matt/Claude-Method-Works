# The large end's interior: the proof of (a)-(d), scoped (item 414)

*First headed* 2026-10-14, on M's item 414: "Proof first , then the computation. But before you start the computation,
let's discuss the approach as to not spend days failing." This file is the proof's plan. It says what follows from
known theorems, what needs a derivation of the board's own, and where the hard core is, so that no step is started
that cannot close. Labels: M's (a ruling), READ (quoted from a source read), deduced, computed, estimate. Nothing here
is proved yet; each proposition carries its status.

## What is to be proved

The requirements are INTERIOR-REQUIRED (a)-(d), for the large hole's five-dimensional interior D: inside the event
horizon, from where the 4D stretch ends (curvature radius ell, R_5 = 12^(1/6) (r0 ell^2)^(1/3)) to 273's quantum region.

**Hypotheses (H).**
1. Einstein's law in the bulk, R_ab = -(4/ell^2) g_ab, vacuum (324-328; 320's bulk content at its own order).
2. The plane at sigma > 0, a boundary of the bulk carrying Israel's condition.
3. Static: a hypersurface-orthogonal Killing field xi (the record's ansatz has no cross term with tau).
4. SO(3)-symmetric about the axis.
5. Classical GR holds in D (273: given up only inside the quantum region).

## The propositions, and how each is reached

**(a) A forward clock with its rate bounded below.** Status: **reduces to (b)** (deduced from standard results, which
are cited but not yet re-read: Bernal and Sanchez's smooth Cauchy temporal functions; non-imprisonment in strongly
causal spacetimes).
- If D has no Cauchy horizon (b), D is globally hyperbolic up to 273's region. It then carries a smooth temporal
  function: a clock whose gradient is timelike everywhere, so it is strictly monotone along every causal path.
- The rate: modulo the static time, which every quantity ignores, D's quotient is compact (s between two finite
  values, x in [0, 1], the sphere). A continuous positive function on a compact set has a positive minimum, so the
  clock's rate is bounded below away from our face. Along timelike paths, proper time is then at most (clock range) /
  (least rate).
- Null paths cannot be imprisoned in a compact set of a globally hyperbolic region, so each leaves it, and reaches 273's
  region in finite affine parameter.

**(b) No inner horizon.** Static (t-homogeneous) data develop t-invariantly, so an inner (Cauchy) horizon of D is
t-invariant. In this setting it comes in two kinds:
- **(b1) A Killing inner horizon**, where the static field xi turns null again (g_tt = 0 inside). Status: **to be
  derived, route known.** The published no-inner-horizon theorems forbid it for static black holes. READ, Cai, Li and
  Yang, arXiv:2009.05520 (JHEP 03 (2021) 263): "We are interested in static charged black holes that are homogeneous and
  isotropic". That is, the metric depends on one radial coordinate, and their identity is the radial conservation law.
  Ours depends on two (s, x). The coordinate-free form of that law is a Komar identity, integrating the divergence of
  nabla^a xi^b over a region between two horizons. With a vacuum bulk at Lambda < 0 its volume term has one sign, and an
  inner horizon needs a term of the other sign (charge does that for Reissner-Nordstrom). Two things are new and must
  be derived: the brane's boundary term (sigma > 0 is expected to give it a sign), and a region between the horizons in
  two coordinates. Controls, before it is believed: Reissner-Nordstrom-AdS must keep its inner horizon, and
  Schwarzschild-AdS and Schwarzschild-de Sitter must come out right.
- **(b2) A non-Killing inner horizon.** In two coordinates there is a second kind, which one coordinate cannot have: a
  null curve in the (s, x) plane, swept along the static time and the sphere, ending the development at some x before
  others. Status: **open; no theorem known to the board.** It would appear exactly where the clock fails, where N^2 =
  -g_ss + g_sx^2/g_xx reaches zero or blows up before 273's region. So (b2) and (a)'s quantitative form are one
  statement, and proving it needs a priori bounds on the 2D PDE system. That is the hard core.

**(c) Curvature finite to 273's region.**
- **(c1)** If 273's region is the set where curvature reaches the bulk's Planck value, curvature is below that value in
  D by definition, and the development's only other ending, a Cauchy horizon, is excluded by (b). Status:
  **definitional, given (b)** (deduced), once 273's boundary is fixed as that set. That definition is M's to confirm.
- **(c2)** That the Planck set is reached at the centre, after the README, and nowhere off the shell earlier. Status:
  **open as a theorem**: a statement about the solution, not about definitions. Measurable: curvature's growth per
  Zeno halving (5D Kasner predicts 2^8 per halving; the 4D stretch's 2^6 is exact, item 392).

**(d) Position 2's side**, with its own r_s2 and sigma2: the time reverse of (a)-(c). Status: **follows by time
reversal** (deduced), with the same open core.

## What this means

The proof can close **(a) given (b)**, **(b1)** if the Komar identity's signs hold with the brane, **(c1)** by definition
and **(d)** by reversal. It leaves a sharp core: **(b2) and (c2)**. In plain words: that the clock N^2 stays positive
and finite, and that curvature reaches the Planck value first at the centre, all the way to 273's region.

That core is exactly what the computation measures, cell by cell, with the criterion derived at 405-3: E = 0 with
every error counted. So the computation is not asked to establish everything. It is asked only the two questions the
proof cannot answer, and its approach is put to M before it runs (414).

## Steps, each reported as it closes

- **P2.** Derive the Komar identity for the static 5D brane interior, between the event horizon and a putative inner
  Killing horizon, with the brane's term. Check its signs, and run the three controls. Outcome: (b1) proved, or a class
  of counterexamples named. Conversation and sympy.
- **P3.** Try to reduce (b2) to (a): a non-Killing inner horizon forces N^2 to zero or infinity at some x first. If no
  proof closes, state the open core exactly, with what the computation must show.
- **P4.** (c1) written exactly, with 273's boundary as M confirms it; (c2) stated with its measure.
- **P5.** The proven parts machine-checked (sympy, and Z3 where finite), seated as a lemma with selftest and mutants.
