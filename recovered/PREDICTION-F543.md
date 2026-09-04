# PREDICTION-F543 -- CLOSING F54.3 (rung 1 engaged at Z=88 on the c=1e6 walk)
FILED BEFORE ANY ROW IS COMPUTED.  R 1449.

## RECORD ALREADY READ (declared, NOT predicted)
pack54/c3.jsonl Z=88 was read before this file was written.  It states:
  rung_ref = 0 ; chan['7s'].rung = 0 ; chan['6d'].rung = 0 ; chan['5f'].rung = 1
  order[0]=7s -0.14359, order[1]=6d -0.13478, 5f -0.03154 (6th), margin 0.00881
These are declarations from the record.  They are not scored as predictions.

## PREDICTIONS (scored by pack55/gate90.py)
F3-1  Re-running channel 5f at Z=88, c=1e6, with the ladder TRUNCATED to rung 0
      only (beta=0.4, maxit=100) returns conv=False, it=100.  It does not
      converge at rung 0.  A number for it at rung 0 does not exist.
F3-2  Re-running 7s and 6d at Z=88, c=1e6, rung 0 only, converges (conv=True,
      it<100) and reproduces D_ent=-0.14359 and D_6d=-0.13478 to +/-1e-5.
F3-3  Therefore margin(Z=88) = 0.00881 +/- 2e-5 and ent=7s, computed with NO
      rung-1 solve anywhere in the comparison.
F3-4  The rung-0 LAST ITERATE of 5f (the cycling value, recorded not used) is
      shallower than -0.06 Ha, i.e. it could not have entered the 7s/6d decision
      at any rung.
F3-5  The reference solve reproduces at rung 0 with it=34.

## RULING SOUGHT
If F3-1..F3-5 hold, F54.3 CLOSES with this finding: the rung-1 engagement at Z=88
touched ONE channel that is 110 mHa below the decision and is excluded from it.
The Z=88 entrant is a pure rung-0 result of the ruling field.  Nothing in C3-1
rests on a rung-1 solve.
If F3-2 fails, Z=88 is withdrawn from the c3 table pending recomputation.