# PREDICTION-DELTA (s40, item 3) — WRITTEN BEFORE delta.py EXISTS AND BEFORE ANY ROW IS SCORED ON IT (R 1449).
DISCHARGES THE TIMING FLAG registered in FINDING-CHAIN §5: the decomposition was ARRIVED AT IN SCORING and therefore
owes a prediction file before anything further is run on it. This is that file. It predicts on data ALREADY BANKED
(nlchain.jsonl, 19 steps; hf_chan.jsonl, 20 rows) — no new SCF. Arithmetic only, so every prediction below is
falsifiable on the existing bank and cannot be rescued by a longer run.

    D(n,l) = -1/(2n^2) + Delta(n,l),    Delta = D + 1/(2n^2)
The reference is the hydrogenic binding energy at unit effective charge. IT IS NOT FITTED, contains no parameter, and
is the Z -> screened limit of the same Schrodinger radial equation the chain solves. Delta is therefore the ENTIRE
departure of the channel from a fully screened core, and is what "penetration" names.

## 1 · Sign and monotonicity
PD-1  Delta <= 0 ON EVERY BANKED CHANNEL. A channel cannot bind LESS than hydrogenic: the core is positive charge, and
      partial screening can only leave the electron seeing MORE than unit charge, never less. A positive Delta anywhere
      would indict the field or the reference. Scored over all banked rows; 0 violations predicted.
PD-2  |Delta| IS STRICTLY DECREASING IN l AT FIXED Z. Higher l is held further out by the centrifugal barrier and
      penetrates less. Predicted to hold on EVERY chain step that offers two or more l at the same Z. Failures counted
      per step, not per table.
PD-3  |Delta| IS NOT MONOTONE IN n AT FIXED l. Predicted: at fixed l, |Delta| rises with Z and the n-ordering is set by
      how much core lies inside. This is stated as the NEGATIVE of PD-2 deliberately — if |Delta| turned out monotone
      in n as well, the decomposition would carry no more information than D itself.

## 2 · The non-penetrating floor — the sharpest claim
PD-4  |Delta| < 1e-3 Ha FOR EVERY CHANNEL WITH l >= l_max + 2, where l_max = the largest l occupied in the reference
      configuration. This is register 1255's centrifugal gate (frac(delta) ~ 0 when l - l_core >= 2, 123 channels,
      median 0.017 against 0.327 below the gate) RESTATED ON Delta AND ON A DIFFERENT INSTRUMENT. If it holds, the
      s39-s40 chain has independently re-derived a gate this project measured from quantum defects, from SCF energies.
PD-5  4f IS NON-PENETRATING FROM Z=12 TO Z=55 AND PENETRATING BY Z=58. Predicted |Delta(4f)| < 1e-3 at every banked Z
      up to and including Cs, and |Delta(4f)| > 0.1 at Ce. THE f COLLAPSE IS A DISCONTINUITY IN Delta AND NOT IN D.
      Falsifiable on four banked Z (12, 19, 20, 55) plus Ce.

## 3 · The ordering clause — that the decomposition is not a relabelling
PD-6  BOTH TERMS ARE LOAD-BEARING. Predicted: among the 19 banked chain steps there is AT LEAST ONE where the entrant
      is NOT the channel of largest |Delta|, and AT LEAST ONE where the entrant is NOT the channel of smallest n.
      If the entrant were always argmax|Delta|, the hydrogenic term would be inert and the law would be pure
      penetration. If it were always argmin n, Delta would be inert and the law would be pure hydrogenic. NEITHER.
PD-7  AND THE n+l ORDERING IS THE COMPETITION BETWEEN THEM. Predicted: at every step, D is minimised by a channel whose
      -1/(2n^2) is NOT the smallest available whenever the smallest-n channel is full or high-l. Stated concretely and
      falsifiably at Z=19: 4s wins over 3d, i.e. the LARGER n wins, and it wins on Delta (-0.11649 vs -0.00251)
      against a hydrogenic term that favours 3d (-0.05556 vs -0.03125) by 0.02431. The hydrogenic term prefers 3d and
      LOSES. That is the 4s-before-3d inversion decomposed, and it says the inversion is entirely a penetration effect.

## 4 · What is NOT predicted here
Nothing about Z > 20 on the chain. No claim that Delta is analytic, has a closed form, or is derivable from n and l
alone — Delta is Z-dependent and that dependence is unmeasured. No claim about g channels beyond the two banked.

## 5 · Held
Arithmetic on the bank only. No SCF, no new field, no constant beyond c, no fitted reference. CORR=False throughout.
