# LOWDIN-HANDOFF-21 — single superset archive (session 21, 2026-08-16). Supersedes HANDOFF-20 + PACK-21.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack21.
Verify:  bash verify21.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-20.md (which chains README-19 -> README-18), then: cp pack21/*.py pack21/*.jsonl rt/   (scipy required for t7c_occ analysis)
Gates (all before ANY new work; run in rt/): gates (1)-(9) of README-HANDOFF-20.md, plus
 (10) python3 -c "from t7c_sic import scf_sic_sr; from t5_scf import ground_occ,minus; Es,h,s=scf_sic_sr(57,1,occ=minus(ground_occ(57),5,2,1.0),entrant=(5,2),mode='all'); print(round(Es[(5,2,s,'ent')],4))"  -> -0.2202
 (11) python3 -c "from t7c_corr import scf_sic_corr; from t5_scf import ground_occ,minus; Es,h,s=scf_sic_corr(57,1,occ=minus(ground_occ(57),5,2,1.0),entrant=(5,2),mode='all',corr='P'); print(round(Es[(5,2,s,'ent')],4))"  -> -0.2284
 (12) python3 t7a_sic_all.py 26  -> must SKIP (Z done); if you delete the row first it must reprint ts_pol -0.378 ts_sic -0.3854
Read first: pack21/BRIDGE-LOWDIN-SESSION-21.md (s3 candidates need rulings), then FINDING-T7C-CORR, FINDING-T7A-SICDEC, FINDING-T7C-OCC (F21.1).
Next: rulings on bridge-21 s3(1)-(5); write predictions BEFORE any run; T4 writing chat LAST (R 1701–1825 owed).
Known: bash egress denies network entirely (no pip, no NIST); web_search tool works for literature. Known (F18.1): list rt/ for files not in any pack.
Known (s21): scf_occ Etot is tail-conditioned -- do NOT read banked dscf as a functional property (F21.1). Ruling (D) in force: nothing fitted stands.
Handoff: M's ruling -- trigger 90 %, archive READY before 100 %; next archive = LOWDIN-HANDOFF-22 superset.