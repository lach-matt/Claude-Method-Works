# POWERSOURCE.md — the inverse problem

`tools/powersource.py` runs the balance backwards. Every other instrument here takes a configuration
and returns a number; this one sets the number to unity and returns the configuration.

    python3 tools/powersource.py            # the specification
    python3 tools/powersource.py --selftest # 15 checks, stdlib only

## Why it exists

The paper reported that no heat form and no work form clears unity. That is a verdict. The project
asked for a **specification** — identify the self-sustaining power source using the mathematics,
describe what it should look like, and say how it is measured — and a verdict is not one.

## What it does

`G = N·V·η/E_π = 1`, solved for each term with the others held where the machine of §7 puts them.

**Two of the four terms are closed above by physics rather than by engineering**, and the instrument
reports which rather than quoting a number:

- the service life `N` is capped at `1/ω_s` = **198** cycles — the requirement is 878.7, forbidden by
  **4.44**;
- the collection `η` is a fraction — the requirement is **284.7 %**.

**Two are bounded by nothing proved anywhere in the corpus**: the production cost `E_π` and the value
recovered per fusion `V`. And `E_π` cannot carry the requirement alone, because the **1.900 GeV** it
would need is below even the published optimisation at 4.69. So the whole question is `V`, and `V` is
the blanket.

## The subcritical relation

One source neutron entering an assembly of multiplication factor `k` is multiplied over all
generations to `1/(1−k)` neutrons — a geometric sum that converges *because* the assembly is
subcritical. One of those is the source neutron, so `k/(1−k)` were born in fission, and each fission
makes `ν` of them. Hence

    F = k / (ν(1−k))      fissions per source neutron
    E = F · E_f           energy released

with ν = 2.9 (fast Pu-239) and E_f = 200 MeV. Two sourced inputs, one identity, no fitted parameter.
Corollary 10.1 inverts it: `k = r/(1+r)` with `r = E·ν/E_f`, which is below unity for any finite `E`,
so the question is never *whether* but *how far below*.

**It is checked before it is trusted.** The sourced fission-suppressed blanket multiplies the
neutron's energy by 1.6; attributing all of that to fission — an overstatement, some is ⁶Li exotherm —
puts it at `k ≤ 0.246`. A design built to suppress fission sits deeply subcritical, which is where it
should sit.

## The specification it returns

| configuration | V required | k required | the fusion's share |
|---|---|---|---|
| the machine as built | 234.3 MeV | **0.770** | 7.5 % |
| with both collector alterations | 152.7 MeV | **0.684** | — |
| with the optimised production target | 98.7 MeV | **0.580** | — |
| with all three alterations | 64.3 MeV | **0.469** | 27.4 % |

Against **0.95** for an accelerator-driven subcritical system and **1.000** for a power reactor. The
requirement is met with a very large margin to criticality, which is a safety property as much as an
engineering one.

## The spallation comparison — `--spallation`

The obvious objection to §9.2 is that the same protons could drive a subcritical blanket by spallation
alone, without a solenoid, a fuel cell or a tritium inventory. The answer turns on the structure
rather than on the arithmetic.

**The muon channel does not replace spallation.** The same protons strike the same target and make
both — pions *and* spallation neutrons, in the same collisions, which is the premise §9.2 rests on.
The channel is therefore **additive in neutrons**, and there is no *instead* to price.

**What it can cost is the target.** A target the pions can escape from is narrow, and a narrow target
is a poorer spallation source than the thick one a facility would otherwise choose. That is the whole
of the trade. Setting a spallation-optimised target's yield `Y` against a transparent one's `Y(1−f)`
plus the muon channel's fusion neutrons, the channel gains whenever

    f  <  w · Y_fus / Y,      Y_fus = Y_π · η · N

and `Y_fus` is fixed by figures already in the ledger: **52.41 neutrons per proton** with both
collector alterations, 34.14 as built. So:

| spallation-optimised yield | transparency may cost up to |
|---|---|
| 100 n/proton | 52.4 % |
| 150 n/proton | 34.9 % |
| 250 n/proton | 21.0 % |

**Conservative in three places, all the same way.** It counts a 14.1 MeV neutron as worth exactly one
spallation neutron, where in a fast blanket it is worth more. It does not count the alpha. And it
treats transparency as a straightforward loss, which in a **blanket-coupled** system it is not — a
neutron or secondary escaping a narrow target is not lost, it enters the blanket. A narrow target
costs a *neutron source* its yield because the neutrons must reach moderators; it costs a
blanket-coupled system much less.

## The two target figures — `--target`

**One: what a spallation-optimised target returns.** A target thick enough to contain the cascade
degrades essentially all of the beam into it, and the neutron yield *per unit of energy deposited* is
a flat property of the material rather than of the machine — **25 to 30 neutrons per GeV** for lead or
mercury. At 8 GeV that is **200 to 240 neutrons per proton**, the top of the `--spallation` scan and
the place where the requirement on transparency is tightest.

**Two: what transparency costs it — and here the question changes.** The production target this work
specifies is the published mercury jet. Mercury's inelastic interaction length is 15 cm, and the jet
is **2.00** of them long and **0.027** across:

| along the beam | 2.00 λ | 86.5 % of primaries interact |
|---|---|---|
| **across it** | **0.027 λ** | **2.6 % of the cascade is kept** |

**It is not a narrow spallation target. It is a production foil.** It stops the primary and retains
almost none of the cascade that primary starts. In a bare neutron source that would be the whole loss,
because the neutrons must be made in the target — there is nowhere else. In a **blanket-coupled**
system there is somewhere else: the cascade crosses into the blanket and develops there. Writing `y`
for neutrons per GeV deposited and `φ` for what the target retains,

    Y = E [ φ·y_target + (1−φ)·y_blanket ]

so the penalty against a fully-containing target of the same material is `(1−φ)(1−y_blanket/y_target)`
— **negative for any blanket that out-yields the target per GeV**, and a fissile one does. Depleted
uranium out-yields lead by about 1.5, so the penalty is **−48.7 %: a gain, not a cost.**

**The conclusion does not rest on that figure.** The penalty is *exactly zero at parity* and turns
positive only for a blanket **worse** per GeV than the target it replaces — a low-Z or non-fissile
one, which is not what §9.2 specifies. It would survive both inputs being wrong by any amount short of
reversing that inequality, and the selftest asserts the sign turns at parity rather than anywhere
convenient.

## What is left, and it is a margin rather than a question

`--target`'s retention is **geometry, not transport**: `1 − exp(−r/λ)` does not follow a cascade
through the assembly, and Proposition 10's blanket relation is point kinetics. Both are used as
**requirements rather than predictions**, both say so where they appear, and §10 Stage D measures what
they estimate — on one apparatus, the same beam and the same blanket with the fuel cell in and out.

**It does not predict a blanket's yield.** Proposition 10 is point kinetics: one multiplication factor
for the whole assembly, no source position, no leakage, no spectrum. A real blanket's source is
central and its neutrons enter at 14.1 MeV rather than at a fission spectrum's mean, both of which
raise the yield above this estimate for the same `k`. **The proposition is a requirement, not a
prediction**, and §9.3 of the paper states the three measurements that would replace it — pulsed
neutron by the Sjöstrand area method, source jerk, and Rossi-α noise — with the rule that two of them
disagreeing is a refusal rather than an average.

## What it costs to say

At the least demanding configuration the fusion supplies **27.4 %** of the recovered energy and all of
the neutrons; at the most demanding, **7.5 %**. The device is a **fusion-driven subcritical fission
reactor**, and calling it a fusion power plant would be false. It is a self-sustaining power source on
the project's own criterion — it returns more energy than the beam that drives it, as heat, on site,
with nothing leaving the device — and both halves of that are stated in §9.2 because neither stands
alone.

## The criterion the project asked for — `--plant`

Everything above prices the reaction against the **beam**. That is the eighth condition's question and
the right one to ask of a *reaction*. It is the wrong one to ask of a *power source*, and the reason is
easy to walk past: **the beam does not stop.** A machine that returns more than its beam is an
**amplifier** — it needs feeding for as long as it runs. A machine that needs nothing after start-up is
a **power source**. The difference is two conversions nothing in this work had counted:

    G_loop = G · η_th · η_acc > 1      ⟺      G > 1/(η_th · η_acc)

`η_th` is bounded above by Carnot at the blanket temperature (0.750, already in the ledger); a real
cycle reaches about 0.60 of its ceiling, so 0.450. `η_acc` — wall plug to beam for a high-power proton
linac — runs 0.20 to 0.50. So the loop needs **G between 4.44 and 11.11**, not 1.

**And the accounting changes with the question.** Against the beam only the fusion neutrons counted;
they are what the *reaction* makes. For the **plant**, everything the beam makes counts, because the
blanket does not know which neutron is which:

    E = E_beam + Y_fus·Q_fus + (Y_sp + Y_fus)·E(k)

| η_acc | G needed | k with the muon channel | k without | margin |
|---|---|---|---|---|
| 0.50 | 4.44 | **0.586** | 0.645 | +0.059 |
| 0.30 | 7.41 | **0.728** | 0.772 | +0.043 |
| 0.20 | 11.11 | **0.810** | 0.842 | +0.032 |

**The loop closes, subcritically, in every case** — every k below the 0.95 an accelerator-driven system
is designed around. A plant selling three quarters of its output closes at **0.924**, which lands
almost exactly on that design point, for the same reason it exists.

**What the muon channel contributes, plainly: not the loop.** A subcritical assembly driven by
spallation alone closes it too — that is what an ADS is, and it has been proposed for decades. What the
channel adds is **24 % more source neutrons** and with them the same loop at a k lower by 0.043. The
selftest asserts the loop closes *without* the channel, on purpose: the instrument must not be able to
report the channel as necessary when the arithmetic says it is not.

**After start-up it consumes:** no electricity (the loop is closed), no tritium (bred at 1.15 per
fusion, above replacement), and fertile fuel bred in place — **not free**, and the fuel cycle is not
priced here.

## Stability — `--stability`

Two questions with opposite answers, and conflating them is the error to avoid.

**The neutronics are stable by construction.** The assembly is subcritical, so power is set by the
source rather than by a self-sustaining chain: no prompt-critical excursion is available at any k < 1,
and cutting the beam stops it. The margin a reactivity insertion would have to cross is **27,178 pcm**
where the loop only closes and **7,609 pcm** at the plant point — the latter being **1.5×** the entire
control worth of a comparable fast core. No credible insertion reaches criticality.

**The loop is not stable by construction, and that is the finding.** At the operating point its gain is
*exactly one* — that is what "closed" means — so a fixed-fraction feedback is **marginally stable**: a
perturbation neither grows nor decays and the machine walks off its point on any drift. **The loop
cannot be closed passively.** The beam must be regulated against a measured power to a setpoint, so the
loop is closed by a controller rather than by the physics. Ordinary problem, ordinary solution — but it
must be said, because "the loop closes" sounds passive and is not.

**The physics does supply the restoring term.** Power amplifies reactivity as `1/(k(1−k))` — 14.2 per
unit k at the plant point — and Doppler broadening in the fertile loading is negative, 0.005 to 0.010
in `|T dk/dT|`. That restores one percent of loop gain in **112 K**, inside an ordinary swing. Adequate,
and the right sign.

**What the muon channel does for stability:** the same loop at 0.728 instead of 0.772 — **4,339 pcm** of
extra margin and a power sensitivity lower by 1.12. That is what it is worth here.

**Unbounded: beam trips.** An ADS's characteristic problem is interruption rather than runaway. Every
trip is a thermal cycle through the assembly, and trip *rate* limits component life. No figure here
bounds it; it is a driver requirement, not a physics one.

## `--ignition` — three problems one word was hiding

There is no ignition. The device has no threshold to cross and no burning state to reach; it starts
when the beam starts. What a station needs *before* it runs is three separate things, and they are
usually run together under one word because in a tokamak they would be one thing.

**1. Electricity — solved, and a neighbour supplies it.** The drivers need 267 MW at the wall before
the plant makes any. A running station sells 1,141 MW, so **one station starts 4.36 neighbours at
once**. Ordinary: every thermal station takes house power to start. After that this one takes none at
all, for ever.

**2. Tritium — solved, and a neighbour supplies it slowly.** The station's cells need more than the
world's civil stock, so the modules are charged in stages — most from stock, the rest bred by those
already running, full power in year 3.9. A finished station breeds a successor's whole charge in
**15.0 years**.

**3. Fissile — not solved from the plant's own output, and this is the one that binds.**
`f_b = k/(ν−k)` is a **break-even** condition: it was chosen to *hold* k, not to make surplus. What
the neutron budget has left over after fission, break-even breeding, leakage and ⁶Li can go to extra
fertile capture, giving a breeding ratio of **1.233** (high leakage) to **1.538** (low) — a fissile
doubling of **35 to 136 years**, against 15 on tritium. **A fleet does not grow on its own fissile.**

It grows on a stockpile, and there is one — the same shape of answer as the fuel. **Separated civil
plutonium**: about 560 t exists, nobody has a use for it, everybody is paying to guard it, and it is
a proliferation liability by simply existing. It charges **15 to 24 stations**; the ~4,000 t in world
spent fuel would charge **104 to 173**. The first charge stays a safeguarded acquisition — what
changes is that the station *fissions* it and does not give it back, so the fleet's growth rate is
set by reprocessing capacity and by policy rather than by physics. That is a different kind of limit
and is not reported as the same one.

**Could a station start smaller and breed up?** A little, and it is recorded rather than used: the
loop still closes down to **k = 0.756**, which at first order saves 20 % of the charge and costs
**5.4×** in output while it breeds. A fifth off the charge for four fifths off the power is not a
lever.

## A note on where the fuel question is answered

Whether d-t is the only mesomolecular fuel is `window.py --fuels`, not this file — it is the same
*shape* of argument as Theorem 1's binder scan (a closed candidate set, tested in the order that
constrains) and it belongs beside it. Whether the fertile feed has a successor is
`materials.py --fertile`. Both bear on figures this file computes, and neither is restated here.

## `--routes` — the route decision, and the correction it forced

Two decisions are recorded rather than argued: **fertile is uranium**, with seawater uranium as the
replacement and thorium refused; and **fusion is no longer mandatory**, the criterion being cleaner
and more efficient.

**The correction comes first, because it reverses a comparison this file's own neighbour made.**
`environment.py --tradeoff` priced the three routes on *beam power* and found the deuterium route and
the no-channel route within 0.001 of each other. That is true and it is not the whole cost — **the
machine is not the beam power.**

For a pure spallation plant the gain is **exactly invariant in beam energy**. Yield per GeV
*deposited* is a flat material property, so `y_s = n_per_GeV·E` and

```
G = (1000E + y_s·E_k)/(1000E) = 1 + n_per_GeV·E_k/1000
```

with `E` cancelling. The scan returns **37.03 at 0.6 GeV and at 12 GeV alike**, and the selftest
asserts that numerically rather than trusting the algebra.

**So the 8 GeV is bought by pion production and by nothing else.** HARP's own columns make 3 GeV/c
1.63× dearer per pion than 8. Delete the muon channel and the driver drops to about **1 GeV** — SNS
and MYRRHA class, machines that exist — and 21 capture solenoids, 42 km of REBCO and every fuel cell
go with it.

| route | y_fus | share of source | G | over C | station T |
|---|---:|---:|---:|---:|---:|
| A  d–t | 18.12 | 7.610 % | 40.04 | 8.12 % | 33.71 kg |
| B  d–d self-tritiating | 0.28 | 0.128 % | 37.08 | 0.13 % | 0.52 kg |
| C  no muon channel | 0.00 | 0 % | 37.03 | — | 0 kg |

Driver for A and B: 8 GeV, 21 solenoids. Driver for C: ~1 GeV, none.

**Route B pays route A's machine for route C's output.** Its channel is a tenth of a percent of the
plant and needs the whole 8 GeV driver to deliver it. It is a route that makes sense only to
*demonstrate* the fusion, never for the fusion to *contribute*.

**Route C gains twice more, and neither gain is the driver.** With no tritium to breed, the whole ⁶Li
share of the neutron budget returns to fertile capture: the breeding ratio rises from 1.233 to 1.442
and the fissile doubling falls from 82–136 to **43–72 years** — easing the fleet's worst constraint by
nearly half.

**And the 8 % is not needed.** The loop requirement is 7.41; A clears it by 5.41× and C by 5.00×.
Neither is near the edge, so route A's extra gain buys margin that was already there.

On the criterion as stated — cleaner and more efficient — **route C wins and it is not close**. What
argues for route A is not efficiency and never was: it is that the fusion is the project's subject.
**The instrument does not decide that**, and its selftest asserts that it says so.

## `--driver` — the driver already bought, and the ceiling that is not computed

`--rescale` left the module count free and said nothing about the **drivers**, which come in whole
machines of `LINAC_BEAM_MW` = 20 MW. Asking what the drivers are doing turns up a **fault in the
sizing**, not an optimisation.

**The fault.** `station_beam_mw()` solves

```
net = P(G·η_th(1−dry) − 1/η_acc) − n·S/η_acc
```

for `P`, and it must be told `n` — how many drivers the answer will need — *before* it has the
answer. It was passed the default, **one**. At the ADS convention that is nearly harmless: five
drivers, four unbilled standbys, and the whole-module round-up covers them. At the adopted operating
point the beam is 2.86× larger, the station carries **twelve** drivers, and eleven unbilled standbys
are **36.7 MW electric** — more than the round-up returns.

So every re-scaled station landed **below the million households it was sized for**:

| target | modules | beam MW | drivers | installed | stranded | households |
|---|---:|---:|---:|---:|---:|---:|
| MEGAPIE, operated 2006 | 293 | 228.5 | 12 | 240 | 11.5 | 969,130 |
| SNS, operating | 164 | 229.6 | 12 | 240 | 10.4 | 973,788 |
| ESS, design | 46 | 230.0 | 12 | 240 | 10.0 | 975,546 |
| high-power study | 23 | 230.0 | 12 | 240 | 10.0 | 975,546 |

`station()` is now sized by **closing the loop** — walking up from the open-loop figure, which is a
floor and never an over-estimate, charging the drivers it builds. At the ADS convention it returns
the base station unchanged, which is why the fault went unseen. **The open-loop sizing is kept as
`station_open_loop()` rather than as a paragraph**: a finding is easier to hold than to describe, and
the selftest pins that every one of those rows was short.

**What closes the shortfall was already bought.** No target row needs a new driver — the beam is
already installed and already paid for; what it needs is **targets**, the cheap half of a module.

| target | modules | beam MW | drivers | households | new drivers |
|---|---:|---:|---:|---:|---:|
| MEGAPIE, operated 2006 | 303 | 236.3 | 12 | 1,003,404 | 0 |
| SNS, operating | 169 | 236.6 | 12 | 1,004,547 | 0 |
| ESS, design | 48 | 240.0 | 12 | 1,019,486 | 0 |
| high-power study | 24 | 240.0 | 12 | 1,019,486 | 0 |

At the ESS row **the station that meets the baseline and the station that strands no capacity are the
same station**.

**Why the stranded beam is the cheapest beam in the plant.** The standby is fixed per driver, so a
module inside installed capacity pays none of it and a module that crosses a driver boundary pays a
whole one:

| | net MW per beam MW |
|---|---:|
| average over the whole station | 4.843 |
| the module inside capacity | 5.009 |
| the module that buys a driver | 4.343 |

A factor of **1.154** between the last two. **And it is bounded**: worth exactly the 10 MW that was
stranded, and not one MW more.

**What it does not cost.** Adding source neutrons does not change `k` — `k` is composition and the
fuel salt is unchanged — so the subcritical margin stays 10,000 pcm and the always-subcritical
property is untouched. It is the one lever in this work that buys output and **spends no safety**.

## The ceiling is not computed here, and that is the finding

Net is **exactly linear** in beam at a fixed driver count — the selftest asserts the second difference
is zero — so this model will hand back more output for more beam without limit. **That is a property
of the model and not of the plant.**

The blanket is **not split** (splitting is refused separately, at 2.71× the leakage for twenty ways):

| | thermal |
|---|---:|
| the station the inventories are computed at | 3,364 MW |
| the station that meets the baseline at k = 0.900 | 4,684 MW (1.39×) |

`materials.py` takes the station whole from `station()` and derives the salt flow, the salt inventory,
the heavy-metal inventory and the drain tank **from its thermal power**; `restart.py` takes the decay
heat from the same figure. Every one of those is computed at the pre-decision station and is
**understated by 1.39×**.

**A correction this section owes.** It first read that factor as a factor on the *power density*, on
the reasoning that one unsplit blanket taking more beam must run denser. **It does not** — the
blanket's volume is not fixed either: the inventory is flow times loop transit and the flow is set by
the heat, so a bigger station holds proportionally more salt and the density does not move. What is
understated is the **inventories**. `--blanket` below is where that was found, and it bounds the
density question rather than leaving it open.

## `--current` — the driver as a machine, and the correction it forces on `--routes`

`--driver` asked what the drivers are *doing*. This asks what they **are**, and it was owed before
phase 4: a station size is not achievable if its accelerator is not.

The relation is exact and needs no model — one milliamp through one gigavolt is one megawatt:

```
P[MW] = I[mA] · E[GeV]
```

So **at fixed beam power the current is inversely proportional to the energy**. `--routes` concluded
that "the 8 GeV is bought by pion production and by nothing else"; that is incomplete. The 8 GeV also
buys a factor of **eight off the current**, and the same factor off the fractional beam loss.

**What has been built, and what has been designed** (average proton current, `P/E`):

| machine | GeV | MW | mA | status |
|---|---:|---:|---:|---|
| MYRRHA | 0.600 | 2.40 | 4.000 | DESIGN |
| ESS | 2.000 | 5.00 | 2.500 | DESIGN |
| PSI HIPA cyclotron | 0.590 | 1.40 | **2.373** | OPERATED |
| SNS after PPU | 1.300 | 2.80 | 2.154 | OPERATED |
| SNS, as built | 1.000 | 1.40 | 1.400 | OPERATED |
| LANSCE | 0.800 | 0.64 | 0.800 | OPERATED |
| J-PARC RCS | 3.000 | 1.00 | 0.333 | OPERATED |

**The two routes as accelerators**, at the adopted operating point:

| | route A (d–t) | route C (no muon channel) |
|---|---:|---:|
| driver energy | 8.0 GeV | 1.0 GeV |
| station beam | 240 MW | 275 MW |
| drivers | 12 | 14 |
| station current | 30.0 mA | 275.0 mA |
| **current per driver** | **2.50 mA** | **20.00 mA** |
| — against the operated record | 1.05× | **8.43×** |
| — against the designed record | 0.62× | **5.00×** |
| linac length, each | 2,400 m | 300 m |
| linac length, all drivers | 28.8 km | 4.2 km |
| fractional loss allowed at 1 W/m | 1.20e-4 | 1.50e-5 |
| — against SNS's 2.14e-4 | 1.79× tighter | **14.3× tighter** |

**So `--routes` is corrected on its own terms.** It calls route C's driver "SNS and MYRRHA class,
machines that exist". **That is true of the energy and false of the current.** SNS runs 1.40 mA at
1.0 GeV; a 20 MW driver at 1 GeV is **20 mA** — 8.4× the highest average proton current ever operated
and 5.0× the highest ever designed. The same driver at 8 GeV is 2.50 mA, **at** the operated record
rather than past it. The `--routes` prose and its source comment now carry the qualification.

**The beam-loss budget runs the same way, and that half is counter-intuitive.** At the 1 W/m
hands-on-maintenance rule the allowance goes with *length* and the length goes with *energy*, while
the power is fixed — so the **high-energy machine is the forgiving one**. The selftest asserts the
ratio is exactly the energy ratio rather than trusting the algebra.

**What route C actually buys is length**, and a lot of it: 4.2 km of linac against 28.8 km, a factor
of **6.9** — the saving `startcost.py` found by another route. What it costs is a machine nobody has
built at a current nobody has designed for. **The two do not cancel; they are not the same kind of
quantity.**

**What a current cap would do to the driver count:**

| cap on one driver's current | route A | route C |
|---|---:|---:|
| the operated record, 2.373 mA | 13 | **116** |
| the designed record, 4.000 mA | 8 | **69** |
| none — as designed here | 12 | 14 |

**The 20 MW driver is only buildable because of the 8 GeV.** Held to a current that has been designed
for, route A's driver count barely moves and route C's multiplies.

**And what that costs is not priced, deliberately.** `REF_STANDBY_KW` is 1,000 kW for a driver of
*unstated* size, inside a sourced band of 200–2,000 kW, and nothing here scales it with machine size.
`--driver` has just shown per-driver standby is a real cost — eleven unbilled ones were 36.7 MW
electric — so multiplying the driver count by five or by ten is a large term this file cannot compute
without inventing the scaling. **Recorded as owed, before any route is priced on its accelerator
count.**

**This file does not decide the route on it.** What it removes is the sentence that made route C's
driver sound like an ordinary order.

## `--linac` — the driver re-scaled, and the term that decides it

`--rescale` asked what sets the **module** size and found the answer was a pion target route C does
not have. `LINAC_BEAM_MW = 20.0` had never been asked the same question — it is marked ASSUMED,
*"4× ESS, and four of them"* — and `--current` showed the assumption is load-bearing.

**What proton linacs actually are:**

| machine | GeV | MW | mA | status |
|---|---:|---:|---:|---|
| PSI HIPA, CW | 0.590 | 1.40 | 2.373 | OPERATED |
| SNS, design power | 1.000 | 1.40 | 1.400 | OPERATED |
| Project X, 8 GeV upgrade | 8.000 | 4.00 | 0.500 | STUDIED |
| ESS | 2.000 | 5.00 | 2.500 | BUILDING |
| BNL HFBR SC linac | 1.000 | 10.00 | 10.000 | STUDIED |
| CW proton driver study | 2.000 | 15.00 | 7.500 | STUDIED |

The assumed 20 MW driver is **4.00×** the largest under construction, **1.33×** the largest studied
anywhere, and **5.00×** the largest ever studied at route A's own energy.

**The station built out of each class, at both ends of the standby question** — and the two ends are
the finding:

| driver MW | drivers | beam MW | standby MWe | drivers | beam MW | standby MWe |
|---:|---:|---:|---:|---:|---:|---:|
| | *standby FIXED per machine* | | | *standby SCALED with size* | | |
| 20.00 | 12 | 240.0 | 40.0 | 12 | 240.0 | 40.0 |
| 15.00 | 16 | 240.0 | 53.3 | 16 | 240.0 | 40.0 |
| 10.00 | 25 | 245.0 | 83.3 | 24 | 240.0 | 40.0 |
| 5.00 | 53 | 265.0 | 176.7 | 48 | 240.0 | 40.0 |
| 4.00 | 69 | 275.0 | 230.0 | 60 | 240.0 | 40.0 |
| **1.40** | **311** | **435.0** | **1036.7** | **172** | **240.0** | **40.1** |

Both halves are the same plant. The only difference is an assumption nobody has written down.
`REF_STANDBY_KW` is a driver's fixed cryogenic and rf load, sourced as a band for a machine of
*unstated size*, and nothing states how it scales — fixed per machine, or with the machine's size.

At a driver of the largest power ever **operated**, 1.4 MW, the standby load is **40 MW electric at
one end and 1,037 MW at the other**, against a station that nets about 1,162 MW. **The difference is
comparable to the whole output.** It also decides whether that station exists: with the load fixed
per machine, a station of operated-class drivers needs **435 MW** of beam against 240 — a factor of
**1.81**, because every driver added to carry the beam brings a load the beam must then carry. With
the load scaling, the division is free and the beam does not move at all.

**This is now the largest unpriced term in the plant**, and it was invisible while the driver size was
assumed. **What would settle it is one number from an operating machine**: the fixed cryogenic and rf
load of a superconducting proton linac, stated beside that machine's beam power — an ordinary
operating quantity at every facility in the table, not found published in usable form.

**Until it is, the driver size is not a free choice.** The design keeps its assumed 20 MW driver,
because changing it would be choosing an answer to that question rather than measuring it. The
assumption is now recorded with its consequence rather than carried silently.

## `--blanket` — the ceiling `--driver` left open, bounded

**The basis matters and is the easiest thing to get wrong.** A power density over the **core** is not
one over the whole fuel **circuit**; in the one design that publishes both they differ by two, the
fraction of the salt in the core. This plant's figure is a **circuit** figure, because `materials.py`
sizes the inventory from the loop transit and states **no core volume** — so core rows are printed for
scale and explicitly not compared.

| reference | MWth | m³ | MW/m³ | basis |
|---|---:|---:|---:|---|
| MCFR, optimised | 2,500 | 25.0 | 100.0 | CORE (not compared) |
| MSFR, whole fuel circuit | 3,000 | 18.0 | **166.7** | CIRCUIT |
| MSFR, core only | 3,000 | 9.0 | 333.3 | CORE (not compared) |
| this plant, pre-decision | 3,364 | 152.9 | **22.0** | CIRCUIT |
| this plant, baseline-meeting | 4,684 | 212.9 | **22.0** | CIRCUIT |

**The density does not move with station size.** The inventory is flow × loop transit and the flow is
set by the heat, so a bigger station holds proportionally more salt. Adding beam does not make this
plant denser — it makes it bigger. **That corrects `--driver`**, which had read the 1.39× thermal
factor as a factor on power density.

Against the one published circuit figure the headroom is **7.58×** in thermal power at equal salt.
**That is not a licence to spend it.** The headroom exists because this plant holds **45.5 litres of
salt per MW against 6.0**, and that is bought by an **assumed** 30 s loop transit. Shorten the transit
and the inventory falls and the density rises in exact proportion. **The headroom is a property of an
assumption, not of a design, and may not be quoted as margin.**

**The decay model can be checked, and this is the only place it can be.**

| | |
|---|---:|
| MSRE, published | 1.000 % of full power at 1.5 h |
| this model returns | 1.083 % — agreeing to **1.083** |

That is the Wigner–Way constants checked against a *published* molten-salt reactor figure by a route
sharing nothing with it.

**The transient is invariant in beam power.** Decay heat goes as the power and the salt mass goes as
the power, so `restart.py`'s 361 K adiabatic rise in the first hour is the same at every station size.
A bigger station does not have a worse transient — it has a bigger **duty**: 39.8 MW at 1 h
pre-decision, **55.4 MW** at the baseline-meeting station, against a sourced passive residual-heat
system's 2.36 MW. **23 of those**, so decay-heat removal is active and large — which is the size of
what `restart.py` means when it says the plant cannot be walked away from.

**What is still not computable here** — a short list now rather than an open question:

- the **core volume**, and so the core power density, which needs a geometry this work does not have;
- the **coolant velocity, pumping power and erosion limit**, which need that geometry too;
- the **structural damage limit** at the flux the blanket runs at.

None of the three is bounded by anything published, because each is a property of a design rather than
of a class.

## `--standby` — the measurement `explore.py` ordered first, made

`explore.py` ranked the driver standby the largest unpriced term in the plant and named exactly what
would settle it: *"the fixed cryogenic and rf load of a superconducting proton linac, stated beside
that machine's beam power."* It is published — **in the cryogenics literature rather than the
accelerator literature**, which is why looking for it beside a beam power did not find it.

What is published is the cryoplant's **refrigeration capacity at 2 K**; the specific power that turns
it into a wall-plug load is a standard figure. Two machines carry both.

| machine | GeV | beam MW | W at 2 K | wall plug MW | MW per MW of beam | status |
|---|---:|---:|---:|---|---|---|
| SNS | 1.0 | 1.40 | 2,500 | 2.12 – 2.82 | 1.51 – 2.02 | OPERATED |
| ESS | 2.0 | 5.00 | 3,000 | 2.54 – 3.39 | 0.51 – 0.68 | BUILDING |

**A cryoplant has two circuits and the first pass counted one.** That is a correction this section
owes itself, and it came out of a question about the shields. ESS's plant covers **3.0 kW at 2 K
*and* 10.8 kW at 40–50 K** for the thermal shields; the shield circuit was simply missing. The figures
above now carry both, with the shield scaled from ESS's in proportion to the 2 K duty — an assumption,
and a small one: the shield is a seventh of the total.

**And putting both in turns the cross-check into a measurement.** Capacity and consumption together
*determine* the plant's realised fraction of Carnot; neither alone does:

| | |
|---|---:|
| ESS states | 3.0 MW electrical |
| its two duties cost, at Carnot | 0.508 MW |
| so the plant realises | **16.9 % of Carnot** |

That lands inside the independently sourced 15–20 % band — **the corroboration the first pass thought
it already had, and now actually has**. The magnitude did not move and every conclusion below
survives; what moved is why the number is trusted.

### One candidate law is refuted outright

| | SNS → ESS | |
|---|---|---:|
| beam power | 1.40 → 5.00 MW | **×3.57** |
| standby | 2.82 → 3.39 MW | **×1.20** |

**The standby does not track beam power.** A 3.6× larger beam carries a 1.2× larger cryoplant. So
`--linac`'s **SCALED** branch — the one on which dividing the beam into more, smaller drivers was free
— **is refuted by measurement**, and the FIXED branch is the plant. The cheaper of the two readings was
the wrong one.

### What it does not settle

A load that is static heat leak goes with cryomodule **length**, and length goes with **energy**. The
two machines differ by 2 in energy and 1.20 in cryoplant — neither constant nor proportional, implying
an exponent of **0.26**. **That is not a fitted law and is not used as one**: two points determine a
one-parameter fit exactly, with no residual and therefore no evidence.

| law | standby per driver | beam MW | drivers | standby MWe |
|---|---:|---:|---:|---:|
| constant — a cryoplant is a cryoplant | 2.98 MW | 255.0 | 13 | 129.1 |
| what the two points imply | 4.29 MW | 270.0 | 14 | 200.3 |
| linear in energy | 11.92 MW | 380.0 | 19 | 754.9 |

**The exposure is now bounded at 1.49× rather than unbounded**, and the design's assumed 1.0 MW per
driver is **low** — the measured machines carry 2.5–3.0 MW at a quarter of the energy and a fraction of
the beam. The assumption is **not replaced here**: replacing it is a design change and this is a
measurement.

### And it settles the driver size — in the opposite direction to the one `--linac` expected

At the measured standby, **a station of drivers of the largest class ever operated does not close at
all**, while the assumed 20 MW driver closes at **six percent more beam**. The 20 MW driver is not a
convenience the design should apologise for — **it is a requirement**, and the plant cannot be built
out of machines that exist. That is a harder statement than `--linac` was written to make, and it is
measured rather than assumed.

### It also cuts against route A, which `--current` cut for

A cryoplant load that goes with cryomodule length goes with **energy**, and route A's driver is 8×
route C's. On current and on beam loss the 8 GeV machine was the forgiving one; on standby it is the
expensive one. **Neither result cancels the other and this file does not net them.**

## `--efficiency` — the second measurement, and it closes an escape route

`explore.py` ranked η_acc the largest genuinely **open** axis (2.00× on its own), and `--basis` made
it the escape route: not knowing k precisely was to be answered by **specifying a better
accelerator** — a purchase rather than a discovery. This is that measurement. **It does not come back
the way the design needed it to.**

### What has been measured end to end

| facility | beam MW | grid MW | grid-to-beam | machine |
|---|---:|---:|---:|---|
| ESS | 5.00 | 25.00 | **20.0 %** | pulsed 4 % duty, superconducting linac |
| PSI HIPA, minimal | 1.30 | 7.10 | **18.3 %** | CW, normal-conducting cyclotron |
| PSI HIPA, facility | 1.30 | 12.50 | **10.4 %** | the same machine, whole bill |

Two figures are published for PSI and they are not the same quantity — 18.3 % counts only the
subsystems minimally needed to make the beam; 10.4 % counts the facility's 12.5 MW bill (RF 5.3,
magnets 3.6, cooling 1.65, auxiliaries 1.95). **Both are kept**: the design's η_acc appears in a
*plant balance*, where what matters is the bill.

**Both sit at the bottom of the band this design carries, and the design assumes 0.30.** `ETA_ACC_LO`
= 0.20 is SOURCED and is essentially these machines; `ETA_ACC_HI` = 0.50 is *"the design target for a
superconducting one"* and `provenance.py` already graded it **UNANNOTATED**. **The band's low end is a
measurement and its high end is a hope.**

### The fair counter-argument, which is real

Neither machine is the machine this design wants:

- **PSI is normal-conducting** — 5.3 MW of RF for a 1.3 MW beam is mostly copper losses, and 3.6 MW of
  magnet is a cyclotron's iron. A superconducting linac has neither.
- **ESS is pulsed at 4 % duty** — 150 MW of peak RF delivers 5 MW average, so the plant is sized 25×
  its useful output and idles 96 % of the time. A CW machine is not.

### So the component model, for the machine actually wanted

| term | value | status |
|---|---|---|
| klystron | 0.63 – 0.66 | **SOURCED**, ESS's own |
| RF to beam | 0.95 | ASSUMED; cavity dissipation *is* the 2 K load, measured at 3 kW on a 5 MW beam |
| auxiliaries | 0.10 – 0.20 of RF wall plug | ASSUMED |
| cryoplant | from `--standby`, both scaling laws | SOURCED + one assumption |

**Projected grid-to-beam: 37.3 – 52.0 %.** That is **2.60× the best figure any machine has ever
returned**, and the gap is a factor of two to three this work cannot close: the model omits whatever
lies between a component sum and a facility bill, and the one facility publishing both shows that
difference is large.

### What it does to the design basis, and it is the point

| η_acc | k floor | margin at k = 0.900 | vs the model's 0.135 | |
|---:|---:|---:|---|---|
| **0.200** | 0.8385 | **0.0615** | **NOT COVERED** | every machine measured |
| 0.300 | 0.7670 | 0.1330 | NOT COVERED | the design's assumption |
| 0.516 | 0.6299 | 0.2701 | COVERED | `--basis` Requirement 2 |
| 0.500 | 0.6393 | 0.2607 | COVERED | the band's UNANNOTATED top |

**At the measured efficiency the design has less than half the margin its own model's uncertainty
needs.** That is the finding, it is unwelcome, and it is what the measurement was for.

**And it closes `--basis`'s escape route rather than opening it.** Requirement 2 still holds
arithmetically — a better accelerator does buy k margin. But the accelerator it asks for, 0.516
grid-to-beam, is **2.58× anything ever operated** and above even the projection's top end. **It is a
projection, not a purchase, and calling it a purchase was that section's error.**

**So Requirement 1 is not one of three — it is the gate.** The transport calculation on the fissile
fraction decides whether the plant exists, and no accelerator anyone has built takes that decision
away from it.
