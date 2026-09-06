# FINDING-F392 (s41, addendum) — F39.2 PROMOTED BY MEASUREMENT, REPAIR ATTEMPTED, REPAIR FAILED, AND THE FAILURE RELOCATES THE FAULT

## 1 · THE s41 RULING'S VERDICT IS OVERTURNED FOR Z >= 39, BY DROP CENSUS
M's test was "repair only if it furthers n+l". At Z <= 30 it did not: every dropped channel had n+l
strictly ABOVE the winner's, 0 unsafe on 29 steps. **The census of WHICH channels drop overturns this
prospectively:**
    5d  11/11 = 100%      4d  10/10 at every step since Z=21      5g  6/11      3p  2/15
**The 4d row is Z=39..48, where 4d must WIN.** A channel dropping 100% of the time cannot win, and the
substitute winner (5p or 6s) also sits at n+l = 6, so f392_guard fires UNSAFE and the walk HALTS.
**F39.2 therefore blocks the walk, and is PROMOTED. M was right and my s41 verdict was right only for Z<=30.**

## 2 · REPAIR ATTEMPTED (t7d_node.py) AND IT FAILED — LOGGED, NOT SUPPRESSED
Diagnosis confirmed live: Z=21 4d raises `42 nodes 0` — tgt = n-l-1 = 1, returned 0. The seed is too deep
and the bracket falls to a lower-node state.
Repair built: HFCN(hfc2.HFC) overriding solve_one. Node count identifies a bound state uniquely at fixed l,
so the parent's bracket is correct machinery pointed at the wrong state by its seed; re-seed by walking n'
outward and accept the first return with nd == tgt. Parent kernel only, no reimplemented numerics,
INERT on healthy channels by construction. t7c_hfsr.py / t7b_hf.py NOT edited.
**RESULT: `F39.2 repair exhausted: l=2 n=4 tgt=1 got nd=0`.** No seed in n' = 5..14 returns a 1-node d state.

## 3 · WHAT THE FAILURE MEANS — THE FAULT MAY NOT BE NUMERICS AT ALL
If no seed anywhere yields a 1-node d solution, the likeliest reading is that **4d IS NOT BOUND in the frozen
avg-of-config reference field of neutral Sc**, and the missing state is missing because it does not exist there
— not because the bracket mislaid it. The RuntimeError would then be the field reporting an UNBOUND CHANNEL
through the wrong exception. **This lands exactly on PV-3 (frozen-vs-relaxed, UNBOUNDED), open since s37 and
already load-bearing for the Ac 5f positive Delta.** Two independent routes now terminate on the same object.
**PV-3 IS NO LONGER DEFERRABLE: it is the prerequisite for the 4d row.**
NOT YET DISTINGUISHED, and this is the next measurement: (a) genuinely unbound in the frozen field, vs
(b) bound but outside the bracket's expansion range. Test: probe log-norm sign across a wide e grid at fixed
(l=2, Sc+ frozen potential) and count nodes directly. Cheap, decisive, and it was not reached this session.

## 4 · STATUS
t7d_node.py is sealed as an ATTEMPT WITH A NEGATIVE RESULT. It is NOT wired into nlchain and no chain row was
produced with it. No banked number changed. Gates 1-71 remain byte-identical; f392_guard remains the standing
protection. The walk stands at 29 of 107 and can proceed to Z=31..38 unaffected, because 4d does not need to
win until Z=39.