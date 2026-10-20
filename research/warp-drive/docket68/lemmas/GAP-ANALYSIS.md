# The warp theorem analysed for gaps and weak lemmas (item 541)

M, 541: "analysis the warp theorem to identify gaps or weak lemmas, to determine if more lemmas are needed to clarify,
or support anything currently contained in the theorem".

**What was read.** The statement (warptheorem.py's head) and all 83 rows of LEMMAS_NOW: each claim, every note and
the 40 RESTS_ON_NOW edges. Each row was traced to the instrument or record its notes cite where a claim looked thin.
The register stands at 74 PROVED, 6 DEFINITION and 3 COMPUTED-THEORIZED, and the theorem selftest passes 12/12.

**The determination.** More lemmas are needed: seven to support or clarify what the theorem now states, three
clarifications that are M's to decide, and five register corrections. Three of the seven are gaps: the statement
claims something no row carries. Four are weak rows: the row exists, but its support is narrower than its claim.
Nothing below moves a status. Each item names what would settle it.

## A. Gaps: the statement claims it, no row carries it

**A1. The middle of the family (lemma GMID).** The statement's scope is "N >= 7.12e9 ... exactly one static corridor".
The rows cover the two ends only: small, r_h << ell (Tangherlini), and large, r0 >> ell (Figueras-Wiseman, beyond
20 ell). corridor_family's verifier (item 261) found neither end controlled for r_h > 0.1 ell and r0 < 10 ell, and
E(N) through the crossover "published in neither paper read". At the statement's own ell (13.964 um) that band is:
- N from 5.31e57 to 3.38e62, a factor of 6.4e4;
- E from 1.99e37 to 8.45e39 J, the rest energy of 2.2e20 to 9.4e22 kg.

No row computes E(N), the area law's E, kappa > 0 or uniqueness there.
- *Settles it:* the static brane-hole family computed through the crossover with corridor_p2's Einstein-DeTurck solver,
  which already reproduces Figueras and Wiseman's uncharged hole (item 455). Their family, R4/ell 0.07-20, has one
  negative mode and no zero modes (READ, item 261). Alternatively, narrow the statement's scope to the two ends.

**A2. Uniqueness at the small end (lemma G0s).** G1 and G3 carry "exactly one static (J = 0) corridor" on Gibbons, Ida
and Shiromizu. Their theorem is for asymptotically flat vacuum. The small-end corridor is the hole on our plane at
finite ell: a brane with a bulk cosmological constant, which their hypotheses exclude. B3s records the finite-ell hole
as known "only numerically for one plane (Kudoh-Tanaka-Nakamura) and at the example through its first-order
deviation". So uniqueness, and existence beyond first order, are not proved where the example README sits
(r_h/ell = 8.0e-16).
- *Settles it:* Tangherlini's static perturbation problem in the mirror class (Kodama and Ishibashi's master equations at
  omega = 0, every type, even l >= 2) has no zero mode that is regular at the horizon and decays outward. l = 0 is the
  mass, fixed by N. l = 1 normal to the plane is odd under the mirror, and along it is the hole's position. A
  non-degenerate linearisation makes the localized hole exist and be unique order by order in (r_h/ell)^2.
- *Prior art:* Figueras and Wiseman's "no zero modes" (READ) is the cross-check. This is a computation, not a reading.

**A3. Our universe's information over the hole's life (lemma I3).** After the README is released at the write's end, our
face radiates for the rest of its life (CLOSEs; 336). b4d_small D15 keeps the Hawking partners in the core ("none of it
crosses"). D14 ends the face at most 2.05 J and 176 bits, by complete evaporation or a remnant, and leaves the choice
open. The radiation's fine-grained entropy grows toward the face's N ln2 = 1.90e15 nats, 1.6e13 times the end's
capacity. As the rows stand, either:
- our universe's evolution is not unitary, which QB itself assumes it is; or
- a remnant holds about 1e13 times its covariant capacity.

No row addresses this. Clause (I)'s "only information crosses" and (E)'s "radiated into our universe" are silent on the
partners' entanglement.
- *Settles it:* the Page curve on the theorem's geometry by the island formula (Penington 2019; Almheiri, Engelhardt,
  Marolf and Maxfield 2019; the replica-wormhole derivations), checked against 336 and 386 (nothing crosses after the
  release). If it holds, it also decides D14's end: complete evaporation, the information in the radiation.
- *Status:* this is semiclassical gravity beyond the established core. It would be theorized, and it is M's direction.

## B. Weak rows: supported, but narrower than the claim

**B1. The negative null energy on QB (lemma Z3q).** Z3bs and Z3b, and clause (Z), say the passage's negative is
"confined to the quantum region". That was computed on transition5, whose quantum region is sharp: "null energy failing
only inside the region". Since 537 the ten rows rest on QB instead. In QB the interior's mass function falls
continuously to the bounce: the departure is 0.2736 (x/x_b)^2 before it (bounce_close C4), with the whole mass carried
as negative effective energy there (C3). So on QB the negative has a tail through the interior; it is not sharply
confined. The tail is small: (x_h/x_b)^2 = 2.6e-18 at the horizon at the small end. The confinement has not been
re-derived on the row's current basis.
- *Settles it:* the effective null energy on QB's state along each ray: exactly zero outside the horizon, and inside it
  bounded by its (x/x_b)^2 tail with the integral computed. Then "confined" is restated as that bound. This is a short
  computation from bounce_qm's state.

**B2. Our face under gravitational perturbations (lemma O3g).** Clause (O) says "our face damping every disturbance".
O3s proves survival for Wall E's scalar wave (S6; Schlue, READ) and notes that "gravitational perturbations hold
Ishibashi-Kodama's mode stability only, outside the row's scope". Hung, Keller and Wang (READ in settle5: Theorem 2,
"the master quantities of every type", dimension six and below; Theorem 1, l < 2 pure gauge plus a linearised
Myers-Perry solution) give decay for every type. settle_late S2 shows the reconstruction regular for the scalar and
tensor types.
- *Settles it:* add the vector type's reconstruction. Exclude l < 2 Myers-Perry by J = 0 (the reflections). At the
  large end, cite Dafermos, Holzegel and Rodnianski's linear stability of Schwarzschild (to be READ). O3s's scope then
  lifts from the scalar wave to linearised gravity, metric included.

**B3. Z3c against the measured dark energy (lemma Z3d).** Z3c derives "w >= -1 at every epoch" from (Z). nature_rows Z3
records the tension and stops: the banked DESI+CMB+Union3 fit gives w(a -> 0) = -1.76. DESI DR2 (Abdul-Karim et al.
2025) prefers evolving dark energy over a cosmological constant:
- at 2.8, 3.8 and 4.2 sigma with Pantheon+, Union3 and DESY5;
- at 3.1 sigma from DESI+CMB alone.

The preferred fits cross into w < -1 in the past. No row says what the theorem does with this.
- *Settles it:* what (Z) admits as an apparent w < -1 without any null-energy violation, for example energy exchange in
  the dark sector, the brane's dark-radiation term (Z1's C', held >= 0 there) or a matter-density offset. Or the
  conflict is stated as the theorem's falsifier. Literature first (442), then the computation.

**B4. The static corridor after a finite-wavelength formation (row SETTLEs).** (G) asserts a static corridor, and
ARRIVALs has E(N) forming the face. At the emitter's physical wavelength the shell is round only on average, so the
static corridor needs the formed hole to settle. settle_late S0-S5 determines it: the end state is Tangherlini (proved),
linear settling holds (proved), the nonlinear evolution settles (computed) and its proof is open in the field
(theorized). This sits only in SOURCE's notes; no row carries it.
- *Settles it:* a row SETTLEs, COMPUTED-THEORIZED with its complete proof (M-CT-PROOF), tied to the 10 l5 work in the
  N1* session.

## C. Clarifications that are M's

**C1. Proved on QB.** 15 rows are PROVED and rest on QB (COMPUTED-THEORIZED): H2, M1, O1a, O1bs, O1cs, O1b, O1c, Z3bs,
Z3b, B3s, B3, B4ds, B4d, FACE2s and FACE2. By 441 PROVED means consistent with established physics, and the notes say
these rows rest beyond it, through QB. The tally of 74 PROVED does not show that. The docstring's "proved exactly when
no lemma is OPEN" then calls the whole theorem proved.
- *Recommended:* state the theorem conditionally, with QB and SOURCE's named theorized steps as its explicit
  hypotheses. Or give these rows a conditional label such as "PROVED on QB". The vocabulary is M's.

**C2. Which ell the SI figures use.** (G)'s 1.12008e-20 m and 1.28098e9 J are at ell = 13.964 um, the window's top, one
of the record's three readings. Under the Higgs tie (0.611 nm) or the dark-energy tie they differ.
- *Recommended:* name the reading beside the figures and give the scalings: r_h is proportional to ell^(1/3), E to
  ell^(-1/3).

**C3. Each row's current basis.** Notes accumulate by item, so a row's present support is read from its last notes,
past superseded ones. O1a, for example, carries 482's "specified, not derived", 483's loop-quantum-gravity basis
and 485's onset premise before 537's and 538's.
- *Recommended:* one generated "current basis" line per row, audited like the map.

## D. Register corrections (fix on approval)

- **D1.** E2us and E2xs still cite c_junction J1's "face open at most 33.6 clocks", withdrawn at 427. Unlike CLOSEs, O2
  and B4ds, they carry no 491 correction ("at most 2 r_h/c").
- **D2.** Missing RESTS_ON_NOW edges. The rows' own notes put the README's emergence on FACE2s/FACE2 and E1us's emission
  on close_small (CLOSEs's instrument). E1u and E1x rest on CLOSE, but E1us and E1xs have no edges. The missing edges:
  - E1us -> CLOSEs;
  - E1xs -> CLOSEs, FACE2s;
  - E1x -> FACE2;
  - O1a -> FACE2s, FACE2.

  T2 would miss these rows if FACE2s, FACE2 or CLOSEs moved.
- **D3.** The statement's clause (O) is stale in two places:
  - it puts the faces' equal mass "on one onset curvature for both sectors (415's P1-P4; transition5r R5)", but since
    537 it rests on unitarity with time-reversal symmetry (bounce_close C3; H2's 537 note);
  - "the white hole of our hole's mass (transition5q)" is now bounce_qm's reflected state, with transition5q supporting
    it.
- **D4.** passage_est's Q7 still reads "face2_open's, OPEN" and "error below any epsilon, not exactly", both withdrawn
  at 491. It is instrument text kept as written, so it needs a note, not an edit.
- **D5.** The write's balance is an unstable equilibrium. In five dimensions P_H is proportional to 1/M, so a mismatch
  grows with e-fold time 2 lives. Over the write, (1 + b) lives with b = 0.0062, that is a factor e^0.503 = 1.65.
  passage_est Q6's "match P_H to 1/N" should carry the factor. This is minor and changes no verdict.

## Order proposed

The computations that close a gap or restate a claim come first:
- G0s (A2), Z3q (B1) and O3g (B2), each short and on instruments in hand;
- then GMID (A1), using corridor_p2's solver;
- then Z3d (B3), literature first.

I3 (A3) and SETTLEs (B4) wait on M's direction. SETTLEs also waits on the N1* session's 10 l5. C1-C3 and D1-D5 are M's
to approve. D1-D3 are a few lines each.
