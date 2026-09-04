# LOWDIN-HANDOFF-18 — single superset archive (session 18, 2026-08-16). Supersedes HANDOFF-17 + PACK-18.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack18.
Verify:  bash verify18.sh                      (expect ok=N bad=0)
Runtime: mkdir rt; cp -r pack5/. rt/; cp pack7/pack5/*.py rt/; cp -r pack8/pack5fix/. rt/; cp pack9/*.py pack9/*.jsonl rt/;
         cp pack10/* rt/; cp pack12/*.py pack13/*.py rt/; cp pack16/*.py pack16/*.jsonl rt/; cp pack17/*.py pack17/*.jsonl pack17/*.c rt/;
         cp pack18/*.py pack18/*.jsonl pack18/*.c rt/;
         cd rt; gcc -O2 -shared -fPIC -o libshoot.so shoot.c; gcc -O2 -shared -fPIC -o libshoot_sr.so shoot_sr.c; gcc -O2 -shared -fPIC -o libshoot_x.so shoot_x.c
Gates (all before ANY new work; run in rt/):
 (1) python3 derive_P_fix.py; python3 derive_P2_fix10.py; python3 derive_P3_fix10.py; cmp derive_P3.json ../pack8/pack5fix/derive_P3_fix.json
 (2) python3 probe13.py 20 0.111 10.0 4s 3d          -> "20 lam 0.111 mu -0.893 4s=-0.4611 3d=-0.4109 d=0.0502"
 (3) python3 t5_scf.py                                -> "21 3d probe -0.4866  banked -0.4866" and "57 5d probe -0.3581  banked -0.3581"
 (4) python3 t7c_kernel.py                            -> "H 1s ... sr(c=137.036) -0.5000064 ..." ; python3 t7c_pol.py gate 26 -> "-0.378 banked ts_pol -0.378"
 (5) python3 t7b_hf.py                                -> "GATE A  Z=2 1s eps -0.91796 ..." and "GATE A  Z=10 2p eps -0.85041 ..."
     python3 t7b_gate.py B                            -> "Z=21 3d hfs-switch eps -0.2752  T5 hfs_ts -0.2752" and Fe -0.4925/-0.4925
Read first: pack18/BRIDGE-LOWDIN-SESSION-18.md (s3 candidates need rulings), then FINDING-T7B-SESSION-18.md, FINDING-T7C-RESIDUE-SESSION-18.md.
Next: rulings on bridge-18 s3(1)-(3); write predictions BEFORE any run; T4 writing chat LAST (R 1701–1799 owed).
Known: bash egress denies physics.nist.gov (use web_fetch: element_name_a.htm, then <el>table1_a.htm / <el>table6_a.htm).
Known (F18.1): the working container can hold artefacts from an abandoned branch of the same chat — list rt/ for files not in any pack
before writing; quarantine, audit by gate, then adopt or discard by ruling. pack18/foreign/ is the session-18 record of this.
Handoff: §H.10 — state at 90 % and hand off; next archive = LOWDIN-HANDOFF-19 superset.