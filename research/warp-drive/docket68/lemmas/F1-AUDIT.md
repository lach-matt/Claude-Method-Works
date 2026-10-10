# F1 audit: eq. (17) as our plane's own metric, across the twelve lemmas that rest on it, and the theorem M1 that would green most of them (computed, READ and deduced; checked by two separate AI sessions in this project, findings applied; not seated; 2026-10-09)

*First headed* "F1 audit: eq. (17) as our plane's own metric, across the ten lemmas that rest on it, and the one theorem
M1 that would green them (computed, READ and deduced; not verified; not seated; 2026-10-09)". That heading over-claimed
twice. **Twelve** lemmas rest on F1, not ten: G1 and G3 do too. And M1 does **not** green all of them: Z2 and E4 as
stated need more than M1 gives.

Two separate AI sessions in this project checked the first version: one tried to refute it, one looked for
over-claims. Their 25 findings were reproduced and applied here; none was rejected. The instrument is `f1_audit.py`.
It imports its owners by path and copies none: `bulk/stability.py`, `bulk/passage5d.py` (and through it
`bulk/bulkseries.py`), `copy/coin.py`, `copy/plane.py`, `copy/exactE.py`, `bulk/localbulk.py`, `lemmas/ledger.py`,
`lemmas/b4_static.py`, `lemmas/b4d_stage6.py`, `lemmas/axioms.py`, `warptheorem.py` (statuses), `lemmas/b1_matter.py`
(the item-192 audit's input list), `../cosmo.py` (Planck's H0 and Ω_m) and `tools/cypher.py`. Its selftest and
`--mutants` results are in History at the end. It writes no file but its `--json` output. This note and the instrument
are the only files written. Nothing in `warptheorem.py` or `WARPTHEOREM.md` is changed; the proposed rows are at the
end, for the integration.

Labels: **computed** (by the instrument; check IDs in brackets), **numerical** (computed with fixed-step RK4 and no
error control, on the sampled points only), **READ** (verbatim, with page), **deduced**, **STRUCTURAL**,
**standard-not-READ**, **OPEN**. Your words are quoted verbatim. The board's readings are named H-… and kept apart from
your words.

## What you said

- **187 (3):** you chose *"Seat both"*. Clause (G) is seated as *"the corridor sits in the bulk, on neither plane
  (179/180), with eq. (17) kept only as a plane's possible reading of the corridor's mouth"*.
- **179/180:** *"We know the corridor \*does not sit on either position's plane, it only bridges them. So one could
  surmise that the corridor is exclusive to the bulk."*
- **184:** *"There are no matter free planes"*.
- **129 (1):** *"… the corridor is a bridge, so it adds nothing to either position."* **130 (1):** *"1 - i - no added
  matter. And in my model a black hole is not matter, it is what the mouth at position 1 looks like."*
- **132:** *"do the horizons still hold the README too (your item 106), as well as the throat? - yes. And the passage is
  one way by nature, a black hole in and a white hole out, side views of the same corridor object"*, with your
  correction *"\*different views of the same object"*.
- **172 (1):** you chose *"Yes, it may"*: position 2's piece may carry the README's stress. The board had said your
  129, 130 and 136 (2) read against it as worded.
- **183:** you chose *"Yes: never violated as a pair"*.
- **182:** *"If I had to guess, I would go with C"* (the two-sided bridge). A guess, not a ruling.
- **192:** *"this appears to be a question to put to the math language hierarchy cypher"*. **194:** *"Disregard that last
  ruling. I want that question put to the cypher"*. **195:** *"The README is not a pair"*. **196:** *"All questions get
  works through the cypher"*.
- **The round's task**, as relayed in the round's request and not recorded in the rulings file: see if the chain can
  go full green, "even if it means new or edited lemmas".

## Plain words first

1. **Every F1 lemma's decisive check still passes** [A1–A10]. What those checks establish is a statement about eq. (17)
   on a matter-free plane at the Randall–Sundrum tension: they use F1 and F2 both. O1's "nonsingular" is OPEN even
   there, because geodesic completeness was never computed (plane.py P1). Whether these are statements about *your*
   corridor is what F1 decided. Under seated (G) they are, only if a plane really reads eq. (17) as the mouth's side
   view. That is the theorem M1.
2. **Twelve lemmas rest on F1, not ten.** G1 (the one exact energy E(N)) and G3 (r₀ = 2m) also do. axioms.py builds
   E(N) from eq. (17)'s horizon at F = 0, so E(N) = r₀c⁴/(2G) is the plane's horizon relation. The item-192 list
   carried both as F1-free and counted them green; this audit moves them under M1. [C9]
3. **Five statements can be green now, without F1:**
   - **H2**, the horizons hold the README as well as the throat: **DERIVED** from your 132, which is its wording. No
     axiom is claimed; your 132 is used as your carried statement.
   - **O1a**, one way, a black hole in at position 1 and a white hole out: **DERIVED** from your 132 with your 130's
     "the mouth at position 1".
   - **Z1q**: for a Z2-symmetric plane bounding the vacuum bulk, along every null ray, the plane's apparent null-energy
     deficit is exactly the bulk's pull plus the plane's own matter. **PROVED** [B6]. Our plane is the case at the RS
     tension. The formula is **false** for position 2's negative-tension plane, which has its own form [B6, B7].
   - **B1q**: that same plane meets Gauss and Codazzi with its own matter (your 184). **PROVED** [B7].
   - **B2q**: for any such plane a local vacuum bulk exists, unique among analytic ones. **PROVED** (STRUCTURAL).
4. **What M1 would green, and what it would not.**
   - **M1 greens eight**, in their reach-limited forms on our side of the throat: G1, G3, O1b (no curvature
     singularity), O2, Z1t, Z2r, B2t and E4r. [C9]
   - **H2t also needs M1-P2**: position 2's side reads eq. (17)'s other leg.
   - **Z2 and E4 as stated are not greened by any M1.** They need eq. (17) exactly, out to infinity (M1-global), and Z2
     needs it on both legs. M1-global's exact form is **excluded**: the observed dark energy makes our plane's R4
     non-zero, and eq. (17) has R4 = 0 [C10]. Their reach-limited forms carry 99.96% of Z2's leg and 98.2% of E/4
     within 30m.
   - **O1c, geodesic completeness, stays OPEN.** B3, B4b and B4d stay non-green for reasons of their own.
5. **Two negative results, stated plainly (135).**
   - **Extremality does not follow from "the throat sits on the horizon".** Schwarzschild's throat does that with
     surface gravity 1/(4m). O2 needs eq. (17)'s particular form, or M1. [B3]
   - **M1's single-plane form fails near the horizon at every computed grid point, on the board's reading
     H-OWN-MATTER-ONLY.**
     - Every regular single-plane geometry with a compact horizon whose plane reads eq. (17)'s near-horizon geometry
       needs plane matter at the horizon of about 0.66 (ℓ/2m) σ_RS. At SIM2's edge of the window that is 8.0 σ_RS;
       at the example README it is 1.7×10⁴¹ times nuclear density. [C4–C6, numerical on the grid]
     - That matter is positive and obeys the NEC, but it is never our universe's matter.
     - With no added matter the bulk is singular at SIM2's depth y_s [C2]. A matter-free negative-tension plane does
       no better at the sampled ℓ [C2b].
     - **This rests on H-OWN-MATTER-ONLY**, the board's reading that the needed stress cannot be the README's. Your
       172 (1) allowed README stress on position 2's piece although the board had said 129/130 read against it. So the
       reading is not yours, and the cypher does not decide it [C11]. That is the one question below.
   - If the reading stands, **M1 survives only as a bridge:** your *"it only bridges them"* (179/180), your guess C
     (182). Position 2's piece must cap our plane's bulk before y_s.
6. **Through the cypher (196).**
   - **M1's single-plane question** [C8]. On the board's index no language admits "single plane, our matter only,
     regular". That exclusion is the index's own two-coordinate dependence: the projection to (matter, regular) is
     excluded alike. It restates the computation C2 and adds no independent exclusion.
   - **The stress question** [C11]. May our plane carry the README's stress at the mouth? Over every value order of
     the board's index, **no language of any roster decides it**. The control, with that cell seated, is decided by
     three languages.
7. **M1 is not claimed.** The first computation that would decide its bridge form is the whole position-2 piece
   (phase 2b-i), set out near the end of this note.

## The twelve lemmas

Each lemma below is given (a) its statement, quoted in the heading from `warptheorem.py` (abridged), with its status
there; (b) where eq. (17) as the plane's metric enters; (c) what survives with the corridor in the bulk (179/180); and
(d) whether it is re-proved now or needs M1.

### G1 "one exact energy, at the bound: E(N)" (DERIVED) and G3 "both holds at least size give r₀ = 2m" (PROVED)

- **(b)** axioms.derive_h2_g1 solves eq. (17)'s F = 0 for the horizon and sets m = r₀/2 (its comment: *"132: horizon
  radius 2m = r0"*), so E = r₀c⁴/(2G). exactE.py's identity "r₀ := r_min and m := GE/c⁴ give r₀ = 2m" then rests on
  the same relation. [A1, computed]
- **(c)** With the corridor in the bulk, the relation between the pull (131/133) and the horizon radius the plane
  reads is not fixed without eq. (17) on the plane. The 2 in r_h = 2Gm/c² is eq. (17)'s (and Schwarzschild's).
- **(d)** **Needs M1** (M1-c at the horizon). The item-192 list carried both with no input and counted them green
  [C9]. M1 is therefore stated below without E(N), from H1's area.
- **H1** (4πr₀² = N·A_bit) is not moved. It sizes the throat by its area (131), with no F. Whether that area is the
  plane's 2-sphere or a bulk 3-area is H2's bulk-form question (OPEN, below).

### H2: "the horizons hold the README as well as the throat" (DERIVED, axioms.py)

- **(b)** axioms.py H2 puts the horizon at eq. (17)'s F = 0, r = 2m, on the throat r₀ = 2m, with area N·A_bit. Its
  statement is plural: *"P1's future horizon and P2's past horizon are one null surface ... so both hold it"*. [A1]
- **(c)** On a plane that reads eq. (17), the horizon's trace is the sphere r = 2m, of area 4π(2m)² = N·A_bit. In the
  bulk the horizon is a three-dimensional surface, and how its 3-area relates to N bits is not fixed without the bulk
  geometry (standard area laws, standard-not-READ).
- **(d)** **The qualitative statement is DERIVED from your 132**, which is its wording (rulings file, line 1065) [B1,
  READ]. No axiom is claimed. When the board last carried one of your answers as an axiom (193) you withdrew it (194).
  Your 132 is used here as your carried statement, the convention the sibling notes use (b1_matter.py). H2 is one of
  your ten lemmas (151); its **PROVED** form, area N·A_bit on both planes, is **H2t**. H2t needs M1 for P1 and M1-P2
  for P2.

### O1: "one way, 1 → 2, nonsingular" (PROVED, plane.py P1; exactE.py)

- **(b)** exactE.py's z3 one-way check is the future cone at the throat in eq. (17)'s ingoing chart. plane.py P1 is
  eq. (17)'s causal structure. [A2, computed; both controls refuted]
- **(c)** Your 132 already says it of the corridor: *"one way by nature, a black hole in and a white hole out, side
  views of the same corridor object"*. With 130 (*"what the mouth at position 1 looks like"*) that is 1 → 2, a
  deduction from the two. On a plane that reads eq. (17), exactE's cone is that plane's view of it.
- **(d)** **Split three ways.**
  - **O1a**, one way, 1 → 2: **DERIVED** from 132 with 130 [B1, READ].
  - **O1b**, no curvature singularity: M1's regularity clause (M1-e), so it needs M1.
  - **O1c**, geodesic completeness: **OPEN**. It was never computed even for eq. (17) (plane.py P1: *"Geodesic
    completeness is not computed: OPEN"*), and M1 does not supply it.

### O2: "the horizon is extremal (surface gravity 0)" (PROVED, stability.py S1)

- **(b)** S1 computes D′(ρ_H) = 0 for eq. (17) at r₀ = 2m, with r₀ = 1.8m as the control. [A3, computed]
- **(c) Extremality as a property of the bulk horizon.**
  - A plane tangent to the bulk's static Killing field reads the bulk's surface gravity: D_ξ ξ = P(∇_ξ ξ) = P(κξ) = κξ
    on the horizon. STRUCTURAL, deduced. READ, Kaus–Reall 0901.4236v1 PDF p.4: *"In the bulk, the surface gravity is
    constant. Hence, by continuity, it will take the same value on the brane. Therefore if the horizon is degenerate on
    the brane then it will also be degenerate in the bulk."* (via `epass_ground.json`) [B2].
  - Computed instances: the RS black string has κ = 1/(4m) at every depth, the plane's value; Kaus–Reall's
    near-horizon ansatz has κ = 0 at every depth. [B4]
  - So O2's bulk form, "the corridor's bulk Killing horizon is degenerate", is DERIVED from M1 and S1.
- **(d) Needs M1.** It cannot come from your rulings without a geometry. "Both holds at the least size" (G3, 132) puts
  the throat on the horizon, and a throat on the horizon does not force κ = 0.
  - With F and H vanishing together, κ² = lim F′²H/(4F).
  - Schwarzschild (F = H, its Einstein–Rosen throat on the bifurcation sphere) gives κ² = 1/(16m²).
  - Eq. (17) at r₀ = 2m has H = O(F²), so κ = 0. [B3, computed]

### Z1: "5D null energy zero along the passage; plane deficit = bulk pull" (PROVED, passage5d.py P2)

- **(b)** P2 builds the bulk series on eq. (17) as the plane's metric with a matter-free plane (K = −g/ℓ), and reads
  R5(n,k,n,k) = −R4(k,k) = 2r″/r = (1/2)/((r − 3/2)²r) along the plane's radial null geodesic through the throat.
  [A4, computed; the passage5d foil breaks it]
- **(c) Under 179 the passage runs in the bulk, not on the plane.** What survives:
  - **"5D null energy zero" holds along any null ray of a vacuum bulk:** R5(k,k) = (2Λ₅/3)g(k,k) = 0 (axioms.py Z3's
    computation).
  - **The plane's deficit is the bulk's pull plus its own matter, for any trace, on a Z2 plane.** Take the contracted
    Gauss identity R5(k,k) = R4(k,k) + R5(n,k,n,k) − K K(k,k) + (K·K)(k,k). B5 checks it on two unrelated families;
    the identity itself is the Gauss equation, standard-not-READ. Add Israel's K for a Z2-symmetric plane of tension
    qσ_RS carrying any symmetric matter τ [B6, symbolic]. Then
    **q·8πG τ(k,k) + κ₅⁴ π(k,k) = R4(k,k) + R5(n,k,n,k)**, with π SMS's quadratic term and 8πG := κ₅²/ℓ.
  - **Our plane is q = 1**, at the RS tension of clause (B) as worded (to be re-worded after the item-186 note). The
    q = 1 form is **false** at position 2's q = −1/3, −1/4 or −1/6 (139 (1), in the counts stages 6–7 carry) and at
    multiplane M4's 4/3 [B6]. **A plane without Z2 symmetry is outside:** its K is not fixed by τ [B7].
  - On a plane that reads eq. (17), with H-OWN-MATTER-ONLY, τ at the mouth is ours. That is at most 2.3×10⁻⁶³ of eq.
    (17)'s tidal term at r = 3m for the example README [C1, C10]. That precision is for a plane reading eq. (17) only.
- **(d)** **Z1q** (the identity) is **re-proved now** (PROVED on the standard Gauss equation and Israel junction; F1-free
  and F2-free). **Z1t** (the value 2r″/r along the mouth's radial ray, our leg) needs M1.

### Z2: "the integral equals the plane's reading on both legs" (PROVED, passage5d.py P3; coin.py)

- **(b)** Q = ∫R5(n,k,n,k) dλ = 8/(3m) − (4/(3√3 m)) artanh(√3/2) = 1.652872/m. That is exactly −2 × coin.py's per-leg
  reading, over both legs of eq. (17)'s radial ray, u from −∞ to ∞ with r = 2m + u². [A5, computed]
- **(c)** The two legs are the two sides of the throat. coin.py reads them as the two positions (*"in the plane both
  positions read alike ... equal legs"*). Our leg alone carries Q/2 = 0.826436/m [C10].
  - Integrated Z1q on our plane: ∫[R4(k,k) + R5(n,k,n,k)] dλ = 8πG∫τ(k,k) dλ + κ₅⁴∫π(k,k) dλ.
  - Suppose the matter is a perfect fluid with ρ ≥ 0 and ρ + p ≥ 0 at each point. Then π(k,k) = ρ(ρ + p)(u·k)²/6 ≥ 0
    [B8]. Under your 183 (net per light ray, ∫τ(k,k) ≥ 0) such matter can only add to the bulk's load:
    ∫R5(n,k,n,k) ≥ −∫R4(k,k). Deduced. It holds also for matter ≪ σ (ours).
  - **For general NEC-obeying matter, π(k,k) is not sign-definite** (ρ = 0, p₁ = 1 gives −1/6) [B8]. So the inequality
    is not claimed there.
- **(d)** **Z2r**, our leg within the reach, to M1-c's order, needs M1. **Z2 as stated** needs M1-global (out to
  infinity) and M1-P2 (the second leg). M1-global's exact form is excluded [C10], so Z2 as stated is carried by Z2r:
  99.96% of our leg's integral lies within r = 30m.

### B1: "the plane is matter-free (R = 0) and meets Gauss and Codazzi" (PROVED, localbulk.py L1–L2)

- **(b)** R(4) = 0 is eq. (17)'s own [A6, computed; SdS fails]. "Matter-free" is input F2, which your 184 rules out
  as your configuration.
- **(c)–(d)** **B1q, re-proved now:** a Z2-symmetric plane of tension qσ_RS bounding the vacuum bulk, carrying its own
  matter τ, meets
  - Gauss: −R4 = −12(q² − 1)/ℓ² + q·8πG τ + κ₅⁴(τ·τ/4 − τ²/12). This is computed symbolically for general symmetric τ
    and general q [B7], on the Israel junction and Gauss equation (standard-not-READ). Our plane, q = 1, gives
    −R4 = 8πG τ + κ₅⁴(…).
  - Codazzi: D^μ τ_μν = 0 (conservation), STRUCTURAL.

  F1-free and F2-free. On a plane that reads eq. (17) exactly (R4 = 0), the matter must be traceless at leading order.
  Uniform dark energy is not traceless, so no plane carrying it reads eq. (17) exactly [C10]. That is why M1-c below is
  stated to an order, not exactly.
- **The name:** b1_matter.py also proposes a B1′ and a B2′, for the FRW plane with READ SMS and Dahia–Romero. To avoid
  the collision these are named B1q and B2q here; the integration reconciles the two.

### B2: "a local vacuum bulk exists, unique among analytic ones" (PROVED, localbulk.py L4)

- **(b)** The Cauchy data are eq. (17) with K = −g/ℓ; L3 shows them analytic through the horizon,
  dρ/du = 2√(m/2 + u²). [A7, computed; the owner's flags and an independent check at r₀; r₀ = 9m/5 fails]
- **(c)–(d)** **B2q, re-proved now (STRUCTURAL):** for any analytic trace and plane matter meeting B1q, the
  Cauchy–Kovalevskaya theorem with constraint propagation gives a local vacuum bulk, unique among analytic ones. This
  is localbulk L4's argument verbatim with general data (standard-not-READ, as there; b1_matter.py's B2′ has the READ
  Dahia–Romero footing for the FRW case). The instance **B2t**, the bulk beneath eq. (17), needs M1.
- **A consequence** (deduced, in b4_static's locally analytic class): under M1, the corridor's bulk near our plane
  *is* b4_static's static bulk, to M1-c's order. That bulk reaches a curvature singularity at y_b ≈ 2.49–2.50m above
  r = 2.15m (b4_static S2, Padé evidence, a heuristic). So **M1, in that class, needs some boundary, position 2's
  piece, to cut the bulk before y_b(r) over the throat.**

### B4b: "the bulk regular within every admissible hold's double cone" (READING, b4_static.py)

- **(b)** "With eq. (17) held on the plane, the static bulk (forced there in the board's locally analytic class)".
  Re-run from the bank: t_cert = 11.28 clocks, K ≤ 2.7 in its cone; the per-bit 28.48 clocks reaches K > 10⁴.
  [A8, computed]
- **(c)** Unchanged as a statement about the bulk beneath any plane whose trace is eq. (17) with no added matter. Under
  M1 the singular surface it finds must be excised (B2's consequence).
- **(d)** M1 removes its F1 input. It stays a READING (analytic class; Padé agreement a heuristic) and rests on F4 (the
  write lasts ≥ 2.0×10⁵ clocks), so it stays non-green.

### B4d: "the opening and closing evolve regularly in five dimensions" (OPEN)

- **(b)** Stages 5–7, simulation phases 1–2 and sim2_passage took eq. (17) as a plane's own metric. Stage 6 J6
  (STRUCTURAL): every positive-tension plane has a side where the warp decays [A9, re-run with the owner's
  `sigma_over_rs`]. Stage 5 makes that side singular, and C2 reproduces the throat column's singular depth.
- **(c)** Under M1 the same plane data give the same bulk, so these results bind any plane that reads eq. (17).
- **(d)** M1 removes F1 only. B4d stays OPEN: it is a five-dimensional evolution through the write, and M1 is static.

### E4: "the field energy outside the neck, total − pull = E/4 … the bulk's Weyl field read on the plane" (PROVED, ledger.py)

- **(b)** Misner–Sharp mass of eq. (17): M(R) = m + (m/4)(1 − m/(2R − 3m)), m at the throat and 5m/4 far away. "G = −E"
  uses a matter-free plane. [A10, computed; cross-checked with plane.py's Misner–Sharp at r₀; r₀ = 9m/5 fails]
- **(c)** This is a plane's-reading statement by nature: it is what a plane that reads eq. (17) sees of the bulk's
  Weyl field.
- **(d)** **E4 as stated** is the exact E/4 = M(∞) − M(throat). That needs M1-global, whose exact form is excluded
  [C10]. **E4r**, total − pull within the reach, (E/4)(1 − m/(2R* − 3m)) to M1-c's order, needs M1. 98.2% of E/4 lies
  within 30m [C10]. Even approximately, M1-global would bring back ITEM179's γ = β = 5/4 against Garriga–Tanaka's
  γ = 1 (READ in ITEM185, GT eq. (27) *"when 'the other' wall (the one in which we do not live) is empty"*).

(**B3**, "a complete bulk exists", is equivalent to B4a–B4d. F1 enters it only through B4b and B4d.)

## M1, stated

**M1 (H-PLANE-READS-MOUTH, as a theorem; OPEN; not claimed).** For each README size N, let r_h be fixed by H1's area,
4πr_h² = N·A_bit, and set m := r_h/2. G1's E(N) = mc⁴/G is then M1-c's reading at the horizon, not an input. There
are an ℓ in the window and a static five-dimensional spacetime 𝓑 such that:

- **(M1-a) vacuum bulk** (clause (B)): R_AB = −(4/ℓ²) g_AB on 𝓑;
- **(M1-b) the corridor exclusive to the bulk** (179/180): 𝓑 is bounded by our plane P1 and, in the bridge form
  (182), by position 2's piece P2; the corridor sits on neither;
- **(M1-c) the trace, to an order:** on P1, outside the corridor's horizon and within the reach R\*, the induced metric
  is eq. (17) at r₀ = 2m, up to corrections of relative order ε(r) from our universe's matter. B4c's causality step
  already says eq. (17) *"holds only within the reach"*. The bound [C10, computed; the measure is the board's, our
  matter's 8πGρ/c² against eq. (17)'s radial tidal term]:
  - our densest matter at the mouth, bounded by nuclear density: ε ≤ 2.3×10⁻⁶³ at r = 3m;
  - the uniform dark energy, ρ_Λ = 5.8×10⁻²⁷ kg/m³ (computed from READ Planck H0 and Ω_m via cosmo.py, flat):
    ε = 2.3×10⁻¹⁰⁶ at r = 3m. It grows as r³ and reaches 1 only at R_Λ ≈ 3.1×10³⁵ m(N), about 6×10⁷ m for the
    example README;
- **(M1-d) no added matter, on the board's reading H-OWN-MATTER-ONLY** (184 with 129 (1), 130 (1)): P1 carries the RS
  tension and its own universe's matter only, K = −(1/ℓ)h − (κ₅²/2)(τ − τh/3) with τ ours. **This clause is the board's
  reading, not your ruling** (see C11 and the question below);
- **(M1-e) regular:** no curvature singularity in the closure of 𝓑, and a smooth Killing horizon of the static field
  ∂_t, which is tangent to P1;
- **(M1-f) P2 admissible:** its stress, if any (172 (1)), is positive (139 (2), as H-POSITIVE-ON-P2 reads it) and obeys
  the NEC, net per light ray (183).

**Two stronger statements, kept apart from M1:**

- **M1-P2 (OPEN):** position 2's side, the white-hole view (132), reads eq. (17)'s other leg to the same order. That
  is the leg of H-EQ17-ON-P2. C2b finds its matter-free form singular at every sampled ℓ from 4.80m up, including
  position 2's own ℓ₂ under both counts. With 172 (1)'s README stress it is OPEN.
- **M1-global (excluded in its exact form):** R\* = ∞ with eq. (17) exact. That needs R4 = 0 everywhere on P1.
  - B1q gives R4 ≠ 0 for any uniform dark energy, whether it sits on the plane as matter (τ = −ρ_Λ h) or as a tension
    shift (q ≠ 1: R4 = 12(q² − 1)/ℓ²) [C10, computed]. The dark energy is observed (READ, Planck via cosmo.py).
  - Even approximately, ε passes 1 at R_Λ.
  - And even if it held, it would meet the γ = 5/4 caveat.

**What it greens** [C9, STRUCTURAL; the board's green rule: PROVED, DERIVED or AXIOM, with no non-green input; your
carried rulings count as green inputs, the sibling convention]:

| | green now (item-192 list) | green now, G1/G3 corrected | after the edits, M1 OPEN | with M1 | with M1 and M1-P2 |
|---|---|---|---|---|---|
| G1, G3 | green | not green | not green | **green** | green |
| the ten F1 lemmas' edits | none | none | **H2, O1a, Z1q, B1q, B2q** | + O1b, O2, Z1t, Z2r, B2t, E4r | + **H2t** |
| Z2, E4 as stated | not green | not green | not green | not green | not green (M1-global excluded) |
| O1c | — | — | OPEN | OPEN | OPEN |
| B3, B4b, B4d | non-green | non-green | non-green | non-green | non-green (own status: OPEN, READING, OPEN) |

So **M1 greens the reach-limited, our-leg forms.** H2t also needs M1-P2. Z2 and E4 as stated are never greened by
any M1: their exact values are the R\* → ∞ limit of Z2r and E4r. O1c stays OPEN. B3, B4b and B4d are non-green for
reasons of their own (O3, F4, F5 and the write).

## What is known for and against M1

**For:**
- **Local existence:** B2/B2q, the bulk beneath eq. (17) exists near the plane (computed L1, L3; CK
  standard-not-READ).
- **A regular region:** the static bulk is regular and Padé-stable in a region, with holds below 11.3 clocks; from
  r = 2.35m out, K stays below 2 to the grid's depth (b4_static S3, computed) [A8].
- **The degenerate horizon is consistent:** KR p.4 (READ above), and eq. (17)'s near-horizon AdS₂(2m)×S²(2m) is
  exactly KR's Q = 0 plane data (READ via the ground stage, deduced there).
- **A regular single-plane geometry exists at every computed 2m/ℓ** [C4]. Its only obstruction is the no-added-matter
  reading, not the geometry.
- **Near the throat the bridge passes:** SIM2-FACING, on its verified map (13 radii to 10m, nine ℓ), found facing
  allowed near the throat, in a band [y\*, y_s), with the README's stress on position 2's piece obeying the NEC.
  Positive energy needs ℓ ≥ 49.86m for a reached nearest point, or ℓ > 27.07m with an approach held at depth ≥ d₊.
  That is a necessary condition only (its own words: *"It does not say that such a piece exists."*). Those edges were
  computed with eq. (17) on our plane, which M1 grants.

**Neutral:**
- **FW 1105.2558 p.1** (READ in ITEM185): *"extremal solutions are thought to evade the non-existence conjecture"*.
  ITEM185 adds straight after: *"Ref. [25] is Kaus–Reall; those horizons are charged."* Their charge is plane matter
  (KR p.11: the bulk is independent of the brane's matter, READ via the ground stage). An M1 with no added matter
  excludes that matter, and C4's caps show the same.

**Against:**
- **Route 1 (ITEM185):** every READ static vacuum RS-II black-hole family cut by one positive-tension plane is
  non-extremal. KTN p.5: *"Assuming the surface gravity is nonzero (nonextremal)"*; the families have κr_h between
  about 1/2 and 1.
- **The vacuum-plane cap:** in KR's regular family the plane's charge reaches Q = 0 only as the horizon shrinks to
  nothing. READ via the ground stage, PDF pp.7–8: *"ρ0 and Q are monotonically increasing functions of A0 which vanish
  as A0 → 0"*. SIM2's Q = 0 throat bulk ends singular at y_s = 2.5536m (flat), reproduced here, and 0.9139m at ℓ = m.
  [C2]
- **This note's near-horizon result:** with no added matter the single-plane form fails at the computed grid points
  on H-OWN-MATTER-ONLY, and a matter-free negative-tension plane fails at the sampled ℓ ≥ 4.80m [C2b, C4–C6; next
  section].
- **The analytic bulk is singular:** b4_static S2 puts its singular surface at y_b ≈ 2.49–2.50m above r = 2.15m, so
  M1 needs P2 within that depth over the throat (deduced, analytic class, Padé evidence).
- **The far field:** M1-global is excluded exactly, and approximately it meets γ = 5/4 against every READ linear law,
  which gives γ ≤ 1.
- **A caution, carried from the E-PASS ground stage and not re-read here:** Horowitz–Kolanowski–Santos find that
  tidal forces generically diverge at extremal horizons when Λ < 0.

## What plane matter eq. (17) would need (your 184)

With matter on the plane the trace need not be vacuum, so the board computed what it would need, from B1q and Z1q
(q = 1, our plane) and three candidate bulks.

1. **The four-dimensional limit (bulk Weyl term zero).** The plane's matter must be G(eq. 17)/(8πG).
   - Its radial null part is R4(k,k) = −2r″/r < 0 at every r tested: −0.956, −0.2, −0.0741, −6.9×10⁻⁴ and −5.2×10⁻⁷
     per m² at r = 2.01, 2.5, 3, 10 and 100m. Pointwise negativity alone is not against 183, which allows a negative
     member paired along the same light rays.
   - Its net over both legs of the ray is −Q = −1.652872/m: **negative net per light ray, against your 183.**
   - It is also eq. (17)'s Bronnikov–Kim effective fluid. The board reads your 130 (*"a black hole is not matter"*) as
     saying that fluid is not plane matter either (H-BK-FLUID-NOT-MATTER, the board's gloss).
   - At r = 3m for the example README it needs about 1.0×10⁸⁰ kg/m³. Nuclear density supplies 2.3×10⁻⁶³ of that;
     neutron-star cores, several times denser, change nothing.
   - **Inadmissible.** [C1, computed]
2. **The matter-free plane (Weyl term supplies all; Q = 0).**
   - Admissible as matter.
   - Its near-horizon bulk is singular at y_s [C2].
   - On a negative-tension plane, the growing side (H-EQ17-ON-P2, stage 6 J3), numerical and sampled [C2b]:
     - no singularity to y = 50m at ℓ = 2m and 4.79m;
     - singular at the sampled 4.80m (19.50m deep) and 8m (3.951m);
     - singular at position 2's own ℓ₂ under both counts on the record: 2.634m at 3 × 27.07m (stage 6 J3 with 138),
       and 2.593m at 6 × 27.07m (B4D-STAGE6's downstream note, *"ℓ₂ = 6ℓ, not 3ℓ"*, put to you; 174 (2) *"For the
       math"*).
   - The 27.07m edge itself rests on F1. Stage 5 F6's "regular on the evidence" was found in the range ℓ = m/2 to 2m and
     agrees.
   - **No single matter-free plane carried eq. (17)'s near-horizon geometry regularly at any sampled ℓ from 4.80m up.**
3. **The regular single-plane geometries with a compact horizon (Kaus–Reall's ansatz).**
   - **The ansatz.** Near a static degenerate horizon the bulk is a warped product (KR cite it as proved in their ref.
     [16]; standard-not-READ). With SO(3) that is KR's (2.2), *"ds^2 = A(ρ)^2 dΣ^2 + dρ^2 + R(ρ)^2 dΩ^2"* (READ, PDF
     pp.4–5, via the ground stage), with dΣ² unit AdS₂.
   - **The equations.** The instrument derives the bulk equations and the constraint itself, and checks that its
     integrator's right-hand sides equal them [NH, computed].
   - **The cap and the cut.** A compact horizon must close where R → 0 (KR p.5: *"In the bulk, compactness of the
     horizon implies that R(ρ) must vanish somewhere"*), smoothly by their (2.8). Integrating from that cap, the first
     radius where A = R is the only place a Z2 plane can sit and read AdS₂(L)×S²(L) with equal radii. That is eq. (17)'s
     near-horizon geometry with L = 2m.
     - The series start meets the constraint [C3b]. It uses c₃ = (1/A₀² + 2/ℓ²)/18; the first version's /10 was wrong
       and moved the results by at most 3×10⁻⁸.
     - The cap's continuation shows one A = R crossing at every A₀ tested [C4]: A₀ = 0.005, 0.02, 0.05 (inside the
       window) and 0.6, 0.8, 0.95. The continuation runs out to ρ = 60ℓ, or to where it ends at A → 0 beyond the cut,
       which it does for the in-window caps (a curvature singularity on the side the Z2 plane discards; DOP853 agrees,
       a separate check).
   - **A non-compact horizon** (the branch that grows to the conformal boundary) is **not checked by this instrument.**
     One of the two checking sessions scanned the whole Israel constraint curve at 2m/ℓ = 0.0044, 0.0739 and 0.5. It
     found that branch needing ρ/σ between −2.62 and −1.82 at 0.5, and none at the other two values. That is recorded
     here, not re-run.
   - **What Israel then says.** For AdS₂-invariant plane matter (energy ρ, tangential pressure p, and radial pressure
     −ρ by the symmetry): ℓA′/A = 1 − (ρ + 2p)/σ and ℓR′/R = 1 + (2ρ + p)/σ. KR's (2.16) is the Maxwell case p = ρ
     (READ). The constraint at the cut is then exactly SMS's trace equation [NH].
   - **Integrator controls [C3]:**
     - A₀ = ℓ is AdS₅ (A = ℓ cosh, R = ℓ sinh) and has no cut;
     - **A₀ = ℓ/2 is exact.** There A = ℓ/2, R = (ℓ/√2) sinh(√2ρ/ℓ), the cut is at L = ℓ/2 with ℓR′/R = √6, and the
       plane needs ρ = (2√6 − 3)σ/3 and p = (3 − √6)σ/3.
   - **The family, computed on the grid** [C4, C5; numerical, RK4 without error control; monotone on the 12 grid
     points, not proved between them]. There is no cut for A₀ = 1.2 or 1.5:

     | 2m/ℓ | ρ/σ_RS | p/σ_RS |
     |---|---|---|
     | 0.0044 | 150.1 | −39.5 |
     | 0.0439 | 14.13 | −3.09 |
     | 0.0739 (SIM2's edge) | 8.02 | −1.48 |
     | 0.179 | 2.83 | −0.178 |
     | 0.5 | (2√6 − 3)/3 = 0.633 | (3 − √6)/3 = 0.184 |
     | 1.72 | 0.0589 | 0.0500 |
     | 57.7 | 5.0×10⁻⁵ | 5.0×10⁻⁵ |

     - ρ > 0 and ρ + p > 0 at every cut, with ρ + p_r = 0 by the AdS₂ symmetry: **positive and NEC-obeying.**
     - **The limits.** ρ/σ → 0.6627 (ℓ/2m) as 2m/ℓ → 0 (the ℓ = ∞ cap). ρ/σ → (1/6)(ℓ/2m)² as 2m/ℓ → ∞, which is
       four-dimensional general relativity's Bertotti–Robinson matter ρ = 1/(8πG L²) (standard-not-READ), reproduced
       to 10⁻⁴.
   - **Against your 129 (1)/130 (1), on H-OWN-MATTER-ONLY** [C6]:
     - **The window's lower edges are not F1-free.** SIM2-FACING's 27.07m was computed with eq. (17) on our plane, so it
       holds under M1's own premise. B4c's 4.0×10⁵ m is to be redone. The figures at the edges are conditional on
       them.
     - **At SIM2's edge the plane needs 8.0 σ_RS** (8.02), and 1.3×10⁵ σ_RS at B4c's edge.
     - **The example-README figure uses only the upper edge** (ℓ ≤ 13.964 µm). σ_RS is then 7.17×10¹⁸ times nuclear
       density, so at the example README the need is 1.67×10⁴¹ times nuclear density.
     - **Nuclear density would suffice** only for a mouth 2m ≥ 1.53×10⁴ m, a README of N ≥ 4.0×10⁷⁸ bits (4.6×10⁷⁷ at
       2×10¹⁸ kg/m³, neutron-star cores). Item 108's full snapshot is 1.088×10²⁹. Even granting the upper edge away, ℓ
       would have to exceed 2.3×10³⁶ m.
     - **So, on that reading, the corridor would have to add the matter.**
   - **Two capped sides do not help.** Every cap has ℓR′/R > ℓA′/A at its cut. Two capped sides of a two-sided plane
     therefore cannot cancel their anisotropy, which stage 6 J1's matter-free condition Π_L = −Π_R requires.
     [C7, computed within the family]
   - **Verdict (deduced, conditional).**
     - A static, single-plane M1 needs added matter at every computed grid point. Its premises: static, SO(3), the
       warped-product theorem, KR's regularity, a compact horizon, a Z2 or two-capped plane, and H-OWN-MATTER-ONLY.
     - The added matter is positive and obeys the NEC. It is excluded only by 129 (1)/130 (1) **as the board reads
       them**. ITEM185 read X22's cap the same way (*"needs README stress on our plane … which 129 (1) and 130 (1) read
       against"*); that is the same reading, not separate support.
     - **The reading is in tension with your 172 (1)**, where you allowed the README's stress on position 2's piece
       although the board had said the same rulings read against it. Whether the needed stress could be the README's
       on our plane is not ruled, and the cypher does not decide it (C11).
     - Not computed: whether the held README's energy E(N) could supply that stress. A first caution, deduced from the
       AdS₂ metric (standard-not-READ): the redshifted (Killing) energy of such matter near the horizon is finite, while
       its proper energy diverges logarithmically. Which energy E(N) is compared with must be fixed first.
     - Without added matter the single plane is singular. Hence, on the reading, the bridge.

## The questions through the cypher (your 196)

### M1's single-plane question [C8]

- **H-M1-TRACE-INDEX** (the board's encoding). The cells are the computed static near-horizon configurations whose
  plane trace is eq. (17)'s AdS₂(2m)×S²(2m), on the 12 grid sizes x = 2m/ℓ (ranks):
  - the regular single-plane caps, (x, ρ-rank > 0, regular 1);
  - the matter-free plane's bulk, (x, 0, regular 0), singular (C2).

  The question is (x, 0, 1): a single plane, our matter only, regular. Every roster in `tools/cypher.py` was run and
  none chosen. Analysis was declared, with the continuous law ρ/σ = f(2m/ℓ) as its witness.
- **Result** [C8, computed]:
  - Under rosters 1173 and 33.1, order, algebra, geometry, information and statistics each admit **0 of 12** question
    cells. Under 20.2, order and geometry admit 0 and the other four read NOT-RUN, which is the docket, not silence.
  - Documentary is SILENT by construction. Analysis returns a magnitude, not a binary.
- **What it means, plainly.**
  - The question cell is absent by construction, because C2 found the ρ = 0 configuration singular.
  - On the projection to (ρ, regular) alone, order, algebra, geometry and information also admit no (0, 1) [C8
    projection]. So the closures reproduce the index's own two-coordinate dependence: they restate C2.
  - **The cypher adds no independent exclusion.**
- **Control** (designed to flip): add a coordinate "extremal" and route 1's READ non-extremal families as
  (x, 0, 1, 0). They cover the grid: Tangherlini, KTN, FW and AC-PYT; at x < 0.004 the Tangherlini limit, by
  ITEM185's scoping. Then every operator-bearing language admits **12 of 12**. A three-way reading (extremal, regular,
  no added matter) applies to this control index only.

### The stress question: may our plane carry the README's stress at the mouth? [C11]

- **H-STRESS-INDEX** (the board's encoding): cells (plane, stress kind, allowed), one for each ruling:
  - (P1, own, 1): 184 with 129 (1);
  - (P2, own, 1): 184;
  - (P2, readme, 1): 172 (1);
  - (P1, added, 0) and (P2, added, 0): 130 (1).

  The question is (P1, readme, ·). The plane and the stress kind are nominal, so their value orders are the encoding's
  choice. All 12 orders are swept. A language **decides** only if, in every order, it admits exactly one of
  (P1, readme, 1) and (P1, readme, 0), the same one.
- **Result** [C11, computed]: **no language of any roster decides it.**
  - Order and algebra give three different verdicts across the orders. Geometry and information alternate between
    "allowed" and neither. Statistics admits neither cell in every order, which places no README stress on our plane at
    all but does not choose.
  - Analysis is declared silent (no magnitude here). Documentary is SILENT. Under 20.2 four languages read NOT-RUN.
- **Control** (must flip): seat (P1, readme, 1) as a cell. Then geometry, information and statistics decide it
  "allowed" in every order (geometry alone under 20.2), and none decides "excluded".
- **So the rulings and the cypher together do not decide it.** That is the question below.

## The first computation that would decide M1

On H-OWN-MATTER-ONLY the single-plane form fails at every computed grid point. If you allow the README's stress on our
plane, the single-plane form reopens with C4's caps as its candidates. The bridge form is left either way. Its first
decisive computation is **D1, the whole position-2 piece**: SIM2-FACING's OPEN G and phase 2b-i, sharpened by B2's
consequence.

- **The bulk.** Use the static bulk beneath P1. It is unique in the analytic class (localbulk L4), and computed by
  b4_static.py and sim2_facing.py (banked: `b4_static.json`, `sim2_bank.json`).
- **Find a hypersurface P2: y = Y(r)** with:
  - (i) Y(r) < y_b(r) wherever b4_static's singular surface exists (r from 2m to about 2.35m);
  - (ii) its throat end in SIM2's band [y\*, y_s), or an approach held at depth ≥ d₊;
  - (iii) its Israel stress positive and NEC-obeying at every r, from the one-sided junction with position 2's own bulk
    beyond (138). Z1q and B1q do not apply there: they are for a Z2 plane. It carries the README's stress (172 (1)).
- **What decides:**
  - If no such Y exists on the verified map for any ℓ in the window, static M1 is refuted in the analytic class.
  - If one exists, M1's static existence is met in that class. That leaves M1-P2, the analytic-class premise, and
    B4d's write.
- **What it needs first:** b4_static.json banks A, B and K but not C, the sphere's metric function that P2's
  extrinsic curvature needs, so the bank must be regenerated with C. SIM2's E-FAR/E-G (r ≈ 2.03–2.7m) is its first
  leg.

## Status earned, and on what

- **H2: DERIVED** from your 132 (READ, line 1065), carried as yours. No axiom is claimed. Green under the board's
  rule, with your carried ruling as its only input.
- **O1a: DERIVED** from your 132 with 130 (both READ). Green.
- **Z1q: PROVED.** Symbolic for general symmetric τ and general tension q [B6]; B5 checks the Gauss identity on two
  families. It rests on the Gauss equation and Israel's Z2 junction, standard-not-READ. That is the footing passage5d
  P2 and localbulk L1–L4 already use for warptheorem's PROVED Z1, B1 and B2. Green on that footing. Under b1_matter.py's
  stricter rule, where a green input must be READ or computed, the footing would need a READ.
- **B1q: PROVED** [B7], on the same footing; Codazzi ⟺ conservation, STRUCTURAL. Green on that footing.
- **B2q: PROVED (STRUCTURAL)**, localbulk L4's argument with general data; CK and constraint propagation
  standard-not-READ (b1_matter.py's B2′ carries the READ Dahia–Romero footing for the FRW case). Green on that footing.
- **On M1 (not green while M1 is OPEN):** G1, G3, O1b, O2, Z1t, Z2r, B2t and E4r, PROVED or DERIVED as conditionals
  [A1–A10, B3, B4, C10].
- **On M1 and M1-P2:** H2t.
- **Not greenable as stated:** Z2 (both legs, to infinity) and E4 (the exact E/4). They need M1-global, excluded in its
  exact form [C10]. They are carried by Z2r and E4r.
- **O1c (geodesic completeness): OPEN.**
- **M1: OPEN.** Its single-plane form fails at every computed grid point **on H-OWN-MATTER-ONLY** (computed and
  numerical: C2, C2b, C4–C7; READ: KR via the ground stage; standard-not-READ: the warped-product theorem). That
  reading is not ruled, and the cypher does not decide it (C11). Its bridge form is undecided (D1).
- **The theorem: not green.** F1 was a hidden non-green input of twelve lemmas, ten counted green-status and two (G1,
  G3) counted green. This audit replaces it with one explicit OPEN lemma, M1, and two stronger statements: M1-P2 (OPEN)
  and M1-global (excluded exactly). It greens five statements that never needed F1. And it takes G1 and G3 out of the
  green count until M1 is proved.

## Proposed rows for warptheorem.py (for the integration; not applied here)

- **G1, G3:** inputs gain M1 (M1-c at the horizon); statuses unchanged.
- **H2:** "the horizons hold the README as well as the throat", DERIVED from item 132 (carried as M's).
- **H2t:** "on each plane reading eq. (17), the horizon's trace is r = 2m with area N·A_bit", PROVED on M1 (P1) and
  M1-P2 (P2) (axioms.py).
- **O1a:** "one way, 1 → 2: a black hole in, a white hole out, different views of one object", DERIVED from items 132
  and 130.
- **O1b:** "no curvature singularity", DERIVED on M1 (M1-e).
- **O1c:** "geodesic completeness", OPEN.
- **O2:** "the corridor's bulk Killing horizon is degenerate", DERIVED on M1 (stability.py S1 plus the tangency lemma;
  KR p.4).
- **Z1q:** "for a Z2-symmetric plane of tension qσ_RS bounding the vacuum bulk, q·8πGτ(k,k) + κ₅⁴π(k,k) = R4(k,k) +
  R5(n,k,n,k); R5(k,k) = 0 in the vacuum bulk; our plane is q = 1", PROVED (f1_audit.py B5, B6).
- **Z1t:** the value along the mouth's radial ray, our leg, within the reach, PROVED on M1 (passage5d.py P2).
- **Z2r:** our leg's integral within the reach, to M1-c's order, PROVED on M1 (passage5d.py P3, coin.py).
- **Z2:** both legs to infinity, PROVED on M1-global and M1-P2 (M1-global excluded in its exact form).
- **B1q:** "a Z2-symmetric plane of tension qσ_RS carrying its own matter meets Gauss (−R4 = −12(q² − 1)/ℓ² + q·8πGτ +
  κ₅⁴(τ·τ/4 − τ²/12)) and Codazzi (D^μτ_μν = 0)", PROVED (f1_audit.py B7). To be reconciled with b1_matter.py's B1′.
- **B2q:** "for any analytic trace and matter meeting B1q a local vacuum bulk exists, unique among analytic ones",
  PROVED (STRUCTURAL). To be reconciled with b1_matter.py's B2′.
- **B2t:** its instance for eq. (17), PROVED on M1 (localbulk.py L3–L4).
- **E4r:** total − pull within the reach, (E/4)(1 − m/(2R\* − 3m)) to M1-c's order, PROVED on M1 (ledger.py).
- **E4:** the exact E/4, PROVED on M1-global (excluded in its exact form).
- **M1:** as stated above, OPEN, replacing input F1; **M1-P2**, OPEN; **M1-global**, excluded in its exact form.
- **B4b, B4d, B3:** F1 replaced by M1 in their inputs; statuses unchanged.

## Named hypotheses

- **Yours:** 129 (1), 130 (1), 132, 172 (1), 179/180, 183, 184, 187 (3), 194, 195, 196; your guess C (182) is cited as
  a guess.
- **The board's:**
  - **H-PLANE-READS-MOUTH** (ITEM179), here the theorem M1.
  - **H-OWN-MATTER-ONLY**: 184's recorded gloss with 129 (1)/130 (1). Our plane's matter at the mouth is ours alone,
    bounded by nuclear density. In tension with 172 (1); not decided by the cypher (C11).
  - **H-STRESS-INDEX** and **H-M1-TRACE-INDEX**: the cypher encodings.
  - **H-BK-FLUID-NOT-MATTER**: eq. (17)'s Bronnikov–Kim effective fluid is not plane matter (a gloss of 130).
  - **H-RH-IS-2M** (ITEM185): x = 2m/ℓ.
  - **H-EQ17-ON-P2** (stage 6), tested in C2b; its leg is M1-P2.
  - **H-POSITIVE-ON-P2** (ITEM185), in M1-f.
  - Your carried rulings as green inputs: the sibling convention (b1_matter.py's AXIOM_ITEMS). It means your carried
    statement, not an axiom you have declared.
  - The measure of M1-c's ε, our matter's 8πGρ/c² against eq. (17)'s radial tidal term.
  - b4_static's locally analytic class, where used.

## OPEN

- **The stress question** (below, for you).
- **M1's bridge form:** D1 above. **M1-P2:** position 2's side reading eq. (17)'s other leg, with README stress.
- **Non-static or non-analytic bulks.** M1 is static, and the write is not (O3, B4d).
- **Where the README is held.** Your 195's working reading, the README held by the horizon (its energy the horizon's
  mass), is about the horizon, not the plane's junction stress. Whether the held README's energy could supply the
  stress C4 needs is not computed; the redshift caution above comes first.
- **The rest of the cap family.**
  - The map A₀ → 2m/ℓ is monotone on the 12 computed points; between them this is not proved.
  - The crossing count covers six A₀ values.
  - All of C2b, C4 and C6 are fixed-step RK4 without error control, on the sampled points.
  - C2b's "no singularity" means none to y = 50m (evidence, not a bound).
  - The non-compact branch is checked only by a checking session's scan, not by this instrument.
- **H1 and H2's bulk form:** whether the throat's and the horizon's area of N bits is the plane's 2-sphere or a bulk
  3-area, for a horizon of the corridor's size.
- **The footing:** whether standard-not-READ Gauss, Israel and CK count as green footing (warptheorem's practice) or
  need a READ (b1_matter.py's rule). Recorded, not decided.
- **Verification of the READs.** Every READ here comes through `epass_ground.json`, ITEM185, b1_matter.py or cosmo.py
  and was not re-opened at source.

## The question for you

**May our plane carry the README's stress at the corridor's mouth while the corridor holds, as your 172 (1) allowed for
position 2's piece?** Options: "Yes, it may" / "No: our plane carries only our universe's matter" / "For the math".

Your 129 (1) and 130 (1) read against it as worded, and your 172 (1) shows they did not stop you on position 2's piece.
The cypher does not decide it (C11).

- **A "No"** keeps the single-plane form refuted at the computed points, and M1 must be the bridge.
- **A "Yes"** reopens the single-plane form, with C4's caps as its candidates. They need 1.7×10⁴¹ times nuclear density
  at the example README, to be compared with the README's own energy.

## History

- **2026-10-09, written for the green-the-chain round** (your 192–196). The instrument and the note were built and run in
  one session: selftest 30/30, mutants 23/23, every check failed by a mutation.
- **2026-10-09, checked by two separate AI sessions in this project, findings applied.** A refuter and an over-claim
  reader raised 25 findings (12 and 13). Each was reproduced first; all 25 were real and all were applied:
  - G1 and G3 added;
  - Z2 and E4 moved to M1-global, and H2t to M1-P2;
  - M1-c stated to an order with the bound computed, and M1-global excluded in its exact form;
  - H2 and O1a re-labelled DERIVED, not AXIOM;
  - Z1′/B1′ narrowed to Z2 planes and re-derived for general tension (now Z1q, B1q);
  - the cap start's c₃ corrected, with a constraint check;
  - both counts of ℓ₂ quoted;
  - Z2's inequality restricted;
  - statuses imported, not typed;
  - the cypher reading corrected, and the stress question put to the cypher;
  - wording narrowed throughout to what was computed.
  - Gates were tightened to the printed figures.

  The instrument now runs 36 checks: selftest 36/36 (about 25 s). `--mutants` runs 29 named mutations; every one
  fails at least one check, and every one of the 36 checks is failed by at least one mutation (about 1 min). The six new
  mutations are: c₃ over 10; SMS's π without its trace term; no dark energy; Z2 and E4 keyed to M1 alone; the stress
  cell seated; and G1, G3 read F1-free.
