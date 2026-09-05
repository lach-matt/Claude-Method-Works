# PLAN — from the store as it stands (BUILD110 / BUILD231, W-238) to a finalized, publishable set of the six volumes. APPROVED BY M, 5 September 2026; seated at W-239.

**M's ruling (5 September 2026):** *"approved, proceed with phase 0 rulings as recommended. however, with 2, any math
that does not resolve to the claims of this book must be flagged to me for review."* The four things §6 asks for are
approved; the Phase 0 rulings as given, and the five the plan offered no recommendation for, are recorded in
`RULINGS-R4.md`, which governs. The condition M attached to ruling 2 is a standing rule over every count this plan
touches, and is stated there. This member is rewritten by successor at each phase close; `PLAN-R4-ANNEX.tsv` is the
item inventory behind §2, one row per survey item with the phase that owns it.

Written from a survey of every record of outstanding work the store holds (the sixteen DEF-153 files, RUL-153, the
docket and its twenty-six deltas, DEFERRED.md in full, RULINGS-R2, the §0 gate text, the Working Register W-201 to
W-238, all seventy-six READ records, the census and its sixty-five closure files) and from two surveys of the six
reader-facing volumes themselves (work matter; structure), with the five audit instruments run over the store. The
survey found 800 candidate items; 731 are open.

## 1. What "publishable" has to mean here, or the plan cannot be finished

The store keeps three things apart, and the plan keeps them apart:

- **The archive** — every member ever seated, never edited, successors only. It is the record and it is not published.
- **The source volumes** — the six reader-facing members. They change only by a guarded build carrying a Register entry.
  Findings against them are recorded, never silently repaired (the chat-67 hold, lifted only class by class under R3).
- **The print edition** — what a reader holds. The archive already has a press: `build.py` (a seated member) presses
  each source volume through 261 press-time substitutions (Rulings 42, 45, 46, 60: "source files are never edited")
  and pandoc into docx, with a paged print index. It has not been run since chat 130-odd and its anchors have drifted.

So the operational definition: **the set is publishable when the press, run from the archive over the seated volumes,
produces six documents in which (a) every finding ever recorded against the volumes has a disposition — repaired by
entry and build, ruled not a defect, or stated in the volume itself as open by design; (b) no work matter reaches the
reader (no build, chat, docket, instrument or file handle, nothing a reader cannot interpret from the subject); (c)
every pointer, figure and count resolves; (d) the audit instruments and the census run green over the PRESSED text, not
only the source; and (e) the archive records the path, so the edition is regenerable byte for byte.** M signs the
pressed proofs; that is the end.

## 2. Where the store stands, measured

| | |
|---|---|
| Register | entries 1 to 1835; 1,677 seated (1,670 numbered + 7 grouped); 133 numbers absent by excision, unexplained to a reader; 1797 staged, never seated |
| Main volume | 18,692 lines; read in full by R2; three section blocks sit in the wrong chapter; nine sections are headings with no body; 15 sentences spell the Register's size as "one thousand six hundred and thirty-five" |
| Compendia (4) | never swept by class (M's 3 September scope ruling names the sweep; the docket records none executed); front matter names absent generators, dates and rebuild commands; 265 handles in one Mathematical Compendium column, 137 resolving nowhere; object ids (`A.ext` …) cited at 239 sites cannot be followed into the compendium |
| Defect census | 1,609 rows; 699 closed by a verdict, every closure id still resolving after the content-keyed regeneration; **910 open** — C8 299, C9 197, C6 178, C10 85, C11 50, C6a 35, C7 34, C13 23, pointers 9 (C1 4, C2 4, C2b 1) |
| Docket | 38 index items and 26 deltas; the R3 work queue; rewritten last at chat 127 |
| Instruments | 86 live goldens green, census step green; 8 held (readings owed); superseded predecessors seated red pending an archive ruling; 3 numpy packs, the figure generator and 4 census/tower instruments still in `extracted/`, unseated |
| Audit instruments | arith: 0 live disagreements; pointers: 4 register numbers and 31 in-range numbers cited with no entry, 37 `§4.n` pointers at unheaded rows, theorem numbers from an old chapter order, `E.4` with no parent, Figure 15.3 named and placed nowhere |
| Press | `build.py` seated; five dead Register anchors at BUILD90, one anchor moved by a date; pandoc absent from this container (LibreOffice present) |

## 3. The plan, in eight phases

Each phase is closed by a Working Register entry and a gate verdict; no phase begins before the rulings it names are
given; every volume change is a guarded build with a Register entry; every figure is re-run before it is seated; the
press is never run on a source that has not passed the gate. The order is M's standing rule RUL-128 item 1 —
mathematics first, then the prose that reflects it, then appendices and indices — with the Register and compendia legs
placed where their inputs are settled.

### Phase 0 — Rulings (M; one sitting, then written into RULINGS as a member)

The plan cannot start on these without you. Each is a choice, not a finding; my recommendation is first.

1. **The Register as a published volume.** It is a chronicle: instrument names in 112 lines, chats in 17, builds in 11,
   dockets throughout, "Claude" in two entries. (a) Publish it as the record of the work, with a reader's key up front
   (what a build, a chat, an instrument, a docket are), and press only the handles that name nothing a reader can hold
   (BUILD numbers, W-numbers, file paths, hashes) — recommended; (b) a full press pass rewriting every handle into
   subject language (1,677 entries; XL); (c) publish a reader's Register — the load-bearing entries and every entry a
   volume cites — and keep the whole in the archive.
2. **The fifteen spelled-out "one thousand six hundred and thirty-five"** in the main volume: re-type by press to the
   live count with a named state, or leave as narrative of the moment (recommended: press, one pair per site).
3. **The nine heading-only sections** (§14.5.2–§14.5.7, §2.22, §28.7.6, §28.9; also §21.5.4 and the compendium's twelve):
   you author them, or the headings are withdrawn by entry. This is the one item no one but you can do.
4. **Entry 1797** (the agreement theorem's counterexample, staged since W-196; its instrument now seated): seat or withdraw.
5. **Entry 1836** (the bracket result, drafted; instrument seated): seat, and its kind.
6. **The language roster** (dockets 20x-04 / 20x-09): six or seven; the measured five plus two special rows.
7. **The twenty chat-witnessed retraction rows** (DEF-153P) and **the 1,168 prose-only statements** (DEF-153R): a triage
   rule — which become your entries, which are recorded as leads and stay.
8. **The 110 withdrawn entries and "register 1725"**: none reinstated (recommended), and the four cited absent numbers
   (287, 1000, 1002, 1725) repaired at their citing sites by entry.
9. **Withdrawn things named by number in reader text** (Figure 15.3; the C7 class's pointer form "the figure §12.11.5
   withdraws; register 1819"): the form stands (recommended) or every such site is reworded.
10. **Unheaded targets**: `§4.1–§4.7` (Chapter 4's protocol rows, 37 sites) and `E.4` — give them headings by build
    (recommended) or rule that a prefix resolves.
11. **The compendia's generators** (`mathreg.py`, `compendium.py`, `indices.py`, `physics.py`, `mathverify.py` are not
    members and cannot be): rule the four compendia hand-maintained volumes, their "generated by / rebuild with"
    sentences pressed out, and the Löwdin verifier sentence reworded — recommended; the alternative is to write and seat
    generators that reproduce the volumes, which is XL and reproduces text that was hand-edited since.
12. **COORDINATES-2.13** (the Spectra Compendium's data companion, 11 MB, in the mirror only): seated as a member with the
    tools (your 5 September ruling reaches it) — recommended — or stated as external data with its md5.
13. **The superseded goldens**: an archive pass (ARCHIVE1's precedent) moving every predecessor with a seated successor
    out of the live set — recommended, so the gate's full walk is green — or leave them seated red.
14. **The census's C8 class** (299 rows, "named statement; stated in bold in main: yes/NO"): a listing, not a defect
    class — close by one ruling — or read row by row.
15. **The consolidation branch** (unmerged; two CLAUDE.md hunks conflict) and **Drive** (frozen at BUILD184/BUILD90):
    merge the branch to main, then this branch; reconcile Drive once at the end, not per build.

### Phase 1 — The mathematics leg (L; instruments then entries)

Every computable claim still unproven or contradicted, re-derived by a standard-library instrument and settled by entry
before any prose moves: the main-volume-versus-compendium contradiction class (docket 16z-01 first, then K I, Ne I),
the withdrawn-figure-re-asserted class (every WARNING read), the truncation-printed-as-equality class (16z-04 confirmed
wrong at the fifth decimal), the arithmetic-convention class (name the convention or correct the figure), the σ
collision (Rule 4 against §22.5), the 32/11 scope docket, the single-witness class, the unprinted-input class (sixty
figures printed without their inputs), the false-universal class (§34.6's "never resets" fails at Mo), the Chapter 34
walk ledger (1332/1402/1445/1448/1460/1463 read together; the memoryless 104 of 106 not reproduced), §10.2's
seventeenfold/hundredfold, the seed at the d-shell cap (1835's un-re-derived figure), MC §11's marginal-exclusion box,
the calendar fixture of 1175, 1141's n₀ reading, the compendium's combined 94 %. The Löwdin and three-body record-carried
class (1701–1724, instruments not held) is labelled record-carried by entry where no instrument can be built. Output: one
instrument per class, banked; one Register entry per correction or withdrawal; the count classes re-taken.

### Phase 2 — The Register leg (L)

Entries owed: §18.4.1's refinement, §18.5's pole correction, L9326's home, Thm 11.1's, §23.10.2's correction, the Sc VI
prediction, Appendix F's method ratio and the 19 removed figures with no home, the four intake drafts re-keyed, the
1448↔1332 tie, the seed's lower bound 5, MC-13 to MC-16's objects, the chat-witnessed retractions you rule are yours.
Then the Register's own defects: the emphasis class (22 unbalanced entries, a checker seated into the gate first), the
handle-leak class (23 open C13 rows and the 176 Ruling-46 candidates — by press under ruling 1, or by successor entry),
the front matter (five compendia against four, "ten grouped headings" against seven, the load-bearing table's casing,
the build labels and dates, a contents way into 1,677 entries, the 133 absent numbers explained in one sentence), the two
entries naming the assistant, 375's false sentence and 332's lost sentence (withdraw or restore by entry).

### Phase 3 — The prose leg over the main volume (XL; the largest phase)

The prose pass RUL-128 defers everything to, chapter by chapter in reading order, each chapter one guarded build:
Ruling 45 (first-person and session narration, 133 members and the later deltas — "session" in two headings), Ruling 46
(work matter, about thirty sites), the four pointer classes (forty-five wrong targets; targets that say nothing of the
claim; citations with no entry; one event with four homes), the caption-corrected-but-not-the-prose class (Chapter 34 at
chapter scale), the retired-basis class ("an earlier version" ×8, "an earlier draft" ×7), spliced text, the numbering
passes (Chapter 28; the §3 audits; placeholders), the duplicated section §9.2 = §27.5.1, the three misplaced section
blocks (§2.21–2.24 inside Chapter 3; §12.11.8 inside 13; §28.10 inside 29), two headings broken across lines, the stale
self-counts (§28's opening twenty-six; §14.6's 248/265/299; §32.1's index over 35 chapters and 6 appendices when there
are 36 and 7; "at this build" figures re-taken at the final press), §14.5.12–14 pointed at 1833–1835, MV-DEF-01 at §10.4,
the References (33 cited names unbibliographed; chordal, treewidth, girth absent), the Index regenerated with Appendix G
locators, Appendix E's parent heading, the formatting pass. Your authored sections enter here.

### Phase 4 — The compendia and the Index of Indices (L)

The class sweep your scope ruling names, never executed: nine transversal classes over the four volumes (WARNING sweep;
citations and § pointers; attributions against References; handles; counts against the Register; data rows; front
matter; withdrawn statements; interface disclosures). Then the volumes' own defects: the handle vocabulary stated (a
printed key for the 265 handles and the object ids cited at 239 sites), the front matter under ruling 11 (299 against 265
against 248; "generated on"; rebuild commands; MECHANISMS.md; sessions and file names in the Spectra Compendium), the
data defects (Spectra L562, nine duplicated keys, IoI L2021, "interiority" twice), the twenty-seven "objects rest on it"
counts, the 285-of-431 channel sentence against the Spectra Compendium's current count, Appendix G's three pointers to
entries that do not exist, the bibliography's objects column, the bracket-system object, the IoI's Λ₁₂/Λ₁₃ rows against
its generator claim.

### Phase 5 — Closing the census (L, in parallel with 1–4)

910 open rows, one reading instrument per class over the whole census, each row a verdict in a closure file and, where a
defect, routed to its phase: C6 (178; a compendium number not in its stated source) with C6a (35; an entry with no source
pointer), C9 (197; always/never/every — the false-universal class's census face), C10 (85; proved with no Register entry),
C11 (50; the R-form incomplete), C7 (34; withdrawn numbers surviving — ruling 9 closes them), C13 (23; ruling 1 closes
them by press), the 9 pointer rows, and C8 (299) by ruling 14. The census is regenerated after every build that moves a volume; its step in the gate stays green.

### Phase 6 — The instrument estate and the archive (M; alongside)

Under your 5 September ruling every instrument the record names goes in: the three numpy packs (chats 57, 58, 65),
`fig_indices.py` and the two Index of Indices figures re-run, `a4_census.py` / `a4b_census.py`, `method_tower.py` with
its missing driver found or recorded absent, register 66's re-measurement instrument, the audit-7 ledger, COORDINATES
under ruling 12. Successors owed: r2-26b2 (a reading), r2-ch18b / r2-ch23b / r2-reg11a2 / r2-reg12b (content-keyed,
within the gate's ceiling), r3-wl2's golden, r2-28b3 banked or retired, pointers.py's three blind spots, census2's
cross-volume pointers, a gate.py successor naming main by glob, RETIRED.tsv carried forward, the r2lib lifts. The archive
pass under ruling 13. The gate text (method/CLAUDE.md) re-taken to the store's state; the docket index consolidated
(rewritten last at chat 127); README and docs re-taken; the consolidation branch and Drive under ruling 15.

### Phase 7 — R4, the cross-volume audit (M)

Every figure in every volume equal to its banked golden; arith, pointers, cypher, populate, buildtrace and slopeaxis
run with every finding disposed; the census at zero open rows or every row closed; the count classes agreeing across the
six volumes. Then the production line the record already names: the compendium renumbered into the main volume's
physical order (once, last), the bibliography, the Register expansions, the canon order. Nothing else changes after this.

### Phase 8 — The press and the proofs (M)

A `build.py` successor: the dead anchors repaired, the substitution table extended to the residue of rulings 1, 2, 9 and
11 (each pair a recorded press-time substitution, never a source edit), pandoc installed or LibreOffice's route
measured, the paged print index, six documents pressed from the seated members. Then the audit instruments and a
work-matter census run over the PRESSED text and required green; the proofs read whole (withdrawals legible, contents
true, index locators true); the pressed documents seated as members with their md5s and a Working Register entry; your
signature on the proofs.

## 4. What stays open by design, and is published as such

The main volume's own open set (ten Q items, three unreached documents, five unlocated results, one unexplained
ratio), the Index of Indices' indexes named and not built, the Spectra Compendium's 126 untested channels for want of
data, the two unfinished Mathematical Compendium objects, Appendix B's four totals awaiting twenty rows, the eighteen
cells wanting a longer capture. These are the book's honesty; the plan makes each one say so in place and leaves it.

## 5. Order, dependencies, size

Phase 0 gates everything. Phases 1 and 5 start together on the rulings; 2 follows 1's entries; 3 follows 1 and 2
(prose after mathematics, RUL-128); 4 can run beside 3; 6 runs throughout; 7 needs 1–6 closed; 8 needs 7 green. Rough
sizes at the sessions this work has actually taken: Phase 1 eight to twelve; Phase 2 four to six; Phase 3 fifteen to
twenty-five (the prose pass is chapter by chapter, and your authored sections are on its path); Phase 4 six to ten;
Phase 5 four to six in parallel; Phase 6 three to five; Phase 7 three; Phase 8 three to five. The whole is on the order
of fifty to seventy working sessions, of which your own time is the rulings (one sitting), the authored sections, the
retraction and prose-only triage, and the proofs.

## 6. What I ask you to approve

1. The definition in §1 as the finishing line.
2. The eight phases and their order.
3. The rulings of Phase 0, or your alternatives, so that Phase 1 can open.
4. That the plan is seated as a member and rewritten by successor at each phase close, with the docket consolidated
   into it, so there is one place the remaining work is counted.
