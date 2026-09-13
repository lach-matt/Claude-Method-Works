# `hlaw.py` — the hierarchy law as an instrument

The paper states and proves the law. `law.py` argues it, `induce.py` measured it over random
worlds, `lawfigures.py` pins every figure the paper prints. **None of those is a thing you can point
at an index.** `hlaw.py` is.

```
python3 hlaw.py --example energy-conditions   run the law against a named index
python3 hlaw.py --index FILE                  ... or one you supply
python3 hlaw.py --list                        the built-in indexes
python3 hlaw.py --sweep 400                   try to break the law over N random indexes
python3 hlaw.py --selftest                    fixtures are the paper's own numbers
```

Stdlib only. **Exit 0 if the law holds on the index, exit 1 if it does not** — and a non-zero exit
is a refutation of a proved clause, not a bug report. The docstring's closing section says what to
check before believing one.

## What it reports

Six blocks, and the separations between them are the design:

| block | what it is |
|---|---|
| the five closures | `\|L(X)\|` and the residual `E = \|L(X)\| − \|X\|` for each |
| sizes | a size order, **labelled as not a nesting order** |
| **the law** | the seven lawful containments, each checked, each carrying the clause that proves it |
| this index only | the other thirteen, marked `INDEX-ONLY` when they happen to hold |
| the partial order | pairwise, with `INCOMPARABLE` and `EQUAL` printed as themselves |
| clause readout | A, B, C, D and G evaluated on the index; F as a relabelling test |

## What it refuses to do

Each refusal is a mistake the paper made and withdrew, turned into a property of the program.

**It never prints a total ranking of the five.** Clause E is a refutation — the order in which the
five nest is a property of the index, and fourteen distinct rankings appear across four hundred. A
program that printed "the hierarchy" as a list would be reporting an artefact of whichever index it
was handed.

**It never reports a size comparison as a containment.** On the energy-condition index `geometry` has
29 cells and `information` has 156, and the two are set-theoretically **incomparable** — neither
contains the other. An earlier draft of the paper read a size reversal between two indexes as a
nesting swap and had to withdraw it. Sizes and containments print in separate blocks and are never
merged.

**It never promotes a containment to a law because it held on your index.** Seven are lawful and
proved; the other thirteen vary. Six of the thirteen are refuted as universal claims by an explicit
minimal witness the paper prints, and the report says which.

**It does not repair a refutation.** No retry under another ambient, no downgrading a clause.

## What it imports rather than reimplements

The operators are `decomposable.py`'s (`stair`, `gen`, `joinclose`) and `lawfigures.py`'s (`stat`,
`geom`). The energy-condition index's cells come from `necindex.py`, where that index is seated.
**Nothing here recomputes a closure another instrument already defines** — if the operators are
wrong they are wrong in one place, and every instrument moves together.

## The selftest, and why its fixtures are the strongest available

`--selftest` does not check the program against itself. Its fixtures are the paper's printed
numbers, so a pass ties the instrument to the published table rather than to its own arithmetic:

- `LAWFUL` is asserted **equal to Clause H's measured seven** — the law is quoted here, not derived,
  and the selftest is what keeps the quotation honest.
- Seven of twenty, thirteen remaining, six witnessed — the arithmetic of §6d.
- Each named witness index really shows the non-containment it is named for.
- On the energy-condition index: `|geometry| = 29`, `|information| = 156`, the two **incomparable**,
  `order = algebra = 192`, `statistics` admitting exactly the 17 seated cells at `E = 0`, and a box
  of 288. Every one of those figures is in the paper.
- A 200-index sweep finds no violation.

## The sweep is corroboration, not proof

`--sweep N` draws N random indexes and checks all seven lawful containments on each. It prints, on a
clean run, that this **corroborates the law and does not prove it** — the proofs are in the paper and
a sweep cannot add to them. What a sweep can do is fail, and a failure would be worth more than any
number of passes.

## Input format

One tuple per line, integers separated by commas or whitespace; `#` comments and blank lines
ignored; every tuple the same arity; `d ≥ 2`. A JSON list-of-lists also works. Ragged input, empty
input and `d = 1` are rejected with a message rather than a traceback — `d = 1` because the law says
nothing there (N3 in the paper: `order` returns SILENT and both sides would be `X`).

Because the inputs are integer tuples, every factor is a chain, which is exactly the hypothesis
Clause B needs. The paper's N2 — the staircase under-generating off non-chain factors — is
unreachable from anything this program can read, and the docstring says so rather than leaving it as
a trap.
