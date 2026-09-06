# REGISTER QUEUE — everything earned after R 1700, reconciled across seven chats
Built 2026-08-15 in the register chat. **PROPOSED, NOT WRITTEN.** No bank is uploaded; nothing
here has touched `REGISTER-DATA.md`, and nothing may be written from this file until it has.
Sources: the project folder (read as files), and the project's chat transcripts (read via search).

---

## 0 · THE GOVERNING FINDING OF THIS CHAT

**Three chats each claimed R 1701 onward, independently, from the same bank.**
`restore-point-2_13.tar.gz` closed at R 1700. Since then, work has run in parallel chats, none of
which could see the others' numbering, and the register was the shared resource none of them held.

| chat | claimed | content |
|---|---|---|
| *Lowdin challenge solution work* | R 1701, R 1702 | clique-3 · P1 |
| *The Books* (press 1.8.4) | R 1701 – R 1709 | the press run, nine entries |
| *the Lowdin challenge 2* | R 1707, R 1708, R 1709 | diagonal · concavity · self-correction |

**R 1701–1709 collide three ways and R 1707–1709 collide twice.** Verified at source: `grep` on
`REGISTER-2_13.txt` for `^ {0,3}170[1-9]\.` returns **0**. No id in the range exists. Every claim
is against empty ground, so no entry is wrong — but only one sequence can be written.

*This is the parallel-chat form of the fault the record already knows: R 1670, a practice adopted
at close with nowhere to live, dies at the seal. Here it is an ID adopted mid-session with no
allocator. The register is a single-writer object and the work has gone multi-writer.*

**Owner: M.** The proposal below orders by content dependency; that ordering is CHOSEN, not
measured, and is §5-of-a-bridge material until M rules.

---

## 1 · A SECOND MEASUREMENT: THE REGISTER'S OWN COUNT IS INSTRUMENT-DEPENDENT

Three chats reported three sizes for the same register. Measured here on `REGISTER-2_13.txt`:

| instrument | count | who reported it |
|---|---|---|
| `^ {0,3}[0-9]{3,4}\. \*\*` — bolded headings | **1,352** (1,352 distinct, 0 duplicates) | *the Board* |
| `^ {0,3}[0-9]{3,4}\. ` — any numbered heading | **1,483** | *The Lowdin Challenge 1.2* |
| stated on `REGISTER-DATA.md` at the 1.8.3 seal | **1,486 distinct ids** | `BRIDGE-1_8_3-to-next.md` |

Max id **1700** under every instrument; no duplicates under the strict one. The spread is 134 lines
between the loosest and strictest reading, and a further 3 between the extract and the source.
**None of the three is wrong; there is no declared instrument.** R 1617 already recorded the
adjacent fault — a wrapped line beginning with digits reads as a false heading.
**Owed: one declared counting instrument, named in `DIGEST.md`, so the certificate's register
clause measures one quantity.** Owner: M or Claude on M's word. Not adjudicated here.

---

## 2 · THE PROPOSED SEQUENCE

Ordering: by content dependency, then by chat close. Provenance is marked on every entry.
**`[FILE]`** = drafted against an artefact read in full in the project folder.
**`[TRANSCRIPT]`** = the artefact exists only inside a chat container and was NOT uploaded;
the finding is real but the wording must be drafted from the file, not from a summary
(the standing correction, §2.14).

### From *Lowdin challenge solution work* — `BRIDGE-LOWDIN-SESSION.md`, `CLIQUE3-FINDING.md`, `P1-FINDING.md` **[FILE]**

**R 1701 — THE CLIQUE-3 OBSTRUCTION IS NOT AT THREE ELEMENTS, AND R 1517'S ATTRIBUTION IS
CORRECTED.** 106 corridors rebuilt from `brack.py`'s own construction; 735 edges, density 0.132,
max clique 3, 10 isolated vertices, stabbing points 0.7071 / 1.7071 / 2.4409, agreeing by two
routes (greedy-by-right-endpoint and brute-force max clique). Generating form **g(p) =
1/(√(p+2) − √p)**; a canonical corridor is the band (g(p−2), g(p)); 32 of 106 canonical, in four
intervals only — p=0 (26 members), p=2 {La, Gd}, p=3 {Ac, Th, Cm}, p=5 {Lr}. The even and odd
sub-chains interleave and p=3 overlaps p=2 on (1.3660, 1.7071): **that overlap is why the answer
is 3 and not 4.** R 1517 reads *"forced by three elements — boron, lanthanum and lawrencium."*
**There are 205 maximum cliques, not one:** slot 1 admits 51 interchangeable elements, slot 2 five,
slot 3 **Lr alone in all 205**; 57 of 106 vertices appear in some maximum clique. **Only lawrencium
is forced.** Naming B and La is the object-versus-observer coordinate fault (R 1578, R 1672's
negative-from-scope) — a property of a class attributed to the representative the scan reached
first. Lr is sole member of the p=5 band because it is the only entrant with p=5 bracketed at p±2
— **a fact about where the table ENDS, not about lawrencium**, consistent with R 1696's declared
bound. *Script `clique3.py`; artefact `CLIQUE3-FINDING.md`.*

**R 1702 — P1 ANSWERED: THE CORRIDOR IS AN INSTRUMENT OF THE CANDIDATE FORM'S SHAPE, AND TWO OF MY
OWN CLAIMS WERE WITHDRAWN GETTING THERE.** ν = A(n,ℓ) − a·B(n,ℓ) makes each step one linear
inequality in a. The verdict MOVES with B, so the corridor measures the form and not the atom.
Because the constraints evaluate B only at integer p ∈ {0…7} and translation and scaling cancel in
the differences, **a candidate form IS an increasing 8-vector** — the class is finite-dimensional
and samplable. 30,000 uniform increasing vectors: 2,206 feasible, cliques 3/4/5 at 1,843/354/9.
5,000 from the concave cone: **5,000 feasible, clique 3 in all of them.** WHAT SURVIVES: *if the
ordering functional is concave in the node count, the table is representable and requires exactly
three parameter values* — sufficiency measured, **a proof owed and not attempted**. The stabbing
points belong to ν alone (0.7071/1.7071/2.4409 under √p; 1.5/7.5/24.0 under p/(1+p)); the surds are
ν's coordinates for the number three, never its content. **TWO SELF-CORRECTIONS, REGISTERED NOT
HIDDEN (the R 1672 / R 1675 pattern):** (i) *concavity is NECESSARY* — WITHDRAWN, 2,928 non-concave
vectors are feasible; the claim came from generalising seven named functions, P5 and §2.14 exactly;
(ii) *local concavity at p = {2,3,5} is the condition* — WITHDRAWN, it admits 1,702 infeasible and
misses 1,394 feasible; an enrichment, not a condition, and **the exact condition is not
characterised.** THE SIX — La, Gd, Ac, Th, Cm, Lr — that refute a linear or convex form (boundary
exactly at β = 1 in p^β) **are exactly the members of the three upper canonical bands of R 1701**,
from two computations sharing no code path. La and Ac are where Madelung is false (R 1594).
**The exceptions are not noise around the rule; they are the entire measurement.** Löwdin's
challenge is NOT met: a shape constraint by refutation is not a mechanism. *Scripts `p1.py`,
`p1b.py`, `p1c.py`; artefact `P1-FINDING.md`.*

### From *The Books* — press session 1.8.4, `PRESS-CERTIFICATE-1_8_4.md` **[FILE]**

**R 1703 — M'S RULING: PRESS THE SOURCE AS IT STANDS.** A truthful snapshot, open threads rendered
as open. Six documents pressed against `restore-point-2_13`; network disabled, no fetch attempted
or needed. The book pressed TWICE and the second pass is the true one: pass 1 rebuilt byte-identical
to the banked PDF, `pagemap.py` then located 486 of 487 headings and rewrote `PAGEMAP.tsv` with 136
changed lines — **the banked contents was stale and is now true**, R 665's mechanism working as
designed. Gates 25/25 · 6/6 at baseline and at close.

**R 1704 — THE SIX PROJECT FILES NAMED `.pdf` ARE NOT PDFs.** Two are UTF-8 text extractions
(702,517 and 562,568 chars); four are zips of page rasters (56, 38, 20, 12 jpeg). All six fail
`pdftotext` with *Couldn't find trailer dictionary*. Had they been staged as audit inputs on the
strength of their names, FIDELITY and PROJECTION would have compared source against a derivative of
the artefact. **The R 1672 pattern and the `destination_url` guard are one guard: check what
arrived, not what it is called.** *Found independently in two chats — the press session and the
board session (its row B-13). Merged here as one entry; the duplication is itself the R 1670 shape.*

**R 1705 — THE PRESS QUOTE-BRANCH REPAIR, FENCED AND REVERSIBLE.** `press_compendia.py` line 211
only: the blockquote branch rendered one line at a time while the body branch has joined
consecutive lines since R 632, so a `**bold**` statement wrapped across two `> ` lines printed its
asterisks. Mathematical Compendium **4 leaks → 0**. Original preserved in `UNDO-PRESS-REPAIR.txt`;
no source, no index, no `REGISTER-DATA.md` touched, so **no A.cert operation is involved**.
R 259's instance-fix pattern: a fix applied to one branch and never to its neighbour.

**R 1706 — THE §26 REGISTER TRIPWIRE NO LONGER FIRES, AND THAT IS A FINDING.** The book press
prints `F.3: E(G) not recomputed: min() iterable argument is empty`. Measured across 62,835
characters and 44 headings of §28: 3-digit matches 0, 4-digit 0, any leading number 1. The section
did not outgrow a numbering — **it no longer prints a numbered entry list at all**; R 633 moved the
entries to the Register Compendium and §28 kept the argument as prose, *"one thousand one hundred
and seventy-one claims…"*, spelled not enumerated. Per P8 the failure is a true answer and
therefore a bound: **the book can no longer recompute its own register range at build.** It fails
loudly rather than printing a stale number. Per the null protocol the gap wants a different
instrument — a count read from `REGISTER-DATA.md`, not a regex over prose. **NOT BUILT; M has not
ruled.** *Note: this bound is the same object as §1 of this queue — the register's count has no
declared instrument. Two chats reached it by different routes.*

**R 1707 — `artefact_audit` WIDENED TO SIX DOCUMENTS; R 995'S OMISSION CLOSED.** The Physics
Compendium, omitted since register 901, now reads 12 pp · 40,062 chars · 0 glyphs · 0 markup ·
0 lost statements. Closed in the second instrument.

**R 1708 — THE P FAMILY RESTORED TO `QUEUE.md`.** `mathreg.py` held 17, `MECHANISMS.md` 17,
`QUEUE-LOG.md` 17, `QUEUE.md` **zero** — the 1.6.1 rollback rebuilt the queue from transcript and
the list did not survive. Restored from `MECHANISMS.md` with the rollback recorded in the block;
previous state at `QUEUE.prev.md`. **MECHANISM LISTS AGREE.**

**R 1709 — THE ZENO STEP CACHE SERVES A STALE VERDICT AFTER AN INSTRUMENT CHANGES.** `zeno.py`'s
`step()` keys on the step's NAME, so `.zeno/artefact_audit.json` replayed the five-document result
after the instrument had been widened, printing five rows twice. **An audit rerun after an
instrument change must clear `.zeno/` or pass `force=True`, or its pass is a pass of the OLD
instrument.** Same family as R 998 and R 649 — except this guard did not fire at all; it answered
from memory. Cache cleared, step relabelled, sixth row appeared.

**R 1710 — FIGURE ASSERTIONS CORRECTED TO MEASUREMENT, AND THE PROPOSED RULE REFUTED BEFORE
ADOPTION.** Index of Indices 4 → **5** (R 993 moved `fig-spectra-lattice.png` in; five referenced,
five render); Spectra 0 → **3**, so an under-asserted document is no longer silently unchecked. The
book's 33 and the Register's 0 were NOT touched: the book press walks `figures/` rather than reading
image tags, and the Register's single apparent reference is **R 1848's own literal example**
`![caption](file.png)` — a register entry about figure syntax, read by a regex as figure syntax. A
rule deriving expectation from source refs would have broken the book and swallowed R 1848.
**Computed before proposing (P5, §2.14).**

**R 1711 — SELF-CORRECTION: §H.11 BROKEN BY AN UNBOUNDED CENSUS, AND THE CENSUS IS VOID ANYWAY.**
A parity census over `REGISTER-DATA.md` printed many hundreds of lines in one tool call against
§H.11's ~25-line clause. **Registered, not hidden.** And the measurement is VOID as a fault count:
at source level entries interleave bold, italic and notation asterisks across wrapped lines, so
parity cannot separate markup from content — **which R 1565 already established.** The six leaks
are visible in the RENDERED text and nowhere else; parity on the generated `REGISTER.md` was the
right instrument at the right level. *Six asterisks in the Register (source lines 5822, 5830, 5834,
5846, 5850, 5866) stand DISCLOSED, not repaired, on M's ruling: `REGISTER.md` is generated from
`REGISTER-DATA.md`, so repairing them means editing the record. No claim is altered, only emphasis.*

### From *The Lowdin Challenge 1.2* — the bank-extraction session **[TRANSCRIPT]**

**R 1712 — THE LÖWDIN SESSION'S OWN ARTEFACTS WERE NEVER IN THE BANK.** `p1.py`, `p1b.py`,
`p1c.py`, `clique3.py`, `P1-FINDING.md`, `CLIQUE3-FINDING.md` searched by name and by content across
all 694 files of `restore-point-2_13`: **absent.** They were written inside the previous session's
container and never banked; `BRIDGE-LOWDIN-SESSION.md` was the sole surviving record of the 205
cliques and the concavity result. **Confirmed at source: the register contains neither R 1701 nor
R 1702.** *The R 1670 shape again — a result produced outside the sealed tree does not survive the
seal unless something carries it. What carried these was M's upload to project knowledge, not the
bank.*

**R 1713 — SELF-ERROR: I WROTE INTO THE BANK TREE, THEN OVER-CORRECTED AND DESTROYED FOUR OF ITS
FILES.** Importing `ground.py` wrote a `.pyc` into the bank tree and the first manifest read 695.
Correcting it I deleted the whole `__pycache__`, taking the bank's own four files with it and
dropping to 690. Restored from the archive; **C4 holds at 694.** Two faults, one shape:
self-generated output entering the data (M's standing correction), then an over-broad correction.

**R 1714 — EIGHT `-2_13` EXTRACTS BUILT AND ROUND-TRIP VERIFIED.** 21/21 source files recover
verbatim from their emitted copies; each carries a header naming the bank, its sha256 and each
source's own hash, so a stale snapshot cannot pass as current. `brack.py` reproduced exactly: **19
distinct bound values across 106 atoms**, La (0.7071, 1.7071), Ac (1.3660, 1.9841), Lr (1.9841,
2.4409). `ground.py` carries clean provenance — NIST ASD 5.12, DOI 10.18434/T4W30F, retrieved
2026-08-09, register 1306, header stating *this file is READ, not computed*. Node counts run
exactly 0–7, independently confirming P1's 8-vector claim.

### From *the Lowdin challenge 2* — `BRIDGE-LOWDIN-SESSION-2.md`, `DIAGONAL-FINDING.md`, `FEASIBILITY-FINDING.md` **[TRANSCRIPT — FILES NOT UPLOADED]**

*This chat numbered its own owed entries R 1707–1709. Those ids are taken above. Renumbered here;
the content is unchanged and is M's to reorder. **The three artefacts are not in the project folder
and must be uploaded before these are written** — drafting them from a transcript summary is the
fault §2.14 names.*

**R 1715 — THE DIAGONAL READING.** Four facets live on single Madelung diagonals; ν is
one-variable at fixed M; the six refuting steps of R 1702 are proved as interior-of-diagonal
entrants. *Wording owed to `DIAGONAL-FINDING.md`.*

**R 1716 — δ IS MEASURED CONCAVE ALONG FIVE DIAGONALS, 7/7.** Five cores and charge states (K, Rb,
Sr II, Cs, Ba II); **the shape is charge-invariant while the order is not** — on the Kr core Rb I
orders 5p < 4d and Sr II orders 4d < 5p (R 1304's reordering, reproduced from held data) and both
are concave. *That is the split the work has circled since R 1311: the shape is a one-electron
property of the core, where the atom sits on it is the many-electron amplitude.* Facets 1–2
confirmed at Cs I (−1.308, −3.281); facets 4–5 stated UNTESTED for want of a Rn-core d/f channel —
**superseded by R 1719 below.** On Cs I's measured δ, 5d enters first for 0.411 < a < 0.887 —
non-empty, interior, and it excludes a = 1, so ν is still not n\* (R 1457 kept) and `a` is still
undelivered (R 1311, unchanged). Physically: penetration saturating, f centrifugally excluded
(R 1255's gate). **The amplitude `a` is untouched and Löwdin's challenge stands.**

**R 1717 — SELF-CORRECTION: I PROPOSED A SERIES-CONCAVITY TEST R 1457 HAD ALREADY CLOSED.**
*M's standing direction, again: everything needed is contained in the record.*

### From *the Lowdin Solution 2.1* — `ONFOLDER-FINDING.md`, `onbank.py` **[TRANSCRIPT — FILES NOT UPLOADED]**

**R 1718 — `charge` IS 1-BASED AND R 1672 FIRED ON MYSELF.** In `COORDINATES.tsv` `charge` is the
SPECTRUM NUMBER, not the ion charge: charge = 1 is the neutral, Ra II is charge 2. My first pass
queried charge = 0 for neutrals, got zero rows, and was one keystroke from reporting *"Rb I, Fr I
and Rn I are absent from the index"* — a negative that would have been a statement about my query.
The convention is consistent with the index's own arithmetic: charge runs 1…Z, so Σ Z = 7,260 pairs.

**R 1719 — FACET 1 AND FACET 4 ARE ONE INEQUALITY, AND FACETS 4–5 WERE NEVER BLOCKED ON THE Rn
CORE.** On a Madelung diagonal, p = M − 2ℓ − 1, so ℓ alone fixes p and consecutive ℓ steps p by
two. M odd carries facets 1–2, M even carries 4–5. In channel defects of one closed core:
**facet 1 = facet 4 = δ(f) − 2δ(d) + δ(p)**; facet 2 = 2δ(f) − 3δ(d) + δ(s); facet 5 = δ(d) −
2δ(p) + δ(s); facet 3 is the one chord mixing parities. **Five facets, four distinct diagonal
conditions.** So facets 4–5 need any species with measured δ at ℓ = 0,1,2,3 — **the folder holds
43** — and the board's *"untested for want of a Rn core"* is superseded; the Rn-core INSTANCE
remains a separate open question. Instrument checked before use: Cs I facets 1–2 reproduce at
−1.30781, −3.28301 against the bridge's −1.308, −3.281. Hg II satisfies both M=8 facets (−0.86980,
−0.57840). **The pooled counts 10/43 · 13/43 · 31/43 ARE NOT RATES** — the population spans
hydrogenic species where δ(d) ≈ 0 and heavy species where the d channel has collapsed, and pooling
those is the operation this project forbids. Split on δ(d), facet 1/4 satisfaction separates 41/43
and the smallest true satisfier is **Ti IV at 0.6202 — the exact value `SPECTRA.md` uses as its own
Janet-collapse boundary example.** Stated as an ASSOCIATION, not a condition; R 1702 records what
promoting an enrichment costs. *Computed from `COORDINATES-2_13.csv`, grade `measured` only, 358
rows on 75 species. No fetch. Nothing written.*

### From *the Board* and *the Board 1.1* — `BOARD-3-REVISED.md` **[FILE]** + transcript

**R 1720 — THREE PROPOSED BOARD ROWS WERE WRONG, AND ALL THREE ARE ONE FAULT.** (i) Λ_ladder
proposed OPEN — **closed at R 1427** (fourteen ladders, nine cells, E = 0 on (seat, kind, Zcross)
once the X-ray pair is seated at subvalence; the Index of Indices PDF prints it open on the *old*
coordinates). (ii) Referee flag 5's owner given as M — **M had already ruled**, *"And I agree so run
it please"*, at R 251–252, and the run was begun. (iii) Referee flag 4 proposed a fix **the press
already performs at every build** — the withdrawal ratio is computed each press and has moved
0.445 → 0.249, so the flag's premise is superseded and its question is answered: yes, it is falling.
**Each is a status read off a stale generated artefact and handed to M as a question.**
THE CLAUSE EARNED: ***before a row goes to M, the register must be asked, not the build.*** And its
general form: **a status read from a generated artefact is a statement about the build date** —
R 1672's clause arriving by a new route. *Verified against the register: R 1701/1702 absent
(confirmed), flag 5's run has no registered result and therefore did not complete, Q.exch open,
the twenty channel rows of R 630–631 open, E(local register) never built, Λ_ladder closed at
R 1427, item D routed at R 244.*

**R 1721 — THE RETRIEVAL LAYER CAN FIND A CLOSURE BUT CANNOT CERTIFY AN OPENING.** Project
knowledge attaches only inside a project chat and lives in the retrieval layer: `/mnt/project` is
searchable and readable, **never executable and never countable**. Under R 1672 the scope of a
retrieval search cannot be audited, so a negative from it stays a statement about the search — but
a POSITIVE is decisive. **The instrument that kills the R 1720 fault class is precisely the one
that cannot certify openness.** Honest use: run register checks to knock out anything wrongly
listed open; carry survivors to M marked *"no closure found — search-scope unaudited"*, never
*"open"*. *Corollary recorded in the same chat: a bridge cannot assume the project folder attaches;
it does not in a chat outside the project.*

---

## 3 · FLAGS — carried out of this chat, not closed in it

**F1 · `BOARD-3-REVISED.md` CARRIES A WITHDRAWN CLAIM AS CURRENT.** Its §B-10 states P1's result as
*"strictly concave … are **necessary**"* and its row N-2 asks *"is concavity sufficient as well as
necessary?"* **Both are the withdrawn first statement.** `P1-FINDING.md` §2 and the Löwdin bridge
§5.4 record the opposite: concavity is **SUFFICIENT, NOT NECESSARY** — 2,928 non-concave vectors are
feasible — and N-2's question is already answered at 5,000/5,000. The board was written from the
chat record ahead of the corrected artefact. **The board must not go to M in this state.** *This is
R 1720's own fault, committed by the chat that discovered it.*

**F2 · C4 DISAGREES BETWEEN TWO SESSIONS ON THE SAME ARCHIVE.** `PRESS-CERTIFICATE-1_8_4.md` reads
694 files **+ 14 dirs**; `BOARD-3-REVISED.md` §E reads 694 files, **13 dirs**; `BRIDGE-1_8_3` and the
digest carry 694 files without a directory count, against 679 + 12 at 2_12. Files agree, directories
do not. **One measurement, one instrument, before the next certificate cites C4.**

**F3 · Rb I STORE GAP, T9-SHAPED** — raised in *the Lowdin challenge 2*, unexamined here.

**F4 · `CHAPTER-LOWDIN.md` §8 REWRITE, STILL OWED.** It lists P3 and Demkov–Ostrovsky as open;
they closed at **R 1617** and **R 1621**. Clique-3 and P1 are now answered. P4 stays as a
**prohibition, not a gap**. *§34 of the book has the same fault.* Needs the bank.

**F5 · R 1517'S TEXT IS NOT SELF-CORRECTING.** R 1701 corrects its attribution; §H.4 says history is
not rewritten, so the correction lives in the new entry and the old entry stands. **Whether the
chapter and compendium quoting R 1517 must carry a pointer is M's call.**

**F6 · THE REGISTER'S COUNTING INSTRUMENT IS UNDECLARED** — §1 above. Also R 1706's bound: the book
can no longer recompute its own register range, and the replacement instrument is not built.

**F7 · NOTHING IN THIS FILE CAN BE WRITTEN WITHOUT THE BANK.** Writing requires
`REGISTER-DATA.md`, then `python3 register_gen.py > REGISTER.md` **with the redirect** (R 1700's
recorded failure), then 25 audits and round-trip. Three artefacts named `[TRANSCRIPT]` above must
also be uploaded first.

---

## 4 · WHAT THIS CHAT DID NOT DO

No write to `REGISTER-DATA.md`, `COORDINATES.tsv`, `MEASUREMENTS.tsv`, any board, any chapter or any
generated artefact. No gate was run — `indices.py` and `roundtrip.py` are not present and
`/mnt/project` is not executable. The index stands where R 1696 left it: 104,832 cells, 7,260 pairs,
E = 0, untouched. The ~150,000 unread words remain named as unread (§H.8 C7).
