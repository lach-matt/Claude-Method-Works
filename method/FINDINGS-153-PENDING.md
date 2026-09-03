# FINDINGS-153-PENDING.md — the audit-instrument class sweep, staged for the next close

Written in the repository session of 3 September 2026 (chat 153, INFERRED from chat 150 = W-189,
chat 151 = M's store ruling, chat 152 = the compendia scope block staged as `method/RUL-152-PENDING.md`).

**Staged, not seated.** WORKING-REGISTER.md, DEFERRED.md and DOCKET.md are seated append-only
members and grow only through `close.py --append`. Nothing here is written into a member and no
volume is touched. The next close seats this block; the file is deleted once seated.

**No repair was made. The chat-67 hold is in force** — restated at chat 128 ("the chat-67 hold for
every class") and again in the chat-152 block staged today ("What does not change. The chat-67
hold"). RUL-128 item 3 puts R3 at stage (iii); the audit is in stage (ii). Findings below are
recorded, never repaired.

## Gate (MEASURED)

`git rev-parse HEAD` b695e4889740a64dcae95c7b187303527a2b4b25, `git status --porcelain` clean.
`python3 method/verify.py`: 343 members checked, 0 mismatched; BUILD90_main 2 members spliced ->
49065309b0c4fe8e055f693aed295cca OK; BUILD180_compendia 341 members spliced ->
ea5becc40e13debe4faaf6c7e0cde960 OK. VERIFY OK.

Five instrument selftests, all OK: `cypher` (Λ at 976 with E = 0, the degeneracy guards),
`arith` 42 fixtures, `pointers` 53, `buildtrace` 29, `populate` 77.

## What the instruments were run as

`tools/arith.py --roster volumes` and `tools/pointers.py --findings` over the six reader-facing
volumes and the companion, on the BUILD90 / BUILD180 members. The sweep is the arithmetic class and
the pointer class of the docket, which is the route RUL-152 item 2 prescribes for the four
compendia that close by class sweep rather than by a source-order read.

## A — deviations

**153-01 (NEW). Mathematical Compendium L2930: `146 of 163 = 92%` — the percentage does not belong
to the count it is printed against.** MEASURED: 146/163 = 89.57 %, which quantizes to **90 %**
(`Decimal.quantize`, ROUND_HALF_EVEN, convention named per the standing method; `round()` not used).
The Register states the same claim correctly at **L3893**: *its penetration claim gains 29 steps to
**146 of 163**, 90% against 92%, interval 84–93%* — and in the same line gives 92 % its own object,
*Combined as two claims: 198 of 215 — 92%* (198/215 = 92.09 % -> 92 %, MEASURED). The compendium
carries the count from the re-measurement and a percentage that is not that count's.

Two readings of the Register's *90% against 92%* are available and **the choice is not made here**:
(i) 92 % is the superseded pre-gain value of the penetration claim, and the compendium was
partially updated — the count moved, the percentage did not; (ii) 92 % is the combined
two-claim figure at 198 of 215 and has been transposed one claim leftward. Either way the printed
90 % of the Register governs the site and the compendium's 92 % is wrong against its own operands.
Not previously recorded: `146 of 163`, `89.57` and the site itself return nothing from
WORKING-REGISTER.md, the READ files or DEFERRED.md.

**Provenance (buildtrace).** `--first "146 of 163 = 92%"` reads 8 of the 119 archived builds and
finds the string present in the oldest, BUILD9: **its introduction predates the series and the
archive cannot date it.** That is an ABSENT-class refusal, not a finding, and is not quoted as one.

## B — flagged by an instrument and NOT a defect

These are recorded so that no later pass repairs them. Each was read at the site.

**153-02. Main volume L1413, `33 × 5 = 166` — the book's own audit fixture, correct as printed.**
`arith.py` scores it DISAGREE (stated 166, computed 165, under every convention). The site is a
table of *the input that must make it fail*: *ARITHMETIC — a product stated beside its own printed
factors and wrong: 33 × 5 = 166 against §12.6.1's table, which prints 33, 5 and 165.* The volume is
quoting a wrong product as the constructible failing input for its own ARITHMETIC audit. Repairing
it destroys the example. This is the "a citation is not a declaration" case of the standing method
and the C7/C9 regex-artefact precedent.

**153-03. The §4.5 / §4.6 / §4.7 pointer class — all 8 SECTION findings are resolver artefacts.**
`pointers.py` returns UNRESOLVED for §4.6 (main L1205, 1405, 3559, 4006, 4834, 5011 +1; reg L1329,
1533, 1573, 1713, 1877, 2233 +3; mc L2647), §4.7 (main L1430; reg L1333, 1397) and §4.5 (reg L1349,
1577). MEASURED: Chapter 4's only heading occurrences are main L117 and L1436, and **the chapter
numbers its ten subsections as list items, not as headings** — L1441 ff., `4.1 attributed outward
before checking inward` through `4.9 a coordinate collapsed into a count`. The targets exist and
say what cites them: §4.6 is *a test that could not fail*, which is the class W-189's OBJ-T
convention reads §4 for. **The finding is about the instrument, not the books.**

**153-04. The THEOREM class is at least partly cross-addressing, not a pointer.** mc L310
*Proved — T 1.7 (App. G) / M §17.2 Thm 10.1; Birkhoff 1940* scores UNRESOLVED; `M Thm 10.1`
addresses the **main volume's** numbering, and WORKING-REGISTER L1874 records the convention
explicitly — *CROSS-ADDRESSED objects: `T 1.2 / M A.2`, `T 1.7 / M §17.2 Thm 10.1`, …*. The
compendium's own heading at L304 is `### Adjunction never repairs (M Thm 10.1)`. Two of the nine
THEOREM findings are classified here (mc 10.1 artefact; reg L6299 Thm 11.1 genuine, see C);
**the remaining seven are unclassified and are not counted either way.**

## C — the instruments reproduce recorded findings independently

- reg L3113 `§784` KIND-MISMATCH — a Register number given a § sigil. Recorded as **26b-08** (W-189).
- reg L6299 `Thm 11.1` UNRESOLVED — cited and printed in none of the six volumes. Recorded as
  **26b-09** (W-189).
- `reg 571` absent from the range at main L7719's neighbourhood — **docket item 9 (c)**, 15i-09.

## Counts (MEASURED, and the refusals are not findings)

- `arith.py --roster volumes`: 235 claims checked — AGREE 57, WITHIN-INPUT-PRECISION 1,
  **DISAGREE 2**, NOT-BOUND 175. The 175 NOT-BOUND are refusals and are not findings.
- `pointers.py --findings`: 1,932 pointer tokens — RESOLVED-HERE 438, RESOLVED 1387, AMBIGUOUS 65,
  PARTIAL 17, PREFIX-ONLY 3, UNRESOLVED 21, KIND-MISMATCH 1; **42 findings** by class
  (APPSEC 2, FIGURE 2, REGISTER 4, REGISTER-RANGE 17, SECTION 8, THEOREM 9). The 65 AMBIGUOUS are
  refusals and are not findings.
- **Of the 44 raw findings the two instruments report, 2 are read here as genuine deviations
  (one new, 153-01; one already recorded, 26b-09), 9 are read as artefacts (153-02, 153-03,
  153-04's mc row), and the rest are unclassified pending their own reading.** A raw instrument
  count is not a defect count.

## The withdrawn-law class (16z-01) — verified ready, still HELD

`r3-wl.py` was run under the staged gate (`method/bin/stage-gate`, Python 3.12): **it reproduces
its banked golden `r3-wl.out` byte-exact.** It prints its own guard — main 11 substitutions and
Register 2 substitutions + 2 entries, both reverses recovering 4aef772b… and 79aaf239…, the bundle
reverse recovering 49065309…, and `DRY RUN — nothing written under /home/claude; BUILD90 stays live
(class HELD, chat 128)`.

Its release condition under chat 128 item 2 is *in R3 after the Chapter 34 figures are re-taken
under docket 37*. The re-take was run at chat 143 (W-183) and **confirms the class** — 34re-05,
*five sites restate as live what 1350's WARNING qualifies and 1460 demotes*, re-confirming
16z-01 / 16z-02. The figures the approved wording quotes (99 of 106 in sample, 90 held out,
Madelung 96, registers 1437 / 1438 / 1445 / 1460 / 1463) are cited from the record and were not
disturbed by the re-take. **The second half of the condition — that it executes in R3 — is not
met: R3 has not opened.**

## Not done, by design

No repair of any class, including 153-01 and the withdrawn-law class. No build, no Register entry,
no member edited, no golden re-banked. The remaining re-derivations of DEF-143 item 11 (26b-02 and
26b-03 next, then 27a-02, 28a-06, 28b-06) are untouched, as are the Register's full read and the
four compendia class sweeps that RUL-152 scopes.
