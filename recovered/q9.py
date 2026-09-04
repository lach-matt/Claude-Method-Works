import numpy as np
from numpy.polynomial import polynomial as P
R=109737.3
T=lambda v: R/v**2
print("="*76)
print("  Q9.  THE BRACKET USES TWO NEIGHBOURS. WHAT IF YOU HAVE MORE?")
print("="*76)
print("""
  Every V in this book compares a bracket from n+-1 against a LINEAR
  estimate from the same two points. But a channel with many members
  supports a HIGHER-ORDER estimate. Ask what that does to the ratio.

     the BRACKET is bounded by the NEAREST measured neighbours -- extra
     points outside them cannot narrow it

     the ESTIMATE improves with every added point

  So V must GROW with the amount of data. Compute by how much.
""")
def bracket(n,h=1):
    return abs(T(n+h)-T(n-h))
def est_err(n,k):
    """error of degree-(2k-1) polynomial interpolation using 2k neighbours"""
    xs=[n+j for j in range(-k,k+1) if j!=0]
    ys=[T(x) for x in xs]
    c=np.polyfit(xs,ys,len(xs)-1)
    return abs(np.polyval(c,n)-T(n))
print("  %5s%8s%14s%16s%14s%10s"%("nu","points","bracket w","estimate e","V","log2 V"))
for n in (20,40):
    w=bracket(n)
    for k in (1,2,3,4):
        e=est_err(n,k)
        V=w/e
        print("  %5d%8d%14.6g%16.6g%14.6g%10.2f"%(n,2*k,w,e,V,np.log2(V)))
    print()
print("""
  **THE COST OF A GUARANTEE GROWS WITHOUT BOUND AS DATA ACCUMULATES.**

  Two points: V ~ 4nu/3. Eight points: V is larger by several orders. And
  the growth has a clean form -- each added PAIR of points multiplies the
  estimate's accuracy by roughly (nu/h)^2 while leaving the bracket
  untouched.
""")
print("  %5s%8s%18s%20s"%("nu","points","V","ratio to 2-point"))
for n in (40,):
    w=bracket(n); base=None
    for k in (1,2,3,4,5):
        try:
            e=est_err(n,k); V=w/e
        except Exception: break
        if base is None: base=V
        print("  %5d%8d%18.6g%20.4g"%(n,2*k,V,V/base))
print("""
==========================================================================
  AND THAT EXPLAINS WHY THE FIELD ABANDONED BOUNDS
==========================================================================

  In 1908 a spectroscopist had three or four members of a series. Today a
  channel runs to n = 100 with sub-MHz precision. **Over that century the
  estimate improved by many orders of magnitude and the bracket improved
  only as the levels got closer together.**

  **A deductive bound is worth most when data is scarce, and its relative
  value falls monotonically as data accumulates.** That is not a defect of
  the method -- it is the method's domain, stated in the one variable the
  book never varied.
""")
print("="*76)
print("  Q10.  SO IS THERE A REGIME WHERE THE BRACKET WINS?")
print("="*76)
print("""
  V > 2 always, so a bracket is NEVER narrower than the estimate beside it.
  The bracket wins only where the estimate CANNOT BE TRUSTED -- where the
  smoothness assumption fails.

     a perturbed level         the Ritz fit is wrong; containment is not
     a coupling-scheme change  the fit has no valid form; containment holds
     a single measured pair    no fit is possible; containment still is
     an unknown limit          the fit needs I; containment does not

  **FOUR REGIMES, AND ALL FOUR ARE FAILURE MODES OF THE ESTIMATE.**
  The bracket's domain is exactly the complement of the fit's.
""")
print("="*76)
print("  Q11.  DOES THE CLAIM SET CLOSE NOW?")
print("="*76)
print("""
  Re-close after adding: V = 4r^3/(3r^2-1); lambda^2 = (2/3)T;
  Aitken(y) = -y/(p-1); V = (4x/h)|bias|; w/T = 4h/nu; e/T = 3(h/nu)^2;
  E_bits = log2 C(|R|,E); self-concordance for nu <= (sqrt6/2)Z sqrt R.

  NEWLY ADMITTED, AND NOT YET STATED:
""")
print("""     (i)   V grows with the ORDER of the estimate, not only with nu/h
           -- Q9 above, now stated

     (ii)  the Aitken bias and V share the pole, so **any accelerator's
           bias diverges exactly where the bracket's cost does**

     (iii) lambda > 1 for every measured level, so **no Rydberg level is
           in the Newton-safe region** -- Q8, now stated

     (iv)  **E_bits and log2 V are the same currency, so the periodic
           table's 105 bits and a bracket's 5.7 bits are comparable**
           -- 105 bits is eighteen brackets' worth of surrendered
           precision

  **E(claim set) = 4 before this message, and (i)-(iv) are now stated.**
  The closure is not yet empty: each of these admits further consequences,
  and the honest position is that the set has not stopped growing.
""")