# FINDING-CHAIN (s40) — THE SELF-DRIVING WALK RUNS, AND THE ORDERING SEPARATES INTO A HYDROGENIC TERM AND A PENETRATION TERM.

## 0 · What was built
nlchain.py (new, pack40). config(Z+1) = config(Z) + one electron in the channel minimising E_HF, on the ruling field
(hfc2, SR, CORR=False). Reference = the CATION of element Z carrying config(Z-1). Seed config(1) = 1s, CHOSEN and declared.
RECORD-FREE FROM Z=2: ground.py is read only for the comparison column. Runs above Z=108 by construction, where
nlwalk_hf.entrant() and hf_chan.py both raise KeyError. Candidate rule per SPEC-CHAIN §4; NO n+l anywhere in it.

## 1 · F40.1, REGISTERED, CAUGHT IN SMOKE TEST BEFORE ANY RESULT WAS READ
First build put the reference at nuclear charge Z-1, making D a total-energy difference between two DIFFERENT ATOMS rather
than a binding energy. Detected by PC-0 on its first row: Li 2s came back -4.5717 against the banked -0.19629. Three rows
purged and re-run. Affects no result. THE GATE CAUGHT IT ON THE FIRST NUMBER IT SAW, which is what PC-0 was written for.

## 2 · PC-0 MACHINERY GATE: 6/6 EXACT TO 5 dp
Li 2s -0.19629 · 2p -0.12862 · Na 3s -0.18217 · K 4s -0.14774 · 3d -0.05807 · 4p -0.09363. All six reproduce the banked
hf_chan D_HF_rel exactly at the three Z where the chain's reference coincides with hf_chan's ion. Results readable.

## 3 · PC-1 HELD. 19/19. FIRST DIVERGENCE: NONE.
Seeded at hydrogen and given no record, the chain reproduces the OBSERVED ground configuration at every Z from 2 to 20.
This is aufbau PERFORMED, not assumed. It is the first time in this project that the filling sequence has been produced
rather than read, and it is produced on a parameter-free scalar-relativistic HF field with no constant beyond c.
Scope stated plainly: Z <= 20, no Madelung exception in range, and the chain has no reset — see SPEC §5.

## 4 · PC-3 PARTLY FAILED, AND THE FAILURE FOUND THE REAL LAW
HELD: |m| >= 0.05 Ha at every step (minimum 0.05411 at Z=19).
FAILED: I predicted the three smallest margins at Z=19, Z=5, Z=13. Measured: Z=19 (0.05411), Z=20 (0.06058), Z=3 (0.06767).
Z=19 right; Z=5 (0.17686) and Z=13 (0.10460) wrong, and both are in the upper half. I reasoned that subshell OPENINGS have
small margins. They do not: p-openings have LARGE margins.
UNPREDICTED AND REGISTERED — THE MARGIN LAW: m GROWS MONOTONICALLY AS A SUBSHELL FILLS AND RESETS TO ITS MINIMUM AT EACH
NEW ns OPENING. 2p run: 0.177 0.239 0.307 0.383 0.466 0.556. 3p run: 0.105 0.153 0.207 0.266 0.331 0.401. Both strictly
increasing, six of six. 4s: 0.054 0.061. 2s: 0.068 0.096. ONE EXCEPTION: the 3s run reads 0.127 then 0.093, DECREASING —
and that is the row F39.2 corrupts (see §6). The law predicts Na's true margin is BELOW 0.09346; the repair can test it.

## 5 · THE RESULT — D SEPARATES INTO A HYDROGENIC TERM AND A PENETRATION TERM, WITH NO FITTED REFERENCE
TIMING FLAG (R 1449): THIS FINDING PRECEDES ITS PREDICTION. It was not predicted in PREDICTION-CHAIN-LIGHT and is
registered as arrived-at-in-scoring. It owes a prediction file before any further row is run on it.
    D(n,l) = -1/(2n^2) + Delta(n,l),   Delta = D - hydrogenic,   Delta <= 0
The reference -1/(2n^2) is the hydrogenic value at unit effective charge. IT IS NOT FITTED AND CONTAINS NO PARAMETER.
Measured Delta, Z=19 (K):  4s -0.11649 · 4p -0.06238 · 3d -0.00251 · 4d -0.00157 · 4f  0.00000
Measured Delta, Z=20 (Ca): 4s -0.15766 · 4p -0.09708 · 3d -0.04187 · 4d -0.01315 · 4f -0.00007 · 5f -0.00005 · 5g 0.00000
  · 4f AT K IS ZERO TO 5 dp. 5g AT Ca IS ZERO TO 5 dp. The high-l channels sit EXACTLY on the hydrogenic value: they do
    not penetrate the core at all, and they see a fully screened nucleus of charge 1.
  · Delta IS MONOTONE IN l AT FIXED Z, across every row measured.
  · The hydrogenic term is a pure function of n and is IDENTICAL FOR ALL l AT THE SAME n. THEREFORE THE ENTIRE
    l-DEPENDENCE OF THE ORDERING LIVES IN Delta, AND Delta IS PENETRATION. This is PW-6 (s39) — "the ordering mechanism
    is RADIAL, NOT ANGULAR" — now measured directly against a parameter-free reference rather than inferred from the
    class-flatness of the term/SO/correlation objects.
AND THE f COLLAPSE IS A JUMP IN Delta, NOT IN D. Banked 4f: Delta = -0.00002 at Cs (Z=55) and -0.33575 at Ce (Z=58).
Zero penetration through Z=55, then a fall of 0.336 Ha in three protons. Bridge item 4 (the Cs->Ba->La->Ce trace) now has
its instrument: run it on Delta, not on D.

## 6 · F39.2 LOCATED — A DEAD VARIABLE IN TWO SOLVERS
PC-4 HELD: 3p fails at Z=11 under the chain driver, same signature as s39 (nodes 0, expected 1), reached by a different
driver. It also fails at Z=10, and 5d fails at Z=20 (nodes 1, expected 2) — THREE instances, not one.
MECHANISM, located by reading: in BOTH t7c_hfsr.solve_one and t7b_hf.solve_one, `tgt = n-l-1` is computed on the first
line of the function AND NEVER USED AGAIN. The eigenvalue search is a pure bracket on log(norm) with NO node constraint,
so it can converge on a lower-n state of the same l. The node check that catches it sits one level up, at hfc2.py:55,
AFTER the fact. That is why the failure is intermittent — it depends on where the bracket happens to land.
STATUS CORRECTED FROM s39: F39.2 does affect one reported number. The Z=11 margin (0.1265) is computed against 3d because
3p is absent, and is therefore an OVERSTATEMENT. It does not change any entrant choice: 2p wins at Z=10, 3s at Z=11,
4s at Z=20, none of them the failed channel. 19/19 stands.
REPAIR IS NOT A ONE-LINE EDIT AND WAS NOT ATTEMPTED. t7c_hfsr and t7b_hf are gated machinery (gates 5, 13 among others)
and gates 1-71 must stay byte-identical. The repair belongs in a NEW module reimplementing the bracket with the node
target enforced, run side by side, COMPARISON DECIDES. Next session, with its own prediction file.

## 7 · Held / not in this run
No terms, no SO, no correlation, no F^k scale, no intermediate coupling. CORR=False. No constant beyond c. No Z > 20 run.
No literature configuration entered any file. Nothing written to register/index/store. Bank 2_13 (R 1700) untouched.
