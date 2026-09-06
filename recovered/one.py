import numpy as np, sympy as sp
from itertools import product
CAP=lambda l:2*(2*l+1)
NC,LC,KC,EC,FC=3,2,3,3,2
cells=[]
for n in range(1,NC+1):
  for l in range(0,min(n,LC)):
    for k in range(1,min(CAP(l),KC)+1):
      for q in range(0,k+1):
        for e in range(1,EC+1):
          for f in range(0,min(e,FC)):
            for g in range(0,min(q,CAP(f))+1):
              for S2 in range(0,k+1): cells.append((n,l,k,q,e,f,g,S2))
L=sorted(set(cells))
print("="*76)
print("  CAN EVERY CELL BE DEFINED IN ONE EXPRESSION?")
print("="*76)
print("\n  enumerated cells: %d\n"%len(L))
print("="*76)
print("  1.  IN LOGIC -- A SINGLE INDICATOR")
print("="*76)
print("""
  Every constraint of Section 2.1 is an inequality. A cell is admitted iff
  all seven hold, so the indicator is a single product of step functions:

     chi(x) = H(n-1-l) H(4l+2-k) H(k-q) H(k-2S) H(e-1-f) H(4f+2-g) H(q-g)

  **Lambda = { x in Z^8 : chi(x) = 1 }.**  One expression, exact.
""")
def chi(x):
    n,l,k,q,e,f,g,S2=x
    return int(l<=n-1 and k<=4*l+2 and q<=k and S2<=k and f<=e-1 and g<=4*f+2 and g<=q
               and 1<=n<=NC and 0<=l<LC and 1<=k<=KC and 1<=e<=EC and 0<=f<FC)
A=[sorted({x[i] for x in L}) for i in range(8)]
amb=list(product(*A))
print("  verify: chi selects %d of %d ambient points   match: %s"
      %(sum(chi(x) for x in amb),len(amb),sum(chi(x) for x in amb)==len(L)))
print("="*76)
print("  2.  IN ALGEBRA -- INTEGER POINTS OF A POLYHEDRON")
print("="*76)
print("""
  All seven constraints are LINEAR. Writing x = (n,l,k,q,e,f,g,2S):

        **Lambda  =  Z^8  and  { x : A x <= b,  x >= x_min }**

  with A the 7 x 8 matrix
""")
rows=[("l - n <= -1",[-1,1,0,0,0,0,0,0],-1),
      ("k - 4l <= 2",[0,-4,1,0,0,0,0,0],2),
      ("q - k <= 0",[0,0,-1,1,0,0,0,0],0),
      ("2S - k <= 0",[0,0,-1,0,0,0,0,1],0),
      ("f - e <= -1",[0,0,0,0,-1,1,0,0],-1),
      ("g - 4f <= 2",[0,0,0,0,0,-4,1,0],2),
      ("g - q <= 0",[0,0,0,-1,0,0,1,0],0)]
for nm,r,bb in rows: print("     %-14s %s  <=  %d"%(nm,r,bb))
print("""
  **LAMBDA IS THE SET OF LATTICE POINTS IN A POLYTOPE.** That single fact
  explains three results the book proves separately: closure under min/max
  (the polytope is a distributive lattice polytope), the tree structure
  (each row has exactly two nonzeros), and treewidth 1.
""")
print("="*76)
print("  3.  IN GEOMETRY -- AND THE TREE MAKES THE COUNT FACTORISE")
print("="*76)
print("""
  Each row of A has exactly TWO nonzero entries, so the constraint graph
  is a graph on 8 nodes with 7 edges -- a TREE. Therefore the sum over
  Lambda factorises with no inclusion-exclusion:
""")
def count():
    tot=0
    for n in range(1,NC+1):
      for l in range(0,min(n,LC)):
        for k in range(1,min(4*l+2,KC)+1):
          nS = k+1
          inner=0
          for q in range(0,k+1):
            for e in range(1,EC+1):
              for f in range(0,min(e,FC)):
                inner += min(q,4*f+2)+1
          tot += nS*inner
    return tot
print("     |Lambda| = SUM_n SUM_l SUM_k (k+1) * SUM_q SUM_e SUM_f [min(q,4f+2)+1]")
print("\n     computed: %d      enumerated: %d      match: %s"%(count(),len(L),count()==len(L)))
print("="*76)
print("  4.  IN ANALYSIS -- ONE RATIONAL GENERATING FUNCTION")
print("="*76)
z=sp.symbols('z')
from collections import Counter
rk=Counter(sum(x) for x in L)
poly=sum(v*z**k for k,v in sorted(rk.items()))
print("""
  The rank generating function F(z) = SUM_x z^(sum of coordinates) encodes
  EVERY cell's rank. For a lattice polytope it is rational; here, finite:
""")
print("     F(z) = %s"%sp.factor(sp.expand(poly)))
print("\n     F(1) = %d = |Lambda|   -- the count is the value at z = 1"%poly.subs(z,1))
print("     F'(1)/F(1) = %.4f  -- the mean rank"%float(sp.diff(poly,z).subs(z,1)/poly.subs(z,1)))
print("="*76)
print("  5.  THE SINGLE EXPRESSION")
print("="*76)
print("""
  All four are the same object written four ways. The one that carries
  every cell, its order, its rank and its count simultaneously is the
  MULTIVARIATE generating function, and the tree makes it a PRODUCT OF
  NESTED SUMS with no cross terms:
""")
print("""
     **F(z_1..z_8) = SUM over the tree, rooted at e:**

        F = SUM_{n=1}^{N} z1^n SUM_{l=0}^{n-1} z2^l SUM_{k=1}^{4l+2} z3^k
              * [ SUM_{S=0}^{k} z8^S ]
              * SUM_{q=0}^{k} z4^q
                  SUM_{e=1}^{E} z5^e SUM_{f=0}^{e-1} z6^f
                    SUM_{g=0}^{min(q,4f+2)} z7^g

  **SETTING EVERY z_i = 1 GIVES |Lambda|.
    SETTING EVERY z_i = z GIVES THE RANK POLYNOMIAL.
    THE COEFFICIENT OF z1^n...z8^S IS 1 IF THE CELL EXISTS AND 0 IF NOT.**

  That last line is the answer to the question: **the coefficient function
  of F IS the indicator chi, so F is a single expression containing every
  cell of the lattice and nothing else.**
""")
print("="*76)
print("  AND WHY IT IS POSSIBLE AT ALL")
print("="*76)
print("""
  A single closed expression exists because of THREE structural facts the
  book proves separately and never combines:

     every constraint is a MONOTONE BOUND      -> the region is a polytope
     every bound couples exactly TWO variables -> the graph is a tree
     the tree has no cycles                    -> the sum factorises

  **REMOVE ANY ONE AND NO SUCH EXPRESSION EXISTS.** A sum bound (Section
  10.4) breaks the first; a three-variable constraint breaks the second; a
  cycle breaks the third -- and inclusion-exclusion returns, with 2^d terms.

  **SO 'ALL THE INFORMATION IN ONE EXPRESSION' IS NOT A CURIOSITY. IT IS
  EXACTLY WHAT CLOSURE BUYS**, and it is the strongest statement of what
  E(X) = 0 means: the expression IS the index, and the cells are its
  coefficients.
""")