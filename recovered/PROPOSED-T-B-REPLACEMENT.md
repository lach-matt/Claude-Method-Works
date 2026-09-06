# PROPOSED — A REPLACEMENT FOR T-B. FOR M'S RULING. NOTHING IS FILED OR RUN.
# SESSION 65. Follows F65.1. Both candidates are cheap: sealed chain, no solves.

## THE REQUIREMENT F65.1 IMPOSES
A test of §5 must predict a block's first-entry order from data that **does not
contain that order**. Any α built from D(A) and D(B) at Z_open fails this
immediately. So the predictor must be displaced — in the BASE it is measured from,
or in the Z it is measured at. That gives exactly two routes and they are both here.

---

## CANDIDATE A · SHIFT THE BASE. SAME ATOM, ONE SHELL OUT.
At Z_open the base (n,l) is full. The base (n+1,l) is not. Use the same functional
form on the base that exists:

    α_shift = [D(n+1,l+1) − D(n+1,l)] / [D(n+2,l) − D(n+1,l)]     evaluated at Z_open

    PREDICT: α_shift < 1 ⟺ the lower-n channel A=(n,l+1) enters first.

A does not appear in it. **DECLARED WEAKNESS, BEFORE ANY RUN:** α_shift < 1 is
algebraically the statement that (n+1,l+1) is deeper than (n+2,l) at Z_open — the
tie-break comparison of block N+2, read at this Z. So Candidate A tests whether the
block-to-block ordering is *coherent within one atom*, which is a real claim but a
weaker one than §5 makes. It is offered because it is the honest reading of "define
α at Z_open with the base unavailable", and because it costs nothing.

---

## CANDIDATE B · TRANSFER. SAME l-PAIR, OTHER ATOMS. THIS IS THE ONE THAT BITES.
§5 asserts α is a property of *which l values collide* — ≈0.5 for s→p, ≈1.1–1.5 once
d and f are involved. If that is true, α measured on the l→l+1 step **at atoms where
all three channels are available** must predict the block outcome at Z_open, where
they are not. The 42 sealed measurements partition cleanly and the cells are full:

    l-pair     n    median α     min      max     Z range
    s->p       6      0.528     0.483    0.608    4-88
    p->d      19      1.069     0.676    1.103   12-88
    d->f      17      1.502     1.085    1.561   34-118

    PREDICT: for each of the 11 blocks, sign(median α(l-pair) − 1) predicts the
             observed first-entry order. Blocks spanning s↔p and p↔d → A first;
             blocks spanning d↔f → B first.

**THIS TEST HAS A LIVE FALSIFIER AND IT IS ALREADY VISIBLE.** Three blocks span p↔d
— 3d/4p at Z=21, 4d/5p at Z=39, 5d/6p at Z=57 — and in all three the lower-n channel
enters first, which requires α < 1. The transferred p→d median is **1.069 > 1**.
On its face Candidate B is heading for 8/11, not 11/11, with the p↔d blocks failing.

If that is the outcome it is a **result, not a defeat**: it says α is not a function
of the l-pair alone, that n or the core state moves it, and §5 must be refined to
name what else it depends on or withdrawn. Either way the session learns something,
which T-B could not have delivered.

---

## RECOMMENDED
**Run BOTH, file the prediction for both before either is run, score both.** They
are the same instrument and one run. Standing practice: let the comparison decide.
A alone risks confirming a weaker claim than §5; B alone risks reading a failure of
transfer as a failure of the explanation. Together they separate those two.

## WHAT IS NOT PROPOSED
No new solves. No edit to `alpha.py` (it is sealed in pack64) — a new driver
`pack65/ablocks.py` beside it, F44.1 route. No change to the assembly. Item 2 of the
s65 work list (M's ruling on ASSEMBLY-REVISION-S64 R1–R4) is untouched by this and
is still owed.
