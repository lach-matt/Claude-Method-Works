# READ-reg4.md — the Register, unit 4: the mature record opens, entries 165–198 (L731–L850)

Fourth unit of the Register's source-order read under M's compendia-scope ruling, and the first with
no natural block boundary — 1,464 bare entries run 165 to 1792 unbroken. The unit is cut at 120 lines
(the chat-81 mean is 116) on an entry boundary: 165 through 198, thirty headings. Instrument
`r2-reg4a.py`, golden `r2-reg4a.out` (4,828 B · `c808a9d6` · 74 lines). All instrument checks OK;
**one deviation**.

## The precedent that governs this unit, read before anything was scored

The register has already ruled on stale numerals inside entries, at the Appendix F renumbering:

> **THREE REFERENCES IN THIS REGISTER ARE LEFT AS THEY STAND — entries 371, 372 and 1780 — BECAUSE
> ENTRIES ARE APPEND-ONLY.** *A superseded numeral inside an entry is the record of what was written,
> not a defect in it; this entry is the correction, and a reader meeting F.3.3 at 371, 372 or 1780 is
> meeting the section now numbered F.3.1.*

Applied here, that protocol **acquits** most of what a naive pass would flag. It is not unconditional:
the same entry rests it on having measured *"zero occurrences of either numeral in any volume"* — the
renumber *"collides with nothing"*. So the scored question is not *is the numeral stale* but **does
the stale numeral now resolve to a different live object**, which is the case the precedent does not
reach.

## A — deviation

**reg4-01 — entry 193 names two live figures that are not the ones it describes.** The entry reads
*"Figure 23.2 appeared before Figure 23.1, because the arity plot sits in §30.3.2 and the step law in
§30.3.4."* MEASURED in the main volume:

| | line | sits under | is |
|---|---:|---|---|
| Figure 30.1 | 8444 | `### 30.3.2 The law` | **the arity plot** — *"the fraction of each arity's constraint language that is 2-SAT expressible"* |
| Figure 30.2 | 8493 | `### 30.3.4 The step law` | **the step law** — *"the growth step against dimension"* |
| Figure 23.1 | 6191 | `### 23.1 The ratio` | the exact cost against its asymptote |
| Figure 23.2 | 6328 | Chapter 23, *The cost surface* | the cost surface |

The figures entry 193 describes are **30.1 and 30.2**, and it calls them 23.1 and 23.2. Both of those
numerals are **live** and denote different objects. Two consequences: a reader following the entry
lands on the cost-surface figures, which have nothing to do with arity or step laws; and the entry's
order claim is **false of them** — 23.1 (L6191) precedes 23.2 (L6328), measured. Both pairs are in
correct reading order in the volume today.

This is the class W-105 recorded from the other side (*"L1264 keeps Figures 23.1/23.2 for what are
now 30.1/30.2"*) and it is **narrowed here**: not a stale numeral, which the register's own protocol
permits and preserves, but a stale numeral that collides with a live one. **R3: a new entry that
cites 193 and names the current numbers — the F.3.3 model — never an edit to 193.** Docket 9(a) / 23.

Recorded as this instrument's fault 1: entry 193 was first scored as a live defect because 23.1 and
23.2 *are* in reading order. They are, and the entry is not about them. The finding was withdrawn and
re-taken in its correct, narrower form.

## B — verified

- **Every section pointer resolves to its heading and carries its claim** — §3.1 *Why three of the
  audits were needed*, §24.4 *He II — the δ = 0 edge itself*, §30.3.2 *The law*, §30.3.4 *The step
  law*, §31.3.4 *E(X) on a specifiable slice, and 540 predictions*, §32.2 *Self-reference*, §32.6
  *The falsification tests, run*. Seven of seven, each to the claim and not merely the heading.
- **The 540 predictions of entries 197 and 198 are the section's own headline figure**, printed in
  §31.3.4's title.
- **The sequence gaps are accounted for, two of them by the record itself.** 176 and 177 are narrated
  inside entry 175's body rather than given headings — recorded as this instrument's fault 2, having
  first read four unexplained absences where there are three.
- **The absent-number class reconciles with the register's own measurement.** L6574 states *"Across
  165 to 1781 the span holds 1,617 places and 1,485 are occupied, so 132 are absent"*; MEASURED here
  over 1–1792, **132**.
- **The unit's form is consistent.** Sixteen of thirty headlines open on a quoted claim and then
  refute or qualify it in the same headline — the self-audit form.

## C — incidental

- **190, 196 and 199 are absent and cited nowhere** — outside docket 9(c)'s absent-**and-cited** class,
  and unexplained in this unit. Recorded, not scored. L6574 already withdraws three claims the
  register made about its own numbering and names eleven numbers in no group; these three are not
  among them.
- **Entry 175's *"Λ's box has 10^2080 subsets"* is not reproducible from the page, and the negative
  has a witness.** 2ⁿ = 10²⁰⁸⁰ needs n ≈ 6,910. Tested against every size the work prints — genesis
  box 630 (10¹⁹⁰), 450, 210, Λ₈ 976 (10²⁹⁴), Λ₉ 1,654, Λ₁₀ 2,535, Λ₁₁ 13,585 (10⁴⁰⁸⁹), Λ₁₂, Λ₁₃ —
  and none is near it. The entry names no box. A budget, not a negative. Docket 10.
- The measurements of entries 166–187 (a quarter of pairs, 44 of 130, 20.5%, 90.4% → 9%, 39%/49.5%)
  are records of past computations whose instruments are not in the bundle. Not re-derivable, not
  scored, and the standing rule gives the record the benefit.

## Census

**No census row engages this unit** (measured over reg L731–L850). `CENSUS-CLOSURES-reg4.tsv` is
header-only.
