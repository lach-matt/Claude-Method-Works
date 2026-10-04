# DOCKET 68 · WAVE 2 · W2B-vacuum: vacuum entanglement as the pair supply (N_VAC, O-MAKE-DIST)

**Status: a docket work item, wave 2 (2026-10-04). Nothing here is seated.** This is step 2 of M's order (M-RULINGS item 10:
*"1 then 2 then 3 then 4"*). The instrument is `vacuum.py`, beside this file. `PYTHONDONTWRITEBYTECODE=1 python3 vacuum.py
--selftest` runs **50 counted checks and passes all 50**, in about 110 s. **10 of them are controls** built to fail
if the code is wrong. One counted check, B1, did fail during the build and exposed a fault in the draft (section B). **9 items cannot fail.** They are printed STRUCTURAL and not counted. `python3
vacuum.py` prints the report, and `--json PATH` writes it as JSON.

`vacuum.py` imports what it uses and copies nothing. From `settle.py` it takes `first_transit_times`, which is LEDGER D23 as
corrected in DOCKET 67 and prices the probes. It also takes `bloch_exact` and `bob_y_exact`, which give W2's drift on a
branch, and the constants `C_LIGHT`, `AU_M`, `LY_M` and `YEAR_S`. From `../transit.py` it takes `teleport`, `fidelity` and
`TRAVERSAL_IS_REMOVED`. It writes nothing outside the output path the caller names.

## M's words, and what wave 1 left

> What if information is faster than light, not because us moves faster, but because is already exists everywhere?
> (CHARTER.md, verbatim)

`combine.py` carries this reading as the OPEN pathway **N_VAC**: *"pre-existing entanglement (of the vacuum) usable as the
channel's pairs with no distribution"*. B-combine records the result as **"O-MAKE in its distribution form, OPEN via N_VAC
only"**. In wave 1, N_VAC's text said: *"Whether any setup supplies the pairs a qubit needs faster than distribution is NOT
computed: OPEN"*. This file computes it.

## The answer, first

1. **M is right that the entanglement is already there.** Two probes that cannot communicate do end up entangled by the
   vacuum, and no entangled carrier crosses between them. This is READ in Reznik, Reznik-Retzker-Silman, Pozas-Kerstjens &
   Martín-Martínez and Tjoa & Martín-Martínez. This file reproduces Reznik's two figures, and PKMM's closed forms are checked
   against independent integrals. RRS show it at **any** separation.
2. **Usable pairs do not arrive without something crossing at ≤ c first.** That is computed. The crossing moves:
   - The probes must be in place. D23, imported, prices this at L/2c from a midpoint and L/c from one end.
   - The harvest window must itself last a fixed fraction of the light time: **T > 0.9097 L/c** for Reznik's window at any
     gap in [2, 40], or **7T = L/c** for a Gaussian at β = 7.
   - A near-maximal pair needs classical messages in **both** directions. The harvested state has a symmetric extension on
     each side, so by Chen et al.'s Theorem 1 no protocol with no messages, or with messages in one direction only, can
     distil it.

   So the vacuum route's **floor**, for any protocol, is **2.41-3.00 L/c**. A midpoint pair source is ready at **0.50 L/c**.
   The computed recurrence-and-hashing protocols take **43-204 L/c**.
3. **O-MAKE-DIST: OPEN → LEFT-IF {H-UDW, H-PERTURB, H-O4-FLOOR, H-MINK-VAC, H-SPACELIKE, H-LOCC, H-IID, H-NEARMAX,
   H-PROBE-OPERATED}.** Distribution is relocated, not removed: from the pairs to the probes and to two-way classical
   messages. Outside that set it is **OPEN** via N_NLDIST, N_W2WEAK and N_VACNP, and none of the three is computed. *Wave 1
   said: OPEN via N_VAC only.*
4. **Weak pairs used as they come (H-NEARMAX dropped).** These figures are at β = 7, λ = 0.1.
   - Teleportation fidelity is **2/3 + 2N/3**, an excess of **2.7e-17** over the classical 2/3. The harvested state already
     sits at the ceiling (f = 1/2 + N) that Verstraete-Verschelde and Vidal-Werner set for any LOCC on one copy.
   - W2's drift signal per pair is **second order** in Bob's branch transverse length: ρ⊥ = 3.1e-15, giving a signal of
     **5.8e-30**, against 0.537 for a Bell pair.
   - Neither figure is zero, and **O-BITS is untouched**. The two classical bits of teleportation remain.
5. **Scaling with distance.** At a fixed window the harvested negativity falls faster than any power of L in both computed
   families. For the Gaussian, **N+_max ≈ (e/2π) e^(−β²/2) β⁻⁴** at the best gap α² ≈ β² − 2. That is DERIVED here and within
   1% of the computed value at β = 14. Reznik's window harvests for no gap beyond **L/T = 1.0993**.

   The massless model has no scale of its own. A fixed negativity at any L therefore needs **T ∝ L**: the harvest lasts a
   fixed fraction of the light time. No READ upper bound covers 3+1 detectors with every possible window, so that bound is
   **OPEN**.

## Sources READ at source this pass (M-RULINGS items 15-16: web instruments, open content only)

| id | source | route | used for |
|---|---|---|---|
| R1 | Reznik, quant-ph/0212044v2 ("Entanglement from the vacuum") | READ via alphaXiv (answer_pdf_queries, full text), pp.1-15; **figures re-read**: Fig.1 p.11, Fig.2 p.12 | eq.(19) entanglement condition, p.10; eq.(20) window, p.11; Fig.1 "8 < Ω < 11" (L = T = 1); Fig.2 "L/T < 1.1" (Ω = 9.5); p.13 purification "approach gradually to a perfect pure EPR-Bohm pair" |
| R2 | Reznik, Retzker & Silman, quant-ph/0310058v2 ("Violating Bell's inequalities in the vacuum") | READ via alphaXiv, pp.1-4 | "arbitrarily far-apart regions"; eq.(8) N ≥ e^(−(L/cT)³); "N(ρ) ≥ e^(−(L/T)²)" (numerical, p.3); local filters eqs.(9)-(10): close to maximally entangled "at the price of reducing the detectors' entanglement" (p.4) |
| R3 | Pozas-Kerstjens & Martín-Martínez, arXiv:1506.03081v7 ("Harvesting correlations from the quantum vacuum") | READ via alphaXiv, pp.1, 3-8, 11, 14-15 | eq.(13) state; eq.(22) Gaussian switching; eqs.(33), (34), (37) closed forms; eq.(68) N = \|M\| − L; p.11 fourth order adds nothing new |
| R4 | Tjoa & Martín-Martínez, arXiv:2109.11561v3 ("When entanglement harvesting is not really harvesting") | READ via alphaXiv, pp.1-8, 13 | commutator part = communication (state-independent); eq.(38) N+; eq.(28) strong support [−3.5T, 3.5T]; compact switching "essentially the same" (p.13) |
| R5 | Bennett, Brassard, Popescu, Schumacher, Smolin & Wootters, quant-ph/9511027v2 | READ via alphaXiv, pp.1-4 | eq.(7) recurrence; "two-way classical communication"; eq.(8) hashing yield, "positive for F > 0.8107" |
| R6 | Bennett, DiVincenzo, Smolin & Wootters, quant-ph/9604024v2 | READ via alphaXiv, pp.1, 6-11, 22-42 | "EPPs require classical communication" (abstract); eqs.(42)-(43); "D2(W_5/8) > 0.00457" and "D1(W_F) = 0 for all F < 3/4" (p.42) |
| R7 | Vidal & Werner, quant-ph/0102117v1 | READ via alphaXiv, pp.1-7 | N; Prop.3 (LOCC monotone, on average); eq.(39) F_opt ≤ (1+2N)/m; Prop.7 E_D ≤ E_N |
| R8 | Verstraete & Verschelde, quant-ph/0203073v3 | READ via alphaXiv, pp.1-4 | Thm 1: F ≤ (1 + N_VV)/2, N_VV = 2N |
| R9 | Chen, Ji, Kribs, Lütkenhaus & Zeng, arXiv:1310.3530v2 | READ via alphaXiv, pp.1-4 | Thm 1: symmetric extension iff tr(ρ_B²) ≥ tr(ρ_AB²) − 4√det ρ_AB; p.1 no one-way distillation from an extendible state; p.4 Werner boundary at fidelity 3/4 |
| R10 | Horodecki ×3, quant-ph/9607009; quant-ph/9801069 | READ (abstract) via Firecrawl inspect_paper | any inseparable 2×2 state is distillable (filtering + BBPSSW); distillable ⇒ NPT |
| R11 | Marcovitch, Retzker, Plenio & Reznik, arXiv:0811.1288 | READ (abstract) via Firecrawl inspect_paper | 1D field: long-range entanglement "decays exponentially". Corroboration only; no number uses it |

No paywall or login wall was met; every source is an arXiv open copy. Only short phrases are quoted.

## What `vacuum.py` computes

### A. Reznik's inertial probes reproduced (R1, the control)

The amplitude ratio |⟨0|X_AB⟩|/|E_A|², R1 eq.(19), is computed for the window cos²(πt) on |t| ≤ 1/2 with T = 1. The exchange
amplitude is computed two independent ways, in momentum space and as a time-domain double integral. The two agree to a
relative 1.1e-11.

| | computed | READ |
|---|---|---|
| Fig.1 (L = T): window in Ω | **8.025 < Ω < 10.537**; peak 1.306 at Ω = 9.44 | "8 < Ω < 11" |
| Fig.2 (Ω = 9.5): edge in L | **L/T < 1.0974** | "L/T < 1.1" |
| ⇒ window as a fraction of the light time | T/(L/c) ∈ (0.9113, 1) at Ω = 9.5 | combine's DERIVED-FROM-READ (0.909, 1) |

**Reading note.** The text layer prints the window as "cos²(t)". That literal window switches on suddenly, and its emission
integral grows ×1.913 as the cutoff goes from 500 to 8000: it diverges logarithmically. cos²(πt) changes by ×1.0000004 over
the same range. Only cos²(πt) reproduces both figures, so the reading is DERIVED by reproduction (control A5). A second
control (A6) shows that a factor-2 error in the emission term would remove Fig.1's window entirely.

### B. Gaussian switching (R3 closed forms; R4's split)

The closed forms used are R3 eq.(33) for L_AA, eq.(37) for M (split as R4 does into M+, the erfi term, which is harvesting,
and M−, the −i term, which is the commutator and so communication) and eq.(34) for L_AB. All three are checked against
independent integrals at four values of (α, β), agreeing to a relative 1e-5 or better. The M route uses a principal value
derived here.

**History.** The first draft's numeric route for L_AB used too loose a tolerance. Check B1 **failed** at (7, 7), with a 3%
disagreement. The closed form was right, and the numeric route was tightened. The same draft labelled L_AB at γ = 0
"purely imaginary"; it is real, because w(−z₁) = conj(w(z₂)), and the STRUCTURAL label now says so.

| β = L/cT | α at best N+ | N+_max / λ² | N_max / λ² (with commutator) | N+ / asymptote |
|---|---|---|---|---|
| 1 | 0.936 | 1.85e-2 | 3.70e-2 | 0.070 |
| 2 | 1.566 | 2.45e-3 | 2.72e-3 | 0.670 |
| 3 | 2.610 | 6.31e-5 | 6.33e-5 | 1.064 |
| 5 | 4.792 | 2.49e-9 | 2.49e-9 | 0.964 |
| 7 (supports spacelike) | 6.855 | 4.00e-15 | 4.00e-15 | 0.971 |
| 10 | 9.899 | 8.20e-27 | 8.20e-27 | 0.983 |
| 14 | 13.928 | 3.07e-48 | 3.07e-48 | 0.991 |

- At β = 1 half of N is communication (N/N+ = 2.00). At β = 7 the commutator contributes nothing (check B6), which
  matches R4.
- The asymptote (e/2π) e^(−β²/2) β⁻⁴ is DERIVED. Using the next terms of the erfi and erfc expansions, the bracket is
  (4 + δ) e^(−δ/2)/β⁴, which is greatest at δ = α² − β² = −2.
- **History.** The first hand derivation dropped the 1/β⁴ and 3/α⁴ terms. It gave e^(−β²/2)/(2πeβ⁴), off by e² = 7.39.
  It is kept as control B3, which rejects it (measured ratio 7.32).

### C. A compact window, strictly spacelike, at every gap

Reznik's window gives L > cT exactly, so the commutator vanishes and there is nothing to separate. The negativity is
maximised over Ω ∈ [2, 40]:

- N_max/λ² = 7.48e-5 at L = T (best Ω = 9.00);
- 2.97e-5 at L/T = 1.05;
- **0 for every gap from L/T = 1.0993**, found by bisection with best Ω = 9.35 just inside. That makes **T > 0.9097 L/c**.

Gaps above 40 were not scanned, which is a named limit. R2's superoscillating windows do harvest at any L, and are not
recomputed here.

### D. The harvested state, its fidelity and what one copy is worth

The state is R3's eq.(13), with ρ_ee,ee at H-O4-FLOOR. The case shown is β = 7, λ = 0.1; the λ = 0.01 rows are in the
report.

| quantity | value | how |
|---|---|---|
| N | 4.00e-17 | exact X-state block formula. The full-matrix eigensolver agrees where double precision can resolve N (β = 3, λ = 0.3: 5.6998e-6 both ways, D1) |
| f − 1/2 | 4.00e-17 = N | R8 Thm 1's ceiling, **saturated**. At β = 3, λ = 0.3 Horodecki's SVD formula gives the same value (D1b) |
| teleportation fidelity − 2/3 | 2.67e-17 | (2f+1)/3. A simulated standard protocol equals the formula (D1c). Controls: a Bell pair gives 1, as `transit.teleport` does; a product state gives 2/3 |
| E_N | 1.16e-16 bits | log₂(1 + 2N) |
| copies per ebit | ≥ **8.66e15** | R7 Prop.7, E_D ≤ E_N: a floor for any protocol (λ = 0.01: 8.66e17) |
| symmetric-extension margin on B, and on A | +1.99e-15 each (≈ 2 L_AA; also positive at 10× the ρ_ee floor) | R9 Thm 1, X-state form without cancellation. The generic routine agrees at β = 3 (D1d). Controls: Werner states change sign at F = 3/4 (+0.0002 at 0.7499, −0.0002 at 0.7501), and a Bell pair gives −0.500 |

**Consequence (R9 p.1, computed for every case in the table).** The harvested state has a symmetric extension in both
directions. No protocol using local operations alone, or local operations with one-way messages in either direction, can
distil it. Distillation needs messages each way.

### E. Local operations alone (no communication)

The test applies 3,000 random local channels and the amplitude-damping family to one side and to both sides. Across all of
them, **N never rises** (largest rise 0, R7 Prop.3) and **f never passes 1/2 + N** (largest excess 0, R7 eq.39 and R8
Thm 1). Two controls do break the bounds: a global unitary takes f to 0.9999, and a CNOT raises N on a product state from 0
to 0.5.

R2's local filters do produce near-maximal **heralded** pairs. At a gap three times the optimum (|M+|/L_AA = 9.26), the
heralded fidelity is **0.9025** against 0.5000 unfiltered. The success probability is **1.8e-201**. Averaged over the four
joint outcomes, the negativity falls (Σ pᵢNᵢ ≤ N in both cases tested). Each party sees only its own filter's outcome, so
telling which pairs passed takes a message from each side.

### F-G. Distillation with messages: one protocol, priced (H-PROTOCOL)

The formulas are checked against READ values first:

- **0.81071** for the hashing threshold (R5: 0.8107);
- R5 eq.(7) equals R6 eqs.(42)-(43) under the twirl, to below 1e-14;
- R6's printed **0.00457** for W_5/8, reproduced as 0.0045701 using a fixed rotation after each step that swaps the 10 and
  11 components. That component map was **identified by searching** the six maps that leave 00 fixed, and was not READ:
  R6 names only "Macchiavello's B_x". With no rotation the yield is 3e-8 (control G4).

Starting from the twirled harvested state, F = 1/2 + N, the recurrence needs this many rounds before hashing pays:

| N₀ | 1e-2 | 1e-4 | 1e-8 | 1e-12 | 1e-17 | 1e-20 |
|---|---|---|---|---|---|---|
| rounds (twirl) | 20 | 45 | 95 | 146 | 209 | 247 |

The rounds grow as log(1/N₀)/log 1.2, because F' = 1/2 + 1.2δ + … near F = 1/2. At β = 7 and λ = 0.1 that is **201 rounds**
and 10^111 pairs per surviving pair with the twirl, or **106 rounds** and 10^61 pairs with the rotation. These price these
protocols only. The floor for every protocol is the single exchange in each direction required by R9, together with R7's
bound on copies.

### H. W2 on a harvested pair (settle's drift law, imported)

The law is H = ε⟨X⟩Z per branch, under H-C2 and H-NLCONTROL-FORM. On a Bell pair `bloch_exact` reproduces settle's
tanh(2εT) exactly (0.537050 at ε = 0.1, T = 3; check H1). On the β = 7 harvested pair, Bob's branch states lie almost on
|g⟩, with ρ⊥ = 3.10e-15. The signal comes out at exactly 2εTρ⊥² (ratio 1.0000): **5.76e-30**. That is second order, below
the 1e-12 fraction of the Bell signal that check H2 allows. W2 × F1's pair counts in A1 and B-combine assume Bell pairs. With
harvested pairs a usable W2 signal would need N_W2WEAK, which is not computed.

### I. The timeline, with the probes priced as D23 prices a pair source

Times are counted from launch: the probes move at c (`settle.first_transit_times`), the window follows, and then come the
messages, one simultaneous exchange per round (H-SIMUL).

| case | probes in place | window | **floor, any protocol** | recurrence + hashing | midpoint pair source |
|---|---|---|---|---|---|
| Gaussian β = 7, λ = 0.1, probes from the midpoint | 0.5 L/c | 1.0 L/c | **2.50 L/c** | 203.5 L/c (twirl) / 108.5 L/c (rotation) | 0.50 L/c |
| same, probes from one end | 1.0 L/c | 1.0 L/c | **3.00 L/c** | 204.0 / 109.0 L/c | 0.50 L/c |
| Reznik window, L/T = 1.05, λ = 0.1, midpoint | 0.5 L/c | 0.952 L/c | **2.45 L/c** | 79.5 / 42.5 L/c | 0.50 L/c |
| same, one end | 1.0 L/c | 0.952 L/c | **2.95 L/c** | 80.0 / 43.0 L/c | 0.50 L/c |

Every entry scales with L, so the factors are the same at 1 AU and at 1 ly. At 1 ly, the floor for the midpoint Gaussian
case is 7.89e7 s, or 2.5 yr. Every vacuum-route floor arrives **after the light time**, and the midpoint pair source arrives
before it (I1, all four cases).

Probes placed in advance amortise their placement exactly as pairs stored in advance do. Neither changes O-BITS: the two
classical bits per teleported qubit are still sent at c when the pair is used.

## Grades (this file's; combine's screen is not edited here)

| item | grade | premises |
|---|---|---|
| N_VAC (i): vacuum entanglement reaches probes that cannot communicate, with no entangled carrier crossing | **TRUE-IF** | {H-UDW, H-PERTURB, H-MINK-VAC, H-SPACELIKE}; R1-R4 READ; R1 Figs.1-2 reproduced |
| N_VAC (ii): usable as the channel's pairs with nothing crossing at ≤ c first | **FALSE-IF** | {H-LOCC, H-NEARMAX, H-PROBE-OPERATED}: probes cross (D23); messages each way (R9, computed); window ≥ 0.91 L/c (compact) or 7T (Gaussian) |
| **O-MAKE-DIST** | **LEFT-IF** {H-UDW, H-PERTURB, H-O4-FLOOR, H-MINK-VAC, H-SPACELIKE, H-LOCC, H-IID, H-NEARMAX, H-PROBE-OPERATED}; **OPEN** outside it via N_NLDIST, N_W2WEAK, N_VACNP | relocated, not removed. *Wave 1 said: OPEN via N_VAC only* |
| O-BITS | **unchanged** (LEFT) | no part of the vacuum route touches the two classical bits (`transit.CLASSICAL_BITS_PER_QUBIT` = 2; `READING_CARRIES_NOTHING_ALONE` = True) |

**A suggestion for the seating step, not applied** (combine.py and the ledger are not edited in this wave). N_VAC could be
replaced in combine's OPEN list by the three named escapes. A premise could also be added under which B-LOCC binds with N_VAC
read as (ii). Whether to do so is for the seating step and M.

## Named hypotheses (every limitation is one)

- **H-UDW**: pointlike two-level detectors coupled to a massless scalar in 3+1 flat space. Atoms and the electromagnetic
  field are not computed here, although R2 states that similar results hold for them.
- **H-PERTURB**: everything is at order λ², per λ². Non-perturbative harvesting is not computed.
- **H-O4-FLOOR**: ρ_ee,ee is set to max(|M|, |L_AB|)²/(1 − 2L_AA). The verdicts are checked at the floor and at 10×.
- **H-MINK-VAC**: no curvature, no thermal bath, no boundary.
- **H-SPACELIKE**: harvesting means the probes cannot communicate. That requires compact windows with L > cT, or Gaussian
  windows with β ≥ 7.
- **H-LOCC**: linear QM. R5-R9 are theorems of linear QM, and under W2 local maps are not linear (N_NLDIST).
- **H-IID**: harvests are independent copies. Repeated harvests at the same probes are not shown independent.
- **H-NEARMAX**: the consuming channel needs near-maximal pairs. Without it the weak pair's value is the 2/3 + 2N/3 and
  2εTρ⊥² above.
- **H-PROBE-OPERATED**: a probe is an operated device. Matter merely present at the far end, such as an S5-type stock, is
  not one.
- **H-PROTOCOL**: round counts price BBPSSW and BDSW protocols, not the minimum.
- **H-SIMUL**: one round costs L/c.
- **H-LAMBDA-ILLUSTRATIVE**: λ = 0.1 and 0.01 are illustrations, not the coupling of any device.

## Open pathways named here (none assumed in a removal)

- **N_NLDIST**: a state-dependent local operation that raises entanglement without messages. Not computed. Under H-C2 the
  drift needs a branch, that is, a measurement that consumes the pair.
- **N_W2WEAK**: W2 drawing a usable signal from many weak pairs. The per-pair figure is computed (second order); the
  many-pair case is not.
- **N_VACNP**: harvesting outside H-UDW or H-PERTURB that escapes the Gaussian decay in distance. No READ source was found
  this pass.

## Over-representation, both ways

- **FOR M, kept.** The vacuum's entanglement does exist across spacelike separations. It is extracted without anything
  entangled crossing, at any L (RRS), and the negativity depends only on (ΩT, L/cT): distance alone does not destroy it.
  This file does not say "the vacuum is not entangled", nor that harvested pairs are worthless. One copy does beat classical
  teleportation, by 2N/3.
- **AGAINST M, kept.** "Already exists everywhere" does not make the pairs **usable without transit**. The probes travel.
  The harvest lasts about the light time. Distillation needs messages each way, so its floor is 2.4-3.0 L/c, against 0.5
  L/c for a midpoint source. The amounts are exponentially small in (L/cT)². None of it reaches O-BITS.
- **Not over-claimed.** The BBPSSW/BDSW round counts are one protocol's price, not a bound. The Macchiavello component map
  was identified by search, not read. The asymptote is DERIVED, not READ. No upper bound covering every window in 3+1 is
  read.

## Reproduce

```
cd research/warp-drive/docket68
PYTHONDONTWRITEBYTECODE=1 python3 vacuum.py --selftest     # 50/50 counted, 10 controls, 9 STRUCTURAL (~110 s)
python3 vacuum.py --json /tmp/vacuum.json                 # the report above
```
