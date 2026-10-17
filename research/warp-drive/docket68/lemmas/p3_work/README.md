# p3_work: P3(a) in progress (BOUNCE-RESEARCH section 24). Not seated, not verified.

Working code for the interior of P2's lambda = 64 hole, kept so the work survives the session.

- `inner.py`: the interior chart (r^2 -> -rho^2).
- `insolve.py`: sigma = rho^2 slabs from horizon data.
- `across.py`: one solution across the horizon in s = r^2.
- `slab_s.py`: interior-only Cauchy slabs.
- `refslab.py`: the same with a field-valued DeTurck reference, optional constraint damping, and even parity in x.
- `acrossref.py`: the global solve with that reference.
- `deeper.py`, `control.py`, `evenmarch.py`, `arun2.py`: the drivers.

Paths inside point at the session scratchpad: P2's saved solutions (`H20_lam64_mt0.843.npy`, `E20_bt2_mu0.000.npy`)
are not in the repository. An instrument with a selftest replaces this directory once P3(a) is settled.

## Under item 462: the magnetic corridor, marched (BOUNCE-RESEARCH section 26)

- `p3m.py`: the magnetic field-on-the-plane system. The bulk is vacuum Einstein-DeTurck with Lambda_5. The plane's
  field enters Israel's condition as kappa/g_OmOm^2, with the true unit normal. It provides a global static solve and
  interior slabs in two variants: regular axis (S = B + x^2 Sigma) and Gundlach constraint damping.
- `kretsch.py`: a numerical Kretschmann scalar and mixed Ricci tensor from g, dg, ddg. Tested on AdS5 (40),
  Tangherlini (72 mu^2/r^8) and Schwarzschild x R.
- `p3curv.py`: that engine attached to the s-chart.
- `einres.py`: the reference-free Einstein residual max|R^a_b + 4 delta^a_b|. Inside the horizon xi^2 is not
  positive and does not certify a solution; this does.
- `march_m.py`, `diagmarch.py`: the marches.
- `run_global.py`, `ctrl0.py`, `kglobal.py`, `kappa.py`: the static solves, the uncharged control, the curvature over
  a global solution, and kappa read from P2's member.
