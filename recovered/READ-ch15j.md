# READ-ch15j — main L7721–L7855 (§28.8, §28.9, §28.9.1) — chat 110

Unit cut at a section boundary by my own heading scan: §28.8 L7721, §28.9 L7772, §28.9.1 L7774,
chapter 29 L7856. 135 lines, three subsections, under the 141-line ceiling. **This closes the body
of chapter 28.** §28.10 is printed inside chapter 29 at L8222–L8237 (15f-05) and is still owed as
its own short read, out of source order.

Census: two rows in range, MEASURED from DEFECT-CENSUS.tsv on the column `member` — 1169 (L7828)
and 1170 (L7847), both C9-OVERGENERALISATION-WORD. Instruments: **r2-ch15n** computable (banked,
9,529 B, md5 20cdb902, 134 lines) and **r2-ch15o** prose (banked, 14,485 B, md5 65dfc401,
176 lines).

---

## A — deviations

**15j-01 — §2.22 is a heading with no body, and it is cited twice in this unit as the reason the
register closes.** §2.22 *A corroborable entry must carry its object, and the object must carry it*
is at L1145 with body L1145–L1147, **zero non-blank lines**; §2.23 opens at L1148. The unit cites it
at L7809 — *The withdrawals register closes through §2.22, not through effort* — and at L7835 —
*That is why §2.22 is a requirement and not a tidiness*. **Empty in Prints & Proofs too**
(P1154–P1156, zero non-blank): authoring gap, not production loss. The cited requirement is legible
only from the section's title. This is the **third member of docket 1's heading-only class outside
§14.5**, after §28.7.6 (15i-03) and §28.9 below, and the first whose title alone carries the claim
two later sections lean on.

**15j-02 — §28.9 is a heading with no body, and the claim cited to it is printed in its
subsection.** §28.9 *The register, indexed and closed* is at L7772, body L7772–L7773, zero non-blank
lines, with §28.9.1 opening at L7774. L7806 cites *§28.9's envelope* for *repair ≤ φ(corroboration)*,
which is printed at **L7831, inside §28.9.1**. Under `body_range` the pointer is absent; under
`section_span` it resolves only because the span swallows the subsection. Also **empty in PP**
(P7694–P7695). Docket 1 and docket 9(a) together.

**15j-03 — the repair partition sums to 320 against a printed 319.** L7803–L7804: *Of 319 entries,
210 are recorded and not repaired, 93 are instance fixes, 10 reach class level and 7 produce a
protocol.* 210 + 93 + 10 + 7 = **320**, one over. Neither the four counts nor the total is
reproducible from the chapter, which prints 104 distinct numerals to a maximum of 164 (C11).

**15j-04 — the 67.5 % matches no denominator in the section.** L7851 states *67.5% recorded but not
repaired* for the 210 of 15j-03. 210/319 = **65.8 %**, 210/320 = **65.6 %**, 210/265 = 79.2 %,
210/248 = 84.7 %, all under `Decimal.quantize` HALF_UP and HALF_EVEN alike. 67.5 % is exact on a
denominator of 320 only at a numerator of **216**, not 210. The two figures cannot both stand and
neither reproduces; repair them with 15j-03 in one pass.

**15j-05 — the density superlative is false, and it is false in two volumes.** L7824–L7825: *density
68.8%, the densest object in this book after the periodic table's 71.4%*. The book's own
§12.11.1.1 table prints the eleventh axis at the book's caps (3, 3, 1, 3, 1) as
**10,585/13,585 = 77.9 %** (L3189, exact under both conventions, as are the other three rows). 77.9 %
is above both 68.8 % and 71.4 %. **Register 416 carries the same superlative** — *248 entries over 33
cells in a box of 48, density 68.8% — the densest object here after the periodic table* (reg L1547
heading, L1549 body) — so this is a main-volume/Register pair, docket 14 as well as docket 19. The
71.4 % comparison figure has **exactly one site in six volumes** (L7825) and is never computed
anywhere; 5/7 = 71.4 % is the only ratio that reaches it.

**15j-06 — "The six cells the register admits and lacks" lists three.** L7843–L7848 introduces six
and prints, semicolon-separated: *an owed entry caught by an instrument or from outside and repaired
at class level*; *an unreferenced entry that nonetheless produced a protocol*; *a fully referenced
entry repaired only to class*. Three, or four if the first is read as two (by an instrument / from
outside). Docket 21 (end-rule overstatement) and docket 31.

**15j-07 — L7740 cites §16.4 for a sentence printed verbatim in §7.2.** L7740: *That is §16.4 form —
one coordinate bounded by a monotone function of one other.* §16.4 is *D2 — ⅅ_def catches a wrong
derivation, but only under two routes* and carries no such form. §7.2 is titled **Every constraint is
of one form** and states at L1765: *Each constraint reads xᵢ ≤ φ(xⱼ) — one coordinate bounded by a
monotone function of one other.* The wording at L7740 is that sentence. App F.4.3 L11379 states the
closure rule in the same terms. **Identical in PP** (P7662 against P1769). Docket 9(a), and the
cleanest member yet: the true home is verbatim.

**15j-08 — the anchoring error has three attributed homes and is described at a fourth.** It is
**described** at §28.4 L7444 (*Anchoring on a published estimate*, the Ba I 5d² ¹G₄ point prediction
developed with a literature value). It is attributed to **§25.6** at L7472 (§28.6) and at L7723
(this unit), and to **§28.6** at L8080 (§29.7.1). §25.6 is *The one deduction, and why it is not a
prediction* — Sc VI's ⁴S° channel, eight non-blank lines, no anchoring content, **and the same in PP**
(P6923–P6932, seven non-blank). Docket 9(a) at event scale; docket 8 records a separate failing
pointer into the same §25.6.

**15j-09 — a Ruling 46 site inside the unit's closing sentence.** L7852: *stated here as a reading
whose conditions are the regex.* An internal instrument reference in a reader-facing volume. Docket
6.

**15j-10 — three Ruling 45 sites.** L7785 *Across this session its settled count rose by twenty*;
L7770 *it arrived last, from a question about a single row of a table*; L7749 *The book had built the
index and had not noticed it was one*. L7727's *An earlier draft* is a **new word-form** for docket
15's narrated-past-state class, which had nine sites in the form *an earlier version*. Docket 5 and
docket 15.

**15j-11 — the split heading.** L7721 ends *…and naming the* and the sentence finishes at L7722,
*dependency names the coordinate*, as body. Docket 18's fourth member (14q-06 held L4407, L6582,
L8659) — and **§16.4's own heading at L4407 is the same shape**, which the pointer work above
re-confirms.

**15j-12 — the four-class table prints its header twice.** L7753 and L7756 both read
*error · index that carries it · mechanism*, splitting one four-row table into a one-row block and a
three-row block. Docket 28.

**15j-13 — the fibre figures cover three of four layers.** L7822 fibres the index by §18.4.1's
four-body layer *object, law, procedure, reference*; L7839–L7841 gives LAW 44 entries / 11 cells /
E = 1, REFERENCE 23 / 11 / E = 8, OBJECT 80 / E = 19. **PROCEDURE is never printed**, and OBJECT's
cell count is never printed. The three printed layers total 147 against 248 or 319, leaving 101 or
172 unaccounted. Docket 10 (unprinted input).

---

## B — verified, so R3 does not re-derive

- **47 + 105 = 152** — the mathematics register's partition is exact (L7779).
- **20 + 19 + 6 + 1 + 1 = 47** — the unfinished itemisation is exact (L7782–L7784).
- **33/48 = 68.8 %** under HALF_UP and HALF_EVEN alike; the density column is cells/box, so its
  constancy across the three growth rows is structurally forced, not a copied figure.
- **The box of 48 is exactly the printed coordinate lists**: corroboration 4 values × caught 3 ×
  repair 4 = 48, counted from L7818–L7820. Absent cells 48 − 33 = 15, of which E = 6 are
  admitted-and-absent — internally consistent.
- **319 − 248 = 71**, so L7796's *Seventy-one entries and the shape has not moved* is exact.
- **The two rarest values** (L7805) are class 10 and protocol 7 — the claim holds on the printed
  counts.
- **Register 416 and Register 486 both exist and both support their citations** — 416 at reg L1547,
  *THE REGISTER IS AN INDEX AND IT CLOSES AT E = 6*; 486 at reg L1807, *THIS BOOK KEEPS TWO REGISTERS
  AND HAD ONE WORD FOR THEM*. Neither is grouped; neither is a false citation. (416 does carry
  15j-05's superlative — a defect of the entry, not of the citation.)
- **§16.5, §18.4.1 and §2.18 all resolve to their claims.** §16.5 carries the refused ionisation
  limit; §18.4.1 carries the four-body layer five times; §2.18 *What is computable, and what is
  decided* is exactly the division L7853 applies to the record.
- **0 of 70 long lines in the unit recur anywhere in six volumes** — the duplicated-section sweep
  (docket 27) gains nothing here.
- **No lower-case section opening in the unit.**
- **L7774's heading tag is the last of the volume's seven** *retained in the compendium* tags
  (L7426, L7481, L7506, L7531, L7559, L7644, L7774) — docket 5's heading-tag sub-sweep is now
  complete.
- **§14.5.7 measures 24 citations across six volumes**, exactly as chat 95 recorded; L7799 is one of
  them, and the eleventh in the main volume.

---

## C — incidentals

1. **The process index's box is never printed.** L7736–L7742 gives cells (step, visible,
   alternatives, committed) under *visible ≤ committed* and states *36 cells, closed, E = 0*, but no
   coordinate range. Twelve 0-based boxes admitting the printed anchoring cell close at exactly 36,
   all of the form step 3 × alternatives 4 × committed 2 with visible free — so 36 is reachable and
   the figure is not contradicted, only unreconstructable as stated. E = 0 under a single monotone
   constraint on a product box is structurally forced and is not a finding.
2. **The anchoring cell is correctly outside the closed set**: (step 2, visible 2, alternatives 3,
   committed 0) has visible ≤ committed false, so χ refuses it exactly as L7742 says.
3. **L7824's *248 entries* is the earlier state printed in the present tense** four lines after the
   table that carries the register to 319. Register 416 also states 248, so the prose is faithful to
   the entry it cites and stale against its own section. Docket 15's shape, but the figure is not
   wrong at its source.
4. **The chapter's numerals, measured:** 41 item lines, 17 of them heading a range, covering 104
   distinct numerals to a maximum of 164, with 59 printed twice and 60 numerals below the maximum
   never covered. Against L7780's *319 entries*, **155 numerals above 164 are never printed at all**.
   This corroborates docket 31 from a new direction and is measured, not re-derived.
5. **Census rows disposed.** 1169 (L7828, *a bound this book has never stated*) — the envelope is
   printed at five sites in three volumes, all of them this finding's own restatements
   (main L7806/L7831, reg L1549, mc L940/L946), so *never stated* is a claim about the book before ℛ
   and is not falsified: **not a defect**, regex artefact of the C9 class. 1170 (L7847, *an object the
   entry never names*) is a conditional about a cell that does not exist: **not a defect**.
6. **Ten paragraph-final lines carry no terminal punctuation**, of which eight are table rows,
   display blocks or headings; only L7751 (*The four error classes are one mechanism on four
   coordinates*) is a prose line, and it is a table lead-in. Not the 15b spliced-text shape.
7. **PP prints §28.9.1's heading as *From registers, and only one of them is a backlog***, where the
   volume prints *Two registers…*. Another count word filled in after the input — docket 32's sweep
   now has a member outside §28.7.

---

## Instrument faults — nine, self-caught, rewritten, none trimmed

1. **F1** the six-cells list split at the paragraph end and swallowed the following bold sentence.
2. **F2 (carries)** chapter 28's item numerals are printed **bold** (`**58.`) and many head a
   **range** (`**112–118.`); a plain `^\s*\d+[.)]` regex read **8** items where the chapter prints 41
   item lines covering 104 numerals. Any future numbering sweep over this chapter must match both
   forms.
3. **F3** the 36-cell reconstruction ranged over boxes that could not contain the printed anchoring
   cell, returning 63 candidates instead of 12.
4. **F4** literal `%%` in non-format strings.
5. **F5** — none reached the golden; see F6.
6. **F6 (carries)** the pointer-site regex `§N(?![\d.])` **rejects any pointer that ends a
   sentence**, because the sentence period trips the lookahead; §16.5 printed as uncited when it is
   cited at L7742. The rule wanted is `(?!\d)(?!\.\d)`.
7. **F7 (carries)** the claim test counted the **heading line** as body, so §14.5.7 — a section with
   zero body lines — scored RESOLVES on the word *seed* in its own title.
8. **F8 (carries)** `has_token` is letter-bounded, so the stem *corroborat* matched **nothing** in
   the whole corpus and reported the token absent from six volumes. A stem test must be left-bounded
   only.
9. **F9** §2.18 was recorded as unresolved on the token *division*, which is **my** word and not the
   book's; reading the section settled it as verified. A token test is not a claim test.

The book was right and the instrument wrong in F2, F6, F7, F8 and F9 — five times in one unit.
