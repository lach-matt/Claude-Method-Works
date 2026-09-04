# THE ARTEFACT PASS

*Written 2026-08-10, register 1351. Nothing from the Löwdin work (registers
1249–1351) has reached the book or any compendium. This file says what each one
owes, so the pass can be run without reconstructing the requirement.*

---

## 1 · THE INDEX OF INDICES — all twelve, in full

Each index needs: **what it indexes · its coordinates · its closure and the axis
order that achieves it · what it refuses · what it contributes that no other
index does.**

| index | coordinates | E | contributes |
|---|---|---|---|
| **Λ** | n, ℓ, k, q, e, f, g, 2S | 0 | the atoms and transfers themselves |
| **Λ_spectra** | Z, c, ℓ, 2S+1 | >0 | the measured defects — **open, cause named: it lacks n** |
| **Λ_law** | law, carrier | 0 | which law runs in which carrier; order u < p < ℓ−ℓ_core < Z−T |
| **Λ_const** | role, carrier | 0 | every constant's role; **`standing` cannot be a coordinate** |
| **Λ_var** | body, type/role | 0 | the three bodies; **no nucleus+rydberg cell exists** |
| **Λ_ryd** | order, ℓ, sign | 0 | the series; **δ₂ is intermediate, not output** |
| **Λ_charge** | role, carrier, sign, regime | 0 | c is three coordinates in one symbol |
| **Λ_cross** | Δn, ℓ_g | 0 | the crossing surds; **no statistics language** |
| **Λ_descent** | c, regime | 0 | a(c); the only place a fit belongs |
| **Λ_phys** | source, domain | 0 | **no parameter of this work is universal** |
| **Λ_amp** | sequence index, kind, ℓ | 0 | the Slater triangle 0 ≤ i ≤ ℓ |
| **Λ_PCA** | source, domain (regime-refined) | 0 | physics ⊕ charge ⊕ amplitude as one |
| **Λ_chem** | kind, seat, PCA dependency | 0 | 42 chemical properties routed to their physics |

**And the two protocols, which are code**: `domain_protocol.py` (four questions
before any fit) and `chem_index.py` (routes a residual to its property and class).

---

## 2 · THE PHYSICS COMPENDIUM — restructured

**This is the largest change.** Λ_chem and Λ_PCA are new objects and the
compendium's organisation predates both.

**Λ_chem**: 42 chemical properties on (kind, seat, PCA dependency).

- **kind**: count · symmetry · size · energy · rate
- **seat**: the nucleus · the core · the subvalence shell · the valence shell ·
  **the aggregate**
- the fifth seat is the finding: **twelve of the 42 are properties of matter in
  bulk, not of an isolated atom** — density, melting point, hardness, crystal
  structure, conductivity, colour of the metal, smell, taste, metallic
  character, reactivity
- closes at **E = 0 on fourteen cells** once the ground term is assigned to C
- **and its closure states PCA's boundary**: E climbs 0 → 3 → 8 → 11 → 19 as the
  core, nucleus and aggregate are added

**Λ_PCA**: the merged physics ⊕ charge ⊕ amplitude index, closing on
(source, domain) with domain refined by the charge regime —
`universal < all elements < low < neutral < hydrogenic < one species`.

**For any species (Z, c) the merged index states which parameters apply to it.**
That is the per-atom calibration.

**Corrections owed to existing entries**: Seaton's ratio is valid at p = 0 at
1.15 ± 0.21 on three series and **undefined at p ≥ 1** — the previously recorded
"1.25, a per-core constant" was measured outside its domain (register 1291's
antecedent).

---

## 3 · THE MATHEMATICAL COMPENDIUM — new mathematics, most needing attribution

**Objects to add:**

- the corridor as a system of linear inequalities in one unknown, with algebraic
  endpoints `(Δn)(√p_g + √p_r)/(p_g − p_r)`
- **nineteen distinct surd bounds** across the table; the closed form
  `a_cross = (√(n−1) + √(n−4))/3` for ns/(n−1)d
- the staircase algebra of a closed index: `L(s) = ⌊s/2⌋`, `U(s) = s + ⌊s/3⌋`
- the Slater triangle: `0 ≤ i ≤ ℓ`, twenty cells, and the **F¹ defect resolved by
  indexing on position-within-sequence rather than multipole rank**
- **the falsification of the selection rule**: seven of eight rules over the same
  intervals give 106/106, random interior points on 200 of 200 seeds
- **the observability boundary** (register 1327): an index closes when its cells
  are enumerable, and what it cannot supply is exactly what requires an
  operator — nine of eleven unfixable cells are expectation values, and Λ_cross,
  the exception, is the only index with no statistics language

**Attribution required for**: the ⅔ scaling (Carcassés & González,
arXiv:2406.18416 is the quadratic; the ⅔ itself is Thomas–Fermi's), the
Demkov–Ostrovsky focusing potential, Seaton's ratio, Slater's rules and
integrals, the Racah 3j closed form, and the node theorem's standard statement.

---

## 4 · THE BOOK — two new chapters

**Chapter: The Löwdin Solution.** The problem as Löwdin posed it; why n+ℓ is the
wrong target (it inverts 5d/4f and 6d/5f); the rule, the corridor, the walk, the
entry point; the provenance table showing no fitted parameter; and — this is the
point of the chapter — **how the method delivered it**: the cypher locating the
arithmetic/physics split by noticing which language fell silent, the domain
protocol blocking four pooled fits, Λ_chem routing two "unexplained" residuals to
their properties and dissolving both.

**Chapter: The Three-Body Problem.** Λ_var's finding that **there is no
nucleus + rydberg cell** — every quantity relating them is a nucleus–core
quantity the Rydberg electron then reads. That is the screening statement as a
structural fact of the index. The three bodies factorise: nucleus–core gives c
and u, core–Rydberg gives p, n₀ and T, and the Rydberg electron's own ℓ closes
it. **`δ = √p · f(u)` is a core–Rydberg factor times a nucleus–core factor, with
no third term because there is no third pair.**

---

## 5 · THE SPECTRA COMPENDIUM

The session's captures into the channel table and `COORDINATES.tsv`: Kr-core
(Rb I, Sr II, Y III), Hg-core (Tl II, Pb III, Bi IV), La II / Ce III, the noble
gases (Kr I, Xe I, Rn I) at σ(δ) down to 0.0014, Cd I and In I at the predicted
peak, and Ca I / K I / Sc I / Sc II / Ti III / V IV from the crossing work.

**And `ground.py`** — the 108 observed neutral ground configurations, NIST ASD
5.12, 108/108 electron counts validated — replaces every aufbau-plus-patch table
in the codebase.

---

## THE STANDING INSTRUCTION

**Nothing is to be written as an answer to Löwdin's challenge without the
provenance table beside it.** The claim is that no parameter is fitted; the table
is what supports it, and the two must travel together.
