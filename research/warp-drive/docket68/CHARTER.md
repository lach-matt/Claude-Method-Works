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
