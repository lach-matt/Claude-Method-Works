
---

# PART III — THE METHOD

---

# 13. The bracket

Everything so far has been about structure. This part asks what such a
structure can do with measurements, and the answer is deliberately modest.

## 13.1 The rule

For a Rydberg channel — fixed parent, fixed ℓ, varying *n* — the binding
energies *T* = *I* − *E* are monotone in *n*. So for any interior member:

> **T(n) lies between T(n−1) and T(n+1)**

That is the bracket. It uses **only measured neighbours**. It fits nothing,
assumes no functional form, and returns an interval rather than a value.

**It is a deduction, not a prediction.** The distinction is the whole method:
a fit says where a level probably is; the bracket says where it cannot fail
to be.

## 13.2 The bracket is limit-free

Since *T* = *I* − *E* for a **constant** *I*:

> **T(n) between T(n±1) ⟺ E(n) between E(n±1)**

Containment is invariant under the affine map. **ν, δ and *V* all need the
ionisation limit; containment does not.**

**Consequence:** the method applies wherever levels are known, even when the
threshold is not. This is not a technicality — it is what allowed the
antiprotonic-helium cells of §15.6, where the relevant threshold is
ambiguous.

## 13.3 Admissibility

A channel is admissible when its levels are separated by more than their
uncertainty:

> **r = 2*Z*²*R* / (ν³σ) ≥ 5**

*r* falls as ν⁻³. Every channel eventually leaves the domain; the rule states
where.

## 13.4 What the bracket costs

A guarantee is wider than an estimate. Chapter 14 prices it exactly, and the
price is the only linearly rising quantity in the structure.

---

# 14. The cost surface

## 14.1 The ratio

Let *w* be the bracket width |*T*(*n*+1) − *T*(*n*−1)| and *e* the
interpolation error |*T*(*n*) − ½(*T*(*n*−1) + *T*(*n*+1))|.

> **V = w / e = 4ν/3**

for a Rydberg series. And in general, for *y* = *x^p* sampled at step *h*:

> **V(x, p) = 4x / ( h · |p − 1| )**

Verified on power laws from *p* = −3 to +11, agreement under 1%.

## 14.2 V is a bound, not a tool

**V contains no σ.** Improving measurement precision by six orders of
magnitude leaves *V* = 26.689 unchanged at ν = 10.

> **No spectrometer can buy a narrower bracket. The price of certainty in a
> Rydberg series is set by the series.**

So *V* is not an instrument. It is an impossibility statement, and it makes
four:

| | forbids |
|---|---|
| *V* = 4ν/3 | a guarantee costs 4ν/3 × an estimate, and no measurement reduces it |
| *V* ≥ **32/11** | no guarantee is ever cheaper than 2.909 × |
| pole at *p* = 1 | no guarantee exists for a linear observable |
| ν_V ceiling | above it the cost cannot be *measured*, though it stays defined |

**The exact *V* is rational at every ν** — 32/11, 54/13, 256/47, 250/37,
4000/299 — and 4ν/3 + 4/(9ν) is its asymptotic form, low by 0.69% at ν = 2 and
exact to four decimals by ν = 10. **The floor 32/11 belongs to the exact
expression, not to the asymptote.**

## 14.3 The exponent axis

Two involutions act on *p*: **cost**, *p* ↦ 2 − *p* (paired values multiply to
*x*²); and **virial**, *p* ↦ −*p* (paired values multiply to a constant).
Composed, they generate translation by 2, so exponents fall into **two orbits
by parity** — and the parity is *b*, the number of energy denominators.

**The pole at *p* = 1 sits in the odd orbit.** Nothing built purely from
powers of ⟨*r*⟩ can reach it.

## 14.4 Inversion

|*p* − 1| = 4*x*/(*hV*), and the sign is fixed by sign(*y*′) and sign(*y*″).
Controls recover *p* = −1 and −3 correctly; 9 of 10 within 5%.

**On real data:** Na I −1.993, K I −1.998, C₃ 3.999, α 6.990, **C₆ 10.956.**

## 14.5 The second admission bound

> **ν_V = (3*Z*²*R* / 5*q*)^{1/4}**

for quotation granularity *q*. The bracket needs levels **separated** (ν⁻³,
governed by *r*); the cost needs curvature **resolved** (ν⁻⁴, governed by
ν_V).

**Curvature washes out before separation, in every channel in this work.**

| channel | *q* | ν_V | ν reached |
|---|---|---|---|
| K I *n*d | 0.0001 | 160 | 45.7 |
| Na I *n*s | 0.001 | 90 | 20.0 |
| **Al I *n*f** | **0.01** | **50.7** | **55.0** |

**Al I *n*f is the first channel to reach its own ceiling.** Predicted 50.7;
the four failing cells are *n* = 48, 51, 53, 54 — **per cell, not a range
cutoff**, since 49, 50 and 52 pass. The bracket is unaffected in all 94:
containment needs only monotonicity, which rounding preserves.

**And in Li I, ν_V was applied prospectively** — eight of fifty-five cells
excluded from the cost test *before it ran*, because the ASD's quotation
coarsens above *n* = 33. That is the difference between a bound derived and a
bound noticed.

---

# 15. The collection

**1,442 interior cells across 35 atomic systems. The bracket holds in every
one.**

## 15.1 What it spans

| axis | span |
|---|---|
| ℓ | **0 through 6** |
| *Z* | **1 through 83** |
| *Z*_eff | 1 through 3 |
| core types | **23, all characterised** |
| isoelectronic pairs | **5**, each at two charge states |

**Cores tested:** bare · 1s ²S · 1s² ¹S₀ · 1s²2s ²S · 2s² ¹S₀ · 2p⁵ ²P° ·
2p⁶ ¹S₀ · 3s ²S · 3s² ¹S₀ · 3s²3p ²P° · 3p⁴ · 3p⁵ ²P° · 3p⁶ ¹S₀ · 3p⁶4s ²S ·
3d¹⁰ ¹S₀ · 3d⁹ ²D (declined) · 3d¹⁰4s² ¹S₀ · 4p⁵ ²P° · 4p⁶5s ²S · 4d¹⁰ ¹S₀ ·
5p⁶ ¹S₀ · 5p⁶6s ²S · 5d¹⁰ ¹S₀ · 3d4s ³D · 6p² ³P.

## 15.2 The largest contributors

| species | core | channels | cells |
|---|---|---|---|
| **He I** | 1s ²S | 9 | **189** |
| **Ne I** | 2p⁵ ²P°, two limits | 16 | **131** |
| K I | 3p⁶ ¹S₀ | 4 | 105 |
| Al I | 3s² ¹S₀ | 4 | 94 |
| Na I | 2p⁶ ¹S₀ | 6 | 80 |
| Ga I | 3d¹⁰4s² ¹S₀ | 5 | 61 |
| Li I | 1s² ¹S₀ | 3 | 55 |

## 15.3 He I — the angular span

Nine channels, ℓ = 0 through 6, singlets and triplets, *n* to 35. And the
defect falls monotonically with ℓ:

> 0.2965 (s³) · 0.1392 (s¹) · −0.0133 (p) · +0.0014 (d) · −0.0010 (f) ·
> −0.0014 (g) · **−0.0016 (i)**

**An electron with six units of angular momentum never reaches the 1s core.**

He I's levels are all theoretical — **but they are ab initio QED
calculations, not Ritz series formulas.** That distinction matters and §15.7
develops it.

## 15.4 He II — the δ = 0 edge itself

A hydrogenic ion at *Z* = 2. Its defects run **7.6 × 10⁻⁵ at ℓ = 0 down to
1.6 × 10⁻⁶ at ℓ = 6**, monotone across six orders of magnitude, and never
reach zero.

**There is no core to penetrate.** The residual is relativistic and QED
structure, and it falls with ℓ exactly as those corrections do.

**And the ionisation limit came out of the data.** Minimising the δ spread
over the *n*g channel gives **438,908.871 cm⁻¹** against the tabulated
438,908.885 — **agreement to 0.014 cm⁻¹, three parts in 10⁸**, from a
criterion that never used the tabulated value.

## 15.5 Bi I — the charge span

Atomic number 83, more than double anything previously tested. The 6p³ ground
term is strongly j-j coupled and the levels carry jK labels throughout.
**δ̄ = 4.90 for the *n*s channel** — the largest defect in this work, as
expected when a 6s-like electron penetrates a filled 5d¹⁰6s² core.

**And Bi I settles a rule.** Its core carries five J levels — the same
dilution that made neon II fail entirely — but its ³P₀ parent reaches *n* = 11.

> **Dilution divides. It does not forbid.**
>
> cells per channel ≈ (measured shells / D) − 2

Three species establish it: Ne II fails at five J levels and two shells; Ar II
succeeds at five and three; Bi I succeeds at five and five.

## 15.6 The isoelectronic pairs

| sequence | *Z*_eff = 1 | *Z*_eff = 2 |
|---|---|---|
| helium-like | He I | Li II |
| lithium-like | Li I | Be II |
| sodium-like | Na I | Mg II |
| aluminium-like | Al I | Si II |
| potassium-like | K I | Ca II |

**Same electrons, different nuclear charge, the method run identically.** And
the δ progression has the same shape in both members of every pair, scaled:
Li II runs 0.182 → 0.054 → 0.002 → 0.0002 across s→f; Be II runs 0.262 →
0.049 → 0.002 → 0.0001.

**Li II and Be II both give ℓ = 5 defects near −0.0003 with a real two-electron
core** — the cleanest demonstration in the collection that **penetration, not
the presence of a core, creates a defect.**

## 15.7 A caveat the collection forced

The ASD marks series-formula values in brackets. Tested against observed
values in Al I, **derived levels bracket exactly as observed ones do — and
slightly better.**

**That is not a validation.** Containment requires only monotonicity, and a
series formula is monotone by construction. **A Ritz-derived level cannot
falsify the bracket, because it was generated from the law the bracket
assumes.**

> **Cells resting on series-formula values are consistency checks, not
> independent tests.**

**But bracketed values are not one category.** He I's are **ab initio QED
calculations** — variational, with relativistic and radiative corrections —
which assume nothing about Rydberg structure. Those are genuine tests, and at
uncertainties of 10⁻⁹ cm⁻¹ they are sharper than any measurement here.

## 15.8 Two cross-checks

Al I and Al II were held from two independent sources — the NIST compilations
and the ASD.

> **Al II: 36 of 36 levels identical to machine precision.**
> **Al I: one disagreement in 40** — 3s²11d, ASD 47379.7 against Kaufman &
> Martin 47379.140, **Δ = 0.560 cm⁻¹.**

The K&M value is the more precise measurement and is the one used. **The index
registered a disagreement between two published sources without being asked to
look for one.**

## 15.9 Four ways a species declines

**A collection reporting only successes cannot be checked.**

| species | cause | cells |
|---|---|---|
| **Ne II** | dilution — 5 core J levels, only 2 shells measured | **0** |
| **Ar II** | same dilution, **beaten by depth** | 10 |
| **Si I, P II** | coupling scheme changes LS → jK mid-series | 4, 1 |
| **Cu II** | **core-excited configurations interleave the series** | **0** |
| Bi II, Bi III | mixing to 34% leading percentage; a third limit inside range | 0 |

**Cu II's is a structural exclusion.** Its 3d⁸4s4p levels sit at
107,942–111,124 cm⁻¹, straddling the 3d⁹5s Rydberg levels at 108,014–110,366.
The series is buried in core-excited states.

> **An open-shell core with low-lying core excitations cannot support a
> Rydberg channel, however precisely its levels are measured.**

And that predicts the same outcome for every open-*d* and open-*f* sequence
**without fetching any of them** — which the census of §15.10 confirms
independently.

## 15.10 The census, computed rather than searched

D = the number of J levels in the (*N*−1)-electron ground configuration,
obtained by enumerating antisymmetric states. **No spectroscopic data enters.**

> **27 sequences admitted (D ≤ 2) · 12 needing exceptional depth · 5 excluded**

The five are **Cr-, Mn-, Fe-, Co- and Ni-like**, with D running from 19 to 37.
**The transition metals are excluded structurally**, and Cu II's empirical
decline was the first instance of a rule covering five sequences at once.

## 15.11 What the structure determines, and what it does not

Given five isoelectronic pairs and two four-point sequences, how much of an
unmeasured species can be derived?

**Fitting δ(*Z*) = δ_∞ + *a*/*Z* + *b*/*Z*² and holding one member out:**

| held out | lithium-like | sodium-like |
|---|---|---|
| **neutral, *Z* = 1** | **11.1%** | **23.4%** |
| *Z* = 2 | 1.4% | 2.4% |
| *Z* = 3 | 0.8% | 1.3% |
| *Z* = 4 | 1.8% | 2.5% |

> **Interpolation works to about one percent. Extrapolation to the neutral
> does not.**

**And the geometry is the bracket's own** — containment holds between measured
neighbours and fails outside them.

| | |
|---|---|
| across sequences | δ **not** determined; the *Z*=1→2 ratio spans 0.53–0.83 |
| within a sequence, interior | δ determined to ~1% |
| within a sequence, at an end | δ **not** determined |

> **Interior members need not be fetched. The ends always must — and the
> neutral is always an end.**

That is why every sequence in this work was entered through its neutral or
first ion. It was not convenience; it was forced.

---

# 16. Domain, failure, and the bound in the silence

## 16.1 A method that has never failed has not been tested

**1,442 cells, no bracket failure.** Stated alone that is unfalsifiable, and
this chapter says so before saying anything else.

## 16.2 The failure condition

> **The bracket fails ⟺ |Δ*T*| > 2*Z*²*R*/ν³**

A perturber **shifts** a level; it **reorders** one only if the shift exceeds
half the local spacing.

**Tested on the strongest mixing in the work.** Hg II's 5d¹⁰7p sits at 60%
leading percentage with 20% admixture, and the 5d⁹6s6p perturbers lie
2,000–3,000 cm⁻¹ away. **The half-spacing at *n* = 7 is 24,634 cm⁻¹.** The
level is displaced by a tenth of what reordering would require.

**And the condition predicts where failure would occur:**

| perturbation | ν_fail (*Z* = 1) | ν_fail (*Z* = 2) |
|---|---|---|
| 3,000 cm⁻¹ | 4.2 | **6.6** |
| 1,000 | 6.0 | 9.6 |
| 100 | 13.0 | 20.6 |
| 10 | 28.0 | 44.4 |

**Hg II's *n*p reaches ν = 5.3. It is not deep enough to fail.**

## 16.3 Why the collection never enters the failure regime

**The two requirements are anticorrelated in nature.** Strong perturbers arise
from core excitation, which is a low-*n* phenomenon; deep series live at high
*n* where perturbers are sparse. **Large Δ*T* and large ν rarely coexist.**

That is why the bracket has not failed — stated as physics, not as luck.

## 16.4 The bound in the silence

Read the condition backwards:

> **the bracket held ⟹ |Δ*T*| < 2*Z*²*R*/ν³ at that cell**

**Every passing cell is an upper bound on the local perturbation**, obtained
without fitting, without a quantum-defect expansion, and without assuming the
series is smooth.

**1,061 cells contribute bounds. The tightest:**

| species | channel | *n* | ν | \|Δ*T*\| < |
|---|---|---|---|---|
| **Al I** | 3s²*n*f | 54 | 54.0 | **1.398 cm⁻¹** |
| **Ga I** | 4s²*n*p | 54 | 51.7 | **1.585** |
| Li I | *n*p | 42 | 41.8 | 3.25 |

**These are statements about the atom:**

> **No configuration interacts with Al I 3s²54f by more than 1.4 cm⁻¹.**

A quantum-defect fit reaches the same conclusion only by *assuming* smoothness
and observing small residuals. **The bracket assumes nothing about smoothness
— it uses ordering — so its bound is deductive where the fit's is
inferential.**

> **Before:** 1,442 cells, no failure. Unfalsifiable.
> **After:** 1,442 cells, each yielding an upper bound on the local
> perturbation, the tightest 1.398 cm⁻¹.

Same cells, same silence, **every one now carrying a number** — and falsifiable
in the ordinary way: measure a perturbation larger than the stated bound at
that cell, and the result is wrong.

## 16.5 The one prediction

Every verified cell in this work lies at *Z*_eff between 1 and 3. A
measurement of Sc VI (⁴S°)6s would place the method at ***Z*_eff = 6** —
double the highest charge state tested — **falsifiable to about half a per
cent.**

It is offered as a target, not a result.

---

# 17. Collective sections

## 17.1 The assembly rule

An observable built as ⟨*r*⟩^*a* / (Δ*E*)^*b* scales as

> **ν^{2a + 3b}**

**Derived, not fitted**, from ⟨*r*⟩ ∝ ν² and Δ*E* ∝ ν⁻³.

| observable | *a*, *b* | *p* |
|---|---|---|
| ⟨*r*⟩ | 1, 0 | 2 |
| cross-section, C₃, quadrupole, diamagnetic shift | 2, 0 | 4 |
| polarisability α | 2, 1 | 7 |
| **C₆** | 4, 1 | **11** |
| C₈ | 6, 1 | 15 |

**Scope, stated.** The rule covers observables assembled from ⟨*r*⟩ and Δ*E*.
**Hyperfine coupling is excluded** — it scales as ν⁻³ through |ψ(0)|², which
is neither a matrix element nor a denominator.

## 17.2 One dimension, fifteen perspectives

Across fifteen Rydberg quantities and forty values of ν, the centred
log-matrix has singular values 9.49 × 10¹, then **1.8 × 10⁻¹⁴**.

> **rank(log **q**) = 1**

**One dimension. Fifteen perspectives.** Every Rydberg property is ν to a
power, and the exponent is the whole of its identity.

## 17.3 Collective coefficients are not a separate class

**C₆ = ν¹¹ is (ν²)⁴/ν⁻³** — four single-atom dipole factors over one
single-atom denominator. **The two-atom quantity is assembled from the
one-atom ν and nothing else.**

## 17.4 Error amplifies as the exponent — which is the point

A fractional error ε in ν gives *k*ε in an observable of exponent *k*. Inverted:

> **measuring C₆ to 1% fixes ν to about 0.085%** — roughly nine times sharper
> than the three-level bracket achieves.

**The collective quantity is the most sensitive probe of dimension 1.**

## 17.5 Tested against a published parameterisation

Singer *et al.* (2005) give C₆ = *n*¹¹(*c*₀ + *c*₁*n* + *c*₂*n*²) for Rb
*n*s–*n*s. The quadratic factor makes the **local exponent move**:

> *p*_eff = 11 + *n*(*c*₁ + 2*c*₂*n*)/(*c*₀ + *c*₁*n* + *c*₂*n*²)

running from **12.58 at *n* = 35 to 11.44 at *n* = 100.**

**The cost law tracks it: median error 1.05%, maximum 1.83%**, across nine
points. **Bracket 66 of 66.**

## 17.6 And the bracket is the wrong tool here

**C₆ comes from a closed-form fit at every *n*.** Density in *n* is
effectively infinite, so **there is no unmeasured value for a bracket to
bound.**

> **The bracket is worth something only where the quantity is sparse in *n*.
> C₆ is dense. Collective sections are the wrong place to deploy it.**

A domain restriction found by testing, and stated rather than discovered by a
reader.