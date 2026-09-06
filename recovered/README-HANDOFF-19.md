# LOWDIN-HANDOFF-19 — single superset archive (session 19, 2026-08-16). Supersedes HANDOFF-18 + PACK-19.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack19.
Verify:  bash verify19.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-18.md, then: cp pack19/*.py pack19/*.jsonl rt/   (t7c_mult.py needs sympy for Gaunt coefficients)
Gates (all before ANY new work; run in rt/): gates (1)-(5) of README-HANDOFF-18.md, plus
 (6) python3 t7c_scpol.py bare CeIV        -> d -0.42268 (== t7c_scres SR; PP0)   [appends a row to t7c_scpol.jsonl -- delete it after, or diff]
 (7) python3 t7c_so.py 5d 57                -> E_ts -0.2079 == banked t7c_pol; zeta_5d 0.00308
Read first: pack19/BRIDGE-LOWDIN-SESSION-19.md (s3 candidates need rulings), then the three FINDING-T7C-*-SESSION-19.md.
Next: rulings on bridge-19 s3(1)-(3); write predictions BEFORE any run; T4 writing chat LAST (R 1701–1808 owed).
Known: bash egress denies physics.nist.gov (use web_fetch). Known (F18.1): list rt/ for files not in any pack before writing; quarantine, audit, then adopt or discard by ruling.
Handoff: §H.10 — state at 90 % and hand off; next archive = LOWDIN-HANDOFF-20 superset.