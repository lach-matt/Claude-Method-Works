# READ-25b.md — chat 148 (Cowork) — 25b-03, DEF-143 item 11's fourth re-derivation

Instrument `r2-25b.py`, golden `r2-25b.out` (16,449 B, md5 49da811d, 169 lines). Not a section read: a family re-derivation
against docket 34 / 12 and DEF-138 item 6. Members read: `The_Method_1_6-2.md` (md5 4aef772b), `The_Method_1_6___The_Register-2.md`
(md5 79aaf239). Line numbers are this chat's measurements and are not carried forward.

## A — deviations

- **25b-03 CONFIRMED and NARROWED, on a reading.** E.8 L11217 *The cost is in Chapter 28. Sixty-odd corrections come from §30.3
  alone.* Chapter 28's own attributions: 123-139 = **seventeen**, whose lead-in L7619 gives them to *§30.3's reorderability
  problem* (and names §2.15 only as where ten of them are tabulated; L7626 *Ten of the seventeen … Seven produced nothing* —
  10 + 7 = 17, internally consistent); 145-149 = **five**, given to Chapter 30 *against its own §30.4*; 150-189 = **forty**,
  given to *the session that closed §30.3 and §32.2*. DEF-138 owed R3 a reading of the forty for their §30.3 share and warned
  that a token probe is not one. **The reading is now done and the forty are fully readable** — §28.7.4 prints the lead-ins for
  150-164 (fifteen) and the Register prints 165-189 (twenty-five entry bodies, 176-177 grouped under 175); no budget is owed
  (DEF-147 item 6's convention: a closed item's inputs are searched in the whole volume AND the Register first).
  Under **SUBJ** — an entry is §30.3's when its own text is about the objects §30.3.1-§30.3.9 define, §32.2's when it is about
  self-reference, NEITHER when it is another section's or an audit's, UNATTRIBUTED when its own text decides neither, every
  verdict carrying a deciding phrase the instrument asserts present in that entry — the forty divide **§30.3 33 | §32.2 1
  (167, P22 and the self-reference claim) | NEITHER 4 (150, 151 the §24.4 / §18.4 cross-references; 186 and 189, which §28.7.5
  itself calls the two entries about the audits) | UNATTRIBUTED 2 (172, 182)**. §30.3's own share of the record is therefore
  **17 + 33 = 50, upper bound 52**. Against E.8's figure under two named readings of the count word (BAND: STRICT 60-69,
  LOOSE 55-65): HEAD 17, SUBJ 50, SUBJ+ 52 are outside both; **BLOCK 57 reaches the loose band only by giving §30.3 the whole
  of a block the chapter shares with §32.2; BLOCK+30.4 62 reaches the strict band only by adding §30.4's five as well.**
  **No convention that respects *alone* reaches either band — the defective word is *alone*, not *Sixty-odd*.** Docket 34 / 12.
- **25b-07 (NEW) — §28.7's heading counts nothing it prints.** `### 28.7 Six made after the register was closed, two printed
  here` L7481: six lead-ins are printed (49-54), not two, and the block's own closing line L7502 reads *Two of these six are
  corrections of corrections*. The *Six* is right; *two printed here* counts neither the rows nor the closing line's two.
  Docket 34 / 23.
- **25b-08 (NEW) — §28.7.3's *all printed* is false, and its count word counts a range.** `### 28.7.3 Seventy-five more from the
  audit work of the final session, all printed` L7559: the block's numbers span 75-149 = seventy-five, but **twelve are not
  printed (99-105, 140-144) and 118 is printed twice** (L7604 inside 112-118, again alone at L7608) — **63 of 75 printed**.
  Docket 34 / 31 / 23.
- **25b-09 (NEW) — a second entry numbered 59.** L7517 in §28.7.1 (*Purity as a perturbation measure*) and L7533 in §28.7.2
  (*The cheapest undetectable forgery in Λ is 60 cells, not one*). §28.7.1's own block is 55-62 = eight and §28.7.2's is
  63-74 = twelve, so both count words are right and **the numeral is the defect**. Docket 31.

## B — verified

- The forty are 150-189: 189 - 150 + 1 = 40, and §28.7.5 names 186 and 189 as members. §28.7.4's heading names **both** §30.3
  and §32.2 (`['§30.3', '§32.2']`, measured). §28.7.1 *Eight more* = 55-62 = 8; §28.7.2 *Twelve more* = 63-74 = 12; §28.7's
  *Six* = 49-54 = 6; §28.7.3's *Seventy-five* = the span 75-149 = 75. §28.7.5's *Thirty-one of the forty* and its *186 and 189*
  are present as printed.
- The Register's front matter (*genesis 1-94, superseded 95-164, mature record 165-1792*) is exact over this band: **150-164 all
  read `**SUPERSEDED (Λ₈ successor development); see register 313.**`** and 165-189 all carry text. 176 and 177 carry no
  heading of their own and are printed inside 175's body — one of the seven grouped entries of docket 30's 1,635 = 1,628 + 7.
- **Register sweep: no WARNING line on any entry of 123-189 or on 313** (39 WARNING lines exist in the Register; none here),
  none of 150-189 is cited as *register N* in the main volume, and **E.8's sentence is the only *sixty-odd* site in either
  volume** — no later statement qualifies it (docket 17's single witness, already recorded).
- Resolvers, both run: §28.7.1-§28.7.5, §32.2 agree under `body_range` and `section_span`; §28.7 (7481, 7506) vs (7481, 7721),
  §30.3 (8399, 8405) vs (8399, 8575) and §30.4 (8575, 8583) vs (8575, 8609) differ, both reported. `lettered('E.8')` resolves
  to L11212; the numeric resolver returns None on a lettered heading, as the conventions record.

## Census

`CENSUS-CLOSURES-25b.tsv` — **ten rows**, the census rows lying in this unit's engaged range (main L7481-7677, §28.7 to
§28.7.5, plus E.8 L11212-11221; none of the ten was closed by any earlier closure file). All ten are **not a defect**:
ids 1 and 704 at L7584 (the withdrawn Figure 15.3, whose entry IS the record of the withdrawal), 705-707 at L7604 (entry
numbers 112 / 118 read as withdrawn line numbers, and the live 71.8), and 1161-1165 (C9 *never* inside claims the register
quotes in order to refute, or witnessed by 200 of 200 in the same line) — precedents 678, 680-687, 1067, 1069.
**Out of range and left open:** ids 1166 (L7700) and 1167 (L7703), which fall in §28.7.8-§28.7.9, not read by this unit.

## C — incidental

- L962 (§2.19-ish front matter) states the §28.7 pattern independently: *§28.7 states a count in its title — Eight more, Twelve
  more, Fifteen more, Forty more*. **Fifteen more names no §28.7.x heading in this build** (the headings are Eight, Twelve,
  Seventy-five, Forty) — a candidate for docket 34 / 15, not scored here: it is outside this family and belongs to whatever
  unit reads §2.19.
- **25b-10 — 150-164 are the chapter's single witness.** The Register is *the source* (front matter), and over 95-164 it carries
  no entry text; Chapter 28's descriptions of 150-151 (*two cross-references to §24.4 for a theorem in §18.4*) and 152-164
  (*thirteen implementation errors across nine attempts at a d ≥ 3 PQ-tree analogue*) cannot be checked against it. Docket 17.
- §28.7.5's *Thirty-one of the forty are one error class* is **not fully checkable**: only 165-189 (twenty-five of the forty)
  carry text, so a class census over all forty is impossible — a budget, not a negative. Docket 38.
- L7614's *119-122. Four from the shape work* repeats L7599's *110-111* almost verbatim (the nuclear-index commentary beneath
  E(X) = 0 and the re-coordinatisation that *broke a closure which had not been broken* — 0 became 27). Docket 26 / 23
  candidate, recorded, not scored: it is §28.7.3's, and this family's scope is the forty.
