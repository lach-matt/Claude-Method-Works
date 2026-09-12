# The loop, and the theorem it produced

`ROTATING-SHELL.md` — written near the start of this project — established:

> *"A single rotating shell carries ADM angular momentum, so its exterior is Kerr rather than
> Schwarzschild — and the Fuchs construction is built on a Schwarzschild exterior.
> **Counter-rotation sets `J = 0` exactly, the `g_tφ` frame-dragging term vanishes**, and the
> exterior is restored."*

`kerr.py` — twelve exchanges later — announced that `J` sources a vacuum shift as though it were
new. **It was not new. The project had looped.**

## Why the index did not catch it

The index held 32 findings and computed `E(X) = 0`. But **nine papers had never been seated**,
`ROTATING-SHELL.md` among them. A finding the index does not hold cannot be predicted by its own
closure, so `E(X) = 0` over an incomplete `X` was measuring the completeness of the **bookkeeping**,
not of the knowledge.

Fixed: all nine seated, and `index3.py --selftest` now fails if any paper in the tree has no cell.
That guard caught `SOURCE-CODE.md` on its first run.

## What the two visits give together

Neither visit alone was the theorem. Put side by side:

| | |
|---|---|
| **ROTATING-SHELL** | the shell **requires** `J = 0`, or the Schwarzschild exterior the whole solution rests on is destroyed |
| **KERR** | `J ≠ 0` is exactly what produces a vacuum shift |

**The shell's own boundary condition forbids it the only vacuum-shift mechanism that exists** — and
not by coincidence, but through the same quantity. That is the theorem, and it took returning to the
same place from the opposite direction to see it.

## The trichotomy

Every route to a shift is closed, and all three by one accounting — **the charge that sources it**:

1. **Translation** needs linear momentum `P`. `CM-THEOREM`: an isolated system cannot manufacture it.
2. **A vacuum shift** needs `J ≠ 0`. But `J ≠ 0` gives a Kerr exterior, which breaks the construction
   (`ROTATING-SHELL`), and its transport is **circular** — it points nowhere (`kerr.py`).
3. **`J = 0`** preserves the Schwarzschild exterior and the translation-shaped geometry — and leaves
   **no vacuum shift at all**, so the shift must live inside matter, which is where `NO-TAPER` and
   SSV bite at any opening.

Want translation, you need `P`, forbidden. Want a vacuum shift, you need `J`, and you get rotation.
Want the geometry to stay translational, you set `J = 0`, and the shift has nowhere to live but
matter — which closes at the first hole you cut in it.

## The loop was the instrument

In this corpus's own terms, arriving at a cell from a second, independent coordinate is not waste —
it is how a region is shown to be **closed**. The trichotomy is not three separate failures. It is
one bounded region, and the loop is what measured its boundary.

What it does not touch: the coupling family, which manufactures no shift and therefore owes no
charge. `FLYBY` and `SLINGSHOT` remain the only cells affirmative on all three directives.
