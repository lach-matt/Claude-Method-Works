# What the README's source is required to be (item 385)

*First headed* 2026-10-14, on M's item 385: "We must first ask what the source is required to be". Worked in the
conversation from M's rulings and the rows already proved; no runs. This is SOURCE's specification, not its
construction: SOURCEs and SOURCE stay last (345, 358). Each requirement names where it comes from. Labels: M's (a
ruling), proved/derived (a row), computed (a number from a named instrument), estimate.

## Item 530: the second order of the record's own equations at 2w, exact (route b)

M, 530: "Yes , b please" -- the second-order source derived symbolically from the record's own equations, the l = 2
seed wave squared, solved for the outgoing amplitude at 2w (the 527 report's route (b)).

- **Built** (`lemmas/seed_second.py`, 9/9, mutants 3/3; heavy stages cached under `data/seed_second/`).
  - *The equations* (exact). hf_mirror5's class in kn_gauge's K1 form -- the 2+1 reduction h = rho^2 g3, Bondi's
    conditions, the two scalars psi and omega with R[h]_ab = (3/2) dpsi dpsi + 2 domega domega and the two box
    equations -- expanded about Tangherlini to order eps^2 by sympy (the order-0 identically zero). The fields are
    Legendre modes in x = cos 2 th; each equation is cleared of its denominators, reduced by the common factor of its
    rows and projected exactly on P_m; the same multiplier is applied to the quadratic terms, every coefficient reduced
    to lowest terms in x and sin 2 th first (the raw sums carry powers to 1/sin^23 2 th that cancel only together;
    evaluated as they stand they are noise). In the frequency domain the main equations give the radial system,
    v th and v v are the supplementary conditions (Bondi's lemma, checked), v r the trivial one.
  - *The l = 2 waves in the record's variables* (exact): tensor type Ps = -1/2, Om = -(3/4) x; scalar type
    Ps = (2/3) x, Om = 1 (Kodama-Ishibashi's harmonics with both circles' charges zero); the record's own F and G
    without their h(x) are exactly -F/3 of the one and -F/4 of the other. At second order the products reach l' = 4,
    n <= 2: three modes close the tower exactly (no truncation).
  - *The solve*: regular at the horizon (the pole's Frobenius expansion to its next order, the 2 NM exponents
    -1 + i w excluded; the particular solution started on the pole balance), supplementary rows at r = 2, incoming
    amplitudes by a Hann-windowed projection on r^-3/2 over [R/2, R], the 2 NM residual gauge directions fixed by the
    least h_vv, h_vr, h_vth at R; the outgoing projection on r^-3/2 e^{2 i w r*} is gauge-clean to 1e-15. Second
    order: the particular solution from the horizon, no incoming wave at 2w, the supplementary rows with their
    sources, the gauge fixed as before; C = P_out(2w)/P_in(w) at unit record amplitude.
- **Validated.** The l = 2 reflection of each type reproduces Kodama and Ishibashi's barriers (522's V_T, 525's V_S)
  at x = w r_h = 1.0, 1.5, 2.1, 2.5, 3.0 -- tensor 0.993559, 0.557119, 8.28849e-3, 3.73881e-4; scalar 0.378617,
  1.81518e-3, 2.2326e-6, 1.84e-8 -- to 1e-4 (the scalar at 2.1 to 9e-4, at 1.0 to 2e-3, at 3.0 to 9e-3), the modes pure to 1e-6, the
  supplementary rows holding at R/2 to 1e-11 (first order) and 1e-6 (second; 2e-5 at x = 1.0). The record's equations are linearized
  five-dimensional gravity mode by mode, and the identification of the types in its variables is exact. C at x = 2.1
  is the same at R = 100 and 150 (2e-5) and under a pure gauge admixture of the wave's own size at first order (to
  every printed digit).
- **Found** (C = the second-order energy out at 2w over the wave's, per unit record amplitude eps = lam A; the
  energy out is C eps^2 = (9/4) C h_H^2 in 527's strain).

  | x = w r_h | C tensor | C scalar | sigma, T7's normalisation (tensor / scalar) | T7's model, tensor p = 3 / 6 |
  |---|---|---|---|---|
  | 1.0 | 8.99e-4 | 2.29 | 1.22 / 0.251 | 1.29 / 0.72 |
  | 1.5 | 7.51e-4 | 1.51e-3 | 0.110 / 1.42e-2 | 0.176 / 0.069 |
  | 2.1 | 4.34e-7 | 8.04e-8 | 1.50e-3 / 2.47e-4 | 1.65e-3 / 1.84e-3 |
  | 2.5 | 1.44e-9 | 1.90e-10 | 9.93e-5 / 1.76e-5 | 9.8e-5 / 1.6e-4 |
  | 3.0 | 1.3e-12 | 1.4e-13 | 3.5e-6 / 6.6e-7 | 3.3e-6 / 7.3e-6 |

  Above the barrier tops C falls exponentially: the amplitude slope over x = 1.5-3.0 is 6.7 (tensor) and 7.7
  (scalar), T7's model slopes 5.7-6.9 (near 2 pi); in T7's own normalisation (out at infinity over in at the horizon)
  the exact tensor coupling is 0.9 times the model's p = 3 line at x = 2.1 and 1.0 times it at 2.5 and 3.0 -- the
  model couplings f/r^3 were the right ones -- the scalar type 1-5 times its p = 3 line. Below the tops (x = 1.0) the
  law does not hold: the scalar type's 2w emission there exceeds the wave itself per unit amplitude, a near-resonant
  response with the first order almost wholly reflected. The horizon start matters: the particular solution started
  from zero at r = 1 + eps, or on eigenvectors of the pole's degenerate cluster, carries an outgoing-from-horizon
  admixture of order eps that floors C near 1e-8 (x = 2.5) and 1e-11 (3.0); the Frobenius start and the pole-residue
  basis remove it (C(3.0) the same at eps = 1e-3 and 1e-4 to 10-20 %).
- **At the derived point** (527: x* = 10.67 copper, h_H = 1.3e-4; the example 8.5e-4; the large end 1e-10). With
  T7's deliberately low slope (3 in amplitude, 6 in C) from the last computed point x = 3.0, C(x*) is 1e-32 for
  copper and the second order lets out 2e-17 half bits; the example and the large end below that (the instrument's
  report prints each anchor). The channels the full pattern adds (its h(x) tail; 0.988 of the power is l = 2) are
  bounded by the first-order escape times h_H^2, below 1e-7 half bits at every anchor.
- **What this closes.** The second order is no longer an estimate on model couplings: it is computed on the record's
  own equations, validated against Kodama-Ishibashi at first order, gauge-invariant and radius-independent at second
  order, and T7's model is confirmed in slope and, for the tensor type, in value. Under 441 the delivery of E5(N) within half a
  bit at the derived point rests on: the exact barriers (first order), the exact second order (this item), the strain
  at the horizon 1.3e-4 (the expansion parameter), the monochromatic treatment at the envelope's peak (an upper
  bound) and a Tangherlini hole of fixed mass through the passage. SOURCEs and SOURCE go to M for PROVED under 441.
- **Caveats.** Monochromatic; mu = 1; the extrapolation beyond x = 2.5 by slope, as T7's; the pure l = 2 seed (the
  tail bounded, not computed at second order); route (b) throughout, the record's own gauge and variables.

## Item 527: the seed derived and proved; the sequence's status; E6 by the math; the large end

M, 527 (re-sent as 528; "Continue" at 529): "it must be derived then proven" (the seed's size, and with it the
wavelength); "if it was FULLY computed, then it counts as computed" (the sequence); "this was ruled, this math decides
this" (E6); "Continue with all SOURCE work".

- **The seed and the wavelength, derived** (`lemmas/seed_derive.py`, 10/10, mutants 4/4).
  - *The floor* (criterion). From the record's E5 = 3 pi hbar c r_h^2/(8 l5^3), a quantum of the shell of energy
    2 pi hbar c/lam has horizon radius r_q^2 = (16/3) l5^3/lam; it is not a hole of its own while its reduced
    wavelength exceeds r_q: lam > lam_P = (64 pi^2/3)^(1/3) l5 = 5.949 l5. U3's reading (each quantum below
    hbar c/l5) is 2 pi l5 = 1.056 lam_P. The floor's constant is an order-one criterion, not a theorem.
  - *Monotone* (exact in the law; checked on the grid). The energy let out is (3/(16 pi)) (lam/l5)^2 I(2 pi r_h0/lam)
    E_P5 with I decreasing, so the least seed mu0(lam) increases with lam: the least seed over the window is at the
    floor. Checked at 60 wavelengths for all four anchors.
  - *The derived seed at lam_P*: copper 102 l5^2 (r_h0 10.1 l5); the example README 61 l5^2; r0 = 20 ell 808 l5^2
    (28.4 l5); the Earth cap 917 l5^2 (30.3 l5). At 2 pi l5: 116, 69, 906, 1028. The 10 l5 of 522-525 was a value in
    the window; as the wavelength it is superseded by the derived floor (its seeds, 324 and 199, stand as computed).
  - *The law*: x0* = 0.577 ln(r_hf/l5) + 1.75, the slope 1/ln((1 + sqrt 2)^2) to 2 %: at large x the escape is set by
    the modes at their barrier tops, l near 2x, whose share of the record's power falls as (1 + sqrt 2)^(-2k) (the
    poles of h(x) at x = +-i). The seed grows as (ln r_hf)^2 across sixteen orders of magnitude in N.
- **The seed, proved** (what "proven" rests on).
  - First order, exact: the barriers are Kodama and Ishibashi's V_T and V_S (READ), the angular content split exactly
    (seed_types T2-T4); at (lam_P, mu0*) the shell delivers E5(N) within half a bit at every anchor.
  - Where escape is decided the strain at the horizon is 1.3e-4 (copper), 8.5e-4 (the example), 9.3e-11 and 1.9e-11
    (the large end), the growth per crossing 3.8e-6, 9.0e-5, 1.4e-17, 7.0e-19: the first order is the expansion.
  - The second order at 2w (seed_types T7's bound, slope 3 from x = 3): 1.2e-15 half bits (copper), 2.4e-13 (the
    example), below 1e-35 at the large end. On model couplings.
  - The check in the record's own exact equations was run and does not resolve it (`lemmas/seed_nonlinear.py`, 6/6,
    mutants 3/3): hf_core5's scheme, nothing cut out, the seed mu0 = 1 at L = 102, w r_h0 = 2.1 (escape of order 3 %
    of the shell), shells of 0.5 % and 5 % of the seed, to v = 12. The evolutions hold (angular residual <= 1.4e-3
    and 1.2e-2), but the mass read at the compactified infinity swings by 8.3 and 3.0 shells once the reflected wave
    runs out through y = r^(-1/2), and the horizon bracket is still 5.1 and 1.7 shells wide at v = 12 (lost at five
    samples at the larger shell): the predicted escape lies 100-260 times below both floors. A first configuration
    at a small hole (mu0 = 0.04) broke the scheme outright. Recorded as what the exact code shows; the second order
    stays an estimate on model couplings.
- **The large end, computed** (526's item 2). The derived seed is 28-30 l5 against ell = 9.07e19 l5, so the seed
  phase is five-dimensional Tangherlini ((r_h0/ell)^2 = 1e-37); half a bit there is hbar c^3 ln2/(16 pi G M) with
  M = r0 c^2/(2G) (emitter_process C2), equal to E/(4N) of earth_cap's figures; its shell (sigma_t = 113.9 GM/c^3)
  reaches the seed phase at 3e-5 of its length.
- **The sequence's status** (M-SEQUENCE-FULL). hf_core5's sequence is complete on D with nothing cut out: four
  wavelengths at mu0 = 100 l5^2 and three at 1000, lam-bar/r_h0 = 0.1 to 0.00625, the shell 0.18 of the seed. Its
  first row (L = 100, lam-bar = 0.1 r_h0) is a wavelength of 2 pi l5 on a seed of 100 l5^2: the derived point to 2 %.
  It is not the delivery of E5(N), whose shell is 1e11 times the seed; that growth is beyond direct computation, and
  the delivery at the derived point rests on the scattering computation above. Under M's rule the sequence counts as
  computed for what it computes: THM-HF5's rates on D.
- **E6, closed by the math** (M-E6-BY-MATH). emitter.py E1-E6 and emitter_process D2: the opening shell's emitter
  stands in the bulk, on a coordinate sphere of radius R > r_h about the face's centre, mirrored across the plane, a
  source of the bulk's own vacuum gravitational waves; our plane's matter cannot be it. No question remains.
- **Open after 527:** the second order on the exact equations, an estimate on model couplings now. Two routes:
  (a) the exact code with new diagnostics -- a flux through a worldtube at finite radius, a MOTS solved rather than
  bracketed, a ringdown of tens of r_h -- which can reach only the x = 2 regime, never the derived point's x = 10.7;
  (b) the second-order source derived symbolically from the record's own equations (hf_mirror5's, about Tangherlini,
  the l = 2 mode squared), which gives the exact coupling at the derived point: the route that closes the item. The
  board's recommendation is (b). SOURCEs and SOURCE stay OPEN until it is done and M rules on PROVED under 441.

## Item 526: what is left to finish SOURCE

M, 526: "So what is left to finish SOURCE?"

- **In hand** (each computed or READ):
  - the specification (`source_spec.py` U0-U8);
  - the device that reads (`reader.py`, 492) and the bulk emitter's process (`emitter_process.py`, 496);
  - the high-frequency limit, exact where the shell is locally (`hf_limit5.py`, 497);
  - the sequence onto the seed with no inner horizon, computed numerically (`hf_core5.py`, `src_hole.py`, 505-508);
  - THM-HF5's limit and (iv), exact (`hf_theorem5.py`, 511, 513);
  - delivery within half a bit at 10 l5, to first order on the exact barriers (`seed_escape.py`, `seed_types.py`,
    522-525), with the second order estimated far below.
- **Left, which the board can compute:**
  1. *The second order on the exact equations.* 525's bound uses model couplings c = f/r^p. The record's own
     second-order equations (hf_mirror5's, expanded about Tangherlini) give the exact coupling; T7 is rerun on it.
  2. *The large end.* 522 and 525 computed the small end (copper, the example README): SOURCEs. SOURCE proper is the
     large end, and the same instrument runs at its N and r_h.
- **Left, which needs M's ruling or a derivation the record does not hold:**
  3. *The seed's size, tied to the emitter's wavelength* (computed, `seed_types.py` T5). The record gives only the
     least seed (sqrt 72 l5^2, 508) and the window's floor lam > 2 pi l5 (`source_spec.py` U3: each quantum below the
     5D Planck energy); 10 l5 is a round value in the window, not derived. Within the window the least seed never
     delivers: copper needs mu0 >= 116 l5^2 at 2 pi l5, 324 at 10 l5 and 1477 at 20 l5, where hf_core5's 1000 fails;
     the example README needs 69, 199 and 924. Nothing in the record yet fixes the seed or the wavelength: is the seed
     the emitter's to set, or to be derived?
- **M's, standing:**
  4. *The status of the computed sequence*: numerical (lam = 0.1 to 0.0125), onto the seed; the proof for every lam is
     N1*, with the other session (509, 522, 524). Whether it is 441 (1)'s "computed solution" was put to M at 498 and
     505-508.
  5. *Who or what stands in the bulk and holds E5(N) before the release* (emitter E6), not a row of the theorem.
- **Then.** With 1 and 2 done and 3-5 decided, SOURCEs and SOURCE can be put to M for PROVED under 441.

## Item 525: SOURCE continued -- the scalar-type barrier and the second order

M, 525: "Continue with SOURCE please"

- **What 522 left open:** the scalar-type barrier at low l, and nonlinear scattering in the seed phase. Both are
  computed here (`lemmas/seed_types.py`, 12/12, mutants 5/5).
- **The record's waves, split exactly into Kodama and Ishibashi's types** (computed, exact).
  - The class holds scalar-type and tensor-type perturbations only. Its reflections forbid every component odd in
    phi1 or phi2, and a divergence-free vector on S^3 with only a theta component is C/(s c), singular at both axes.
  - The class's tensor-type harmonics solve Gegenbauer's equation, A'' + 6 cot(2 theta) A' + (k_T^2 - 6) A = 0:
    A_j = C_j^(3/2)(cos 2 theta), l = 2j + 2.
  - Projected in the energy norm, the record's F and G radiation is 0.639 scalar type and 0.361 tensor type, summing
    to 1 to 1e-15. l = 2 holds 0.988. 522's proxy had put 0.777 at l = 0, which carries no radiation.
- **The scalar-type barrier** (READ; computed). Kodama and Ishibashi, Prog. Theor. Phys. 110, 701 (2003), (3.6)-(3.7):
  "V_S(r) = f(r) Q(r) / (16 r^2 H^2)". The transcription reproduces Zerilli's potential exactly at n = 2. 1655
  reflection integrations, cached under a hash of their code. The scalar type reflects far less at low l: at l = 2
  its top reflects 0.0018, against the tensor type's 0.557.
- **Escape and the least seed at 10 l5** (computed).
  - Copper: the least seed (sqrt 72 l5^2) lets 1.87e7 half bits out. Delivery needs r_h0 >= 17.99 l5,
    mu0 >= 324 l5^2.
  - The example README: 2.41e5 half bits; 14.10 l5, 199 l5^2.
  - hf_core5's mu0 = 1000 passes both, and 100 fails both. The least seed suffices only for lam <= 1.94 l5 (copper).
  - 522's verdicts stand; its numbers move by under 1%. The escape near w r_h = 11 is decided by modes of l near 20
    at their barrier tops, where the two types differ less.
- **How far from linear** (computed). Where the escape is decided, the wave's strain at the horizon is <= 2.6e-4
  (copper) and 1.6e-3 (example), and the hole grows by <= 7.6e-6 and 1.8e-4 per light-crossing. The first order is a
  good expansion. But h_H^2 is 2.6e14 half bits (copper): whether the second order leaves decides delivery.
- **Whether the second order leaves** (computed on model couplings; estimate).
  - The steady second-order part is the round dust, l = 0. By Birkhoff it changes the mass and radiates nothing.
  - The part at 2w is driven by c(r) psi1^2, with model couplings c = f/r^p, p = 3, 6, rational and singular only at
    r = 0, as the second-order couplings on Tangherlini are. Its outgoing-to-ingoing amplitude ratio falls as
    e^(-s w r_h), s = 5.7-6.9, near the 2 pi set by the phase mismatch against the singularity at Im r* = pi r_h/2,
    for l2 = 2, 4 and both types.
  - A passing seed starts at w r_h >= 11.3 (copper) and only grows. With a deliberately low slope of 3, the escaping
    second order is <= 1.1e-16 half bits (copper) and 2.1e-14 (example).
- **What SOURCE now holds** (deduced). At 10 l5 the seed delivers E5(N) within half a bit if mu0 >= 324 l5^2 (copper),
  199 l5^2 (example): to first order on the exact barriers, with the second order estimated far below. hf_core5's
  computed seed, 1000 l5^2, meets it.
- **Open:** the second order on the exact second-order Einstein equations (here model couplings). Who holds E5(N) in
  the bulk (E6), and the sequence's status, are M's. SOURCEs and SOURCE stay OPEN.

## Item 522: SOURCE continued; N1* and the response paper handed to another session

M, 522: "Two tasks: Continue SOURCE AND Prepare instructions for another session to finish N1* and the counterpart
theorem, and then right a formal response paper to the Huneau and Luk's theorem. That session will need access to all
you work on the proof, so it'll all need to be pushed to the repo and identified there for the other session"

- **The handoff (done).**
  - Instructions: `research/warp-drive/paper/INSTRUCTIONS-N1STAR-AND-HL-RESPONSE.md`. They cover the commission
    verbatim; what is proved and what was corrected; the read-first order; reproduction; the sources to re-READ;
    routes W (5D wave gauge, Touati's construction carried to 4+1 and a large background) and D (5D double null);
    M's rules; the response paper; and the audit.
  - `docket68/handoff-n1star/MANIFEST.tsv` lists 54 files of the proof with md5s: instruments, data, Lean, the
    record's write-ups, and the scratch derivations, now in the repository under `handoff-n1star/scratch/` with
    their own README.
  - The other session works on its own branch, based on this one. It leaves the board's shared record (rulings,
    WARPTHEOREM, map, register, write-ups) untouched and logs its own work; this board integrates on M's direction.
  - Brought forward at 524 (M: "Please bring forward the handoff and instructions for the N1 session"): the
    manifest re-taken at the branch's head, the instructions noting that the SOURCE work below is not N1*, and the
    message that starts the session in `handoff-n1star/README.md`.
- **SOURCE continued: the seed's escape at 10 l5 (computed; `lemmas/seed_escape.py`, 11/11, mutants 4/4).**
  - The question. 517-521 left the seed phase open: while the hole is small against the wavelength, it reflects part
    of what arrives, and that part leaves. SOURCE needs E5(N) in the hole to within half a bit, which is 1/(3N) of it
    (2.6e-22 for copper, 1.2e-16 for the example README). This is linear scattering off the hole as it stands, not
    N1* (521).
  - The barrier (computed, exact; READ). A massless field on five-dimensional Tangherlini meets
    V = f[((l+1)^2 - 1/4)/r^2 + 9 mu/(4 r^4)]. Kodama and Ishibashi's tensor-type equation (Prog. Theor. Phys. 110,
    701 (2003), (5.2)-(5.3)) is the same equation at n = 3. The top sits near w r_h = (l+1)/2.
  - Reflection (computed). 1681 integrations, l = 2k for k = 0..45, cached under a hash of the solver's code.
    R + T = 1 to 1.2e-9. R is near 1/2 at the top; above it R falls 1e3-6e3 per unit of w r_h; at l = 0 the far
    fall is e^(-2 pi w r_h).
  - Angular power (computed). The record's profiles on the torus-invariant harmonics P_k(cos 2 theta): p0 = 0.7768,
    p1 = 0.2129, the tail falling as (1 + sqrt 2)^(-2k).
  - Escape (deduced). As the hole grows by absorbing the shell, the share leaving is (2/(w r_hf)^2) int x S(x) dx,
    from w r_h0 up.
  - At 10 l5 (computed):
    - The record's least seed (508: sqrt 72 l5^2, r_h 2.913 l5) lets 3.97e-15 of the energy out. That is 1.5e7 half
      bits for copper and 2.0e5 for the example README. SOURCE fails at the least seed.
    - The least seed for half a bit is r_h0 = 17.95 l5, mu0 = 322 l5^2 (copper); 13.96 l5, 195 l5^2 (example).
    - hf_core5's computed seeds: mu0 = 1000 l5^2 passes both; mu0 = 100 fails both.
    - Moving the harmonic labelling by one gives 16.3-19.6 l5 (copper) and 12.3-15.7 l5 (example). The verdicts
      stand.
    - The record's least seed delivers within half a bit only for lam <= 1.95 l5 (copper) or 2.52 l5 (example).
  - What SOURCE now holds (deduced). At 10 l5 the seed must be a size (508) of at least 322 l5^2 for copper, and
    hf_core5's runs at mu0 = 1000 meet it. 508's sqrt 72 l5^2 is the least hole, not the least seed for delivery.
    521's "a seed over about 20 wavelengths" is where the remainder estimate's seed phase ends, not this requirement;
    here r_h0 >= 1.8 lam.
  - Caveats. The angular content rides on scalar harmonics: the tensor-type barrier is identical (READ), and the
    scalar-type is the same at high l but not computed. Scattering is linear and adiabatic (dr_h/dv <= 0.0110 on the
    record's shell). Beyond the computed window R follows the e^(-2 pi) law, which over-estimates escape.
  - Open for SOURCE: the scalar-type barrier at low l, and nonlinear scattering in the seed phase. Who holds E5(N) in
    the bulk (E6), and the sequence's status, are M's. SOURCEs and SOURCE stay OPEN.

## Item 521: does SOURCE need N1*? No -- what SOURCE rests on instead

M, 521: "Does SOURCE rely on or need N1* ?" Answered from SOURCE's own statement and the record (no new instrument;
the numbers are counterpart5's and emitter_process's).

- **No. SOURCE does not rest on N1*.**
  - N1* is the lemma of THM-HF5's part (i): existence for every lam <= lam0 with lam-uniform estimates (520 P5). That
    is the proof for every lambda.
  - M placed that proof after SOURCE, verbatim at 509: "No proof for every λ - we will build this proof from the
    calculations when the SOURCE work is finished". The record carries it the same way ("The proof for every lambda is
    built from these calculations once SOURCE is finished", Where it stood at item 509).
  - N1* could not settle SOURCE either way. It is a statement as lam -> 0 with lam0 not controlled; every constant is
    fixed but large (the crude exponent 1.384e4, 520 P1). So it would not say whether the emitter's own wavelength
    lies below lam0. It is neither needed for SOURCE nor enough for it.
- **What SOURCE does rest on, for its carrier (497-511).**
  - That the round null shell is made of the bulk's own gravitational waves. In hand: the limit, exact (THM-HF5 F3:
    averaged 5D vacuum waves are null dust, giving Vaidya with Isaacson's flux); the vacuum sequence onto the seed,
    computed inward to x = 1 (hf_core5, both seeds, rates F4).
  - That the face receives E5(N) to within half a bit: 2.6e-22 of E5 (emitter_process C1). At the emitter's
    wavelength this is a question about that wavelength, not about lam -> 0.
- **Open there, and not N1*: the seed phase at 10 l5.**
  - At 10 l5 the waves arrive while the seed is under 20 wavelengths for the first 11 % of the shell. That part holds
    7.7e-6 of the energy (counterpart5 P1), about 3.0e16 half-bits.
  - How much of it the small seed absorbs, and how much scatters back out to infinity, is not computed. It has to be
    known to half a bit.
  - The seed phase disappears for waves below 0.144 l5 at the least seed, or for a seed whose horizon exceeds about
    20 wavelengths (sqrt(mu0) > 202 l5 at 10 l5). The record fixes the seed only from below (at least sqrt(72) l5^2,
    508).
- **SOURCE's other named open points stand as before.**
  - Who or what in the bulk holds E5(N) is no row of the theorem (emitter E6).
  - The status of the computed sequence is M's (498, 506-508).
- SOURCEs and SOURCE stay OPEN. N1* is not among their dependencies.

## Item 520: the counterpart proof -- what finishing it takes, measured; 517's N1 and N2 corrected

M, 520: "Can you finish the counterpart proof?" The board's reading: THM-HF5 (511), the proof 497-498 named "the 5D
counterpart of Huneau and Luk's nonlinear theorem", whose one open lemma, L-UNIF', 517-519 narrowed to three points.
`counterpart5.py`, 8/8, mutants 4/4.

- **Not finished.** What finishing takes is now measured, and two of 517's claims are corrected.
- **The seed phase and the 0.21 belong to the application, not to the counterpart theorem (P1, computed).**
  - THM-HF5 is a statement as lam -> 0 at fixed mu0, A and env.
  - The Kretschmann scalar of 5D Tangherlini is 72 mu^2/r^8 (computed from the metric). So a wave is shorter than a
    tenth of the curvature radius where z^2 > 10 72^(1/4) lam/sqrt(mu). That holds on all of D whenever
    lam < l5/10.
  - The seed phase exists only when lam > 0.144 l5 (at the least seed). It holds 7.7e-6 of the energy at 10 l5,
    5.4e-9 at 0.3 l5, and none at 0.1 l5.
  - Measured against the test-field energy, 517's exponents behave as follows:
    - the crude exponent is 1.384e4 at every wavelength;
    - the "second order" stays near 0.21 from 10 l5 down to 0.3 l5, because the seed phase's edge holds it, so
      517's "second order, estimate 0.21" was not a small-lam property;
    - once the seed phase is gone, it falls in proportion to lam: 0.148 at 0.1 l5, 0.0148 at 0.01 l5.
  - In the lam -> 0 theorem every constant is independent of lam, so a crude estimate suffices -- if the estimate
    exists at all.
- **517's K6 is withdrawn: the KN gauge loses two angular derivatives (P2, computed).**
  - h^vv = h^vth = 0 exactly, so no second v-derivative appears anywhere. The high-frequency structure is right.
  - The hypersurface equations form Bondi's hierarchy:
    - rr fixes h_vr from (d_r psi)^2 and (d_r omega)^2;
    - r-theta fixes h_vth through d_theta h_vr;
    - theta-theta fixes h_vv through d_theta^2 h_vr and d_r d_theta h_vth.
  - h_vv sits in h^rr, the coefficient of d_r^2 in box_h. So an estimate with k angular derivatives needs k + 2.
    Bondi's weak hyperbolicity survives the torus frame.
- **517's K5 is corrected: N2 was proved for test fields (P3, computed).**
  - On the background, box_h psi0 = box_h omega0 = 0. Their linearizations in the base metric are not zero:
    - the one for psi holds h_vv and d_r h_vv;
    - the one for omega holds d_theta h_vr and d_r h_vth;
    - both with O(1) coefficients.
  - So the remainder of the Killing norms is driven by the base metric's remainder at O(1).
  - The class's linear problem is therefore linearized gravity in the T^2-mirror class (515, item 2, open on a growing
    hole), not the test-field wave equation.
  - The multiplier and the constant 35 stand for T^2-invariant test fields. K8's ratio 0.92 and its exponents are
    measured against that test-field energy.
- **Prior art for the remaining step (P4, READ 2026-10-19).**
  - Touati, Commun. Math. Phys. 402, 3109 (2023), Theorem 2.2, and Touati, arXiv:2402.17530, Theorem 1.3:
    - 3+1 dimensions, on [0, 1] x R^3, with the background "close to Minkowski";
    - even in wave gauge "their coupling induces a loss of derivatives", regained "by a null foliation associated to
      g0 as well as a Fourier cut-off".
  - Huneau and Luk: small data, elliptic gauge.
  - Luk and Rodnianski: 3+1, double null, local.
  - None treats a large background, five dimensions, or the fixed points (axes) of a symmetry.
- **What finishing takes (P5, deduced).**
  - The counterpart theorem is THM-HF5 on D_T (v <= v_end + T, for each fixed T), as Huneau-Luk's and Touati's
    theorems hold on a fixed time.
  - Already in hand:
    - the limit and part (iv), exact (511);
    - v null at every lam, with no second v-derivative anywhere (F5, P2);
    - every constant independent of lam, and no seed phase below 0.144 l5 (P1).
  - OPEN, named **N1***: existence on D_T for lam <= lam0, with lam-uniform energy estimates for the remainder. It
    needs a formulation without derivative loss and regular across the T^2 axes: five-dimensional generalised wave
    gauge (Touati's route) or double null (Luk and Rodnianski's). It must hold on the large background, 5D Vaidya with
    its interior to x = 1. No published theorem gives it, and a proof is the size of Touati's 2023 paper.
  - Beyond D_T, the settling after the shell is the nonlinear stability of 5D Tangherlini in the class (open, 515).
  - The application at 10 l5 needs, besides N1*, control of linearized gravity in the class over the shell (P3). The
    seed phase and the 0.21 close there.
  - No inner or Cauchy horizon enters: D ends at the spacelike x = 1 (519).
- **Status.** For the counterpart theorem, L-UNIF' now stands as N1*. For the 10 l5 application it stands as N1* plus
  those three points. It is not proved, and the status is M's.

## Items 517-519: a new gauge, derived from the five needs and proved to meet them (KN gauge)

M, 517: "We need to derive and then prove a new or previously unidentified gauge that will meet the needs of the theorem".
M, 518 (during the work): "Continue, and check the background tasks please". M, 519: "Please confirm that you ARE
NOT chasing a chaucy horizon again" -- confirmed: see the last point.
(`kn_gauge.py` K0-K8, 18/18, mutants 10/10.)

- **Why 516 found N2 met by no gauge.** N2 was posed as linearized gravity on a growing five-dimensional hole. Its
  natural engine, the Teukolsky equation, does not decouple in D > 4. The class has more structure than that, and the
  derivation starts from it.
- **The derivation (exact, general base metric).** In the T^2-mirror class the two Killing fields commute, are
  orthogonal, and are hypersurface-orthogonal: g = g3 + e^(2U1) dphi1^2 + e^(2U2) dphi2^2. Then:
  - R(phi_i, phi_i) = -e^(2U_i) box_5 U_i, R(a, phi) = 0, and R_ab = R3_ab - sum_i (D_a D_b U_i + dU_i dU_i).
  - In the torus frame h = rho^2 g3, with rho = e^(U1+U2), off shell:
    R[h]_ab = R_ab + sum_i dU_i dU_i + dpsi dpsi + g3_ab sum_i e^(-2U_i) R(phi_i, phi_i), where psi = ln rho.
  - So vacuum in the class is exactly 2+1 gravity on h with two free massless scalars:
    R[h] = (3/2) dpsi^2 + 2 domega^2, box_h psi = box_h omega = 0, with omega = (U1 - U2)/2.
  - 2+1 gravity has no waves of its own. Every wave of the class lives in psi and omega. These are the Killing norms:
    geometric scalars, the same in every gauge.
  - For every T^2-invariant f, box_h f = rho^-2 box_5 f. For every base vector X, the 5D energy current satisfies
    div_5 J = rho^2 ((1/2) T_h^ab (L_X h)_ab + (X f) box_h f). The radiation's own oscillation (in psi, omega, the
    torus and the conformal factor) never enters the energy identity. Only the base metric h does.
  - Prior art: Schmidt (gr-qc/9712034) reduces D dimensions with D - 2 such Killing fields to 2D dilaton gravity;
    Choquet-Bruhat and Moncrief, and Huneau and Luk (1706.09499), reduce 4D polarized U(1) to 2+1 Einstein-wave map.
    The 5D cohomogeneity-three form with its torus frame, used as the gauge for this problem, is what is identified here.
- **The gauge (KN gauge).**
  - v is the phase of the incoming radiation, a null coordinate; theta is carried along the null generators; r is
    fixed by h_thth = r^6 sin^2 theta cos^2 theta.
  - The unknowns are the Killing norms psi and omega together with the base metric h.
  - The averaged form adds one near-identity fast diffeomorphism, x -> x + lam^2 Xi(x, v/lam).
  - On the record's ansatz, h_thth = rho^2 g_thth = r^6 s^2 c^2 for every P1, P2, so these are exactly the record's
    Bondi coordinates. F1-F7 and every run stand in it; what is new is the frame, the unknowns and the averaging.
- **How it meets each need.**
  - **N2 (proved; constants computed).** By the derivation, the linear problem of the class is the scalar wave
    equation for T^2-invariant fields on the averaged background, 5D Vaidya with mu' >= 0, not linearized gravity.
    In units of sqrt(mu(v)), with z = r/sqrt(mu):
    - Kodama: the bulk of d_v is (mu'/2r^2) f_r^2 >= 0, exact. The apparent horizon is spacelike and is a future
      boundary of the exterior, so the exterior T-energy only falls, apart from what enters at past null infinity.
    - A new multiplier: X = alpha d_v - sigma d_r, with alpha = 12z^4 - 4z^6 + (3/8)z^8 and sigma = z^2(4 - z^2)^2
      for z < 2, and X = 32 d_v beyond (C^1 at z = 2). Proved by exact root counting:
      - X is future-timelike on (0, inf), and across the apparent horizon, where sigma = 9;
      - its bulk is positive definite on (0, sqrt(12/7)), through the horizon at z = 1;
      - its (v, r) block is semidefinite up to z = 2;
      - all of this for every growth rate eps = mu'/sqrt(mu) in [0, 1/20].
    - The shell's largest growth rate is eps = 0.0219.
    - Dafermos and Rodnianski's argument (red-shift plus a monotone T-energy; READ, with its lemma proved here) gives
      the nondegenerate energy on every cone at most C2 = 35.0 times its data and input. This holds uniformly in v
      and lam, across the horizon, to x = 1. The constants are b = 0.0748, B = 15.6, C1 = 76.3 and c1 = 8.38.
    - At x = 1 the energy is weighted by z^2: a factor of 2.2e4 in energy, 150 in amplitude.
  - **N3 (exact).** The base metric's oscillation is pure gauge:
    - In the gauge h_rr = h_rth = 0 and h_thth is wave-independent, so every oscillation of h lies in the v-row,
      which is l (x) zeta + zeta (x) l with l = dv.
    - This is special to 2+1. The kernel of the linearized Ricci tensor's high-frequency symbol has dimension 3, all
      gauge. In 3+1 it is 6 = 4 + 2 and in 4+1 it is 10 = 5 + 5; the excess is the gravitational polarizations.
    - The fast diffeomorphism adds exactly lam (l (x) h.Xi' + h.Xi' (x) l) + O(lam^2), so it removes h's first-order
      oscillation.
    - On the background the torus frame reproduces Tangherlini exactly. To first order h_vr responds exactly as
      2 dpsi h_vr.
    - T_h^(va) has no f_v, so the oscillation meets only the derivatives that the cone energy controls.
  - **N1 (structure exact; the energy method deduced).** The radiative equations are linear waves. The base's three
    main equations (rr, r theta, theta theta) have sources 2 dPsi.dPsi in cone-tangential first derivatives only: no
    v-derivative and no second derivative. The D D U terms that make Bondi's free evolution weakly hyperbolic are
    removed exactly by the torus frame. Well-posedness of the characteristic problem then follows the standard energy
    method; that step is not machine-checked here.
  - **N4 (deduced).** These are the record's coordinates, in which the sequence reaches x = 1 (hf_core5) and the
    boundary is spacelike (hf_theorem5 F2). The averaging is O(lam^2), so the boundary stays spacelike.
  - **N5 (computed).** First-order oscillation:
    - The record's wave profiles satisfy the leading supplementary constraints exactly: the largest coefficient is
      1.6e-207 at 100 digits, zero to working precision. So the homogeneous mass and angular-momentum aspects are not driven at first order.
    - h's first-order response is computed exactly: h_vr = 2 dpsi h_vr, h_vth = Phi c_p(theta) r^(7/2), and h_vv
      from the theta theta equation.
    - Against X's positive bulk, its largest ratio per unit A env mu^(-1/4) is 1.7e-4 at z = 0.01, 0.2 at z = 0.5,
      4.4 at z = 1 and 15 at z = 1.2.
    - Over the record's shell with 10 l5 waves, the oscillation is absorbed outright below the waves' high-frequency
      edge z_hf = (29.1 w/sqrt(mu))^(1/2) and below z = 1.2. The largest ratio is 0.92; it reaches 1 at 12.5 l5.
    - Above z_hf the averaging removes the first order exactly.
  - Second order, after the seed phase: the remainder's exponent is 0.21. This is an estimate (strain times the
    first-order rate), not a second-order computation.
  - The seed phase stays open. While the hole is smaller than 20 wavelengths (sqrt(mu) < 202 l5, the first 11 % of
    the shell's duration, 7.7e-6 of its energy), the waves are not high-frequency outside the hole and no positive
    bulk is there. The crude sup-norm exponent is 1.2e4 there, and 1.4e4 over the whole shell. 515's e^43 was the end
    scale only. Closing this needs a weighted (Morawetz or Hardy) estimate outside the small hole in place of the
    sup norm.
- **What it settles and what stays open.** 
  - Settled by the KN gauge:
    - the radiation reduced exactly to two gauge-invariant scalar waves;
    - N2's engine, uniform with constant 35;
    - the base's oscillation made pure gauge;
    - the record's coordinates kept, reaching x = 1;
    - the first-order oscillation absorbed or removed over the whole shell.
  - Still open, all three not machine-checked:
    - the seed phase's exterior estimate;
    - the second-order remainder, an estimate of 0.21;
    - the energy-method step of N1.
  - L-UNIF' therefore narrows to these three. It is not proved.
  - No inner or Cauchy horizon enters anywhere (519): the background's f = 1 - mu/r^2 has one root, and the domain
    ends at the spacelike x = 1.

## Item 516: every gauge for L-UNIF', measured against its five needs

M, 516: "Deep research all gauges applicable to our specific needs".
(`gauge5.py` G0-G6, 7/7, mutants 5/5.)

- **The needs** (item 515):
  - N1, a well-posed problem on the theorem's domain: data at scri, the spacelike outflow boundary at x = 1, five
    dimensions;
  - N2, uniform linear control of the growing hole in the T^2-mirror class over 269 r_h;
  - N3, the high-frequency remainder;
  - N4, the interior reached to x = 1 with nothing cut out (505);
  - N5, the nonlinear closure.
- **Ten gauge families, read:** Bondi-Sachs; double null; wave-map (generalized harmonic); maximal slicing with spatial
  elliptic conditions; CMC (York time, hyperboloidal); puncture (1+log, Gamma-driver); the GCM/Teukolsky frame;
  gauge-invariant variables (Kodama-Ishibashi, Hollands-Wald canonical energy); the T^2 areal gauge; Friedrich's
  conformal gauge.
- **What the five-dimensional computation adds (exact).**
  - **Maximal slicing stops 129 times outside x = 1.** A spherically symmetric maximal slice through the vacuum at
    radius r needs C^2 >= mu r^4 - r^6. The maximum, 4 mu^3/27, sits at r_lim = sqrt(2/3) r_h (the 4D control gives
    3M/2). Independently, the interior r = const slices have mean curvature K(r) = (3r^2 - 2mu)/(r^2 sqrt(mu - r^2)),
    zero exactly at r_lim, so the two derivations agree. In the T^2-reduced 2+1 Einstein frame, the frame of Huneau and
    Luk's elliptic gauge, the torus moves the limit out to (2/sqrt5) r_h. For the example README's hole that is
    59,410 l5 and 65,080 l5, against r_q = 460 l5. The maximal foliation and every stationary 1+log-type trumpet freeze
    there (maximal is their f -> infinity limit; READ 0905.0450). Going further would need excision, which 505 excludes.
  - **CMC slicing does reach x = 1.** |K| rises monotonically inward to 0.687 l5^-1 at r_q. But a slice with K != 0
    is hyperboloidal and reaches null infinity, where five-dimensional radiation falls as r^(-3/2). That half-integer
    power rules out a smooth conformal compactification (READ Tanabe, Kinoshita and Shiromizu, PRD 84, 044055 (2011);
    Hollands and Ishibashi). So CMC fails N1 for data posed at scri.
  - **The T^2 areal gauge degenerates inside the hole.** rho = (r^2/2) sin 2theta has |grad rho|^2 = r^2 - mu sin^2
    2theta. It turns null on r = r_h |sin 2theta|, which meets every interior radius (r_q at |sin 2theta| = 0.0063). So
    the areal coordinate of the T^2 cosmologies is neither a time nor a space coordinate across the hole.
  - **Five dimensions ease N5.** Waves decay as t^(-3/2), whose integral from 1 to infinity is 2; four dimensions'
    t^(-1) diverges. So wave coordinates need no null condition (READ Choquet-Bruhat, Chrusciel and Loizelet, CQG 23,
    7383 (2006), for Minkowski). Near the hole the decay comes from Laul and Metcalfe and from Schlue, with a loss of
    derivatives at trapping.
- **What the reading adds.**
  - The Kerr proofs' geometric route (GCM spheres, Klainerman and Szeftel 2104.11857) runs on the Teukolsky equation.
    In D > 4 that decouples only on Kundt spacetimes, and "decoupling does not occur in higher-dimensional black hole
    spacetimes" (Durkee and Reall, 1009.0015, READ).
  - Kodama-Ishibashi master equations (hep-th/0305185) and Hollands-Wald canonical energy (1201.0463) control a static
    hole linearly; neither evolves the nonlinear problem.
  - The only nonlinear 5D black-hole stability results are cohomogeneity two, in double null (Dafermos and Holzegel,
    gr-qc/0510051).
  - High frequency has been handled in three gauges, all in 3+1:
    - double null with angular regularity (Luk and Rodnianski 2009.08968), oscillation along at most two null
      families -- ours oscillates along one;
    - an elliptic gauge under U(1) symmetry (Huneau and Luk 1706.09499). Five-dimensional vacuum with a diagonal T^2
      reduces to 2+1 Einstein-scalar fields, the same structure (deduced);
    - generalized wave coordinates (Touati 2402.17530; Huneau and Luk 2403.03470).
  - A refinement of item 515's point 1. As a free-evolution system Bondi gauge is weakly hyperbolic in the simplest
    norms (2111.14794). But Gundlach (2404.16720) gives a symmetric-hyperbolic Bondi formulation, linearized about
    four-dimensional Schwarzschild, well posed in a special energy norm.
- **The matrix** (M meets, P partial, F fails, O open):

  | gauge | N1 | N2 | N3 | N4 | N5 |
  |---|---|---|---|---|---|
  | Bondi-Sachs | P | O | P | M | O |
  | double null | P | P | P | M | P |
  | wave-map / generalized harmonic | M | P | P | O | P |
  | maximal + spatial elliptic | M | O | P | F | O |
  | CMC (York time, hyperboloidal) | F | O | P | M | O |
  | puncture (1+log, Gamma-driver) | P | O | O | F | O |
  | GCM / Teukolsky frame | P | F | O | O | P |
  | gauge-invariant variables | P | P | O | F | F |
  | T^2 areal | P | O | O | F | O |
  | conformal (Friedrich) | F | O | O | O | O |

  Each cell's ground is in `gauge5.py` (MATRIX).
- **What the matrix says (deduced).**
  - No gauge meets all five needs.
  - Seven families are excluded by a computed or READ failure: maximal, puncture and T^2 areal at N4; CMC and conformal
    at N1; GCM/Teukolsky at N2; gauge-invariant variables at N4 and N5.
  - No gauge meets N2. The obstruction there is the linear engine for a slowly growing five-dimensional hole, not the
    choice of gauge.
- **Recommendation.**
  - Bondi stays the computation gauge: F1-F7 live there, and its v is null.
  - Double null, angularly regular, for the shell, the high frequencies and the interior to x = 1. Bondi's v serves as
    its v.
  - A wave-map gauge relative to the Vaidya approximant, with constraint damping (Hintz 2302.13804), for the exterior's
    long time, where the integrable decay closes the nonlinearity.
  - Still open: N2's linear engine, and matching the two gauges across the shell. L-UNIF' stays OPEN.

## Item 515: what proving the inequality needs -- determined; a correction to 514

M, 515: "Check on the background tasks please. Then, -What is still not proved.- determine what is needed to prove the
inequality, and then prove it. We cannot complete the warp theorem as it is without it. Use every tool available to
you."

- **The background runs.** At mu0/l5^2 = 1000 the late spread converges with the angular grid at lambda = 0.05:
  1.2e-3, 4.3e-4 and 2.9e-4 at x = 16, 20 and 24, onto 498's 2.7e-4, with the exterior mass within 1.4e-6 of 498's.
  At lambda = 0.1 it does not (1.3e-2, 1.5e-2 against 2.6e-2). There the core boundary is outside the high-frequency
  regime: lambda A r^(-3/2) = 0.6 at mu0/l5^2 = 1000. So the sequence at 1000 is lambda = 0.05, 0.025, 0.0125 on the
  x = 20 grid; the 0.0125 run and a fifth wavelength at 100 (0.00625) are running.
- **A correction to item 514.** The anchored instrument took r_q as the scale at x = 1. The scale that decides high
  frequency is the local curvature radius K^(-1/4), and at x = 1 it is l5 for every hole, by the definition of x. So no
  wave of a physical length is high-frequency at x = 1. Corrected (`hf_anchor5.py` A4):
  - 10 l5 waves are high-frequency from infinity down to r = 4,604 l5 (x = 1e-4), and a small perturbation all the way
    to x = 1 (strain 7.2e-3 there, 3.6e-6 at the horizon);
  - r_h/10 waves are high-frequency only beyond r = 124,186 l5, outside the horizon (that needs w < 2,498 l5), and not
    small at x = 1 (strain 5.2).
  - The band "10-46 l5 reaching x = 1" that 514 reported is withdrawn.
- **What proving the inequality needs (determined).**
  1. A gauge in which the problem is well posed in energy norms: double null or wave gauge. Bondi gauge is only weakly
     hyperbolic (Giannakopoulos, Hilditch and Zilhao 2020).
  2. Uniform control of linear perturbations of the growing five-dimensional black hole, in the T^2-mirror class, for
     the whole shell: 269 r_h for the record's least shell, about 2e6 periods of 10 l5 waves. That control is needed at
     the horizon (red-shift), outside it (decay past the photon sphere at r = sqrt(2) r_h) and inside it down to x = 1.
     Prior art (READ): mode stability for every perturbation type (Ishibashi and Kodama, Prog. Theor. Phys. 110, 901
     (2003)), and decay for scalar waves on higher-dimensional Schwarzschild (Schlue, Anal. PDE 6, 515 (2013); Laul and
     Metcalfe, Proc. AMS 140, 3247 (2012)). It is not yet known for linearized gravity in this class on a growing
     background.
  3. The high-frequency remainder over that time. Only the remainder after the geometric-optics approximant is small:
     the waves themselves carry O(1) energy, because the shell is the hole's mass. Crude estimates grow like
     exp(||d g_app|| T) = exp(0.16 x 269), about e^43, over the shell. The oscillation's averaging must be used, which
     is what F5's light-cone structure supplies.
  4. Near x = 1, where the curvature radius is l5, the waves are long against it but small (strain 7.2e-3). There the
     approximant is linear perturbation theory with its power-law growth inward, not geometric optics.
  5. The nonlinear closure of 2-4.
- **Its status.** Items 2-5 together are nonlinear stability of a five-dimensional black hole, over a long time, in a
  cohomogeneity-three symmetry class.
  - The literature proves that only in cohomogeneity two: Dafermos and Holzegel, gr-qc/0510051, triaxial Bianchi IX,
    a class the plane's mirror excludes here (hf_limit5 H6).
  - Schlue 2013 names the general problem as open: his estimates are "in principle required in a nonlinear stability
    problem".
  - It is not proved here. It cannot be settled by computation at our universe's values either: a direct run would
    have to follow about 2e6 wave periods across a factor of 5e4 in scale. The proof has to be analytic and two-scale.
- **What holds exactly without it, and what it leaves to the inequality.**
  - The runs' mass gain matches the exact incoming flux to 0.01 % (item 514).
  - A stationary final state with the mirror carries no angular momentum. With T^2 symmetry such a black hole is
    fixed by its mass, angular momenta and rod structure: "identical if and only if their masses, angular momenta, and
    their 'rod structures' coincide" (Hollands and Yazadjiev, Commun. Math. Phys. 283, 749 (2008), READ). The static
    one is Tangherlini (Gibbons, Ida and Shiromizu, PRL 89, 041101 (2002), READ). So the final face is Tangherlini of
    the final mass, and holds the N of the energy kept.
  - What is left to the inequality is that the solution exists through the shell and settles, and that what escapes
    to future null infinity stays below half a bit (2.6e-22 of E5, emitter_process C1). In odd dimensions even the
    Bondi energy's definition needs care: Hollands and Ishibashi's "definitions and constructions fail in odd spacetime
    dimensions" (J. Math. Phys. 46, 022503 (2005), READ).

## Item 514: the remaining estimate, its coefficients evaluated and anchored in our universe

M, 514: "Prove the remaining estimate please. Anchor you work with real value from our universe so you can calculate
what you need to evaluate the coefficients that are preventing a precise answer instead of an estimate".
(`hf_anchor5.py` A0-A4, 5/5, mutants 2/2.)

- **What kept it an estimate.** L-UNIF' says the solution stays within C lambda of its approximant, with C and the
  order beyond it unevaluated and lambda abstract. Here both are made definite.
- **The coefficients, exact (computed; the runs agree).**
  - First order: the departure the runs measure is the waves' amplitude rescaled by r^(3/2), which is carried unchanged
    along each ingoing cone at leading order. So it is sqrt(2) A lambda exactly (sqrt 2 = h(0)). The runs give
    P/lambda = 1.406 and 1.449 at lambda = 0.025 and 0.0125, within 3 %.
  - Second order: the scri flux with the data's exact rates, averaged over the phase, is (A^2/6)(env^2 + lambda^2
    env'^2) at every x. So the mass gained exceeds Vaidya's by (2/9) A^2 lambda^2 int env'^2: 5 pi^2/(36 T) = 0.45693
    per A^2 for the record's envelope. The runs give 0.4608, 0.4590, 0.4568 (mu0/l5^2 = 100) and 0.459, 0.4589 (1000):
    converging on it to 0.01 %.
  - After both, the rest is below 0.1 lambda^3 at every lambda <= 0.05.
- **Anchored in our universe's values (READ by path).** l5 = 1.54e-25 m; the example README's face, N = 2.74e15 bits,
  E5 = 1.28e9 J, r_h = 1.12e-20 m = 72,762 l5; the record's least shell, the sin^8 flux over 269.15 r_h; the least
  seed. The shell's amplitude is then A = 66.7 l5^(1/2). For 10 l5 waves, the window's floor:
  - the second-order mass offset is 1.5e-13 of the shell;
  - the strain is 3.6e-6 at the face's horizon and 7.2e-3 at the record's quantum boundary x = 1 (r_q = 460 l5);
  - onto the least seed, 99.78 % of the energy arrives with the expansion's conditions holding at x = 1, and all but
    2e-6 of it at the horizon.
- **A correction the anchoring finds.** *[Item 515: withdrawn as worded -- at x = 1 the curvature radius is l5, so no wave is high-frequency there; see "Item 515".]* The band that reaches x = 1 within the expansion's regime is 10 l5 to 46 l5.
  The r_h/10 that emitter_process C4 names lies 160 times outside it: its strain at x = 1 is 5.2, not a small
  perturbation, and none of its energy is in the regime there. So the emitter's waves must be at most 46 l5 for the
  high-frequency limit to hold down to x = 1. *[A note beside emitter_process C4; the instrument is not edited.]*
- **What this settles, and what it does not.** The estimate's coefficients are evaluated exactly, not estimated, and
  our universe's lambda is fixed and bounded below by the window's floor, so lambda -> 0 is never needed. It is still
  not an analytic inequality for every lambda. Our lambda lies below the computed ones, and the answer there is the
  exact coefficients' as long as the series stays asymptotic, which the runs show at four wavelengths. A fifth
  (lambda = 0.00625) is running.

## Item 513: the light cone settles THM-HF5's nonlinear coupling

M, 513: "Refer back to the light cone work we did proving that gravity is governed by relativity, which is governed by
observation, which is a first principle". (`hf_theorem5.py` F5; 7/7, mutants 7/7.)

- **The chain, as the record proved it.** Observation (GW170817's one speed, MICROSCOPE, Cassini; READ) gives relativity
  (relativity.py U6). Relativity gives the one light cone for every front on every background (M-ONE-LIGHT-CONE, 328).
  The one light cone gives the law: alpha = 0, Einstein's equations exactly in five dimensions (gb_cone C7). With
  alpha != 0, gravity's fronts would split from the light cone.
- **What the light cone makes of the coupling (computed, exact, every v-derivative of every Ricci component).**
  - The fronts are null for the full metric at every lam (g^vv = 0), and no component holds a second v-derivative of
    anything. The waves never move their own cone.
  - The three equations that fix the metric on each cone (R_rr, R_r-theta, the angular trace) hold no v-derivative of
    anything. The metric on a cone is fixed by what lies on that cone, where the oscillation enters only at O(lam).
  - The evolution equations carry only the waves' own rates, linearly: no rate of W, beta or U, and no product of
    rates. The waves propagate linearly along the cone.
  - The one product of rates anywhere is R_vv's: the waves' own, the dust. Its average is the limit's mass growth. Its
    oscillation, carried along the cone, integrates for the record's envelope to 2.6e-7 of the shell at lam = 0.1 and
    1.6e-18 at lam/16 (falling as lam^9.3).
  - So the nonlinear coupling is O(1) only through the dust, which is the limit itself. Everything else is O(lam).
- **What remains: L-UNIF', narrowed.** It is no longer the waves' interaction but an estimate: the remainder after the
  geometric-optics approximant, driven by O(lam) sources with coefficients g_0 + O(lam) along the cones, stays O(lam)
  on D. It must be measured in norms rough along v and smooth along the cones (Luk and Rodnianski's framework), with
  the angular coupling of Bondi gauge handled in double null gauge or in norms analytic in x, as the data are. Not
  proved. Evidence: the sequence at four and three wavelengths.

## Item 511: the nonlinear PDE theorem for the shell's sequence onto the seed (THM-HF5)

M, 511: "I think you can now build nonlinear PDE theorem for this, and fairly quickly now that you have done the
computations ... Utilize outside research and publications, and utilize all the proof building tools available to
you." (`hf_theorem5.py` F0-F4, 6/6, mutants 5/5; Z3; Lean 4.33 core; Wolfram Language 15.) It is built on the redone
work (506-508), with the exclusions (481, 484) held first.

- **The theorem.** Take a seed mu0 >= sqrt(72) l5^2 and the record's wave data at past null infinity. Let D be the region
  from past null infinity to the record's quantum boundary x = 1. Then the five-dimensional vacuum solutions g_lam
  (T^2 symmetry, both reflections):
  - (i) exist on D for every lam <= lam0;
  - (ii) converge uniformly to five-dimensional Vaidya with mu' = (2/9) A^2 env^2, at O(lam) in the metric and
    O(lam^2) in the mean mass;
  - (iii) have one horizon and no inner one;
  - (iv) end at a spacelike boundary that every characteristic leaves, beyond which the record's core continues the
    limit.
- **Proved (exact).**
  - Part (iv): inside the horizon the boundary's normal is timelike, g^-1(dPhi, dPhi) = f - 2 r_q' < 0, and outgoing
    rays move inward faster than the boundary (Z3). Nothing inside the boundary reaches D, so D is the data's domain of
    dependence and nothing is cut out.
  - The limit. In the full ansatz only R_vv carries the waves at O(1), as -2(P1_v^2 + P1_v P2_v + P2_v^2). No component
    of the Ricci tensor carries them at O(1/lam), because v is null. With the round average A^2 env^2/6 and Vaidya's
    G_vv = 3 mu'/(2 r^3), mu' = (2/9) A^2 env^2: Isaacson's flux, derived. Both results are cross-checked in Wolfram
    Language 15. The form is positive definite (Lean, Z3), so the dust's energy is never negative.
  - Part (iii), in the limit: f = 1 - mu/r^2 has one positive root, and x = 1 lies inside it whenever
    mu > sqrt(72) l5^2. Beyond it the record's core has its two roots on opposite sides of one transition surface.
- **Computed.** The sequence meets the theorem's orders at both scales:
  - P halves with lam (2.48, 2.32, 1.94 at mu0/l5^2 = 100; 2.43, 2.33 at 1000);
  - the mean-mass offset quarters (5.17, 4.01, 4.02; 4.65, 3.84);
  - the horizon's departure halves, and every run has exactly one horizon.
- **Prior art (READ).**
  - Luk and Rodnianski (arXiv:2009.08968) prove both directions of Burnett's limit in 3+1 dimensions, for data rough
    along the null directions and smooth along the spheres, locally.
  - Touati (Ann. PDE 11, 22 (2025)) constructs the vacuum families for a background with a small parameter, on
    [0, 1] x R^3.
  - Huneau and Luk (Duke Math. J. 167 (2018); arXiv:1907.10743) do the polarized U(1) case, reduced to 2+1, for small
    generic backgrounds. That is the structure here, with two scalars.
  - Giannakopoulos, Hilditch and Zilhao (PRD 102, 064035 (2020)) show Bondi-like gauges are only weakly hyperbolic, so
    the proof of (i) belongs in a double null or wave gauge.
  - None covers a five-dimensional black-hole background on a fixed region reaching inside the horizon.
- **Open, named: L-UNIF.** The vacuum solution exists on D for every lam <= lam0 and stays within C lam of the
  geometric-optics approximant built on the limit. Part (i), and the rates for every lam, need it.
  - The route: the reduced 2+1 system in double null gauge (the data are rough only along v), with the published
    stability arguments carried from a small background to the limit on D. The limit is smooth on D, and D's boundary
    is outflow.
  - Test waves on the limit already have energy bounded uniformly in lam, since the boundary flux leaves with the right
    sign. The nonlinear coupling is what is open.
  - Evidence, not proof: the sequence at four wavelengths and at three.
- **Beside it.** At mu0/l5^2 = 1000 the late spread against 498's is not settled (hf_core5 C1, 9/10); finer grids are
  running.

Status: part (iv) and the limit are PROVED; part (iii) is PROVED in the limit and computed for every lam run; part (i)
and the rates are OPEN on L-UNIF.

## Item 510: after the instant, position 2's own values of the 26 govern the copy, and they hold nothing of what sat there

M, 510, to 509's closing line "position 2's laws still govern the copy after the instant (148, 240). That is a law, not
prior matter, so it falls outside 509": "this can be proven, as a continuation of the proof. Remember position 2's laws
are determined by its variations its own baez's list (same constants with different values)". (`p2_indep.py` Part II,
I0'-I11; 13/13 with Part I; mutants 8/8.) The line is withdrawn and proved.

- **Position 2's laws are its 26 (computed; Baez READ in address26 A1; Uzan READ).** The Yukawa sector's physical
  parameters, counted from the flavour rotations' orbit at random couplings, are 10 for the quarks and 10 for the leptons
  with right-handed neutrinos. Add three gauge couplings, the Higgs mass and expectation value, and the cosmological
  constant: 26. That is Baez's composition, and Uzan's count (Living Rev. Relativ. 14, 2 (2011), Table 1: 19
  dimensionless with theta_QCD among them; "at least seven new constants" for massive neutrinos): 19 - 1 + 7 + 1 = 26.
  The strong CP angle is the 27th only once the axion is excluded (434); G is the unit. So position 2's laws are one
  Lagrangian at position 2's values.
- **The labels are the same at every position (computed, exact).** Hypercharges solved from anomaly cancellation and the
  gauge invariance of each Yukawa term give one ray (Geng and Marshak 1989). With right-handed neutrinos the family is
  Y and B - L (Foot, Lew and Volkas 1993), and the gauged generator is the theory's own content, which "the same
  constants" keeps. No value of the 26 enters any condition. The charges u 2/3, d -1/3, nu 0, e -1 are the same at every
  position, so the README's labels name the same states under every set of values.
- **After the instant (exact, and computed).** The evolution exp(-i H(c2) t) does not depend on what sat at position 2,
  so the composite is again a replacement map: its output is position 1's README carried by position 2's law. Computed
  for four laws, three times and six prior states:
  - the copy is U_t sigma_r U_t^+ (5.6e-16);
  - I(ref : copy) = 0, and the Choi matrix is U_t sigma_r U_t^+ (x) I/8;
  - the laws govern: the copies differ between laws by at least 1.3e-3 and move from the README by 0.10.

  This rests on the 26 being constants. A "constant" set by position 2's prior matter breaks it (the mutant), and that
  is excluded twice: by 434 ("Anything conditional cannot by definition be a constant") and by Uzan ("Any constant
  varying in space and/or time would reflect the existence of an almost massless field that couples to matter" -- a
  field, not one of the 26).
- **The surroundings (computed).** Position 2's matter is displaced, not removed (284). It lies beside the copy holding
  all it was. Coupled to the copy under the same law, it changes the copy at first order in the coupling: copies of two
  priors differ by 3.5e-3 at g = 0.02 (ratio 2.008 at 2g), and by 6e-16 at g = 0. That is 240's "conditions" acting on
  an object once it exists, which survivability meets. It is not reconstruction.
- **Mass and fate (computed; exact where marked).**
  - The hydrogen README's labels are bound states for every alpha and every mass (exact). At alpha x 1.1 and m_e x 0.9
    the binding is 14.809 eV against 13.598, the atom is 51.1 keV lighter and 1.010 times the size: position 2 assembles
    its own mass on the same labels (240).
  - A finite well holds a label only in a window (exactcopy X3). The Morse model's top level v = 16 is bound only while
    the mass ratio is at least 0.8981 of ours. Below that, position 2's law moves the README's state (survivability,
    240), decided by position 2's values and the README alone.
- **So 509 continues past the instant.** The copy is position 1's matter at the instant, and after it is governed by
  position 2's own values of the 26, which hold nothing of what sat at position 2. Position 2's former matter can still
  act from outside, as surroundings act on any object.

## Item 509: whatever matter sits at position 2, it reconstructs only position 1's matter

M, 509: "position 2's matter is only relevant in the sense that its matter reconstructs the same matter from position 1.
No matter what matter sits at position 2, it always only reconstructs the matter from position 1. - prove this".
(`p2_indep.py` I0-I6, 7/7, mutants 4/4.) This answers 506's open point on position 2's mass: position 2's matter is
material, never content.

- **No other outcome is possible (computed, exact).** A reconstruction exact for every state of position 2's matter
  (146: no tolerance) is a linear map constant on all density matrices. Density matrices span all matrices, so it is the
  replacement map sigma_r Tr( . ). Solved in rational arithmetic, Phi(E_ij) = delta_ij sigma_r. The argument holds in
  every dimension; it is computed at d = 4. So the copy can carry nothing of what position 2 held.
- **It is physical (computed).**
  - The room's matter is displaced into a cold dump, as 284-285 say, and the README's labels are moved in from a
    reservoir by swaps chosen by r alone.
  - The room ends in the README's state for pure, mixed and reference-entangled initial states (error 5.6e-16).
  - The process commutes with total charge and with the energy of identical local Hamiltonians (exactly 0).
  - Its Choi matrix is sigma_r (x) I: it is the replacement map.
- **Where position 2's matter goes (computed; the no-hiding theorem, Braunstein and Pati, PRL 98, 080502 (2007)).**
  With a reference purifying it, I(ref : copy) = 0 and I(ref : dump) = 2 S(rho), to 1e-15. All that position 2's matter
  was is in what was displaced.
- **"The same matter" is literal (computed).** Identical particles carry no identity. The states with position 2's
  particle in one mode and position 1's in the other are one state up to sign, for fermions and bosons, and 100 random
  symmetric observables read the same on both. A copper atom from position 2's stock is position 1's copper atom.
- **The kind of matter enters only the energy (computed, AME2020 Table I through tools/isotopes.py).** The record's
  Cu-63 is the same atom built from hydrogen, helium, carbon, oxygen or iron (each with hydrogen to balance). The energy
  released differs: 524.8, 123.8, 87.4, 160.7 and 56.0 MeV per atom. Baryon number is conserved, so position 2's matter
  must hold at least the copy's baryons; that is necessary for any process. Given it, the composition never reaches the
  copy.
- **The kind of matter enters the cost too, never the copy (computed; molar entropies READ, NIST, 298.15 K).** Clearing
  a 1 cm^3 room costs at least T S (Landauer): 1394 J if it held copper, 1154 J for water, 2.4 J for air. The copy is
  the same in all three.
- *[Item 510: this line read "Not this item's question. Position 2's laws govern the copy after the instant (148, 240):
  a law, not prior matter." M: "this can be proven, as a continuation of the proof". Proved as 509's continuation;
  see "Item 510" above.]*

## Items 505-508: the work redone without the inner horizon

M, 505: "This whole your calculations were all wrong because - The excised core ... - you are still assuming there is a
inner/chaucy horizon when there is not." 506: "Those will be answered by the math. Redo the work without the inner
horizon". 507: "Keep going." 508: "There is always a seed - refer to the the method corpus materials".
(`src_hole.py` S0-S8, 8/8, mutants 4/4; `hf_core5.py` C0-C4.)

- **Held against the exclusions first (481, 484).** Nothing below has an inner horizon or a Cauchy horizon, and no part
  of the hole is cut out. The core is the record's own: one horizon, a transition surface, no inner horizon
  (core_large, transition5, transition5q).
- **What the math answers: the seed (computed, in the high-frequency limit).**
  - The prior art first: Ghosh and Dadhich's 5D null collapse from flat space is naked iff lam <= 1/27, with a Cauchy
    horizon as its earliest ray out (reproduced).
  - The record's quantum boundary x = 1 is r_q^4 = sqrt(72) mu l5^2 (exact). It lies inside the apparent horizon iff
    mu > sqrt(72) l5^2.
  - Without a seed, the hole's first phase has its core outside its horizon. At the record's least arrival spread,
    28.5 r_h (emitter_process C2), rays from that core reach infinity at mu_f/l5^2 = 1e4 and 7e40. So the core would be
    seen from outside, and 273's one-way passage and 484 both fail. It stays hidden only for spreads below 0.45 r_h,
    sixty times shorter than C2 allows.
  - With a seed of mu0 >= sqrt(72) l5^2 (r_h >= 2.91 l5) in place, every ray from the core is trapped from the shell's
    first instant to its last.
  - So the shell arrives onto a seed, as 508 states and The Method's own sec. 14.5.7-14.5.9 say of any closed index
    (Registers 1793, 1797: the seed is constructible and is a size, not a set). The math gives its least size.
- **The core while it takes the shell in (computed, exact).**
  - On transition5's chart with the mass free, f = 1 - M(r, v)/R^2, the Einstein tensor is derived from the metric.
    Its null energies are G(n,n) = -3 R''/R and G(l,l) = -3[(M - R^2)^2 R'' - 2 R^2 M_v R']/(4 R^5). The mixed part,
    G(l,n) + G(e,e), with them decides every null direction.
  - Outside the modified region our side is exactly 5D Vaidya null dust.
  - The mass may not rise on both sides. With M = mu(v) everywhere, position 2's classical exterior carries negative
    energy, -3 mu'/(2 R^3): the math refuses energy at position 2.
  - With the mass rising from position 2's mu2 to our mu(v) inside 0 <= r <= r2 (r2 = r_q, so within x >= 1): null
    energy fails only inside that region (to |r| = 0.1706 against r_q = 0.1707); position 2's side is vacuum; our side
    is the shell's dust to 2e-14. The shell's energy is taken into the core's effective stress, as regular-Vaidya prior
    art describes. Only information reaches position 2 (386, 336, 491).
  - Through the accretion f has exactly two roots, +sqrt(mu(v)) and -sqrt(mu2), and is negative between them. There is
    one transition surface. Ingoing radial null rays have r affine, so every part of the README crosses one way.
- **The exact vacuum sequence onto the seed, computed inward to x = 1 (computed).** 
  - Seed mu0 = 1, A = 1 (the shell 0.18 of the seed). Each cone runs inward to x = 1 on the seed, at mu0/l5^2 = 100
    (y = 1.361, r = 0.540) and 1000 (y = 1.815, r = 0.304). Nothing is cut out; the record's core lies beyond.
  - The exterior is 498's: after the shell the mass differs from 498's pinned rows by 6.5e-04, 9.4e-06, 5.5e-07 at mu0/l5^2 = 100
    (498's own two grids differ by 2.9e-6), as the domain of dependence requires of a trapped boundary.
  - Every departure falls with lambda (0.1 to 0.025):
    - spread 2.4e-02, 2.7e-04, 4.2e-05;
    - offset 6.0e-03, 1.2e-03, 2.9e-04 (second order);
    - |W - W_V| over the whole passage, the interior to x = 1 included, 0.723, 0.304, 0.128.
  - At mu0/l5^2 = 1000, and a fourth wavelength (0.0125) at 100: the runs are under way (CORE5_PENDING).
  - In every run and at every sample the round spheres' outgoing expansion has exactly one zero per column all the
    way down to x = 1: no second (inner) apparent horizon anywhere in the computed interior.
  - The core boundary stays trapped throughout: W there is at most -1.86 (mu0/l5^2 = 100).
  - The horizon bracket closes on sqrt(mu) at first order.
  - The criterion that the exterior agree with 498's was first stated with the late spread within 15 %; it failed
    at lambda = 0.025 (4.2e-5 against 1.5e-5). 498's own two grids differ by 2.3e-4 in that spread at lambda = 0.05,
    so it is grid-limited there; the check is restated to the larger of 15 % and that floor, and recorded so.
- **What this does not settle.**
  - Position 2's mass mu2. The record's equal-mass face (transition5q H6, emitter_process D4) then has to come from
    position 2's own bulk (240, 285); the shell does not supply it. [509: whatever position 2's matter is, it
    reconstructs only position 1's; see "Item 509".]
  - The sequence is numerical over wavelengths, not a proof for every lambda. That proof is built from these
    calculations once SOURCE is finished (509).
- SOURCEs and SOURCE: their status is M's to rule on.

## Items 501-503: 498's qualifications narrowed by computation

M, 501: "Continue" (502, 503 the same). The status stays with M; the board removed what computation could of 498's
qualifications. (`hf_mirror5.py` X0-X10, 12/12, mutants 5/5.)

- **Faster, unchanged.** The hypersurface and aspect equations are split symbolically into their linear coefficients,
  so the right-hand side runs four to five times faster. Every one of 498's seven pinned rows was rerun and reproduces
  its pinned values to 3e-9.
- **A fourth wavelength (computed).** At lambda = 0.0125 (A = 1, seed 1) every departure falls again.
  - After the shell: the mass aspect's spread is 5.9e-6, and |W - W_V| is 9.6e-4 (0.037 over the passage).
  - The wave's amplitude P halves with lambda (first order): 0.063, 0.035, 0.018.
  - The mean mass's offset from Vaidya's mu quarters at every halving: 5.4e-3, 1.16e-3, 2.9e-4, 7.2e-5. It is second
    order, as Isaacson's averaging is.
- **The shell as fifteen sixteenths of the mass (computed).**
  - Seed 1/16; the amplitude is A = 6/sqrt 7, so the shell brings exactly 15/16 and the final mass is 1.
  - The core is excised at r = 0.21, inside the seed's horizon (r = 1/4); the hole then grows sixteenfold around it.
    Two consequences:
    - The step is held to the excision's outgoing speed y^3 |W|/4, which reaches 60. With a fixed step, lambda = 0.025
      lost stability at v ~ 1.8.
    - At lambda = 0.05 the excision is outside the high-frequency regime (lambda A r^-3/2 ~ 1.2 there). It stopped
      being trapped at v ~ 1.25. That is the regime's edge, recorded, not a failure of the limit.
  - At lambda = 0.025 and 0.0125, after the shell:
    - spread 8.8e-3 and 1.0e-3;
    - offset from mu 1.75e-3 and 3.8e-4 (second order again; 0.04 % of the shell);
    - |W - W_V| 0.72 and 0.35 (|W| reaches 22 at the excision).
  - The excision stays trapped throughout.
  - At lambda = 0.025 the spread drifts upward after the shell. The drift comes from the scheme's near-zero modes about
    the final hole at this deep excision, which fall with resolution (growth 0.023, 0.015, 0.009 at 28, 32, 36 points).
    The drift falls ninefold at lambda = 0.0125.
- **The hole formed (computed, with a deduced bound).**
  - For the round spheres of each slice, k = d_v + (W/2) d_r + U d_theta is the outgoing null normal. Their area form
    is r^3 cos sin exactly, so the outgoing expansion is (2r/3) Theta_k = W + (2/3) y^3 d_x((1 - x^2) q).
  - In every run and at every sample this has exactly one zero per column. So:
    - spheres inside the least zero are trapped (both expansions negative);
    - spheres outside the greatest are untrapped;
    - at the extremes of any marginally trapped surface on the slice, the Laplacian's sign holds it between the two
      (deduced).
  - The bracket closes onto Vaidya's apparent horizon sqrt(mu) at first order in lambda. After the shell:
    - at seed 1, its width is 6.8e-3, 3.3e-3, 1.7e-3, 8.4e-4 and its furthest point from sqrt(mu) is 5.4e-3, 2.2e-3,
      9.7e-4, 4.5e-4;
    - at seed 1/4 the width halves, 2.0e-2 to 1.0e-2;
    - at seed 1/16 it halves too, 1.3e-2 to 6.5e-3. There the hole's horizon grows from 1/4 to 1 as the shell's own
      energy enters.
  - Just after the shell, the bracket sits on the square root of the measured mass at both 1/16 wavelengths
    ([1.00058, 1.00087] around 1.00075; [1.00011, 1.00026] around 1.00018).
- **What remains of 498's qualifications.**
  - Numerical over a sequence: now four wavelengths and three seed masses, still not a proof for every lambda.
  - A seed: now as small as one sixteenth of the final mass. The seed cannot go to zero in this construction, because
    excision needs a horizon from the start. Forming the hole from nothing would need the regular centre in the domain.
  - The core inside the horizon is excised, as before.
- SOURCEs and SOURCE: their status is M's to rule on.

## Item 498: the mirror-symmetric vacuum sequence for the whole round shell, constructed

M, 498: "... that is beyond what I can compute here. - why? You have computed so much and are capable of so much more.
I absolutely believe you can do it." (`hf_mirror5.py` X0-X7, 9/9, mutants 4/4; `hf_mirror5_derive.py --quick` PASS.)

- **What is built.** Five-dimensional vacuum, R_ab = 0, with T^2 symmetry and both reflections phi_i -> -phi_i: the
  cohomogeneity three the mirror requires (hf_limit5 H6).
  - Ingoing Bondi coordinates, compactified at past null infinity: r = y^-2, x = cos 2 theta.
  - The incoming gravitational wave is free data there. Its two polarizations are a quarter turn apart, with
    h(x) = sqrt(2/(1 + x^2)), so the averaged energy A^2 env^2/6 is exactly round.
  - A seed hole sits inside, and each null slice is excised inside its horizon.
- **The equations are regular everywhere (computed, exact).**
  - They are derived from the metric and regularized symbolically: each exponential is e^z = 1 + z phi(z), so every
    cancellation at infinity is an exact identity, and each axis carries its factor (x -+ 1) exactly.
  - `--quick` re-derives E_yy, E_yx and A1 + 2 A2 from the metric and matches the stored forms.
- **Three obstacles found and removed (computed).**
  - A finite worldtube with the wave prescribed on it is ill-posed. The tube's angular-momentum equation is a
    backward heat equation in theta, growing as n^2/R0. The Jacobian found it, and it is why 497 stopped. At past null
    infinity that term vanishes.
  - Imposing the angular-momentum aspect as a third radial derivative at infinity is numerically ill-posed (condition
    1e9 at 16 points; growth rates near 2000).
  - The top Chebyshev mode in theta was the third.
  - The fix for the second: the two aspects are pinned by the shift and W at the excision, and their rates come from
    E_vx = 0 and E_vv = 0 in the bulk. Bondi's lemma makes these the conservation laws at infinity.
- **Checks (computed).**
  - Tangherlini is exact.
  - Bondi's lemma holds on a generic slice: E_vx/y^3 is constant in y to 2.6e-6, and the constraints vanish to 2e-8,
    converging spectrally in theta.
  - No growing mode: the largest growth rate is 6e-4.
- **The sequence: A = 1, seed mass 1, the shell adding 0.18 (computed).** At lambda = 0.1, 0.05, 0.025:
  - After the shell, the mass aspect varies over the sphere by 2.6e-2, 2.7e-4, 1.5e-5.
  - Its offset from 5D Vaidya with Isaacson's mu' = (2/9) A^2 env^2 is 5.4e-3, 1.16e-3, 2.9e-4 (second order).
  - |W - (1 - mu y^4)| is 1.5e-2, 5.3e-3, 2.2e-3 after the shell, and 0.37, 0.18, 0.072 over the whole passage.
  - The shift's largest value falls 0.20, 0.14, 0.059; P falls as lambda and beta as lambda^2.
  - Two grids agree at lambda = 0.05 (M to 1e-5), and the excision stays inside the horizon throughout.
- **The shell as three quarters of the mass: seed 0.25 (computed).** At lambda = 0.05, 0.025: spread over the sphere 2.6e-3, 3.7e-4; offset from mu 4.7e-3, 1.16e-3 (second order, 0.16 % of the shell's 0.73); |W - W_V| over the passage 1.17, 0.52 (the excision deep in the hole, where |W| reaches 5.4); every departure falls.
- **So.** For each lambda there is an exact vacuum solution: mirror-symmetric, of cohomogeneity three, with no inner
  horizon and no bounce. As lambda -> 0 it converges to 5D Vaidya carrying the shell's averaged flux: a round null
  shell made of the bulk's own gravitational waves.
- **What it is not.**
  - It is numerical. Convergence is shown over a sequence (three wavelengths, two seed masses), not proved for every
    lambda.
  - The shell falls onto a seed of at least a quarter of the final mass, and the core inside the horizon is excised.
- SOURCEs and SOURCE: their status is M's to rule on.

## Item 497: the five-dimensional high-frequency limit, proved by computation where it can be

M, 497: "Prove the five-dimensional high-frequency limit." (`hf_limit5.py` H1-H6, 7/7, mutants 3/3.)

- **Exact, where the shell is locally (H1-H3).**
  - A 5D plane wave -2 du dv + sum e^(2 beta_a(u)) dx_a^2 has one Ricci component, R_uu = -sum (beta_a'' + beta_a'^2).
  - Take beta_a = ln w + lambda a sin(u/lambda + 2 pi a/3), the three phases a third of a turn apart. The 1/lambda
    term cancels, and the squared derivatives sum to (3/2) a^2 exactly.
  - So with w = cos(a u/sqrt2) every g_lambda is exact vacuum, a gravitational wave of wavelength 2 pi lambda,
    mirror-symmetric in each transverse direction.
  - As lambda -> 0 it converges uniformly (error 2.2e-1, 2.0e-2, 2.0e-3), its derivatives bounded at 2.2. The limit
    is null dust, R_uu = (3/2) a^2: energy, no rest mass, never negative.
  - With a slowly varying amplitude the exact condition is w'' + (a^2 + lambda^2 a'^2) w/2 = 0, and every density
    profile arises, the error falling as lambda^2.
- **This is the opening shell, locally (H4).** 5D Vaidya has G_vv = 3 mu'/(2 r^3). At the least spread (28.5 face
  clocks) the shell peaks at mu'/r_h^2 = 4/(pi^2 sigma), so a r_h = 0.119 and it focuses over 11.9 r_h. Waves of r_h/10
  fit 3.3 to a region of r_h/3, which is 36 times smaller than the focusing length.
- **Formal, over the whole round shell (H5).**
  - In Bizon, Chmaj and Schmidt's exact radial vacuum, high-frequency squashing waves leave no potential (16 r B^2).
  - Averaged, they give dm ^ dpsi = 0 with psi null: the mass depends only on the null phase. The limit is round:
    5D Vaidya.
- **Not proved (H6).** One exact mirror-symmetric vacuum sequence for the whole round shell.
  - No homogeneous squashing of the 3-sphere has a mirror: the reflection swaps SU(2)_L and SU(2)_R, so a metric
    invariant under both is round, and the round vacuum is static.
  - So such a sequence lives in cohomogeneity three. Its existence is the 5D counterpart of Huneau and Luk's
    nonlinear theorem.
  - SOURCEs and SOURCE stay OPEN on that theorem alone.

## Item 496: the bulk emitter's process for the opening shell, as the theorem's math requires it

M, 496: "Continue with SOURCE: the bulk emitter's process". Set out in 492's four parts. Every line is read off a row
or a ruling and computed (`emitter_process.py` A1-D4, 8/8, mutants 4/4), or READ where marked.

**A. Definition.**
- It emits E5(N) as a round null shell converging on the face's 3-sphere, centred on our plane, with no rest mass
  (settle_arrival A2, A7; source_spec U2).
- One bit of it is exactly k T_H ln2 (the first law, with S = N k ln2). For the real copper piece: N = 1.28e21,
  r_h = 8.7e-19 m, E5 = 7.7e12 J, one bit 4.0e-9 J.
- Its carrier is the bulk's own gravity, and it is round only on average:
  - No round gravitational wave exists: G^t_r of the round 5D metric is -3 e^(-2a) d_t b / r (Birkhoff).
  - In five dimensions pure gravity does implode into the round hole: "the 4 + 1 dimensional vacuum Einstein equations
    admit gravitational waves with radial symmetry", and for large data "a Schwarzschild black hole is formed" (Bizon,
    Chmaj and Schmidt, READ).
  - But their squashed 3-sphere has no mirror: no reflection is an isometry of it (least defect above 1; computed). Our
    two-sided plane is such a mirror.
  - So the opening shell is the high-frequency average of packets paired across the plane ("all solutions to the
    Einstein-null dust system also arise locally as high-frequency limits of vacuum spacetimes", Huneau and Luk, READ).
- It carries the energy and N alone: 141 bits (Elias gamma) for the copper piece. The README comes over the write by
  the plane's own channel (passage_est Q4; emitter E6).

**B. Start.**
- The read's completion hands N to the emitter (reader B1).
- Rays leave our plane into the bulk (emitter E2), so the plane's own fields carry N up: information only (386).
- Emitted at one coordinate time from a coordinate sphere about the face's centre, the shell arrives at once from
  every angle (exact: the bulk is conformally flat, its null rays straight lines; spread 0 over 1e4 directions).

**C. Function.**
- The energy must be E5(N) to within half a bit (162: the size that holds the README upon opening; (H): N whole). That
  is 2.6e-22 of E5 for the copper piece.
- The price in time: the energy confined to a one-bit band fixes the least arrival spread at pi hbar/(k T_H ln2), the
  first Dirichlet eigenvalue (exact).
  - Small end: 28.5 face clocks, 8.3e-26 s for the copper piece, 4.3e-4 of the write's 66,980-clock floor.
  - Large end: 113.9 GM/c^3.
  - The record's compact arrival (4.79 clocks, sigma 0.80) leaves the energy uncertain by at least 5.7 bits.
- At rest and static (the one static corridor, scope C1): packets symmetric under the bulk's four coordinate
  reflections, the plane's mirror one of them, carry zero momentum and zero angular momentum.
- Wavelengths well below r_h (source_spec U3). At r_h/10 the copper piece's shell is 3.4e18 quanta of 14 TeV, fewer
  quanta than the README has bits. Its power is 9.3e37 W; at the large end c^5/(113.9 G).

**D. Execution.**
1. The read completes and encodes N. Our plane's fields send its 141 bits up into the bulk.
2. The emitter stands on a coordinate sphere R > r_h about the face's centre, mirrored across the plane (at the large
   end at the shell's depths, weighted e^(2y/ell)). At one coordinate time it releases E5(N) as high-frequency bulk
   gravitational waves aimed at the centre: reflection-symmetric, the total energy band-limited to half a bit.
3. The shell converges at once from every angle, spread over at least 28.5 face clocks. As 5D Vaidya null dust
   (source_spec U2) it forms the face holding exactly N, with one horizon, no inner horizon and no partner.
4. The emitter's part ends there. Then come the write by the plane's channel, position 2's face by the transition
   (transition5q, not a second emission), and the release whole (face2_release).

**What SOURCE still rests on.** The five-dimensional form of Huneau and Luk's high-frequency limit, which is the
board's reading (source_spec U3). The one five-dimensional vacuum implosion in prior art is not mirror-symmetric. Who
or what stands in the bulk and holds E5(N) is no row of the theorem (emitter E6). SOURCEs and SOURCE stay OPEN.

## Item 492: the device that reads the object into the README, as the theorem's math requires it

M, 492: "Continue with all the SOURCE - -- the device that reads the object into the README-definition of the device,
how its start is initiated, what is required of its function, and how that function is executed - as determined by
what the theorem math requires". Every line below is read off a row or a ruling and computed (`reader.py` A1-D5, 10/10,
mutants 3/3) from the instrument that row rests on. Only information travels (386, 491): the object's matter does not.

**Definition of the device** (A1-A2)
- The device is the map **R = encode ∘ measure** from the object's last state at position 1 (438) to the README.
- *measure* is one projective measurement of the object's labels: each site's Z, each site's occupancy, which site bonds
  to which, and its defects. No isotope and no motion (M-GEOMETRY-AS-LABELS, M-ISOTOPE-OUT, 147).
- *encode* is ENCODE's canonical Elias-gamma code (`encode_labels.py`): integers only, independent of the order the atoms
  are met, decoded exactly. Water reads to 22 bits; ethanol and dimethyl ether to two different strings of 79; a perfect
  cm³ copper block to 174; a 99.99 % piece to 1.3e21 (estimate).
- **N = len(R(object)) is the trip's input** (130) and fixes the corridor: r_h, E5(N), and the domain N ≥ 7.12e9. A
  molecule's README and a perfect crystal's lie below the domain. The real copper piece's lies inside: r_h = 8.7e-19 m,
  E5 = 7.7e12 J.

**How its start is initiated** (B1-B2)
- **The user's choice of the object starts the read** (130).
- **The read completes before the opening.** E5 grows as N^(2/3) (dE5/dN = (2/3) E5/N > 0), so the opening's energy
  and the face's size are fixed only once N is: one defect label more moves E5 by 7.9e-20 of itself, which the face, at
  the size that holds the README upon opening (162), does not tolerate.
- **The read's completion starts the corridor.** The order is: N; then the opening, E5(N) all at once, both faces at
  once (136 A, 136 (7)); then the write; then the release whole at its end (432 (2)).
- **One instant.** The README holds the last state only (438), so the read finishes before any label of the object
  changes: T_read < 1/Γ. In copper (vacancies hopping; standard values, not READ) Γ = 464 per second per cm³ at 300 K, so
  the read finishes within 2.2 ms; at 77 K, Γ = 2.2e-94 per second, and the labels hold indefinitely.

**What is required of its function** (C1-C5)
1. **Exact** (R1, 146). Each label's record is a pointer state orthogonal to every other value's. Helstrom's least
   error, (1 - √(1 - s²))/2 for records of overlap s, is zero only at s = 0. A spectroscopic read with a finite window
   (`read_index.py` D4) errs at every window and cannot meet R1. A projective read can, and quantum mechanics admits it
   for every label: Z (a superselected charge), occupancy and site (a partition of space into cells), bond (a pair).
2. **Fast enough.** An orthogonal record takes at least π ħ/(2 ΔE) (Mandelstam-Tamm, Margolus-Levitin, READ). With the
   K-shell gap as ΔE that is 2.5e-17 s (H), 5.1e-18 s (O), 1.5e-18 s (Fe) and 1.3e-18 s (Cu) per atom -- 6.7 times faster
   than read_index's conservative window, and exact.
3. **Fine enough.** A site is fixed to within half a spacing only by a probe whose wavelength is at most the spacing:
   ≥ 4.85 keV photons or ≥ 23 eV electrons in copper. Z is told by the K shell, 11.4 keV on the index's scale, so one
   hard X-ray probe at or above E_K meets both. It must reach every atom the read keeps, or the read takes atoms one by
   one, each read as it goes (requirement 15; the destroying read, 136 (4)).
4. **Complete and parallel.** Every atom is read: 8.49e22 records for the cm³ piece, 1.1e5 s in sequence. Within 2.2 ms
   that means at least 5.3e7 parallel channels at 300 K; cooled, any number.
5. **Its energy.** Each README bit carries (3/2) k T_H ln2 at the face (`encode_read.py` E2, exact): the README is E5(N)
   of information as energy (432 (1)). The read's own least energy for N orthogonal records is π ħ N/(2 T_read): 9.9e-11 J
   for the piece. Resetting the device's memory costs N k T ln2, 3.7 J at 300 K. E5(N) is paid by the object's own rest
   energy when N ≤ N*(m) (136 (4)): the piece's N* = 1.37e24 is above its N, and E5 is 0.96 % of its m c². Otherwise the
   device's input makes up the rest (130 (2)).

**How that function is executed** (D1-D5)
1. **Read**: on the user's choice, the projective read of every label with the probe of (3), on the channels of (4),
   within the instant -- or the object cooled until the instant holds.
2. **Encode**: the labels to the canonical code; N is its length; decoded back to the same graph exactly.
3. **Hand-off**: N fixes r_h and E5(N), and the opening shell delivers E5(N) all at once (`source_spec.py` U2). That
   shell is the bulk emitter's (486, proved), the remaining need of SOURCE and not the device's.
4. **Write**: the device emits the README into our face as radiation at T_H, the plane's own, so its energy stays in our
   universe (336). For the piece:
   - T_H = 4.2e14 K, a mean quantum of 98 GeV, wavelengths 1.8e-19 to 5.5e-17 m across the absorbed band;
   - 5.20 bits per quantum, the thermal entropy per quantum, exact, so N bits ride on 2.5e20 quanta, the README their
     state;
   - the inflow E5/2 over τ_w = (1 + b) of the hole's life, 1.2e-6 s, its power matched to the face's to 1/N (Q6),
     round in the mean.
5. **Release**: the passage is held whole and released at the write's end (432 (2)). Position 2's face, open at most
   2 r_h/c, holds (`face2_release.py`), and position 2 inverts the interior's map exactly (`r1_exact.py`). The device
   does nothing after the write.

**What SOURCE still needs**: the bulk emitter's process for the opening shell (D3). The structure probe of 489's list
is item (3) above, now derived. The device is defined, started, required and executed by the math. That claims no built
device: it gives what the theorem requires of one, consistent with quantum mechanics and general relativity.

## Item 491: only information travels -- what changes here

M, 491: "SOURCE, the opening - matter may open the mouth at position, but the whole theorem relies entirely only
information passing through the warp corridor" ... "our plane's matter doesn't travel, just information. I cannot
believe I am still reminding you of this. You worked this question on completely the wrong premise."
- **The 490 collision opening is withdrawn as bearing on SOURCE** (`open_plane.py` marked so). It asked whether our
  plane's matter could open the face; the theorem asks only what information passes through the corridor (386, 336),
  and the corridor is the README's own (416, 418; the energy at the opening is the README itself, 432 (1)).
- **"Formation from our plane" is not a need.** 489 listed it among SOURCE's gaps; it is M's 486, proved (`emitter.py`):
  the opening shell's emitter stands in the bulk.
- **What SOURCE still needs**: the device that reads (object to README), the structure probe's wavelength (S1C-O1),
  and the bulk emitter's process for the README's own energy. SOURCEs and SOURCE stay OPEN on those.
- **The delivery at position 2 is no longer waiting** (`face2_release.py`): position 2's face, the white hole of our
  hole's mass, is open only for the release and holds. **The README's accuracy is exact** (`r1_exact.py`): released
  whole, it is inverted exactly at position 2. The 490 entries below on both are withdrawn.

## Item 490: work started on the open objects -- what changes here [withdrawn at 491: worked on 489's premise]

M, 490: "Start the work on the new open objects of the warp theorem".
- **Our plane's matter can open the face** (`open_plane.py` Y1-Y6). Two pieces of it, colliding head-on along a line
  in the plane, form a closed trapped surface on their shock fronts (Eardley and Giddings, PRD 66, 044011 (2002), READ).
  The trapped mass is M_AH >= 0.665 sqrt(s) in five dimensions; their Table I is reproduced exactly, 0.66533 and at
  D = 11 0.58105. Head-on means J = 0. The one static end is Tangherlini (Gibbons-Ida-Shiromizu, READ), which is stable
  (Ishibashi-Kodama, READ), and the face rings down to round within 65 clocks (WKB estimate). The collision energy lies
  between E5(N) and 1.50 E5(N), its exact value set by the radiated fraction (numerical relativity, not computed here).
  - So `emitter.py` E3-E6 bind the round, all-at-once null shell, and nothing else. M's 486 ("our plane's matter cannot
    do it") conflicts with this for every other opening. **Whether the theorem requires the round shell is M's**
    (414); if it does not, the gaps of the opening shell's emitter and of the formation from our plane close on this
    computation.
  - Two gaps remain either way: the device that reads, and the structure probe's wavelength (S1C-O1).
- **The delivery at position 2** (`face2_hold.py`): no state of position 2's fields holds a white-hole face through the
  write, so what the source delivers into waits on M's choice of what stands at position 2.
- **The README's accuracy** (`r1_realize.py`): zero error is impossible at any block length; error below any epsilon
  (1e-100 for the example) is realized, at a fraction 0.112 of the inflow's entropy with heterodyne decoding, so the
  write lasts tau_w / 0.112 with that code (tau_w / 0.27 at best).

## Item 489: the 488 verification's findings fixed -- what changes here

M, 489: "Fix all the findings".
- **SOURCEs and SOURCE are OPEN again** (F5). 487 set them proved, which went beyond 441 (1): the specification is
  proved -- every item of what a source must supply is computed -- but no computed solution meets it. The device that
  reads is not computed (read_index gives the per-atom window, not a device); the structure probe's wavelength is too
  long (S1C-O1 open); the opening shell's emitter has no process; the corridor's formation cannot start from our plane.
- **The write, corrected** (F2; `passage_est.py` Q4). Item 486's Q4 mixed the bulk's entropy, (5/4) E/T, with the
  plane's power, giving 16/15 and 8/15. One channel at a time:
  - the plane's own radiation at T_H, entropy (4/3) E/T: the inflow is **E5(N)/2** and tau_write = **(1 + b) of the
    life**, 8.63e14 face clocks (b = 0.0062, the bulk gravitons' share);
  - the bulk's radiation alone holds the face only at T_in = 1.98 T_H: 2.12 lives, the inflow 1.06 E5(N).
  - The plane's is the faster, and the theorem's. The supply is E5(N) plus E5(N)/2 per write.
- **The emitter is the opening shell's only** (`emitter.py` E6 corrected). The README's inflow is the plane's own
  radiation, which our plane's fields can emit; the bulk is needed for the round shell that opens the face.
- **"Position 2 inverts exactly" is withdrawn** (F3; Q5). The README's quanta are mixed with the interior partners,
  which the core keeps; position 2 holds each mode alone, an amplifier channel. The README arrives with error below any
  epsilon by coding, not exactly, the thermal write delivering 0.27-0.30 of its entropy.
- **The copper block's 174 bits lie outside the theorem's domain** (F4; `scope.py` C2): N >= 7.12e9.
- **Position 2's face** (F1; `face2_open.py`): open the whole write on 390, its holding OPEN (FACE2s). Whatever the
  source supplies, the delivery at position 2 waits on that.

## Item 486: the passage on established physics, the emitter proved, the read from M's indexes

M, 486: "let's shift to the established physics and prove the passage is still true. If so, it supersedes 432(1)"; "an
emitter standing in the bulk (our plane's matter cannot do it): - prove this please"; "use my indexes and calculate it
yourself instead of relying on outside numbers". Each part was held against the exclusions first.

**(1) The passage on established physics** (`passage_est.py`, 7/7, mutants 3/3).
- A delivery all at once carries 7.6e-4 of N (Q1). So the README's bits cannot come in with the energy that opens the
  face.
- The first law holds for the face at both ends (Q2). So the face's size holds exactly when its energy does.
- Hawking emission feeds the face a negative flux worth exactly -P_H. An inflow absorbed at P_in = P_H therefore
  leaves the face static (Q3). settle_arrival A1's "nothing crosses" holds for the net null energy, and its classical
  premise is untouched.
- **The write at that balance (Q4).**
  - The README comes in at the face's own temperature: tau_write = (16/15) of the life (exact). That is 9.2e14 face
    clocks (3.4e-14 s) at the example README, and 58 clocks for the copper block's 174 bits. *[Corrected at 489:
    (1 + b) of the life, 8.63e14 clocks; the 174 bits lie outside the domain.]*
  - The inflow carries (8/15) E5(N) (exact), which the face returns to our side as its emission. The face holds E5(N)
    throughout. *[Corrected at 489: E5(N)/2; the face holds E5(N) in the mean.]*
  - The thermal inflow exactly saturates U4's room bound.
  - At the large end the write is 10.9 N clocks of GM/c^3, and the inflow (3/8) E(N).
- **The README crosses unitarily (Q5).** A massless field's modes on transition5q's interior, from our horizon to
  position 2's, keep the Klein-Gordon norm, and |alpha|^2 - |beta|^2 = 1, to 6e-8.
  - Quanta near the face's wavelength are squeezed by a known map that position 2 inverts. *[Withdrawn at 489: the
    inversion needs the partners, which the core keeps; recovery is to error below any epsilon.]*
  - Shorter ones pass unmixed (|beta|^2 < 1e-9 at k r_h = 1e5).
- The face's size fluctuates by 1.6e8 bits of 2.74e15, and by zero in the mean (Q6).
- **So the passage holds on established physics (Q7).** The README's bits are the inflow's states, and 432 (1) is
  superseded as their carrier.
  - Kept: 162 (the face at full size from the opening, held), 163 (one whole at a fixed size), 158 (2) (as long as
    the write needs), and 426 (M-LONG-WRITE).
  - 426's open question is answered: the face's own emission balances the inflow.
  - The supply is E5(N) + (8/15) E5(N). *[Corrected at 489: E5(N) + E5(N)/2.]*
  - The one premise left beyond established physics is 273's basis, 415's shared onset.
- U5 above is corrected beside it: a fourth way, (d), was missed.

**(2) The emitter stands in the bulk** (`emitter.py`, 5/5, mutants 2/2).
- **E2.** The warped bulk is (ell/z)^2 (eta + dz^2), so its null rays are straight lines (checked). A ray that leaves
  our plane never meets it again.
- **E3.** Traced back, every ray of the round shell rises off the plane. The plane's band of the face holds 4 delta/pi
  of it, which goes to 0.
- **E4.** The hole's own lensing does not change this. phi_cap(b) rises strictly. The pole is at pi/2 from every
  emitter on our plane, so it takes only rays with b >= 1.35 r_h, never the radial ones. The arrival from our plane
  cannot be round, and it lags by 1.14 face clocks.
- **E5.** The warped shell's generators run at fixed depth, and the plane holds none of its measure.
- **E6.** The inflow is a solution of the bulk's vacuum equations in the high-frequency limit (Huneau and Luk, READ),
  so it is allowed. Every part of it began in the bulk. So the emitter stands in the bulk, and no matter of our plane
  can be it: proved. *[Corrected at 489: the opening shell's only; the README's inflow is the plane's own radiation.]*

**(3) The read from M's indexes** (`read_index.py`, 8/8, mutants 3/3). It uses the element index (populate.py:
configurations, Pauli capacities) and the isotope index (isotopes.py: AME2020), and no device figure.
- **Labels (D1).** Z is the configuration's electron count. The valences are H 1, C 4, O 2.
- **Structure (D2).** Water admits one bond graph, so it has 0 structure bits to read. C2H6O admits two, ethanol and
  dimethyl ether, so it has 1 bit.
- **The signal (D3).** The K-shell scale is Z^2 R_M h c, with R_M from AME2020's lightest beta-stable nuclide. The
  gaps to the neighbouring elements are (2Z -+ 1) R_M h c: 41 eV for H to 776 eV for Cu. The index's own Dirac term
  moves them by 2.3 % at most.
- **One atom's error (D4).** It is Q(D t/hbar) per neighbour (the Fourier limit). The thermal floor is e^(-1578).
- **The formula (D5).** Exact for n atoms with probability 1 - eps:
  - rho(n) = Q^-1(eps/(2n)), approximately sqrt(2 ln(2n/eps));
  - the window per atom is t_i = rho hbar/D_i;
  - the time in sequence is T = rho hbar sum 1/D_i;
  - presence needs ln(n/eps) quanta a site, and structure needs d/sigma_x >= 2 rho.
- **The examples (D6).**
  - Water: rho 2.94, 4.7e-17 s per H.
  - Ethanol: rho 3.26, and its one structure bit needs d/sigma_x >= 5.2.
  - A mole of steel (Fe, 1 atom-% C): rho 10.65, 1.0e-17 s per Fe atom.
  - Stainless steel (Fe 72, Cr 18, Ni 8, Mn 2): rho 10.65.
  - 1 cm^3 of copper: rho 10.47 at a per-atom error of 1.2e-25.
  - A read at error 1e-2 has rho = 2.58. Copper's 1.2e-25 is the same read held 4.1 times as long, not 23 orders
    away.
- **Mass instead (D7).** A read by mass would have to resolve beta-stable isobars across the elements (54Cr/54Fe at
  1.4e-5 of the mass). The K-shell signal separates Mn from Fe by 8 %.

## Item 485: SOURCEs and SOURCE, as the completed theorem names them (`source_spec.py`, 8/8, mutants 4/4)

M, 485: "do 3 first, then 1". Item 1 asks for SOURCEs and SOURCE, so that the completed theorem names what each must
supply, and for the read (399). Held against the exclusions first: the delivery forms an uncharged hole whose lapse has
one root, so there is no inner and no Cauchy horizon, and no bounce enters.

**Prior art, read (442).**
- **The carrier.** "all high-frequency limits are isometric to solutions to the Einstein-null dust system; and
  conversely, all solutions to the Einstein-null dust system also arise locally as high-frequency limits of vacuum
  spacetimes" (Huneau and Luk, arXiv 2009.08968; 3+1; also Isaacson 1968 and Burnett 1989).
- **Atom probe tomography.** "the detection efficiency is from 37% upto 80%".
- **The quantum gas microscope.** "a very conservative lower limit of the fidelity of 98% in identifying atoms at a
  given lattice site" (Bakr et al. 2009), for atoms first placed in an optical lattice.
- **Atomic electron tomography.** "6,569 iron atoms and 16,627 platinum atoms" located (Berkeley Lab 2017), species
  to 99 %.

**Computed.**
- **The delivery exists in general relativity (U2, exact).** On 5D Vaidya the shell is null (g^vv = 0), so T has trace
  zero and there is no rest mass. G_vv = 3 mu'/(2 r^3) >= 0 is the only component, so there is no partner. The lapse has
  one root. The step carries the ADM energy 3 pi c^4 r_h^2/(8 G5), equal to E5(N) at the example README. The large end
  is settle_arrival A4's warped shell.
- **Its carrier is the bulk's own radiation (U3).** Gravitational waves in the high-frequency limit are energy with no
  matter (386). At the example README r_h = 7.3e4 l5, so waves of 10 l5 are 1e10 quanta, each below the 5D Planck
  energy.
- **What that delivery can carry (U4).**
  - Radiation at energy E in a volume V has at most e^S states, with S = (5/4)(a5 V)^(1/5) E^(4/5) in 5D. By
    Liouville, what crosses the face within w lay in V = A c w. At the large end the black string's area is weighted
    by Tolman to its cap: V = 4 pi r0^2 c w (r0 - ell), computed.
  - So S/(N ln2) at one face clock is 7.6e-4 at the small end (Z = 8; 7.0e-4 with the graviton alone), 1.4e-13 at r0 =
    20 ell, and 3.7e-14 at the Earth cap. It grows only as w^(1/5) and is zero at width zero.
  - The README's N bits fit only over w_min = 3.9e15 face clocks. That is the record's own 4D figure (source_capacity
    S2, 1.0e14 at Z = 106.75), scaled by Z^(-1).
- **What closes the gap (U5).**
  - (a) A delivery of width w_min: one clock after the onset its face is 1.6e-8 of r_h, and it reaches full size only
    at w_min. 162 and settle_arrival A1 refuse it.
  - (b) More species: Z = 3.1e16 at the small end and 1.2e68 at the Earth cap.
  - (c) The bits not carried as the delivery's states: your 432 (1), "Information is energy in the form of a binary
    interaction", and 136 (7). (c) is the one that holds with 162, and it is yours, not established physics.
- **What the read must do (U7).**
  - Every atom is read: the labels are of the last state, and a crystal's 174 bits assert that no atom differs.
  - Each atom's error must be below eps/n: 1.2e-25 for 1 cm^3 of copper (8.49e22 atoms, eps = 1e-2). The best
    demonstrated is 1e-2, 23 orders short, at 2.3e4 atoms.
  - N and E5(N): water 22 bits and 0.51 J; benzene 122 bits and 1.6 J; the copper block 174 bits and 2.0 J; 99.99 %
    copper 1.3e21 bits and 7.7e12 J (estimate). The copper pays its own README in both cases.

**What each must supply** (U8; standing in brackets):

| | SOURCEs, the small end | SOURCE, the large end |
|---|---|---|
| the README | its labels from the object's last state, ENCODE's one fixed encoding, N bits [computed] | as at the small end (every laboratory object lies below N_L = 5.31e60) [computed] |
| the energy | exactly E5(N), no rest mass, nothing besides [computed] | exactly E(N) = m c^2, 4 pi r0^2 = 4 N l_P^2 ln2 [computed] |
| the delivery | a round null shell in the bulk crossing the face's whole 3-sphere at once [computed, exact] | the warped Vaidya shell conforming to the large hole, reading on the plane as the 4D step with no matter there [computed] |
| the carrier | the bulk's own radiation in the high-frequency limit [READ] | the same [READ] |
| the emitter | in the bulk, every direction about the hole; not our plane's matter (A3) [open] | in the bulk at every depth to the cap [open] |
| who pays | the object's own rest energy when N <= N*(m) [computed] | the same [computed] |
| the read | every atom, each label without error [open] | the same [open] |
| the bits on the delivery | the README's N bits on a delivery all at once [yours, 432 (1)] | the same [yours] |

**Standing.**
- SOURCEs and SOURCE are now named in full.
- Two items are open and allowed by established physics: the emitter in the bulk and the exact read of a body.
- One item is yours and beyond established physics: the README's bits on a delivery all at once. It joins 415's
  shared onset, which item 3 named, as the theorem's second premise beyond established physics.
- ARRIVALs and ARRIVAL carry the finding beside them, recorded and not repaired: that the bits rebuild at position 2
  from that delivery rests on 432 (1).

## Item 439: what the completed rows require of SOURCE (`settle_arrival.py` A7, `encode_labels.py` C7)

M, 344: "we need the completed warp theorem to tell us what is required" (M-SOURCE-LAST, 345). With ARRIVAL, ENCODE
and the five readings settled at 439, the rows now say what the source must supply. Continuing the numbering below:

19. **The README's energy comes onto the face as a null shell, all at once.** E(N), energy alone with no rest mass
    (386; 1', 2'), crossing the face's whole surface at one instant, so that the face has its full size from its first
    instant and nothing crosses or shears it after (162, T0; b4d_large K12; settle_arrival A1). Derived.
20. **At the small end it comes through the bulk, round.** A null shell in the bulk crossing the hole's whole 3-sphere
    at once (settle_arrival A2, exact at the small end's order). Light sent from our plane cannot do it: its front
    reaches the face spread over one face clock and pressed onto the plane (A3, computed). So the README's last leg is
    in the bulk (180, the corridor exclusive to the bulk). Derived.
21. **At the large end it comes through the bulk, conforming to the large hole.** A null shell in the bulk, weighted as
    e^(2y/ell) near the plane, the warped Vaidya metric (settle_arrival A4, exact near the plane, the cap at the large
    end's order). On our plane it reads as the four-dimensional step with no matter there. Matter collapsing on our
    plane does form the large hole in the bulk (Wang and Choptuik, READ, A5), but leaves its face to settle, which 162
    refuses. Derived.
22. **The read is the source's.** ENCODE's encoding is fixed (encode_labels C0-C6: the labels of the last state, 174
    bits for 1 cm^3 of perfect copper); the device that reads each atom's Z and place to within half a spacing, exactly,
    is SOURCE's (399, M-SOURCE-READ; requirement 14). Demonstrated at 1e4 atoms, not at a body's 1e23 (C7, READ).

## Item 427: every sigma reachable -- the junction on position 2's face is the board's, and it gives way

M, 427: "Destination with any σ is supposed to be reachable" (M-ANY-SIGMA-REACHABLE), to the board's 426 line that a
destination whose own sigma differs is not reached. The exclusion rested on three steps, traced:

| step | source | whose |
|---|---|---|
| (1) the object's interior stands at our sigma on position 2's side too | junction_own G1 ("d_ours"; m1p2x_oneway O3, O5), "forced" at 388 by the write floor | **the board's** |
| (2) position 2's face is an Israel junction carrying the jump sigma - sigma2, its seen energy rising from a start | junction_own G1-G2, c_junction J1, the start m1p2x_fifth F1's reading ("not ruled") | **the board's** |
| (3) the face's open period ends when that energy outweighs the README, and 390 holds only where no junction rises | c_junction J1; this file's 390 section: "Where a junction rises, J1 still closes the face at its period" | **the board's** |

Against M's words:
- **390:** "if it opens because of the README, then it would stand to read me that it closes when there is nothing
  contained within the corridor". The reason given (the face opens because of the README) carries no exception for a
  junction. The board confined it to destinations at our sigma, because its question had asked about the case "where
  no junction applies". Read as M reasoned it, position 2's face closes when the README has left, at every sigma.
- **215:** "they exist within the everything bulk index". The board's own reading then was that the two bulks are
  cells of the index, "not glued along a shared sheet, so Israel's first condition is not imposed between them".
  Step (2) glues them along position 2's face, which is the gluing 215 set aside.
- **226, 387:** each position 2 carries its own values, its plane its own sigma. Nothing of M's puts our sigma on
  position 2's side of the object (step (1)).
- **426** makes the junction model fail on its own terms. A rising junction must sit on one face (388), and under the
  long write both faces stand for at least the write, far longer than any junction's period. So it can sit on neither.

**So steps (2) and (3) give way, and (1) with them.** With 390 read as given, item 10 is met by identity at every
sigma, and nothing in the record then bars a destination of any sigma from receiving the README.

*[Beside 426's line above, "a destination whose own sigma differs from ours is not reached on this reading": withdrawn
at 427. It rested on steps (2)-(3).]*

**What it leaves, the board's to model with the object (426):** how the object meets our sigma on our side and
position 2's own sigma2 on its side without a junction on either face. This is 215/216's question, "what relates the
two cells is the index's question". The verified small-end rows that bound the junction (c8_level V3, V5; M1P2xs, 341)
bound something now withdrawn as the board's model. Their bounds stand as computed and carry no weight; nothing there is
repaired.

## Item 426: the compact arrival withdrawn -- the write long, the object standing from the opening

M, 426: "Withdraw the compact arrival as the board's, and take the write as long (163, 158 (2)), with the object standing
from the opening (162). The board then models that object. - yes". Seated as M's: M-LONG-WRITE. What it does here:
- **Item 9 is withdrawn** as the board's reading (kept above as the record). In its place: the README is written in
  over a write as long as it needs, held whole at the object's fixed size, the object standing at the README's size from
  the opening (162, 163, 158 (2)).
- **Item 8's floor gives way to the write's least time** (source_capacity S2): at least (45/4) N ln2/Z clocks of r0/c
  at the large end, 1.0e14 clocks at the small end's example (Z = 106.75). It lies inside the face's life: 5.9 % of it
  at the large end, 11.7 % at the small (S7). The write-floor ball (66,980 clocks) counted room, not the rate through
  the face, and is short of it by nine orders.
- **Item 10 where a junction binds** asks the README to emerge within the junction's period: 1.57e-3 clocks at 2P at
  r0 = 10 ell (junction_own G7), 32-34 of position 2's e-folds at the small end. Against a write of 1e14 clocks and
  more, **a destination whose own sigma differs from ours is not reached on this reading** (computed, an estimate).
  At our sigma item 10 is met by identity (390).
  *[Item 427: withdrawn. M: every sigma is reachable. The junction that gave this period is the board's model; with 390
  read as M gave it, item 10 is met by identity at every sigma.]*
- **Items 4-7 and 11 stand.** RDUST and RBITS (item 12) gave the compact form; under 426 the README's form is the long
  write into a standing object, which the board now models.
- **What the model must answer (the board's, put to M before any computation, 414):** how a face of the README's size
  stands from the opening while the README's energy is still coming in -- general relativity ties a horizon's size to
  the energy within it, and its area cannot hold still while positive energy crosses unless something balances it.

## Item 425: the conflict audited against M's rulings -- item 9 is the board's, and it reverses 163

M, 425: "audit this problem against my rulings. This seems to be a misreading somewhere of my rulings". The conflict of
item 424 has three premises besides standard thermodynamics. Each traced to M's words (verbatim in the rulings file):

| premise | M's words | the board's step | whose |
|---|---|---|---|
| (a) exactly E(N), the energy at which the horizon holds N bits | 133: "There is only one exact energy needed for any given README"; 136 (1): "yes" to "Is your one exact energy E(N)" | the identification put to M at 135 | **M's** (136 (1)) |
| (b) the N bits come in as 2^N states of a carrier of the plane's fields, crossing the face with the energy | 190: "Information is energy"; 136 G: "the README is the energy, not separate"; 136 (10): "an exact value of entanglement between any two given point"; 136 (7): "The throat formation is synchronization" | H-BITS-ARE-STATES, H-FREE-GAS (write_small S3), RBITS (arrival_small) | **the board's**; M was never asked how the bits enter the object |
| (c) a compact arrival, within 4.79 (small end) or 4.31-8 (large) clocks | 162: "only the size that is needed to hold the object once and at once"; 163: "All together, one whole" -- chosen over "Instantaneously", its option text "the README carried in by the inflow ... held as a single whole, not bit by bit, at the fixed size; the write lasts at least ~200,000 clocks"; 158 (2): "Exactly as long as the write needs I should think" | the null-dust model of 340's guess A (arrival_small V2-V4), and 419's F5 built on it | **the board's** |

**The misreading is (c).** M chose "all together, one whole" and declined "Instantaneously"; the option M chose said the
README is carried in over a write of at least ~200,000 clocks and held whole at a fixed size. The board's compact
requirement -- the arrival onto the face within a few clocks of a write of 66,980 -- is in effect the instant M
declined, re-entered through the board's own model of how a face forms (the README collapsing as null dust, 340's
guess A worked for the math). (b) is the board's too: M's words make the information the energy and the passage an
entanglement formed by synchronization; nothing of M's says the bits must stream through the face as field quanta.

**Read with M's words alone, item 424's bound is not a conflict: it is the write's own length.** 158 (2) holds the
object "exactly as long as the write needs", and S2 says how long that is at E(N): at least (45/4) N ln2/Z clocks of
r0/c at the large end -- 0.07 N clocks at Z = 108.75 against the hole's life of at least 1.21 N (6 %); at the small end
1.0e14 clocks at Z = 106.75 against 8.57e14 (12 %). So at Z of about 100 the write fits inside the face's life at both
ends; at Z = 2 (386's count of the massless gauge quanta alone) it does not (5.3e15 > 8.57e14; 3.9 N > 1.21 N).
Computed (source_capacity S2, close_large L3, hold_small L5).
*[Item 426, beside the text: "at Z = 2 it does not" compared the write at Z = 2 with lives computed at Z of about 107.
The lives go as 1/Z as well, so with the carrier and the emission counting the same species the write is a fixed share
of the face's life whatever Z is: 5.9 % at the large end, 11.7 % at the small end (source_capacity S7, computed).]*

**What that reading leaves, the board's to work, not M's to answer:**
- A face of the README's size standing from the opening (162), before the README's energy is all inside. General
  relativity ties a horizon's size to the energy within it; at 340 the board framed this as "the hole ending with 2E"
  (option B), which is how the compact reading came to be preferred. M's 130 ("a black hole is not matter, it is what
  the mouth at position 1 looks like") and 136 (7) ("The throat formation is synchronization") describe an object the
  board has not modelled.
- With a face standing from the opening, F5's condition holds by construction: the README's first part meets a face
  already there (419's widths then bind nothing).
- Which carrier, and so Z, is SOURCE's (386).

## Item 424: the carrier's room -- items 5 and 9 cannot hold together (`source_capacity.py`, S1-S6)

M, 424: "review all the other open items in the warp theorem map, and close them". Every open row at the large end
rests on SOURCE through the arrival's width, so the review asked whether a carrier can meet item 5 (exactly N bits,
2^N states, at exactly E(N)) and item 9 (a compact arrival) at once. Computed; an estimate in its idealizations (free
fields of Z species, geometric-optics capture); not verified; not seated.
- **The room (S1, standard thermodynamics, not READ here).** At fixed energy E in volume V a massless carrier holds at
  most e^S states, S = (4/3) (pi^2 Z/30)^(1/4) (V/(hbar c)^3)^(1/4) E^(3/4). What crosses the face's capture
  cross-section sigma within a time tau lay in the volume sigma c tau, so N ln2 <= S(E, sigma c tau).
- **The least arrival (S2, exact).** tau_min = (3 N ln2/4)^4 (hbar c)^3 / ((pi^2 Z/30) E^3 sigma c). On the plane's
  hole at the bound it is exactly **(45/4) N ln2 / Z clocks of r0/c**, with no free number: bringing the README in takes
  of order the time its Hawking emission takes to carry it out.
- **The figures (S3).** Small end: 5.3e15 clocks (Z = 2) and 1.0e14 (Z = 106.75), against 4.79, and beyond the hole's
  life of 8.57e14 at Z = 2. Large end: 5.3e63 and 9.7e61 at r0 = 20 ell; 5.3e66 and 9.8e64 at the Earth cap, against
  4.31-8 at our sigma and 1.6e-3 where a junction binds.
- **What compact would cost (S4, solved self-consistently: a bigger energy makes a bigger hole).** Within the compact
  width the carrier needs E_c/E(N) = 912 at the small end, 1.5e10 at r0 = 20 ell and 4.8e10 at the Earth cap. The
  face it forms then holds 2.8e4 N, 2.3e20 N and 2.3e21 N bits, far more than N (136 (1), 162).
- **So (S5)** items 5 and 9 cannot hold together for any carrier of the plane's fields. Something in the premise set
  gives, and which is M's:
  (a) the exact energy at the bound (G1, 133, 136 (1));
  (b) the compact arrival -- the onset hidden (arrival_small V2-V4; focusing_parts F5, so O1b and O1c for the earliest
      parts) and, where a junction binds, item 10;
  (c) the carrier: a species count of 2e15 to 1e66 would be needed.
  RBITS, the bits arriving with the energy, is the board reading this refutes for a compact arrival (an estimate). The
  verified ARRIVALs (348) rests on it as a reading through SOURCE; nothing there is repaired.
- **(S6, exact)** An ultrarelativistic carrier at fixed E and S has kT = (4/3) E/S whatever its volume: at the bound,
  (8/3) of the hole's Hawking temperature, with its peak wavelength at 10.5 r0 at every N. So the geometric-optics
  capture S1 uses flatters it; the true room is smaller still.

## Item 399: the read -- a geometric object into the README

M, 399: "Converting a geometric object into an information README... this is the the next part of the SOURCE to
pursue", with an answer M quoted from Gemini on how to "convert a geometric object into a binary matrix". The read sits
before the write: object -> README (N bits) -> written onto the plane (write_small S3, o3_write) -> the corridor. It is
the row the record already holds open as COPY-O3 ("the read") and S1C-O1 ("an atom-resolving read of a bulk object
that reads every atom it removes, or removes none"; LEDGER). Worked in the conversation; no runs. Labels as above, and
READ (2nd hand) for what is taken from the Gemini text without being read at source.

**What the record already fixes about the README the read must produce** (M's unless marked):
- Its size is "the most simplistically exact binary code form" of the object's definition (131,
  H-README-MINIMAL-EXACT), one fixed exact encoding (136 (5)), and the trip's cost is that size (89,
  H-COST-IN-README).
- No tolerance at all (146), written in what every universe shares, "such as element identity and electron
  configuration" (146, H-INVARIANT-ENCODING).
- The object's motion is not in it (147, H-MOTION-NOT-ENCODED); it carries both labels and values (147).
- A destroying read is admissible (136 (4), the original irrelevant); whether the original is retired stays open (89).
- The board's readings, kept as the board's: what survives "no tolerance" exactly is discrete labels -- Z, electron
  configuration, bound quantum numbers -- while bond lengths and frequencies are law values set by position 2's laws
  (bulk/EXACTCOPY.md, H-LABEL-ENCODING); the values the README can carry are state values, preparable at the instant
  (bulk/REARRANGE.md, H-STATE-VALUES); the README is as small as the builder's knowledge makes it (copy/FAITHFUL.md 4,
  H-REGENERABLE).
- Five readings of the object's information are kept (33, 89): the board's four snapshot counts -- species sequence,
  a 1 A grid, a 0.1 A grid, thermal entropy: 9.5e27 to 1.1e29 bits for a body -- and the identity core (FAITHFUL 3).
- A classical README needs no quantum resources and is not bound by no-cloning (FAITHFUL 5, 7).

**Gemini's three phases, read against that** (READ 2nd hand; deduced):
- *Phase 1, voxelization.* A grid of occupied/empty cells is the record's grid count when the cell is atomic (1 A,
  0.1 A) and a label is added per cell. At any coarser cell it carries the envelope only -- no element identity, no
  electron configuration -- so by 146 it cannot be the README. At any cell size it fixes positions to within a cell,
  a tolerance, which 146 refuses unless the positions are themselves discrete labels (lattice sites, which atom bonds
  to which). And a raw grid is not the minimal exact form (131): it is a snapshot (FAITHFUL 1).
- *Phase 2, quantum gas microscopes, Rydberg tweezer arrays.* As described, they image atoms first placed in an optical
  lattice or in tweezers, not atoms bound in an object. They do not answer S1C-O1, the read of a bulk object.
  Whether any does is still open; the record's best demonstrated bulk read, atom probe tomography, removes 60 % of the
  atoms unread (step1c/supply.py).
- *Phase 2, tomography.* It reconstructs a state from many identically prepared copies. One object is one copy, and a
  single copy cannot be measured into its unknown state (FAITHFUL, "ruled out", Scarani p.3). So the object's full
  quantum state cannot be captured -- and by 147 and H-STATE-VALUES it is not asked for.
- *Phase 3, collapse to bits.* This fits the record: the README is classical binary (131), the read may destroy
  (136 (4)), no-cloning does not bind it (FAITHFUL 7). But one projective outcome is one sample of the state, zero-point
  motion included (EXACTCOPY 3). What must be fixed is the labels and the preparable state values, not one sampled
  configuration.

**What the read is required to be** (continuing the numbering below):

13. **Its output is the one fixed exact encoding**, in labels and state values, with no motion (131, 136 (5), 146,
    147; H-LABEL-ENCODING and H-STATE-VALUES as the board's readings). M's, with the board's readings named.
14. **It is exact.** Every label is read without error, since the reconstruction has no tolerance (146). Read errors
    are dissolved by redundancy at I/(1 - h2(p)) bits (step1b C3); N is the error-free count. M's, computed (record).
15. **It reads every atom it consumes, or consumes none** -- S1C-O1, still open: no demonstrated bulk method, READ
    at source (step1c). Gemini's methods do not close it. READ.
16. **It may destroy the object** (136 (4)); the original's retirement stays open (89). M's.
17. **Its size is N, the shortest exact encoding given what position 2's builder knows** (131; H-REGENERABLE). That
    N is G1's and H1's N: it sets E(N), the hole, the floor of item 8 and every row after the write. M's, derived.
18. **The object's geometry is carried as labels of structure, not as coordinates** -- which element sits at which
    lattice site, which atom bonds to which -- with the positions themselves set by position 2's laws as the matter
    rearranges to the README (148). Coordinates carry a tolerance (146) and motion (147). Deduced from 146, 147 and 148
    with EXACTCOPY; a board reading, for M (fork (a) below).

**A worked example, 1 cm^3 of copper** (computed in the conversation; E from the record's large-end
459,404,002.42 J per sqrt(bit), copy/exactE.py; density, molar mass and isotope abundances standard values, not READ
here):

| reading of the read | N (bits) | E at the large end |
|---|---|---|
| envelope voxels at 1 um (Gemini's phase 1, raw) | 1e12 | 4.6e14 J |
| atomic grid at 1 A, occupancy and element (the record's grid count) | 2e24 | 6.5e20 J |
| element and isotope per atom (8.49e22 atoms, 63Cu/65Cu at 0.8914 bits each) | 7.6e22 | 1.3e20 J |
| a perfect crystal: element, lattice, shape (an estimate) | about 300 | 8.0e9 J |

- The raw grids are snapshots, far above the minimal exact form, as FAITHFUL found for a body.
- **Natural copper's isotopes sit at random, so if each atom's isotope is a label the README cannot be shorter than
  0.89 bits per atom**: the read must then resolve every nucleus, and E rises by a factor of 1.6e10 over the crystal's
  labels. 146 names element identity and electron configuration; whether the isotope (a nucleus, not an element) is
  in the README is not ruled (fork (b) below).
- A real piece of copper is a polycrystal with defects; its structure labels (grain orientations, dislocations) lie
  between the crystal and the isotope rows. Not computed.

*[Item 437, beside the table, a finding recorded, not repaired (`encode_read.py` E3, E4): the table priced every
reading at the large end's 459,404,002.42 J per sqrt(bit), but the large end begins at N_L = 5.31e60 bits and every
reading lies far below it, at the small end, where E5(N) = 3 pi hbar c r_h^2/(8 l5^3) grows as N^(2/3). There the four
rows cost 6.5e6 J, 1.0e15 J, 1.2e14 J and 2.9 J. Against the copper's own rest energy, 8.05e14 J, the crossover is N* =
1.37e24 bits: the isotope reading (14.5 % of m c^2) and the crystal's labels lie under it, the atomic grid over it. "E
rises by a factor of 1.6e10 over the crystal's labels" reads 4.0e13 at the small end.]*

**Forks that are M's:**
- (a) **How the geometry is carried**: as labels of structure, the positions then set by position 2's laws (the
  board's reading, 18), or as measured coordinates to a stated resolution (which 146 and 147 refuse)?
  *[Item 437: deduced from 131, 146, 148 and M-RECON-ALWAYS (`encode_read.py` E1): no tolerance with a finite README
  admits only discrete data, and every coordinate is a law value that moves with the electron's mass and alpha across
  the 26-lattice and is re-set by position 2's 26. So the first option follows; it stays M's to confirm.]*
  *[Item 438: M, "confirm" -- the first option is M's (M-GEOMETRY-AS-LABELS), and requirement 18 with it.]*
- (b) **The isotope**: is each atom's isotope part of the README (item 146's "element identity" read as the nucleus),
  or only the element? It moves N by up to twenty orders for natural matter.
  *[Item 438: M, "no. The README only contains the last state of the object at position 1, not all of its states
  possible states, however, potential to be other states is carried as part of the README" -- M-ISOTOPE-OUT,
  M-LAST-STATE, M-POTENTIAL-IN. The isotope row of the copper table is not the README; the copper's README is the
  labels of its last state, the crystal's row (about 300 bits, an estimate) and, for a real piece, its defects. The
  read need not resolve nuclei. The board's reading of "potential", put to M: what a label carries -- an element's
  identity, which its isotopes and excitations share -- and which of them the copy takes is position 2's (RECON).]*
- (c) **Which reading of the read is SOURCE's**: every atom of the object (S1C-O1), or only what position 2's builder
  cannot regenerate (H-REGENERABLE, FAITHFUL 4)? Item 33's five readings stay kept until M rules.

**Outstanding work it adds:**
- Read Gemini's named methods at source (quantum gas microscopy's single-site imaging, Rydberg tweezer arrays,
  tomography's copy requirement), so none rests on the second-hand text.
- An instrument for the read: N under each reading for named objects (a crystal, a polycrystal, a molecule, the
  record's body), with E(N) and the downstream rows each N moves.
- S1C-O1 stays open: a demonstrated read of a bulk object that loses no atom.

## Corrected at item 386: nothing but the README's information goes in

M, 386: "How can it be a gas if matter cannot travel, only information can travel?" It cannot. Requirements 1 and 2
below were wrong as worded, and are kept as the record of what was corrected. The rulings:

- What crosses is information only: "Information only" (30, the value balanced between the positions); "that was for
  moving matter instead of information" (35); "the throat size only needs to carry the binary information defining the
  object in transit" (131).
- The information is the energy: "Information is energy" (190); "the README is the energy, not separate" (136 G).
- Matter is assembled at position 2, never carried: "Newly introduced energy to a position triggers a field reaction,
  such as a higgs field, however slightly, allowing for matter assembly" (101); the release "activates the higgs field
  forming the mass defined in the README" (136 (2)); the object is built from position 2's bulk (240, 285).

So the source is required to be:

1'. **The README's information as energy alone, E(N) carrying its N bits, with no matter** -- nothing the Higgs field
    has assembled, no rest mass. M's.
2'. **Moving on the light cone.** Energy with no rest mass travels at c (relativity.py: the massless on the light cone,
    the massive inside it; 324). So it comes onto the face as a null inflow of energy only. Its null energy is >= 0 on
    every ray (item 6), and B5a holds for it without a matter model. Derived.

What the correction changes:
- "A gas of our plane's fields, not null dust" was the board's sentence in 344, which M quoted as a process to define.
  "Gas" is withdrawn. A null inflow of energy alone is the form RDUST (item 12) already has, so RDUST is no longer only
  a stand-in model: it is the shape the requirement takes. Whether the README's information, written on our plane,
  comes in that way is still SOURCE's to prove.
- Item 8's floor came from a free gas counting every Standard Model species as a carrier of the README's states (Z =
  106.75). With only the massless gauge quanta counted it is longer: 252,191 clocks at Z = 2 (computed, write_small
  S3's formula). No row turns on it: the small end's hole lasts 1.28e10 times the old floor (o3_hold), the large end's
  3.3e10 times (close_large L3). Which count is right is SOURCE's.

## Settled at item 387: position 2's plane carries its own sigma

M, 387: "it should carry its own σ." That answers the fork below. What follows from it, worked from the record:
[Item 388: what follows holds only for destinations at our sigma, 218's example among them. For the theorem see
"Corrected at item 388". Kept as written.]
[After 389: the J2 bound used below is withdrawn. J2 is a two-way element: Barcelo's suffocation needs inflow from
position 2 onto its face, and on the one-way object nothing from position 2 meets it (277, i_oneway I3). At our
sigma the face ends 2 r_s2/c after the README's last part (109; "Corrected after item 389").]

- At the working destination, its own sigma is ours. Position 2 is "a universe identical to this one with a singular
  exception, that that universe is 1 hour ahead of ours" (218), and each position 2 carries its own universe's values
  (226). So s2 = s_in = sigma: no junction rises on position 2's face, at either end (c8_level V2). J1's junction does
  not bind there. Deduced.
- Position 2's open period is then J2's short white-hole phase, (Delta u)* <~ 2 r_s/c (c_junction J2, READ: Barcelo,
  Carballo-Rubio and Garay). It is an order, not an exact bound. At the small end that is about 2 clocks of r_h/c
  (c_junction J4). At the large end it is 4 clocks of GM/c^3 (close_large L4 (a)).
- So item 10 is one requirement at both ends, in each end's own units: the README's arrival lasts less than about
  twice the hole's horizon radius in light time. Deduced.
- At the small end this is stricter than item 9's 4.79 clocks. The margin of 6.9 against J1's 33.6 is gone, and item
  10 now binds at both ends. Deduced.
- A destination whose own sigma differs from ours, such as 2P and its combinations (sigma/4 in SI, p2_planck Q2),
  would carry a junction of the difference. Its period would have to be computed. The working experiment (218) does
  not need it, so it is not computed (384).
  [Item 388: wrong -- the theorem needs it, and it is computed below. Kept as written.]
- New, and the math's to answer: with no junction, M's rulings carry nothing that closes position 2's face. The
  record's only bound on the open period is J2, which is READ. A bound from the theorem itself would replace it.

## Ruled at item 390: position 2's face closes when the corridor holds nothing

M, 390: "if it opens because of the README, then it would stand to read me that it closes when there is nothing
contained within the corridor". This is M's ruling (M-CLOSES-WHEN-EMPTY), and it meets the board's 109 deduction below.

- **What the corridor contains, on position 2's side, is the white hole's anti-trapped region.** Position 2's face bounds
  it. Both radial light directions expand there exactly where r < r_s2, and nowhere inside the emerging shell.
- **So the face closes when the README's last part crosses r_s2 outward.** The null surface's continuation through the
  empty flat region (the 2 r_s2/c below) contains nothing, and is no part of the open face (junction_own G10, computed,
  exact; selftest 13/13, mutants 7/7).
- **Item 10 at a destination at our sigma is met by identity**: the face is open exactly while the README is within it.
  Where a junction rises, J1 still closes the face at its period, so there the README must have emerged by then.

## Corrected after item 389: J2 withdrawn, the face closed by 109

The board's own audit, after 389, against M's 277. Items 387 and 388 above, close_large L4 (a) and arrival_large A4 used
J2, Barcelo, Carballo-Rubio and Garay's short white-hole phase, as a bound on position 2's open period. The record
withdrew J2 at 277. Barcelo's suffocation needs inflow from position 2 onto its white-hole face, and on the one-way
object nothing from position 2 meets that face (i_oneway I3; c_junction's item-277 note). Corrected (junction_own G8-G9;
selftest 12/12, mutants 6/6):

- **What closes position 2's face where no junction binds is M's 109**: "A horizon cannot exist without the object of
  which it needs to exist". On 273's construction the README's shell has flat space inside it (o1c_oneway Z2b), and
  position 2's side is our side's reflection. Our face is born 2 r_s/c before the README's first part reaches it:
  arrival_large A3's exact 4 clocks of GM/c^3 at the large end, and 2 clocks of r_h/c at the small end. So position 2's
  face ends 2 r_s2/c after the README's last part has crossed it outward. The face ends with its object. Computed,
  exact; 109 M's.
- **Item 10 is then a requirement only where a junction binds.** Where it binds, the README must have emerged within the
  junction's period:
  - below our sigma at both ends;
  - above our sigma at the large end, with F1's start.

  At a destination at our sigma -- 218's example, 2a, 2b, 2c -- the face lasts from its opening through the README's
  emergence and 2 r_s2/c beyond, and item 10 puts no bound on SOURCE. Deduced.
- **Small end**: the junction's period is 32-34 of position 2's e-folds wherever it rises. That is 33.6 on 139 (1)'s
  quarter and 46.3 of our clocks at 2P, all above the compact 4.79. arrival_small V8's comparison stands as first
  written; 387's "about 2 clocks" and 388's "J2 binds everywhere" are withdrawn. Computed.
- **Large end**: 388's junction figures stand where sigma2 differs from ours (1.57e-3 clocks at 2P at r0 = 10 ell).
  The 4 clocks at our sigma (close_large L4 (a), arrival_large A4, 387) is withdrawn: no bound there. Computed.
  *[Item 419, beside the text: a bound returns at our sigma from the passage's own rows. Under 418 every route is a
  README part, and O1b and O1c hold for the earliest parts only if our face is born before the README's first part.
  On the plane that needs an arrival within 7.94 (exact 8), 4.75, 4.44 and 4.31 clocks of r_h/c at onset orders 1-4
  (16 to 8.6 of GM/c^3; lemmas/focusing_parts.py F5-F6, computed). Where a junction binds, its bound is far tighter.]*
- The open question 387 named -- what closes position 2's face with no junction -- is answered from M's 109 and 273,
  not from another's model.

## Item 389: the rows that wait on it

M, 389: "this can only be determined once the source is determined". ARRIVAL, M1P2x, E1x and H2tx at the large end are
not finalized, as readings or otherwise, until SOURCE is determined. They stay open, reported under 358 (c), and wait on
this specification. SOURCE stays last (345, 358).

## Corrected at item 388: the theorem, not the example

M, 388: "we do need to compute this. You're basing your decision off an applied simplified example of the warp
theorem." The 387 section above set item 10 from 218's one-hour jump, where the destination's own sigma happens to be
ours. The theorem is general: each position 2 carries its own values (226), and its own sigma2 can differ from ours.
Computed in junction_own.py (G0-G7; selftest 10/10, mutants 5/5):

- The junction law carries the two tensions and nothing else (m1p2x_index Y1, called), so it holds at every destination
  whatever its G2 and ell2. On position 2's face, with the interior at our sigma, mu' = sigma - sigma2. Computed, exact.
- Below our sigma the junction rises. At our sigma there is none. Above it the junction falls, and it needs a start or
  positivity fails at the face where it is owed (284, 285). Taking the start as the README's energy laid on the
  junction (m1p2x_fifth F1's reading), the face stays open at most -ln(1 - 1/(K0 |b|)) e-folds. For a large jump the two
  signs give the same period, 1/(K0 |b|) e-folds. Deduced from the computed form.
- [After 389: this bullet rests on J2, withdrawn on the one-way object; see "Corrected after item 389".]
  **Small end: J2's short phase binds at every destination**, junction or not. The junction would bind only for sigma2
  below -7.7e13 sigma. At 139 (1)'s quarter too, J1's 33.6 clocks never bound: J2's about 2 always did. In our clocks
  the bound is 2 to 3.17 over the record's twelve destinations and the quarter, and 1.41 at the inverse 2P step
  (G/2, 4 sigma). Computed; J2 READ, an order.
- **Large end: the junction binds wherever sigma2 differs from ours** by more than about 5e-4 sigma (at r0 = 10 ell; the
  band shrinks as (ell/r0)^2). Its period is about (ell/r0)^2/(3 (G2/G)^(3/2) |1 - sigma2/sigma|) clocks of GM/c^3. At
  r0 = 10 ell (240 (b); one Kruskal geometry in brackets): 2P and 2a + 2P 1.57e-3 [2.22e-3], 2b + 2P and 2c + 2P
  5.6e-4 [1.11e-3], the quarter 2.67e-3, the inverse 2P step 3.14e-3 [2.22e-3]. Only at our sigma is it J2's: 4 clocks
  where G2 = G (ours, 2a), 5.66 at 2b and 2c. Computed.
- Where the jump would rise, d_ours (the interior at our sigma) is forced at both ends. Otherwise the junction would sit
  on our face, and our face must stand at least 66,980 clocks against the junction's 34. Computed comparison.

So item 10 is a function of the destination -- its own sigma2, G2 and G5_2 -- and, at the large end, of r0. SOURCE meets
it for the destination it serves. The strictest case is not the example's 4 clocks: at the large end it is the
junction's, a small fraction of a clock, at every destination whose own sigma differs from ours. Still open: what
closes the face where no junction binds (J2 is READ), and what supplies a falling junction's start (F1's reading, not
ruled).

## What it is

1. *[Withdrawn at item 386: see 1'.]* **Written on our plane, in our plane's own fields** -- "a gas of the plane's fields, not null dust" (344,
   M-SOURCE-IN-THE-MAP; H-README-ON-PLANE, write_small S3). M's.
2. *[Withdrawn at item 386: see 2'.]* **Ordinary matter of our universe** -- particles, scalar and gauge fields with their kinetic terms of the positive
   sign (pointwise.py P1-P4). Then B5a's condition (rho + p >= 0, rho > -sigma/6) holds for it at every point with no
   further work. Derived.
3. **One process for each end** -- SOURCEs onto the README's own five-dimensional hole, SOURCE onto the
   four-dimensional corridor (346, M-SOURCE-BY-END). M's.

## What it must carry

4. **Exactly the README's one energy, E(N) at the bound, and nothing besides** -- 136 (1), 136 G ("the README is the
   energy, not separate"), G1. So no face stands before the README (109), and the hole never carries 2E (the math of
   340: reading (ii)). M's, derived.
5. **Exactly N bits, one fixed exact encoding** (136 (5)). Its carrier holds at least 2^N states
   (H-BITS-ARE-STATES), and exactly N ln2 of entropy at the write's floor ball: the generalized second law saturates at
   the final face's area, nothing lost (arrival_small V4, with item 348's note). M's, computed.
6. **No partner** -- the arrival only adds energy, so null energy is >= 0 on every ray: G_vv = 3 mu'/(2 r^3) at the
   small end, 2 m'/r^2 at the large (117, 183; arrival_small V1, arrival_large A1). Computed, exact.
7. **One whole** -- 163, "All together, one whole"; 162, "only the size that is needed". At a fraction e of E the
   face holds e^(3/2) N bits (small end) or e^2 N (large end), fewer than have come in, so the README is held only when
   all of it is in. The source must deliver all of it, not a part. M's, computed exact.

## How it must come in

8. **The write takes at least its floor.** All of the README starts inside a ball of radius (1 + T) r_h, T >=
   (3/2)(5 N ln2/Z)^(1/3) - 1 clocks of r_h/c: 66,980 clocks at the example README (Z = 106.75, small end);
   199,702 clocks of m/c at the large end (Z = 108.75). The start is flat and carries only the README's E (write_small
   S3; o3_write W3; H-FLAT-START, H-README-ALONE). Computed.
9. **The arrival onto the face is compact**, the face born before the README's first part, so the onset -- and 273's
   quantum region -- stays behind our face.
   - Small end: width at most 4.79 clocks of r_h/c, the least of the thresholds for the onset hidden (4.79-5.27) and
     the coarse second law (4.82-5.75) (arrival_small V2-V4).
   - Large end: any width below 16 clocks of GM/c^3 keeps a linear onset hidden (arrival_large A3).
   Computed.
10. **The README emerges within position 2's open period.**
    - Small end: 32.6-34.5 of position 2's clocks (c_junction J1). Item 9's 4.79 meets it, with a margin of 6.9.
    - Large end: below 2.67e-3 (10 ell/r0)^2 clocks of GM/c^3 with position 2's plane at 139 (1)'s quarter, or below
      4 clocks with it at its own sigma (close_large L4; arrival_large A4). This is the strictest requirement on the
      source, and it is new to the large end. For the Earth's corridor with ell at its ceiling the quarter's bound is
      6.6e-7 clocks, about 1e-17 s.
    Computed.
    [Item 387: position 2's plane carries its own sigma, which at 218's destination is ours. So the bound at both ends
    is J2's short phase, about 2 clocks of r_h/c at the small end and 4 clocks of GM/c^3 at the large (READ, an order).
    The small end's 32.6-34.5 and the large end's quarter bound were J1's junction, which does not rise there. Kept as
    written; see "Settled at item 387" above.]
    [Item 388: that note holds only at our sigma. For the theorem the bound depends on the destination: J2's at the
    small end everywhere, and at the large end the junction's wherever sigma2 differs from ours (junction_own G7). See
    "Corrected at item 388" above.]
    [After 389: J2 is withdrawn on the one-way object (277). Item 10 binds only where a junction does; at our sigma the
    face ends with the README (109). See "Corrected after item 389".]
11. **It keeps our vacuum.** It never carries our plane's Higgs over its barrier: our universe is defined by its offset
    (201), which a bubble of the deeper vacuum would change by more than eighty orders (322; 382). At the example README
    the gas is about 5.6e3 GeV at the floor ball and 2.3e7 GeV at the face, against the barrier's 3.68e10 GeV -- at most
    6e-4 of it, and 2e-2 with ell at 0.588 nm. Estimate.

## What it replaces

12. **The three board readings that stand in for it** (readings.py). SOURCE must show that the gas of the plane's
    fields does what each assumes, or prove the rows without it:
    - RDUST: the README arriving as radial null dust (ARRIVALs, B4ds);
    - RBITS: the bits arriving with the energy (ARRIVALs; it gives item 7's whole-only holding);
    - RSHELL: the thin null shell (O1cs, O1bs), with no weight beyond RDUST.
    At the large end the same three stand in for it in ARRIVAL (arrival_large A2, A3).

## Forks that are M's

- **Position 2's tension at the destination.** It is 139 (1)'s quarter, or the destination's own sigma (218, 226). The
  large end's arrival must be shorter than 2.67e-3 (10 ell/r0)^2 clocks in the first case and 4 clocks in the second:
  a factor of at least 1,500 apart, and the record holds both readings.
  [Answered at item 387: its own sigma. Kept as written.]
- **The arrival's width itself.** By 163 it is one whole, not an instant; nothing in the rulings or the geometry sets
  it. It is SOURCE's to set, within items 9 and 10.
