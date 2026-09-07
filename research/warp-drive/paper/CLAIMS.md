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

**A normalisation caution, enforced in the file:** the *sign* of the Unruh term comes from
`universal.py` and the *magnitude* ratio from `selfconsistent.py`. Those are different normalisations;
no mixed quantity is reported.

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
- That the achronality scan is exhaustive. It covers impact parameter for `+x` rays at three speeds.
  A ray family it does not contain is reported `NOT-RUN`, never as absent.
