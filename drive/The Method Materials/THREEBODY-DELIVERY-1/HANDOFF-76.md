# HANDOFF-76 — The Method 1.6 — chat 123 → chat 124

- Written from **chat 123** for **chat 124**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD152 compendia** (= BUILD151 + W-162 + DEF-123 + six new members). Register **1 to
  1792** (no Register entry since the chat-67 hold). W-162 IS seated; chat 124 seats nothing at open
  and writes W-163 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still the
  last: **a finding is not a question.** A deviation in the mathematics or in the prose is recorded
  and **flagged for repair**, never put to M. **Prints & Proofs is read before any question is
  asked.** The chat-81 cadence is unchanged: read, census in two kinds, exactly two instrument
  batches, never split a section read.
- **§32.5, §32.5.1, §32.5.2, §32.5.3, §32.6 and §32.6.1 are CLOSED.** Chat 123 cut **L9157–L9306,
  150 lines**, two movements whole, ending where §32.7 opens. **Main volume now 78.5 % read
  (L9306 of 11,855).**
- **MEASURED main-volume heading lines, to be re-taken by your own scan:** §32.7 **L9307**,
  `# PART VII` **L9393**, `## 33.` body **L9399**, §33.1 **L9404**, §33.2 **L9427**, §33.3
  **L9440**, §33.4 **L9455**, `## 34.` body **L9494**. **Resolve every heading to its BODY
  occurrence** — `## 30.`, `## 31.`, `## 32.`, `## 33.` and `## References` each have two
  occurrences (contents at L110–L175, body at L8316, L8609, L8790, L9399, **L11503**); taking the
  contents hit reports every attribution unbibliographed. **Chapters 20 and 21 are the exception and
  chat 123 measured it: their contents entries are plain body lines at L138–L139, not `## N.`
  headings, so a heading scan of the contents sees 34 of 36.**
- **The natural next unit is §32.7 alone (L9307–L9392, 86 lines)**, which closes chapter 32 and sits
  squarely in the measured 74–150 band. Cut it yourself, re-measuring first, and say which you chose.
  §32.7 has no subsections, so `body_range` and `section_span` should COINCIDE — say so when they do.
- **§32.7 is the thread chat 122 opened and chat 123 did not reach.** It is *On a verification that
  does not test its claim*, and chat 122 measured **L9328** as the second site of *twenty-member
  channel* and of *self-duality* + *involution* together — it re-tells §32.3's two traced audit
  failures. **Read §32.3 L9045–L9052 against it; the two accounts must agree.**
- **DO NOT RE-DERIVE these, measured in chat 123 inside its own unit:** the Sc VI table **exact in
  all six figures** — E(6s) **736,688**, lower **735,860**, upper **738,547**, width **2,687**,
  convex upper **737,380**, convex width **1,520** — recomputed from δ(4s) = **1.0057**, δ(5s) =
  **0.9812** (L7004) and the limit **892,700 ± 400 cm⁻¹ printed at L6914**, with Z_eff = 6, so the
  recomputation is **non-circular** and *no constant supplied by hand* holds; the **seven** display
  lines of §25.6.1+§25.6.2 (L7010, 7014, 7018, 7019, 7025, 7030, 7033); **33 embedded figures, 33
  distinct tags, 0 unpaired**; all 36 chapters present with **no** absent cross-reference and **no**
  § reference to an absent chapter; the condition-2 table exact at every cell and percentage
  (46/85 = 54, 56/63 = 89, 60/63 = 95); the condition-3 sweep at **three** sites for the four named
  words, two of them the test's own text; **0+16+40+5+4 = 65**; and registers **275, 387, 396 and
  573 all present and on point** — 396's five terms summing to **44** against its own printed 43,
  exactly as L9273 says.
- **Register 571 has NO ENTRY.** Cited at main L7719 and now L9274 (*Registers 571–573*). Do not
  re-derive; do not put it to M.
- **CONVENTIONS worth keeping.** The volume heads appendices **`## Appendix X — …`, twice** —
  contents L110–L175 and body — so `lettered_heading` (which matches `## B.1 …`) returns None for
  Appendix B and Appendix E. Use a **body-occurrence appendix resolver**. `heading_line` is
  **numeric-only**: §E.1.4 resolves to None though the volume heads it at **L10986**; a lettered
  pointer needs **`§([A-Z]\.\d+(?:\.\d+)*)`**. Both are owed to r2lib and carry provenance comments
  in r2-ch16q/r.
- **A caption count is not a caption test.** A line-anchored `^Figure N.N` regex returns 32 against
  33 embeds and scores a false mismatch; **pair each embed against a following six-line window**.
  Chat 123's fault 6.
- **`\b(I|my|we|our)\b` matches the Roman numeral in *He I*.** Chat 123's fault 8: L9241 scored as
  first-person prose. The unit's true first-person count is **zero**.
- **A literal species probe is not a species test.** `Sc VI` scores **zero** in the Spectra
  Compendium, which carries Sc rows at **L800–L810**. Chat 123's fault 9 — it would have recorded the
  book's one worked species as an absent member.
- **A pointer-site regex must be `§N(?!\d)(?!\.\d)`.** Chat 123's fault 4: `§(\d+)(?!\d)` reads the
  chapter part of every §32.5 as a bare §32 pointer.
- **A count word over a table counts DATA rows.** Chat 123's fault 1 counted the header and reported
  a seven-row table under a *Six of six* count word.
- **`body_range` and `section_span` DIFFER wherever a section has subsections.** In chat 123's
  pointer set **§32.1, §25.6, §16.5 and §16.3 DIFFER**; **§14.5.6, §6.3 and §29.2.2 COINCIDE**.
  Resolve under both, always, and **when they coincide say so**.
- **Census rows: measure them yourself** from DEFECT-CENSUS.tsv keyed on the column named `member`,
  whose values are `all`, `ioi`, `main`, `mc`, `pc`, `reg`, `sc` — **there is no per-filename value**.
  Columns are `id class member line item detail`. **Sweep classes `main` AND `all`**. Chat 123's
  range held **four**: 713 (C7, a live section label, artefact) and 1191–1193 (C9 *never*), of which
  **1193 disposed a DEFECT** and the other two not defects.
- **One global Prints & Proofs offset held across chat 123's unit at −94**, sixteen witnesses for
  sixteen, measured per witness on its own text. **Anchor every PP witness on its own text**; chat
  120 measured −88 and −94 inside a single 99-line unit.
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
  identical in BUILD122–152. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch16r is chat 123's) and W-101…W-162 in
  WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**52 `##` headings — 51 chat blocks plus the verbatim HANDOFF-25 block; chat 123's is the last**)
  governs; do not re-derive.
- **One open scope question, put to M by chat 113 and not yet answered** (a scope choice, not a
  finding, so properly M's): should R2's remaining scope stay a full source-order read of all six
  volumes, or should the five compendia be read against what the transversal sweeps have already
  covered rather than line by line? Measured basis: main volume now **78.5 % read at L9306**, the
  other five volumes 0 % in source order but swept transversally by every batch since chat ~90;
  measured rate ~74–150 main-volume lines per chat. **Do not re-ask it unprompted; carry it.**

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 123. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD152_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths.
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'38bd45711e2813dc9b73d8335a306103'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD152_compendia_papers_audits.md'}
SPILL={'main':'/mnt/user-data/tool_results/<main-id>.json','comp':'/mnt/user-data/tool_results/<comp-id>.json'}
for tag in ('main','comp'):
    b=base64.b64decode(json.loads(json.load(open(SPILL[tag]))[0]['text'])['content'], validate=True)
    m=hashlib.md5(b).hexdigest(); print(tag, f'{len(b):,} B', m, b.count(b'\n'), 'lines', 'OK' if m==EXP[tag] else 'FAIL'); assert m==EXP[tag]
    assert not os.path.exists(NAME[tag]); open(NAME[tag],'wb').write(b)
os.makedirs('/home/claude/members'); n=0
for tag in NAME:
    for m in re.finditer(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', open(NAME[tag],'rb').read(), re.S|re.M):
        p='/home/claude/members/'+m.group(1).decode(); assert not os.path.exists(p); open(p,'wb').write(m.group(2)); n+=1
print('members extracted', n)
EOF
```

   Expected: main 1,983,081 B · `49065309b0c4fe8e055f693aed295cca` · 18,470 lines; compendia
   **7,146,099 B · `38bd45711e2813dc9b73d8335a306103` · 94,030 lines**; **564 members extracted
   (2 + 562)**.
4. **Fetch the Prints & Proofs original before step 7** — `r2-ch15e`, `r2-ch15o`, `r2-ch15p`,
   `r2-ch15q`, `r2-ch15s`, `r2-ch15u`, `r2-ch15z`, `r2-ch16a`, `r2-ch16c`, `r2-ch16f`, `r2-ch16i`,
   `r2-ch16l`, `r2-ch16n`, `r2-ch16p` and **`r2-ch16r`** all read it and will fail on a missing path.
   Folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, title `The Method 1.6.md`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977 ·
   11,371 lines**, written to `/home/claude/PP_The_Method_1_6.md`. **Fifteen banked instruments now
   read it.**
5. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 14 s).
6. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
7. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **37,791 B ·
   c06506f22d3ac875e94fa7de5faf7b98 · 564 lines**; WORKING-REGISTER.md **793,430 B ·
   753d52cd7b3c6de6d881ab2b4a6b793d · 7,307 lines**, ends **W-162** (163 entries); DEFERRED.md
   **52 `##` headings / 51 chat blocks**; RULINGS-R2.md 9,844 B · 10a2ea7e · 82 lines (unchanged);
   r2lib.py 21,022 B · 580d2ea2 · 453 lines (unchanged); gate.py 9,377 B · a01ef15a;
   close.py 6,456 B · 98acae67; r2-tools.py 6,529 B · 4702f5f9; tower-2.py c0bce27a;
   census.py f5a73e2b; kinds.py 4262f7c5; minmax.py 26da1d78. If two `BUILD*_compendia` files are
   present after a close, pass `--comp <path>` explicitly.
8. `python3 /home/claude/members/gate.py run r2-ch16q r2-ch16r` → two `OK` (chat 123's goldens:
   r2-ch16q.out **14,494 B · dd756ed0 · 185 lines**; r2-ch16r.out **39,054 B · 97074f49 · 547
   lines**). Both are fast (≈ 2 s and ≈ 1 s); **r2-ch16r reads the Prints & Proofs path**.
9. `python3 /home/claude/members/gate.py cert 124` → writes `/home/claude/GATE-ch124.txt`, verdict
   PASS only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 123 did (do not repeat)

**Unit L9157–L9306 (§32.5, §32.5.1, §32.5.2, §32.5.3, §32.6, §32.6.1) read, censused, instrumented
in two batches, closed.** Ten deviations, nineteen verified groups, eight incidentals, four census
rows disposed. All of it is in `READ-ch16r.md` and DEF-123; **do not re-measure any of it.** The six
that carry:

- **16r-02 — *All 1,061* with the wrong referent.** L9188 makes it a count of **brackets**; main
  L6517 supersedes *§25.5's 1,061 order-1 bounds*, and L6683, L6958, L9354 and L10266 all make it
  the **perturbation-bound** count. Appendix B prints the bracket at **1,105 of 1,105** (head) and
  **1,577 of 1,738 cells across 392 rows** (§B.2). Same shape as chat 122's 16q-02.
- **16r-06 — *four indices* over five terms, and register 396 on the same side.** L9268 and L9302
  say four; L9270 prints five; L9273 says *its own five terms*. Under four, L9286's *the other three*
  fails. Register **396** carries the identical *across the four* over the same five terms.
- **16r-07 — register 571 cited and absent.** *Registers 571–573* at L9274. 572 is present but
  carries the ten mechanisms, not this claim; 573 is exactly on point.
- **16r-03 — §16.5 cited for a formulation it does not carry.** Read whole (L4449–L4470) it is
  **D3**, stating totality as χ_Λ total on the ambient box, verified on 6,912 points. *supported*,
  *cited*, *marked open* appear nowhere in it.
- **16r-05 — a count word its own table refutes.** *Thirty-nine claims … each has been given one*
  against a table showing **7 bare before repair and 3 after** — four repairs — in a paragraph that
  says the 54 %→89 % move happened *before a single repair was made*.
- **16r-10 — §14.5.6 cited for a pair it cannot carry.** Heading-only in BUILD90 (L3806–L3807) and
  in PP (P3772–P3775); *dishonest* has zero sites in the §14.5 span; the pair's home is **register
  573**, which prints *outside · dishonest* verbatim.

**16j-05 CLOSED as a finding.** §31.3.4 L8755's *fourth falsification test* is the fourth of §32.6's
three conditions plus its own. The enumeration exists and is printed **450 lines later**; none
precedes the ordinal. A forward reference, not a phantom.

**Negative witnesses recorded so classes aren't made to look worse than the book is:** the Sc VI
table exact at six of six from inputs the volume itself prints; the seven-line arithmetic reaching
at exactly seven; §16.3, §6.3, §E.1.4 and §29.2.2 all carrying their claims, §6.3 verbatim;
condition 1's first two checks and its figure pairing all still passing; condition 2's table exact
at every cell and percentage; condition 3 exact at one genuine hit; the E-terms summing to
sixty-five; the domination arithmetic closing three ways; registers 275, 387, 396 and 573 all on
point; PP at sixteen for sixteen at −94; and **seventeen consecutive units with zero duplicated
sections**.

**Nine faults, self-caught, rewritten in place, none trimmed.** The book was right and the
instrument wrong **four** times (faults 6, 7, 8, 9 above). Running tally: chat 110 five, 111 three,
112 zero, 113 one, 114 one, 115 two, 116 three, 117 four, 118 three, 119 two, 120 four, 121 six,
122 three, **123 nine**.

## Chat 124's section read

- **Re-measure the extent by heading scan before reading a line.** Proposed unit: **L9307–L9392
  (§32.7), 86 lines**, which closes chapter 32 and ends where `# PART VII` opens at L9393.
- **Sweep the classes chats 107–123 opened:** every count word against its own body, **its row
  labels**, **the numeral span**, **its own body's status markers** **and the Register entry that
  restates it**; every *N of these M* sentence; every list-opening universal against every member of
  the list it opens; every withdrawal item describing another section's state; every section
  declaring a defect repaired, re-read against the entry it cites; every section announcing a
  correction, checked at the corrected section AND in the Register; every attribution against
  `## References` **body occurrence** AND against R.7, **and the reverse direction too**; every
  superlative and index-size count against the book's own printed tables and against the external
  fact it names; every register citation against its entry's headline, grouped-aware, existence
  first; every *the earlier figure of N* against a digit-bounded sweep **in both the plain and the
  comma-grouped form**; every printed inequality against the orientation of its own symbols; **every
  cited criterion read in full at its target before its conclusion is accepted**; **every chapter
  named in a claim checked at that chapter and at its neighbours**; and every figure a section
  computes about the BOOK re-measured against the book as it now stands — chat 123's *18 / 18* is
  now 33.
- **What the docket owes anywhere in the volume**, to test if the unit touches it: docket 5's Ruling
  45 prose sweep (**now one hundred and eighteen members**; chapter 32 is the densest region
  measured and §32.6/§32.6.1 denser still); docket 6's Ruling 46 sweep — run 5 and 6 in one pass,
  **case-sensitively** (**now twenty main-volume sites**, chat 123's L9169 *this book's own markdown*
  being the last); docket 9's pointer sweep, with **§24.6 and §25.6** as magnets; docket 19's
  false-universal sweep; docket 20's absent-member sweep; the duplicated-section sweep (DEF-105 item
  1); and the placeholder-heading sweep (DEF-107/108/109 item 1, DEF-110 item 12).
- **The channel table remains the arbiter for every species figure.** Section II is spectra-member
  **L293–L934**; its totals line is **L900**: *596 channel rows across 28 elements · 2,269 interior
  cells parsed.* Bound every parse to that span and check it against L900 before trusting one figure.
  **Appendix B's own 153 is the superseded figure (15n-07, and chat 123's 16r-01 is a new
  re-assertion site) — do not use it as a denominator.**

Instruments: **r2-ch16s** (computable) and **r2-ch16t** (prose). Import `heading_line`,
`section_span`, `has_token`, `enclosing`, `Rset`, `L8_at` and `is_tree` from r2lib by path; **copy
nothing**; **read members, never a bundle**; **pass the resolvers the LINE LIST**. Functions still
owed to r2lib and carrying provenance comments in r2-ch16q/r: **`body_range`**,
**`lettered_heading`**, **an appendix body-occurrence resolver**, **a lettered-pointer resolver**,
**`numsites`** (comma-aware), **`regentry`** (grouped-aware), **`joins`**, an **8-tuple transfer
factorisation** to replace `factor_q`, a **meet-characterisation join-irreducible counter**, and a
**space-aligned table parser that sees a wrapped first column**. Note `T.L8` in tower-2.py is a
**function**: call it, and remember `L8_at(caps)` takes `(n_max, e_max, l_max, k_max, f_max)` in
that order and returns 8-tuples whose index 1 is ℓ. **`r2lib.factor_q` is a Λ₉ function** and cannot
be called on 8-tuples; for Λ₈ the halves are source (n, ℓ, k, 2S) = 0,1,2,7; transfer q = 3; target
(e, f, g) = 4,5,6.

**Standing method, unchanged and all of it earned:** exact-token heading resolver, never prefix,
resolved to the **body** occurrence; never span a section by heading rank; grep lowercase
`register NNN` by hand; check every printed pair count against C(N, 2) and name the denominator;
resolve every pointer to the claim and not the heading, **under both `body_range` and
`section_span`**, **and locate where the claim does live**; test on the **raw** line,
case-insensitively, word-bounded, in the word's other forms, left-bounded for a stem — and check the
stem actually contains the word's other tenses (`withdraw` misses `withdrew`) — **raw for a symbol,
never transliterated**, and on the whitespace-normalised two-line join as well as the line. Give
every negative claim its own witness and **state what a sweep covered before recording a negative
from it**. Where a section is short, **print it rather than probe it** — chat 123 printed §16.5,
§16.3, §6.3, §14.5.6, §E.1.4, §29.2.2, §31.3.4 and Appendix B whole, and three of the ten deviations
were only visible in the full text. Check the arithmetic of every ratio and percentage; **never
round with `round()`** — use `Decimal.quantize` and name the convention, and run all conventions
before scoring a percentage wrong. **State a budget rather than a negative** when a computation is
too large. **Sweep the convention, not just the base** — a Gröbner basis size is meaningless without
its monomial order, a closure size without one step against fixed point, and a surplus without its
ambient space. **Derive a table's convention from the book before scoring the table** — chat 122
recovered surplus = |J| − log₂(cells) from L2149; **chat 123 recovered the Sc VI limit from L6914
and only then found all six figures exact, which is what made the recomputation non-circular.**
A formula numerator is not a value; a citation is not a declaration; a heading is not a statement; a
bound is not a measurement; an assertion is not a proof; a count of headings is not a count of what
they contain; a numeral is not a corroboration; **a token probe is not a reading**; a
colon-terminated lead-in is not a list item; **a count word may reach only the items sharing one
label, and it counts DATA rows**; **a Register entry restating a count is not independent
corroboration of it**; a section that says a defect was repaired is not evidence that it was; a
section that cites a criterion is not evidence it applied it — but reading the criterion whole may
equally clear the citation; **an identity entailed by another is not an independent test**; a
chapter cited as an authority may be the chapter next to the one that carries the claim; **a literal
species string is not a species test**; and a token test is not a claim test. Where the text prints a
sample, measure the population. **Match a printed figure at the source's precision, not at yours.**
**Grep the volume and the Register for a later or exact statement before recording any figure as
unreproducible.** **When an instrument disagrees with a hand reading already taken from the file, or
with a totals line the source states about itself, the instrument is wrong until proved otherwise** —
chats 94–123 hit that twice, four, three, twice, twice, twice, twice, once, three, four, ten, seven,
five, twice, twice, three, five, three, zero, once, once, twice, three, four, three, twice, twice,
twice, three and **four times**.

## The repair docket

Carried forward until R3 executes it. **None of these goes to M.** Chat 123's additions are in
DEFERRED's chat-123 block in full; **DEFERRED.md's 52 blocks govern in detail** and the list below
is the standing index, unchanged from HANDOFF-75 except where chat 123 moved it.

1. **§14.5.2–§14.5.7 — six heading-only sections, forty citations. R3's largest single item.**
   MEASURED against Prints & Proofs: **authoring gap, not production loss.** Citations: §14.5.2 → 4,
   §14.5.3 → 1, §14.5.4 → 4, §14.5.5 → 4, **§14.5.6 → 3 plus chat 123's L9281 (16r-10)**,
   §14.5.7 → 24. Order: read the Register's nine §14.5.7 citations first and author to what they
   already say, then §21.5.4, then the Mathematical Compendium's twelve. Chat 90's **seed(Λ₈) = 7**
   is the settled material. **For §14.5.6 the material already exists in register 573**, which prints
   *outside · dishonest* verbatim. **The class outside §14.5 is three: §28.7.6 (15i-03), §28.9
   (15j-02) and §2.22 (15j-01) — and §2.22 is the urgent one.** Joined by 15g-02's truncated item 74,
   15h-01's twelve unprinted numerals, and chat 119's §31.3 zero-body-line consistency point.
2. **The §18.4.1 one-dimensional refinement — a missing Register entry** (main L5977–L5980).
   Register 319, which the passage cites, states a different claim. Chat 118's second member: the
   §18.5 pole correction announced at L8639 has no Register entry at all (16g-08).
3. **The Register has no entry for the correction §23.10.2 cites** (14n-A3). Adjacent: §23.10.2
   L6455 cites *the correction … recorded at 96–98*, printed at §28.7.3 L7582.
4. **The σ collision.** Rule 4 (main L6047) defines σ = 2R Z_eff² · SE_pred / ν³; §22.5 (L6168) uses
   σ as the levels' measured uncertainty, and substituting cancels ν³ identically — MEASURED
   r = 100.000000 at ν = 10, 20, 40, 80. Paired with 14x-04 and 15f-01 (69.6 % against 68.1 %).
5. **The Ruling 45 class, one hundred and eighteen members** — HANDOFF-75's one hundred and one plus
   **chat 123's seventeen (L9168, L9169, L9172, L9226, L9235, L9236, L9237, L9239, L9240, L9242,
   L9244, L9261, L9262, L9265, L9269, L9271, L9272)**, all present in PP. **Chat 115 supplies the
   class's discriminator and R3 must apply that split to the whole standing list before repairing any
   of it.** The seven heading tags are recorded and that sub-sweep is CLOSED. Captions state facts
   only. **Chapter 32 is the densest region measured, and §32.6/§32.6.1 denser than §32.2–§32.4.2.**
   **First-person prose: chats 113–123 clean inside their units; L4415 (*I wrote*, §16.4) is an
   out-of-unit member.**
6. **The Ruling 46 class — twenty main-volume sites** (15f-04's seventeen, chat 120's L8816
   `bookindex.py`, chat 122's L9107 `rclose.py` — both absent from PP — and **chat 123's L9169
   *this book's own markdown***), five Register sites, 15i-10's Register purpose paragraph
   (L7658–61) and 15j-09's L7852. Run 5 and 6 together, case-sensitively.
7. **RESOLVED AS A FINDING, chat 113 (15m-06), not as a repair.** §23.8.3's affine-invariance reason
   is stated at §23.8.3 L6368 itself; §29.7 L8052 is an attribution row naming self-concordance
   without a reason. 15b-07 remains adjacent: §23.8.1 L6345 is λ²'s home and L7185 should point there.
8. **CLOSED as a finding (14z-08), not as a repair.** §23.6 L6319's pointer into §25.6 has no target
   anywhere in the volume. 15j-08 adds two more failing pointers into §25.6 — **§25.6 is a magnet.**
9. **The pointer class, four-headed.** (a) *Off-by-one and wrong-target pointers*, **forty-three
   members**, now including **chat 123's 16r-09** (the backwards range §32.1–24.4). (b) **Register or
   principle citations whose target says nothing of the claim** — 15h-09's four, 15i-06's Register
   286, 15l-03's Principle 8, 15m-04's §29.7, 15n-03's registers 253 and 254, 16j-03, 16j-02,
   16m-05, 16o-06, 16q-04, 16q-05 **and chat 123's 16r-03 (§16.5 cited for a bibliographic totality
   it does not state) and 16r-10 (§14.5.6, heading-only, cited for a pair whose home is register
   573)**. (c) **Register citations with no entry at all** — 15i-09's 571, **now cited three times
   (main L7719, L9274)**. (d) **An event with four attributed homes and a fifth where it is
   described** (15j-08 + 15m-05), plus chat 118's §11.7 self-citation at L2260. **Chats 117–123 are
   the class's counter-cases: four-for-four, eleven-for-eleven, two-for-two, seven-for-seven,
   nine-for-ten, nine-for-eleven, and eleven-for-fifteen.**
10. **The unprinted-input class, sixty members** — unchanged by chat 123.
11. **The 32/11 scope docket** (14j-01), six measured main sites — L6193, L6213, L6233, L6237,
    L6381, L10245 — plus 2.909 at four. *4ν/3* has **24 sites** and *32/11* **8**.
12. **The truncation-printed-as-equality class** (14l-02/03, 14n-A10, 15b-04, 15d-02, L7308's
    asymptote-as-price, 16d-01, 16g-01, 16j-02, 16m-05).
13. **The two unsourced counts of L6517** (14n-A6/A7) — *619 refusals* and *§25.5's 1,061 order-1
    bounds*; the recomputation at matched order is still owed. Item 55 (L7507) restates it.
    **Chat 123's 16r-02 is the same figure used as a bracket count at L9188.**
14. **The main-volume/compendium contradiction class** (14p-19, 14r-01/02/03, 14t-02/07/08, 14v-06,
    14x-05, 14z-03/04/13, 15b-06, 15j-05, 15k-09, 15l-07, 15m-02, 15n-01, 15n-07, 16j-01, 16m-01,
    16m-06, 16o-03, 16o-05, 16o-07, 16q-01, 16q-02). **Chat 123 adds 16r-02 (1,061 as a bracket
    count), 16r-06 (*four indices* with register 396 on the same side) and 16r-08 (ten open items
    against §E.1.4's eleven).** Resolve K I *n*d 45.7 first, then Ne I 16/131 and K I 4/105.
15. **The retired-basis / narrated-past-state class** (14t-01). *An earlier version* has **8 main
    sites**; *an earlier draft* **7**; *a previous draft* none. R3's sweep must cover all three forms
    and *from recollection* (L8018), *the earlier figure of N* (L8329), *now states* (L8311, L8584,
    L8588, **L9240**), *the guess that preceded it* (L8293), *the earlier reading* (L8379), *a draft
    withdrew* (L8411), *the withdrawal is withdrawn* (L8412), *it is now discharged* (L8460), *was
    tried first here* (L8470), *what reopened the question* (L8545), *the relation set has grown
    since* (L8584), *the missing Chapter 30* (L8838), the whole *first reading* apparatus of
    §32.1.1, 16o-05, 16o-08, chat 122's L9065, **and chat 123's L9271 (*An earlier form of this
    section*) and L9222 (*This chapter was written as Chapter 31* — printed inside Chapter 32)**.
16. **The Edlén dating docket (15l-04, superseding 14r-20).** **1960 at 4 lines** against **1964 at
    25**, listed in DEF-112 item 4. Joined by **15l-05**, **15l-07**, **15n-05** and **16j-04**. Also
    here: the Nesterov name-form sweep (14m-07); *"KI"* without its space at L6657/L6716/L6704;
    *"neon II"* at L6704; 14x-08's *Cooper-type node* at L6896; 15i-12's *detector artifact*.
17. **The single-witness class** — HANDOFF-71's list plus chat 118's three (47.9 · 6.9 × 10⁻⁴ ·
    3.6 × 10⁻⁹) and chat 122's 2,873. Chat 115's refinement stands: figures recomputed here are not
    single-witness in the strict sense, only the unrecomputable POPULATION COUNTS are. **Chat 123
    adds none — every figure in its unit is recomputable from the volume, which is exactly what
    §32.5 claims and, for the six of the Sc VI table, achieves.**
18. **Heading sentences finishing in the body** (14q-06) — five: L4407, L6582, L8659, L7721, L7856,
    plus the paragraph-scale form at L8325 and the inverse at L8419–L8422. **Chat 123's unit adds
    none.**
19. **The false-universal and superlative class** (14v-01, L6970, L7075, 15f-06, 15h-10, 15j-05,
    15l-02, 15m-03, 15n-C4, 15o's L8281 UNMEASURABLE, 16d-03, 16g-05, 16g-06, chat 119's
    unfalsifiable-test form, 16m-06). **Chat 123 adds L9304 (*are not open items and never will be*,
    census row 1193 disposed defect) and supplies counter-cases: L9190's *a reader with these pages
    and no internet* holds for the six figures actually recomputed, and condition 3's *No claim in
    this book is left in limbo* survives its own sweep at one hit.**
20. **The absent-member class** (14v-02, 14x-05, 14z-13, 15b-09, 15m-07, 15n-06). C IV, **Sr at any
    stage**, the sulphur-like sequence, **Rb in six volumes**, three of the four authors of the
    survey cited at L8096, and Kurucz, VALD, BRASS, Hasse and QSAR. MEASURED stage lists: Ca I II IX;
    Ba II III; Ti III XI; Sc III; Hg II; Al I II III IV; Ga I II; Li I II III; **Sr none; Sc VI none;
    Rb none.** **Chat 123's caution: the literal string `Sc VI` scores zero in the Spectra
    Compendium, which nonetheless carries Sc rows at L800–L810 — re-measure this class with a
    notation-tolerant probe before repairing any of it.**
21. **The end-rule overstatement** (14v-07) — §24.13's L6877/L6879; 15f-03 runs the other way;
    15g-09, 15h-08, 15h-12 (CLOSED by chat 118 as 16g-03); 15i-04/05; 15j-06; 15k-05; 15k-06;
    15l-02; 15m-08; 15o-01; 16b-01/02; 16d-04; 16g-02; 16g-04; 16j-01; 16j-05 (**CLOSED by chat 123
    as a forward reference**); 16m-02; 16o-03. Sweep all twenty-three.
22. **The census anchor** (14v-08) — §24.12 must state which member of a sequence D is computed on,
    and print the census's range (27 + 12 + 5 = 44 sequences).
23. **The caption-corrected-but-not-the-prose class** (14x-02), at section scale (14z-01),
    cross-volume (15b-06), Register-scale (15d-05, 15f-07), twice in chat 107, at register-citation
    scale in 15h-09, at repair-declaration scale in 15i-06/07, at repair-execution scale in 15k-07,
    cross-volume in 15l-04/05, at CHAPTER scale in 15m-01, at CORRECTION scale in 16g-08, at APPENDIX
    scale in 16m-06. Negative witnesses: App D.5.2 L10575, Figure 23.1 → 30.1, PP's *Figure 23.2* →
    **Figure 30.2**, §31.2.2's correction registered at 1787, chat 119's register 387, chat 120's
    registers 424–426, chat 121's twenty-for-twenty, chat 122's five-for-five, **and chat 123's
    four-for-four on registers 275, 387, 396 and 573 — with 396 a member through 16r-06.**
    **The largest live class after item 1.**
24. **Two compendium data defects** (14x-09/10): spectra **L562**'s malformed `n 41–5` (read 41–55),
    and **nine duplicated (species, series) keys over 18 rows**.
25. **The inherited-estimate class** (14z-02) — sweep every bracket for an edge tracing back to an
    estimate. **Adjacent, chat 123: §25.6.1 L7019 adds *the limit's own ±400 to be added at both
    edges*, and §32.5.1's table carries no such caution.**
26. **The spliced-text class** (15b-01/02) — main **L7156**; 15f-08's L7405–07; 15h-13's L7621–23;
    chat 116's L8401; chat 117's L8564–L8565; 16o-07's L8908–L8912. **Chat 123 adds none, but
    L9196–L9197 (*Λ contains the cell the book says every number the prediction needs*) reads as a
    join of two clauses and is present in PP in the same form.**
27. **The duplicated-section class (15d-01).** §9.2 L1961–L1990 and §27.5.1 L7299–L7330 are one
    passage with two Register entries, 438 and 446. **Chats 106–123 ran the sweep on their own units:
    0 of 71, 55, 32, 44, 70, 38, 51, 76, 75, 53, 65, 67, 47, 70, 95, 45 and 57 long lines recur —
    seventeen consecutive clean units.**
28. **Table formatting (15d-04)** — four of Chapter 27's five tables are space-aligned and §27.1's is
    shattered mid-word, in PP too; 15f-09's thirty lower-case section openings; §28.6's header
    shattered at L7462–64; 15j-12's four-class table printing its header twice; 15k's attribution
    continuations; §29.7 as two blocks; chat 116's L8421; chat 117's step-law table; chat 120's
    §32.1.1 E(book) table; chat 121's §32.1.4 and §32.1.3 tables; chat 122's recursion table and both
    §32.4.2 tables. **Chat 123 adds the contents entries for Chapters 20 and 21 (L138–L139, plain
    body lines where all thirty-four others are `## N.` headings) and §31.3.4's sub-headings numbered
    24.3.4.1 / 24.3.4.2 / 24.3.4.3 at L8738, L8755, L8777.** One formatting pass.
29. **Section order (15f-05). MEASURED AND CLOSED AS A FINDING in chat 111.**
30. **The Register's own size (15f-02), five figures over twenty-three sites.** **1,635** in words at
    **fifteen** main sites (L20, 89, 104, 202, 523, 646, 3514, 7367, 7900, 8918, 9055, 9364, 9376,
    9381, 10296) and absent from PP; **1,635** in digits at main **L7373** and reg L6, L65, L6127,
    L6133; **1,631** at main L7658; **1,628** bare headings at reg L6109, L6115; and a measured
    **1,660 distinct entry numbers (1,628 bare + 7 grouped spanning 32), maximum 1792**. Adjacent:
    the front matter's *571 entries are cited by other entries* against `register_cites.py`'s
    **593**; 16o-04's *the register is a quarter of it*; and 16q-02.
31. **The item-numbering class (15g-01, 15h-06/07, 15i-01/02/04/05, 15j-03/04, 15k-09, DEF-107 item
    7, 16j-06).** MEASURED in chat 110: chapter 28 prints **41 item lines, 17 of them heading a
    range, covering 104 distinct numerals to a maximum of 164**, with **59 printed twice** and **60
    numerals below the maximum never covered**; against L7780's *319 entries*, **155 numerals above
    164 are never printed at all**. R3 repairs the chapter-28 part in **one numbering pass**.
32. **The placeholder-heading class (DEF-107/108/109 item 1, DEF-110 item 12).** PP prints §28.7.2,
    §28.7.3 and §28.7.4 with placeholder headings where the volume prints *Twelve more*, *Seventy-five
    more* and *Forty more*. §28.7.7's *119* is in PP already. §28.9.1's PP heading reads *From
    registers…* where the volume reads *Two registers…*. 16j-06 belongs here too.
33. **The §3 audit numbering (15i-08).** §3 prints numbered rows **1–7**, names twelve more at
    L1024–25, and states *twenty-two audits*; §2.19.1 cites *audit 15 ENUMERATION*, §28.7.5 cites an
    *exhaustiveness clause* that appears nowhere in §3, and §28.10 L8234 cites *part 2 of the audit*.
    15l-03 is the same shape for the principles; 16j-05 for the falsification tests (**CLOSED by chat
    123**); 16m-02 for the referee flags; 16o-08 for the audit count at three values; 16q-01;
    **and chat 123's 16r-06, *four indices* over five terms, the same shape at index scale.**
    **Adjacent, chat 123: §32.6.1 L9290 names three occupied audits — SEQUENCE, PROJECTION, INPUT —
    which R3 should check against §3's numbered rows.**
34. **The arithmetic-convention class (15l-01).** Chat 113 adds L8035; 114 adds 15n-02; 115 adds
    15o-03; 116 adds 16b-03; 117 adds 16d-02; 118 adds the monomial order; 119 adds the closure
    convention; 120 adds 16m-03; 121 adds 16o-02 and five passes; 122 adds twenty-eight passes.
    **Chat 123 adds no member and eleven passes: the six Sc VI figures, the three condition-2
    percentages under Decimal.quantize HALF_UP, and the two E-sums.**
35. **The withdrawn-figure-re-asserted class (15m-01).** 15n-07 is the tighter case. Adjacent, chat
    120: Appendix E's three live item counts. 16o-01 is the inverse. **Chat 123 adds 16r-01 (§32.5's
    *all 153 channels*, against Appendix B's own §B.2 and the spectra arbiter's L900) and 16r-04
    (*figures embedded / captions 18 / 18* against a measured 33 / 33 / 0 unpaired).**
36. **The unbibliographed-attribution class (15m-07).** **The bibliography is `## References`
    L11503–L11855 (R.1–R.7) — the BODY occurrence.** Chat 113's Habib, Nourine and Thierry, chat
    114's Kurucz, VALD, BRASS, Hasse and QSAR, chat 117's NextClosure, chat 118's Roche, Titius,
    Bode, Regge, Hagedorn and Gröbner, chat 119's Klemm, chat 122's Knaster and Tarski. **Chat 123
    adds none: its unit names no authority.** Chat 120's reverse member is **CONFIRMED FROM BOTH
    SIDES**: L11555 and L11799 cite §32.2 for a listing §32.2 does not carry. R3 sweeps every
    attribution in the six volumes against References and R.7, and back.

## Close (chat 124)

`gate.py bank r2-ch16s r2-ch16t`; delete pycache in its own delete-only call; write `W-163.md`
(begins `### W-`, **ends with a blank line** — close.py asserts it, and chat 123 tripped that assert
by ending on a single newline); append a DEFERRED block as `DEF-124.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD152_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD153_compendia_papers_audits.md --w W-163.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-124.md \
  --members members/READ-ch16t.md members/CENSUS-CLOSURES-ch16t.tsv members/r2-ch16s.py \
  members/r2-ch16s.out members/r2-ch16t.py members/r2-ch16t.out
```

It must print **reverse recovers md5 38bd45711e2813dc9b73d8335a306103 == old: True** before writing;
if it does not, nothing is written and the failure is reported. `--append` arguments must precede
`--members`. **A changed append-only member is grown with `--append <member> <delta-file>`, never
passed to `--members`.** After a close, `gate.py manifest` reports FAIL on changed members because
the extracted copies stay at pre-close state; **verify appends by reading the new bundle directly** —
and note the Register member lives in the **main** bundle. `gate.py bank` refuses to overwrite an
existing `.out`; correcting an instrument after banking needs a **delete-only** call first. **An
instrument may be rewritten in place with `str_replace` before it is banked** — chats 110–123
rewrote sixty-four faults that way at no extra cost. Then copy BUILD153, HANDOFF-77 and the READ file
to `/mnt/user-data/outputs` and present them. **Budget the close: begin it with ≥ 8 calls left, and
write the handoff before the final verification, not after.**

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-76.md` and
  `The_Method_1_6_BUILD152_compendia_papers_audits.md`.
- **Retire** once BUILD152 gates PASS in chat 124: HANDOFF-75 and BUILD151, plus any earlier
  compendia builds still present (BUILD107–BUILD150) **except BUILD124**.
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Read those values out of the
  **member** rather than re-running the instrument.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 and required by
  the gate itself, now read by **fifteen** banked instruments — the certificates,
  OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 124

"Chat 124. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD152 compendia (7,146,099 B, md5
38bd45711e2813dc9b73d8335a306103, 94,030 lines, 562 members). List uploads, outputs and /home/claude
first. Run HANDOFF-76's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 564 files), fetch the Prints & Proofs original 'The Method 1.6.md'
(738,550 B, md5 49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md because
fifteen banked instruments read it, then gate.py census, run --core, manifest, run r2-ch16q
r2-ch16r, cert 124; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the
chat-95 block governs and it says a finding is not a question — deviations in the mathematics and in
the prose are recorded and flagged for repair, never put to M, and Prints & Proofs is read before any
question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 123's block is the last
of fifty-one chat blocks (fifty-two ## headings). The standing block's Phase 0–4 Löwdin/three-body
plan is executed carried state; discard it per Ruling 41 — its discard is W-118. Line numbers are
MEMBER line numbers and are never carried between chats, and neither is any count or any heading
list. §32.5 through §32.6.1 are CLOSED: chat 123 closed L9157–L9306. §32.7 opens at L9307 and
# PART VII at L9393. Re-measure by heading scan, resolving each heading to its BODY occurrence —
'## 30.', '## 31.', '## 32.', '## 33.' and '## References' each have two occurrences and taking the
contents one reports every attribution unbibliographed, while Chapters 20 and 21 have only ONE
because their contents entries are plain body lines at L138–L139. The proposed unit is L9307–L9392
(§32.7 alone, 86 lines), which closes chapter 32. Cut it yourself and say which you chose, preferring
the cut that closes a movement, and never split a section read. §32.7 is 'On a verification that does
not test its claim': read it against §32.3 L9045–L9052, because L9328 is the second site of
'twenty-member channel', 'self-duality' and 'involution', so the two accounts of the traced audit
failures must agree. Count every count word against its own body, its DATA rows, its numeral span,
its own body's status markers AND the Register entry that restates it — chat 123 found 'four indices'
printed twice over five terms with register 396 carrying the same 'across the four', and 'thirty-nine
claims … each has been given one' over a table showing seven bare before repair and three after.
Read every cited criterion IN FULL at its target before accepting OR rejecting the conclusion:
chat 123 printed §16.5, §16.3, §6.3, §14.5.6, §E.1.4, §29.2.2, §31.3.4 and Appendix B whole, and
three of ten deviations were visible only in the full text — §16.5 read whole is D3, stating totality
as χ_Λ total on the ambient box, and carries nothing of the bibliographic condition §32.5.3
attributes to it. Re-measure every figure a section computes about the BOOK against the book as it
now stands; chat 123's '18 / 18' figures is now 33 embedded, 33 distinct tags, 0 unpaired. Derive a
table's convention from the book before scoring the table, and find its missing input before calling
a recomputation circular — the Sc VI limit is printed at L6914 (892,700 ± 400 cm⁻¹) and with
δ(4s) = 1.0057 and δ(5s) = 0.9812 from L7004 all six figures reproduce exactly. Never round with
Python's round(); use Decimal.quantize and name the convention. A numeral sweep must match the
printed thousands separator. The volume heads appendices '## Appendix X — …' twice, so
lettered_heading returns None for Appendix B and E — use a body-occurrence resolver; and
heading_line is numeric-only, so §E.1.4 resolves to None though the volume heads it at L10986 —
a lettered pointer needs §([A-Z]\.\d+(?:\.\d+)*). A pointer-site regex must be §N(?!\d)(?!\.\d).
A caption count is not a caption test: pair each embed against a following window. \b(I|my|we|our)\b
matches the Roman numeral in 'He I'. A literal 'Sc VI' probe scores zero in the Spectra Compendium,
which carries Sc rows at L800–L810 — a literal species string is not a species test. Measure the
census rows in range yourself from DEFECT-CENSUS.tsv keyed on the column named member, whose values
are all, ioi, main, mc, pc, reg and sc; sweep classes main AND all; chat 123's range held four, one
of them a defect. Do not re-derive chat 123's findings: the Sc VI table exact at six of six, the
seven display lines of §25.6.1–2, 33 figures all paired, all 36 chapters present with no absent
cross-reference, the condition-2 table exact at every cell and percentage, condition 3 exact at one
genuine hit, 0+16+40+5+4 = 65, and registers 275, 387, 396 and 573 all present and on point with
396's five terms summing to 44 against its printed 43. Register 571 has NO ENTRY and is cited at
L7719 and L9274 — recorded, not re-derived, and never put to M. Then continue Phase R2 under the
chat-81 cadence: read the unit in full, census its claims into computable and prose, then run exactly
two instrument batches, r2-ch16s computable and r2-ch16t prose, importing heading_line, section_span,
has_token, enclosing, Rset, L8_at and is_tree from r2lib — copy nothing, pass them the LINE LIST and
not the member text, read the six volume MEMBERS never a BUILDnnn bundle path, and note that
tower-2.py's L8 is a FUNCTION, so call it, and that L8_at takes (n_max, e_max, l_max, k_max, f_max)
in that order. r2lib.factor_q is a Λ₉ function and cannot be called on 8-tuples. Report numeral SITES
rather than counts, and sweep the word form too. A symbol is tested raw and never transliterated.
has_token is letter-bounded on BOTH sides, so use a left-bounded matcher for a stem, and test a
Ruling 46 token case-sensitively and word-bounded. A colon-terminated lead-in is not a list item.
Anchor every Prints & Proofs witness on its own text — chat 123 measured a uniform −94 at sixteen
witnesses for sixteen. body_range is the resolver for a section body and section_span for a chapter;
resolve every pointer under BOTH before recording an absence, say so when they coincide, and locate
where the claim does live — §14.5.6 is heading-only in BUILD90 and in PP, and the pair it is cited
for lives in register 573. A heading-RANK scan can never end a span. A token probe is not a reading;
where a section is short, print it rather than probe it. An identity entailed by another is not an
independent test. A Register entry restating a count is not independent corroboration of it. Sweep:
every attribution against the BODY occurrence of ## References and against R.7, and the reverse
direction too; every register citation against its entry's headline, grouped-aware and existence
first; every section citing another for a figure the cited section later withdrew. Figure references
are a production layer: the volume has 33 and PP has none, no .png is a member, and an unresolvable
image path is NOT a text defect. The book's present is 2026. Expect the instrument to be wrong before
the book — that fired four times in chat 123, three in 122, six in 121, four in 120. Name the pair
convention before reporting any pair count, the monomial order before any Groebner basis size, and
the closure convention before any E(X). Give every negative claim its own witness and state what a
sweep covered. Record the passes as well as the failures, or a class will look worse than the book
is. Index each volume once rather than rescanning it per phrase. Close the section read before the
next opens. At close: bank both goldens with gate.py bank, write W-163 ending with a blank line,
build BUILD153 with close.py (reverse must recover 38bd4571…), write HANDOFF-77 BEFORE the final
verification, and begin the close with at least eight tool calls left. No corrections, no Register
entries, no TASK 1 until the review closes. Handoff at 90–95% of context or on a closed section read
— never earlier, never mid-section. Timeout on every call. Delete-only calls for pycache, never
chained to any other command. Never copy over an existing file."
