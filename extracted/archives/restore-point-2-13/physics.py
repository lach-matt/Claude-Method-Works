#!/usr/bin/env python3
"""physics.py -- generates The Physics Compendium.

Register 901. The book has four compendia and none of them states the INTERFACE
between a physical quantity and the index that holds it. That gap cost four faults
in one session:

    R 868  R_inf used for every species where the reduced-mass constant is correct
    R 879  Li III's limit written as 9 R_inf, a FORMULA where a measurement was needed
    R 766  atomic numbers passed where the CORE's charge is required
    R 782  the bracket column set equal to its own denominator

Each is a transition performed without its rule written down anywhere.

This compendium is NOT a list of mechanisms — those live in MECHANISMS.md and
mathreg.py, and a third copy would drift as register 778's list did. It states, for
each index:

    WHAT IT INDEXES     the physical objects the cells stand for
    THE QUANTITY        the physical number attached to each cell
    THE TRANSITION      the rule taking one to the other, written out
    CONSTANTS REQUIRED  named, with which value and why
    MUST BE MEASURED    what may NOT be computed from a formula, and what happens
                        when it is
    WHAT PHYSICS DOES   and, equally, what it does NOT do here

Generated, so it cannot drift from the source it cites.
"""
import datetime, re, importlib.util as iu

OUT = []
def W(s=""): OUT.append(s)

def reg():
    sp = iu.spec_from_file_location("_m", "mathreg.py"); m = iu.module_from_spec(sp)
    try: sp.loader.exec_module(m)
    except SystemExit: pass
    return m.REG
REG = reg()
NP = sum(1 for k in REG if k.startswith("P."))

W("# The Physics Compendium")
W()
W(f"Generated from `mathreg.py` and `SPECTRA-DATA.tsv` on "
  f"{datetime.date.today().isoformat()}. **{len(REG)} registered objects, "
  f"{NP} of them physical mechanisms.**")
W()
W("This compendium states the **interface** between a physical quantity and the index "
  "that holds it. It is not a list of mechanisms — those are in `MECHANISMS.md` and the "
  "Mathematical Compendium, and a third copy would drift as register 778's list did. "
  "It states, for each index, what the cells stand for, what number is attached to them, "
  "the rule taking one to the other, which constants that rule requires, **what must be "
  "measured rather than computed**, and what physics does and does not do.")
W()
W("Four faults in a single session were transitions performed without their rule written "
  "down: register 868 used R∞ for every species where the reduced-mass constant is "
  "correct; register 879 wrote Li III's ionisation limit as a formula where a measurement "
  "was required; register 766 passed atomic numbers where the core's charge is needed; "
  "register 782 set a verification column equal to its own denominator. **This document "
  "exists because those four share one cause.**")
W()
W("---")
W()

# ---------------------------------------------------------------- Λ
W("## Λ — the elemental index")
W()
W("**What it indexes.** Electron configurations of the ground states of the elements, on "
  "eight coordinates (n, ℓ, k, q, e, f, g, 2S). **976 cells.**")
W()
W("**The quantity.** None. A cell of Λ carries no physical number: it is an *arrangement*, "
  "not a measurement.")
W()
W("**The transition.** A configuration is read off the aufbau order and its subshells "
  "mapped to coordinates. `L.real` establishes that Λ's eight constraints hold on 247 "
  "real subshells across all 118 elements — **18,288 tests, no failures**.")
W()
W("**Constants required.** None.")
W()
W("**Must be measured.** Nothing. Λ is closed — |Λ| = |ℛ(Λ)| = 976, **E(Λ) = 0** — and the "
  "partition identity holds exactly: 6,912 = 976 + 0 + 5,936 (register 833).")
W()
W("**What physics does.** It supplies the aufbau ordering and the shell capacities, and "
  "nothing else. **What it does NOT do:** confer predictive power. §24 states that Λ "
  "*\"contains no physics that was not already in the quantum numbers; it is a recoding … a "
  "recoding adds nothing.\"* Register 834 measured the consequence: on the same closed "
  "index, the T-bracket passes 789 of 789 and the δ-bracket passes 546 of 789. **Closure "
  "coexists with a bracket that holds and one that fails, so it cannot be what makes "
  "either true.**")
W()
W("---")
W()

# ------------------------------------------------- the spectra index
rows = [l.rstrip().split("\t") for l in open("SPECTRA-DATA.tsv", encoding="utf-8")][1:]
nch = len(rows); ncell = sum(int(r[4]) for r in rows)
nsp = len({r[0].rstrip(" *") for r in rows})
W("## Λ_spectra — the index of Rydberg channels")
W()
W(f"**What it indexes.** Rydberg series: a fixed parent core, a fixed ℓ, n running. "
  f"**{nch} channels across {nsp} spectra, {ncell:,} interior cells.** The complete index "
  f"over the same alphabets is closed: |X| = |ℛ(X)| = 624, **E = 0** (register 853).")
W()
W("**The quantity.** The **quantum defect** δ — a continuous real number measuring how far "
  "the Rydberg orbital penetrates the ionic core. It is not an integer and has no "
  "factorization (register 896).")
W()
W("**The transition.** For a level at energy E below a limit I,")
W()
W("        n* = Z_c √( R_M / (I − E) )        δ = n − n*")
W()
W("**Constants required, and which value:**")
W()
W("  - **Z_c — the charge of the CORE, not the atom.** NIST states the formula as "
  "E_nl = −Z_c²/(n−δ)², *\"where Z_c is the charge of the core\"*. Be III and B III are "
  "third spectra and take Z_c = 3, not 4 and 5. Passing atomic numbers gave defects of "
  "−2 to −5 with spreads above 1.0 (registers 766, 883).")
W("  - **R_M — the reduced-mass Rydberg, R∞/(1 + mₑ/M), not R∞.** For helium "
  "109,722.386 against 109,737.316. Using R∞ understates every defect by "
  "n*(√(R∞/R_M) − 1) — 0.00240 for helium at n* = 35 — which drove He I's high-ℓ defects "
  "**negative**. Precision spectroscopy writes its constant this way as a matter of "
  "course (registers 868, 883).")
W("  - **The exception.** Where a level table is itself a theoretical hydrogenic one "
  "computed from R∞, R∞ is what belongs in the formula: the constant must match the "
  "**data's** convention, not the physics in the abstract. Applying a reduced mass to "
  "Li III's table drove its spreads from 0.0000 to 0.0125 (register 872).")
W()
W("**Must be measured, not computed.** **The ionisation limit.** Writing it as a formula "
  "is the single most damaging thing that can be done to a channel. Li III's limit was "
  "recorded as *\"Z²R = 9 × 109737.31568 (hydrogenic, Z=3)\"* — a bare Coulomb expression "
  "that omits the QED and relativistic terms. Fitting the limit from the series gives "
  "**987,662.29 ± 0.36, higher by 26.45 cm⁻¹**, and every Li III channel moves from "
  "−0.0038…−0.0082 to a uniform **+0.0003** (register 879). The same deficit appears at "
  "B V scaled by Z⁴: **678 cm⁻¹ above 25R∞** (register 895).")
W()
W("**How a wrong limit announces itself.** A defect that should be constant instead "
  "deviates, and **the power of n\\* names the cause**:")
W()
W("        n*³    a shift in the ionisation limit")
W("        n*⁷    a magnetic field       — needs tens of tesla")
W("        n*¹⁰   an electric field      — begins at n > 60")
W()
W("**Two of the three cannot fire on this compendium.** Its highest member anywhere is "
  "**n = 56** (Si I's nd (3/2,5/2)); eight channels exceed n = 40 and **none exceeds 60**. "
  "So every residual chased here was a limit, and none was a field — not by luck but "
  "because ASD's tables stop below where field effects begin (register 915).")
W()
W("**And the limit term's tolerance is published: a shift of even 0.2 cm⁻¹ \"causes totally "
  "different behavior of quantum defect versus n\".** Li III's was **26.45** — a hundred and "
  "thirty times that (register 914).")
W()
W("Li III's residual went as n³ and the limit was the fault. This is published and was "
  "derived independently here (registers 877, 885).")
W()
W("**Where the index STOPS, and why that is a decision.** Λ is finite because all 118 ground "
  "configurations are known within its caps. **The spectra index is not**: Rydberg series are "
  "unbounded in n and ℓ runs to n−1, so it is **infinite unless capped**, and every cap is a "
  "choice. Three defensible ones give:")
W()
W("        the measured alphabet          1,312 cells    E = 1,084")
W("        charge 1..Z−1, elements held   4,376 cells    E = 4,148")
W("        all 118 elements, l 0-7       55,224 cells    E = 54,996")
W()
W("**A factor of fifty between them, and all three close when complete.** Closure is a "
  "result about ℛ; the E that accompanies it is a result about the cap. At the physical "
  "cap the compendium holds **0.413%** — Λ holds 100% within its own (registers 959–962).")
W()
W("**What physics does.** It sets δ through core penetration, and the sixteen mechanisms "
  "in `MECHANISMS.md` describe how. **What it does NOT do:** make δ an integer, or give "
  "the index predictive power over cells it does not contain. Of 624 cells, 160 are "
  "measured and **193 are fully isolated** — no measured channel adjacent in ℓ or in an "
  "isoelectronic sequence, so no bound reaches them (register 890).")
W()
W("---")
W()

# ------------------------------------------- point of observability
W("## The point of observability — what the equation actually delivers")
W()
W("**The quantum defect is a phase shift.** Outside the ionic core, where the potential is "
  "purely Coulombic, the radial Schrödinger solution is a superposition of the regular and "
  "irregular Coulomb functions:")
W()
W("        ψ  =  cos(πδ)·f(E,ℓ,r)  −  sin(πδ)·g(E,ℓ,r)")
W()
W("and **πδ is the phase shift with respect to the pure hydrogenic solution**, due to all "
  "short-range non-Coulombic interactions at r < r_c. Seaton's theorem continues it across "
  "threshold, δ_ℓ(0) = πμ_ℓ(0), so the same number describes bound levels and scattering.")
W()
W("**The consequence, and it is sharp.** The equation depends on δ only through cos πδ and "
  "sin πδ. **What it determines is δ modulo 1. The integer part is not in the equation** — it "
  "is supplied afterwards by counting nodes inside the core, and it is a labelling, not a "
  "measurement.")
W()
W("**What this costs the compendium.** Register 891 tested the rule "
  "*floor(δ) = (core orbitals of that ℓ) − 1* and found it holding for 318 of 407 channels — "
  "78%, with Al I's ns at 1.767 where the rule requires 2.x. **It was testing a convention.** "
  "And testing P.lcollapse both ways:")
W()
W("        on the full defect        150 correct,  8 inverted   94.9%")
W("        on δ mod 1 (observable)   127 correct, 31 inverted   80.4%")
W()
W("**The ordering survives on the assigned value and degrades on the observable one.** So "
  "P.lcollapse is a statement about node-counting as much as about penetration. Only **96 of "
  "431** channels have |δ| > 1 at all — the rest have no integer part to assign, and for them "
  "the distinction does not arise (registers 910–913).")
W()
W("**The general rule this gives.** *A mechanism that holds on the assigned value and fails on "
  "the observable one is a statement about the index, not about the atom.* That is §24's "
  "distinction — a recoding adds nothing — reappearing at the level of a single number rather "
  "than a whole lattice.")
W()
W("---")
W()


# ------------------------------------------- kinematic against stateful
W("")
W("---")
W("")
W("## Kinematic and stateful — an interface the register found in its own objects")
W("")
W("**A geometric hypothesis cannot do a state's work, and the register's one OPEN object is "
  "what happens when it is asked to.**")
W("")
W("`M.C1` assumes Θ = 0 — the non-expanding condition, geometry and nothing else — and it "
  "succeeds: the presymplectic form is block diagonal in y and the commutator is "
  "(1/4√q) sgn(u−u′) δ^(d−2)(y−y′). **`M.C2` adds exactly one hypothesis, *ω Hadamard*, and that "
  "is a condition on a STATE.**")
W("")
W("**Every obstruction encountered sits on the stateful side:**")
W("")
W("  - a geometric modular flow needs a Killing vector — the flow is stateful and the geometry "
  "must match it")
W("  - half-sided modular inclusion ⟺ a positive generator, and positivity is a property of a state")
W("  - Θ = 0 is invariant under ℓ → a(y)ℓ, so **the geometry does not fix the state**")
W("  - smoothness supplies a *local* Hartle–Hawking state, and local states do not glue")
W("  - Hadamard is microlocal and therefore too weak to select one")
W("  - and uniqueness, where it is available at all, needs invariance under a Killing flow")
W("")
W("**And the split is NOT geometry against state, which was the first reading and was wrong.** "
  "The standard definition of a non-expanding horizon has three conditions and the third is "
  "*\"Einstein field equations hold on Δ, and the stress-energy tensor T_ab is such that "
  "−T^a_b ℓ^b is future causal\"* — **an energy condition, hence a condition on the state.** "
  "Through the kk-component of the Einstein equation it forces the null-null flux T_ab ℓ^aℓ^b "
  "and the shear σ_ab to VANISH, giving £_ℓ q_ab = 0. *So `M.C1`'s hypothesis is not an "
  "assumption but a consequence of the horizon's own definition, which is why it succeeds.*")
W("")
W("**What the condition does not do is reach the right order.** It fixes the BACKGROUND — "
  "vanishing shear, vanishing null flux — while the linearised Raychaudhuri ∂_u δΘ = −8πG_N T_uu "
  "carries T_uu ≠ 0 on the perturbations, which is what the theory is about. **Half-sidedness is "
  "a spectral statement about those perturbations, and future-causality of −T^a_b ℓ^b is not one** "
  "(registers 1038–1042).")
W("")
W("**The dimensional ledger states the split arithmetically**: d − 1 = 1 + (d − 2), one HSMI per "
  "generator supplying the affine line and the transverse direct integral coming from the "
  "kinematic side. *The stateful object supplies one dimension; the kinematic one supplies d − 2.*")
W("")
W("**And it explains a result that otherwise looks like luck.** Computing the free half on one "
  "generator gives a positive translation generator immediately — negative to positive spectral "
  "weight 5 × 10⁻⁵ — **because a state was supplied by hand, the vacuum on a null line.** *The "
  "moment a state is given the inclusion follows; nothing on a non-expanding horizon gives one.* "
  "Registers 1033–1037.")
W("")

# ------------------------------------ placing against valuing
W("")
W("---")
W("")
W("## Placing a cell and valuing it are different operations")
W("")
W("**ℛ places. Mechanisms value.** The distinction is invisible in Λ, where a cell is an "
  "arrangement and carries no number, so recovering the cell recovers everything. It is "
  "the whole difficulty in Λ_spectra, where the cell carries a quantum defect and that is "
  "its entire content.")
W("")
W("        placed by ℛ          1,762 of 1,775 cells      99.3%")
W("        valued               525                        32%")
W("")
W("**A relation is usable as a STEP — carrying a value from one cell to another — only "
  "where the physics has collapsed to ONE PARAMETER.** Measured on pairs where both cells "
  "are known, as a geometric scatter:")
W("")
W("        Nₑ at fixed charge ÷ Thomas-Fermi, s+p, Nₑ ≥ 9     1.07")
W("        elem, s+p, Nₑ ≥ 9, raw                            1.10")
W("        ℓ at ℓ ≥ 4, Seaton's ratio, filtered              1.12")
W("        charge at fixed Nₑ, s                             1.23")
W("        charge at fixed Nₑ, p                             1.38")
W("        ℓ at p, d, f                                      3.31")
W("        elem, all ℓ and Nₑ                                3.85")
W("        Nₑ at fixed charge, raw                           4.12")
W("")
W("**Above ℓ = 4 the electron never enters the core and only the polarisability matters — "
  "one number, and Seaton's formula follows. At ℓ ≤ 1 with Nₑ ≥ 9 penetration is "
  "statistical and Thomas-Fermi governs. At ℓ = 2, 3 or Nₑ < 9 neither dominates**, and "
  "four separate corrections — Seaton's ratio, core-orbital counts, the defect's own "
  "magnitude, a free Thomas-Fermi exponent — each left the scatter where it was.")
W("")
W("**The transition zone is not a missing systematic. It is the absence of one**, and those "
  "cells require measurement rather than propagation (registers 1102–1118).")
W("")
# ------------------------------------------------ relativity
W("## Where relativity enters, and where it does not")
W()
W("**One place: the ionisation limit of a hydrogenic ion.** A Coulomb expression Z²R gives "
  "the limit only to order (Zα)². The Sommerfeld correction — special relativity applied to "
  "the atom in 1916, and shown by Gordon and Darwin to follow exactly from the Dirac "
  "equation — adds")
W()
W("        ΔE = Z⁴ α² R_M / 4        for the 1s state")
W()
W("**Measured against the reduced-mass baseline Z²R_M, three hydrogenic species give:**")
W()
W("        Li III   deficit 103.94   Dirac 118.32   ratio 0.878")
W("        Be IV    deficit 329.80   Dirac 373.97   ratio 0.882")
W("        B V      deficit 816.68   Dirac 913.03   ratio 0.894")
W()
W("**0.8849 ± 0.0069 across Z = 3, 4, 5** (register 906). The missing 11.5% is the **1s Lamb "
  "shift**, which raises the level and reduces the binding; it goes as α³Z⁴ against Dirac's "
  "α²Z⁴, so their ratio is order α times a slowly varying function — which is why three "
  "elements agree to under one per cent (register 908).")
W()
W("**The practical consequence.** Register 879's Li III fault was a Coulomb expression used "
  "where a relativistic one was required: the limit was written as 9R∞ and was low by 26.45 "
  "cm⁻¹, showing as a spurious defect of −0.0048 growing as n³ across every ℓ. **A hydrogenic "
  "limit computed rather than measured will always be low by this term.**")
W()
W("**Where relativity does NOT enter.** General relativity has no measurable term at these "
  "energies, and the compendium makes no use of it. The relativistic content here is entirely "
  "the special-relativistic kinetic correction, spin-orbit coupling and the Darwin term — the "
  "three that make up fine structure — plus the QED Lamb shift, which is not relativity at all "
  "(register 909).")
W()
W("---")
W()

# ----------------------------------------------------- the bracket
W("## The bracket — the transition from a channel to an interval")
W()
W("**What it indexes.** An interior cell: a series member with a measured neighbour on "
  "each side.")
W()
W("**The quantity.** Not a value but an **interval**, and the book is explicit that this "
  "is the point: §22 says it *\"fits nothing, assumes no functional form, and returns an "
  "interval rather than a value. It is a deduction, not a prediction.\"*")
W()
W("**The transition — and there are TWO, which the book does not distinguish.**")
W()
W("  - **§22.1, on binding energy.** T = I − E is monotone in n, so T(n) lies between "
  "T(n−1) and T(n+1). **Passes 789 of 789.** A Rydberg series rises toward its limit by "
  "construction, so this form **cannot fail** (registers 797, 800, 830).")
W("  - **§25.6.1, on the defect.** δ(n) lies between δ(n−1) and δ(n+1), resting on "
  "*\"within a channel, δ falls monotonically with n\"*. **Passes 546 of 789.**")
W()
W("**The trade-off, stated.** §22.1's bracket is a genuine deduction and carries no "
  "information. §25.6.1's carries information and is not a deduction. **Chapter 22's "
  "modesty is exactly what buys the 100%, and the price is that the 100% was never "
  "evidence** (register 803).")
W()
W("**And the monotonicity claim is the wrong form.** The extended Ritz expansion is")
W()
W("        δ(n) = δ₀ + δ₂/(n−δ₀)² + δ₄/(n−δ₀)⁴ + …")
W()
W("and **caesium's nF series is measured with δ₂ = −0.2014(16) — negative — its defects "
  "RISING** with n. So the law is that **δ approaches δ₀ monotonically**; the direction is "
  "sign(δ₂), a property of the channel, and falling is only the common case (register "
  "858).")
W()
W("**What physics does.** It guarantees the monotonicity of T. **What it does NOT do:** "
  "guarantee the monotonicity of δ, which holds in 113 of 130 resolved steps — 87%, "
  "interval 80–92% — and only where a step exceeds its own uncertainty. With error "
  "estimated from quoted decimals instead, the same test gives **55%**, and the intervals "
  "do not overlap (register 822).")
W()
W("---")
W()

# --------------------------------------------------- what is owed
W("## What the interface still does not state")
W()
W("**Uncertainties.** Five of 49 species files carry a quoted uncertainty column. The "
  "monotonicity law is testable only where a step can be distinguished from its own "
  "error, and **44 of 49 species do not supply what that needs** (register 807).")
W()
W("**The bracket's own inputs.** `channels.py` writes `bracket = \"untested\"` for every "
  "channel it builds, because running the bracketing method needs measured neighbours and "
  "a tolerance and the script supplies neither. **285 of 431 channels are unverified on "
  "the compendium's central claim**, and the column says so rather than asserting a "
  "verification that never ran (register 782).")
W()
W("**Appendix B's inputs.** 133 channels were lifted with their values and without their "
  "levels. `spectra_raw/` holds no He I file, so when register 868 corrected the Rydberg "
  "constant those channels **could not be recomputed**. *A result kept without its inputs "
  "cannot be corrected when its method is* (register 871).")
W()


# ============================================================ Lambda_phys
# Register 1238-1240. The compendium stated the INTERFACE between a quantity and the
# index that holds it, and never held the parameters themselves. This section does.
import importlib.util as _iu
_sp = _iu.spec_from_file_location("_pp", "params.py"); _pm = _iu.module_from_spec(_sp)
_sp.loader.exec_module(_pm)
_P = _pm.P
_KIND = ["exact by definition", "measured constant", "read from a table",
         "derived here", "fitted here"]
_SRC  = ["mathematics", "international standard", "published literature", "this work"]
_DOM  = ["universal", "all elements", "a region of the index", "one species"]

W("---")
W()
W("# Λ_phys — THE INDEX OF PHYSICAL PARAMETERS")
W()
W("**Every number the work takes from physics, with what it is, where it comes from, "
  "and where it stops being right.** *A parameter with no stated failure mode is a "
  "parameter being used outside a domain nobody has checked.*")
W()
W(f"**{len(_P)} parameters.** Coordinates: **kind** (exact → fitted), **source** "
  "(mathematics → this work), **domain** (universal → one species), and how many "
  "registered objects rest on it.")
W()

W("## What the index shows about the work's dependence")
W()
W("| kind | universal | all elements | a region | one species |")
W("|---|---|---|---|---|")
for _k in range(5):
    _row = [sum(1 for p in _P if p[3] == _k and p[5] == _d) for _d in range(4)]
    if not sum(_row): continue
    W(f"| **{_KIND[_k]}** | {_row[0]} | {_row[1]} | {_row[2]} | {_row[3]} |")
W()
_own = [p for p in _P if p[4] == 3]
W(f"**{len(_own)} of the {len(_P)} parameters are this work's own.** "
  f"*Of those, **{sum(1 for p in _own if p[5] == 0)} are universal**, "
  f"{sum(1 for p in _own if p[5] == 1)} hold across all elements, and "
  f"**{sum(1 for p in _own if p[5] >= 2)} hold only in a region or for one species.** "
  "No number this work fitted claims wide validity.*")
W()
W("**And the dependence concentrates on TABLES, not on constants.** The three "
  "parameters carrying the most objects are all read rather than fitted:")
W()
W("| parameter | objects resting on it | kind |")
W("|---|---|---|")
for p in sorted(_P, key=lambda x: -x[6])[:6]:
    W(f"| {p[0]} | **{p[6]}** | {_KIND[p[3]]} |")
W()

W("## The parameters")
W()
for p in sorted(_P, key=lambda x: (x[3], -x[6])):
    W(f"### {p[0]} — `{p[1]}`")
    W()
    W(f"**{p[2]}** · {_KIND[p[3]]} · from {_SRC[p[4]]} · valid {_DOM[p[5]]} · "
      f"{p[6]} objects rest on it")
    W()
    W(f"**What it is.** {p[7]}")
    W()
    W(f"**Where it comes from.** {p[8]}")
    W()
    W(f"> **Where it fails.** {p[9]}")
    W()

W("## The three failures that are measured rather than anticipated")
W()
W("*Most of the failure modes above are domain statements: the parameter is right "
  "inside its range and untested outside. Three are different — the compendium has "
  "MEASURED the failure.*")
W()
W("**Seaton's polarisation constant.** The ratio δ₂/δ₀ should be −ℓ(ℓ+1)/3 with the "
  "polarisability cancelling. On fourteen channels with δ₀ > 0.01 the observed ratio "
  "is **1.25 times** the predicted one, and the departure is a per-core constant "
  "reproducible within a species to two decimals — Si III g gives 1.77 four times, "
  "Si III h gives 1.12 twice.")
W()
W("**The Thomas–Fermi exponent k.** Fitted per charge state, it reads **0.84, 0.91, "
  "1.03, 1.40** at s and **1.01, 1.13, 1.28, 1.52** at p, for charges 1 to 4, with "
  "trend R² between 0.87 and 0.98. **The equation carries a single k = 0.494.** "
  "*Register 1214.*")
W()
W("**The exchange coefficient.** The fitted sign is opposite to the measured one, and "
  "no uniform coefficient can work: exchange acts through an overlap that falls "
  "sharply with ℓ, so one constant gives 0 of 66 triplet-above-singlet pairs or 66 of "
  "66. *Withdrawn at register 1168.*")
W()
W("**These three are why the compendium states failure modes at all.** *A parameter "
  "whose failure has been measured is more useful than one whose validity has been "
  "assumed, and the difference is not visible unless both are written down.*")
W()


# --- hand-authored tail, appended rather than generated (registers 1373, 1386, 1388) ---
# The generator does not write this region. It is declared here so that
# roundtrip.py's DECLARE question has an answer, and so a rebuild cannot
# silently discard it. If the tail is missing the generator REFUSES:
# a generator that cannot produce its whole output must not produce part of it.
import os as _os, sys as _sys
def _tail(_name):
    _p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), _name)
    if not _os.path.exists(_p):
        _sys.stderr.write(f"REFUSING: {_name} is absent; the output would be incomplete.\n")
        _sys.exit(2)
    return open(_p, encoding="utf-8").read()

_t = _tail("PHYSICS-TAIL.md")   # refuses before the file is opened for writing
open("PHYSICS.md", "w", encoding="utf-8").write("\n".join(OUT) + "\n" + _t)
print(f"  PHYSICS.md written — {len(OUT)} lines, {sum(len(x.split()) for x in OUT)} words")
