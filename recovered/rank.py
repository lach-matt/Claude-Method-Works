import sys; sys.path.insert(0,"/home/claude/work")
from fractions import Fraction as F
from sixpair_screen import level, PAIRS, woods_saxon, tensor, eff_mass
import numpy as np

# The corridor constraint with a candidate term:
#     beta*dA + alpha*dS' + gamma*dT  <  0        (dN = 0 on all six)
# On these pairs dA = 4*dS', so the first two collapse to (4b+a)*dS'.
# Write s = 4b+a. Feasibility needs (s, gamma) with
#     dS'_i * s + dT_i * gamma < 0   for all six.
# That is a 2-D linear feasibility problem — SOLVE it, don't guess from signs.
def feasible(dS, dT):
    """is there (s, gamma) with dS_i*s + dT_i*gamma < 0 for every i?
    2-D homogeneous strict system: feasible iff the vectors (dS_i, dT_i) all lie
    strictly within some open half-plane."""
    V=[(float(a),float(b)) for a,b in zip(dS,dT)]
    for k in range(3600):
        th=k*np.pi/1800.0
        u=(np.cos(th),np.sin(th))
        if all(a*u[0]+b*u[1] < -1e-12 for a,b in V): return True,u
    return False,None

def deltas(fn):
    dS,dT=[],[]
    for a,b,_ in PAIRS:
        x,y=level(a),level(b)
        dS.append(y['S']-x['S'])
        dT.append(fn(x)-fn(y))
    return dS,dT

print("  THE SCREEN, DONE PROPERLY — 2-D linear feasibility, not sign-matching\n")
CANDS=[("Woods-Saxon  N(N+3)",woods_saxon),("tensor  <S12>",tensor),
       ("eff. mass  (N+3/2)l",eff_mass),
       ("CONTROL l(l+1)",lambda x: F(x['ell']*(x['ell']+1))),
       ("CONTROL <L.S>",lambda x: x['S']),
       ("CONTROL none (gamma=0)",lambda x: F(0))]
for name,fn in CANDS:
    dS,dT=deltas(fn)
    ok,u=feasible(dS,dT)
    prop = "proportional to dS" if all(
        (dT[0]*dS[i]==dT[i]*dS[0]) for i in range(6)) else ""
    print(f"  {name:<26}{'FEASIBLE' if ok else 'still empty':<14}{prop}")
    if ok: print(f"  {'':<26}e.g. 4b+a = {u[0]:+.3f}, gamma = {u[1]:+.3f}")