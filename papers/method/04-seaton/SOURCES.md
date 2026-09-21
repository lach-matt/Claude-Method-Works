# SOURCES.md — provenance map for 04-seaton (not published)

Paper: `PAPER.md`, "A Correction to Seaton's Ratio". Drafted 2026-09-21. Every number in the paper
is produced by `check.py` (18 of 18 obligations, `--selftest` adds three negative controls, all
refuted) or is CITED.

## Where each section draws from

| paper section | source passages (all under `method/members/`) |
|---|---|
| Thesis, §0 | Physics Compendium 841–868 ("A CORRECTION TO SEATON'S RATIO": the table p = 0 / 3 / 1.150 / 0.206 and p ≥ 1 / 10 / −0.015 / 0.177; "valid at p = 0 and undefined at p ≥ 1, which is a domain statement"; "the sign of δ₂ is penetration, not ℓ: 0 of 3 positive at p = 0, 2 of 2 at p = 5, monotone in p between"); Index of Indices 1614–1626 (Λ_ryd, the same figures as "1.15 ± 0.21"); Mathematical Compendium 3737–3738 ("Seaton's ratio δ₂/δ₀ = −ℓ(ℓ+1)/3 is Seaton's; the domain restriction to p = 0 is this work's") |
| §1 D1 (δ, n*, Z_c, R_M) | Physics Compendium 24–42 (Λ_spectra: the transition n* = Z_c √(R_M/(I − E)), δ = n − n*; Z_c the core charge; R_M the reduced-mass Rydberg); Spectra Compendium §0 14–20 (the four coordinates; E = −Z_c²R/(n−δ)²) |
| §1 D2 (Ritz curve) | Spectra Compendium §III "A channel is a curve" 950–958 (δ(n) = δ₀ + δ₂/(n − δ₀)²; δ₀ the limit value, δ₂ the curvature; 274 channels; the sign rule); Mathematical Compendium 770–784 ("The channel curve", "The sign of δ₂", R 1150–1162); Register 1157–1158 |
| §1 D3 (p) | Spectra Compendium §0 "The bound, which needs no measurement at all" 102–106 ("p the core's orbital count at that ℓ … read from the ground-state configuration"); Register 1261 (line 4727: "p, the core's orbital count at this ℓ"); Mathematical Compendium "The Pauli bound" 3030–3038; `tools/populate.py` `core_p` (imported by path; it reads `LW1-ground.py`, the observed ground configurations of register 1306) |
| §1 D4, §2 Theorem 1 | Physics Compendium 518–526 ("Seaton polarisation constant — 3 alpha c^2 / K(l)", K(ℓ) = ℓ(ℓ+1)(2ℓ−1)(2ℓ+1)(2ℓ+3); "Seaton, MNRAS 118 (1958) 504-518; Drake & Swainson, Phys. Rev. A 44 (1991) 5448"); Physics Compendium 684 and Register 1240 ("The ratio δ₂/δ₀ should be −ℓ(ℓ+1)/3 with the polarisability cancelling"); Mathematical Compendium 3120–3131 ("Seaton's term"), 2946–2956 ("Core polarisation": Born & Heisenberg 1924, Mayer & Mayer 1933), 2960–2970 (Seaton 1958, 1983); Physics Compendium 70–80 (the phase-shift reading of δ and Seaton's theorem across threshold — read, not used) |
| §3 data | `recovered/ritz.py` (RECOVERED from conversation 3851d6dc…, 2026-08-03) — the level dictionary `S` of the thirteen series, with limits, masses, R∞ and m_p/m_e; the NIST capture files `extracted/archives/restore-point-2-13/spectra_raw/{CdI,RbI,SrII}.tsv` and `extracted/archives/spectra-levels-store/deliver/queue2/InI.tsv` (EXTRACTED from the Drive mirror's `restore-point-2_13.tar.gz` and `spectra_levels_store.zip`); Spectra Compendium §IV B.1 sources 985–1000 and the published-values table 1005–1016 |
| §4 measurement | `recovered/ryd_close.py` (RECOVERED, same conversation) — the instrument that produced the four figures: curve_fit of the Ritz form, `PMAP` for p, `(d2/d0)/seat`, `statistics.median` and `statistics.pstdev`, the p ≥ 1 statistic taken over series with `abs(seat) > 1e-9`; its printed output of 2026-08-09 in the chat shard, reproduced in `check.py`'s `SOURCE_FIT` (thirteen (δ₀, δ₂) pairs to 4 dp) |
| §5 failure modes | Physics Compendium 44–60 (limit error as n*³, fields as n*⁷ and n*¹⁰, "none exceeds 60"), 500–508 (core dipole polarisability "fails below l = 4 … AND for nf treated as non-penetrating: … alpha_d and alpha_q that then disagree"), 518–526 ("fails at l < 4, and wherever the quadrupole term matters"), 868–901 (the failure-modes table; only the polarisability rows bear on this paper), 116–139 ("Above ℓ = 4 the electron never enters the core and only the polarisability matters"); Register 1112 (dividing the ℓ step at p, d, f by Seaton's ratio makes it worse: 3.31 → 4.15); Mathematical Compendium "Series perturbation" 2934–2942 |
| main volume | The_Method_1_6-2.md 9737 (ℓ(ℓ+1) recorded "as the gate, the collapse switch, the barrier and Seaton's ratio") — a cross-reference only; §22–§23 (5944–6628) are the bracket and its cost surface and carry no definition the paper needed beyond ν = n − δ (6427) |

## What the paper states about the correction, and how strongly

The source's correction is a **domain restriction measured on thirteen series**, and the paper states
it as a measurement (Propositions 1 and 2, MEASURED), never as a theorem. What *is* a theorem is the
relation itself (Theorem 1), which the paper proves from the hydrogenic ⟨r⁻⁴⟩ rather than citing,
because the ratio's independence of α_d and z is the whole point of the test and the derivation is
short. The source's phrase "the relation holds to 15%" is read as the median ρ of 1.150; the paper
says so and prints the three individual values.

## Reproduction — what reproduces and what does not

**Reproduced exactly.** All thirteen (δ₀, δ₂) pairs to 4 dp against the instrument's printed
output; the four statistics to 3 dp (1.150 / 0.206 / −0.015 / 0.177); the class sizes 3 and 10;
the sign counts (0 of 3 at p = 0; 2 of 2 at p = 5; 1 of 2 at p = 1, 2, 3; 2 of 2 at p = 4 — the
source says "monotone in p between" and the fractions are 0, ½, ½, ½, 1, 1); the p table for the
four cores from `populate.core_p` equals the instrument's hand-typed `PMAP`. The fit here is an
exact profile least squares with a certified minimiser, independent of scipy's curve_fit; agreement
to 4 dp on all 26 coefficients shows curve_fit converged to the same (single) basin.

**Interpretation the source leaves implicit, made explicit in the paper.**

1. *The statistic is the median and the population standard deviation.* The source table says
   "ratio to Seaton" and "sd"; the instrument computes `statistics.median` and `statistics.pstdev`.
   The mean (1.273, 0.017) and the sample sd (0.253, 0.194) do not reproduce the table; the median and
   pstdev do. The paper defines D6 accordingly and prints both.
2. *The "10 series" of the p ≥ 1 row include four s series whose ratio is undefined.* Seaton's value
   at ℓ = 0 is 0, the instrument drops them from the median/sd (`abs(seat) > 1e-9`) but counts them
   in `len(B_)`. So −0.015 ± 0.177 is a statistic over **six** series, not ten. The paper's §0 table
   carries both counts. This is a reading of the source, not a correction to it, but a reader of the
   source table alone would take the statistic to be over ten.
3. *p is the core's orbital count at ℓ.* The brief's phrase "no nodes" is not the source's
   definition; the source defines p by the ground configuration (Spectra Compendium §0; register
   1261) and the paper follows the source. (p = 0 does imply the Rydberg orbital carries no radial
   node forced by orthogonality to a core orbital of its ℓ; the paper says this in §5.1 as a
   consequence, not as the definition.)
4. *"Series" = a channel with a Ritz fit.* The instrument fits any series with ≥ 4 members and all
   thirteen qualify; the paper's D2 states the threshold.

**Not reproduced / not reproducible here, recorded.**

- *"Previously recorded: the ratio δ₂/δ₀ comes out at 1.25 … on fourteen channels with δ₀ > 0.01
  … a per-core constant reproducible to two decimals — Si III g gives 1.77 four times, Si III h gives
  1.12 twice"* (Physics Compendium 684, 841–843; Register 1240). No instrument or channel list for that
  measurement was found in `recovered/`, `extracted/` or the chat shard, and the paper does not print
  1.25 as a measurement; §0 mentions "a value such as 1.25 reported there" only as the kind of number
  the correction disowns. Marked for M: which fourteen channels.
- *The prefactor of Seaton's polarisation constant.* The source prints δ₀ = 3αc²/K(ℓ) (Physics
  Compendium 518, Mathematical Compendium 3122, Spectra Compendium 947). The derivation in Theorem 1,
  from ⟨r⁻⁴⟩ = [3n² − ℓ(ℓ+1)]/[2n⁵(ℓ+3/2)(ℓ+1)(ℓ+½)ℓ(ℓ−½)] and δ = −n³ΔE/z², gives δ₀ = 6αz²/K(ℓ),
  i.e. (3/4)α z²/[(ℓ−½)ℓ(ℓ+½)(ℓ+1)(ℓ+3/2)], the familiar 3α/(4ℓ⁵) at large ℓ — **twice the source's
  prefactor**. The ratio δ₂/δ₀ does not depend on the prefactor, so nothing in this paper's result
  turns on it, and the paper prints the derived form. The source's internal use of the constant
  inverts the same formula to extract α from data (`extracted/archives/restore-point-2-13/seaton.py`),
  so its α values would be twice the a₀³ values in the literature if the factor is as it appears.
  **Marked for M**: whether "3αc²/K" is a units convention or a factor-2 slip; I could not consult
  Seaton 1958 (no access through the proxy).
- *Seaton 1958 itself.* The citation form "Seaton, M. J., The quantum defect method, MNRAS 118
  (1958) 504–518" is what the source gives (Mathematical Compendium 2968, Physics Compendium 524,
  Index of Indices 1492) and agrees with my recollection; the paper prints exactly that. Whether the
  ratio −ℓ(ℓ+1)/3 is stated in that paper in that form, or only implied by the polarisation formula
  it uses, was not verified; the paper attributes the ratio "as the spectroscopic literature does" and
  derives it. Marked for M.
- *Bethe & Salpeter 1957.* Cited for the closed form of ⟨r⁻⁴⟩ — a source outside the volumes, added
  because Lemma 1 needs a citation for general n (the exact check reaches n = 30). Publisher and year
  are from memory; marked for M to confirm the citation form.
- *The channel table's Cd I nd ³D₁ value 2.0898.* The Spectra Compendium §II row (line 536: n 5–11,
  7 members, δ +2.0898, σ 0.0049, limit 72,540.050) has the same n-range and limit as the "Cd I d"
  series here. Recomputing from the same seven levels: **median 2.0875, mean 2.0898**. The table's
  value is the mean of the members, not the median — although §0 declares "the stored δ is the MEDIAN
  over a cell's members" (T2, R 1673/1675/1679, which also record that the two coincide for 18
  series). Recorded, not repaired; it corroborates the Cd I levels and the R_M/limit conventions
  (every level enters the mean). The other three Cd I rows have different n-ranges from the series
  used here and were not compared. Marked for M.
- *Three of the four species are absent from the channel table.* Spectra Compendium §II holds Cd I
  (7 rows) but no In I, Rb I or Sr II row; In I's limit 46670.107 appears in §0's bound list. The
  thirteen-series test therefore rests on `ritz.py`'s level dictionary, which is the only place in the
  tree the thirteen series are assembled. Its 80 levels were checked against the NIST capture files
  named above: **79 of 80 occur there at the same n and ℓ**; the one absent, Cd I 5p 43692.384
  (5s5p ¹P°₁), lies below the first row of the Cd I capture, which starts at 6s. That value is the
  known Cd resonance level and was not altered. B.1 of the Spectra Compendium lists Cd II but not Cd I
  among the NIST ASD draws, though the table holds Cd I rows — a listing gap in the source, noted.
- *The brief's "596 rows … recompute … over the channel rows from the volumes' own tables."* The
  channel table carries δ (a median or mean over members) and σ but no δ₂ and no level energies, so
  Seaton's ratio cannot be computed from it; the four numbers come from the thirteen series and were
  recomputed exhaustively over those. The paper does not claim the split over 596 rows.

## Interpretations chosen

- **Atomic masses.** `ritz.py` uses A = 112.41, 114.82, 84.912, 87.906 with R_M = R∞/(1 + 1/(A·m_p/m_e)).
  This treats the nuclear mass as A proton masses; the paper states the formula as used and prints
  the four R_M values so the reader can substitute. The effect on δ is ~10⁻⁵ and on ρ far below the
  printed precision.
- **The Ritz denominator.** The instrument fits δ₂/(n − δ₀)²; Seaton's relation is for the
  coefficient of n⁻² (or n*⁻²). Lemma 3 records the identity and the paper prints the 1/n² refit
  (1.175 / 0.221 and −0.040 / 0.547) beside the headline figures.
- **"Holds to 15%".** Read as |median ρ − 1| = 0.150; the individual departures 10%, 15%, 56% are
  printed.
- **Series labels.** The paper names the term of each series from the capture files (Cd I ³S₁,
  ¹P°₁, ³D₁, ³F°₃; In I ²S, ²D₃/₂, ²F°; Rb I ²S, ²P°₁/₂, ²D₃/₂; Sr II ²S, ²D₃/₂, ²F°). Sr II nf mixes
  J = 5/2 and 7/2 members and In I nf lists both J at the same energy; the fine structure is below the
  precision the fit sees.
- **In I nd** has rms 0.0176, ten times any other series, and a defect rising with n; the paper names
  it in §5.5 as a probable perturbed series and notes it is in the penetrating class, so it does not
  touch the p = 0 figure.

## Figures

All three computed by `figures.py` from `check.py`'s `run_fits()`/`stats()`; no audited plate in
`method/PROOF-FIGURES.tsv` shows Seaton's ratio (the only hit, figure 26.1, is the ν-cost plate).
