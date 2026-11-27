# P-APPC2: Appendix C rewritten around the rule (writer's report, as handed back)

File: proofs/P-APPC2.md, md5 17ddd6468c288a0af34a64bac0e52ab7, 1,412 lines. Working copy in the writer's scratchpad.

Checks (scratch tree, the appendix as chapters/97-approximant.md): lint --chapters 13 hits, all pending markers;
assemble --check 0 problems; the in-memory assembled lint 26 hits (the same 13 markers counted twice). The appendix
numbers as C (C.1-C.7); its heading is now "## Appendix. ... {#app:approximant}".

Against P-APPC:
- opening reworded: the coefficients are defined by an exactly specified rule; the paper contains the complete
  definition of the approximant, not its coefficients;
- cases (1, D_A), (2, D*), (1, D*); layouts are "layout B" (the first xi-box from -1821/200, the first v-box from 1/2);
  the inner-nine-tenths condition relaxed at those two edges only;
- sec:appc-format replaced by "The rule" (sec:appc-rule, eight subsections, the right-hand side in full as 236
  definitions, eq:appc-rhs, transcribed mechanically and round-trip checked on 200 random inputs) and "The output and
  its digest" (canonical ASCII, SHA-256; eq:appc-sums kept as exact block checks);
- eq:appc-linecheck, lem:appc-checks and sec:appc-specimen dropped; sec:appc-spot "Digests and spot values" added;
- the certification sections unchanged except wording; outcome targets from G0h (divided by 10), outcomes pending;
- no trace of the final part of tables; one clause proposed for the introduction (01:198-200); 90 crosswalk rows.

The rule: B = 320 fixed point with floor; exact dot products rounded once; exp, log, sin, cos, pi, sinh, cosh, sqrt
stated as algorithms; matrices as floors of exact rationals on the rounded nodes; the seed by bisection then Newton;
the cone data in G-form with 40 Raychaudhuri sweeps; cells, Goursat boundary terms, jets, the cell map and its edges;
segments (Zeno: 16, 8, 4, 2, 1, 1 columns of 32; 32, 16, 8, 4, 2, 1, 1 of 64), each with its own M and a defined
hand-off state with its own digest; element values by Lagrange interpolation, Chebyshev transform, z = floor(10^p C + 1/2).

The iteration (decided from new pilot measurements, one core, nice 19): plain Picard stalls in the second row of cells
(5.7e-17 at sweep 10, 3.5e-21 at sweep 31); defect correction with fixed-point 64-bit inner sweeps is limited by its
absolute rounding; **defect correction with binary64 inner sweeps** reaches 1.3e-47 (row 0) and 5.6e-43 (row 1) after
5 outer steps at M = 160, 2.5-3.0 s per decade. So the rule uses binary64 inner sweeps, stated as mathematics (dyadic
rationals, round to nearest, ties to even, sums in a fixed order; no fused multiply-add, no reordering, no extended
precision); plain Picard kept as a remark. About 1 page more than plain Picard.

Underspecified points found and now stated: endpoint nodes; precedence of the division; 4(e3 . G) against
floor(4 e3 G); the form of S; which evaluation's Phi and rho give the top values; the tie rule for element nodes and
nodes outside the grid; the nesting of the interpolation dot products; the per-element angular degree; the summation
order in binary64; the hex case of the digest. The S-RULE pilot cannot be reproduced bit for bit from this text (it
took constants from the quad-double solver); first-cell spot values must come from an implementation of P-APPC2.

Pending markers: lem-tl5-cip-axis, lem-tl5-f3-residual, lem-tl5-l7-rates (carried); appc-evolution-identity (a remark
that in exact arithmetic the right-hand side is the evolution system; needs a written derivation, used by neither the
definition nor the certificate); computational-appc-parameters, -targets, three outcome markers, -spot; references
ref-fips-180-4 and ref-ieee-754.

Provisional parameters (to be confirmed once B3/q is measured and convergence at production M in every row):
(1, D_A) 32 x 30 cells, (26, 39), M = 184, (N_o, N_i) = (9, 25), p = 56; (2, D*) 64 x 30, (28, 42), M = 184, (10, 25),
p = 61; (1, D*) 64 x 30, (30, 45), M = 200 then 328 for the last 16 columns, (10, 25), p = 64.
Expected cost (deduced, +-50 %): about 160, 400 and 680 core-hours, about 1,240 in all (about two weeks of four free
cores). With sec:tl5-hfw merged the targets should loosen by 1.8-3.6 decades (about 7 % of cost per decade).
