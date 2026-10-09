# B6″: k's scale tied to our G and our plane's tension (items 191 and 192; the board's edit of B6′; computed, READ and deduced; not verified; not seated; 2026-10-09)

The instrument is `lemmas/b6p_scale.py`. Its selftest passes 15 of 15 checks in about 85 s, most of it spent in
`exactE.py`'s coefficient table. `--mutants` runs 30 named mutations, and each one makes its check fail. Nothing in
`warptheorem.py`, `WARPTHEOREM.md` or any other instrument was edited. The rows proposed for the integration are at
the end. The note has had no refute or overclaim pass yet.

## What you said

- **191** (verbatim): *"Based on the results of gravity, let's assume the same interaction for k"*. Carried as
  H-K-LIKE-GRAVITY (yours).
- **192** (verbatim): *"this appears to be a question to put to the math language hierarchy cypher"*. Carried as
  H-K-TIE-TO-THE-CYPHER (yours).
- **136 (8)** (verbatim): *"8 - leave it to measurement. But we can accurately hypothesize it first. Measurement would
  confirm."*
- **140** (verbatim): *"If k helps define the bulk, the math in our work should give you pieces to both derive and prove
  k. Our math is not dependent on k, k is dependent on our work."*
- **141** (verbatim): *"If planes are constantly in motion around each other, a stable throat cannot form. I suggest the
  planes are static, but their surfaces contain their own movements from within their own contained dimensions"*.
- **184** (verbatim): *"There are no matter free planes"*. **187 (2):** you chose *"For the math"*.
- **139 (4)** (verbatim): *"4 - why are you still chasing distance/speed? This was ruled out"*. B6″ chases neither. k is
  the bulk's curvature, a property of the geometry.

## Plain words first

1. **The cypher's answer to 192.** Under one five-dimensional law (191), a plane's k, its tension σ and its G lie on
   **one axis**: any two of them fix the third. G is measured. So k's scale comes down to one number, our plane's
   tension, which your 136 (8) leaves to measurement.
2. **The relation is standard physics, READ at source.** It is **ℓ² = 3c⁴/(4πGσ)**: Maartens–Koyama's eq. (25), which
   follows from Shiromizu–Maeda–Sasaki's eqs. (18)–(19). The exact form, valid for any Λ₄, is
   ℓ² = 3/(4πGσ/c⁴ − Λ₄). Neither G nor σ grows with the README, so the tie meets 191's requirement and ITEM179's √N
   rule.
3. **It gives no value, and neither does Λ₄.** Λ₄ fixes only how far σ departs from the Randall–Sundrum value, never σ
   itself. The value is nature's.
4. **Status: the relation is DERIVED, σ is NATURE.** So B6″ is **not GREEN** in the strict sense, because NATURE is not
   PROVED, DERIVED or AXIOM. It is **not OPEN** either. The theorem's own condition ("proved exactly when no lemma is
   OPEN") is met by B6″ just as it was by B6′. Stated plainly (135): the cypher supplies k's **tie**, not k's
   **value**. B6 can go fully green only with a measured σ, or equivalently a measured ℓ, and that is measurement, by
   your 136 (8).
5. **One reading of the board's is used, and only for completeness.** H-ONE-K-LAW says there is no k of the corridor's
   own. It is needed only for B6″ to be the whole of "k's scale". The relation itself does not use it.
6. **The window:** σ ≥ 1.48×10⁵³ J/m³, that is σ^¼ ≥ 9.2 TeV, from ℓ ≤ 13.964 µm.

## The board's readings (kept apart from your words)

- **H-CYPHER-COUPLING-INDEX** is the board's encoding of 192's question as indices for `tools/cypher.py`, described in
  §1. The roster stays data: all three rosters in `cypher.py` are run (1173, 33.1, 20.2), and none is chosen.
- **H-ONE-K-LAW** is the board's reading of 191, as worded in 191's record: one five-dimensional curvature law; each
  universe's k follows from its own plane; a corridor's region has no k of its own. It sets H-K-PER-CORRIDOR (186)
  aside as the working assumption. It is withdrawn if you say otherwise.
- **H-ONE-G5** is the board's provisional decision on 187 (2) (ITEM186 §6): one 5D coupling.
- **H-ZERO-MODE-NORM** is the board's model for a two-sided plane's G: the zero mode normalised over two infinite AdS
  sides. Its mirror-plane limit is MK eq. (27), READ.
- **H-MEASURED-G-IS-LOCAL** says our measured G is SMS's local G_N on our plane. Within the Lykken–Randall family it is
  deduced to better than 10⁻⁴ (§5). Beyond that family it is the board's reading, and it affects only a numerical
  coefficient.

## 1. The cypher (computed; `tools/cypher.py` imported by path; encoding H-CYPHER-COUPLING-INDEX)

Each index is built inside the instrument. Each analysis witness is a residual computed there. Every check below has
a mutation that makes it fail.

| index (d ≥ 4, never degenerate) | result |
|---|---|
| **Mirror (Z2) planes, one κ₅**: (k_a = k_b, σ, G) | every operator-bearing language has E = 0 and they agree; K.langclose holds; information flags **k_a, k_b, σ, G each as a KEY, not an axis** (register 1356): **one axis** |
| **Two-sided planes, one κ₅**: k_a, k_b ∈ {1..4}; σ ∝ k_a + k_b, G = 2k_ak_b/(k_a + k_b) | **G adds nothing beyond (k_a, k_b)** (information; logic's binary: G fixed by (k_a, k_b)). The nonlinear law gives **E > 0** (order 63, geometry 80, information 30, statistics 12); languages disagree; K.langclose holds |
| **Control: G with a coupling of its own** (λ ∈ {1, 2}) | **information's binary on G flips**: G no longer "adds nothing", and (k_a, k_b) no longer fix G |
| **G5 under one bulk law** (exponent coordinates N, G, σ, l_P, G5; G5² = 3G/(4πσ)) | G5 is fixed by **(G, σ)**, and by none of N, G, l_P, (G, N), (G, l_P, N) or σ. Information: σ is recoverable from (G, G5) and N is not |
| **Control: G5 = G·N** | the binaries flip: fixed by (G, N), not by (G, σ); N is recoverable and σ is not |
| **The radion: two planes, separation free** (k_L, sep ∈ {coincident, far}, σ₁, G_measured) | G is **not** fixed by (k_L, σ₁): **the separation is a second axis**. At a fixed separation, whichever it is, there is one axis again. Your 141 fixes it |

- **Rosters.** All three are run. On the mirror index every measured language in every roster has E = 0. Roster
  20.2's arithmetic, calculus, logic and constraint-language stay **NOT-RUN**, never SILENT (register 1172).
  Documentary is SILENT by construction (P20). Analysis is DECLARED, with a computed witness.
- **What the cypher adds, stated without overclaiming:**
  - The E = 0 on mirror planes is STRUCTURAL once the law is given. A one-parameter family monotone in every
    coordinate is a chain, and every closure of a chain is itself. The mutation that swaps G at k = 2 and 3 gives
    E > 0.
  - Likewise the G5 binaries follow logically from the exponent law.
  - The cypher's contribution is twofold. It finds **no hidden second axis** in the board's encoding. And it **detects
    one wherever one is put in**: a second coupling, a README-tied G5, or a free separation.

## 2. The relation (computed with sympy; READ)

**READ at source, verbatim from each PDF's text layer (math linearised as the text layer gives it):**
- Shiromizu–Maeda–Sasaki, gr-qc/9910076v3, **p.3**:
  - *"T_μν = −Λg_μν + S_μν δ(χ), (13) where S_μν = −λq_μν + τ_μν, (14) … λ and τ_μν are the vacuum energy and the
    energy-momentum tensor, respectively, in the brane world. Note that λ is the tension of the brane in 5
    dimensions."*
  - *"Λ₄ = ½κ₅²(Λ + ⅙κ₅²λ²), (18)  G_N = κ₅⁴λ/48π, (19)"*
  - *"Now we impose the Z2-symmetry on this spacetime, with the brane as the fixed point."*
  - *"Furthermore, we would have the wrong sign of G_N if λ < 0"*.
  - *"It should be noted that the decomposition of S_μν into λq_μν and τ_μν can be ambiguous, particularly in
    cosmological contexts."*
- The same paper, **p.4**:
  - *"k = κ₅²λ/6"*
  - *"One can scale them as M_G → f²M_G and M_λ → f³M_λ, where f is an arbitrary constant, while keeping the
    gravitational constant G_N unchaged."*
- Maartens–Koyama, 1004.3962v2:
  - **p.3** eq. (3): *"κ²₄₊d = 8πG₄₊d = 8π/M²⁺ᵈ₄₊d"*.
  - **p.8**: *"Λ₅ = −6/ℓ²"* (19), *"(5)G_AB = −Λ₅ (5)g_AB"* (22), and *"The branes have equal and opposite tensions ±λ,
    where λ = 3M_p²/(4πℓ²). (25)"*
  - **p.9**: *"M₅³ = M_p²/ℓ. (27)"*, and *"The fine-tuning in Equation (25) ensures that there is a zero effective
    cosmological constant on the brane"*.
- Gregory–Rubakov–Sibiryakov, hep-th/0002072v2, **p.3**: *"σ = 3k/(4πG5), Λ = −σk, where G5 is the five-dimensional
  Newton constant."*

**Derivation (computed).**
1. The map between the two papers' constants is κ₅²Λ_SMS = Λ₅. It is deduced from SMS (6) with (13), set against
   MK (22).
2. Eliminating κ₅ through (19) turns (18) into **Λ₄ = 4πGσ − 3/ℓ²**, exactly. So ℓ² = 3/(4πGσ − Λ₄).
3. At Λ₄ = 0 this is ℓ² = 3/(4πGσ), which is MK (25) with M_p² = 1/G (MK (3)).
4. At that tuning, SMS's k = κ₅²λ/6 equals 1/ℓ, and G = κ₅²/(8πℓ) = G5/ℓ (MK (27)). So G5² = 3G/(4πσ), the cypher's
   second finding in closed form.

**Two-sided (computed).** With Israel's junction (standard-not-READ) and H-ZERO-MODE-NORM:
- σ = (3/κ₅²)(k_a + k_b) and G = (κ₅²/8π)·2k_ak_b/(k_a + k_b).
- So σG = 3k_ak_b/(4π), that is **ℓ_a ℓ_b = 3/(4πGσ)**.
- Both mirror limits reproduce what is READ: GRS's σ and MK (27)'s G.
- The mutation that normalises G with MK (28)'s volume factor e^(−4ky) fails this check. That is a real pitfall.

**Controls that fail, as they must (computed).**
- A wrong tuning coefficient (⅓ for SMS's ⅙) gives 3/(8πGσ), which is not MK (25).
- Under SMS's own scaling, **G is invariant and ℓ scales as f⁻⁶**. So G alone fixes nothing, which is the cypher's
  "not by G" binary.
- With λ < 0, G < 0 (SMS p.3). The relation belongs to our positive plane, not to position 2's negative one (your 139
  (1)).

## 3. Λ₄ (computed; READ)

- From (18): **Λ₄ = (κ₅⁴/12)(σ² − σ_RS²)**, where σ_RS = 6/(κ₅²ℓ) is the tuned tension for the bulk's κ₅ and ℓ.
- In our G: **Λ₄ = (4πG/c⁴)(σ − 3c⁴/(4πGℓ²))**.
- **It fixes only the departure σ − σ_RS, never σ.** That is one equation in (σ, ℓ). Two bulk scales with the same G
  and Λ₄ give two tensions (computed).
  - SMS p.4 (READ) says the same: *"Hence Λ₄ may take arbitrary value as one may wish by appropriately specifying the
    values of Λ and λ."*
- **Numbers (computed).** Inputs: H0 (PINNED) and Ω_m (READ, Planck 2018 Table 2), both from `cosmo.py`, imported; flat
  ΛCDM with radiation neglected (deduced).
  - Λ₄ = 1.0891×10⁻⁵² m⁻², ρ_Λ = 5.2447×10⁻¹⁰ J/m³.
  - The departure (σ − σ_RS)/σ ≤ 7.1×10⁻⁶³ across the whole window. So the tuned form and the exact form agree to
    that precision, and B6″ needs no tuning premise.

## 4. The window (computed; READ)

- **Upper edge on ℓ.**
  - READ, Adelberger et al. hep-ph/0611223v3 **p.3**, eq. (18): *"V^k_ab(r) = −G M_a M_b/r β_k (1 mm/r)^(k−1)"*.
  - Their Table I, *"68% confidence laboratory constraints on power-law potentials"*: k = 3, |β_k| = 1.3×10⁻⁴.
  - With MK **p.10** eq. (41), *"V(r) ≈ GM/r (1 + 2ℓ²/(3r²))"*, this gives ℓ ≤ √(1.5 × 1.3×10⁻⁴) mm = **13.964 µm**
    (it reproduces ITEM185).
- **So σ ≥ 1.4817×10⁵³ J/m³ = 7,106 TeV⁴, that is σ^¼ ≥ 9.18 TeV, and k ≥ 7.16×10⁴ m⁻¹.**
  - The check against MK's own step, READ **p.11**: *"ℓ ≲ 0.1 mm … Then by Equations (25) and (27), this leads to
    lower limits on the brane tension … λ > (1 TeV)⁴"*. At 0.1 mm this instrument gives 138.6 TeV⁴ > 1, so it holds.
    MK add that *"These limits do not apply to the 2-brane case"*. Your 138 multi-plane bulk is covered in §5.
- **The lower edges in m(N)**, where m(N) = m₁√N and m₁ = 3.79593×10⁻³⁶ m from `exactE.py`, imported. Under one k
  (191) each edge ℓ > c_e·m(N) caps σ at 3c⁴/(4πG c_e² m₁² N), and **caps the README** at N ≤ (ℓ/(c_e m₁))²:

| edge (c_e) | standing | README cap at ℓ = 13.964 µm | σ_max at the example README |
|---|---|---|---|
| 27.0665 (SIM2, `sim2_facing.ell_w_class()`, imported) | a limit under 179 (eq. (17) on our plane) | N ≤ 1.847×10⁵⁸ (ITEM186 S3's 1.85×10⁵⁸) | 9.98×10⁹⁵ J/m³ |
| 49.859 (SIM2 reached point, `sim2_bank.json`) | the same | N ≤ 5.444×10⁵⁷ | 2.94×10⁹⁵ J/m³ |
| 4 (E-PASS cap) | a candidate, not an edge. Under one k it holds at **one README size only**, N = 8.46×10⁵⁹ at 13.964 µm, so it cannot be a law for every corridor (ITEM179's √N rule) | — | — |

- B4c gives no lower edge: the ellipsoidal far surface (ITEM186 §8, carried, not recomputed).
- **The classical floor, N-free.** Under one coupling G5 = Gℓ, so l₅³ = l_P²ℓ, and **ℓ > l₅ ⟺ ℓ > l_P** (deduced,
  checked symbolically). Hence σ ≤ 3c⁷/(4πħG²) = 1.106×10¹¹³ J/m³.
- The full snapshot (1.088×10²⁹ bits) sits far inside every cap above.

## 5. Which G, which k (computed from `bulk/multiplane.py`, imported; READ)

- **In B6's own configuration our plane is the mirror point.** That is the Lykken–Randall bulk as multiplane.py
  transcribes it from PRZ: τ₁ = 24M³k_L, the one-plane value at k_L. So SMS's local relation holds on it as
  ℓ_L² = 3/(4πG_loc σ₁) (STRUCTURAL).
- **The measured G against the local one** (computed from `lr()`):
  - G_meas/G_loc = **(3 − X)/(3(1 + X))** and γ = (3 + X)/(3 − X), with X = e^(−2k_L r)(k_L − k_R)/k_R.
  - The Newtonian projection (1 + c₀/2) is deduced from multiplane's h ~ T + (c₀/2)ηT.
  - At coincidence (r = 0) with B6's k_R = 3k_L/4: **2/3**, with γ = 5/4, which reproduces M4. Far apart: 1.
  - So on the coincident composite, in the measured G: ℓ_L²Gσ₁ = 1/(2π) and ℓ_R²Gσ₁ = 8/(9π), against 3/(4π) on one
    mirror plane. **The tie stands and the coefficient changes.**
- **Our current state.**
  - Your 129: no corridor. 127's coinciding is read since 172 as the endless approach down the throat.
  - READ, Will 1403.7377v1 **p.43**: *"Doppler tracking of the Cassini spacecraft … with a result γ − 1 = (2.1 ± 2.3) ×
    10⁻⁵."*
  - Within the LR family this gives X ≤ 6.6×10⁻⁵, so |G_meas/G_loc − 1| ≤ 8.8×10⁻⁵ (deduced).
  - It also puts any such negative plane at r ≥ 4.26 ℓ_L from ours **now** (deduced).
- **Two k's, one scale.** B6's ratio gives ℓ_R = (4/3)ℓ_L, so both are fixed once one is (computed).
- **The coefficient matters only when σ is measured by a route other than ℓ itself.** A short-range measurement
  (β₃ > 0) gives ℓ, and so k, directly.

## 6. Status earned, and whether it counts green (STRUCTURAL; the board's accounting)

- **B6″a, the tie (k fixed by G and σ, one axis): DERIVED.** It rests on the following, each green:
  - SMS, MK and GRS, READ at source;
  - Israel's junction and the two-sided zero mode (standard-not-READ; their mirror limits READ);
  - your 57, 58, 120 and 138 (planes joined through a higher dimension, in a bulk);
  - your 184, read with SMS (14)'s split of tension from matter (READ). SMS warn the split can be ambiguous in
    cosmological contexts (p.3, READ); σ is the tension part of it;
  - your 141, which fixes the separation so the radion is no second axis. It is carried as yours (H-STATIC-PLANES),
    and its own word is *"I suggest"*;
  - the exact Λ₄ form, which removes any tuning premise.
- **B6″a's coefficient 3/(4π)** holds on the mirror-plane reading and in the LR family, including our current state by
  Cassini. **Beyond the LR family, in a general multi-plane bulk (138), it is OPEN.** That affects the coefficient only,
  not the tie.
- **B6″b, σ's value: NATURE**, by your 136 (8). The board does not stretch 136 (8) into an AXIOM. It rules that the
  value is measurement's, which is not the same as giving a value.
- **B6″ as a whole: NATURE**, its weakest conjunct.
  - **Not GREEN** in the strict sense (GREEN = PROVED, DERIVED or AXIOM with no non-green input). The mutation that
    counts NATURE as green is caught.
  - **Not OPEN**, so the theorem's condition is met by B6″ as it was by B6′.
- **Completeness as "k's scale"** rests on H-ONE-K-LAW, the board's reading of 191 (READING). If you withdraw it,
  B6″a still fixes our plane's ambient k. A corridor's own k would then be a further lemma, OPEN (ITEM186 K6).
- **What changes from B6′.**
  - B6′ was a free premise of nature, "k's scale, by measurement".
  - B6″ makes k a function of measured G and one tension, k = √(4πGσ/(3c⁴)), on one axis. So measuring σ, ℓ, β₃ or G5
    measures all of them.
  - That is the "accurate hypothesis first" of your 136 (8), with measurement left to confirm.
  - It is also "derive k from the work" (140), as far as the work reaches: the tie, not the value.

## What it does to the chain (proposed; nothing edited, no status moved, nothing seated)

- **Rows proposed for `warptheorem.py`'s LEMMAS** (they are in the instrument as `PROPOSED_ROWS`):
  - **B6″a**, DERIVED: the relation, with its scope stated.
  - **B6″b**, NATURE: σ by measurement, with the window.
  - Together they replace B6′ ("k's scale, by measurement", NATURE).
- **The chain audit's input F6** ("k's scale: our plane's tension σ … 136 (8) NATURE") becomes B6″b. B6″a carries no
  non-green input for the tie.
- **B4's dependence on ℓ** (WARPTHEOREM's B6 row: "not B4, whose depth and far boundary depend on ℓ") becomes a
  dependence on σ through ℓ = √(3c⁴/(4πGσ)).
- **OPEN, newly named:**
  - the coefficient beyond the LR family;
  - how Cassini's r ≥ 4.26 ℓ_L in our current state sits with M4's r = 0, from which B6's ratio comes. That question is
    B6's, not B6″'s.
- **A candidate question for you, not asked here.** "By 'the same interaction for k', do you mean that a corridor's
  region has no k of its own?" A yes turns H-ONE-K-LAW into yours.

## Reproduce

```
python3 research/warp-drive/docket68/lemmas/b6p_scale.py              # the report
python3 research/warp-drive/docket68/lemmas/b6p_scale.py --selftest   # 15 checks
python3 research/warp-drive/docket68/lemmas/b6p_scale.py --mutants    # 30 mutations, each must be caught
```

## History

- **2026-10-09, built for item 192's round** ("run the Warp Theorem's chain through the cypher … even if it means new
  or edited lemmas"; this run builds the B6′ edit only).
  - **Sources.** SMS and Will were READ through the alphaXiv PDF reader, by page. arxiv.org is refused by the egress
    proxy (403). Adelberger, GRS and MK were READ from local PDFs in the session's scratch.
  - **Reproduction.** Every number was reproduced in a separate scratch script that does not import the instrument.
  - **The live cypher runs were re-run from the instrument.** It imports `tools/cypher.py` by path, rebuilds the six
    indices and runs every roster. The results of all five live indices were reproduced (§1). The radion index
    is new here.
