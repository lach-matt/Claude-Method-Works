# Λ_chem — THE CHEMICAL PROPERTIES INDEX

*Registers 1339, 1343–1346. Forty-two chemical properties of a species, indexed
on what each one IS and on which of physics, charge or amplitude it supplies.*

## Why the compendium needed it

Repeatedly in the Löwdin work a residual was left unexplained because a universal
account of it was sought. **Each time the answer was a property of the individual
species.** The record: the 1.029 factor on t(ℓ); the occupancy slope varying from
0.021 to 0.243; no f corridor, hence √6 untested; the crossing charge set by n_f;
Seaton's ratio valid only at p = 0.

**Λ_phys had been saying this all along** — no parameter of this work sits in the
universal column. **Λ_chem is the routing table that makes the statement usable:
before calling a residual unexplained, look up which chemical property supplies it
and which class it holds on.**

## The coordinates

**KIND** — what the property measures: *count · symmetry · size · energy · rate*

**SEAT** — which part of the species it belongs to: *the nucleus · the core · the
subvalence shell · the valence shell · **the aggregate***

**PCA** — which of *physics · charge · amplitude* it supplies

## The fifth seat

**Twelve of the forty-two are properties of MATTER IN BULK and not of an isolated
atom at all**: density, melting point, boiling point, hardness, crystal structure,
electrical and thermal conductivity, colour of the metal, smell, taste, metallic
character, reactivity.

*With eleven hand-picked properties the index could not say this. It appeared the
moment every chemical property of a species was demanded, and it is the reason the
compendium can now distinguish an atomic property from a bulk one at all.*

## The closure, and the boundary it declares

**E = 0 on fourteen cells** over the subvalence and valence shells. And the defect
climbs as foreign seats are added:

| seats included | cells | E |
|---|---|---|
| **subvalence + valence** | 14 | **0** |
| + the core | 15 | 3 |
| + the nucleus | 20 | 8 |
| + the aggregate | 21 | 11 |
| all five | 26 | 19 |

**PCA's domain is the subvalence and valence shells, and the index declares it by
degrading monotonically outside it.** *That is not a failure to close. It is a
boundary stated — as Seaton's ratio is valid at p = 0 and undefined beyond.*

## The last cell, and what filled it

All 1,440 orderings of the three axes give minimum E = 1, so the defect is
structural rather than a labelling artefact. **The cell is `symmetry × the valence
shell × a charge role`.**

**The fill is the ground TERM, which changes with charge:**

| Nₑ | c=1 | c=2 | c=3 | c=4 |
|---|---|---|---|---|
| **20** | ¹S₀ | ³D₁ | ³F₂ | ³F₂ |
| **38** | ¹S₀ | ³D₁ | ³F₂ | ³F₂ |
| 56 | ¹S₀ | ³F₂ | ³H₄ | — |
| 88 | ¹S₀ | ¹S₀ | ³H₄° | — |

*The sequence ¹S₀ → ³D₁ → ³F₂ is identical at two electron counts. Every ladder
table carried the term symbol; the configurations were recorded and the terms were
not.*

## The routing, by residual

| residual | property | class |
|---|---|---|
| the 1.029 factor on t(ℓ) | subshell radius | one subshell |
| no f corridor | centrifugal barrier | d and f only |
| the occupancy slope | subshell radius | one subshell |
| the crossing charge 2, 3, 5 | closed f shell n_f | period 6, 7 |

**Both of the first two were routed and both dissolved.** *The f corridor does not
exist because p = 0 is the node floor, so no rival lies below and L = −∞ — the
missing test is forbidden by the node count, not by missing data. And the 1.029
was arithmetic: the excess above U is 0.028 of the spread at p and 0.785 at d, a
ratio of 27.7, and the apparent 2.9% agreement came from comparing a ratio at p,
where t ≈ 1, with a ratio at d, where t ≈ 1.78.*

---

# Λ_PCA — PHYSICS ⊕ CHARGE ⊕ AMPLITUDE, AS ONE

*Registers 1297, 1323–1324, 1345. The merged index that correlates every chemical
property to the physics that requires it.*

## The merge

**Λ_phys** closes on (source, domain). **Λ_charge** closes on (role, carrier, sign,
regime). **The shared axis is `domain ≡ regime`** — both say where a statement
holds, and the charge regime is the physics domain at finer resolution.

**Merged on that axis alone: E = 0 on nine cells.**

| | universal | all elements | low | neutral | hydrogenic | one species |
|---|---|---|---|---|---|---|
| **standard** | 5 | · | · | · | · | · |
| **mathematics** | 3 | 1 | · | · | · | · |
| **literature** | · | 7 | 1 | · | · | · |
| **this work** | · | 2 | 5 | 2 | 4 | · |

**A staircase, and the diagonal is the whole content: nothing standard is
restricted to a region, and nothing this work produced claims universal validity.**

## What it gives that neither parent does

**The per-atom calibration.** A parameter's domain now reads as a SET OF ATOMS —
*universal* is every atom and ion, *all elements* every neutral, *neutral* c = 1,
*low* c = 2, *hydrogenic* c ≥ 3, *one species* a single (Z, c). **For any given
species the index states which parameters apply to it.**

**And the closing order puts `low` before `neutral`** — charge 2 is the most
particular domain. *The isoelectronic ladders confirm it independently: c = 2 is
the only charge with two-sided brackets.*

## Λ_amp — the amplitude's own index

**The amplitude is the electron–electron term**, and the multipole expansion of
1/r_ij gives, for each subshell pair, an exact finite list: **F^k for k even up to
2min(ℓ,ℓ′), G^k for k ≡ ℓ+ℓ′ (mod 2) from |ℓ−ℓ′| to ℓ+ℓ′.**

**Twenty cells, E = 0, a triangle 0 ≤ i ≤ ℓ** — once indexed on position within
sequence rather than multipole rank. *Indexed on the raw rank the single defect is
F¹, a term parity forbids.*

**And it explains the Slater result exactly.** At s/s the exchange G⁰ IS the direct
F⁰, so dropping exchange costs nothing; at f/f it discards four independent
quantities. **The count of lost integrals is the count of failures: Slater
screening threads 5 of 5 s-block brackets and 0 of 1 f.**

**The angular factor of the sole exchange integral for an s electron against an ℓ
electron is exactly 1/(2ℓ+1)** — 1, 1/3, 1/5, 1/7 at s, p, d, f, to machine
precision. *The reciprocal of the subshell's orbital degeneracy, a count Λ already
holds, and it agrees independently with h(ℓ) = h₀√(2ℓ+1) measured from the
collapse data.*

---

# A CORRECTION TO SEATON'S RATIO

**Previously recorded**: the ratio δ₂/δ₀ comes out at 1.25 where the dipole term
gives 1.00, and the departure is a per-core constant reproducible to two decimals.

**That measurement was made on penetrating channels, where the relation is
undefined.** Seaton's derivation assumes the outer electron is non-penetrating, so
the core polarisability is the whole interaction.

**Stated properly:**

| | series | ratio to Seaton | sd |
|---|---|---|---|
| **p = 0** | 3 | **1.150** | 0.206 |
| **p ≥ 1** | 10 | **−0.015** | 0.177 |

**On the non-penetrating branch the relation holds to 15%. On the penetrating
branch the ratio is zero — the relation carries no information at all.**

*Not "broken at d and sound at f". Valid at p = 0 and undefined at p ≥ 1, which is
a domain statement and exactly what Λ_phys's domain axis is for.*

**And the sign of δ₂ is penetration, not ℓ**: 0 of 3 positive at p = 0, 2 of 2 at
p = 5, monotone in p between.

---

# The channel constants in Lambda_phys

*Owed since register 1296; written at register 1571. The failure modes are the
point - a constant listed without the conditions under which it stops meaning
anything is a number pretending to be a law.*

| standing | count | what it means |
|---|---|---|
| attributed / derived | 5 | traceable to a published result or a proof |
| measured | 6 | read from data, with a stated spread |
| **fitted** | 3 | set to make the form agree; **carries no physics** |

**The three fitted constants are the amplitude law's**, and they are why nothing
in this work answers Loewdin's challenge.

## Failure modes

| constant | fails when | how it shows |
|---|---|---|
| the amplitude a | across a language boundary | six placement rules dead; a seventh **prohibited** |
| beta = 2/3 | - | no failure mode found; attributed, arity three |
| the gate l(l+1) | never as a gate | but SIX appearances under six discipline names |
| u0 = 4 | outside the collapse region | the switch is local to the d-wave entry |
| the nu form | as a MEASURE | bounded delta against diverging a*sqrt(p) - **impossible** |
| the three fitted | held out | the walk scores 90 against Madelung's 96 |

**The last row is the one to read.** A constant fitted on the data it explains
scores 99; held out it scores below the rule it was built to improve on.
*A failure mode is not a caveat - it is the boundary of the domain, and
Lambda_phys exists to carry boundaries.*
