# One light ray, two readings (M-RULINGS item 122 (2); deduced, computed and READ; verified once; not seated; 2026-10-06)

*First headed* "(… not verified; not seated; 2026-10-06)".

## What M said

- Asked about the candidate H-UMBILIC-GEODESIC (COIN.md point 5), *"OPEN until it is computed and READ"*: **"read
  then compute"** (item 122).
  - That reading of item 122 is the board's: your four answers are read against the coin report's numbering.
- **Item 123:** *"forget the coin metaphor. It served its intended purpose already."* What it described stays yours.
  Item 120: *"the NEC only ever appears to break, but never does"* (H-NEC-NEVER-VIOLATED).

Every number is printed by `umbilic.py`.
- **Selftest:** 3/3 checks, 1 genuine control, with 7 STRUCTURAL lines printed and not counted. It takes about 15
  seconds.
  - *First written:* "6/6 checks, 2 genuine controls and 1 contrast". Three of those held by construction, and one
    half-check compared a typed-in 0 (History).
- **Imported, not rebuilt:**
  - `closedbulk.py`, for the bulk;
  - `pairing.py`, for the five-dimensional Ricci tensor;
  - `coin.py`, for the plane's integral;
  - `escape.py`, for S3.

## Read

- **Youm, "Null Geodesics in Brane World Universe", hep-th/0110013v2.** The route was Firecrawl's PDF reader; arXiv
  itself is refused here. Page numbers are from the verifier's alphaXiv full text.
- **§2 eq. (7), p.2**, for his metric ds² = −n²dt² + a²γdx² + dy². That metric is cosmological, not the board's static
  one.
  - It is the y-component of the bulk geodesic equation.
  - In the board's convention (K = ½∂_y g, so Γ^y_μν = −K_μν), its term for a ray along a plane is −K_kk. That form is
    the board's translation, and it is standard.
- **§1, p.1:** *"gravitons are assumed to propagate freely in the bulk, whereas all the matter fields are assumed to be
  confined on the brane"*.
- **§2, p.4:** a ray off a plane *"is observed on the hypersurface to be the timelike motion under the additional
  influence of extra non-gravitational force"*. That is for a generic surface y = y₀.
  - **At the plane, with the mirror (H-Z2), eqs. (21, 22) p.5:** *"the null bulk geodesic motion is observed on the
    three-brane as the timelike geodesic motion"*.
  - The extra force appears only *"if the brane universe does not possess the Z2 symmetry"* (abstract).
  - *First written* with only the p.4 sentence. That is the opposite case from the one the board assumes.

## What passes

- **U1. The plane's light rays are light rays of the bulk (STRUCTURAL).**
  - Γ^y_kk = −K_kk = a q_kk = 0. This follows from the input K = −a q (escape.py S3) and k being light-like. sympy only
    confirms the code reads it.
  - The ray has one affine parameter in both readings.
  - It holds for every light-like direction along the plane.
  - At the horizons it holds by the tensor identity. The coordinate computation is singular at r = 2m.
  - *First written* as a counted computation, with a control that tested only the code.
- **U2. Along that ray, the bulk reads 0 and the plane reads the corridor.**
  - R⁽⁵⁾_kk = 0 on the plane holds **by construction**: the bulk's first solved equations set it (STRUCTURAL).
    - *First written:* "which closedbulk.py's constraint checks defend". That named the wrong defence.
  - **What is computed:** the bulk's Weyl reading along the ray, E_kk = R⁽⁵⁾_{kyky}, from the series' own Riemann
    tensor.
    - It equals **−G_kk exactly**.
    - So the plane's reading R⁽⁴⁾_kk = −E_kk = G_kk is the bulk's projected Weyl curvature. That is the
      Shiromizu–Maeda–Sasaki split with τ = 0; escape.py S3: *"E = -G carries the whole reading"*.
    - **Control:** a mis-stated y² coefficient gives E_kk + G_kk = δr/(r − 2m) ≠ 0.
  - Integrated along the whole passage (m = 1, r₀ = 1.8):

    | reading | ∫ along the ray (E/m) |
    |---|---|
    | the plane, G_kk | **−1.914712** |
    | the bulk, R⁽⁵⁾_kk | **0**, derived from R⁽⁵⁾_kk = 0 |

    *First written* with the bulk's 0 typed in, not derived.
  - The mirror plane's own sheet of energy is proportional to S = −σq, and q_kk = 0 keeps it out of this ray.
- **U3. Light near the plane is drawn back to it; matter is pushed off it (STRUCTURAL; it follows from U2).** This was
  the verifier's finding.
  - A ray displaced off the plane drifts as D²ξ^y/dλ² = −R_{kyky}ξ^y = +G_kk ξ^y.
  - G_kk is negative on the whole corridor, so the ray is pulled back. **The plane's "broken" reading is the bulk
    focusing light onto the plane** (the board's reading).
  - A massive body at rest (outside r = 2m) is pushed away from the plane on either side: d²y/dτ² = +a.
    - With the mirror, the plane is an unstable balance point for matter. Staying there needs the confinement Youm
      assumes.
    - *First written:* "matter on the plane is not on a bulk geodesic". That was true only on one side.

## With your item 122

- **(3) Your two sides are P1's black-hole horizon and P2's white-hole horizon** (H-SIDES-AS-HORIZON-PAIR). The ray of
  U1 runs from one side to the other. On the plane it reads −1.914712 E/m, and in the bulk 0.
- **(4) "The er=epr only apply to physical matter. The rules apply, but do not restrict information"**
  (H-ER=EPR-MATTER-ONLY, H-RULES-NOT-INFORMATION).
  - U1 and U3 separate light-like paths from massive ones.
  - Youm's confinement covers *"all the matter fields"*, light included.
  - Whether this bears on your (4) is not computed.
  - *First written:* "U1's contrast is the board's nearest computed fact". That over-reached.
- **(1) "likely yes", a five-dimensional censorship theorem** (H-5D-CENSORSHIP, your expectation; no such theorem READ).
  - In a bulk of vacuum energy, R⁽⁵⁾_kk = 0 for every light-like direction at every point off the planes. That includes
    rays that leave the plane.
  - So the averaged condition can fail only at a plane.
  - Standard, NOT READ: a ray crossing our plane (τ = 0, positive tension) picks up a positive contribution there.
  - Where such a theorem would require the failure to sit is the board's open question. "Must fail somewhere" is the
    board's reading of a theorem no one has READ.

## Scope

- **U1–U3 use only the exact local data at the plane:** the y⁰, y¹ and y² terms; τ = 0; K = −a q; H-VACUUM-BULK; H-Z2.
  They do not depend on how far the series converges (H-NEAR-PLANE).
  - *First written:* "The scope is closedbulk.py's … H-NEAR-PLANE". That drew it too narrowly.
- **Only the −1.914712 is specific to radial rays.**

## Named hypotheses

- **Yours:** H-NEC-NEVER-VIOLATED (117, 120, 123); H-SIDES-AS-HORIZON-PAIR, H-ER=EPR-MATTER-ONLY,
  H-RULES-NOT-INFORMATION, H-5D-CENSORSHIP (122, read against the coin report's numbering, which is the board's reading).
- **The board's:** closedbulk.py's H-VACUUM-BULK and H-Z2; H-BK-CORRIDOR; H-RS1; H-PLANE-READING;
  H-UMBILIC-GEODESIC, now computed.

## Sources READ

| source | route | used |
|---|---|---|
| Youm, hep-th/0110013v2 | Firecrawl (PDF, pp.1–6 of 11); pages by the verifier (alphaXiv) | §1 p.1; eq. (7) p.2; p.4; eqs. (21, 22) p.5; abstract |
| escape.py S3 (seated) | the board | E = −G |

## OPEN

1. The paths of rays that leave the plane, and their crossings of other planes. What the bulk reads along them away
   from the planes is already 0.
2. A five-dimensional censorship theorem (your H-5D-CENSORSHIP), and where it would place a failure.

## History (verifier, 2026-10-06)

Twelve findings were applied:

- U1 and R⁽⁵⁾_kk = 0 hold by construction.
- The bulk's 0 was typed in. It is replaced by the genuine E_kk = −G_kk computation.
- Youm's mirror-symmetric result was added, with pages.
- The massive-observer wording was one-sided.
- Light is drawn back to the plane.
- The scope was too narrow.
- The censorship note was added.
- The Youm attribution in COIN.md was corrected.
- The (4) link over-reached.
- The numbering is now marked as the board's reading.
- Minor signs and wording were fixed.

When I first coded E_kk, I lowered its index with the metric before setting y = 0, and the check failed. It passes once
both are evaluated at the plane.
