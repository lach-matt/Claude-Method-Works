import re,sympy as sp
src=open('gr-qc_9506083.py').read()
src=src.split('print("E.')[0].replace('sys.exit','pass #')
exec(src)
for xx in (0.1,0.3,0.5):
  for bb in (-1,0,0.5,2):
    A=float(V2w.subs({x:xx,b2:bb})); B=float(wall_Vpp.subs({x:xx,b2:bb}))
    print(xx,bb,A,B,A/B if B else None)
print(sp.factor(sp.numer(sp.together(V27u))), '|', sp.factor(q33))
