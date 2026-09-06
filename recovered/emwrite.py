#!/usr/bin/env python3
"""emwrite.py -- the electromagnetic index, written as an object."""
from zeno import State, step
P="The Method 1.4.md"; s=open(P,encoding="utf-8").read(); N=[]
def after(a,t,n):
    global s
    assert s.count(a)==1, f"{n}: {s.count(a)}"
    i=s.index(a); j=s.index("\n\n",i)
    s=s[:j]+"\n\n"+t.strip("\n")+s[j:]; N.append(n)

def sec():
    after("### 12.11.4 Precision is path-dependent; physics is not",
"""
### 12.11.6 The electromagnetic index, and it was inside Λ all along

 A cell of Λ is called a transition, and a transition is not an atomic event — it is an
 electromagnetic one. Whether a photon connects two configurations is decided by multipolarity,
 parity and the angular momentum the field carries. **None of that is a coordinate of Λ. All of it is
 a function of Λ's coordinates.**

 **What Λ supplies, and what it does not.** Λ's cells give a source (n, ℓ, k, 2S) and a target
 (e, f, g, 2S′, v, 2J_c, 2K, 2J). **There is no source J** — the tower builds J on the target side
 only. So exactly two electromagnetic quantities are available:

    Δℓ = f − ℓ      at Λ₈        ΔS = 2S′ − 2S      at Λ₉

 and |ΔJ| is available at no level of the tower. The multipole is therefore determined by Δℓ and
 parity alone: **Δℓ = 0 → M1, Δℓ = 1 → E1, Δℓ = 2 → E2, Δℓ = 3 → E3**, the lowest whose parity
 matches. The map was validated against nine textbook classifications before use and shown able to
 refuse, per §4.6.

 **The image, and it is a rectangle.** All 1,654 cells of Λ₉ map, onto eight cells:

  multipole   ΔS = 0   ΔS = 1   ΔS = 2   ΔS = 3
  E1             264      342      180       54
  M1             262      337      171       44

 **E = 0, and the zero is worth nothing**, because the image is the complete product — 2 × 4 here,
 and 4 × 11 at caps (5,5,3,10,3). Register 333's warning, in a new place: a closure test passes on a
 full box for free. **What the rectangle says is that Δℓ and ΔS are independent in Λ: every multipole
 occurs with every spin change.**

    **Λ imposes no electromagnetic constraint at all.** 576 of its Λ₉ cells are E1
    transitions with ΔS ≠ 0 — intercombination lines, which LS coupling forbids.

 **Half the missing law can be imposed and half cannot**, and §17.3's criterion says which in advance:

  rule                as a set                convex in range?   imposed on Λ₉
  ΔS = 0, spin        σ⁻¹({0})                **yes**            526 cells, **E = 0**
  |Δℓ| = 1, parity    δ⁻¹({−1, +1})           **no, hole at 0**  840 cells, **E = 750**

 and the spin rule holds at four cap settings — 1,654, 2,664, 44,153 and 60,164 cells, E = 0 at each.
 **The parity rule is the fourth instance of §12.11.2's second excluded form**, and the first for
 which the criterion names the repair that would work: any reparametrisation moving the hole to an
 endpoint.

 **It is a quotient, not an extension.** Adjoining the electromagnetic coordinates to Λ₉ as new axes
 gives **E = 3,900** against E(Λ₉) = 0 — Theorem 10.1 in the direction that matters, since every one
 of them is a function of coordinates Λ already carries. **A derived coordinate cannot improve
 closure either.**

 **And it is not composability.** §12.11.0's transit condition 2S′ ≤ g admits 1,169 cells; the
 electromagnetic condition and the composability condition share **0.0004 bits of a possible 0.633**.
 The first is about state succession — whether a target is a legal source. The second is about
 whether a photon connects them. **They are near-independent predicates on the same cells, and the
 book has been calling the first one a transition.** Registers 442–444.
""","INSERT §12.11.6  the electromagnetic index")

def reg():
    after("441. **The falsifier for the declined law was named and run.**",
"""
 442. **The electromagnetic index was inside Λ and was never finished.** Every selection-rule
 quantity is a function of Λ's own coordinates — Δℓ from (ℓ, f), ΔS from (2S, 2S′) — and |ΔJ| is
 available at no level of the tower, because Λ carries no source J. The multipole is fixed by Δℓ and
 parity alone.

 443. **Λ imposes no electromagnetic constraint.** Its image on (multipole, ΔS) is the complete
 rectangle at every cap tested, so E = 0 there is register 333's vacuous zero. **576 Λ₉ cells are E1
 transitions with ΔS ≠ 0** — intercombination lines, forbidden in LS coupling and admitted here. The
 spin rule can be imposed and closure survives at four cap settings; the parity rule cannot, at
 E = 750, and §17.3's criterion says why: a hole at zero.

 444. **Composability is not the transition condition.** 2S′ ≤ g and the electromagnetic condition
 share 0.0004 bits of a possible 0.633 on Λ₉'s cells. §12.11.0 established Λ₉ as the first level at
 which a transition has a defined endpoint; that is **state succession**, and whether a photon
 connects the two configurations is a different function of the same coordinates. Both are true and
 the book has used one word for them.

 445. **A section heading had lost its markup and its number since the chapter was written.**
 §18.2 read ` 13.2 ν is inadmissible as an axis` — no `###`, and chapter 13's number inside chapter
 18. Being no heading, every heading-based audit skipped it, and it surfaced only when a new
 cross-reference to §18.2 failed to resolve. **Audit 6 caught it at one remove: not the defect, but a
 reference to what the defect concealed.**
""","INSERT §26.7  registers 442-445")

with State("emwrite") as st:
    for f in (sec, reg): step(st, f.__name__, f, budget=30)
open(P,"w",encoding="utf-8").write(s)
print(f"  {len(N)} edits"); [print("   ",x) for x in N]
