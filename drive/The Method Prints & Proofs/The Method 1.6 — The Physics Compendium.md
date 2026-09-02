# The Physics Compendium

Generated from `mathreg.py` and `SPECTRA-DATA.tsv` on 2026-08-12. **248 registered objects, 17 of them physical mechanisms.**

This compendium states the **interface** between a physical quantity and the index that holds it. It is not a list of mechanisms — those are in `MECHANISMS.md` and the Mathematical Compendium, and a third copy would drift as register 778's list did. It states, for each index, what the cells stand for, what number is attached to them, the rule taking one to the other, which constants that rule requires, **what must be measured rather than computed**, and what physics does and does not do.

Four faults in a single session were transitions performed without their rule written down: register 868 used R∞ for every species where the reduced-mass constant is correct; register 879 wrote Li III's ionisation limit as a formula where a measurement was required; register 766 passed atomic numbers where the core's charge is needed; register 782 set a verification column equal to its own denominator. **This document exists because those four share one cause.**

---

## Λ — the elemental index

**What it indexes.** Electron configurations of the ground states of the elements, on eight coordinates (n, ℓ, k, q, e, f, g, 2S). **976 cells.**

**The quantity.** None. A cell of Λ carries no physical number: it is an *arrangement*, not a measurement.

**The transition.** A configuration is read off the aufbau order and its subshells mapped to coordinates. `L.real` establishes that Λ's eight constraints hold on 247 real subshells across all 118 elements — **18,288 tests, no failures**.

**Constants required.** None.

**Must be measured.** Nothing. Λ is closed — |Λ| = |ℛ(Λ)| = 976, **E(Λ) = 0** — and the partition identity holds exactly: 6,912 = 976 + 0 + 5,936 (register 833).

**What physics does.** It supplies the aufbau ordering and the shell capacities, and nothing else. **What it does NOT do:** confer predictive power. §24 states that Λ *"contains no physics that was not already in the quantum numbers; it is a recoding … a recoding adds nothing."* Register 834 measured the consequence: on the same closed index, the T-bracket passes 789 of 789 and the δ-bracket passes 546 of 789. **Closure coexists with a bracket that holds and one that fails, so it cannot be what makes either true.**

---

## Λ_spectra — the index of Rydberg channels

**What it indexes.** Rydberg series: a fixed parent core, a fixed ℓ, n running. **596 channels across 70 spectra, 2,269 interior cells.** The complete index over the same alphabets is closed: |X| = |ℛ(X)| = 624, **E = 0** (register 853).

**The quantity.** The **quantum defect** δ — a continuous real number measuring how far the Rydberg orbital penetrates the ionic core. It is not an integer and has no factorization (register 896).

**The transition.** For a level at energy E below a limit I,

        n* = Z_c √( R_M / (I − E) )        δ = n − n*

**Constants required, and which value:**

  - **Z_c — the charge of the CORE, not the atom.** NIST states the formula as E_nl = −Z_c²/(n−δ)², *"where Z_c is the charge of the core"*. Be III and B III are third spectra and take Z_c = 3, not 4 and 5. Passing atomic numbers gave defects of −2 to −5 with spreads above 1.0 (registers 766, 883).
  - **R_M — the reduced-mass Rydberg, R∞/(1 + mₑ/M), not R∞.** For helium 109,722.386 against 109,737.316. Using R∞ understates every defect by n*(√(R∞/R_M) − 1) — 0.00240 for helium at n* = 35 — which drove He I's high-ℓ defects **negative**. Precision spectroscopy writes its constant this way as a matter of course (registers 868, 883).
  - **The exception.** Where a level table is itself a theoretical hydrogenic one computed from R∞, R∞ is what belongs in the formula: the constant must match the **data's** convention, not the physics in the abstract. Applying a reduced mass to Li III's table drove its spreads from 0.0000 to 0.0125 (register 872).

**Must be measured, not computed.** **The ionisation limit.** Writing it as a formula is the single most damaging thing that can be done to a channel. Li III's limit was recorded as *"Z²R = 9 × 109737.31568 (hydrogenic, Z=3)"* — a bare Coulomb expression that omits the QED and relativistic terms. Fitting the limit from the series gives **987,662.29 ± 0.36, higher by 26.45 cm⁻¹**, and every Li III channel moves from −0.0038…−0.0082 to a uniform **+0.0003** (register 879). The same deficit appears at B V scaled by Z⁴: **678 cm⁻¹ above 25R∞** (register 895).

**How a wrong limit announces itself.** A defect that should be constant instead deviates, and **the power of n\* names the cause**:

        n*³    a shift in the ionisation limit
        n*⁷    a magnetic field       — needs tens of tesla
        n*¹⁰   an electric field      — begins at n > 60

**Two of the three cannot fire on this compendium.** Its highest member anywhere is **n = 56** (Si I's nd (3/2,5/2)); eight channels exceed n = 40 and **none exceeds 60**. So every residual chased here was a limit, and none was a field — not by luck but because ASD's tables stop below where field effects begin (register 915).

**And the limit term's tolerance is published: a shift of even 0.2 cm⁻¹ "causes totally different behavior of quantum defect versus n".** Li III's was **26.45** — a hundred and thirty times that (register 914).

Li III's residual went as n³ and the limit was the fault. This is published and was derived independently here (registers 877, 885).

**Where the index STOPS, and why that is a decision.** Λ is finite because all 118 ground configurations are known within its caps. **The spectra index is not**: Rydberg series are unbounded in n and ℓ runs to n−1, so it is **infinite unless capped**, and every cap is a choice. Three defensible ones give:

        the measured alphabet          1,312 cells    E = 1,084
        charge 1..Z−1, elements held   4,376 cells    E = 4,148
        all 118 elements, l 0-7       55,224 cells    E = 54,996

**A factor of fifty between them, and all three close when complete.** Closure is a result about ℛ; the E that accompanies it is a result about the cap. At the physical cap the compendium holds **0.413%** — Λ holds 100% within its own (registers 959–962).

**What physics does.** It sets δ through core penetration, and the sixteen mechanisms in `MECHANISMS.md` describe how. **What it does NOT do:** make δ an integer, or give the index predictive power over cells it does not contain. Of 624 cells, 160 are measured and **193 are fully isolated** — no measured channel adjacent in ℓ or in an isoelectronic sequence, so no bound reaches them (register 890).

---

## The point of observability — what the equation actually delivers

**The quantum defect is a phase shift.** Outside the ionic core, where the potential is purely Coulombic, the radial Schrödinger solution is a superposition of the regular and irregular Coulomb functions:

        ψ  =  cos(πδ)·f(E,ℓ,r)  −  sin(πδ)·g(E,ℓ,r)

and **πδ is the phase shift with respect to the pure hydrogenic solution**, due to all short-range non-Coulombic interactions at r < r_c. Seaton's theorem continues it across threshold, δ_ℓ(0) = πμ_ℓ(0), so the same number describes bound levels and scattering.

**The consequence, and it is sharp.** The equation depends on δ only through cos πδ and sin πδ. **What it determines is δ modulo 1. The integer part is not in the equation** — it is supplied afterwards by counting nodes inside the core, and it is a labelling, not a measurement.

**What this costs the compendium.** Register 891 tested the rule *floor(δ) = (core orbitals of that ℓ) − 1* and found it holding for 318 of 407 channels — 78%, with Al I's ns at 1.767 where the rule requires 2.x. **It was testing a convention.** And testing P.lcollapse both ways:

        on the full defect        150 correct,  8 inverted   94.9%
        on δ mod 1 (observable)   127 correct, 31 inverted   80.4%

**The ordering survives on the assigned value and degrades on the observable one.** So P.lcollapse is a statement about node-counting as much as about penetration. Only **96 of 431** channels have |δ| > 1 at all — the rest have no integer part to assign, and for them the distinction does not arise (registers 910–913).

**The general rule this gives.** *A mechanism that holds on the assigned value and fails on the observable one is a statement about the index, not about the atom.* That is §24's distinction — a recoding adds nothing — reappearing at the level of a single number rather than a whole lattice.

---


---

## Kinematic and stateful — an interface the register found in its own objects

**A geometric hypothesis cannot do a state's work, and the register's one OPEN object is what happens when it is asked to.**

`M.C1` assumes Θ = 0 — the non-expanding condition, geometry and nothing else — and it succeeds: the presymplectic form is block diagonal in y and the commutator is (1/4√q) sgn(u−u′) δ^(d−2)(y−y′). **`M.C2` adds exactly one hypothesis, *ω Hadamard*, and that is a condition on a STATE.**

**Every obstruction encountered sits on the stateful side:**

  - a geometric modular flow needs a Killing vector — the flow is stateful and the geometry must match it
  - half-sided modular inclusion ⟺ a positive generator, and positivity is a property of a state
  - Θ = 0 is invariant under ℓ → a(y)ℓ, so **the geometry does not fix the state**
  - smoothness supplies a *local* Hartle–Hawking state, and local states do not glue
  - Hadamard is microlocal and therefore too weak to select one
  - and uniqueness, where it is available at all, needs invariance under a Killing flow

**And the split is NOT geometry against state, which was the first reading and was wrong.** The standard definition of a non-expanding horizon has three conditions and the third is *"Einstein field equations hold on Δ, and the stress-energy tensor T_ab is such that −T^a_b ℓ^b is future causal"* — **an energy condition, hence a condition on the state.** Through the kk-component of the Einstein equation it forces the null-null flux T_ab ℓ^aℓ^b and the shear σ_ab to VANISH, giving £_ℓ q_ab = 0. *So `M.C1`'s hypothesis is not an assumption but a consequence of the horizon's own definition, which is why it succeeds.*

**What the condition does not do is reach the right order.** It fixes the BACKGROUND — vanishing shear, vanishing null flux — while the linearised Raychaudhuri ∂_u δΘ = −8πG_N T_uu carries T_uu ≠ 0 on the perturbations, which is what the theory is about. **Half-sidedness is a spectral statement about those perturbations, and future-causality of −T^a_b ℓ^b is not one** (registers 1038–1042).

**The dimensional ledger states the split arithmetically**: d − 1 = 1 + (d − 2), one HSMI per generator supplying the affine line and the transverse direct integral coming from the kinematic side. *The stateful object supplies one dimension; the kinematic one supplies d − 2.*

**And it explains a result that otherwise looks like luck.** Computing the free half on one generator gives a positive translation generator immediately — negative to positive spectral weight 5 × 10⁻⁵ — **because a state was supplied by hand, the vacuum on a null line.** *The moment a state is given the inclusion follows; nothing on a non-expanding horizon gives one.* Registers 1033–1037.


---

## Placing a cell and valuing it are different operations

**ℛ places. Mechanisms value.** The distinction is invisible in Λ, where a cell is an arrangement and carries no number, so recovering the cell recovers everything. It is the whole difficulty in Λ_spectra, where the cell carries a quantum defect and that is its entire content.

        placed by ℛ          1,762 of 1,775 cells      99.3%
        valued               525                        32%

**A relation is usable as a STEP — carrying a value from one cell to another — only where the physics has collapsed to ONE PARAMETER.** Measured on pairs where both cells are known, as a geometric scatter:

        Nₑ at fixed charge ÷ Thomas-Fermi, s+p, Nₑ ≥ 9     1.07
        elem, s+p, Nₑ ≥ 9, raw                            1.10
        ℓ at ℓ ≥ 4, Seaton's ratio, filtered              1.12
        charge at fixed Nₑ, s                             1.23
        charge at fixed Nₑ, p                             1.38
        ℓ at p, d, f                                      3.31
        elem, all ℓ and Nₑ                                3.85
        Nₑ at fixed charge, raw                           4.12

**Above ℓ = 4 the electron never enters the core and only the polarisability matters — one number, and Seaton's formula follows. At ℓ ≤ 1 with Nₑ ≥ 9 penetration is statistical and Thomas-Fermi governs. At ℓ = 2, 3 or Nₑ < 9 neither dominates**, and four separate corrections — Seaton's ratio, core-orbital counts, the defect's own magnitude, a free Thomas-Fermi exponent — each left the scatter where it was.

**The transition zone is not a missing systematic. It is the absence of one**, and those cells require measurement rather than propagation (registers 1102–1118).

## Where relativity enters, and where it does not

**One place: the ionisation limit of a hydrogenic ion.** A Coulomb expression Z²R gives the limit only to order (Zα)². The Sommerfeld correction — special relativity applied to the atom in 1916, and shown by Gordon and Darwin to follow exactly from the Dirac equation — adds

        ΔE = Z⁴ α² R_M / 4        for the 1s state

**Measured against the reduced-mass baseline Z²R_M, three hydrogenic species give:**

        Li III   deficit 103.94   Dirac 118.32   ratio 0.878
        Be IV    deficit 329.80   Dirac 373.97   ratio 0.882
        B V      deficit 816.68   Dirac 913.03   ratio 0.894

**0.8849 ± 0.0069 across Z = 3, 4, 5** (register 906). The missing 11.5% is the **1s Lamb shift**, which raises the level and reduces the binding; it goes as α³Z⁴ against Dirac's α²Z⁴, so their ratio is order α times a slowly varying function — which is why three elements agree to under one per cent (register 908).

**The practical consequence.** Register 879's Li III fault was a Coulomb expression used where a relativistic one was required: the limit was written as 9R∞ and was low by 26.45 cm⁻¹, showing as a spurious defect of −0.0048 growing as n³ across every ℓ. **A hydrogenic limit computed rather than measured will always be low by this term.**

**Where relativity does NOT enter.** General relativity has no measurable term at these energies, and the compendium makes no use of it. The relativistic content here is entirely the special-relativistic kinetic correction, spin-orbit coupling and the Darwin term — the three that make up fine structure — plus the QED Lamb shift, which is not relativity at all (register 909).

---

## The bracket — the transition from a channel to an interval

**What it indexes.** An interior cell: a series member with a measured neighbour on each side.

**The quantity.** Not a value but an **interval**, and the book is explicit that this is the point: §22 says it *"fits nothing, assumes no functional form, and returns an interval rather than a value. It is a deduction, not a prediction."*

**The transition — and there are TWO, which the book does not distinguish.**

  - **§22.1, on binding energy.** T = I − E is monotone in n, so T(n) lies between T(n−1) and T(n+1). **Passes 789 of 789.** A Rydberg series rises toward its limit by construction, so this form **cannot fail** (registers 797, 800, 830).
  - **§25.6.1, on the defect.** δ(n) lies between δ(n−1) and δ(n+1), resting on *"within a channel, δ falls monotonically with n"*. **Passes 546 of 789.**

**The trade-off, stated.** §22.1's bracket is a genuine deduction and carries no information. §25.6.1's carries information and is not a deduction. **Chapter 22's modesty is exactly what buys the 100%, and the price is that the 100% was never evidence** (register 803).

**And the monotonicity claim is the wrong form.** The extended Ritz expansion is

        δ(n) = δ₀ + δ₂/(n−δ₀)² + δ₄/(n−δ₀)⁴ + …

and **caesium's nF series is measured with δ₂ = −0.2014(16) — negative — its defects RISING** with n. So the law is that **δ approaches δ₀ monotonically**; the direction is sign(δ₂), a property of the channel, and falling is only the common case (register 858).

**What physics does.** It guarantees the monotonicity of T. **What it does NOT do:** guarantee the monotonicity of δ, which holds in 113 of 130 resolved steps — 87%, interval 80–92% — and only where a step exceeds its own uncertainty. With error estimated from quoted decimals instead, the same test gives **55%**, and the intervals do not overlap (register 822).

---

## What the interface still does not state

**Uncertainties.** Five of 49 species files carry a quoted uncertainty column. The monotonicity law is testable only where a step can be distinguished from its own error, and **44 of 49 species do not supply what that needs** (register 807).

**The bracket's own inputs.** `channels.py` writes `bracket = "untested"` for every channel it builds, because running the bracketing method needs measured neighbours and a tolerance and the script supplies neither. **285 of 431 channels are unverified on the compendium's central claim**, and the column says so rather than asserting a verification that never ran (register 782).

**Appendix B's inputs.** 133 channels were lifted with their values and without their levels. `spectra_raw/` holds no He I file, so when register 868 corrected the Rydberg constant those channels **could not be recomputed**. *A result kept without its inputs cannot be corrected when its method is* (register 871).

---

# Λ_phys — THE INDEX OF PHYSICAL PARAMETERS

**Every number the work takes from physics, with what it is, where it comes from, and where it stops being right.** *A parameter with no stated failure mode is a parameter being used outside a domain nobody has checked.*

**22 parameters.** Coordinates: **kind** (exact → fitted), **source** (mathematics → this work), **domain** (universal → one species), and how many registered objects rest on it.

## What the index shows about the work's dependence

| kind | universal | all elements | a region | one species |
|---|---|---|---|---|
| **exact by definition** | 2 | 0 | 0 | 0 |
| **measured constant** | 2 | 0 | 0 | 1 |
| **read from a table** | 0 | 3 | 2 | 1 |
| **derived here** | 0 | 2 | 1 | 0 |
| **fitted here** | 0 | 1 | 6 | 1 |

**8 of the 22 parameters are this work's own.** *Of those, **0 are universal**, 1 hold across all elements, and **7 hold only in a region or for one species.** No number this work fitted claims wide validity.*

**And the dependence concentrates on TABLES, not on constants.** The three parameters carrying the most objects are all read rather than fitted:

| parameter | objects resting on it | kind |
|---|---|---|
| ionisation limit | **25** | read from a table |
| aufbau ordering | **19** | read from a table |
| Janet block boundary | **15** | read from a table |
| subshell capacity | **12** | exact by definition |
| angular momentum bound | **12** | exact by definition |
| Hund's first rule | **12** | read from a table |

## The parameters

### subshell capacity — `4l+2`

**exact integer** · exact by definition · from published literature · valid universal · 12 objects rest on it

**What it is.** the number of electrons a subshell of angular momentum l can hold: 2 spin states times 2l+1 orbital states.

**Where it comes from.** Stoner, The distribution of electrons among atomic levels, Phil. Mag. 48 (1924) 719-736; made exclusive by Pauli, Z. Phys. 31 (1925) 765-783

> **Where it fails.** for parastatistics of order m the capacity is m(4l+2) -- T.para shows the index still closes, so the constraint is a cap and not a magic number.

### angular momentum bound — `l <= n-1`

**exact integer** · exact by definition · from published literature · valid universal · 12 objects rest on it

**What it is.** the orbital angular momentum of a bound state cannot reach the principal quantum number; it is the condition for the radial function to have a node structure.

**Where it comes from.** Bohr, Phil. Mag. 26 (1913) 1-25; Schroedinger, Ann. Phys. 79 (1926) 361-376

> **Where it fails.** never within non-relativistic quantum mechanics.

### Rydberg constant — `R_inf`

**109737.31568 cm^-1** · measured constant · from international standard · valid universal · 9 objects rest on it

**What it is.** the binding energy of a hypothetical one-electron atom with an infinitely heavy nucleus, expressed as a wavenumber. It sets the scale of every atomic term value.

**Where it comes from.** Rydberg, K. Sven. Vetensk. Akad. Handl. 23 (1890) for the empirical constant; value CODATA 2018, uncertainty 1.9e-6 cm^-1 -- eleven significant figures

> **Where it fails.** never as a constant; but using it in place of the reduced-mass R_M is wrong for every species (register 868). The error is 1 part in 1836 A, largest at hydrogen.

### proton-electron mass ratio — `m_p/m_e`

**1836.15267343** · measured constant · from international standard · valid universal · 9 objects rest on it

**What it is.** the ratio of the proton rest mass to the electron rest mass; the quantity that makes the reduced-mass correction small but not negligible.

**Where it comes from.** CODATA 2018, uncertainty 1.1e-10

> **Where it fails.** never; it enters only through R_M, so an error here is an error there.

### Cs I np defect — `3.5667`

**measured** · measured constant · from published literature · valid one species · 2 objects rest on it

**What it is.** the limiting quantum defect of the caesium np series, the compendium's only MEASURED far anchor.

**Where it comes from.** arXiv:1706.06237 (2017), n = 70-100; earlier 3.55925 at n = 9-50 (Lorenzen & Niemax, Z. Phys. A 315, 1984)

> **Where it fails.** the two values differ by 0.007 because of stray-field shifts; the compendium uses the field-free one.

### ionisation limit — `I`

**per species, cm^-1** · read from a table · from published literature · valid one species · 25 objects rest on it

**What it is.** the energy at which a Rydberg series converges -- the term value of the ion's ground state relative to the neutral. Every defect is measured against it.

**Where it comes from.** the extrapolation method is Rydberg 1890 and Ritz, Ann. Phys. 12 (1903) 264-310; values from NIST ASD where published, built by summing two spectra where not (P.buildlimit), joint-fit where neither

> **Where it fails.** wherever it was CONSTRUCTED rather than published -- such a channel is not a measurement against an independent standard, and the compendium marks the column.

### aufbau ordering — `n+l, then n`

**a permutation of subshells** · read from a table · from published literature · valid all elements · 19 objects rest on it

**What it is.** the order in which subshells fill as Z increases: lowest n+l first, and within one n+l value, lowest n first.

**Where it comes from.** Janet 1928 (Considerations sur la structure du noyau de l'atome, Beauvais 1929), who recognised it before Madelung 1936; shell lengths by the Klechkovski-Hakala formulas

> **Where it fails.** at about twenty known exceptions among the elements -- Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag, La, Ce, Gd, Pt, Au, Ac, Th, Pa, U, Np, Cm, Lr. The compendium reads the OBSERVED configuration, so the exceptions are data and not failures. AND the rule's ORIGIN is unresolved: Loewdin's challenge, Allen & Knight, Int. J. Quantum Chem. 90 (2003) 80-88.

### Janet block boundary — `Z = 21, 57, 89`

**exact integer** · read from a table · from published literature · valid all elements · 15 objects rest on it

**What it is.** the atomic number at which a new n+l block opens -- n+l = 5 at Sc, 7 at La, 8 at Ac -- which is where the corresponding orbital contracts into the core.

**Where it comes from.** the block structure is Janet 1928; the CONTRACTION is Goeppert-Mayer, Phys. Rev. 60 (1941) 184-187, and Griffin, Andrew & Cowan, Phys. Rev. 177 (1969) 62-71

> **Where it fails.** as a SHARP threshold: collapse is rapid, not instantaneous. Ca I at Z = 20 has nd = 0.908 against a threshold of 21, and Ba II at 56 has nf = 0.756 against 57.

### Hund's first rule — `max S for the core`

**a term selection** · read from a table · from published literature · valid all elements · 12 objects rest on it

**What it is.** of the terms a configuration allows, the one of highest total spin lies lowest in energy; it fixes which multiplicities a core can present.

**Where it comes from.** Hund, Z. Phys. 33 (1925) 345-371

> **Where it fails.** for a core in an excited term rather than its ground term. The index takes the ground term, so an excited-core series is outside it.

### core dipole polarisability — `alpha_d`

**per core, a0^3** · read from a table · from published literature · valid a region of the index · 10 objects rest on it

**What it is.** the induced dipole moment of the ionic core per unit applied field; the leading term in the potential a distant electron feels beyond the Coulomb tail.

**Where it comes from.** Born & Heisenberg, Z. Phys. 23 (1924) 388-410; systematic values Mayer & Mayer, Phys. Rev. 43 (1933) 605-611; modern e.g. Cs+ 15.696(16) a0^3, arXiv:2502.20961

> **Where it fails.** below l = 4, where penetration dominates and Seaton's formula does not apply. AND for nf treated as non-penetrating: arXiv:2502.20961 reports alpha_d and alpha_q that then disagree with the ng energies.

### actinide defects — `5.2, 4.75, 3.8, 2.0`

**theoretical** · read from a table · from published literature · valid a region of the index · 2 objects rest on it

**What it is.** the asymptotic ns, np, nd and nf quantum defects predicted for the actinides, Z = 89-103; the compendium's only high-Z anchors.

**Where it comes from.** arXiv:2508.06733 (2025), theoretical

> **Where it fails.** as MEASUREMENTS -- they are calculated. Four of the seven far anchors are these, and the equation's high-Z arm moves if they are revised (register 1202).

### Seaton polarisation constant — `3 alpha c^2 / K(l)`

**derived** · derived here · from published literature · valid a region of the index · 10 objects rest on it

**What it is.** the limiting quantum defect of a non-penetrating series, set by the core's polarisability and the centrifugal factor K(l) = l(l+1)(2l-1)(2l+1)(2l+3).

**Where it comes from.** Seaton, MNRAS 118 (1958) 504-518; Drake & Swainson, Phys. Rev. A 44 (1991) 5448

> **Where it fails.** at l < 4, and wherever the quadrupole term matters. The compendium measures the ratio delta_2/delta_0 against -l(l+1)/3 at 1.25 rather than 1.00.

### reduced-mass Rydberg — `R_M`

**R_inf/(1 + 1/(A m_p))** · derived here · from international standard · valid all elements · 9 objects rest on it

**What it is.** the Rydberg constant corrected for a nucleus of finite mass A, by replacing the electron mass with the electron-nucleus reduced mass.

**Where it comes from.** Bohr 1913: after Fowler objected that the Pickering series did not fit, Bohr replaced the electron mass with the reduced mass and obtained five-digit agreement, which identified the series as ionised helium. Bohr, Nature 95 (1915) 6-7 for his later comment.

> **Where it fails.** for an ion of unknown isotopic composition: A is the dominant isotope, and a mixed sample shifts R_M by roughly the isotope shift.

### bracket yardstick — `2 Z^2 R / nu^3`

**derived** · derived here · from published literature · valid all elements · 4 objects rest on it

**What it is.** the local spacing between adjacent Rydberg levels -- the derivative of the term formula. A perturbation larger than half of it reorders the levels.

**Where it comes from.** derived from Rydberg's term formula (1890)

> **Where it fails.** for a PERTURBED series, where a level of another channel crosses in. Fano, Phys. Rev. 124 (1961) 1866-1878; Lu & Fano, Phys. Rev. A 2 (1970) 81-86.

### channel equation, a — `0.3772`

**fitted** · fitted here · from this work · valid a region of the index · 8 objects rest on it

**What it is.** the overall amplitude of the penetrating branch: how much defect one core orbital of the same l produces at unit electron count and unit charge.

**Where it comes from.** fitted here by least squares on 277 in-region channels plus 7 far anchors; the FORM it scales is the penetration picture of Hartree, Proc. Camb. Phil. Soc. 24 (1928) 89-110

> **Where it fails.** outside Z <= 92, charge <= 10, l <= 4, single-parent core.

### channel equation, e0 — `0.8297`

**fitted** · fitted here · from this work · valid a region of the index · 8 objects rest on it

**What it is.** the intercept of the exponent on the core-orbital count p -- how sharply the defect grows with the number of same-l orbitals in the core, at small Ne.

**Where it comes from.** fitted here; the p-count itself is the Pauli occupancy (Pauli 1925)

> **Where it fails.** as above. Its value moved from 0.583 to 0.830 when the far anchors were added, so it is sensitive to the high-Z end.

### channel equation, e1 — `-0.0900`

**fitted** · fitted here · from this work · valid a region of the index · 8 objects rest on it

**What it is.** the log-Ne slope of that exponent: the rate at which additional core orbitals stop mattering as the atom grows.

**Where it comes from.** fitted here; that screening saturates with electron count is the Thomas-Fermi picture of Fermi, Z. Phys. 48 (1928) 73-79

> **Where it fails.** as above; it was -0.027 before the anchors, a factor of three.

### channel equation, k — `0.4942`

**fitted** · fitted here · from this work · valid a region of the index · 8 objects rest on it

**What it is.** the Thomas-Fermi exponent: how the defect scales with the number of electrons in the core, through the screening the statistical model predicts.

**Where it comes from.** fitted here; the scaling is Fermi, Z. Phys. 48 (1928) 73-79, who applied the statistical model to Rydberg corrections directly

> **Where it fails.** MEASURABLY: k rises with charge, from 0.84 at charge 1 to 1.52 at charge 4 (register 1214). A single value is a simplification and the register says so.

### channel equation, h — `0.5415`

**fitted** · fitted here · from this work · valid a region of the index · 8 objects rest on it

**What it is.** the amplitude of the collapse branch: how much defect a collapsed orbital produces where the core has no orbitals of its own l.

**Where it comes from.** fitted here; the collapse is Goeppert-Mayer 1941 and Griffin, Andrew & Cowan 1969

> **Where it fails.** below the Janet boundary, where the polarisation floor is absent.

### isoelectronic ladder, B — `per sequence`

**fitted** · fitted here · from this work · valid a region of the index · 3 objects rest on it

**What it is.** the single free coefficient of delta(c) = B ln(c+1)/c along a sequence of fixed electron count, with the constant term fixed at zero by the hydrogenic edge.

**Where it comes from.** fitted here per sequence on the 52 with three or more charge states; the isoelectronic method is Edlen, Handbuch der Physik XXVII (1964) 80-220

> **Where it fails.** as a CLOSED FORM: no expression of B in the coordinates beats the per-sequence fit by less than a factor of twenty, and PMC3671562 reports the same for ionisation energies.

### five-sigma admissibility — `r >= 5`

**a threshold** · fitted here · from this work · valid all elements · 3 objects rest on it

**What it is.** the bracket is applied only where the signal exceeds five times the measurement uncertainty, so that a bracket failure is a fact about the levels and not noise.

**Where it comes from.** the convention is particle physics's; its history and its critics are in Lyons, Discovering the significance of 5 sigma, arXiv:1310.1284 (2013)

> **Where it fails.** it is a CHOICE. At three sigma more cells enter and more brackets fail; the compendium states the threshold rather than tuning it.

### exchange coefficient — `s = -0.0782`

**fitted, WITHDRAWN** · fitted here · from this work · valid one species · 1 objects rest on it

**What it is.** the fractional difference between a triplet channel's defect and its singlet partner's, from the exchange interaction between the Rydberg electron and the core.

**Where it comes from.** fitted at register 987, WITHDRAWN at 1168; the physics is Heisenberg, Z. Phys. 38 (1926) 411-426, with Hund's first rule (1925)

> **Where it fails.** everywhere: the fitted sign is opposite to the measured one, and a uniform s gives 0 of 66 pairs or 66 of 66.

## The three failures that are measured rather than anticipated

*Most of the failure modes above are domain statements: the parameter is right inside its range and untested outside. Three are different — the compendium has MEASURED the failure.*

**Seaton's polarisation constant.** The ratio δ₂/δ₀ should be −ℓ(ℓ+1)/3 with the polarisability cancelling. On fourteen channels with δ₀ > 0.01 the observed ratio is **1.25 times** the predicted one, and the departure is a per-core constant reproducible within a species to two decimals — Si III g gives 1.77 four times, Si III h gives 1.12 twice.

**The Thomas–Fermi exponent k.** Fitted per charge state, it reads **0.84, 0.91, 1.03, 1.40** at s and **1.01, 1.13, 1.28, 1.52** at p, for charges 1 to 4, with trend R² between 0.87 and 0.98. **The equation carries a single k = 0.494.** *Register 1214.*

**The exchange coefficient.** The fitted sign is opposite to the measured one, and no uniform coefficient can work: exchange acts through an overlap that falls sharply with ℓ, so one constant gives 0 of 66 triplet-above-singlet pairs or 66 of 66. *Withdrawn at register 1168.*

**These three are why the compendium states failure modes at all.** *A parameter whose failure has been measured is more useful than one whose validity has been assumed, and the difference is not visible unless both are written down.*

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
