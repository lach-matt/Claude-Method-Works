# BRIDGE — THE LÖWDIN SESSION 8 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-7.md (read in full, with bridge-6 and DERIVE-P-SESSION-7). Bank
restore-point-2_13 (R 1700, sha256 8057…d857a5) UNCHANGED; nothing written to register/index/store.
Handoff-6 verified 140/140, pack-7 11/11, 0 mismatches. Session-7 derive_P3 regenerated bit-identical
before any new work (reproduction gate).

## 1 · M ruled this session, in order
1. **T2 closure: NO.** The derived law at 100/106 (P_iii, donor term, timing flag, thin 5f margins,
   Sr/Ce/Pr/Ra/Th timing, Lr relativistic) does NOT meet ruling 1. Not closed. Chapter 34 stays gated.
2. **Pack-5 floor: repair now.** Done — REPAIR-FLOOR-SESSION-8.md, pack5fix/.

## 2 · Done (all on disk, LOWDIN-PACK-8)
- Adaptive-bracket eigen (eigen_fix.py); rule-B column of step3 recomputed 106/106: 24 flagged rows moved
  (each deepened once), 82 bit-identical, no verdict moved (87 = 87). Os window 0.3766 → 0.5494; Os
  P_ii/P_iii 0.1678 → 0.1502, IN. Nine other species unchanged to the digit. **10/10 and 100/106 stand.**
- New flag (R 1671 shape): COMPUTED-TFD.tsv was built with the same floor and is NOT audited — scan for
  floor cells before the R 1715 index write. Owed.

## 3 · Next chat's work, in order (after M)
T0  — M to say what "closed without questions" needs beyond 100/106 derived: which of the named residues
      (donor-term timing · 5f margins · five timing steps · Lr) is the blocker, so the next run has a target.
T1' — derivable kernel improvement at 4f/5f (margins) — only if M sends it. Kernel + chain in pack5fix/.
T2  — (re-ask only when T0 is answered and the target is met.)
T3  — outside lookups still owed: Ac III 6d–5f, Ra II nf, Latter's tables; FLAG 1 Rb I / Y III; Bk F^k
      (Carnall 1992) as outside CHECK only.
T4  — COMPUTED-TFD floor audit (new, §2). Then Record (writing chat): R 1701–1734 as bridge-7 T4, plus
      R 1735 M's closure ruling NO · R 1736 floor repair (adaptive bracket, 24 rows, Os) · R 1737
      COMPUTED-TFD floor flag. Each write regenerating artefacts and both gates.
Chapter 34: NOT until closure (ruling 1, unchanged; reaffirmed by ruling 1 of this session).

## 4 · Figures (§H.6)
MEASURED: 24 repaired E_B; Os chain values. CHOSEN: none (bracket mechanics only, invariant to step size).
INHERITED: bridge-7 §4 in full.

## 5 · Files
LOWDIN-PACK-8.tar.gz: REPAIR-FLOOR-SESSION-8.md · BRIDGE-LOWDIN-SESSION-8.md · MANIFEST-PACK-8.txt ·
pack5fix/{eigen_fix.py, step3_fix.py, step3B_fixed.jsonl, WIN_fixed.json, derive_P_fix.py/.json,
derive_P2_fix.py/.json, derive_P3_fix.py/.json}. The _fix scripts import eigen_fix after step2_run and
carry the repaired Os window; they need tfd.py, rad.py, step2_run.py, ground.py, libshoot.so, step3_rows.jsonl
alongside (all in HANDOFF-6 pack5 + PACK-7 pack5).
Bring next: LOWDIN-HANDOFF-6 + LOWDIN-PACK-7 + LOWDIN-PACK-8 + CODE-LOWDIN-2_13.txt, COORDINATES-2_13.csv,
register, compendia. Unread inventory unchanged (~380k words).
Sandbox: sh not bash (brace expansion fails); network OFF; ≤200 s per call held.