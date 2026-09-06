# FINDING-LWALK (s35) — the l-walk with n, on the frontier pair (d vs s) of five rows, three ways: (i) frozen HFS field, (ii) frozen HF field (Koopmans),
(iii) relaxed E path. Run: lwalk.py (25 channels + 4 swaps, ~1-3 s each), lwalk_hf.py (SR HF, no corr; frontier s partner DSCF, 5 rows). TABLE-LWALK-SESSION-35.txt.
FRONTIER PAIR d(ground entrant) vs s(swap removal), D_rel(iii) / D_rel_HF(ii) / D_frz(i):
  Sc 3d -0.342 vs 4s -0.269 (d deeper 0.073) | HF 3d -0.267 vs 4s -0.203 (0.064) | frz 3d -0.447 vs 4s -0.295 (0.152)
  Y  4d -0.256 vs 5s -0.256 (0.0004)         | HF 4d -0.196 vs 5s -0.193 (0.003) | frz 4d -0.320 vs 5s -0.284 (0.037)
  La 5d -0.274 vs 6s -0.226 (0.048)          | HF 5d -0.206 vs 6s -0.172 (0.034) | frz 5d -0.336 vs 6s -0.245 (0.091)
  Lu 5d -0.246 vs 6s -0.262 (s deeper 0.016) | HF 5d -0.160 vs 6s -0.211 (s 0.051) | frz 5d -0.310 vs 6s -0.292 (d DEEPER 0.018)  <- FLIP
PL1 near-degeneracy (<0.05 on iii): HELD Y (0.0004) · La (0.048) · Lu (0.016); FAILED Sc (0.073). Non-frontier steps at fixed n: 0.10-0.30 on every row (held).
PL2 field-invariant ordering: HELD Sc/Y/La; FAILED Lu -> PL4 FIRES and NAMES Lu 5d/6s: on the frozen HFS field 5d is deeper than 6s, on the frozen HF
field and on the relaxed E path 6s is deeper (5d removed first, as the record has it). The 5d relaxes 0.064 against 0.030 for 6s: THE n+l TIE AT Lu IS
NOT A PROPERTY OF THE LOCAL FROZEN FIELD; the relaxation step decides it. (On the HF frozen field the order is already right: exact exchange holds the tie
where local exchange does not — R 1578-type distinction between the two frozen references, and the same home as the s34 exchange seam.)
PL3 bracketing (iii between i and ii): HELD on 9 of 10 frontier channels (both members of Sc/Y/La/Lu); FAILED on Cs 6s (relaxed -0.150 deeper than both
frozen points, -0.142/-0.128: Cs relaxes NEGATIVE, as FINDING-B2 found) — the bracket is a d-row property, not general.
ALSO (not predicted, recorded): La 4f channel is the DEEPEST channel on both local objects (frz eps -0.288, D_rel -0.375 vs 5d -0.274) — the local 4f
collapse of FINDING-MP2ENT seen as a filling-order fault: the E path would fill La at 4f. HF 4f channel NOT run (owed). Cs: every channel relaxes negative
(-0.007..-0.011, class-flat), unlike every d row (positive) — a diffuse-row property, stated.
Steps at fixed n (iii): Sc 3d->4d 0.27, 4s->4p(4p chan) --; Y 4d->5d 0.19; La 5d->6d 0.21; Lu 5d->6d 0.18; Cs 6s->6p 0.047, 6p->5d(4f) --. Steps at fixed l:
Sc 4s->5s 0.17; Y 5s->6s 0.16; La 6s->7s 0.14; Lu 6s->7s 0.17; Cs 6s->7s 0.077. Frontier: Delta_n(s) ~ 0.14-0.17 on d rows, and the d/s tie sits 0.0004-0.073
from zero — the n+l statement is that the s->s' step and the d->d' step straddle the tie; measured, not fitted.
Reading (bound): the l-walk gives the Madelung tie as a measured near-degeneracy on the relaxed point (Y at 0.4 mHa), the same ordering on both fields
except at Lu where the local frozen field misorders and relaxation restores, and a bracket that holds on d rows only. Nothing entered; no constant; no
measured input; channels enumerated. Owed: HF (ii) on the empty channels (4f at La; 4p/5p/6p) — 25 s each; Cs frontier partner (5d) is a chan, not a swap.
Owed to T4: R 1938 lwalk built · R 1939 PL1 Y/La/Lu held, Sc failed · R 1940 PL4 fires at Lu 5d/6s: tie is not a local-frozen-field property · R 1941 bracket
holds on d rows, fails on Cs · R 1942 La 4f collapse as filling-order fault · R 1943 steps at fixed n / fixed l tabulated.
Files (pack35): PREDICTION-LWALK · lwalk.py/.jsonl · lwalk_hf.py/.jsonl · TABLE-LWALK-SESSION-35.txt · this finding.