# `tools/arith.py` — the arithmetic audit run as a program

`DOCKET.md` §2 requires, at every section read:

> Check the arithmetic of every ratio and percentage; never round with `round()` — `Decimal.quantize`,
> convention named.

This is that check run as a **class** over whole members instead of one section at a time. It
extracts the arithmetic the volumes state *about themselves*, recomputes each claim in `Decimal`,
and reports a verdict per claim.

```sh
python3 tools/arith.py --selftest                       # against the corpus's own numbers
python3 tools/arith.py --list-rosters
python3 tools/arith.py --roster volumes
python3 tools/arith.py --roster reader-facing --only DISAGREE
python3 tools/arith.py --member The_Method_1_6___The_Register-2.md --class CHOOSE
python3 tools/arith.py --roster volumes --all-verdicts --json
```

Stdlib only, Python 3.9+. No dependencies, so an audit can run it from any tree.

## Why it exists

The main volume declares an `ARITHMETIC` defect class, and records at L1407 that it has **caught
nothing**:

> ARITHMETIC and REPRODUCTION have caught nothing in this book — no register entry names any of them.

L1413 gives the class its illustration — *"a product stated beside its own printed factors and
wrong: 33 × 5 = 166"*. The class was declared and never landed, because sweeping it by hand means
re-deriving several hundred ratios in source order and nobody does that twice.

Swept mechanically, the class lands. See **The findings** below.

## Six verdicts, and only two of them are findings

| verdict | meaning | a finding? |
| --- | --- | --- |
| `AGREE` | recomputes to the stated value at the stated precision, under every named convention | no |
| `WITHIN-INPUT-PRECISION` | the point estimate differs, but by less than the operands' own printed precision | no |
| `DISAGREE` | recomputes to a different value under every named convention | **yes** |
| `ROUNDING-SENSITIVE` | agrees under one convention and fails under another — an exact tie, and the text owes its convention a name | **yes** |
| `NOT-BOUND` | a fraction and a percentage share a line but the text does not bind them. An assertion, not a result | no |
| `UNCHECKABLE` | zero denominator, `k > n`, a value that does not parse | no |

## Three things it refuses to do

**1. It never rounds with `round()`.** Every comparison is `Decimal.quantize` at the precision *the
text itself states* — a value printed to one decimal place is not a claim about the second — under a
named convention, and the convention is printed above every report. The default pair is `HALF_UP,
HALF_EVEN`; `--conventions` takes any of `HALF_UP, HALF_EVEN, HALF_DOWN, DOWN, UP`.

**2. It never reports `DISAGREE` for a co-located pair.** A fraction and a percentage on one line
are not a claim unless the text *binds* them. This is the regex-artefact discipline of the C7/C9
precedents, and it is most of the work: of 280 claims in the reader-facing members, **212 are
`NOT-BOUND`** — three quarters. The Mathematical Compendium's

> `floor(delta) ≤ B for 311 of 311 measured channels. As an equality it is right 57%`

is the shape of the trap: `311/311` is 100%, the `57%` belongs to a different quantity, and a
tool that paired them would report a defect that is not there. Binders are ranked — `=` and
parentheses assert the identity, a comma merely apposes it — and `--strict-binding` drops the comma.

**3. It never picks the rounding convention for you.** A claim that agrees under one convention and
fails under another sits on an exact tie; `ROUNDING-SENSITIVE` reports that rather than resolving
it. `1 of 8 = 13%` is 13 under `HALF_UP` and 12 under `HALF_EVEN`, and which one the text meant is
not the tool's to decide.

## The five claim classes

| class | shape | example |
| --- | --- | --- |
| `FRACTION-PCT` | a fraction bound to a percentage | `146 of 163 = 92%`, `84/99 = 85%`, `303 of 311, 97%` |
| `EQUATION` | a chain of arithmetic expressions joined by `=` | `33·5 + 33·10 + 23·15 + 8·17 = 165 + 330 + 345 + 136 = 976` |
| `CHOOSE` | a binomial pair count | `C(120,2) = 7,140`, `C(9,2)·4 = 144` |
| `COMPLEMENT` | a stated failure count against a stated pass fraction | `318 of 407 … failed for 89` |
| `PCT-OF` | a percentage of a base, with the result stated | `20% of 264 is 53` |

`--class` restricts the sweep to one of them.

### Chains, because that is how the volumes write arithmetic

`EQUATION` reads `a = b = c` as the assertion that **all** members are equal. Pairing only the first
`=` with what follows reads the second expression as a scalar and manufactures defects. MC §10.3's

> `|Λ| = Σ_q |A(q)| × |B(q)| = 33·5 + 33·10 + 23·15 + 8·17 = 165 + 330 + 345 + 136 = 976`

is one claim with three computed members, all 976, and it is `AGREE`. Read pairwise it looks like
two defects (`… = 165` and `330 + 345 + 136 = 976`) and is neither.

### Wraps, because the corpus's own convention says to read them joined

`DOCKET.md` §2: *a roster that wraps is read on the whitespace-normalised join.* A line ending in a
dangling arithmetic operator is joined to its continuation, which is why the main volume's

```
    248,305 with h¹¹ ≥ 140 · … · and 248,305 +
    248,305 − 495,515 = 1,095, as reported.
```

is one claim — correct inclusion–exclusion — and not a false one. **Nothing else is joined.**
Joining two adjacent table rows would fabricate arithmetic the text never states, so only a
dangling operator licenses it.

### `WITHIN-INPUT-PRECISION`, because a count is exact and a decimal is not

A literal without a decimal point is a count and exact. A decimal printed to *d* places stands for
anything within half an ulp of itself, and the tool propagates those intervals through the products
and sums. MC's

> `1.0838 × 1.0854 × 1.1212 × 1.0522 × 1.0125 × 1.0022 = 1.4081 = joint/product to four decimals`

multiplies out to 1.408218 — but the factors are printed to four decimals, so what they stand for
lies in `[1.407818, 1.408618]`, which covers the stated 1.4081. Faulting it would fault the text for
arithmetic it never claimed. The same shape with integer operands — `33 × 5 = 166` — is **not**
softened, because counts carry no interval.

## The findings

Over `--roster reader-facing` (the six volumes and the two papers), 280 claims:

```
AGREE 64   WITHIN-INPUT-PRECISION 2   DISAGREE 2   NOT-BOUND 212
```

*Re-measured again at BUILD117, where registers 1849–1852 brought **four further claims under the tool and
all four are `NOT-BOUND`** — `AGREE`, `DISAGREE` and `WITHIN-INPUT-PRECISION` are each exactly as they were.
The four correcting entries introduced no arithmetic claim the tool can bind, let alone one it disputes.*

*Re-measured 2026-09-07 at BUILD116. This block read 235 / 57 / 1 / 175 when written and went stale
across the R4 leg; `tools/docfigures.py` caught it. **`DISAGREE` did not move.** Thirty-four further
claims came under the tool as entries were seated, and every one of them either agrees, is not bound,
or is inside its operands' printed precision — **no new arithmetic finding has appeared, and the two
below are still the whole of it.** The second `WITHIN-INPUT-PRECISION` is not a second claim either:
it is the same six-factor product, quoted into the Register at `reg:6764` from the Mathematical
Compendium line the section below already discusses.*

**`mc:2930` — `146 of 163 = 92%`. It is 89.57%.** The site reads

> penetration (|d|≥0.1) falls 146 of 163 = 92%; polarisation (|d|<0.01) RISES 52 of 52 = 100%;
> combined 94% against 66% as a single claim (R 985–987)

`52 of 52 = 100%` on the same line is right. `146 of 163` is 89.6%, not 92%, bound by the text's own
`=`. The string `146 of 163` occurs exactly once in the store and no nearby entry states 89.6%, so
the figure is unrecorded — the first landing of the `ARITHMETIC` class L1407 says has caught
nothing. **Recorded, not repaired:** the chat-67 full hold governs, and the disposition of the
`combined 94%` clause beside it is a reader's question for R3.

**`main:1413` — `33 × 5 = 166`** is the `ARITHMETIC` class's own illustration, quoted deliberately
wrong. The verdict is correct and the site is not a defect. See Known gaps.

## `--selftest`

42 fixtures: the verdict machinery against synthetic lines, a `NEGATIVE` list of constructions that
must yield **no** claim, a `WRAPPED` list read across a line break, and a `CORPUS` list of live sites
in `method/members/`. The corpus fixtures are addressed **by the text of the site, not by line
number**, so a rebuild cannot move a fixture out from under the self-test.

Three of them are guards earned by getting it wrong first:

| fixture | what it protects against |
| --- | --- |
| `ⅅ=0  failed, found, repaired — 39 claims, now 60 of 63` | a table row whose zero and whose word *failed* both **precede** the fraction. The failure count must follow what it complements. |
| `the degree sum 12·10 + 20·6 + 30·4 = 360 = 2E` | closing the chain on the `2` of `2E`. A digit glued to a letter is a variable; the register says *"the arithmetic is sound throughout"* and is right. |
| `heavy elements fail at 23% against light at 8%` | reading a failure **rate** as a failure **count**. `129 − 114 = 15`, and 23 is a percentage. |

Current state: `SELFTEST OK`.

## Known gaps

- **It cannot tell a defect asserted from a defect quoted.** `main:1413`'s `33 × 5 = 166` is an
  illustration of wrongness and reads `DISAGREE`, correctly and uselessly. Nothing in the text marks
  a quotation as one, so this is left to the reader rather than guessed at.
- **A fraction and its percentage on different lines are not paired.** Only a dangling arithmetic
  operator licenses a join, so `… 146 of 163\n= 92%` would read `NOT-BOUND`. No such site is known
  in the current members.
- **It checks each site against itself, never against another site.** The same fraction given two
  different percentages in two volumes is two `AGREE`s if each is internally right. A cross-site
  concordance is a different instrument.
- **`NOT-BOUND` is not triaged.** 175 of them is a reading list, not a result; `--all-verdicts`
  prints them.
- **Percentages of percentages, and ranges** (`interval 82-93%`) are not claim classes. They state a
  spread rather than an identity, and nothing is recomputable from the line alone.
