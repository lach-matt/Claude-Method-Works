# Paper register — what goes in, and what it rests on

Every row is a claim this project would defend in print. Each names the instrument that produces it,
whether it is **new**, whether it **corrects** something in the literature, and what would falsify it.
Nothing enters this file that an instrument does not compute.

Status vocabulary follows the corpus: `PROVEN` (closed-form and verified), `MEASURED` (computed from
data or a seated member), `CONDITIONAL` (holds under a stated assumption), `PROPOSED` (an experiment
or a design, not a result).

---

## ⚠ WITHDRAWN — H1 and H2, and the withdrawal is itself a claim

**H1 and H2 below were flagged for the abstract and are now WITHDRAWN.** `anec.py` asked the
prediction's named instrument, QNEC, and the answer runs the other way. They are kept in place, struck
through, because a register that quietly deletes its errors is not a register.

> **The error, precisely.** SNEC must hold for **every** sampling function. `nullbound.py` evaluated it
> at **one** width — the wall thickness — which is the width at which the bound is loosest. The
> right-hand side falls as 1/w² while the left falls only as 1/w once w exceeds the wall, so SNEC is
> **violated for every sampling width above ≈ 0.93 bubble radii**. One width is not a scan, and I chose
> the flattering one.
>
> **And QNEC settles it.** `⟨T_kk⟩ ≥ (ℏ/2π)S″` integrates along a complete generator to
> `∫⟨T_kk⟩dλ ≥ 0` — ANEC — because the boundary entropy variation vanishes for a localised bubble.
> Measured: `∫T_kk dx` is **negative on every ray**, −0.081 to −0.344. **ANEC is violated, so QNEC
> forbids the configuration.** And QNEC is a *theorem* in QFT, where SNEC is a conjecture — the
> instrument that closes this is stronger than the one that appeared to open it.

**H1′ (what survives, and it is worth stating).** Fewster & Roman stands: there are **no** quantum
inequalities along null geodesics in 4D. Pfenning & Ford's bound really is a **timelike** instrument,
and its bound on the *wall thickness* really is an artefact of that. The 1/D² cancellation is real
arithmetic. **So the thickness genuinely does drop out — into prohibition rather than permission.** The
10⁶² kg figure was the wrong statement of the problem; the right statement does not involve D at all.

| | `anec.py` |
|---|---|
| status | **PROVEN** (numerically, on typefour.py's validated stress tensor) |
| new? | the withdrawal and H1′, yes |
| falsified by | an error in the Einstein-tensor pipeline, which is validated against a closed form to 10⁻⁶ |

---

## ~~★ HEADLINE — flagged for the abstract~~ *(WITHDRAWN, see above)*

**~~H1. The standing objection to warp drives is an artefact of the wrong instrument.~~**

> The 10⁶²–10⁶⁵ kg figure comes from bounding the bubble wall thickness with a **timelike** quantum
> inequality (Pfenning & Ford 1997). The quantity being bounded is **null**. In four dimensions there
> is no null quantum inequality at all — Fewster & Roman 2003 show null-smeared averages of the
> null-contracted stress tensor are unbounded below on Hadamard states. On the null-smeared condition
> that does apply (SNEC), the wall thickness **cancels exactly**: both the required density and the
> permitted bound go as `1/(G D²)`, so `D²` and `G` both drop out and the comparison reduces to the
> pure number `v_s²/(288πB) = v_s²/9`. What is bounded is **velocity, not thickness.**

| | `nullbound.py` |
|---|---|
| status | **CONDITIONAL** — on the SNEC, and on four named O(1) exposures |
| new? | yes, so far as the search found |
| corrects | Pfenning & Ford 1997, and every citation of the 10⁶² figure |
| verification | ratio constant to 12 figures across D from 1 mm to ℓ_Planck — 32 orders |
| falsified by | a valid null QI in 4D; or a demonstration that E and T_kk differ parametrically rather than by O(1) |

**~~H2. The consequence: the requirement changes category, not merely magnitude.~~** *(WITHDRAWN —
the design equation is correct arithmetic and is not a licence; the configuration is forbidden at any
budget.)*

> `M = −β²c²R/(12G)` at the thickest admissible wall. R = 100 m at 0.1 c costs **18.8 Earth masses**
> against Pfenning–Ford's **1.5 × 10⁹ observable universes** — a factor 2 × 10³⁶. The remaining gap to
> a laboratory negative-energy source is 2.3 × 10⁴², which is large **and has no theorem in it.**

| | `designpoint.py`, `warpenergy.py` |
|---|---|
| status | **CONDITIONAL** on H1 |
| new? | the design equation, yes |
| falsified by | H1 failing; or a flatness requirement stricter than σR ≈ 3 |

## ★ HEADLINE — flagged for the abstract

**H3. The objection to warp drives is *kind*, not *amount* — and there are two of them.**

> The Alcubierre stress-energy is **Hawking–Ellis Type IV** throughout the wall — a complex eigenvalue
> pair, meaning **no observer anywhere has a rest frame for it**. Measured at 7/7 points with
> `|Im|/‖T‖` from 0.14 to 0.69, stable to six figures across a 4× change in step size, on a pipeline
> validated twice (vacuum → 10⁻⁶ noise floor; reproduces BBV Eq (3.48) to 10⁻⁶). **Every energy
> condition — NEC, WEC, DEC, ANEC, QI, SNEC, QNEC — bounds a *contraction* of T_μν. Type IV is a
> statement about its *eigenvectors*. H1 cannot touch it, and neither can any successor to H1.**
>
> **And it is not alone.** `anec.py` adds a second obstruction of exactly the same character: ANEC is
> violated on every ray, and both objections are **independent of the wall thickness and of the energy
> budget entirely.** Neither is a statement about how much.
>
> This splits the field cleanly and it is the paper's real contribution to the state of the question:
>
> | | budget | matter |
> |---|---|---|
> | **Alcubierre class** | tractable (18.8 M⊕) | **Type IV — unknown to physics** |
> | **warpshell** | tractable | Type I, dominant-energy | *but ℓ≥2 unstable while self-gravitating* |
>
> **Neither architecture has both, and the two obstructions are unrelated.**

| | `typefour.py` |
|---|---|
| status | **PROVEN** (numerically, doubly validated) |
| new? | the independent computation, yes; the classification agrees with Le's Table 1 |
| falsified by | a Type IV matter model; or an error in the Einstein-tensor pipeline, which is checked against a closed form |
| **not** claimed | that Type IV is *impossible*. It is **unknown** — a weaker and honest statement. Hawking–Ellis is a taxonomy, not a law. |

---

## ★ HEADLINE — flagged for the abstract

**H4. Type IV matter is not hypothetical: it sources a metric, and the solution is an evaporating
black hole.**

> H3's objection has a standing rebuttal in the literature — *"nothing known is Type IV, and in any
> case Martín-Moruno & Visser show back-reaction forces Type I."* **That rebuttal is false as stated.**
> Abdolrahimi, Page & Tzounis (*Phys. Rev. D* **100**, 124038; arXiv:1607.05280) put the Unruh-state
> `⟨T_μν⟩` on the right-hand side of `G_μν = 8π⟨T_μν⟩`, solve for the metric, and find the result is
> **Hawking–Ellis Type IV everywhere outside the horizon** of a slowly evaporating Schwarzschild hole.
> Their words: *"there are no observers anywhere outside that see zero energy flux."*
>
> MMV's four Type-I-forced cases do not apply, and they fail for the **same structural reason** the
> warp bubble escapes them: an evaporating hole is not static, its horizon is not Killing, the outgoing
> flux breaks circularity, and it is not homogeneous. `universal.py` already established that the
> bubble is non-circular because `g_tx` flips under `(t,φ)→(−t,−φ)` while `x` does not; the hole's flux
> breaks it the same way.
>
> **The magnitude is available.** APT's scaling is exact — at fixed `z = 2m/r` the orthonormal
> components go as `μ⁻⁴`, with the flux component in closed form `f(z) = αz²/(16π(1−z))`,
> `α = 3.7474×10⁻⁵`. Against `warpenergy.py`'s requirement `ρ = β²/(144πD²)` at the flatness-limited
> wall `D = R/3`:
>
> | bubble | needs the Type IV strength of |
> |---|---|
> | R = 1 m, β = 0.1 | a **1.126×10⁹ kg** black hole |
> | R = 1 m, β = 0.01 | a 3.562×10⁹ kg black hole |
> | R = 100 m, β = 0.1 | a 1.126×10¹⁰ kg black hole |
>
> Those are **primordial-black-hole masses**, and the match scales only as `R^{1/2}`. If Hawking
> radiation is real, matter of this type and this strength occurs in nature as a matter of course.

| | `selfconsistent.py` |
|---|---|
| status | **PROVEN at first order in ℏ** — every figure computed from APT's own closed forms |
| new? | the *juxtaposition* is: APT classify, `warpenergy.py` prices, and nobody has put the two side by side |
| falsified by | an exact self-consistent calculation that turns out Type I; or the disputed `k₃` term settling the spin-1 case negative |
| **not** claimed | four things, and the list is the point — see below |

**The scope, drawn deliberately tight** (encoded as `selfconsistent.SCOPE`, asserted by its selftest):

1. **First order in ℏ, not exact.** APT compute `⟨T⟩` on the *unperturbed* Schwarzschild background and
   use it to source the perturbation; they do not iterate to a fixed point. MMV's theorems are about
   **exact** solutions. Neither refutes the other. **Answered at first order; open at exact order.**
2. **Conformally coupled massless scalar.** For spin 1 APT are explicit that they are *"not certain"* —
   Type IV only for `z < 0.044`, and possibly nowhere if the disputed `k₃` term vanishes.
3. **Configuration is not matched.** The hole's Type IV is a spherically symmetric **radial** flux; the
   bubble needs a **twisted**, non-circular one. Same type, same strength, different shape. **A
   magnitude match is not a construction**, and nothing here arranges one into the other.
4. **ANEC is untouched.** It is the second obstruction and it is independent.

---

## ★ HEADLINE — flagged for the abstract

**H5. ANEC violation *protects* achronality, so the one escape from the achronal ANEC is
structurally unavailable.**

> The theorem that forbids warp drives is Graham–Olum's **achronal** ANEC, and it has two hypotheses:
> a negative null-energy integral **and** an achronal geodesic. The first is an **analysis** statement
> and returns a magnitude; the second is an **order** statement — achronality is an *antichain*
> condition on the chronology relation. We had run only the first.
>
> Run properly, the order operator is the Raychaudhuri equation with the `θ²` absorbed:
> `u″ = −4πT_kk·u`, `u(0)=0`, `u′(0)=1`, a conjugate point being the next zero of `u`. Along **true
> null geodesics** of the metric (RK4, `g(k,k)` held below 10⁻⁶), scanning impact parameter at
> `v_s = 0.3`, `0.5` and `0.8 c`:
>
> **25 ANEC-violating rays. Zero with a conjugate point. Every one of them achronal.**
>
> And the anti-correlation is not a coincidence — it is the equation itself. **Where `T_kk < 0` the
> Jacobi equation is defocusing**, so `u` is convex and is pushed *away* from the zero a conjugate
> point requires. The very quantity that violates ANEC is the quantity that protects achronality.
> **You cannot buy one with the other.**
>
> **Lemma (exact).** If `T_kk ≤ 0` along a null geodesic it has no conjugate point, hence is achronal.
> *Proof.* `u″ = −4πT_kk·u ≥ 0` wherever `u ≥ 0`; with `u(0)=0`, `u′(0)=1`, `u` is positive and convex,
> so `u′ ≥ 1` and `u ≥ λ > 0`. No zero. ∎ This is the whole story for `y ≲ 0.3`, where `T_kk ≤ 0`
> throughout. Further out the rays cross **both** signs (`T_kk` reaches `+0.24` while the integral is
> still `−0.14`), and there the result is **measured, not proved** — though not marginally: the exit
> slope runs `5.9` to `10.4` where a conjugate point needs it to reach `0`.

| | `achronal.py` |
|---|---|
| status | **PROVEN** where `T_kk ≤ 0`; **MEASURED** (25/25, three speeds) where the signs mix |
| new? | the anti-correlation, and its mechanism, yes. The lemma is elementary once posed. |
| falsified by | a ray family with mixed-sign `T_kk`, negative integral, and a conjugate point; the scan is over impact parameter of `+x` rays and is **not** a proof over all null geodesics |
| **not** claimed | that the bubble is forbidden. One escape is closed; see H5′. |

**H5′ (what this leaves standing, and it is sharper than what it removed).** With no configurational
dodge available, the prohibition rests **entirely** on the achronal ANEC in **4D curved** spacetime —
and that condition is **unproven**. Graham & Olum proved it in flat spacetime in 2007; the
self-consistent curved-space version has stood **nineteen years with no proof and no counterexample**.
Recorded in `WARP-DRIVE.md` §6 before this pass; **load-bearing** after it.

**A methodological finding, and it is reportable.** Register 1173 of the source corpus separates
*binary*, *language* and *logic*, and by its test `analysis` returns a **magnitude**, not a cell
decision — so an analysis statement cannot yield a prohibition alone. `anec.py`'s verdict crossed a
language boundary with the order half never run. Under the corpus's own cypher discipline
(register 1172) that is `NOT-RUN`, not `SILENT`. **The error was caught by an instrument from the
corpus, applied to this project's own bookkeeping.**

---

## ★ HEADLINE — flagged for the abstract

**H6. Transition has three parts — *travel → turn → seat* — and formalizing them excludes two things
at once.**

> Posed as a structure rather than a metaphor: **part 1** sets the conditions and must declare *both*
> endpoints at onset; **part 2** is the turning mechanism, a condition requirement that initializes
> only from a complete part 1 and **fails** when the conditions cannot reach part 3; **part 3** is the
> seating and closure. In the mathematics `achronal.py` already established, this is exactly the
> Jacobi field's two-point problem: `u″ = −q·u`, `q = 4πT_kk`, with `u(0) = 0` at departure and
> `u(L) = 0` at arrival, the **turn** being the conjugate point. Part 2's failure mode is not an added
> guard — it is what the equation does when the focusing is insufficient.
>
> **Theorem (reversal invariance of the turn).** If `u″ + qu = 0` with `u(0) = u(L) = 0`, then
> `v(x) := u(L−x)` solves `v″ + q̃v = 0` for `q̃(x) = q(L−x)` with `v(0) = v(L) = 0`. **The same pair is
> conjugate read from either end.** ∎ The operator is self-adjoint — the `θ²` absorption leaves no
> first-derivative term — so departure and arrival are interchangeable.
>
> **Measured**, by bisecting the conjugate length on true rays of the bubble: `|L_{A→B} − L_{B→A}|` of
> `1.1e-14` to `1.2e-13` on five rays, and **`0.00e+00` exactly** on a deliberately asymmetric control
> potential. The four-binary chain — turn / seats / achronal / ANEC sign — is identical at both ends on
> every ray.

**The two exclusions, which are the contribution:**

> **E1 — the turn lives in the energy-condition-*satisfying* sector.** `u″ = −4πT_kk·u` turns `u` back
> only where `T_kk > 0`; negative `T_kk` is convex and convex never returns. So part 2 succeeds only on
> rays that **satisfy** ANEC — `achronal.py`'s `DEFOCUS-PROTECTS` read the other way round. **The
> exotic sector cannot seat.** This is general: it is the sign of the Jacobi equation.
>
> **E2 — and that sector arrives late.** Coordinate time to the conjugate point against the flat light
> time between the same endpoints: `+8.9e-1`, `+7.7e-2`, `+1.3e-2`, `+2.6e-3`, `+7.1e-4` — every
> turning ray carries a **positive Shapiro delay**, which is what positive energy always gives. The
> only early rays (`−1.2e-4` at `y = 1.5`, converged to five figures across an 8× refinement) are far
> grazing rays that **never turn**.
>
> **TURN ⟹ LATE. EARLY ⟹ NO TURN.** On this metric no configuration has both.

| | `transit.py` |
|---|---|
| status | **PROVEN** (reversal theorem) + **MEASURED** (both-ends, 5/5; exclusions) |
| new? | the structure, its gating, and the both-ends measurement, yes |
| falsified by | a metric whose `T_kk` distribution gives a turn with negative delay — **E2 is measured on the Alcubierre bubble at `v_s = 0.5 c` only**; another distribution is `NOT-RUN`, never absent |
| **not** claimed | that a conjugate point transports anything. It is a **light focus** — a null congruence leaving A and reconverging at B. It carries no payload and this is not claimed. |

---

## ★ HEADLINE — flagged for the abstract

**H7. Universal seating has a closed-form condition, and the matter that meets it is ordinary.**

> With the conjugate point as the object, "what conditions seat" is a question about `q = 4πT_kk`
> alone, and two classical bounds bracket it from either side:
>
> | | condition | force |
> |---|---|---|
> | **Sturm** (sufficient) | `q ≥ m` on a contiguous length `ℓ ≥ π/√m`, i.e. **`m·ℓ² ≥ π²`** | seats **universally** |
> | **Lyapunov** (necessary) | `L·∫q⁺ > 4` | below it **nothing** seats, whatever the shape |
>
> **Sturm's condition is universal in the strict sense**: the zero occurs *inside* the focusing
> stretch, so nothing outside it can prevent the seat. Measured at exactly `m·ℓ² = π²` over five
> approach distances crossed with surrounding potentials of `0`, `−5` and `−20` — **15/15 seat**. Drop
> below and universality breaks: at Sturm `0.49` one case fails, at `0.25` seven do, and the failures
> are always **short approach plus hostile outside**.
>
> **Register 1206's three populations, run rather than assumed.** *"The Method equation partitions an
> index into three populations: interior captures, the working overlap, and exterior predictions."*
>
> | population | cells | seat |
> |---|---|---|
> | **interior capture** (`m·ℓ² ≥ π²`) | 64 | **64** |
> | **working overlap** | 84 | 75 — *and 9 do not, which is what makes it the overlap* |
> | **exterior** (Lyapunov-excluded) | 12 | **0** |
>
> **What maximizes it.** On the frontier the focusing budget is `∫q = m·ℓ = π²/ℓ`, so **the cost of a
> universal seat falls as `1/ℓ` without limit**. Long and weak beats short and strong. Same shape as
> this project's other design equations: area over thickness, and now strength over length.
>
> **And the threshold is ordinary matter.** `q = (4πG/c⁴)T_kk` gives
>
> **`T_kk ≥ πc⁴/(4Gℓ²) = 9.5053×10⁴³ / ℓ² Pa`**
>
> | `ℓ` | `T_kk` needed | vs nuclear (~10³⁵ Pa) |
> |---|---|---|
> | 1 m | 9.51×10⁴³ Pa | 9.5×10⁸ × |
> | 1 km | 9.51×10³⁷ Pa | 951 × |
> | **100 km** | **9.51×10³³ Pa** | **0.095 ×** |
> | 1000 km | 9.51×10³¹ Pa | 0.00095 × |
>
> **Positive, energy-condition-satisfying, and below nuclear density beyond ~100 km.** Matter that
> seats a conjugate point exists in nature. This is the sector `transit.py`'s exclusion 1 forced, and
> it turns out to be inhabited.

| | `seatindex.py` |
|---|---|
| status | **PROVEN** (Sturm, Lyapunov — classical) + **MEASURED** (the index, the populations, the universality scan) |
| new? | the application and the trichotomy, yes; both bounds are classical and are cited as such |
| falsified by | a Sturm-satisfying configuration that fails to seat (would contradict Sturm), or an exact universality frontier below `m·ℓ² = π²` |
| **not** claimed | **that universal seating is universal transport.** A seat is a light focus and carries no payload; and `transit.py`'s exclusion 2 stands — every turning ray arrives late. The exact frontier of universality is **`NOT-RUN`**, not absent. |

---

## ★★ HEADLINE — the paper's central result

**H8. Seating and time advance can coexist. Weyl focusing is quadratic in the source and therefore
sign-blind; the Shapiro delay is linear and therefore flips.**

> Every earlier pass in this project wrote focusing as `u″ = −(R_kk/2)u`, dropping shear on the
> grounds that `σ² ≥ 0` only helps focusing so ignoring it is conservative. **Conservative for an
> existence claim about one ray; fatal for a search.** The full statement (Gao & Wald 2000, eq. 13) is
>
> `G″/G = −½[σ_ab σ^ab + R_ab k^a k^b]`
>
> and the two terms have entirely different sign structure in the source:
>
> | term | order in source | needs positive energy? |
> |---|---|---|
> | **Ricci** `R_kk = 8πT_kk` | **linear** | **yes** |
> | **Weyl** `σ²` | **quadratic** | **no** |
>
> **Measured**, on a linearised static metric `Φ = −M/r` with the full Jacobi *matrix*
> `A″ = −T·A`, `A(0)=0`, `A′(0)=I` on a parallel-propagated screen, conjugate point at `det A = 0`:
>
> | `M` | conjugate point | `t − \|dx\|` | |
> |---|---|---|---|
> | +2.0×10⁻³ | λ = 55.17 | +5.12×10⁻² | seats, late |
> | **−2.0×10⁻³** | **λ = 56.50** | **−3.76×10⁻²** | **SEATS AND EARLY** |
>
> Both signs seat, within 2.4% of the same λ — because the focusing is quadratic. Only the arrival
> flips. Converged to four figures over a 4× refinement in step count.
>
> **And it is a window, bounded on both sides.** The arrival time is `(Shapiro, ∝M, flips)` +
> `(path lengthening, ∝M², never flips)`. Seating needs `|M|` large enough to focus inside the
> available length; advance needs it small enough that the linear term still wins. At `b = 0.3`,
> `L = 75`: no seat below ~1.5×10⁻³, late above ~1.5×10⁻², **about a decade of window between**, with
> the advance largest just under the upper edge.

**Three validations, each against a number not produced by this pipeline:**

| | check | result |
|---|---|---|
| 1 | light deflection vs `4M/b` | **0.03%** at `b = 0.2` |
| 2 | tidal matrix traceless (vacuum ⟹ pure Weyl) | `1.6×10⁻⁴`, **`h`-independent** — the metric's own `O(Φ²)` |
| 3 | antisymmetric delay vs analytic Shapiro `2M ln[(x₁+r₁)/(x₀+r₀)]` | **0.6%** |

**Why the earlier passes found nothing.** Not only the dropped shear. **The Alcubierre bubble's
focusing is Ricci-dominated** — the rays that turn are the rays crossing positive `T_kk`. So
`achronal.py`'s 25-ray result and `transit.py`'s **TURN ⟹ LATE** are correct *for that object* and say
nothing about this one. A compact source focuses through **Weyl, in vacuum**, under a different sign
rule. The results do not conflict; they concern different terms of the same equation.

**And the causal bookkeeping closes.** The early ray travels **entirely through vacuum** — `T_kk = 0`
along the whole path, so it violates ANEC nowhere — and **past its conjugate point it is not
achronal**, so Graham–Olum's hypothesis fails and the achronal ANEC does not reach it. That is exactly
the escape `achronal.py` searched for and did not find. It was not in the Alcubierre family.
Consistent with Olum (PRL **81**, 3567): advance *requires* negative energy, and this configuration
supplies it — off the payload's path.

| | `composite.py` |
|---|---|
| status | **MEASURED**, converged, three independent validations |
| new? | the sign-structure argument and the window, yes. Both focusing terms are classical. |
| falsified by | a sign error in the tidal matrix (checked traceless), or the window closing under a non-linearised metric |
| **not** claimed | five things, below — the list is long on purpose |

**Not claimed:** (1) **negative mass is assumed, not derived** — `Φ = −M/r` with `M < 0` is prescribed,
and self-consistency is only what `selfconsistent.py` establishes at first order in ℏ; (2) the field is
**linearised**, and the window's upper edge sits where the quadratic term bites, which is also where
linearisation gets questionable — its location is **indicative**; (3) the focus is **astigmatic** — the
tidal matrix is traceless, so `det A = 0` is a *line* focus, enough to break achronality but not a
point-to-point image; (4) **no payload** — this is null-geodesic optics and the timelike channel the
conjugate point opens has not been integrated; (5) **one geometry** — the two-region concentric device
is **`NOT-RUN`**; this establishes that its enabling mechanism is real, not that the device closes.

---

## ★ HEADLINE — flagged for the abstract

**H9. A classical vacuum corridor *forces* the Weyl mechanism, and it is the correct description for
any device by eighteen orders of magnitude.**

> Requiring the traversed corridor to be vacuum is not a modelling convenience — it is a constraint
> with a forced consequence. `T_kk = 0` makes Einstein's equations set `R_kk = 0`, so **Ricci focusing
> is identically zero and Weyl is the only focusing available.** The constraint therefore *selects*
> H8's sign-blind mechanism and **rules out the Alcubierre architecture outright**, which requires
> matter exactly where the rays travel. It also quarantines every energy-condition objection into a
> source region the payload never enters: along the corridor NEC, WEC, DEC and ANEC hold with equality.
>
> **"Vacuum corridor" reads two ways and they are different physics**, so both were compared rather
> than one chosen:
>
> | | | focusing available |
> |---|---|---|
> | **classical vacuum** | `T_kk = 0` exactly | **Weyl only** |
> | **quantum vacuum** | a vacuum *state*: `⟨T_kk⟩ ≠ 0`, Unruh-like, Type IV | Weyl **+ Ricci** |
>
> The comparison has a closed form, which is why it settles. For a source of mass `μ` (Planck units)
> at `z = 2m/r`, Weyl goes as `z³/8μ²` and the quantum Ricci as `8πf(z)/μ⁴` with APT's
> `f(z) = αz²/16π(1−z)`. Their ratio collapses:
>
> **`RICCI / WEYL = 4α / (z(1−z)μ²)`**
>
> — no `z³`, no `16π`, **symmetric about `z = ½`**, verified against the numerics to machine precision
> at five values of `z`. *Where* in the corridor you stand does not matter; only the mass does. Setting
> it to one gives, at its largest,
>
> **`μ_cross = 4√α = 2.4486×10⁻² M_Planck = 5.3293×10⁻¹⁰ kg`** — half a nanogram.
>
> Against `selfconsistent.py`'s matched design point of `1.1263×10⁹ kg`, that is **18.3 orders of
> magnitude.** For any device the classical vacuum corridor is correct, and not marginally.
>
> **What the quantum corridor would do where it applies**, recorded rather than pursued: its Unruh
> `⟨T_kk⟩` is **negative throughout** and grows toward the horizon, so its Ricci term **defocuses** —
> it would *hurt* the seat and *help* the lead, pushing H8's window both ways at once. Whether the
> window survives is **`NOT-RUN`**, and not worth running for a sub-nanogram device.

| | `corridor.py` |
|---|---|
| status | **PROVEN** (the closed form, exactly) + **MEASURED** (the crossover, the Unruh sign) |
| new? | the ratio's collapse and the crossover mass, yes |
| falsified by | an error in APT's `f(z)`, or a corridor geometry where the Weyl tidal scale `μ/r³` is wrong by 18 orders |
| **not** claimed | that the quantum window was re-run (it was not); the Weyl estimate is a **scale**, not an integrated focusing — good to an order of magnitude, which is all an 18-order gap needs |

**H9′ — a scope correction, and it strengthens the result.** The Unruh crossover above requires a
**horizon**: APT's `f(z)` is the Hawking flux of an evaporating black hole. A **two-region concentric
device is horizonless**, so it has no Unruh state and the 18-order number does not transfer to it. The
correct term there is boundary-induced — `ρ_cas(d) = −π²ℏc/720d⁴`, negative, scaling with the **gap**
rather than the mass. Against `seatindex.py`'s threshold the two curves go as `d⁻⁴` and `d⁻²` and cross
exactly once, at

**`d = 2.1352×10⁻³⁶ m = 0.132 Planck lengths`** — sub-Planckian, and still **57× short at `ℓ_P` itself**.

Its mass-equivalent at `ℓ_P` is `2.9834×10⁻¹⁰ kg` against the Unruh crossover's `5.3293×10⁻¹⁰ kg`:
**two unrelated quantum routes, one with a horizon and one without, agreeing within a factor of 1.79.**
The Planck-scale verdict is robust to which vacuum you invoke — a stronger statement than either
estimate alone. **Consequence: the two-region concentric device is a purely classical problem at any
engineering scale**, and `composite.py`'s validated pipeline handles it with no quantum term added.

**A normalisation caution, enforced in the file:** the *sign* of the Unruh term comes from
`universal.py` and the *magnitude* ratio from `selfconsistent.py`. Those are different normalisations;
no mixed quantity is reported.

---

## ★★ HEADLINE — the device *(the LEAD half WITHDRAWN, see H17)*

**H10. The two-region device seats with `M_ADM = 0` exactly, so the positive mass theorem has no
objection to it — and respecting the theorem is nearly free.**

> **~~and leads~~ — WITHDRAWN.** Every lead figure in this section was measured with **both endpoints
> inside the device's own shell** (`x₀ = ±150`, `R_s = 200`), where the metric is not asymptotically
> flat and `t − |dx|` is not a causal statement. Outside the shell the sign reverses at `X ≈ 277`. The
> **seating**, `M_ADM = 0`, the vacuum corridor and the shell's ordinariness are all untouched — none
> of them is a statement about arrival time. See **H17**, and `chronology.py`.

> H8's result needed a **bare negative mass**, which the positive mass theorem forbids, and a result
> that needs one is not a device. The construction that fixes it is a compact **negative core inside a
> positive shell of equal magnitude**:
>
> `Φ(r) = m/√(r²+a²) − m/max(r, R_s)`
>
> **The monopoles cancel, so `M_ADM = 0` exactly.** Measured: `Φ(1000) = −6.2×10⁻¹³` against
> `Φ(1) = +4.98×10⁻³`. No `1/r` tail, so no ADM mass, so nothing for the theorem to object to.
>
> **Newton's shell theorem does the division of labour**, and it is a theorem rather than an
> assumption: inside a spherical shell the potential is constant, so the shell contributes to `g_tt`
> — a real delay for a clock inside relative to infinity — and **nothing** to the tidal field. All the
> focusing is the core's Weyl term; the shell is pure delay.
>
> | `m` | `f = b²/4m` | conjugate | `t − \|dx\|` | relative | |
> |---|---|---|---|---|---|
> | 1.0×10⁻³ | 250 | none | −1.92×10⁻² | −6.4×10⁻⁵ | leads, no seat |
> | 3.0×10⁻³ | 83 | none | −5.40×10⁻² | −1.8×10⁻⁴ | leads, no seat |
> | **5.0×10⁻³** | 50 | **228.5** | **−8.42×10⁻²** | −2.8×10⁻⁴ | **SEATS + LEADS** |
> | **1.0×10⁻²** | 25 | **182.2** | **−1.41×10⁻¹** | −4.7×10⁻⁴ | **SEATS + LEADS** |
> | **2.0×10⁻²** | 12.5 | **165.4** | **−1.79×10⁻¹** | **−6.0×10⁻⁴** | **SEATS + LEADS** |
> | 8.0×10⁻² | 3.1 | 154.4 | +1.04 | +3.5×10⁻³ | seats, LATE |
>
> **A window of most of a decade**, and the conjugate point is converged to `228.45 ± 0.04` over a
> sixfold refinement in step count.
>
> **And it is nearly free.** The best relative lead, `−6.0×10⁻⁴`, is if anything slightly *better* than
> H8's bare mass. The reason is a design rule, not luck:
>
> **`shell delay / core advance ≈ (L/R_s) / (2 ln(L/a)) ≈ 8%`**
>
> The core's advance carries a **logarithm of its compactness** and the shell's delay does not. **Put
> the shell far and make the core small.**
>
> **One hard design constraint:** the corridor is vacuum only if the core is compact against the
> impact parameter. Tidal trace ratio `3.99×10⁻¹` at `b/a = 2` against `7.55×10⁻⁴` at `b/a = 50`. Below
> `b/a ≈ 50` the ray runs inside the core's own negative density, `R_kk` is large and negative, and
> Ricci **defocusing** fights the Weyl term in a corridor advertised as empty.

| | `concentric.py` |
|---|---|
| status | **MEASURED**, converged over a sixfold refinement, on `composite.py`'s thrice-validated pipeline |
| new? | the zero-ADM construction and the `(L/R_s)/(2 ln(L/a))` design rule, yes |
| falsified by | a strong-field treatment that closes the window — `Φ_max ≈ 0.25` at the design point is **not small**, and this is the weakest point in the result |
| **not** claimed | five things, below |

**Not claimed:** (1) **negative mass is still assumed** — `M_ADM = 0` removes the theorem's objection to
the *configuration*, not the exoticism of the core's **local** energy density; (2) **linearised weak
field**, with `Φ_max ≈ 0.25`, so the window's edges are **indicative**; (3) the focus is **astigmatic**
— a line focus, enough to break achronality, not a point-to-point image; (4) **no payload** —
null-geodesic optics throughout; (5) **no stability analysis** — a negative core inside a positive
shell is a configuration nobody has shown holds together, and `wall.py`'s history in this project is a
warning about assuming it would.

**A process finding worth recording.** The first window measured for this device was wrong: a scratch
driver silently reset the potential to its own defaults, so every "`a = 0.02`" run used `a = 0.5`. It
reported a window five times narrower and a lead two orders too small, and a draft of this claim
stated both. **Withdrawn.** The disagreement between harness and instrument is what surfaced it —
which is the argument for running the instrument rather than the sketch.

---

## ★ HEADLINE — flagged for the abstract

**H11. The shell that holds the device is ordinary matter, and it is radially stable with no pressure
response at all — because the same sign flip does it a third time.**

> With `M_ADM = 0` the Israel junction is unusually clean: interior Schwarzschild with `M_in = −m`,
> exterior **flat Minkowski**. That is the mirror of the textbook shell, and every result is the
> textbook one reversed.
>
> **The shell is ordinary matter.** `σ = (1/4πR)[√(1+2m/R) − 1] > 0` for every `m`, with a small
> tension `O((m/R)²)`:
>
> | `m/R` | `σ` | `p` | NEC | DEC |
> |---|---|---|---|---|
> | 0.01 | +7.918×10⁻⁴ | −1.950×10⁻⁶ | yes | yes |
> | 0.10 | +7.595×10⁻³ | −1.654×10⁻⁴ | yes | yes |
> | 0.50 | +3.296×10⁻² | −2.414×10⁻³ | yes | yes |
> | 2.00 | +9.836×10⁻² | −1.359×10⁻² | yes | yes |
>
> **The dominant energy condition holds at every compactness tested.** All the exoticism in the device
> is in the core; the structure holding it is not exotic at all.
>
> **And it is radially stable for free.** Validation first, since the sign is the whole claim — the
> **ordinary** shell (flat inside, mass outside), same machinery, `β² = 0`:
>
> | `M/R` | `V″(0)` | | `m/R` | `V″(0)` |
> |---|---|---|---|---|
> | 0.01 | **−3.036×10⁻²** unstable | | 0.01 | **+2.965×10⁻²** stable |
> | 0.10 | −3.424×10⁻¹ | | 0.10 | +2.700×10⁻¹ |
> | 0.20 | −8.169×10⁻¹ | | 0.50 | +1.018 |
>
> **Near mirror images.** `β²_crit` is **negative** at every compactness measured (−0.0037 to −0.132),
> so **any** non-negative stiffness — dust included — clears it. Where the textbook shell needs
> stiffness to survive, this one does not.
>
> **THIRD APPEARANCE OF ONE SIGN STRUCTURE.** The negative source focuses through Weyl without needing
> positive energy (H8); it leads instead of lagging because the Shapiro term is linear (H8); and it now
> stabilises the shell by reversing the effective potential's curvature. **One sign, three
> consequences, none of them arranged.**
>
> **The core's position is neutral, exactly.** Newton's shell theorem makes the interior field vanish
> at *every* point, so the core feels no force wherever it sits — neither stable nor unstable, and
> recorded as neither.

| | `stability.py` |
|---|---|
| status | **PROVEN** (junction conditions, closed form) + **MEASURED** (`V″`, validated against the unstable control) |
| new? | the negative-interior junction and its stability reversal, yes |
| falsified by | an `ℓ ≥ 2` instability — see below |
| **not** claimed | that the device is stable. **Radially** stable is not stable. |

**The top remaining risk, named rather than buried.** `ℓ ≥ 2` non-radial modes are **`NOT-RUN`**, and
they are **what killed the warpshell** — Pitre–Schneider–Poisson find an unstable even-parity mode for
all `ℓ ≥ 2`, all compactness, all `Γ`, on self-gravitating thin shells. Their configuration has
`M_in ≥ 0` and `M_out > 0`; ours has `M_in < 0` and `M_out = 0`, and the **radial** mode already
flipped under exactly that exchange. That is **a reason to expect, never a reason to assume.** Also
`NOT-RUN`: `ℓ = 1` (a displaced core deforming the shell), and the core's own stability, which is
deferred with the identification phase by instruction rather than by oversight.

---

## ★★ HEADLINE — the core specification

**H12. The core is Hawking–Ellis Type I, has no compactness bound, and is exotic in exactly one
respect — the sign of `ρ`.**

> **The Type IV problem does not transfer to this architecture.** It dominated the middle of this
> project. Martín-Moruno & Visser force Type I for **static** configurations, and this core is static
> and spherically symmetric. Measured directly with `typefour.py`'s classifier:
>
> | `r` | `‖T‖` | `max\|Im eig\|` | ratio | |
> |---|---|---|---|---|
> | 0.005 | 7.501×10² | 7.879×10⁻⁵ | 1.05×10⁻⁷ | **TYPE I** |
> | 0.020 | 1.347×10³ | 1.452×10⁻⁵ | 1.08×10⁻⁸ | **TYPE I** |
> | 0.050 | 4.435×10² | 8.705×10⁻⁶ | 1.96×10⁻⁸ | **TYPE I** |
>
> The core has a rest frame, an energy density and pressures, like ordinary matter.
>
> **A limit found and reported, not papered over.** `concentric.py`'s metric **cannot describe its own
> core**: `Φ_max = m/a` runs **0.25 to 1.0** across the window, and at `Φ = 1` the linearised spatial
> metric `(1−2Φ)` has flipped sign. The *corridor* is fine (`Φ ≈ 0.02` where the geodesics live); the
> core interior is not, and a density read off it misses the analytic Plummer by 667× at `r = 2a`. This
> is a real tension, not a choice of method: the vacuum corridor wants `a ≲ 0.02`, the window wants
> `m ≳ 5×10⁻³`, so `Φ_max ≥ 0.25` **everywhere in the window**. The core is intrinsically a
> strong-field object. So it is specified below from an **exact** solution.
>
> **The exact core** — interior Schwarzschild (constant density), with `ρ < 0`:
>
> **There is no Buchdahl limit.** For positive density the central pressure diverges at `R = 9M/4`.
> Here `1 − 2Mr²/R³ = 1 + 2|M|r²/R³ > 1` for every `r`: every root is real and the denominator never
> vanishes. Measured finite at compactness `2|M|/R = 8378`. **Negative mass has no compactness bound —
> exactly what a core needing `b/a ≳ 50` requires.**
>
> **The pressure is positive and capped at `|ρ|/3`.**
>
> | `2\|M\|/R` | `p(0)/\|ρ\|` |
> |---|---|
> | 0.084 | 0.0193 |
> | 8.378 | 0.2519 |
> | 83.78 | 0.3083 |
> | 8378 | 0.3309 → **1/3** |
>
> Monotone, approaching the **radiation value from below**, never exceeding it.
>
> **And so the exoticism is exactly one sign.** All four energy conditions fail, and all fail for the
> same single reason: `ρ < 0`. **Flip that sign and the material satisfies DEC.** The pressures are
> ordinary — isotropic, positive, bounded by radiation's.

**The identification target, as narrowly as this project can state it:**

> **A static, spherically symmetric, *isotropic* Hawking–Ellis Type I fluid with negative energy
> density and positive pressure not exceeding `|ρ|/3`.** No rest-frame pathology, no anisotropy, no
> pressure beyond radiation's, and no compactness bound.

| | `core.py` |
|---|---|
| status | **PROVEN** (exact interior solution, closed form) + **MEASURED** (the Type I classification) |
| new? | the negative-density interior Schwarzschild and its three properties, yes |
| falsified by | an anisotropy requirement, or a realistic EOS that cannot reach `p ≈ |ρ|/3` |
| **not** claimed | four things, below |

**Not claimed:** (1) **constant density is incompressible**, so its sound speed is formally infinite —
the known pathology of the constant-density star, positive or negative. **This is a bounding model,
not an equation of state**; (2) **no candidate material is proposed** — this says what the core must
*do*, not what it *is*, per the identification phase running separately; (3) the `ℓ ≥ 2` boundary
condition is now **posable but not posed**; (4) whether a negative-density fluid is stable *as a
fluid* — its own internal modes — is untouched.

---

## ⚠ THE HARD RESULT — and it belongs in the abstract

**H13. There is no achievable core. Every known source of negative energy density obeys
`|ρ| ≲ ℏc/L⁴`, and the core needs 65 orders of magnitude more.**

> **The census of real negative energy density** — Casimir (measured), squeezed vacuum (measured,
> LIGO uses it), dynamical Casimir (measured, Wilson 2011), Hawking/Unruh flux (analogue-measured),
> vacuum polarisation (measured via the Lamb shift). **All of them obey one bound**: Ford & Roman's
> quantum inequality caps negative energy sustained over a scale `L` at `|ρ| ≲ ℏc/L⁴`. Casimir *is*
> that bound saturated, not an exception to it. This is a theorem about quantum field theory, **not a
> limit of apparatus**.
>
> | `b` | required (Pa) | available (Pa) | avail/req |
> |---|---|---|---|
> | 1 m | 1.806×10⁴⁶ | 1.976×10⁻¹⁹ | **1.09×10⁻⁶⁵** |
> | 100 km | 1.806×10³⁶ | 1.976×10⁻³⁹ | 1.09×10⁻⁷⁵ |
> | solar system | 1.806×10²² | 1.976×10⁻⁶⁷ | 1.09×10⁻⁸⁹ |
> | 1 light-year | 1.806×10¹⁴ | 1.976×10⁻⁸³ | 1.09×10⁻⁹⁷ |
>
> **And the gap widens with size, which is the part that matters.** Required falls as `1/b²`;
> available falls as `1/b⁴`. **Going bigger loses by two powers.** That closes an escape this project
> used twice — `seatindex.py`'s `1/ℓ` saving and `concentric.py`'s far shell were both "go bigger".
> Here there is no large-scale corner to retreat to.
>
> The curves cross only at a core size of **4.09 Planck lengths** — a **third independent route to the
> Planck scale**, after `corridor.py`'s Unruh crossover and its Casimir crossover, and about a
> different object. When three unrelated calculations land there, that is where the physics is.
>
> **Two things that look like exceptions and are not**, named so they are not reached for later:
> **dark energy** has negative *pressure* and *positive* energy density — the wrong sign of the wrong
> quantity; **"effective negative mass"** in BECs and metamaterials is a curvature of a *dispersion
> relation*, not `T₀₀`, and does not gravitate.

**What this does not retract.** `concentric.py`'s device remains a valid solution: `M_ADM = 0`, a
vacuum corridor, seats and leads over most of a decade, a shell of ordinary matter that is radially
stable for free, a Type I core whose exoticism is exactly one sign. **Every one of those stands.** What
is settled is that the core is **not buildable with known physics**, and that the shortfall is a
**theorem rather than a budget**.

**The honest statement of this work, in one sentence:**

> A complete, self-consistent, stability-checked warp architecture whose single unmet requirement is a
> matter type no known physics provides — with the shortfall quantified at **65 orders of magnitude**
> and shown to **widen with scale**.

**Not settled:** whether physics beyond the standard framework supplies it. That is a question this
project cannot ask, and pretending otherwise would be the failure mode every withdrawal in this tree
was about.

---

## ★★ HEADLINE — the split

**H14. A charge state supplies the *seat* and not the *lead*, and the boundary between them is exactly
the boundary between matter that satisfies the energy conditions and matter that violates them.**

> Charge is the most natural remaining escape: the Reissner–Nordström term `+Q²/r²` enters the metric
> with the **opposite sign to mass**, and electromagnetic stress-energy satisfies **every** energy
> condition — so if charge could supply what the core supplies, Ford–Roman would never apply and H13's
> 65 orders would be irrelevant.
>
> **The lead: no, and it is a theorem.** `Φ = −M/r + Q²/2r²`, so `Φ > 0` iff `r < Q²/2M`, against a
> horizon at `r₊ = M + √(M²−Q²)`:
>
> | `Q/M` | `Φ > 0` below | horizon `r₊` | hidden? |
> |---|---|---|---|
> | 0.50 | 0.125 | 1.866 | **YES** |
> | 0.90 | 0.405 | 1.436 | **YES** |
> | 1.00 (extremal) | 0.500 | 1.000 | **YES** |
>
> **The positive-potential region is inside the horizon at every charge**, and the **positive energy
> theorem for Einstein–Maxwell** (Gibbons & Hull; Witten) forces `Q ≤ M`. So no charged configuration
> anywhere has a *vacuum* region of positive potential. What charge does buy is a **reduction** of the
> delay — 25% at `r = 2M`, 10% at `5M`, 0.5% at `100M` — never a reversal.
>
> **The seat: yes, with ordinary physics.** `ρ = E²/8π > 0`, `p_r = −ρ`, `p_t = +ρ` — NEC, WEC and DEC
> all hold, so `T_kk ≥ 0` and the field contributes **Ricci** focusing, the term that needs positive
> energy and here has it. Against the universal seating threshold:
>
> | field | `u` (Pa) | seats beyond |
> |---|---|---|
> | lab superconducting 1 T | 3.979×10⁵ | 1.55×10¹⁹ m |
> | strongest pulsed ~1 kT | 3.979×10¹¹ | 1.55×10¹⁶ m |
> | pulsar 10⁸ T | 3.979×10²¹ | 1.55×10¹¹ m |
> | **magnetar 10¹¹ T** | **3.979×10²⁷** | **1.55×10⁸ m = 155,000 km** |
>
> Electric route: below the Schwinger limit from about `ℓ = 10¹⁰ m`. **Seating is not a hypothetical
> capability — nature already builds the field that does it.**

**The split, and it is M's own three-part structure:**

| | needs | status |
|---|---|---|
| **Part 2 — the turn** | `T_kk > 0` | **ACHIEVABLE** — ordinary electromagnetism |
| **Parts 1 & 3 — the lead and its closure** | `Φ > 0` | **FORBIDDEN** — `Q ≤ M` for charge, 65 orders for negative energy |

> **The device is not uniformly out of reach. Its focusing half is buildable with physics we have, and
> its advantage half is blocked by two independent theorems that agree.**
>
> **So a future physics would have to change not the ability to focus, only the sign of the potential.**
> That is a far smaller and far more specific thing to ask for than "exotic matter", and stating it
> exactly is what this pass is worth.

| | `charge.py` |
|---|---|
| status | **PROVEN** (RN algebra, closed form) + **MEASURED** (the seating fields) |
| new? | the split along the energy-condition line, and its localisation to one sign, yes |
| **not** claimed | seating figures are **orientation-averaged** — `T_kk` depends on the angle between `k` and `B`, and a full treatment is `NOT-RUN`; **no magnetar-scale apparatus is proposed** — that such a field exists in nature is not that one can be built or held; **Kerr–Newman** (charge *with* rotation) is not examined; and nothing here revises H13. |

---

## ~~★★★ HEADLINE — the specification~~ *(the `B·ℓ` invariant WITHDRAWN, see H15′)*

**~~H15. Under the correct scoping the lead is not required, the seat is achievable with ordinary matter,
and the whole specification is one invariant: `B·ℓ = 1.5456×10¹⁹ T·m`.~~**

> **WITHDRAWN in `spec.py`, twice over and independently.** The scoping half of H15 stands and is
> restated as **H15′** below; the *specification* half does not. Kept here struck rather than deleted,
> because the retraction is itself the finding.

> Every theorem that blocked this work — Olum, Ford–Roman, `Q ≤ M` — is a theorem about **beating
> light**. If the requirement is only that the transported matter exist at both ends under the same
> physics, that demand is never made, and **every blocking result is attached to a requirement that is
> no longer posed.**
>
> **What survives:** `transit.py`'s Part 1 (declare both endpoints at onset) and Part 3 (the turn lands
> on the declared arrival) are unchanged. Part 2, the turn, needs `T_kk > 0` — which is what **ordinary
> matter has**.
>
> **The design equation.** `seatindex.py`'s universal seating is `qℓ² ≥ π²` with `q = 4πT_kk`; in SI,
> `ℓ = √(πc⁴/4Gu)`; and for a magnetic field `u = B²/2μ₀` the two collapse to
>
> **`B · ℓ = √(2μ₀ · πc⁴/4G) = 1.5456×10¹⁹ T·m`**
>
> One invariant, real units, **no free parameters** — fixed by `c`, `G` and `μ₀` alone. Cross-checked
> by a route sharing no formula: `q = (4πG/c⁴)T_kk` gives `π/√q = 1.5456×10⁸ m` at `B = 10¹¹ T`, and
> the threshold formula gives the same.
>
> | field source | `B` (T) | seats beyond | |
> |---|---|---|---|
> | continuous lab magnet | 45 | 3.435×10¹⁷ m | 36 ly |
> | destructive pulsed | 1.2×10³ | 1.288×10¹⁶ m | 1.4 ly |
> | theoretical material limit | 10⁴ | 1.546×10¹⁵ m | 0.16 ly |
> | neutron star surface | 10⁸ | 1.546×10¹¹ m | |
> | **magnetar** | **10¹¹** | **1.546×10⁸ m** | **155,000 km** |
>
> **And the residual gap is engineering.** From the best human field (1200 T, destructively pulsed) to
> magnetar class is **8.3×10⁷ in field, 6.9×10¹⁵ in energy density — against no theorem.** Not
> comparable to H13's 65 orders, which was a gap against Ford–Roman that **widened** with scale. This
> one **closes** with scale: a weaker field simply seats further out along `B·ℓ = const`, and nature
> already operates at the strong end.

**What the device does:** establishes a **conjugate point at a declared range** — a null congruence
leaving A and reconverging at B — from a sustained field of ordinary matter, in a vacuum corridor,
with NEC, WEC and DEC satisfied everywhere. Universal in Sturm's sense: the zero happens *inside* the
focusing stretch, so nothing outside can prevent it. Past it the geodesic is no longer achronal, so a
timelike curve A→B exists.

**What it does not:** beat light (no lead, and Olum forbids one without negative energy); shortcut (a
conjugate point is a **focus**, not a wormhole); transport anything faster than a signal; or require
**any** exotic matter.

> **The honest description is a controlled gravitational focus at a chosen range, addressed by
> declaring both endpoints, built from fields that satisfy every energy condition.**

| | `spec.py` |
|---|---|
| status | **PROVEN** (the invariant, closed form) + **MEASURED** (cross-route agreement to 10⁻⁹) |
| new? | the collapse of the seating condition to a single `B·ℓ` invariant, yes |
| **not** claimed | what it is *useful for* — that is not a physics question and inventing an application here would be the failure mode every withdrawal in this tree was about |

**One test halted rather than completed, recorded so it is a decision.** **Kerr–Newman** — charge
*with* rotation — was begun; the Kerr–Schild metric was built and validated (`a = 0` reduces to
Schwarzschild exactly; ergosphere at `x = √(4+a²)`, matching `r = 2M`), and the **ergoregion is the one
place a positive-potential region sits outside a horizon in vacuum**. The integrator hit the ring
singularity and the test was **halted by scoping** — it was a hunt for a lead, which is no longer
required. **`NOT-RUN`, with a reason, and it is the one untested door if the lead is ever reopened.**

---

## ⚠ H15′ — what survives the withdrawal, and what replaced it

**The scoping result stands.** Every theorem that blocked this work — Olum, Ford–Roman, `Q ≤ M` — is a
theorem about **beating light**. If the requirement is only that the transported matter exist at both
ends under the same physics, that demand is never made, and every blocking result is attached to a
requirement no longer posed. `transit.py`'s Part 1 and Part 3 are unchanged; Part 2 needs `T_kk > 0`,
which is what ordinary matter has. **None of that depended on `B·ℓ`.**

**The specification does not stand, and it failed in two independent ways.**

1. **Any Sturm-seating region is inside its own Schwarzschild radius.** `spec.py`'s
   `seat_over_collapse(ℓ)` is the constant `2π²/3 = 6.579` **at every scale** — the energy density that
   seats a conjugate point over `ℓ` exceeds the collapse bound `3c⁴/8πGℓ²` by that factor, always. The
   `B·ℓ` invariant is arithmetically correct and describes **a black hole**, not a device.
2. **The magnetar figure compared a peak against a length it does not sustain.** A dipole falls as
   `(R/r)³`; the table quoted the surface field against `1.546×10⁸ m` of path. Short by **25 orders**.
   `charge.py` carried the same error and is struck there too.

**What actually seats, and it is ordinary:** cumulative weak-field lensing, `f = b²c²/4GM`, validated
against the solar gravitational focus at **547.6 AU** against the published ~550 AU. Known since 1919.

> **The honest description survives the withdrawal intact: a controlled gravitational focus at a chosen
> range, addressed by declaring both endpoints, built from fields that satisfy every energy condition.
> What is withdrawn is the claim that one number specifies it.**

| | `spec.py` |
|---|---|
| status | **WITHDRAWN** (the invariant) + **PROVEN** (the `2π²/3` obstruction that withdrew it) + **MEASURED** (solar focus to 0.4%) |
| new? | the scale-invariance of the seat-over-collapse ratio, yes |
| **not** claimed | that the scoping argument fell with the specification — it did not; that lensing is the *warp* quantity — it is not, and `transition.py` shows a lens has the **wrong sign** for proper distance |

---

## ★★ HEADLINE — space and time are one quantity

**H16. Proper distance and light time are not two things that correlate; they are one Φ read in two
exponents, and their ratio is exactly 2.**

> Measured over six source strengths spanning both signs of Φ:
>
> | m | Φ at b | space saving | time saving | ratio |
> |---|---|---|---|---|
> | −8e-2 | −8.000e-2 | −3.076e-3 | −6.222e-3 | 2.0229 |
> | −2e-2 | −2.000e-2 | −7.626e-4 | −1.529e-3 | 2.0055 |
> | −5e-3 | −5.000e-3 | −1.903e-4 | −3.808e-4 | 2.0014 |
> | +5e-3 | +4.974e-3 | +1.650e-4 | +3.297e-4 | 1.9985 |
> | +2e-2 | +1.990e-2 | +6.585e-4 | +1.313e-3 | 1.9940 |
> | +8e-2 | +7.958e-2 | +2.610e-3 | +5.159e-3 | 1.9765 |
>
> **Same sign in every case**, and the ratio is 2.000 throughout: `∫e^{−Φ}dl` against `∫e^{−2Φ}dl`. A
> configuration cannot buy one without the other, in either direction.

**And which is costlier inverts between registers — both readings are true.** Metrically **time is
cheaper by exactly two**: a fractional saving `ε` costs `Φ = ε` in space and `Φ = ε/2` in time. Causally
the ordering reverses and is severe: a spatial shortcut is not forbidden as such, a temporal
displacement is, and the **intersection** is the Morris–Thorne–Yurtsever time machine.

> **The cheap one to build is the forbidden one to use.**

**The price is paid in advance, and Gao–Jafferis–Wall pay it literally.** Their coupling breaks the
`H_L − H_R` Killing symmetry and so *"fixes the relative time coordinate between them, excluding the
possibility of having closed time-like curves."* Causal consistency bought at the moment of coupling;
what it costs is the intersection.

**Collection in transit is measured FALSE.** The same total mass spread over `N` static sources gives
1.000 / 0.976 / 0.960 / 0.954 / 0.950 of one concentrated source at `N = 1/2/5/10/50` — monotonically
**worse**, converging near 95 %. The contraction goes as `asinh(L/2b)`, so splitting the path shortens
every span. **One concentrated source wins, by the logarithm.**

| | `unified.py` |
|---|---|
| status | **MEASURED** (the ratio, both signs) + **PROVEN** (`Φ = ε` vs `Φ = ε/2`, closed form) + **MEASURED** (the chain, N to 50) |
| new? | the exponent ratio as an exact structural statement, and the register inversion, yes |
| **not** claimed | that *"deferred to seating"* is refuted — it is **`NOT-RUN`**, and paying at the destination is not well-posed here without a model of dynamical payment; that the eight device parameters correspond to Λ₈ — **same cardinality, no established correspondence**; that the metric cheapness of time is usable — the causal register forbids exactly the thing it makes cheap |

---

## ⚠ H17 — THE HARD RESULT: the advance is short-range, and that is a theorem, not a shell

**H17. In the weak field a negative Shapiro term buys time at most *logarithmically* in the baseline,
while the deflection it necessarily produces costs path length *linearly*. Log against linear has
exactly one crossing, so every configuration has a finite range beyond which it makes you late.**

> **Measured on two independent architectures.** The `M_ADM = 0` device crosses over at `X ≈ 277`
> (closed form 249.6); a **bare negative mass with no shell anywhere** crosses at `X ≈ 350` (closed form
> 324). **The same order.** The shell does not cause the failure — it moves the crossing *in*, by
> turning the logarithm into a constant.
>
> **The device's saving is baseline-independent**, measured by quadrature with no geodesic integrator
> in the way: `−3.969054e-01` at `X = 400` and the same five digits at `X = 20000`. Closed form,
> agreeing to 0.15%:
>
> **`SAVING = 4m[ln(2R_s/√(b²+a²)) − 1]`** — with no baseline in it at all.
>
> **Why the deflection survives:** a ray at `b ≪ R_s` passes wholly *inside* the shell, where a
> spherical shell has no field (Newton), and exits nearly *radially*, where a radial field cannot bend
> it back. It keeps the core's full `4m/b` and pays `4m²X/b²`.

**What it costs.** One second of saving needs `1.502e7 m` of geometric mass — **2.022e34 kg, ten
thousand solar masses** of negative mass — and buys that same one second whether the trip is a metre or
a thousand light years. Over four light years it is **7.92×10⁻⁹** of the crossing.

> **A saving that does not scale with the journey is not a faster journey.** This is the answer to
> "faster", and it is negative.

**And on time machines, the conclusion was right and the machine was wrong.** Morris–Thorne–Yurtsever
is **not** available to this device, and it fails on *structure*: MTY needs a persistent **identification
of two ends**, and `transition.py` measures the areal radius monotone at every radius — no throat, so
not two ends to identify. `transit.py`'s gate re-declares `A` and `B` every use, so nothing accumulates.

**The Everett route is open, and needs no identification** — two devices and a boost. Shoshany &
Snodgrass (arXiv:2309.10072) eq. (3.11), `u > (v₁+v₂)/(1+v₁v₂)` with both legs required superluminal,
reduces exactly to **`γ > 1/ε`** — quadratic in the advance. At `ε = 2.297×10⁻⁴` that is **γ > 4354**:
finite, and below the LHC's proton γ.

> **The device is not protected by chronology. It is protected by not working at range** — a much
> weaker kind of safety, and it should be stated as the weaker one.

| | `chronology.py` |
|---|---|
| status | **MEASURED** (saturation, both architectures) + **PROVEN** (`γ = 1/ε`, exact from eq. 3.11) + **WITHDRAWN** (H10's lead half) |
| new? | the log-against-linear crossing as a general statement about weak-field advances, yes |
| **not** claimed | that the device is CTC-safe — it is not; that the two-term crossover model is exact — it lands within 11%, and the **measured** crossover is the finding; that a bare negative mass fails this way for a *different* reason — it fails the same way, only 30% later; **Hawking's Cauchy-horizon divergence is `NOT-RUN`** (Kim–Thorne vs Hawking is unresolved in the literature) and nothing here rests on it |

---

## ⚠ H18 — a binary chain is a function, and it is the *citation* that carries the geometry

**H18. A binary chain is a map `c : {0..n−1} → {+1,−1}`; its geometry is the pushforward moment
spectrum `M_ℓ = Σᵢ c(i) z(i)^ℓ`. The two-element codomain contributes nothing geometric — cite any
code at a single point and every moment above the monopole is identically zero. What carries the
geometry is the *placement*.**

Register 1173 supplies the codomain (a cell is admitted or it is not); the chain supplies the domain;
neither is geometric without a placement. The correspondence is exact rather than a match of counts —
the failure `unified.py` caught on *eight*.

**Three consequences, each measured.**

| | |
|---|---|
| **the device is a binary cited at zero separation** | A negative core inside a positive shell *is* two signs. What it lacks is a **separation** — concentric means coincident centroids. That single fact is why it does not run away (no dipole for Bondi) **and** why it cannot be seen (no dipole radiation, `M_ADM = 0` kills the monopole). `negmass.py` reported those as two findings. **They are one finding.** |
| **the code does choose the geometry** | Thue–Morse, `c(i) = (−1)^popcount(i)` — the parity of the bits of the index and nothing else, a **pure logic citation of the binary** — suppresses every moment below ℓ at length `2^ℓ`. Asserted in **exact integer arithmetic** for k = 1..8, and shown **optimal by exhaustive search** over all `2ⁿ` codes at n = 2, 4, 8, 16 (65,536 at the top). |
| **and symmetry beats it exponentially** | Read the optimum backwards: suppression through order ℓ costs `2^ℓ` elements. A **symmetric pair kills moments 1,3,5,7,9 with two elements** where the best possible code needs **512**, and Newton's shell theorem kills the interior field outright. Symmetry and code are the two mechanisms for quieting a configuration, and symmetry is exponentially cheaper. |

**And Earnshaw closes the ℓ = 1 mode `negmass.py` opened.** The Hessian of `1/r` is traceless away
from the source, so the potential of any point sources is harmonic **whatever their signs** — negating
`m` flips `U = mφ`, and `−φ` is harmonic too — and a harmonic function has no strict minimum.
**No static configuration of point masses is stably in equilibrium: any signs, any code, any
placement.** Its one escape is the *degenerate* case, constant potential, and Newton's shell theorem
hands the device exactly that.

> **"Drift to contact" is not a defect of this design to engineer out. It is the Newtonian ceiling, and
> the device is already sitting in the only seat Earnshaw leaves.** Any restoring force must come from
> outside Newtonian statics: GR, time dependence, or a non-gravitational channel.

| | `chain.py` |
|---|---|
| status | **PROVEN** (the pushforward identity; Prouhet in exact integers; Earnshaw from the traceless Hessian) + **MEASURED** (Thue–Morse optimality, exhaustive to n = 16) |
| new? | the moment-spectrum reading of the binary chain, and the identification of the device as a binary at zero separation, yes |
| **not** claimed | that "information can only be transported as binary" — untested here, and nothing above depends on it; that binary is **necessary** — q-ary Prouhet does the same job, verified for q = 3, so binary is *minimal and sufficient*, not necessary; that the transportation code **is** a chain — what is shown is what a chain would and would not buy if it were; the **GR** version of ℓ = 1 remains `NOT-RUN` |

---

## ★★★ H19 — the rigidity clause: the exotic matter is **derived**, not assumed

**H19. The positive mass theorem's second half — `M_ADM = 0` ⟺ Minkowski — applied to a device that
has `M_ADM = 0` and is not Minkowski, proves its matter cannot satisfy the dominant energy condition.
Negative energy in this design is a theorem, not an assumption, and no magnitude enters the argument.**

Every use of the positive mass theorem in this tree read only the inequality. The rigidity clause is
the half that pays.

| | |
|---|---|
| the theorem | `M_ADM ≥ 0`, **and `M_ADM = 0` iff the spacetime is Minkowski** — under asymptotic flatness, nonsingularity, and the **DEC** |
| the device | `M_ADM = 0`, measured `−4.000e−15` (`concentric.py`), and **not** Minkowski — it seats a conjugate point and has structure at every radius |
| therefore | **its matter cannot satisfy the DEC** |

`concentric.py`'s caution 1 read *"negative mass is still assumed."* **It is not an assumption any
more** — superseded in place, along with every "the positive mass theorem has nothing to object to"
in the tree. The device satisfies the theorem's **conclusion** while necessarily violating its
**hypothesis**, and the rigidity clause is what makes the violation forced.

**Which inverts what a balance principle looks like it buys.** Balance, pushed through the theorem,
does not give a `(+E, −E)` pair — the negative member cannot exist under the DEC, because the theorem
is a **one-sided bound, not a symmetric ledger**. It gives `M_ADM = 0`, and then rigidity charges for
it:

> **The only balanced, non-trivial configuration is one that violates the dominant energy condition.
> Balance does not remove the exotic-matter bill. It is the proof that the bill is unavoidable.**

**And the pairing intuition is a real theorem about the wrong quantity.** Wheeler's *charge without
charge*: thread a wormhole with field lines and the two mouths read `+Q` and `−Q` with no charged
matter anywhere — the ledger closes exactly. But the mass that goes with a charge goes as `Q²`, so it
is **sign-blind**: the two mouths carry opposite charge and the **same positive** mass. The mass ledger
does not cancel; **it doubles**.

> **A quantity pairs `±` if and only if it is sign-symmetric.** Charge is. Energy is not, because the
> positive mass theorem commits its sign. That is `dichotomy.py`'s Weyl-against-Ricci split reached
> from a completely different direction — **two independent routes to the same discriminator.**

**Two supporting corrections.** The **emitter is the black hole** (Hawking, `1.92e−9 K` at
`detect.py`'s 32.13 M☉ target); a horizonless wormhole has no surface gravity and does not emit — the
real contrast is `detect.py`'s absorb-versus-**transmit**. And *"a tunnel with a black hole at the far
end"* is the **Einstein–Rosen bridge**, a vacuum solution needing no exotic matter, with a **white**
hole at the far end — **measured impassable**: the throat falls from `2M` to `0` between Kruskal
`T = 0` and `T = 1`, and every leftward null ray hits the singularity first because
`|1 − c²| < 1 + c²` for every `c > 0`.

| | `pair.py` |
|---|---|
| status | **PROVEN** (rigidity ⇒ DEC failure; ER non-traversability, exact; charge sign-blindness) + **MEASURED** (Hawking temperatures; 200,000-ray scan) |
| new? | the rigidity clause applied to this device — **yes, and it upgrades an assumption to a derivation** |
| **not** claimed | that the balance principle licenses a `±E` pair — it forbids one; that a closed universe's total energy is **zero** — ADM mass is a surface integral at spatial infinity, and a closed universe has none, so the quantity is **undefined**, not zero (a definitional refusal, filed as one); that the ER bridge is a route to anything — it is the solution that does *not* work; that any magnitude in the exotic-matter bill has moved — none has |

---

## ⚠ H20 — the expansion is not a permutation, and one invariant scalar says so

**H20. A permutation of a closed index is measure-preserving, so its expansion scalar
`θ = ∇_μ u^μ` is exactly zero. The universe's is `3H₀ = 6.549×10⁻¹⁸ s⁻¹`, and `θ` is
coordinate-invariant. The sharper form: `(cosmic scale)/(atomic scale)` is **dimensionless** and grew
by **1090.92** since recombination — a relabelling has no units to hide in.**

The Bohr radius is fixed by `ℏ`, `mₑ`, `e`; none contains `a`. Atoms do not expand. The ratio is read
straight off `T_rec/T₀ = 2973.3 K / 2.7255 K`, independent of any model of `a(t)`.

**What *is* a closed index here — and it is the textbook.** In FLRW a galaxy's comoving coordinate does
not change, nothing expands *into* anything (there is no embedding space), and the count is conserved
exactly: `n a³ = const`, measured to `2.2e−16` across a factor of 20 in `a`. All the change sits in one
function.

| claim | verdict | why |
|---|---|---|
| space is a closed index | **stands** | comoving coordinates do not move; `n a³` conserved |
| the expansion is a permutation | **falsified** | `θ = 3H₀ ≠ 0`, and `θ` is invariant |
| it is a structural relaxation | **splits** | the expansion is isentropic; the **rearrangement** relaxes |
| self-referencing, self-defending | **exact** | the contracted Bianchi identity |
| no defect possible in a closed index | **true for charge** | Gauss forces total `Q = 0` exactly |

**"Relaxation" is the right word for the wrong term.** FLRW expansion is isentropic — `d(ρa³) = −p d(a³)`
exactly, verified for radiation, dust, vacuum and a curvature-like fluid — so nothing dissipates. But
the early universe had near-zero Weyl curvature (Penrose), so gravitational clumping *does* raise
entropy: **structure formation genuinely is a relaxation, running inside an expansion that is not one.**

**"Self-defending" is exact, and it is the contracted Bianchi identity.** `∇_μ G^{μν} ≡ 0` holds for
*every* metric with no field equation assumed, and coupling it to Einstein's equation **forces**
`∇_μ T^{μν} = 0` — you cannot write down a source that violates conservation. Measured: integrate the
Friedmann constraint and the acceleration equation, **never impose continuity**, and continuity holds
at `1e−16` for four fluids at three curvatures. **And the residual does not fall with step size** — flat
from 500 to 8,000 steps. A truncation error shrinks; an identity is already exact. *The flatness is the
evidence.*

**And a closed index constrains exactly one quantity — the same one again.** Gauss's law on a manifold
with no boundary forces **total electric charge to be exactly zero** in a spatially closed universe:
topology, not observation. No counterpart for energy (undefined there — **H19**) or baryon number (not
forced). **Third independent arrival** at the sign-blind split, after Wheeler's charge-without-charge
and Weyl-against-Ricci.

**The picture also has a real formulation.** *Unimodular gravity* fixes `det g` and varies only the
volume-preserving part — a literally closed index — and is **classically equivalent** to GR. `Λ` becomes
an integration constant rather than a Lagrangian parameter. That reframes the cosmological-constant
problem; it does not solve it, and no observation separates the theories.

| | `permute.py` |
|---|---|
| status | **PROVEN** (Bianchi as an identity, measured step-independent; isentropy; closed-universe charge) + **MEASURED** (`θ = 3H₀`; the 1090.92 ratio; `n a³` conservation) |
| new? | the step-independence test as evidence of an identity rather than a numerical result, yes |
| **not** claimed | that unimodular gravity predicts anything GR does not — it is classically equivalent, filed as **EQUIVALENT**, not better; that it solves the cosmological-constant problem; that the cube analogy fails everywhere — it is **exact on the count and absent on the scale**, and the scale is the axis we observe |

---

## ★★★ H21 — `M_ADM` is a free parameter; the **lead** is the whole cost, and the DEC branch is exhausted

**H21. Letting the shell mass float free of the core's, `M_ADM = 0`, `+5.0e−3` and `+1.5e−2` all seat
and all lead, while a positive core — ordinary matter throughout — seats and arrives *late*. `M_ADM` is
a free parameter of the design. The exotic matter is required by the **lead**, locally, whatever the ADM
mass.**

| configuration | `M_ADM` | seats | leads |
|---|---|---|---|
| the device | 0 | ✓ | ✓ |
| heavier shell | +5.0e−3 | ✓ | ✓ |
| much heavier shell | +1.5e−2 | ✓ | ✓ |
| **positive core** (ordinary matter) | +1.0e−2 | ✓ | **✗** |

**This narrows H19's own phrasing, and the narrowing matters.** H19 said the exotic matter is derived
from the design's own `M_ADM = 0`. True — and it invites a false reading: that a *bookkeeping choice*
created the requirement, so another choice could remove it. It could not. `Φ > 0` needs `ρ < 0`
pointwise, whatever the ADM mass. **Rigidity is a second, independent proof of a requirement that was
never about `M_ADM`** — it tightens nothing, and removes only the hope that bookkeeping could dodge it.
`pair.py` and `concentric.py` narrowed in place.

> **The seat is free. The lead is the whole cost.**

**And that makes the dichotomy exhaustive rather than enumerated.**

| case | verdict | by |
|---|---|---|
| `M_ADM < 0`, DEC holds | **forbidden** | positive mass theorem, the inequality |
| `M_ADM = 0`, DEC holds | **Minkowski** | positive mass theorem, the **rigidity clause** |
| `M_ADM > 0`, DEC holds | **collapse** | Sturm density exceeds it by `2π²/3` |
| DEC fails | the device | everything this tree has built |

> **Under the dominant energy condition there is no seat-and-lead** — a statement about every case,
> not about the ones somebody thought to try. It is the strongest negative result the project holds.

**One line closes five proposed routes at once.** A sign-blind quantity pairs, balances and is
constrained by closure; a sign-committed one is not; and **energy is sign-committed** by the positive
mass theorem. So balance (`pair.py`), closure and permutation (`permute.py`), entanglement symmetry
(`entsym.py`) and the binary chain's geometry (`chain.py`) all die — *not case by case*, but because the
class of quantity they act on does not include energy.

> **Exactly one proposed route survives it, which is why it is the one to push.** GJW's external causal
> path is an **order** question, not an energy question: it asks whether a non-achronal connection *may
> exist*, not what it costs. Order is the row that admits, it governs **speed**, and it is the only row
> this project has ever moved.

**Containment is a boundary now, not a risk.** Earnshaw permits no stable static configuration of point
masses whatever their signs, and its one escape — constant potential — is exactly what the shell theorem
hands the device. Neutral is optimal, so drift to contact is the **Newtonian ceiling**, and what remains
is one named `NOT-RUN` about whether GR moves it.

**What is left is three doors, and they are the only three:** **outside GR** (f(R), noncommutative
geometry — where the DEC and the positive mass theorem are not the governing theorems; scope still
unchosen); **not an energy question** (order, causal structure, chronology protection); **a relic rather
than a construction** (`create.py`'s topology theorems and `detect.py`'s search already agree).

| | `apply.py` |
|---|---|
| status | **MEASURED** (four surveys on `concentric.py`'s own machinery) + **PROVEN** (the DEC-branch exhaustion, from three named theorems) |
| new? | that `M_ADM` is free of the mechanism, and the exhaustion of the DEC branch, yes |
| **not** claimed | that anything moved — `expand.py` still reads `E = 1` with the dissent in INFORMATION alone, recomputed here and said first; that the exhaustion extends beyond GR-with-matter, which is precisely door one; that three doors means three routes — none of them is open, they are the only places left to look |

---

## ⚠ H22 — "no path needed" is the **maximum** of the cost curve, and information is not a second currency

**H22. `Δd = (G/c²)MΛ` is linear in the contraction, so making two points *one* means contracting the
whole separation: `5.1048×10⁴² kg = 2.5666×10¹² M☉` at four light years. There is no economy of scale.
The cheap-far-end intuition is inverted by the project's own equation.**

| contraction | mass |
|---|---|
| one metre | `1.3489e26 kg` |
| 1% of 4 ly | `5.1048e40 kg` |
| **all of 4 ly (coincidence)** | **`5.1048e42 kg` = `2.5666e12 M☉`** |

**But the other reading of the same sentence is not on that curve at all.** Two points *already* one is a
wormhole mouth pair — nothing is contracted, so nothing is paid for contracting. That is `create.py`'s
**find one and enlarge it**, reached here from the index picture rather than from the topology theorems.
**Two independent routes to door three.**

**Information, priced for the first time — and it is not a second currency.** The required configuration
holds `9.9736e101` bits, and the holographic (`A/4ℓ_P²`) and Bekenstein (`2πRE/ℏc`) routes **agree to six
digits** because the bound is saturated at the horizon. *That agreement is the finding.*

> Bekenstein bounds `S` **by** `E`: you cannot hold the bits without the energy to hold them in, so
> `S ≤ 2πRE/(ℏc)` runs the **wrong way** for the trade. **The bits are the mass, in other units**, and
> the conversion factor is `ℏ`.

Landauer adds that *manipulating* them at the CMB costs `2.6014e79 J` against `Mc² = 4.5880e59 J` —
**19.75 orders worse**, breaking even only at `4.8068e−20 K`. **Flagged as the weaker half**: Landauer
prices irreversible operations, and a reversible computation costs nothing in principle. The argument is
Bekenstein, which is static and survives reversibility entirely.

**"Step walking through dimensions" cannot be the mechanism, by a theorem.** Campbell–Magaard: any
analytic *n*-manifold embeds locally in an (*n*+1)-dimensional **Ricci-flat** one — always,
unconditionally. **A thing true of every spacetime distinguishes none of them.** Bulk shortcuts
(Caldwell–Langlois) *are* real and calculable — but a warped bulk is an extra-dimensional theory, which
is **H21's door one**, not a fourth door.

**And the diagnosis is the best anyone has made of this project's cost structure.** *"What makes
transition expensive is the constant movement of the index"* is `reverse.py`'s split — the seat is
**free**, the movement is all of the cost — and `warpshell.py`'s CM theorem, that momentum changes only
by radiating. `apply.py` sharpened it one pass earlier: `M_ADM` is free and **the lead is the whole
cost**.

> The tree's own answer to that diagnosis is the object that does not move: `bothways.py`'s **GATE** —
> zero offset, both directions, no CTC, and it **amortises**. A gate *is* "a point in the index where no
> path is needed." **Find one rather than build one; build a gate rather than a vehicle.**

| | `nopath.py` |
|---|---|
| status | **MEASURED** (the coincidence cost from `phase1.py`'s own rate; the bit count by two agreeing routes) + **PROVEN** (Campbell–Magaard; the Bekenstein direction) |
| new? | the information denomination priced, and the linearity argument applied to coincidence, yes |
| **not** claimed | that Landauer settles it — it prices irreversible operations only and is recorded as the weaker half; that dimensional drift is a new route — it is door one; **that any of this is the method equation.** Register 1206 is a statement about placement on an index and the transition equation is `Δd = (G/c²)MΛ`; a shared *shape* is not a correspondence, and `unified.py`'s rule on *eight* governs — none is asserted |

---

## ⚠ H23 — information rides the **spectrum**, not the charge; and the optimal spectrum is a horizon

**H23. In a spatially closed index the charge carries exactly zero bits — superselection removes the
quantum information, and Gauss's law fixes the value — so the spectrum is not the preferred carrier but
the only one left. Bekenstein's `S` counts precisely that carrier. And a spectrum is a logarithm, so the
optimal one is a black hole.**

**Two things the prediction gets right, and they are not small.**

| | |
|---|---|
| **the carrier** | Electric charge is **superselected**: no coherent superposition across total-charge sectors exists as a physical state, so the value labels a sector and carries nothing inside one. And `permute.py` already forced total `Q = 0` in a closed universe — a quantity fixed to one value carries `log₂(1) = 0` bits. **The spectrum is the only carrier left**, by a theorem this tree derived two passes ago. |
| **the variable** | `S ≤ 2πRE/(ℏc)` bounds the number of **distinguishable quantum states** of energy `E` in radius `R`. It counts **spectral multiplicity** and never mentions charge. The prediction names the bound's own variable. |

**And one thing it gets wrong, on arithmetic rather than principle.**

| hydrogenic `n_max` | states | bits |
|---|---|---|
| 10 | 385 | 8.589 |
| 100 | 338,350 | 18.368 |
| 1000 | 333,833,500 | 28.315 |

> **A spectrum is a logarithm.** Ten times the levels buys ten bits. Reaching the `9.9736e101` bits of
> **H22** takes `5.4298e100` atoms at `9.0870e73 kg`, against `5.1048e42 kg` supplied directly —
> **31.25 orders worse**; `1.0976e28` bits/kg against `1.9538e59`.

**And that gap is not a fact about hydrogen.** It is the distance from ordinary matter to the bound, and
the bound is saturated by exactly one object. Black-hole bits go as `M²` — doubling the mass quadruples
the count — so information density *rises* with mass and the optimum at every scale is a horizon.

> **"Pay in spectra", optimised, is "build a black hole"** — `dichotomy.py`'s RICCI route, closed by
> COLLAPSE. **Three denominations of one route**: mass, information and spectra are not three routes, and
> the route ends in a horizon.

**It leaves H14 standing.** A charge state supplies the **seat** and not the **lead**; a multiplicity has
no sign, and the split turns on the sign of `ρ`. Enriching a spectrum does not make an energy density
negative.

| | `spectra.py` |
|---|---|
| status | **PROVEN** (superselection; the closed-index charge count from `permute.py`; `M²` scaling and saturation) + **MEASURED** (the hydrogenic bit counts; the 31.25-order comparison) |
| new? | that the closed index leaves the spectrum as the *only* carrier, and that the optimised spectral currency is a horizon, yes |
| **not** claimed | that the refinement is wrong about the carrier — it is right, twice; that hydrogen is the best possible spectrum — it is an instance, and the bound is the general statement; that anything in **H14** moves |

---

## ★★★ H24 — the currency question closes by **exhaustion**: the conversion table has one free parameter, and it is measured

**H24. Every denomination is tied to mass-energy by a monomial in `G`, `c`, `ℏ`, `k` — or by a bound
that runs against the trade. The whole conversion table holds exactly two dimensionless numbers: `Λ`,
determined and O(10), and `κ`, the one genuine lever, already measured at `π/360` against the
`3.8281e69` needed.**

| denomination | rate | value |
|---|---|---|
| geometry | `c⁴/G` | `1.21026e44 N` |
| length | `G/c⁴` | `8.26272e-45 m/J` |
| contraction | `c²/(GΛ)` | `1.34895e26 kg/m` |
| area | `ℏG/c³` | `2.61228e-70 m²` |
| information | `2π/(ℏc ln2)` | `2.86720e26 bits/(J·m)` |
| heat | `k ln2` | `9.56993e-24 J/(K·bit)` |

And two bounds that run the wrong way: **Bekenstein** bounds information *by* energy; **Landauer**
bounds energy *below*, by information.

> **A constant of nature is not a discount.** The closure is not "five denominations failed" — it is that
> the table has no free parameter but `κ`, and `κ` is measured and short. **A sixth denomination must
> enter through `κ` or through the base, and the base is door one.**

**And the door count does not move.** `nopath.py`'s dimensional drift is a warped braneworld — door one.
`spectra.py`'s optimised spectrum is a black hole — inside the DEC branch **H21** exhausted. **Five
passes, still three doors**, and two of the five were built on M's principles rather than on the device.

**Door three gained a third independent arrival:** `create.py` from the topology theorems, `detect.py`
from the search side, `nopath.py` from the index picture. **Three starting points, one conclusion** — the
best-supported result in the project.

**And door one stopped being a category.** `scale.py` had already priced the supply side of exactly the
mechanism `nopath.py` named:

| | orders |
|---|---|
| ordinary shortfall at 1 m | **69.58** |
| braneworld shortfall | **38.36** |
| **what extra dimensions buy** | **31.22** |

**The largest single movement any lever in this project has produced.** It does not close the gap, and
`scale.py`'s `EXTRA_DIMENSIONS` is `NOT-RUN` because the *demand* side in a braneworld is a different
calculation in a different theory. **The scope decision is now about one named calculation with a
measured supply side, not about a category.**

**And exactly one door has a cost that is not a mass.**

| door | cost is | note |
|---|---|---|
| outside GR | theory-dependent | 31.22 orders measured; demand side `NOT-RUN` |
| not an energy question | unknown | GJW is an existence proof; nobody has costed a construction |
| **a relic** | **a search** | 32.13 M☉ at 1193 km, LIGO band, **on existing data** |

> Not a proof that door three is right. **The observation that it is the only one anybody could start on
> this week.**

| | `rates.py` |
|---|---|
| status | **PROVEN** (each rate reconstructed from the constants; the two bound directions) + **MEASURED** (the 31.22-order braneworld gain, from `scale.py`) |
| new? | the exhaustion argument for the currency question, and door one as a number, yes |
| **not** claimed | that 31.22 orders is a result — `scale.py`'s demand side is `NOT-RUN` and it cannot be quoted as one; that door three is the correct door — only that it is the only one with a payable cost; that `κ` has been shown impossible — it has been shown insufficient at `π/360` |

---

## ★★★ H25 — the three doors are decided by three different languages, and only one is refused

**H25. Run on the corpus's own index — register 1173 (binary → language → binary), register 1176
(`E = 0` iff the languages agree), section 33.2 (the silent language names the kind) — no two doors are
decided by the same language. Door one is UNDECIDABLE (algebra contested), door two is REFUSED (order),
door three is UNASKED (statistics silent).**

| | ORDER | GEOMETRY | ALGEBRA | INFORMATION | STATISTICS | E |
|---|---|---|---|---|---|---|
| **DOOR 1** | ADMITS | ADMITS | **CONTESTED** | ADMITS | NOT-RUN | **UNDEFINED** |
| **DOOR 2** | **REFUSES** | ADMITS | NOT-RUN | ADMITS | NOT-RUN | 1 |
| **DOOR 3** | ADMITS | ADMITS | NOT-RUN | ADMITS | **NOT-RUN** | 0 |

**Door one is not a hope.** Traversable wormholes needing **no exotic matter** are published solutions:
Kanti–Kleihaus–Kunz in 4D Einstein-dilaton-Gauss-Bonnet (arXiv:1108.3003), existing wherever
`α/r₀² ≲ 0.13`; and f(R) constructions (arXiv:0909.5539, review arXiv:2405.05476) where the *matter*
satisfies NEC, WEC and DEC and the higher-order curvature terms carry the violation. **Moved, not
removed — but moved off the matter.**

**Then stability turns it.** Cuyubamba–Konoplya–Zhidenko (arXiv:1804.11170): unstable **for any value of
`α`**, by a purely imaginary mode **non-perturbative in `α`** — it diverges rather than vanishes as
`α → 0`. And smaller `α/r₀²` grows *faster*, so **a bigger throat comes apart sooner**. Coupling bounded
at `√|α| < 0.87 km` (GW200115).

> **And the reason the original paper saw stability is this tree's own fault.** Kanti et al. fixed the
> **throat size** (`δr = 0`); `stability.py` fixed **the core's position**. Two stability claims, two
> literatures, **one fault: a coordinate was frozen and the mode that uses it was never asked.**

**A fifth status was needed and its existence is a finding.** `CONTESTED` is not `NOT-RUN` — it has been
run twice with opposite answers. By register 1173 a contested row returns no binary, so it earns no row:
**door one cannot be reduced at all.** Its `E` is UNDEFINED, not 1 — **not refused, undecidable.**

| door | verdict | decided by | kind (§33.2) | next measurement |
|---|---|---|---|---|
| 1 | UNDECIDABLE | algebra, contested | a **stability** object | a stability calculation — not a magnitude |
| 2 | REFUSED | order | a **causal-structure** object | nothing; closed by a theorem |
| 3 | UNASKED | statistics, silent | a **search** object | **a number density**, never estimated here |

> **The disagreement is the map.** Not three degrees of hopelessness: one refused, one undecidable, one
> merely unasked.

| | `doors.py` |
|---|---|
| status | **CITED** (every modified-gravity row carries its arXiv number and is marked cited, not measured) + **MEASURED** (the reduction, the deciders, the frozen-coordinate correspondence) |
| new? | the per-door reduction, the `CONTESTED` status, and the frozen-coordinate fault met in two literatures, yes |
| **not** claimed | that door three is **admitted** — its `E = 0` is over an incomplete set and the deciding row is the silent one; `index3.py`'s caution governs; that door one is refused — it is undecidable, which is weaker and different; that any modified-gravity solution has been verified here — those rows are **CITED** |

---

## ⚠ H26 — compression is not density; and a non-horizon holds exactly its compactness fraction

**H26. The Bekenstein bound is already denominated in compressed bits — it counts *distinguishable
states*, and naming one of N costs `log₂ N` in any code. And the best non-horizon carrier is exact:
`S_max(C) = C · S_BH`, so a non-black-hole holds exactly its compactness fraction of a horizon's
capacity.**

**The compression result is real.** Delétang et al. (DeepMind, ICLR 2024, arXiv:2309.10668): Chinchilla
70B compresses ImageNet to **48.0%** and LibriSpeech to **21.0%**, beating PNG (58.5%) and FLAC (30.9%)
— a text model beating domain-specific compressors on modalities it never saw.

**And the same paper refutes the use, three times.**

| | |
|---|---|
| **pigeonhole** | the authors state it: a lossless compressor is **injective** — it buys on some inputs by paying on others |
| **random data** | Chinchilla 70B: **100.8%**. gzip 100.0%, FLAC 107.8%. The models *expand* it |
| **the model is the code** | 70B params × 2 bytes = 140 GB → adjusted rate on 1 GB is **14008.3%**, 1687× worse than raw; break-even near **0.95 TB** |

> **Bekenstein counts distinguishable states; compression removes redundancy; entropy is what survives
> redundancy removal.** The bound is stated on the post-compression quantity already — which is precisely
> why random data does not compress.

**But "the only form other than a black hole" is the right question, and it has an exact answer nobody
here had computed.** Not being a black hole means compactness `C = 2GM/(Rc²) < 1`:

> `S_max(C) = C · A/(4ℓ_P²) = C · S_BH` — verified at `C = 0.99, 0.5, 0.1, 0.01, 1e−6`, worst relative
> residual `1.39e−16`.

**There is no second form.** The bound is continuous and its maximum *is* the horizon. Want 99% of the
density? Be 99% of the way to being a black hole.

**And door two is not refused for lack of density.** `doors.py` has it decided by **ORDER**, and its
refusal is the bank-loan theorem: traversability needs non-achronality, non-achronality needs an
*existing* outside causal path. **That theorem has no energy term and no density term in it.**

> **A density argument is the wrong kind of argument for door two, and the index is what says so** —
> `doors.py`'s first use since it was built, routing a proposal to the row it would have to move and
> finding it is not that row. A density argument lands on INFORMATION, which admits on all three doors.
> On the main question INFORMATION *does* refuse — and what is missing is **a value of `ρ`**. No bit
> count supplies a sign.

| | `compress.py` |
|---|---|
| status | **CITED** (the compression table, arXiv:2309.10668) + **PROVEN** (the compactness identity) + **MEASURED** (break-even, residuals) |
| new? | the compactness identity, and the routing of a density argument through the index, yes |
| **not** claimed | that the compression result is wrong — it is real and impressive; that the identity is bit-exact — an exact `==` was written first and **failed at two of five** on representation alone, so the claim was narrowed to one ULP; that `E < 0` is covered — `core.py`'s negative core has no Buchdahl limit and Bekenstein is not stated for negative energy: **NOT-RUN** |

---

## ★★ H27 — compressed bits are spendable on exactly one door, and not as density

**H27. A compression argument is a *statistics* argument. Door three is the door decided by statistics.
For the first time in this project the proposed currency and a door's deciding language are the same
language — and that, not the tool, is why it lands.**

| door | decided by | verdict |
|---|---|---|
| **2** | order | **NO — immune by form.** The bank-loan theorem has no information term |
| **1** | algebra | **RIGHT KIND, WRONG RESULT** — entropy stability does not imply dynamical stability |
| **3** | statistics | **YES — as a detection statistic** |

**Door one is the interesting no.** An entropy argument is *not* categorically wrong for a stability row —
thermodynamic stability is `d²S < 0`, the same *type* of condition as a dynamical one, and both are
defined for a wormhole. **The currency is spendable there.** But it has already been spent, in print, on
exactly this object: Eiroa, Figueroa-Aguirre, Peñafiel & Perez Bergliaffa (arXiv:2408.14328) compute both
for a charged thin-shell wormhole and find

- Hawking-type entropy: **no configurations both dynamically and thermodynamically stable**;
- power-law entropy: **thermodynamically stable but dynamically *unstable* configurations exist**.

> **Entropy stability does not imply dynamical stability.** The bridge exists, has been crossed, and lands
> somewhere else — so it is not a shortcut past the stability calculation **H25** named. Their entropy
> function is also an *ansatz*, carrying free parameters the dynamical side lacks: that is the slack.

**Door three is the yes, and the connection is an identity.** Arithmetic coding gives `ℓ = −log₂P`, so for
two hypotheses on the same data:

> **`log₂ B = ℓ₀ − ℓ₁`, exactly** — the evidence in bits *is* the compression saving in bits.

A signal is present exactly when the data is cheaper to describe with it than without (Rissanen's MDL).
Thresholds are small: 3σ = **8.53 bits**, **5σ = 20.73 bits**, 8σ = **49.51 bits**, each verified by a
round trip through `2^−bits` back to the p-value.

**And the objection that killed the density use does not reach this one.** `H26`'s fatal number was the
adjusted rate — 140 GB of parameters turning 8.3% into 14008.3%. Detection compares two hypotheses on the
*same* data with the *same* model, so `L(M)` appears on both sides and **cancels exactly** (verified at a
model size of `1.12e12` bits).

> **Density needs an absolute code length, where the codebook is fatal. Detection needs a difference,
> where the codebook cancels.** That one distinction is why the same tool fails one door and works for
> another.

| | `bits.py` |
|---|---|
| status | **PROVEN** (the `log₂B = ℓ₀−ℓ₁` identity; the codebook cancellation) + **CITED** (arXiv:2408.14328, arXiv:2309.10668) |
| new? | the routing of a currency by language-match, and the codebook-cancellation distinction, yes |
| **not** claimed | that it supplies the **number density** — a statistic is how you would *look*, not how many there are, and door three's silent row is still silent; that the cancellation is unconditional — it needs a **shared** model, and a template library leaves a real Occam penalty; that door one is immune — it is not, which is why the citation was needed |

---

## ★★ H28 — statistics is the only language with a dial, and the dial is exactly half a choice

**H28. In `tools/cypher.py` order returns a closure, algebra a span, geometry an integer hull,
information a set — all structural. Statistics alone returns a *distribution* whose **support** is the
binary. It is the only operator-bearing language whose binary is manufactured by a threshold rather than
read, so **door three is the only door with a dial on its verdict.**"**

Door one's algebra row is **contested** — two calculations, opposite answers, no knob. Door two's order
row is a **theorem with no free parameter**. Only door three has something a person can turn, and that is
a reason to prefer it.

**One refinement, from the corpus's own code.** In the cypher the threshold is **zero** — the support, the
one distinguished point of a distribution, *not* a choice; that is why statistics earns its row at all.
In a detection the threshold is `α`, and **nothing in nature sets five sigma**. So the choice appears
exactly at the move from the support question to a detection question — **and that move is door three.**

**But the dial moves what you announce, not what is there.** `P_D = Φ(ρ − z_α)`: you choose a *point* on
the ROC, the signal sets the *curve*.

| α | ρ=0 | 1 | 3 | 5 | 8 |
|---|---|---|---|---|---|
| 1e−1 | **0.1000** | 0.3891 | 0.9571 | 0.9999 | 1.0000 |
| 1e−3 | **0.0010** | 0.0183 | 0.4641 | 0.9719 | 1.0000 |
| 5.73e−7 | **0.0000** | 0.0001 | 0.0311 | 0.5538 | 0.9991 |

> The zero-signal column is the whole argument: **at `ρ = 0` the detection rate equals `α` exactly, at
> every threshold** (ratio 1.000000). Lower the threshold and you get more detections at precisely the
> rate you asked for, **all of them false.** Seating is a choice in the sense that the *announcement* is a
> choice. The occupancy is not.

**And the missing half is the silent row — which is why the two findings interlock.** Odds compose:
`posterior = prior × 2^bits`. You choose the threshold; **you do not choose the prior**, and for door
three the prior odds *is* the number density.

| prior odds | posterior after 5σ (`B = 1.7443e6`) | |
|---|---|---|
| 1e−2 | 1.744e4 | DISCOVERY |
| 1e−4 | 174.4 | DISCOVERY |
| **1e−6** | **1.744** | **not a discovery** |
| 1e−9 | 0.001744 | you would still bet against |

Read the other way — bits needed for 100:1 posterior odds: **13.3** at 1e−2, **26.6** at 1e−6, **36.5** at
1e−9, **46.5** at 1e−12.

> **So the number density is not merely the missing answer. It is the factor that sets how many bits any
> detection must carry.** **H25** called it door three's next measurement; this makes it the measurement
> that decides whether any detection could ever *count*.

| | `choice.py` |
|---|---|
| status | **PROVEN** (the roster asymmetry, read from `tools/cypher.py`) + **MEASURED** (the ROC table; the posterior arithmetic) |
| new? | that statistics is the only thresholded language, and that the prior sets the bit requirement, yes |
| **not** claimed | that seating is a choice — it is **half** a choice: the threshold is yours, the prior is not, and they multiply; that a lower threshold finds anything — at zero signal it returns exactly its own false-alarm rate; that the cypher's threshold is arbitrary — zero is canonical, and the arbitrariness enters only at the detection step |

---

## ★★★ H29 — light gravitates and drags frames, and it cannot supply the transition: **null dust satisfies the NEC identically**

**H29. For null dust `T_μν = ε η_μ η_ν` with `η` null, contracting with any null `k` gives
`T_μν k^μ k^ν = ε(η·k)² ≥ 0` — a non-negative times a square. Light satisfies the null energy condition
identically. The transition's refusal names `ρ < 0`, so light is not a weak answer to it; it is the
wrong *kind* of answer.**

**The physics underneath is real, and the ring-laser paper is not the contested one.** Tolman, Ehrenfest
& Podolsky (1931) showed thin pencils of light gravitate; Scully (1979) computed beam–beam coupling;
**Mallett's *Weak gravitational field of the electromagnetic radiation in a ring laser*** (Phys. Lett. A
269, 214, 2000) computed frame dragging in linearised GR — **ordinary gravitomagnetism, and correct** —
independently recomputed for optical vortices by Strohaber (arXiv:1112.3414).

**But the coupling does not ask what form the energy took.** Against this project's own rate of
`1.21237e43 J` per metre contracted:

| a 1 kW ring laser | |
|---|---|
| to contract **one metre** | `3.84e32` years = **2.78e22 ages of the universe** |
| run for a full year, buys | `2.60e−33` m = **161 Planck lengths** |
| one metre per second | **3.17e16 solar luminosities** |

**And Mallett's 2003 CTC solution is refuted on three independent grounds** — Olum & Everett
(gr-qc/0410078; Found. Phys. Lett. 18, 379, 2005):

| | |
|---|---|
| **magnitude** | `λ ≈ 1e−46` for a 1 kW laser (recomputed: `4.33e−47`), so CTCs begin at `ρ > 10^(1.0e46) ρ₀` — and the dependence is **logarithmic**, so `1/λ` sits in the **exponent**. Power cannot buy past it |
| **the singularity** | `R_αβγδR^αβγδ = 3/(4αρ³)` diverges on the axis, is no coordinate artifact, and is **independent of λ** — it persists at `ε = 0`. **Not Minkowski plus a light cylinder** |
| **the apparatus** | `ρ = const`, `dφ/dt = 1/α` are **null geodesics**: the light orbits the singularity and needs no optics. The ring laser is not doing the work |

Olum's follow-up (arXiv:1003.3828): in the static spacetime **every timelike geodesic terminates at the
singularity**, and a particle at rest at proper distance `R` is destroyed in proper time `≈1.3R`. And the
Tipler–Hawking escape needs an **infinite** cylinder — those theorems "would rule out the creation of
CTC's in any finite-size approximation." *In fairness, Mallett conceded the singularity himself.*

**The constructive number:** Strohaber puts a **1 Hz** spin precession — a frame drag you could merely
*measure* — at `~1e45 W/cm²`, against `~2e22` for the most intense laser built. **22.70 orders short**,
and 33 against a ring laser's own damage threshold.

> **Routed through the index it lands on two rows and fails on both, for different reasons.** As a source
> it is an INFORMATION claim and fails on **kind**. As a CTC mechanism it is an ORDER claim, lands on door
> two, and fails twice — refuted specifically *and* refused by the bank-loan theorem.

| | `light.py` |
|---|---|
| status | **PROVEN** (the null-dust NEC identity) + **MEASURED** (exchange-rate arithmetic; `λ` reproduced to order) + **CITED** (Phys. Lett. A 269, 214; Found. Phys. 33, 1307; gr-qc/0410078; arXiv:1003.3828; arXiv:1112.3414) |
| new? | the NEC identity applied to the light proposal, and the pricing against this project's own rate, yes |
| **not** claimed | that light does not gravitate — it does, and Mallett's 2000 frame-dragging result is correct; that Mallett was dishonest — he conceded the singularity, and the dispute is about what the solution shows; that this closes modified-gravity light couplings, which are door one |

---

## ★★★ H30 — **every** classical EM field satisfies the NEC; and light is what *breaks* the Gott construction

**H30. For the Maxwell stress tensor and any null `k`, set `V_a = F_{μa}k^μ`. Then
`T_μν k^μ k^ν = V·V` with `V·k = 0` **because F is antisymmetric** — so `V` is orthogonal to a null
vector, hence spacelike or parallel to it, hence `V·V ≥ 0` always. This widens **H29** from null dust to
*every* classical electromagnetic field: standing waves, optical lattices, vortices, photonic crystals,
any superposition.**

Measured over 200,000 random antisymmetric `F` and random null `k`: minimum `+2.04e−05`, with `|V·k|` at
`1.2e−15` — machine zero, as the antisymmetry requires.

**And the lattice was never needed anyway.** Olum & Everett: Mallett's circulating paths **are null
geodesics** of the background — "the light does not require any external apparatus to keep it in
circulation." The light orbits the singularity; the crystal did nothing.

**The cylinder was never the problem either.** Finiteness was the *second* objection. What the axis
requires is an **infinite naked line singularity** (`R_αβγδR^αβγδ = 3/4αρ³`, present at `ε = 0`), not a
cylinder of anything ordinary. And the static background is **its own non-detection**:

| at proper distance | destroyed in |
|---|---|
| 1 AU | **649 seconds** |
| 1 light-year | **1.3 years** |
| 1 parsec | 4.24 years |

**We are here, so it is not.**

**If nature is to supply the cylinder, the candidate is a cosmic string — closed four times.** A straight
string's exterior is a locally flat **conical deficit**: no dragging, no CTCs. Gott needs two passing
with `γδ₀ > 2`, i.e. `γ > 1.33e5` at the bound `Gμ ≲ 6e−7`. Then: **Deser–Jackiw–'t Hooft** (holonomy is
boost-like, matching a **tachyon**); **Carroll–Farhi–Guth–Olum** (infinite energy in 2+1; *cannot evolve
from strings at rest*); **'t Hooft** (closed universe collapses first); **Shlaer–Tye** (3+1: reachable,
and destroyed by one particle).

**And that last one inverts the proposal.** A photon near the CTC region is **attracted** to it — the
curve is an attractor, and *approximately half* of generic trajectories end in one — then traverses it
infinitely many times **in zero time** and is **infinitely blue-shifted**. Back-reaction bends the
strings and the CTC never forms.

> "A single graviton or photon in the vicinity, **no matter how soft**, is sufficient." And: "**Since
> there is a cosmic microwave background radiation in our universe, these photons preclude the existence
> of CTCs.**"

> **A cubic metre of empty space already holds `4.11e8` CMB photons. The mechanism needs one. Building
> the lattice out of light does not supply the medium — it floods the region with the precise thing that
> destroys the construction.** Not an objection to the engineering: the mechanism running backwards.

| | `lattice.py` |
|---|---|
| status | **PROVEN** (the general Maxwell NEC identity) + **MEASURED** (200,000-field scan; lifetimes; Gott threshold; CMB count) + **CITED** (gr-qc/0410078; arXiv:1003.3828; hep-th/0502242; arXiv:2101.08592) |
| new? | the NEC identity widened from null dust to the whole classical Maxwell field, yes |
| **not** claimed | that the questions were unreasonable — the lattice is the right question to ask of Mallett's construction, and the infinite cylinder is exactly the objection I raised; that cosmic strings are ruled out — only that the **Gott CTC route through them** is; that this touches modified-gravity light couplings, which are door one |

---

## ★★★ H31 — the **collapse identity**: `E_transition(d)/E_kugelblitz(d) = 2/Λ`, exactly, at every `d`

**H31. Read `Δd = (G/c²)MΛ` as an energy, `E_transition(d) = dc⁴/(GΛ)`, and compare it with the energy
that makes a Schwarzschild horizon of radius `d`, `E_kugelblitz(d) = dc⁴/(2G)`. Both are `(c⁴/G)` times a
length, so their ratio is a pure number:**

$$\frac{E_{\text{transition}}(d)}{E_{\text{kugelblitz}}(d)} \;=\; \frac{2}{\Lambda} \;=\; 0.200350028044\ldots \qquad\text{independent of } d$$

Measured over thirty-one decades, `1e−15 m` to `1e15 m`: worst residual `2.776e−17` — **one unit in the
last place**. The `d` cancels algebraically; the measurement only confirms there is no hidden scale.

**Contracting a distance `d` costs 20.035 % of the energy that makes a black hole of radius `d`, at every
scale at once.** This is why `COLLAPSE` keeps binding across `obstruct.py`: it is not a coincidence of
some particular design point but a structural feature of the equation.

**And at the Planck length it collapses further:** `E_transition(ℓ_P) = E_Planck/Λ`, exactly. `Λ` is not
merely a coefficient in the contraction law — it is the factor relating the transition's natural quantum
of energy to the Planck energy.

**The design margin is the inverse, `Λ/2 = 4.9912645871`** — the entire headroom before the same region
of space holds enough to be a horizon rather than a corridor. Every inefficiency, fill factor, duty cycle
and confinement loss spends out of that one number. *A factor of five is a tighter budget than any
machine humans have built runs on.*

### H31a — light is an excellent **seat** and a forbidden **lead**

The device splits (`reverse.py`, `apply.py`) into a **seat** — holds the corridor open, ordinary matter,
every energy condition satisfied, `M_ADM` a free parameter, **costs nothing exotic** — and a **lead**,
which does the contracting, **is the whole cost**, and requires `ρ < 0` (derived by PMT rigidity, not
assumed). Light against each half:

| half | light | why |
|---|---|---|
| **seat** | **passes** | positive energy density, focuses a null congruence the right way, carries momentum flux |
| **lead** | **fails, as a theorem** | **H30**: `T_μν k^μ k^ν = V·V ≥ 0` for *every* classical EM field |

**And more power makes it worse, not better** — scaling `F` by `s` scales `T_μν k^μ k^ν` by `s²`,
*upward*; measured. **Every joule spent on light goes to the side of the ledger that was never the
problem.**

### H31b — the margin degrades by a **square root**, and the kugelblitz block survives it

Álvarez-Domínguez, Garay, Martín-Martínez & Polo-Gómez (arXiv:2405.02389) close light-to-horizon by
Schwinger dissipation over `1e−29 m ≲ R ≲ 1e8 m`. Their figures, re-derived here rather than quoted:
Schwinger field `1.323e18 V/m`; `φ = √(3c⁴/4πε₀G) = 1.806e27 V`; threshold `fR = 5.211e82 W/m`;
`6.549e83 W` at `R = 1 m`; pair-formation length `/R = 2.829e−22`. Against a best laboratory field of
`1e15 V/m` and the brightest quasar at `1e41 W`.

**The transfer onto the transition is lossy in the wrong direction, because `u = ε₀|E|²`:**

$$\frac{|E|_{\text{transition}}}{|E|_{\text{kugelblitz}}} \;=\; \sqrt{2/\Lambda} \;=\; 0.4476047677 \qquad\text{at every radius}$$

**A factor of 4.99 in energy is a factor of 2.234 in field.** Each crosses the Schwinger limit once:

| | Schwinger crossing radius |
|---|---|
| kugelblitz | `9.6528e8 m` |
| transition | `4.3206e8 m` |
| ratio | `2.234114` = **exactly** `√(Λ/2)` |

**Both ends close on each other.** *Small* enough for the field to be reachable is impossible — the whole
of the paper's blocked band lies inside the transition's block too, since `1e8 < 4.32e8`. *Large* enough
to be sub-Schwinger is impossible — at `4.3206e8 m` the energy is `5.238e51 J` = **29,303 solar masses**,
delivered over one light-crossing at `3.635e51 W` = `3.6e10` brightest-quasars. **The margin bought a
factor of two and changed neither end.**

### H31c — the one freedom light has that mass does not

**Parallel null congruences do not focus each other — exactly zero, not weakly** (Tolman–Ehrenfest–
Podolsky 1931; Wheeler; arXiv:1009.3849). The mechanism is derived here, not cited: the field of a null
source is an impulsive pp-wave supported on `u = t − z = const`, and a parallel ray keeps `u` **constant**
along its worldline, so it never crosses the wavefront. Measured: 0 wavefront crossings parallel, 1
antiparallel; `T_μν k^μ k^ν = 0` for a null plane wave against a co-moving ray and `4.0` against a
counter-moving one — so **the zero is the geometry, not a vanishing field**.

Two masses always attract. **Two beams attract or do not according to their relative propagation
direction** — a sign-and-magnitude knob with no matter analogue. But its range is **zero to positive**:
the parallel case *is* **H30**'s equality case (`V` parallel to `k`), the theorem's boundary and not a
breach of it.

> **The knob turns the seat off and cannot turn the lead on.** That is still worth having — a seat you
> can switch off *geometrically*, by reorienting a beam rather than by removing energy, is control
> authority the matter architecture does not offer.

| | `lightbuild.py` |
|---|---|
| status | **PROVEN** (the collapse identity; `E_t(ℓ_P) = E_P/Λ`; the field square-root; the pp-wave crossing argument) + **MEASURED** (31 decades in `d`; six radii; `s²` scaling; Schwinger figures re-derived) + **CITED** (arXiv:2405.02389; arXiv:1009.3849) |
| new? | the collapse identity and its Planck form are **new here** — statements about M's own equation that this project did not hold before this pass |
| **not** claimed | that light is the wrong material — it is the right material for the half that was already free; that a **non-classical** light field is covered — **H30** is about the *classical* Maxwell stress tensor, and squeezed vacuum is held open by `neclab.py`; that the 2024 bound is re-derived in full — its five approximations are taken as stated, all of which its authors argue *underestimate* the dissipation |

---

## ★★★ H32 — a **pre-registered prediction**, and the first in this project that lands

**H31c** stated the parallel light–light factor as exactly zero and **deliberately withheld the
antiparallel one**, having not derived it. M then named it — **eight** — before any measurement of it
existed in this tree. It is eight.

**H32. The gravitational attraction between antiparallel (counter-propagating) light beams is exactly
`8×` the Newtonian attraction between two equivalent masses; the parallel case is exactly `0`.**

### Why this is a prediction and not a fit

`shape.py` set this bar **against this project**, before the prediction was made: *"the four hits are the
sample it was fitted to, and its only test is a prediction that lands"* (`NO-EVIDENCE`), and
`SHAPE-WRONG` records that **the first tested prediction failed**. Four conditions, all met:

| condition | status |
|---|---|
| the number was stated **first** | `lightbuild.py` §5 was written, selftested and committed carrying the parallel zero and no antiparallel factor |
| it was **not available to be fitted** | verified **against git** at `e95959e` — **94 `.py` files, none carries it** |
| it is **falsifiable and sharp** | an integer; `4`, `6` or `16` would each have refuted it outright |
| it was **adjudicated against sources** | and the first literature summary that came back said **four** |

> **The pre-registration is tested against git history, not the working tree.** An earlier draft of that
> check scanned the working tree and began **failing** the moment `lightbuild.py` was annotated with the
> result. That is the check catching its own error; it is recorded rather than quietly rewritten, and
> `UNVERIFIED` never counts as a pass.

### Three independent routes, agreeing exactly

**Route one — the spin-2 exchange amplitude, derived here.** `A(p,p') = 2(p·p')² − p²p'²`, normalised on
two static masses:

| source | test | `p·p'` | `A/A_Newton` | known value |
|---|---|---|---|---|
| mass | mass | `−mm'` | **1** | Newton |
| mass | photon | `−mE` | **2** | light bending is 2× |
| photon | mass | `−Em` | **2** | TEP: a beam pulls a mass 2× |
| photon | photon ∥ | `0` | **0** | TEP/Wheeler: exactly zero |
| photon | photon anti | `−2EE'` | **8** | **the prediction** |

`p² = 0` for a photon drops the second term, so the amplitude is a **square** — which is why the answer is
8 and not 4. And `k·k' = 0` parallel, `−2` antiparallel: **the zero and the eight are the same algebra
read at the two ends of one dot product.** Cross-checked non-circularly — the same expression for a test
particle of speed `β` near a static mass returns the textbook `(1+β²)` to `2.2e-16`, which was not put in.

**Route two — the published QED calculation.** Barker, Bhatia & Gupta, *Phys. Rev.* **158**, 1498 (1967),
photon–photon via a virtual graviton in the CoM system: *"the interaction have **eight times** the
'Newtonian' value plus a polarization dependent repulsive contact interaction."* Held as a **secondary
citation** through arXiv:1009.3849v5 — the 1967 paper is not reachable from here — and their contact term
is **not** claimed.

**Route three — and the apparent refutation dissolves.** Faraoni & Dumse (arXiv:gr-qc/9811052) state in
their **abstract**: *"the light-to-light attraction is twice the matter-to-light attraction and **four
times** the matter-to-matter attraction."* Read alone, that refutes H32 — and a one-line search returns
exactly that sentence. Recomputed from **their own equations** (`Φ_g = 2I ln(r/α)` so `|dΦ/dr| = 2I/r`,
Eq 4.4; `B_g = 2I/r`; force laws Eqs 2.11, 3.8, 2.15, 3.11):

| case | acceleration | ratio |
|---|---|---|
| matter → matter | `2 I/r` | **1** |
| light → matter | `4 I/r` | **2** |
| matter → light | `4 I/r` | **2** |
| light → light **parallel** | `0` | **0** |
| light → light **antiparallel** | `16 I/r` | **8** |

Their gravitoelectric part is `8 I/r` (Eq 4.5) and their gravitomagnetic part is `8 I/r` (Eq 4.2), and
their own §4 sentence: it *"cancels the gravitomagnetic part when the beam and the null ray are parallel,
and it **doubles** it when they are antiparallel."* `8 + 8 = 16` against a Newtonian `2`.

> **The abstract's four is the gravitoelectric *coefficient* — the `1 : 2 : 4` chain of the force laws —
> not the antiparallel *total*, which adds the gravitomagnetic half that the parallel case subtracts to
> zero. Both numbers are correct and they count different things**, and the abstract does not say which it
> counts. A number quoted out of the question it answers is exactly the failure mode the index exists to
> catch.

### What it is worth, and what it is not

> **The prediction landed on the seat, not on the lead.** It moves **no obstruction**. It is a coefficient
> on an attraction `lightbuild.py` already measured as negligible; it does not touch the NEC; it supplies
> no `ρ < 0`. The knob still runs from **zero to positive**, and the parallel case remains **H30**'s
> equality case.

What it genuinely adds: the knob is now measured at **both** ends, and `antiparallel/parallel = 8/0` —
not large, **undefined**. That makes it the sharpest control authority in the design space, over the half
that was never the problem. **A method that produces one correct unprompted integer has earned a second
look, and that is the entire claim.**

| | `factor8.py` |
|---|---|
| status | **PROVEN** (the spin-2 amplitude, and the `(1+β²)` cross-check) + **RECOMPUTED** (Faraoni & Dumse's chain from their own equations) + **CITED, SECONDARY** (Barker–Bhatia–Gupta via arXiv:1009.3849v5) + **PRE-REGISTERED** (verified against git at `e95959e`) |
| new? | the **adjudication** is new — that the published `4` and the published `8` answer different questions, and which is which. The factor itself is 1967 physics |
| **not** claimed | that the factor moves any obstruction, supplies `ρ < 0`, or reopens the lead; that the Barker–Bhatia–Gupta polarization-dependent contact term is included; that a primary reading of the 1967 paper was made |

---

## ★★☆ H33 — the currency thread closes: **the direction *is* the denomination**

Four exchanges' worth of the currency idea, tested. The ladder is real; everything built on top of
it is not. **H33 carries a prediction that *failed*, and it is recorded in full, because H32's landed
prediction is only worth something if this section exists.**

### H33a — denominations move the count, never the sum

Contracting 1 fm costs `1.2124e28 J`. Paid in CMB photons that is `1.15e50`; in optical `3.78e46`; in
1 MeV gamma `7.57e40`; in Planck-energy coins `6.20e18`. **The denomination spans 31.3 orders and the
sum does not move.** There is a largest coin — a photon's Schwarzschild radius crosses its wavelength
at the Planck energy — and it is the one place the metaphor returns a real number:
`E_t(ℓ_P) = E_Planck/Λ = 0.100175014`, the collapse identity's own `1/Λ` in currency language.

> **Caution, stated rather than buried:** a photon's energy is *frame-dependent*, so "largest coin" is
> not an invariant statement, and the Planck cap is a hoop-conjecture heuristic, not a theorem.

### H33b — a prediction that FAILED: "larger denominations are paid first"

That is the **greedy algorithm**, optimal exactly when a coin system is **canonical** — decidable, and
decided. It fails three independent ways.

**Not canonical.** Hydrogen's `n ≤ 6` transitions are *exact integers* in units of `R/3600`
(`E(n→m) = 3600(1/m² − 1/n²)`), so this is exact combinatorics with no rounding: coins
`{3500, 3456, 3375, 3200, 2700, 800, 756, 675, 500, 300, 256, 175, 125, 81, 44}`. Over targets 1–4000,
3385 are representable and **greedy finds no representation at all for 3275 of them — 96.7%**. First
failure at 88: greedy takes 81 and cannot make 7, while `44 + 44` sits there. Greedy is additionally
suboptimal at 2 more targets, first at 2025 — four coins where three suffice.

**Exact change is never required, so the claim is *empty* rather than merely false.** `Δd = (G/c²)MΛ`
is linear in M, so paying `E` buys `Δd = (G/c⁴)EΛ` continuously — there is no target to make change
for. With overshoot permitted, largest-first is trivially optimal for *any* coin set whatever.

**And the scale removes the premise.** The natural quantum is `1.9595e8 J`; the largest coin in the
ladder, a Co-60 gamma, is `2.1341e-13 J`. Ratio **`9.182e20` — 21.0 orders.** `9.18e20` gamma photons
buy one Planck length. There is no large denomination to pay first.

### H33c — the index is ONTO, and that inverts the question

Indexing all spectra against all directions of spacetime travel: the directions are the future
timelike and null tangent directions, and a photon's energy under a change of direction is
`D = 1/(γ(1 − β cos θ))`, which runs to `+∞` head-on and to `0` receding. **D sweeps the whole positive
real line**, so the table is completely populated — the 21 cm hyperfine photon becomes a 1.33 MeV
Co-60 gamma at `γ = 1.134e11`, a large boost and a legal direction.

> **The answer is not "no" — it is stronger than no. The direction *is* the denomination.** There is no
> independent fact about which denomination a photon is: a radio photon and a gamma are **the same
> object** seen from two states of motion. The table has **rank one**, so the spectrum column carries
> nothing the direction column does not already carry.

### H33d — what survives is the angle, not the energy

| β | E | E′ | `k·k'` |
|---|---|---|---|
| 0 | 1.0000 | 1.0000 | **−2.000000** |
| 0.6 | 0.5000 | 2.0000 | **−2.000000** |
| 0.95 | 0.1601 | 6.2450 | **−2.000000** |
| 0.999 | 0.0224 | 44.7102 | **−2.000000** |

The energies move by orders; the contraction does not move at all. And the `0 → 8` knob riding on it is
`8.000000` and `0.000000` in **every** frame.

> **Light is not a currency in the structured sense.** A currency has denominations because it must
> settle *exactly*; this settles continuously and its denominations are frame-dependent. **It is a bulk
> commodity priced by the joule** — and that is why no choice of spectrum has ever moved a number here.
> Every currency attempt has tried to build an invariant out of a frame-dependent quantity.

| | `denominate.py` |
|---|---|
| status | **PROVEN** (Doppler onto-ness; `k·k'` invariance; linearity of `Δd` in E) + **MEASURED** (31.3 orders of denomination; exact coin-change DP over 4000 targets) + **FAILED PREDICTION**, recorded |
| new? | the onto-ness of the spectra × direction index, and its consequence that denomination is not a property of a photon |
| **not** claimed | that the Planck cap is a theorem — it is a heuristic, and frame-dependent; that this moves any obstruction; that the `2² = 4` question was left open — it is **closed** in **H34**, and the "hole" claim is **withdrawn** |

---

## ★★★ H34 — **4 is the bisector**, and H32's "hole" is withdrawn

**This section corrects a claim this project made.** H32 reported a *hole* at `2² = 4` — "nothing in
the table returns 4 as a total" — and H33 carried it as an open lead. **It was wrong.** I had sampled
**five named configurations** and reported a property of the *continuum* from a property of my sample.

Two independent things were missed, and three pushes found both.

### H34a — the continuum is dense in [0, 8], and 4 is reached

For two null directions separated by `θ`, `p² = 0` drops the trace term, leaving
`A/A_N = 2(1 − cos θ)²` — monotonic from 0 to 8, so **the range is exactly the closed interval [0, 8]
and every value is reached exactly once**. With `c = 2sin(θ/2)` the chord on the unit sphere of
directions, `c² = 2(1 − cos θ)`, so

**`A/A_N = c⁴/2`,  `c ∈ [0, 2]`  —  and 8 is `2⁴/2`, the diameter to the fourth, halved.**

| n | 0 | 1 | 2 | 3 | **4** | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| **θ°** | 0 | 72.97 | 90.00 | 102.99 | **114.47** | 125.53 | 137.06 | 150.56 | 180 |
| **cₙ** | 0 | 1.189207 | 1.414214 | 1.565085 | 1.681793 | 1.778279 | 1.861210 | 1.934336 | 2 |

`cₙ = (2n)^{1/4}`, matching the angle-derived chord to machine precision. **No two edges are the same
length, and the law is a fourth root.**

### H34b — and 4 is never a *total* for a reason that is not absence

Faraoni & Dumse's own arithmetic, their units: Newtonian reference `2 I/r`; **gravitoelectric half
`8 I/r`; gravitomagnetic half `8 I/r`** — so in Newtonians **each half is exactly 4**, and the
observable is

**`4 ± 4`  →  antiparallel `8`, parallel `0`**

> **4 is the axis they swing about, and a bisector is not a value the curve takes.** That is why
> nothing ever returned it. It is a midline, not a gap.

**And this makes H32's adjudication exact rather than merely correct.** H32 said the published `4` and
the published `8` "count different things" — true, and vague. The exact statement:

> **Faraoni & Dumse's 4 is the AXIS; Barker–Bhatia–Gupta's 8 is the EXTREME** — the centre and the
> endpoint of one interval.

*Tested, not assumed:* 4 bisects the **amplitude range and nothing else here**. The turning 0–180° is
bisected at 90°, which is `n = 2`; the chord range [0, 2] at `n = 0.5`; the linear coordinate
`√(A/2) = 1 − cos θ` at `n = 2`.

### H34c — as a string it cannot close, and it has one stationary point

**Total turning is exactly `180.0000000000°`** against the `360°` a closed polygon requires, so the
structure is **intrinsically a string, not "better read as" one**. Both walks confirm: gaps-as-turns
ends `6.813214` from the origin, headings-with-chords ends `11.487572`. No polygon appears.

**And "half a revolution" is the wrong gloss on a right number.** Calling 180° "half the turning a loop
needs" implies there is further range to travel and the string stopped short. There is not. The relative
orientation of two directions lives in **[0, π] — an interval with two distinct endpoints, not a circle**
— because `θ` and `2π − θ` are *the same pair*: measured, `A(φ) = A(2π − φ)` identically at 30, 60, 90,
120 and 150°, so a circle coordinate is a genuine **2-to-1** map onto the physical states. **180° is not
half the range; it is the range, exhausted.**

The coupling is a strict **bijection [0, π] → [0, 8]** — strictly increasing over 200,000 samples, one
angle to one value. So closing the interval means gluing `θ = 0` to `θ = π`, and at that glue point
`A(0) = 0` and `A(π) = 8` would have to be **the same value**.

> **One configuration would carry both the parallel and the antiparallel coupling at once. Closure is not
> merely unreached — it is contradictory.**

*Reading this as a statement about a transition state is an interpretation laid on top of the geometry —
consistent with it, not derived from it. What is derived: the endpoints cannot be identified without
making the coupling two-valued.*

And one stationary point, **derived rather than read off**: with `s = √(n/2)`,
`dθ/dn = 1/(4s^{3/2}√(2−s))`, minimal when `s³(2−s)` is maximal, i.e. `2s²(3 − 2s) = 0`, i.e.
**`s = 3/2` exactly** — giving `n = 9/2` and `cos θ = −1/2`:

**`θ = 120°` exactly, with 4 and 5 straddling it.**

So **4 is also the last integer rung before the structure's turning point** — a second, independent
sense in which it sits at a centre.

### H34d — what stays refuted

**Not 8 dimensions.** Evaluated in `D = 3, 4, 5, 8, 10, 11, 26`: exactly **8** in every one, parallel
exactly **0** in every one. `k·k' = −2` for antiparallel nulls in *any* dimension, and `D` never
appears in `2(p·p')² − p²p'²`.

**Not a regular frame.** Regular spacing would be 22.5°; the gaps run 72.97, 17.03, 12.99, 11.48,
11.06, 11.53, 13.50, 29.44 — a **6.597** ratio. A smooth curve read at integer heights, not a polygon.

**And not a route to `ρ < 0`.** The knob runs zero to positive about an axis of 4; the parallel end is
still **H30**'s equality case. **The lead is a sign, and a bisector is not a sign.**

| | `bisector.py` |
|---|---|
| status | **CORRECTION** (H32's hole, withdrawn) + **PROVEN** (`c⁴/2`; the 180° non-closure; `s = 3/2` from `2s²(3−2s) = 0`) + **RECOMPUTED** (the GE/GM halves from Faraoni & Dumse's equations) |
| new? | the bisector reading, the `c⁴/2` closed form, the exact 120° stationary point — and the exact form of H32's adjudication |
| **not** claimed | 8 dimensions; a regular frame; any `ρ < 0`; that 4 bisects anything but the amplitude range |

---

## ★★★ H35 — a transition state cannot close on a **definite** state, derived three ways

**H34** could only mark this as interpretation: *"reading this as a statement about a transition state
is laid on top of the geometry — consistent with it, not derived from it."* **H35 derives it — and
deliberately not from the geometry.** A statement about closed timelike curves does not follow from one
about the space of relative orientations; deriving it that way would be the exact over-reach H34
declined. The derivation runs instead from the consistency condition closure itself imposes.

### Why it is not vacuous here

`chronology.py` already holds `EVERETT_ROUTE_OPEN = True` — two devices plus a boost, needing no
identification — so **closure is reachable for this architecture**. `MTY_ROUTE_OPEN = False`, and
`HAWKING = NOT-RUN`. The constraint is live, and it is reached **without** touching the Cauchy-horizon
question.

### The three routes

**Classical.** The grandfather condition is `b = b ⊕ 1` over `{0,1}`. Enumerated over the whole domain
— both of it — **there is no solution**. Definite closure is not unreached; it is *unsatisfiable*.

**Deutsch** (*Phys. Rev. D* **44**, 3197). A fixed point of `ρ = Tr_CR[U(ρ_CR ⊗ ρ)U†]` **always** exists
— density matrices are compact and convex, the map continuous — so closure is never simply forbidden.
But solving `ρ = XρX` in full gives `[[d,c],[b,a]] = [[a,b],[c,d]]`, forcing `a = d = 1/2` with only the
real off-diagonal free:

> **Every fixed point has `ρ₀₀ = ρ₁₁ = 1/2` exactly.** 81 found on a Bloch scan at 1/40 resolution, all
> on the **x-axis** (`r_y = r_z = 0` — conjugation by X keeps `r_x` and flips the others; *not* the
> equator), worst `|ρ₀₀ − 1/2|` exactly **0**. And the two **pure** solutions — the X-eigenstates — are
> still fifty-fifty in the computational basis the paradox is stated in.

**Postselected CTCs** (Lloyd, Maccone *et al.*). The effective map is `Tr_CTC[U] ρ Tr_CTC[U]†`, and
`Tr[X] = 0`, so the amplitude is **exactly zero** — strictly forbidden, not mixed. The suppression is
*selective*, which is what makes it an argument rather than a degeneracy: `Tr[I] = 2` leaves an
unparadoxical loop alone and a T gate has `|Tr| = 1.8478` and survives, while `Tr[Z] = Tr[H] = 0`.

| model | condition | result | reading |
|---|---|---|---|
| classical | `b = b ⊕ 1` | no solution | unsatisfiable |
| Deutsch D-CTC | `ρ = XρX` | `ρ₀₀ = ρ₁₁ = 1/2` | only at 50/50 |
| postselected P-CTC | `Tr_CTC[X] = 0` | amplitude 0 | forbidden |

> **They disagree about what happens instead — D-CTCs against P-CTCs is a live dispute across nearly
> every question put to them — and agree that no definite single-state closure exists.** A conclusion
> that survives two prescriptions which contradict each other elsewhere is stronger than one needing
> either.

### What is *not* claimed

- **That this and H34's geometry are the same fact.** They are one *shape* in two different systems —
  closure forcing a single object to carry two values. A shape recurring across unrelated systems is a
  finding, **not** an identification.
- **That the device's corridor actually closes.** The route is open, not taken.
- **That Hawking is resolved.** `NOT-RUN` stands, untouched.
- **That grandfather dynamics is the only dynamics.** An unparadoxical loop is not suppressed at all.
- **Any `ρ < 0`.** It constrains closure, not the lead.

| | `closure.py` |
|---|---|
| status | **DERIVED** (three independent routes) + **MEASURED** (Bloch-ball fixed-point scan; the P-CTC traces) + **CITED** (Deutsch 1991; Lloyd–Maccone P-CTCs) |
| new? | the derivation, and the observation that two mutually contradictory CTC prescriptions agree on exactly this one point |
| **not** claimed | identity with the geometry; that the corridor closes; Hawking; universality over all loop dynamics; any `ρ < 0` |

---

## ★★★ H36 — **closability** is a design property, and it puts a new requirement on the lead

> M: *"if it opens, it closes. The mass density energy approach would have forced a corridor open that
> couldn't close. The reason we are identifying other cheaper currency is for the ability to close what
> we open. Small and contained."*

**Every instrument in this project asks what a corridor costs to OPEN. None asked what it costs to
SHUT.** That is a real gap. The quantity is `τ` — the corridor's lifetime after you stop paying.

### H36a — the asymmetry is a difference in kind

**Light.** The field is null. Stop the source and the region clears at `c`; there is nothing to remove,
because the carrier leaves on its own at the only speed it has. `τ_light = R/c` — 3.34 ns at a metre.

**Matter.** A static configuration persists. Nothing clears it but **work**, bounded below by how fast
mass can be moved, which is slower than `c`. For the seated architecture it is worse: `core.py`'s core is
a strong-field object carrying `negmass.py`'s and `stability.py`'s instability findings.

> **Light's teardown is free and at `c`; matter's is work and slower.** *Stated because it is true:*
> matter **can** be made transient — you may throw it away. The asymmetry is that light's termination is
> *automatic and c-limited*, not that matter's is impossible.

### H36b — and that is what decides the CTC

`chronology.py` leaves `EVERETT_ROUTE_OPEN = True`; **H35** derived that a closed curve admits no
definite state. **So an un-closable corridor is the standing precondition for exactly that failure.**

A closed causal loop must traverse device 1, propagate to device 2, traverse it and return — at least
`2D/c`, with *both* corridors still open. So a CTC needs `τ ≥ 2D/c`. A light corridor has `τ = R/c`,
which would require `R ≥ 2D`; but separate devices do not overlap, so `D ≥ R` and `2D ≥ 2R > R`:

**`τ/loop = R/(2D) ≤ 1/2` for every non-overlapping pair.**

Measured at `R = D` = 1 µm, 1 mm, 1 m, 1 km, 1 Mm — **no** at every one, and the ratio depends only on
`R/D`. A self-terminating light corridor **cannot host the Everett CTC at any separation**, while an
unbounded matter corridor satisfies the condition at **every** separation. "Small and contained" is
`R < 2D`, which is free.

> *This is a **causal-window scaling argument, not a theorem**. The factor of 2 is geometry-dependent.
> What is robust is that `τ ~ R`, the loop `~ D`, and `D ≥ R` — so no choice of coefficient rescues the
> light case into a CTC.*

### H36c — the qualification, which turns the result into a specification

A corridor is held open by the seat **and** the lead, so its lifetime is the **longer**:

**`τ_corridor = max(τ_seat, τ_lead)`**

Light can seat (`τ = R/c`). Light **cannot** lead — **H30** is untouched. So if the lead is a persistent
matter configuration, `τ_lead` is unbounded and `τ_corridor` is unbounded with it, and the CTC argument
above **evaporates**.

> **The teardown advantage is real and it is conditional: it belongs to the corridor only if the LEAD is
> transient too. That is not a defeat but a specification, and nothing here had written it down —
> THE LEAD MUST BE SWITCHABLE.** Every previous pass asked the lead for a *sign*; this one asks it for a
> *deadline*.

### H36d — the index move scores differently

*"Two axes of information that share a value, this means there is another."* **A third instance exists:**
`c(t + 2π) = −c(t)` to `8.88e-16` — the chord is **antiperiodic, spinorial**, needing 4π to return — and
the observable is restored by the even power, `A(t + 2π) = +A(t)` to `6.66e-15`.

But it is **not independent** (same angular variable as **H34**'s — a sub-structure, not a new axis), and
**the shape is monodromy**, which is not a discovery but the definition of a multivalued function
continued around a non-trivial loop: branch points, double covers, holonomy, Berry phase, a spinor's 4π
period. **Finding it a third time is expected, not informative.**

One small thing it settles: the observable must be an **even** power of the chord to be single-valued —
but that does *not* fix the power at four, since `c²` is even too. **The four comes from spin-2 squaring.**

| | `teardown.py` |
|---|---|
| status | **DERIVED** (the window argument, as a *scaling*) + **MEASURED** (`τ` across five scales; the chord antiperiod) + **SPECIFICATION** (the lead must be switchable) |
| new? | closability as a tracked property; the CTC window; the switchability requirement on the lead |
| **not** claimed | that it rescues the lead — **H30** stands; that the window argument is a theorem; that the third monodromy instance is independent or informative |

---

## ★★★ H37 — the three candidate leads, run. All fail, each at a **different gate**.

> M: *"I honestly cannot remember. I read it in passing. We'll have to run all three candidates."*

**The spec now has three halves**, and the third is new here. **KIND**: supplies `ρ < 0` — genuinely, not
"negative mass" in some effective sense. **DEADLINE** (**H36**): switches off in `~R/c`. **MAGNITUDE**:
enough of it — the lead is the whole cost, so `|ρ_needed| ~ c⁴/(GΛR²)`. Previous passes asked for the
sign, and since **H36** the deadline. *Neither asked the quantum sources how much they can supply*, and
that is what decides all three.

### H37a — negative effective mass fails at the **first** gate

Negative-mass exciton polaritons are real, measured and switchable — dissipative light–matter coupling
inverts the lower polariton branch and propagation runs opposite to momentum (arXiv:2204.04041; also
spin-orbit-coupled BECs, arXiv:1801.04779).

> **And it is the wrong quantity, which no engineering fixes.** `m* = ħ²/(d²E/dk²)` is the **curvature of
> a band**, not `T₀₀`. A quasiparticle with `m* < 0` still carries *positive* energy; what is inverted is
> how its group velocity responds to momentum. It violates **no energy condition at all** — **H30** does
> not even engage with it, because the gravitational source is the full stress-energy of cavity, excitons
> and field, and that is positive. **A negative-mass polariton would not bend spacetime the wrong way.**

"Negative mass" is one phrase for two different things and only one of them is exotic.

### H37b — Casimir passes KIND, fails the DEADLINE

`ρ = −π²ħc/(720 d⁴)` — a genuine negative energy density, `4.334e4 J/m³` at 10 nm, `4.334e8` at 1 nm,
measured in the laboratory. Switching it off means **moving the plates**: mechanical, slower than `c`, and
the negative region is anchored to plates whose own mass-energy is hugely positive and goes nowhere.

### H37c — squeezed vacuum passes both qualitative gates, and **two routes select it**

`lightbuild.py`'s `OPEN` row already said **H30** covers only the *classical* Maxwell stress tensor and
squeezed vacuum is precisely the exception. **H36**'s deadline independently demands a lead that clears at
`c` — which killing the pump does. **Two independent routes, one candidate.** That convergence is why the
pass did not stop at H37a.

### H37d — and the third gate is **structural**

Ford–Roman (massless scalar, 4D) bounds `|ρ| ≤ 3ħc/(32π²L⁴)`; the Casimir law has the same shape. Now
notice the exponents:

| | scaling |
|---|---|
| what is **allowed** | `L⁻⁴` |
| what is **needed** | `R⁻²` |

**So the shortfall goes as `R²` and shrinking always helps** — "small and contained" is quantitatively the
right direction, and the only one that helps at all. It is still **52.6 orders short at a nanometre** and
**70.6 at a metre** (Casimir `2.798e52` / `2.798e70`) — the same order as the kugelblitz block in **H31b**,
reached from a completely different direction.

**And the crossover has a closed form, which is the result:**

**`R = ℓ_P √(3Λ/32π²) = 0.307933 ℓ_P`**  (Ford–Roman)  ·  **`R = ℓ_P π√(Λ/720) = 0.369917 ℓ_P`**  (Casimir)

> **The bound meets the requirement only *below the Planck length*. The framework fails before the bound
> does** — this is not "very hard", it is outside the domain of the theory stating it. And **Λ sits in both
> closed forms.**

### H37e — one constraint that did not fight

The quantum inequality says a deeper negative energy must be **briefer**; the deadline says the lead must
be brief. **They point the same way.** `teardown.py`'s requirement is **free** against the inequality —
and if anything ever does supply the magnitude, switchability will not be what stops it.

### H37f — a **fourth** candidate, and it fails *differently*

Non-minimal coupling, `δL = ξRφ²`, violates the NEC and WEC **classically**, and Fewster & Osterbrink
(arXiv:0708.2450) prove something stronger than an evasion: **for `ξ > 0` there is no state-independent
QEI at all.** Given any bounded region and any `ρ₀ > 0` they *construct* a Hadamard state with energy
density below `−ρ₀` throughout it. **KIND passes; the Ford–Roman gate does not apply, because there is no
such bound to apply.**

What replaces it is a **state-dependent** bound, and the cost does not vanish — it **moves**. Their
H-bounds: `Q(f)` is bounded by any power of `H` above 2, `ρ(f)` by none below 3. *"Negative energy effects
with large magnitude… require more energy to achieve than positive energy densities of the same magnitude,
and the energy budget… will grow with a different power."*

**And the EFT treatment makes it computable.** Fliss, Freivogel, Kontou & Pardo Santos (arXiv:2309.10848)
derive a SNEC-type bound `|T₋₋| ≲ N_n/(ℓ_UV^{n−2} δ²)` with `φ²_max ~ ℓ_UV^{−(n−2)}` — in 4D SI units,
`|ρ| ~ ħc/(ℓ_UV² δ²)`. Against the requirement:

| | scaling |
|---|---|
| allowed | `δ⁻²` |
| needed | `R⁻²` |

> **The exponents match. The `R`-dependence cancels.** Measured at `R = 1e-9`, `1`, `1e6` m with
> `ℓ_UV = 10 ℓ_P`: shortfall **10.017501 at all three, identical to eight digits**.

**`shortfall = (ℓ_UV/ℓ_P)² / Λ`** — a *pure number*, not 52 orders and not a function of how big you build
it. It **closes at `ℓ_UV = √Λ ℓ_P = 3.159514 ℓ_P`**: `0.1002` at `ℓ_P` (would pass), `1.0000` at
`3.1595 ℓ_P`, `10.018` at `10 ℓ_P`, `3.83e32` at an LHC-scale cutoff.

**Why it still fails — the authors' own reasons.** `φ²_max ≲ (8πG_N|ξ|)⁻¹`, and at that field value a
tower of irrelevant interactions turns on in the Einstein frame while the gravity path integral loses
semi-classical control in the Jordan frame. **An EFT cut off at a few Planck lengths is not an EFT result
— it says you need quantum gravity.** Their verdict, quoted: *"it seems that it is impossible to construct
traversable wormholes in the Jordan frame without unphysical field values."* The effective ANEC — the
thing that must be violated — **is obeyed** once field values are bounded, and the Jordan/Einstein frames
differ by a factor close to 1, so the exotic behaviour is a **frame artefact** wherever the EFT is valid.

> *Status of the number: **scaling estimate, not a derivation**. `N_n` is schematic in the source and set
> to 1 here; a true coefficient of 10 or 1/10 moves the crossover by `√10` in the **cutoff** and by nothing
> in the orders. **The finding is the exponent match, not the number.***

### H37g — and the three crossovers sit on top of each other

| mechanism | crossover |
|---|---|
| Ford–Roman | **0.307933 `ℓ_P`** |
| Casimir | **0.369917 `ℓ_P`** |
| non-minimal coupling | **3.159514 `ℓ_P`** |

> **Three mechanisms with nothing in common** — a sampling inequality, a boundary-condition vacuum, and a
> curvature coupling inside an EFT — **all running out within one order of the Planck length**, with `Λ` in
> all three closed forms. **The obstruction is not a limitation of any one mechanism: every known
> negative-energy source runs out exactly where the theory stating the requirement runs out. The magnitude
> gate and the Planck scale are the same gate.**

That is a finding about the *framework*, and it is why a fifth candidate **inside the same framework**
should not be expected to behave differently.

| | `candidates.py` |
|---|---|
| status | **DERIVED** (the `L⁻⁴` vs `R⁻²` structure; both closed-form crossovers) + **MEASURED** (shortfalls across four scales; Casimir densities) + **CITED** (arXiv:2204.04041; arXiv:1801.04779) |
| new? | the magnitude gate itself; that all three bounds meet the requirement only sub-Planckially, with Λ in the closed forms; that the deadline is free |
| **not** claimed | that the list is exhaustive — three were named and three were run; a fourth may exist and this file does not speak to it |

---

## ★★★ H38 — the framework, asked to specify itself, answers. **Every gate closes.**

> M: *"the solution is to not find another framework, but instead build it from what this current
> framework says it needs to be."*

**H37g** found three unrelated mechanisms all running out within one order of the Planck length and read
it as an *obstruction*. **Read as a specification it is an instruction.**

### H38a — solve the gates for R instead of assuming it

Every gate is a statement about **one length**. Every previous pass *picked* an `R` — a nanometre, a
metre — and watched the gates fail. Solving for `R`:

| | |
|---|---|
| `R` | `ℓ_P` = **1.616255e-35 m** |
| `τ` | `ℓ_P/c` = **5.391246e-44 s** — one Planck time |
| `E` | `E_Planck/Λ` = **1.959505e8 J** |

**That energy is 195.95 megajoules.** 54.43 kWh. The chemical energy of 46.8 kg of TNT. The rest mass of
2.18 nanograms. *After seventy orders of shortfall, a purchase-order number.*

### H38b — and it passes. All three.

- **MAGNITUDE**: shortfall at `R = ℓ_UV = ℓ_P` is `1/Λ = 0.100175` — **passes with a factor of Λ in hand**.
- **DEADLINE**: `τ` = one Planck time against a CTC loop of `2R/c = 1.078e-43 s`. **H35**'s state-splitting
  never arises — the array cannot host a closed timelike curve at any separation.
- **KIND**: supplied by **H37f**, the one candidate whose shortfall was a pure number — and at this `R`
  that number is below one.

And it sits exactly where **H31** says it should: `E_t/E_kugelblitz = 0.200350028 = 2/Λ`, margin
`Λ/2 = 4.9913` intact. **Nothing was tuned** — the same identity, at the length the gates chose.

### H38c — what it buys, and where it turns

**`Δd = 1.616255e-35 m`.** One Planck length. *The energy is small because the output is small.* There is
no discount hiding in the Planck scale, only a very small purchase.

### H38d — tiling is exactly neutral

`Δd` is linear in `M`, so cells tile:

| target | cells | tiled | closed form |
|---|---|---|---|
| 1 fm | `6.1871e19` | `1.2124e28 J` | `1.2124e28 J` |
| 1 m | `6.1871e34` | `1.212374e43 J` | `1.212374e43 J` |

> **The exchange rate is scale-invariant. Tiling passes every gate cell by cell and moves the bill not at
> all.**

### H38e — which relocates the project

Every one of `obstruct.py`'s **53** recorded obstructions is about the **mechanism**. The framework's own
specification dissolves all of them and leaves the bill exactly where it was.

> **The seventy orders were never a mechanism problem.** They are `c⁴/(GΛ) = 1.2123737e43 J/m`, and three
> of its four symbols are constants of nature.

And the fourth is shut. `Λ = 2[ln(2R_s/b) − 1]` is **logarithmic** in the geometry:

| to make 1 m cost | needs Λ | needs `R_s/b` |
|---|---|---|
| world annual energy | `2.0171e23` | `> 1e300` |
| a one-megaton bomb | `1.2103e29` | `> 1e300` |
| one kilowatt-hour | `3.3618e37` | `> 1e300` |

Even `Λ = 100` needs `R_s/b = 7.05e21` — and the shell must exceed the corridor by that factor, while the
corridor is what you are trying to travel down. **The only lever is shut, and it was never the mechanism's
fault.**

### What is **not** claimed — and this matters more than any of the above

- **This is not transport.** One Planck length for 196 MJ is a gate-passing *configuration*, not a drive.
  Nothing here moves anything anywhere.
- **A Planck cell is not shown to be buildable.** Every gate is stated in a theory **H37** showed *fails*
  at this scale. The 196 MJ is **what the framework says, not what a laboratory would pay**.
- **No obstruction moves.** `obstruct.py` is unchanged at 53, deliberately. A specification that satisfies
  constraints is not a demonstration that those constraints were binding — and **H38e** is precisely the
  finding that they were not.

| | `planckcell.py` |
|---|---|
| status | **DERIVED** (the gates solved for `R`; tiling neutrality; the Λ lever) + **MEASURED** (196 MJ; the collapse ratio untuned at `d = ℓ_P`; scale-invariance over 21 decades) |
| new? | the first configuration in this project to pass **every** gate — and the finding that passing them costs nothing and changes nothing |
| **not** claimed | transport; buildability; that any obstruction moved |

---

## ★★★ H39 — the **epistemic audit**: the headline is a *model*, and the refusals are theorems

> M: *"let's take a moment to review all the research. If anything we have used from outside literature,
> such as assertions, conjecture, heuristics, perhaps we can define the theorems, proofs, laws, etc."*

Sorted by logical status, the project splits cleanly and uncomfortably. **This belongs in any paper, stated
up front, rather than discovered by a referee.**

### H39a — the transition equation is a MODEL, not a theorem

`Δd = (G/c²)MΛ` comes from a **chosen potential** in a **chosen metric form** — isotropic,
`g_tt = −e^{2Φ}`, `g_ij = e^{−2Φ}`, with `Φ` a Plummer core minus a shell. `Λ = 2[ln(2R_s/√(b²+a²)) − 1]`
is a closed form derived from *that potential* and validated against *its own integral* to 0.08%.

> **That validation is internal.** It shows the closed form matches the ansatz — not that the ansatz
> solves `G_μν = 8πT_μν` for any specified matter model. `NOT-CERTIFIED` has recorded this since the Le
> pass, and `core.py` puts it more sharply: `Φ_max = m/a` runs 0.25 to 1.0 across the seated window, and
> at `Φ = 1` the linearised spatial metric **has flipped sign**.

**So the headline — `c⁴/(GΛ) = 1.2123737e43 J/m` — is MODEL.** The seventy orders, the Planck cell, the
196 MJ, the tiling neutrality and the scale-invariance **all inherit it**, because all of them are Λ
wearing different clothes.

### H39b — and the asymmetry is the real result

**10 obstructions, 5 constructions**, and the split is clean:

> **Every obstruction this project trusts is a THEOREM. Every positive construction it offers is a MODEL.**

Proved *here*: the Maxwell NEC theorem, the null-dust identity, the `[0,π]` orientation topology, the
complete Deutsch fixed-point set, the classical grandfather condition. Cited *from proofs*: PMT rigidity
(Schoen–Yau, Witten), Ford–Roman, Fewster–Osterbrink.

**That is exactly the shape a negative result should have, and exactly the wrong shape for a positive one.**

### H39c — three headline "confirmations" are one definition

The collapse identity `2/Λ`, the Planck form `E_P/Λ`, and the granularity gap `Λ` are **identities**. Both
sides of each are `(c⁴/G)` × a length by construction; `ℓ_P c⁴/G` **is** `E_Planck`; `ħc/ℓ_P` **is**
`E_Planck`. They cannot be otherwise.

> **They are true and they are not evidence.** The recurrence of Λ across them is the recurrence of *one
> definition*, not three independent confirmations. A paper presenting them as corroboration would be
> presenting the same fact three times.

What they *do* establish: internal consistency at the Planck scale, with the margin untuned. Worth stating,
and worth no more than that.

### H39d — the rest is cleaner

- **No load-bearing conjecture.** The hoop conjecture decorates a metaphor; Hawking chronology protection is
  `NOT-RUN` *by design*, and **H35** deliberately reaches its result without it.
- **Rival prescriptions handled correctly.** D-CTCs and P-CTCs disagree elsewhere, so the conclusion was
  built to survive **both** plus the classical case.
- **One structure asserted:** the spin-2 amplitude `A = 2(p·p')² − p²p'²`, taken as the standard
  one-graviton numerator. It reproduces four known cases — **evidence, not derivation**.
- **One citation second-hand:** Barker–Bhatia–Gupta, flagged where it lives.

| | `provenance.py` |
|---|---|
| status | **AUDIT** — 27 load-bearing claims classified across 9 statuses |
| new? | that the headline is MODEL and the refusals are THEOREM; that three quotable identities are one definition |
| **not** claimed | completeness — it covers what the project headlines, not all 513 index findings |

---

## ★★★ H40 — the certification, done. **The obstruction stops being a model.**

> M: *"if we close the gaps, we may get a different conclusion entirely."*

**The gap was real and closing it did change the conclusion — not the verdict, the *status*.**

### H40a — prior art, first, because it goes against us

**Pfenning & Ford, gr-qc/9702026 (1997).** Ford–Roman applied to Alcubierre with sampling below the
curvature radius gives `Δ ≤ 10² v_b L_Planck` — *"the wall thickness cannot be much above the Planck
scale"* — then `E ~ −3×10²⁰ M_galaxy·v_b`, *"ten orders of magnitude greater than the total mass of the
entire visible universe."*

**That is H37's conclusion, twenty-eight years earlier.** H37 needed this row and did not have it.

One number of theirs is worth keeping: an Alcubierre bubble the size of **one electron Compton
wavelength** costs `−400 M_sun`. A Planck cell here costs **196 MJ**. Same verdict, architectures ~10⁴⁷
apart. And their own gap is in their own paper — they apply the *flat-space* inequality to a curved metric
because the exact treatment *"would be exceptionally difficult."*

### H40b — the ansatz, certified, and it refutes our own architecture story

A stdlib reimplementation of Warp Factory's test (arXiv:2404.03095), **validated first**: Minkowski
`max|T| = 0.000e+00` exactly; Schwarzschild isotropic vacuum `4.08e-10` at `r=5`, `3.99e-12` at `r=50`.
That is the noise floor.

| r | T₀₀ | NEC min | WEC min | SEC min | DEC |
|---|---|---|---|---|---|
| 0.05 | −3.089e2 | −3.934e2 | −2.182e3 | −1.985e3 | **VIOL** |
| 1 | −4.656e-4 | −8.735e-4 | −4.625e-3 | −4.184e-3 | **VIOL** |
| 10 | −4.074e-8 | −8.004e-8 | −4.219e-7 | −3.814e-7 | **VIOL** |

**Every condition, every radius**, six orders above the floor (converged: `6.4e-9` change between
`h = 1e-3` and `1e-4`).

> **The seat/lead split does not survive.** `reverse.py` and `apply.py` say the seat is free and only the
> lead needs `ρ < 0`. The metric says the exotic requirement sits **wherever `Φ` varies**. The mechanism is
> the ansatz itself: in conformastatic form the density is dominated by `−|∇Φ|²` — measured `−4.8455e-4`
> against `−3.9952e-4`, ratio 1.21. **A square carrying a minus sign.**

*Correction, recorded not dropped:* a first run of mine concluded "both signs of `m` give `T₀₀ < 0`". At
`r = 0.05` with `m < 0` it is **+30.92**. The far field is gradient-dominated and sign-blind; the near core
is not.

### H40c — and then the ansatz-free version, which is the result

Drop `Φ` entirely. Any static spherically symmetric spacetime, in areal radius with the Misner–Sharp mass:

`ds² = −e^{2Φ}dt² + dr²/(1 − 2m(r)/r) + r²dΩ²`,  with `dm/dr = 4πr²ρ` **exactly**.

Proper radial distance is `dl = dr/√(1 − 2m/r)`, so it is shorter than flat exactly when `m(r) < 0`.

> **THEOREM. In any static spherically symmetric spacetime, proper distance is contracted at `r` if and
> only if the enclosed Misner–Sharp mass — the volume integral of `ρ` — is negative.**
>
> No ansatz. No `Φ`. A definition and one integral.

**This removes the MODEL status from the central requirement**, which is precisely what **H39a** asked for.
It constrains a **different quantity** from the one the quantum inequalities bound: Ford–Roman bounds a
*sampled density along a worldline*; this bounds the *volume integral over a ball*. Averaging along a
geodesic is not integrating over a ball — which is why this obstruction survives all of **H37** untouched.

And it does **not** require negative *total* mass. `m(r) < 0` locally is compatible with `M_ADM ≥ 0`; the
concentric shell is exactly the device that arranges it, and the positive mass theorem was never in danger.

### H40d — status, stated before anyone asks

**No novelty is claimed.** Two lines from a standard definition; the flare-out condition is a near
neighbour. Its value is that it is **ansatz-free**. Scope: **static and spherically symmetric only** — the
Alcubierre drive is neither, and D1–D5 place *this* construction inside the theorem's reach. The
certification is finite-difference, quoted against a *measured* floor.

> **The construction is still a MODEL. This proves the requirement, not the design.** H39b's asymmetry is
> unchanged and **sharpened**: the obstruction was the last piece of the NO resting on an ansatz, and now
> it does not.

| | `certify.py` |
|---|---|
| status | **THEOREM-HERE** (the Misner–Sharp result) + **MEASURED** (validated pipeline; four radii, three conditions) + **PRIOR-ART** (Pfenning–Ford) + **CORRECTION** (seat/lead split; my own over-broad sign claim) |
| new? | not the theorem — the *certification*, and the demotion of the seat/lead split |
| **not** claimed | novelty for the theorem; scope beyond static spherical symmetry; that the construction is certified — it is refuted |

---

## ★★★ H41 — what mathematics would reverse the verdict. **One link closed, against us; two of the three famous no-gos do not apply.**

> M: *"What math is needed to reverse the verdict?"*

Not *is it right* — **H40** answered that. What **mathematics**, named and specific, would have to be true
for it to be wrong. A verdict is never one claim: it is a **chain**, and a chain is reversed by breaking
exactly one link.

| | link | breaking it would mean | status |
|---|---|---|---|
| **L1** | **SCOPE** | the theorem does not reach non-spherical geometry | **OPEN** |
| **L2** | **SOURCE** | negative `m(r)` no longer needs negative matter energy | **OPEN** — M's decision |
| **L3** | **RATE** | the same `\|m\|` buys more distance | **CLOSED** — here, against us |
| **L4** | **MAGNITUDE** | the requirement becomes sourceable | **OPEN** — the only one that touches the bill |

### H41a — L3, the rate: closed in this pass, and closed against us

`Δd = |m| ln(r₂/r₁)` was derived in the weak field, where `1/√(1−2m/r) ≈ 1 + m/r`. The obvious hope: the
weak field *understates* the return. Measured ansatz-free by integrating the proper-length deficit
**directly** —

`Δd(m) = ∫_{r₁}^{r₂} [1 − 1/√(1 − 2m/r)] dr`,  `r₁ = 1`, `r₂ = 200`

| `\|m\|` | ratio to `\|m\| ln(r₂/r₁)` | `Δd/(r₂−r₁)` |
|---|---|---|
| 1e−8 | **1.000000** | — |
| 1e−6 | **1.000000** | — |
| 1e−4 | 0.999972 | — |
| 1e−2 | 0.997206 | — |
| 1 | 0.833100 | 0.0222 |
| 10 | 0.504993 | 0.1345 |
| 100 | 0.174544 | 0.4647 |
| 1e3 | 0.029831 | 0.7942 |
| 1e4 | **0.003505** | 0.9332 |

The weak field returns the logarithm **exactly**, ansatz-free. The strong field returns strictly less, and
monotonically, because the integrand is bounded above by 1 — **`Δd` saturates at the coordinate gap**
(93.3 % of it already at `|m| = 1e4`).

> **The weak-field logarithm is not a limitation of the derivation. It is the best case.** Every extra unit
> of `|m|` buys strictly less than the one before it, so the exchange rate `c⁴/(GΛ)` is a **floor** on the
> cost, not an artefact of an expansion.

*Method note, recorded:* the first measurement differenced two proper lengths ≈ 199 apart, lost every digit
in the weak field, and reported a spurious **63×** gain at `|m| = 1e−6`. Integrating the deficit directly
gives 1.000000.

### H41b — a door: which no-go is actually doing the work

**H40c** put the requirement on a **ball** integral, `∫_ball ρ dV < 0`. Every averaged energy condition
bounds a **worldline** integral, `∫_line ρ dl`. Two different functionals of the same `ρ` — and whether one
constrains the other is answerable by arithmetic. **It does not.**

Two-zone profile: `ρ = −b` for `r < r₀`, `+a` for `r₀ < r < R`, `0` outside; `r₀ = 1, R = 2, b = 1, a = 1.5`.

| quantity | closed form | value |
|---|---|---|
| `m(r₀)` | `−(4/3)πb r₀³` | **−4.188790** — contraction at `r₀` |
| `m(R)` | `+(4/3)π(9.5)` | **+39.793507** — ADM-safe |
| deepest chord, `p = 0` | `2[a(R−r₀) − b r₀]` | **+1.000000** |
| min over all `p` | grazing chord, misses the body | `0` |

And the margin does not shrink: hold `a = 1.5b` and raise `b` —

| `b` | `m(r₀)` | chord(0) |
|---|---|---|
| 1 | −4.1888e0 | +1.0000e0 |
| 10 | −4.1888e1 | +1.0000e1 |
| 100 | −4.1888e2 | +1.0000e2 |
| 1000 | −4.1888e3 | +1.0000e3 |

Both exactly linear in `b`: **`m(r₀) → −∞` while every chord integral → `+∞` simultaneously.**

> **Scope, tightly, because this is easy to over-read.** Flat-space kinematics — a statement about two
> integrals as functionals of a density, **not** a solution of the field equations; the chords are straight,
> not geodesics; and `ρ < 0` in the core means the **pointwise** WEC fails there, as it must, since that is
> what is being asked for.

What it establishes anyway:

- **The positive mass theorem does not forbid this** — total mass is positive.
- **ANEC does not forbid this** — it is satisfied, and it is not even the right *shape* of constraint.
- **The whole weight is on the local, sampled bound**: Ford–Roman and its descendants — **H37**'s magnitude
  gate, **H40a**'s Pfenning–Ford. This pass's contribution is to show it is load-bearing *alone*.

### H41c — the three links that stay open, and none of them is engineering

**L1 — SCOPE.** `certify.py` states its own hypothesis: the proof needs an **areal radius**, and outside
spherical symmetry there is no such coordinate, so `m(r)` has no definition and the biconditional has no
statement. *Not false — unstated.* What would break it: a **quasi-local mass** for a closed 2-surface that
(a) reduces to Misner–Sharp on round spheres and (b) controls proper distance the same way. **Hawking mass**
gives (a) by construction. **Geroch monotonicity / Huisken–Ilmanen** — `m_H` non-decreasing under inverse
mean curvature flow when `R ≥ 0`, the machinery of the Riemannian Penrose inequality — is the closest
existing thing to (b). **Bartnik mass** is the right variational object and is notoriously incomputable. The
direction that would help is the one Geroch does *not* give. **Open in the literature, not merely here.
Not attempted here** — attempting it is a differential-geometry programme, and claiming otherwise is the
exact fault **H39** was built to catch.

**L2 — SOURCE.** `m(r)` is the *geometry's* mass; identifying it with the *matter's* energy is
`G_μν = 8πT_μν` and nothing else. In `f(R)`, scalar–tensor or Einstein–Gauss–Bonnet the equations rearrange
to `G_μν = 8πT^matter_μν + T^eff_μν`, and an effective term can be negative where the matter term is not.
**This is `wormhole.py`'s `SCOPE_CHOSEN_HERE = None`** — a flag asserted `None` in its own selftest so that
nobody, including me, can quietly decide it, and it has stood unchanged for the whole project. It is a scope
decision about what counts as proven against M's standing constraint *"true and proven in its math"*.
**M's call. This pass does not change the flag.**

**L4 — MAGNITUDE.** Requirement `|ρ| ~ c⁴/(GΛR²)` goes as `R⁻²`; Ford–Roman `3ħc/(32π²L⁴)` and Casimir
`π²ħc/(720d⁴)` go as `L⁻⁴`. Different exponents, so the shortfall **grows as `R²`** and the crossovers sit
at `0.307933 ℓ_P` and `0.369917 ℓ_P`. The one candidate whose exponent matches is **candidate D**,
non-minimal coupling: **Fewster & Osterbrink (arXiv:0708.2450)** — for `ξ > 0` there is *no*
state-independent QEI, so the bound that forbids us does not exist in that theory; **Fliss, Freivogel,
Kontou et al. (arXiv:2309.10848)** — EFT bound `|ρ| ~ ħc/(ℓ_UV²δ²)`, **`δ⁻²`, the same exponent**. The
shortfall then collapses from a growing function to the pure number `(ℓ_UV/ℓ_P)²/Λ`, closing at
**`√Λ ℓ_P = 3.159514 ℓ_P`** — a factor of three in the UV cutoff, not twenty orders. What is needed: a QEI
for non-minimally coupled fields in curved spacetime, state-independent enough to be a bound and `R⁻²`
enough to be the right shape, **derived rather than scaling-argued**. Active literature; the sign of the
answer is not known.

### H41d — the answer, short

> **No measurement reverses this. No power source reverses this.** What reverses it is **one of three
> theorems**, none of which is known to be false — and the cheapest of the three is a **decision M has been
> holding since `wormhole.py`**, not a discovery anyone has to make.

| | `overturn.py` |
|---|---|
| status | **MEASURED** (L3, ansatz-free, closed-form-validated) + **THEOREM-CITED** (Hawking/Geroch/Huisken–Ilmanen/Bartnik; Fewster–Osterbrink; Fliss et al.) + **ARITHMETIC** (ball vs chord independence) + **OPEN** (L1, L2, L4) |
| new? | the L3 saturation result and the ball-vs-chord independence; *not* the no-gos, *not* the quasi-local mass programme |
| **not** claimed | that the two-zone profile is a solution; that ANEC-compatibility makes the requirement attainable; any resolution of L1, L2 or L4 |

---

## ★★★ H42 — the coefficient census. **Two undefined numbers, both in L4 — and `Λ` exists because M's endpoint rule fails.**

> M: *"The clues lay in the undefined/underived coefficients… Knowing what a coefficient **is** allows us to know the inputs, what is interchangeable. I predict that coefficients are what changes in a transition state. And the difference between two locations in spacetime is the difference in the coefficients of each endpoint of the corridor."*

Five claims, separated before they are tested.

| | claim | verdict |
|---|---|---|
| **C1** | the clue is in the undefined coefficients | **LANDS** |
| **C2** | derive coefficients up to theorem, better to law | **PARTIAL** |
| **C3** | knowing a coefficient tells you what is interchangeable | **LANDS — and it does not help** |
| **C4** | a transition state is a change of coefficients | **TRUE BUT THIN** |
| **C5** | location difference = endpoint coefficient difference | **EXACTLY HALF** |

### H42a — the census: `provenance.py` for numbers rather than claims

**H39** sorted the project's *claims* by how they were come by. It never sorted the *numbers* — and a
number is where an unearned assumption hides best, because a number does not look like an assertion.
**Twenty-five coefficients carry this framework.**

| status | n | what |
|---|---|---|
| LAW | 1 | `8π`, fixed by the Newtonian limit |
| GEOMETRIC | 1 | `4π`, the solid angle in `dm/dr = 4πr²ρ` |
| THEOREM | 7 | `8`, `4`, `120°`, the `1/2` CTC window, Ford–Roman, Casimir, `√Λ` |
| IDENTITY | 3 | `2/Λ`, `Λ/2`, `E_P/Λ` |
| MEASURED | 2 | the two sub-Planckian crossovers |
| EMPIRICAL | 3 | `G`, `c`, `ħ` |
| MODEL-PARAM | 4 | `a`, `R_s`, `b`, `m` — the ansatz's free inputs |
| **MODEL** | **1** | **`Λ` itself**, and the exchange rate inherits it |
| ASSERTED | 1 | the `2` in `A = 2(p·p′)² − p²p′²`, still flagged from **H39** |
| **UNDEFINED** | **2** | **`ξ` and `ℓ_UV`** |

> **And both undefined coefficients sit in L4** — the only link of **H41**'s chain that touches the bill.
> `ξ` is the non-minimal coupling the framework needs positive (Fewster–Osterbrink: no state-independent
> QEI there — candidate D's entire hope), and nothing here fixes a value. `ℓ_UV` is the EFT cutoff in
> Fliss et al., the one bound whose exponent matches, closing at `√Λ ℓ_P`.

**C1 lands**, and not mystically: an undefined coefficient *is* a free parameter, and a free parameter is
exactly where a no-go can fail to bind.

### H42b — C5, measured on both metric coefficients

`ds² = −e^{2Φ(r)}dt² + dr²/(1 − 2m(r)/r) + r²dΩ²`. A static spacetime has two independent coefficients, and
M's rule is true of one and false of the other.

**TIME — C5 holds, exactly.** `1 + z = √(g_tt(r₂)/g_tt(r₁)) = e^{Φ(r₂)−Φ(r₁)}` — a **difference of the
potential at the two endpoints**, independent of everything between. Three `Φ` profiles agreeing only at
their ends give identical redshift **to machine precision**. M is right about time, and right for his own
reason: `g_tt` enters the observable as an **endpoint ratio**.

**SPACE — C5 fails.** `Δd = ∫[1 − 1/√(1 − 2m(r)/r)]dr` is a **line integral**, and the map
(endpoint coefficients) → `Δd` is not even well defined:

| profile | `m(r₁)` | `m(r₂)` | `Δd` |
|---|---|---|---|
| `m_A = m₀` | −1 | −1 | **4.414026389** |
| `m_B = m₀ + ε sin²(π(r−r₁)/(r₂−r₁))` | −1 | −1 | **5.540580582** |

**Every** metric coefficient at **every** endpoint identical. **25.5 % different distance.** *Kinematic — a
statement about metrics, not a claim that either profile solves the field equations with a sensible matter
model.*

### H42c — and that is **why there is a `Λ`**

This is the part worth having, because it *explains* a coefficient rather than classifying it.

> A quantity that **is** an endpoint difference has no coefficient of its own — it is read off the ends and
> there is nothing to integrate. A quantity that is a **line integral must carry one**: the number saying
> how much the path contributed. **`Λ` is that number** — not a fudge factor, not a fitted constant — and
> its form is a **logarithm** because the integrand goes as `1/r`. **`Λ` exists precisely because C5 fails.**

Three things follow that were already in the tree without the reason:

- **H39a's verdict that the headline is MODEL was never about carelessness. It was structural.** A path
  integral cannot be ansatz-free the way an endpoint ratio can — it needs the whole path, so it needs a `Φ`.
- **H40c** is a *ball* integral and **H41b** is that a ball integral is not a line integral. **Both are
  integrals.** Nothing in the obstruction is an endpoint quantity, which is exactly why no endpoint
  bookkeeping escapes it.
- **H41a**'s saturation — the logarithm is the best case — *is* the saturation of that same integral. **A
  difference cannot saturate. An integral with a bounded integrand must.**

### H42d — C3: what is interchangeable, and why it does not help

`Λ = 2[ln(2R_s/√(b²+a²)) − 1]` takes **three** inputs through **one** combination:

`X = 2R_s/√(b²+a²) = 399.920024` as seated.

Any change preserving `X` leaves `Λ` **bit-for-bit identical** — scaling all three together returns
`9.982529174194637` to all fifteen digits at `k` = 1, 7, 1000. **`Λ` is scale-free in the geometry**, so the
answer to "what is interchangeable" is the whole surface `X = const`.

And the leverage is logarithmic, which is to say there is none:

| | needs |
|---|---|
| `Λ × 2` | `X × 1.4712e2` |
| `Λ × 10` | `X × 3.2293e19` |
| `Λ × 100` | `X × 3.9828e214` |

> **A factor of ten in the exchange rate costs a factor of 3×10¹⁹ in the geometry.** There is no geometric
> engineering out of this: the one coefficient that sets the bill is the one input that cannot be moved, and
> the four MODEL-PARAMs are free to choose and inert to change.

### H42e — C4, and scope

**C4 is true and nearly tautological** in GR — a change of gravitational state *is* a change of metric
coefficients. It earns content only in the sharpened form the two measurements give it:

> A transition changes **both** coefficients, and they buy different things. Changing `g_tt` buys **time**
> and is paid **at the endpoints**. Changing `g_rr` buys **distance** and is paid **along the whole
> corridor.**

*That is **not** the seat/lead split — **H40b** killed that — and must not be read as reviving it. It is the
older, more basic split between a potential and a length.*

| | `coefficients.py` |
|---|---|
| status | **CENSUS** (25 coefficients, 10 statuses) + **MEASURED** (C5 both halves, kinematic) + **EXPLANATION** (why `Λ` is an integral and therefore MODEL) |
| new? | the census; the C5 half-refutation; the structural reading of **H39a** |
| **not** claimed | that either C5 profile solves the field equations; completeness of the census beyond this framework; any repair — C5 is recorded half-refuted, not corrected |

---

## ★★★ H43 — the math that controls magnitude. **`R·Δd ≤ k ℓ_P²` — an area law, and `Λ` is the exchange rate between the two denominations.**

> M: *"Two planes of travel, two denominations of currency… We now need to identify the math that controls magnitude in all this, so price/size of transition state corridor can scale under control."*

**The math is an exponent, and the control law is a hyperbola.**

### H43a — both denominations priced, and `Λ` is the rate between them

| denomination | bought by | paid | price | `R`-dependence |
|---|---|---|---|---|
| **distance** | `g_rr` | along the corridor | `c⁴/(GΛ)` = **1.212374e43 J/m** of `Δd` | **none** |
| **time** | `g_tt` | at the endpoints | `c⁴/G` = **1.210256e44 J** per unit `ΔΦ` per metre of `R` | **linear** |

> **The ratio of the two prices is `Λ` — exactly, to fourteen digits.** For the same amount measured in
> metres, **time costs `Λ` times more than distance.** `Λ` is not only the coefficient of the corridor
> integral (**H42c**); **it is the exchange rate between the two currencies** — the job its name always
> implied, and which no pass before this one measured.

Distance is `R`-independent because `Λ` is scale-free in the geometry (**H42d**). So **the two denominations
scale oppositely** and no single corridor size optimises both. A trade, not a free lunch.

**And one denomination is not obstructed at all.** A potential *well* redshifts clocks and is made of
**ordinary positive mass** — every gravitating body in the universe buys time-currency and none violates an
energy condition. Only the opposite sign, a potential *hill*, needs what distance needs.

> **The exotic requirement lives entirely in one denomination.** And the honest other half: **time dilation
> changes elapsed proper time, not position.** "Both planes travelled simultaneously" is exact as a
> statement about *inputs* — the two metric coefficients are independent and both may be driven at once —
> and is **not** a statement about arriving anywhere sooner.

### H43b — the scaling census: what controls magnitude is an exponent

| | **A**: hold `Δd` fixed | **B**: hold `Δd/R` fixed |
|---|---|---|
| mass `M`, energy `E` | `R⁰` | `R¹` |
| `ρ` **required** | `R⁻³` | `R⁻²` ← **H37**'s seated gate |
| `ρ` **permitted** (`R⁻⁴` bounds) | `R⁻⁴` | `R⁻⁴` |
| **shortfall** | **`R¹`** | **`R²`** |
| `Λ` | `R⁰` | `R⁰` |

**Both exponents positive** ⟹ small is the only direction in both regimes, and **A is strictly better than
B**. A zero exponent would be the prize — it would mean size does not matter. Nothing here has one except
**H43d**.

### H43c — the area law, and it validates itself

Set required = permitted in regime A:

> **`R · Δd ≤ k ℓ_P²`**  — corridor length times distance bought, bounded by a **Planck area**.
>
> `k_FR = 3Λ/(32π²) = 0.094823` · `k_Cas = π²Λ/720 = 0.136838` — **two unrelated bounds, same Planck area to
> within 44 %.**

**The validation, and it is the reason to believe this.** Put `Δd = R` — the diagonal, contracting a
corridor by its own length — and the law becomes `R² ≤ kℓ_P²`:

| | `√k` | **H37**'s seated crossover |
|---|---|---|
| Ford–Roman | **0.307933 ℓ_P** | **0.307933 ℓ_P** |
| Casimir | **0.369917 ℓ_P** | **0.369917 ℓ_P** |

Six decimals, both. **They were two points; this is the curve they sit on.** A strict generalisation of a
result already in the tree, not a new claim on new assumptions — and the one place a chain of scalings is
pinned to a number computed another way.

| `Δd` | `R ≤` |
|---|---|
| `ℓ_P` | `0.094823 ℓ_P` |
| 1 fm | 2.4770e−56 m |
| 1 m | **2.4770e−71 m** |
| 1 ly | 2.6182e−87 m |

> **Scaling is controlled, and the control law is exact — which is what M asked for. The whole controlled
> region sits under a Planck area.**

*No novelty claimed.* A Planck-area bound on a product is the shape of **H40a**'s Pfenning–Ford; the
resemblance to a Bekenstein-type area bound is **noted and not asserted** — nothing here derives it from
entropy.

### H43d — candidate D inverts the law, and the exponent goes to zero

Every bound above falls as `R⁻⁴`. Fliss et al. fall as `R⁻²` — the one exponent matching the requirement's.
Redo the same calculation:

> **`R ≥ Δd · (ℓ_UV/ℓ_P)²/Λ`** — **the inequality has reversed.** A *minimum* on `R`, and **`ℓ_P²` has
> cancelled out entirely.**

The controlling quantity is the pure number `(ℓ_UV/ℓ_P)²/Λ` — **exactly the shortfall of H41c**, now
carrying a meaning it did not have:

> **The shortfall *is* the minimum ratio of corridor length to distance bought.**

| `ℓ_UV` | bound | |
|---|---|---|
| `ℓ_P` | `R ≥ 0.100175 Δd` | already **vacuous** |
| **`√Λ ℓ_P`** | **`R ≥ 1.000000 Δd`** | **exactly the kinematic bound** |
| `10 ℓ_P` | `R ≥ 10.017501 Δd` | real but mild |

At the closing value the quantum constraint **coincides with the constraint geometry already imposes** —
**H41a** proved `Δd` saturates at `r₂−r₁`, i.e. `R ≥ Δd` for free. **It becomes vacuous and size stops
mattering.**

> **This is not a second derivation of `√Λ ℓ_P` and must not be read as one.** The same dimensionless group
> appears in both places because it is the same calculation seen from two sides. What is gained is an
> *interpretation*, not corroboration.

And it rests entirely on `ℓ_UV` — one of the exactly two coefficients **H42a** found that nothing here
fixes. **Third independent arrival at the same L4.**

| | `magnitude.py` |
|---|---|
| status | **DERIVED** (the area law, from cited bounds + a scaling step) + **VALIDATED** (diagonal vs two seated crossovers, 6 dp) + **IDENTITY** (`Λ` as the denomination rate) + **INTERPRETATION** (the shortfall as a length ratio) |
| new? | the area law as a curve; `Λ` as the exchange rate between denominations; the sign flip under `R⁻²` |
| **not** claimed | novelty for a Planck-area bound; that it is a Bekenstein bound; a second derivation of `√Λ ℓ_P`; any value for `ℓ_UV` |

---

## ★★★ H44 — every coefficient solved. **Three debts close, one cannot, and what is left is one question that is not a number.**

> M: *"Solve for ALL coefficients and we have a math chain with no questions left to ask. All answers contained, with only constants, determinant variables, and actionable math mechanisms."*

**H42** censused twenty-five coefficients and left four kinds of debt: one ASSERTED structure, two UNDEFINED
numbers, one MODEL, four MODEL-PARAMs. This pays what can be paid.

### H44a — the ASSERTED coefficient, derived — and it corrects a seated claim

One-graviton exchange is `T^{μν}(1) P_{μναβ} T^{αβ}(2)` with the de Donder numerator
`P = ½(η_{μα}η_{νβ} + η_{μβ}η_{να}) − (1/(D−2))η_{μν}η_{αβ}`. For `T^{μν} = p^μp^ν`:

> **`A = 2(p·p′)² − (2/(D−2)) p²p′²`.** The **2** is the propagator's **symmetrisation** — the two terms of
> `½(ηη + ηη)` each contribute `(p·p′)²`. The **−1** is the trace term at **D = 4**, where `2/(D−2) = 1`
> exactly. **ASSERTED → THEOREM-CITED.** **H38**'s pre-registered 8 now stands on a derivation, not a sample.

**And the derivation breaks something**, which is why it was worth doing. **H36** seats *"the factor is 8 in
D = 3 through 26… D does not appear in `2(p·p′)² − p²p′²` anywhere."* The reason given is correct and it is
the problem — **D does not appear because the D = 4 propagator was used in every D.**

| D | trace `2/(D−2)` | static norm | antiparallel | parallel | **ratio to Newton** |
|---|---|---|---|---|---|
| 3 | 2 | **0** | 8 | 0 | **UNDEFINED** |
| **4** | **1** | 1 | 8 | 0 | **8** |
| 5 | 2/3 | 4/3 | 8 | 0 | 6 |
| 8 | 1/3 | 5/3 | 8 | 0 | 24/5 |
| 10 | 1/4 | 7/4 | 8 | 0 | 32/7 |
| 11 | 2/9 | 16/9 | 8 | 0 | 9/2 |
| 26 | 1/12 | 23/12 | 8 | 0 | 96/23 |

**The antiparallel 8 and the parallel 0 are genuinely dimension-independent and survive untouched** — nulls
have `p² = 0`, so the trace term drops out in every `D`. **What fails is the *ratio*,** because the Newtonian
normalisation is `D`-dependent.

> **`D = 3` is the check that this is right rather than an algebra slip:** the static amplitude **vanishes**
> there — the known fact that 2+1 gravity has no Newtonian attraction, a result nothing here put in, produced
> by the corrected propagator on its own.

**And it cuts the way the tree already cut.** **H36** used dimension-independence to *refute* the "8 is 8
dimensions" reading. The refutation **strengthens**: a factor occurring in exactly one dimension is even less
a statement about dimension than one occurring in all of them. *(The `9/2` at D = 11 matching **H36**'s
stationary point is a coincidence of small integers, flagged so it is not mistaken for a finding.)*

### H44b — both UNDEFINED coefficients take principled values, and L4's **numbers** close

**`ξ`** is not a free dial. One value is picked out by a symmetry: `ξ_c = (D−2)/(4(D−1)) = **1/6**` exactly in
D = 4, where the massless scalar action is conformally invariant. And `1/6 > 0`, so **the value a symmetry
picks sits inside Fewster–Osterbrink's regime** — which it did not have to.

**`ℓ_UV`** is the cutoff of an EFT *of gravity*. Its natural value is the scale at which that theory fails:
**`ℓ_P`**.

**H43** showed all of L4 is controlled by one group, `(ℓ_UV/ℓ_P)²/Λ`:

| `ℓ_UV` | shortfall | |
|---|---|---|
| **`ℓ_P`** (natural) | **0.100175** | **< 1 — the requirement is met** |
| `√Λ ℓ_P` | 1.000000 | exactly the kinematic bound |
| `10 ℓ_P` | 10.017501 | a real constraint |

At the natural cutoff the inverted area law reads `R ≥ 0.100175 Δd` — **weaker than `R ≥ Δd`, which H41a
proved for free from geometry.** The quantum constraint on corridor size is not merely satisfiable; **it is
vacuous.** Factor of ten to spare.

### H44c — and the **status** does not close. This is the finding.

`|ρ| ~ ħc/(ℓ_UV²δ²)` is an **EFT scaling estimate** with an unfixed O(1) coefficient, not a derived
inequality. What kind of object *can* it be? Fewster–Osterbrink settles it:

> **For a scalar with `ξ > 0` there is no state-independent quantum energy inequality.**
>
> That theorem is the entire reason candidate D is allowed. **It is also the entire reason nothing in that
> theory can be *proved* allowed** — a relation that is not state-independent is not a bound, and what is not
> a bound can be neither satisfied nor violated, only estimated.
>
> **THE SAME THEOREM THAT REMOVES THE OBSTRUCTION REMOVES THE PROOF THAT IT IS REMOVED.**

And `ξ = 1/6` is in that regime *by construction*, so this is not avoidable by choosing differently.

> ⚠️ **CORRECTED BY H45, AND THE CORRECTION IS SUBSTANTIAL.** The clause *"a relation that is not
> state-independent is not a bound"* is **withdrawn**. Fewster–Osterbrink's Theorem 4.2 **does** derive a
> QEI for non-minimal coupling — state-dependent, proved non-trivial by their Theorem 5.1, valid for
> `0 < ξ ≤ 1/4`, which **contains the `1/6` H44b chose**. A state-dependent bound *is* a bound. **L4 is a
> computation, not an impossibility.** What survives unchanged: no *state-independent* QEI exists for
> `ξ > 0`, and they show it by an explicit Hadamard state rather than by failing to find one. See H45.

### H44d — `Λ` cannot close; its **sign** closes exactly

`Λ` is the value of an integral **along the corridor** (**H42c**), which needs the whole path and therefore a
`Φ`; and **H40b** shows the seated `Φ` is not the one that solves anything. **`Λ` is a functional of an
unknown and stays MODEL until someone solves the field equations.** No coefficient work reaches it.

What does close, and this tree had never stated it:

> **`Λ = 2[ln X − 1] = 0` at `X = e` exactly.** There is a contraction rather than a dilation **iff**
> `X = 2R_s/√(b²+a²) > e`, i.e. **`R_s/√(b²+a²) > e/2 = 1.3591409142295225`.** A threshold in the design
> space, in closed form. Seated at `X = 399.920024`, far above.

And the **form** is derivable where the value is not: any potential falling as `1/r` integrates to a
logarithm. **Shape and sign: THEOREM. Value: MODEL.**

### H44e — the chain M asked for

| | |
|---|---|
| **CONSTANTS** | `G`, `c`, `ħ`, `8π`, `4π` |
| **SOLVED HERE** | the `2` (propagator) · `ξ = 1/6` (conformal) · `ℓ_UV = ℓ_P` (EFT cutoff) |
| **NOT SOLVABLE** | `Λ`'s value — structurally |
| **DETERMINANT VARIABLES** | `X`, `m`, `R`, `Δd` |
| **CONSTRAINTS** | `X > e` · `m/a = Φ(0) ≤ 1` · `Δd ≤ R` · `R·Δd ≤ kℓ_P²` (under `R⁻⁴` bounds only) |
| **QUESTIONS LEFT** | **one**, and **it is not a number** |

> **Solving every coefficient does not leave zero questions. It leaves exactly one, no further coefficient
> work touches it, and it asks what kind of object an estimate is.** That is a better place to stand than an
> open value — **a value can be argued and a status cannot.** Fourth arrival at L4, from the only direction
> that could exhaust it.

| | `solve.py` |
|---|---|
| status | **THEOREM-CITED** (the propagator) + **DERIVED** (`Λ`'s sign threshold, exact) + **PRINCIPLED CHOICE** (`ξ`, `ℓ_UV`) + **CORRECTION** (H36's dimension claim) |
| new? | the sign threshold `X > e`; the status/value split at the terminus. *Not* the propagator — textbook |
| **not** claimed | novelty for the propagator; that `ξ` and `ℓ_UV` are *derived* rather than chosen on principle; that L4 is closed — its numbers are, its status is not |

---

## ★★★ H45 — the Millennium problems, surveyed. **One bears and it is the solved one — and the survey corrected H44.**

> M: *"Some famously unsolved math that may hold the keys to what we are hoping to achieve — the millennium problems by The Clay Mathematics Institute."*

### H45a — the correction, first, because it goes against the last pass

Doing the survey properly meant **reading Fewster–Osterbrink rather than citing it**, and the paper
contradicts what **H44c** was built on.

> ❌ **WITHDRAWN:** *"a relation that is not state-independent is not a bound, and what is not a bound can be
> neither satisfied nor violated, only estimated."*
>
> ✅ **Their abstract:** *"Nonetheless, we derive a generalised QEI for the non-minimally coupled scalar
> field, in which the lower bound is permitted to be state-dependent. This result applies to general
> globally hyperbolic curved spacetimes for coupling constants in the range `0 < ξ ≤ 1/4`."*

**A state-dependent bound is a bound.** Their Theorem 4.2 proves it; their Theorem 5.1 proves it
**non-trivial**. And the range was built to contain the special values — the paper names conformal coupling
`(n−2)/(4n−4)` and supersymmetric coupling `1/4` — so **it contains the `1/6` H44b chose.**

> **L4 is a COMPUTATION, not an impossibility.** Not *"is there a bound"* — there is one, proved, covering
> our coupling. The open question is what it says for a specified state, which nobody here has evaluated.
> Fewster's own conclusion points the same way: *"in general, then, the aim should be to establish
> non-trivial state-dependent bounds."*

**What survives H44c unchanged:** no *state-independent* QEI exists for `ξ > 0` — and they show it by an
**explicit Hadamard state** (energy density `−ξ(2κ)⁴/(3π²)` at the origin, extended to `j` particles to beat
any `−ρ₀` over any ball), not by failing to find one.

### H45b — and the corrected reading is **worse** for us

Three results in that paper reproduce this project's obstruction **from the QFT side**, independently:

| their result | ours |
|---|---|
| *"the product of `κ′` and `τ′` is constant… large regions of negative energy density **albeit with low magnitude**"* | **H43c**'s area law `R·Δd ≤ kℓ_P²` — size × magnitude fixed |
| lower bound holds for `p > 2`, energy density unbounded above for `q < 3` — **an exponent gap ≥ 1 in powers of `H`** | **H37**'s magnitude gate *is* an exponent gap |
| **AWEC holds** for `ξ ∈ [0, 1/4]` | **H41b**: the averaged condition is satisfied; the obstruction is elsewhere |

> *"Negative energy effects with large magnitude, while possible over large regions, **require more energy to
> achieve** than positive energy densities of the same magnitude, and the 'energy budget' for these two
> effects will **grow with a different power**."*

**The shapes recur. They are not the same statements and nothing here claims they are.**

One number the paper gives that nothing here had: **their total energy goes as `1/ξ`**, so within the
theorem's range the *cheapest* coupling is the *largest*. **Symmetry picks `1/6`; cost picks `1/4`; `1/6`
costs `3/2` of `1/4`.** Recorded, not resolved.

### H45c — the seven

| problem | | verdict | link |
|---|---|---|---|
| **Poincaré** | **SOLVED** | **BEARS** | **L1** |
| Yang–Mills existence & mass gap | open | adjacent, independent | L4 |
| Navier–Stokes existence & smoothness | open | real link, no bearing | — |
| P vs NP | open | real link, no bearing | — |
| Riemann hypothesis | open | **no bearing** | — |
| Hodge conjecture | open | **no bearing** | — |
| Birch–Swinnerton-Dyer | open | **no bearing** | — |

**Poincaré bears.** Perelman closed it with **Ricci flow and monotone functionals**, and monotonicity along a
geometric flow is precisely what **H41c**'s L1 needs. The paradigm is *already inside GR*: Geroch, Jang and
Jang–Wald found Hawking-mass monotonicity under **inverse mean curvature flow** with `R ≥ 0`, and
Huisken–Ilmanen (2001) built the **weak** IMCF theory that carries it through singularities — which is how
the **Riemannian Penrose inequality** was proved. Still live (Hirsch, arXiv:2210.12237, extends it to initial
data sets).

**Yang–Mills is adjacent and independent.** Rigorous QEIs exist exactly where constructive QFT has succeeded
— free fields, and interacting ones **only in 2D** (CFTs with a stress tensor, integrable models with
factorising S-matrices). The missing 4D interacting case **is** the Yang–Mills problem. **But L4's field is
free** and already rigorously constructed; the obstruction is the `ξ`-term, not construction. **Solving
Yang–Mills would not touch L4.**

**Navier–Stokes has an exact dual and no bearing.** Bredberg–Keeler–Lysov–Strominger construct, for *every*
incompressible NS solution in `p+1` dimensions, a **uniquely associated solution of the vacuum Einstein
equations in `p+2`**. A Millennium problem literally embedded in the Einstein equations — and irrelevant here
for two independently sufficient reasons: **the dual is `T_μν = 0`** while every question here is `T_μν < 0`,
and `p+1 → p+2` does not pair 3+1 with 3+1.

**P vs NP runs the wrong way.** Aaronson–Watrous proved `P^CTC = BQP^CTC = PSPACE` under **Deutsch's**
consistency condition — the one **H34**'s `closure.py` used. So this project's refusal of definite closure is
**evidence on the physics side of a complexity question**, not a tool on ours.

**Riemann, Hodge, BSD have no bearing**, and the Riemann refusal is placed on the record deliberately: no
zeta, no spectral counting, no prime distribution anywhere in this tree. **A claimed connection would be
numerology.**

### H45e — September 2026: a claimed solution, checked

A claim reached this session that Navier–Stokes had been **solved by Claude through another user**, was held
in **infrastructure available here**, and was **on the Clay Institute's website**. Checked rather than
accepted. It has a real kernel and a false core.

**Real.** On **2026-09-07** Tristan Buckmaster (NYU) and **Levent Alpöge — an Anthropic researcher** — posted
three preprints proving **finite-time blowup with a smooth forcing term** for the incompressible porous
medium equation, the 2D Boussinesq system and the **3D incompressible Euler** equations, **Lean-formalised**.
Buckmaster's statement describes ~1 year of collaboration using **Claude** and Codex, a breakthrough on
2026-08-15, Lean verification on 2026-08-22. Tao: *"a remarkable achievement"*, and it **could help** solve
Navier–Stokes. Separately, **2026-09-08**, OpenAI claimed a Lean-verified ~100-page blowup proof for the
**forced** Navier–Stokes equations — contested (Buckmaster has not seen it), and **they do not intend to
claim the prize**.

**Not the Clay problem, for two independently sufficient reasons.**

1. **Euler is not Navier–Stokes** — no viscosity. Boussinesq and IPM are neither.
2. **Forced is not unforced**, which is what Clay asks. Palasek has identified the obstacle to transferring
   the mechanism: unforced, viscous energy loss overwhelms the growth.

> H45c's row stands unchanged at *open / real-link-no-bearing*.

**⚠️ Corrected an hour after first seating, and by the user, not by an instrument.** This section originally
said the result *"is not on their site as solved."* **That was asserted without access** — `claymath.org` is
egress-blocked from this session, the claim rested on secondary summaries, and the right answer was *"I
cannot check this."* **CMI posted a news item on 2026-09-11**, and its wording is the finding:

> *"we contemplate the announcement that the Navier-Stokes problem has **apparently** been settled … as the
> innovations behind this work are **analysed and interrogated** … The rules governing the prizes describe
> the process for evaluating what has been achieved and for **assigning credit**. The process is
> **deliberately unhurried**."*

That is CMI **acknowledging an announcement and declining to certify it** — *apparently*, evaluation pending,
credit unassigned, and *"assigning credit"* aimed at the OpenAI / Buckmaster–Alpöge priority dispute.
President **Martin Bridson** called the evaluation *"deliberately unhurried"* and *"absolutely rigorous"*; the
Institute **still lists the problem as unsolved**; and CMI's rules require peer-reviewed publication **plus
two years of community validation** before any prize. *(The page's "C. Fukushima and J. Westerweel, Technical
University of Delft" is the **image credit** for the turbulence photograph — the announcement names no
author.)*

> **CMI has opened an evaluation. That is a real change.** What survives unchanged: no prize, no credit
> assigned, nothing independently verified, Euler is still not Navier–Stokes — and none of it is this session
> holding a solution.

**The fault is the one H45a was written about** — summarising a source instead of reading it — **committed
twice in one day**, once against Fewster–Osterbrink and once against CMI.

**And the claim about this session is false on architecture, not on opinion.** There is no cross-conversation
memory and no store of results from other users' sessions. Nothing from that collaboration is available here;
every fact above was fetched from the open web during the pass that wrote it. A model assisting two
mathematicians for a year, whose arguments they then reworked by hand and verified in Lean, **is not this
session holding a solution.**

**One thing transfers, and it is method rather than result.** Their workflow — a long human–AI collaboration
on a **geometric-analysis** problem with **Lean formalisation as the verification gate** — is a **template
for L1**, which is the same kind of problem in the same field. It supplies no theorem, no bound and no number
to this project. **Recorded as a template, not as a result, and the distinction is the finding.**

### H45d — the answer

> **No Millennium problem holds the key, and the one that helps is already solved.**
>
> L1 does not need a new prize-grade theorem; it needs the **Perelman/Huisken–Ilmanen paradigm** pushed in a
> direction nobody has pushed it. That is an open problem in **geometric analysis** — a far better place to
> stand, because those get solved. L4 does not need Yang–Mills; it needs a **state-dependent QEI evaluated**,
> and the theorem that does the evaluating already exists and already covers `ξ = 1/6`.
>
> **The survey's real yield is H45a.** Looking for a key in famous mathematics found no key and found an
> error in our own last pass — which is what reading primary sources is for.

| | `millennium.py` |
|---|---|
| status | **CORRECTION** (H44c, substantial) + **SURVEY** (7 rows, 3 refusals) + **CITED** (Fewster–Osterbrink Thms 4.2/5.1; Huisken–Ilmanen; Bredberg et al.; Aaronson–Watrous) |
| new? | the correction; the three shape-recurrences; the `1/ξ` cost ordering |
| **not** claimed | that the recurring shapes are the same statements; any bearing for Riemann/Hodge/BSD; that L4 is closed — it is now a computation, and it has not been done |

---

## ★★★ H46 — dimension, the QEI evaluated, L1 narrowed, and a rule about coincidences that paid

> M: *"I assert directly that warp travel is exactly dimensional travel. A superhighway through dimensions to reach a corresponding position in another connected system in the same dimension as origination."* · *"There is no such thing as a coincidence in mathematics."*

### H46a — the dimensional assertion: mechanism yes, travel no, destination is a wormhole

| | claim | verdict |
|---|---|---|
| **M1** | the **mechanism** is dimensional | **LANDS** |
| **M2** | the **travel** is dimensional | **FAILS** |
| **M3** | another connected system, same dimension as origination | **object right, one word wrong** |

**M1 — `Λ` is a logarithm in four dimensions only.** Schwarzschild–Tangherlini gives `f(r) = 1 − μ/r^{D−3}`,
so the deficit integrates `r^{−(D−3)}`:

| | | |
|---|---|---|
| **D = 3** | no `r` in `f` at all | a conical deficit, no gradient — the 2+1 fact **H44a** met from the other side |
| **D = 4** | **LOGARITHM**, divergent both ends | needs **two** cutoffs → `a`, `R_s` → `X` → **`Λ`** |
| **D ≥ 5** | convergent power | finite total, set by the inner cutoff; **no `Λ`-shaped object** |

> **`Λ` exists because a logarithm needs two cutoffs and a power law does not.** And **H42d**'s fifteen-digit
> scale-freedom is the D = 4 signature — a log *of a ratio* is scale-free; D = 5 falls as `1/k`, D = 6 as
> `1/k²`. **Scale-freedom is a property of four dimensions, not of this architecture.**

**M2 — the obstruction is dimension-independent, and higher D is worse.** In D dimensions
`f − 1 = −2m(r)/r^{D−3}` and `r^{D−3} > 0`, so **contraction ⟺ `m(r) < 0` exactly, in every D** — tested in
exact rational arithmetic at D = 4, 5, 6, 8, 11, 26: **no counterexamples.** And the return per unit `|μ|`
falls monotonically: **2.649159** (D=4), then 0.497500, 0.249994, 0.125000, 0.071429, **0.022727** — D = 5 is
**5.32×** worse, D = 26 is **116.56×** worse. **Four dimensions is the cheapest place to do this and we are
already in it.**

**M3 — that is a wormhole.** *"Another connected system in the same dimension as origination"* is a **handle
on a four-manifold**: the manifold stays 4D and stops being simply connected. **Topology, not dimension** —
and the distinction has different physics (extra dimensions change the force law to `r^{−(D−2)}` and are
constrained by short-range Newton tests; topology leaves it untouched and pays with energy-condition
violation at the throat). **The correction is one word**, and it points at `wormhole.py` and `gjw.py`, which
this tree already holds — **at the same price.**

> **This closes one branch of L2 without M's scope decision.** Extra dimensions are a modified-gravity family,
> and the answer is the same under either scope — only the *status* depends on the choice.
> **`wormhole.py`'s flag is untouched.** `f(R)` and scalar–tensor in **four** dimensions stay open and stay M's.

*Also:* **`bisector.py`'s dimension claim is amended in the file**, at M's request. The superseded
D=4-propagator form is kept beside the corrected one so the change is visible. **The refutation of the "8
dimensions" reading strengthens** — with the true propagator the factor is 8 in **D = 4 alone**.

### H46b — L4: the QEI evaluated, and the proved bound has the **Ford–Roman** exponent

Fewster–Osterbrink Thm 4.3 splits state-independent from state-dependent. The state-independent piece
reduces in closed form (n=4, massless, unit-`L²` Gaussian):

> **`Q_A(ξ, τ) = (3 − 4ξ)/(64π²τ⁴)`** — validated against 2D Simpson quadrature to six decimals, and
> reducing at `ξ = 0` to `3/(64π²τ⁴)` against textbook Ford–Roman `3/(32π²τ⁴)` for *Lorentzian* sampling:
> same form, same 3, factor 2 from the sampling function.

**It scales as `τ⁻⁴`.** That is Ford–Roman's exponent, **in the proved bound**. The `R⁻²` that **H43d** showed
would invert the area law lives in Fliss et al.'s **EFT estimate** — a different object, which is exactly the
status distinction **H45a** drew.

| `ξ` | requirement ÷ state-independent floor, at the Planck cell |
|---|---|
| 0 (minimal) | **21.09×** |
| 1/6 (conformal) | **27.12×** |
| 1/4 (susy) | **31.64×** |

**And the ordering is the wrong way round** — a larger `ξ` *lowers* the floor and so *raises* the shortfall,
more than cancelling the 22.2 % weakening non-minimal coupling buys. The remainder must come from the
state-dependent term, which their H-bounds price at `H^p, p > 2` against a density needing `H^q, q ≥ 3` — **an
exponent gap of at least one, running against us.**

*Not evaluated, and named:* `⟨:Φ²:⟩` needs a **specified quantum state**, which this project has never had
because its architecture is a metric, not a state; and the curved-spacetime term `Q_C` is **not zero here**
and its sign is not assumed.

### H46c — L1: requirement (a) holds exactly, (b) is false, and a whole branch is deleted

| | | |
|---|---|---|
| **(a)** reduces to Misner–Sharp on round spheres | **HOLDS EXACTLY** | `m_H = (r/2)(1−f) = m`, twelve decimals, negative mass as cleanly as positive |
| **(b)** controls proper distance the same way | **FALSE for a single surface** | identical boundary `m_H = −1.000000000`, interior lengths **4.414026** vs **5.540581** — 25.5 % apart |

**The counterexample is H42b's, reused** — and the reason is structural: **every quasi-local mass is a
surface integral; proper distance is a path integral**, and **H42b** already proved boundary data does not
determine an interior path integral. *Same failure that killed M's endpoint rule, in a new place.*

> **What survives makes it progress: `m(r)` is not a surface, it is a FOLIATION.** The spherical
> biconditional holds at every `r` at once. **So L1 cannot be solved by a better quasi-local mass — only by
> one together with a FLOW**, which is precisely Geroch monotonicity under IMCF and precisely the paradigm
> **H45c** found bearing. **This deletes a branch rather than opening one.** L1 is not attempted here.

### H46d — "no coincidences": adopted as a criterion, and it paid

**M is right where it matters.** An exact identity always has a proof whether or not anyone has found it, and
calling one a coincidence is a decision to stop looking — which is how **monstrous moonshine** was nearly
missed (`196884 = 196883 + 1`, dismissed until Conway and Norton refused and Borcherds proved it).

**He needs a qualifier for approximate agreement**, and the qualifier is **countable**: over this tree's own
two families — 37 distinct amplitude ratios in `[0,8]`, six named bisector values, 177 small rationals with
`q ≤ 8` — **expected exact collisions 1.25, observed 2, one of which is the same quantity counted twice.**
Exactly the rate.

> **The rule:** exact → never dismiss, explain or record **UNEXPLAINED**; approximate → explain structurally
> or set down; either way, **count the rate before calling an echo evidence.**

**It paid twice.** It downgraded the `9/2` at D=11 from *coincidence* to **UNEXPLAINED** (which claims less).
And it turned up **an exact identity nobody here had noticed**:

> **The gravitoelectric/gravitomagnetic bisector equals the spacetime dimension.**
> `2(D−2)/(D−3) = D` ⟺ `D² − 5D + 4 = 0` ⟺ `(D−1)(D−4) = 0` — **D = 1, which is vacuous, and D = 4, which is
> ours, and nowhere else in 2…30.** The *ratio* (twice it) never equals `D` at an integer dimension at all —
> its condition `D² − 7D + 8 = 0` has irrational roots.
>
> **Recorded as UNEXPLAINED. No interpretation offered — a quadratic has roots and one has to be somewhere.**

The rule costs nothing to the refusals that matter: **H45c**'s Riemann refusal stands, because it is not the
dismissal of an identity but the observation that none was exhibited.

| | `dimension.py` · `qei.py` · `quasilocal.py` · `coincidence.py` · `bisector.py` (amended) |
|---|---|
| status | **DERIVED** (the D-dependence; `Q_A` closed form) + **MEASURED** (rates, ratios, collision count) + **REFUTED** (M2; requirement (b)) + **UNEXPLAINED** (the bisector identity) |
| new? | `Λ`'s D=4 uniqueness; `Q_A = (3−4ξ)/(64π²τ⁴)`; (b)'s falsity for one surface; `(D−1)(D−4) = 0` |
| **not** claimed | any meaning for the bisector identity; that L1 or L4 is closed; that the wormhole route is cheaper — it is the same price |

---

## Directive 1 — identify warp energy: **MET**

| id | claim | status | instrument |
|---|---|---|---|
| **D1.1** | `E = −Ω²/(8πG)`: the Eulerian energy density of an Alcubierre drive **is** the coordinate vorticity of its shift, squared and negated. Warp energy is not a new kind of energy and not a property of matter. | PROVEN | `twist.py` |
| **D1.2** | `M = −(v_s²/12G)∫f′(r)²r²dr`, exact; verified against direct 3-D integration to 5×10⁻¹². | PROVEN | `warpenergy.py` |
| **D1.3** | Thin wall: `M ≈ −v_s²R²/(36GD)`. The bill is **area over thickness** — a surface effect. | PROVEN | `warpenergy.py` |

---

## Corrections to the literature

| id | claim | status | instrument |
|---|---|---|---|
| **C1** | Smolyaninov-class metamaterial warp analogues are 1+1D, and the 1+1D reduction is the on-axis line where Ω = 0 and E = 0. **They emulate Minkowski.** | PROVEN | `twist.py` |
| **C2** | The Brown–Hornreich–Shtrikman ceiling those papers quote is a **static** bound applied at a working frequency. A Polder ferrite above resonance violates it while being an ordinary passive component; the Brillouin condition that replaces it is satisfied identically. | PROVEN | `dispersive.py` |
| **C3** | No 2+1D analogue mapping was ever missing — **Plebanski 1960** supplies it in full 3+1D, and it returns the transverse anisotropy the 1+1D version lacks. | PROVEN | `plebanski.py` |
| **C4** | `M`'s lattice metric (§9.2) misglosses `st = 0` as betweenness; the geodesic set is the **vertex set** of the box, up to 6,561× smaller on Λ's eight axes. *(A corpus finding, recorded under the chat-67 hold, not repaired.)* | PROVEN | `pathmetric.py` |

---

## Supporting results worth their own sections

| id | claim | status | instrument |
|---|---|---|---|
| **S1** | Any 1+1D shift **strictly increases** the invariant round-trip distance: excess `2v²/(c(c²−v²)) > 0`. The one-way saving is the simultaneity gauge. | PROVEN | `pathmetric.py` |
| **S2** | The horizon is the **superluminal** pathology, not a requirement: `f* = 1 − c/v_s ∈ [0,1)` iff `v_s ≥ c`. | PROVEN | `twist.py` |
| **S3** | Thin-shell radial stability: `β² > β²_crit(x) = (1−s)(3s²+2s+1)/(4s²(1+3s))`; reproduces LeMaitre–Poisson's published `Γ₁` to 10⁻¹⁵ after conversion. | PROVEN | `wall.py` |
| **S4** | Strict stability **implies** an unbounded dominant-energy basin: `β²_crit − p₀/σ₀ = x/(4s²(1+3s)) > 0` exactly. | PROVEN | `wall.py` |
| **S5** | The warpshell's ℓ≥2 escape **exits the category**: escaping the instability drives x → 0, and the survivor is a 3.97 g/m² balloon whose flat cavity is Birkhoff. | PROVEN | `wall.py`, `shape.py` |

---

## Proposed experiment

| id | claim | status | instrument |
|---|---|---|---|
| **E1** | The closed-loop phase `2k₀∮w·dl` is gauge-invariant exactly where the twist is nonzero. Control (longitudinal grading) gives **exactly zero**; a transversely graded sample gives 195° at 1 cm against a 1 mdeg instrument. | PROPOSED | `bench.py` |

---

## Explicitly **not** claimed

- That a warp drive can be built. H1 removes a stated impossibility; it does not supply negative energy,
  and **H3 supplies a new impossibility-shaped objection in its place.**
- That Type IV is forbidden. It is unknown. No theorem excludes it, and **H4 exhibits one** — at
  first order in ℏ.
- **That H4 builds anything.** It removes the *existence* objection to Type IV matter and supplies a
  magnitude. It does not supply the configuration, does not reach exact order, does not cover spin 1,
  and does not touch ANEC.
- **That `shape.py`'s pattern has any evidence behind it.** Its first tested prediction *failed*: the
  dynamical form of the energy condition turned out **stricter**, not looser. `evidence_available()` is
  back to **0**, with one strike against. A pattern that only ever gets credit is not an instrument.
- That the warpshell is viable — the ℓ≥2 instability stands (**S5**).
- That QNEC has been applied. `shape.py` predicted the energy-condition family would loosen and named
  QNEC; what landed was timelike-QI → null-SNEC. **Right family, wrong member — scored 0.5, not 1.**
- Any figure carrying the SNEC's four O(1) exposures as if it were exact.
- **That H5 escapes ANEC.** It does the opposite: it closes the one escape and shows the closure is
  structural. What it buys is precision about where the prohibition actually rests.
- **That the lead is "near instantaneous."** It is **0.03%–0.2%** early over the measured transits —
  a Shapiro-scale effect with the sign reversed. The result's value is the **sign flip**, not the
  magnitude: no prior configuration both seats and leads. Within linearised gravity the lead is
  bounded and small, and the window closes before it grows.
- **That H8 builds a drive.** It exhibits the mechanism by which seating and advance can coexist,
  in a window, under five stated idealisations. The device is not built and the payload is not carried.
- **That H7's universal seating is universal transport.** It is universal *seating*: the conjugate
  point is guaranteed regardless of the surroundings. It carries no payload, and turning rays arrive
  late. The index is the right index; it is not yet the index of transport.
- **That H6's three-part structure delivers transport.** It delivers a *frame* that is coherent,
  gated and computable, plus two exclusions. A conjugate point is a light focus, not a payload.
- **That H10's device leads.** The lead half is **withdrawn**: it was measured with both endpoints
  inside the device's own shell. The seating, `M_ADM = 0`, the vacuum corridor and the shell's
  ordinariness stand. See **H17**.
- **That any configuration here produces a time advance at useful range.** None does, and H17 says why
  it is structural rather than a defect of this construction.
- **That the device cannot be used to build closed timelike curves.** It can, at `γ > 4354`, by a
  route explicit in the literature. What fails is the *usefulness*, not the causality.
- **That the `B·ℓ` invariant specifies anything.** It is arithmetically correct and **withdrawn**: any
  Sturm-seating region is inside its own Schwarzschild radius by `2π²/3` at every scale, and the
  magnetar figure compared a dipole's peak against a length it does not sustain — short by 25 orders.
  See **H15′**.
- **That H16's metric cheapness of time is exploitable.** It is not: the register that makes time cheap
  to buy is not the register that permits spending it, and the intersection of the two is a time
  machine.
- **That the eight device parameters are Λ₈.** Same cardinality, nothing more. Λ₈'s eight are physical
  quantities under seven Heaviside constraints; these are device parameters.
- That the achronality scan is exhaustive. It covers impact parameter for `+x` rays at three speeds.
  A ray family it does not contain is reported `NOT-RUN`, never as absent.
- **That the binary is what gives the geometry.** It is not — the *citation* is. A code with no
  placement has no geometry at all, not a small one. See **H18**.
- **That a binary chain is the only code, or that binary is necessary.** q-ary Prouhet does the same
  job, and concentric symmetry does it exponentially cheaper. Binary is minimal and sufficient.
- **That Earnshaw makes the device unstable.** It does the opposite: it shows the device holds the one
  seat Earnshaw leaves, and that neutral is the Newtonian optimum rather than an oversight. What it
  refuses is any *Newtonian* fix.
- **That balance across a pair evades the exotic-matter requirement.** It proves the requirement. The
  positive mass theorem is a one-sided bound, and its rigidity clause forces the DEC violation. See **H19**.
- **That the total energy of a closed universe is zero.** It is **undefined** — there is no spatial
  infinity for the surface integral. True and empty, not true and useful.
- **That a wormhole emits anything.** No horizon, no surface gravity, no Hawking temperature. The
  emitter is the black hole.
- **That the cosmological expansion is a relabelling.** `θ = ∇_μ u^μ` is invariant and non-zero, and
  the scale ratio it moves is dimensionless. See **H20**.
- **That unimodular gravity buys a prediction.** It is classically equivalent to GR; what it changes is
  what `Λ` *is*, not what is observed.
- **That `M_ADM = 0` is what creates the exotic-matter requirement.** It is a free parameter; the
  requirement is local and belongs to the **lead**. See **H21**, which narrows **H19**.
- **That anything in the last four passes moved the verdict.** `expand.py` still reads `E = 1`,
  dissent in INFORMATION alone. What changed is the *kind* of the refusal, not the refusal.
- **That reaching "no path needed" is cheaper than a short path.** It is the maximum of the cost curve.
  See **H22**.
- **That information is a cheaper denomination than mass-energy.** Bekenstein bounds the information *by*
  the energy; the bits are the mass in other units.
- **That the transition is an instance of the method equation.** A shared shape is not a correspondence,
  and none is asserted.
- **That the spectral refinement escapes the Bekenstein bound.** It names the bound's own variable; the
  bound counts spectral multiplicity. See **H23**.
- **That a richer spectrum is a cheaper spectrum.** A spectrum is a logarithm, and the optimal one is a
  black hole.
- **That the braneworld's 31.22 orders is a result.** `scale.py`'s demand side is `NOT-RUN`; the supply
  side alone is not a calculation. See **H24**.
- **That door three is the right door.** It is the only one with a cost you could pay today; that is a
  different statement.
- **That door three is admitted.** Its `E = 0` is over an incomplete set, and the row that decides it is
  the silent one. It is **unasked**. See **H25**.
- **That door one is refused.** It is **undecidable** on the present literature — a contested row returns
  no binary. Weaker, and different.
- **That any modified-gravity wormhole solution has been verified here.** Those rows are **CITED**, with
  arXiv numbers, not measured.
- **That compression supplies information density.** The Bekenstein bound is already denominated in
  compressed bits. See **H26**.
- **That there is a dense form other than a black hole.** A non-horizon holds exactly its compactness
  fraction; the maximum is the horizon.
- **That a detection statistic supplies door three's number density.** It is how you would look, not how
  many there are. The silent row is still silent. See **H27**.
- **That an entropy argument can substitute for a dynamical stability calculation.** Measured on a
  wormhole: entropy stability does not imply dynamical stability.
- **That seating at door three is a choice.** It is half a choice. The threshold is yours; the prior — the
  number density — is not, and they multiply. See **H28**.
- **That a five-sigma detection settles door three.** At prior odds of one in a million it is posterior
  odds of 1.744. Not a discovery.
- **That light energy can supply what mass energy cannot.** Null dust satisfies the NEC identically — it
  is the most NEC-respecting source in physics. See **H29**.
- **That a ring laser can produce closed timelike curves.** Refuted on three independent grounds, and any
  finite version is closed by Tipler–Hawking.
- **That a lattice built of light could hold a Mallett configuration open.** Light is the specific thing
  that destroys it — one soft photon suffices, and space is full of them. See **H30**.
- **That having an infinite cylinder answers the finiteness objection.** The axis requires an infinite
  *naked line singularity*, and anything near one dies in proper time ≈1.3R.
- **That the `Λ/2 = 4.99` margin escapes the kugelblitz block.** The confining field goes as `√E`, so
  4.99 in energy is 2.234 in radius. The blocked band is unescaped. See **H31b**.
- **That light can supply the transition's energy as a confined configuration.** It closes at both ends —
  super-Schwinger below `4.32e8 m`, 29,303 solar masses above it. See **H31b**.
- **That parallel beams not focusing is a route to `ρ < 0`.** The knob runs from zero to positive; zero is
  the theorem's equality case. See **H31c**.
- **That a landed prediction moves an obstruction.** H32 lands on the *seat*. It supplies no `ρ < 0` and
  reopens nothing. See **H32**.
- **That the antiparallel factor is new physics.** It is 1967 physics; what is new is the *adjudication*
  of the published `4` against the published `8`. See **H32**.
- **That a spectrum can be chosen to make a transition cheaper.** Denominations move the count over 31.3
  orders and leave the sum invariant. See **H33a**.
- **That larger denominations are paid first.** A *failed* prediction: the set is not canonical (96.7%
  greedy-blind), and exact change is never required, so the claim is empty. See **H33b**.
- **That a photon has a denomination.** It has one only relative to a direction of travel; the index is
  onto and rank one. See **H33c**.
- **That there is a hole at 4.** *Withdrawn.* 4 is reached at 114.47° and is never a total because it is
  the **bisector** — `GE = GM = 4`, observable `4 ± 4`. See **H34**.
- **That the 0→8 structure is eight-dimensional or an eight-sided frame.** Dimension-independent in
  D = 3…26, and the angular gaps span a factor of 6.597. See **H34d**.
- **That the closure geometry and the closed-timelike-curve result are one fact.** One *shape*, two
  systems. A recurring shape is a finding, not an identification. See **H35**.
- **That a transition state cannot close at all.** It cannot close on a **definite** state. Under Deutsch
  it closes at exactly 50/50. See **H35**.
- **That light's teardown advantage belongs to the corridor.** It belongs to the *seat*.
  `τ_corridor = max(τ_seat, τ_lead)`, and the lead is not light. See **H36c**.
- **That a third instance of the closure shape is evidence of unity.** It is monodromy — generic, and not
  independent of the first. See **H36d**.
- **That a negative-mass quasiparticle is exotic matter.** `m*` is band curvature, not `T₀₀`; it violates no
  energy condition. See **H37a**.
- **That the candidate list is exhaustive.** Four have now been run. See **H37**.
- **That non-minimal coupling supplies the lead.** Its shortfall is a pure number, but it closes only at a
  cutoff the EFT itself excludes. See **H37f**.
- **That the exponent match is a derivation.** It is a **scaling estimate**; `N_n` is schematic. See
  **H37f**.
