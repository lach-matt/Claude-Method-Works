# rule/: the approximant's rule (P-APPC2), production implementation and exact reference

An independent implementation of the rule that defines the approximant of each seed, as specified by the Appendix C
text proofs/P-APPC2.md, as confirmed at ebdddecc (md5 47a32377…; the rule text is that of the reviewed fixed copy 446f53e8, review notes/reviews/R-P-APPC2.md): fixed point with B = 320 fractional bits (every product and
quotient floored, every dot product exact and floored once), the stated elementary functions, the seed by bisection
and Newton, the cone data with 40 Raychaudhuri sweeps, cells with Goursat boundary terms, and **defect correction**:
N_o outer steps, each a defect in 320-bit fixed point corrected by N_i sweeps of the linearised map in **binary64**
(the short arithmetic 𝔻 of def:appc-short), then segments with their own M, element values, Chebyshev coefficients,
canonical strings and SHA-256 digests. It was written from the text, not from the pilot (solver/rule-pilot/).

The right-hand side eq:appc-rhs is the solver's generated program solver/rhs_gen.h (sha256 2223ff5a…4eb4cc1):
`tests/rhs_vs_text.py` shows it identical to the printed 236 definitions, term by term and in order (order matters in
𝔻, where sums are formed from the left).

| file | what |
|---|---|
| `fixp.h` | 𝔽 (def:appc-arith) in 6 two's-complement 64-bit limbs: exact +, −, n·x; floored ⊙, ⊘, ⊘n, √; exact dot products. Every result is range-checked (integer part below 2⁶⁰); an overflow stops the program rather than wrap, so a finished run computed the unbounded model's values |
| `gmpmin.h` | the GMP interface (the real `<gmp.h>` when installed, else its stable ABI declared directly) |
| `exactfn.h` | def:appc-functions: exp, sin, cos, log, π̂, L̂₂, ĉ(j, n), sinh, cosh, ξ̂₀, â, λ̂ |
| `matrices.h` | def:appc-nodes: node families, Q, D, D², QQ, W, V, Ĉ, Lagrange values, resampling (def:appc-resample); floors of exact rationals by closed forms (GMP), not the reference's polynomial algebra |
| `cell.h` | def:appc-rule-seed, def:appc-grid, def:appc-cell (P(G) = B + I(G) in 𝔽) and I_𝔻 (def:appc-iteration (iv): value-and-tangent pairs through rhs_gen.h in binary64) |
| `scheme.h` | def:appc-iteration (the outer steps), separate from the cell map; plain Picard (rem:appc-picard) kept for comparisons only |
| `rule.cpp` | def:appc-rule-data (the cone), the march by segments, hand-offs (def:appc-handoff), checkpoints, def:appc-element-values, sec:appc-digest, sec:appc-spot |
| `sha256.h` | SHA-256 (FIPS 180-4), lowercase hex |
| `rule_ref.py` | the second implementation: Python integers for 𝔽 and Python floats (IEEE binary64) for 𝔻, as direct a transcription of the text as possible; small runs |
| `tests/` | `t_fixp.*` (𝔽 against Python's integers), `rhs_vs_text.py`, `segtests.sh`, `cmp_cells.py`, `pilotin.cpp` (the pilot cell's inputs and the solver's quad-double cell), `plan.py` (cost model), `bench.cpp` |
| `cfg/` | test configurations: tZ (zero cone data: exact zero defects), tB2rev (tB2's elements in reverse order), tA2 (four cells), tB2 (a complete tiny case in three segments, M = 4, 6, 8), tB3 (M = 6, 6, 8: a boundary between equal M, resampled by m-9), tR2/tR3 (resume), tK (a pilot-size cell: the real-size determinism and resume test) |

## Build

Needs g++ ≥ 11 with OpenMP, GMP (libgmp; the headers are optional), an x86-64 CPU with BMI2 (x86-64-v3). The flags
`-ffp-contract=off` and no `-ffast-math` are **part of the rule**: 𝔻 is binary64 with every operation rounded once, no
fused multiply-add, no reordering, and x86-64 doubles are SSE2 (no extended precision). Build outside the repository:

    make BUILD=/path/to/build          # rule, t_fixp; prints the sha256 of solver/rhs_gen.h

## Configuration

    seed 1                         # 1: λ̂ = 1;  2: λ̂ = √(1/10)
    xi_e -3421/500                 # ξ_e, v_e: the largest right ends of the layout's boxes (def:appc-grid)
    v_e 7171/2000
    ncol 32                        # n_c × n_r cells
    nrow 30
    pxi 26                         # (p_ξ, p_v)
    pv 39
    segment 0 16 184 9 25          # columns [c0, c1): M, N_o, N_i   (one line per segment, tiling the columns)
    segment 16 24 184 9 25
    ...
    p 56                           # the quantum 10^-p
    elem 1 1 -1821/200 -7891/1000 1/2 21231/10000 104 136    # i j ξ-box v-box N_t N_s (layout B; M_e is derived)
    threads 4  batch 4  ckpt_minutes 30  out /data/s1A         # execution only; none changes the output

`rule params CFG` prints the canonical parameters and their SHA-256 (the parameter digest, embedded in every file).

## Run, resume, assemble, verify

    rule run CFG [out=DIR] [threads=N] [batch=N] [ckpt_minutes=X]   # every segment in order
    rule run CFG S ...                                              # only segment S, from DIR/handoff_{S-1}.bin
    rule assemble CFG [out=DIR]        # coefficients, DIR/case.txt (the canonical string), DIR/digests.txt
    rule verify DIR/case.txt DIR/digests.txt

- **The march.** Columns outward, rows upward; the cells of each anti-diagonal of a segment are independent and are
  iterated together in batches of `batch` cells, OpenMP over the nodes of all of them. Results do not depend on the
  thread count or the batching (every 𝔽 sum is exact; every 𝔻 sum is formed in the stated order inside one thread).
- **Resume.** Rerun the same command. A finished cell is `DIR/seg_SS/cell_IIII_JJJJ.bin` (edges, top values, the
  element values it owns), written atomically; a batch in progress is checkpointed after an outer step at most every
  `ckpt_minutes` (`DIR/seg_SS/batch.ckpt`: G and the residual log). An outer step depends on G alone, so a resumed
  run is identical to an uninterrupted one.
- **Segments and hand-offs** (sec:appc-segments). A segment is the unit of work: it runs on its own from the previous
  segment's hand-off. When it ends it writes `DIR/handoff_SS.bin` (+ `.sha256`): the right edge of its last column
  (R, m, n, W at the last ξ-node, every row, v-node and x-node; def:appc-handoff), in a compact binary (one byte: sign
  and length; then the magnitude bytes), with the **digest of the canonical string** of def:appc-handoff in its header;
  reading it back recomputes that digest. It also writes `DIR/elem_SS.bin` (+ `.sha256`), the element values its cells
  own. The next segment resamples the hand-off to its M (def:appc-resample) at every boundary, also when the two M
  are equal (the review's m-9: in 𝔽 that resampling is not the identity).
- **Assembly** checks every file's checksum and every hand-off digest, forms Γ, resamples to M_e, transforms in x, then
  σ, then t, z = ⌊10^p C + ½⌋, and writes the canonical string and `digests.txt`: the case digest, the hand-off
  digests, per block its digest, nonzero count, S₁, S₂, S₀, z₀₀₀, z₁₀₀, z₀₁₀, z₀₀₁, and the spot values of sec:appc-spot.

## Tests

    BUILD/t_fixp | python3 tests/t_fixp.py
    python3 tests/rhs_vs_text.py ../proofs/P-APPC2.md ../solver/rhs_gen.h
    BUILD/rule cells cfg/tA2.cfg out=X;  python3 rule_ref.py cfg/tA2.cfg Y;  diff X/cells.dump Y.dump
    BUILD/rule run cfg/tB2.cfg out=X && BUILD/rule assemble cfg/tB2.cfg out=X
    python3 rule_ref.py cfg/tB2.cfg Y && cmp X/case.txt Y.txt && diff X/digests.txt Y.digests
    tests/segtests.sh BUILD cfg         # segments one at a time; 2 threads and another batching; kill and resume
    tests/fixtests.sh BUILD cfg rule_ref.py ../solver/rhs_gen.h   # the review fixes: batch=0 refused; an exact zero
                                        # defect (cfg/tZ.cfg) keeps N_o entries of max|r|; stop and resume; element order
    # real size (about 50 s of cpu): cell (0,0) of cfg/tK.cfg has the same sha256 with threads=1, with threads=2, and
    # when the run is killed after an outer step (ckpt_minutes=0) and resumed with threads=2:
    BUILD/rule cells cfg/tK.cfg out=K1; BUILD/rule cells cfg/tK.cfg out=K2 threads=2; grep '^cell' K1/cells.dump K2/cells.dump

(`rule_ref.py` reads solver/rhs_gen.h relative to itself, or from `RULE_RHS`.) Two hooks exist for tests only and are
not part of the rule: the configuration key `zero_data 1` (zero cone data, so every defect is exactly 0; it enters the
parameter digest), and the environment variable `RULE_STOP_AFTER_OUTER=k`, which saves the batch's checkpoint after
outer step k and exits (code 9), a deterministic stand-in for a crash.

## The iteration scheme

`scheme.h` holds def:appc-iteration; `cell.h` the operators. A scheme receives a batch of cells (B, G, counts) and calls
`Batch::evaluate` (Ψ, Φ, J̄ from G in 𝔽), `Batch::integrate` (P(G) = B + I), and `Batch::lin` (I_𝔻 of the cell's d in
𝔻); it leaves the final G and the Φ of the last evaluation of P. Plain Picard (`scheme_picard`) is the remark's
alternative.

## Where the text leaves a choice

The draft's open points (the reciprocals in 𝔻, the 0-tie, the orders of the canonical strings, twenty-five jets,
resampling between equal M, the Lagrange bases of the element values) are settled in the fixed copy, and this code
follows the fixed copy. What remains is listed in the report (I-RULE): h_ξ ⊙ h_v and h_v ⊙ h_v in I_𝔻 (taken:
(rd h_ξ) ⊗ (rd h_v), the rd of each listed number, not the rd of the product); the per-cell spot values of
sec:appc-spot give no order of printing (here: the order of the list).
