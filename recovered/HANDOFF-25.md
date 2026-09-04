# THE METHOD 1.6 — HANDOFF (chat 23 → chat 24), 2026-08-26
Chat: 23. Build described: BUILD-24. Register range: 165–1770.
Those three agree with the files. Register: 1,449 entry headings · 1,474 numbers (all distinct) ·
7 grouped headings · 4 non-numeric front-matter subheads.
**TWO REGISTER ENTRIES ADDED (1769, 1770). TWO VOLUMES CHANGED — main and Mathematical — AND BOTH
CHANGES ARE RECORDED BY 1770 IN THE SAME BUILD.** First volume change in seven chats.
**Rulings 1–42 plus the R27 Amendment are in force. NO RULING ISSUED THIS CHAT** — the author's
T disposition was an instruction under standing question 16, executed, not a new ruling.

## 0. THE READING GATE — EXECUTE BEFORE ANY OTHER WORK. NO EXCEPTIONS.
It has now run ten times and found an error inside itself on nine.
  G1  recent_chats n=20; again with before= if the earliest is not reached. **21 chats: Rebuild 1–12,
      13–19, 21, 22, 23. THERE IS NO CHAT 20 — the sequence skips it. Do not hunt for it.**
  G2  Split both BUILD-24 bundles. MEASURE both. Count DECLARED, PAIRED and spurious markers
      SEPARATELY. If a bundle looks absent, RE-LIST; /mnt/project syncs late.
  G3  Read WORKING-REGISTER.md. MEASURE ITS LENGTH FIRST. **`wc -l` RETURNS 1944. The file is
      1,945 LINES — the last line is unterminated, so `wc -l` reports one less. NOT A DISAGREEMENT.**
      VERIFY, do not recite. `sed -n 'a,bp'` does not elide and is cheaper than `view`.
      It carries RULINGS 27, 28, the R27 Amendment, and 31–42 — **NOT 29 and 30**, whose verbatim
      text is in HANDOFF-16 onward. Also 114 excised headings (119 numbers, 3 grouped, lines 28–710)
      and W-001…W-019. **W-015 has no `###` heading — bold inline at line 1648. Present, not missing.**
  G4  PRINT THE CERTIFICATE. Until it prints, state NOTHING about the work, change NO file.
      CERT: chats read = N/__ · bundle members = ___ + ___ · rulings = 1–42 + amendment
            · Register entry headings = ____ · Register numbers = ____ · instruments = ____
  G5  VERIFY BUILD IDENTITY, NOT SIZE: `grep -c 'App. G' <Math>` (32) and
      `grep -c 'W-019' WORKING-REGISTER.md` (>=1). Either disagrees -> STOP and report.
  Failure mode: any count RECITED from a prompt rather than READ from a file = gate not passed.

**RECONCILIATIONS — measure once, do not treat as conflicts.** Re-measured at chat 23.
  - Register 1,453 `### ` lines - 4 front-matter subheads = 1,449 entry headings, 1,474 numbers.
    NOT the 1,447/1,472 question held at PR1; that one is untouched and stays held.
  - **EVERY FILE IN THIS PROJECT ENDS WITHOUT A NEWLINE — EXCEPT `Transitions.md`, WHICH ENDS WITH
    ONE.** It came from the bank, not from bundle.py. So `wc -l` under-reports by one for every file
    BUT that one. Main 11,750 · Register 5,895 · Math 3,471 · Physics 861 · IoI 1,947 · Spectra 1,010
    · WORKING-REGISTER 1944 · **Transitions 2,288 exactly**. The old §0's blanket statement was
    right for six volumes and wrong for T; chat 23 corrected it.
  - Excised: 114 headings, 119 numbers, THREE grouped. 69 A-production · 22 B-session · 23 C-internal.

**MEMBER COUNTS: STATE NONE IN THE OPENING PROMPT. MEASURE AT PACK TIME.** BUILD-24 measured at
chat 23: bundle 1 = 2, bundle 2 = 83, total 85, paired, zero spurious. Bundle 2 grew by one because
**Transitions.md is now a bundle member** — the paper can no longer become unreachable.

**THE FALSE STATE — RULING 41 EXPLAINS IT; DO NOT REFUTE IT AGAIN.** Ruling 40-about-F.4.2,
BUILD-25, HANDOFF-28, regsize.py, ratios.py, pageproof.py, RESTORE-PACKS.md, Register ~1,787 are
residue of chats deleted after a fatal error. **IT ARRIVED AGAIN AT CHAT 23 THROUGH THE MODEL'S
CARRIED MEMORY** — third consecutive session through that channel, now the only channel.
The gate caught it. Expect it; record it; proceed on the files.
COLLISION: a GENUINE Ruling 40 exists (the tower held entire). A "Ruling 40" about F.4.2,
withdrawn counts or a 0.09:1 ratio is the false one.

## 1. INSTRUMENTS — 24 .py. NONE ADDED, EDITED OR REMOVED THIS CHAT.
**RULING 41 CLOSES THE MISSING-INSTRUMENT QUESTION PERMANENTLY.** guard.py, press_all.py, mkref.py,
figs.py, pageproof.py, ratios.py, regsize.py, indices.py, mathreg.py, mathverify.py, compendium.py,
store_gen.py, RESTORE-PACKS.md all lived in deleted chats and are NOT recoverable. Two dispositions:
REBUILT FROM SCRATCH under a ruling, or IGNORED. Do not search Drive. Do not ask the author.
`appf.py` is RETIRED, not deleted — dead code, do not call it. It was NOT called this chat.
**guard.py DOES NOT EXIST**, so the standing "guard.py OLD NEW before any bundle" cannot run. Its
function was served this chat by: two volumes changed + entry 1770 recording both, in the same build.

**ref.docx IS NOT IN THE BUNDLE and must be rebuilt before any press. USE W-013's CORRECTED RECIPE**
(WORKING-REGISTER.md ~line 1549), NOT HANDOFF-20 §1's, which is wrong in three places:
  (i) `<w:sectPr />` SERIALISES WITH A SPACE — match BY ELEMENT NAME with a regex anchor.
  (ii) docDefaults already carries `w:sz`/`w:szCs` at 24 — REPLACE, do not insert.
  (iii) the fonts are THEME attributes (`w:asciiTheme` etc.) — 48 of them.

**FIGURES — STILL NOT FETCHED. OWED SINCE CHAT 19; NOW FIVE CONSECUTIVE SESSIONS.**
`The_Method_1_6_figures_BUILD13.zip`, Drive id `1q7pvnxMPILD9AVoH6XjymZHXX79YzITd`, 6,299,293 bytes.
Unzip into `/home/claude/build/`: `figures/` (49), `figures-compendia/` (12). Five figures known
absent without it. **Appendix G references no figure, so it does not add to this debt.**

**THE DRIVE LARGE-FILE PATH IS PROVEN — USE IT, DO NOT FEAR IT.** Any file over ~1 MB is written to
`/mnt/user-data/tool_results/<tool_call_id>.json` and NEVER arrives inline. Decode:
`d=json.load(open(p)); inner=json.loads(d[0]['text']); blob=base64.b64decode(inner['content'])`
then sha256-verify against the Drive `fileSize`. `pdftotext -layout` and `pdfinfo` are present.
**Extract to disk and grep — never read a paper into context.**

**COORDINATES-2.13 — SUPPLIED, DO NOT ASK AGAIN.** `/mnt/project/COORDINATES-2_13.csv`,
10,912,381 bytes. THE CONNECTOR REFUSES IT (10 MB cap). Not a bundle member. coords.py gates
Spectra automatically inside build.py.

**PRESS INVOCATIONS.** The digit is LAST in argv; it is index_pages.py's DEPTH.
  main      `python3 build.py The_Method_1_6-2.md OUT/main.docx "The Method 1.6" strip pages 2`
  Register  `python3 build.py ...The_Register-2.md OUT/register.docx "... — The Register" fix 0`
            **NO `pages`. RULING 38. SETTLED TWICE — do not re-derive it a third time.**
  math/phys/ioi/spectra  `python3 build.py <src> OUT/<x>.docx "<title>" pages 2`
  Register afterwards: `soffice --headless --convert-to pdf --outdir OUT OUT/register.docx`

## 2. WHAT CLOSED THIS CHAT — STANDING QUESTION 16, AND T IS NOW REACHABLE
**THE AUTHOR'S DISPOSITION, VERBATIM:** "The transition table needs to be an appendix in the book,
and appropriate comendiums. Then the T references in the books can be re-sourced." A fourth
disposition, not one of the three W-018 offered. **Executed in full.**
**THE AUTHOR PLACED `Transitions-1.md` IN PROJECT KNOWLEDGE MID-SESSION** — 121,691 bytes, byte-exact
to the record. Copied in as `Transitions.md` and IT IS NOW A BUNDLE MEMBER.

**THE CITATION CENSUS, MEASURED WITH A GUARDED PROBE — 42 CITATIONS, 30 DISTINCT LOCATORS,
ALL 30 RESOLVE, ZERO DANGLING.** main 2 prose · Register 8 prose · Math 3 prose + 29 source fields ·
**Physics, IoI and Spectra cite T NOWHERE.** The disposition therefore landed on three volumes,
not six. T has 77 sections; the book rests on 30 and the other 47 do not enter.

**APPENDIX G — "Transitions, indexed" — WRITTEN INTO THE MAIN VOLUME.** Body before `# END MATTER`
(the LAST of two occurrences — the first is the contents block), contents line after Appendix F.
A 30-row table: locator | the statement relied on | the objects that rest on it. Main 11,704 -> 11,751
lines. Appendix letters A–F were taken; G was the next free one, measured not assumed.

**34 CITATIONS RE-SOURCED — main 2 prose, Math 29 source fields + 3 prose.** Form: the T locator is
KEPT and the internal address appended — `T 1.2 (App. G)` in source fields, `T §8.2 (Appendix G)` in
prose. The origin is never erased; the address is added.
**THE REGISTER'S EIGHT DO NOT RE-SOURCE AND MUST NEVER BE MADE TO.** Entry bodies are never edited.
The author approved a draft of 1770 saying "forty-two re-source"; that was MY error, caught before
writing, and 1770 as written says thirty-four. **A wording approval is not a licence to write a
sentence the file would refute.**

**ENTRIES 1769 AND 1770 APPENDED.** 1769 corrects R 1002's archive note (R 1002 itself untouched).
1770 records the absorption. Counts driven to fixed point: 15 spelled-out + 2 numeric sites in main,
2 count lines + the kinds-table note in the Register, `kinds.py --write` recomputed at 1,449.
Two residual bare `1447` strings are `### 1447` and `(register 1447)` — entry identities, correctly
left alone.

## 3. FAULTS AND SHORTFALL OF MINE THIS CHAT
  (i)   **I arrived holding the false state in memory again** and said so before the gate.
  (ii)  **`T\\s§` matched the T of "AT"** — the Register's headlines end "...RECORDED AT §32.1.1" —
        manufacturing 11 dangling citations and inflating the census from 42 to 53. Caught by
        reading the contexts before reporting. **Third consecutive session in which an unguarded
        parser nearly produced a false finding.**
  (iii) **A co-address classifier recognised `M §` but not `M A.2`** and returned 24/5. NOT reported;
        the Register's recorded 37/32 was left standing.
  (iv)  **A lowercase `audit 27` probe returned 0 against T and would have unseated W-018's
        identification.** The string is capitalised. Re-tested before a word was said.
  (v)   **SHORTFALL — five of six open items were not started:** the twelve remaining standing
        questions, Ruling 42's site list, the figures fetch, the press (now five consecutive
        sessions with no press), and A4/A5/A6's reader reads.

## 4. OPEN, IN ORDER, FOR CHAT 24
1. **THE PRESS — FIVE SESSIONS OWED, AND NOW IT HAS NEW CONTENT TO PROVE.** Rebuild ref.docx on
   W-013's recipe, fetch the figures, press all six volumes. **Appendix G has NEVER been pressed —
   a 30-row 3-column table is exactly the shape that broke silently in chats 8 and 9. READ THE
   PRESSED PDF at Appendix G, not the source.** The contents must show Appendix G with a page number.
2. **THE REMAINING TWELVE STANDING QUESTIONS**, one at a time, few words, no batching.
   HANDOFF-22 §5B carries the list; items 1 and 16 are now answered.
3. **PUT RULING 42's SITE LIST TO THE AUTHOR** — 29 non-Register lines (main 10 · Math 12 · IoI 3 ·
   Physics 2 · Spectra 2). Then execute. Whether an editorial removal earns a Register entry is
   §5B item 15 and BLOCKS this.
4. **A4's READER READ** (mechanical layer closed at W-016), then **A5 the Register**, then **A6 the
   main volume LAST.** All findings to WORKING-REGISTER.md, NEVER to the Register.
   **A6 MUST NOW ALSO READ APPENDIX G as a reader** — it is new, unpressed and unaudited.
5. SCHEDULED, NOT NOW: WP-1 Appendix F, WP-2 the Register's front matter, Ruling 31's renumber.

## 5. DO NOT START WITHOUT M's RULING
- **The tower — HELD ENTIRE by Ruling 40 until A4 and A6 report.** Ruling 39 is NOT withdrawn and
  NOT executed; its steps 1–3 STAND AS DONE and are not to be re-derived. ZERO SITES EDITED.
- **Ruling 42's removals** — the site list goes to the author first.
- The 126 unreconciled Spectra rows. The five narrow-bracket FAIL rows named in R1763.
- **Rebuilding ANY deleted instrument — Ruling 41.** indices.py matters most.
- The 1,447 / 1,472 count question (HELD by M at PR1 — now 1,449/1,474; report if it moves, do not re-ask).
- Any re-sort of the Spectra channel table (SPEC-06) — reader-visible and press-hazardous.
- The renumber (Ruling 31) and Appendix F's rebuild (Ruling 30) — scheduled, neither open.
- **Register navigation — CLOSED BY RULING 38. Do not raise it again.**
- **The two unexamined Drive PDFs** — `theory_of_everything_expanded_formalism.pdf`
  (`1rMUDhfMyT5sxPxKT3X8it-7ymEdpNvK6`) and `Everything_we_can_see,_touch,_or_detect_using_elec....pdf`
  (`1xKvugHqahCHKs1DsaTlDwCZqmxmR1sna`). The author has said they are for a later part of the
  project. Still unruled — do not absorb, cite or act on them.
- **Whether the 47 uncited T sections should ever enter.** 1770 says they do not. If the author
  later wants T published whole as a companion, that is a NEW ruling and Appendix G stays regardless.
- register_cites.py parses ENTRY BODIES ONLY, so a citation in the Register's front matter is
  invisible to it (this is how 1732 was missed in chat 14). Unrepaired.