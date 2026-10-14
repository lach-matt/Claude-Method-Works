# B6″: k's scale tied to our G and the plane's tension (items 191 and 192; the board's edit of B6′; computed, READ and deduced; verified once by two separate AI sessions of this project, findings applied; not seated; 2026-10-09)

The instrument is `lemmas/b6p_scale.py`. In the run named under Reproduce, `--selftest` passed **18 of 18** checks in
76.7 s wall (75.2 s of it loading the owners, mostly `exactE.py`'s coefficient table), and `--mutants` ran **42**
named mutations and caught **42**, with none passing and none crashing (74.5 s wall). Nothing in `warptheorem.py`,
`WARPTHEOREM.md` or any other instrument was edited. The rows proposed for the integration are at the end.

Two separate AI sessions of this project checked the build: a refute pass and an overclaim pass. They are in-project
checks, not outside review. Their findings were reproduced and all of them applied (the list is under "Verification").
The status the build claimed **did not hold**, and this note now says what B6″ actually earns.

## What you said (verbatim, typing kept)

- **191**: *"Based on the results of gravity, let's assume the same interaction for k"*. Carried as H-K-LIKE-GRAVITY
  (yours).
- **192**: *"this appears to be a question to put to the math language hierarchy cypher"*.
- **196**: *"Review all tasks running. Stop any that are no longer relevant. All questions get works through the
  cypher"*.
- **136 (8)**: *"8 - leave it to measurement. But we can accurately hypothesize it first. Measurement would confirm."*
  This answered a question about **k**, and is carried as H-K-BY-MEASUREMENT.
- **139 (4)**: *"4 - why are you still chasing distance/speed? This was ruled out"*. The board's record of it reads:
  "the scale of k is not to be pursued as a hypothesis (H-K-BY-MEASUREMENT stands, item 136 answer 8)". B6″ puts
  forward no value for k. It gives a tie, which 191 and 192 later directed the board to find.
- **140**: *"If k helps define the bulk, the math in our work should give you pieces to both derive and prove k. Our
  math is not dependent on k, k is dependent on our work."*
- **127 (1)**: *"1 - yes"* (the planes coincide), carried "while the corridor exists". **141**: *"If planes are
  constantly in motion around each other, a stable throat cannot form. I suggest the planes are static, but their
  surfaces contain their own movements from within their own contained dimensions"*.
- **138**: *"In the standard one-plane bulk  - the problem is that you assume the bulk is contained to a single plain.
  It is not. I keep saying, it is multi-universal."* **139 (1)**: *"1 - yes"* (position 2's plane is negative, a
  quarter of ours; ours is positive).
- **184**: *"There are no matter free planes"*. **187 (2)**: you chose *"For the math"*. **129 (1)**: our current state
  holds matter and no corridor.
- **193** was withdrawn by **194**, and nothing here uses it. **195** (*"The README is not a pair"*) does not bear on k.

## Plain words first

1. **What the cypher says about 192.** It classifies; it derives nothing.
   - **With the five-dimensional coupling's value known**, a mirror plane's k, its tension σ and its G are four copies
     of one number. The cypher marks every coordinate a KEY. That is the register 1356/1175 artefact: it says nothing
     about scale, and the build was wrong to report it as an answer.
   - **With the coupling's value left free**, as it actually is, the cypher finds E > 0 and the languages disagree.
     The board's own dependence test, which is not the cypher, finds that G alone does not fix k and σ alone does not
     either. G and σ together do.
   - So the answer to 192 is **one relation with two free numbers**. Measuring G removes one of them. The tension is
     the other.
2. **The relation is standard physics, READ at source.** On one mirror plane:
   **ℓ² = 3c⁴/(4πGσ − Λ₄c⁴)**, exactly, from Shiromizu–Maeda–Sasaki eqs. (18)–(19). At Λ₄ = 0 it is Maartens–Koyama
   eq. (25).
   - This is DERIVED from READ physics.
   - It is a one-plane limit, not the configuration of your 138.
3. **In the chain's own configuration** (lemma B5: the planes coinciding, the separation held, no radion), the pair
   acts as one Randall–Sundrum plane at k_R.
   - There **ℓ_R² = 3c⁴/(4πGσ_sum)**, with σ_sum = σ₁ + σ₂ = ¾σ₁ (your 139 (1)) and G the measured G.
   - For our own plane's (ℓ_L, σ₁) the coefficient is **9/(16π)**, not 3/(4π).
   - This is READING: it rests on two of the board's readings, H-LR-ZERO-MODE and H-ONE-G5.
4. **A correction to the build, stated plainly (135).** The build claimed that Cassini makes the measured G local to
   better than 10⁻⁴, and that it puts the planes at least 4.26 ℓ_L apart now. Both claims need the radion, a field
   that your 141 and lemma B5 remove, and the board withdraws both.
   - With the radion removed, γ = 1 at every separation, so Cassini bounds nothing here.
   - `bulk/STATIC.md` had already recorded γ = 1 with the radion gone.
5. **On a two-sided plane, G and σ fix only the product k_a·k_b**, not k itself.
6. **Λ₄ fixes only how far σ departs from the Randall–Sundrum value, never σ itself.**
7. **Status.**
   - **B6″ is NOT GREEN.** It rests on READ and standard-not-READ premises, on readings of the board's, and on a
     value that is NATURE.
   - **It carries one OPEN row, B6″c, which B6′ did not.** B6″c covers a finite separation (our current state too,
     if its planes are apart) and your multi-plane bulk.
   - So, as worded, **B6″ does not meet the theorem's condition** ("proved exactly when no lemma is OPEN"). B6′ met
     it.
   - In the chain's own configuration alone (rows a and b) it is NATURE, and still not green.
   - The cypher gives k's **tie**, not k's **value**. The value is measurement's, by your 136 (8).
8. **The window.**
   - On one plane: σ ≥ 1.48×10⁵³ J/m³, that is σ^¼ ≥ 9.18 TeV. This is a 68% confidence bound, read through MK
     eq. (41), which is the one-plane law.
   - On the chain's composite: σ₁ ≥ 1.98×10⁵³ J/m³.

## The board's readings (kept apart from your words)

- **H-CYPHER-COUPLING-INDEX**: the board's encoding of each question as an index for `tools/cypher.py`. The roster
  stays data: all three rosters (1173, 33.1, 20.2) are run, and none is chosen.
- **H-ONE-K-LAW**: the board's reading of 191, as worded in 191's record. It holds that:
  - there is one five-dimensional curvature law;
  - each universe's k follows from its own plane;
  - a corridor's region has no k of its own;
  - and so the tie must not grow with the README.

  It is used only in two places: for B6″ to be the whole of "k's scale", and for the README caps in §4. Each place it
  is used, it is named as the board's reading, never as 191.
- **H-ONE-G5**: the board's provisional decision on 187 (2) (ITEM186 §6). It takes one 5D coupling, so one M across
  both Lykken–Randall regions.
- **H-ZERO-MODE-NORM**: the board's model for a two-sided plane's G: the zero mode normalised over two infinite AdS
  sides. Its mirror limit is MK eq. (27), READ.
- **H-LR-ZERO-MODE**: the board's (`bulk/MULTIPLANE.md`): Lykken–Randall at linear order, zero modes only. It is used
  here as `bulk/STATIC.md` uses it, with the radion removed (141, B5) rather than left unstabilized.
- **H-MEASURED-G-IS-LOCAL**, carried by the build, is **withdrawn**. Its Cassini grade needed the radion.

## 1. The cypher (computed; `tools/cypher.py` imported by path; it classifies, it is not a physical derivation)

Each index is built inside the instrument. The board's analysis declaration is a **computed** residual: each cell is
checked against S2's sympy law, which is derived independently of the cells, and analysis speaks only when the
residual is zero on every cell. The "fixed by" binaries come from the instrument's own `determined()`, the board's
functional-dependence test, which is not part of `cypher.py`. They are marked **(helper)**. E, agreement, "adds
nothing" and KEY are `cypher.py`'s.

The E values below are for roster 1173, in the order order / algebra / geometry / information / statistics.

| index | `cypher.py` | helper and analysis |
|---|---|---|
| **Mirror planes, coupling's value known** (k_a = k_b, σ, G; 4 cells) | E = 0/0/0/0/0; the languages agree; **every coordinate is a KEY** (register 1356/1175 artefact) | analysis speaks |
| **CONTROL: coupling's value free** (G5 ∈ {1, 2}; 8 cells) | E = 23/23/19/8/0; the languages **disagree**; no KEY | (helper) G alone: no; σ alone: no; **(G, σ): yes**. Analysis speaks (σG = 3k²/(4π) holds at any coupling) |
| **Two-sided planes** (k_a, k_b ∈ {1..4}; 16 cells) | E = 63/63/80/30/12; the languages disagree; G adds nothing | (helper) G is fixed by (k_a, k_b) |
| **CONTROL: G with a coupling of its own** (32 cells) | E = 288/288/296/131/27; G no longer "adds nothing" | (helper) (k_a, k_b) no longer fix G; analysis falls silent |
| **G5 under one bulk law** (exponents N, G, σ, l_P, G5; 27 cells) | E = 54/54/30/27/30; the languages disagree; σ is recoverable, N is not | (helper) G5 is fixed by (G, σ), and by none of N, G, l_P, (G, N), (G, l_P, N) or σ |
| **CONTROL: G5 = G·N** (27 cells) | E = 30/30/30/15/30; N is recoverable, σ is not | (helper) fixed by (G, N), not by (G, σ); analysis falls silent |
| **The separation, radion removed** (k_L, sep ∈ {coincident, far}, σ₁, G; 8 cells) | E = 6/6/6/3/2; the languages disagree | (helper) with the separation free, G is **not** fixed by (k_L, σ₁); at either fixed separation it is |
| **Λ₄ against σ** (3k², σ, Λ₄; 9 cells; S3's question) | E = 18/18/10/9/10; every coordinate is recoverable from the other two; no KEY | (helper) Λ₄ alone does **not** fix σ; (Λ₄, 3k²) does |
| **CONTROL: Λ₄ with no bulk term** (9 cells) | E = 0; 3k² is a free axis | (helper) Λ₄ now fixes σ; analysis falls silent |

- **Rosters.** All three are run. On the mirror index, every measured language in every roster has E = 0. Roster
  20.2's arithmetic, calculus, logic and constraint-language stay **NOT-RUN**, never SILENT (register 1172).
- **What the cypher adds, without overclaiming:**
  - It detects a second axis wherever one is put in: a second coupling, the coupling's value, a G5 tied to the
    README, a free separation, Λ₄'s bulk term.
  - It finds none in the mirror index, because that index was built with the coupling's value fixed. That is not a
    finding that no second axis exists.
- **A note on the encoding.** The refute pass's own encoding of the free coupling (σ = k/G5) gave
  E = 43/43/32/11/2. This instrument's encoding (σ ordinal 2k/G5) gives 23/23/19/8/0. The magnitudes differ; the
  verdict is the same: E > 0, disagreement, no KEY.

## 2. The relation (computed with sympy; READ)

**READ at source, verbatim from each PDF's text layer (math linearised as the text layer gives it):**
- Shiromizu–Maeda–Sasaki, gr-qc/9910076v3, **p.3**:
  - *"T_μν = −Λg_μν + S_μν δ(χ), (13) where S_μν = −λq_μν + τ_μν, (14) … λ and τ_μν are the vacuum energy and the
    energy-momentum tensor, respectively, in the brane world. Note that λ is the tension of the brane in 5
    dimensions."*
  - *"Λ₄ = ½κ₅²(Λ + ⅙κ₅²λ²), (18)  G_N = κ₅⁴λ/48π, (19)"*
  - *"Now we impose the Z2-symmetry on this spacetime, with the brane as the fixed point."*
  - *"Furthermore, we would have the wrong sign of G_N if λ < 0"*
  - *"It should be noted that the decomposition of S_μν into λq_μν and τ_μν can be ambiguous, particularly in
    cosmological contexts."*
- The same paper, **p.4**:
  - *"k = κ₅²λ/6"*
  - *"One can scale them as M_G → f²M_G and M_λ → f³M_λ, where f is an arbitrary constant, while keeping the
    gravitational constant G_N unchaged."*
- Maartens–Koyama, 1004.3962v2:
  - **p.3**, eq. (3): *"κ²₄₊d = 8πG₄₊d = 8π/M²⁺ᵈ₄₊d"*.
  - **p.8**: *"Λ₅ = −6/ℓ²"* (19) and *"(5)G_AB = −Λ₅ (5)g_AB"* (22).
  - **p.8**, under the two-brane model: *"RS 2-brane: There are two branes in this model [362], at y = 0 and y = L,
    with Z2-symmetry identifications y ↔ −y, y + L ↔ L − y. (24) The branes have equal and opposite tensions ±λ,
    where λ = 3M_p²/(4πℓ²). (25)"*
  - **p.9**: *"M₅³ = M_p²/ℓ. (27)"*, and *"The fine-tuning in Equation (25) ensures that there is a zero effective
    cosmological constant on the brane"*.
- Gregory–Rubakov–Sibiryakov, hep-th/0002072v2, **p.3**: *"σ = 3k/(4πG5), Λ = −σk, where G5 is the five-dimensional
  Newton constant."*

**Derivation (computed).**
1. The map between the two papers' constants is κ₅²Λ_SMS = Λ₅, deduced from SMS (6) with (13), set against MK (22).
2. Eliminating κ₅ through (19) turns (18) into **Λ₄ = 4πGσ − 3/ℓ²**, exactly. So ℓ² = 3/(4πGσ − Λ₄).
3. At Λ₄ = 0 this is MK (25), with M_p² = 1/G (MK (3)).
4. At that tuning, SMS's k = κ₅²λ/6 equals 1/ℓ, and G5 = Gℓ (MK (27)). So **G5² = 3G/(4πσ)**: G5 is fixed by G and σ.
   No subset of {N, G, l_P} fixes it.
- **Scope.** MK print (25) under the two-brane model. Their p.11 pairs (25) with (27) for the one-brane model, and
  adds that *"These limits do not apply to the 2-brane case"*. The relation used here is the single mirror plane of
  SMS's premise.

**Two-sided (computed).** This uses Israel's junction (standard-not-READ) and H-ZERO-MODE-NORM (the board's):
- σ = (3/κ₅²)(k_a + k_b) and G = (κ₅²/8π)·2k_ak_b/(k_a + k_b).
- So **σG = 3k_ak_b/(4π)**: G and σ fix only the product k_a·k_b.
- Both mirror limits reproduce what is READ: GRS's σ and MK (27)'s G.
- Normalising G with MK (28)'s volume factor e^(−4ky) fails this check, which a mutation shows.

**Controls that fail, as they must (computed).**
- A wrong tuning coefficient (⅓ for SMS's ⅙) gives 3/(8πGσ), which misses MK (25).
- Under SMS's own scaling, G is invariant and ℓ scales as f⁻⁶, so G alone fixes nothing.
- With λ < 0, G < 0 (SMS p.3). The relation belongs to our positive plane, not to position 2's negative one.

## 3. Λ₄ (computed; READ; and through the cypher, 196)

- From (18): **Λ₄ = (κ₅⁴/12)(σ² − σ_RS²)**. In our G: **Λ₄ = 4πG(σ − σ_RS)**, with σ_RS = 3/(4πGℓ²).
- **It fixes only the departure σ − σ_RS, never σ.** Two bulk scales with the same G and Λ₄ give two tensions
  (computed).
  - The cypher's index, with its control, says the same (§1).
  - So does SMS p.4 (READ): *"Hence Λ₄ may take arbitrary value as one may wish by appropriately specifying the values
    of Λ and λ."*
- **Numbers (computed).** Inputs: H0 (PINNED) and Ω_m (READ, Planck 2018), both from `cosmo.py`, imported. The model is
  flat ΛCDM with radiation neglected (deduced).
  - Λ₄ = 1.0891×10⁻⁵² m⁻², ρ_Λ = 5.2447×10⁻¹⁰ J/m³.
  - Across the window, (σ − σ_RS)/σ ≤ 7.1×10⁻⁶³. So the tuned form and the exact form agree to that precision.

## 4. The window (computed; READ; scoped)

- **The upper edge on ℓ.**
  - READ, Adelberger et al., hep-ph/0611223v3, **p.3**, eq. (18): *"V^k_ab(r) = −G M_a M_b/r β_k (1 mm/r)^(k−1)"*.
  - Their Table I: *"68% confidence laboratory constraints on power-law potentials"*, with k = 3, |β_k| = 1.3×10⁻⁴.
  - With MK **p.10**, eq. (41), *"V(r) ≈ GM/r (1 + 2ℓ²/(3r²))"*, this gives ℓ ≤ **13.964 µm** (68% CL).
  - MK (41) is the one-plane law, and MK p.11 says these limits do not apply to the two-brane case. So this bound
    holds **on one plane**. The build's line "your 138 multi-plane bulk is covered in §5" was false and is
    withdrawn: §5 treats one two-plane family, and computes no short-range correction for it.
- **On one plane: σ ≥ 1.4817×10⁵³ J/m³ = 7,106 TeV⁴, that is σ^¼ ≥ 9.18 TeV** (68% CL).
- **On the chain's composite** (deduced, on H-LR-ZERO-MODE at r = 0):
  - The composite is one RS plane at k_R, so MK (41) bounds ℓ_R, which is the only bulk region left.
  - That gives σ_sum ≥ 1.48×10⁵³ J/m³ and **σ₁ = (4/3)σ_sum ≥ 1.98×10⁵³ J/m³**.
  - Putting the bound on ℓ_L instead, with 9/(16π), would give 1.11×10⁵³ J/m³. But ℓ_L has no bulk region at r = 0,
    and a mutation that does this is caught.
- **MK's own step**, READ **p.11**: *"ℓ ≲ 0.1 mm … this leads to lower limits on the brane tension … λ > (1 TeV)⁴"*.
  - At 0.1 mm the instrument gives 138.6 TeV⁴ > 1.
  - That inequality has about 140× slack, so it is a consistency remark, not a guard. A normalisation error of 8π
    would still pass it. The pinned σ_min catches such an error.
- **The lower edges in m(N), under H-ONE-K-LAW** (the board's reading, not 191's words). Here m(N) = m₁√N, with
  m₁ = 3.79593×10⁻³⁶ m from `exactE.py`.

| edge (c_e) | standing | README cap at ℓ = 13.964 µm | σ_max at the example README |
|---|---|---|---|
| 27.0665 (SIM2, `sim2_facing.ell_w_class()`) | a limit under 179 | N ≤ 1.847×10⁵⁸ (ITEM186 S3's 1.85×10⁵⁸) | 9.98×10⁹⁵ J/m³ |
| 49.859 (SIM2 reached point, `sim2_bank.json`) | the same | N ≤ 5.444×10⁵⁷ | 2.94×10⁹⁵ J/m³ |
| 4 (E-PASS cap) | a candidate, not an edge; under one k it holds at one README size only (N = 8.46×10⁵⁹) | — | — |

- **The classical floor, N-free.** Under one coupling, ℓ > l₅ ⟺ ℓ > l_P (deduced, checked symbolically). Hence
  σ ≤ 1.106×10¹¹³ J/m³.
- **S4b: item 191's N-free ties run, folded in.** That run was a separate AI session's scratch work and is not in the
  tree. It is carried here, not re-run. This instrument re-computes only two things:
  - The window's tension scales run from (9.18 TeV)⁴ at ℓ = 13.964 µm up to about (3.72×10¹¹ GeV)⁴. The top is where
    item 155's README (3.8×10²² J, the board's figure in 155's question) stops fitting SIM2's down-the-throat edge.
  - The electroweak scale v = 246.22 GeV (standard-not-READ), taken as a tension, gives ℓ = 1.94 cm, **outside** the
    window. v sits about 37 times below the bottom of the window.
  - Whether any other N-free tie fixes σ is that run's result, carried.

## 5. Which G, which k (computed from `bulk/multiplane.py`, imported; READ)

- **The radion is removed, as the lemma's premises require.**
  - PRZ's c₀, as `multiplane.lr()` transcribes it, splits exactly into the Einstein zero mode plus the radion:
    **c₀ = −1 + 8M̂²/C_r** (computed).
  - Your 141 holds the separation, and B5 says the held separation leaves no radion. So c₀ = −1.
  - READ, MK **p.9**: *"In order to recover 4D general relativity at low energies, a mechanism is required to stabilize
    the inter-brane distance, which corresponds to a scalar field degree of freedom known as the radion"*.
- **With the radion removed** (computed):
  - G_meas/G_loc = **1/(1 + X)** and **γ = 1 for every X**, where X = e^(−2k_L r)(k_L − k_R)/k_R.
  - At coincidence (r = 0) with B6's k_R = ¾k_L the ratio is **¾**; far apart it is 1.
- **The composite at r = 0** (computed): the summed tension is 24M³k_R, the Randall–Sundrum value at k_R (B5a). So:
  - **ℓ_R²Gσ_sum = 3/(4π)**, in the measured G;
  - **ℓ_L²Gσ₁ = 9/(16π)**;
  - ℓ_R = (4/3)ℓ_L.
  - The build's 1/(2π) and 8/(9π) came from the radion and are withdrawn.
- **The radion kept** (a negative result, computed only to state it):
  - PRZ's c₀ gives ⅔ and γ = 5/4 at r = 0.
  - Its kinetic coefficient there is C_r = −96M³/k_L < 0: a ghost, which 141, B5 and your 139 (2) exclude.
  - If it were kept, Cassini (READ, Will 1403.7377v1 **p.43**: *"γ − 1 = (2.1 ± 2.3) × 10⁻⁵"*) would bound
    |G_meas/G_loc − 1| at 8.8×10⁻⁵ (68% CL), or 1.34×10⁻⁴ at two standard deviations (the board's Gaussian reading).
    It would also put a negative plane at least 4.26 ℓ_L away (68% CL), or 4.05 ℓ_L.
  - With B5's r = 0, it would predict γ = 5/4 on our plane today, which Cassini excludes.
  - None of this is a result about the chain: it holds only for a field the chain does not have.
- **What this does to the chain, plainly.**
  - B6's ratio k_R = ¾k_L (kderive.py K3) comes from your 139 (1)'s tension ratio alone, so it is **untouched**.
  - What falls is the reading of multiplane.py M4's "γ = 5/4 at r = 0" as a property of static planes: that γ came
    from the radion. `bulk/STATIC.md` already records it: *"With the radion gone, the long-range field is Einstein's
    (γ = 1), not eq. (17)'s 5/4."*
- **Our current state.**
  - 127's coinciding is carried "while the corridor exists", and our current state has no corridor (129).
  - If 141's static planes mean the separation never changes, it is zero now as well (deduced, on a ruling whose own
    word is *"I suggest"*). Then B6″a applies to our measured G.
  - If the planes are apart now, the coefficient depends on the separation, which no ruling fixes and which γ no
    longer bounds. That case is **B6″c, OPEN**.

## 6. Status earned (STRUCTURAL; the board's accounting of its own labels)

Each row's status is computed from its inputs' labels by `warptheorem.py`'s taxonomy, weakest input first (OPEN, then
NATURE, then READING, otherwise DERIVED). It is never typed in. GREEN is the stated rule: PROVED, DERIVED or AXIOM, with
every input green. Under that rule a READ input is a named premise, not a green one (135's board note). C15 checks that
this accounting is **consistent**. It cannot check that the labels are **true**.

| row | statement | status | rests on |
|---|---|---|---|
| **B6″a0** | on ONE mirror plane, ℓ² = 3c⁴/(4πGσ − Λ₄c⁴) exactly; a limit, not your 138 configuration | **DERIVED** (not green) | SMS (13), (14), (18), (19) and the Z2 premise, p.3, READ; MK (3), (19), (22), (25), (27), READ; SMS (14)'s split of tension from matter, READ, with SMS's caveat; your 184, only for "every plane carries matter"; κ₅²Λ_SMS = Λ₅, STRUCTURAL |
| **B6″a** | in the chain's configuration (r = 0, separation held, no radion): ℓ_R² = 3c⁴/(4πGσ_sum), σ_sum = ¾σ₁ | **READING** | SMS and MK, READ; PRZ as transcribed in multiplane.py, READ there; **H-LR-ZERO-MODE** and **H-ONE-G5** (the board's); your 57, 58, 120, 139 (1), and 127 with 141 (carried as H-STATIC-PLANES; its word is *"I suggest"*); chain lemma B5, DERIVED, which carries standard-not-READ inputs of its own |
| **B6″a2** | a two-sided plane: G and σ fix only k_a·k_b | **READING** | Israel's junction, two-sided (**standard-not-READ**; its mirror limit is GRS p.3, READ); **H-ZERO-MODE-NORM** (the board's) |
| **B6″b** | σ's value | **NATURE** | your 136 (8), carried from k to σ through B6″a (deduced); σ fixed by no lemma, Λ₄ included; the N-free ties carried from item 191's run |
| **B6″c** | the tie at a finite static separation (our current state too, if it is not zero), or in your multi-plane bulk (138; 123–124): k is fixed only together with every separation | **OPEN** | the separation index (§1) and §5 |

- **B6″ as one lemma: OPEN** (its weakest row), and **not GREEN**. No row is green.
- **The theorem's condition is not met by B6″ as worded**, because B6″c is OPEN. B6′ (NATURE) carried no OPEN row.
  - The integration may decide that B6″c lies outside the theorem, since the chain's configuration is B5's r = 0,
    where B6″a holds.
  - The board does not drop B6″c in order to make the condition hold.
- **In the chain's configuration alone** (B6″a and B6″b): NATURE, its weakest row, not green. A green B6 would need a
  measured σ or ℓ, and that is measurement, by your 136 (8).
- **Completeness as "k's scale"** rests on H-ONE-K-LAW (READING). If you withdraw it, B6″a still fixes the bulk's k in
  the chain's configuration, and a corridor's own k would be a further OPEN lemma (ITEM186 K6).
- **Rulings not stretched.**
  - 184 is used only for "every plane carries matter". The split of tension from matter is SMS's, READ, with their
    caveat.
  - "One k" and "no growth with the README" are H-ONE-K-LAW, not 191's words.
  - 136 (8) answered about k; σ inherits NATURE through B6″a (deduced).
  - Reading B6″ as 136 (8)'s "hypothesize it first", or as 140's "k is dependent on our work", is the board's reading.
    The tie comes from standard physics, READ, not from the chain's own lemmas.
- **196.** Every question here was put to the cypher with a control that can fail: the coupling, G5, the separation,
  and Λ₄ (S3's question, new in this pass). The helper's binaries are labelled as the board's, apart from the
  cypher's verdicts.

## What it does to the chain (proposed; nothing edited, no status moved, nothing seated)

- **Rows proposed for `warptheorem.py`'s LEMMAS** (in the instrument as `PROPOSED_ROWS`):
  - **B6″a**, READING: the tie in the chain's configuration;
  - **B6″b**, NATURE: σ by measurement, with the window's scope stated;
  - **B6″c**, OPEN: a finite separation, or your multi-plane bulk.
  - Together they would replace B6′ ("k's scale, by measurement", NATURE). B6″a0 is the one-plane limit inside S2.
- **The chain audit's input F6** (k's scale, 136 (8), NATURE) becomes B6″b.
- **B4's dependence on ℓ** becomes a dependence on σ_sum through ℓ_R = √(3c⁴/(4πGσ_sum)), in the chain's
  configuration.
- **A candidate question for you, not asked here:** "By 'the same interaction for k', do you mean that a corridor's
  region has no k of its own?" A yes would make H-ONE-K-LAW yours.

## Verification (two separate AI sessions of this project; findings reproduced, then applied)

Each finding was first reproduced by a scratch script that imports neither this instrument nor the verifiers'
scripts (`recover/work/B6p-scale/apply2/repro2.py`). No finding was rejected.

- **Refute F1, overclaim OC-3: the radion.**
  - Reproduced: c₀ = −1 + 8M̂²/C_r; with c₀ = −1, the ratio is 1/(1 + X), γ = 1 and the r = 0 value is ¾; C_r(0) =
    −96M³/k_L; the two-standard-deviation deviation is 1.34×10⁻⁴.
  - Applied: S5 and C14 are recomputed with the radion removed, and the Cassini deduction is withdrawn. The radion is
    kept only as a labelled negative result. The old `einstein_c0` mutation, which counted the correct premise as a
    failure, is replaced by `radion_kept`. The mislabelled `no_radion` index is now the separation index.
  - One refinement: F1's σ_min of 1.11×10⁵³ assumed that the table-top bound constrains ℓ_L. At r = 0 it constrains
    ℓ_R, so σ₁ ≥ 1.98×10⁵³ J/m³. The ℓ_L version is the `composite_on_ellL` mutation, which is caught.
- **F2, OC-1: a hidden OPEN.**
  - Reproduced: B6″_open was typed in from constants.
  - Applied: it is now derived from the rows' statuses; B6″c is its own OPEN row; the C15 mutation `open_hardcoded`
    is caught.
- **F3, OC-2: hidden non-green inputs.**
  - Reproduced: a standard-not-READ input was labelled READ, and DEFINITION was in the green set.
  - Applied: the labels are restored, and a guard checks each label against its own text. H-ONE-G5, H-ZERO-MODE-NORM
    and H-LR-ZERO-MODE are now inputs. GREEN is {PROVED, DERIVED, AXIOM}, and READ is not green.
- **F4, OC-5: "one axis" was an artefact.**
  - Reproduced with the free-coupling index.
  - Applied: C1 is relabelled as the 1356/1175 artefact, the control C1b is added, and "one axis" is removed from
    every row.
- **F5, OC-7: declared witnesses.** Four were static strings. Now every witness is a residual computed against S2's
  law, analysis speaks only when that residual is zero, and the helper is labelled apart from the cypher.
- **F6, OC-4, OC-8: scope.**
  - The window is scoped to one plane at 68% CL, and the composite's window is added.
  - "Covered in §5" is withdrawn.
  - Two-sided, G and σ fix only k_a·k_b.
  - 138 is no longer an input to the tie; it is why B6″c is OPEN.
  - MK (25) is READ with its two-brane heading.
- **F7.** C13 is labelled STRUCTURAL: σ's independence of N is assumed from SMS's split, not tested. MK (42) is a
  remark, not a guard (138.6 TeV⁴, about 140× slack; an 8π error gives 5.5 TeV⁴ and would still pass).
- **F8 and 196.** Λ₄'s question goes through the cypher with a control (C16), and items 193–196 are addressed above.
- **OC-6.** The rulings are restated as above (184, 191 as H-ONE-K-LAW, 136 (8), 140, and 139 (4)'s record).
- **OC-9.** The build's line "every number was reproduced in a separate scratch script" overstated what was done.
  - It was a same-session arithmetic replay outside the tree:
    `scratchpad/green/undefined/work/xcheck.py`.
  - It took S5's ratio as given. It did not reproduce the cypher E values, σ_max at the example README, the E-PASS
    N = 8.46×10⁵⁹, or the Λ₄ algebra.
  - The refute pass's own scripts did reproduce the numbers independently.
  - The runtimes in this note are copied from the named run.
- **OC-10.** SMS (17) is no longer cited, since it was never banked verbatim.

## Reproduce

```
python3 research/warp-drive/docket68/lemmas/b6p_scale.py              # the report
python3 research/warp-drive/docket68/lemmas/b6p_scale.py --selftest   # 18 checks
python3 research/warp-drive/docket68/lemmas/b6p_scale.py --mutants    # 42 mutations, each must be caught
```

The named run (2026-10-09, after the findings were applied) gave:
- `selftest PASSED: 18 checks, wall 76.7 s (owners 75.2 s)`
- `mutants: 42 run, 42 caught, 0 passed []; wall 74.5 s`

## History

- **2026-10-09, built for item 192's round.** The build claimed 15 checks and 30 mutations, and the status "B6″a
  DERIVED, B6″ NATURE, not OPEN".
  - **Sources.** SMS and Will were READ through the alphaXiv PDF reader, by page; arxiv.org is refused by the egress
    proxy (403). Adelberger, GRS and MK were READ from local PDFs in the session's scratch. MK pp.8, 9 and 11 were
    re-checked in this pass against the local text layer.
- **2026-10-09, refute and overclaim passes** (two separate AI sessions of this project). Both found that the status
  was not justified: four major refute findings and one overclaim blocker, plus minor findings. All are listed above.
- **2026-10-09, findings applied** (resumed across two container restarts from a partly edited instrument).
  - The status is re-graded to: B6″a0 DERIVED, B6″a READING, B6″a2 READING, B6″b NATURE, B6″c OPEN. B6″ is not
    GREEN and carries one OPEN row.
  - H-MEASURED-G-IS-LOCAL is withdrawn.
  - Λ₄'s question is put to the cypher (196).
  - Item 191's N-free ties run is folded in as S4b, carried and not re-run.
