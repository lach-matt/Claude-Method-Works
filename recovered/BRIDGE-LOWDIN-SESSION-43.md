# BRIDGE — THE LÖWDIN SESSION 43 (2026-08-19)
Successor to BRIDGE-LOWDIN-SESSION-42.md. Bank restore-point-2_13 (R 1700) UNCHANGED.
HANDOFF-42 verified **ok=909 bad=0**. Runtime layered 5 -> 18 -> 19..42 with .json (F38.1).
Gates 1-71 at open: **283 lines, diff = 0, BYTE-IDENTICAL to GATES-42-OPEN.log**, including
gate 6's sec field. PT8 pass (2.78e-17 / 0 / 0). Gate 74 FEASIBLE 13/13 on lam in
[0.215,0.529], 315 pts. Gates 77, 78 reproduce **only after F43.1 was closed** (see §3).
**THE WALK MOVED: chain 29 -> 37 of 107 steps.**

## 1 · Rulings (M, s43)
(1) "**discard and re-derive**" — the unsealed pack43 is discarded, Z=31.. re-walked from
    the sealed 29-step state.
(2) "**yes, adopt exception-naming only**" — NodeGated's exception, not its bracket.
(3) "**The files I gave you are correct. Continue from them.**" — the environment forensics
    are closed; the sealed archive is the ground truth and work proceeds from it.
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 flags; comparison decides; no
scans; no constant beyond c; residue is not closure; T4 LAST; the n+l walk is the solution
format; Delta is a scored column only.

## 2 · Findings (pack43)
(1) **THE 4p ROW GOES 8/8.** Z=31..36 entrant 4p, Z=37..38 entrant 5s, every one matching
    the record. Chained **35/37**, FIRST DIVERGENCE unchanged at **25**.
(2) **7 of 8 filed claims HELD, 1 CONSISTENT-by-flag, 0 FAILED.** First clean sweep of a row.
(3) **THE n+l TIE-BREAK HOLDS ON A SECOND PAIR.** Clause 2 held 10/10 on 4s/3d in the 3d row
    and now 6/6 on **4p/5s**. It is not a property of the pair it was found on.
(4) **THE ROW'S REAL RESULT: argmin n IS NOW WRONG AT FOUR ELEMENTS.** PD-6 reports entrant
    != argmin n at **Z = [19, 20, 37, 38]**; 37 and 38 are new. At Rb and Sr the field picks
    5s while the smallest available n is 4 (4d); n+l separates them (5 vs 6). **n picks
    wrong, n+l picks right**, twice more, in a second row. Same shape as the Lu finding of
    s35. Evidence for the ORDERING VARIABLE, from more than one row for the first time.
    **NOT YET A MECHANISM.**
(5) **THE FIELD IS SMOOTH INSIDE A SUBSHELL.** Per-proton steps -0.05255 -> -0.06260, second
    differences ~ -0.002, against the 3d row's +0.1285 swing in one proton. No shell opens
    inside p and the field says so.
(6) **THE 4d COMPETITION IS ALREADY VISIBLE.** Margin narrows 0.07991 (Z=37) -> 0.05639
    (Z=38), the only counter-trend move in the row. Measured approach, not a prediction.
(7) **PD-6's EXCEPTION SET IS STILL EMPTY** with 8 new steps in; PC3D-10's expected Delta
    break at Z=39..41 has not arrived early.
(8) **RULING 2 EXECUTED AND GATED.** `t7g_exc.HFCN` raises `NodeCountMismatch` (a
    RuntimeError subclass, so every existing catch site still catches it) carrying
    Z, n, l, e, nd, target. Parent: `Z=21 42 nodes 0`. Adopted: `Z=21 4d nodes 0 (target 1)
    at e=-0.083340 -- no normalisable 1-node solution in THIS field`. **Inert: D =
    -0.266643, it [30,35], identical to the s42 D1 reference.** No bracket, no scan.

## 3 · Faults registered this session
**F43.1 — AN UNSEALED `pack43` WAS ON DISK AND THE MANIFEST COULD NOT SEE IT.** Gates 77/78
  read 31/15 and 29/31 against the filed 29/13 and 27/29. Measured: the tarball holds 955
  entries and **no pack43**; MANIFEST-HANDOFF-42.txt holds 909 lines and **zero pack43
  entries**. **`ok=909 bad=0` was TRUE and the runtime was still not the sealed state** —
  `sha256sum -c` reports on files the manifest LISTS, and an unlisted file does not fail the
  check, it fails to be a file. **This is R 1671's fault class reaching the handoff verifier
  itself.** Closed by restoring the store from pack41; gates then reproduce exactly.
  **REMEDY OWED: the verifier must also assert that the tree contains NO file absent from
  the manifest.** Until it does, `bad=0` is not evidence that the tree is the sealed tree.
**F43.2 — I ASSERTED A CAUSE I HAD NOT MEASURED.** Reported the census +2 (274 -> 276) as
  pack42's t7e_probe.py/t7f_rep.py. False — it was pack43's two files. R 1645's class,
  stated to M before it was checked. The remaining delta is now measured: +1 OK is
  TABLE-FROZEN-SPLIT-SESSION-26.txt restored per README after gate 30 and byte-identical to
  pack26; +1 NOPACK is `__pycache__`.
**F43.3 — WITHDRAWN, AND THE WITHDRAWAL IS THE ENTRY.** I diagnosed a "concurrent writer"
  in the container from mtimes and three distinct chain-store hashes, and recommended
  aborting the session on it. **M: "It does not have another writer. You are mistaken."**
  Re-measured: `f392_guard.py` and `delta.py` open the store READ-ONLY, nothing invokes
  `nlchain.py` with a range, no process was running. The artefacts are consistent with a
  REGENERATED TURN of this same conversation — me, in a discarded branch. **This is F43.2
  committed a second time and larger: the first was a wrong cause for a census delta, the
  second was a wrong cause used to recommend that M abandon a session.** The instinct to
  explain an anomaly by an external agent, rather than by my own prior action, is the fault
  to carry forward.
**R 1449 TIMING FLAG (survives F43.3's withdrawal).** While diagnosing F43.1 I READ D_ent
  for Z=31, 32, 33 before writing PREDICTION-CHAIN-4p. Declared at the top of that file;
  PC4P-2 and PC4P-3 score CONSISTENT, not HELD, at those three. **The re-derivation returned
  those three values exactly** — which does NOT legitimate the discarded store. R 1645:
  provenance, not accuracy, is what the gate protects.

## 4 · Next chat, in order
(1) **REPAIR THE VERIFIER FIRST (F43.1).** Add the completeness half: every file in the tree
    must appear in the manifest. Can-fail by planting one unlisted file. **This gates
    everything, because every session opens by trusting `bad=0`.**
(2) **EXTEND THE CHAIN Z=39..48 — THE 4d ROW.** Write **PREDICTION-CHAIN-4d** BEFORE
    pointing nlchain at Z=39. This is where PC3D-10 expects Delta's first break, where s42
    measured 4d clean and unblocked (D = -0.195614), and where the margin is already
    narrowing. **The most informative row yet reached.**
(3) A configuration column in nlchain (s41 finding 5) — still OWED, not blocking (PC4P-7).
(4) PV-3 frozen-vs-relaxed — Ac 5f positive Delta only.
(5) Z=49..108, then Z=109..120 under the s40 ruling.
(6) Reverse derivation to Schrodinger. (7) T4 LAST: R 1701-1966.

## 5 · Figures (§H.6)
MEASURED: the eight chain rows of §2(1); the per-proton steps and second differences; the
D1 inertness pair (-0.266643, it [30,35]); PD-6's exception sets. RECALLED-NOT-ENTERED:
record ground configurations Z=31..38 (comparison column only). CHOSEN: unchanged from s42
(seed, candidate rule, grid 4000/2e-5, qtail 1/2, HF maxit 100, frozen avg-of-config).
DERIVED: rest. **No constant entered beyond c = 137.035999.**

## 6 · Files (pack43)
PREDICTION-CHAIN-4p.md · FINDING-CHAIN-4p.md · t7g_exc.py · nlchain.jsonl (37 rows) ·
this bridge · CENSUS-SESSION-43-OPEN.txt · GATES-43-OPEN.log.
**GATE 80 (new, adopted)**: `t7g_exc` inertness — `D_of(HFCN,(3,2),Z=21)` equals
`D_of(hfc2.HFC,(3,2),Z=21)` at D = -0.266643, it [30,35]; and `run(HFCN, CFG_CA+4d, 21)`
returns ok=False with a `NodeCountMismatch` naming channel, target and e. Can-fail, ~2 min.
**GATE 81 (proposed, owed by F43.1)**: manifest completeness — no file in the tree absent
from the manifest. Can-fail by planting one.

## 7 · Unread / owed
Unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Grüneis-Kresse 2009 / Ren 2013).
Owed: T4; PR3; PN-3; La 4f+corr; PN4 s' channels; PV-3; nlchain config column; **the
verifier's completeness half (F43.1)**.
Known: bash egress DENIES network. Known: ground.py caps at Z=108 (R 1426).
Known: nlchain's reference is the previous NEUTRAL's configuration on the CURRENT nucleus
(F40.1). Known: shell order in `occ` is load-bearing — build configs via `nlchain.add`
(F42.2). Known (s43): `bad=0` from verifyN.sh does NOT establish that the tree is the
sealed tree (F43.1).
