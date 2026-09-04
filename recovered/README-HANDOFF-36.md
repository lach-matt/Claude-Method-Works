# LOWDIN-HANDOFF-36 — single superset archive (session 36, 2026-08-17). Supersedes HANDOFF-35 + PACK-36.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack36.
Verify:  bash verify36.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-35.md (which chains 34 -> ... -> 18) — COPY PACKS IN STRICT NUMERIC ORDER 19..36 (F36.1: an out-of-order copy reverts frachf_S.jsonl
 to pack33's; t7c_corrz.py to pack23's) — then: cp pack36/*.py pack36/*.jsonl rt/   (all new files; no supersession; rt/ MUST sit beside the packs)
Census (F36.1 repair): compare each rt file against its LATEST pack copy (globs pack*/ pack*/pack5/ pack*/pack5fix/; pack30/foreign is quarantine), not any pack.
Gates (all before ANY new work; run in rt/): gates (1)-(65) of README-HANDOFF-35.md (runner: pack36/gates_run.sh, copy beside rt/: `bash gates_run.sh A B` ->
 ../GATES-36-OPEN.log; restore pack26/TABLE-FROZEN-SPLIT-SESSION-26.txt into rt/ after gate 27; gate 62 restores xseam.jsonl itself), plus
 (66) python3 nlwalk.py 21 -> must SKIP x4; if a row is deleted reprints 3d D_rel -0.34175 / swap4s D_rel -0.26903 (1-3 s)
 (67) python3 hf_chan.py 57 4f -> must SKIP; if deleted reprints D_HF_rel -0.10556 eps_c -0.23403 (25 s)
Read first: pack36/BRIDGE-LOWDIN-SESSION-36.md, then FINDING-NLWALK, TABLE-NLWALK, FAULT-F36.1.
Known: bash egress denies network. Known: tool call ~300 s. Known (s36): hf_chan Ac 5f hit maxit (it 100) — value is a bound, not entered.
Known (s35): t5_scf is NON-REL; nlwalk Stage 1 is non-rel; the record E path (janak_S) is SR. Known: nlwalk.py exec-splits xseam_relax.py — both in rt/.
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-37 superset.