# RULINGS-R2.md — rulings and standing discipline in force during Phase R2 (append-only)

This member replaces the rulings paragraph of the handoff (chat 74, ruling 3). A chat appends a dated block when M rules; nothing here is edited or removed. The Register is a different object (subject matter only); this is process.

## As restated in HANDOFF-25 (chat 74), verbatim

**Rulings in force** (unchanged from HANDOFF-24): chat 67 — every volume read in full, no editing until the review closes; chat 68 — instruments travel as bundle members, the gate fetches the two bundles by title, Drive is the store; chat 69 — handoff at **90–95 %** of context or on a closed segment, never earlier, never mid-segment; chat 70 R1 — CENSUS-CLOSURES-A governs its 21 shared rows, A vocabulary (*defect / not a defect*) in every closure file, an unreferenced prior-art row is a defect, co-located stale text counts against its census row; chat 72's rule, followed by chats 73 and 74 — begin the close when the remaining context would not fit a segment plus the build, and record the estimate in W-NNN; M's priorities — the computational audits are paramount, every stated value recomputed; stale self-description and production classes are noted, not a concern. Standing discipline: measure from files, never recite (grep every line number before it is written); label MEASURED / INFERRED / record-carried; no silent change; list a directory before copying, never copy over an existing file; a message with a question ends at the question mark; never announce a next action with a question; `timeout 280` on every call; /bin/sh is dash — write text via python heredocs or create_file; remove `__pycache__` before any member census or build; import tower-2.py by path (importlib, as r2-ch12i/j/k do), never by copying it to tower_2.py; C7 census rows whose flagged token is a live figure or label are regex artefacts (precedent 678, 680, 681–687).

## Chat 74 (30 August 2026) — session-throughput rulings

1. **Declined:** direct upload of the bundles as an archive (M: not enough internal storage). The gate keeps fetching both bundles from Drive by title; Drive remains the store.
2. **Approved:** the gate and the close as instruments — gate.py (MANIFEST.tsv verification of both bundles, golden-output runs printing only mismatches, census, extent sites, certificate), close.py (guarded build with manifest and reverse recovery), r2lib.py (shared functions lifted verbatim from the instruments), banked NAME.out goldens for every deterministic instrument. Instrument design remains Claude's.
3. **Approved:** the handoff carries identity (chat, build, Register range, md5s), the bootstrap, the gate run list, next work, Drive actions and the prompt; rulings live here and deferred items in DEFERRED.md, both append-only.
4. **Approved:** built in chat 74 itself (BUILD101 + HANDOFF-26; HANDOFF-25 and BUILD100 retired unused).

Measured basis (chat 74 transcript, byte shares): gate 32 %, close 10 %, reading 57 %; each Drive fetch leaves a ~65 KB base64 preview in context (13 % of the chat for the two). Rulings 2–4 remove the by-eye comparison and the handoff growth; ruling 1 leaves the fetch cost as it is.

## Chat 81 (30 August 2026) — the R2 read order, and two batches per section

**M, verbatim:** "UPDATE TO FULL AUDIT PROCESS - Read the remaining chapters first for where the computable claims are, then instrument those in batches. AND Read the remaining chapters first for where the prose claims are, then instrument those in batches. Two batches per section read."

Issued after chat 81's close, in answer to the measured rate: chats 75–81 read 967 main-volume lines at 138 lines per chat, one bespoke instrument per subsection, which projects to roughly 160 further sessions for the six volumes (MEASURED rate, INFERRED projection, W-118's closing report).

1. **The read comes before the instrument.** A section is read first to locate what it claims, not read and instrumented in one movement. The read produces a claim census, and the census is what the instruments are built against.
2. **The census is in two kinds, and both are instrumented.** *Computable claims* — anything re-measurable on the tower's cells, pairs, closures or seeds — and *prose claims* — pointers, attributions, figures restated from elsewhere, self-description, citation chains, vocabulary. The second kind is not read-only: it is instrumented too, as r2-ch13i instrumented the pointer census of §14.5.2–§14.5.7.
3. **Two batches per section read.** Each section read closes with exactly two instrument runs — one computable batch, one prose batch — rather than one instrument per subsection. A batch may carry the claims of several subsections; that is the point of batching.

**Operative reading, recorded so it is reversible on one word:** the unit is the *section* (a `###`-level section and its subsections, or a `##` chapter where its sections are short), not the whole remaining book. Chat 82 reads §14.5.8–§14.6 as one section read, censuses its claims into the two kinds, then runs two batches. A single forward census pass over all thirty-one remaining chapters before any instrumenting is the wider reading of "read the remaining chapters first"; it is not the reading taken, because a census taken far ahead of its instruments is a site list carried rather than measured, which this project has found short four times (W-002, W-003, W-014, W-024).

**What does not change.** The chat 67 hold stands: findings are identified and recorded, never repaired, and no Register entry is written until the review closes. Every claim is still resolved to the claim and not the heading, every figure still grepped for its other sites, every batch still banked as a golden, and each section read still closes — files written, md5s measured, golden banked — before the next opens. READ-chNN.md keeps its A / B / C form; CENSUS-CLOSURES-chNN.tsv keeps its vocabulary. The gate and the close are unchanged.

## Chat 95 (31 August 2026) — the escalation bar, and Prints & Proofs before any question

**M, verbatim,** in answer to four items put up as needing a ruling: "1 - so look in the proofs &
prints folder. This did not require my ruling. 2 - understood. This is also, not requiring my
ruling. 3 - this needs to be flagged for correct. The project works should contain the answer, or
the math is wrong. 4 - this is the whole point of these audit. You are to find these errors in both
the math and the prose, and flag them for repair."

1. **A finding is not a question.** A deviation found in the subject matter — in the mathematics or
   in the prose — is recorded and **flagged for repair**. It is not put to M. Finding them is the
   work; escalating them is not. This governs both kinds equally: a wrong pointer, a wrong clause
   ordinal, a misattributed species and a false universal claim are all repair items, not ruling
   items.
2. **Prints & Proofs is searched before any question is asked, not after.** Ruling 56 makes the
   folder (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) the original-input witness. Where a question is of
   the form *did this text ever exist* — production loss against authoring gap, a dropped table, a
   figure without a caption — the folder answers it and the question never reaches M. G8 already
   said questions answerable by reading are never escalated; this names the folder as one of the
   places that must be read first.
3. **An internal contradiction is a defect of the work, not an ambiguity for the author.** Where
   two sites cannot both stand, the project works contain the answer or the mathematics is wrong.
   Either way the item is flagged for correction in R3 and carries both readings; it is not held
   open waiting on a ruling. The §22.5 / Rule 4 σ collision is disposed of on this basis.
4. **What still reaches M.** Only a choice that no file can settle and no measurement can decide —
   a preference between two defensible repairs, a change of scope, a new phase. Not a defect, not a
   missing entry, not a contradiction, not a pointer that fails.

**Consequence for the handoff form.** The handoff's standing section *"Items needing M's ruling
before R3 can move"* is **retired**. In its place a handoff carries a **repair docket**: the
finding, both texts, the measurement, and the candidate repairs — carried forward until R3 executes
it. HANDOFF-48 is the first written in the new form.

**Disposed of under this ruling, all four items chats 90–95 had been carrying:**

- **§14.5 heading-only sections — closed as a finding, chat 95.** MEASURED against the Prints &
  Proofs original `The Method 1.6.md` (738,550 B · md5 49900cf41f818ab789bb90fc596ac977): §14.5.2
  through §14.5.7 carry **zero non-blank body lines there too**, at P3764–P3775, exactly as in
  BUILD90 at L3798–L3809. The text never existed. **Authoring gap, not production loss** — the
  question five chats old is answered, and it did not need M. Two carried figures are corrected:
  the class is **six sections, not five** (§14.5.2 is also empty), and §14.5.7 carries **24
  citations, not nine**.
- **The §18.4.1 one-dimensional refinement** — a missing Register entry, written when the chat-67
  hold lifts. No ruling required.
- **The §22.5 / Rule 4 σ collision** — flagged for correction under 3 above.
- **The ν_V pointer and the Ga I attribution** (chat 95's 14k-01, 14k-02) — flagged for repair
  under 1 above.

**What does not change.** The chat 67 hold stands: findings are recorded, never repaired as found,
and no Register entry is written until the review closes. The chat 81 cadence stands: read, census
in two kinds, exactly two instrument batches, section reads never split. The gate and the close are
unchanged.
## Chat 127 (1 September 2026) — five rulings: scope, authoring, the hold, the handoff

**M, verbatim,** in answer to five items put to him after the session-count estimate (about 30
sessions to close R2 under items 1–2 against 45–55; about 230 for a line-by-line compendia read;
85–125 through R4 and production): "Implement all 5 please, and then rebuild the handoff for the
next chat."

1. **Appendices D–G are censused as data.** Appendix D *The mathematics, indexed* (main L10320–
   L10897), E *Q, indexed and closed* (L10898–L11221), F *The numbers, indexed* (L11222–L11360) and G
   *Transitions, indexed* (L11361–L11406) — 1,087 lines of indexed rows — are audited by an
   instrument that reads every row as a claim: the object named resolves to its Register entry or
   section, the figure is grepped for its other sites, the status marker is tested against the entry
   it restates and against that entry's WARNING line. Prose paragraphs inside them are still read.
   Chapters 35–36, Appendices A–C, the Index and the References stay under the chat-81 cadence.
2. **The compendia are audited by class across all six volumes, not in source order.** This closes
   the scope question chat 113 put open. After the main volume closes, R2 continues as one
   transversal instrument per docket class, each banked as a golden with a READ-sweep file and a W
   entry, in this order: (i) the Register WARNING sweep — every entry carrying a WARNING, matched
   against every reader-facing site that still prints its figures (the instrument that found
   16z-01); (ii) register citations and § pointers, existence first, grouped-aware, both resolvers;
   (iii) attributions against `## References` body and R.7, both directions; (iv) count words against
   DATA rows, numeral spans and restating entries; (v) numerals cross-site at the printed precision;
   (vi) heading-only and placeholder sections against Prints & Proofs; (vii) absent members,
   notation-tolerant; (viii) formatting; (ix) every species figure against the channel table
   (spectra L293–L934, totals L900). Prose that only reading can test — the narrative sections of
   the Physics and Spectra Compendia, measured at that point — is read line by line.
3. **Authoring begins now, in parallel with R2.** M authors the six heading-only sections
   §14.5.2–§14.5.7, §2.22, §28.7.6, §28.9 and the Chapter 34 rewrite. The Register already holds the
   material: seed(Λ₈) = 7 (chat 90) and register 573 for §14.5; registers 1437, 1445, 1460, 1465 and
   1470 for Chapter 34. Authored text enters a volume only through a guarded build with a Register
   entry in the same build (no silent change), and every figure in it is censused and instrumented
   before seating (W-101: all subject matter true and proven). The audit does not wait for it and it
   does not wait for the audit.
4. **The chat-67 hold is lifted for one class only: the withdrawn-law class (16z-01).** R3's first
   item executes now, ahead of the review's close: the status of ν in Chapter 34, Chapter 35's
   opening sentences (L9718–L9721, L9731–L9732) and the appendix rows L10850–L10856 are corrected as
   status sentences — the form, its scores (99 of 106 in sample, 90 held out against Madelung's 96),
   the corridor's non-emptiness as a result about the form, registers 1437/1445/1460 cited — with
   new Register entries recording the correction, a guarded main-volume build (BUILD91, the first
   change since chat 62), the kinds table recounted and the extent restated everywhere. The
   candidate wording is put to M once, at chat 128's open, and executed on his word. The hold stands
   for every other class.
5. **The handoff is slimmed and the bundle split.** The repair docket index, the standing method and
   the conventions move to `DOCKET.md`, a bundle member rewritten at every close; the handoff carries
   identity, gate, the next unit, Drive actions and the prompt. The compendia bundle is split into a
   LIVE bundle (the four compendia, the governing members, the gate and close instruments, the
   instruments and READ files of chats 110 onward) and an ARCHIVE bundle (the 48 legacy handoffs and
   the pre-chat-110 instruments, goldens, READ and closure files — MEASURED 393 members, 3.7 MB of
   7.4 MB), fetched only when a docket item reads one of its members (r2-ch14l.out's eight V values
   is the standing case). The split is its own segment with its own reverse-recovery guard, and both
   bundles are gated by md5 from then on.

**What does not change.** The chat-81 cadence for every line-by-line unit; the gate and the close;
findings recorded and flagged, never put to M; no correction outside item 4 until the review
closes; Register entries append-only; every volume change carried by a Register entry in the same
build; the chat-95 escalation bar.

## Chat 128 (1 September 2026) — the order of correction, the audit order, and the two project requests

**M, verbatim,** on the withdrawn-law wording put to him: "Approved"; then, on the wording's one measured
correction (1794: *'measured' and 'verified'*): "Yes, but I worry that any prose edits we do now may have to
again be altered based on what is corrected elsewhere in the books. So all the math has to be correct and
proven, so the prose can then reflect the correct math, and then the appendices and indecies can be corrected
to also reflect the correct math." And: "Another that must be taken into consideration when the math is
reviewed, audited, and corrected...all claims, rules theorems, laws, solutions, must be true. Remember the
scope of the whole 6 book works. We're trying to show the whole world how centuries of math and science works
together as a single machine/index that can solve any problem, answer any question, all based on real and
witnessed periodic elements." On the audit order proposed: "I do approve".

1. **Every claim, rule, theorem, law and solution in the six volumes is true and proven** (W-101 restated as
   the standard the audit measures against). **The order of correction is the mathematics first, then the
   prose that reflects it, then the appendices and indices that reflect both.**
2. **The withdrawn-law class (chat-127 item 4) is HELD, not executed.** Its wording is approved as
   R3-CLASS-WL.md items 1–6 as put, with L9664 read as register 1437's *eight of the ten*, item 7 (L9731–L9732,
   L9742) added, and entry 1794 reading *carried 'measured' and 'verified'*; `r3-wl.py` specifies it with a
   banked dry-run golden. It executes in R3 after the Chapter 34 figures are re-taken under docket 37.
3. **The audit order approved:** (i) close the main volume under the chat-81 cadence and chat-127 item 1;
   (ii) the Register WARNING sweep, then every computable claim in the Register and the Mathematical
   Compendium re-derived by instrument and banked — the Chapter 34 re-take and the SCF chain first; (iii) R3
   in the order of item 1, each change through a guarded build with a Register entry; (iv) R4, every figure in
   every volume equal to its golden, then the press.
4. **The Löwdin and three-body projects are asked for their instruments.** REQUEST-LOWDIN.md (twelve items)
   and REQUEST-THREEBODY.md (ten items) are members; deliveries arrive in Materials subfolders
   `LOWDIN-DELIVERY-1/` and `THREEBODY-DELIVERY-1/`; each object enters only through a guarded build with a
   Register entry, a validation block against the Register's anchors, and a golden; "not held" is an answer,
   and the figure is then labelled record-carried and reconstructed.

**What does not change.** The chat-81 cadence; the gate and the close; findings recorded and flagged, never
put to M; the chat-67 hold for every class; Register entries append-only; no silent change; the chat-95 bar.

## Chat 151-R (3 September 2026) — the compendia scope: the Register in full, the other four by class sweep

**M, in answer to the scope question put to him** in the repository session of 3 September 2026 — not a
Method chat. The question was put with three routes and their measured costs and M chose the third.
**There is no verbatim quotation: the answer was given by selection, not in words**, so the three routes
are reproduced here as they were put and the choice is checkable against them.

**The question.** DEF-141 item 15, parked at the main volume's close and never put. Chat 67 rules that
every volume is read in full; chat 127 item 2 rules that the compendia close by class sweeps, and W-167
recorded chat 113's scope question as closed by it. The two had not been reconciled.

**The extents, MEASURED on the BUILD180 members:**

| volume | lines | bytes |
|---|---:|---:|
| The Register | 6,611 | 1,203,491 |
| Mathematical Compendium | 3,802 | 309,403 |
| The Physics Compendium | 878 | 61,366 |
| The Index of Indices | 2,093 | 118,373 |
| Spectra Compendium | 1,159 | 100,790 |
| **total** | **14,543** | **1,793,423** |

**The routes as put.** (i) Class sweeps throughout — 25–35 sessions. (ii) Source-order reads for all
five — ~230 sessions on the chat-127 projection, ~125 on the main volume's measured rate of 116 lines
per session (INFERRED). (iii) The Register in full, the other four by class sweep.

1. **The Register is read in full, in source order, under the chat-81 cadence,** as the main volume was.
   It is 6,611 of the 14,543 lines and the volume the other five cite.
2. **The Mathematical Compendium, the Physics Compendium, the Index of Indices and the Spectra
   Compendium close by class sweep** against the docket's classes, under chat 127 item 2. They are not
   read line by line.
3. **DEF-141 item 15 is CLOSED as a question.** Chat 67 and chat 127 item 2 are reconciled by items 1
   and 2 above; neither is reopened.
4. **RUL-128 item 3 (ii) is unaffected.** Every computable claim in the Register and the Mathematical
   Compendium is re-derived by instrument and banked, whichever route its volume takes.

**Projection (INFERRED).** 60–90 sessions for the compendia leg, against 25–35 for route (i) and ~230
for route (ii).

**What does not change.** The chat-67 hold; the chat-81 cadence; the gate and the close; the chat-95
escalation bar; findings recorded and flagged, never put to M; Register entries append-only; no silent
change; the order of correction under RUL-128 item 1.

**Where this was seated.** The answer was given in the repository session of 3 September and staged there unseated while chat 151-B closed BUILD181 through BUILD184 in Drive. It is seated at **BUILD185** by the same repository session (W-194, keyed 151-R), together with the Register read it authorised. **Item 1 is discharged: the Register is read in full, entries 1–1792, in thirteen source-order units plus a whole-volume sweep.** Item 2 is what R2 still owes.
