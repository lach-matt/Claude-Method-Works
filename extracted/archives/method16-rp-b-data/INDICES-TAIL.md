# IX · THE INDEXES BUILT IN THE LÖWDIN WORK

*Registers 1249–1429. **Fifteen indexes: fourteen closed — Λ_ladder now among them
— and Λ_spectra closing at the limit with eleven named cells.** Each is stated the same way:
what it indexes, its coordinates, the axis order that closes it, what it refuses,
and the one thing it contributes.*

---

## Λ_law — the laws of the channel equation

**What it is.** Seven laws on (law, carrier). **E = 0** at carrier order
**u < p < ℓ−ℓ_core < Z−T**, and 288 of 120,960 orderings reach it.

**What only it contributes.** *The carrier.* The order is monotone in how LOCAL
the variable is — u is the whole atom, p counts one ℓ's shells, ℓ−ℓ_core compares
two angular momenta, Z−T is one distance to one threshold. **The index says which
law runs in which variable, and fitting a law in the wrong carrier is what took
the ℓ-spread from a spurious r² 0.868 to a real 0.356.**

## Λ_const — the constants

**What it is.** Fourteen constants on (role, carrier), role order
**exponent < centre < width < scale**. **E = 0** at 2 of 576 orderings.

**What only it contributes.** *That `standing` cannot be a coordinate.* With
attributed/derived/measured/fitted on an axis the index cannot close at any
ordering; without it, it closes at once. **An index whose coordinates mix the
object with the observer cannot close, because the observer's axis has no order
the object respects.** The same fault recurs as `origin` in Λ_var, `kind` in
Λ_phys and `state` in Λ_ladder.

**And the role axis orders by how much physics a number has absorbed.** Every
CENTRE in the system is a small integer or half-integer — 2, 2, 2.5, −1.5, 5.4 —
and no SCALE is.

## Λ_var — the variables

**What it is.** Twelve variables on (body, role), body order
**nucleus < core < core+rydberg < nucleus+core < rydberg**. **E = 0.**

**What only it contributes.** *That there is no nucleus + rydberg cell.* Not one
variable relates them directly: every quantity connecting the Rydberg electron to
the nucleus — c, u — is a nucleus–core quantity that the Rydberg electron then
reads. **That is the screening statement appearing as a structural fact of the
index rather than a modelling choice, and it is the three-body factorisation:
nucleus–core gives c and u, core–Rydberg gives p, n₀ and T, and the Rydberg
electron's own ℓ closes it.**

**And the singleton rule.** Λ_var passes ℛ with both δ and n\* present, because
both land in the same cell — **only a second criterion sees it. An index is closed
when its output class is a singleton; two outputs mean the observer is still
choosing which to read.**

## Λ_ryd — the Rydberg series

**What it is.** Five cells on (Ritz order, ℓ, sign). **E = 0** once δ₂ is
reclassified as INTERMEDIATE — it is fitted from the series, never measured.

**What only it contributes.** *The n-dependence Λ_spectra discards.* A channel's
δ is not one number but a convergent sequence — Cd I's ns series gives 3.7171,
3.6835, 3.6719, 3.6665, 3.6637, 3.6621, 3.6610. **Λ_spectra holds δ₀; Λ_ryd holds
δ₂ and δ₄.**

**And the sign of δ₂ is penetration, not ℓ**: 0 of 3 positive at p = 0, 2 of 2 at
p = 5. **Seaton's ratio is valid where p = 0 at 1.15 ± 0.21 and UNDEFINED where
p ≥ 1** — a domain, not a failure.

## Λ_charge — the roles of the charge

**What it is.** Nine occurrences on (role, carrier, sign, regime), nine distinct
cells, **E = 0**, and dropping any single role also gives 0.

**What only it contributes.** *That c is three coordinates in one symbol.* The
charge appears inside u = ln(Nₑ/c^(2/3)), as the base of c^(−x), and inside the
exponent x itself. **Every degeneracy of the session was between a charge term and
something else, and this index says why: one symbol occupying three positions,
and any fit letting two of them float will trade them.**

**A warning the index also carries**: declaring the three roles as coordinates in
Λ_spectra raises E from 1929 to 13,605. **A closed sub-index says its roles are
well-posed; it says nothing about whether the parent index wants them.**

## Λ_cross — the crossing values

**What it is.** The value at which an ordering flips,
**a_cross = Δn(√p_g + √p_r)/(p_g − p_r)** — nineteen distinct surds across the
table, including 1/√3, 1/√2, 1, 1/(√3−1), 1+1/√2 and 1/(√2−1). **E = 0** on
(Δn, ℓ_g).

**What only it contributes.** *An index with no statistics language.* Order,
algebra (closed in ℚ(√p) for p ≤ 7) and geometry all speak of it; **analysis and
statistics do not.** A quantity that is ordinal, algebraic and geometric but not
analytic is an INTEGER OBJECT: it cannot be fitted and needs no fitting.

**And it is the one index whose unfixable cell is fixed anyway** — a node count
needs no measurement. **Nine of eleven unfixable cells across the work are
expectation values ⟨Ψ|Ô|Ψ⟩; Λ_cross is the exception, and it is the only index
with no statistics language. The two facts are the same fact.**

## Λ_descent — the charge dependence

**What it is.** a(c) on (c, regime). **E = 0.**

**What only it contributes.** *The only place a fit belongs.* Order and analysis
both speak of it, information says c adds everything, and statistics answers yes.
**Every fit of the session was applied to the WHOLE of a — the crossing and the
descent together — and that is why the constants kept absorbing each other: half
the object has no analysis language, and the fitted parameters were competing to
represent a set of surds.**

## Λ_phys — the parameters, rebuilt

**What it is.** Twenty-one parameters of real atoms on (source, domain),
**E = 0**, at source order **standard < mathematics < literature < this work** and
domain order **universal < all elements < a region < one species**.

**What only it contributes.** *That no parameter of this work is universal.* The
closing grid is a staircase and the diagonal is the whole content: CODATA
constants are universal, this work's numbers hold on a region or all elements and
never universally. **A pooled fit across regions asserts a universal parameter,
which the closed index says does not exist — that is a structural prohibition,
not a stylistic preference, and it is what `domain_protocol.py` enforces.**

**Rebuilt on three rulings**: `kind` is the same axis as `source`; `arity` is a
property of the book, not the parameter; and parameters that are artefacts of the
METHOD are not physics of real atoms.

## Λ_amp — the electron–electron term

**What it is.** The Slater integrals: for each subshell pair, F^k for k even up to
2min(ℓ,ℓ′) and G^k for k ≡ ℓ+ℓ′ (mod 2) from |ℓ−ℓ′| to ℓ+ℓ′. **Twenty cells,
E = 0**, a perfect triangle **0 ≤ i ≤ ℓ**.

**What only it contributes.** *That the rank is not a free coordinate.* Indexed on
the multipole rank k the index gives E = 1 and the single defect is **F¹ — a term
parity forbids.** Reindexed on POSITION WITHIN SEQUENCE it closes. **The same
fault as `breadth` in Λ_chem: an axis whose values are constrained by another
axis.**

**And its structure explains the Slater result exactly**: at s/s the exchange G⁰
IS the direct F⁰, so dropping exchange costs nothing; at f/f it discards four
independent quantities. **The count of lost integrals is the count of failures —
5 of 5 s-block brackets threaded, 0 of 1 f.**

## Λ_PCA — physics ⊕ charge ⊕ amplitude, merged

**What it is.** Nine cells on (source, domain) with the domain refined by the
charge regime: **universal < all elements < low < neutral < hydrogenic < one
species**. **E = 0.**

**What only it contributes.** *The per-atom calibration.* A parameter's domain
reads as a SET OF ATOMS, so for any (Z, c) the index states which parameters
apply to it. **And the closing order puts `low` — charge 2 — BEFORE the neutral,
which the ladders independently confirm: c = 2 is the only charge with two-sided
brackets, the narrowest domain and therefore the most particular.**

**A correction recorded here**: merging Λ_phys and Λ_charge on identified axis
NAMES raised E from 6 to 11 and I concluded they were not one object. That was
against a malformed Λ_phys. **Merged on `domain ≡ regime` alone, after the
rebuild, they close.**

## Λ_chem — the chemical properties

**What it is.** Forty-two chemical properties of a species on (kind, seat, PCA
dependency). **E = 0 on fourteen cells** over the subvalence and valence shells.

- **kind**: count · symmetry · size · energy · rate
- **seat**: the nucleus · the core · the subvalence shell · the valence shell ·
  **the aggregate**
- **PCA**: which of physics, charge or amplitude the property supplies

**What only it contributes.** *That twelve of the forty-two are properties of
MATTER IN BULK and not of an isolated atom* — density, melting point, hardness,
crystal structure, conductivity, colour of the metal, smell, taste, metallic
character, reactivity. **With eleven hand-picked properties the index could not
say this; it appeared the moment every property was demanded.**

**And its closure states PCA's own boundary.** E climbs **0 → 3 → 8 → 11 → 19** as
the core, the nucleus and the aggregate are added. **PCA's domain is the
subvalence and valence shells, and the index declares it by degrading
monotonically outside it** — as Seaton's ratio is valid at p = 0 and undefined
beyond.

**The last defect cell, found by exhaustive reordering.** All 1,440 orderings give
minimum E = 1 and none reaches zero: the cell is **symmetry × the valence shell ×
a charge role**. The fill is the ground TERM, which changes with charge —
Nₑ = 20 gives ¹S₀ → ³D₁ → ³F₂ → ³F₂ and Nₑ = 38 the identical sequence.
**Every ladder table carried the term symbol; the configurations were recorded and
the terms were not.**

## Λ_t — the corridor position

**What it is.** Twelve cells on (ℓ, n) holding **t = (a − L)/(U − L)**, where a
sits in its corridor. **E = 3.**

| ℓ \ n | 2 | 3 | 4 | 5 | 6 | 7 | limit |
|---|---|---|---|---|---|---|---|
| **s** | 0.268 | 0.335 | 0.266 | 0.218 | 0.257 | 0.195 | — |
| **p** | · | 1.120 | 1.049 | 1.022 | 1.002 | · | **1.0000** |
| **d** | · | · | 1.819 | 1.433 | · | · | **1.7321** |

**What only it contributes.** *That the ℓ axis carries the LIMIT and the n axis
the APPROACH.* t converges to √(ℓ(ℓ+1)/2), the centrifugal term — 6p sits 0.2%
above it — and the gap falls **0.120 → 0.049 → 0.022 → 0.002** along n.

**And q is not a coordinate.** With the Pauli fraction in the radicand, t barely
moves across a subshell: 6p gives 1.0237, 1.0417, 1.0009, 1.0036, 0.9946, 0.9940
across all six occupancies.

**Its three defect cells are 7p, 6d and 7d** — real absences, each a subshell
whose corridor is one-sided or whose ionisation energy is not held.

## Λ_ladder — the ladders themselves

**What it is.** The walks, on (seat, kind, Zcross). **FOURTEEN ladders in three
families — six species, six state, two X-ray — nine cells, E = 0. IT CLOSES.**
Registers 1356, 1374, 1375, 1384, 1427.

Two relations, three ladders each — **Z = Nₑ + c − 1** on Λ, and **A = Z + N** on
the nuclide chart. Only two of three are independent either side, so no ladder
varies Z alone: forbidden by arithmetic, not by lack of data.

| family | ladder | fixes | reaches | held |
|---|---|---|---|---|
| species | isoelectronic | Nₑ | valence | 11 of 11 |
| species | the walk | c | valence | 106 of 106 |
| species | ionisation | Z | subvalence | 15 of 108 |
| species | isotopic | Z, Nₑ, c | nucleus | **1 rung traced** |
| species | isotonic | N | nucleus | none — NEW |
| species | isobaric | A | nucleus | none — NEW |
| state | the Rydberg series | the species | valence | every δ held |
| state | the ℓ-ladder | species, n | valence | 62 pairs |
| state | the term ladder | species, cfg | valence | 66 pairs |
| state | the outer-j ladder | species, cfg | valence | P.jsplit |
| state | the parent-term | the species | core | 12 of 15 |
| state | the isomeric | Z, N, e⁻ | nucleus | none — NEW |

**What only it contributes.** *That a coordinate individuating the cells is a KEY,
not an axis.* At four ladders `fixes` was injective by construction — a ladder IS
named by what it holds fixed — so one cell per row, and **E = 0 was FORCED: 2% of
admissible arrangements could refuse.** At six, ionisation and isotopic both fix
Z, and the zero becomes earnable. That is the dual of A.define, where a
single-valued coordinate contributes no envelope; this is the other end of the
same degeneracy.

**IT CLOSES, and both blocking reasons are resolved.** The E = 1 defect stood at
**(subvalence, counting, across elements)** — Moseley's ladder, in a direction
ionisation does not go. That defect is what demanded Λ_xray, and Λ_xray filled it:
Moseley enters at subvalence as counting/across, the Kα doublet as coupling/within.
**Only the subvalence seat closes** — nucleus gives 1, core 2, valence 1 — and the
seat is settled from OUTSIDE the closure rather than by it, since Λ_PCA excluded
the core independently, on different coordinates, before this was computed. The
physics agrees: a Kα line is not a property of the 1s shell but a transition
*between* shells, so the seat is where the transition spans, not where the hole
sits. **Contingency: 90% of comparable nine-cell sets refuse, so the zero is
earned** (R 1427).

**And the five shared cells are four findings and one separation** (R 1428). Two
pairs are ONE OBJECT and the index is right to merge them — isotonic fixes N and
isobaric fixes A with A = Z + N; isoelectronic fixes Nₑ and the walk fixes c with
Z = Nₑ + c − 1. That is *charge is one symbol in three positions*, one level up.
Two are separated by axes already in the index but not among the three that close:
isotopic is species where the isomeric is state; the Rydberg series fixes the
species where the ℓ-ladder fixes species and n. **The fifth was the real
ambiguity** — the term ladder and the outer-j ladder — and they are five tower
stages apart, nested rather than parallel: the term ladder moves 2S, Λ₈'s own
letter, while the outer-j ladder moves 2J, which arrives only at Λ₁₃. Adding the
tower stage as a fourth axis separates that pair and only that pair, but costs
closure, E going 0 → 1. **So the stage is the discriminator, not an axis** (R 1429).

## Λ_xray — the inner shell

**What it is.** The dipole-allowed inner-shell transitions, on
(Δn, Δℓ, jtype_hole). **33 lines through the N shell → 9 cells, E = 0.**
Register 1378.

**Where it comes from.** Built with no new data. **Λ's cell IS a transition** —
source subshell into target subshell — and its constraints impose no order between
n and e, so a downward transition was already inside its alphabet; only the caps
excluded it. EM.map gives the dipole rule, T.a12 the j triangle. The six K-shell
lines emerge as the classical set unadjusted: K-L2 and K-L3 are Kα₂ and Kα₁,
K-M2 and K-M3 are Kβ₃ and Kβ₁, K-N2 and K-N3 are Kβ₂. Energies are NIST SRD 128,
Deslattes *et al.*, *Rev. Mod. Phys.* **75** (2003) 35–99.

**What only it contributes.** *That thirty-three named lines are nine transition
types.* Seventy-two of 165 three-coordinate systems reach E = 0 and **every one
collapses to exactly nine cells** — Kα, Lα and Mα are one type read at three
depths, which Siegbahn notation hides.

**And it settles what Λ_cross's silences mean.** The two close on the same shape —
differences plus one endpoint — and the cypher separates them:

| language | Λ_cross | Λ_xray |
|---|---|---|
| order | speaks | speaks, E = 0 |
| geometry | speaks | speaks |
| statistics | **silent** | **speaks** — pairwise marginals recover all 9 |
| analysis | **silent** | **speaks** — Moseley, R² = 0.998 |

*Λ_cross remains the only integer object: cells AND values fixed by arithmetic.
Λ_xray has integer cells and measured values.* Registers 1379, 1380, 1385.

## The one-line summary, extended

| index | the one thing only it gives |
|---|---|
| **Λ_law** | the carrier — which variable a law runs in |
| **Λ_const** | that `standing` cannot be a coordinate |
| **Λ_var** | no nucleus + rydberg cell — the three-body factorisation |
| **Λ_ryd** | the n-dependence Λ_spectra discards |
| **Λ_charge** | c is three coordinates in one symbol |
| **Λ_cross** | an index with no statistics language |
| **Λ_descent** | the only place a fit belongs |
| **Λ_phys** | no parameter of this work is universal |
| **Λ_amp** | the rank is not a free coordinate |
| **Λ_PCA** | the per-atom calibration |
| **Λ_chem** | twelve of forty-two properties are not an atom's at all |
| **Λ_t** | ℓ carries the limit, n carries the approach |
| **Λ_ladder** | that a coordinate individuating the cells is a key, not an axis |
| **Λ_xray** | thirty-three named lines are nine transition types |

**Fourteen close.** Λ_xray is new and closes at nine transition types. **Λ_ladder
now closes too** — fourteen ladders, nine cells, E = 0, once the X-ray pair is
seated at subvalence (R 1427), its five shared cells resolving as four findings
and one separation (R 1428–1429).

**Λ_spectra closes at the LIMIT** — not for want of the principal number, as
register 1341 supposed. The index runs to the last available species and stops:
98 cells, E = 58, of which 38 need more electrons than any atom has. **The
remaining twenty are within the limit, and eleven of those are the Madelung
exceptions, each nameable** (R 1395, corrected at R 1426).
