# Paper register — what goes in, and what it rests on

Every row is a claim this project would defend in print. Each names the instrument that produces it,
whether it is **new**, whether it **corrects** something in the literature, and what would falsify it.
Nothing enters this file that an instrument does not compute.

Status vocabulary follows the corpus: `PROVEN` (closed-form and verified), `MEASURED` (computed from
data or a seated member), `CONDITIONAL` (holds under a stated assumption), `PROPOSED` (an experiment
or a design, not a result).

---

## ★ HEADLINE — flagged for the abstract

**H1. The standing objection to warp drives is an artefact of the wrong instrument.**

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

**H2. The consequence: the requirement changes category, not merely magnitude.**

> `M = −β²c²R/(12G)` at the thickest admissible wall. R = 100 m at 0.1 c costs **18.8 Earth masses**
> against Pfenning–Ford's **1.5 × 10⁹ observable universes** — a factor 2 × 10³⁶. The remaining gap to
> a laboratory negative-energy source is 2.3 × 10⁴², which is large **and has no theorem in it.**

| | `designpoint.py`, `warpenergy.py` |
|---|---|
| status | **CONDITIONAL** on H1 |
| new? | the design equation, yes |
| falsified by | H1 failing; or a flatness requirement stricter than σR ≈ 3 |

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

- That a warp drive can be built. H1 removes a stated impossibility; it does not supply negative energy.
- That the warpshell is viable — the ℓ≥2 instability stands (**S5**).
- That QNEC has been applied. `shape.py` predicted the energy-condition family would loosen and named
  QNEC; what landed was timelike-QI → null-SNEC. **Right family, wrong member — scored 0.5, not 1.**
- Any figure carrying the SNEC's four O(1) exposures as if it were exact.
