# BRIDGE — THE LÖWDIN SESSION 9 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-8.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to
register/index/store. Archives verified: HANDOFF-6 138/138, PACK-7 11/11, PACK-8 21/21. Reproduction gate PASSED
(derive_P3 byte-identical) — see GATE-SESSION-9.md for the packaging fault found on the way.

## 1 · M ruled this session
1. T0(b) opened ("same object in another mathematical language?"); then: run ALL identifiable tests, every
   answer true or false is an answer. Done — 11 predictions stated first, all scored (FINDING-T0b §tally).

## 2 · Findings (FINDING-T0b-SESSION-9.md, all data in this pack)
- Packaging fault: PACK-8 `_fix` scripts import unfixed derive_P; gate passes only with derive_P.py := derive_P_fix.py.
- TFD vs SCF is one functional (same nucleus/Hartree/Dirac-x/Latter) in two kinetic-energy languages; the map is
  NOT a Z-mean. SCF ε_nl is LINEAR in shell occupancy N with the outer shell fixed (Slater screening, R² .99);
  TFD ε_nl is CONCAVE in Z (empty-shell collapse curve). N is the coordinate the density language lacks.
- Class steps: SCF−TFD gap growth is carried by the entrant's own residual (9/10). No Hund kink in either kernel.
- Whole-shell Hund penalty inside SCF, P_c=(2l+1)/2(J_H+K): 7/10 (Tc misses by 0.002; Gd, Cm by 2–3×) — the SCF
  f eigenvalue is at fault, not P. 100/106 remains a TFD-language result.
- Measured check: only Ca I 3d in the index — TFD +36 %, SCF −140 %: the kernels bracket the truth at onset.
  Hypothesis for T3: measured near the geometric mean of the two (2 points; La recalled, NOT entered).
- WITHDRAWN this session: "−0.10 Ha per added electron" (outer-shell confound, 0.20 Ha).

## 3 · Next chat's work, in order (after M)
T0  — M's ruling on the kernel finding: (a′) build the object with BOTH coordinates — spin-polarised / SIC-free
      orbital density (Hund visible), derivable, and re-score 106; or (d) fix the object as TFD, accept 100/106 as
      the TFD-language law and take the six residues one by one; or another target.
T3  — outside lookups now decisive: Sc–Cu I 3d and La–Lu I 4f bindings (NIST) to score the bracket/geometric-mean
      hypothesis (prediction on record); Carnall Cm³⁺/Bk³⁺; Ac III; Ra II; Latter's tables; FLAG 1 Rb I / Y III.
T4  — Record (writing chat): R 1701–1739 (bridge-8) plus R 1740 packaging fault · R 1741 T0(b) kernel relation
      (linear vs concave; no mean) · R 1742 whole-shell Hund 7/10 · R 1743 Ca I bracket · R 1744 withdrawn "−0.10/e".
Chapter 34: NOT until closure (ruling 1, unchanged).

## 4 · Figures (§H.6)
MEASURED: testA 50 SCF eigenvalues; Ca I δ_d from index. CHOSEN: none (row endpoints are the shells' own
occupancy limits; fits are diagnostics, not law). RECALLED-NOT-ENTERED: La I 4f ≈ −0.17 Ha. INHERITED: bridge-8 §4.

## 5 · Files
LOWDIN-PACK-9.tar.gz: BRIDGE-LOWDIN-SESSION-9.md · GATE-SESSION-9.md · PREDICTION-T0b-SESSION-9.md ·
FINDING-T0b-SESSION-9.md · testA.py · testA.jsonl · testA_fit.json · T0b_pairs.json · T0b_fit.json ·
T0b_classdecomp.txt · MANIFEST-PACK-9.txt. testA.py needs hfs.py + PACK-8 pack5fix + HANDOFF-6 pack5 alongside,
with derive_P.py := derive_P_fix.py (gate note). Bring next: HANDOFF-6 + PACK-7 + PACK-8 + PACK-9 + project files.
Sandbox: sh (no `time`, no brace expansion); network OFF; ≤200 s per call held; SCF ≈ 2 s each.