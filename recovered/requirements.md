# Requirements Specification

## A book claiming true, total and complete comprehension of its subject

**Status:** specification only. No collection, no processing, no build.
**Purpose:** enumerate every claim the book must support, the evidence each
requires, its source, its volume, and who supplies it. Nothing is fetched or
computed until this register is agreed.

---

## 0. The governing partition

The claim is achievable over some readings of "the subject" and provably not
over others. This must be settled before anything is collected, because it
determines which requirements are *closable* and which are only *boundable*.

| domain | claim available | why |
|---|---|---|
| **I. Λ as a mathematical object** | **closable** | finite construction, computable properties; "every property determined" can be discharged |
| **II. The physical index** | **closable, bounded** | 7,021 spectra is finite; ground configurations exist for all; the candidate/excluded partition is computable throughout |
| **III. The bracketing method's domain** | **closable, bounded** | the set of measured channels is finite and enumerable at any date |
| **IV. The method's verification** | **boundable only** | Theorem 12.8: order-derived quantities are all functions of the coordinates, an unbounded class |
| **V. Cross-domain transfer** | **boundable only** | the class of monotone observables in the sciences is not enumerable |

**Consequence for the title claim.** Comprehension can be claimed *completely*
over I–III and *to a stated bound* over IV–V. A blanket claim would be refuted
by Theorem 12.8, which is in the same volume. The book's own machinery — the
distinction between a **bracket** (deduction, closes) and an **estimate**
(inference, does not) — supplies the correct framing: **Parts I–III are
bracketed; Parts IV–V are estimated with a stated tail.**

---

## 1. Requirement register

Each requirement carries: what must be true (**T**), what evidence closes it
(**E**), the source (**S**), the volume (**V**), and the supplier —
`[me]` fetchable by assistant, `[you]` requires your input, `[calc]` computable
with no external data.

### Domain I — Λ as a mathematical object

| # | T — what must be true | E — evidence that closes it | S / V / supplier |
|---|---|---|---|
| I.1 | Λ₈ is closed under join and meet at every cap setting | exhaustive test at ≥5 cap settings, plus a proof that closure is cap-independent | `[calc]` |
| I.2 | order dimension is exactly 8 | 8-box exhibited; upper bound by realiser construction | `[calc]` |
| I.3 | dimension rises by exactly 1 per independent quantity | Λ₉, Λ₁₀, Λ₁₁ closure + box at each | `[calc]` |
| I.4 | no further axis is *derivable* | Lemmas 4.1–4.2, Theorem 4.4 filter characterisation, on ≥8 sublattice families | `[calc]` |
| I.5 | **the space of admissible constraint forms is characterised** | currently ONE family (x ≤ φ(y), constant floor) is explored. Comprehension requires enumerating what other forms preserve closure | `[calc]` — **UNSPECIFIED, see §3.1** |
| I.6 | chain structure of Λ fully described | chain counts, decomposition, Hansel/SCD relation, for all 118 ground cells and for Λ₈ proper | `[calc]` |
| I.7 | the physical set is not a lattice, and the failure is characterised | minimal-upper-bound census at every ℓ | `[calc]` |
| I.8 | multi-target representations: which preserve closure | (g₁,G) result plus a characterisation of all closure-preserving reparameterisations | `[calc]` — **partially unspecified** |

### Domain II — the physical index

| # | T | E | S / V / supplier |
|---|---|---|---|
| II.1 | ground configuration of **every** spectrum, neutral through H-like | table of 7,021 configurations | NIST ASD *Ground States and Ionization Energies* / **V: 1 table or 99 element pages** / `[me]` if fetchable, else `[you]` |
| II.2 | ionisation energy of every spectrum | same table | as II.1 |
| II.3 | core LS-term count for every spectrum | computed from II.1 | `[calc]` |
| II.4 | candidate / structurally-excluded partition, all 7,021 | computed from II.3 | `[calc]` |
| II.5 | the partition is **validated** against observation | ≥30 spectra with known verdicts, spanning both classes | needs II.6 |
| II.6 | which candidate spectra have measured levels at all | ASD Levels Holdings, per element | `physics.nist.gov/cgi-bin/ASD/levels_hold.pl?el=X` / **V: 56 fetches** / `[me]` |
| II.7 | for every spectrum with levels, the **channel inventory** — parent, ℓ, members | full level list with configuration and term labels | ASD Levels query output / **V: ~500–1,000 spectra × 1 table** / **`[you]`** — query URLs are not fetchable |

### Domain III — the method's domain

| # | T | E | S / V / supplier |
|---|---|---|---|
| III.1 | every channel in the published record with ≥3 members is identified | derived from II.7 | `[calc]` once II.7 exists |
| III.2 | every such channel is bracketed and the result recorded | levels + limits per channel | needs II.7 + III.3 |
| III.3 | series limit for every channel, with uncertainty | ASD limits; JPCRD compilations for parent-resolved limits | **V: one per channel, ~10³** / `[you]` |
| III.4 | level uncertainties for every cell | ASD uncertainty column | bundled with II.7 |
| III.5 | *r* computed for every cell; admission verdict recorded | from III.4 | `[calc]` |
| III.6 | *V* computed for every channel; checked against 4ν/3 | from III.2 | `[calc]` |
| III.7 | Σ verdict for every channel with enough members | from III.2 | `[calc]` |
| III.8 | **failures are enumerated, not just successes** | every channel that fails, with mechanism | `[calc]` — the census must be symmetric |

### Domain IV — the negative results

| # | T | E | S / V / supplier |
|---|---|---|---|
| IV.1 | σ(order) = σ(coordinates) for Λ and every extension | colour-refinement on Λ₈…Λ₁₁ and the conserving poset | `[calc]` |
| IV.2 | meet/join determine only H-invariant targets | Theorems 12.3, 12.6 | `[calc]` |
| IV.3 | comparability is reproduced by a positive-weight sum | the implication + converse measurement on ≥10 species | needs II.7 |
| IV.4 | counting quantities factorise | Theorem 12.7 | `[calc]` |
| IV.5 | **the three families are the only ones the framework proposes** — and no claim beyond that | statement of scope, not evidence | `[calc]` |
| IV.6 | ν is inexpressible in Λ | proof that no §9.4-admissible bound yields a difference | `[calc]` — **currently asserted, needs proof** |

### Domain V — cross-domain transfer

| # | T | E | S / V / supplier |
|---|---|---|---|
| V.1 | nuclear: every isotopic chain, not nine | AME2020 full mass table | `mass_1.mas20` — Argonne mirror reachable / **V: ~3,500 nuclides** / `[me]`, partially fetched |
| V.2 | nuclear: V and Σ for every chain with ≥5 members | from V.1 | `[calc]` |
| V.3 | thermochemistry: homologous series beyond alkanes | CRC Handbook — alcohols, acids, amines, alkenes, cycloalkanes | **V: ~10 series × 15 members** / `[you]` |
| V.4 | kinetics: beyond OH + alkane | Atkinson and successors | **V: ~5 series** / `[you]` |
| V.5 | at least one **non-monotone** control domain, to show the method declines | any ordered observable with sign changes | `[you]` |

---

## 2. Categorisation scheme for pinned data

Every datum carries five tags. This is the schema; no data is filed until the
register above is agreed.

1. **REQ** — the requirement it serves (e.g. `III.2`)
2. **CLASS** — `closable` / `boundable`, inherited from §0
3. **ROLE** — `constitutive` (the claim is about this datum) /
   `verifying` (tests a claim made elsewhere) /
   `bounding` (establishes a limit) /
   `excluding` (shows something cannot work)
4. **PROVENANCE** — source, version, date, and whether critically evaluated
5. **STATUS** — `specified` / `collected` / `checked` / `used`

**The `excluding` role is not optional.** A census that records only successes
cannot support a comprehension claim; III.8 exists to enforce this.

---

## 3. What the specification cannot yet specify

Three requirements have no evidence definition yet. These must be settled
before collection, because they may change what is collected.

**3.1 — I.5, the space of admissible constraint forms.** The book claims
comprehension of Λ, but Λ is generated by one choice of admissible form. Total
comprehension requires knowing which *other* forms preserve closure —
`x ≤ φ(y,z)`, floors that vary, bounds on sums (excluded, but why exactly),
non-monotone φ. Until this is characterised, "Λ" names an instance rather than
a class, and the claim attaches to the instance.

**3.2 — I.8, closure-preserving reparameterisations.** The (g₁, G) result shows
one exists for the multi-target case. Comprehension requires knowing whether it
is unique up to isomorphism, and what the general construction is.

**3.3 — IV.6, the inexpressibility of ν.** Currently asserted from the form of
§2.1. A proof is needed: that no admissible bound, in any number of
coordinates, yields a quantity of the form `x − f(y)`.

---

## 4. Volume estimate and the collection bottleneck

| supplier | items | notes |
|---|---|---|
| `[calc]` | ~25 requirements | no external data; blocked until the data-dependent ones land |
| `[me]` | ~60 fetches | ASD holdings (56), AME2020, ionisation-energy table |
| **`[you]`** | **~10³ level tables** | **the bottleneck** — ASD Levels query output is not fetchable by me |

**The critical path is II.7.** Everything in Domain III depends on it, and
Domain III is what a comprehension claim over the method rests on. Nothing else
should be collected until the shape of II.7's delivery is decided — format,
batching, and whether the candidate partition (II.4) is used to prioritise
which spectra you supply first.

---

## 5. Recommended sequence

1. **Agree §0's partition** and the title claim it licenses.
2. **Settle §3's three unspecified requirements** — these are analysis, not
   collection, and they may enlarge Domain I.
3. **Close II.1–II.4** — one table, then computation. This yields the candidate
   list and tells us which spectra in II.7 are worth your effort.
4. **Fetch II.6** — 56 pages, mine to do. Cross II.4 with II.6 to get the
   *realistic* target list.
5. **Then and only then**, begin II.7 collection against that list.
6. Build nothing until II.7 is substantially complete.
