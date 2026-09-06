import numpy as np
from itertools import product
from collections import Counter
print("="*88)
print("  THE CALABI-YAU CATALOGUE, TESTED AGAINST THE BOOK'S TWO CRITERIA")
print("="*88)
print("""
  **What I have and what I do not.** The 30,108 Hodge pairs are at
  hep.itp.tuwien.ac.at as a gzipped file that came back unreadable. So the
  tests below use DOCUMENTED STRUCTURAL FACTS, each cited, and no invented
  data. Where a number is from the literature it is marked [L].
""")
print("="*88)
print("  TEST 1 — IS THE CATALOGUE SELF-DUAL?  (Section 3.4's question)")
print("="*88)
print("""
  Batyrev's theorem: for every reflexive polytope Δ the polar dual Δ* is
  also reflexive, and the Calabi-Yau hypersurfaces have SWAPPED Hodge
  numbers. **The Kreuzer-Skarke list is complete** — all 473,800,776
  reflexive 4-polytopes [L] — **so it is closed under polar duality by
  construction.**

     the set of Hodge pairs is exactly closed under (h11,h21) -> (h21,h11)

  **THAT IS A THEOREM, NOT AN OBSERVATION**, and it is the sharpest
  possible contrast with Λ:
""")
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)}
A=[sorted({z[i] for z in LAM}) for i in range(8)]
mx=[max(a) for a in A]
sd=sum(1 for x in LAM if tuple(mx[i]-x[i] for i in range(8)) in LAM)
rk=Counter(sum(x) for x in LAM); ks=sorted(rk); c=[rk[k] for k in ks]
print("  %-34s%18s%18s"%("","Λ","the KS catalogue"))
print("  "+"-"*70)
print("  %-34s%18s%18s"%("self-dual cells","%d of %d"%(sd,len(LAM)),"ALL [theorem]"))
print("  %-34s%18s%18s"%("rank polynomial palindromic",str(c==c[::-1]),"TRUE"))
print("  %-34s%18s%18s"%("duality","fails","exact"))
print("""
  **THE CATALOGUE HAS THE SYMMETRY Λ LACKS, AND IT IS BUILT IN.** Mirror
  symmetry is not a discovered regularity in the KS list — it is a
  consequence of the list being COMPLETE under an involution. **Λ is not
  complete under any involution**, which is why Section 3.4 finds 8 of 976.

  **AND THAT IS A DESIGN LESSON THE BOOK CAN STATE:** an index closed under
  a duality has a palindromic rank polynomial, and one that is not, does
  not. **The 8 survivors measure exactly how far Λ is from being closed
  under reflection.**
""")
print("="*88)
print("  TEST 2 — THE h11 + h21 >= 22 BOUNDARY.  DEFECT OR FEATURE?")
print("="*88)
print("""
  Documented [L]:
     the KS manifolds populate h11 + h21 >= 22 densely
     the region h11 + h21 < 22 is 'much less populated, and all known
     examples arise from OTHER CONSTRUCTIONS'  (arXiv:2310.05909)
     the tip where both are small is 'thinly populated' (Triadophilia,
     arXiv:0706.3134)

  **Section 10.7.1's test: is the absence removable by re-coordinatising —
  here, by re-CONSTRUCTING?**
""")
print("  %-40s%s"%("construction","populates h11+h21 < 22?"))
print("  "+"-"*66)
for nm,ok in [("Batyrev / toric hypersurfaces (KS)","no — sparse"),
              ("complete intersections (CICY)","yes [L]"),
              ("Klemm-Kreuzer toric CICYs","yes [L]"),
              ("toric conifold transitions","yes [L]")]:
    print("  %-40s%s"%(nm,ok))
print("""
  **THE ABSENCE VANISHES UNDER A DIFFERENT CONSTRUCTION.** By the test of
  Section 10.7.1 that makes it a **defect of the index**, not a feature of
  the world — the same verdict as the periodic table's 36, and the
  opposite of the asteroid belt's six.

     the periodic table's 36   removable by relayout        -> defect
     **the KS gap below 22     removable by reconstruction  -> defect**
     the belt's six absences   removable by nothing         -> feature

  **So the landscape's thin tip is a property of Batyrev's construction,
  not of Calabi-Yau geometry.** That is a statement the book's own
  criterion makes, and it agrees with what the literature says
  qualitatively — **the criterion supplies the reason.**
""")
print("="*88)
print("  TEST 3 — WHAT THE BOOK CANNOT DO HERE, STATED PLAINLY")
print("="*88)
print("""
     **E(X) of the catalogue is NOT computed.** It needs the 30,108 pairs
     and they are behind a gzipped file this session cannot read. The
     Hugging Face parquet mirror exists and would settle it.

     **The two tests above are structural, not enumerative.** Test 1 is a
     theorem restated in the book's language. Test 2 applies the book's
     criterion to a documented fact. **Neither is a computation on the
     data**, and the book must say so.

  **WHAT WOULD SETTLE E(X):** load the 30,108 pairs, take (h11, h21) as
  coordinates, compute 𝓡 and count. **One afternoon with the file.**
""")