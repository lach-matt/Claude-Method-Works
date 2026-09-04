#!/usr/bin/env python3
"""close3.py -- write in what the cycle reduced.

Every edit is an anchored insertion or a one-token replacement. Anchors verified
unique in the body. Backup taken before this ran.
"""
import re, sys
from zeno import State, step

P = "The Method 1.4.md"
s = open(P, encoding="utf-8").read()
N = []

def after(anchor, text, name):
    """insert after the paragraph the anchor opens"""
    global s
    assert s.count(anchor) == 1, f"{name}: {s.count(anchor)}"
    i = s.index(anchor); j = s.index("\n\n", i)
    s = s[:j] + "\n\n" + text.strip("\n") + s[j:]; N.append(name)

def swap(old, new, name):
    global s
    assert s.count(old) == 1, f"{name}: {s.count(old)}"
    s = s.replace(old, new); N.append(name)

# ---------------------------------------------- O15, O9, O10, O11, O12 : §1
def principles():
    after("**Three of these were corrected by the act of formalising them.**",
"""
 **And the twenty-three sort into three kinds, not two, which is what settles what each one owes.**
 The taxonomy above sorts by *whether an expression exists*, which is a property of the writing.
 Sorted by what a principle **is**:

  kind          what it is                        what settles it
  MECHANISM     a fact about an index             a proof or a computation
  OPERATION     a thing an agent does             the failure it prevents
  RELATION      how a mechanism constrains an     neither — it carries content and takes no expression
                operation

 **Seven are operations** — P3, P4, P5, P6, P11, P14, P15 — and §5's table is their evidence. Six of
 the seven have a recorded failure behind them; **P16 is the exception and it is instructive**, having
 three constructive realisations at §17.4, §12.11.0.2 and §18.4.2 and no register entry, **because it
 never failed. It was adopted rather than learned**, and §5's table is extended accordingly.

 **Two are relations** — P7 and P17 — and each carried an expression that could not be evaluated,
 which is why. An expression is a mechanism's form and a relation is not a mechanism. Both keep their
 content and lose their expressions, exactly as §1 already says is better than manufacturing one.

 **And four mechanisms were stated without something they need.**

 **P2 needs its hypothesis, and the hypothesis has a name.** ⅅ ≥ dim q − rank ∂Φ/∂p ≥ dim q − dim p,
 so **ⅅ ≥ 1 exactly when dim q > dim p** — when the index derives strictly more quantities than it
 assigns parameters. That is **surplus**, which §11.1.1 measures at 7.07 bits per cell and Chapter 16
 states in prose as *it found it because it carried more than it needed*. For Λ the bound is tight:
 dim p = 4, dim q = 6, rank 4, ⅅ = 2. **Without surplus there is no check**, which is Edlén's
 footnote 78.

 **P7's well-founded measure, which this book demanded and never supplied, is already computed in
 Appendix E.** The measure is not the count of open items — §1 shows why — but the **multiset of
 their `blocks` values** under the ordering *nothing < a novelty assessment < one stated claim < a
 result the book relies on*. That coordinate is ordered and bounded below, so it is well-founded, and
 the multiset extension of a well-founded order is well-founded. Checked against §27.2.1's own
 movement, where six items' stake fell to nothing: the count went 13 → 10 and the multiset decreased
 in the Dershowitz–Manna sense. **That is precisely what *the set grew and the scope descended*
 means.**

 **P17's 1/N is derivable and the constant was dropped.** §10.3 decides whether a box lies inside Λ
 in **seven comparisons**, against one membership test per cell for enumeration. So following the
 bounds costs **c/N with c the number of constraints**, c = 7 here — 7/976 on Λ, 7/199,130 on Λ₁₃.
 **And N is nowhere defined**: neither §18.4 nor Chapter 12 introduces it, so the symbol is
 ungrounded in the sense §16.6's ⅅ_gro names. The corrected form carries no N: *following the bounds
 costs one comparison per constraint where searching the volume costs one per cell.*

 **P22 claimed what §16.8.2 refutes.** *No lie can exist within it* is false: rebuilt around a
 fabrication the index closes, has E = 0, is a fixed point of ℛ and satisfies every law here.
 Restated: **in a complete index every rule is content rather than inference, so a false cell is
 contradicted in the open by a stated rule where an inferred rule would have absorbed it. A forger's
 remaining move is to alter a rule, and an altered rule is equally visible. A complete index
 therefore converts deception into disagreement — error survives, concealment does not.** The index
 cannot be lied **to**; it can be **replaced**, and replacement is an act performed on it rather than
 a question put to it. Registers 417–420.
""", "INSERT §1  the three kinds, and P2, P7, P17, P22 corrected")

# ------------------------------------------------------- O16, O14 : §5
def five():
    swap("  §7.4 dilution                         excluding a viable species                   Ar II, Bi I",
         "  §2.4 dilution                         excluding a viable species                   Ar II, Bi I",
         "SWAP §5  §7.4 -> §2.4, dilution's pre-renumber address")
    after("**The protocols are not advice. They are the failure modes of this work, inverted.**",
"""
 **And the table stopped where the protocols stopped being about spectroscopy.** Eight are uncited by
 it — §2.4 above, and §2.16 through §2.22, every one written after this section was. They are added
 here, and one of them needs a second column.

  protocol                               what it prevents                             instance
  §2.16 the grid                        hunting where a layout would show             §28.3, 22 formulations
  §2.17 triangulation                   three measurements read as three facts        the step law, 1, 2, 4
  §2.18 computable or decided           a decision checked as though computable        reg. 277
  §2.19 what a safe repair requires     a repair riskier than its defect              reg. 286, 287
  §2.20 the prime directive             a computation lost whole to a timeout          reg. 343
  §2.21 a withdrawn figure's data       a number deleted rather than replaced          reg. 374
  §2.22 a corroborable entry            a defect that cannot be traced to its proof    reg. 415

 **And the second column is P16's, which no failure corroborates.** P16 — treat bounds and limits as
 coordinate values — has three realisations and no register entry, because **it was never learned
 from a failure; it was adopted and then built with**: §17.4 replaces (g₁, g₂) by (g₁, G) and
 conservation holds by construction; §12.11.0.2 carries (g, G) and recovers prior occupancy as a
 derived quantity; §18.4.2 indexes the partial sums of a mass vector and reaches treewidth 1 at every
 n. **An operation may be corroborated by a construction as well as by a failure**, and P16 is the
 only one in this book that is. Register 421.
""", "INSERT §5  eight uncited protocols, and corroboration by construction")

# ------------------------------------------------------------- O18 : §3
def audits():
    after("### 3.9 The audits are run on every output",
"""
 **And three of the twenty-one have never fired, which §4.6 says is not the same as passing.** A check
 must be demonstrated capable of returning a failure before its passing is evidence, and ANTECEDENT,
 ARITHMETIC and REPRODUCTION have caught nothing in this book — no register entry names any of them.
 Each has a constructible failing input and none needs new theory:

  audit          the input that must make it fail
  ANTECEDENT     a label used in Chapter 1 and defined in Chapter 30 — a forward reference the
                 source-against-itself read must flag
  ARITHMETIC     a product stated beside its own printed factors and wrong: *33 × 5 = 166* against
                 §12.6.1's table, which prints 33, 5 and 165
  REPRODUCTION   an altered Condon–Shortley term entry, against the microstate enumeration that
                 reproduces ten tables of ten exactly

 **Running these three is not optional bookkeeping.** §3.6 records two sections surviving their own
 supersession and passing five audits; §3.4 records the whitespace audit's first two measurements
 being wrong. **An audit that has never returned a failure is indistinguishable from one that
 cannot**, and this book has three. Register 422.
""", "INSERT §3.9  three audits never shown capable of failing")

# ------------------------------------------------------------- O4 : §14.4
def fourteen():
    swap("**Nine mechanisms.** Six follow from closure without further hypothesis. Two require something constructed — a tree, and disjoint derivations.",
         "**Nine mechanisms.** Six follow from closure without further hypothesis. **Three** require "
         "something closure does not supply — a tree for S2, a second derivation for D2, and for D1 "
         "a measurement from outside the index. The count read *two* until the mechanisms were "
         "scrutinised one at a time: D1 was counted among the six, and §16.7.3 forbids it — the only "
         "thing distinguishing a real map from a perfect map of an imaginary city is going there.",
         "SWAP §14.4  two require something constructed -> three")

# --------------------------------------------------- O19 : §26.7.8 grouping
def grouping():
    after("362. **§26.7.8, titled",
"""
 271. **§4.4 — a fix that left the mechanism unchanged.** The instance the mechanism list lacked: a
 defect repaired in one place while its class stood, recorded as an instance fix and not as a repair.

 179, 187, 240, 387. **§4.5 — a null recorded without its definition.** A hierarchy called convergent
 from a column that was flat; a map called small before its image was measured at 39% and 49.5%; a
 flag closed before the recomputation that closed it; a density read at one cap and reported as a
 property. **Four instances, one act: recording what was not found before defining what was looked
 for.** §26.7.8 grouped five of the seven mechanisms and left these two ungrouped, which is the
 heading defect of register 287 at the level of a mechanism list. Register 423.
""", "INSERT §26.7.8  §4.4 and §4.5 grouped")

# ------------------------------------------- the K.clock correction
def clock():
    swap("**430 against 430**",
         "**350 against 350 pure, with 80 cells in both**",
         "SWAP §12.11.0.1  the tick's two sources, de-double-counted")

# --------------------------------------------------- O24, O25, O26 : Ch 30
def ebook():
    after("### 30.1.1 What a referee would flag",
"""
 **First, the index of §30.1 is computed here, which it never was.** Harvesting every claim-bearing
 paragraph outside the register — §30.6's own test for what a claim is — gives 354 claims carrying a
 § citation and **138 distinct (location, support) cells**.

  resolution                          cells   box   density   E(book)
  chapter                               138   900     15.3%       578
  chapter, restricted to §30.1's own      80   465     17.2%       228
  **part**                               **25**  **25**  **100.0%**    **0**

 **And by §18.4.1 in its certificate form that number measures the drawing.** Coarsening to parts is
 an admitted operation and it reaches a fixed point of ℛ exactly — twenty-five cells filling a box of
 twenty-five. **A certificate exists, so E(book) at chapter resolution records how the chapters
 happen to cite one another, not a defect of the work.** This book is in the periodic table's
 category and not the measured nuclide chart's, and this is the first time its own law has been
 turned on it.

 **Second, §30.6's Condition 1 is named for a quantity it does not evaluate.** It is titled
 *E(book) > 0* and its test extracts headings, cross-references, section references and figures and
 checks that each target exists. **That is reference integrity.** It found a real defect — the
 missing Chapter 28 — and it has never computed E over the index §30.1 defines. The two are separated
 here: Condition 1 is a reference-integrity test, and E(book) is the figure above.

 **Third, §30.1's own constraint is violated fifty-eight times.** It states a claim in section s is
 supported by evidence at or before s. **Fifty-eight of 138 cells — 42% — cite forward**: the preface
 pointing at Chapter 23, Chapter 1 pointing at Chapter 28. Those are correct prose. **The constraint
 was written for an index and applied to a book**, and either it drops the ordering clause or this
 book carries fifty-eight admitted violations of a rule it states about itself. It is recorded rather
 than repaired, because deciding which is a decision in §2.18's sense. Registers 424–426.
""", "INSERT §30.1  E(book) computed, Condition 1 separated, the constraint tested")

# ------------------------------------------------------------- the register
def register():
    after("416. **The register is an index and it closes at E = 6.**",
"""
 417. **P2 was stated without its hypothesis.** ⅅ ≥ 1 requires dim q > dim p, which closure does not
 supply. The hypothesis is **surplus** and this book measures it at 7.07 bits per cell without ever
 attaching it to the principle. Edlén's footnote 78 is the boundary case.

 418. **P7's well-founded measure was demanded by this book and never supplied — and it was already
 computed.** It is the multiset of Appendix E's `blocks` values under Dershowitz–Manna, not the item
 count. Verified against §27.2.1: count 13 → 10 while the multiset strictly decreased.

 419. **P17's expression contains an ungrounded symbol.** *Following a bound costs 1/N* — and neither
 §18.4 nor Chapter 12 defines N. The derivable form is c/N from §10.3's seven comparisons, and the
 corrected statement carries no N at all. ⅅ_gro's class, in Part I.

 420. **P22 claimed what §16.8.2 refutes.** *No lie can exist within it* is false of an index rebuilt
 around a fabrication, which closes at E = 0 and satisfies every law here. Restated as visibility of
 rules: deception becomes disagreement, error survives, concealment does not.

 421. **P16 is corroborated by construction and by no failure**, having three realisations and no
 register entry, because it was adopted rather than learned. §5's table gains a second column.

 422. **Three audits have never fired.** ANTECEDENT, ARITHMETIC and REPRODUCTION name no register
 entry between them, and §4.6 says a check must be shown capable of failing before its passing is
 evidence. A constructible failing input is now printed for each.

 423. **Two of seven assistant failure modes were never grouped.** §4.4 has one instance and §4.5 has
 four, and §26.7.8 collected five mechanisms and left these two. Register 287's heading defect, at
 the level of a mechanism list.

 424. **E(book) is computed for the first time: 578 at chapter resolution, 0 at part resolution.**
 A certificate exists, so by §18.4.1 the figure measures the drawing rather than the work.

 425. **§30.6's Condition 1 is named E(book) > 0 and tests reference integrity.** It found the missing
 Chapter 28 and has never evaluated E. Separated here.

 426. **§30.1's constraint is violated by 42% of this book's own cells.** *Support at or before the
 claim* is an index's rule applied to prose, and fifty-eight claims cite forward. Recorded, not
 repaired: which of the two gives is a decision.

 427. **The two sources of the tick were double-counted.** §12.11.0.1 reports 430 against 430; the
 split table it prints gives (0,1) 270, (1,0) 270, (0,2) 80, (2,0) 80, (1,1) 80 — **350 pure on each
 side with 80 cells belonging to both.** The conclusion is stronger under the corrected count, since
 350 against 350 shares nothing. Register 393's mechanism, committed rather than caught.
""", "INSERT §26.7  registers 417-427")

with State("close3") as st:
    for f in (principles, five, audits, fourteen, grouping, clock, ebook, register):
        step(st, f.__name__, f, budget=30)

open(P, "w", encoding="utf-8").write(s)
print(f"  {len(N)} edits written")
for x in N: print(f"    {x}")
