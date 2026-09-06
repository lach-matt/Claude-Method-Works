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

## 3. Current state (live files as of W-239, MEASURED in the repo on 6 September 2026)

- **This section was rewritten on M's order of 6 September 2026** (*"yes. reassess R3 in full"*) because it had
  gone sixteen main builds and thirty-eight compendia builds out of date and named instruments and gate steps the
  store had replaced. `method/R3-REASSESSED.md` carries the reassessment and the before/after table; what follows
  is what the gate reports on the live pair. **`method/README.md` carries the operative gate procedure** and is
  kept current with the store; where it and §6 below differ, README governs.
- **Live files, both in `method/` and asserted by `method/verify.py`: BUILD110 main** (2,054,674 B ·
  `e1264def2a04df9ac010db3f0ea90953` · 18,692 lines · 2 members) and **BUILD232 compendia** (15,170,136 B ·
  `199df6336b30801dfe6567c39cd98485` · 123,726 lines · 665 members). **667 members in all.** **The Register runs
  1 to 1835, 1,677 seated** (1,670 numbered + 7 grouped). **W-239 seated.**
- **THE GATE IS GREEN ON EVERY STEP THE STORE TREATS AS LIVE.** MEASURED 6 September: `python3 method/verify.py`
  VERIFY OK (667 members, both bundles recovered by splicing); `gate.py run --core` **5 OK**;
  `gate.py manifest --main ../The_Method_1_6_BUILD110_main_and_register.md` **OK**, 666 listed / 668 extracted;
  `tools/gate_live.py --census` **OK**, the seated census a fixed point (1,609 rows, 2 carried retired, 1,607
  regenerated exactly, 0 NEW, 0 GONE, md5 `4742c83a4dcf7d9eb1af0ee27e6b020d` equal to the seated member);
  `tools/gate_live.py` over the 86 live goldens **86 OK, 0 FAIL**.
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
- **The successor framework is `PLAN-R4-PUBLICATION.md`** — approved by M on 5 September and seated at W-239, with
  `PLAN-R4-ANNEX.tsv` (800 rows, 731 open at the survey) as its inventory and `RULINGS-R4.md` as its rulings.
  Eight phases; ten of the fifteen Phase 0 rulings given, **five outstanding and named rather than inferred**:
  3 (the nine heading-only sections, which only M can author or withdraw), 4 (entry 1797, seat or withdraw),
  6 (the language roster, dockets 20x-04 / 20x-09), 7 (the retraction and prose-only triage). **Phase 1 (the
  mathematics leg) and Phase 5 (the census) open on the rulings given.**
- **OWED, AND IT IS THE FIRST THING: five ruling documents are not in the store.** `RULINGS-R4b.md` through
  `RULINGS-R4f.md` carry M's rulings from five later sittings and exist only as working files — a chat opening by
  the §0 gate reads `RULINGS-R2.md` and `RULINGS-R4.md` and does not see them. `SETTLED-R4.tsv` (134 rows) and
  `FINDING-R4-01` … `FINDING-R4-23` are unseated with them; whether the findings are seated is M's ruling.
  **Seating the rulings comes before any phase work**, on the store's own precedent that a governing document the
  store does not carry does not hold (reg13-01, entry 1617).
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
