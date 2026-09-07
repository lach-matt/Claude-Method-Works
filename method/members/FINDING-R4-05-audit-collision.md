# FINDING R4-05 — §2.21's "twenty-two distinct cells, no collision" is false, and the R2 read found it first. This confirms it and adds the reason it matters. NOT REPAIRED.

Re-measured 6 September 2026 in the Chapter 2 subject-matter read. **The finding is not new.** Chat
69's R2 reading of Chapter 3 already recorded it in the Working Register:

> *"the §2.21 table has 21 distinct cells, not 22 — CENSUS (row 22) duplicates SCOPE (row 10) — so
> L1140's 'no collision' is false"*

It is recorded and held, exactly as the chat-67 full hold requires. What follows is an independent
reproduction of it and one argument the record does not make.

## What is claimed

**§2.21, immediately under its own table:** *"**Twenty-two audits over twenty-two distinct cells, no
collision.**"*

§2.21 prints that table for a stated reason: *"§3.8 computes E(audits) and the hierarchy's dimension
from these four values per audit… **The table is the input; a reader can rerun either.**"* This is
that rerun, by a seated instrument rather than by hand.

## What the table gives

Parsed from the seated main member by its own column header rather than by a line number, and encoded
with §2.21's own stated orders, *labels are addressable* reading as the second exactly as §2.21
directs:

| | |
|---|---|
| audits | **22** |
| distinct cells | **21** |
| collisions | **1** |
| box | 144 |
| \|ℛ(X)\| | 37 |
| **E(audits)** | **16** |

**The collision is audit 10 SCOPE and audit 22 CENSUS.** Both rows read *source · itself · wrong ·
claims individually true*, character for character. No encoding choice separates them.

## The new part: the claim contradicts the computation it is the input for

The audits index grew, and the book prints each step. All three reproduce:

| | cells | collisions | E |
|---|---|---|---|
| 20 audits, before INPUT — §3.8's growth table prints **E = 17** | 20 | 0 | **17** |
| 21 audits, INPUT added — §3.7.1 prints *"adding it takes E(audits) from 17 to 16"* | 21 | 0 | **16** |
| 22 audits, CENSUS added — the Index of Indices prints **21 cells, E = 16** | **21** | **1** | **16** |

The last row holds **because** CENSUS shares SCOPE's cell. Had CENSUS taken a cell of its own, E would
have fallen to 15 and the book's printed 16 would be wrong. **So the book's own E(audits) = 16
requires the collision that §2.21's sentence denies** — the two are not merely inconsistent, one is
the negation of what the other rests on.

**And it shows what happened.** At twenty-one audits the sentence was true: twenty-one audits,
twenty-one distinct cells, no collision, which the same measurement confirms. CENSUS was added as the
twenty-second. **The number in the sentence was updated and the property was not rechecked** — §2.14,
*compute, then write*, which §2.14 itself calls *"the protocol most often violated in the production
of this book"*, occurring inside the chapter that states it.

## Why it is subject matter under M's test

Strip the prose and the object is *"the twenty-two audit rows are pairwise distinct"* — a property of
a printed table, decidable by inspection, and false. A reader who trusts the sentence and recomputes
E gets 16 while expecting 15.

## What is owed

The repair is a sentence and it is M's: **twenty-two audits over twenty-one distinct cells, one
collision — SCOPE and CENSUS, indistinguishable in these four coordinates.** Whether the collision is
worth a remark is M's call too. There is a precedent for treating it as a result rather than an
embarrassment: §2.24 records the same thing among the protocols — *"§2.8 and §2.24 occupy the same
cell in every coordinate"* — as a finding, and register 514 carries it.

**Nothing is repaired here.**

## Also re-measured, and §3.7 verifies in every part

**§3.7's dimension certificate is sound.** Twenty-two precedences as stated; both printed linear
extensions of each component are genuine extensions; each pair intersects in exactly its component's
order, which is what certifies **dim = 2**; and both counts §3.7 prints reproduce exactly — **792**
linear extensions for the nine-element component, **4,140** for the ten.

**Its two rhetorical counts reproduce as well, and the record supplies the decomposition for one of
them.** *"Finding them took eight and a half million"* is C(4140, 2) = 8,567,730. *"Verifying these
four lists takes 362 comparisons"* is the R2 read's **4·81 + 2·19 = 324 + 38 = 362** — four lists
against eighty-one pairs, plus each component's nineteen relations. That decomposition was recorded
in chat 69 and is adopted here rather than re-derived; my own first reading gave 162 and was wrong,
which is the standing rule working as intended: **where a reconstruction disagrees with the record,
the finding is about the reconstruction.**

**One item in §3.7 remains open and it is the record's, not mine.** The precedences leave CENSUS in no
relation at all, so the comparability order has **four** components — ten, nine, a pair, and CENSUS
alone — against §3.7's *"falls into three components"*. Recorded in chat 69, held, not repaired. The
dimension is unaffected: a singleton has dimension at most one.

---

## The same object again in Chapter 18, printed at two values twelve lines apart. Candidate E-061, settled.

Measured while the instrument was open, and it closes the first clause of candidate **E-061**.

**Chapter 18 prints E for the audits index twice, in one section, for the same four coordinates:**

| main | the row | E |
|---|---|---|
| L5031 | *the audits, four coordinates · **16** · the certificate: drop DEPTH, the fourth coordinate · after: **0*** | **16** |
| L5068 | *the audits, four coordinates · **17** · fourteen cells with no audit in them* | **17** |

**16 is right.** It is the value at twenty-two audits, it is what §3.7.1's chain arrives at, and it
is what the Index of Indices prints. **17 was the value at twenty audits**, before INPUT was added —
§3.8's growth table prints it as that, correctly.

**And the 17 row's gloss belongs to the 16.** *"Fourteen cells with no audit in them"* is not a
count of seventeen anything. It is the count of the **dominated** cells among the sixteen: measured,
of the sixteen admitted and absent, **fourteen are dominated** — some occupied cell is at least as
large on every axis — **and two are on the frontier**, where the index stops. So L5068 carries a
stale E beside a current sub-count of a different number.

**The Index of Indices' entry on those two cells reproduces exactly, cell for cell.** It states the
frontier pair as *outside · dishonest*, and measured they are:

- **outside · other places · dishonest · also mutually consistent**
- **outside · a computation · dishonest · also mutually consistent**

which is the entry's claim and, as it says, the same pair §14.5.6 finds ℛ₄ refusing, reached by two
computations sharing no code. **That is true and proven.**

**What is owed:** L5068's *17* is stale and its gloss belongs to the other row. M rules; nothing is
repaired here.
