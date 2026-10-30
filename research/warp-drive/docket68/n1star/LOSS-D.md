# LOSS-D -- the loss d of III.J''' Theorem 4.1, added up as far as the record allows (E1')

Status: written (D347); to be read.

EFFECTIVE-CONSTANTS.md (E1') called the loss d "bookkeeping": add up III.J''''s losses part by part, so that α = 8d+2
and N = 21d+6 become numbers. This note does that bookkeeping and finds that it does not end in a number. The record
gives d as a finite composition whose step losses are explicit formulas in the weights the proof chooses, apart from
five losses whose proofs give no closed form, and whose step counts are chosen freely under step-size bounds. The
weights themselves are fixed only by inequalities against the index sets of 5D Tangherlini. So d is a number once
three things are done (section 4), and not before. On the way, one symbol of III.K, k'', turns out never to be
defined (LD1, repaired).

Sources: two extractions over proof5 (D347), each quoting file and line; the lines below are theirs, spot-read here
where a finding rests on them.

## 1. The structure of d

III.J''' Theorem 4.1 (PART-III-J3-TAME.md:278, proof 288-292): "Lemma 1.2 (b)-(g) gives a tame family with a loss d
equal to the sum of the losses, independent of k, for d_0 ≥ d and δ_0 small". The sum runs over the 18 rows of III.J'''
section 3 (lines 255-272), each a composition of the families of Lemma 2.1 (FWD, BG, MOD, FIN, INT) with the solution
maps of earlier parts. The composition rules are Lemma 1.2 (lines 62-86): losses add under composition (b), a sum or a
finite-dimensional assembly keeps the larger (a, c, g), an N-fold product costs Nd (e). So

    d = Σ_rows Σ_steps (loss of the step),                                                                      (1.1)

with the step counts of section 3's table and the step losses of Lemma 2.1 (a)-(g). The table has no loss column; its
step counts are "1", "finitely many", or a number of levels or rounds (section 3 below).

## 2. The step losses

**Explicit in the weights.** These have closed forms in the proofs:

| loss | where fixed | formula |
|---|---|---|
| ℓ of II.G' Corollary 4.5 (J3 Lemma 2.1 (f)) | PART-II-G2-DECAY.md:859 | ℓ = 2ℓ_3 + ℓ_4 + ℓ_5 |
| ℓ_3 | II.G2:851-852 | 1 + ⌈(max(β'_K, β'_ι − β'_I) − ½)₊⌉ |
| ℓ_5 | II.G2:848-849 | ⌈(½ − min(β_K, β_ι + 1 − β_I))₊⌉ |
| ℓ_4 | II.G2:828, 853 | ℓ_1 + ℓ_2 + 2N + ⌈(δ_2 − δ_1)₊⌉, with δ_1 = δ_2 = 0 at the use |
| ℓ_1, ℓ_2 | II.G2:789, 775-776 | ℓ_1 := max(⌈(s−1)₊⌉, ⌈sup r − r_out⌉); ℓ_2 := max(⌈(−s)₊⌉, ⌈r_out − inf r⌉) |
| N of Lemma 4.3 | II.G2:773, 776, 790 | from N_0 := ⌈(−min(b_out, inf b))₊ + 1⌉ and N_1, which is ⌈(−inf b)₊⌉ at 776 and ⌈(sup b)₊⌉ at 790 |
| r_out, β_scf at Cor 4.5 | II.G2:690, 850, 938 | r_out := β_scf − 2 − ε/2; β_scf := β'_I + ε |
| ℓ of II.G' Prop 3.5 (1) | II.G2:530 | ⌈(max(β_ι − β_scf, β_K) + ε − ½)₊⌉ |
| ℓ of II.G' Prop 3.5 (2) | II.G2:536-537 | ⌈(3/2 − δ)₊⌉ + ⌈(β' − ½)₊⌉, β' := max(β_K, β_ι − β_I) |
| III.I'' Lemma 3.1's ℓ | PART-III-I3-ALMOST.md:121, 141 | Prop 3.5 (1)'s, at β_I = 3/2, β_ι = α♯_+ + 1, β_K = α_K − 1 (PART-III-I4-BOOST.md:224-225) |
| III.F' Corollary 3.4 | PART-III-F2-INDICIAL.md:488-491 | Lemma 4.1's ℓ := max(⌈sup r − r_out⌉, ⌈(s−1)₊⌉), ℓ̃ := max(⌈r_out − inf r⌉, ⌈(−s)₊⌉) |
| III.G''' Lemma 2.2's l | PART-III-G4-RESONANT.md:114 | 2⌈ℓ_I⌉ + 10 |
| III.G''' Prop 2.4's l' | G4:225 | l + sup d, d of III.G' Theorem 3.1 (2) |
| III.G' Theorem 3.1 (2)'s d | PART-III-G2-IOTA.md:375-383 | at most ⌈ℓ_I − Re λ⌉ + 2 steps, each losing two b-derivatives: d ≤ 2(⌈ℓ_I − Re λ⌉ + 2) |
| the "+5" of J3 Lemma 2.1 (a) | PART-III-I-CONE.md:376-383, 422-424 | III.I Corollary 5.2's class (0; k−5), from H^(k−2) ⊂ C^(k−5) in dimension 5 |
| N_* (III.I'''''''''' windows) | PART-III-I11-SPACETIME.md:72-73 | ⌈5/η_0⌉ + 2, η_0 := min(Re π_1(E_ind ∪ E^ι_ind) ∪ {1}) |
| the zero-energy levels at n = 4 | PART-III-I12-SPECTRAL.md:14, 528-529 | four solves, α_K = 4 + ε_K |
| fixed small losses | J3 Lemma 2.1 (b)-(e), (g) | 0 (finite-dimensional, III.A L1.2, 3.2, III.H Cor 4.2), 1 (II.G' P3.3 (1), III.H P3.2), 2 (order-2 operators, L_b, L̃) |

**Not in closed form.** Five losses are fixed by their proofs only as "the sum of the losses met" or by citation:

1. III.A Proposition 4.2 (1)'s l (PART-III-A-PREREQ.md:571; proof 649-704): a recursion over the index set, l' := l −
   |E_(I,≤)| − l_0, l_0 the loss with E_I = ∅, and "l the sum of the losses met".
2. II.G' Corollary 4.2 (1)-(2)'s ℓ (II.G2:673): "there is ℓ ∈ N_0, depending only on P̂"; no ℓ in the proof's lines read.
3. III.G''' Proposition 3.7's l (G4:372-388): Lemma 3.5's loss, no formula.
4. III.G''' Corollary 3.1's loss (G4:272-290): not located.
5. III.I'' Lemma 4.2's ℓ (PART-III-I3-ALMOST.md:244-255): from II.G' Proposition 4.7's proof with III.H Corollary 4.2 and
   Theorem 4.1 (3).

Each is finite by its proof; each needs that proof re-read with the losses carried (E1'b).

## 3. The weights and the counts

**Weights.** Fixed only by inequalities at n = 4:

- ℓ_I: 3 + ε_+ < ℓ_I < min(a_I + ½, ℓ_I^max), off discrete exclusion sets (PART-III-I11-SPACETIME.md:46 (H4);
  PART-III-I6-ALMOSTBDD.md:27-28 and PART-III-I4-BOOST.md:264 for III.I'' (5.1)).
- α ∈ (2, 4 + ε_K] admissible (I11:156), α_K = 4 + ε_K (I12:14); ε_K small with no Re λ in (2, 2+ε_K] ∪ (3, 3+ε_K]
  (I11:153); ε'_0 := ½ min(ε_K, ε_+ − ε_K) (I11:157-158); ε_ind ∈ (0, 1] with d(Re λ, Z) ≥ ε_ind (PART-III-F2-
  INDICIAL.md:130-131); w_+ = 5 + ε_+ (I11:32).
- The β-weights per use (II.G' Corollary 4.5 and Proposition 3.5): β_I, β_ι, β_K free with conditions (II.G2:444,
  834), fixed at each use by the α's and ℓ_I (I4:162-163, 197, 224-225; I7:287; I14:130).

None of ε_+, ε_K, ε_ind, ε, E_ind, E_+, ℓ'_+, ℓ_I^max is given a number at n = 4. They are constrained by the index sets
of the operators at 5D Tangherlini, which the record computes (indicial roots, resonances) but does not turn into
chosen numbers.

**Counts.** The α-levels α_0 < … < α_N = α are chosen with α_(i+1) − α_i < a_K − 2 (PART-III-I9-COMMOTION.md:374-375);
the β-levels β_0 < … < β_K = α with steps below α − 4 (PART-III-I15-AUGMENT5.md:323-324); the rounds i_0 are "finitely
many" (I9:304). Each count is bounded by a quotient of fixed lengths once the weights are numbers.

**The order of choices for δ.** J3 Lemma 2.1 (f) makes Corollary 4.5's k-dependent loss ⌈kδ⌉ + ℓ into ℓ + 1 by
choosing η and the trapping data with (k+1)δ_Γ(−η) ≤ 1 (J3:149-154, 184-192), and ℓ does not depend on η or the
trapping data (J3:150-151). So d is fixed first, then N = 21d + 6, then η and the trapping data at the order N; the
estimates are used at the orders k ≤ N only (III.K:410-411). No circularity.

## 4. What a number needs

- **E1'a. The weights.** Choose numbers for ε_ind, ε_K, ε_+, ε, ℓ_I, a_I, ℓ_I^max, the E_+ bound and the β's at each
  use, from the computed index sets at n = 4, satisfying every inequality of section 3.
- **E1'b. The five losses** of section 2, by re-reading their proofs with the losses carried.
- **E1'c. The counts** N, K and i_0 from their step bounds and the chosen weights.

Then (1.1) is a finite sum of integers. Until then the honest statement is: d is an explicit function of finitely
many chosen weights and of five losses that the record proves finite without computing.

## 5. Findings

- LD1 (k'' undefined; MINOR, repaired). III.K writes H^(k+k'') (PART-III-K-NONLINEAR.md:233, 302, 411, 413) and
  d_1 := N + k'', and Part VIII uses the same bound (PART-VIII-LINEAR.md:198), but k'' is defined nowhere in proof5.
  The bound comes from III.K Proposition 1.2 (3) (III.K:131-132), which gives "for each k there are k' and C_k": a
  loss k'_k that may depend on k. Repair: Lemma 2.2 (d) holds with k'_k at every order, and III.K now defines k'' :=
  max_(k ≤ N) k'_k, finite, which is all the smallness argument uses (the constants C_k with k ≤ N, and the norm
  F^(2d) with 2d ≤ N). Part VIII's bound at an order k > N reads k'_k for k''.

- LD2 (the record's own description). EFFECTIVE-CONSTANTS.md called E1' bookkeeping. It is a reduction to E1'a-E1'c;
  the description is corrected there.
