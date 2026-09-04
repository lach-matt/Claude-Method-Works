# HANDOFF-77 — The Method 1.6 — chat 124 → chat 125

- Written from **chat 124** for **chat 125**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD153 compendia** (= BUILD152 + W-163 + DEF-124 + six new members). Register **1 to
  1792** (no Register entry since the chat-67 hold). W-163 IS seated; chat 125 seats nothing at open
  and writes W-164 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still the
  last: **a finding is not a question.** A deviation in the mathematics or in the prose is recorded
  and **flagged for repair**, never put to M. **Prints & Proofs is read before any question is
  asked.** The chat-81 cadence is unchanged: read, census in two kinds, exactly two instrument
  batches, never split a section read.
- **§32.7 is CLOSED, and with it chapter 32 and Part VI.** Chat 124 cut **L9307–L9392, 86 lines**,
  ending where `# PART VII` opens. **Main volume now 79.2 % read (L9392 of 11,855).**
- **MEASURED main-volume heading lines, to be re-taken by your own scan:** `# PART VII` **L9393**,
  `## 33.` body **L9399**, §33.1 **L9404**, §33.2 **L9427**, §33.3 **L9440**, §33.4 **L9455**,
  **§33.5 L9477** — *which HANDOFF-76 omitted; do not trust a carried heading list* — `## 34.` body
  **L9494**, §34.1 **L9500**. **Resolve every heading to its BODY occurrence**: `## 30.`, `## 31.`,
  `## 32.`, `## 33.` and `## References` each have two occurrences (contents L110–L175, body at
  L8316, L8609, L8790, L9399, **L11503**); taking the contents hit reports every attribution
  unbibliographed. **Chapters 20 and 21 are the exception:** their contents entries are plain body
  lines at L138–L139, so a heading scan of the contents sees 34 of 36.
- **The natural next unit is L9393–L9493 (the Part VII divider plus Chapter 33 entire, §33.1–§33.5),
  101 lines**, which closes a whole chapter and sits in the measured 74–150 band. Cut it yourself,
  re-measuring first, and say which you chose.
- **`section_span` CANNOT bound a section that ends a Part.** Chat 124's C1, and it refutes
  HANDOFF-76's prediction: for §32.7 `body_range` returned (9307, **9393**) and `section_span`
  (9307, **9399**) — `section_span` runs to the next **numbered** heading and steps straight over
  the `# PART VII` divider into Chapter 33. **Resolve under BOTH, always; say so when they coincide;
  bound the unit by `body_range`.** In chat 124's set §24.2, §29.6 and §32.3 COINCIDE; §32.6 and
  §32.7 DIFFER.
- **DO NOT RE-DERIVE these, measured in chat 124 inside its own unit:** the self-duality case
  **exact in both figures** — cells whose per-coordinate image lies in Λ₈ number **8** under
  *x* ↦ max − *x* and **112** under *x* ↦ max + min − *x*, from Λ₈ at caps (3,3,1,3,1), 976 cells,
  per-coordinate max **[3,1,3,3,3,1,3,3]** and min **[1,0,1,0,1,0,0,0]** (the minima are not all
  zero, which is the only reason the two maps differ); *Five worked cases* = **5 DATA rows**;
  *the other four things* = **4**; the falsification summary exact against §32.6's L9261–L9263;
  L9354's inequality orientation right against L6966 and L10047; **eleven authorities named and
  zero unbibliographed**; **P8 verbatim at L666**; the Register at **1,635 numeral headings (1,628
  bare + 7 grouped) and 1,660 distinct numbers, max 1792**; ***4ν/3* = 24 sites across six volumes**
  (main 22, mc 1, sc 1); PP **sixteen for sixteen at −94**; **zero** census rows, **zero** Ruling 46
  sites, **zero** first-person sites, **0 of 36** long lines recurring.
- **PP prints *one thousand one hundred and seventy-one* where the volume prints *one thousand six
  hundred and thirty-five*** (P9270/L9364 and P9282/L9376). That is why those two witnesses fail an
  exact match. It is a retired-basis datum, **not a defect**, and it is why the word-form 1,635 is
  recorded as absent from PP.
- **CONVENTIONS worth keeping.** The volume heads appendices **`## Appendix X — …`, twice** —
  contents and body — so `lettered_heading` (which matches `## B.1 …`) returns None for Appendix B
  and E; use a **body-occurrence appendix resolver**. `heading_line` is **numeric-only**: §E.1.4
  resolves to None though the volume heads it at **L10986**; a lettered pointer needs
  **`§([A-Z]\.\d+(?:\.\d+)*)`**. A pointer-site regex must be **`§N(?!\d)(?!\.\d)`**. A caption
  count is not a caption test — pair each embed against a following six-line window.
  **`\b(I|my|we|our)\b` matches the Roman numeral in *He I*** — guard it. **A literal species string
  is not a species test** (`Sc VI` scores zero in the Spectra Compendium, which carries Sc rows at
  L800–L810). **A count word over a table counts DATA rows.**
- **The book numbers its principles P1–P23 with P10, P12 and P18 unassigned — twenty in all
  (L233).** The phrase *Principle N* occurs **twice in six volumes, both as *Principle 8*** (L7947,
  L9316). Resolve any principle citation to the **P-form**, not the word form.
- **Census rows: measure them yourself** from DEFECT-CENSUS.tsv keyed on the column named `member`,
  whose values are `all`, `ioi`, `main`, `mc`, `pc`, `reg`, `sc` — **there is no per-filename
  value**. Columns are `id class member line item detail`. **Sweep classes `main` AND `all`.**
  Chat 124's range held **zero**.
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based, 11,855 lines); the bundle numbers each line one higher because of its `<<<FILE:` header.
- **The book's present is 2026.** **Figure references are a production layer:** 33 inline
  `![Figure …]` references, none in PP, no `.png` is a member, and an unresolvable image path is
  **NOT** a text defect.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard is
  **W-118 (chat 81)**. Project knowledge holds BUILD12/BUILD53 only — list it, never read those
  bundles. Retired handoffs are gone from Drive; never fetch or cite one. **Never add HANDOFF-NN.md
  as a member.**
- **Known and pre-existing:** the compendia bundle carries **48 legacy `HANDOFF-NN.md` members**,
  identical in BUILD122–153. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch16t is chat 124's) and W-101…W-163 in
  WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**53 `##` headings — 52 chat blocks plus the verbatim HANDOFF-25 block; chat 124's is the last**)
  governs; do not re-derive.
- **One open scope question, put to M by chat 113 and not yet answered** (a scope choice, not a
  finding, so properly M's): should R2's remaining scope stay a full source-order read of all six
  volumes, or should the five compendia be read against what the transversal sweeps have already
  covered rather than line by line? Measured basis: main volume now **79.2 % read at L9392**, the
  other five volumes 0 % in source order but swept transversally by every batch since chat ~90;
  measured rate ~74–150 main-volume lines per chat. **Do not re-ask it unprompted; carry it.**

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 124. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
< truncated lines 91-447 >
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Read those values out of the
  **member** rather than re-running the instrument.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 and required
  by the gate itself, now read by **twenty** banked instruments (MEASURED) — the certificates,
  OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 125

"Chat 125. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD153 compendia (7,218,771 B, md5
69aae2e381b1a07c5adcb891383373ac, 95,127 lines, 568 members). List uploads, outputs and /home/claude
first. Run HANDOFF-77's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 570 files), fetch the Prints & Proofs original 'The Method 1.6.md'
(738,550 B, md5 49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md because
twenty banked instruments read it, then gate.py census, run --core, manifest, run r2-ch16s
r2-ch16t, cert 125; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the
chat-95 block governs and it says a finding is not a question — deviations in the mathematics and in
the prose are recorded and flagged for repair, never put to M, and Prints & Proofs is read before
any question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 124's block is the
last of fifty-two chat blocks (fifty-three ## headings). The standing block's Phase 0–4
Löwdin/three-body plan is executed carried state; discard it per Ruling 41 — its discard is W-118.
Line numbers are MEMBER line numbers and are never carried between chats, and neither is any count
or any heading list — HANDOFF-76's heading list omitted §33.5 and chat 124 caught it by
re-measuring. §32.7 is CLOSED and with it chapter 32 and Part VI: chat 124 closed L9307–L9392.
# PART VII opens at L9393, '## 33.' body at L9399, §33.1 L9404, §33.2 L9427, §33.3 L9440, §33.4
L9455, §33.5 L9477, '## 34.' body L9494. Re-measure by heading scan, resolving each heading to its
BODY occurrence — '## 30.', '## 31.', '## 32.', '## 33.' and '## References' each have two
occurrences and taking the contents one reports every attribution unbibliographed, while Chapters 20
and 21 have only ONE because their contents entries are plain body lines at L138–L139. The proposed
unit is L9393–L9493 (the Part VII divider plus Chapter 33 entire, §33.1–§33.5, 101 lines), which
closes a chapter. Cut it yourself and say which you chose, preferring the cut that closes a movement,
and never split a section read. CRITICAL RESOLVER FACT measured by chat 124: section_span runs to
the next NUMBERED heading and steps over a '# PART N' divider — for §32.7 it returned (9307, 9399)
against body_range's (9307, 9393) — so a section that ends a Part cannot be bounded by section_span.
Resolve every pointer under BOTH resolvers, say so when they coincide, bound the unit by body_range,
and locate where a claim does live rather than only recording its absence — chat 124's 16t-01 found
§24.2 cited for the four unreachable documents when §24.2 is a species table and §29.6 carries all
of them. Count every count word against its own DATA rows, its numeral span, its own body's status
markers AND the Register entry that restates it — chat 124 found §29.6's heading saying three over a
four-row table, the third site of a tangle chat 122 opened at L9057. Test every list-opening
universal against every member of the list it opens: that is how 16t-03 found the fifth of five
worked cases with one site in six volumes. Read every cited criterion IN FULL at its target before
accepting OR rejecting the conclusion, and resolve a principle citation to the book's own P-form —
the principles are P1–P23 with P10, P12 and P18 unassigned, twenty in all, and 'Principle 8' at
L9316 is exactly L666's 'P8 says any true answer, good or bad, is a bound'. Name the convention
before scoring any figure: a self-duality count needs its map AND its membership test, and under
'cells whose per-coordinate image lies in Λ₈' the book's 112 and 8 both reproduce exactly. Never
round with Python's round(); use Decimal.quantize and name the convention. A numeral sweep must match
the printed thousands separator and the word form too. The volume heads appendices '## Appendix X —
…' twice, so lettered_heading returns None for Appendix B and E — use a body-occurrence resolver;
heading_line is numeric-only, so §E.1.4 resolves to None though the volume heads it at L10986 — a
lettered pointer needs §([A-Z]\.\d+(?:\.\d+)*). A pointer-site regex must be §N(?!\d)(?!\.\d). A
caption count is not a caption test. \b(I|my|we|our)\b matches the Roman numeral in 'He I'. A literal
species string is not a species test. Measure the census rows in range yourself from
DEFECT-CENSUS.tsv keyed on the column named member, whose values are all, ioi, main, mc, pc, reg and
sc; sweep classes main AND all; chat 124's range held zero. Do not re-derive chat 124's findings:
the self-duality figures exact at two of two, both count words exact against their data rows, the
falsification summary exact against §32.6's L9261–L9263, the inequality orientation right against
L6966 and L10047, eleven authorities named and every one bibliographed, P8 verbatim at L666, the
Register at 1,635 numeral headings (1,628 bare + 7 grouped) and 1,660 distinct numbers, 4ν/3 at 24
sites across six volumes, PP sixteen for sixteen at −94 with 1,171 printed where the volume prints
1,635, and zero census rows, zero Ruling 46 sites, zero first-person sites, 0 of 36 long lines
recurring. Then continue Phase R2 under the chat-81 cadence: read the unit in full, census its claims
into computable and prose, then run exactly two instrument batches, r2-ch16u computable and r2-ch16v
prose, importing heading_line, section_span, has_token, enclosing, Rset, L8_at and is_tree from
r2lib — copy nothing, pass them the LINE LIST and not the member text, read the six volume MEMBERS
never a BUILDnnn bundle path, and note that tower-2.py's L8 is a FUNCTION, so call it, and that
L8_at takes (n_max, e_max, l_max, k_max, f_max) in that order. r2lib.factor_q is a Λ₉ function and
cannot be called on 8-tuples. Report numeral SITES rather than counts. A symbol is tested raw and
never transliterated. has_token is letter-bounded on BOTH sides, so use a left-bounded matcher for a
stem, and test a Ruling 46 token case-sensitively and word-bounded. A colon-terminated lead-in is not
a list item. Anchor every Prints & Proofs witness on its own text. A heading-RANK scan can never end
a span. A token probe is not a reading; where a section is short, print it rather than probe it. An
identity entailed by another is not an independent test. A Register entry restating a count is not
independent corroboration of it. Sweep: every attribution against the BODY occurrence of ##
References and against R.7, and the reverse direction too; every register citation against its
entry's headline, grouped-aware and existence first; every section citing another for a figure the
cited section later withdrew. Figure references are a production layer: the volume has 33 and PP has
none, no .png is a member, and an unresolvable image path is NOT a text defect. The book's present
is 2026. Expect the instrument to be wrong before the book — that fired zero times in chat 124, four
in 123, three in 122, six in 121. Give every negative claim its own witness and state what a sweep
covered. Record the passes as well as the failures, or a class will look worse than the book is.
Index each volume once rather than rescanning it per phrase. Close the section read before the next
opens. At close: bank both goldens with gate.py bank, write W-164 ending with a blank line, build
BUILD154 with close.py (reverse must recover 69aae2e3…), write HANDOFF-78 BEFORE the final
verification, and begin the close with at least eight tool calls left. No corrections, no Register
entries, no TASK 1 until the review closes. Handoff at 90–95% of context or on a closed section read
— never earlier, never mid-section. Timeout on every call. Delete-only calls for pycache, never
chained to any other command. Never copy over an existing file."
