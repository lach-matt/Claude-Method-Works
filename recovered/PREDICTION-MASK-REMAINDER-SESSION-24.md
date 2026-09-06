# PREDICTION — bridge-24 s3(2): the TS-mask remainder (ratio 1.44 vs PZ exchange scaling 1.0), session 24. Written BEFORE the run.
Object: t7c_cuaudit.py + env CSIC_ENT (default 1 = standing): CSIC_ENT=0 removes the correlation SIC on the ENTRANT channel only
(siblings unchanged), so only the f-dependence of the entrant's own SIC changes. Test D grid on Sc (ratio 1.25) and Yb (ratio 1.44).
PM1: with CSIC_ENT=0 the ratio (DE_J - eps(1/2)) / (-0.0583 |E_x[n_ent]|) falls to [0.95, 1.15] on both rows -- the remainder is the
     correlation SIC's own curvature in f (LDA eps_c[f n] is not homogeneous in f).
PM2: eps(1/2) itself moves by < 0.004 on both rows (the correlation SIC of a half-density is small); DE_J moves by more than eps(1/2) does.
Alternative if PM1 fails with ratio unchanged (>1.3): the remainder is total-density LSD-x/c curvature + relaxation, not the SIC.
Thresholds stated. 14 SCF; timeout 200; rows keyed (Z,'D0',f) in t7c_ownshell.jsonl.