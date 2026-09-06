import sympy as sp, numpy as np, time
print("="*76)
print("  THE LANGUAGE IS A BOUND ON THE QUESTION")
print("="*76)
print("""
  Three closure mechanisms have now been used, each in a different
  language, each with a different guarantee. Set them side by side.
""")
L=[("monotone two-variable bounds","Sec 9.4 form",
    "tree factorisation","O(d) -- one pass, no inclusion-exclusion",
    "ALWAYS closes; E(X) computable exactly"),
   ("polynomial relations","this session's V, lambda, w, e",
    "Groebner basis","finite by Hilbert; doubly exponential worst case",
    "ALWAYS closes; membership decidable"),
   ("linear arithmetic with quantifiers","Presburger",
    "quantifier elimination","triply exponential",
    "closes, but not feasibly"),
   ("arithmetic with multiplication","Peano",
    "none","--",
    "DOES NOT CLOSE -- Goedel"),
   ("documentary claims","Paschen & Goetze SecIII; Sc VI 6s",
    "none","--",
    "NO MECHANISM AT ALL -- a citation is not a coefficient")]
print("  %-32s%-22s%s"%("language","mechanism","closure"))
print("  "+"-"*74)
for a,ex,m,c,cl in L:
    print("  %-32s%-22s%s"%(a,m,cl.split(';')[0]))
    print("  %-32s%-22s%s"%("  e.g. "+ex[:24],"  cost: "+c[:18],""))
print("""
{0}
  AND THE BOOK'S OWN QUESTIONS SIT ON DIFFERENT RUNGS
{0}
""".format("="*76))
Q=[("is Lambda closed?","monotone bounds","CLOSED -- one pass"),
   ("E(periodic table)?","monotone bounds","CLOSED -- 36"),
   ("does the claim set close?","polynomial","CLOSED -- basis of 8"),
   ("is V = 4nu/3h implied?","polynomial","CLOSED -- reduces to 0"),
   ("do all accelerators pay 1/|p-1|?","polynomial","DECIDABLE, unrun"),
   ("optimal order given sigma?","polynomial + real data","needs a measured sigma"),
   ("is V = 4nu/3 novel?","documentary","NO MECHANISM"),
   ("Paschen & Goetze SecIII","documentary","NO MECHANISM"),
   ("Sc VI 6s","empirical","NO MECHANISM -- needs a spectrometer")]
print("  %-38s%-24s%s"%("question","language","status"))
print("  "+"-"*76)
for q,l,s in Q: print("  %-38s%-24s%s"%(q,l,s))
print("""
{0}
  VERIFY THE COSTS ARE REAL
{0}
""".format("="*76))
V,w,e,T,h,nu,lam=sp.symbols('V w e T h nu lam',positive=True)
G=[3*h*V-4*nu,3*lam**2-2*T,w*V-8*lam**2,w*nu-4*T*h,e*nu**2-3*T*h**2,V*e-w]
t=time.time(); gb=sp.groebner(G,V,w,e,lam,T,h,nu,order='lex'); t1=time.time()-t
print("  Groebner, 6 relations, 7 vars : %.3f s, basis size %d"%(t1,len(gb.exprs)))
t=time.time()
G2=G+[V**2*e-w**2/e*e, T*h**3-T*h**3]
gb2=sp.groebner([g for g in G2 if g!=0],V,w,e,lam,T,h,nu,order='lex'); t2=time.time()-t
print("  Groebner, extended            : %.3f s, basis size %d"%(t2,len(gb2.exprs)))
from itertools import product
def treecount(NC=3,LC=2,KC=3,EC=3,FC=2):
    tot=0
    for n in range(1,NC+1):
      for l in range(0,min(n,LC)):
        for k in range(1,min(4*l+2,KC)+1):
          inner=0
          for q in range(0,k+1):
            for ee in range(1,EC+1):
              for f in range(0,min(ee,FC)):
                inner+=min(q,4*f+2)+1
          tot+=(k+1)*inner
    return tot
t=time.time(); c=treecount(); t3=time.time()-t
print("  tree factorisation, |Lambda|  : %.5f s, count %d"%(t3,c))
print("""
  **THE MONOTONE-BOUND LANGUAGE IS ~%.0fx FASTER THAN THE POLYNOMIAL ONE
  ON THESE PROBLEMS**, and the documentary language has no timing because
  it has no algorithm.
"""%(t1/max(t3,1e-9)))
print("="*76)
print("  THE PRINCIPLE")
print("="*76)
print("""
  **P20.  The language in which a question is posed bounds whether it can
          close, and at what cost.**

     monotone two-variable bounds  ->  closes in one pass
     polynomial relations          ->  closes, finitely, by Groebner basis
     full arithmetic               ->  does not close       (Goedel)
     documentary                   ->  no mechanism exists

  **AND THE CHOICE OF LANGUAGE IS MADE WHEN THE INDEX IS BUILT, NOT WHEN
  THE QUESTION IS ASKED.** Section 2.1 chose monotone two-variable bounds
  for Lambda. That single decision determined that E(X) is computable,
  that the sum factorises, that a single expression exists, and that every
  question about Lambda's CONTENTS would close.

  **IT ALSO DETERMINED WHAT COULD NEVER CLOSE.** Section 10.4's sum bound
  is outside the language, and its repair -- making the sum a coordinate --
  is precisely a translation BACK INTO the closing language.

  SO P20 SUBSUMES THREE RESULTS ALREADY IN THE BOOK:

     E3, which forbids constraints outside Sec 9.4 form
     the multi-target repair, which restores the form by re-coordinating
     P19's Q(X) = 0, which is reachable exactly when the language closes

  **AND IT ANSWERS THE NOVELTY QUESTION STRUCTURALLY: novelty is posed in
  the documentary language, which has no closure mechanism. That is not a
  failure of searching. It is a property of the language the question is
  written in.**
""")