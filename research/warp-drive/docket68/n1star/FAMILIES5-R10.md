# FAMILIES5-R10 -- round 10: the round-8 confirming reader's findings, seated

The confirming reader of FAMILIES5-R8.md and of round 9's `checks/mbslice5.py` reproduced every program and found the
certificates sound. Its findings were one false sentence in the proposed paper block (Major 1), six minors and seven
nits, all about wording, labels and controls. Each is seated below: what changed, which program shows it, and the
result. Where a finding offered "compute it or relabel it", it is computed; the one place where computing was not
possible is said, with the reason. The corrected paper block is R10.1; it supersedes R8.8.

Earlier notes keep their text. Bracketed [R10] notes mark the affected lines in FAMILIES5-R8.md, FAMILIES5-MB.md and
FAMILIES5-R6.md. Nothing in the paper or in N1STAR-PROOF.md is edited.

## R10.0 The findings and what was done

- **Major 1 (the false sentence).** The block said data exist "on every vacuum band of the slice that meets the
  black-hole region". Bands with √μ3 < R < R_EH meet the black-hole region where f > 0, and there Theorem P gives E > 0.
  - The block now says "every vacuum band of the slice that meets {f < 0}" and "Where f < 0, inside the apparent
    horizon R² = μ", for the existence result.
  - It says "Where f > 0, E is positive on every invariant perturbation that is not a gauge one", which is Theorem P's
    class, and "So on bands in {f > 0}" for the non-existence result.
  - The matter sentence's "outside the horizon" and "inside it" became "where f > 0" and "where f < 0". This is Theorem
    Q′'s own condition: ξ future causal, or spacelike.
  - FAMILIES5-MB.md carries a note at its status paragraph that reads every "black-hole region" as {f < 0} and every
    "outside the horizon" as {f > 0}, with pointers at verdict items 1 and 2.
  - The event horizon's location is not computed in the record, and nothing uses it, so it is dropped rather than
    computed. FAMILIES5-R8.md R8.7 and R8.8 carry notes.
- **minor 1 (spot checks behind "computed exactly").** Computed.
  - `checks/mbslice5.py` S4 does mbsign5 E4 (a) and (c) on the static slice for every (R, θ, μ). It uses
    μ = R²(1 − ν²), so √f = ν, and θ = 2 arctan t. Every quantity is a polynomial over powers of the atoms R, t, 1 − t,
    1 + t, 1 + t² and ν, and only products of atoms are inverted.
    - In (a), the (S, S′) structure holds; every coefficient has zero t-derivative; and the radial coefficients E5-E9
      use are these, exactly.
    - In (c), all four mode-free identities hold. Control: the lapse direction without −ψ Ric fails.
  - S1 and S2 now cover l = 2, 4, 6 and 8 on every slice. The θ-integrated density over |T|² at l = 6 and 8 is,
    pointwise, the affine interpolant in k_T² of l = 2 and 4.
  - k_T² is not carried as a free symbol: the θ-integral is taken harmonic by harmonic (a Gegenbauer polynomial of
    fixed degree). Carrying k_T² would need the angular reduction by parts done symbolically for a harmonic of
    unspecified degree, which this route cannot represent. So "every l" stays the minor-8 deduction, labelled deduced,
    now checked at two more l.
  - MB §6's status table is repointed: Theorem T and Lemma X1 to mbslice5 S1-S2; Lemma G and the modes to S4; Theorem
    P to S1 and S4.
- **minor 2 (qsign5 Q1 at three points).** Computed. mbslice5 S5 runs Q1 for every background and every (R, θ).
  - G = g² and κ0, Y0, ν are free functions, and E = e^(Ia) is a free symbol whose derivatives follow
    Ia′ = (3c − 1)/R.
  - The seed solves the linearised H, M_R and M_θ identically, and the Euler operator of (Q-density − decomposition)
    in ψ and s1 is the zero rational function.
  - Control: 4νE² → 3νE² fails.
- **minor 3 (nledger5).**
  - Recount: stage m has mixed harmonics with up to m + 2 families (R6 §4.1 (d)). So a coefficient's source is any set
    of at most M + 2 families, for stages 0..M.
  - nledger5 L2 counts the term list for sources of at most 2, 3 and 4 families. The degrees are 4, 5 and 6, exact by
    interpolation and checked on further N. So the count has degree M + 4.
  - "Same types for every N" is computed for N = 2..8, and follows for every N because the generator never reads a
    family label into a row's numbers.
  - L4 is now labelled a definition check: it holds by λ0's definition, so it has no control.
- **minor 4.** The block cites `checks/truebg5.py` beside `checks/intcert5.py` for the band's extent. T3 is what shows
  nothing else fails below R_*.
- **minor 5 (controls on the pass conditions).**
  - truebg5 T2: the tube shrunk to d/10 does not contain the background (rejected).
  - mbsign5 E9: the input is mutated, h = 2k with the lapse dropped; it gives neither sign of the target (rejected).
  - intcert5 C1: the input is mutated, mass μ0 → −μ0; 235 cells fail (rejected).
- **minor 6.** R6's [R8] note now says M_b is settled both ways.
- **Nits.**
  - The v̂ = 0.5 values now come from truebg5.out at n = 160: ψ_III(0.5) ∈ [−0.20610997, −0.20607584], the n = 160
    spline −0.20610803 (inside), and μ0 = 0.82211118 (n = 160) inside μ3's enclosure.
  - "A few parts in 10³" now reads "up to 3 %".
  - "About 5×" is withdrawn: the bounds are certified upper bounds, not measured errors. truebg5 now prints that the
    certificate uses only the bounds.
  - v̂ = 0 is R = 0.680.
  - T2's sup bounds are now upper ends of intervals, with no float sums.
  - mbsign5's E2 and E3 prints now say "at three slice points" and point to mbslice5.
  - MB verdict item 2 carries section 5's qualifier for "to every order".
- **mbslice5 (c).** Lemma X1 is now computed at l = 2, 4, 6 and 8 (S2), and the wording says so. FAMILIES5-MB.md's
  section 2 note is replaced accordingly.

**Programs changed and rerun in full**, each `.out` regenerated, all PASS:

| Program | Checks | Change | Runtime |
|---|---|---|---|
| `checks/mbslice5.py` | S1-S5 | S4 and S5 new; S1 and S2 at l ≤ 8 | 303 s |
| `checks/nledger5.py` | L1-L4 | L2 recount; L4 relabelled | about a minute |
| `checks/truebg5.py` | T1-T4 | T2's interval bounds, d/10 control, v̂ = 0.5 print | about half an hour |
| `checks/intcert5.py` | C1-C3 | C1's input-mutation control | about a quarter of an hour |
| `checks/mbsign5.py` default | E1-E9 | E2/E3 prints; E9's input-mutation control | 299 s |
| `checks/mbsign5.py` `--full` | E4-E9 | as default | 244 s |

## R10.1 The section 9 block (supersedes R8.8)

The old text is the paper's current bullet, located by content. It begins "- **More families.** Angular separation and
the passage to Vlasov matter are not attempted." and ends "No statement about several families is proved." It occurs
exactly once in `paper/RESPONSE-HL-5D.md` (section 9, "What is not proved") and is quoted verbatim in R7.6.

New:

```
- **More families.** Two crossing radial null dusts, one ingoing and one outgoing, are carried through the record's
  argument: the two-dust background on the whole domain, the approximant to every order, the uniform estimate and the
  data (deduced, the identities computed; supplement `docket68/n1star/FAMILIES5-FULL.md` Part I). In the T² class each
  family's null second fundamental form is diag(θ_h, κ1, κ2), the torus terms first order, and at an axis the planar
  shear is recovered elliptically from the expansion, so the class Einstein–null-dust system is Cauchy-stable on compact
  domains of the record's type, without smallness, for caustic-free dusts whose lateral boundaries are adapted (one
  family) where they meet an axis (deduced; `docket68/n1star/FAMILIES5-AXIS.md`). A massless Vlasov limit in the class
  is restricted (computed); a smooth restricted field never reaches an axis off the axial directions, its density
  growing like 1/ρ2 there (computed, `docket68/n1star/checks/vlasovhf5.py` H7), and at an axis point at most one ingoing
  and one outgoing family are separated (computed, `docket68/n1star/checks/axisphase5.py`). Every smooth class
  Einstein–restricted massless Vlasov solution whose field is a family of dusts labelled by initial direction,
  caustic-free, off the axes and at an angle from the radial dusts where it meets them, the radial dusts having adapted
  lateral boundaries at the axes, on a domain of the record's type whose initial spheres have positive mean curvature
  and a hyperbolic momentum system, is a weak limit of class vacuum metrics along odd N (deduced: N-dust approximants
  uniform in N; torus-polarised waves at frequencies 1, Λ, …, Λ^(N−1), which leave no combination of phases resonant up
  to the order the scheme uses; data with overlapping families, whose only divisors are spacetime symbols; the N-family
  energy estimate, its power counting computed term by term (`docket68/n1star/checks/nledger5.py`); a diagonal choice of
  λ_N, as Huneau and Luk do; `docket68/n1star/FAMILIES5-VLASOV.md`, `docket68/n1star/FAMILIES5-R6.md`,
  `docket68/n1star/FAMILIES5-R8.md`, the identities, divisors and data step computed). These hypotheses are open for
  perturbations whose supports stay in a fixed compact set and whose radial dusts keep adapted boundaries (deduced), and
  an explicit test family on Tangherlini meets them (computed, `docket68/n1star/checks/vlasovex5.py`). Data localised in
  an angle exist on cones exactly (computed) and, near Part I's data, on all of Part I's slice in a band widened by a
  computed amount (deduced): Rácz's split is hyperbolic on the slice except one band inside the shell, R between 4.29
  and 4.53 (computed, `docket68/n1star/checks/racglobal5.py`; its extent certified by interval arithmetic for the
  background with the record's characteristic data, whose reduction to ordinary differential equations is deduced, each
  edge enclosed to within 0.008, `docket68/n1star/checks/intcert5.py`, `docket68/n1star/checks/truebg5.py`), where no
  foliation of that slice is hyperbolic (deduced from Rácz's characteristic equation), and a slice bent by at most
  0.0012 is hyperbolic everywhere (certified for that background and for its computed approximation in a stated
  interpolant; `docket68/n1star/checks/racslice5.py`, `docket68/n1star/checks/intcert5.py`,
  `docket68/n1star/checks/truebg5.py`). Near Part I's data, exactly localised vacuum data whose first-order part
  perturbs the extrinsic curvature alone do not exist for small amplitude: their charge is minus a sum of squares minus
  a term carrying the mass, at the axes too (deduced; the identity computed exactly for every background and every R and
  θ, `docket68/n1star/checks/qsign5.py`, `docket68/n1star/checks/mbslice5.py`, and the last term's sign certified for
  that background and for its computed approximation in a stated interpolant, `docket68/n1star/checks/truebg5.py`,
  `docket68/n1star/checks/intcert5.py`); with matter obeying the dominant energy condition such data do not exist where
  f > 0, and where f < 0 they exist with outgoing null dust (deduced; the sign computed). For first-order parts that
  perturb the metric the charge is Q = 2∫_U G^(2)(ξ, n) =: −E, and its sign is decided
  (`docket68/n1star/FAMILIES5-MB.md`, `docket68/n1star/checks/mbsign5.py`, `docket68/n1star/checks/mbslice5.py`). Where
  f < 0, inside the apparent horizon R² = μ, E takes both signs on perturbations of tensor type, so near Part I's data
  exactly localised vacuum data background + εδ + O(ε²), δ a perturbation of the metric that is not a gauge one, exist
  for small amplitude on every vacuum band of the slice that meets {f < 0} (deduced, by intermediate values; the tensor
  sector's charge computed exactly on every slice). Where f > 0, E is positive on every invariant perturbation that is
  not a gauge one: in the class it is the sum, over the even harmonics, of the energies of Kodama and Ishibashi's master
  equations, whose potentials are positive in five dimensions for every l ≥ 2 (the reduction and the positivity computed
  exactly; the tensor harmonics beyond l = 8 and the passage to a static slice deduced). So on bands in {f > 0}, near
  Part I's data, no exactly localised vacuum data background + εδ + O(ε²) with δ an invariant perturbation that is not a
  gauge one exist for small amplitude: exact vacuum localisation fails there at second order.
```

## Files

`FAMILIES5-R10.md` (this note); the programs and outputs above; [R10] notes in FAMILIES5-R8.md, FAMILIES5-MB.md and
FAMILIES5-R6.md.
