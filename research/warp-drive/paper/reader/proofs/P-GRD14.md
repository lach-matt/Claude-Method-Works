### The threshold of the continuation, and the factor of H at a point {#sec:tl5-hfc}

This section makes two changes. First, [[lem:tl5-continuation]] extends solutions under the a priori bound y_σ ≤ 2A, and
every smallness condition of this chapter is formed with that bound: Step 1 of the a priori estimate applies the bounds
at a point with ℰ_g(p) ≤ e^(φ(p)) Y_σ² ≤ 4e^(φ(p)) A², which gives the term with A of 𝔰_*. The argument needs only a
number 𝔜 at which q(y) := By² − y + A is negative, and every 𝔜 between the two roots Y₋ < Y₊ of q serves; the solution
then satisfies y_σ ≤ Y₋ = 2A/(1 + (1 − 4AB)^(1/2)), which lies between A and 2A and is close to A when 4AB is small
([[lem:tl5-hfc-cont]]). So 𝔰_* may be formed with Y₋ in place of 2A. Second, the bounds at a point carry the factor 2
of |H| ≤ 2|h| in the products 2C_S and 2C_(0,0). Under 𝔰 ≤ 𝔰_♭ the identity H = −g⁻¹ h ĝ⁻¹ gives |H| ≤ 𝔤₁ |h|, as it
does in the constant 𝔨_B, so these products become 𝔤₁ C_S and 𝔤₁ C_(0,0) ([[lem:tl5-hfc-h]]). Both changes enter the
constants with index c ([[def:tl5-hfc-constants]], [[thm:tl5-hfc]]). The closing condition is [[eq:tl5-hfc-closing]];
every new constant is at most the one it replaces, and the earlier closing conditions remain valid. The notation is that
of [[sec:tl5-hfe]].

**Lemma {#lem:tl5-hfc-cont}** (Existence by continuity with a threshold below 2A.) In the setting of
[[lem:tl5-continuation]] let A, B > 0 with 4AB < 1, and put

    Y₋ := 2A/(1 + (1 − 4AB)^(1/2)),      Y₊ := (1 + (1 − 4AB)^(1/2))/(2B),                               {#eq:tl5-hfc-y}

the roots of q(y) := By² − y + A, so that q < 0 on (Y₋, Y₊), q ≥ 0 on [0, Y₋], and A ≤ Y₋ < 2A < 1/(2B) ≤ Y₊. Let 𝔜 ∈
(Y₋, Y₊), and suppose that every solution g on every D^κ_s with y_σ(g) ≤ 𝔜 for all σ ∈ [1/2, s] satisfies (H1), (H2) and
(H4) of [[lem:tl5-continuation]], and that y_(1/2)(g) ≤ A for every solution g. Then there is a solution g on D^κ, and
y_σ(g) ≤ Y₋ for every σ ∈ [1/2, v*]. For 𝔜 = 2A the hypotheses are those of [[lem:tl5-continuation]].

*Proof.* With x := 4AB ∈ (0, 1), the roots of q are (1 ∓ (1 − x)^(1/2))/(2B), and (1 − (1 − x)^(1/2))/(2B) = x/(2B (1 +
(1 − x)^(1/2))) = Y₋. As 1 < 1 + (1 − x)^(1/2) ≤ 2, A ≤ Y₋ < 2A; 2A < 1/(2B) as x < 1; and 1/(2B) ≤ Y₊. As q has
positive leading coefficient and q(0) = A > 0, q < 0 exactly on (Y₋, Y₊), and q ≥ 0 on [0, Y₋]. So if y ≥ 0 satisfies y
≤ A + By² and y ≤ 𝔜, then q(y) ≥ 0 and y ≤ 𝔜 < Y₊ give y ≤ Y₋ < 𝔜; this takes the place of the first paragraph of the
proof of [[lem:tl5-continuation]], whose rest holds with 𝔜 in place of 2A. Let I be the set of s ∈ (1/2, v*] for which
there is a solution g on D^κ_s with y_σ(g) ≤ 𝔜 for all σ ∈ [1/2, s]. It is not empty, as y_(1/2)(g) ≤ A ≤ Y₋ < 𝔜 and y_σ
is continuous in σ. It is open: for s ∈ I, s < v*, and the solution g on D^κ_s, (H1) for the restrictions of g to the
D^κ_σ, σ ∈ (1/2, s], and y_σ(g) ≤ 𝔜 give y_σ(g) ≤ Y₋ < 𝔜, so y_s(g) < 𝔜; (H4) and (F3_W) of [[thm:tl5-wg]] extend g to a
solution g′ on some D^κ_(s′), s′ > s, and y_σ(g′) ≤ 𝔜 on [1/2, s″] for some s″ ∈ (s, s′] by continuity. It is closed, by
the argument of that proof with (H2), the bound y_σ ≤ 𝔜 passing to the limit as the bound y_σ ≤ 2A does there. So v* ∈
I. For the solution g on D^κ and σ ∈ (1/2, v*], the restriction of g to D^κ_σ is a solution with y_σ′ ≤ 𝔜 for σ′ ≤ σ, so
(H1) gives y_σ(g) ≤ Y₋, and y_(1/2)(g) ≤ A ≤ Y₋. For 𝔜 = 2A, which lies in (Y₋, Y₊), the hypotheses are (H1), (H2), (H4)
and (H3) of [[lem:tl5-continuation]]. ∎

**Lemma {#lem:tl5-hfc-h}** (The factor of H at a point.) Let h be as in [[def:tl5-hfg-graded]] and q a point with 𝔰(q) ≤
𝔰_♭. Then |H(q)| ≤ 𝔤₁ |h(q)|, with 𝔤₁ = 1 + 2𝔰_♭ of [[def:tl5-hfs-bounds]]. Consequently, under their hypotheses and in
the forms that the later lemmas of this chapter give them, [[lem:tl5-hfg-linfty]], [[lem:tl5-hfs-linfty]],
[[lem:tl5-hft-small]], [[lem:tl5-hfq-theta]] and [[lem:tl5-hfv-rec]] hold with 𝔤₁ C_S and 𝔤₁ C_(0,0) in place of 2C_S
and 2C_(0,0): in the first inequality of [[eq:tl5-hfs-linfty]], in C_∞^(m) and C_(∞,0)^(m) of [[eq:tl5-hfg-cinf]] and
their forms with μ and with ν, and in C_P^v and C_(P,0)^v of [[lem:tl5-hfv-rec]].

*Proof.* By [[lem:tl5-wg-norms]] (a), |H(q)| ≤ 2|h(q)| ≤ 2𝔰(q) ≤ 2𝔰_♭, as |h| ≤ 𝔰 and 𝔰_♭ ≤ 1/8. As g⁻¹ − ĝ⁻¹ = −g⁻¹ h
ĝ⁻¹, as in the proof of [[lem:tl5-hfg-quadratic]], H = −g⁻¹ h ĝ⁻¹. In the frame F, where ĝ^MN = η^MN, raising an index
with ĝ⁻¹ does not change the norm and a contraction with H multiplies it by at most |H|, so a factor g⁻¹ = ĝ⁻¹ + H that
raises an index costs at most 1 + |H| ≤ 1 + 2𝔰_♭ = 𝔤₁, as in the proofs of [[lem:tl5-hfs-quadratic]] (a) and
[[thm:tl5-hfv]]; this gives |H(q)| ≤ 𝔤₁ |h(q)|. In each lemma named, the hypothesis on Q(a, b), 𝔰 ≤ 𝔰₀^⋆, 𝔰₀^♮, 𝔰₀^μ or
𝔰₀^q, or 𝔰 ≤ 𝔰₁^v ≤ 𝔰₀/2 with the replacements of [[lem:tl5-hfy-abs]], each at most 𝔰_♭, gives 𝔰(p) ≤ 𝔰_♭ at the point p
of the bound. There the factors 2 of 2C_S and 2C_(0,0) are those of |H(p)| ≤ 2|h(p)| in the step of zeroth order, which
bounds μ |H(p)| by 2μ |h(p)| and μ |h(p)| by C_S ℰ_g(p)^(1/2) + C_(0,0) η₀(p), with the weights of the lemma in use (for
H in [[lem:tl5-hfq-theta]] the factor 2 is taken up by 2C_S and 2C_(0,0), as stated there, and in [[lem:tl5-hft-small]]
(a) the bound is that of |H(p)| by 2|h(p)|); each other quantity of 𝔰_P⁰, of 𝔰_g^(m) and of 𝔰 enters these maxima with
its own constant. With |H(p)| ≤ 𝔤₁ |h(p)| in place of |H(p)| ≤ 2|h(p)| the bound of μ |H(p)| has the factor 𝔤₁, and as
𝔤₁ ≥ 1 the entries 𝔤₁ C_S and 𝔤₁ C_(0,0) also bound the quantities Ψ_B that the entries 2C_S and 2C_(0,0) bounded; so
the maxima hold with 𝔤₁ C_S and 𝔤₁ C_(0,0). ∎

**Definition {#def:tl5-hfc-constants}** (The constants with index c.) In the setting of [[def:tl5-hfe-constants]], the
constants with index c are the constants with index l formed with 𝔤₁ C_S^l and 𝔤₁ C_(0,0) in place of 2C_S^l and
2C_(0,0), C_(0,0) in its form with index l: at the sites of [[lem:tl5-hfc-h]], in 𝔎 and 𝔎₀ of [[def:tl5-hfs-constants]],
which Step 3 of the proof of [[prop:tl5-hfs-bootstrap]] forms from the bound of 𝔰_P⁰, and in every constant formed from
these, among them 𝔎^D and 𝔎^D₀, C_P, C_(P,0), C_(∞,μ)^(m) and C_((∞,0),μ)^(m) with their forms with ν, S_F, 𝔯 and 𝔰_*.
Let S_F^c, S_M^c, ε_M^c and 𝔯^c be S_F^l, S_M^l, ε_M^l and 𝔯^l formed with them, ε^c := ε^l, and

    η_c := 1 − max(ϑ₁, ϑ₂) − 𝔯^c,      A_c := η_c^(−1/2) δ_w + η_c⁻¹ (ε^c + ε_M^c),      B_c := η_c⁻¹ (S_F^c + S_M^c).

For a number 𝔜 ≥ 0 let 𝔰_*^c[𝔜] be 𝔰_*^l formed with the constants with index c and with 𝔜/2 in place of A_l, so that
its term with A_l carries 𝔜 in place of 2A_l, and, when 4A_c B_c < 1, put

    Y_c := 2A_c/(1 + (1 − 4A_c B_c)^(1/2)),      𝔰_*^c := 𝔰_*^c[Y_c].                            {#eq:tl5-hfc-constants}

**Theorem {#thm:tl5-hfc}** (Existence with the threshold Y_c and the factor 𝔤₁.) In the setting of [[thm:tl5-hfe]], with
the constants with index c of [[def:tl5-hfc-constants]], suppose: (a) η₀ < 𝔰₁^v; (b) the rates (1 − ϑ₁) a_o, (1 − ϑ₂)
a_i are admissible for (𝔅_N, E_o^N, E_i^N); (c) η_c > 0, the closing condition

    4 A_c B_c = 4 η_c^(−3/2) (δ_w + η_c^(−1/2) (ε^c + ε_M^c)) (S_F^c + S_M^c) < 1,                 {#eq:tl5-hfc-closing}

and 𝔰_*^c < 𝔰₁^v. Then there is a solution g of the reduced problem on D^κ with Y_σ(g) ≤ Y_c for every σ ∈ [1/2, v*],
and the other conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with 𝔰_*^c in place of 𝔰_*. Each
constant with index c is at most the one with index l it replaces, η_c ≥ η_l, A_c ≤ A_l, B_c ≤ B_l, Y_c ≤ 2A_c ≤ 2A_l
and 𝔰_*^c ≤ 𝔰_*^l; so the hypotheses of [[thm:tl5-hfe]] imply these.

*Proof.* If A_c = 0, the proof of [[thm:tl5-hf]] gives ĝ as the solution, with Y_σ(ĝ) = 0 = Y_c. Otherwise A_c > 0 and
B_c > 0, as S_F^c > 0, and Y_c < 2A_c by [[lem:tl5-hfc-cont]]. The term of 𝔰_*^c[𝔜] with A_l is a(p) 𝔜 with a(p) ≥ 0,
and its other terms do not depend on 𝔜 and are nonnegative, so 𝔰_*^c[𝔜] ≤ (𝔜/Y_c) 𝔰_*^c for 𝔜 ≥ Y_c; fix 𝔜 with Y_c < 𝔜
≤ 2A_c and 𝔜 𝔰_*^c < Y_c 𝔰₁^v, so that 𝔰_*^c[𝔜] < 𝔰₁^v.

*The factor of H.* By [[lem:tl5-hfc-h]], the bounds at a point that the proof of [[thm:tl5-hfe]] uses hold with the
constants with index c. The proofs on which it rests use the products 2C_S and 2C_(0,0) only through these bounds and
through 𝔎 and 𝔎₀, which Step 3 of the proof of [[prop:tl5-hfs-bootstrap]] forms from 𝔰_P⁰ ≤ 2C_S e^(φ/2) Y_s + 2C_(0,0)
η₀, with 𝔤₁ in place of 2 by [[lem:tl5-hfc-h]]. So that proof applies with the constants with index c, and gives (H1)
with A_c and B_c, under the a priori bound it uses.

*The threshold.* In the proof of [[thm:tl5-hfe]] and in the proofs on which it rests, the a priori bound Y_σ ≤ 2A, A the
number of the theorem in use (A_w, A_(w,4), A_g, …, A_l), enters at three places, and we use Y_σ ≤ 𝔜 at each of them.
(i) In the a priori estimate, [[prop:tl5-hf-bootstrap]] and its forms, it enters only Step 1, through ℰ_g(p) ≤ e^(φ(p))
Y_σ(g)² ≤ 4e^(φ(p)) A² for p ∈ D^κ_σ, as φ ≤ φ(p) on Σ₁(τ₁(p), τ₂(p)). With ℰ_g(p) ≤ e^(φ(p)) 𝔜² in its place, the
bounds at p and the argument with Σ_* of the proof of [[thm:tl5-hfy]] give 𝔰 ≤ 𝔰_*^c[𝔜] < 𝔰₁^v on D^κ_s; Steps 2 and 3
use this smallness and Y_s itself, not the a priori bound, and so give Y_s ≤ A_c + B_c Y_s². (ii) In
[[lem:tl5-hf-persistence]] and [[lem:tl5-hf4-persistence]], as in the proofs of [[thm:tl5-hfg]] and [[thm:tl5-hf4g]],
the a priori estimate enters only through 𝔰 ≤ 𝔰_*, which gives |H| ≤ 1/8 and the bounds of θ_H, θ_H^(1) and θ_H^(2) (as
in the proof of [[thm:tl5-hfv]]) and, at level four, the bound of |D̂²Ψ_B|, |B| ≤ 3, by a constant (as in the proof of
[[thm:tl5-hf4t]]); and the a priori bound enters only P(N), through the bound μ^(−N) e^(Φ_o(u*) + Φ_i(v*)) 4A² of the
energies of level N. Under Y_σ ≤ 𝔜, (i) gives the first, with 𝔰_*^c[𝔜] < 𝔰₁^v, and P(N) holds with 𝔜² in place of 4A²;
so (H2) holds, and (H4) follows from |h|_k̂ < κ_m/2 as there. (iii) In the proof of [[thm:tl5-hf]] or of
[[thm:tl5-hf4]], [[lem:tl5-continuation]] is applied with y_σ := Y_σ; apply [[lem:tl5-hfc-cont]] with A := A_c, B := B_c
and 𝔜, which lies in (Y_c, Y₊) as 𝔜 ≤ 2A_c < Y₊. Its hypotheses are (H1), (H2) and (H4) for the solutions with Y_σ ≤ 𝔜,
given by the factor of H and by (i) and (ii), 4A_c B_c < 1 and Y_(1/2) = 0 ≤ A_c. It gives a solution g on D^κ with
Y_σ(g) ≤ Y_c for every σ ∈ [1/2, v*].

As Y_σ(g) ≤ Y_c and 𝔰_*^c[Y_c] = 𝔰_*^c < 𝔰₁^v, (i) with Y_c in place of 𝔜 and s = v* gives 𝔰 ≤ 𝔰_*^c on D^κ, |h|_k̂ <
κ_m/2 and the bounds of θ_H; the rest of the conclusions follows from these as in the proofs of [[thm:tl5-hf]] and
[[thm:tl5-hf4]], the bound for ε being [[eq:tl5-hf-eps]] with 𝔰 ≤ 𝔰_*^c. For the last claim, 𝔤₁ ≤ 5/4 < 2 as 𝔰_♭ ≤ 1/8,
and every constant with index l is nondecreasing in the products it contains, so each constant with index c is at most
the one it replaces; then η_c ≥ η_l, A_c ≤ A_l, B_c ≤ B_l and 4A_c B_c ≤ 4A_l B_l, as in the proof of [[thm:tl5-hfe]].
Y_c ≤ 2A_c as 1 + (1 − 4A_c B_c)^(1/2) ≥ 1, and 𝔰_*^c[𝔜] is nondecreasing in 𝔜 and in the constants, so 𝔰_*^c ≤
𝔰_*^c[2A_c] ≤ 𝔰_*^l. ∎

**Remark {#rem:tl5-hfc-what}** (What changes.) The continuation needs, for the solutions it extends, a bound y_σ ≤ 𝔜
that (H1) makes strict, and q(𝔜) < 0 is what makes y ≤ A + By² and y ≤ 𝔜 give y ≤ Y₋ < 𝔜. The threshold 2A of
[[lem:tl5-continuation]] is one such number, with q(2A) = A(4AB − 1); every number between the roots serves, and the
bound of the solution is the smaller root Y₋ = 2A/(1 + (1 − 4AB)^(1/2)) = A + A²B + 2A³B² + ⋯, which tends to A as 4AB
tends to 0 and to 2A as 4AB tends to 1. The term of 𝔰_* with A carries the a priori bound, so it takes the factor 2/(1 +
(1 − 4A_c B_c)^(1/2)) in place of 2: when the closing condition holds with room this nearly halves that term, and when
the closing condition is close to binding the gain is small. As 𝔰_*^c < 𝔰₁^v is strict, a number 𝔜 slightly above Y_c
keeps 𝔰_*^c[𝔜] < 𝔰₁^v, and the solutions with Y_σ ≤ 𝔜 are those the continuation extends; Steps 2 and 3, the persistence
of regularity and the conclusions use the a priori bound only through the smallness it gives and through a bound of the
energies by a constant. The factor 2 of 2C_S and 2C_(0,0) is that of |H| ≤ 2|h|, which holds for |h| ≤ 1/2; at every
point where a bound at a point is formed, 𝔰 ≤ 𝔰_♭ holds, and there |H| ≤ 𝔤₁ |h|, the bound already used for 𝔨_B. So the
entry of C_P^v, of 𝔎 and of C_∞^(m) that bounds μ |H| loses its factor 2, the other entries keeping theirs; the factor 2
of 2𝒥_g in the nonlinear parts of the absorption, which comes from |H| ≤ 2|h| as well and enters only with 𝔵^z, is kept.
The counts, the recovery constants, the Sobolev constants, the weights 𝔲₀, 𝔲₁, 𝔲_M, the thresholds 𝔰₀ and 𝔰₁^v and the
rates are unchanged. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfc]] are established in
this paper for no background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD 0563d28a, where sec:tl5-hfe is merged (Section 57.28,
merge 0563d28a). Line numbers serve only to find the place.

*1. Where the section goes.* The section above, from its heading (label sec:tl5-hfc) through the last line of
[[rem:tl5-hfc-what]], is inserted at the end of [[ch:ten-l5]], after the last line of [[rem:tl5-hfe-what]] (line 7505,
as changed by item 2), with one blank line before it, as a sibling "###" section. No number already printed changes.

*2. The last sentence of [[rem:tl5-hfe-what]] (lines 7503–7504).* Old:

at a point, the leaf constant C_(E,0)(𝔶), 𝔨₂, K_rec, 𝔨_♯, 𝔵^z and the thresholds are unchanged. As for [[thm:tl5-hf]]
and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfe]] are established in this paper for no background at 10 l5.

New (one line added, of 118 characters; the two old lines are unchanged):

at a point, the leaf constant C_(E,0)(𝔶), 𝔨₂, K_rec, 𝔨_♯, 𝔵^z and the thresholds are unchanged. As for [[thm:tl5-hf]]
and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfe]] are established in this paper for no background at 10 l5.
[[sec:tl5-hfc]] takes the threshold of the continuation at the smaller root and the factor 𝔤₁ for H ([[thm:tl5-hfc]]).

*3. Nothing else changes.* No earlier text is edited: the sites listed in the Comparison keep their texts, and the new
constants are defined in def:tl5-hfc-constants by reference to them.

### Comparison and the factors for the evaluation

Not chapter text. thm:tl5-hfc acts at every level, on thm:tl5-hfe. Every new factor is at most the old one, for all
admissible weights and choices, so the theorem contains thm:tl5-hfe, and through it every earlier theorem in the range
where thm:tl5-hfe contains it.

Unchanged: all counts (𝔠^♮, 𝔠^D, 𝔠^(D,7), 𝔠^ϱ, 𝔠^Mq), the recovery constants, the Sobolev and leaf constants (C_S^l,
C₁^l, C_(1,ϱ)^l, C_(0,0), C_(1,0), C_(E,0)(𝔶)), the weights 𝔲₀, 𝔲₁, 𝔲_M, 𝔶, θ, ϑ₁, ϑ₂, 𝔨₁, 𝔨₂, k₂^z, 𝔵^z, the
thresholds 𝔰₀ and 𝔰₁^v with the cap, ε (ε^c = ε^l), S_M, ε_M, and the rates.

1. The threshold of the continuation (lem:tl5-hfc-cont).
   - Old: lem:tl5-continuation with the a priori bound y_σ ≤ 2A; every 𝔰_* carries 2 C_∞ μ^(−N/2) e^(φ/2) A.
   - New: any 𝔜 ∈ (Y₋, Y₊), Y₋ = 2A/(1 + (1 − 4AB)^½), Y₊ = (1 + (1 − 4AB)^½)/(2B); the solution has y_σ ≤ Y₋; and
         𝔰_*^c = 𝔰_*^c[Y_c],  Y_c = 2A_c/(1 + (1 − 4A_cB_c)^½),
     that is the factor 2 of the term with A becomes 2/(1 + (1 − 4A_cB_c)^½) ∈ [1, 2).
   - Y₋ = A + A²B + 2A³B² + ⋯; Y₋/A = 1 / 1.111 / 1.172 / 1.225 / 1.382 / 2 at 4AB = 0 / 0.36 / 0.5 / 0.6 / 0.8 / 1.
   - The sites of the a priori bound, at HEAD 0563d28a, and what each takes:
     - 87:3500, 3513, 3520, 3527–3552 (lem:tl5-continuation, "y_σ(g) ≤ 2A for all σ ∈ [1/2, s]" and its proof):
       replaced, in thm:tl5-hfc, by lem:tl5-hfc-cont with 𝔜; the lemma itself is kept.
     - 87:4460, 4470–4471 (prop:tl5-hf-bootstrap, "with Y_σ(g) ≤ 2A_w for every σ ∈ [1/2, s]" and "ℰ⁰_N(p) ≤ μ^(−N)
       e^(φ(p)) Y_σ(g)² ≤ 4μ^(−N) e^(φ(p)) A_w²"), and its forms 87:4835 (prop:tl5-hf4-bootstrap), 87:5306, 5313
       (prop:tl5-hfg-bootstrap), 87:5685 (prop:tl5-hfs-bootstrap), 87:5921, 5927 (prop:tl5-hft-bootstrap, "ℰ_g(p) ≤
       e^(φ(p)) Y_σ(g)² ≤ 4 e^(φ(p)) A_t²"), 87:6103 (prop:tl5-hfq-bootstrap) and Step 1 of the proofs of thm:tl5-hfv to
       thm:tl5-hfe: with 𝔜 in place of 2A (proof of thm:tl5-hfc, (i)). Steps 2 and 3 do not read the bound.
     - 87:4518, 4526 (lem:tl5-hf-persistence, "Y_σ(g) ≤ 2A_w" and "P(N) holds: ℰ⁰ ≤ μ^(−N) e^(Φ_o(u*) + Φ_i(v*))
       4A_w²") and 87:4878, 4892 (lem:tl5-hf4-persistence, "… 4A_(w,4)²"), with the uses of them in 87:5371–5372,
       5393–5394 (proofs of thm:tl5-hfg, thm:tl5-hf4g), 87:5731, 5950, 6129: with 𝔜 in place of 2A and 𝔜² in place
       of 4A² (proof of thm:tl5-hfc, (ii)); the smallness they use is 𝔰_*^c[𝔜] < 𝔰₁^v.
     - 87:4571, 4580, 4582 (thm:tl5-hf, "Y_σ(g) ≤ 2A_w for every σ ∈ [1/2, v*]") and 87:4979 (thm:tl5-hf4): the
       conclusion becomes Y_σ ≤ Y_c, which implies Y_σ ≤ 2A_c ≤ 2A_l; nothing downstream reads the value 2A.
     - The smallness conditions 87:4453, 4824, 5298, 5676, 5910, 5914, 6098 and their forms 𝔰_*^v, 𝔰_*^w, …, 𝔰_*^l:
       formed with Y_c (𝔰_*^c), and with 𝔜 slightly above Y_c inside the proof.
     - 87:2493 (rem:tl5-wg-continuation, "an a priori bound y ≤ 2A must imply"): unchanged; the strict tilt is implied
       by y ≤ 𝔜 as by y ≤ 2A.
     No site keeps 2A in thm:tl5-hfc: each reads Y_σ ≤ 𝔜 with Y_c < 𝔜 ≤ 2A_c, or the conclusion Y_σ ≤ Y_c.
2. The factor of H (lem:tl5-hfc-h). |H| ≤ 𝔤₁|h|, 𝔤₁ = 1 + 2𝔰_♭, where 𝔰 ≤ 𝔰_♭; proved from lem:tl5-wg-norms (a) (|H| ≤
   2|h|, so |H| ≤ 2𝔰_♭), H = −g⁻¹hĝ⁻¹ (proof of lem:tl5-hfg-quadratic, second expansion) and the cost 1 + |H| of a
   factor g⁻¹ raising an index (proofs of lem:tl5-hfs-quadratic (a), 87:5518, and of thm:tl5-hfv, 87:6240). 𝔰 ≤ 𝔰_♭
   holds at every point where a bound at a point of the chain is formed: the hypotheses 𝔰 ≤ 𝔰₀^⋆, 𝔰₀^♮, 𝔰₀^μ, 𝔰₀^q on
   Q(a, b) are each at most 𝔰_♭, and from sec:tl5-hfy on 𝔰 ≤ 𝔰₁^v ≤ 𝔰₀/2. The sites, at HEAD 0563d28a, old → new:
   - 87:5139 (eq:tl5-hfg-cinf) "C_∞^(m) := 2 max(2C_S, C₁^g, k₁^(m) (2𝔐^(m))^(1/2) max(C_S, C₁^g)),"
       → the entry 2C_S becomes 𝔤₁C_S, in all its forms (C_(∞,μ)^(m), with ν, with 𝔐_p^(m), the outer 2 being
       (1 − 𝔵^z)⁻¹ from sec:tl5-hfy on);
   - 87:5141 "C_(∞,0)^(m) := 2 max(2C_(0,0), C_(1,0)^g, …)" → 2C_(0,0) becomes 𝔤₁C_(0,0), likewise;
   - 87:5174 (lem:tl5-hfg-linfty) "And μ |H(p)| ≤ 2μ |h(p)|." → 𝔤₁μ|h(p)|;
   - 87:5557 (eq:tl5-hfs-linfty) "𝔰_P⁰(p) ≤ 2C_S ℰ_g(p)^(1/2) + 2C_(0,0) η₀(p)," → 𝔤₁C_S, 𝔤₁C_(0,0);
   - 87:5576 (lem:tl5-hfs-linfty) "N − 2, and μ |H(p)| ≤ 2μ |h(p)|; this gives the bound of 𝔰_P⁰(p)." → 𝔤₁;
   - 87:5655 (def:tl5-hfs-constants) "𝔎 := max(2C_S 𝔨_A, C_P^♮ 𝔨_B), … 𝔎₀ := max(2C_(0,0) 𝔨_A, C_(P,0)^♮ 𝔨_B),"
       → max(𝔤₁C_S𝔨_A, C_P𝔨_B), max(𝔤₁C_(0,0)𝔨_A, C_(P,0)𝔨_B); through these 𝔎^D and 𝔎^D₀ (index d);
   - 87:5712 (prop:tl5-hfs-bootstrap, Step 3) "𝔰_P⁰ ≤ 2C_S e^(φ/2) Y_s + 2C_(0,0) η₀" → 𝔤₁;
   - 87:5868 (lem:tl5-hft-small (a)) "and |H(p)| ≤ 2|h(p)|." → 𝔤₁;
   - 87:6044–6045 (lem:tl5-hfq-theta) "(for H the factor 2 of |H| ≤ 2|h| is taken up by 2C_S and 2C_(0,0) in the
       constants)" → 𝔤₁C_S and 𝔤₁C_(0,0);
   - 87:6199–6200 (lem:tl5-hfv-rec) "C_P^v := 2 max(2C_S, C₁, 𝔨_rec)," and "C_(P,0)^v := 2 max(2C_(0,0), C_(1,0),
       𝔨_rec^0)." → (1 − 𝔵^z)⁻¹ max(𝔤₁C_S^l, C₁^l, 𝔨_rec^l), (1 − 𝔵^z)⁻¹ max(𝔤₁C_(0,0), C_(1,0), 𝔨_rec^(0,l)).
   Kept: 87:4323–4325 (lem:tl5-hf-linfty, the constants of thm:tl5-hf, proved under 𝔰 ≤ 1/8 without 𝔰_♭); the factor 2
   of 2𝒥_g in the nonlinear parts of the absorption (87:4338, 5167, and (k₁ + 2𝔵)/(1 − 𝔵) from sec:tl5-hfy on), which
   enters only with 𝔵^z; and 87:5211, whose 𝔨_B already takes 𝔤₁ (thm:tl5-hfv).
3. The closing condition eq:tl5-hfc-closing is eq:tl5-hfe-closing with the constants with index c; it also defines
   Y_c, through 4A_cB_c < 1.

What they give, deduced, not evaluated; upper figures. At G0p's interim optima of thm:tl5-hfe (level 4: −22.01 /
−20.70 / −29.14 / −26.02; level 6: −32.01 / −28.82 / −40.54 / −34.82). Assumptions:
- every supremum at one point: the falls below are those of the leading entry at its supremum; with the new factors the
  supremum, or the leading entry, may move, so the figures are upper figures;
- the term with A of 𝔰_* is its binding part (its ϱ and η₀ terms 9.5–13 decades away, G0l), B fixed, and the part of
  A that moves is ε with the shares of f and ϱ fixed;
- G0p's margins 0.09 / 0.24 / 0.30 in the three level-4 cases where 𝔰_* binds are read as the closing condition's
  spare, x₀ := 4A₀B₀ = 10^(−spare); the closing binds at seed 2 D_A.
Lever 1. If 𝔰_* binds before and both bind after, the term of 𝔰_* with A fixed gives 2A/(1 + (1 − x)^½) = 2A₀, with
x = 4AB; so 1 − (1 − x)^½ = x₀, x = 2x₀ − x₀² and A/A₀ = 2 − x₀.
- Level 4: +0.07 / +0.15 / +0.18 in the three cases where 𝔰_* binds; 0 at seed 2 D_A (x₀ = 1).
- Level 6: 4AB is several decades below 1 (G0o: 𝔰_* sets ε, 5.9 below the closing), so A/A₀ → 2: +0.30 on the ε budget,
  which f and ϱ share; ϱ binds there and f is 0.02–0.5 above, so both move by about +0.30.
Lever 2. The entry of C_P^v that bounds μ|H| falls by 2/𝔤₁ (log₁₀ = 0.301 at 𝔰_♭ = 10⁻⁴).
- Level 4: G0p's 𝔲₁ makes 2C_S the leading entry of C_P^v at 83–100 % of the points; C_P^v falls by the smaller of 0.30
  and the margin of the next entry, max(C₁^l, 𝔨_rec^l), below 2C_S, which is not reported. At the measured 1:1 rate of
  the C_P^v levers, up to +0.30 on min(f, ϱ); G0p's pending price "C_S ÷ 2" is this lever at level 4 up to the μ-small
  entries 𝔷₂′μC_S and μ𝔯_♯C_S of 𝔨_rec^p, which lever 2 does not change.
- The closing at seed 2 D_A: S_F falls where the entry 𝔤₁C_S𝔨_A leads 𝔎; which term of S_F leads there is not reported.
- Level 6: about 0. In C_(∞,μ)^(2) the entry k₁^(2,μ)𝔐_p^(2) leads, and 𝔐_p^(m) carries C_S without the factor of H.
The two levers act on different factors: lever 2 on C_P^v (in 𝔰_* and in S_F), lever 1 on the multiplier of A in 𝔰_*.
At level 4 their upper figures add, about +0.37 to +0.48 where 𝔰_* binds; at level 6 lever 1 alone, +0.30.

Not done (as planned, P-GRD15 if G0p's prices leave room).
- The step of zeroth order with its parts of zeroth order passed to the first derivatives of the shorter words, and a
  smaller leaf weight 𝔶₀ for that step alone (the lever 3a of the plan).
- The parts with ϱ of the products moved from ε into 𝔯, by bounding the factor at a point through its bound at the
  point in place of 𝔰 ≤ 𝔰₁^v (the lever 4 of the plan).
- The weighted Cauchy–Schwarz inequality for 𝔨₁ (3max(r₁, r₂, r₃) → r₁ + r₂ + r₃) and |H| ≤ |h|/(1 − |h|) in place of
  𝔤₁ (a gain of order 𝔰_♭, about 10⁻⁴).

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfc	paper/reader/proofs/P-GRD14.md@PENDING:1	P-GRD14, section	new; at the end of ch:ten-l5, after rem:tl5-hfe-what; the continuation with any threshold Y between the roots of By^2 - y + A, so s_* with the smaller root Y_- in place of 2A; and |H| <= g_1 |h| in place of |H| <= 2|h| in the bounds at a point
    lem:tl5-hfc-cont	paper/reader/proofs/P-GRD14.md@PENDING:15	P-GRD14, Lemma	lem:tl5-continuation with any threshold Y in (Y_-, Y_+) in place of 2A; the solution has y_sigma <= Y_- = 2A/(1 + (1 - 4AB)^(1/2)); A <= Y_- < 2A
    eq:tl5-hfc-y	paper/reader/proofs/P-GRD14.md@PENDING:18	P-GRD14, display	new
    lem:tl5-hfc-h	paper/reader/proofs/P-GRD14.md@PENDING:39	P-GRD14, Lemma	|H| <= g_1 |h| where s <= s_flat; the bounds at a point with g_1 C_S and g_1 C_(0,0) in place of 2C_S and 2C_(0,0)
    def:tl5-hfc-constants	paper/reader/proofs/P-GRD14.md@PENDING:60	P-GRD14, Definition	constants with index c: g_1 C_S, g_1 C_(0,0) in C_P^v, C_(P,0)^v, K, K_0, C_infinity; eta_c, A_c, B_c; Y_c = 2A_c/(1 + (1 - 4A_c B_c)^(1/2)); s_*^c = s_*^c[Y_c]
    eq:tl5-hfc-constants	paper/reader/proofs/P-GRD14.md@PENDING:72	P-GRD14, display	new
    thm:tl5-hfc	paper/reader/proofs/P-GRD14.md@PENDING:74	P-GRD14, Theorem	thm:tl5-hfe with the constants with index c and the threshold Y_c; Y_sigma <= Y_c; its hypotheses are implied by those of thm:tl5-hfe
    eq:tl5-hfc-closing	paper/reader/proofs/P-GRD14.md@PENDING:78	P-GRD14, display	closing condition: 4 eta_c^(-3/2)(delta_w + eta_c^(-1/2)(eps^c + eps_M^c))(S_F^c + S_M^c) < 1
    rem:tl5-hfc-what	paper/reader/proofs/P-GRD14.md@PENDING:121	P-GRD14, Remark	what changes
