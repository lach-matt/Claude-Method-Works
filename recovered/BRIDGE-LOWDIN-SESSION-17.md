# BRIDGE — THE LÖWDIN SESSION 17 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-16.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive verified: HANDOFF-16 258/258 (sha f0fd43d3). Gates 1–3 PASSED (derive_P3.json byte-identical; probe13 exact RUN-12 line;
t5_scf Sc 3d −0.4866 / La 5d −0.3581 banked; only its pack9 path repointed, as README-16 anticipated). Chats/transcripts reviewed first.
## 1 · Rulings in force
T7 all three, comparison decides (session 16): T7c DONE, T7a DONE, T7b OWED. M ruled (this session): T7c Go; T7a Go; handoff now at
~60 % with T7b opened FRESH next session (option a). T4 writing chat LAST. Chapter 34 gated on closure. Standing preference: always
both objects. Handoff = single superset archive per session (LOWDIN-HANDOFF-N).
## 2 · Findings
T7c CLOSED (FINDING-T7C-SESSION-17.md, RUN-T7C-SESSION-17.txt): scalar-relativistic KH kernel, c = 137.035999, no constant. Gates: c=1e6
regenerates t5 hfs_ts and t6 ts_pol exactly; H 1s → −0.5000064 (Dirac −0.5000067). The SR shift on 4f TS is +0.163…+0.192 Ha = the
WHOLE shell-constant offset (shift/offset Dy 1.19, Er 0.83, Tm 0.87, Yb 1.00), not half. SR spin-polarised TS: 4f Dy +8.6 %, Er −15.1 %,
Tm −9.8 %, Yb 0.0 % of measurement; 3d 3.6–7.5 %; 5d degraded to the band edge, 12.9/13.2/15.1 % SHALLOW growing La→Lu (the known
relativistic 5d destabilisation; PC2's physics was wrong, the kernel is not). PC1 direction+growth hold, magnitude+"≤ half" fail;
PC2 fails; PC3 holds; pol additivity holds ≤ 0.003 Ha. By the comparison rule T7c is the direction. Faults F17.1 (shoot.c start
exponent, caught by gate before any result; repaired shoot_sr.c), F17.2 (rmin precision limit ~1e-5 rel on core shifts; stated).
T7a CLOSED (FINDING-T7A-SESSION-17.md): orbital-resolved PZ SIC; gate Zn identical to hfs_sic to the last digit; Fe reproduces T6 exactly.
Entrant 4f TS shift ≤ 0.010 Ha on all four; Fe 0.007. PA1 fails (magnitude), PA2 holds, PA3 exclusion follows by a NULL (flagged
reading): at f = ½ self-Hartree (∝ f) and Dirac self-exchange (∝ f^{4/3}) cancel (Yb: +0.618 − 0.564 → −0.054 Ha before relaxation).
T6 channel-averaged SIC column confirmed an artefact of the mean-f weighting. Faults: none.
Standing after T7c+T7a: relativity owns the 4f offset; self-interaction has no leverage on the observable. Residue after SR-pol is no
longer shell-constant: 4f scatter of mixed sign (~0.02–0.04 Ha), 5d small shallow systematic growing La→Lu.
## 3 · Next chat, in order
(1) T7b per T7-BUILD-SPEC.md and PREDICTION-T7-SESSION-16.md (PB1–PB4, do NOT rewrite): Fock exchange on the log mesh (Slater Y^k;
    hfs.numerov_wf inner solver; occupation = scf_occ's). Gates: He 1s ε −0.91796, Ne 2p ε −0.85041 (Fischer 1977, MEASURED-STANDARD, not
    fitted); Fock→Dirac-local switch regenerates the T5 HFS-TS column. Then HF-TS and HF-ΔSCF on the ten species (both objects). PB4's
    exact-exchange branch cannot fire (PC1 gave the whole offset) — T7b now answers whether the exchange LANGUAGE moves the 5d edge / the
    4f scatter, and completes M's "all three".
(2) CANDIDATE, not opened, needs a ruling: sum T7c + T7b if both partly right (comparison rule; R 1449 timing on the sum). Also candidate:
    re-probe Ra II / Th / Lr (relativistic corridor residues, R 1578 class) with t7c_kernel — out of T7 scope, owed as a step.
(3) T4 writing chat LAST: R 1701–1786 (bridge-16) + R 1787 T7c closure (SR shift = the whole offset; 4f inside band on SR-pol; 5d to
    band edge) · R 1788 F17.1 · R 1789 F17.2 · R 1790 T7a closure (orbital-resolved SIC null on the TS observable; f=½ cancellation)
    · R 1791 T6 channel-averaged SIC column re-read as artefact · R 1792 §H.10 handoff at 60 % by ruling (T7b too large to close).
## 4 · Figures (§H.6)
MEASURED: none new (targets from t5/t6 jsonl). RECALLED-NOT-ENTERED: Au 1s/4f DHF orbital energies (recalled during the instrument audit,
uncertain, NOT entered — the audit was scored on pattern only); Fischer 1977 He/Ne HF ε quoted from PREDICTION-T7 as gate standards.
CHOSEN: none. c = 137.035999 is CODATA, not a chosen constant.
## 5 · Files (PACK-17): t7c_kernel.py t7c_run.py t7c_pol.py shoot_sr.c t7c.jsonl t7c_pol.jsonl RUN-T7C-SESSION-17.txt
FINDING-T7C-SESSION-17.md t7a_sic.py t7a.jsonl FINDING-T7A-SESSION-17.md BRIDGE-LOWDIN-SESSION-17.md MANIFEST-PACK-17.txt.
Runtime: as README-HANDOFF-17 (rt/); pack17/*.py + shoot_sr.c into rt/, gcc shoot_sr.c → libshoot_sr.so.
Bring next: LOWDIN-HANDOFF-17 (single superset: HANDOFF-16 + PACK-17 + README + verify17.sh) + project files.