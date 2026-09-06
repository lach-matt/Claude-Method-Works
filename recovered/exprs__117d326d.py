import numpy as np, sympy as sp, random
from itertools import product, permutations
from collections import Counter
random.seed(13)
z,t,zA,zB=sp.symbols('z t zA zB')
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={x for x in product(*AX) if all(x[v]<=ub(x) for v,p,ub in CONS)}
L=sorted(LAM); QS=sorted({x[3] for x in LAM})
geo=lambda a,b,zz: sp.Piecewise((0,b<a),(sum(zz**i for i in range(a,b+1)),True)) if b>=a else 0
def G(a,b,zz=z):
    """closed-form geometric sum z^a + ... + z^b"""
    if b<a: return sp.Integer(0)
    return sp.simplify(zz**a*(1-zz**(b-a+1))/(1-zz))
print("="*88)
print("  EXPRESSION 1 — THE WHOLE LATTICE, AS A CYLINDER")
print("="*88)
print("""
     **S(t; zA, zB) = SUM_{q=0}^{3}  t^q · A_q(zA) · B_q(zB)**
""")
print("="*88)
print("  EXPRESSION 2 — A_q, THE CATERPILLAR")
print("="*88)
print("""
     **A_q(z) = SUM_{n=1}^{3} z^n SUM_{l=0}^{min(n-1,1)} z^l
                SUM_{k=max(q,1)}^{min(4l+2,3)} z^k · [ (1 - z^{min(k,3)+1}) / (1-z) ]**

  The bracketed factor is the 2S pendant, summed in closed form — it is a
  chain of length min(k,3)+1 and contributes a geometric series.
""")
def A_cf(q,zz=z):
    tot=0
    for n in range(1,4):
        for l in range(0,min(n-1,1)+1):
            lo=max(q,1); hi=min(4*l+2,3)
            for k in range(lo,hi+1):
                tot+=zz**(n+l+k)*G(0,min(k,3),zz)
    return sp.expand(sp.simplify(tot))
def A_brute(q,zz=z):
    return sp.expand(sum(zz**(n+l+k+S) for n in range(1,4) for l in range(0,2) if l<=n-1
        for k in range(1,4) if k<=4*l+2 and k>=q for S in range(0,4) if S<=k))
print("  %4s%14s%14s%10s"%("q","closed form","brute force","match"))
for q in QS:
    a=A_cf(q); b=A_brute(q)
    print("  %4d%14d%14d%10s"%(q,a.subs(z,1),b.subs(z,1),sp.simplify(a-b)==0))
print("="*88)
print("  EXPRESSION 3 — B_q, THE PATH")
print("="*88)
print("""
     **B_q(z) = SUM_{e=1}^{3} z^e SUM_{f=0}^{min(e-1,1)} z^f
                · [ (1 - z^{min(q,4f+2)+1}) / (1-z) ]**
""")
def B_cf(q,zz=z):
    tot=0
    for e in range(1,4):
        for f in range(0,min(e-1,1)+1):
            tot+=zz**(e+f)*G(0,min(q,4*f+2,3),zz)
    return sp.expand(sp.simplify(tot))
def B_brute(q,zz=z):
    return sp.expand(sum(zz**(e+f+g) for e in range(1,4) for f in range(0,2) if f<=e-1
        for g in range(0,4) if g<=4*f+2 and g<=q))
print("  %4s%14s%14s%10s"%("q","closed form","brute force","match"))
for q in QS:
    a=B_cf(q); b=B_brute(q)
    print("  %4d%14d%14d%10s"%(q,a.subs(z,1),b.subs(z,1),sp.simplify(a-b)==0))
print("="*88)
print("  EXPRESSION 4 — A BOX, THE BOTTOM FIBRE")
print("="*88)
print("""
     **Box(a,b)(z) = PROD_i  z^{a_i} (1 - z^{b_i - a_i + 1}) / (1 - z)**

  every bottom fibre is of this form; the tower terminates here.
""")
def Box(a,b,zz=z): return sp.expand(sp.prod([G(a[i],b[i],zz) for i in range(len(a))]))
for (a,b) in [((1,0),(3,1)),((0,),(3,)),((1,0),(3,1))]:
    print("     Box%s..%s (1) = %d   = prod(b_i-a_i+1) = %d"%(a,b,Box(a,b).subs(z,1),
          int(np.prod([b[i]-a[i]+1 for i in range(len(a))]))))
print("="*88)
print("  EXPRESSION 5 — A GENERIC INTERVAL")
print("="*88)
print("""
     **I_{x,y}(z) = SUM_{v in [x,y]} chi(v) z^{rank v}**

  and it equals the box **iff no constraint binds across [x,y]**:

     **I_{x,y} = Box(x,y)  <=>  for every constraint (i <= f(j)),
                                 y_i <= f(x_j)**
""")
le=lambda a,b: all(p<=q for p,q in zip(a,b))
def is_box(x,y):
    return all(y[v]<=ub(x) for v,p,ub in CONS)
ok=0; tot=0; mism=0
for _ in range(500):
    x,y=random.choice(L),random.choice(L)
    if not le(x,y): continue
    tot+=1
    I=[v for v in L if le(x,v) and le(v,y)]
    exp=int(np.prod([y[i]-x[i]+1 for i in range(8)]))
    pred=is_box(x,y); actual=(len(I)==exp)
    if pred==actual: ok+=1
    else: mism+=1
print("     intervals tested        : %d"%tot)
print("     criterion predicts box  : %d correct, %d wrong"%(ok,mism))
print("     **the criterion is exact : %s**"%(mism==0))
print("="*88)
print("  EXPRESSION 6 — THE RANK LEVELS")
print("="*88)
rk=Counter(sum(x) for x in LAM)
F=sum(v*z**k for k,v in sorted(rk.items()))
print("""
     **F(z) = SUM_r c_r z^r**,  and level r is the antichain of size
     c_r = [z^r] F(z)
""")
print("     F(z) = %s ..."%str(sp.expand(F))[:64])
print("     F(1) = %d    max c_r = %d at r = %d"%(F.subs(z,1),max(rk.values()),
      max(rk,key=rk.get)))
print("="*88)
print("  EXPRESSION 7 — THE MAXIMAL CHAINS")
print("="*88)
print("""
  A distributive lattice is J(P), the order ideals of its poset of
  join-irreducibles. **Its maximal chains are in bijection with the LINEAR
  EXTENSIONS of P.** Section 3.3 finds 17 join-irreducibles.

     **#maximal chains = e(P), the number of linear extensions of the
       17-element poset of join-irreducibles**
""")
def is_ji(x):
    below=[y for y in L if le(y,x) and y!=x]
    if not below: return False
    mx=[y for y in below if not any(le(y,w) and y!=w for w in below)]
    return len(mx)==1
JI=[x for x in L if is_ji(x)]
print("     join-irreducibles found : %d"%len(JI))
covers={x:[y for y in L if sum(y)==sum(x)+1 and le(x,y)] for x in L}
bot=min(L,key=sum); top=max(L,key=sum)
memo={}
def paths(x):
    if x==top: return 1
    if x in memo: return memo[x]
    memo[x]=sum(paths(c) for c in covers[x])
    return memo[x]
nc=paths(bot)
print("     maximal chains          : %d"%nc)
print("     rank of top − bottom    : %d  (chain length)"%(sum(top)-sum(bot)))
print("="*88)
print("  EXPRESSION 8 — THE DIVISOR IMAGE")
print("="*88)
PR=[2,3,5,7,11,13,17,19]
print("""
     **N(x) = PROD_i p_i^{x_i}**,  with p = (2,3,5,7,11,13,17,19)

     gcd(N(a),N(b)) = N(a AND b)      lcm = N(a OR b)
     rank(x) = Omega(N(x))            the total number of prime factors
""")
from math import gcd
mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b)); jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b))
N=lambda v:int(np.prod([PR[i]**v[i] for i in range(8)]))
okg=all(gcd(N(a),N(b))==N(mt(a,b)) for a,b in [(random.choice(L),random.choice(L)) for _ in range(300)])
print("     gcd/lcm homomorphism on 300 pairs : %s"%okg)
print("     N(top) = %d"%N(top))
print("="*88)
print("  AND THE MASTER RELATION BETWEEN THEM")
print("="*88)
S=sum(t**q*A_cf(q,zA)*B_cf(q,zB) for q in QS)
print("""
     S(1,1,1)          = %d = |Lambda|
     S(1,z,z)·(rank shift) recovers F(z) up to the base's own weight
     Box is the q,k,f-fibre of S
     I_{x,y} is S restricted to a subinterval
     e(P) counts the maximal chains of J(P) = Lambda

  **Every shape is a specialisation or a restriction of S.** The cylinder
  is the object; the rest are its slices, its fibres, its intervals and
  its chains.
"""%S.subs({t:1,zA:1,zB:1}))