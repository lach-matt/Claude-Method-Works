# I-RULE: an independent implementation of the rule (P-APPC2, confirmed at ebdddecc)

Implementer's report as handed back (the harness refused the file from the subagent; saved here by the coordinator).
Nothing committed by the implementer; code in rule/, scratch outputs in the session scratchpad (irule/).

## Summary
- A production C++ implementation of the rule (rule/) and an exact Python reference (rule_ref.py), first built from
  S-RULE §3 (plain Picard), then re-implemented from P-APPC2 (draft, then the reviewed copy 446f53e8; the confirmed
  copy has the same rule text).
- Bit for bit at every stage: arithmetic, constants, cells, binary64 inner sweeps, segments, resampling, element values,
  transforms, canonical strings, digests and spot values.
- Thread count, batching, segmenting and resume do not change the output (a thread-safety bug, a binary64 constant table
  built lazily inside a parallel region, was found by these tests and fixed).
- Defect correction reaches the 320-bit floor in 8-9 outer steps in rows 0 and 1, no stall; the production first cell
  of (1, D_A) takes 360 s on one core.
- At the G0k targets the three cases need about 520 core-hours, about 8 days on three free cores.

## Bit-for-bit results
- 3,000 random cases of every fixed-point operation against Python integers.
- solver/rhs_gen.h equals the printed 236 definitions of eq:appc-rhs, definition by definition (tests/rhs_vs_text.py).
- pi, L2, xi0, a, lambda, R_s(xi0, 1/2), exp 1, log 3, sin 1: C++ = Python = the printed values = the reviewer's script.
- C++ against Python: tA2 (four cells, every G, the top values, max |r| per outer step); tB2 (a complete case in segments,
  M = 4, 6, 8: the 175 kB canonical string, case digest, 3 hand-off digests, 20 block digests and sums, spot values);
  tB3 (an equal-M boundary); the first cell at pilot size (16, 24, 80), (N_o, N_i) = (2, 2): all 172,125 integers.
- One thread against two, batch sizes 1-3, kill and resume: identical outputs (cell (0, 0) of cfg/tK.cfg: 45e54c87...).
- Against the S-RULE pilot (pilot inputs): state hashes reproduced after 1, 4 and 200 sweeps (23c50a0fe9f55e0b); the
  pilot's reciprocals are not exact floors (40 of 50 wrong by up to 2.2e11 units of 2^-320).
- Against the solver's quad-double cell: agreement to the level at which the two sets of cone data agree (1.3e-49
  absolute in R, from the solver's tolerance-stopped n1_row; m, n on the cone to 3e-64 relative).

## Places where the text leaves a choice
- S-RULE §3: 22 open points, all fixed by P-APPC2 (several the other way from the implementer's first reading).
- P-APPC2 draft: the "twenty-four" jets, the Lagrange bases, the binary64 reciprocals, "the latter" (settled as m-3,
  m-10, M-1, n-7); equal-M resampling settled by m-9.
- Confirmed copy: nothing more that changes integers. Two remarks: h_xi . h_v in I_D is (rd h_xi) x (rd h_v) (implied;
  one sentence would make it explicit); the value half of each binary64 pair is recomputed from the rounded jets (clear,
  costs about half of each inner sweep).

## Measured costs (CPU, one core, load 7-9)
| | per node per outer evaluation (320-bit) | per node per inner sweep (binary64) | whole cell (9, 25), per node |
|---|---|---|---|
| M = 80, (16, 24) | 104 us | 1.35 us | 1.32 ms |
| M = 160, (16, 24) | 129 us | 1.57 us | 1.76 ms |
| M = 184, (26, 39) | 151 us | 1.90 us | 1.78 ms |

Gain per outer step falls with M (12.5, 10, 9.4 decades at M = 80, 160, 184).

Provisional P-APPC2 parameters: (1, D_A) 96, (2, D_A) 85, (2, D*) 251, (1, D*) 411 core-hours (about 840 for all four).

## Zeno-segmented plan for this machine (G0k targets, three free cores)
Proposed parameters (to be confirmed): (1, D_A) p = 53, (24, 36), M = 176, (8, 25); (2, D*) p = 58, (26, 39), M = 176,
(8, 25); (1, D*) p = 61, (28, 42), M = 184 then 312 from column 48, (9, 25).
Segments 16, 8, 4, 2, 1, 1 of 32 columns; 32, 16, 8, 4, 2, 1, 1 of 64. Core-hours (wall hours):
- (1, D_A): 33.8 (12.5), 16.9 (6.3), 8.4 (3.1), 4.2 (1.6), 2.1 (0.8), 2.1 (0.8); 68, about 1 day.
- (2, D*): 80.5 (29.8), 40.3 (14.9), 20.1 (7.5), 10.1 (3.7), 5.0 (1.9), 2.5 (0.9), 2.5 (0.9); 161, about 2.5 days.
- (1, D*): 113 (42), 57 (21), 59 (22), 30 (11), 15 (5.5), 7.4 (2.8), 7.4 (2.8); 289, about 4.5 days.
Effort halves with each segment on the uniform grid (equal effort would need graded cells, a change to the rule).
Hand-offs (compact binary): about 32 MB per segment (1, D_A), 34 MB (2, D*), 39 MB at M = 184 and 65 MB at M = 312
(1, D*); all under 100 MB. Element values are 2.1, 4.1 and 7.5 GB per case (local disk only).
Per segment: question (converged and resolved at its (M, N_o, N_i)?); criteria (every cell's last max |r| two decades
below the target or at the floor; the hand-off's top-eight Chebyshev coefficients in x below a tenth of the accuracy;
the hand-off reads back with its checksum and canonical digest; agreement with the quad-double reference to ~1e-40 where
it covers); stop (the segment's cells done; a failing criterion stops and reports, since the remedy is a specification
decision). Checked first: (1, D_A) segment 0 against the reference's column 15 (a read-only copy of s1A_r/s1A.ckpt when
the reference passes column 15). Run order: (1, D_A), (2, D*), (1, D*).
