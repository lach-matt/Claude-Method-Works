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
