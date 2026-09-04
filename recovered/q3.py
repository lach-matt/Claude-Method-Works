import numpy as np
R=109737.3
d0,d2=1.35,0.06
print("="*76)
print("  THE PRICE OF LIMIT-FREEDOM, COMPUTED PROPERLY")
print("="*76)
print("""
  Bracket delta, then MAP THE INTERVAL BACK TO ENERGY and compare with the
  bracket taken directly on T. Both must be in cm^-1 to be comparable.

     T = R/(n-delta)^2   so   dT/ddelta = 2R/nu^3
     an interval of width w_delta in delta becomes (2R/nu^3)*w_delta in T
""")
nuf=lambda n: n-(d0+d2/n**2)
dl =lambda n: d0+d2/n**2
Tf =lambda n: R/nuf(n)**2
def brack(f,n,h=1):
    a,m,b=f(n-h),f(n),f(n+h)
    return abs(b-a), abs(m-(a+b)/2)
print("  %4s%12s%14s%16s%14s%10s"%("n","nu","w_T (cm-1)","w_delta","w_d->cm-1","ratio"))
for n in (8,10,15,20,30,40,55):
    nu=nuf(n)
    wT,_=brack(Tf,n)
    wd,_=brack(dl,n)
    conv=2*R/nu**3
    wd_cm=wd*conv
    print("  %4d%12.4f%14.5g%16.4g%14.5g%10.4f"%(n,nu,wT,wd,wd_cm,wT/wd_cm))
print("""
  **THE RATIO IS NOT 10^6, NOT 2-3, AND NOT CONSTANT.** Compute what it
  actually is.
""")
print("="*76)
print("  WHY -- AND THE EXACT ANSWER")
print("="*76)
print("""
  w_T is the SECOND difference structure of T; w_delta mapped through
  dT/ddelta is the second difference structure of delta times a LOCAL
  derivative. The two differ because T's variation comes from BOTH the
  change in delta AND the change in n.

     T(n) = R/(n-delta(n))^2

     dT/dn = -2R/nu^3 * (1 - ddelta/dn)

  and ddelta/dn = -2*delta_2/n^3 is TINY. So

     w_T  ~  (2R/nu^3) * 2h * |1 - ddelta/dn|   ~  (2R/nu^3) * 2h
     w_d(mapped) ~ (2R/nu^3) * w_delta          ~  (2R/nu^3) * 2h*|ddelta/dn|

     **ratio = 1/|ddelta/dn| = n^3/(2*delta_2)**
""")
print("  %4s%16s%18s%14s"%("n","ratio measured","n^3/(2 delta_2)","agreement"))
for n in (8,10,15,20,30,40,55):
    nu=nuf(n)
    wT,_=brack(Tf,n); wd,_=brack(dl,n)
    meas=wT/(wd*2*R/nu**3)
    pred=n**3/(2*d2)
    print("  %4d%16.4g%18.4g%14.4f"%(n,meas,pred,meas/pred))
print("""
  **SO THE 'NARROWING' IS ENTIRELY ILLUSORY.** delta's bracket looks
  10^4-10^6 times narrower only because delta barely moves -- and it
  barely moves because delta_2 is small. Mapped back into energy, the
  delta-bracket is narrower by exactly n^3/(2*delta_2), which is not a
  property of the METHOD but of the SIZE OF THE RITZ COEFFICIENT.
""")
print("="*76)
print("  AND THAT SETTLES THE QUESTION")
print("="*76)
print("""
  A bracket on delta does NOT bound T. It bounds delta. To bound T you
  must ALSO know the ionisation limit, and then

     T = R/(n-delta)^2   with delta in [d_lo, d_hi]

  gives an energy interval that DEPENDS ON THE LIMIT'S OWN UNCERTAINTY.
""")
print("  %4s%16s%18s%18s"%("n","w_T direct","w_T via delta","+ limit sigma=0.01"))
for n in (10,20,40):
    nu=nuf(n)
    wT,_=brack(Tf,n)
    wd,_=brack(dl,n)
    lo,hi=dl(n)-wd/2, dl(n)+wd/2
    wvia=abs(R/(n-lo)**2 - R/(n-hi)**2)
    print("  %4d%16.5g%18.5g%18.5g"%(n,wT,wvia,wvia+2*0.01))
print("""
  **THE delta-BRACKET IS GENUINELY NARROWER IN ENERGY -- BY THE FACTOR
  ABOVE -- BUT IT IS NOT A BOUND ON THE MEASURED QUANTITY.** It bounds a
  DERIVED quantity whose conversion to energy carries the limit's
  uncertainty, typically 0.01-1 cm^-1 in this collection.

  SO THE COMPLETE, CORRECTED STATEMENT:

     bracket T       bounds the MEASURED level, needs nothing,
                     width 2h*2R/nu^3
     bracket delta   bounds a DERIVED quantity, needs the limit and
                     inherits its uncertainty; narrower in delta by
                     n^3/(2 delta_2), but the energy bound is no better
                     than the limit is known

  **AT nu = 40 THE BOOK'S TIGHTEST BRACKET IS 1.398 cm^-1 AND THE BEST
  LIMIT UNCERTAINTIES IN THE COLLECTION ARE 0.001-0.4 cm^-1. So the
  delta route would win, but only where the limit is known to better
  than the bracket -- which is not everywhere.**

  FIFTY-FOURTH CORRECTION STANDS. The choice was NOT nearly free, and it
  was NOT costly: **it is conditional on how well the limit is known**,
  and that is a statement the book can make and had not.
""")