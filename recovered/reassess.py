print("="*92)
print("  §23.4 REANALYSED IN LIGHT OF EVERYTHING SINCE")
print("="*92)
print("""
  **The question as the section asks it:** given an index whose constraint
  graph has cycles, can its coordinate order be recovered?

  **What has changed about the QUESTION, not just the answer:**
""")
R=[
("the object","'𝓡-reorderability'","**'does a relabelling make X a sublattice of a product of chains'** — the two are identical, 828 instances, zero disagreements"),
("the literature","withdrawn as wrong","**reinstated** — Stahl & Wille, Yannakakis are lattice-embedding results, and that IS the problem"),
("why d = 2 works","a theorem about intervals","**because its CSP is binary** — two cells in two dimensions differ on ≤ 2 axes, k=3 fraction exactly 0.000"),
("why everything else failed","19 separate defeats","**§13.4** — no conjunction of projections suffices, and 13 of 17 attempts were projections"),
("what the failures were","failures","**13 of 17 were seed-independent INVARIANTS** — a family of partial breaks, not a sequence of mistakes"),
("the completeness ceiling","unknown","**fibres partial (4 of Λ's 8 axes) · pairs 94/95 · triples separate the residual** — arity-graded, none complete"),
("Λ's own status","assumed to be at stake","**not at stake** — tree constraint graph, implied extras, ∏|A_i|! = 11,943,936, enumerable"),
("the hardness parameter","cell count","**alphabet size** — the exponential is in max|A_i|, not |X|"),
]
print("  %-22s%-30s%s"%("aspect","was","is"))
print("  "+"-"*112)
for a,b,c in R: print("  %-22s%-30s%s"%(a,b[:30],c[:66]))
print("="*92)
print("  SO WHAT IS THE SOLUTION?")
print("="*92)
print("""
  **For Λ and any capped-alphabet index: SOLVED.** The search space is
  ∏|A_i|! and it is small precisely because the coordinates are capped —
  which §23.7.5 identifies as what capping buys. **Λ: twelve million
  orderings, seconds.**

  **For d = 2 at any alphabet size: SOLVED.** Proved characterisation, and
  the reason is that the CSP is binary.

  **For d ≥ 3 with large alphabets: OPEN, and now bounded on both sides.**

       not shown polynomial   — 20 formulations, including propagation (0/547)
       not shown NP-hard      — 2 reductions, both over-constraining, and the
                                over-constraining is STRUCTURAL: every pair
                                constrains, so clauses cannot be isolated
""")
print("="*92)
print("  AND THE REASSESSMENT THAT MATTERS")
print("="*92)
print("""
  **§23.4 was written as a gap in the method. It is not one.**

  The section sits in a chapter called 'What remains open', and it asks
  whether the ORDER-RECOVERY step generalises. **The measurements say:**

     Λ's constraint graph is a tree                       -> Ch.10 applies
     Λ's recovered graph has k = 9, all implied            -> and still applies
     every sublattice and interval of Λ has E = 0          -> the rules descend
     Λ's own reorderability is decidable by enumeration    -> nothing at stake

  > **The open problem is about indices Λ is not, at alphabet sizes Λ does
  > not have.** It is a question in complexity theory that the book's method
  > raises and does not need answered.

  **That is a different KIND of open item from the other five in §23.9.**
  Sc VI needs a spectrometer. Paschen & Götze needs a library. **This needs
  a theorem, and the book does not depend on it.**
""")
print("="*92)
print("  WHAT §23.4 SHOULD SAY")
print("="*92)
print("""
     1. the identification — 𝓡-closure IS sublattice closure
     2. the literature, reinstated, with the withdrawal recorded
     3. d = 2 proved, and WHY: the CSP is binary
     4. §13.4 as the organising theorem, with the 13-of-17 count
     5. the arity ladder: fibres partial, pairs 94/95, triples separate
     6. the hardness parameter is |A|, not |X|
     7. Λ's own case decidable, and the problem not load-bearing
     8. open for d ≥ 3, bounded on both sides, with both obstructions named
""")