# R4 READINESS — M's question of 6 September: *"is the R3 phase complete for all volumes? are we truly ready to begin the prose work?"*

**Measured, not recited. The answer is no to the second question, and "complete" needs splitting for the first.**
Every figure below is measured in the live pair — **BUILD113 main** (`9877ce8a…`) and **BUILD239 compendia**
(`99fe7ccd…`) — on 6 September 2026, with the command beside it.

---

## 1. "Is R3 complete" is two different questions with two different answers

**R3 THE PASS IS COMPLETE, and that is what `method/CLAUDE.md` §3 asserts.** DEF-152's ten items, the
withdrawn-law and arithmetic classes, reg1-04 with its class, the positional class closed by generator, Q5 in
full at entries 1821–1835, the census made content-keyed, every tool seated as a member. `DEF-153O-PENDING.md`
is its running account, and the gate is green on every live step.

**`docs/R3-REPAIR-PLAN.md` IS NOT, AND ITS OWN STATUS LINE IS STALE.** That document is the plan for the
twenty-five retraction rows — Batch A, 9 rows over 7 findings, volume sites repaired in place; Batch B, 17 rows
over 13 findings, Register entries corrected by a new appended entry. It opens *"This is a proposal. Nothing
here has been done."* **That sentence is now false at at least one item and unmeasured at the rest:**

- **A1 is done.** Its two live sites read *"2,475 cells (the figure §12.11.5 withdraws; register 1819)"* at
  main L914 and L3439 — the pointer form Phase 0 ruling 9 blesses. Repaired by other work, not by this plan.
- **A6 is not done.** *"not a lattice"* still stands at main L3380, and `FINDING-R4-02` records it as
  NOT REPAIRED.

`grep -c '2,475' method/members/The_Method_1_6-2.md` → 3. **The plan needs re-measuring against the live pair
before it can be worked at all**, because it does not know which of its own items have since been overtaken.

---

## 2. The plan's own inventory says the work is 90 % ahead of us

`awk -F'\t' 'NR>1{print $3}' method/PLAN-R4-ANNEX.tsv | sort | uniq -c`

| status | rows |
|---|---|
| **OPEN** | **721** |
| DONE | 66 |
| DUP | 13 |

And by phase, the open rows are:

| phase | open | what it is |
|---|---|---|
| **0 — rulings** | **80** | M's, and Phase 1 and 3 wait on several |
| **1 — the mathematics leg** | **41** | **every computable claim still unproven or contradicted** |
| 2 — the Register leg | 46 | entries owed, then the Register's own defects |
| **3 — the prose leg** | **392** | the phase M is asking about |
| 4 — compendia and Index of Indices | 56 | |
| 5 — closing the census | 10 | runs in parallel |
| 6 — instruments and archive | 61 | |
| 8 — press and proofs | 9 | |
| recorded | 26 | |

**Phase 1 is not a formality and it stands in front of the prose.** `RULINGS-R4c` §3 fixes the order —
**subject matter, then prose, then pointers** — and Phase 1's open rows include the σ collision (Rule 4 against
§22.5), sixty figures printed without their inputs, the truncation-printed-as-equality class, the
main-volume-versus-compendium contradiction class, the false-universal class, the arithmetic-convention class,
and the withdrawn-figure-re-asserted class. **Prose written over an unsettled figure has to be written twice.**

---

## 3. THE HARD BLOCKER, and it is the one item no one but M can clear

**Phase 0 ruling 3 — the nine heading-only sections — is not given, and all nine are still empty.** Measured
by walking every heading in the main volume and the Mathematical Compendium and keeping those with no
non-blank line before the next heading:

| section | line | body |
|---|---|---|
| §2.22 | main L1148 | **none** |
| §14.5.2 … §14.5.7 | main L3803, 3805, 3807, 3809, 3811, 3813 | **none, six consecutive** |
| §28.7.6 | main L7682 | **none** |
| §28.9 | main L7777 | **none** |

(§21.5.4 has a body — main L5802 — and the compendium's letter headings are index structure, not missing
sections.) The plan states it plainly: ***"you author them, or the headings are withdrawn by entry. This is the
one item no one but you can do."*** **A prose pass cannot close over nine empty sections**, and it cannot
withdraw them either, because withdrawal is a ruling.

**Four other Phase 0 rulings are outstanding and each blocks named work:** ruling 4 (entry 1797 — the Register's
extent has a hole no instrument can explain to a reader), ruling 6 (the language roster, dockets
20x-04 / 20x-09, where register 1173, §33.1 and §20.2 print three different rosters), ruling 7 (the triage of
the twenty chat-witnessed retraction rows and the 1,168 prose-only statements), and ruling 5 is taken
**reversibly** on an inference from a draft rather than on anything M approved.

---

## 4. What is owed before any of it: the store does not carry its own governance

**`RULINGS-R4b.md` … `RULINGS-R4f.md`, `SETTLED-R4.tsv` and `FINDING-R4-01` … `FINDING-R4-24` are working
files, not members.** A chat opening by the §0 gate reads `RULINGS-R2.md` and `RULINGS-R4.md` and does not see
them — and rulings 1 through 13 of `RULINGS-R4f`, on which the last four builds were made, are among them. On
the store's own precedent (reg13-01, entry 1617) **a governing document the store does not carry does not
hold.** `method/CLAUDE.md` §3 already calls this *"OWED, AND IT IS THE FIRST THING"*. It still is.

---

## 5. A fault of mine, found by this measurement and recorded here

**`PLAN-R4-ANNEX`'s ruling 5 reserved Register 1836 for the bracket result, and I took that number on
6 September for the §34.4 qualifier entry.** `DRAFT-R3-LEAD-bracket.md` carries `### 1836` and `RULINGS-R4.md`
ruling 5 seats it there; `r4-a1.py` read *"the Register runs 1 to 1835, so the next free number is 1836"* and
did not check for a reserved draft.

**Nothing seated is wrong** — a Register number is assigned at seating, the Register is append-only, and the
bracket entry takes the next free number when Phase 2 opens. The draft now carries a note saying so. **But the
next build must not repeat it: the next free number is not the highest seated plus one when a draft holds a
number.** The Register runs to 1838; 1839 is next, and `DRAFT-R3-LEAD-bracket.md` has first claim on it.

---

## 6. The answer, in two sentences

**R3 the pass is complete; the twenty-five-row retraction repair plan named R3 is not, and does not yet know
its own state.** **We are not ready to begin the prose work:** nine sections have no bodies and only M can
give them, four Phase 0 rulings are outstanding, the mathematics leg has 41 open rows that the order of work
puts in front of prose, and the five ruling documents the last four builds were made under are not in the
store.

**What would make us ready, in the order the plan itself gives:** seat the rulings; give Phase 0's four; work
Phase 1 to zero; re-measure `docs/R3-REPAIR-PLAN.md` against the live pair and work Batch A and Batch B; then
Phase 3 opens. **Rulings 2, 3 and 5 of `RULINGS-R4f` — §34.7 and register 1337 — are Phase 3's first item and
not a separate task**, since their repair is a rewritten passage and prose is M's.
