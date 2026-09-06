# LOWDIN-HANDOFF-33 — single superset archive (session 33, 2026-08-17). Supersedes HANDOFF-32 + PACK-33.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack33.
Verify:  bash verify33.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-32.md (which chains 31 -> ... -> 18), then: cp pack33/*.py pack33/*.json pack33/*.jsonl rt/   (all new files; no supersession; rt/ MUST sit beside the packs)
Gates (all before ANY new work; run in rt/): gates (1)-(53) of README-HANDOFF-32.md (a runner is at pack33/gates_run.sh: `bash gates_run.sh A B` runs gates A..B into ../GATES-33-OPEN.log;
 copy it beside rt/), plus
 (54) SIC_NOCLAMP=1 SUBCELL=1 python3 dzeta.py 39 -> must SKIP; if Y deleted reprints A -0.0009 B 0.00194 D -0.00284 (7 s); ZINT=fx ... -> dzeta_fx.jsonl B 0.00066 D -0.00156
 (55) SIC_NOCLAMP=1 SUBCELL=1 python3 cand_i.py 39 -> must SKIP; if deleted reprints H_tot 0.02524 H_ent 0.01079 Delta_i 0.01444 A_half -0.00083 (7 s)
 (56) SIC_NOCLAMP=1 python3 gd_seam.py            -> D_avg 0.19137 (== frachf D_HF) seam 0.01908 closed_form 0.02159 (~60 s)
Read first: pack33/BRIDGE-LOWDIN-SESSION-33.md, then FINDING-DZETA, FINDING-CAND, FINDING-SEAM, FINDING-GDSEAM (in that order: five candidates against (a)).
Known: bash egress denies network. Known (F18.1/F30.1/F31.4/F32.1): census rt/ against the packs BYTE-LEVEL to a file at open, before writing, before sealing (the loop
used this session is in pack33/CENSUS-SESSION-33.txt's header line of the bridge §6); a name census misses in-place edits. Known: gate 27 regenerates
rt/TABLE-FROZEN-SPLIT-SESSION-26.txt shorter than pack26's — restore the pack copy after (census flag, not a fault). Known: tool call ~300 s.
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-34 superset.