# Requirements Specification — Revision 2

## Restructured around ν as dimension 1

**Supersedes:** revision 1. The change is not cosmetic. Recognising ν as the
complete 1D expression collapses one whole domain from *measurement* to
*derivation*, and changes the collection ask from ~10³ level tables to ~10²
quantum-defect tables.

---

## 0. The subject, restated

**Dimension 1 is ν.** Binding energy is *T* = *Z*²*R*/ν² exactly. Both
quantities governing the method are functions of ν:

> *V* = 4ν/3 + 4/(9ν) — the cost, with *Z*, *R* and δ cancelling identically
> *r* = 2*Z*²*R*/(ν³σ) — the validity, verified to 0.88–1.04 across ν = 4.4–21

**The eight coordinates are ν's integer decomposition.** *e* gives its integer
part; *f* and the core determine δ; the rest specify the core. **The defect
function is the bridge from integers to continuum, and it is measured, never
derived.**

This restates the subject as three things, and the claim attaches to each
differently:

| | subject | claim available |
|---|---|---|
| **A** | the decomposition — Λ and its structure | **closable** |
| **B** | the bridge — δ as a function of the coordinates | **tabulable**, never closable: empirical |
| **C** | the consequences — everything that follows from ν | **closable, and derived rather than measured** |

**The title claim the specification licenses:** complete comprehension of the
decomposition and its consequences, with the bridge tabulated to the extent the
literature provides. That is a total claim over a stated subject, and it does
not collide with Theorem 12.8.

---

## 1. What changed from revision 1, and why

**Domain III has collapsed from measurement to derivation.** Revision 1 required
bracketing every channel in the literature — requirement II.7, ~10³ level
tables, the critical path. That is no longer necessary. Given ν and σ for a
channel, *V* and *r* follow in closed form. The method's behaviour on a channel
is **predicted**, not measured, and measurement is needed only to *test* the
prediction on a sample.

**The collection ask changes in kind.** A quantum-defect table is a handful of
parameters per channel — δ₀, δ₂, δ₄ and a fit range. A level table is dozens of
numbers. Where published defects exist, they replace the levels entirely.

**Four exclusions became one mechanism.** Every §10 exclusion is a failure to
determine or apply ν: Ti I (ambiguous δ from too many parents), fine structure
(a difference of two ν's, not a function of one), Sc VI (too few members to fix
δ), collapsed orbitals (δ departs from Ritz). This is now a single requirement
with four instances rather than four requirements.

---

## 2. Requirement register, revision 2

Supplier tags: `[me]` fetchable, `[you]` your input, `[calc]` no external data.

### A — the decomposition (closable)

| # | must be true | evidence | supplier |
|---|---|---|---|
| A.1 | Λ₈ closed at every cap; closure is cap-independent | exhaustive test + proof | `[calc]` |
| A.2 | order dimension exactly 8; +1 per independent quantity to Λ₁₁ | box exhibition + realiser | `[calc]` |
| A.3 | no further axis derivable; the failure is characterised | Lemmas 4.1–4.2, Theorem 4.4 on ≥8 sublattice families | `[calc]` |
| A.4 | **which decompositions of a 1D continuum preserve closure** | characterise the admissible-form space. *Sharper than rev-1's I.5: the question is now about decompositions, not arbitrary constraint forms* | `[calc]` — **unspecified, §4.1** |
| A.5 | the physical set is not a lattice; failure characterised | minimal-upper-bound census at every ℓ | `[calc]` |
| A.6 | chain structure fully described | counts, decomposition, Hansel relation | `[calc]` |
| A.7 | closure-preserving reparameterisations characterised | (g₁,G) plus uniqueness | `[calc]` — **unspecified, §4.2** |
| A.8 | **ν is not expressible in any admissible decomposition** | proof that no §9.4 bound yields *x* − *f*(*y*) | `[calc]` — **unspecified, §4.3** |

### B — the bridge (tabulable, never closable)

| # | must be true | evidence | supplier |
|---|---|---|---|
| B.1 | ground configuration and ionisation energy of every spectrum | one table, 7,021 rows | ASD *Ground States and Ionization Energies* / `[me]` if fetchable else `[you]` |
| B.2 | core LS-term count for every spectrum | computed from B.1 | `[calc]` |
| B.3 | candidate / structurally-excluded partition | computed from B.2; **already validated 13/13** | `[calc]` |
| B.4 | which spectra have measured levels at all | ASD Levels Holdings, 56 pages | `[me]` |
| B.5 | **quantum defects δ₀, δ₂, … for every published channel** | defect tables with fit ranges. **This replaces rev-1's II.7 and is the whole empirical content of the book** | **`[you]`** — **V: ~10²** |
| B.6 | series limit and its uncertainty per channel | published limits | `[you]`, bundled with B.5 |
| B.7 | typical level uncertainty per source | one figure per compilation | `[you]`, bundled |

### C — the consequences (closable, derived)

| # | must be true | evidence | supplier |
|---|---|---|---|
| C.1 | *V* = 4ν/3 for every channel, derived not measured | from B.5 | `[calc]` |
| C.2 | *r* = 2*Z*²*R*/(ν³σ) for every channel | from B.5–B.7 | `[calc]` |
| C.3 | admission verdict for every channel and every cell | from C.2 | `[calc]` |
| C.4 | **the derivation is tested against measurement on a sample** | full level tables for **~20 channels only**, spanning ν = 2–30 and *Z* = 1–6 | **`[you]`** — **V: ~20, down from ~10³** |
| C.5 | every exclusion is a failure to determine or apply ν | the four instances, each demonstrated | `[calc]` + C.4 sample |
| C.6 | **failures enumerated symmetrically with successes** | every channel that fails, with mechanism | `[calc]` |
| C.7 | the general form *V* ≈ 4\|*y*′\|/(*h*\|*y*″\|) holds outside Rydberg systems | nuclear, thermochemical, kinetic series | `[me]` for AME2020; `[you]` for the rest |

### D — what the decomposition cannot reach (closable)

| # | must be true | evidence | supplier |
|---|---|---|---|
| D.1 | σ(order) = σ(coordinates) for Λ₈…Λ₁₁ and the conserving poset | colour refinement | `[calc]` |
| D.2 | meet/join determine only H-invariant targets; those are vacuous | Theorems 12.3, 12.6 | `[calc]` |
| D.3 | comparability is reproduced by a positive-weight sum | implication + converse on ≥10 species | `[calc]` + C.4 sample |
| D.4 | counting quantities factorise | Theorem 12.7 | `[calc]` |
| D.5 | **the decomposition adds nothing to what it decomposes** | the unifying statement D.1–D.4 instantiate | `[calc]` — **new, and the book's thesis** |

---

## 3. The collection ask, revised

| supplier | rev 1 | rev 2 | change |
|---|---|---|---|
| `[you]` — level tables | ~10³ | **~20** (C.4 sample only) | **50× reduction** |
| `[you]` — defect tables | — | ~10² | new, and much smaller per item |
| `[me]` — fetches | ~60 | ~60 | unchanged |
| `[calc]` | ~25 | ~30 | more, because more is derived |

**The bottleneck has moved and shrunk.** It is no longer "bracket everything"
but "tabulate the bridge". A defect table is three or four numbers and a fit
range; a level table is dozens. And the sample needed to *test* the derivation
is ~20 channels, not the whole literature.

---

## 4. Still unspecified — all analysis, no data

**4.1 — A.4, the space of admissible decompositions.** Revision 1 asked which
constraint forms preserve closure. The ν framing sharpens it: **which integer
decompositions of a one-dimensional continuum preserve closure?** Λ is one such
decomposition. Comprehension requires knowing the class. This is now a
well-posed question with a plausibly small answer.

**4.2 — A.7, uniqueness of closure-preserving reparameterisations.**

**4.3 — A.8, the inexpressibility of ν.** Under the ν framing this is the
book's central structural claim and it is still only asserted. It needs a proof
that no admissible bound, in any number of coordinates, yields a difference.

---

## 5. Recommended sequence, revised

1. **Settle §4's three questions.** Analysis only. A.8 in particular is now
   load-bearing for the whole framing and must not remain an assertion.
2. **Close B.1–B.4.** One table, 56 fetches, then computation. Yields the
   validated candidate list.
3. **Scope B.5 against that list** — you supply defect tables only for spectra
   the census says can work. The 35% structurally excluded need nothing.
4. **Collect C.4's ~20-channel sample**, chosen to span ν and *Z*, not chosen
   for convenience.
5. **Derive C.1–C.3 and D.1–D.5.** No further data.
6. Build nothing until B.5 and C.4 are in hand.

---

## 6. One risk worth naming

**The derivation may be too good.** If *V* and *r* follow from ν in closed form,
a reader may ask what the lattice contributes at all. The honest answer is the
book's thesis and should be stated as such: **the lattice is the integer
skeleton that locates a cell in ν, and nothing more** — which is exactly what
Part III proves and what the title claim should reflect. A book that discovered
its central object to be a bookkeeping device, and said so, is stronger than
one that did not notice.
