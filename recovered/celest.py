import numpy as np
from itertools import product
from collections import Counter
print("="*88)
print("  THE INDEX READ AS CELESTIAL MECHANICS — WHAT SURVIVES TRANSLATION?")
print("="*88)
print("""
  P21 says a definition must be true in every language. Celestial mechanics
  is not a mathematical language, so this is not a P21 test. It is a test
  of whether the STRUCTURES have counterparts — and where they fail to,
  that failure is the informative part.
""")
MAP=[
 ("Λ, the cell set","the set of admissible configurations",
  "phase space? NO — Λ is a set of DISCRETE labels, phase space is continuous",0),
 ("a channel: one ℓ, one series in n","a FAMILY: one topology, one continuation parameter",
  "periodic-orbit families indexed by braid word; Lagrange points in μ",1),
 ("monotone bound x_i ≤ φ(x_j)","a conserved inequality along a family",
  "Sundman: I''= 2E+U bounds collapse; Hill regions nest with Jacobi constant",1),
 ("the bracket T(n±1)","two neighbouring members of a family",
  "verified: 18 of 18 on L1,L2,L3 across k=1..3",1),
 ("V = 4|y'/y''|/h","the cost of a guaranteed continuation step",
  "L1 24.6 · L2 12.4 · L3 16,423 · L4/L5 infinite",1),
 ("the pole at p = 1","exact linear dependence on the parameter",
  "L4/L5: x = 1/2 − μ exactly. Bracket unnecessary, not worthless",1),
 ("refusal: wrong sign of Δ^k","a BIFURCATION along the family",
  "same instrument, no fit, no equations of motion",1),
 ("E(X), the closure defect","families the classification admits and nobody has found",
  "the braid-word catalogues are exactly this kind of object",1),
 ("𝒟, two disjoint routes","two independent continuations to the same orbit",
  "e.g. continuation in μ and in energy meeting at the same solution",1),
 ("the Pauli coupling g ≤ 2(2f+1)","an EXCLUSION that is physics, not counting",
  "no counterpart: gravity excludes nothing by occupancy",0),
 ("2S as an inert leaf","a label that scales the count and changes no structure",
  "no clean counterpart",0),
 ("the caterpillar tree","the dependency graph of the constraints",
  "unknown for orbit families — nobody has drawn it",-1),
 ("the single expression F","a generating function for the family catalogue",
  "unknown — would require the constraint graph first",-1),
 ("closure 𝓡(X) = X","the catalogue implies its own admissibility rules",
  "untested on any orbit catalogue",-1),
]
print("  %-30s%-40s%s"%("in the index","in celestial mechanics","status"))
print("  "+"-"*86)
for a,b,c,s in MAP:
    tag={1:"TRANSFERS",0:"NO COUNTERPART",-1:"UNTESTED"}[s]
    print("  %-30s%-40s%s"%(a[:30],b[:40],tag))
n1=sum(1 for *_,s in MAP if s==1); n0=sum(1 for *_,s in MAP if s==0); nm=sum(1 for *_,s in MAP if s==-1)
print("\n     transfers %d   no counterpart %d   untested %d"%(n1,n0,nm))
print("="*88)
print("  AND THE THREE THAT DO NOT TRANSFER ARE ONE THING")
print("="*88)
print("""
  The Pauli coupling, the inert spin leaf, and the discrete cell set all
  fail for the same reason:

     **Λ's coordinates are OCCUPANCY NUMBERS. They count how many
       electrons are in a state, and exclusion caps them.**

     **Celestial mechanics has no occupancy.** Three bodies may occupy any
     configuration; nothing forbids two orbits from being arbitrarily
     close. There is no Pauli principle for masses.

  **So the single non-counting bound in the whole lattice — Section 6.5's
  one coupling — is precisely the thing with no gravitational analogue.**
  Everything else in the index is counting and ordering, and counting and
  ordering transfer.
""")
print("="*88)
print("  WHICH MAKES A PREDICTION ABOUT THE EXPRESSION")
print("="*88)
print("""
  §6.5: the min(q, 4f+2) coupling is the ONLY non-product term in F.
  Remove it and F becomes a pure product of independent sums.

  **A celestial-mechanics index has no such coupling. So its generating
  function should factorise COMPLETELY** — no min, no truncation, a bare
  product over the family's parameters.
""")
def count(coupled):
    t=0
    for n in range(1,4):
      for l in range(0,2):
        if l>n-1: continue
        for k in range(1,min(4*l+2,3)+1):
          inn=0
          for q in range(0,4):
            if q>k: continue
            for e in range(1,4):
              for f in range(0,2):
                if f>e-1: continue
                inn+=len([g for g in range(0,4) if g<=(min(q,4*f+2) if coupled else q)])
          t+=(k+1)*inn
    return t
print("     Λ with the exclusion coupling  : %d cells"%count(True))
print("     Λ without it (a 'gravitational' analogue) : %d cells"%count(False))
print("     the coupling removes %d — and only those 24 make F non-product"%(count(False)-count(True)))
print("="*88)
print("  THE THREE UNTESTED ITEMS ARE THE PROGRAMME")
print("="*88)
print("""
  **Does a periodic-orbit catalogue close?** Take Šuvakov–Dmitrašinović's
  free-group classification, or any braid-word catalogue, index it by
  (word length, symmetry class, angular momentum sign, stability), and
  compute E(X). **If E > 0 the classification names families nobody has
  integrated.** That is Chapter 1's question, asked of a different table.

  **What is the constraint graph?** Λ's is a caterpillar and that is why a
  single expression exists. **Nobody has drawn the equivalent for orbit
  families**, and until someone does, no closed count is available.

  **And 𝒟 is already available and unused.** Two independent continuations
  reaching the same orbit is exactly 𝒟 = 1, and continuation codes compute
  both routinely without ever comparing them as a check.
""")
print("="*88)
print("  WHAT THE TRANSLATION SHOWS ABOUT THE BOOK")
print("="*88)
print("""
  **The index divides into two parts and only now is the division visible:**

     COUNTING AND ORDERING     transfers wholesale — the bracket, V, the
                               pole, refusal, E(X), 𝒟
     OCCUPANCY AND EXCLUSION   does not transfer at all — the one coupling,
                               the spin leaf, the discreteness of cells

  **And the book presents them as one thing.** Chapter 2 builds Λ from
  quantum numbers as though the exclusion bound were the same kind of
  object as ℓ ≤ n−1. **It is not. Six of the seven constraints are
  bookkeeping; one is physics**, and the celestial reading is what makes
  that legible.
""")