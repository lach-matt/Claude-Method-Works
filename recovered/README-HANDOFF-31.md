# LOWDIN-HANDOFF-31 — single superset archive (session 31, 2026-08-17). Supersedes HANDOFF-30 + PACK-31.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack31.
Verify:  bash verify31.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-30.md (which chains 29 -> ... -> 18), then: cp pack31/*.py pack31/*.jsonl rt/   (pack31/t7c_corrz.py supersedes pack23's: corr='R' hook;
         corr='Z' byte-identical; rt/ MUST sit beside the packs: t5_scf reads ../pack9/)
Gates (all before ANY new work; run in rt/): gates (1)-(45) of README-HANDOFF-30.md (gate 16 also holds with corr='R'), plus
 (46) SIC_NOCLAMP=1 SUBCELL=1 FORM=R python3 t7c_corrRZ_run.py 21 39 55 -> must SKIP all; if Sc deleted reprints EF -0.3265 shift -0.0299 (4 s);
      SIC_NOCLAMP=1 SUBCELL=1 FORM=Z python3 t7c_corrRZ_run.py 21 -> SKIP; if deleted reprints EF -0.3211
 (47) python3 frachf_eps0.py 21              -> must SKIP; if deleted reprints corr eps -0.246301 gap_run 8.7e-05 (12 s)
 (48) SIC_NOCLAMP=1 SUBCELL=1 python3 rz_mech.py 21 39 -> must SKIP; if Y deleted reprints rs_wc 1.868 dR_loc -0.00513 (6 s)
Read first: pack31/BRIDGE-LOWDIN-SESSION-31.md, then FINDING-RZMECH + FAULT-F31.2, COMPARE-RZ, SPEC-SOSEX-SESSION-32 (the next build), SPEC-WALK-SESSION-32.
Known: bash egress denies network (web_search/web_fetch work). Known (F18.1/F30.1/F31.4): census rt/ against the packs TO A FILE (comm), never through `| head`.
Known: tool call ~300 s. Known: rz_mech's benchmark points are RECALLED (comparison only); nothing in the chain reads them.
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-32 superset.