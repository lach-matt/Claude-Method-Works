# DOCKET — open questions of this research tree, and the rulings on them

The corpus keeps its open questions in `DEFERRED.md` under numbered dockets and
rules on them in the Register. This tree is not the corpus and writes nothing
into it, so it keeps its own. Same discipline: a docket states the question and
what would settle it; a ruling states what was decided, on what measurement, and
what it costs.

A ruling here binds this tree's instruments and nothing else. It is not a
Register entry and must never be cited as one.

---

## DOCKET 1 — HOW IS A BLOCK ASSIGNED?  **RULED**

*Raised 2026-09-14 by M: "Drop the block convention question into a docket and
rule on it."*

### The question

`tools/populate.py`'s `block_of` assigns an element's block from the
**differentiating electron of its observed ground configuration** — the subshell
that distinguishes Z from Z−1. It asserts that convention in its docstring
("the Löwdin construction's own object") and **cites no register**, where
`period_of` and `group_of` are pinned to §6's ninety cells and checked in the
selftest.

It matters because the corpus's rarest refusal turns on it. K1 —
*{information} refuses, everything else admits*; every pair of requirements
jointly satisfiable and the full combination not — occurs at `(period 4,
group 11, s-block)` of `periodic layout 3-D`, and that is the warp
obstruction's own kind.

Three conventions are available:

| | rule | reaches | source |
|---|---|---|---|
| **A** | differentiating electron of the **observed** configuration | Z ≤ 108 | `LW1-ground.py` |
| **B** | the **drawn** 18-column layout, group → block | all 118 | the classroom table |
| **C** | differentiating electron of the **Madelung** configuration | all 120 | the filling law |

### The measurement that settles it

Three coherent charts, each using ONE convention throughout, against the seated
index which uses two:

| chart | cells | closes in | master cell | R(X) | K1 |
|---|---|---|---|---|---|
| **C** pure Madelung — Janet `(n+ℓ, ℓ, k)`, Z ≤ 120 | **120** | **all five, E = 0** | (5,1,1,1,1) | {0,7} | **no** |
| **A** pure observed — Janet `(n+ℓ, ℓ, k)`, Z ≤ 108 | 98 | nothing | (0,0,0,1,1) | {0,2,6,7} | **no** |
| **B** pure drawn, He as s | 80 | nothing | (0,0,0,1,1) | — | **no** |
| **HYBRID, AS SEATED** — drawn period + group, **observed** block | 80 | nothing | (0,0,0,1,1) | {0,1,3,4,5,6,7} | **YES** |

**`periodic layout 3-D` as seated is a hybrid**: two of its three coordinates
come from convention B and the third from convention A. **K1 exists only in the
hybrid.** No coherent single convention produces it.

And the hybrid carries **seven of the eight refusal kinds** where the pure charts
carry two and four. *Mixing conventions manufactures refusal structure.* That is
the general form of the finding and it is worth more than the particular cell.

### THE RULING

**The three are not three conventions for one coordinate. They are three
different coordinates answering three different questions, and each has a home.**

1. **C — the Madelung differentiating electron — is the LAYOUT coordinate.**
   Janet's left-step table is defined by it. It reaches all **120 cells and all
   118 known elements with no data boundary**, because the filling law needs no
   observation. Built here it closes in **all five languages at E = 0**, which
   **independently confirms §6.1's `left-step (Janet) | 120 | E = 0` by a
   different operator family** — §6.1 measured the envelope operator ℛ on a
   two-coordinate layout; this is the five-language hierarchy closure on a
   three-coordinate chart. Two routes, same verdict. *Use C to lay out.*

2. **A — the observed differentiating electron — is a MEASUREMENT PER ELEMENT,
   not a layout coordinate.** It is where the aufbau anomalies live: six
   displaced elements (Mn, Zn, Tc, Ag, Cd, Hg), all drawn-d differentiating into
   s, none in the reverse direction. It stops at Z = 108 because measurement
   does — register 1446's four edges, *102 observed, 108 listed, 118
   synthesised, 120 by Janet*. *Use A to measure. Never to lay out.*

3. **B — the drawn group → block rule — is a PRESENTATION.** §6.1 already prices
   it: the 18-column drawing costs **E = 36** where Janet costs **0**, and the
   thirty-six "belong to the drawing that hangs in classrooms". It also needs a
   helium ruling before it has a channel at all — He as s gives K0, He as p gives
   K2. *Use B to draw. Not to index.*

**And therefore:**

- **(a) The seated `Janet (n+ℓ, ℓ)` at 19 cells is a COARSENING of Janet's
  table, not Janet's table.** It charts 80 elements onto 16 cells. **REPLACE it
  with the complete 120-cell chart.** Measured cost: the master index keeps nine
  indexes, eight cells, closes in nothing, and demands exactly `(1,1,0,2,1)` —
  **unchanged**. Janet alone moves, from `(5,1,1,0,2)` to `(5,1,1,1,1)`, **a cell
  that was vacant.** A correction that disturbs no finding and fills a hole.

- **(b) DO NOT ALSO SEAT IT.** Adding the complete table as a tenth index beside
  the coarsening takes statistics to E = 2 and raises a second demand at
  `(5,1,1,1,2)`. That is the over-representation fault again, committed freshly.
  Replace, do not add.

- **(c) `periodic layout 3-D` STAYS SEATED, AND IS DECLARED A HYBRID.** It is not
  dropped. A finding is recorded, never repaired, and the hybrid is a real and
  interesting object: it is precisely *where the classroom drawing and the atoms
  disagree*. What was wrong was not building it but not labelling it.

- **(d) ITS K1 MAY NEVER BE QUOTED AS A FACT ABOUT THE ELEMENTS WITHOUT THE
  CONVENTION STATED.** Every use of the `(4, 11, 0)` refusal — in `duality.py`,
  in `refusal.py`, in `research/README.md`, in the corridor definition — carries
  the qualifier or it is a false finding. The cell rests on exactly two elements,
  copper and silver (157 of 160 single-cell perturbations leave it in place), and
  the causal chain is palladium's empty valence 5s → silver alone in the s-block
  at group 11 → statistics admits `(4,11,0)` → K1.

### What the ruling costs, stated plainly

It costs the periodic end of the K1 thread its standing as a fact about matter.
The thread from the bounds index to the periodic layout is now a thread from a
real refusal to a **seam between two conventions**. What survives untouched is
the **warp cell's own K1**, which `statrow.py` measures from the device and not
from any periodic chart, and the **bounds index's K1**, which is that index's own
demanded cells. Those two are unaffected by this docket.

### What is NOT ruled

- **Whether `periodic layout 2-D` should be dropped.** Measured: dropping it, or
  Janet, or `periodic layout 3-D`, or any combination, leaves the master index
  closing in **nothing** in all eight variants. The over-representation is real
  and is **not** why the cells are vacant. Deferred to docket 2.
- **Which of the 120 Janet cells the two unoccupied ones are**, and whether an
  unoccupied layout cell should be seated at all. Note the precedent: the corpus
  refused to supply a ninth Janet block because *"a block with no elements in it
  is an INVENTED CELL, and the proposal was that fault dressed as a test"*. Two
  empty cells inside an occupied block is a different case from an empty block,
  and it has not been argued either way here.
- **Whether Z = 109…118 should carry blocks under convention A.** They cannot:
  `LW1-ground.py` stops at 108 and `docs/POPULATE.md` records that as deliberate
  — *"LW1-ground.py stops there because measurement does."* Under convention C
  the question does not arise, which is part of why C is the layout coordinate.

---

## DOCKET 2 — SHOULD THE PERIODIC TABLE BE SEATED MORE THAN ONCE?  **OPEN**

The master index seats the periodic table three times: `periodic layout 2-D`
`(period, group)`, `periodic layout 3-D` `(period, group, block)`, and
`Janet (n+ℓ, ℓ)`. On the 80 elements all three reach, the first two are
**injective and therefore in bijection**, and `block` is a **function of
`(period, group)`** there — so the 3-D chart is the 2-D chart plus a coordinate
carrying zero information about which element is which. Janet is a strict
coarsening, 80 onto 16.

Yet they occupy three different master cells in three different channels, and
**dropping any of them, alone or in combination, leaves the master index closing
in nothing.** So the duplication is real and the vacancy is not caused by it.

**What would settle it: a criterion for a legitimate chart.** This tree has never
stated one, and docket 3 is why that is now urgent.

---

## DOCKET 3 — WHAT IS A LEGITIMATE CHART?  **OPEN, AND IT IS THE PRIOR QUESTION**

A master cell is a property of the **chart**, not of the object. Appending a
coordinate that is a *function of the existing ones* — zero information — moves
**five of the nine** seated master cells. A **monotone** such coordinate leaves
every channel intact; a **non-monotone** one does not, and the periodic table's
block is the witness in this tree's own membership.

**And the standing demand `(1,1,0,2,1)` is satisfiable by re-charting what is
already seated: 20 of 550 re-chartings land on it**, including the bounds index
minus its gravity coordinate and the energy-condition family under five different
single-coordinate drops.

So the demand is exactly as strong as a criterion for a legitimate chart, and no
such criterion exists here. Until one does, **a demanded cell is a demand for a
chart with those properties, not for an object** — which is weaker than the
demand has been stated at anywhere in this tree.

Nothing is repaired on the strength of this. It is recorded, and it gates
docket 2.
