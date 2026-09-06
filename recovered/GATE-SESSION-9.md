# GATE — LÖWDIN SESSION 9 (2026-08-16)
Bank restore-point-2_13 (R 1700) UNCHANGED. Nothing written to register/index/store.
Archives verified: HANDOFF-6 138/138, PACK-7 11/11, PACK-8 21/21 (manifests self-excluded), 0 mismatches.
Reproduction gate: derive_P_fix → P2_fix → P3_fix regenerated; derive_P3.json BYTE-IDENTICAL to banked
derive_P3_fix.json. 10/10 class, Os P_ii 0.1502, Bk P_iii 0.1343. step3B_fixed: 87/106 rule-B, 24 changed.
FAULT (packaging, registered before result read): derive_P2_fix.py / derive_P3_fix.py import `derive_P`,
which in the packs is the UNFIXED pack-7 module (eigen from step2_run, floor −0.6). Run as packed, stage 2
regenerates Os E_nl = −0.6, P_ii = 0.1678 (pack-7 value) — NOT the banked 0.1502. Session 8's runtime must
have had derive_P.py already carrying `from eigen_fix import eigen`. Gate passes only with derive_P.py :=
derive_P_fix.py. Fix owed to PACK-9: `_fix` scripts must import from derive_P_fix, or pack the fixed derive_P.py.
No numerical result changes; the 10/10 and 100/106 stand.