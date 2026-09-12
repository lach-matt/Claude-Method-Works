# The gate is closed — both architectures fail

> ## ⚠ NARROWED by `kerr.py`
>
> The measurement below stands exactly as recorded. The **generalisation drawn from
> it did not**: I wrote "a shift cannot terminate in vacuum", and Kerr refutes that —
> `g_tφ ≠ 0` and `T_µν = 0` everywhere outside the horizon, dragging the local frame
> at 0.5 c. The tested bump was **tanh-tapered, i.e. compactly supported**. Correct
> statement: *a shift cannot be **compactly supported** in vacuum; it **can** decay
> asymptotically.* The gate still fails — its bore needs a bounded boosted region —
> but the theorem is narrower than claimed. See `kerr.py`.

Measurement record. Drivers: `octave/run_axial.m`, `octave/run_torus.m`, `octave/tsolve.py`.

## The pincer

`residue.py` reduced the gate to two architectures and killed one:

- **Sealed gate** — the payload is boosted *relative to the shell*, crosses the 4.9 km bay in
  2.69 dynamical times, and must then transit 8.49 km of wall. A bore closes in 5.78e-06 s
  against a 5.95e-04 s transit. **Egress is impossible.**
- **Open gate** — a torus whose bore is part of the equilibrium. The only survivor, and the
  subject of this file.

## The isolation test

The open gate needs its shift to fall to zero along the bore axis, out of the mouths, where
there is **no matter**. Everything else was stripped away to test just that: flat spatial
slices, unit lapse, one compactly-supported shift bump, vacuum everywhere.

```
g_ij = delta_ij     alpha = 1     beta^x = -v S(x,s)
S = 1 in a cylinder r < 10, |x| < 8, tapering over 1.5
```

**Control (v = 0): 0 live cells, max|T00| = 0.000e+00.** Exactly Minkowski, exactly zero
stress-energy — the construction is valid.

| v | BORE | MOUTH | WALL |
|---|---|---|---|
| 0.020 | **165/165 Type IV** | **210/210 Type IV** | **154/154 Type IV** |
| 0.040 | **165/165 Type IV** | **210/210 Type IV** | **154/154 Type IV** |
| 0.100 | **165/165 Type IV** | **210/210 Type IV** | **154/154 Type IV** |

**Every cell where the shift varies is Hawking–Ellis Type IV.** Type IV means the
stress-energy has *no timelike eigenvector* — no rest frame exists, so no matter of any kind
can be it, and WEC and DEC fail unconditionally. This is not a margin that could be widened.
The magnitude scales with `v` (max|T00| 4.8e37 → 1.2e39) but **the type does not change**, so
tapering more gently does not help and neither does going slower.

## What this is

A numerical confirmation of Santiago–Schuster–Visser at the exact point where this project
needed it to fail. A compactly-supported shift on flat slices is a Natário-class drive, and
SSV proved those violate the null energy condition. Fuchs *et al.* escape SSV by co-locating
the shift gradient with **matter** — that is the whole trick, and TARGET-1 measured it working:
the shift ramps from 0.040000 to 0.000000 *through the wall*.

**An opening is by definition a place with no matter.** So the shift gradient at a bore mouth
has nothing to sit in, and it reverts to the Natário case that SSV forbids.

## Verdict

> **Sealed gate: cannot be unloaded. Open gate: cannot hold a shift.**
> **The geodesic launcher cannot be built.**

The physics of the launcher is not what failed — TARGET-1 verified the boosted flat interior
frame-independently, and it stands. What fails is that a payload can neither enter nor leave
it. Every route in or out is either 8.5 km of nuclear matter or a hole where the shift cannot
terminate.

## A failed construction, recorded

The first attempt at the open gate (`run_torus.m`) **failed its own control**: at v = 0 the
bore, mouth and far regions read −3.77e39, −2.10e39 and −3.07e39. The cause was mine — I used
the Brill–Lindquist lapse `α = (2−ψ)/ψ`, exact for *vacuum* and wrong for matter. The
Hamiltonian constraint (solved correctly in `tsolve.py`, ψ ∈ [1.039, 1.354], residual 8.8e-05)
fixes only the spatial slice; the lapse needs its own coupled equation with the stress trace.
That run is retained because it is the same failure mode as `SPHERICITY.md`'s oblate attempt
and shows the control doing its job twice.

The isolation test needed none of that machinery, which is why it settled the question and the
full construction did not.

## What survives

Nothing about the coupling family is touched. FLYBY and SLINGSHOT manufacture no shift at all —
they borrow an existing gradient — so SSV, Type IV and the bore have nothing to say about them.
They remain the only cells affirmative on all three directives.
