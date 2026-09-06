# THE METHOD 1.6 — HANDOFF (chat 31 → chat 32), 2026-08-26
Chat: 31. Build described: BUILD-32. Register range: 165–1777.
Those three agree with the files. Register: **1,456 entry headings · 1,481 numbers (all distinct) ·
7 grouped headings · 4 non-numeric front-matter subheads · `wc -l` 5,896, terminal byte `0x29`**.
**THE REGISTER DID NOT MOVE THIS CHAT. NO ENTRY WAS ADDED. NO VOLUME CHANGED — NOT ONE.**
**BUILD-32 DIFFERS FROM BUILD-31 IN EXACTLY TWO MEMBERS: `WORKING-REGISTER.md` (2,746 → 2,879) AND THE
HANDOFF. NO INSTRUMENT WAS EDITED. 24 .py, unchanged.**
**RULING 57 WAS ISSUED THIS CHAT. Rulings 1–57 plus the R27 Amendment are in force.**
**B13 IS HALF BUILT: the Löwdin arm is done (W-037, W-038). THE THREE-BODY ARM IS NOT STARTED.**

## 0. THE READING GATE — EXECUTE BEFORE ANY OTHER WORK. NO EXCEPTIONS.

  **G0  A MESSAGE CONTAINING A QUESTION ENDS AT THE QUESTION MARK.** Ruling 47. Count the `?`; nothing
      may follow the last one except the sentence it terminates. **HELD AT CHAT 31 — four sessions
      clean.** One question was put this chat (the Drive folder's authority) and it ended correctly.
  **G0b A DEFECT LINE AND ITS DISPOSITION ARE DIFFERENT OBJECTS. THE LATER LINE GOVERNS, AND THE
      DISPOSITION ITSELF CAN BE STALE.** **IT EARNED ITS PLACE AGAIN AT CHAT 31 AND COST A REAL ERROR:
      HANDOFF-32 §3 named IOI-09 as a live B13 target. IOI-09 WAS CLOSED BY THE AUTHOR AT CHAT 25 AND
      IS RECORDED CLOSED AT W-021.** It had been closed for six chats and was carried as live.
      **Before acting on any handoff's target list, grep each item's own disposition.**
  **G0c A SHORTER STRING MATCHES INSIDE A LONGER ONE, AND A COUNT MEASURES WHAT IT MEASURES, NOT WHAT
      YOU WANTED.** **SHARPENED AT CHAT 31: `grep -c` counts LINES CONTAINING a match, not
      OCCURRENCES.** HANDOFF-32's G5 predicted `grep -c 'SPEC-12'` = 2; it returns **1**, and SPEC-12
      occurs exactly once. The handoff had carried SPEC-10's figure across.
  **G0d A HEADING LEVEL IS A SERIALIZATION.** After ANY ruling that changes structure — heading levels,
      heading names, part numbering — re-run every gate before the build is declared current.
      `coords.py` was repaired at chat 30 for exactly this and now passes.
  **G0e `pdftotext` OUTPUT IS NOT THE PAGE.** SPEC-12: 51 rows correct in the `.docx` extract, zero from
      the PDF text layer. **APPLIED PROPERLY AT CHAT 31 FOR THE FIRST TIME:** when W-038 rested on
      absences in a PDF's text layer, the five figure pages were RENDERED WITH `pdftoppm -r 90 -png`
      AND READ AS IMAGES before the absences were called final. **That is the remedy; use it.**
  **G0f NEW, AND IT IS A CONTEXT-KILLER RATHER THAN A CORRECTNESS FAULT: THE DRIVE CONNECTOR WRITES TO
      DISK ONLY ABOVE ~1 MB OF RESPONSE. BELOW THAT IT COMES BACK INLINE, IN FULL, AS BASE64.**
      Base64 inflates by 4/3, so **the danger band is a file of roughly 100 KB to 750 KB**: too big to
      read, too small to be spilled to disk. A 340 KB PDF arrives as ~454 KB of base64 ≈ 114,000 tokens.
      **COMPUTE `size × 4/3` BEFORE EVERY DRIVE FETCH.** Over ~1 MB → safe, lands at
      `/mnt/user-data/tool_results/<id>.json`. Under ~60 KB → safe, small. **In between → fetch it in
      the FIRST segment of a session or not at all.** This is why the three-body arm of B13 is unstarted.

  G1  `recent_chats n=20`; again with `before=`. **31 CHATS AT CHAT 32**: Rebuild 1–12, 13–19, 21–31,
      plus one unnumbered ("Extract transitions from file"). **THERE IS NO CHAT 20.** n=20 stopped at
      **Rebuild 11** at chat 31; expect **Rebuild 12**. MEASURE; DO NOT RECITE.
  G2  Split both BUILD-32 bundles with `split.py`. **IT IS A BUNDLE MEMBER, SO BOOTSTRAP IT FIRST:**
      one regex pass over bundle 2 pulling only `bundle.py` and `split.py`, then
      `python3 split.py <b1> <b2> -o /home/claude/build`. It prints declared · paired · spurious ·
      re-assembly and **exits nonzero if re-assembly is not byte-exact**. If a bundle looks absent,
      RE-LIST; /mnt/project syncs late.
  G3  Read `WORKING-REGISTER.md`. **`wc -l` RETURNS 2879.** VERIFY. `sed -n 'a,bp'` is cheaper than
      `view`. It carries **RULINGS 27, 28, the R27 Amendment, 29–57** and **W-001…W-038 plus SPEC-12**.
      **RULING HEADING LINES — 27 at 4, 28 at 11, Amendment at 19, 29 at 736, 30 at 785 (BOLD INLINE,
      not `###`), 31 at 837 and 884, 32 at 903, 33 at 943, 34 at 974, 35 at 987, 36 at 994, 37 at 1001,
      38 at 1217, 39 at 1420, 40 at 1619 (the tower held entire — the GENUINE one), 41 at 1734,
      42 at 1755, 43 at 2019, 44 at 2024, 45 at 2038, 46 at 2052, 47 at 2108, 48 at 2146, 49 at 2175,
      50 at 2190, 51 at 2229, 52 at 2286 — DEAD, read 55 with it — 53 at 2319, 54 at 2363, 55 at 2570,
      56 at 2636 (NOT 2635; HANDOFF-32 was one off), 57 at 2748.**
      **SEARCH RULINGS CASE-INSENSITIVELY. `W-015` MATCHES INSIDE `W-015a`.**
  G4  PRINT THE CERTIFICATE. Until it prints, state NOTHING about the work, change NO file.
      CERT: chats read = N/__ · bundle members = ___ + ___ · rulings = 1–57 + amendment
            · Register entry headings = ____ · Register numbers = ____ · instruments = ____
            · **G0 · G0b · G0c · G0d · G0e · G0f acknowledged**
  G5  VERIFY BUILD IDENTITY, NOT SIZE. **NO VOLUME CHANGED THIS CHAT, SO THERE IS NO NEW VOLUME
      DISCRIMINATOR. Spectra's `grep -n '^\\*He II'` still returns 573 and MUST.** The build
      discriminators are `grep -c 'RULING 57' WORKING-REGISTER.md` and `grep -c 'W-038'`.
      **If a VOLUME disagrees, stop. If only the working register disagrees, read this handoff's
      closing block before concluding anything.**
  G6  **CHECK THE TOOL EXISTS BEFORE TRUSTING ITS SILENCE.** `xxd` IS NOT INSTALLED. Use `od -An -tx1`.
      `pdftoppm` IS installed — verified chat 31.
  G7  **A REIMPLEMENTATION THAT DISAGREES WITH AN INSTRUMENT IS THE THING THAT IS WRONG.**
  G8  **A QUESTION YOU CAN ANSWER BY READING IS NOT A STANDING QUESTION.** **VINDICATED AT CHAT 31:**
      B13's scope question — which artefact is Ruling 56's "original input" — was carried by HANDOFF-32
      as possibly needing the author. It was settled by two Drive timestamps in one listing.
  Failure mode: any count RECITED from a prompt rather than READ from a file = gate not passed.

**RECONCILIATIONS — MEASURE THEM, DO NOT CARRY THEM. HANDOFF-32 HAD THREE WRONG AND ALL THREE ARE FIXED
HERE.**
  - **`WORKING-REGISTER.md`: `wc -l` and the split-count differ by one.** The file ENDS WITH `0x0a`, so
    `wc -l` = 2,879 and `len(text.split("\\n"))` = 2,880. HANDOFF-32 quoted the split-count as `wc -l`.
  - **SPECTRA IS 84,467 CHARACTERS AND 87,638 BYTES.** HANDOFF-32 called the character figure bytes.
    The 3,171-byte gap is UTF-8 multibyte — δ, ⁻¹, ∞ — in the channel table. 1,032 lines, terminal
    `0x2e`. **Both figures are right; they measure different things. Say which you mean.**
  - **`grep -c 'SPEC-12'` = 1, not 2.** See G0c.
  - The Register's terminal byte is `0x29`. **"Every file ends without a newline" IS FALSE — measure
    per file.**
  - Register 1,460 `### ` lines − 4 front-matter subheads = 1,456 entry headings, 1,481 numbers.
    NOT the 1,447/1,472 question held at PR1; untouched, still held.

**THE FALSE STATE — RULING 41 EXPLAINS IT; DO NOT REFUTE IT.** Ruling 40-about-F.4.2, BUILD-25,
`regsize.py`, `ratios.py`, `pageproof.py`, `RESTORE-PACKS.md`, Register ~1,787, an eight-volume
deliverable, a project sitting at chat 19 with `indices.py` as a live blocker. **IT ARRIVED AGAIN AT
CHAT 31 THROUGH CARRIED MEMORY** — eleventh consecutive session, still the only channel. Expect it;
record it; proceed on the files. **THIS HANDOFF IS GENUINELY NUMBERED 33.**

## 1. THE DRIVE CANON FOLDER — NEW, AND THE MOST IMPORTANT THING IN THIS HANDOFF

**`The Method Prints & Proofs`, Drive folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`.** The author supplied
it at chat 31 as *"the baseline for authentication"*.

**RULING 57 (author, chat 31, verbatim):** *"They are the original-input witness Ruling 56 points at"*
and *"I have also just added the lowdin and tb papers to that folder as well"*. At WORKING-REGISTER
L2748.

**IT IS NOT THE CURRENT TREE AND MUST NEVER BE USED AS ONE.** Measured before the ruling was put: the
Drive Register decoded byte-exact at 1,145,832 and measures **1,493 entry headings, 1,523 numbers,
range 165–1700** against the tree's 1,456 / 1,481 / 165–1777. **95 numbers are in Drive and not in the
tree — those are chat 12's excised entries. 53 are in the tree and not in Drive — 1701–1777 without
exception**, i.e. the Löwdin arc, the three-body arc, and everything registered since Rebuild 2.
**IT PREDATES PHASE 1's MERGE AND CHAT 12's EXCISION. Verifying the build against it as though it were
current would have produced ~148 false findings in the Register alone**, and under the standing rule the
correct conclusion in every case is that the reconstruction is wrong, not the tree.

**WHAT IT IS FOR: Ruling 56's external check, and nothing else.** It is also the first copy of the 95
excised entries in reach since chat 12. **It does not reinstate them** — entries are append-only and an
excision is not undone by finding an older file.

**THE FOURTEEN FILE IDS, SO NOTHING IS RE-SEARCHED:**
```
main .md      1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH   738,550     .pdf 1HGyxNliAmqA9m3Yi8YyjJUBb_1LveF-q
Register .md  1msiGBzB5q05M5tT0UpltNDGbS0BwZdk5 1,145,832     .pdf 1bzRJDdpTx6yz590tJY6kHNcCZ2ggOJ3C
Math .md      1PWVD1DDmglZLIV3I3NwEOcd7eSzD2QDf   188,768     .pdf 1pH3CV33lAGubrIuELFl4kd-Fp-JfgX4B
Physics .md   1goehl5D6Wnf90e-sJM3_s0PQz114WzIZ    43,519     .pdf 1_I5JLcXg7LRLso-pxS6S2F6SwDgeY0KF
IoI .md       1OoPPXi1x2fsPuc5xNJeCu1YJAUai-fpQ    89,393     .pdf 1WgqpZRWD7VbmWv15i0MvIQ08IcB4oTIg
Spectra .md   1eVsesDBML-paJq6UejtAFhF-xTS7wvje    78,292     .pdf 1joTQEpGnw-pT6YMN8cKCizQtI-SdqB3q
LÖWDIN ORIGINAL .pdf      1r5_KE69TLo7dqcU3jhS8qbdHFQfC7rz7   879,791   FETCHED, VERIFIED, ON DISK
THREE-BODY ORIGINAL .pdf  151Yg3WgY-aqx24jrlHdvtPK8a-rNgMKL   340,837   **NOT FETCHED — SEE G0f**
```
**THE TIMESTAMPS ARE THE EVIDENCE THAT SETTLED B13's SCOPE.** Löwdin PDF CreationDate
**2026-08-23 20:14:46 UTC**, filed 20:17:47. Three-body filed **22:05:27**. **Rebuild 1 — the project's
first session — opened 23:10:27.** Both papers predate the first chat, so they ARE *"the original input
at the project's start"*, and the absorbed Chapters 35 and 36 are not. **Do not re-derive this.**
**COLLATERAL: Löwdin 20:14 precedes three-body 22:05 on the same day, which corroborates — from a
source the ruling never saw — the timestamp ruling giving Löwdin 1701–1712 / Ch 35 and three-body
1713–1724 / Ch 36.**

## 2. INSTRUMENTS — 24 .py. NONE ADDED, REMOVED OR EDITED THIS CHAT.

`appf.py bookindex.py build.py bundle.py channels_LIMB.py coords.py crop_titles.py dclose.py depoint.py
excise.py fig_rerender.py heii.py index_gen.py index_pages.py kinds.py qgraph.py rclose.py
register_cites.py ruled_bracket.py run489.py spectra_count.py split.py tb_audit.py trueres.py`

**RULING 41 CLOSES THE MISSING-INSTRUMENT QUESTION PERMANENTLY.** guard.py, press_all.py, mkref.py,
figs.py, pageproof.py, ratios.py, regsize.py, indices.py, mathreg.py, mathverify.py, compendium.py,
store_gen.py, RESTORE-PACKS.md lived in deleted chats and are NOT recoverable. Do not search Drive. Do
not ask the author. `appf.py` is RETIRED — dead code, do not call it. **guard.py DOES NOT EXIST**; its
function is md5 of the tree against a pristine re-split of the previous build with `split.py`.
**DO NOT REBUILD ANY INSTRUMENT. Ruling 54 is spent.**

**ref.docx — NOT A BUNDLE MEMBER. Rebuild every session that presses**, on W-013's corrected recipe
(~WORKING-REGISTER line 1549). pandoc's default here carries 36 theme attributes and 3 plain; convert
all to literal Georgia; docDefaults already carries `sz` 24 so **REPLACE it with 21, never insert**; add
`EntryBody`; match `sectPr` **BY ELEMENT NAME** — it serialises `<w:sectPr />`, with a space — and set
12240×15840 with six 1440 margins. Verified object: 9,773 bytes.

**FIGURES — NOT bundle members, refetch each session that presses.**
`The_Method_1_6_figures_BUILD13.zip`, Drive `1q7pvnxMPILD9AVoH6XjymZHXX79YzITd`, **6,299,293 bytes**,
md5 `78888f2078dc5342ab221a59bbcf8921`. Unzip into `/home/claude/build/`: `figures/` **49**,
`figures-compendia/` **12**. **Over 1 MB, so it spills to disk — safe under G0f.**

**COORDINATES-2.13 — SUPPLIED, DO NOT ASK AGAIN.** `/mnt/project/COORDINATES-2_13.csv`, 10,912,381
bytes; the connector refuses it (10 MB cap). Not a bundle member. `coords.py` reaches `/mnt/project/`
directly and gates Spectra inside `build.py`. 104,832 rows; grade exact 929 · measured 358 · computed
103,545; bound 22 distinct, 21 printed rows summing to 104,499. **Gate returned PASS at chat 30.**

**PRESS INVOCATIONS.** The digit is LAST in argv; it is `index_pages.py`'s DEPTH.
**`build.py` PREFIXES ITS OWN BASE DIR — pass a bare filename, never an absolute path.**
  main      `python3 build.py The_Method_1_6-2.md OUT/main.docx "The Method 1.6" strip pages 2`
  Register  `python3 build.py ...The_Register-2.md OUT/register.docx "... — The Register" fix 0`
            **NO `pages`. RULING 38. SETTLED TWICE — do not re-derive it a third time.**
  math/phys/ioi/spectra  `python3 build.py <src> OUT/<x>.docx "<title>" pages 2`
  Register afterwards: `soffice --headless --convert-to pdf --outdir OUT OUT/register.docx`

## 3. WHAT WAS BUILT THIS CHAT — RULING 57, W-037, W-038. NO VOLUME MOVED.

**W-037 — B13's LÖWDIN ARM: PASS, NO FINDING AGAINST THE TREE.** Number-multiset comparison of the
original's text against `THE-LOWDIN-SOLUTION-2.md`: **96 distinct numbers in the original, 115 in the
tree, ZERO present in the original and absent from the tree.** The tree is a strict superset; nothing
lost. Fourteen roman sections in the same order under the same names in both. **Seven load-bearing
values re-read IN THEIR SENTENCES rather than merely counted** — 137.035999 as the only entered number,
V.1's *107 out of 107*, the period sequence 2, 8, 8, 18, 18, 32, 32, the no-g-block result, Z = 91
protactinium's zero-crossing, the twelve predictions Z = 109–120, and Z = 120 — **all seven agree.**
**One apparent conflict chased and cleared:** the tree's *"The law's domain is Z ≤ 112"* against a
section titled *predictions to Z = 120* is a faithful compression of §VIII's two-part boundary —
spin-orbit worst case **0.083 hartree**, (n,ℓ) safe through Z = 112, (n,ℓ,j) reproducing Dirac–Fock
through Z = 120. **Recorded as a pass because an unrecorded pass cannot be told from a check that never
ran.**

**W-038 — RULING 56's REACH IS BOUNDED, AND IT IS NARROWER THAN HANDOFF-32 ASSUMED.** Measured on the
original's text layer: **976 → 0 hits · 6912 → 0 · 5936 → 0 · 247 → 0 · 18288 → 0 · 199130 → 0 ·
118 → 1 · 107 → 18.** **The paper states the filling rule, the period lengths, the exceptions, the
ordering clause and the predictions. IT DOES NOT STATE THE INDEX CELL COUNTS**, which are objects
derived in THIS work, after the paper.
**CONSEQUENCES, AND THEY REWRITE B13's TARGET LIST:**
  - **IOI-05 IS NOT REACHABLE BY RULING 56** — 199,130 does not appear in the original at all, so the
    Löwdin solution cannot adjudicate between its two readings.
  - **RULING 39's TOWER IS NOT REACHABLE EITHER. Ruling 40 still holds it entire and Ruling 56 does not
    release it** — HANDOFF-32 said so and was right, but for a weaker reason than the true one.
  - **SPEC-10 IS NOT REACHABLE** — it is a Rydberg channel flag; the paper is about periodic-table
    filling.
  - **IOI-09 IS CLOSED** (W-021, chat 25) and should never have been on the list. See G0b.
**WHAT RULING 56 CAN REACH, STATED POSITIVELY: every index or passage in the volumes that restates the
periodic law** — the Madelung (n+ℓ) rule, the period-length sequence, the derived exceptions, the
no-g-block result, the Z ≤ 112 domain, the twelve predictions. **That is the real target list.**
**THE G0e CHECK WAS RUN AND CLOSED, NOT CARRIED.** Five figure pages rendered with
`pdftoppm -f N -l N -r 90 -png` and read as images. Figure 1 (p6) is *The Spectra Index, Z = 2–120*;
Figure 2 (p7) is *The Filling Index*, annotated *ordering clause 107/107*. **Neither carries a cell
census.** Figures 3–5 stand on their captions, which are text: the predictions window, the dm2
widening, the relativistic table against c → ∞ with eleven disagreements. **Figures 1–2 MEASURED as
images; 3–5 measured as captions and INFERRED as to their interiors.**
**COLLATERAL FOUND ON FIGURE 2's PAGE, NOT PREVIOUSLY IN THE RECORD AND NOT CHECKED AGAINST THE TREE:**
§V.3 gives the g-block frontier candidacies as **5g at 65 elements, 6g at 70, 7g at 57, 8g at 28**.

**SHORTFALL, NAMED: B13's THREE-BODY ARM WAS NOT STARTED, AND B8–B12 WERE NOT REACHED.** The three-body
arm was blocked by G0f, not by time — see §4 item B13b. B8–B12 were not opened because B13 was the
queue head and the Drive folder arrived mid-session and had to be characterised before anything could
rest on it.

## 4. THE BUILD QUEUE
  **B13b FIRST ITEM OF CHAT 32, AND IT MUST BE THE FIRST TOOL CALL AFTER THE GATE.** Fetch
      `The_Three_Body_Problem_for_Unknown_Masses_Lach.pdf`, Drive `151Yg3WgY-aqx24jrlHdvtPK8a-rNgMKL`,
      340,837 bytes. **IT WILL ARRIVE INLINE AS ~454 KB OF BASE64 ≈ 114,000 TOKENS — G0f.** That is
      survivable at the start of a session and fatal at the end. **Then repeat W-037's method against
      `The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md`: number-multiset comparison, then the
      load-bearing values re-read in their sentences, then the figures as images.**
  **B13c THE REAL VERIFICATION PASS — the periodic-law restatements across the volumes, against the
      Löwdin original.** W-038 defines the target list. This is what Ruling 56 was issued for. **Do not
      fold it into another item; it is its own segment.**
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
      **HAZARD: Spectra's "read from `COORDINATES-2.13` at build time" IS THE PHRASE `coords.py`'s
      PRESS GATE TRIGGERS ON.** Press-time suppression is safe because the gate reads source.
  B11 **THE PRESS**, owed on main, Register, Physics, IoI plus whatever B8–B10 move. **Spectra IS
      PRESSED AND CURRENT.** Rebuild ref.docx, refetch the figures. **Read the pressed page at IoI 308;
      ALSO READ Λ_phys's 27 FOLDED HEADINGS AND THE FIVE-COLUMN DOMAIN TABLE. AND READ THEM AGAINST THE
      DOCX, NOT ONLY `pdftotext` — G0e.**
  B12 A4's reader read, then A5 the Register, then A6 the main volume LAST. **A6 MUST READ APPENDIX G AS
      A READER** and takes the Index/References Contents finding below. **A4 TAKES SPEC-10, SPEC-11 AND
      SPEC-12.**
  SCHEDULED, NOT QUEUED: WP-1 Appendix F, WP-2 the Register's front matter, Ruling 31's renumber.

**FINDING HELD, NOT REPAIRED — `Index` and `References` have NO page numbers in the main Contents.**
`index_pages.py` line 84 emits them bare, no leader dots, no page. Pre-existing in every press. A reader
cannot find the Index from the Contents. Reader-facing. **For A6.**

**FOR A4 — Spectra's `B.2 Channels` IS ABSENT FROM THE CONTENTS.** The press reports `headings 34
mapped 33` with `B.2 Channels` unmapped, on every press. **SPEC-11 already holds that same section for
a different defect**, so the two travel together.

**THREE FINDINGS HELD FOR A4:**
  **SPEC-10 — a flagged channel the table no longer carries in that form.** `Si II 3s²np ²P°` at 0.272
    has no counterpart; the table carries that series J-resolved at 0.0878 and 0.0868. **BOTH VOLUMES
    CARRY THE IDENTICAL ROW, so any disposition moves two volumes and needs an entry.**
  **SPEC-11 — the compendium tells itself its rows are lifted to it.** Spectra §B.2 opens *"The 133
    channel rows are lifted to the Spectra Compendium."* — inside the Spectra Compendium. An absorbed
    cross-reference pointing at its own volume, and a **stale 133**.
  **SPEC-12 — 51 rows are in the docx and absent from the PDF's text layer.** Seven species. **The
    deliverable is intact; the text layer is not.** Needs the rendered page looked at as an image —
    **and chat 31 proved `pdftoppm -r 90 -png` is the way to do it.**

## 5. THE STANDING-QUESTION DOCKET IS EMPTY.
**CLOSED AND NOT TO BE RE-ASKED:** all of HANDOFF-22 §5B, `split.py`'s repair, Ruling 52's merge
template (Ruling 55 removed the merge), and **B13's scope question, which G8 settled by reading**.
**THE ONE B9 AND B10 WILL RAISE:** Ruling 45's and 42's site lists and Ruling 53's four headings go to
the author in ONE message before running, and Ruling 46's ~216 sites in another.

**HOW TO ASK. THE AUTHOR CORRECTED THE FORM FIVE TIMES ACROSS CHATS 26 AND 27:**
**PUT THE MATERIAL FIRST, THEN ONE SENTENCE, THEN STOP.** A bare sentence drew *"I have no context to
this question"*; a padded one drew *"Over convoluted!"*. **The form that lands: the passage quoted or
tabled, short, then a single question sentence. NOTHING AFTER THE QUESTION MARK.** It worked at chat 31.

## 6. DO NOT START WITHOUT M's RULING
- **The tower — HELD ENTIRE by Ruling 40 until A4 and A6 report.** Ruling 39 is NOT withdrawn and NOT
  executed; its steps 1–3 STAND AS DONE. ZERO SITES EDITED. **Ruling 56 does not release it, and W-038
  now shows it cannot.**
- The 126 unreconciled Spectra rows. The five narrow-bracket FAIL rows named in R1763.
- **Rebuilding ANY instrument — Ruling 41. Ruling 54 is spent.** Repair of an existing one is allowed.
- The 1,447 / 1,472 count question (HELD by M at PR1 — now 1,456/1,481; report if it moves, do not
  re-ask).
- The renumber (Ruling 31) and Appendix F's rebuild (Ruling 30) — scheduled, neither open.
- **Register navigation — CLOSED BY RULING 38. Do not raise it again.**
- **Parts IX and X — CLOSED BY RULING 55. Do not propose a merge again.**
- **The 95 excised entries now visible in the Drive Register. DO NOT REINSTATE THEM.** Entries are
  append-only; an excision is not undone by finding an older file. Ruling 57 makes the Drive set a
  witness, not a source.
- **The two unexamined Drive PDFs** — `theory_of_everything_expanded_formalism.pdf`
  (`1rMUDhfMyT5sxPxKT3X8it-7ymEdpNvK6`) and `Everything_we_can_see,_touch,_or_detect_using_elec....pdf`
  (`1xKvugHqahCHKs1DsaTlDwCZqmxmR1sna`). For a later part of the project. Do not absorb, cite or act.
- `register_cites.py` parses ENTRY BODIES ONLY, so a citation in the Register's front matter is
  invisible to it. Unrepaired.

## 7. THE STANDING LESSON THIS CHAT ADDS
**AN EXTERNAL CHECK MUST BE SCOPED BEFORE IT IS TRUSTED, AND SCOPING IT IS THE FIRST HALF OF USING IT.**
Ruling 56 arrived as a gift — a true and accurate source against which the indexes could be measured —
and HANDOFF-32 immediately listed four findings it would settle. **It settles none of them.** The paper
does not contain the numbers those findings are about, because those numbers were produced by this work
after the paper was written. Nothing was wrong with the ruling and nothing was wrong with wanting to use
it; the fault was assuming that a source described as authoritative is authoritative *about the thing in
front of you*. **The rule that generalises: before an external source is used to adjudicate anything,
measure what it actually contains, and write down what it cannot reach.** A source's silence on a
question is not agreement, and it is not disagreement — it is absence of jurisdiction.
The second lesson is narrower and is now G0f. **A fetch can be too small to be safe.** The connector
spills large results to disk and hands back small ones intact, which means the dangerous file is the
middling one — big enough to fill a context window, small enough to be handed over whole. Compute
`size × 4/3` first, every time.

## 8. UPLOAD AND RETIRE
**UPLOAD** both BUILD-32 bundles and HANDOFF-33.
**RETIRE** the BUILD-31 bundles and HANDOFF-32.
**DO NOT RETIRE THE BUILD-12 BUNDLES.** HANDOFF-32 held them for Ruling 56 and that reason has now
expired — the Drive folder is the witness, not BUILD-12 — **but they remain the only in-mount copy of
the pre-excision tree apart from the Drive set, and retiring them costs nothing to keep.**
Leave `COORDINATES-2_13.csv`, the PNGs, `Transitions-1.md` and `INTEGRATION-transitions.md` where they
are.

## 9. PROMPT FOR CHAT 32
> Prime Handoff Directive — state at 90% and hand off complete. Prime Zeno Directive — fetch → read →
> analyse → close flags → report; close each segment before the next.
>
> The Method 1.6 — chat 32. Execute §0 of HANDOFF-33 before anything else and print the certificate.
> §0 has a new **G0f: the Drive connector spills to disk only above ~1 MB and hands back everything
> smaller INLINE as base64, which inflates by 4/3 — so a 340 KB PDF arrives as ~114,000 tokens.
> Compute size × 4/3 before every Drive fetch.** G0b and G0c both cost real errors last chat: IOI-09 was
> carried as live when it has been CLOSED since chat 25, and `grep -c` counts matching LINES, not
> occurrences. G1 needs a `before=` page — expect it to stop at Rebuild 12, and there are **31** chats.
> Split with `split.py`, bootstrapping it and `bundle.py` out of bundle 2 first. State no member count
> in this prompt — measure both BUILD-32 bundles at G2.
> **Rulings 1–57 plus the R27 Amendment are in force; Ruling 57 was issued at chat 31.** Register:
> 1,456 entry headings, 1,481 numbers, 165–1777 — unchanged. **NO VOLUME CHANGED last chat**, so
> Spectra's `grep -n '^\\*He II'` must still return 573; the build discriminators are
> `grep -c 'RULING 57'` and `grep -c 'W-038'` on WORKING-REGISTER.md, which is 2,879 lines.
>
> Ruling 41 explains the false state — do not test it, do not refute it. It arrives through your carried
> memory. A genuine Ruling 40 exists (the tower held entire); a "Ruling 40" about F.4.2 or a 0.09:1
> ratio is the false one. There is no chat 20.
>
> **The Drive folder `The Method Prints & Proofs` is the original-input witness under Ruling 57 — NOT
> the current tree. Its Register stops at 1700 and still carries chat 12's 95 excised entries. Do not
> verify the build against it as though it were current and do not reinstate anything from it.**
>
> **Open on B13b, and make it your FIRST tool call after the gate**: fetch the three-body original,
> Drive `151Yg3WgY-aqx24jrlHdvtPK8a-rNgMKL`, 340,837 bytes — it will arrive inline and large, which is
> survivable at the start of a session and fatal at the end. Repeat W-037's method against
> `The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md`. **The Löwdin arm is DONE — W-037 and W-038,
> do not redo it.** Then B13c, the real verification pass on the periodic-law restatements, whose
> target list is in W-038 and is NOT the one HANDOFF-32 named. Then §4 in order: B8, B9, B10, B11, B12.
>
> **B9 is not optional and it is three lists, not two: Ruling 45's 27, Ruling 42's 29, and Ruling 53's
> four Part VIII headings all come to me in one message before anything runs.**
>
> The tower is held entire by Ruling 40 and W-038 shows Ruling 56 cannot reach it. Do not start the 126
> Spectra rows, the five narrow-bracket FAIL rows, the renumber, or Appendix F's rebuild without my
> ruling. Do not absorb, cite or act on the two unexamined Drive PDFs.
