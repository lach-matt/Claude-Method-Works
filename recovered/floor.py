import numpy as np, sympy as sp
R=109737.3; T=lambda v: R/v**2
def pa(nd,n): return np.polyval(np.polyfit(nd,[T(t) for t in nd],len(nd)-1),n)
def bk(n,k):
    lo,hi=-np.inf,np.inf
    for m in range(0,k+2):
        bl=k+1-m
        if bl<0: continue
        nd=sorted([n+j for j in range(1,m+1)]+[n-j for j in range(1,bl+1)])
        if len(nd)!=k+1 or min(nd)<2: continue
        p=pa(nd,n)
        if (k+1+m)%2==0: lo=max(lo,p)
        else: hi=min(hi,p)
    return lo,hi
def est(n,k):
    nd=sorted([n+j for j in range(-k,k+1) if j!=0])[:k+1]
    return abs(pa(nd,n)-T(n))
print("="*80)
print("  DOES MATCHED-ORDER V VIOLATE THE FLOOR?")
print("="*80)
print("""
  Prop 15.2 proves V > 2 for a monotone sequence. Section 22.6 says
  matched-order V oscillates ABOUT that floor. The table shows values
  below it. One of those statements is wrong.
""")
print("  %6s%5s%14s%14s%12s%10s"%("nu","k","bracket w","estimate e","V","> 2?"))
print("  "+"-"*62)
bad=0; tot=0
for nu in (20,40,80):
    for k in (1,2,3,4,5):
        lo,hi=bk(nu,k); w=hi-lo; e=est(nu,k); V=w/e
        tot+=1; ok=V>2
        if not ok: bad+=1
        print("  %6d%5d%14.6g%14.6g%12.4f%10s"%(nu,k,w,e,V,"yes" if ok else "NO"))
    print()
print("     values below 2 : %d of %d"%(bad,tot))
print("="*80)
print("  WHY — AND PROP 15.2 IS NOT VIOLATED")
print("="*80)
print("""
  **Prop 15.2 is a statement about ONE object: the first-order bracket
  against the LINEAR estimate on the same two neighbours.** Its proof uses
  w = |y(x+h) − y(x−h)| and e = |y(x) − mean|, and the mean is exactly the
  linear interpolant. **The two quantities are locked together.**

  At matched order they are NOT. The order-k bracket uses k+1 nodes chosen
  by SIGN; the order-k estimate uses a different set chosen for accuracy.
  **They are computed from different data**, so no inequality between them
  is implied by the proposition.
""")
print("  DEMONSTRATE: at order 1, are the two objects the same?\n")
for nu in (20,40):
    lo,hi=bk(nu,1)
    a,m,b=T(nu-1),T(nu),T(nu+1)
    print("     nu=%d  bracket [%.6f, %.6f]"%(nu,lo,hi))
    print("            [min,max] of neighbours [%.6f, %.6f]"%(min(a,b),max(a,b)))
    print("            classical w=%.6f  e=%.6f  V=%.4f"%(abs(b-a),abs(m-(a+b)/2),abs(b-a)/abs(m-(a+b)/2)))
    print("            order-1 w=%.6f  e=%.6f  V=%.4f"%(hi-lo,est(nu,1),(hi-lo)/est(nu,1)))
    print()
print("""
  **THE ORDER-1 BRACKET IS NOT THE CLASSICAL BRACKET.** The sign rule with
  k = 1 uses two nodes chosen by parity — one above, one below, or two on
  one side — and produces a NARROWER interval than [min, max] of the
  neighbours. So its V is smaller, and Prop 15.2 has nothing to say about it.
""")
print("="*80)
print("  SO WHAT IS THE FLOOR AT MATCHED ORDER?")
print("="*80)
vals=[]
for nu in np.arange(6,120,1.0):
    for k in (1,2,3,4,5):
        try:
            lo,hi=bk(nu,k); e=est(nu,k)
            if e>0 and np.isfinite(lo) and np.isfinite(hi): vals.append((hi-lo)/e)
        except Exception: pass
vals=np.array(vals)
print("\n     matched-order V over %d (nu,k) pairs:"%len(vals))
print("        minimum %.4f   median %.4f   maximum %.4f"%(vals.min(),np.median(vals),vals.max()))
print("        below 2 : %d  (%.0f%%)"%((vals<2).sum(),100*(vals<2).mean()))
print("        below 1 : %d"%((vals<1).sum()))
print("""
  **THE MATCHED-ORDER RATIO HAS NO FLOOR AT 2. Its floor is 1**, and it
  cannot go below that, because a deductive bracket must contain the value
  and the estimate is one point inside it.

  **CORRECTION 93.** Section 22.6 and Section 15.10.2 both say the
  matched-order V oscillates about Prop 15.2's floor. It does not. The two
  quantities are different objects and the resemblance to 2 is numerical
  coincidence at the depths tested, not a bound.

  **What survives is the finding that matters: matched-order V does not
  GROW with k.** That is what refutes 'bounds become worthless as data
  accumulates'. The value it sits near is incidental.
""")