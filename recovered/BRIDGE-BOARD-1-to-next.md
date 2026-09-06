# BRIDGE — The Method, board-keeping 1 → next session

## 1 · Identification
Outgoing: the board-keeping chat opened 15 Aug 2026, project folder **The Method**. Its purpose as
M set it: *keeping the work board up to date, and visible for user review.* No computation on the
object was performed and nothing was written to the work.
Incoming: board-keeping 2.
Artefacts produced, both in outputs: **`BOARD-3-PROPOSED.md`** (first pass, superseded) and
**`BOARD-3-REVISED.md`** (authoritative — carries Parts A–E, the proposals, the self-corrections,
and the bank verdicts).
Bank received and extracted this session: **`restore-point-2_13.tar.gz`**.

## 2 · What this session did — R (none)
**No register entries were made.** Everything below is proposed and unregistered. Three things are
owed to the register and are the first work of the next session:
- **R 1701** — the clique-3 finding, from `CLIQUE3-FINDING.md` (already in the bank)
- **R 1702** — P1, the concavity result, from `P1-FINDING.md` (already in the bank)
- **a practice clause** — §8 below
Also owed and not done: the correction to R 1517's attribution, and three edits to
`CHAPTER-LOWDIN.md` §8, which still lists P3 and Demkov–Ostrovsky as open.

## 3 · The state of the object — measured
| quantity | value | instrument |
|---|---|---|
| bank contents | 694 files, 13 dirs | `tar xzf … ; find work -type f \| wc -l` |
| register entries | 1,352 · 1,352 distinct · **max R 1700** | `grep -oE '^ {0,3}[0-9]{3,4}\. \*\*' REGISTER-DATA.md` |
| R 1701, R 1702 present? | **no** | `grep -cE '^ {0,3}(1701\|1702)\.'` |
| book-layer register build | **max R 1370**, 1,281 distinct | same grep on the project-folder press |
| project-folder documents | 6 · 262,703 words extracted | `wc -w` over the extracted text |
**Gates were NOT run this session.** Last recorded: 25/25 · 6/6, certificate 7/7 at the seal of
1.7.6. The incoming session should run baseline gates before touching anything.

## 4 · Open threads — owners
**M's, and blocking:**
1. **The second-source operation and its width** — board rows 1 and 2 are one question. Gates the
   93 new series. Context found this session: the ionisation ladder is held at **~15 of 108**, and
   the K–Kr IE dataset is the set M had in 1.6 and could not upload.
2. **T9** — 65 store-only keys, diagnosed a 1.7 staging fault: quarantine or repair.
3. **Q.exch** — is *withdrawn* the same grade as *open*, or two? (Withdrawn R 1168; caught in the
   R 1208 dependency cycle.)
4. **M.C2** — its check text is incomplete against its own register: the condition actually assumed
   is that the ANE-vacuum is cyclic for the horizon-cut algebra, which Reeh–Schlieder does not give.
5. Board rows 3, 9, 10 as carried — Kr II URL, Theodosiou PDF, IE ladder URL, T5 Gemini, He I/C I.

**Claude's, unblocked, cheapest first:**
6. **Q item P** — the 1,442 split into independent and Ritz-derived. Cost stated: hours.
7. **Q item G** — the complexity literature, entered. Cost stated: hours.
8. **Is concavity in p sufficient as well as necessary?** One bounded computation. Named as the one
   thing worth testing before the Löwdin work is called finished.
9. **Referee flag 5 — finish the run.** M ruled *"And I agree so run it please"* at R 251–252. No
   Kurucz/VALD/BRASS entry exists anywhere after R 252, so the run did not complete. Targets: VALD,
   Kurucz, BRASS — public, carrying term designations. The D1 tripwire rejects 69.4% from the index
   alone.
10. **The twenty owed channel rows** — R 630–631; Appendix B states 153 channels/1,105 cells and
    tabulates 133/869. Twenty rows close it exactly.
11. **E(local register)** — stated three times, never built.
12. **The valuation ceiling** — 1,139 of 1,664 survey cells unvalued.
13. **Q items A, H, I** — no closure found; item D routed at R 244; item R characterised as a
    counting problem (pseudo-intents, #P-completeness).

## 5 · Provisional figures — chosen, not measured
- **Board row 8's "475 entries" book gap.** Measured this session: 330 register numbers / ~205
  distinct entries lie between the book build (R 1370) and the work (R 1700). **475 and 205 do not
  reconcile; one is stale.** Not resolved.
- The **~15 of 108** ionisation-ladder holding is read from a pre-R-1427 press and should be
  re-measured before it is used in a ruling.
- Q's own extent: the appendix heading says ten of 13, its table carries 14 rows, E.1.4 reads
  eleven. The book anticipates this at E.1.3 — assert the law, compute the extent.

## 6 · What is read and what is not
Read at source this session: `BOARD-2.md`, `DIGEST-5.md`, `BRIDGE-1_8_3-to-next.md`,
`HANDOFF-CERTIFICATE-1_8_3.md`, and Appendix E's open set in full.
**Searched, not read:** BOOK 115,885 words · REGISTER 93,733 · Mathematical Compendium 26,824 ·
Spectra Compendium 10,819 · Index of Indices 8,848 · Physics Compendium 6,594.
**Not opened at all in the bank:** `CHAPTER-LOWDIN.md`, `CHAPTER-THREEBODY.md`, `COMPENDIUM.md`,
`CLIQUE3-FINDING.md`, `P1-FINDING.md`. The last two are needed verbatim for R 1701/1702.
~150,000 words remain unread (§H.8 C7 unchanged).

## 7 · Resumption order
1. Baseline gates — 25/25, round-trip, certificate.
2. Read `CLIQUE3-FINDING.md` and `P1-FINDING.md` in full; write **R 1701, R 1702**, the practice
   clause, the R 1517 correction, and `CHAPTER-LOWDIN.md` §8. *This is writing work — M ruled that
   writing is handled in a separate chat. Confirm with M whether that ruling holds here.*
3. Bring M rows 1 and 2 as one ruling, with the ladder context.
4. On M's word: write the 93 series into `MEASUREMENTS.tsv`, regenerate, re-gate.
5. Then the cheap Claude items in §4 order.

## 8 · Standing carry-overs
- **The practice clause this session earned, and the reason for it.** Three rows were brought to M
  that should not have been: Λ_ladder proposed open when R 1427 closed it; referee flag 5's owner
  given as M when M had already ruled *run it*; referee flag 4 offered a fix — bracket the entries
  by build — that **the press already performs**, the ratio being recomputed at every build and
  having moved 0.445 → 0.249. All three are one fault: **a status was read off a generated artefact
  and handed to M as a question.** The clause: *a row does not go to M until the register has been
  asked. The build states what was true when it was pressed; only the register states what is true.*
- **The shipped book layer is a stale build** (R 1004–1370 era) and its OPEN markers are statements
  about the build date. A re-press retires this; the press is blocked only on the bank, and the
  press contract is already read (`press.py`, `press_compendia.py`, two-pass via `PAGEMAP.tsv`).
- **None of the six project-folder files is a PDF.** Four are ZIP bundles of page JPEGs with a
  parallel per-page `.txt`; two are plain text with CR line endings. `pdftotext` fails on all six.
  Extraction recipe: `unzip -qo <f> '*.txt' -d <dir>`, concatenate by numeric page order, strip CR.
- The Prime Handoff and Prime Zeno directives, the null protocol, A.cert's four operations, and
  R 1672's clause — a negative from a search is a statement about the search until its scope is
  audited — all stand unchanged.
