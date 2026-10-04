# DOCKET 68 — information without transit (CHARTER, NOT YET OPENED)

**Status: chartered 2026-10-02, to open when DOCKET 67 closes** (M: "Open after D67"). Order: D67 → D68 → D66 →
Step 1b → Step 1c. Nothing here is seated. The three scripts beside this file are pre-docket computations, kept so
every number below is owned.

## M's words, verbatim

> Maybe we just aren't advanced enough yet in out understanding of physics. What if information is faster than
> light, not because us moves faster, but because is already exists everywhere? We don't need to produce
> exotic/immense energy or move faster than light, we need to understand how information moves throughout
> spacetime without any geometric values

Replying to the three routes put to M:

> I varied Alice's measurement angle across seven settings: - test the 12 fields in the 12 vertex trajectory model
> of the warp device idea...
> Spacetime comes from information. - let's assume this is correct
> Quantum mechanics is slightly non-linear. - quantum easing/quantum settling
> A preferred frame - maybe messages can travel into the past, it seems impossible because our lack of
> understanding about cosmic information

M's answers to the follow-up questions (2026-10-02):

- the 12-vertex trajectory model is **the 12-vector** of `multiverse_12_vector_taxonomy_v2.pdf` (Drive, Warp
  folder): V = [M, R, K, T, CP, α_s, Z0, Λ, G, G_F, G_θ, v];
- quantum easing / quantum settling is **deterministic drift**: the state's own value steers its evolution,
  smoothly and the same every time;
- the docket opens **after D67**.

## Standing instruction from M: test in combination, verbatim (2026-10-02)

> Remember that some of the hypothesies lined up for docket 68 may turn out, after initial testing, to work better
> in combination.

**How the docket runs because of it.**
1. **Each hypothesis is tested alone first** -- H-IT, H-SETTLE, H-FRAME, H-12, H-INFO, H-ZERO, H-NULL, with the two
   readings R-INDEX and R-QUANTUM -- and graded on what it does alone: not only pass/fail, but which obstruction it
   removes and which it leaves (the two classical bits; making the corridor; holding it open; the matter at the
   destination; time loops).
2. **A failure alone does not retire a hypothesis.** It is retired only if it also fails in every combination
   tested; a partial result is kept with the obstruction it leaves named.
3. **Combinations are screened, then tested.** Seven hypotheses give 127 non-empty combinations. Each is first
   screened for consistency against what the board holds (a z3 pass, with the vacuity guards PROOF-ASSISTANT.md
   requires), so contradictory combinations are named, not silently skipped. Then combinations are tested where
   one member removes an obstruction another leaves -- complementary obstructions, not every subset.
4. **Pairings the record already shows:** H-ZERO with H-IT (emergent gravity makes the zero of energy free --
   Padmanabhan & Padmanabhan pp. 6-7); H-FRAME with curvature (an expanding universe admits only equal-cosmic-time
   identifications -- frw_frame.py); H-NULL with H-INFO (the QNEC prices a throat's null deficit in bits --
   nullinfo.py); H-SETTLE with H-12 (a parameter whose value drifts with the state is a channel -- nlcontrol.py);
   H-IT with Laughlin & Pines (a protected low-energy law hides the layer beneath it until protection is escaped).
5. **No coverage is capped silently**: every combination not tested is listed with the reason.

## M on the null condition, verbatim (2026-10-02)

> Null (NEC) is a containment. This is where information lives, and is quantifiable

Carried as **H-NULL**. Two results the board audited tie null surfaces to information, both READ (D67: NARROWED):
- Bousso's covariant entropy bound (hep-th/9905177 pp. 9-10): the entropy on a light-sheet -- a NULL hypersurface
  of non-positive expansion bounded by a surface B -- is at most A(B)/4 in Planck units; "we must use null
  hypersurfaces" (the spacelike version fails). Computed: 1.3807e69 bits per square metre of B. Conjectured, not
  derived ("no fundamental derivation"), never seen exceeded; hypotheses include Einstein's equation and an energy
  condition.
- The QNEC (Bousso-Fisher-Leichenauer-Wall 1509.02542): <T_kk> >= (hbar/2 pi) S''_out/A -- null energy is bounded
  below by the curvature of entanglement entropy along a null deformation. Where null energy goes negative,
  information must curve.
Computed in `nullinfo.py` (sympy, exact): IF the QNEC applied at a Morris-Thorne throat, the throat's null deficit
would require S''_out/A <= -(1 - b'(r0))/(4 l_P^2 r0^2) -- the light-sheet density 1/(4 l_P^2) itself, divided by
r0^2: -1.3807e69 bits per m^2 per m^2 at r0 = 1 m, b'(r0) = 0. The corridor's cost then has a price in bits, which
is H-INFO's claim in a form a computation can test. NAMED LIMIT: the QNEC is proven only on stationary null surfaces
of fixed backgrounds without dynamical gravity, with vanishing expansion and shear at the point; a throat has
dynamical gravity, so this is the QNEC carried outside its proven scope -- a hypothesis, not a result.

## M's redefinition of zero, verbatim (2026-10-02)

> What if we redefine 0. Consider 0 to me a point of ground state, and anything less that 0 is not negative, just
> less than the ground state

Carried as **H-ZERO**. Read against the board:
- It is already the convention for local "negative energy": Kuo & Ford's <:T00:> is normal-ordered, i.e. measured
  from the Minkowski vacuum (the field's ground state), and the Casimir density is "below the vacuum". What is
  called negative is "less than the ground state" in exactly M's sense.
- Computed in `zero.py` (sympy, arbitrary T_ab, every null and boosted timelike direction): moving the zero of
  energy everywhere (T_ab -> T_ab + lambda g_ab) changes the WEC density by -lambda and the SEC combination by
  +lambda, and changes the NEC combination T_ab k^a k^b by EXACTLY 0, because g_ab k^a k^b = 0 for null k. The
  Morris-Thorne throat's rho + p_r = (r b' - b)/(8 pi r^3) is unchanged. So H-ZERO can relabel a WEC violation away;
  it cannot relabel the throat's NEC violation, which depends on the shape b(r), not on where zero sits.
- In general relativity moving the zero is not free: it is adding a cosmological constant, which gravitates.
  Padmanabhan & Padmanabhan (1703.06144, pp. 6-7, READ) name the paradigm in which it IS free -- emergent gravity,
  where the field equations are invariant under adding a constant to the matter Lagrangian and Lambda is an
  integration constant. H-ZERO is a statement about that paradigm, and belongs beside H-IT.

## Sources M placed in the Warp folder for this docket (2026-10-02)

M placed two papers as Adobe Acrobat share links (Drive text stubs 1Wb1XRsa2cWPebP04v66Yyr1cXyDUbx7-,
182FXTvfP3b2S_BuxE0N8mhHSHq8U1P9e). acrobat.adobe.com is refused by the egress proxy (reported, not routed around).

**1. Padmanabhan & Padmanabhan, "Cosmic Information, the Cosmological Constant and the Amplitude of primordial
perturbations", arXiv:1703.06144v1 (17 Mar 2017) -- READ at source (alphaXiv), pp. 1-9; per M-D67-2 the arXiv
version is the object.** CosmIn is N(a2, a1) = (2/3 pi) ln(h1/h2), the number of modes (counted by
d^3x d^3k/(2 pi)^3) that cross the Hubble radius (eq. 1). Its finiteness forces late-time acceleration. The single
postulate N(a_Lambda, a_QG) = 4 pi, with matter + radiation + Lambda and a pre-geometric -> classical transition at
E_QG = E_Pl/nu, gives rho_Lambda (eq. 4-5); the primordial amplitude A = 0.19 c1/nu (eq. 6) with c1 an undetermined
O(1) factor. Re-derived in `cosmin.py` from the paper's printed inputs:
- nu = 6144 (6.05e3 .. 6.35e3 over the printed 1-sigma inputs); paper (6.2 +/- 0.3)e3. Coefficient 0.1890 (paper
  0.19); A/c1 = 3.08e-5 (paper 3.05e-5); c1 = 1.52 for A_obs = 4.69e-5 (paper 1.54). REPRODUCED.
- READING NOTE: the text layer flattens fractions; read literally, eq. (4) gives nu ~ 1e-15. The reading that makes
  eq. (4) the exact inverse of eq. (3) -- E_QG in a denominator, (rho_eq L_P^4)^(-1/2) -- is DERIVED (check A,
  round-trip to 12 digits) and reproduces every number. A fault in the reading, not shown to be in the paper.
- FINDING (a narrowing of the paper's emphasis, not a refutation): eq. (7)'s "4 pi [1 + O(1e-3)] ... to the accuracy
  of one part in a thousand" holds at c1 = 1.54, and c1 is itself fitted. At c1 = 1 the ratio is 1.0071. And I_c
  depends on nu only through (2/3 pi) ln nu: any nu within a factor 1.81 of 6144 gives I_c within 1% of 4 pi. What
  the paper establishes is that nu from Lambda (6.1e3) and nu from A at c1 = 1 (4.0e3) agree to the O(1) factor c1.
- Bearing on this docket: a published, quantitative case where an information count fixes a physical constant --
  H-INFO and Q-1 in a concrete form, and Lambda is the 12-vector's Lambda-vector. The paper itself leaves open how
  its mode count relates to other measures of information (p. 8); a mode count is not a Shannon entropy, and Q-1
  must say how they relate before either is used for the other. Hypotheses to carry: the 4 pi postulate (motivated
  by dimensional reduction to D = 2 near the Planck scale, refs [5, 6], NAMED-NOT-READ), the sudden-transition
  idealisation, no inflaton, c1 undetermined.

M then placed the PDFs themselves (Drive 1sURRSCXFoIuKNyHjCsCocXmr0ocQxuBG, 1kNzmjH78gh6fwg12L6g00bcQTzMfvFpV),
both READ through the Drive connector.

- **1703.06144.pdf** is the same v1 (17 Mar 2017). Its layout settles the reading note above: eq. (3)'s argument
  prints k1(rho_L^2 rho_eq)^(1/12) over E_QG, and eq. (4) prints 1 over nu^6 (rho_eq L_P^4)^(1/2) -- the reading
  cosmin.py derived. The paper's equations are as derived; no discrepancy in the paper.

**2. Laughlin & Pines, "The Theory of Everything", preprint dated 1 April 1999, "[Published as Proc. Natl. Acad.
Sci. 97, 28 (2000).]" -- READ (M's Drive copy; the preprint, not the typeset PNAS pages).** Its claims: the
non-relativistic many-body Schrodinger equation (eqs. 1-2) is the theory of everything for everyday matter, yet
cannot be solved beyond about 10 particles -- memory for k particles scales as N^k, "a catastrophe of dimension";
exact laboratory results (flux quantum hc/2e, e^2/h, the Josephson relation) follow from "higher organizing
principles" (continuous symmetry breaking, localization), not from microscopics, and "would continue to be true
... even if the Theory of Everything were changed"; stable phases are "quantum protectorates" whose low-energy
excitations are particles "in exactly the same sense that the electron ... is a particle"; renormalizability,
gauge forces and fractional quantum numbers occur as emergent properties of ordinary matter, and "The Higgs
mechanism is nothing but superconductivity with a few technical modifications"; "The nature of the underlying
theory is unknowable until one raises the energy scale sufficiently to escape protection."
Bearing on this docket (readings, to be tested, not results):
- On H-IT: Laughlin & Pines make the vacuum's properties possibly emergent -- close to "spacetime comes from
  information" in form -- but the same argument cuts the other way: a protected low-energy law holds whatever lies
  beneath it. If relativistic causality is protected, an information layer beneath geometry would not show in
  low-energy signalling until the protection is escaped. That is a test condition for H-SETTLE, not a refutation.
- On the device (M: it "copies the information that defines the geometric object"): their N^k is the cost of a
  CLASSICAL description of a quantum many-body state. Teleportation does not store that description: it moves
  the state with 2 classical bits per qubit (transit.py), linear in the number of qubits. The catastrophe of
  dimension bears on copying the quantum definition as a classical record, not on moving it.
- On the board: their quasiparticles-as-particles corroborates the seating of quasiparticles beside the bosons
  (DOCKETS 27-31), and their Higgs-as-superconductivity is Anderson 1963 (their ref. 23, NAMED-NOT-READ), the
  analogue DOCKETS 63 and 65 work beside.

## M's thesis, verbatim (2026-10-02)

> My idea is that warp travel costs little because we are only relying on the communication of information
> between two entangled locations in spacetime

What the board already holds against it, owned by `transit.py` (computed, selftested): the protocol moves state,
not mass or energy (CARRIES_SUBSTANCE = False), so the cost per transit is a Bell measurement and two classical
bits per qubit -- **the "costs little" half holds**. But withhold the two bits and Bob's state is exactly I/2, so the
transit arrives no sooner than light (BEATS_LIGHT = False; advantage 0.000 at four distances); the pairs had to
cross the distance first (TRAVERSAL_IS_REMOVED = False, "it is MOVED EARLIER"; Maldacena-Susskind section 3.2, read
today, says the same of bridges); and the matter must already be at the destination (DOCKET 65: S10 REFUSED as a
supply, S13, the held-seat release route, OPEN and priced). **This docket tests the one step that blocks the
thesis: whether any channel removes the need for those two classical bits.**

## M's three replies on the corridor, verbatim (2026-10-02)

> Making the corridor. Joining two separate positions into one changes the topology of spacetime. - only to an
> observer
> Holding it open. Morris–Thorne (1988), graded STANDS: a crossable throat needs the null energy condition broken
> at the throat. - this is simply a translation of information only. No physics. The null energy doesn't exist
> here as it is being supplied by probability in the citation/seating
> Which moment the two ends share. - what if our error is accepting that spacetime is flat?

Read against the board:
- In general relativity topology is a property of the manifold: every observer agrees whether two regions are
  connected; what differs between observers is simultaneity and distance. Under H-IT, a corridor in the
  information layer is not a geometric topology change, and Geroch's theorem (a statement about Lorentzian
  manifolds) says nothing about it. Its cost is then whatever the information layer charges -- this docket's
  question.
- Likewise Morris-Thorne constrains a geometric throat; with no throat it does not apply. What "supplied by
  probability in the citation/seating" means is ASKED of M, not presumed.
- FLATNESS WAS A HYPOTHESIS of corridors.py (latticectc's H1), and M is right to strike it. Computed in
  `frw_frame.py` (sympy, Killing equation; control: in Minkowski the boost and time translation ARE Killing): in
  the spatially flat expanding universe ds^2 = -dt^2 + a(t)^2 dx^2 with a non-constant, spatial translations and
  rotations are symmetries; a time translation and a boost are NOT. So the only identifications that respect the
  geometry join positions at the SAME COSMIC TIME -- the expanding universe itself selects the frame H-FRAME asks
  for, and the different-frame corridors that build time loops in corridors.py are not identifications this
  geometry admits (their two ends would not match). The measured candidate frame is the CMB rest frame
  (`cmb-dipole-370kms`, D67: NARROWED).

### What "supplied by probability in the citation/seating" means -- M: "Consider both 1 and 2" (2026-10-02)

Both readings put to M are carried, as two work items:
- **R-INDEX** -- the probability of a cell in The Method's closed index, measured substrate-free by Q-1 (bits); the
  seat is where the cell is written. The measure contains no energy term at all, so within it there is no null
  energy condition to break. Energy re-enters only at the exchange rates (Landauer, Bekenstein, Holevo), which is
  where this reading is tested.
- **R-QUANTUM** -- probability in the quantum sense: states whose local energy density dips below zero. These are
  real (Casimir; squeezed states -- Kuo & Ford, D67) and bounded in magnitude and duration by the quantum energy
  inequalities the board holds (D67: gr-qc/9506083 STANDS; 1208.5399, gr-qc/0209036, fewster-osterbrink-qei,
  ford-roman-qi-and-fewster-casimir-fraction, kontou-fo-ffkp-nmc-qei NARROWED). This reading is tested against
  those bounds as graded.

## M on speed and the corridor, verbatim (2026-10-02)

> Speed is a non-issue. Consider that the corridor connects two positions as one, thus speed never enters the
> equation. Warp allows for two positions to occupy the same spacetime for whatever increment of
> relative/perceived/observed spacetime

Read against the board. Once two positions are identified, the distance across is zero and speed does not enter --
correct. The questions move to the corridor itself, each already held:
- MAKING it is topology change. Geroch 1967 (D67: NARROWED; the kinematic theorem stands): a compact, time-oriented
  interpolating spacetime with no closed timelike curve cannot change topology. Tipler 1977 (D67: NARROWED): the
  non-compact case gives a singularity or a point at infinity, under assumptions Borde leaves unnamed.
- HOLDING it open: Morris-Thorne 1988 (D67: STANDS) -- a traversable throat needs the null energy condition
  violated at the throat (flare-out).
- WHICH MOMENT the two ends share -- M's "whatever increment of relative/perceived/observed spacetime". Computed in
  `corridors.py` with latticectc's THEOREM (imported; model choice named: a corridor as an identification of
  positions under latticectc's H1-H3): one corridor whose ends share a moment in some frame closes no causal
  curve; two such corridors keyed to DIFFERENT frames (latticectc's witness E1, E2) do; any number keyed to ONE
  frame never do (by inspection, every lattice vector then has t = 0; 2000 random pairs checked). H-FRAME is
  therefore what separates a corridor network from a time machine.

## M's clarification of the device, verbatim (2026-10-02)

> The warp device doesn't copy the geometric object for reconstruction on the other side, it copies the
> information that defines the geometric object. The matter itself is irrelevant for the process, only the
> information defining it is necessary

Read against the board: this is the reconstruction route (specthm's Rec; DOCKET 65's S13 note, "only information
arrives"). Two cases by M's ruling M-S1A-P5 ("both. Quantum first, which should derive the classical."): a
QUANTUM definition cannot be copied, only moved (no-cloning, D67 adjudication: STANDS; transit.py
IT_IS_A_MOVE_NOT_A_COPY = True); a CLASSICAL definition can be copied, but is not the whole quantum definition of
the object. "Matter is irrelevant for the process" holds for the transfer; on arrival the information must be held
by a system with at least as many distinguishable states, or that matter formed (DOCKET 65: S10 REFUSED as a
supply; S13 OPEN, priced). The arrival time is set by the classical channel, which is this docket's question.

## M's premise and request, verbatim (2026-10-02)

> Cosmic/quantum information is all that matters. It is the only multi-universal currency. Without it, matter
> cannot exist, let alone form structural mass. We need to quantify information, unambiguously and independently
> of all cosmic/quantum physicalities

Carried as named hypothesis **H-INFO** (information is primary; matter cannot exist without it) -- M's, neither
established nor refuted here. The request is a work item: **Q-1, the substrate-free measure.**

What Q-1 starts from, READ at source 2026-10-02 (alphaXiv): Baez, Fritz & Leinster, arXiv:1106.1791v3, Theorem 2.
Any map F sending a measure-preserving function f: p -> q between finite probability spaces to a number in
[0, inf) that is functorial (F(f o g) = F(f) + F(g)), convex-linear and continuous satisfies
F(f) = c (H(p) - H(q)) for a constant c >= 0, with H(p) = -sum p_i ln p_i. The hypotheses name only finite sets,
probability measures and functions -- no physical quantity enters. Built on Faddeev 1956 (restated there as
Theorems 5-6; the uniform case forces phi(nm) = phi(n) + phi(m), hence phi(n) = c ln n). Shannon 1948 and Faddeev
1956 are NAMED-NOT-READ (restated in 1106.1791). What the theorem leaves open: the unit (c: bits for log base 2),
and -- the one place physics re-enters -- WHICH alternatives count as distinguishable, and with what probabilities.

On The Method's own closed index the alternatives are fixed by the coordinate list, so the count is unambiguous:
log2 976 = 9.930737 bits per cell of Lambda, log2 6912 = 12.754888 bits per cell of the product box (6,912 =
976 + 0 + 5,936, the corpus's own identity). Computed, not seated.

To read when the docket opens: Holevo's bound (how many classical bits n qubits can carry), Landauer (the energy
price of erasing a bit), and the Bekenstein bound (`bekenstein-bound`, D67: NARROWED) -- the exchange rates between
information and physics, kept separate from the measure itself.

## The question, as one sentence

Is there a channel, beyond linear quantum mechanics or beneath geometry, in which Bob's statistics depend on
Alice's choice? The test is any measured deviation from Bob's 0.5.

## Named hypotheses (M's, carried as hypotheses, never as results)

| id | hypothesis | source of the term |
|---|---|---|
| H-IT | spacetime comes from information | M, "let's assume this is correct" |
| H-SETTLE | quantum mechanics is slightly non-linear by deterministic drift ("quantum easing / quantum settling") | M's term; appears nowhere in the tree, corpus or chat export (searched 2026-10-02) |
| H-FRAME | a preferred frame exists, and messages may travel into the past | M |
| H-12 | the twelve parameters of the 12-vector are the fields to test as carriers | M |

## Pre-docket computations (2026-10-02, scripts beside this file)

1. `nosig.py`: singlet state. CHSH |S| = 2.828427 (Tsirelson 2√2; any local-hidden-variable account is capped at
   2). Over seven of Alice's angles Bob's P(+1) = 0.5 every time; I(Alice's choice; Bob's outcome) = 0.0 bits.
2. `fields12.py`: twelve independent fields coupling Alice's qubit to her local apparatus, each varied alone over
   [−50, 50] and all twelve over 500 random joint settings: largest change in Bob's reduced state 1.44e-15
   (rounding). In linear QM this is a theorem for every value of every field. The control in this file as first
   written is VACUOUS (a symmetry under conjugation by X averages it away) and is kept as a recorded fault.
3. `nlcontrol.py`: a deterministic Weinberg-type non-linearity H = ε⟨X⟩Z at Bob. Bob's ⟨σ_y⟩ then depends on
   Alice's basis: 0.00600 (ε = 1e-3), 0.05993 (1e-2), 0.53706 (1e-1), at T = 3; the linear control gives 0. Under
   H-SETTLE as M defines it, the drift is therefore a channel whose strength scales with ε and can be bounded by
   experiment.

## Read at source this session (alphaXiv)

- Maldacena & Susskind, arXiv:1306.0533v2: ER = EPR; footnote 1 makes non-traversability an assumption of the
  conjecture ("If this were not true, the ER=EPR connection would be wrong"); §3.1 no superluminal signals; §3.2
  no creation by LOCC; the particle-pair bridge is "Planckian ... probably cannot be described by classical
  geometry" (p.17), introduced as speculation (p.2).
- Maldacena, Stanford & Yang, arXiv:1704.05333v1: traversability needs an explicit coupling between the sides; the
  coupled protocol is teleportation with classical bits (eq. 2.3); what passes is bounded by the bits exchanged
  (eqs. 2.21–2.25).

## Named, not yet read (to be read at source when the docket opens)

Weinberg 1989 (non-linear QM); Gisin 1990 and Polchinski 1991 (signalling from deterministic non-linearity);
experimental bounds on non-linear QM; the collapse-model family (GRW/CSL), for contrast with H-SETTLE; Gao–Wald
on bulk versus boundary causality, for H-IT; closed-timelike-curve consistency (Deutsch; Novikov) and chronology
protection, for H-FRAME. Board holdings that bear on it: `latticectc.py` O3_CLOSED = False (CTCs held open);
`cmb-dipole-370kms` (D67: NARROWED) as the measured candidate frame; `no-communication-theorem` (D67: NARROWED);
`emtension.py` ENTANGLED_BRIDGE_IS_TRAVERSABLE = False (cites no source; read today — whether to record that is
asked of M and unanswered).

## M on negative probabilities and Q-1, verbatim (2026-10-03)

> strains Q-1, and this is a real obstacle. Shannon's entropy has a term p·log p, and the log of a negative number
> isn't defined. - we can define this. We plot it. With all its inverses, and reflections on the same multi-axis
> graph and the positive values will triangulate the negative values

> Yes. When docket 68 workflow is finished. Let's create the instrument and implement its use. Incidently, if this
> does prove useful, we should set up instructions for a new separate session to write a professional paper about
> the complex and negative entropy findings

Work item **Q-1s (signed / complex entropy)**, queued after the wave-1 repair. What it must establish, by
computation, before anything is claimed (the lead's derivation in conversation, by hand, not yet run):
- H = -sum p ln p on the principal branch, for quasi-probabilities (sum p = 1, some p < 0): Re H = -sum p ln|p|,
  Im H = pi N with N the total negative weight; the other branches add 2 pi i k per negative entry.
- Additivity on independent products: Re H additive (each factor sums to 1); Im H NOT additive (pi(N_p P_q + P_p N_q));
  M = log sum|p| additive (sum|p| multiplicative), zero exactly when no entry is negative; N = (sum|p| - 1)/2.
- Re H can be negative (p = (1.5, -0.5): -0.95 nats) -- to be read, not explained away.
- Whether (Re H, M) is the UNIQUE lawful pair under signed-measure versions of Baez-Fritz-Leinster's axioms: OPEN;
  the BFL theorem is proved for probability measures only.
- M's triangulation as a computation: reconstruct a signed distribution from non-negative projections along many
  axes (inverse Radon), with a control; the established laboratory form (optical homodyne tomography) is
  NAMED-NOT-READ until read at source, as are 'mana' and the Wigner-negativity literature.
Implementation: in Q-1 (measure.py), R-INDEX and any index carrying signed weights. If it proves useful: instructions
for a separate session to write a professional paper on the complex and negative entropy findings.

**Correction note (2026-10-03, wave-4 repair R3-alone; discrepancy D1 of Q1s-signed.md).** Added below M's verbatim
text and the Q-1s bullets above; nothing above this note was changed. The bullet "the other branches add 2 pi i k per
negative entry" states the shift of the **logarithm**, not of H. Putting entry i on branch k_i (Log_k z = ln|z| +
i(arg z + 2 pi k)) shifts **H** by **-2 pi i k_i p_i**: for a negative entry that is +2 pi i k_i |p_i| (for
p = (1.5, -0.5), k = 1 on the negative entry moves Im H by +pi, not 2 pi); positive entries have branches too
(-2 pi k_i p_i each); and a uniform k on every entry shifts H by exactly -2 pi i k, because sum p = 1. Re H is
branch-free. This is elementary and is computed in `signed.py` (selftest, section (1)); see Q1s-signed.md section 1 and
"Discrepancies and history", D1.

## M's rulings of 2026-10-03, verbatim (carried from M-RULINGS-2026-10-03.md; appended by M-apply, nothing above changed)

M's words are quoted exactly as `M-RULINGS-2026-10-03.md` records them; the line under each says only where it is
applied. These are rulings and are applied as worded.

1. **Clash (d), H-INFO-S against B-RECV.** M:
   > Teleportation carries no physical substance, but does carry information (non physical properties/bounds that
   > give shape to the geometry at the seat)

   Carried as the reading **H-INFO-SHAPE** (A3-measure.md § (viii), `measure.py` GRADES and `info_shape_screen`).
   H-INFO-S is kept as history and as the alternative reading.
2. **Weighting in the mean-value axiom.** M: "Carry both (Recommended)". Both are carried, each with the axioms it
   satisfies (`signed.py` § (8), Q1s-signed.md § 9): signed w selects Re H; |w| selects signed Rényi.
3. **"All its inverses and reflections".** M:
   > All of the above. Remember that the center begins at the ground state values given in real numbers from the
   > periodic table. That is the calibration

   All four are carried on one multi-axis table centred at the ground state (`signed.py` § (9), Q1s-signed.md § 10):
   the log branches, the conjugate and reciprocal, the fold to |p|, and the Radon inverse.
4. **D67's five held OPEN rows at (0,-1,0).** M: "Keep held, noted (Recommended)". They stay as they are, each saying
   in its text that the -1 is not a bound.
5. **H-INFO-SHAPE confirmed.** Asked whether what arrives is the defining information that shapes the geometry at the
   seat, with the physical substance supplied by the seat itself, M: "Yes, from the seat". O-MATTER is relocated to
   **O-SEAT, supply at the seat**, graded against LEDGER S13 (held-seat release, OPEN, priced) and S10 (REFUSED as a
   supply), DOCKET 65's instruments imported (A3-measure.md § (viii)). It stays an obstruction until the seat's
   supply is shown.
6. **Calibration of the origin.** M: "Mass/ binding. But could work for any of the other options depending on the
   question being asks or the object of study". The default calibration is MASS/BINDING (READ AME2020 / PDG / NIST
   values); GROUND-CONFIG (LW1-ground.py) and IONISATION are selectable, and every use names its calibration
   (`signed.calibrate`).

**Note (2026-10-03, F-alone; the third pair of re-verifications, V4-0 and V4-1 in `wave1/MRULINGS-RESULT.json`).**
Appended; nothing above this note was changed. Two application lines in the section above are made exact here:
- **Item 5.** M's words are "Yes, from the seat". Grading O-SEAT against S13 and S10 only is the record's carrying, not
  M's words: it is now the named hypothesis **H-SEAT-ROUTES**. The board's own supply-from-the-seat route, **S5**
  (reconstruction from destination stock; NOT REFUSED by M's mechanism, `massform.RECONSTRUCTION_SURVIVES`) with its
  **D25** stock gate, is computed as **H-SEAT-S5** (`measure.seat_route_s5`, `measure.info_shape_screen`): LEDGER S5 and
  D25 are OPEN, the gate is unchecked at every destination, S5's price is not re-derivable. **O-SEAT is graded OPEN**
  (its pathway S5/D25 is open; removed only if S5's supply is shown and D25 holds) and **LEFT given H-SEAT-ROUTES**; it
  stays an obstruction until the seat's supply is shown, and nothing removes it by assertion (A3-measure.md § (viii)).
  The ~0.998 mass share already at the seat is a first-order estimate (H-LINEAR), not a bound.
- **Item 6.** M lists "ground configurations, ionisation energies, or populate.py's axes". **POPULATE-AXES is not
  implemented: OPEN** (no rule turns an axis into a ground p0), and `signed.calibrate` refuses it with that reason.
  Item 3's "real numbers from the periodic table": MASS/BINDING centres an element on one nuclide (**H-NUCLIDE-GROUND**,
  AME2020); the periodic table's standard atomic weight, an isotope mean, is carried as the alternative **PT-AVERAGE**
  (**H-PT-WEIGHT**; CIAAW 2024 as DOCKET 67's raw audit read it, NAMED-NOT-READ at source this pass -- ciaaw.org 403).
  No verdict moves on the choice (Q1s-signed.md § 10).

**Dated note (2026-10-04), appended; nothing above edited.** The question this charter records as "asked of M and
unanswered" -- whether to record emtension.py's ENTANGLED_BRIDGE_IS_TRAVERSABLE against Maldacena & Susskind
arXiv:1306.0533v2 -- had been answered on 2026-10-02 before this charter was written: M, "Record it (Recommended)".
Recorded verbatim in M-RULINGS-2026-10-03.md item 14 and in the ledger as M-D68-C12; emtension.py carries the record.

**Correction to the note above (2026-10-04), appended.** That note said the question "had been answered on 2026-10-02
before this charter was written". The commit times show the reverse: this charter was committed (a1a2890, 14:44:20)
still reading "asked of M and unanswered", and M's answer was applied to emtension.py afterwards (50c53b9, 14:56:49).
The charter was written that day before the answer, as M-RULINGS item 14 and ledger M-D68-C12 say.
