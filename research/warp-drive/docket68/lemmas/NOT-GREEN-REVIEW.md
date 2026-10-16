# Every row not green, reviewed and settled (item 439)

M, 439: "Review all item not green in the warp theorem map, and correct any discrepancies. I see two open lemmas,
ARRIVAL  and ENCODE, as well as 5 readings, that need to be addressed, proved, and settled."

Before this item the register (`warptheorem.py` LEMMAS_NOW, 80 rows) held nine rows that were not green:
- two open lemmas, ARRIVAL and ENCODE;
- five readings: ARRIVALs, B3s and B4ds at the small end, B3 and B4d at the large end;
- two rows you deferred, SOURCEs and SOURCE.

The work is in `settle_arrival.py` (A0–A7, selftest 6/6, mutants 5/5) and `encode_labels.py` (C0–C7, selftest 6/6,
mutants 4/4). Labels: computed, deduced, READ, estimate, M's.

## 1. What settles the six arrival rows

The five readings and ARRIVAL rested on one board model: the README coming in as radial null dust, which SOURCE was to
replace. Item 438 turned that model into a requirement of the math:
- your 386 makes what crosses energy alone, so it moves on the light cone (324);
- your 162 with T0 admits a null inflow only as a step.

Item 439 shows that the required delivery exists, and records what it asks of SOURCE.
- **A1 (computed, z3).** A face of fixed size takes no energy and no shear after the opening (Raychaudhuri with
  theta = 0). So the delivery must leave behind exactly the static hole.
- **A2 (computed, exact).** At the small end the step exists exactly at the small end's order: 5D Vaidya, whose one
  Einstein component is 3 mu'/(2 r^3). It is round in the bulk, with Tangherlini outside.
- **A3 (computed, exact).** Light sent from our plane cannot make that round shell. It reaches the face's 3-sphere
  spread over one face clock and pressed onto the plane. So the README's last leg comes in through the bulk (180).
- **A4 (computed, exact; estimate for the cap).** At the large end the warped Vaidya metric solves the five-dimensional
  equations exactly.
  - It is a null shell in the bulk, with our plane carrying its tension alone and reading the four-dimensional step.
  - It is exact where the large hole is a black string. The cap, where the horizon closes in the bulk, carries
    (ell/r0)^2 of the area: the large end's own order.
- **A5 (READ).** Wang and Choptuik's five-dimensional collapse of matter on a brane forms the static large hole. This
  answers your 232 request to compute the formation in the bulk. Their delivery leaves the face to settle, which A1
  refuses.
- **A6 (deduced).** So ARRIVALs, B3s and B4ds are derived. ARRIVAL, B3 and B4d are derived at the large end's order,
  the order every large-end row carries.
- **A7 (deduced).** Whether SOURCE can supply the delivery is SOURCE's question (your 344–345). No row rests on SOURCE.

## 2. What settles ENCODE

The encoding of a geometric object is the labels of its last state, as your 438 sets it: each atom's element, which
atom bonds to which, or a crystal's lattice, basis, cell counts and defects.
- It is gamma-coded and canonical (the same code whatever order the atoms are listed in).
- It decodes exactly.
- It holds integers only, so no constant of position 2 changes it.
- 1 cm³ of perfect copper is 174 bits, 2.0 J at the small end.
- A real piece at 99.99 % purity is about 1.3e21 bits, 1 % of its own rest energy.

The device that performs the read is SOURCE's, as you placed it at 399. Atomic electron tomography is the nearest
demonstration, read at source: 23,804 atoms, positions to 22 pm, species 99 % correct.

## 3. Discrepancies found, and how each was corrected

Each correction is kept beside the text, never over it.

| where | what stood | correction |
|---|---|---|
| register SOURCEs, SOURCE (names) | "written there as a gas of the plane's fields, not null dust" | "gas" was withdrawn at 386; re-worded as energy alone, delivered as the theorem requires, the old wording kept in a note |
| register SOURCE (where) | "the large end's ARRIVAL and WRITE are open" | WRITE has been derived since 362, ARRIVAL since 439; noted |
| register WRITEs, WRITE (names) | ">= 66,980 clocks of r_h/c", ">= 199,702.19 clocks of m/c" as the write's length | S2's free-field floors stood on a reading that gave way at 432 (1); the least write by the math is 9.49 and 28.48 clocks (437 (2)); renamed, the old names kept in notes; the holds proved cover either |
| register ARRIVALs (name, where) | "compact"; "5.39 clocks, 8.0e-5 of the write"; V5's floor | the step, the compact range at width zero; "all at once"; the old text kept |
| register B4ds (where) | the opening "on 340's compact reading, ... lambda <= 1/27" | the opening is the step, its onset hidden; noted |
| register ARRIVAL (where) | "formation in the bulk (179)" open; "a READING through SOURCE, put to M" | answered by A4 and A5 |
| map, Formation station | "On a reading" and "Open lemma"; the shared B4d entry "Open" while the register read "Reading" | both pass; the entries match the register |
| map, Address station | "On a reading" at the small end | passes |
| map, ARRIVAL row | "The compact width is withdrawn at your 426 ... 5.9 % of the face's life" | replaced by the settled text |
| map, B3s, B4ds and ARRIVALs rows | "re-read under the long write ... once the board has modelled it" | replaced by the settled text |
| map, SOURCEs and SOURCE rows | "Today ARRIVALs models it ..."; "ARRIVAL and WRITE are open" | what they must supply (SOURCE-REQUIRED 19–22) |
| map, WRITEs row | "at least 66,980 clocks" | the least time, 9.49 clocks |
| map, the Read station | RECON and ENCODE counted in the tally since 437 but drawn nowhere | both rows added |
| map, tally | 71 green, 5 readings, 2 open | 78 green, 2 deferred |
| WARPTHEOREM.md, table and count line | as above | brought to the register; the old count line kept in a note |
| `readings.py` Q29 | "the README's true form, a gas of our plane's fields" | an item-438/439 note beside it |
| `b4d_small.py` D10 and `b4d_large.py` K9 | checks expecting READING and OPEN | moved to DERIVED with notes; both selftests pass |

## 4. What stays as it is

- **SOURCEs and SOURCE stay deferred** (M-SOURCE-LAST). The completed rows now state what each must supply:
  SOURCE-REQUIRED requirements 19–22.
- **Your 109 and the event horizon.** In every collapse from a regular centre, the event horizon is born before the
  opening: 2 face clocks for a shell. The face of your 162 and 109 is the trapping horizon (b4d_large K12 (i)).
- **"Potential to be other states"** is read as costing no bit: a label carries every state its laws allow (C6 (c)).
  The board's reading was put to you at 438 and is restated there.
