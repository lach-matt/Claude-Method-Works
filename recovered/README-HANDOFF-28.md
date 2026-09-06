# LOWDIN-HANDOFF-28 — single superset archive (session 28, 2026-08-17). Supersedes HANDOFF-27 + PACK-28.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack28.
Verify:  bash verify28.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-27.md (which chains 26 -> ... -> 18), then: cp pack28/*.py pack28/*.jsonl rt/   (pack28 t7c_corrz/t7c_cuaudit/t7b_hf/hfc2 supersede: SUBCELL and frac hooks, default byte-identical behaviour)
Gates (all before ANY new work; run in rt/): gates (1)-(31) of README-HANDOFF-27.md (all reproduce with pack28 files, SUBCELL unset), plus
 (32) SUBCELL=1 SIC_NOCLAMP=1 python3 cellcut_run.py 22 0.3  -> must SKIP; if row deleted reprints Ti it 34 converged True E -0.38064
 (33) SUBCELL=1 SIC_NOCLAMP=1 python3 cellcut_run.py 29 0.3  -> must SKIP; if deleted reprints Cu it 33 converged True E -0.3735
 (34) SUBCELL=1 python3 onefunc.py 39                         -> must SKIP; if deleted reprints Y slope_half -0.028004 D_frozen -0.028685 gap -0.000681
 (35) python3 frachf.py 39                                    -> must SKIP; if deleted reprints Y janak_gap_corr -0.000605 gap_sc -0.000829 (~90 s)
Read first: pack28/BRIDGE-LOWDIN-SESSION-28.md (s3 needs rulings), then FINDING-CELLCUT, FINDING-ONEFUNC, FINDING-FRACHF.
Known: bash egress denies network. Known (F18.1): list rt/ for files not in any pack. F24.1/F25.1 CLOSED under SUBCELL=1. F26.2 LIFTED for class rows
(q_c=0) via t7b_hf.frac; 3d/4f fractional path still needs a second radial function. gate-13 'hfs' is Hartree-Fock-Slater.
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-29 superset.