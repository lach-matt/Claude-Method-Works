# DIGEST — what a session needs to hold before it works
Written 2026-08-15 (session 1.8), after a bounded read of the book and the four compendia.
This is an orientation file, not a substitute for any of them. It records what was read,
what was not, and the load-bearing facts a fresh session must not have to rediscover.

## The one claim
A **closed** index — closed under the meet and join of its own coordinates — cannot help
containing its own definition, cannot help containing its own contradiction, and determines
exactly what may be added to it. `E(X) = |ℛ(X)| − |X| = 0` is the closure test;
`|∏ᵢ Aᵢ| = |X| + E(X) + refused` is the partition identity.
Closure gives **six things and no others**: alphabet, bounds, totality of the membership
test, which cells may be added, which axes adjoined, which constraints imposed.
Three further mechanisms exist and none follows from closure: order recovered only across a
tree, a wrong value only from outside, a wrong derivation only along a second route.
**Closure never gives reference** — that the coordinates refer to anything.
An index that is not a fixed point is **not defective**: where a certificate exhibits an
operation reaching a fixed point, E measures the *drawing*; where none exists, E measures the
*world*. Openness is a measurement; closure is the case where it is zero.

## The objects
- **Λ** — 976 cells, eight coordinates (n, ℓ, k, q, e, f, g, 2S), seven bounds. A cell is a
  **transition, not a state**. E(Λ) = 0. E(periodic table) = 36 — the whole argument.
- **Λ_spectra** — and **the name covers two different objects**, which is a live defect:
  - in `SPECTRA.md` and `COORDINATES.tsv`: four coordinates (Z, charge, ℓ, 2S+1),
    **104,832 cells** at the Z=120 bound, E = 0.
  - in `INDICES.md`: three coordinates (Z, core charge, ℓ), **1,664 cells**, E = 1,351,
    holding 596 channels across 313 cells.
  The second is the *measured channel survey*; the first is the *coordinate index*. They are
  not the same lattice and both are called Λ_spectra. See R 1657.
- **Λ_phys, Λ_chem, Λ_PCA, Λ_xray** — in the Physics Compendium and INDICES.

## The shape of Λ_spectra, as computed (R 1651–1656)
Two rules generate it and nothing else:
1. **charge ≤ Z** — the triangle. At Z=120: 7,260 pairs = 120·121/2.
2. **mult = f(N)**, N = Z − charge + 1 — the isoelectronic count. Exact, zero exceptions.
   The 19 N whose fibre is a **singleton** are precisely the aufbau first-in-subshell counts
   [1,3,5,11,13,19,21,31,37,39,49,55,57,71,81,87,89,103,113]. The Madelung sequence is already
   inside the index, as a fibration rather than a coordinate.
ℓ runs 0–7 in full on every pair. Product 1,036,800 − 104,832 present = 931,968 refused by rule.
**E = 0 at any cutoff**, because both rules are total — so the Z bound is a declaration about
the world, not a property of the index. Z = 119, 120 are carried with the bound
"no nuclide synthesised; theoretically admitted — Janet left-step".

## The law that governs changes: A.cert
Four admitted operations and no fifth: **RELABEL · RE-COORDINATISE · REFINE A FIBRATION ·
DROP A COORDINATE**. *Add-a-coordinate is not admitted* — four attempts, four failures
(R 1581, 1599, 1602, 1608). A fibration must be decidable from **that coordinate alone**.

## The principles that bite most often
- **P5** compute the result before assuming it. **§2.14** compute, then write — *the most
  violated protocol in the book*, and the fault recurred four times in session 1.8 alone.
- **P8/§2.15** every failure is a true answer and therefore a bound; record what it excludes.
- **P22** a complete index converts deception into disagreement: error survives, concealment
  does not. **P23** completeness is a standing claim, held until a question arrives.
- **§2.8** two independent routes — an identity computed along one path is vacuous.
- **§2.9** refuse rather than coerce; no silent default. **§2.20** the Zeno directive: nothing
  runs unbounded; fetched literature is the single exception.

## The gates
`The_Method_1_6_audits.py` — 25 prime audits: LATTICE · EQUATIONS · CONSISTENCY · REDUNDANCY ·
ARTEFACT · COHERENCE · ATTRIBUTION · CELL · DISTINCTNESS · SCOPE · ANTECEDENT · MARKUP ·
AGREEMENT · ARITHMETIC · ENUMERATION · FIDELITY · MEASURE · REPRODUCTION · SEQUENCE ·
PROJECTION · INPUT · CENSUS · GRAPH · CYCLE · NOMENCLATURE.
`roundtrip.py` — 5 generated artefacts must regenerate identically: COMPENDIUM, INDICES,
PHYSICS, SPECTRA, REGISTER. **A write to COORDINATES.tsv is not complete until every artefact
generated from it has been regenerated** (learned R 1655).

## What was read, and what was not
READ IN FULL: the book's front matter and note from the collaborator; Part 0 (preface);
Part I §1 (principles P1–P23) and §2 (protocols 2.1–2.20); the audit names; each compendium's
declaration and full heading structure; INDICES §"The spectra index"; SPECTRA §0 and §I.
NOT READ: the book's Parts II–VII and appendices (~95,000 words) and the bodies of the four
compendia (~80,000 words). Those remain to be read in bounded passes.