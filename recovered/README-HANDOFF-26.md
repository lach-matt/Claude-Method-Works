# LOWDIN-HANDOFF-26 — single superset archive (session 26, 2026-08-16). Supersedes HANDOFF-25 + PACK-26.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack26.
Verify:  bash verify26.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-25.md (which chains 24 -> ... -> 18), then: cp pack26/*.py pack26/*.jsonl rt/   (pack26/frozen_scan_corrnone.jsonl supersedes pack25's)
Gates (all before ANY new work; run in rt/): gates (1)-(23) of README-HANDOFF-25.md, plus
 (24) SIC_NOCLAMP=1 python3 frozen_split.py 21   -> must SKIP 21 Z; if rows deleted reprints Sc M_xsic_fine -0.01355 == law, M_exp_grid -0.01454
 (25) SIC_NOCLAMP=1 python3 frozen_resp.py 21    -> must SKIP; if deleted reprints Sc Mresp2_d10 -0.0015, chi_x_d10 0.03603
 (26) python3 hfdscf.py 21                       -> must SKIP; if deleted reprints Sc D_HF 0.26664, eps_koop -0.33564, Delta_c -0.03609
 (27) python3 frozen_split_table.py | tail -7    -> P26.0-4 HELD, P26.5-6 FAILED, as TABLE-FROZEN-SPLIT
Read first: pack26/BRIDGE-LOWDIN-SESSION-26.md (s3 needs rulings), then FINDING-FROZEN-SPLIT, FINDING-HFCORR, FINDING-XFOCK.
Next: rulings on bridge-26 s3(1)-(4); write predictions BEFORE any run; T4 writing chat LAST (R 1701–1863 owed).
Known: bash egress denies network (web_search/web_fetch work). Known (F18.1): list rt/ for files not in any pack. Known (F24.1/F25.1): Ti, Cu at maxit=100, E stable.
Known (F26.2): HF/HFSR mode 'hf' valid at INTEGER occupation only. Known: gate-13 'hfs' is Hartree-Fock-Slater, not HF.
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-27 superset.