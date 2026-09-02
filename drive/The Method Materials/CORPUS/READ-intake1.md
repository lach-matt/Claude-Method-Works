# READ-intake1 — chat 130 — Segment A: intake of LOWDIN-DELIVERY-1-part1 and THREEBODY-DELIVERY-1

**Scope.** RUL-128 item 4; DEF-129 item 7; docket 38 (the record-carried class). Nothing enters a volume. Instruments
**r2-lw1** (65 lines) and **r2-tb1** (120 lines), both banked and re-run deterministic. Every figure below is MEASURED
by those instruments unless marked INFERRED. The deliveries' text files travel as members under the prefixes `LW1-`
and `TB1-` with bytes unchanged (md5 preserved; every file ends in a newline, so no byte was added). The five PNGs
are not members: their md5s are TB1-MANIFEST.tsv's rows; the zips on Drive remain the store.

**Location, MEASURED (Drive search `title contains 'DELIVERY'`, two pages).** Both zips are inside the two subfolders
`LOWDIN-DELIVERY-1/` (`1aQe7IofPbSQrudSYr_Iq0hgUtTZDlw3Q`) and `THREEBODY-DELIVERY-1/`
(`1iMguyEFqM7OiNa5NQXhVITlvrd7NLVL1`), not at Materials root as HANDOFF-82 recorded — M tidied between chats. Five
copies, two byte-identities: Löwdin 5,371 B · `632f911b7660184880cabb83f6533936` (three copies); three-body 413,058 B
· `f30a60d203a098eb098e156b68a45806` (two copies). No further Löwdin part exists (`-part1` is the only part).
Both zips CRC-clean (`zipfile.testzip` → None). 4 + 20 members as manifested; all 22 manifested files match bytes
and md5; nothing unlisted. Environment MEASURED identical to the deliveries' stated one: Python 3.12.3, NumPy 2.4.4,
SymPy 1.14.0, SciPy 1.17.1, Matplotlib 3.10.8.

## A. Validation block — Löwdin (r2-lw1)

| object (REQUEST-LOWDIN.md) | delivered? | status | evidence |
|---|---|---|---|
| 3 `ground.py` (1306) | YES | **REPRODUCED** | `python3 LW1-ground.py` stdout = LW1-ground-run.log byte-for-byte (294 B, md5 `6bc5a619…`); 108/108 electron counts; 19 subshells; Pd `[Kr]4d10`, Lr `[Rn]5f14 7s2 7p`; Z = 1–108 configurations equal cell-for-cell to r2-ch16y's independent NIST reconstruction (108/108) |
| 1, 2, 4, 5, 6, 7, 8, 10 | NO | **PENDING BANK** (delivery's own status) | LOWDIN-HANDOFF-103.tgz named, not delivered — record-carried |
| 9 (1707–1711) | NO | PENDING BANK + **NOT HELD** (S104 restatement) | record-carried |
| 11 six figures | NO | **NOT HELD** as files | pack104 never sealed (delivery's finding, severity FOUNDATIONAL) — record-carried |
| 12 paper + record | NO | PENDING M's copy | the .pdf is in Prints & Proofs (`1r5_KE69TLo7dqcU3jhS8qbdHFQfC7rz7`, 879,791 B per README; not fetched) |

**1306 / 1307 against the delivered table.** *108 of 108* = 108/108. *Two of nineteen*: the observed opening
sequence and the Madelung order of the same nineteen differ by two adjacent transpositions (5d↔4f, 6d↔5f; four
displaced positions) — the entry counts transpositions (convention now named). La opens 5d at 57, 4f first at Ce 58;
Ac opens 6d at 89, 5f first at Pa 91. Neither entry carries a WARNING. **The Löwdin chain proper (1701–1712) receives
no instrument in this delivery: every figure in Chapter 35 stays record-carried.** Register 1710 ABSENT (17b-01).

## B. Validation block — three-body (r2-tb1)

Every delivered instrument is a **labelled reconstruction** from the transcript of chat `b778e075` (concluded
2026-08-23 22:06:58 UTC); no original md5 exists. A match is therefore *the reconstruction reproducing the record*.

| object (REQUEST-THREEBODY.md) | delivered? | status | evidence |
|---|---|---|---|
| 1 `tb_audit.py` = `audit.py` (1717; §36.2) | YES (reconstructed) | **REPRODUCED** | stdout = audit.log byte-for-byte; 78/78; |S| = 6 · 2 · 1 |
| 2 triangle-form closure (1716) | YES; `3B.tri` is a label, not a file | **REPRODUCED + RE-DERIVED** | caps 3–12 cells 24·52·95·156·238·344·477·640·836·1,068; meet 12·111·477·1,488·3,780·8,385·16,812·31,227·54,555·90,705; join 0; chain 0 — own closure operator agrees at every cap; C(344,2) = 58,996 named |
| 3 N₈ (1719, 1720) | YES (reconstructed) | **REPRODUCED + RE-DERIVED** | N₈ compact form = product over (ℤ/2)³; withdrawn U⁴ coefficient = 2p²+16q (true 6p²−8q); withdrawn U² ≠ true; 0 at u = (3,5,7) |
| 4 shape-potential audit, both states (1718, 1722, 1723) | YES (reconstructed) | **REPRODUCED** | failing state A False 13/13; the single code difference is L58 `Vs=V0_shape(w,m)/R` → `Vs=V0_shape(w,m)` |
| 5 mass-uniformity (§36.4) | derivation by reading | held as text | `closure_test` and `P8` take no mass argument (read in audit.py) |
| 6 stratification (1713, 1714) | NO | **NOT HELD — never data** | theorem-assembly; record-carried |
| 7 five points, threshold (§36.3) | YES | **REPRODUCED + RE-DERIVED** | Euler quintic one positive root at all 13 (own numpy roots; Descartes one sign change); Routh μ = (9−√69)/18 = 0.0385208965 = solution of 27μ(1−μ) = 1 (Decimal) — CITED in the record, COMPUTED here |
| 8 eight attribution questions (1721) | NO | **NOT HELD** as file | text, not instrument; record-carried |
| 9 five figures | YES (re-renders) | **REPRODUCED** | figs.log byte-identical; all five PNGs re-rendered in chat 130 byte-identical to the manifested md5s (out of band; `run-tb/`) |
| 10 paper and record | PDF on Drive; .md not held | not fetched this chat | `151Yg3WgY-aqx24jrlHdvtPK8a-rNgMKL`, 340,837 B per README |

**1713–1724 against the delivery.** All twelve present, none carries a WARNING; 1716's six tokens and figures, 1717's
78/78 and 6, 2, 1, 1718's *failed 13/13* and *hyper-radius*, 1719's *2p² + 16q* / *6p² − 8q* / *withdrawn*, 1720's
(ℤ/2)³ and 1770, 1721's *Eight … seven closed* all read and reproduce where computable. **1725 ABSENT** (17b-01's
neighbour). **1756 ABSENT** — cited for `tb_audit.py` by REQUEST-THREEBODY item 1, by the delivery's README, and by
main **L9903** (§36.2); no Register line contains `tb_audit` (substring, whole member). 1717 is the entry that holds
the 78/78. *Segment B site.* Main L9903 also prints *Eight attribution questions, eight closed* against 1721's *seven
closed to named owners* — *Segment B site.*

### intake1-01 — finding about the reconstruction: 13 labels, 12 orderings
The delivered `cases` dict carries 13 labels, but *x<y, y>z* at (1,3,2) and *x<z, z<y* at (1,3,2.5) realise one
weak ordering (x<z<y); the ordering **z<x<y is never tested** (the thirteen weak orderings of three labelled masses
are the ordered Bell number a(3) = 13). Run through the delivered six checks as an appended 14th case, z<x<y passes
all six (|S| = 1). Every check is True at all 13 labels, so *78 of 78* stands as printed; the label count is the
record's own. Under the standing rule the finding is about the reconstruction: **flagged to the three-body project;
not a book deviation without the original instrument.** Docket 38 / 37 (reconstruction-versus-record ledger).

### intake1-02 — incidental: `caps_table.log`'s sixth column is wall-clock
Not bankable as delivered; r2-tb1 diffs the five data columns and re-derives them. Delivery form note.

### intake1-03 — incidental: five PNGs of the delivery's names in the project knowledge
`/mnt/project/fig1_shape_sphere.png … fig5_constraint_graphs.png` at 59,166 / 40,235 / 38,598 / 61,552 / 27,036 B,
md5 `9a5f1e03…` / `37a3db2b…` / `77c24dff…` / `7760d5ee…` / `e23104b3…` — different bytes from the re-renders;
fig5 viewed side by side is the same figure. Whether these are the session's "lost" originals is **INFERRED**
(names match; provenance unverified). Recorded so the three-body project can compare; nothing depends on it.

## C. R3 draft Register entries — NOT seated (RUL-128 item 4: each delivered object enters only through a guarded build)

Numbers 1795–1798 are drafts; 1793–1794 are R3-CLASS-WL.md's. Bodies follow R-FORM; wording is M's to rule on at R3.

**1795 — `ground.py` DELIVERED AND REPRODUCED: THE OBSERVED TABLE OF 1306 RUNS AGAIN, 108 OF 108, NINETEEN OPENINGS,
TWO TRANSPOSITIONS FROM MADELUNG.** *Delivered 2026-09-01 as produced (md5 236975ac…); its printed log reproduced
byte-for-byte; the 108 configurations equal this book's independent NIST reconstruction cell for cell; the two
departures from Madelung are the adjacent transpositions 5d↔4f and 6d↔5f.* Registers 1306; 1307. (a reproduction.)

**1796 — THE THREE-BODY AUDIT RUNS AGAIN FROM A RECONSTRUCTION: 78 OF 78, CAP 8 = 344 · 8,385 · 0, CHAIN 0, THE
FIRST-RUN FAILURE 13 OF 13 AT ONE LINE.** *No file of the session survives; the instruments were recovered from its
transcript and re-run; every printed figure of 1716–1718 reproduces, and the closure figures reproduce under an
independent operator at every cap 3–12. The thirteen labelled mass cases realise twelve orderings; the thirteenth
(z<x<y) passes all six checks when added.* Registers 1716; 1717; 1718; 1722. (a reproduction, of a reconstruction.)

**1797 — N₈ AND THE WITHDRAWN POLYNOMIAL, BOTH RUN: THE NORM IS THE PRODUCT OVER (ℤ/2)³, THE WITHDRAWN U⁴ TERM IS
2p² + 16q AGAINST 6p² − 8q.** *Symbolic identity, zero remainder; the U² term likewise differs; N₈ vanishes at
u = (3, 5, 7), V = 15.* Registers 1719; 1720. (a reproduction.)

**1798 — ROUTH'S THRESHOLD, CITED IN THE RECORD, NOW COMPUTED: μ₁ = (9 − √69)/18 = 0.0385208965, THE ROOT OF
27μ(1 − μ) = 1.** *Decimal, forty digits; agrees with the printed 0.0385209 at seven places, half-up.* Registers
1717. Prior art: Routh 1875. (a computation.)

**Not drafted (nothing held):** 1713/1714 (never data), 1721's ledger, the six Löwdin figures, the Löwdin chain
1701–1712 — all remain record-carried with the label docket 38 assigns.

## Instrument faults (self-caught, rewritten before banking)

- r2-lw1 fault 1: a §1 note contradicted itself about README.md's manifest row; rewritten to state that MANIFEST.tsv
  lists 3 of 4 files and not itself. Fault 2: the Pd line's label said *5s occupancy* while printing 4d and 5s.
- r2-tb1 fault 1: the §5 DATA-row filter swept the README's second table (Runs) into the status table (17 rows for
  10); rewritten to read the first table only. Fault 2: §3b asserted 13 orderings from 13 labels without naming the
  duplicate; rewritten to name it and to run the missing ordering (intake1-01).
