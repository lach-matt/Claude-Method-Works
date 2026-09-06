print("="*76)
print("  THE LAW, FORMALISED AND TESTED")
print("="*76)
print("""
  **P19.  An index is complete only when there are no more questions left
          to answer about its contents.**

        COMPLETE(X)  <=>  Q(X) = empty

  where Q(X) is the set of unanswered questions the index's own contents
  admit.
""")
print("="*76)
print("  IT IS STRICTLY STRONGER THAN CLOSURE")
print("="*76)
print("""
     E(X) = 0        no CELL the structure admits is absent
     Q(X) = empty    no QUESTION the contents admit is unanswered

  **E(X) = 0 is necessary and not sufficient.** Lambda has E = 0 and has
  had open questions throughout: whether V depends on order, what the
  Aitken bias generalises to, whether a higher-order bracket exists.
  Every one was admitted by contents already present.

     E(Lambda) = 0                     since Chapter 2
     Q(Lambda) non-empty               still, at this moment

  **CLOSURE IS ABOUT WHAT THE INDEX HOLDS. COMPLETENESS IS ABOUT WHAT IT
  HAS BEEN ASKED.**
""")
print("="*76)
print("  AND IT IS THE MISSING HALF OF P7 AND P13")
print("="*76)
print("""
     P7   all questions must close        exists N with Omega_N = empty
     P13  coherence needs Omega = empty
     P19  completeness needs Q = empty

  P7 says questions CAN close. P13 forbids claiming coherence while any
  stand. **P19 says what their emptiness BUYS: completeness, and nothing
  less confers it.**

  The three are one principle in three moods -- possibility, prohibition,
  and definition -- and P19 was the missing definition.
""")
print("="*76)
print("  TEST: IS THIS BOOK COMPLETE?")
print("="*76)
Q=[("does the perturbation-bound inversion tighten at higher order?",
    "1,061 bounds are order-1; order 3 would bound ~200x tighter"),
   ("is there an order maximising the bound, given sigma?",
    "tighter bracket vs smaller tolerated perturbation -- an optimum exists"),
   ("does the collection's cell count change at matched order?",
    "1,442 is an order-1 count; the order-k count is unknown"),
   ("what is V for the convex bracket on the 1,442 real cells?",
    "computed on T = R/nu^2 only, never on measured levels"),
   ("do all accelerators pay 1/|p-1|, or only Aitken?",
    "Shanks, Levin, Wynn untested"),
   ("does the claim set close, and under what measure?",
    "E(claim set) > 0 at every audit so far"),
   ("Paschen & Gotze section III",
    "one section, unread"),
   ("Sc VI 6s",
    "committed prediction, unmeasured"),
   ("nine unentered literatures",
    "named, unentered")]
print("\n  OPEN QUESTIONS ADMITTED BY CONTENTS ALREADY PRESENT:\n")
for i,(q,w) in enumerate(Q,1):
    print("   %2d. %s"%(i,q))
    print("       %s"%w)
print("""
     |Q| = %d

  **THE BOOK IS NOT COMPLETE, BY ITS OWN NEW LAW.** And it can say so
  precisely: nine open questions, each named, each admitted by material
  already written.
"""%len(Q))
print("="*76)
print("  AND THE LAW APPLIES TO ITSELF -- CHAPTER 22's RECURSION")
print("="*76)
print("""
  Chapter 22 proves the recursion is structurally stationary: a book
  comprehending a closed index is itself an index. **P19 inherits.**

     Q(Lambda) = empty        would make the LATTICE complete
     Q(book)   = empty        would make the BOOK complete
     and the book is a representation of the lattice, so the second
     REQUIRES the first

  **NEITHER IS EMPTY. AND THE LAW MAKES THAT A STATEMENT RATHER THAN AN
  ADMISSION** -- it says exactly what is missing and what would close it.

  WHICH IS THE POINT: **an incomplete index that can enumerate its own
  open questions is in better condition than a complete-looking one that
  cannot.** E(X) = 0 was never going to be enough, because a structure can
  hold every cell and still have been asked nothing.
""")
print("="*76)
print("  THE TERMINATION CONDITION, AND WHY IT IS REACHABLE")
print("="*76)
print("""
  P7 was corrected once already: closure needs a WELL-FOUNDED MEASURE, not
  a shrinking count. The same applies here. Q has grown at nearly every
  step of this work -- but the questions have narrowed:

     'is V novel?'                            unbounded
     'is V in spectroscopy?'                  one field
     'what is V mathematically?'              one identity
     'does V depend on order?'                one parameter
     'what does order cost?'                  three quantities
     'is there an optimal order?'             one number

  **THE SET GREW AND THE SCOPE FELL.** That is a well-founded descent,
  and it is why P19 is a criterion rather than an impossibility.

  Q(X) = empty is reached not when nobody asks, but when every question
  the contents admit has an answer IN the contents.
""")