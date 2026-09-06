# PREDICTION-CHAIN-LIGHT (s40, item 1a) — WRITTEN BEFORE nlchain.py EXISTS AND BEFORE ANY ROW IS RUN (R 1449).
Object: the chain of SPEC-CHAIN §2 run on the RULING FIELD (hfc2, SR, CORR=False) from the seed config(1)=1s to Z=20.
The light end is taken first because it is where a reverse derivation to Schrodinger must anchor, because it is cheapest
(banked hf_chan sec: Li 1-2 s, Na 5 s, K 5-14 s per channel), and because F39.2 sits inside it at Z=11.
Record configurations RECALLED-NOT-ENTERED, comparison column only.

## 0 · MACHINERY GATE, to pass BEFORE any chain result is read (PE-0 / PT8 pattern, can-fail)
PC-0  Where the chain's reference config(Z-1) COINCIDES with hf_chan's ion (= ground(Z) minus entrant), D_chain MUST
      reproduce the banked D_HF_rel to 5 dp. Three coincidences exist in the light end and all three are banked:
        Li  2s -0.19629 · 2p -0.12862      (ref 1s2 = ground(2))
        Na  3s -0.18217                    (ref Ne  = ground(10))
        K   4s -0.14774 · 3d -0.05807 · 4p -0.09363   (ref Ar = ground(18))
      Any disagreement is a fault in the reference or the occupancy builder, NOT a result. 6 of 6 required.

## 1 · The chain against the record, Z = 2..20
PC-1  THE CHAIN REPRODUCES THE OBSERVED CONFIGURATION AT EVERY Z FROM 2 TO 20. FIRST DIVERGENCE: NONE below Z=21.
      Ground: there is no Madelung exception below Sc (Z=21) in the observed table, and s39 already derived the ns-over-
      (n-1)d ordering at K on this exact field (PE-1, margin 0.0897 Ha). 19 of 19 steps.
PC-2  IF PC-1 FAILS, THE FIRST DIVERGENCE IS AT Z=19 OR Z=20 AND NOWHERE EARLIER. Below Z=19 no d channel is open in
      competition (3d first becomes a candidate at Z=11 under the §4 rule but lies far above 3s/3p); the first genuine
      cross-shell competition in the table is 4s against 3d. A divergence at Z<=18 would indict the field or the
      candidate rule, not the physics, and must be reported as such.
PC-3  THE MARGIN AT EACH STEP IS LARGE AT SHELL INTERIORS AND SMALL AT SHELL EDGES. Predicted |m| >= 0.05 Ha at every
      step inside a subshell, and the three smallest margins of the run are at Z=19 (4s/3d), Z=5 (2p opening against 3s)
      and Z=13 (3p opening). This is PW-4 restated for the chain and is the quantity the law rests on.

## 2 · F39.2, predicted to fire and predicted to fire in a named way
PC-4  AT Z=11 THE CANDIDATE SET CONTAINS 3p, AND F39.2 FIRES. s39 registered: Na 3p fails the node check (nd=0, expected
      1 — the SCF fell to a 2p-like solution). Predicted: the same failure, same signature, reached by a different driver.
      If it does NOT fire under the chain's reference, then F39.2 is a fault of hf_chan's ION reference and not of the
      3p channel itself, and that is the more useful outcome — it would localise the fault to the reference, not the SCF.
PC-5  THE REPAIR IS AN INITIAL-GUESS / NODE-CONSTRAINT PROBLEM, NOT A FIELD PROBLEM. Predicted: 3p converges to a
      1-node solution when started from a hydrogenic 3p guess or when the node count is enforced, and its D lies between
      3s and 3d. If instead no 1-node bound solution exists on this field at Na, the SR-HF field does not bind Na 3p and
      the light-end anchor has a real hole, which would be a finding against the field and must be reported as one.

## 3 · What is NOT predicted here
Nothing above Z=20. Nothing about 5g. No Z>108 row is run in this file's scope. The heavy segment and the Janet-120
extension are separate files with their own predictions, written before their own runs.

## 4 · Held
No terms, no SO, no correlation, no F^k scale, no intermediate coupling. CORR=False. No constant beyond c.
Cost unknown at filing; the run is segmented cheapest-first and the segmentation is reported.
