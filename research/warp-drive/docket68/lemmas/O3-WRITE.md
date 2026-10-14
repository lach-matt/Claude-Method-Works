# Lemma O3 under item 158: the write's least time, and what it does to the hold (computed, READ and deduced; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated …)". The instrument is `o3_write.py`, selftest 12/12.

The first draft concluded that the static bulk gives way and that your question 158 (3) was decided. Its verifier
showed the step needed a reading the draft never named. The draft also set the threshold at the edge of the verified
region rather than at the singular surface, and led with a particle count the gas's own temperature rules out. All of
this is corrected below (History).

## What you said

- **Item 158 (2):** *"Exactly as long as the write needs  I should think"*. The hold is the write.
- **Item 158 (1), (3), (4):** *"This is for the math to decide, not myself"*; *"This question needs the math worked to
  answer it."*; *"This too is a question for the math."*
- **Item 115 (c):** *"The README itself"*. The opening's inflow is the README.
- **Item 157:** *"we already have at least half the model, our current universe."*
- **Item 106:** *"horizon position 1 only as the corridor opens"*. This is the first of the three holds.

## O3's question, as it now stands

- **The question.** O3 asks whether the corridor stays regular for as long as it must.
- **Two numbers.** That splits into how long it must (the write, by your 158 (2)) and how long it can (the bulk).
- **What this pass computes.** The first number, as a floor.

## The rate bounds do not decide it (W2, computed from READ)

- **The source.** Bekenstein and Schiffer's 1990 review, quant-ph/0311050, prints the information-rate bounds.
- **Why they don't decide it.** Each rate is linear in E, and E² grows like N. So each bound turns into a fixed number
  of clocks, whatever N is:

  | bound | least time for N bits, in clocks |
  |---|---|
  | eq. (86), p.20, bulk transport | 2 |
  | eq. (97), p.22, one channel, mean energy, self-heralding | 79.5 |
  | eq. (112), p.24, one channel, energy ceiling | 8π²/ln2 = 113.9 |
  | eq. (115), p.26, N_ch ≫ 1 channels | 113.9 / log₂(N_ch/ln2) |
  | quant-ph/0311049 eq. (26), already READ | 1/(2ξ) |

## W1 (STRUCTURAL)

- **The identity.** G1's E is the black-hole energy of N bits: 't Hooft's eq. (3), p.4, gives n = N, and Bekenstein's
  eq. (85) is saturated at R = 2m.
- **Why it is not a finding.** It holds by G1's own construction (H1, G3).
- **A caveat on the source.** 't Hooft's eq. (1) carries a "+ C", which his eq. (3) drops.

## W3. The gas bound (computed from READ, under named mappings)

**The steps.**
- **When the write ends.** The write is done when the README has crossed onto the throat at r = 2m
  (H-WRITE-IS-ARRIVAL).
- **Where it starts.** Nothing moves faster than light. So when the write began, all of the README lay inside the ball
  of radius (2 + T)m:
  - T is measured in advanced time (H-HOLD-FRAME);
  - the ball is in flat space (H-FLAT-START, the board's gloss on your 157, which says only "our current universe");
  - it carries only the README's energy E (H-README-ALONE).
- **How much it can hold.** Until it collapses, its number of states is at most a free gas's at that E and V
  (H-FREE-GAS). This is 't Hooft's *"The most probable state would be a gas at some temperature"*, eqs. (4)–(5), p.5.
- **N bits need e^S ≥ 2^N** (H-BITS-ARE-STATES, the board's use of 't Hooft's eq. (2)). Exactly, in the
  thermodynamic limit and without self-gravity:

  **T ≥ (3645 ln2 · N / (8Z))^(1/3) − 2 clocks.**

**Z is not free.**
- **The gas's own temperature.** At the bound it is 4E/(3S) = 1/(3πm), which is 8/3 of the README hole's Hawking
  temperature. At the example README that is 1.1 × 10¹¹ GeV.
- **What that fixes.** Every Standard Model particle is lighter than that. So Z ≥ 108.75: the Standard Model's 106.75
  and the graviton's 2.
- **Z = 2 is an illustration only.**

**At the example README** (N = 2,742,570,311,524,972):

| variant | least write, clocks | × the static window |
|---|---|---|
| Z = 108.75 | 2.0 × 10⁵ | 1.8 × 10⁴ |
| Z = 2 (illustration) | 7.6 × 10⁵ | 6.7 × 10⁴ |
| through the extra dimension, d = 4, Z = 2 (H-NO-SHORTCUT) | 4.7 × 10⁴ | 4.2 × 10³ |
| dropping H-README-ALONE: 't Hooft eq. (8), energy up to collapse, scales as N^(1/6) | 630 | 56 |
| prior entanglement (superdense coding, items 111, 137 (1)): 2^(−4/3) on 2 + T, Z = 2 | 3.0 × 10⁵ | 2.7 × 10⁴ |

- **Self-gravity at the start:** 2m/R ≈ 10⁻⁵.
- **Teleportation does not get round it.** The classical bits still have to arrive.

## W4. What it does to the hold (deduced; the choice of reading is the board's)

By your 158 (2) the hold is the write. Where the write sits has two readings.

**Reading (i), H-WRITE-IN-STATIC-HOLD.** The write happens inside the static eq. (17) hold of `b4_static.py`.
- **What that bulk carries.** It is verified (heuristically, by Padé agreement) below 11.28 clocks. Above that it is
  undecided. K ≥ 100 from 14.9 clocks, and it reaches the singular surface by about 18 clocks (B4.md, the verifier's
  figure).
- **What the write does to it.** The write passes those three edges at N ≈ 7.41 Z, 15.2 Z and 25.3 Z bits: 806, 1,657
  and 2,755 bits at Z = 108.75.
  - Between the first and the last, the static hold is **not certified**.
  - Above the last it is **refuted**.
- **At the example README** the static window would need more than 3.7 × 10¹⁴ light particle states.
- **The members a refutation on (i) rests on:**
  - your 115 (c), 157 and 158 (2);
  - the board's H-WRITE-IN-STATIC-HOLD, H-WRITE-IS-ARRIVAL, H-FREE-GAS, H-BITS-ARE-STATES, H-SPECIES-FINITE,
    H-FLAT-START, H-README-ALONE (or eq. (8) in its place), H-HOLD-FRAME, H-PULL-IS-COST and
    H-EXACT-ENERGY-AT-BOUND (G1);
  - the static bulk: eq. (17) held, the flat limit, the locally analytic class and Padé continuation.

**Reading (ii): the write is the opening.**
- **Why it reads this way.** Under your 115 (c) and H-PULL-IS-COST, the corridor of mass m does not exist until the
  README has arrived. So the write is item 106's first hold, *"only as the corridor opens"*.
- **How the board models that hold.** As ingoing Vaidya (`opening.py`, R-VAIDYA-HOLDS), which is non-static by
  construction.
- **What the bound becomes.** A floor on the opening: 2.0 × 10⁵ clocks at the example README. That supersedes
  `opening.py` O5's 4-clock Dyson floor by 5 × 10⁴.
- **The static window is untouched.**

**On either reading:**
- The bulk is not still through the write. That is the math's answer to 158 (3), on both readings.
- O3 waits on B4d.
- H-HOLD-IN-WINDOW is refuted only on reading (i).

## W5. Linear survival over the needed hold (computed; reading (i) only)

- **The factors.** `o3_hold.py`'s O3c factors over a hold of T clocks are T/4 (S4) and (1 + T/8)² (S5b). At the example
  README they are 5.0 × 10⁴ and 6.2 × 10⁸.
- **Where they apply.** They describe perturbations of the static corridor, so they apply on reading (i) only.
- **What they show.** Survival is not certified there.

## In seconds

- **The write is short in seconds:** 1.3 × 10⁻³¹ s at the example README. That agrees with your item 86 answer 5,
  *"incredibly short, maybe even immeasurable but not zero"*.
- **But long in clocks:** 1.8 × 10⁴ of the corridor's clocks, against the 11.3 the static bulk is verified for.

## What this decides, and what it does not

- **158 (3), the bulk's stillness: decided.** The bulk is not still through the write, on either reading.
- **158 (1), collective or bit by bit: not decided.** The bound holds whatever the mode of writing.
- **158 (4), the energy's place: not decided.** d = 4 changes the power, not the verdict; where the energy goes is B4d's.
- **Which reading holds: not decided.** Reading (ii) follows from your 115 (c) with H-PULL-IS-COST. Reading (i) is what
  O3 assumed until now.
- **O3 becomes OPEN, waiting on B4d.** Formation and Address already were.
- **What else this touches:**
  - B4b and B4c's far-boundary reading (ℓ > 2R_reach ≈ 23m) were calibrated to the 11.3-clock reach. With the write's
    floor the reach to be covered is ~10⁵ clocks, so both are re-read with B4d.
  - B6′ is still nature's.

## Named hypotheses

- **Yours:** H-INFLOW-IS-README (115 (c)), H-HALF-IS-OURS (157), H-HOLD-AT-BOUND (158 (2)).
- **The board's:**
  - H-WRITE-IN-STATIC-HOLD (reading (i));
  - H-WRITE-IS-ARRIVAL;
  - H-FREE-GAS;
  - H-BITS-ARE-STATES;
  - H-SPECIES-FINITE: Z below ~10¹⁴;
  - H-FLAT-START;
  - H-README-ALONE;
  - H-HOLD-FRAME;
  - H-NO-SHORTCUT (d = 4);
  - H-PULL-IS-COST: m = GE/c⁴, the clock;
  - H-EXACT-ENERGY-AT-BOUND (G1);
  - R-VAIDYA-HOLDS (reading (ii)).

## History (verifier, 2026-10-07)

**The verifier ran the selftest (8/8) and READ both sources at the quoted pages.** Every equation, page and phrase was
right. Its independent checks agreed with every computed figure. The bound stood in every variant it tried. Its
findings, all applied:

**MUST-FIX**
1. **"The static bulk gives way" and "158 (3) decided" needed an unnamed member, and the reading chosen was not
   forced.** H-WRITE-IN-STATIC-HOLD is now named. Reading (ii), the write as the opening, is stated beside it and is
   equally live. The bound now also stands as a floor on the opening, superseding O5. 158 (3) is decided on both
   readings; H-HOLD-IN-WINDOW is refuted only on (i).
2. **The conjunction left out members.** Now added: Padé continuation, H-PULL-IS-COST, G1, H-BITS-ARE-STATES,
   H-FLAT-START, H-README-ALONE, H-HOLD-FRAME and H-NO-SHORTCUT.
3. **11.3 clocks is the end of the verified region, not the singular surface.** There are now three thresholds:
   7.41 Z (not certified above), 15.2 Z (K ≥ 100) and 25.3 Z (refuted above).

**SHOULD-FIX**
4. **Z = 2 is inconsistent with 't Hooft's own definition of Z.** The gas temperature is now computed (1.1 × 10¹¹ GeV),
   and the headline uses Z = 108.75.
5. **H-README-ALONE was unnamed.** It is now named. The eq.-(8) variant, which needs fewer hypotheses, is computed:
   630 clocks.
6. **The entanglement readings were not considered.** Superdense coding is now computed. The verifier gave its factor
   as 2^(−1/3) and 6.0 × 10⁵; the instrument found 2^(−4/3) and 3.0 × 10⁵, because the radius goes as bits^(4/3)/N.
   The verifier's figure was wrong and this one is checked.
7. **W1 is STRUCTURAL,** and the Bekenstein control is W1 restated. Both are now labelled STRUCTURAL.
8. **Wrong figures.** "792" is now 806 at the new Z. The uncomputed "~10⁵ times" is now computed ratios.
9. **The N = 10 control sits in the Planck regime.** It is now marked formal.
10. **Flatness is the board's gloss on 157.** It is now H-FLAT-START.
11. **"One question" overstated what remains.** The effect on B4b and B4c is now recorded, and B6′ is noted.
12. **(NOTE) Labels.** W2 now says self-heralding and simple system. W5 applies on reading (i) only. Selftest
    tolerances are tightened. W4 is labelled "deduced; the choice is the board's". The d = 4 Bose constant is now a
    control.

**Not applied.** The verifier raised Dvali's species bound, which would squeeze the large-Z escape to an O(1) band. It
is not READ, so it is not used.
