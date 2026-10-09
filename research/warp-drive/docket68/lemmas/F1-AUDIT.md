# F1 audit: eq. (17) as our plane's own metric, across the ten lemmas that rest on it, and the one theorem M1 that would green them (computed, READ and deduced; not verified; not seated; 2026-10-09)

*First headed* "F1 audit … (computed, READ and deduced; not verified; not seated; 2026-10-09)". The instrument is
`f1_audit.py`: selftest 30/30 (about 25 s); `--mutants` runs 23 named mutations, every one fails at least one check,
and every one of the 30 checks is failed by at least one mutation (about 55 s). It imports its owners by path and
copies none: `bulk/stability.py`, `bulk/passage5d.py` (and through it `bulk/bulkseries.py`), `copy/coin.py`,
`copy/plane.py`, `copy/exactE.py`, `bulk/localbulk.py`, `lemmas/ledger.py`, `lemmas/b4_static.py`,
`lemmas/b4d_stage6.py`, `lemmas/axioms.py` and `tools/cypher.py`. It writes no file but its `--json` output. This note
and the instrument are the only files written. Nothing in `warptheorem.py` or `WARPTHEOREM.md` is changed; the
proposed rows are at the end, for the integration.

Labels: **computed** (by the instrument; check IDs in brackets), **READ** (verbatim, with page), **deduced**,
**STRUCTURAL**, **standard-not-READ**, **OPEN**. Your words are quoted verbatim; the board's readings are named H-….

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
- **172 (1):** you chose *"Yes, it may"*: position 2's piece may carry the README's stress.
- **182:** *"If I had to guess, I would go with C"* (the two-sided bridge). A guess, not a ruling.
- **192:** *"this appears to be a question to put to the math language hierarchy cypher"*. **195:** *"The README is not
  a pair"*. **196:** *"All questions get works through the cypher"*.
- **The round's task, from your 192 onward:** run the theorem's chain through the cypher and get it to go full green,
  *"even if it means new or edited lemmas"*.

## Plain words first

1. **Every F1 lemma still computes.** Each owner's decisive check was re-run and all ten pass [A1–A10]. The eight
   green-status ones are true statements about eq. (17) on a plane. What F1 decided was whether they are statements
   about *your* corridor. Under seated (G) they are, only if a plane really reads eq. (17) as the mouth's side view.
   That is the one theorem M1.
2. **Five statements can be green now, without F1:**
   - **H2**, the horizons hold the README as well as the throat, is your 132 word for word: an **AXIOM**.
   - **O1a**, one way, a black hole in at position 1 and a white hole out, is your 132 (with 130's "the mouth at
     position 1"): an **AXIOM**.
   - **Z1′**: on any plane, along every null ray, the plane's apparent null-energy deficit is exactly the bulk's pull
     plus the plane's own matter. It holds whatever the plane reads; **PROVED** (computed) [B5, B6].
   - **B1′**: every plane meets Gauss and Codazzi with its own matter (your 184); **PROVED** (computed) [B7].
   - **B2′**: for any such plane a local vacuum bulk exists, unique among analytic ones; **PROVED** (STRUCTURAL,
     localbulk's own argument with general data).
3. **Seven need M1** and wait on it: the horizon's area on the plane (H2t), "nonsingular" (O1b), extremality as a
   property of the bulk's horizon (O2), Z1's value along the mouth's radial ray (Z1t), Z2's Q, E4, and B2's instance
   for eq. (17) (B2t). **B4b and B4d lose F1 under M1 but stay non-green by their own status.** [C9]
4. **Two negative results, stated plainly (135).**
   - **Extremality does not follow from "the throat sits on the horizon".** Schwarzschild's throat does that with
     surface gravity 1/(4m). O2 needs eq. (17)'s particular form, or M1. [B3]
   - **M1's single-plane form is refuted near the horizon, on the board's reading H-OWN-MATTER-ONLY.**
     - Every regular single-plane static geometry whose plane reads eq. (17)'s near-horizon geometry needs plane
       matter at the horizon of about 0.66 (ℓ/2m) σ_RS. In the window that is at least 8 σ_RS; at the example README
       it is at least 1.7×10⁴¹ times nuclear density. [C4–C6]
     - That matter is positive and obeys the NEC, but it is never our universe's matter. The corridor would add it,
       which your 129 (1) and 130 (1) read against.
     - With no added matter the bulk is singular at SIM2's depth y_s [C2]. A matter-free negative-tension plane does
       no better in the window [C2b].
   - **So M1 survives only as a bridge:** your *"it only bridges them"* (179/180), your guess C (182). Position 2's
     piece must cap our plane's bulk before y_s. SIM2-FACING found that possible near the throat, with the README's
     stress on position 2's piece (your 172 (1)).
5. **Through the cypher (196)** [C8].
   - **On the board's index** of configurations whose plane trace is eq. (17), no language admits "single plane, our
     matter only, regular".
   - **The control** adds the non-extremal families READ in the matter round's route 1. Then every language admits it.
   - **What that means:** the obstruction is a three-way conjunction (extremal, regular and no added matter) that the
     closure languages cannot see from pairs. The computation is what excludes it.
6. **M1 is not claimed.** The first computation that would decide its bridge form is the whole position-2 piece
   (phase 2b-i), sharpened at the end of this note.

## The ten lemmas

Each lemma below is given (a) its statement, quoted in the heading from `warptheorem.py` (abridged), with its status
there; (b) where eq. (17) as the plane's metric enters; (c) what survives with the corridor in the bulk (179/180); and
(d) whether it is re-proved now or needs M1.

### H2: "the horizons hold the README as well as the throat" (DERIVED, axioms.py)

- **(b)** axioms.py H2 puts the horizon at eq. (17)'s F = 0, r = 2m, on the throat r₀ = 2m, with area N A_bit.
  [A1, computed]
- **(c)** On a plane that reads eq. (17), the horizon's trace is the sphere r = 2m, of area 4π(2m)² = N A_bit. In the
  bulk the horizon is a three-dimensional surface, and how its 3-area relates to N bits is not fixed without the bulk
  geometry (the black string's 3-area/(4G₅) equals the plane's 2-area/(4G); a small bulk hole's does not, deduced from
  the standard area laws, standard-not-READ).
- **(d)** **Re-proved now as an AXIOM:** the statement is your 132 verbatim (rulings file, line 1065) [B1, READ]. The
  quantitative form, area N A_bit on the plane, is **H2t**, which needs M1.

### O1: "one way, 1 → 2, nonsingular" (PROVED, plane.py P1; exactE.py)

- **(b)** exactE.py's z3 one-way check is the future cone at the throat in eq. (17)'s ingoing chart; plane.py P1 is
  eq. (17)'s causal structure. [A2, computed; both controls refuted]
- **(c)** Your 132 already says it of the corridor: *"one way by nature, a black hole in and a white hole out, side
  views of the same corridor object"*. With 130 (*"what the mouth at position 1 looks like"*) that is 1 → 2. On a
  plane that reads eq. (17), exactE's cone is that plane's view of it.
- **(d)** **Split.**
  - **O1a**, one way, 1 → 2: an **AXIOM** (132, 130) [B1, READ].
  - **O1b**, nonsingular: not ruled by you. It is M1's regularity clause, so it needs M1. Note that geodesic
    completeness was never computed even for eq. (17) (plane.py P1: *"Geodesic completeness is not computed: OPEN"*).

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
  - With F, H vanishing together, κ² = lim F′²H/(4F).
  - Schwarzschild (F = H, its Einstein–Rosen throat on the bifurcation sphere) gives κ² = 1/(16m²).
  - Eq. (17) at r₀ = 2m has H = O(F²), so κ = 0. [B3, computed]

### Z1: "5D null energy zero along the passage; plane deficit = bulk pull" (PROVED, passage5d.py P2)

- **(b)** P2 builds the bulk series on eq. (17) as the plane's metric with a matter-free plane (K = −g/ℓ), and reads
  R5(n,k,n,k) = −R4(k,k) = 2r″/r = (1/2)/((r − 3/2)²r) along the plane's radial null geodesic through the throat.
  [A4, computed; the passage5d foil breaks it]
- **(c) Under 179 the passage runs in the bulk, not on the plane.** What survives:
  - **"5D null energy zero" holds along any null ray of a vacuum bulk:** R5(k,k) = (2Λ₅/3)g(k,k) = 0 (axioms.py Z3's
    computation).
  - **The plane's deficit is the bulk's pull, for any trace.** The contracted Gauss identity
    R5(k,k) = R4(k,k) + R5(n,k,n,k) − K K(k,k) + (K·K)(k,k) [B5, computed on two unrelated families; the Gauss equation
    itself standard-not-READ], with Israel's K for a plane carrying matter τ [B6, computed symbolically for a general
    symmetric τ], gives
    **8πG τ(k,k) + κ₅⁴ π(k,k) = R4(k,k) + R5(n,k,n,k)**, with π SMS's quadratic term.
  - With your 129 (1)/130 (1) read as H-OWN-MATTER-ONLY, τ at the mouth is ours: at most 2.3×10⁻⁶³ of eq. (17)'s
    tidal term at r = 3m for the example README [C1, computed]. So "deficit = bulk pull" holds to that precision on
    any plane, whatever it reads.
- **(d)** **Z1′** (the identity) is **re-proved now** (PROVED, F1-free and F2-free). **Z1t** (the value 2r″/r along the
  mouth's radial ray) needs M1.

### Z2: "the integral equals the plane's reading on both legs" (PROVED, passage5d.py P3; coin.py)

- **(b)** Q = ∫R5(n,k,n,k) dλ = 8/(3m) − (4/(3√3 m)) artanh(√3/2) = 1.652872/m, exactly −2 × coin.py's per-leg
  reading, on eq. (17)'s radial ray. [A5, computed]
- **(c)** The integrated Z1′ holds on any plane: ∫[R4(k,k) + R5(n,k,n,k)] dλ = 8πG∫τ(k,k) dλ + O(κ₅⁴τ²). Under your
  183 (net per light ray), plane matter obeying the NEC can only add to the bulk's load: ∫R5(n,k,n,k) ≥ −∫R4(k,k).
  Deduced.
- **(d)** The value Q is a property of the trace, so it needs M1.

### B1: "the plane is matter-free (R = 0) and meets Gauss and Codazzi" (PROVED, localbulk.py L1–L2)

- **(b)** R(4) = 0 is eq. (17)'s own [A6, computed; SdS fails]; "matter-free" is input F2, which your 184 rules out
  as your configuration.
- **(c)–(d)** **B1′, re-proved now:** a plane at the RS tension carrying its own matter τ meets
  - Gauss: −R4 = 8πG τ + κ₅⁴(τ·τ/4 − τ²/12) [B7, computed symbolically, general symmetric τ; Israel and Gauss
    standard-not-READ];
  - Codazzi: D^μ τ_μν = 0 (conservation), STRUCTURAL.

  F1-free and F2-free. On a plane that reads eq. (17) (R4 = 0), the leading-order matter must be traceless; with our
  matter (≈ 0) B1′ reduces to L1. That instance is under M1.

### B2: "a local vacuum bulk exists, unique among analytic ones" (PROVED, localbulk.py L4)

- **(b)** The Cauchy data are eq. (17) with K = −g/ℓ; L3 shows them analytic through the horizon,
  dρ/du = 2√(m/2 + u²). [A7, computed; the owner's flags and an independent check at r₀; r₀ = 9m/5 fails]
- **(c)–(d)** **B2′, re-proved now (STRUCTURAL):** for any analytic trace and plane matter meeting B1′, the
  Cauchy–Kovalevskaya theorem with constraint propagation gives a local vacuum bulk, unique among analytic ones. This
  is localbulk L4's argument verbatim with general data (standard-not-READ, as there). The instance **B2t**, the bulk
  beneath eq. (17), needs M1.
- **A consequence worth stating** (deduced, in b4_static's locally analytic class): under M1, the corridor's bulk near
  our plane *is* b4_static's static bulk, to our matter's 10⁻⁶³. That bulk reaches a curvature singularity at
  y_b ≈ 2.49–2.50m above r = 2.15m (b4_static S2, Padé evidence). So **M1 forces some boundary, position 2's piece, to
  cut the bulk before y_b(r) over the throat.**

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
- **(c)** Under M1 the same plane data give the same bulk, so these results bind any plane that reads eq. (17). They
  are what forces the bridge form (C4–C7 below).
- **(d)** M1 removes F1 only. B4d stays OPEN: it is a five-dimensional evolution through the write, and M1 is static.

### E4: "the field energy outside the neck, total − pull = E/4 … the bulk's Weyl field read on the plane" (PROVED, ledger.py)

- **(b)** Misner–Sharp mass of eq. (17): M(R) = m + (m/4)(1 − m/(2R − 3m)), m at the throat and 5m/4 far away. "G = −E"
  uses a matter-free plane. [A10, computed; cross-checked with plane.py's Misner–Sharp at r₀; r₀ = 9m/5 fails]
- **(c)** This is a plane's-reading statement by nature: it is exactly what a plane that reads eq. (17) sees of the
  bulk's Weyl field. With our matter alone, G = −E holds to 10⁻⁶³.
- **(d)** Needs M1. **Caveat:** the exact E/4 needs eq. (17) out to the far field. That brings back ITEM179's
  γ = β = 5/4 against Garriga–Tanaka's γ = 1 (READ in ITEM185, GT eq. (27) *"when 'the other' wall (the one in which we
  do not live) is empty"*). Two thirds of the E/4 lies within 3m and 98% within 30m (ledger.py), so a reach-limited M1
  carries E4 to that share.

(**B3**, "a complete bulk exists", is equivalent to B4a–B4d. F1 enters it only through B4b and B4d.)

## M1, stated

**M1 (H-PLANE-READS-MOUTH, as a theorem; OPEN; not claimed).** For each README size N (m = G E(N)/c⁴, r₀ = 2m) there
are an ℓ in the window and a static five-dimensional spacetime 𝓑 such that:

- **(M1-a) vacuum bulk** (clause (B)): R_AB = −(4/ℓ²) g_AB on 𝓑;
- **(M1-b) the corridor exclusive to the bulk** (179/180): 𝓑 is bounded by our plane P1 and, in the bridge form
  (182), by position 2's piece P2; the corridor sits on neither;
- **(M1-c) the trace:** on P1, outside the corridor's horizon, the induced metric is eq. (17) at r₀ = 2m.
  - It holds out to the reach R\*. B4c's causality step already says eq. (17) *"holds only within the reach"*.
  - **M1-global** takes R\* = ∞ and meets the γ = 5/4 caveat;
- **(M1-d) no added matter** (184 with 129 (1), 130 (1); H-OWN-MATTER-ONLY): P1 carries the RS tension and its own
  universe's matter only, K = −(1/ℓ)h − (κ₅²/2)(τ − τh/3) with τ ours;
- **(M1-e) regular:** no curvature singularity in the closure of 𝓑, and a smooth Killing horizon of the static field
  ∂_t, which is tangent to P1;
- **(M1-f) P2 admissible:** its stress, if any (172 (1)), is positive (139 (2), as H-POSITIVE-ON-P2 reads it) and obeys
  the NEC, net per light ray (183).

**What it greens** [C9, STRUCTURAL; the board's green rule: PROVED, DERIVED or AXIOM, with no non-green input]:

| | green now (F1 an input) | after the edits, M1 OPEN | after the edits, M1 proved |
|---|---|---|---|
| the eight green-status F1 lemmas | none | H2, O1a, Z1′, B1′, B2′ | all edits: + H2t, O1b, O2, Z1t, Z2, B2t, E4 |
| B3, B4b, B4d | non-green | non-green | non-green (own status: OPEN, READING, OPEN) |
| M1 | — | OPEN | — |

So M1 is the one theorem whose proof greens every F1-dependent green-status lemma at once. It cannot green B3, B4b or
B4d, which are non-green for reasons of their own (O3, F4, F5 and the write).

## What is known for and against M1

**For:**
- **Local existence:** B2/B2′, the bulk beneath eq. (17) exists near the plane (computed L1, L3; CK
  standard-not-READ).
- **A regular region:** the static bulk is regular and Padé-stable in a region, with holds below 11.3 clocks; from
  r = 2.35m out, K stays below 2 to the grid's depth (b4_static S3, computed) [A8].
- **The degenerate horizon is consistent:** KR p.4 (READ above), and eq. (17)'s near-horizon AdS₂(2m)×S²(2m) is
  exactly KR's Q = 0 plane data (READ via the ground stage, deduced there).
- **A regular single-plane geometry exists at every 2m/ℓ** [C4]. Its only obstruction is the no-added-matter
  reading, not the geometry.
- **Near the throat the bridge passes:** SIM2-FACING, on its verified map (13 radii to 10m, nine ℓ), found facing
  allowed near the throat, in a band [y\*, y_s), with the README's stress on position 2's piece obeying the NEC.
  Positive energy needs ℓ ≥ 49.86m for a reached nearest point, or ℓ > 27.07m with an approach held at depth ≥ d₊.
  That is a necessary condition only (its own words: *"It does not say that such a piece exists."*).
- **The literature leaves extremal ones open:** FW 1105.2558 p.1 (READ in ITEM185): *"extremal solutions are thought
  to evade the non-existence conjecture"*.

**Against:**
- **Route 1 (ITEM185):** every READ static vacuum RS-II black-hole family cut by one positive-tension plane is
  non-extremal. KTN p.5: *"Assuming the surface gravity is nonzero (nonextremal)"*; the families have κr_h between
  about 1/2 and 1.
- **The vacuum-plane cap:** in KR's regular family the plane's charge reaches Q = 0 only as the horizon shrinks to
  nothing. READ via the ground stage, PDF pp.7–8: *"ρ0 and Q are monotonically increasing functions of A0 which vanish
  as A0 → 0"*. SIM2's Q = 0 throat bulk ends singular at y_s = 2.5536m (flat), reproduced here as 2.5535m, and 0.9138m
  at ℓ = m. [C2]
- **This note's near-horizon result:** with no added matter the single-plane form fails, and a matter-free
  negative-tension plane fails too, for ℓ ≥ 4.80m [C2b, C4–C6; next section].
- **The analytic bulk is singular:** b4_static S2 puts its singular surface at y_b ≈ 2.49–2.50m above r = 2.15m, so
  M1 needs P2 within that depth over the throat (deduced).
- **The far field:** M1-global meets γ = 5/4 against every READ linear law, which gives γ ≤ 1.
- **A caution, carried from the E-PASS ground stage and not re-read here:** Horowitz–Kolanowski–Santos find that
  tidal forces generically diverge at extremal horizons when Λ < 0.

## What plane matter eq. (17) would need (your 184)

With matter on the plane the trace need not be vacuum, so the board computed what it would need, from the Gauss
equation (B1′, Z1′) and three candidate bulks.

1. **The four-dimensional limit (bulk Weyl term zero).** The plane's matter must be G(eq. 17)/(8πG).
   - Its radial null part is R4(k,k) = −2r″/r < 0 at every r: −0.956, −0.2, −0.0741, −6.9×10⁻⁴ and −5.2×10⁻⁷ per m² at
     r = 2.01, 2.5, 3, 10 and 100m.
   - Its net over both legs of the ray is −Q = −1.652872/m.
   - So it breaks the NEC pointwise and net per light ray, against your 117/120 and 183.
   - It is also eq. (17)'s Bronnikov–Kim effective fluid, which your 130 says is not matter.
   - At r = 3m for the example README it needs about 10⁸⁰ kg/m³; our densest matter supplies 2.3×10⁻⁶³ of that.
   - **Inadmissible.** [C1, computed]
2. **The matter-free plane (Weyl term supplies all; Q = 0).**
   - Admissible as matter.
   - Its near-horizon bulk is singular at y_s [C2], and on a negative-tension plane, which is the growing side,
     H-EQ17-ON-P2 (stage 6 J3), it is regular to y = 50m only for ℓ ≤ 4.79m [C2b, computed]. It is singular from
     4.80m: 3.951m deep at ℓ = 8m, and 2.634m at position 2's own ℓ₂ = 3 × 27.07m.
   - Stage 5 F6's "regular on the evidence" was found in the range ℓ = m/2 to 2m and agrees; at window values it does
     not hold.
   - **No single matter-free plane carries eq. (17)'s near-horizon geometry regularly in the window.**
3. **The regular single-plane geometries (Kaus–Reall's ansatz).**
   - **The ansatz is general here.** Near a static degenerate horizon the bulk is a warped product (KR cite it as
     proved in their ref. [16]; standard-not-READ). With SO(3) that is KR's (2.2), *"ds^2 = A(ρ)^2 dΣ^2 + dρ^2 +
     R(ρ)^2 dΩ^2"* (READ, PDF pp.4–5, via the ground stage), with dΣ² unit AdS₂.
   - **The equations.** The instrument derives the bulk equations and the constraint itself, and checks that its
     integrator's right-hand sides equal them [NH, computed].
   - **The cap and the cut.** A compact horizon must close where R → 0 (KR p.5: *"In the bulk, compactness of the
     horizon implies that R(ρ) must vanish somewhere"*), smoothly by their (2.8). Integrating from that cap, the first
     radius where A = R is the only place a Z2 plane can sit and read AdS₂(L)×S²(L) with equal radii, which is
     eq. (17)'s near-horizon geometry with L = 2m.
   - **What Israel then says.** For AdS₂-invariant plane matter (energy ρ, tangential pressure p, and radial pressure
     −ρ by the symmetry): ℓA′/A = 1 − (ρ + 2p)/σ and ℓR′/R = 1 + (2ρ + p)/σ. KR's (2.16) is the Maxwell case p = ρ
     (READ). The constraint at the cut is then exactly SMS's trace equation [NH].
   - **Integrator controls [C3]:**
     - A₀ = ℓ is AdS₅ (A = ℓ cosh, R = ℓ sinh) and has no cut;
     - **A₀ = ℓ/2 is exact.** There A = ℓ/2, R = (ℓ/√2) sinh(√2ρ/ℓ), the cut is at L = ℓ/2 with ℓR′/R = √6, and the
       plane needs ρ = (2√6 − 3)σ/3 and p = (3 − √6)σ/3.
   - **The family, computed** [C4, C5]. One cut per cap, and none for A₀ > ℓ:

     | 2m/ℓ | ρ/σ_RS | p/σ_RS |
     |---|---|---|
     | 0.0044 | 150.1 | −39.5 |
     | 0.0439 | 14.13 | −3.09 |
     | 0.0739 (SIM2's edge) | 8.02 | −1.48 |
     | 0.178 | 2.83 | −0.178 |
     | 0.5 | (2√6 − 3)/3 = 0.633 | (3 − √6)/3 = 0.184 |
     | 1.72 | 0.0589 | 0.0500 |
     | 57.7 | 5.0×10⁻⁵ | 5.0×10⁻⁵ |

     - ρ > 0 and ρ + p > 0 at every cut, with ρ + p_r = 0 by the AdS₂ symmetry: **positive and NEC-obeying.**
     - **The limits.** ρ/σ → 0.6627 (ℓ/2m) as 2m/ℓ → 0 (the ℓ = ∞ cap). ρ/σ → (1/6)(ℓ/2m)² as 2m/ℓ → ∞, which is
       four-dimensional general relativity's Bertotti–Robinson matter ρ = 1/(8πG L²) (standard-not-READ), reproduced
       to 10⁻⁴.
   - **Against your 129 (1)/130 (1), on H-OWN-MATTER-ONLY** [C6]:
     - **In the window (2m/ℓ ≤ 0.0739) the plane needs at least 8.0 σ_RS**, and 1.3×10⁵ σ_RS at B4c's edge.
     - σ_RS is at least 7.2×10¹⁸ times nuclear density (ℓ ≤ 13.964 µm), so at the example README the need is
       1.7×10⁴¹ times nuclear density.
     - **Our matter would suffice** only for a mouth 2m ≥ 15 km, a README of N ≥ 4×10⁷⁸ bits. Item 108's full
       snapshot is 1.088×10²⁹. Even granting the upper edge away, ℓ would have to exceed 2×10³⁶ m.
     - **So the corridor would have to add the matter.**
   - **Two capped sides do not help.** Every cap has ℓR′/R > ℓA′/A at its cut. Two capped sides of a two-sided plane
     therefore cannot cancel their anisotropy, which stage 6 J1's matter-free condition Π_L = −Π_R requires.
     [C7, computed within the family]
   - **Verdict (deduced).**
     - A static, single-plane M1 needs added matter. Its premises: static, SO(3), the warped-product theorem, KR's
       regularity, a Z2 or two-capped plane, and H-OWN-MATTER-ONLY.
     - The added matter is positive and obeys the NEC. It is excluded by 129 (1)/130 (1) as the board reads them, the
       same reading ITEM185 gave X22's cap (*"needs README stress on our plane … which 129 (1) and 130 (1) read
       against"*).
     - Without added matter the single plane is singular. Hence the bridge.

## The question through the cypher (your 196)

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
  - Logic's binary: the plane matter is fixed by x.
- **Control** (designed to flip): add a coordinate "extremal" and route 1's READ non-extremal families as
  (x, 0, 1, 0). They cover the grid: Tangherlini, KTN, FW and AC-PYT; at x < 0.004 the Tangherlini limit, by
  ITEM185's scoping. Then every operator-bearing language admits **12 of 12**. Algebra and information admit the
  question as the join of a matter-free singular cell and a regular non-extremal one.
- **What the cypher says (the board's reading).** Within the eq. (17)-trace configurations, every language excludes
  the single-plane, no-added-matter, regular cell. Once objects of another kind are present, the languages combine
  "regular" from one with "extremal" from the other. The obstruction is a conjunction of three coordinates, which
  pairwise and lattice closures do not see. So the exclusion rests on the computation (C4–C6), not on the closures.
  No language fell silent on the question, and NOT-RUN is not counted as silent.

## The first computation that would decide M1

The single-plane form is decided (refuted on H-OWN-MATTER-ONLY). The bridge form is left, and its first decisive
computation is **D1, the whole position-2 piece**: SIM2-FACING's OPEN G and phase 2b-i, sharpened by B2's
consequence.

- **The bulk.** Use the static bulk beneath P1. It is unique in the analytic class (localbulk L4), and computed by
  b4_static.py and sim2_facing.py (banked: `b4_static.json`, `sim2_bank.json`).
- **Find a hypersurface P2: y = Y(r)** with:
  - (i) Y(r) < y_b(r) wherever b4_static's singular surface exists (r from 2m to about 2.35m);
  - (ii) its throat end in SIM2's band [y\*, y_s), or an approach held at depth ≥ d₊;
  - (iii) its Israel stress positive and NEC-obeying at every r. It is one-sided toward P1, with position 2's own
    bulk beyond (138), and carries the README's stress (172 (1)).
- **What decides:**
  - If no such Y exists on the verified map for any ℓ in the window, static M1 is refuted in the analytic class.
  - If one exists, M1's static existence is met in that class. That leaves the far field (M1-global's γ = 5/4), the
    analytic-class premise, and B4d's write.
- **What it needs first:** b4_static.json banks A, B and K but not C, the sphere's metric function that P2's
  extrinsic curvature needs, so the bank must be regenerated with C. SIM2's E-FAR/E-G (r ≈ 2.03–2.7m) is its first
  leg.

## Status earned, and on what

- **H2: AXIOM**, your 132 (READ, line 1065). No input.
- **O1a: AXIOM**, your 132 with 130. No input.
- **Z1′: PROVED**: computed [B5, B6]; the Gauss equation and Israel's junction, standard-not-READ (the footing
  passage5d P2 already used). No input.
- **B1′: PROVED**: computed [B7]; Codazzi ⟺ conservation, STRUCTURAL. No input.
- **B2′: PROVED (STRUCTURAL)**: localbulk L4's argument with general data; CK and constraint propagation
  standard-not-READ. No input.
- **H2t, O1b, O2, Z1t, Z2, B2t, E4**: PROVED or DERIVED as conditionals on M1 [A1–A10, B3, B4]. **Not green while M1
  is OPEN.**
- **M1: OPEN.** Its single-plane form is refuted near the horizon on H-OWN-MATTER-ONLY (computed: C2, C2b, C4–C7;
  READ: KR via the ground stage; standard-not-READ: the warped-product theorem). Its bridge form is undecided (D1).
- **The theorem: not green.** This audit turns F1 from a hidden non-green input of eight green-status lemmas into one
  explicit OPEN lemma, M1, and greens five statements that never needed F1.

## Proposed rows for warptheorem.py (for the integration; not applied here)

- **H2:** "the horizons hold the README as well as the throat", AXIOM, item 132.
- **H2t:** "on a plane reading eq. (17), the horizon's trace is r = 2m with area N A_bit", PROVED on M1
  (axioms.py).
- **O1a:** "one way, 1 → 2: a black hole in, a white hole out, side views of one object", AXIOM, items 132 and 130.
- **O1b:** "nonsingular", DERIVED on M1 (M1-e).
- **O2:** "the corridor's bulk Killing horizon is degenerate", DERIVED on M1 (stability.py S1 plus the tangency lemma;
  KR p.4).
- **Z1′:** "on any plane, 8πGτ(k,k) + κ₅⁴π(k,k) = R4(k,k) + R5(n,k,n,k); R5(k,k) = 0 in the vacuum bulk", PROVED
  (f1_audit.py B5, B6).
- **Z1t, Z2:** the values along the mouth's radial ray, PROVED on M1 (passage5d.py P2, P3).
- **B1′:** "each plane meets Gauss (−R4 = 8πGτ + κ₅⁴(τ·τ/4 − τ²/12)) and Codazzi (D^μτ_μν = 0) with its own matter",
  PROVED (f1_audit.py B7).
- **B2′:** "for any analytic trace and matter meeting B1′ a local vacuum bulk exists, unique among analytic ones",
  PROVED (STRUCTURAL).
- **B2t:** its instance for eq. (17), PROVED on M1 (localbulk.py L3–L4).
- **E4:** as stated, PROVED on M1; the exact E/4 on M1-global.
- **M1:** as stated above, OPEN, replacing input F1.
- **B4b, B4d, B3:** F1 replaced by M1 in their inputs; statuses unchanged.

## Named hypotheses

- **Yours:** 129 (1), 130 (1), 132, 172 (1), 179/180, 184, 187 (3), 195, 196; your guess C (182) is cited as a guess.
- **The board's:**
  - **H-PLANE-READS-MOUTH** (ITEM179), here the theorem M1.
  - **H-OWN-MATTER-ONLY**: 184's recorded gloss with 129 (1)/130 (1). Our plane's matter at the mouth is ours alone,
    bounded generously by nuclear density.
  - **H-M1-TRACE-INDEX**: the cypher encoding.
  - **H-RH-IS-2M** (ITEM185): x = 2m/ℓ.
  - **H-EQ17-ON-P2** (stage 6), tested in C2b.
  - **H-POSITIVE-ON-P2** (ITEM185), in M1-f.
  - b4_static's locally analytic class, where used.

## OPEN

- **M1's bridge form:** D1 above.
- **Non-static or non-analytic bulks.** M1 is static, and the write is not (O3, B4d).
- **Where the README is held.** Your 195's working reading, the README held by the horizon (its energy the horizon's
  mass), is about the horizon, not the plane's junction stress. Your 172 (1) placed README stress on position 2's
  piece, not ours. Whether the held README could appear as our plane's stress at the mouth is not your ruling and is
  not used here.
- **The rest of the cap family.**
  - The map A₀ → 2m/ℓ is monotone on the 12 computed points; between them this is not proved.
  - One crossing per cap is checked for A₀ = 0.6, 0.8 and 0.95 out to ρ = 10.
  - C2b's "regular" means regular to y = 50m (evidence, not a bound).
- **The bulk 3-area against N bits** for a horizon of the corridor's size (H2's bulk form).
- **The far field:** M1-global against the linear laws (γ = 5/4 against γ ≤ 1).
- **Verification.** Not verified. Every READ here comes through `epass_ground.json` or ITEM185 and was not re-opened at
  source.

## History

- **2026-10-09, written for the green-the-chain round** (your 192–196). The instrument and this note were built and run
  in one session: selftest 30/30, mutants 23/23, every check failed by a mutation.
- **Not verified.** Verifiers in both directions are next.
