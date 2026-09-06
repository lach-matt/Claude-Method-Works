# LOWDIN-HANDOFF-22 — single superset archive (session 22, 2026-08-16). Supersedes HANDOFF-21 + PACK-22.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack22.
Verify:  bash verify22.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-21.md (which chains README-20 -> 19 -> 18), then: cp pack22/*.py pack22/*.jsonl rt/
Gates (all before ANY new work; run in rt/): gates (1)-(12) of README-HANDOFF-21.md, plus
 (13) python3 t7c_hfsr.py                        -> "G1 He 1s c=1e6 -0.91796", "G2 Z=21 hfs sr eps(1/2) -0.2686", "G2 Z=57 ... -0.2017"
 (14) SIC_NOCLAMP=1 python3 -c "from t7c_corr2 import scf_sic_corr; Es,h,s=scf_sic_corr(1,1,occ=[],entrant=(1,0),mode='all',corr='P'); print(round(Es[(1,0,s,'ent')],4))"  -> -0.5
 (15) python3 t7c_dyaudit.py 70  -> appends a Yb row with F2 ts/neu/ion 0.5739/0.555/0.5915 (delete the appended row after, or diff against pack22)
Read first: pack22/BRIDGE-LOWDIN-SESSION-22.md (s3 candidates need rulings), then FINDING-T7C-CORR-ALL (+TABLE-CHAIN-15), FINDING-T7C-CORR2 (F22.1), READ-GB-ZETA.
Next: rulings on bridge-22 s3(1)-(5); write predictions BEFORE any run; T4 writing chat LAST (R 1701–1836 owed).
Known: bash egress denies network entirely (web_search/web_fetch work; Hoffman PRB 45 8730 paywalled). Known (F18.1): list rt/ for files not in any pack.
Known (F22.1): banked SIC/GB rows carry the Latter clamp on SIC channels; t7c_corr2 SIC_NOCLAMP=1 is the repaired object; regeneration owed.
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-23 superset.