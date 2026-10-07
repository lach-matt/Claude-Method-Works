# The spectra index against the background radiation (M-RULINGS item 142; READ and computed; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## What you said

- **Item 142:** *"I have an idea for bulk ... We use the spectra index against our universe's own background radiation
  and see if the lowdin solution points is at a radiation signature that suggests an element not currently witnessed
  in our universe"*.
- **Carried:** M-CMB-ELEMENT-SEARCH, as evidence for item 138's H-ELEMENTS-PER-UNIVERSE.
- **The Löwdin solution** is the corpus's Chapter 35 (`recovered/BODY2-CHAPTER-35-THE-LOWDIN-SOLUTION.md`).
  - It derives the periodic order from the many-electron equation, 107/107 over Z = 2–108.
  - Beyond that, *"twelve rows, Z = 109–120"*, published as *"unwitnessed"*.
  - And *"no g block below Z = 121"*.
- **The spectra index** is `COORDINATES-2_13.csv`. It holds one quantum defect δ per element, charge, ℓ and
  multiplicity, for Z = 1–120.
  - Most values are computed by the channel equation, whose rms against the 358 measured channels is 0.1809
    (docs/POPULATE.md).
- **The instrument:** `cmbindex.py`. Selftest 11/11.
  - **Controls:** two.
  - **Marked STRUCTURAL:** three.
  - **READ from the index itself:** one.

## What passes

### 1. The index reaches every Löwdin point (B4, B6)

- **All twelve unwitnessed rows, Z = 109–120, carry computed defects** for the neutral atom's s, p and d channels.
- **The index already marks each of them**, at every neutral row: *"no long-lived isotope"* (Z = 109–118) or *"no
  nuclide synthesised"* (Z = 119–120).

### 2. The background radiation sits exactly where an atom's outermost lines fall (B2, B3)

- **The background radiation peaks at 160.2 GHz** (Wien's law at T₀ = 2.72548 K, Fixsen 2009, READ).
- **Any neutral atom's Rydberg transitions n → n−1 fall in FIRAS's band for n = 23 to 46.**
- **Those lines need no series limit:** it cancels between two levels of one series. So the index can write a search
  template for any element, witnessed or not, without breaking its own rule that the limit is never computed.
  - That the limit cancels is STRUCTURAL.

### 3. The measured background radiation, read point by point (B1)

- **FIRAS measured the spectrum from 2 to 21 cm⁻¹** (Fixsen et al. 1996, READ). In their words, *"the RMS deviations
  are less than 50 parts per million of the peak"*.
- **The board read their 43 monopole residuals (Table 4) against the blackbody.**
  - Every one lies within 2.52σ.
  - Summed, (r/σ)² is 45.0 for 43 points (diagonal; their correlations ignored).
  - **There is no line.**
- **Control:** a line injected at 5σ into one channel is flagged.

## The answer to your question

- **No Löwdin point sits at a radiation signature in our background radiation, because the background radiation, as
  measured, carries no element signature at all.**
  - That includes our own hydrogen and helium.
  - The lines from our universe's own recombination are computed from hydrogen and helium alone (Sunyaev–Chluba 2009,
    pp.13–18, READ), at 10⁻¹⁰ to 10⁻⁷ of the blackbody (their Fig. 8).
  - They are not yet detected: they *"may become observable in the near future"* (abstract).
- **And our own background radiation could not carry these elements in any case.**
  - It was released from the gas before stars, made of hydrogen and helium.
  - Every nucleus at Z ≥ 109 has, in the index's own words, no long-lived isotope or no nuclide at all.

## Even with a line, could the index name an unwitnessed element?

- **Not by its defects (B4).**
  - In this band a neutral atom's series carries δ mod 1 for each channel.
  - Within the channel equation's own rms (0.1809), each of Z = 109–118 matches between six and fifteen witnessed
    elements in all three channels at once.
  - **Control:** at a tolerance of 0.001 the same test returns none. So the test can tell elements apart, and at the
    index's precision it does not.
- **Z = 119 and 120 read δ = 0.0 in every neutral channel (B = 0).** That makes them hydrogen-like in the index, so the
  one witnessed element they match is hydrogen. Recorded, not repaired.
- **Not by mass (B5).**
  - A Rydberg line sits below the infinite-mass line by c·mₑ/M:
    - hydrogen 163 km/s;
    - lead 0.79 km/s;
    - uranium 0.69 km/s;
    - any nucleus of 270–300 u, 0.55–0.61 km/s.
  - **A superheavy element is within 0.3 km/s of lead.** One FIRAS channel spans about 25,000 km/s.

## The walls, as questions

**A. Can light cross between universes, or only gravity?**
- On a plane in the bulk, matter and light stay on their own plane, and only gravity travels through the bulk. Youm,
  READ in UMBILIC.md: *"gravitons are assumed to propagate freely in the bulk, whereas all the matter fields are
  assumed to be confined on the brane"*.
- So another universe's element could not put light into our background radiation.
- If your bulk carries only gravity between universes, the signature would have to be gravitational, not a line in the
  radiation. Does it carry light?

**B. If another universe's elements "measure exactly as ours do", what would differ in their light?**
- Item 138: *"118 completely different ones that measure exactly as are ours do. The difference is the relative laws
  of physics to that universe"*.
- If they measure exactly as ours, their lines fall where ours do, and no spectrum could tell them apart.
- The Löwdin walk has one entered constant, c = 137.035999 (the fine-structure constant), and it is visibly
  relativistic. At c → ∞ the walk *"misplaces eleven elements"*. So a universe with different laws, a different
  constant, would have a different table and different lines.
- Is that the difference you mean? The board cannot rerun the walk at another constant: its code is not held (LW1
  README: *"PENDING BANK"*).

## What this does and does not show

- **It shows:**
  - the index reaches the Löwdin points;
  - the background radiation's band is exactly where an atom's outer lines fall, and those lines need no series limit;
  - the measured background radiation has no line, at 50 ppm;
  - at its own precision, the index cannot single out an unwitnessed element by its lines in that band.
- **It does not show:**
  - anything about a gravitational signature (wall A);
  - what another universe's spectra would be (wall B);
  - the recombination lines' future measurement, at nanokelvin level, which would test our own hydrogen and helium
    first.

## Named hypotheses

- **Yours:**
  - M-CMB-ELEMENT-SEARCH (142);
  - H-MULTIVERSAL-BULK and H-ELEMENTS-PER-UNIVERSE (138).
- **The board's:**
  - H-NEUTRAL-RYDBERG (the signature sought is a neutral atom's Rydberg series in the FIRAS band);
  - H-INDEX-PRECISION (the channel equation's rms as the index's precision for δ);
  - H-Z2 and brane confinement (UMBILIC.md, READ).

## OPEN

1. **Your answers to walls A and B.**
2. If light does cross: which band, and at which redshift, another universe's lines would arrive in.
3. If only gravity crosses: what gravitational signature an element of another universe would leave.
