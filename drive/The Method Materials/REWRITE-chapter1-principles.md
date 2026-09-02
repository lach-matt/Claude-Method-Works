# Rewrite (light touch) — Chapter 1, "The principles"

**Treatment (Option 1, as agreed).** The three reference tables of the twenty-three principles are kept intact — an expert returns to them as a list, and prose cannot replace that. What is added is a short plain-language gloss beside each formal expression, so a reader meets no bare symbol without a sentence to hold, plus a softening of the densest commentary. No principle, expression, number, or §-reference is changed. Every gloss is grounded in the record.

A note on how the glosses are shown: each table is reproduced as it stands, and a **reading** line is added under each group that walks its expressions in plain terms. This keeps the compact table for reference and gives the newcomer the key beside it, without breaking the table apart.

---

## 1. The principles

The method rests on twenty-three principles. They are gathered here as a reference — stated formally where a formal statement exists, and grouped by what each one is. A reader meeting them for the first time should not need to decode the expressions alone; a plain reading follows each group.

### Formalised — ten

| | principle | expression | where |
|---|---|---|---|
| **P1** | a complete index is self-referencing | ℛ(Λ) = Λ | §16.1, Ch. 8 |
| **P2** | a complete index is self-defending | ⅅ = dim q − rank ∂Φ/∂p ≥ 1 | Ch. 9 |
| **P3** | when the path is not found, work backwards from the desired output to an established input | invert Φ; if the fibre is non-trivial, find the datum that separates it | §23.1.3 |
| **P7** | all questions must close | ∃N : Ω_N = ∅ — terminal, not monotone | §25.6 |
| **P8** | any true answer, good or bad, is a bound | A_n ⊆ A_{n−1}, a decreasing filtration | §28.6 |
| **P9** | if the first dimension is a single all-encompassing definition, every other dimension is a perspective of it | rank(log q) = 1 | §24.2 |
| **P10** | allow continued expansions | §16.4-form constraints preserve closure | Ch. 10 |
| **P12** | every test must be run against every cell | ρ = 0 certain ⟺ n = \|Λ\| | B.2 |
| **P13** | coherence cannot be claimed while any caveat, gap or contradiction stands | COHERENT ⟺ Ω = ∅ | §25.6 |
| **P17** | the path is always through the bounds | following a bound costs 1/N of searching the volume | §18.4, Ch. 12 |

**Reading the expressions.** P1: the index equals its own reconstruction — rebuilt from its cells, it returns itself (this is the closure identity of the Preface). P2: it carries a defence — it derives strictly more quantities than it assigns parameters (dim q > dim p), and that surplus is what lets a second route check the first. P3: when there is no forward path to an answer, invert the map from output back to input, and where several inputs give the same output, find the datum that tells them apart. P7: there is a stage N at which the set of open questions Ω is empty — and it must actually reach empty, not merely shrink. P8: each answer narrows the admissible set, so the sets nest one inside the last — even a negative answer is a bound. P9: take logs of the derived quantities and they have rank one — every dimension is a multiple of the single defining one. P10: a new constraint of the §16.4 shape keeps the index closed, so the object can keep growing without breaking. P12: the certainty that nothing was missed is reached only when every cell has been tested — when the number tested equals the whole of Λ. P13: coherent exactly when no open question remains. P17: following the index's bounds to locate a cell costs a small fixed fraction of what searching the whole volume costs.

**Three of these were corrected by the act of formalising them.** P7 was first stated as though the count of open items always decreases; it does not — across this work it ran 5 → 4 → 3 → 4 → 3 → 7 → 3 → 3. Closure needs a **well-founded measure** — a quantity that cannot descend forever — rather than a shrinking count, which is why the principle correctly forbids *claiming* coherence rather than asserting that gaps always close.

**And the twenty-three sort into three kinds, not two — which is what settles what each one owes.** The table above sorts by whether an expression exists, which is a property of the writing. Sorted by what a principle *is*:

| kind | what it is | what settles it |
|---|---|---|
| MECHANISM | a fact about an index | a proof or a computation |
| OPERATION | a thing an agent does | the failure it prevents |
| RELATION | how a mechanism constrains an operation | neither — it carries content and takes no expression |

**Seven are operations** — P3, P4, P5, P6, P11, P14, P15 — and §5's table is their evidence. Six of the seven have a recorded failure behind them. **P16 is the exception, and it is instructive**: it has three constructive realisations (§17.4, §12.11.0.2, §18.4.2) and no register entry, because it never failed. It was adopted rather than learned, and §5's table is extended to say so.

**P9 has a second instance, which this book produced without recognising it.** Its only computed case was rank(log q) = 1 over fifteen Rydberg observables — and that is a tautology once §26.1's assembly rule makes every observable a power of ν, so it measures the rule and not the principle. **The second case is E itself.** E measures whether an index can carry a constraint, and it is read three ways: **forward** as a diagnosis (which of two modes produced the defect, and whether it is repairable); **backward** as a prohibition (that a minimal failing support of three admits no repair by any operation on coordinates); and **as an outcome** (§16.7.1's test of whether E is removable). The three were obtained separately and their identity had to be computed, so unlike the Rydberg case it is not a tautology. One definition, three dimensions, each a perspective of it — which is what P9 says. Register 429.

**Two are relations** — P7 and P17 — and each carried an expression that could not be evaluated, which is the tell. An expression is a mechanism's form, and a relation is not a mechanism; both keep their content and lose their expressions, exactly as this chapter says is better than manufacturing one.

**And four mechanisms were stated without something they need.**

**P2 needs its hypothesis, and the hypothesis has a name.** From ⅅ ≥ dim q − rank ∂Φ/∂p ≥ dim q − dim p, it follows that **ⅅ ≥ 1 exactly when dim q > dim p** — when the index derives strictly more quantities than it assigns parameters. That surplus is measured at 7.07 bits per cell (§11.1.1), and Chapter 16 states it in prose as *it found it because it carried more than it needed*. For Λ the bound is tight: dim p = 4, dim q = 6, rank 4, ⅅ = 2. **Without surplus there is no check** — which is Edlén's footnote 78.

**P7's well-founded measure, which this book demanded and never supplied, is already computed in Appendix E.** The measure is not the count of open items — this chapter shows why — but the multiset of their `blocks` values under the ordering *nothing < a novelty assessment < one stated claim < a result the book relies on*. That coordinate is ordered and bounded below, so it is well-founded, and the multiset extension of a well-founded order is again well-founded. Checked against §29.2.1's own movement, where six items' stake fell to nothing: the count went 13 → 10 while the multiset decreased in the Dershowitz–Manna sense. That is precisely what *the set grew and the scope descended* means.

**P17's 1/N is derivable, and the constant was dropped.** §10.3 decides whether a box lies inside Λ in **seven comparisons**, against one membership test per cell for enumeration. So following the bounds costs **c/N with c the number of constraints**, c = 7 here — 7/976 on Λ, 7/199,130 on Λ₁₃. **And N is nowhere defined**: neither §18.4 nor Chapter 12 introduces it, so the symbol is ungrounded. The corrected form carries no N: *following the bounds costs one comparison per constraint, where searching the volume costs one per cell.*

**P22 claimed what §16.8.2 refutes.** *No lie can exist within it* is false: an index rebuilt around a fabrication still closes, has E = 0, is a fixed point of ℛ, and satisfies every law here. Restated correctly: **in a complete index every rule is content rather than inference, so a false cell is contradicted in the open by a stated rule, where an inferred rule would have quietly absorbed it. A forger's remaining move is to alter a rule, and an altered rule is equally visible. A complete index therefore converts deception into disagreement — error survives, concealment does not.** The index cannot be lied *to*; it can be *replaced*, and replacement is an act performed on it rather than a question put to it. Registers 417–420.

### Procedural — seven

| | principle |
|---|---|
| **P4** | always audit results |
| **P5** | always compute the result before assuming the result |
| **P6** | when a question is confusing, reframe the question |
| **P11** | close all gaps before continuing |
| **P14** | a structural problem suggests a structural solution |
| **P15** | for fetching: use the index to navigate; data can be retrieved in pieces |
| **P16** | treat bounds, constraints and limits as coordinate values |

**These have no expressions, and saying so is better than manufacturing one.** They govern how an agent uses an index, not what an index is. P15 is the exception in one respect: it has a *measure* — retrieval redundancy ρ, Chapter 19 — without being reducible to it.

### The reflexive principles

| | principle | expression |
|---|---|---|
| **P18** | if the index is complete, a work that comprehends it completely is itself an index, and is itself self-referencing and self-defending | Chapter 32 |
| **P19** | an index is complete only when there are no more questions left to answer about its contents | COMPLETE(X) ⟺ Q(X) = ∅ |
| **P20** | the language in which a question is posed bounds whether it can close, and at what cost | — |
| **P21** | any definition contained within the lattice, and thus its equations, must be true in every mathematical language and in their combinations | — |
| **P22** | because everything is defined in a complete index, the entirety of the index is visible, and no lie can exist within it | — |

#### P19, and why it is neither P7 nor P13

Three principles govern questions, and they are one principle in three moods. P19 was the missing one.

| | says | mood |
|---|---|---|
| **P7** | ∃N : Ω_N = ∅ | questions **can** close — possibility |
| **P13** | COHERENT ⟺ Ω = ∅ | coherence **may not** be claimed otherwise — prohibition |
| **P19** | COMPLETE ⟺ Q = ∅ | what their emptiness **buys** — definition |

**And P19 is strictly stronger than closure.**

      E(X) = 0 says no cell the structure admits is absent. Q(X) = ∅ says no question the
      contents admit is unanswered.

**Λ has had E = 0 since Chapter 7 and has never had Q = ∅.** Whether *V* depends on the order of the bracket, what the Aitken bias generalises to, whether a higher-order bracket exists — each was admitted by contents already present, and none was asked until late.

      Closure is about what an index holds. Completeness is about what it has been asked.

**And the condition is reachable, for the same reason P7's is.** P7 was corrected once: closure needs a well-founded measure rather than a shrinking count. **Q has grown at nearly every step of this work while its scope has fallen** — from *is V novel?* to *is there an optimal order?* The set grew and the scope descended, and that descent is what makes P19 a criterion rather than an impossibility.

**Q(X) = ∅ is reached not when nobody asks, but when every question the contents admit has an answer in the contents.**

#### P20 — the language bounds the question

Three closure mechanisms are used in this book, each in a different language, each with a different guarantee.

| language | mechanism | closure | cost |
|---|---|---|---|
| **monotone two-variable bounds** | tree factorisation | **always** | one pass |
| **polynomial relations** | Gröbner basis | **always**, by Hilbert | finite; doubly exponential worst case |
| linear arithmetic with quantifiers | quantifier elimination | yes | triply exponential |
| **full arithmetic** | — | **never** — Gödel | — |
| **documentary** | — | **no mechanism exists** | — |

**Measured on the objects of this book: tree factorisation 0.00018 s, Gröbner 0.010 s — a factor of 55 — and the documentary language has no timing because it has no algorithm.**

      The choice of language is made when the index is built, not when the question is asked.

§7.1 chose monotone two-variable bounds. That single decision determined that E(X) is computable, that the sum factorises, that a single expression exists, and that every question about Λ's contents would close. It equally determined what could not: §11.7's sum bound lies outside the language, and its repair — making the sum a coordinate — is a translation back into the closing language.

**P20 subsumes E3, the multi-target repair, and P19's reachability.** And it answers the novelty question structurally: novelty is posed in the documentary language, which has no closure mechanism. That is not a failure of searching — no amount of it would help.

#### P21 — every definition true in every language

Not merely expressible in each mathematical language. **True** in each, and in their combinations.

| definition | order | algebra | geometry | analysis | information | logic |
|---|---|---|---|---|---|---|
| \|Λ\| | 976 | 976 | 976 | 976 | 976 | 976 |
| rank(x) | 13 | 13 | 13 | 13 | 13 | 13 |
| mean rank | 11.0666 | 11.0666 | 11.0666 | 11.0666 | 11.0666 | 11.0666 |
| E(periodic table) | 36 | 36 | 36 | 36 | 36 | 36 |

And the combinations must name real objects, not analogies. Verified: gcd(N(a),N(b)) = N(a∧b) and lcm = N(a∨b) exactly; F′(1)/F(1) = mean rank; E_bits = log₂ C(\|ℛ\|, E) = 105.1 for the classroom table.

**P21 is an instrument, not only a criterion.** When a property holds in five languages and fails in the sixth, it is the sixth *expression* that is wrong — not the property. This has located two errors, and in both the structure was sound and the translation was not. First: E(X) was recorded as having no analytic route — "E is a count, calculus measures a continuum" — and its defence value set to 1. The route exists: E(X) = F_ℛ(1,…,1) − F_X(1,…,1). Second: deletion-repair was recorded as failing in geometry. The convex hull does fail — it permits arbitrary facets, so a vertex can be the sole witness of a facet and its deletion is unrecoverable — but Λ's facets are two-variable monotone bounds, and the closure matching that form (the intersection of all valid such bounds) restores every deletion: 30 deletions, 0 failures; 20 additions, 20 absorbed; fixed point exact at 976. **A mismatched operator is not a counter-example. It is a mistranslation.**

**What the law then establishes.** The self-feeding loop and its asymmetry hold in all five languages:

| language | closure operator | delete | add |
|---|---|---|---|
| order | ℛ | restored | absorbed |
| geometry | monotone polyhedron | restored | absorbed |
| algebra / logic | ideal, Gröbner basis | still derivable | T·h enters the ideal |
| analysis | coefficients of F | restored | absorbed |
| information | description length | E_bits stays 0 | grows |

      Extensive gives repair. Monotone gives absorption. Every language has a closure operator,
      so both hold everywhere.

And that is the formal reason Chapter 16 cannot rely on self-reference alone. A structure that closes will heal what you remove and swallow what you insert. Self-consistency defends against loss and never against invention — which is why the defence against a wrong *value* (ⅅ_phys) must reach outside the index, and why Chapter 21 records what the loop could not catch.

#### P22 — visibility, and why a complete index cannot be lied to

A lie requires concealment. A complete index has nowhere to conceal.

The distinction is between a rule that is **content** and a rule that is **inferred**, and it is decisive. Consider the cell

      y = (n=1, ℓ=0, k=1, q=0, e=1, f=0, g=0, 2S=2)

— one electron with spin multiplicity 2, which no atom has.

Where the rule is inferred, ℛ recovers the bound on 2S from the cells themselves — and so it simply revises that bound to admit the new cell:

| *k* | before | after |
|---|---|---|
| **1** | 2*S* ≤ **1** | 2*S* ≤ **2** |
| 2 | 2*S* ≤ 2 | 2*S* ≤ 2 |
| 3 | 2*S* ≤ 3 | 2*S* ≤ 3 |

      The index did not reject the cell. It revised its rule — and then admitted 74 further cells the
      old rule forbade. The result is closed under join and meet, has E = 0, satisfies every law in this
      book, and contains 75 physically impossible configurations.

Where the rule is **content**, the same cell is checked against a stated rule set — (bounded, parent, slope, intercept) held as cells of their own index — and returns

    VIOLATES 2S ≤ 1·k + 0 (2S = 2, bound = 1).

**Same cell. Same index. The only difference is whether the rule was present or inferred.**

**What the law does and does not claim.** It does not claim that a complete index knows what is true. It claims that nothing in it is hidden.
