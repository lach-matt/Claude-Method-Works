# Item 197: our plane sees its own reflection, not the other plane (computed, deduced and STRUCTURAL; not verified by a separate session; not seated; 2026-10-10)

*First headed* 2026-10-10, on M's item 197, worked in the conversation (no workflow). Instrument:
`lemmas/m1_facing.py` (selftest 14/14, mutants 8/8). It imports `lemmas/f1_audit.py` and `tools/cypher.py` by path.

## What you said

The board's F1 audit (`lemmas/F1-AUDIT.md`) reported that a plane on its own can read eq. (17) smoothly only if it
carries extra matter. You quoted that sentence back and added a clause (item 197, verbatim):

> "A plane on its own can read eq. (17) smoothly only if it carries extra matter. - because it sees its own
> reflection, not the other plane"

The first sentence is the board's. The clause after the dash is yours: **M-SEES-OWN-REFLECTION**.

## Plain words first

- **You were right about where the extra matter came from** (computed). The F1 audit's single plane was a mirror
  construction, so the bulk beyond our plane was a copy of our own side. Its horizon then had to close back on
  itself, on a cap, and only extra matter on our plane makes that closing smooth: 8.02 times our tension at SIM2's
  edge.
- **Facing the other plane, our plane needs no extra matter at all** (computed). It carries its tension and nothing
  else, reading eq. (17) exactly. The bulk runs from our plane toward the singular depth y_s, and position 2's plane
  sits before y_s and ends it. The horizon then runs from plane to plane and is bounded by them, so it no longer has to
  close on itself.
- **The reflection itself is not removed. It is forced, locally** (STRUCTURAL, computed). A plane carrying only its
  tension and reading eq. (17)'s equal radii has only one solution: the bulk is a mirror image on its two sides near
  the plane, whatever lies beyond. So what your 197 changes is not the plane but **where the bulk ends**: on its own
  image (a cap) or on the other plane.
- **What is needed moves to position 2's plane**, and there it is admissible over a range of depths (computed):
  - null energy holds at every depth, at every ℓ tested;
  - with position 2's tension at your 139 (1)'s "a quarter of ours", the energy left over is positive in a band of
    depths once ℓ > 8.54m. Every real README is far past that, because its mouth is tiny against the window's ℓ;
  - it is negative at coincidence itself, at every ℓ. That agrees with SIM2-FACING: positive energy needs the
    approach held at a depth, not coinciding.
- **The question the board held for you after the F1 audit is moot** (deduced): our plane needs no added stress, so
  whether it may carry the README's stress does not arise. It is withdrawn, not put.
- **No status moves; nothing is seated.**

## The facts

All of these are in the F1 audit's own class: Kaus–Reall's warped-product near-horizon geometry,
ds² = A(ρ)² dΣ²(AdS₂) + dρ² + R(ρ)² dΩ², with a vacuum bulk R_AB = −(4/ℓ²) g_AB. That is the throat region only, not
the full bulk.

1. **The mirror lemma, L1** [C1; STRUCTURAL, computed symbolically with sympy].
   - At a plane reading equal radii A = R, the bulk constraint on each side is a² + 4ab + b² = 6. Here
     a = ℓA′/A and b = ℓR′/R, along that side's outward normal.
   - A plane carrying only the RS tension needs (a₁ + a₂)/2 = (b₁ + b₂)/2 = 1.
   - The only solution is a₁ = b₁ = a₂ = b₂ = 1. Second-order uniqueness then makes the two sides the same solution:
     **local mirror symmetry is forced.**
   - Control: once added matter is allowed, the two sides need not agree. That case is computed.
   - A different ℓ on the far side is outside the lemma. The discriminant is 3(r − 1)(r − 9) with r = (ℓ/ℓ₂)², so
     there is no real solution for 1 < r < 9. In any case the tension there is not σ_RS.
2. **The single plane, reproduced** [C2, computed]. The compact-horizon cap at 2m/ℓ = 0.0739 needs
   ρ = 8.017 σ_RS and p = −1.480 σ_RS on our plane (F1-AUDIT C6).
3. **Facing** [C3, C4; computed, RK4]. Our plane P1 carries the RS tension only and has eq. (17)'s Q = 0 data:
   A = R = 2m, with slopes −1/ℓ into the bulk. Position 2's plane P2 is a Z2 plane at constant depth y₂ < y_s.
   - **P1's added matter is exactly 0.**
   - P2's stress, in units of σ_RS: e₂ = −(α + 2β)/3 and P₂ = (2α + β)/3, with α = −ℓA′/A and β = −ℓR′/R at y₂.
     Then e₂ + P₂ = (α − β)/3.
   - **The NEC holds at every sampled depth on (0, y_s), at all six ℓ** (2m/ℓ = 0.0044 to 1.72). The minimum is
     positive, falling to 0⁺ at coincidence.
   - As y₂ → 0, P2 tends to the RS1 sheet (e₂, P₂) → (−1, +1). That is SIM2-FACING S15's limit, found there in the
     full static bulk.
4. **The energy left on P2 after its tension** [C5, C6, C6b; computed].
   - Your 139 (1), verbatim: *"1 - yes"*, to *"whether position 2's plane is the negative-tension one, a quarter of
     ours, with ours positive"*. With ours at exactly σ_RS (clause (B) as worded), that is q₂ = −1/4 on one sheet.
     That is the per-sheet count. The doubled count gives −1/8 per sheet (`COUNT-CYPHER.md`; which count holds is
     undecided).

     | q₂ subtracted | remainder positive in a depth band when | at coincidence |
     |---|---|---|
     | −1/4 (139 (1), per-sheet) | ℓ > 8.5415m (2m/ℓ < 0.23415) | −3/4, at every ℓ |
     | −1/8 (139 (1), doubled, per sheet) | ℓ > 10.3998m | −7/8 |
     | −1/3 (M4) | ℓ > 7.3007m | −2/3 |
     | −1 (the RS1 sheet: the trace's coincidence value) | every ℓ tested | 0⁺ |
     | +1 (H-SPLIT-AT-OUR-TENSION, for comparison) | ℓ > 27.0665m | −2 |

   - The +1 row reproduces SIM2-FACING's 27.07m edge. That is the same configuration in its throat limit, so it is
     a **consistency check, not independent evidence**. That reading treats P2 as a piece of our own plane; your 139 (1)
     and 197's *"the other plane"* both read against it.
   - At ℓ = 454.5m (2m/ℓ = 0.0044) the band for −1/4 is y₂/y_s ∈ [0.008, 0.784]. For any real README 2m/ℓ is far
     smaller still: the mouth is subatomic and ℓ is of order microns.
5. **Controls** [C7, computed]. With P2 removed, the Q = 0 bulk reaches A → 0 at y_s, and the single-plane verdict
   returns. With P2 at or past y_s, the slab holds the singularity.
6. **A second engine** [C12, computed]. Scipy DOP853 (rtol 10⁻¹¹), with its right-hand sides typed independently,
   agrees on y_s to 10⁻⁴ relative and on the 27.0665m threshold. Its constraint residual is at most 1.1×10⁻⁴.

## The cypher run (your 196)

- **The binary statement:** *Facing the other plane P2 rather than its own reflection, does our plane read eq. (17)
  regularly with no matter beyond the RS tension?*
- **The encoding** is H-CYPHER-FACING, the board's. Each cell is a configuration the board computed, and no premise
  is entered as a cell. Coordinates:
  - face: reflection, or the other plane;
  - end: cap, P2, or y_s;
  - extra: none, or added matter;
  - regular: no, or yes.
  - The four cells are: one plane at Q = 0, singular; one plane with a cap and added matter (F1 C4–C7); facing at
    y₂ < y_s, regular; facing at or past y_s, singular.

| language | state | E | MAIN (facing cell in) | MAIN, facing cell left out | CONTROL: facing its reflection, no added matter, regular |
|---|---|---|---|---|---|
| order | SPEAKS | 11 | YES | NO | **YES** (structural caveat) |
| algebra | SPEAKS | 11 | YES | NO | **YES** (structural caveat) |
| analysis | declared witness needed; not run | — | — | — | — |
| geometry | SPEAKS | 1 | YES | NO | NO (native ordering) |
| information | SPEAKS | 4 | YES | NO | NO, under every ordering of *end* |
| statistics | SPEAKS | 0 | YES | NO | NO, under every ordering of *end* |
| documentary | SILENT (by construction) | — | — | — | — (citations: F1-AUDIT C2–C7, SIM2-FACING S15, M's 139 (1), 197) |

- **What logic cites back:**
  - MAIN is admitted with the facing cell in. That is **forced: the cell is data** (the extensivity `COUNT-CYPHER.md`
    found). It is not evidence.
  - **With it left out, no language regrows it, under any of the six orderings of *end*.** The other plane is not
    implied by the reflection cells. A plane on its own cannot know the other plane, which is the content of your 197,
    classified rather than derived.
- **The control:** a plane facing its reflection, with no added matter, still regular.
  - Information and statistics refuse it under every ordering; geometry refuses it on the native ordering. So the
    binary flips for those three.
  - Order and algebra admit it. Their closure reaches a cell the computation refutes (F1 C2 and C4–C7). That is a
    **STRUCTURAL caveat**, recorded.

## What it does to M1 and the chain

- **M1's single-plane clause no longer decides it.** The F1 audit's single-plane failure was the plane facing its
  reflection. Your configuration is the facing form, and there our plane needs no added matter.
  - M1-d's H-OWN-MATTER-ONLY is met on our plane without strain: it carries its tension and our universe's matter.
  - The held question about the README's stress on our plane is moot and withdrawn.
- **M1's bridge form is SIM2-FACING's configuration.** What it still needs:
  - **Whether a whole P2 exists:** phase 2b-i, a free-boundary problem, together with OPEN G and E-FAR.
  - **P2 positive at the depth it is held:** ℓ above 8.54m on the per-sheet count, never at coincidence.
  - **M1-P2:** position 2's side reading eq. (17)'s other leg. Untouched here; P2 reads unequal radii in general.
- **No status moves.** M1 stays OPEN, F1 stays replaced by M1, and the chain is not green.

## What it does not show

- **Near-horizon class only:** the throat region, not the full bulk. SIM2-FACING carries the full static bulk's
  version, and the two agree on the 27.07m edge and on the coincidence limit.
- **P2 at constant depth, as a Z2 plane.** Its one-sided form, with position 2's own bulk beyond, and its shape
  away from the throat are not computed.
- **Static.** The write, E-NS and E-ROT are untouched.
- **Not verified by a separate AI session.** The checks are the instrument's own: its controls, a second engine and
  eight mutants.

## OPEN

1. Phase 2b-i: whether a whole P2 exists over the band or down the throat (SIM2-FACING), now with 139 (1)'s quarter
   tension as P2's.
2. Which count holds for P2's tension per sheet: −1/4 or −1/8 (`COUNT-CYPHER.md`).
3. Whether the held README's energy E(N) is what sits on P2 (172 (1)), compared only after fixing Killing against
   proper energy (the F1 audit's caution).
4. M1-P2, and O1c (geodesic completeness).

## Named hypotheses (the board's, never yours)

- **H-WHERE-THE-BULK-ENDS:** 197 read as follows. The reflection is local and forced (L1); the extra matter comes
  from the bulk closing on itself; facing the other plane, the bulk ends on it.
- **H-CYPHER-FACING:** the index encoding above.
- **H-SPLIT-AT-OUR-TENSION** and **H-LAW-READ-BY-TRACE:** carried from SIM2-FACING, for comparison only.

## History

- 2026-10-10: first headed on item 197. The board first launched a workflow, then stopped it on M's word (*"I'm not a
  fan of these workflows. It feels like we get more done more quickly when we do it here"*) and worked it here.
  - L1 proved with sympy.
  - Facing computed with f1_audit's own integrator; the second engine agrees.
  - The cypher was run with a leave-out and a control.
  - Thresholds computed for 139 (1)'s quarter tension under both counts.
  - `m1_facing.py`: selftest 14/14, mutants 8/8.
  - Not seated.
