# LOWDIN-HANDOFF-14 — single archive superseding HANDOFF-11 + PACK-12 + PACK-13 + PACK-14 (2026-08-16)
Contents: pack5..pack11 + BRIDGE-LOWDIN-SESSION-5.md + README/MANIFEST-HANDOFF-11 (= HANDOFF-11 verbatim, 8099d49e) · pack12 · pack13 · pack14.
Each sub-pack keeps its own original MANIFEST (verifiable in place). MANIFEST-HANDOFF-14.txt covers all files.
LATEST BRIDGE: pack14/BRIDGE-LOWDIN-SESSION-14.md. Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store.
Runtime: mkdir rt; cp -r pack5/. rt/; cp pack7/pack5/*.py rt/; cp -r pack8/pack5fix/. rt/; cp pack9/*.py pack9/*.jsonl rt/;
cp pack10/* rt/; cp pack12/*.py pack13/*.py rt/; cd rt; gcc -O2 -shared -fPIC -o libshoot.so shoot.c
Gates: (1) python3 derive_P_fix.py; python3 derive_P2_fix10.py; python3 derive_P3_fix10.py; cmp derive_P3.json ../pack8/pack5fix/derive_P3_fix.json
       (2) python3 probe13.py 20 0.111 10.0 4s 3d  ->  "20 lam 0.111 mu -0.893 4s=-0.4611 3d=-0.4109 d=0.0502"
Verify: bash verify14.sh
Next (bridge-14 §3): T3b' remaining 14 species via Handbook _a route -> T0(b) -> T4 writing chat last.
Known: bash egress denies physics.nist.gov (use web_fetch: element_name_a.htm first, then <el>table1_a.htm / <el>table6_a.htm).