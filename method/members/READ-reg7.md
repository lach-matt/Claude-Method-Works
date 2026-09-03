# READ-reg7.md — the Register, unit 7: the emphasis class (out of source order, at M's direction)

M directed the read to jump to the 1642–1699 cluster the sweep flagged, and to return to entry 290
afterwards. Recorded as a **directed departure** from the chat-81 source order, not a drift.
Instrument `r2-reg7a.py`, golden `r2-reg7a.out` (4,023 B · `6ed594d1`). All instrument checks OK.

## The cluster is not a cluster

The sweep's odd-asterisk test flagged eleven entries between 1642 and 1699, which looked like one
authoring session. Reading them shows the shape is **`X* *Y`** — a bold `**` split so one asterisk
attached to the preceding word and one to the following. That is exactly entry 313's
`is* *iterate**` (reg3-01).

**Measured for that shape rather than for parity, the class holds 275 of 1,635 entries at 429
sites, from entry 238 to entry 1729** — 16.8 % of the record, with the flagged band holding only a
handful of them. The cluster was an artefact of the parity test.

| band | entries |
|---|---:|
| 200–399 | 32 |
| 400–599 | **86** |
| 600–799 | 46 |
| 800–999 | 20 |
| 1000–1199 | 12 |
| 1200–1399 | 23 |
| 1400–1599 | 26 |
| 1600–1799 | 30 |

## A — findings

**reg7-01 — 275 entries carry emphasis that does not arrive.** Each intends a sub-phrase to stand
out inside an italic body. Single asterisks cannot nest inside an italic run: **each pair closes the
body and opens a new italic**, so the page shows one continuous italic and the distinction the
author made is not on it. Three from the record:

- entry 289 — `*What* *fifteen* *counted cannot be settled…` — *fifteen* was to be emphasised.
- entry 290 — `…count of withdrawals* *made* *while printing a* *selection**.` — *made* and
  *selection* were the contrast the sentence is about.
- entry 238 — `…six Q items move from* *blocks: novelty* *to* *blocks: nothing*.` — the two states
  were to be marked.

This is not untidiness. It is **emphasis that does not reach the page**, in a volume whose front
matter says every entry is *"a capitalised headline, then the body in italics"*. Docket 28 / 31.

**reg7-02 — eleven entries must leave a literal asterisk on the printed page.** Where the split also
makes the line's asterisk total odd, one marker cannot close and survives as a character:
**313, 604, 747, 1642, 1643, 1648, 1649, 1652, 1653, 1657, 1681**. Entry 313 is the case already
confirmed by reading at reg3-01; the other ten are the same defect found by measurement.

## B — verified

**Eleven entries the parity test accused are correct as printed.** An asterisk is *notation* in this
corpus, and the sweep's classifier was too narrow — it required a digit before the asterisk and so
missed the term symbols. Acquitted: **26, 27, 1003, 1646, 1673, 1674, 1677, 1682, 1694, 1699,
1774** — carrying `2P*` and `²P*<1/2>` (odd-parity term symbols), `φ*` (Miedema's electronegativity
parameter), and `(3, 0, 1, 1, *, 0, 1, 1)` (a wildcard coordinate). **The sweep's "14 candidates" is
superseded: the true broken set is 11, and the other 11 are the record being right.**

## C — the pass this is consistent with, and why nothing attests it

`REGISTER_AUDIT` R4 records: *"Five forms of entry across the record … **Closed — ruling C.** Every
entry normalised to the settled form (caps headline, italic body); tags removed; no content changed.
Recorded as entry 1725 with Register-1 named as the witness."*

MEASURED: **entry 1725 does not exist** (reg1-05). So the pass that normalised every entry to the
form this class disfigures is recorded at an entry that is not in the register.

**Causation is not claimed.** What is measured is three things side by side: a 275-entry class, a
normalisation whose stated shape matches it, and no seated entry attesting the normalisation. R3
reads the three together. Docket 28 / 2.

## Census

No census row engages the entries scored here. `CENSUS-CLOSURES-reg7.tsv` is header-only.
