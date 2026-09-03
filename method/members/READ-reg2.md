# READ-reg2.md — the Register, unit 2: the genesis block, entries 1–94 (L75–L450)

Second unit of the Register's source-order read under M's compendia-scope ruling. 376 lines, 94
entries, numbered 1 to 94 with no gap.

**How a historical block is scored, fixed before anything was scored.** The front matter calls 1–94
*"the genesis block — the founding chat and the first paper, prepended as the record of where the
work began"*. It is history, and several of its figures are superseded inside the block itself
(4 → 11/12 is the model case). So a genesis figure that disagrees with today's lattice is **not**
automatically a defect — preserving it is what the block is for. What is scored is (i) arithmetic
that must hold on its own terms, (ii) a genesis claim contradicting **another genesis claim** with no
correcting entry between them, and (iii) a pointer that does not resolve. Superseded-and-marked is
recorded as verified. Without this convention the block reads as ninety-four deviations and says
nothing.

**The lattice was rebuilt, not recited.** This is the three-axis genesis lattice (n, ℓ, k) of entry
2, not Λ₈, so `tower-2` is not used: the box of entry 57 is built directly from the constraints the
entries themselves print, and every count below is derived from it.

Instrument `r2-reg2a.py`, golden `r2-reg2a.out` (6,885 B · `5fe03282` · 105 lines). All instrument
checks OK; **two deviations, and they are one finding at two sites.**

## A — deviations

**reg2-01 — the block prints an *unbounded* lattice's figures inside a *bounded* lattice, at two
sites, and nothing reconciles them.** Entry 57 fixes the box: n ≤ 7, ℓ ≤ 4, k ≤ 18 — 630 cells,
reduced to 450 by ℓ ≤ n−1 and to **210** admissible by k ≤ 2(2ℓ+1). All three reproduce exactly. But:

- **Entry 43** prints *"Counting admissible cells at fixed n: Σ(ℓ=0 to n−1) 2(2ℓ+1) = 2n², so the
  capacities 2, 8, 18, 32, 50, 72, 98 are the slice volumes."* MEASURED slice volumes on entry 57's
  own box: **2, 8, 18, 32, 50, 50, 50**. The formula is right and the *sentence* is not: 2n² needs ℓ
  to reach n−1, so n = 6 needs an h-subshell and n = 7 an i-subshell, and entry 2 caps ℓ at g. The
  printed series sums to **280**; entry 57 prints 210.
- **Entry 50** prints *"The volume of each Madelung slice is 2, 2, 8, 8, 18, 18, 32, 32, 50, 50, 72,
  72 — equal consecutive pairs"*, and rests the periodicity argument on the pairing. MEASURED on the
  same box: **2, 2, 8, 8, 18, 18, 32, 30, 42, 32, 18** — eleven groups, not twelve, agreeing to
  n+ℓ = 7 and diverging from n+ℓ = 8, where n ≤ 7 truncates the series.

The two sites are the same fault: the physical capacities (2n², the Madelung pairing) are stated as
**counts of this lattice** when they are counts of its unbounded idealisation. MEASURED that no entry
in the block corrects either — `register 43` and `register 50` are cited nowhere in 1–94, and entry
57 is the only entry that prints the ℓ ≤ 4 cap. Entry 47's "truncates" is about ℓ ≤ n−1 at *small* n,
a different ceiling. **R3: either bound the sentences to the idealisation, or state the cap where the
capacities are claimed.** Docket 12 / 19 / 35.

## B — verified

Everything else in the block reproduces, which for 94 historical entries is the result:

- **The lattice chain** 630 → 450 → 210, each step from the printed constraint.
- **The census and its own correction.** Entry 4's 118 + 14 + 180 + 240 + 78 = 630; entry 11's
  180 + 240 + 92 + 118 = 630; entry 12's 78 + 14 = 92. MEASURED independently: **180 void** (ℓ ≥ n),
  **240 reactive** (k over capacity), and 210 − 118 = **92 reserved**. The genesis draft's 78, the
  ghost 14, and the recount to 92 are all exactly as printed, with both states kept.
- **Entry 39** — 210 cells give C(210,2) = **21,945** pairs, and exhaustive checking returns **0 join
  failures and 0 meet failures**. Λ is a bounded lattice, as claimed.
- **Entry 46** — the parity balance: **105 even-rank and 105 odd-rank** cells.
- **Entry 47** — the full 28-term rank sequence reproduces term for term, sums to 210, is not
  palindromic, and its maximum is carried by **rank 11** as stated (the value 15 occurs at ranks 11
  and 12; the entry names the first).
- **Entry 73** — log₂(118) = **6.883** to three decimals.
- **Entry 74** — C(10,4) = **210**, and the first twelve level sizes are 1, 2, 3, 4, 6, 8, 11, 13,
  14, 15, 15, 14 against the Gaussian binomial's 1, 1, 2, 3, 5, 6, 9, 10, 13, 14, 16, 16 — differing
  from the second term, which is the entry's own point. The coincidence is correctly refused.
- **Every pointer resolves.** 19 distinct register pointers, all inside 1–94, none absent, none
  reaching out of the block. No § pointer and no chapter pointer anywhere in 376 lines — the genesis
  block is closed under its own citation.

## Census

Five rows engaged (1234, 1235, 1236, 1237, 1238), all C9-OVERGENERALISATION-WORD, all closed **not a
defect** in `CENSUS-CLOSURES-reg2.tsv`. Two were not closed on judgement but on measurement: **1235**
("raising n never violates ℓ ≤ n−1") is proved exhaustively — 0 violations over every admissible cell
raised to every larger n; **1237**'s "19 saturated, 6 empty" rests on a column count that reproduces
at **25**.

## C — incidental

- **Not scored, and named as budgets:** entry 60's 450 → 330 → 210 chain on the (n, ℓ, m, s) build
  cannot be rebuilt from the page — the m and s ranges are not printed. Entry 71's three maximal
  cells and five covering addresses, and the order-ideal claims of 1236/1237, need the 118 occupied
  cells, which the block does not enumerate. All eight named addresses are admissible on this
  lattice, which is as far as the page allows.
- Entry 23's regression, entries 26/38/52/77/93's prior-art citations, and the crystallographic
  apparatus are external sources; not re-derivable here and not scored.
