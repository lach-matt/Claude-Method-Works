# KERNEL TEST — THE DERIVED LAW UNDER A SELF-CONSISTENT DENSITY — SESSION 8 (2026-08-16)
Bridge-7 T1', run on M's word: "derivability is the goal; errors refine the solution." Bank UNCHANGED;
nothing written to register/index/store. Code: pack5fix/hfs.py, class_hfs.py, step3_hfs.py; data:
class_hfs.jsonl, class_hfs_summary.json, step3_hfs.jsonl (106/106 rows).

## 1 · The kernel change, and why it is derivable
tfd.py: V = −Z/r + V_es[ρ_TF] + V_x[ρ_TF], V_x = −(3ρ/π)^{1/3} (Dirac; the D in TFD), Latter tail V ≤ −q/r.
hfs.py keeps ALL of that and replaces only the density: ρ from the occupied one-electron orbitals of the
same potential, iterated to self-consistency (Gáspár 1954 / Kohn–Sham 1965 exchange-only; run as
Herman–Skillman 1963 with Latter's tail). Occupations: the OBSERVED configuration of the core (ground.py,
NIST 5.12), i.e. the same core the TFD object represents statistically. Nothing chosen: same nucleus, same
functional, same tail, same core count. Mixing 0.3, tolerance 2e-5 in max|r ΔV| — numerics; every SCF
converged in ≤ 31 iterations to < 2e-5. Numerics repaired on the way: numerov_wf's inward tail underflows
for deep core states (noise nodes) — tail cleaned beyond 1e-9·max|u|, node count on nonzero samples; gate:
Tb 4f J_H in the TFD object reproduced 0.04018 exactly through the cleaned path. Bare-nucleus core (N = 0,
rule A at Z 3–10) handled as hydrogenic.

## 2 · Predictions stated before the run (R 1449) — and their fate
P1 J_H(4f, Tb) moves DOWN toward Tb³⁺ 0.0351 but stays above → **FALSIFIED**: it moved UP, 0.0402 → 0.0472.
P2 d-shell class steps (Mn Fe Tc Ru, Os Hs) stay IN → **FALSIFIED**: Tc falls out.
P3 5f: no confident prediction → outcome: Cm fails, Bk passes.
P4 E_B gaps change by O(10 mHa) → **badly under**: miss-step gaps grew 4–10×
   (Mn 0.011 → 0.110 · Tc 0.026 → 0.114 · Gd 0.057 → 0.397 · Cm 0.125 → 0.439). Windows rebuilt (P4 kept).

## 3 · The ten class species under the SCF kernel (per-species scoring, session-7 convention)
| el | kind | gap TFD→SCF | J_H TFD→SCF | P_iii TFD→SCF | verdict |
|---|---|---|---|---|---|
| Mn | miss | 0.0108→0.1099 | 0.0343→0.0410 | 0.098→0.151 | pass |
| Fe | hit | 0.2978→0.4751 | 0.0404→0.0482 | 0.161→0.208 | pass |
| Tc | miss | 0.0262→0.1141 | 0.0278→0.0316 | 0.061→0.092 | **FAIL** |
| Ru | hit | 0.2245→0.3972 | 0.0305→0.0356 | 0.094→0.122 | pass |
| Gd | miss | 0.0569→0.3965 | 0.0355→0.0432 | 0.190→0.249 | **FAIL** |
| Tb | hit | 0.2180→0.6434 | 0.0402→0.0472 | 0.198→0.241 | pass |
| Os | hit | 0.5494→0.3624 | 0.0377→0.0333 | 0.150→0.125 | pass |
| Cm | miss | 0.1250→0.4388 | 0.0289→0.0338 | 0.140→0.173 | **FAIL** |
| Bk | hit | 0.2145→0.6198 | 0.0312→0.0362 | 0.134→0.160 | pass |
| Hs | hit | 0.3261→0.3624 | 0.0297→0.0307 | 0.111→0.116 | pass |
**7/10 per species (5/10 in the shell-window framing).** The three failures are all MISS steps: the
one-electron exchange penalty (0.09–0.25 Ha) cannot bridge gaps of 0.11–0.44 Ha. Under TFD the same gaps
were 0.01–0.13 Ha. **The 100/106 rests on the TFD density; it does not survive the kernel change.**

## 4 · The whole walk under the SCF kernel (step3_hfs.jsonl), held out as before
| | rule A (closed core) | rule B (charge 1) | openings (18) |
|---|---|---|---|
| TFD (pack-5) | 96 | 87 | A 16 |
| SCF (this) | 95 | **97** | A 15 · B 15 |
Rule B GAINS TEN and overtakes rule A. SCF rule B misses (9): Mn Tc Gd Cm (the pairing class, gaps as §3),
La (4f by 0.187) · Ac (5f by 0.096) · Th (5f by 0.245) — the f-collapse arriving ONE STEP EARLY where TFD
had it one step late (Ce, Pr) — Ra (6d by **0.0022** — a hair; timing) · Lr (relativistic, as before).
Rule A moved: Sr Ce Pr recovered; Ca Ba La Ac lost (Ca 3d, Ba 5d: the d-collapse early). Both kernels are
one step off around each collapse, in opposite directions — TFD late, SCF early.

## 5 · What this says (stated, not decided)
- The pairing class is REAL in both kernels (Mn Tc Gd Cm are misses under both), but the SIZE of the
  gap the penalty must bridge is kernel-dependent by an order of magnitude. A one-electron exchange
  penalty closes it under TFD and not under SCF. Either the TFD gaps are fortuitously small, or the
  penalty is a first term of something larger (the whole shell's Hund stabilization, not one electron's).
- The charge-1 object under a self-consistent density is the best single rule seen so far (97/106) and
  its error structure is cleaner: one class (4) + collapse-onset (3) + one hair (Ra) + Lr.
- Chapter 34 unaffected (ruling 1). Nothing closes; the direction is sharper.

## 6 · Figures (§H.6)
MEASURED (kernel): all of the above. CHOSEN: none — mixing/tolerance are numerics, converged. INHERITED:
step-3 candidate lists and ground.py; the per-species pass/fail convention of DERIVE-P §2.