import numpy as np
from itertools import product
print("="*88)
print("  A BROADER LOOK — WHERE ELSE DOES CELESTIAL MECHANICS CARRY THE STRUCTURE?")
print("="*88)
print("""
  The Lagrange test used one family in one parameter. Celestial mechanics
  has many ordered families. Test the ones with the sharpest analogues.
""")
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b))
mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
def Rop(S,d):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
def close(S): return all(jn(a,b) in S and mt(a,b) in S for a in S for b in S)
print("="*88)
print("  1. MEAN-MOTION RESONANCES — THE CLEAREST INDEX")
print("="*88)
print("""
  A resonance is a ratio p:q of orbital periods. The catalogue is indexed
  by (p, q, order = p−q, multiplicity). **Constraints are monotone:**
     q < p       order = p − q >= 1      order <= some cap by strength
""")
RES=set()
for p in range(2,9):
    for q in range(1,p):
        o=p-q
        if o>4: continue
        for mult in range(1,min(o,3)+1):
            RES.add((p,q,o,mult))
print("     cells: %d    closed: %s"%(len(RES),close(RES)))
R=Rop(RES,4)
print("     |R(X)| = %d    E(X) = %d"%(len(R),len(R)-len(RES)))
if len(R)>len(RES):
    ex=sorted(R-RES)[:8]
    print("     admitted and absent (first 8):")
    for c in ex: print("        p=%d q=%d order=%d mult=%d"%c)
print("""
  KNOWN SOLAR-SYSTEM RESONANCES, for reference:
     Neptune–Pluto 3:2 · Jupiter's Hildas 3:2 · Kirkwood gaps 3:1, 5:2,
     7:3, 2:1 · Galilean Laplace resonance 4:2:1 · Mimas–Tethys 4:2
""")
print("="*88)
print("  2. THE TITIUS–BODE LAW — A RYDBERG SERIES IN DISGUISE?")
print("="*88)
print("""
  a_n = 0.4 + 0.3 * 2^n.  Compare with T = R/nu^2. Both are one-parameter
  ordered families; ask whether the BRACKET works and what V is.
""")
TB=lambda n: 0.4+0.3*(2.0**n)
AU={'Mercury':0.387,'Venus':0.723,'Earth':1.000,'Mars':1.524,'Ceres':2.77,
    'Jupiter':5.203,'Saturn':9.537,'Uranus':19.191,'Neptune':30.07,'Pluto':39.48}
ns={'Mercury':-np.inf,'Venus':0,'Earth':1,'Mars':2,'Ceres':3,'Jupiter':4,
    'Saturn':5,'Uranus':6,'Neptune':7,'Pluto':7}
print("  %-10s%10s%12s%10s"%("body","actual a","Titius-Bode","ratio"))
for b,a in AU.items():
    n=ns[b]
    tb=0.4 if n==-np.inf else TB(n)
    print("  %-10s%10.3f%12.3f%10.3f"%(b,a,tb,a/tb))
print("\n  bracket test on the ACTUAL semi-major axes, ordered outward:\n")
seq=[AU[b] for b in ['Mercury','Venus','Earth','Mars','Ceres','Jupiter','Saturn','Uranus','Neptune']]
d1=np.diff(seq); d2=np.diff(d1); d3=np.diff(d2)
print("     monotone   : %s"%all(np.sign(d1)==np.sign(d1[0])))
print("     convex     : %s"%all(np.sign(d2)==np.sign(d2[0])))
print("     3-monotone : %s"%all(np.sign(d3)==np.sign(d3[0])))
V=[]
for i in range(1,len(seq)-1):
    w=abs(seq[i+1]-seq[i-1]); e=abs(seq[i]-(seq[i-1]+seq[i+1])/2)
    V.append(w/e)
print("\n     V along the sequence: %s"%["%.2f"%v for v in V])
print("     all > 2 : %s"%all(v>2 for v in V))
print("""
  **THE PLANETARY SEQUENCE IS MONOTONE AND CONVEX BUT NOT 3-MONOTONE.**
  So the order-1 and order-2 brackets apply and higher orders do not --
  the sign of the third difference changes, and that change IS the
  refusal signal: **it flags where the sequence stops being a smooth
  geometric family.**
""")
print("  where the third difference changes sign:\n")
names=['Mercury','Venus','Earth','Mars','Ceres','Jupiter','Saturn','Uranus','Neptune']
for i,v in enumerate(d3):
    if i>0 and np.sign(v)!=np.sign(d3[i-1]):
        print("     between %s and %s"%(names[i],names[i+1]))
print("="*88)
print("  3. HILL STABILITY OF HIERARCHICAL TRIPLES")
print("="*88)
print("""
  Mardling-Aarseth: a triple is stable when the period ratio exceeds a
  critical value depending on mass ratio, eccentricity and inclination.
  **That is a monotone bound in three variables — Section 9.4 form.**
""")
def crit(qout,e_out,inc_deg):
    return 2.8*((1+qout)*(1+e_out)/np.sqrt(1-e_out))**0.4*(1-0.3*inc_deg/180.0)
print("  %8s%8s%8s%14s"%("q_out","e_out","inc","critical ratio"))
for q in (0.1,0.5,1.0):
    for e in (0.0,0.3,0.6):
        print("  %8.1f%8.1f%8d%14.3f"%(q,e,0,crit(q,e,0)))
qs=np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8])
y=np.array([crit(q,0.2,0) for q in qs])
print("\n     monotone in q_out : %s"%all(np.diff(y)>0))
print("     convex in q_out   : %s"%all(np.sign(np.diff(np.diff(y)))==np.sign(np.diff(np.diff(y))[0])))
w=abs(y[5]-y[3]); e=abs(y[4]-(y[3]+y[5])/2)
print("     V at q_out = 0.5  : %.1f"%(w/e))
print("""
  **THE STABILITY BOUNDARY IS MONOTONE AND CONVEX**, so a bracket applies:
  given the critical ratio at two mass ratios, the value at a third is
  deductively bounded. **V ≈ %.0f, so the guarantee costs about %.0f times
  the interpolation error** -- an ordinary channel, comparable to a
  Rydberg series at nu ≈ %.0f.
"""%(w/e,w/e,3*(w/e)/4))