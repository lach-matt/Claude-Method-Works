# DOCKET 67 — close-out: every verdict and figure that moved on M's follow-up rulings

M's rulings on `FOLLOWUPS.md` (verbatim where quoted): a verdict stays only on a correct stated ground, "If there is
none, it is open"; bare negative mass — "include it"; the Hadamard hypothesis in qeihps.py — "do it"; figures —
"address/correct/repair all figures"; status words — "ok, update"; stale figures, including the paper's DOCKET 55
withdrawals — "address/repair/correct". Commits: cbba4db, 9a10717, 310f243 (owners), 426418a (integration),
c9ae0c7 (residue). Every moved value keeps its first-written form as a `*_AS_FIRST_WRITTEN` / `*_WITHDRAWN` constant
or a CORRECTED note, and the old value is still checked as a RECORD.

## 1. Verdicts that moved

| site | was | now | reason |
|---|---|---|---|
| obstruct.py ACHRONALITY | CLOSED-NEGATIVE | **OPEN** | its ground was the false converse of the conjugate-point theorem; no correct ground was found, and `cylinder_converse_fails()` computes the converse failing: on flat R x S^1 x R^2 (period L) a null geodesic has no conjugate point yet is chronal for every s > L/2 (first grid point found, 0.51 L). obstruct census: 32 closed-negative, 2 OPEN (TYPE-IV, ACHRONALITY) |
| index3.py ACHRONAL, DEFOCUS-PROTECTS (now DEFOCUS-NO-CONJUGATE-POINT) | (+1,−1,−1), (+1,−1,0) | (+1,0,0) | same false converse; what is computed is "no conjugate point in the shear-dropped reduction" |
| driven.py standard_table row | REFUTED on an unshown premise | REFUTED **on nonstatic T1–T3 only**, under named hypotheses | HV and Olum reach the corridor only on premises the file now names (`REFUTED_ROW_HYPOTHESES`) |
| phase1.py bare negative mass | excluded (Λ slot None) | **included and ranked first**: Λ = 21.192870, above the corridor for X > 73.5725 b | the positive mass theorem forbids it only under the DEC; its cost is D2 and the DEC (which the corridor's core also violates). The corridor remains the only entry that keeps D2 |
| create.py `which_fails()` | `['D2']` | `['FIXED-MANIFOLD']` | a handle wormhole violates phase1's fixed-manifold clause, not D2 |
| qeihps.py FFKP, FO on HPS | OPEN | **REFUSED** (OPEN only were HPS's state Hadamard) | both theorems hold only for Hadamard states; HPS's state is NOT-ESTABLISHED Hadamard. Carried to ledger O5 and hpscentre O5 |
| pair.py closed-universe total energy | declared 0 | **CONTESTED**: ADM UNDEFINED (computed), Hamiltonian 0 on shell | DOCKET 67 re-derived it; the two readings disagree. Carried to permute.py, index3 CLOSED-ENERGY-CONTESTED, paper H19/H20 |
| apply.py DEC_BRANCH | COLLAPSE (universal) | **split**: COLLAPSE for (T_kk/u)(s/l)² < 2π²/3; OPEN at or above it (T_kk = 2u on a diameter, 0.8225, inside the DEC) | follows S-2 seated OPEN; `dichotomy_is_exhaustive()` = False. index3 DEC-BRANCH-SPLIT (+1,+1,+1) → (+1,0,+1); paper H21 "no case has a demonstrated seat-and-lead", the fourth door OPEN |
| formation.py belt flag | one flag "withdrawn by source" | two: evidence removed by source = True (READ); excluded by source = False (2.03σ, computed) | MacGregor 2018 finds "no need to posit" the belt; that is not a withdrawal |
| index3.py PLANCK-THIRD-TIME (now PLANCK-CROSSING-IS-AN-IDENTITY) | (+1,+1,+1) | (+1,0,0) | DOCKET 55 withdrew its ground in place: the 4.09 l_P crossing is the identity L = l_P/√K |
| index3.py GATE-FAILS-D2 → GATE-FAILS-FIXED-MANIFOLD; ONLY-ENTRY → ONLY-ENTRY-KEEPING-D2; THEOREM-IS-FREE → SHELL-DELAY-IS-13-PERCENT | renamed, cells kept | — | each id asserted a withdrawn claim |
| index3 pins | TRIPLE 290, AFFIRM 171 | 287, 169 | read off the file after the cell moves; controls reproduce 290/171 and the integration's 288/170 exactly |

## 2. Figures that moved (selected; every one computed, first value kept)

- Corridor distance: 4.0 ly → **Proxima 4.2464599 ly** (Gaia DR3 parallax 768.066539187357 mas) in phase1, closeout,
  wormhole (2.725e10 M☉, 15.005 orders), supply (4.871e57 J), nopath (5.4193e42 kg, 2.7248e12 M☉), spectra
  (1.0241e74 kg, 31.28 orders), obstruct, index3, paper H22/H23.
- Nuclear density: recalled 2.3e17 → **address.RHO_NUCLEAR 2.676e17** (DERIVED-FROM-ORDER) in warpdrive, emwarp,
  drivespec (4.544 km, 1.03 M☉), mouth, core (margin 2.530 at 100 km), elements, gatespec, launcher, residue,
  THE-DRIVE.md, WARP-DRIVE.md and ENGINE-ASSESSMENT.md (7.56 km, 1.71 M☉), ROTATING-SHELL.md, necladder, ledger S2/B4
  (7.83e-4). GATE 1 keeps R1 = 4902 m, now stated as 0.859× nuclear (GATE1-SIZED-ON-RECALLED-DENSITY).
- gjw: 4.387e71 D² (energy-density ratio) → **1.097e71 D² on T_kk** (H-WIND), unity at 0.187 l_P; κ π/360 → π/90 in
  scale, rates, obstruct, splitcost (residue 1.3304e52), paper H24.
- concentric Shapiro b-form **0.1315** (paper H10 "13.1 % of the core's advance", not "nearly free"); Jacobi sign
  corrected (core re-run: 228.60/228.72).
- F&T prefactor carried as printed **1/π**; Fewster scalar Dirichlet constant **1440** by default (6.7 %);
  stockgate Ne/Ar restored (largest gap Ne 9.05 dex); CMS bound **0.0034**; branelink exact threshold
  0.999999935193; Garattini r₀ computed 0.6968196708 beside his printed value; seatindex 9.505325e43;
  ħ = h/2π exact in achievable, candidates, tolman, ladder (hierarchy target 1.0110346501e-16).
- DOCKET 55 withdrawals cleared from the paper (H13 headline, table, "4.09 Planck lengths", "theorem rather than a
  budget"), index3's achievable rows, and entangle.py: the duration bound, **71.256 orders at 1 m**, widening as b².
- scale.py: the gjw match is a consistency check on one length (SINGLE-LENGTH), not an independent route.

## 3. Status words updated

QED coefficients READ-VIA-RESTATEMENT (address); horizon computed from READ Planck inputs (cosmo); G_F and m_h READ,
125.20 WITHDRAWN, Higgs-inflation ξ COMPUTED from READ eq. (13) (higgs, excite, xigate, ledger D20, massform S11).

## 4. Left for M — each needs a ruling, nothing was changed

1. **GATE 1 re-size.** It stands at 4902 m = 0.859× nuclear; re-sizing to drivespec's 4544 m moves every GATE 1 figure.
2. **Three index3 cells** (THREE-CROSSINGS-AGREE, PLANCK-FOURTH-TIME, THEOREM-REPRODUCES) keep (+1,+1,+1) with
   corrected text; by the reading applied to PLANCK-CROSSING-IS-AN-IDENTITY their Y/Z would read 0.
3. **The OPEN-cell reading.** Cells moved to 0 on Y/Z for OPEN (the house NU-OPEN reading); some older OPEN rows read −1.
4. Not re-adjudicated against DOCKET 55: index3's BOUNDS-FALL-FASTER-THAN-NEED (candidates.py) and
   QI-CARRIES-THE-WHOLE-WEIGHT (overturn.py); research/README.md's journal keeps first-written passages as history.

## 5. Checks

Full selftest sweep over the instruments under research/warp-drive (281 with a selftest): see the final commit
message for the count. Two fail, and both fail identically at 68d7ac7, before any follow-up: `preserve.py`
(bosonqp.py and phonondex.py replacements from 3f171f8 / 0ab3aa8 not adjudicated) and `subpop.py` (index counts
23 ≠ 20, 5 ≠ 4, chain depths). Neither is a DOCKET 67 file; both are recorded, not repaired.
`ledger.py --check` ok; `tools/docfigures.py` 59/59.
