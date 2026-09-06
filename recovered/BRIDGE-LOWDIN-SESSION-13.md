# BRIDGE — THE LÖWDIN SESSION 13 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-12.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archives verified: LOWDIN-HANDOFF-11 (8099d49e) 204/204; LOWDIN-PACK-12 (481a822b) 7/7. Reproduction gate PASSED:
derive_P3.json BYTE-IDENTICAL to PACK-8 (10/10 class; Os .1502; Bk .1343; Cm .1403). Probe gate PASSED (RUN-12 lines regenerated).
## 1 · M ruled this session
T0: run (a) AND (b) — both answers needed. T3b: finish BEFORE T0. T4 stands (writing chat LAST). Handoff at 90% (§H.10).
## 2 · Findings
- T3b CLOSED (FINDING-T3B-SESSION-13.md, served.tsv, RUN-T3B, score_t3b.py): 6/6 points served (Sc,Ti,Cr,Fe,Cu 3d; Yb 4f);
  V, Mn NULL (Handbook lists persistent levels only — gap, not negative); Co, Ni, La–Tm, Lu not attempted. PB-11.1 3/6 (holds
  Sc–Cr, fails Fe on: both kernels deeper); PB-11.2 1/6 FALSIFIED; PB-11.3 held but failure is monotone from Cr, not a crossing
  artefact. THE FINDING: measured hole-state binding is Z-flat (3d −0.29..−0.40 Ha; Yb 4f −0.33) while both one-electron
  kernels deepen steeply — the seam is Koopmans': eigenvalue vs hole-state DIFFERENCE; residue = orbital relaxation (R 1578-type
  object/observer distinction at the level of the observable). Scorer fault (Z-only key) registered & repaired; Sc regenerated exactly.
- T0(a) CLOSED, NOT a closure (FINDING-T0A-SESSION-13.md, RUN-T0A, tfdw4.py, probe13.py, probe13a.py): derived lam(s) split selects
  r_switch 1.6–2.3 a.u. for every species, i.e. lam=1 wherever d/f probes live; reproduces RUN-12 lam=1 column (~0.002 Ha):
  Sr repair lost, Ce/Pr toward, holds hold. PA1/PA3/PA4 held, PA2 falsified. Uniform-lam retirement stands; PW5 shape recurs.
- T0(b) OPENED NOT RUN (PREDICTION-T0B-SESSION-13.md): method and PB1–PB6 on record. Session-12 probe script was NOT banked
  (lost artefact); rebuilt as probe13.py and gated on RUN-12 — bank it.
- Object convention fixed for the record: probe core N = Z−2 for M II, Z−4 for M IV/M V (RUN-12 baselines regenerate only so).
## 3 · Next chat, in order
T0(b) — RUN as specified; score PB1–PB6. If PB6 holds, report to M that T0's question is answered jointly by (a)+(b)+T3b:
       the collapse-curve fault is not in the one-electron potential; next derivable candidate acts on the observable
       (hole-state difference; Slater transition state / DeltaSCF, owners named) — RULING OWED before any such run.
T3b' — optional completion: Co, Ni, La–Tm, Lu from ASD levels (Handbook cannot serve them); ~5% each; only if M rules it useful.
T4  — Writing chat, LAST: R 1701–1764 (bridge-12) + R 1765 T3b served/finding · R 1766 T0(a) split retired · R 1767 probe-script
       loss & rebuild · R 1768 T3b scorer fault · R 1769 Handbook NULLs (V, Mn) · R 1770 core-N convention. Chapter 34: NOT until closure.
## 4 · Figures (§H.6)
MEASURED (new, served, refs in served.tsv): Ti, Cr, Fe, Cu 3d; Yb 4f. RECALLED-NOT-ENTERED: none. CHOSEN: none (lam split width 1/9
is the series' own coefficient ratio; r_switch and r_s are density-selected).
## 5 · Files (PACK-13): tfdw4.py probe13.py probe13a.py score_t3b.py served.tsv RUN-T3B-SESSION-13.txt RUN-T0A-SESSION-13.txt
FINDING-T3B-SESSION-13.md FINDING-T0A-SESSION-13.md PREDICTION-T0B-SESSION-13.md BRIDGE-LOWDIN-SESSION-13.md MANIFEST-PACK-13.txt.
Runtime = HANDOFF-11 README recipe + copy pack12/*.py + pack13/*.py into rt. Bring next: LOWDIN-HANDOFF-11 + LOWDIN-PACK-12 + LOWDIN-PACK-13 + project files.