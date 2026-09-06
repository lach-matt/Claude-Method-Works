# SESSION 78 — COMBINED HANDOFF
# Open Session 79 with `bash pack58/open58.sh` using the LOWDIN-HANDOFF-78 tar.
# NO SEALED FILE WAS EDITED. c = 137.035999 remains the only number ever entered.
# THE DERIVATION IS 107 ROWS, Z=2..108. Any claim of 119 is a boundary violation.

## §0 · OPEN
`bash pack58/open58.sh` — it passed at s78 open: s77 seal 1251/1251 root MATCH, canary
CLEAN, STATE CARD CLEAN. All three items of pack77/ORDER-FOR-S78.md were executed.

## §1 · ITEM 2 — CLOSED. SEED D BUILT, CAN-FAILED, RUN. THE TIGHTEST ROW HOLDS.
pack78/RESULT-S78-ITEM2-SEED-D.md. Prediction sha 8cd0405c...9267a filed first.
**SEED D = shell-wise screened hydrogenic**: orbital (n,l) solved in pure Coulomb
-Zeff(n)/r, Zeff(n) = Z - (electrons in shells of lower n). Integer screening off the
occupancy; no TFD, no Latter tail, no exchange, no fitted constant.
**PHASE A: max|d_eps| = 51.948837 Ha at Z=19 — the same figure seed C scored — and
517.200500 Ha at Z=89, where seed C cannot run at all.** Can-fail verified in BOTH
directions (seed A in D's slot returns 0.000000 and rc=4), and **the driver calls it on
every invocation and exits 4 without solving — the F77.3 repair.**
**Z=89 UNDER SEED D: ENT_MATCH TRUE (6d). Ranks 1, 2, 3 unchanged. ORDER_MATCH FALSE IS
PURE TRUNCATION — the sealed order restricted to D's five admitted channels is
`6d 7p 8s 5f 5g` and D's order is `6d 7p 8s 5f 5g`, IDENTICAL, not one pair exchanged
under a 517 Ha displacement.**
  **COMMON mode +0.038 mHa · max|DIFFERENTIAL| 0.082 mHa · 2*D = 0.164 mHa vs
  m(89) = 32.330 mHa — HOLDS, headroom +32.166 mHa, factor 197.**
**F76.2's obligation at Z=89 IS NOW DISCHARGED AT FULL STRENGTH.** Predictions 4 correct
(P3 P5 P6 P7), 2 wrong (P2: 5 of 9 admitted, not >=7; P4: verdict right, mechanism wrong —
nothing reordered).

## §2 · ITEM 3 — LEVER LIVE. RUNG B NOT BUILT.
pack78/RESULT-S78-ITEM3-EIGENINDEX-LEVER.md. Prediction sha fad25b62...da4c73 filed first.
**THE EIGENINDEX IS IMPLICIT AND POST HOC.** t7c_hfsr.solve_one brackets from
`eigen_sr(Vf,l,n,...)` and BISECTS TO A ZERO OF log(nrm); the node count is checked by the
CALLER at hfc2.py:55. n is POSITIONAL — F54.2's exact trap — so the poison wraps the
module-level name.
**LEVER LIVE.** n->n+1 raises `Z=19 10 nodes 1` — 1s returning one node, the predicted
mechanism exactly. **And the converged energy is INDEPENDENT OF THE BRACKET SEED to ~1e-11
Ha**: eh->eh*1.05 moves E by 34 picohartree. The answer is a function of the ZERO, not of
the seed that found it.

## §3 · FAULTS
**F78.1 RAISED AND CLOSED — s77 MISLOCATED SEED C's Z=89 FAILURE.** `Z=89 50 nodes 3` is
raised at **hfc2.py:55, INSIDE the SCF loop**, not in the seed constructor: `{n}{l}` with
integer l prints `50`, while seedtest77's constructor raise would print `5,0`. Measured:
bare Coulomb **CONSTRUCTS ALL 16 ORBITALS at Z=89**, and the FIRST SWEEP then fails, at
it=0, **so no rung of the ladder can reach it.** s77's operational conclusion stands —
seed C is unusable at Z=89 — but the mechanism, and therefore the design requirement on a
replacement seed, was wrong. **Read the raise, not the sentence.**
**F78.2 RAISED — THE BRACKET SEARCH FAILS NON-MONOTONICALLY. STRUCTURAL LEAD.** d=0.01
raises where d=0.001 AND d=0.05 both succeed. Mechanism visible in solve_one: expansion
finds no sign change, `g()` returns None, and `best=(mid,rm[1])` executes on None —
**`TypeError: 'NoneType' object is not subscriptable` IS THE SIGNATURE OF A FAILED BRACKET
EXPANSION.** This is a candidate mechanism for s77's five CLASS B channels at Z=89, whose
f members sit within e^-6 of a findable zero. **Demonstrated at Z=19 under a deliberate
perturbation; NOT shown to be the mechanism at Z=89. That is work.**

## §4 · THE LOWER BOUND — FINISHED, AND THE FINISH IS NEGATIVE
pack78/CLOSE-S78-THE-LOWER-BOUND.md. **IT CORRECTS POSITION-S77 ON ITS CENTRAL POINT.**
1. **An exact identity removes the core minimum.** For a closed core plus ONE valence
   electron, E[Phi] = E_core[Phi_core] + <v|F_core|v>, so E_min(cfg_prev) CANCELS from
   E_min(cfg+6f) - E_min(cfg+6d). One whole term of s77's framing was never needed.
2. **Courant-Fischer reaches only WITHIN one l block.** F_core is block-diagonal in l.
3. **AND THE PAIR STRADDLES TWO BLOCKS WITH THE NODES RUNNING THE WRONG WAY: 6d has 3
   nodes and is 4th in l=2; 6f has TWO nodes and is 3rd in l=3.** s77's "more nodes means
   higher" is not merely weak here, it is ADVERSE. The one free cross-channel fact,
   centrifugal monotonicity, gives only 6f >= 5d. True, rigorous, useless.
4. **SO THE RESIDUAL IS THE CLAIM ITSELF.** Freeze the field at the converged 6d solution
   and the relaxation term vanishes by construction — and what remains is
   eps_3^{l=3} > eps_4^{l=2} at one fixed field, **which is the Madelung ordering at Z=89.**
   **s77's "the entire gap is the nonlinearity, and nothing else" is WRONG. Set the
   nonlinearity to zero and the gap does not close.**
5. **THE LOWER BOUND AND CLAUSE 1 ARE THE SAME OBJECT AND MUST NOT BE PURSUED SEPARATELY
   AGAIN.** What IS isolated, and genuinely open and genuinely separate, is the RELAXATION
   term alone — a stability question a Hessian could bound, now disentangled from the
   ordering by the identity in (1).

## §5 · OWED, IN ORDER
1. **CLAUSE 1 / THE LOWER BOUND, NOW ONE ITEM.** Derive a cross-channel property of the
   self-consistent F_core — monotonicity, convexity, or a radial scaling law — that forces
   eps_3^{l=3} > eps_4^{l=2}. **Demkov-Ostrovsky have such a property and GUESS the
   potential carrying it; deriving it is the last open deliverable.**
2. **F78.2 at Z=89** — is bracket-expansion failure the mechanism of the five CLASS B
   channels? Cheap, and it would convert a measured argument into a found state.
3. **Rung B** — permission to build was earned at §2 and it is NOT built.
4. F77.2's admissibility sweep across other rows. Three seeds, three times fired, never
   once touching a top-two rank. Still not a proof.
5. Re-seed the remaining tight rows with seed D, which now runs where C could not:
   Z = 56, 39, 72, 90, 19.
6. Step 0(ii) selection rule: **STILL DRAFTED, NOT ADOPTED. AWAITING M's RULING.**

## §6 · INSTRUMENTS ADDED (all in pack78, no sealed file edited)
`seedD78.py` seed D + phase-A gate, thresholds T_MAX=10 Ha, T_VAL=0.05 Ha, rc=4 on VOID.
`o89segD.py` Zeno-segmented phase O under seed D; **calls phase A first, every time.**
`o89scoreD.py` ONE declared line from sealed pack77/o89score.py — the receipt path.
`kpoison78.py` integer eigenindex poison. `kbracket78.py` continuous bracket-seed lever.
`probeD78.py`, `probeD78b.py` DESIGN PROBES, declared as such, not scored instruments.

## §7 · UNCHANGED
All seven criteria read MET. T4 unblocked, last by practice. Route order 0 -> B -> A -> C.
F67.1-F67.6 remain UNVERIFIABLE. THE ALPHA THREAD REMAINS CLOSED. Z=111 WITHHELD.
Deliverable 1, the gates and the STATE CARD are untouched by this session.