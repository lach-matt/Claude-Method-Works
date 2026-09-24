# SOURCES.md — provenance map for 01-closure-law (not published)

Paper: `PAPER.md`, "The Closure Law of a Finite Index". Drafted 2026-09-21 on a `check.py` written in
an earlier, interrupted run; that check was read in full, run, and left as it was. **Repaired
2026-09-24 against `AUDIT.md`** (40 findings, every one dispositioned there). The check now discharges
**134 rows, 0 failures** (20 GUARD, 53 MACHINE-CHECKED, 47 EXHAUSTIVE, 6 REFUTATION, 8 CITED) in about
85 s, and `--selftest` adds three negative controls, all refuted by a decision procedure (137 rows).
Every number in the paper is either produced by that run or is a bibliographic figure in the reference
list. The repair added obligations and guards and weakened none.

## Novelty, as the paper now states it (AUDIT A-1 / R-C1)

The audit identified the c = 2 case of Theorem 15 with Theorem 2.1 of G. Czédli, *Generating Boolean
lattices by few elements and exchanging session keys* (arXiv:2303.10790; Novi Sad J. Math., DOI
10.30755/NSJOM.16637). **Verified on the arXiv full text (v3, 29 Oct 2023):** Theorem 2.1 reads "Bₙ has
an at most k-element generating set iff n ≤ Sp(k)", Sp(k) = C(k, ⌊k/2⌋); its "only if" half maps a
generating set into the free meet-semilattice and applies Sperner's theorem to an n-element antichain
in Bₖ, its "if" half takes the ⌊k/2⌋-subsets antichain — the two halves of the paper's proof at c = 2.
By the paper's own Theorem 2, seed(X) is the least generating size of the lattice X, so the
identification is exact.

The audit then asked whether Czédli's later generating-set papers cover c ≥ 3. **They do, in full.**
arXiv:2309.13783 (direct powers of free distributive lattices) and arXiv:2401.00842 (subspace lattices)
do not; but **arXiv:2308.15625** (Ural Math. J. 10(1), 2024), *Sperner theorems for unrelated copies of
some partially ordered sets in a powerset lattice and minimum generating sets of powers of distributive
lattices*, Theorem 2.4, makes k ↦ G_min(Dᵏ) the left adjoint of n ↦ S(J(D), n) for every finite
distributive lattice D, and its Observation 3.1(c)–(d) gives S(U, n) = C(n − p, ⌊(n − p)/2⌋) for a
bounded U with p the least size of a set whose subsets embed U — the Griggs–Stahl–Trotter theorem for a
chain. For the c-element chain J(D) is the (c−1)-element chain, p = c − 2, and G_min = c − 2 + m(d):
Theorem 15 for every c. **The paper therefore claims no part of Theorem 15.** It is headed "Czédli",
carries a CITED paragraph naming both papers and Griggs–Stahl–Trotter 1984, and keeps its own proof
(Theorem 13 + Bollobás) as a second proof in the paper's terms. What the paper claims in §9 is
Theorem 13 (seed = set cover, for this operator), Theorem 14 (the simplex L(d, c−1), which is not a
direct power and so not a case of Czédli's theorem — no prior statement of it was found; the
generating-set literature on Young's lattice was not searched beyond Czédli's papers, and R-C7's
"check" is discharged only to that extent), and the refutation of the source's linear law.

**A discrepancy with Czédli 2023b, recorded and not repaired.** Table (4.30) of arXiv:2308.15625
prints G_min(C₄ᵏ) = 18 for the five-element chain at k = 2022 and 2023. Theorem 2.4 there with
Observation 3.1(d) — p = 3 for the four-element chain of join-irreducibles, f*(2023) = 14 since
C(13,6) = 1,716 < 2,023 ≤ 3,432 = C(14,7) — gives 17, as Theorem 15 does. `check.py` prints both
figures on its row "the law at (c, d) = (5, 2023)", confirms the shift c − 2 rather than c − 1 by
direct closure at 5² (seed 5, no four cells generate), and the paper states the arithmetic in one
sentence after Theorem 15. Which reading of that table is intended is a question for its author.

**Bibliographic details not confirmed here.** The Novi Sad J. Math. volume and year of Czédli 2023a
(the DOI is the audit's); the reference gives the DOI and arXiv id only. The Jamison-Waldner 1982 and
van de Vel 1993 attributions for "Carathéodory number = breadth" (R-C3) are the audit's; the paper
cites them as the audit gave them, with Queyranne–Tardella 2017 (verified: Math. Oper. Res. 42(2),
495–516) for the sublattice convexities of product spaces.

All line ranges below are in `method/members/`. `M` is `The_Method_1_6-2.md`, `C` is
`The_Method_1_6___Mathematical_Compendium-2.md`.

## Where each section draws from

| paper section | source passages |
|---|---|
| Thesis, Abstract, §0 | M §14.1 3686–3722 (Theorem 14.1 "X is closed iff X = ℛ(X)"; the attribution to Bergman's double-projection theorem, to Baker & Pixley 1975 via the majority term, to Montanari 1974 and Dechter 1992 for global consistency — **the paper does not carry "global consistency" as the name of E = 0 nor the Dechter 1992 citation** (AUDIT R-C2): E = 0 is stated as binary decomposability into staircase constraints in Montanari's sense, with global consistency of the row-convex network following from van Beek & Dechter 1995, and the counterexample X = {(0,1),(1,0)} — a globally consistent network at E = 2 — is printed; the forward projection-determination theorem is attributed to Baker & Pixley, Bergman to the name and the converse, Veinott 1989 added (R-C4), and to Deville, Barette & Van Hentenryck 1999 for the staircase class; and the correction that **Freuder 1982 is a different theorem** — backtrack-free search at strong (w+1)-consistency — which this paper carries); M §14.3 3724–3735 (the scope: each coordinate presented as a chain, not each factor a chain; what fails is folding two chains into one coordinate); C §IV.A 334–346 ("E is coordinate-relative": any set of composite size relabels onto a full rectangle) |
| §1 D1–D5 | M §6.1 1537–1556 (Âᵢ(X), φ̂ᵢⱼ(v) = max{xᵢ : x ∈ X, xⱼ ≤ v}, ℛ(X) = {x ∈ ∏Âᵢ : xᵢ ≤ φ̂ᵢⱼ(xⱼ) ∀ i≠j}, E(X) = \|ℛ(X)\| − \|X\|); C §IV.A 168–178 ("the recovery operator"), 324–332 ("monotone upper envelope / staircase bound", with max ∅ = −∞) and 146–156 ("closure defect"); notation aligned to `research/warp-drive/paper/THE-HIERARCHY-LAW.md` §1 D1–D5 (observed alphabet, box, generated sublattice, boundary function, staircase) and to its two ambient regimes, own-box and fixed-box |
| §1 D6–D8 | M §14.1 (closed = fixed point); M §14.5.7 and C §IV.S 782–792, "A seed": "G ⊆ X is a seed of X under ℛ iff φ̂(G) = φ̂(X)" |
| §2 Proposition 1 | C §IV.A 236–244 ("the defect bounds: 0 ≤ E(X) ≤ \|box\| − \|X\|", proved, box = ∏\|Âᵢ(X)\|) |
| §2 worked defects | M §6 1516–1536 (periodic table: 90 main-table cells, 126 admitted, E = 36; the 36 named as period 1 groups 2–17 and periods 2–3 groups 3–12); M §6.1.1 1557–1598 (helium at group 18 gives 36, at group 2 gives 20, and the mechanism is φ̂(group \| period ≤ 1) = 18 against 2); M §6.2 1599–1610 (the table row "a box ordering, l ≥ w ≥ h — 56 — 0"); M §6.2 1682–1686 (the seven named) and §6.3 1710–1725 (the calendar's seven cells named, and the relabelling that drops E to 0) |
| §3 Lemmas 1–3, Theorem 1 | `THE-HIERARCHY-LAW.md` §2 Lemmas 1–3 and §3 Clause A (φ total and isotone; φ monotone in X; ℛ does not move its own boundary) — the proofs here are written independently but the lemma structure is that paper's; M §6.2 1605–1608, which cites the idempotence of ℛ and draws the consequence that a band closes as a theorem rather than a finding |
| §3 Lemma 5, Theorem 2 | `THE-HIERARCHY-LAW.md` §4 Clause B and its four-witness construction at d = 2, with the lift cited to Baker & Pixley 1975 and Queyranne–Tardella 2008 Thm 9(ii)/Thm 11; M §14.1 3688–3700 and C §IV.A 366–376 (the same attribution, and Bergman named) |
| §3 Theorem 3 | M §14.1 3686–3700 (Theorem 14.1); C §IV.A 366–376 |
| §4 Theorem 4, normal form | M D.4.2 10414–10424 ("Λ = {x : xᵢ ≤ minⱼ φᵢⱼ(xⱼ)}", "the pointwise minimum is the operator's entire content"); M D.4.4 10444–10456 (ℛ idempotent, one application takes any presentation to a canonical form); M D.4.4.1 10457–10466 (Λ → the defining bounds is NOT a function — the map runs one way) |
| §4 Theorem 5, the algebra | C 3592–3610 ("A.staircls": E(ℛ) = 0 iff the held set is an intersection of monotone staircases; a closed index is a system of inequalities; **L(s) = ⌊s/2⌋ and U(s) = s + ⌊s/3⌋**, "both exact on s ∈ {0,1,2,3}"); M §14.5.4 / C §IV.A 554–562 ("the one-corner characterisation") |
| §5 | M §14.5 3737–3762 (the Moore family, the three-ambient table 73/146/731 and the ∩ 100% / ∪ 64.4–68.3–32.6 columns, and the meet-irreducible counts 12, 14, 20); M §14.6 4081–4104 (the family theorem: every member has E = 0, ∩-closed, ∪-broken, E(Cl(U)) > 0 at 182/365/64,804); M §14.6.2 4125–4152 (**E(Cl(U)) = 2^\|U\| − \|Cl(U)\| exactly**, the six-ambient table, and the mechanism — Cl holds ∅ and U and separates every ordered pair, so every envelope is constant at 1; "12 of 12, 56 of 56, 72 of 72 separating pairs"); C §IV.F 824–866 |
| §6 | M Appendix A.3 9990–10000 (projections of closed sets are closed, with the proof this paper's §6 reproduces); M §18.4 4985–5002 (closure is not locally determined: the six-cell witness in d = 3, c = 2, and "roughly one in five") |
| §7 adjunction | M §17.2 4804–4818 (E2: "Λ × h is closed iff h is a lattice homomorphism", 100% over 424 tests; **Theorem 17.1, adjunction never repairs**, with its proof); M Appendix A.11 10049–10058 (ν = e − δ inadmissible: a difference is not a lattice homomorphism); M §18.2 4975–4980; M §17.3 4819–4845 (the interval property for δ = f − ℓ, with its proof — the Remark of §7) |
| §7 products | C §IV.A 472–492 ("the product rule for closure": if no constraint links the factors, ℛ(A×B) = ℛ(A)×ℛ(B); "the product rule for the defect": E(A×B) = \|A\|E_B + \|B\|E_A + E_A E_B) |
| §8 | M Appendix A.15 10088–10105 (B_k = {(a,b) : \|a−b\| ≤ k} is a sublattice; C = {(a,b,c) : \|a−b\| ≤ c} is join-closed and is **not** a sublattice; the meet-failure counts **12,654 at cap 8, 113,568 at cap 12, 565,284 at cap 16**; "a bound by a constant is monotone in both directions, a bound by a free coordinate is not"); M Appendix A.18 10107–10124 (the triangle region join-closed and meet-broken, with the two witnesses (0,1,1)∧(1,0,1)=(0,0,1) and (4,0,4)∧(2,2,0)=(2,0,0), and the reading that max moves each coordinate toward the slack side); M §18 4929–4935 (the triangle's two inequalities are one sum and one difference, so coupling enters at envelope precision) |
| §9 | C §IV.S 598–608 (the generation criterion: alphabet equality plus envelope equality, and the licence for the set-cover formulation); C §IV.S 660–670 (the envelope-step law: (i,j,t) a step when t is minimal at that envelope value, and covering all steps and slots suffices "because the running max is constant between steps"); C §IV.S 680–688 ("the seed is a set cover", Karp 1972, Johnson 1974); C §IV.S 690–698 (the down-set seed law d + c − 1, "exact: LB = UB at d=4 c=4"); C §IV.S 638–648 (the box seed law d + c − 2, "exact by branch and bound at 3³ and 4³"); C §IV.S 650–658 (the Carathéodory lower bound = breadth = d); M §14.5.9 3922–3980 (the set-cover reading, the exact figures by branch and bound, and the two laws) |
| Λ's own seed | M §14.5.1 3763–3800 and §14.5.9 3936–3946 (seed(Λ₈) = 7) — **mentioned in one sentence and not developed**, per the brief; nothing about it is checked here |

## Interpretations chosen, and why

1. **Own-box regime throughout.** The source computes ℛ inside ∏Âᵢ(X), the box X itself realises
   (M §6.1). The hierarchy paper names the alternative (fixed-box) and records that conflating the
   two caused an error. The paper states the regime explicitly in §1 and every result is in it.
   `check.py`'s reference implementation and its Z3 predicate `own` both build the box conjunct in,
   and a guard shows the witness form *without* that conjunct is a different operator (73
   disagreements of 2,851 cells) — so the regime is not a stylistic choice.

2. **The hull identity is stated as a theorem in its own right.** The source's Theorem 14.1 is
   "X closed ⟺ X = ℛ(X)" and the attribution to Bergman / Baker–Pixley is given beside it. The
   paper separates the two: Theorem 2 (ℛ(X) = ⟨X⟩) carries the cited step, and Theorem 3 is its
   corollary. This is done because it localises the import to one place, which §0 then names.

3. **Theorem 9 is a biconditional where the source has two one-way statements.** M §17.2 gives the
   E2 criterion ("Λ × h is closed iff h is a lattice homomorphism", measured at 424 tests) and
   Theorem 17.1 ("adjunction never repairs", proved in one direction). The paper proves the single
   biconditional that contains both, and Corollary 1 is Theorem 17.1. The source's 424-test figure
   is not reproduced and is not needed.

4. **Theorem 14 is proved here; the source states only the count.** For the simplex the
   source gives d + c − 1 with "LB = UB at d=4, c=4"; the paper proves it for all d ≥ 2, c ≥ 2 and
   additionally shows the minimum seed is unique and every one of its cells forced. The source calls
   D(d, c) a "down-set"; it is not one in the product order ((1,1) ∈ D(2,2), (0,1) ∉ D(2,2)), and the
   paper says "ordered simplex" and identifies it with L(d, c−1) (AUDIT A-3). For the full box see
   item 2 of the next section and the novelty section above.

5. **`seed` is defined for closed X only.** The source's definition (C §IV.S 782) assumes X closed
   and the paper follows it (D8). For open X the source's "seed + E" decomposition exists and is
   outside this paper.

6. **The Carathéodory number is stated for what it bounds.** See item 3 below.

## Reproduction — what reproduced, and what did not

**Reproduced exactly.** The periodic table at 90 cells, \|ℛ\| = 126, E = 36, with the 36 gaps
matching the two named blocks cell for cell; the same table with helium at group 2, E = 20; the
calendar at 365 cells, \|ℛ\| = 372, E = 7, with the seven cells identical to the source's list; the
ordered box at 56 cells, E = 0. The Moore-family table at every ambient the source reports — 73, 146
and 731 non-empty members; ∩ at 100%; ∪ at 64.4%, 68.3% and 32.6% without the empty set and 65.3%,
68.8% and 32.7% with it, both of which the source prints in different places; the meet-irreducible
counts 12, 14, 20. The six-ambient E(Cl(U)) table of M §14.6.2 — 13/3, 38/26, 74/182, 147/365,
506/3,590, 320/3,776 — and the identity E(Cl(U)) = 2^\|U\| − \|Cl(U)\| at all of them, plus
2⁴ at 732/64,804 from M §14.6. The separation property behind that identity (the source's "12 of 12,
56 of 56, 72 of 72" are the ordered pairs of cells at 4, 8 and 9 cells, and the check verifies
separation over every ordered pair at all seven ambients). The meet-failure counts of the region
\|a−b\| ≤ c: **12,654 / 113,568 / 565,284** at caps 8, 12, 16, with 0 join failures at each. Both
triangle meet witnesses. The nine-cell staircase L(s) = ⌊s/2⌋, U(s) = s + ⌊s/3⌋, E = 0, and the
fibre extremes read back off the cells. The down-set seed law d + c − 1 at nine instances, by exact
minimum cover and (where small enough) by direct closure as well.

**Not reproduced, and the paper prints the measured result instead.**

1. **M §18.4's "roughly one in five".** The source says that of the sets passing every
   proper-projection test, "roughly one in five" fails closure. Measured over the family the source's
   own witness lives in — every subset of a 2×2×2 box with at least two cells whose three two-fold
   projections are all closed — there are **117 such subsets and 52 of them are open, 44.4%**. (The
   one-fold projections impose nothing: every subset of a chain is closed.) The paper prints 117 and
   44.4% and names the family. The source gives no family for its figure, so this is a measurement
   against an unstated population rather than a contradiction; it is recorded rather than repaired,
   and the source's phrase is not printed.

2. **C §IV.S's box seed law d + c − 2 is false from d = 5.** The source states "a full box c^d seeds
   at d + c − 2", "exact by branch and bound at 3³ and 4³", and M §14.5.9 repeats it as one of "two
   laws [that] become exact rather than fitted". Both of the source's verifications are at d = 3,
   where the law is correct. It is correct at d = 2, 3 and 4 for every c and **fails at d = 5**:
   `{0,1}⁵` is generated by four cells, where d + c − 2 = 5. `check.py` refutes it by direct closure
   (no three cells generate 2⁵, four do) and as a `--selftest` negative control. The paper prints
   the exact law **seed(c^d) = c − 2 + m(d)** with m(d) = min{m : C(m, ⌊m/2⌋) ≥ d}, which is
   Theorem 15 — proved here from Bollobás's set-pair inequality above and an explicit antichain
   construction below, and confirmed by direct closure at eight boxes and by exact maximum-clique
   search at thirteen more points. **Theorem 15 is not new: it is Czédli's** (2023a at c = 2; 2023b
   with Griggs–Stahl–Trotter 1984 for every c) — see the novelty section above; the first draft
   called it "new to this paper" and that claim is withdrawn. The source has no law beyond the linear
   one. The disagreement is an over-generalisation from two data points, not a computational error in
   the source.

3. **C §IV.S's "seed ≥ the Carathéodory number = the breadth = d" does not hold as a lower bound on
   the seed.** The Carathéodory number of the subsemilattice convexity is the breadth, and the
   breadth of a product of d chains is d — both correct, and cited in the paper (Jamison-Waldner 1982;
   van de Vel 1993; Queyranne & Tardella 2017 — the first draft cited Queyranne & Tardella 2008, which
   is about hulls, representations and counting, not these numbers: AUDIT R-C3). But the
   Carathéodory number bounds how many generators reach **one point of the hull**, not how many
   reach the whole set, and the breadth in question is the breadth of the object generated, not of
   the ambient. The two-element chain {(0,0,0), (1,1,1)} is closed in d = 3 and seeds at 2.
   `check.py` files this as a REFUTATION with that witness. The paper states the Carathéodory number
   for what it does bound, gives the refutation, and proves the bound that survives —
   **Proposition 5, seed(X) ≥ maxᵢ \|Aᵢ(X)\|** — verified over all 219 closed subsets of a 3×3 and a
   2×2×2 box with 0 violations. On the witness that bound reads seed ≥ 2 and is tight.

4. **M §14.5.8 (3815–3921)'s earlier seed table is superseded inside the source itself and is still wrong at its
   first entry.** That section reports "full box 3^d: 4 · 6 · 8 · 10 · 12, law 2d" from prune-greedy
   removal; M §14.5.9 retracts every seed size that section reports, prune-greedy being a poor
   set-cover heuristic. The later passage governs. Even so, its replacement d + c − 2 gives 3 at
   3² where §14.5.8's table gives 4, and the exact value by direct closure is **3** — the three
   cells (0,2), (1,1), (2,0). Nothing from §14.5.8 is printed.

**Stated by the source and outside this paper's scope — read, not used, and not printed.**

- M §6.1.1's decomposition of the 36 into 25 forbidden by ℓ ≤ n−1 and 11 deferred by the Madelung
  order, and the Janet (left-step) table at 120 cells with E = 0 and the 32-column form at E = 106.
  These are readings of the periodic table's defect in terms of quantum numbers and layout
  conventions; `check.py` computes none of them and the paper prints none.
- M §6.2 (1599–1709)'s nuclide-chart defect (E = 9 at four proton cutoffs), the subnet (E = 8), the
  bibliography (E = 6, floor 2 under 5,184 relabellings), and the ionization-energy monotonicity
  measurement. All are further instances of the same operator; none is needed for the law.
- M §18.4.1 (5004–5100)'s law of realised closure and its certificate form, M §18.6's reading of E(X) as a
  prediction budget, and M §18.1's σ-algebra theorems. Read in full; they are consequences drawn
  about indexing practice rather than about ℛ, and they carry no obligation `check.py` discharges.
- M §14.5.1, §14.5.10 through §14.5.14 on Λ's own seed — seven cells for 976, the 24,585 exact
  minimum covers, the single forced cell, the alphabet law and the binary reading. The brief
  directs that Λ's seed be mentioned and not developed; §9 carries one sentence and no number.
- M §17.3 (4819–4880)'s convexity criterion for constraints on a difference, and its measurement that convex
  preimages are 8.2%, 10.3% and 0.8% of the closed subsets at the three ambients. The paper's §7
  Remark carries the interval property the criterion rests on and stops there.
- C §IV.A's ℛ₄ (the four-orientation closure) and the orientation cost; C §IV.A's binary path
  consistency BPC(X) with X ⊆ BPC(X) ⊆ ℛ(X). Both are about neighbouring operators.

## One correction carried from the source, and it is the source's own

M §14.1 records that this line of work had been citing **Freuder 1982** for the decomposability
result and that the citation is wrong: Freuder 1982 gives *backtrack-free search* on a graph of
width w under strong (w+1)-consistency. The decomposability certificate is **Dechter 1992**, with
**Montanari 1974** for the monotone case. The paper carries the corrected attribution in §0 and §3
and states plainly what Freuder's theorem is, so a reader meeting the claim elsewhere can tell the
two apart. C §IV.A's own "Freuder 1982" entry — "a tree-structured constraint network is globally
consistent after arc consistency" — is a third statement of that paper and is not what Freuder
proves either; M §14.1 is later and governs, and the paper follows M.

## Guards, and what they are worth

`check.py` runs twenty guards before it reports anything, and two of them are negative controls
that must fail. The operator under test is the one `tools/cypher.py` computes (`op_order`), imported
by path and never copied; a reference implementation of D1–D5 written fresh for this paper agrees
with it on 400 random instances over six box shapes, and the join-closure — a deliberately wrong
reference — disagrees on 24 of 50. The Z3 staircase predicate is evaluated concretely on 2,919 cells
of the declared boxes and agrees with the operator everywhere, while the same predicate without its
box conjunct disagrees on 73 of 2,851. The Z3 closure predicate (D6) is evaluated on 300 random sets
over five box shapes against a direct closure test, 0 disagreements (added for AUDIT A-5). The hull
encoding ("the intersection of all closed supersets") is brute-forced against the generated sublattice
on 60 instances. Fourteen non-vacuity checks cover five hypothesis shapes: four at three boxes each,
and Theorem 4's isotone-system hypothesis at 3×3 and 2×2×2 (added for A-5). §10 names exactly which
predicates are guarded and which are transcriptions. The sampled figures are the only SAMPLED numbers
anywhere in the work and none is a result; the paper says so in §10. Theorem 7's column E(Cl(U)) is
now computed directly at every ambient, including 65,536 cells at 2×2×2×2 (A-4); the earlier check
derived that entry from the constant-boundary mechanism. Negative control (3) of the selftest is
direct closure at 2⁵ (A-8), not a formula comparison.

## Figures

Five figures, all computed. **Figure 2 was an audited plate taken unmodified** — row 33 of
`method/PROOF-FIGURES.tsv`, graded NAMED-GENERATION against caption 6.2, sourced from
`extracted/archives/the-method-1-6-figures-build8/figures/figure-6.2.png`, md5
`b383daa6351d7fb140a7055651649f1f`. The audit (A-16) found that the plate's own title is drawn over
its period-1 row and overprints the red cells it describes at print size, so it is **replaced by a
computed figure**, `figures.py fig_periodic()`, drawn from `check.py periodic_cells(18)` and `stair()`
— the same 90 cells the check closes, cell for cell the plate's data. `FIGURES.tsv` records the
replaced plate's path and md5 and the reason. Its four checkable facts — 90 held, 36 admitted and
denied, 126 in all, and the red pattern at period 1 groups 2–17 and periods 2–3 groups 3–12 — are
produced by `check.py`'s periodic-table row, so the caption prints nothing the check does not.

The other four are computed by `figures.py` from `check.py`'s own reference implementation, which
`figures.py` imports by path; Figure 1's |ℛ| = 9 and E = 4 now have their own `check.py` row (A-7)
and Figure 3's grid is the 4×5 box the nine cells realise (A-17). `FIGURES.tsv` records for each the file, the paper's figure number,
what it shows, how it was made and the md5. The second audited plate that bears on this material
(row 32, caption 6.1 — the external definition cost of seven indices) is not used: four of its seven
indices are outside this paper, and its two that are inside are already printed as numbers in §2.
