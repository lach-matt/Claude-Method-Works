import numpy as np
from itertools import combinations
R=109737.3
T=lambda v: R/v**2
print("="*76)
print("  THE k-TH ORDER BRACKET, DEFINED FROM THE ORDER PROPERTY ALONE")
print("="*76)
print("""
  LATTICE FACT: for T = R/nu^2 every derivative has known sign,
  sign(f^(j)) = (-1)^j.  That is an ORDER property, checkable on data as
  the sign of the j-th finite difference -- no fit, no smoothness beyond
  a sign.

  CLASSICAL INTERPOLATION ERROR with k+1 nodes x_0..x_k:

        f(x) - p_k(x) = f^(k+1)(xi)/(k+1)! * prod_i (x - x_i)

  At x = n: a node at n+j contributes (n-(n+j)) = -j < 0
            a node at n-j contributes (n-(n-j)) = +j > 0

  So with m of the k+1 nodes ABOVE n,   sign(prod) = (-1)^m,  and

        sign( f(n) - p(n) ) = (-1)^(k+1) * (-1)^m = (-1)^(k+1+m)

  THEREFORE:
     k+1+m EVEN  =>  f(n) > p(n)  =>  p is a LOWER bound
     k+1+m ODD   =>  f(n) < p(n)  =>  p is an UPPER bound

  **A DEDUCTIVE TWO-SIDED BRACKET AT EVERY ORDER, BY CHOOSING m.**
""")
def poly_at(nodes,n):
    ys=[T(x) for x in nodes]
    c=np.polyfit(nodes,ys,len(nodes)-1)
    return np.polyval(c,n)
def bracket_k(n,k,hmax=None):
    """k-th order deductive bracket: k+1 nodes, m above chosen for each side"""
    lo,hi=-np.inf,np.inf
    best=None
    for m in range(0,k+2):
        below=k+1-m
        if m>0 and below<0: continue
        nodes=[n+j for j in range(1,m+1)]+[n-j for j in range(1,below+1)]
        if len(nodes)!=k+1: continue
        if min(nodes)<2: continue
        p=poly_at(sorted(nodes),n)
        if (k+1+m)%2==0: lo=max(lo,p)
        else:            hi=min(hi,p)
    return lo,hi
print("  %5s%6s%16s%16s%14s%10s"%("nu","k","lower","upper","width","holds?"))
for n in (20,40,80):
    for k in (1,2,3,4,5):
        lo,hi=bracket_k(n,k)
        w=hi-lo
        ok = lo<=T(n)<=hi
        print("  %5d%6d%16.8g%16.8g%14.6g%10s"%(n,k,lo,hi,w,ok))
    print()
print("="*76)
print("  DOES IT CONTAIN, ALWAYS?")
print("="*76)
tot=0; bad=0
for n in range(8,120):
    for k in (1,2,3,4,5):
        lo,hi=bracket_k(n,k); tot+=1
        if not (lo<=T(n)<=hi): bad+=1
print("\n  containments tested : %d"%tot)
print("  failures            : %d"%bad)
print("  **%s**"%("ALL HOLD" if bad==0 else "FAILS"))
print("="*76)
print("  AND NOW THE QUESTION: DOES V STAY BOUNDED AT MATCHED ORDER?")
print("="*76)
def est_err(n,k):
    nodes=[n+j for j in range(1,(k+1)//2+1)]+[n-j for j in range(1,(k+2)//2+1)]
    nodes=sorted(nodes)[:k+1]
    return abs(poly_at(nodes,n)-T(n))
print("\n  %5s%6s%16s%16s%14s"%("nu","k","bracket width","estimate err","V matched"))
for n in (20,40,80):
    prev=None
    for k in (1,2,3,4,5):
        lo,hi=bracket_k(n,k); w=hi-lo
        e=est_err(n,k)
        V=w/e if e>0 else np.inf
        print("  %5d%6d%16.6g%16.6g%14.6g"%(n,k,w,e,V))
    print()
print("""
  **V AT MATCHED ORDER IS THE ANSWER TO Q9.**

  Read the k = 1..5 column at fixed nu. If V is roughly constant, a
  bracket keeps pace with an estimate and Q9's conclusion is fully
  withdrawn. If V grows, it grows far more slowly than the 1.1e8 that
  holding the bracket at order 1 produced.
""")