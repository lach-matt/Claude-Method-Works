# LOWDIN-HANDOFF-38 — single superset archive (session 38, 2026-08-18). Supersedes HANDOFF-37 + PACK-38.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack38.
Verify:  bash verify38.sh                      (expect ok=N bad=0)
Runtime: mkdir rt; cp -r pack5/. rt/; cp pack7/pack5/*.py rt/; cp -r pack8/pack5fix/. rt/; cp pack9/*.py pack9/*.jsonl rt/; cp pack10/* rt/;
 cp pack12/*.py pack13/*.py rt/; cp pack16/*.py pack16/*.jsonl rt/; cp pack17/*.py pack17/*.jsonl pack17/*.c rt/; cp pack18/*.py pack18/*.jsonl pack18/*.c rt/;
 then for n in 19..38 IN STRICT NUMERIC ORDER: cp packN/*.py packN/*.jsonl packN/*.c packN/*.json rt/
 F38.1 (s38): the *.json data files MUST be layered too — omitting them loses eps0a_table.json (pack23) and breaks every t7c_cuaudit importer (gates 16,19,21,22,24…).
 rt/ MUST sit beside the packs. Compile: cd rt; gcc -O2 -shared -fPIC -o libshoot.so shoot.c; libshoot_sr.so shoot_sr.c; libshoot_x.so shoot_x.c
Census: cp pack37/census37.sh . ; bash census37.sh > CENSUS-...txt  (latest-pack rule; only BAD allowed after gate 1 are derive_P{,2,3}.json, gate-regenerated).
Gates (all before ANY new work): cp pack37/gates_run.sh . ; sed the log name to GATES-39-OPEN.log; then bash gates_run.sh 1 8; 9 20; 21 30 (then restore
 pack26/TABLE-FROZEN-SPLIT-SESSION-26.txt into rt/); 31 45; 46 52; 53 60; 61 71. Expect: identical to GATES-38-OPEN.log except gate 6's 'sec' field.
 NEW (PT8): python3 nlterm.py gate -> lowest 3F / 3H / 4I, dsum <= 3e-17. NEW (72): python3 nlterm.py 21 -> SKIP (if deleted: Sc gap_avg -0.06372 gap_term -0.06891).
Read first: pack38/BRIDGE-LOWDIN-SESSION-38.md, then FINDING-TERMS-SESSION-38.md, TABLE-TERMS-SESSION-38.txt, PREDICTION-TERMS-VALIDATION-SESSION-38.md.
Known: bash egress denies network. Known: tool call ~300 s. Known (s38): nlterm.py imports hfterm (radial/E_open/E_avg/hund_det) and runs on hfc2 with CORR=False;
 its D_d/D_s reproduce nlwalk_hf to 5 dp. Known (s37): nlwalk_sr.py exec-splits xseam_relax.py; nlwalk_hfc.py patches hfc2 at import — never beside a CORR=0 gate.
Handoff: M's ruling — trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-39 superset.