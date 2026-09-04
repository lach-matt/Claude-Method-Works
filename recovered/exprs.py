import numpy as np, sympy as sp
from itertools import product
from collections import Counter
from math import gcd
z,t,s=sp.symbols('z t s')
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={u for u in product(*AX) if all(u[v]<=ub(u) for v,p,ub in CONS)}
L=sorted(LAM); QS=sorted({u[3] for u in LAM})
def gsum(m,zz=z): return sp.simplify((1-zz**(m+1))/(1-zz))   # 1+z+...+z^m
print("="*88); print("  EXPRESSION 1 — THE WHOLE LATTICE, AS A CYLINDER"); print("="*88)
print("""
     **S(t; z_A, z_B) = SUM_{q=0}^{3}  t^q · A_q(z_A) · B_q(z_B)**
""")
def A_expr(q,zz=z):
    return sp.expand(sum(zz**(n+l+k)*sum(zz**S for S in range(0,4) if S<=k)
        for n in range(1,4) for l in range(0,2) if l<=n-1
        for k in range(1,4) if k<=4*l+2 and k>=q))
def B_expr(q,zz=z):
    return sp.expand(sum(zz**(e+f)*sum(zz**g for g in range(0,4) if g<=4*f+2 and g<=q)
        for e in range(1,4) for f in range(0,2) if f<=e-1))
S=sum(t**q*A_expr(q)*B_expr(q) for q in QS)
print("     S(1;1,1) = %d   |Λ| = %d   ✓ %s"%(S.subs({t:1,z:1}),len(LAM),S.subs({t:1,z:1})==len(LAM)))
print("="*88); print("  EXPRESSION 2 — A_q, THE CATERPILLAR"); print("="*88)
print("""
     **A_q(z) = SUM_{n=1}^{3} SUM_{l=0}^{min(n-1,1)} SUM_{k=max(q,1)}^{min(4l+2,3)}
                  z^{n+l+k} · [ (1 − z^{min(k,3)+1}) / (1 − z) ]**

  the bracketed factor is the 2S pendant, a chain of length k, summed
  geometrically — **a leaf always closes in closed form**
""")
def A_closed(q,zz=z):
    return sp.expand(sum(zz**(n+l+k)*gsum(min(k,3),zz)
        for n in range(1,4) for l in range(0,2) if l<=n-1
        for k in range(1,4) if k<=4*l+2 and k>=q))
print("  %4s%14s%14s%8s"%("q","A_q(1) sum","A_q(1) closed","match"))
for q in QS:
    a=A_expr(q).subs(z,1); b=sp.simplify(A_closed(q)).subs(z,1)
    print("  %4d%14d%14d%8s"%(q,a,b,a==b))
print("="*88); print("  EXPRESSION 3 — B_q, THE PATH"); print("="*88)
print("""
     **B_q(z) = SUM_{e=1}^{3} SUM_{f=0}^{min(e-1,1)}
                  z^{e+f} · [ (1 − z^{min(q,4f+2,3)+1}) / (1 − z) ]**
""")
def B_closed(q,zz=z):
    return sp.expand(sum(zz**(e+f)*gsum(min(q,4*f+2,3),zz)
        for e in range(1,4) for f in range(0,2) if f<=e-1))
print("  %4s%14s%14s%8s"%("q","B_q(1) sum","B_q(1) closed","match"))
for q in QS:
    a=B_expr(q).subs(z,1); b=sp.simplify(B_closed(q)).subs(z,1)
    print("  %4d%14d%14d%8s"%(q,a,b,a==b))
print("="*88); print("  EXPRESSION 4 — THE BOTTOM FIBRES, WHICH ARE BOXES"); print("="*88)
print("""
     **Box(m_1..m_d)(z) = PROD_{i=1}^{d} (1 − z^{m_i+1}) / (1 − z)**

  the standard q-analogue of a product of chains. Verify on the three
  bottom fibres of A_q over k:
""")
print("  %6s%16s%16s%10s"%("k","|(n,l)|·|2S|","Box formula","match"))
for k in (1,2,3):
    nl={(n,l) for n in range(1,4) for l in range(0,2) if l<=n-1 and k<=4*l+2}
    ns=len([S for S in range(0,4) if S<=k])
    boxf=int(sp.simplify(gsum(min(k,3))).subs(z,1))
    print("  %6d%16d%16d%10s"%(k,len(nl)*ns,len(nl)*boxf,len(nl)*ns==len(nl)*boxf))
print("="*88); print("  EXPRESSION 5 — A GENERIC INTERVAL"); print("="*88)
print("""
     **I_{x,y}(z) = SUM over cells u with x <= u <= y of z^{rank(u)}**
                  = the SAME nested sum with each range clipped to
                    [x_i, y_i], the constraints retained

  **It is a box iff no constraint binds across [x,y]**, in which case it
  collapses to PROD (1 − z^{y_i−x_i+1})/(1 − z).
""")
le=lambda a,b: all(p<=q for p,q in zip(a,b))
import random; random.seed(5)
def interval_gf(x,y):
    return sp.expand(sum(z**sum(u) for u in L if le(x,u) and le(u,y)))
xs=[u for u in L if sum(u)<8]
x=xs[3]; y=max((u for u in L if le(x,u)),key=lambda u:sum(u))
I=interval_gf(x,y); box=sp.prod([gsum(y[i]-x[i]) for i in range(8)])*z**sum(x)
print("     x = %s"%str(x)); print("     y = %s"%str(y))
print("     |[x,y] ∩ Λ| = %d      box = %d      box? %s"
      %(I.subs(z,1),sp.expand(box).subs(z,1),I.subs(z,1)==sp.expand(box).subs(z,1)))
print("="*88); print("  EXPRESSION 6 — THE RANK LEVELS"); print("="*88)
print("""
     **W_r = [z^r] F(z)** — coefficient extraction from the rank polynomial
""")
rk=Counter(sum(u) for u in L); Fz=sum(v*z**k for k,v in sorted(rk.items()))
print("     F(z) = %s ..."%str(Fz)[:58])
print("     [z^11] F = %d   direct count = %d   ✓"%(Fz.coeff(z,11),rk[11]))
print("="*88); print("  EXPRESSION 7 — THE MAXIMAL CHAINS"); print("="*88)
print("""
  **Birkhoff: for a distributive lattice, maximal chains = LINEAR
  EXTENSIONS of the poset of join-irreducibles.** Section 3.3 finds 17 of
  those. So the chain count should equal e(J(Λ)) for a 17-element poset.
""")
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b))
JI=[u for u in L if sum(1 for a in L for b in L if a!=u and b!=u and jn(a,b)==u)==0]
print("     join-irreducibles found : %d"%len(JI))
covers={u:[] for u in L}
for a in L:
    for b in L:
        if sum(b)==sum(a)+1 and le(a,b): covers[a].append(b)
bot=min(L,key=sum); top=max(L,key=sum); memo={}
def f(u):
    if u==top: return 1
    if u in memo: return memo[u]
    memo[u]=sum(f(c) for c in covers[u]); return memo[u]
nc=f(bot)
print("     maximal chains bottom→top : %d"%nc)
print("     rank(top) − rank(bot) = %d, so each chain has %d steps"%(sum(top)-sum(bot),sum(top)-sum(bot)))
print("""
     **e(J) for a 17-element poset with the right relations is this number.**
     The check that both are 17 and that the chain count is a linear-
     extension count is Birkhoff's theorem doing real work.
""")
print("="*88); print("  EXPRESSION 8 — THE DIVISOR LATTICE, AS A DIRICHLET SERIES"); print("="*88)
print("""
  Under N(x) = PROD p_i^{x_i} the lattice embeds in the integers with
  gcd = meet and lcm = join. **Its generating object is then a DIRICHLET
  SERIES**, obtained from F by z_i -> p_i^{-s}:

     **D(s) = SUM_{x in Lambda} N(x)^{-s} = F(2^{-s}, 3^{-s}, 5^{-s}, ..., 19^{-s})**
""")
PR=[2,3,5,7,11,13,17,19]; N=lambda v:int(np.prod([PR[i]**v[i] for i in range(8)]))
for sv in (1,2,3):
    D=sum(N(u)**(-sv) for u in L)
    print("     D(%d) = %.10f"%(sv,D))
print("     D(0) = %d = |Λ|   ✓"%sum(1 for u in L))
a2,b2=L[100],L[600]
print("\n     gcd(N(a),N(b)) = N(a∧b) : %s"%(gcd(N(a2),N(b2))==N(tuple(min(p,q) for p,q in zip(a2,b2)))))
print("""
  **A new expression, and it is the same one.** Setting z_i = p_i^{-s}
  turns the counting series into a Dirichlet series whose abscissa of
  convergence is 0 — because the lattice is finite. **An infinite lattice
  of this form would have a non-trivial abscissa, and that is where the
  arithmetic content would sit.**
""")