# LOWDIN-HANDOFF-30 — single superset archive (session 30, 2026-08-17). Supersedes HANDOFF-29 + PACK-30.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack30.
Verify:  bash verify30.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-29.md (which chains 28 -> ... -> 18), then: cp pack30/*.py pack30/*.json pack30/*.jsonl rt/   (rt/ MUST sit beside the packs: t5_scf reads ../pack9/)
Gates (all before ANY new work; run in rt/): gates (1)-(40) of README-HANDOFF-29.md (log of the s30 open run: pack30/GATES-1-40-SESSION-30-OPEN.log), plus
 (41) python3 drow_p.py 21 39 57 71 55 64      -> must SKIP all six; if Sc deleted reprints A -0.03077 B 0.011046 R -0.006287 (~60 s/row, <=2 rows per call)
 (42) python3 drow_n.py 55 21 39 57 71         -> must SKIP all (epse=ion); EPSE=neu python3 drow_n.py 21 39 -> SKIP; if Cs deleted reprints E2_closed -0.02082 adiab_closed_full -0.02886 (17 s)
 (43) python3 nodesplit.py 39 57 71 21         -> must SKIP all; if Y deleted reprints B_in 0.000315 Q_in 0.0189
 (44) python3 ring_table.py                    -> SKIP z 0.0 .. 1.0 (11); python3 corr_ring.py -> "rs 0.001 z 0.0: R -0.26164  Z -0.26161"
 (45) python3 frachf_ring.py 39 21 57 71 55    -> must SKIP all; if Y deleted reprints DEc_R -0.027778 delivered_R 0.845 (27 s)
Read first: pack30/BRIDGE-LOWDIN-SESSION-30.md, then COMPARE-DROW (decision + addendum), FINDING-RING, FINDING-DROW-P, FINDING-DROW-N, FINDING-NODESPLIT, FAULT-F30.1.
Known: bash egress denies network (web_search tool works). Known (F18.1, recurred as F30.1): an abandoned branch of the SAME chat can write into rt/ minutes after
a clean check — list rt/ for files not in any pack before writing AND before adopting anything; pack30/foreign/ is the s30 record. Known: tool call ~300 s.
Known: the box basis (drow_n) needs r >= 3e-4 and the regular inner condition; a FD expectation of an interpolated orbital is roundoff-dominated (F30.3/3b).
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-31 superset.