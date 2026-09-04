# RESULT S78 — ITEM 2. SEED D BUILT, CAN-FAILED, AND RUN AT Z=89.
# THE TIGHTEST ROW OF ALL 107 HOLDS UNDER A 517 Ha DISPLACEMENT.
# Prediction sha256 8cd0405cfe9b39ebec1aaebcd979e8e88ce8874a8cb2a8a51cdad1efb559267a, filed first.

## THE SEED
**SEED D — shell-wise screened hydrogenic.** Orbital (n,l) is solved in a pure Coulomb
potential -Zeff(n)/r with **Zeff(n) = Z - (electrons in shells of lower principal quantum
number)**, floored at 1. No TFD, no Latter tail, no exchange, no statistical model.
**Zeff is an integer count read off the occupancy — nothing is fitted and c remains the
only number ever entered.** At Z=89 this runs Zeff = 89, 87, 79, 61, 29, 11, 3 from the
1s shell out to 7s. **Physically unlike seed A, which is a Thomas-Fermi-Dirac statistical
potential with a Latter tail.**

## PHASE A — RUN FIRST, AND REACHABLE BY THE DRIVER (THE F77.3 REPAIR)
| Z | max\|d_eps\| A->D | at | valence | valence d |
|---|---|---|---|---|
| 19 | **51.948837 Ha** | 1s | 3p | -3.63710 Ha |
| 89 | **517.200500 Ha** | 1s | 7s | +0.19239 Ha |
**PHASE A PASS.** The Z=19 figure is 51.948837 Ha — **the same number seed C scored**,
because Zeff(1s) = Z in both. **The order's requirement, that seed D be displaced
comparably to seed C's 51.9 Ha, is met exactly at Z=19 and exceeded by a factor of ten at
Z=89, where seed C cannot run at all.**
**CAN-FAIL VERIFIED IN BOTH DIRECTIONS.** Installing seed A into seed D's slot returns
max|d_eps| = 0.000000 at both Z and the gate returns VOID, rc=4.
**AND IT GATES.** pack78/o89segD.py calls phase A on EVERY invocation and exits 4 without
attempting a solve if it does not pass. **s77's item-1 can-fail ran after its scan; this
one cannot, because the driver's only path to a solve is through it.**

## PHASE O — Z=89, ZENO-SEGMENTED, 15 ITEMS
|  | ent | margin mHa | admitted | nfail | ENT_MATCH | ORDER_MATCH |
|---|---|---|---|---|---|---|
| sealed | 6d | 32.330 | 9 | 5 | — | — |
| seed D | **6d** | 32.410 | **5** | 9 | **TRUE** | FALSE (truncation only) |
Admitted under D: 6d 7p 8s 5f 5g. **Dropped relative to seed A: 8p, 6g, 7g, 8g —
ranks 4, 7, 8 and 9. Neither rank 1 nor rank 2 was touched.**
**ORDER_MATCH=FALSE IS ENTIRELY TRUNCATION AND NOT A REORDERING.** The sealed order
restricted to the five channels seed D admits is `6d 7p 8s 5f 5g`, and seed D's order is
`6d 7p 8s 5f 5g`. **Identical. Not one pair exchanged under a 517 Ha displacement.**

## THE MEASUREMENT THAT DECIDES IT
  **COMMON mode +0.038000 mHa · max|DIFFERENTIAL| 0.082000 mHa**
  **2*D = 0.164 mHa against m(89) = 32.330 mHa — the criterion HOLDS, headroom
  +32.166 mHa, a factor of 197.** Raw margin moved 0.08 mHa. Well inside s76's
measured bound of 1.560 mHa.

## PREDICTION SCORED — 4 CORRECT, 2 WRONG
  P2 >=7 of seed A's 9 candidates converge . . . . **WRONG — 5 of 9.** The stated
     rationale, that a candidate does not change the inner screening 5s reads, was right
     about 5s and wrong about the outer channels: the four dropped are 8p and the three
     g channels, all diffuse, and a crude integer screening is worst exactly there.
  P3 ENT_MATCH TRUE, entrant 6d . . . . . . . . . **CORRECT**
  P4 ORDER_MATCH FALSE, a pair below rank 2 reorders . **WRONG IN ITS MECHANISM.** The
     verdict is FALSE and the reason is truncation; **nothing reordered.** Recorded as
     wrong: the prediction named a reordering and there was none.
  P5 admissibility moves, ranks 1 and 2 untouched . **CORRECT** — F77.2 fires again, and
     again harmlessly.
  P6 2*D < m(89), differential larger than seed B's 0.052 mHa, below 1.560 mHa
     . . . . . . . . . . . . . . . . . . . . . . . **CORRECT on all three** — 0.082 mHa.
  P7 raw margin moves < 1 mHa unless rank 1 or 2 is deleted . **CORRECT** — 0.08 mHa.

## WHAT THIS CLOSES
**F76.2's obligation at Z=89 IS NOW DISCHARGED AT FULL STRENGTH.** s77 could report only
that the tightest row survived the 2 Ha falsifier, because the 52 Ha one would not run
there. **It has now survived one ten times larger than the instrument s77 called
unavailable, and the entrant, the top three ranks and the relative order of every common
channel are unchanged.** The differential is 394 times smaller than the margin it must
not cross.
**AND THE F77.2 ADMISSIBILITY CHANNEL HAS NOW FIRED AT THREE SEEDS AND NEVER ONCE TOUCHED
A TOP-TWO RANK.** Seed B dropped ranks 3 and 4; seed D dropped ranks 4, 7, 8, 9. That is
three of three consistent with the bounding observation recorded at s77 — a seed can only
change the entrant by deleting the winner, and what a seed deletes is a channel the
shooting could not find, not a channel shown to lie higher. **Still not a proof.**

## WHAT THIS DOES NOT CLOSE
Z = 56, 39, 72, 90, 19 remain un-re-seeded. **One row has now survived one strong
falsifier. That is what it is and it is not seed-independence of the walk.**