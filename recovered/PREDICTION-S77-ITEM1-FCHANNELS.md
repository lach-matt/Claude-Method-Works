# PREDICTION — THE FIVE FAILED CHANNELS AT Z=89. FILED BEFORE ANY f-CHANNEL SCAN IS READ.
# Instrument pack77/nodespec77.py. Delta from sealed rt/nodespec.py is FOUR LINES: cache
# redirected to pack77, prediction gate repointed at pack66 (unchanged file, verified sha),
# and the channel filter widened from `l != 2` to `l not in (2,3)`. SCAN GEOMETRY UNTOUCHED.

## WHAT WAS ALREADY IN THE RECORD AND WAS NOT READ (s66, pack66/nodespec.jsonl)
  Z=89 **7d**  tgt 4 nodes ATTAINED, CLASS B, window **[-0.053839, -0.032719] Ha**
  Z=89 **8d**  tgt 5 nodes ATTAINED, CLASS B, window **[-0.028889, -0.022521] Ha**
**Both windows lie an order of magnitude above the winner's D = -0.15762 Ha.** The
argument I said the record did not contain, for two of the five, was already sealed at
s66 and unread. s66 scoped itself to l=2, so 6f, 7f and 8f were never scanned — at any Z.

## PREDICTIONS FOR 6f, 7f, 8f AT Z=89
**N1 CAN-FAIL.** 5f at Z=89 CONVERGED in the walk, so the l=3 path must return
`NO-RAISE / channel converged` for it. **If the widened filter raises on a channel the
walk converged, the instrument is broken and every f row is void.**
**N2 CLASS.** 6f, 7f, 8f return CLASS B or C — the target node count IS attained
somewhere in e<0. *Basis: the d channels at this Z were both B, and a node-count failure
in a Coulombic tail is a shooting failure, not an absence of the state.*
**N3 THE NUMBERS THAT DECIDE THE ROW.** Every window returned lies **above -0.0400 Ha**,
hence far above 6d's -0.15762 Ha and above 7p's -0.12529 Ha.
  *Basis, stated so it can be wrong: 5f converged at -0.03146 Ha, and within one channel
  a state with more radial nodes lies higher in a fixed field. 6f/7f/8f carry 2, 3 and 4
  nodes against 5f's 1.*
**N4 ORDERING CONSEQUENCE.** None of the five changes the entrant. **At most they change
the RANKING below the winner** — 7d at ~-0.05 would sit between 8p (-0.04917) and 8s
(-0.07065), and 8d at ~-0.025 below 5f (-0.03146).

## WHAT THIS CAN AND CANNOT ESTABLISH
A node-spectrum window is a ONE-ELECTRON bracket in a field, **not a converged total
energy and not a lower bound on E^RHF at that occupancy.** Proving 6f lies ABOVE 6d needs
a LOWER bound on the 6f total, and the variational principle gives only upper bounds.
**SO ITEM 1 CAN PRODUCE A STRONG MEASURED ARGUMENT AND CANNOT PRODUCE A PROOF. The proof
is Rung C's, and Rung C is open here and open in the literature.**