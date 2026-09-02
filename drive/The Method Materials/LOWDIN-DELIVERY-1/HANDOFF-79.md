# HANDOFF-79 — The Method 1.6 — chat 126 → chat 127

- Written from **chat 126** for **chat 127**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD155 compendia** (= BUILD154 + W-165 + DEF-126 + six new members). Register **1 to
  1792** (no Register entry since the chat-67 hold). W-165 IS seated; chat 127 seats nothing at open
  and writes W-166 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still the
  last: **a finding is not a question.** A deviation in the mathematics or in the prose is recorded
  and **flagged for repair**, never put to M. **Prints & Proofs is read before any question is
  asked.** The chat-81 cadence is unchanged: read, census in two kinds, exactly two instrument
  batches, never split a section read.
- **Chapter 34 is HALF CLOSED.** Chat 126 cut **L9494–L9608, 115 lines** — the chapter head, the
  epigraph and §34.1–§34.4 entire, ending where the rule is stated and before it is executed.
  **Main volume now 81.0 % read (L9608 of 11,855).**
- **MEASURED main-volume heading lines, to be re-taken by your own scan:** §34.5 **L9609**, §34.6
  **L9622**, §34.7 **L9634**, §34.8 **L9649**, §34.9 **L9661**, §34.10 **L9673**, and `## 35.` body
  at **L9716**. **Chat 127's unit is L9609–L9715, 107 lines — inside the 74–150 band, one unit, do
  not cut it.** It closes Chapter 34. **Resolve every heading to its BODY occurrence**: `## 34.` and
  `## 35.` have contents hits at **L157** and **L158**; `## References` body is at **L11503** (the
  contents hit at L173 is not it). **Chapters 20 and 21 are the exception:** their contents entries
  are plain body lines at L138–L139.
- **DO NOT RE-DERIVE these, measured in chat 126 inside its own unit:** the ν rule **byte-identical**
  at both printings (L9518, L9583); **5d opens at Z = 57 and 6d at Z = 89**, both recovered from the
  printed sequence and the printed capacity rule 2(2ℓ+1) with no constant supplied by hand; the
  ladder table exact against **Z = Nₑ + c − 1** on all four rows; the Λ_var table exactly **3
  singletons + C(3,2) pairs = 6 DATA rows** with **exactly one** empty pair row; **E = 0**
  corroborated at ioi L1599; Madelung (1936) bibliographed exactly at L11815; §34.6's **eighteen
  resets = 8 + 6 + 4**; **Ruling 46 zero sites**, **first-person zero sites**, **zero unmarked
  sub-headings**; **1 of 56 long lines recurring**, and that one is the epigraph (chat 125's
  16v-06); **PP five headings for five** at −94/−96; the ten scatter figures all corroborated at
  **register L5065**, so none is single-witness; **one census row, disposed as a DEFECT** (row 1195).
- **§34.5–§34.7 WERE PRINTED IN FULL in chat 126** to test L9580's forward pointer, and they use the
  rule. **You still read them in full as your own unit** — that print was a pointer test, not a
  section read, and it censused nothing.
- **THE UNIT'S OWN BIG TEST, already set up:** §34.9 **L9663** reads *Exceptionless on 106 elements,
  Z = 3 to 108*; §34.5 **L9616** reads *All 106 non-empty*; §34.6 **L9629** reads *104 of 106
  steps*. **106 = 108 − 3 + 1 is exact**; chat 126 measured that. But chat 126's **16x-01** shows the
  opening sequence at L9507 needs **Z = 113** for its last member, 7p, against a population the
  chapter caps at 108 at four sites. **Test §34.5's 106, §34.6's 104 of 106 and §34.9's
  exceptionless claim against that same ceiling**, and test **§34.6's 8 subshell openings** against
  the sequence's **19**. Also **L9685's *the domain protocol blocked four fits* against register
  1336's own replay, which records three BLOCKED and two PASS.**
- **CONVENTIONS worth keeping, and two are new.** **Strip the section number from BOTH sides of a
  Prints & Proofs heading comparison** — PP numbers `## 34.` and does **not** number its `###`
  headings, so neither a whole-line nor a one-sided title comparison works (chat 126's fault 4).
  **Print a short cited section rather than probing it** — a ν-token probe scored §34.6 and §34.7 at
  zero and would have condemned a correct pointer (chat 126's fault 3, the third such in four
  chats). A roster or list that **wraps across two lines** must be read on the
  **whitespace-normalised join**. An **unmarked-sub-heading test must require a blank line above**.
  The volume heads appendices **`## Appendix X — …`, twice**, so `lettered_heading` returns None for
  Appendix B and E — use a **body-occurrence appendix resolver**; `heading_line` is **numeric-only**,
  so §E.1.4 resolves to None though the volume heads it at **L10986** — a lettered pointer needs
  **`§([A-Z]\.\d+(?:\.\d+)*)`**. A pointer-site regex must be **`§N(?!\d)(?!\.\d)`**. A caption count
  is not a caption test. **`\b(I|my|we|our)\b` matches the Roman numeral in *He I*** — guard it.
  **A literal species string is not a species test.** **A count word over a table counts DATA rows.**
  **Never split a regex on a comma when the printed form contains one** — chat 126's fault 1 split
  `ν(n,ℓ,q)` at its own argument list and reported a false mismatch.
- **`section_span` CANNOT bound a section that ends a Part** (chat 124's C1). Chat 126's unit had no
  Part-ending section and the two resolvers **coincided at ten of twelve**, differing only at `§34`
  and `§35`, which is resolver semantics on a chapter head carrying subsections, not a defect.
  **Resolve under BOTH, always; say so when they coincide; bound the unit by `body_range`.**
- **The book numbers its principles P1–P23 with P10, P12 and P18 unassigned — twenty in all (L233).**
  Resolve any principle citation to the **P-form**. The language-bounds claim is assigned to **P2**
  at L366 and headed **P20** at L396, while §20.1 L5559 attributes it to P20.
- **Census rows: measure them yourself** from DEFECT-CENSUS.tsv keyed on the column named `member`,
  whose values are `all`, `ioi`, `main`, `mc`, `pc`, `reg`, `sc` — **there is no per-filename
  value**. Columns are `id class member line item detail`. **Sweep classes `main` AND `all`.** Chat
  126's range held **one**, disposed as a **defect** — the first non-artefact disposition in several
  chats, because the flagged token headed a live universal rather than a live figure.
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
  identical in BUILD122–155. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch16x is chat 126's) and W-101…W-165 in
  WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**55 `##` headings — 54 chat blocks plus the verbatim HANDOFF-25 block; chat 126's is the last**)
  governs; do not re-derive.
- **One open scope question, put to M by chat 113 and not yet answered** (a scope choice, not a
  finding, so properly M's): should R2's remaining scope stay a full source-order read of all six
  volumes, or should the five compendia be read against what the transversal sweeps have already
  covered rather than line by line? Measured basis: main volume now **81.0 % read at L9608**, the
  other five volumes 0 % in source order but swept transversally by every batch since chat ~90;
  measured rate ~74–150 main-volume lines per chat. **Do not re-ask it unprompted; carry it.**

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 126. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD155_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths.
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'3ab965257137cead542ea706820a4bbb'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD155_compendia_papers_audits.md'}
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
   **7,387,582 B · `3ab965257137cead542ea706820a4bbb` · 97,672 lines**; **582 members extracted
   (2 + 580)**.
4. **Fetch the Prints & Proofs original before step 7** — twenty-two banked instruments read it and
   will fail on a missing path, `r2-ch16x` among them. Folder
   `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, title `The Method 1.6.md`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977 ·
   11,371 lines**, written to `/home/claude/PP_The_Method_1_6.md`.
5. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 14 s).
6. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
7. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **39,001 B ·
   70641df21f33d49e3e7f5aab176560cf · 582 lines**; WORKING-REGISTER.md **805,823 B ·
   37f27087327409ef295d2fb0fd052c72 · 7,476 lines**, ends **W-165** (166 entries); DEFERRED.md
   **55 `##` headings / 54 chat blocks**; RULINGS-R2.md 9,844 B · 10a2ea7e · 82 lines (unchanged);
   r2lib.py 21,022 B · 580d2ea2 · 453 lines (unchanged); gate.py 9,377 B · a01ef15a;
   close.py 6,456 B · 98acae67; r2-tools.py 6,529 B · 4702f5f9; tower-2.py c0bce27a;
   census.py f5a73e2b; kinds.py 4262f7c5; minmax.py 26da1d78. If two `BUILD*_compendia` files are
   present after a close, pass `--comp <path>` explicitly.
8. `python3 /home/claude/members/gate.py run r2-ch16w r2-ch16x` → two `OK` (chat 126's goldens:
   r2-ch16w.out **22,951 B · e4d1ebb3 · 336 lines**; r2-ch16x.out **11,228 B · 1f9f25cf · 160
   lines**). Both are fast (≈ 1 s and ≈ 3 s); **r2-ch16x reads the Prints & Proofs path**.
9. `python3 /home/claude/members/gate.py cert 127` → writes `/home/claude/GATE-ch127.txt`, verdict
   PASS only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 126 did (do not repeat)

**Unit L9494–L9608 (ch.34 head + epigraph, §34.1–§34.4) read, censused in two kinds (24 computable,
19 prose), instrumented in two batches, closed.** Seven deviations, fifteen verified groups, nine
incidentals, one census row disposed as a defect. All of it is in `READ-ch16x.md` and DEF-126; **do
not re-measure any of it.** The seven deviations:

- **16x-01 — the opening sequence overruns its own population.** L9504/L9592 read it from *the 108
  neutrals*; the sequence's last opening, **7p**, needs **Z = 113** by the unit's own capacity rule.
  Validated on the book's own anchors (5d → 57, 6d → 89, both exact). Present in PP unchanged.
- **16x-02 — *Seventeen of nineteen* needs its convention named.** 15 of 19 position-by-position,
  **17 of 19** by longest common subsequence; the printed **89%** discriminates for the second.
- **16x-03 — Λ_var: eleven in the main volume, TWELVE in the Index of Indices** (ioi L1598), whose
  singleton rule needs **n\***, absent from the main table.
- **16x-04 — the radicand is called a count of states** (L9524) and is a count of **subshells**;
  they differ by 2(2ℓ+1) in 18 of 18 cases.
- **16x-05 — *the provenance of every term is §34.8's table*** (L9596): §34.8's five rows carry no
  row for **q**, zero occurrences.
- **16x-06 — Janet (1929)** at L9600 against **Janet, C. (1928)** at References L11777; 1929 has
  zero sites in the References body.
- **16x-07 — *Both Pauli quantities*** (L9523) names **one**, 2(2ℓ+1), in two roles.

**Instrument faults: four**, all self-caught and rewritten in place, none trimmed. **Twice the book
was right and the instrument wrong** — the ν-token probe on §34.6/§34.7 and the one-sided PP heading
comparator. Running tally: chat 110 five, 111 three, 112 zero, 113 one, 114 one, 115 two, 116 three,
117 four, 118 three, 119 two, 120 four, 121 six, 122 three, 123 nine, 124 zero, 125 three,
**126 four**.

## Chat 127's section read

- **Re-measure the extent by heading scan before reading a line.** The unit is **L9609–L9715, 107
  lines**, §34.5–§34.10, and it **closes Chapter 34**. Do not cut it; do not split it.
- **Sweep the classes chats 107–126 opened:** every count word against its own body, **its DATA
  rows**, **its row labels**, **the numeral span**, **its own body's status markers** **and the
  Register entry that restates it**; every *N of these M* sentence; every list-opening universal
  against **every member of the list it opens**; every withdrawal item describing another section's
  state; every section declaring a defect repaired, re-read against the entry it cites; every
  attribution against `## References` **body occurrence** AND against R.7, **and the reverse
  direction too**; every register citation against its entry's headline, grouped-aware, existence
  first; every printed inequality against the orientation of its own symbols; **every cited criterion
  read in full at its target before its conclusion is accepted**; **every chapter named in a claim
  checked at that chapter and at its neighbours**; and every figure a section computes about the
  BOOK re-measured against the book as it now stands.
- **The unit's own computable claims, sighted but NOT measured by chat 126 — they are yours:**
  §34.5's *All 106 non-empty*, *Nineteen distinct surds*, and the four crossings **0.5773503,
  1.0000000, 1.2168450, 1.3938270** at n = 4 to 7 against **(√(n−1) + √(n−4))/3**; §34.6's
  **eighteen resets = 8 + 6 + 4** (exact, chat 126 checked the arithmetic only) and *104 of 106
  steps admit two to four*; §34.7's **1.028 / 1.785, the ratio √3 to 0.19%**, and the Λ_t p row
  **1.120, 1.049, 1.022, 1.002** with *6p sits 0.2% above*; §34.8's five provenance rows; §34.9's
  *Exceptionless on 106 elements, Z = 3 to 108*; §34.10's account, including **L9685's *the domain
  protocol blocked four fits***.
- **What the docket owes anywhere in the volume**, to test if the unit touches it: docket 5's Ruling
  45 prose sweep (**now one hundred and thirty-three members**); docket 6's Ruling 46 sweep — run 5
  and 6 in one pass, **case-sensitively** (**twenty main-volume sites**, unchanged by chat 126);
  docket 9's pointer sweep, with **§24.6 and §25.6** as magnets; docket 19's false-universal sweep;
  docket 20's absent-member sweep; the duplicated-section sweep (DEF-105 item 1); and the
  placeholder-heading sweep (DEF-107/108/109 item 1, DEF-110 item 12).
- **The channel table remains the arbiter for every species figure.** Section II is spectra-member
  **L293–L934**; its totals line is **L900**: *596 channel rows across 28 elements · 2,269 interior
  cells parsed.* Bound every parse to that span and check it against L900 before trusting one figure.
  **Appendix B's own 153 is the superseded figure — do not use it as a denominator.**

Instruments: **r2-ch16y** (computable) and **r2-ch16z** (prose). Import `heading_line`,
`section_span`, `has_token`, `enclosing`, `Rset`, `L8_at` and `is_tree` from r2lib by path; **copy
nothing**; **read members, never a bundle**; **pass the resolvers the LINE LIST**. Functions still
owed to r2lib and carrying provenance comments in r2-ch16w/x: **`body_range`**,
**`lettered_heading`**, **an appendix body-occurrence resolver**, **a lettered-pointer resolver**,
**`numsites`** (comma-aware), **`regentry`** (grouped-aware), **`joins`**, **`htitle`** (chat 126's
number-stripping heading comparator, needed on BOTH sides of a PP match), an **8-tuple transfer
factorisation** to replace `factor_q`, a **meet-characterisation join-irreducible counter**, and a
**space-aligned table parser that sees a wrapped first column**. Note `T.L8` in tower-2.py is a
**function**: call it, and `L8_at(caps)` takes `(n_max, e_max, l_max, k_max, f_max)` in that order
and returns 8-tuples whose index 1 is ℓ. **`r2lib.factor_q` is a Λ₉ function** and cannot be called
on 8-tuples; for Λ₈ the halves are source (n, ℓ, k, 2S) = 0,1,2,7; transfer q = 3; target
(e, f, g) = 4,5,6.

**Standing method, unchanged and all of it earned:** exact-token heading resolver, never prefix,
resolved to the **body** occurrence; never span a section by heading rank; **never bound a
Part-ending section by `section_span`**; grep lowercase `register NNN` by hand; check every printed
pair count against C(N, 2) and name the denominator; resolve every pointer to the claim and not the
heading, **under both `body_range` and `section_span`**, **and locate where the claim does live**;
test on the **raw** line, case-insensitively, word-bounded, in the word's other forms, left-bounded
for a stem — **raw for a symbol, never transliterated** — and on the whitespace-normalised two-line
join as well as the line. Give every negative claim its own witness and **state what a sweep covered
before recording a negative from it**. Where a section is short, **print it rather than probe it**.
Check the arithmetic of every ratio and percentage; **never round with `round()`** — use
`Decimal.quantize` and name the convention. **State a budget rather than a negative** when a
computation is too large — chat 126 did that for *Raw occupancy makes every one worse*, which needs
§34.5's corridor and §34.6's walk and is therefore **yours to settle**. **Sweep the convention, not
just the base** — a Gröbner basis size is meaningless without its monomial order, a closure size
without one step against fixed point, a surplus without its ambient space, a self-duality count
without the map and the membership test, a combination count without its combination convention
(C(6,2) = 15), and **a sequence-agreement count without its comparison convention** (chat 126's
16x-02). A formula numerator is not a value; a citation is not a declaration; a heading is not a
statement; a bound is not a measurement; a count of headings is not a count of what they contain;
**a token probe is not a reading**; a colon-terminated lead-in is not a list item; **a count word
counts DATA rows**; **a Register entry restating a count is not independent corroboration of it**;
**an identity entailed by another is not an independent test**; **a literal species string is not a
species test**; **a heading missing from Prints & Proofs at its offset may be present there
unnumbered — and the chapter head may be present there NUMBERED**. Where the text prints a sample,
measure the population; **and check the population against its own stated ceiling**, which is how
16x-01 was found. **Match a printed figure at the source's precision, not at yours.** **Grep the
volume and the Register for a later or exact statement before recording any figure as
unreproducible.** **When an instrument disagrees with a hand reading already taken from the file, or
with a totals line the source states about itself, the instrument is wrong until proved otherwise.**

## The repair docket

Carried forward until R3 executes it. **None of these goes to M.** Chat 126's additions are in
DEFERRED's chat-126 block in full; **DEFERRED.md's 55 blocks govern in detail** and the list below
is the standing index, unchanged from HANDOFF-78 except where chat 126 moved it.

1. **§14.5.2–§14.5.7 — six heading-only sections, forty citations. R3's largest single item.**
   MEASURED against Prints & Proofs: **authoring gap, not production loss.** Citations: §14.5.2 → 4,
   §14.5.3 → 1, §14.5.4 → 4, §14.5.5 → 4, §14.5.6 → 3 plus L9281, §14.5.7 → 24. Order: read the
   Register's nine §14.5.7 citations first and author to what they already say, then §21.5.4, then
   the Mathematical Compendium's twelve. Chat 90's **seed(Λ₈) = 7** is the settled material. For
   §14.5.6 the material already exists in **register 573**. **The class outside §14.5 is three:
   §28.7.6 (15i-03), §28.9 (15j-02) and §2.22 (15j-01) — §2.22 is the urgent one.**
2. **The §18.4.1 one-dimensional refinement — a missing Register entry** (main L5977–L5980).
   Register 319, which the passage cites, states a different claim. Chat 118's second member: the
   §18.5 pole correction announced at L8639 has no Register entry at all (16g-08). Adjacent, chat
   124: L9326's *closure is d-dimensional* is the same distinction and its figure has no home.
3. **The Register has no entry for the correction §23.10.2 cites** (14n-A3); §23.10.2 L6455 cites
   *the correction … recorded at 96–98*, printed at §28.7.3 L7582.
4. **The σ collision.** Rule 4 (main L6047) defines σ = 2R Z_eff² · SE_pred / ν³; §22.5 (L6168) uses
   σ as the levels' measured uncertainty, and substituting cancels ν³ identically — MEASURED
   r = 100.000000 at ν = 10, 20, 40, 80. Paired with 14x-04 and 15f-01.
5. **The Ruling 45 class, one hundred and thirty-three members** — HANDOFF-78's one hundred and
   thirty-two plus **chat 126's L9593** (*§34.10 gives the session that did it*), the only
   unambiguous member of its unit's five candidates. **Chat 115 supplies the class's discriminator
   and R3 must apply that split to the whole standing list before repairing any of it.** Captions
   state facts only. Chapter 32 is the densest region measured, at nine sites in 86 lines. **Chat
   126's L9515–L9516 is a POST-PP addition** — the volume gained exactly those two lines against the
   original, which is why the PP offset shifts −94 → −96 inside §34.1. **First-person prose: chats
   113–126 clean inside their units; L4415 is an out-of-unit member.**
6. **The Ruling 46 class — twenty main-volume sites**, five Register sites, 15i-10's Register purpose
   paragraph (L7658–61) and 15j-09's L7852. **Chat 126 adds none.** Register 1336 names
   `domain_protocol.py`, which is permitted in the Register and would not be in a reader-facing
   volume. Run 5 and 6 together, case-sensitively.
7. **RESOLVED AS A FINDING, chat 113 (15m-06).** §23.8.3's affine-invariance reason is at §23.8.3
   L6368; §29.7 L8052 is an attribution row. 15b-07 remains adjacent.
8. **CLOSED as a finding (14z-08).** §23.6 L6319's pointer into §25.6 has no target anywhere.
   15j-08 adds two more failing pointers into §25.6 — **§25.6 is a magnet.**
9. **The pointer class, four-headed.** (a) *Off-by-one and wrong-target pointers*, **forty-five
   members**, including chat 125's 16v-02 and chat 124's 16t-01. (b) **Register or principle
   citations whose target says nothing of the claim** — 15h-09's four, 15i-06's Register 286,
   15l-03's Principle 8, 15m-04's §29.7, 15n-03's registers 253/254, 16j-03, 16j-02, 16m-05, 16o-06,
   16q-04, 16q-05, 16r-03, 16r-10 and 16v-05. (c) **Register citations with no entry at all** —
   15i-09's 571, cited at main L7719 and L9274. (d) **An event with four attributed homes and a
   fifth where it is described** (15j-08 + 15m-05), plus chat 118's §11.7 self-citation at L2260.
   **Chats 117–126 are the class's counter-cases**, ending in chat 125's three-for-five on chapter
   pointers and **chat 126's clean sweep: every one of the unit's twelve pointers resolves, and the
   Register is cited nowhere in the whole of Chapter 34.**
10. **The unprinted-input class, sixty members** — unchanged by chat 126.
11. **The 32/11 scope docket** (14j-01), six measured main sites — L6193, L6213, L6233, L6237,
    L6381, L10245 — plus 2.909 at four. ***4ν/3* is 24 sites across ALL SIX VOLUMES** — main 22,
    mc 1, sc 1; **32/11** has 8.
12. **The truncation-printed-as-equality class** (14l-02/03, 14n-A10, 15b-04, 15d-02, L7308's
    asymptote-as-price, 16d-01, 16g-01, 16j-02, 16m-05). **Chat 126 adds 16x-04**, the radicand
    called a count of states where it counts subshells — the class's definitional form.
13. **The two unsourced counts of L6517** (14n-A6/A7) — *619 refusals* and *§25.5's 1,061 order-1
    bounds*; the recomputation at matched order is still owed. Item 55 (L7507) restates it; chat
    123's 16r-02 is the same figure as a bracket count at L9188.
14. **The main-volume/compendium contradiction class** (14p-19, 14r-01/02/03, 14t-02/07/08, 14v-06,
    14x-05, 14z-03/04/13, 15b-06, 15j-05, 15k-09, 15l-07, 15m-02, 15n-01, 15n-07, 16j-01, 16m-01,
    16m-06, 16o-03, 16o-05, 16o-07, 16q-01, 16q-02, 16r-02, 16r-06, 16r-08, 16v-04, **16x-03**).
    Resolve K I *n*d 45.7 first, then Ne I 16/131 and K I 4/105. **Chat 126's 16x-03 is the second
    member where the compendia settle the main volume**, and the strongest: the Index of Indices'
    twelve variables against the main table's eleven, with the ioi's own singleton rule depending on
    the missing n\*, so the repair direction is fixed — add n\* to the main table.
15. **The retired-basis / narrated-past-state class** (14t-01). *An earlier version* has **8 main
    sites**; *an earlier draft* **7**; *a previous draft* none. R3's sweep must cover all three forms
    and *from recollection* (L8018), *the earlier figure of N* (L8329), *now states* (L8311, L8584,
    L8588, L9240), *the guess that preceded it* (L8293), *the earlier reading* (L8379), *a draft
    withdrew* (L8411), *the withdrawal is withdrawn* (L8412), *it is now discharged* (L8460), *was
    tried first here* (L8470), *what reopened the question* (L8545), *the relation set has grown
    since* (L8584), *the missing Chapter 30* (L8838), the whole *first reading* apparatus of §32.1.1,
    16o-05, 16o-08, L9065, L9271 and L9222. PP prints 1,171 where the volume prints 1,635. **Chat
    125's 16v-03** is the class at its cleanest.
16. **The Edlén dating docket (15l-04, superseding 14r-20).** **1960 at 4 lines** against **1964 at
    25**, listed in DEF-112 item 4. Joined by 15l-05, 15l-07, 15n-05 and 16j-04. Also here: the
    Nesterov name-form sweep (14m-07); *"KI"* without its space at L6657/L6716/L6704; *"neon II"* at
    L6704; 14x-08's *Cooper-type node* at L6896; 15i-12's *detector artifact*. §29.6's four rows
    carry Edlén 1964, Ritz 1908, Paschen & Götze 1922 and Dunz 1911. **Chat 126 adds 16x-06 —
    Janet (1929) in the body against Janet, C. (1928) in the References body, with 1929 carrying
    zero References sites.**
17. **The single-witness class** — HANDOFF-71's list plus chat 118's three (47.9 · 6.9 × 10⁻⁴ ·
    3.6 × 10⁻⁹), chat 122's 2,873 and chat 124's two (−0.00128, −0.00159). **Chat 126 adds none**,
    and supplies a ten-figure counter-case: every one of §34.1's scatter figures is corroborated at
    register L5065. Chat 115's refinement stands: figures recomputed here are not single-witness in
    the strict sense, only the unrecomputable POPULATION COUNTS are.
18. **Heading sentences finishing in the body** (14q-06) — five: L4407, L6582, L8659, L7721, L7856,
    plus the paragraph-scale form at L8325 and the inverse at L8419–L8422. **Chat 126 adds none.**
19. **The false-universal and superlative class** (14v-01, L6970, L7075, 15f-06, 15h-10, 15j-05,
    15l-02, 15m-03, 15n-C4, 15o's L8281 UNMEASURABLE, 16d-03, 16g-05, 16g-06, chat 119's
    unfalsifiable-test form, 16m-06, L9304, 16t-03, 16v's L9486). **Chat 126 adds two: 16x-05**
    (*the provenance of every term is §34.8's table*, where q has no row) **and L9576's *has never
    been traced***, which is the census's own row 1195 and is unmeasurable by sweep — the sweep that
    covered it found *isotopic* at 1 main site, 6 reg, 3 ioi, 1 pc, 0 mc, 0 sc.
20. **The absent-member class** (14v-02, 14x-05, 14z-13, 15b-09, 15m-07, 15n-06). C IV, **Sr at any
    stage**, the sulphur-like sequence, **Rb in six volumes**, three of the four authors of the
    survey cited at L8096, and Kurucz, VALD, BRASS, Hasse and QSAR. MEASURED stage lists: Ca I II IX;
    Ba II III; Ti III XI; Sc III; Hg II; Al I II III IV; Ga I II; Li I II III; **Sr none; Sc VI none;
    Rb none.** Re-measure this class with a **notation-tolerant** probe before repairing any of it.
    **Chat 126's counter-case: lanthanum, cerium, actinium and protactinium all resolve** by name and
    symbol across the volumes, 6–19 Register sites each.
21. **The end-rule overstatement** (14v-07) — §24.13's L6877/L6879; 15f-03 runs the other way;
    15g-09, 15h-08, 15h-12 (CLOSED as 16g-03); 15i-04/05; 15j-06; 15k-05/06; 15l-02; 15m-08; 15o-01;
    16b-01/02; 16d-04; 16g-02/04; 16j-01; 16j-05 (**CLOSED, chat 123**); 16m-02; 16o-03. Sweep all
    twenty-three.
22. **The census anchor** (14v-08) — §24.12 must state which member of a sequence D is computed on,
    and print the census's range (27 + 12 + 5 = 44 sequences).
23. **The caption-corrected-but-not-the-prose class** (14x-02), at section scale (14z-01),
    cross-volume (15b-06), Register-scale (15d-05, 15f-07), twice in chat 107, at register-citation
    scale in 15h-09, at repair-declaration scale in 15i-06/07, at repair-execution scale in 15k-07,
    cross-volume in 15l-04/05, at CHAPTER scale in 15m-01, at CORRECTION scale in 16g-08, at APPENDIX
    scale in 16m-06, and at TWIN-SITE scale in 16v-01. Negative witnesses: App D.5.2 L10575, Figure
    23.1 → 30.1, PP's *Figure 23.2* → **Figure 30.2**, §31.2.2's correction registered at 1787, chat
    119's register 387, chat 120's registers 424–426, chat 121's twenty-for-twenty, chat 122's
    five-for-five, chat 123's four-for-four. **The largest live class after item 1.**
24. **Two compendium data defects** (14x-09/10): spectra **L562**'s malformed `n 41–5` (read 41–55),
    and **nine duplicated (species, series) keys over 18 rows**.
25. **The inherited-estimate class** (14z-02) — sweep every bracket for an edge tracing back to an
    estimate. Adjacent: §25.6.1 L7019's *the limit's own ±400 to be added at both edges*, and
    §32.5.1's table carrying no such caution.
26. **The spliced-text class** (15b-01/02) — main **L7156**; 15f-08's L7405–07; 15h-13's L7621–23;
    chat 116's L8401; chat 117's L8564–L8565; 16o-07's L8908–L8912; chat 125's **16v-06**.
    **Chat 126 supplies 16v-06's PP witness and it changes the repair:** PP carries BOTH copies, at
    **P9396–P9398** (Part frame) and **P9402–P9404** (chapter frame). They are two frames sharing a
    126-character prefix, present in the original, **not a splice** — R3 rewords the shared opening
    rather than deleting a copy.
27. **The duplicated-section class (15d-01).** §9.2 L1961–L1990 and §27.5.1 L7299–L7330 are one
    passage with two Register entries, 438 and 446. **Chats 106–126 ran the sweep on their own units:
    0 of 71, 55, 32, 44, 70, 38, 51, 76, 75, 53, 65, 67, 47, 70, 95, 45, 57, 36, 46 and 56 long lines
    recur — twenty consecutive clean units** (chat 126's single recurrence is the epigraph, item 26).
28. **Table and heading formatting (15d-04)** — four of Chapter 27's five tables are space-aligned
    and §27.1's is shattered mid-word, in PP too; 15f-09's thirty lower-case section openings;
    §28.6's header shattered at L7462–64; 15j-12's four-class table printing its header twice;
    15k's attribution continuations; §29.7 as two blocks; chat 116's L8421; chat 117's step-law
    table; chat 120's §32.1.1 E(book) table; chat 121's §32.1.4 and §32.1.3 tables; chat 122's
    recursion table and both §32.4.2 tables; chat 123's contents entries for Chapters 20 and 21
    (L138–L139) and §31.3.4's sub-headings numbered 24.3.4.1/2/3 at L8738, L8755, L8777; chat 124's
    two unmarked sub-headings L9338 and L9367 and the principles table header shattered mid-word at
    L243–L244. **Chats 125 and 126 add none** — the unit's two tables are well formed and its
    headings are all marked. One formatting pass.
29. **Section order (15f-05). MEASURED AND CLOSED AS A FINDING in chat 111.** Adjacent and already
    closed in chat 80: §12.11.8's heading at **L3543**, outside Chapter 12's body span and after
    `## 13.` opens at L3508.
30. **The Register's own size (15f-02), five figures over twenty-three sites.** **1,635** in words at
    **fifteen** main sites and absent from PP — **PP prints 1,171**; **1,635** in digits at main
    **L7373** and reg L6, L65, L6127, L6133; **1,631** at main L7658; **1,628** bare headings at reg
    L6109, L6115. **MEASURED, chat 124: 1,635 numeral headings = 1,628 bare + 7 grouped; 1,660
    distinct entry numbers; maximum 1792.** Adjacent: the front matter's *571 entries are cited by
    other entries* against `register_cites.py`'s **593**; 16o-04; 16q-02. **Referent drift is the
    live part:** L202, L7367 and L7900 fix *withdrawn claims* as canonical; **chat 122's L9055
    remains the single outlier.**
31. **The item-numbering class (15g-01, 15h-06/07, 15i-01/02/04/05, 15j-03/04, 15k-09, DEF-107 item
    7, 16j-06).** MEASURED in chat 110: chapter 28 prints **41 item lines, 17 of them heading a
    range, covering 104 distinct numerals to a maximum of 164**, with **59 printed twice** and **60
    numerals below the maximum never covered**; against L7780's *319 entries*, **155 numerals above
    164 are never printed at all**. R3 repairs the chapter-28 part in **one numbering pass**.
32. **The placeholder-heading class (DEF-107/108/109 item 1, DEF-110 item 12).** PP prints §28.7.2,
    §28.7.3 and §28.7.4 with placeholder headings where the volume prints *Twelve more*, *Seventy-
    five more* and *Forty more*. §28.7.7's *119* is in PP already. §28.9.1's PP heading reads *From
    registers…* where the volume reads *Two registers…*. 16j-06 belongs here too. **The benign form
    must not be confused with these: PP carries §33's five headings UNNUMBERED where the volume
    numbers them, and chat 126 adds the other half of that datum — PP DOES number the chapter head
    `## 34.`. Numbering is a production layer in both directions.**
33. **The §3 audit numbering (15i-08).** §3 prints numbered rows **1–7**, names twelve more at
    L1024–25, and states *twenty-two audits*; §2.19.1 cites *audit 15 ENUMERATION*, §28.7.5 cites an
    *exhaustiveness clause* that appears nowhere in §3, §28.10 L8234 cites *part 2 of the audit*.
    15l-03 is the same shape for the principles; 16j-05 for the falsification tests (CLOSED); 16m-02
    for the referee flags; 16o-08; 16q-01; 16r-06; 16t-02; chat 125's P2/P20 duplication. **Chat 126
    adds 16x-07**, a count word promising two and naming one.
34. **The arithmetic-convention class (15l-01).** Chat 113 adds L8035; 114 adds 15n-02; 115 adds
    15o-03; 116 adds 16b-03; 117 adds 16d-02; 118 adds the monomial order; 119 adds the closure
    convention; 120 adds 16m-03; 121 adds 16o-02 and five passes; 122 adds twenty-eight passes; 123
    adds eleven passes; 124 adds the self-duality map-and-membership convention; 125 adds §20.2's
    C(6,2) = 15. **Chat 126 adds 16x-02**, where the comparison convention decides between exact and
    false, and the printed 89% settles which the book means.
35. **The withdrawn-figure-re-asserted class (15m-01).** 15n-07 is the tighter case. Adjacent, chat
    120: Appendix E's three live item counts. 16o-01 is the inverse; 16r-01 and 16r-04 are chat
    123's; 16v-03 is its near neighbour. **Chat 126 adds none.**
36. **The unbibliographed-attribution class (15m-07).** **The bibliography is `## References`
    L11503–L11855 (R.1–R.7, R.7 at L11806) — the BODY occurrence.** Chat 113's Habib, Nourine and
    Thierry, chat 114's Kurucz, VALD, BRASS, Hasse and QSAR, chat 117's NextClosure, chat 118's
    Roche, Titius, Bode, Regge, Hagedorn and Gröbner, chat 119's Klemm, chat 122's Knaster and
    Tarski, chat 125's Schrödinger and Demkov–Ostrovsky. **Chat 126 adds Klechkovskii** — named at
    L9600 as one of the three owners of the n+ℓ rule, the other two both bibliographed — **and
    Pauli**, used adjectivally at L9523, L9527 and L9587. Chat 124's counter-case stands as the
    class's largest: eleven authorities named in 86 lines, every one present. Chat 120's reverse
    member is CONFIRMED FROM BOTH SIDES: L11555 and L11799 cite §32.2 for a listing it does not
    carry. R3 sweeps every attribution in the six volumes against References and R.7, and back.

## Close (chat 127)

`gate.py bank r2-ch16y r2-ch16z`; delete pycache in its own delete-only call; write `W-166.md`
(begins `### W-`, **ends with a blank line** — close.py asserts it); append a DEFERRED block as
`DEF-127.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD155_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD156_compendia_papers_audits.md --w W-166.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-127.md \
  --members members/READ-ch16z.md members/CENSUS-CLOSURES-ch16z.tsv members/r2-ch16y.py \
  members/r2-ch16y.out members/r2-ch16z.py members/r2-ch16z.out
```

It must print **reverse recovers md5 3ab965257137cead542ea706820a4bbb == old: True** before writing;
if it does not, nothing is written and the failure is reported. `--append` arguments must precede
`--members`. **A changed append-only member is grown with `--append <member> <delta-file>`, never
passed to `--members`.** After a close, `gate.py manifest` reports FAIL on changed members because
the extracted copies stay at pre-close state; **verify appends by reading the new bundle directly** —
and note the Register member lives in the **main** bundle. `gate.py bank` refuses to overwrite an
existing `.out`; correcting an instrument after banking needs a **delete-only** call first. **An
instrument may be rewritten or extended in place with `str_replace` before it is banked** — chats
110–126 did that seventy-one times at no extra cost, and chat 126 used it four times to repair the
four faults named above. Then copy BUILD156, HANDOFF-80 and the READ file to `/mnt/user-data/outputs`
and present them. **Budget the close: begin it with ≥ 8 calls left, and write the handoff before the
final verification, not after.**

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-79.md` and
  `The_Method_1_6_BUILD155_compendia_papers_audits.md`.
- **Retire** once BUILD155 gates PASS in chat 127: HANDOFF-78 and BUILD154, plus any earlier
  compendia builds still present (BUILD107–BUILD153) **except BUILD124**.
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Read those values out of the
  **member** rather than re-running the instrument.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 and required
  by the gate itself, now read by **twenty-two** banked instruments (MEASURED) — the certificates,
  OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 127

"Chat 127. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD155 compendia (7,387,582 B, md5
3ab965257137cead542ea706820a4bbb, 97,672 lines, 580 members). List uploads, outputs and /home/claude
first. Run HANDOFF-79's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 582 files), fetch the Prints & Proofs original 'The Method 1.6.md'
(738,550 B, md5 49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md because
twenty-two banked instruments read it, then gate.py census, run --core, manifest, run r2-ch16w
r2-ch16x, cert 127; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the
chat-95 block governs and it says a finding is not a question — deviations in the mathematics and in
the prose are recorded and flagged for repair, never put to M, and Prints & Proofs is read before any
question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 126's block is the last
of fifty-four chat blocks (fifty-five ## headings). The standing block's Phase 0–4 Löwdin/three-body
plan is executed carried state; discard it per Ruling 41 — its discard is W-118. Line numbers are
MEMBER line numbers and are never carried between chats, and neither is any count or any heading
list. Chapter 34 is half closed: chat 126 cut L9494–L9608, the chapter head and epigraph plus
§34.1–§34.4 entire. Your unit is L9609–L9715, §34.5 to §34.10, 107 lines — inside the band, one unit,
do not cut it and do not split it; it closes Chapter 34, and '## 35.' body opens at L9716. Take the
heading lines by your own scan, resolving each to its BODY occurrence ('## 34.' and '## 35.' have
contents hits at L157 and L158). Resolve every pointer under BOTH body_range and section_span and say
so when they coincide — chat 126's twelve coincided at ten, differing only at §34 and §35, which is
resolver semantics on a chapter head with subsections and not a defect — and bound the unit by
body_range. Read every cited criterion IN FULL at its target before accepting OR rejecting the
conclusion, and PRINT a short cited section rather than probing it: a ν-token probe scored §34.6 and
§34.7 at zero occurrences in chat 126 and would have condemned a correct pointer. Measure the unit's
computable claims yourself: §34.5's 'All 106 non-empty', 'Nineteen distinct surds', and the four
crossings 0.5773503, 1.0000000, 1.2168450, 1.3938270 at n = 4 to 7 against (√(n−1) + √(n−4))/3;
§34.6's eighteen resets as 8 + 6 + 4 and its '104 of 106 steps'; §34.7's 1.028 and 1.785 with the
ratio √3 to 0.19%, and the Λ_t p row 1.120, 1.049, 1.022, 1.002 with '6p sits 0.2% above'; §34.8's
five provenance rows; §34.9's 'Exceptionless on 106 elements, Z = 3 to 108'. Test every one of those
populations against the chapter's own ceiling: chat 126's 16x-01 measured that the opening sequence
at L9507 needs Z = 113 for its last member, 7p, while the chapter caps its population at 108 at four
sites, and that §34.6's 8 subshell openings sits against the sequence's 19. Test L9685's 'the domain
protocol blocked four fits' against register 1336's own replay, which records three BLOCKED and two
PASS. Also settle what chat 126 could only budget: 'Raw occupancy makes every one worse' (L9530)
needs §34.5's corridor and §34.6's walk, both in your unit. Do not re-derive chat 126's findings: the
ν rule byte-identical at both printings, 5d at Z = 57 and 6d at Z = 89 from the printed sequence and
capacity rule, the ladder table exact against Z = Nₑ + c − 1 on all four rows, the Λ_var table as 3
singletons plus C(3,2) pairs with exactly one empty pair row, E = 0 corroborated at ioi L1599,
Madelung (1936) bibliographed at L11815, PP five headings for five at −94/−96, 1 of 56 long lines
recurring, and zero Ruling 46 sites, zero first-person sites and zero unmarked sub-headings. Grep the
Register for a later or exact statement before recording any figure as unreproducible, and check
whether a later entry SUPERSEDED the figure the text still prints. Read every roster or list on the
whitespace-normalised JOIN of its lines. When comparing a heading to Prints & Proofs, strip the
section number from BOTH sides: PP numbers '## 34.' and does not number its '###' headings, and a
one-sided comparator reported the chapter head absent in chat 126. An unmarked-sub-heading test must
require a blank line above. Count every count word against its own DATA rows, its numeral span, its
own body's status markers AND the Register entry that restates it. Name the convention before scoring
any figure — a sequence-agreement count needs its comparison convention, a combination count needs
C(6,2) = 15. Never round with Python's round(); use Decimal.quantize and name the convention. Never
split a regex on a comma when the printed form contains one — that truncated ν(n,ℓ,q) at its own
argument list in chat 126. A numeral sweep must match the printed thousands separator and the word
form too. The volume heads appendices '## Appendix X — …' twice, so lettered_heading returns None for
Appendix B and E — use a body-occurrence resolver; heading_line is numeric-only, so §E.1.4 resolves
to None though the volume heads it at L10986 — a lettered pointer needs §([A-Z]\.\d+(?:\.\d+)*). A
pointer-site regex must be §N(?!\d)(?!\.\d). A caption count is not a caption test. \b(I|my|we|our)\b
matches the Roman numeral in 'He I'. A literal species string is not a species test. Measure the
census rows in range yourself from DEFECT-CENSUS.tsv keyed on the column named member, whose values
are all, ioi, main, mc, pc, reg and sc; sweep classes main AND all; chat 126's range held one,
disposed as a DEFECT because the flagged token headed a live universal. Then continue Phase R2 under
the chat-81 cadence: read the unit in full, census its claims into computable and prose, then run
exactly two instrument batches, r2-ch16y computable and r2-ch16z prose, importing heading_line,
section_span, has_token, enclosing, Rset, L8_at and is_tree from r2lib — copy nothing, pass them the
LINE LIST and not the member text, read the six volume MEMBERS never a BUILDnnn bundle path, and note
that tower-2.py's L8 is a FUNCTION, so call it, and that L8_at takes (n_max, e_max, l_max, k_max,
f_max) in that order. r2lib.factor_q is a Λ₉ function and cannot be called on 8-tuples. Report numeral
SITES rather than counts. A symbol is tested raw and never transliterated. has_token is
letter-bounded on BOTH sides, so use a left-bounded matcher for a stem, and test a Ruling 46 token
case-sensitively and word-bounded. A colon-terminated lead-in is not a list item. Anchor every Prints
& Proofs witness on its own text. A heading-RANK scan can never end a span. An identity entailed by
another is not an independent test. A Register entry restating a count is not independent
corroboration of it. Sweep: every attribution against the BODY occurrence of ## References and
against R.7, and the reverse direction too; every register citation against its entry's headline,
grouped-aware and existence first; every section citing another for a figure the cited section later
withdrew. Figure references are a production layer: the volume has 33 and PP has none, no .png is a
member, and an unresolvable image path is NOT a text defect. The book's present is 2026. Expect the
instrument to be wrong before the book — that fired twice in chat 126, twice in 125, zero times in
124, four in 123. Give every negative claim its own witness and state what a sweep covered. Record
the passes as well as the failures, or a class will look worse than the book is. Index each volume
once rather than rescanning it per phrase. Close the section read before the next opens. At close:
bank both goldens with gate.py bank, write W-166 ending with a blank line, build BUILD156 with
close.py (reverse must recover 3ab96525…), write HANDOFF-80 BEFORE the final verification, and begin
the close with at least eight tool calls left. No corrections, no Register entries, no TASK 1 until
the review closes. Handoff at 90–95% of context or on a closed section read — never earlier, never
mid-section. Timeout on every call. Delete-only calls for pycache, never chained to any other
command. Never copy over an existing file."
