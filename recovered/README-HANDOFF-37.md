# LOWDIN-HANDOFF-37 — single superset archive (session 37, 2026-08-17). Supersedes HANDOFF-36 + PACK-37.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack37.
Verify:  bash verify37.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-36.md (chains 35 -> ... -> 18) — COPY PACKS IN STRICT NUMERIC ORDER 19..37 — then: cp pack37/*.py pack37/*.jsonl rt/   (all new files;
 no supersession; rt/ MUST sit beside the packs). Compile: cd rt; gcc -O2 -shared -fPIC -o libshoot.so shoot.c; libshoot_sr.so shoot_sr.c; libshoot_x.so shoot_x.c
Census: cp pack37/census37.sh . ; bash census37.sh > CENSUS-...txt   (latest-pack rule; the only BAD allowed after gate 1 are derive_P{,2,3}.json, gate-regenerated).
Gates (all before ANY new work): cp pack37/gates_run.sh . ; bash gates_run.sh 1 8; 9 20; 21 30 (then restore pack26/TABLE-FROZEN-SPLIT-SESSION-26.txt into rt/);
 31 45; 46 52; 53 60; 61 71 -> GATES-37-CLOSE.log name inside the script: sed it to GATES-38-OPEN.log first. Expect: 1-65 as GATES-37-OPEN.log; 61-71 SKIP;
 (68) nlwalk_hf.py 71 -> SKIP (if deleted: Lu 5d D_rel -0.15979 / 6s -0.21137, ~35 s) (69) nlwalk_hfc.py 21 -> SKIP (Sc 3d DEc -0.03188) (70) CLIGHT=1e6 nlwalk_sr.py 21
 -> SKIP (Sc 3d D_rel -0.34175 = Stage 1) (71) nlwalk_sr.py 21 -> SKIP (Sc 3d D_rel SR -0.33330 approx; see nlwalk_sr.jsonl).
Read first: pack37/BRIDGE-LOWDIN-SESSION-37.md, then FINDING-STAGE23, FINDING-HFCORR, FINDING-XSEAM-S, PREDICTION-TERMS.
Known: bash egress denies network. Known: tool call ~300 s. Known (s37): nlwalk_sr.py exec-splits xseam_relax.py (both in rt/); nlwalk_hfc.py patches hfc2 with the
S form (eps_S/v_S) at import — never import it beside a CORR=0 gate in one process. Known (s36): t5_scf is NON-REL; nlwalk Stage 1 non-rel; Stage 3 (nlwalk_sr) SR.
Handoff: M's ruling — trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-38 superset.