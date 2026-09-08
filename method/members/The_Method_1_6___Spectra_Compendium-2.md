
# THE METHOD 1.6 — SPECTRA COMPENDIUM

**The index of Rydberg channels, and a value for every cell of it.**

This compendium supplies the book with coordinates. Its subject is Λ_spectra; its output is a defect for every channel of every element, graded by how the value was got. *The register carries the working record — the corrections, the reversals, and what remains open. This carries the answers.*

---

# 0 · THE COORDINATE SUPPLY

## What a coordinate is

        (Z, charge, ℓ, 2S+1)   →   δ,  with a grade, a source and a bound

**Z** the atomic number · **charge** the ionisation stage, 1 for the neutral · **ℓ** the Rydberg orbital · **2S+1** the multiplicity, which Hund's rule on the core derives from the ground state and does not require measuring.

**δ** is the quantum defect: E = −Z_c²R/(n−δ)², so a channel's whole Rydberg series follows from one number and the core charge.

**DECLARATION — the stored δ is the MEDIAN over a cell's members (T2, closed).** This was measured, not chosen: of 433 series whose member count reproduces exactly from raw, the stored value equals the median in 430 (99.3%); the 18 mean-agreements are series where median and mean coincide and distinguish nothing (R 1673, 1675, enlarged sample R 1679). The mean and asymptotic perspectives are carried alongside per cell, as perspectives of one definition (T6, M's ruling).

## The grades

| grade | rows | what it means |
|---|---|---|
| **exact** | **929** | forced by symmetry — δ = 0 when one electron faces a bare nucleus |
| **measured** | **358** | fitted to captured levels against an ionisation limit |
| **computed** | **103,545** | supplied by the channel equation, within the domain stated below |

**Nothing is ungraded.** A value with no provenance is not a coordinate.

## The witness

*Register 1578. This table used to grade cells VERIFIED, POSSIBLE and IMPROBABLE. **Improbable is a judgement about the future, not a fact about the record** — and register 1287 had already established the rule it breaks: an index whose coordinates mix the OBJECT with the OBSERVER cannot close. What replaces it is a fact and a named obstacle.*

| | cells | |
|---|---|---|
| the index admits | **104,832** | every channel of every element |
| **witnessed** | **358** | reality has been consulted for this cell |
| **unwitnessed** | **104,474** | it has not — see the bound |

**0.341% of the index has been checked against reality.** Every other cell is theory, and the compendium should be read that way.

## The bounds, witnessed and unwitnessed

*Not probabilities. Named obstacles, each of which may or may not be lifted.*

| cells | the obstacle |
|---|---|
| **28,526** | series unresolved above ng in any published analysis |
| **24,312** | no long-lived isotope |
| **17,626** | not keyable: no single 2S+1 (hole+electron or multi-valence) |
| **11,605** | open-shell core, 16 parents |
| **9,756** | open-shell core, 3 parents |
| **5,280** | open-shell core, 119 parents |
| **2,691** | no analysis located at this charge (NOT a bound on existence) |
| **1,760** | no nuclide synthesised; theoretically admitted — Janet left-step, 8s(2) closes the eighth period at element 120 |
| **1,744** | no nuclide synthesised; theoretically admitted — Janet left-step, 8s(1) opens element 119 |
| **929** | derived by symmetry; no measurement required |
| **240** | none — separable series, simply not yet measured |
| **6** | limit 41449.451; one electron outside a closed shell |
| **5** | no primordial isotope (R 1587) |
| **5** | limit 31406.4677325; one electron outside a closed shell |
| **3** | limit 66928.04; one electron outside a closed shell |
| **3** | limit 49266.66; one electron outside a closed shell |
| **2** | limit 48278.48; one electron outside a closed shell |
| **2** | limit 48387.634; one electron outside a closed shell |
| **2** | limit 32848.872; one electron outside a closed shell |
| **1** | limit 46670.107; one electron outside a closed shell |
| **1** | limit 43762.6; one electron outside a closed shell |

**The charge bound is the one to distrust.** It reads *no analysis located*, not *no analysis exists* — and register 1577 found twelve MEASURED cells above it in this index's own file (Ti XI, Fe XV, Fe XVI), with Theodosiou 1986 covering all positive ions of all atoms to Z = 37.

*Accuracy figures in this compendium are quoted against the WITNESSED-plus-possible set, not against the whole index.*

## The bound, which needs no measurement at all

        B = min( p , n₀ − ℓ − 1 )

with **p** the core's orbital count at that ℓ and **n₀** the first Pauli-allowed principal number, both read from the ground-state configuration. **floor(δ) ≤ B holds on every measured channel without exception**, and B travels with every row of the table — so the book can bound a defect without consulting one.

## The filler, and its domain

Where no capture reaches, the channel equation supplies the value:

        p > 0 :   δ = 0.3772 · p^e(Nₑ) · Nₑ^k · ln(c+1)/c
        p = 0 :   δ = 0.5415 · C(Z) · (Nₑ−1)/Nₑ · Nₑ^k · ln(c+1)/c

        e(Nₑ) = 0.8297 − 0.0900·ln Nₑ          k = 0.4942
        Nₑ    = Z − charge + 1
        C(Z)  = the collapse coordinate across the Janet block boundary

**Domain: Z ≤ 92, charge ≤ 10, ℓ ≤ 4, a single-parent core.** Fitted there on 277 channels at rms 0.1329 and R² 0.9747, anchored at Z = 2 and Z = 90. *Every value outside the domain is `unwitnessed`, and the `bound` column names why.*

## The table

*The index is a rectangle, and the file says so: 13,104 keys of (Z, charge, 2S+1), each carried across all eight values of ℓ, 104,832 cells in all. Nothing is missing from it and nothing is chosen — what varies from row to row below is not how many cells exist but how they were got.*

| ℓ | cells | exact | measured | computed | δ, low to high |
|---|---|---|---|---|---|
| **0** s | 13,104 | 115 | 92 | 12,897 | 0.0000 … 6.0207 |
| **1** p | 13,104 | 115 | 81 | 12,908 | −0.0144 … 5.6604 |
| **2** d | 13,104 | 115 | 89 | 12,900 | −0.1152 … 4.8123 |
| **3** f | 13,104 | 115 | 59 | 12,930 | −0.2367 … 3.6462 |
| **4** g | 13,104 | 115 | 36 | 12,953 | −0.0401 … 0.0381 |
| **5** h | 13,104 | 118 | 1 | 12,985 | 0.0000 … 0.0001 |
| **6** i | 13,104 | 118 | 0 | 12,986 | 0.0000 … 0.0000 |
| **7** k | 13,104 | 118 | 0 | 12,986 | 0.0000 … 0.0000 |
| | **104,832** | **929** | **358** | **103,545** | |

**The measured cells and the witnessed cells are the same 358 — not two counts that agree, the same set, tested cell by cell.** *A cell is measured exactly when reality was consulted for it, so the grade column and the witness column answer one question twice.*

**Two readings a reader should take from the shape.** *The first: the observation runs out at ℓ = 5. One cell above g has ever been measured, and none above h; everything the compendium says about high-ℓ channels is the channel equation speaking, and §* The filler, and its domain *states the domain it speaks within. The second: δ narrows as ℓ rises — the s channels span six units, the g channels a twelfth of one — which is the core's reach falling away, and it is why the Pauli bound of §* The bound, which needs no measurement at all *costs nothing to state at high ℓ and everything at low.*

*Every figure in this table is read from the coordinate file itself, and a figure that drifts from it fails the press.*

## The file

**`COORDINATES-2.13`** (CSV, 104,832 rows, one per admitted cell) is the coordinate index itself, and is delivered with this compendium as its data companion. Everything in Parts 0–II is read from it at build; the file is the object, the pages are the reading. A cell is cited from any volume as **COORD(Z, charge, ℓ, 2S+1)** — the four coordinates are the key and are unique in the file.

| column | alphabet | meaning |
|---|---|---|
| `Z` | 1 … 120 | the element; 119 and 120 admitted on Janet's authority, register 1578's bound column saying so |
| `charge` | 1 … Z | the ion; charge ≤ Z is the triangle, 7,260 (Z, charge) pairs |
| `l` | 0 … 7 | the running electron's ℓ |
| `mult` | 1 … 9 | 2S+1; the set allowed at a pair is a function of the electron count Z − charge alone, holding on all 7,260 pairs |
| `delta` | −0.2367 … 6.0207 | the quantum defect held for the channel |
| `grade` | exact · measured · computed | 929 · 358 · 103,545 — one-electron cells are exact by symmetry |
| `source` | six provenances, 32 strings | the rule that computed the value, or the compilation and species it was taken from; the strings run to thirty-two because each NIST retrieval carries its own session |
| `B` | 0.0000 … 7.0000 | the Pauli bound on δ, read from the ground state; nonzero on 36,917 cells, and integer-valued on all but twenty-five of them |
| `witness` | witnessed · unwitnessed | 358 · 104,474 — reality consulted, or not |
| `bound` | 22 distinct | the named obstacle — on every unwitnessed cell and on 25 witnessed ones (§ *The bounds, witnessed and unwitnessed*) |

**The six provenances, and why the column shows thirty-two strings.** *Every cell says where its
value came from, and the strings fall into six kinds:* **the channel equation, 103,545 cells · one
electron, δ = 0 by symmetry, 929 · captured levels, 325 · NIST ASD retrieved 2026-08-14, 25 ·
three species read from their own level files at register 1627, 3 · Theodosiou, Manson and Inokuti
1986, 5.** *They sum to 104,832. The thirty-two distinct strings are not thirty-two compilations:
twenty-five of them are the same NIST retrieval, each carrying the session that fetched it and the
series it drew, so the count of strings measures provenance detail and not variety of source. The
compilations behind the measured channels are named in* § B.1 Sources.

**One row, as it stands in the file.** *Sodium, singly charged nucleus, the s channel, doublet:*

```
Z=11  charge=1  l=0  mult=2  delta=1.34857  grade=measured
source=NIST ASD fetched 2026-08-14 (session 1.8 queue); NaI 2S n=3-20, 18 members; median defect
B=0.02475  witness=witnessed  bound=limit 41449.451; one electron outside a closed shell
```

*Read it as* COORD(11, 1, 0, 2)*: the quantum defect of the sodium s series is 1.34857, measured
rather than computed, taken as the median over eighteen members of the n = 3–20 series, and the
Pauli bound the ground state imposes on it is 0.02475. A cell carries its value, how the value was
got, who supplied it, and what stands in the way of getting a better one.*

*The seven columns Part 0 once printed —* `Z charge l mult delta grade source B status` *— were the file at register 630; `status` (improbable / possible) became `witness` and `bound` at register 1578, and Z was extended from 118 to 120 at the entry that admitted 3,504 cells on Janet's authority. Every count on these pages is read from the file; none is transcribed.*

![The coordinate supply](figures-compendia/fig-supply.png)

*Above: the supply per element, on a log scale — the measured and exact cells against the computed. Below left: every measured coordinate, δ against electron count, coloured by charge. Below right: the Pauli bound, which holds on every measured cell and is read from the ground state alone.*

---

# 0′ · THE DERIVED SUPPLY — Λ_chain's candidate spectrum

*This compendium's founding supply runs observation-side: (Z, charge, ℓ, 2S+1) →
δ, graded by how the value was got. The Löwdin solution adds the equation-side
supply: at every element, a depth for every frontier channel, computed from the
many-electron field with one constant and no measurement. The two supplies meet
at the same atoms from opposite directions, and where one is silent the other
speaks.*

## What a derived coordinate is

        (Z, n, ℓ)   →   D,  in hartree, with margin, provenance and score

**Z** the atomic number, neutral walk · **(n, ℓ)** any frontier channel offered at
that step · **D** its converged one-channel depth in the frozen V^{N−1} field ·
**margin** attached to the entrant row: the gap to the runner-up, the quantity
every later scrutiny is measured against.

![The entrant margin](figures/figaddscmargin.png)

*The entrant margin at every scored row. Blue: the five contested rows, where the correlation clause was computed and every competition widened.*

## The grades

| grade | meaning | rows |
|---|---|---|
| **SCORED** | the entrant met the measured ground configuration | 107 of 107, Z = 2–108 |
| **UNWITNESSED** | no measurement exists to meet; published falsifiable | 12, Z = 109–120 |
| **PINNED** | the channel's depth is hydrogenic and Z-independent | every g row |

*UNWITNESSED carries this book's own sense: not undefected for want of trying —
the rows await a measurement science has yet to provide* (register 1712).

## The pinned rows, stated as values

![The pinned rows](figures/figaddscgpin.png)

*The pinned rows — the constants of the derived supply. Top: the four g channels, each at −1/(2n²) to storage precision, spread ≤ 10⁻⁵ across spans of 28 to 70 elements. Bottom: the same lines against the f and d channels that respond to Z.*

> **5g: −0.020000 over 65 elements · 6g: −0.013889 over 70 · 7g: −0.010204 over
> 57 · 8g: −0.0078125 over 28** — each equal to −1/(2n²) to storage precision,
> spread ≤ 10⁻⁵ across the full span.

**A channel whose value the nucleus cannot move needs no measurement and admits
no fit.** The compendium records these once, as constants of the walk, and the
absence of a g series anywhere in the observation-side supply is thereby
explained rather than merely noted (register 1704).

## The unwitnessed twelve

| Z | entrant | D_ent | margin |
|---|---|---|---|
| 109–112 | 6d | −0.326 → −0.423 | 0.171 → 0.264 |
| 113–118 | 7p | −0.160 → −0.360 | 0.058 → 0.210 |
| 119, 120 | 8s | −0.159, −0.189 | 0.097, 0.098 |

Worst-case spin-orbit narrowing 0.083 Ha; every margin clears it. *When the
spectra can be taken, these rows are scored like any others, and this table is
where a miss would land.*

## How the two supplies interlock

**Where the observation supply goes silent, the derived supply names why.** The f
corridor of Chapter 34 has no test (L = −∞ at the node floor); the derived supply
puts the collapse condition at that exact address and decides La, Ac, Th there
(register 1703). **Where the derived supply is unwitnessed, the observation
supply states what witnessing would take.** And at the hundred-odd elements both
supplies cover, they are independent routes to one order — *the strongest
cross-check either one owns.*

---

# I · THE INDEX

## The four coordinates, and where each comes from

| coordinate | alphabet | derived from |
|---|---|---|
| Z | 1 … 120 | given; 119–120 admitted, unwitnessed |
| charge | 1 … Z | given |
| ℓ | 0 … 7 | given |
| 2S+1 | Hund's rule on the core | **the ground state** |

**The multiplicity is not a free coordinate.** Hund's first rule applied to the core's ground configuration gives the allowed values, exact on all 24 electron counts tested. Applying it as a constraint removes **247,248 cells — 71%** of what the naive product would admit.

## Which cells exist

A cell is admitted when charge ≤ Z, at least one electron remains, the multiplicity is one Hund's rule allows, and an orbital of that ℓ is available. **Every cell the index admits is physically possible**: the forbidden ones were excluded at construction, so the survey holds none.

## Which cells can be measured

| restriction | cells |
|---|---|
| the index admits | 104,832 |
| Z ≤ 92 — naturally occurring | 61,152 |
| and charge ≤ 10 | 11,416 |
| and ℓ ≤ 4 — where series resolve | 4,395 |
| **and a single-parent core** | **1,755** |

## The parent-term wall

**A closed-shell core has one parent term and gives one Rydberg series per ℓ.** An open-shell core gives one series per parent, all interleaved, converging on different limits.

Fe IV's 3d⁴ core carries sixteen LS terms. Its published levels show thirteen of them across **24 distinct (parent, ℓ, term) series, every one with a single member.** Fe IV has about a thousand analysed levels and no extractable defect: *the levels are identified and the series are not separable.*

**This is why the compendium holds Ne-like and Na-like ions at charge 15 and 16 and no open-shell ion above charge 6.** An open-shell core does not produce the object a quantum-defect index holds.

## The Janet collapse

Two channels can both have p = 0 — no core orbitals of their own ℓ — and differ by a factor of ten. Ti IV's nd is **0.6202**; Sr II's nf is **0.0618**.

What separates them is **orbital collapse**, and its threshold is a Janet block boundary exactly:

| orbital | n+ℓ | block opens at | element | collapse threshold |
|---|---|---|---|---|
| **3d** | 5 | **Z = 21** | Sc | **21** |
| **4f** | 7 | **Z = 57** | La | **57** |
| **5f** | 8 | **Z = 89** | Ac | **89** |

Across 116 cells with p = 0 at ℓ = 2 or 3: **collapsed median 0.637, uncollapsed 0.036**, U-test p = 9.8×10⁻⁴. The transition is rapid rather than sharp — the largest defects are the atoms *approaching* a boundary: Ca I nd = 0.908 at Z = 20 against a threshold of 21, and Ba II nf = 0.756 at 56 against 57.

**The collapse coordinate is read from the periodic table, not fitted**, and it is why a defect at ℓ = 2 can be large in one element and negligible in its neighbour.

![The channel map](figures-compendia/fig-channel-map.png)

*Every cell valued. The upper panel is δ itself, charge collapsed to its largest; the lower is which mechanism sets it, with the three Janet boundaries marked.*

---

# II · THE CHANNELS

**Every captured series, with its fit.** These are the measured rows of the coordinate table.

Three marks state a limitation. An **asterisk** on the species marks a two-member channel: two points give a defect and one consistency check but cannot detect a perturbation. A **dagger** on the n-range marks an internal gap. And the **limit column** names how the ionisation limit was obtained — *published* where a source quotes it, *theoretical* where it is exact by construction, *constructed* where this work built it by summing two spectra. *A channel resting on a limit this work computed is not a measurement against an independent standard, and the row says so.* The **bracket column** reads `m/k` — of k cells with true measured neighbours on both sides, m pass the sealed test under ruling 26 (strict membership, quotation-floor guard, §22.5 admissibility; register 1763) — or `no-triple` where the row's members contain no three consecutive n, or `untested` where the run's data conditions are not met (the count paragraph below the table gives the split).

| species | series | n | levels | interior | bracket | n* range | δ | σ(δ) | fits | limit cm⁻¹ |
|---|---|---|---|---|---|---|---|---|---|---|
| Al I | 3s²nf ²F° | 4–55 | 52 | 50 | 50/50 | 4.0–55.0 | +0.0429 | 0.0552 | 1 | 48,278.480 |
| Al I | 3s²nd ²D | 3–34 | 32 | 30 | 30/30 | 2.6–33.7 | +0.0248 | 0.6297 | 1 | 48,278.480 |
| Al I | 3s²ns ²S | 4–16 | 13 | 11 | 11/11 | 2.2–14.2 | +1.7670 | 0.0537 | 1 | 48,278.480 |
| Al I | 3s²np ²P° | 3–7 | 5 | 3 | 3/3 | 1.5–5.7 | +1.3365 | 0.2080 | 1 | 48,278.480 |
| Al II | 3sns ¹S | 4–16 | 13 | 11 | 11/11 | 2.8–14.8 | +1.2028 | 0.0147 | 2 | 151,862.500 |
| Al II | 3sns ³S | 4–13 | 10 | 8 | 8/8 | 2.7–11.7 | +1.2711 | 0.0474 | 2 | 151,862.500 |
| Al II | 3snd ¹D | 3–11 | 9 | 7 | 7/7 | 3.2–10.9 | +0.0603 | 0.3897 | 2 | 151,862.500 |
| Al II | 3sng | 5–13 | 9 | 7 | 7/7 | 5.0–13.0 | +0.0212 | 0.0070 | 2 | 151,862.500 |
| Al II | 3snd ³D | 3–10 | 8 | 6 | 6/6 | 2.8–9.8 | +0.2024 | 0.0096 | 2 | 151,862.500 |
| Al II | 3snf ³F° | 4–11 | 8 | 6 | 6/6 | 3.9–11.0 | +0.0140 | 0.4088 | 2 | 151,862.500 |
| Al II | 3snp ³P° | 4–10 | 7 | 5 | 5/5 | 3.1–9.1 | +0.8982 | 0.0571 | 2 | 151,862.500 |
| Al III | nd 2D J=5/2 | 3–8 | 6 | 4 | 4/4 | 2.9–7.9 | +0.0644 | 0.0071 | 3 | 229,445.710 |
| Al III | nf 2F* J=5/2 | 4–9 | 6 | 4 | 4/4 | 4.0–9.0 | +0.0044 | 0.0005 | 3 | 229,445.710 |
| Al III | ng 2G J=7/2 | 5–9 | 5 | 3 | 2/3 | 5.0–9.0 | +0.0010 | 0.0001 | 3 | 229,445.710 |
| Al III | nh 2H* J=9/2 | 6–9 | 4 | 2 | 1/2 | 6.0–9.0 | +0.0003 | 0.0000 | 3 | 229,445.710 |
| Al III | np 2P* J=1/2 | 3–7 | 5 | 3 | 3/3 | 2.4–6.4 | +0.6056 | 0.0128 | 3 | 229,445.710 |
| Al III | ns 2S J=1/2 | 3–8 | 6 | 4 | 4/4 | 2.1–7.1 | +0.9049 | 0.0098 | 3 | 229,445.710 |
| Al IV * | nf 2[5/2] J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0349 | 0.0100 | 4 | 968,924.400 |
| Al IV | ns 2[3/2]* J=2 | 3–5 | 3 | 1 | 0/1 | 2.2–4.2 | +0.7638 | 0.0042 | 4 | 968,924.400 |
| Ar I | nd 2[7/2]* J=4 | 3–6 | 4 | 2 | 2/2 | 2.8–5.6 | +0.3516 | 0.0715 | 1 | 127,198.600 |
| Ar I | np 2[1/2] J=1 | 4–7 | 4 | 2 | 1/2 | 2.2–5.2 | +1.7855 | 0.0204 | 1 | 127,198.600 |
| Ar I | np 2[3/2] J=1 | 4–7 | 4 | 2 | 1/2 | 2.3–5.3 | +1.7107 | 0.0123 | 1 | 127,198.600 |
| Ar I | np 2[5/2] J=3 | 4–7 | 4 | 2 | 1/2 | 2.2–5.2 | +1.7437 | 0.0119 | 1 | 127,198.600 |
| Ar I | ns 2[3/2]* J=1 | 4–7 | 4 | 2 | 1/2 | 1.8–4.8 | +2.1701 | 0.0138 | 1 | 127,198.600 |
| Ar I | ns 2[3/2]* J=2 | 4–7 | 4 | 2 | 1/2 | 1.8–4.8 | +2.1886 | 0.0132 | 1 | 127,198.600 |
| Ar II | (³P)ns ⁴P J=5/2 | 4–6 | 3 | 1 | 1/1 | 2.2–4.3 | +1.7463 | 0.0477 | 2 | 222,848.300 |
| Ar II | (³P)ns ⁴P J=3/2 | 4–6 | 3 | 1 | 1/1 | 2.2–4.3 | +1.7246 | 0.0663 | 2 | 222,848.300 |
| Ar II | (³P)ns ⁴P J=1/2 | 4–6 | 3 | 1 | 1/1 | 2.2–4.4 | +1.6821 | 0.1507 | 2 | 222,848.300 |
| Ar II | (³P)ns ²P J=3/2 | 4–6 | 3 | 1 | 1/1 | 2.3–4.4 | +1.6711 | 0.1084 | 2 | 222,848.300 |
| Ar II | (³P)ns ²P J=1/2 | 4–6 | 3 | 1 | 1/1 | 2.3–4.4 | +1.6355 | 0.1526 | 2 | 222,848.300 |
| Ar II | (³P)nd ⁴D J=7/2 | 3–5 | 3 | 1 | 1/1 | 2.2–4.4 | +0.6930 | 0.1695 | 2 | 222,848.300 |
| Ar II | (³P)nd ⁴D J=5/2 | 3–5 | 3 | 1 | 1/1 | 2.2–4.4 | +0.6880 | 0.1753 | 2 | 222,848.300 |
| Ar II | (³P)nd ⁴D J=3/2 | 3–5 | 3 | 1 | 1/1 | 2.2–4.4 | +0.6786 | 0.1919 | 2 | 222,848.300 |
| Ar II | (³P)nd ⁴D J=1/2 | 3–5 | 3 | 1 | 1/1 | 2.2–4.4 | +0.6669 | 0.2155 | 2 | 222,848.300 |
| Ar II | (³P)nd ⁴F J=9/2 | 3–5 | 3 | 1 | 1/1 | 2.3–4.4 | +0.6121 | 0.0885 | 2 | 222,848.300 |
| Ar II | ng 2[4] J=9/2 | 6–8 | 3 | 1 | untested | 6.0–8.0 | +0.0089 | 0.0036 | 2 | 222,848.300 |
| Ar II | ng 2[6] J=11/2 | 6–8 | 3 | 1 | untested | 6.0–8.0 | +0.0035 | 0.0003 | 2 | 222,848.300 |
| Ar II | ng 2[6] J=13/2 | 6–8 | 3 | 1 | untested | 6.0–8.0 | +0.0035 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ng 2[2] J=3/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | -0.0006 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ng 2[2] J=5/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | -0.0006 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ng 2[3] J=5/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0063 | 0.0001 | 2 | 222,848.300 |
| Ar II * | ng 2[3] J=7/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0063 | 0.0001 | 2 | 222,848.300 |
| Ar II * | ng 2[4] J=7/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0114 | 0.0001 | 2 | 222,848.300 |
| Ar II * | ng 2[5] J=11/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0119 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ng 2[5] J=9/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0119 | 0.0002 | 2 | 222,848.300 |
| Ar II * | nh 2[3]* J=5/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | -0.0017 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[3]* J=7/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | -0.0017 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[4]* J=7/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0021 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[4]* J=9/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0021 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[5]* J=11/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0047 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[5]* J=9/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0047 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[6]* J=11/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0045 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[6]* J=13/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0045 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[7]* J=13/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | -0.0000 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[7]* J=15/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | -0.0000 | 0.0001 | 2 | 222,848.300 |
| Ar II * | ni 2[4] J=7/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | -0.0009 | 0.0005 | 2 | 222,848.300 |
| Ar II * | ni 2[4] J=9/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | -0.0009 | 0.0005 | 2 | 222,848.300 |
| Ar II * | ni 2[5] J=11/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | +0.0012 | 0.0003 | 2 | 222,848.300 |
| Ar II * | ni 2[5] J=9/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | +0.0012 | 0.0003 | 2 | 222,848.300 |
| Ar II * | ni 2[6] J=11/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | +0.0025 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ni 2[6] J=13/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | +0.0025 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ni 2[7] J=13/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | +0.0023 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ni 2[7] J=15/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | +0.0023 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ni 2[8] J=15/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | -0.0000 | 0.0006 | 2 | 222,848.300 |
| Ar II * | ni 2[8] J=17/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | -0.0000 | 0.0006 | 2 | 222,848.300 |
| Ar II | 3s2.3p4.(3P).nd 4D J=7/2 | 3–5 | 3 | 1 | untested | 2.2–4.4 | +0.6930 | 0.0749 | 2 | 222,848.300 |
| Ar II | 3s2.3p4.(3P).ns 4P J=1/2 | 4–6 | 3 | 1 | untested | 2.2–4.4 | +1.6821 | 0.0615 | 2 | 222,848.300 |
| Ar II | 3s2.3p4.(3P).ns 4P J=3/2 | 4–6 | 3 | 1 | untested | 2.2–4.3 | +1.7246 | 0.0283 | 2 | 222,848.300 |
| Ar II | 3s2.3p4.(3P).ns 4P J=5/2 | 4–6 | 3 | 1 | untested | 2.2–4.3 | +1.7463 | 0.0203 | 2 | 222,848.300 |
| B II | nd 1D J=2 | 3–7 | 5 | 3 | 2/3 | 3.0–7.1 | -0.0323 | 0.0111 | 2 | 202,691.900 |
| B II | nd 3D J=1 | 3–6 | 4 | 2 | 2/2 | 2.9–5.9 | +0.0772 | 0.0138 | 2 | 202,691.900 |
| B II | nf 3F* J=2 | 4–7 | 4 | 2 | 2/2 | 4.0–6.9 | +0.0397 | 0.0132 | 2 | 202,691.900 |
| B II | ng 3G J=3 | 5–7 | 3 | 1 | 1/1 | 5.0–7.1 | -0.0401 | 0.0192 | 2 | 202,691.900 |
| B II | np 1P* J=1 | 3–5 | 3 | 1 | 1/1 | 2.7–4.6 | +0.3284 | 0.0668 | 2 | 202,691.900 |
| B II | np 3P* J=0 | 3–6 | 4 | 2 | 2/2 | 2.7–5.8 | +0.2231 | 0.0345 | 2 | 202,691.900 |
| B II | ns 1S J=0 | 3–6 | 4 | 2 | 1/2 | 2.6–5.6 | +0.4303 | 0.0172 | 2 | 202,691.900 |
| B II | ns 3S J=1 | 3–7 | 5 | 3 | 2/3 | 2.5–6.5 | +0.5211 | 0.0148 | 2 | 202,691.900 |
| B III | nd 2D J=3/2 | 3–11 | 9 | 7 | 7/7 | 3.0–11.0 | +0.0023 | 0.0002 | 3 | 305,930.800 |
| B III | nf 2F* J=5/2 | 4–11 | 8 | 6 | 5/6 | 4.0–11.0 | +0.0003 | 0.0000 | 3 | 305,930.800 |
| B III | ng 2G J=7/2 | 5–10 | 6 | 4 | 3/4 | 5.0–10.0 | +0.0001 | 0.0000 | 3 | 305,930.800 |
| B III | nh 2H* J=9/2 | 6–10 | 5 | 3 | 3/3 | 6.0–10.0 | +0.0000 | 0.0000 | 3 | 305,930.800 |
| B III | np 2P* J=1/2 | 2–9 | 8 | 6 | 3/6 | 2.0–9.0 | +0.0437 | 0.0007 | 3 | 305,930.800 |
| B III | ns 2S J=1/2 | 2–9 | 8 | 6 | 6/6 | 1.8–8.8 | +0.1959 | 0.0030 | 3 | 305,930.800 |
| B IV | 1s.nd 1D J=2 | 3–10 | 8 | 6 | 2/6 | 3.0–10.0 | +0.0007 | 0.0002 | 4 | 2,091,995.451 |
| B IV | 1s.nd 3D J=1 | 3–10 | 8 | 6 | 3/6 | 3.0–10.0 | +0.0021 | 0.0003 | 4 | 2,091,995.451 |
| B IV | 1s.nf 1F* J=3 | 4–9 | 6 | 4 | 3/4 | 4.0–9.0 | +0.0004 | 0.0005 | 4 | 2,091,995.451 |
| B IV | 1s.ng 1G J=4 | 5–9 | 5 | 3 | 0/3 | 5.0–9.0 | +0.0002 | 0.0004 | 4 | 2,091,995.451 |
| B IV | 1s.nh 1H* J=5 | 6–9 | 4 | 2 | 1/2 | 6.0–9.0 | -0.0002 | 0.0002 | 4 | 2,091,995.451 |
| B IV * | 1s.ni 1I J=6 | 7–8 | 2 | 1 | no-triple | 7.0–8.0 | -0.0003 | 0.0003 | 4 | 2,091,995.451 |
| B IV | 1s.np 1P* J=1 | 3–10 | 8 | 6 | 3/6 | 3.0–10.0 | -0.0096 | 0.0003 | 4 | 2,091,995.451 |
| B IV | 1s.np 3P* J=0 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0350 | 0.0001 | 4 | 2,091,995.451 |
| B IV | 1s.ns 1S J=0 | 3–10 | 8 | 6 | 4/6 | 3.0–10.0 | +0.0392 | 0.0004 | 4 | 2,091,995.451 |
| B IV | 1s.ns 3S J=1 | 3–10 | 8 | 6 | 6/6 | 2.9–9.9 | +0.1011 | 0.0009 | 4 | 2,091,995.451 |
| B V | nd 2D J=3/2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0005 | 0.0002 | 5 | 2,744,111.380 |
| B V | nf 2F* J=5/2 | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +0.0004 | 0.0002 | 5 | 2,744,111.380 |
| B V | ng 2G J=7/2 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0003 | 0.0002 | 5 | 2,744,111.380 |
| B V | nh 2H* J=9/2 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0003 | 0.0001 | 5 | 2,744,111.380 |
| B V | ni 2I J=11/2 | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0004 | 0.0001 | 5 | 2,744,111.380 |
| B V * | nk 2K* J=13/2 | 8–9 | 2 | 1 | no-triple | 8.0–9.0 | +0.0004 | 0.0001 | 5 | 2,744,111.380 |
| B V | np 2P* J=1/2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0008 | 0.0002 | 5 | 2,744,111.380 |
| B V | ns 2S J=1/2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0008 | 0.0002 | 5 | 2,744,111.380 |
| Ba II | nd 2D J=3/2 | 5–25† | 14 | 12 | 10/10 | 2.4–22.6 | +2.4147 | 0.0516 | 2 | 80,687.900 |
| Ba II | nf 2F* J=5/2 | 4–12 | 9 | 7 | 7/7 | 3.7–11.1 | +0.7559 | 0.1645 | 2 | 80,687.900 |
| Ba II | ng 2G J=7/2 | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | +0.0185 | 0.0022 | 2 | 80,687.900 |
| Ba II | np 2P* J=1/2 | 6–12 | 7 | 5 | 5/5 | 2.7–8.8 | +3.2408 | 0.0287 | 2 | 80,687.900 |
| Ba II | ns 2S J=1/2 | 6–30† | 18 | 16 | 14/14 | 2.3–26.4 | +3.5984 | 0.0191 | 2 | 80,687.900 |
| Ba III | 5p5.(2P*<3/2>).nd 2[1/2]* J=0 | 5–7 | 3 | 1 | 1/1 | 2.5–4.7 | +2.3509 | 0.0972 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[1/2]* J=1 | 5–7 | 3 | 1 | 1/1 | 2.5–4.8 | +2.3360 | 0.0975 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[3/2]* J=1 | 5–7 | 3 | 1 | 1/1 | 2.7–4.9 | +2.1891 | 0.0829 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[3/2]* J=2 | 5–7 | 3 | 1 | 1/1 | 2.6–4.8 | +2.3061 | 0.0981 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[5/2]* J=2 | 5–7 | 3 | 1 | 1/1 | 2.6–4.8 | +2.2821 | 0.0849 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[5/2]* J=3 | 5–7 | 3 | 1 | 1/1 | 2.6–4.8 | +2.2601 | 0.0738 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[7/2]* J=3 | 5–7 | 3 | 1 | 1/1 | 2.6–4.8 | +2.3041 | 0.0846 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[7/2]* J=4 | 5–7 | 3 | 1 | 1/1 | 2.6–4.8 | +2.3113 | 0.0890 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).ns 2[3/2]* J=1 | 6–8 | 3 | 1 | 1/1 | 2.7–4.8 | +3.2585 | 0.0242 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).ns 2[3/2]* J=2 | 6–8 | 3 | 1 | 1/1 | 2.7–4.7 | +3.2795 | 0.0267 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<1/2>).nd 2[3/2]* J=2 | 7–16 | 10 | 8 | 8/8 | 4.8–13.8 | +2.1786 | 0.0136 | 3 | 306,650.000 |
| Ba III | 5p5.(2P*<1/2>).ns 2[1/2]* J=1 | 8–17 | 10 | 8 | untested | 4.8–13.8 | +3.2300 | 0.0154 | 3 | 306,650.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[3/2]* J=2 | 8–22† | 14 | 12 | untested | 5.9–19.9 | +2.1273 | 0.0227 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).ns 2[3/2]* J=1 | 9–23 | 15 | 13 | untested | 5.8–19.9 | +3.2018 | 0.0273 | 3 | 289,100.000 |
| Ba III * | 5p5.(2P*<3/2>).ng 2[11/2]* J=5 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0394 | 0.0028 | 3 | 289,100.000 |
| Ba III * | 5p5.(2P*<3/2>).ng 2[11/2]* J=6 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0397 | 0.0029 | 3 | 289,100.000 |
| Ba III * | 5p5.(2P*<3/2>).ng 2[5/2]* J=2 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0428 | 0.0002 | 3 | 289,100.000 |
| Ba III * | 5p5.(2P*<3/2>).ng 2[5/2]* J=3 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0422 | 0.0000 | 3 | 289,100.000 |
| Ba III * | 5p5.(2P*<3/2>).ng 2[7/2]* J=3 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0208 | 0.0006 | 3 | 289,100.000 |
| Ba III * | 5p5.(2P*<3/2>).ng 2[7/2]* J=4 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0212 | 0.0007 | 3 | 289,100.000 |
| Ba III * | 5p5.(2P*<3/2>).ng 2[9/2]* J=4 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0174 | 0.0030 | 3 | 289,100.000 |
| Ba III * | 5p5.(2P*<3/2>).ng 2[9/2]* J=5 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0172 | 0.0029 | 3 | 289,100.000 |
| Be I | 2snp ¹P° | 3–13 | 11 | 9 | 9/9 | 2.7–12.6 | +0.3590 | 0.1025 | 1 | 75,192.500 |
| Be I | 2snd ³D | 3–12 | 10 | 8 | 8/8 | 2.9–11.9 | +0.1109 | 0.0129 | 1 | 75,192.500 |
| Be I | 2snd ¹D | 3–12 | 10 | 8 | 8/8 | 3.2–12.1 | -0.1152 | 0.0970 | 1 | 75,192.500 |
| Be I | 2sns ¹S | 3–11 | 9 | 7 | 7/7 | 2.3–10.3 | +0.6774 | 0.0136 | 1 | 75,192.500 |
| Be I | 2sns ³S | 3–8 | 6 | 4 | 4/4 | 2.2–7.2 | +0.7910 | 0.0429 | 1 | 75,192.500 |
| Be I | 2snp ³P° | 3–8 | 6 | 4 | 4/4 | 2.6–7.6 | +0.3773 | 0.0374 | 1 | 75,192.500 |
| Be I | 2snf ³F° | 4–7 | 4 | 2 | 2/2 | 4.0–7.0 | +0.0305 | 0.0063 | 1 | 75,192.500 |
| Be II | ns ²S | 2–10 | 9 | 7 | 7/7 | 1.7–9.7 | +0.2623 | 0.0112 | 2 | 146,882.860 |
| Be II | np ²P° | 2–10 | 9 | 7 | 7/7 | 2.0–10.0 | +0.0491 | 0.0039 | 2 | 146,882.860 |
| Be II | nd ²D | 3–9 | 7 | 5 | 5/5 | 3.0–9.0 | +0.0021 | 0.0004 | 2 | 146,882.860 |
| Be II | nf ²F° | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +0.0001 | 0.0001 | 2 | 146,882.860 |
| Be II | ng ²G | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | -0.0001 | 0.0001 | 2 | 146,882.860 |
| Be II | nh ²H° | 6–10 | 5 | 3 | 3/3 | 6.0–10.0 | -0.0002 | 0.0001 | 2 | 146,882.860 |
| Be III | 1s.nd 1D J=2 | 3–10 | 8 | 6 | 4/6 | 3.0–10.0 | +0.0008 | 0.0002 | 3 | 1,241,256.601 |
| Be III | 1s.nd 3D J=2 | 3–10 | 8 | 6 | 3/6 | 3.0–10.0 | +0.0023 | 0.0002 | 3 | 1,241,256.601 |
| Be III | 1s.nf 1F* J=3 | 4–9 | 6 | 4 | 2/4 | 4.0–9.0 | +0.0002 | 0.0001 | 3 | 1,241,256.601 |
| Be III | 1s.ng 1G J=4 | 5–9 | 5 | 3 | 1/3 | 5.0–9.0 | +0.0002 | 0.0001 | 3 | 1,241,256.601 |
| Be III | 1s.nh 1H* J=5 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0000 | 0.0000 | 3 | 1,241,256.601 |
| Be III * | 1s.ni 1I J=6 | 7–8 | 2 | 1 | no-triple | 7.0–8.0 | +0.0000 | 0.0000 | 3 | 1,241,256.601 |
| Be III | 1s.np 3P* J=1 | 2–10 | 9 | 7 | 5/7 | 2.0–10.0 | +0.0429 | 0.0001 | 3 | 1,241,256.601 |
| Be III | 1s.ns 1S J=0 | 2–10 | 9 | 7 | 4/7 | 1.9–9.9 | +0.0508 | 0.0003 | 3 | 1,241,256.601 |
| Be III | 1s.ns 3S J=1 | 2–10 | 9 | 7 | 5/7 | 1.9–9.9 | +0.1302 | 0.0028 | 3 | 1,241,256.601 |
| Be IV | nd 2D J=3/2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0002 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | nf 2F* J=5/2 | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +0.0001 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | ng 2G J=7/2 | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | +0.0001 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | nh 2H* J=9/2 | 6–10 | 5 | 3 | 3/3 | 6.0–10.0 | +0.0000 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | ni 2I J=11/2 | 7–10 | 4 | 2 | 2/2 | 7.0–10.0 | +0.0000 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | nk 2K* J=13/2 | 8–10 | 3 | 1 | 1/1 | 8.0–10.0 | +0.0000 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | np 2P* J=1/2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0004 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | ns 2S J=1/2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0004 | 0.0000 | 4 | 1,756,018.810 |
| Bi I | (³P₀)ns 2[0] J=1/2 | 7–11 | 5 | 3 | 3/3 | 2.0–6.1 | +4.9036 | 0.0649 | 1 | 58,761.650 |
| Bi I | (³P₀)nd 2[2] J=3/2 | 6–10 | 5 | 3 | 3/3 | 2.7–6.7 | +3.2646 | 0.0470 | 1 | 58,761.650 |
| Bi I | (³P₀)nd 2[2] J=5/2 | 6–9 | 4 | 2 | 2/2 | 2.8–5.8 | +3.2071 | 0.0272 | 1 | 58,761.650 |
| Bi I | (³P₀)np 2[1]° J=1/2 | 7–9 | 3 | 1 | 1/1 | 2.5–4.6 | +4.4712 | 0.0588 | 1 | 58,761.650 |
| Bi II | 6s2.6p.nd (1/2,3/2)* J=1 | 6–14 | 9 | 7 | 2/7 | 2.8–11.0 | +2.9846 | 0.0626 | 2 | 134,720.000 |
| Bi II | 6s2.6p.nd (1/2,3/2)* J=2 | 6–10† | 4 | 2 | no-triple | 2.8–6.9 | +3.1079 | 0.0545 | 2 | 134,720.000 |
| Bi II | 6s2.6p.nd (1/2,5/2)* J=2 | 6–8 | 3 | 1 | 0/1 | 2.9–5.0 | +3.0001 | 0.1072 | 2 | 134,720.000 |
| Bi II | 6s2.6p.nf (1/2,5/2) J=3 | 5–8† | 3 | 1 | no-triple | 3.9–6.8 | +1.1755 | 0.0437 | 2 | 134,720.000 |
| Bi II | 6s2.6p.nf (1/2,7/2) J=4 | 5–8† | 3 | 1 | no-triple | 3.9–6.8 | +1.1468 | 0.0343 | 2 | 134,720.000 |
| Bi II | 6s2.6p.ns (1/2,1/2)* J=0 | 7–9 | 3 | 1 | 1/1 | 2.6–4.7 | +4.3705 | 0.0333 | 2 | 134,720.000 |
| Bi II | 6s2.6p.ns (1/2,1/2)* J=1 | 7–9 | 3 | 1 | 1/1 | 2.6–4.7 | +4.3684 | 0.0313 | 2 | 134,720.000 |
| Bi II * | 6s2.6p.nf (1/2,7/2) J=3 | 5–6 | 2 | 1 | no-triple | 3.9–4.9 | +1.1419 | 0.0039 | 2 | 134,720.000 |
| Bi II * | 6s2.6p.np (1/2,1/2) J=0 | 7–8 | 2 | 1 | no-triple | 3.0–4.1 | +3.9567 | 0.0079 | 2 | 134,720.000 |
| Bi III | 6s2.nd 2D J=3/2 | 6–8 | 3 | 1 | 1/1 | 3.0–5.2 | +2.8926 | 0.0795 | 3 | 206,242.000 |
| Bi III | 6s2.nd 2D J=5/2 | 6–8 | 3 | 1 | 1/1 | 3.1–5.2 | +2.8456 | 0.0496 | 3 | 206,242.000 |
| Bi III | 6s2.ng 2G J=7/2 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0378 | 0.0043 | 3 | 206,242.000 |
| Bi III | 6s2.ng 2G J=9/2 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0383 | 0.0046 | 3 | 206,242.000 |
| Bi III | 6s2.np 2P* J=1/2 | 6–8 | 3 | 1 | 1/1 | 2.2–4.4 | +3.7096 | 0.0732 | 3 | 206,242.000 |
| Bi III | 6s2.np 2P* J=3/2 | 6–8 | 3 | 1 | 1/1 | 2.3–4.5 | +3.6044 | 0.0630 | 3 | 206,242.000 |
| Bi III | 6s2.ns 2S J=1/2 | 7–9 | 3 | 1 | 1/1 | 3.0–5.0 | +3.9869 | 0.0234 | 3 | 206,242.000 |
| Bi III * | 6s2.nh 2H* J=11/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0103 | 0.0005 | 3 | 206,242.000 |
| Bi III * | 6s2.nh 2H* J=9/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0103 | 0.0005 | 3 | 206,242.000 |
| C I * | nd 1F* J=3 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0320 | 0.0059 | 1 | 90,937.500 |
| C I * | nd 3D* J=1 | 3–4 | 2 | 1 | no-triple | 2.9–3.9 | +0.0638 | 0.0097 | 1 | 90,937.500 |
| C I * | np 3D J=1 | 3–4 | 2 | 1 | no-triple | 2.3–3.3 | +0.7201 | 0.0073 | 1 | 90,937.500 |
| C I * | np 3P J=0 | 3–4 | 2 | 1 | no-triple | 2.4–3.4 | +0.6284 | 0.0046 | 1 | 90,937.500 |
| C I * | np 3S J=1 | 3–4 | 2 | 1 | no-triple | 2.3–3.3 | +0.6641 | 0.0048 | 1 | 90,937.500 |
| C I | ns 1P* J=1 | 3–5 | 3 | 1 | 0/1 | 1.9–3.9 | +1.0532 | 0.0037 | 1 | 90,937.500 |
| C I | ns 3P* J=0 | 3–5 | 3 | 1 | 0/1 | 1.9–3.9 | +1.0925 | 0.0127 | 1 | 90,937.500 |
| C II | 2s²ns ²S | 3–8 | 6 | 4 | 4/4 | 2.3–7.3 | +0.6624 | 0.0063 | 2 | 196,664.700 |
| C II | 2s²np ²P° | 3–7 | 5 | 3 | 3/3 | 2.6–6.7 | +0.3928 | 0.1344 | 2 | 196,664.700 |
| C II | 2s²nd ²D | 3–7 | 5 | 3 | 3/3 | 2.9–6.9 | +0.0924 | 0.0645 | 2 | 196,664.700 |
| C II | 2s²nf ²F° | 4–7 | 4 | 2 | 2/2 | 4.0–7.0 | +0.0220 | 0.0069 | 2 | 196,664.700 |
| C II | 2s²ng ²G | 5–7 | 3 | 1 | 1/1 | 5.0–7.0 | +0.0054 | 0.0011 | 2 | 196,664.700 |
| C II | 2s2(1S)np 2P° J=1/2 | 2–4 | 3 | 1 | 0/1 | 1.5–3.6 | +0.4403 | 0.0469 | 2 | 196,664.700 |
| C II | 2s2(1S)np 2P° J=3/2 | 2–4 | 3 | 1 | 0/1 | 1.5–3.6 | +0.4401 | 0.0469 | 2 | 196,664.700 |
| C II * | 2s2(1S)nd 2D J=3/2 | 3–4 | 2 | 1 | no-triple | 2.9–3.9 | +0.0740 | 0.0044 | 2 | 196,664.700 |
| C II * | 2s2(1S)nd 2D J=5/2 | 3–4 | 2 | 1 | no-triple | 2.9–3.9 | +0.0740 | 0.0044 | 2 | 196,664.700 |
| C II * | 2s2(1S)ns 2S J=1/2 | 3–4 | 2 | 1 | no-triple | 2.3–3.3 | +0.6615 | 0.0020 | 2 | 196,664.700 |
| C III | nd 1D J=2 | 3–7 | 5 | 3 | 1/3 | 3.0–7.0 | +0.0067 | 0.0036 | 3 | 386,241.000 |
| C III | nd 3D J=1 | 3–9 | 7 | 5 | 3/5 | 2.9–8.9 | +0.0816 | 0.0069 | 3 | 386,241.000 |
| C III | nf 3F* J=2 | 4–7 | 4 | 2 | 1/2 | 3.9–7.0 | +0.0127 | 0.0398 | 3 | 386,241.000 |
| C III | ng 3G J=3 | 5–7 | 3 | 1 | 1/1 | 5.0–7.0 | +0.0126 | 0.0021 | 3 | 386,241.000 |
| C III | np 1P* J=1 | 3–8 | 6 | 4 | 1/4 | 2.8–7.8 | +0.1806 | 0.0527 | 3 | 386,241.000 |
| C III | np 3P* J=0 | 3–6 | 4 | 2 | 1/2 | 2.8–5.8 | +0.1856 | 0.0217 | 3 | 386,241.000 |
| C III | ns 1S J=0 | 3–5 | 3 | 1 | 1/1 | 2.7–4.5 | +0.3819 | 0.0499 | 3 | 386,241.000 |
| C III | ns 3S J=1 | 3–7 | 5 | 3 | 2/3 | 2.6–6.6 | +0.3993 | 0.0137 | 3 | 386,241.000 |
| C V | 1s.nd 1D J=2 | 3–7 | 5 | 3 | 3/3 | 3.0–7.0 | +0.0108 | 0.0077 | 5 | 3,162,788.800 |
| C V | 1s.nd 3D J=1 | 3–7 | 5 | 3 | 3/3 | 3.0–7.0 | +0.0122 | 0.0078 | 5 | 3,162,788.800 |
| C V | 1s.nf 1F* J=3 | 4–6 | 3 | 1 | 1/1 | 4.0–6.0 | +0.0092 | 0.0042 | 5 | 3,162,788.800 |
| C V | 1s.nf 3F* J=3 | 4–6 | 3 | 1 | 1/1 | 4.0–6.0 | +0.0092 | 0.0041 | 5 | 3,162,788.800 |
| C V | 1s.ng 1G J=4 | 5–7 | 3 | 1 | 1/1 | 5.0–7.0 | +0.0152 | 0.0059 | 5 | 3,162,788.800 |
| C V | 1s.ng 3G J=4 | 5–7 | 3 | 1 | 1/1 | 5.0–7.0 | +0.0153 | 0.0059 | 5 | 3,162,788.800 |
| C V * | 1s.nh 1H* J=5 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0186 | 0.0042 | 5 | 3,162,788.800 |
| C V | 1s.np 1P* J=1 | 2–7 | 6 | 4 | 4/4 | 2.0–7.0 | +0.0002 | 0.0084 | 5 | 3,162,788.800 |
| C V | 1s.np 3P* J=0 | 2–7 | 6 | 4 | 4/4 | 2.0–6.9 | +0.0384 | 0.0075 | 5 | 3,162,788.800 |
| C V | 1s.ns 1S J=0 | 2–7 | 6 | 4 | 4/4 | 2.0–6.9 | +0.0399 | 0.0079 | 5 | 3,162,788.800 |
| C V | 1s.ns 3S J=1 | 2–7 | 6 | 4 | 3/4 | 1.9–6.9 | +0.0927 | 0.0063 | 5 | 3,162,788.800 |
| Ca I | nd 1D J=2 | 4–9 | 6 | 4 | untested | 3.0–8.6 | +0.9084 | 0.2360 | 1 | 49,305.950 |
| Ca I | nd 3D J=1 | 4–9 | 6 | 4 | untested | 3.1–8.4 | +0.8917 | 0.1405 | 1 | 49,305.950 |
| Ca I | nf 1F* J=3 | 4–8 | 5 | 3 | untested | 4.0–7.9 | +0.0654 | 0.0190 | 1 | 49,305.950 |
| Ca I | nf 3F* J=2 | 4–9 | 6 | 4 | untested | 3.9–8.9 | +0.0893 | 0.0059 | 1 | 49,305.950 |
| Ca I | np 1P* J=1 | 5–10 | 6 | 4 | untested | 3.0–8.2 | +1.8902 | 0.1793 | 1 | 49,305.950 |
| Ca I | ns 1S J=0 | 5–11 | 7 | 5 | untested | 2.6–8.7 | +2.3548 | 0.0350 | 1 | 49,305.950 |
| Ca I | ns 3S J=1 | 5–11 | 7 | 5 | untested | 2.5–8.6 | +2.4639 | 0.0227 | 1 | 49,305.950 |
| Ca II | ns 2S J=1/2 | 4–6 | 3 | 1 | 1/1 | 2.1–4.2 | +1.8338 | 0.0183 | 2 | 95,751.880 |
| Ca II | nd 2D J=3/2 | 3–16 | 14 | 12 | untested | 2.3–15.4 | +0.6341 | 0.0154 | 2 | 95,751.870 |
| Ca II | nf 2F* J=5/2 | 4–10 | 7 | 5 | untested | 4.0–10.0 | +0.0248 | 0.0029 | 2 | 95,751.870 |
| Ca II | ng 2G J=7/2 | 5–9 | 5 | 3 | untested | 5.0–9.0 | +0.0048 | 0.0004 | 2 | 95,751.870 |
| Ca II * | nh 2H* J=9/2 | 8–10† | 2 | 1 | untested | 8.0–10.0 | +0.0016 | 0.0000 | 2 | 95,751.870 |
| Ca II | np 2P* J=1/2 | 4–6 | 3 | 1 | untested | 2.5–4.5 | +1.4775 | 0.0207 | 2 | 95,751.870 |
| Ca II | ns 2S J=1/2 | 4–10 | 7 | 5 | untested | 2.1–8.2 | +1.8192 | 0.0175 | 2 | 95,751.870 |
| Ca IX | nd 1D J=2 | 4–6 | 3 | 1 | 0/1 | 3.9–5.8 | +0.1572 | 0.0090 | 9 | 1,520,640.000 |
| Ca IX * | nf 1F* J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0124 | 0.0050 | 9 | 1,520,640.000 |
| Ca IX | np 1P* J=1 | 4–6 | 3 | 1 | 0/1 | 3.6–5.6 | +0.4121 | 0.0041 | 9 | 1,520,640.000 |
| Ca IX * | ns 3S J=1 | 4–5 | 2 | 1 | no-triple | 3.4–4.4 | +0.5725 | 0.0078 | 9 | 1,520,640.000 |
| Cd I | nd 1D J=2 | 5–15† | 10 | 8 | 5/6 | 2.9–12.8 | +2.1886 | 0.0288 | 1 | 72,540.050 |
| Cd I | nd 3D J=1 | 5–11 | 7 | 5 | 5/5 | 2.9–8.9 | +2.0898 | 0.0049 | 1 | 72,540.050 |
| Cd I | nf 3F* J=3 | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +0.0346 | 0.0034 | 1 | 72,540.050 |
| Cd I | np 1P* J=1 | 6–12 | 7 | 5 | 3/5 | 2.9–8.9 | +3.0515 | 0.0005 | 1 | 72,540.050 |
| Cd I | np 3P* J=0 | 6–10 | 5 | 3 | 3/3 | 2.8–6.8 | +3.1814 | 0.0184 | 1 | 72,540.050 |
| Cd I | ns 1S J=0 | 6–15 | 10 | 8 | 5/8 | 2.4–11.4 | +3.5926 | 0.0131 | 1 | 72,540.050 |
| Cd I | ns 3S J=1 | 6–16 | 11 | 9 | 7/9 | 2.3–12.3 | +3.6677 | 0.0188 | 1 | 72,540.050 |
| Cd II | nd 2D J=3/2 | 5–13 | 9 | 7 | 7/7 | 3.1–11.1 | +1.8942 | 0.0159 | 2 | 136,374.740 |
| Cd II | nf 2F* J=5/2 | 4–9 | 6 | 4 | 4/4 | 4.0–8.9 | +0.0489 | 0.0092 | 2 | 136,374.740 |
| Cd II | ng 2G J=7/2 | 5–11 | 7 | 5 | 4/5 | 5.0–11.0 | +0.0076 | 0.0004 | 2 | 136,374.740 |
| Cd II | np 2P* J=1/2 | 5–12† | 7 | 5 | 2/3 | 2.2–9.3 | +2.7444 | 0.0319 | 2 | 136,374.740 |
| Cd II | ns 2S J=1/2 | 5–13 | 9 | 7 | 7/7 | 1.8–9.9 | +3.1175 | 0.0330 | 2 | 136,374.740 |
| F I | nd 4D J=7/2 | 3–6 | 4 | 2 | 1/2 | 3.0–6.0 | +0.0323 | 0.0008 | 1 | 140,518.700 |
| F I | nd 4F J=9/2 | 3–6 | 4 | 2 | 1/2 | 3.0–6.0 | +0.0149 | 0.0012 | 1 | 140,518.700 |
| F I * | np 4D* J=7/2 | 3–4 | 2 | 1 | no-triple | 2.2–3.2 | +0.8308 | 0.0097 | 1 | 140,518.700 |
| F I | ns 2P J=3/2 | 3–6 | 4 | 2 | 2/2 | 1.8–4.9 | +1.1857 | 0.0604 | 1 | 140,518.700 |
| F I | ns 4P J=5/2 | 3–8 | 6 | 4 | 4/4 | 1.7–6.7 | +1.2800 | 0.0117 | 1 | 140,518.700 |
| Fe XV * | nd 3D J=1 | 4–5 | 2 | 1 | no-triple | 3.9–4.9 | +0.1278 | 0.0017 | 15 | 3,679,500.000 |
| Fe XV | nf 1F* J=3 | 4–6 | 3 | 1 | 1/1 | 4.0–6.5 | -0.2367 | 0.2030 | 15 | 3,679,500.000 |
| Fe XV * | nf 3F* J=2 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0371 | 0.0016 | 15 | 3,679,500.000 |
| Fe XV * | np 1P* J=1 | 4–5 | 2 | 1 | no-triple | 3.7–4.7 | +0.2872 | 0.0017 | 15 | 3,679,500.000 |
| Fe XVI | nd 2D J=3/2 | 3–8 | 6 | 4 | 4/4 | 2.9–7.9 | +0.0750 | 0.0031 | 16 | 3,946,570.000 |
| Fe XVI | nf 2F* J=5/2 | 4–8 | 5 | 3 | 3/3 | 4.0–8.0 | +0.0116 | 0.0036 | 16 | 3,946,570.000 |
| Fe XVI | np 2P* J=1/2 | 3–6 | 4 | 2 | 2/2 | 2.8–5.8 | +0.2233 | 0.0059 | 16 | 3,946,570.000 |
| Fe XVI | ns 2S J=1/2 | 3–7 | 5 | 3 | 3/3 | 2.7–6.7 | +0.3174 | 0.0152 | 16 | 3,946,570.000 |
| Ga I | 4s²ns ²S | 5–28 | 24 | 22 | 22/22 | 2.2–25.2 | +2.8013 | 0.0535 | 1 | 48,387.634 |
| Ga I | 4s²nd ²D | 4–27 | 23 | 21 | 21/21 | 2.8–25.7 | +1.2926 | 0.1920 | 1 | 48,387.634 |
| Ga I | 4s²np ²P° high | 41–55 | 15 | 13 | 13/13 | 38.8–52.7 | +2.2107 | 0.1209 | 1 | 48,387.634 |
| Ga I | 4s²nf ²F° | 4–8 | 5 | 3 | 3/3 | 4.0–8.0 | +0.0252 | 0.0057 | 1 | 48,387.634 |
| Ga I | 4s²np ²P° low | 4–7 | 4 | 2 | 2/2 | 1.5–4.7 | +2.3450 | 0.2026 | 1 | 48,387.634 |
| Ga II | nd 1D J=2 | 4–7 | 4 | 2 | 2/2 | 3.3–6.1 | +0.8475 | 0.1127 | 2 | 165,465.800 |
| Ga II | nd 3D J=1 | 4–7 | 4 | 2 | 2/2 | 2.9–5.9 | +1.0630 | 0.0133 | 2 | 165,465.800 |
| Ga II | nf 1F* J=3 | 4–7 | 4 | 2 | 2/2 | 4.0–6.9 | +0.0598 | 0.0070 | 2 | 165,465.800 |
| Ga II | nf 3F* J=2 | 4–7 | 4 | 2 | 2/2 | 3.9–6.9 | +0.0617 | 0.0080 | 2 | 165,465.800 |
| Ga II | ng (1/2,7/2) J=3 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0146 | 0.0012 | 2 | 165,465.800 |
| Ga II | ng (1/2,9/2) J=5 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0142 | 0.0010 | 2 | 165,465.800 |
| Ga II | ns 1S J=0 | 5–8 | 4 | 2 | 1/2 | 2.7–5.8 | +2.2610 | 0.0138 | 2 | 165,465.800 |
| Ga II | ns 3S J=1 | 5–8 | 4 | 2 | 2/2 | 2.6–5.7 | +2.3228 | 0.0169 | 2 | 165,465.800 |
| Ge III | nd 1D J=2 | 4–6 | 3 | 1 | 1/1 | 3.2–5.1 | +0.8820 | 0.0572 | 3 | 274,693.000 |
| Ge III | nd 3D J=1 | 4–6 | 3 | 1 | 1/1 | 3.0–5.0 | +1.0025 | 0.0189 | 3 | 274,693.000 |
| Ge III * | ng 3G J=3 | 5–6 | 2 | 1 | no-triple | 5.0–6.0 | +0.0181 | 0.0010 | 3 | 274,693.000 |
| Ge III | ns 1S J=0 | 5–7 | 3 | 1 | 1/1 | 3.0–5.0 | +2.0116 | 0.0057 | 3 | 274,693.000 |
| Ge III | ns 3S J=1 | 5–8 | 4 | 2 | 2/2 | 2.9–6.0 | +2.0576 | 0.0162 | 3 | 274,693.000 |
| He I | 1sns ³S | 2–35 | 25 | 23 | 23/23 | 1.7–34.7 | +0.2965 | 0.0164 | 1 | 198,310.666 |
| He I | 1sns ¹S | 2–35 | 25 | 23 | 23/23 | 1.9–34.9 | +0.1392 | 0.0118 | 1 | 198,310.666 |
| He I | 1snp ¹P° | 2–35 | 25 | 23 | 23/23 | 2.0–35.0 | -0.0133 | 0.0050 | 1 | 198,310.666 |
| He I | 1snd ¹D | 3–35 | 24 | 22 | 22/22 | 3.0–35.0 | +0.0007 | 0.0019 | 1 | 198,310.666 |
| He I | 1snf ¹F° | 4–35 | 23 | 21 | 21/21 | 4.0–35.0 | -0.0010 | 0.0020 | 1 | 198,310.666 |
| He I | 1snd ³D | 3–35 | 22 | 20 | 20/20 | 3.0–35.0 | +0.0014 | 0.0018 | 1 | 198,310.666 |
| He I | 1sng ¹G | 5–35 | 22 | 20 | 20/20 | 5.0–35.0 | -0.0014 | 0.0020 | 1 | 198,310.666 |
| He I | 1snh ¹H° | 6–35 | 21 | 19 | 19/19 | 6.0–35.0 | -0.0015 | 0.0020 | 1 | 198,310.666 |
| He I | 1sni ¹I | 7–35 | 20 | 18 | 18/18 | 7.0–35.0 | -0.0016 | 0.0019 | 1 | 198,310.666 |
| He II | ns | 1–10 | 10 | 8 | 8/8 | 1.0–10.0 | +7.6e-05 | 2e-05 | 2 | 438,908.871 |
| He II | np | 2–10 | 9 | 7 | 7/7 | 2.0–10.0 | +5.1e-05 | 8e-06 | 2 | 438,908.871 |
| He II | nd | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +2.5e-05 | 4e-06 | 2 | 438,908.871 |
| He II | nf | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +1.4e-05 | 2e-06 | 2 | 438,908.871 |
| He II | ng | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | +8.6e-06 | 1e-06 | 2 | 438,908.871 |
| He II | nh | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +4.5e-06 | 4e-07 | 2 | 438,908.871 |
| He II | ni | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +1.6e-06 | 4e-07 | 2 | 438,908.871 |

*He II's seven rows print δ in exponent form because the series lies below the table's four decimals. They are the corrected series (register 1758): term values against the limit 438,908.871 cm⁻¹ with the reduced-mass Rydberg R_He = R∞/(1 + mₑ/M_He), each level taken as the J-centroid of its fine-structure pair, from the NIST ASD levels; the earlier rows, −0.0003 to −0.0005 and rising, were the same levels against R∞, which is the uncorrected series §24.4 replaced.*
| Hg II | nd 2D J=3/2 | 6–11 | 6 | 4 | 4/4 | 3.1–8.1 | +2.8758 | 0.0227 | 2 | 151,269.200 |
| Hg II | nf 2F* J=7/2 | 5–8 | 4 | 2 | 2/2 | 4.0–6.9 | +1.0622 | 0.0083 | 2 | 151,269.200 |
| Hg II | ng 2G J=9/2 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0053 | 0.0028 | 2 | 151,269.200 |
| Hg II | np 2P* J=1/2 | 6–8 | 3 | 1 | 1/1 | 2.1–4.2 | +3.8196 | 0.0624 | 2 | 151,269.200 |
| Hg II | ns 2S J=1/2 | 6–11 | 6 | 4 | 4/4 | 1.7–6.8 | +4.1850 | 0.0515 | 2 | 151,269.200 |
| K I | nd 2D J=5/2 | 3–13 | 11 | 9 | 9/9 | 2.9–12.7 | +0.2460 | 0.0380 | 1 | 35,010.600 |
| K I | nf 2F* J=5/2 | 4–12 | 9 | 7 | 7/7 | 4.0–12.0 | +0.0112 | 0.0030 | 1 | 35,010.600 |
| K I | np 2P* J=1/2 | 4–15 | 12 | 10 | 9/10 | 2.2–13.3 | +1.7268 | 0.0133 | 1 | 35,010.600 |
| K I | ns 2S J=1/2 | 4–18 | 15 | 13 | 12/13 | 1.8–15.8 | +2.1912 | 0.0111 | 1 | 35,010.600 |
| K II | 3p⁵nf 2[3/2] J=1 | 4–6 | 3 | 1 | 1/1 | 4.0–6.0 | +0.0426 | 0.0069 | 2 | 255,072.800 |
| K II | 3p⁵nf 2[9/2] J=5 | 4–6 | 3 | 1 | 1/1 | 4.0–6.0 | +0.0336 | 0.0071 | 2 | 255,072.800 |
| K II | 3p⁵nf 2[5/2] J=3 | 4–6 | 3 | 1 | 1/1 | 4.0–6.0 | +0.0242 | 0.0052 | 2 | 255,072.800 |
| K II | 3p⁵nf 2[7/2] J=4 | 4–6 | 3 | 1 | 1/1 | 4.0–6.0 | +0.0143 | 0.0059 | 2 | 255,072.800 |
| Li I | np 2P° | 2–42 | 41 | 39 | 39/39 | 2.0–41.8 | +0.1477 | 0.6779 | 1 | 43,487.114 |
| Li I | ns 2S | 2–11 | 10 | 8 | 8/8 | 1.6–10.6 | +0.4014 | 0.0180 | 1 | 43,487.114 |
| Li I | nd 2D | 3–12 | 10 | 8 | 8/8 | 3.0–12.0 | +0.0031 | 0.0129 | 1 | 43,487.114 |
| Li I | np 2P° J=1/2 | 2–4 | 3 | 1 | 1/1 | 2.0–4.0 | +0.0436 | 0.0021 | 1 | 43,487.150 |
| Li I | np 2P° J=3/2 | 2–4 | 3 | 1 | 1/1 | 2.0–4.0 | +0.0436 | 0.0021 | 1 | 43,487.150 |
| Li I * | nd 2D J=3/2 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0016 | 0.0001 | 1 | 43,487.150 |
| Li I * | nd 2D J=5/2 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0016 | 0.0001 | 1 | 43,487.150 |
| Li I * | ns 2S J=1/2 | 2–3 | 2 | 1 | no-triple | 1.6–2.6 | +0.4077 | 0.0038 | 1 | 43,487.150 |
| Li II | 1s.nd 1D J=2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0011 | 0.0001 | 2 | 610,078.400 |
| Li II | 1s.nd 3D J=2 | 3–10 | 8 | 6 | 5/6 | 3.0–10.0 | +0.0027 | 0.0003 | 2 | 610,078.400 |
| Li II | 1s.nf 1F* J=3 | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +0.0000 | 0.0002 | 2 | 610,078.400 |
| Li II | 1s.nf 3F* J=3 | 4–10 | 7 | 5 | 4/5 | 4.0–10.0 | +0.0006 | 0.0002 | 2 | 610,078.400 |
| Li II | 1s.ng 1G J=4 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0000 | 0.0000 | 2 | 610,078.400 |
| Li II | 1s.nh 1H* J=5 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | -0.0000 | 0.0000 | 2 | 610,078.400 |
| Li II | 1s.np 1P* J=1 | 2–14 | 13 | 11 | 7/11 | 2.0–14.0 | -0.0144 | 0.0014 | 2 | 610,078.400 |
| Li II | 1s.np 3P* J=1 | 2–10 | 9 | 7 | 7/7 | 1.9–9.9 | +0.0543 | 0.0004 | 2 | 610,078.400 |
| Li II | 1s.ns 1S J=0 | 2–10 | 9 | 7 | 5/7 | 1.9–9.9 | +0.0744 | 0.0010 | 2 | 610,078.400 |
| Li II | 1s.ns 3S J=1 | 2–10 | 9 | 7 | 7/7 | 1.8–9.8 | +0.1814 | 0.0035 | 2 | 610,078.400 |
| Li II * | 1s.ni 1I J=6 | 7–8 | 2 | 1 | no-triple | 7.0–8.0 | -0.0001 | 0.0000 | 2 | 610,078.400 |
| Li II * | 1s.np 3P* J=0 | 2–3 | 2 | 1 | no-triple | 1.9–2.9 | +0.0537 | 0.0004 | 2 | 610,078.400 |
| Li II * | 1s.np 3P* J=2 | 2–3 | 2 | 1 | no-triple | 1.9–2.9 | +0.0537 | 0.0004 | 2 | 610,078.400 |
| Li III | nd 2D J=3/2 | 3–9 | 7 | 5 | 4/5 | 3.0–9.0 | +0.0003 | 0.0002 | 3 | 987,662.290 |
| Li III | nd 2D J=5/2 | 3–9 | 7 | 5 | 4/5 | 3.0–9.0 | +0.0002 | 0.0002 | 3 | 987,662.290 |
| Li III | nf 2F* J=5/2 | 4–9 | 6 | 4 | 4/4 | 4.0–9.0 | +0.0003 | 0.0002 | 3 | 987,662.290 |
| Li III | nf 2F* J=7/2 | 4–9 | 6 | 4 | 4/4 | 4.0–9.0 | +0.0002 | 0.0002 | 3 | 987,662.290 |
| Li III | ng 2G J=7/2 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0003 | 0.0001 | 3 | 987,662.290 |
| Li III | ng 2G J=9/2 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0003 | 0.0001 | 3 | 987,662.290 |
| Li III | nh 2H* J=11/2 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0003 | 0.0001 | 3 | 987,662.290 |
| Li III | nh 2H* J=9/2 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0003 | 0.0001 | 3 | 987,662.290 |
| Li III | ni 2I J=11/2 | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0004 | 0.0001 | 3 | 987,662.290 |
| Li III | ni 2I J=13/2 | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0004 | 0.0001 | 3 | 987,662.290 |
| Li III | np 2P* J=1/2 | 2–10 | 9 | 7 | 5/7 | 2.0–10.0 | +0.0004 | 0.0002 | 3 | 987,662.290 |
| Li III | np 2P* J=3/2 | 2–10 | 9 | 7 | 5/7 | 2.0–10.0 | +0.0003 | 0.0002 | 3 | 987,662.290 |
| Li III | ns 2S J=1/2 | 1–9 | 9 | 7 | 5/7 | 1.0–9.0 | +0.0003 | 0.0002 | 3 | 987,662.290 |
| Li III * | nk 2K* J=13/2 | 8–9 | 2 | 1 | no-triple | 8.0–9.0 | +0.0004 | 0.0001 | 3 | 987,662.290 |
| Li III * | nk 2K* J=15/2 | 8–9 | 2 | 1 | no-triple | 8.0–9.0 | +0.0004 | 0.0001 | 3 | 987,662.290 |
| Mg I | 3snd 1D J=2 | 3–5 | 3 | 1 | 1/1 | 2.7–4.5 | +0.4034 | 0.0647 | 1 | 61,671.050 |
| Mg I | 3snd 3D J=1 | 3–5 | 3 | 1 | 1/1 | 2.8–4.8 | +0.1701 | 0.0009 | 1 | 61,671.050 |
| Mg I | 3snd 3D J=2 | 3–5 | 3 | 1 | 1/1 | 2.8–4.8 | +0.1701 | 0.0008 | 1 | 61,671.050 |
| Mg I | 3snd 3D J=3 | 3–5 | 3 | 1 | 1/1 | 2.8–4.8 | +0.1701 | 0.0008 | 1 | 61,671.050 |
| Mg I | 3snp 1P° J=1 | 3–6 | 4 | 2 | 2/2 | 2.0–5.0 | +1.0135 | 0.0265 | 1 | 61,671.050 |
| Mg I | 3snp 3P° J=0 | 3–6 | 4 | 2 | 2/2 | 1.7–4.9 | +1.2056 | 0.0789 | 1 | 61,671.050 |
| Mg I | 3snp 3P° J=1 | 3–6 | 4 | 2 | 2/2 | 1.7–4.9 | +1.2052 | 0.0789 | 1 | 61,671.050 |
| Mg I | 3snp 3P° J=2 | 3–6 | 4 | 2 | 2/2 | 1.7–4.9 | +1.2045 | 0.0788 | 1 | 61,671.050 |
| Mg I | 3sns 1S J=0 | 4–6 | 3 | 1 | 1/1 | 2.5–4.5 | +1.5331 | 0.0067 | 1 | 61,671.050 |
| Mg I | 3sns 3S J=1 | 4–6 | 3 | 1 | 1/1 | 2.3–4.4 | +1.6603 | 0.0180 | 1 | 61,671.050 |
| Mg I * | 3snf 1F° J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0413 | 0.0022 | 1 | 61,671.050 |
| Mg I * | 3snf 3F° J=2 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0413 | 0.0022 | 1 | 61,671.050 |
| Mg I * | 3snf 3F° J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0413 | 0.0022 | 1 | 61,671.050 |
| Mg I * | 3snf 3F° J=4 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0413 | 0.0022 | 1 | 61,671.050 |
| Mg II | ns ²S | 3–10 | 8 | 6 | 6/6 | 1.9–8.9 | +1.0749 | 0.0289 | 2 | 121,267.640 |
| Mg II | nd ²D | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0411 | 0.0145 | 2 | 121,267.640 |
| Mg II | np ²P° | 3–9 | 7 | 5 | 5/5 | 2.3–8.3 | +0.7077 | 0.0361 | 2 | 121,267.640 |
| Mg II | nf ²F° | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +0.0030 | 0.0009 | 2 | 121,267.640 |
| Mg II | ng ²G | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | +0.0007 | 0.0001 | 2 | 121,267.640 |
| Mg II | nh ²H° | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0002 | 0.0000 | 2 | 121,267.640 |
| Mg II | ni ²I | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0000 | 0.0000 | 2 | 121,267.640 |
| Mg II | np 2P° J=1/2 | 3–5 | 3 | 1 | 1/1 | 2.3–4.3 | +0.7187 | 0.0123 | 2 | 121,267.640 |
| Mg II | np 2P° J=3/2 | 3–5 | 3 | 1 | 1/1 | 2.3–4.3 | +0.7174 | 0.0123 | 2 | 121,267.640 |
| Mg II | ns 2S J=1/2 | 3–6 | 4 | 2 | 2/2 | 1.9–4.9 | +1.0806 | 0.0102 | 2 | 121,267.640 |
| Mg II * | nd 2D J=3/2 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0340 | 0.0036 | 2 | 121,267.640 |
| Mg II * | nd 2D J=5/2 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0340 | 0.0036 | 2 | 121,267.640 |
| Mg III * | nd 2[1/2]* J=1 | 4–5 | 2 | 1 | no-triple | 3.9–4.9 | +0.0934 | 0.0014 | 3 | 646,402.000 |
| Mg III | nd 2[3/2]* J=1 | 4–9 | 6 | 4 | 1/4 | 4.0–9.0 | +0.0388 | 0.0017 | 3 | 646,402.000 |
| Mg III * | nf 2[3/2] J=1 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0111 | 0.0005 | 3 | 646,402.000 |
| Mg III * | nf 2[3/2] J=2 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0108 | 0.0004 | 3 | 646,402.000 |
| Mg III * | nf 2[5/2] J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0039 | 0.0003 | 3 | 646,402.000 |
| Mg III * | nf 2[7/2] J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0000 | 0.0004 | 3 | 646,402.000 |
| Mg III * | nf 2[7/2] J=4 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | -0.0000 | 0.0004 | 3 | 646,402.000 |
| Mg III * | nf 2[9/2] J=4 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0073 | 0.0004 | 3 | 646,402.000 |
| Mg III * | nf 2[9/2] J=5 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0073 | 0.0004 | 3 | 646,402.000 |
| Mg III | ns 2[3/2]* J=1 | 4–6 | 3 | 1 | 1/1 | 3.1–5.2 | +0.8487 | 0.0050 | 3 | 646,402.000 |
| Mg III * | ns 2[3/2]* J=2 | 4–5 | 2 | 1 | no-triple | 3.1–4.1 | +0.8634 | 0.0030 | 3 | 646,402.000 |
| N I | nd 2F J=5/2 | 3–5 | 3 | 1 | 1/1 | 3.0–5.0 | +0.0273 | 0.0024 | 1 | 117,244.100 |
| N I * | nd 4D J=1/2 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0041 | 0.0041 | 1 | 117,244.100 |
| N I | nd 4F J=3/2 | 3–5 | 3 | 1 | 0/1 | 3.0–4.9 | +0.0514 | 0.0035 | 1 | 117,244.100 |
| N I | np 2D* J=3/2 | 3–5 | 3 | 1 | 0/1 | 2.3–4.5 | +0.6233 | 0.0955 | 1 | 117,244.100 |
| N I | np 4D* J=1/2 | 3–5 | 3 | 1 | 1/1 | 2.2–4.2 | +0.7714 | 0.0136 | 1 | 117,244.100 |
| N I | np 4P* J=1/2 | 3–5 | 3 | 1 | 1/1 | 2.2–4.3 | +0.7329 | 0.0169 | 1 | 117,244.100 |
| N I | ns 2P J=1/2 | 3–6 | 4 | 2 | 2/2 | 1.9–4.9 | +1.1040 | 0.0116 | 1 | 117,244.100 |
| N I | ns 4P J=1/2 | 3–6 | 4 | 2 | 2/2 | 1.8–4.8 | +1.1697 | 0.0190 | 1 | 117,244.100 |
| N II | 2p·ns ³P° J=0 | 3–6 | 4 | 2 | 2/2 | 2.2–5.2 | +0.7747 | 0.0264 | 2 | 238,750.500 |
| N II | 2p·ns ³P° J=1 | 3–6 | 4 | 2 | 2/2 | 2.2–5.2 | +0.7731 | 0.0260 | 2 | 238,750.500 |
| N II | 2p·ns ³P° J=2 | 3–6 | 4 | 2 | 2/2 | 2.2–5.3 | +0.7633 | 0.0464 | 2 | 238,750.500 |
| N II | 2p·ns ¹P° J=1 | 3–6 | 4 | 2 | 2/2 | 2.2–5.3 | +0.7325 | 0.0824 | 2 | 238,750.500 |
| N III | nd 2D J=3/2 | 3–12 | 10 | 8 | 5/8 | 2.9–11.9 | +0.0737 | 0.0124 | 3 | 382,672.000 |
| N III | nf 2F* J=5/2 | 4–7 | 4 | 2 | 2/2 | 4.0–7.0 | +0.0281 | 0.0048 | 3 | 382,672.000 |
| N III | ng 2G J=7/2 | 5–7 | 3 | 1 | 1/1 | 5.0–7.0 | +0.0022 | 0.0009 | 3 | 382,672.000 |
| N III * | nh 2H* J=9/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | -0.0026 | 0.0009 | 3 | 382,672.000 |
| N III | np 2P* J=1/2 | 3–5 | 3 | 1 | 0/1 | 2.7–4.7 | +0.2917 | 0.0185 | 3 | 382,672.000 |
| N III | ns 2S J=1/2 | 3–14 | 12 | 10 | 9/10 | 2.5–13.3 | +0.5660 | 0.0740 | 3 | 382,672.000 |
| Na I | ns | 3–20 | 18 | 16 | 16/16 | 1.6–18.7 | +1.3506 | 0.0250 | 1 | 41,449.451 |
| Na I | np | 3–20 | 18 | 16 | 16/16 | 2.1–19.1 | +0.8584 | 0.0279 | 1 | 41,449.451 |
| Na I | nd | 3–20 | 18 | 16 | 16/16 | 3.0–20.0 | +0.0141 | 0.0045 | 1 | 41,449.451 |
| Na I | nf | 4–20 | 17 | 15 | 15/15 | 4.0–20.0 | +0.0014 | 0.0004 | 1 | 41,449.451 |
| Na I | ng | 5–20 | 16 | 14 | 14/14 | 5.0–20.0 | +0.0003 | 0.0001 | 1 | 41,449.451 |
| Na I | nh | 6–10 | 5 | 3 | 3/3 | 6.0–10.0 | +0.0000 | 0.0000 | 1 | 41,449.451 |
| Na II | (²P°₃⁄₂)ns 2[3/2]° J=2 | 3–6 | 4 | 2 | 2/2 | 1.9–5.0 | +1.0385 | 0.0284 | 2 | 381,390.200 |
| Na II | (²P°₃⁄₂)ns 2[3/2]° J=1 | 3–6 | 4 | 2 | 2/2 | 1.9–5.0 | +1.0268 | 0.0371 | 2 | 381,390.200 |
| Na II | (²P°₃⁄₂)nd 2[1/2]° J=0 | 3–5 | 3 | 1 | 1/1 | 2.9–4.9 | +0.0671 | 0.0083 | 2 | 381,390.200 |
| Na II | (²P°₃⁄₂)nd 2[1/2]° J=1 | 3–5 | 3 | 1 | 1/1 | 2.9–4.9 | +0.0641 | 0.0085 | 2 | 381,390.200 |
| Na II | (²P°₃⁄₂)nd 2[3/2]° J=2 | 3–5 | 3 | 1 | 1/1 | 2.9–4.9 | +0.0556 | 0.0027 | 2 | 381,390.200 |
| Na II | (²P°₃⁄₂)nd 2[3/2]° J=1 | 3–5 | 3 | 1 | 1/1 | 3.0–5.0 | +0.0268 | 0.0026 | 2 | 381,390.200 |
| Ne I | 2s22p5(2P*3/2)nd 2[3/2]* J=1 | 13–20 | 8 | 6 | 2/6 | 13.0–20.0 | +0.0154 | 0.0024 | 1 | 173,929.750 |
| Ne I | 2s22p5(2P*3/2)ns 2[3/2]* J=1 | 12–20 | 9 | 7 | 4/7 | 10.7–18.7 | +1.2923 | 0.0047 | 1 | 173,929.750 |
| Ne I | 2s2.2p5.(2P*<1/2>).nd 2[3/2]* J=1 | 11–20 | 10 | 8 | untested | 11.0–20.0 | +0.0119 | 0.0043 | 1 | 174,710.090 |
| Ne I | 2s2.2p5.(2P*<1/2>).ns 2[1/2]* J=1 | 11–20 | 10 | 8 | untested | 9.7–18.7 | +1.2974 | 0.0038 | 1 | 174,710.090 |
| Ne I | 2s.2p6.(2S).np 1P* J=1 | 3–12 | 10 | 8 | untested | 2.2–11.1 | +0.8409 | 0.0191 | 1 | 390,977.350 |
| Ne I * | 2p5(2P°3/2)nd 2[7/2]° J=4 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0193 | 0.0014 | 1 | 173,929.750 |
| Ne I * | 2p5(2P°3/2)ns 2[3/2]° J=2 | 3–4 | 2 | 1 | no-triple | 1.7–2.7 | +1.3329 | 0.0085 | 1 | 173,929.750 |
| Ne II | 2s2.2p4.(3P).nd 4D J=3/2 | 3–6 | 4 | 2 | untested | 2.9–5.9 | +0.0700 | 0.0012 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).nd 4D J=5/2 | 3–6 | 4 | 2 | untested | 2.9–5.9 | +0.0773 | 0.0036 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).nd 4D J=7/2 | 3–6 | 4 | 2 | untested | 2.9–5.9 | +0.0813 | 0.0047 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).nd 4F J=9/2 | 3–6 | 4 | 2 | untested | 3.0–5.9 | +0.0547 | 0.0070 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).ns 2P J=1/2 | 3–7 | 5 | 3 | untested | 2.0–6.3 | +0.8636 | 0.0857 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).ns 2P J=3/2 | 3–7 | 5 | 3 | untested | 2.0–6.0 | +0.9480 | 0.0143 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).ns 4P J=1/2 | 3–7 | 5 | 3 | untested | 2.0–6.2 | +0.9132 | 0.0743 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).ns 4P J=3/2 | 3–7 | 5 | 3 | untested | 2.0–6.2 | +0.9261 | 0.0730 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).ns 4P J=5/2 | 3–7 | 5 | 3 | untested | 2.0–6.0 | +0.9906 | 0.0125 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(1D).nd 2S J=1/2 | 3–8 | 6 | 4 | untested | 3.0–7.9 | +0.0701 | 0.0422 | 2 | 356,229.300 |
| Ne II | 2s2.2p4.(1D).ns 2D J=3/2 | 3–5 | 3 | 1 | untested | 2.0–4.0 | +0.9850 | 0.0115 | 2 | 356,229.300 |
| Ne II | 2s2.2p4.(1D).ns 2D J=5/2 | 3–5 | 3 | 1 | untested | 2.0–4.0 | +0.9850 | 0.0115 | 2 | 356,229.300 |
| Ne II | 2s2.2p4.(3P).np 2D* J=3/2 | 3–6 | 4 | 2 | untested | 2.4–5.5 | +0.5651 | 0.0645 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).np 2D* J=5/2 | 3–6 | 4 | 2 | untested | 2.4–5.4 | +0.6294 | 0.0117 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).np 2S* J=1/2 | 3–6 | 4 | 2 | untested | 2.4–5.4 | +0.6010 | 0.0199 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).np 4D* J=1/2 | 3–6 | 4 | 2 | untested | 2.3–5.5 | +0.5916 | 0.0576 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).np 4D* J=5/2 | 3–6 | 4 | 2 | untested | 2.3–5.5 | +0.6055 | 0.0551 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).np 4D* J=7/2 | 3–6 | 4 | 2 | untested | 2.3–5.4 | +0.6541 | 0.0133 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).np 4P* J=1/2 | 3–6 | 4 | 2 | untested | 2.3–5.4 | +0.6430 | 0.0585 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).np 4P* J=3/2 | 3–6 | 4 | 2 | untested | 2.3–5.3 | +0.6767 | 0.0235 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).np 4P* J=5/2 | 3–6 | 4 | 2 | untested | 2.3–5.3 | +0.6884 | 0.0174 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).np 4S* J=3/2 | 3–6 | 4 | 2 | untested | 2.4–5.5 | +0.5679 | 0.0424 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).nf 2[2]* J=5/2 | 5–8 | 4 | 2 | untested | 5.0–8.0 | +0.0039 | 0.0001 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).nf 2[3]* J=7/2 | 5–8 | 4 | 2 | untested | 5.0–8.0 | +0.0086 | 0.0001 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).nf 2[4]* J=7/2 | 5–8 | 4 | 2 | untested | 5.0–8.0 | +0.0096 | 0.0002 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).nf 2[4]* J=9/2 | 5–8 | 4 | 2 | untested | 5.0–8.0 | +0.0098 | 0.0002 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).nf 2[5]* J=11/2 | 5–8 | 4 | 2 | untested | 5.0–8.0 | +0.0025 | 0.0003 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).ng 2[2] J=3/2 | 5–7 | 3 | 1 | untested | 5.0–7.0 | -0.0016 | 0.0001 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).ng 2[3] J=5/2 | 5–7 | 3 | 1 | untested | 5.0–7.0 | +0.0010 | 0.0001 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).ng 2[4] J=7/2 | 5–7 | 3 | 1 | untested | 5.0–7.0 | +0.0029 | 0.0001 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).ng 2[5] J=9/2 | 5–7 | 3 | 1 | untested | 5.0–7.0 | +0.0030 | 0.0001 | 2 | 330,388.600 |
| Ne II | 2s2.2p4.(3P).ng 2[6] J=11/2 | 5–7 | 3 | 1 | untested | 5.0–7.0 | -0.0002 | 0.0001 | 2 | 330,388.600 |
| Ne II * | 2s2.2p4.(1D).nd 2F J=5/2 | 3–4 | 2 | 1 | untested | 3.0–4.0 | +0.0289 | 0.0055 | 2 | 356,229.300 |
| Ne II * | 2s2.2p4.(1D).nd 2F J=7/2 | 3–4 | 2 | 1 | untested | 3.0–4.0 | +0.0289 | 0.0055 | 2 | 356,229.300 |
| Ne II * | 2s2.2p4.(1D).nd 2G J=7/2 | 3–4 | 2 | 1 | untested | 2.9–3.9 | +0.0674 | 0.0050 | 2 | 356,229.300 |
| Ne II * | 2s2.2p4.(1D).nd 2G J=9/2 | 3–4 | 2 | 1 | untested | 2.9–3.9 | +0.0674 | 0.0050 | 2 | 356,229.300 |
| Ne II * | 2s2.2p4.(1D).nd 2P J=3/2 | 3–4 | 2 | 1 | untested | 2.9–3.9 | +0.0605 | 0.0040 | 2 | 356,229.300 |
| O III | nd 1D* J=2 | 3–5 | 3 | 1 | 1/1 | 2.9–4.9 | +0.1196 | 0.0040 | 3 | 443,325.200 |
| O III * | nd 3D* J=1 | 3–4 | 2 | 1 | no-triple | 2.9–3.9 | +0.0791 | 0.0043 | 3 | 443,325.200 |
| O III | nd 3F* J=2 | 3–5 | 3 | 1 | 1/1 | 2.9–4.9 | +0.1290 | 0.0090 | 3 | 443,325.200 |
| O III * | np 3D J=1 | 3–4 | 2 | 1 | no-triple | 2.6–3.6 | +0.4221 | 0.0073 | 3 | 443,325.200 |
| O III | ns 1P* J=1 | 3–5 | 3 | 1 | 1/1 | 2.4–4.4 | +0.5852 | 0.0048 | 3 | 443,325.200 |
| O III | ns 3P* J=0 | 3–5 | 3 | 1 | 1/1 | 2.4–4.4 | +0.6250 | 0.0048 | 3 | 443,325.200 |
| O IV | nd 2D J=3/2 | 3–6 | 4 | 2 | 2/2 | 2.9–5.9 | +0.0681 | 0.0025 | 4 | 624,202.200 |
| O IV | nf 2F* J=5/2 | 4–7 | 4 | 2 | 0/2 | 4.0–6.9 | +0.0408 | 0.0115 | 4 | 624,202.200 |
| O IV * | ng 2G J=7/2 | 5–6 | 2 | 1 | no-triple | 5.0–6.0 | -0.0028 | 0.0018 | 4 | 624,202.200 |
| O IV * | nh 2H* J=9/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | -0.0125 | 0.0030 | 4 | 624,202.200 |
| O IV | np 2P* J=1/2 | 3–5 | 3 | 1 | 1/1 | 2.7–4.8 | +0.2462 | 0.0106 | 4 | 624,202.200 |
| O IV | ns 2S J=1/2 | 3–5 | 3 | 1 | 1/1 | 2.6–4.5 | +0.4408 | 0.0072 | 4 | 624,202.200 |
| P II * | np 3P J=0 | 4–5 | 2 | 1 | no-triple | 2.8–3.8 | +1.1670 | 0.0004 | 2 | 159,929.200 |
| P II | ns 3P* J=0 | 4–6 | 3 | 1 | 0/1 | 2.4–4.4 | +1.5468 | 0.0075 | 2 | 159,929.200 |
| P III | nd 2D J=5/2 | 3–6 | 4 | 2 | 2/2 | 2.8–5.7 | +0.2754 | 0.0451 | 3 | 243,573.700 |
| P III | ng 2G J=7/2 | 5–8 | 4 | 2 | 1/2 | 5.0–8.0 | +0.0197 | 0.0011 | 3 | 243,573.700 |
| P III | nh 2H* J=9/2 | 6–8 | 3 | 1 | 1/1 | 6.0–8.0 | +0.0024 | 0.0012 | 3 | 243,573.700 |
| P III | np 2P* J=1/2 | 4–6 | 3 | 1 | 0/1 | 3.1–5.1 | +0.8886 | 0.0128 | 3 | 243,573.700 |
| P III | ns 2S J=1/2 | 4–9 | 6 | 4 | 4/4 | 2.8–7.8 | +1.1692 | 0.0144 | 3 | 243,573.700 |
| P IV | nd 1D J=2 | 4–6 | 3 | 1 | 0/1 | 3.8–5.8 | +0.1991 | 0.0295 | 4 | 415,551.800 |
| P IV | nd 3D J=1 | 4–6 | 3 | 1 | 0/1 | 3.8–5.8 | +0.2312 | 0.0239 | 4 | 415,551.800 |
| P IV | nf 3F* J=2 | 4–6 | 3 | 1 | 1/1 | 4.0–5.9 | +0.0597 | 0.0170 | 4 | 415,551.800 |
| P IV | np 1P* J=1 | 4–6 | 3 | 1 | 0/1 | 3.3–5.4 | +0.6991 | 0.0588 | 4 | 415,551.800 |
| P IV | np 3P* J=0 | 4–6 | 3 | 1 | 0/1 | 3.3–5.3 | +0.6699 | 0.0079 | 4 | 415,551.800 |
| P IV | ns 1S J=0 | 4–6 | 3 | 1 | 1/1 | 3.1–5.1 | +0.9018 | 0.0111 | 4 | 415,551.800 |
| P IV | ns 3S J=1 | 4–7 | 4 | 2 | 0/2 | 3.1–6.0 | +0.9498 | 0.0073 | 4 | 415,551.800 |
| S III * | ns 3P* J=0 | 4–5 | 2 | 1 | no-triple | 2.7–3.7 | +1.2846 | 0.0049 | 3 | 281,130.000 |
| S IV | nd 2D J=3/2 | 3–5 | 3 | 1 | 1/1 | 2.8–4.7 | +0.2649 | 0.0197 | 4 | 382,135.000 |
| S IV | np 2P* J=1/2 | 4–7 | 4 | 2 | 1/2 | 3.2–6.2 | +0.7607 | 0.0167 | 4 | 382,135.000 |
| S IV | ns 2S J=1/2 | 4–7 | 4 | 2 | 1/2 | 3.0–6.0 | +1.0264 | 0.0100 | 4 | 382,135.000 |
| S V | 3s.nd 1D J=2 | 4–6 | 3 | 1 | 0/1 | 3.8–5.8 | +0.1819 | 0.0275 | 5 | 586,610.400 |
| S V | 3s.nd 3D J=1 | 4–7 | 4 | 2 | 1/2 | 3.8–6.8 | +0.2170 | 0.0211 | 5 | 586,610.400 |
| S V | 3s.nf 1F* J=3 | 4–6 | 3 | 1 | 0/1 | 4.0–6.0 | +0.0002 | 0.0246 | 5 | 586,610.400 |
| S V | 3s.nf 3F* J=2 | 4–6 | 3 | 1 | 1/1 | 4.0–5.9 | +0.0637 | 0.0116 | 5 | 586,610.400 |
| S V | 3s.np 1P* J=1 | 4–7 | 4 | 2 | 1/2 | 3.4–6.4 | +0.5900 | 0.0229 | 5 | 586,610.400 |
| S V | 3s.np 3P* J=0 | 4–6 | 3 | 1 | 0/1 | 3.4–5.3 | +0.6221 | 0.0348 | 5 | 586,610.400 |
| S V | 3s.ns 1S J=0 | 4–7 | 4 | 2 | 0/2 | 3.2–6.2 | +0.8043 | 0.0144 | 5 | 586,610.400 |
| S V | 3s.ns 3S J=1 | 4–7 | 4 | 2 | 1/2 | 3.2–6.1 | +0.8428 | 0.0080 | 5 | 586,610.400 |
| S VI | nd 2D J=3/2 | 3–9† | 6 | 4 | 2/2 | 2.9–8.9 | +0.0925 | 0.0069 | 6 | 710,194.700 |
| S VI | nf 2F* J=5/2 | 4–10 | 7 | 5 | 4/5 | 4.0–10.0 | +0.0074 | 0.0011 | 6 | 710,194.700 |
| S VI * | ng 2G J=7/2 | 5–6 | 2 | 1 | no-triple | 5.0–6.0 | +0.0010 | 0.0001 | 6 | 710,194.700 |
| S VI * | nh 2H* J=9/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0003 | 0.0001 | 6 | 710,194.700 |
| S VI | np 2P* J=1/2 | 3–7 | 5 | 3 | 3/3 | 2.6–6.6 | +0.4228 | 0.0110 | 6 | 710,194.700 |
| S VI | ns 2S J=1/2 | 3–8 | 6 | 4 | 4/4 | 2.4–7.4 | +0.6242 | 0.0083 | 6 | 710,194.700 |
| Sc III | 3p6.nd 2D J=3/2 | 3–7 | 5 | 3 | 3/3 | 2.2–6.4 | +0.6538 | 0.0617 | 3 | 199,677.370 |
| Sc III | 3p6.nd 2D J=5/2 | 3–7 | 5 | 3 | 3/3 | 2.2–6.4 | +0.6529 | 0.0616 | 3 | 199,677.370 |
| Sc III | 3p6.nf 2F* J=5/2 | 4–7 | 4 | 2 | 2/2 | 4.0–6.9 | +0.0450 | 0.0069 | 3 | 199,677.370 |
| Sc III | 3p6.nf 2F* J=7/2 | 4–7 | 4 | 2 | 2/2 | 4.0–6.9 | +0.0450 | 0.0069 | 3 | 199,677.370 |
| Sc III | 3p6.ng 2G J=7/2 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0073 | 0.0007 | 3 | 199,677.370 |
| Sc III | 3p6.ng 2G J=9/2 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0073 | 0.0007 | 3 | 199,677.370 |
| Sc III | 3p6.np 2P* J=1/2 | 4–7 | 4 | 2 | 2/2 | 2.7–5.7 | +1.2861 | 0.0211 | 3 | 199,677.370 |
| Sc III | 3p6.np 2P* J=3/2 | 4–7 | 4 | 2 | 2/2 | 2.7–5.7 | +1.2815 | 0.0211 | 3 | 199,677.370 |
| Sc III | 3p6.ns 2S J=1/2 | 4–8 | 5 | 3 | 3/3 | 2.4–6.4 | +1.5848 | 0.0180 | 3 | 199,677.370 |
| Sc III * | 3p6.nh 2H* J=11/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0022 | 0.0001 | 3 | 199,677.370 |
| Sc III * | 3p6.nh 2H* J=9/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0022 | 0.0001 | 3 | 199,677.370 |
| Si I | nd (3/2,3/2)* J=1 | 20–50 | 31 | 29 | 29/29 | 20.0–50.0 | +0.0126 | 0.0444 | 1 | 66,035.000 |
| Si I | nd (3/2,5/2)* J=3 | 20–56 | 37 | 35 | 35/35 | 19.9–56.0 | +0.0570 | 0.0366 | 1 | 66,035.000 |
| Si I | ns (3/2,1/2)* J=1 | 11–24 | 14 | 12 | untested | 9.1–22.1 | +1.8546 | 0.0082 | 1 | 66,035.000 |
| Si I | ns (3/2,1/2)* J=2 | 11–19 | 9 | 7 | untested | 9.1–17.1 | +1.8883 | 0.0005 | 1 | 66,035.000 |
| Si I | 3s2.3p.(2P*<3/2>).nf 2[3/2] J=1 | 4–7 | 4 | 2 | untested | 4.0–7.0 | -0.0003 | 0.0026 | 1 | 66,035.000 |
| Si I | 3s2.3p.(2P*<3/2>).nf 2[3/2] J=2 | 4–7 | 4 | 2 | untested | 4.0–7.0 | -0.0008 | 0.0023 | 1 | 66,035.000 |
| Si I | 3s2.3p.(2P*<3/2>).nf 2[5/2] J=2 | 4–7 | 4 | 2 | untested | 4.0–7.0 | +0.0277 | 0.0056 | 1 | 66,035.000 |
| Si I | 3s2.3p.(2P*<3/2>).nf 2[5/2] J=3 | 4–7 | 4 | 2 | untested | 4.0–7.0 | +0.0281 | 0.0057 | 1 | 66,035.000 |
| Si I | 3s2.3p.(2P*<3/2>).nf 2[7/2] J=3 | 4–7 | 4 | 2 | untested | 4.0–6.9 | +0.0471 | 0.0041 | 1 | 66,035.000 |
| Si I | 3s2.3p.(2P*<3/2>).nf 2[7/2] J=4 | 4–7 | 4 | 2 | untested | 4.0–6.9 | +0.0462 | 0.0039 | 1 | 66,035.000 |
| Si I | 3s2.3p.(2P*<3/2>).nf 2[9/2] J=4 | 4–7 | 4 | 2 | untested | 4.0–7.0 | +0.0165 | 0.0023 | 1 | 66,035.000 |
| Si I | 3s2.3p.(2P*<3/2>).nf 2[9/2] J=5 | 4–7 | 4 | 2 | untested | 4.0–7.0 | +0.0181 | 0.0027 | 1 | 66,035.000 |
| Si I | 3s2.3p.(2P*<1/2>).nd 1D* J=2 | 3–8 | 6 | 4 | untested | 2.4–7.9 | +0.4032 | 0.1771 | 1 | 65,747.760 |
| Si I | 3s2.3p.(2P*<1/2>).nd 1F* J=3 | 3–8† | 5 | 3 | untested | 3.0–8.4 | -0.1375 | 0.1513 | 1 | 65,747.760 |
| Si I | 3s2.3p.(2P*<1/2>).nd 1P* J=1 | 3–8 | 6 | 4 | untested | 3.0–8.0 | +0.0284 | 0.0044 | 1 | 65,747.760 |
| Si I | 3s2.3p.(2P*<1/2>).nd 3F* J=2 | 3–8 | 6 | 4 | untested | 2.6–7.6 | +0.3730 | 0.0333 | 1 | 65,747.760 |
| Si I | 3s2.3p.(2P*<1/2>).nd 3F* J=3 | 3–8 | 6 | 4 | untested | 2.6–7.8 | +0.3007 | 0.0615 | 1 | 65,747.760 |
| Si I | 3s2.3p.(2P*<1/2>).nd 3F* J=4 | 3–8 | 6 | 4 | untested | 2.6–8.2 | +0.1429 | 0.2129 | 1 | 65,747.760 |
| Si I * | np (1/2,1/2) J=1 | 6–7 | 2 | 1 | untested | 4.5–5.5 | +1.4808 | 0.0027 | 1 | 65,747.760 |
| Si I * | np (1/2,3/2) J=1 | 6–7 | 2 | 1 | untested | 4.6–5.6 | +1.4252 | 0.0076 | 1 | 65,747.760 |
| Si I * | np (1/2,3/2) J=2 | 6–7 | 2 | 1 | untested | 4.6–5.6 | +1.4210 | 0.0078 | 1 | 65,747.760 |
| Si I | ns (1/2,1/2)* J=0 | 6–10 | 5 | 3 | 3/3 | 4.1–8.1 | +1.8930 | 0.0038 | 1 | 65,747.760 |
| Si I | ns (1/2,1/2)* J=1 | 6–10 | 5 | 3 | 3/3 | 4.1–8.1 | +1.8758 | 0.0091 | 1 | 65,747.760 |
| Si I | ns (1/2,1/2)* J=0 | 13–21 | 9 | 7 | untested | 11.1–19.1 | +1.8873 | 0.0031 | 1 | 65,747.760 |
| Si I | ns (1/2,1/2)* J=1 | 13–21 | 9 | 7 | untested | 11.1–19.1 | +1.8765 | 0.0105 | 1 | 65,747.760 |
| Si I | nd (1/2,3/2)* J=1 | 14–44 | 29 | 27 | 27/27 | 14.0–43.9 | +0.0612 | 0.0310 | 1 | 65,747.760 |
| Si I | nd (1/2,3/2)* J=1 | 9–44† | 34 | 32 | untested | 9.0–43.9 | +0.0584 | 0.0312 | 1 | 65,747.760 |
| Si I | nd (3/2,3/2)* J=0 | 8–13 | 6 | 4 | 4/4 | 8.1–13.1 | -0.0680 | 0.0129 | 1 | 66,035.000 |
| Si I | nd (3/2,3/2)* J=1 | 20–50 | 31 | 29 | untested | 20.0–50.0 | +0.0129 | 0.0444 | 1 | 66,035.000 |
| Si I | nd (3/2,5/2)* J=1 | 8–13 | 6 | 4 | 4/4 | 7.9–12.9 | +0.0784 | 0.0064 | 1 | 66,035.000 |
| Si I | nd (3/2,5/2)* J=3 | 20–56 | 37 | 35 | untested | 19.9–56.0 | +0.0573 | 0.0366 | 1 | 66,035.000 |
| Si I | nd (3/2,3/2)* J=0 | 8–16 | 9 | 7 | untested | 8.1–16.0 | -0.0609 | 0.0146 | 1 | 66,035.000 |
| Si I | nd (3/2,5/2)* J=1 | 8–16 | 9 | 7 | untested | 7.9–15.9 | +0.0816 | 0.0073 | 1 | 66,035.000 |
| Si II | 3s2.nd 2D J=3/2 | 3–8 | 6 | 4 | 4/4 | 2.9–7.7 | +0.2290 | 0.0556 | 2 | 131,838.140 |
| Si II | 3s2.nd 2D J=5/2 | 3–8 | 6 | 4 | 4/4 | 2.9–7.7 | +0.2289 | 0.0558 | 2 | 131,838.140 |
| Si II | 3s2.nf 2F* J=5/2 | 4–11 | 8 | 6 | 6/6 | 3.9–10.9 | +0.0846 | 0.0120 | 2 | 131,838.140 |
| Si II | 3s2.nf 2F* J=7/2 | 4–11 | 8 | 6 | 6/6 | 3.9–10.9 | +0.0846 | 0.0120 | 2 | 131,838.140 |
| Si II | 3s2.ng 2G J=7/2 | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | +0.0174 | 0.0015 | 2 | 131,838.140 |
| Si II | 3s2.ng 2G J=9/2 | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | +0.0174 | 0.0015 | 2 | 131,838.140 |
| Si II | 3s2.np 2P* J=1/2 | 3–10 | 8 | 6 | 2/6 | 1.8–9.1 | +1.0239 | 0.0878 | 2 | 131,838.140 |
| Si II | 3s2.np 2P* J=3/2 | 3–10 | 8 | 6 | 2/6 | 1.8–9.1 | +1.0215 | 0.0868 | 2 | 131,838.140 |
| Si II | 3s2.ns 2S J=1/2 | 4–9 | 6 | 4 | 4/4 | 2.6–7.6 | +1.3944 | 0.0161 | 2 | 131,838.140 |
| Si III | nd 1D J=2 | 3–9 | 7 | 5 | 3/5 | 3.1–9.0 | +0.0507 | 0.1195 | 3 | 270,139.300 |
| Si III | nd 3D J=3 | 3–9 | 7 | 5 | 2/5 | 2.8–8.8 | +0.1977 | 0.0294 | 3 | 270,139.300 |
| Si III | nf 1F* J=3 | 4–9 | 6 | 4 | 2/4 | 3.9–9.0 | +0.0240 | 0.1413 | 3 | 270,139.300 |
| Si III | nf 3F* J=2 | 4–9 | 6 | 4 | 4/4 | 4.0–9.0 | +0.0226 | 0.0272 | 3 | 270,139.300 |
| Si III | nf 3F* J=3 | 4–9 | 6 | 4 | 4/4 | 4.0–9.0 | +0.0224 | 0.0275 | 3 | 270,139.300 |
| Si III | nf 3F* J=4 | 4–9 | 6 | 4 | 4/4 | 4.0–9.0 | +0.0221 | 0.0280 | 3 | 270,139.300 |
| Si III | ng 1G J=4 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0266 | 0.0040 | 3 | 270,139.300 |
| Si III | ng 3G J=3 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0281 | 0.0047 | 3 | 270,139.300 |
| Si III | ng 3G J=4 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0281 | 0.0047 | 3 | 270,139.300 |
| Si III | ng 3G J=5 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0280 | 0.0047 | 3 | 270,139.300 |
| Si III | nh 1H* J=5 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0082 | 0.0007 | 3 | 270,139.300 |
| Si III | nh 3H* J=5 | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0086 | 0.0004 | 3 | 270,139.300 |
| Si III | nh 3H* J=6 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0082 | 0.0007 | 3 | 270,139.300 |
| Si III | ni 1I J=6 | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0033 | 0.0002 | 3 | 270,139.300 |
| Si III | ni 3I J=7 | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0033 | 0.0002 | 3 | 270,139.300 |
| Si III | np 1P* J=1 | 4–7 | 4 | 2 | 0/2 | 3.2–6.3 | +0.7576 | 0.0165 | 3 | 270,139.300 |
| Si III | np 3P* J=0 | 4–7 | 4 | 2 | 2/2 | 3.2–6.3 | +0.7563 | 0.0149 | 3 | 270,139.300 |
| Si III | ns 1S J=0 | 4–8 | 5 | 3 | 2/3 | 3.0–7.0 | +1.0185 | 0.0017 | 3 | 270,139.300 |
| Si III | ns 3S J=1 | 4–8 | 5 | 3 | 3/3 | 2.9–7.0 | +1.0646 | 0.0175 | 3 | 270,139.300 |
| Si IV | nd 2D J=5/2 | 3–8 | 6 | 4 | 4/4 | 2.9–7.9 | +0.0802 | 0.0079 | 4 | 364,093.100 |
| Si IV | nf 2F* J=5/2 | 4–8 | 5 | 3 | 3/3 | 4.0–8.0 | +0.0054 | 0.0007 | 4 | 364,093.100 |
| Si IV | ng 2G J=7/2 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0011 | 0.0001 | 4 | 364,093.100 |
| Si IV * | nh 2H* J=9/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0003 | 0.0001 | 4 | 364,093.100 |
| Si IV | np 2P* J=1/2 | 3–8 | 6 | 4 | 4/4 | 2.4–7.5 | +0.5262 | 0.0121 | 4 | 364,093.100 |
| Si IV | ns 2S J=1/2 | 3–8 | 6 | 4 | 4/4 | 2.2–7.2 | +0.7845 | 0.0094 | 4 | 364,093.100 |
| Ti III * | nd 1F J=3 | 4–5 | 2 | 1 | no-triple | 3.2–4.2 | +0.7987 | 0.0056 | 3 | 223,827.100 |
| Ti III * | nd 3D J=1 | 4–5 | 2 | 1 | no-triple | 3.2–4.2 | +0.7899 | 0.0076 | 3 | 223,827.100 |
| Ti III * | np 1D* J=2 | 4–5 | 2 | 1 | no-triple | 2.6–3.6 | +1.4159 | 0.0063 | 3 | 223,827.100 |
| Ti III * | np 3D* J=1 | 4–5 | 2 | 1 | no-triple | 2.6–3.6 | +1.4039 | 0.0025 | 3 | 223,827.100 |
| Ti III * | np 3F* J=2 | 4–5 | 2 | 1 | no-triple | 2.6–3.6 | +1.3956 | 0.0072 | 3 | 223,827.100 |
| Ti III * | ns 1D J=2 | 4–5 | 2 | 1 | no-triple | 2.3–3.3 | +1.6726 | 0.0013 | 3 | 223,827.100 |
| Ti III * | ns 3D J=1 | 4–5 | 2 | 1 | no-triple | 2.3–3.3 | +1.6901 | 0.0041 | 3 | 223,827.100 |
| Ti XI * | nf 1F* J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0129 | 0.0041 | 11 | 2,137,900.000 |
| Ti XI | np 1P* J=1 | 4–7 | 4 | 2 | 1/2 | 3.6–6.7 | +0.3273 | 0.0161 | 11 | 2,137,900.000 |
| Ti XI * | ns 1S J=0 | 4–5 | 2 | 1 | no-triple | 3.5–4.5 | +0.4738 | 0.0070 | 11 | 2,137,900.000 |
| Ti XI * | ns 3S J=1 | 4–5 | 2 | 1 | no-triple | 3.5–4.5 | +0.4983 | 0.0067 | 11 | 2,137,900.000 |
| Zn I | nd 1D J=2 | 12–20 | 9 | 7 | untested | 10.8–18.8 | +1.2232 | 0.0018 | 1 | 75,769.310 |
| Zn I | np 1P* J=1 | 13–40 | 28 | 26 | untested | 10.9–37.9 | +2.0966 | 0.0033 | 1 | 75,769.310 |
| Zn I * | 4snd 3D J=1 | 4–5 | 2 | 1 | no-triple | 2.9–3.9 | +1.0940 | 0.0007 | 1 | 75,769.330 |
| Zn I * | 4snd 3D J=2 | 4–5 | 2 | 1 | no-triple | 2.9–3.9 | +1.0936 | 0.0007 | 1 | 75,769.330 |
| Zn I * | 4snd 3D J=3 | 4–5 | 2 | 1 | no-triple | 2.9–3.9 | +1.0930 | 0.0007 | 1 | 75,769.330 |
| Zn II | ns ²S | 4–9 | 6 | 4 | 4/4 | 1.7–6.8 | +2.2084 | 0.0679 | 2 | 144,892.600 |
| Zn II | nd ²D | 4–9 | 6 | 4 | 4/4 | 3.0–8.0 | +0.9583 | 0.0228 | 2 | 144,892.600 |
| Zn II | np ²P° | 4–8 | 5 | 3 | 3/3 | 2.1–6.1 | +1.8386 | 0.0616 | 2 | 144,892.600 |
| Zn II | nf ²F° | 4–8 | 5 | 3 | 3/3 | 4.0–8.0 | +0.0172 | 0.0044 | 2 | 144,892.600 |
| Zn II | ng ²G | 5–7 | 3 | 1 | 1/1 | 5.0–7.0 | +0.0038 | 0.0008 | 2 | 144,892.600 |

**596 channel rows across 28 elements · 2,269 interior cells parsed.**

| element | channels |
|---|---|
| Al | 19 |
| Ar | 50 |
| B | 32 |
| Ba | 27 |
| Be | 30 |
| Bi | 22 |
| C | 36 |
| Ca | 18 |
| Cd | 12 |
| F | 5 |
| Fe | 8 |
| Ga | 13 |
| Ge | 5 |
| He | 16 |
| Hg | 5 |
| K | 8 |
| Li | 36 |
| Mg | 37 |
| N | 18 |
| Na | 12 |
| Ne | 44 |
| O | 12 |
| P | 14 |
| S | 18 |
| Sc | 11 |
| Si | 67 |
| Ti | 11 |
| Zn | 10 |

---

# III · THE MECHANISMS

**How a value is got where no capture reaches.** Each is measured on pairs where both cells are known.

| mechanism | the move | what it gives |
|---|---|---|
| the ground-state derivation | none | the multiplicity, and the bound B |
| the isoelectronic ladder | (Z, c) → (Z+1, c+1) | δ along a sequence |
| the charge ladder | c → c+1 at fixed Z | δ falls with charge |
| ℓ-collapse | ℓ → ℓ+1 | δ falls with ℓ |
| the exchange split | singlet ↔ triplet | the triplet defect exceeds the singlet at ns |
| the Janet collapse | a lookup in the periodic table | whether a p = 0 channel is large |
| Seaton's formula | none | δ₀ = 3α/K(ℓ) for a non-penetrating series |

## The isoelectronic ladder

**Along a sequence of fixed electron count, a channel's defect follows δ(c) = A + B·ln(c+1)/c.** Fitted per sequence on the 52 with three or more charge states it reaches a median rms of **0.0083** — the tightest relation the compendium holds.

**And A is fixed rather than fitted.** As charge grows at constant electron count the core collapses to a point and the ion becomes hydrogenic, so δ → 0. That is the periodic table's own edge, and setting A ≡ 0 leaves one parameter.

## A channel is a curve

        δ(n) = δ₀ + δ₂/(n − δ₀)²

**δ₀ is the limit value the index carries; δ₂ is the curvature.** Fitted on 274 channels, the second term removes **48%** of what a constant defect leaves as scatter.

**And the sign of δ₂ names the regime**: positive for core penetration, negative for core polarisation. By orbital: **s 76% positive, p 74%, d 37%, f 6%, g 7%.** *The sign rule is NIST's own, stated in the reference the levels come from. What the compendium adds is the measurement across 274 channels and the finding that |δ₂| predicts a channel's scatter at R² = 0.761.*

![The index](figures-compendia/fig-index-final.png)

---

## The bracket's deficit, on a classical object

**The bracket — T(n) between T(n−1) and T(n+1) — is the book's one ternary object (§21.5.1), and Λ₃ is the ternary object of celestial mechanics.** The two share the deficit: both need strong 3-consistency and both get level 2 from ℛ. In spectra the deficit is paid per channel by the envelope cells of §12.11.3; in three bodies it is paid once, by the stratum boundaries. No channel entry changes. *The same shortfall, on a classical object, is Λ₃ (Index of Indices V; register 1716, 1724).*

---

# IV · THE SOURCES

## B.1 Sources
  compilation                 spectra drawn
  Kaufman & Martin            Al I, Al II
  1991, JPCRD 20, 775
  Kramida & Martin            Be I
  1997, JPCRD 26, 1185
  NIST ASD                    Ar II, Be II, Bi I, C II, Ca II, Cd II, Ga I, He I, He II, Hg II, K II, Li I, Li II, Mg II, N II, Na II, Ne I (³⁄₂), Ne
                              I (¹⁄₂), Si I, Si II, Zn II
  Sansonetti 2008,            Na I
  JPCRD 37, 1659
  Sansonetti 2008,            K I
  JPCRD 37, 7
 **Additional sources used for exotic systems and collective quantities:**
 Hori *et al.*, *Nature* **475**, 484 (2011) and *Phys. Rev. Lett.* **96**, 243401 (2006), both accessed via CODATA 2010 Table XII (arXiv:1203.5425) and arXiv:1304.4330 · Korobov, *Phys. Rev. A* **77**, 042506 (2008) · Singer, Stanojevic, Weidemüller & Côté, *J. Phys. B* **38**, S295 (2005) · Sugar & Corliss 1985, *JPCRD* **14** Suppl. 2 · Sugar & Musgrove 1990, *JPCRD* **19**, 527 and 1995, *JPCRD* **24**, 1803.
## B.2 Channels
  **The channel rows are printed here in full.** Each carries its species,
  channel, n-range, level count, interior cells, bracket, ν range, mean quantum defect, its
  spread, Z_eff and the series limit. *The main volume reproduces one only where it carries an
  argument; the rest are data, and this is where data belongs.*
  **THE METHOD 1.6 — SPECTRA COMPENDIUM, counted from the table above rather than from what once generated it.** 596 channel rows — 477 series of three or more members and 119 two-member channels (starred) — across 28 elements and 70 species; 3,342 levels, 2,269 interior cells. The bracket stands at **1,577 of 1,738 cells across 392 rows** — the first collection's 844 of 844 on 107 rows; 658 of 813 on 250 rows run under ruling 26 (register 1763); and 75 of 81 on 35 rows run by the same sealed instrument on the six captures the delivering bank's cut carried, each verified against that cut's MANIFEST by hash before a cell was computed (register 1768) — throughout, the sealed test of register 796 at strict interval membership, the only ε the quotation floor — half a unit in the last quoted decimal of the measured level — and admissibility per §22.5, r = 2Z²R/(ν³σ) ≥ 5 with σ the quotation floor. **Cells refused: 0.** The 161 failing cells sit in 98 rows and are results, not defects of the test (register 784: no failures would itself be suspect); five of those rows carry a failing bracket narrower than twice the floor, named in 1763 for the author's eye — none of the six cells failing at this build is among them, each missing a bracket wider than twice its floor. 78 rows read `no-triple`: their members, matching the row exactly, contain no three consecutive n, so the sealed test — true neighbours only — defines no cell there; the ten added at this build are the ten starred two-member rows of the six delivered species. 126 rows remain `untested`, and the reason is data, not definition: the parent-term and coupling selection that built them is not reproducible blind (register 1578's wall), and the delivered selection record covers none of their eight species (register 1767). All bracket figures in this paragraph are recomputed from the table itself.
 *The earlier statement of this paragraph — 133 rows, 23 elements, 869 interior cells, bracket 869/869, with a twenty-channel gap disclosed against a total of 153 — was true at registers 630–631 and was overtaken by the parent-term wall (register 1578) and the J-resolved rows of T8-J (registers 1699–1700). It claimed the table could not drift from the generator that once wrote it; the table did drift, so that generator is retired: the table above is the source, and every count in the paragraph above it is taken from the table — 596, 477, 119, 28, 70, 3,342 and 2,269 agree to the row. The exotic and collective sources named above still carry sources and no rows, and that remains disclosed rather than reconciled.* Registers 630–631; 1578; 1699–1700.
## B.3 Flagged channels
 Channels whose δ spread exceeds 0.25 or whose V departs from 4ν/3 by more than 5% are flagged.
 Every flag in this collection has an identified cause; none is unexplained.

  species      channel        δ spread    cause
  Al I         3s²nd ²D       0.630       compilers relabelled this series; y²D removed as a perturber
  Al II        3snd ¹D        0.390       local perturber
  Al II        3snf ³F°       0.409       δ reverses sign between n = 6 and 7 — local perturber
  Li I         np 2P°         0.678       39 cells to n = 42; quotation coarsens above n = 33
  Si II        3s²np ²P°      0.272       perturber

## Published values the coordinates are checked against

| source | what it gives |
|---|---|
| **NIST Atomic Spectra Database** | the levels every capture is fitted to |
| **Theodosiou, Inokuti & Manson, At. Data Nucl. Data Tables 35, 473 (1986)** | asymptotic quantum defects of s, p, d and f orbitals for **all ionisation stages of all ions with Z ≤ 50**, Hartree–Slater |
| Manson, Inokuti & Theodosiou, OSTI 7104964 | the isoelectronic, isonuclear and isoionic pictures |
| Seaton 1958; Drake & Swainson 1991 | the polarisation formula |
| Peper *et al.* 2019 | K I to eight digits |
| Freeman & Kleppner 1976 | Na I ng |
| arXiv:1706.06237 | Cs I np at n = 70–100 |
| arXiv:2508.06733 | actinide defects, Z = 89–103 |
| arXiv:2502.20961 | Cs⁺ dipole and quadrupole polarisabilities |
| ARC Alkali Rydberg Calculator | an independent check on K I |

*The full bibliography, with what each source was used for, is in the Mathematical Compendium.*


---

# V · THE CAPTURE GROUPS

*Register 1296 marked these as owed. Counts below are read from `COORDINATES-2.13` at build time, not transcribed.*

| group | species | cells | measured | exact | computed |
|---|---|---|---|---|---|
| **Kr-core** | Kr | 512 | 0 | 8 | 504 |
| **Cd/In** | Cd/In | 1,384 | 13 | 16 | 1,355 |
| **La/Ce** | La/Ce | 1,632 | 0 | 16 | 1,616 |
| **Hg-core** | Hg | 1,168 | 5 | 8 | 1,155 |

**4,696 cells across six species**, every one spanning l = 0-7 and the full charge ladder from 1 to Z.

## What the counts say, measured on this compendium's own basis

*Section 0 states that accuracy is quoted against the WITNESSED-plus-possible set and not against the whole index. The same basis is used here.*

**The four groups hold 18 reachable cells of the index's 358 - 5.0% of the reachable set on 4.5% of the cells.** They are therefore slightly BETTER than representative, not worse.

On the raw grade column they carry 18 `measured` cells of 4,696 - Cd/In thirteen and Hg five, with **Kr-core and La/Ce carrying none.** *That ratio is not a fact about these groups: the whole index is 98.8% computed, which section 0's table already states. The filler is the index's condition, not these captures' shortcoming.*

## Why each was captured

- **Kr-core** - the n = 4 closure; its 5s manifold is still one level short
- **Cd/In** - the d10 closure and the first post-d p-electron
- **La/Ce** - THE JANET ANOMALY ITSELF - La opens 5d, Ce is where 4f appears
- **Hg-core** - the 5d closure at high Z, where the relativistic wall stands

**La/Ce is the group that earns its place.** The other three fill coordinate space; **La/Ce is where the filling order itself breaks**, and holding it in the index lets the anomaly be stated as a coordinate fact rather than a footnote.

---

# VI · THE LÖWDIN SUPPLY

*The Löwdin solution is tested against measurement, and this is the measurement it is tested against. Registers 1524–1677 record the capture of these bodies one at a time, each verified before it was written and several corrected after; §* Why each was captured *does the same office for the coordinate groups. What follows is the empirical supply itself, set out so that a reader can see what was consulted, how much of it there is, and what each body can and cannot carry.*

## What this supply is, and what it is not

**Seven families, 1,816 rows, of which 1,262 were captured from a published compilation and verified before they were held.** *Almost none of it is computed by this work. It is the outside world, brought in and checked: X-ray transition energies, ionisation energies along the charge ladder and across the neutral atoms, two level tables, nuclear radii and masses, quantum defects from an independent database, and a staged block of index cells.*

| family | rows | span | source compilation |
|---|---|---|---|
| **the X-ray lines** | 474 | Ne–Fm, six transitions | NIST SRD 128 v1.2 (Deslattes *et al.* 2003) |
| **the isoelectronic ladder** | 546 | Z = 1–18 and 19–36 | NIST ASD ver. 5.12 |
| **the neutral ionisation energies** | 108 | Z = 1–108 | NIST ASD ver. 5.12 |
| **the level tables** | 29 | Fe I, Kr I | NIST ASD |
| **the nuclear supply** | 37 | Th–Cf, the A = 9 chain | Angeli & Marinova 2013; AME2020 |
| **the quantum defects** | 68 | Li, O, Na, Mg, all stages | TOPbase, *via* de Kertanguy |
| **the staged cells** | 554 | 158 index cells | this work's own retrievals |
| | **1,816** | | |

**The row total and the family total differ, and the difference is the point.** *The staged cells are not an outside compilation — they are this work's retrievals staged in the index's own schema, and they are listed here because register 1649 named them as the source of a figure the compendium prints. The outside supply proper is 1,262 rows.*

**Two of the eighteen bodies the register names are not held here, and their absence is stated rather than papered over.** *The measurements store and the rows recovered at register 652 are stores this work built, not captures it took; register 1674 records that the first has no generator and survives only as data. Neither is an outside compilation, and neither is reproduced in this supply.*

## The X-ray transition energies

*Six transitions, captured one at a time between registers 1524 and 1555, and the family that cost the most to get right: register 1526 records four fabricated theory values in the first of them, copied from the experimental column where the source stood blank, and the correction is why every later capture was verified by destination address and body header before it was written.*

| transition | line | rows | first | last |
|---|---|---|---|---|
| K–L3 | Kα₁ | 98 | Ne | Fm |
| L3–M5 | Lα₁ | 78 | Ca | Fm |
| L3–M4 | Lα₂ | 78 | Ca | Fm |
| L3–M1 | Lℓ | 88 | Na | Fm |
| L1–N2 | Lγ₂ | 67 | Ga | Fm |
| L1–N3 | Lγ₃ | 65 | As | Fm |
| | | **474** | | |

**Each row carries the element, a mass number where the source gives one, a theoretical energy, a direct experimental energy, and an uncertainty on each.** *NIST's compact parenthetical form is preserved as it stands: 849.17(54) is 849.17 ± 0.54 eV. Two flags travel with the value — an asterisk where the source interpolated from neighbouring elements, and a hash where experiment and theory diverge far enough that the source itself doubts the measurement. A blend field says where Kα₁ and Kα₂ are unresolved at that element. Blank means blank; nothing is inferred into an empty field.*

**One row, as it stands:**

```
Kα₁   U   238   theory 98433.6(36)   experiment 98431.58(28)   ref 5d
```

**The K–L3 capture carries thirteen actinide isotope rows — uranium at two masses, plutonium at two, americium at two, curium at two, berkelium at two and californium at three — and those are the anchors register 1555 identified.** *Californium's third row has no direct experimental value at all; the field is empty in the source and empty here. The mass-number column is blank below bismuth, because the compilation populates it only for radionuclides.*

**The physical check the family supports, and it is the reason two of the six were taken.** *Lα₂ must lie below Lα₁ at every element, since M4 is the more tightly bound of the two levels; the pair was captured precisely so that the inequality could be tested rather than assumed. Lγ₃ − Lγ₂ is the 4p splitting, and register 1528 took both to see whether the post-krypton offset showed stable structure per region.*

## The isoelectronic ladder

*Two captures, taken through different endpoints on different days, and their overlap is what makes either trustworthy.*

**`LADDER-K-Kr` holds 495 rows: every ionisation stage of every element from potassium to krypton, Z = 19 to 36 — the whole 3d block and its shoulders, in electronvolts.** *The quality flag is the source's own: 96 measured, 287 estimated, 112 theoretical. That distribution is the ladder's real condition — beyond the first few stages of a mid-Z element, the published value is usually an estimate, and the compendium's high-charge cells inherit that.*

**`LADDER-H-Ar-I-III` holds 51 rows: hydrogen through argon at charges 0, +1 and +2, in wavenumbers, with the ground configuration, the ground level term, the isoelectronic sequence and an uncertainty on each.**

**One row, as it stands:**

```
H I   Z=1   charge 0   sequence H   ground 1s   2S<1/2>   109678.77174307 cm⁻¹ ± 0.00000010
```

**The two ladders and the neutral table agree where they overlap, and the agreement was tested rather than assumed.** *Register 1538 puts eighteen first ionisation energies from a supplied table against the K–Kr capture at a maximum discrepancy of 7.8 × 10⁻⁵ eV with nothing beyond 5 × 10⁻⁴; register 1539 finds the krypton limit agreeing to 4 × 10⁻⁹ eV. Three retrievals through three routes, converging — which is corroboration, since the routes are unalike.*

## The ionisation energies of the neutral atoms

**108 rows, Z = 1 to 108, first ionisation energy of the neutral atom with its uncertainty, and the source's own quality notation carried across intact: 98 measured, 7 estimated, 3 theoretical.** *Register 1593 cross-checked these against the K–Kr ladder's own charge-zero rows: eighteen values overlap and all eighteen agree exactly, in value and in flag. The square and round brackets the compilation prints are not decoration — they are the quality claim, and dropping them would have discarded the only statement of confidence the source makes.*

## The two level tables

**Fe I — 19 levels across five terms, all five multiplets inverted, as Hund's third rule requires of a 3d shell more than half filled.** *Every row passes the wavenumber-to-electronvolt conversion at better than 6 × 10⁻⁴ eV. The ionisation potential is excluded, and the a⁵P anomaly is flagged in the capture itself rather than in prose alone, so that the flag travels with the data.*

**Kr I — 10 levels, the 4p⁵(²P₃⁄₂)5p manifold complete at all six.** *All ten satisfy J₁ℓ pair coupling, K = J₁ ⊗ ℓ and J = K ± ½. **The table is one row short of the eleven its own header claims, and the missing row is named:** register 1541 settles 85846.709 cm⁻¹ as the J = 1 level and records the J = 0 metastable as absent from the source, with 86583.760 belonging elsewhere. The capture marks the disputed rows and leaves the choice unmade.*

## The nuclear supply

**23 measured actinide rows — thorium 5, uranium 5, plutonium 6, americium 2, curium 5 — each carrying a change in mean-square charge radius against a reference isotope, an absolute rms charge radius, and an uncertainty on both.** *From Angeli and Marinova's 2013 table of experimental ground-state charge radii. Four of the six anchors the argument needs are present and two are absent, which register 1557 predicted from the compilation's own scope before the table was in hand.*

**Berkelium and californium are computed, not measured, and the capture says so in its first line.** *Nine rows, five absolute radii and four differences, from a regression on eighteen pairs across five elements. **They are indicative only and carry their stated error.** The measurement cannot presently be made — register 1559 records that three of the four methods need tens of milligrams of material — so the values are labelled predicted in the file itself, where no later reading can mistake them for a capture.*

**The A = 9 isobar chain — five nuclides, ⁹He, ⁹Li, ⁹Be, ⁹B, ⁹C — mass excess and uncertainty from AME2020, with a stability note on each.** *Verified three ways before it was written, including reproduction of the known binding energy per nucleon from the mass excess. **Five nuclides of roughly three and a half thousand:** the capture is a probe of the chain, not a survey of the table, and register 1544 says so in the entry that records it.*

## The quantum defects of the light ladders

**68 cells: lithium 6, oxygen 16, sodium 22, magnesium 24 — each species across every one of its ionisation stages, with the defect given per ℓ.** *From TOPbase, the Opacity Project's database, as tabulated by de Kertanguy. The trail was followed there from Theodosiou, Inokuti and Manson's 1986 compilation, which this work could not obtain directly and which the paper cites as its own reference.*

**This is the charge-edge extension, and it is the only held source that supplies a complete ladder for a species.** *Register 1585 identifies it as the most valuable of the extensions available, for exactly that reason: the compendium's own measured cells cluster at low charge, and a complete ladder is what tests whether the defect's behaviour along the charge axis is what the channel equation says it is.*

## The staged cells

**554 rows over 158 distinct index cells, in the index's own eleven-column schema — the same columns §** The file *sets out, plus a tier.* **Graded A 218, B 157, C 179.** *Many rows to one cell, which is the whole point: register 1662 records that treating repeat measurements of one channel as duplicates inverted the direction of the error, since the second and third measurement of a cell are true measurements with nowhere to sit, not noise.*

**Thirty-nine series are staged as skipped, unbounded — no limit stands above them.** *A series with no limit above its top member has no defect to compute, and the staging records the fact rather than dropping the row.*

## How this supply is cited

**A body in this part is cited by its section name, as the coordinate index is cited by** COORD(Z, charge, ℓ, 2S+1). *The register's working entries name the capture files these bodies were held in; the volumes name the bodies. A reader who wants the sodium ladder is sent to §* The isoelectronic ladder*, not to a filename, and that is the whole of the difference.*

**Nothing in this part is recomputed at press.** *The counts are of captures taken and verified on the dates the register records, and they are stated as of capture. §* The table *and §* The file *are read from the coordinate companion at build and fail the press if they drift; this part is not, because the bodies it describes are compilations that do not change under this work's hand.*

