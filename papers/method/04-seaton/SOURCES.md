# SOURCES.md — provenance map for 04-seaton (not published)

Paper: `PAPER.md`. **Title, settled 2026-09-24 at the author's direction** (carried until then as a working title from the repair pass): *"The Domain of the
Polarisation Ratio δ₂/δ₀ = −ℓ(ℓ+1)/3: a Necessary Condition from the Core Configuration, Tested on
Thirteen Rydberg Series"*. The paper was drafted 2026-09-21 as **"A Correction to Seaton's Ratio"**
and retitled in the repair pass of 2026-09-24 (AUDIT.md R-21, A-13): the audit found that the
n-dependent polarisation defect and its restriction to non-penetrating series are the standard
account (Van Vleck & Whitelaw 1933; Edlén 1964; Freeman & Kleppner 1976), so the paper corrects
nothing in the literature; that "Seaton's ratio" is the corpus's name and not the literature's; and
that the sentence "as the spectroscopic literature attributes it" rested on a paper (Seaton 1958)
that was never read. The new title names what the paper establishes — the p criterion as a necessary
condition with the orbital-collapse proviso, the exact reproducible fit with its sensitivities, and
the sign rule — and claims no priority. The corpus's own phrase "the domain restriction to p = 0 is
this work's" (Mathematical Compendium 3737–3738) survives in the paper only as the p criterion, now
stated as necessary and not sufficient.

Every number in the paper is produced by `check.py` (**32 of 32 obligations**: 7 PROVED, 11 EXHAUSTIVE,
2 MACHINE-CHECKED, 8 MEASURED, 1 CROSS-CHECK, 3 SOURCE; `--selftest` adds four negative controls, all
refuted) or is CITED.

## The repair pass of 2026-09-24 (against AUDIT.md)

Every finding's disposition is in `AUDIT.md` Part C and its repair record. What bears on provenance:

- **Lemma 2 (A-1).** The printed rearrangement had lost a factor 2; the correct factor is
  2(n−δ)²/(n(2n−δ)) = 1 − (3nδ − 2δ²)/(n(2n−δ)). Both identities are now exact obligations
  (`ob_defect_rearrangement`, 121 grid points above degree) and the wrong factor is a negative
  control. Theorem 1's first-order conclusion was never affected.
- **The domain (A-20 / R-11).** The corpus itself splits p = 0 into uncollapsed and collapsed
  regimes (Register 1261 regimes 3 and 4; Mathematical Compendium 3066–3070: "across 116 p = 0
  channels at l = 2 or 3: collapsed median 0.637, uncollapsed 0.036", Ca I nd = 0.908, Ba II nf =
  0.756; 530–534: Seaton's term fails on Ba II and Hg II "where the 4f orbital has collapsed into the
  core and the series penetrates"). The paper's D4 now defines the class N := p = 0 and uncollapsed,
  with the collapse account cited to Goeppert-Mayer 1941 and Griffin, Andrew & Cowan 1969 exactly as
  Mathematical Compendium 3070 and Physics Compendium 484 print them. The four cores (Z = 37, 38,
  48, 49) are far below the 4f onset at the lanthanides, so the three p = 0 nf series are in N and
  **nothing measured changed**. §5.3 was re-examined: the argon-like d test (Ca II nd) the earlier
  draft proposed is not clean — Register 1262 places the argon-core d channels across the 3d
  threshold (y = 0.086 at K I, 0.291 at Ca I/Ca II, 0.342 at Sc III, 0.373 at Ti IV) — and the paper
  now says so without citing that measurement.
- **Lemma 1 (R-2)** is proved for all n through the Kramers–Pasternack recursion, CITED to
  Pasternack 1937, with ⟨r⁻²⟩ CITED to Bethe & Salpeter 1957 §3 (Mathematical Compendium 1956);
  `check.py` verifies the recursion at 902 (n, ℓ, s) triples, the seeds on 435 states and the algebra
  on a rational grid. **Lemma 4** (new) derives ⟨r⁻⁵⟩ and ⟨r⁻⁶⟩ the same way, verified on 406 states,
  and Corollary 1 machine-checks that a positive quadrupole term gives ρ > 1 (R-14); the directions of
  the second-order dipole and residual-penetration corrections are now stated as undetermined.
- **The Z3 obligation (A-2)** now encodes the premise (the ⟨r⁻⁴⟩ form) and lets Z3 derive the
  ratio from two-point coefficients, with a third point for affineness; its fidelity guard compares
  the Z3 term with the Laguerre integral (`expect_power`), which shares no formula with it. Seed 5.
- **The independent fit (A-6)** is a float Gauss–Newton fitter in `check.py` (`gauss_newton`), 26 of 26
  coefficients to 4 dp. `SOURCE_FIT`/`SOURCE_STAT` remain, as comparisons with the instrument's
  printed output, and the paper now describes them as "figures previously computed for the same
  data" on which no claim rests.
- **Sensitivities (R-13, R-19)** are `ob_sensitivity`: lowest member out (ρ 1.051 / 1.154 / 1.623),
  the quotation floor as a linearised sum over members of |Δρ| for half a unit in NIST's last
  quoted digit (0.0164 / 0.0016 / 0.0020 — a different procedure from the auditor's ±0.009 propagation,
  and stated as such), the Cd II limit's published ±0.13 cm⁻¹ (capture header; ρ 1.120–1.180) and
  +0.1 cm⁻¹ on every limit. The In II and Sr III limit uncertainties are not held in the tree.
- **The implied polarisabilities (R-12 / A-19).** Table 3 prints α = δ₀K(ℓ)/(6z²): 24.76 a₀³ (Cd⁺),
  26.20 (In⁺), 10.21 (Sr²⁺). The comparison with published values is **not made** in the paper and
  the paper says so: the auditor quoted α(Sr²⁺) = 5.8 a₀³ from Mitroy, Safronova & Clark 2010, which
  would put the model's δ₀(Sr II nf) at 0.037 against the fitted 0.0648 — but arXiv, IOP and APS are
  blocked by the proxy, no copy of that table is in the tree, and a number is not printed on
  recollection. **Marked for the author**: confirm α(Sr²⁺) (and Cd⁺, In⁺ if tabulated) from that
  review and add the sentence; if 5.8 stands, Sr II nf fails the model at the δ₀ level by a factor
  1.8 before any ratio is taken.
- **Table 2 (A-18)** is now printed at NIST's quoted precision, generated by `check.py` from the
  capture strings (`quoted_levels`); the one level absent from the captures (Cd I 5p) keeps its
  three decimals from the level dictionary.
- **Typography (A-12).** No code span holds mathematics. α_d is now α (D5 defines α as the dipole
  and β as the quadrupole polarisability, since Unicode has no subscript d or q); R_M is Rₘ; the
  effective quantum number is written n∗ (U+2217) so that no markdown asterisk can pair. In the finishing pass Table 1 gave up its A and Rₘ columns (ten columns wrapped every Rₘ value in
  the PDF); the four (core, A, Rₘ) triples are printed in the table's caption, so the values remain printed
  for a reader to substitute another convention.
- **Declined (R-17).** A comparison of the Rb I Ritz coefficients with the millimetre-wave and EIT
  values (Li et al. 2003; Mack et al. 2011) would calibrate what a six-member fit can say about δ₂;
  the values are not held in the tree and could not be verified against their sources here, so
  nothing is printed. **Marked for the author** as worth adding.

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
  **Settled 2026-09-24, at the author's direction**: a factor-2 slip, not a units convention. The
  compendia define K(ℓ) = ℓ(ℓ+1)(2ℓ−1)(2ℓ+1)(2ℓ+3) (Physics Compendium 522, Mathematical Compendium
  3122) — the paper's K — so the two forms differ by exactly two, and the derived form is the one an
  independent series supports: on Rb ng, δ_g(30) = 0.00405(6) (Afrousheh et al. 2006) against
  α_d(Rb⁺) = 9.116(9) a₀³ (Berl et al. 2020) and 9.11 a₀³ (Lim et al. 2000, coupled cluster), 6α/K(4)
  gives 0.003946 and 3α/K(4) gives 0.001973; with c₂/n² and Lemma 4's quadrupole term at Berl's
  α_q = 38.4 a₀⁵ the model gives 0.004080, inside the measurement's uncertainty. The paper now says so
  in §2 ("The prefactor"), the check carries the arithmetic as a MEASURED obligation with the 3/K form
  as a fifth negative control, and the three references are added (verified by web search; the
  publishers' pages are behind the proxy). Seaton 1958 itself is still unread here, and nothing rests
  on it. The consequence for the record — `seaton.py` reports every α at twice the literature's
  value — is recorded, not repaired.
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

## The references, verified against what the record prints

Every reference was checked against what the volumes themselves print. Components **not held
anywhere in the tree are not printed in the paper**, and each is named here.

| reference | held in the record | NOT held, and therefore not printed |
|---|---|---|
| Seaton 1958 | *"Seaton, The quantum defect method, MNRAS 118 (1958) 504-518"* — Mathematical Compendium 2968, Physics Compendium 524, Index of Indices 1492 (three independent sites, agreeing); `extracted/archives/restore-point-2-13/params.py` 108 carries the same string | the initials **M. J.** — no site in `method/`, `recovered/`, `docs/` or `extracted/` prints them |
| Seaton 1983 | *"Quantum defect theory, Rep. Prog. Phys. 46 (1983) 167-257"* — Mathematical Compendium 2968, 2850; Index of Indices 1492 | initials |
| Born & Heisenberg 1924 | full title *"Über den Einfluss der Deformierbarkeit der Ionen auf optische und chemische Konstanten"*, *Z. Phys.* **23** (1924) 388–410 — Mathematical Compendium 2956, 3018, 3130; Physics Compendium 504 | initials **M.** and **W.** The paper expands the journal abbreviation *Z. Phys.* to *Zeitschrift für Physik*, which is the unambiguous expansion of the abbreviation the record prints |
| Mayer & Mayer 1933 | full title *"The polarizabilities of ions from spectra"*, *Phys. Rev.* **43** (1933) 605–611 — Mathematical Compendium 3018; the volume and first page also at 2956 and Physics Compendium 504 | initials **J. E.** and **M. G.** |
| Drake & Swainson 1991 | *"Drake & Swainson, Phys. Rev. A 44 (1991) 5448"* — Physics Compendium 524, Mathematical Compendium 532 and 3517, Spectra Compendium 1014 | **the title and both sets of initials were verified by web search on 2026-09-24** (APS record, journals.aps.org/pra/abstract/10.1103/PhysRevA.44.5448: G. W. F. Drake and R. A. Swainson, "Quantum defects and the 1/n dependence of Rydberg energies: Second-order polarization effects") and are now printed; 5448 is printed as the first page only |
| Bethe & Salpeter 1957 | *"Bethe & Salpeter, Quantum Mechanics of One- and Two-Electron Atoms (1957), sec. 3"* — Mathematical Compendium 1956 | publisher and city (an earlier draft printed "Springer, Berlin" from memory; **removed**), and both authors' initials. The paper now prints author, year, title and §3, which is what is held |
| Hartree 1928 | *"Hartree, Proc. Camb. Phil. Soc. 24 (1928) 89"* — Mathematical Compendium 2908; the page range **89-110** at Physics Compendium 554 | initials **D. R.** |
| Theodosiou, Inokuti & Manson 1986 | *"At. Data Nucl. Data Tables 35 (1986) 473-486, Hartree-Slater, for all ionisation stages of all ions with Z ≤ 50"* — Index of Indices 1492, Mathematical Compendium 3030, Spectra Compendium 1012 | initials |
| Kramida, Ralchenko, Reader & the NIST ASD Team 2024 | the whole entry, verbatim: *"Kramida, A., Ralchenko, Yu., Reader, J. and NIST ASD Team (2024). NIST Atomic Spectra Database (ver. 5.12). https://physics.nist.gov/asd DOI 10.18434/T4W30F"* — main volume 11562 | the publisher line "National Institute of Standards and Technology, Gaithersburg" (an earlier draft printed it; **removed** — it is not in the record) |
| Ritz 1903 | *"Ritz, Zur Theorie der Serienspektren, Ann. Phys. 12 (1903) 264-310"* — **Mathematical Compendium 780 and Physics Compendium 464**; initials **W.** at main volume 11666 | nothing. **Correction (A-13):** the first finishing pass stripped this entry to a description on the ground that "no part of the citation appears anywhere in the tree" — the grep was for "Annalen" and the tree abbreviates to "Ann. Phys.". The entry is restored exactly as the two sites print it, with the journal expanded (see the expansions below) |

**Journal abbreviations expanded (A-15).** The tree prints MNRAS, Phys. Rev., Phys. Rev. A, Proc. Camb.
Phil. Soc., At. Data Nucl. Data Tables, Rep. Prog. Phys., Z. Phys., Ann. Phys. and J. Phys. B; the paper
expands each to its unambiguous full name (Monthly Notices of the Royal Astronomical Society, Physical
Review, Physical Review A, Atomic Data and Nuclear Data Tables, Reports on Progress in Physics,
Zeitschrift für Physik, Annalen der Physik, Journal of Physics B). Hartree 1928 is no longer cited
(R-25: it is the self-consistent-field paper, not the penetration argument; Edlén 1964 is).

**References added in the repair pass (R-22), and where each was verified.**

| reference | held in the tree | verified by search (2026-09-24) |
|---|---|---|
| Edlén, B. (1964). Atomic spectra. *Handbuch der Physik* XXVII, 80–220 | Mathematical Compendium 188, 2814, 2826 ("Edlen, Atomic spectra, Handbuch der Physik XXVII (1964) 80-220"); initial **B.** not held, printed on the audit's record | — |
| Goeppert-Mayer, M. (1941). Rare-earth and transuranic elements. *Phys. Rev.* 60, 184–187 | Mathematical Compendium 3070, 2862; Physics Compendium 484 (title, journal, volume, pages); initial **M.** not held, printed on the audit's record | — |
| Griffin, D. C., Andrew, K. L. and Cowan, R. D. (1969). Theoretical calculations of the d-, f- and g-electron transition series. *Phys. Rev.* 177, 62–71 | Mathematical Compendium 3070, 3176; Physics Compendium 484; initials not held, printed on the audit's record | — |
| Freeman, R. R. and Kleppner, D. (1976). Core polarization and quantum defects in high-angular-momentum states of alkali atoms. *Phys. Rev. A* 14, 1614 | Spectra Compendium 1016 ("Freeman & Kleppner 1976, Na I ng") only | APS record, doi 10.1103/PhysRevA.14.1614: authors, title, volume 14 issue 5 page 1614 |
| Van Vleck, J. H. and Whitelaw, N. G. (1933). The quantum defect of nonpenetrating orbits, with special application to Al II. *Phys. Rev.* 44, 551 | not held | APS record, doi 10.1103/PhysRev.44.551: authors, title, 44, 551, October 1933; the last page was not verified and is not printed |
| Pasternack, S. (1937). On the mean value of rˢ for Keplerian systems. *PNAS* 23, 91–94 | not held | PNAS record, doi 10.1073/pnas.23.2.91: author, title, 23(2), 91–94, 15 February 1937 |
| Gallagher, T. F. (1994). *Rydberg Atoms*. Cambridge University Press | not held | publisher's and Internet Archive records: Cambridge Monographs on Atomic, Molecular and Chemical Physics 3, 1994, ISBN 9780521385312 |
| Mitroy, J., Safronova, M. S. and Clark, C. W. (2010). Theory and applications of atomic and ionic polarizabilities. *J. Phys. B* 43, 202001 | not held | IOP record, doi 10.1088/0953-4075/43/20/202001; arXiv:1004.3567. The paper's text could not be fetched (proxy), so no value from its tables is printed |

**The central attribution, as it stood before the repair pass (superseded by the Provenance paragraph of §2).** The relation δ₂/δ₀ = −ℓ(ℓ+1)/3 is attributed to Seaton.
What the record supports is: (i) the relation itself — *"The ratio δ₂/δ₀ should be −ℓ(ℓ+1)/3 with the
polarisability cancelling"* (Physics Compendium 684); (ii) that the polarisation term `3αc²/K(ℓ)`
it comes from is credited to Seaton (1958) — Mathematical Compendium 3130, Physics Compendium 518–526,
Spectra Compendium 947 and 1014; (iii) the bibliographic record above; and (iv) the corpus's own
division of credit, *"Seaton's ratio δ₂/δ₀ = −ℓ(ℓ+1)/3 is Seaton's; the domain restriction to p = 0
is this work's"* (Mathematical Compendium 3737–3738). **What the record does NOT support** is that
Seaton 1958 states the ratio in that form: I could not obtain MNRAS 118, 504 through the proxy, and
no passage in the tree quotes it. The earlier draft said in §2 that the ratio "is attributed to Seaton here as it is in the
spectroscopic literature"; the audit (R-21) found that sentence unsupported, and the repair pass
replaced it with a Provenance paragraph that attributes the polarisation formula to the literature
that states it (Born & Heisenberg 1924, Van Vleck & Whitelaw 1933, Mayer & Mayer 1933, Edlén 1964,
Freeman & Kleppner 1976), cites Seaton 1958 for the quantum defect method only, and claims no
priority. Nothing in the paper's result depends on who first wrote the ratio down. The corpus's
phrase "Seaton's ratio" is not used in the paper. **Marked for M**: whether the books' attribution of
the ratio to Seaton 1958 should itself be revisited.

## Data provenance, verified

- **Species and levels.** Thirteen Rydberg series of four species — Cd I (s, p, d, f), In I (s, d, f),
  Rb I (s, p, d), Sr II (s, d, f) — **80 levels in all**, n from 4 to 12. The level dictionary is
  `recovered/ritz.py`'s `S`, read by AST (the file's own `import scipy` cannot run here); `check.py`
  transcribes nothing.
- **Source and version.** NIST Atomic Spectra Database, **version 5.12**. The version is held in two
  independent places: the Cd I capture's own header line (*"Cd I — NIST ASD 5.12, refs
  L3466/L3486/L3641/L9542/L18843"*) and the main volume's References entry (ver. 5.12, DOI
  10.18434/T4W30F).
- **Retrieval date — what is held and what is not.** Only the In I capture carries an explicit date:
  *"In I — NIST ASD levels, fetched live 2026-08-14"*. The Cd I, Rb I and Sr II captures name the
  database and its references but no date. The two archives holding them are dated 2026-08-24 in
  `drive/MANIFEST.tsv`, and the seated retrieval record for the ground configurations gives
  2026-08-09. **Settled 2026-09-24**: the chat export dates each capture's writing — the Cd I capture
  was written on 2026-08-08, Rb I and Sr II on 2026-08-09, and In I's header dates its fetch
  2026-08-14 — so the paper now prints "8 August 2026 (Cd I), 9 August (Rb I and Sr II) and 14 August
  (In I)" in §3 and "retrieved 8–14 August 2026" in the reference.
- **Limits.** Cd I: Cd II (5s ²S₁/₂) = 72,540.05 ± 0.13 cm⁻¹, marked PUBLISHED in the capture header.
  In I: In II ¹S₀ = 46,670.107, from the capture header. Sr II: 88,965.18, from the capture header.
  Rb I: 33,690.81 — **the Rb I capture header reads "limit fitted", and that line is stale**: register
  1261's krypton-core entry (line 4715) records *"Rb I (limit 33690.81, published)"* and states
  outright that a first limit fitted from the series alone gave 33,474.6 with σ(δ) of 0.25 to 0.89,
  against 0.0012 to 0.016 for the published one. The value in `ritz.py` is the published one. The
  paper's §3 therefore says "none is fitted from its own series", and §5's "tabulated, not fitted"
  stands. Recorded, not repaired.
- **Masses.** A = 112.41, 114.82, 84.912, 87.906 — the tabulated atomic weights of Cd, In and Rb and
  the ⁸⁸Sr isotope mass, as `ritz.py` holds them; `R_M = R_∞/(1 + 1/(A·m_p/m_e))` with
  R_∞ = 109737.31568 cm⁻¹ and m_p/m_e = 1836.15267343, both from `ritz.py` and both now printed by
  `check.py`.
- **How the channels were fitted.** Not by the source's `curve_fit`: `check.py` solves the
  least-squares problem of D2 independently and exactly. For fixed δ₀ the model is linear in δ₂, so
  δ₂*(δ₀) is closed-form and S(δ₀) is an exact rational function; S is scanned at 401 equally spaced
  exact rationals, the least is bracketed, and ninety exact ternary steps narrow the bracket to
  ≤ 1.5 × 10⁻¹⁸. The minimiser is **certified** — S there is at or below S at every scanned point and
  at both ends of the final bracket — and the scan's local minima are counted, so a second basin would
  be reported; the maximum over all thirteen series is 1. Agreement with the source's `curve_fit`
  output to 4 dp on all 26 coefficients is then a cross-check of two implementations, not a
  transcription.
- **Table 2 against the paper.** The eighty (series, n, E) triples printed in PAPER.md were compared
  with `ritz.py`'s dictionary programmatically: **exact bijection, 80 = 80, no difference either way.**
- **Table 2 against a second retrieval.** 79 of the 80 occur, at the same n and ℓ, in the per-species
  NIST capture files. The one that does not is Cd I 5p (5s5p ¹P°₁, 43,692.384 cm⁻¹), which lies below
  the Cd I capture's first row (that capture begins at 6s). §3 of the paper now says so.

## Interpretations chosen

- **Atomic masses.** `ritz.py` uses A = 112.41, 114.82, 84.912, 87.906 with R_M = R∞/(1 + 1/(A·m_p/m_e)).
  This treats the core mass as A proton masses (A-16: the factor is m_p/m_e = 1836.15, not u/m_e =
  1822.89, and 84.912 / 87.906 are the ⁸⁵Rb / ⁸⁸Sr isotope masses, not atomic weights); the paper now
  says exactly that in D1 and §3 and prints the four R_M values so the reader can substitute. No R_M
  was recomputed — the numbers did not move to fit a sentence. The effect of the convention on δ is
  parts in 10⁷ and on ρ nil at the printed precision.
- **The Ritz denominator.** The instrument fits δ₂/(n − δ₀)²; Seaton's relation is for the
  coefficient of n⁻² (or n*⁻²). Lemma 3 records the identity and the paper prints the 1/n² refit
  (1.175 / 0.221 and −0.040 / 0.547) beside the headline figures.
- **"Holds to 15%".** Read as |median ρ − 1| = 0.150; the individual departures 10%, 15%, 56% are
  printed.
- **Series labels.** The paper names the term of each series from the capture files (Cd I ³S₁,
  ¹P°₁, ³D₁, ³F°₃; In I ²S, ²D₃/₂, ²F°; Rb I ²S, ²P°₁/₂, ²D₃/₂; Sr II ²S, ²D₃/₂, ²F°). Sr II nf mixes
  J = 5/2 and 7/2 members and In I nf lists both J at the same energy; the fine structure is below the
  precision the fit sees.
- **In I nd** has rms 0.01755, twelve times the next largest (0.00141), and a defect rising
  monotonically from 2.18 at n = 5 to 2.31 at n = 10; the paper names it in §5 as a probable perturbed
  series and notes it is in the penetrating class, so it does not touch the p = 0 figure. Both figures
  are now `check.py` obligations.
- **A sixth status word.** PAPER-SPEC §5 lists five (PROVED, MACHINE-CHECKED, EXHAUSTIVE, SAMPLED,
  CITED, REFUTATION). The paper declares and uses **MEASURED** for a number computed from the cited
  data by a stated procedure, as `03-bracket/PAPER.md` does, and states in §6 that **no claim in it is
  SAMPLED**. The five spec words are never merged with it or with each other.
- **The field-shift bullet.** Physics Compendium 46–50 gives n*⁷ for a magnetic field, which *"needs
  tens of tesla"*, and n*¹⁰ for an electric field, which *"begins at n > 60"*. The audit (A-9) found
  the two numbers printed with no check and no citation; the paper now keeps only the two powers and
  cites Gallagher 1994 for Rydberg atoms in fields.

## Figures

Regenerated in the repair pass (A-11): true minus signs in every annotation; the p ≥ 1 label of
Figure 1(b) moved below its band at the right edge, clear of the In I d and Rb I p markers; the row
labels of Figure 2 moved to the right edge of each row, clear of the ρ = 0 and ρ = 1 lines; panel
(b)'s title shortened because it was clipped at the panel edge; the legend and line labels no longer
say "Seaton". No plotted value changed. `FIGURES.tsv` carries the new md5s.

All three computed by `figures.py` from `check.py`'s `run_fits()`/`stats()`; no audited plate in
`method/PROOF-FIGURES.tsv` shows Seaton's ratio (the only hit, figure 26.1, is the ν-cost plate).
`FIGURES.tsv` carries each file's md5 and is regenerated with the figures, never by hand.

Each figure was read against its caption and against `check.py`'s own table. Figures 1 and 2 were
**redrawn** in the finishing pass for two layout faults, neither of which touched a number:
Figure 2's one-sd bands were positioned with `axvspan`'s `ymin`/`ymax`, which are axes fractions and
not data coordinates, so both bands sat about 0.65 of a row above the points they belonged to; and
Figure 1(b)'s three p = 0 labels overlapped the median bar, with "Sr II f" clipped by the axis. The
plotted values, the medians and the band widths are unchanged and come from `stats()`. Figure 3 was
not changed. The three captions were checked number by number: 1.150, 0.206, −0.015, 0.177, nine
series with ℓ ≥ 1, thirteen in all, and 15% / 10% / 56% for the three p = 0 series in the panel order
drawn — every one of them a line of `check.py`'s output.


## Settled 2026-09-24, second pass (the remaining open points)

- **The implied polarisabilities are now compared with published values (§5.7)**, read through the alphaXiv connector, which serves arXiv texts the proxy does not: Cd⁺ 25.2(6) a₀³ (Li, Yu and Sahoo 2018, Table VI, CCSD + experiment); In⁺ 24.33 a₀³ at 0.62% (Yu et al. 2015, Table I, final) beside the 24.01 of Safronova et al. quoted there; Sr²⁺ 5.813 (RRPA) and 5.792 (RCCSDT) from Mitroy, Safronova and Clark 2010, Table IV, which also lists Rb⁺ at 9.076 (RRPA), 9.11(4) (RCCSDT) and 9.0 (spectral analysis). The implied 24.76, 26.20 and 10.21 come out at 0.98, 1.08 and 1.76 of the published values; under 3/K every ratio would be at least 1.96. The check carries the arithmetic as a MEASURED obligation.
- **The Rb fits are calibrated against the published coefficients (R-17, formerly declined)**: Li et al. 2003's ⁸⁵Rb values as tabulated in Mack et al. 2011, Table I (read through alphaXiv; Mack's own ⁸⁷Rb values beside them). δ₀ agrees to 4 × 10⁻⁴ (s) and 2–4 × 10⁻³ (d); δ₂ differs by 11% and 23%, as a two-term fit over n ≤ 12 must against fits over n ≥ 19. A MEASURED obligation. The np coefficients were not compared: Li et al.'s paper itself could not be read, and Mack's table carries s and d only.
- **Author initials**: filled from the publishers' records found by search — Bethe, H. A. and Salpeter, E. E.; Born, M. and Heisenberg, W.; Mayer, J. E. and Goeppert Mayer, M.; Seaton, M. J.; Theodosiou, C. E., Inokuti, M. and Manson, S. T., with that paper's title, "Quantum defect values for positive atomic ions".
- **Seaton 1958 itself** is still unread — the ADS scan did not come through the connector — and nothing in the paper rests on it; the search index's summary of the paper says it treats the polarisation potential −α⟨r⁻⁴⟩/2 and the defect it produces, which is consistent with the attribution the paper does not make. Closed.
- **The 1.25 on fourteen channels**: closed as not reconstructible. The store's only occurrences of the phrase are the sentence itself, its generator, and two unrelated instruments that happen to run fourteen channels; the channel index the paper draws on carries one defect per channel and no δ₂, so the ratio cannot be re-measured on it.
- **The two discrepancies of the record** (a limit marked fitted that the record says is published; a mean where the convention says median) stay recorded above and not repaired.
