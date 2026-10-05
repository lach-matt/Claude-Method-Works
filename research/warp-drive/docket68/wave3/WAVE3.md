# DOCKET 68 wave 3 — the corridor (first pass, 2026-10-05; not seated)

Opened on M-RULINGS item 34 ("Corridor (D68 wave 3)"). The charter section is in `docket68/CHARTER.md` (wave 3). There
are three instruments, all stdlib + numpy; each imports its owners and READs outside results at source, with the route
recorded. Nothing here is seated until it has been verified.

| item | file | selftest |
|---|---|---|
| W3A the A–B coupling | `corridor.py` | 14/14, 2 controls, 1 STRUCTURAL |
| W3B the twelve criteria | `criteria12.py` | 12/12, 2 controls, 1 STRUCTURAL |
| W3C ranking seats | `seatrank.py` | 10/10, 2 controls, 1 STRUCTURAL |

## W3A — the corridor as the A–B coupling (M items 21–22)

The model is one excitation on two positions, H = J(|A⟩⟨B| + |B⟩⟨A|). That is Christandl et al.'s N = 2 chain
(quant-ph/0309131v2, READ).

- **Never in between holds.** The position observable has exactly two eigenvalues, so every measurement finds A or B.
  The transfer is complete at t* = π/2J, reproducing Christandl's F(π/2) = −i. Nuance: the *mean* position passes
  between A and B (399 of 401 sampled times); no single outcome does.
- **"The entanglement of two positions at once" is the mid-transfer state.** Its mode concurrence is 1, which is
  maximal.
- **A coupling is a channel.** B's occupation depends on what A prepared, with a deviation of 0.5. The control,
  entanglement alone (a Bell pair with J = 0), does not signal. So the coupling carries the state with no classical
  bits.
- **Where distance enters.** The two-site time contains no distance. Relayed through local physics, distance comes back:
  - In a uniform chain, first arrival grows linearly with N, at slope 0.5 per site (speed 2J).
  - Christandl's engineered chain transfers perfectly at π/λ, but with bounded coupling the time doubles each time N
    doubles.
  - The amplitude outside the light cone falls about 100× per 10 sites. This is Lieb-Robinson, Nachtergaele & Sims
    arXiv:1004.2086v1 Thm 2.3 (READ): "the same kind of locality structure provided in a field theory by the
    finiteness of the speed of light".
- **Grade (proposed):** O-BITS REMOVED-IF {H-DIRECT-COUPLING}, and H-DIRECT-COUPLING clashes with H-LOCALITY. O-SEAT
  is untouched, since the coupling moves state, not substance. O-LOOP is governed by corridors.py's H-FRAME, recorded
  and not re-derived.

## W3B — the twelve criteria at A and B (M items 23–24)

- **By kind** (settle.H12's own class column): 8 constants (CP, α_s, Z0, Λ, G, G_F, θ, v), 2 emergent (M, R), and 2
  material (K, T).
- **Can they differ between Earth and Proxima b?** The two seats are joined at one moment, so what matters is a
  *spatial* bound. The only READ one is α's coupling to the gravitational potential, 14(11)e-9. Applied to the computed
  ΔΦ/c² = −1.5e-8, it gives **|Δα/α| ≤ 3.8e-16**. M and R inherit that bound. The other constants have no READ spatial
  bound and are equal under H-UNIFORM-CONSTANTS.
- **H-12Q.** A criterion with a definite value at both seats carries no mutual information and no entanglement. The
  seats *agree*, which is classical equality. The control is a Bell pair, with quantum MI 2 and entanglement 1.
  "Literally quantum-correlated" is therefore non-trivial only if the constants are fields (H-CONSTANTS-ARE-FIELDS).
  Field vacua are entangled between separated regions, but the entanglement can be extracted only for L/T < 1.1
  (Reznik quant-ph/0212044v2, READ). At the Proxima span that means probes switched on for **≥ 3.86 yr**, against a
  light time of 4.25 yr.
- **Predetermination (M item 23).** Ten criteria decide nothing between seats. The two material ones are properties of
  the object's own materials. The test therefore **reduces to the stock gate**, computed from the starting state, and
  it is **OPEN at Proxima** because the binder P is measured nowhere in the system.

## W3C — ranking seats by signed magnitudes (M item 25, H-SEATRANK)

- **Exact in aggregate.** For any normalised quasi-distribution, P = 1 + N, so stronger negative magnitudes force
  stronger positive magnitudes "automatically". This is printed STRUCTURAL; the control is an unnormalised weighting,
  which breaks it.
- **Not per seat from the negatives alone.** (0.7, 0.5, −0.2) and (0.5, 0.7, −0.2) share their negatives but rank
  opposite seats first. With the negatives fixed and the positives permuted, the top seat moves in 0.665 of cases
  (1 − 1/n_pos predicts 0.671).
- **Triangulation from projections recovers the ranking** (signed.fbp, imported). With K = 4 projections the top seat
  is located to one grid step; from K = 16 it is located exactly, together with the negative minimum. With K = 2 it is
  off by 0.81.
- **Weak correlations cost more with more negativity.** By Pashayan et al. (arXiv:1503.07525v2 eq. 12, READ),
  separating two seats whose weights differ by Δ takes 8M² ln(2/δ)/Δ² samples, with M = 1 + 2N.

| N | M | Δ = 0.01 | Δ = 0.001 |
|---|---|---|---|
| 0 | 1 | 2.95e5 samples | 2.95e7 samples |
| 2 | 5 | 7.38e6 samples | 7.38e8 samples |

  The estimator check on w = (0.6, 0.55, −0.15) gives a mean of 0.547 against a true 0.55, and a variance of 0.412
  against a predicted 0.4125. So stronger negativity *raises* the cost of resolving a weak difference, by M².
- **Grade (proposed):** H-SEATRANK holds in aggregate (an identity); it is not fixed per seat by the negatives alone;
  the ranking is recovered with the negatives from projections; and negativity raises the sampling cost. It moves no
  obstruction grade, because it ranks seats and supplies none.

## Named hypotheses

H-DIRECT-COUPLING, H-LOCALITY, H-ONE-EXCITATION, H-BOUNDED-J (W3A); H-12Q, H-UNIFORM-CONSTANTS,
H-CONSTANTS-ARE-FIELDS, H-REZNIK-WINDOW, H-SAME-COMPOSITION, H-SAME-ISOTOPES (W3B); H-SEATRANK, H-SEAT-QUASI,
H-WIGNER-SEATS, H-NOISELESS (W3C).

## OPEN

1. A direct A–B coupling: no local interaction supplies one (H-DIRECT-COUPLING against H-LOCALITY).
2. Spatial bounds on the seven constants with none READ here.
3. The stock gate at Proxima: P is unmeasured.
4. Whether the seat quasi-distribution is a Wigner function, so that its projections are measurable (H-WIGNER-SEATS).

## History

- `criteria12.py`'s last control was first written vacuous: it compared against a branch that could never be taken.
  It was rewritten to pass the measurement in as a parameter, so it now tests the logic.
- `seatrank.py` first counted the identity P = 1 + N as a check. It cannot fail for a normalised weighting, so it is
  now printed STRUCTURAL; a control shows it failing when the sum is not 1.

## How big must the corridor be if only information passes? — `aperture.py`, 9/9 pass, 2 controls

M: "If information is what is being sent, how big does the corridor actually have to be? We assumed 1 meter, but that
was for moving matter instead of information". The 1 m throat was sized for a body; as a throat it costs 5.36e25 kg.
Information sets the size three ways, computed for all four counts:

- **(A) All at once.** The smallest throat whose holographic capacity A/4 holds the whole description
  (`throatbits.r_fit`, DOCKET 66) has **r = 7.4e-22 to 2.5e-21 m**, which is about 1e14 Planck lengths. Its throat
  mass is 4e4 to 1.3e5 kg. This is a ceiling on what a throat that size can hold, not an encoding anyone has built.
- **(B) Streamed over one mode.** One mode carries any amount of information, given time. At the board's energy floor
  for a 1D thermal channel, the channel's quantum is kT = 2 E_bit / ln 2. That relation is derived from LNM's 1D law
  and checked against `seat.channel_floor`'s own rate. The opening must be at least about half the quantum's
  wavelength (H-HALF-WAVE). For the species count:

| schedule | quantum | opening | throat mass |
|---|---|---|---|
| 1 day | 96 MeV | ≥ 6.5e-15 m (nuclear scale) | 3.5e11 kg |
| 1 yr | 263 keV | ≥ 2.4e-12 m | 1.3e14 kg |
| 100 yr | 2.6 keV | ≥ 2.4e-10 m (atomic scale) | 1.3e16 kg |

  The schedule sets the width: a faster schedule needs harder quanta and a narrower opening.
- **(C) The coupling view** (W3A). The corridor as a coupling term has no cross-section at all; size is replaced by
  count and time. One coupling run at the schedule's pace needs ħJ = ħIπ/(2T): 312 keV at 1 yr and 3.1 keV at 100 yr.
  That is the same scale as (B)'s quanta. Both are set by ħ × the bit rate.

Across all three, **the information corridor is between about 1e-21 m and 1e-10 m wide, not 1 m.** As a geometric
throat that lowers the throat mass by 1e9 to 1e21 relative to 1 m, since throat mass is linear in r. The board's other
limits on small throats stand as graded: DOCKET 66's held throats, DOCKET 67's quantum inequalities, and the Ford-Roman
crossover at 0.307933 and 5.625229 l_P, carried both ways on M's "Carry both".
