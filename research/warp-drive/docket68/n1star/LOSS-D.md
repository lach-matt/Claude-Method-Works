# LOSS-D -- the loss d of III.J″ Theorem 4.1, added up as far as the record allows (E1')

Status: written (D347); LD3 added (D348), LD5 (D353), section 2b (E1'b, D357), LD6 (D365), LD7 (D377, which corrects LD6
(ii)-(iii); repaired D380). Read by verifier 164 (D348), whose three major findings (the structure of d, the scope of
LD3, a second nested loop) and its minor findings and nits are seated (LD4); section 2b read by verifier 166 (D358),
findings seated. LD6-LD8 to be read (LD8: D397). LD9 (D408), LD10 (D420, D422), LD11 (D507, corrected D509 after
verifier 218), LD12 (D514, corrected D516 after verifier 221), LD13 (D529, corrected D531 after verifier 229), LD14 (D534, corrected D538 after verifier 232 and D541 after verifier 234; the reading settled at source D542, its argument corrected D544), LD15 (D550), LD16 (D553, corrected D557, D560, D562).

EFFECTIVE-CONSTANTS.md (E1') called the loss d "bookkeeping": add up III.J″'s losses part by part, so that the
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

III.J″ Theorem 4.1 (PART-III-J3-TAME.md:278, proof 288-292) is an induction over the parts: each part's solution
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

1. III.A Proposition 4.2 (1)'s l (PART-III-A-PREREQ.md:571; proof 649-704): a recursion over the index set, l' := l
   − |E_(I,≤)| − l_0, l_0 the loss with E_I = ∅, and "l the sum of the losses met".
2. II.G' Corollary 4.2 (1)-(2)'s ℓ (II.G2:673): "there is ℓ ∈ N_0, depending only on P̂"; no ℓ in the proof's lines read.
3. III.G''' Proposition 3.7's l (G4:372-388): Lemma 3.5's loss, no formula.
4. III.G''' Corollary 3.1's loss (G4:272-290): not located.
5. III.I'' Lemma 4.2's ℓ (PART-III-I3-ALMOST.md:244-255): from II.G' Proposition 4.7's proof with III.H Corollary 4.2 and
   Theorem 4.1 (3).
6. III.G' Theorem 3.1 (2)'s d (PART-III-G2-IOTA.md:173, 375-382): at most ⌈ℓ_I − Re λ⌉ + 2 steps of two b-derivatives
   each, plus d_1(s) and m(s), which depend on s with no formula: d ≤ d_1(s) + m(s) + 2(⌈ℓ_I − Re λ⌉ + 2) (verifier
   164's m1).

Each is finite by its proof; each needed that proof re-read with the losses carried (E1'b, done in section 2b).

## 2b. The six losses carried (E1'b, D357)

Each proof re-read with its losses carried. Notation: n_H := |E_(H,≤)|, the number of pairs (z, m) of the index set E_H
with Re z ≤ β_H; ⌊·⌋, ⌈·⌉ as usual; ϑ_in, ϑ_H the threshold quantities of the operator at the incoming radial set and
the horizon (I.A); s_c the fixed regularity order of II.G' Corollary 4.2's proof, s_c > ½ + ϑ_H. Where a proof states
"costs at most one derivative", that bound is carried; it is an upper bound.

1. **III.A Proposition 4.2.** Its inputs are lossless except as stated. II.G' Proposition 3.3 (1) ((2.25a)) loses 1.
   The converse of Lemma 1.3 loses n_H, each factor costing one derivative. The direct Lemma 1.3, Lemma 1.2 and Lemma
   3.3 lose nothing beyond their a priori hypotheses. (2.26a) loses ℓ_F := ⌈(max(β_ι − β_scf, β_K) + ε − ½)₊⌉
   (II.G' Proposition 3.5 (1)), and so do its harmless terms at the weights used.
   - *Part (1), E_I = ∅.* (4.6) costs 1. R_ι u has order k + l − n_ι, and (2.25a) on it gives (4.7) with l ≥ n_ι + 1.
     R_K u has order k + l − n_K, and (4.7) on it costs n_ι + 1. The extra product ∏_(j≤⌊β_K−1⌋)(σ∂_σ − j) costs
     ⌊β_K⌋. Integrating the n_K + ⌊β_K⌋ factors one at a time costs one each. So l_0 = 1 + n_ι + 2(n_K + ⌊β_K⌋).
   - *Part (1), general E_I.* χ_K u costs l_0. For u vanishing near K, the K-weight is raised to β'_K, the least
     admissible non-integer above B := max(β_K, β_ι + max(0, −min Re π_1E_I)), so ⌊β'_K⌋ = ⌊B⌋ and E_K = ∅.
     Then R_I u costs n_I, the case E_I = ∅ costs 1 + n_ι + 2⌊β'_K⌋, and Lemma 3.3 is lossless given its a priori
     order. Integrating at
     scf costs n_I.
   - So III.A Proposition 4.2 (1) has

         l = 1 + n_ι + 2 max(n_K + ⌊β_K⌋, n_I + ⌊B⌋).                                                            (2.1)

   - *Part (2).* With E_K = ∅, (4.8) costs ℓ_F and R_tf costs n_ι, and Lemma 1.3 at ι is lossless: l_2 = n_ι + ℓ_F. For
     general E_K, R_zf costs n_K and Lemma 1.3 at K is lossless. So

         l = n_ι + n_K + ⌈(max(β_ι − β_scf, β_K) + ε − ½)₊⌉.                                                     (2.2)

2. **II.G' Corollary 4.2.** Its ℓ is in the proof (II.G2:698-702), past the lines the D347 extraction read. It is
   ℓ = ℓ_a + ℓ̃, with ℓ_a := max(⌈(½(−1 + ϑ_in) + 7/2 − β_scf)₊⌉, ⌈(s_c − 1)₊⌉) and ℓ̃ := ⌈(−s_c)₊⌉. The proof needs
   only s_c > ½ + ϑ_H, and ϑ_H may be negative, so s_c ≥ 0 is taken as a further choice; then ℓ̃ = 0 and

       ℓ = max(⌈(ϑ_in/2 + 3 − β_scf)₊⌉, ⌈(s_c − 1)₊⌉);                                                           (2.3)

   (1) then loses j + ℓ for ∂_σ^j.
3. **III.G''' Proposition 3.7.** (3.6) is continuous by Proposition 2.4, with loss l'. The range and the right inverse
   use Lemma 3.5's map u ↦ f, which loses 2 (Lemma 2.3, N_ι⁺ being of order 2). So l = max(l', 2) = l', where
   l' = 2⌈ℓ_I⌉ + 10 + sup d over the strip of Proposition 2.4 (G4:221-226), and d is loss 6.
4. **III.G''' Corollary 3.1.** It is stated at order ∞. At finite order, (1) comes from Proposition 2.4 on a strip
   containing λ_0, so it loses l' = 2⌈ℓ_I⌉ + 10 + sup d. (2) loses nothing more: III.G'' Theorem 3.1's expansion costs
   nothing relative to u (G3:202-213). Its functionals, continuous on H^(k+2), are counted separately where III.J's proof
   of Theorem 2.4 sums the losses (PART-III-J-PARAM.md:352-355: "d is the sum of these losses plus 2"); a +2 here
   would count them twice (verifier 166's F3).
5. **III.I'' Lemma 4.2.** The proof is II.G' Proposition 4.7's. That gives ℓ = ℓ_a + ℓ̃, with ℓ_a and ℓ̃ from II.G'
   Lemma 4.1 for the orders r_± ∈ [r_out, r_in], where r_out := β_scf − 2 − ε/2 and r_in := max(r_out, ½(−1 + ϑ_in) + 1).
   So ℓ̃ = ⌈(−s_c)₊⌉ = 0 (s_c ≥ 0, as in item 2), and

       ℓ = max(⌈(ϑ_in/2 + 5/2 + ε/2 − β_scf)₊⌉, ⌈(s_c − 1)₊⌉),                                                 (2.4)

   with ϑ_in, ϑ_H those of L̃_b (S̄ = 0) and β_scf < 3/2. For the same operator data this is at most (2.3)'s ℓ.
6. **III.G' Theorem 3.1 (2).** Write d = d_1 + m(s) + 2(⌈ℓ_I − Re λ⌉ + 2) (Step 5; verifier 164's m1). Carried here:
   - *d_1 = 0.* Step 5 (i) puts F := the extension by 0 of v^(−2−λ)f in L¹ in v, with values in H^(k+d)(S³). Hence
     F ∈ H^(−½−δ)(ℝ; H^(k+d)(S³)) ⊂ H^(s−1)(ℝ × S³), since s − 1 ≤ −½ − δ (the inclusion
     H^σ(ℝ; L²(S³)) ⊂ H^σ(ℝ × S³) for σ ≤ 0 has no loss).
     - The module fields: L_Ω commutes with the extension, and (v∂_v)^j F is the extension of (v∂_v)^j(v^(−2−λ)f) for
       every j ≤ k + d. The boundary term at v = 0 vanishes by the b-Sobolev embedding in v alone, which uses one
       v∂_v-derivative of (v∂_v)^(j−1)(v^(−2−λ)f), so order j ≤ k + d.
     - Near R = 0 the space is H^(s−1+k')_(b,μ) ⊃ R^(ℓ_K+Re λ) H^(k+d)_b for k' ≤ k + d (s < 1, μ < ℓ_K + Re λ); in
       between, H^(s−1+k') ⊃ H^(k+d).
     - So F ∈ Ḣ^((s−1;k+d),μ)_(b;b), and III.G Theorem 5.1 (3) inverts at the same k.
   - *m(s).* By Lemma 2.1's proof, m(s) = 2 + ⌈max(0, −s)⌉ + j(s), with j(s) := ⌈½ − s⌉, the least j with s + j > ½
     (s < ½ here).
   - So, with s = min(½, 2 − Re λ) − δ,

         d(λ) = 6 + ⌈max(0, Re λ − 2 + δ)⌉ + ⌈max(0, Re λ − 3/2) + δ⌉ + 2⌈ℓ_I − Re λ⌉.                        (2.5)

     That is 7 + 2⌈ℓ_I − Re λ⌉ for Re λ < 2 − δ. When 3 < ℓ_I < 3.5 it is at most 12 on 2 ≤ Re λ < ℓ_I.
   - *Over a strip.* d is not monotone in Re λ: at ℓ_I = 3.2 it is 11 at Re λ = 1.4 and at 2.5, and 12 at 2.1 (verifier
     166's F1). So over a strip λ_− ≤ Re λ ≤ ℓ_I − ε, (2.5) is maximised over its breakpoints. When 3 < ℓ_I < 3.5,
     sup d ≤ max(7 + 2⌈ℓ_I − λ_−⌉, 12). Proposition 2.4's strip has λ_− < 3/2 (Lemma 3.4). With λ_− just below 3/2
     this gives sup d = 12, and so l' = 30 in items 3-4.

**What this closes.** The six losses are now closed forms in the following data:

- the weights: the β's, ℓ_I and ε;
- the threshold quantities ϑ_in, ϑ_H of the operators at n = 4;
- the index-set counts n_H;
- free choices still to be made: δ, the strip's ε and λ_−, s_c ≥ 0 and β'_K.

With section 2's table, every elementary loss of (1.1) is a closed form in those data. E1'b is done in that sense
only: integers need E1'a (numbers for the data) and E1'c (the counts). The zf and scf integrations of item 1 are
charged one derivative per factor, as the record's proof does. Lemma 1.3's own count is N − 1, or 0 by its order-k
argument, so (2.1) may be an overcount (F6). Labels: derived here by re-reading the cited proofs (II.G2:690-702,
917-955; G4:200-226, 272-295, 334-388; I3:244-269; G2-IOTA:130-173, 362-392; A-PREREQ:109-138, 440-536, 563-704);
d_1 = 0 is this note's own reading where the record wrote "d_1 depending on s"; PART-III-G2-IOTA.md:375-376 now cites
it. Verifier 166 (D358) checked (2.1)-(2.5), m(s) and d_1 = 0 against the cited lines. Its findings are seated here: F1
the strip rule, F2 s_c ≥ 0, F3 Corollary 3.1 (2), F4 the free choices and λ_− < 3/2, and the nits F5-F10.

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
  1 + η_2 − 2ε (η_2 < ε_+ < ε_ind) up to β − 2 (I14:120-128; PART-III-I12-SPECTRAL.md:287-297), composed by III.J″
  (J3:44-45, 170-171, line 267); I15 calls I14's Lemma 2.2 at every β-level (I15:342-343).

**The order of choices for δ.** J3 Lemma 2.1 (f) makes Corollary 4.5's k-dependent loss ⌈kδ⌉ + ℓ into ℓ + 1 by
choosing η and the trapping data with (k+1)δ_Γ(−η) ≤ 1 (J3:149-154, 184-192), and ℓ does not depend on η or the
trapping data (J3:150-151). So d is fixed first, then N = 21d + 6, then η and the trapping data at the order N. The
smallness constants are used at the orders k ≤ N only (III.K:410-411); the tame estimate itself at every order.

## 4. What a number needs

- **E1'a. The weights.** Choose numbers for ε_ind, ε_K, ε_+, ε, ℓ_I, a_I, ℓ_I^max, the E_+ bound and the β's at each
  use, from the computed index sets at n = 4, satisfying every inequality of section 3. Its first question, whether
  another admissible parameter point moves the lowest root λ^C − 1 away from 1, is answered by LD5: no; the best gap is
  about 3.1 × 10⁻⁵.
- **E1'b. The six losses** of section 2, by re-reading their proofs with the losses carried. Done in section 2b
  (D357): closed forms (2.1)-(2.5) in the weights, the threshold quantities and the index-set counts.
- **E1'c. The counts** of section 3 (the α-levels and rounds, the β-levels, the level-3 rounds at each β-level) from
  their step bounds and the chosen weights, and (1.1) evaluated at I15's Theorem 3.1.

Then (1.1) is a finite expression in integers. Until then the honest statement is: the d this proof produces is an
explicit function of finitely many chosen weights, threshold quantities and index-set counts (section 2b), and of the
loop counts of section 3.

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
  proof). (i) I15's β-chain: α ∈ (4, 4 + ε_K] (I15:37) and α_1 ∈ (2, α − 2) (I15:305), so the chain climbs more than 2 in
  steps below α − 4 ≤ ε_K, and K > 2/(α − 4) ≥ 2/ε_K. With ε_K < ε_ind < 3 × 10⁻⁶ (J-PARAM:34, F2:133-136), K > 6.8 ×
  10⁵. The levels are composed in the proof itself: level k + 1 takes R_q u with u at level k (I15:327-329), R_q is of
  second order (I15:179-181), and the one-step route of the source is closed at n = 4 (I15:12-17). Within III.J″'s
  accounting each level costs at least 2 (BG applied to R_q u, J3:115, 121), so the d it produces is at least 2K > 1.3 ×
  10⁶, and N = 21d + 6 > 2.8 × 10⁷. (ii) Nested inside, at every β-level, I14's level-3 loop rises by ε_ind − ε per round
  from about 1 to β − 2, so about (β − 3)/ε_ind rounds at the levels above 3, about 3 × 10⁵ near β = 4. Over the β-chain
  this is of order (1/ε_K)(½/ε_ind) > 5 × 10¹⁰ rounds; if a round costs a derivative (it rests on III.F' Corollary 3.4's
  ℓ, section 2's table), the d this proof produces exceeds that. (iii) These bound the d that III.J″'s accounting of the
  record's proof delivers: Lemma 1.2's rules are upper bounds, Theorem 4.1 is existential, and the optimal loss may be
  far smaller. The levers: the parameter point (E1'a's first question); a per-level gain larger than α − 4; a different
  proof of the level step, keeping in mind that the source's one-step route is closed at n = 4 (I15:12-17). (iv) [D425:
  with (1.1)'s ε_ind ≤ 1.94 × 10⁻⁸ at the record's point (LD10, D422), (i) gives K > 2/ε_K > 1.03 × 10⁸, the d of
  III.J″'s accounting at least 2K > 2.06 × 10⁸, and N = 21d + 6 > 4.3 × 10⁹. (ii)'s nested loop runs about (β − 3)/ε_ind
  > 5.1 × 10⁷ rounds per level near β = 4, and more than (1/ε_K)(½/ε_ind) > 1.3 × 10¹⁵ rounds over the chain. These are
  lower bounds for what the record's proof delivers, not for the optimal loss, as in (iii).] [D507, LD11: (ii)'s
  condition holds, each round costing at least two derivatives in III.J″'s accounting (corrected D509), so that d exceeds
  2.6 × 10¹⁵ and N exceeds 2.78 × 10¹⁶.] [D514, LD12: the levels below 3 run a loop of the same size, so d >
  5.3 × 10¹⁵ and N > 1.11 × 10¹⁷.]

- LD5 (E1'a's first question answered: no admissible point opens the gap; D353). The record's construction fixes the
  damping parameters (v, e, h) by e ≤ e_0(v) ≈ 6.9 × 10⁻⁵ v² (the interior saddle, semiclass5.py W4) and h below e (the
  roots near 2 stay above 2 only there, damping5.py U6). `checks/gapscan5.py` computes the gap near 2 of the scalar
  indicial roots over that region: it is set by h, about c(v) h for h ≪ e with c(1/2) ≈ 3.06, flat in e (G2), and its
  largest value, at e = e_0(v), h → e, v ≈ 0.45, is about 3.1 × 10⁻⁵ (G3), against 2.93 × 10⁻⁶ at the record's point
  (G1). Since ε_ind is at most this gap, at every admissible point ε_K < ε_ind < 3.1 × 10⁻⁵, so LD3's counts improve by
  at most about ten: K > 6.5 × 10⁴, the d this proof produces exceeds 1.3 × 10⁵, and the nested loop runs more than
  5 × 10⁸ rounds. A gap of order one needs a different constraint damping, not a different point of this one.

- LD6 (the β-chain's step is set by the top order, and the top order is a choice; D365). (i) The step bound β_(k+1) −
  β_k < α − 4 comes from R_q u ∈ 𝒴⁰_2(β) for β < β_k + α − 4 (I15:324, 328-329, Lemma 2.3 with w = β_k − 2). R_q's
  coefficients, from q, have K⁺-order (α − 2)−, and R_q is of second order, so a level gains α − 4. (ii) The cap α ≤ 4 +
  ε_K is stated as the order that four zero-energy solves reach [LD7: the count is not the cap]: "The source reaches the
  order α_K = 4+ε_K through zero-energy solves ... The zf-Taylor expansion ... has four terms (orders σ⁰, …, σ³, as α −
  1 > 3)" (I12:14-16); "The order α_K = 4+ε_K needs four zero-energy solves" (I12:528-529). No indicial root or
  resonance is named there as blocking a higher order. (iii) [Corrected by LD7: four solves already serve every α ≤ 5,
  and the cap is the gap condition (G), so this is not the lever.] So a lever for LD3 (i), not yet examined: a fifth
  solve would carry the zf expansion to σ⁴. If that term exists at n = 4, without a log term or a zero-energy
  obstruction (to be checked: n = 4 is even, where logarithms enter the free resolvent's expansion), it would take α
  towards 5. The step would then be about 1 and K about 3, against K > 6.5 × 10⁴ now. The exclusions of ε_K
  (I11:152-154) would then have to hold on the longer range. The source's one-step route needs, among other conditions,
  the background's K⁺-order α − 2 − ε ≥ 4 + ε_K (I15:14-16), so α above 6 + ε_K, two orders further. LD3 (ii), the
  nested level-3 loop, is set by ε_ind and is untouched by this lever (LD5).

- LD7 (the cap on α is ε_+, not the number of solves; deduced from the record's text, D377, repaired D380 after verifier
  174). It corrects LD6 (ii)-(iii).
  - *The Taylor count is not the cap.* The zf-Taylor expansion of the source needs the orders σ⁰, …, σ^(⌈α−1⌉−1)
    (deduced; I12:16 states the case "orders σ⁰, …, σ³, as α − 1 > 3"), so four terms cover every α − 1 ≤ 4. LD6 (ii)
    read the record's "four solves reach 4 + ε_K" as a cap set by the count, and LD6 (iii)'s fifth solve addresses only
    the count.
  - *What ties α − 4 to ε_+ with four solves.* Level 3's conormal outputs lie above α − 2 because η_2 exceeds α − 4:
    their K⁺-weight is at least 2 + η_2 − 2ε (I12:349-350, 531-532), with η_1, η_2 chosen in (ε_K, ε_+) (I12:58). And
    the ι⁺ data stop at the u-exponent 3 + ε_+ − ε (w_+ = 5 + ε_+, I10:47; I11:106-107). So the record keeps α − 4 ≤ ε_K
    < η_2 < ε_+.
  - *What caps ε_+.* 0 < ε_K < ε_+ < min(δ_♯, ε_ind) (I10:47 (1.1), J-PARAM:34), the ground LD3 already uses. With F2's
    ε_ind ≤ 2.932 × 10⁻⁶ at the record's point (the root 1 + 2.932 × 10⁻⁶; F2 (2.2), :133-136), α − 4 ≤ ε_K < 2.94 ×
    10⁻⁶ (α ≤ 4 + ε_K by I11:156), and below LD5's 3.1 × 10⁻⁵ at every admissible damping point. [D405, verifier 180:
    (2.2)'s least distance is printed at N1STAR-PROOF.md:4071-4072 as 7.3846 × 10⁻⁸ at the record's point, so
    ε_ind ≤ 7.4 × 10⁻⁸; the bounds here that use 2.932 × 10⁻⁶ are true and about 40 times loose.] [D420, verifier
    182: 7.3846 × 10⁻⁸ is δ_12, the value at the cutoff l ≤ 12 of that computation, not a minimum; δ_l → 0. D422:
    (2.2) ranges over |λ| ≤ 50, where the least distance is δ_50 = 1.94 × 10⁻⁸, so (1.1)'s ε_ind ≤ 1.94 × 10⁻⁸
    (LD10).] I11 Definition 1.3's
    (G) is a further constraint, which can only lower ε_K; whether it binds below ε_ind is not computed. ((1.1)'s ε_ind
    is III.G⁗ Proposition 5.1's (I10:48, I11:38), which is F′ (2.2)'s (G5:122, 190). VI4-PARAMS:38's row w1 read it as
    min Re ℰ^ι_ind, under which no number follows; that row now reads it as (1.1) does, D390.)
  - *Withdrawn.* D377 put the damping root λ^C − 1 into ℰ_ind, and so 3 + 2.93 × 10⁻⁶ into Λ. Nothing in the record says
    so. The ℰ_ind inside Λ is built from expansions of the gauge-potential operator □^Υ(0) (I8:35-36, I9:32-33,
    I10:38-40, I5:190; D3:33-48), whose indicial roots are not near 1 (verifier 174's B1).
  - *Consequence.* The β-chain's step α − 4 is bounded by ε_+, hence by F2's ε_ind: the constraint-damping gap of LD3
    (ii) and LD5. A fifth solve does not touch it.
  - *Open.* Lifting the cap would need all of the following relaxed: (1.1)'s ε_+ < min(δ_♯, ε_ind); the choice η_2 <
    ε_+; δ_♯, since 2λ_♯ = 3 + 2δ_♯ > 3 + ε_+ (I11:127); and (G), whose purpose is that the remainder 2 + ε_K is reached
    with 𝒩's rows alone (I11:434-438). Whether the cascade can run with ε_+ of order one while ε_ind stays small is not
    examined.

- LD8 (whether (G) binds below ε_ind, reduced; deduced from the record's text, D397). I11 Definition 1.3's (G) asks
  that no λ ∈ Λ have real part in (2, 2 + ε_K] ∪ (3, 3 + ε_K], and no λ + d_c0, λ + d_c1 in (2, 2 + ε_K]
  (I11:152-156).
  - *What (G) is.* Λ is discrete with finitely many elements in each bounded region (I11 Lemma 1.2 (a)). So (G) is
    exactly ε_K < δ_G, where δ_G > 0 is the least positive value of Re λ − 2 and Re λ − 3 over λ ∈ Λ, and of
    Re(λ + d_c) − 2 for c = c0, c1. "(G) binds below ε_ind" means δ_G < ε_ind.
  - *What cannot make it bind by itself.* Λ's generators of real part exactly 2 or 3 (the (2, 0) of 𝒢 := (2, 0) ∪
    (2 + ℰ_ind), I8:40, and 3) lie on the open ends of the windows. One translate of them by w ∈ π_1(ℰ_ind ∪ ℰ^ι_ind)
    has Re w ≥ ε_ind > ε_K (D3:44-48, I6:119), so it does not land in the window above the same integer; 2 + ℰ_ind
    likewise. Translates by 1 stay on integers. 2λ_♯ = 3 + 2δ_♯ (I11:127) is not in a window even if it is in Λ, as
    2δ_♯ > ε_+ > ε_K. At the record's point γ_Υ = e_Υ = 1/100 (N1STAR-PROOF.md:5457) this is λ_♯ = 1.5099 and
    δ_♯ = 0.0099, computed from G4:14's λ_♯ = 3/2 + (1 − e_Υ)γ_Υ.
  - *What could (corrected D402, verifier 179).* Λ is the smallest set containing its generators and closed under
    Λ + w ⊂ Λ for w ∈ π_1(ℰ_ind ∪ ℰ^ι_ind) ∪ {1} (I11:66-69, Definition 1.1). So its elements are the sums
    g + Σ n_i w_i, n_i ∈ ℕ₀, over its generators g: π_1(ℰ_++ ∪ 𝒢 ∪ ℰ^C_I), λ_♯, 3 and the column exponents
    2 + π_1 ℰ_col. The bound Re w ≥ ε_ind keeps a single translate out of the window above the same integer, but not a
    sum out of the window above the next one: 2 + w lies in (3, 3 + ε_K] when Re w ∈ (1, 1 + ε_K]. The distance
    d(Re λ, ℤ) ≥ ε_ind is stated for the single roots of F2 (2.2) (F2:130-131; D3:44-48), and for ℰ^ι_ind the record
    gives only min Re ≥ ε_ind (I6:119). [D538, verifier 232: I6:118-119 defines its own ε_ind := min Re ℰ^ι_ind, not
    (1.1)'s, so this citation does not give the inequality; it holds anyway, min Re ℰ^ι_ind ≥ d1 > δ_50 ≥ (1.1)'s ε_ind
    (LD14).]
 So two kinds of element remain, none computed as numbers at n = 4 in the
    record:
    - a sum g + Σ n_i w_i with real part in (2, 2 + ε_ind) ∪ (3, 3 + ε_ind), for any generator g. For g = λ_♯ this
      asks Re Σ n_i w_i within ε_ind above ½ − δ_♯ = 0.4901 (mod 1); for g = 2 and 3, within ε_ind above an
      integer. The other generators are the elements of ℰ_++ (I9:37-40, min Re ≥ λ_♯) and of ℰ^C_I (C2:257-259,
      min Re > 3/2 + 2γ_Υ, I11:110), and 2 + ℰ_col (I12:103-104, real parts ≥ 0), with the sums of each;
    - λ + d_c, c = c0, c1, with real part in (2, 2 + ε_ind), for λ ∈ π_1 ℳ = Λ ∩ {Re < 2} (I11:113), that is
      Re λ ∈ (2 − d_c, 2 − d_c + ε_ind) (corrected D405, verifier 180). Here d_c := −μ_c, and μ_c0 = 2 − λ^Υ_s0,2,
      μ_c1 = 2 − λ^Υ_s1,2 are themselves non-integer roots of F2 Proposition 2.3 (F2:106-110), so d_c ≥ ε_ind by
      (2.2) (I11:154-155 notes d_c > ε_K); and d_c0 ≤ z_Υ/3, d_c1 < ¼ (G2-IOTA:106-107, 117-118; I10-CORR4:72-73). So
      λ = 2 and Re λ ≥ 2 cannot bind, and neither can λ_♯ (λ_♯ + d_c < 1.76); what remains is an element of π_1 ℳ
      within d_c below 2: under ¼ in general, and under 1.34 × 10⁻⁶ at the record's point (d_c0 ≈ z/3, d_c1 ≈ z/12,
      z = 4 × 10⁻⁶; N1STAR-PROOF.md:3155, 4070). D402's two worked cases, d_c < ε_ind at λ = 2 and d_c near 0.4901 at
      λ_♯, are excluded by these bounds and are withdrawn.

    D397 listed four sources: sums from λ_♯, single elements of ℰ_++, ℰ^C_I and ℰ_col, and d_c at λ = 2 only. It
    missed the sums from the other generators, and λ + d_c for λ below 2. (Λ is also closed under conjugation, I11:64;
    harmless for real parts.)
  - *A near miss that is not in Λ.* The roots 2 + 2.93 × 10⁻⁶ of □^C at l = 2 (`checks/iota5.py`:44) would bind if
    they were in Λ. Nothing places them there: Λ's ℰ_ind is □^Υ(0)'s (verifier 174's B1), and ℰ_++ is required to
    contain only ℰ^♯_+ ∩ {Re < 2}.
  - So the open question of LD7 is reduced to these two kinds. Each needs the index sets at n = 4 as numbers, which
    the record has not computed, and then the sums over them up to real part 3 + ε_ind.

- LD9 (whether (G) binds, at two of the record's own roots; computed, conditional, D408; `checks/gapsums5.py`).
  - *What E_ind is (classes corrected D413, verifier 181).* Λ's increments are π_1(ℰ_ind ∪ ℰ^ι_ind) ∪ {1}. ℰ_ind is
    the index set of III.D″ Proposition 3.1 and III.F‴ Proposition 2.2 at b_0 (I5:190, I8:35). The classes differ by
    state (D3:141-147, I8:37-38): ω_s1 − ω̄_s1 and ω_v1 − V lie in 𝒜^((2,0) ∪ (2 + ℰ_ind)); the second s1 state and
    the mass state's gauge part ω̇(ḃ) lie in 𝒜^((1,0) ∪ (1 + ℰ_ind)); and the s0 state has ω_s0 − ω̄_s0 ∈ ρ²C^∞, with
    no non-integer exponent. Exponents are indicial roots plus integers (D4:52-60), the roots being the exponents of
    the components in the frame where dt̄ and d(rS) have root 0 (GAUGEPOT:195-199). The record bounds
    min Re ℰ_ind ≥ ε_ind and does not list the exponents.
  - *Two of them.* □^Υ(0)'s s0 and s1 roots through 2 are λ_s0 = (1 + (9 + 4z)^(1/2))/2 and λ_s1,2 = (1 + (17 + 2z −
    2(z² + 4z + 16)^(1/2))^(1/2))/2 (III.D (4.1); N1STAR-PROOF.md:4575-4576). Their offsets above 2 are
    d0 = 1.3333327 × 10⁻⁶ ≈ z/3 and d1 = 3.3333305 × 10⁻⁷ ≈ z/12 at z = 4 × 10⁻⁶. d0 − 4d1 = 5.56 × 10⁻¹³ = O(z²):
    the two are nearly commensurate.
    - A ρ^(2+d1) term in ω_s1 − ω̄_s1 (class 2 + ℰ_ind) puts d1 into ℰ_ind.
    - A ρ^(2+d0) term in ω̇(ḃ) (class 1 + ℰ_ind) puts 1 + d0 into ℰ_ind, not d0. D408 read it as d0, which needs a
      state in a 2 + ℰ_ind class carrying ρ^(2+d0), and none cited does.
  - *Only offsets with integer part 0 can be stacked.* The windows of (G) lie above 2 and 3, and the generators that
    reach them have real part ≥ 3/2. So an increment with integer part ≥ 1 can be used at most once there, and only
    increments in (0, 1) can be summed many times. Of the computed roots, only d1 is one: the sl roots
    λ_sl,l+1 = l + 1 + δ_l and λ_sl,l+2 = l + 2 + δ′_l (GAUGEPOT:193-194, 204-211) enter a 2 + ℰ_ind class as
    (l − 1) + δ_l and l + δ′_l, and the mass state's root as 1 + d0, as above. At most one increment with integer part
    ≥ 1 fits in any one sum, and from the generator 2 only δ_2 or δ′_1 does (D420, verifier 182).
  - *(G)'s third window* (LD8), λ + d_c in (2, 2 + ε_K] for λ ∈ π_1 ℳ below 2, takes d_c0 = d0 once without d0 being
    in ℰ_ind. With λ = λ_♯ + n d1 the least value above 2 is 2 + 2.45 × 10⁻⁷, for d_c = d0 and d1 alike
    (`checks/gapsums5.py` G6, D420, verifier 182). So the bound below stands.
  - *If ℰ_ind contains d1 and 1 + d0* (`checks/gapsums5.py` G4-G5, D413), with the increment 1: the least value above
    2 or 3 is 3 + 1.39 × 10⁻⁷ from the generator 2, and 3 + 5.02 × 10⁻⁸ from λ_♯, both reached with d1 alone. So
    δ_G ≤ 5.0 × 10⁻⁸. D4:54-57 fixes ε_ind below half the least distance between distinct points of ℳ, which is
    2.92 × 10⁻¹⁰ under the reading LD10 fixes, so ε_ind < 1.46 × 10⁻¹⁰, more than 300 times below 5.0 × 10⁻⁸. That is the
    gauge potential's ε_ind; against (1.1)'s, F′ (2.2)'s, ε_ind ≤ 1.94 × 10⁻⁸ (LD10, D422), the margin is about 2.6
    (D429, verifier 183). So (G)
    is not shown to bind below ε_ind. It may still bind, since 5.0 × 10⁻⁸ only bounds δ_G from above. (Corrected
    D420, verifier 182: D413 compared with 7.38 × 10⁻⁸ and 3.7 × 10⁻⁸, but 7.38 × 10⁻⁸ is δ_12, not that distance.)
  - *If ℰ_ind contained d0 and d1* (D408's hypothesis, which no cited state supports; G2-G3), then
    2 + n0 d0 + n1 d1 ∈ Λ for all n0, n1 ≥ 0, the least such value above 3 would be 3 + 4.68 × 10⁻¹³, at
    (n0, n1) = (350001, 1599998), and from λ_♯ 2 + 5.10 × 10⁻¹³. D408's δ_G ≤ 4.7 × 10⁻¹³, and with it ε_K < 4.7 ×
    10⁻¹³ and K > 4 × 10¹², rest on that hypothesis and are withdrawn as consequences of the record.
  - *Controls.* With d0 alone the least gap is 8.9 × 10⁻⁷; with d1 alone 1.39 × 10⁻⁷ (G4 is that value). It is the
    near-commensurability d0 ≈ 4d1 that brought D408's sums close, and it needs both offsets stackable.
  - *Every computed root at once (D430; `checks/gapsums5.py` G7, exact, 50 digits).* From the generators 2, 3 and λ_♯,
    with d1 summed freely and at most one of 1, 1 + d0, 1 + δ_2 and 1 + δ′_1 (δ_2 = 2.6666653 × 10⁻⁷ ≈ z/15,
    δ′_1 = 6.0000008 × 10⁻⁷ ≈ 3z/20; δ_1 = d1 to 40 digits; every other computed root has integer part ≥ 2 and
    overshoots both windows), the least value above 2 or 3 is still 3 + 5.02 × 10⁻⁸, from λ_♯ + 4,470,304 d1. Check:
    without the two sl offsets it reproduces G4-G5's minimum (a consistency check, not a control: the sl offsets, forced
    once, give no less than 1.78 × 10⁻⁷; verifier 185, D433). Admitting also the reflected residues 1 − d0, 1 − δ_l and 1
    − δ′_l of D4:54-58's ℳ, one at a time for l ≤ 3000 (verifier 185's probe, not in the script), the least value is 2.65
    × 10⁻⁸, still above 1.94 × 10⁻⁸. The third window gives 2.45 × 10⁻⁷ (G6).
    - So the computed roots do not make (G) bind: from them δ_G = 5.02 × 10⁻⁸, above ε_ind ≤ 1.94 × 10⁻⁸ > ε_K, and
      the binding constraint on ε_K is ε_ind (LD10), with K > 1.03 × 10⁸; (G) from these roots alone would give only
      K > 2/δ_G = 4.0 × 10⁷.
    - (G) can still bind through Definition 1.1's generators the record does not list (π_1 ℰ_++, 𝒢, ℰ^C_I,
      2 + π_1 ℰ_col and the increments of ℰ^ι_ind; I11:66-71): each adds bases, and every base adds a residue below d1.
  - *Not decided.* Whether the coefficient of ρ^(2+d1) is nonzero, so that ℰ_ind contains d1 (the record keeps ℰ_ind as a
    bound; at every cut-off computed it is nonzero, D442, D450), and δ_G over the unlisted generators. The sl offsets are
    δ_l = z l/(2(l + 1)(2l + 1)) + O(z²) and δ′_l = (l + 2)z/(2(l + 1)(2l + 3)) + O(z²) (GAUGEPOT:194 prints δ′_l; both
    follow from ∂_z s_l,j = (s − κ)/(2s − 2 − 2κ − z) on Q_l's roots). Entering with integer parts l − 1 and l, at most
    one of them fits in a sum. That adds shifts to d1's multiples and could lower the bound below 5.0 × 10⁻⁸ [computed,
    D430: it does not], but it cannot bring the O(z²) parts into play. (D408 said "if they all enter, δ_G is set by the
    O(z²) parts"; withdrawn, D413.)
  - *The local expansion does not decide it (D412; `checks/s1reson5.py`, exact).* The s1 state is dx¹ + w. On
    Tangherlini, □^Υ(dx¹) starts at ρ⁴, which is the order resonant with the root 2 + d1:
    F4 = μ(−2γ_Υ(e_Υ + 2), −3, 1) on (dt, dr, dχ).
    - The flat indicial matrix on the l = 1 harmonic has det I(λ) = λ(λ − 4) q(λ), with q's root λ_s1,2, and
      det I(2) = 16 e_Υ γ_Υ² = 4z.
    - At γ_Υ = 0 (z → 0 at fixed e_Υ) the left null vector (0, 1, 3) of I(2) annihilates F4, so along that branch
      the forcing is not resonant and the particular solution μ(0, ¼ − 1/e_Υ, −¼ − 1/e_Υ) stays finite. Along
      e_Υ → 0 at fixed γ_Υ the null vector is (−2γ_Υ/9, 1/3, 1), its pairing with F4 is 8γ_Υ²μ/9 ≠ 0, and the
      particular solution is O(1/e_Υ) = O(4γ_Υ²/z): that is why it is about −100μ at the record's point (qualified
      D420, verifier 182). Control: a forcing with nonzero pairing with (0, 1, 3) gives a particular solution of order
      1/z.
    - So the coefficient of ρ^(2+d1) is that of the homogeneous decaying solution, fixed by regularity at the horizon:
      a global question, not a local one.
    - Computed (D442; `checks/s1coef5.py` S1-S5): the s1 system solved from the horizon at z = 1/2 and z = 1/8 (d1 =
      0.0375 and 0.0101), μ = 1, γ_Υ,H = 1/10, c_Υ = ζ r⁻¹ dt (ζ = 0 near the horizon, one admissible choice as dt is
      singular there, smoothness needing only ζ = O(r − 1), and 1 for r ≥ 2.5) and c_Υ,H = −½η dr (η = 1 near the
      horizon, 0 for r ≥ 1.8), in ingoing coordinates. The ODEs reproduce genstates5's operator in static coordinates.
      The solutions smooth at the horizon are three power series: its exponents are 0 four times, 1 and −1, the 1 handled
      as a resonance. At infinity the state is u_0 + A u_(2+d1) + B3 u_λ3 + B4 u_4, u_0 the series from dx¹ with the
      logarithm the roots 0 and 4 force, the others with unit leading vectors. A agrees to ten digits over two matching
      radii and a second run with another starting radius and tolerance; verifier 190 reproduced it by Chebyshev
      collocation, with its own derivation of the operator (η term included), to nine digits (D443).
    - A = 2.584 at z = 1/2 (γ_Υ = e_Υ = 1/2) and 2.662 at z = 1/8 reached along γ_Υ → 0 (γ_Υ = 1/4, e_Υ = 1/2); at z =
      1/8 reached along e_Υ → 0 (γ_Υ = 1/2, e_Υ = 1/8) it is 10.99, about four times larger, consistent with the local
      picture above (there the near-resonant particular solution grows like 1/e_Υ). Two points on each branch at most;
      the record's point is the next bullet, and whether these γ_Υ, e_Υ, γ_Υ,H meet III.D′ Proposition 4.1's ε_0, ε_1 is
      not checked (D443).
    - *At the record's point (D450-D451; `checks/s1coef5.py --record`, S6, computed).* γ_Υ = e_Υ = 1/100, z = 4 × 10⁻⁶,
      d1 = 3.3 × 10⁻⁷: A = 141.4269, the same to ten digits at both matching radii and the second start (condition up to
      10⁵), and reproduced to 10⁻⁹ by verifier 194's Chebyshev collocation from the horizon. It is large because of the
      near-resonance: u_0's ρ² coefficient there is (0, −99.75, −100.25), D412's particular solution, with component P_v
      = −141.4214 along ρ^(2+d1)'s unit vector v, and the near-resonance forces A = −P_v + O(1). Near I_0 the state
      carries A (ρ^(2+d1) − ρ²) ≈ A d1 ρ² log ρ plus the ρ² vector A v + c_2 = (0.0133, 0.2473, −0.2395), of norm 0.345,
      close to D412's finite part (0, ¼, −¼) and so nearly orthogonal to v: its component along v, A + P_v = 0.0055, is
      small for that reason, not forced (along the branch it is −0.016 to 0.014 and changes sign between γ_Υ = e_Υ = 1/30
      and 1/100; at D442's points −0.16 to −0.31; verifier 194, D451). So d1 ∈ ℰ_ind at the record's point too, with
      coefficient about 141 for these cut-offs. The cut-offs move A by 7 × 10⁻⁶ (ζ's interval), 1.9 × 10⁻³ (a ζ bump of
      20) and 0.17 (an η bump of 20, through the horizon term γ_Υ,H η): small against A, not against A + P_v, which the η
      bump moves 32-fold. A second near-cancellation sits at ρ⁴. Not checked: whether these parameters meet III.D′
      Proposition 4.1's ε_0, ε_1, and whether any of the record's estimates bounds the ρ^(2+d1) and ρ² pieces separately.
  - *The global problem depends on choices the record leaves open (D415, deduced).* The s1 state solves □^Υ_b ω = 0
    and is smooth on X (D4:109-111), so its ρ^(2+d1) coefficient depends on □^Υ_b everywhere, not only near infinity.
    The record fixes c_Υ only near infinity: c_Υ = ζ(|x|)|x|⁻¹ dt with ζ = 1 for large |x|, and c_Υ,H = −½χ(|x|) d|x|
    with χ supported in {|x| < 5R_1} (III.B Definition 6.1, B-FAMILY:430-432; D3:31-33).
    - Changing ζ or χ on a compact set changes □^Υ_b = 2(δ + E^Υ)Gδ* by the compactly supported first-order term
      2(δE^Υ)Gδ*, since E^Υ is algebraic in c. The state changes by the decaying solution of □^Υ_b δω = −2(δE^Υ)Gδ*ω,
      whose ρ^(2+d1) coefficient is the pairing of that source with the dual state of the root 2 + d1.
    - That pairing is an integral against δζ (or δχ). It vanishes for every variation only if its integrand vanishes
      identically, which nothing in the record forces.
    - So whether d1 ∈ ℰ_ind is a property of the cut-offs, not of the record. The dependence is computed (D442; it had
      been asserted, D429): over 22 rows of choices of ζ and η (transition intervals moved, compactly supported bumps of
      amplitude up to 100 added to ζ on [1.6, 2.4] or [2.55, 2.95], or to η near the horizon; three rows repeat the
      baseline), A changes with every one that differs from the baseline: by up to 1.60 from it at z = 1/2, a spread of
      1.75 (D443). It stays positive throughout (from 0.98 to 2.74 at z = 1/2, 1.25 to 2.82 and 6.6 to 11.2 at the two z
      = 1/8 points). A ζ solving the one real equation A = 0 would remove this state's term (one for all S ∈ 𝒮_1, as ζ
      and χ are rotation invariant), but none was found in these families.
    - For the loss d: the record keeps ℰ_ind as a bound valid for its choices, so LD9's δ_G ≤ 5.0 × 10⁻⁸ is the one to
      carry unless ζ is chosen to exclude d1. At every cut-off computed (D442, D450; z = 1/2, 1/8 and the record's point)
      the state carries d1.
    - *Whether a cut-off makes A vanish at the record's point (D457; `checks/s1coef5.py --zeros`, S7, computed).* Every
      variation supported in (1.25, 3), between the horizon series and the matching radius. The pairing with the dual
      state, measured by unit bumps: dA/dζ from −1.0 × 10⁻⁵ to −3.1 × 10⁻⁵ and dA/dη from 0.034 to 0.061 per unit
      integral, curvature at most 10⁻⁴; their Riemann sum, 0.084, estimates to first order how far cut-offs within 1 of
      the baseline move A (an estimate, not a bound: it leaves out (1.25, 1.3) and (2.9, 3), and η0 − 1 there moves A by
      −0.098; verifier 196, D459); the extreme cut-offs valued in [0, 1] give A from 141.4177 to 141.4938. Along ζ0 + t b
      and η0 + t b, b the most sensitive bump, A stays in [123.95, 141.43] at the sampled |t| ≤ 10⁵ (ζ; between samples
      it dips further, 121.42 at t = 1.5 × 10⁴, D459) and in [140.24, 141.94] at the sampled −100 ≤ t ≤ 10⁵ (η), each
      value the same at matching radii 3 and 4; for η at t ≤ −1000 the matching degenerates (condition above 10¹²: 2 ×
      10¹⁴ at t = −1000, where the two radii still agree, and they disagree from −10⁴) and A was not decided there;
      matching with the horizon columns re-orthonormalised decides it, A = 130.27 to 130.48 from t = −10³ to −10⁵ (D472).
      No zero was found: A is pinned by the near-resonance's −P_v = 141.42, and the cut-offs move only the rest, by about
      20 at most even at amplitude 10⁴ on the samples. So for the cut-offs computed, and to first order for any within 1
      of the record's on (1.25, 3) (not proved), d1 ∈ ℰ_ind and LD9's δ_G is the one to carry. That 'no zero' holds at
      the samples only: inside r = 1.25 A does vanish, at bump amplitudes of order 10³ and 10⁴ between the samples
      (D482), and Definition 6.1 (III.B) bounds neither c_Υ nor c_Υ,H in size, so those cut-offs are admissible to it
      (other Parts' conditions not checked). So d1 ∈ ℰ_ind at the record's cut-offs and near them, not for every
      admissible cut-off (D483: the zeros found sit beside poles, at amplitudes from 1640 inside r = 1.25, and none at r
      ≥ 2.45 to amplitude 10⁵).
    - *Beyond r = 3 (D465; `checks/s1coef5.py --zeros-far`, S8, computed).* Matched at r = 8 (A0 the same to ten
      digits), dA/dζ falls outward, from −2.7 × 10⁻⁵ at r = 3.2 to −1.2 × 10⁻⁵ at 7.6, but dA/dη levels off near 0.068
      per unit integral (0.063 at 3.2, 0.068 at 7.6): c_Υ,H = −½η dr carries no decay, so to first order an η within 1 of
      the record's moves A by about 0.07 per unit of support. The record confines χ to |x| < 5R_1 (III.B Definition 6.1),
      and R_1 = √μ_end = 1 in these units (BEYOND5, r_0 = ½R_1), so over its whole support (1.25, 5) an η within 1 moves
      A by about 0.22 to first order: 0.130 on (3, 5), S7's η-only 0.084 on (1.3, 2.9), and 0.0015 and 0.0062 on the gaps
      (1.25, 1.3) and (2.9, 3) that neither scan samples (D468; D465's 0.21 used S7's joint ζ + η sum and left the gaps
      out, verifier 199). A ζ within 1 on (3, 8) moves it by 9 × 10⁻⁵, but dA/dζ falls only like r^(−0.92), so on (3, R)
      ζ's first-order effect grows like log R (about 10⁻⁴ ln(R/3)), and as the record fixes ζ only for large |x|, (3, 8)
      is a choice, not its bound. Both are far from the 141.4 the near-resonance forces, at first order: no curvature is
      computed beyond r = 3.
    - *Beyond first order (D472; `checks/s1coef5.py --zeros-far-amp`, S9, computed).* The extreme cut-offs valued in [0,
      1] that the record's support allows (η switching off as late as [4.75, 4.95], ζ on as late as [7.5, 7.8], and both)
      move A by +0.168, +6.5 × 10⁻⁵ and +0.168. Along η0 + t b (b at r = 4.8) and ζ0 + t b (r = 3.2), at the sampled |t|
      from 1 to 10⁵, A is in [107.42, 141.97] and [120.47, 141.43] (between samples it can dip lower: 119.208 for ζ at t
      = 1.3 × 10⁴, verifier 202). Where the plain matching fails (for η at t ≤ −10³, one horizon solution outgrows the
      others across the bump), the horizon columns are re-orthonormalised at every step of a grid, which A, a coefficient
      of an infinity column, does not see; that matching agrees with the plain one to twelve digits where both hold, and
      with itself at a second radius and half the step size to 10⁻⁷ (and with independent DOP853, LSODA and Radau
      integrations to 5 × 10⁻⁸, verifier 202). Every value is reliable, the least is 107.418, and A changes sign at none
      of the samples: the −166 the plain matching gave at t = −3 × 10⁴ was its failure. So beyond r = 3, to the record's
      support and well past amplitude 1, no cut-off computed makes A vanish.
    - *Inside r = 1.25 (D479; `checks/s1coef5.py --zeros-near`, S10, computed).* Started at r = 1.05, where the horizon
      series still converges (A0 the same to ten digits as from 1.25, and at matching radii 3 and 4), the cut-offs can be
      varied on (1.05, 1.25): bumps of half-width 0.025 give dA/dη = 0.011 to 0.025 and dA/dζ about −5 × 10⁻⁶, so a
      cut-off within 1 of the record's there moves A by 0.0037 (η) and 1.2 × 10⁻⁶ (ζ) to first order; along η0 + t b and
      ζ0 + t b at r = 1.225, |t| from 1 to 10⁵, A stays in [140.34, 141.96] (QR matching where the plain one fails, every
      value reliable) at the sampled amplitudes; but between the samples A has real poles and zeros in t, and vanishes
      for η at t = −1642.825 and for ζ at t = −14570.834 (verifier 205, D482): the claim of no sign change there is
      withdrawn, and the families are scanned densely below (D483).
    - *Dense in amplitude (D483, corrected D498; `checks/s1coef5.py --zeros-dense`, S11, computed).* A pole of A in a
      family is a zero of the matching determinant det[H | −I_1 −I_2 −I_3], which is smooth in t, so poles are located
      by its sign (match_det; with the horizon columns re-orthonormalised at each step, R's diagonal kept positive, the
      sign is the plain matching's), each refined by bisection, and the zero of A beside each pole by A's own sign; a
      zero with no pole beside it shows as a change in A's sign alone when it is the only one in its step. Sampling A
      misses such pairs, since A returns to the same sign on both sides of a simple pole with a zero beside it. On t =
      ±10^k, k ∈ [0, 5], 30 amplitudes per decade (20 for the far η family), every value reliable by S11's test (finite,
      with condition below 10¹² at one radius; S9-S10's second radius is not used, and an unreliable point would drop
      both steps beside it; the runs have none): inside r = 1.25 (half-width 0.025 at r = 1.225, started at 1.05) η has
      one pole, at t = −1640.954, with its zero at −1642.825, and ζ four, at t = 1946.632, −1946.977, 14562.909 and
      −14558.973, with zeros at 1943.638, −1943.977, 14574.511 and −14570.834 (D482's two zeros among them). The ζ pairs
      are nearly symmetric in t because A is nearly even in t there: its odd part is −2.2 × 10⁻⁷t up to |t| = 10³, not
      small beside the second-order coefficient (1.15 × 10⁻⁷), so this is not the first-order effect D483 named, and
      from |t| = 10⁴ the expansion fails (D498). At r = 2.85 (η) and 2.45 (ζ), half-width 0.1, matched at 3 and 4, and
      at r = 4.8 (η) and 3.2 (ζ), half-width 0.2, matched at 8 and 10: no pole and no zero. Each pole is simple, A ≈
      c/(t − t_p) with c = 263.4 (η) and 424.5, −425.2, −1641 and 1678 (ζ), and each zero lies at −c/A_reg from its
      pole, within 0.2 % in t. The matching's condition number falls like 1/|t − t_p|: 1.5 × 10¹³ plain and 2.4 × 10⁹
      re-orthonormalised at t = −1640.954, 2 × 10⁻⁴ from the pole; 1.5 × 10⁹ plain at η's zero, and 2.5 × 10⁵ and 6.8 ×
      10⁷ at the ζ zeros 1943.638 and 14574.511 (D483's 10¹⁸ was its value at the bisected pole itself, where the matrix
      is singular by construction). A sign change shows an odd number of zeros in a step, so two poles in one step (8 %
      in t at 30 per decade, 12 % at 20), two zeros of A in one step with no pole, a determinant zero of even
      multiplicity, or a second zero beside a pole (the search finds one per side) would be missed, and |t| < 1 is not
      scanned (the first-order analysis covers it); 'none' is for this grid. Reproduced independently (verifier 210,
      D498): every pole and zero to the printed digits by another matching (horizon columns integrated outward with its
      own re-orthonormalisation, infinity columns inward, matched at r = 1.25), and at 150 to 200 amplitudes per decade
      the same determinant sign changes in the same brackets and none elsewhere. So, on these grids, A vanishes only
      beside a pole, a zero-energy state of the s1 sector, at bump amplitudes from 1640 up, concentrated inside r = 1.25
      (one bump position per region for each cut-off); in every family scanned, amplitudes below 1640 give neither.
    - Not computed: variations inside r = 1.05, where the horizon series itself assumes ζ = O(r − 1) and η = 1, cut-offs
      that are not rotation invariant (the record's are), and the dual state as a function rather than through its
      pairings.

- LD10 (ε_ind as D4 defines it; computed, D420 after verifier 182; `checks/epsind5.py` E1-E2, exact).
  - *The definition.* D4:54-57 lets ℳ be "the finite set of real numbers in [−10, 10] of the form Re λ + j", λ an
    indicial root of □^Υ (GAUGEPOT Lemma 4.1), j ∈ ℤ, and fixes ε_ind below half the least distance between distinct
    points of ℳ. F4:25-27 and D3:44-45 define it instead as below d(Re λ, ℤ) over the same window, which E2 puts at 9.47
    × 10⁻⁸: the record holds both definitions (D429, verifier 183).
  - *E1, read literally it is empty.* The sl roots l + 1 + δ_l have δ_l = zl/(2(l + 1)(2l + 1)) + O(z²) → 0:
    3.3 × 10⁻⁷ at l = 1, 7.38 × 10⁻⁸ at l = 12, 9.9 × 10⁻⁹ at l = 100. So over every l, ℳ is not finite, its points
    accumulate at the integers, and no ε_ind > 0 exists. The record's 7.3846 × 10⁻⁸ (N1STAR-PROOF.md:4069-4072,
    used in D405 and D413) is δ_12, the value at the cutoff l ≤ 12 of that computation, not a minimum.
  - *E2, the finite reading* (roots with real part in [−10, 10], so l ≤ 9). There are 35 distinct fractional parts.
    - The least distance between distinct points of ℳ is 2.92 × 10⁻¹⁰, between the mirrors 1 − λ of λ_s8,2 and λ_s7,1
      (epsind5 prints s8,2−, s7,1−; δ_7 against
      δ′_8), so ε_ind < 1.46 × 10⁻¹⁰.
    - The least distance of a point from ℤ is δ_9 = 9.47 × 10⁻⁸.
    - Control: at z = 0 every root is an integer.
  - *Which ε_ind, read at source (D422).* The record has two.
    - The gauge potential's is fixed in III.D″ section 1 "less than d(Re λ, ℤ) for every indicial root λ of
      □^Υ_b(0) with non-integer real part of modulus at most 10" (F4:25-27, D3:44-45; D4:54-57 refines it). This
      settles D4's reading as the finite one, and that ε_ind is below 9.47 × 10⁻⁸ by F4's distance from ℤ and below 1.46
      × 10⁻¹⁰ by D4's refinement (E2). It bounds ℰ_ind's real parts.
    - F4:27 calls it "the gauge potential operator's number, not that of III.F′ (2.2)". (2.2) asks d(Re λ, ℤ) ≥ ε_ind
      "for every non-integer root λ with |λ| ≤ 50" of L̂_b(0) (F2:130-132).
    - (1.1)'s ε_ind is III.G⁗ Proposition 5.1's (I10:48), which is III.F′ Proposition 2.3 (f)'s (G5:122, 190): the (2.2)
      one.
  - *E3, (2.2) at the record's point.* By lin5.py E2's factorisation, det N(L, λ) = det N(□^Υ, λ − 1) det N(□^C, λ + 1)
    times factors with integer roots, divided by D, which has integer roots; so every □^Υ root plus 1 with non-integer
    real part is a root of L̂_b(0). Over those with |λ| ≤ 50 the least distance from ℤ is δ_50 = 1.94 × 10⁻⁸, at
    λ = −49 − δ_50. Over l ≤ 12 it is 7.3846 × 10⁻⁸, the record's number. So the record computed (2.2) on l ≤ 12
    (lin5.py's LMAX = 12) while (2.2) ranges over |λ| ≤ 50. □^C's roots can only lower the minimum further.
  - *Consequences.* ε_K < ε_+ < ε_ind ≤ 1.94 × 10⁻⁸. LD3's chain has K > 2/ε_K > 1.03 × 10⁸ levels, and the d it
    produces is at least 2K > 2.06 × 10⁸. This replaces D420's two readings (K > 1.3 × 10¹⁰ if (1.1)'s ε_ind were D4's,
    as 2/(1.462 × 10⁻¹⁰) = 1.37 × 10¹⁰, printed 1.4 there,
    K > 2.1 × 10⁷ with the window |Re λ| ≤ 10). The gap condition (G) is not the binding constraint (LD9).
  - *For the record.* The same δ_l → 0 makes any condition d(Re λ, ℤ) ≥ ε_ind for all roots unsatisfiable without a
    bound on l, which does not bear on F2 (2.2), whose roots are bounded by |λ| ≤ 50 (F2:130-132; corrected D429). A
    reading that bounds l (the real-part window, or l ≤ 12 as
    N1STAR-PROOF.md computed) has to be fixed for D4's definition to make sense. Recorded, not repaired.

- LD11 (LD3 (ii)'s condition settled: each level-3 round costs a derivative; deduced from the record's text, D507,
  corrected D509 after verifier 218). LD3 (ii) left open whether a round of I14's level-3 loop costs a derivative. The
  record's own accounting says it does. (i) The rounds compose: "While the tf-weight τ of the current level-3 source is
  at most β − 2, apply III.G⁗ Proposition 5.1 … Each round leaves a remainder of tf-weight τ + ε_ind − ε"
  (PART-III-I14-LEVELS.md:121-128; the same loop at α, PART-III-I12-SPECTRAL.md:287-298); Proposition 5.1's remainder is
  f − L̂_b(σ)u (PART-III-G5*:631), built from its solution, not from the source's expansion (at β < 4, k_0 = 0 and the
  zf-sum is empty, G5:648-655), and it is the next round's source. (ii) A round has loss at least 2: its remainder is
  formed in Proposition 5.1's proof by second-order b-operators applied to u_1 = N_tf⁻¹(|σ|^(−α)f_1) (G5:694, 713-715;
  L̂_b − L̂-bar ∈ ρ²_scf ρ⁴_tf Diff²_b, G5:18-19), which III.J″ charges loss 2 (J3:118-121, 164), and N_tf⁻¹ costs
  Corollary 3.4's ℓ ∈ ℕ_0 (J3:167-168, F2:466), so 2 + ℓ by Lemma 1.2 (a)-(b). [D507 cited instead J3:168-169's "compose
  it with L̃_b(0)⁻¹"; G5 applies no such inverse (it cites III.H nowhere, and its Remark 4.5 says the zero-energy
  operator is not inverted in this range), the zero-energy inverse being I12 Lemma 2.1's, once per level after the rounds
  (I12:110-112, 299) and omitted at β < 4 (I14:120-121): J3's sentence misdescribes G5.] (iii) III.J″ sums the losses
  over a composition: Theorem 4.1 gives "a loss d equal to the sum of the losses" (J3:288-293), and J3 (g)'s "finitely
  many rounds whose number is fixed by the weights (each raises the order by at least ε_ind − ε): fixed loss" means a
  loss independent of k (J3:157-158), proved by Lemma 1.2 (e) (J3:192-194), so N rounds cost N times one. So the d of
  III.J″'s accounting is at least twice the total number of level-3 rounds. At a level β ∈ (3, 4 + ε_K] the loop runs
  from τ_3 = 1 + η_2 − 2ε to β − 2 in steps ε_ind − ε, about (β − 3)/ε_ind rounds; the β-chain has a level in every
  interval of length α − 4 ≤ ε_K (I15:323-324), so over (3, 4] the rounds total about ½/(ε_K ε_ind), and with ε_K < ε_+ <
  ε_ind ≤ δ_50 = 1.94137 × 10⁻⁸ (LD7, LD10) that is more than 1.32 × 10¹⁵ (a direct sum gives 1.3266 × 10¹⁵, verifier
  218). So d > 2.6 × 10¹⁵ by the loss 2 per round (d > 1.32 × 10¹⁵ counting one), against 2.06 × 10⁸ in LD3 (iv), and N =
  21d + 6 > 2.78 × 10¹⁶ already at d > 1.32 × 10¹⁵. A floor: a finer accounting might charge less (the remainder's
  leading part sees u_1 only through finitely many coefficients, G5:705-706, 712), which is the optimal-loss question. As
  in LD3 (iii), it bounds what this proof's accounting delivers, not the optimal loss. The per-level count is set by the
  round's step ε_ind − ε (LD10), the number of levels by the β-chain's step α − 4 ≤ ε_K < ε_+ < ε_ind (LD7); raising
  ε_ind relaxes both caps, a longer level step (LD3 (iii)) the second.

- LD12 (a second long loop, at the β-levels below 3; deduced from the record's text, D514). LD3 (ii) and LD11 count the
  level-3 rounds at the β-levels in (3, 4 + ε_K]. The levels below 3 run a loop of the same size. (i) I15 Step 2 applies
  III.I′′′′′′′′ Lemma 3.2 at every level below 3: "For β_(k+1) < 3, III.I′′′′′′′′ Lemma 3.2 (transferred to P_4 as in
  Step 1, with β_(k+1) − β_k < a_K − 2) applied to u gives (3.4)" (PART-III-I15-AUGMENT5.md:346-348); the levels are
  spaced below α − 4 ≤ ε_K there as everywhere (I15:323-324). (ii) Lemma 3.2's Step 3 makes the source f̂_5 afresh at
  each call, of tf-weight τ_0 := 2 + ε_ind − 2ε (PART-III-I9-COMMOTION.md:276-282, from III.I′′′′′′ (2.7)), and its Step
  3.4′ is a tf-iteration: while τ_i ≤ α − ε′ it applies III.G⁗ Proposition 5.1, and f̂^(i+1) := f̂^(i) − σ L̂_b(σ) v_i
  has tf-weight τ_(i+1) := τ_i + ε_ind − ε (I9:284-301). So the level α runs i_0 ≥ (α − ε′ − τ_0)/(ε_ind − ε) rounds, a
  count no index set enters. (iii) The rounds compose, each remainder being the next round's source and built from the
  solution v_i, and each is Proposition 5.1 with N_tf⁻¹; so by LD11 (ii) each costs at least 2 in III.J″'s accounting.
  (iv) The levels in (α_1, 3), with α_1 < α − 2 ≤ 2 + ε_K (I15:305), number at least about 1/ε_K. Over them the rounds
  total about ½/(ε_K ε_ind), as in LD11 (iii) with β − 2 for β − 3, again more than 1.32 × 10¹⁵ since ε_K < ε_+ < ε_ind
  ≤ δ_50. So the β-chain runs more than 2.65 × 10¹⁵ rounds of Proposition 5.1: d > 5.3 × 10¹⁵ (d > 2.65 × 10¹⁵ counting
  one per round), and N = 21d + 6 > 1.11 × 10¹⁷. As LD3 (iii), these bound what the record's proof delivers, not the
  optimal loss. (v) Toward an upper estimate (not made). The per-round loss is 2 + ℓ, with ℓ III.F′ Corollary 3.4's, a
  fixed integer from II.G′ Lemma 4.1's closed forms (section 2's table). Most of the other loops are short. The α-levels
  of III.I′′′′′′′′ step below a_K − 2 (I9:374-375), and a_K ≥ 4 + ε_K (I15:332), so there are finitely many,
  independently of ε_K. III.I′′′′′′′′′′′ Step 4 runs about 1/ε_ind rounds, once (I12:287-298). Two loops have a length
  that depends on the index sets. The first is the level-2 rounds of III.I′′′′′′′′′′′ Step 3 and of their repetition at
  every β-level above 3: "its remainder exponents α_0 + E_ind may again lie below 2 + η_2, and are treated in turn
  (finitely many rounds, the real parts rising by ≥ ε_ind)" (I12:278-281). That is about (1 + η_2 − η_1)/ε_ind rounds
  per chain, one chain for each tf-exponent of g_2 in the window, and the chains can interleave (corrected D516,
  verifier 221); so of order 1/(ε_K ε_ind) or more over the β-chain if the smallest element of E_ind is about ε_ind. The
  second is the ι⁺ iteration of III.I′′′′′ Proposition 2.1, which Lemma 3.2's Steps 1-2 run at every level below 3
  (I9:230, 256-257; PART-III-I6-ALMOSTBDD.md:167-172; J3:261, "exponents in a window"), up to about (2 − λ_♯)/ε_ind
  rounds per level; it is not counted here. D514 had named III.I′′′′′′ Steps 3-3.3, whose row (J3:262) has count 1
  (corrected D516). So the record's d at its best admissible weights is at least about 2(½ + ½)/(ε_K ε_ind). Each of
  those two loops can add a term of the same order, 1/(ε_K ε_ind): the ι⁺ rounds up to about (2 − λ_♯)/(ε_K ε_ind) over
  the levels below 3. E1'c's number needs them counted. [Corrected D534: the ι⁺ loop's step is I6's own ε_ind := min Re
  ℰ^ι_ind (PART-III-I6-ALMOSTBDD.md:118-119, "not (1.1)'s"), not (1.1)'s ε_ind, so its order is not fixed by 1/(ε_K
  ε_ind); see LD14.]
- LD13 (the level-2 loop's length, from ℰ_ind's least elements; computed, conditional, D529; `checks/level2loop5.py`
  L1-L4, exact). LD12 (v) left the level-2 rounds of III.I′′′′′′′′′′′ Step 3 of order 1/(ε_K ε_ind) "if the smallest
  element of E_ind is about ε_ind". At the record's point it is not, on LD9's reading of ℰ_ind, and each of its chains
  is then shorter than a β-level's level-3 rounds; on a broader reading it is far longer. (Corrected D531, verifier 229:
  the loop as a whole is N_2 times a chain, N_2 the number of g_2's tf-exponents in the window, which the record does
  not bound, so it is shorter than the counted loops only while N_2, with the log orders, stays below about 8.6.)
  - *The rounds.* Step 3 takes each tf-exponent (α_0, k) of g_2 with 1 + η_1 ≤ Re α_0 < 2 + η_2, and its remainder
    exponents α_0 + ℰ_ind below 2 + η_2 "are treated in turn" (PART-III-I12-SPECTRAL.md:278-281). A chain is therefore a
    set of points α_0 + (sums of elements of ℰ_ind) in a window of length below 1 + η_2 − η_1, one round of III.G⁗
    Proposition 4.4 per point and log order. η_1, η_2 ∈ (ε_K, ε_+) (I12:58), so η_2 − η_1 < ε_+ < ε_ind ≤ δ_50 = 1.94137
    × 10⁻⁸ (LD7, LD10).
  - *ℰ_ind below 2* (L2). III.D Lemma 4.1's list is complete: the non-integer roots of □^Υ(0) above ½ are λ_s0,2 and the
    sl roots l + 1 + δ_l, l + 2 + δ′_l, the other factors having integer roots (PART-III-D-GAUGEPOT.md:186-206). The
    roots below ½, the mirrors 1 − λ, are left out, as they must be: read literally (D4:54-59), each 1 − λ_sl,l+1 would
    put a base-2 element 1 − δ_l into ℰ_ind for every l, infinitely many below 1, against Step 3's "finitely many
    rounds" (I12:280-281) (stated D531, verifier 229). A root enters ℰ_ind through a class 𝒜^((b,0) ∪ (b + ℰ_ind)), b =
    1 or 2 (D3:143-148), as λ − b plus a non-negative integer. The record's base-3 classes (F4:97, 299-300; I12:96-98)
    are derivative images of base-2 terms with the same offsets (F4:89, 109; D3:201-202), and ω̇(0, A) is of vector type
    1 at b_0, whose roots are integers (F4:103-104; GAUGEPOT:184), so they add no element below 1 (D531). Every element
    in [1, 2) other than 1 itself (from the roots 3 of s0 and v1 at b = 2, D3:40, GAUGEPOT:184; D531) is then at least 1
    + δ_2, δ_2 = 2.6667 × 10⁻⁷ (λ_s2,3 at b = 2), above 1 + δ_50, so inside the window only elements below 1, and the
    element 1 once, can be added. On LD9's reading (the s0 state is ρ²C^∞, D3:143, and λ_s0,2 enters only as 1 + d0,
    through the mass state's gauge part) the only element below 1 is d1 = 3.3333305 × 10⁻⁷, from λ_s1,2 at b = 2, 17.2
    times δ_50. On the broad reading, every root through either class, d0 = 1.3333327 × 10⁻⁶ is below 1 as well; that
    needs a ρ^(2+d0) term in some 2 + ℰ_ind class, which no state cited carries (LD9) and which the record does not
    exclude, since it does not list ℰ_ind.
  - *Per chain* (L3). On LD9's reading a chain is α_0 + n d1 alone: at most ⌊(1 + δ_50)/d1⌋ + 1 = 3,000,003 rounds, and
    one more, α_0 + 1, when Re α_0 < 1 + η_2 (D531). On the broad one it is α_0 + n d1 + m d0, the lattice points below
    1 + δ_50: 1,125,003,384,947 ≈ 1/(2 d1 d0) of them, distinct exponents since d0 − 4d1 = 5.56 × 10⁻¹³ ≠ 0. Admitting
    δ′_1 or δ_2 in place of d0 as a second element below 1 would give 2.50 × 10¹² or 5.63 × 10¹² (verifier 229, D531).
  - *Against the level-3 rounds* (L4). A β-level in (3, 4 + ε_K] runs about (β − 3)/ε_ind level-3 rounds, on average
    ½/ε_ind ≥ 2.5755 × 10⁷ (LD11). On LD9's reading one level-2 chain is at most 2δ_50/d1 = 0.1165 of that, and less for
    smaller ε_ind, since the level-2 count does not depend on ε_ind. The level-2 loop is repeated at every β-level above
    3 with the same window (LD12 (v); I14:107-117), so the comparison holds level by level: at each, at most about N_2 ·
    3.0 × 10⁶ level-2 rounds, N_2 the number of g_2's tf-exponents (α_0, k) in the window (chains that share points only
    lower it), against about (β − 3)/ε_ind level-3 rounds. So they add no term of order 1/(ε_K ε_ind) unless N_2 exceeds
    about 8.6 (at ε_ind = δ_50; more for smaller ε_ind): the loop's length per chain is set by the record's root d1, not
    by ε_ind. (Corrected D531, verifier 229: the β-levels number at least about 1/ε_K, I15:323-325, "possible as the
    admissible levels are dense", not at most, so the total N_2 · 3.0 × 10⁶/ε_K printed here before was not a bound; the
    comparison level by level is unaffected.) On the broad reading a chain is 4.37 × 10⁴ times a level's level-3 rounds,
    and the level-2 rounds, about N_2 · 1.1 × 10¹²/ε_K > N_2 · 5.7 × 10¹⁹, would outnumber the counted 2.65 × 10¹⁵ by
    about 2.2 × 10⁴ (4.37 × 10⁴ is a chain against one level's level-3 rounds; corrected D531).
  - *What it rests on.* (a) ℰ_ind's sources being classes with b ∈ {1, 2} at the roots' own terms: a base 3 carrying a
    root's own term would put δ_2 = z/15 < d1 into ℰ_ind (the record's base-3 classes do not, L2), and a base l + 1 in
    harmonic l would make its least element δ_50 (L2's controls), which is LD12 (v)'s case. (b) Whether d0 ∈ ℰ_ind,
    LD9's open point, on which the count now moves by a factor of about 3.75 × 10⁵. (c) N_2, g_2's exponents not being
    listed: "shorter" needs N_2 times the log orders below about 8.6 (D531). (d) Log orders: a round is per (α_0, k),
    and the log orders at a point multiply its count; not bounded here. [D550: the record bounds (c) and (d) together,
    through III.I′′′′′′′′′′'s Λ, the chains merging there; the bounds and their sizes are LD15.] (e) Proposition 4.4's
    loss per round, not read, so this counts rounds, not loss. [D553: read; 2 + ℓ per application in III.J″'s
    accounting, as Proposition 5.1's; LD16.] The ι⁺ loop of LD12 (v) is untouched: E^ι_ind is not read. (f) Above all,
    the reading (D541, verifier 234): the record's convention is generic, ℰ_ind any index set with min Re ≥ the gauge
    potential's ε_ind (D3:46-47; < 9.47 × 10⁻⁸, < 1.46 × 10⁻¹⁰ by D4's refinement), and read so, a chain can run up to
    (1 + δ_50)/ε_ind rounds, the loop then possibly far longer than the counted ones. (a)-(e) hold on the reading that
    ℰ_ind is built from the indicial roots' offsets. That is the construction's (LD14, D542): III.D‴'s every exponent
    lies in ℳ.
- LD14 (the ι⁺ loop's length; deduced from the record's text, D534). LD12 (v) gave the ι⁺ iteration that Lemma 3.2's
  Steps 1-2 run at every β-level below 3 (I9:230-232, 256-261) as up to about (2 − λ_♯)/ε_ind rounds per level, and so
  possibly of the counted loops' order 1/(ε_K ε_ind). The record fixes it differently.
  - *The step.* The iteration is III.I′′′′′ Proposition 2.1's Step 2 (I9:231, "the iteration and its termination are
    III.I′′′′′'s"). There ε_ind is defined afresh as min Re ℰ^ι_ind, ℰ^ι_ind being III.G″ (4.4)'s index set, "not
    (1.1)'s" (PART-III-I6-ALMOSTBDD.md:118-119). Each round treats every λ_0 of the window together and raises the least
    real part c_0 of the source's ι⁺-exponents by at least that number, starting at c_0 ≥ λ_♯ and ending once c_0 ≥ α♯_+
    (I6:167-172). So, with m_ι := min Re ℰ^ι_ind, a level runs at most ⌈(α♯_+ − λ_♯)/m_ι⌉ rounds, and α♯_+ < 2 (α♯_+ :=
    2 − ε at the levels below 3, I9:256-257), λ_♯ = 3/2 + (1 − e_Υ)γ_Υ = 1.5099 at the record's point (LD8): at most
    ⌈0.4901/m_ι⌉. Unlike the level-2 loop (LD13), there is no factor for the number of exponents: the window is one
    round.
  - *What m_ι is.* The record does not compute it, but its class structure bounds it (corrected D538, verifier 232).
    III.G″ (4.4) gives ℰ^ι_ind only as "an index set ℰ_ind with min Re ℰ_ind > 0 depending only on L̄ and on whether λ =
    1" (PART-III-G3-GRAFT.md:298-299), and its proof says where it comes from: the Myers-Perry formal solutions differ
    from the Minkowski ones at ι⁺ by corrections O(t_*^(−min Re ℰ_ind)), ρ ~ t_*^(−1) there (G3:305-308), the s1 and v1
    states entering through III.D″ (3.4) (G3:309-311). G3:338-339 collects that set from "the states' index sets of
    III.D″, III.D‴, III.F⁗, 2 + ℕ_0, and (2, 1) when λ = 1", whose classes are (k, 0) ∪ (k + E) with E the indicial-root
    offsets (D3:198-203, F4:80, D4:52-60). On LD13's reading of those offsets, m_ι ∈ {d1} ∪ [1, ∞): m_ι ≥ d1 = d(Re
    λ_s1,2, ℤ), with no Tangherlini computation. That is a reading, not the record's convention (corrected D541,
    verifier 234): the record's index sets are generic, "an index set with min Re ℰ_ind ≥ ε_ind, which may change from
    line to line" (D3:46-47; D4:57-58; F4:28-29; G3:298-299), that ε_ind being the gauge potential's, below 9.47 × 10⁻⁸
    (F4's distance from ℤ) and 1.46 × 10⁻¹⁰ (D4's refinement; LD10). On the convention as written the ceiling is
    ⌈0.4901/ε_ind⌉ for that ε_ind: above 5.2 × 10⁶ rounds per level, and up to 3.4 × 10⁹ at D4's bound, which against
    (1.1)'s ε_ind ≤ δ_50 would make the ι⁺ loop up to about 130 times the counted tf-rounds. And LD13 does not address
    the III.D‴ class-root rows (G3's Table 1.1; D4:160-170): a base-3 class carrying λ_s2,3's own term would put δ_2 =
    z/15 into the set, 1,837,876 rounds per level. It differs from (1.1)'s ε_ind in value (VI4:38); the sets overlap
    (I9:32-33).
  - *Values, on LD13's reading.* There m_ι ≥ d1 and a level runs at most ⌈0.4901/d1⌉ = 1,470,302 rounds, against about
    (β − 2)/ε_ind of Lemma 3.2's tf-rounds at the same level (LD12 (ii)), on average ½/ε_ind ≥ 2.5755 × 10⁷: a ratio 2(2
    − λ_♯)ε_ind/m_ι ≤ 0.0571, smaller for smaller ε_ind, the number of levels being common to both. If the ρ^(2+d1) term
    were absent, m_ι ≥ 1 and the loop would be one round per level on LD9's reading (on LD13's broad one m_ι = d0,
    367,576 rounds; D541); but LD9 computes it present at the record's point, A = 141.4269 (D450-D451, pinned by the
    near-resonance, nonzero at every cut-off computed), so m_ι = d1 there (A is computed with S6's cut-offs; ℰ_ind being
    fixed once, I5:190, one admissible cut-off with A ≠ 0 suffices, D541) and the loop runs up to the 1,470,302 per
    level, a ceiling, since a round raises c_0 by at least m_ι and may skip (I6:167-168; D541) (corrected D539; LD9's
    "not decided" is the bound over every cut-off, not the record's point). Only m_ι near ε_ind would make it comparable
    to the counted loops (ratio 1 at m_ι ≈ 1.90 × 10⁻⁸), which the class structure excludes on LD13's reading (corrected
    D538) and the convention as written does not (D541).
  - *What is needed.* the reading itself (corrected D541): that the record's ℰ^ι_ind, and LD13's ℰ_ind, are built from
    the indicial roots' offsets, the III.D‴ class-root rows included, rather than being any index set above the gauge
    potential's ε_ind. On that reading m_ι = d1 at the record's point (D538-D539); on the convention as written neither
    loop is bounded by d1, and both could outgrow the counted ones. Each round's loss, III.G″ Corollary 4.3 and III.I′
    Proposition 3.1 composed, is not read here. With LD13, the two loops LD12 (v) left uncounted are then both bounded
    per level by the record's own roots (d1 for the level-2 chains, m_ι for ι⁺), the first up to the factor N_2.
  - *The reading, at source (D542, read and deduced).* The construction answers D541. III.D‴ fixes ℳ, the real numbers
    in [−10, 10] of the form Re λ + j, λ an indicial root and j ∈ ℤ, and says "every exponent below lies in ℳ"
    (PART-III-D4-GENSTATES.md:54-59; a statement of III.D‴'s, and ℳ is finite, so below 10, not in the ℕ_0 tails;
    corrected D544): the generic "index set with min Re ≥ ε_ind" is the notation for what the construction yields. Lemma
    2.1 (D4:76-100) builds each state from its leading term ρ^m w, the corrections that A − N(A) ∈ ρDiff²_b adds
    (exponents m + 1 + ℕ_0, the coefficients being smooth), the formal solution of III.A Lemma 1.5 ("its exponents are
    those of ℱ_1 plus ℕ_0"), and the decaying part P_b⁻¹f_2, whose exponents are the indicial roots with Re ≥ λ_s1,2 = 2
    + d1 plus ℕ_0, with the source's own (III.A Lemma 1.4, D4:93-97). The sources are not always smooth: the boost's
    breve state is sourced by [□, t_*]ω′, which carries ρ^(3+d1), and has the exponent 1 + d1, offset d1 from its base 1
    (D3:221-225). So the offsets are not merely integers or (root ≥ 2 + d1) + j − base, as D542 wrote (corrected D544,
    verifier 235). What holds: every exponent is a root or a source exponent shifted by integers, the types being
    preserved at b_0 (D4:83-85, 173-175), and the only positive roots below 3 are 2 + d1 and 2 + d0 (GAUGEPOT:178-186),
    so an offset strictly below d1 needs a base in (2, 2 + d1], which no state has. Among the states III.G″ collects
    (G3:338-339, Table 1.1 at G3:44-60), checked family by family (verifier 235: the boost state and its breve, h_s1 and
    h̆¹, the s0 chain, the III.D‴ classes, III.F‴'s mass states and III.F⁗'s physical states), none gives an offset in
    (0, 1) other than d1. The boost state (base 2 in ω′, 3 in h_s1 = δ*ω, D3:198-203) and its breve give d1; the s0
    state is ρ²C^∞ (D3:143), so d0 does not enter; the v1 roots are integers; the III.D‴ class states have bases ≤ 0;
    III.F⁗ (F5, not F4, which is III.F‴) has in its Proposition 5.1 set λ^C − 1 just above 1 (F5:314; 1 + 2.93 × 10⁻⁶,
    F2:133-134), offset 3.0000029 from its base −2, its own bounds keeping offsets ≥ 1 (F5:275-277, 312-317). So, on the
    construction, ℰ^ι_ind ∩ (0, 1) = {d1} and, A ≠ 0 (LD9), m_ι = d1: the ι⁺ loop runs at most 1,470,302 rounds per
    level, about 1/17.5 of the levels' tf-rounds. The same construction gives LD13's ℰ_ind ∩ (0, 1) = {d1}, the s0 state
    carrying no ρ^(2+d0). Outside G3:339's list, the λ = 1 mass-change and boost-source grafts (G3:18-21, 390-394,
    436-437): their mass states add no element of (0, 1) (D544). D542 had left III.F⁗ unread with a wrong reason ("above
    4"), and cited F4 for it.
- LD15 (the level-2 rounds through the record's Λ; deduced from I11 and I12, counted at the record's point; D550,
  `checks/lambdacount5.py` C1-C5, exact). LD13 left two factors of the level-2 loop open: (c) N_2, the number of g_2's
  tf-exponents in the window, and (d) the log orders. The record bounds both, in one set, as finite (corrected D554,
  verifier 239: it gives no size).
  - *The container.* III.I′′′′′′′′′′ Definition 1.1 (PART-III-I11-SPACETIME.md:66-79) defines Λ as the smallest set,
    closed under conjugation, containing π₁(ℰ_++ ∪ 𝒢 ∪ ℰ^C_I) ∪ {λ_♯, 3} ∪ (2 + π₁ℰ_col) with Λ + w ⊂ Λ for every w ∈
    π₁(ℰ_ind ∪ ℰ^ι_ind) ∪ {1}; 2 ∈ Λ (I11:155). Its Lemma 1.2 (c) (I11:96-107): every exponent (λ, k) the construction
    produces with 2 ≤ Re λ ≤ 3 + ε_+ has λ ∈ Λ and k ≤ K(λ) := L_0 + (N_* + 1)(l_* + 1)(n(λ) + 1), N_* := ⌈5/η_0⌉ + 2,
    η_0 the least real part of the increments, n(λ) the number of points of Λ below Re λ. Level 2's window in
    u-exponents is W = [2 + η_1, 3 + η_2): I12 chooses η_1, η_2 so that no point of Λ has real part at either end
    (PART-III-I12-SPECTRAL.md:58-60), the tf-window [1 + η_1, 2 + η_2) shifted by one. So LD13's chains lie in Λ and
    merge there: a level's level-2 rounds number at most |Λ ∩ W| if a round treats an exponent, and at most Σ_(λ∈Λ∩W)
    (K(λ) + 1) if it treats an exponent and a log order, as Step 3's "for each tf-exponent (α_0, k)" reads (I12:278).
    N_2 and the overlap of chains are no longer separate factors, and Lemma 1.2 (a) makes both bounds finite
    (I11:87-88). (Corrected D554, verifier 239: the merging uses Λ + d1 ⊂ Λ, which holds on the construction's reading,
    d1 ∈ π₁(ℰ_ind ∪ ℰ^ι_ind) (D542-D544); the record lists neither the increments nor a size, only finiteness.)
  - *What the record names* (C2-C3). It does not number |Λ ∩ W|: ℰ_++, 𝒢, ℰ^C_I and ℰ_col are not listed. Its named
    generators λ_♯ = 3/2 + (1 − e_Υ)γ_Υ = 1.5099, 2 and 3, with the increments d1 (on the construction, D542-D544, A ≠
    0) and 1, give Λ_0 ⊂ Λ with |Λ_0 ∩ W| = 7,470,307: the chains λ_♯ + n d1 (3,000,002 points in W), λ_♯ + 1 + n d1
    (1,470,302) and 2 + n d1 (3,000,002), and the point 3, no two sharing a point, the count the same at the three η
    tested. With LD9 G7's increments 1 + d0, 1 + δ_2 and 1 + δ′_1 (on LD9's reading that they lie in ℰ_ind) it is
    11,881,206.
  - *Against the level-3 rounds* (C4). A β-level's level-3 rounds are on average ½/ε_ind ≥ 2.5755 × 10⁷ (LD11). At ε_ind
    = δ_50 the named part of the container is already 0.290 of that (0.461 with G7's increments), and each further base
    (an unlisted generator with real part in [3/2, 3 + η_2), or one plus an increment of integer part ≥ 1) adds up to
    3,000,003 points, 0.1165; at smaller ε_ind the ratios fall as ε_ind, the container not depending on it. So at ε_ind
    = δ_50 the container shows the level-2 loop shorter than a level's level-3 rounds if the unlisted generators add at
    most six chains (four with G7's increments), and at δ_50/10 at most 83 (81); it does not decide it, and LD13's route
    through N_2 (rounds ≤ min(N_2 · 3,000,003, |Λ ∩ W|)) stands beside it. (Corrected D554, verifier 239: D550 wrote
    "only if" and "fewer than about six", the thresholds being those of ε_ind = δ_50 and sufficient, not necessary.)
    That is LD13's threshold N_2 ≲ 8.6 again, now with the chains counted once.
  - *The log orders* (C5). On the construction η_0 = d1, so N_* = ⌈5/d1⌉ + 2 = 15,000,015, and at every point of W, n(λ)
    ≥ 1,470,303 (λ_♯ + n d1 below 2, and 2), so K(λ) ≥ 1 + (N_* + 1)(n(λ) + 1) ≥ 2.2055 × 10¹³ (L_0 ≥ 1, l_* ≥ 0). That
    is Lemma 1.2 (c)'s ceiling, set by its count (at most N_* raises at an exponent, each by at most l_* + 1, one per
    window of width at least η_0 below 2; I11:101-105), not by the log orders the construction produces. Read per (α_0,
    k), the record's own bound on one level's level-2 rounds is at least the sum over Λ_0 ∩ W of K + 1, ≥ 5.83 × 10²⁰
    rounds, above the counted loops' 1.33 × 10¹⁵ rounds in total (their loss 2.65 × 10¹⁵, LD11) at a single level
    (corrected D554, verifier 239: D550 set rounds against that loss). So, counted per (α_0, k), the record's
    bookkeeping does not bound the level-2 loop below the counted loops; counted per exponent (LD16: one application
    covers an exponent's log orders) its bound is |Λ ∩ W|, which the record leaves undecided; and the log orders
    actually produced might bound it, which the record does not compute.
  - *What it rests on, and what is needed.* The reading of W in u-exponents (I12:58-60's two excluded values are the
    level-2 window's ends); the construction's increments (D542-D544); for the second bound, a round per (α_0, k), as
    Step 3 writes it. Needed: ℰ_++ (whose part below 2 is π₁ℳ, I11:88), 𝒢, ℰ^C_I and ℰ_col listed at the record's point,
    and the log orders produced. LD13 (c) and (d) are replaced by this. The ι⁺ loop (LD14) has neither factor, one round
    treating a whole window.
- LD16 (the two uncounted loops' loss per round, in III.J″'s accounting; read and deduced, D553). LD13 (e) and LD14
  counted rounds, not loss. The record's accounting gives each round a loss, as LD11 (ii) did for the level-3 loop.
  - *The level-2 loop.* Each round is III.G⁗ Proposition 4.4 (PART-III-G5-TF.md:448-462). Its proof builds u from u_tf,α
    := N_tf⁻¹(ρ_ztf^(−α)f_0) (G5:484-488) and forms the next round's source as the error F_α := source − L̂_b(σ)u_α
    (G5:520), a second-order b-operator applied to the inverse's output: the structure LD11 (ii) charged Proposition
    5.1. III.J″ charges L_b loss 2 (PART-III-J3-TAME.md:115-121, 164) and N_tf⁻¹ the loss ℓ of III.F′ Corollary 3.4
    (J3:167-168), and names Proposition 4.4 beside 5.1 in that bullet (J3:168-171): 2 + ℓ per application, as for a
    level-3 round, so LD13 and LD15's comparisons of round counts are comparisons of loss, the per-round loss being the
    same. (Corrected D557, verifier 242: 2 + ℓ is this note's sum by Lemma 1.2 (a)-(b), J3 saying only "fixed loss" and
    naming L̃_b(0)⁻¹, which G5 does not apply; the 2 is solid, while ℓ is III.F′ Corollary 3.4's closed form at each
    proposition's own weights, not shown equal for 4.4 and 5.1, so the comparisons of counts are comparisons of loss up
    to that.) [D560, read: ℓ is the same. Corollary 3.4's proof fixes its orders from β_sctf alone, β := −β_ztf, q := 2
    − β entering only near ztf without loss, r_out := β_sctf − 2 − ε/2 and r_± I.A Lemma 7.1's with that outgoing value,
    and its loss is II.G′ Lemma 4.1's ℓ + ℓ̃ near sctf (PART-III-F2-INDICIAL.md:478-491), a closed form in β_sctf and
    those orders (section 2's row for Corollary 3.4). Both kinds of round apply it with β_sctf = ℓ_scf (G5:209-211,
    694-695), and ℓ_scf = 3/2 − ε at both levels: at level 2 by I12:267, at level 3 since Proposition 5.1's output has
    scf weight 3/2 − 2ε = ℓ_scf − ε (I12:293-294) and its source 5/2 − ε = ℓ_scf + 1 (I14:128-129). So a level-2 and a
    level-3 round cost the same 2 + ℓ + ℓ̃ in this accounting, and LD13 and LD15's comparisons of counts are comparisons
    of loss.] [Corrected D563, verifier 245: the loss does not depend on β_sctf alone. II.G′ Lemma 4.1's ℓ = max(⌈sup r
    − r_out⌉, ⌈(s − 1)₊⌉) uses sup r = r_in and s, which F2's proof leaves free (r_in only "above the largest incoming
    threshold", F2:368-371; s ∈ ℤ large, F2:382), and which II.G′ Corollary 4.2 fixes as r_in := max(r_out, ½(−1 + ϑ_in)
    + 1) and s := s_c (PART-II-G2-DECAY.md:690-701), so ϑ_in and s_c enter; ℓ̃ = ⌈(−s)₊⌉ = 0 there (s_c ≥ 0, r ∈ [r_out,
    r_in]). So the two kinds of round cost the same if both make the same choices of s, r_in and the radial-set inner
    products, natural for the one operator N_tf(L̂_b, ±1) but not stated in the record: "the same" is conditional, not
    settled. Citations corrected: I12:267 is level 1 (Step 2); level 2 is Step 3 (I12:278-281), which restates only
    ℓ_zf, its input 5/2 − ε (I12:131-137) admitting ℓ_scf = 3/2 − ε; level 3's value is explicit at
    PART-III-I9-COMMOTION.md:287-288 and PART-III-I7-PARAMS.md:226 (I12:293-294 pins it only to (3/2 − 2ε, 3/2 − ε]).
    And "ℓ" here is Corollary 3.4's integer, Lemma 4.1's ℓ_a + ℓ̃, not the ℓ_a of the paragraph's first bracket; III.J″
    itself states only "fixed loss" for Propositions 4.4 and 5.1.] One application at (α_0, k) treats every log power up
    to k: its proof solves away each of the k + 1 terms ρ_tf^(α_0)(log ρ_tf)^j f_0, and u is a sum of up to k-fold
    α_0-derivatives of terms holomorphic in α_0 (G5:474, 476-481, 489-491). So the applications at lower log orders that
    Step 3's "for each tf-exponent (α_0, k)" would add are redundant, if the top order at α_0 is treated first
    (I12:278-281 fixes no order; D557); LD15's per-(α_0, k) bound is the procedure as written, and its per-exponent
    bound |Λ ∩ W| the procedure without the redundancy.
  - *The ι⁺ loop.* Each round applies III.G″ Corollary 4.3 to the source's terms at λ_0 and removes the error by III.I′
    Proposition 3.1, the next source being F − L_b(u_λ0 + u′_λ0) (PART-III-I6-ALMOSTBDD.md:128-131, 156-157, 167-168).
    III.J″ charges Corollary 4.3 the loss d + 2, d being III.G′ Theorem 3.1 (2)'s for N_ι+(λ)⁻¹ composed with a contour
    integral and with L_b (J3:160-164), and Proposition 3.1 a fixed loss through L̃ (loss 2; J3:173-176). So a round
    costs at least 4 + d_G, d_G := III.G′ Theorem 3.1 (2)'s loss. (Corrected D557, verifier 242: d_G has a closed form,
    section 2's item 6 (2.5), d = 7 + 2⌈ℓ_I − Re λ⌉ for Re λ < 2 − δ, so on the ι⁺ window 11 when 3 < ℓ_I < 3.5 (at most
    12 at the window's top) and 13 at ℓ_I = 3.6; "no formula" was LD4 m1's, before item 6, and the open input is a_I,
    which bounds ℓ_I (section 3). And 4 + d_G is a floor, not a ceiling: Proposition 3.1's fixed loss has no value in
    the record, and the replacement F − L_b(u_λ0 + u′_λ0) adds an L_b, so D553's comparison, at most (4 + d_G)/35 of the
    counted loops' and below them only while d_G < 31, is withdrawn; it also took a level-3 round at 2 rather than 2 +
    ℓ, and held only at ε_ind = δ_50.) What stands: with LD14's ceiling of 1,470,302 rounds per level, 1/17.52 of a
    level's level-3 rounds at ε_ind = δ_50 (less at smaller ε_ind), the ι⁺ loop's loss per level is below the counted
    loops' if one of its rounds costs less than 17.52 times a level-3 round; the floors are 4 + d_G, 15 to 17 at those
    ℓ_I, and 2 + ℓ, and neither round's cost has a ceiling in the record. [D562, E1'a for ℓ_I; `checks/dg5.py` G1-G3,
    exact: a_I is a free weight in the record, a_I > 3/2 (PART-III-I-CONE.md:65; I5:471), asked a_I > 3 + ε_+ by (H4)
    (I11:46-48), and the source fixes it at 3 + ε_I with 0 < ε_K < ε_+ < min(ε_ind, ε_I) < 1 (I-CONE:68, 472-473);
    ℓ_I^max > 100 (PART-III-I2-SCRI.md:31). So every admissible a_I allows ℓ_I ∈ (3 + ε_+, 3.5), the range section 2's
    items 3-4 assume, and there (2.5) gives d_G = 11 on the whole ι⁺ window [λ_♯, 2 − ε) once the free δ is taken below
    ε (G1): an ι⁺ round costs at least 15. With the source's a_I and ℓ_I up to 3.5 + ε_I < 4.5, d_G ≤ 13 on the window,
    14 at its top if δ ≥ ε (G2).] III.J″'s row for III.I′′′′′ (J3:261) is this iteration's (I9:231; its MOD column lists
    III.G″ Corollary 4.3) and counts "exponents in a window, and rounds raising α′_K to α_K": exponents, not the rounds
    LD14 counts, a round treating every λ_0 of the window together (I6:127-129), and which of the two III.J″ multiplies
    is not stated (corrected D557: D553 said the table has no row); by its rule (g) and Lemma 1.2 (e) (J3:157-158,
    76-77) their loss is their number times one round's.
  - *What it rests on.* LD11 (ii)'s reading of III.J″'s accounting, now applied to Propositions 4.4 and to Corollary 4.3
    with III.I′ Proposition 3.1; the per-round floors 2 and 4 + d_G, which a finer accounting might lower (as LD11 (ii)
    notes). Open: a_I (through ℓ_I, d_G's input), Proposition 3.1's fixed loss, and ℓ's value (equal at both kinds of
    round if both make the same choices of s and r_in, D560, D563); the per-round loss is independent of k by J3's (g)
    (J3:157-158), as it claims.
- LD4 (verifier 164, D348). No blocking finding. M1: section 1 described d as a flat sum over the table's rows; it is
  the recursion (1.1), with two rows outside Theorem 4.1. M2: LD3 bounds the d III.J″ produces, not the optimal loss.
  M3: the level-3 loop nested inside the β-chain was missing; it is LD3 (ii) and in the counts. m1: III.G' Theorem 3.1
  (2)'s d has parts d_1(s), m(s) with no formula, the sixth loss of section 2. m2: the k'' scope sentence in III.K was
  false at the e_S bound; repaired there. m3: LD3's conditional is already discharged within the accounting (2 per
  level). m4: the labels of the many-primed parts, now file names. Nits: I15:37 cited for α; K > 2/ε_K; Lemma 1.2 (e),
  (g) described correctly; III.K line numbers updated.
