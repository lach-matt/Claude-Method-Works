# LOWDIN-HANDOFF-45 — single superset archive (session 45, 2026-08-19). Supersedes HANDOFF-44.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack45.
Verify:  bash verify45.sh                      (expect ok=N bad=0 EXTRA=0 — BOTH halves, F43.1)
 HALF A is integrity (every listed file present and hashing). HALF B is completeness (no file in the tree absent from the manifest).
 `bad=0` alone does NOT establish the tree is the sealed tree — that was F43.1, and Half B is the repair. Can-fail: `touch pack45/PLANTED && bash verify45.sh` -> extra=1, exit 1.
Runtime: mkdir rt; cp -r pack5/. rt/; cp pack7/pack5/*.py rt/; cp -r pack8/pack5fix/. rt/; cp pack9/*.py pack9/*.jsonl rt/; cp pack10/* rt/;
 cp pack12/*.py pack13/*.py rt/; cp pack16/*.py pack16/*.jsonl rt/; cp pack17/*.py pack17/*.jsonl pack17/*.c rt/; cp pack18/*.py pack18/*.jsonl pack18/*.c rt/;
 then for n in 19..45 IN STRICT NUMERIC ORDER: cp packN/*.py packN/*.jsonl packN/*.c packN/*.json rt/
 F38.1 (s38): the *.json data files MUST be layered too — omitting them loses eps0a_table.json (pack23) and breaks every t7c_cuaudit importer (gates 16,19,21,22,24…).
 rt/ MUST sit beside the packs. Compile: cd rt; gcc -O2 -shared -fPIC -o libshoot.so shoot.c; libshoot_sr.so shoot_sr.c; libshoot_x.so shoot_x.c
 NOTE (s45): pack45/nlchain.jsonl carries **53 rows** and supersedes pack44's 47. The layering order guarantees this; do not copy pack44's after it.
Census: cp pack37/census37.sh . ; bash census37.sh > CENSUS-...txt  (latest-pack rule; only BAD allowed after gate 1 are derive_P{,2,3}.json, gate-regenerated).
 s45: an OPEN census reads ok=278 bad=0 nopack=3. A POSTGATE census reads ok=281 bad=3 nopack=4 and was byte-identical to s44's.
 **Do NOT copy gates_run.sh into rt/** — it is not a runtime file and its presence adds a 4th BAD to the census (F45.1 sub-fault).
Gates (all before ANY new work): cp pack37/gates_run.sh gates_run45.sh ; sed the log name in **gates_run45.sh** to GATES-45-OPEN.log;
 then bash gates_run45.sh 1 8; 9 20; 21 30 (then restore pack26/TABLE-FROZEN-SPLIT-SESSION-26.txt into rt/); 31 45; 46 52; 53 60; 61 71.
 **F45.1 — THE SED MUST TARGET A SESSION-NAMED COPY.** Root `gates_run.sh` is MANIFEST-LISTED. Editing it in place makes verify45.sh report bad=1.
 A procedure that mutates a sealed file cannot precede the gate that checks sealed files. pack45/gates_run45.sh is the s45 copy, sealed.
 Expect gates 1-71: **283 lines, diff = 0 against GATES-45-OPEN.log** except gate 6's 'sec' field.
 **F45.2 — DIFF AGAINST GATES-45-OPEN.log, NOT GATES-44-OPEN.log.** The s44 log's PT8 block is a hand-condensed one-liner, not `nlterm.py`'s stdout, so it cannot be diffed.
   Values agree exactly (3F / 3H / 4I, dsum 2.78e-17 / 0 / 0). Per H.4 the s44 log is sealed and is not rewritten.
 PT8: python3 nlterm.py gate -> lowest 3F / 3H / 4I, dsum <= 3e-17. (72): python3 nlterm.py 21 -> SKIP. (73): python3 soz.py 21 -> SKIP.
 (77): python3 f392_guard.py -> **53 scored, 0 UNSAFE**, exit 0. **Its scored count GROWS WITH THE CHAIN — growth is not divergence** (s45 general ruling).
 (78): python3 nlchain.py show -> **48/53, FIRST DIVERGENCE 25**.
 (79+80): cp pack44/gate7980.py rt/ ; python3 gate7980.py -> PASS, exit 0, 14 clauses, ~4 min.
   Can-fail: `--fail 79` -> exit 1 (PP-0a trips at 9.93e-08 vs bound 1e-8); `--fail 80` -> exit 1 (3 clauses trip on a subclass shifting e by 1e-4).
 (81): bash verify45.sh -> ok=N bad=0 extra=0. Can-fail by planting one unlisted file.
 **(83) NEW, s45**: cp pack45/nlcfg.py rt/ ; python3 nlcfg.py gate -> 8 clauses, <5 s, NO SCF. Can-fail: `python3 nlcfg.py gate --fail` -> exit 1, 3 clauses.
   **ITS EXPECTATIONS ARE THE Z<=48 VALUES (39/47, 42/47) AND MUST BE RESTATED FOR 53 ROWS (45/53, 48/53) BEFORE IT PASSES.** Owed, and it is deliberate: the
   restatement is the next session's first contact with the gate, and a gate whose expectation grows must say so in its own text.
   Stated limit: `ok_fail` is unchanged under `--fail` BY CONSTRUCTION, not by insensitivity. Not evidence of anything.
Read first: pack45/BRIDGE-LOWDIN-SESSION-45.md, then PARTS-OF-THE-LAW.md, then FINDING-CONFIG-COLUMN.md and FINDING-CHAIN-5p.md.
**BINDING BEFORE ANY RUN PAST Z=54**: PREDICTION-4f-COLLAPSE (before Z=55) and PREDICTION-OPENINGS (before Z=57, and again before Z=89). R 1449.
Known: bash egress denies network. Known: tool call ~300 s; a chain step costs ~90-110 s at this width. Known: ground.py caps at Z=108 (R 1426).
Known (F40.1): nlchain's reference is the previous NEUTRAL's configuration on the CURRENT nucleus. Known (F42.2): build configs via nlchain.add — shell order is load-bearing.
Known (F44.2): `margin` does not name its runner-up — read `order[1]`. A margin is never quoted without the channel it is against.
**THE BLOCK OF s44 IS LIFTED**: the configuration column exists. **CONFIG 45/53 and STEP 48/53 travel together and neither is quoted alone** — the 1969 challenge names both.
Handoff: M's ruling — trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-46 superset.
