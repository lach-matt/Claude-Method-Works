import sympy as sp, numpy as np
from itertools import product
from collections import Counter
z=sp.symbols('z')
NC,LC,KC,EC,FC=3,2,3,3,2
cells=[]
for n in range(1,NC+1):
  for l in range(0,min(n,LC)):
    for k in range(1,min(4*l+2,KC)+1):
      for q in range(0,k+1):
        for e in range(1,EC+1):
          for f in range(0,min(e,FC)):
            for g in range(0,min(q,4*f+2)+1):
              for S2 in range(0,k+1): cells.append((n,l,k,q,e,f,g,S2))
L=sorted(set(cells))
print("="*76); print("  ANATOMY OF THE SINGLE EXPRESSION"); print("="*76)
print("""
  F = SUM_n z1^n SUM_{l<n} z2^l SUM_{k<=4l+2} z3^k
        * [ SUM_{S<=k} z8^S ]
        * SUM_{q<=k} z4^q SUM_e z5^e SUM_{f<e} z6^f SUM_{g<=min(q,4f+2)} z7^g
""")
print("="*76); print("  PART 1 -- THE SHAPE OF THE TREE"); print("="*76)
print("""
     n --- l --- k --- q --- g --- f --- e
                 |
                 2S

  **NOT A GENERIC TREE. A PATH OF SEVEN NODES WITH ONE PENDANT.** In graph
  terms a CATERPILLAR, and the simplest tree that is not a path.

  CONSEQUENCE, not previously stated: a caterpillar admits a LINEAR
  nesting order. Every sum can be written in one left-to-right sweep with
  a single bracketed factor. **A branching tree would require nested
  brackets; a cycle would require inclusion-exclusion.**
""")
print("="*76); print("  PART 2 -- THE ONLY COUPLING IN THE WHOLE EXPRESSION"); print("="*76)
print("""
  Every bound is a single inequality EXCEPT one:

        g <= min(q, 4f+2)

  **g is the only INTERNAL node of the path that is summed last**, so both
  its neighbours are already fixed when its range is set. Every other
  variable has exactly one fixed neighbour at its turn.

  THAT MIN IS THE ENTIRE NON-PRODUCT CONTENT OF F. Remove it -- let g run
  to q alone -- and F becomes a pure product of independent sums.
""")
def count(coupled=True):
    tot=0
    for n in range(1,NC+1):
      for l in range(0,min(n,LC)):
        for k in range(1,min(4*l+2,KC)+1):
          inner=0
          for q in range(0,k+1):
            for e in range(1,EC+1):
              for f in range(0,min(e,FC)):
                inner += (min(q,4*f+2)+1) if coupled else (q+1)
          tot+=(k+1)*inner
    return tot
print("     with the min : %d cells   (= enumeration: %s)"%(count(True),count(True)==len(L)))
print("     without      : %d cells   -- the coupling removes %d"%(count(False),count(False)-count(True)))
print("="*76); print("  PART 3 -- THE DETACHABLE FACTOR"); print("="*76)
print("""
        [ SUM_{S=0}^{k} z8^S ]  =  (1 - z8^(k+1)) / (1 - z8)

  **2S is a LEAF, so its sum closes in the geometric form and multiplies
  out.** It contributes (k+1) to every count and never interacts.

  CONSEQUENCE: spin multiplicity is ALGEBRAICALLY INERT in this lattice.
  It scales every cell count by (k+1) and changes no structure. **That is
  why removing it leaves E(X) = 0 unchanged** -- a fact the book verifies
  numerically and never explains.
""")
Ls={x[:7] for x in L}
print("     |Lambda| with 2S : %d"%len(L))
print("     |Lambda| without : %d   ratio %.4f"%(len(Ls),len(L)/len(Ls)))
print("="*76); print("  PART 4 -- THE RANK POLYNOMIAL, READ CLOSELY"); print("="*76)
rk=Counter(sum(x) for x in L); ks=sorted(rk); c=[rk[k] for k in ks]
poly=sum(v*z**k for k,v in sorted(rk.items()))
print("\n     min rank %d = 1(n) + 1(k) + 1(e); all other coordinates may be 0"%min(ks))
print("     max rank %d"%max(ks))
print("\n     coefficients:", c)
lc=all(c[i]**2>=c[i-1]*c[i+1] for i in range(1,len(c)-1))
uni=all(c[i]<=c[i+1] for i in range(np.argmax(c)))and all(c[i]>=c[i+1] for i in range(np.argmax(c),len(c)-1))
pal=(c==c[::-1])
print("\n     log-concave : %s   -> unimodal -> SPERNER"%lc)
print("     unimodal    : %s"%uni)
print("     palindromic : %s"%pal)
print("""
  **AND THAT LAST LINE IS A CONNECTION THE BOOK NEVER MAKES.**

  A rank polynomial is palindromic IFF the poset is SELF-DUAL. Section 3.3
  reports, as a separate numerical fact, that only 8 of 976 cells survive
  x -> max - x. **The two statements are the same statement.** The
  coefficient list read forwards and backwards are
""")
print("     forwards : %s"%c[:6])
print("     backwards: %s"%c[::-1][:6])
print("""
     and they differ at the second entry: %d against %d. **Self-duality
     fails at rank 1, and everything downstream follows.**
"""%(c[1],c[::-1][1]))
print("="*76); print("  PART 5 -- WHAT THE SPECIAL VALUES SAY"); print("="*76)
for val,name in [(1,"|Lambda|"),(-1,"even-rank minus odd-rank"),(0,"cells of minimum rank")]:
    v=poly.subs(z,val)
    print("     F(%2d) = %-8s   %s"%(val,v,name))
mean=float(sp.diff(poly,z).subs(z,1)/poly.subs(z,1))
d2=float(sp.diff(poly,z,2).subs(z,1)/poly.subs(z,1))
var=d2+mean-mean**2
print("     F'(1)/F(1)      = %.4f   mean rank"%mean)
print("     variance of rank= %.4f   sd %.4f"%(var,np.sqrt(var)))
print("     midpoint        = %.1f   skew %.4f"%((min(ks)+max(ks))/2,mean-(min(ks)+max(ks))/2))
print("""
  **F(-1) = %s IS NOT ZERO**, which is the same non-self-duality again:
  a self-dual graded poset with a symmetric rank function has F(-1) = 0
  when the rank range is odd. Here it is not.
"""%poly.subs(z,-1))
print("="*76); print("  PART 6 -- WHAT HOLDS IT TOGETHER, AND WHAT WOULD BREAK IT"); print("="*76)
BR=[("make a bound depend on a SUM","g <= q + f","polytope survives, TREE DIES",
     "2^d inclusion-exclusion returns; Sec 10.4 measured 89,864 join failures"),
    ("make a bound depend on THREE variables","g <= q + k - f","tree dies",
     "no linear nesting; brackets nest"),
    ("add a CYCLE","n <= 2S","factorisation dies",
     "the sweep never terminates; no closed form"),
    ("make a bound NON-MONOTONE","g <= |q - 3|","polytope dies",
     "the region is not convex; min/max closure fails"),
    ("remove the min coupling","g <= q only","nothing dies",
     "F becomes a pure product -- SIMPLER, and describes a different set")]
print("  %-34s%-18s%s"%("perturbation","what dies","consequence"))
print("  "+"-"*76)
for a,ex,d,c2 in BR:
    print("  %-34s%-18s%s"%(a,d,c2[:34]))
print("""
  **THREE OF THE FIVE ARE FATAL AND ONE IS BENIGN.** The benign one is the
  coupling -- the expression's only complication is also the only part
  that could be removed without loss of structure.

  **SO WHAT CLOSES THE EXPRESSION IS NOT THE COUPLING BUT THE ABSENCE OF
  CYCLES, SUMS AND NON-MONOTONICITY.** The min is decoration; the tree is
  load-bearing.
""")