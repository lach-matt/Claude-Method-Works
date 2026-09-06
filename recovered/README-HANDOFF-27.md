# LOWDIN-HANDOFF-27 — single superset archive (session 27, 2026-08-16). Supersedes HANDOFF-26 + PACK-27.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack27.
Verify:  bash verify27.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-26.md (which chains 25 -> ... -> 18), then: cp pack27/*.py pack27/*.jsonl rt/
Gates (all before ANY new work; run in rt/): gates (1)-(27) of README-HANDOFF-26.md, plus
 (28) python3 hfterm.py 0                       -> PT0 four rows, last field < 1e-12 (Slater average reproduced)
 (29) python3 hfterm.py 24                      -> must SKIP; if row deleted reprints Cr D_avg 0.19234 dE_term_neu -0.21087 dE_term_ion -0.15196 D_term 0.25125
 (30) CORR=0 python3 hfc2.py 55                 -> must SKIP; if row deleted reprints Cs D_HF 0.12779 == hfdscf (PC1)
 (31) SIC_NOCLAMP=1 python3 limitcycle.py 22 0.3 -> must SKIP; if row deleted reprints Ti it 100 E -0.38063, hist tail period 7 (0.015961 max)
Read first: pack27/BRIDGE-LOWDIN-SESSION-27.md (s3 needs rulings), then FINDING-LIMITCYCLE, FINDING-HFTERM, FINDING-HFC2, CORRECTIONS.
Next: rulings on bridge-27 s3(1)-(4); write predictions BEFORE any run; T4 writing chat LAST (R 1701–1868 owed).
Known: bash egress denies network (web_search works). Known (F18.1): list rt/ for files not in any pack. Known (F24.1/F25.1): MECHANISED, repair pending ruling.
Known (F26.2): HF 'hf' valid at INTEGER occupation only. Known: gate-13 'hfs' is Hartree-Fock-Slater. Known: v_gbz hard-cuts v_c where eps_c>=0.
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-28 superset.