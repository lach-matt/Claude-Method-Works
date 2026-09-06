
---

# VI · THE LÖWDIN SUPPLY

*The Löwdin solution is tested against measurement, and this is the measurement it is tested against. Registers 1524–1677 record the capture of these bodies one at a time, each verified before it was written and several corrected after; §* Why each was captured *does the same office for the coordinate groups. What follows is the empirical supply itself, set out so that a reader can see what was consulted, how much of it there is, and what each body can and cannot carry.*

## What this supply is, and what it is not

**Seven families, 1,510 rows, every one of them captured from a published compilation and verified before it was held.** *None of it is computed by this work. It is the outside world, brought in and checked: X-ray transition energies, ionisation energies along the charge ladder and across the neutral atoms, two level tables, nuclear radii and masses, quantum defects from an independent database, and a staged block of index cells.*

| family | rows | span | source compilation |
|---|---|---|---|
| **the X-ray lines** | 474 | Ne–Fm, six transitions | NIST SRD 128 v1.2 (Deslattes *et al.* 2003) |
| **the isoelectronic ladder** | 546 | Z = 1–18 and 19–36 | NIST ASD ver. 5.12 |
| **the neutral ionisation energies** | 108 | Z = 1–108 | NIST ASD ver. 5.12 |
| **the level tables** | 29 | Fe I, Kr I | NIST ASD |
| **the nuclear supply** | 37 | Th–Cf, the A = 9 chain | Angeli & Marinova 2013; AME2020 |
| **the quantum defects** | 68 | Li, O, Na, Mg, all stages | TOPbase, *via* de Kertanguy |
| **the staged cells** | 554 | 158 index cells | this work's own retrievals |
| | **1,816** | | |

**The row total and the family total differ, and the difference is the point.** *The staged cells are not an outside compilation — they are this work's retrievals staged in the index's own schema, and they are listed here because register 1649 named them as the source of a figure the compendium prints. The outside supply proper is 1,262 rows.*

**Two of the eighteen bodies the register names are not held here, and their absence is stated rather than papered over.** *`MEASUREMENTS.tsv` and the rows recovered at register 652 are stores this work built, not captures it took; register 1674 records that the first has no generator and survives only as data. Neither is an outside compilation, and neither is reproduced in this supply.*

## The X-ray transition energies

*Six transitions, captured one at a time between registers 1524 and 1555, and the family that cost the most to get right: register 1526 records four fabricated theory values in the first of them, copied from the experimental column where the source stood blank, and the correction is why every later capture was verified by destination address and body header before it was written.*

| transition | line | rows | first | last |
|---|---|---|---|---|
| K–L3 | Kα₁ | 98 | Ne | Fm |
| L3–M5 | Lα₁ | 78 | Ca | Fm |
| L3–M4 | Lα₂ | 78 | Ca | Fm |
| L3–M1 | Lℓ | 88 | Na | Fm |
| L1–N2 | Lγ₂ | 67 | Ga | Fm |
| L1–N3 | Lγ₃ | 65 | As | Fm |
| | | **474** | | |

**Each row carries the element, a mass number where the source gives one, a theoretical energy, a direct experimental energy, and an uncertainty on each.** *NIST's compact parenthetical form is preserved as it stands: 849.17(54) is 849.17 ± 0.54 eV. Two flags travel with the value — an asterisk where the source interpolated from neighbouring elements, and a hash where experiment and theory diverge far enough that the source itself doubts the measurement. A blend field says where Kα₁ and Kα₂ are unresolved at that element. Blank means blank; nothing is inferred into an empty field.*

**One row, as it stands:**

```
Kα₁   U   238   theory 98433.6(36)   experiment 98431.58(28)   ref 5d
```

**The K–L3 capture carries thirteen actinide isotope rows — uranium at two masses, plutonium at two, americium at two, curium at two, berkelium at two and californium at three — and those are the anchors register 1555 identified.** *Californium's third row has no direct experimental value at all; the field is empty in the source and empty here. The mass-number column is blank below bismuth, because the compilation populates it only for radionuclides.*

**The physical check the family supports, and it is the reason two of the six were taken.** *Lα₂ must lie below Lα₁ at every element, since M4 is the more tightly bound of the two levels; the pair was captured precisely so that the inequality could be tested rather than assumed. Lγ₃ − Lγ₂ is the 4p splitting, and register 1528 took both to see whether the post-krypton offset showed stable structure per region.*

## The isoelectronic ladder

*Two captures, taken through different endpoints on different days, and their overlap is what makes either trustworthy.*

**`LADDER-K-Kr` holds 495 rows: every ionisation stage of every element from potassium to krypton, Z = 19 to 36 — the whole 3d block and its shoulders, in electronvolts.** *The quality flag is the source's own: 96 measured, 287 estimated, 112 theoretical. That distribution is the ladder's real condition — beyond the first few stages of a mid-Z element, the published value is usually an estimate, and the compendium's high-charge cells inherit that.*

**`LADDER-H-Ar-I-III` holds 51 rows: hydrogen through argon at charges 0, +1 and +2, in wavenumbers, with the ground configuration, the ground level term, the isoelectronic sequence and an uncertainty on each.**

**One row, as it stands:**

```
H I   Z=1   charge 0   sequence H   ground 1s   2S<1/2>   109678.77174307 cm⁻¹ ± 0.00000010
```

**The two ladders and the neutral table agree where they overlap, and the agreement was tested rather than assumed.** *Register 1538 puts eighteen first ionisation energies from a supplied table against the K–Kr capture at a maximum discrepancy of 7.8 × 10⁻⁵ eV with nothing beyond 5 × 10⁻⁴; register 1539 finds the krypton limit agreeing to 4 × 10⁻⁹ eV. Three retrievals through three routes, converging — which is corroboration, since the routes are unalike.*

## The ionisation energies of the neutral atoms

**108 rows, Z = 1 to 108, first ionisation energy of the neutral atom with its uncertainty, and the source's own quality notation carried across intact: 98 measured, 7 estimated, 3 theoretical.** *Register 1593 cross-checked these against the K–Kr ladder's own charge-zero rows: eighteen values overlap and all eighteen agree exactly, in value and in flag. The square and round brackets the compilation prints are not decoration — they are the quality claim, and dropping them would have discarded the only statement of confidence the source makes.*

## The two level tables

**Fe I — 19 levels across five terms, all five multiplets inverted, as Hund's third rule requires of a 3d shell more than half filled.** *Every row passes the wavenumber-to-electronvolt conversion at better than 6 × 10⁻⁴ eV. The ionisation potential is excluded, and the a⁵P anomaly is flagged in the capture itself rather than in prose alone, so that the flag travels with the data.*

**Kr I — 10 levels, the 4p⁵(²P₃⁄₂)5p manifold complete at all six.** *All ten satisfy J₁ℓ pair coupling, K = J₁ ⊗ ℓ and J = K ± ½. **The table is one row short of the eleven its own header claims, and the missing row is named:** register 1541 settles 85846.709 cm⁻¹ as the J = 1 level and records the J = 0 metastable as absent from the source, with 86583.760 belonging elsewhere. The capture marks the disputed rows and leaves the choice unmade.*

## The nuclear supply

**23 measured actinide rows — thorium 5, uranium 5, plutonium 6, americium 2, curium 5 — each carrying a change in mean-square charge radius against a reference isotope, an absolute rms charge radius, and an uncertainty on both.** *From Angeli and Marinova's 2013 table of experimental ground-state charge radii. Four of the six anchors the argument needs are present and two are absent, which register 1557 predicted from the compilation's own scope before the table was in hand.*

**Berkelium and californium are computed, not measured, and the capture says so in its first line.** *Nine rows, five absolute radii and four differences, from a regression on eighteen pairs across five elements. **They are indicative only and carry their stated error.** The measurement cannot presently be made — register 1559 records that three of the four methods need tens of milligrams of material — so the values are labelled predicted in the file itself, where no later reading can mistake them for a capture.*

**The A = 9 isobar chain — five nuclides, ⁹He, ⁹Li, ⁹Be, ⁹B, ⁹C — mass excess and uncertainty from AME2020, with a stability note on each.** *Verified three ways before it was written, including reproduction of the known binding energy per nucleon from the mass excess. **Five nuclides of roughly three and a half thousand:** the capture is a probe of the chain, not a survey of the table, and register 1544 says so in the entry that records it.*

## The quantum defects of the light ladders

**68 cells: lithium 6, oxygen 16, sodium 22, magnesium 24 — each species across every one of its ionisation stages, with the defect given per ℓ.** *From TOPbase, the Opacity Project's database, as tabulated by de Kertanguy. The trail was followed there from Theodosiou, Inokuti and Manson's 1986 compilation, which this work could not obtain directly and which the paper cites as its own reference.*

**This is the charge-edge extension, and it is the only held source that supplies a complete ladder for a species.** *Register 1585 identifies it as the most valuable of the extensions available, for exactly that reason: the compendium's own measured cells cluster at low charge, and a complete ladder is what tests whether the defect's behaviour along the charge axis is what the channel equation says it is.*

## The staged cells

**554 rows over 158 distinct index cells, in the index's own eleven-column schema — the same columns §** The file *sets out, plus a tier.* **Graded A 218, B 157, C 179.** *Many rows to one cell, which is the whole point: register 1662 records that treating repeat measurements of one channel as duplicates inverted the direction of the error, since the second and third measurement of a cell are true measurements with nowhere to sit, not noise.*

**Thirty-nine series are staged as skipped, unbounded — no limit stands above them.** *A series with no limit above its top member has no defect to compute, and the staging records the fact rather than dropping the row.*

## How this supply is cited

**A body in this part is cited by its section name, as the coordinate index is cited by** COORD(Z, charge, ℓ, 2S+1). *The register's working entries name the capture files these bodies were held in; the volumes name the bodies. A reader who wants the sodium ladder is sent to §* The isoelectronic ladder*, not to a filename, and that is the whole of the difference.*

**Nothing in this part is recomputed at press.** *The counts are of captures taken and verified on the dates the register records, and they are stated as of capture. §* The table *and §* The file *are read from the coordinate companion at build and fail the press if they drift; this part is not, because the bodies it describes are compilations that do not change under this work's hand.*