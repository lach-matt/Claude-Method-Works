
---

# PART IV — THE RECORD

---

# 18. Withdrawals

**Forty-eight claims made in the course of this work were wrong.** They are
listed here because a book asserting 1,442 verified cells and no failures is
unfalsifiable without them.

## 18.1 The dominant pattern

> **Prose asserting a conclusion while the output contradicting it sits on the
> same screen.**

This accounts for the majority. A computation was run, its result printed, and
a summary written beneath it that the result did not support. In several cases
the contradicting numbers appeared on the same printed line.

**That pattern is the reason the mechanisms of Chapter 9 matter.** An index
that only holds what its method consumes cannot catch it. One that holds
redundant quantities can, and did.

## 18.2 The five that earned their place

**The wrong nuclear charge.** Al II and K II computed at *Z*_eff = 1 when both
have doubly charged cores. **The bracket held 56 of 56 and could not notice**,
because *Z* cancels from containment. δ came out at 4.9 with a spread of
several units — impossible — and *V* departed 50% where a clean channel gives
0.2%. **Two derived quantities, neither needed by the method, both correct.**

**The wrong limit.** A neon-like sodium spectrum read as neutral neon.
*T* = *I* − *E* went negative and **every channel was refused at entry.**
Totality did not detect the error; it prevented the computation.

**"*w* = 3ν·*e*."** Relation (b) of Chapter 9 written down incorrectly, with
540.0 and 1215.0 printed side by side. **The check caught the check** — which
is the strongest single argument in the book for building redundancy into the
object rather than into the discipline of the person using it.

**The silent discard.** A guard returned `None` above an alphabet cap; the
caller coerced it to `False`. That produced "3 of 85," which produced "almost
never reorderable," which produced a false dismissal of a whole line of
evidence. **One discard, three conclusions, none of which looked wrong** —
because the arithmetic stayed consistent. **𝒟 ≥ 1 cannot catch this.** Only
totality can, and totality had not yet been stated.

**The retrieval failure.** Chapter 12 argues that an index should enumerate
its targets and navigate before searching. Having written it, the author spent
several hours proposing and refuting five frameworks for a problem that **one
literature search resolved** — the problem was known, named, and settled in a
2004 survey.

## 18.3 Others worth listing

- Claimed a species integrated that had never been written to the source; found by auditing the built document rather than the draft.
- Fitted a curve through non-monotone data and extrapolated it to zero.
- Stated the ℓ-ordering law from a hand-typed subset rather than from the files; the real figure was 10 of 16, not 10 of 10.
- Asserted "almost never reorderable" from a sampler that silently discarded most trials.
- Ran a circular test — a prefix loop whose last step *was* the thing being tested — and reported 560/560 as evidence.
- Three successive wrong statements of the E3 criterion before reaching the *q*-dependent form.
- Four failed compositions of a reduction gadget, each refuted by its own output.
- Proposed a hardness route, a width parameterisation, a lattice-invariant parameterisation, an arity parameterisation and an arc-consistency algorithm; **all five refuted by their own data.**

## 18.4 What the register is for

Two things.

**It makes the rest checkable.** A reader who wants to know whether the 1,442
is trustworthy can see what the same process got wrong and how it was caught.

**And it is the evidence for Chapter 9.** The three defence mechanisms are not
proposed on theoretical grounds. **Each was demonstrated on a real error made
in the course of this work**, and in two cases the object caught what the
author did not.

---

# 19. Novelty, and its limits

## 19.1 On priority for *V* = 4ν/3

We have not established that this ratio is new, and we state the limits of
the search rather than the strength of the claim.

*V* = 4ν/3 is **two lines of algebra** from *T* = *Z*²*R*/ν², in a field
worked continuously since 1885. The prior expectation that nobody wrote it
down should be **low**.

**Ritz (1908) does not contain it.** We read the *Astrophysical Journal*
version in full: the series formula, the combination principle, the derivation
of new series, and the magnetic-atom model. **No error bound of any kind.**

**But it contains the qualitative ancestor.** Ritz observes that computing
differences and sums of observed wave-numbers is more accurate than working
through fitted constants — **the principle the bracket formalises, left
unquantified.**

**Martin (1980) does not contain it.** Its deliverable is a set of formulas
predicting one-electron levels to a stated ±0.03 cm⁻¹ — **flat, not
ν-dependent.**

## 19.2 The four documents we could not reach

Named so that a reader with library access can settle it:

| document | why it matters |
|---|---|
| **Edlén, *Handbuch der Physik* XXVII (1964)**, on series formulas | Edlén wrote the standard account; an elementary ratio would plausibly appear as an unremarked aside. In English despite the German series title. |
| **Ritz, *Physikalische Zeitschrift* **9**, 521 (1908)** | Two pages longer than the ApJ version, carrying the "further particulars" Ritz promises in a footnote. Reprinted in *Œuvres* (1911), ~pp. 142–150. |
| **Paschen & Götze, *Seriengesetze der Linienspektren* (Springer, 1922)** | Book-length treatment by the two people who measured most of the underlying spectra. |
| **Dunz, *Seriengesetze der Linienspektra* (Leipzig, 1911)** | Earliest complete compilation, chronologically closest to Ritz. |

**ρ ≤ 2 for each; every route closed.** By the analysis of Chapter 12, that is
a property of pre-digital print, not of the search.

## 19.3 The assessment

> **We put the probability that *V* = 4ν/3 is novel at approximately 75%**,
> with the residual concentrated in four named documents rather than spread
> across a century.

**One argument supports the higher end.** The quantity has **no use in a
fitting paradigm**. One computes bracket-width-over-interpolation-error only
if one is constructing brackets, and the literature is uniformly predictive.
That is a reason for absence rather than a failure to find.

**One cuts the other way.** It could have been written down and forgotten, in
a book nobody cites, by an author who saw no use for it. **That is precisely
what the four documents are.**

## 19.4 The other claims

| claim | assessed | basis |
|---|---|---|
| *V* = 4ν/3 | ~75% | nine searches, Ritz read in full, four documents open |
| ν_V ceiling | ~75% | very specific form, not found |
| cost surface, pole at *p* = 1 | ~50% | the framing is new; the content elementary |
| bracketing rather than predicting | ~85% | literature uniformly predictive |
| **E(X) as closure defect** | **not claimed** | see below |
| **reorderability complexity** | **not claimed** | see below |

**E(X) is deliberately not claimed as novel.** Closure operators, Galois
connections and formal concept analysis are established mathematics. **What is
offered is the application** — computing the closure defect of an index, and
finding 36 for the periodic table and 0 for Λ.

**And the reorderability material claims nothing.** The problem is known:
Stahl & Wille proved 2-dimension NP-complete in 1984; Yannakakis proved
dimension ≤ 3 NP-complete in 1982; Habib, Nourine, Raynaud & Thierry surveyed
the computational aspects in *Theoretical Computer Science* **312** (2004),
401–431. **The work reported in Chapter 20 was done before that literature was
located**, and is retained only for what it records about method.

## 19.5 Why state it this way

**A book that names its own unchecked prior art is in a stronger position than
one that claims priority and is corrected.** The four documents are a finite,
specified task. Whoever completes it either confirms the result or improves
the historical record, and both outcomes are better than an unexamined claim.

---

# 20. What remains open

## 20.1 The one open item in the collection

**The four German documents of §19.2.** ρ ≈ 1, library access only. They bound
the novelty assessment and nothing else — no result in this book depends on
their contents.

**Everything else in Part I and Part III is closed.** The census is complete
at 23 core types; the four decline modes each have a worked case; the parked
questions of earlier drafts — C₆ density, antiprotonic helium, the
isoelectronic law — are resolved in Chapters 15 and 17.

## 20.2 Order recovery above the tree

Chapter 8 recovers Λ's coordinate order because its constraint graph is a
tree. **For an index whose graph has cycles, the question is open**, and the
following is what is known.

**Complete but unproved.** Fixing one *pair* of axes jointly and extending
with backtracking found a valid ordering in **139 of 139** cases where one
exists. No proof; no counterexample.

**Not backtrack-free.** Measured depths 0, 2, 2, 7, 3 at *d* = 3 through 7.
Typical cost is polynomial — permutations ∝ *d*^2.6, closure checks ∝ *d*^1.1
— but **nothing here bounds the worst case.**

**And the worst case cannot be bounded by a local test**, because of §11.4:
closure is not determined by its proper projections.

## 20.3 What governs the difficulty

Ten structural invariants were tested against backtracking — dimension,
alphabet size, cell count, occupancy, join-irreducibles, poset height, poset
width, covers, antichain, rank range. **The best correlation was 0.31.**

**Solution density governs it**, at −0.68 in log:

| solution fraction | backtrack-free | mean backtracks |
|---|---|---|
| 0.009 – 0.25 | **24%** | 2.9 |
| 0.25 – 0.50 | 47% | 1.0 |
| 0.50 – 1.00 | 82% | 0.2 |
| 1.00 | **100%** | **0.0** |

> **The search is hard exactly when the solution is nearly unique.**

That is the signature of a **search** problem rather than a structural one,
which is why every structural parameter failed. **It is also, almost
certainly, the standard constraint-satisfaction phase transition**, and is
reported as a rediscovery.

## 20.4 The literature, and a caution

The problem family is settled and NP-complete throughout: 2-dimension (Stahl &
Wille 1984), dimension ≤ 3 (Yannakakis 1982), weak Boolean-lattice embedding.
**Habib et al. (2004) is the accessible account.**

**Whether reorderability reduces to any of them is the specific open
question.** The betweenness route is closed — by exhaustion over the complete
candidate pool, monotone bands cannot express an unconstrained element — but
other reductions exist for adjacent problems.

**The caution is procedural and belongs in the record.** This chapter's
material was produced before the literature was located, by a method the book
itself recommends against. **Chapter 12 was written first.**

## 20.5 The state of the whole

| | |
|---|---|
| collection | **closed** — 1,442 cells, 23 core types, 4 decline modes |
| the law | **closed** — nine mechanisms, six from closure, three constructed |
| the negatives | **closed** — five limitations, each with a counterexample or proof |
| novelty | **stated at ~75%**, four documents named |
| order recovery beyond trees | **open**, and known to be hard |

---

# Appendix A — Proofs

**A.1 Closure of Λ** — §2.3.
**A.2 Closure ⟺ 𝓡(X) = X** — §7.1, with the witness construction.
**A.3 Projections of closed sets are closed** — lift, join, project; the join
is componentwise and projection drops coordinates.
**A.4 𝒟 ≥ dim *q* − dim *p*** — rank–nullity on the Jacobian.
**A.5 χ_Λ is total** — a finite conjunction of decidable comparisons.
**A.6 Adjunction never repairs closure** — §10.2.
**A.7 "May precede" is necessary** — §8.3, dimension-free.
**A.8 The total-order criterion at *d* = 2** — necessity and sufficiency.
**A.9 μ_Λ in closed form** — via Birkhoff, §4.3.
**A.10 The tree factorisation of the void count** — §5.4.
**A.11 ν is inadmissible as an axis** — §11.2.
**A.12 The bracket is limit-free** — §13.2.
**A.13 The failure condition and its inversion** — §16.2, §16.4.

# Appendix B — The seventeen principles

Ten admit exact statement. **Three were corrected by the act of formalising
them**, which is recorded.

| | principle | expression |
|---|---|---|
| 1 | self-referencing | 𝓡(Λ) = Λ |
| 2 | self-defending | 𝒟 = dim *q* − rank ∂Φ/∂*p* ≥ 1 |
| 3 | work backwards | invert Φ; separate the fibre |
| 7 | all questions close | ∃N : Ω_N = ∅ — **terminal, not monotone** |
| 8 | every answer is a bound | A_n ⊆ A_{n−1}, a filtration |
| 9 | dimension 1 and its perspectives | **rank(log q) = 1** |
| 10 | allow expansions | §9.4-form constraints preserve closure |
| 12 | test every cell | ρ = 0 certain ⟺ n = \|Λ\| |
| 13 | coherence | COHERENT ⟺ Ω = ∅ |
| 17 | the path is through the bounds | cost ratio 1/N per bound followed |

**Seven remain procedural** — audit, compute before assuming, reframe, close
gaps, structural solutions, fetching, bounds as coordinates. They govern how
an agent uses an index, not what an index is. **They have no expressions, and
saying so is better than manufacturing one.**

**Principle 7 was corrected by its own formalisation.** The open-item count
across this work ran 5 → 4 → 3 → 4 → 3 → 7 → 3 → 3. **Not monotone.** Closure
requires a well-founded measure, not a shrinking count — which is why the
principle correctly forbids *claiming* coherence while Ω ≠ ∅ rather than
asserting that Ω always shrinks.

# Appendix C — Data and provenance

Every cell traces to a named compilation, table and page, or to the NIST
Atomic Spectra Database with its stated uncertainty.

**Primary sources:** Sansonetti 2008 (*JPCRD* **37**, 1659 and **37**, 7) ·
Kramida & Martin 1997 (*JPCRD* **26**, 1185) · Kaufman & Martin 1991 (*JPCRD*
**20**, 775 and **20**, 83) · Sugar & Corliss 1985 (*JPCRD* **14** Suppl. 2) ·
Sugar & Musgrove 1990 (*JPCRD* **19**, 527) and 1995 (*JPCRD* **24**, 1803) ·
Martin & Zalubas 1983 (*JPCRD* **12**, 323) · NIST ASD.

**Exotic systems:** Hori *et al.*, *Nature* **475**, 484 (2011) and *PRL*
**96**, 243401 (2006), both accessed through CODATA 2010 Table XII
(arXiv:1203.5425) and arXiv:1304.4330 · Korobov, *Phys. Rev. A* **77**, 042506
(2008) · Singer, Stanojevic, Weidemüller & Côté, *J. Phys. B* **38**, S295
(2005).

**All computations are reproducible.** Data files, scripts, and the figures
they generate are listed with the results they support.

---

# Index

*This index satisfies the law of this book.*

**Construction.** Terms are ordered by specificity: *s* ⊑ *t* when *s* is a
specialisation of *t*. The index is **closed** iff

> ***s* ⊑ *t* ⇒ loc(*s*) ⊆ loc(*t*)**

— every location of a specialisation is also a location of its
generalisation. That is a down-set condition in §9.4 form, so a closed index
is a sublattice of (terms × locations).

**Consequences.** The term list is recoverable as the set of first
coordinates (S1); the specificity order is recoverable by tree propagation,
since a term hierarchy is a tree (S2); loc(·) is recoverable as the union over
specialisations (S3); and every (term, location) pair is either present or
absent — no "see also" limbo, no partial entries (D3).

**E(index) = 0**, verified.

**An index with E > 0 requires the reader to already know where to look —
which is the periodic table's failure, at the scale of a back-matter page.**

*index, self-referencing* …………………………………………… *this page*