# FINDING-REPAIR-4D (s42, item 0b) — ALL THREE CANDIDATES FAIL. F39.2 IS NOT A FAULT AND THE WALK IS NOT BLOCKED.

## 0 · D1 INERTNESS — REFERENCE RECOVERED, AND A FAULT FOUND IN MY OWN HARNESS FIRST
Banked s41 Z=21 3d: **D = -0.26664**. Harness first returned -0.266347 (|d| = 2.9e-4). Cause found before
any candidate was scored: **`nlchain.candidates` returns (n,l) PAIRS and `nlchain.add` SORTS the config**, so
3d is inserted BEFORE 4s, not appended. **SHELL ORDER IN `occ` IS LOAD-BEARING AT FINITE TOLERANCE.**
Registered **F42.2**. Harness corrected to build configs through `nlchain.add` itself; reference then
reproduces at **-0.266643 vs -0.26664, |d| = 3e-6.** D1 results, all against that reference:
    (i) NodeGated  -0.266643  IDENTICAL     (ii) beta=0.20  -0.266643  IDENTICAL
    (iii) ChanHold -0.266643  IDENTICAL     (ii) beta=0.10  -0.266972  it=[100,100] NOT CONVERGED (maxit artefact)
All three pass D1. None moves a healthy banked number.

## 1 · D2 — ALL THREE FAIL. TWO LOUDLY, ONE SILENTLY.
**(i) NODE-GATED BRACKET — FAILS D2, EXACTLY AS PREDICTED AND FOR THE PREDICTED REASON.**
    `NoRootInNodeWindow: nd==1 window exists but log(nrm) has no zero in it: l=2 n=4 Z=21 minlog=+0.9083`
    PR-1 HELD. It converts a silent wrong state into a loud correct failure. That is worth having and it
    does not open the 4d row.
**(ii) MIXING DAMPING — FAILS D2 AT EVERY beta TESTED: 0.20, 0.10, 0.05, 0.02.** Same raise, same iteration.
    **PR-2 FAILED.** The reason PR-2 gave — "the instability is driven by the SIZE of the orbital change" —
    is REFUTED: a 2% admixture of the diffuse orbital destroys the root as surely as 40%. **It is not a
    step-size problem, so it is not a convergence-control problem.**
**(iii) CHANNEL HOLD — APPEARS TO PASS D2, AND THE PASS IS SPURIOUS. PR-3 FAILED.**
    It returned D = -0.049895, eps4d = -0.050029, converged it=[30,30]. **Verified against the UNMODIFIED
    parent at its own fixed point: parent returns e = -0.083545, nd = 0, and RAISES.** A 421-point scan of
    (-0.12, -0.015) at that fixed point finds **exactly one root, nd 0->0, at -0.08362. NO nd=1 ROOT EXISTS
    THERE.** ChannelHold converged **by not solving the channel** — it held the first-iteration orbital and
    called the result self-consistent. **A CONVERGENCE THAT HOLDS THE FAILING OBJECT IS NOT A CONVERGENCE.**
    Caught only because D3's cross-check was written before the run; with one survivor and no cross-check
    this number would have entered the record as a converged 4d.

## 2 · THE FOURTH OUTCOME IS THE TRUE ONE (PREDICTION §4, REGISTERED IN ADVANCE)
**The self-consistent field of [Ar]4s^2 4d^1 at Z=21 has NO normalisable 1-node solution.** Not at the start
(it1 has one, at -0.047224), not on the path, not at the fixed point. The 4d state exists in the INITIAL
field and is absent from the SELF-CONSISTENT one. This is the PV-3 object (frozen-vs-relaxed, UNBOUNDED).
**AND IT IS NOT A NUMERICS FAULT: IT IS THE FIELD ANSWERING CORRECTLY.** Neutral scandium has no
self-consistent 4d channel — the d electron collapses to 3d, which is what the record shows and what
FINDING-CHAIN-3D measured as the 3d collapse. **The raise is the correct answer delivered through the wrong
exception.**

## 3 · AND THEREFORE F39.2 IS NOT A BLOCKER — MEASURED, NOT ARGUED
s41 promoted F39.2 by this inference: 4d drops 10/10 at every step since Z=21, a channel dropping 100% of
the time cannot win at Z=39, so the guard fires UNSAFE and the walk HALTS. **The inference is refuted by
direct measurement.** DIAGNOSTIC (config RECALLED-NOT-ENTERED, chain has not reached Z=39):
    **Z=39, [Kr]5s^2 + 4d:  D = -0.195614,  eps(4d) = -0.231503,  converged in 34 iterations, NO RAISE.**
**4d CONVERGES CLEANLY WHERE IT MUST WIN.** The drop rate at Z <= 30 says nothing about Z=39 because THE
FIELD IS DIFFERENT — that is the same per-element-to-universal fault the register has corrected repeatedly
(R 1675), committed here against a census of my own drops. **NO REPAIR IS REQUIRED. THE WALK IS NOT BLOCKED.**

## 4 · SCORING
    D1 inertness      (i) PASS   (ii) PASS at 0.2   (iii) PASS       [reference re-derived after F42.2]
    D2 produces 4d    (i) FAIL   (ii) FAIL all beta (iii) FAIL (spurious pass, caught by cross-check)
    D3 agreement      VACUOUS — no two survivors. **THE COMPARISON DECIDED AGAINST ALL THREE.**
    D4 gates          HELD — no parent file edited; gates 1-71 byte-identical; census clean
    D5 furthers n+l   **YES, BY REMOVING THE OBJECT**: guard UNSAFE stays 0 and 4d wins at Z=39 unrepaired
    PR-1 HELD · PR-2 FAILED · PR-3 FAILED · PR-4 VACUOUS · PR-5 VOID (held seed, not a solution) · PR-6 NOT REACHED

## 5 · WHAT IS ADOPTED, AND WHAT IS NOT
**NOT ADOPTED: all three repairs.** None is wired into nlchain. No banked number changed.
**RECOMMENDED FOR ADOPTION (M's ruling required): (i) NodeGated's EXCEPTION ONLY, not its bracket.** The
value measured is that it names the condition — "node window exists, norm condition has no root in it" —
where the parent says "nodes 0". It is a DIAGNOSTIC upgrade, inert on every healthy channel (D1 identical),
and it would have made this session's finding readable from the error string alone. It opens no row and
changes no number.
**PV-3 STATUS: the object is real and now has a mechanism, but it is NOT the prerequisite for the 4d row.**
It remains owed for the Ac 5f positive Delta. s41 §2b(11) and s42's own FINDING-PROBE-4D §7 are BOTH
superseded here: §7 said the two routes are different objects, which is right; s41 said PV-3 blocks the
4d row, which is wrong for a reason neither session had measured.

## 6 · HELD
No record value entered as an input. The Z=39 configuration is RECALLED-NOT-ENTERED and used for a
DIAGNOSTIC only — it is not a chain row and must not be scored as one. c = 137.035999 only.
beta is CHOSEN-CONVERGENCE-CONTROL; no adopted value depends on it.
