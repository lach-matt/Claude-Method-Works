# `tools/pointers.py` — the pointer audit run as a program

`DOCKET.md` §2 requires, of every section read:

> exact-token heading resolver, never prefix, resolved to the **body** occurrence … resolve every
> pointer to the claim and not the heading, under both resolvers, and locate where the claim does
> live

and `CLAUDE.md` §6 adds that the pointer regex is case-sensitive and that lowercase `register NNN`
and `A.N` are **grepped by hand**. This is that resolution run as a class over the whole store, in
both cases, with the hand-grep folded in.

```sh
python3 tools/pointers.py --selftest
python3 tools/pointers.py --roster with-companion --findings
python3 tools/pointers.py --roster volumes --class SECTION --only UNRESOLVED
python3 tools/pointers.py --extent                     # the Register's gaps, and which are cited
python3 tools/pointers.py --roster with-companion --findings --json
```

Stdlib only, Python 3.9+. It answers four census classes mechanically:

| class | census |
| --- | --- |
| `SECTION` | `C1-SECTION-POINTER-UNRESOLVED` |
| `THEOREM` | `C2-THEOREM-POINTER-UNPRINTED` |
| `FIGURE` | `C3-FIGURE-POINTER-UNPLACED` |
| `REGISTER`, `REGISTER-RANGE` | `C5-REGISTER-POINTER-UNRESOLVED` |

`CHAPTER`, `APPENDIX` and `APPSEC` are swept too and carry no census class.

## Why it exists

`r2-tools.py pointers A B` — a seated member, and the recorded convention — takes **one line range
of the main volume** and resolves it against the main volume's headings. That is the right shape for
a section read and the wrong shape for a class sweep: it cannot run corpus-wide, it resolves from
one member only, and by design it stops at the heading, leaving *"resolve to the claim and not the
heading"* and the lowercase `register NNN` grep to the hand.

This runs all six volumes plus the companion as **sources and as targets at once**, so a pointer
that misses its own volume is told where it does land.

## The one thing it refuses to do

**It never reports `UNRESOLVED` for a pointer that resolves somewhere else in the roster.** Four of
the census's own C1 rows are that case:

| census row | pointer | where it actually lives |
| --- | --- | --- |
| 10, 11 | reg L5605, L5609 `§5.7` | `Transitions.md` L567 |
| 24 | mc L2474 `§6.5` | `Transitions.md` L656 |
| 25 | mc L2484 `§5.1` | `Transitions.md` L469 |
| 26 | ioi L141 `§5.7` | `Transitions.md` L567 |

And the text says so each time — *"§5.7 of the companion"*, *"the split alphabet of T §6.5"*. Under
`--roster volumes` all four read `UNRESOLVED`, which is what the census recorded; under
`--roster with-companion` all four read `RESOLVED` and name the member. Both are in the self-test,
because the roster is the thing that changes the answer and it should be visible that it does.

## Eight verdicts, and four of them are findings

| verdict | meaning | a finding? |
| --- | --- | --- |
| `RESOLVED-HERE` | resolves in the citing member itself | no |
| `RESOLVED` | resolves in exactly one other member, named | no |
| `AMBIGUOUS` | resolves in more than one member and the pointer does not say which | no |
| `PARTIAL` | a range citation some of whose numbers carry no entry | **yes** |
| `PREFIX-ONLY` | no exact heading, but sub-section headings begin with it | **yes** |
| `UNRESOLVED` | nowhere in the roster | **yes** |
| `KIND-MISMATCH` | a register number written as a section pointer | **yes** |
| `OUT-OF-EXTENT` | a register number past the Register's extent | **yes** |

`AMBIGUOUS` is not a finding: each volume numbers its own sections, so `§3.1` existing in three of
them is the notation, not a defect.

`PREFIX-ONLY` is reported as its own verdict rather than folded into `UNRESOLVED` because the
exact-token resolver is the one in force — so the pointer does not resolve — while **whether an
unheaded parent section is a defect is R3's ruling, not the tool's**. `DEFERRED.md` L156 has exactly
this open: *"R3 decides once whether Chapter 4's protocol rows take headings."*

## Three conventions it had to learn from the store

**A range is one claim, not one per number.** The Spectra Compendium L1061 reads *"Registers
1524–1677 record the capture of these bodies one at a time"*. Expanding that into 154 pointers and
reporting the 19 absentees turns one finding about a range into nineteen rows. `REGISTER-RANGE` is a
single site whose verdict states what the sweep covered: *135 of the 154 numbers in the range carry
an entry.*

**The volume heads its sections twice.** Main L162 is the contents — seven appendix headings in a
row with no prose between them — and L9939 is Appendix A itself. `DOCKET.md` requires the **body**
occurrence, so a heading followed by another heading is a contents entry and a heading followed by
prose is the body. Chapter 4 is the same: L117 contents, L1436 body. Both are asserted in the
self-test by line number, because that rule is what those two line numbers are for.

**Appendix A states most of its proofs as a table.** A.3, A.8 and A.9 take `### A.n` headings; A.1,
A.2, A.4–A.7, A.14, A.16 and A.17 are rows of an indented table —

```
  A.2       X closed ⟺ ℛ(X) = X                    §14.1, in full
```

— which is precisely what `CLAUDE.md` §6 means by the pointer regex *ignoring Appendix A item
numbers* and owing a hand grep. A heading-only resolver reports exactly those nine as unresolved and
is wrong nine times. A labelled proof row is a placement.

A fourth was inherited rather than learned: **`§12` is chapter 12**, whose heading is `## 12. …`.
`r2-tools.py` carries that fallback and this copies it. Without it, 59 whole-chapter pointers read
`PREFIX-ONLY` against their own sub-sections — `PREFIX-ONLY` fell from 61 to 3 when it was put back.

## Provenance

The section, chapter, appendix and appendix-section site patterns are copied from the seated member
`r2-tools.py` (chat 70). The register patterns and `_reg_nums`' guards — the **165 floor** and the
200-wide range cap — are copied from `register_cites.py`, whose `(?i)` is the reason the hand-grep
for lowercase `register NNN` is no longer owed. Both are bundle members and neither is lifted to
`r2lib`, so per `CLAUDE.md` §5 the functions travel with a provenance comment until they are.

## What it reports

Over `--roster with-companion`, 2,152 pointer tokens:

```
RESOLVED-HERE 438  RESOLVED 1605  AMBIGUOUS 65  PARTIAL 19
PREFIX-ONLY 3  UNRESOLVED 21  KIND-MISMATCH 1
44 findings  (APPSEC 2, FIGURE 2, REGISTER 4, REGISTER-RANGE 19, SECTION 8, THEOREM 9)
```

*A class this audit deliberately does not score, named at BUILD122: a citation can RESOLVE and still be
wrong, because `pointers.py` asks whether an address exists and not what stands at it. Registers 1861, 1871
and 1874 are three measured instances — A.15's "Register 230", §23.10.2's "recorded at 96–98", and §12.11.1
citing itself for a nominal value it never states. All three score RESOLVED and all three are correct to.
Where a citation names WHAT its target establishes, that description is checkable against the target's own
words, so a successor could score the claim as well as the address. Not built; named so it is a decision.*

*Two further instances at BUILD124, and they are the cheapest kind to check because the wrong target is a
NUMBER. §34.6 and register 1804 both cite **register 1580** for the corridor census — "73 fully bounded ...
the maximum set of PAIRWISE DISJOINT corridors is THREE" and "1580's certified three". **That census is
register 1517's.** 1580 states no census at all: it prints the held-out walk's scores, floor 87, midpoint 83,
ceiling 82 and STAY 92. Both citations score `RESOLVED` because 1580 exists, and both send a reader to an
entry that does not carry what it was cited for. Register 1877 records them; `method/proofs/corridors.py`
locates the strings so the attribution is measured rather than argued. **This is the first instance of the
class in which the citing text and the target could have been compared MECHANICALLY** — the census's own
figures do not occur in 1580 — which is what a successor to `pointers.py` would look for first.*

*Re-measured again at BUILD117, where registers 1849–1852 added **six pointer tokens, all six RESOLVED** —
findings stayed at 44, every class of them unmoved, and `PARTIAL` stayed at 19. Four entries that correct
statements about the volumes added no pointer defect of any kind, which is what a correction should do.*

*Re-measured 2026-09-07 at BUILD116. This block read 1,932 / 1387 / 17 / 42 when written and went
stale across the R4 leg as entries were seated; `tools/docfigures.py` caught it. **Read what moved and
what did not.** The tokens rose by 154 and `RESOLVED` by 152 — that is the leg's new entries citing
things that resolve, which is the pointer audit reporting health, not defect. **Five of the six finding
classes did not move at all**: APPSEC 2, FIGURE 2, REGISTER 4, SECTION 8, THEOREM 9, each exactly as
before. Only `REGISTER-RANGE` moved, 17 → 19, so **no new KIND of pointer defect has appeared** — two
further range citations were seated, each partial for the same reason the other seventeen are, and
neither is in registers 1842–1848 (no `PARTIAL` cites a Register line above 6684, and those entries
begin at 6812).*

**Nothing here is new, and that is the point.** Every finding it reports is either a row of
`DEFECT-CENSUS.tsv` or an item already recorded:

- `main:7584 Figure 15.3` — census row 1, the only one of 33 cited figures not among the 32 placed.
- `Theorem 7.1, 9.1, 10.1, 11.1, 11.2, 12.1, 4.4` — census rows 2, 4–6, 9, 12–13, 19–21, 23.
- `reg:3113 §784` — census row 7, `KIND-MISMATCH`: a register number written as a section pointer.
- `reg 1000, 1002, 1725` — census rows 3, 8, 15–17.
- `§4.6, §4.7` and `reg 287` — **not** census rows, but `WORKING-REGISTER.md` L4687 already has
  *"259 and 287-class pointers resolve only to groups; §4.4/§4.6/§4.7 resolve to unheaded lines"*,
  and `DEFERRED.md` L156 dockets it for R3.

What is new is the **scope**: §4.6 is cited at 17 sites across three volumes, not the one the docket
names, and the 17 `PARTIAL` ranges were never enumerated. G0v applies — *a docket's target is a
hypothesis until read and measured* — and this measures them.

## `--extent`

The Register's extent is stated as 1 to 1889; 1,756 of those numbers carry a `###` entry and 133 do
not. **An uncited absence is not a pointer failure**, so `--extent` lists only the absences
something cites:

```
Register extent 1 to 1848; 1715 numbers carry a ### entry, 133 do not.
  reg 287   cited at main:1503
  reg 1000  cited at reg:4667
  reg 1002  cited at reg:6529
  reg 1725  cited at reg:10
4 cited absences of 133 absences in the extent.
```

## `--selftest`

53 fixtures. The theorem declaration/citation discriminator and `register_cites.py`'s floor and
range cap are unit-tested; the contents/body rule is asserted at the two line numbers it exists to
disambiguate; and every corpus fixture is addressed **by member and token, never by line number**,
so a rebuild cannot move one out from under the test. The `§5.7` family is asserted twice, once
under each roster.

Current state: `SELFTEST OK`.

## Known gaps

- **`C2b-THEOREM-17.1-CITED-AS-§17.1` is not mechanical.** `§17.1` *does* exist (main L4794), so
  nothing distinguishes the pointer from a correct one; the finding is that the author meant Theorem
  17.1. Census row 22 stays a reader's finding.
- **It cannot read which volume a pointer means.** 65 `AMBIGUOUS` tokens resolve in several members;
  the text usually says (*"M §17.2"*, *"T §6.5"*, *"of the companion"*) and that prefix is not
  parsed. Reading it would turn most of the 65 into `RESOLVED` and is the obvious next increment.
- **A pointer resolving to a heading is not a pointer resolving to the claim.** `DOCKET.md` asks for
  the claim; this gets to the heading and no further, which is the same limit `r2-tools.py` has.
  `RESOLVED` means *a target of that name exists*, not *the target says what the citation says it
  says*.
- **A prefix hit in another member says nothing about the cited one.** `§0` at reg L6311 cites *"the
  Spectra Compendium at its §0"*; among the volumes it is `UNRESOLVED`, which is census row 14, and
  adding the companion makes it `PREFIX-ONLY` because `§0.1`–`§0.4` exist — in `Transitions.md`, the
  wrong member. The verdict names where it hit, so the coincidence is visible, but the tool does not
  know it is one. Both rosters are in the self-test for exactly this reason.
- **Tables have no class.** `Table N.N` pointers are collected by no pattern here, because the store
  has no single declaration form for a table to resolve against.
- **`reg 287` is under-described.** `WORKING-REGISTER.md` L4687 says the 287-class pointers *resolve
  only to groups*; this reports the absence of a `### 287` heading and does not look inside grouped
  entries for the material. The grouped heading `### 227, 253, 254, 305` at reg L1327 is headlined
  *§4.6 — A TEST THAT COULD NOT …*, so the two findings are one finding.
