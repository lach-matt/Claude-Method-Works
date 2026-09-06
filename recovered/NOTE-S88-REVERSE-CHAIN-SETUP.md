# NOTE S88 — SETUP FOR THE REVERSE CHAIN (s89). Everything s89 needs, in one place.

## The objects (all in rt/ and pack84-88)
  semi84.field_of(Z)            -> h (frozen N-1 core), row, eps. ~5-18 s.
  gtest83.channels(row, lmax=3) -> frontier candidates; sort by nu; rank 0,1 = width 2.
  semi85.q_native(h,n,l)        -> (r, q) of the channel's q(r) = -r V_loc (E7 exchange if occupied)
  semi85.channel_row(E,l,r,q)   -> K, b0, b1, J, n_regions, r_in, r_out (OUTER well ruling)
  semi84.J_of(E,l,qfun,detail)  -> J plus meta['I_inner'] for the inner well (s88 wells())
  semi85.J_tent, semi87.J_profile, prof88.profile_J -> the bounds of L3
  The banked g-difference per step: rt/nlchain.jsonl rows (D1); s84 §S7 rule = sign(dg/dl)
  at rank-2 channel vs sign of banked g-difference (35/37 agree, Z=56 a region switch).

## The five open rows of L3 and their neighbours (sealed numbers)
  4d: Z=37 two wells (outer K=0.056 J=1.011); Z=38 ONE well J=2.234 K=1.381; Z=39 J=2.273;
      Z=40 J=2.076 (4d enters A here); Z=42 J=1.873. Collapse 37->38.
  5d: Z=55 two wells, outer J=1.036 inner J=1.861; Z=56 one well J=2.441; Z=57 J=1.985.
  6d/5f: Z=89 6d J=2.020; Z=90 5f J=2.102 (6d 1.906); Z=91 5f J=2.046 (6d 1.832).
  All five rows are CORRECT at width 2 in D1. The failure is of the bound, not the order.

## What L3 at the pair must answer
  For the step Z-1 -> Z with candidates A (entrant) and B (rival): Delta g = g_A - g_B.
  One-channel: dg/dl = 2 - J each. Two-channel: the sign of Delta g is what D1 uses.
  Hypothesis to file: at a merge row the merged candidate's J >= 2 while the rival's J < 2
  and the banked Delta g has the sign the MERGE predicts. Can-fail: a merge row where it does not.

## Timing and Zeno
  wells() at 4 rows: 40 s. A 15-row neighbourhood scan (38-41, 55-57, 88-92) ~3 min in 3
  segments. Field rows Z>=88: 18 s each.

## Discipline reminders specific to this chain
  * Each link gets its OWN prediction file and sha before its unit runs.
  * L6 is VARIATIONAL; do not write it as a limit. The proof form names it.
  * The target is the observed ORDER; n+l is its 89%-accurate name (La, Ac invert).