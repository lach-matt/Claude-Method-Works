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
