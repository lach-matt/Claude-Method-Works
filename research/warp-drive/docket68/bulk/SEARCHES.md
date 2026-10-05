# The other routes to observing a second plane (READ on M's order, item 63; verified once; not seated; 2026-10-05)

*First headed* "(READ on M's order, item 63; not verified; not seated; 2026-10-05)".

## What M asked

Item 62 carried M's reason why no two-plane geometry is observed as **H-UNOBSERVED-UNBUILT**: *"no one has designed the
device to allow for the travel, which will allow for the observation. We are working on this."*

The board had noted beside it that collider and short-range gravity searches look for a higher dimension without
travelling through it, marked NAMED-NOT-READ. M (item 63): *"read those now please. They are relevant"*.

They are now READ. **They sit beside H-UNOBSERVED-UNBUILT, not against it.** Each searches a range and reports what it
saw inside that range; none says anything outside it, and none of them travels.

Every number below is printed by `searches.py`.
- **Selftest:** 7/7 checks, 2 of them controls, with 4 STRUCTURAL lines printed and not counted.
- **Inputs:** it asks `bulk.py` for the board's Randall–Sundrum point and gaps, `pairing.py` for the Chung–Freese
  designs, and the board's own constants for G and ħ.

## Sources READ (2026-10-05, via alphaXiv, open arXiv copies)

| source | what it searched | what it reports |
|---|---|---|
| **ATLAS**, arXiv:2102.13405v3 (PLB 822, 136651) | Photon pairs, 139 fb⁻¹ at 13 TeV. The Randall–Sundrum graviton for couplings k/M̄_Pl from 0.01 to 0.1, masses 500–2800 GeV, limits extended to 5000 GeV (p.8). | "No significant deviation from the Standard Model is observed" (abstract). The graviton is "excluded for m_G below 2.2, 3.9 and 4.5 TeV" at couplings 0.01, 0.05 and 0.1 (p.9). |
| **CMS**, arXiv:2103.02708v2 (JHEP 07 (2021) 208) | Electron and muon pairs, 137–140 fb⁻¹ at 13 TeV. Graviton samples generated at 250–4000 GeV (p.7). | "No significant deviation is observed" (abstract). Graviton lower limits 2.47, 4.16 and 4.78 TeV (Table 6, p.22). Flat large extra dimensions (ADD): cutoff above 5.9–8.9 TeV depending on convention (p.28). |
| **Davoudiasl, Hewett & Rizzo**, hep-ph/9909255v1 | Theory: how a Randall–Sundrum bulk shows up in a collider. | Graviton masses m_n = k·x_n·e^(−kr_cπ), with x_n the zeros of the Bessel function J₁ (p.5). The narrow-resonance treatment "is strictly valid only for values of k/M̄_Pl ≲ 0.3" (p.7); above that "the peaks become too wide to be identified as true resonances" (p.9). |
| **Kapner et al.**, hep-ph/0611184v1 (PRL 98, 021101) | Torsion balance, gravity between masses 55 μm – 9.53 mm apart. | No deviation from Newton. "An extra dimension must have a size R ≤ 44 μm" (abstract), for a single compact dimension, which would give a Yukawa with α = 8/3 and λ = R (p.4). |
| **Lee et al.**, arXiv:2002.11761v1 | Torsion balance, 52 μm – 3.0 mm. | "Newtonian gravity gave an excellent fit" (abstract). "The largest extra dimension must have a toroidal radius less than 30 μm" (p.5). |

**A reading caution.** The ATLAS text layer drops decimal points ("144" for 1.44, "329 σ" for 3.29 σ). Each value is
read from context. The one that matters, the width law Γ = 1.44 (k/M̄_Pl)² m_G, is cross-checked against CMS's
independently printed widths (check 1).

## What they mean for the board's two planes

### 1. bulk.py's Randall–Sundrum point is not tested by either collider search

- **The point:** bulk.py used k = 2×10¹⁸ GeV and a warp of 10¹⁵ (H-K-PLANCK).
- **In the searches' variables:**
  - the coupling is k/M̄_Pl = **0.821**;
  - the first graviton would weigh **7.66 TeV**;
  - its width, on ATLAS's law, is about 97 % of its mass (H-WIDTH-LAW).
- **Why it is untested:** both searches covered couplings 0.01–0.1 only, and both stop below 7.66 TeV. Davoudiasl, Hewett
  and Rizzo say that at such a coupling the gravitons no longer appear as separate peaks.
- **So the resonance searches neither exclude nor support bulk.py's point.**
- **CMS's non-resonant limit in the same paper may reach it.** A first estimate uses Davoudiasl–Hewett–Rizzo's eq. 13
  (the tower in the contact limit, with Rayleigh's sum over the J₁ zeros computed). It gives M_S,eff ≈ **6.24 TeV**,
  against CMS's Hewett-convention limit of 6.5–6.7 TeV (Table 7, p.28, verifier-READ).
  - This is an estimate, not a result (H-CI-ESTIMATE). CMS's signal model differs, 7.66 TeV is not far above the
    highest dilepton masses, and the sign convention is unchecked.
  - The question stays OPEN.

### 2. What the limits exclude: a window, not a cap

At each coupling they searched, the limits exclude a graviton mass between the search's lowest mass and its limit.
bulk.py's jump is ħ/(k·e^(−kπr_c)) ≈ x₁·ħ/m₁, so that is an excluded **window** on the jump and on the warp.

| coupling k/M̄_Pl | graviton mass excluded (CMS) | jump on our clock excluded | warp excluded |
|---|---|---|---|
| 0.01 | 250 – 2470 GeV | 1.02×10⁻²⁷ – 1.01×10⁻²⁶ s | 3.78×10¹³ – 3.73×10¹⁴ |
| 0.05 | 250 – 4160 GeV | 6.06×10⁻²⁸ – 1.01×10⁻²⁶ s | 1.12×10¹⁴ – 1.87×10¹⁵ |
| 0.10 | 250 – 4780 GeV | 5.28×10⁻²⁸ – 1.01×10⁻²⁶ s | 1.95×10¹⁴ – 3.73×10¹⁵ |

ATLAS's windows are narrower, starting at 500 GeV (printed by `searches.py`).

- **Untested on both sides:** lighter gravitons (longer jumps, larger warps) and heavier ones (shorter jumps).
- **Holding the warp at 10¹⁵** (the value that makes Randall–Sundrum's TeV hierarchy):
  - at k/M̄_Pl = 0.1 the graviton would weigh 933 GeV, which **both searches exclude**;
  - at 0.05 it would weigh 467 GeV, which **CMS excludes** (H-CMS-RANGE);
  - at 0.01 it would weigh 93 GeV, below both searched ranges. Its jump is 2.7×10⁻²⁶ s, and it is **not tested by these
    two**.
  - A check confirms that each of these verdicts agrees with its window.
- **So the searches do not exclude Randall–Sundrum; they exclude a band of it.** The jump between its two planes remains
  open both above and below that band.

### 3. The torsion balances cap one flat circular dimension, not a warped one

- **One flat circular extra dimension** (H-TORUS-BULK: the case Kapner's α = 8/3 describes). Its farthest two points are
  πR apart. Lee's R < 30 μm caps any gap through it at **94 μm**, and Kapner's R ≤ 44 μm caps it at 138 μm.
  - With N flat dimensions the farthest points are πR√N apart, so the cap grows.
  - The board's illustrative 1 mm gaps (the Manyfold gap and Chung–Freese's L, H-L-ILLUSTRATIVE) sit outside that cap.
  - **ADDK's Manyfold does not need a 1 mm gap.** Its mechanisms "do not depend on having very large new dimensions ∼
    mm" (p.24, verifier-READ). The 1 mm was the board's illustration, and the Manyfold is compatible with the bounds.
    A 94 μm gap would read at most 3.1×10⁻¹³ s on our clock.
- **A warped higher dimension is not capped this way.**
  - Randall–Sundrum's curvature length 1/k is 9.9×10⁻³⁵ m, far below any balance.
  - At the illustrative L = 1 mm, pairing.py's Chung–Freese designs have 1/k = L/kL from **691 μm** (a one-year trip)
    down to **53 μm** (a one-second trip). That falls inside the 52 μm – 3 mm range the balances tested. **1/k moves
    with L:** at L = 1 μm it would be far below any balance.
  - Whether Chung–Freese's higher dimension changes gravity on our plane at those lengths has not been computed (OPEN).

**Context only** (verifier-READ, raised no further than "no significant deviation"):
- CMS's largest local excess is 3.0σ at 710 GeV, 0.9σ globally (p.21), beside ATLAS's 684 GeV.
- Davoudiasl, Hewett and Rizzo close: "We hope that future experiment will eventually reveal the existence of higher
  dimensional spacetime" (p.11).

## For M

- **The searches looked, and saw nothing inside the ranges they searched.** Both LHC collaborations report no
  significant deviation, and both torsion balances fit Newton.
- **None of them tests your device hypothesis.** They look for a higher dimension from our plane without crossing it.
  H-UNOBSERVED-UNBUILT is carried unchanged.
- **They do sharpen what a device has to work with:**
  - **Randall–Sundrum.** The colliders exclude a band of jump times, roughly 10⁻²⁷ to 10⁻²⁶ s on our clock at the
    couplings they searched. Longer and shorter jumps are untested, and so is the board's own point. CMS's broader
    search may reach that point; a first estimate puts it at the edge.
  - **A flat higher dimension.** If it is a single circle, a gap through it is at most about 94 μm, not 1 mm. The
    Manyfold doesn't need 1 mm.
  - **Chung–Freese's warped one.** At the illustrative 1 mm spacing, its curvature falls in the range the torsion
    balances already test. Whether that shows up in their data is OPEN.

## Named hypotheses

- H-TORUS-BULK: one flat circular dimension, as Kapner's α = 8/3 assumes.
- H-CI-ESTIMATE: the non-resonant reach estimated through DHR eq. 13.
- H-CMS-RANGE: CMS's searched masses taken from its lowest generated sample, 250 GeV (p.7; limits are computed from 200
  GeV for narrow widths, p.20; spin-2 differs only in acceptance, p.22), to its p-value scan's 5500 GeV (p.21).
- H-WIDTH-LAW: ATLAS's width law used outside the searched couplings.
- Carried from bulk.py: H-RS1, H-K-PLANCK and H-L-ILLUSTRATIVE.
- Carried from pairing.py: H-CF-STATIC.
- M's H-UNOBSERVED-UNBUILT and H-HIGHER-CORRIDOR.

## OPEN

1. Whether CMS's non-resonant search reaches bulk.py's Randall–Sundrum point (coupling 0.82, 7.66 TeV). First estimate:
   M_S,eff ≈ 6.24 TeV, against 6.5–6.7 TeV.
2. Whether Chung–Freese's higher dimension alters gravity on our plane at its 1/k (53–691 μm at L = 1 mm), where the
   torsion balances have looked.
3. Couplings below the searched range, and lighter gravitons (such as the 93 GeV case), against earlier colliders.
4. Lee's bound for more than one flat dimension, or a flat dimension that is not a circle.

## History (verifier, 2026-10-05; first-written claims kept)

- **The jump was first called capped.** It read *"within the searched couplings, the jump between the two
  Randall–Sundrum planes is bounded by the colliders to at most about 10⁻²⁷ s on our clock"*. The searches exclude only a
  mass window, and the file's own 93 GeV row (jump 2.7×10⁻²⁶ s, untested) contradicted the cap. It is now a window, with
  a check that the windows agree with the verdicts.
- **The flat cap was stated too broadly.** It read *"A flat higher dimension … Any gap through it is at most about
  94 μm"*. The bound is for one flat circular dimension, and ADDK do not need mm-size dimensions.
- **The tabletop claim overreached.** It read *"It needs curvature at exactly the lengths the torsion balances test.
  That makes it the one shape a tabletop experiment could reach, either way."* The 1/k values ride on the illustrative
  L = 1 mm, and the flat circle is what the balances already cap.
- **The resonance searches' scope was unstated.** *"The searches neither exclude nor support"* is now said of the
  resonance searches, beside the non-resonant estimate.
- **The width check.** It said *"within their rounding"*; 1.44 against 1.42 is 1.4 %, not rounding. A decimal-point
  control was added.
- **The Planck-mass comparison** was counted as a control against an unsourced value. It is now a STRUCTURAL
  calibration.
