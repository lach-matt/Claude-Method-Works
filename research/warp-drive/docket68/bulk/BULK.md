# Two planes joined through a higher dimension (H-HIGHER-CORRIDOR, H-NO-SPEED; verified once; SEATED in ledger.py section 8i on M's "4, then 3 please.", item 59; 2026-10-05)

*First headed* "(H-HIGHER-CORRIDOR, H-NO-SPEED; verified once; not seated; 2026-10-05)".

## M's words and how they are carried

- **Item 57, verbatim:** *"If two points, each on a different spacetime plane, are connected by a corridor through a
  higher dimension, then speed cannot exist in the dimension below the corridor as you are at position 1 then position
  2, with no in between, which means no travel, no speed"*.
- **Item 58:** *"3, then 2, then 1 please"*. So the case is fixed first as two separate planes, then the sources are
  READ, then the corridor is modelled.

These are carried as M's hypotheses **H-NO-SPEED** and **H-HIGHER-CORRIDOR**, never as results. O9 stays OPEN.

Every number below is printed by `bulk.py`.
- **Selftest:** 4/4 checks, 2 of them controls, with 4 STRUCTURAL lines printed and not counted.
- **Inputs:** it asks `branelink.py` and `cosmo.py` for its inputs.
- **Verification:** it was verified once, and its findings are applied (see History).

## Step 3: the case is two planes

Two separate 4D worlds ("branes") joined only through a fifth dimension (the "bulk"). Three published geometries with
this shape are carried. **None is observed: all three are models.**

| geometry | what it is | source (READ) |
|---|---|---|
| **Randall–Sundrum** | Two branes, ours and a "hidden" one, with a warped slice of AdS5 between them. Ordinary matter stays on a brane; gravity lives in the bulk. | hep-ph/9905221v1 |
| **Chung–Freese** | Two branes, *"one is our observable universe and the other is the hidden sector"*. The warp stretches distance along the hidden brane but not time. | hep-ph/9910235v2 |
| **Manyfold** | Our own brane, folded in the bulk. Its folds are *"nearby in the bulk, at sub-millimeter distances"*, so an object seen far away *"may in fact be just a millimeter away through the bulk!"* | hep-ph/9911386v1 (Arkani-Hamed, Dimopoulos, Dvali & Kaloper) |

## Step 2: what the sources say (READ via alphaXiv, 2026-10-05; printed pages)

- **Randall–Sundrum.**
  - The metric is eq. 12 (p.4), and the bulk is "a slice of an AdS5 geometry" (p.3).
  - A visible-brane mass is e^(−kr_cπ)m₀ "when measured with the metric ḡ" (eq. 21, p.5). So **our atoms' observed
    masses are ḡ masses, and our clocks count ḡ time** (H-OBSERVED-FRAME).
  - The warp factor is "of order 10^15" (p.6). Gravity's bulk modes couple to our matter at "Energy/TeV" (p.6).
  - **Discrepancy (a misprint or ambiguity in the paper, not a refutation):** p.6 prints "kr_c [symbol lost] 50", where
    the 50 is genuine text. A warp of 10¹⁵ gives kr_c = 11.0, and Goldberger & Wise read "kr_c around 12"
    (verifier-READ).
- **Chung–Freese.**
  - The metric is eq. 3, ds² = dt² − [e^(−2ku)a²dh² + du²], with ours at u = 0 and the hidden brane at u = L.
  - A signal crosses (A), runs along the hidden brane (B) and returns (C). It covers h(1,2) = e^(kL)∫dt/a, against our
    brane's h(1,3) = ∫dt/a (eqs. 7–8, p.4). "kL ∼ ln(10^5)" solves the horizon problem (p.4).
  - **Their caveats.**
    - The path is **patched**: its corners need interactions between the bulk and the branes (p.4).
    - "we have not found continuous paths which return to our brane at a point more distant than our naive 'horizon'"
      (p.4).
    - "we have a fine tuned solution" (p.8).
- **Manyfold.**
  - Folds "can communicate at rates which appear superluminal to a brane-localized clock".
  - "these effects do not violate causality of the theory" (p.15).
- **Caldwell & Langlois** (gr-qc/0103070v1).
  - In static Randall–Sundrum the bulk and brane horizons are "exactly identical" (p.5).
  - "there is no shortcut for compact, flat extra dimensions" (p.8).
  - Eq. 22 (p.6) is for a single brane in an infinite bulk, valid for a_B ≫ a_A.

## Step 1: the model, computed, with no speed anywhere

Only each end's own clock is computed (H-LOCAL-CLOCK). One-way readings use the static slicing (H-STATIC-SLICING); the
round trip is convention-free.

### 1. Randall–Sundrum: the jump between the two planes

- **No speed exists between bulk-paired points.** There is no curve *in either plane* between them, so a speed is
  undefined there, as M said (STRUCTURAL).
- **What each clock reads,** at k = 2×10¹⁸ GeV (H-K-PLANCK, at the edge of RS's own k < M):

  | clock | reads |
  |---|---|
  | **ours**, one way | **3.29×10⁻²⁸ s**, which equals ħ divided by the model's 2 TeV scale |
  | ours, round trip | 6.58×10⁻²⁸ s |
  | a hidden clock built to the same physics | 3.29×10⁻¹³ s of its own |

- **The checks.** Integrating the null path numerically reproduces the closed form to 1.6×10⁻¹⁵.
  - **Control:** removing the warping (k → 0 with r_c fixed) gives both clocks πr_c/c.
- **This is "position 1, then position 2".** Our clock registers about 3×10⁻²⁸ s, and there is nothing in between in
  either plane.

### 2. Randall–Sundrum: landing somewhere else

In this geometry **every** causal path reads at least the light time to a place a distance D away. That holds for static,
flat branes (H-RS1, STRUCTURAL); for the Proxima span it is 4.2465 yr. **This floor belongs to this geometry, not to
brane-worlds in general.**

### 3. Chung–Freese: landing somewhere else, through the other plane

- **The route:** cross to the hidden plane, run along it, and come back (patched, static: H-CF-STATIC, H-CF-PATCHED).
- **Our clock reads 2L/c + e^(−kL)·D/c.** That is shorter than D's light time once D exceeds 2L/(1 − e^(−kL)).
- **At their kL = ln(10⁵):**
  - the Proxima span's term is **1340 s, about 22 minutes**;
  - the crossing term 2L/c is 6.7×10⁻¹² s at an illustrative L = 1 mm (H-L-ILLUSTRATIVE).
- **The checks.**
  - The static reading reproduces their factor of 10⁵.
  - **Positive control:** no shortcut below the threshold, and one above it.

### 4. Manyfold: places that look far but are near

- **The gap.** A 1 mm bulk gap reads 3.3×10⁻¹² s on our clock.
- **Proxima is not on another fold.** We see it at its light time, so it lies on our own fold, and the Manyfold pairs
  only places that *look* electromagnetically far.

### 5. One plane (the board's present case)

- **Static Randall–Sundrum:** no shortcut.
- **Caldwell–Langlois's expanding single brane,** at z = 1090:
  - at ℓ = 1/k (ℓH₀ = 7.2×10⁻⁶¹), the advance is 2.0×10⁻¹¹⁴;
  - at their bound, it is at most 3.9×10⁻⁵².
- **The board's moving brane (O7):** **at most** 93.8 ns over 4.2465 yr.
  - This is conditional on the graviton being in the bulk, on an untilted brane, and on GW170817's simultaneous-emission
    edge. Under GW170817's −100 s emission window the figure is 5.09 μs.
  - Caldwell–Langlois's "no shortcut for compact, flat" dimensions is the static case; O7's saving comes from the brane's
    motion.

### 6. Loops, and entering and leaving (STRUCTURAL)

- **Loops.** Static Randall–Sundrum has a global time, so it has no closed causal loop. Chung–Freese hide their apparent
  causality violation today, and the Manyfold "do[es] not violate causality". Gao & Wald's time-delay theorem under the
  null energy condition is NAMED-NOT-READ.
- **What crosses.**
  - In Randall–Sundrum it is gravitational: bulk modes produced and detected through their decay products. Collider rates
    exist (Davoudiasl–Hewett–Rizzo, NAMED-NOT-READ).
  - In Chung–Freese it is bulk-brane interactions at the corners.
  - The board has not computed or READ a rate for a carrier of the defining information (O6).

## For M

- **Your two-plane corridor matches published models.** None of them is observed. Your reason (item 62, carried as
  H-UNOBSERVED-UNBUILT): *"no one has designed the device to allow for the travel, which will allow for the
  observation"*. Other routes to the same observation exist beside it: collider and short-range gravity searches
  look for a bulk without travelling through it. READ on M's order (item 63, `SEARCHES.md`): none saw a deviation
  inside its searched range. The colliders did not search this file's Randall–Sundrum point (coupling 0.82, a 7.66 TeV
  graviton). Where they did search, they exclude a band of jump times, roughly 10⁻²⁷ to 10⁻²⁶ s on our clock; longer
  and shorter jumps are untested. The torsion balances cap a gap through one flat circular dimension at about 94 μm,
  against the illustrative 1 mm used here; the Manyfold does not need 1 mm.
- **Between bulk-paired points there is no path in either plane, so no speed exists there,** as you said. In
  Randall–Sundrum our own clock reads about 3×10⁻²⁸ s for the jump.
- **Whether the corridor can land somewhere far away depends on the higher dimension's shape.**
  - Flat, static Randall–Sundrum: no. Landing D away costs at least D's light time.
  - **Chung–Freese's two planes: yes.** Through the other plane the Proxima span reads about **22 minutes** on our
    clock, against 4.25 years for light along our plane. Their path needs interactions where it meets each plane, they
    found no smooth path that does this, and the solution is fine-tuned.
  - **The Manyfold: yes, for places on another fold.** They look billions of light-years away but are a millimetre away
    through the bulk. Proxima, though, is on our own fold.
- **So the open question is the shape of the higher dimension between here and the destination.** That is what fixes
  which places are close through it (H-BULK-PAIRING), and published shapes exist that do it.

## Named hypotheses

- H-RS1, H-RS1-WARP and H-K-PLANCK.
- H-OBSERVED-FRAME, H-SAME-LAGRANGIAN and H-STATIC-SLICING.
- H-BULK-PAIRING.
- H-CF-STATIC, H-CF-PATCHED and H-L-ILLUSTRATIVE.
- H-MM-FOLD.
- H-GRAVITATIONAL-CARRIER.
- M's H-NO-SPEED, H-HIGHER-CORRIDOR, H-LOCAL-CLOCK and H-UNOBSERVED-UNBUILT (item 62).

## OPEN

1. A bulk geometry in which a chosen destination is close through the higher dimension, beyond Chung–Freese's patched,
   fine-tuned example and the Manyfold's folds.
2. Entering and leaving the corridor (O6): a rate for a carrier of the defining information.
3. Whether any second plane exists. None of the three geometries is observed (M's reason: H-UNOBSERVED-UNBUILT,
   item 62). The LHC searches constrain Randall–Sundrum only within the couplings they searched, which do not include this
   file's point; the torsion balances cap one flat circular dimension (READ, `SEARCHES.md`).
4. Randall–Sundrum's published kr_c (PRL, NAMED-NOT-READ) against the v1 text.

## History (verifier, 2026-10-05; first-written claims kept)

- **Our clock was in the wrong frame.** The first version said our clock reads *"3.29×10⁻⁴³ s … about the Planck
  time"*. Our atoms keep their observed masses in ḡ, so our clock reads 3.29×10⁻²⁸ s; the hidden clock's figure was
  likewise mis-stated.
- **The floor was overstated.** It said *"landing somewhere else on our plane costs at least that place's light time"*
  as if general, and that *"no source says what fixes"* the pairing. Both are wrong: the floor is specific to static,
  flat Randall–Sundrum, and Chung–Freese and the Manyfold are published counterexamples, now carried with their caveats.
- **The checks.** Four of the six checks could not fail, and the control was an identity. They were replaced by a real
  control (k → 0) and a positive control (Chung–Freese).
- **The detour figures** were hand-picked depths, not bounds.
- **Caldwell–Langlois** was applied at z = 0, outside its validity, and to the wrong model.
- **O7's 93.8 ns** is a maximum, under conditions now listed.
- **Two phrases were too strong.** *"Exists as published physics"* overstated a model, and *"no one has computed a
  rate"* was wrong.
- **M's reason for "none is observed" (item 62, 2026-10-05).** The For-M line first read only *"Your two-plane
  corridor matches published models. None of them is observed."* M's reason is now carried beside it as a hypothesis.
- **The searches READ (item 63, 2026-10-05).** The For-M line first said what they report was *"NAMED-NOT-READ here"*,
  and OPEN 3 first read *"LHC searches constrain Randall–Sundrum (NAMED-NOT-READ)"*. Both are now READ in
  `SEARCHES.md`.
- **The searches' verifier (2026-10-05).** The For-M line first said the colliders *"cap the jump at about 10⁻²⁷ s"*
  and the balances *"cap a flat bulk's gap at about 94 μm"*. The first is a window, not a cap. The second holds for one
  flat circular dimension.
