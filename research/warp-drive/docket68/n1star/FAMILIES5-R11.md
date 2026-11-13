# FAMILIES5-R11 -- round 11: the last minor and four nits of the round-10 reader

The round-10 reader confirmed that Major 1 is fixed everywhere and found no new Major. It confirmed several things:
- mbslice5 S4 and S5 are exact, with complete substitutions;
- l = 6 and 8 pass;
- the degree count is M + 4;
- the new controls test the pass conditions;
- the R10.1 block is correct.

One minor and four nits remained. Each is seated below. Bracketed [R11] notes mark the affected lines in
FAMILIES5-R10.md, FAMILIES5-MB.md, FAMILIES5-R8.md and FAMILIES5-R6.md. Nothing in the paper or N1STAR-PROOF.md is
edited.

## R11.0 What was done

- **minor 1 (E4 (b) was a three-angle check).** *Computed.* `checks/mbslice5.py` S4 now does (b) by the same exact
  route as (a) and (c), for every (R, θ, μ).
  - The shifts of (a, b, c, e) under L_X γ, with X = αS∂_R + βS′∂_θ, hold in every component.
  - The lapse direction's trace-free angular part is ψ Ŝ^TF.
  - Controls (rejected): 2k²/3 → k²/3 in the c-shift; the lapse claim doubled.
  - So R10.1's "the reduction … computed exactly", and MB §6's row for the modes and gauges, now cover (a), (b) and
    (c) on every slice.
- **Nit 1.** MB §6's status table, which the round-10 edit had reflowed into a paragraph, is restored as a table. Its
  [R10] and [R11] entries name mbslice5's exact checks.
- **Nit 2.** "Degree M + 4" holds for single-harmonic sources. Coefficients nonlinear in g_app carry products of
  harmonics, which only add terms, so under this bookkeeping the degree is **at least** M + 4.
  - nledger5's print and docstring say so; rerun, PASS.
  - [R11] notes are added at FAMILIES5-R10.md, FAMILIES5-R8.md R8.4's note and FAMILIES5-R6.md §4.
  - Computing the full degree with products was not attempted. Products of p harmonics have unbounded p for
    coefficients nonlinear in g_app; at fixed order in λ they are finite, but which orders the bootstrap reads would
    have to be fixed first. The statement is now a lower bound, which is what the record supports, and the count
    enters only the constants.
- **Nit 3.** S4 (a)'s θ-freeness test now has its own control. The eigen-relation with cot θ − tan θ → cot θ leaves
  the coefficients of C and E_V θ-dependent, and the test rejects them.
- **Nit 4 (the band √μ3 < R < R_EH).** The argument is written out in `checks/ehband5.py` and in the [R11] notes, and
  labelled deduced. It is also computed on the computed background.
  - The argument: on Σ_τ0, R = √μ3 lies in region III, and its outgoing ray is marginal until the ingoing shell
    arrives. There A > 0 makes e^(−2s)R_v strictly decrease, so the ray ends trapped, and with A ≥ 0 it stays trapped.
    Trappedness is open in the starting radius.
  - ehband5 H1 (floating point, twobg5 at n = 80 and 160): every grid row crossing Σ_τ0 between √μ3 = 0.9067 and
    R_x = 1.000 is untrapped at the crossing and ends trapped. Every row from 1.005 up ends untrapped.
  - Control: with the ingoing shell removed, no row above √μ3 is trapped.

**Programs changed or new, rerun in full**, `.out` saved, PASS:
- `checks/mbslice5.py` (S1-S5, with S4 (b) and the θ-freeness control new);
- `checks/ehband5.py` (new; H1 and its control);
- `checks/nledger5.py` (L2's wording).

## R11.1 The paper block

The R10.1 block stands unchanged; this round changes no word of it. Its "(the reduction and the positivity computed
exactly; …)" is now true of E4 (b) as well, through S4 (b). The single old/new pair in the wording file is the
paper's current "More families" bullet (OLD) and FAMILIES5-R10.md R10.1 (NEW), as before.

## [R11-nits] The confirming reader's two nits

- **S4 (b)'s controls changed the target, so they could not fail once (b) passed.** They are replaced by input
  mutations:
  - the vector field X = αS∂_R + βS∂_θ, with S in place of S′, fails the shift formulas;
  - the lapse ψS′ in place of ψS fails the trace-free claim.
  Both are rejected. `checks/mbslice5.py` was rerun and its `.out` saved: S1-S5 PASS.
- **"Ends trapped, so it lies in the black-hole region"** is now named in ehband5's docstring and in MB's status note.
  It is the standard result that a trapped surface lies inside the black-hole region of a strongly asymptotically
  predictable spacetime satisfying the null convergence condition: Wald, General Relativity (1984), Proposition 12.2.2;
  Hawking and Ellis (1973), Proposition 9.2.1.
  - Not READ at source: neither book is reachable here. It is cited in arXiv:1909.02001 and in
    doi:10.1007/s10714-024-03245-5, Appendix A.
  - It holds in five dimensions: the proof uses only the null Raychaudhuri equation and the causal structure of
    J⁻(I⁺), and vacuum and null dust satisfy the null convergence condition.
  - In this SO(4) class the direct argument also suffices (deduced).
- **One sentence of the R10.1 block is reworded** (the final-pass audit), and the wording pair is updated to match.
  "These hypotheses are open for perturbations whose supports stay in a fixed compact set …" now reads "These
  hypotheses hold on an open set of solutions: they persist under perturbations small in C² × C¹ whose supports stay in
  a fixed compact set and whose radial dusts keep adapted boundaries (deduced)".
  - This is Lemma O″'s content, with "open" unambiguously topological.
  - No other word changed; the generator now also keeps short formulas such as "f > 0" on one line.
