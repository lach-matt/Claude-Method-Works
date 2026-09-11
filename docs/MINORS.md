# `tools/minors.py` — the seven minors, settled

> **Corrected 2026-09-11.** Figures in this file computed before the load-shape correction (`docs/LOADSHAPE.md`)
> are superseded: the reconstructed load had its seasonal term inverted. The instrument's current output is
> authoritative; the corrected headline figures are in `docs/LOADSHAPE.md` and `CLAUDE.md`.

**Why it exists.** After the majors pass, seven rows of `proposals/FLAWS.tsv` remained, all
`MINOR` — wording, citation, and figures that descend from a figure already corrected. A minor is
not closed by agreeing it is minor: each is settled the way the register asks, computed where it
is numerical (CO₂, jobs, noise, the seismic margin) and stated as a named mechanism where it is not
(the Authority, the procurement structure, the cycle's label). Every computed row prints mid and
critical, by the author's standing rule — simulate critical, not optimal.

**Run it.** `python3 tools/minors.py` prints the report; `--selftest` pins every figure below.
Stdlib only; it imports `cspchain.py` (the cycle and the block) and `hourly3.py` (served energy)
and copies nothing.

## What is settled

- **F-32 — the cycle's label.** Helios-3's cycle is **sCO₂ recompression Brayton at 715 °C, 0.50**
  (`cspchain.py`); the nitrate-salt fallback is **subcritical reheat steam** — ~540 °C live steam
  from 565 °C salt — at **0.43**. Supercritical steam needs ≥ 600 °C live steam, which 565 °C salt
  cannot give. *Supercritical Rankine* is withdrawn; the efficiencies were right and the label
  was wrong.
- **F-33 — seismic.** Seismic zones left the California Building Code in 2001; the design basis is
  site-specific under ASCE 7 (site class, mapped MCE_R). The **0.75 g** target is kept and lies
  above the mapped PGA at every node: Mojave 0.45 / 0.50 g (target 1.67× / 1.50×), Imperial
  0.35 / 0.45 g (2.14× / 1.67×), Central Valley 0.40 / 0.55 g (1.88× / 1.36×), mid / critical.
  The mapped values are **ASSUMED** from the USGS hazard record and the site study fixes them;
  what the selftest pins is that the target clears every one.
- **F-34 — CO₂ avoided.** Recomputed from `hourly3.py`'s served energy at a CAISO marginal
  emissions factor of **0.40 / 0.35 t/MWh** (mid / critical — the critical case is the *lower*
  factor, because a cleaner grid credits the plant less):

  | | mid | critical |
  |---|---|---|
  | served as sized, TWh | 15.19 | 15.12 |
  | avoided as sized, MMT/yr | **6.08** | **5.29** |
  | served closed, TWh | 18.11 | 18.11 |
  | avoided closed, MMT/yr | **7.24** | **6.34** |

  v0.1 claimed 11.8 MMT. The honest figure is 5.3–7.2.
- **F-37 — the Authority.** *Sovereign authority* named no mechanism. The Authority is a
  statutory public entity created by the Act on the pattern of the California Consumer Power and
  Conservation Financing Authority (SB 6X, 2001), which existed and was defunded by 2004 — a
  history the Act acknowledges rather than repeats — and is registered as a load-serving entity in
  CCA form (F-10). Gov. Code §8571 is cited only for what it does, suspend regulatory statutes
  during a declared emergency; it issues no coastal permit and shortens no NEPA review (F-15,
  F-25). *Sovereign* is a description, not a power.
- **F-38 — jobs.** From built plants per MW rather than asserted — Crescent Dunes ~45 permanent
  on 110 MW (0.41/MW), Ivanpah ~90 on 392 MW (0.23/MW), and Ivanpah's 2,100 construction peak on
  392 MW:

  | | mid | critical |
  |---|---|---|
  | block at ×1.5, MW | 3,930 | 3,930 |
  | permanent, Title I | **1,901** | **1,214** |
  | construction peak, Title I | 21,054 | 21,054 |
  | permanent, Title II (water route) | 1,313 | 1,410 |

  v0.1's 22,500 construction and 1,350 permanent were the right order of magnitude; the $4.2 B
  multiplier is unsourced and is not carried.
- **F-39 — procurement.** *Turnkey EPC* is replaced by a structure: one EPC per node under an
  owner's engineer across the program, with the pilot aperture and the first 100 MWe module let as
  separate contracts — because no contractor has delivered more than one commercial tower at a time
  in the US, and the ladder (`helios3.py` R-12) buys the hours before the fleet.
- **F-40 — noise.** RO high-pressure pumps at **90 / 100 dBA** at 1 m reach 40 dBA at
  **316 / 1,000 m** in the open; a full enclosure of **28 / 22 dB** brings the boundary to
  **13 / 79 m**, inside the brownfield F-27 assumes, at **$19 / $58 M per module**, mid / critical.
  The cost is carried in the Title II module's band; *quieter than a library* is withdrawn as a
  comparison.

## Status

Seven rows move to RESOLVED. **Forty of forty are resolved.** The three v0.2 documents
(`proposals/Title_I_Helios-3_v0.2.md`, `Title_II_Aqua-Sovereign_v0.2.md`,
`Title_III_Joinder_v0.2.md`) are the program as it stands; the minors' figures are folded
into the documents by `rebase.py` (Title I §2 for the cycle label and a new §8 for CO₂, employment,
seismic, procurement and the Authority) and `rebase2.py` (Title II §3 for noise, employment and the
Authority), read from this instrument at render time.
Nothing in `FLAWS.tsv` is deleted, and the resolution column names the instrument and the date.
