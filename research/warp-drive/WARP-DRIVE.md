# WARP DRIVE

### Where the object sits in the violation index, what its energy is, and which engine can be built

**Prepared under the protocols of The Method v1.6.** Draft v1.0.

> **Scope.** This paper reads `method/` as a research resource and writes nothing into it. No volume,
> no member, no Register entry is touched. The chat-67 full hold governs: findings here are
> **recorded, never repaired** into the corpus.

---

## Abstract

The repository's companion paper `TRANSITIONS` carries two references to warp drive theory and never
names the object again. We seat it. Rebuilding the fifteen-letter violation index of `TRANSITIONS`
Part VII from the recovered constructor — which reproduces its three printed figures **18,888 /
18,072 / 816** exactly — we find that **a superluminal warp drive built in standard general relativity
occupies the index's core cell**: the single cell the index excludes, and the one the paper's subtitle
calls *one cell that no index can carry*. The identity is four-for-four. Alcubierre's construction
asks for second-order equations of motion (`EOM = 0`), no explicit Lorentz violation (`X_exp = 0`),
ordinary non-ghost field content (`U_ghost = 0`), and macroscopic quantum-inequality-bounded exotic
matter (`NEC_pt = 3`). That conjunction **is** the core.

**Warp energy is identified**, and it is not a substance. It is the null-energy-condition-violating
component of the stress-energy in the bubble wall, `T_ab k^a k^b < 0`, concentrated in a torus
perpendicular to the direction of travel, with magnitude set entirely by the wall's thickness. Under
the Ford–Roman quantum inequality a 100 m bubble at `v = c` needs a wall **1.18 × 10⁻³³ m** thick and
a total energy of **−8.5 × 10⁷⁹ J**, or 4.8 × 10²⁰ Milky Way masses. That figure is a statement about
the wall, not about warp drives: at a one-metre wall the same bubble costs 0.56 solar masses, and 0.019
after the Bobrick–Martire optimisations.

**A warp drive can be built, and one has been specified.** Fuchs *et al.* (2024) exhibit a
constant-velocity subluminal warp shell satisfying the null, weak, dominant and strong energy
conditions simultaneously — the only warp drive that does. We give its engineering specification and
derive its scaling law. The published solution is a 20 m shell holding **2.37 Jupiter masses at
6.66 × 10⁵ times nuclear density**, sitting at **66.7 % of its own horizon ceiling**, cruising at
**0.04 c**. Because the ceiling `M < R₁c²/2G` is linear in radius while density falls as `1/R₁²`,
scaling the design to an inner radius of **8.16 km** brings the material requirement down to exactly
nuclear density at a cost of **1.84 solar masses**. That is the trade, and it is the design space.

What cannot be built is the superluminal drive, and we state precisely how firmly. Of the 5,304 index
cells admitting one, **none pays nothing**; 92.3 % pay a preferred frame, 53.8 % pay ghosts, 26.9 % pay
higher-derivative equations of motion. Santiago–Schuster–Visser prove independently that every generic
Natário warp drive violates the NEC and lists five escapes; **those five escapes are the index's repair
coordinates, one for one.** But the theorem that would close the door outright — the self-consistent
achronal ANEC in four dimensions — **is unproven, and has been for nineteen years**. `TRANSITIONS`
§8.6b grades Graham–Olum a *conjecture with a sufficiency proof attached*, and §10.4 localises the gap:
it is a modular theory gap, one cell from where it is proved. The door is not closed. It is unlatched,
and we know which latch.

---

## 0. Procedure, provenance and grades

### 0.1 What was read

| source | role |
|---|---|
| `method/members/Transitions.md` | the warp-drive document; read Parts IV–XIII and Appendix B |
| `recovered/objects15.py` | the fifteen-letter index constructor; stdlib, runs, verified |
| `extracted/archives/restore-point-2-13/vi_edges.py` | the nine-letter edge-list search; **did not converge** |
| Alcubierre 1994; Pfenning–Ford 1997; Bobrick–Martire 2021; Santiago–Schuster–Visser 2022; Fuchs *et al.* 2024 | primary literature, full text |

### 0.2 Grades

Following the Admission Law (`TRANSITIONS` §0.2): **a derived entry carries the minimum grade of its
inputs, and no derivation raises a grade.**

| grade | meaning |
|---|---|
| **MEASURED** | read off a file in this repository, with the command given |
| **COMPUTED** | computed by `warpdrive.py` here, from a cited formula |
| **CITED** | someone else's result, stated with provenance |
| **INFERRED** | a mapping or judgement made in this paper, defended and open to refusal |
| **OPEN** | stated as unresolved |

### 0.3 Reproduction

```
python3 research/warp-drive/warpdrive.py --selftest    # 22 fixtures, all from printed numbers
python3 research/warp-drive/warpdrive.py               # the full report
```

The instrument is stdlib-only. Its selftest fixtures are **the corpus's own printed figures and the
literature's own printed figures**, never numbers this paper invented. It copies the closure rules
verbatim from `objects15.py` with a provenance comment, per the standing rule that an instrument
imports a seated form and never silently reimplements one.

---

## 1. What the repository already held

### 1.1 The document

`TRANSITIONS` — *What an index can carry, and one cell that no index can* — is a seated member of the
BUILD180 compendia bundle at `method/members/Transitions.md`, 2,289 lines. Its Appendix B.3, *Energy
conditions and wormholes*, carries the corpus's only two warp-drive references:

```
- Alcubierre, M. (1994). The warp drive. CQG 11, L73–L77. [S]
- Bobrick, A. & Martire, G. (2021). Introducing physical warp drives. CQG 38, 105009. [F]
```

*(MEASURED: `grep -in "warp" method/members/Transitions.md` returns exactly these two lines, at 2213
and 2214. The whole tree returns five files, and the other three are the same two lines carried by
BUILD180 itself and by two recovered `mkmd` generators.)*

The grades are the paper's own access grades: `[S]` secondary, `[F]` full text read. **Alcubierre was
never read in full by the corpus.** That is worth stating plainly at the outset, because the object
this paper seats was cited from secondary sources only.

### 1.2 The machinery, and one thing that does not work

The corpus's violation index exists in two alphabets. **The nine-letter index is not reconstructible
from the repository.** `TRANSITIONS` §5.7 says so outright — *"the edge list itself is not printed
anywhere in this paper"* — and offers five acceptance conditions in its place. The repository holds an
attempt: `extracted/archives/restore-point-2-13/vi_edges.py`, a hill-climbing search over disjunctive
rules whose own docstring records that register 588 *"reached distance 288 at eight rules"*. Distance
zero is exact reproduction. **It never converged, and nothing in the tree says it later did.**
*(MEASURED.)*

**The fifteen-letter index is a different story, and it is fully seated.** `recovered/objects15.py`
carries the closure rules explicitly, runs on the stdlib, and reproduces every figure `TRANSITIONS`
§7.1 prints:

| figure | paper §7.1 | `objects15.py` |
|---|---|---|
| closed cells describing a theory (`SD_field = 0`) | 18,888 | **18,888** |
| admitted after the core charge | 18,072 | **18,072** |
| the defect **E** | 816 | **816** |

*(COMPUTED, `warpdrive.py --selftest`.)* This paper therefore works at fifteen letters throughout, and
makes no claim that depends on the unrecovered nine-letter edge list.

---

## 2. Warp energy, identified

### 2.1 It is not a substance

The question "can we identify warp energy" has a clean answer and it is not the expected one. Warp
energy is **not** a species of matter, a field, or a particle. It is a *sign condition on a contraction
of the stress-energy tensor*: a region where

> **T_ab k^a k^b < 0 for some null vector k^a** — the null energy condition, violated.

Everything else follows from that one inequality. *(CITED: this is the standard definition; see
Santiago–Schuster–Visser §5.)*

### 2.2 Where it sits, and how much of it

For the Alcubierre metric the energy density seen by every geodesic observer is

**⟨T^00⟩ = −(1/8π) · v_s² ρ² / (4 r_s²) · (df/dr_s)²**

*(CITED: Pfenning–Ford eq. 8, and Alcubierre 1994.)* Three facts are legible in that one line and they
are the whole engineering picture:

1. **It is negative everywhere it is nonzero.** There is no positive part to cancel against.
2. **It vanishes wherever `df/dr_s = 0`** — that is, everywhere except the bubble *wall*. Inside and
   outside are flat and empty. The energy lives in a **torus perpendicular to the direction of
   travel**, and nowhere else.
3. **Its magnitude is set by `(df/dr_s)²`**, the square of the shape function's gradient — which is to
   say, by the *inverse square of the wall thickness*. The wall thickness is the only lever.

Santiago–Schuster–Visser sharpen point 1 into a theorem: for the Alcubierre class,
`ρ = −(1/32π)((∂ₓv)² + (∂_yv)²) ≤ 0`, and via the geometric identity `G_zz = 3G_nn` they obtain
`ρ + T_zz = 4ρ < 0`, so **the NEC is violated in all Alcubierre warp drives**. *(CITED, §7.1.)*

### 2.3 How much, quantitatively

Integrating over all space (Pfenning–Ford eq. 28):

**E = −(1/12) · v_b² · ( R²/Δ + Δ/12 )**   *(geometrized units)*

with `R` the bubble radius and `Δ` the wall thickness. The Ford–Roman quantum inequality bounds `Δ`
from above (their eq. 22), giving `Δ ≤ (3/4)√(3/π) · v_b / α²` in Planck lengths, with `α` the ratio of
sampling time to local curvature radius and `α ≪ 1` required. At their `α = 1/10`:

**Table 1 — the warp energy budget.** `R = 100 m`, `α = 0.1`. *(COMPUTED.)*

| `v/c` | wall `Δ` [m] | `E` [J] | `|E|` [kg] |
|---|---|---|---|
| 0.1 | 1.185 × 10⁻³⁴ | −8.514 × 10⁷⁸ | 9.473 × 10⁶¹ |
| 1.0 | 1.185 × 10⁻³³ | −8.514 × 10⁷⁹ | 9.473 × 10⁶² |
| 2.0 | 2.369 × 10⁻³³ | −1.703 × 10⁸⁰ | 1.895 × 10⁶³ |
| 10.0 | 1.185 × 10⁻³² | −8.514 × 10⁸⁰ | 9.473 × 10⁶³ |

At `v = c` that is **4.76 × 10²⁰ Milky Way masses**. Pfenning–Ford print −6.2 × 10⁷⁰ `v L_Planck`; the
computation above gives 4.35 × 10⁷⁰, **agreeing to a factor of 1.4**, which is inside the
order-of-magnitude precision their §4 claims for itself. *(COMPUTED; the discrepancy is recorded, not
smoothed.)*

### 2.4 The number is about the wall, not about warp drives

This is the most misquoted result in the field and the instrument is built to make the point
unavoidable:

**Table 2 — the same bubble, three walls.** `R = 100 m`, `v = c`. *(COMPUTED.)*

| wall `Δ` | `E` [J] | `|E|` [M☉] |
|---|---|---|
| QI-bounded, 1.18 × 10⁻³³ m | −8.51 × 10⁷⁹ | 4.76 × 10³² |
| 1 fm | −1.01 × 10⁶² | 5.64 × 10¹⁴ |
| 1 m | −1.01 × 10⁴⁷ | **0.564** |

Eighteen orders of magnitude in the wall buys thirty-three in the energy. The Bobrick–Martire
optimisations then act on the 1 m case: the variationally optimal shape function `f̄ = min(r₀/r_s, 1)`
divides the requirement by about three, and flattening the bubble by a factor of ten divides it by ten
again — **0.019 M☉** in total. *(COMPUTED, factors CITED from Bobrick–Martire §5.3.)*

> **And none of that makes the energy positive.** It makes less of it negative. Optimisation moves the
> magnitude; it does not touch the sign, and the sign is the whole obstruction.

---

## 3. The placement: the warp drive is the core cell

### 3.1 The claim

The fifteen-letter violation index has exactly one excluded profile, and `TRANSITIONS` §7.1 states it:

> **The core is (X_exp = 0, U_ghost = 0, NEC_pt = 3, EOM = 2nd-order)** — macroscopic exotic matter, no
> explicit Lorentz violation, no ghosts, second-order equations of motion.

Now read Alcubierre's construction as a specification:

| what the warp drive asks for | index coordinate |
|---|---|
| standard general relativity — the Einstein equations, second order in the metric | `EOM = 0` |
| no explicit Lorentz-violating term in the Lagrangian | `X_exp = 0` |
| ordinary field content; the exotic matter is not a ghost condensate | `U_ghost = 0` |
| macroscopic negative energy, quantum-inequality-bounded | `NEC_pt = 3` |

**These are the same four conditions.** *(INFERRED — this is the paper's central mapping, and it is a
judgement, not a computation. It is defensible line by line and refusable line by line; §3.3 states
what would refute it.)*

The consequence is exact and is verified by the instrument: the cell
`close(X_exp=0, …, NEC_pt=3, …, EOM=0)` **is a closed cell** of the index and **is not an admitted
one**. *(COMPUTED, two selftest fixtures.)*

> A superluminal warp drive in standard general relativity is not *near* the index's defect. It **is**
> the defect. The paper's subtitle — *one cell that no index can carry* — names this object without
> ever naming it.

### 3.2 Seating it as an object

`TRANSITIONS` §5.6 seats six objects as thresholds and the warp drive is not among them. We seat it in
four variants. The placement of the superluminal case turns on one point of standing, and it is the
paper's second inference:

> **A superluminal warp drive violates the *achronal* ANEC, where a long wormhole does not.**
> Graham–Olum's jurisdiction, in `TRANSITIONS` §8.1's own charger table, is *asymptotically flat,
> simply connected*. A wormhole escapes by being **not simply connected** — which is precisely how the
> Maldacena–Milekhin–Popov wormhole sits at `NEC_pt = 2, NEC_ach = 0` in §6.5. **A warp drive is
> asymptotically flat and simply connected by construction.** It has no such escape. It is a genuine
> shortcut through a simply connected spacetime, and that is exactly what the achronal ANEC forbids.
> *(INFERRED, from CITED jurisdictions.)*

So the superluminal drive sits at `NEC_pt ≥ 3, NEC_ach ≥ 1` — structurally the *short* wormhole class,
not the long one.

**Table 3 — the warp drive, seated.** *(COMPUTED.)*

| tag | object | cells | admitted here? |
|---|---|---|---|
| `WD-SHELL` | subluminal positive-energy warp shell (Fuchs *et al.*) | 18,072 | **YES** |
| `WD-SUB-ALC` | subluminal Alcubierre / Natário bubble | 8,976 | no |
| `WD-SUP` | superluminal warp drive | 5,304 | no |
| `WD-SUP-CTC` | superluminal, two bubbles (Everett) | 1,632 | no |

`WD-SHELL`'s predicate is *vacuously true*: a positive-energy subluminal shell spends no coordinate of
this index at all. It is admitted in every cell, including ours. **That is not a triviality in the
report — it is the finding**, and §5 collects it.

### 3.3 What would refute the mapping

Stated so the inference can be attacked:

- **`EOM = 0` fails** if one builds the drive in a higher-derivative theory. That is not a refutation,
  it is route A of §5, and the mapping predicts it works.
- **`NEC_pt = 3` is wrong** if the required violation is *not* macroscopic — but Pfenning–Ford's
  integral is over a 100 m bubble and gives 10⁶² kg, so it is macroscopic by any reading.
- **`NEC_ach ≥ 1` is wrong** if a superluminal drive can be arranged so that no achronal null geodesic
  samples the negative region. No such construction is known to us, and Graham–Olum's sufficiency proof
  says the achronal ANEC *would* rule the object out. But see §6: **the condition itself is unproven**,
  which weakens the placement's force without weakening its correctness.

---

## 4. The buildability verdict

### 4.1 What every admitting cell pays

**Table 4 — payment profile of `WD-SUP`, over its 5,304 admitting cells.** *(COMPUTED.)*

| currency | cells | share |
|---|---|---|
| a preferred frame (`X_exp > 0`) | 4,896 | 92.3 % |
| a preferred frame (`X_spon > 0`) | 4,080 | 76.9 % |
| signalling (`IC ≥ 2`) | 3,744 | 70.6 % |
| non-unitarity (`U_open > 0`) | 3,276 | 61.8 % |
| ghosts (`U_ghost > 0`) | 2,856 | 53.8 % |
| higher-derivative EOM | 1,428 | 26.9 % |
| **pay nothing** | **0** | **0 %** |

**Read the last row honestly.** `PAY NOTHING = 0` is *not* an independent discovery: the core charge
that defines the admitted set removes exactly the cells with `NEC_pt ≥ 3` and none of
`{X_exp > 0, EOM > 0, U_ghost ≥ 1}`, so the zero follows from the charge. It is a **consistency check
that the charge does what it says**, and this paper declines to quote it as a finding.

**The distribution above it is not forced**, and that is where the content is. The charge requires *at
least one* of three payments; it says nothing about the other three currencies or about the
proportions. That 92.3 % of admitting cells carry a preferred frame, and only 26.9 % a
higher-derivative EOM, is a property of the closure rules, and it says the cheap routes are scarce.

The same table for `WD-SUP-CTC` reads **100 % `X_exp`**: once two bubbles close a timelike curve,
*every* admitting cell has explicit Lorentz violation. Chronology and Lorentz invariance do not
coexist in this index.

### 4.2 The independent theorem

Santiago–Schuster–Visser (PRD **105**, 064038) prove, without reference to any index:

- **Every generic Natário warp drive violates the NEC** — and therefore the WEC, SEC and DEC. The proof
  needs no asymptotic condition and no zero-ADM-mass assumption: along an Eulerian observer's worldline
  the NEC forces `dK/dτ ≤ −(3/2) tr([K^tf]²) ≤ 0`, so the trace of the extrinsic curvature can never
  increase; but an observer the bubble passes must *return* to `K ≈ 0`. **NEC violation is necessary
  for spacetime to restore its asymptotics after a warp drive passes through.** *(CITED, §7.4.)*
- **Even in modified gravity**, physically reasonable warp drives violate the purely *geometric* null
  and timelike convergence conditions.
- Lentz's positive-energy claim fails because the Einstein equations were never solved — only the
  density, flux and trace, not the trace-free part of `T_ij`. Fell–Heisenberg and Bobrick–Martire check
  only Eulerian observers, which is insufficient for the WEC. *(CITED, Appendix D.)*

### 4.3 The verdict, in three tiers

| object | verdict | grade |
|---|---|---|
| **Superluminal warp drive in standard GR** | **excluded.** It is the core cell; the index will not carry it and SSV prove the NEC violation directly. | COMPUTED + CITED |
| **Subluminal Alcubierre/Natário bubble** | **excluded on the same grounds.** SSV's theorem does not care about the velocity: 8,976 admitting cells, none paying nothing. | COMPUTED + CITED |
| **Subluminal positive-energy warp shell** | **buildable in principle.** Satisfies NEC, WEC, DEC, SEC. Spends no index coordinate. Specified in §5. | CITED |

---

## 5. The engine that can be built

### 5.1 How it escapes

Fuchs, Helmerich, Bobrick, Sellers, Melcher & Martire (*CQG* **41** (2024) 095009) take
Santiago–Schuster–Visser's **escape (ii): modify the definition of warp drive.** The SSV theorem is a
theorem about the *Natário class* — unit lapse `α = 1`, flat spatial metric `γ_ij = δ_ij`. The warp
shell has neither. It is a stable matter shell with a Schwarzschild exterior and **positive ADM mass**,
carrying an added shift vector on its interior that produces linear frame dragging — the geodesic
transport that is the warp effect — without any energy-condition violation.

This is not a loophole in the pejorative sense. It is the index's own reading: **the object leaves the
threshold.** `NEC_pt = 0`, and none of the four core conditions is in play.

### 5.2 Specification

**Table 5 — the published solution.** *(CITED for R₁, R₂, M, β, v, δt; COMPUTED for the rest.)*

| quantity | value |
|---|---|
| inner radius `R₁` | 10 m |
| outer radius `R₂` | 20 m |
| shell mass `M` | 4.490 × 10²⁷ kg |
| — in Jupiter masses | **2.37** |
| — in solar masses | 2.258 × 10⁻³ |
| shell volume | 2.932 × 10⁴ m³ |
| mass density | **1.531 × 10²³ kg m⁻³** |
| energy density | 1.376 × 10⁴⁰ J m⁻³ |
| — in units of nuclear saturation density | **6.658 × 10⁵** |
| Schwarzschild radius `2GM/c²` | 6.669 m |
| horizon margin `R₁ / r_s` | **1.500** |
| horizon ceiling at `R₁ = 10 m` | 6.733 × 10²⁷ kg |
| fill fraction of that ceiling | **66.7 %** |
| shift vector `β` | 0.02 |
| drive velocity | **0.04 c** |
| light-ray test delay vs flat | 7.6 ns |

The computed energy density, 1.376 × 10⁴⁰ J m⁻³, matches the paper's own plotted profiles at
~1.4 × 10⁴⁰ J m⁻³. *(COMPUTED, selftest fixture.)*

### 5.3 The design constraints, and there are four

1. **No horizon.** `R₁ > 2GM/c²`, hence **`M < R₁c²/2G`**. This is the hard ceiling. The published
   solution sits at 66.7 % of it — a margin of 1.5, which is not generous.
2. **Momentum flux below energy density.** Increasing `β` adds momentum flux; past a threshold it
   exceeds `ρ` and the energy conditions fail. `β = 0.02` is stated by the authors as conservative and
   *not* an upper limit; **the upper limit is unpublished.** *(OPEN.)*
3. **Non-isotropic pressure.** The inner boundary needs a hoop stress against gravitational collapse,
   with all principal pressures below the local energy density.
4. **Subluminality.** The comoving-observer construction is a Lorentz transformation from the
   Alcubierre form, which restricts it to `v < c` intrinsically.

### 5.4 The scaling law — the actual engineering lever

Constraint 1 is linear in radius; density is cubic. Fixing the fill fraction at the published 66.7 %
and the ratio `R₂ = 2R₁`, mass grows as `R₁` while density falls as `1/R₁²`:

**Table 6 — scaling the shell.** *(COMPUTED.)*

| `R₁` [m] | `M` [kg] | `M` [M☉] | `ρ` [kg m⁻³] | `ρ / ρ_nuclear` |
|---|---|---|---|---|
| 10 | 4.490 × 10²⁷ | 2.258 × 10⁻³ | 1.531 × 10²³ | 6.658 × 10⁵ |
| 10² | 4.490 × 10²⁸ | 2.258 × 10⁻² | 1.531 × 10²¹ | 6.658 × 10³ |
| 10³ | 4.490 × 10²⁹ | 2.258 × 10⁻¹ | 1.531 × 10¹⁹ | 6.658 × 10¹ |
| **8.16 × 10³** | **3.664 × 10³⁰** | **1.842** | **2.300 × 10¹⁷** | **1.000** |
| 10⁵ | 4.490 × 10³¹ | 2.258 × 10¹ | 1.531 × 10¹⁵ | 6.658 × 10⁻³ |

> **The trade.** The 20 m ship needs material 666,000 times denser than a nucleus — which is to say,
> denser than a neutron star and not known to be stable outside one. Scale the same design to an
> **8.16 km inner radius** and the requirement falls to **exactly nuclear density**, material whose
> equation of state is at least studied — at a cost of **1.84 solar masses**. Push to 100 km and the
> density becomes trivial while the mass reaches 22.6 M☉, which is a stellar-mass black hole's worth of
> shell that must not be a black hole.
>
> **There is no radius at which both numbers are comfortable.** That is the engineering result, and it
> is a curve, not a wall.

### 5.5 What the engine does, stated without inflation

It provides **geodesic transport at 0.04 c**: passengers travel between two points along a geodesic,
feeling no acceleration, while the shell moves inertially. It is not faster-than-light. It is not
faster than a rocket. At 0.04 c, Proxima Centauri is 106 years away.

And **nobody knows how to accelerate it.** The solution is constant-velocity only. Simply moving the
coordinate centre reproduces the Schwarzschild Drive pathology and demands negative energy density
throughout space; a rocket-like momentum transfer needs an ejected mass larger than a structure already
massing 2.4 Jupiters. The authors call this "one of the foremost problems in warp drive research", and
we agree with their assessment. **The open problem is acceleration, not mass.** *(CITED + INFERRED.)*

---

## 6. The door that is not closed

### 6.1 The five escapes are the index's repair coordinates

Santiago–Schuster–Visser close their paper by listing the only ways out. Set that list against the
index's letters:

| SSV escape | index coordinate | status |
|---|---|---|
| (i) modify the theory of gravity | `EOM ≥ 1` or `X_exp ≥ 1` | route A / C below |
| (ii) modify the definition of warp drive | leave the object's threshold | **taken — §5** |
| (iii) modify the energy conditions | a rung change on `NEC_pt` | §6.2 |
| (iv) appeal to macroscopic quantum physics | the QI regime, `NEC_pt = 2` vs `3` | open |
| (v) allow singularities or CTCs | `X_exp = 3` | `WD-SUP-CTC`, 100 % Lorentz-violating |

**The correspondence is one for one.** *(INFERRED.)* Two independent constructions — a constraint index
built from a literature census, and a GR theorem's list of loopholes — enumerate the same escape set.
We record this as a **match, not a derivation**: nothing forces the two lists to agree, and the
agreement is evidence that the index's letters are carrying real physics rather than bookkeeping.

### 6.2 The three routes still open, as engineering

**Route A — degenerate higher-derivative gravity (`EOM ≥ 1`, ghost-free).** The index's closure carries
`EOM ≥ 1 → U_ghost ≥ 1`: Ostrogradsky's theorem turns higher derivatives into ghosts, so the route
appears to pay twice. **But Ostrogradsky's jurisdiction, in `TRANSITIONS` §8.1's own table, is
*non-degenerate* — and Galileons escape.** A degenerate higher-derivative theory (Horndeski, beyond
Horndeski, DHOST) has `EOM ≥ 1` with `U_ghost = 0`, and simultaneously falls outside
Buniy–Hsu–Murray, whose jurisdiction is *second-order EOM*. **Both chargers lose standing at once.**
This is the single most promising route the index exposes, and `TRANSITIONS` Part XIII already lists it
as reopened: *"whether Buniy extends to Lorentz-violating second-order theories"*. The caution is SSV's:
in modified gravity the purely geometric null convergence condition is still violated, so the route is
narrowed, not cleared. *(INFERRED from CITED jurisdictions.)*

**Route B — explicit Lorentz violation (`X_exp ≥ 1`).** Einstein-aether, Hořava–Lifshitz. 92.3 % of
admitting cells take this route, which makes it the *common* one, not the cheap one — a preferred frame
is a large price and it is the price most cells pay.

**Route C — ghosts (`U_ghost ≥ 1`).** Pay the currency directly. 53.8 % of admitting cells. The vacuum
is then unstable, which is what Buniy–Hsu–Murray's charge means.

### 6.3 And the theorem that would end the argument does not exist

This is the finding that most changes the picture, and it comes from the corpus rather than the
literature.

The single condition that would rule out a superluminal warp drive outright is the **self-consistent
achronal ANEC in four dimensions**. `TRANSITIONS` §8.6b grades it:

| | |
|---|---|
| status | **CONJECTURE with a sufficiency proof attached** |
| what is proved | that the condition, *if* it holds, rules out wormholes and closed timelike curves |
| what is not | the condition itself |
| age | **19 years, no proof, no counterexample** |
| function | a filter, not a derivation |

And Part XIII adds the reason the obvious route is blocked: **null quantum energy inequalities have no
finite lower bounds in four dimensions** (Fewster–Roman), which is why the Kontou–Olum path cannot be
extended.

`TRANSITIONS` §10.4 then localises the gap with unusual precision, and this is the corpus's own
strongest result on the question:

> **The ANEC gap in curved spacetime is not an ANEC problem. It is a modular theory problem.**

Five of six curved-space routes to the ANEC need a Killing field or a horizon generated by one; the
sixth substitutes a holographic dual and returns a weighted bound. The obvious repair — extending
geometric modular flow to near-horizon boosts — is **excluded by theorem** (Sorce 2024: any geometric
modular flow must be generated by a conformal Killing field). The one route that survives is
**half-sided modular inclusion**, established for Killing horizons (`STAT = 0`, 8 cells) and open for
non-expanding ones (`THETA = 0`, 16 cells).

> **The open question is HSMI on isolated horizons** — one cell from where it is proved, and the cell is
> standard in general relativity.

So the honest statement of buildability is not "impossible". It is:

> **The superluminal warp drive is excluded by every argument that has standing, and the one condition
> that would exclude it unconditionally is a nineteen-year-old conjecture whose proof is missing a
> single, identified, technical step in modular theory.**

That is not encouragement. `TRANSITIONS` §10.4d is explicit that the remaining piece — condition C2,
whether a Hadamard state respects the transverse factorisation that C1 establishes — "is the whole
remaining problem", and it is a hard one. But it is the difference between a closed question and an
open one, and the corpus is the only place we found that says which.

---

## 7. Results

**1. The repository's warp-drive content is two bibliography lines, and Alcubierre was read at grade
`[S]` only.** *(MEASURED.)* The object is cited and never seated.

**2. The fifteen-letter violation index is fully reconstructible from the repository; the nine-letter
one is not.** `objects15.py` reproduces 18,888 / 18,072 / 816 exactly. `vi_edges.py` records a search
that reached distance 288 and never converged. *(MEASURED + COMPUTED.)*

**3. A superluminal warp drive built in standard general relativity is the index's core cell.** Four
conditions, four coordinates, exact match. The object the paper's subtitle calls *one cell that no
index can carry* is the warp drive. *(INFERRED, from COMPUTED.)*

**4. Warp energy is identified: it is `T_ab k^a k^b < 0` in the bubble wall, toroidal, and scaled by the
inverse square of the wall thickness.** Not a substance; a sign condition with a geometry.
*(CITED + COMPUTED.)*

**5. The famous energy figure is a statement about the quantum inequality, not about warp drives.**
−8.5 × 10⁷⁹ J at a Planck-scale wall; 0.56 M☉ at a one-metre wall; 0.019 M☉ after optimisation.
Optimisation moves the magnitude and never the sign. *(COMPUTED.)*

**6. A warp drive can be built, subluminally, with positive energy, and one has been specified.** The
Fuchs *et al.* shell satisfies all four energy conditions and spends no index coordinate.
*(CITED + COMPUTED.)*

**7. Its engineering is a curve, not a wall.** `M < R₁c²/2G` is linear in radius, density falls as
`1/R₁²`. Nuclear-density material suffices at `R₁ = 8.16 km` and 1.84 M☉. No radius makes both numbers
comfortable. *(COMPUTED — this paper's principal engineering contribution.)*

**8. The open problem for the buildable engine is acceleration, not mass.** The solution is
constant-velocity; every known acceleration scheme either reintroduces negative energy globally or
demands an ejected mass exceeding the ship. *(CITED.)*

**9. Santiago–Schuster–Visser's five escapes are the index's repair coordinates, one for one.** A match
between two independently constructed enumerations, recorded as corroboration and not as derivation.
*(INFERRED.)*

**10. `PAY NOTHING = 0` is a consistency check, not a finding**, and is not quoted as one. The
informative result is the distribution above it, which the charge does not force: 92.3 % preferred
frame, 53.8 % ghosts, 26.9 % higher-derivative. *(COMPUTED.)*

**11. The most promising open route is degenerate higher-derivative gravity**, because Ostrogradsky and
Buniy–Hsu–Murray lose jurisdiction simultaneously — the first by degeneracy, the second by the loss of
second-order EOM. Narrowed, not cleared, by SSV's geometric convergence conditions. *(INFERRED.)*

**12. The condition that would settle the question is unproven and its missing step is identified.** The
self-consistent achronal ANEC in 4d: nineteen years, no proof, no counterexample; the gap is modular
theory; the live target is half-sided modular inclusion on isolated horizons, one cell from where it is
proved. *(MEASURED from the corpus.)*

---

## 8. Open

| item | state |
|---|---|
| the upper limit on the shift vector `β` before momentum flux exceeds energy density | unpublished; Fuchs *et al.* call `β = 0.02` conservative and give no bound |
| physical acceleration of a positive-energy warp shell | the foremost open problem in the field; no known scheme survives |
| whether a degenerate higher-derivative warp drive exists | route A. Not attempted here and not, to our knowledge, attempted anywhere |
| an equation of state for matter at 6.7 × 10⁵ × nuclear density | none; the 8.16 km scaling exists to avoid needing one |
| the self-consistent achronal ANEC in 4d | 19 years open; condition C2 on isolated horizons is the whole remaining problem |
| whether the nine-letter index's edge list is recoverable | `vi_edges.py` stalled at distance 288; no later run recorded |
| whether the `NEC_ach ≥ 1` placement of `WD-SUP` survives a construction that samples no achronal geodesic | none known; would refute §3.2 |

---

## Appendix A · Reproduction

Every number in this paper carries a command.

```
python3 research/warp-drive/warpdrive.py --selftest
python3 research/warp-drive/warpdrive.py
grep -in "warp" method/members/Transitions.md
sed -n '1,60p' extracted/archives/restore-point-2-13/vi_edges.py
```

The selftest's 22 fixtures are drawn from `TRANSITIONS` §7.1, Pfenning–Ford §§3–4, and Fuchs *et al.*
§§3–5. It asserts the index reconstruction, the core cell's exclusion, the `WD-SUP` placement and
payment profile, the quantum-inequality wall bound, both Pfenning–Ford energy figures, and the shell's
density, horizon margin and scaling. A `FAIL` means this paper is wrong, not that the fixture is stale.

## Appendix B · References

**Access grades**, per `TRANSITIONS` §0.2. **[F]** full text read here. **[S]** secondary.

- Alcubierre, M. (1994). The warp drive: hyper-fast travel within general relativity. *CQG* **11**, L73–L77. **[S]**
- Pfenning, M. J. & Ford, L. H. (1997). The unphysical nature of "warp drive". *CQG* **14**, 1743. gr-qc/9702026. **[F]**
- Ford, L. H. & Roman, T. A. (1995). Averaged energy conditions and quantum inequalities. *PRD* **51**, 4277. **[S]**
- Van Den Broeck, C. (1999). A 'warp drive' with more reasonable total energy requirements. *CQG* **16**, 3973. **[S]**
- Natário, J. (2002). Warp drive with zero expansion. *CQG* **19**, 1157. **[S]**
- Bobrick, A. & Martire, G. (2021). Introducing physical warp drives. *CQG* **38**, 105009. arXiv:2102.06824. **[F]**
- Lentz, E. W. (2021). Breaking the warp barrier: hyper-fast solitons in Einstein–Maxwell-plasma theory. *CQG* **38**, 075015. **[S]**
- Fell, S. D. B. & Heisenberg, L. (2021). Positive energy warp drive from hidden geometric structures. *CQG* **38**, 155020. **[S]**
- Santiago, J., Schuster, S. & Visser, M. (2022). Generic warp drives violate the null energy condition. *PRD* **105**, 064038. arXiv:2105.03079. **[F]**
- Helmerich, C. *et al.* (2024). Analyzing warp drive spacetimes with Warp Factory. *CQG* **41**, 095009. **[S]**
- Fuchs, J., Helmerich, C., Bobrick, A., Sellers, L., Melcher, B. & Martire, G. (2024). Constant velocity physical warp drive solution. *CQG* **41**, 095009. arXiv:2405.02709. **[F]**
- Graham, N. & Olum, K. D. (2007). Achronal averaged null energy condition. *PRD* **76**, 064001. **[S]**
- Olum, K. D. (1998). Superluminal travel requires negative energies. *PRL* **81**, 3567. **[S]**
- Everett, A. E. & Roman, T. A. (1997). Superluminal subway: the Krasnikov tube. *PRD* **56**, 2100. **[S]**
- Buniy, R. V., Hsu, S. D. H. & Murray, B. M. (2006). The null energy condition and instability. *PRD* **74**, 063518. **[S]**
- Sorce, J. (2024). On the geometric modular flow conjecture. **[S]**
- Fewster, C. J. & Roman, T. A. (2005). On wormholes with arbitrarily small quantities of exotic matter. *PRD* **72**, 044023. **[S]**
- Lach, M. *TRANSITIONS: what an index can carry, and one cell that no index can.* The Method 1.6, BUILD180 compendia bundle, `method/members/Transitions.md`. **[F]**

*The last eleven grades are this paper's own access grades and are not `TRANSITIONS`'s. Where a work
appears in both bibliographies the grades may differ, and the difference is not an error.*
