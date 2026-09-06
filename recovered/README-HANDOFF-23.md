# LOWDIN-HANDOFF-23 — single superset archive (session 23, 2026-08-16). Supersedes HANDOFF-22 + PACK-23.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack23.
Verify:  bash verify23.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-22.md (which chains 21 -> 20 -> 19 -> 18), then: cp pack23/*.py pack23/*.json pack23/*.jsonl rt/   (numpy>=2: trapezoid)
Gates (all before ANY new work; run in rt/): gates (1)-(15) of README-HANDOFF-22.md, plus
 (16) SIC_NOCLAMP=1 python3 -c "from t7c_corrz import scf_sic_corr; Es,h,s=scf_sic_corr(1,1,occ=[],entrant=(1,0),mode='all',corr='Z'); print(round(Es[(1,0,s,'ent')],4))" -> -0.5 (also with LAM1=1)
 (17) python3 ring_zeta.py 0 0.005   -> "= -0.07115 Ha";  python3 lam1_zeta.py -> lam1(0) 0.0092292 lam1(1) 0.0047924
 (18) SIC_NOCLAMP=1 python3 t7c_regen.py 57 -> must SKIP (Z done); if row deleted, reprints noclamp base -0.2161
Read first: pack23/BRIDGE-LOWDIN-SESSION-23.md (s3 candidates need rulings), then FINDING-T7C-CORRZ (+TABLE-CHAIN-15-Z/Z1), FINDING-FK-DENSITY.
Next: rulings on bridge-23 s3(1)-(4); write predictions BEFORE any run; T4 writing chat LAST (R 1701–1842 owed).
Known: bash egress denies network (web_search/web_fetch work). Known (F18.1): list rt/ for files not in any pack. Known: OUT-file switch in t7c_corrz_run.py via LAM1.
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-24 superset.