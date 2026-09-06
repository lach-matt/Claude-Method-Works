#!/usr/bin/env python3
"""catchup.py -- write this session's findings into the book.

Every edit is an anchored INSERTION or a MOVE. No existing sentence is retyped
except where a claim is withdrawn, and each withdrawal names what replaces it.
A backup was taken before this ran. Invariants are checked afterwards.
"""
import sys, re
from zeno import State, step

P = "The Method 1.4.md"
s = open(P, encoding="utf-8").read()
EDITS = []

def after(anchor, text, name):
    """insert text immediately after the paragraph the anchor begins"""
    global s
    assert s.count(anchor) == 1, f"{name}: anchor not unique ({s.count(anchor)})"
    i = s.index(anchor)
    j = s.index("\n\n", i)
    s = s[:j] + "\n\n" + text.strip("\n") + s[j:]
    EDITS.append(name)

def before(anchor, text, name):
    global s
    assert s.count(anchor) == 1, f"{name}: anchor not unique ({s.count(anchor)})"
    i = s.index(anchor)
    s = s[:i] + text.strip("\n") + "\n\n" + s[i:]
    EDITS.append(name)

def swap(old, new, name):
    global s
    assert s.count(old) == 1, f"{name}: old not unique ({s.count(old)})"
    s = s.replace(old, new)
    EDITS.append(name)

# ---------------------------------------------------------------- 1. the move
# the body prints PART III before chapter 13; the contents places 13 in PART II.
# smallest repair: move the one heading line to sit after §13.4.
def move_part_iii():
    global s
    head = "\n# PART III — THE LAW\n\n## 13."
    assert s.count(head) == 1
    s = s.replace(head, "\n## 13.")
    tgt = "\n## 14. Closure\n"
    assert s.count(tgt) == 1
    s = s.replace(tgt, "\n# PART III — THE LAW\n\n## 14. Closure\n")
    EDITS.append("MOVE  PART III heading, from before ch.13 to before ch.14")

# ------------------------------------------------- 2. attribution, audit 7
def attribution():
    after("**This is not new mathematics and the book gains by saying so.**",
"""
 **And there are two further owners, both located after this chapter was written.** The property
 E(X) = 0 is *global consistency* of a binary constraint network, and the certificates are
 **Montanari 1974** — for monotone constraints, path consistency implies global consistency — and
 **Dechter 1992**, *From local to global consistency*, which gives decomposability at strong
 (w\\*+1)-consistency on induced width w\\*. **Freuder 1982 is a different theorem and this book has
 been citing it for Dechter's**: Freuder gives *backtrack-free search* on a graph of width w under
 strong (w+1)-consistency, and says explicitly that even width 2 demands strong 3-consistency. The
 mis-citation is corrected here and recorded at register 400.

 **And the constraint class has a name.** A binary constraint that is (α, β)-monotone with
 α, β ∈ {≤, ≥} is a **staircase** constraint, and the connected row-convex class containing it is
 closed under composition, intersection and transposition — **Deville, Barták and Van Hentenryck,
 *Artificial Intelligence* 1999**. φ̂ recovers exactly a staircase, so the operator of §6.1 has been
 building a named object since Chapter 6. Register 401.
""", "INSERT §14.1  Montanari, Dechter, Deville; Freuder mis-citation corrected")

# ------------------------------------------------- 3. the closure rule, two-sided
def closure_rule():
    after("### 14.4 The three consequences",
"""
 **First, the rule itself, stated correctly.** This book has said throughout that a tightening
 preserves E = 0 when it binds one coordinate by a monotone function of one other. **That is the
 one-sided reading of a two-sided condition, and it understates the operator.** φ̂ is indexed over
 *ordered* pairs, so φ̂ᵢⱼ and φ̂ⱼᵢ are both built and their conjunction bounds a region from both
 sides. A band — |x − y| ≤ c — is monotone in neither direction and closes at E = 0.

 **The correct statement is already in this book, in Part I.** §2.15.2, the closing result of ten
 recorded failures on §28.3, gives it: *X is ℛ-closed iff X = {(r,c) : c ≤ M(r) and r ≤ N(c)}, with
 M, N the running maxima of its own row and column maxima.* Recomputed on eight regions over a 5 × 5
 box, that characterisation reproduces ℛ-closure exactly — staircases, bands, two-sided intervals and
 the full box close; decreasing bounds, congruences, peaks and disconnected row-convex sets do not.

    **A tightening preserves E = 0 iff each of its binary projections is the intersection
    of that projection's own two upper envelopes.** The monotone rule is the case where one
    of the two is vacuous.

 **Nothing already excluded is readmitted** — a decreasing cap still breaks joins, a congruence still
 breaks meets, a two-parent bound is still arity — so no count in this book moves. What changes is
 that the criterion stops being narrower than the operator, and §17.4's repair and §18.4.1's cap
 table are owed a re-run against the wider form. **The two statements were obtained six chapters
 apart, for different purposes, and neither cited the other.** Register 402.
""", "INSERT §14.4  the two-sided closure rule, bridged to §2.15.2")

# ------------------------------------------------- 4. Chapter 16, three -> six
def defences():
    after("### 16.6 The three defences are disjoint",
"""
 **Three was the count while every defence was built from the object. There are six, and the other
 three reach a coordinate this book does not carry: what a term refers to.**

  mechanism        catches                                        runnable by the book
  ℛ(Λ) = Λ         rules not recoverable from cells               yes
  ⅅ ≥ 1            a wrong value in data or derivation            yes
  χ_Λ total        a missing value coerced to a real one          yes
  §26.8's index    a choice that depended on its answer           yes
  **ⅅ_ref**        **a term meaning one thing here and another in the theorem it was borrowed from**   **no — the verdict must be read**
  **ⅅ_dict**       **drift away from a referent already established**                                  **yes, given the referent**
  **ⅅ_gro**        **a term with no referent at all**                                                  **yes, once the term is placed**

 **Why the first four cannot reach the last three.** All four compare the book against the book. A
 conflation is not a disagreement between two places in this book; it is an *agreement* between the
 book and itself about a word doing different work elsewhere. Twenty-one structural audits passed on
 a companion document carrying five of them.

 **ⅅ_ref and ⅅ_dict are not the same mechanism at two strengths.** Establishing a referent requires
 reading someone else's theorem and is not runnable. *Maintaining* one is mechanical: once a
 coordinate carries a stated referent, checking that every later use is consistent with it is a
 computation. ⅅ_ref is paid once per coordinate; ⅅ_dict runs forever after. The tower's 2K is the
 worked case — it means J_c + ℓ_outer in jK, L_total + S_core in LK, and jj has no K at all, and
 Racah's recoupling coefficients translate between them exactly.

 **ⅅ_gro is the one with no instance anywhere until now.** *q*, this book's transfer coordinate, has
 no referent in the spectroscopic literature — not conflated, since there is nothing to conflate
 with. ⅅ_ref cannot see it: if no theorem names the term, the pair never enters the table.

 **And the three repairs are already named, in the companion paper, without being named as
 defences**: SPLIT for a conflation, DICTIONARY for one meaning in two bases, TRANSLATOR for a
 referent that must be manufactured. Register 403.
""", "INSERT §16.6  three defences become six")

# ------------------------------------------------- 5. the reference index
def refindex():
    after("### 16.6 The three defences are disjoint",
"""
### 16.6.1 The vocabulary of reference, as an index

 The three new mechanisms need a vocabulary this book does not have: its back-matter Index carries
 fifty-one terms and **not one of them says what a term points at**. Defined here on the same
 discipline as every other index in this book — ordered coordinates, one categorical fibre,
 constraints of §16.4 form.

  coordinate   values
  access       blocked < secondary < abstract < full text
  referent     none < named < named with its stated hypothesis
  checked      not checked < against one theorem < against every theorem naming it
  verdict      undetermined < conflated < partial < match

 fibred by **kind** — coordinate · equation · source · result. *Repair* — none, dictionary, split,
 translator — is **not a coordinate**: it is a function of verdict and referent, and §1.7 forbids a
 derived coordinate. It is read off.

 **38 cells, ambient box 144, density 26.4%, E = 0** — the densest object in this book after the
 periodic table. **And it is not a tree**: access bounds *referent at its top value* and bounds
 *checked* directly, closing the cycle access–referent–checked. Width 2, so Freuder cannot be
 inherited and the zero above is a computation rather than a certificate — §12.11.0.4's Λ₉′ arriving
 in the vocabulary rather than in the lattice.

 **Applied to twenty-eight load-bearing terms of this book and its companion: thirteen cells
 occupied of thirty-eight, E = 11.** One term with no referent, eight named and never checked, nine
 checked and conflated, two partial, eight matching, four capped by a blocked source. **Sixty-eight
 per cent have been checked at all.**

 **One constraint was withdrawn during construction and the withdrawal is the finding.** The index
 first required a named referent to have a reachable source, and refused four cells the book
 occupies — Edlén 1964, Ritz 1908, Paschen & Götze 1922, Dunz 1911. §19.5 already says otherwise:
 *a blocked ρ = 1 cell is a stated gap, not an unexplained absence.* Naming a referent and reading
 one are different acts. Totality forbade rather than detected, exactly as §16.5 says it does, and
 what it forbade located the wrong constraint. Register 404.
""", "INSERT §16.6.1  the reference index, defined and applied")

# ------------------------------------------------- 6. D = 0 on verdict
def dzero():
    after("### 16.6 The three defences are disjoint",
"""
### 16.6.2 And one coordinate sits below this book's own floor

 §16.1 gives ⅅ ≥ 1 as the condition under which an index can check itself, and every defence in this
 book rests on it. **The reference index has one coordinate for which ⅅ = 0, permanently.**

 Three of its four coordinates are internal: *access*, *referent* and *checked* are all recordable
 from this book's own pages. **Verdict is not.** It requires reading someone else's theorem, and the
 index that supplies it is the bibliography — for which §27.1 already proves ⅅ(novelty) = 0,
 necessarily and permanently, because search is one route and can never be two.

    ⅅ(bibliography) = 0 ⟹ ⅅ(verdict) = 0, inherited.

 **So the reference debt is not unpayable because sources are blocked.** Blocked access caps four of
 twenty-eight terms at a lower level. The undefendability of *verdict* caps all twenty-eight, and it
 is the first coordinate anywhere in this book below the ⅅ ≥ 1 floor the rest of Chapter 16 stands
 on. Register 405.
""", "INSERT §16.6.2  D(verdict) = 0 inherited from the bibliography")

# ------------------------------------------------- 7. the four-body shape
def shape():
    after("**And this book is a three-body object.**",
"""
 **And it is a four-body object, on evidence gathered after that paragraph was written.**
 REFERENCE — what this book's terms point at — is a fourth part, and the test that it is a *node*
 rather than a relation is the one the companion paper uses to withdraw a false node of its own:
 status is one bit per part, and the partition forces one-hot. Over two term lists neither of them
 chosen for this purpose, **six terms predicate on reference alone** — *referent, ungrounded, stated
 hypothesis, access grade, vocabulary, dictionary* — **and none is content of any other part.**

 **The decisive figure is a zero.** This book's own back-matter Index carries fifty-one author-chosen
 terms and **none of them predicates on reference, and none of them is a relation term at all.** A
 book with no vocabulary for what a coordinate refers to is what a book missing this node looks like
 from inside.

 **All six edges are witnessed**, each by a term from a list drawn rather than composed: *cap/frame*
 for object–law, *computable* for object–procedure, *falsification test* for law–procedure,
 *conflated* for object–reference, *jurisdiction* and *precedent* for law–reference, *term-sharing
 pair* for procedure–reference. **Four nodes, six edges, complete, width 3** — computed exactly by
 elimination over all orderings.

 **And the shortfall is a magnitude rather than a fact.** ℛ is 2-decomposable and verified equal to
 binary path consistency on every object in this book. By Freuder a width-3 graph needs strong
 4-consistency for backtrack-free search; by Dechter, strong (w\\*+1)-consistency gives
 decomposability. **The operator reaches level 2 and the object requires level 4.** E(this book) > 0
 was already a theorem about its shape; the fourth node doubles the deficit, and no amount of work on
 the object, the law or the procedure closes it, because the shortfall is in the consistency level
 the operator reaches and not in the diligence with which it is applied.

 **What would refute it, and it is cheap.** Exhibit a term this book uses that predicates on
 reference alone and is already content of another part, and reference collapses to a relation; or
 show that one of the six edges has no relation term, and the width drops to 2. Both were run and
 neither fired. Register 406.
""", "INSERT §18.4.1  the four-body shape, tested")

# ------------------------------------------------- 8. three-parent decisions
def threeparent():
    after("**This is §12.11's dichotomy, arriving in the one place",
"""
 **And with the fourth node of §18.4.1 the count goes to three.** In a triangle every node has degree
 two, so a decision has at most two parents; in K₄ every node has degree three. **Three-parent
 decisions exist and each resisted for the same reason** — none can be delegated to one predecessor
 or deferred until one is settled:

  the decision                        its three parents
  is Λ the clean control?             the object (976 cells, E = 0) · the law (what E = 0 certifies) ·
                                      reference (seven of thirteen letters conflated)
  is the closure rule correct?        the object (Λ closes) · the law (the admissibility criterion) ·
                                      reference (what *monotone* names in the constraint literature)
  is E(audits) meaningful?            the procedure (the set) · the law (the coordinate list, a frame) ·
                                      reference (whether *audit* means one thing across it)

 **Two instances was not a law and three is not much better**, which §18.4.1 says of its own
 prediction and which this section repeats of the extension. What is worth recording is that the
 three were not gathered for the test: each arrived as a difficulty before the shape was drawn.
 Register 407.
""", "INSERT §2.18.1  three-parent decisions")

# ------------------------------------------------- 9. the four cuts explained
def cuts():
    after("**And the balance is not special to the transfer.**",
"""
 **And the reason it is exactly four is the tree.** Deleting a coordinate splits the constraint graph
 into two components precisely when that coordinate is an internal vertex of degree two. n, e and 2S
 are leaves and deleting one leaves a single component; k has degree three and deleting it leaves
 three. **ℓ, q, f and g are the caterpillar's four internal degree-two vertices, and they are the
 only two-sided cuts that exist.** Recomputed on the tree rather than on coordinate order: defect
 zero at every one of the four, and the other four are not two-sided cuts at all. The list was
 complete when it was written and never said why. Register 408.
""", "INSERT §12.11.0.8  why exactly four cuts")

# ------------------------------------------------- 10. order dimension derived
def dimension():
    after("### 8.6 Order dimension",
"""
 **And it is asserted here rather than derived, which this section now says.** The order dimension of
 a finite distributive lattice is the width of its poset of join-irreducibles — Dilworth — so
 dim(Λ₈) = 8 follows from §8.3's seventeen generators rather than standing on its own. It is the one
 quantity in Part II carried without a derivation, found by building the dependency graph of this
 book's mathematics and looking for objects nothing derives. Register 409.
""", "INSERT §8.6  the dimension is Dilworth's, not free-standing")

# ------------------------------------------------- 11. register
def register():
    after("397. **A past value quoted as history",
"""
 398. **Λ is not the clean control.** Audited from outside against Condon–Shortley and Racah, seven of
 thirteen letters are conflated, *q* is ungrounded and one quantity is read and never indexed. No
 computed figure moves — E(Λ) = 0 reproduces at 112 of 112 checks — and Λ loses its role. **Closure
 states that the cells are mutually consistent and says nothing about whether the coordinates refer
 to anything.** §30.1.1 gains flag 8.

 399. **Every mathematical expression in this work connects to another, and did not.** Built as a
 dependency graph over 132 registered objects, the corpus falls into **six components**: the operator
 and the lattice, the bracket and the cost surface, modular theory, and three fragments. **Eleven
 edges close it to one**, ten of them quotable from prose that asserts the connection without
 carrying it — §25.2's *E is the slack counted, the void is the slack counted over an interval, V is
 the slack measured* is the only thing joining Part IV to Part II, and it is a sentence.

 400. **Freuder was cited for Dechter's theorem.** Freuder 1982 gives backtrack-free search at strong
 (w+1)-consistency on width w; the global-consistency form is Dechter 1992, which this book lists and
 cites for nothing. Corrected at §14.1.

 401. **Deville, Barták and Van Hentenryck 1999 name the operator's constraint class**: a
 (α,β)-monotone binary constraint is a *staircase*, and connected row-convexity is the class path
 consistency decides. Entered.

 402. **The closure rule was one-sided and the operator is two-sided.** φ̂ runs over ordered pairs, so
 a band closes at E = 0 where the stated rule refuses it. The correct characterisation was already at
 §2.15.2, six chapters away, obtained from ten failures on the reorderability problem. Nothing
 excluded is readmitted; the criterion stops being narrower than the operator.

 403. **Chapter 16's three defences are six.** ⅅ_ref, ⅅ_dict and ⅅ_gro reach a coordinate no index
 here carried. Twenty-one structural audits passed on a document containing five conflations, because
 all twenty-one compare the book against the book.

 404. **The reference index refused four cells the book occupies** — the four blocked pre-digital
 sources — and the refusal located a wrong constraint of mine rather than a defect of theirs. Naming
 a referent and reading one are different acts, which §19.5 already said.

 405. **ⅅ(verdict) = 0, inherited from the bibliography**, which §27.1 proves undefendable. The first
 coordinate in this book below the ⅅ ≥ 1 floor the whole of Chapter 16 stands on.

 406. **A fourth node, and the width goes to 3.** Reference passes the one-hot test on two term lists
 neither of them composed for it, all six edges are witnessed, and both available refutations were
 run and did not fire. The operator reaches consistency level 2 and the object requires level 4.

 407. **Three-parent decisions, three found**, none gathered for the test.

 408. **The four two-sided cuts are the caterpillar's four internal degree-two vertices**, which is
 why there are four. The list was right and unexplained.

 409. **dim(Λ₈) = 8 was asserted and is Dilworth's**, being the width of J(Λ). Found by building the
 dependency graph and looking for what nothing derives.

 410. **§18.6.1 gains a fifth index and §16.7.1 a third verdict.** The bibliography, indexed on era,
 ρ, access and depth of entry, holds 22 sources over 7 cells with E = 6 — **the only non-zero
 prediction budget in this method, and the only one whose cells can be occupied.** Under exhaustive
 relabelling E falls to 2 and never to 0, so it is irreducible in §16.7.1's sense and unlike the
 asteroid belt its absences are fillable. *Irreducible does not mean unoccupiable.*

 411. **Three verifications of mine were wrong in one session and the book was right every time**:
 the tree cut taken on coordinate order, Aitken indexed from the wrong end of its triple, and an
 invariant checker reading the wrong table *while executing §2.19's own condition (v)*. §3.4 records
 the same thing happening twice to the whitespace audit. **An audit is not exempt from the discipline
 it enforces**, and §4.1 — attribute inward first — earned its place three times over.
""", "INSERT §26.7  register 398–411")

with State("catchup") as st:
    step(st, "move the PART III heading", move_part_iii, budget=20)
    step(st, "attribution: Montanari, Dechter, Deville", attribution, budget=20)
    step(st, "the two-sided closure rule", closure_rule, budget=20)
    step(st, "D(verdict) = 0", dzero, budget=20)
    step(st, "the reference index", refindex, budget=20)
    step(st, "three defences become six", defences, budget=20)
    step(st, "the four-body shape", shape, budget=20)
    step(st, "three-parent decisions", threeparent, budget=20)
    step(st, "why exactly four cuts", cuts, budget=20)
    step(st, "order dimension is Dilworth's", dimension, budget=20)
    step(st, "register 398-411", register, budget=20)

open(P, "w", encoding="utf-8").write(s)
print(f"\n  {len(EDITS)} edits written")
for e in EDITS: print(f"    {e}")
print(f"\n  source {len(s):,} chars (was 665,{'':0})")
