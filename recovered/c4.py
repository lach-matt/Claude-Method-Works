import sys; sys.path.insert(0,"/home/claude/work")
from fractions import Fraction as F
import numpy as np
LCODE={'s':0,'p':1,'d':2,'f':3,'g':4,'h':5,'i':6}
def lev(tag):
    nr=int(tag[0]); l=LCODE[tag[1]]; num,den=tag[2:].split('/')
    j=F(int(num),int(den)); N=2*(nr-1)+l
    S=(j*(j+1)-l*(l+1)-F(3,4))/2
    return dict(tag=tag,l=l,j=j,N=N,S=S)
BASE=["1s1/2","1p3/2","1p1/2","1d5/2","2s1/2","1d3/2","1f7/2","2p3/2","1f5/2",
      "2p1/2","1g9/2","1g7/2","2d5/2","2d3/2","3s1/2","1h11/2","1h9/2","2f7/2",
      "1i13/2","3p3/2","2f5/2","3p1/2"]
def constraints(order):
    """each consecutive pair gives  b*dA + a*dS' < dN ;  return the rows."""
    rows=[]
    for x,y in zip(order,order[1:]):
        X,Y=lev(x),lev(y)
        dA=F(X['l']*(X['l']+1)-Y['l']*(Y['l']+1))
        dS=Y['S']-X['S']
        dN=Y['N']-X['N']
        rows.append((dA,dS,dN))
    return rows
def feasible(rows):
    """is there (b,a) with b*dA + a*dS < dN for every row? 2-D LP by scan."""
    import math
    best=None
    for k in range(2000):
        th=k*math.pi/1000.0
        for r in (0.5,1,2,5,10,50,200):
            b,a=r*math.cos(th),r*math.sin(th)
            if all(float(dA)*b+float(dS)*a < float(dN)-1e-12 for dA,dS,dN in rows):
                return True,(b,a)
    return False,None
def swap(order,x,y):
    o=order[:]; i,j=o.index(x),o.index(y); o[i],o[j]=o[j],o[i]; return o
print("  C4 — THE NEAR-DEGENERATE SWAPS. a form surviving EITHER ordering is robust.\n")
tests=[("as validated (Krane/Wong)", BASE),
       ("swap 2f7/2 <-> 1h9/2",      swap(BASE,"1h9/2","2f7/2")),
       ("swap 3p3/2 <-> 2f5/2",      swap(BASE,"3p3/2","2f5/2")),
       ("both swapped",              swap(swap(BASE,"1h9/2","2f7/2"),"3p3/2","2f5/2"))]
for lab,o in tests:
    rows=constraints(o)
    ok,sol=feasible(rows)
    print(f"  {lab:<28} {len(rows)} constraints   "
          f"{'FEASIBLE  b=%.3f a=%.3f'%sol if ok else 'EMPTY — family refuted'}")
print("\n  and the six degenerate pairs under each ordering — do they still")
print("  collapse to 4β+α with both signs?\n")
PAIRS=[("2s1/2","1d3/2"),("2p3/2","1f5/2"),("3p3/2","2f5/2"),
       ("2d3/2","3s1/2"),("1g7/2","2d5/2"),("1h9/2","2f7/2")]
for lab,o in tests:
    senses=[]
    for x,y in PAIRS:
        if x not in o or y not in o: continue
        i,j=o.index(x),o.index(y)
        X,Y=(lev(x),lev(y)) if i<j else (lev(y),lev(x))
        dA=float(X['l']*(X['l']+1)-Y['l']*(Y['l']+1))
        dS=float(Y['S']-X['S'])
        if abs(dS)<1e-12: continue
        senses.append(1 if dA/dS>0 else -1)
    print(f"      {lab:<28} senses {sorted(set(senses))}"
          f"   {'BOTH' if len(set(senses))>1 else 'one'}")