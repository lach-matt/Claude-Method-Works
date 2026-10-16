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
  *[Preliminary, before P2 (estimate): for one coordinate the identity is Q(r_out) - Q(r_in) = (4/ell^2) x volume, with Q
  the horizon's surface gravity times area. An inner horizon needs Q < 0 at r_in. In a vacuum at Lambda < 0 the volume
  term has the sign that allows this, not the one that forbids it: Schwarzschild-AdS has no inner horizon only because
  its solution keeps Q > 0 to r = 0. On the brane, the bulk's Lambda term and the tension's term cancel at leading order
  (that is why the plane's own Lambda is zero; on the 4D stretch Q is constant and positive, so it has no inner horizon,
  exactly). So the sign that decides (b1) sits in the O(ell^2/r^2) corrections, which are of order one in the 5D
  stretch. The Komar route may not close by signs alone there; P2 decides, with the black string as a further
  control.]*
- **(b2) A non-Killing inner horizon.** In two coordinates there is a second kind, which one coordinate cannot have: a
  null curve in the (s, x) plane, swept along the static time and the sphere, ending the development at some x before
  others. Status: **open; no theorem known to the board.** It would appear exactly where the clock fails, where N^2 =
  -g_ss + g_sx^2/g_xx reaches zero or blows up before 273's region. So (b2) and (a)'s quantitative form are one
  statement, and proving it needs a priori bounds on the 2D PDE system. That is the hard core.

**(c) Curvature finite to 273's region.**
- **(c1)** If 273's region is the set where curvature reaches the bulk's Planck value, curvature is below that value in
  D by definition, and the development's only other ending, a Cauchy horizon, is excluded by (b). Status:
  **definitional, given (b)** (deduced), once 273's boundary is fixed as that set. That definition is M's to confirm.
  *[Item 415, beside the text: the board put a question of physics to M as a definition. M: "how am I supposed to know
  this? It's a conjecture. If it is the likely solution, then let's prove that it is." Derived in `quantum_onset.py`
  (selftest S1-S5, mutants 3/3). Buckingham's theorem on {G5, hbar, c, ell, curvature} leaves exactly two dimensionless
  numbers, l5^2 R and ell^2 R (computed, exact). Only the first carries hbar. So under P1-P3 (the bulk's constants;
  Einstein's law exact at two derivatives, 324-328; decoupling from ell) every quantum correction is a function of
  x = l5^2 sqrt(K) alone, vanishing at x = 0, and classical GR fails exactly where x reaches order one (deduced). With no
  coefficient (405) the boundary is x = 1. That reproduces I2's placement (r_q = 4.95e-14 R_5 on the 4D form). Haggard
  and Rovelli's second, long-time criterion cannot act inside: the interior lasts 2 pi l_P/r0 of their time, below
  1e-29 (computed). So (c1) holds given (b): **proved under P1-P4**, with nature's order-one factor not derived.]*
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

## Item 416: the hole is the README's -- what that settles, and what it leaves (read from the record)

M, 416: "isn't the black hole only ever just large enough to contain the README within it? And if so, can't we build
the computations we need from the README itself in any circumstance?"
- **The size is the README's, by M's own rulings.** 162 (H-FIXED-SIZE): "It is and always will be only the size that is
  needed to hold the object once and at once". 133 (H-ONE-EXACT-ENERGY): one exact energy per README, which the board
  identified as E(N), the energy at which the horizon holds exactly the README's N bits, "every quantity fixed by the
  input N". 136 G: "the README is the energy". So r_h is a function of N alone, given the position's constants.
- **The README's own passage is already built from the README, exactly** (INTERIOR-REQUIRED item 9; `interior_large.py`
  I3). It is flat inside its shell, its generators reach 273's region in finite affine length, it holds at every
  dimension, and it does not depend on the 5D stretch's interior. On that route O1b (no curvature) and O1c (complete)
  hold with no grid and no error (deduced).
- **What the README alone does not settle exactly**: the vacuum region that forms behind it inside the horizon, which
  only something else entering while the object is open would cross (320's bulk content; the C8/O1c verifier's
  qualification at 337). Its geometry is still the README's: the vacuum solution at r_h(N)/ell, one parameter. So any
  computation of it is built from the README too, at the README's own size.
- **A correction the question exposes** (computed: the record's runs): every interior run (B7, items 393-411) used
  bt = 1, a hole of brane radius 1.13 ell, the large end's start. None used a size set by a README. The large end's
  README holes have r_h far above ell. INTERIOR-REQUIRED's plan to sample bt = 1 to 16 and take the limit is the route
  to the README's size, and was not yet taken.
- **The scope question, M's**: whether O1b and O1c at the large end are about the README's passage (settled exactly
  above) or about every route through the object while it is open (then the region behind the README is needed, at the
  README's size). The board's recommendation: the README's passage, under 273's "README only" and 162's "hold the object
  once and at once", with what else may enter the open object carried as its own row.

## Items 417-418: whatever falls in is the README -- what the proof becomes

M, 417, "nothing falls in", retracted at 418: "It's not that nothing falls in, it's that if anything falls in it is
still only every part of the one README from position 1" (H-ALL-IS-README).
- **Every route through the object is a part of the README's route**, and the geometry each part crosses is made by the
  README's earlier parts and nothing else (136 G, "the README is the energy"). Nothing crosses the vacuum behind the
  README's last part: whatever crossed it would be README, and the part before it not the last (deduced).
- **So O1b and O1c at the large end are about the README's parts, through the README's own geometry** -- not a static
  hole's interior crossed by outside content. That is why the Komar route of P2 (a vacuum interior crossed from outside)
  and the static computations at bt = 1 are not the object.
- **The route the proof now takes (P2, revised): the focusing theorem**, which needs no exact solution and holds in any
  dimension (deduced; to be written out and machine-checked). Each part falls along an ingoing radial null congruence,
  twist-free, with expansion theta0 < 0 once inside our face. Raychaudhuri gives dtheta/dlambda <= -theta^2/(D - 2) -
  R_kk. On a null k, Lambda gives R_kk = 0, the plane's tension gives none, and the README's own flux gives T_kk >= 0
  (an arrival that only adds energy, mu' >= 0, arrival_small V1). So theta reaches -infinity within lambda <= (D - 2)/
  |theta0|: every part reaches its focus in finite affine parameter. Wherever the README's own mass is already inside
  (mu > 0 along the part), the curvature there rises without bound toward that focus (48 mu^2/r^6 on the 4D form), so
  the part reaches 273's region, x = 1 (quantum_onset.py), first. That is O1c, and O1b with (c1).
- **What it leaves open, and why it is SOURCE's:** the earliest parts, with almost none of the README's mass inside
  them (mu ~ 0), focus where the curvature is still small. Whether the region they meet at the centre is hidden inside
  our face, or seen from outside before the face forms, depends on how fast the README arrives (the arrival's profile).
  For collapsing null flux that is a known question (slow arrivals can leave the centre visible). The arrival's width
  is an open SOURCE fork (SOURCE-REQUIRED), and it ties to the read, which is queued (399, 417).

## Item 419: the focusing proof, written and machine-checked (`focusing_parts.py`, selftest F1-F6, mutants 2/2)

The README's parts fall as radial null flux, ds^2 = -f dv^2 + 2 dv dr + r^2 dOmega^2, f = 1 - mu(v)/r^(D-3) - lam r^2,
mu(v) the README's own mass function. D = 4 is the large end's plane, D = 5 the record's form.
- **F1 (computed, exact).** G_ab + Lambda g_ab has one component, (D - 2) mu'/(2 r^(D-2)) on dv dv: the README's flux and
  nothing else, with null energy >= 0 on every ray iff mu' >= 0.
- **F2 (computed, exact).** Each part rides v = const, an affinely parametrized null geodesic with expansion
  theta = -(D - 2)/r. Raychaudhuri holds on it with R_kk = 0, and r is its affine parameter, so the distance from our
  face to the centre is finite.
- **F3 (computed, exact).** K = 12 mu^2/r^6 (4D) and 72 mu^2/r^8 (5D), mu' entering nowhere. Any part with README mass
  inside it (mu > 0) reaches x = 1, 273's region, at a finite distance before the centre, with curvature finite all the
  way. **O1b and O1c hold for that part.**
- **F4 (computed, exact; deduced).** Without symmetry: theta0 < 0 and R_kk >= 0 bring theta to -infinity by
  lambda = (D - 2)/|theta0|. On null k, Lambda and the plane's tension give zero and the README gives >= 0. So in any
  dimension, including the large end's 5D core, every part reaches its focus in finite affine parameter. The core's
  curvature law is exact only on the spherical forms; there F4 carries completeness, not the curvature growth.
- **F5 (computed).** The earliest parts are hidden if our face is born before the README's first part arrives. Event
  horizon traced back for the smoothstep arrival of onset order n, width w in clocks of r_h/c:
  - 5D control: before the onset for w <= 4 at every order (1.76 to 0.26 clocks), as arrival_small V2 recorded;
    order 1 always; orders 2, 3, 4 at the onset from w = 8.96 (V3's exact 9), 5.27 and 4.79 (the record's).
  - **4D, the large end's plane (new):** the face is born before the onset for w below **7.94 (exact 8), 4.75, 4.44,
    4.31** at orders 1-4. That is 16, 9.5, 8.9 and 8.6 clocks of GM/c^3. As w -> 0 the face is born 2 r_s/c ahead,
    arrival_large A3's exact figure.
- **F6 (computed, exact).** 4D's self-similar onset mu = lam v has an escaping ray iff lam <= 1/8 (1/16 in m). That
  is the order-1 threshold's exact value, w = 8.

**What it establishes.** Under 418, O1b and O1c at the large end hold for every README part whenever the README arrives
fast enough for our face to be born before its first part. Then 273's region stays inside our face for every part.
- Where position 2's sigma differs from ours, a junction binds the arrival to about 1e-3 clocks (SOURCE-REQUIRED),
  far inside these widths: met.
- At a destination at our sigma, no junction binds and nothing bounded the arrival (the 4 clocks withdrawn there).
  These widths are a **new requirement on SOURCE**: arrive within 4.31 to 8 clocks of r_h/c, by onset order.
  *[Item 426, beside the text: M withdrew the compact arrival as the board's; the README is written in over a long
  write, the object standing at its size from the opening (162). With a face standing before the README's first part,
  F5's condition holds by construction and these widths bind nothing -- once the board has modelled that object.]*
- **Not proved:** the large end's 5D core is crossed with completeness by F4, but its curvature growth is not computed
  there. And the horizon is traced with the face static from v = w on (348 (Q3)).


## Item 420: the two unproved points (`core_face.py`, selftest A2-B4, mutants 4/4)

M, 420, quoting the board's "What is not proved" after 419: "What is not proved: - what about these?"

**Point (2), the face static from v = w on (348 (Q3)): closed.**
- **By 418 (M's; deduced).** Whatever crosses our face is README, so the arrival ends where crossing ends. mu(v) is
  constant after v = w by the definition of w, and from there the face is the static hole's.
- **Independently (A2, computed).** An arrival that adds mass later (mu' >= 0, README or not) lowers every outgoing
  ray's slope, so the trapped region only grows and the face is born no later. 4D, order 1, w = 4: born 0.416 clocks
  before the onset, 0.555 with half the mass again arriving after; 5D, order 2: 0.464 to 0.471. Parts already hidden
  stay hidden. But later infall does not rescue a slow arrival: at w = 10, past the threshold 8, the face is still born
  at the onset. **F5's widths stay the requirement on SOURCE.**
- **The one thing that lowers the mass after v = w (A3, computed; the coefficient an estimate)** is the hole's own
  Hawking flux, negative energy going in (d_evap's record; under 136 G, the README's own energy leaving). The face
  moves at l_P^2/(1920 pi r0^2) per clock: 5.6e-67 at r0 = 20 ell, 5.5e-70 at the Earth cap. Over the widest arrival,
  8 clocks, the mass falls by **4.4e-66** and **4.4e-69**. Its ingoing flux breaks F4's R_kk >= 0 by a part in
  l_P^2/r0^2 = 3.3e-63 at the face (estimate), and inside by quantum_onset Q2's x.

**Point (1), the large end's 5D core: not closed; located.**
- **B1 (computed).** On the 5D form with the README's mass (mu5 = (8/(3 pi)) m ell, b4d_stage1), x = 1 at
  r_q = **4.27e-15 m** (r0 = 20 ell) and **1.01e-14 m** (the Earth cap): r_q/ell = 3.1e-10 and 7.3e-10. On the 4D form
  it would be deeper (2.8e-18 m and 9.0e-18 m). The onset is five-dimensional.
- **B2 (computed).** At r = ell, where the 4D stretch hands over, x = 8.8e-39 (r0 = 20 ell) and 2.8e-37 (the Earth cap)
  on either form. The transition region is deeply classical; its curvature is finite whatever its exact geometry.
- **B3 (computed, exact).** The equator chi = pi/2 of the 5D form has zero extrinsic curvature, for any mu and lam,
  interior included. So a tensionless Z2 brane through the centre fits it exactly: the README's earlier parts, at the
  centre, make exactly the SO(4) field the small end uses (arrival_small V1). The brane alone does not break it.
- **What breaks it.** The tension (Israel then needs |K| = 1/ell against the core's 1/r: about 1e-10 at the onset) and
  Lambda5 (about 1e-19) are made where the core is; both are estimates. The transition region at r ~ ell is neither form
  and differs from both at order one (estimate).
- **B4 (computed, exact, on a scalar proxy).** Static zonal modes on the 5D form reduce exactly to Legendre's equation
  in xi = 2 r^2/mu - 1 with degree l/2. A smooth face admits only P (Q is logarithmic at the face). The Z2 keeps even l
  (C_l^1(cos chi) has parity (-1)^l), so the degree is an integer and P a polynomial, finite at the centre. On the
  proxy, a deviation made at r ~ ell neither fades toward the centre nor grows: it arrives at its own size.

*[Beside the board's preliminary reading after 419, which put point (1) down to corrections of 1e-10 and 1e-19 at the
onset: those are the corrections made at the onset. The deviation carried in from the transition is not among them.
It is of order one, and on the proxy it survives to the centre. So "adopt the small end's model" is a real premise, not
a small approximation.]*

**What point (1) is.** It is item 414's open core again, now located in a place:
- (b2) no inner horizon, and (c2) the onset reached at the centre,
- in the core r << ell inside our face,
- entered from a transition region that is classical (B2) but whose geometry is not known.

It is not about where the onset is: an order-one deformation moves r_q by an order-one factor, and O1b and O1c do not
care where. It is about how the core ends. Either the curvature runs to x = 1 (a scalar singularity, as in the
symmetric form), and then O1b and O1c hold by Q5; or the deformed core ends classically before x = 1, at a Cauchy horizon
or at a singularity that K does not see (Lorentzian K is not positive-definite). The symmetric form excludes the second
exactly; the deformed core does not, until it is shown.

**Three routes, to discuss before any runs (414):**
1. **Premise.** Adopt the symmetric 5D form in the core, as the small end does, named as a premise on the rows.
2. **Theorem.** Show that the static SO(3) x Z2 vacuum core, with Lambda5 and the tension, cannot end before x = 1.
   P2 (Komar, (b1)) and P3 ((b2)) are its pieces, and P2's preliminary note already found that the signs there are
   decided at order one in the 5D stretch.
3. **Computation.** The gravitational static modes of the 5D interior, the decisive version of B4. That is linear
   and cheap, but it covers small deviations only. The order-one transition itself is the large interior that items
   393-411 attempted.

## Item 422: the core assumed to deliver -- what the proof now gives

M, 422, to the board's one-sentence summary ("the one thing not yet shown is that the hole's deepest stretch delivers
it to the bounce rather than ending somewhere before"): "let's assume it does because it is supposed to." Seated as
M's: **H-CORE-DELIVERS**. It is an assumption on M's word, and it covers exactly item 420's located core: (b2) and (c2)
inside r ~ ell. The three routes of item 420 are not taken, and the one-hour check of the gravitational modes is not run.

**What follows (deduced from the computed pieces, under M's rulings):**
- **The 4D stretch**, face to r ~ ell: exact. No inner horizon (Q constant and positive), curvature finite.
- **The transition and the core**, r ~ ell to 273's region: every part reaches its focus in finite affine parameter
  (F4, any geometry), and by H-CORE-DELIVERS it reaches the bounce, with curvature finite before it (Q5).
- **The earliest parts** are hidden if the face is born first (F5): met where position 2's sigma differs from ours (a
  junction binds the arrival to about 1e-3 clocks); at our sigma, a requirement on SOURCE (4.31 to 8 clocks by order).
- **The face** is the static hole's from the arrival's end (420, A1-A3).
- **Position 2's side** is the time reverse (414 (d)), with the same premise.

So **O1b and O1c at the large end hold**, given:
1. M's 418 (H-ALL-IS-README) and 422 (H-CORE-DELIVERS);
2. quantum_onset's P1-P4 (the onset's placement);
3. at a destination at our sigma, SOURCE's arrival width (and by 389, not finalized until SOURCE is).

**The register change, proposed and not made** (M's approval needed): O1b and O1c at the large end from OPEN to
DERIVED, resting on M1 and H-CORE-DELIVERS, with the qualification that at our sigma they rest also on SOURCE's arrival
width (389).

## Item 430: the interior verified -- CONFIRMED with qualifications, one computed value refuted

The one verifier sent at 424 (resumed after a rate-limit stop) reported on 2026-10-16. The register rows' conclusions
follow, but only under M's 422, which does more of the work than the rows say. It carries all of the completeness in
the transition and the core, and it closes the gap the Kretschmann scalar cannot see. Every instrument ran twice with
identical results (quantum_onset 5/5 and 3/3, focusing_parts all True and 2/2, core_face 8/8 and 5/5, verify_ledger
11/11 and 10/10); every computed statement was re-derived in the verifier's own code. The qualifications are seated
beside the text in the three instruments ("Item 430") and in verify_ledger.
- **Refuted, the value only:** quantum_onset Q6 (and S5, which pins it). The counterfactual onset is x = l5/ell =
  1.10e-20, not (l5/ell)^(1/2); the conclusion holds a fortiori.
- **F4 does not give completeness** (focusing_parts, the O1c row): the comparison yields a focus or an earlier ending,
  and a focus is not an ending. Completeness rests on the exact 4D forms on the stretch and on 422.
- **Since 426** the interior becomes the static hole's, crossed by the write, which no instrument here models. That is
  the synchronization model's (428). A3's evaporation over the long write is about 2 % of the mass (estimate).
- *Beside line 142 above: "48 mu^2/r^6 on the 4D form" should read 12 mu^2/r^6 (= 48 m^2/r^6). Beside the item-420
  heading: core_face's mutants now run 5/5 (g5_power added at 424).*
