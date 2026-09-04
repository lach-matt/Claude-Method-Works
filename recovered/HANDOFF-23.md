# THE METHOD 1.6 — HANDOFF (chat 21 → chat 22), 2026-08-26
Chat: 21. Build described: BUILD-22. Register range: 165–1768.
Those three agree with the files. Register: 1,447 entry headings · 1,472 numbers (all distinct) ·
7 grouped headings · 4 non-numeric front-matter subheads.
**NO REGISTER ENTRY ADDED OR REMOVED. NO VOLUME CHANGED. Zero characters edited in any of the six
volumes.** One file changed: WORKING-REGISTER.md, 1,772 → 1,835 lines, W-017 appended under
Ruling 27. **Rulings 1–42 plus the R27 Amendment are in force. NO RULING ISSUED THIS CHAT.**

## 0. THE READING GATE — EXECUTE BEFORE ANY OTHER WORK. NO EXCEPTIONS.
It has now run eight times and found an error inside itself on seven.
  G1  recent_chats n=20; again with before= if the earliest is not reached.
  G2  Split both BUILD-22 bundles. MEASURE both. Count DECLARED, PAIRED and spurious markers
      SEPARATELY. If a bundle looks absent, RE-LIST; /mnt/project syncs late.
  G3  Read WORKING-REGISTER.md. MEASURE ITS LENGTH FIRST — 1,835 lines at the close of chat 21.
      VERIFY, do not recite. `sed -n 'a,bp'` does not elide and is cheaper than `view`.
      It carries RULINGS 27–42 + the R27 Amendment, 114 excised headings (119 numbers), W-001…W-017.
  G4  PRINT THE CERTIFICATE. Until it prints, state NOTHING about the work, change NO file.
      CERT: chats read = N/__ · bundle members = ___ + ___ · rulings = 1–42 + amendment
            · Register entry headings = ____ · Register numbers = ____ · instruments = ____
  G5  VERIFY BUILD IDENTITY, NOT SIZE: `wc -l WORKING-REGISTER.md` (1,835) and
      `grep -c coords build.py` (3). Either disagrees → STOP and report.
  Failure mode: any count RECITED from a prompt rather than READ from a file = gate not passed.

**RECONCILIATIONS — measure once, do not treat as conflicts.** Re-measured at chat 21.
  - Register 1,451 `### ` lines − 4 front-matter subheads = 1,447 entry headings, 1,472 numbers.
    NOT the 1,447/1,472 question held at PR1; that one is untouched and stays held.
  - Every volume lacks a trailing newline, so `wc -l` reports one less. Main 11,703 · Register 5,860
    · Math 3,471 · Physics 861 · IoI 1,947 · Spectra 1,010. NOT a defect.
  - Excised: 114 headings, 119 numbers, THREE grouped. 69 A-production · 22 B-session · 23 C-internal.

**MEMBER COUNTS: STATE NONE IN THE OPENING PROMPT. MEASURE AT PACK TIME.** Eight sessions have now
logged a member-count discrepancy and **every one was a PREDICTION, never a packing fault.**
W-015a predicted BUILD-21 bundle 2 would land at 76 "by design"; chat 21 measured **79**, paired,
zero spurious. The BUILD20 residue members WERE dropped — the only BUILD-named members left are
`EXCISE-SITES-BUILD14.json` and `POINTERS-BUILD14.json`, the pair that once fooled a `grep -c BUILD`.
The residual two could not be diffed because the BUILD-20 bundle is not in project knowledge.
**Unresolved, not explained. Do not re-predict it; measure it.**

**THE FALSE STATE — RULING 41 EXPLAINS IT; DO NOT REFUTE IT AGAIN.** Ruling 40-about-F.4.2,
BUILD-25, HANDOFF-28, regsize.py, ratios.py, pageproof.py, RESTORE-PACKS.md, Register ≈1,787 are
residue of chats deleted after a fatal error. **NEW AT CHAT 21: it arrived through the MODEL'S
CARRIED MEMORY, not through the prompt or the handoff.** Seven sessions met it in the prompt; the
eighth met it in memory. The gate caught it. Expect that channel.
COLLISION: a GENUINE Ruling 40 exists (the tower held entire). A "Ruling 40" about F.4.2,
withdrawn counts or a 0.09:1 ratio is the false one.

**CHAT NUMBERING DRIFTS BY ONE AT HANDOFF-22**, which numbers itself chat 20 where the index counts
19 sessions (Rebuild 1–12, then 13–19). This handoff calls itself chat 21 to stay continuous with
the prompts. **Build number and Register range are the operative identifiers.** Not chased further.

## 1. INSTRUMENTS — 24 .py. NONE ADDED, EDITED OR REMOVED THIS CHAT.
**RULING 41 CLOSES THE MISSING-INSTRUMENT QUESTION PERMANENTLY.** guard.py, press_all.py, mkref.py,
figs.py, pageproof.py, ratios.py, regsize.py, indices.py, mathreg.py, mathverify.py, compendium.py,
store_gen.py, RESTORE-PACKS.md all lived in deleted chats and are NOT recoverable. Two dispositions:
REBUILT FROM SCRATCH under a ruling, or IGNORED. Do not search Drive. Do not ask the author.
`appf.py` is RETIRED, not deleted — dead code, do not call it.
**BOARD.md IS NOT A MEMBER of BUILD-22 — measured. Nothing in this project edits against it.**

**ref.docx IS NOT IN THE BUNDLE and must be rebuilt before any press. USE W-013's CORRECTED RECIPE**
(WORKING-REGISTER.md ~line 1549), NOT HANDOFF-20 §1's, which is wrong in three places:
  (i) `<w:sectPr />` SERIALISES WITH A SPACE — match BY ELEMENT NAME with a regex anchor.
  (ii) docDefaults already carries `w:sz`/`w:szCs` at 24 — REPLACE, do not insert.
  (iii) the fonts are THEME attributes (`w:asciiTheme` etc.) — 48 of them; converting only the 3
        plain ones yields a ref.docx that is NOT Georgia at the document default.

**FIGURES — STILL NOT FETCHED. OWED SINCE CHAT 19; NOW THE OLDEST OPEN PRODUCTION ITEM.**
`The_Method_1_6_figures_BUILD13.zip`, Drive id `1q7pvnxMPILD9AVoH6XjymZHXX79YzITd`, 6,299,293 bytes.
Connector writes large results to `/mnt/user-data/tool_results/<id>.json`; decode with
`json.loads(d[0]['text'])['content']` → b64decode. Unzip into `/home/claude/build/`:
`figures/` (49), `figures-compendia/` (12). Five figures are known absent without it.

**COORDINATES-2.13 — SUPPLIED, DO NOT ASK AGAIN.** `/mnt/project/COORDINATES-2_13.csv`,
10,912,381 bytes. THE CONNECTOR REFUSES IT (10 MB cap). Not a bundle member. coords.py gates
Spectra automatically inside build.py.

**PRESS INVOCATIONS.** The digit is LAST in argv; it is index_pages.py's DEPTH.
  main      `python3 build.py The_Method_1_6-2.md OUT/main.docx "The Method 1.6" strip pages 2`
  Register  `python3 build.py …The_Register-2.md OUT/register.docx "…— The Register" fix 0`
            **NO `pages`. RULING 38. SETTLED TWICE — do not re-derive it a third time.**
  math/phys/ioi/spectra  `python3 build.py <src> OUT/<x>.docx "<title>" pages 2`
  Register afterwards: `soffice --headless --convert-to pdf --outdir OUT OUT/register.docx`

## 2. WHAT CLOSED THIS CHAT — W-017, VERBATIM IN WORKING-REGISTER.md
**MATH-01 IS RESOLVED TO AN IDENTIFICATION AND ONE OWED VERIFICATION.**
**T HAS FIVE NAMESPACES, NOT FOUR.** Board rows · session tests · dotted `T.` compendium objects ·
disk artefacts · **and `T` + space + locator = A BIBLIOGRAPHIC SOURCE KEY**, which is the one
MATH-01 is about: 37 uses in Math, 2 in main, 6 in the Register. Disambiguation rule in W-017.
A register-number rule FAILS — `T §8.2` sits at R1375/1535/1551.
**T IS "THE COMPANION" — MEASURED.** `W.face` body: *"the companion's local null surface is a FACE
of the 6-cube"*; its grade line sources that same statement to `T §10.1, §10.4`. One line apart.
**T'S APPARATUS:** §§1–10 (§10.4c), A1–A5 + A14–A18, C1eq–C5eq, D1 + D7–D10, E0–E5, F1/F2/F6/F7,
`T audit 27`. **NOT CONTIGUOUS — gaps at A6–A13, D2–D6, E3, F3–F5.** A contiguity argument for
"one document" is NOT available on this evidence and must not be repeated as if it were.
**IDENTIFICATION, INFERRED NOT MEASURED:** T = `On the Matter of Time Travel: the clock in the
constraint`, Lach & Claude 2026, 25,000 words, 43 sections, registers 344–346 (main §R.3).

## 3. CHAT 22 OPENS HERE — THE VERIFICATION THAT CLOSES MATH-01
**The author placed the paper in Drive at 2026-08-26T14:33Z, AFTER this session's Drive sweep.**
  `On_the_Matter_of_Time_Travel.pdf` — id `11PaIIC8l6v-_QTDczkxh9cWTA5YVRwCj`, 1,619,880 bytes.
  Two further new files, UNEXAMINED and unruled:
  `theory_of_everything_expanded_formalism.pdf` id `1rMUDhfMyT5sxPxKT3X8it-7ymEdpNvK6` (31,759 B)
  `Everything_we_can_see,_touch,_or_detect_using_elec....pdf` id `1xKvugHqahCHKs1DsaTlDwCZqmxmR1sna`
  (688,239 B)
**THE TEST, three questions, and it is cheap:** does the paper carry sections to §10 with a
**§10.4c**; an appendix **E0–E5**; and an **audit 27**? Three yes → T is MEASURED, MATH-01 closes,
and the standing question 1 is answered. Numbering disagrees → **the identification is WRONG
however well the subject fits**, and the honest report says so.
**METHOD, so context is not lost to it:** at 1.6 MB the connector should write to
`/mnt/user-data/tool_results/<id>.json` rather than inline. Decode in the container, extract with
pdftotext, and **grep for the three markers — do NOT read 25,000 words into context.**
A 1.6 MB inline arrival would end a session; do this EARLY, not at 88%.

## 4. FAULTS AND NEAR-FAULTS OF MINE THIS CHAT
  (i)  **I arrived holding the false state in memory** and said so before the gate, rather than
       acting on it. Recorded because the channel is new.
  (ii) **The press was not run and the figures were not fetched** — owed since chat 19, a third
       consecutive session. Stated, not implied.
  (iii) **The fourteen standing questions were not worked through.** Question 1 (what is T)
       consumed the session and is answered but not closed. THIRTEEN REMAIN.
  (iv) **Ruling 42's site list was not put to the author.** Not started.

## 5. OPEN, IN ORDER, FOR CHAT 22
1. **VERIFY T** against the PDF — §3 above. Then put question 1's answer to the author and close it.
2. **THE REMAINING THIRTEEN STANDING QUESTIONS**, one at a time, in few words, no batching.
   HANDOFF-22 §5B carries all fourteen; item 1 is now answered. **A SIXTEENTH IS ADDED BY W-017:**
   if T is a real paper the author holds, do M/R/T get a legend expanding them? Ruling 42 does NOT
   reach it — T is a SOURCE, not machinery, and a reader can go and get a source.
3. **PUT RULING 42's SITE LIST TO THE AUTHOR** — 29 non-Register lines (main 10 · Math 12 · IoI 3 ·
   Physics 2 · Spectra 2); the 96 Register lines are almost certainly out of scope under Ruling 27.
   Then execute. **THIS WOULD BE THE FIRST VOLUME CHANGE IN FIVE CHATS.** Whether an editorial
   removal earns a Register entry is §5B item 15 and BLOCKS this.
4. **FETCH THE FIGURES AND PRESS ALL SIX VOLUMES.** Rebuild ref.docx first, corrected recipe.
5. **A4's READER READ** (mechanical layer closed at W-016; the reader read was never opened),
   then **A5 the Register**, then **A6 the main volume LAST.**
   All findings to WORKING-REGISTER.md, NEVER to the Register.
6. SCHEDULED, NOT NOW: WP-1 Appendix F, WP-2 the Register's front matter, Ruling 31's renumber.

## 6. DO NOT START WITHOUT M's RULING
- **The tower — HELD ENTIRE by Ruling 40 until A4 and A6 report.** Ruling 39 is NOT withdrawn and
  NOT executed; its steps 1–3 STAND AS DONE and are not to be re-derived. ZERO SITES EDITED.
- **Ruling 42's removals** — the site list goes to the author first.
- The 126 unreconciled Spectra rows. The five narrow-bracket FAIL rows named in R1763.
- **Rebuilding ANY deleted instrument — Ruling 41.** indices.py matters most.
- The 1,447 / 1,472 count question (HELD by M at PR1 — report if it moves, do not re-ask).
- Any re-sort of the Spectra channel table (SPEC-06) — reader-visible and press-hazardous.
- The renumber (Ruling 31) and Appendix F's rebuild (Ruling 30) — scheduled, neither open.
- **Register navigation — CLOSED BY RULING 38. Do not raise it again.**
- register_cites.py parses ENTRY BODIES ONLY, so a citation in the Register's front matter is
  invisible to it (this is how 1732 was missed in chat 14). Unrepaired.
- **The two unexamined new Drive PDFs** — do not absorb, cite or act on them without a ruling.