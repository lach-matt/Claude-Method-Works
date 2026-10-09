# Item 179: the corridor exclusive to the bulk, and k's scale from that angle (the board's reading; computed, READ and deduced; verified once, findings applied; not seated; 2026-10-09)

*First headed* "Item 179 … (verified once, findings applied; not seated)". The instrument is `kstatic.py` (selftest
19/19, about 3 s). The refute verifier reproduced it independently in sympy and Wolfram 15.0.1. Items 180–185 were
recorded while it ran and are folded in.

## What you said

- **179/180** (verbatim): *"We know the corridor \*does not sit on either position's plane, it only bridges them. So
  one could surmise that the corridor is exclusive to the bulk."*
- **181:** *"this bears directly on B4d, and requires priority"*.
- **184:** *"There are no matter free planes"*.
- **185:** *"If it has potential to solve most of the current and future work, then we should run that now"*.

## Plain words first

1. **179 fits your rulings, with one exception.** That exception is 166's literal wording, and the fit rests on the
   board's reading that each plane carries only its mouth's side view.
   - It is your own picture from 57/58: two planes joined through a higher dimension.
   - It makes explicit what 101 (5), 129, 136 (3) and 152 (1) already said.
   - 127 (1) (the planes coincide) fits through 152 (1) and through 172 (2)'s endless approach.
2. **What gives way is the board's wording, not yours.** Clause (G), PASSAGE5D and the E-PASS route put the
   corridor's throat on our plane. Clause (B)'s "The plane is free of matter" also gives way, to your 184.
3. **k's scale still has no value.** No case computed so far ties ℓ to the corridor, and the verifiers found the
   structural reason (below).

## The board's reading

- **H-CORRIDOR-IN-BULK** (yours, as recorded). The board's re-reading of your carried H-CORRIDOR-SPANS-BOTH is
  **H-SPANS-BETWEEN**: the one object spans between both planes at once and is carried on neither. Your carried line
  is unchanged. H-BOTH-PIECES-AT-ONCE is proposed for withdrawal as a reading of 166.
- **H-PLANE-READS-MOUTH** (the board's reading, adopted under 149 and withdrawn if the mathematics refutes it).
  - "The corridor" is the bridging interior. Each plane carries at most the side view of its mouth or horizon (130,
    132).
  - This is consistent with 104 (b), 106 (b), 109, 130 and 132, and with Kaus–Reall and EHM (READ via
    epass_ground.json).
  - Your 182 (guess C) is consistent with it, but it is a guess, so it is not grounds.
- **Eq. (17) is demoted from input to candidate output.**
  - READ, Bronnikov–Kim gr-qc/0212112 p.1 and p.6: eq. (17) is a brane's intrinsic metric, with two flat ends on the
    brane for r₀ > 2m (p.3-4).
  - At the board's r₀ = 2m that two-ended structure is the board's own continuation: BK do not treat this member, and
    Pappas–Nakas call it the "WH/BH threshold".
  - BK's G = −E assumes a matter-free brane, so under 184 eq. (17) is at most a local reading.
  - Whether any plane reads it is OPEN.
- **Where standard physics pushes back (READ; reported, not refutations):**
  - For a static, matter-free plane at the Randall–Sundrum value, a bulk horizon beside it reaches it
    (Chamblin–Hawking–Reall hep-th/9909205 p.4; Kaus–Reall). With matter, or off the RS value, a static plane can sit
    beside a bulk horizon it never meets: Cooper et al. 1810.10601 p.63, case d; Myers–Ruan–Ugajin 2403.17483, warm
    phase, footnote 15.
  - In the literature, traversable bridges between branes put the throat **on** a negative-tension plane
    (Anchordoqui–Bergliaffa gr-qc/0001019 p.2; Barcelo–Visser hep-th/0004022 p.8). That is position 2's plane in M4.
  - No brane-boundary censorship theorem for a bridge between two planes was found in the sources searched. Galloway
    et al. state theirs for conformal boundaries; the board's CENSOR5D uses CGS with finite far boundaries. CENSOR5D's
    Theorem W carries only for the one-plane or coincident-composite case. For model C and separated planes it is
    OPEN.

## k's scale

**Verdict (computed in scratch, then verified once): no equality in any class computed so far.**

1. **Pure-tension planes in a uniform 5D black hole's bulk (the matter-free limit under 184; `kstatic.py`).**
   - *kstatic's static-plane lemma* (not the E-PASS spec's Lemma S): a plane at its flat-tuned tension is static only
     if k_s/a² = −2δ², where δ measures how unequal the bulk masses on its two sides are. Exception: a zero-tension
     interface between identical bulks.
   - **Our Z2 plane at the RS value.** Staticity forces μ = 0 and flat slicing: the bulk black hole is absent, and the
     separation is free (PRZ's massless radion, READ).
   - **Each universe with its own bulk (138).** The solutions are one-parameter families; every member has a naked
     singularity in an outer bulk, or coincident planes.
   - **The bridge (your C) does not occur in this class.** That is a matter-free limit, not your case under 184.
   - **Controls that can fail behave as they must:**
     - at μ = 0 and the RS value, nothing is fixed;
     - off the RS value with ε > 0, our plane is fixed and position 2 has no solution;
     - with ε < 0, the system is fixed but inadmissible (naked μ₂);
     - the literal per-sheet quarter has no static position-2 plane in this configuration.
   - **This rests on one assumption, A2: "static" means fixed R** (H-STATIC-SCALE, the board's reading of 141). 141
     itself fixes only the relative separation (H-INTERNAL-MOTION). The weaker reading is OPEN and must be redone: a
     fixed proper separation with expanding planes, where staticity is a radion condition (BDEL p.6-8, READ).
2. **Extremality (r_h = ℓ/√2 at k_s = −1) is not a candidate.**
   - No static plane at these tensions borders that bulk from outside its horizon.
   - Under the board's H-BULK-HORIZON-IS-THROAT it would give ℓ = 2√2 m = 5.62×10⁻²⁸ m. That is below the former
     lower edges, which are themselves being redone.
   - It also grows as √N (below).
3. **A static, uniform, closed toy plane with vacuum energy.**
   - The bulk mass is fixed against Λ₄ and ℓ drops out. That toy is unstable and is not our expanding universe.
   - Observation excludes it: its dark radiation would be about 2×10⁵ times the bound (refute verifier, computed;
     observed values standard-not-READ).

**The structural reason, found by the refute verifier (deduced).**
- Every corridor length grows with the README: m(N) ∝ √N, since r_min(N) = √N · r_min(1) (KDERIVE).
- So any equation of the form ℓ = c × (a corridor length) makes ℓ grow as √N, a different k for every README size.
  That covers:
  - the extremal value;
  - Maldacena–Milekhin's energy relation, whose r_e is free;
  - the five-dimensional count of your N bits: with G₅ = Gℓ, matching the chain's E(N) and N bits to a 5D horizon
    gives ℓ ∝ N²/E³ ∝ √N (deduced);
  - **any "local match" that ties m to ℓ, which is part of 185's plan.**
- Your 127 (2) (k is a coefficient with "the individual value for our current state") and 138 are read by the board
  as one k for our universe. On that reading, a candidate must tie ℓ to a scale that does **not** grow with the
  README: the Planck length through r_min(1), our Λ₄, or a corridor property independent of N.
- **This is a reading of 127 (2).** If k may differ per corridor, the conclusion changes (THROATBULK T4's
  H-K-PER-README). Your 140 ("k is dependent on our work") could be read either way. Whether to put this to you is
  decided after the matter round reports.

**The window.**
- The upper edge (ℓ < 10⁻⁴ m, table-top) stands.
- Both lower edges are to be redone under 179:
  - SIM2's 27.07m rests on eq. (17) on our plane.
  - B4c's edge holds for a round far surface only. With the write's ≥ 2.0×10⁵ clocks (163), B4D-STAGE1 D1 gives
    ℓ > 2R_reach = 4.0×10⁵ m in mass lengths for that surface, not the ~26m quoted before.
- **Conditional (deduced, order of magnitude):** if our plane reads eq. (17) in four-dimensional form, stage 2 S2
  gives ℓ ≲ 0.6m. That is in tension with the five-dimensional regime the old lower edges assumed.

## What the board told you that needs correcting

1. **"The 3/4 rests on your 139 (1) alone"** is not quite right.
   - It rests on your 139 (1) read in PRZ's doubled-space count (stage 7 K5). The literal per-sheet reading gives
     k_R = k_L/2, which is open under 174 (2).
   - The γ = β = 5/4 target, its obstruction, and the 9/8 light-bending and 13/12 perihelion predictions lapse only if
     no plane reads eq. (17)'s far field, which is OPEN. If our plane does read it, they bind that limit again.
2. **"B4c's lower edge ~26m"** holds only for a round far surface and the old static hold. With the write, it is
   4.0×10⁵ m in mass lengths, still to be redone.

## What it does to B4d (no status moves; nothing seated)

- **Order (181–185):**
  1. The two-plane balance, models A, B and C, with their matter-free limits.
  2. The matter round (185), covering both planes with matter, the local tidal match and the uniform dark radiation.
  3. The look-ahead re-run.
  4. E-PASS rebuilt as a passage through the bulk, with the spec's [FREE] core built first; open through 183, not
     refuted.
  5. Phase 2b-i reframed.
  6. E-NS.
  7. Phase 3.
  Phase 2 stays within one universe, as your 168 directs.
- **To redo:**
  - clause (G)'s wording;
  - clause (B)'s "The plane is free of matter", which gives way to 184 (each plane carrying its own universe's matter,
    the matter-free plane kept as a limit);
  - clause (Z) and clause (B)'s positivity, re-read under 183 as net per light ray;
  - both lower edges;
  - A2's weaker reading (expanding planes at fixed separation);
  - E-PASS's X6 placement and X7–X9, with the planes' face data as outputs of the bridge.
- **Carried unchanged** (statements about the bulk or about junctions): Lemma T, Lemma C, T5c, Lemma W, Lemma N, S15's
  coincident pair, the throat-bulk equations, sim2_passage X1–X6 and X10 (a)(c)(e), B4a, and SIM1 S3b in 5D.
- **Carried only as limits:** results that took eq. (17) as a plane's own metric, and matter-free results. They still
  bind any matter-free plane that reads eq. (17) (analytic uniqueness, LOCALBULK; X10 (c)).

## History

- **2026-10-09, workflow `item179-bulk-corridor`.**
  - **Run:** four readers (rulings, work impact, sources, the k computation), a synthesis, and refute and overclaim
    verifiers. The core mathematics reproduced in both. The overclaim verifier found no blockers, 6 major and 11
    minor problems; the refute verifier found 8 major and 9 minor.
  - **Applied:**
    - the "every case reaches the plane" claim is restricted to static, matter-free, RS-valued planes, with
      counter-cases cited;
    - the vacuum-energy result is reported as an unstable static toy that observation excludes, not as "our dark
      energy fixes the bulk mass";
    - A2 is named as the board's reading, and the weaker reading opened;
    - "refuted" for the extremal value is replaced by its proper grounds;
    - the √N constraint is stated once and applied to every candidate, 185's local match included;
    - the 5/4 obstruction is carried as a conditional limit, not set aside;
    - the 3/4 ratio's dependence on the doubled count is stated;
    - CENSOR5D's Theorem W is restricted to the one-plane and composite cases;
    - clause (B)'s matter-free wording is added to the redo list;
    - the "rulings fix it" grounds for H-PLANE-READS-MOUTH are replaced by the board adopting it as its own reading;
    - the for-M opening is made consistent;
    - BK's READ is limited to r₀ > 2m;
    - C2's control is restated;
    - B4c's edge is restated with the write's hold;
    - Maldacena–Milekhin's departures from you are listed (a gauged U(1); passage slower than going around; R5 not
      fixed);
    - 184's gloss is marked as the board's;
    - "withdrawn" is replaced by "proposed for withdrawal";
    - 185 is folded into the order.
