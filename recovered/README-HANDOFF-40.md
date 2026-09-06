NEW (s40, gate 74): python3 fkscale.py -> FEASIBLE, interval (0.2145, 0.5298), 315 grid points, ~1 s. RECOMMENDED ADOPTED.
NEW (s40, gate 75): python3 nlchain.py show -> chained score 19/19, FIRST DIVERGENCE none (reads nlchain.jsonl, ~0 s).
Known (s40): nlchain.py is RECORD-FREE from Z=2 and runs above Z=108, where nlwalk_hf.entrant() and hf_chan.py raise
 KeyError. Its reference is the CATION of element Z carrying config(Z-1) -- nuclear charge Z, Z-1 electrons (F40.1).
Known (s40): F39.2 located -- `tgt = n-l-1` is a DEAD VARIABLE in both t7c_hfsr.solve_one and t7b_hf.solve_one; the node
 target is never enforced in the bracket and the check sits one level up at hfc2.py:55. Do NOT edit those two files:
 gates 1-71 must stay byte-identical. The repair goes in a new module and comparison decides.