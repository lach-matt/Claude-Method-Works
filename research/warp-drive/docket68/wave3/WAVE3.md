# DOCKET 68 wave 3 — the corridor (verified once, corrected; not seated)

Opened on M-RULINGS item 34 ("Corridor (D68 wave 3)"). The charter section is in `docket68/CHARTER.md` (wave 3).
There are four instruments, all stdlib + numpy; each imports its owners and READs outside results at source, with the
route recorded. Each instrument was verified adversarially in both directions on 2026-10-05, and every finding was
applied; the history is kept in each file's docstring. **Not seated** until M has seen it.

| item | file | selftest |
|---|---|---|
| W3A the A–B coupling | `corridor.py` | 17/17, 4 controls, 3 STRUCTURAL |
| W3B the twelve criteria | `criteria12.py` | 14/14, 3 controls, 3 STRUCTURAL |
| W3C ranking seats | `seatrank.py` | 14/14, 3 controls, 2 STRUCTURAL |
| corridor size (M's question, item 35) | `aperture.py` | 9/9, 2 controls, 1 STRUCTURAL |

## W3A — the corridor as the A–B coupling (M items 21–22)

The model is one excitation on two positions, H = J(|A⟩⟨B| + |B⟩⟨A|). That is Christandl et al.'s N = 2 chain
(quant-ph/0309131v2, READ).

- **Never in between holds in the two-site model, which is H-DIRECT-COUPLING.** Only A or B is ever found; this is
  true by construction and printed STRUCTURAL. On any **relayed** chain it fails. At half the transfer time the object
  is found between A and B with probability 0.50 (N = 3), 0.75 (N = 4), 0.98 (N = 8) and 0.9999 (N = 16), all
  computed. The *mean* position passes between A and B even in the two-site model.
- **"The entanglement of two positions at once" is the mid-transfer state.** Its mode concurrence is 1, under
  H-MODE-ENTANGLEMENT, which is a contested reading of a single excitation.
- **A coupling is a channel.** On/off keying gets through, with a deviation of 0.5. Two controls give none: the same
  protocol with J = 0, and a Bell pair (entanglement alone). The state itself moves with the fixed phase F(t*) = −i,
  so no classical bits are needed.
- **Where distance enters.** The two-site time π/2J has no distance in it. Relayed, distance returns:
  - In a uniform chain, arrival time is linear in N, at speed 2J.
  - Christandl's engineered chain transfers perfectly at π/λ. With bounded coupling its time doubles each time N
    doubles.
  - At half the light-cone time the amplitude falls about 90× per 10 sites. Near the cone the decay is weak.
  - This is the short-range Lieb-Robinson bound (Nachtergaele & Sims arXiv:1004.2086v1 Thm 2.3, READ): "non-relativistic
    quantum dynamics has, **at least approximately**, the same kind of locality structure provided in a field theory by
    the finiteness of the speed of light".
- **The speed-free set, stated fairly.** "No speed" holds iff any one of these holds:
  - H-DIRECT-COUPLING.
  - **H-LONG-RANGE with α < d.** Eldredge et al., arXiv:1612.02442v2 (READ): "If α < d, the state transfer time is
    asymptotically independent of L". This is realised in polar molecules, Rydberg atoms and ions, as quasi-static
    interactions. Their fn. 45 caveat: for α ≤ d a volume prefactor 1/L^(d−α) multiplies the time.
  - **Unbounded J.**

  Each of these clashes with relativistic microcausality at the fundamental level (H-LOCALITY). A quasi-static
  interaction is the non-retarded limit of a field that travels at c. An effective direct term (H-EFFECTIVE-COUPLING)
  needs a mediator already spanning A to B.
- **Before light** (the board's DEF-BITS). The coupling beats light across the Proxima span iff J > πc/(2L). That means
  **ħJ > 7.7e-24 eV per qubit** in parallel. Serially, the whole object needs ħJ > 73 keV (species count) to 839 keV
  (0.1 Å count).
- **Grade (proposed):** O-BITS REMOVED-IF all three of:
  - one of H-DIRECT-COUPLING, H-LONG-RANGE (α < d), or unbounded J;
  - J > πc/2L;
  - H-STATE-AS-BITS.

  Each speed-free option clashes with H-LOCALITY. O-SEAT is untouched (H-INFO-SHAPE). O-LOOP goes through corridors.py's
  H-FRAME, under H-CORRIDOR-AS-IDENTIFICATION.

## W3B — the twelve criteria at A and B (M items 23–24)

- **By kind** (settle.H12's class column):
  - 2 emergent: M, R.
  - 2 material: K, T.
  - 8 others: CP, α_s, θ (Lagrangian parameters), Z0 (derived), Λ, G (coupling), G_F (Lagrangian-derived) and v (a
    field's expectation value). These are not independent: Z0, M and R reduce to α, and G_F is tied to v.
- **Earth against Proxima b.** The only READ spatial bound is α's coupling to the potential, 14(11)e-9. It was measured
  on the annual variation of the Sun's potential, ΔΦ/c² ≈ 1.65e-10. Applying it to the computed ΔΦ/c² = −1.5e-8, about
  91× that lever arm, needs **H-LINEAR-PHI**. Under it, **|Δα/α| ≤ 3.8e-16** at the 1σ upper end, or 5.4e-16 at 2σ;
  the central value is −2.1e-16. The other seven criteria have no READ spatial bound; they are equal under
  H-UNIFORM-CONSTANTS.
- **H-12Q (M chose "literally quantum-correlated").** Three cases, each computed:
  - A definite value at both seats carries no mutual information and no entanglement.
  - A shared but uncertain value carries MI of 1 bit and no entanglement. This is the reading M set aside.
  - A Bell pair carries quantum MI 2 and entanglement 1.

  So H-12Q needs criteria that are quantum observables. H12 marks α_s, Z0, G, G_F and v as field carriers and CP, Λ,
  θ as conditional. **settle.py's H-12-CARRIER** is a constant whose value depends on the quantum state. For α_s, G and
  v it has **no READ bound and is NOT excluded**. It is the nearest thing on the board to M's "predetermination ...
  based on the starting state".
- **Vacuum entanglement between the seats** is extractable **at any separation**. Reznik, Retzker & Silman
  quant-ph/0310058v2 (READ) find negativity ≥ e^−(L/cT)³, numerically ≥ e^−(L/T)². After filtering, CHSH is violated
  "for every separation distance, L". At the Proxima span with T = 1 yr the bound is ≥ 10^−7.8: tiny, not zero. What
  decays is the *extracted* amount, which is a lower bound on the vacuum entanglement. Reznik 2003's L/T < 1.1 belongs
  to his cos² window only; at this span that window gives 3.86 ≤ T < 4.25 yr.
- **Predetermination (M item 23).** The test reduces to the stock gate under four hypotheses (H-UNIFORM-CONSTANTS,
  H-LINEAR-PHI, H-SAME-COMPOSITION, H-SAME-ISOTOPES) and with H-12-CARRIER false. This is assigned from those
  hypotheses, so it is printed STRUCTURAL.
  - The gate needs 749.1 kg of CI-chondrite stock, with P as the binder (H-CI-PROXY).
  - It is **OPEN at Proxima**, because P is unmeasured there.
  - With H-12-CARRIER true, a state-dependent criterion could distinguish seats. That branch is OPEN.

## W3C — ranking seats by signed magnitudes (M item 25, H-SEATRANK)

- **The aggregate.** P = 1 + N is true by normalisation of every signed measure, so it is printed STRUCTURAL. It
  neither tests nor supports the per-seat claim.
- **Unconstrained, the negatives fix only the total.** (0.7, 0.5, −0.2) and (0.5, 0.7, −0.2) share their negatives but
  rank opposite seats first.
- **In a physical family the negatives do locate the positive peak** (H-CONSTRAINED-FAMILY). Over 2,836 qubit states
  cosθ|0⟩ + e^{iφ} sinθ|1⟩, the location and depth of the negative minimum predict the peak's location to a median of
  0.071, about 1.4 grid steps. A random pairing gives 1.08, and the error falls as the family is sampled more densely.
  The peak lies opposite the minimum. **This supports a literal "triangulate" given knowledge of the family.** It does
  not show the negatives decide alone.
- **Projections recover peak and negatives together** (signed.fbp, sup01, H-WIGNER-SEATS). The argmin is exact at
  K = 4 and the argmax exact from K = 8. Here the projections are the input and the negatives an output, so this is
  tomographic triangulation, not M's mechanism.
- **Cost of resolving a weak difference** (H-WEAK-AS-DELTA). This matters only if seats are *estimated by sampling* the
  quasi-distribution (H-QUASI-SAMPLING). Pashayan et al.'s eq. 12 (READ) gives a Hoeffding **sufficient** count
  2M² ln(2/δ)/Δ². The **typical** (CLT) cost grows about **linearly** in M at fixed seat weights. For seats 0.30 vs
  0.25:

| M | typical (CLT) samples |
|---|---|
| 1 | 593 |
| 5 | 2,970 |
| 21 | 12,500 |

  Empirically at M = 5, 2e4 samples ordered the seats correctly in every trial, while the sufficient bound asks for
  7.4e4. **Measured** seats carry no M factor (Pashayan eq. 1): negativity "bounds the efficiency of a classical
  estimation".
- **Grade (proposed):** these findings move no obstruction grade. H-SEATRANK ranks seats and supplies none.

## How big must the corridor be if only information passes? (M item 35)

M: "If information is what is being sent, how big does the corridor actually have to be? We assumed 1 meter, but that
was for moving matter instead of information". The 1 m throat was sized for a body, and costs 5.36e25 kg. The
**smallest opening consistent with each reading** is:

- **(A) Hold the whole description at once.** r = 7.4e-22 to 2.5e-21 m (`throatbits.r_fit`; a capacity ceiling, not an
  encoding).
- **(B) Stream it over one mode at the floor energy.** The minimum opening is about half the channel quantum's
  wavelength, so it scales as T/I. For the species count it is 6.5e-15 m in a day, 2.4e-12 m in a year and 2.4e-10 m
  in a century; a faster schedule *permits* a narrower one. Caveats:
  - At width λ/2, 61 % of the floor channel's entropy flux lies below the cutoff, so it needs more width or more power.
  - A TEM line has no cutoff at all.
  - A circular guide's radius is about 0.59 × (λ/2).
- **(C) As a coupling, no cross-section at all.** ħJ = ħIπ/(2T): 312 keV at 1 yr.

As a geometric throat, these sizes lower the throat mass by 4e9 to 1.4e21 relative to 1 m. The board's other limits
on small throats stand as graded.

## Named hypotheses

- **W3A:** H-DIRECT-COUPLING, H-LOCALITY, H-LONG-RANGE, H-QUASI-STATIC, H-EFFECTIVE-COUPLING, H-BOUNDED-J,
  H-ONE-EXCITATION, H-MODE-ENTANGLEMENT, H-STATE-AS-BITS, H-CORRIDOR-AS-IDENTIFICATION, H-INFO-SHAPE.
- **W3B:** H-12Q, H-UNIFORM-CONSTANTS, H-LINEAR-PHI, H-CONSTANTS-ARE-FIELDS, H-12-CARRIER, H-REZNIK-WINDOW,
  H-CI-PROXY, H-SAME-COMPOSITION, H-SAME-ISOTOPES.
- **W3C:** H-SEATRANK, H-SEAT-QUASI, H-CONSTRAINED-FAMILY, H-WIGNER-SEATS, H-QUASI-SAMPLING, H-WEAK-AS-DELTA,
  H-NOISELESS.
- **Corridor size:** H-HALF-WAVE, H-TEM-LINE, H-TE11, H-THERMAL-1D, H-CAP-AT-THROAT.

## OPEN

1. Speed-free coupling: each route (direct, long-range α < d, unbounded) clashes with H-LOCALITY.
2. H-12-CARRIER for α_s, G and v: no READ bound excludes a state-dependent constant.
3. The stock gate at Proxima: P is unmeasured.
4. Whether the seat quasi-distribution is a Wigner function (H-WIGNER-SEATS) or belongs to a known family
   (H-CONSTRAINED-FAMILY).
5. "Complex binary" (M item 25): not addressed in W3C. The board's reading of complex values is signed.py's Im H = πN.
6. Spatial bounds on the seven constants with none READ here.

## History

The first-pass figures and claims that verification corrected are kept in each file's HISTORY block. In short:
- Reznik's L/T < 1.1 had been generalised beyond its window.
- H-12-CARRIER was omitted.
- The α extrapolation was unnamed.
- A worst-case sampling bound was read as a requirement.
- Projections were credited to M's negatives.
- "Never in between" was stated without its two-site condition.
- The O-BITS grade lacked "before light".
- Long-range relays were omitted.
- Corridor widths were stated as required widths rather than minima.
- Several counted checks could not fail.
