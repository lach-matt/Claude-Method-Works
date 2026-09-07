# FINDING R4-12 — Chapter 34's two remaining record items, 34re-05 and 34re-06, close as conventions the chapter's own instrument uses. One prose site remains. NOT REPAIRED.

Measured 6 September 2026. With these, every one of the seven 34re findings the record raised
against Chapter 34 has been settled in this pass, and the tally is below.

## 34re-06 — "seventeen of nineteen openings agree" is right, and the book names its own convention

**§34.1:** *"Seventeen of nineteen openings agree; two do not"*, *"89 % accurate"*, and *"Madelung
inverts 5d/4f and 6d/5f."*

**The record (34re-06):** position-wise the observed and Madelung sequences agree at 15 of 19
(78.9 %); as inverted adjacent pairs the count is 2, i.e. 17 undisplaced (89.5 %); *"the sentence
names neither convention."*

**Measured, both conventions:**

| convention | agree | of | |
|---|---|---|---|
| position-wise | 15 | 19 | 78.9 % |
| adjacent inversions | **17** | 19 | **89.5 %** |

The two inversions are **5d/4f and 6d/5f** — exactly the pair the sentence names. **So the book does
name its convention, by naming its exceptions:** two adjacent inversions, seventeen undisplaced,
89 %. Under M's test the object — *Madelung inverts two adjacent pairs, 5d/4f and 6d/5f* — is true.
**Not a false claim.** A word naming the count as one of inversions would remove the ambiguity, and
that is the prose pass's.

## 34re-05 — five sites, and four of them have already closed

The record: five sites restate as live what register 1350's WARNING qualifies and 1460 demotes.
Checked against the current build:

| site | now | |
|---|---|---|
| §34.8 *"No parameter is fitted in the form; the placement of `a` along the walk is a fit (register 1445)"* | **already qualified** | closed |
| *"Exceptionless on 106 elements"* | **no longer in Chapter 34** | closed |
| §34.6 *"resets eighteen times"* | **verified true** — `walkresets.py`, 18 recalibrations | closed |
| §34.5 *"Nineteen distinct surds across the whole table"* | **verified true under the instrument that produced it** — see below | closed |
| **§34.4 *"No parameter is fitted"*** | **unqualified**, twelve lines above the qualified form | **open, prose** |

**The nineteen is a convention the record scored under a different generator.** `walk.py`, which
produced §34.6's eighteen, generates candidates to n ≤ 8 and gives **exactly 19 distinct finite
corridor endpoints**. The seated `r2-ch16y.py` defaults to n ≤ 7 and gives 17 — and its own sweep
prints both: *"n≤7: 17 | n≤8: 19"*, under either ℓ cap. **The book's figure is the instrument's
figure.** One word is loose: three of the nineteen are 0, ½ and 1, which are not surds. The count is
exact; the noun is not.

**What remains of 34re-05 is one site**, §34.4's *"No parameter is fitted"* without the *"in the
form"* that §34.8 already carries. It is the withdrawn-law class the record holds for R3, and the
repair is the three words §34.8 has.

## The tally for Chapter 34, all seven record items

| item | what it was | how it closed |
|---|---|---|
| 34re-01 | two crossings wrong at the fifth decimal | **confirmed** by a third route, `precision.py` |
| 34re-02 | the 8 / 6 / 4 split | **book right**, finding R4-01 withdrawn |
| 34re-03 | never resets mid-subshell | **false**, derivation found in the corpus (R4-06, R4-08) |
| 34re-04 | 1.028 unreproducible; 0.25 % not 0.19 % | **withdrawn**, both halves (R4-11) |
| 34re-05 | five sites restate what 1350 qualifies | **four closed, one prose site open** |
| 34re-06 | seventeen of nineteen, convention unnamed | **book right**, convention named by its exceptions |
| 34re-07 | 5f opens with p = 1 | **confirmed**; §34.9 repaired at 4f by ruling |

Four of the seven found the book right or better than the record said. **Nothing is repaired here.**
