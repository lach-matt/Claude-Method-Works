# LOWDIN-HANDOFF-35 — single superset archive (session 35, 2026-08-17). Supersedes HANDOFF-34 + PACK-35.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack35.
Verify:  bash verify35.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-34.md (which chains 33 -> ... -> 18), then: cp pack35/*.py pack35/*.jsonl rt/   (all new files; no supersession; rt/ MUST sit beside the packs)
Gates (all before ANY new work; run in rt/): gates (1)-(62) of README-HANDOFF-34.md (runner: pack35/gates_run.sh, copy beside rt/: `bash gates_run.sh A B` -> ../GATES-35-OPEN.log;
 restore pack26/TABLE-FROZEN-SPLIT-SESSION-26.txt into rt/ after gate 27; gates 61-62 by hand as README-34), plus
 (63) python3 xseam_relax.py 21 -> must SKIP; if the row is deleted reprints D_rel -0.34175 chk 0.0016 relax_E 0.10511 (3 s)
 (64) python3 lwalk.py 21 -> must SKIP x6; if a row is deleted reprints e.g. 3d D_rel -0.34175 / swap D_rel -0.26903 (1-2 s each)
 (65) SIC_NOCLAMP=1 SUBCELL=1 python3 lwalk_hf.py 21 -> must SKIP; if deleted reprints eps_g -0.33564 D_s_rel -0.20292 (12 s)
Read first: pack35/BRIDGE-LOWDIN-SESSION-35.md (§1(3): the n+l WALK IS THE SOLUTION FORMAT — ruled), then FINDING-LWALK, FINDING-B2, FAULT-F35.1.
Known: bash egress denies network. Known (F18.1/F30.1/F31.4/F32.1): census rt/ against the packs BYTE-LEVEL to a file at open, before writing, before sealing.
Known: gate 27 regenerates rt/TABLE-FROZEN-SPLIT-SESSION-26.txt shorter than pack26's — restore the pack copy after. Known: tool call ~300 s.
Known (s35): t5_scf is NON-RELATIVISTIC — the s35 frozen reference and relaxed E-path points are non-rel; the record E path (janak_S) is SR; chk on nd/5d = SR shift.
Known (s35): xseam_relax.py imports its energy functional by exec-splitting; lwalk.py exec-splits xseam_relax.py — both must sit in rt/ together.
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-36 superset.