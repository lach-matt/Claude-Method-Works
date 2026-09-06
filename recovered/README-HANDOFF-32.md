# LOWDIN-HANDOFF-32 — single superset archive (session 32, 2026-08-17). Supersedes HANDOFF-31 + PACK-32.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack32.
Verify:  bash verify32.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-31.md (which chains 30 -> ... -> 18), then: cp pack32/*.py pack32/*.json pack32/*.jsonl rt/
         (pack32/t7c_corrz.py supersedes pack31's: corr='S' hook, corr='Z'/'R' byte-identical; pack32/t7c_corrRZ_run.py adds FORM=S; rt/ MUST sit beside the packs)
Gates (all before ANY new work; run in rt/): gates (1)-(48) of README-HANDOFF-31.md (gate 16 also holds with corr='S'; gate 7 APPENDS a La row to t7c_so.jsonl -- delete it after, or diff), plus
 (49) python3 sumrule_gates.py 2 1; python3 sumrule_gates.py 2 0.5 -> both "G-S4/G-S5: PASS" (f-sum 0.442291 at rs 2 lam 1; compressibility zeta0 1.326873)
 (50) python3 sox_table.py gates             -> G-S1 zeta 0/1 bare 0.0241943 PASS; G-S2 rs 1e-3 zeta 0 0.0241676; PS-1 rs 2 zeta 0 ratio 0.6747, zeta 1 0.8019
 (51) python3 sox_qres.py 1.44881             -> must SKIP; if that row is deleted (NZ=80 NU=80 NPP=64 NPV=128) reprints g2b_Ry 0.0293843 (~6 s)
 (52) SIC_NOCLAMP=1 SUBCELL=1 FORM=S python3 t7c_corrRZ_run.py 21 39 55 -> must SKIP all; if Sc deleted reprints EF -0.327 shift -0.0304 (9 s); Y EF -0.2373
 (53) python3 sox_mc.py 8000000 32            -> bare MC 0.024071 +- 0.000126, z-scores <= 1 (60 s)
Read first: pack32/BRIDGE-LOWDIN-SESSION-32.md, then FINDING-SOSEX (the SIC-cancellation law), FINDING-SUMRULES, FAULT-F32.1, SPEC-SOSEX-32 §A1-§A2, SPEC-WALK-32 (pack31).
Known: bash egress denies network (web_search/web_fetch work). Known (F18.1/F30.1/F31.4/F32.1): census rt/ AND the working pack against the packs BYTE-LEVEL
(cmp every file against every pack copy) TO A FILE, before writing, before adopting, and again before sealing; a name census misses in-place edits; re-census
whenever a write is refused as pre-existing. Known: tool call ~300 s. Known: rz_mech's/sox_bench_compare's benchmark points are RECALLED (comparison only).
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-33 superset.