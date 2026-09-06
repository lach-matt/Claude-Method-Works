#!/usr/bin/env python3
"""catchup2.py -- the session's remaining findings into the book."""
import re, sys
from zeno import State, step
P="The Method 1.4.md"; s=open(P,encoding="utf-8").read(); N=[]
def after(a,t,n):
    global s
    assert s.count(a)==1, f"{n}: {s.count(a)}"
    i=s.index(a); j=s.index("\n\n",i)
    s=s[:j]+"\n\n"+t.strip("\n")+s[j:]; N.append(n)

def directive():
    after("### 2.20 The prime directive",
"""
 **One exception, and it is the only one.** **Fetched literature is exempt.** A computation may be
 halved and rerun on half; an external source cannot, because halving what was read changes what was
 read. A source consulted at half length is a different source, and the register would carry a claim
 about a document nobody has seen. So a fetch runs to completion or is not made, and the budget is
 declared before it rather than enforced during it. Register 432.
""","INSERT §2.20  literature exempt from the directive")

def schemes():
    after("### 12.11.4 Precision is path-dependent; physics is not",
"""
 **And the same trade, measured across four schemes rather than two.** The tower as built uses jK. The
 other three standard schemes — LS, LK and jj — were rebuilt from their recoupling chains, and two
 reproduce their stated Λ₁₃ counts exactly from the chain alone: **jK 199,130 and LK 341,150.** LS and
 jj depend on a looseness convention that is named and not printed, and two committed readings of it
 **bracket** the stated figures rather than determining them: LS ∈ [383,065, 597,325] ∋ 431,050 and
 jj ∈ [160,380, 244,060] ∋ 206,520.

 **The chains are standard.** NIST states LK as *the core's orbital momentum coupled with the external
 electron's to give L, then L coupled with the spin of the core to obtain K*, and jK as
 ℓ₁+s₁ = j₁, j₁+ℓ₂ = K, K+s₂ = J. Cowan and Andrew, *JOSA* **55**, 502 (1965), treat exactly these
 four as the four types of pure coupling for two-electron configurations — a precedent for the set,
 not only for the members.

    **The exact J multiset is identical in all four schemes, in every configuration tested.**

 Verified across fifteen configurations by computing the multiset through the jK chain, the LS chain
 and the jj chain independently. A coupling scheme is a basis change; the atoms do not move. **So the
 four cell counts, spanning a factor of 2.17, price four ROUTES to one object.** §12.11.4's sentence
 one level down says it already — *the exact J-set is the same whether J is reached through K or
 directly, 12 of 12; the envelopes differ, 64.4% against 39.4%. The index remembers the route; the
 atom does not.* Register 433.
""","INSERT §12.11.4  four schemes, one object")

def density():
    after("### 12.11.1 The axes, and what each one sees",
"""
 **Two readings the definition requires and a loose reading drops.** The density column was rebuilt
 from the definition above, and four of six values fell out at once; two did not, and localising them
 gives two conditions that are not stated anywhere:

 **First, the sum runs over the STAGE BELOW.** For axis 12 that is Λ₁₁, so the cells are Λ₁₀'s
 weighted by their own 2S′ and v fibres — not Λ₈'s. The same quantity computes to 30.8% over Λ₈,
 31.1% over Λ₉ and **31.4% over Λ₁₀**, which is the stated value. The weighting is a third of a
 percentage point per stage and it converges on the answer exactly.

 **Second, each envelope is priced once.** Filtering axis 12's numerator on whether J_c is physically
 realised charges axis 11's price a second time — 12.7% against 30.8%, an eighteen-point gap that is
 entirely the double charge. §12.11.3's dichotomy says each coupling axis pays once, and the density
 column is where that has to be enforced rather than stated. Register 434.
""","INSERT §12.11.1  the two operative readings of the density definition")

def collection():
    after("### 22.9 A caveat the collection forced",
"""
 **And the caveat is sharper than it was written, on two counts, both established against the ASD
 itself rather than argued.**

 **First, the delimiters mean what NIST says they mean.** ASD marks provenance three ways: a plain
 value is observed; **`[ ]` is "interpolation, extrapolation, or other semi-empirical procedure" and
 explicitly includes "fitting the Ritz-type formulas along series of levels"**; `( )` is "determined
 from an ab-initio calculation". This section reads `[ ]` as covering ab initio and it does not.
 **He I, queried directly: every level in the table is bracketed** — 1s² through 1s16d without
 exception, and the ASD's own note says why. Excitation energies for n ≤ 10 were obtained by
 subtracting Drake's *theoretical* ionization energy from Kandula's experimental ground level; the
 higher levels were obtained **by fitting the extended Ritz quantum-defect expansion**. He I has no
 observed level values at all. **Its 189 cells — the largest single block of the 1,442 — are not
 independent tests by the criterion this section itself states.** H I, the other species read, is
 majority bracketed, every level from n = 13 to 40 among them.

 **Second, and larger: independence is a property of TRIPLES, not of cells.** The bracket is a
 relation on T(n−1), T(n), T(n+1). A cell is an independent test only if **all three** of its levels
 are independent, so one Ritz-fitted level poisons **three** tests rather than one.

  fraction of levels derived    cells surviving    TESTS surviving
  0.1                           0.90               **0.73**
  0.2                           0.80               **0.51**
  0.3                           0.70               **0.34**
  0.5                           0.50               **0.12**

 Computed on H I, which is 38% plain: **only 13 of 64 interior cells — 20% — are independent tests.**
 The nd series is the sharpest case, six of ten levels plain and **not one clean triple**, because the
 derived values alternate and every triple contains one. And the collection is worse than scattered,
 because the derived values are the high-n ones, which is where the channels run.

    **1,442 cells over ~190 channels, of which an unknown number of channels contain no
    independent test at all — He I's nine certainly, H I's nd series certainly — and the
    count of independent tests is bounded above by the count of CLEAN TRIPLES, not by
    the count of cells.**

 That is the honest form and it supersedes *an unknown proper subset*. The subset is knowable, the
 read is mechanical, and two species of thirty-five are done. Registers 436 and 437.
""","INSERT §22.9  the ASD read, and independence as a triadic property")

def interval():
    after("### 9.2 The occupancy measure",
"""
 **And this is one leg of something the book states three times without naming it once.**

    **Between any two points there is an interval, and the method returns its measure.**

 Not an equation connecting two points — the orders are partial and share 0.3%, so no single order
 relates an arbitrary pair. **An interval between two points is total**, because every pair of cells
 has a meet and a join whether or not either order relates them. That is why d(x,y) works where the
 order does not.

  between                        the interval              its measure
  two **cells**                  [x∧y, x∨y]                d = ∏(\\|Δᵢ\\|+1) = τ(lcm/gcd), five forms
  two **states** under           [min, max] output rank    17% of 264 inputs single-valued, worst
  composition                                              spread 12, range [3, 23]
  two **measurements**           [T(n−1), T(n+1)]          w, priced at V = 4ν/3

 §12.11.0.12 says the middle row in its own words — *from one coordinate up, a transition is not a
 function of its inputs; it is an interval* — and §20.1 gives the third. §25 already proves the three
 MEASURES are one quantity; what was missing is that the three OBJECTS are one shape.

 **And the form survives what an equation would not.** Theorem 11.2 permits it, because an interval
 carries *less* than the coordinates and not more. §18.6 permits it, because an interval bounds where
 something already is rather than proposing an unlisted cell — §23.6.3's own correction. And the 0.3%
 overlap stops being a defeater and becomes the content: **two intervals per pair, nearly disjoint, so
 what a thing IS and what it can BECOME are separately bounded and rarely both.**

 It is universal over indices whose constraints are pairwise monotone envelopes, per §14.3, and not
 over all mathematics. **And it is why this is a method rather than an equation**: an equation returns
 a value; this returns an interval and a verdict on what the interval is about, which by §18.4.1 is
 whether E measures the drawing or the world. That second half is not expressible as an equation.
 Register 438.
""","INSERT §9.2  the interval form")

def register():
    after("431. **Two of the six build-time readouts cannot run.**",
"""
 432. **§2.20 amended: fetched literature is exempt from the prime directive.** A computation may be
 halved; a source cannot, because halving what was read changes what was read, and the register would
 then carry a claim about a document nobody has seen.

 433. **Coupling schemes are basis changes and the counts price routes.** The exact J multiset is
 identical in jK, LS and jj across fifteen configurations. jK and LK reproduce their stated Λ₁₃ counts
 exactly from the standard chains; LS and jj are bracketed, because the looseness convention is named
 and not printed. **Two readings of it were tested and both refuted** — the value lies between them.
 The convention is needed only where a chain ends in a coupling of two free momenta rather than a
 spin-½ mutual bound, which is where it must be printed. Cowan and Andrew 1965 owed as a precedent
 for the four-scheme set.

 434. **The density column needs two conditions the definition implies and the text omits**: the sum
 runs over the stage below, not over Λ₈; and each envelope is priced once, so filtering axis 12 on
 J_c's realisability charges axis 11 twice. 12.7% against 31.4%, and the gap is entirely the double
 charge.

 435. ***densities.py* and *numbers-index.py* were absent and are rebuilt from the printed rules.**
 Five of six densities reproduce exactly and the sixth to a rounding; E(G) now recomputes at build
 rather than printing a failure notice. **All six build-time readouts run for the first time**, which
 §2.21 has required since the manifest was written.

 436. **He I has no observed level values in the ASD.** Every level is bracketed, and NIST's note says
 why: n ≤ 10 from Drake's theory anchored to Kandula's measured ground level, n ≥ 11 by fitting the
 extended Ritz quantum-defect expansion. §22.9 read `[ ]` as ab initio; NIST marks ab initio with
 `( )`. **The collection's largest block — 189 cells — contains no independent test.**

 437. **Independence is a property of triples, not of cells**, because the bracket relates
 T(n−1), T(n), T(n+1). One derived level poisons three tests. At a scattered derived fraction f the
 surviving tests go as (1−f)³, not (1−f). H I: 38% of levels plain, **13 of 64 interior cells
 independent**, and its nd series has six plain levels of ten and not one clean triple.

 438. **The three intervals are one shape.** [x∧y, x∨y] between cells, [min, max] output rank between
 states, [T(n−1), T(n+1)] between measurements — three objects the book computes separately, whose
 measures §25 already proves are one quantity. **Between any two points there is an interval, and the
 method returns its measure.** The form survives Thm 11.2 and §18.6 where an equation would not,
 because an interval carries less than the coordinates and bounds rather than proposes.
""","INSERT §26.7  registers 432-438")

with State("catchup2") as st:
    for f in (directive, schemes, density, collection, interval, register):
        step(st,f.__name__,f,budget=30)
open(P,"w",encoding="utf-8").write(s)
print(f"  {len(N)} edits"); [print("   ",x) for x in N]
