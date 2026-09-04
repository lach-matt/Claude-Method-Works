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
