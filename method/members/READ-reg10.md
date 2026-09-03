# READ-reg10.md — the Register, unit 10: entries 327–361 and the grouped block (L1211–L1346)

136 lines rather than the usual 120, because the seven grouped fault headings stand between entries
361 and 362 and are read **with** the entry that precedes them. The chat-81 cadence does not split a
section read, and the grouped block is one object: splitting it would leave a heading in one unit and
its mechanism in the next. Instrument `r2-reg10a.py`, golden `r2-reg10a.out`. All instrument checks
OK. **No deviation.**

## B — verified

**The grouped block is organised by the mechanisms §4 names.** Seven headings, 32 numbers, range
203–354, all seven standing after entry 361 — and **five of the seven name a §4.x mechanism
explicitly**:

| heading | mechanism |
|---|---|
| 203, 215, 218, 259, 280, 283, 284, 286, 291 | **§4.2** — wrote into a structure without reading it |
| 207, 209, 213, 219, 220, 221, 231 | **§4.1** — attributed outward before checking inward |
| 227, 253, 254, 305 | **§4.6** — a test that could not fail |
| 288, 308 | **§4.7** — a detector artifact taken for a defect |
| 239, 256 | **§4.3** — claimed completion that had not happened |
| 310, 337, 340, 351, 354 | an instrument narrowed by a literal it carried, *continued* |
| 293, 318, 342 | a check that passed on a defect it was built to catch |

All five §4.x locate in the volume (main L1441–L1448) **as list items, not headings** — the
convention MAIN_AUDIT V1 fixed and the sweep re-measured. The heading resolver is not used on them.

**Entry 334 re-derives exactly.** *"Λ₁₃ enters as a chain of 44 rank values, 12.14 bits lost per
cell, 31 % surviving."* From the seated tower alone: log₂(199,130) = **17.6034**, log₂(44) =
**5.4594**, so the loss is **12.1439 → 12.14** as printed and the survival is **31.01 % → 31 %** as
printed. Nothing outside `tower-2.out` was needed.

**Entry 336 re-derives exactly.** *"…which is 85.9 % of Λ."* 1 − 976/6,912 = **0.8588 → 85.9 %**.
The ambient box is the figure three entries corroborate (248, 255 and genesis 8) and which unit 6
verified through genesis 8's own printed ratio.

**Both remaining section pointers resolve** — §7.1 *The constraints, and where each comes from*,
§28.8 *A dependent choice is indexable…*.

## Census

Three rows engaged, all closed **not a defect** in `CENSUS-CLOSURES-reg10.tsv`. **1241** records that
its own figure moves — *"47 at the time of writing, having been 55 when this section was first
computed"* — which is the register printing both states, not an overgeneralisation; it is also the
site register 375 rests on (26c-02, W-190) and is not re-scored here. **1242**'s *never* states a
property of the construction which the entry then measures. **1243**'s *never* is a bounded fact
about three named Q items and is the very mechanism its §4.3 heading exists to name.

## C — incidental

Five of the ten §4 mechanisms are cited by the grouped headings — 4.1, 4.2, 4.3, 4.6, 4.7. The other
five are not, and two headings name a mechanism carrying no §4.x number at all. Whether the grouping
is meant to exhaust §4 is not stated on the page; recorded, not scored.
