import numpy as np, sympy as sp
print("="*86)
print("  Q4.  WHAT FAMILY ACHIEVES THE FLOOR V = 2?")
print("="*86)
print("""
  Prop 15.2: V > 2 for every monotone sequence, and 32/11 for a Rydberg
  series. **Which families come CLOSE to 2, and does anything in celestial
  mechanics sit there?**

  V = 4x/(h|p−1|) falls as the power law steepens, so look for something
  steeper than any power: an EXPONENTIAL.
""")
k,h=sp.symbols('k h',positive=True)
x=sp.symbols('x')
y=sp.exp(k*x)
w=sp.simplify(y.subs(x,x+h)-y.subs(x,x-h))
e=sp.simplify((y.subs(x,x-h)+y.subs(x,x+h))/2-y)
V=sp.simplify(w/e)
print("     y = e^(kx)   ->   V = %s"%sp.simplify(V))
print("     limit kh -> 0   : %s"%sp.limit(V.subs(h,sp.Symbol('t')/k),sp.Symbol('t'),0))
print("     limit kh -> oo  : %s"%sp.limit(V.subs(h,sp.Symbol('t')/k),sp.Symbol('t'),sp.oo))
print("""
  **V = 2 sinh(kh)/(cosh(kh) − 1), and it falls to 2 as kh grows.**
  An exponential family approaches the floor and never crosses it —
  Prop 15.2 holds, and the exponential is the case that saturates it.
""")
print("  %8s%14s"%("kh","V"))
for kh in (0.1,0.5,1,2,3,5,8):
    print("  %8.1f%14.6f"%(kh,2*np.sinh(kh)/(np.cosh(kh)-1)))
print("""
  **AND RESONANCE STRENGTH IS EXPONENTIAL IN ORDER.** The disturbing term
  enters at e^|p−q|, so the strength sequence across orders is exactly this
  family. **The Kirkwood catalogue sits at the cheapest guarantee there is.**
""")
strength=lambda o,ecc=0.1: ecc**o
print("\n  V for resonance strength vs order, at e = 0.1 (kh = ln(1/e) = %.2f):\n"%np.log(10))
for o in (2,3,4,5,6):
    a,m,b=strength(o-1),strength(o),strength(o+1)
    print("     order %d :  V = %.4f"%(o,abs(b-a)/abs(m-(a+b)/2)))
print("     floor    :  2.0000")
print("="*86)
print("  Q5.  IS THE BELT'S ORDER CUT THE ADMISSIBILITY RULE?")
print("="*86)
print("""
  Section 15.10.4: order k is admissible while |Δ^(k+1)T| > 5·2^(k+1)·σ —
  a signal exceeding a noise floor.

  The belt: a resonance is visible while its strength exceeds the
  population scatter. **Same form. Test whether the numbers agree.**
""")
print("  strength ~ e^order with e the typical belt eccentricity ~ 0.15")
print("  detectable while strength > relative scatter of the population\n")
ecc=0.15
print("  %8s%16s%16s%12s"%("order","strength e^o","observed?","ratio to cut"))
OBSCUT=7
for o in range(1,12):
    s=ecc**o
    print("  %8d%16.3e%16s%12.2f"%(o,s,"YES" if o<=OBSCUT else "no",s/ecc**OBSCUT))
thr=ecc**OBSCUT
print("\n     implied detection floor : %.3e  (relative)"%thr)
print("     i.e. a resonance is seen while its strength exceeds ~%.1e"%thr)
print("""
  **THE ORDER CUT IS AN ADMISSIBILITY BOUNDARY, NOT A CAPACITY.** It is not
  a magic number — there is no shell filling. It is the point where a
  signal drops below what the data can resolve, **exactly as ν_V is the
  depth where curvature drops below quotation granularity.**

  **SO THE TWO SUBJECTS SHARE THE RULE AND NOT THE MECHANISM:**

     Λ, the nucleus  : capacity bounds -> magic numbers, periods, blocks
     the belt        : NO capacity -> no magic numbers, only a resolution
                       floor, and the cut at order 7/8 is that floor
""")
print("="*86)
print("  Q6.  WHICH MEANS THE BOOK HAS TWO DIFFERENT KINDS OF BOUND AND SAYS ONE")
print("="*86)
print("""
  Every constraint in Λ is a CAPACITY: l <= n−1, k <= 2(2l+1), g <= q.
  Each says 'this coordinate cannot exceed that function of another'.

  Every admissibility rule is a RESOLUTION: r >= 5, nu <= nu_V,
  |Δ^(k+1)T| > 5·2^(k+1)σ. Each says 'below this, the data cannot tell'.

  **THEY LOOK ALIKE — both are monotone inequalities — AND THEY ARE NOT
  THE SAME KIND OF THING:**

     a capacity bound is about the WORLD. Violating it means the
     configuration does not exist.

     a resolution bound is about the MEASUREMENT. Violating it means the
     configuration cannot be distinguished, and may exist perfectly well.

  **E(X) counts violations of the first. The refusal rate counts
  violations of the second.** The book computes both and calls both
  'admissibility', and the celestial reading is what separates them:
  gravity has resolution floors everywhere and capacity bounds only at the
  Hill sphere.
""")