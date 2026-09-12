# Running Warp Factory under GNU Octave

Warp Factory (Helmerich & Fuchs, MIT, `github.com/NerdsWithAttitudes/WarpFactory`) is MATLAB and
wants the Curve Fitting and Parallel Computing toolboxes. It runs under **GNU Octave 8.4** with the
five shims in `shim/` and three one-line compatibility edits to the clone. Nothing here is copied
from Warp Factory; the toolkit is cloned at run time and cited, never vendored.

```sh
apt-get install -y --no-install-recommends octave          # 8.4.0 on Ubuntu noble
git clone --depth 1 https://github.com/NerdsWithAttitudes/WarpFactory.git wf
#   apply the three edits below to ./wf
WF_SCALE=2 WF_VLIST="[0 0.02 0.025 0.03 0.04]" \
  octave --no-gui --quiet --eval "addpath(genpath('./wf')); addpath('./shim'); run('./run_sweep.m')"
```

## The shims

| shim | why |
|---|---|
| `smooth.m` | Curve Fitting Toolbox. Moving average over an odd span with symmetrically shrinking end windows, which is what `smooth(y,span)` does by default. |
| `isgpuarray.m`, `gpuArray.m`, `gather.m`, `canUseGPU.m` | Parallel Computing Toolbox. Identity / always-false. |
| `pagemtimes.m` | R2020b batched matrix multiply. One call site, `Mᵀ·T·M` over 4×4 pages; vectorised over the trailing dimensions. |

## The three edits to the clone

1. `Solver/verifyTensor.m` — `string(x)` → `char(x)`, and `"lit" + string(x)` → `["lit" char(x)]`.
   Octave has no `string` type and `+` on char arrays is arithmetic. Cosmetic: validation messages only.
2. `Analyzer/utils/getEulerianTransformationMatrix.m` — `sum(X,'all')` → `sum(X(:))`. Octave 8 has no
   `'all'` option.
3. `Analyzer/utils/generateUniformField.m` — **a real bug, not a compatibility issue.** It passes a
   hard-coded `1` as the `useGPU` argument to `getEvenPointsOnSphere` in three places, ignoring its
   own `tryGPU` parameter. So `evalMetric(metric, 0, 1)` — the documented CPU path — still reaches
   `zeros(...,'gpuArray')` and fails on any install without the Parallel Computing Toolbox. Passing
   `tryGPU` through fixes it. Worth reporting upstream.

`run_sweep.m` builds the metric once and rescales `g_tx`, which is exact: the shift enters the build
only as `g_tx = −S_warp(r)·vWarp` on an otherwise diagonal metric, so nothing else depends on it.
That turns an N-value sweep into one 2-minute build plus N six-second evaluations.

Results are in `../MEASURED.md`.
