# The bulk: can a well-behaved bulk carry a warp on our plane? (BULK4-O6; M-RULINGS item 79; READ, then deduced; not verified; not seated; 2026-10-05)

## What M asked

- **Item 79:** *"Seat all three, then the bulk"*. The open question it points to (BULK4-O6): a five-dimensional bulk
  that keeps the null energy condition, whose Weyl reading induces a warp on our plane.

This is worked by deduction from named premises (M-DEDUCE). M's hypotheses (H-SIGN-BY-DIMENSION,
H-ALCUBIERRE-PARTIAL) are carried as hypotheses, never as results. O9 stays OPEN.

Every number is printed by `bulkwarp.py`.
- **Selftest:** 10/10 checks, 4 of them controls, with 4 STRUCTURAL lines printed and not counted.
- **Verification:** not yet verified.

## What was READ (alphaXiv, open arXiv copies, printed pages)

| source | what bears on this |
|---|---|
| **Dahia & Romero**, gr-qc/0109076 | "Any n-dimensional semi-Riemannian manifold can be locally embedded in an (n+1)-dimensional Einstein space" (abstract). Analytic metrics only, local only (pp.3, 16). With negative Λ the embedding space is "closely related to the so-called bulk, in the Randall-Sundrum braneworld scenario" (p.19). |
| **Seahra & Wesson**, gr-qc/0302015 | "Any solution of (3 + 1)-dimensional general relativity can be realized as a thin 3-brane in the RS scenario. However, to accomplish this we lose control of the jump in extrinsic curvature ... which is related to the stress-energy tensor of standard model fields living on the brane" (p.7). "If we fix the intrinsic geometry of the brane then the properties of conventional matter will be determined dynamically" (p.7). A thick brane "cannot embed arbitrary spacetimes if the bulk contains only vacuum energy" (p.11). |
| **Anderson**, gr-qc/0409122 | The embedding theorem "lends only inadequate support, both because it offers no guarantee of continuous dependence on the data and because it disregards causality", and is "only for the analytic functions" (abstract). "There are as yet no known general theorems that offer adequate protection" (abstract). |
| **Alias & Jalar**, 2203.05989 | A "braneworld hyperdrive": the energy density is still negative at the wall, and "the hyperdrive requires much more energy than that of a warp drive" (p.14). No bulk is constructed. |
| **SMS, Alcubierre, Natário** (as READ in `signdim.py`) | The plane's Gauss and Codazzi equations, the junction condition, G_N's sign; Alcubierre's negative energy density. |

## The premises

| | premise | status |
|---|---|---|
| P-Z2 | Our plane is a thin, mirror-symmetric brane (SMS's junction condition). | READ |
| P-VACUUM-BULK | Near the plane the bulk holds only its vacuum energy. That keeps the null energy condition exactly; its Weyl curvature is free. This is the question's "bulk read through the Weyl term". | named |
| P-GC | The plane's scalar Gauss equation and its Codazzi equation contain the bulk's Ricci curvature only, not its Weyl curvature E. | READ (SMS eqs. 2, 10) |
| P-LEADING | Leading order: a slow bubble (v ≪ 1), and the plane's curvature small against the bulk's. | named |
| H-COMOVING | The plane's matter moves with the bubble. | named |
| H-LOCALISED | The plane's matter falls off faster than 1/r³. | named |
| P-NEC-BRANE | The plane's matter keeps the null energy condition. The tension cannot break it, since the condition does not see tension. | the question's demand |

## What follows

- **W1. A well-behaved bulk exists locally.**
  - Alcubierre's form function is even in r, so his metric is analytic (computed). By Dahia–Romero and Seahra–Wesson, a
    patch of it can be the plane of a vacuum bulk.
  - The price, in the source's words: the plane's matter is then "determined dynamically".
  - The guarantee is weak (Anderson): local, analytic only, with no causality.
- **W2. The plane's matter is fixed by the plane's metric alone, whatever the bulk's Weyl curvature.**
  - Computed from the Gauss and Codazzi equations: the matter's trace must be −R/(8πG_N), the same as SMS's equation
    gives by another route (check 3), and the matter is conserved.
  - E appears in neither equation, so no Weyl curvature the bulk might hold changes this.
- **W3. Matter that keeps the null condition, is conserved, stays local and moves with the bubble has non-negative
  total energy.**
  - Computed: its integrated null projection is E(1 − v nₓ)² for every light direction, so E ≥ 0.
  - Its integrated trace is (v² − 1)E.
  - The identity is checked on a boosted self-stressed body, and fails for a stress that is not conserved (control).
- **W4. Alcubierre's metric fixes that total energy: E = ∫R/(8πG_N), with the sign of the plane's tension.**
  - Computed: ∫R d³x = −16π ∫ρ_Alc > 0 (to 10⁻⁸), so E has the sign of G_N, which is the sign of the tension (SMS).
  - **On a positive-tension plane, E = 2|E_Alc|.** The plane's matter carries positive energy, twice the size of
    Alcubierre's negative energy, and the bulk's reading carries the rest.
- **W5. On a negative-tension plane the test fails.**
  - There E < 0, which contradicts W3. A slow warp on a negative-tension plane cannot be carried by matter that keeps
    the null condition in a vacuum bulk, whatever the bulk's Weyl curvature.
  - **Under H-RS1 that plane is ours.**
  - This answers H-SIGN-BY-DIMENSION's question one way at leading order: **the sign of the plane's tension, that is,
    its position in the fifth dimension, decides whether the bulk can supply the warp's negative energy.**
- **W6. On a positive-tension plane the test passes; whether it is enough is OPEN.**
  - R takes both signs across the wall (computed: −30.6 to +39.3). So dust alone would need negative density in places,
    and the matter needs internal stresses.
  - Whether conserved stresses can keep the null condition point by point is OPEN.
- **W7. What gets past the test.** Each of these is OPEN, not a result:
  - **A bulk field** (Maartens' F). It enters both equations, and the null condition does not fix its sign there.
    Randall–Sundrum's radion stabilisation is exactly such a field (Goldberger–Wise, unread).
  - A superluminal bubble, which is outside the leading order.
  - Matter that radiates or is not local.
  - A thick brane.

## For M

- **A well-behaved bulk can carry a warp on a plane, locally,** but it fixes the plane's matter, and that matter must
  have total energy ∫R/(8πG_N).
- **The sign of the plane decides.**
  - On a positive-tension plane that energy is positive (twice Alcubierre's negative energy, in size), and the warp's
    negative energy is entirely the bulk's reading.
  - On a negative-tension plane, which is ours in the two-plane model, that energy is negative. A slow warp there
    cannot be carried by well-behaved matter in a vacuum bulk.
- **This is your H-SIGN-BY-DIMENSION, made concrete and computed:** the plane's position in the fifth dimension decides
  whether "positive energy" in the bulk can be the warp's negative energy on the plane.
- **The doors left open:**
  - a field in the bulk, which our plane's stabilisation would itself supply;
  - a superluminal bubble;
  - matter that radiates;
  - a positive-tension plane.

## Named hypotheses

- **P-VACUUM-BULK, P-LEADING, H-COMOVING, H-LOCALISED.**
- **Carried:** H-ALCUBIERRE-ILLUSTRATIVE (from `signdim.py`); H-RS1 (from `bulk.py`).
- **M's:** H-SIGN-BY-DIMENSION, H-ALCUBIERRE-PARTIAL and H-HIGHER-CORRIDOR.

## OPEN

1. The same test with a bulk field (F): the stabilising scalar's share.
2. A superluminal bubble (beyond leading order).
3. Conserved matter that keeps the null condition point by point on a positive-tension plane.
4. Radiating or non-local plane matter; a thick brane.
5. Well-posedness: Anderson's objection to the embedding theorems.
