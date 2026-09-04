# THE BOARD — REVISED after transcript review
Supersedes `BOARD-3-PROPOSED.md` of this session. Still **PROPOSED, not applied**; no register
numbers assigned. Sources: the project folder (six documents, extracted and searched), the
working layer, and the project's chat transcripts read via search.

## THE FINDING THAT GOVERNS THE REST
**The shipped book layer is a stale build, and its OPEN markers cannot be read as current state.**
The six documents in the project folder are ~R 1004–1370-era presses. Two of the items I proposed
last pass as open were closed in the register long ago; the PDF still prints them OPEN because the
PDF has not been re-pressed since. **Every "OPEN" in the book layer must be checked against
`REGISTER-DATA.md` before it is believed.** This is the R 1672 clause — a negative from a search
is a statement about the search — arriving in a new form: *a status read from a generated artefact
is a statement about the build date.*

---

## PART A — SELF-CORRECTIONS to my own last pass

### ✗ B-6 WITHDRAWN — Λ_ladder is CLOSED, not open
**Λ_ladder closed at R 1427**: fourteen ladders (six species, six state, two X-ray), nine cells,
E = 0, on (seat, kind, Zcross), once the X-ray pair is seated at subvalence. Open since R 1356;
the defect at the subvalence seat demanded Λ_xray, and Λ_xray filled it. Contingency: 90% of
comparable nine-cell sets on that grid refuse, so the zero is earned.
The Index of Indices PDF prints it OPEN on the *old* coordinates (fixes, seat) — a pre-R-1427 build.
**What survives, and matters:** the ionisation ladder's coverage, **~15 of 108 held**. That is the
live substance, and it is exactly what board rows 1 and 9 are about — the K–Kr IE dataset M had in
1.6 but could not upload, requested then in element-range splits.

### ~ B-4 REVISED — M.C2 still open, but the obstruction has moved
The compendium's account (geometric route only; bottoming out at positivity) is superseded.
Since then: **R 1479 corrected** — the 4D interacting case is *not* the obstruction; half-sided
modular inclusion is established for interacting theories on a Killing horizon, and the Killing
field enters at exactly one step, identifying the modular Hamiltonian with the boost.
**A fourth condition was isolated:** Borchers' data is a quadruple, and Faulkner–Speranza's (iii)
bundles invariance with standardness. The condition actually assumed is **that the ANE-vacuum is
cyclic for the horizon-cut algebra** — assumed in the source, *not* supplied by Reeh–Schlieder
(which gives cyclicity of the global vacuum), and absent from M.C2's own check.
**M.C2's check text is incomplete against its own register.** Owner: **M**.

### ~ B-10 REVISED — Löwdin's §8 open list is empty but for P4
| item | state |
|---|---|
| P1 — what the corridor is an instrument of | **CLOSED**, most recent chat |
| P2 / Demkov–Ostrovsky | **CLOSED R 1621** |
| P3 — the onset formula K(x) | **CLOSED R 1617** |
| clique-3 obstruction | **CLOSED** — 205 maximum cliques, not one; only **Lr** forced in all 205 |
| P4 | open, but a **prohibition, not a gap** |
P1's result: strictly concave increasing functions of the node count p are **necessary** — feasible
at all 106 steps, clique 3 invariantly; linear and convex forms refuted at exactly 6 steps. The six
— La, Gd, Ac, Th, Cm, Lr — are identical to the three upper canonical bands from the clique
computation, across two code paths sharing nothing. La and Ac are where Madelung is false.
**Löwdin's challenge itself stands:** concavity is a necessary condition established by refutation,
not a mechanism, and nothing here derives the order from the Schrödinger equation.

---

## PART B — NEW ROWS from the transcripts

### N-1 · The register is behind the work — R 1701 and R 1702 are earned and unwritten
The board's `max R 1700` is stale in the other direction: two findings are closed and not
registered. Owed to a writing chat, explicitly deferred by M's ruling *writing will be handled in
another chat*:
- **R 1701** — the clique-3 finding (205 maximum cliques; Lr alone forced; Boron an artefact of
  the greedy scan's ordering)
- **R 1702** — P1, the concavity result
- **correction to R 1517's attribution** — 205 maximum cliques, only Lr forced
- **`CHAPTER-LOWDIN.md` §8** — three edits; it still lists P3 and Demkov–Ostrovsky as open
Artefacts already written and waiting: `CLIQUE3-FINDING.md`, `P1-FINDING.md`, `clique3.py`, `p1.py`.
Owner: the writing chat. **Until these land, both gates are being run against a register that does
not hold two of the project's closed results.**

### N-2 · Is concavity in p *sufficient* as well as necessary?
No concave form has been found to fail, but this was not formally tested. Named as the one thing
worth testing before the Löwdin work is called finished. Owner: Claude, one bounded computation.

### N-3 · The press is blocked on the bank — and pressing retires the stale-build problem
The Books chat has read the press contract at source: `press.py` (594 lines, DejaVu, heading gate,
legacy-figure assert), `press_compendia.py` (244 lines, five source→artefact pairs), and the
**two-pass requirement** — press → `pagemap.py` → press, because `PAGEMAP.tsv` is built by running
`pdftotext -layout` over the *previous* build. All five compendium sources are generated artefacts
that just passed 6/6, so the compendia press sits downstream of a gate that has already declared
them clean.
It is blocked on one thing: `restore-point-2_13.tar.gz` has not been uploaded.
**A re-press closes B-11, B-12 and the governing finding above in one operation**, because the
shipped PDFs would then carry R 1700+ and their OPEN markers would again mean what they say.

---

## PART C — CARRIED, UNCHANGED
Board rows 1–10 of `BOARD-2.md` (R 1700) stand as written; nothing in the transcripts closed any
of them. Rows 1 and 9 gain the Λ_ladder context in Part A.
From `BOARD-3-PROPOSED.md`, still standing and still unchecked against the register:
**B-1** (Q's ten open items) · **B-2** (referee flag 5, targets identified, run not attempted) ·
**B-3** (referee flag 4, and the second observation now available) · **B-5** (Q.exch grade/status) ·
**B-7** (twenty channel rows owed, R 630–631) · **B-8** (1,139 of 1,664 survey cells unvalued) ·
**B-9** (E(local register), not yet built) · **B-13** (none of the six files is a PDF).
**Caveat now attached to all eight:** each was read from the stale build. Each needs one register
check before it is brought to M as open. That check needs the bank.

---

## PART D — SECOND TRANSCRIPT PASS

### ✗ B-2 CORRECTED — referee flag 5 already has M's ruling
The flag was re-graded at **R 251–252** from *no target identified* to *targets identified, run not
attempted*, against named public data: VALD, Kurucz, NIST ASD, BRASS. The D1 tripwire of §11.3.1
rejects 150 of 216 offered assignments — **69.4% from the index alone**, no spectrum, no model
atmosphere; mechanical where current practice is manual, prior where it is posterior.
**M then ruled: "And I agree so run it please."** The run was begun in the same session — Kurucz
format spec obtained, level labels confirmed to carry parent term, outer orbital and level term,
linelists page fetched, data pull attempted.
**Its outcome is not visible in the transcripts searched, and the shipped book still carries the
pre-run wording of R 251–252.** So one of two things is true and the record must say which:
either the run stalled and this is a live task under a standing ruling, or it completed and the
book is stale about it. **I listed the owner as M pending admission. That was wrong — M admitted
it. The owner is Claude, and the task is either to finish the run or to find its result.**
Check needed: register entries after 252 for a Kurucz/tripwire/line-list result.

### ~ B-1 — Q's ten items: no closure found, and the search was narrow
Q's set is stable across builds — the 1.4 press and the shipped press carry the same items, with
**R** (|Cl(ℛ)| for Λ) entered later and **M** restated. One targeted search on three item names
returned no closure for any of A, D, H, I, P, R.
**This is not a negative result.** Per R 1672, it is a statement about a single unaudited search.
Q's ten stay on the board with the caveat unchanged, and the register check stands.

### Cheapest live items, now that the owners are right
| item | cost stated | owner | blocked on |
|---|---|---|---|
| Q item P — the 1,442 split | hours | Claude | nothing but the bank |
| Q item G — complexity literature | hours | Claude | nothing but the bank |
| referee flag 5 — finish or locate the run | days | **Claude, ruling already given** | the bank |
| N-2 — is concavity sufficient? | one computation | Claude | nothing but the bank |

---

## PART E — MEASURED AGAINST THE BANK (`restore-point-2_13.tar.gz`)
Bank extracted: **694 files, 13 dirs — C4 holds.** Register measured directly from
`REGISTER-DATA.md`: **1,352 entries, 1,352 distinct, max R 1700, no duplicates.** Gates NOT run
(context). Nothing written to the work.

| row | verdict against the register |
|---|---|
| **N-1** R 1701/1702 | **CONFIRMED OPEN** — neither id exists in `REGISTER-DATA.md` |
| **B-2** flag 5 run | **CONFIRMED OPEN** — no Kurucz/VALD/BRASS entry after R 252 anywhere in the register. The run has no registered result, so under this project's discipline it did not complete. **Live task, Claude, ruling already given (R 251–252).** |
| **B-5** Q.exch | **CONFIRMED OPEN** — withdrawn R 1168, entangled in the R 1208 dependency cycle (Q.delta → Q.exch → Q.delta, undetected across 248 objects and six audit sets); no closure entry. The grade/status inconsistency is real. |
| **B-7** twenty rows | **CONFIRMED OPEN** — R 630 states it exactly; no closure entry follows. |
| **B-9** E(local register) | **CONFIRMED OPEN** — stated three times in the register, never built. |
| **B-6** Λ_ladder | **CONFIRMED CLOSED** — R 1427 present. My withdrawal was correct. |
| **B-3** flag 4 | **✗ WITHDRAWN — my proposal was already implemented.** The withdrawal ratio is **computed by the press at every build**, and has moved **0.445 → 0.249**. The flag's premise (one observation, cannot be tracked) is superseded by the press itself, and the answer to what it asked — *is it falling?* — is **yes**. |
| **B-1** Q items | **PARTLY SUPERSEDED.** Item **D** moved from blocked to routed at R 244 (three independent routes). Item **R** is characterised: \|Cl(ℛ)\| is a counting problem, pseudo-intents and #P-completeness. Items A, H, I, P show no closure. |

### The three faults of this session, all one fault
1. Λ_ladder — proposed open, closed at R 1427.
2. Referee flag 5 — owner given as M, M had already ruled.
3. Referee flag 4 — proposed a fix the press already performs.
**Each is a status read off a stale generated artefact and handed to M as a question.** The rule
this earns: *before a row goes to M, the register must be asked, not the build.*
