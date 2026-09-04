# BRIDGE — The Method 1.7.3 → next session
Built to **§H.2**. Read `DIGEST.md` first, then this (§H.7). Handoff begun under **§H.10**.

**BEFORE ANY WORK — the practice clauses, because 1.7.2's were lost at the seal (R 1670).**
> §H.11 stands: no tool call returns more than ~25 lines; a census is written to a file and
> reported by its shape; the gates run at baseline and at close and otherwise only when
> something generated has changed; rulings sharing a subject are batched; §H is consulted by
> clause. **A change of practice survives a handoff only if it is REGISTERED** — the bridge
> carries facts and threads, the register carries rulings, and a practice with neither dies.

## 1 · Identification
- **Outgoing:** The Method 1.7.3 (2026-08-15). **Incoming:** next session, project folder *The Method*.
- **Final bank:** `restore-point-2_10.tar.gz`. Predecessor: `restore-point-2_9.tar.gz`.
- **Predecessor bridge:** `BRIDGE-1_7_2-to-next.md`, still in the tree, still the record of T1–T8.
- **Inherited transcripts** in `transcripts/` with `journal.txt`.

## 2 · What this session did — register ranges
**R 1669–1675.**
- **1669** `DIGEST.md` extended from the bridge; the Λ_spectra / Λ_spectra^obs name collision closed in it.
- **1670** **§H.11 adopted** — and the finding that a practice survives only if registered.
- **1671** **C6 passed on 3 of 5 threads** — it detected threads by the same expression that required
  an owner, so an ownerless thread could not fail it, only vanish from it. Repaired; negative-tested.
- **1672** **The archives are not disjoint — the probe was.** `spectra_raw/queue2/` was never searched.
- **1673** **T2 answered by measurement: the store's statistic is the MEDIAN.**
- **1674** The store has **no generator**; `phase4.py` only reads it. Bracketed levels admitted.
- **1675** **`store_gen.py` runs: 353 of 358 exact-count series confirm the median — the §2.8 second
  route now exists.** And R 1674's bracket ratio withdrawn: 1.9% archive-wide, not half.

## 3 · The state of the object — measured
Read with `grep -acE '^### [0-9]+' REGISTER.md`, `python3 store_gen.py`, `tar tzf … | wc -l`.

| quantity | value |
|---|---|
| `COORDINATES.tsv` rows | **104,832** — untouched this session |
| register | **1,471 entries, R 165–1676** |
| `MEASUREMENTS.tsv` | **554 rows** on 158 cells; 409 usable δ, 145 voided |
| `MEASUREMENTS-DERIVED.tsv` | **486 series**, three perspectives + bracket grade |
| member count reproduces | **358 of 486** |
| median = stored δ | **353 of 358 (98.6%)** |
| bracketed members | **114 of 5,867 (1.9%)**, 84 of them Na I |
| gates | **25/25 audits · 5/5 round-trip** |
| bank | **662 files · 7/7 certificate clauses** |

## 4 · Open threads — each with an owner (§H.2.4)
**T2 · Which statistic the cell's δ uses. Owner: M — but it is now a RECORDING, not a choice.**
R 1673/1675 measured it: the median, 353 of 358. **What would settle it:** M's word written into
`SPECTRA.md`'s declaration, so the file states what the computation does.

**T5 · The four Gemini items. Owner: M for direction, Claude for tests.** All four tested. The
fourth: Madelung as minimisation of I(n,ℓ) = (n+ℓ) − ε/n holds for EVERY ε from 0.01 to 11.99, so ε
carries no physics and the functional is a relabel. **Nothing from Gemini has entered any index.**

**T6 · The standing store. Owner: M — RULED THIS SESSION, mechanics half-built.** M: *the store is
authoritative; each cell is a statistical value; expand the index to show all three values per cell,
each a perspective of the whole definition.* `store_gen.py` delivers the values. **What remains:**
it inherits the LIMIT ASSIGNMENT from the store, so the SERIES CONSTRUCTION is still ungenerated and
C3 does not yet cover the store. A round-trip clause is the last step.

**T7 · Is `mult` the ground state's or the parent's? Owner: M.** R 1665. One coordinate name doing
two jobs; 69 series carry the parent's. A.cert does not admit adding a coordinate, so this is a
definition question. **M ruled that NO CELLS SHOULD BE COST and asked for an elaboration of the
issue. THE ELABORATION WAS NEVER DELIVERED — it is owed, and it blocks further neutral incorporation.**

**T8 · The 145 voided δ. Owner: Claude, on M's direction.** Where a parent's limit was never
published the series cannot be defected at all — E measuring the world rather than the drawing.

**T9 · The generator's residue. Owner: Claude.** **68 series recover no members; 128 recover a count
disagreeing with the store.** Neither diagnosed. Likely causes untested: term-string variants,
J-splitting conventions, and the staging's own n-range cuts. **This is the first thing to compute.**

## 5 · Provisional figures — chosen, not measured (§H.6)
- **Z = 120** — *chosen*. E = 0 at any cutoff.
- **Tier thresholds** A ≤ 0.05, B ≤ 0.2, C > 0.2 — *chosen*, and R 1666 shows they graded the wrong
  quantity on 55% of rows.
- **The asymptotic perspective = the deepest member** — *chosen* definition, not derived. An
  extrapolation to n → ∞ was not attempted.
- **Reduced-mass R_M from standard atomic weights** in `store_gen.py` — *chosen* isotope convention.
- **The context estimate triggering §H.10** — *judged*. No counter exists.
- Historical figures quoting **101,328** stand as history (§H.4).

## 6 · What is read and what is not
**Reading is on demand (R 1668), not a queue.** Newly read this session: `handoff_cert.py` at source,
`phase4.py` head, §H.2/§H.5/§H.7/§H.8/§H.10 by clause, `store_gen.py`'s inputs in full.
Still unread: Part II (Ch. 6–13), Ch. 15–16, Ch. 19, Parts IV–VII incl. Ch. 34 (Löwdin), all
appendices, and the bodies of COMPENDIUM, INDICES, PHYSICS and SPECTRA. Roughly 150,000 words.

## 7 · Resumption order
1. `DIGEST.md`, this bridge, then **both gates before touching anything**.
2. **T9** — diagnose the 68 and the 128. Until then the generator's coverage is unexplained, and an
   unexplained 26% is not a residue, it is an unread finding.
3. **T7's elaboration** — owed to M, and it blocks neutral incorporation.
4. **T6's last step** — a round-trip clause so C3 covers the store.
5. **T2** — write the median into `SPECTRA.md`'s declaration.
6. Board rows 1 and 2, then the standing carry-overs.

## 8 · Standing carry-overs
- **`BOARD.md` is stale** — built at R 1614, register now 1675. The reassessment has NOT been written back.
- **`COMPENDIUM.md` line 767** quotes 337 / 101,328 in the present tense.
- **`roundtrip.py` covers five markdown artefacts and no JSON** — and no TSV, which is why the store
  escaped C3 for as long as it did.
- The **book gap**: the book cites nothing past R 1225; the register is at 1675 — **450 entries**.
- Book PDF render and its prime audit; nuclear corridor; remaining unclosed indexes; board rows 8 and 9.
- **Four NIST captures still pending live re-fetch via pasted URLs** — unrelated to the store, which
  is fully covered by held data.
