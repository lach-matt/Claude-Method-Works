# PHASE 1 LEDGER — the mathematics leg, worked item by item

M, 7 September 2026: *"everything you just asked about finishing has already been ruled. it all must be
done."* Phase 1 of `PLAN-R4-PUBLICATION.md` is *"every computable claim still unproven or contradicted,
re-derived by a standard-library instrument and settled by entry before any prose moves"*, and
`PLAN-R4-ANNEX.tsv` holds **41 open rows** in it. `RULINGS-R4c` §3 fixes the order: **subject matter, then
prose, then pointers**, so this leg stands in front of the prose pass.

**One instrument per class, banked, each with a `--selftest` whose fixtures are the corpus's own recorded
numbers.** Nothing is repaired in a volume by this ledger; what each instrument settles is what the
Register entry for its class will record.

---

## Worked

### J-20 · §32.1.1's self-index — `bookindex2.py`, selftest 10 of 10

§32.1.1 prints its index as *"Recomputed at this build (2026-08-24, `bookindex.py`), over the thirty-five
chapters and six appendices the book now has"*. **The book has thirty-six chapters and seven appendices** —
measured from its own headings, 1 to 36 with no gap, and A to G.

**And the instrument is as stale as the sentence.** `bookindex.py` hard-codes `APP='ABCDEF'`, filters
references with `1<=r<=35`, and sets `n=41  # 35 chapters + 6 appendices`. **Three constants, not a
reading** — so no re-run of it can ever count Chapter 36 or Appendix G. The answer is a successor
instrument, which is what the store did twice before (`census` → `census2`, `r2-reg1a` → `r2-reg1a3`) and
never an edit to the seated original, which G0c forbids.

| | printed | at the seated bounds | at the true extent |
|---|---|---|---|
| claims | 1,021 | 1,014 | **1,021** |
| cells | 400 | 402 | **410** |
| box | 1,681 | 1,681 | **1,849** |
| E(book) | 1,265 | 1,302 | **1,407** |

**The claim count is current and the three box-dependent figures are not**, which is a sharper result than
"the sentence is stale": what has moved is the box, because the extent moved.

### D-60 · F-191 · H-23 · §10.2's range in cell count — `voidrange.py`, selftest 9 of 9

Two lines apart, of one measurement: §10.2 prints *"a **seventeenfold** range in cell count"* and Figure
10.1's caption prints *"a **hundredfold** range in cell count"*, with an appendix row at *"2.4 points over
a 100×"*. **Every cell-count ratio the record names is computed, and none is seventeen and none is a
hundred**: the tower Λ₈→Λ₁₃ is 204×, Λ₈→Λ₁₂ 72.6×, Λ₈→Λ₁₁ 13.9×, Λ₈→Λ₁₀ 2.6×, and register 1830's six
sampled settings reach 234,340 cells from 976, which is 240×.

**Register 1830 already recorded why it cannot be decided**: the base-cap pair population is 475,800, *"no
one-parameter cap family from the base sums to 776 million"*, and the figures are *"a measurement at a
population the record does not name"*. **So this is not a choice between a right number and a wrong one.
Both printed ranges are unsupported, and what the volume owes is the cap family**, after which the ratio is
arithmetic. Main L3538's *"2.17-fold spread"* is a different object and is named so it is not swept in.

### D-05 · G-01 · the σ collision — `sigmacollision.py`, selftest 7 of 7

**Rule 4 (§22.2)**: *"take σ = 2R Z_eff² · SE_pred / ν³ from the fit's prediction standard error"* — σ is an
**output**. **§22.5**: *"r = 2Z²R / (ν³σ) ≥ 5 … r falls as ν⁻³"* — σ is an **input**.

**Substitute one into the other and the ν³ cancels exactly**: r = Z²/(Z_eff²·SE_pred), a constant in ν. So
if §22.5's σ were Rule 4's σ, **§22.5's own next sentence would be false** — r would not fall as ν⁻³ and no
channel would ever leave the domain. **The two σ are necessarily different quantities**, and the chapter
corroborates it two lines above Rule 4: *"This book's tightest bracket is 1.398 cm⁻¹; limit uncertainties in
the collection run 0.001 to 0.4 cm⁻¹"* — measured level uncertainties in cm⁻¹, constants of the channel,
which is exactly what makes r fall as ν⁻³. **Which symbol is renamed and where is prose, and prose is M's.**

### F-147 · §34.6's eighteen resets — already settled, and against me

The row reads *"'resets eighteen times' (8+6+4) not reproduced"*. **`FINDING-R4-01` is the withdrawal of
that finding**: the entry's parenthetical *"(four of them also openings)"* makes the three classes disjoint,
8 + 6 + 4 = 18 reproduces exactly on the seated ground configurations, and every figure register 1333 prints
returns. **The book is right and the error was mine.** No instrument is owed.

### D-61 · the 1,585-fold — withdrawn at W-245

Ruling 10, executed as work matter: the interval the printed inputs allow is [1577.81, 1588.07) and 1,585
lies inside it. `method/proofs/precision.py`.
