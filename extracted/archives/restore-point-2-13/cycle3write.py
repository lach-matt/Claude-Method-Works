#!/usr/bin/env python3
"""cycle3write.py -- STEP 4 of the cycle. Book and bibliography, no output."""
from zeno import State, step
P="The Method 1.6.md"; s=open(P,encoding="utf-8").read(); N=[]
def after(a,t,n):
    global s
    assert s.count(a)==1, f"{n}: {s.count(a)}"
    i=s.index(a); j=s.index("\n\n",i)
    s=s[:j]+"\n\n"+t.strip("\n")+s[j:]; N.append(n)
def swap(a,b,n):
    global s
    assert s.count(a)==1, f"{n}: {s.count(a)}"
    s=s.replace(a,b); N.append(n)

def moore():
    after("### 14.4 The three consequences",
"""
### 14.5 The family of all closed sets

 A closed index is one object. **The closed subsets of a closed index are a family**, and this book
 has carried the question of what that family is since Λ was built. It is answerable by enumeration
 at small size, and the answer is standard once it is seen.

  ambient        cells   closed subsets   of 2ⁿ    ∩ closed   ∪ closed
  2 × 2 × 2          8       **73**       28.5%     **100%**     64.4%
  3 × 3              9      **146**       28.5%     **100%**     68.3%
  2 × 2 × 2 × 2     16      **731**        1.1%     **100%**     32.6%

    **The closed sets of ℛ form a MOORE FAMILY: closed under intersection, containing
    the whole index, and NOT closed under union.**

 That is the standard fact about any closure operator — the closed sets of a closure operator are a
 Moore family, and the correspondence between operators, families and lattices is cryptomorphic. **It
 is worth stating here because the asymmetry is ℛ's own, one level up.** ℛ carries meets and refuses
 joins in §14.2; its family of fixed points does the same, at 100% against 32–68%.

 **And it is the setting in which register 458's finding lives.** Λ₉ is closed and 300 of 300 random
 subsets of it are open, because the closed ones are a Moore family inside a power set — a vanishing
 minority, and the only place from which the open ones can be measured.

 **The count for Λ itself is open.** Brute force is 2⁹⁷⁶. The Moore-family structure gives the route,
 since a Moore family is determined by its meet-irreducible members, and §8.4 already counts those
 for Λ under a different name. Q item R. Register 461.
""","INSERT §14.5  the family of all closed sets")

def coverage():
    after("**Criterion.** δ⁻¹(T) is a sublattice of Λ **iff",
"""
 **How much of the family this supplies, measured.** Every convex preimage is closed — the criterion
 is sound in the direction it is used. **It is nowhere near complete**: on the three ambients of
 §14.5 the convex preimages are **8.2%, 10.3% and 0.8%** of all closed subsets. So the criterion
 decides the constraints this book actually imposes and does not enumerate the closed sets. **A
 sufficient condition tested for necessity and found to be a small part of what it describes**, which
 is what §4.6 asks of any criterion before it is relied on.
""","INSERT §17.3  the criterion's coverage")

def biblio():
    swap("""Galois connections / formal concept analysis. — E(X) as a closure defect; the general setting for ℛ.""",
"""Galois connections and formal concept analysis. — E(X) as a closure defect; the general setting for
 ℛ. **This entry named a field and no work, alone among the thirteen in this section, until §2.23's
 own requirement was turned on it.** · **Caspard, N. & Monjardet, B.** (2003). The lattices of
 closure systems, closure operators, and implicational systems on a finite set: a survey. *Discrete
 Applied Mathematics* **127**(2), 241–269. — the standard survey of the setting; cited for the
 cryptomorphism between closure operators, Moore families and closure systems, which §14.5 uses.
 **[S] located through the enumeration literature, not read in full.** · **Colomb, P., Irlande, A. &
 Raynaud, O.** (2010). Counting of Moore families for n = 7. *Formal Concept Analysis*, LNCS 5986,
 72–87. — cited for the distinction §14.5 turns on: that literature counts **how many closure systems
 exist** on n elements, 1, 2, 7, 61, 2 480, 1 385 552, 75 973 751 474, where §14.5 counts **how many
 closed sets one operator has.** Different questions, and theirs is the harder. **[S]**""",
 "SWAP References  the FCA entry gains its works")

def reg():
    after("460. **The press hardcoded the title block",
"""
 461. **The family of all closed sets has its first numbers, and it is a Moore family.** 73, 146 and
 731 closed subsets of ambients at 8, 9 and 16 cells — **intersection-closed at 100%, union-closed at
 32 to 68%.** ℛ's own asymmetry, reproduced by its fixed points. The count for Λ is open at 2⁹⁷⁶ by
 brute force and the route is the meet-irreducibles. Q item R.

 462. **§17.3's convexity criterion is sound and covers 0.8 to 10.3% of the family it describes.**
 Every convex preimage is closed; the closed sets are overwhelmingly not convex preimages. **A
 sufficient condition tested for necessity**, which §4.6 requires before a criterion is relied on and
 which had not been done.

 463. **One bibliography entry named a field and no work** — *Galois connections / formal concept
 analysis* — alone among thirteen in its section, and it is the entry naming **the general setting
 for ℛ.** §2.23 requires a closed index to be stated by its expression; the same demand turned on the
 References found the one place where the book cites a subject rather than a source. Caspard &
 Monjardet's survey and Colomb, Irlande & Raynaud's count are entered, both **[S]**.

 464. **The cycle gains a fourth step.** Fill to the limit from what exists · search, **beginning
 with this book's own bibliography index** · reassess the mathematics · **write the book and the
 bibliography, without building.** Step 2's amendment paid on its first run: the References named the
 setting before any external search did, and named it defectively, which is how 463 was found.
""","INSERT §28.7  registers 461-464")

with State("cycle3write") as st:
    for f in (moore, coverage, biblio, reg): step(st, f.__name__, f, budget=30)
open(P,"w",encoding="utf-8").write(s)
print(f"  {len(N)} edits"); [print("   ",x) for x in N]
