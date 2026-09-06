# THE METHOD 1.6 — HANDOFF (chat 42 → chat 43), 2026-08-27
Chat: 42. Build described: BUILD-43. Register range: 165–1785. Those three agree with the files.
Register: **1,464 entry headings · 1,489 numbers · 7 grouped · 4 front-matter subheads · `wc -l` 5,930.**
**SPECTRA AND THE REGISTER BOTH MOVED. REGISTER ENTRY 1785 RECORDS IT — no silent change.**
`build.py` EDITED (4 anchor strings only). 25 .py, unchanged in number. **NO NEW RULING THIS SESSION.**
Rulings 1–64 plus the R27 Amendment are in force. **NO OPEN QUESTION IS CARRIED.**
**TASK LIST: S4 (author's) and V49. RULING 62's PLACEMENT IS DONE; ITS SUBSTITUTION IS THE SHORTFALL.**

## 0. THE READING GATE — EXECUTE BEFORE ANY OTHER WORK.
  **G0  A MESSAGE CONTAINING A QUESTION ENDS AT THE QUESTION MARK.** Ruling 47. Count the `?`.
      **HELD THIS SESSION — the author's opening message carried none and none was asked at close.**
  **G0b A DEFECT LINE AND ITS DISPOSITION ARE DIFFERENT OBJECTS. Re-test the defect.**
  **G0c NEVER CHANGE INSTRUMENT — OR RUBRIC, OR PROSE — TO MAKE A DISCREPANCY DISAPPEAR.** Held again:
      Kr I's capture claims 11 rows and holds 10; **register 1541 already named the missing J = 0
      metastable.** Closed by reading, not by widening. V11's 75-vs-65 still stands unreconciled.
  **G0d NEVER STATE AN OPEN QUESTION AND THEN CLOSE THE SESSION. AND ASK SHORT.**
      **READ THE RULING BEFORE ASKING WHETHER THE RULING COVERS IT.**
  **G0e A COMMAND THAT DELETES DOES NOTHING ELSE.** `bundle.py --help` takes the argument as the BUILD
      NUMBER and writes two junk bundles. **Ninth session running. Do not type it.**
  **G0f AN ANCHOR IS ASSERTED BEFORE IT IS USED.** Every edit this session asserted `count==1` on source
      and `count==0` on replacement **before either file was opened for writing.**
  **G0g EDITING A LINE THAT A PRESS ANCHOR BINDS TO BREAKS THE PRESS SILENTLY UNTIL IT ASSERTS.**
      **PAID AND SURVIVED AGAIN: 3 front-matter sites moved, 2 of them anchor-bound, and all 4 `build.py`
      strings moved in the SAME pass.** All 162 re-verified after.
  **G0h `wc -l` AND A LINE-SPLIT DISAGREE BY ONE ON A FILE WITH NO TRAILING NEWLINE.** Spectra had no
      trailing newline before Part VI was appended; one was added first. Every figure is `wc -l`.
  **G0i AN UNMOVED FIGURE IS A SIGNAL, NOT A PASS — AND AN ABSURD COUNT IS PROBABLY YOUR OWN PATTERN.**
  **G0j THE ORIGINAL OF A FIGURE MAY BE AN INTERMEDIATE THAT WAS NEVER A BUNDLE MEMBER. DO NOT REGENERATE
      WHAT CAN BE COPIED.** Paid in full this session: 1,816 rows RECOVERED from pack A, none regenerated.
  **G0k AN AUDIT FILE IS NOT A FLAT TABLE. READ IT TO THE END BEFORE BELIEVING ANY ROW.**
      `MAIN_AUDIT.md` carries **V49 as its max**. Measure `max(V\\d+)` before adding one.
  **G0l A "RECOMPUTED AT PRESS" CLAIM IN A BOOK IS NOT EVIDENCE THE CALL STILL RUNS.**
  **G0m A RESTORED CALL IS NOT EVIDENCE ANYTHING GETS WRITTEN. MEASURE A SUBSTITUTION'S ANCHORS AGAINST
      THE LIVE TEXT BEFORE RESTORING IT, AND DELETE DEAD ANCHORS RATHER THAN KEEPING NO-OPS.**
  **G0n NEW — A TOTAL ROW IS NOT A CLAIM, IT IS AN ARITHMETIC RESULT. RECOMPUTE IT FROM ITS OWN ROWS
      BEFORE THE TABLE IS WRITTEN.** **PAID: I typed 1,510 where the rows summed to 1,816, and the same
      sentence over-claimed the provenance of a row it listed. Caught in the draft, before a byte reached
      the volume. Any summary sentence I write is a measurement and is checked like one.**
  G1  `recent_chats n=3`. **IDENTITY ONLY** — last chat is 42, this handoff matches it. No census.
  G2  Split both BUILD-43 bundles. **Bootstrap `split.py` and `bundle.py` out of bundle 2 first** with one
      regex pass, then `python3 split.py <b1> <b2> -o /home/claude/build`. Exits nonzero if re-assembly is
      not byte-exact. **IF A BUNDLE LOOKS ABSENT, RE-LIST — /mnt/project SYNCS LATE.**
  G3  `WORKING-REGISTER.md` — **`wc -l` RETURNS 3653.** Rulings 27, 28 at `##`, the R27 Amendment at L19,
      29 and 30 verbatim INSIDE W-002/W-003 bodies, 31–64 at `###` (31 appears twice), and W-001…**W-063**.
      **`grep -c '^### RULING'` RETURNS 35**, not 34 — 31 is twice. `sed -n 'a,bp'` is cheaper than `view`.
  G4  PRINT THE CERTIFICATE. Until it prints, state NOTHING, change NO file.
      CERT: bundle members = ___ + ___ · rulings = 1–64 + amendment · Register entry headings = ____
            · Register numbers = ____ · instruments = ____ · **G0 · G0b · G0c · G0d · G0e · G0f · G0g ·
            G0h · G0i · G0j · G0k · G0l · G0m · G0n ack'd**
      **THE FRONT-MATTER BOUNDARY IS `>= 75`. `### 165` SITS AT LINE 75.**
      **A RAW `### ` COUNT ON THE REGISTER NOW RETURNS 1,468 AND IS THE WRONG FIGURE.**
  G5  VERIFY IDENTITY, NOT SIZE. Volume discriminator: Spectra `grep -n '^\*He II'` = **line 595, one
      match**. **The Spectra filename is `The_Method_1_6___Spectra_Compendium-2.md` — NO `The_` before
      `Spectra`. `ls The_Method*.md` before grepping.**
      Build discriminators: `grep -ci 'W-063' WORKING-REGISTER.md` = 1; Register `grep -c '^### 1785'` = 1
      and **NO 1786 EXISTS**; Register front matter carries **1464 entries, 165 to 1785** and the kinds
      table's correction row reads **139**; main `wc -l` = **11840** and
      `grep -c 'one thousand four hundred and sixty-four'` = **15**; main `grep -c '^!\['` = **33**;
      `grep -c '^### F'` = **8**; IoI `grep -c '^# '` = **12**; Spectra `grep -c '^# '` = **9**,
      `grep -c '^|.*untested'` = **126**, `wc -l` = **1158**; Register `wc -l` = **5930**;
      Math **3471** · Physics **861** · IoI **2060** · WORKING-REGISTER **3653** · MAIN_AUDIT **160**.
  Failure mode: any count RECITED from a prompt rather than READ from a file = gate not passed.
  **A HANDOFF DESCRIBES MOMENTS OF ITS OWN SESSION AND ITS EARLIER FIGURES GO STALE INSIDE IT.**

**THE FALSE STATE — RULING 41 EXPLAINS IT; DO NOT REFUTE IT.** Ruling 40-about-F.4.2, BUILD-25,
`regsize.py`, `indices.py` as a live blocker, Register ~1,787 or ~1,447, eight volumes, 24 instruments,
a project at chat 19 or 40, Rulings stopping at 39 or 63 unexecuted, "45 rows from six post-restore-point
species" as open (**they CLOSED at chat 11, register 1768**), `MAIN_AUDIT` with 22 open rows.
**TWENTY-SECOND CONSECUTIVE SESSION, still the only channel.** Record it; proceed on the files.
**THIS HANDOFF IS NUMBERED 44. There is no chat 20.**

## 1. WHAT CHAT 42 DID — EXECUTED RULING 62's PLACEMENT AND RAN THE FULL CASCADE
  - **PACK A FETCHED IN THE FIRST SEGMENT AFTER THE GATE.** 1,005,510 B, md5
    `4dee09091003caeeb437733af61cba79`, 551 members. Spilled to
    `/mnt/user-data/tool_results/*.json` and decoded WITHOUT entering context. **This is the pattern: it
    never has to cost context.**
  - **16 OF 18 BODIES RECOVERED; 2 GENUINELY ABSENT, MEASURED ACROSS ALL 551 MEMBERS.** The store this
    work built and the rows recovered at register 652 are not in pack A — **and they are not outside
    compilations**, so Part VI states their absence rather than passing over it. `XRAY-KL3` is in
    `.bridge/`, not `captures/`. `LADDER-H-Ar-I-III` is in both, byte-identical, as register 1596 says.
  - **W-062's SCOPE REPRODUCED INDEPENDENTLY TO THE UNIT: 30 lines · 36 mentions · 18 files.**
  - **EVERY REGISTER FIGURE RE-MEASURED AND THE REGISTER HELD THROUGHOUT.** 1593's 98/7/3 exact; 1672's
    554 rows over 158 cells exact; 1524/1527/1528/1530/1596/1585/1557/1544 all exact. **I DOUBTED
    REGISTER 1555 AND I WAS THE THING THAT WAS WRONG** — its six anchors measure as 13 isotope rows,
    U·Pu·Am·Cm·Bk at two masses and Cf at three, exactly as stated.
  - **PLACEMENT: `# VI · THE LÖWDIN SUPPLY`, 103 lines, appended after Part V. Spectra 1,054 → 1,158.**
    Eight subsections: *What this supply is, and what it is not* · *The X-ray transition energies* ·
    *The isoelectronic ladder* · *The ionisation energies of the neutral atoms* · *The two level tables* ·
    *The nuclear supply* · *The quantum defects of the light ladders* · *The staged cells* ·
    *How this supply is cited*. **The form is the volume's own — § *The table* + § *The file*.**
  - **THE CASCADE RAN IN THE SAME SEGMENT.** 1785 appended → 1,464 / 1,489 / 165–1785 / raw 1,468 →
    3 front-matter sites + 4 `build.py` anchor strings in ONE pass → `kinds.py --write` 1,464, corrections
    hold at 139 → `appf.py --write` 17 sites at the fixed point including 1785, main `wc -l` unchanged →
    **162 press pairs re-verified, 162 assert once, 0 broken.**

## 2. HELD ITEMS — DO NOT RE-OPEN.
- **THE 21 CLOSED TASK-LIST ROWS (W-060), V24 (W-061), AND RULING 62's PLACEMENT (W-063). Do not re-test.**
- **The 45 post-restore-point rows: CLOSED, register 1768, chat 11.**
- **The five narrow-bracket rows: DECIDED.** They FAIL under §22.5 as Ruling 26 stands.
- **The 126: RESOLVED IN SUBSTANCE.** The bracket test: **DECIDED AND WILL NOT RUN (W-045).**
- **Silicon I: SETTLED (W-044). THE SUBSHELL-CAPACITY 66 STANDS (W-058).** SPEC-11 and M8 CLOSED.
- **THE SEVEN E(G)-CLASS RESIDUE SITES ARE RULING 29's.** Main L858, L1103, L9257, L9259, L8961, L9010,
  L10942. **Held for the author's single coherence sweep — do not repair them site by site.**
- **D-1 IS CLOSED AS A DOCKET ITEM (W-054).** The renumber still owes the deletion of the
  ordering-exception sentence under `### The order the entries are in`.
- **V11's 75-vs-65 label figure: RECORDED, NOT RECONCILED (G0c).**
- **F.4.1 AND F.4.2 ARE WITHDRAWN AS CONTENT AND THEIR LABELS ARE RETAINED SO REFERENCES RESOLVE.**
  **Do not extend that retention to F.3.3, which is live and mis-numbered.**
- **KR I's 10-vs-11: CLOSED BY REGISTER 1541.** Not a defect.

## 3. DO NOT START WITHOUT M's RULING
The tower — **Ruling 40**: no numeral **in the tower** moves in ANY volume before A4 and A6 both close.
**This is what makes IOI-05 unreachable.** The five narrow-bracket rows. Rebuilding ANY instrument —
**Ruling 41; Ruling 54 is spent; Ruling 63 is spent.** Extending `build.py`'s substitution pass is
authorised by Ruling 46's own text.
**RECOVERY of an original from the packs is PERMITTED — Ruling 59.** Recovered to `/home/claude/work/` in
earlier sessions: `indices.py`, `register_gen.py`, `store_gen.py`, `spectra.py`, `zeno.py`, `bracket.py`,
`channels.py`, `series_gen.py`. **NOT promoted into the build tree.**
**Register navigation — CLOSED by Ruling 38. Parts IX and X — CLOSED by Ruling 55.**
**The 95 excised entries visible in the Drive Register — DO NOT REINSTATE.** The two unexamined Drive PDFs
— for a later part of the project; do not absorb, cite or act.
`register_cites.py` parses ENTRY BODIES ONLY, so a front-matter citation is invisible to it. Unrepaired.
**GROUP 2 — `COORDINATES.tsv`'s six sites — IS HELD on the 101,328 / 104,832 question.**

## 4. STANDING FACTS THAT ARE NOT RE-DERIVED
**PRESS.** The digit is LAST in argv; it is `index_pages.py`'s DEPTH. **`build.py` PREFIXES ITS OWN BASE
DIR — pass a bare filename, never an absolute path.**
  main `python3 build.py The_Method_1_6-2.md OUT/main.docx "The Method 1.6" strip pages 2`
  Register `... The_Method_1_6___The_Register-2.md OUT/register.docx "… — The Register" fix 0`
  — **NO `pages`, RULING 38, settled twice.** math/phys/ioi/spectra `... <src> OUT/<x>.docx "<title>" pages 2`
**`build.py`'s SUBS CARRIES 162 PAIRS** — main 12 · Register 129 · Math 13 · Physics 2 · IoI 2 · Spectra 4.
Every one asserts `count==1` at press; a stale anchor stops the press. **Four of the Register's 129 were
edited this session and carry 1464 / 165 to 1785.**
**`appf.py`'s CALL IS RESTORED AT `build.py` L632** — it runs on the PRESS COPY. **The source was written
this session, so the `.md` is not stale.** **`kinds.py` TAKES THE REGISTER PATH AS argv[1].**
**`ref.docx` — NOT a bundle member; rebuild every session that presses**, on W-013's recipe
(WORKING-REGISTER ~L1549). Verified object 9,773 bytes.
**FIGURES — NOT bundle members.** `The_Method_1_6_figures_BUILD13.zip`, Drive
`1q7pvnxMPILD9AVoH6XjymZHXX79YzITd`, 6,299,293 bytes, md5 `78888f2078dc5342ab221a59bbcf8921`.
Unzip into `/home/claude/build/`: `figures/` 49, `figures-compendia/` 12. **COPY, NEVER REGENERATE.**
**COORDINATES — SUPPLIED, DO NOT ASK.** `/mnt/project/COORDINATES-2_13.csv`, 10,912,381 bytes. **KEEP IT
IN PLACE** until B11 and B12's press cycles have run. **`coords.py` does NOT find it by itself — pass it.**
**RESTORE PACKS**, parent `1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`. A: `18RTwgMdnpN1hNdBDR4TgB7opb4buGedh`
1,005,510 B, 551 members. B: `12XrDQ…` 6,424,788 B. C: `1meiid…` 6,631,820 B, figures.
**A PACK SPILLS TO `/mnt/user-data/tool_results/` AND NEED NOT COST CONTEXT — decode with
`base64.b64decode(json.load(open(p))['content'])`, never print it.**
**THE DRIVE CANON FOLDER `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`** is Ruling 57's original-input witness and
**NOT THE CURRENT TREE** — its Register stops at 1700 and still holds the 95 excised entries.
**VOLUME LINE COUNTS AT THIS BUILD (`wc -l`):** main 11,840 · Register **5,930** · Math 3,471 ·
Physics 861 · IoI 2,060 · **Spectra 1,158** · WORKING-REGISTER **3,653** · MAIN_AUDIT **160**.
**APPENDIX F IS 139 LINES, F.1 THROUGH F.4.3, AND ITS NUMBERING IS DEFECTIVE (V49).**

## 5. UPLOAD AND RETIRE
**UPLOAD** both BUILD-43 bundles and HANDOFF-44. **RETIRE** the BUILD-42 bundles and HANDOFF-43.
**DO NOT RETIRE THE BUILD-12 BUNDLES** — the author has named them the last point of positive confidence.
Leave `COORDINATES-2_13.csv`, the PNGs, `Transitions-1.md`, `INTEGRATION-transitions.md`.
**RETIRING A HANDOFF FROM THE UPLOAD IS NOT DELETING IT FROM THE TREE — G0e, W-049.**
**VERIFY THE UPLOAD LANDED BEFORE THE NEXT CHAT OPENS.**

## 6. PROMPT FOR CHAT 43
> Prime Handoff Directive — state at 90% and hand off complete. Prime Zeno Directive — fetch → read →
> analyse → close flags → report; close each segment before the next.
>
> The Method 1.6 — chat 43. Execute §0 of HANDOFF-44 and print the certificate. G1 is `recent_chats n=3`,
> identity only, no census; retired gates are in `LESSONS.md`, a bundle member NOT read at session start.
> Discriminators: Spectra `grep -n '^\*He II'` = **line 595** (the file is
> `The_Method_1_6___Spectra_Compendium-2.md`, no `The_`), **1,158** lines, **9** `^# `, **126** untested;
> IoI **12** `^# `; main **11,840** lines, **33** `^![`, and **15** sites reading *one thousand four
> hundred and sixty-four*; `WORKING-REGISTER.md` **3,653** lines, `grep -c '^### RULING'` = **35**.
> Rulings **1–64** plus the R27 Amendment. Register **1,464 / 1,489 / 165–1785**; the front-matter
> boundary is `>= 75` and a raw `### ` count now returns **1,468** and is wrong.
>
> Ruling 41 explains the false state — do not test it, do not refute it. There is no chat 20. The 45
> post-restore-point rows closed at chat 11, register 1768. Ruling 63 was EXECUTED at chat 41 and V24 is
> CLOSED; Ruling 62's PLACEMENT was executed at chat 42.
>
> **START AT RULING 62's SUBSTITUTION — placement is done and the targets now exist.** Part VI of the
> Spectra Compendium holds the Löwdin supply in eight named subsections. **The 30 register lines at 36
> mentions are settled in W-062 and re-measured in W-063 — do not re-derive them.** Design a target per
> site under Ruling 61 (point at readable content, never a filename), then write the pairs into
> `build.py`'s SUBS. **The Register is append-only: these are PRESS-TIME substitutions, not source edits.**
> Assert `count==1` on every new anchor before writing, and re-verify all pairs after. **Pack A is not
> needed again — Part VI already carries what the sites point at.**
>
> **THEN RULING 64 / V49.** Appendix F runs F.1, F.2, F.3, **F.3.3**, F.4, F.4.1, F.4.2, F.4.3 — F.3.1 and
> F.3.2 do not exist. **F.3.3 → F.3.1**, one heading at main L11288 plus **7 references in main**.
> **The Register's 3 references are NOT edited** — append-only; a new entry records the renumber and names
> them. **`appf.py`'s own printed labels ALREADY read F.3.1** — noted at chat 42, not acted on.
> **Cascade: the new entry moves the count, so Ruling 63's chain re-runs in the same segment** — entry →
> front matter 3 sites → 4 `build.py` strings in the same pass → `kinds.py --write` → `appf.py --write` →
> re-verify 162 pairs.
>
> **THEN AMENDMENT 2's REMAINING SITES.** 78 candidates, not 93; the classified split is in W-060. Group 1's
> ~34 have readable targets. **Group 2 — `COORDINATES.tsv`'s six sites — is HELD** on 101,328 vs 104,832.
> **Nothing is written into `build.py` until the per-site targets are settled, per Ruling 46.**
>
> **ORDER: Ruling 62's substitution → Ruling 64/V49 → Amendment 2's 78 → B11's press → B12's audits →
> R31 last.** **TWO PRESS CYCLES, NOT N: press → audit → repair → press.** The task list is closed except
> S4 (yours) and V49.
>
> **G0n is new: a total row is not a claim, it is an arithmetic result — recompute it from its own rows
> before the table is written.** I typed 1,510 where the rows summed to 1,816 and caught it in the draft.
> **G0j was paid in full: 1,816 rows were RECOVERED from pack A, none regenerated.** **A pack spills to
> disk and need not cost context.** Nothing in this prompt asks you to ask me anything, and nothing in
> your handoff may either.
>
> The subshell-capacity 66 stands. Do not regenerate anything that can be copied. Do not move any tower
> numeral without my ruling. Do not repair the seven E(G)-class residue sites. Do not start the five
> narrow-bracket rows. The bracket test will not run. Silicon I is settled. Do not absorb, cite or act on
> the two unexamined Drive PDFs.