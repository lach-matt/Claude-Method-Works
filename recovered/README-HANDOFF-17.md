# LOWDIN-HANDOFF-17 — single superset archive (session 17, 2026-08-16). Supersedes HANDOFF-16 + PACK-17.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack17.
Verify:  bash verify17.sh                      (expect ok=N bad=0)
Runtime: mkdir rt; cp -r pack5/. rt/; cp pack7/pack5/*.py rt/; cp -r pack8/pack5fix/. rt/; cp pack9/*.py pack9/*.jsonl rt/;
         cp pack10/* rt/; cp pack12/*.py pack13/*.py rt/; cp pack16/*.py pack16/*.jsonl rt/; cp pack17/*.py pack17/*.jsonl pack17/*.c rt/;
         cd rt; gcc -O2 -shared -fPIC -o libshoot.so shoot.c; gcc -O2 -shared -fPIC -o libshoot_sr.so shoot_sr.c
Gates (all four before ANY new work; run in rt/):
 (1) python3 derive_P_fix.py; python3 derive_P2_fix10.py; python3 derive_P3_fix10.py; cmp derive_P3.json ../pack8/pack5fix/derive_P3_fix.json
 (2) python3 probe13.py 20 0.111 10.0 4s 3d          -> "20 lam 0.111 mu -0.893 4s=-0.4611 3d=-0.4109 d=0.0502"
 (3) python3 t5_scf.py                                -> "21 3d probe -0.4866  banked -0.4866" and "57 5d probe -0.3581  banked -0.3581"
     (t5_scf.py __main__ reads ../pack9/T0b_pairs.json relative to rt/ — the only environment-specific line; sed it if extracted elsewhere)
 (4) python3 t7c_kernel.py                            -> "H 1s ... sr(c=137.036) -0.5000064 ..." and "Z=70 1s sr(analytic V) -2634.8449"
     python3 t7c_pol.py gate 26                       -> "26 3d pol sr(c=1e6) -0.378 banked ts_pol -0.378"
Read first: pack17/BRIDGE-LOWDIN-SESSION-17.md, then pack16/PREDICTION-T7-SESSION-16.md (PB1–PB4) and pack16/T7-BUILD-SPEC.md.
Next: T7b (Fock exact exchange; gates He 1s −0.91796, Ne 2p −0.85041; Dirac-local switch regenerates t5 hfs_ts) FRESH, full budget;
      then candidate steps per bridge-17 §3(2) need rulings; T4 writing chat LAST (R 1701–1792 owed).
Known: bash egress denies physics.nist.gov (use web_fetch: element_name_a.htm, then <el>table1_a.htm / <el>table6_a.htm).
Handoff: §H.10 — state at 90 % and hand off; bridge as few files as possible; next archive = LOWDIN-HANDOFF-18 superset.