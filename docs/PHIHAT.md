# `tools/phihat.py` — φ̂ at arbitrary caps, and which form of it is right

`r2lib.py` L391–392 records what was missing:

> Its companion `phi_at` is **NOT lifted**: it depends on TERMS, which is still owed.

This supplies both. TERMS is §12.11.1's microstate enumeration, run rather than described;
`phi_at` is φ̂ at any caps, computed rather than hardcoded at the three values `tower-2.py` carries.

```sh
python3 tools/phihat.py --candidates                     # the forms, as data
python3 tools/phihat.py --compare                        # every form against the record
python3 tools/phihat.py --phi   --caps 4,4,2,6,2
python3 tools/phihat.py --tower --caps 4,4,2,6,2 --form pointwise
python3 tools/phihat.py --max2j --l 3
python3 tools/phihat.py --selftest
```

Stdlib only, Python 3.9+.

## It takes no position

§12.11.1 gives φ̂'s genus and one value set — *"the monotone envelope of k → max 2J over the parent
shells admitted by the caps, so φ̂ = {1: 3, 2: 4, 3: 5} at 7.4's"* — and never says **over what** the
envelope is taken. Members print it two ways. So the candidate forms are **data**, exactly as
`cypher.py`'s language rosters are data, and the tool **measures** each against the numbers the
corpus records rather than asserting one.

| form | definition |
| --- | --- |
| `pointwise` | max 2J over terms of ℓᵏ at occupancy exactly k — the form printed at MC L1686 and Transitions A15 L1819, both with no envelope operation |
| `running-max` | max over k′ ≤ k of the pointwise value: the monotone majorant |
| `fold` | max over the particle–hole conjugate pair k and 4ℓ+2−k, using §8.4's conjugation |
| `clamp-half` | the pointwise value at min(k, half filling) per shell |
| `global-max` | constant at the largest pointwise value under the caps |

## What the record decides

Five fixtures, every one a number the corpus states about itself:

```
  form         [1]  [2]  [3]  [4]  [5]
  pointwise     ok   ok    x    x   ok
  running-max   ok   ok   ok   ok   ok
  fold          ok   ok    x    x   ok
  clamp-half    ok   ok   ok   ok   ok
  global-max     x    x    x   ok   ok
```

1. φ̂ = {1:3, 2:4, 3:5} at §7.4's caps — main L3072, MC L1686, `tower-2.py`'s `PHI`
2. |Λ₈…Λ₁₃| = 976 / 1,654 / 2,535 / 13,585 / 70,905 / 199,130 — §12.11.0.10's table
3. |Λ₁₃| = 199,130 / 4,731,790 / 40,310,170 / 77,083,771 at the four caps — main L3124–3125
4. φ̂ monotone at all four caps — main L3122, *"φ̂ stays monotone"*
5. |Λ₈| = 976 / 1,636 / 2,394 — `r2lib.py` L390–391's own documented returns

**`pointwise`, `fold` and `global-max` are refuted.** Fixtures 1, 2 and 5 cannot separate anything —
every form except `global-max` passes them, because they all live at or below k = 3 where the
question does not arise. Fixtures **3 and 4 do the work**, and they are the only two that reach
k = 6.

`running-max` and `clamp-half` both survive, and they are **not the same expression** — they differ
at 648 of 1,512 cap settings swept. But at **none** of the 864 that are Pauli-consistent. They part
only where k_max exceeds the largest admitted shell's capacity, which §7.1's `k ≤ 2(2ℓ+1)` already
forbids. **On the admissible domain the record is decisive**, and the tool says so rather than
leaving "indistinguishable" as the last word.

### The whole disagreement is one cell

At caps (4, 4, 2, 6, 2):

```
running-max   φ̂ = {1:5, 2:8, 3:11, 4:12, 5:13, 6:13}   monotone: True    |Λ₁₃| = 40,310,170  ✓
pointwise     φ̂ = {1:5, 2:8, 3:11, 4:12, 5:13, 6:12}   monotone: False   |Λ₁₃| = 37,954,320  ✗
```

φ̂(6) = 13 against 12. That single value is worth **2,355,850 cells** in |Λ₁₃|, and it is invisible
at §7.4's caps, where k stops at 3 and every form agrees.

## Why the printed form is wrong, in the corpus's own words

The corpus already knows the pointwise object is non-monotone, and already gives it a **different
name**. Main L3368–3369:

> §8.4 — particle-hole conjugation, terms(ℓᵏ) = terms(ℓ^(4ℓ+2−k)), verified exactly for every k on
> the p and d shells — and **a symmetric non-constant function is not monotone, so §14.4 cannot
> carry it** … **max2J(ℓ,k), unimodal with its peak at half filling, 25 at f⁷, zero at closure**,
> for the core's J.

and §12.11.2, main L3382–3383:

> the core's J needs a non-monotone φ. **Each admissible extension is the monotone envelope of its
> physics.**

So `max2J` is the physics and φ̂ is its monotone envelope. MC L1686 and Transitions A15 L1819 print
φ̂ *as* `max2J`, with no envelope, and Transitions A15 then gives that formula the Status line
**"monotone in k"** — which is false of what it printed, by §12.11.2's own sentence.

`max2J` is exposed separately by `--max2j`, with all four of its recorded properties asserted in the
self-test: 25 at f⁷, peak at half filling, zero at closure, fold-symmetric on p, d and f. Those were
banked at WORKING-REGISTER L4817 against `r2-ch12y.out` (42a33746), and this reproduces them.

## Witness status, and it is carried

Every count this tool prints is **`THEORETICAL`**: proven by construction on the lattice, never
verified by spectroscopic measurement. M's ruling: such a figure is publishable **as theoretically
proven but not yet witnessed**, and the label travels with the number. A tower count is not a
measurement and this tool never prints one as though it were.

## Three things it refuses to do

1. **It never asserts a form.** `--compare` reports what each candidate reproduces and what it
   fails, and where survivors part. The first version of this tool asserted `running-max` in its own
   self-test and the comparison refused it — two forms survive, not one, and the fixture now says so.
2. **It never prints a count without its witness status.** `THEORETICAL` is a class, not a hedge.
3. **It never edits a seated member.** `phi_at` is owed to `r2lib.py`; lifting it there is a close
   action under `close.py --append`, not this tool's to take.

## `--selftest`

36 fixtures: TERMS against textbook values (p², p³, d², s², p⁶); `max2J`'s four recorded properties
on p, d and f; §8.4's conjugation as *terms*, not merely as `max2J`; the full comparison, asserting
which candidates are refuted and which survive; that `pointwise` passes fixture 1 and fails fixture 3
— because if it failed at §7.4's caps the ambiguity would never have been invisible, and it was; the
survivors' divergence, asserting it is non-empty overall and empty on the Pauli-consistent domain;
and §12.11.0.10's whole table.

Current state: `SELFTEST OK`.

## Known gaps

- **`phi_at` is not lifted to `r2lib`.** It lives here because a seated member may not be edited in
  place. The lift is a close action, and `TERMS` goes with it.
- **The tower is counted, not enumerated.** |Λ₁₃| at (5,5,2,6,2) is 77 million cells; the counts are
  combinatorial. That makes them fast and means this tool cannot answer set questions — closure,
  E, projections — only cardinalities. `cypher.py` holds ℛ for the set questions.
- **Five candidates is not all candidates.** The roster is data and takes additions. A form that
  reproduces fixtures 3 and 4 by some other route would deserve a row.
- **The refutation is of the printed formula, not of the members' intent.** MC L1686 and
  Transitions A15 may mean the envelope and have compressed the notation. Which is the case is a
  ruling, and the classification of the defect is M's.
