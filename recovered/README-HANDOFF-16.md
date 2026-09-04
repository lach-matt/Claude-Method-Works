# LOWDIN-HANDOFF-16 — single superset archive (session 16, 2026-08-16). Supersedes HANDOFF-14 + PACK-15 + PACK-16.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack16.
Verify:  bash verify16.sh                      (expect ok=N bad=0)
Runtime: mkdir rt; cp -r pack5/. rt/; cp pack7/pack5/*.py rt/; cp -r pack8/pack5fix/. rt/; cp pack9/*.py pack9/*.jsonl rt/;
         cp pack10/* rt/; cp pack12/*.py pack13/*.py rt/; cp pack16/*.py pack16/*.jsonl rt/; cd rt;
         gcc -O2 -shared -fPIC -o libshoot.so shoot.c
Gates (all three before ANY new work; run in rt/):
 (1) python3 derive_P_fix.py; python3 derive_P2_fix10.py; python3 derive_P3_fix10.py; cmp derive_P3.json ../pack8/pack5fix/derive_P3_fix.json
 (2) python3 probe13.py 20 0.111 10.0 4s 3d          -> "20 lam 0.111 mu -0.893 4s=-0.4611 3d=-0.4109 d=0.0502"
 (3) python3 t5_scf.py                                -> "21 3d probe -0.4866  banked -0.4866" and "57 5d probe -0.3581  banked -0.3581"
     (t5_scf.py's gate path expects pack9/T0b_pairs.json at ../pack9 relative to rt — edit the absolute path in its __main__ if the
      archive is extracted elsewhere; the path is the only environment-specific line.)
Read first: pack16/BRIDGE-LOWDIN-SESSION-16.md, then pack16/PREDICTION-T7-SESSION-16.md and pack16/T7-BUILD-SPEC.md.
Next: T7 (three 4f candidates, comparison decides) per the spec; T4 writing chat LAST (R 1701–1786 owed).
Known: bash egress denies physics.nist.gov (use web_fetch: element_name_a.htm, then <el>table1_a.htm / <el>table6_a.htm).
Handoff: §H.10 — state at 90% and hand off; bridge as few files as possible; next archive = LOWDIN-HANDOFF-17 superset.