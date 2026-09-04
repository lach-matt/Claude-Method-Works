# Rewrite — "Closure, and the seed of Λ" (source Chapter 14 §14.1–§14.5.14; prose revision, numbering left at source)

**Placement:** Part III — The Law. **First of two reader chapters split from source Chapter 14** (closure + seed; the family is open). This chapter states what closure is, credits the mathematics it rests on, and reads Λ's seed — the seven cells the whole index closes from. **Numbering left at source values** (renumber-last). Per standing treatment: every result kept and stated with the confidence branch-and-bound earned; the workshop cut — but here the workshop is subject-matter proof-of-work and is owed to the Register (tracked in OWED-REGISTER-EXPANSIONS.md, R-01..R-05), not merely filed. Proofs tokenized across all four compendia.

> **REVISION NOTE (this session):** source Ch14 splits here per M's ruling. This is part A (§14.1–§14.5.14). The family-is-open theorem (§14.6–§14.6.2) is the companion chapter. The §14.5.8 counting/coupling seed-cost result STAYS (it is subject matter): the untangle is that the surviving finding — counting axes cost the seed little, coupling axes cost more, the dichotomy read through the seed — is stated cleanly, and the withdrawn prune-greedy per-axis numbers (+1/+10, κ = S/4 − 1) are not carried into reader prose at all; they are owed to the Register as proof-of-work (R-02). Empty source headings §14.5.2–§14.5.7 (no bodies; content consolidated downstream) do not carry. Register self-citations, the prune-greedy correction narrative, the mis-citation catch, and the erasure-code false start are cut to the Register queue.

---

## Closure, and the seed of Λ

A set is closed when nothing its own structure admits is missing from it.

### 14.1 The characterisation
**Theorem 14.1.** X is closed iff X = ℛ(X), where ℛ reconstructs value sets and pairwise monotone bounds from X's own extension. The development is carried in the Mathematical Compendium [MC-42].

This is not new mathematics, and the book gains by saying so. The theorem is Bergman's double-projection theorem specialised to products of chains — a sublattice of a finite product of lattices is fixed by its two-fold projections — itself a consequence of Baker and Pixley (1975) for any algebra with a majority term, of which the lattice median is one. Λ's coordinates are counts, so each factor is a chain, and a sublattice of a product of two chains is exactly a staircase cut by monotone bounds — which is what ℛ recovers.

Two further owners belong to the same result. The property E(X) = 0 is *global consistency* of a binary constraint network, certified by Montanari (1974) — for monotone constraints, path consistency implies global consistency — and by Dechter (1992), *From local to global consistency*. And the constraint class has a name: a binary constraint that is (α, β)-monotone with α, β ∈ {≤, ≥} is a **staircase** constraint, and the connected row-convex class containing it is closed under composition, intersection and transposition (Deville, Barták and Van Hentenryck, 1999). ℛ recovers exactly a staircase, so the operator has been building a named object since Chapter 6. The provenance of these attributions — including one citation this book had to correct — is carried in the Physics and Mathematical Compendia [PC-04].

What follows is that **E(Λ) = 0 is the statement that Λ is a sublattice**, and sublattices have been binary-determined since 1975.

### 14.2 ℛ is a closure operator
ℛ is extensive, monotone and idempotent — all three axioms, exhaustively. So **E(X) = |ℛ(X)| − |X| is a closure defect**, a standard object in Galois theory, formal concept analysis and database dependency theory. The book claims no novelty for the machinery; what it offers is the application — computing the closure defect of an *index*, and finding that the periodic table's is 36 while Λ's is 0. [MC-43]

### 14.3 The scope, stated exactly
Theorem 14.1 requires each coordinate to be presented as a chain — which is not the same as requiring the factors to be chains. Any distributive factor can be so presented, by Birkhoff, as the down-sets of its join-irreducibles, one chain per irreducible. What fails is bundling: ℛ reconstructs coordinate by coordinate, so folding two chains into one non-chain coordinate hides structure from it. The theorem survives, but only when the presentation respects it. [MC-44]

### 14.5 The family of all closed sets
A closed index is one object. The closed *subsets* of a closed index are a family, and the answer to what that family is is standard once it is seen:

| ambient | cells | closed subsets | of 2ⁿ | ∩ closed | ∪ closed |
|---|---|---|---|---|---|
| 2 × 2 × 2 | 8 | 73 | 28.5% | 100% | 64.4% |
| 3 × 3 | 9 | 146 | 28.5% | 100% | 68.3% |
| 2 × 2 × 2 × 2 | 16 | 731 | 1.1% | 100% | 32.6% |

> The closed sets of ℛ form a **Moore family**: closed under intersection, containing the whole index, and not closed under union.

That is the standard fact about any closure operator, and it is worth stating because the asymmetry is ℛ's own, one level up: ℛ carries meets and refuses joins, and its family of fixed points does the same — 100% against 32–68%. A closed index is a vanishing minority inside its own power set, which is the only place from which the open indexes can be measured. The count for Λ itself is open — brute force is 2⁹⁷⁶ — but the Moore family is determined by its meet-irreducible members, and those are the route to the seed. [MC-45]

### 14.5.1 Λ is the closure of seven cells
The meet-irreducibles are the route, and taking it turns up a property of Λ that had not been looked for.

First, **no cell of Λ is removable.** ℛ(Λ ∖ {x}) = Λ for every one of the 976 cells: remove any single cell and the operator puts it back, exactly. So Λ has no closed set of the form Λ ∖ {x}, and every cell is implied by the other 975.

Second, and this is the number:

> **Λ is the closure of seven of its cells — a compression of 139 to 1, exact by branch and bound.**

The seed is a **minimum set cover**: read the envelope steps as the elements to be covered and each cell as the set of steps it witnesses, and the smallest generating set is the smallest cover. That reading is what makes seven exact rather than approximate — the quantity is a lower bound met, not a heuristic's best attempt. [MC-46]

Seven is tighter than Birkhoff's seventeen join-irreducibles, and for a stated reason: ℛ fills the envelope box where the lattice join reaches only the down-set, so the generating set is smaller than the lattice's because ℛ is the stronger operator.

**And the quantity has a name outside this book.** In a convexity space the **Carathéodory number** is the least c such that anything in the hull of a set lies in the hull of some subset of size at most c, and it equals the largest irredundant set. For a semilattice with its subsemilattices as convex sets — which is Λ's case — the Helly number is the height and the Carathéodory number is the breadth. [MC-47]

### 14.5.8 The seed is linear in dimension
On a controlled family the seed has a law. Full boxes and down-sets seed linearly in dimension — 2d, 3d, d + 3, d + 4 for the families tested — so:

> **The seed is linear in dimension and the index is not.** Compression is |X| over a linear term, which is why Λ₈ compresses 89× and Janet, at d = 2, compresses 3×.

The coefficient was already in the book's own references, glossed and left: the breadth of a product of d chains is d, and the seed cannot be constant because a generating set must reach the breadth of what it generates. So

> **seed = Carathéodory number + alphabet cost** —

the breadth, plus one witness per value no envelope step already supplies. [MC-48]

**And the seed reads the dichotomy.** Taken up the tower, the linear law holds exactly while the tower is adding counting axes and breaks when it begins adding coupling axes:

> A counting axis costs the seed little. A coupling axis costs more.

This is §12.11.3's dichotomy — counting coordinates close exactly, coupling coordinates close as envelopes — seen in a third quantity. The seed formula is a counting-axis formula, and it fails at precisely the stage where the tower stops counting and starts coupling: the same tree-or-tightness trade that costs cells and costs E also costs seed. [MC-49]

*(The specific per-axis seed costs this section once carried came from a set-cover heuristic later shown to overcount; the surviving finding is the counting/coupling asymmetry above, and the withdrawn numbers are proof-of-work in the Register.)*

### 14.5.10 A stable core, and nothing is forced
Four cells appear in every sampled minimum seed — corners, each extremal on the coordinates it fixes — and yet **no cell is forced.** Tested directly: is any envelope element covered by exactly one cell? The answer is zero, at every cap setting and at Λ₉. The four are a stable attractor of greedy covering, not a forced core; a set that nothing forces and nothing avoids. They cover 85% of the envelope elements, and the rest fall to three further cells, with the freedom concentrated on g — the coordinate carrying g ≤ min(q, 4f+2), the single non-product term and the only place the Pauli principle enters. [MC-50]

### 14.5.11 The completions are a heavy-tailed redundancy
519 triples complete the seed, drawn from 66 distinct cells, none appearing in all 519 — min 3, median 12, max 157, a thirteenfold spread. A tie is two equal options; this is 519 ways to finish one object across a gradient, so a lost free cell is recoverable and the recoverability is measurable per position. Losing one of the four corners is likewise recoverable, by rebuilding more than one position — the redundancy is real and there is no critical core, because nothing is forced. [MC-51]

### 14.5.12 What every minimum seed contains
Under randomised search over shuffled orders — a harder test than greedy — 219 distinct minimum covers appear, and the same four corners appear in every one, still without any being necessary. Six conditions hold in all 219, and this is where the real constraint lives:

| every cover contains | 219 of 219 |
|---|---|
| an s → s transition | 100% |
| an s → p transition | 100% |
| a p → s transition | 100% |
| a p → p transition | 100% |
| a null transition, q = 0 | 100% |
| a full transfer, q = k | 100% |

> **The constraint is on the channel, not on the cell.** That is why no element is uniquely covered while every cover looks alike. [MC-52]

### 14.5.13 The fifth position
Every one of the 219 covers contains a cell matching (3, 0, 1, 1, *, 0, 1, 1) — seven coordinates fixed, the target shell free — one electron in a 3s subshell holding exactly one, moving into an s subshell ending with exactly one, at doublet spin. Its function is the one thing the corners cannot do: the four corners are extremal on every coordinate they fix and none of them carries the value **one**. The corners span the extremes; the fifth cell carries the unit. Its free coordinate is a fork between exactly two elements — one witnessing the target's ceiling, one the source's — so the cell covers nine things either way and then chooses which end of the transition has its maximum witnessed. [MC-53]

### 14.5.14 And the five read as binary
Writing 1 for a coordinate at its maximum, 0 at its minimum, · for interior:

| n | l | k | q | e | f | g | 2S | | transition | |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | · | · | 1 | 1 | · | · | corner 1 | 1s² → 3p | out |
| · | 1 | 1 | 1 | 0 | 0 | 0 | 1 | corner 2 | 2p³ → 1s | in |
| · | 1 | 1 | 1 | · | 1 | 1 | 0 | corner 3 | 2p³ → 2p | across |
| 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | corner 4 | 3p¹ → 3p | still |
| 1 | 0 | 0 | · | 1 | 0 | · | · | unit 5 | 3s¹ → 3s | the unit |

Corner 1 and corner 2 are exact complements, three bits of three; corner 3 and the unit cell are exact complements, three of three; corner 4 is the only fully specified cell — 11001100 — and it is the static transition. **Every one of the eight coordinates receives both a 0 and a 1 across the five** — not one column is one-sided, which is what a covering set of envelope steps must do, made visible as a bit table.

> The seed is five words in which every letter is spoken both ways.

*Measured at one cap setting; whether the complementary pairing survives other caps is a described property of Λ₈, not yet a structural law.* [MC-54]