# FINDING — node split (PREDICTION-NODESPLIT-SESSION-30): the inner lobe is NOT the d-row discriminator.  s30. Files: nodesplit.py, nodesplit.jsonl.
row  nodes r_node  Q_in    B        B_in      B_in/B  A_frz     A_in      A_in/A  excess   B_in/excess
Y    1     0.611   0.019   0.006098 0.000315  0.052   -0.03554  -0.00205  0.058   0.0102   0.031
La   2     0.949   0.030   0.004420 0.000343  0.078   -0.03194  -0.00285  0.089   0.0072   0.048
Lu   2     0.688   0.017   0.005246 0.000225  0.043   -0.03355  -0.00182  0.054   0.0083   0.027
Sc   0     —       0       0.011046 0         0       -0.04866  0         0       0.0014   0   (control)
PQ1 FAILED (Q_in 0.017-0.030, below 0.03 on two rows: the inner lobes hold 2-3 % of the entrant). PQ2 FAILED (B_in/B 0.04-0.08, not 0.2-0.6).
PQ3 FAILED: B_in 0.0002-0.0003 Ha, ten times below the committed [0.002,0.005]; B_in/excess 0.03-0.05. Flat-ish, but 3-5 % of the object. PQ4 FAILED (0.05-0.09).
Decision by the rule: the node is REFUSED as the class discriminator. Whatever separates nd>=4 from 3d, it is not the inner lobe's self-correlation nor its share
of the total-density term. Reading (not a claim): the frozen single-SCF A (-0.032 to -0.049) exceeds the two-SCF ΔA of drow_p (-0.020 to -0.031) by ~60 %:
core relaxation along the ionisation path carries a large part of the local correlation change — the same signal as PP3 (R ~ -0.65 B).
Build error on record: node detection counted tail sign noise (Sc 2 'nodes' at r>27, Lu 4) — caught on the nodeless control, amplitude mask added, two rows rerun.
No timing flag on the predictions (all written before the first run). Gate: python3 nodesplit.py 39 57 71 21 -> must SKIP all; if Y deleted reprints B_in 0.000315.
Candidate (ii) of COMPARE-DROW is closed. The d-row excess remains a NEW OBJECT with no candidate on the table beyond the class statement.