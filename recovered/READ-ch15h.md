# READ-ch15h — main §28.7.3, L7559–L7643 (85 lines), chat 108

Unit cut at a section boundary: §28.7.3 alone. MEASURED by heading scan — §28.7.3 opens at L7559,
§28.7.4 at L7644, so the body is L7559–L7643. §28.7.4 was not read; the only figures below that
touch it are junction measurements, named as such. Instruments: `r2-ch15j` (computable, F0–F12),
`r2-ch15k` (prose, G1–G10), both banked. Prints & Proofs read as the original-input witness.

---

## A. Deviations

**15h-01 — the heading counts a span, not its items, and "all printed" is false.**
The heading reads *Seventy-five more from the audit work of the final session, **all printed***.
MEASURED (F1): fifteen item blocks, numerals 75–149, span 75 — but **63 distinct numerals are
printed**. Twelve are absent: **99, 100, 101, 102, 103, 104, 105** and **140, 141, 142, 143, 144**.
The count word is right about the span and wrong about the body.
**PP is the witness (G4):** the original input prints `### 28.7.3 From more from the audit work of
the final session, all printed — retained in the compendium here` at **P7482** — the placeholder
form. *Seventy-five* was filled in later, computed from 149 − 75 + 1, above a body with two holes
in it. This is DEF-107 item 1's class, now with a second instance and a mechanism.

**15h-02 — the same twelve are missing chapter-wide.**
MEASURED (F3) over `section_span(28)` = L7366–L7855: 104 distinct numerals across 49–164, gaps
exactly **[99–105, 140–144]**. The holes are not a section-scoped artefact; nothing later in
Chapter 28 prints them. PP has the identical gaps (G4) — **authoring gap, not production loss**.

**15h-03 — §28.7.4's heading is out by twenty-five (junction measurement).**
F4: §28.7.4 (L7644–L7663) prints numerals **150–164, fifteen distinct**, under a heading saying
***Forty** more*. Recorded from the junction scan only; §28.7.4 has not been read, and the next
chat measures it in its own read before this is treated as closed.

**15h-04 — *75–79. Four hypotheses* spans five numerals and prices four rules with three figures.**
L7560–63. Span 5, count word *Four*. Four rules are named — leaf, load, marginal, activity — and
three out-of-sample errors are printed: **652 %, 560 %, 1,156 %**. Both the numeral span and the
figure list are one short of the rule list.

**15h-05 — *80–83 … wrong three times* spans four numerals.**
L7565. Three failures are named (global slackening 1 of 7, one-sided slackening 13 of 140, and the
verdict line asserting a discrepancy its own output showed to be zero) across four numerals.

**15h-06 — item 89 is printed twice, word for word.**
L7571 as its own item, and L7577 as the third of *90–92*: *a tree-factorisation harness that
dropped two guards, giving 1,548 against 976*. F10 locates the sentence at both lines. One
correction, two numerals, and the second occurrence is inside a block whose count word (*Three*)
is exact only if the repeat is counted as new.

**15h-07 — items 110–111 are printed again inside *119–122*.**
L7599 and L7614 both carry *"E(X) > 0 means it is NOT closed" printed directly beneath E(X) = 0*
and *a re-coordinatisation offered as a repair that broke a closure which had not been broken —
0 became 27*. Two of the four in *119–122* are items 110 and 111 under new numerals. With 15h-06
this is twelve numerals for ten corrections in one section — and the twelve missing numerals of
15h-01 sit in the same list.

**15h-08 — two closing notes four lines apart count the same population differently.**
L7573–75: *Of the last fifteen corrections, eleven are in test harnesses and four in the book.*
L7579–80: *Of the last twenty corrections, fifteen are in test harnesses.* Between them lie the
three numerals 90–92. The population moves by five and the harness count by four where three
items intervene, and both notes state *35 of 35* for the book's equations. 11 + 4 = 15 is exact
(F5); the pair is not reconcilable with the items between them.

**15h-09 — four register self-citations, and neither reading corroborates.**
L7601–02: *Six of these are the same failure: a sentence written past the number beside it. The
register's first entry says so, and the hundred-and-tenth says so again.*
L7616–17: *The register's hundred-and-nineteenth entry is the same failure as its third.*
MEASURED both readings (G3), headline quoted before citing:
- **The Register compendium.** Entry 1 (reg L75) is *THE ORIGIN IS THE CLOSEST MEASURABLE DISTANCE
  TO ZERO…*; entry 3 (reg L83) is *FAMILIES BECOME SPATIAL NEIGHBOURHOODS…*; entries 110 (reg L511)
  and 119 (reg L547) are both *SUPERSEDED (Λ₈ successor development); see register 313.* None
  states the failure.
- **Chapter 28's own withdrawal numbering.** Items 110 (L7599) and 119 (L7614) are printed here and
  do fit; items 1 and 3 fall inside the unprinted 1–48 range recorded at 15g-04, so neither is
  checkable from the book.
The phrase *written past the number beside it* has exactly **two sites in six volumes**, both in
this section. Under either reading, half the citations cannot be verified — and under the second,
the section's own load-bearing self-reference depends on the numbering gap of 15g-04.

**15h-10 — §31.1 does carry the Hill-radius correlation the unit says it never carried.**
L7636–37: *§31.1's object list, missing six — including the Hill-radius correlation measured in
§23.14.1 and never carried across.* MEASURED: §31.1's span (L8614–L8658) prints **Hill stability of
hierarchical triples** (L8626), **Hill radius (μ/3)^{1/3}** (L8628) and **satellite counts vs Hill
radius — log–log +0.86 across six planets — §23.14.1's capacity bound** (L8633). The correlation is
carried across and cites §23.14.1 by name. **Census row 1165's *never* is a live defect.** Whether
§31.1 was repaired after the withdrawal was written is not decidable from the volume; the sentence
is false against the text as it stands.

**15h-11 — three failed pointers, each with its home located.**
Every pointer was resolved under `body_range` **and** `section_span` (G1); two first-pass absences
flipped to found and are not recorded.
- **§6.2's Janet table** (L7595). Absent under both resolvers in §6.2 (L1594–L1704). The Janet
  left-step table is **§6.1.1's**, at L1585 and L1587.
- **§30.3.1's characterisation** (L7626). Absent under both in §30.3.1 (L8405–L8416). *which is what
  produced the characterisation* is **§2.15.2's**, at L703 — and §2.15 is cited correctly six lines
  earlier for the ten that became bounds.
- **§23.10 and §31.1 both said matched-order V oscillates about Proposition 23.1's floor** (L7582).
  Absent under both in §23.10 (span L6434–L6518) and in §31.1. **§23.10.2 L6453 is the home** and
  its words differ: *An earlier draft claimed V stays near 2 at matched order and that Q9's
  conclusion … was an artefact.* §31.1 states nothing of the kind. Docket 15's shape — a withdrawal
  narrated against a section that has since been rewritten past it — with docket 9.

**15h-12 — *Five lists in one chapter* against four sections in two chapters.**
L7641–42, closing *145–149*, whose heading is *re-auditing Chapter 30 against its own §30.4*. The
five items name §30.4, §31.1, §31.2 and §31.3 — four sections, spanning Chapters 30 and 31 — plus
the unattributed *"The difficulty is not structural"*. Docket 21's shape at paragraph scale.

**15h-13 — a mid-sentence break inside item 123–139.**
L7621 ends *a sort direction guessed rather than derived, four times; a*, then a blank line, then
L7623 *criterion proved against the wrong closure operator*. G9's terminal-punctuation sweep found
exactly one such site in the unit. 15f-08's class, docket 26 — one formatting pass.

---

## B. Verified — so R3 does not re-derive

- **Span arithmetic.** 149 − 75 + 1 = 75; the heading's numeral is exact **for the span**.
- **Ten of the fifteen count words match their spans exactly** (F2): *Three* for 84–86, *Two* for
  87–88, *Three* for 90–92, *Six* for 93–98, *Three* for 106–108, *Two* for 110–111, *Seven* for
  112–118, *Four* for 119–122, *Seventeen* for 123–139, *Five* for 145–149.
- **123–139 reconciles twice over.** Ten that became bounds + (four + one + one + one) = 17 = the
  span; and *Ten of the seventeen … Seven produced nothing* gives 10 + 7 = 17. The named worst,
  **125**, lies inside 123–139.
- **§31.3's Pareto factor is exact.** 473,800,000 / 495,515 = **956.1769068544847…**, quantizing to
  **956** under both ROUND_HALF_UP and ROUND_HALF_EVEN (F6). §31.3.3 L8721–23 states the same
  factor and the same denominators (1,095 of 495,515 = 0.221 %), and calls the wide denominator
  *true and uninformative* — the withdrawal item and the section agree.
- **Eight levels against four at ν = 40, k = 3** (L7587) is corroborated verbatim at §23.10.2 L6457.
- **976 is exact.** Measured on the rebuilt lattice at caps (3, 3, 1, 3, 1): |Λ₈| = 976. The
  harness's 1,548 exceeds it by 572 cells, ratio 1.5861.
- **Seven constraints, six clustered, one extreme:** 6 + 1 = 7, matching Λ₈'s seven Heaviside
  constraints. *min(q, 4f+2)* at f_max = 1 takes the values {2, 6}.
- **Eleven + four = fifteen** (L7573).
- **Ten of the unit's fourteen section pointers resolve to their claims**, four of them only under
  `section_span`: §2.15, §16.7.2, §17.2, §23.10.1, §23.10.4, §23.14.1, §30.3, §30.4, §31.2, §31.3.
- ***The index was never deceived*** (L7569, census 1164) is not a false universal: **no site in six
  volumes** records the index as deceived.
- **Formatting sweeps clean:** no lower-case section opening; **0 of 32** long lines recur elsewhere
  in main (DEF-105 item 1 gains no member); every item block's final line carries terminal
  punctuation (F9) — the unit adds nothing to 15g-02's truncation class.
- **No Ruling 46 token in the unit** — no script name, build number, chat number, `register NNN`,
  W-entry or handoff reference.

---

## C. Incidental

1. **Ruling 45, docket 5 — the section's own heading tag** *— retained in the compendium here*
   (L7559), one of the volume's seven. The class reaches **twenty-five members**.
2. **Ruling 45 vocabulary inside the unit, seven sites:** *the final session* (L7559), *in one hour*
   (L7582), *the person operating it* (L7575), *I hardcoded it* (L7597) — first person singular,
   L7677's *collaborator's hand* class — *for an hour* (L7614), *for one message that was recorded
   as evidence* (L7631), *in the same session and not written down* (L7638).
3. **Docket 15 gains a ninth site in a new form.** L7584 prints ***The** earlier version's Figure
   15.3*; the eight carried sites (L6066, L6280, L6483, L6628, L6632, L6907, L7066, L8676) are all
   *An earlier version*. A sweep on the indefinite form alone misses this one.
4. **Figure 15.3 has one site in six volumes — its own** (G2). The text names it as withdrawn, so
   the reader is not sent to a missing object.
5. **Single-witness figures:** **1,156 %** is the only figure in the unit with a single site across
   the six volumes. 0.606 and 473.8 have two each (both in main); 495,515 has five, all in main.
6. **Q9 has two sites** — L6453 (§23.10.2) and L7589 — and they agree that the withdrawal was the
   error, not the finding.

---

## Census closures (8 rows in range, from DEFECT-CENSUS.tsv keyed on `member` == 'main')

| id | line | class | verdict | reason |
|---|---|---|---|---|
| 1 | 7584 | C3-FIGURE-POINTER-UNPLACED | not a defect | Figure 15.3 is named in the same clause as withdrawn; the pointer is to a stated absence, not an unplaced figure. New docket-15 site (C3). |
| 704 | 7584 | C7-WITHDRAWAL-LINE-NUMBER-SURVIVES | not a defect | regex artefact: *15.3* is the withdrawn figure's own label (precedents 678, 680–687). |
| 705 | 7604 | C7-WITHDRAWAL-LINE-NUMBER-SURVIVES | not a defect | regex artefact: *112* is a live item numeral opening the range. |
| 706 | 7604 | C7-WITHDRAWAL-LINE-NUMBER-SURVIVES | defect, already recorded | item 118 is printed at L7604 and again at L7608; DEF-107 item 7, not new here. |
| 707 | 7604 | C7-WITHDRAWAL-LINE-NUMBER-SURVIVES | not a defect | regex artefact: *71.8* is the measured value the item prices *V ≈ 8N* against. |
| 1163 | 7567 | C9-OVERGENERALISATION-WORD | not a defect | *never* sits inside the quoted claim the item withdraws (*"Self-consistency never defends against invention"*); the sentence corrects it. |
| 1164 | 7569 | C9-OVERGENERALISATION-WORD | not a defect | *The index was never deceived* is measured true: no site in six volumes records the index as deceived. |
| 1165 | 7637 | C9-OVERGENERALISATION-WORD | **defect** | *never carried across* is false: §31.1 L8633 prints the satellite-count/Hill-radius correlation and cites §23.14.1. See 15h-10. |

---

## Instrument faults, self-caught, rewritten, none trimmed

1. **F2 read the wrong word.** The first draft took the first number word anywhere in the head line
   as the count word and returned *one* from *one anomaly*, *two* from *two guards*, *one* from
   *one hour*. Rewritten to print **every** number word in the head sentence with its context and
   compare each against the span; the reading is done by hand. Without the rewrite, ten true
   matches would have been recorded as mismatches.
2. **F3 spanned a chapter with the wrong resolver.** `body_range(M, '28')` returns L7366–L7385 —
   heading to §28.1 — and the chapter-wide duplicate sweep found zero items in twenty lines.
   `section_span` is the correct resolver for a chapter, `body_range` for a section body. The two
   are not interchangeable and the instrument now says so in its own docstring.
3. **G1 recorded five absences on `body_range` alone.** A section pointer names the section
   *including* its subsections. Under `section_span`, **§31.2 and §31.3 both resolve** — §31.2's
   body is three lines and §31.3's is two, and each claim lives in a numbered subsection below.
   **The book was right twice and the instrument wrong.** Only the three that fail under both
   resolvers are recorded at 15h-11.
