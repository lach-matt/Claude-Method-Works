import numpy as np
print("="*88)
print("  DOES 'INDEXED' IMPLY 'COMPLETELY DEFINED'?  P20 ALREADY ANSWERS THIS")
print("="*88)
print("""
  P20: the language in which a question is posed bounds whether it can
  close.

     monotone two-variable bounds  ->  closes in one pass
     polynomial relations          ->  closes, by Groebner basis
     **full arithmetic             ->  DOES NOT CLOSE   (Godel)**

  **Celestial mechanics and string theory are stated in full arithmetic.**
  Real numbers, differential equations, quantifiers over functions. By the
  book's own principle they cannot be completely defined by any index.
""")
print("="*88)
print("  SO WHAT WAS ACTUALLY ESTABLISHED?  AN HONEST TALLY")
print("="*88)
CEL=[("Lagrange points in mu","INDEXED","5 cells, closed, E=0, brackets 18/18"),
     ("mean-motion resonances","INDEXED","13 occupied cells, E=2, order cut recovered"),
     ("Hill stability boundary","BRACKETABLE","monotone, convex, V~100 — no index built"),
     ("planetary semi-major axes","BRACKETABLE","monotone; sign change at Jupiter-Saturn"),
     ("satellite systems","BOUND ONLY","Hill radius caps a_moon; no index built"),
     ("periodic orbit families","UNTESTED","braid catalogues exist; E(X) never computed"),
     ("three-body trajectories","NOT INDEXABLE","sensitive dependence destroys monotonicity"),
     ("the n-body problem in general","NOT INDEXABLE","full arithmetic; P20 forbids closure")]
STR=[("mass spectrum m^2 = (N-1)/a'","INDEXED","linear in N — exactly on the pole"),
     ("level degeneracy d(N)","BRACKETABLE","monotone, convex, 3-monotone in log"),
     ("partition function","SAME OBJECT AS F","generating function, counts not booleans"),
     ("Calabi-Yau Hodge pairs","UNTESTED","(h11,h21) catalogue; E(X) never computed"),
     ("mirror symmetry","UNTESTED","should be Section 3.3's self-duality"),
     ("the landscape","NOT INDEXABLE","no monotone coordinatisation known"),
     ("dualities in general","NOT INDEXABLE","not order-preserving maps"),
     ("the theory itself","NOT INDEXABLE","full arithmetic; P20 forbids closure")]
for nm,L in [("CELESTIAL MECHANICS",CEL),("STRING THEORY",STR)]:
    print("\n  %s\n"%nm)
    print("  %-32s%-18s%s"%("object","status","evidence"))
    print("  "+"-"*84)
    for a,b,c in L: print("  %-32s%-18s%s"%(a,b,c[:34]))
    ix=sum(1 for _,b,_ in L if b in ("INDEXED","SAME OBJECT AS F"))
    br=sum(1 for _,b,_ in L if b in ("BRACKETABLE","BOUND ONLY"))
    un=sum(1 for _,b,_ in L if b=="UNTESTED")
    no=sum(1 for _,b,_ in L if b=="NOT INDEXABLE")
    print("\n     indexed %d   bracketable %d   untested %d   not indexable %d"%(ix,br,un,no))
print("="*88)
print("  THE CLAIM, TESTED")
print("="*88)
print("""
  **'We can define each completely' is FALSE as stated, and the book says
  why in two places.**

     P20  full arithmetic does not close. Both subjects are stated in it.

     P19  completeness requires Q(X) = 0 — every question about the
          contents answered FROM the contents. **Neither subject's Q is
          even enumerable**, let alone empty.

  **WHAT IS TRUE IS NARROWER AND STILL SUBSTANTIAL:**

     the INDEXED objects are completely defined, because that is what an
     index with E = 0 means. Five Lagrange points, thirteen resonances,
     the string mass spectrum: **each is exactly determined by its cells
     and its bounds, and no question about their contents is open.**

     the BRACKETABLE objects are bounded but not defined. Hill stability
     has a deductive interval and no closed index.

     the UNTESTED are a programme.

     the NOT INDEXABLE are not a gap in the work. **They are outside the
     language, and P20 says no amount of work brings them in.**
""")
print("="*88)
print("  AND THE DISTINCTION MATTERS BECAUSE OF P22")
print("="*88)
print("""
  P22: a complete index admits no lie, because every rule is content and a
  false cell contradicts stated content.

  **That protection extends exactly as far as the index does.** The five
  Lagrange points are lie-proof in the book's sense. **A claim about a
  chaotic trajectory is not**, and cannot be made so, because there is no
  index to contradict.

  **So the honest form of the claim is:**

     'celestial mechanics and string theory are included in the index'
        -> FALSE

     'certain families within each are indexed, and those families are
      completely defined and lie-proof; the rest is bracketed, untested,
      or outside the language'
        -> TRUE, and it is the strongest form available

  **CORRECTION 114**, entered against a claim I would otherwise have
  accepted: the transfer is real and partial, and calling it total would
  be exactly the coherent fabrication of Section 10.7.2 — a complete,
  consistent account of something that is not there.
""")