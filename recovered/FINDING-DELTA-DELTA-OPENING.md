# FINDING — Δδ, THE ANALYTIC OPENING. ITEM 3.
# SESSION 67. Standing 6 run first: the analytic route named in
# `FINDING-ALPHA-THE-WHY.md` §7 has NEVER been attempted in this chain. No WKB, no
# phase integral, no turning-point analysis exists in any pack. §7 names it and stops.
# THIS IS ANALYTIC WORK. It carries no prediction and no score, because it computes
# nothing — it derives. Standing 7 does not apply; what applies is that every step must
# be checkable by hand and must reduce to a known limit.
# NOTHING HERE IS FITTED. No number is entered. c is not used.

## WHAT MUST BE DERIVED, STATED EXACTLY
α = Δδ = δ_ℓ − δ_{ℓ+1} is derived (§4a). **Δδ ≈ 1 at neutrality is not.** Madelung is
the assertion α = 1, and §2 established that α = 1 is the critical value of the
tie-break clause and nothing else. So the Challenge reduces to: **what fixes the
quantum-defect decrement, and why does it sit at 1 for neutral atoms.**

## STEP 1 · THE DEFECT IS A PHASE, AND THE PHASE IS AN INTEGRAL
For a radial channel in a field that is −Z_eff(r)/r with Z_eff(0)=Z and Z_eff(∞)=1,
the bound spectrum is E = −1/2(n−δ_ℓ)². The defect is the extra phase the core puts
into the wavefunction relative to a pure Coulomb tail:

    δ_ℓ = (1/π) [ Φ_ℓ(field) − Φ_ℓ(Coulomb) ]

    Φ_ℓ = ∫ dr sqrt( 2E + 2Z_eff(r)/r − L²/r² ),      L = ℓ + ½   (Langer)

L = ℓ+½ rather than sqrt(ℓ(ℓ+1)) is the Langer correction, and it is REQUIRED, not
chosen: it is the condition that the radial WKB form be exact for the Coulomb problem,
which is the limit this derivation must reproduce. **That is the ℓ(ℓ+1)/2r² term of the
Schrödinger equation entering, and it is the only place ℓ enters at all.**

## STEP 2 · THE CORE INTEGRAL, DONE IN CLOSED FORM
At the valence threshold E → 0⁻, inside a region where Z_eff is constant at some value
q, the integral is elementary. With u = sqrt(2qr − L²):

    ∫ (1/r) sqrt(2qr − L²) dr  =  2u − 2L·arctan(u/L)

from the inner turning point r_min = L²/2q (where u = 0) out to R (where U = sqrt(2qR − L²)):

    Φ(q, L, R) = 2U − 2L·arctan(U/L)

**And for R ≫ L²/2q this is**

    Φ  ≈  2·sqrt(2qR)  −  πL  +  2L²/sqrt(2qR)  +  O(R^{-3/2})

## STEP 3 · THE FIRST RESULT, AND IT IS A NULL — THE LEADING ℓ-TERM CANCELS
Take the crudest model that has a core at all: Z_eff = Z for r < a, Z_eff = 1 for r > a.
The defect is the field's phase minus the Coulomb phase over the same range. The −πL
term appears in BOTH with the same coefficient, because it comes from arctan(U/L) → π/2,
which is the same limit in both. **It cancels identically.**

    δ_ℓ  =  (2/π)·[ sqrt(2Za) − sqrt(2a) ]  +  O(L²)   —   NO TERM LINEAR IN L
    Δδ   =  δ_ℓ − δ_{ℓ+1}  =  0  at leading order,  for every ℓ, at every Z.

**THIS IS THE CENTRAL NULL AND IT IS THE POINT.** A sharp-edged screened core produces
a defect that does not depend on ℓ, hence α = 0 — the HYDROGEN value. The model
reproduces the one limit the project has measured exactly (α = 0 for hydrogen, E(2s) =
E(2p) to 2 µHa, s63 Rung 5) and produces nothing else. **Madelung is invisible at this
order.** Whatever sets Δδ ≈ 1 is not in the leading phase.

## STEP 4 · WHERE THE ℓ-DEPENDENCE MUST THEREFORE LIVE
Two candidates, and they are distinguishable:

  (a) **THE SUBLEADING TERM.** +2L²/sqrt(2qR) survives with different q inside and out,
      giving δ_ℓ a piece going as L² = (ℓ+½)². Then
      Δδ ∝ (ℓ+½)² − (ℓ+3/2)² = −(2ℓ+2), **linear in ℓ with slope −2**. It has the right
      SHAPE — an ℓ-dependence that grows — but the wrong sign, and it is a correction
      term, small by construction.

  (b) **THE TURNING POINT LEAVES THE CORE.** r_min = L²/2q. For the integral of Step 2
      to see the core at all, r_min must lie inside it: **L² < 2Za.** Once L² > 2Za the
      channel never enters the region where Z_eff ≠ 1, the two phases are identical,
      and **δ_ℓ = 0 exactly.** This is not an approximation — it is a statement about
      the domain of integration.

**(b) is not a correction. It is a switch**, and it is the same statement the compendium
already carries independently: *δ = 0 exactly for a non-penetrating, uncollapsed
channel.* The condition L² = 2Za defines a critical ℓ at each Z, and channels straddle
it.

## STEP 5 · WHAT THIS PREDICTS ABOUT Δδ WITHOUT ANY NUMBER BEING ENTERED
If (b) governs, then across an ℓ-pair Δδ = δ_ℓ − δ_{ℓ+1} takes its LARGEST values where
one member penetrates and the other does not — δ_ℓ finite, δ_{ℓ+1} = 0 — and its
smallest where both penetrate fully and the difference is only the O(L²) correction of
(a). **Δδ is therefore not a smooth function of ℓ. It is governed by how many members of
the pair sit on each side of L² = 2Za.**

That is a testable ordering claim and it is NOT tested here. What is recorded is that it
is consistent with the direction of the three sealed medians — s→p 0.53, p→d 1.07,
d→f 1.50 — since higher ℓ pairs are the ones that straddle. **Consistent with, not
established by. No score is claimed and no instrument was run.**

## STEP 6 · AND IT PUTS THE ORTHOGONALITY-COUNTING ARGUMENT BACK IN PLAY, WITH A CAVEAT
§4(b) withdrew the counting argument (δ_ℓ counts core shells of the same ℓ; hence
Δδ = 1) as TESTED AND FALSIFIED: dN = 1 gave median α 1.092, dN = 2 gave 1.077, so dN
did not discriminate. **That test was run on the 42-measurement sample, which F67.4
shows is a 10% survivor set whose survival rate falls monotonically with ℓ — the same
axis dN varies along.** dN=2 drew 34 of its 42 measurements from that filtered pool.

**This is NOT a claim that the counting argument is right.** It is the observation that
its falsification and F67.4's filter share a sample, and that §4(b) does not currently
state this. The two are independent in principle: WKB says the core phase is an
integral, and node-counting says it is an integer count of core shells — **and Step 2
shows these are the same statement**, since each core node contributes exactly π to Φ
and therefore exactly 1 to δ. **The counting argument is the integer limit of the phase
integral, not a rival to it.** That is a derivation-level connection and it is new.

## WHAT IS OPEN, AND IT IS THE WHOLE OF IT
The switch at L² = 2Za gives δ = 0 or δ ≠ 0. It does not yet give **1**. What is needed
is the value of Φ for a penetrating channel in a REAL Z_eff(r) — not a sharp edge — and
that is where the project's own field is the right object and no model is required:
Z_eff(r) is available from the sealed self-consistent field at every Z.

**THE NEXT STEP IS NAMED PRECISELY:** evaluate Φ_ℓ numerically on the sealed field's own
Z_eff(r) at one atom, for two adjacent ℓ, and compare (1/π)ΔΦ against the α this chain
already measures at that atom. **If they agree, the defect decrement is derived from the
radial equation and Löwdin's question has an answer. If they disagree, the phase
integral is not what sets it and this route closes cleanly.** Either is a result. It is
one atom and one integral, and it requires a filed prediction before it runs.
