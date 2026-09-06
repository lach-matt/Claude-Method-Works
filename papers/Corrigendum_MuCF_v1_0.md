# Corrigendum to *Muon-Catalysed Fusion: Definition, Procedure, and Two Gaps* (v1.0, 1 August 2026)

**Matthew Lach** — Independent researcher
*6 September 2026. Prepared with a computing collaborator under the protocols of* The Method *v1.2-8.*

*This corrigendum records seven corrections to v1.0 of the above paper. Six affect its §§3.2, 4 and 5;
one affects a table entry. The paper's definition (§1), its uniqueness argument (§2), its procedure
(§3.1, §3.3–§3.6), and its exclusions (§6) stand unaltered. A revised version incorporating all seven
is issued as v1.1. Every corrected figure is reproducible by `tools/mucf.py`, whose `--selftest` is
fixtured on v1.0's own Table 5.1.*

---

## Summary

v1.0 stated that two quantitative gaps separate the demonstrated d–t muon-catalysed reaction from
useful power, and that they are independent. **The claim of independence is withdrawn.** The two are
one collection chain read at two thresholds. Two further corrections follow from re-examining the
paper's energy accounting, and one from a temperature–density opposition the paper stated as two
separate operating recommendations.

The corrections do not weaken the paper's central results. The definition, the structural window
[119, 918] mₑ, the uniqueness of the muon, the procedure and the exclusions are unaffected. What
changes is the paper's statement of what remains to be done, which becomes both narrower and better
posed.

---

## Correction 1 — the two gaps are not independent

**v1.0, §5** — *"The two gaps are independent, and the second is the harder: it is not a parameter to
optimise but a machine that does not exist."*

**Corrected.** The 5 GeV figure in §4 is the cost per muon **produced**, and already presumes the
collection chain A3–A6 is solved. A real beamline **delivers** at a very different cost: PSI's ~1.4 MW
driver against ~10¹⁰ μ/s delivered is

> 1.4 MW ÷ 10¹⁰ s⁻¹ = 1.4 × 10⁻⁴ J = **874 TeV per delivered muon**, i.e. **1.75 × 10⁵** times 5 GeV.

The flux gap, computed from the other end, is 1.2 × 10¹⁵ ÷ 10¹⁰ = 1.2 × 10⁵. **These are the same
quantity.** The energy threshold and the flux threshold are two readings of one chain, and essentially
all of the deficit sits in stages A3–A6 — capture solid angle, decay acceptance, transport, stopping
fraction.

The paper's own figures were self-consistent; only the framing was wrong. At 5 GeV per muon, 1 MW of
driver beam yields 1.25 × 10¹⁵ μ/s, which is exactly what 1 MW of fusion requires.

**Consequence.** "A machine that does not exist" is correct but imprecise. Neither beam power nor pion
production is short: 1 MW of proton beam exists, and 1 MW at 590 MeV already yields ~10¹⁵ π⁻/s, the
requirement to within a factor of order one. What does not exist is a **collector** — and its design
objective is the inverse of every muon channel ever built, since every discard a physics beamline makes
(momentum spread, emittance, beam spot, background rejection) is one a reactor does not want.

## Correction 2 — the energy threshold is accelerator-dominated

**v1.0, §5.1** — *"Two sticking levers are required; neither suffices alone."*

**Narrowed.** That conclusion holds only with E_μ frozen at 5 GeV. The same paper's §4 identifies E_μ
as "the most tractable free parameter", with 16.7× of headroom against the 0.30 GeV kinematic floor and
"none of it forbidden". §5.1 does not vary it.

At the kinematic floor, **measured** sticking (0.45 %, SIN) already returns **Q ≈ 13**. Restated as the
viability inequality N > E_μ/Q_fus — where N is a sticking quantity and E_μ an accelerator quantity —
breakeven requires **either** both sticking levers **or** a sub-2× accelerator improvement:

| service life convention | crossover E_μ (heat) | improvement required |
|---|---|---|
| φ = 1.2, decay-corrected | 2.93 GeV | 1.70× of 16.7× |
| φ = 3.0, decay-corrected | 3.45 GeV | 1.45× |
| N = 222, asymptotic | 3.90 GeV | 1.28× |

The accelerator deficit is 4.3× the sticking deficit in joules per muon. §5.1's table is correct; its
framing understates the accelerator.

## Correction 3 — Q in §5.1 counts heat against work

**v1.0, §5.1** — Q is computed as 17.59 MeV of fusion yield against GeV of accelerator input.

**Corrected.** This compares a joule of heat with a joule of work. Only the α's 3.5 MeV (19.9 %)
deposits in the fuel; the neutron's 14.1 MeV (80.2 %) escapes to a blanket which may sit at any
temperature — 62 % Carnot at 800 K against 300 K ambient. The convertible fraction is **50.1 %**.

**Work-breakeven is E_μ < 1.96 GeV, a 2.55× accelerator improvement** — still inside the 16.7×
headroom, but twice the ask the heat convention implies, and it is the correct threshold for a plant.

## Correction 4 — the cryogenic operating branch is excluded

**v1.0, §3.2** — *"Density: φ as high as the cryogenics permit."* and *"Temperature: high, not low."*

**Corrected.** These are opposed, and v1.0 gave them as separate recommendations without saying so.
The formation resonance pushes hot (λ_dtμ rises ~2 orders toward 800 K); density pushes cold (hydrogen
is liquid at 20 K, gaseous above 33 K).

The opposition resolves against the cryogenic branch on thermodynamics alone. Below ambient, fusion
heat can do no work, and at 20 K removal costs 10.4× the heat removed:

| fuel T | blanket T | recovered | cooling | net |
|---|---|---|---|---|
| 20 K | 800 K | 0.501 | 10.446 | **−9.945** |
| 300 K | 800 K | 0.501 | 0.000 | +0.501 |
| 800 K | 800 K | 0.501 | 0.000 | +0.501 |

**A μCF reactor cannot be net-positive while cold**, and no accelerator or sticking improvement
rescues it. The operating point is high temperature at high pressure — of order kilobars for 1 LHD at
800 K — with density bought mechanically rather than cryogenically. Above ambient the recovered
fraction is fixed by the blanket, not the fuel.

This is a **bracket**, with the same two-bound shape as the mass window of §2: bounded below by a rate
condition and above by a degeneracy condition. v1.0 did not name it.

## Correction 5 — Table 5.1, row ω_s = 0.234 %

**v1.0, §5.1, Table 5.1** — the row reads 0.93 / 1.10 / 1.21 at φ = 1.2 / 2.0 / 3.0.

**Corrected.** Those values reproduce at λ_c ≈ 2.69–2.74 × 10⁸ s⁻¹ — the unrounded transfer rate
2.7 × 10⁸ — rather than the 2.6 × 10⁸ saturation the paper pins in §3.3. The row is computed at the
cap's parent rather than at the value stated beside it. **At the pinned λ_c the row reads
0.92 / 1.09 / 1.20.**

The remaining twelve cells of Table 5.1 and all three breakeven thresholds (0.202 / 0.262 / 0.292 %)
reproduce exactly. The row still clears breakeven at φ ≥ 2, so the paper's conclusion survives; the row
was marginally optimistic against its own parameter.

## Correction 6 — the ~222 sticking ceiling is an asymptote

**v1.0, §3.4** — *"a sticking ceiling of ~222 turns."*

**Clarified.** 1/ω_s = 222 is the limit of N = φλ_c/(λ₀ + ω_s·φλ_c) as φ → ∞, and omits muon decay. The
decay-corrected service life is 167 at φ = 1.2 and 196 at φ = 3.0. Figures quoted against 222 are
therefore ~13 % optimistic; the corrected crossover is 3.45 GeV rather than 3.90 GeV. Both conventions
are stated in v1.1 §5.1 and neither is presented as the other.

## Correction 7 — a reservation promoted

**v1.0, §7** carried, among reservations, that *"whether the 0.31 % figure is initial or
post-reactivation sticking is not resolved by its source."*

**Promoted to the body.** The composed value ω_s = 0.234 % is 0.34 % × (0.31/0.45), so the entire
"both levers" row of Table 5.1 — the row on which v1.0's breakeven claim rests — inherits an
unresolved figure. This is stated in v1.1 §5.1 rather than left in the reservations list.

---

## What is unaffected

The definition of cold fusion as binding-geometry fusion and its seven necessary conditions; the
structural window [119, 918] mₑ and the uniqueness of the muon within it; the reaction
μ⁻ + (d,t) → (dtμ)⁺ → ⁴He + n + μ⁻ + 17.59 MeV and the fixing of its formation and exit channels; the
cycle and its rates; the exit branching; the two observables and the requirement that they be run
simultaneously; the failure signatures; the ash bracket; the ambient exclusion by adiabaticity and
energy audit; and the exclusion of chain multiplication on the grounds that no nuclear event funds a
muon.

## What remains open

The per-stage collection budget for A3–A6 does not exist. "None of it is forbidden" is a statement
about physics, not engineering. Until a stage-by-stage accounting with a defensible ceiling on each
stage exists, against which the 1.75 × 10⁵ can be allocated or shown to be unallocatable, the honest
statement is that the problem is well posed and unsolved.

## Reproducibility

All corrected figures are computed by `tools/mucf.py` (stdlib only). `--selftest` asserts v1.0's own
Table 5.1, its three breakeven thresholds, the composed lever, the sticking ceiling, scientific
breakeven at 5 GeV, and every figure in this corrigendum. `--collector` prints Correction 1; `--work`
prints Correction 3; `--band` propagates the ±33 % transfer-rate uncertainty that Corrections 2 and 5
both inherit.
