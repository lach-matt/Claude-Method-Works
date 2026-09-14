# DOCKET — open questions of this research tree, and the rulings on them

The corpus keeps its open questions in `DEFERRED.md` under numbered dockets and
rules on them in the Register. This tree is not the corpus and writes nothing
into it, so it keeps its own. Same discipline: a docket states the question and
what would settle it; a ruling states what was decided, on what measurement, and
what it costs.

A ruling here binds this tree's instruments and nothing else. It is not a
Register entry and must never be cited as one.

**A figure inside a ruled docket is AS MEASURED WHEN THAT DOCKET WAS RULED, and
several have moved since — some of them twice.** DOCKET 8 seated a tenth index,
taking "nine indexes, eight cells" to ten and nine; **DOCKET 2 then withdrew
one, and the live figure is nine indexes on eight cells again — a different
nine and a different eight.** The master index closed in `statistics` alone at
E = 0 where earlier dockets record it demanding one cell, and **since DOCKET 2
it closes in `{geometry, statistics}`**: withdrawing an index GAINED it a
language. The counts in DOCKET 5's and DOCKET 6's tables were taken at nine.
They are left as written because a docket is the record of a decision and the
measurement it rested on — changing them would make the ruling unreadable.
**For a current figure ask the instrument, never this file**: `mi.py --selftest`
pins the live index, rebuilt from scratch on admissible coordinates, and
`master.py --selftest` pins the five-coordinate reading it succeeds.

**AND TWO COORDINATES OF THAT FIVE ARE NOW DISQUALIFIED.** DOCKET 3 states the
criterion and measures arity and density against it: both move on 9 of 9. Every
five-coordinate cell quoted anywhere in this file is a statement about a chart,
two of whose coordinates are decoration. The rulings stand; the coordinates they
are written in do not all survive.

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

## DOCKET 4 — IS BEKENSTEIN GRAVITATIONAL?  **RULED**

*Raised 2026-09-14 by the warp-cell audit, which found it while trying to bridge
the two surviving K1 sites.*

### The question

`bounds.py` seats Bekenstein at **G = 1**. Its own rule for that slot reads,
verbatim:

    G  gravity enters       0 no    1 yes (a G or an area appears)

Bekenstein's bound as stated is **S ≤ 2πRE**. It contains no Newton constant and
no area. By the file's own test it is **G = 0**.

The corpus's rarest refusal turns on the answer. With Bekenstein at G = 1 the
bounds index holds **two K1 cells**; at G = 0 it holds **none**.

### The case each way

**For G = 1 (as seated).** The derivation is the generalised second law with a
black-hole gedankenexperiment. The saturating object is a black hole. The file's
own note for the row reads *"saturated by black holes"*.

**For G = 0.** Three arguments, and the third is decisive.

1. **The rule is a syntactic test on the STATEMENT**, and the statement has
   neither a G nor an area. Nothing in the slot's definition mentions derivation
   or provenance.
2. **Bousso says so in print** (hep-th/0402058): the bound *"does not contain
   Newton's constant"* and *"remains nontrivial when gravity is turned off
   completely"*.
3. **SATURATION ALREADY HAS ITS OWN SLOT, AND BEKENSTEIN IS IN IT.** `K = 0` is
   the saturated flag — zero, ANEC, Ford–Roman and Bekenstein all carry it. So
   *"saturated by black holes"* is recorded in `K`. Coding `G = 1` for the same
   reason **double-counts one fact across two coordinates**, which is exactly
   the fault that makes a coordinate stop being a coordinate.

### THE RULING

**Bekenstein is G = 0.** The `G` slot tests the statement, as the file defines
it; provenance is not in its remit and saturation is in `K`'s. A tree whose
discipline is to follow its own stated rules does not get to make an exception
for the row where the exception is load-bearing.

**If anyone wishes to reverse this, the way to do it is to change the RULE — to
say `G` means "gravitational by provenance" — and then to re-code every other
row against the new rule.** What is not available is leaving the rule as written
and the row as coded.

### What the ruling costs, stated plainly

Measured, and the blast radius is smaller than the consequence:

| | before | after |
|---|---|---|
| bounds cells | 8 | **8** |
| bounds master cell | (0,0,0,2,0) | **(0,0,0,2,0)** |
| bounds closers | nothing | **nothing** |
| R(bounds) | {0,1,2,3,4,7} | **{0,2,3,4,7}** |
| the gravity split | 2 of 9 | **1 of 9** |
| **K1 cells in the bounds index** | **2** | **0** |

And the consequence that matters:

**THE CORPUS NOW HOLDS ONE K1 CELL, AND DOCKET 1 HAS ALREADY RULED IT AN
ARTEFACT.** The survivor is `periodic layout 3-D` at (4, 11, 0), which exists
only in a chart mixing two block conventions.

**So the warp cell's K1 has no other non-artefact instance in this corpus at
all.** That is a stronger and lonelier statement than the one `duality.py` was
built on, and it changes what "the rarest refusal kind" means: not *rare among
several*, but *unique, with the only companions withdrawn*. Anything built on
the K1 thread must be rebuilt on that.

### What is NOT ruled

- **Whether `G` is the right coordinate at all.** `refusal.py` already records
  that *bounds minus its G coordinate* is one of the 20 re-chartings landing on
  the master index's demanded cell; this docket finds that the same coordinate,
  changed on **one member**, destroys the K1 outright. G is load-bearing twice
  over and in opposite directions. That is docket 3's question in its sharpest
  form and it is not answered here.
- **Whether Bousso should also move.** It genuinely carries A/4G, so its G = 1
  is not in dispute under either rule. Only Bekenstein was contested.

---

## DOCKET 5 — THE PRODUCT-BOX FAULT, AND IT DELETES THE DEMAND  **RULED IN PART**

*Raised 2026-09-14 by M: "three of the 23 cells the master index demands are
among the forbidden four ... this is a huge flag we must chase." Chased.*

### The fault

Every density in this tree is taken against a **product box** — `master.shape`
multiplies the sizes of the observed value sets. A product box contains positions
that **no member could ever occupy**, because the coordinates are logically
coupled. Three instances, in increasing order of consequence.

**ONE — the master index's own box.** At arity 2 the only 2-subset of
coordinates is the whole tuple, so statistics admits a cell iff it IS a member,
so statistics always closes and `C = 0` is impossible at arity band 0. Verified
by exhaustion over **74,518 non-degenerate two-coordinate indexes, zero
failures.** Four of the 72 cells are impossible — **and order and algebra each
demand three of them.** An `E` of 25 counts three cells that cannot exist.

**TWO — the refusal index M2.** `H = 0` holds exactly of members and forces
`K = 0, W = 2, J = 3`; `W = 2` is a biconditional with `K in {0,1}`. **645 of
1,152 positions violate one. 507 remain.** No occupied profile violates either.
Density 3.91 % → 8.88 %, which crosses a band edge, which withdrew *the two
master indexes coincide* and *M1 is a cell of itself*.

**THREE — and this one is a theorem.** A Weyl tensor has **exactly four principal
null directions counted with multiplicity**, so `(P, X)` — distinct PNDs and
maximum multiplicity — is a partition of four and admits exactly the six Petrov
types. `petrov.py`'s other two slots, `E` (evidential directness) and `V`
(vacuum), are free.

| | product | realisable |
|---|---|---|
| Petrov box | 5 × 4 × 2 × 2 = **80** | 5 × 2 × 2 = **20** |
| density | 10.0 % → band 1 | **40.0 % → band 2** |
| master cell | (1,1,0,1,1) | **(1,1,0,1,2)** |

*(Robust to the reading: counting Type III's absent `X = 3` as available gives a
box of 24 and 33.3 %, still band 2.)*

### AND THAT DELETES THE STANDING DEMAND

    master index with Petrov corrected:  9 indexes, 8 cells
    order E 25, algebra E 25, geometry E 4, information E 10, statistics E 0
    CLOSES IN statistics.  DEMANDS NOTHING.

The demand `(1,1,0,2,1)` has survived a great deal in this tree — the bounds
index arriving, the bounds fill being withdrawn, DOCKET 1(a)'s Janet
replacement. **It does not survive a theorem about the Weyl tensor.** The
demand's `(C, R) = (1, 1)` two-marginal had Petrov as its sole supplier; move
Petrov and the marginal is gone.

Exhaustive over all 256 R-band assignments to the four indexes whose bands move,
the demand survives **only** where Petrov stays at band 1. Over the tree's own
forty declared bandings it goes from demanded-in-14 to **demanded-in-0**.

### THE RULING, and it is deliberately partial

**RULED: the Petrov correction stands.** It rests on the algebra of the Weyl
tensor, not on a convention, and nothing in this tree gets to prefer a product
box to a theorem.

**RULED: the demand is therefore withdrawn as an outstanding prediction.** Every
statement in this tree of the form *"the master index demands a cell nothing
occupies"* is now conditional on a density taken against a product box, and must
say so or be withdrawn. `master.py` section 7, `rubik.py`'s para-index headline
and `research/README.md` all carry it.

**NOT RULED: the general re-plumbing.** Applying this properly means every index
declaring its realisable box, and `master.shape` taking that instead of the
product. That is a real design change and it is docket 3's question — *what is a
legitimate chart* — in its most concrete form. Four of the nine indexes move
bands at the defensible tier (Janet 1→3 but vacuously, since its realisable box
IS its cell set at exactly 120 = 120; bounds 0→1; periodic 3-D 1→2 or 3;
Petrov 1→2). Five hold.

**LEFT UNDECIDED, and flagged because it is one clause from mattering:** the
energy-condition family does not move on any defensible constraint, but it sits
at density **0.0469 against a band edge of 0.05**. One assumed coupling clause
would move it — into the demanded cell itself. Not claimed either way.

---

## DOCKET 6 — IS THE MASTER INDEX THE RIGHT SHAPE?  **MEASURED, NOT RULED**

*Raised 2026-09-14 by M: "If a vacancy cannot be filled, in an index of
information, why is there no information to fill them? And does this suggest the
index is not as accurate as it should be? Should it be a different shape?"*

### The vacancy count, exactly

The honest lawful box is **84** — seven `(C, Sc, Oc)` signatures from the eight
lawful channel sets (K3 and K4 share `(2,1,0)`), times three arity bands, times
four density bands.

| | |
|---|---|
| lawful box | **84** |
| seated | 8 |
| forbidden (arity-2 lemma, at bandings `[3,5]`/`[3,6]`) | 8 |
| **REALIZABLE VACANCIES** | **68** |

### What is contained in them

A vacancy is a **specification**: *an index closed by these languages, with this
many coordinates, at this density*. Grouped:

| signature | vacant | seated |
|---|---|---|
| closes in nothing | 4 | 4 |
| **information alone** | **8** | **0** |
| statistics alone | 10 | 2 |
| two languages | 11 | 1 |
| **three languages** | **12** | **0** |
| **four languages** | **12** | **0** |
| all five | 11 | 1 |

**Three signatures are wholly empty** — information alone, three languages, four
languages — and that is **32 of the 68**. The rest spread almost uniformly:
19/24/25 across arity bands, 17/15/18/18 across density bands.

**That uniformity is the tell.** If arity and density discriminated which
indexes exist, the vacancies would clump. They do not.

### Why there is no information to fill them

Over the C(9,2) = 36 pairs of seated indexes, how many does each coordinate
separate that **no other coordinate separates**?

| coordinate | separates | separates **uniquely** |
|---|---|---|
| C | 27 of 36 | **0** |
| Sc | 20 | **0** |
| Oc | 8 | **0** |
| D — *assigned* | 24 | **1** |
| R — *assigned* | 27 | **2** |

**The three coordinates this tree defends as measured carry no unique
discrimination at all. The two it apologises for carry all of it.**

And the crux: **seven of the nine seated indexes sit under a signature shared
with another index, and both of those groups are told apart EXCLUSIVELY by D and
R.** The four "closes in nothing" indexes — bounds, periodic 3-D, substances,
the languages — are identical in `(C, Sc, Oc)` and separated only by their arity
and density bands.

**So the answer to M's question is: there is no information to fill the
vacancies because most of them were never information-bearing positions.** The
grid measures a real seven-position classification and then multiplies it
twelvefold by two banded continua. The 68 is the product, not a census of
absence.

### Is there a better derived fit?  NO, AND THE CONTROL IS WHY

| shape | box | cells | density | closes | indexes sharing a cell |
|---|---|---|---|---|---|
| `(C,Sc,Oc,D,R)` full | 84 | 8 | 9.5 % | nothing | 1 |
| `(C,Sc,Oc,R)` | 28 | 7 | 25.0 % | statistics | 2 |
| `(C,Sc,Oc,D)` | 21 | 6 | 28.6 % | statistics | 3 |
| `(C,Sc,Oc)` signature | 7 | 4 | **57.1 %** | **all five** | 5 |
| `(C)` alone | 6 | 4 | 66.7 % | nothing | 5 |

The signature projection looks like the answer — six times the density, and it
closes in all five where the full grid closes in nothing.

**IT IS NOT, AND THE CONTROL SAYS SO OUTRIGHT.** Of the C(7,4) = 35 four-element
subsets of the seven lawful signatures, **all 35 close in all five. 100 %.**
Closure in that box is forced by its smallness and carries no information
whatever. The apparent improvement is an artefact of projecting into a box too
small to fail in.

    A HEADLINE THIS DOCKET NEARLY CARRIED, KILLED BY ITS OWN CONTROL: "the
    closure signature is the better fit, closing in all five where the full grid
    closes in nothing."  False.  Every comparable subset does.

### What is therefore established, and what is not

**ESTABLISHED.** The vacancy rate is a product-box artefact; D and R inflate a
seven-position classification twelvefold. C, Sc and Oc separate nothing
uniquely. Seven of nine indexes are discriminated only by assigned coordinates.

**NOT ESTABLISHED, and not by omission.** That a better shape exists. Every
projection tried trades discrimination for density and buys no closure that
isn't vacuous. The full grid remains the only shape that keeps eight of nine
indexes distinct.

**SO NO RULING.** The right shape is not settled by finding the current one
unsatisfactory, and this docket declines to invent one. What it fixes is the
reading: **the 68 vacancies are not 68 missing indexes.** They are a real
seven-way classification seen through two banded continua, and any statement of
the form *"the master index has 68 unfilled positions"* must say so.

### ADDENDUM — asked to tell its own shape, the index cannot, and the reason is size

*M: "I don't think we need to invent one at all. The index should tell you its
shape, and I can guarantee that shape is definitive."*

**The method is right, it is the corpus's own, and this docket should have
reached for it first.** Register 35: *"the order dimension of Λ is exactly
three… the third coordinate is necessary rather than merely convenient."*
Dushnik–Miller order dimension is an **invariant of the order**, not a choice —
the least number of linear orders whose intersection reproduces the containment.
An index asked that question answers with a number nobody selected.

Asked:

| index | declared | order dimension |
|---|---|---|
| the master index | 5 | **2** |
| bounds | 6 | **2** |
| exotic mechanisms | 6 | **2** |
| the languages | 5 | **2** |
| spacetimes (Petrov) | 4 | **2** |
| substances | 4 | **2** |
| periodic layout 2-D | 2 | 2 — *tight* |
| Janet, periodic 3-D, energy conditions | 3, 3, 6 | ≥ 2, not computed exactly |

And the realizer for the master index is **exhibited, not asserted** — two linear
orders, 42 incomparable pairs, all 42 reversed, intersection reproducing the
containment exactly. That is register 35's own standard: *the realiser is
exhibited, never found; what is falsifiable is the exhibition.*

**AND THE CONTROL SAYS THE ANSWER CARRIES NO INFORMATION.**

| | dimension ≤ 2 among random sets of the same size in the same box |
|---|---|
| master index, 8 cells in 192 | **95.0 %** |
| bounds, 8 in 216 | **96.4 %** |
| Petrov, 8 in 80 | **92.8 %** |
| substances, 8 in 24 | **88.8 %** |
| any 6-cell set | **100 %** |

Almost every small set has dimension 2. Forcing dimension 3 needs a **standard
example** `S₃` — six elements in one exact configuration — and a random eight-cell
set rarely contains one. So *"the master index has order dimension 2"* is true,
exhibited, and **says nothing about the master index**.

    THE SECOND HEADLINE THIS DOCKET KILLED WITH ITS OWN CONTROL, and the pattern
    is now the finding: an apparently decisive structural fact about the master
    index turns out to be a fact about its SIZE.  The first was closure under
    the signature projection (100 % of comparable subsets close).  This is the
    same shape of error, caught the same way.

**SO: the index cannot tell you its shape, and the reason is not that the method
is wrong — it is that there is not enough index to carry the question.**
Register 35 got a definitive answer for Λ because **Λ has 976 cells**. The master
index has **eight**. It is not merely sparse; at this size it is
**under-determined** — too small for its own invariants to discriminate.

**What would change that is not a better shape but more distinct cells** — and
the threshold is now measured rather than gestured at. Testing dimension ≤ 2 by
Gallai's forcing relation (polynomial, so it reaches sizes the linear-extension
enumeration could not), over random sets in the master index's own 192-cell box:

| distinct cells | dim ≤ 2 among random sets | reading |
|---|---|---|
| 6 | 100.0 % | saturated |
| **8** | **96.7 %** | **saturated — the seated master index** |
| 10 | 81.5 % | weak |
| **11** | — | **the populated reading** |
| **12** | **54.2 %** | **INFORMATIVE — a coin flip, so a full bit** |
| 14 | 28.2 % | informative |
| 16 | 15.0 % | informative |
| 20 | 1.7 % | informative |
| 30 | 0.0 % | informative |

**THE THRESHOLD IS TWELVE DISTINCT CELLS.** Below it the answer is forced by
size; at twelve the base rate is a coin flip and the measurement carries a full
bit; by twenty it is decisive.

    The seated master index has EIGHT and needs FOUR more.
    The populated reading has ELEVEN and needs ONE.

**So the populated master index is a single distinct cell away from being able
to state its own shape.** That is the most concrete construction task this whole
line has produced, and the supply is known: the realizable vacancies of DOCKET 6,
or — under DOCKET 7's reading — the two vacant positions of the language lattice,
K1 and K5.

---

## DOCKET 7 — IS THE LANGUAGE INDEX THE MASTER INDEX?  **RULED, IN PART**

*Raised 2026-09-14 by M: "My thought is that perhaps the language index is the
master index."*

### The strong form is false

They are different objects and the refusal index separates them:

    R(the master index) = {0, 2, 3, 4, 5, 7}
    R(the languages)    = {0, 4, 5, 7}

M1 carries K2 and K3 the language index does not. Nine cells against five, and
different content. **Not the same index.**

### But M1's own master cell IS the language index's cell

Corrected symmetrically — both densities against realisable boxes, the fix
`duality.py` §5c makes — M1 sits at **(0, 0, 0, 2, 1)**, and that is exactly
where `the languages` sits. The master index's own master cell is the language
index's cell.

*Recorded and not leaned on:* a random 8-cell set self-coincides about 4 % of the
time, and given self-coincidence, landing on any one of eight occupied cells is
about one in eight. The coincidence is exact; it is not rare.

### AND THE DEEP FORM IS TRUE, WHICH IS WHAT THE HYPOTHESIS WAS FOR

**M1's entire measured content is a point in the language down-set lattice.**

The eight lawful channel sets are precisely the eight **down-sets of the language
containment order** — that is what makes them lawful, and `master.channel_sets()`
derives them that way. So `(C, Sc, Oc)` is not three independent measurements; it
is one measurement, *which languages close this index*, whose value space is an
eight-element lattice of subsets of the languages. Nothing else in M1 is
measured: `D` and `R` are assigned bands, and DOCKET 6 shows they do **all** the
discriminating while `C`, `Sc` and `Oc` separate nothing uniquely.

    THE 84-CELL GRID IS (7 signatures drawn from an 8-element language lattice)
    x (3 arity bands) x (4 density bands).

    THE LATTICE IS MEASURED.  THE TWELVE IS ASSIGNED.

### So the shape M asked for, and it was never invented — it was there

| | positions | occupied | vacancies |
|---|---|---|---|
| as the 84-cell grid | 84 | 8 | **68** |
| **as the language lattice** | **8** | **6** | **2** |

| K | closes in | standing |
|---|---|---|
| K0 | `{}` | seated ×4 |
| **K1** | `{information}` | **VACANT** |
| K2 | `{statistics}` | seated ×3 |
| K3 | `{geometry, statistics}` | species ×4 |
| K4 | `{information, statistics}` | seated ×1 |
| **K5** | `{geometry, information, statistics}` | **VACANT** |
| K6 | `{algebra, information, order, statistics}` | witness |
| K7 | all five | seated ×1 |

**The master index has two vacancies, not sixty-eight.** And both are named
specifications rather than positions in a padded box: *an index closed by
information alone*, and *an index closed by geometry, information and statistics*.
K1 is the warp obstruction's own kind.

### What is ruled, and what this does not claim

**RULED.** Any statement of the form *"the master index has N unfilled
positions"* must say which reading it is using. Against the language lattice —
the only part of M1 that is measured rather than assigned — **N is 2.**

**NOT CLAIMED: that 6 of 8 is remarkable.** Control: nine indexes thrown at eight
positions fill **5.60** on average, and the corpus fills 6. The occupancy is
exactly at chance. What the lattice buys is not a surprising density but the
*right box* — one forced by the closure law rather than chosen, whose vacancies
are specifications instead of padding.

**NOT RULED: that M1 should be rebuilt as the lattice.** Collapsing to it loses
the discrimination `D` and `R` provide, which DOCKET 6 measures as all of it.
The two readings answer different questions and both are now stated.

---

## DOCKET 8 — THE QUESTION ROSTER IS SEVEN, FOR THIS TREE  **RULED**

*M: "There are seven languages, and likely 7 distinct, formalized, universal
questions that can only be asked in that language." And: "This work is proven to
supersede … the older corpus material is now superseded for all further work
unless I rule otherwise."*

### THE RULING

**This tree's question roster is SEVEN — one question per language.** All seven
**ask**; only five **answer with a binary**. That reconciles a discrepancy the
tree had carried unexamined: the channel lattice is built on five because
register 1173 admits a language only if it returns a binary, while the language
index has seven members. The two counts were never in conflict — they count
different things.

| language | asks — one thing, generally | an answer is |
|---|---|---|
| order | is there an admissible precedence? | binary |
| algebra | is it closed under its operation? | binary |
| geometry | does it embed? | binary |
| information | does it need an unavailable coordinate? | binary |
| statistics | is it drawn from a distribution? | binary |
| **analysis** | is there a continuous law? | **magnitude** |
| **documentary** | is it recorded, and by what? | **citation** |

Six are the tree's own words, from `research/README.md`'s expansion table.
`documentary`'s is `cypher.ADMISSION` as `alpha.py` quotes it verbatim.

### SCOPE, AND IT IS NARROW BY CONSTRUCTION

**The roster stays DATA.** `questions.py --roster` selects one, exactly as
`cypher.py` does; nothing asserts a roster in code.

**This rules NOTHING on the corpus's docket 20x-04/20x-09**, which stays open,
and **`tools/cypher.py` is not touched** by this file or this ruling. M's
supersession applies to which findings this tree builds on, not to the store of
record: `method/` and `drive/` are unchanged and stay so.

### AND THE CONSTRUCTION RETURNS A NEGATIVE, WHICH IS THE USEFUL PART

Coordinatised by **properties of the question** — not of the language, or the
index would be the language index relabelled — five coordinates were grounded:
`RET` what an answer is, `OPR` whether an operator answers it, `RUN` whether the
tree has run it, `DECL` roster-1173 declaration, `SPK` whether it speaks on the
energy-condition index.

**They are not independent. `RET` DETERMINES `OPR`, `RUN` and `SPK`; only `DECL`
is independent of it. Seven questions collapse to FOUR distinct cells.**

That is the honest content: *as far as this tree can measure them, the seven
questions differ only in what kind of answer they return, refined once by
whether roster 1173 declared them.* No more resolution is available — the five
binary languages are extensive, idempotent and monotone alike (300 of 300), and
nothing separates them but what they close, which is the channel lattice, which
is the language index again.

### IT LANDS ON THE DEMANDED CELL.  THAT IS NOT A FILL.

The five-coordinate form closes in `statistics` alone at 5.6 % over arity 5 —
master cell **(1, 1, 0, 2, 1)**, exactly `DEMANDED_AT_EIGHT`. Three measurements
refuse the reading:

- **1 of 26** non-degenerate coordinate subsets lands there. Reduced to the
  independent content `(RET, DECL)` it lands on `(2,1,0,0,3)` — already occupied
  by `periodic layout 2-D`.
- **The hit rests on redundant coordinates.** Three of the five are determined
  by `RET`; the arity band placing it at `D = 2` is carried by coordinates that
  say nothing about which question is which.
- **The demand is not live.** DOCKET 5's Petrov correction deletes it —
  Petrov-corrected the master index closes and demands **nothing**.

**AND THIS IS THE THIRD TIME.** The bounds index landed there, its own file
recording *"drop any single one of the five slots and the hit fails"*, and that
fill was withdrawn. `refusal.py` measures **21 of 565** re-chartings of the
already-seated indexes landing there. Now a third construction lands there under
one coordinate choice of twenty-six.

    THE DEMANDED CELL IS EASY TO HIT, AND HITTING IT HAS NEVER ONCE SURVIVED
    SCRUTINY.  The finding is about the demand, not about any of the three
    indexes that hit it.

### AND IT IS SEATED ANYWAY — THE SEATING AND THE FILL ARE DIFFERENT CLAIMS

*M: "It makes sense that the demand cell would demand the questions of the
question index be answered before admittance into the index. So the seating
seems to work."*

Both halves of that reading were checked before anything moved, and both hold:

- **A channel set IS the yes-set of the five binary questions.** Over the nine
  indexes seated at the time, *0 mismatches*: the set of languages that close an
  index is exactly the set of binary questions that answer yes on it. Admission
  to any index in this tree *is* answering those questions. That is definitional
  once the questions are written down, which is why it is stated as a check and
  not as a discovery.
- **The cell was vacant and the seating closes the index.** `questions` is now
  `master.inventory()["questions"]`. Ten indexes, nine distinct master cells,
  and the master index **closes in `statistics` at E = 0, demanding nothing** —
  the first time it has closed since the eighth index was seated.

**THE SEATING IS A CLOSURE FACT. IT IS NOT THE DEMAND MET.** Four measurements
stand against reading it as a fill, and the fourth is new and is the sharpest:

1. **The demand was already deleted** (DOCKET 5). Petrov-corrected, the
   nine-index master index demands nothing at all.
2. **The banding carries it.** `questions` fills the eight-index demand in
   **8 of 40** bandings, and the **ten-index** master index closes in **17 of
   40** — *fewer* than the nine-index one's 20. Seating it made the closure
   slightly *less* banding-robust.
3. **The landing rests on redundant coordinates** — 1 of 26 subsets, three of
   five coordinates determined by `RET`.
4. **The control refuses it.** `master.signature_control` run in the question
   index's own 72-cell box: **4,474 of 20,000** random same-shaped sets land on
   the demanded cell — **22.4 %**. The same control on the bounds box reads
   **4 of 20,000, 0.02 %**. *The non-generic landing belongs to the stage that
   was WITHDRAWN, not to the one that is seated.* Both figures are pinned in
   `master.SIGNATURE_CONTROLS`.

The measurement that survives is the exact one: **E = 0**. Everything read on
top of it is qualified above, and the qualifications are seated in the selftest
so they cannot quietly fall out.

One consequence is recorded rather than repaired: `questions.demand_is_live()`
became **self-referential** on seating — asking whether the demand is live on a
master index that now contains the index being tested. It measures the
nine-index state by default; `demand_is_live(True)` asks the other question and
returns **(1, 1, 0, 1, 1)**, a *different* cell. Correcting the box moves the
demand; it does not certify the one it moved off.

---

## DOCKET 2 — SHOULD THE PERIODIC TABLE BE SEATED MORE THAN ONCE?  **RULED**

> **RULING (M).** *"3D is the finding and it is the superseding model moving
> forward in all projects working with the corpus."*
>
> `periodic layout 2-D` is **WITHDRAWN** from the inventory as
> over-representation. `periodic layout 3-D` supersedes it. Nine seated
> indexes, eight distinct cells.

**AND THE MEASUREMENT NOW SUPPORTS THE RULING, WHERE ONCE IT CUT AGAINST IT.**
The paragraphs below were written when the 3-D chart stopped at Z = 108 — a
defect, not a fact about the chart: `populate.block_of` reads the *observed*
differentiating electron from `LW1-ground.py`, which stops there. Taken from
Madelung, which needs no observation, **both charts reach 92 positions**, and on
all ninety-two:

| chart | cells | injective | reaches |
|---|---|---|---|
| `(period, group)` | 92 | yes, one element each | Z ≤ 120 |
| `(period, group, block)` | 92 | yes, one element each | Z ≤ 120 |
| `(n+ℓ, ℓ)` | 20 | **no** — 92 onto 20 | Z ≤ 120 |

3-D projected onto `(period, group)` **is** 2-D, cell for cell, and `block` is a
function of `(period, group)` with **zero** exceptions. So 2-D is a strict
projection of 3-D and reaches nothing 3-D does not. The old objection — *"2-D
reaches ten elements 3-D cannot"* — was an artefact of the truncated build and
is **withdrawn**. Janet stays: it is a strict coarsening, not a duplicate, and
it is the only chart of the three that is not injective.

**WHAT THE RULING COST, STATED IN FULL.** Withdrawing one index is not free and
none of this is hidden:

- **The master index GAINED a language.** At ten it closed in `{statistics}`
  alone; at nine it closes in `{geometry, statistics}`. The withdrawn chart was
  obstructing geometry.
- **K1 left the corpus entirely.** `refusal.py` §4's rarest refusal kind is now
  carried by no seated index. The cause is **the block convention, not the
  reach** — see the four-build table in `refusal.block_convention_table()` —
  and completing the chart *forced* that convention, because past Z = 108 there
  is no observed differentiating electron to read. **That convention question
  is still open and a ruling is owed**; DOCKET 2 closed it by side effect.
- **K7 became universal.** The withdrawn chart was the one index too dense
  (71.4 %) to have a cell every language refuses. The counterexample was
  removed rather than explained, so this is a fact about the seated nine and
  not a law about indexes.
- **`rubik.py`\'s discriminator became under-powered** — the withdrawal removed
  most of the law-violating region and its sampled test began reporting two
  unlawful containments as lawful. Repaired by making it exhaustive.

**A departure from a corpus figure was required and is recorded.** The
open-bound ruling (*"until we can prove that no more elements are left to
discover or synthesize, the upper bound of the periodic table is open"*) applies
to both charts or to neither. Applied to 2-D it gives 92 cells where chapter 6
draws 90. **The corpus is not changed**: section 6 still states ninety,
`tools/populate.py` is untouched, and `layout_closure()` returns what it always
returned. `research/` now *constructs* its two-coordinate chart instead of
importing the drawn one. M: *"yes, and we must do it because the evidence says
we must."*

The original argument, kept as the record of what was measured before:

---

### The original entry (superseded above)

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
stated one, and docket 3 is why that is now urgent. *(DOCKET 3 now states one —
see the ruling below.)*

---

## DOCKET 10 — IS K6 OCCUPIED?  **OPEN**

**A chart of the corpus's own element data lands in K6, and K6 was vacant.** The
master index occupies K0, K2 and K7 and nothing else. K6 —
`{order, algebra, information, statistics}`, everything but geometry — is the
channel that is **alone in its phase**, join-irreducible, meet-irreducible, a
co-atom. `madelung.k6_chart()` is `(n+ℓ, k)`: the 170 differentiating electrons
addressed by fill-order shell and slot, with the subshell dropped. It closes in
exactly those four.

**The reach control passes.** K6 at every complete shell reach from
`n+ℓ ≤ 3` through `n+ℓ ≤ 11` — nine consecutive reaches, 10 cells to 122. Only
the two degenerate reaches give K7.

**And it is half of an exact duality.** The same projection on the other base —
`(n, k)`, the shell fibration with ℓ dropped — gives 82 cells too, a *different*
82, and lands in **K3**. The two channels are complementary: union all five,
intersection `{statistics}`, the poset minimum. K3 = down(geometry) and
K6 = down(order) = down(algebra), so **the two charts realise the principal
down-sets of the two maximal languages** — the two switches of the phase square.
Which maximal language survives is decided by the choice of base and nothing
else.

**WHAT IS MEASURED IS THAT K6 IS REACHABLE.** That was open before, and it is
now closed: a chart built only from seated corpus data sits in K6 and stays
there across an order of magnitude of reach.

**WHAT IS NOT MEASURED IS THAT IT DESERVES A SEAT**, and there is a real
objection:

> **The K6 chart is a COARSENING.** It maps 170 elements onto 82 cells —
> **88 elements share an address with another** and the chart cannot say which
> element is which. Every one of the nine seated indexes, and both fibrations,
> are injective on their own members. A non-injective chart of 170 elements is
> a weaker object than any of them.

DOCKET 3's criterion does not settle this: it governs the **coordinates of the
master index** and asks whether a coordinate survives an appended monotone
redundant one. Dropping a coordinate is a different operation, and no criterion
in this tree governs it. The nearest precedent cuts against seating — the
re-charting census in `refusal.py` §2 treats coordinate drops as showing the
demand is *chart-relative*, not as producing new members.

**What would settle it:** a criterion for when a coarsening may be seated. The
obvious candidate — that a seated index must be injective on the objects it
charts — would refuse this one and would also have to be checked against the
nine already seated. **Janet is a coarsening too**, of the elements onto
`(n+ℓ, ℓ, k)`; it is injective there, but `(n+ℓ, ℓ)` alone is not, and DOCKET 2
turned on exactly which projections count.

Nothing is seated on the strength of this. K6 is **reachable and unseated**.

---

## DOCKET 9 — WHICH BLOCK CONVENTION DOES THE CORPUS RULE FOR?  **OPEN, AND OWED**

**DOCKET 2 CLOSED THIS BY SIDE EFFECT AND THAT IS NOT A RULING.** Completing the
three-coordinate layout required abandoning the *observed* differentiating
electron — `populate.block_of` reads it from `LW1-ground.py`, which stops at
Z = 108, so past there is nothing to read — and adopting the *Madelung* block.
That was forced by the completion, argued for by nobody, and it destroyed the
corpus's last K1 cell.

**THE MEASUREMENT ISOLATING IT** (`refusal.block_convention_table()`):

| reach | block convention | cells | K1 |
|---|---|---|---|
| 108 | observed | 80 | at `(4,11,0)` |
| 108 | **madelung** | 80 | **none** |
| 120 | observed | 80 | at `(4,11,0)` |
| 120 | **madelung** | 92 | **none** |

The reach does nothing alone — under the observed convention, extending to 120
adds not one cell. **The convention does all of it.**

**AND `refusal.py` §4 PREDICTED THE DESTINATION BEFORE DOCKET 2 EXISTED**, for a
*third* convention (the block read off the drawn layout): *"K1 VANISHES,
becoming K4 {information, statistics}"*. The measured value of `(4,11,0)` in the
completed chart is K4, `{information, statistics}`, exactly. Two different
departures from the observed convention, the same destination.

**What would settle it:** a corpus citation. `populate.py`'s `block_of` asserts
its convention in a docstring **without citing a register**, where `period_of`
and `group_of` are pinned to section 6's ninety cells. DOCKET 1 ruled on how a
block is *assigned* given a convention; it did not rule on which convention the
corpus holds. Until that is settled, **the absence of K1 from this corpus is a
fact about a convention this tree chose under duress**, and must not be quoted
as a fact about the elements.

Nothing is repaired on the strength of this.

---

## DOCKET 3 — WHAT IS A LEGITIMATE CHART?  **RULED**

> **THE CRITERION.** A coordinate of the master index is **admissible** iff it
> is invariant under appending a **monotone redundant** coordinate to the index
> it charts.

**IT IS WELL-POSED, AND THAT IS THE WHOLE ARGUMENT.** For monotone `g`,
`(x, g(x)) ≤ (y, g(y)) ⟺ x ≤ y`. So appending a monotone redundant coordinate
cannot change the order, cannot change which elements the index distinguishes,
and cannot change anything the index *is*. Whatever moves under it was reading
the chart and not the object. No appeal to taste, no list of blessed
coordinates — one operation, and the coordinate either survives it or does not.

**MEASURED OVER THE NINE SEATED INDEXES** (`charts.py`):

| coordinate | moves on | verdict |
|---|---|---|
| arity | 9 of 9 | **DISQUALIFIED** |
| density | 9 of 9 | **DISQUALIFIED** |
| height | 0 of 9 | admitted |
| width | 0 of 9 | admitted |
| cells | 0 of 9 | admitted |
| comparable pairs | 0 of 9 | admitted |
| join-irreducibles | 0 of 9 | admitted |

The separation is total — 9/9 or 0/9, nothing in between. **`D` and `R`, two of
the five coordinates the master cell has been written in throughout this tree,
fail.** `C` survives, which is why the closure reading was never in doubt.

**CONSEQUENCE, AND IT IS THE REBUILD.** `mi.py` charts the master index on
`(K, height, width)` — all admissible — and inherits nothing from `master.py`.
`master.py` keeps its five-coordinate cell so the record of what was measured
under it stays readable, and every file that quotes a five-coordinate cell is a
statement about a chart two of whose coordinates are now known to be decoration.
`rubik.py` §5b records the sharpest case: its puzzle is the cuboid `(C, D, R)`,
so its "legitimate perturbation" shifts exactly the two disqualified axes.

**AND IT ANSWERS THE DEMAND.** The demanded cell `(1,1,0,2,1)` is written in the
disqualified chart. The criterion does not say the demand is void; it says the
demand was **exactly as strong as the then-unstated criterion**, which is
weaker than it has been stated anywhere in this tree, and that the right cell
to demand is one written in admissible coordinates. Nothing is repaired on the
strength of this — the five-coordinate readings stand as records.

The original argument, kept as the record of what was measured before:

---

### The original entry (superseded above)

A master cell is a property of the **chart**, not of the object. Appending a
coordinate that is a *function of the existing ones* — zero information — moves
**six of the ten** seated master cells (five of nine before DOCKET 8). A **monotone** such coordinate leaves
every channel intact; a **non-monotone** one does not, and the periodic table's
block is the witness in this tree's own membership.

**And the demanded cell `(1,1,0,2,1)` is reachable by re-charting what is
already seated: 28 of 640 re-chartings land on it**, including the bounds index
minus its gravity coordinate, the energy-condition family under five different
single-coordinate drops, and — since DOCKET 8 — **seven re-chartings of the
question index that now occupies it**. That last is the sharpest form of this
docket's point: the index seated *on* the cell can be re-charted seven ways and
still land there, which measures the cell's reachability, not the seating.

So the demand is exactly as strong as a criterion for a legitimate chart, and no
such criterion exists here. Until one does, **a demanded cell is a demand for a
chart with those properties, not for an object** — which is weaker than the
demand has been stated at anywhere in this tree.

Nothing is repaired on the strength of this. It is recorded, and it gates
docket 2.
