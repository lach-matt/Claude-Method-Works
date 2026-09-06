# BRIDGE — THE LÖWDIN SESSION 11 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-10.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to
register/index/store. Archives verified: HANDOFF-6 140/140, PACK-7 11/11, PACK-8 21/21, PACK-9 15/15, PACK-10 8/8
(manifests self-excluded), 0 mismatches. Reproduction gate PASSED: derive_P / P2 / P3 BYTE-IDENTICAL to PACK-8
banked (10/10 class; Os 0.1502; Bk 0.1343) via derive_P_fix -> derive_P2_fix10 -> derive_P3_fix10.

## 1 · M ruled this session
1. T0: residuals mean closure is NOT achieved but GIVE DIRECTION; smaller residuals = right path.  2. Then T3.
3. Ruling (a): begin bracket/geometric-mean test and bridge mid-way.

## 2 · Findings
- (d) RESIDUE TABLE CLOSED WITH SERVED VALUES (T3-RESIDUES-SESSION-11.md); all recalled figures retired; 4/4 predictions held.
  Ra II 6d 12084.38 (NIST Handbook M58) -> 0.057 Ha · Ce IV 5d 49737 (NIST via Rynkun+2022 T2 <- Reader&Wyart 2009) -> 0.390
  · Pr V 5d 115052.3 (Kaufman&Sugar 1967 JRNBS 71A 583) -> 0.527 (NEW, no prior figure) · Th IV 6d 9193 (Klinkenberg&Lang 1949)
  vs TFD 5f<6d .044: residue 0.002, SAME ORDER · Lr IV: no measured spectrum -> GAP (null-as-gap).
  READING: Th leaves the kernel class — on its own object TFD is right to .002; the Th miss is object mismatch (neutral 6d²7s²)
  only. Residue class is now {Sr,Ra} d/s-onset (0.07/0.06) and {Ce,Pr} f-onset (0.39/0.53): ONE collapse-curve fault, ℓ-scaled,
  growing along each sequence (Ca->Sr .018->.109; Ce->Pr .39->.53). Target = TFD collapse curve, not the penalty law.
- BRACKET TEST PARTIAL (FINDING-T3-BRACKET-SESSION-11.md): definition & 3 predictions stated first. Sc I 3d served
  (NIST Handbook SC85): E_bind(3d) = 52922.0+11736.36 cm-1 = -0.2946 Ha (4s -0.2411). Between kernels YES; geo mean 29.8% off
  (edge), arithmetic 2.5% off — opposite of Ca I. Reading: the mean is not the object (consistent with session-9 'no mean').
  Ti–Cu I, La–Lu I NOT served. 1 of 6 steps.
- FAULTS: web_fetch ignored its token cap on A&A full-HTML (~15% context; register as tool fault; fetch table sub-pages
  T2.html instead). Sc I 4s vs 3d: measured 3d more bound by .054 Ha in the neutral (R 1303 in Ha).

## 3 · Next chat, in order
T3b — Continue bracket test: NIST Handbook <element>table5.htm (neutral limit) + table6.htm (ion levels) for Ti–Cu I 3d
      (hole state = ion 3d^{n-1}4s^2 term) and La–Lu I 4f; ~5% context per element; score PB-11.1/2/3 at >=6 points.
T0  — Ruling owed: with Th removed from the kernel class and the residue = TFD collapse curve (ℓ-scaled), is a collapse-curve
      correction to the TFD kernel (derivable, no constant) ruled as the closure run? Candidates named, not decided.
T4  — Writing chat: R 1701–1754 (bridge-10) + R 1755 (d) residues served · R 1756 Th object-mismatch · R 1757 Pr V new
      · R 1758 Lr IV gap · R 1759 Sc I bracket · R 1760 fetch-cap tool fault.
Chapter 34: NOT until closure (unchanged).

## 4 · Figures (§H.6)
MEASURED (served, cited): Ra II, Ce IV, Pr V, Th IV levels; Sc I limit, Sc II 4s² ¹S. RECALLED-NOT-ENTERED: none remaining
in the residue table. CHOSEN: none.

## 5 · Files (PACK-11, minimal)
T3-RESIDUES-SESSION-11.md · FINDING-T3-BRACKET-SESSION-11.md · BRIDGE-LOWDIN-SESSION-11.md · MANIFEST-PACK-11.txt.
Runtime unchanged from bridge-10 §5 (HANDOFF-6 + PACK-7 + PACK-8 + PACK-9 + PACK-10; gcc libshoot.so; gate = derive_P_fix.py,
derive_P2_fix10.py, derive_P3_fix10.py). Bring next: HANDOFF-6 + PACK-7…PACK-11 + project files.