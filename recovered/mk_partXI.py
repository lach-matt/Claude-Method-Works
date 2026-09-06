# -*- coding: utf-8 -*-
import re, io
MAIN="The_Method_1_6-2.md"; IOI="The_Method_1_6___The_Index_of_Indices-2.md"
src=open("/mnt/project/Transitions-1.md",encoding="utf-8").read().split("\n")
order=[]
for l in src:
    m=re.match(r'^### (\d+\.\d+[a-z]?) (.+)$',l)
    if m: order.append(m.group(1))
assert len(order)==77, len(order)

# --- Appendix G's thirty, verbatim ---
mt=open(MAIN,encoding="utf-8").read().split("\n")
gi=[i for i,l in enumerate(mt) if l=="## Appendix G — Transitions, indexed"][-1]
G={}
for l in mt[gi:gi+80]:
    if l.startswith("|") and not l.startswith("|---") and not l.startswith("| § "):
        c=[x.strip() for x in l.strip().strip("|").split("|")]
        if len(c)>=2 and re.match(r'^\d+\.\d+[a-z]?$',c[0]): G[c[0]]=c[1]
assert len(G)==30, len(G)

U={
"0.1":"Five working protocols, the first of which is commit before looking: a position is written down before any retrieval, and the retrieval scores it.",
"0.2":"The Admission Law. An entry's grade bounds the operations it may enter; a derived entry carries the minimum grade of its inputs, and no derivation raises a grade.",
"0.3":"A biconditional licenses a merge only if it holds at every rung of the graded axis. Merging on a fact true at one point and then grading the axis is the error.",
"0.4":"Operator reliability, measured. Predictions aimed at logical structure scored 4/4 on three consecutive tests; predictions of how a field regards a claim scored 1/4, and that class was barred from entering.",
"1.1":"The definitions: the value sets, the monotone upper envelope φ̂ᵢⱼ of one coordinate against another, R(X) as every point of the observed box respecting all envelopes, and E(X) as its excess.",
"1.5":"X ⊆ BPC(X) ⊆ R(X), so E > 0 is in principle ambiguous between genuine inconsistency and envelope coarseness. Computed for every object in the paper, R = BPC exactly and the ambiguity does not arise.",
"2.3":"All six density values reproduce once three non-obvious exact sets are used — the spin set of f^g by microstate enumeration at axis 9, terms genuinely new at occupancy v at axis 10, and the J values of terms of ℓᵏ at axis 11.",
"2.5":"Four monotone variants of the ℓ-bound close and two non-monotone variants do not. The decisive pair, ℓ ≤ ⌊n/2⌋ and ℓ ≤ \\|n−3\\|, have identical cardinality at 32,535 cells and opposite outcomes: monotonicity is the discriminant, not cardinality.",
"2.6":"The Standard-Model Extension lifts the Coulomb accidental degeneracy but moves no quantum number, because ℓ ≤ n−1 follows from node counting. The lattice does not individuate universes by Lorentz structure.",
"2.7":"Transit admissibility is directional. Outward is unobstructed; inward is not, because a cell with occupancy beyond our Pauli bound fails the one-dimensional index before any question of joint structure arises.",
"2.8":"Three things locate a transition and the index certifies only the first. The lattice says what exists; the order says what is near, and only 24.2% of the 475,800 pairs of Λ₈ cells are ordered by componentwise domination; the measure says what it costs, and it is external.",
"3.1":"The eighteen-column table has E = 36, and re-indexing period as n + ℓ is not what repairs it — neither is contiguity. ℓ is fully determined by group: s at 1–2, d at 3–12, p at 13–18.",
"3.2":"Of the 36, twenty-five — 1d, 1p and 2d — could never hold an element, being forbidden by ℓ ≤ n−1: the footprint of a law the coordinate system has no axis for. The remaining eleven are 3d, deferred past 4s by the Madelung order, and period 1 group 2.",
"3.3":"The periodic table is not an analogy for the violation index; it is the other failure mode, and having both is what makes the distinction visible. Ordering failures are repairable because re-ordering acts on one relation at a time.",
"5.2":"Chronology violation requires the causal ladder, non-unitarity at the Lindblad rung and arbitrarily small ANEC violation — and not signalling, cloning, nonlinearity or loss of microcausality, each of which appears under Deutsch's prescription and not otherwise.",
"5.5":"The repair space is closed, and both directions fail for opposite reasons: adding fails because the box inflates, merging fails because the envelopes coarsen. Two lines cover all six repairs.",
"5.6":"Objects are thresholds. Of the 1,146 cells permitting a macroscopic wormhole, 1,116 pay with a preferred frame, 714 with non-unitarity and 756 with signalling — and none pays with nothing.",
"6.1":"Of the nine coordinates, five are fully conflated, two partially, and two are clean.",
"6.2":"Every conflation merges an inert rung with a potent one, and that is not coincidence: the index was graded from papers about what breaks, and the papers that matter for atomic structure are about what holds. Two different literatures.",
"6.3":"None of the five was findable from inside. All surfaced from a specific question about a named theorem; inspecting the coordinate list finds none of them.",
"6.4":"Audit 22. For every coordinate whose term appears in a cited theorem, state what the theorem means by it, state what the rung means, and record match, conflation or unchecked. Its output is a debt, not a pass.",
"7.2":"Recomputed under the documented nine-letter conventions the linearisation figure reproduces exactly at 7,734; the slide figure does not, and the earlier 8,856 is refuted outright, the operation acting on a three-coordinate object whose box is at most 40.",
"7.3":"The frontier formulas in closed form, d(c) and s(c), verified on 1,500 sampled cells with zero distance mismatches.",
"7.4":"The spin-statistics hypotheses have three letters and no proxies. 900 of 18,072 cells — 5.0% — have the Pauli lattice guaranteed, and we are among them; for the rest parastatistics becomes available and Λ₈ can be 1,600 rather than 976.",
"8.1":"A charge relation has three parts, not two: trigger, what incurs the charge; currency, what may pay; and jurisdiction, where the charger has standing to collect.",
"8.3":"Buniy's jurisdiction is necessary, and the counterexample is the ghost condensate of Creminelli, Luty, Nicolis and Senatore (2006). It escapes through higher-derivative structure, not Lorentz violation: the Lagrangian is manifestly Lorentz-invariant and the vacuum breaks the symmetry.",
"8.5":"Retained as history, not current analysis. Built on the seven-vocabulary partition that §8.4 derives away and §12.3 withdraws, and kept because §8.6's correction is only legible against what it corrects.",
"8.6":"An earlier draft placed the exclusion of macroscopic wormholes in a component the law index cannot reach, and made that the reason six repairs failed. Rebuilt on the four derived vocabularies, that is wrong: the system is connected and the severance was an artefact.",
"8.6b":"Graham–Olum is listed by the charger index as firing and should be conditional. A conjecture with a sufficiency proof is a third category the index does not have.",
"8.7":"Retained as history. No configuration is a connected tree; Hartman must drop V2 rather than V3, and reducing Wall backfires because its V1–V5 edge is coupling's only connection.",
"8.8":"Checked twice, including through an adjacent literature: the general ANEC-from-causality argument is flat-space, and curved-space results exist only with a V2 condition retained.",
"9.1":"Three measures, and the third did not exist. E measures what an index cannot carry; the vocabulary debt measures what it has not checked it carries correctly, 32 of 48; nothing measured what was never named at all, and seven law-classes appear in cited sources with no letter.",
"9.2":"The axis index itself — nine cells in a box of 5,184.",
"9.3":"Pair-completion. The nine leave four value-directions unoccupied, and every hand-found axis outside the box occupies a pair — never one direction, never three.",
"10.2":"§2.8 is corrected. A faithful measure exists and compresses 976 cells to eighteen values, because any strictly monotone function of the coordinates is automatically faithful.",
"10.3":"Λ audited. The conflation rates of Λ and the violation index are proportionally indistinguishable; the causes differ, V1 conflating because two literatures used one word.",
"10.4b":"The one open cell. Following §10.4's target down gives a single surface class and a single condition, and the target is a boundary point rather than a region; an isolated horizon has Θ = 0 exactly.",
"10.6":"The chain, primary-sourced, with a fifth caveat on T0: Reeh–Schlieder is a theorem in Minkowski space, proved from analyticity, the spectrum condition and the action of the Poincaré group, and in curved spacetime it is a property established for free massive fields.",
"10.7":"Five instances of one shape, the last stated as physics rather than bookkeeping: gauge redundancy is the bookkeeping needed to describe subsystems relationally in a gauge-invariant system.",
"12.1":"The promotion ledger. Everything promoted is about the method and everything held is either a general claim or a physical number — the instrument is better characterised than anything it measured.",
"12.2":"Twelve claims withdrawn with their causes, among them defect 60, an unbounded Helly number, projection-covariance as a scaling law, and the defect growing with jurisdiction count.",
"12.3":"The withdrawals post-dating the previous draft, several of which correct claims that draft asserts.",
"12.4":"The numeric debt. Of six claims carried with no dataset behind them, five clear on recomputation and one is corrected — refuted by a bound, the slide operation acting on a three-coordinate object whose defect cannot exceed 40.",
"12.5":"Audit 23 is the only external validation in the construction and it passes: ten published LS term tables reproduced exactly, zero microstate discrepancies against C(4ℓ+2, k).",
"12.6":"Thirty instances of one class — a conclusion drawn from a comparison that was not licensed. The arithmetic was correct in every case; the warrant was not.",
"13.1":"For a product with no linking constraint every cross-envelope is vacuous, so R(A × B) = R(A) × R(B). With E(Λ) = 0 the join of Λ with the violation index gives E = 976 × 30 = 29,280: the defect is extensive.",
}
missing=[s for s in order if s not in G and s not in U]
assert not missing, missing
assert len(U)==47, len(U)

rows=[]
for s in order:
    if s in G: rows.append(f"| {s} | {G[s]} | **rests on it** — Appendix G |")
    else:      rows.append(f"| {s} | {U[s]} | not used |")

body = """# XI · TRANSITIONS, THE COMPLETE TABLE

**Every section of the source, not only the ones the book leans on.** *Transitions* v3.0 is the
origin of the closure operator R, the excess E, and the two failure modes on which Part IV of this
compendium and Chapter 12 of the main volume both rest. Thirty of its sections are load-bearing
here, and the main volume's Appendix G sets those thirty out with the objects that stand on each.
This section is the other half of that address: **all seventy-seven sections, in order, with what
each states and whether this work rests on it.**

**Why the forty-seven are printed at all.** An index of indices that lists only what a work used
tells a reader nothing about what it declined. The forty-seven are the paper's own ordering
arguments, its withdrawals, its axis index and its open join — several of them corrections to
sections this book *does* use, and one of them, §10.2, a correction to §2.8 that reverses a claim
about the measure. A reader who wants to know whether a result of this book was picked from a
larger field or was the only thing on offer can only answer that from the complete list.

**The count.** Seventy-seven sections; thirty relied on, forty-seven not. The paper remains the
origin and is named as such throughout; this table and Appendix G are the address.

| § | what it states | in this work |
|---|---|---|
""" + "\n".join(rows) + """

**Reading the third column.** *Rests on it* means at least one object of this work — a lemma
label, a chapter, or a Register entry — cites that section; Appendix G names which. *Not used*
means no object cites it, and carries no judgement on the section: §12.5's external validation and
§13.1's extensivity result are both sound and both simply outside what this book claims.
"""
t=open(IOI,encoding="utf-8",newline="").read()
assert "# XI ·" not in t
assert t.count("Λ_V5 — the contested-row closure")==1
nt = t.rstrip("\n") + "\n\n---\n\n" + body
open(IOI,"w",encoding="utf-8",newline="").write(nt)
print("rows:",len(rows),"| used:",sum(1 for r in rows if 'rests on it' in r),"| unused:",sum(1 for r in rows if 'not used' in r))
print("IoI lines:",t.count(chr(10)),"->",nt.count(chr(10)))