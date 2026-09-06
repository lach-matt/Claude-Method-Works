# FINDING R4-06 — two universals in Chapter 34. One is false and the record understates it; the other has a false reason and a true conclusion. NOT REPAIRED.

Measured 6 September 2026, candidate **D-21** of `CANDIDATES-R4-subject-matter.tsv`, from the
seated member `LW1-ground.py` (register 1306, the observed NIST ASD 5.12 configurations).
`method/proofs/universals.py` holds the test; its selftest asserts twelve of the corpus's own
recorded numbers, `resets.py`'s *12 of 18* among them.

The record already carries both as findings **34re-03** and **34re-07**, and **both are correct as
recorded**. Neither is new. What is new is the extent of the first and the disposition of the second:
the first is false under three readings rather than one, and the second turns out to be a false
premise under a true conclusion.

---

## 1. "It never resets mid-subshell" — false under every reading, and the consequent is the clearest

**§34.6 (main L9640):** *"`a` is carried between elements and resets eighteen times. Every reset is
a **subshell opening** (8), an **aufbau exception** (6), or the **return from one** (4) — Tc after
Mo, Tb after Gd, Bk after Cm, Hg after Au. **It never resets mid-subshell**, which is why each
subshell fills at constant `a`."*

*Mid-subshell* is not defined in the chapter, so it is tested three ways. **All three refute the
sentence** and they differ only in how many counterexamples they name.

**(a) The record's convention — an entrant equal to the previous step's entrant.** Named with
READ-ch34re and applied to register 1401's fourteen forced resets, it gives **two**: Mo 42 and
Rh 45. **That is finding 34re-03 and it is exactly right.** Reproduced here from the seated member.

**(b) Not at an opening — the entrant was already occupied at the step before.** This gives **six**:
Mo 42, Tc 43, Rh 45, Tb 65, Hg 80, Bk 97. It is the complement of the recovered instrument
`resets.py`'s own reading, *"opens a subshell : 12 of 18"*, which this program reproduces exactly.
The six are the two aufbau exceptions that are not also openings, plus all four returns.

**(c) The consequent's own test, and this is the one that settles it.** *"which is why each subshell
fills at constant `a`"* fails for a subshell if any reset falls strictly between its opening and its
completion. **Four subshells fail, carrying ten resets:**

| subshell | opens | full | resets inside |
|---|---|---|---|
| 4d | Z 39 | Z 46 | Mo 42, Tc 43, Rh 45 |
| 5d | Z 57 | Z 79 | Ce 58, Gd 64, Tb 65 |
| 4f | Z 58 | Z 70 | Gd 64, Tb 65 |
| 5f | Z 91 | Z 102 | Cm 96, Bk 97 |

**This reading needs no convention about the word at all.** It asks the question the sentence itself
poses — does each subshell fill at one value of `a`? — and the answer is that four do not.

**Register 1333's 8 / 6 / 4 partition is untouched and stands.** Finding R4-01 measured it disjoint
and exact, and this rests on it rather than disputing it: the twelve openings of reading (b) are the
eight plus the four exceptions that are also openings, and the six are the two exceptions that are
not, plus the four returns. **One object, two readings, and they agree.**

---

## 2. "At any f opening p = 0" — the premise is false at 5f, and the conclusion still holds

**§34.9 (main L9702):** *"**f is outside the domain and the law says so.** At any f opening
p = n−ℓ−1 = 0, the floor of the node count — no subshell has fewer nodes than none — **so no rival
lies below and L = −∞.**"*

**The premise is arithmetic and it is wrong at 5f.** There are two f openings in the observed order:

| | opens at | p = n − ℓ − 1 |
|---|---|---|
| 4f | Z 58, Ce | **0** |
| 5f | Z 91, Pa | **1** |

5 − 3 − 1 = 1. The record has this as 34re-07 and it is exact.

**But the conclusion survives, and this is the part the record does not carry.** Tested directly —
every candidate admissible under the law's own rule *q < 2(2ℓ+1)*, read at the step before, over the
candidate set the record names — **neither f opening has an admissible rival below its entrant**:

- **At 4f the book's reason is the right one.** p = 0 is the node floor and nothing can be below it.
- **At 5f the reason is different.** p = 1, and every subshell with a lower p — 1s, 2p, 3d and 4f,
  the four with n = ℓ+1 — is **full at thorium** and therefore inadmissible. Nothing lies below 5f
  because everything below it is closed, not because 5f is at the floor.

**So L = −∞ at every f opening is true, and the sentence that justifies it is false.** Under M's
test the false object is *"at any f opening p = n−ℓ−1 = 0"*; the object *"L = −∞ at every f
opening"* is true and proven.

**One dependency, stated because it is the only thing the result rests on that is a convention
rather than a measurement.** The candidate set is ℓ ≤ 3, which the record names with READ-ch34re and
which is the domain the law is stated over. 5g has p = 0, and were g subshells admitted it would lie
below 5f and the conclusion would fail there. The book's law does not admit them.

---

## What is owed, and it is M's

1. **§34.6's sentence.** Both halves are false. The measured statement is available and is not
   weaker: *twelve of the eighteen resets are at a subshell opening; the other six — two aufbau
   exceptions and all four returns — fall inside a subshell already filling, and four subshells
   therefore do not fill at one value of `a`.* That is a description of the walk rather than a
   property of the law, which may be what §34.6 wants to say. The chapter's own next paragraph
   already says the walk is not the object — *"eighteen is the cost of walking Z in order, not the
   cost of the table"* — so the correction sits with an argument the chapter is already making.
2. **§34.9's reason.** The conclusion stands and the reason must change. The measured reason covers
   both cases in one clause: **at every f opening no admissible rival lies below the entrant** — at
   4f because p = 0 is the node floor, at 5f because every subshell of lower p is full.

**Nothing is repaired here**, and under `RULINGS-R4c.md` the prose is not touched until M rules.
