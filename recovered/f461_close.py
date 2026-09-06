"""f461_close.py -- F46.1 closing test.
maxit=100 is a CHOSEN parameter of the ruling field (s45 figures list). This
script does NOT change it for the chain; it varies it as a DIAGNOSTIC to decide
between two accounts of D_6p(54)=+0.11105:
  (A) a real unbinding of the 6p channel at Z=54;
  (B) a total energy read off an SCF that had not converged when run2 returned.
(A) predicts the value is stable as maxit rises. (B) predicts it moves and
settles near the 6p eigenvalue, -0.0795, continuing -0.07617, -0.07922.
Comparison decides.
"""
import os, sys, json, time
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
import hfc2 as H
from t7c_kernel import C0
import nlchain as NC
H.CORR = False

Z = 54
rows = {d['Z']: d for d in map(json.loads, open('nlchain.jsonl'))}
cfg = NC.cfg_from_chain(Z - 1, rows)
c6p = (6, 1)

print("maxit  beta      E_ref          E_6p           D_6p       it   eps_6p")
for maxit, beta in [(100, 0.4), (300, 0.4), (600, 0.4), (600, 0.2)]:
    t = time.time()
    Er, _, itr, _ = H.HFC(Z, [tuple(x) for x in cfg], c=C0).run2(beta=beta, maxit=maxit)
    E, _, it, eps = H.HFC(Z, [tuple(x) for x in NC.add(cfg, c6p)],
                          c=C0).run2(beta=beta, maxit=maxit)
    print(f"{maxit:>5}  {beta:<4}  {Er:.6f}  {E:.6f}  {E-Er:+.5f}  {it:>4}  "
          f"{eps[c6p]:+.6f}   {'HIT MAXIT' if it >= maxit else 'CONVERGED'}"
          f"  ({int(time.time()-t)}s)", flush=True)
