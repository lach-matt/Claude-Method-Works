# READ-regsweep.md — the Register read: the whole-volume mechanical baseline

**Not a substitute for the source-order read.** M ruled the Register is read in full under the
chat-81 cadence, and it is. This instrument exists so each unit scores its prose against a measured
baseline rather than rebuilding the same six resolvers thirty-eight times. It answers only what a
machine can answer over all 1,635 entries at once; every claim question — whether a resolved pointer
carries the claim, whether a numeral is superseded-and-preserved or stale-and-colliding, whether a
count word counts what it says — stays with the unit reads.

Instrument `r2-regsweep.py`, golden `r2-regsweep.out`. All instrument checks OK.

## The fault worth naming first, because it is the worst kind

The section resolver first ended in `\s+`, **which matches a newline**. So `### 784` — a Register
*entry* heading — satisfied the pattern for `§784`, and the sweep reported that pointer as resolving.
It does not resolve: §784 is a register number printed with a § sigil, and it is **26b-08, already
recorded at W-190**. An instrument that *hides* a known finding is worse than one that invents a
false one. It hid it for exactly one run. The resolver now requires a title after the numeral on the
same line, which no bare entry heading can satisfy.

## What the baseline establishes

- **Population.** 1,635 entries — 1,628 bare, 7 grouped — over 1,660 distinct numbers, and **no entry
  number is printed twice**.
- **Every entry carries a bold headline.** 1,635 of 1,635; none has an empty body.
- **Every section pointer is accounted for.** 180 distinct pointers; eleven resolve in no volume and
  **all eleven have a witness**: §0 is the Spectra Compendium's own §0; §4.1–§4.7 are Chapter 4's
  list items rather than headings (MAIN_AUDIT V1); §5.7 is the companion paper (IOI_SPEC_AUDIT I1);
  §8.7 is a section of *Transitions* v3.0, among the forty-seven this work does not use; §784 is
  26b-08. **Nothing is unaccounted for.**
- **Every chapter pointer is in range** — the register cites chapters 1–35 and the volume runs to 36.
- **Every figure numeral the register names is live in the main volume.** Whether it names the *right*
  figure is a claim question; reg4-01 is the worked case.
- **The absent-number class reconciles with the register's own account.** 132 absent in 1–1792,
  exactly the figure L6574 states, and L6574 accounts for them as *"the thirteen never assigned,
  together with those withdrawn with their content"*. Only **two** are absent *and cited* on the
  bare-number net — 344 and 571, both from the main volume.
- **The two nets disagree, and the disagreement is the point.** `register_cites.py` reports 31
  absent-and-cited on a range-aware net that expands `registers 344–346` and the `R NNN` form; this
  sweep's bare-number net reports 2. Both are right about their own convention. That is reg1-05's
  finding stated generally: **what a sweep sees is decided by the net it uses**, which is why the
  front matter's four provenance pointers — printed as bare numbers after a script name — are in no
  absent-and-cited list at all.
- `F.3.2` and `F.3.3` are named by the register and exist in no volume. Both are **deliberate**: the
  Appendix F entry records that there was never an F.3.1 or F.3.2, and that 371, 372 and 1780 keep
  F.3.3 *because entries are append-only*.

## The one new class: unbalanced emphasis

**22 entries carry an odd number of asterisks on their headline line**, and an odd count cannot close
its own emphasis. This is the reg3-01 class (entry 313) at volume scale.

It is a **candidate list, not a verdict**, because an asterisk is also notation in this corpus — φ\*
is Miedema's electronegativity parameter (entry 26), and `(3, 0, 1, 1, *, 0, 1, 1)` is a wildcard
coordinate (entry 604). Both are correct text with an odd count. Labelled:

- **8 carry a recognisable notation token** and are very likely correct as printed — 26, 27, 604,
  747, 1642, 1643, 1646, 1681.
- **14 carry none and are candidates** — **313** (confirmed by reading, reg3-01), 1003, 1648, 1649,
  1652, 1653, 1657, 1673, 1674, 1677, 1682, 1694, 1699, 1774.

Eleven of the fourteen fall in 1642–1699, one stretch of the record. Each is handed to the unit that
reaches it; none is scored here. Docket 28 / 31.
