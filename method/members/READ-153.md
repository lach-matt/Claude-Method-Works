# READ-153.md — the audit-instrument class sweep, and R3's first two executions

Chat 153, a repository session. `tools/arith.py --roster volumes` and `tools/pointers.py --findings`
over the six reader-facing volumes and the companion. Both selftests pass before either is trusted
(42 and 53 fixtures). The refusals are not findings and none is quoted as one: 175 NOT-BOUND in
arith, 65 AMBIGUOUS in pointers.

## A — deviations

**153-01. Mathematical Compendium L2930: the penetration percentage did not follow its own count.
REPAIRED, entry 1795.** The volume printed *penetration (|d|≥0.1) falls 146 of 163 = 92%*. MEASURED:
146/163 = 89.57 %, quantizing to **90 %** (Decimal.quantize, ROUND_HALF_EVEN, convention named;
`round()` is forbidden by the standing method). **Register 1048** states the same claim as *146 of
163, 90% against 92%, interval 84–93%* and in the same line gives 92 % its own object — *Combined as
two claims: 198 of 215 — 92%* (198/215 = 92.09 % -> 92 %, MEASURED).

Two readings of *90% against 92%* are available and **neither is chosen**: (i) 92 % is the claim's
own superseded pre-gain value and the volume was partially updated, the count moving and the
percentage not; (ii) 92 % is the combined two-claim figure and has been transposed one claim
leftward. On either reading 92 % is not the percentage of 146 of 163, and 1048's 90 % governs.
Corrected to 90 % under R3's arithmetic class; one numeral changed, no count touched.

Not previously recorded: `146 of 163`, `89.57` and the site return nothing from WORKING-REGISTER.md,
the READ files or DEFERRED.md. **Provenance:** `buildtrace.py --first` reads 8 of the 119 archived
builds and finds the string in the oldest, BUILD9 — its introduction predates the series and the
archive cannot date it. That is an ABSENT-class refusal, not a finding.

## B — flagged by an instrument and NOT a defect

Recorded so that no later pass repairs them. Each was read at the site.

**153-02. Main volume L1413, `33 × 5 = 166` — the volume's own audit fixture, correct as printed.**
arith.py scores it DISAGREE under every convention. The site is a table of *the input that must make
it fail*: *ARITHMETIC — a product stated beside its own printed factors and wrong: 33 × 5 = 166
against §12.6.1's table, which prints 33, 5 and 165.* The volume is quoting a wrong product as the
constructible failing input for its own ARITHMETIC audit. **Repairing it destroys the example.**
The standing method's *a citation is not a declaration*, and the C7/C9 regex-artefact precedent.

**153-03. The §4.5 / §4.6 / §4.7 class — all eight SECTION findings are resolver artefacts.**
UNRESOLVED at §4.6 (main L1205, 1405, 3559, 4006, 4834, 5011 +1; reg L1329, 1533, 1573, 1713, 1877,
2233 +3; mc L2647), §4.7 (main L1430; reg L1333, 1397) and §4.5 (reg L1349, 1577). MEASURED:
Chapter 4's only heading occurrences are main L117 and L1436, and **the chapter numbers its ten
subsections as list items, not headings** — `4.1 attributed outward before checking inward` through
`4.9 a coordinate collapsed into a count`. The targets exist and say what cites them; §4.6 is *a test
that could not fail*, the class W-189's OBJ-T convention reads §4 for. **The finding is about the
instrument.** pointers.py's resolver gap is recorded, and the instrument is NOT changed here (G0c).

**153-04. The THEOREM class is at least partly cross-addressing, not a pointer.** mc L310 *Proved —
T 1.7 (App. G) / M §17.2 Thm 10.1; Birkhoff 1940* scores UNRESOLVED, but `M Thm 10.1` addresses the
**main volume's** numbering; WORKING-REGISTER L1874 records the convention — *CROSS-ADDRESSED
objects: `T 1.2 / M A.2`, `T 1.7 / M §17.2 Thm 10.1`, …* — and the compendium's own heading at L304
is `### Adjunction never repairs (M Thm 10.1)`. Two of the nine THEOREM findings are classified
(this one artefact; reg L6299 genuine, see C); **the other seven are unclassified and counted
neither way.**

## C — recorded findings the instruments reproduced independently

- reg L3113 `§784` KIND-MISMATCH — a Register number given a § sigil. **26b-08** (W-189).
- reg L6299 `Thm 11.1` UNRESOLVED — cited and printed in none of the six volumes. **26b-09** (W-189).
- `reg 571` absent from its range — **docket item 9 (c)**, 15i-09.

## Counts

- arith, six volumes: 235 claims — AGREE 57, WITHIN-INPUT-PRECISION 1, **DISAGREE 2**, NOT-BOUND 175.
- pointers: 1,932 tokens — RESOLVED-HERE 438, RESOLVED 1387, AMBIGUOUS 65, PARTIAL 17, PREFIX-ONLY 3,
  UNRESOLVED 21, KIND-MISMATCH 1; **42 findings** (APPSEC 2, FIGURE 2, REGISTER 4, REGISTER-RANGE 17,
  SECTION 8, THEOREM 9).
- **Of the 44 raw findings, 2 read as genuine (153-01 new; 26b-09 already recorded) and 9 as
  artefacts; the rest are unclassified pending their own reading. A raw instrument count is not a
  defect count**, and applying these reports unread would have damaged the volumes at 153-02.

## D — the withdrawn-law class

Executed this chat as R3's first item; see W-190 segment A and R3-CLASS-WL.md. `r3-wl.py` reproduced
its banked golden byte-exact before it was run for effect, and the Chapter 34 re-take of chat 143
confirms the class at 34re-05 rather than disturbing it.
