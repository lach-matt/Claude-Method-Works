# P-40-sem: the fixed seminorms of sec:iii-i8-1 and prop:iii-i8-4-1 (i)

Tree read at HEAD 6a65bbad. I edited three chapters: 40 (the gap itself), and 41 and 44, where a use of
prop:iii-i8-4-1 (i) had to change to stay consistent. I did not touch the crosswalks, because no label was added or
removed. Nothing in chapters 43, 46 or 71 was edited, and neither was proofs/P-U71-small.md. No commit was made.
Line numbers below are those of the edited files.

## 1. Verdict on point 3: it is a real gap

The proof of (i) at α″ used one fixed seminorm on both sides, and no finite regularity can satisfy that. The same gap
is in (ii) at α″, which the report did not mention. A closely related form of it is in two uses outside chapter 40:
the end of the proof of thm:iii-i11-4-1 (ch. 41) and step (4) of prop:iii-i15-2-5 (ch. 44).

**Notation.** At the level α_i write Y_i := ‖·‖_(𝒴(α_i)), with regularity y_i, and N_i := ‖·‖_(α_i), with regularity
n_i. Before the repair, sec:iii-i8-1 (old 40:737–742) chose Y_i so that the maps of lem:iii-i8-3-2 *and those of
prop:iii-i8-4-1 (i)* are bounded in it. The proof of (i) at α″ (old 40:1187–1193) wrote ‖F‖ := ‖F‖_(𝒴(α″)) = Y_(i+1)(F).

**The requirements.**

- **(R1) Step 0 of lem:iii-i8-3-2 at (α_i, α_(i+1)).** The proof needs ‖(L − L_b)u‖_(Y_(i+1)) ≤ C(‖h‖ + |p⃗|)N_i(u).
  L − L_b is a b-differential operator of order 2 whose coefficients are small but generic, so this needs
  n_i ≥ y_(i+1) + 2. The proof of prop:iii-i8-4-1 uses the same count for v(S⃗) (40:1183–1185) and in (ii) (40:1228).
- **(R2) The bound of the solution at α_i.** Old (i) at α_i says N_i(u) ≤ C Y_i(F), and the same holds for the
  remainder bound of lem:iii-i8-3-2 that proves it. The map F ↦ u is a right inverse of the wave operator L, cut down
  to forward solutions. Such an inverse gains at most one derivative. To see this, take a wave packet u of frequency λ
  along a null geodesic, supported in the interior of Ω_* and vanishing near {t^♭_* = 1}, so that u is its own forward
  solution. Its amplitude must be cut off along the geodesic, so ‖Lu‖_(H^k_b) ~ λ^(k+1) while ‖u‖_(H^(k+2)_b) ~ λ^(k+2).
  Hence n_i ≤ y_i + 1. In the paper the bound is in fact a loss: the forward solution operator loses d_T (ch. 43,
  lem:iii-j2-2-1 (a)), and chapter 71 charges a level step below 3 at most 497 plus its iterations. So y_i ≥ n_i − 1,
  and in the paper y_i ≥ n_i + (a positive loss).
- **(R3) Old (i) at α″.** It applies (i) at α′ = α_i to F ∈ 𝒴(α_(i+1)): both |p⃗′_(α′)(F)| ≤ C Y_i(F) and
  N_i(u(0)) ≤ C Y_i(F). It then needs Y_i(F) ≤ C Y_(i+1)(F) on 𝒴(α_(i+1)). On that space a seminorm of higher
  regularity is not bounded by one of lower regularity (oscillating sections supported in the interior show this). So
  this needs y_(i+1) ≥ y_i, and also ε_(i+1) ≤ ε_i.

**The cycle.** y_(i+1) ≥ y_i (R3) ≥ n_i − 1 (R2) ≥ y_(i+1) + 1 (R1). This is a contradiction. So no choice of finite
regularities satisfies the text as written, even if F ↦ u gained a whole derivative.

**The other places with the same gap.**

- **(ii) at α″.** Old 40:1220–1225 obtains only ‖(L_j − L_0)w_j‖_(𝒴(α″)) → 0, which is R1 with the w_j bounded only
  in N_i. It then uses (i) at α′ as ‖w_j − w‖_(α′) ≤ C‖R_j‖_(𝒴(α′)). This needs R_j → 0 in Y_i, which is the same
  comparison as R3.
- **The end of the proof of thm:iii-i11-4-1 (41:1034–1042).** The old text writes ‖F‖ := ‖F‖_(𝒴⁰(α)). It needs
  ‖F‖_(𝒴(α′)) ≤ C‖F‖, and also ‖u_0(0)‖_(w_0) ≤ C‖F‖. But ‖·‖_(w_0) lies two orders above ‖·‖_(𝒴⁰(α)) (Step 0 of
  lem:iii-i11-3-2), and the old text routes it through (i) at α′. That closes the same cycle.
- **Step (4) of prop:iii-i15-2-5 (44:330).** It reads (i) at α_1 as |p⃗′_(α_1)(Ψ)| ≤ C‖Ψ‖_(𝒴(α_1)), in the fixed
  seminorm, and that seminorm is the forcing seminorm of the level step that ends at α_1.

**What was never wrong.** The statements themselves were not wrong. "Linear, with bounds uniform", read as continuity
of linear maps between Fréchet spaces, is true. Only the bookkeeping inside the proofs was wrong, as the report said.
prop:iii-i15-2-5 states its own induction bound with "‖F‖ … of large enough regularity", and that is the form that
works.

## 2. The repair

The repair keeps lem:iii-i8-3-2, lem:iii-i8-3-3 and lem:s21-motions-at-b exactly as stated, and states the bound of
(i) in a second seminorm ‖·‖^+_(𝒴(α)). This is the quotient norm of sec:iii-i8-1 at a larger regularity and a smaller
ε, depending on the seminorm bounded.

- **Ch. 40, sec:iii-i8-1 (40:737–746).**
  - The maps of (i) are removed from the list of maps bounded in ‖·‖_(𝒴(α)).
  - ‖·‖_(α′) is said to have regularity at least that of ‖·‖_(𝒴(α)) plus 2, because of Step 0.
  - ‖·‖^+_(𝒴(α)) is introduced, with the reason for it.
  - The demand on d is widened: the bounds by ‖h‖ must hold in these seminorms, namely those of lem:iii-i8-2-6 (b),
    lem:s21-motions-at-b and the count of Step 0.
- **Ch. 40, prop:iii-i8-4-1 (i) (40:1131–1133).** "Linear, with bounds uniform …: for each fixed seminorm ‖·‖_(α) of
  the space of eq:iii-i8-4-2 there are a seminorm ‖·‖^+_(𝒴(α)) of 𝒴(α) … and C with
  |p⃗′_(h,p⃗)(F)| + ‖u‖_(α) ≤ C‖F‖^+_(𝒴(α))". Part (ii) and the rest of the statement are unchanged.
- **Ch. 40, the base (40:1141–1142).** The maps of cor:iii-i7-4-6 are continuous on 𝒴(α_0), so each fixed seminorm of
  their values is bounded by some ‖·‖^+_(𝒴(α_0)). This is (i) at α_0.
- **Ch. 40, the new paragraph "The seminorms" in the step (40:1150–1155).**
  - Fix the target ‖·‖_(α″).
  - Take ‖·‖_(𝒴(α″)) and ‖·‖_(α′) for lem:iii-i8-3-2 with the remainder in ‖·‖_(α″).
  - Let ‖·‖^+_(𝒴(α′)) be the seminorm of (i) at α′ for ‖·‖_(α′).
  - Let ‖·‖^+_(𝒴(α″)) be the quotient norm at a regularity at least those of ‖·‖_(𝒴(α″)) and ‖·‖^+_(𝒴(α′)), and at an
    ε at most theirs. On 𝒴(α″) ⊂ 𝒴(α′) it bounds both, the second up to a constant. The reason is that each defining
    space at α″ lies in the one at α′, with its norm bounding the norm at lower regularity and larger ε, because the
    K⁺-weight α″ exceeds α′. The quotient norm takes the infimum over more splittings at α′.
  - The induction is then over i with "(i) for every target". So the regularities need no global ordering.
- **Ch. 40, the level map (40:1177–1182).**
  - lem:s21-motions-at-b is used in ‖·‖_(𝒴(α″)) and in ‖·‖^+_(𝒴(α′)), so (i) at α′ bounds p⃗′_(α′)(Σe^ν).
  - lem:iii-i8-2-6 (b) is used in ‖·‖^+_(𝒴(α′)) for ‖v(S⃗)‖_(α′) ≤ C|S⃗|.
- **Ch. 40, (i) at α″ (40:1202–1211).** The proof writes ‖F‖ := ‖F‖^+_(𝒴(α″)) and proceeds as follows:
  - ‖G(0)‖_(𝒴(α″)) ≤ C‖F‖;
  - ‖u(0)‖_(α′) ≤ C‖F‖^+_(𝒴(α′)) ≤ C‖F‖;
  - |C(0)| ≤ C‖F‖ by lem:iii-i8-3-2, with the fixed pair;
  - |S⃗| ≤ C‖F‖;
  - ‖F(S⃗)‖_(𝒴(α″)) + ‖F(S⃗)‖^+_(𝒴(α′)) ≤ C‖F‖;
  - the rest as before.
- **Ch. 40, (ii) at α″ (40:1225–1232).**
  - The Φ_j converge in 𝒴(α″) ⊂ 𝒴(α′). So by (i) at α′, used for every target seminorm, the w_j are bounded in a
    seminorm two orders above ‖·‖^+_(𝒴(α′)).
  - The count of Step 0 in ‖·‖^+_(𝒴(α′)) gives R_j → 0 there.
  - Then ‖w_j − w‖_(α′) ≤ C‖R_j‖^+_(𝒴(α′)) → 0.
- **Ch. 41, the end of the proof of thm:iii-i11-4-1 (41:1034–1042). This changed for consistency.**
  - ‖·‖^+_(𝒴(α′)) is the seminorm of (i) at α′ for the ‖·‖_(α′) already chosen there.
  - ‖F‖ is "a seminorm of 𝒴⁰(α) of large enough regularity", bounding ‖F‖_(𝒴⁰(α)) and ‖F‖^+_(𝒴(α′)).
  - F(W⃗) is measured in ‖·‖^+_(𝒴(α′)).
  - The statement of the theorem is unchanged. So is the later use at 41:1459, which already reads these seminorms
    "for every choice of the seminorms of large enough regularity".
- **Ch. 44, step (4) of prop:iii-i15-2-5 (44:330–331, 44:359–361, 44:378). This changed for consistency.**
  - The bound is now |p⃗′_(α_1)(Ψ)| ≤ C‖Ψ‖^+_(𝒴(α_1)).
  - (2) bounds e_rows in that seminorm, which needs h and q small at a large enough order.
  - The display of (2) carries ^+.
  - The statement of prop:iii-i15-2-5 and eq:s25-motions-small are unchanged.

**Every proof is complete.** Every constant is as uniform as before, since the comparison constant of "The seminorms"
depends only on the regularities. No statement of 41–44 changes in substance.

**Explicit orders.** The text gives no explicit regularity for any of these seminorms, before or after the repair. So
no order was invented. The repair says only how the seminorms are related to each other (≥ +2, ≥ the one below) and
that d must cover them.

**The diff** (also saved as P-40-sem.diff beside this report):

```diff
diff --git a/research/warp-drive/paper/reader/chapters/40-s21-parameters.md b/research/warp-drive/paper/reader/chapters/40-s21-parameters.md
index a5043a42..47f1df67 100644
--- a/research/warp-drive/paper/reader/chapters/40-s21-parameters.md
+++ b/research/warp-drive/paper/reader/chapters/40-s21-parameters.md
@@ -736,10 +736,14 @@ parameter b ∈ ℬ̄_*, as throughout. 𝒴(α) is a Fréchet space, and bounds
 ‖·‖_(𝒴(α)): the quotient norm on 𝒴_1(α) + 𝒴_2(α) of the two defining spaces at one finite regularity and one ε > 0.
 The regularity is taken so large, and ε so small, that the linear maps used below, which are continuous on 𝒴(α)
 uniformly for (h, p⃗) small and b ∈ ℬ̄_* (in the proof of [[lem:iii-i8-3-2]], the maps from the forcing f′ of its
-Step 0 to the coefficients and to the remainder; and those of [[prop:iii-i8-4-1]] (i)), are bounded in this seminorm;
-and d is taken so large that the bounds of [[lem:iii-i8-2-6]] (b) and [[lem:s21-motions-at-b]] in it are bounds by
-‖h‖. In the same way ‖·‖_(α′) is one fixed seminorm of the space of the hypothesis of [[lem:iii-i8-3-2]] at the level
-α′.
+Step 0 to the coefficients and to the remainder), are bounded in this seminorm. In the same way ‖·‖_(α′) is one fixed
+seminorm of the space of the hypothesis of [[lem:iii-i8-3-2]] at the level α′, of regularity at least that of
+‖·‖_(𝒴(α)) plus 2, α the level above α′ there, as Step 0 of the proof of that lemma bounds (L − L_b)u in ‖·‖_(𝒴(α))
+by ‖u‖_(α′). The bounds of [[prop:iii-i8-4-1]] (i) are taken in a second seminorm ‖·‖^+_(𝒴(α)), the same quotient
+norm at a larger regularity and a smaller ε, fixed in its proof: its step bounds the solution at a lower level α′ in
+‖·‖_(α′) by (i) at α′, so its seminorm of the forcing must bound the seminorm of (i) at α′ as well as ‖·‖_(𝒴(α)). d
+is taken so large that the bounds by ‖h‖ used below hold in these seminorms: those of [[lem:iii-i8-2-6]] (b) and
+[[lem:s21-motions-at-b]], and the count of Step 0 of the proof of [[lem:iii-i8-3-2]].
 
 ### Corrections of the third kind and the operator {#sec:iii-i8-2}
 
@@ -1124,24 +1128,35 @@ satisfies
 
     u ∈ ⋂_(ε>0) H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β_+,α−2−ε)_b(Ω_*; S²T*)^(•,−)   for every β_+ < min(3/2, min Re ℰ_+). {#eq:iii-i8-4-2}
 
-Moreover (i) p⃗′_(h,p⃗) and F ↦ u are linear, with bounds uniform for (h, p⃗ − p⃗_b) small and b ∈ ℬ̄_*; (ii) at fixed
-b, if (h_j, p⃗_j) → (0, p⃗_b) and F_j → F in 𝒴(α), then p⃗′_(h_j,p⃗_j)(F_j) → p⃗′_(0,p⃗_b)(F). In compact spatial sets
-u = O(t_*^(−α+2+ε)), almost O(t_*⁻¹) as α → 3.
+Moreover (i) p⃗′_(h,p⃗) and F ↦ u are linear, with bounds uniform for (h, p⃗ − p⃗_b) small and b ∈ ℬ̄_*: for each fixed
+seminorm ‖·‖_(α) of the space of [[eq:iii-i8-4-2]] there are a seminorm ‖·‖^+_(𝒴(α)) of 𝒴(α), as in [[sec:iii-i8-1]],
+and C with |p⃗′_(h,p⃗)(F)| + ‖u‖_(α) ≤ C‖F‖^+_(𝒴(α)); (ii) at fixed b, if (h_j, p⃗_j) → (0, p⃗_b) and F_j → F in 𝒴(α),
+then p⃗′_(h_j,p⃗_j)(F_j) → p⃗′_(0,p⃗_b)(F). In compact spatial sets u = O(t_*^(−α+2+ε)), almost O(t_*⁻¹) as α → 3.
 
 *Proof.* Choose admissible α_0 < α_1 < ⋯ < α_n = α with α_0 ∈ (2, min(a_K, 2 + ε_g, 5/2)) and
 α_(i+1) − α_i < a_K − 2 (the excluded set is finite). By induction on i we prove the statement, with (i)–(ii), at α_i.
 Write p⃗′_(h,p⃗,α_i) for the map at the level α_i.
 
 *Base.* ℳ_(α_0) = ∅, as Re λ − 1 ≥ λ_♯ − 1 > 1/2 > α_0 − 2. By [[lem:iii-i8-3-1]], [[cor:iii-i7-4-6]] gives existence,
-uniqueness and linearity. The bounds are uniform by [[lem:iii-i7-2-5]] (c) and [[prop:iii-i15-2-12]], the
-finite-dimensional maps inverted in [[lem:iii-i7-4-3]] and [[lem:iii-i7-4-5]] lying within
+uniqueness and linearity. Its maps are continuous on 𝒴(α_0), so each fixed seminorm of their values is bounded by a
+seminorm ‖·‖^+_(𝒴(α_0)) of 𝒴(α_0), as (i) states. The bounds are uniform by [[lem:iii-i7-2-5]] (c) and
+[[prop:iii-i15-2-12]], the finite-dimensional maps inverted in [[lem:iii-i7-4-3]] and [[lem:iii-i7-4-5]] lying within
 C(‖h‖ + |p⃗ − p⃗_b| + |b − b₀|) of ±id; and (ii) holds as those maps converge at fixed b (by their construction and
 [[lem:iii-i7-4-1]], which allows forcings varying with j).
 
 *Step.* Let the statement hold at α′ := α_i, and let α″ := α_(i+1), ℳ′ := ℳ_(α″) ∖ ℳ_(α′) and
-F ∈ 𝒴(α″) ⊂ 𝒴(α′). For S⃗ = (S_ν)_(ν∈ℳ′) conjugation-symmetric ([[sec:iii-i8-1]]; the map T_(h,p⃗) below preserves
-these, L_(h,p⃗) and F being real) put F(S⃗) := F − Σ_(ν∈ℳ′) f^ν_(h,p⃗)(S_ν) ∈ 𝒴(α″) ([[lem:iii-i8-2-6]] (b)), and let
-u(S⃗) be the forward solution of
+F ∈ 𝒴(α″) ⊂ 𝒴(α′).
+
+*The seminorms.* Fix the seminorm ‖·‖_(α″) of (i) at α″. Take ‖·‖_(𝒴(α″)) and ‖·‖_(α′) as in [[sec:iii-i8-1]] for
+[[lem:iii-i8-3-2]] at the levels α′ < α″, with the remainder in ‖·‖_(α″); let ‖·‖^+_(𝒴(α′)) be the seminorm of (i) at
+α′ for ‖·‖_(α′), and ‖·‖^+_(𝒴(α″)) the quotient norm of [[sec:iii-i8-1]] on 𝒴(α″) at a regularity at least those of
+‖·‖_(𝒴(α″)) and ‖·‖^+_(𝒴(α′)) and an ε at most theirs. On 𝒴(α″) it bounds ‖·‖_(𝒴(α″)), and ‖·‖^+_(𝒴(α′)) up to a
+constant: each defining space at α″ lies in the one at α′, its norm bounding that at a lower regularity and a larger
+ε, as the K⁺-weight α″ exceeds α′.
+
+For S⃗ = (S_ν)_(ν∈ℳ′) conjugation-symmetric ([[sec:iii-i8-1]]; the map T_(h,p⃗) below preserves these, L_(h,p⃗) and F
+being real) put F(S⃗) := F − Σ_(ν∈ℳ′) f^ν_(h,p⃗)(S_ν) ∈ 𝒴(α″) ([[lem:iii-i8-2-6]] (b)), and let u(S⃗) be the forward
+solution of
 
     L_(h,p⃗)u(S⃗) = G(S⃗) := F(S⃗) − D_p⃗P_3(h, p⃗)(p⃗′_(h,p⃗,α′)(F(S⃗))) ∈ 𝒴(α″),
 
@@ -1159,15 +1174,15 @@ solution of L_(h,p⃗)u = G_1(S⃗) is Σ_ν m_ν(S_ν) + v(S⃗), where v(S⃗)
 
     L_(h,p⃗)v(S⃗) = R(S⃗) := Σ_ν e^ν_(h,p⃗)(S_ν) − D_p⃗P_3(h, p⃗)(p⃗′_(h,p⃗,α′)(Σ_ν e^ν_(h,p⃗)(S_ν))).
 
-By [[lem:s21-motions-at-b]] (α″ < min(a_K, 3)) and (i) at α′, ‖R(S⃗)‖_(𝒴(α″)) ≤ C(‖h‖ + |p⃗ − p⃗_b| + |b − b₀|)|S⃗|.
-The forward solution of G_1(S⃗) = G(0) − G(S⃗) is u(0) − u(S⃗), which lies in [[eq:iii-i8-4-2]] at α′, and so does
-Σ_ν m_ν(S_ν); hence v(S⃗) = u(0) − u(S⃗) − Σ_ν m_ν(S_ν) satisfies the hypothesis of [[lem:iii-i8-3-2]]. Moreover
-‖v(S⃗)‖_(α′) ≤ C|S⃗|: u(0) − u(S⃗) is the solution of [[eq:iii-i8-4-1]] at α′ for the forcing Σ_ν f^ν_(h,p⃗)(S_ν), of
-norm at most C|S⃗| by [[lem:iii-i8-2-6]] (b), so (i) at α′ bounds it by C|S⃗|, and ‖m_ν(S_ν)‖_(α′) ≤ C|S_ν| by
-[[lem:iii-i8-2-2]]. The coefficients of [[lem:iii-i8-3-2]] are read from the forcing f′ = R(S⃗) − (L_(h,p⃗) − L_b)v(S⃗)
-of Step 0 of its proof by maps fixed by L_b, and the count of that step gives
-‖(L_(h,p⃗) − L_b)v(S⃗)‖_(𝒴(α″)) ≤ C(‖h‖ + |p⃗|)‖v(S⃗)‖_(α′), the coefficients of L_(h,p⃗) − L_b having size
-O(‖h‖ + |p⃗|). So the coefficients of v(S⃗) satisfy
+By [[lem:s21-motions-at-b]] (α″ < min(a_K, 3)), in ‖·‖_(𝒴(α″)) and in ‖·‖^+_(𝒴(α′)) ([[sec:iii-i8-1]]), and (i) at α′,
+‖R(S⃗)‖_(𝒴(α″)) ≤ C(‖h‖ + |p⃗ − p⃗_b| + |b − b₀|)|S⃗|. The forward solution of G_1(S⃗) = G(0) − G(S⃗) is u(0) − u(S⃗),
+which lies in [[eq:iii-i8-4-2]] at α′, and so does Σ_ν m_ν(S_ν); hence v(S⃗) = u(0) − u(S⃗) − Σ_ν m_ν(S_ν) satisfies
+the hypothesis of [[lem:iii-i8-3-2]]. Moreover ‖v(S⃗)‖_(α′) ≤ C|S⃗|: u(0) − u(S⃗) is the solution of [[eq:iii-i8-4-1]]
+at α′ for the forcing Σ_ν f^ν_(h,p⃗)(S_ν), of norm at most C|S⃗| in ‖·‖^+_(𝒴(α′)) by [[lem:iii-i8-2-6]] (b), so (i) at
+α′ bounds it by C|S⃗|, and ‖m_ν(S_ν)‖_(α′) ≤ C|S_ν| by [[lem:iii-i8-2-2]]. The coefficients of [[lem:iii-i8-3-2]] are
+read from the forcing f′ = R(S⃗) − (L_(h,p⃗) − L_b)v(S⃗) of Step 0 of its proof by maps fixed by L_b, and the count of
+that step gives ‖(L_(h,p⃗) − L_b)v(S⃗)‖_(𝒴(α″)) ≤ C(‖h‖ + |p⃗|)‖v(S⃗)‖_(α′), the coefficients of L_(h,p⃗) − L_b having
+size O(‖h‖ + |p⃗|). So the coefficients of v(S⃗) satisfy
 
     |S^(h,p⃗)(R(S⃗))| ≤ C‖R(S⃗)‖_(𝒴(α″)) + C(‖h‖ + |p⃗|)‖v(S⃗)‖_(α′) ≤ C(‖h‖ + |p⃗ − p⃗_b| + |b − b₀|)|S⃗|,
 
@@ -1184,14 +1199,15 @@ lies in [[eq:iii-i8-4-2]] at α″. *Uniqueness:* if p⃗″ ∈ 𝒫_(α″) al
 then its solution lies in [[eq:iii-i8-4-2]] at α′ with the forcing F(S⃗″) − D_p⃗P_3(h, p⃗)(q⃗), q⃗ ∈ 𝒫_(α′), so
 q⃗ = p⃗′_(h,p⃗,α′)(F(S⃗″)) by uniqueness at α′, the solution is u(S⃗″), and C(S⃗″) = 0 gives S⃗″ = S⃗.
 
-*(i) at α″.* Linearity holds by construction. Write ‖F‖ := ‖F‖_(𝒴(α″)). By (i) at α′ and [[lem:iii-i8-2-6]],
-‖G(0)‖_(𝒴(α″)) ≤ C‖F‖, and u(0), the solution of [[eq:iii-i8-4-1]] at α′ for the forcing F, has ‖u(0)‖_(α′) ≤ C‖F‖;
-so the bound of [[lem:iii-i8-3-2]] gives |C(0)| ≤ C‖F‖, and |S⃗| ≤ 2|C(0)| ≤ C‖F‖. Then ‖F(S⃗)‖_(𝒴(α″)) ≤ C‖F‖
-([[lem:iii-i8-2-6]] (b)), and (i) at α′, with [[lem:iii-i8-2-6]] for G(S⃗), bounds p⃗′_(h,p⃗,α′)(F(S⃗)), G(S⃗) and
-u(S⃗), the solution of [[eq:iii-i8-4-1]] at α′ for F(S⃗), by C‖F‖ in 𝒫_(α′), 𝒴(α″) and ‖·‖_(α′).
-So |p⃗′_(h,p⃗,α″)(F)| ≤ C‖F‖, and the bound of [[lem:iii-i8-3-2]] on the remainder, which is u(S⃗) itself, gives
-‖u(S⃗)‖_(α″) ≤ C‖F‖. The constants are uniform for (h, p⃗ − p⃗_b) small and b ∈ ℬ̄_*, as those of (i) at α′, of
-[[lem:iii-i8-3-2]] and the bound on T_(h,p⃗)⁻¹ are.
+*(i) at α″.* Linearity holds by construction. Write ‖F‖ := ‖F‖^+_(𝒴(α″)), which bounds ‖F‖_(𝒴(α″)), and
+‖F‖^+_(𝒴(α′)) up to a constant (*The seminorms*). By (i) at α′ and [[lem:iii-i8-2-6]], ‖G(0)‖_(𝒴(α″)) ≤ C‖F‖, and
+u(0), the solution of [[eq:iii-i8-4-1]] at α′ for the forcing F, has ‖u(0)‖_(α′) ≤ C‖F‖^+_(𝒴(α′)) ≤ C‖F‖; so the
+bound of [[lem:iii-i8-3-2]] gives |C(0)| ≤ C‖F‖, and |S⃗| ≤ 2|C(0)| ≤ C‖F‖. Then
+‖F(S⃗)‖_(𝒴(α″)) + ‖F(S⃗)‖^+_(𝒴(α′)) ≤ C‖F‖ ([[lem:iii-i8-2-6]] (b)), and (i) at α′, with [[lem:iii-i8-2-6]] for G(S⃗),
+bounds p⃗′_(h,p⃗,α′)(F(S⃗)), G(S⃗) and u(S⃗), the solution of [[eq:iii-i8-4-1]] at α′ for F(S⃗), by C‖F‖ in 𝒫_(α′),
+𝒴(α″) and ‖·‖_(α′). So |p⃗′_(h,p⃗,α″)(F)| ≤ C‖F‖, and the bound of [[lem:iii-i8-3-2]] on the remainder, which is u(S⃗)
+itself, gives ‖u(S⃗)‖_(α″) ≤ C‖F‖. The constants are uniform for (h, p⃗ − p⃗_b) small and b ∈ ℬ̄_*, as those of (i) at
+α′, of [[lem:iii-i8-3-2]] and the bound on T_(h,p⃗)⁻¹ are, and that of the comparison of the seminorms.
 
 *(ii) at α″, at fixed b.* Let (h_j, p⃗_j) → (0, p⃗_b) and F_j → F in 𝒴(α″). Write T_j, C_j for the objects above at
 (h_j, p⃗_j) with the forcing F_j, and T, C for those at (0, p⃗_b) with F. We first show: *if Φ_j → Φ in 𝒴(α″), and w_j,
@@ -1206,12 +1222,14 @@ D_p⃗P_3(h, p⃗) is linear in the direction, bounded uniformly and continuous
 
     L_(0,p⃗_b)(w_j − w) = R_j := Ψ_j − Ψ − (L_(h_j,p⃗_j) − L_(0,p⃗_b))w_j.
 
-The w_j are bounded in ‖·‖_(α′) by (i) at α′, and the coefficients of L_(h_j,p⃗_j) − L_(0,p⃗_b) have norm
-O(‖h_j‖ + |p⃗_j − p⃗_b|) and gain a_K near K⁺, where both backgrounds are g_b; so the count of Step 0 of the proof of
-[[lem:iii-i8-3-2]] gives ‖(L_(h_j,p⃗_j) − L_(0,p⃗_b))w_j‖_(𝒴(α″)) → 0, and R_j → 0 in 𝒴(α″) ⊂ 𝒴(α′); R_j is real.
-w_j − w lies in [[eq:iii-i8-4-2]] at α′, as w_j and w do. So p⃗′ = 0 has, for (0, p⃗_b) and the forcing R_j, the
-property of the statement at α′; by uniqueness at α′, p⃗′_(0,p⃗_b,α′)(R_j) = 0 and w_j − w is the solution of
-[[eq:iii-i8-4-1]] at α′ for R_j, and (i) at α′ gives ‖w_j − w‖_(α′) ≤ C‖R_j‖_(𝒴(α′)) → 0.
+The Φ_j converge in 𝒴(α″) ⊂ 𝒴(α′), so, by (i) at α′, the w_j are bounded in each fixed seminorm of the space of
+[[eq:iii-i8-4-2]] at α′, among them one of regularity two above that of ‖·‖^+_(𝒴(α′)). The coefficients of
+L_(h_j,p⃗_j) − L_(0,p⃗_b) have norm O(‖h_j‖ + |p⃗_j − p⃗_b|) and gain a_K near K⁺, where both backgrounds are g_b; so the
+count of Step 0 of the proof of [[lem:iii-i8-3-2]], in ‖·‖^+_(𝒴(α′)), gives (L_(h_j,p⃗_j) − L_(0,p⃗_b))w_j → 0 there,
+and R_j → 0 in ‖·‖^+_(𝒴(α′)), with R_j ∈ 𝒴(α″) ⊂ 𝒴(α′) real. w_j − w lies in [[eq:iii-i8-4-2]] at α′, as w_j and w
+do. So p⃗′ = 0 has, for (0, p⃗_b) and the forcing R_j, the property of the statement at α′; by uniqueness at α′,
+p⃗′_(0,p⃗_b,α′)(R_j) = 0 and w_j − w is the solution of [[eq:iii-i8-4-1]] at α′ for R_j, and (i) at α′ gives
+‖w_j − w‖_(α′) ≤ C‖R_j‖^+_(𝒴(α′)) → 0.
 
 For fixed S⃗ take Φ_j := Σ_ν f^ν_(h_j,p⃗_j)(S_ν) and Φ := Σ_ν f^ν_(0,p⃗_b)(S_ν), so that Φ_j → Φ ([[lem:iii-i8-2-6]]
 (c)); then Ψ_j and Ψ are G_1(S⃗) at (h_j, p⃗_j) and at (0, p⃗_b), and w_j, w their forward solutions, so
diff --git a/research/warp-drive/paper/reader/chapters/41-s22-kerr-face.md b/research/warp-drive/paper/reader/chapters/41-s22-kerr-face.md
index 64d8a3a7..1270af73 100644
--- a/research/warp-drive/paper/reader/chapters/41-s22-kerr-face.md
+++ b/research/warp-drive/paper/reader/chapters/41-s22-kerr-face.md
@@ -1031,14 +1031,15 @@ F are real and T commutes with the conjugation of [[sec:iii-i9-1]].
 
 *Uniqueness.* If p⃗″ also gives [[eq:iii-i11-4-2]] at α, its solution lies in [[eq:iii-i8-4-2]] at α′, so its
 𝒫_(α′)-part is q⃗(W⃗″) by the uniqueness at α′ ([[prop:iii-i8-4-1]]), where W⃗″ is its 𝒩′-part; then C(W⃗″) = 0, so
-W⃗″ = W⃗. *Linearity, bounds, continuity:* linearity holds by construction. Write ‖F‖ := ‖F‖_(𝒴⁰(α)); F lies in
-𝒴(α′) with ‖F‖_(𝒴(α′)) ≤ C‖F‖. By [[prop:iii-i8-4-1]] (i) at α′, |q⃗(0)| ≤ C‖F‖ and ‖u(0)‖_(α′) ≤ C‖F‖, with the
-seminorm ‖·‖_(α′) taken as above; so ‖G(0)‖_(𝒴⁰(α)) ≤ C‖F‖ and, as above, ‖u_0(0)‖_(w_0) ≤ C‖F‖. The bound of
-[[lem:iii-i11-3-2]] then gives |C(0)| ≤ C‖F‖, so |W⃗| ≤ 2|C(0)| ≤ C‖F‖, and (i) at α′ for the forcing F(W⃗), of size at
-most C‖F‖ in 𝒴(α′), gives |q⃗(W⃗)| ≤ C‖F‖ and ‖u(W⃗)‖_(α′) ≤ C‖F‖. So |p⃗′_(h,p⃗)(F)| ≤ C‖F‖, and likewise
-‖G(W⃗)‖_(𝒴⁰(α)) ≤ C‖F‖ and ‖u_0(W⃗)‖_(w_0) ≤ C‖F‖, with C uniform for (h, p⃗) small. Continuity at
-(0, 0) as in [[prop:iii-i8-4-1]] (ii), with [[lem:iii-i11-3-3]] at b_0, whose hypothesis (the solutions u_0 bounded)
-these bounds give. ∎
+W⃗″ = W⃗. *Linearity, bounds, continuity:* linearity holds by construction. With the seminorm ‖·‖_(α′) taken as
+above, let ‖·‖^+_(𝒴(α′)) be the seminorm of [[prop:iii-i8-4-1]] (i) at α′ for it, and write ‖F‖ for a seminorm of
+𝒴⁰(α) of large enough regularity ([[sec:iii-i8-1]]): it bounds ‖F‖_(𝒴⁰(α)), and F lies in 𝒴(α′) with
+‖F‖^+_(𝒴(α′)) ≤ C‖F‖. By (i) at α′, |q⃗(0)| ≤ C‖F‖ and ‖u(0)‖_(α′) ≤ C‖F‖; so ‖G(0)‖_(𝒴⁰(α)) ≤ C‖F‖ and, as
+above, ‖u_0(0)‖_(w_0) ≤ C‖F‖. The bound of [[lem:iii-i11-3-2]] then gives |C(0)| ≤ C‖F‖, so |W⃗| ≤ 2|C(0)| ≤ C‖F‖,
+and (i) at α′ for the forcing F(W⃗), of size at most C‖F‖ in ‖·‖^+_(𝒴(α′)), gives |q⃗(W⃗)| ≤ C‖F‖ and
+‖u(W⃗)‖_(α′) ≤ C‖F‖. So |p⃗′_(h,p⃗)(F)| ≤ C‖F‖, and likewise ‖G(W⃗)‖_(𝒴⁰(α)) ≤ C‖F‖ and ‖u_0(W⃗)‖_(w_0) ≤ C‖F‖, with
+C uniform for (h, p⃗) small. Continuity at (0, 0) as in [[prop:iii-i8-4-1]] (ii), with [[lem:iii-i11-3-3]] at b_0,
+whose hypothesis (the solutions u_0 bounded) these bounds give. ∎
 
 At a base point with black hole parameter b ∈ ℬ̄_*, the elimination is [[prop:iii-i15-2-5]] with q = 0: when
 h_(b,v1) ≠ 0 the v1 terms u^rot of [[lem:iii-i11-3-2]] are not removed by the parameters of 𝒫, whose v1 rows carry the
diff --git a/research/warp-drive/paper/reader/chapters/44-s25-base-points.md b/research/warp-drive/paper/reader/chapters/44-s25-base-points.md
index cb098e38..702166e1 100644
--- a/research/warp-drive/paper/reader/chapters/44-s25-base-points.md
+++ b/research/warp-drive/paper/reader/chapters/44-s25-base-points.md
@@ -327,10 +327,11 @@ are used below are at most C(‖F‖ + |W⃗_free|), C uniform in b and in (h, p
 with p⃗′_<-component 0 and row components W⃗ = (W_ν)_(ν∈𝒩′⊔𝒩_rot) (the split below), as in Step 1. For Ψ ∈ 𝒴(α_1) let
 p⃗′_(α_1)(Ψ) ∈ 𝒫_(α_1) be the parameter that [[prop:iii-i8-4-1]], for P_5 at (h, p⃗, q) (Step 1), assigns to the forcing
 Ψ: the unique one for which the forward solution u_Ψ of L_(h″,p⃗)u_Ψ = Ψ − D_(p⃗)P_5(h, p⃗, q)(p⃗′_(α_1)(Ψ)) lies in
-𝒵_(α_1). By (i) of that proposition, Ψ ↦ p⃗′_(α_1)(Ψ) is linear and |p⃗′_(α_1)(Ψ)| ≤ C‖Ψ‖_(𝒴(α_1)), with C uniform in b
-and in (h, p⃗, q) small. A point of 𝒫 is p⃗′_< ⊕ W⃗, with p⃗′_< ∈ 𝒫_(α_1) (the motion coordinates and the motions of
-ℳ_(α_1)) and W⃗ = (W_ν)_(ν∈𝒩′⊔𝒩_rot) the other row coordinates (Step 1). By [[eq:iii-i14-3-1]] and the linearity of
-D_(p⃗)P_5(h, p⃗, q) in the direction, u(p⃗′_< ⊕ W⃗) is the forward solution of
+𝒵_(α_1). By (i) of that proposition, Ψ ↦ p⃗′_(α_1)(Ψ) is linear and |p⃗′_(α_1)(Ψ)| ≤ C‖Ψ‖^+_(𝒴(α_1)), with
+‖·‖^+_(𝒴(α_1)) the seminorm of that (i) and C uniform in b and in (h, p⃗, q) small. A point of 𝒫 is p⃗′_< ⊕ W⃗, with
+p⃗′_< ∈ 𝒫_(α_1) (the motion coordinates and the motions of ℳ_(α_1)) and W⃗ = (W_ν)_(ν∈𝒩′⊔𝒩_rot) the other row
+coordinates (Step 1). By [[eq:iii-i14-3-1]] and the linearity of D_(p⃗)P_5(h, p⃗, q) in the direction, u(p⃗′_< ⊕ W⃗) is
+the forward solution of
 
     L_(h″,p⃗)u = (F − D_(W⃗)P_5(W⃗)) − D_(p⃗)P_5(h, p⃗, q)(p⃗′_<),
 
@@ -355,8 +356,10 @@ m_ν(W)), and D_(W⃗)P_5(W⃗) is real; so e_rows(W⃗) is real.
 
 (2) *The remainder is small.* The class 𝒴(α_1) contains the class 𝒴_2(α_1) of [[sec:iii-i8-1]], which holds every
 conormal section supported in supp χ_K ⊂ supp χ^♯_K ([[eq:iii-i-1-2]]) of K⁺-weight above α_1 and plain ι⁺-weight
-above 4 (below the weight 4 − ε its ι⁺-index set ℰ_++ + 2 is then not used); the 𝒴(α_1)-norm of such a section is at
-most a seminorm of it in those weights. The four kinds of terms of e_rows(W⃗):
+above 4 (below the weight 4 − ε its ι⁺-index set ℰ_++ + 2 is then not used); the seminorm ‖·‖^+_(𝒴(α_1)) of such a
+section is at most a seminorm of it in those weights at the same regularity, and the bounds below hold in that
+seminorm, d and the order of the seminorm of q being large ([[sec:iii-i8-1]], [[sec:iii-i14-1]]). The four kinds of
+terms of e_rows(W⃗):
 
 - r^ν_(h,p⃗)(W) is supported in supp χ_K and lies in the class [[eq:iii-i9-2-5]], of plain ι⁺-weight
   Re λ + 2 + λ_♯ − ε > 4 and K⁺-weight Re e_ν + a_K − ε > α_1, with norm at most C|W|(‖h‖ + |p⃗|), uniformly on ℬ̄_*
@@ -372,7 +375,7 @@ most a seminorm of it in those weights. The four kinds of terms of e_rows(W⃗):
 
 So, as |p⃗| ≤ |p⃗ − p⃗_b| + |p⃗_b| = |p⃗ − p⃗_b| + |b − b₀|,
 
-    ‖e_rows(W⃗)‖_(𝒴(α_1)) ≤ C(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b₀|)|W⃗|,     C uniform in b.
+    ‖e_rows(W⃗)‖^+_(𝒴(α_1)) ≤ C(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b₀|)|W⃗|,     C uniform in b.
 
 (3) *The rows carry no parameter.* m_rows(W⃗) vanishes for t^♭_* < 10 ([[lem:iii-i9-2-2]] (c)), so it is the forward
 solution of L_(h″,p⃗)u = L_(h″,p⃗)m_rows(W⃗) (Step 0). It lies in 𝒵_(α_1). Every row of 𝒩′ has K⁺-rate above
```

## 3. Uses checked

These are every citation of prop:iii-i8-4-1, found with grep, and every use of the fixed seminorms of sec:iii-i8-1.

**Chapter 40.**

- 40:19, 66, 77, 446, 573, 631 and 1673 are prose, or the base step through prop:iii-i15-2-12. No seminorm is involved,
  and none needs a change.
- lem:iii-i8-3-2 and lem:iii-i8-3-3 use only the fixed pair (‖·‖_(𝒴(α)), ‖·‖_(α′)). They are unchanged and consistent.
- lem:s21-motions-at-b is unchanged. The setting now asks its bound to hold in ‖·‖^+ as well, through d.

**Chapter 41.**

- **41:67.** Prose. No change.
- **41:918–936, lem:iii-i11-3-3.** It uses (i) at α′ for a target ‖·‖_(α′) that it chooses itself ("We take that
  seminorm … regularity at least that of ‖·‖_(w)"), and it needs R_j → 0 in 𝒴(α′). There the u_j are bounded in the
  hypothesis space, so R_j → 0 in the Fréchet topology, and hence in ‖·‖^+. No change.
- **41:963, 1014, 1040.** These use (ii), and the continuity of (ii) is unchanged. No change.
- **41:970–979, "prop:iii-i8-4-1 for P_4".** The extra term is O(|W⃗|) in every seminorm. No change.
- **41:1023–1027, "Near (0, 0)".** The forcing is O(|W⃗|) in 𝒴(α′) in the Fréchet sense, and the target is chosen as
  in lem:iii-i11-3-3. No change.
- **41:1034–1042. Edited**, as in section 2.
- **41:1618, lem:iii-i13-2-3.** Same as lem:iii-i11-3-3. No change.
- **41:1626, prop:iii-i13-2-4.** No seminorm. No change.
- **41:864–868, 1452–1459, 1588, 1719–1720.** The seminorms "chosen as in sec:iii-i8-1", or "depending on the seminorm
  bounded (of large enough regularity, as in sec:iii-i8-1)". They are consistent with the new setting. No change.

**Chapter 42.**

- **42:143.** "q small … in one fixed seminorm of large order". This is unchanged. "Large" must now also cover the
  bounds of R_q m_rows and Δ_q in ‖·‖^+_(𝒴(α_1)) (44:359–361).
- **42:402–416, Step 1.** This is a transfer of prop:iii-i8-4-1 to P_5, with terms that are O(|W⃗| + ‖q‖). No change.
- **42:454–457.** Uses (ii), and says "each losing finitely many derivatives". No change.

**Chapter 43.**

- **43:213 and 43:378.** Inventory lists. No change.
- **43:304–305, lem:iii-j2-2-3.** "[[ch:s21]] fixes h small as small in 𝒳^d, d fixed, … the same convention for
  prop:iii-i8-4-1 and T_(h,p⃗)". This is still true, as d is fixed by sec:iii-i8-1 to cover ‖·‖^+ too. The value of d
  may be larger than the fixed seminorms alone would ask. Chapters 40–44 state no value for it, so no statement moves.

**Chapter 44.**

- **44:324**, the induction bound at k = 0. It is already stated with "‖F‖ … of large enough regularity". No change.
- **44:328–331. Edited.**
- **44:359–378, step (2). Edited.**
- **44:380–393, steps (3)–(4).** They use uniqueness, and the bound of (i), which is now consistent with (2). No change.
- **44:505–507, 599, 641.** Lists, and the continuity used at fixed b. No change.
- **44:681, 699.** "E^ν … in a fixed seminorm" and "both in fixed seminorms, so d_* is unchanged". These concern the
  direct bound of Step 3 and lem:iii-i15-2-4, which use the fixed seminorms of the reads. No change.

**Chapter 46 (not edited).**

- **46:1386.** Here the defect terms e_S(S′) + e_(S⁰)(S⁰′) are asked small "in the fixed seminorm in which the proof of
  lem:iii-j2-2-3 asks such terms small", with m its order and d ≥ m + 5. The same terms are said to perturb Step 1, the
  base level, "by terms of the same kind, small with them".
- After the repair it is explicit that, at the base level, the parameter map bounds them in ‖·‖^+_(𝒴(α_1)). So this
  needs d ≥ (regularity of ‖·‖^+_(𝒴(α_1))) + 5, or that regularity ≤ m.
- The original text had the same unstated requirement, with ‖·‖_(𝒴(α_1)) in place of ‖·‖^+, so this is not new.
- Under the orders of proofs/P-U71-small.md, the base orders are ≤ 2R_base + 16, far below the read orders ~C_lev. So
  it holds there. But chapter 46 does not say so. Its owner may want a clause, for example "m at least the order of the
  seminorms of the base level".

**Chapter 71 (not edited).**

- **71:1757, 1831, 1899, 2300, 2336, 3859, 3879, 4195, 4239, 4250.** These count *charges along chains*: the level step
  α_0 → α_1, "the sources f^ν and D_p⃗P_3 (11), the inverse T⁻¹ (0), and lem:iii-i8-3-2 from α_0 to α_1 … 508", and the
  base with I_base. They never claim that (i) is lossless or bounded in one fixed seminorm.
- The repaired (i) is a bound with exactly the loss that chapter 71 charges. So no loss and no figure of chapter 71
  moves.
- The repair also matches lem:uc-small-orders (c) of proofs/P-U71-small.md. That passage already reads (i) as "a base
  map, from the forcing at the order of the seminorm plus 2 + R_base", and asks the bounds of lem:iii-i8-2-6 (b) and
  lem:s21-motions-at-b "in these norms" at regularities ≤ 2R_base + 2.
  - The repaired proof asks e^ν small in ‖·‖^+_(𝒴(α_0)). That seminorm has regularity at most
    reg ‖·‖_(𝒴(α_1)) + 2 + (base loss), which is within that bound.
  - So 2R_base + 16, D_*, D′_* and the bounds on d_NM stand.

**A finding of the same shape outside the report's point (not edited).** The proof of prop:iii-i15-2-12, (2)
(40:586–613), has the same structure with the fixed norm ‖·‖_𝒴 of sec:iii-i7-4, "fixed once and for all".

- It bounds ‖(L_(h,p⃗) − L_(0,p⃗_b))u_1‖_(𝒴^S_(α,α_+)) and ‖(L_(h,p⃗) − L_(0,p⃗_b))u_1‖_𝒴 by C(‖h‖ + |p⃗ − p⃗_b|)‖F_1‖_𝒴.
- Here u_1 is bounded by F_1 through the forward solution map (lem:iii-i7-2-5 (c)), and 𝒴^S is "normed in the same
  way". So the right side needs ‖F_1‖ at a regularity above that of ‖·‖_𝒴, by R1 and R2.
- The statement of prop:iii-i15-2-12, the finite-dimensional bounds eq:iii-i15-2-8, is unaffected. (2) is applied only
  to the smooth sources f^S_(0,p⃗_b)(S′) and F_(h,p⃗)(p⃗′^(=0)), whose norms at any finite regularity are O(|S′|) and
  O(|p⃗′^(=0)|) for d large.
- The least repair is to read ‖F‖_𝒴 and ‖F_1‖_𝒴, where they multiply (‖h‖ + |p⃗ − p⃗_b|), in a norm ‖·‖′_𝒴 of the same
  kind at a regularity larger by 2 plus the loss of lem:iii-i7-2-5 (c), with d large enough for it.
- I did not make this edit. It is not the gap I was given, it is a different fixed norm, and no use of
  prop:iii-i8-4-1 depends on more than the statement of prop:iii-i15-2-12. It can be done as a two-phrase edit in (2).
- lem:iii-i7-4-1 is fine if "F_j → F in 𝒴" is read in the Fréchet topology, as its uses provide.

## 4. Verdict on point 1

The text does not settle on (b) as its reading of the "fixed seminorm of large order". It supports (a) for what the
fixed seminorms are: the seminorms in which finite-dimensional coefficients or parameters are read and smallness is
asked. Every bound of a solution or remainder is then carried with a loss, in a seminorm of the data "of large enough
regularity". That is a third form, which the report's (a) and (b) only half-describe. It reduces to (a) for the orders
of the smallness conditions. The literal (b) occurs in one clause of chapter 40, and after the repair its effect is
confined to the levels of one application of prop:iii-i8-4-1.

**Evidence for (a) and for the loss carried by the data.**

- **43:315–317, lem:iii-j2-2-3.** This is the lemma that defines d_*. It reads "with S^(0,0)_ν bounded by one fixed
  seminorm ([[lem:iii-j2-2-1]] (c)), so they need R_j → 0 only in that seminorm … with u_j bounded at a fixed order".
  The fixed seminorm is the one the coefficient functional reads, and the solutions are bounded separately.
- **43:219, lem:iii-j2-2-1 (c).** The coefficient functionals are "bounded by a fixed low norm of the solution or right
  side they are applied to".
- **44:320–323, prop:iii-i15-2-5.** "‖·‖_(𝒴,k) for the seminorm of 𝒴^♮(β_k) of lem:iii-i13-2-2 … and ‖F‖ for a
  seminorm of F in 𝒴^♮(α − ε), of large enough regularity"; "the seminorms of u(p⃗′) in 𝒵_(β_k) that are used below are
  at most C(‖F‖ + |W⃗_free|)".
- **44:453.** "each level losing finitely many derivatives". The growth from level to level sits in ‖F‖, not in
  ‖·‖_(𝒴,k).
- **42:456–457, thm:iii-i14-3-1.** "u(p⃗′) is bounded in 𝒵_(β_k) … by the induction (finitely many levels, each losing
  finitely many derivatives)".
- **41:864–868, lem:iii-i11-3-2.** The "one fixed seminorm of 𝒴⁰(α)" bounds only |S_ν| + |u^rot|. The remainder bounds
  of thm:iii-i12-3-1 (41:1452–1455) take "a seminorm of 𝒴⁰(α) … depending on the seminorm bounded (of large enough
  regularity, as in sec:iii-i8-1)". The same form is at 41:1719–1720, and at 41:1459 "for every choice of the
  seminorms of large enough regularity".
- **After the repair, 40:1131–1133.** prop:iii-i8-4-1 (i) has the same form: a bound by ‖F‖^+_(𝒴(α)), "depending on"
  the target seminorm.

**Evidence for (b).**

- **40:737–739, sec:iii-i8-1.** It still reads: "the maps from the forcing f′ of its Step 0 to the coefficients *and to
  the remainder* … are bounded in this seminorm".
- **40:990, lem:iii-i8-3-2.** It bounds ‖ũ‖_(α) by C‖F‖_(𝒴(α)) + C(‖h‖ + |p⃗|)‖u‖_(α′), in the same seminorm as the
  coefficients.
- I kept both, because changing them would change the statement of lem:iii-i8-3-2. Together they force a downward
  choice within one induction: y_(i+1) ≥ n_(i+1) + loss and n_i ≥ y_(i+1) + 2.
- After the repair this choice is made only inside prop:iii-i8-4-1, over its own levels α_0 < ⋯ < α_n. At the
  computational point there is one level step α_0 → α_1 (ch. 71, lem:ec-counts and def:cs-choices (f)), so the
  accumulation is a single step.
- **44:453–455, Step 3 of prop:iii-i15-2-5.** This is the one place in the long induction where (b) can still be read.
  It bounds f′ in the fixed ‖·‖_(𝒴,k+1) before passing to ũ "losing finitely many derivatives". Read with the count of
  Step 0 at the regularity the next level needs (the count holds at every regularity) and with the induction bound for
  u_0, it is the loss form. Read literally, with ũ bounded from ‖·‖_(𝒴,k+1), it is (b) across the levels β_k, which is
  rem:uc-small-reading's D′_*.
- The text does not force the literal reading there, and the other passages of chapters 43–44 (43:315–317, 44:320–323)
  choose the loss form.

So proofs/P-U71-small.md is right to make (a) its main reading. Its rem:uc-small-reading covers the literal reading of
40:737–739 and 44:453–455, and both readings give d_NM < D_acc, so the printed numbers do not depend on the choice. A
one-clause change would make the text unambiguous. In 44:453–455, it would say that the count is taken at the
regularity that the next level needs. In sec:iii-i8-1, it would say that the fixed seminorm need bound the remainder
only into the target of the step at hand. I did not make these changes: the second would alter what lem:iii-i8-3-2
states, and that is to be reported, not made.

## 5. Check outputs

After all edits, run from research/warp-drive/paper/reader:

    $ python3 lint.py --chapters
    chapters: 62 file(s), 4570 label(s) defined, 0 hit(s)

    $ python3 assemble.py --check
    labels 4570, computations cited 0, problems 0

assemble.py --check does not test line length after labels are resolved, so I checked that separately. Using
assemble.py's own numbering in memory on chapters 40, 41 and 44, every resolved line is at most 121 characters, and no
wrapped line starts with "+ ", "* ", "> ", "#", "=" or "|". No label was added, so the crosswalks are unchanged and
the label count stays 4570.

## prop:iii-i15-2-12

This edit was made on top of 14817ece. Only chapters/40-s21-parameters.md changed, and no crosswalk changed because no
label was added. Nothing is committed. Line numbers are those of the edited file.

### The chain

‖·‖_𝒴 is "the norm of one such space, fixed once and for all" (sec:iii-i7-4, 40:494–495). It is a finite-regularity
space of the 𝒴 kind on which the bounds of lem:iii-i7-2-5 (c) hold. 𝒴^S_(α,α_+) is "normed in the same way" (40:497).
Let k be the regularity of these norms. The old (2) (40:586–606) has three bounds of one shape:

- ‖(L_(h,p⃗) − L_(0,p⃗_b))u_1‖_(𝒴^S_(α,α_+)) ≤ C(‖h‖ + |p⃗ − p⃗_b|)‖F_1‖_𝒴, for the boost parameters;
- ‖(L_(h,p⃗) − L_(0,p⃗_b))u_1‖_𝒴 ≤ C(‖h‖ + |p⃗ − p⃗_b|)‖F_1‖_𝒴, for the parameters Q;
- |Ṡ_(h,p⃗)(F) − Ṡ_(0,p⃗_b)(F)| ≤ C(‖h‖ + |p⃗ − p⃗_b|)‖F‖_𝒴, and the second term of the bound on Q, which follow from
  the first two.

In each, u_1 is the forward solution of L_(h,p⃗)u_1 = F_1, bounded by F_1 "through prop:iii-i4-4-1 (1), resp.
prop:iii-i6-2-1 … (lem:iii-i7-2-5 (c))".

- **(R1′)** L_(h,p⃗) − L_(0,p⃗_b) is a b-differential operator of order 2. So bounding it at regularity k needs u_1 at
  regularity k + 2. The boost term χ_K h^(≤1)_(b,♮)(Ṡ_1) is smooth and costs only |Ṡ_1|, so the issue is ũ_1.
- **(R2′)** A forward solution gains at most one derivative. The wave-packet argument of section 1 (R2) applies
  unchanged. So bounding ũ_1 at regularity k + 2 needs F_1 at regularity at least k + 1. In the paper it needs more:
  k + 2 plus the loss of lem:iii-i7-2-5 (c).
- **(R3′)** The bound is stated with ‖F_1‖_𝒴, of regularity k.

So k ≥ k + 1, a contradiction. No finite regularity serves, because a single norm appears on both sides. It is the
same cycle as in (i) of prop:iii-i8-4-1, collapsed to one level. The statement of prop:iii-i15-2-12 (the
finite-dimensional bounds, eq:iii-i15-2-8) was never in question: (2) is applied only to the sources f^S_(0,p⃗_b)(S′),
f^(=0)_(0,p⃗_b) and F_(h,p⃗)(p⃗′^(=0)), which are bounded at every finite regularity.

### The edit (least change, as for (i) of prop:iii-i8-4-1)

- **40:586–594, (2).**
  - (2) opens by defining ‖·‖^+_𝒴: "the norm of the same kind as ‖·‖_𝒴 at a larger regularity and a smaller ε, in
    which the bounds of lem:iii-i7-2-5 (c) bound the forward solutions u_1 below at the regularity of ‖·‖_𝒴 plus 2, d
    being large enough for lem:iii-i7-3-1 (c) in it as well".
  - In both displayed bounds, the norm multiplying (‖h‖ + |p⃗ − p⃗_b|) becomes ‖·‖^+_𝒴. The term C‖F_1 − F_2‖_𝒴 keeps
    the fixed norm.
  - A sentence after "made quantitative" gives the reason: the count reads u_1 two orders above ‖·‖_𝒴, and bounds it
    by F_1 through a forward solution.
- **40:601, 604, 607.** The three counts carry ‖F_1‖^+_𝒴 or ‖F‖^+_𝒴. "Its size is at most C‖R‖_𝒴" (40:609) is
  unchanged, and it is consistent: C‖R‖_𝒴 ≤ C‖F_1 − F_2‖_𝒴 + C(…)‖F_1‖^+_𝒴.
- **40:618–619, the boost map.** The second term uses ‖f^S_(0,p⃗_b)(S′)‖^+_𝒴 ≤ C|S′| (lem:iii-i7-3-1 (c), at h = 0).
- **40:630–634, the reduced map.**
  - F_(h,p⃗) and f^(=0)_(0,p⃗_b) are bounded per unit p⃗′^(=0) in ‖·‖^+_𝒴. This uses lem:iii-i7-3-1 (c) with d large,
    and the inverse of the boost map, of norm at most 2, which bounds p⃗′^(<0)_(h,p⃗)(0, ·) inside F_(h,p⃗).
  - The term C(‖h‖ + |p⃗ − p⃗_b|) per unit p⃗′^(=0) of the M-comparison and the A-comparison then hold as written.
  - The last lines of the proof are reflowed.

The statement of prop:iii-i15-2-12 is unchanged, and so are (1), the boost-map identity and the reduced-map identity.
I added no sentence to the setting of sec:iii-i7-4, because ‖·‖^+_𝒴 is used nowhere else.

```diff
diff --git a/research/warp-drive/paper/reader/chapters/40-s21-parameters.md b/research/warp-drive/paper/reader/chapters/40-s21-parameters.md
index 47f1df67..fbc3bc85 100644
--- a/research/warp-drive/paper/reader/chapters/40-s21-parameters.md
+++ b/research/warp-drive/paper/reader/chapters/40-s21-parameters.md
@@ -583,25 +583,28 @@ h-derivative by [[eq:iii-i4-3-1]], the p⃗-derivative by the count of [[eq:iii-
 in the differences of the metrics, with coefficients smooth in their inverses. The mean value theorem along the segment
 from (0, p⃗_b) gives the bound.
 
-(2) For F ∈ 𝒴, |Ṡ_(h,p⃗)(F) − Ṡ_(0,p⃗_b)(F)| ≤ C(‖h‖ + |p⃗ − p⃗_b|)‖F‖_𝒴. And for F_1, F_2 ∈ 𝒴 with
-Ṡ_(h,p⃗)(F_1) = 0 = Ṡ_(0,p⃗_b)(F_2), where alone Q_(h,p⃗) and Q_(0,p⃗_b) are defined,
+(2) Let ‖·‖^+_𝒴 be the norm of the same kind as ‖·‖_𝒴 at a larger regularity and a smaller ε, in which the bounds
+of [[lem:iii-i7-2-5]] (c) bound the forward solutions u_1 below at the regularity of ‖·‖_𝒴 plus 2, d being large
+enough for [[lem:iii-i7-3-1]] (c) in it as well. For F ∈ 𝒴, |Ṡ_(h,p⃗)(F) − Ṡ_(0,p⃗_b)(F)| ≤ C(‖h‖ + |p⃗ − p⃗_b|)‖F‖^+_𝒴.
+And for F_1, F_2 ∈ 𝒴 with Ṡ_(h,p⃗)(F_1) = 0 = Ṡ_(0,p⃗_b)(F_2), where alone Q_(h,p⃗) and Q_(0,p⃗_b) are defined,
 
-    |Q_(h,p⃗)(F_1) − Q_(0,p⃗_b)(F_2)| ≤ C‖F_1 − F_2‖_𝒴 + C(‖h‖ + |p⃗ − p⃗_b|)‖F_1‖_𝒴.
+    |Q_(h,p⃗)(F_1) − Q_(0,p⃗_b)(F_2)| ≤ C‖F_1 − F_2‖_𝒴 + C(‖h‖ + |p⃗ − p⃗_b|)‖F_1‖^+_𝒴.
 
-This is the comparison of [[lem:iii-i7-4-1]] made quantitative. Let u_1, u_2 be the forward solutions of
+This is the comparison of [[lem:iii-i7-4-1]] made quantitative. The second norm is not ‖·‖_𝒴: the count below reads
+u_1 two orders above ‖·‖_𝒴, and bounds it by F_1 through a forward solution. Let u_1, u_2 be the forward solutions of
 L_(h,p⃗)u_1 = F_1 and L_(0,p⃗_b)u_2 = F_2. Then L_(0,p⃗_b)(u_1 − u_2) = R := F_1 − F_2 − (L_(h,p⃗) − L_(0,p⃗_b))u_1. Both
 backgrounds equal g_b near K⁺ ([[lem:iii-i-3-6]]), so L_(h,p⃗) − L_(0,p⃗_b) has coefficients of K⁺-weight a_K there; at
 ι⁺ it gains as in the proof of [[lem:iii-i7-4-1]]; and its coefficients have size O(‖h‖ + |p⃗ − p⃗_b|).
 *The boost parameters.* Fix α ∈ (1, min(a_K − 1, 3/2)) and α_+ ∈ (α, 2). For a general F_1 ∈ 𝒴, u_1 carries a boost
 term of K⁺-weight −1 − ε, so (L_(h,p⃗) − L_(0,p⃗_b))u_1 has K⁺-weight only a_K − 1 − ε, which may lie below α_K: R need
 not lie in 𝒴. It lies in 𝒴^S_(α,α_+) of [[sec:iii-i7-4]], by the count of the proof of [[lem:iii-i7-4-1]] (a), with
-‖(L_(h,p⃗) − L_(0,p⃗_b))u_1‖_(𝒴^S_(α,α_+)) ≤ C(‖h‖ + |p⃗ − p⃗_b|)‖F_1‖_𝒴, u_1 being bounded by F_1 through
+‖(L_(h,p⃗) − L_(0,p⃗_b))u_1‖_(𝒴^S_(α,α_+)) ≤ C(‖h‖ + |p⃗ − p⃗_b|)‖F_1‖^+_𝒴, u_1 being bounded by F_1 through
 [[prop:iii-i4-4-1]] (1) for L_(h,p⃗), uniformly ([[lem:iii-i7-2-5]] (c)). With F_1 = F_2 = F, the boost terms of u_1
 and u_2 are built from the same state at b, so the difference of the boost parameters is Ṡ_(0,p⃗_b)(R), of size at
-most C‖R‖_(𝒴^S_(α,α_+)) ≤ C(‖h‖ + |p⃗ − p⃗_b|)‖F‖_𝒴. *The parameters Q.* Under the condition
+most C‖R‖_(𝒴^S_(α,α_+)) ≤ C(‖h‖ + |p⃗ − p⃗_b|)‖F‖^+_𝒴. *The parameters Q.* Under the condition
 Ṡ_(h,p⃗)(F_1) = 0 = Ṡ_(0,p⃗_b)(F_2), u_1 has no boost term, so it has K⁺-weight −ε and is bounded by F_1 in the space of
 [[prop:iii-i6-2-1]] for L_(h,p⃗), uniformly; as in the proof of [[lem:iii-i7-4-1]] (b), the K⁺-weight a_K − ε ≥ α_K
-then gives ‖(L_(h,p⃗) − L_(0,p⃗_b))u_1‖_𝒴 ≤ C(‖h‖ + |p⃗ − p⃗_b|)‖F_1‖_𝒴, and R ∈ 𝒴. Also u_1 − u_2 has no boost term,
+then gives ‖(L_(h,p⃗) − L_(0,p⃗_b))u_1‖_𝒴 ≤ C(‖h‖ + |p⃗ − p⃗_b|)‖F_1‖^+_𝒴, and R ∈ 𝒴. Also u_1 − u_2 has no boost term,
 so Ṡ_(0,p⃗_b)(R) = 0, and Q_(h,p⃗)(F_1) − Q_(0,p⃗_b)(F_2) = Q_(0,p⃗_b)(R), by the uniqueness in the proof of
 [[lem:iii-i7-4-1]] (b), which uses the injectivity of (ḃ, Ṡ) ↦ ġ_b(ḃ) + h_b(Ṡ). Its size is at most C‖R‖_𝒴.
 
@@ -612,7 +615,8 @@ Hence
     S^(−1)_(h,p⃗)(S′) − S′ = Ṡ_(h,p⃗)(f^S_(h,p⃗)(S′) − f^S_(0,p⃗_b)(S′)) + (Ṡ_(h,p⃗) − Ṡ_(0,p⃗_b))(f^S_(0,p⃗_b)(S′))
                             + Ṡ_(0,p⃗_b)(E^mot_b(S′, 0, 0)),
 
-and by (1), (2) and [[lem:iii-i15-2-11]] the three terms are at most C(‖h‖ + |p⃗ − p⃗_b| + |b − b₀|)|S′|.
+and by (1), (2) and [[lem:iii-i15-2-11]] the three terms are at most C(‖h‖ + |p⃗ − p⃗_b| + |b − b₀|)|S′|, as
+‖f^S_(0,p⃗_b)(S′)‖^+_𝒴 ≤ C|S′| ([[lem:iii-i7-3-1]] (c)).
 
 *The reduced map.* At (0, p⃗_b), [[eq:s21-boost-choice]] gives
 S′_0 := A_(0,p⃗_b)p⃗′^(=0) = −(S^(−1)_(0,p⃗_b))⁻¹Ṡ_(0,p⃗_b)(f^(=0)_(0,p⃗_b)(b′, S″)). By [[eq:iii-i15-2-7]],
@@ -624,11 +628,13 @@ K⁺-weight −ε > −1, so no boost term, and Q_(0,p⃗_b) of that forcing is
 
 whence |M_(0,p⃗_b) + id| ≤ C|b − b₀|. For (h, p⃗) near (0, p⃗_b), M_(h,p⃗)(p⃗′^(=0)) = Q_(h,p⃗)(F_(h,p⃗)(p⃗′^(=0))) with
 Ṡ_(h,p⃗)(F_(h,p⃗)(p⃗′^(=0))) = 0, and likewise at (0, p⃗_b). So (2), for the pair (F_(h,p⃗), F_(0,p⃗_b)), bounds
-M_(h,p⃗) − M_(0,p⃗_b) by C‖F_(h,p⃗) − F_(0,p⃗_b)‖_𝒴 + C(‖h‖ + |p⃗ − p⃗_b|) per unit p⃗′^(=0); and (1) bounds
-‖F_(h,p⃗) − F_(0,p⃗_b)‖_𝒴, with A_(h,p⃗) − A_(0,p⃗_b) bounded the same way through [[eq:s21-boost-choice]], (1), (2)
-and the bound on the boost map. This proves the bound on A_(h,p⃗) and [[eq:iii-i15-2-8]], and the Neumann series gives
-the inverses. The proofs of [[lem:iii-i7-4-3]], [[lem:iii-i7-4-5]] and [[cor:iii-i7-4-6]] below, and the base step of
-[[prop:iii-i8-4-1]], use, beyond [[lem:iii-i7-2-5]] (c), only these inverses and their bounds. ∎
+M_(h,p⃗) − M_(0,p⃗_b) by C‖F_(h,p⃗) − F_(0,p⃗_b)‖_𝒴 + C(‖h‖ + |p⃗ − p⃗_b|) per unit p⃗′^(=0), F_(h,p⃗) and
+f^(=0)_(0,p⃗_b) being bounded per unit p⃗′^(=0) in ‖·‖^+_𝒴 ([[lem:iii-i7-3-1]] (c), with the inverse of the boost map,
+of norm at most 2); and (1) bounds ‖F_(h,p⃗) − F_(0,p⃗_b)‖_𝒴, with A_(h,p⃗) − A_(0,p⃗_b) bounded the same way through
+[[eq:s21-boost-choice]], (1), (2) and the bound on the boost map. This proves the bound on A_(h,p⃗) and
+[[eq:iii-i15-2-8]], and the Neumann series gives the inverses. The proofs of [[lem:iii-i7-4-3]], [[lem:iii-i7-4-5]] and
+[[cor:iii-i7-4-6]] below, and the base step of [[prop:iii-i8-4-1]], use, beyond [[lem:iii-i7-2-5]] (c), only these
+inverses and their bounds. ∎
 
 **Lemma {#lem:iii-i7-4-3}** ([Hin26, Lemma 11.43] in dimension 4 + 1.) For (h, p⃗) small as in
 [[prop:iii-i15-2-12]], with parameter b ∈ ℬ̄_*, f ∈ 𝒴 and p⃗′^(=0) ∈ 𝔟 ⊕ 𝒮_1 there is a unique
```

### Uses checked

I grepped chapters 39–44, 46 and 71 for prop:iii-i15-2-12 and for ‖·‖_𝒴, and also checked lem:iii-i7-4-1.

**Uses of ‖·‖_𝒴 (all in chapter 40).**

- **40:495 and 497.** These are the definition and 𝒴^S. Unchanged; ‖·‖^+_𝒴 is "of the same kind".
- **40:580, (1).** This bounds a difference of smooth sources in the fixed norm, with d large, and is correct as it
  stands. Unchanged.
- **40:601–609.** Edited, as above.
- **40:630–634.** Edited, as above.

**Uses of prop:iii-i15-2-12 that use only its statement, so the change does not touch them.**

- **Chapter 40:** 40:65, 77, 447, 540, 634–692 (lem:iii-i7-4-3 for invertibility and the bound on A,
  lem:iii-i7-4-5, cor:iii-i7-4-6) and 1143 (the base of prop:iii-i8-4-1).
- **Chapters 41 and 42:** 41:66 and 42:1019, where it shrinks the ball.
- **Chapter 43:** 43:213 and 43:377, the inventory.
- **Chapter 44:** 44:32, 51, 115, 437, 507, 509, 539, 602, 643, 646 and 667, which cite the direct bounds and the
  constants uniform in b.

**40:948 and 40:974–977, lem:iii-i8-3-1.** This says that the proof of prop:iii-i15-2-12, with its bound of the
difference of operators applied to the solution, holds with 𝒴(α_0) in place of 𝒴, "unchanged". Read with ‖·‖_𝒴 and
‖·‖^+_𝒴 as norms of 𝒴(α_0), it stays true. No edit.

**lem:iii-i7-4-1 (40:500–538).** The change does not touch it. Its proof uses neither ‖·‖_𝒴 nor (2). It is correct
when "F_j → F in 𝒴" is read in the Fréchet topology, which is what its only use provides (the base of
prop:iii-i8-4-1 (ii), where F_j → F in 𝒴(α_0)). It would have the same shape only if the sentence "Forcings converge
in the finite-regularity spaces …" (40:493–494) were taken to mean convergence in ‖·‖_𝒴 alone. I report this and did
not edit it.

**prop:iii-i15-2-8 (39:873–923).** This is the matching boost bound in chapter 39. It already does what the repair
does. It reads the solution "at the regularity k_1 + 2 that Π_b needs, as d ≥ k_1 + d_T + 7", bounds Π_b on that
space, and measures the smooth source f_(0,0;b)(S′) in an unnamed norm. No edit.

**Chapter 46.** There is no citation of prop:iii-i15-2-12 or of ‖·‖_𝒴, so there is nothing to change.

**Chapter 71.**

- There is no citation of prop:iii-i15-2-12 or of ‖·‖_𝒴, so no loss moves.
- The proof file proofs/P-U71-small.md (lem:uc-small-orders (c)) already reads "the counts … of (2) of the proof of
  prop:iii-i15-2-12, with u bounded", with the norms of sec:iii-i7-4 at regularities ≤ 2R_base + 2.
- reg ‖·‖^+_𝒴 ≤ reg ‖·‖_𝒴 + 2 + (the loss of the forward solution of a base, ≤ R_base), and reg ‖·‖_𝒴 ≤ R_base by
  that file's own count. So reg ‖·‖^+_𝒴 ≤ 2R_base + 2.
- Hence 2R_base + 16, D_*, D′_* and the bounds on d_NM stand. The new norm enters only as a bound on data, not as a
  smallness condition.

No statement changes in substance.

### Check outputs

After this edit, run from research/warp-drive/paper/reader:

    $ python3 lint.py --chapters
    chapters: 62 file(s), 4570 label(s) defined, 0 hit(s)

    $ python3 assemble.py --check
    labels 4570, computations cited 0, problems 0

Using assemble.py's numbering in memory on chapter 40, every line resolves to at most 121 characters, and no wrapped
line starts with a forbidden marker.
