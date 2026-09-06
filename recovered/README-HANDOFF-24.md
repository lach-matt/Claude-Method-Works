# LOWDIN-HANDOFF-24 — single superset archive (session 24, 2026-08-16). Supersedes HANDOFF-23 + PACK-24.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack24.
Verify:  bash verify24.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-23.md (which chains 22 -> 21 -> 20 -> 19 -> 18), then: cp pack24/*.py pack24/*.jsonl rt/
Gates (all before ANY new work; run in rt/): gates (1)-(18) of README-HANDOFF-23.md, plus
 (19) FENT=0.5 FOCC=0.5 SIC_NOCLAMP=1 python3 t7c_cuaudit_run.py 21   -> must SKIP (row present); if row deleted, reprints Sc E -0.3211 resid -0.0265
 (20) python3 janak_table.py | grep "^Sc"   -> "Sc 3d | -0.4841 -0.3211 -0.3330 | -0.3381 | -0.0170 | +0.0000 | -0.0265 -0.0435"
 (21) SIC_NOCLAMP=1 python3 exent.py 70 -> must SKIP; if row deleted reprints Yb Ex_ent -0.5066 rmean 0.818
Read first: pack24/BRIDGE-LOWDIN-SESSION-24.md (s3 needs rulings (b),(c)), then FINDING-OWNSHELL-JANAK (+TABLE-JANAK), FINDING-CU-AUDIT, ATTRIBUTION-NOTE.
Next: rulings on bridge-24 s3(1)-(4); write predictions BEFORE any run; T4 writing chat LAST (R 1701–1848 owed).
Known: bash egress denies network (web_search/web_fetch work). Known (F18.1): list rt/ for files not in any pack. Known (F24.1): record `it`; s23 rows unaudited.
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-25 superset.