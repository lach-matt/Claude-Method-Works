# LOWDIN-HANDOFF-25 — single superset archive (session 25, 2026-08-16). Supersedes HANDOFF-24 + PACK-25.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack25.
Verify:  bash verify25.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-24.md (which chains 23 -> 22 -> 21 -> 20 -> 19 -> 18), then: cp pack25/*.py pack25/*.jsonl rt/
Gates (all before ANY new work; run in rt/): gates (1)-(21) of README-HANDOFF-24.md, plus
 (22) SIC_NOCLAMP=1 python3 frozen_scan.py 21   -> must SKIP; if rows deleted reprints Sc f=1.0 E_fr -0.26947, f=0.5 -0.32114 (it_ref 37)
 (23) python3 t7c_3dhund.py 28                 -> Ni zeta_3d 0.00362, stab_n = stab_i = -0.0259, col +0.0  [appends a row -- delete after, or diff]
Read first: pack25/BRIDGE-LOWDIN-SESSION-25.md (s3 needs rulings), then FINDING-FROZEN-SCAN (+TABLE), FINDING-3D-SOHUND (+TABLE), FINDING-KOOPMANS-LINK.
Next: rulings on bridge-25 s3(1)-(4); write predictions BEFORE any run; T4 writing chat LAST (R 1701–1856 owed).
Known: bash egress denies network (web_search/web_fetch work). Known (F18.1): list rt/ for files not in any pack. Known (F24.1/F25.1): Ti, Cu standing rows at maxit=100, E stable.
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-26 superset.