# FINDING — T3b' CLOSED (session 15, 2026-08-16). 16/16 attempted; 9 served, 7 NULL/gap. Nothing written to bank.
Convention (fixed s14, before lookup): entrant = shell gained at observed step; hole = M II with one entrant removed, all else fixed.
Route: web_search once to seed, then web_fetch element_name_a.htm -> <el>table1_a.htm (IP) -> <el>table6_a.htm (M II levels).
PB-13' (restated before lookup): flatness persists; kernels deepen; PB-11.1 keeps failing. Predicted NULL: Co, Ni.
## Served this session (E_bind = -(IP + E_hole)/219474.63 Ha)
La 5d  IP 44981 MZH78 + La II 6s2 1S0 7394.57 MZH78            -> -0.2386   TFD -0.0787 SCF -0.3581  BETWEEN (Y)  geo 29.6%
Dy 4f  IP 47900 WSPC78 + Dy II 4f9 6s2 6H15/2 12336.314 NG00   -> -0.2745   TFD -0.6228 SCF -0.7960  shallower (N) geo 157%
Er 4f  IP 49262 WSPC78 + Er II 4f11 6s2 4I15/2 6824.774 MZH78  -> -0.2556   TFD -1.1188 SCF -0.8236  shallower (N) geo 276%
Tm 4f  IP 49879.8 C71 + Tm II 4f12 6s2 3H6 12457.29 MZH78      -> -0.2840   TFD -1.4027 SCF -0.8349  shallower (N) geo 281%
Ni 3d  IP 61619 PG90 + Ni II 3d7 4s2 4F9/2 51045.46 S70        -> -0.5133   TFD -0.8852 SCF -0.8518  shallower (N) geo 69%
## NULL / gap (hole configuration NOT LISTED in Handbook M II table; IP recorded)
Ce 5d6s2 (IP 44672 WSPC78) · Pr 4f2 6s2 donor (44140 WSPC78) · Nd 4f3 6s2 (44562) · Pm 4f4 6s2 (45020) · Sm 4f5 6s2 (45519.6 JRB00)
Eu 4f6 6s2 (45734.74 NRCA00) · Tb 4f8 6s2 donor (47294 WSPC78) · Ho 4f10 6s2 (48567 WSPC78) · Co 3d6 4s2 (63564.6 PG90)
Nulls are gaps: the Handbook lists 4f^(n-1)6s2 only where it lies low (Gd, Dy, Er, Tm, Yb). Not negative results.
## Score (score_t3b_prime.py, RUN-T3B-PRIME-SESSION-15.txt): PB-11.1 between kernels 5/13 · PB-11.2 geo within 30% 3/13.
Holds: Sc, Ti, Cr, La, Gd. Fails: Fe, Ni, Cu, Dy, Er, Tm, Yb, Lu.
## Reading
1. PB-13' HOLDS DECISIVELY. Measured 4f entrant binding is FLAT: Dy -0.27, Er -0.26, Tm -0.28, Yb -0.33 (spread 0.07 Ha) while TFD 4f
   deepens -0.62 -> -1.71 (2.7x) and SCF -0.80 -> -0.84. Same for 3d: Sc..Cu measured -0.29..-0.51 while TFD -0.09 -> -1.14.
2. SCF eigenvalue is nearly flat across Dy-Yb (-0.80..-0.84) but ~3x too deep; TFD is neither flat nor right. The residue is
   the eigenvalue-vs-hole-state seam (relaxation), not the kernel shape — supports PB6 of PREDICTION-T0B-SESSION-13.
3. 5d entrants (La, Gd) sit BETWEEN kernels; Lu does not (shallower than both). Early-series entrants hold, late-series fail:
   the failure grows with shell filling — consistent with intra-shell relaxation scaling with occupancy.
4. PREDICTION MISS: Ni II 3d7 4s2 IS listed (51045.46, S70); Co II 3d6 4s2 is not. Recorded per R 1449 convention.
## Faults
(a) web_fetch URL-seeding resets each turn: element_name_a must be re-fetched before any table page (mechanics, not data).
(b) served_prime.tsv carries s11 rows "Co/Ni NOT ATTEMPTED" plus s15 rows; superseded rows kept, not deleted (record convention).
(c) score_t3b_prime.py: sort crashed on NULL rows (None vs float) — patched to sort on Z; kernel-pair path repointed to pack9.