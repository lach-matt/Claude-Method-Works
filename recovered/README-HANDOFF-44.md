# LOWDIN-HANDOFF-44 — single superset archive (session 44, 2026-08-19). Supersedes HANDOFF-43.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack44.
Verify:  bash verify44.sh                      (expect ok=N bad=0 EXTRA=0 — BOTH halves, F43.1)
 HALF A is integrity (every listed file present and hashing). HALF B is completeness (no file in the tree absent from the manifest).
 `bad=0` alone does NOT establish the tree is the sealed tree — that was F43.1, and Half B is the repair. Can-fail: `touch pack44/PLANTED && bash verify44.sh` -> extra=1, exit 1.
Runtime: mkdir rt; cp -r pack5/. rt/; cp pack7/pack5/*.py rt/; cp -r pack8/pack5fix/. rt/; cp pack9/*.py pack9/*.jsonl rt/; cp pack10/* rt/;
 cp pack12/*.py pack13/*.py rt/; cp pack16/*.py pack16/*.jsonl rt/; cp pack17/*.py pack17/*.jsonl pack17/*.c rt/; cp pack18/*.py pack18/*.jsonl pack18/*.c rt/;
 then for n in 19..44 IN STRICT NUMERIC ORDER: cp packN/*.py packN/*.jsonl packN/*.c packN/*.json rt/
 F38.1 (s38): the *.json data files MUST be layered too — omitting them loses eps0a_table.json (pack23) and breaks every t7c_cuaudit importer (gates 16,19,21,22,24…).
 rt/ MUST sit beside the packs. Compile: cd rt; gcc -O2 -shared -fPIC -o libshoot.so shoot.c; libshoot_sr.so shoot_sr.c; libshoot_x.so shoot_x.c
Census: cp pack37/census37.sh . ; bash census37.sh > CENSUS-...txt  (latest-pack rule; only BAD allowed after gate 1 are derive_P{,2,3}.json, gate-regenerated).
 s44 note: a census taken at OPEN reads bad=0. A census reading bad=3 was taken AFTER gate 1. pack43/CENSUS-SESSION-43-OPEN.txt is mislabelled in this respect; left as sealed evidence (H.4).
Gates (all before ANY new work): cp pack37/gates_run.sh . ; sed the log name to GATES-44-OPEN.log; then bash gates_run.sh 1 8; 9 20; 21 30 (then restore
 pack26/TABLE-FROZEN-SPLIT-SESSION-26.txt into rt/); 31 45; 46 52; 53 60; 61 71. Expect: identical to GATES-44-OPEN.log except gate 6's 'sec' field.
 NEW (PT8): python3 nlterm.py gate -> lowest 3F / 3H / 4I, dsum <= 3e-17. NEW (72): python3 nlterm.py 21 -> SKIP. NEW (73): python3 soz.py 21 -> SKIP.
 NEW (77): python3 f392_guard.py -> 37 scored, 20 drops, 0 UNSAFE, exit 0. NEW (78): python3 nlchain.py show -> 42/47, FIRST DIVERGENCE 25.
 **NEW (79+80), REPLACING BOTH OLD LINES — F44.1**: cp pack44/gate7980.py rt/ ; python3 gate7980.py -> PASS, exit 0, 14 clauses, ~4 min.
   Can-fail: `python3 gate7980.py --fail 79` -> exit 1 (PP-0a trips at 9.93e-08 vs bound 1e-8); `--fail 80` -> exit 1 (3 clauses trip on a subclass shifting e by 1e-4).
   The OLD gate 79 text (`python3 t7e_probe.py`) IS NOT A GATE: that module has no __main__ and exits 0 having compared nothing. The OLD gate 80 text named
   D_of/run/CFG_CA on t7g_exc; they live in **t7f_rep.py**. Both corrected here and nowhere else — README-HANDOFF-43.md is sealed and is not edited (H.4).
 NEW (81): bash verify44.sh -> ok=N bad=0 extra=0. Can-fail by planting one unlisted file.
Read first: pack44/BRIDGE-LOWDIN-SESSION-44.md, then FINDING-CHAIN-4d.md, then FAULT-F44-1.md and FAULT-F44-2.md.
Known: bash egress denies network. Known: tool call ~300 s. Known: ground.py caps at Z=108 (R 1426).
Known (F40.1): nlchain's reference is the previous NEUTRAL's configuration on the CURRENT nucleus. Known (F42.2): build configs via nlchain.add — shell order is load-bearing.
Known (F44.2): `margin` does not name its runner-up — read `order[1]`. A margin is never quoted without the channel it is against.
BLOCKING (s44): the nlchain configuration column. `ok` and the configuration disagreed at 7 of 10 steps in the 4d row; 42/47 is NOT a configuration score.
Handoff: M's ruling — trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-45 superset.
