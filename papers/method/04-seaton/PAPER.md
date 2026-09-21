# A Correction to Seaton's Ratio

**The polarisation relation between the two Ritz coefficients of a Rydberg channel, δ₂/δ₀ = −ℓ(ℓ+1)/3, is a statement about non-penetrating channels only: on the three series whose core holds no orbital of the channel's ℓ it holds to a median 15%, and on the six penetrating series with ℓ ≥ 1 its ratio scatters about zero.**

**Matthew Lach** · Independent Researcher · 21 September 2026

---

## Abstract

A Rydberg series converging on an ionic core has a quantum defect δ(n) that is not one number but a curve, δ(n) = δ₀ + δ₂/(n − δ₀)². When the running electron never enters the core, the only interaction beyond the Coulomb tail is the core's dipole polarisation, and first-order perturbation theory fixes the ratio of the two coefficients without a free parameter: δ₂/δ₀ = −ℓ(ℓ+1)/3. This paper states that relation, derives it exactly from the hydrogenic expectation value ⟨r⁻⁴⟩, and tests it on thirteen Rydberg series of Cd I, In I, Rb I and Sr II fitted from the NIST level tables. The series are split by p, the number of occupied subshells of the channel's orbital angular momentum ℓ in the ground configuration of the core. Writing ρ for the fitted ratio divided by Seaton's value, the three series with p = 0 give median ρ = 1.150 with population standard deviation 0.206; the six series with p ≥ 1 and ℓ ≥ 1 give median ρ = −0.015 with standard deviation 0.177; the four s series have Seaton's value 0 and no ratio. The correction is to the relation's domain, not to its coefficient or its sign: the relation is a law of the non-penetrating branch and carries no information on the penetrating one. The paper states what the split establishes and what a sample of thirteen series cannot: on these four cores p = 0 and ℓ ≥ 3 are the same partition, so the data do not separate the two descriptions.

---

## §0 · The result

**Seaton's ratio is valid at p = 0 and undefined at p ≥ 1, and that is a statement about its domain.**

A quantum defect measures how far a Rydberg orbital penetrates its ionic core. For a non-penetrating orbital the core is felt only through its polarisability, and the leading correction to the hydrogenic energy is the expectation value of −α_d/(2r⁴). Because ⟨r⁻⁴⟩ in a hydrogenic state is (3n² − ℓ(ℓ+1)) times a function of ℓ alone, the defect has the form δ₀ + δ₂/n² with δ₂/δ₀ = −ℓ(ℓ+1)/3 — the polarisability cancels, the core charge cancels, and nothing is left to fit. That is the relation tested here (Theorem 1, PROVED and MACHINE-CHECKED).

Measured on thirteen series from four cores (Table 1), with ρ the fitted ratio divided by −ℓ(ℓ+1)/3:

| class | series | ρ defined | median ρ | population sd |
|---|---|---|---|---|
| **p = 0** (non-penetrating) | 3 | 3 | **1.150** | 0.206 |
| **p ≥ 1** (penetrating) | 10 | 6 | **−0.015** | 0.177 |

On the non-penetrating branch the relation holds to 15% at the median, the three values being 1.105, 1.150 and 1.564. On the penetrating branch ρ is centred on zero with a spread of 0.18: the fitted curvature bears no relation, in sign or in size, to the polarisation value. The four series with ℓ = 0 are penetrating and have Seaton's value 0, so ρ is undefined for them; they are counted in the ten and excluded from the six.

**What is corrected.** Not the coefficient −ℓ(ℓ+1)/3, which is a theorem, and not its sign. What is corrected is the scope on which a measured departure from it may be read. Measured across penetrating channels the ratio comes out wherever the penetration puts it, and a value such as 1.25 reported there is a number about the sample, not about the relation. The split by p is what the relation's own hypothesis requires: Seaton's derivation assumes the outer electron does not enter the core, and p = 0 is the condition under which the core has no orbital of the electron's ℓ for it to overlap.

**A second measurement rides on the same fit.** The sign of δ₂ follows p, not ℓ: all three p = 0 series have δ₂ < 0, all four series with p ≥ 4 have δ₂ > 0, and the two series at each of p = 1, 2, 3 split one and one. The fraction with positive δ₂ is non-decreasing in p across the six values p takes.

**What is not established.** The p = 0 class has three members, all with ℓ = 3, and on these four cores p = 0 holds exactly when ℓ ≥ 3, so the sample cannot distinguish a domain stated in p from one stated in ℓ. The spread of 0.206 is a population standard deviation of three numbers. The relation is first order in the dipole polarisability; the quadrupole term, second-order dipole terms and the residual penetration of an f orbital into a 4d¹⁰ core are all outside it and are the natural account of a ρ above 1 (§5). And the penetrating-branch result is not a refutation of anything: a relation whose hypothesis fails makes no prediction, and −0.015 ± 0.177 is the measurement of that silence.

**Status words.** Five are used and never merged.

| status | meaning |
|---|---|
| **PROVED** | a derivation is written out below and every step is justified; the algebraic identities are verified exactly on a grid exceeding their degree |
| **EXHAUSTIVE** | a decision procedure visited every case in a stated finite family |
| **MACHINE-CHECKED** | Z3 returned `unsat` on the negation of an obligation over a named box, with both guards passed |
| **CITED** | taken from the literature or from a public database, with the source |
| **MEASURED** | a number computed from the cited data by the stated procedure; the paper's own result, with its sample stated |

---

## §1 · Definitions

**D1 (Rydberg channel, quantum defect).** A Rydberg channel is a sequence of bound levels of one species, one orbital angular momentum ℓ and one parent term of the ionic core, with principal quantum number n running and energies `E_n` (in cm⁻¹ above the ground level) converging on the ionisation limit `I` of that parent. The core charge is `z` (1 for a neutral atom, 2 for a singly charged ion). The effective quantum number and the quantum defect of the level n are

> `n* = z √( R_M / (I − E_n) )`,  `δ_n = n − n*`,

with `R_M` the Rydberg constant for the reduced mass of the electron and the nucleus. Throughout, `R_M = R_∞ / (1 + 1/(A·1836.15267343))` with `R_∞ = 109737.31568 cm⁻¹` and `A` the atomic mass in unified mass units as tabulated in Table 1; the four values of `R_M` used are printed there.

**D2 (Ritz curve, δ₀ and δ₂).** A channel's defect is fitted by

> `δ(n) = δ₀ + δ₂ / (n − δ₀)²`,

the two-term Ritz expansion, by unweighted least squares over the channel's members. `δ₀` is the limit value and `δ₂` the curvature. The fit is defined for channels with at least four members. For fixed `δ₀` the model is linear in `δ₂`, so the minimiser is found as the minimum of a one-variable function; §4 states how it is located and certified.

**D3 (core, and the count p).** The core of a channel is the ion on whose state the series converges. Its ground configuration is a list of occupied subshells. For the channel's ℓ,

> `p := the number of occupied subshells of orbital angular momentum ℓ in the core's ground configuration.`

A channel is **penetrating** when p ≥ 1 and **non-penetrating** when p = 0. Table 1 lists the core and p for every series used.

**D4 (the dipole polarisation model).** Outside the core the running electron moves in the Coulomb field of charge z and, to leading order in the core's static dipole polarisability `α_d` (in units of a₀³), in the additional potential `V_pol = −α_d / (2r⁴)` (atomic units). The model treats `V_pol` in first-order perturbation theory on the hydrogenic state (n, ℓ) of charge z.

**D5 (Seaton's ratio).** For a channel with ℓ ≥ 1 and δ₀ ≠ 0,

> `ρ := (δ₂/δ₀) / ( −ℓ(ℓ+1)/3 )`.

ρ = 1 is exact agreement with the polarisation model (Theorem 1). For ℓ = 0 the model's value is 0 and ρ is undefined.

**D6 (the class statistics).** For each class of series the statistic reported is the median of ρ over the series with ρ defined, and the population standard deviation (divisor N, not N − 1) of the same values. The mean and the sample standard deviation are printed beside them in §4 and are not the headline figures.

**Notation.** `K(ℓ) := ℓ(ℓ+1)(2ℓ−1)(2ℓ+1)(2ℓ+3)`. Atomic units are used in §2; the data of §3 are in cm⁻¹.

---

## §2 · Seaton's relation

**Lemma 1 (the hydrogenic ⟨r⁻⁴⟩).** For the hydrogenic state (n, ℓ) of unit charge, ℓ ≥ 1,

> `⟨r⁻⁴⟩ = [3n² − ℓ(ℓ+1)] / [ 2n⁵ (ℓ+3/2)(ℓ+1)(ℓ+1/2) ℓ (ℓ−1/2) ]  =  4 [3n² − ℓ(ℓ+1)] / ( n⁵ K(ℓ) )`.

For a core of charge z, `⟨r⁻⁴⟩_z = z⁴ ⟨r⁻⁴⟩_1`.

*Proof.* The radial function is `R_nℓ(r) = N r^ℓ e^{−r/n} L^{(2ℓ+1)}_{n−ℓ−1}(2r/n)`, a polynomial in r of lowest degree ℓ times an exponential, and `⟨r^s⟩ = ∫₀^∞ R_nℓ² r^{s+2} dr`. Every integral is of the form `∫₀^∞ r^k e^{−2r/n} dr = k! (n/2)^{k+1}`, convergent for integer k ≥ 0, and for s = −4 the lowest power is 2ℓ − 2 ≥ 0 when ℓ ≥ 1. So ⟨r⁻⁴⟩ is a rational number computable exactly from the Laguerre coefficients, and the closed form is verified by computing it: for every (n, ℓ) with 2 ≤ n ≤ 30 and 1 ≤ ℓ ≤ n − 1 — 435 states — the exact integral equals the closed form. As a control the same integration reproduces `⟨r⁻²⟩ = 1/(n³(ℓ+1/2))` on the same 435 states. The closed form for general n is the standard result of Bethe and Salpeter (1957), CITED; the equality of the two expressions in the statement is the identity `(ℓ+3/2)(ℓ+1/2)(ℓ−1/2) = (2ℓ+3)(2ℓ+1)(2ℓ−1)/8`. The scaling in z follows from `r → r/z` in the radial function. ∎ **EXHAUSTIVE** (435 states) and **CITED** (general n).

**Lemma 2 (the defect is the first-order energy shift, exactly).** Let `E(n, δ) = −z²/(2(n−δ)²)` be the term energy of a level with defect δ (atomic units). Then, as an identity in n, δ and z,

> `E(n, δ) − E(n, 0) = − z² δ (2n − δ) / ( 2n² (n − δ)² )`.

Consequently, if a perturbation shifts the hydrogenic level by ΔE, the defect that reproduces the shifted energy satisfies `δ = −(n³/z²) ΔE · (n−δ)²/(n(2n−δ))`, whose second factor is `1 + O(δ/n)`; so to first order in the perturbation `δ = −(n³/z²) ΔE`.

*Proof.* Put both sides over the common denominator `2n²(n−δ)²`: the left is `z²[(n−δ)² − n²] / (2n²(n−δ)²) = z²(−2nδ + δ²)/(2n²(n−δ)²)`, which is the right. After clearing the denominator the identity is polynomial of degree 2 in each of n, δ and z; it is verified exactly on a 4 × 4 × 4 grid of rationals, which exceeds the degree in every variable, and a polynomial vanishing on such a grid is identically zero. The rearrangement for δ is division by `z²(2n−δ)/(2n²(n−δ)²)`, legitimate for 0 < δ < 2n, and `(n−δ)²/(n(2n−δ)) = 1 − (3nδ − δ²)/(n(2n−δ)) = 1 + O(δ/n)`. ∎ **PROVED.**

**Theorem 1 (Seaton's ratio).** In the dipole polarisation model (D4), the quantum defect of the non-penetrating channel (ℓ ≥ 1) of a core of charge z and polarisability α_d is, to first order in α_d,

> `δ(n) = 6 α_d z² / K(ℓ)  −  2 α_d z² ℓ(ℓ+1) / ( K(ℓ) n² )  =:  c₀ + c₂/n²`,

and therefore

> `c₂ / c₀ = − ℓ(ℓ+1) / 3`,

independent of α_d, of z and of n. If α_d > 0 then c₀ > 0 and c₂ < 0.

*Proof.* First-order perturbation theory gives `ΔE = ⟨V_pol⟩ = −(α_d/2) ⟨r⁻⁴⟩_z = −(α_d/2) z⁴ ⟨r⁻⁴⟩_1` (Lemma 1). Lemma 2 gives, to first order, `δ = −(n³/z²)ΔE = (α_d/2) z² n³ ⟨r⁻⁴⟩_1`. Substituting Lemma 1,

> `δ = (α_d/2) z² n³ · 4[3n² − ℓ(ℓ+1)]/(n⁵ K(ℓ)) = 2 α_d z² [3 − ℓ(ℓ+1)/n²] / K(ℓ)`,

which is the displayed form with `c₀ = 6α_d z²/K(ℓ)` and `c₂ = −2α_d z² ℓ(ℓ+1)/K(ℓ)`. Their ratio is `−ℓ(ℓ+1)/3`. K(ℓ) > 0 for ℓ ≥ 1, so the signs follow from the sign of α_d. The identity `(α_d/2) z² n³ ⟨r⁻⁴⟩_1 = c₀ + c₂/n²` is verified exactly for every state of Lemma 1's family with n ≤ 20 on a grid of α_d and z above the degree, 2,280 points in all. ∎ **PROVED**; and **MACHINE-CHECKED**: for each ℓ ∈ {1, …, 8}, Z3 returns `unsat` on the negation of "for all real α_d and z, 3c₂ = −ℓ(ℓ+1)c₀, and α_d > 0 ∧ z ≠ 0 ⇒ c₀ > 0 ∧ c₂ < 0", eight obligations; the hypothesis is satisfiable (non-vacuity) and the encoded c₀, c₂ agree with an independent exact implementation on 200 random rational (α_d, z, ℓ) with no disagreement (encoding fidelity).

**Attribution.** The polarisation origin of the high-ℓ defect is Born and Heisenberg (1924); its systematic use to extract polarisabilities from spectra is Mayer and Mayer (1933); the quantum defect method in which the relation is used is Seaton (1958), with the second-order polarisation corrections in Drake and Swainson (1991). The ratio is attributed to Seaton here as it is in the spectroscopic literature; the derivation above is self-contained, and its prefactor `6α_d z²/K(ℓ) = (3/4) α_d z² / [(ℓ−1/2)ℓ(ℓ+1/2)(ℓ+1)(ℓ+3/2)]` is the familiar leading term `3α_d/(4ℓ⁵)` at large ℓ. The ratio does not depend on the prefactor.

**Lemma 3 (the Ritz denominator).** The fit of D2 uses `(n − δ₀)²` where Theorem 1 has `n²`. As an identity,

> `δ₂/(n−δ₀)² − δ₂/n² = δ₂ δ₀ (2n − δ₀) / ( n² (n−δ₀)² )`,

and in the polarisation model δ₀ and δ₂ are both first order in α_d, so the difference is second order. The Ritz coefficient ratio therefore equals −ℓ(ℓ+1)/3 to the same order as Theorem 1; the physical reason is that the hydrogenic expectation value belongs to the effective quantum number, and `n − δ₀` is the effective quantum number to first order.

*Proof.* Common denominator: `δ₂[n² − (n−δ₀)²]/(n²(n−δ₀)²) = δ₂(2nδ₀ − δ₀²)/(n²(n−δ₀)²)`. After clearing the denominator the identity is polynomial of degree 2 in n, 3 in δ₀ and 1 in δ₂ and is verified exactly on a 4 × 5 × 3 grid, above the degree in every variable. ∎ **PROVED.** The measured size of the effect on this sample is given in §4.

---

## §3 · The data

**Provenance.** Every level is taken from the NIST Atomic Spectra Database (Kramida, Ralchenko, Reader and the NIST ASD Team, version 5.12), CITED. The ionisation limits are the tabulated limits of the parent ions (Cd II 5s ²S₁/₂, In II 5s² ¹S₀, Rb II ¹S₀, Sr III ¹S₀). The atomic masses are the tabulated atomic weights (Cd, In, Rb) and the ⁸⁸Sr isotope mass. The series and their members are those the tables resolve without a perturber crossing the fitted range; §5 names the one series whose residual says otherwise.

**The four cores.** Cd I converges on Cd⁺, ground configuration [Kr] 4d¹⁰ 5s; In I on In⁺, [Kr] 4d¹⁰ 5s²; Rb I on Rb⁺ and Sr II on Sr²⁺, both [Kr] = 1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶. Counting occupied subshells by ℓ gives p for s, p, d, f of (5, 3, 2, 0) for the two cadmium-like cores and (4, 3, 1, 0) for the two krypton-like cores. On all four, p = 0 exactly when ℓ ≥ 3.

**Table 1 — the thirteen series.** z is the core charge, N the number of members, I the limit and A the mass used in R_M.

| series | core | ℓ | p | z | n | N | I (cm⁻¹) | A | R_M (cm⁻¹) |
|---|---|---|---|---|---|---|---|---|---|
| Cd I f | [Kr] 4d¹⁰ 5s | 3 | 0 | 1 | 4–9 | 6 | 72540.050 | 112.41 | 109736.784 |
| In I f | [Kr] 4d¹⁰ 5s² | 3 | 0 | 1 | 4–9 | 6 | 46670.107 | 114.82 | 109736.795 |
| Sr II f | [Kr] | 3 | 0 | 2 | 4–9 | 6 | 88965.180 | 87.906 | 109736.636 |
| Rb I d | [Kr] | 2 | 1 | 1 | 5–10 | 6 | 33690.810 | 84.912 | 109736.612 |
| Sr II d | [Kr] | 2 | 1 | 2 | 5–10 | 6 | 88965.180 | 87.906 | 109736.636 |
| Cd I d | [Kr] 4d¹⁰ 5s | 2 | 2 | 1 | 5–11 | 7 | 72540.050 | 112.41 | 109736.784 |
| In I d | [Kr] 4d¹⁰ 5s² | 2 | 2 | 1 | 5–10 | 6 | 46670.107 | 114.82 | 109736.795 |
| Cd I p | [Kr] 4d¹⁰ 5s | 1 | 3 | 1 | 5–8 | 4 | 72540.050 | 112.41 | 109736.784 |
| Rb I p | [Kr] | 1 | 3 | 1 | 6–11 | 6 | 33690.810 | 84.912 | 109736.612 |
| Rb I s | [Kr] | 0 | 4 | 1 | 6–12 | 7 | 33690.810 | 84.912 | 109736.612 |
| Sr II s | [Kr] | 0 | 4 | 2 | 6–11 | 6 | 88965.180 | 87.906 | 109736.636 |
| Cd I s | [Kr] 4d¹⁰ 5s | 0 | 5 | 1 | 6–12 | 7 | 72540.050 | 112.41 | 109736.784 |
| In I s | [Kr] 4d¹⁰ 5s² | 0 | 5 | 1 | 6–12 | 7 | 46670.107 | 114.82 | 109736.795 |

The series are single-parent, single-term series: Cd I ns ³S₁, np ¹P°₁, nd ³D₁, nf ³F°₃; In I ns ²S₁/₂, nd ²D₃/₂, nf ²F°; Rb I ns ²S₁/₂, np ²P°₁/₂, nd ²D₃/₂; Sr II ns ²S₁/₂, nd ²D₃/₂, nf ²F°. Eighty levels in all.

**Table 2 — the levels (cm⁻¹), CITED from NIST ASD.**

| series | n | E (cm⁻¹) | series | n | E (cm⁻¹) |
|---|---|---|---|---|---|
| Cd I s | 6 | 51483.980 | In I f | 7 | 44406.310 |
| Cd I s | 7 | 62563.435 | In I f | 8 | 44938.810 |
| Cd I s | 8 | 66682.029 | In I f | 9 | 45303.310 |
| Cd I s | 9 | 68682.325 | Rb I s | 6 | 20132.510 |
| Cd I s | 10 | 69806.814 | Rb I s | 7 | 26311.437 |
| Cd I s | 11 | 70502.040 | Rb I s | 8 | 29046.816 |
| Cd I s | 12 | 70961.993 | Rb I s | 9 | 30499.031 |
| Cd I p | 5 | 43692.384 | Rb I s | 10 | 31362.331 |
| Cd I p | 6 | 59907.280 | Rb I s | 11 | 31917.221 |
| Cd I p | 7 | 65501.412 | Rb I s | 12 | 32294.911 |
| Cd I p | 8 | 68059.393 | Rb I p | 6 | 23715.081 |
| Cd I d | 5 | 59485.768 | Rb I p | 7 | 27835.020 |
| Cd I d | 6 | 65353.372 | Rb I p | 8 | 29834.940 |
| Cd I d | 7 | 67989.814 | Rb I p | 9 | 30958.910 |
| Cd I d | 8 | 69400.900 | Rb I p | 10 | 31653.850 |
| Cd I d | 9 | 70244.090 | Rb I p | 11 | 32113.550 |
| Cd I d | 10 | 70787.850 | Rb I d | 5 | 25700.536 |
| Cd I d | 11 | 71158.957 | Rb I d | 6 | 28687.127 |
| Cd I f | 4 | 65586.000 | Rb I d | 7 | 30280.113 |
| Cd I f | 5 | 68093.700 | Rb I d | 8 | 31221.440 |
| Cd I f | 6 | 69456.400 | Rb I d | 9 | 31821.855 |
| Cd I f | 7 | 70277.400 | Rb I d | 10 | 32227.610 |
| Cd I f | 8 | 70809.700 | Sr II s | 6 | 47736.530 |
| Cd I f | 9 | 71174.200 | Sr II s | 7 | 64964.100 |
| In I s | 6 | 24372.957 | Sr II s | 8 | 73237.100 |
| In I s | 7 | 36301.864 | Sr II s | 9 | 77857.600 |
| In I s | 8 | 40636.980 | Sr II s | 10 | 80701.800 |
| In I s | 9 | 42719.020 | Sr II s | 11 | 82576.100 |
| In I s | 10 | 43881.260 | Sr II d | 5 | 53286.310 |
| In I s | 11 | 44595.860 | Sr II d | 6 | 67522.870 |
| In I s | 12 | 45067.190 | Sr II d | 7 | 74621.300 |
| In I d | 5 | 32892.230 | Sr II d | 8 | 78688.800 |
| In I d | 6 | 39048.530 | Sr II d | 9 | 81240.200 |
| In I d | 7 | 41836.410 | Sr II d | 10 | 82951.500 |
| In I d | 8 | 43335.930 | Sr II f | 4 | 60990.040 |
| In I d | 9 | 44234.700 | Sr II f | 5 | 71065.800 |
| In I d | 10 | 44815.060 | Sr II f | 6 | 76553.400 |
| In I f | 4 | 39707.590 | Sr II f | 7 | 79861.300 |
| In I f | 5 | 42220.250 | Sr II f | 8 | 82005.900 |
| In I f | 6 | 43584.660 | Sr II f | 9 | 83472.700 |

---

## §4 · The measurement

**Procedure.** For each series the defects `δ_n` of D1 are computed with the square root taken to forty significant digits and every other operation exact. The least-squares problem of D2 is solved by profiling: for fixed δ₀ the optimal `δ₂` is `Σ r_i w_i / Σ w_i²` with `r_i = δ_i − δ₀` and `w_i = (n_i − δ₀)⁻²`, and the residual sum `S(δ₀)` is an exact rational function. `S` is evaluated at 401 equally spaced points of `[min δ_i − 1, max δ_i + 1]` (capped below the first member's n), the least is bracketed, and a ternary search of ninety exact steps narrows the bracket to below 10⁻¹⁷. The minimiser is certified: `S` there is no greater than at every scanned point and at both ends of the final bracket, and every scan shows exactly one local minimum. The fit is **EXHAUSTIVE** over the thirteen series in that sense: each reported (δ₀, δ₂) is the certified least-squares solution of its series, not a converged iterate.

**Table 3 — the fits.** ρ is D5; rms is the root-mean-square residual of the fit in units of δ.

| series | ℓ | p | δ₀ | δ₂ | δ₂/δ₀ | −ℓ(ℓ+1)/3 | ρ | rms |
|---|---|---|---|---|---|---|---|---|
| Cd I f | 3 | 0 | 0.0393 | −0.1808 | −4.6009 | −4.000 | 1.150 | 0.00029 |
| In I f | 3 | 0 | 0.0416 | −0.1838 | −4.4187 | −4.000 | 1.105 | 0.00019 |
| Sr II f | 3 | 0 | 0.0648 | −0.4054 | −6.2546 | −4.000 | 1.564 | 0.00031 |
| Rb I d | 2 | 1 | 1.3504 | −0.7418 | −0.5493 | −2.000 | 0.275 | 0.00057 |
| Sr II d | 2 | 1 | 1.4514 | +0.5152 | +0.3550 | −2.000 | −0.177 | 0.00114 |
| Cd I d | 2 | 2 | 2.0837 | +0.1403 | +0.0673 | −2.000 | −0.034 | 0.00041 |
| In I d | 2 | 2 | 2.3009 | −1.0075 | −0.4379 | −2.000 | 0.219 | 0.01755 |
| Cd I p | 1 | 3 | 3.0522 | −0.0082 | −0.0027 | −0.667 | 0.004 | 0.00083 |
| Rb I p | 1 | 3 | 2.6540 | +0.3258 | +0.1227 | −0.667 | −0.184 | 0.00017 |
| Rb I s | 0 | 4 | 3.1308 | +0.1980 | +0.0633 | 0.000 | — | 0.00019 |
| Sr II s | 0 | 4 | 2.7055 | +0.3394 | +0.1254 | 0.000 | — | 0.00048 |
| Cd I s | 0 | 5 | 3.6551 | +0.3354 | +0.0918 | 0.000 | — | 0.00096 |
| In I s | 0 | 5 | 3.7193 | +0.3168 | +0.0852 | 0.000 | — | 0.00141 |

**Proposition 1 (the split).** With the classes of D3 and the statistics of D6:

> p = 0: 3 series, 3 with ρ defined — ρ = 1.105, 1.150, 1.564 — median **1.150**, population sd **0.206**;
> p ≥ 1: 10 series, 6 with ρ defined — ρ = −0.184, −0.177, −0.034, 0.004, 0.219, 0.275 — median **−0.015**, population sd **0.177**.

The means and sample standard deviations are 1.273 ± 0.253 and 0.017 ± 0.194. **MEASURED**, on the sample of Table 1.

**Robustness of the figures.** Leaving out one p = 0 series at a time moves the median to 1.334, 1.357 and 1.127 — with three points the median is one of the data. Refitting every series with the denominator `n²` in place of `(n − δ₀)²` (Lemma 3) gives p = 0: median 1.175, sd 0.221; p ≥ 1: median −0.040, sd 0.547 — the non-penetrating figures move by 0.03, the penetrating spread triples, because on a penetrating series δ₀ is of order 1 to 4 and the two denominators are no longer close. The reported figures are those of the Ritz form, which is the form in which the effective quantum number enters (Lemma 3).

**Proposition 2 (the sign of δ₂).** From Table 3, the number of series with δ₂ > 0 by p is: p = 0, 0 of 3; p = 1, 1 of 2; p = 2, 1 of 2; p = 3, 1 of 2; p = 4, 2 of 2; p = 5, 2 of 2. The fraction 0, ½, ½, ½, 1, 1 is non-decreasing in p. Theorem 1 requires δ₂ < 0 for a polarisation series and every p = 0 series obeys it; every series with p ≥ 4 has the opposite sign, which is the sign of a penetration series. **EXHAUSTIVE** over the thirteen series; a rule, not a law — the sample at each p ≥ 1 is two series.

![Figure 1](figures/fig1-ratio-vs-p.png)

*Figure 1. (a) The fitted ratio δ₂/δ₀ of all thirteen series against p, with the polarisation value −ℓ(ℓ+1)/3 drawn for ℓ = 0, 1, 2, 3. (b) ρ against p for the nine series with ℓ ≥ 1: the p = 0 class at median 1.150 with the ±0.206 band, the p ≥ 1 class at median −0.015 with the ±0.177 band.*

![Figure 2](figures/fig2-distributions.png)

*Figure 2. The two distributions of ρ: three values at p = 0 (median 1.150, sd 0.206) and six at p ≥ 1, ℓ ≥ 1 (median −0.015, sd 0.177). The bands are one population standard deviation about the median.*

![Figure 3](figures/fig3-p0-curves.png)

*Figure 3. The three non-penetrating series with their Ritz fits and, for comparison, the curve of Theorem 1 with the same δ₀ (δ₂ = −4δ₀). The fitted curvature exceeds the polarisation value by 15%, 10% and 56%.*

---

## §5 · What the split establishes, and what it does not

**1. The correction is a domain statement.** Theorem 1 is a theorem about a model whose hypothesis is that the running electron does not enter the core. Where p ≥ 1 the core holds an orbital of the electron's own ℓ, the Rydberg orbital is orthogonal to it and carries the corresponding radial nodes inside the core, and the short-range interaction — not the polarisation tail — sets the defect. Nothing in the derivation survives that, and Proposition 1's penetrating figure says so: the fitted curvature is of either sign and small against ℓ(ℓ+1)/3. A ratio reported on penetrating series, of whatever value, is a fact about those series and not a test of the relation. The relation is not "broken at d and sound at f"; it is valid at p = 0 and undefined at p ≥ 1.

**2. What p = 0 establishes.** On the three non-penetrating series the fitted ratio is within 10% and 15% of the polarisation value for Cd I and In I and 56% above it for Sr II; the median departure is 15%. The relation predicts the curvature of an f series from its limit value with no free parameter, and the prediction lands within a factor of 1.6 on all three. A first-order relation is expected to hold to that order and no better: the corrections are the quadrupole polarisability term, which adds to δ₀ a term with a different n-dependence; second-order dipole terms (Drake and Swainson 1991); and, for an f orbital outside a 4d¹⁰ or 4p⁶ core, a residual overlap that is small but not zero. Sr II, with z = 2 and the largest δ₀ of the three, sits farthest from 1, which is the direction those corrections point; it is one series, and the paper draws no more from it.

**3. What the sample cannot separate.** Every p = 0 series here has ℓ = 3, and on all four cores p = 0 holds exactly when ℓ ≥ 3 (§3). A domain stated as "p = 0" and one stated as "ℓ ≥ 3" coincide on this sample, and the data do not discriminate between them. Cores that do separate them exist — a d series on an argon-like core, which holds no d orbital (Ca II nd has p = 0 where Sr II nd has p = 1), or an f series on a core with a filled 4f shell (p = 1 at ℓ = 3) — and none is in this sample. The statement in p is the one the derivation supports, because the hypothesis is about penetration and not about ℓ; the statement in ℓ is what the sample tests.

**4. What three numbers cannot establish.** The population standard deviation of three values is a description of those three, and the median is one of them. The leave-one-out medians run from 1.127 to 1.357. The paper reports 1.150 ± 0.206 because that is the statistic on the sample; it does not claim a confidence interval.

**5. Where the relation fails, and how a failure would show.**

- *Penetration, p ≥ 1.* The hypothesis fails; the relation makes no prediction. This is the correction.
- *ℓ = 0.* The polarisation value is 0 and the ratio is undefined. The four s series have δ₂/δ₀ between 0.06 and 0.13, all positive, which is the penetration sign.
- *The limit.* A shift ΔI in the ionisation limit changes δ_n by about `n*³ ΔI / (2z²R_M)`, a term growing as n³ that the two-term Ritz fit absorbs into both coefficients. The limits of Table 1 are tabulated, not fitted, and the fit residuals of the three p = 0 series are 0.0002 to 0.0003 in δ, so no such term is present at the level the fit can see.
- *Perturbers.* A level of another channel crossing the series distorts δ(n) locally. In I nd is the one series in Table 3 whose residual, 0.0176, is an order of magnitude above the others, and its defect rises with n from 2.18 to 2.31; its ρ = 0.219 is in the penetrating class and does not enter the non-penetrating figure.
- *Fields.* External-field shifts grow as n*⁷ (magnetic) and n*¹⁰ (electric) and begin at n of order 60; the highest member here is n = 12.
- *The quadrupole term.* Where the core's quadrupole polarisability is not negligible the constant term acquires a contribution with a different centrifugal factor and the ratio is no longer −ℓ(ℓ+1)/3; the size of the departure at ℓ = 3 is not measured here.

**6. The sign rule is a second, weaker result.** Proposition 2 is exhaustive on the sample and holds at every p, but at p = 1, 2, 3 it rests on two series each. Its content is that the sign of the second Ritz coefficient follows the penetration count and not the orbital angular momentum: the d series split by p (Rb I and Sr II at p = 1 against Cd I and In I at p = 2 give one sign each), and the s series at p = 4 and 5 are uniformly positive.

---

## §6 · Verification record

| object | PROVED | EXHAUSTIVE | MACHINE-CHECKED (Z3) | CITED / MEASURED |
|---|---|---|---|---|
| Lemma 1, ⟨r⁻⁴⟩ | — | **435 states**, n ≤ 30, 1 ≤ ℓ ≤ n−1; control ⟨r⁻²⟩ on the same 435 | — | closed form for general n CITED |
| Lemma 2, energy–defect identity | ✓ | 64-point grid above degree (2, 2, 2) | — | — |
| Lemma 3, Ritz denominator | ✓ | 60-point grid above degree (2, 3, 1) | — | — |
| **Theorem 1**, c₂/c₀ = −ℓ(ℓ+1)/3 | ✓ | **2,280** exact (n, ℓ, α_d, z) points | **✓ 8 obligations**, ℓ ∈ {1..8}, α_d and z real | — |
| D3, p for the four cores | — | 16 (core, ℓ) cells; p = 0 ⇔ ℓ = 3 | — | ground configurations CITED |
| Table 2, the levels | — | — | — | CITED, NIST ASD 5.12 |
| Table 3, the fits | — | **13 certified minimisers**, one local minimum each | — | MEASURED |
| Proposition 1, the four statistics | — | 3 + 6 series | — | MEASURED |
| Proposition 2, the sign rule | — | 13 series, six values of p | — | MEASURED |

**The exhausted families, named.** 435 states: every hydrogenic (n, ℓ) with 2 ≤ n ≤ 30 and 1 ≤ ℓ ≤ n − 1. 2,280 points: every (n, ℓ) with n ≤ 20, times three values of α_d and four of z. 13 minimisers: every series of Table 1, each certified as in §4. 16 cells: the four cores at ℓ = 0, 1, 2, 3.

**The two guards on the machine check.** *Non-vacuity*: the hypothesis α_d > 0 ∧ z ≠ 0 is satisfiable. *Encoding fidelity*: the Z3 terms for c₀ and c₂, evaluated at 200 random rational (α_d, z, ℓ), agree with an independent exact implementation in every case. A negative control — the claim c₂/c₀ = −2ℓ(ℓ+1)/3 — is reported satisfiable, with a model.

**What is not machine-checked, and why.** Propositions 1 and 2 are measurements: they are recomputed from the cited levels by the stated procedure and are not of a shape a solver decides. Lemma 1's closed form for general n is cited; the exact computation reaches n = 30. The least-squares certificate of §4 is a finite check (the minimiser beats every scanned point and its bracket ends) and not a proof of global optimality over the real line; each scan showed a single basin.

---

## References

- Bethe, H. A. and Salpeter, E. E. (1957). *Quantum Mechanics of One- and Two-Electron Atoms*. Springer, Berlin.
- Born, M. and Heisenberg, W. (1924). Über den Einfluss der Deformierbarkeit der Ionen auf optische und chemische Konstanten. *Zeitschrift für Physik* **23**, 388–410.
- Drake, G. W. F. and Swainson, R. A. (1991). Quantum defects and the 1/n dependence of Rydberg energies: second-order polarization effects. *Physical Review A* **44**, 5448.
- Kramida, A., Ralchenko, Yu., Reader, J. and the NIST ASD Team (2024). *NIST Atomic Spectra Database*, version 5.12. National Institute of Standards and Technology, Gaithersburg. DOI 10.18434/T4W30F.
- Mayer, J. E. and Mayer, M. G. (1933). The polarizabilities of ions from spectra. *Physical Review* **43**, 605–611.
- Ritz, W. (1903). Zur Theorie der Serienspektren. *Annalen der Physik* **12**, 264–310.
- Seaton, M. J. (1958). The quantum defect method. *Monthly Notices of the Royal Astronomical Society* **118**, 504–518.
- Seaton, M. J. (1983). Quantum defect theory. *Reports on Progress in Physics* **46**, 167–257.
