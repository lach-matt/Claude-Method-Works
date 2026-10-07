# The spectra index against the background radiation (M-RULINGS item 142; READ and computed; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)". The first draft carried three physics over-claims and a
defect test that compared the channel equation with itself; all are corrected, and a comb search is added (History).

## What you said

- **Item 142:** *"I have an idea for bulk ... We use the spectra index against our universe's own background radiation
  and see if the lowdin solution points is at a radiation signature that suggests an element not currently witnessed
  in our universe"*.
- **Carried:** M-CMB-ELEMENT-SEARCH, as evidence for item 138's H-ELEMENTS-PER-UNIVERSE.
- **The Löwdin solution** is the corpus's Chapter 35 (`recovered/BODY2-CHAPTER-35-THE-LOWDIN-SOLUTION.md`).
  - It derives the periodic order over Z = 2–108, *"every element with a measured ground configuration"*.
  - Beyond that, *"twelve rows, Z = 109–120"*, published as *"unwitnessed"*.
  - And *"no g block below Z = 121"*.
- **Your own line falls at 118.** Item 138: *"We have 118 current elements that are observable to our universe so
  far"*. So in your count, "an element not currently witnessed in our universe" is **Z = 119 and beyond**. The index
  draws the same line:
  - *"no long-lived isotope"* for Z = 104–118;
  - *"no nuclide synthesised"* for Z = 119–120.
- **The spectra index** is `COORDINATES-2_13.csv`. It holds one quantum defect δ per element, charge, ℓ and
  multiplicity, for Z = 1–120.
  - Most values are computed by the channel equation, whose rms against the 358 measured channels is 0.1809
    (docs/POPULATE.md).
- **The instrument:** `cmbindex.py`. Selftest 13/13; it takes about three minutes.
  - **Controls:** three (B1, B2, B4), and a null test of 400 sign-flipped copies (B2).
  - **Marked STRUCTURAL:** two.
  - **READ from the index itself:** one.

## What passes

### 1. The index reaches every Löwdin point, and it can write a search template for any of them

- **Every row Z = 109–120 carries computed defects** for the neutral atom's s, p and d channels.
- **Between two levels of one series the series limit cancels** (STRUCTURAL). So a template of an element's lines needs
  no limit, and the index's rule that the limit is never computed is kept.

### 2. The board ran the search you asked for, on the measured spectrum (B2)

- **The data:** FIRAS's 43 monopole residuals about the blackbody (Fixsen et al. 1996, Table 4, READ; all 43 rows
  checked).
- **The search:** a matched filter for a whole series of lines n → n−1, at any redshift from 0 to 3000.
  - It was run for a hydrogen-like series (δ = 0), which is what the index writes for Z = 119 and 120.
  - And for each of Z = 109–118's s, p and d defects: 31 series in all.
- **The result: no series stands out anywhere.**
  - The largest significance among all 31 is 3.0σ.
  - For the hydrogen-like series it is 2.8σ. Against 400 sign-flipped copies of the same residuals that is ordinary:
    p = 0.27, where the 95th percentile of the copies is 3.1σ.
  - The 2σ limit on a series' channel-averaged amplitude is about 17–18 kJy/sr. At the peak's 384 MJy/sr, that is
    about 45 ppm.
- **Control:** a series injected at 5σ at z = 1089 reads 4.5σ at that redshift.
  - The scan's largest value then lands at z = 11.1. With 43 channels each 13.6 GHz wide, a series' redshift is not
    unique (aliasing).

### 3. The background radiation read channel by channel (B1)

- **Every residual lies within 2.52σ.** The paper's own figure, with correlations and three fitted parameters, is
  χ²/dof = 46/40.
- **What that excludes, in Fixsen et al.'s terms** (p.23): a channel-averaged excess above about 50 ppm of the peak, in
  13.6 GHz channels of the sky-averaged spectrum, after their Galactic template is fitted.
- **It does not exclude a narrow line.** A channel dilutes a line by its width over 13.6 GHz. One FIRAS channel spans
  about 6,400 km/s at the top of the band, 25,000 at the peak and 60,000 at the bottom.

## The answer to your question

- **No Löwdin point sits at a radiation signature that FIRAS can see.**
  - No spectral line has been detected in the background radiation's sky-averaged spectrum.
  - The board's search for a whole series, at any redshift, for every Löwdin row finds nothing beyond chance.
- **This is a statement about the spectrum's lines, not about elements in general.**
  - The background radiation does carry our hydrogen and helium in other ways: its last scattering is hydrogen
    recombination, and its anisotropies measure primordial helium. That is standard knowledge, not READ here.
  - The recombination lines themselves are computed from hydrogen and helium (Sunyaev–Chluba 2009, pp.13–18, READ).
    They are not yet detected: they *"may become observable in the near future"* (abstract).
- **Where an early-universe atom's lines land** (B3).
  - Light from recombination arrives *"~10³ times redshifted"* (Sunyaev–Chluba p.13).
  - From z = 1089 only an atom's innermost series lines fall in FIRAS's band, n* = 3–4, Balmer- and Paschen-like.
  - Its outermost lines, n* = 23–46, fall there only for a source at rest.
- **Our own background radiation could not carry Z ≥ 109 in its lines.** It was released from gas before stars,
  hydrogen and helium with traces of lithium. Every nucleus at Z ≥ 104 has, in the index's words, no long-lived
  isotope, and Z = 119–120 *"no nuclide synthesised"*.

## Can the index name an unwitnessed element by its lines?

- **Against measured series, yes in one direction (B4).**
  - Only 20 neutral series have s, p and d all measured (or exact, for hydrogen).
  - None matches any of Z = 109–118 within the channel equation's rms.
- **Your target rows match hydrogen and helium.** Z = 119 and 120 read δ = 0.0 in every neutral channel (B = 0). So
  the index's template for your "element not currently witnessed" is **hydrogen-like**, and it matches hydrogen
  (exact) and helium (measured).
  - That is the sharpest finding here. In the index, your target would be indistinguishable from our two lightest
    elements.
  - Recorded, not repaired.
- **Against the index's own computed rows, the test cannot decide.**
  - Z = 109–118 have 6 to 15 computed look-alikes.
  - Our own elements, each tested against the others, have a median of 14 (range 1 to 27).
  - The Löwdin rows are no less distinguishable than ours. A uniform scatter would give 5.1.
- **A candidate, from the equation's own periodicity, not a measurement:**
  - the nearest computed rows of Z = 111, 112 and 114 are their homologues: gold, mercury, lead;
  - Z = 115–118 sit one step before theirs;
  - Z = 109 and 110 sit nearest Hs (108).
- **Not by mass** (B5).
  - A line sits c·mₑ/M below the infinite-mass line: hydrogen 163 km/s, lead 0.79, any nucleus of 270–300 u 0.55–0.61.
  - **But that is a uniform scaling of the whole series, so it cannot be told from a redshift** (STRUCTURAL).
  - And a 300 u atom's thermal width at 3000 K, 0.29 km/s, exceeds its gap to lead.

## The walls, as questions

**A. What carries an element's signature between universes?**
- **In the brane models the board has READ, only gravity crosses.** Youm, in UMBILIC.md: *"gravitons are assumed to
  propagate freely in the bulk, whereas all the matter fields are assumed to be confined on the brane"*. That is an
  assumption of those models, not a theorem.
- **Your item 90 already names a third option:** *"not by light. If not gravity, something else not yet identified or
  considered"* (H-UNIDENTIFIED-CARRIER). And item 140 carries universal entanglement.
- **If the carrier is not light, a search of the background radiation's light cannot find it.** Which carrier should
  the search look in?

**B. What, in another universe's elements, would differ from ours?**
- Item 138: *"118 completely different ones in another universe that measure exactly as are ours do. The difference is
  the relative laws of physics to that universe"*.
- **If they measure exactly as ours, their lines fall where ours do,** and no spectrum could tell them apart.
- **The Löwdin walk's one entered constant is c = 137.035999,** that is 1/α in atomic units. At c → ∞ the walk
  *"misplaces eleven elements"*. So different laws, a different constant, would give a different table.
- **But a change of the overall scale of the lines is again degenerate with redshift.** Only shifts that differ from
  line to line, such as relativistic ones, would tell universes apart.
- Is that the difference you mean? The board cannot rerun the walk at another constant: its code is not held (LW1
  README: *"PENDING BANK"*).

## Named hypotheses

- **Yours:**
  - M-CMB-ELEMENT-SEARCH (142);
  - H-MULTIVERSAL-BULK and H-ELEMENTS-PER-UNIVERSE (138);
  - H-UNIDENTIFIED-CARRIER (90);
  - H-ENTANGLED-PIN (140).
- **The board's:**
  - H-NEUTRAL-RYDBERG (the signature sought is a neutral atom's series);
  - H-TOPHAT-CHANNEL and H-EQUAL-COMB (the comb search's line model);
  - H-INDEX-PRECISION (the channel equation's rms as the index's precision).

## OPEN

1. **Your answers to walls A and B.**
2. A higher-resolution spectrum than FIRAS's, for narrow lines.
3. The recombination lines' own measurement, at nanokelvin level, which would test our hydrogen and helium first.

## History (verifier, 2026-10-07)

Twenty findings, all applied:

1. **Rest frame and observed frame were conflated.** The "exactly where an atom's outer lines fall" pass is withdrawn.
   From z ~ 1100 only n* = 3–4 reach the band.
2. **"No line at 50 ppm" overstated FIRAS** for narrow lines. Now stated in Fixsen et al.'s own terms, with the channel
   widths.
3. **"No element signature at all" was false.** It is now "no spectral line detected", with hydrogen recombination and
   helium named.
4. **Most of B4's "witnessed" comparators were computed.** Measured series are now separated: Z = 109–118 match none.
5. **Only the last multiplicity was kept.** All are kept now; Z = 119–120 match hydrogen and helium.
6. **The B4 control was weak and misreported.** It is replaced by our own elements tested against each other.
7. **The B1 control** is marked STRUCTURAL.
8. **Your own line at 118** makes Z ≥ 119 the target. The index's hydrogen-like template for those rows is now the
   lead finding.
9. **Wall A stated brane confinement as fact** and dropped your item 90. It is now conditioned and cites item 90.
10. **Mass is degenerate with redshift**, and thermal width is now included.
11. **"No nuclide at all"** is now "no nuclide synthesised". The isotope flag also covers Z = 104–108, so it is not
    distinctive. Lithium is added.
12. **A comb search was the better test.** It is now B2, with nulls and an injected control.
13. **The paper's χ² 46/40** is cited.
14. **The Sunyaev–Chluba amplitude** is no longer quoted from a figure the board could not read.
15. **n* is distinguished from n.**
16. **Channel widths** are given across the band.
17. **Wall B:** c is 1/α in atomic units. A uniform rescaling is degenerate with redshift.
18. **The item 138 quote** is restored verbatim.
19. **B2 (the Wien peak)** is a computed value. It is no longer marked STRUCTURAL.
20. **The homologue pattern** is recorded as a candidate, scoped to the equation's own periodicity. The board's run
    found Z = 109 and 110 nearest Hs, not Ir and Pt.
