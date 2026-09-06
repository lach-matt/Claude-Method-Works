# FINDING-PROBE-4D (s42, item 0) — F39.2 IS NEITHER (a) NOR (b). THE 4d SOLUTION EXISTS AND IS DESTROYED BY THE FIRST SCF UPDATE.

## 0 · PP-0 MACHINERY GATE PASSED (can-fail, run before any 4d number was read)
Probe root on the healthy l=2 (n=3) channel: **-0.3808072844** vs parent solve_one **-0.3808072853**,
**|de| = 8.4e-10** (bound 1e-8). log(nrm) at the parent's e = **-2.8e-09** (bound 1e-6). nd = 0 as required.
The probe is the parent kernel called directly, and that is now TESTED rather than asserted.

## 1 · THE VERDICT — BOTH BRIDGE ALTERNATIVES ARE REFUTED
**(a) "4d genuinely unbound in the field" is REFUTED.** The tail is exactly Coulombic: V*r = **-1.000000**
at r = 30, 60, 100, 200, 298 (grid runs to 300). `_ceff = Q[a]-1 = 0` for the q=1 shell, so the channel
carries NO residual self-Coulomb and the -1/r tail holds an infinite Rydberg series. Measured directly:
the l=2 well supports nd = 1, 2, 3 and 5 states at e < 0. The channel is bound and the well is deep enough.
**(b) "bound but outside the bracket's reach" is REFUTED.** The seed is not outside anything. Measured:
**it2 seed eh = -0.040180, and nd AT THE SEED = 1.** The bracket STARTS ON THE CORRECT STATE.

## 2 · WHAT IS ACTUALLY HAPPENING — UNPREDICTED, TIMING-FLAGGED (R 1449)
Per-iteration trace of the (l=2, n=4) channel at Z=21, config [Ar]4s^2 4d^1:
    it1   e0 = -0.055752   e = **-0.047224**   **nd = 1**   <- CORRECT STATE, FOUND
    it2   e0 = -0.052341   e = **-0.092513**   **nd = 0**   <- raise: "Z=21 42 nodes 0"
**THE 4d SOLUTION EXISTS AT IT1 AND IS GONE AT IT2.** Fine scan of it2's field, 421 points across the
whole nd=1 window (-0.070 .. -0.028): **ZERO sign changes of log(nrm).** The closest approach is
**min log(nrm) = +0.892 at e = -0.05420, i.e. the norm is 2.44x too large** — not a near-miss, structural.
Across the entire e < 0 range the ONLY zero crossing is the nd = 0 one at -0.0925.
**So at it2 no normalised 1-node solution exists anywhere, and no seed could have found one.**
THIS EXPLAINS s41's FAILED REPAIR EXACTLY: t7d_node walked n' = 5..14 to move the SEED, but the root was
not absent from the seed's neighbourhood — it was ABSENT FROM THE FIELD. The repair failed for the right
reason and its negative result is now positively diagnosed.

## 3 · THE MECHANISM, NAMED
The exchange source is built from the channel's OWN orbital: `X += 0.5*Q[b]*c3j0sq*Yk(P[a],P[b],k)/r*P[b]`
carries P[a], and `yold = Pold*exp(-x/2)` sets the inhomogeneous boundary from P[a] as well. At it1 P[4d]
is the compact hydrogenic seed. it1 returns a DIFFUSE Rydberg orbital (e = -0.047, turning point r[m] ~ 17
rising to ~30 by e = -0.03). Mixed in at beta = 0.4, that diffuse orbital re-drives its own source, the
response over-normalises by 2.44x, and the norm condition log(nrm) = 0 has no root left in the node-1 window.
**The instability is specific to a WEAKLY BOUND channel whose exchange source is fed by its own diffuse
orbital. It is a property of the SCF UPDATE, not of the field's boundedness and not of the bracket's seed.**

## 4 · AND THE BRACKET THEN WALKS DOWN AND OUT — PP-4 FAILED, INVERTED
`solve_one` seeds at eh, sets hi = eh - 1e-7|eh|, and if log(nrm) there is NOT negative it expands
DOWNWARD (step 0.02|eh|+1e-4, x1.6) until it finds a negative value. log(nrm) is positive throughout the
node-1 window, so the expansion walks past the window entirely and brackets [lo, hi] SPANNING TWO STATES.
Bisection on a bracket containing two roots returns whichever the sign pattern selects — here the nd = 0
state at -0.0925. **The node target `tgt` is computed and never used, so nothing stops the walk-out.**
PP-4 predicted the seed sits BELOW the node-1 window. **It sits INSIDE it. The failure is inverted.**

## 5 · SCORING (as written, before the run)
    PP-0  machinery gate                                    **HELD**  (8.4e-10 / 2.8e-09)
    PP-1  exists e<0 with nd = 1                            **HELD**  (window -0.065..-0.033; root at it1)
    PP-2  node-1 root in (-0.12, -0.015) Ha                 **HELD at it1** (-0.047224); VOID at it2 (no root)
    PP-3  nd(e) monotone non-decreasing                     **HELD**  (0,0,0,0,0,0,0,0,1,1,1,2,3,5)
    PP-4  seed below the window, first crossing still nd=0  **FAILED, INVERTED** (seed INSIDE, nd=1 at seed)
    PP-5  nd jumps 0->2 / non-monotone (instrument fault)   **HELD FALSE** (nd_full == nd at every point;
                                                                     no node hides outside the turning point)
**VERDICT PREDICTED (b), VERDICT MEASURED: NEITHER. A THIRD MECHANISM, NOT IN THE FILE. TIMING-FLAGGED.**

## 6 · TWO CORRECTIONS TO BRIDGE s41 §3(0), ENTERED BECAUSE THEY MISDIRECT THE PROBE
- The field is **NOT FROZEN and NOT Sc+**. `nlchain.step` runs a FULL SCF per candidate; the failing object
  is a 21-electron NEUTRAL system at nuclear charge 21 inside `run2`.
- `solve_one` **does not raise**. It returns (u, e, nd=0, res); `hfc2.py`'s node check raises afterwards.

## 7 · WHERE THIS LEAVES PV-3
**PV-3 IS NOT THE PREREQUISITE FOR THE 4d ROW.** s41 §2b(11) read the repair's failure as evidence that 4d
is unbound in the reference; that reading is now refuted by direct measurement of the tail and of the node
spectrum. PV-3 remains open and remains owed for the **Ac 5f positive Delta**, but the two routes that s41
said "terminate on the same object" DO NOT. They are different objects and F39.2 is the nearer one.

## 8 · NOT DONE HERE
No repair designed, no chain row produced, no banked number touched. Whether the fix is (i) enforcing the
node target inside the bracket, (ii) damping the diffuse channel's own source, or (iii) a different SCF
update for weakly bound channels is a SEPARATE prediction file, written before any repair is built.
Gates 1-71 remain byte-identical: t7c_hfsr.py, t7b_hf.py, hfc2.py were not edited.
