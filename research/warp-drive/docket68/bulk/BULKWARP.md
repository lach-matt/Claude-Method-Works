# The bulk: can a well-behaved bulk carry a warp on our plane? (BULK4-O6; M-RULINGS item 79; READ, then deduced; verified once; not seated; 2026-10-05)

*First headed* "(BULK4-O6; M-RULINGS item 79; READ, then deduced; not verified; not seated; 2026-10-05)".

## What M asked

- **Item 79:** *"Seat all three, then the bulk"*. The open question it points to (BULK4-O6): a five-dimensional bulk
  that keeps the null energy condition, whose Weyl reading induces a warp on our plane.

This is worked by deduction from named premises (M-DEDUCE). M's hypotheses (H-SIGN-BY-DIMENSION,
H-ALCUBIERRE-PARTIAL) are carried as hypotheses, never as results. O9 stays OPEN.

Every number is printed by `bulkwarp.py`.
- **Selftest:** 9/9 checks, 3 of them controls, with 5 STRUCTURAL lines printed and not counted.
- **Verification:** verified once, with its findings applied (History).

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
| P-GC | The plane's scalar Gauss equation and its Codazzi equation contain the bulk's Ricci curvature only, not its Weyl curvature E. | READ (SMS eq. 1, Gauss; eq. 8's trace, E traceless by eq. 9; eqs. 2, 10, Codazzi) |
| P-LEADING | Leading order: a slow bubble (v ≪ 1), the plane's matter continuous in v, and its density far below the tension. | named |
| H-BOUNDED | The plane's matter keeps bounded second moments in time. *First written* H-COMOVING (it moves with the bubble), which is stronger. | named |
| H-LOCALISED | The plane's matter falls off faster than 1/r³. | named |
| P-NEC-BRANE | The plane's matter keeps the null energy condition. The tension cannot break it, since the condition does not see tension. SMS p.4: normal matter "should satisfy the local energy condition". | the question's demand |

## What follows

- **W1. A well-behaved bulk exists locally.**
  - Alcubierre's form function is even in r, so his metric is analytic (computed). By Dahia–Romero and Seahra–Wesson, a
    patch of it can be the plane of a vacuum bulk.
  - The price, in the source's words: the plane's matter is then "determined dynamically".
  - The guarantee is weak (Anderson): local, analytic only, with no causality. Local patches "generally each belong to
    different possible global data sets", so W1 gives no whole plane; W4–W6 are conditions on whole-plane integrals.
- **W2. The plane's matter is fixed by the plane's metric alone, whatever the bulk's Weyl curvature.**
  - Computed from the Gauss and Codazzi equations: the matter's trace must be −R/(8πG_N), consistent with SMS's
    equation 17 (check 3), and the matter is conserved. E appears in neither equation.
  - The matter has to be small, of order v². A smaller-order part would be static, traceless, conserved, local and keep
    the null condition, and such a tensor vanishes. Alcubierre's order-v curvature, which is non-zero point by point but
    integrates to zero, is carried by E.
  - G_N here is SMS's coefficient, not the measured Newton constant. The relation needs only the matter to be far below
    the tension, not E to be small, so Shiromizu–Koyama's large E on the negative plane does not affect it.
- **W3. Matter that keeps the null condition, is conserved, stays local and stays bounded has non-negative total energy,
  and its integrated trace is minus that energy.**
  - At the working order the matter is static in the bubble's frame, so Laue's identities apply. Matter that is bounded
    but does not move with the bubble satisfies them on time average.
  - The identity is checked on a boosted self-stressed body, and fails for a stress that is not conserved (control).
- **W4. Alcubierre's metric fixes that total energy: E = ∫R/(8πG_N), with the sign of the plane's tension.**
  - Computed: ∫R d³x = −16π ∫ρ_Alc > 0 (to 10⁻⁸), so E has the sign of G_N, which is the sign of the tension (SMS).
  - **On a positive-tension plane, E = 2|E_Alc|** (with E_Alc taken in SMS's G_N): positive, and the Weyl term carries
    −3|E_Alc|.
- **W5. On a negative-tension plane the test fails.**
  - There E < 0, which contradicts W3. A slow warp on a negative-tension plane cannot be carried by matter that keeps
    the null condition in a vacuum bulk, whatever the bulk's Weyl curvature.
  - **Under H-RS1 that plane is ours**, in the two-plane model *without* a stabilising field. That is the configuration
    `signdim.py` S6c already found excluded by observation. With the stabilising field the vacuum-bulk premise fails, and
    W7's first door applies.
  - Under the reading of H-SIGN-BY-DIMENSION as the plane's position (its tension's sign), this answers it one way at
    leading order. The reading is named; the hypothesis stays a hypothesis.
- **W6. On a positive-tension plane the test passes, as a necessary condition only; whether it is enough is OPEN.**
  - R takes both signs across the wall (computed: −30.6 to +39.3 at v_s = 1; R is exactly proportional to v², so the
    pattern does not depend on v). So dust alone would need negative density in places, and the matter needs internal
    stresses.
- **W7. What gets past the test.** Each of these is OPEN, not a result:
  - A bulk field (Maartens' F); the radion's stabilising field is one.
  - A superluminal bubble.
  - Matter whose moments grow without bound (radiation, escaping matter).
  - A thick brane.
  - Not yet READ: an induced-gravity term on the plane (which can flip the trace relation's sign), a Gauss–Bonnet bulk,
    an asymmetric embedding, and a plane density near the tension.
  - **Not doors:** the hidden plane's matter and bulk gravitational waves reach our plane only through E and drop out;
    bounded time-dependent matter (W3).

## For M

- **A well-behaved bulk can carry a warp on a plane, locally,** but it fixes the plane's matter, and that matter must
  have total energy ∫R/(8πG_N).
- **The sign of the plane decides, at the level of totals.**
  - On a positive-tension plane that energy is positive (twice Alcubierre's negative energy, in size). The warp's
    negative energy *would be* the bulk's reading, if such a configuration exists point by point (OPEN).
  - On a negative-tension plane (ours in the two-plane model without a stabilising field) that energy is negative. A
    slow warp there cannot be carried by well-behaved matter in a vacuum bulk.
- **Under the reading of your H-SIGN-BY-DIMENSION as the plane's position,** a positive-tension plane realises it at the
  integrated level: well-behaved matter with positive energy is read on the plane as Alcubierre's negative energy, with
  the bulk's Weyl term supplying the difference. The positive energy is the plane's matter; the bulk supplies curvature.
- **The doors:** a bulk field, a superluminal bubble, radiating matter, a thick brane (item 80: being tested).

## Named hypotheses

- **P-VACUUM-BULK, P-LEADING, H-BOUNDED, H-LOCALISED;** and the reading of H-SIGN-BY-DIMENSION as the plane's tension sign.
- **Carried:** H-ALCUBIERRE-ILLUSTRATIVE (from `signdim.py`); H-RS1 (from `bulk.py`).
- **M's:** H-SIGN-BY-DIMENSION, H-ALCUBIERRE-PARTIAL and H-HIGHER-CORRIDOR.

## OPEN

1. The same test with a bulk field (F): the stabilising scalar's share.
2. A superluminal bubble (beyond leading order).
3. Conserved matter that keeps the null condition point by point on a positive-tension plane.
4. Radiating or non-local plane matter; a thick brane.
5. Well-posedness: Anderson's objection to the embedding theorems.
6. The ratio in measured units under H-RS1: how much of the 4D-inferred negative energy the plane's matter would carry
   (G_obs against SMS's G_N; depends on H-STABILISED or H-UNSTABILISED).
7. Not yet READ: induced gravity, Gauss–Bonnet, asymmetric embedding, plane density near the tension.

## History (verifier, 2026-10-05; first-written claims kept)

- **"The plane's matter can be chosen O(v²)."** A no-go must cover all matter: it *must* be O(v²).
- **"Alcubierre's total G_ty is O(v)."** Only point by point; its integral is zero.
- **W3 used the factors (1 − v nₓ)² and (v² − 1) as working identities.** They exceed the order's accuracy; the static
  Laue identities are what is used. H-COMOVING is replaced by the weaker H-BOUNDED.
- **G_N and E_Alc were not said to be SMS's coefficient.**
- **"Under H-RS1 that plane is ours"** did not note that the vacuum-bulk two-plane model is the unstabilised one.
- **"The warp's negative energy is entirely the bulk's reading", and H-SIGN-BY-DIMENSION "made concrete and computed".**
  The first holds only if a configuration exists; the second is a named reading. "'Positive energy' in the bulk"
  misplaced the energy: it is the plane's matter.
- **Citations.** SMS eq. 1 is Gauss; eqs. 2 and 10 are Codazzi.
- **Missing doors** (induced gravity, Gauss–Bonnet, asymmetric embedding, high density), and the record of what is not a
  door.
- **Controls.** The untuned control did not exercise the trace residual, and "G_yy is O(v²)" was a contrast, not a
  control.
