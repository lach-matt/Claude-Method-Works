# LOWDIN-HANDOFF-34 — single superset archive (session 34, 2026-08-17). Supersedes HANDOFF-33 + PACK-34.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack34.
Verify:  bash verify34.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-33.md (which chains 32 -> ... -> 18), then: cp pack34/*.py pack34/*.jsonl rt/   (all new files; no supersession; rt/ MUST sit beside the packs)
Gates (all before ANY new work; run in rt/): gates (1)-(57) of README-HANDOFF-33.md (runner: pack34/gates_run.sh, copy beside rt/: `bash gates_run.sh A B` -> ../GATES-34-OPEN.log;
 gates 54-57 are in the runner now; restore pack26/TABLE-FROZEN-SPLIT-SESSION-26.txt into rt/ after gate 27), plus
 (58) SIC_NOCLAMP=1 SUBCELL=1 python3 janak_S.py 21 -> must SKIP x9; if a row is deleted reprints E -0.32698 at f=0.5 (6 s); python3 table_B.py -> Sc -0.0166 Y -0.0109
 (59) SIC_NOCLAMP=1 SUBCELL=1 python3 rz_mech_S.py 21 -> must SKIP; if deleted reprints dS_loc 0.00128 frac_tail 0.003 (6 s)
 (60) LMAX=3 python3 mp2_ent.py 2 21 -> must SKIP; if deleted reprints He E2 -0.04903, Sc E2_ent -0.06522 (~4 s; sympy)
Read first: pack34/BRIDGE-LOWDIN-SESSION-34.md, then FINDING-B, FINDING-A, FINDING-MP2ENT (in that order).
Known: bash egress denies network. Known (F18.1/F30.1/F31.4/F32.1): census rt/ against the packs BYTE-LEVEL to a file at open, before writing, before sealing.
Known: gate 27 regenerates rt/TABLE-FROZEN-SPLIT-SESSION-26.txt shorter than pack26's — restore the pack copy after. Known: tool call ~300 s.
Known (F34.4): mp2_ent's box spectrum needs r_min >= 1e-3/Z (dense symmetric form); do not lower it. Known (F34.3): O-path DEc is R on Sc/Y/La/Lu/Cs, S on Gd.
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-35 superset.