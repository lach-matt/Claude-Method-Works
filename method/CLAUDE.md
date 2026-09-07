# CLAUDE.md — The Method 1.6 (Matthew Lach, "M")

Consolidated from the standing prompt block, RULINGS-R2.md (append-only member, md5 5df68594…), HANDOFF-28 and the working discipline of chats 62–76. Where this file and a later ruling in RULINGS-R2.md disagree, the ruling governs. This file is a project instruction, not a bundle member: never add it to a build.

**Store change (M's ruling, chat 151).** The store of record is now this git repository, not Drive.
Everything the gate reads is a file in the checkout; nothing is fetched from Drive to open a chat.
Section 0 below governs. Drive remains the archive and the original-input witness (Ruling 56); it is
no longer on the read path.

## 0. Where everything is read from

- **SUSPENDED — read this first.** At chat 151-B's open **M suspended the chat-150 ruling that the
  repository is the store of record, for as long as GitHub is unreachable from Cowork** (`W-190`).
  The standing loop is now: a chat **opens from Drive**, works with Graphify as the substrate for
  state and cross-check, and **closes by writing only the small build parts and the handoff back to
  Drive**. The reasons were measured, not assumed (`W-190`, `DEF-151` item 10): from Cowork the
  GitHub App token 404s this private repository even with all repositories granted, no `add_repo`
  is provisioned, and Drive does not resolve from the container at all. The rest of this section
  describes how the repository store works and applies **whenever a session can reach GitHub** — it
  is how BUILD181 and BUILD182 were carried back here — but it does not describe where a Cowork
  chat closes.
- **The repository as store.** `method/` holds the two live bundles, `method/members/`
  holds all 424 members extracted from them byte-exact, and `method/MEMBER-INDEX.tsv` records
  every member's bundle, size, md5 and byte offset in that bundle.
- **The tree is a witness, not a convenience copy.** `python3 method/verify.py` checks every member
  against its recorded size and md5, then splices every member back into its bundle at the recorded
  offset and asserts the bundle's own md5. A checkout that passes it provably reproduces what the
  old Drive gate used to extract. It is the first thing the gate runs and a FAIL stops the chat.
- **Instruments read members by name from `method/members/`**, exactly as before. No instrument
  changes: they were always written to read a member by name and never a bundle path.
- **Drive is still the archive.** `The Method Materials`
  (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`) and `Prints & Proofs`
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, the original-input witness under Ruling 56) are unchanged
  and are mirrored read-only under `drive/`. Read them for provenance questions, never to open a chat.
- **Two container chores before the gate, both in `method/bin/`.** `./method/bin/stage-gate` symlinks
  the tree to `/home/claude`, because `census.py` is a seated member that hard-codes
  `/home/claude/members/`; and `export PATH="$PWD/method/bin:$PATH"` puts a Python ≥ 3.12 in front,
  because `gate.py` runs instruments as `python3 NAME.py` and several do not parse under 3.11.
  `numpy` and `sympy` must be installed. `method/README.md` has the commands.
- **`BUILDNNN-PARTS` is NOT retired.** This section once said it was, on the reasoning that git has
  no upload limit. That holds only for a session that can reach git. Under the suspension above the
  close goes to Drive, whose connector takes content inline only, so the parts split is back and in
  use — `BUILD181-PARTS`, `BUILD182-PARTS`, `BUILD183-PARTS`. Chat 151-B also established that
  `create_file` accepts **`base64Content`** with `disableConversionToGoogleType: true`, which cannot
  carry the corruption `textContent` could, so two parts now suffice where four were needed.
  Each folder carries a `REBUILD-BUILDNNN.md`: the bundle is never uploaded, its **derivation** is,
  with an md5 on every input and every step.

## 1. Role and prime directives

- **Executorial role.** Execute precisely; do not decide. Every subject-matter and editorial decision belongs to M. Instrument design decisions belong to Claude.
- **Read everything before doing anything.** Review the project knowledge (list it; the BUILD12/BUILD53 bundles there are superseded — never read them), the uploaded handoff, and the recent chats before any action. Questions answerable by reading the files are never escalated to M.
- **Follow every directive contained in the subject matter of the books as well as the prompt.** No exceptions.
- **Prime Zeno directive.** Every action — fetch, read, compute, build — runs in Zeno segments: fetch/search → read/encode → analysis/computation → address/close downstream flags → interpretation/report. Each step is closed (files written, md5s measured, golden banked) before the next opens. Never leave a segment half-done.
- **Prime handoff directive.** State when context reaches 90 %+ and hand off. Handoff at 90–95 % of context or on a closed segment — never earlier, never mid-segment; begin the close when the remaining context would not fit a segment plus the close (≈ 5 %, INFERRED), and record the estimate in the W-NNN entry. A handoff is self-identifying (its chat number, build number and Register range must agree with the files), carries every tool needed to continue, condenses to as few files as possible, and comes with Drive instructions (upload / retire / keep) and the exact opening prompt for the next chat.
- **Baseline for authentication:** the Google Drive "Prints & Proofs" folder (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) is the original-input witness (Ruling 56). Materials / restore packs: `1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`.

## 2. The project

- Six reader-facing volumes: main volume (with the Register appended in the main bundle), Register, Mathematical Compendium, Physics Compendium, Index of Indices, Spectra Compendium; companion papers; audits.
- Central object: Λ₈ (976 cells, 8 coordinates, 7 Heaviside constraints) and the tower Λ₉ … Λ₁₃ (1,654 / 2,535 / 13,585 / 70,905 / 199,130), rebuilt by tower-2.py (md5 c0bce27a…) at caps (n_max, e_max, ℓ_max, k_max, f_max) = (3, 3, 1, 3, 1).
- **Two registers, never confused.** The Register (a compendium) records subject matter only — the thought process and proof of work of the books; it is cited in the other volumes. The working register (WORKING-REGISTER.md, a bundle member) is the audit log: every reader-perspective audit (including the book's own §23–25 class), every editorial entry, every finding, goes there and is forbidden from the books.
- The Löwdin and three-body papers were absorbed into the books, not rebuilt. **The standing block's "Phase 0–4" Löwdin/three-body plan is executed carried state** (Chapters 35–36 seated at main-member L9716/L9892; Register 1701–1724): discard it per Ruling 41; never re-open it or put it to M.
- This project is for constructing the drafts. Reader-perspective audits of the drafts are essential and belong in the working register.

## 3. Current state (live files as of W-249, MEASURED in the repo on 7 September 2026)

- **This section was rewritten on M's order of 6 September 2026** (*"yes. reassess R3 in full"*) because it had
  gone sixteen main builds and thirty-eight compendia builds out of date and named instruments and gate steps the
  store had replaced. `method/R3-REASSESSED.md` carries the reassessment and the before/after table; what follows
  is what the gate reports on the live pair. **`method/README.md` carries the operative gate procedure** and is
  kept current with the store; where it and §6 below differ, README governs.
- **Live files, both in `method/` and asserted by `method/verify.py`: BUILD127 main** (2,136,245 B ·
  `dad1af971146d2979314fe622e1f7c9f` · 18,905 lines · 2 members) and **BUILD284 compendia** (16,472,247 B ·
  `2f3f73f618f5d94d62f89ea23470410e` · 143,859 lines · 751 members). **753 members in all.** **The Register runs
  1 to 1889, 1,731 seated** (1,724 numbered + 7 grouped). **W-289 seated.**
- **BUILD277 TO BUILD283 ARE THE FIRST REPAIRS TO A READER-FACING VOLUME SINCE THE CHAT-67 HOLD**, on M's three
  rulings of 7 September, and **none of them could have been made when the leg began**: `close.py` refuses any
  change to a seated member, `close_main.py` writes only the Register, `close_rebank.py` only a golden and
  `close_census.py` only the census, so **a compendium had no route into the store of record at all.**
  `tools/close_vol.py` is that fourth route (W-282) — count-asserted substitutions, no member added or removed,
  the W text appended in the same build, and a reverse guard that must reproduce the old bundle's md5.
  BUILD278 seats the two determinate corrections (W-283); BUILD279 the Ruling 46 / 45 pass, **thirty
  substitutions over all four compendia** (W-284); BUILD280 closes the census, which moves on one row (W-285);
  BUILD281 seats the one site the pass missed, `close_L.py`, whose capital letter defeats `compendia.py`'s own
  pattern (W-286); BUILD282 seats `proofs/handlemap.py` (W-287); BUILD283 re-banks **eleven goldens by running
  them** (W-288). **After the pass the four volumes print no script name, no data-file name and no build
  stamp**; the seventeen sites that remain under `r2-ch16r2`'s wider pattern are figure image paths and are
  refused with their reason.
- **THE HANDLE RULING IS MEASURED AND NOT EXECUTED, AND `method/HANDLE-MAP.tsv` IS WHY.** 265 handles at 417
  Mathematical Compendium sites — 407 of them one column of one table — and 76 more in the main volume, with
  **no key printed anywhere and the generator not held.** The obvious resolution, that a family's objects are
  printed in handle order, **is false and the volume refutes it**: 3B is nine objects and nine handles in
  MEANING order, W is nine and nine in handle order, and nothing says which a family is. Resolved order-free
  instead: **112 RESOLVED, 55 AMBIGUOUS, 98 UNRESOLVED**, and by bibliography site **178 of 407 supported**.
  The table is written for approval, not applied.
- **M THEN RULED THE HANDLE MAP STALE AND THE MAP MINE TO BUILD (W-289), AND THAT CHANGED THE OBJECT.** The
  bibliography's own opening line says what its objects column is — *"Every object of this compendium names a
  work … with the objects each carries"* — so the column is the **inverse of the attributions the objects
  already carry**, on their grade lines and in their prior-art quotes. `proofs/bibindex.py` derives it:
  **127 of 162 rows DERIVED, 12 YEAR-DIFFERS, 7 NAME-FORM, 16 NOT-ATTRIBUTED**, into
  `method/BIBLIOGRAPHY-OBJECTS.tsv`, each object by its descriptive title. **The cross-check confirms M's
  ruling by measurement**: of 145 legible handle titles on derivable rows, 134 agree, and on all eleven that
  do not the derived answer is the object the work is named for — `Borchers 1992` to *Borchers 1992 /
  Wiesbrock 1993*, `Karp 1972` to *The seed is a set cover*. **An attribution is not a mention**: widening to
  an object's body prose reaches 129 and the two extra are kept out. **Fifteen works are named nowhere in any
  object entry**, this work's own two companion papers among them.
- **AND W-281's "FALSE BY 34" IS CORRECTED TO 12 (W-289).** The measurement stands — 34 objects carry no
  handle — but the label was wrong: **twelve objects name no work**, and `bibindex.py` names all twelve.
- **A figure in this section was wrong for one commit and is corrected here rather than quietly.** It named
  BUILD238 at 15,193,016 B / `7d9d0af1…`, which is a bundle that was **discarded before it was ever seated**:
  the first `close_rebank` run carried a W text saying sixty-six goldens where the count is sixty-seven, so it
  was thrown away and rebuilt, and the figures came from the discarded run's report. The seated BUILD238 was
  15,193,022 B / `4ff7ccaa…`, and W-245's close supersedes it. **The stale figure was caught by the next close
  asserting its predecessor's md5** — which is what the reverse guard is for.
- **THE GATE IS GREEN ON EVERY STEP THE STORE TREATS AS LIVE.** MEASURED 7 September: `python3 method/verify.py`
  VERIFY OK (753 members, both bundles recovered by splicing); `gate.py run --core` **5 OK**;
  **That figure read 742 for several builds and no instrument pinned it** — `docfigures.py` pins the member
  count against `MEMBER-INDEX.tsv` from CLAUDE.md at the repository root and not from this line, so this one
  drifted silently through three closes. Corrected here rather than quietly.

  `tools/gate_live.py --census` **OK**, the seated census a fixed point (1,638 rows, 3 carried retired, 1,635
  regenerated exactly, 0 NEW, 0 GONE, md5 `dbc3d6d6a8d6d925b64a7bfd2037aa49` equal to the seated member);
  **The live set is 85 from BUILD121**: `r2-26c2` is held with successor `r2-26c3` owed, because register 1868
  names the method ratio and so joins 296 in that instrument's pinned list — a record outgrowing a pin, which is
  `r2-26b`'s shape and takes a successor rather than an edit (W-260).
  `gate.py manifest --main … --comp …` **OK**;
  `tools/gate_live.py` over the 85 live goldens **86 OK, 0 FAIL** at BUILD127/BUILD284 counting the census
  step, registers 1886-1889's **33** moved goldens having been censused and then re-banked by running (W-279).
  **Two builds were seated before one re-bank**, which is the cheaper order when neither moves a line reference:
  BUILD126 and BUILD127 both append only, so of the Register's 6,984 lines exactly eight differ in the common
  range and **the shift class is ruled out structurally for the second build running**. One residue is `reg8-B`
  recurring for the reason it recurred before — **657 left the withdrawn-numbers-in-front-matter list and 1731
  entered**, and neither is a fact about a withdrawn entry: 657 was inside "1,657 entry headings" and 1731 is
  inside "1,731 entries". A third confirmation of the digit-coincidence class.
  The previous verdict: **86 OK, 0 FAIL** at BUILD125/BUILD268,
  registers 1880-1885's 36 moved goldens censused and re-banked by running (W-272).
  **That census needed no shift window at all** — the first of this leg for which the shift class was ruled
  out STRUCTURALLY rather than checked: of 6,961 Register lines exactly nine differ in the common range, all
  of them front-matter counts, and nothing before the append moved. **One residue fell and is the same
  numerator over a larger denominator**: 16.0 % → 15.9 %, the split-headline class at 275 entries before and
  after, while the same instrument's pinned odd-asterisk class held at 22 — the emphasis-parity guard doing
  its work on six new entries. **And one residue is a consequence of seating**: entry 1885 carries *Prior art:
  Routh 1875* and the References have no Routh, so this build added one to the standing cited-but-
  unbibliographed class the prose pass owns. **The census close came AFTER the re-bank here and that is the
  wrong order, and it cost a cycle** (W-273, corrected by W-274). **W-273 claimed no live golden reads the
  census and that the confirming gate proved it. Both halves are false**: `r2-bib2` prints the census md5 and
  `r2-ch16t3` its row count, and the gate passed only BECAUSE the re-bank had just aligned both sides of a
  stale census. **A gate that passes is not evidence a dependency is absent when the re-bank has aligned both
  sides of it.** The two were re-banked at BUILD269 and the order — census first, then the re-bank — now has a
  measured instance behind it rather than an argument.
  The previous verdict: **86 OK, 0 FAIL** at BUILD124/BUILD265,
  register 1876-1879's 64 moved goldens censused and re-banked by running (W-270).
  **That census is the largest of this leg and every one of its thirty residues was read**, because the ≥ 7
  table grew by two rows at L47 and shifted every Register line below it by two. One residue is worth keeping:
  `r2-ch16f2`'s six-volume count for the token `18` FELL, 140 → 139, with nothing deleted from any volume — the
  lost site is the front matter's own *"the **18** cited seven times or more"*, now *"the 20"*. **A count that
  fell because the sentence naming the table's size was itself one of the sites counted.**
  The earlier verdict: **86 OK, 0 FAIL** at BUILD118/BUILD250,
  register 1853's 33 moved goldens having been censused and then re-banked by running (W-255).
  At BUILD117/BUILD247, before this leg's second re-bank, it read **56 OK, 30 FAIL**, and the 30
  were exactly the set the diff census had already traced to registers 1849-1852 — every one of them, with the
  new entries' own site tallies landing only at Register lines 6844 and 6848, which are 1851 and 1852
  themselves; all 30 were re-banked at BUILD248 by RUNNING their instruments, change set proved to be
  `{MANIFEST.tsv, WORKING-REGISTER.md, the 30 goldens}` and the reverse guard recovering BUILD247's md5 (W-253).
  **The main volume's md5 moves on a Batch B append and its byte count does not**, because §28 carries the
  Register's own counts and they are re-taken in the same build: a build that seated entries and left the main
  md5 alone would mean the counts had NOT been re-taken. The earlier figures for the first re-bank: at
  BUILD116/BUILD245 it read **49 OK, 37 FAIL**, and the 37 were exactly the set the census had traced to
  registers 1842-1848; all 37 were re-banked at BUILD246 by
  RUNNING their instruments, under `close_rebank.py`'s guards — change set proved to be
  `{MANIFEST.tsv, WORKING-REGISTER.md, the 37 goldens}` and nothing else, reverse guard recovering BUILD245's
  own md5 (W-251). **This line was left unpinned for one commit** while that confirming walk ran, and says so
  because a verdict this section has not measured is not a verdict it may carry.
- **RUN THE GATE WITH `method/bin` ON PATH, and this is not advice.** `gate.py` runs every instrument as
  **`python3 NAME.py`, hard-coded**, and ten seated members do not parse before 3.12. Without the shim four
  goldens — `archive-split`, `r2-ch16n3`, `r2-ch16u4`, `r2-tools-constants` — differ from their banked output
  **by a `SyntaxError` traceback and are reported FAIL**, which is how a gate run at BUILD116 read 41 failures
  where the true count is 37. `close_rebank.py` regenerates by RUNNING, so a re-bank of those four **would have
  banked the tracebacks as the goldens**, and `verify.py` and the census would both have passed afterwards. The
  diff census W-200 requires before any re-bank is what caught it.
- **THE OLD "56 READINGS" ARE EIGHT HELD INSTRUMENTS, EACH WITH A STATED REASON**, and the sentence this section
  used to carry — *"KNOWN RED, and it is now 56, not three"* — is closed. Held: `r2-26b` (UNRUNNABLE, successor
  `r2-26b2` owed), `r2-ch18b` · `r2-ch23a` · `r2-ch23b` · `r2-ch28a` (readings, not re-banks, DEF-153B),
  `r2-reg11a2` · `r2-reg12b` (census rows keyed by Register line, W-224), `r3-wl` (re-taken by `r3-wl2`).
  `tools/gate_live.py --list` prints the live set and the reason every other golden is left out; the superseded
  predecessors stay seated and red by design until the archive pass (Phase 0 ruling 13).
- **THE GATE'S OWN TOOLS HAVE MOVED, and this section named the retired ones.** `gate.py census` **stays red by
  construction** — the live census step is `tools/gate_live.py --census`. `gate.py run --all` reports nothing the
  held list does not; `tools/gate_live.py` is the live walk. `shiftcheck.py` **cannot sort a Register-line shift**
  (132 of 136 UNEXPLAINED at W-234) and is superseded for that job by `tools/shiftinv.py`,
  `tools/shiftcheck2.py`, `tools/reanchor.py` and `tools/proveanchor.py`. `r2-28b3.py` sits in `members/` in no
  bundle, superseded by `r2-28b4`, left in place by ruling.
- **R3 IS COMPLETE, and its successor is approved and seated.** DEF-152's ten items (entries 1807–1813), the
  withdrawn-law and arithmetic classes (1798–1800), reg1-04 repaired with its class (1815), the positional class
  closed by generator (forty-four successors proved byte-exact), **Q5 in full** (1821–1835, every figure
  re-derived by a standard-library instrument before its entry was written), the census made content-keyed
  (`census2.py`, `close_census2.py`), and every tool in the repository seated as a member (W-236). The running
  account is `DEF-153O-PENDING.md`.
- **THE CHAT-67 HOLD IS OFF ITS FIRST SITE, ONE RULING AT A TIME.** `RULINGS-R4f` §5 item 3 was specified before
  it was executed — `DRAFT-R4-R3-CORRECTIONS.md` measures every site of rulings 2, 3, 9, 10, 11 and 12 and sorts
  them into what is mechanical, what is blocked on M's prose and what touches no volume — and M was then asked one
  question at a time. **Rulings 11 and 12 are executed** (6 September): §34.4 takes §34.8's *"in the form"*
  (register 1836, `r4-a1.py`, W-240), and §35.2 and §35.5 take the wider bound **no g block through Z = 125**
  (register 1837, `r4-a2.py`, W-241 and W-242), and the four sites outside §35 that ruling 12's own rule reaches
  follow at register 1838 (`r4-a3.py`, W-243 and W-244) — **the first build in this pass to move both bundles at
  once**, because a volume may not change unless a Register entry in the same build records it and the sites and
  the entry are in different bundles. Each is one guarded build with the count classes re-taken in it and the
  moved goldens re-banked by running — **33, then 34, then 67 of the 86**, the last because register 1704 crossed
  to seven citations and the front matter's table gained a row, shifting every Register line from L50 by one.
- **AND THE CENSUS FOUND WHAT THE SECOND REPAIR COSTS, UNPROMPTED.** Regenerated at W-241 it grew to 1,613 rows
  with **6 NEW**, and the first is not an artefact: `C6-NUMBERS-NOT-IN-SOURCE` at Mathematical Compendium L3178,
  whose *pinned-channel theorem* cites §35 and register 1704 and still prints the bound as Z = 121. **Four sites
  outside §35 now disagree with the volume they cite** — that entry and `THE-LOWDIN-SOLUTION-2.md` L13, L47 and
  L114. **M: *"this is obviously yes, and did not require a ruling from me"*** — the four are repaired at W-243,
  the row is GONE at the next regeneration, and **census id 1610 is retired on M's ruling**, carried verbatim with
  the mark `RETIRED W-243: not measured at this build`. **Batch A is discharged**, and rulings 9 and 10 followed at W-245 as work matter, leaving only
  2, 3 and 5 — one site, §34.7 and register 1337, whose repair is prose and is M's.
- **AND `docs/R3-REPAIR-PLAN.md` IS FINISHED** (M: *"complete R3 please"* and then *"don't tell me R3 is
  finished until it is"*; W-246, W-247, W-248; `method/R3-COMPLETION.md`). The pass named R3 was already
  complete; the twenty-five-row retraction plan carrying the name had never been worked and **did not know
  its own state**. **All twenty-one items are now disposed**: **twelve were already done and not one by this
  plan**; **three corrections do not survive the record** (B4 is its own `CORRECTION-SUPERSEDED` row, B9 is
  aimed at a claim register 1148 does not make, B10's site was settled by ruling 9); **two are REFUSED on the
  standing rule** that a recorded finding is never withdrawn on reconstructed evidence without the original
  instrument (B3, whose data lived in a chat container, and B7, which the seated `cypher.py` positively
  contradicts); **one is scoped to the prose pass by register 1790** (A5); **two are measured and recorded**
  (A6 repaired at three sites with register 1840, A8 measured with register 1841); **and one is seated**,
  register 1839, the 1983 Kitagawara & Barut priority register 1450's own literature search missed by one
  paper. **Three instruments were built to do it** — `coupling.py` (§12.11.2's triangle paragraph, six of
  six), `composab.py` (the compendium's composability series, four of six), `cgraph.py` (the constraint
  graph, every one of register 1790's numbers) — and each carries a selftest against the corpus's own
  recorded figures.
- **THE STORE CARRIES ITS OWN GOVERNANCE, AND THAT WAS OWED BEFORE ANY OF THE WORK DONE UNDER IT** (W-249,
  M: *"everything you just asked about finishing has already been ruled. it all must be done."*).
  **Seventy-one members seated**: `RULINGS-R4b.md` … `RULINGS-R4f.md`, `SETTLED-R4.tsv`,
  **`FINDING-R4-01` … `FINDING-R4-25`** — M's ruling answers the question this section used to leave open,
  and the withdrawn findings are seated with the standing ones because a withdrawal that leaves no trace is
  not a record — `R3-REASSESSED.md`, `R4-READINESS.md`, `R3-COMPLETION.md`, the five `r4-a*.py` build
  instruments, twenty-six `method/proofs/` measurement instruments, and the six `tools/` instruments still
  unseated under W-236. **A chat opening by the §0 gate could not see the rulings nine builds were made
  under**, and the store's own precedent is that a governing document the store does not carry does not hold
  (reg13-01, entry 1617). **The proofs' goldens are deliberately not seated**: `gate_live.py` enrols every
  `NAME.out` in `members/` and `gate.py` runs it from there under a 270-second ceiling, and these are
  written to run from `method/proofs/`; each is checked by its own `--selftest` instead. `CLAUDE.md`,
  `README.md`, `MEMBER-INDEX.tsv`, `verify.py`, the `W-*.md` files and R3's `DEF-153*` / `DRAFT-*` notes to
  M stay outside the bundles, as the store already had them.
- **PHASE 2 OF THE PUBLICATION PLAN HAS NO OPEN ROW LEFT: 43 DONE, 1 REFUTED, 1 PART, and one row RULED with
  its pass owed.** M gave the three rulings on 7 September and `RULINGS-R4g.md` is seated with them. BUILD125
  seats **1880–1885** (`r4-c1.py`, W-271): the Request-3 bracket result, whose reserved number 1836 a later
  build had spent — **a Register number is assigned at seating**; the agreement theorem's counterexample staged
  as 1797 and never seated, where **1797 stays a hole because a number is not reused**; and the four
  `READ-intake1.md` drafts. **M ruled entry 1880's kind is BOTH, and the mechanism is the absence of a tag**:
  `kinds.py` collapses an entry to one kind only where a trailing tag is present, and 1880 measures as
  `['a finding', 'a measurement']`. Only 105 of the seated entries carry a tag at all. Two instruments were
  built for the pass and are seated — `intake.py` (44/44), which re-runs all six delivered scripts against
  their banked logs, and `agreement.py` (17/17), which requires ℛ to return the printed **E = 36** for the
  periodic table before trusting it — and **`factor.py` is seated byte-exact** at md5 `55c518c9…`, closing the
  seated `r3-br-measure.py`'s pre-seating fallback to the mirror.
- **AND M's REASON FOR ONE OF THE THREE REORDERS THE PLAN.** *"the compendiums must be finished before the
  prose work, so the main volume pointers can be fixed during the prose phase."* The compendia close **before**
  Phase 3 opens; the main volume's pointers into them are repaired inside the prose pass rather than ahead of
  it. `RULINGS-R4g.md` §1(c) carries it.
- **PHASE 2 IS NOW COMPLETE: 45 DONE, 1 REFUTED, 0 OPEN, 0 PART.** Ruling 3(b) is worked (BUILD126, registers
  **1886–1887**, W-275) and E-012's last two items with it (BUILD127, registers **1888–1889**, W-277).
- **AND THE CHAT-WITHDRAWAL CLASS WAS BUILT ON THE WRONG TEST.** DEF-153P filed twelve entries on the ground
  that each carries no withdrawal marker *in its own first 1,500 characters*. **The store repairs by a NEW
  APPENDED entry citing the superseded one, so a correctly repaired entry carries no marker** — the test finds
  nothing exactly when the repair is right. Read the other way, by looking for a later entry that cites it AND
  carries the correction's own figure, **ten of the twelve were already repaired**: 230 by 1819, 314 by 1841,
  599 by 601, 602 by 1820, 807 by 823, 1395 by 1426, 1450 by 1839, 1461 by 1463, 1595 and 1628 by 1629. **One
  was not a withdrawal at all** — 807's chat row is a MEASUREMENT that extended its evidence, and 823 says so.
  **Three were genuinely unrepaired, and the κ withdrawal is wider than the list**: the message that withdraws
  500 and 502 withdraws 497, 498 and 499 in the same table and marks 501 as surviving. `withdrawn.py` (32/32)
  is that census; `kparent.py` (20/20) is E-012's.
- **THE ONE FINDING WORTH CARRYING OUT OF E-012**: §12.11.1 **defines** f_max as the cap on f, *"not the cell's
  own f"*, and says the bound has **one parent** — and the same chapter then writes *"K's parents are J_c and
  f"*, which is the reading register 1790's edge count is built on. Corrected, fourteen edges become thirteen
  and the cycle rank falls to (0, 0, 1, 1, 1, 1). **The triangle, the hub degree and §21.5.1's one-level
  shortfall are untouched, so 1790's finding survives its own arithmetic** (register 1889). BUILD124 seats **1876–1879** (`r4-b9.py`,
  W-268): the Compendium's equality-case gloss, register 1517's corridor census with its two wrong citations,
  §12.11.1.2's three faults, and registers 623/625 read as one fault. Three measurement instruments were built
  for it and are seated as members — `geodesic.py` (17/17), `corridors.py` (32/32), `consshare.py` (36/36) —
  each with a selftest against the corpus's own numbers, and each refusing something it could have guessed at.
  **`corridors.py` meets the "tools ahead of their member" condition head-on**: it imports the working
  `slopeaxis.py` because the seated member is eighty lines behind M's ruling of 6 September, and it ASSERTS
  that the two agree at the seated member's own convention, endpoint for endpoint, before measuring anything
  through it.
- **Drive stands at BUILD184 + BUILD90 and is reconciled once at the end**, not per build (Phase 0 ruling 15).
  `RECONCILE-153-STORE-STATE.md` in Materials states the store head and forbids opening a chat from Drive's pair.
## 4. Rulings in force

- Chat 67: every volume read in full, no editing until the review closes.
- Chat 68: instruments travel as bundle members; the gate fetches the two bundles from Drive by title; Drive is the store. **Superseded in part by M's chat-151 ruling: the repository is the store and the gate reads the checkout. Instruments still travel as bundle members — that half stands.**
- Chat 69: handoff at 90–95 % or on a closed segment.
- Chat 70 (R1): CENSUS-CLOSURES-A governs its 21 shared rows; A vocabulary (*defect / not a defect*) in every closure file; an unreferenced prior-art row is a defect; co-located stale text counts against its census row.
- Chat 72: begin the close when the remaining context would not fit a segment plus the build; record the estimate.
- Chat 74: (1) no direct bundle uploads — Drive remains the store; (2) the gate and the close are instruments (gate.py, close.py, r2lib.py, banked NAME.out goldens); (3) the handoff carries identity, bootstrap, run list, next work, Drive actions and the prompt; rulings live in RULINGS-R2.md and deferred items in DEFERRED.md.
- M's priorities: the computational audits are paramount; every stated value is recomputed; stale self-description and production classes are noted, not a concern.
- Earlier rulings still governing the books: Ruling 29 (the only Register edit class: pointer removal), 38 (the Register's front matter is a purpose statement only), 41 (false carried state is discarded without refutation), 45 (no build or editorial-process remarks in any reader-facing volume), 46 (no script names, build numbers or internal file references visible to readers), 56 (Prints & Proofs as original-input witness), W-101 (all subject matter completely true and proven).

## 5. Standing discipline (gates G0…)

- **Measure from files, never recite.** Grep every line number before it is written. Label every claim MEASURED (with the command), INFERRED, or record-carried; inferences are never carried into a handoff as fact.
- **No silent change.** A volume may not change unless a Register entry in the same build records it. Every edit is a measured diff with count-asserted substitutions and a reverse-md5 guard; build.py's SUBS six-way split is the preferred discriminator (G0x).
- **Register entries are append-only** — never removed, relocated or renumbered; a superseded entry is corrected by a new entry that cites it; both states are preserved. Moving an entry out is a deletion.
- **When a reconstruction disagrees with the record, the finding is about the reconstruction.** Never withdraw a recorded finding on reconstructed evidence without the original instrument. Never change an instrument to make a discrepancy disappear (G0c).
- **Authorised work is reported done or not done;** a shortfall is named explicitly. Silence is not completion.
- A message containing a question ends at the question mark; the next action is never announced in the same message as a question (G0, highest priority). Rulings are compact numbered lists and take effect without re-explanation.
- A defect line and its disposition are different objects; the later line governs (G0b). Re-test defects from the file, never from prior dispositions. Measure in the pressed PDF, not simulation (G0aa); census figures at press, not at source (G0w). A docket's target is a hypothesis until read and measured (G0v).
- A command that deletes does nothing else (G0e). Never hand-transcribe base64. `validate=True` on every b64decode. Simulate sweep order before asserting anchor uniqueness (G0q). "Registers N" cites and is counted by register_cites.py; "entries N" merely names (G0i).
- `timeout 280` on every call. Never copy over an existing file; list a directory before copying. Never edit a seated member in place (append-only members grow only through close.py `--append`). Remove `members/__pycache__` (delete-only call) before any census or build and after every instrument run.
- Shell is dash: text goes through python heredocs or create_file; no `<(…)`; one heredoc per call; non-ASCII grep output through python. Import tower-2.py by path via r2lib.load_tower(), never by copying.
- Instruments print no wall-clock time (goldens must be deterministic); an instrument over ~200 s is trimmed. Functions owed to r2lib are copied verbatim into the new instrument with a provenance comment until lifted (DEFERRED lists them).
- C7/C9 census rows whose flagged token is a live figure, label, or the cited section's own claim are regex artefacts (precedents 678, 680–687, 1067, 1069).

## 6. Session shape

1. **§0 gate**, each step its own call: confirm the checkout (`git -C <repo> rev-parse HEAD` and `git status --porcelain` — a dirty tree is reported before anything else); `python3 method/verify.py` (424 members and both bundle md5s — this replaces the Drive fetch, the spill decode and the extraction in one deterministic step); `gate.py census`; `gate.py run --core`; `gate.py manifest --main ../The_Method_1_6_BUILD92_main_and_register.md`; `gate.py run` on the previous chat's instruments; `gate.py cert NN`. Any FAIL stops the chat with a report. Nothing is fetched from Drive.
2. Read RULINGS-R2.md and DEFERRED.md from the members.
3. **Segments:** one or two subsections each. `r2-tools.py lines|pointers|figures|census|layout A B` (pointer regex is case-sensitive and ignores Appendix A item numbers — grep lowercase `register NNN` and `A.N` by hand); read every line; resolve every pointer to heading AND claim; grep every figure; re-measure every tower-computable claim on all cells or pairs in `members/r2-chNN.py` importing r2lib by path; write READ-chNN.md (A deviations with both texts; B verified; C incidental) and CENSUS-CLOSURES-chNN.tsv (id, verdict, reason; header only when no row is in range); bank the golden with `gate.py bank`.
4. **Close:** W-NNN.md (begins `### W-NNN —`, ends with a blank line; gate, segments, close estimate); `close.py --old … --new … --w … [--append DEFERRED.md …] --members …` (reverse must recover the old md5); HANDOFF-NN+1 in the current handoff's form; copy to outputs without overwriting; present the handoff first, then the build and the READ files; closing report of done / not done. **The close ends in the repository, not in Drive:** write the new bundle to `method/bundles/`, re-extract its members over `method/members/`, regenerate `method/MEMBER-INDEX.tsv`, run `python3 method/verify.py` until it reports VERIFY OK, then commit and push. There is nothing for M to upload.

## 7. Content standards for the books

- All subject matter completely true and proven; every figure computed on the rebuilt lattice before authoring.
- Compendium entries follow R-FORM: descriptive title → bold dense headline with §-pointers on first mention → italic scope-caps line → Proved/Computed + citation chain → blockquote Prior art. All attributions that can be made are made (R-ATTR).
- No object handles or workshop jargon in reader-facing volumes; cross-references name the object by its descriptive title with a source pointer on first mention per entry. Image captions state facts only.
- The compendium standard: comprehensive scope without filler; intuitive taxonomy with a robust index; consistent formatting; concise synthesis; unified voice; strict fact-checking; fluid cross-referencing; dual-purpose accessibility; clear visual hierarchy. Compendium canon order is the main volume's physical order; reordering and renumbering is a last step executed once after all subject matter is settled.
- kinds.py's table is recomputed after any Register entry addition; extent ("1 to NNNN") restated everywhere.

## 8. Response style

- Focused and brief; caveats short; the bulk of the response is the answer; high-level unless depth was requested. Cover the substance; skip boilerplate and redundant summaries.
- Scope rule: deliver what was asked; raise a better approach in one sentence; then proceed as asked.
- Delegation rule: large independent work only, never for self-verification, low spawn counts.
- Keep internal or system tags out of responses. Rulings are given back as numbered lists.

## 9. Tools and quirks

- Drive: large files spill to `/mnt/user-data/tool_results/<id>.json`; decode with `base64.b64decode(json.loads(json.load(open(p))[0]['text'])['content'], validate=True)`. Small files arrive inline (quoted heredoc, strip, same decode). Hard cap ≈ 10 MB. `read_file_content` mangles indentation — never for code. `parentId = '<id>'` with excludeContentSnippets lists a folder.
- Bundle member extraction: `(?:\A|\n)<<<FILE: (.*?)>>>\n(.*?)<<<END FILE: \1>>>` with `re.S` on the bundle bytes. The member body **includes its trailing newline** — ending the group at `\n<<<END FILE:` silently truncates every member by one byte and every md5 fails. `method/verify.py` is the reference implementation; reuse it rather than rewriting the regex.
- The gate no longer decodes Drive spills; `method/members/` is already on disk. `gate.py` runs instruments as `python3 NAME.py`, so `python3` must resolve to an interpreter with numpy. `gate.py` itself needs Python 3.12+ (an f-string containing a backslash does not parse under 3.11). Install numpy for both if the container lacks it.
- Build pipeline: Markdown → pandoc → LibreOffice → docx/pdf; `pdftotext -layout` drops table rows — confirm through docx XML.
- Key instruments: tower-2.py, lam8.py, build.py, kinds.py, register_cites.py, appf.py, index_pages.py, coords.py, bundle.py, split.py, gate.py, close.py, r2lib.py, r2-tools.py, census.py, minmax.py.
