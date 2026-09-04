print("="*98)
print("  ALL NINETEEN ATTEMPTS, READ AS BOUNDS")
print("="*98)
A=[
(1,"Γ-free / totally balanced","necessary, not sufficient","reorderable ⊊ tot.balanced","upper"),
(2,"chain of row supports","sufficient, not necessary","chain ⊊ reorderable","lower"),
(3,"row chain OR column chain","68%","neither axis decides alone; the condition is TWO-SIDED","structural"),
(4,"slice-chain lift to d=3","69%","the d=2 condition does not lift","upper"),
(5,"3-SAT reduction","refuted","a reduction must control which pairs arise","method"),
(6,"depth-1 descent on E","89.8%","E is a genuine potential; the landscape has traps","positive"),
(7,"depth-2, depth-3 descent","stalls, worsening with size","**no constant-depth local method decides it**","negative"),
(8,"linear extensions of inclusion","82% / 48.7%","the inclusion order is NOT Birkhoff's poset","structural"),
(9,"width ≤ 2 per container","necessary","three incomparable rows cannot reach two ends","upper"),
(10,"end-assignment 2-SAT","necessary","the projection form of the path constraint","upper"),
(11,"immediate-container forest","necessary","one level does not constrain the rest","upper"),
(12,"overlap components ≤ 2","necessary","components compete, not just rows","upper"),
(13,"≤2 immediate children","necessary","two non-nested children cannot share an end","upper"),
(14,"path 2-SAT on the tree","FN only","**correct in FORM; failed on the tree**","method"),
(15,"containment 2-SAT on poset","0 FN, 108 FP","**loses the overlap axis**","structural"),
(16,"pointwise containment 2-SAT","0 FN, 80 FP","intersecting more projections is still a projection","structural"),
(17,"row/col-deleted sub-instances","0 FN","**a GENERATOR of necessary conditions**","upper"),
(18,"bottom-up traversal ×7","errors both ways","**frontier-correct ⇏ anchor-complete**","structural"),
(19,"two-state tree + coupling","88% at k=0","the failure is in tree recovery, not in the coupling","method"),
]
print("\n  %3s%-30s%-24s%-46s%s"%("#","attempt","result","the bound","kind"))
print("  "+"-"*126)
for i,a,b,c,d in A: print("  %3d%-30s%-24s%-46s%s"%(i,a[:30],b[:24],c[:46],d))
import collections
k=collections.Counter(d for *_,d in A)
print("\n     upper %d   lower %d   structural %d   negative %d   method %d   positive %d"
      %(k['upper'],k['lower'],k['structural'],k['negative'],k['method'],k['positive']))
print("="*98)
print("  WHAT THE COLLECTION ENCLOSES")
print("="*98)
print("""
  **Seven upper bounds** all say the same thing in different notations: a
  projection is necessary. **§13.4 makes that a theorem**, so they are one
  bound seen seven times, not seven bounds.

  **One lower bound.** chain ⊊ reorderable.

  **Six structural bounds, and these are the load-bearing ones** — each
  names a THING THE PROBLEM HAS that a formulation lacked:

       two-sidedness          (3)   — a criterion must constrain both axes
       Birkhoff ≠ inclusion   (8)   — the poset must be of join-irreducibles
       the overlap axis       (15)  — containment alone is insufficient
       projection ≠ enough    (16)  — confirmed against §13.4
       **anchor-completeness** (18)  — frontier-correct is the wrong test
       implied vs real coupling (19) — k of the defining graph, not the recovered

  **Two negatives.** No constant-depth local method. No backtrack-free
  method.

  **Three method bounds.** A reduction must control its pairs; the path
  formulation is right in form; the tree-recovery step is the weak link.
""")
print("="*98)
print("  THE BOUNDS NOT YET STATED — READ OFF THE GAPS")
print("="*98)
print("""
  **1. The MEET bound.** Today's 12%/88% split: the 88% fail by a missing
     JOIN, the 12% by a missing MEET — 8.244 join-failures against 0.028.
     **§13.4's counterexample is a join counterexample, so its signature is
     blind to the meet class.** The meet condition is necessary and is
     nowhere stated in the book.

  **2. The implication bound.** Λ's defining graph has k = 0, its recovered
     graph k = 9, and **all nine extras are implied.** An index is
     tree-recoverable when its extra edges are implied — a checkable
     property §23.2 does not have.

  **3. The alphabet bound.** Reorderability falls in |A| as well as in d:
     1.000 → 0.986 → 0.810 at d = 2 for |A| = 2,3,4. **The d = 2 theorem is
     not vacuous; it excludes 19% at |A| = 4 and 0% at |A| = 2.**

  **4. The counting bound.** Closed sets are exponentially many with a base
     below 2 that decays in BOTH parameters — and **decays faster in
     dimension than in alphabet size**: b = 1.6131 at (d=2,|A|=4) against
     1.5101 at (d=4,|A|=2), same 16 cells.

  **5. The value-of-reordering bound.** Counted exactly: 1.25× at
     (2,2), **3.46× at (2,3)**, 2.15× at (3,2). Reordering buys most in two
     dimensions with large alphabets.

  **6. The density bound.** Reorderability RISES with cell density — a
     nearly full box is a box, and a box is closed.
""")
print("="*98)
print("  AND THE ONE THE COLLECTION POINTS AT AND NOBODY HAS TESTED")
print("="*98)
print("""
  Every upper bound is a projection. Every structural bound names a missing
  axis. **Bound 1 says the missing axis in §13.4 itself is the MEET.**

  > **If the join condition and the meet condition are BOTH necessary and
  > their failure classes are disjoint — 88% and 12% with a
  > three-hundredfold separation — then their CONJUNCTION may be what no
  > single projection could be.**

  That is testable directly, it has not been tested, and it is the first
  candidate today that is not a projection of one kind.
""")