# READ-ch13l.md — Phase R2 section read: Chapter 15, main L4270–L4331

Chat 83. The unit is the `##` chapter, as the chat-81 ruling's operative reading allows for a short
chapter. Chapter 15 is 62 lines: §15.1 (L4272), §15.2 (L4277), §15.3 (L4293), §15.4 (L4308), §15.5
(L4325). Chapter 16 opens at L4332. Two instrument batches: **r2-ch13l** (computable, golden
`1b04f0e6`) and **r2-ch13m** (prose, golden `d15b0e3f`).

HANDOFF-35's range is confirmed: the chapter opens at L4270. It also prints DEFERRED.md at 36,073 B;
the member measures **36,063 B**, 108 lines. The bundle md5 gated, so the member is authentic to
BUILD110 and the handoff figure is a transcription slip.

## The claim census

**Computable (batched into r2-ch13l).** C1 the alphabet map Âᵢ is a projection and always succeeds
(L4273–4275); C2 a closed index equals the set its own envelopes admit (L4283); C3 Λ₈ has 56 envelope
functions (L4290); C4 ℛ(Λ) = Λ exactly (L4290) and for any closed index relative to a given order
(L4329); C5 the may-precede lemma and its dimension-freedom (L4298–4300); C6 the d = 2 converse and
the exactness of the criterion (L4302); C7 the verification figures 120 sets and 274 of 274 (L4302);
C8 the constraint graph is a tree and each axis is constrained only by its parent (L4309, L4326); C9
order recovery 20 of 20 at two cap settings on 216 and 976 cells with all eight axes permuted
(L4312–4313); C10 cost Σᵢ|Aᵢ|! and never ∏ᵢ|Aᵢ|! (L4315); C11 the two failed methods, 0 of 12 and
42 % / 25 % (L4317); C12 the figure's monotone bound q ≤ k (L4321).

**Prose (batched into r2-ch13m).** P1 §2.23 cited at L4280 as a requirement rather than a preference;
P2 §18.4 cited at L4305 for the failure of the converse above d = 2; P3 Chapter 30 cited at L4327 for
what is known when the graph has cycles; P4 the S1 / S2 / S3 labels and their order of presentation;
P5 the attribution of the Lemma and of the d = 2 criterion; P6 the restatement of the same
verification at main L9981; P7 the three "20 of 20" sites; P8 Figure 15.1's placement, registry and
caption; P9 census rows 1083 and 1084; P10 how the other volumes restate the chapter.

---

## A. Deviations

**13l-01 — the d = 2 criterion is false as worded, and true under the reading the text does not
give. Load-bearing; the same wording is in Appendix A.** L4302 prints: *"the criterion is exact: X is
closed under some order iff "may precede" is a total order, and that order **is** the relabelling."*
A.8 at L9969–9970 prints the same statement. Measured exhaustively, on every subset of a 3 × 3 and a
4 × 3 grid with at least two values on A₀:

| reading of "a total order" | 3 × 3, 490 sets | 4 × 3, 4,067 sets |
|---|---|---|
| strict (antisymmetric + transitive), as printed | says yes 198, **mismatches 124** | says yes 816, **mismatches 1,297** |
| total preorder (ties allowed, transitive) | says yes 322, **mismatches 0** | says yes 2,113, **mismatches 0** |

Brute force over every relabelling gives 322 and 2,113 closed sets. The smallest counterexample to
the printed reading is X = {(0,0), (1,0)}: closed under either order on A₀, but *u* and *v* may
precede each other, so the relation is not antisymmetric and the printed criterion returns *not
closed*. Under the preorder reading the criterion is **exact on both populations**, so the claim's
substance is true and only its statement fails. Two consequences: "a total order" must weaken to a
total preorder, and "that order **is** the relabelling" must weaken to *any linear extension of it is
a relabelling*, since with ties the relabelling is not unique. Ties are not an edge case in this
book — see 13l-02.

**13l-02 — "may precede" is not antisymmetric on three of Λ₈'s eight axes.** Measured on all 976
cells: the relation holds in both directions on axes **n**, **e** and **2S**, and is antisymmetric on
ℓ, k, q, f, g. The lemma itself is unaffected — all 29 pairs u < v at Λ₈ and all 35 at Λ₉ satisfy it
(B1) — but the criterion of L4302, applied to the book's own central object, does not pin the order
on three axes. §15.3 says only that above d = 2 the condition is "necessary and not sufficient"; the
stronger and measured fact is that the relation is not a total order there in the first place.

**13l-03 — Appendix A sends A.7 to a section that does not contain it.** The Appendix A index at
L9951 prints `A.7  "may precede" is necessary   §16.3, in full`. §16.3 is L4359–4378, *"D1 — D_phys
catches a wrong value in the data"*, and contains **zero** occurrences of "may precede". The
necessity proof is at **§15.3 L4296–L4300**, which contains three. The other eight rows of that index
resolve correctly (A.1 → §7.3, A.2 → §14.1, A.4 → §16.1, A.5 → §16.5, A.6 → §24.2, A.14 and A.16 →
§12.11.2, A.17 → §12.11.3). The 13d-01 / 13h-01 / 13i-04 / 13j-08 class: a pointer resolving to a
heading and not to the claim.

**13l-04 — Chapter 15 attributes nothing.** In 62 lines the chapter prints A.7 (the Lemma, L4298) and
A.8 (the d = 2 criterion, L4302), and cites **Appendix A zero times, A.7 zero times, A.8 zero times,
and no Register entry at all**. A.8's proof of sufficiency is written out in Appendix A at
L9974–L9979 and is not referenced here; A.8's own necessity half says *"This is A.7, specialised"*.
Against R-ATTR (all attributions that can be made must be made). Register 1597, 1633 and 1913 carry
Chapter 15's subject matter and none is cited.

**13l-05 — §18.4 does not contain the claim §15.3 sends the reader to it for.** L4304–4306: *"Being a
total order on every axis separately is necessary and not sufficient — the axes' requirements can be
mutually incompatible. That is developed in §18.4."* Measured over §18.4 and §18.4.1 together:
occurrences of "may precede" **0**, "total order" **0**, "order on" **0**, "recover" **0**. §18.4's
statement is *"Closure is not implied by every proper projection being a fixed point of ℛ"* — the
same mechanism one level up, about closure and projections rather than about orders and axes. The
analogy is real; the development §15.3 promises is not there. Note the reciprocal is sound in the
other direction: A.7's remark at L9965 cites §18.4 for the converse failing, which is what §18.4
exhibits.

**13l-06 — the same verification is stated twice in two wordings, and the adjective moves.** L4302:
*"Verified on 120 sets; 274 of 274 **constructed** total orders give closed sets."* L9981: *"Verified
on 120 **constructed** sets; 274 of 274 **recovered** total orders yield closed sets."* At L9981 the
274 orders were produced by the criterion and then tested; at L4302 they were constructed, which
describes a different experiment. One of the two states what was done. Neither is re-measurable as
printed — the population behind "120 sets" is not stated — but the exhaustive measurement in 13l-01
supersedes both as evidence: 322 of 322 and 2,113 of 2,113 under the correct reading.

**13l-07 — the figure registry's line column is stale for every row.** FIGURE_ASSETS.md and
FIGURE_MAP.md give Figure 15.1 at line 4290; it is placed at **L4319**. Measured across the whole
registry: **32 of 32 rows** carry a line number that is not the figure's placement line, offsets
running from −11 (Figure 6.1) to +29 (Figure 15.1). Both are process members and neither is
reader-facing, so this is a production defect and not a volume defect — but R3 must not use that
column to place anything.

**13l-08 — the caption describes rather than states.** L4321–4323 carries *"the structure is
invisible"* alongside the factual Left / Centre / Right description. Against the standing image-caption
rule (captions state facts only; no pictorial or descriptive language). The rest of the caption —
the monotone bound, the permutation, the propagation order, "uses no external information" — is
factual and measured true (B7).

**13l-09 — two rates printed with no denominator.** L4317: *"Alternating refinement across all eight
axes at once: **0 of 12.** Greedy propagation without backtracking: 42 % and 25 %."* The first is a
count out of a stated 12; the second and third are bare percentages. If the denominator is the same
12, then 42 % is 5/12 = 41.67 % rounded and 25 % is 3/12 exactly — MEASURED as arithmetic, INFERRED
as the reconstruction. Neither method is specified anywhere in the section, so neither rate is
re-measurable from the text: the 13j-07 class (a figure that rests on an unstated heuristic).

## B. Verified

**B1 — the lemma of L4298–4300 holds, and is dimension-free as claimed.** All 29 pairs u < v at Λ₈
and all 35 at Λ₉ satisfy may-precede; 58 and 70 ordered pairs tested. Zero failures of meet or join
membership.

**B2 — "56 functions" is exact.** Λ₈ has d = 8, so d(d−1) = 56 envelope functions φ̂ᵢⱼ. (Λ₉ gives 72,
Λ₁₀ gives 90 — neither is printed here.)

**B3 — ℛ(X) = X exactly, and stable under a second application.** Measured with the ambient-box
sweep: Λ₈ 976 cells in a box of 6,912, ℛ recovers 976, **E = 0**; Λ₉ 1,654 in 27,648, E = 0; Λ₁₀
2,535 in 110,592, E = 0; the 216-cell index, E = 0. ℛ(ℛ(X)) = ℛ(X) in every case. This confirms
L4290, L4329 and L1786's *"E(Λ) = 0 … exact in one step and stable under a second application"*.

**B4 — all four cap settings of L1786 rebuild.** 976 at (3,3,1,3,1), 1,636 at (3,3,1,4,1), 2,394 at
(4,3,1,4,1), each unique in the search space; 216 at 32 distinct settings.

**B5 — the constraint graph is a tree.** The seven Heaviside constraints give edges n–ℓ, ℓ–k, k–q,
k–2S, q–g, g–f, f–e: 8 nodes, 7 edges, connected, acyclic, **zero non-tree constraints**. Rooted at
n every axis has exactly one parent (ℓ←n, k←ℓ, q←k, 2S←k, g←q, f←g, e←f), so L4309's *"each axis is
constrained only by its parent"* and L4326's *"its constraint graph is a tree"* are both exact.

**B6 — 20 of 20 reproduces at both cap settings, and the propagation is sound.** Twenty seeded
trials at each of 216 and 976 cells, all eight axes independently permuted: an order was found in
**20 of 20** at both, and a found order closed globally in **20 of 20** at both. Critically,
**0 candidate orders passed every parent–child local test and then failed global closure** — which is
the question DEFERRED since chat 74 ("§15.4 read as the propagation the tree makes sound"). On this
index the local test does not admit a wrong order. **This closes that deferred item affirmatively**,
with the scope named: measured on Λ₈ and on the 216-cell index, not proved in general — and §18.4's
warning that closure is not locally determined is exactly why the global check was run.

**B7 — the cost claim, and the figure's bound.** Alphabet sizes at Λ₈ are (3,2,3,4,3,2,4,4):
Σ|Aᵢ|! = **94**, ∏|Aᵢ|! = **11,943,936**. The recovery search visited 75 nodes at 976 cells and 73 at
216 cells — below the sum, five orders of magnitude below the product. L4315 holds. Separately,
q ≤ k on all 976 cells, with q attaining k on 461 of them, so Figure 15.1's *"the monotone bound
q ≤ k"* is exact.

**B8 — the two live pointers resolve to their claims.** §2.23 (L1148) carries the reciprocal
explicitly at L1150–1152, citing §15.2 for envelope recoverability. Chapter 30 (L8316) states at
L8322–8323 exactly what §15.5 reports of it: recovery works for Λ because the graph is a tree, and
for a graph with cycles the question is open.

## C. Incidental

- **C1.** The chapter presents S1, then **S3**, then S2. The order is deliberate (S3 is the corollary,
  S2 is "the hard one") and the labels are used consistently at the seven other S-label sites
  (L8921, L9032, L9034, L9036), where S1 = alphabet, S2 = order, S3 = bounds. Not a defect.
- **C2.** "20 of 20" appears at three main-volume sites naming **two** populations: L1910 and L4312
  are this chapter's twenty recovery trials; L10886 is Audits 2 and 3 over all 475,800 pairs. Same
  tally, different experiments, in one volume.
- **C3.** The 216-cell figure is reachable at **32** cap settings and the text names none of them.
  Only **4** of the 32 give all eight axes an alphabet of more than one value, which is what
  L4312–4313's *"all eight axes independently permuted"* requires; the richest is (2,2,1,2,1) with
  alphabets (2,2,2,3,2,2,3,3), and that is the setting measured in B6. At the smallest setting,
  (1,4,0,2,2), the n and ℓ alphabets are singletons and permuting them is vacuous.
- **C4.** Eight lines of the chapter are 4-space indented blocks that render as code: L4273, L4278,
  L4283 (display mathematics, defensible) and L4298–L4300, L4312–L4313 (a prose Lemma with proof, and
  a prose result). The Lemma renders in monospace. Production class.
- **C5.** The Mathematical Compendium cites the chapter twice (L352, L634), both *"Proved — M §15.2
  … ; Moore 1910"*, attributing the corollary to prior art the chapter itself does not name. The
  Physics Compendium, the Index of Indices and the Spectra Compendium cite Chapter 15 not at all.
- **C6.** Register 1913 records that Chapter 15 was destroyed for two hours by a slice bounded at the
  wrong heading and recovered by Audit 6 — the provenance of this chapter's text.

## Census closures

Rows 1083 and 1084 are the only DEFECT-CENSUS rows in range; both are C9-OVERGENERALISATION-WORD and
both are disposed in CENSUS-CLOSURES-ch13l.tsv.
