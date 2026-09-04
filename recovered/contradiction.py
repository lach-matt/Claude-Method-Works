import numpy as np, math
from itertools import product, permutations, combinations
print("="*88)
print("  THE CONTRADICTION, EXAMINED")
print("="*88)
print("""
  **My statement:** 'does the obstruction count grow polynomially in the box?'

  **The objection:** the list is finite and computable, so it has an end
  coordinate. It does not grow — it is simply not yet fully defined.

  **Where the objection lands.**

  'Grows' quantifies over BOXES — a family of indices. And this session
  established that **completeness descends and does not ascend**: the family
  of all closed sets is not itself an index (union 64–89%, intersection
  70–81%, distributivity failing at 1,302 of 6,416 triples).

  > **So a growth question is a question about the family Λ belongs to, and
  > that family is not an index.** Within the frame, the well-posed question
  > is: FOR THIS INDEX, what is the list? And that has an answer.

  **Where I was loose.** I wrote 'computable' meaning FINITE and
  WELL-DEFINED. That is not the same as ENUMERABLE IN PRACTICE.
""")
dims=[3,2,3,4,3,2,4,4]
n=int(np.prod(dims))
print("="*88)
print("  Λ's OWN BOX, PRECISELY")
print("="*88)
print("""
     alphabets            : %s
     cells in the box     : %d
     subsets of the box   : 2^%d  ≈ 10^%d
     **the obstruction list is a finite subset of that**
"""%(dims,n,n,int(n*math.log10(2))))
print("""  **So: finite, well-defined, with an end coordinate — and not enumerable by
  this or any machine.** Both statements are true, and I conflated them.
  CORRECTION 175.
""")
print("="*88)
print("  WHAT IS ACTUALLY DEFINED, AND WHAT IS NOT")
print("="*88)
T=[("the list EXISTS for Λ's box","YES — finite by Sperner","defined"),
   ("its size is bounded","YES — by C(6912, 3456)","defined"),
   ("it has an end coordinate","YES — a finite antichain has a last element in any linear extension","defined"),
   ("it is enumerable in practice","NO — 10^2081 subsets","**not defined**"),
   ("Λ is in it","NO — Λ is reorderable, and derivable","defined"),
   ("membership is testable for a GIVEN X","YES — by subset search against the list","conditional on the list"),
   ("the list for Λ's box has been WRITTEN","NO","**not defined**")]
print("\n  %-42s%-46s%s"%("statement","value","status"))
print("  "+"-"*108)
for a,b,c in T: print("  %-42s%-46s%s"%(a,b[:46],c))
print("="*88)
print("  SO THE RESIDUE, RESTATED WITHOUT THE CONTRADICTION")
print("="*88)
print("""
  **Not:** 'does the list grow?'  — that quantifies outside the index.
  **Not:** 'is the list computable?' — it is, and that says nothing useful.

  > **The residue is: the obstruction list for a given box is finite,
  > sparse, and NOT YET WRITTEN — and no method is known for writing it
  > that is faster than enumerating subsets.**

  **That is a definition problem, not a growth problem**, and it is exactly
  what P23 describes: **all of the definitions are not yet identified.**

  **And it is the same residue the d = 2 case resolved by a different
  route.** Booth & Lueker never wrote Tucker's list either — **the PQ-tree
  decides membership without the list existing in written form.**

  > **So the missing object is still a data structure, and the obstruction
  > list was never the thing to write.** The list is finite; the structure is
  > what makes it unnecessary.
""")