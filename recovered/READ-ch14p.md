# READ-ch14p.md — Chapter 23, §23.12 to the end (main member L6549–L6622)

Chat 98. Unit: **§23.12 L6549 through §23.15, ending L6622 — 74 lines, five headings**, boundaries
re-scanned on `The_Method_1_6-2.md` before a line was read (§23.12 6549, §23.13 6569, §23.14 6582,
§23.14.1 6595, §23.15 6606; Chapter 24 opens 6623). This unit **closes Chapter 23**.

Instruments: `r2-ch14p` (computable, golden 15,920 B · `fee8fd64` · 167 lines) and `r2-ch14q`
(prose, golden 12,769 B · `88b2d69d` · 115 lines). Both import `heading_line`, `section_span`,
`has_token` and `enclosing` from `r2lib` by path, and both read the six volume **members** by name;
neither opens a `BUILDnnn` bundle. Chat 96's `r2-ch14l.out` is read **as a member** for the exact V
values rather than re-run, since re-running it needs a retired bundle.

No corrections were made and no Register entry was written: the chat-67 hold stands.

---

## A. Deviations

**14p-02 — "a signed sum of 2^(k+1) measured levels" is wrong at every k ≥ 1.** L6553–L6554 derives
the admissibility floor from the claim that the (k+1)-th difference is a signed sum of 2^(k+1)
measured levels. MEASURED: Δ^m T spans **m+1 = k+2 levels**, and 2^(k+1) is the sum of the absolute
binomial coefficients, not the level count. At the table's own k = 2 the sentence claims eight
levels where a third difference uses four. The **bound it derives is correct** — the accumulated
error really is at most 2^(k+1)σ — so the repair is one clause, not the argument.

**14p-03b — the |Δ^(k+1)T| column reproduces, but only under an unprinted window.** All four rows
reproduce to three significant figures from the hydrogenic term R/n² with the volumes' own
R = 109737.31568 and no quantum defect, under one convention: the m+1 consecutive levels nearest ν,
ties broken downward (ν = 20, k = 2 → n = 18…21 → 0.943384; k = 3 → 18…22 → 0.209407; k = 4 →
17…22 → 0.0760096; ν = 40, k = 2 → 38…41 → 0.0274552). §23.12 never states the window, and the value
moves across the admissible anchors by more than the rows differ from each other. **Tenth member of
the unprinted-input class, and the cheapest to repair — a convention, not a number.**

**14p-07 — the ten controls of §23.13 are a single witness.** L6570–L6571 states that controls
recover p = −1 and −3 correctly and that 9 of 10 fall within 5 %, printing neither the controls nor
their recovered values. MEASURED: "9 of 10" occurs at one site in the main volume. Unverifiable from
the six volumes, not merely uncorroborated.

**14p-08 — the Figure 23.4 caption is one order out of step with itself.** The caption states the
rule as |Δ^(k+1)T| > 5·2^(k+1)·σ and then defines a refusal as a sequence whose **k-th** difference
has the wrong sign. §23.12 uses (k+1) throughout.

**14p-11 — the +0.86 Hill-radius slope cannot be recomputed.** MEASURED: the slope is stated at two
sites, L6598 and L8633 (§31.1.1), and computed at neither; no line in the six volumes names the six
planets, their masses, their semi-major axes or their satellite counts, so r_H cannot be formed.
Eleventh member of the unprinted-input class. **Uncorroborated rather than single-witness** — the two
sites agree with each other and with the bibliography entry at L11790. (L4368's 0.86 % is a
different figure and is not part of this class.)

**14p-12 — "crosses the detection floor at order 7 exactly" rests on an unprinted floor.** With
e = 0.15, order 6 gives 1.13906 × 10⁻⁵ and order 7 gives 1.70859 × 10⁻⁶, so the claim implies a
floor in (1.709 × 10⁻⁶, 1.139 × 10⁻⁵]. No detection floor is printed at this site or anywhere in the
six volumes. Twelfth member of the class, and the word carrying the weight is *exactly*.

**14p-19 — two of §23.15's three "ν reached" figures are not the collection's.** MEASURED against the
Spectra Compendium's own tabulated ranges: Al I *n*f 55.0 is **exact** (row reaches 55.0); Na I *n*s
is printed at 20.0 but its row reaches **18.7** — 20.0 is what Na I *n*d, *n*f and *n*g reach, so the
figure belongs to a sibling channel; K I *n*d is printed at 45.7 and **no K I channel in the six
volumes reaches it** (nd reaches 12.7; the species tops out at 15.8 on ns). The ceiling verdict is
unaffected — both are far below their ν_V — but the column as printed is not the collection's. **The
strongest finding of this read.**

**14q-02 — 14n-A1 confirmed from the section itself.** L6501 sends the reader to §23.13 for *r* ≥ 5
and ν_V. MEASURED: §23.13 (Inversion, L6569–L6581) carries neither; §23.14 **L6585** carries both.
Repair is a retarget.

**14q-03 — the Ga I attribution closes against §23.15 (14k-02).** MEASURED: **no site in the six
volumes gives Ga I a ν_V.** §23.15 prints ν_V for three channels only; §23.11.1 L6538 gives Ga I a
refusal count and the verdict *a bifurcation*; §25.5 L6976 gives Ga I 51.7 under a header (L6972)
whose column is **ν**, not ν_V — read from the header, not inferred from the number. L6270 names
"Al I at *n* = 51 and Ga I at *n* = 53" while §23.15 lists **51 and 53 both** among Al I *n*f's own
four failing cells: L6270 hands one of Al I's cells to Ga I. Repair: L6270, against §23.15's list.

**14q-04 — the ν_V pointer closes on both citing sites (14k-01).** L6270 and L6923 both cite §23.11,
which carries ν_V zero times; §23.15 carries it four times. Both retarget to §23.15. With 14q-02 the
**pointer-off-by-one class now has five members inside Chapter 23 alone**.

**14q-06 — §23.14's heading sentence finishes in the body.** L6582 ends "…and the book has been
calling them" and L6583 is the single word " one". MEASURED: four sites of this shape in the main
volume — L4407 (+ "routes"), L6582 (+ "one"), L6634 (+ a table header), L8659 (+ "disanalogy"). A
small class, not a one-off; L6634 is not a sentence, so R3 reads all four before repairing any.

**14q-09 — "in every channel in this work" quantifies over a set the work never covers.** MEASURED:
the Spectra Compendium tabulates **477 channel rows**; a ν_V is printed for **three**. The three
satisfy the claim (14p-14); the other 474 are untested because no q is printed for them. Repair:
scope the sentence to the tabulated channels, or print q for the rest.

---

## B. Verified

**14p-01** — all four admissibility floors are exact: 5·2^(k+1)·σ gives 0.4, 0.08, 0.016, 0.004
against the printed 4.0 × 10⁻¹, 8.0 × 10⁻², 1.6 × 10⁻², 4.0 × 10⁻³, and **every row satisfies its own
rule** (|Δ^(k+1)T| > floor in all four).

**14p-04** — §23.12's "information per cell rises monotonically in k" is the correct restatement of
§23.10.2's V table, which chat 97 measured monotone in k across every row; §23.12 adds the reason (σ
stops the climb) rather than a new claim. Not re-measured.

**14p-05 / 14p-06** — §23.13's five recovered exponents all lie within 5 % of their integer targets
(Na I 0.350 %, K I 0.100 %, C₃ 0.025 %, α 0.143 %, C₆ 0.400 %), and **K I −1.998 sits on the exact-V
inversion −1.9975 to three decimals**. The printed values are nearer their integers than the
section's own asymptotic inversion is (C₆: printed 10.956, inversion 10.781, target 11), which is
exactly what L6573's "each recovered from its own measured series" claims. Tested against the eight
exact V values chat 96 banked, read out of `r2-ch14l.out`.

**14p-09** — "Every constraint in Λ is a CAPACITY" holds on the rebuilt lattice: all seven Heaviside
constraints (ℓ ≤ n−1, k ≤ 2(2ℓ+1), q ≤ k, f ≤ e−1, g ≤ 2(2f+1), g ≤ q, 2S ≤ k) hold on all 976 cells
and every one is a monotone cap. The three §23.14 prints are exact members of that set.

**14p-10** — L6585 carries `r ≥ 5`, `ν_V` **and** the difference rule, so §23.14 is the true home of
14n-A1's two objects.

**14p-13** — all three ν_V values reproduce exactly from (3Z²R/5q)^{1/4} at Z = 1 with R =
109737.31568, quantised half-up at the printed precision: 160.1867 → 160, 90.0796 → 90, 50.6555 →
50.7.

**14p-14** — "curvature washes out before separation" holds in all three printed channels: ν_V of
160.19, 90.08 and 50.66 against the r ≥ 5 separation ceiling of 405.717 at Z = 1 (record-carried,
chat 96's 14l-13).

**14p-15** — exactly one channel reaches its own ceiling (Al I *n*f, 55.0 > 50.66), so "the first
channel to reach its own ceiling" is true; "only" would be tighter, but a first is a first.

**14p-16** — "per cell, not a range cutoff" is refuted-as-a-range by its own list: n = 48 fails
**below** the predicted ceiling of 50.66 while 49, 50 and 52 pass across it, and 48…54 is exactly the
seven cells named.

**14p-17** — both denominators reproduce from the Spectra Compendium: **94 = 50+30+11+3**, Al I's
usable cells over its four channels; **55 = 39+8+8**, Li I's over its three undivided channels (the
two J-split rows would make 57).

**14p-18** — "eight of fifty-five … above *n* = 33" is what the population admits: only Li I np
reaches past n = 33, carrying nine raw levels there, and two of its 41 members are already unusable.

**14q-01** — both §-pointers in the unit resolve to the **claim**: §16.7 L4614 states the
defect-of-the-index against feature-of-the-world distinction L6593 cites it for, and §15.4 L4321
states the monotone bound q ≤ k that L6597 calls "exactly §15.4's form".

**14q-05** — §23.14's vocabulary claim is measured true in the direction it makes: every "capacity
bound" and "resolution bound" in the six volumes is at or after §23.14 (L6589, L6590, L6596, L6602,
L8633, L11790). The book had not been distinguishing the two kinds by name.

**14q-07** — Figure 23.4's caption carries no build or editorial remark (Ruling 45 clean), its asset
is listed in FIGURE_ASSETS.md, and Chapter 23's figure numbering runs unbroken 23.1 → 23.4, each
mentioned twice.

**14q-10** — the two cell counts of §23.15 reproduce (see 14p-17).

---

## C. Incidental

1. **No Register citation anywhere in the unit** — 74 lines, zero `register NNN` sites, lowercase
   grepped by hand. Chapter 23's late sections carry their authority internally.
2. **Six of twelve distinctive figures in the unit are single-witness** — 9.43, 10.956, 6.990,
   3.999, 1.998, 1.993. Chat 97 measured fourteen in 115 lines, chat 96 seventeen in 131, chat 95
   thirteen in 125; at 74 lines the density holds. Bare integers (94, 33, 160, 90, 55, 20) cannot be
   tested this way and were tested as phrases instead.
3. **Neither denominator is named where it is used** — the 94 and the 55 are recoverable only from
   the Spectra Compendium. A sample printed without its population; recoverable, so not a defect.
4. **§23.14.1's Hill-sphere framing is consistent across its four sites** — L5156, L6597, L7604 and
   L11790 all call it a monotone cap or capacity bound, and L8633 cites §23.14.1 correctly.
5. **§23.15's ν_V formula is restated twice in the Mathematical Compendium** (L40 and L2026), in
   both cases identically and with a §23.15 pointer at L40.
6. **The Register carries ν_V zero times**, as do the Physics Compendium, the Index of Indices and
   the Spectra Compendium. The object lives in the main volume and the Mathematical Compendium only.
7. **Al I's four failing cells are not contiguous with its ν range** — the channel runs to ν 55.0
   while the ceiling is 50.66, so five cells sit above the ceiling and four of them fail; n = 52
   passes above it. The section says this, and the numbers bear it out.

---

## Instrument faults, self-caught and rewritten — eleven this chat, none trimmed

1. `heading_line` and `section_span` were passed the member **text**; they take the **line list**.
   All five headings returned None.
2. The Δ^(k+1)T sweep tried **two** window anchors and declared the column unreproducible. Sweeping
   every anchor found all four rows reproducing under one convention. *A negative result from a
   sweep is a statement about the sweep.*
3. The celestial verdict said the planets appear nowhere **two lines below** a test printing that
   they do. Chat 97's fault class, hit again.
4. The corrected verdict then said "two sites" beside its own list of **three**, one of which was an
   unrelated 0.86 %.
5. §25.5's ν column was about to be read as a ν_V because the number sat beside Ga I; the header at
   L6972 settles it. *A token count cannot settle a pointer.*
6. The single-witness census used bare integers (94, 33, 160), which match hundreds of unrelated
   sites in every volume.
7. The vocabulary verdict claimed the phrases appear only after §23.14 **without measuring where
   they appear**; the line numbers were added and the verdict then stood.
8. The channel census counted species named beside the word "channel" anywhere, sweeping in eighty
   Register process entries.
9. The 94 was called unrecoverable **beside a printed table containing 50, 30, 11 and 3**.
10. The Li I verdict read 41.8 as the last **n** of the series; it is the last **ν**. The series
    ends at n = 42.
11. The first draft of the Ga I test dumped forty lines of Register matches for the bare token "Ga",
    burying the three sites that mattered.

Faults 9 and 10 were caught **after `r2-ch14p` was banked**; the golden was removed in a
delete-only call and re-banked, per the standing rule.
