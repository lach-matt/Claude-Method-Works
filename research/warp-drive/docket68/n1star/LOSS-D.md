# LOSS-D -- the loss d of III.J''' Theorem 4.1, added up as far as the record allows (E1')

Status: written (D347); LD3 added (D348); read by verifier 164 (D348), whose three major findings (the structure of d,
the scope of LD3, a second nested loop) and its minor findings and nits are seated (LD4). To be read again.

EFFECTIVE-CONSTANTS.md (E1') called the loss d "bookkeeping": add up III.J''''s losses part by part, so that the
exponent 8d+2 and N = 21d+6 become numbers. This note does that bookkeeping and finds that it does not end in a
number. The record gives d as a nested composition whose elementary losses are explicit formulas in the weights the
proof chooses, apart from six losses whose proofs give no closed form, and whose loop counts are chosen under
step-size bounds. The weights are fixed only by inequalities against the index sets of 5D Tangherlini. So d is a
number once three things are done (section 4), and not before. Two loop counts are already known at the record's
parameter point, and they are very large (LD3). On the way, k'' turned out never to be defined in III.K (LD1).

Labels. Parts with many primes are named by file: I15 = PART-III-I15-AUGMENT5.md, III.I with fourteen primes; I16 =
PART-III-I16-BASEPOINTS.md, fifteen primes; I14 = PART-III-I14-LEVELS.md, thirteen primes. Sources: two extractions
over proof5 (D347), quoting file and line, spot-read here where a finding rests on them, and verifier 164 (D348).

## 1. The structure of d

III.J''' Theorem 4.1 (PART-III-J3-TAME.md:278, proof 288-292) is an induction over the parts: each part's solution
map is a composition of a fixed number of the families of Lemma 2.1 (FWD, BG, MOD, FIN, INT) and of the solution maps
of earlier parts, which the table of section 3 (lines 255-272) lists per part. Lemma 1.2 (lines 62-86) gives upper
bounds for the losses: a composition adds them (b), an N-fold composition costs N times the loss (e), a sum or a
finite-dimensional assembly keeps the larger (a, c), and a family whose order-k bounds each have loss at most d has
loss d (g). So the loss is a recursion over calls, not a sum over rows:

    d(part) = Σ over the steps of its composition [the elementary loss of the step, or d(called part)],           (1.1)

each loop of the part contributing its count times the loss of one pass, and an inner part's loss counted once per
call. The d that III.K needs is III.K Lemma 2.3's (PART-III-K-NONLINEAR.md:411-416), the right inverse's loss in II.G
Theorem 2.1, which is at least Theorem 4.1's d at the top part, I15's Theorem 3.1. Two rows of the table lie outside
Theorem 4.1: line 271 (I16 Proposition 2.5, at b ≠ b_0) and line 272 (III.J' Theorem 2.1, Theorem 4.2's). And (1.1)
bounds the d that this proof produces: Lemma 1.2's rules are upper bounds, so the optimal loss may be smaller.

## 2. The elementary losses

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
| the "+5" of J3 Lemma 2.1 (a) | PART-III-I-CONE.md:376-383, 422-424 | III.I Corollary 5.2's class (0; k−5), from H^(k−2) ⊂ C^(k−5) in dimension 5 |
| N_* (III.I'''''''''' windows) | PART-III-I11-SPACETIME.md:72-73 | ⌈5/η_0⌉ + 2, η_0 := min(Re π_1(E_ind ∪ E^ι_ind) ∪ {1}) |
| the zero-energy levels at n = 4 | PART-III-I12-SPECTRAL.md:14, 528-529 | four solves, α_K = 4 + ε_K |
| fixed small losses | J3 Lemma 2.1 (b)-(e), (g) | 0 (finite-dimensional, III.A L1.2, 3.2, III.H Cor 4.2), 1 (II.G' P3.3 (1), III.H P3.2), 2 (order-2 operators: L_b, L̃, and BG applied to R_q u, J3:115, 121) |

**Not in closed form.** Six losses are fixed by their proofs only as a sum of losses met, by citation, or with a
part that depends on s without a formula:

1. III.A Proposition 4.2 (1)'s l (PART-III-A-PREREQ.md:571; proof 649-704): a recursion over the index set, l' := l −
   |E_(I,≤)| − l_0, l_0 the loss with E_I = ∅, and "l the sum of the losses met".
2. II.G' Corollary 4.2 (1)-(2)'s ℓ (II.G2:673): "there is ℓ ∈ N_0, depending only on P̂"; no ℓ in the proof's lines read.
3. III.G''' Proposition 3.7's l (G4:372-388): Lemma 3.5's loss, no formula.
4. III.G''' Corollary 3.1's loss (G4:272-290): not located.
5. III.I'' Lemma 4.2's ℓ (PART-III-I3-ALMOST.md:244-255): from II.G' Proposition 4.7's proof with III.H Corollary 4.2 and
   Theorem 4.1 (3).
6. III.G' Theorem 3.1 (2)'s d (PART-III-G2-IOTA.md:173, 375-382): at most ⌈ℓ_I − Re λ⌉ + 2 steps of two b-derivatives
   each, plus d_1(s) and m(s), which depend on s with no formula: d ≤ d_1(s) + m(s) + 2(⌈ℓ_I − Re λ⌉ + 2) (verifier
   164's m1).

Each is finite by its proof; each needs that proof re-read with the losses carried (E1'b).

## 3. The weights and the counts

**Weights.** Fixed only by inequalities at n = 4:

- ℓ_I: 3 + ε_+ < ℓ_I < min(a_I + ½, ℓ_I^max), off discrete exclusion sets (PART-III-I11-SPACETIME.md:46 (H4);
  PART-III-I6-ALMOSTBDD.md:27-28 and PART-III-I4-BOOST.md:264 for III.I'' (5.1)).
- The top decay order: α ∈ (4, 4 + ε_K] for I15's theorem (I15:37), used with α > 4 at I15:227 and I15:324; the
  admissible orders range over (2, 4 + ε_K] (I11:156); α_K = 4 + ε_K (I12:14); ε_K small with no Re λ in (2, 2+ε_K] ∪
  (3, 3+ε_K] (I11:153); ε'_0 := ½ min(ε_K, ε_+ − ε_K) (I11:157-158); ε_ind ∈ (0, 1] with d(Re λ, Z) ≥ ε_ind
  (PART-III-F2-INDICIAL.md:130-131); w_+ = 5 + ε_+ (I11:32); 0 < ε_K < ε_+ < min(δ♯, ε_ind) (PART-III-J-PARAM.md:34).
- The β-weights per use (II.G' Corollary 4.5 and Proposition 3.5): β_I, β_ι, β_K free with conditions (II.G2:444,
  834), fixed at each use by the α's and ℓ_I (I4:162-163, 197, 224-225; I7:287; I14:130).

None of ε_+, ε_K, ε_ind, ε, E_ind, E_+, ℓ'_+, ℓ_I^max is given a number at n = 4. They are constrained by the index sets
of the operators at 5D Tangherlini, which the record computes (indicial roots, resonances) but does not turn into
chosen numbers; the one number it states is ε_ind < 3 × 10⁻⁶ at its parameter point (F2:133-136).

**Counts.** The loops, each a count in (1.1):

- the α-levels α_0 < … < α_N = α of III.I'''''''' with α_(i+1) − α_i < a_K − 2 (PART-III-I9-COMMOTION.md:374-375), and
  its rounds i_0, "finitely many" (I9:304);
- I15's β-levels α_1 = β_0 < … < β_K = α with β_(k+1) − β_k < α − 4 (I15:323-324);
- at every β-level, I14's level-3 loop, whose tf-weights rise by ε_ind − ε per round, τ = τ_3 + i(ε_ind − ε) from τ_3 =
  1 + η_2 − 2ε (η_2 < ε_+ < ε_ind) up to β − 2 (I14:120-128; PART-III-I12-SPECTRAL.md:287-297), composed by III.J'''
  (J3:44-45, 170-171, line 267); I15 calls I14's Lemma 2.2 at every β-level (I15:342-343).

**The order of choices for δ.** J3 Lemma 2.1 (f) makes Corollary 4.5's k-dependent loss ⌈kδ⌉ + ℓ into ℓ + 1 by
choosing η and the trapping data with (k+1)δ_Γ(−η) ≤ 1 (J3:149-154, 184-192), and ℓ does not depend on η or the
trapping data (J3:150-151). So d is fixed first, then N = 21d + 6, then η and the trapping data at the order N. The
smallness constants are used at the orders k ≤ N only (III.K:410-411); the tame estimate itself at every order.

## 4. What a number needs

- **E1'a. The weights.** Choose numbers for ε_ind, ε_K, ε_+, ε, ℓ_I, a_I, ℓ_I^max, the E_+ bound and the β's at each
  use, from the computed index sets at n = 4, satisfying every inequality of section 3. First question: whether
  another admissible parameter point than the record's moves the lowest root λ^C − 1 away from 1, so that ε_ind is
  not of order 10⁻⁶.
- **E1'b. The six losses** of section 2, by re-reading their proofs with the losses carried.
- **E1'c. The counts** of section 3 (the α-levels and rounds, the β-levels, the level-3 rounds at each β-level) from
  their step bounds and the chosen weights, and (1.1) evaluated at I15's Theorem 3.1.

Then (1.1) is a finite expression in integers. Until then the honest statement is: the d this proof produces is an
explicit function of finitely many chosen weights and of six losses that the record proves finite without computing.

## 5. Findings

- LD1 (k'' undefined; MINOR, repaired). III.K wrote H^(k+k'') (Lemma 2.2 (d), the e_S bound in Lemma 2.3's proof, the
  Smallness paragraph) and d_1 := N + k'', and Part VIII uses the same bound (PART-VIII-LINEAR.md:198-199), but k'' was
  defined nowhere in proof5. The bound comes from III.K Proposition 1.2 (3) (III.K:131-132), which gives "for each k
  there are k' and C_k": a loss k'_k that may depend on k. Repair: Lemma 2.2 (d) and Part VIII's bound carry k'_k at
  every order; III.K defines k'' := max_(k ≤ N) k'_k, finite, used in the smallness constants (orders k ≤ N, and the
  norm F^(2d), 2d ≤ N); and the e_S bound, which II.G Theorem 2.1 (2.4) needs at every order k (PART-II-G-
  NASHMOSER.md:73-80), carries k'_k in its high-order term and k'' only in its fixed low-order factor (D348, verifier
  164's m2; III.K:233-236, 303-305).

- LD2 (the record's own description). EFFECTIVE-CONSTANTS.md called E1' bookkeeping. It is a reduction to E1'a-E1'c;
  the description is corrected there.

- LD3 (two long loops at the record's parameter point; about the size of the d this proof produces, not a gap in any
  proof). (i) I15's β-chain: α ∈ (4, 4 + ε_K] (I15:37) and α_1 ∈ (2, α − 2) (I15:305), so the chain climbs more than 2
  in steps below α − 4 ≤ ε_K, and K > 2/(α − 4) ≥ 2/ε_K. With ε_K < ε_ind < 3 × 10⁻⁶ (J-PARAM:34, F2:133-136), K > 6.8 ×
  10⁵. The levels are composed in the proof itself: level k + 1 takes R_q u with u at level k (I15:327-329), R_q is of
  second order (I15:179-181), and the one-step route of the source is closed at n = 4 (I15:12-17). Within III.J''''s
  accounting each level costs at least 2 (BG applied to R_q u, J3:115, 121), so the d it produces is at least 2K >
  1.3 × 10⁶, and N = 21d + 6 > 2.8 × 10⁷. (ii) Nested inside, at every β-level, I14's level-3 loop rises by ε_ind − ε
  per round from about 1 to β − 2, so about (β − 3)/ε_ind rounds at the levels above 3, about 3 × 10⁵ near β = 4. Over
  the β-chain this is of order (1/ε_K)(½/ε_ind) > 5 × 10¹⁰ rounds; if a round costs a derivative (E1'b: it rests on
  III.F' Corollary 3.4's ℓ), the d this proof produces exceeds that. (iii) These bound the d that III.J''''s accounting
  of the record's proof delivers: Lemma 1.2's rules are upper bounds, Theorem 4.1 is existential, and the optimal loss
  may be far smaller. The levers: the parameter point (E1'a's first question); a per-level gain larger than α − 4; a
  different proof of the level step, keeping in mind that the source's one-step route is closed at n = 4 (I15:12-17).

- LD4 (verifier 164, D348). No blocking finding. M1: section 1 described d as a flat sum over the table's rows; it is
  the recursion (1.1), with two rows outside Theorem 4.1. M2: LD3 bounds the d III.J''' produces, not the optimal loss.
  M3: the level-3 loop nested inside the β-chain was missing; it is LD3 (ii) and in the counts. m1: III.G' Theorem 3.1
  (2)'s d has parts d_1(s), m(s) with no formula, the sixth loss of section 2. m2: the k'' scope sentence in III.K was
  false at the e_S bound; repaired there. m3: LD3's conditional is already discharged within the accounting (2 per
  level). m4: the labels of the many-primed parts, now file names. Nits: I15:37 cited for α; K > 2/ε_K; Lemma 1.2 (e),
  (g) described correctly; III.K line numbers updated.
