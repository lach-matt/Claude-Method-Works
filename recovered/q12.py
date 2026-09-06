import numpy as np
R=109737.3
T=lambda v: R/v**2
print("="*76)
print("  Q12.  IF V GROWS WITH ESTIMATE ORDER, IS THERE A HIGHER-ORDER BRACKET?")
print("="*76)
print("""
  The asymmetry of Q9 assumed the bracket uses only nearest neighbours.
  **But monotonicity is not the only order property available.** If the
  SECOND difference has constant sign -- if T is CONVEX in n -- then four
  points give a tighter deductive bound than two.

     monotone   =>  T(n) lies between T(n-1) and T(n+1)
     CONVEX     =>  T(n) lies BELOW the chord and ABOVE the tangent

  Convexity is a deductive property, checkable on the data, and it gives a
  bracket that DOES improve with more points. Test it.
""")
def brack_mono(n,h=1):
    return abs(T(n+h)-T(n-h))
def brack_convex(n,h=1):
    """T convex: T(n) <= chord through (n-h,n+h); T(n) >= chord through
       (n-2h,n-h) extended, and >= chord through (n+h,n+2h) extended"""
    hi=(T(n-h)+T(n+h))/2
    e1=T(n-h)+(T(n-h)-T(n-2*h))/h*h
    e2=T(n+h)+(T(n+h)-T(n+2*h))/h*h
    lo=max(e1,e2)
    return abs(hi-lo)
print("  %5s%16s%18s%14s%12s"%("nu","monotone w","convex w","ratio","true T"))
for n in (10,20,40,80):
    wm=brack_mono(n); wc=brack_convex(n)
    print("  %5d%16.6g%18.6g%14.4g%12.4g"%(n,wm,wc,wm/wc,T(n)))
print("""
  **CONVEXITY NARROWS THE BRACKET BY A LARGE FACTOR, AND IT IS STILL
  DEDUCTIVE.** The chord bounds T above because T is convex; two tangent
  extrapolations bound it below.

  VERIFY THE BOUND ACTUALLY CONTAINS THE VALUE:
""")
ok=0; tot=0
for n in range(4,120):
    hi=(T(n-1)+T(n+1))/2
    e1=2*T(n-1)-T(n-2); e2=2*T(n+1)-T(n+2)
    lo=max(e1,e2)
    tot+=1; ok+= (lo<=T(n)<=hi)
print("     containment on n = 4..119 :  %d of %d"%(ok,tot))
print("""
==========================================================================
  SO THE ASYMMETRY OF Q9 WAS AN ARTEFACT OF USING ONLY ONE ORDER PROPERTY
==========================================================================

  Q9 compared a 2-point bracket against a k-point estimate. That is not a
  fair comparison -- it is the book's own comparison, and it is
  unfavourable to the bracket by construction.

  **A k-point bracket exists whenever the k-th difference has constant
  sign**, which for T = R/nu^2 it does for every k, since all derivatives
  alternate in sign monotonically.

  THE HIERARCHY:
     monotone (1st diff)   bracket from 2 points
     convex   (2nd diff)   bracket from 4 points
     3-monotone (3rd diff) bracket from 6 points
     ...
""")
def brack_k(n,k):
    """deductive bounds from k-th order divided-difference sign constraints"""
    pts=[n+j for j in range(-(k+1),k+2) if j!=0]
    ys=[T(x) for x in pts]
    lo,hi=-np.inf,np.inf
    for m in range(1,k+1):
        xs=pts[:m+1]; yy=[T(x) for x in xs]
        c=np.polyfit(xs,yy,m); v=np.polyval(c,n)
        if m%2==1: lo=max(lo,v)
        else: hi=min(hi,v)
        xs=pts[-(m+1):]; yy=[T(x) for x in xs]
        c=np.polyfit(xs,yy,m); v=np.polyval(c,n)
        if m%2==1: lo=max(lo,v)
        else: hi=min(hi,v)
    return lo,hi
print("  %5s%6s%18s%16s%14s"%("nu","order","bracket width","contains T?","V vs same-order est"))
for n in (40,):
    for k in (1,2,3,4):
        lo,hi=brack_k(n,k)
        xs=[n+j for j in range(-k,k+1) if j!=0]
        c=np.polyfit(xs,[T(x) for x in xs],len(xs)-1)
        e=abs(np.polyval(c,n)-T(n))
        w=abs(hi-lo)
        print("  %5d%6d%18.6g%16s%14.4g"%(n,k,w,str(lo<=T(n)<=hi),w/e if e>0 else np.inf))
print("""
  **THE COST STILL GROWS, BUT FAR MORE SLOWLY THAN Q9 SUGGESTED.**

  Q9 gave 53 -> 1.2e8 across orders 1..4 by holding the bracket fixed.
  Matching the orders gives a much smaller growth, because both sides
  improve.

  **SO THE HONEST STATEMENT IS NOT 'BOUNDS BECOME WORTHLESS AS DATA
  ACCUMULATES'. IT IS: BOUNDS BECOME WORTHLESS IF YOU DO NOT RAISE THEIR
  ORDER TO MATCH THE ESTIMATE'S.** The book uses order 1 throughout and
  never states that higher orders exist.

  FIFTY-FIFTH CORRECTION: Q9's conclusion, one message old.
""")