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

## What it refuses

**It does not compare the configuration against spending the same beam on a spallation-driven
subcritical system.** That is the deciding comparison for a builder, no number in this repository
settles it, and it is measurable on one apparatus because it is the same beam and the same blanket
with the fuel cell in and out. §11 of the consolidated paper records it as unmade.

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
