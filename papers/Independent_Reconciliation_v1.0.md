# The Binder Economy Against the Recent Literature: Four Independent Results, and What They Correct

**Matthew Lach** — Independent researcher
*v1.0, 6 September 2026. Prepared with a computing collaborator under the protocols of* The Method *v1.2-8.*

*An independent application paper. It uses the lattice, carries its own abstract and its own
references, and takes no part in the main paper's subject matter. It is not a member of either live
bundle.*

> **Companion.** This paper is the reconciliation half of *Cold Fusion and the Binder Economy: A
> Closed Definition, a Unique Realisation, and the Bound That Decides It* (v1.0), referred to
> throughout as **the companion**. Section references of the form §5.9 or §10.2 are to the companion;
> §2.1 to §2.6 are sections of this paper. The two share one claims ledger.

> **Verification.** Every quantity below is carried by `papers/CLAIMS.tsv` and checked by
> `python3 tools/verify_paper.py papers/Independent_Reconciliation_v1.0.md`, which recomputes each
> derived row from the instruments, binds each cited constant to the instrument that holds it, and
> fails on any number in the prose that no ledger row carries. The prose is a translation of the
> ledger and cannot outrun it.

---

## Abstract

The companion paper adds an eighth condition to the seven that admit the muon as a cold-fusion
binder — `E_binder < Q_fus · f_work / ω_s` — and works it against measured production. This paper
tests that work against four independent results published while it was being done, and reports what
each confirms and what each corrects.

**Condition 8 is not this paper's alone.** An independent group derives the same inequality as a
Lawson-inspired cycle-closure criterion, from a rate-renewal argument rather than from a condition
count, and their conditional sticking no-go rearranges term for term into condition 8. A second
independent analysis proposes the same fission-breeding escape the companion reaches at its §5.18,
for the same reason. A third, pricing the external-field stripping route the companion's §5.21
estimates, arrives within a factor of **1.48** on the field required. Three corroborations, none of
them the companion's own.

**Three corrections follow, and two of them are the companion's.** The production figure the companion
integrates from measured cross sections, **11.13 GeV per pion**, is a thin-target measurement; an
optimised thick target is calculated at **4.69 GeV**, a factor of **2.37** the companion declines to
adopt and carries beside it. A binder-loss channel neither paper had modelled — transfer to a high-Z
contaminant — makes fuel purity better than about one part per million a condition on the procedure,
tightening linearly with density. And the companion's service-life model, run at the conditions of the
one measurement it can be checked against, returns **335.3** cycles where **150** were measured: an
over-prediction of **2.24** that every "bound case" figure inherits and no bred-fuel figure does.

**One correction runs the other way.** The stripping route the companion leaves open is now
quantified and capped: even at near-perfect post-stripping recycling it buys **1.39** in cycles,
against a collection factor of 1.64 to 3.33 and a production factor of 2.37, and it is limited by
transport of the freed binder rather than by the field. It is the smallest of the three levers and
the only one requiring a machine that does not exist.

**And the criterion inverts into a result the companion does not state**: the density each product
needs. Bred fuel breaks even **below liquid density** at every collection efficiency considered,
including the 30 percent a front end achieves today, so the companion's structural bound on density
does not bear on that route at all. Heat breaks even at **2.10** times liquid density rather than the
companion's bound-case 8.5, which the field's own diamond anvil cell already reaches.

---

## 1. What this paper is, and its relation to the lattice

The companion states a definition, seven conditions, a unique realisation, an eighth condition on net
energy, and a laboratory programme. It was written from measured cross sections and the corpus's own
protocols, and it was largely complete before the four results below were read.

This paper does the check that a claim of this kind requires: it puts the companion's spine beside
independent work on the same question, and reports agreement and disagreement without adjusting either
to fit. Its relation to the lattice is the companion's — the binder-mass window of §2 is an index
statement, and nothing here revisits it. What is at issue here is arithmetic and provenance.

**Three conventions govern the readings**, and they are the corpus's own. A finding is **recorded, not
repaired**: where the companion is wrong, this paper says so and does not silently correct it. A
**status is never flattened**: a figure this paper prefers is carried beside the companion's, never in
place of it, and each keeps its own status. And a **disagreement between two independent routes is a
refusal rather than an average** — where a source and the companion differ, neither is averaged into
the other.

**Nothing here is adopted into the companion's balances.** Every figure the companion states remains
computed from the companion's own inputs. What each independent result would do to those balances is
stated, and a reader who prefers a source's figure can apply the stated factor.

## 2. The four results

**§2.1 is not one of the four.** It is the companion's own estimate of the stripping route, moved here
because §2.6 is the independent calculation of the same thing and the two belong side by side. It is
stated first so that the comparison in §2.6 is against something the reader has already seen, rather
than against a figure quoted from elsewhere.

### 2.1 Pricing the stripping route — the companion's own estimate

The companion's §5.20 opened a route to the reactivation term and left it unquantified. This prices
what it must beat.

**The geometry is more favourable than it first appears.** The window is not the ash's slowing time.
Once the ash has stopped, the bound binder–ash ion persists until the binder decays, so an irradiating
field has of order **2.14 microseconds** rather than picoseconds. Whatever defeats this route, it is
not the space–time overlap that defeats a focused beam — which is the second reason the
companion's §5.20 no-go and
this proposal are not the same claim.

**Direct photoionisation sets the scale.** The bound state's binding is 10.9 keV, so the threshold is
**0.1137 nm**, agreeing with the 0.11 the source states. A hydrogenic photoionisation cross-section
scales as the orbital area, giving **3.68 × 10⁻²³ cm²** for this system. Then:

| to achieve | required flux | **sustained intensity** |
|---|---|---|
| a stripping rate merely matching binder decay | 1.27 × 10²⁸ /cm²/s | **2.21 × 10¹³ W/cm²** |
| stripping of 95 percent of stuck binders | 2.72 × 10²⁹ /cm²/s | 4.74 × 10¹⁴ W/cm² |

**Against what exists**: free-electron lasers reach 10¹⁸ W/cm² and beyond, but in femtosecond pulses
at duty cycles near 10⁻⁹, so the time-averaged intensity is orders lower; synchrotron beamlines are
lower still. **A sustained hard-X-ray field of 10¹³ W/cm² over a reactor fuel volume does not exist.**

**But the proposal does not rest on direct photoionisation, and that is the point of it.** Its
mechanism is resonant: driving at twice the bound binder's own eigenfrequency to excite a chaotic
instability — the analogue of microwave ionisation of a Rydberg atom — whose effective cross-section
can exceed the direct one by orders. The source demonstrates that behaviour in simulation and **does
not quantify the enhancement.**

> **So the route is unquantified, and this section states the gap it must close.** Direct
> photoionisation would need 2.21 × 10¹³ W/cm² sustained. The required resonant enhancement is whatever
> brings that within reach of a real source, and **no published figure gives it.** This paper neither
> credits the route nor dismisses it: it records what would have to be true.


### 2.2 The production target was never optimised here, and someone has optimised it

§5.1 integrated the HARP-measured pion cross sections and obtained **11.13 GeV of beam energy per
π⁻ produced**, which every balance in this paper divides by. That figure carries a caveat §5.1 stated
and this paper has not until now acted on: HARP measured a **5 percent interaction-length** target,
so its yield is *per interacting proton*, and the beam's remaining energy leaves the target with the
beam. The measurement is a measurement of production, not of a production **target**.

An independent study optimised the target. Kelly, Hart and Rose [1] ran a G4Beamline optimisation over beam species, beam energy, target material and target
geometry, and report their best configuration as a **3.61 GeV** deuteron beam on a tungsten rod
**652 mm** long and **5.1 mm** across, giving **0.77 π⁻ per beam particle**. Dividing:

> **4.69 GeV of beam energy per π⁻ produced — a factor of 2.37 below this paper's own figure.**

**This paper first attributed the difference to target thickness, and that was wrong.** The reading was
that a 652 mm tungsten rod is many interaction lengths, so secondaries produce pions from beam energy a
thin target lets escape. **The source of the companion's own production figure refuses it.** Strait et
al. measure exactly this, per interacting proton, and going from **0.05** to 2 interaction lengths
buys **0.963** at 4.1 GeV and **1.186** at 11.1 GeV. Thickness is worth between 0.87 and 1.19 — never
2.37 — and the earlier reading is withdrawn.

**What survives is the beam species, which is the axis they optimised over.** Inverting Strait's
tabulated captured-muon yield through the companion's §5.24 acceptance model recovers **0.375** π⁻ per
interacting *proton* at 4.1 GeV. Against Kelly's **0.77** per beam *deuteron* at 3.61 GeV that is a
ratio of **2.05** at comparable total beam energy — two nucleons rather than one, each carrying about
half the energy. Nothing here settles whether that ratio is real, and it is a simulation on both
sides; what has changed is that the question is now a **species** question and can be asked as one.

**And the same inversion corroborates the companion's own figure.** That 0.375 π⁻ per interacting
proton implies **10.93 GeV** per π⁻ against the companion's HARP-integrated **11.13** — an agreement
of **0.982** between two routes that share the cross sections and share neither the integration, the
acceptance convolution, nor the normalisation.

Kelly et al. also assume every π⁻ becomes a usable μ⁻, so their figure is a **perfect-collection**
cost, comparable like-for-like with §5.1's.

**What it does to the balances**, at perfect collection and on this paper's own accounting:

| balance at 4.69 GeV per π⁻ | |
|---|---|
| bred fuel, bound-case service life | **18.3** |
| bred fuel, demonstrated 150 cycles | **4.67** |
| heat, bound-case service life | **3.27** |
| work, bound-case service life | **2.46** |
| heat, demonstrated 150 cycles | 0.834 |
| work, demonstrated 150 cycles | 0.625 |

Every margin in this paper multiplies by 2.37, and the qualitative structure of §5.23 survives
unchanged: the heat form at demonstrated cycle counts is still short — 0.834 — and still needs either
the service life or the breeding credit. What changes is the size of the residual everywhere else.

**This paper does not adopt 4.69 as its figure, and the reason is a status distinction, not caution
for its own sake.** §5.1's 11.13 GeV is integrated from *measured* cross sections; 4.69 GeV is a
*simulated* target optimisation. The corpus's own rule is that a status is never flattened. So both
are carried: **11.13 GeV is this paper's spine and the conservative number, 4.69 GeV is what an
optimised target is calculated to give**, and every balance stated in §5.14 through §5.24 is a floor
in this respect as well as the others. A reader who prefers the simulated target may multiply.

**One check on the simulation, and it is a partial disagreement.** Kelly et al. report their own
energy gain as **0.65 to 0.78**, using 150 fusions and **3.9 GeV** of heat per muon. That heat figure
is 26.0 MeV per fusion — which agrees with this paper's independently derived thermal value of
26.06 MeV per fusion to better than a quarter of a percent, an agreement of two blanket accountings
that share no input. Their Q is below unity where the table above puts the same case at 0.834 and
0.625, so the disagreement is small and in the expected direction: their Q counts beam energy per
*beam particle delivered*, and this paper's counts it per pion, which are the same only if every
beam particle is used. **Their conclusion and this paper's agree: at demonstrated cycle counts, heat
alone does not close the balance.**

### 2.3 An independent review reaches the same escape, and omits the axis this paper measures

§5.18 changed the question — pricing the fusion neutron as bred fuel rather than as heat — and §5.23
showed that change is what makes the balance robust. An independent review [2] proposes the same
thing: a decoupled μCF fission-breeding hybrid, with the μCF vessel as a neutron source and a
²³⁸U blanket bred for ²³⁹Pu, on the grounds that this "avoids the stringent physical requirements of
direct μCF power generation". Two analyses that share no inputs reach the same escape from the same
constraint. **That is the strongest corroboration §5.18 has, and it is not this paper's own.**

**They also state this paper's service-life law**, at unit density: cycles per binder as
1/(λ_μ/λ_c + ω_s), which is the companion's §2 service-life law N(ω_s, φ) at φ = 1. Their unpolarised row reproduces exactly from
their own parameters — sticking **0.0045**, cycle rate **2.0 × 10⁸ s⁻¹**, giving **147.6** against
the **148** they print.

**One row does not reproduce, and it is the row that matters.** Their "fully polarised optimistic"
column prints a sticking of **0.00315** and a cycle rate of **3.0 × 10⁸ s⁻¹**, and states **292**
cycles and an energy gain of **1.03**. Their own equation on those two parameters gives **214.3**
cycles and **0.754**. The sticking that *would* give 292 at that cycle rate is **0.00191** — which is
the value in the next column, not this one. This is recorded and not repaired, and it may be that the
row's parameters and its result come from different calculations rather than that either is wrong.
But the consequence is worth stating, because that column is where their ladder first crosses unity:
**on the equation printed beside it, full polarisation alone reaches 0.754 and not 1.03.** It is the
same conclusion §5.7 and §5.15 reach by a different route — sticking improvement alone does not carry
the balance.

**The larger difference is an axis their analysis does not contain.** They take the cost of a
negative muon as **5 GeV**, stating that this "includes systematic losses from pion production,
transport, decay, and muon collection". §2.2 shows an optimised production target is calculated to
cost **4.69 GeV per pion produced**, *before any collection at all*. A figure of 5 GeV cannot be a
production cost and also carry the collection loss on top of it. Applying the companion's §5.24
calculation instead — which reproduces the built front end's own simulation to **0.982**, so it is a
computed figure and not an estimate:

| | |
|---|---|
| their Q at today's aperture, both hemispheres, no stopping window | divide by **1.64** |
| their Q at today's aperture through a 265 MeV/c stopping window | divide by **2.25** |
| their Q at today's front end as built | divide by **3.33** |

The middle row is the one a reactor would actually meet, and the companion's §5.24 shows the stopping
window is the largest term in the spread.

So their unpolarised **0.52** becomes **0.32**, and their polarised-optimistic column — recomputed at
0.754 as above — becomes **0.46**.

**And this is the point the two analyses most differ on.** Their entire improvement programme — dual
polarisation, high-density confinement, field-assisted binder recovery, resonant enhancement — buys a
factor of **5.9** in cycles per binder, from 148 to 873, and the last of those columns is explicitly
extrapolative. **The collection factor their accounting omits costs between 1.64 and 3.33.** That is
the same order as their whole programme, it applies to every column of their table at once, and no
item on their list addresses it. §5.9 specified the collector against this paper's own numbers; §2.3
is the same specification arrived at against someone else's.

**In fairness to the review, and it matters:** their table is offered as model-based projection and
says so, they name the polarisation measurement as the central experimental challenge, and their
hybrid concept is proposed as conceptual with neutronics and burnup calculations outstanding. The
disagreement here is about one input, not about their method — and on the escape itself, the two
papers agree.

### 2.4 The deciding measurement is being made, and it exposes a channel this paper had not priced

The companion's §5.10 states a protocol for the measurement that decides between the two published
stickings, and its §9
ranks it third among the things that would change the answer. It is not hypothetical. A collaboration
is running it [3]: a diamond anvil cell on the PSI muon beam, with deuterium–tritium campaigns
completed and data in analysis. Three facts from that apparatus bear directly on this paper.

**First, the disagreement §5.10 turns on is the field's own.** They give as their motivation that
"theory and experiment do not fully agree on the kinetics and yield of the process in dense DT
mixtures", which is §5.10's premise stated by an experiment rather than by an analysis. Their
detectors are neutron and electron rather than the neutron-and-X-ray pair the companion's §3.5 refusal rule
specifies, so what they measure bears on §5.10's question without being §5.10's protocol; a final
sticking determined by two simultaneous independent routes remains unmade.

**Second, §5.13's density bound survives contact with the best apparatus in the field, and that is
worth more than agreement.** Their cell holds a stable sample at **933 MPa** and up to **400 K**,
with a design ceiling of **500 K** and a sample volume of **19.2 mm³** — more than twice liquid
density, which on this paper's own relation is a molar volume of **14.2 cm³/mol**. §5.13's
bound-case density needs **3.33 cm³/mol**, which on hydrogen's equation of state is hundreds of
gigapascals. So the purpose-built instrument reaches under one gigapascal where the bound case needs
two to three orders more. **§5.13's bound is not a modelling artefact of this paper**; it is the
distance between what the analysis requires and what the field's best cell delivers, now measured
from both ends.

**Third — and this is new to this paper — there is a binder-loss channel none of §§5.11–5.20 models.**
A muon transferred from the fuel to a high-Z contaminant is captured into that nucleus and leaves the
cycle permanently. The transfer rate to oxygen is about **1 × 10¹⁰ s⁻¹** per liquid-hydrogen density
of oxygen, against a binder decay rate near 4.665 × 10⁵ s⁻¹. Scaling that to a contamination fraction
at fuel density φ and setting it equal to decay:

| density | contamination at which impurity loss equals decay |
|---|---|
| the bound case | **5.49 ppm** |
| φ = 3 | **15.6 ppm** |

and the service life at the bound case falls from **588.9** cycles pure to **575.8** at one part per
million, **480.1** at ten, and **180.4** at a hundred.

> **Fuel purity better than about one part per million is a condition on the companion's procedure §3, and it
> tightens linearly with density.** Every balance in this paper is stated for perfectly pure fuel and
> is therefore an overestimate by this factor, whatever it turns out to be.

**And it supplies a rival explanation for something §5.15 asserts.** §5.15 argues that the residual
sits on the temperature axis, which the analysis holds fixed. The experimenters note that the highest
yields ever observed are in cryogenic *solid* DT, and offer as the likely reason that those data
points had both the highest densities **and the best mixture purity**. Purity, density and temperature
are confounded in the existing record: the coldest data are also the cleanest and the densest. §5.15's
reading remains available, and so does the reading that some of what looks like a temperature effect
is a purity effect. **This paper cannot separate them and does not claim to** — which is why the companion's §9 now
carries purity as an item rather than a caution, and why the same DAC campaign, which varies
temperature and density at controlled purity, is the instrument that separates them.

### 2.5 Condition 8 has been derived independently, and it exposes an over-prediction here

Condition 8 was introduced in this paper as an addition to the seven: `E_binder < Q_fus · f_work / ω_s`.
An independent group states the same inequality [4]. Their "conditional sticking no-go condition" is
ω_eff < 1/(G·N) with N = E_cost/(η·E_use) — which rearranged is E_cost < η·E_use/ω_eff, the same
inequality with the same three factors, arrived at from a Lawson analogy rather than from a condition
count. **The spine of this paper is not idiosyncratic**, and their formulation is the better one for
diagnosis because it separates rate-limited, sticking-limited and cost-limited regimes explicitly.

**Evaluated on this paper's numbers, their boundary reproduces §5.23's conclusion.** Their reference
case uses a useful cycle energy of **20.4 MeV** against a **5 GeV** binder, giving a boundary at
**0.408 percent** effective sticking, and their historical anchors at 0.45 to 0.57 percent sit on the
forbidden side of it. Substituting this paper's own accounting:

| product, at the measured production cost | boundary on effective sticking |
|---|---|
| bred fuel | **1.31 %** |
| heat | **0.234 %** |
| work | **0.176 %** |
| heat, at today's aperture over both hemispheres | **0.143 %** |
| bred fuel, at today's front end as built | **0.394 %** |

This paper's effective sticking is 0.1487 percent. It clears the heat and work boundaries at perfect
collection, clears the bred-fuel boundary by an order of magnitude, and **fails the heat boundary once
a real collection efficiency is applied** — which is §5.23's finding restated in someone else's
coordinates.

**The same criterion inverts into a density specification, which is §5.22's mirror and is new here.**
Solving the balance for the density at which it equals one, rather than for the collection efficiency:

| product | perfect collection | §5.9 collector | today's aperture, both hemispheres | today's front end |
|---|---|---|---|---|
| bred fuel | **0.154 LHD** | **0.174** | **0.275** | **0.730** |
| heat | **2.10 LHD** | **2.89** | no density suffices | no density suffices |
| work | **6.67 LHD** | **19.2** | no density suffices | no density suffices |

Two readings, and both are sharper than anything §5.11 to §5.13 states.

**The bred-fuel route needs no compression at all.** At every collection efficiency considered —
including the 30 percent a front end achieves today — the density it requires is **below liquid
density**. §5.13's structural bound on density, and the hundreds of gigapascals behind it, do not
bear on this route in any way. **And the heat route needs 2.10 rather than the bound case's 8.5**: the
bound case was chosen as ninety percent of the sticking asymptote, not as breakeven, and breakeven is
a much weaker requirement — one that the diamond anvil cell of §2.4 already reaches at 933 MPa.

**Where "no density suffices" appears, that is their no-go and not a rounding.** The service life
saturates at 1/ω_eff = 672 cycles however dense the fuel, and the heat route at 61 percent collection
needs 700. Compression cannot buy it; only sticking or collection can.

---

**And the criterion exposes something in this paper that has to be said plainly.** Their table anchors
the historical record as **124** fusions at an effective sticking of **0.57 percent** (SIN/Crowe) and
**150** at **0.45 percent** (LAMPF/Jones). Run this paper's service-life model at Los Alamos
conditions — the same equation, at 1.2 times liquid density, with the effective sticking of
0.1487 percent this paper derives through the excited-state channel — and it returns **335.3** cycles
where **150** were measured.

> **The model over-predicts its one checkable point by a factor of 2.24.**

Run instead with the *final* sticking of 0.45 percent, without the excited-state reduction, and it
returns **166.8** — consistent with the measurement. So the reduction to 0.1487 percent is not
realised at Los Alamos conditions, and the paper has not established that it is realised anywhere.
Two readings are available and this paper does not choose between them: either the excited-state
reduction is density-dependent through the reactivation term and appears only at densities Los Alamos
did not reach — in which case the bound case is self-consistent and the historical point is not a
counter-example — or the reduction is not realised at all, in which case **every "bound case" figure in
§§5.11 to §5.24 is optimistic by about this factor.** Nothing in the corpus or the literature settles
it, and the companion's §10.2 is what would.

**This does not touch the bred-fuel result, and the asymmetry is the point.** The bred-fuel
headline figures — **1.203** at today's magnet, **1.772** with the §5.9 collector — are computed at the
**measured** 150 cycles and the sourced blanket, and use the service-life model nowhere. Every heat and
work figure at the "bound case" uses it. So the over-prediction found here weakens exactly the routes
§5.23 already identified as the fragile ones, and leaves untouched the one it identified as robust.

**One further note on where this paper sits in their coordinates.** Their cycle-strength parameter for
the SIN anchor is **424**; this paper's bound case corresponds to **4,738**, an order of magnitude
above anything measured. That is the density axis stated as they state it, and it is a fair measure of
how far the bound case is from the record — which is the second reason the companion's §10 puts the bred-fuel route,
which needs none of it, first.

### 2.6 The stripping route, priced independently, and a newer sticking calculation

§2.1 priced the resonant-stripping route and the companion's §9 ranks it last. Both judgements can now be checked
against an independent rate-network calculation of the same route [5], and the check is unusually
clean because the two analyses were built for different purposes.

**The intensity requirement agrees within a factor of one and a half.** §2.1 derived a sustained
**2.21 × 10¹³ W/cm²** from a hydrogenic photoionisation cross-section and the binder decay rate. Their
reference field — **15 keV** photons at an energy fluence of **7.2 × 10⁷ J/cm²** — is
**3.28 × 10¹³ W/cm²** if spread over one binder lifetime, a ratio of **1.48** to §2.1's figure. Two
derivations that share no method and no input agree on the scale of what this route demands. §2.1's
conclusion — that a sustained hard-X-ray field of that order over a reactor fuel volume does not
exist — is therefore not an artefact of its own crude cross-section estimate.

**But §2.1 priced the wrong bottleneck, and this is the correction.** §2.1 asked only what it costs
to *strip* the bound binder. Their rate network follows the freed binder afterwards, and finds that
stripping is not the constraint: the liberated μ⁻ must slow, be captured into a muonic atom, form
dtμ and fuse **before it escapes or decays**, and in their escape-dominated benchmark about two
thirds of stripped binders are lost before re-entering the cycle. **The route is transport-limited,
not field-limited**, and a resonant enhancement that made the stripping free would not by itself
change that.

**And it caps the prize.** Even in their optimistic benchmark, where nearly every stripped binder is
recycled, the cycle yield rises from **112.6** to **156.5** — a gain of **1.39**. Set that against
the collection factor of §2.3, which is **1.64** to **3.33**, and against §2.2's production factor
of **2.37**:

> **The stripping route is the smallest of the three available levers, and it is the only one that
> needs a machine that does not exist.** The companion's §9 ranks it last on that basis rather than
> on judgement.

**A newer calculation of the initial sticking, recorded and not adopted.** A coupled-channel few-body
solution of the (dtμ) fusion reaction [6] gives an initial sticking of **8.57 × 10⁻³** against the
0.938 percent this paper's chain is built on — a ratio of **0.914** — together with an intramolecular
fusion rate of **1.15 × 10¹² s⁻¹**. This paper does not rebuild its sticking chain on it, because that
chain runs through a measured final sticking and an excited-state channel and rebuilding it is a
separate exercise. The first-order effect, rescaling the effective sticking by that ratio, is stated
instead:

| | this paper | rescaled |
|---|---|---|
| effective sticking | 0.1487 % | **0.1359 %** |
| service life, bound case | 588.9 | **637.0** |
| heat balance, bound case, perfect collection | 1.379 | **1.492** |
| heat balance, bound case at today's aperture | 0.842 | **0.911** |

The direction is favourable and the size is modest — about nine percent in sticking, eight in service
life — and it does not change any conclusion in §5.23 or §2.5. It is recorded because a paper that
prices a binder should say when the field's best number for that binder has moved, and because it runs
the opposite way from §2.5's over-prediction, which is larger.


## 3. What the four results leave standing

Set out plainly, and in the order they bear on the companion's conclusion:

**Standing, and now corroborated from outside.** The eighth condition itself; the fission-breeding
escape; the scale of the field the stripping route demands; and the companion's blanket accounting,
whose 26.06 MeV per fusion agrees with an independent figure of 26.0 to better than a quarter of a
percent.

**Standing, and strengthened.** The bred-fuel route. Its headline figures use the measured cycle
count and a sourced blanket, so they are untouched by §2.5's over-prediction; §2.5's density
specification then shows the route needs no compression at all; and §2.2's production factor, if a
reader adopts it, multiplies it by 2.37.

**Weakened, and by how much is stated.** Every companion figure computed at a modelled "bound case"
service life, by a factor of **2.24** if §2.5's second reading is right and by nothing if its first
is. Every balance in both papers, by an unquantified purity factor (§2.4). And the companion's §5.15,
whose temperature reading now has a rival purity reading it cannot be separated from.

**Closed, and it was open.** The stripping route, capped at **1.39** and limited by transport (§2.6).

**Unchanged.** The companion's §5.7 — the binder is not the variable — and its §5.16 — the conversion
ceiling descends from condition 1. Nothing in the four results bears on either.

## References

1. R. Spencer Kelly, L. J. F. Hart and S. J. Rose, *An investigation of efficient muon production for
   use in muon catalyzed fusion*, J. Phys. Energy **3**, 035003.
2. X. Yin, W. Kou and X. Chen, *Muon-Catalyzed Nuclear Fusion: Physical Mechanism, Bottleneck
   Breakthroughs, and an Engineering Pathway*, arXiv:2605.26432 — Table I and §IV.B.
3. E. Koukina *et al.* (MuFusE Collaboration), *Design and Commissioning of a Deuterium-Tritium Gas
   Delivery System for Muon Catalyzed Fusion in a Diamond Anvil Cell*, arXiv:2606.19304; and
   J. D. Kalow *et al.*, arXiv:2606.05333.
4. W. Kou and X. Chen, *A Lawson-inspired Cycle-Closure Criterion for Deuterium--Tritium
   Muon-Catalyzed Fusion*, arXiv:2607.10989 — Eqs. (11)–(13) and Table I.
5. W. Kou and X. Chen, *External-Field-Assisted Muon Reactivation in Muon-Catalyzed Fusion: A
   Rate-Network Criterion for Reducing Alpha Sticking*, arXiv:2606.07077.
6. M. Kamimura, Y. Kino and T. Yamashita, *Comprehensive study of muon-catalyzed nuclear reaction
   processes in the dtμ molecule*, Phys. Rev. C **107**, 034607 (2023).
7. M. Lach, *Cold Fusion and the Binder Economy: A Closed Definition, a Unique Realisation, and the
   Bound That Decides It*, v1.0 — the companion paper.
8. M. Lach, *The Method* v1.2-8 — *The Lach Cylinder: an index of transitions*.
