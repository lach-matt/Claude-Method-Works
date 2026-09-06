# Retrieval as a Lattice Problem

*A section for the book. Principle 15 formalised, with the evidence from
this work's own collection.*

---

## The principle

> **Pertaining to fetching: use the multilattice index for navigation; data
> can be retrieved in pieces.**

This is usually read as advice. It is a structural claim, and it has the same
form as the self-defence result.

---

## The formalisation

Let **C** be the set of **cells** one wants — each a tuple
(system, quantity, index, precision). Let **S** = {*S*₁, …, *S*ₖ} be a set of
**sources**, each a subset of **C**. Let **A**(*Sᵢ*) ∈ {0,1} record whether
source *i* is accessible.

> A cell *c* is **retrievable** iff ∃ *i* : *c* ∈ *Sᵢ* ∧ **A**(*Sᵢ*)

Define the **route set** of a cell:

> **R**(*c*) = { *i* : *c* ∈ *Sᵢ* } and the **retrieval redundancy**
> **ρ**(*c*) = |**R**(*c*)|

**A cell with ρ = 1 is fragile: one access failure loses it. A cell with
ρ ≥ 2 survives the loss of any single source.**

**This is exactly 𝒟_def.** There, two disjoint derivations guard a quantity
against a computational error; here, two disjoint sources guard it against an
access failure. **Same structure, different failure mode.** The book's
completeness law already contains this section's content; it needed only to be
read as a statement about libraries rather than about lattices.

---

## Four consequences, each observed

### 1. A paywall blocks a source, not a cell

The distinction is not pedantic. It determines whether one gives up.

**Worked case — antiprotonic helium.** The target cell was the single-photon
(36,34) → (35,33) frequency in p̄⁴He⁺.

| source | status | contents |
|---|---|---|
| Hori et al., *Nature* **475**, 484 (2011) | **paywalled** | 3 two-photon frequencies |
| Hori et al., *PRL* **96**, 243401 (2006) | **paywalled** | 12 single-photon frequencies |
| **arXiv:1304.4330** | **open** | the *Nature* paper entire, Table 1 |
| **arXiv:1203.5425** (CODATA 2010) | **open** | **Table XII — all fifteen, both papers** |
| **arXiv:1308.1711** (unrelated citing paper) | **open** | corroborates Korobov to 0.1 MHz |
| CERN CDS records | open | deposits |

**ρ = 6 for the target cell. Two routes blocked, four open.** The cell was
retrieved, and the two-path check on it closed at **0.09σ**.

### 2. A secondary source can be better than the primary

CODATA 2010's Table XII carries **both** papers' frequencies **with an extra
digit** the journals did not print — supplied privately to the Task Group by
the experimenters to reduce rounding error.

> **The index does not merely route around an obstruction. It sometimes finds
> a better cell than the one that was blocked.**

The blocked route would have given fewer digits and half the data.

### 3. The retrieval graph is self-referencing

Each fetched source names its successors. The Al I compilation's introduction
lists its own sister volumes verbatim — Na I–XI, Mg I–XII, Si I–XIV, P I–XV,
S I–XVI, and the Kaufman & Martin magnesium compilation. The Be I compilation
cites Sugar & Musgrove for zinc. The Al I reference list gave Sugar & Corliss
1985 for nickel and Sugar & Musgrove 1990 for copper.

**Three coverage gaps in this work's census were filled from documents already
in hand, without a single new search.** One is not searching a literature; one
is traversing a citation graph whose nodes were enumerated in advance by the
census.

### 4. The targets are enumerable before the search begins

The census computes which species could yield cells **from core configuration
alone** — 27 admitted isoelectronic sequences, 12 requiring depth, 5 excluded,
by enumerating antisymmetric states. **No spectroscopic data enters.**

So the retrieval problem is not "find whatever is out there." It is
**cover a known finite target set**, which is a different and much easier
problem. The index says what to look for; the sources say whether it exists.

---

## Where it fails, and why that matters

**Four documents in this work were not retrieved:**

| document | routes found | all blocked because |
|---|---|---|
| Edlén, *Handbuch der Physik* XXVII (1964) | 1 | print-only Springer volume |
| Ritz, *Physikalische Zeitschrift* **9**, 521 (1908) | 2 | not digitised; *Œuvres* reprint not indexed |
| Paschen & Götze (1922) | 1 | print-only |
| Dunz (1911) | 1 | print-only |

**ρ ≤ 2 for each, and every route closed.** The method did not fail through
lack of effort — nine searches, correct citations, the right platform
identified (e-rara.ch, ETH Zurich, free, in scope). **It failed because
pre-digital print has low retrieval redundancy.**

That is the honest limit, and it is a *measurement* rather than an excuse:

> **ρ(c) is a property of the literature, not of the searcher. A cell in a
> 1908 German periodical has ρ ≈ 1. A cell in a 2011 physics paper has ρ ≈ 6.**

**A century of open deposition raised ρ by roughly a factor of six**, and that
is what made the antiprotonic helium cell retrievable and the Ritz cell not.

---

## The practical procedure

1. **Enumerate the target cells from the index**, before searching. The census
   does this structurally.
2. **For each cell, list route candidates** — primary, preprint, review,
   compilation, citing paper, institutional deposit, database.
3. **Prefer high-ρ cells first.** They cost less and often carry more.
4. **Read every retrieved source for its successors.** The graph is
   self-referencing; each fetch names the next.
5. **When a route is blocked, do not re-attempt it.** Move along the route set.
6. **Record ρ for cells that fail.** A cell with ρ = 1 that is blocked is a
   *stated* gap, not an unexplained absence.

---

## Why this belongs in a book about indices

Because it is the same theorem twice.

> **𝒟_def ≥ 1** — a quantity guarded by two disjoint derivations survives a
> computational error.
> **ρ ≥ 2** — a cell guarded by two disjoint sources survives an access
> failure.

Both say that **redundancy of paths, not redundancy of quantities, is what
makes a structure robust.** The first was discovered by writing a relation down
wrongly and having the disagreement caught. The second was discovered by
hitting a paywall and finding five other doors.

**And both were already implied by closure.** A complete index holds more
routes than it needs — which is why it can lose one and continue.

---

*Retrieval redundancy ρ, worked cases, and the stated failure at ρ = 1.*
