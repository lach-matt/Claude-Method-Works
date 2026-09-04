# THE METHOD 1.6 — HANDOFF (chat 30 → chat 31), 2026-08-26
Chat: 30. Build described: BUILD-31. Register range: 165–1777.
Those three agree with the files. Register: **1,456 entry headings · 1,481 numbers (all distinct) ·
7 grouped headings · 4 non-numeric front-matter subheads · `wc -l` 5,896, terminal byte `0x29`**.
**THE REGISTER DID NOT MOVE THIS CHAT. NO ENTRY WAS ADDED. ONE VOLUME CHANGED — SPECTRA — AND THE CHANGE
IS EDITORIAL UNDER RULING 43, SO IT IS RECORDED IN `WORKING-REGISTER.md` AND NOT IN THE REGISTER.**
**ONE INSTRUMENT WAS EDITED: `coords.py`, repaired at four sites. `WORKING-REGISTER.md` 2,633 → 2,747.**
**RULING 56 WAS ISSUED THIS CHAT. Rulings 1–56 plus the R27 Amendment are in force.**
**ONE QUEUE ITEM BUILT: B7. B8–B12 NOT STARTED.**

## 0. THE READING GATE — EXECUTE BEFORE ANY OTHER WORK. NO EXCEPTIONS.

  **G0  A MESSAGE CONTAINING A QUESTION ENDS AT THE QUESTION MARK.** Ruling 47. Count the `?`; nothing
      may follow the last one except the sentence it terminates. **HELD AT CHAT 30 — three sessions
      clean.** It stays at G0.
  **G0b A DEFECT LINE AND ITS DISPOSITION ARE DIFFERENT OBJECTS. THE LATER LINE GOVERNS, AND THE
      DISPOSITION ITSELF CAN BE STALE.** Read the highest hit, then check whether a later ruling has cut
      the ground from under it. **SHARPENED AT CHAT 30 BY W-034: a handoff figure is measured at a
      MOMENT, and work done after that moment invalidates it silently — HANDOFF-31's own Register line
      count was one entry stale.** So the second half now reads: do not re-derive what a handoff reports
      measured, but if the gate's own measurement disagrees, the FILE wins and the handoff is corrected.
  **G0c A SHORTER STRING MATCHES INSIDE A LONGER ONE. GUARD EVERY PROBE WHOSE TARGET IS A PREFIX OF ITS
      OWN REPAIR.** **IT EARNED ITS PLACE AT CHAT 30 AND CAUGHT A FALSE REPORT IN ADVANCE:** counting
      Spectra's species cell raw gives 105 species, because `Ca IX *` and `Ca IX` count as two. The
      asterisk is a mark on a ROW, not part of a NAME. Correct census: 70.
  **G0d NEW, AND IT IS THE MOST EXPENSIVE FAULT THIS CHAT: A HEADING LEVEL IS A SERIALIZATION.**
      `coords.py` locates sections by the literal `### `. **Ruling 49 promoted Spectra's level-3 headings
      to level 2 at chat 28 and killed two of the gate's four checks instantly; no press ran at chat 29,
      so it went undetected for a whole build.** Same fault as W-013's `<w:sectPr />`. **THE STANDING
      RULE: AFTER ANY RULING THAT CHANGES STRUCTURE — HEADING LEVELS, HEADING NAMES, PART NUMBERING —
      RE-RUN EVERY GATE BEFORE THE BUILD IS DECLARED CURRENT.**
  **G0e NEW, AND IT UNDERMINES A METHOD THIS PROJECT HAS RELIED ON SINCE CHAT 8: `pdftotext` OUTPUT IS
      NOT THE PAGE.** SPEC-12 — 51 rows present and correct in the `.docx` extract as ZERO rows from the
      PDF's text layer. **ABSENCE IN `pdftotext` HAS NEVER BEEN EVIDENCE OF ABSENCE ON THE PAGE.**
      Confirm a suspected omission against `word/document.xml` before reporting it.

  G1  `recent_chats n=20`; again with `before=`. **30 CHATS AT CHAT 31**: Rebuild 1–12, 13–19, 21–30,
      plus one unnumbered ("Extract transitions from file"). **THERE IS NO CHAT 20.** n=20 stopped at
      **Rebuild 10** at chat 30; expect **Rebuild 11**. MEASURE; DO NOT RECITE.
  G2  Split both BUILD-31 bundles with `split.py`. **IT IS A BUNDLE MEMBER, SO BOOTSTRAP IT FIRST:**
      one regex pass over bundle 2 pulling only `bundle.py` and `split.py` (they are a pair), then
      `python3 split.py <b1> <b2> -o /home/claude/build`. It prints declared · paired · spurious ·
      re-assembly and **exits nonzero if re-assembly is not byte-exact**. **THE HANDOFF IS A MEMBER OF
      THE BUILD IT DESCRIBES.** If a bundle looks absent, RE-LIST; /mnt/project syncs late.
  G3  Read `WORKING-REGISTER.md`. **`wc -l` RETURNS 2747 AND THE FILE ENDS WITH A NEWLINE.** VERIFY.
      `sed -n 'a,bp'` is cheaper than `view`. It carries **RULINGS 27, 28, the R27 Amendment, 29–56**
      and **W-001…W-036 plus SPEC-12**.
      **RULING HEADING LINES, MEASURED THIS CHAT — USE THEM, DO NOT RE-INDEX:** 27 at 4, 28 at 11,
      Amendment at 19, **29 at 736 and 30 at 785 (BOLD INLINE, not `###`)**, 31 at 837 and 884, 32 at
      903, 33 at 943, 34 at 974, 35 at 987, 36 at 994, 37 at 1001, 38 at 1217, 39 at 1420,
      **40 at 1619 (the tower held entire — the GENUINE one)**, 41 at 1734, 42 at 1755, 43 at 2019,
      44 at 2024, 45 at 2038, 46 at 2052, 47 at 2108, 48 at 2146, 49 at 2175, 50 at 2190, 51 at 2229,
      **52 at 2286 — DEAD, read 55 with it**, 53 at 2319, 54 at 2363, **55 at 2570**, **56 at 2635**.
      **SEARCH RULINGS CASE-INSENSITIVELY. `W-015` MATCHES INSIDE `W-015a`.**
  G4  PRINT THE CERTIFICATE. Until it prints, state NOTHING about the work, change NO file.
      CERT: chats read = N/__ · bundle members = ___ + ___ · rulings = 1–56 + amendment
            · Register entry headings = ____ · Register numbers = ____ · instruments = ____
            · **G0 · G0b · G0c · G0d · G0e acknowledged**
  G5  VERIFY BUILD IDENTITY, NOT SIZE. **THIS BUILD'S DISCRIMINATORS, ONE PER TREE:**
      `grep -c 'SPEC-12' WORKING-REGISTER.md` (**2**, was 0) and — **A VOLUME DISCRIMINATOR, WHICH IS
      THE ONE THAT MATTERS** — `grep -n '^\*He II' <Spectra>` returns **573** (was **344** at BUILD-30).
      **Stop only if a VOLUME disagrees.** A working-register value merely larger than predicted is this
      handoff's own closing block.
  G6  **CHECK THE TOOL EXISTS BEFORE TRUSTING ITS SILENCE.** `xxd` IS NOT INSTALLED — re-verified chat
      30. Use `od -An -tx1`.
  G7  **A REIMPLEMENTATION THAT DISAGREES WITH AN INSTRUMENT IS THE THING THAT IS WRONG.** Import the
      instrument's own functions. **APPLIED AT CHAT 30 IN ITS OTHER DIRECTION TOO: when my census
      disagreed with SPEC-06's recorded one, the RECORD was right and my measurement was the artefact.**
  G8  **A QUESTION YOU CAN ANSWER BY READING IS NOT A STANDING QUESTION.** Grep the term across all six
      volumes, read the enclosing section whole, read the cited entries.
  Failure mode: any count RECITED from a prompt rather than READ from a file = gate not passed.

**RECONCILIATIONS — MEASURE THEM, DO NOT CARRY THEM.**
  - **THE "EVERY FILE ENDS WITHOUT A NEWLINE" RULE IS FALSE.** Measure the terminal byte per file.
    **The Register's is `0x29`. `WORKING-REGISTER.md` DOES end with a newline. Spectra's is `0x2e`.**
  - The Register measures `wc -l` **5,896** — **HANDOFF-31 SAID 5,894 AND WAS ONE ENTRY STALE (W-034).**
  - Register 1,460 `### ` lines − 4 front-matter subheads = 1,456 entry headings, 1,481 numbers.
    NOT the 1,447/1,472 question held at PR1; untouched, still held.
  - **Spectra is 1,032 lines and 84,467 bytes BEFORE AND AFTER B7.** The reorder is length-neutral.

**THE FALSE STATE — RULING 41 EXPLAINS IT; DO NOT REFUTE IT.** Ruling 40-about-F.4.2, BUILD-25,
`regsize.py`, `ratios.py`, `pageproof.py`, `RESTORE-PACKS.md`, Register ~1,787, an eight-volume
deliverable. **IT ARRIVED AGAIN AT CHAT 30 THROUGH CARRIED MEMORY** — tenth consecutive session, still
the only channel. Expect it; record it; proceed on the files. **THIS HANDOFF IS GENUINELY NUMBERED 32.**

## 1. INSTRUMENTS — 24 .py. NONE ADDED OR REMOVED. ONE EDITED: `coords.py`.

`appf.py bookindex.py build.py bundle.py channels_LIMB.py coords.py crop_titles.py dclose.py depoint.py
excise.py fig_rerender.py heii.py index_gen.py index_pages.py kinds.py qgraph.py rclose.py
register_cites.py ruled_bracket.py run489.py spectra_count.py split.py tb_audit.py trueres.py`

**RULING 41 CLOSES THE MISSING-INSTRUMENT QUESTION PERMANENTLY.** guard.py, press_all.py, mkref.py,
figs.py, pageproof.py, ratios.py, regsize.py, indices.py, mathreg.py, mathverify.py, compendium.py,
store_gen.py, RESTORE-PACKS.md lived in deleted chats and are NOT recoverable. Do not search Drive. Do
not ask the author. `appf.py` is RETIRED — dead code, do not call it. **guard.py DOES NOT EXIST**; its
function is md5 of the tree against a pristine re-split of the previous build with `split.py`.
**DO NOT REBUILD ANY INSTRUMENT. Ruling 54 is spent. `coords.py` was REPAIRED, not rebuilt — same class
as chat 28's prefix repair to the same file.**

**ref.docx — NOT A BUNDLE MEMBER. Rebuild every session that presses**, on W-013's corrected recipe
(~WORKING-REGISTER line 1549). **REBUILT AND VERIFIED IN THE OBJECT THIS CHAT: pandoc's default here
carries 36 theme attributes and 3 plain — NOT W-013's 48** (the handoff predicted 36/3 and was right);
convert all to literal Georgia; docDefaults already carries `sz` 24 so **REPLACE it with 21, never
insert**; add `EntryBody`; match `sectPr` **BY ELEMENT NAME** — it serialises `<w:sectPr />`, with a
space — and set 12240×15840 with six 1440 margins. Verified: 0 non-Georgia font attrs · 0 theme attrs ·
one sz at 21 · EntryBody present · pgSz and six margins correct · zip clean · 9,773 bytes.

**FIGURES — NOT bundle members, refetch each session that presses. FETCHED AND VERIFIED THIS CHAT.**
`The_Method_1_6_figures_BUILD13.zip`, Drive `1q7pvnxMPILD9AVoH6XjymZHXX79YzITd`, **6,299,293 bytes**,
sha256 prefix `ee423b9ca550a94e7fe0baa41f6ef032`, md5 `78888f2078dc5342ab221a59bbcf8921`.
Unzip into `/home/claude/build/`: `figures/` **49**, `figures-compendia/` **12**. All three hashes and
both counts matched exactly.

**THE DRIVE LARGE-FILE PATH IS PROVEN AND RAN AGAIN THIS CHAT.** Over ~1 MB the result is written to
`/mnt/user-data/tool_results/<tool_call_id>.json`. Decode:
`d=json.load(open(p)); inner=json.loads(d[0]['text']); blob=base64.b64decode(inner['content'])`
then verify against the Drive `fileSize`. `pdftotext`, `pdfinfo`, `soffice`, `pandoc`, `python-docx`
all present. **`xxd` is NOT.**

**COORDINATES-2.13 — SUPPLIED, DO NOT ASK AGAIN.** `/mnt/project/COORDINATES-2_13.csv`, 10,912,381
bytes; the connector refuses it (10 MB cap). Not a bundle member. `coords.py` reaches `/mnt/project/`
directly and gates Spectra inside `build.py`. 104,832 rows; grade exact 929 · measured 358 · computed
103,545; witness 358 · 104,474; bound 22 distinct, 21 printed rows summing to 104,499; 25 witnessed
cells also bounded. **ALL RE-VERIFIED THIS CHAT AFTER THE REPAIR — THE GATE RETURNS PASS.**

**PRESS INVOCATIONS.** The digit is LAST in argv; it is `index_pages.py`'s DEPTH.
**`build.py` PREFIXES ITS OWN BASE DIR — pass a bare filename, never an absolute path.**
  main      `python3 build.py The_Method_1_6-2.md OUT/main.docx "The Method 1.6" strip pages 2`
  Register  `python3 build.py ...The_Register-2.md OUT/register.docx "... — The Register" fix 0`
            **NO `pages`. RULING 38. SETTLED TWICE — do not re-derive it a third time.**
  math/phys/ioi/spectra  `python3 build.py <src> OUT/<x>.docx "<title>" pages 2`
  Register afterwards: `soffice --headless --convert-to pdf --outdir OUT OUT/register.docx`
  **`index_pages.py` admits `len(hashes) <= DEPTH+1`, so at DEPTH 2 the Contents ALREADY carries
  level-3 headings.**

## 2. WHAT WAS BUILT THIS CHAT — B7, ONE INSTRUMENT REPAIR, ONE RULING RECEIVED

**RULING 56 (author, chat 30, verbatim): "Something very important for you as you build this index, or
any index that is connected to the lowdin work. The lowdin solution is true and accurate, at least the
original input at the project's start is. It can be used to verify the accuracy of the indecies
currently being built."** Recorded at WORKING-REGISTER L2635.
**IT SUPPLIES AN EXTERNAL CHECK WHERE THE PROJECT HAS HAD ONLY INTERNAL CONSISTENCY.** A disagreement
between an index and the Löwdin solution is now a finding ABOUT THE INDEX, not a tie.
**THE SCOPE QUESTION IS OPEN AND IT IS THE FIRST THING CHAT 31 MUST SETTLE, BY READING:** the ruling
names *"the original input at the project's start"*, **not** the absorbed Chapter 35 (registers
1701–1712), which has been edited since. Candidates in reach are `THE-LOWDIN-SOLUTION-2.md` (bundle
member, edited through every press) and **the BUILD-12 bundles still sitting in /mnt/project**.
**THEREFORE: DO NOT RETIRE THE BUILD-12 BUNDLES. They have been listed for retirement since chat 13 and
never retired, and they may be the only copy of the original input in reach.**
**NOT STARTED, DELIBERATELY — the ruling arrived at the handoff threshold**, and opening a verification
pass against a source whose identity is not established would be the wrong first move.

**B7 — SPEC-06'S REORDER, BUILT AND VERIFIED ON THE PRESSED OBJECT. W-035.**
  **596 rows · 92 runs → 70, one per species · 70 species · 28 elements.** SPEC-06's recorded census
  reproduced exactly; **my first measurement (137/105/28) was the artefact**, caught by G0c.
  **Method: a STABLE MERGE**, because 50 of 90 multi-row runs violate levels-descending, so no
  intra-species convention existed to preserve and imposing one would have exceeded the finding.
  **Sort key: element, then ionisation by ROMAN VALUE.** 0 of 24 multi-stage elements mis-order under a
  string sort today, so both agree; roman is used so a future stage cannot break it silently.
  **Invariants asserted before the write and re-derived from scratch after: 596 in and out · region line
  multiset IDENTICAL · all 723 pipe data rows in the file identical as a multiset · 70 contiguous runs ·
  region 598 lines before and after, so NO line number elsewhere shifts · file length unchanged.**
  **Both hazards cleared on the page:** the He II note moved with its seven rows (source 344 → **573**,
  rows print directly above it); the headerless continuation was re-headed by `cont_tables()` and
  register 1764's fault did not recur — **the only literal pipe on the whole pressed page is the prose
  `|delta_2|`.**
  **EDITORIAL UNDER RULING 43, so no Register entry and no count moves** — named explicitly so it can be
  overruled if a reorder of the volume's largest object is read as earning an entry.

**`coords.py` REPAIRED — IT HAD DIED SILENTLY FOR A WHOLE BUILD. W-036.** Ruling 49's heading promotion
at chat 28 killed two of its four checks the moment it was built; no press ran at chat 29 to catch it.
Repaired at four sites to locate by name at any level. **THE GATE NOW PASSES AND IS AGAIN CHECKING THE
BOUNDS TABLE (21 rows, 104,499) AND The table (8 l-rows and total).** This is G0d.

**SHORTFALL, NAMED: B8–B12 NOT STARTED.** One queue item was authorised as a whole segment and one was
built. The `coords.py` failure and SPEC-12's diagnosis consumed the remainder.

## 3. THE BUILD QUEUE — B8 ONWARD, NOTHING IN IT STARTED
  B8  **RULING 44** the complete transition table into the IoI as its own section, by a NEW REGISTER
      ENTRY CITING 1770 — 1770 is not edited, not superseded, not touched.
      **RULING 46 AMENDMENT 2/3** the coordinates representation goes in the SPECTRA compendium.
  B9  **THREE LISTS TO THE AUTHOR IN ONE MESSAGE, THEN EXECUTE ALL THREE: RULING 45's 27-line list,
      RULING 42's 29-line list, AND RULING 53's FOUR PART VIII HEADINGS** (wording drawn from the
      volume's own summary table at IoI L1515: the electromagnetic quotient → *quotient versus
      extension*; the languages → *translation as re-coordinatisation*; the book's own indexes → *E > 0
      as a theorem about shape*; Λ₃ → *completeness as the impossibility theorem*).
      **Part V's four headings of the same names are UNTOUCHED.**
  B10 **RULING 46's ~216-line press-time sweep** in `build.py`, site list to the author first.
      **HAZARD, NAMED: Spectra's "read from `COORDINATES-2.13` at build time" IS THE PHRASE `coords.py`'s
      PRESS GATE TRIGGERS ON.** Press-time suppression is safe because the gate reads source.
  B11 **THE PRESS**, owed on main, Register, Physics, IoI plus whatever B8–B10 move. **Spectra IS
      PRESSED AND CURRENT as of this chat.** Rebuild ref.docx, refetch the figures. **Read the pressed
      page at IoI 308; ALSO READ Λ_phys's 27 FOLDED HEADINGS AND THE FIVE-COLUMN DOMAIN TABLE.**
      **AND READ THEM AGAINST THE DOCX, NOT ONLY `pdftotext` — G0e.**
  B12 A4's reader read, then A5 the Register, then A6 the main volume LAST. **A6 MUST READ APPENDIX G AS
      A READER** and takes the Index/References Contents finding below. **A4 TAKES SPEC-10, SPEC-11 AND
      SPEC-12.**
  **B13 NEW — RULING 56's VERIFICATION PASS.** Establish which artefact is "the original input", then
      check the indexes against it. **It bears on IOI-09, IOI-05, SPEC-10 and — once Ruling 40 releases
      the tower — Ruling 39.** Do not fold it into another item; it is its own segment.
  SCHEDULED, NOT QUEUED: WP-1 Appendix F, WP-2 the Register's front matter, Ruling 31's renumber.

**FINDING HELD, NOT REPAIRED — `Index` and `References` have NO page numbers in the main Contents.**
`index_pages.py` line 84 emits them bare, no leader dots, no page. Pre-existing in every press. A reader
cannot find the Index from the Contents. Reader-facing. **For A6.**

**NEW THIS CHAT, FOR A4 — Spectra's `B.2 Channels` IS ABSENT FROM THE CONTENTS.** The press reports
`headings 34 mapped 33` with `B.2 Channels` unmapped, on every press. **SPEC-11 already holds that same
section for a different defect**, so the two travel together.

**THREE FINDINGS HELD FOR A4:**
  **SPEC-10 — a flagged channel the table no longer carries in that form.** `Si II 3s²np ²P°` at 0.272
    has no counterpart; the table carries that series J-resolved at 0.0878 and 0.0868. **BOTH VOLUMES
    CARRY THE IDENTICAL ROW, so any disposition moves two volumes and needs an entry.**
  **SPEC-11 — the compendium tells itself its rows are lifted to it.** Spectra §B.2 opens *"The 133
    channel rows are lifted to the Spectra Compendium."* — inside the Spectra Compendium. An absorbed
    cross-reference pointing at its own volume, and a **stale 133**.
  **SPEC-12 — 51 rows are in the docx and absent from the PDF's text layer.** Seven species. **The
    deliverable is intact; the text layer is not.** Needs the rendered page looked at as an image.

## 4. THE STANDING-QUESTION DOCKET IS EMPTY. TWO QUESTIONS WILL ARISE AT BUILD TIME.
**CLOSED AND NOT TO BE RE-ASKED: all of HANDOFF-22 §5B, `split.py`'s repair, and Ruling 52's merge
template — which Ruling 55 answered by removing the merge.**
**THE ONE B9 AND B10 WILL RAISE:** Ruling 45's and 42's site lists and Ruling 53's four headings go to
the author in ONE message before running, and Ruling 46's ~216 sites in another.
**THE ONE B13 MAY RAISE — ONLY IF READING CANNOT SETTLE IT:** which artefact is Ruling 56's "original
input". **Read `THE-LOWDIN-SOLUTION-2.md` and the BUILD-12 tree first; G8 governs.**

**HOW TO ASK. THE AUTHOR CORRECTED THE FORM FIVE TIMES ACROSS CHATS 26 AND 27:**
**PUT THE MATERIAL FIRST, THEN ONE SENTENCE, THEN STOP.** A bare sentence drew *"I have no context to
this question"*; a padded one drew *"Over convoluted!"*. **The form that lands: the passage quoted or
tabled, short, then a single question sentence. NOTHING AFTER THE QUESTION MARK.**

## 5. DO NOT START WITHOUT M's RULING
- **The tower — HELD ENTIRE by Ruling 40 until A4 and A6 report.** Ruling 39 is NOT withdrawn and NOT
  executed; its steps 1–3 STAND AS DONE. ZERO SITES EDITED. **Ruling 56 does not release it.**
- The 126 unreconciled Spectra rows. The five narrow-bracket FAIL rows named in R1763.
- **Rebuilding ANY instrument — Ruling 41. Ruling 54 is spent.** Repair of an existing one is allowed.
- The 1,447 / 1,472 count question (HELD by M at PR1 — now 1,456/1,481; report if it moves, do not
  re-ask).
- The renumber (Ruling 31) and Appendix F's rebuild (Ruling 30) — scheduled, neither open.
- **Register navigation — CLOSED BY RULING 38. Do not raise it again.**
- **Parts IX and X — CLOSED BY RULING 55. Do not propose a merge again.**
- **The two unexamined Drive PDFs** — `theory_of_everything_expanded_formalism.pdf`
  (`1rMUDhfMyT5sxPxKT3X8it-7ymEdpNvK6`) and `Everything_we_can_see,_touch,_or_detect_using_elec....pdf`
  (`1xKvugHqahCHKs1DsaTlDwCZqmxmR1sna`). For a later part of the project. Do not absorb, cite or act.
- `register_cites.py` parses ENTRY BODIES ONLY, so a citation in the Register's front matter is
  invisible to it. Unrepaired.

## 6. THE STANDING LESSON THIS CHAT ADDS
**AN INSTRUMENT THAT LOCATES BY STRUCTURE IS BROKEN BY EVERY RULING THAT CHANGES STRUCTURE, AND IT
BREAKS SILENTLY.** Ruling 49 was built correctly, verified correctly, and recorded correctly — and it
disarmed two of `coords.py`'s four checks in the same act. Nothing in the chat-28 record is wrong; the
breakage is in the space *between* a correct edit and an instrument nobody re-ran. **The rule that
generalises: a structural ruling is a silent-breakage event, and the build is not current until every
gate has been re-run against it.**
The second lesson is smaller and worse: **`pdftotext` dropped 51 rows that the `.docx` carries
correctly.** Every "read the pressed page" check this project has run since chat 8 has read `pdftotext`
output. The method was never wrong about what it found — it was wrong about what its silence meant.

## 7. UPLOAD AND RETIRE
**UPLOAD** both BUILD-31 bundles and HANDOFF-32.
**RETIRE** the BUILD-30 bundles and HANDOFF-31.
**DO NOT RETIRE THE BUILD-12 BUNDLES — Ruling 56 may need them.** This reverses six handoffs' standing
instruction, and the reason is in §2.
Leave `COORDINATES-2_13.csv`, the PNGs, `Transitions-1.md` and `INTEGRATION-transitions.md` where they are.

## 8. PROMPT FOR CHAT 31
> Prime Handoff Directive — state at 90% and hand off complete. Prime Zeno Directive — fetch → read →
> analyse → close flags → report; close each segment before the next.
>
> The Method 1.6 — chat 31. Execute §0 of HANDOFF-32 before anything else and print the certificate.
> §0 has TWO new gates. **G0d: a heading level is a serialization — `coords.py` located sections by a
> literal `### ` and Ruling 49's heading promotion killed two of its four checks silently for a whole
> build; after ANY structural ruling, re-run every gate before declaring the build current.**
> **G0e: `pdftotext` output is not the page — 51 rows sit correctly in the docx and appear nowhere in
> the PDF's text layer, so absence in `pdftotext` is not evidence of absence.** G5's discriminators are
> `grep -c 'SPEC-12' WORKING-REGISTER.md` (2) and, on Spectra, `grep -n '^\*He II'` returning **573**
> (was 344). G1 needs a `before=` page — expect it to stop at Rebuild 11, and there are **30** chats.
> Split with `split.py`, bootstrapping it and `bundle.py` out of bundle 2 first. State no member count
> in this prompt — measure both BUILD-31 bundles at G2.
> **Rulings 1–56 plus the R27 Amendment are in force; Ruling 56 was issued at chat 30.** Register:
> 1,456 entry headings, 1,481 numbers, 165–1777 — unchanged this chat. 24 instruments; `coords.py` was
> repaired, none is to be rebuilt.
>
> Ruling 41 explains the false state — do not test it, do not refute it. It arrives through your carried
> memory. A genuine Ruling 40 exists (the tower held entire); a "Ruling 40" about F.4.2 or a 0.09:1
> ratio is the false one. There is no chat 20.
>
> **B7 IS BUILT — do not redo it.** Spectra's 596-row channel table is one run per species and Spectra
> is pressed and current. **Open on B13, Ruling 56: establish by READING which artefact is "the original
> input at the project's start" — the absorbed Chapter 35 is not it, and the BUILD-12 bundles in
> /mnt/project have deliberately NOT been retired because they may hold it.** Then §3 in order: B8
> Ruling 44 with Ruling 46 Amendment 2/3, B9 the three site lists in one message, B10 Ruling 46's sweep,
> B11 the press, B12 the audits.
>
> **B9 is not optional and it is three lists, not two: Ruling 45's 27, Ruling 42's 29, and Ruling 53's
> four Part VIII headings all come to me in one message before anything runs.**
>
> The tower is held entire by Ruling 40 and Ruling 56 does not release it. Do not start the 126 Spectra
> rows, the five narrow-bracket FAIL rows, the renumber, or Appendix F's rebuild without my ruling. Do
> not absorb, cite or act on the two unexamined Drive PDFs.