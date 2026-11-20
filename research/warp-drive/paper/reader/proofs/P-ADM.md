### Admissible points of the damping and gauge parameters (proof file P-ADM)

This file replaces the existential choice of the damping and gauge parameters in rows c2–c4 and u2–u5 of [[sec:vi-c-1]]
and in steps (1)–(2) of [[thm:vi-c-2-1]] by a definition of admissible points whose conditions are explicit
inequalities or conclusions of named results at the point. Parts A to C are chapter text. The sections after them (the
lead, the placement, the crosswalk rows, the interactions and the side findings) are notes for merging and are not
chapter text. The texts of Parts A to C cite labels that the proof files P-T78 and P-T49 define (eq:tf-lambda,
eq:tf-lambda-point, prop:tf-gauge-explicit, lem:tf-lin-reduction, thm:t49-point); see the interactions.

#### Part A. Chapter 46: the definition, the existence of admissible points, and the theorem

Block A1 goes into [[sec:vi-c-1]] before row c1; block A2 is the new row a1; block A3 is the new text of steps (1)–(2) of
[[thm:vi-c-2-1]]; block A4 goes into [[sec:vi-c-2]] after the paragraph that follows the proof of [[thm:vi-c-2-1]].

*Block A1.*

**Definition {#def:vi-c-admissible}** (Admissible points of the damping and gauge parameters.) Let
(v_C, e_C, C_0) := (½, 1/102400, 100), let c_C be the damping 1-form of [[sec:iv4-0]], and let c_Υ = ζ(|x|)|x|⁻¹dt and
c_(Υ,H) = −½χ(|x|)d|x| be the gauge 1-forms of row u1. For 𝗉 = (h, γ_(Υ,H), e_Υ, γ_Υ) ∈ (0, ∞)⁴ put γ_C := h⁻¹,
s_C := (1 − e_C)(1 − v_C)γ_C and z_Υ := 4e_Υγ_Υ², and let □^C_b, □^Υ_b and L_b be the operators of [[eq:iii-e-1-1]],
[[sec:iii-d-1]] and [[eq:iii-f-1-1]] with the damping (c_C, e_C, γ_C) and the gauge modification
E_Υ = (c_Υ, e_Υ, γ_Υ; c_(Υ,H), γ_(Υ,H)). The point 𝗉 is *admissible* if:

(P0) h ≤ 10⁻⁶, e_Υ < 1 and γ_Υ < ¼;

(P1) for every b in a neighbourhood of b₀, □^C_b has the properties (1) and (2) of [[thm:iii-e-1-1]]: mode stability
for σ ≠ 0, and the invertibility of P^C_b, with (H1)–(H4) and ½ + ϑ_ℋ < −C_0;

(P2) the indicial roots of □^C_b satisfy (C4′) of [[sec:iii-f1-1]]: every non-real one with |ι − 1| ≤ 50 has
non-integer real part;

(P3) there is a neighbourhood ℬ(γ_(Υ,H)) of b₀ such that for every b ∈ ℬ(γ_(Υ,H)) and every σ with Im σ ≥ 0,
(□^Υ_b)^(σ) is invertible, as a map 𝒳_σ → 𝒴_σ when σ ≠ 0, and as a map 𝒳_0 → 𝒴_0 for every s > 3/2 and every α with
α + 2 ∈ (0, ι^Υ_(s1,2)) when σ = 0 (the spaces of [[sec:iii-d1-1]]); this is the conclusion of [[prop:iii-d1-4-1]];

(P4) Λ_tf(γ_Υ, e_Υ) < 1 ([[eq:tf-lambda]]), and for every b in a neighbourhood of b₀, (□^C_b)^(·) is tf-admissible
([[def:i-c-5-1]]) with every weight in (1, 2), as (4) of [[thm:iii-e-1-1]] asserts with every weight in [−C_0, 2).

Each condition is a property of 𝗉 alone, and [[thm:settling]] holds at every admissible point
([[thm:vi-c-adm-holds]]). By (P0), γ_C ≥ 10⁶, so s_C = (1 − e_C)γ_C/2 > 100 and γ_Cv_C > 100, which is (C5) of
[[sec:iii-g2-1]]; (C1) of [[sec:iii-f1-1]] holds ([[lem:iv4-1-3]] (a)); z_Υ ∈ (0, ¼), so the results of [[ch:s13]] and
[[ch:s15]] stated for z ∈ (0, ½] apply; 2γ_Υ < ½ < s_C and γ_Υ < ⅜, so γ_Υ < min(½s_C, ⅜) ([[lem:iii-g1-1-1]]); and
δ_♯ := (1 − e_Υ)γ_Υ lies in (0, ¼). (C1) and (C4) imply (C4′). By (P0) and (P4), L_b^(·) is tf-admissible with every
weight in (0, 1] for b near b₀ ([[prop:iii-f1-3-3]]); Λ_tf(γ_Υ, e_Υ) < 1 holds whenever e_Υ ≤ ½, and at
(γ_Υ, e_Υ) = (1/100, 1/100) it is below 1.0111·10⁻⁴ ([[prop:tf-gauge-explicit]]). No condition asks h to lie in the
set 𝖧 of [[eq:iv4-0-1]], the gauge parameters to lie below the thresholds of [[prop:iii-d1-4-1]] or of
[[lem:iii-d-7-1]] (b), or z_Υ to avoid the set Z_exc of [[prop:iii-f1-2-3]] (e): the proofs use those requirements only
through (P1)–(P4), and the simplicity of indicial roots of L̂_b(0) only where (P0) gives it ([[prop:iii-f1-2-3]] (g)).
[[thm:settling]] uses h ≤ 10⁻⁶ only through s_C > 100 and (C1); [[thm:ec-lb-proved]] uses it directly.
[[rem:ec-point-outside]] records which conditions are decided at the computational point.

**Proposition {#prop:vi-c-adm-exist}** (Admissible points exist.) Let h ∈ 𝖧 ([[eq:iv4-0-1]]) and γ_C := h⁻¹; let
γ_(Υ,H) ∈ (0, ϵ_0], with ϵ_0 of [[prop:iii-d1-4-1]] and its ϵ_1 and ℬ(γ_(Υ,H)) at this γ_(Υ,H); and let
e_Υ ∈ (0, min(ϵ_1, ½)] and γ_Υ ∈ (0, min(ϵ_1, ¼)). Then the point (h, γ_(Υ,H), e_Υ, γ_Υ) is admissible, with the
neighbourhood ℬ(γ_(Υ,H)) of [[prop:iii-d1-4-1]] in (P3). Such points exist, with h, e_Υ and γ_Υ arbitrarily small;
they include the points that satisfy in addition 4e_Υγ_Υ² ∉ Z_exc ([[prop:iii-f1-2-3]] (e)), and those with e_Υ and
γ_Υ below the threshold of [[lem:iii-d-7-1]] (b).

*Proof.* (P0): h ∈ 𝖧 gives h < 10⁻⁶; e_Υ ≤ ½ and γ_Υ < ¼ by the choice. (P1), (P2) and the second half of (P4): at
h ∈ 𝖧, [[thm:iii-e-1-1]] holds for every b near b₀ ([[thm:iv4-2-1]], [[thm:iv6-4-1]]); its (1) and (2) are those
of (P1), its (4) contains the tf-admissibility of (P4), and the clauses of its (3) include (C1) and (C4) of
[[sec:iii-f1-1]], which give (C4′). (P3): (Dyn) holds for b near b₀ ([[thm:vi-a-6-1]], [[thm:vi-b1-5-1]]), and
γ_(Υ,H) ∈ (0, ϵ_0], e_Υ ∈ [0, ϵ_1] and 0 < γ_Υ < ϵ_1; so [[prop:iii-d1-4-1]] gives the invertibility of (P3) for
b ∈ ℬ(γ_(Υ,H)), shrunk if necessary so that (Dyn) holds on it. The first half of (P4): e_Υ ≤ ½ and γ_Υ < ¼ give
Λ_tf(γ_Υ, e_Υ) ≤ 41/64 ([[prop:tf-gauge-explicit]]). Existence: 𝖧 = (0, h_*) ∖ 𝖹 with h_* > 0 and 𝖹 countable, so
𝖧 contains points arbitrarily close to 0; and ϵ_0 and ϵ_1 are positive, so the conditions on γ_(Υ,H), e_Υ and γ_Υ
define non-empty intervals with left end point 0. The further conditions of the last sentence are upper bounds on e_Υ
and γ_Υ and, at fixed e_Υ, the exclusion from an open interval of the countable set {γ > 0 : 4e_Υγ² ∈ Z_exc}, which
leaves points. ∎

*Block A2.*

**a1.** (h, γ_(Υ,H), e_Υ, γ_Υ), with γ_C = h⁻¹: an admissible point ([[def:vi-c-admissible]]), that is (P0)
h ≤ 10⁻⁶, 0 < e_Υ < 1 and 0 < γ_Υ < ¼, with (P1)–(P4): the properties (1)–(2) of [[thm:iii-e-1-1]], (C4′) of
[[sec:iii-f1-1]], the conclusion of [[prop:iii-d1-4-1]], and Λ_tf(γ_Υ, e_Υ) < 1 with the tf-admissibility of □^C_b at
the weights in (1, 2) ([[sec:iii-f-1]], [[sec:iii-g2-1]], [[sec:iii-i10-1]], [[eq:iii-c-1-1]], [[sec:iii-k-0]],
[[prop:iii-f1-3-3]]). Threshold: c1, u1; every condition is a property of the point alone.

*Block A3.*

(1) The damping and the gauge (row a1). (v_C, e_C, C_0) := (½, 1/102400, 100), and an admissible point
(h, γ_(Υ,H), e_Υ, γ_Υ) of [[def:vi-c-admissible]], γ_C := h⁻¹. Admissible points exist ([[prop:vi-c-adm-exist]]),
and at each the results of the stability theory hold ([[thm:vi-c-adm-holds]] (1)).

(2) The numbers the point fixes. By (P0), 0 < e_Υ < 1, 0 < γ_Υ < ¼, z_Υ := 4e_Υγ_Υ² ∈ (0, ¼), s_C > 100 and
γ_Cv_C > 100, which is (C5), and (C1) holds; by (P4), L_b^(·) is tf-admissible with every weight in (0, 1]
([[prop:iii-f1-3-3]]). The point fixes δ_♯ := (1 − e_Υ)γ_Υ ∈ (0, ¼), the set σ_Υ, the constant ε_Υ of
[[sec:iii-d2-1]], a constant ε_ind ∈ (0, 1] with [[eq:iii-f1-2-2]] ([[prop:iii-f1-2-3]] (f), under (P2)), and the
neighbourhood ℬ(γ_(Υ,H)) of (P3). [[prop:iii-d-6-3]] (the invertibility of the spectral family of □^Υ_b for
σ with |σ| ≥ c_σ) is implied, for every c_σ and b ∈ ℬ(γ_(Υ,H)), by (P3), which gives it for every σ with Im σ ≥ 0; so
it imposes no further condition.

*Block A4.*

**Theorem {#thm:vi-c-adm-holds}** (The stability theory at an admissible point.) Let 𝗉 = (h, γ_(Υ,H), e_Υ, γ_Υ) be
an admissible point ([[def:vi-c-admissible]]), with γ_C = h⁻¹, the constants of row c1, the 1-forms of row u1 and the
neighbourhood ℬ(γ_(Υ,H)) of its condition (P3).

(1) Every result of [[ch:s13]] from [[sec:iii-d2-1]] on, [[lem:iii-d1-5-1]], every result of [[ch:s14]] from
[[sec:iii-e-2]] to [[sec:iii-e1-3]], and every result of [[ch:s15]] to [[ch:s29]] holds at 𝗉, with its proof.

(2) [[thm:vi-c-2-1]] holds with its step (1) made at 𝗉, and [[thm:iii-k-4-3]], [[cor:s27-rate]],
[[thm:settling-precise]] and [[thm:settling]] hold with the parameters so chosen.

*Proof.* (1) We list every way in which these proofs use the damping and gauge parameters, and show that each is
available at 𝗉.

*The damping.* (a) The properties (1) and (2) of [[thm:iii-e-1-1]]: in [[prop:iii-f2-3-1]], [[prop:iii-f3-4-1]], Step 4
of the proof of [[prop:iii-f4-5-1]] and [[lem:iii-e-2-1]], and through the last in [[prop:iii-e-3-1]] and
[[prop:iii-e1-3-1]]. These are (P1). (b) The clause (C1): in the list of [[prop:iii-f1-2-3]] and its parts (a)–(d) and
(g), in [[lem:iii-e-2-1]] (2), in [[thm:iii-g-5-1]], and in the settings of [[ch:s16]], [[sec:iii-f3-1]],
[[sec:iii-g2-1]] and [[sec:iii-h-1]]. It follows from (P0), by [[lem:iv4-1-3]] (a). (c) The clause (C4): only through
[[prop:iii-f1-2-3]] (f), which assumes only (C4′), that is (P2). (d) The clauses (C2)–(C3) and the condition z_Υ ∉ Z_exc:
only through [[prop:iii-f1-2-3]] (e), whose conclusion, the simplicity of the roots of L̂_b(0), is used only for roots
with real part in (−3, 0]: the root 0 in [[lem:iii-f1-2-5]] and [[lem:iii-g1-1-3]] (b), through (c) of
[[prop:iii-f1-2-3]]; the root −2 at the types s2, v2 and t2 in [[sec:iii-f4-5]]; and the roots of 𝒲(ℓ_K), ℓ_K < ℓ_K^max ≤
3, in [[lem:iii-g2-1-2]], [[thm:iii-g2-3-1]], [[lem:iii-g4-1-1]] (2), [[lem:iii-g4-3-4]], [[thm:iii-g4-3-1]],
[[prop:iii-g4-5-1]] (through the residues Π_μ) and [[lem:iii-i12-2-3]]. By (c) and (g) of [[prop:iii-f1-2-3]], which use
only z_Υ ∈ (0, ½] and (C1), every root with real part in [−101, 0] is real and simple at 𝗉, and these proofs cite (c),
the list or (g) for it. No other proof uses the simplicity of a root of L̂_b(0); those that meet roots of real part below
−101 or above 1 allow them any finite multiplicity ([[lem:iii-g1-1-3]], [[def:iii-i10-1-1]]). (e) The property (4) of
[[thm:iii-e-1-1]]: only in Step 4 of the proof of [[prop:iii-f1-3-3]], at the weights in (1, 2), which is in (P4). (f)
The inequality s_C > 100: in [[sec:iii-f-1]], [[eq:iii-i1-1-1]], [[sec:iii-c1-0]], [[sec:iv2-0]], [[sec:iii-k-0]] and row
d2, and through the bound ℓ_I < 3/2 + s_C in [[thm:iii-g1-3-1]], [[eq:iii-g3-1-2]] and [[sec:iii-i10-1]]; and (C5), in
[[sec:iii-g2-1]] and [[sec:iii-i10-1]]. These follow from (P0). (g) The horizon threshold of [[lem:iii-f2-1-1]] and the
bound of [[cor:iii-f2-1-2]] hold for every γ_C. (h) The set 𝖧, the thresholds h_0 and h_tf and the sets 𝖹, 𝖹₁, 𝖹₂ and 𝖹₃
enter only through [[thm:iii-e-1-1]] and through [[prop:np-10-52]] (ii)–(iii), whose conclusions are those of
[[prop:iii-f1-2-3]] (e)–(f) at z = 4·10⁻⁶; so only through (a)–(f). The bound h ≤ 10⁻⁶ enters through s_C > 100 and (C1).

*The gauge.* (i) The mode stability of □^Υ_b: in the setting of [[sec:iii-d2-1]] and in [[lem:iii-d1-5-1]] (the
invertibility of (□^Υ_b)^(0)), in [[prop:iii-f2-3-1]], [[rem:iii-f3-2-3]] and [[prop:iii-f3-4-1]] (kernels of □^Υ),
and through ℬ(γ_(Υ,H)) in row b2; [[prop:iii-d-6-3]] is implied by it. This is (P3). (j) The tf-admissibility of L_b:
in [[cor:iii-f1-3-4]], [[prop:iii-g-3-2]], [[sec:iii-g-4-1]], [[lem:iii-g-4-5]], [[thm:iii-g-5-1]], [[sec:iii-h-1]],
[[thm:iii-h1-1-3]] and [[thm:iii-h2-2-1]]. [[prop:iii-f1-3-3]] gives it at 𝗉: its hypotheses (C1), 0 < e_Υ < 1,
γ_Υ > 0, z_Υ ≤ ½ and Λ_tf(γ_Υ, e_Υ) < 1 hold by (P0) and (P4), and its proof uses besides only (P4) (in Step 4),
[[lem:tf-lin-reduction]] and [[prop:tf-gauge-explicit]]. (k) The threshold of [[lem:iii-d-7-1]] (b) is used only in
the proof of [[prop:iii-d1-4-1]] ([[sec:iii-d1-1]]), outside the results of (1); elsewhere [[lem:iii-d-7-1]] enters
through its part (a) or through its proof at γ_Υ = 0. (l) The inequalities 0 < e_Υ < 1 and
0 < γ_Υ < ¼: in [[eq:iii-c-1-1]], [[prop:np-10-38]], the opening of [[ch:s19]], [[sec:s20-setting]], [[sec:iii-i9-1]],
[[sec:iii-c1-0]] and row d1; γ_Υ < min(½s_C, ⅜): in [[lem:iii-g1-1-1]], [[thm:iii-g1-3-1]], [[sec:iii-g2-1]],
[[sec:iii-g3-1]] and [[lem:iii-g3-1-2]]; and z_Υ ∈ (0, ½]: in [[lem:iii-d-4-1]], in the constant ε_Υ of
[[sec:iii-d2-1]], in (R1)–(R5) of [[sec:iii-d3-1]] with [[prop:np-10-29]] and [[prop:np-10-30]], in
[[prop:iii-f1-2-3]] and in [[lem:iii-g1-1-3]]. These follow from (P0), as [[def:vi-c-admissible]] records.

*Continuity and the rest.* [[lem:iii-d-5-1]], [[prop:iii-d-6-1]], [[lem:iii-f2-1-1]], [[cor:iii-f2-1-2]],
[[lem:iii-f1-2-4]] and [[lem:iii-f1-3-2]] hold for parameters in a compact set and are applied with the compact set
{𝗉}. Every other smallness in [[ch:s18]] to [[ch:s29]] concerns the metric perturbation, the data, neighbourhoods of
b₀, the thresholds of the Nash–Moser theorem, the cut-off time or the gluing; none of these involves 𝗉 except through
the numbers s_C, z_Υ, δ_♯, σ_Υ, ε_ind, ε_Υ and Λ and the neighbourhoods of b₀ that 𝗉 fixes.

(2) In [[thm:vi-c-2-1]], steps (0) and (3)–(6) and their thresholds see 𝗉 only through the numbers and the
neighbourhood of its step (2) and through results that hold at 𝗉 by (1), so its proof applies. [[thm:iii-k-4-3]],
[[prop:vii-3-2]], [[cor:s27-rate]] and [[cor:vii-2-3]] are results of (1) at the parameters so chosen.
[[thm:settling-precise]] is proved in [[ch:settling-proof]] from these and from results that do not involve the
damping and gauge parameters, and [[thm:settling]] is deduced from it there. ∎

#### Part B. Chapter 34: the clause (C4′) and the part (g) of the indicial roots

Block B1 replaces the clause (C4) of [[sec:iii-f1-1]] by (C4) followed by (C4′); block B2 is the new part (g) of the
statement of [[prop:iii-f1-2-3]]; block B3 is the new end of its proof, (f) under (C4′) and the proof of (g). The
hypothesis of (f) becomes (C4′) (Placement, item 3).

*Block B1.*

(C4) Every indicial root of □^C_b whose real part is an integer in [3, 51] is real.

(C4′) Every non-real indicial root ι of □^C_b with |ι − 1| ≤ 50 has non-integer real part. Under (C1), (C4) implies
(C4′): such a root has |Re ι − 1| ≤ 50, so Re ι ≥ 2 by (C1), and Re ι = 2 only at the real root ι = 2; so an integer
real part would lie in [3, 51], where (C4) would make the root real.

*Block B2.*

ε_ind enters only through [[eq:iii-f1-2-2]], never as a number of order one. (g) Every root with real part in
[−C_0 − 1, 0] is real, and at each type and degree at which it is a root it occurs once in the list, so that it is a
simple zero of the determinant of the indicial matrix N_L there; this needs neither (C2)–(C3) nor z ∉ Z_exc, and it
covers the roots with real part in (−3, 0] that [[ch:s16]] and [[ch:s17]] use.

*Block B3.*

would make ι^C_(·,+) = ι + 1 non-real, with |ι^C_(·,+) − 1| = |ι| ≤ 50 and real part n + 1 ∈ [3, 51], against
(C4′). The minimum of d(Re ι, ℤ) over this finite set is positive, and ε_ind is any number in (0, 1] not exceeding it.

*(g)* By (d), the entries before the semicolons that come from □^C have real part < −C_0 − 1; this includes the root
−2 − 2γ_Cv_C at v1, which is ι^C_(v1,≪) − 1 by [[lem:iii-f1-2-2]] and (C1). By (b), the entries after the semicolons
have real part > 1. So a root with real part in [−C_0 − 1, 0] is one of the following entries, all real
([[lem:iii-d-4-1]]): at s0, 2 − ι^Υ_(s0,2) and 0; at s1, 2 − ι^Υ_(s1,3), 2 − ι^Υ_(s1,2) and −1; at sl, l ≥ 2, −l,
2 − ι^Υ_(sl,l+2), 2 − ι^Υ_(sl,l+1) and 2 − l; at v1, −1; at vl, l ≥ 2, −l and 1 − l; at tl, −l. At each type and
degree these entries are pairwise distinct, by the bounds above: at s0, 2 − ι^Υ_(s0,2) ∈ [−z/3, 0); at s1,
−5/4 < 2 − ι^Υ_(s1,3) < −1 < −¼ < 2 − ι^Υ_(s1,2) < 0; at sl, the chain of the proof of (e),
−l − ¼ < 2 − ι^Υ_(sl,l+2) < −l < 1 − l − ¼ < 2 − ι^Υ_(sl,l+1) < 1 − l < 2 − l; and at vl, −l < 1 − l. So each such
root occurs once in the list of each type and degree at which it is a root. The list gives the zeros of det N_L at
that type and degree with multiplicity ([[lem:iii-f1-2-1]] and the first paragraph of this proof), so each is a
simple zero. Only z ∈ (0, ½], (C1) and [[lem:iii-f1-2-2]] were used. ∎

#### Part C. Chapter 71: the computational point

The new [[rem:ec-point-outside]], which combines this file's statement of what is decided at the computational point with
the texts of P-LB (merged), P-T78 (its text 8) and P-T49 (its text 7).

**Remark {#rem:ec-point-outside}** (The computational point and the proved set.) [[thm:settling]] holds at every
admissible point of the gauge and damping parameters ([[def:vi-c-admissible]], [[thm:vi-c-adm-holds]]); no threshold
and no exceptional set in that definition excludes the computational point. Completed by any γ_(Υ,H) > 0, it
satisfies (P0), as h = 10⁻⁶ and e_Υ = γ_Υ = 1/100 (so s_C = 499995.1171875); in (P1), the hypotheses (H1)–(H4) with
½ + ϑ_ℋ < −C_0 contained in (2) of [[thm:iii-e-1-1]], by [[lem:iv4-1-5]] and [[lem:iv4-1-6]]; (P2), by
[[prop:s14-damping-distance]], since the indicial roots of □^C_b are the roots of P_l, P_0 and p_(v); and, in (P4),
Λ_tf(γ_Υ, e_Υ) < 1.0111·10⁻⁴ ([[eq:tf-lambda-point]]). Three conditions are not decided. First, in (P1), the mode
stability (1) of [[thm:iii-e-1-1]] and the invertibility of P^C_b in its (2), at γ_C = 10⁶ and b near b₀:
[[thm:iv4-2-1]] proves them only for h below a threshold of [[thm:iv5-7-3]] whose existence is proved and whose
value is not determined. Second, in (P4), the tf-admissibility of □^C_b at γ_C = 10⁶ with the weights in (1, 2), which
[[thm:iv6-4-1]] proves only for h below the threshold h_tf of [[thm:iv6-3-1]]. Third, (P3): the invertibility of
(□^Υ_b)^(σ) for every σ with Im σ ≥ 0 at (e_Υ, γ_Υ) = (1/100, 1/100), for some γ_(Υ,H) > 0 and every b near b₀, which
[[prop:iii-d1-4-1]] gives only for γ_(Υ,H) ≤ ϵ_0 and e_Υ, γ_Υ below a threshold ϵ_1 that depends on γ_(Υ,H), both
proved to exist with values not determined. As [[lem:iii-d-7-1]] (a) gives the tf-admissibility of σ ↦ (□^Υ_b)^(σ) at
these parameters for every b and every γ_(Υ,H), (P3) follows from its case b = b₀ by the argument of Step 2 of the
proof of [[prop:iii-d1-4-1]]. [[def:ec-point]] does not fix γ_(Υ,H), and no number of this chapter depends on it: the
horizon thresholds that enter do not involve it ([[lem:iii-d-5-1]], and [[lem:iii-f2-1-1]], where y = 0 for the
1-form c_(Υ,H) = −½χ dr), and the indicial roots of (□^Υ_b)^(0), which fix ℳ and ε_Υ, do not depend on the horizon
modification ([[sec:iii-d2-1]]). The definition asks no simplicity of the indicial roots of L̂_b(0) beyond what (P0)
gives ([[prop:iii-f1-2-3]] (g)); at the point every root of real part in [−101, 5] is simple ([[prop:is-mult]]), and
the point also avoids the countable exclusions of [[eq:iv4-0-1]] and [[prop:iii-f1-2-3]] (e), which the definition
does not ask: h = 10⁻⁶ ∉ 𝖹, and Z_exc is empty at h = 10⁻⁶ ([[thm:t49-point]]). So the computational point is a point
at which the formulas of the proof can be evaluated, not one at which the hypotheses of [[thm:settling]] are shown to
hold. Every number of this chapter that depends on the point is stated at it. For h ∈ 𝖧 the theorems use only
0 < ε_ind(h) ≤ δ_50 ([[prop:np-10-52]] (iii)), and the lower bound of [[thm:loss-d]] uses besides only
ε_Υ < 1.46214·10⁻¹⁰, which holds at every h, ε_Υ being fixed by (γ_Υ, e_Υ) ([[lem:ec-gauge-gap]], [[prop:ec-rounds]]).
At every point of the proved set a lower bound for d holds as an explicit function of z = 4e_Υγ_Υ² and h, with no
threshold evaluated, through bounds for ε_Υ and ε_ind(h) that hold at every such point ([[lem:ec-lb-gauge]],
[[lem:ec-lb-ind]], [[thm:ec-lb-proved]]).

### The lead: every use of the simplicity of indicial roots

This section closes the lead of the audit. It lists every use, in the chapters, of the simplicity of an indicial root of
L̂_b(0), of the condition z_Υ ∉ Z_exc, of (C2), of (C3) and of row u5, directly or through a cited result, and says which
roots each concerns. The search was made over chapters 20–48 and 60–71 for "simple", "simplicity", "multiplicity",
"logarithm", "one-dimensional", "adj", "simple pole", Z_exc, (C2), (C3), u5, [[prop:iii-f1-2-3]] (every citation, by
part), [[lem:iii-g4-1-1]], [[lem:iii-g2-1-2]], [[thm:iii-g2-3-1]] and [[sec:iii-g2-1]]; each hit was read in context.
Uses of the simplicity of the roots of the gauge potential operator (automatic for z > 0, [[lem:iii-d-4-1]]), of
matrices (S̄ in [[lem:iii-g1-1-1]]) and of poles at ι⁺ are not uses of the property in question and are omitted.

(U1) [[prop:iii-f1-2-3]] (c), the root 0 at s0 and s2: used in [[lem:iii-f1-2-5]] (34:532) and [[lem:iii-g1-1-3]] (b)
(35:1103). Real part 0. Part (c) is proved from the list and the bounds alone, with no use of (C2), (C3) or Z_exc.

(U2) The root −2 at the types s2, v2 and t2 (34:1811, [[sec:iii-f4-5]]), cited to [[prop:iii-f1-2-3]] (the list). Real
part −2.

(U3) The standing hypothesis of [[sec:iii-g2-1]] (35:1422–1426), "(C2)–(C3) ... with z_Υ outside Z_exc ..., so that every
indicial root of L̂_b(0) is simple", used in [[lem:iii-g2-1-2]] (35:1493, "the hypothesis on z_Υ"), for μ ∈ 𝒲(ℓ_K), ℓ_K <
ℓ_K^max ≤ 3, that is −3 < μ ≤ 0; and in [[thm:iii-g2-3-1]] (35:1636, "As μ is a simple root"), for a root μ = −z with α <
Re z = z_0 < ℓ_K, α ∈ (−1, 0), so −3 < Re μ < 1 and, by (a), −3 < Re μ ≤ 0.

(U4) The standing hypothesis of [[sec:iii-g4-1]] (36:1138, "z_Υ ∉ Z_exc, so that every indicial root of L̂_b(0) is
simple"), used in [[lem:iii-g4-1-1]] (2) (36:1153–1166), whose statement is made at every root; the lemma is used in
[[lem:iii-g4-3-4]] (36:1360), at the roots −μ in a strip {b < Re λ < b̃} with −1 < b < b̃ ≤ w₀ < ℓ_K^max ≤ 3, so −3 < Re
μ ≤ 0; through it in [[thm:iii-g4-3-1]] (36:1423, "the multiplicities are one per type, as each root is simple", over
𝒲(w₀)); and in Step 2 of the proof of [[prop:iii-g4-5-1]] (36:1698, the residues Π_μ for μ ∈ 𝒲(w), w < 3). Its other
citations (37:546, 38a:56, 39:85, 36:1226, 36:1552, 36:1706) use its parts (1) and (3) only.

(U5) [[lem:iii-i12-2-3]] (41:1203–1205): "the roots being simple" for the roots of real part in (a, 1), a > −3, so −3 <
Re μ ≤ 0, and "As every indicial root is simple ([[sec:iii-g2-1]])" at the least exponent μ_0 ∈ (−3, 0].

(U6) Row u5 and step (2) of [[thm:vi-c-2-1]] (46:1736, 46:1793–1795): they impose z_Υ ∉ Z_exc for (U3)–(U4) only.

(U7) (C2) and (C3) themselves (34:290–294): used only in the proof of [[prop:iii-f1-2-3]] (e) (34:479–483) and in the
hypothesis of (U3). (C2) is also a clause of [[thm:iii-e-1-1]] (3); no proof cites that clause otherwise.

Places that meet roots outside the window allow multiplicity and use no simplicity: the index set ℰ_K
([[lem:iii-g1-1-3]], 35:1094: "(−μ, k) with k below the order of the root"), the count l_* of [[def:iii-i10-1-1]]
(41:154–156, which bounds "the multiplicities of the indicial roots of L̂_b(0)" at real part at most 5), the expansions
by [[lem:iii-a-1-4]] in [[prop:iii-f4-5-1]] Step 3, [[lem:iii-i11-2-1]] and [[cor:iii-g2-3-2]], and the finiteness
statements cited to (f) (36:1166, 43:68, 43:553). [[prop:is-mult]] (71) proves simplicity on [−101, 5] at the
computational point and is used by no theorem outside its chapter.

Conclusion: every use concerns roots with real part in (−3, 0]. On [−101, 0] simplicity holds for every z ∈ (0, ½] under
(C1) alone: this is the new part (g) of [[prop:iii-f1-2-3]], proved in full in block B3 from the list of that
proposition, (d) (which uses (C1)), [[lem:iii-f1-2-2]] and the interval bounds [[eq:iii-d-4-2]]: at s0, 2 − ι^Υ_(s0,2) ∈
[−z/3, 0); at s1, −5/4 < 2 − ι^Υ_(s1,3) < −1 < −¼ < 2 − ι^Υ_(s1,2) < 0; at sl, l ≥ 2, −l − ¼ < 2 − ι^Υ_(sl,l+2) < −l < 1
− l − ¼ < 2 − ι^Υ_(sl,l+1) < 1 − l < 2 − l; at vl, −l < 1 − l; and the root −2 − 2γ_Cv_C at v1 is ι^C_(v1,≪) − 1 < −101
by (C1). So the lead is confirmed: u5, (C2), (C3) and the global simplicity are not needed, and the sites (U3)–(U6) are
rewritten to cite (g) or removed (Placement, items 6, 8–14, 16, 21 and 27). (e) itself stays, true and unused.

### Placement

Each item names the place, the old text and the new text, given as lines of the chapter, with the line breaks shown. Line
numbers are those of the chapters after the merge of P-LB (commit a722cb42) and serve only to find the place; every old
text occurs exactly once in its chapter. Items marked "combined" replace the item of another proof file at the same
place, as the interactions section says. Items 33–38 amend the section of the lower bound that P-LB merged into
[[ch:explicit-constants]].

*1. [[ch:s15]], [[sec:iii-f-1]], the paragraph that fixes the parameters (lines 76–77).* Old, the two lines:

fixed in [[sec:iv4-0]], for which (1 − e_C)(1 − v_C)γ_C > 100 and the constraint propagation operator □^C_b of
[[eq:iii-e-1-1]] has the properties of [[thm:iii-e-1-1]]. The *linearised gauge-fixed Einstein operator* is

New, the four lines:

fixed in [[sec:iv4-0]], for which (1 − e_C)(1 − v_C)γ_C > 100 and the constraint propagation operator □^C_b of
[[eq:iii-e-1-1]] has the properties of [[thm:iii-e-1-1]]. Every result below holds as well, with the same proof, at
every admissible point of the parameters ([[def:vi-c-admissible]], [[thm:vi-c-adm-holds]]). The *linearised
gauge-fixed Einstein operator* is

*2. [[ch:s15]], [[sec:iii-f1-1]], the clause (C4) (line 295).* Old, the line:

(C4) Every indicial root of □^C_b whose real part is an integer in [3, 51] is real.

New: Block B1 of Part B.

*3. [[ch:s15]], [[prop:iii-f1-2-3]] (f), its hypothesis (line 443).* Old, the line:

determined by the roots of □^C_b, such that for z ∉ Z_exc every root is simple. (f) If (C4) holds, then for every R > 0

New, the line:

determined by the roots of □^C_b, such that for z ∉ Z_exc every root is simple. (f) If (C4′) holds, then for every R > 0

*4. [[ch:s15]], [[prop:iii-f1-2-3]], the clause (g) added to the statement (line 454).* Old, the line:

ε_ind enters only through [[eq:iii-f1-2-2]], never as a number of order one.

New: Block B2 of Part B.

*5. [[ch:s15]], the proof of [[prop:iii-f1-2-3]], the end of (f) and the proof of (g) (lines 496–497).* Old, the two
lines:

would make ι^C_(·,+) non-real with real part n + 1 ∈ [3, 51], against (C4). The minimum of d(Re ι, ℤ) over this finite
set is positive, and ε_ind is any number in (0, 1] not exceeding it. ∎

New: Block B3 of Part B.

*6. [[ch:s16]], [[sec:iii-g2-1]], the standing hypotheses (lines 1423–1426).* Old, the four lines:

g_b, b near b_0, by [[thm:vi-a-6-1]] and [[thm:vi-b1-5-1]]; the parameters of [[prop:iii-f1-3-3]] with
γ_Υ < min(½s_C, ⅜) ([[lem:iii-g1-1-1]]); (C1) of [[sec:iii-f1-1]]; and (C2)–(C3) of [[sec:iii-f1-1]] with
z_Υ = 4e_Υγ_Υ² outside the exceptional set Z_exc of [[prop:iii-f1-2-3]] (e), so that every indicial root of L̂_b(0) is
simple. We fix

New, the four lines:

g_b, b near b_0, by [[thm:vi-a-6-1]] and [[thm:vi-b1-5-1]]; the parameters of [[prop:iii-f1-3-3]] with
γ_Υ < min(½s_C, ⅜) ([[lem:iii-g1-1-1]]); and (C1) of [[sec:iii-f1-1]], with z_Υ = 4e_Υγ_Υ² ∈ (0, ½]. Then every
indicial root μ of L̂_b(0) with −101 ≤ Re μ ≤ 0 is real and simple ([[prop:iii-f1-2-3]] (g)); the roots used below
lie in (−3, 0]. We fix

*7. [[ch:s16]], [[sec:iii-g2-1]], the sentence after (C5) (lines 1435–1436).* Old, the two lines:

ℓ_K^max = 3. The choice of parameters in [[thm:vi-c-2-1]] satisfies (C5), as there v_C = ½ and γ_C > 10⁶. Without
(C5) every statement below holds with ℓ_K^max = 2 + 2γ_Cv_C, which still serves every graft at

New, the three lines:

ℓ_K^max = 3. The choice of parameters in [[thm:vi-c-2-1]] satisfies (C5): at every admissible point
([[def:vi-c-admissible]]) v_C = ½ and s_C > 100, so γ_Cv_C > 100. Without (C5) every statement below holds with
ℓ_K^max = 2 + 2γ_Cv_C, which still serves every graft at

*8. [[ch:s16]], the proof of [[lem:iii-g2-1-2]] (lines 1493–1494).* Old, the two lines:

determinant has μ as a simple zero (the hypothesis on z_Υ). So its kernel is one-dimensional for each Y in a basis of
𝒴_τ, and depends linearly on Y. The leading term h̄ = ρ^μφ(ω) of the state lies in the kernel. Indeed it satisfies

New, the three lines:

determinant has μ as a simple zero ([[prop:iii-f1-2-3]] (g), as −3 < μ ≤ 0). So its kernel is one-dimensional for
each Y in a basis of 𝒴_τ, and depends linearly on Y. The leading term h̄ = ρ^μφ(ω) of the state lies in the kernel.
Indeed it satisfies

*9. [[ch:s16]], the proof of [[thm:iii-g2-3-1]], *The lowest term* (lines 1636–1637).* Old, the two lines:

N(A_0, z)c_(z,J−1) + J∂_zN(A_0, z)c_(z,J) = 0. Hence z = −μ for a root μ, which is real, so z = z_0. As μ is a simple
root, ∂_zN(A_0, z) maps ker N(A_0, z) injectively into a complement of the range of N(A_0, z). So Jc_(z,J) = 0, J = 0,

New, the three lines:

N(A_0, z)c_(z,J−1) + J∂_zN(A_0, z)c_(z,J) = 0. Hence z = −μ for a root μ with α < −Re μ < ℓ_K, so −3 < Re μ ≤ 0
([[prop:iii-f1-2-3]] (a)), and μ is real and simple ([[prop:iii-f1-2-3]] (g)); so z = z_0. As μ is a simple root,
∂_zN(A_0, z) maps ker N(A_0, z) injectively into a complement of the range of N(A_0, z). So Jc_(z,J) = 0, J = 0,

*10. [[ch:s17]], [[sec:iii-g4-1]], *The operator* (line 1138).* Old, the line:

[[sec:iii-g2-1]]; in particular z_Υ ∉ Z_exc, so that every indicial root of L̂_b(0) is simple ([[prop:iii-f1-2-3]] (e)).

New, the two lines:

[[sec:iii-g2-1]]; in particular every indicial root μ of L̂_b(0) with −101 ≤ Re μ ≤ 0 is real and simple
([[prop:iii-f1-2-3]] (g)).

*11. [[ch:s17]], [[lem:iii-g4-1-1]] (2), the statement (lines 1154–1155).* Old, the two lines:

û(λ) := ∫ r̂^(−λ)u dr̂/r̂) is N₀(λ) = 𝒩(−λ), its roots are −μ for the roots μ of L̂_b(0), and at each −μ the inverse
N₀(λ)⁻¹ has a simple pole whose residue Π_μ has range ker 𝒩(μ). (3) N_tf(2L̂_b, ±1) = 2N_tf ([[eq:i-c-4-1]]).

New, the three lines:

û(λ) := ∫ r̂^(−λ)u dr̂/r̂) is N₀(λ) = 𝒩(−λ), its roots are −μ for the roots μ of L̂_b(0), and at each −μ with
−101 ≤ Re μ ≤ 0 the inverse N₀(λ)⁻¹ has a simple pole whose residue Π_μ has range ker 𝒩(μ).
(3) N_tf(2L̂_b, ±1) = 2N_tf ([[eq:i-c-4-1]]).

*12. [[ch:s17]], the proof of [[lem:iii-g4-1-1]] (2) (lines 1162–1164).* Old, the three lines:

(2) The first statement is the definition. The roots are simple, so on each isotypic component (type and harmonic) the
determinant of the matrix polynomial 𝒩(λ) has a simple zero at μ, and 𝒩(λ)⁻¹ = adj 𝒩(λ)/det 𝒩(λ) has a simple pole
with residue adj 𝒩(μ)/(det 𝒩)′(μ). Its range lies in ker 𝒩(μ), as 𝒩(μ) adj 𝒩(μ) = 0, and it is non-zero, as the

New, the four lines:

(2) The first statement is the definition. A root μ with −101 ≤ Re μ ≤ 0 is simple ([[prop:iii-f1-2-3]] (g)), so on
each isotypic component (type and harmonic) at which it is a root the determinant of the matrix polynomial 𝒩(λ) has a
simple zero at μ, and 𝒩(λ)⁻¹ = adj 𝒩(λ)/det 𝒩(λ) has a simple pole with residue adj 𝒩(μ)/(det 𝒩)′(μ). Its range
lies in ker 𝒩(μ), as 𝒩(μ) adj 𝒩(μ) = 0, and it is non-zero, as the

*13. [[ch:s17]], the proof of [[lem:iii-g4-3-4]] (lines 1359–1360).* Old, the two lines:

continues ℳR meromorphically to {Re λ < b̃}. In the strip {b < Re λ < b̃}, of width at most 1, the poles are at the
roots −μ in it ([[lem:iii-g4-1-1]] (2)) and at the at most one z_j(α) in it, all simple; for D small none is on the

New, the three lines:
    def:vi-c-admissible	paper/reader/proofs/P-ADM.md:17	P-ADM, Definition (admissible points)	new: (P0)–(P4)
    prop:vi-c-adm-exist	paper/reader/proofs/P-ADM.md:52	P-ADM, Proposition (existence)	new: contains the former rows
    thm:vi-c-adm-holds	paper/reader/proofs/P-ADM.md:95	P-ADM, Theorem (admissible points)	new: thm:settling holds there
continues ℳR meromorphically to {Re λ < b̃}. In the strip {b < Re λ < b̃}, of width at most 1, the poles are at the
roots −μ in it, which have −3 < Re μ ≤ 0, as −1 < b < b̃ ≤ w₀ < 3 ([[prop:iii-f1-2-3]] (a)), and so are simple poles
([[lem:iii-g4-1-1]] (2)), and at the at most one z_j(α) in it, also simple; for D small none is on the

*14. [[ch:s17]], the end of the proof of [[thm:iii-g4-3-1]] (line 1423).* Old, the line:

as each root is simple. ∎

New, the line:

as each root of 𝒲(w₀) is simple ([[prop:iii-f1-2-3]] (g)). ∎

*15. [[ch:s22]], [[sec:iii-i10-1]], after (H4) (line 124).* Old, the line:

[[thm:iii-g2-4-2]] is no restriction, s_C being large by (C1) of [[ch:s15]].

New, the line:

[[thm:iii-g2-4-2]] is no restriction, as s_C > 100 ([[sec:iii-f-1]]).

*16. [[ch:s22]], the proof of [[lem:iii-i12-2-3]], *The reduction* (lines 1204–1206).* Old, the three lines:

logarithm can occur only where a root meets a lower one plus an integer, so the lowest exponent carries none, the roots
being simple. Let μ_0 be the least real part of an exponent of X, and suppose μ_0 ≤ 0. As every indicial root is simple
([[sec:iii-g2-1]]), the argument of the proof of [[thm:iii-g2-3-1]] (the lowest term) applies: the top logarithm at μ_0

New, the four lines:

logarithm can occur only where a root meets a lower one plus an integer, so the lowest exponent carries none, the roots
of real part in (a, 1) lying in (−3, 0] ([[prop:iii-f1-2-3]] (a)) and being simple ([[prop:iii-f1-2-3]] (g)). Let μ_0
be the least real part of an exponent of X, and suppose μ_0 ≤ 0. As the roots of real part μ_0 > −3 are simple, the
argument of the proof of [[thm:iii-g2-3-1]] (the lowest term) applies: the top logarithm at μ_0

*17. [[ch:s23]], the setting (the paragraph that opens with "Everything of [[sec:iii-i14-1]] is kept") (lines 559–560).*
Old, the two lines:

ℓ_I > 3 + ε_+ ((H4) of [[sec:iii-i10-1]]), and [[eq:iii-g3-1-2]] holds, s_C being large by (C1). K_ι(λ) denotes the
order of the pole of [[eq:iii-g3-2-2]] at λ (K(λ) in [[prop:iii-g3-3-7]] and in [[eq:iii-g3-3-6]]). Also from

New, the three lines:

ℓ_I > 3 + ε_+ ((H4) of [[sec:iii-i10-1]]), and [[eq:iii-g3-1-2]] holds, as s_C > 100 ([[sec:iii-f-1]]). K_ι(λ)
denotes the order of the pole of [[eq:iii-g3-2-2]] at λ (K(λ) in [[prop:iii-g3-3-7]] and in [[eq:iii-g3-3-6]]). Also
from

*18. [[ch:s27]], [[sec:iii-k-0]], *Parameters* (lines 89–93).* Old, the five lines:

*Parameters* ([Hin26, Section 13.1, Step 1]). The constraint damping E_C has the constants of [[thm:iii-e-1-1]] fixed
in [[eq:iv4-0-1]], with C_0 = 100: v_C = ½, e_C = 1/102400 and γ_C = h⁻¹, h ∈ 𝖧; as h < 10⁻⁶,
s_C := (1 − e_C)(1 − v_C)γ_C > 100. The gauge modification E_Υ = (c_Υ, e_Υ, γ_Υ; c_(Υ,H), γ_(Υ,H)) has c_Υ and c_(Υ,H)
as in [[sec:iii-d-1]] and [[lem:iii-d1-3-1]], and γ_(Υ,H), e_Υ, γ_Υ small enough for the mode stability of
[[prop:iii-d1-4-1]] and the tf-admissibility of [[prop:iii-f1-3-3]]. The data index set ℰ_0 and the weight ℓ_0 satisfy

New, the eight lines:

*Parameters* ([Hin26, Section 13.1, Step 1]). The constraint damping E_C has v_C = ½, e_C = 1/102400 and C_0 = 100
([[eq:iv4-0-1]]), and γ_C = h⁻¹. The gauge modification E_Υ = (c_Υ, e_Υ, γ_Υ; c_(Υ,H), γ_(Υ,H)) has c_Υ and c_(Υ,H)
as in [[sec:iii-d-1]] and [[lem:iii-d1-3-1]]. The point (h, γ_(Υ,H), e_Υ, γ_Υ) is admissible ([[def:vi-c-admissible]]):
h ≤ 10⁻⁶, so that s_C := (1 − e_C)(1 − v_C)γ_C > 100, 0 < e_Υ < 1 and 0 < γ_Υ < ¼; □^C_b has the properties (1)–(2)
of [[thm:iii-e-1-1]], (C4′) of [[sec:iii-f1-1]] and tf-admissibility with the weights in (1, 2); □^Υ_b has the mode
stability of [[prop:iii-d1-4-1]]; and Λ_tf(γ_Υ, e_Υ) < 1, so that L_b has the tf-admissibility of
[[prop:iii-f1-3-3]]. Such points exist: h ∈ 𝖧 ([[eq:iv4-0-1]]) with γ_(Υ,H) ∈ (0, ε_0], e_Υ ∈ (0, min(ε_1, ½)] and
γ_Υ ∈ (0, min(ε_1, ¼)) ([[prop:vi-c-adm-exist]]). The data index set ℰ_0 and the weight ℓ_0 satisfy

*19. [[ch:s27]], [[sec:vi-c-1]], the opening paragraph (lines 1703–1709).* Old, the seven lines:

made. m₀ > 0 is fixed and R₁ := m₀^(1/2). Conditions that only restate a choice made in another row are omitted. The
constants v_C, e_C, C_0 and γ_C of the damping are fixed once, in [[eq:iv4-0-1]], at the point where [[thm:iii-e-1-1]]
is proved, and no result varies them; every result that names them uses that point. The class parameter of
[[sec:iii-i-1]], the e3b-weight at ℐ⁺ of the admissible operators, is a number in (0, ½) fixed once and for all; it
carries no threshold and depends on no other choice. [[ch:s19]] writes it ℓ_I as well; in the rows below, ℓ_I is the
b-weight at ℐ⁺ of the data class of [[thm:iii-c1-3-1]].


New, the six lines:

made. m₀ > 0 is fixed and R₁ := m₀^(1/2). Conditions that only restate a choice made in another row are omitted. The
constants v_C, e_C and C_0 of the damping are fixed once, in [[eq:iv4-0-1]] (row c1), and γ_C = h⁻¹ is fixed with the
gauge parameters at an admissible point (row a1); no result varies them, and every result that names them uses that
point. The class parameter of [[sec:iii-i-1]], the e3b-weight at ℐ⁺ of the admissible operators, is a number in
(0, ½) fixed once and for all; it carries no threshold and depends on no other choice. [[ch:s19]] writes it ℓ_I as
well; in the rows below, ℓ_I is the b-weight at ℐ⁺ of the data class of [[thm:iii-c1-3-1]].

*20. [[ch:s27]], [[sec:vi-c-1]], rows c1–c4 (lines 1710–1721).* Old, the twelve lines:

**c1.** (v_C, e_C, C_0) = (½, 1/102400, 100), the point at which [[thm:iii-e-1-1]] is proved ([[eq:iv4-0-1]],
[[sec:iii-k-0]]). Threshold: none.

**c2.** γ_C = h⁻¹, h ∈ 𝖧 = (0, h_*) ∖ 𝖹, h_* = min(10⁻⁶, h_0, h_tf), 𝖹 countable ([[eq:iv4-0-1]], [[lem:iv4-1-3]] (b),
[[prop:np-10-52]] (ii)–(iii)). Threshold: c1.

**c3.** γ_C: (C1)–(C4), the clauses of [[thm:iii-e-1-1]] (3) after its first sentence: the indicial roots of □^C_b are
simple, avoid the listed sets, and are real where their real part is an integer in [3, 51] (used in [[ch:s15]]).
Threshold: c1, c2.

**c4.** γ_C: (C5) γ_C v_C ≥ ½ ([[sec:iii-i10-1]], [[sec:iii-g2-1]]), and s_C := (1 − e_C)(1 − v_C)γ_C > 100
([[sec:iii-f-1]], [[sec:iii-k-0]]). Both hold as γ_C > 10⁶. Threshold: c1.

New: Block A1 of Part A, then a blank line, then the two lines of row c1 as they stand:

**c1.** (v_C, e_C, C_0) = (½, 1/102400, 100), the point at which [[thm:iii-e-1-1]] is proved ([[eq:iv4-0-1]],
[[sec:iii-k-0]]). Threshold: none.

*21. [[ch:s27]], [[sec:vi-c-1]], rows u2–u5 (combined text: P-T78 text 6 and this file) (lines 1727–1737).* Old, the
eleven lines:

**u2.** γ_(Υ,H) ∈ (0, ε_0], ε_0 that of [[prop:iii-d1-4-1]]. Threshold: none.

**u3.** e_Υ ∈ (0, min(ε_1, ε_L)), with ε_1 of [[prop:iii-d1-4-1]] and ε_L of [[lem:iii-d-7-1]]
([[prop:iii-f1-3-3]]). Threshold: ε_1 on u2; ε_L on c1–c2.

**u4.** 0 < γ_Υ < min(ε_1, ε_L, γ_1, 3/8, ½s_C, ¼), with γ_1 of [[prop:iii-f1-3-3]]; ε_L contains the bound
C′|γ_Υ| ≤ ½ of the proof of [[lem:iii-d-7-1]] ([[prop:iii-d1-4-1]], [[sec:iii-g2-1]], [[eq:iii-c-1-1]],
[[eq:iii-i9-1-1]]). Threshold: γ_1 on c1–c3 and u2–u3; ε_L on c1–c2.

**u5.** z_Υ := 4e_Υγ_Υ² ∈ (0, ½] ∖ 𝖹_exc, 𝖹_exc countable ([[prop:iii-f1-2-3]] (e), [[sec:iii-g2-1]]). Threshold:
𝖹_exc on c1–c3; u3.

New: Block A2 of Part A.

*22. [[ch:s27]], [[sec:vi-c-1]], row b2 (lines 1741–1744).* Old, the four lines:

**b2.** b ∈ ℬ(γ_(Υ,H)) ([[prop:iii-d1-4-1]]); with the low-frequency radius c_0 of [[cor:iii-h-4-3]], written c_σ in this
section and the next to distinguish it from the constant c_0 of [[sec:iii-k-3]], b ∈ ℬ(c_σ) ([[prop:iii-f2-4-1]]) and in
the neighbourhood of [[cor:iii-h-4-3]]–[[cor:iii-h-4-4]]; and b near b₀ as [[thm:iii-e-1-1]], [[prop:iii-f1-3-3]] and
[[sec:iii-j-1]] ask. Threshold: c1–c2, u1–u5.

New, the four lines:

**b2.** b ∈ ℬ(γ_(Υ,H)), the neighbourhood of (P3) of [[def:vi-c-admissible]]; with the low-frequency radius c_0 of
[[cor:iii-h-4-3]], written c_σ in this section and the next to distinguish it from the constant c_0 of [[sec:iii-k-3]],
b ∈ ℬ(c_σ) ([[prop:iii-f2-4-1]]) and in the neighbourhood of [[cor:iii-h-4-3]]–[[cor:iii-h-4-4]]; and b near b₀ as
(P1), (P4) and [[sec:iii-j-1]] ask. Threshold: c1, u1, a1.

*23. [[ch:s27]], [[sec:vi-c-1]], the threshold of row b3 (line 1747).* Old, the line:

condition on ℬ_* there; b4 shrinks it further. Threshold: b2, u1–u5.

New, the line:

condition on ℬ_* there; b4 shrinks it further. Threshold: b2, u1, a1.

*24. [[ch:s27]], [[sec:vi-c-1]], the threshold of row w1 (line 1763).* Old, the line:

Threshold: u1–u5, d1–d2.

New, the line:

Threshold: u1, a1, d1–d2.

*25. [[ch:s27]], [[sec:vi-c-1]], the threshold of row d1 (line 1770).* Old, the line:

([[thm:iii-c1-3-1]], [[sec:iii-k-0]], (H4) of [[sec:iii-i10-1]]). Threshold: u4.

New, the line:

([[thm:iii-c1-3-1]], [[sec:iii-k-0]], (H4) of [[sec:iii-i10-1]]). Threshold: a1.

*26. [[ch:s27]], [[sec:vi-c-1]], the threshold of row d2 (line 1776).* Old, the line:

[[prop:iii-i1-3-1]], [[sec:iii-i10-1]]). Threshold: c1–c2, u3–u4, d1.

New, the line:

[[prop:iii-i1-3-1]], [[sec:iii-i10-1]]). Threshold: c1, a1, d1.

*27. [[ch:s27]], [[thm:vi-c-2-1]], steps (1)–(2) (combined text: P-T78 text 7 and this file) (lines 1787–1797).* Old,
the eleven lines:

(1) (v_C, e_C, C_0) := (½, 1/102400, 100) and h ∈ 𝖧, γ_C := h⁻¹. Then [[thm:iii-e-1-1]] holds at these values
([[thm:iv4-2-1]] for (1)–(3), [[thm:iv6-4-1]] for (4)), with (C1)–(C4) (row c3), and (C5) and s_C > 100 hold, as
γ_C > 10⁶.

(2) The gauge. ε_0 of [[prop:iii-d1-4-1]] is uniform. Choose γ_(Υ,H) ∈ (0, ε_0]; this fixes ε_1 and ℬ(γ_(Υ,H)).
Choose e_Υ ∈ (0, min(ε_1, ε_L)); this fixes γ_1 of [[prop:iii-f1-3-3]], which fixes all parameters but γ_Υ and
depends on the orders, hence on γ_C. 𝖹_exc is fixed by step (1). Choose γ_Υ in the interval of row u4 with
4e_Υγ_Υ² ∉ 𝖹_exc. This is possible because the interval is nonempty and open, while {γ > 0 : 4e_Υγ² ∈ 𝖹_exc} is
countable. Then z_Υ ∈ (0, ½], as γ_Υ < ¼ and e_Υ < 1. [[prop:iii-d-6-3]] (the invertibility of the spectral family
of □^Υ_b at |σ| ≥ c_σ) is then implied, for every c_σ and b ∈ ℬ(γ_(Υ,H)), by [[prop:iii-d1-4-1]], which gives it for
every σ with Im σ ≥ 0; so it imposes no further condition.

New: Block A3 of Part A.

*28. [[ch:s27]], the proof of [[thm:vi-c-2-1]] (lines 1821–1824).* Old, the four lines:

row of [[sec:vi-c-1]] records that no threshold depends on a later choice. In step (2), the ε_0 of [[prop:iii-d1-4-1]]
is uniform, while its ε_1 and ℬ(γ_(Υ,H)) come after γ_(Υ,H), so the order γ_(Υ,H), e_Υ, γ_Υ meets it. The only
low-frequency radius that depends on the gauge is the c_σ of [[cor:iii-h-4-3]], and it is used only after the gauge is
fixed, through [[prop:iii-f2-4-1]], whose neighbourhood is then chosen. In step (5), each neighbourhood of rows b2 and

New, the five lines:

row of [[sec:vi-c-1]] records that no threshold depends on a later choice. In steps (1)–(2) every condition is a
property of the point (h, γ_(Υ,H), e_Υ, γ_Υ) alone (row a1), every number of step (2) is fixed by it, and the results
that the later steps use hold at it ([[thm:vi-c-adm-holds]] (1)). The only low-frequency radius that depends on the
gauge is the c_σ of [[cor:iii-h-4-3]], and it is used only after the gauge is fixed, through [[prop:iii-f2-4-1]],
whose neighbourhood is then chosen. In step (5), each neighbourhood of rows b2 and

*29. [[ch:s27]], [[sec:vi-c-2]], after the paragraph that follows the proof of [[thm:vi-c-2-1]] (line 1830).* Old, the
line:

σ ∈ Σ_0, |σ| ≤ c_σ, by [[cor:iii-h-4-3]]; its neighbourhood is one of row b2, so it holds on ℬ̄_*.

New: the line as it stands, then a blank line, then Block A4 of Part A:

σ ∈ Σ_0, |σ| ≤ c_σ, by [[cor:iii-h-4-3]]; its neighbourhood is one of row b2, so it holds on ℬ̄_*.

*30. [[ch:explicit-constants]], the opening paragraph (lines 26–28).* Old, the three lines:

most an integer below 1.57157 × 10⁵⁰, and N_NM at most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter
point lies outside the set on which [[thm:settling]] is proved ([[rem:ec-point-outside]]), and the bounds at it bound
what this proof's choices produce, not the optimal loss. The

New, the three lines:

most an integer below 1.57157 × 10⁵⁰, and N_NM at most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter
point is not shown to lie in the set on which [[thm:settling]] is proved ([[rem:ec-point-outside]]), and the bounds at
it bound what this proof's choices produce, not the optimal loss. The

*31. [[ch:explicit-constants]], [[rem:ec-point-outside]] (combined text: P-LB as merged, P-T78 text 8, P-T49 text 7 and
this file) (lines 52–68).* Old, the seventeen lines:

**Remark {#rem:ec-point-outside}** (The computational point and the proved set.) The computational point lies outside
the set on which [[thm:settling]] is proved, and it lies outside through h. [[thm:settling]] takes h in the set 𝖧 of
[[eq:iv4-0-1]], whose supremum h_* = min(10⁻⁶, h_0, h_tf) is at most 10⁻⁶ whatever the values of h_0 and h_tf, and
𝖧 ⊂ (0, h_*); so h = 10⁻⁶ is not in 𝖧 ([[rem:s14-eps-ind-scope]]). Whether the gauge half of the point lies in the
proved set is not decided: the parameters γ_Υ and e_Υ are required in [[thm:vi-c-2-1]] to lie below thresholds whose
existence is proved and whose values are not determined, and (γ_Υ, e_Υ) = (1/100, 1/100) is not shown to lie below them.
[[def:ec-point]] does not fix the parameter γ_(Υ,H) of the horizon modification (row u2 of
[[sec:vi-c-1]]), on which the threshold ε_1 of [[prop:iii-d1-4-1]] for γ_Υ and e_Υ depends, and no number of this
chapter depends on it: the horizon thresholds that enter do not involve it ([[lem:iii-d-5-1]], and [[lem:iii-f2-1-1]],
where y = 0 for the 1-form c_(Υ,H) = −½χ dr), and the indicial roots of (□^Υ_b)^(0), which fix ℳ and ε_Υ, do not
depend on the horizon modification ([[sec:iii-d2-1]]). So the computational point is a point at which the formulas of
the proof can be evaluated, not one at which the hypotheses of [[thm:settling]] are shown to hold. Every number of this
chapter that depends on the point is stated at it. For h ∈ 𝖧 the theorems use only 0 < ε_ind(h) ≤ δ_50
([[prop:np-10-52]] (iii)), and the lower bound of [[thm:loss-d]] uses besides only ε_Υ < 1.46214·10⁻¹⁰, which holds at
every h, ε_Υ being fixed by (γ_Υ, e_Υ) ([[lem:ec-gauge-gap]], [[prop:ec-rounds]]). At every point of the proved set a
lower bound for d holds as an explicit function of z = 4e_Υγ_Υ² and h, with no threshold evaluated, through bounds for
ε_Υ and ε_ind(h) that hold at every such point ([[lem:ec-lb-gauge]], [[lem:ec-lb-ind]], [[thm:ec-lb-proved]]).

New: Part C.

*32. [[ch:explicit-constants]], [[rem:ec-not-evaluated]] (combined text: P-LB as merged, P-T78 text 9 and this file)
(lines 4961–4968).* Old, the eight lines:

positive by the proof of [[thm:settling]]. Explicit values stop first upstream of every constant: the proof fixes the
gauge and damping parameters only below thresholds whose existence it proves ([[thm:vi-c-2-1]]), and the cut-offs and
orders of its function spaces only up to admissibility, so explicit constants need those choices made with numbers, which
this chapter does only at a point outside the proved set: [[def:ec-point]] for the gauge and damping parameters, and
[[def:uc-choice]] and [[def:cs-choices]] for the weights, orders and inner products on which d depends. The lower bound
for d of [[thm:ec-lb-proved]] needs no such choice: it holds at every point of the proved set as an explicit function
of the gauge and damping parameters, and it tends to infinity as z tends to 0 or γ_C to infinity, so that no upper
bound for d holds on all of that set ([[rem:ec-lb-unbounded]]). Among the inputs

New, the ten lines:

positive by the proof of [[thm:settling]]. Explicit values stop first upstream of every constant: the proof fixes the
gauge and damping parameters only at admissible points ([[def:vi-c-admissible]]), which it exhibits only below thresholds
whose existence it proves ([[prop:vi-c-adm-exist]]; the conditions of tf-admissibility on the gauge are explicit,
[[prop:tf-gauge-explicit]]), and the cut-offs and orders of its function spaces only up to admissibility, so explicit
constants need those choices made with numbers, which this chapter does only at a point not shown to lie in the proved
set: [[def:ec-point]] for the gauge and damping parameters, and [[def:uc-choice]] and [[def:cs-choices]] for the
weights, orders and inner products on which d depends. The lower bound for d of [[thm:ec-lb-proved]] needs no such
choice: it holds at every point of the proved set as an explicit function of the gauge and damping parameters, and it
tends to infinity as z tends to 0 or γ_C to infinity, so that no upper bound for d holds on all of that set
([[rem:ec-lb-unbounded]]). Among the inputs

*33. [[ch:explicit-constants]], [[sec:ec-lb-proved]], the opening paragraph (lines 1546–1547).* Old, the two lines:

The lower bound of [[thm:loss-d]] (ii) is stated at the computational point, and that point lies outside the set on
which [[thm:settling]] is proved ([[rem:ec-point-outside]]). This section proves a lower bound for d_acc, and so for

New, the two lines:

The lower bound of [[thm:loss-d]] (ii) is stated at the computational point, which is not shown to lie in the set on
which [[thm:settling]] is proved ([[rem:ec-point-outside]]). This section proves a lower bound for d_acc, and so for

*34. [[ch:explicit-constants]], [[thm:ec-lb-proved]], the first sentence (lines 1707–1709).* Old, the three lines:

**Theorem {#thm:ec-lb-proved}** (The loss at every point of the proved set.) Let h ∈ 𝖧, γ_C = h⁻¹, the gauge
parameters (γ_(Υ,H), e_Υ, γ_Υ), the constants ε_Υ and ε_ind, and the weights be chosen as in [[thm:settling]], that is,
so that the conditions of [[sec:vi-c-1]] hold ([[thm:vi-c-2-1]]). Put z := 4e_Υγ_Υ², let g be the function of

New, the four lines:

**Theorem {#thm:ec-lb-proved}** (The loss at every point of the proved set.) Let the admissible point
(h, γ_(Υ,H), e_Υ, γ_Υ) of row a1 of [[sec:vi-c-1]], with γ_C = h⁻¹, the constants ε_Υ and ε_ind, and the weights be
chosen as in [[thm:settling]], that is, so that the conditions of [[sec:vi-c-1]] hold ([[thm:vi-c-2-1]]). Put
z := 4e_Υγ_Υ², let g be the function of

*35. [[ch:explicit-constants]], the proof of [[thm:ec-lb-proved]], *The gaps* (lines 1727–1730).* Old, the four lines:

*Proof.* *The gaps.* By rows c1–c2 of [[sec:vi-c-1]], (v_C, e_C) = (1/2, 1/102400) and h ∈ 𝖧 ⊂ (0, h_*) with
h_* ≤ 10⁻⁶; by row u5, z ∈ (0, ½]. [[sec:iii-d2-1]] fixes ε_Υ below half the least distance between distinct points of
ℳ, so ε_Υ < g(z) by [[lem:ec-lb-gauge]]. By row c3, (C1) holds (it holds at every h ∈ (0, 10⁻⁶], by [[lem:iv4-1-3]]
(a)), and ε_ind is a constant with [[eq:iii-f1-2-2]] ([[eq:iii-i9-1-1]]); so ε_ind < 40h/13 by [[lem:ec-lb-ind]].

New, the four lines:

*Proof.* *The gaps.* By row c1 of [[sec:vi-c-1]] and (P0) of [[def:vi-c-admissible]], (v_C, e_C) = (1/2, 1/102400),
h ≤ 10⁻⁶ and z ∈ (0, ¼) ⊂ (0, ½]. [[sec:iii-d2-1]] fixes ε_Υ below half the least distance between distinct points of
ℳ, so ε_Υ < g(z) by [[lem:ec-lb-gauge]]. (C1) holds, as h ≤ 10⁻⁶ ([[lem:iv4-1-3]] (a)), and ε_ind is a constant with
[[eq:iii-f1-2-2]] ([[eq:iii-i9-1-1]]); so ε_ind < 40h/13 by [[lem:ec-lb-ind]].

*36. [[ch:explicit-constants]], [[rem:ec-lb-conditions]], the bullets on the parameter point (lines 1769–1773).* Old, the
five lines:

- h ≤ 10⁻⁶ (row c2: 𝖧 ⊂ (0, h_*) with h_* ≤ 10⁻⁶), for [[lem:ec-lb-ind]] and for 6Θ_η < 2·10⁻⁵;
- (C1) (row c3), which holds at every h ∈ (0, 10⁻⁶] ([[lem:iv4-1-3]] (a)), to read ι₂(h) − 1 as an indicial root of
  L_b^(0);
- (C4) (row c3), only through the existence of the constant ε_ind ([[prop:iii-f1-2-3]] (f));
- z ∈ (0, ½] (row u5), for [[lem:ec-lb-gauge]];

New, the five lines:

- h ≤ 10⁻⁶ ((P0) of [[def:vi-c-admissible]]), for [[lem:ec-lb-ind]] and for 6Θ_η < 2·10⁻⁵;
- (C1), which holds at every h ∈ (0, 10⁻⁶] ([[lem:iv4-1-3]] (a)), to read ι₂(h) − 1 as an indicial root of
  L_b^(0);
- (C4′) of [[sec:iii-f1-1]] ((P2)), only through the existence of the constant ε_ind ([[prop:iii-f1-2-3]] (f));
- z ∈ (0, ½], which (P0) gives, for [[lem:ec-lb-gauge]];

*37. [[ch:explicit-constants]], [[rem:ec-lb-conditions]], the paragraph after the bullets (lines 1779–1783).* Old, the
five lines:

It uses none of the thresholds that define the proved set: not h < h_0, h < h_tf or h ∉ 𝖹; not γ_(Υ,H) ≤ ε_0, nor the
bounds ε_1, ε_L and γ_1 on e_Υ and γ_Υ; not z ∉ 𝖹_exc; not (C2), (C3) or (C5), nor (C4) beyond the existence of ε_ind;
not (G) beyond ε_K < ε_Υ, nor (G⁺), (Ex1)–(Ex4) or (A_J); and not the data classes (rows d1–d2), the parameter set ℬ_*
(rows b1–b4) or the smallness of row n1. So the bound holds on the proved set without any of those thresholds being
evaluated. It holds as well at every (h, z) ∈ (0, 10⁻⁶] × (0, ½] at which the constructions of [[sec:ec-floor]] are run

New, the six lines:

It uses no other condition of an admissible point: not (P1), (P3) or (P4); not h < h_0, h < h_tf, h ∉ 𝖹,
γ_(Υ,H) ≤ ε_0, e_Υ < ε_1, γ_Υ < ε_1 or z ∉ 𝖹_exc, by which [[prop:vi-c-adm-exist]] exhibits such points; not (C2),
(C3) or (C5), nor (C4) beyond (C4′); not (G) beyond ε_K < ε_Υ, nor (G⁺), (Ex1)–(Ex4) or (A_J); and not the data
classes (rows d1–d2), the parameter set ℬ_* (rows b1–b4) or the smallness of row n1. So the bound holds on the proved
set without any threshold being evaluated. It holds as well at every (h, z) ∈ (0, 10⁻⁶] × (0, ½] at which the
constructions of [[sec:ec-floor]] are run

*38. [[ch:explicit-constants]], [[rem:ec-lb-unbounded]] (lines 1787–1795).* Old, the nine lines:

**Remark {#rem:ec-lb-unbounded}** (No upper bound holds on all of the proved set.) The set 𝖧 = (0, h_*) ∖ 𝖹, with 𝖹
countable, contains numbers h arbitrarily close to 0, and at each of them [[thm:vi-c-2-1]] completes the choice of the
parameters; there [[thm:ec-lb-proved]] gives d_NM > 0.3168γ_C² = 0.3168h⁻². So d_NM is unbounded on the proved set, and
an explicit upper bound for it can hold at points of that set but not on all of it; in particular d_NM exceeds
1.57157·10⁵⁰, the bound of [[thm:uc-integer]], at every point of the proved set with h ≤ 4.48·10⁻²⁶. Likewise, at a
fixed h the conditions on (e_Υ, γ_Υ) are upper bounds together with z ∉ 𝖹_exc, 𝖹_exc countable, so z takes values
arbitrarily close to 0, where the first bound of [[eq:ec-lb-numbers]] grows like z⁻². If (γ_Υ, e_Υ) = (1/100, 1/100)
is admissible at some h ∈ 𝖧, the theorem gives d_NM > 1.4032·10²⁰ there, as at the computational point, and the larger
bound d_NM > 0.3168γ_C² when h < 4.75·10⁻¹¹. The bound 1.2497·10²⁴ of [[cor:uc-two-offsets]] rests on the gap

New, the ten lines:

**Remark {#rem:ec-lb-unbounded}** (No upper bound holds on all of the proved set.) Admissible points exist with h
arbitrarily close to 0 ([[prop:vi-c-adm-exist]]), and at each of them [[thm:vi-c-2-1]] completes the choice of the
parameters; there [[thm:ec-lb-proved]] gives d_NM > 0.3168γ_C² = 0.3168h⁻². So d_NM is unbounded on the proved set, and
an explicit upper bound for it can hold at points of that set but not on all of it; in particular d_NM exceeds
1.57157·10⁵⁰, the bound of [[thm:uc-integer]], at every point of the proved set with h ≤ 4.48·10⁻²⁶. Likewise, at a
fixed h ∈ 𝖧 the points of [[prop:vi-c-adm-exist]] have e_Υ and γ_Υ arbitrarily small, so z takes values arbitrarily
close to 0, where the first bound of [[eq:ec-lb-numbers]] grows like z⁻². If (h, γ_(Υ,H), 1/100, 1/100) is an
admissible point for some h and γ_(Υ,H), the theorem gives d_NM > 1.4032·10²⁰ there, as at the computational point,
and the larger bound d_NM > 0.3168γ_C² when h < 4.75·10⁻¹¹. The bound 1.2497·10²⁴ of [[cor:uc-two-offsets]] rests on
the gap

*39. [[ch:resolvent-bounds]], [[sec:rb-scalar-blocks]], the paragraph that fixes the parameters (lines 1695–1696).* Old,
the two lines:

those parameters. This point lies outside the set on which the theorems are proved: γ_C = 10⁶ is not of the form h⁻¹
with h as in [[eq:iv4-0-1]], where h < 10⁻⁶, and (γ_Υ, e_Υ) = (1/100, 1/100) are not shown to lie below the thresholds

New, the three lines:

those parameters. This point is not shown to lie in the set on which [[thm:settling]] is proved
([[rem:ec-point-outside]]): γ_C = 10⁶ is not of the form h⁻¹ with h as in [[eq:iv4-0-1]], where h < 10⁻⁶, so
[[thm:iii-e-1-1]] is not proved there, and (γ_Υ, e_Υ) = (1/100, 1/100) are not shown to lie below the thresholds

*40. The front matter, the abstract (lines 35–38).* Old, the four lines:

that set, and, at a parameter point outside it, for one admissible choice of the weights, orders and inner products and
the index sets as the proofs construct them, 1.2497 × 10²⁴ < d < 1.57157 × 10⁵⁰; at equality, μ0 = √72 l5², timelike
curves of g_λ cross the boundary in a layer whose width tends to zero with λ; and at the physical wavelength 10 l5
there is no separation of scales, existence holding where the solution is the seed.

New, the four lines:

that set, and, at a parameter point not shown to lie in it, for one admissible choice of the weights, orders and inner
products and the index sets as the proofs construct them, 1.2497 × 10²⁴ < d < 1.57157 × 10⁵⁰; at equality,
μ0 = √72 l5², timelike curves of g_λ cross the boundary in a layer whose width tends to zero with λ; and at the
physical wavelength 10 l5 there is no separation of scales, existence holding where the solution is the seed.

*41. [[ch:introduction]], [[sec:introduction-scope]] (lines 154–156).* Old, the three lines:

([[thm:ec-lb-proved]]), so that d is unbounded on that set. At a point of the gauge and damping parameters outside it,
d > 1.2497 × 10²⁴ at every admissible choice of the weights, for the index sets as the proofs construct them, and
d < 1.57157 × 10⁵⁰ at one admissible choice of the weights, orders and inner products ([[thm:uc-integer]]). A

New, the four lines:

([[thm:ec-lb-proved]]), so that d is unbounded on that set. At a point of the gauge and damping parameters not shown
to lie in it, d > 1.2497 × 10²⁴ at every admissible choice of the weights, for the index sets as the proofs construct
them, and d < 1.57157 × 10⁵⁰ at one admissible choice of the weights, orders and inner products ([[thm:uc-integer]]).
A

*42. [[ch:theorems]], [[sec:further-results]], the item on the constants (lines 354–358).* Old, the five lines:

  and γ_C² ([[thm:ec-lb-proved]]); at a parameter point that lies outside the proved set, explicit lower bounds
  ([[thm:loss-d]]) and explicit upper bounds for d and N_NM at one admissible choice of the weights, orders and inner
  products ([[thm:uc-integer]]); through the lower bounds, upper bounds for δ and for the modulus of the initial family
  at 2δ (and λ1 < δ); explicit resolvent bounds on five-dimensional Tangherlini ([[ch:resolvent-bounds]]); and where
  explicit evaluation of λ1 and δ stops ([[ch:explicit-constants]]).

New, the five lines:

  and γ_C² ([[thm:ec-lb-proved]]); at a parameter point that is not shown to lie in the proved set, explicit lower bounds
  ([[thm:loss-d]]) and explicit upper bounds for d and N_NM at one admissible choice of the weights, orders and inner
  products ([[thm:uc-integer]]); through the lower bounds, upper bounds for δ and for the modulus of the initial family
  at 2δ (and λ1 < δ); explicit resolvent bounds on five-dimensional Tangherlini ([[ch:resolvent-bounds]]); and where
  explicit evaluation of λ1 and δ stops ([[ch:explicit-constants]]).

*43. [[ch:scope]], [[sec:scope-constants]] (lines 77–79).* Old, the three lines:

computational point is a point at which the formulas of the proof can be evaluated, and it lies outside the set on which
[[thm:settling]] is proved ([[rem:ec-point-outside]]). No result of [[ch:explicit-constants]] is used in the proof of any
theorem outside that chapter; the explicit indices of [[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]], which

New, the three lines:

computational point is a point at which the formulas of the proof can be evaluated, and it is not shown to lie in the
set on which [[thm:settling]] is proved ([[rem:ec-point-outside]]). No result of [[ch:explicit-constants]] is used in
the proof of any theorem outside that chapter; the explicit indices of [[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]], which

*44. [[ch:scope]], [[sec:scope-constants]], the paragraph on explicit values (combined text: P-T78 text 10 and this file)
(lines 83–85).* Old, the three lines:

Explicit values stop upstream of every constant of [[thm:settling]]: the proof fixes the gauge and damping parameters
only below thresholds whose existence it proves, and the cut-offs and orders of its function spaces only up to
admissibility; arguments by contradiction, compactness and defect measures give constants without a value; and the

New, the five lines:

Explicit values stop upstream of every constant of [[thm:settling]]: the proof fixes the gauge and damping parameters
only at admissible points, which it exhibits only below thresholds whose existence it proves (the conditions of
tf-admissibility on the gauge are explicit: e_Υ ≤ ½ and γ_Υ ≤ ¼ suffice, [[prop:tf-gauge-explicit]]), and the cut-offs
and orders of its function spaces only up to admissibility; arguments by contradiction, compactness and defect measures
give constants without a value; and the

*45. Unchanged.* Every other statement of [[ch:s13]], [[ch:s15]]–[[ch:s29]] and [[ch:settling-proof]] keeps its text: the
standing phrases "small", "as [[prop:iii-d1-4-1]] allows" and "the parameters of [[prop:iii-f1-3-3]]" in
[[sec:iii-f1-1]], [[sec:iii-d2-1]], [[lem:iii-d1-5-1]], [[prop:iii-f2-3-1]], [[sec:iii-f3-1]], the opening of [[ch:s16]],
[[thm:iii-g-5-1]], [[sec:iii-g2-1]] and [[sec:iii-h-1]] describe the setting in which the existence results are proved,
and [[thm:vi-c-adm-holds]] (1) extends every result to admissible points; the sentence added to [[sec:iii-f-1]] (item 1)
says so where the chapters read the parameters. [[thm:settling]] and [[thm:settling-precise]] keep their texts: they
refer to steps (3)–(6) of [[thm:vi-c-2-1]], whose numbering is kept, and to δ_♯, ε_ind, (G⁺) and (G), which step (2)
still fixes. Row c1, row u1 and rows b1, b4, w2 and n1 keep their texts. [[prop:iii-f1-2-3]] (e) and the clauses
(C2)–(C3) stay, unused by the proof of [[thm:settling]]. Chapter 33 is not edited by this file; the interactions give
the three sentences there that should follow.

### Crosswalk rows

New rows for the crosswalk of [[ch:s27]], in its four columns separated by tabs, in chapter order: the first two directly
after the row of sec:vi-c-1, the third directly after the row of thm:vi-c-2-1. The line numbers are those of this file,
at the line that carries the label.

CROSSWALK-PLACEHOLDER

Notes to add to existing rows. [[ch:s27]]: sec:iii-k-0, "parameters: an admissible point (P-ADM item 18)"; sec:vi-c-1,
"rows c2–c4 and u2–u5 replaced by def:vi-c-admissible, prop:vi-c-adm-exist and row a1; thresholds of b2, b3, w1, d1, d2
re-keyed (P-ADM items 19–26)"; thm:vi-c-2-1, "steps (1)–(2): an admissible point and the numbers it fixes; proof sentence
on steps (1)–(2); thm:vi-c-adm-holds after it (P-ADM items 27–29)". [[ch:s15]]: sec:iii-f-1, "results hold at admissible
points (P-ADM item 1)"; sec:iii-f1-1, "(C4′) added (P-ADM item 2)"; prop:iii-f1-2-3, "(f) under (C4′); (g) simplicity on
[−101, 0] for every z ∈ (0, ½] (P-ADM items 3–5)". [[ch:s16]]: sec:iii-g2-1, "simplicity from prop:iii-f1-2-3 (g); (C5)
at admissible points (P-ADM items 6–7)"; lem:iii-g2-1-2 and thm:iii-g2-3-1, "simplicity from (g) (P-ADM items 8–9)".
[[ch:s17]]: sec:iii-g4-1, lem:iii-g4-1-1, lem:iii-g4-3-4 and thm:iii-g4-3-1, "simplicity only on [−101, 0], from (g)
(P-ADM items 10–14)". [[ch:s22]]: sec:iii-i10-1, "s_C > 100 cited to sec:iii-f-1, not to (C1) (P-ADM item 15)";
lem:iii-i12-2-3, "simplicity from (g) (P-ADM item 16)". [[ch:s23]]: the row of the section that opens with the setting
(P-ADM item 17), "s_C > 100 cited to sec:iii-f-1". [[ch:explicit-constants]]: ch:explicit-constants,
rem:ec-point-outside, rem:ec-not-evaluated, sec:ec-lb-proved, thm:ec-lb-proved, rem:ec-lb-conditions and
rem:ec-lb-unbounded, "admissible points; the computational point not shown to lie in the proved set (P-ADM items 30–38)".
[[ch:resolvent-bounds]]: sec:rb-scalar-blocks, "point not shown to lie in the proved set (P-ADM item 39)".
[[ch:introduction]]: sec:introduction-scope (item 41). [[ch:theorems]]: sec:further-results (item 42). [[ch:scope]]:
sec:scope-constants (items 43–44).

### Interactions with other proof files

*Merge order.* P-LB is merged (commit a722cb42); the old texts of items 30–38 and 40–42 are its merged texts. The proof
files P-T78 and P-T49 must be merged before this file, or together with it: Parts A–C cite eq:tf-lambda,
eq:tf-lambda-point, prop:tf-gauge-explicit and lem:tf-lin-reduction (P-T78, its items 1 and 4), the parts (a) and (b) of
lem:iii-d-7-1 (P-T78, item 2), the explicit statement of prop:iii-f1-3-3 (P-T78, item 5) and thm:t49-point (P-T49, item
1). Where two files change the same place, apply the combined item of this file and not the other file's item, as listed
below. The merged tree was checked on a scratch copy built in this order: the current chapters (P-LB merged), then P-T78
items 1, 2, 4 and 5, then P-T49 items 1 and 2, then every item of this file. The check lint.py --chapters reports one
hit, the pending marker computational-1 in P-T49's rem:t49-count, which is not this file's, and assemble.py --check
reports 4647 labels and 0 problems.

*P-LB (merged).* No P-LB statement or number changes. Its section in [[ch:explicit-constants]] cited rows c1–c3 and u5
and assumed h ∈ 𝖧; items 33–38 re-key these to row c1, (P0), (P2) and [[prop:vi-c-adm-exist]], and restate
[[thm:ec-lb-proved]] at an admissible point. The bound holds at every admissible point because (P0) contains h ≤ 10⁻⁶:
the proof of [[thm:ec-lb-proved]] uses h ≤ 10⁻⁶ in [[lem:ec-lb-ind]] and in 6Θ_η < 2·10⁻⁵, and otherwise only (C1), (C4′)
and z ∈ (0, ½]. This is why the definition carries h ≤ 10⁻⁶ rather than its two consequences s_C > 100 and (C1), which
are all that [[thm:settling]] uses: with them in its place the set could be larger (by points with h ∈ (10⁻⁶, (1 −
e_C)/200) at which (C1) holds, none of which any result of the paper certifies), and [[thm:ec-lb-proved]] and the
sentences of items 40–43 would need the qualifier "with h ≤ 10⁻⁶". Items 30, 31, 32, 40, 41 and 42 change the words
"outside" in P-LB's merged texts to "not shown to lie in", since the definition no longer excludes the computational
point.

*P-T78.* Its items 1, 2, 4 and 5 do not overlap this file. Its items 6–10 do: apply this file's items in their place, as
follows. P-T78 item 6 (rows u3 and u4): item 21 of this file, which removes rows u2–u5 and puts row a1, whose (P4) is
P-T78's explicit criterion Λ_tf < 1 together with the tf-admissibility of □^C_b at the weights in (1, 2) that Step 4 of
the proof of prop:iii-f1-3-3 still uses. P-T78 item 7 (step (2) of [[thm:vi-c-2-1]]): item 27, the new steps (1)–(2).
P-T78 item 8 ([[rem:ec-point-outside]]): item 31, Part C, which states P-T78's result at the point (Λ_tf < 1.0111·10⁻⁴,
and the tf-admissibility of □^Υ_b by lem:iii-d-7-1 (a)). P-T78 item 9 ([[rem:ec-not-evaluated]]): item 32, which keeps
P-T78's parenthesis "the conditions of tf-admissibility on the gauge are explicit, [[prop:tf-gauge-explicit]]". P-T78
item 10 ([[sec:scope-constants]]): item 44, which keeps P-T78's parenthesis "e_Υ ≤ ½ and γ_Υ ≤ ¼ suffice". P-T78's item
11 list stays true, except that the paragraph of [[sec:iii-k-0]] it names is rewritten by item 18. P-T78's crosswalk
notes for sec:vi-c-1 (rows u3 and u4) and thm:vi-c-2-1 (step (2)) are replaced by this file's notes; its twelve new rows
stand. The definition uses P-T78's criterion in (P4) where it is enough, which is for the gauge half: the explicit
inequality Λ_tf < 1 replaces the thresholds ε_L and γ_1, and it holds whenever e_Υ ≤ ½. It is not enough alone, since
Step 4 of the proof of prop:iii-f1-3-3 still needs the tf-admissibility of □^C_b at the weights in (1, 2); so (P4) keeps
that as its second half.

*P-T49.* Its item 7 ([[rem:ec-point-outside]]) overlaps item 31 of this file: apply item 31, which contains its sentence
as "the point also avoids the countable exclusions of [[eq:iv4-0-1]] and [[prop:iii-f1-2-3]] (e), which the definition
does not ask: h = 10⁻⁶ ∉ 𝖹, and Z_exc is empty at h = 10⁻⁶ ([[thm:t49-point]])". If P-T49 is not merged, in Part C
replace

gives ([[prop:iii-f1-2-3]] (g)); at the point every root of real part in [−101, 5] is simple ([[prop:is-mult]]), and
the point also avoids the countable exclusions of [[eq:iv4-0-1]] and [[prop:iii-f1-2-3]] (e), which the definition
does not ask: h = 10⁻⁶ ∉ 𝖹, and Z_exc is empty at h = 10⁻⁶ ([[thm:t49-point]]). So the computational point is a point

by

gives ([[prop:iii-f1-2-3]] (g)); at the point every root of real part in [−101, 5] is simple ([[prop:is-mult]]).
So the computational point is a point

P-T49's items 2–6 and 8 do not overlap this file. Its item 5 changes the last line of the proof of [[prop:iii-f1-2-3]]
(e) ("type and degree; so each coincidence happens at at most one z, ..."), which items 3–5 of this file do not touch.
Its results do not let the definition drop or replace a further condition, because the definition already asks none of
(C2), (C3), z ∉ Z_exc and h ∉ 𝖹: thm:t49-uniform (𝖹₂ empty, (C3) at every h ≤ 10⁻⁶, Z_exc empty wherever (C2) holds)
bears only on the former rows c2 and u5, and thm:t49-point gives, at the point, (C1)–(C4) (so (P2) a second time) and the
simplicity of every indicial root, which Part C cites; cor:t49-right is not needed. Two of P-T49's chapter texts name
rows that this file removes, and should change after it. In the remark (d) of rem:t49-sets, replace

(d) Z_exc ([[prop:iii-f1-2-3]] (e)), written 𝖹_exc in row u5 of [[sec:vi-c-1]], is defined at an h at which (C2) and

by

(d) Z_exc ([[prop:iii-f1-2-3]] (e)) is defined at an h at which (C2) and

(the line then continues as it stands, "(C3) hold. It is the set ..."). In rem:t49-scope, replace the first four
sentences, from "**Remark {#rem:t49-scope}** (What this decides.) At the damping point, the parts of rows c2, c3 and u5"
through "and the order of choices in [[thm:vi-c-2-1]] meets no exclusion in z.", by:

**Remark {#rem:t49-scope}** (What this decides.) At the damping point the exclusions of [[eq:iv4-0-1]] and
[[prop:iii-f1-2-3]] (e) are met, although [[def:vi-c-admissible]] does not ask them: h = 10⁻⁶ ∉ 𝖹, (C1)–(C4) hold,
and Z_exc = ∅ at h = 10⁻⁶, so z = 4·10⁻⁶ ∉ Z_exc ([[thm:t49-point]]); every indicial root of L̂_b(0) at the
computational point is simple. The computational point is not in 𝖧, because h_* ≤ 10⁻⁶ and 𝖧 is open at h_*, and
whether it is admissible is decided by the conditions that [[rem:ec-point-outside]] lists as open. Away from the
point, 𝖹₂ and Z_exc are empty and (C3) holds at every h ∈ (0, 10⁻⁶] ([[thm:t49-uniform]]), so 𝖹 = 𝖹₁ ∪ 𝖹₃ and the
choice of [[prop:vi-c-adm-exist]] meets no exclusion in z.

and keep the rest of the remark ("The set 𝖹 meets I ..."). P-T49's item 8 sentence "Row u5 of [[sec:vi-c-1]] stays true
as written" lapses, as row u5 is removed.

*P-K (not merged; its file is still changing).* Its texts say that the computational point lies outside the set on which
[[thm:settling]] is proved; after this file each should say that it is not shown to lie in it. In every text of P-K,
old and new alike, make these four substitutions and refill the lines: "which lies outside the set on which" becomes
"which is not shown to lie in the set on which" (its opening paragraph); "point, outside that set" becomes "point, which
is not shown to lie in that set" (rem:uc-data-order-limits); "which lies outside that set" becomes "which is not shown to
lie in that set" (its text 3); and "which lies outside the set where the theorem is proved" becomes "which is not shown
to lie in the set where the theorem is proved" (its text 6). Its text 8 overlaps item 43 of this file, which changes the
second line of P-K's old text: after this file, P-K's text 8 has the old text

d is at most an integer below 1.57157 × 10⁵⁰ and N_NM at most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). The
computational point is a point at which the formulas of the proof can be evaluated, and it is not shown to lie in the

and as its new text its present new text with the last line replaced by "computational point is a point at which the
formulas of the proof can be evaluated, and it is not shown to lie in the". P-K's text 2 (the line "same formulas bound
λ1 by δ, ..." of [[ch:explicit-constants]]) is not touched: item 30 of this file ends before it. P-K's other texts do not
overlap this file.

*Other proof files.* P-CIVP, P-CIVP2, P-F123, P-G1, P-B-morawetz, P-B2-band, P-D1-cone, P-D234-residuals, P-E-background,
P-E-margins, P-F-edge, P-H-l24 and the T-files change no place that this file changes; P-CIVP and P-CIVP2 edit
[[ch:introduction]] near its lines 189–191, [[ch:theorems]] near its lines 367–374 and [[ch:scope]] near its line 200,
away from items 41–44.

*Chapter 33 (being edited in parallel; not changed here).* Three sentences there describe the parameter set of the
paper's theorems as h ∈ 𝖧 and go stale after this file. Suggested texts, to be checked against the chapter as it then
stands. In [[sec:iv4-0]], "Every result of this chapter that names (v_C, e_C, C_0, γ_C) uses these values, and so do all
later chapters." becomes "Every result of this chapter that names (v_C, e_C, C_0, γ_C) uses these values, and so do all
later chapters, which hold as well with γ_C = h⁻¹ at every admissible point ([[def:vi-c-admissible]],
[[thm:vi-c-adm-holds]])." In the opening paragraph of [[sec:s14-pa]], "it does not lie in the set 𝖧 of [[eq:iv4-0-1]] on
which the theorems of this paper are stated" becomes "it does not lie in the set 𝖧 of [[eq:iv4-0-1]] on which
[[thm:iii-e-1-1]] is stated". In [[rem:s14-eps-ind-scope]], "The theorems of this paper take h in 𝖧 = (0, h_*) ∖ 𝖹
([[eq:iv4-0-1]]), and h_* = min(10⁻⁶, h_0, h_tf) ≤ 10⁻⁶; so h = 10⁻⁶ is not in 𝖧, and [[prop:s14-damping-distance]] and
[[cor:s14-eps-ind-point]] are used by none of them." becomes "[[thm:iii-e-1-1]] takes h in 𝖧 = (0, h_*) ∖ 𝖹
([[eq:iv4-0-1]]), and h_* = min(10⁻⁶, h_0, h_tf) ≤ 10⁻⁶; so h = 10⁻⁶ is not in 𝖧. [[prop:s14-damping-distance]] and
[[cor:s14-eps-ind-point]] are used in the proof of no theorem; the first shows that (P2) of [[def:vi-c-admissible]] holds
at h = 10⁻⁶ ([[rem:ec-point-outside]])." The sentence after it, "For h ∈ 𝖧 the theorems use only 0 < ε_ind(h) ≤ δ_50,
...", stays true.

### Side findings of the audit, verified

*1. "s_C large" credited to (C1) (41:123–124, 42:559).* True. [[sec:iii-i10-1]] says "The condition ℓ_I < 3/2 + s_C of
[[thm:iii-g2-4-2]] is no restriction, s_C being large by (C1) of [[ch:s15]]", and the setting of [[ch:s23]] says
"[[eq:iii-g3-1-2]] holds, s_C being large by (C1)". (C1) is a statement about the indicial roots of □^C_b, and no proof
in the chapters derives s_C > 100 from it; by [[lem:iii-f1-2-2]] it gives at vector type 1 only −1 − 2γ_Cv_C < −C_0, that
is γ_Cv_C > 49.5, so s_C = (1 − e_C)γ_Cv_C > 49.49 at v_C = ½. The inequality s_C > 100 is the explicit condition of
[[sec:iii-f-1]] (row c4, now a consequence of (P0)). Items 15 and 17 cite it.

*2. 𝖹₂ and 𝖹₃ in row c2.* True. Row c2 removes from 𝖧 the sets 𝖹₂ and 𝖹₃ of [[prop:np-10-52]] (ii)–(iii), and
[[sec:s14-simple]] defines them at z := 4e_Υγ_Υ² = 4·10⁻⁶, "(e_Υ, γ_Υ) = (1/100, 1/100) ... the constants of the gauge
modification"; but step (1) of [[thm:vi-c-2-1]] chose h ∈ 𝖧 before the gauge of step (2), which was any gauge below the
thresholds. For a gauge with z ≠ 4·10⁻⁶ the two sets were a countable excision that gave nothing: the simplicity and the
constant ε_ind at the chosen gauge came from [[prop:iii-f1-2-3]] (e) and (f). Under the definition 𝖧 enters only through
[[prop:vi-c-adm-exist]], as one way to produce admissible points; and P-T49 (thm:t49-uniform) shows 𝖹₂ = ∅.

*3. [[sec:iii-k-0]] (46:92) names [[prop:iii-d1-4-1]] and [[prop:iii-f1-3-3]] but not [[lem:iii-d-7-1]].* True, and
consistent with the audit: [[lem:iii-d-7-1]] (now its part (b)) enters only the proof of [[prop:iii-d1-4-1]]. Item 18
rewrites that paragraph.

*4. A further point found while tracing the roots (not repaired; outside the lead).* [[lem:iii-i11-2-1]] (41:575–590)
builds E′ from "the indicial roots of L̂_b(0) ([[prop:iii-f1-2-3]]) with real part in (q − 2, q′ − 2)" and says "Below
the real part 3 the only such root is 2 (of type s0: the mass)", listing in its proof the roots 2, 3, 1 + λ^Υ, 4, 5 and
l + 2. The list omits the roots ι^C_(·,+) − 1 that come from □^C, which have real part > 1 and can lie below 3:
[[lem:ec-lb-ind]] gives, for every h ≤ 10⁻⁶, the root ι₂(h) − 1 ∈ (1, 1 + 40h/13) of L̂_b(0) at scalar type 2, and at
h = 10⁻⁶ [[lem:s14-scalar-zero]] and [[prop:s14-damping-distance]] put further roots of C and of P_l in (2, 3), that is
entries ι − 1 in (1, 2). Unless their coefficients are shown to vanish, E′ contains them, and the lemma's last sentence
("in u-exponents at level j these are Λ-valued") and its uses in [[ch:s22]] need to account for them. This does not
involve simplicity and is reported for the coordinator.

*5. A small point in the setting of [[sec:iii-d2-1]].* "Fix γ_(Υ,H) ∈ (0, ϵ_0] and then ... e_Υ ∈ (0, ϵ_1] and 0 < |γ_Υ|
< ϵ_1 as in [[prop:iii-d1-4-1]], so that z ∈ (0, ½]" needs 4ϵ_1³ ≤ ½, which [[prop:iii-d1-4-1]] does not state. At an
admissible point (P0) gives z ∈ (0, ¼), so nothing depends on it.
