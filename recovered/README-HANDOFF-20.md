# LOWDIN-HANDOFF-20 — single superset archive (session 20, 2026-08-16). Supersedes HANDOFF-19 + PACK-20.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack20.
Verify:  bash verify20.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-19.md (which chains README-18), then: cp pack20/*.py pack20/*.jsonl rt/   (sympy required for t7c_mult / t7c_mult_audit)
Gates (all before ANY new work; run in rt/): gates (1)-(7) of README-HANDOFF-19.md, plus
 (8) python3 t7c_srdec.py 57 all               -> E -0.2079 == banked t7c_pol, shift_vs_nr 0.0266   [appends a row to t7c_srdec.jsonl -- delete after]
 (9) python3 t7c_mult_audit.py                 -> f2 groups (11,7,3), f4 groups (13,8,9,5), A3 3H -0.03029 3F 0 3P 0.11106
Read first: pack20/BRIDGE-LOWDIN-SESSION-20.md (s3 candidates need rulings), then FINDING-T7C-SHELL, FINDING-T7C-COMPARE, RECLASS-R1449-S19-PM1.
Next: rulings on bridge-20 s3(1)-(4); write predictions BEFORE any run; T4 writing chat LAST (R 1701–1817 owed).
Known: bash egress denies network entirely in s20 (no web); use web_fetch for NIST if needed. Known (F18.1): list rt/ for files not in any pack.
Handoff: M's ruling s20 — trigger at 90 %, archive READY before 100 %; next archive = LOWDIN-HANDOFF-21 superset.