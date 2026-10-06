# One light ray, two readings (M-RULINGS item 122 (2); deduced, computed and READ; not verified; not seated; 2026-10-06)

## What M said

- Asked about the candidate H-UMBILIC-GEODESIC (COIN.md point 5), *"OPEN until it is computed and READ"*: **"read
  then compute"** (item 122).

Every number is printed by `umbilic.py`.
- **Selftest:** 6/6 checks, 2 genuine controls and 1 contrast, with 4 STRUCTURAL lines printed and not counted. It
  takes about 15 seconds.
- **Imported, not rebuilt:**
  - `closedbulk.py`, for the bulk;
  - `pairing.py`, for the five-dimensional Ricci tensor;
  - `coin.py`, for the plane's integral;
  - `escape.py`, for S3.

## Read

- **Youm, "Null Geodesics in Brane World Universe", hep-th/0110013v2** (Firecrawl, PDF; arXiv itself is refused by this
  environment's proxy).
  - **§2, eq. (7):** the y-component of the bulk geodesic equation, *d²y/dλ² + n n′(dt/dλ)² − a a′ Σ(dx^j/dλ)² = 0*,
    in coordinates with dy² in the metric.
    - For a ray running along the plane (dy/dλ = 0), its force term is −½∂_y g_μν k^μ k^ν. In this board's convention
      (K = ½∂_y g) that is −K_kk.
    - So a light ray of the plane stays a light ray of the bulk exactly when K_kk = 0. An umbilic plane (K ∝ q) gives
      K_kk = 0 for every light-like direction.
  - **§1:** *"gravitons are assumed to propagate freely in the bulk, whereas all the matter fields are assumed to be
    confined on the brane"*.
  - **§2:** a ray that does leave the plane *"is observed on the hypersurface to be the timelike motion under the
    additional influence of extra non-gravitational force"*.

## What passes

- **U1. The corridor's light rays are light rays of the bulk.**
  - On closedbulk.py's bulk, the bulk's force on the plane's radial light ray is Γ^y_kk = **0 at every radius** (sympy,
    from the full five-dimensional Christoffel symbols). That covers the throat and both horizons.
  - The ray has one affine parameter in both readings, because the plane's metric is the bulk's metric restricted to
    y = 0 (STRUCTURAL).
  - **Control:** a non-umbilic plane, with B's first term −2b B₀ and b ≠ a, pushes the ray off: Γ^y_kk = −r(a − b)/(r − 2m).
  - **Contrast:** a static massive observer on the plane has Γ^y_tt u u = −a ≠ 0.
    - Matter on the plane is not on a bulk geodesic. Its place on the plane is confinement, not free fall.
    - Youm *assumes* this confinement (§1). It is not derived here.
- **U2. Along that one ray, the condition is broken in the plane's reading and kept in the bulk.**
  - R⁽⁵⁾_kk = **0** identically on the plane, along the ray (sympy, from the series bulk's Ricci tensor). The plane
    reads G_kk (coin.py C1).
  - Integrated along the whole passage (m = 1, r₀ = 1.8):

    | reading | ∫ along the ray (E/m) |
    |---|---|
    | the plane, G_kk | **−1.914712** |
    | the bulk, R⁽⁵⁾_kk | **0** (saturated, not broken) |

  - **Control:** a mis-stated y² coefficient (A₂ + δA₀) makes R⁽⁵⁾_kk = δr/(r − 2m) ≠ 0.
  - The difference between the two readings is the bulk's projected Weyl term: E_kk = −G_kk. In escape.py S3's words,
    *"E = -G carries the whole reading"*.

**So H-UMBILIC-GEODESIC is computed.** On one curve, with one affine parameter, the condition appears broken from the
plane and is not broken in the bulk. That is your coin's *"appears broken, but is not"*, on a single ray of the
corridor.

## With your item 122

- **(3) Your two sides are P1's black-hole horizon and P2's white-hole horizon** (H-SIDES-AS-HORIZON-PAIR). The ray of
  U1 is the coin turning: it runs from one side to the other.
  - On the plane it reads −1.914712 E/m. In the bulk it reads 0.
- **(4) "The er=epr only apply to physical matter. The rules apply, but do not restrict information"**
  (H-ER=EPR-MATTER-ONLY, H-RULES-NOT-INFORMATION). U1's contrast is the board's nearest computed fact: on this bulk,
  light rays along the plane are free geodesics of the bulk, while matter is not.
  - Whether information rides the light rays is your hypothesis, not computed.

## The boundary (item 82)

- **The scope is closedbulk.py's.** It covers the bulk near the plane (H-NEAR-PLANE), a vacuum bulk, and H-RS1.
- **U2 is a statement about one family of rays** (radial, along the plane). Rays that leave the plane are Youm's
  §2 case, and are not computed here.
- **closedbulk.py's B3 still stands under the compact reading.** The second plane's matter carries ANEC < 0 at leading
  order. U2 says nothing about that plane.
- **(1) "likely yes", a five-dimensional censorship theorem** (H-5D-CENSORSHIP, your expectation; no such theorem READ).
  - If it binds the closed bulk, the averaged condition must fail somewhere in the five-dimensional spacetime for the
    passage to exist.
  - U2 shows it does not fail along the plane's rays in the bulk. B3 puts a failure on the second plane.
  - Whether that placement is what such a theorem requires is OPEN.

## Named hypotheses

- **Yours:** H-NEC-COIN (117; a metaphor, 120); H-SIDES-AS-HORIZON-PAIR, H-ER=EPR-MATTER-ONLY, H-RULES-NOT-INFORMATION,
  H-5D-CENSORSHIP (122).
- **The board's:**
  - closedbulk.py's H-VACUUM-BULK, H-Z2, H-NEAR-PLANE;
  - H-BK-CORRIDOR; H-RS1; H-PLANE-READING;
  - H-UMBILIC-GEODESIC, now computed within that scope.

## Sources READ

| source | route | used |
|---|---|---|
| Youm, hep-th/0110013v2 | Firecrawl (PDF, pp.1–6 of 11) | §1 the confinement assumption; §2 eq. (7); the extra force on rays leaving the plane |
| escape.py S3 (seated) | the board | E = −G |

## OPEN

1. Rays that leave the plane, and what the bulk reads along them (Youm §2).
2. A five-dimensional censorship theorem (your H-5D-CENSORSHIP), and whether B3's placement is what it requires.
3. Whether the closed bulk's second plane is position 2's, and what it may carry (closedbulk.py, still asked).
