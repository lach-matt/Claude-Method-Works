# THE REFUSAL INDEX

> M: *"A refusal index is a tremendous amount of information. We need to build it
> and populate it, analyze, document and seat it as an extension of the master
> index."*
>
> *"each index likely shares the same refusal index as us, which means we can
> draw threads that extend through multiple MIs"*

Both were right, and the second is right about a **smaller object** than it
names. Building it turned into a measurement of the master index's own
construction, and that measurement cost the tree four published findings and its
central device.

Every figure below carries the command that produces it. Run from
`research/warp-drive/` unless stated. The instrument is `refusal.py`; the
rulings it depends on are in `DOCKET.md`.

---

## 1. What it is

A **channel set** is which languages *close* an index — a property of `X`. A
**refusal set** is which languages *refuse* a cell `c` of `X`'s box — a property
of the **pair** `(X, c)`. Both are down-sets of the hierarchy law's containment
order, by dual arguments, so both live in the same eight lawful positions
`K0…K7`. `duality.py` establishes that and is the file to read first.

The refusal index of `X` is then the simplest thing in the neighbourhood:

```
R(X) = { the refusal set of c : c a cell of X's box }   ⊆ {K0 … K7}
```

    python3 -c "import refusal; [print('%-28s %s' % (n, sorted(s))) for n,s in sorted(refusal.refusal_index().items())]"

| index | R(X) |
|---|---|
| Janet `(n+ℓ, ℓ, k)` | `{0,7}` |
| periodic layout 2-D | `{0,4}` |
| substances (Hawking–Ellis) | `{0,2,7}` |
| the languages | `{0,4,5,7}` |
| bounds | `{0,2,3,4,7}` |
| questions | `{0,2,4,5,7}` |
| spacetimes (Petrov) | `{0,3,4,5,7}` |
| energy-condition family | `{0,2,3,4,5,7}` |
| exotic mechanisms | `{0,2,3,4,5,6,7}` |
| periodic layout 3-D | `{0,1,3,4,5,6,7}` |

**K0 is universal.** Every seated index has cells that *nothing* refuses — cells
inside all five closures. Ten of ten.

**K7 is in nine of ten.** The exception is `periodic layout 2-D`, and it is the
densest index in the corpus at 71.4 %: too full to have a cell every language
refuses. Dilute it and K7 appears — see §3.

**The lattice.** Minimal: Janet and periodic layout 2-D. Maximal: exotic
mechanisms and periodic layout 3-D. **Thirteen of the forty-five pairs are
incomparable**, so this is a lattice and not a chain — the same shape the channel
reading has, and for the same reason. The tenth index, `questions`, changed
neither the minima nor the maxima: it sits at `{0,2,4,5,7}`, inside `exotic
mechanisms`, and it is the only index whose *whole profile set* nests inside
another's (§3).

---

## 2. The coordinates, and which of them are real

`duality.py`'s `M2` profiles a pair as `(K, W, H, J, A)`: the refusal set, marginal
completeness, capped Hamming distance to the nearest member, join/meet status,
and the host's arity band. All five survive a redundancy audit — none is a
function of the other four — but two exact constraints hold over all 2,508 real
pairs:

- `H = 0` holds **exactly of member cells**, and a member lies in every closure,
  so `H = 0` forces `K = 0`, `W = 2` and `J = 3` together.
- `W = 2` exactly when statistics admits, which is exactly `K ∈ {0,1}`.

**645 of the 1,152 product positions violate one of those. 507 remain.** No
occupied profile violates either, which is the check that the constraints were
found rather than invented. That is §5's fault in miniature, and it is what
withdrew *the two master indexes coincide*.

### K is the object. W, H, J and A are chart decoration.

Append a coordinate that is a **function of the existing ones** — zero
information about which member is which — and truncate the profile:

    python3 -c "import refusal; [print(k, refusal.truncation_survival(k)[:2]) for k in (('K','W','H','J','A'),('K','W','J'),('K','W'),('K',))]"

| truncation | invariant in |
|---|---|
| `(K,W,H,J,A)` | 3 of 9 |
| `(K,W,J)` | 6 of 9 |
| `(K,W)` | 6 of 9 |
| **`(K)`** | **8 of 9 — and the one exception only GROWS** |

The exception is `periodic layout 2-D`, whose `{0,4}` gains K7. So **K is monotone
under monotone re-charting: it never loses a refusal kind.** `H` is a capped
Hamming distance and `A` is the host's arity band, both dimension-dependent by
construction; what is worth having is that dropping them is not enough, and only
`K` survives.

Under a **non-monotone** re-charting `K` is not even monotone — the periodic
table's 2-D profiles are not contained in its 3-D ones. The invariance is
conditional and the condition is stated.

---

## 3. Does every index share one refusal index? No, and the control kills the
## question too

Built **separately per index** on the full `(K,W,H,J,A)` profile, the ten sets are
**0 of 45 identical and 2 of 45 comparable** — at full coordinates and with `A`
dropped alike. The conjecture is false at its strongest reading: no two indexes
have the same refusal profile set, and 43 of the 45 pairs do not even nest.

**AND THE "0 of 36 comparable" THIS SECTION USED TO CLAIM WAS ALREADY STALE
BEFORE THE TENTH INDEX ARRIVED.** The two comparable pairs are

    Janet (n+l, l, k)  ⊆  periodic layout 3-D      3 profiles inside 12
    questions          ⊆  exotic mechanisms        7 profiles inside 17

and only the second involves the index DOCKET 8 seated. The first is a
consequence of **DOCKET 1(a)**, which recoded Janet from the arity-2 `(n+l, l)`
chart to the complete arity-3 `(n+l, l, k)` table; the sentence here was written
before that and was never re-measured. Recorded as a correction to this file, not
to the instrument — `refusal.py` computes it fresh every run.

**The control still says observing zero *identical* pairs was never informative.**
Over random families of the same shapes, identical pairs came out at a mean of
**0.07 of 36** at nine indexes. That control has **not** been re-run at ten and
the figure is quoted as what it is: the nine-index measurement.

There is exactly **one** profile all ten share, `(K,W,H,J) = (0,2,0,3)`, and it
holds of a cell **iff that cell is a member** — definitional, and worthless. Any
claim of the form *"all ten indexes share a refusal profile"* is true and empty.

**What replaces the conjecture is sharper**: a rare `K` value is a thread between
exactly the indexes carrying it. That is why §4 mattered, and why §4 is now
closed.

---

## 4. The K1 thread, and it is dead at both ends

K1 — *information refuses, everything else admits*; every pair of requirements
jointly satisfiable and the full combination not — was the warp obstruction's own
kind, and it occurred in two indexes. Neither survived.

**DOCKET 1 — the periodic K1 is a CONVENTION seam.** `periodic layout 3-D` takes
period and group from the drawn 18-column layout and the block from the observed
differentiating electron. Three coherent single-convention charts were built and
**none produces a K1 cell**:

| chart | cells | closes in | R(X) | K1 |
|---|---|---|---|---|
| pure Madelung — Janet, Z ≤ 120 | 120 | all five, E = 0 | `{0,7}` | no |
| pure observed — Janet, Z ≤ 108 | 98 | nothing | `{0,2,6,7}` | no |
| pure drawn layout | 80 | nothing | — | no |
| **hybrid, as seated** | 80 | nothing | `{0,1,3,4,5,6,7}` | **yes** |

The hybrid carries **seven of eight refusal kinds** where the pure charts carry
two and four. *Mixing conventions manufactures refusal structure*, and that is
the general form of the finding.

The cell rests on exactly two elements — copper and silver; 157 of 160
single-cell perturbations leave it in place — and the chain is palladium's empty
valence 5s → silver alone in the s-block at group 11 → statistics admits
`(4,11,0)` → K1. *(A framing corrected on the way: copper's anomaly is irrelevant;
**nickel's normality** is the cause.)*

**DOCKET 4 — the bounds K1 is a CODING seam of the same shape.** `bounds.py`'s
own rule for the gravity slot is *"a G or an area appears"*. Bekenstein's bound
is `S ≤ 2πRE` — neither. Bousso states in print that it *"does not contain
Newton's constant"*. And the black-hole saturation that motivated `G = 1` is
already carried by the `K` slot, so coding it again double-counts one fact across
two coordinates. Re-coded, **the bounds index holds no K1 cell.**

**So the corpus holds one K1 cell and DOCKET 1 ruled it an artefact.**

### And the warp cell's K1 is a different object entirely

    python3 -c "import inspect, statrow; print(inspect.getsource(statrow.refusing_set))"

```python
def refusing_set(statistics_admits=True):
    r = {"information"}          # a hardcoded literal
    ...
```

**It is written by hand.** `channel_of_refusal()` looks that literal up in the
lawful down-set list. Every corpus K1 is *computed* as `c ∉ cl_L(X)` over a real
box. The two share a label, not a procedure — which is exactly why the
correspondence looked too strong to be chance.

Three more results close it. The **top-corner theorem**: if the warp cell is read
as *every requirement met*, it is the coordinatewise maximum, which is the join of
all members, and `information` **is** the join closure — so information always
admits and the refusal can never be K1. Zero violations over 9 seated indexes,
3,000 hostile families and 173,991 exhaustive cases. The **base rate**: random
families hold a K1 cell 53–89 % of the time, so at 0.123 % the seated corpus is
~30× *depleted* — K1 is not rare in general, only here. And the **metals do not
touch the device work**: ten instruments name copper three times, none
load-bearing, and no conductivity exists anywhere in the chain.

**What survives is real.** `expand.py`'s verdict table is a genuine measurement —
four languages admit, information refuses, each row from its own instrument. The
obstruction stands. Its identification with the corpus's K1 cells does not.

---

## 5. Why it is not seated as a tenth index

`R` is computed **from** the inventory. Seating it changes the inventory, which
changes `R`. That is a fixed point, not a formality — and a separate pass reports
the iteration converging to a unique 49-cell fixed point in one step. **That
figure is reported and not independently verified here.**

But there is a prior reason to wait, and it is §6. Seating anything new into a
master index whose cells are **charts rather than objects** seats a chart.
`refusal.py` therefore seats `R` as a **function on the members** — an added
structure, addressable by name, with its own lattice — and adds no row. M's word,
*extension*, was the right one.

---

## 6. The fault this build uncovered

Every density in this tree is taken against a **product box**, and a product box
holds positions no member could occupy.

**The master index's cells are charts, not objects.** On the 80 elements all
three periodic charts reach, `(period, group)` and `(period, group, block)` are
both injective, and `block` is a **function of** `(period, group)` there — the
3-D chart is the 2-D chart plus a coordinate carrying zero information. Yet:

| chart, same 80 elements | closes in | master cell |
|---|---|---|
| `(period, group)` | statistics | (1,1,0,0,3) |
| + a **monotone** redundant coordinate | statistics | (1,1,0,1,1) |
| + the **block**, non-monotone, 356 order-reversing pairs | **nothing** | (0,0,0,1,1) |

Across the ten, a monotone redundant coordinate moves **six** master cells and
changes **no** channel.

**And the demand was satisfiable by relabelling.** 28 of 640 re-chartings of the
already-seated ten land on `(1,1,0,2,1)` — including **the bounds index minus its
gravity coordinate**, and the energy-condition family under five different
single-coordinate drops.

**Then the demand was deleted outright.** A Weyl tensor has exactly four principal
null directions, so Petrov's `(P,X)` is a partition of four: product box 80,
realisable box **20**, density 10.0 % → 40.0 %, band 1 → 2. The demand's
`(C,R) = (1,1)` marginal had Petrov as its sole supplier. **With Petrov corrected
the master index closes in statistics at E = 0 and demands nothing.** See DOCKET 5.

**And order and algebra demand the impossible.** At arity 2 the only 2-subset is
the whole tuple, so statistics always closes and `C = 0` cannot occur at arity
band 0 — 74,518 non-degenerate two-coordinate indexes, zero failures. Four cells
are impossible and **order and algebra each demand three of them**; screened,
both fall from `E = 25` to **`E_realisable = 22`**.

> **Two corrections a later pass forced on this section.** *The forbidden four
> are banding-dependent*: forbidden under arity bandings `[3,5]` and `[3,6]`,
> where band 0 is arity 2 alone, but under `[4,5]` and `[4,6]` — both in the
> tree's own alternatives — band 0 admits arity 3, `C = 0` occurs there, and
> **nothing is forbidden**. And *the 72-cell box is itself a product-box
> artefact*: the honest lawful box is **84**, seven channel signatures not six.
> The dropped one is **K1 at `(C 1, Sc 0, Oc 0)`**, assumed away by a map whose
> own status reads RECONSTRUCTED — and it is **reachable**, witness
> `{(0,0,0), (0,1,1), (1,0,1), (1,1,1)}`. Corrected: **8 forbidden, 76
> reachable.** That kills *(Sc, Oc) is a strict function of C* as a law about
> indexes; it survives only as a statement about this corpus, where K1 is vacant
> over the ten seated and the seventy species.

---

## 7. The vacancy census

Of the 72 master cells, **exactly four are forbidden** and all 68 others are
reachable with an explicit witness set verified by hlaw's own operators — and
over the corrected **84-cell lawful box** it is **8 forbidden, 76 reachable**.
Of the 41 vacant cells only **one** is forbidden; the other **40 were filled**.

So M's bet — *"most if not all of the non-contractual ones can be identified and
filled"* — **is won**, 40 of 41, with the exception provably impossible.

Two supporting lemmas, both re-proved: an **injective coordinate** forces
statistics to close at every arity (232 cases, 0 failures); **all-binary
coordinates** force `geometry(X) = statistics(X)` (200 cases, 0 failures). Arity
is **free upward** — the free-coordinate and duplication liftings never fail in
69,238 checks — but neither lemma lowers arity, so every arity-2 result had to be
built directly.

---

## 8. Recorded, not repaired

- **The ten refusal indexes are pairwise distinct**, and the control says that was
  never going to be otherwise. They are *not* pairwise incomparable — two of the
  45 pairs nest, and §3 records that this file claimed otherwise on a stale
  measurement. Recorded.
- **K1 has one instance and it is an artefact.** The warp obstruction stands on
  its own measurement and has no companion in this corpus.
- **The demand mechanism is NOT empty, and this bullet said the opposite.** A
  screening pass shows **every demand the lattice has ever made is realisable** —
  56 (banding, state, cell) triples across the whole history, **zero** forbidden.
  So `E_realisable` salvages nothing because nothing needed salvaging: it bites
  on order and algebra alone. Petrov-corrected, the **populated 80-index** master
  index still demands `(1,1,0,0,2)` — and now `(1,1,0,1,1)` beside it — while the
  seated ten demand something in **23 of the 40** declared bandings. What DOCKET 5
  deletes is *this* demand, at *this* banding, on *these* indexes — not the
  mechanism. (The Petrov-corrected per-banding figure of 9 of 40 recorded here was
  taken at nine indexes and has **not** been re-measured at ten; the 23 above is
  the uncorrected sweep, which is a different quantity.)
- **The scramble census is the one mechanism here that demands the impossible.**
  It names all four forbidden cells among its seventeen para-indexes, at
  robustness 0.059, 0.049, 0.041 and 0.030, none in the top four. Screened it is
  **13, not 17**. A slice move can carry a `C = 0` cell into arity band 0, which
  no index can occupy. `rubik.py` records none of this.
- **A product-box fault one level up.** The master index's *own* box is 192
  product positions against **52** realisable, and its self-density moves
  4.17 % → 15.38 %, band 0 → band 1.
- **`master.shape` still multiplies value-set sizes.** Applying the realisable box
  properly means every index declaring one — a real design change, and docket 3's
  question in its most concrete form.
- **The energy-condition family sits at density 0.0469 against a band edge of
  0.05.** One assumed coupling clause would move it into the demanded cell
  itself. Undecided, and flagged because it is one clause from mattering.
