# Scratch derivations behind kn_gauge.py and counterpart5.py (items 517-520)

These are the working scripts the board ran while deriving the KN gauge and measuring the counterpart proof. They
are **not seated instruments**. The seated versions are authoritative:
`../../lemmas/kn_gauge.py` (K1-K8) and `../../lemmas/counterpart5.py` (P1-P5). They are kept so that a later
session can see how each result was reached. Run each one from its own directory, because they read the `.pkl`
files beside them by relative path. sympy and numpy; some need mpmath.

- `kn/red.py`, `kn/red2.py`: 5D Ricci of g3 + e^(2U1) dphi1^2 + e^(2U2) dphi2^2, and the torus-frame identity.
  Seated as kn_gauge K1-K2.
- `kn/mult.py`, `kn/design.py`, `kn/mproof.py`: the multiplier X = alpha d_v - sigma d_r on 5D Vaidya, its bulk
  form, the design scan, and the root counts. Seated as kn_gauge K5.
- `kn/lin.py`, `kn/lin2.py`, `kn/hlin.py`: the base equations linearized about Tangherlini in the torus frame (the
  v-row). Seated as kn_gauge `_lin_base`.
- `kn/hsolve*.py`: the first-order response: c_p from r-theta, h_vv's ODE from theta-theta, and the supplementary
  constraints. Seated as kn_gauge `_k8_core`.
- `kn/k8.py`, `kn/k8ext.py`, `kn/k8m.py`, `kn/k8v.py`: the error form against X's bulk on the grid, kappa_ext,
  mutants and validation. Seated as kn_gauge `_k8_core` and `_k8_shell`.
- `kn/dbg9.py`: the timing test that kept c_p an undefined function, taking the K8 core from 45 minutes to 3.
- `kn/run1.py`: replays one T1 instrument's selftest in process. It found the T1 failure at hf_core5 C1.
- `kn/*.pkl`: intermediate sympy results the scripts above read.
- `cp/hier.py`: the KN gauge's hypersurface hierarchy, which derivatives each equation holds (the Bondi loss).
  Seated as counterpart5 P2.
- `cp/couple.py`: the background Killing norms' wave operator linearized in the base metric (the O(1) coupling).
  Seated as counterpart5 P3.

Caution from item 520: the K5 multiplier and its constant 35 bound T^2-invariant **test fields**; the class's linear
problem is linearized gravity (counterpart5 P3). K6's well-posedness claim for the KN gauge is withdrawn: its
hierarchy loses two angular derivatives (counterpart5 P2).
