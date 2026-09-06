# LOWDIN-HANDOFF-47 — single superset archive (session 47, 2026-08-19). Supersedes HANDOFF-46.
**THIS FILE WAS WRITTEN, NOT COPIED (F47.1).** HANDOFF-46's README was a byte-identical copy of
HANDOFF-45's and carried four stale clauses, one of which — layering `19..45` — would have
loaded pack45's 53-row nlchain.jsonl as terminal and silently lost Cs and Ba. **Check this
header against the bridge before trusting any recipe below.**
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store. pack5 … pack47.

Verify:  `bash verify47.sh`   (expect **ok=N bad=0 extra=0**, BOTH halves, F43.1)
 HALF A is integrity (every listed file present and hashing). HALF B is completeness (no file in
 the tree absent from the manifest). `bad=0` alone does NOT establish the tree is the sealed tree.
 Can-fail: `touch pack47/PLANTED && bash verify47.sh` -> extra=1, exit 1. Remove it afterwards.

Runtime: `mkdir rt; cp -r pack5/. rt/; cp pack7/pack5/*.py rt/; cp -r pack8/pack5fix/. rt/;`
 `cp pack9/*.py pack9/*.jsonl rt/; cp pack10/* rt/; cp pack12/*.py pack13/*.py rt/;`
 `cp pack16/*.py pack16/*.jsonl rt/; cp pack17/*.py pack17/*.jsonl pack17/*.c rt/; cp pack18/*.py pack18/*.jsonl pack18/*.c rt/;`
 then **for n in 19..47 IN STRICT NUMERIC ORDER**: `cp packN/*.py packN/*.jsonl packN/*.c packN/*.json rt/`
 F38.1: the *.json data files MUST be layered too (eps0a_table.json, pack23).
 **CHECK AFTER LAYERING, DO NOT ASSUME (F47.1): `wc -l < rt/nlchain.jsonl` must read 55**
 (md5 97ac1c0d67c031d23e71a21a8e0593c5). pack47 adds NO nlchain.jsonl — Z=57 is a CANDIDATE, see below.
 rt/ MUST sit beside the packs. Compile: `cd rt; gcc -O2 -shared -fPIC -o libshoot.so shoot.c;` likewise `libshoot_sr.so shoot_sr.c`, `libshoot_x.so shoot_x.c`.

Census: `cp pack37/census37.sh . ; bash census37.sh > CENSUS-SESSION-N-OPEN.txt`
 s47 OPEN census read **ok=281 bad=4 nopack=4**. Three BAD are the gate-regenerated
 derive_P{,2,3}.json. **The fourth is nlcfg.py and it is EXPECTED**: s47 restated gate 83 in the
 runtime copy, and pack47 now seals the restated file — so from s48 this BAD should DISAPPEAR.
 If it persists, the layering did not reach pack47. **Do NOT copy gates_run.sh into rt/.**

Gates (all before ANY new work): `cp pack47/gates_run47.sh gates_run48.sh`; sed the log name in
 **gates_run48.sh** (never the sealed copy, F45.1) to GATES-48-OPEN.log; then
 `bash gates_run48.sh 1 8; 9 20; 21 30` (then restore pack26/TABLE-FROZEN-SPLIT-SESSION-26.txt
 into rt/); `31 45; 46 52; 53 60; 61 71`.
 Expect gates 1-71: **283 lines, diff = 0 against GATES-47-OPEN.log**, gate 6's `sec` excluded.
 **F45.2 — diff against the LATEST sealed log (GATES-47-OPEN.log), never an older one.**
 PT8: `python3 nlterm.py gate` -> 3F / 3H / 4I, dsum <= 3e-17. (72) `nlterm.py 21` SKIP.
 (73) `soz.py 21` SKIP. (77) `f392_guard.py` -> **55 scored, 0 UNSAFE**, exit 0 — **its count
 GROWS WITH THE CHAIN; growth is not divergence.** (78) `nlchain.py show` -> **50/55, FIRST
 DIVERGENCE 25**. (79+80) `gate7980.py` -> PASS, 14 clauses, ~4 min; can-fail `--fail 79`/`--fail 80`.
 (81) `bash verify47.sh`. (83) `python3 nlcfg.py gate` -> **8 clauses, PASS at (47,55)/(50,55)**,
 restated by s47; can-fail `--fail` exit 1, 3 clauses. **Two of its eight clauses GROW WITH THE
 CHAIN and must be restated by whoever extends it; a change in any of the other six IS divergence.**
 **(84) NEW, s47**: `python3 nlguard.py gate` -> **6 clauses, PASS, ~3 min, RUNS SCF**;
 can-fail `--fail` exit 1, 3 clauses. **Gate 84's expectations are chain-length-INVARIANT — they
 must never be restated.** F44.1: read exit codes UNPIPED; `tail`'s `$?` is not the gate's.

**THE INSTRUMENT CHANGED THIS SESSION — READ §2(2),(4),(5) OF THE BRIDGE BEFORE ANY RUN.**
 F47.2: `hfc2.run2` returns unconditionally at maxit with no flag, so a cycling SCF yields a
 total energy indistinguishable from a converged one. `nlguard.run_guarded` is the repair:
 rung ladder (0.4,100) -> (0.2,600) -> (0.1,1200), **rung 0 IS the ruling field and is tried
 first**, and a channel converging at no rung returns NO NUMBER and joins `fail`.
 F47.3: a guarded D is MIXED-RUNG and carries ~1e-5 in its last stored digit. Cannot flip an ordering.

**Z=57 IS COMPUTED AND NOT SEALED.** `pack47/Z57-CANDIDATE-ROW.json`, flagged UNSEALED-CANDIDATE.
 It came from `nlstep47.py`, not `nlchain.py`. **Appending it by hand mixes instruments in one
 file — M's ruling is owed.** If it is sealed, gates 78 and 83 must be restated for 56 rows.
Read first: pack47/BRIDGE-LOWDIN-SESSION-47.md, then PARTS-OF-THE-LAW.md, then
 pack47/PREDICTION-OPENINGS.md and pack46/PREDICTION-4f-COLLAPSE.md (both now SCORED in §3 of the bridge).
**BINDING BEFORE ANY RUN PAST Z=88**: PREDICTION-OPENINGS again before Z=89. The s47 file does
 NOT cover Ac. R 1449.
Known: bash egress denies network. Known: a chain step costs ~104 s at Z=57 and rises with Z.
Known: ground.py caps at Z=108 (R 1426). Known (F40.1): the reference is the previous NEUTRAL's
config on the CURRENT nucleus. Known (F42.2): **build configs via `nlchain.cfg_from_chain` /
`nlchain.add` — shell order is load-bearing, and s47 broke this in its own first diagnostic.**
Known (F44.2): `margin` does not name its runner-up — read `order[1]`.
Handoff: M's ruling — trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-48 superset.
