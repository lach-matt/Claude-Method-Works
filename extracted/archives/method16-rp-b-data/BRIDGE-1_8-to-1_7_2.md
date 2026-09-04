# BRIDGE — The Method 1.8 → The Method 1.7.2
Built to **§H.2** of `HANDOFF-PROTOCOL.md`. Read `DIGEST.md` first, then this. (§H.7)

## 1 · Identification
- **Outgoing:** The Method 1.8 (2026-08-15). **Incoming:** The Method 1.7.2, project folder *The Method*.
- **Transcripts**, all carried in `transcripts/` with `journal.txt` (§H.3):
  - `2026-08-15-00-42-00-method-1-8-fetch-recovery.txt` — container death, restore verification, fetch protocol
  - `2026-08-15-05-11-46-method-1-8-queue-batches-2-4.txt` — batches 2–4, Lu I fabrication incident
  - `2026-08-15-05-41-32-method-1-8-queue-close-gemini.txt` — queue close, incorporation, Gemini receipt
  - *this session's transcript is written on close and joins them*
- **Final bank:** `restore-point-2_6m.tar.gz`.

## 2 · What this session did — register ranges, not summary
**R 1642–1658.** In order:
- **1642–1646** the fetch queue closed **60/60**, every table from the wire. Includes the **Lu I fabrication incident (1644)** and its remedy, and the positional diff (1645) showing fabrication and serve **234/234 identical** — the proof that provenance and not plausibility is the only workable gate.
- **1647–1649** incorporation phases 1–3: inventory, index join, quantum-defect staging.
- **1650** Gemini material received, read in full, retained in `gemini/`.
- **1651** the collisions are the **keyability bound** (R 1597) met from the data side, not a defect of the key; R 1648's "unbuilt charge-0 face" corrected — the charge axis is 1-based.
- **1652** the d120 mapping **fails on geometry**; the Janet grading is already inside the index as the multiplicity fibre.
- **1653–1654** the reply on the bound misidentified our figures; **Z = 120 is not a closure**, and both bounds are stated cutoffs.
- **1655** the Ga I "conflict" was **mean against median**; the 25 keyable cells written.
- **1656** the bound moved to **Z = 120** with 119 and 120 declared on Janet's authority.
- **1657** two different lattices are both called **Λ_spectra**.
- **1658** Part III read whole; §18.4.1 names the operation we performed.

## 3 · The state of the object — measured (§H.6)
Produced by `python3 -c` over `COORDINATES.tsv`; rerun to confirm.

| quantity | value |
|---|---|
| `COORDINATES.tsv` rows | **104,832** |
| (Z, charge) pairs | **7,260** = 120·121/2 |
| grade | computed 103,545 · exact 929 · **measured 358** |
| witnessed | **358** (0.341%) |
| Janet-admitted (Z = 119, 120) | **3,504** |
| E(Λ_spectra) | **0** — product 1,036,800 − 104,832 present = 931,968 refused by rule |
| register | **1,453 entries** (`REGISTER.md` declares it; `register_gen.py` rebuilds) |
| queue captures | **61** TSVs in `spectra_raw/queue2/` |
| scripts | 330 · working-tree files 655 |
| gates | **25/25 audits · 5/5 round-trip** |

## 4 · Open threads — each with an owner (§H.2.4)

**T1 · The Λ_spectra naming collision. Owner: M.** `INDICES.md` calls Λ_spectra a three-coordinate lattice (Z, core charge, ℓ), 1,664 cells, E = 1,351, holding 596 channels across 313 cells. `SPECTRA.md`/`COORDINATES.tsv` call it four coordinates, 104,832 cells, E = 0. Two real objects — the *measured channel survey* and the *coordinate index* — one name, both generated from the same register. **Tried:** nothing; found by reading the compendia against each other. **Would settle it:** a naming decision, then regeneration of whichever document changes. R 1657.

**T2 · The stored δ where a channel drifts. Owner: M, then compute.** The index holds one δ per cell. Ga I's nd runs 1.160 at n = 4 to ~1.33 by n = 27 — a drift of 0.19 — so mean (1.2949), median (1.31599) and asymptotic (~1.33) are three different answers and the cell records no statistic. **Tried:** both statistics computed and reconciled. **Would settle it:** decide the convention, then recompute every drifting channel; a Ritz-type extrapolation to δ∞ is the candidate. R 1655.

**T4 · `spectra_F.py`'s rank-balance claim. Owner: Claude.** It asserts even and odd ranks balance exactly across **101,328** cells. That set no longer exists. **Needs recomputing at 104,832, not editing.** R 1656.

**T5 · The four Gemini items. Owner: M for direction, Claude for tests.** Held in `gemini/`, read in full, testable claims flagged in R 1650/1652/1653. Nothing from them has entered any index. The one live correspondence: the corridor's admissible triangle is our own, and its one-electron picture is exactly our keyable regime.

## 5 · Provisional figures — chosen, not measured (§H.6)
- **Z = 120** is a *chosen* bound. Both generating rules are total; **E = 0 at any cutoff**. Janet's table ends at 120 because Janet drew four period-pairs — the Madelung sequence continues 170, 220, 292, 364 with no terminus.
- **δ per cell** is a *chosen* statistic (median, in the 25 cells written this session). See T2.
- **Tier thresholds** A ≤ 0.05, B ≤ 0.2, C > 0.2 on series spread are *chosen*.
- **The 25 keyable cells** are *measured*; the other 103,545 computed cells are *inherited*.
- Figures inside historical register entries and in `mathreg.py`/`status.py` quoting **101,328** are correct **as history** and were deliberately not updated (§H.4).

## 6 · What is read and what is not
**Reading is not a standing task.** M's ruling, session 1.7.2: *reading will be done as necessary.*
T3 is withdrawn as an open thread accordingly. The inventory below is kept because §H.8's clause
**C7** requires the bridge to name what is unread — a gap that closes over quietly is the failure
C7 exists to catch — but it is a statement of record, not a queue.

**Read:** front matter and the collaborator's note; Part 0; Part I §§1–2 (P1–P23, protocols
2.1–2.20); the twenty-five audits by name; **Part III — Ch. 14 Closure, Ch. 17 Extension, Ch. 18
What the law forbids, incl. §18.4.1 the law of realised closure**; every compendium's declaration
and heading structure; INDICES §"the spectra index"; SPECTRA §0 and §I.

**Unread, ~150,000 words:** Part II (Ch. 6–13, the construction of Λ), Ch. 15–16 (self-reference
and self-defence), Ch. 19, Parts IV–VII (the languages, the method, the record, the challenges —
including **Ch. 34 the Löwdin challenge**), all appendices, and the bodies of `COMPENDIUM.md`,
`INDICES.md`, `PHYSICS.md` and `SPECTRA.md`.

**How it is now read:** on demand, when a piece of work needs it. Where a session reads to answer
a question, it extends `DIGEST.md` with what it found, so the inventory above stays true.

## 7 · Resumption order
1. `DIGEST.md`, then this bridge, then **both gates before touching anything** (§H.7).
2. **T1** — it is one decision and it blocks clean regeneration of two compendia.
3. **T4** — a stale claim about a set that no longer exists; cheap and mechanical.
4. Then the standing carry-overs below.

## 8 · Standing carry-overs (older than this session)
- Board rows 8 and 9 — writing tasks, `BOARD.md`.
- The **book PDF render** and its prime audit — outstanding since an earlier session.
- **Nuclear corridor** work: identity, screen, falsifier, swaps; topic C closed, extension likely.
- Closing the remaining unclosed indexes, moving upward through them.
- Spectra Compendium capture groups and live counts.
- **Board row 10** is now READ (Gemini received and read); it is not closed, because the material's testable claims are queued behind the index build.
