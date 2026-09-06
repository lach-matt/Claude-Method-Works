print("="*100)
print("  EVERY PERCEPTION OF THE QUESTION")
print("="*100)
P=[
(1,"running maxima","does an ordering make M* and N* mutual?","the original §23.4 framing","d=2 only — the formula is 2-D"),
(2,"sublattice","does a relabelling make X closed under join and meet?","**IDENTIFICATION** — 1,487 + 828 instances, 0 disagreements, confirmed on Λ","every d — the definitive form"),
(3,"interval matrix","is X C1P with monotone interval endpoints?","**PROVED at d=2** — 4 lemmas","d=2 exactly; does not lift"),
(4,"CSP","is the constraint system on axis orders satisfiable?","arity = axes on which two cells differ","**explains WHY d=2 is P: arity ≤ 2**"),
(5,"PQ-tree frontier","is there a frontier with no strict nesting?","the d=2 procedure; 9 tree attempts at d≥3","d=2 built and verified"),
(6,"forbidden substructure","does X avoid every obstruction?","**ROUTE CLOSED** — Tucker's families unbounded across boxes","and REOPENED: finite within any box"),
(7,"construction grammar","is X reachable by the six preserving rules?","6 rules at 100%; disjoint union 6%","**certifies every index the book builds**"),
(8,"generation / inversion","is X in the generated family?","**d=2 VERIFIED 3 ways, 984× cheaper**; d=3 lift failed 281/319","d=2 only"),
(9,"critical cell","which single cell decides it?","**81% at distance 1**; T7 tops it 94%","cell space is LINEAR, not factorial"),
(10,"shape","what is the multiset {T7(z)}?","monotone 0.883 -> 0.014 across max T7 0..6","a graded measure, not a decision"),
(11,"valid-order set","is the set of valid orders non-empty?","**DISCONNECTED** — 1.66-2.19 components; orbits of identical-fibre swaps, exact 493/493","rules out local search"),
(12,"monotone closure","does forced propagation reach a contradiction?","seed-free, sound, **0 of 547 rejections** — never fires","inert"),
(13,"distance","is X at cell-distance 0 from reorderable?","median distance 1; greedy 65%","reframes as repair, not decision"),
]
print("\n  %3s%-22s%-46s%s"%("#","perception","what it asks","status"))
print("  "+"-"*136)
for n,nm,q,f,s in P: print("  %3d%-22s%-46s%s"%(n,nm,q[:46],s[:52]))
print("="*100)
print("  HOW THEY RELATE")
print("="*100)
print("""
  **EQUIVALENT to the question (proved or measured to 0 disagreements):**
     2 sublattice · 11 valid-order-set non-empty · 1 running maxima (d=2)
     3 interval matrix (d=2, proved)

  **EXPLANATORY — they say WHY, not WHETHER:**
     4 CSP arity        — d=2 is P because the constraints are binary
     6 obstructions     — why no local test succeeds; and finite per box
     11 disconnection   — why local search plateaus at 96-97%
     9 distance         — why global criteria all reached 58-77%

  **CONSTRUCTIVE — they produce rather than decide:**
     7 grammar          — certifies BUILT indices, including Λ
     8 generation       — produces the family; d=2 verified, d=3 not

  **GRADED — they measure rather than decide:**
     10 shape           — 60-fold discrimination, no threshold
     13 distance        — repair cost, not membership

  **INERT:**
     12 propagation     — sound and never fires
""")
print("="*100)
print("  WHAT THE COLLECTION SAYS THAT NO SINGLE PERCEPTION DOES")
print("="*100)
print("""
  **1. The question has TWO answers, not one.**
     For a BUILT index — one arriving with a derivation — perception 7
     answers it with no search. **Λ: box -> interval -> sublattice ->
     product.** For an ARBITRARY set, perceptions 2-6 apply and none decides
     at d ≥ 3.

  **2. Every perception that DECIDES is 2-dimensional.**
     1, 3, 5, 8 all work at d = 2 and none lifts. **Perception 4 says why:
     the arity is the dimension, and binary CSPs are the tractable ones.**

  **3. Every perception that lifts is EXPLANATORY, not decisive.**
     2, 6, 9, 10, 11 hold at every d and none decides. **They bound the
     answer from both sides and meet nowhere.**

  **4. The one perception nobody had at the start is the one that reframed
     the search space.**
     Perception 9: the space is the CELLS (linear), not the ORDERS
     (factorial). **It arrived last and it is the only one that changes the
     size of the problem.**

  > **So the missing object is not a decision procedure. It is the d ≥ 3
  > member of the family {1,3,5,8} — the perceptions that decide — and every
  > one of those is a STRUCTURE, not an algorithm.**
""")
print("="*100)
print("  AND THE PERCEPTION NOT YET TRIED")
print("="*100)
print("""
  The four deciding perceptions are: a formula (1), a matrix property (3), a
  tree (5), a generator (8). **All four are d = 2 objects.**

  **The collection is missing a perception that is d-dimensional BY
  CONSTRUCTION rather than by generalisation.** Perception 9 is the only
  candidate — the cell space has no dimension dependence at all.

  > **A decision procedure in cell space would be the first perception whose
  > form does not change with d.** That is what has not been tried, and
  > perception 9 arrived too late in the day to be built.
""")