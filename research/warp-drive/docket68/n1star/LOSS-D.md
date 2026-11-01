# LOSS-D -- the loss d of III.J''' Theorem 4.1, added up as far as the record allows (E1')

Status: written (D347); LD3 added (D348), LD5 (D353), section 2b (E1'b, D357), LD6 (D365), LD7 (D377, which corrects LD6
(ii)-(iii); repaired D380). Read by verifier 164 (D348), whose three major findings (the structure of d, the scope of
LD3, a second nested loop) and its minor findings and nits are seated (LD4); section 2b read by verifier 166 (D358),
findings seated. LD6-LD8 to be read (LD8: D397).

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
  1 + η_2 − 2ε (η_2 < ε_+ < ε_ind) up to β − 2 (I14:120-128; PART-III-I12-SPECTRAL.md:287-297), composed by III.J'''
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
  proof). (i) I15's β-chain: α ∈ (4, 4 + ε_K] (I15:37) and α_1 ∈ (2, α − 2) (I15:305), so the chain climbs more than 2
  in steps below α − 4 ≤ ε_K, and K > 2/(α − 4) ≥ 2/ε_K. With ε_K < ε_ind < 3 × 10⁻⁶ (J-PARAM:34, F2:133-136), K > 6.8 ×
  10⁵. The levels are composed in the proof itself: level k + 1 takes R_q u with u at level k (I15:327-329), R_q is of
  second order (I15:179-181), and the one-step route of the source is closed at n = 4 (I15:12-17). Within III.J''''s
  accounting each level costs at least 2 (BG applied to R_q u, J3:115, 121), so the d it produces is at least 2K >
  1.3 × 10⁶, and N = 21d + 6 > 2.8 × 10⁷. (ii) Nested inside, at every β-level, I14's level-3 loop rises by ε_ind − ε
  per round from about 1 to β − 2, so about (β − 3)/ε_ind rounds at the levels above 3, about 3 × 10⁵ near β = 4. Over
  the β-chain this is of order (1/ε_K)(½/ε_ind) > 5 × 10¹⁰ rounds; if a round costs a derivative (it rests on III.F'
  Corollary 3.4's ℓ, section 2's table), the d this proof produces exceeds that. (iii) These bound the d that
  III.J''''s accounting of the record's proof delivers: Lemma 1.2's rules are upper bounds, Theorem 4.1 is
  existential, and the optimal loss may be far smaller. The levers: the parameter point (E1'a's first question); a
  per-level gain larger than α − 4; a different proof of the level step, keeping in mind that the source's one-step
  route is closed at n = 4 (I15:12-17). (iv) [D425: with (1.1)'s ε_ind ≤ 1.94 × 10⁻⁸ at the record's point (LD10,
  D422), (i) gives K > 2/ε_K > 1.03 × 10⁸, the d of III.J''''s accounting at least 2K > 2.06 × 10⁸, and
  N = 21d + 6 > 4.3 × 10⁹. (ii)'s nested loop runs about (β − 3)/ε_ind > 5.1 × 10⁷ rounds per level near β = 4, and
  more than (1/ε_K)(½/ε_ind) > 1.3 × 10¹⁵ rounds over the chain. These are lower bounds for what the record's proof
  delivers, not for the optimal loss, as in (iii).]

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
    gives only min Re ≥ ε_ind (I6:119). So two kinds of element remain, none computed as numbers at n = 4 in the
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
    - Not computed: the dual state, and whether some ζ makes A vanish. A variation for which the pairing is nonzero:
      every one computed in D442.

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

- LD4 (verifier 164, D348). No blocking finding. M1: section 1 described d as a flat sum over the table's rows; it is
  the recursion (1.1), with two rows outside Theorem 4.1. M2: LD3 bounds the d III.J''' produces, not the optimal loss.
  M3: the level-3 loop nested inside the β-chain was missing; it is LD3 (ii) and in the counts. m1: III.G' Theorem 3.1
  (2)'s d has parts d_1(s), m(s) with no formula, the sixth loss of section 2. m2: the k'' scope sentence in III.K was
  false at the e_S bound; repaired there. m3: LD3's conditional is already discharged within the accounting (2 per
  level). m4: the labels of the many-primed parts, now file names. Nits: I15:37 cited for α; K > 2/ε_K; Lemma 1.2 (e),
  (g) described correctly; III.K line numbers updated.
