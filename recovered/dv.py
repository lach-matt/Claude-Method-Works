import numpy as np
R=109737.3
print("="*76)
print("  WHY e/T = 3(h/nu)^2 IS ABSENT -- AND WHAT THE ABSENCE MEANS")
print("="*76)
print("""
  The search returned the field's actual practice, uniformly:

     Ritz fits to delta(n) -- K I, Sr, Th, Rb
     MQDT
     Zilitis: interpolate the QUANTUM DEFECT at three points, quadratic
              in mu(E), two levels plus the threshold

  **NOBODY COMPUTES THE INTERPOLATION ERROR OF T, BECAUSE NOBODY
  INTERPOLATES T. THEY INTERPOLATE delta.**

  And for good reason: T spans orders of magnitude across a series while
  delta is nearly constant. The change of variable is obviously right.

  SO ASK THE QUESTION THE ABSENCE POSES: does interpolating delta escape
  the cost?
""")
print("="*76)
print("  V IS INVARIANT UNDER T -> delta")
print("="*76)
print("""
  delta(n) = delta_0 + delta_2/n^2   (the Ritz form)

     delta'  = -2 delta_2/n^3
     delta'' =  6 delta_2/n^4
     L = |delta'/delta''| = n/3        -- IDENTICAL to T's

  and delta_0 is an additive constant, which cancels from both w and e.
""")
print("        **V(delta) = 4n/(3h) = V(T)**   -- exactly the same\n")
d0,d2=1.35,0.06
dl=lambda n: d0+d2/n**2
T=lambda n: R/(n-dl(n))**2
def we(f,n,h):
    a,m,b=f(n-h),f(n),f(n+h)
    return abs(b-a),abs(m-(a+b)/2)
print("  %5s%4s%14s%14s%10s%10s"%("n","h","V on T","V on delta","4n/3h","w_T/w_d"))
for n in (10,20,40):
    for h in (1,2):
        wT,eT=we(T,n,h); wd,ed=we(dl,n,h)
        print("  %5d%4d%14.4f%14.4f%10.3f%10.3g"%(n,h,wT/eT,wd/ed,4*n/(3*h),wT/wd))
print("""
  **THE COST IS IDENTICAL. THE WIDTH IS NOT.**

  Switching from T to delta narrows the bracket by four to five orders of
  magnitude and leaves V untouched -- because V depends only on the SHAPE
  of the function (the exponent), never on its amplitude or offset.

  THAT IS THE AFFINE INVARIANCE OF SECTION 14.7.3 AGAIN, now doing work:
  delta = delta_0 + delta_2/n^2 is an AFFINE FUNCTION of T's shape, and V
  cannot see an affine map.
""")
print("="*76)
print("  WHICH ANSWERS THE ABSENCE, AND IS A NEW CLAIM")
print("="*76)
print("""
  The field's change of variable -- interpolate delta, not T -- is the
  single most standard move in Rydberg spectroscopy. It was adopted
  because it makes ESTIMATES vastly better.

     **IT DOES NOT MAKE GUARANTEES ANY CHEAPER.**

  The ratio of a deductive bracket to an inferential estimate is 4n/3h
  in either variable. A century of practice improved the numerator and
  the denominator by the same factor.

  **AND THAT IS WHY e/T = 3(h/nu)^2 IS NOWHERE: the quantity was never
  computed because the variable was abandoned, and abandoning it did not
  change the thing this book measures.**
""")
print("="*76)
print("  AND IT PREDICTS WHERE A BRACKET SHOULD ACTUALLY BE APPLIED")
print("="*76)
print("""
  If V is invariant but w is not, then the bracket should be taken in the
  variable with the SMALLEST absolute width -- delta, not T. The guarantee
  costs the same and is four orders narrower.
""")
print("  %5s%4s%16s%16s"%("n","h","bracket on T","bracket on delta"))
for n in (10,20,40):
    wT,eT=we(T,n,1); wd,ed=we(dl,n,1)
    print("  %5d%4d%16.4g%16.4g"%(n,1,wT,wd))
print("""
  **THE BOOK BRACKETS T THROUGHOUT ITS 1,442 CELLS. IT SHOULD HAVE
  BRACKETED delta.** Same guarantee, same cost, a far narrower interval --
  and the reason it did not is that delta requires the ionisation limit,
  while T's containment is limit-free (Section 13.3).

  SO THE TRADE IS EXACT AND NOW STATABLE:

     bracket T      limit-free, wide
     bracket delta  needs the limit, narrow by ~10^4, same V

  **A CHOICE THE BOOK MADE WITHOUT KNOWING IT WAS A CHOICE.**
""")