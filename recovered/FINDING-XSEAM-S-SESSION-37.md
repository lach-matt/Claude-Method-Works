# FINDING-XSEAM-S (s37, item b) — frozen removal exchange LSD+PZ-SIC minus HF (xseam form) on the s MEMBER of the d/s pair, 13 rows, and the singly-occupied
d member on Ce Ac Pa U Cm (Sc Y La Gd Lu d from xseam.jsonl, same code path). xseam_s.py/.jsonl; TABLE-XSEAM-S. Hf Th Rf d members (k=2) NOT run (intra-shell
average-of-configuration term not built; stated). Nothing entered; no constant. Fault of build: name shadowing (module G by a float) caught by traceback on row 3,
repaired (GG); the two rows computed before it are correct (G.expand is called before the shadowing point) — F37.1, minor, closed, no number changed.
RESULT: Delta_x(s) = -0.019 (Sc), -0.020..-0.030 on n>=4 (mean -0.0236, sd 0.0028): the s member carries a class-flat exchange seam of the entrant's sign,
its HF part dominated by the (n-1)p and (n-1)s core exchange (0.012-0.015 / 0.007-0.009) with the d partner third. d-minus-s: Sc -0.036 (largest), n>=4 -0.002..-0.013
(mean -0.006, sd 0.003) — NEGATIVE, while the relaxed pair offset SR-local minus HF+corr is POSITIVE (+0.013..+0.029). PXS-1 sign HELD, Sc size FAILED (0.019 not
0.05: at Sc the s and d members do NOT carry the seam equally — d carries 3x); PXS-2 FAILED (opposite sign, no tracking); PXS-3 HELD (class-flat, sd 0.003).
Reading (bound): the frozen exchange difference between the pair members has the WRONG sign to be the relaxed pair offset; therefore the pair offset is the
RELAXATION difference between the fields (FINDING-B2's object: local relaxes the d entrant 0.06-0.10 vs HF), of size ~ +0.020 - (-0.006) = +0.026 on n>=4 and
+0.036 at Sc, consistent with B2's finding that 3d relaxes most. Neither the frozen seam nor its pair difference is row-differential (sd 0.003): (b) closes the
decomposition as a bound and removes frozen exchange from the candidate list for the Th/Ac residual.
Owed to T4: R 1963 xseam_s built (s member, spin-averaged removal) · R 1964 Delta_x(s) class-flat -0.020..-0.030 · R 1965 pair frozen exchange has the wrong sign
for the pair offset -> the offset is relaxation · R 1966 F37.1 shadowing, closed.
Files (pack37): PREDICTION-XSEAM-S · xseam_s.py/.jsonl · TABLE-XSEAM-S · this finding.