# DOCKET 68 / A1-settle: H-SETTLE alone, H-12's carriers, and the collapse control

**Status: a work-item write-up, not seated.** Instrument: `settle.py` (`python3 settle.py --selftest`: 34/34 checks
pass, about 60 s). It imports `nlcontrol.py` and `corridors.py` and copies neither. Every number here is computed in
`settle.py`, READ at the locator given, or labelled NAMED-NOT-READ or OPEN. Short quotations only, each with its page.

M's hypothesis, carried as M stated it: **quantum easing / quantum settling is deterministic drift**, "the state's own
value steers its evolution, smoothly and the same every time" (CHARTER). It is graded on what it does. Whether it is
fashionable does not enter the grade.

## 1. The signal at Bob: an exact law

For nlcontrol's drift H = ε⟨X⟩Z, the Bloch vector rotates about z at a rate set by its own x component:
ẋ = −2εxy, ẏ = 2εx². The perpendicular length ρ⊥ is conserved, and φ̇ = 2ερ⊥cos φ. Its solution is
φ = gd(2ερ⊥t + gd⁻¹φ₀), checked symbolically with sympy (residual 0). This gives

* **Bob's ⟨σ_y⟩ = tanh(2εT) when Alice measures x, and exactly 0 when she measures z.** In general,
  y(T) = ρ⊥ tanh(atanh(y₀/ρ⊥) + 2ερ⊥T). x keeps its sign and z is constant. Against nlcontrol's own integrator the
  closed form agrees to 1.6e-5 on 12 random states.
* nlcontrol's printed numbers are its integrator's output: 0.00600, 0.05993, 0.53706. The exact values are 0.0059999,
  0.0599281 and 0.5370496. The 0.53706 sits +1.0e-5 above the exact value. That comes from the first-order
  frozen-H step, so it is a discrepancy in the last digit and changes no conclusion. A wrong law, tanh(εT), is caught
  by the same comparison (control A4). The linear control H = εZ gives exactly 0.
* Searching every measurement axis Alice could use finds the largest Bob-side displacement on the **x axis**, equal to
  tanh(2εT). The z and y axes give 0. Bob's mean y is ≥ 0 for every axis, because
  tanh u + tanh v = sinh(u+v)/(cosh u cosh v). So this drift offers no antipodal letter.

**What it is worth.** The channel is: Alice picks x or z, Bob measures σ_y. It carries I = D²/(8 ln 2) bits per pair
for small D, with D = tanh(2εT). The capacity tends to log₂1.25 = **0.3219 bits/pair** as D → 1 (a Z-channel with
crossover ½). The Holevo χ equals the measured mutual information, because the two states commute. So one
teleported qubit, which needs 2 bits, needs **at least 6.21 pairs** with this protocol. Holevo's bound caps any qubit
protocol at 1 bit per pair, so any protocol needs at least 2 pairs (Holevo is NAMED-NOT-READ here).

## 2. The published bounds, by family, and what each permits at Bob

**The KR family: causal by construction.** All entries are READ. Kaplan and Rajendran (2106.10576v2) shift a bosonic
field by ε times its expectation value (eq. 4). For separated systems the evolution factorises into a unitary on x
times a unitary on y (§2.3, pp.7–8). A local operation on Alice's side therefore reaches Bob only through retarded
Green's functions. The bounds on |ε_γ|:

| bound | source |
|---|---|
| 1.15e-12 at 90% CL | 2411.09611v1 p.1, p.7 |
| 5.4e-12 (1 s.d.) | 2206.12976v1 p.1, p.5 |
| 4.7e-11 at 90% CL | 2204.11875v1 p.1, p.3 |
| ≲1e-5 from ion traps, ε > 0 only | 2106.10576v2 p.14 |

**Inverting these bounds into the largest superluminal signal at Bob gives 0, at every ε.** The experiments bound an
inter-branch effect, the "Everett phone" (2411.09611v1 p.2). It is not a channel from Alice to Bob. This family
removes nothing from O-BITS.
Two discrepancies are recorded and neither is a refutation:
* 2411.09611 calls its result an improvement "by nearly a factor of 50" (p.1). The computed ratio
  4.7e-11/1.15e-12 is 40.87.
* KR v2 p.14 prints its Lamb-shift estimate as |ε_γ| ≲ 1e-4. Brož et al. restate it as ≲ 1e-2 (2206.12976v1 p.2, p.5).

**The Weinberg family: deterministic, local on pure states.** This is the family Gisin's theorem covers. It contains
nlcontrol's drift and M's definition. The 1989–90 spin experiments are PRLs that are not on arXiv:
* Majumder et al.: |ε|/2π ≤ 3.8 µHz.
* Walsworth et al.: 3.7e-20 eV, equal to 8.9 µHz. The check h × 8.9 µHz = 3.68e-20 eV is consistent. The abstract's
  text layer prints the exponent as "10^{20}", which is a discrepancy, not a refutation.

Both figures come from abstract metadata seen through a search index (PubMed ids 10042736 and 10041761). I found no
READ arXiv restatement that carries the numbers, so both are **NAMED-NOT-READ**. Bollinger et al. 1989 (⁹Be⁺) and
Chupp & Hoare 1990 (²¹Ne): **the values are OPEN**. Everything below therefore rests on the Majumder figure and on
these named hypotheses:

* H-MAP: the bounded shift is nlcontrol's 2ε. Reading A takes ε = 2πf, reading B takes ε = πf. Both are given.
* H-TRANSFER: a bound measured on a ²⁰¹Hg or H spin applies to Bob's carrier.
* H-SPIN: Weinberg's experiments used spins above ½. nlcontrol's term is not rotation-invariant; it belongs to the
  torsion class (2112.09005v3 eq. 99, and p.23: "frequency 2J₁x").
* H-COHERE: Bob keeps coherence for the drift time.
* H-FRAME3b: the remote preparation happens on a fixed spacelike hypersurface. 2412.20854v1 p.6 calls this a "rather
  strong assumption" that needs "some preferred time-slicing".
* H-DILUTION: KR p.13 says nonlinear effects can be diluted by cosmic history.
* **The bound is an upper limit measured consistent with zero.**

Conditional numbers. The table uses reading A, ε_max = 2.39e-5 s⁻¹; reading B halves ε.

| quantity | reading A | reading B |
|---|---|---|
| drift time to D = 0.5 | 3.20 h | 6.39 h |
| D at T = 1 s | 4.8e-5 | — |
| D at T = 1 h | 0.170 (5.3e-3 bits/pair) | — |
| D at T = 1 day | 0.9995 (0.320 bits/pair) | — |
| best rate per pair | 6.7e-6 bits/s, at T = 8.6 h | 3.4e-6 bits/s, at T = 17.2 h |

* Pairs for a 3σ detection at the limit, reading A: 3.9e9 at T = 1 s, 310 at T = 1 h.
* **The ε that removes O-BITS.** Bob holds each pair for T = L/2c, so the bits arrive before light would. One
  teleported qubit needs N·C ≥ 2 bits. N < 7 is impossible at any ε.

| distance | ε needed at N = 7 | ε needed at N = 1e3 | ε needed at N = 1e6 |
|---|---|---|---|
| 1 AU | 4.6e-3 s⁻¹ (excluded) | 2.1e-4 s⁻¹ (excluded) | 6.7e-6 s⁻¹ (not excluded) |
| 1 ly | 7.3e-8 s⁻¹ (not excluded) | 3.3e-9 s⁻¹ (not excluded) | 1.1e-10 s⁻¹ (not excluded) |
| 4.24 ly (illustrative) | 1.7e-8 s⁻¹ (not excluded) | 7.9e-10 s⁻¹ (not excluded) | 2.5e-11 s⁻¹ (not excluded) |

  Read this table as: at interstellar distances **the unread upper limit does not exclude** a Weinberg-type drift strong
  enough to carry the two bits. It is **not** evidence that such a drift exists. A measurement consistent with zero
  says nothing in M's favour. A bound that does not exclude says nothing against.

## 3. The collapse-type (stochastic) control: it must not signal, and it does not

The model is the QMUPL-form stochastic Schrödinger equation (1204.4325v3 eq. 23, READ), with A = σ_x, H = 0.7σ_y,
λ = 1 and T = 2. Each trajectory is nonlinear and changes a great deal: |0⟩ ends with a per-trajectory ⟨|x|⟩ of 0.82,
against a Lindblad |x| of 0.18. This is the vacuity guard. The **ensemble** follows the linear Lindblad equation
(1204.4325v3 p.89, READ): Monte Carlo matches it within 2.5σ for all four initial states.
* The exact difference between Alice's two ensembles is 1.1e-16.
* The Monte Carlo detector reads 0.0042 ± 0.0077 (0.54σ): **no signal.**

**The control that must signal does, with the same detector.** Deterministic drift plus collapse noise (ε = 0.3,
λ = 0.2, T = 3) reads 0.259 ± 0.003, which is 93σ. Noise does not wash out a deterministic nonlinearity. What protects
causality is a linear ensemble map. Weinberg makes the same point (1109.6462v4 p.11): if the density matrix's evolution
depends on the ensemble, then "instantaneous communication between isolated systems would be possible".

*Recorded fault, kept like fields12's:* in a scratch prototype (not in settle.py) I tried a "non-martingale"
stochastic control: wrong drift coefficient, explicit renormalisation. It showed no signal. The likely cause is that
renormalising every step restores the norm-preserving structure, which makes that control **VACUOUS**. It was not
used. The claim that no-signalling requires the martingale structure (1204.4325v3 p.17) stays READ, not computed.

## 4. H-12: which of the twelve could carry a state-dependent drift

The definitions were READ from M's `multiverse_12_vector_taxonomy_v2.pdf` through the Drive connector.

| class | members | what that means for a drift |
|---|---|---|
| **Cannot carry a drift of their own** (4) | M (Madelung ordering), R (relativistic contraction) | readouts of α and v; they inherit those bounds |
| | K (Kondo T_K), T (Grüneisen γ_TA) | material properties, not constants of nature; no variation-of-a-constant bound applies |
| **Can carry one in KR form** (5 field carriers) | Z0, α_s, G, G_F, v | see the list below |
| **Can carry one only conditionally** (3) | CP (if the Yukawa matrix is a field), Λ (if dark energy is dynamical), G_θ (if an axion exists, 2001.11966v1 p.1) | no READ variation bound |

The five field carriers:

* **Z0**: Z0 = 2αh/e² = 376.730313410 Ω, computed, against CODATA 376.730313412. So Z0's variation is α's. The
  carrier is the photon field. **Z0 is the only one of the twelve with a measured state-dependent bound**,
  |ε_γ| < 1.15e-12, and that bound belongs to the causal family. Time variation: α̇/α = 1.0(1.1)e-18 /yr; coupling
  to gravity (c²/α)dα/dΦ = 14(11)e-9 (2010.06620v2 p.1, Table II).
* **α_s**: carried by the gluon field. KR fn. 5 says no non-trivial bounds can be placed on ε_S. The available proxy
  is Oklo, |Ẋ_s/X_s| < 1e-18 /yr (0705.3704v2 p.1, p.4).
* **G**: carried by the metric. KR p.14 says they are "not aware of any current experimental data" constraining ε_G.
  Ġ/G = (4 ± 9)e-13 /yr from lunar laser ranging (1009.5514v1 p.71 eq. 133, READ-VIA-RESTATEMENT of
  Williams–Turyshev–Boggs 2004).
* **G_F**: carried by the W and Z fields. No numeric bound READ; at tree level it is tied to v (named).
* **v**: the expectation value of a bosonic field, so KR's construction applies to it literally. From
  μ̇/μ = −8(36)e-18 /yr, with m_e ∝ v (fixed Yukawa, named) and the board's H1/H2 with S = 0.047–0.094:
  v̇/v = +8(38)e-18 to +11(51)e-18 /yr.

G_θ static bound: |d_n| < 1.8e-26 e·cm at 90% CL (2001.11966v1 p.6). The conversion to θ̄ is OPEN.

**Named limit: a time-variation bound bounds a drift common to all states. It does not bound state-dependence.**
Among the twelve, only Z0 has a state-dependent bound.

**Discrepancy (recorded, not repaired).** `warpfolder.py` §4 calls the 12-vector "a list of COUPLING CONSTANTS AND ONE
VACUUM EXPECTATION VALUE". The PDF defines M, R, K and T as emergent atomic and condensed-matter properties, and Z0 as an
impedance. warpfolder's category conclusion, that none of the twelve carries a quantum number, is unaffected.

## 5. Grades, alone and in the combinations the charter names

| hypothesis | verdict | removes | leaves |
|---|---|---|---|
| H-SETTLE-W, M's definition (Weinberg/Gisin type), alone | PARTIAL | O-BITS, conditional on ε ≥ ε_min(L, N) and on the hypotheses in §2 | O-MAKE, O-HOLD, O-MATTER, O-LOOP; without a fixed slicing, signals faster than light reopen loops |
| H-SETTLE-KR (causal field-expectation form), alone | OPEN | none | O-BITS, O-MAKE, O-MATTER, O-LOOP; **O-HOLD OPEN** |
| Collapse-type stochastic drift | LEAVES-ALL | none (control: no signal) | all five |
| H-12 alone, linear QM | LEAVES-ALL | none (fields12.py: 1.44e-15) | all five |
| H-SETTLE × H-12 | PARTIAL | O-BITS only through a Weinberg-type carrier drift; none in KR form | the other four |
| H-SETTLE-W × H-FRAME | PARTIAL | O-BITS (conditional); O-LOOP, under the model choice H-SIG-COR | O-MAKE, O-HOLD, O-MATTER |

Why H-SETTLE-KR's O-HOLD is OPEN: KR p.13 reads a gravitational nonlinearity as positive-energy matter in another
branch appearing here as a null-energy-violating source ("may cause it to undergo a bounce"). That is speculation in
the source, and ε_G is unconstrained.

Why the H-SETTLE-W × H-FRAME pairing removes O-LOOP: Gisin's protocol already needs a fixed slicing (2412.20854v1 p.6,
assumption 3b). corridors.py, imported, shows that identifications keyed to one frame close no causal curve
(0 of 2,000 pairs), while two frames do (E1, E2). Treating a signal as such an identification is the model choice
H-SIG-COR.

The record on the theory itself is contested, and the grades above carry no verdict on it:
* Gisin's theorem (READ-VIA-RESTATEMENT: 2412.20854v1 pp.5–7; quant-ph/0012041v3 p.1, p.5; 1109.6462v4 p.11) makes
  signalling generic for local deterministic nonlinearity.
* Polchinski's causal restriction (READ-VIA-RESTATEMENT: 2206.12976v1 p.1; quant-ph/0012041v3 p.1) is disputed by
  Mielnik (quant-ph/0012041v3 p.5). Mielnik argues that an observable satisfying the criterion must be quadratic.
* Bielińska–Eckstein–Horodecki find that a categorical rejection "might be premature" (2412.20854v1 p.25).

## 6. Testable predictions

* **H-SETTLE-W**: Bob's mean σ_y shifts by tanh(2εT) when Alice switches from z to x; the shift is 2εT for small εT.
  At the Majumder limit (reading A), about 310 pairs held for 1 h detect it at 3σ. The arrival time is Alice's time in
  the preferred slicing plus T, whatever the distance. The candidate frame is the CMB rest frame
  (`cmb-dipole-370kms`, D67 NARROWED).
* **H-SETTLE-KR × G**: a gravity gradient from a test mass positioned according to a qubit outcome, read by an atom
  interferometer, as proposed in 2204.11875v1 p.4. It would bound ε_G, which is the parameter that bears on O-HOLD.

## Sources

READ means read at source through alphaXiv.

| source | status | what it was used for |
|---|---|---|
| 2411.09611v1 | READ, pp.1–8 | |
| 2204.11875v1 | READ, pp.1–4 | |
| 2206.12976v1 | READ, pp.1–5 | |
| 2106.10576v2 | READ, pp.1–3, 7–8, 13–14, 22 | |
| quant-ph/0012041v3 | READ, pp.1–6 | |
| 2412.20854v1 | READ, pp.1–10, 17–26 | |
| 1204.4325v3 | READ, pp.1–2, 15–17, 31, 34, 53, 87, 89, 111–112, 131 | |
| 1109.6462v4 | READ, pp.1–14 | |
| 2112.09005v3 | READ, pp.1–11, 23–24 | |
| 2203.10269v3 | READ, pp.1–4 | Weinberg 2016's three-clock test; no 1989 bounds in it |
| 1909.01608v2 | READ | no Weinberg bounds in it |
| 0705.3704v2 | READ, pp.1–7 | |
| 2010.06620v2 | READ, pp.1–4 | |
| 1009.5514v1 | READ, pp.1, 71–79 | |
| 2001.11966v1 | READ, pp.1–6 | |
| Weinberg 1989 | READ-VIA-RESTATEMENT | qualitative structure only |
| Gisin 1989, 1990; Polchinski 1991; Simon–Bužek–Gisin 2001 | READ-VIA-RESTATEMENT | |
| Bollinger 1989; Chupp & Hoare 1990; Walsworth 1990; Majumder 1990 | NAMED-NOT-READ | |

No host refused (no 403). The D67 audit `fermion-mass-constancy` named 2010.06620 and 1009.5514 "for a future read"; the
pages cited here are now READ. That note is for the board; nothing outside docket68/ was edited.
