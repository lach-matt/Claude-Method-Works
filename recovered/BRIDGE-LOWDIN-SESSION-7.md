# BRIDGE — THE LÖWDIN SESSION 7 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-6.md (read in full). Bank restore-point-2_13 (R 1700, sha256 8057…d857a5)
UNCHANGED; nothing written to register/index/store. Handoff-6 archive verified 146 files, manifest read;
PACK-4 recovered tfd.py/rad.py. Context at handoff ~60 % (judged) — written early, under §H.10, because
the session's one task closed and the next needs M's ruling before any further run.

## 1 · Done this session (all on disk, LOWDIN-PACK-7)
1. Kernel recovered from PACK-4 code/ and verified: gate2 0.143 / −0.010, gate2.json byte-identical.
2. **T1 run — P derived from the kernel** (DERIVE-P-SESSION-7.md, derive_P.py, derive_P.json).
   Per-species P = (2l+1)J_H from F^k of the entrant shell in the charge-1 TFD object.
   **8/10 windows pass; Tb (4f, +0.063 Ha) and Bk (5f, +0.004 Ha) FAIL.**
   Clause over 106 with derived P: **96 → 98** (Mn Tc Gd Cm recovered; Tb Bk broken). Not 100.
   The derived value is not inside the chosen corridor for f. Under ruling 4 the four are NOT closed.
3. **Fault flagged in pack-5**: 24/106 step-3 rows have E_B clipped at the −0.6 bisection floor (charge-1
   object, ζ = 1). No rule-B hit changes; gaps on those rows understated. Os in the class is affected
   only in the safe direction. Owed: rerun step3 with a deeper floor for charge 1 (pack-5 artefact — M's call).
4. Discrepancy: MANIFEST-PACK-4 lists LOWDIN-HANDOFF-4.md; the PACK-4 tarball does not contain it
   (31 entries, no .md). Bridge-6 said "read §A first" — could not. Handoff-4 content is in project
   knowledge / prior chats only.

## 2 · Rulings needed from M before the next run (one question, two parts)
(a) The derived P fails at f. Which route next: (i) MEASURED F^k from spectroscopic term analyses for
    Tb II / Bk II (outside search; admissible as MEASURED under §H.6?) or (ii) re-derive the penalty as a
    DIFFERENCE of exchange (entrant in d/f vs entrant in the alternative), i.e. a different derivation —
    or (iii) accept 98 with a derived P as the standing result and stop pushing the four?
(b) Repair the pack-5 floor (rerun step3 charge-1 with floor −0.6·max(ζ,3)² or deeper) — yes / later?

## 3 · Next chat's work, in order (after M rules)
T1' — whichever of (a)(i)/(ii) M chooses. Kernel is on disk in pack5/ now (tfd.py, rad.py, derive_P.py).
T2  — closure ruling with the outcome in hand.
T3  — outside lookups still owed (bridge-6 T3): Ac III 6d–5f, Ra II nf, Latter's tables; FLAG 1 Rb I / Y III.
T4  — Record (writing chat): R 1701–1730 as bridge-6 T4, plus this session's: R 1731 kernel recovery + gate
      reverify · R 1732 derived P, 8/10, 98/106 · R 1733 pack-5 floor fault (24 rows) · R 1734 PACK-4
      manifest/tarball discrepancy. Each write regenerating artefacts and both gates.
Chapter 34: NOT until closure (ruling 1, unchanged).

## 4 · Figures (§H.6)
MEASURED: ten P/F^k/E_B (kernel). CHOSEN: none this session. INHERITED: bridge-6 §4 in full.

## 5 · Files
LOWDIN-PACK-7.tar.gz: DERIVE-P-SESSION-7.md · BRIDGE-LOWDIN-SESSION-7.md · pack5/derive_P.py ·
pack5/derive_P.json · pack5/fk_check.py · pack5/tfd.py · pack5/rad.py (copies from PACK-4) · MANIFEST-PACK-7.txt.
Bring next: LOWDIN-HANDOFF-6.tar.gz + LOWDIN-PACK-7.tar.gz (kernel now travels inside pack-7; PACK-4 no
longer required unless iso/ is wanted) + CODE-LOWDIN-2_13.txt, COORDINATES-2_13.csv, register, compendia.
Unread inventory unchanged from bridge-6 (~380k words).
