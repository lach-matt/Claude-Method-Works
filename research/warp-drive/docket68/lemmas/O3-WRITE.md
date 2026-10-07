# Lemma O3 under item 158: the write's least time, and whether the static bulk can hold through it (computed and READ; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated …)". The instrument is `o3_write.py`.

## What you said

- **Item 158 (2):** *"Exactly as long as the write needs  I should think"*. The hold is the write.
- **Item 158 (1), (3), (4):** *"This is for the math to decide, not myself"*; *"This question needs the math worked to
  answer it."*; *"This too is a question for the math."*
- **Item 115 (c):** *"The README itself"*. The opening's inflow is the README.
- **Item 157:** *"we already have at least half the model, our current universe."* The write starts from our own
  universe, which is flat at the corridor's scale.

## What was looked for, and what was found instead

- **What was looked for.** The board went looking for an exact rate at which information can be moved. With one, the
  least write time would follow, and so would the hold.
- **The rates are READ.** Bekenstein and Schiffer's 1990 review (quant-ph/0311050) prints them:
  - eq. (86), p.20: bulk transport;
  - eq. (97), p.22: one channel, specified mean energy;
  - eq. (112), p.24: one channel, energy ceiling, heralded or not;
  - eq. (115), p.26: many parallel channels.
- **None of these rates decides it.** Each is linear in E, and E² grows like N. So each turns into a fixed number of
  clocks, whatever N is (W2):

  | bound | least time for N bits, in clocks |
  |---|---|
  | eq. (86), bulk transport | 2 |
  | eq. (97), one channel, mean energy | 79.5 |
  | eq. (112), one channel, energy ceiling | 8π²/ln2 = 113.9 |
  | eq. (115), N_ch channels | 113.9 / log₂(N_ch/ln2) |
  | quant-ph/0311049 eq. (26) (already READ) | 1/(2ξ) |

  A single one-dimensional channel already needs more than the static bulk's ~11.3 clocks.
- **What bites instead is the room the README needs before it arrives.** 't Hooft's essay (gr-qc/9310026, pp.4–5,
  eqs. (2)–(5)) gives it.

## W1. The README's energy is the black-hole energy of N bits (computed identity)

- 't Hooft's eq. (3), p.4, counts a black hole's Boolean degrees of freedom: n = 4πM²/ln2.
- With G1's E, n = N exactly. So the README's one exact energy is the mass of the black hole that holds exactly N
  bits.
- The register at r = 2m saturates Bekenstein's eq. (85) exactly: 2πE(2m)/(ħc ln2) = N.
- Control: doubling E gives 4N.

## W3. The gas bound (computed from READ)

- **When the write ends.** The write is done when the README has crossed onto the throat at r = 2m
  (H-WRITE-IS-ARRIVAL, the board's).
- **Where it starts.** Nothing moves faster than light. So when the write began, all of the README lay inside the ball
  of radius (2 + T)m, where T is the write's length in clocks. That ball sits in our flat universe (item 157).
- **How much it can carry.** Until it collapses, the README is matter. At fixed E and V, matter has at most as many
  states as a free gas (H-FREE-GAS). This is 't Hooft's *"The most probable state would be a gas at some temperature"*,
  with E = C₁ZVT⁴ and S = C₂ZVT³.
- **The constants.** They are the Bose integral's. At d = 3 they reduce to Stefan–Boltzmann, which is the control.
- **N bits need e^S ≥ 2^N** ('t Hooft eq. (2), p.4). So:

  **T ≥ (3645 ln2 · N / (8Z))^(1/3) − 2 clocks** (exact).

  Here Z counts the light particle states ('t Hooft: *"the number of different fundamental particle types with mass
  less than T"*).
- **At the example README** (N = 2,742,570,311,524,972):
  - 7.6 × 10⁵ clocks at Z = 2;
  - 2.0 × 10⁵ clocks at the Standard Model's Z = 106.75;
  - 4.7 × 10⁴ clocks through the extra dimension (d = 4, a generous 4-ball), where the power is 1/4 instead of 1/3.
- **Control.** Bekenstein's eq. (85) used in place of the gas gives T ≥ 0. So causality alone does not bite; the gas
  bound does.

## W4. The static bulk cannot hold through the write (computed)

- **The comparison.** By your 158 (2), the hold is the write, so the hold is at least T. The static bulk of
  `b4_static.py` is regular only for holds shorter than about 11.3 clocks.
- **Where it fails.** T exceeds 11.3 clocks for every README above N* = 8Z(v + 2)³/(3645 ln2):
  - about 7.41 Z bits in general;
  - 15 bits at Z = 2;
  - 792 bits at Z = 106.75;
  - about 17 bits at Z = 2 through the extra dimension.
- **At the example README,** the static window would need more than 3.7 × 10¹⁴ light particle states.
- **The control.** At N = 10 bits and Z = 2 the write does fit. The failure depends on N; it is not universal.
- **What is refuted is a conjunction.** It has three parts:
  - your 115 (c), 157 and 158 (2);
  - the board's H-WRITE-IS-ARRIVAL, H-FREE-GAS and H-SPECIES-FINITE;
  - the static bulk of `b4_static.py`: eq. (17) held, the flat limit, the board's locally analytic class.
- **The math's answer to 158 (3).** Your words stand, so the board's reading gives way, and that reading is the static
  bulk. The bulk is not still through the write: it evolves, which is B4d. H-HOLD-IN-WINDOW is refuted for every
  README above N*.

## W5. Linear survival is not certified over the needed hold (computed)

- **The factors.** `o3_hold.py`'s O3c factors over a hold of T clocks are T/4 (S4) and (1 + T/8)² (S5b).
- **At the example README** they are 1.9 × 10⁵ and 8.9 × 10⁹. Linear theory cannot carry the corridor through the
  write, so its survival is B4d's, nonlinear.

## In seconds

- **The needed write is still short.** It is T clocks times the clock: about 5 × 10⁻³¹ s at the example README.
- **This agrees with your item 86 answer 5:** *"incredibly short, maybe even immeasurable but not zero"*. What fails is
  not shortness. The write lasts ~10⁵ times longer than the static bulk can stay regular, measured in the corridor's
  own clocks.

## What this decides, and what it does not

- **158 (3), the bulk's stillness: decided.** The bulk is not still through the write (W4).
- **158 (1), collective or bit by bit: not decided.** The gas bound holds whatever the mode of writing, so it does not
  choose one. Both modes now need longer than the static bulk carries.
- **158 (4), the energy's place: not decided.** The extra dimension does not save the static bulk (d = 4 still needs
  4.7 × 10⁴ clocks), but where the energy goes is B4d's.
- **O3 becomes OPEN.** It now waits on B4d, as Formation and Address already did. The chain's remaining question is one
  question: the corridor's five-dimensional evolution through a write of ~(N/Z)^(1/3) clocks.

## Named hypotheses

- **Yours:** H-INFLOW-IS-README (115 (c)), H-HALF-IS-OURS (157), H-HOLD-AT-BOUND (158 (2)).
- **The board's:**
  - H-WRITE-IS-ARRIVAL: the write ends when the README is on the throat;
  - H-FREE-GAS: before collapse, at most the free gas's number of states;
  - H-SPECIES-FINITE: Z below ~10¹⁴;
  - H-PULL-IS-COST: m = GE/c⁴, the clock.
