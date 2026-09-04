# F78.1 — s77 PUT SEED C's Z=89 FAILURE IN THE WRONG PLACE. SEVERITY: FACTUAL, CORRECTED.
# Raised and closed in the same session. No sealed file edited.

## WHAT s77 RECORDED
RESULT-S77-Z89-RESEED.md §"THE THREE SEEDS AT Z=89": *"All 15 items, reference included,
failed identically: `RuntimeError: Z=89 50 nodes 3` — the bare-Coulomb Numerov start finds
3 nodes in 5s where 4 are required. **The failure is in the SEED CONSTRUCTOR, before any
SCF.** Seed C is inapplicable at Z=89."* Carried forward into SESSION-77-COMBINED §5 and
into ORDER-FOR-S78 item 1, which asks seed D for *"a start that survives the 5s node count"*.

## WHAT IS ACTUALLY TRUE
The string `Z=89 50 nodes 3` is raised at **rt/hfc2.py line 55**, which is inside
`run2`'s iteration loop — `for it in range(maxit)` → `for a in keys` → `solve_one` → node
check. Its format is `f"Z={self.Z} {n}{l} nodes {nd}"`, and `{n}{l}` with l as an INTEGER
prints `50` for 5s. seedtest77.py's own constructor raise has a different format,
`f"seed_C Z={Z} {n},{l} nodes {nd}"`, and would have printed `5,0`. **The printed string
identifies the SCF loop, and it was read as the constructor.**
Measured directly (pack78/probeD78.py, probeD78b.py):
  * bare Coulomb -Z/r at Z=89 **CONSTRUCTS ALL 16 ORBITALS**, every node count met, 0.1 s.
  * the **FIRST SCF SWEEP** then raises `Z=89 50 nodes 3`, in 0 s — at it=0, before any
    mixing has occurred, so **no rung of the convergence ladder can reach it**: beta acts
    on the update after the solve, and the solve is what fails.

## WHAT CHANGES AND WHAT DOES NOT
**DOES NOT CHANGE: seed C remains unusable at Z=89, and s77's operational conclusion
stands.** The 52 Ha probe could not be run there, and the falsifier that ran was the 2 Ha one.
**CHANGES: the mechanism, and therefore the design requirement on any replacement seed.**
The obstacle is not constructibility. Every pure-Coulomb start constructs at Z=89 — this
was measured across Zeff = 1 .. 89 with zero node failures at every value. The obstacle is
that a start with NO SCREENING builds a first-iteration Hartree field in which the 5s
shooting lands on three nodes. **A replacement seed must produce a spatially sane DENSITY,
not merely a constructible set of orbitals** — which is a requirement about the seed's
screening, not about its shooting, and it is why seed D screens by an integer count.

## THE STANDING POINT
**An exception's TEXT names the line that raised it. Two instruments in this runtime raise
node-count errors with near-identical wording and different formats, and the difference
between `50` and `5,0` was the whole of the evidence.** Read the raise, not the sentence.