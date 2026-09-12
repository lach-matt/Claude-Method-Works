# The ceiling was an artefact, twice over

### A correction to nine papers in this series, and a withdrawal of the objection that prompted it

**Status:** correction. Measured with Warp Factory under GNU Octave 8.4, drivers
`octave/run_nec.m`, `octave/run_nec2.m`, `octave/run_attrib.m`.

---

## 1. First, a withdrawal

`WHAT-BINDS.md` §5 and `paper/PAPER.md` §6 raised what they called "the paper's most significant open
item": that Warp Factory contracts the stress-energy with `k = (1, n̂)` built in the **coordinate**
basis, and that at the failure locus (lapse `α = 0.769`) such vectors have `|g_µν k^µ k^ν|` up to
0.494 — spacelike, not null.

**That objection is wrong and is withdrawn.** `getEnergyConditions` calls
`doFrameTransfer(metric, energyTensor, "Eulerian", …)` *before* contracting, and
`getEulerianTransformationMatrix` is documented and implemented as the Cholesky factor satisfying

```
M' * g * M = eta
```

so `M` is a tetrad and the tensor is moved into a **local orthonormal frame**, where `(1, n̂)` is
genuinely null. There was nothing to object to. I read the contraction without reading the frame
transfer that precedes it.

---

## 2. What is actually wrong: the index is lowered with the wrong metric

Reading the same path properly, the null branch does this:

| step | operation | correct? |
|---|---|---|
| 1 | `T_µν` coordinate, covariant | — |
| 2 | `M' T M → T_âb̂`, orthonormal frame, covariant | ✅ |
| 3 | flip `0i` signs → `T^âb̂`, i.e. **raise with η** | ✅ |
| 4 | `changeTensorIndex(…, "covariant", metric)` → **lower with `g`** | ❌ |
| 5 | contract with `k^â = (1, n̂)/√2` | — |

Step 4 lowers **frame** indices with the **coordinate** metric. Those are different index types;
`g` knows nothing about the frame basis. The correct step is to lower with `η`, which exactly undoes
step 3 and returns step 2's tensor. `changeTensorIndex` is not a no-op here — it dispatches to
`flipIndex` with the covariant coordinate metric.

**Validation.** Computing the NEC three ways on one tensor:

- `FRAME` — contract step 2's `T_âb̂` with `(1, n̂)/√2`. *(correct)*
- `COORD` — contract the coordinate `T_µν` with `k^µ` rescaled so that `g_µν k^µ k^ν = 0` exactly.
- `SHIPPED` — as above.

`FRAME` and `COORD` are the same scalar sampled over different direction sets. They agree to **4.4 %**
(−2.87794e36 vs −2.75640e36 at `dx = 1 m`). `SHIPPED` differs from both by **1.49×**. The correction
is confirmed from two independent directions.

---

## 3. And a second error, which is mine

`run_sweep.m` — and therefore every measured number in `MEASURED.md`, `WHAT-BINDS.md`,
`THE-DESIGN-EQUATION.md`, `DENSITY-IS-CLOSED.md`, `SPHERICITY.md` and `paper/PAPER.md` — took the
minimum over the slice `(1, 4:end-3, 4:end-3, 3)`. Splitting that slice into the shell interior
(10.5 < r < 19.5 m) and everything else:

```
  vWarp              PUB          SHELL      PUB\SHELL   r@PUBmin
  0.0000    -2.24433e+35    1.71339e+39   -2.24433e+35      27.23
  0.0200    -2.24433e+35    8.09101e+38   -2.24433e+35      27.23
  0.0218    -2.24433e+35    7.25577e+38   -2.24433e+35      27.23
  0.0300    -2.24433e+35    3.22738e+38   -2.24433e+35      27.23
  0.0350    -2.24433e+35    9.72983e+35   -2.24433e+35      27.23
  0.0400    -4.16307e+38   -4.16307e+38   -8.43947e+37      11.75
  0.0450    -8.40885e+38   -8.40885e+38   -3.07567e+38      11.75
```

The published minimum is **constant at −2.24433e35 for every shift value including zero**, and it
sits at **r = 27.23 m** — outside the shell (`R₂ = 20 m`), out at the grid boundary. `PUB\SHELL`
equals `PUB` exactly at every row up to 0.035. **The published minimum was bare-shell grid-boundary
truncation error and never measured the shift at all.** It only stops being the minimum at
`v ≈ 0.04`, when the real shell-interior violation grows past it.

The published ceiling was obtained as a "least-squares zero of the null-condition minimum in its
linear regime". Fitting a line to a constant and extrapolating it to zero is not a measurement.
That error is mine, not Warp Factory's.

---

## 4. The corrected numbers

Measured in the shell interior, `dx = 0.5 m`:

| diagnostic | slice | threshold | factor |
|---|---|---|---|
| shipped | published (`4:end-3`) | **0.0218 c** | *(published — withdrawn)* |
| shipped | shell interior | **0.0350 c** | 1.61× |
| **corrected (η)** | **shell interior** | **≈ 0.045 c** | **1.27× further** |
| | | **total** | **≈ 2.05×** |

Both errors ran in the same direction: they made the drive look **worse** than it is. The
shell-interior corrected threshold is approximately **twice** the published ceiling.

The corrected figure carries a caveat: it is a linear interpolation across a coarse bracket
(+6.52777e38 at 0.040, −2.21289e39 at 0.060) and wants a finer scan before it is quoted to three
digits. `≈ 0.045 c` is what this measurement supports.

---

## 5. What this does to the rest of the series

**Withdrawn outright** — every absolute figure that descends from the published slice:

- the **0.0218 c** ceiling (`MEASURED.md`, `paper/PAPER.md` §4.1);
- the "**8.5 % headroom**" at the published operating point, and the claim that Table 1 of
  Fuchs *et al.* runs "84 % over its own threshold" — both were computed against an artefact, and
  **the criticism of the published paper is withdrawn with them**;
- the class bound **≈ 0.047 c**;
- the failure locus at **12.51 m** (the corrected minimum sits at 11.27–11.75 m).

**Unvalidated, not withdrawn** — the ratios. The 1.599× profile gain, the fill curve, the
factorisation test and the density sweep were each measured with one instrument on one slice
throughout. The boundary floor does not depend on the shift profile, so a threshold set by "when
does the shift violation exceed the floor" is monotonically related to the true threshold rather
than unrelated to it. The ratios are therefore contaminated but probably not meaningless. **They
have not been re-measured**, and until they are, none of them may be quoted.

**Not re-measured, by decision.** Re-running the profile, fill, density, sphericity and locus sweeps
on the corrected diagnostic and the corrected slice is a session's work. It is not being spent,
because the shell is no longer the object of this project: `THE-ENGINE.md` sets out why a sourcing
design fails by 10³¹ regardless of where its ceiling sits, and a 2× correction to a number that is
31 orders from useful does not change any conclusion that matters. The correction is recorded so the
record is true, not so the shell can be rehabilitated.

---

## 6. What stands

Nothing in this correction touches the two results the series actually rests on:

- **ADM 4-momentum conservation forbids self-acceleration at positive ADM mass.** Analytic, no
  Warp Factory involved.
- **The 10³¹ gap** between attainable stress-energy and the shell's requirement. Arithmetic on
  published material properties.

Both survive intact, and both are why the project moved to a coupler.

---

## Reproduction

```
cd <scratch>                      # Warp Factory clone + shims, see octave/README.md
WF_SCALE=1 WF_VLIST="[0.02 0.03]" octave --no-gui --quiet \
  --eval "addpath(genpath('./wf')); addpath('./shim'); run('./run_nec.m')"   # 3-way validation
octave --no-gui --quiet --eval "addpath(genpath('./wf')); addpath('./shim'); run('./run_nec2.m')"
octave --no-gui --quiet --eval "addpath(genpath('./wf')); addpath('./shim'); run('./run_attrib.m')"
```
