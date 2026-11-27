#### The smaller index sets at h {#sec:tr-flat}

The index sets ℰ^φ_ind and ℰ^(ι,φ)_ind of [[def:is-flat-set]], which omit the offset 𝔡₀ and which [[thm:uc-integer]]
takes, serve at the computational point ([[thm:is-flat-serves]]). This subsection shows that they serve at every h ∈
(0, 10⁻⁶], with η_0 = 𝔡₁ and J_* = 15,000,015 there and with k̄_0 = 3 and l_* = 50 at every h ∈ [h_m, 10⁻⁶) ∖ 𝖩
([[prop:tr-flat-serves]]), and gives for them the counterparts of [[def:tr-excess]], [[prop:tr-lambda]] and
[[thm:tr-transfer]] (iii) and (ii) ([[def:tr-flat-excess]], [[prop:tr-flat-lambda]], [[thm:tr-flat]],
[[prop:tr-flat-lower]]). Run with these index sets, the proof of [[thm:uc-integer]] meets h through the five inputs
(a)–(e) of the opening of [[sec:tr]], and only (e) enters differently: as 𝔡₁ is the only increment of real part below
1, the gap of (G) is a least excess μ♭(h) ≥ μ(h) in which only multiples of 𝔡₁ are added to the roots of real part below
3, and the count N_Λ has a bound linear in the numbers 3 − Re ι, where that of [[def:tr-excess]] is quadratic. The
setting is that of [[sec:tr]]. Λ^φ denotes the set that [[def:iii-i10-1-1]] builds at h from ℰ^φ_ind and ℰ^(ι,φ)_ind,
with the least ℰ^C_I and the least ℰ_++, and N_Λ := #(Λ^φ ∩ {Re < 3 + ε_+}).

**Proposition {#prop:tr-flat-serves}** (The smaller index sets at h.) Let 0 < h ≤ 10⁻⁶, and let ℰ^φ_ind and ℰ^(ι,φ)_ind
be built by [[def:is-flat-set]] at the parameter point (h, 1/100, 1/100).

(a) ℰ^φ_ind is the same at every such h. Whatever the coefficients c_b are, ℰ^φ_ind and ℰ^(ι,φ)_ind may be taken for
ℰ_ind and ℰ^ι_ind in [[sec:uc-index-sets]]: every proof of this paper that uses ℰ_ind and ℰ^ι_ind holds with them, the
memberships of ω̇_b(0, ·) and ġ^Υ_b(0, ·) being read in the forms [[eq:is-flat-memb]]. Λ^φ lies in the set Λ that
[[def:iii-i10-1-1]] builds at h from the index sets as constructed; 𝔡₁ ∈ π_1ℰ^φ_ind ∩ π_1ℰ^(ι,φ)_ind and
𝔡₀ ∉ π_1(ℰ^φ_ind ∪ ℰ^(ι,φ)_ind); the only increment of Λ^φ of real part below 1 is 𝔡₁; every increment of real part at
most 3/2 is a sum of the increments 𝔡₁, 1, 1 + δ′₁, 1 + δ₂, 1 + 𝔡₀ and 1 + 2𝔡₀; and η_0 = 𝔡₁ and J_* = 15,000,015.

(b) If moreover h_m ≤ h < 10⁻⁶ and h ∉ 𝖩, then k̄_0 = 3 and l_* = 50 are admissible for ℰ^φ_ind and ℰ^(ι,φ)_ind.

*Proof.* (a) We go through the inputs of [[def:is-flat-set]], [[lem:is-flat-memberships]], [[lem:is-flat-uses]] and
[[thm:is-flat-serves]] and record which of them involve h.

*The operator (□^Υ_b)^(0).* ℰ^φ_ind is built by [[lem:iii-a-1-4]], [[lem:iii-a-1-5]] and [[lem:is-typed]] from the
constructions (c1)–(c6) of [[sec:is-ind]], from the poles of N(ρ⁻²(□^Υ_b)^(0), ·)⁻¹½(1 ± φ), and from right sides whose
exponents are integers or exponents of earlier constructions. The operator □^Υ_b = 2δ_(g_b,E_Υ)G_(g_b)δ*_(g_b)
([[eq:iii-b-6-4]]) involves the gauge modification E_Υ and not the constraint damping E_C, which carries h; so its
indicial roots, the set R and the offsets 𝔡₀, 𝔡₁, δ′₁ and δ₂ are fixed by z = 4e_Υγ_Υ² ([[lem:is-roots]],
[[lem:is-offsets]]), and so are the constructions, their right sides and the class roots of (c5). The weights at which
the constructions invert (□^Υ_b)^(0) lie in [0, 2 + 𝔡₁), where E(α) = R + ℕ₀ does not depend on the weight (proof of
[[prop:is-ind]]).

*The parity.* φ commutes with □^Υ_b, P_b and L̂_b(0) at every h, as it preserves the 1-form c_C of the constraint damping
as well as c_Υ and c_(Υ,H) ((P3) of [[lem:iii-i15-1-1]]); and the parities of the constructions, those of the proof of
[[thm:is-d0]] (b), do not involve h.

*The terms at 2 + 𝔡₀.* [[lem:is-rot-s0]], [[def:is-cb]] and [[thm:is-d0]] concern the rotation corrections, ω̇_b(0, ·)
and ġ^Υ_b(0, ·), which are built from g_b by inverting (□^Υ_b)^(0) on decaying spaces (proof of [[prop:iii-d2-3-1]],
[[eq:iii-f3-2-1]]); the constraint damping does not enter them ([[rem:is-cb-open]]), and they do not involve h. So the
pairs removed in [[def:is-flat-set]], the set ℰ^φ_ind, the forms [[eq:is-flat-memb]], the statements (a) and (b) of
[[lem:is-flat-memberships]] and those of its (c) on ℰ^φ_ind and ℰ_(𝔡₀) are the same at every h. [[lem:is-flat-uses]]
lists where and how the proofs of this paper use the memberships of ω̇_b(0, ·) and ġ^Υ_b(0, ·); these proofs are the same
at every admissible parameter point, and the lemma does not involve h.

*The states of [[thm:iii-g2-4-2]].* ℰ^(ι,φ)_ind is built from the index sets of the states of the proof of
[[thm:iii-g2-4-2]], those of the table of [[sec:iii-g2-1]] and the s1 and v1 terms (proof of [[prop:is-iota]]): the
states of [[ch:s13]] and ġ^Υ_b, which are constructions of [[sec:is-ind]] or tensors built from them and do not involve
h, and the physical states of [[prop:iii-f4-5-1]], built from the roots of L̂_b(0), which do. (C1) holds at every h ∈
(0, 10⁻⁶] ([[lem:iv4-1-3]] (a)), so every root of L̂_b(0) of positive real part has real part greater than 1
([[prop:iii-f1-2-3]] (a)), and by the proof of [[prop:is-iota]], which uses of h only (C1) (proof of [[prop:tr-inputs]]
(a)), the exponents that the physical states add to those of the constructions of [[sec:is-ind]] are integers and the
numbers ι + 1 + j, ι ∈ Z(h), j ∈ ℕ₀, whose real parts exceed 3 ([[prop:np-10-54]] (ii)); an offset of a physical state is
an integer, an offset of such a construction other than ω̇_b(0, ·), or a number of real part at least 1 (proof of
[[prop:is-logs]] (c)). So at h the exponents of ℰ^ι_ind as constructed of real part at most 3 are those of ℰ_ind and
integers, and the proof of [[lem:is-flat-memberships]] (c) applies at h: the rules [[eq:is-l1]] and [[lem:is-count]] (b)
are monotone in E(α), ord and F, which does not involve h, so ℰ^(ι,φ)_ind ⊂ ℰ^ι_ind; 𝔡₁ ∈ π_1ℰ^(ι,φ)_ind, as the
translation corrections enter the s1 terms; and 𝔡₀ ∉ π_1ℰ^(ι,φ)_ind. Hence the exponents of ℰ^φ_ind ∪ ℰ^(ι,φ)_ind of real
part at most 3/2 are among 1 and the numbers of [[eq:is-low]] other than 𝔡₀, their least real part is 𝔡₁, and their
logarithmic orders are at most those of ℰ_ind and ℰ^ι_ind as constructed at h.

*The proof of [[thm:is-flat-serves]] at h.* Besides the statements above, that proof uses the conditions on ℰ_+, which
are conditions on ℰ_+ alone ([[lem:iii-i10-1-2]] (b)), the count of [[lem:iii-i10-1-2]] (c), the six increments, which
come from the translation and rotation corrections, from ω̇_b(1, 0) and from the class μ_s0, and the inclusions
ℰ^φ_ind ∪ ℰ_(𝔡₀) ⊂ ℰ_ind and ℰ^(ι,φ)_ind ⊂ ℰ^ι_ind. None of these involves h beyond what was just shown, so that proof
gives at h the memberships, Λ^φ ⊂ Λ and the statements on the increments. η_0, the least real part of the increments, is
𝔡₁, and J_* = ⌈5/𝔡₁⌉ + 2 = 15,000,015 ([[prop:is-count]] (c), which reads only 𝔡₁). This proves (a).

(b) l_* bounds, at real part at most 5, the logarithmic orders of ℰ_ind ∪ ℰ^ι_ind ∪ ℰ^C_I, the orders of the poles of
N_ι⁺(L̄, ·)⁻¹ and the multiplicities of the roots of L̂_b(0); k̄_0 bounds, below 2λ_♯, the logarithmic orders of
ℰ⁰_src ∪ ℰ_++ ∪ 𝒢 ∪ (2 + ℰ_col), which are built from ℰ_ind and ℰ^ι_ind by unions and sums, so that smaller index sets
give orders at most as large ([[def:iii-i10-1-1]]); the orders of the poles and the multiplicities do not depend on the
index sets. By (a), the logarithmic orders for ℰ^φ_ind and ℰ^(ι,φ)_ind are at most those for the index sets as
constructed at h. For these, [[prop:tr-inputs]] gives at h the exponents of ℰ^ι_ind of real part at most 5 and their
logarithmic orders, at most 3 at real part at most 3/2 and at most 50 at real part at most 5, the multiplicities, and
[[cor:sp-lstar]] (a)–(c), so that l_* = 50 is admissible ([[prop:tr-inputs]] (d)); and the proof of [[prop:is-count]] (b)
reads only the exponents of ℰ_ind ∪ ℰ^ι_ind of real part below 2λ_♯ − λ_♯ = 1.5099, which are those of real part at most
3/2, and their logarithmic orders, which by [[prop:tr-inputs]] (a) are those of ℰ_ind and the integer 1, with orders at
most 3, as at the computational point; so k̄_0 = 3 is admissible at h. Both are therefore admissible for ℰ^φ_ind and
ℰ^(ι,φ)_ind. ∎

On 𝖩, and for h < h_m, part (a) holds and the proof of part (b) is not available: it rests on (H_ε) and on the simplicity
of [[prop:tr-inputs]] (b), which are proved only for h ≥ h_m off 𝖩 ([[prop:tr-eps]] (a), [[prop:tr-inputs]]); on 𝖩
they can fail ([[rem:tr-scope]]), and (H_ε) fails at every h ≤ 13ε_Υ/40 ([[prop:tr-eps]] (b)). This is the restriction
under which [[thm:tr-transfer]] (iii) holds for the index sets as constructed; the smaller index sets add none of their
own.

**Definition {#def:tr-flat-excess}** (The least excess for the smaller index sets.) Let 0 < h ≤ 10⁻⁶, and let Z₃(h) and
y_ι be as in [[def:tr-excess]]. For y > 0 let m♭(y) := (⌊y/𝔡₁⌋ + 1)𝔡₁ − y, the least positive number q𝔡₁ − y with q ∈ ℕ₀,
and with μ♭ = λ_♯ + 4470304𝔡₁ − 3 of [[cor:is-flat]] put

    μ♭(h) := min({μ♭} ∪ {m♭(y_ι) : ι ∈ Z₃(h)}),     N̄♭(h) := 59,377,257 + Σ_(ι∈Z₃(h)) (⌊y_ι/𝔡₁⌋ + 1).

Z₃(h) being finite, μ♭(h) is a positive minimum and N̄♭(h) an integer. As m♭(y) is one of the numbers whose infimum is
m(y) ([[lem:is-reduction]]), m(y) ≤ m♭(y) ≤ 𝔡₁, and μ_G < μ♭ ([[eq:is-mu]], [[cor:is-flat]]); so μ(h) ≤ μ♭(h) ≤
μ♭ < 5.0193·10⁻⁸. At h = 10⁻⁶, μ♭(h) = μ♭_Z and N̄♭(h) = 59,377,257 + 3,623,813,354 = 3,683,190,611 (proof of
[[cor:is-flat]]).

**Proposition {#prop:tr-flat-lambda}** (The set Λ^φ at h.) Let ℬ♭ be the set of the 31 numbers

    λ_♯,  λ_♯ + 1 + δ′₁,  λ_♯ + 1 + δ₂,  λ_♯ + 1 + 𝔡₀,  λ_♯ + 1 + 2𝔡₀,  2 + c (c ∈ σ^(2)),  5/2 + c (c ∈ σ^(3)),  3,

let Λ^φ_ℬ be the smallest set, closed under conjugation, that contains the generators of Λ^φ other than 1 + 𝒵 and
satisfies Λ^φ_ℬ + w ⊂ Λ^φ_ℬ for every increment w of Λ^φ, and let 0 < ε_+ < ε_Υ.

(a) At every h ∈ (0, 10⁻⁶] and for every ε ∈ (0, δ₂), Λ^φ_ℬ ∩ {Re ≤ 3 + ε} = {β + q𝔡₁ ≤ 3 + ε : β ∈ ℬ♭, q ∈ ℕ₀}, a set of
real numbers that does not depend on h; and for every ε_K > 0, (G) holds with Λ^φ_ℬ in place of Λ if and only if
ε_K < μ♭, the element λ_♯ + 4470304𝔡₁ = 3 + μ♭ having the least excess over the windows. If h is as in [[lem:tr-z3]],
then

    Λ^φ ∩ {Re ≤ 3 + ε_+} = (Λ^φ_ℬ ∩ {Re ≤ 3 + ε_+}) ∪ {ι + q𝔡₁ : ι ∈ Z₃(h), q ∈ ℕ₀, q𝔡₁ ≤ y_ι + ε_+},

every element of Λ^φ ∖ Λ^φ_ℬ of real part at most 3 + ε_+ has real part greater than 2 + 1.4646·10⁻¹⁰, and every element
of Λ^φ of real part at most 2.1 is real.

(b) Let h be as in [[lem:tr-z3]]. Then 0 < μ♭(h) ≤ μ♭ and μ(h) ≤ μ♭(h). For 0 < ε_K < ε_Υ, (G) of [[def:iii-i10-1-3]]
holds for Λ^φ if and only if ε_K < μ♭(h), and (G⁺) of [[def:iii-j-g-plus]] holds for Λ^φ if and only if ε_+ < μ♭(h).

(c) Let h be as in [[lem:tr-z3]]. Then N_Λ ≤ 59,377,257 + Σ_(ι∈Z₃(h)) (⌊(y_ι + ε_+)/𝔡₁⌋ + 1); if ε_+ < μ♭(h), this number
is N̄♭(h); and

    N̄♭(h) < 1.33738·10⁹ + 4.0697·10⁶h^(−1/2).

*Proof.* (a) *The part Λ^φ_ℬ.* Let 0 < ε < δ₂. Every generator of Λ^φ_ℬ has real part at least λ_♯ ([[lem:iii-i10-1-2]]
(a)) and every increment real part at least 𝔡₁ ([[prop:tr-flat-serves]] (a)), so below 3 + ε only increments of real part
below 3 + ε − λ_♯ < 3/2 enter. By [[prop:tr-flat-serves]] (a) their sums are the sums of 𝔡₁, 1, 1 + δ′₁, 1 + δ₂, 1 + 𝔡₀
and 1 + 2𝔡₀, so those below 3/2 are the q𝔡₁ and the t + q𝔡₁ with q ∈ ℕ₀ and t ∈
T := {1, 1 + δ′₁, 1 + δ₂, 1 + 𝔡₀, 1 + 2𝔡₀}. The generators below 3 + ε: the exponents of ℰ_++ there are λ_♯ plus sums of
exponents of ℰ^φ_ind ∪ ℰ^(ι,φ)_ind, as an exponent of ℰ_+ adds at least λ_♯ (proof of [[lem:iii-i10-1-2]] (b), with
ℰ^♯_+ ∩ {Re < 2} = {(λ_♯, 0)} by [[prop:is-ci-pp]] (b)); π_1𝒢 = {2} ∪ (2 + π_1ℰ^φ_ind) and 2 + π_1ℰ_col ⊂ π_1𝒢 + ℕ₀
consist of 2 plus sums of increments; π_1ℰ^C_I gives 2 + c (c ∈ σ^(2)), 5/2 + c (c ∈ σ^(3)) and 3 ([[prop:is-ci-pp]] (a),
as ε < 0.0099); and λ_♯ and 3 are generators. So every element of Λ^φ_ℬ below 3 + ε is g + q𝔡₁ or g + t + q𝔡₁ with t ∈ T
and g in G := {λ_♯, 3} ∪ {2 + c : c ∈ σ^(2)} ∪ {5/2 + c : c ∈ σ^(3)}, and each such number lies in Λ^φ_ℬ. For g ≠ λ_♯,
g + t ≥ 3, with equality only for 2 + 1, and 2 + t > 3 + ε for t ≠ 1, as δ₂ < δ′₁ < 𝔡₀ ([[lem:is-roots]] (b)); and 2 +
1 + q𝔡₁ = 3 + q𝔡₁. For g = λ_♯, λ_♯ + 1 = 5/2 + a with a = 0.0099 ∈ σ^(3), and two elements of T give more than λ_♯ + 2.
This gives the set stated; it does not involve h, and its elements are real.

*Its excesses.* For 0 < ε < δ₂: an element of Λ^φ_ℬ in (2, 2 + ε] is λ_♯ + q𝔡₁, of excess at least m♭(0.4901), or 2 + q𝔡₁
with q ≥ 1, of excess at least 𝔡₁. A number λ + 𝔡₀ with λ ∈ Λ^φ_ℬ and real part in (2, 2 + ε] has Re λ < 2, as 𝔡₀ > δ₂ >
ε, so λ = λ_♯ + q𝔡₁, and its excess is at least m♭(0.4901 − 𝔡₀); a number λ + 𝔡₁ lies in Λ^φ_ℬ, 𝔡₁ being an increment. An
element of Λ^φ_ℬ in (3, 3 + ε] is β + q𝔡₁ with β ∈ ℬ♭, of excess at least m♭(3 − β) if β < 3 and at least 𝔡₁ if β = 3.
The 30 numbers 3 − β, β ∈ ℬ♭ ∖ {3}, are the 28 numbers y of the table of [[thm:is-gap]] and 0.4901 − 𝔡₀ and 0.4901 − 2𝔡₀.
By the column "frac" of that table and the values 1470297.2661 and 1470293.2661 of y/𝔡₁ at 0.4901 − 𝔡₀ and 0.4901 − 2𝔡₀
(proof of [[cor:is-flat]]), m♭(y) = (⌊y/𝔡₁⌋ + 1 − y/𝔡₁)𝔡₁ is least at y = 1.4901, where it is 4470304𝔡₁ − 1.4901 = μ♭,
and above 1.3888·10⁻⁷ at the other 29 numbers; m♭(0.4901) and m♭(0.4901 − 𝔡₀) exceed 2.446·10⁻⁷. As μ♭ < 1.3888·10⁻⁷ <
𝔡₁, the least excess of Λ^φ_ℬ over the windows of (G) is μ♭, attained in the second window by λ_♯ + 4470304𝔡₁; so for
ε_K < μ♭ (G) holds on Λ^φ_ℬ, and for ε_K ≥ μ♭ that element violates it.

*The generator 1 + 𝒵.* Let h be as in [[lem:tr-z3]]. (C1) holds at h ([[lem:iv4-1-3]] (a)), so, as in the proof of
[[prop:is-lambda]], 1 + 𝒵 = {3} ∪ {ι ∈ Z(h) : Re ι < 4}, and 3 ∈ ℬ♭. Let ι ∈ Z(h) with Re ι < 4. If Re ι ≥ 3, then
Re ι ≥ 3 + ε_Υ > 3 + ε_+ ([[lem:tr-z3]] (a)), and so is every sum with it. If Re ι < 3, then ι ∈ Z₃(h) and
Re ι > 2 + 1.4646·10⁻¹⁰ ([[lem:tr-z3]] (a)); an increment of real part at least 1 takes it above
3 + 1.4646·10⁻¹⁰ > 3 + ε_+, and 𝔡₁ is the only increment of real part below 1 ([[prop:tr-flat-serves]] (a)). So the sums
with ι of real part at most 3 + ε_+ are the ι + q𝔡₁ with q𝔡₁ ≤ y_ι + ε_+, and each lies in Λ^φ. Z₃(h) is closed under
conjugation, the polynomials having real coefficients, and a non-real ι ∈ Z₃(h) has real part greater than 2.1
([[lem:tr-z3]] (a)); with the first part of (a) at ε = ε_+ < ε_Υ < δ₂, this gives the rest of (a).

(b) μ♭(h) is a positive minimum and μ(h) ≤ μ♭(h) ≤ μ♭ ([[def:tr-flat-excess]]). Let 0 < ε_K < ε_Υ, and apply (a) with ε_K
in place of ε_+. An element of Λ^φ ∖ Λ^φ_ℬ of real part at most 3 + ε_K has real part greater than
2 + 1.4646·10⁻¹⁰ > 2 + ε_K, and every λ ∈ Λ^φ ∖ Λ^φ_ℬ has real part greater than 2, as the elements of 1 + 𝒵 do
([[lem:iii-i10-1-2]] (a), proof), so that λ + 𝔡₀ and λ + 𝔡₁ have real part greater than 2 + 𝔡₁ > 2 + ε_K. So the first
and the third window hold no element coming from Λ^φ ∖ Λ^φ_ℬ, and in the second window such an element is ι + q𝔡₁ or its
conjugate, ι ∈ Z₃(h), of real part 3 + q𝔡₁ − y_ι, whose excess, if positive, is at least m♭(y_ι) ≥ μ♭(h). With the
excesses of Λ^φ_ℬ, at least μ♭ ≥ μ♭(h) by (a), (G) holds if ε_K < μ♭(h). Conversely Λ^φ contains λ_♯ + 4470304𝔡₁ = 3 + μ♭
and, for each ι ∈ Z₃(h), ι + (⌊y_ι/𝔡₁⌋ + 1)𝔡₁, of real part 3 + m♭(y_ι); one of these has real part 3 + μ♭(h), and (G)
keeps it out of (3, 3 + ε_K], so ε_K < μ♭(h). By (a), the elements of Λ^φ of real part in (3, 3 + ε_+] are elements of
Λ^φ_ℬ, of excess at least μ♭, and numbers ι + q𝔡₁ and their conjugates, of excess at least m♭(y_ι); so none exists when
ε_+ < μ♭(h), and the element of real part 3 + μ♭(h) is one when ε_+ ≥ μ♭(h). This is the statement on (G⁺).

(c) By (a), N_Λ is at most #(Λ^φ_ℬ ∩ {Re < 3 + ε_+}) + Σ_(ι∈Z₃(h)) #{q ∈ ℕ₀ : q𝔡₁ < y_ι + ε_+}. For β ∈ ℬ♭ ∖ {3}, the
q ∈ ℕ₀ with β + q𝔡₁ < 3 + ε_+ number at most ⌊(3 − β)/𝔡₁⌋ + 1, as m♭(3 − β) ≥ μ♭ > ε_Υ > ε_+ by (a); for β = 3 only q = 0
occurs, as ε_+ < 𝔡₁. By the column n⁺ = ⌊y/𝔡₁⌋ of the table of [[thm:is-gap]], for its 28 numbers y, and the values
1470297 and 1470293 of ⌊y/𝔡₁⌋ at y = 0.4901 − 𝔡₀ and 0.4901 − 2𝔡₀, the sum of the ⌊(3 − β)/𝔡₁⌋ + 1 over β ∈ ℬ♭ ∖ {3} is
59,377,256; so Λ^φ_ℬ has at most 59,377,257 elements of real part below 3 + ε_+.
For y > 0, #{q ∈ ℕ₀ : q𝔡₁ < y + ε_+} ≤ ⌊(y + ε_+)/𝔡₁⌋ + 1, and this is ⌊y/𝔡₁⌋ + 1 when ε_+ < m♭(y), as then
y + ε_+ < (⌊y/𝔡₁⌋ + 1)𝔡₁. This gives the bound for N_Λ and, when ε_+ < μ♭(h) ≤ m♭(y_ι) for every ι ∈ Z₃(h), its value
N̄♭(h).

*The bound for N̄♭(h).* As ⌊y/𝔡₁⌋ + 1 ≤ y/𝔡₁ + 1, N̄♭(h) ≤ 59,377,257 + #Z₃(h) + 𝔡₁⁻¹ Σ_(ι∈Z₃(h)) y_ι, and #Z₃(h) <
426 + 2.7177h^(−1/2) ([[lem:tr-z3]] (b)). By the proof of [[lem:tr-z3]] (b), the at most 426 elements of Z₃(h) that are
roots of C or of the P_l with l ≤ 142 have y_ι < 1; for l ≥ 143, ι_B(l, h) lies in Z₃(h) only if x < 1.01, with y_ι <
f_B(x), and ι_P(l, h) and ῑ_P(l, h) only if x < 11/15, with y_ι < f_P(x), where f_B(x) := 1 − x/2 for 0 ≤ x ≤ 1/2,
f_B(x) := 1.01 − x for 1/2 < x < 1.01 and f_B(x) := 0 for x ≥ 1.01, and f_P(x) := (3/4)(11/15 − x) for x < 11/15 and
f_P(x) := 0 for x ≥ 11/15 ([[lem:tr-large]] (a), (c)). Both functions are non-increasing, so f(hl(l + 2)) ≤ f(ht²) for
l − 1 ≤ t ≤ l, and

    Σ_(l≥143) f(hl(l + 2)) ≤ ∫_0^∞ f(ht²) dt = ½h^(−1/2) ∫_0^∞ f(x)x^(−1/2) dx,

which is below 0.728547h^(−1/2) for f_B and 0.313995h^(−1/2) for f_P. So Σ_(ι∈Z₃(h)) y_ι < 426 + 1.356537h^(−1/2), as
0.728547 + 2 · 0.313995 = 1.356537. With 1/𝔡₁ < 3,000,002.5834 ([[lem:is-offsets]] (b)), 426 · 3,000,002.5834 <
1,278,001,101 and 3,000,002.5834 · 1.356537 < 4,069,614.6, this gives N̄♭(h) < 59,377,683 + 1,278,001,101 +
(2.7177 + 4,069,614.6)h^(−1/2) < 1.33738·10⁹ + 4.0697·10⁶h^(−1/2). ∎

**Theorem {#thm:tr-flat}** (The bounds at other values of h for the smaller index sets.) Let h_m ≤ h < 10⁻⁶ with h ∉ 𝖩,
and suppose that the parameter point (h, 1/100, 1/100) is admissible and that (R_h) holds. Take (v_C, e_C) of
[[eq:iv4-0-1]], the index sets ℰ^φ_ind and ℰ^(ι,φ)_ind built at h ([[prop:tr-flat-serves]]), and μ♭(h) and N̄♭(h) of
[[def:tr-flat-excess]]. Then μ(h) ≤ μ♭(h) ≤ μ♭ and N̄♭(h) < 1.33738·10⁹ + 4.0697·10⁶h^(−1/2). For any ε_K, ε_+ with
0 < ε_K < ε_+ < min(μ♭(h), ε_Υ) and ε_K < 0.998ε_Υ, N_Λ ≤ N̄♭(h); the choice of [[def:uc-choice]] with these ε_K and ε_+
and with ℰ^φ_ind and ℰ^(ι,φ)_ind built at h, and that of [[def:cs-choices]], is admissible; and d_acc ≤ d_R ≤ D_acc,
d_NM ≤ D_NM and N_NM ≤ 21D_NM + 6, with D_acc and D_NM of [[prop:uc-dependence]] at k̄_0 := 3, J_* := 15,000,015,
l_* := 50 and N̄_Λ := N̄♭(h).

At h = 10⁻⁶, μ♭(h) = μ♭_Z and N̄♭(h) = 3,683,190,611 ([[def:tr-flat-excess]]); the numbers ε_K = 1.4589·10⁻¹⁰ and
ε_+ = 1.459·10⁻¹⁰ of [[eq:uc-choice]] satisfy the conditions above; and the bounds of [[prop:uc-dependence]] at these
inputs are those of [[thm:uc-integer]]: N_Λ ≤ 3,683,190,611 ([[cor:is-flat]]), d_NM < 1.42556·10³⁸, and K < 3.13622·10³⁹
([[prop:uc-data-order]] (d)).

*Proof.* The first assertions are [[def:tr-flat-excess]] and [[prop:tr-flat-lambda]] (c). Let ε_K and ε_+ be as stated.
As ε_+ < μ♭(h), N_Λ ≤ N̄♭(h) ([[prop:tr-flat-lambda]] (c)). By [[prop:tr-flat-serves]], ℰ^φ_ind and ℰ^(ι,φ)_ind may be
taken for ℰ_ind and ℰ^ι_ind at h, and k̄_0 = 3, l_* = 50, η_0 = 𝔡₁ and J_* = 15,000,015 are admissible for them; the
proof of [[lem:uc-lambda]] (c), which uses only N_Λ ≤ N̄_Λ, these numbers and the order of the elements by their real
parts, gives its statement at h with N̄_Λ := N̄♭(h). The proof of [[lem:uc-admissible]] applies at h with these ε_K and
ε_+ and with these index sets: (G) and (G⁺) hold, as ε_K < ε_+ < min(μ♭(h), ε_Υ) ([[prop:tr-flat-lambda]] (b));
ε_ind(h) ≥ ε_Υ ([[prop:tr-eps]] (a)) allows ε_ind := min(1, ε_ind(h)) ≥ ε_Υ, so ε_g = ε_Υ, and 0 < ε_K < ε_+ < ε_Υ ≤
ε_ind and ε_+ < δ_♯ = 0.0099 meet the constants of [[eq:iii-i9-1-1]], with ε_K < ε_Υ, as [[def:iii-i10-1-3]] asks; (Ex2)
holds as there, ℰ^C_I being the same; η_1 and η_2 exist, as Λ^φ ∩ {Re ≤ 4} is finite ([[lem:iii-i10-1-2]] (a)); α can be
taken with 0.999ε_K ≤ α − 4 ≤ ε_K, off finitely many values; with ε ≤ 10⁻³ε_g, ε_K + ε < 0.999ε_Υ < ε_g and
ε_K < 0.998ε_Υ ≤ ε_g − 2ε; and every other step uses the index sets and choices that do not involve h. So the hypotheses
of [[prop:ec-upper]] and of [[eq:ec-upper-counts]] hold with Δβ_0 = 0.999²ε_K and Δτ_0 = 0.999ε_Υ, and ε_K < 0.998ε_Υ, as
[[prop:uc-dependence]] asks. Of the other statements of [[sec:ec-gap-sums]]–[[sec:cs-small]] that the proofs of
[[thm:uc-integer]] and [[prop:uc-dependence]] use, [[prop:gap-sums]], [[lem:ec-gauge-gap]], [[prop:is-ind]],
[[thm:is-d0]] and [[lem:uc-two-offsets]] concern numbers fixed by (γ_Υ, e_Υ); [[def:is-flat-set]]–[[thm:is-flat-serves]]
hold at h by [[prop:tr-flat-serves]], and [[prop:tr-flat-lambda]] takes the place of [[cor:is-flat]]; [[prop:is-ci-pp]]
(a) concerns the least ℰ^C_I, fixed by σ_Υ; [[lem:uc-gaps]] holds, as min Re ℰ^φ_ind = min Re ℰ^(ι,φ)_ind = η_0 = 𝔡₁
([[prop:tr-flat-serves]] (a)), and [[lem:uc-lambda]] and [[lem:uc-n-iota]] use the increments and the counts above; in
[[sec:cs]] the charges are closed forms in the weights and the counts, the forward loss, which holds for every γ_C
([[lem:fwd-orders]]), ℓ_tf = 1 ([[prop:uc-ltf]]), d_BG = 11 ([[prop:uc-dbg]]) and the free choices of [[def:cs-choices]],
of which (a) uses ϑ_ℋ < ϑ_L + δ with ϑ_L = max(0, 2 − 2a_vγ_Cr_h) < 2 at every γ_C, and (f) the interval
(2, 2 + ε_g − 2ε) with ε_g = ε_Υ; and the proof of [[lem:cs-fourier]] (b) uses ε_ind > ε_K and the reality of the
elements of Λ^φ of real part at most 2 + ε_K, which [[prop:tr-flat-lambda]] (a) gives, and 𝒵 ⊂ {Re > 1}, which holds at
every h ([[prop:iii-f1-2-3]] (a)). The proof of [[prop:uc-dependence]] uses, of the index sets, only the least ℰ^C_I,
min Re ℰ_ind = min Re ℰ^ι_ind = 𝔡₁ and that reality. So it applies at h, with ℰ^φ_ind and ℰ^(ι,φ)_ind, N̄_Λ := N̄♭(h),
k̄_0 = 3, J_* = 15,000,015 and l_* = 50, and gives the bounds.

*At h = 10⁻⁶.* The values of μ♭(h) and N̄♭(h) are those of [[def:tr-flat-excess]]. The numbers of [[eq:uc-choice]]
satisfy ε_K < ε_+ < ε_Υ = 1.4619·10⁻¹⁰ < μ♭_Z and ε_K < 0.998ε_Υ = 1.4589762·10⁻¹⁰, and [[def:uc-choice]] takes
N̄_Λ = 3,683,190,611, k̄_0 = 3, J_* = 15,000,015 and l_* = 50 ([[lem:uc-lambda]]). At these inputs
[[prop:uc-dependence]], with D_e of [[prop:uc-explicit]], gives the integers D_acc and D_NM of [[thm:uc-integer]], so
that d_NM ≤ D_NM < 1.42556·10³⁸; [[prop:uc-data-order]] (d) gives K ≤ 22D_NM + 345 < 3.13622·10³⁹; and
N_Λ ≤ 3,683,190,611 is [[cor:is-flat]]. ∎

**Proposition {#prop:tr-flat-lower}** (Lower bounds for the smaller index sets.) Let 0 < h ≤ 10⁻⁶ be such that the
parameter point (h, 1/100, 1/100) is admissible, and take ℰ^φ_ind and ℰ^(ι,φ)_ind built at h
([[prop:tr-flat-serves]] (a)).

(a) Every ε_K with which (G) holds for Λ^φ satisfies ε_K < μ♭(h), and [[def:iii-i10-1-3]] asks ε_K < ε_Υ besides. Every
admissible choice of the weights with these index sets gives d_NM ≥ d_acc > 2.0517·10¹⁰/min(μ♭(h), ε_Υ), which is at
least 2.0517·10¹⁰/μ♭(h), and N_NM > 4.3085·10¹¹/min(μ♭(h), ε_Υ).

(b) There is h♭ ∈ (5·10⁻⁷, 10⁻⁶) such that ι_B(390, h♭) + 2541391𝔡₁ = 3 and ι_B(390, h) + 2541391𝔡₁ > 3 for
h♭ < h ≤ 10⁻⁶, and for these h, μ♭(h) ≤ ι_B(390, h) + 2541391𝔡₁ − 3, which tends to 0 as h decreases to h♭. So for every
D there is δ > 0 such that at every h ∈ (h♭, h♭ + δ) at which the parameter point (h, 1/100, 1/100) is admissible, every
admissible choice of the weights with these index sets gives d_NM > D.

*Proof.* (a) By [[prop:tr-flat-serves]] (a), λ_♯ is a generator of Λ^φ and 𝔡₁ an increment, so λ_♯ + 4470304𝔡₁ = 3 + μ♭
lies in Λ^φ. For ι ∈ Z₃(h), ι − 1 is an indicial root of L̂_b(0) of real part in (0, 3), as (C1) holds at h
([[lem:iv4-1-3]] (a), proof of [[prop:is-lambda]]), so ι ∈ 1 + 𝒵 and ι + (⌊y_ι/𝔡₁⌋ + 1)𝔡₁ ∈ Λ^φ, of real part
3 + m♭(y_ι). As Z₃(h) is finite ([[def:tr-excess]]), one of these elements has real part 3 + μ♭(h), and (G) keeps it out
of (3, 3 + ε_K]; so ε_K < μ♭(h). The proof of [[prop:ec-rounds]] uses of h only ε_g ≤ ε_Υ < δ̂ and ε_ind ≤ δ_50 < δ̄, and
gives R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂), whose right side decreases in ε_K. Put m := min(μ♭(h), ε_Υ); then ε_K < m ≤
1.4619·10⁻¹⁰, so 3m + 2δ̂ + δ̄ < 2.02·10⁻⁸ and R > (1 − 2.02·10⁻⁸)/(δ̂m). By the argument of [[thm:loss-d]] (ii), which
does not use the computational point (proof of [[thm:ec-lb-proved]]), d_NM ≥ d_acc ≥
3R > 3(1 − 2.02·10⁻⁸)/(1.46214·10⁻¹⁰m) > 2.0517·10¹⁰/m, and N_NM = 21d_NM + 6 > 4.3085·10¹¹/m.

(b) Let l = 390, so κ = 152880 and y = eκ > 1.49 > 1/5; for 0 < h ≤ 10⁻⁶, x = hκ ≤ 0.15288, and ι_B(390, h) is defined,
depends continuously on h and lies in (2 + x/2, 2 + 3x/2) ([[def:tr-exceptional]] (b), [[lem:tr-large]] (a)). At h = 10⁻⁶
the root ι_* of [[lem:is-gap-z]] is real and |ι_* − 2.15288| < 1/100, so ι_* = ι_B(390, 10⁻⁶), and ι_* + 2541391𝔡₁ − 3 =
2541391𝔡₁ − y_(ι_*) > 1.35·10⁻⁷ (proof of [[lem:is-gap-z]]). At h = 5·10⁻⁷, x = 0.07644 and ι_B < 2.11466, while
2541391𝔡₁ < 0.8471297 ([[lem:is-offsets]] (b)), so ι_B + 2541391𝔡₁ < 3. Let h♭ be the largest h ∈ [5·10⁻⁷, 10⁻⁶] with
ι_B(390, h) + 2541391𝔡₁ ≤ 3; by continuity h♭ ∈ (5·10⁻⁷, 10⁻⁶), ι_B(390, h♭) + 2541391𝔡₁ = 3, and
ι_B(390, h) + 2541391𝔡₁ > 3 for h♭ < h ≤ 10⁻⁶. For such h, ι := ι_B(390, h) lies in Z₃(h), as 2 < ι < 2 + 3x/2 < 3, and
2541391𝔡₁ − y_ι = ι + 2541391𝔡₁ − 3 > 0, so m♭(y_ι) ≤ ι + 2541391𝔡₁ − 3 and μ♭(h) ≤ ι + 2541391𝔡₁ − 3
([[def:tr-flat-excess]]); this tends to 0 as h decreases to h♭. The last assertion follows from (a). ∎

**Remark {#rem:tr-flat-scope}** (What the bounds for the smaller index sets assume.) [[thm:tr-flat]] is conditional in
the three ways of [[rem:tr-scope]]: it needs an h ∈ [h_m, 10⁻⁶) at which the parameter point (h, 1/100, 1/100) is
admissible, which this paper does not decide; it needs (R_h), which is decided only at h = 10⁻⁶; and its bound is a
number only once μ♭(h) is known, which is evaluated only at h = 10⁻⁶. Elsewhere this paper proves only μ(h) ≤ μ♭(h) ≤ μ♭
and, on (h♭, 10⁻⁶], an upper bound for μ♭(h) that tends to 0 at h♭ ([[prop:tr-flat-lower]]); and as
μ♭(h) ≤ Re ι + q𝔡₁ − 3 whenever ι ∈ Z₃(h), q ∈ ℕ₀ and this number is positive, μ♭(h) tends to 0 wherever such a number,
for a root that moves continuously with h, tends to 0 from above. The count N̄♭(h) is explicit in the numbers y_ι, and
its bound in [[prop:tr-flat-lambda]] (c) is below 5.408·10⁹ at h = 10⁻⁶ and below 5.913·10¹¹ at h = h_m, against
N̄♭(10⁻⁶) = 3,683,190,611. So at the h of [[thm:tr-flat]], N̄♭(h) < 1.67472·10¹³ ≤ N̄(h); and as μ(h) ≤ μ_G < 0.998ε_Υ
([[eq:is-mu]]) and μ(h) ≤ μ♭(h), every ε_K and ε_+ that [[thm:tr-transfer]] (iii) admits are admitted by [[thm:tr-flat]],
which then gives a bound at most that of [[thm:tr-transfer]] (iii) when D_e := F_1 in both, D_acc and D_NM being
non-decreasing in N̄_Λ ([[prop:uc-dependence]]). The lower bounds of [[prop:tr-flat-lower]] use only admissibility.

### Placement

This part, the notes and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
Old texts are quoted exactly, in fenced blocks, from the chapters at HEAD aa181269, where they are the same as at
40140118; line numbers serve only to find the place. Each new text replaces its old text as a whole, with the
line breaks shown. Every old text occurs exactly once in its file.

*1. Where the subsection goes.*
(chapters/71-explicit-constants.md:6449–6451) The subsection above, from its heading ("The smaller index sets at h",
label sec:tr-flat) through the last line of rem:tr-flat-scope, is inserted at the end of sec:tr, between the last
line of the paragraph that follows prop:tr-mu-small and the heading of sec:ec-linear, with one blank line before
and one after it, as the seventh "####" subsection of sec:tr. Old (the place):

```old
d_NM > 0.3168h⁻², which exceeds 1.42556·10³⁸ for h ≤ 4.71·10⁻²⁰ ([[rem:ec-lb-unbounded]]).

### The first constants of the linear theory {#sec:ec-linear}
```

New: the first line of the old text, a blank line, the subsection above, a blank line, and the heading.

*2. The opening of [[ch:explicit-constants]], the sentence on the other values of h.*
(chapters/71-explicit-constants.md:36–37) Old:

```old
condition on the roots of the damping polynomials of large degree that is decided only at h = 10⁻⁶ ([[thm:tr-transfer]],
[[prop:tr-mu-small]]). The
```

New:

```new
condition on the roots of the damping polynomials of large degree that is decided only at h = 10⁻⁶ ([[thm:tr-transfer]],
[[prop:tr-mu-small]]). For the smaller index sets of [[def:is-flat-set]], which the choice above takes and which serve at
these h as well, the same holds with the least excess μ♭(h) ≥ μ(h) that they give in place of μ(h), with some
h♭ ∈ (5 × 10⁻⁷, 10⁻⁶) in place of h_μ, and with a count below 1.33738 × 10⁹ + 4.0697 × 10⁶h^(−1/2) ([[thm:tr-flat]],
[[prop:tr-flat-lower]]). The
```

*3. The last sentence of [[rem:ec-point-outside]].*
(chapters/71-explicit-constants.md:98–99) Old:

```old
root of real part in [2, 3 + ε_Υ), a condition decided only at h = 10⁻⁶, the bounds of [[prop:uc-dependence]] hold with
the gap and the count at h ([[thm:tr-transfer]]).
```

New:

```new
root of real part in [2, 3 + ε_Υ), a condition decided only at h = 10⁻⁶, the bounds of [[prop:uc-dependence]] hold with
the gap and the count at h ([[thm:tr-transfer]]). The same holds for the smaller index sets of [[def:uc-choice]], with
the gap and the count that they give at h ([[thm:tr-flat]]).
```

*4. The last sentence of [[rem:ec-lb-unbounded]].*
(chapters/71-explicit-constants.md:1836–1837) Old:

```old
index sets, by d_NM > 2.0517·10¹⁰/μ(h), with the least excess μ(h) of [[def:tr-excess]] ([[thm:tr-transfer]]); as h
decreases to a point h_μ ∈ (5·10⁻⁷, 10⁻⁶), μ(h) tends to 0 and this bound to infinity ([[prop:tr-mu-small]]).
```

New:

```new
index sets, by d_NM > 2.0517·10¹⁰/μ(h), with the least excess μ(h) of [[def:tr-excess]] ([[thm:tr-transfer]]); as h
decreases to a point h_μ ∈ (5·10⁻⁷, 10⁻⁶), μ(h) tends to 0 and this bound to infinity ([[prop:tr-mu-small]]). For the
smaller index sets of [[def:is-flat-set]], which [[thm:uc-integer]] takes, [[prop:tr-flat-lower]] gives there
d_NM > 2.0517·10¹⁰/μ♭(h), with the least excess μ♭(h) ≥ μ(h) of [[def:tr-flat-excess]], and this bound too tends to
infinity, as h decreases to a point h♭ ∈ (5·10⁻⁷, 10⁻⁶).
```

*5. The opening of [[sec:tr]], first paragraph.*
(chapters/71-explicit-constants.md:5745–5748) Old:

```old
proved ([[rem:ec-point-outside]]). This section keeps the gauge parameters (γ_Υ, e_Υ) = (1/100, 1/100) and the index sets
as constructed ([[sec:is]]), and lets h run through [h_m, 10⁻⁶), h_m := 4.76·10⁻¹¹; this paper shows that the smaller
index sets of [[def:is-flat-set]], which [[thm:uc-integer]] takes, serve at the computational point
([[thm:is-flat-serves]]), and does not treat them at other h. In the proof of [[thm:uc-integer]], run with the index sets
```

New:

```new
proved ([[rem:ec-point-outside]]). This section keeps the gauge parameters (γ_Υ, e_Υ) = (1/100, 1/100) and lets h run
through [h_m, 10⁻⁶), h_m := 4.76·10⁻¹¹. Up to [[sec:tr-flat]] it takes the index sets as constructed ([[sec:is]]);
[[sec:tr-flat]] treats the smaller index sets of [[def:is-flat-set]], which [[thm:uc-integer]] takes and which serve at
the computational point ([[thm:is-flat-serves]]). In the proof of [[thm:uc-integer]], run with the index sets
```

*6. The opening of [[sec:tr]], end of the second paragraph.*
(chapters/71-explicit-constants.md:5778–5779) Old:

```old
(40/13)h(1 − 5·10⁴h) < ι₂(h) − 2 < 40h/13 ([[lem:ec-lb-ind]]): below 13ε_Υ/40 = 4.751175·10⁻¹¹ no h satisfies (H_ε)
([[prop:tr-eps]] (b)).
```

New:

```new
(40/13)h(1 − 5·10⁴h) < ι₂(h) − 2 < 40h/13 ([[lem:ec-lb-ind]]): below 13ε_Υ/40 = 4.751175·10⁻¹¹ no h satisfies (H_ε)
([[prop:tr-eps]] (b)). With the smaller index sets the same five inputs enter, and (e) gives a least excess
μ♭(h) ≥ μ(h) in which only multiples of 𝔡₁ are added to the roots of real part below 3, and a bound for the count that
is linear in the numbers 3 − Re ι, below 1.33738·10⁹ + 4.0697·10⁶h^(−1/2). The upper bound becomes the bound of
[[prop:uc-dependence]] at these, under the same conditions, and the lower bound d_NM > 2.0517·10¹⁰/μ♭(h) tends to
infinity as h decreases to a point h♭ ∈ (5·10⁻⁷, 10⁻⁶) ([[sec:tr-flat]]).
```

*7. The last sentence of [[rem:tr-scope]].*
(chapters/71-explicit-constants.md:5846–5849) Old:

```old
admissible choice ([[prop:tr-fail]]). The lower bounds of (ii) use only admissibility, and, like [[prop:tr-mu-small]],
which uses 𝔡₀ as an increment, they are proved for the index sets as constructed; for the smaller index sets of
[[def:is-flat-set]], which [[thm:uc-integer]] takes, this paper proves [[thm:is-flat-serves]] at the computational point
only.
```

New:

```new
admissible choice ([[prop:tr-fail]]). The lower bounds of (ii) use only admissibility, and, like [[prop:tr-mu-small]],
which uses 𝔡₀ as an increment, they are proved for the index sets as constructed; for the smaller index sets of
[[def:is-flat-set]], which [[thm:uc-integer]] takes, [[sec:tr-flat]] proves that they serve at these h and gives the
counterparts of (ii), (iii) and [[prop:tr-mu-small]], the sum 2541391𝔡₁ of increments taking the place of w_*
([[prop:tr-flat-serves]], [[thm:tr-flat]], [[prop:tr-flat-lower]]).
```

*8. The proof of [[thm:tr-transfer]] (iii), the end of its list of statements.*
(chapters/71-explicit-constants.md:6370–6371) Old:

```old
[[prop:tr-lambda]] (a) gives, and 𝒵 ⊂ {Re > 1}, which holds at every h ([[prop:iii-f1-2-3]] (a)). So the proof of
[[prop:uc-dependence]] applies at h, with the index sets as constructed, N̄_Λ := N̄(h), k̄_0 = 3, J_* = 15,000,015 and
```

New:

```new
[[prop:tr-lambda]] (a) gives, and 𝒵 ⊂ {Re > 1}, which holds at every h ([[prop:iii-f1-2-3]] (a)). The statements
[[def:is-flat-set]]–[[cor:is-flat]] on the smaller index sets enter only the run with those index sets, in which
[[cor:is-flat]], which depends on h through Z₃, is replaced by [[prop:tr-flat-lambda]] ([[thm:tr-flat]]). So the proof of
[[prop:uc-dependence]] applies at h, with the index sets as constructed, N̄_Λ := N̄(h), k̄_0 = 3, J_* = 15,000,015 and
```

*9. The statement of [[prop:tr-mu-small]], its last sentence.*
(chapters/71-explicit-constants.md:6431–6432) Old:

```old
at every h ∈ (h_μ, h_μ + δ) at which the parameter point (h, 1/100, 1/100) is admissible, every admissible choice of the
weights gives d_NM > D.
```

New:

```new
at every h ∈ (h_μ, h_μ + δ) at which the parameter point (h, 1/100, 1/100) is admissible, every admissible choice of the
weights with the index sets as constructed gives d_NM > D.
```

*10. The item on the constants of [[thm:settling]].*
(chapters/03-theorems.md:366–367) Old:

```old
  bounds under a condition decided only at γ_C = 10⁶ ([[thm:tr-transfer]], [[prop:tr-mu-small]]); through the lower
  bounds, upper bounds for δ and for the
```

New:

```new
  bounds under a condition decided only at γ_C = 10⁶ ([[thm:tr-transfer]], [[prop:tr-mu-small]]), and the same for the
  smaller index sets of that choice ([[thm:tr-flat]], [[prop:tr-flat-lower]]); through the lower
  bounds, upper bounds for δ and for the
```

*11. The sentence on the other values of h.*
(chapters/90-scope.md:88–89) Old:

```old
the damping polynomials of large degree that is decided only at h = 10⁻⁶, and whether such points are admissible is not
decided ([[thm:tr-transfer]], [[prop:tr-mu-small]], [[rem:tr-scope]]). No result of [[ch:explicit-constants]] is used in
```

New:

```new
the damping polynomials of large degree that is decided only at h = 10⁻⁶, and whether such points are admissible is not
decided ([[thm:tr-transfer]], [[prop:tr-mu-small]], [[rem:tr-scope]]). For the smaller index sets of the choice above,
which serve at these h as well, the same holds with the least excess μ♭(h) ≥ μ(h) that they give in place of μ(h) and
with some h♭ ∈ (5 × 10⁻⁷, 10⁻⁶) in place of h_μ ([[thm:tr-flat]], [[prop:tr-flat-lower]]).
No result of [[ch:explicit-constants]] is used in
```

*12. Nothing else changes.* No existing label is renamed or removed, and no number already printed
changes (see the notes).

### Notes

Not chapter text.

*1. What is proved, and where the extension of thm:is-flat-serves stops.*

- The first part of thm:is-flat-serves holds at every h ∈ (0, 10⁻⁶] (prop:tr-flat-serves (a)): the memberships, Λ^φ ⊂ Λ,
  the increments, η_0 = 𝔡₁ and J_* = 15,000,015.
- k̄_0 = 3 and l_* = 50 hold at every h ∈ [h_m, 10⁻⁶) ∖ 𝖩 (prop:tr-flat-serves (b)).
- So nothing fails on [h_m, 10⁻⁶) ∖ 𝖩. On 𝖩, and below h_m, the proof of (b) is not available, because it goes through
  prop:tr-inputs, which needs (H_ε) and the simplicity of the roots. That is exactly the restriction of
  thm:tr-transfer for the index sets as constructed; the smaller index sets add none.
- The record of every input, for h:
  - def:is-flat-set: the constructions (c1)–(c6), lem:iii-a-1-4, lem:iii-a-1-5, lem:is-typed and the projections
    ½(1 ± φ) do not involve h. □^Υ_b = 2δ_(g,E_Υ)Gδ*_g (eq:iii-b-6-4) carries E_Υ, not E_C; its roots, R, 𝔡₀, 𝔡₁, δ′₁
    and δ₂ are fixed by z; the weights lie in [0, 2 + 𝔡₁), where E(α) = R + ℕ₀.
  - The parity: (P3) of lem:iii-i15-1-1 states that x ↦ −x preserves c_C as well, so it commutes with P_b and L̂_b(0)
    at every γ_C.
  - The removed pairs (rotation corrections and ω̇_b(0, ·) at 2 + 𝔡₀ + ℕ₀): lem:is-rot-s0, def:is-cb, thm:is-d0 and
    rem:is-cb-open concern objects fixed by g_b, □^Υ_b and their decay; E_C does not enter. No h.
  - ℰ^(ι,φ)_ind: h enters only through the physical states of prop:iii-f4-5-1, built from the roots of L̂_b(0).
    (C1) holds on (0, 10⁻⁶] (lem:iv4-1-3 (a)). By the proof of prop:is-iota, which uses only (C1), these states add
    integers and the numbers ι + 1 + j with Re > 3 (prop:np-10-54 (ii)). So below real part 3 nothing depends on h.
  - lem:is-flat-memberships (a), (b): no h. Its part (c): h enters only through ℰ^ι_ind as constructed at h, whose
    exponents below 3 are those of ℰ_ind and integers at every h.
  - lem:is-flat-uses: a statement about how the proofs use the memberships; no h.
  - thm:is-flat-serves: memberships, Λ^φ ⊂ Λ, increments, η_0 and J_* follow from the above. k̄_0 and l_* go through
    the orders and multiplicities of prop:tr-inputs (a), (b), (d), and so need h ∈ [h_m, 10⁻⁶) ∖ 𝖩.
  - cor:is-flat: depends on h through Z₃(h). It is replaced at h by prop:tr-flat-lambda. Its part on Λ_ℬ does not
    depend on h; prop:tr-flat-lambda (a) proves that part again, with the description of Λ^φ_ℬ below 3 + δ₂.
- The earlier review's assessment ("□^Υ_b does not involve h; the physical states have offsets ≥ 1") is confirmed,
  with two refinements:
  - what is used is that the h-dependent exponents of the physical states have real part above 3 at every h, so that
    nothing below 3/2 moves;
  - l_* = 50 does involve h, through the simplicity and (H_ε) of prop:tr-inputs, and holds only off 𝖩 for h ≥ h_m.

*2. The reviewer's two formulas, checked against the definitions.*

- μ♭(h) := min({μ♭} ∪ {(⌊y_ι/𝔡₁⌋ + 1)𝔡₁ − y_ι : ι ∈ Z₃(h)}).
  - It is the gap: prop:tr-flat-lambda (b) proves that (G) holds for Λ^φ exactly when ε_K < μ♭(h), for 0 < ε_K < ε_Υ.
  - The third window of (G) (λ + 𝔡₀ near 2) is not contained in the first for Λ^φ, since 𝔡₀ is not an increment. It
    is checked directly: on Λ^φ_ℬ the least excess there is m♭(0.4901 − 𝔡₀) > 2.446·10⁻⁷; off Λ^φ_ℬ, λ + 𝔡₀ > 2 + 𝔡₀.
  - μ♭(h) ≥ μ(h) is proved directly: m(y) ≤ m♭(y) and μ_G < μ♭. It does not rest only on Λ^φ ⊂ Λ.
- N_Λ ≤ 59,377,257 + Σ_(ι∈Z₃(h))(⌊(y_ι + ε_+)/𝔡₁⌋ + 1).
  - Correct for 0 < ε_+ < ε_Υ (prop:tr-flat-lambda (c)). The term 59,377,257 needs ε_+ < μ♭, which ε_Υ < μ♭ gives.
  - For ε_+ < μ♭(h) the sum equals N̄♭(h) := 59,377,257 + Σ(⌊y_ι/𝔡₁⌋ + 1), which does not depend on ε_+. The theorem
    uses this form, as the analogue of N̄(h).
  - 59,377,257: the sum of ⌊(3 − β)/𝔡₁⌋ + 1 over the 30 numbers β < 3 of ℬ♭ is 59,377,256, plus 1 for β = 3. Without
    λ_♯ + 1 + δ′₁ and λ_♯ + 1 + δ₂ the sum is 56,436,656, as in the proof of cor:is-flat.
- The explicit bound N̄♭(h) < 1.33738·10⁹ + 4.0697·10⁶h^(−1/2) is new. It uses Σ y_ι < 426 + 1.356537h^(−1/2), proved
  as lem:tr-z3 (b) proves its bound for Σ y_ι², with the linear functions f_B, f_P in place of g_B, g_P.

*3. One condition the sketch does not show: ε_+ < ε_Υ.*

- In thm:tr-transfer (iii) it follows from ε_+ < μ(h) ≤ μ_G < ε_Υ. For the smaller index sets μ♭(h) may exceed ε_Υ, so
  thm:tr-flat asks 0 < ε_K < ε_+ < min(μ♭(h), ε_Υ) and ε_K < 0.998ε_Υ.
- It is used twice:
  - for the description of Λ^φ below 3 + ε_+: an element of Z₃(h) plus 1 has real part above 3 + 1.4646·10⁻¹⁰, and
    ε_Υ = 1.4619·10⁻¹⁰;
  - for ε_+ < ε_ind(h) in eq:iii-i9-1-1, where only ε_ind(h) ≥ ε_Υ is known.
- The cap on ε_K is the relaxed one of P-UB3, ε_K < 0.998ε_Υ; ε_K < min(μ♭(h), 0.998ε_Υ) as the brief asks.

*4. An addition beyond the brief: prop:tr-flat-lower.*

- The sentence "prop:tr-mu-small does not transfer to Λ^φ" is true as written, since w_* uses 𝔡₀. Its conclusion
  does transfer, with another sum of increments.
  - At h = 10⁻⁶ the root ι_* of P_390 has 2541391𝔡₁ − y_(ι_*) ∈ (1.3537368·10⁻⁷, 1.3537369·10⁻⁷).
  - The continuity argument of prop:tr-mu-small then gives h♭ ∈ (5·10⁻⁷, 10⁻⁶) with μ♭(h) → 0 as h decreases to h♭.
- Without it, the scope sentences would suggest that the smaller index sets avoid the unbounded lower bound near some
  h, which is false. prop:tr-flat-lower is proved in full, and the scope sentences cite it.
- In summaries the weaker form d_NM > 2.0517·10¹⁰/μ♭(h) is used. It holds at every admissible h, since the proved
  bound is 2.0517·10¹⁰/min(μ♭(h), ε_Υ).
- h♭ is not compared with h_μ. Since w_* = 2541390𝔡₁ + 356327ε₀ < 2541391𝔡₁, ι_B(390, h♭) < ι_B(390, h_μ). But the
  monotonicity of ι_B(390, ·) at x ≈ 0.15 is not proved, so no order of h♭ and h_μ is stated.

*5. The scope sites.*

- The sites the earlier review listed:
  - sec:tr opening, first paragraph: "and does not treat them at other h" becomes false. Replaced (item 5).
  - sec:tr opening, the paragraph on input (e): true, as it describes the route for the index sets as constructed. A
    sentence on the smaller index sets is added (item 6).
  - sec:tr-proof (iii), the list of h-independent statements: true for the run with the index sets as constructed,
    which does not use def:is-flat-set–cor:is-flat. One sentence added to say so (item 8); the h-record those
    statements need is prop:tr-flat-serves, and cor:is-flat is replaced by prop:tr-flat-lambda.
  - rem:tr-scope: its last sentence ("this paper proves thm:is-flat-serves at the computational point only") becomes
    false. Replaced (item 7). "Its bound is a number only once μ(h) is known" and "N̄(10⁻⁶) ≤ 909,507,124,095,312"
    concern (iii) for the index sets as constructed and stay true; the counterparts are in rem:tr-flat-scope.
  - Chapter 71 opening, lines 30–37: scoped ("for the index sets as the proofs construct them") and true. One
    sentence added (item 2).
  - rem:ec-lb-unbounded, last sentence: scoped ("for the same index sets") and true. One sentence added (item 4).
  - chapters/03-theorems.md, near "lower bounds that are unbounded near some γ_C": scoped and true. A clause added
    (item 10).
  - chapters/90-scope.md, near "d > 2.0517 × 10¹⁰/μ(h)": scoped and true. One sentence added (item 11).
- Two sites outside that list:
  - prop:tr-mu-small, its last sentence: "every admissible choice of the weights gives d_NM > D" reads as covering
    every choice of index sets. Near h_μ, μ♭(h) is not known to be small, so for the smaller index sets this is not
    proved. Qualified by "with the index sets as constructed" (item 9).
  - rem:ec-point-outside, last sentence: true and scoped. One sentence added (item 3).
- Checked and left as they are:
  - thm:tr-transfer (ii) and the paragraph after the theorem: scoped by "Take … the index sets as constructed".
  - The paragraph after prop:tr-mu-small: it speaks of p𝔡₀ + q𝔡₁ for the index sets as constructed. The counterpart
    with q𝔡₁ alone is in rem:tr-flat-scope.
  - prop:tr-fail: rests on ε_ind(h) only, and holds for every choice of index sets.
  - thm:loss-d's last paragraph, rem:is-summary, thm:uc-reduction, sec:uc-close and rem:uc-offset-d0: all at the
    computational point.
  - rem:uc-data-order-limits ("except at the points of thm:tr-transfer (iii), if there are any"): the h of thm:tr-flat
    are the same points.
  - def:tr-excess, lem:tr-z3 and prop:tr-lambda: as constructed, or free of index sets.

*6. Numbers.*

- No number already printed changes. Every number of each old text occurs unchanged in its new text; this was checked
  mechanically over the eleven pairs, and the existing chapter text outside them is untouched.
- The new numbers were recomputed with exact rational arithmetic, from the bounds of lem:is-offsets (b) and the rows
  of sec:tab-is:
  - Σ_(ι∈Z₃)(⌊y_ι/𝔡₁⌋ + 1) = 3,623,813,354, over the 1269 + 680 rows, a non-real row twice; the non-real part is
    1,227,124,256. Every floor is determined at both ends of its interval.
  - N̄♭(10⁻⁶) = 3,683,190,611, as in cor:is-flat.
  - The least m♭(y_ι) over Z₃ lies in (3.5481255635·10⁻¹⁰, 3.5481255636·10⁻¹⁰), at l = 700; the next is 4.24068·10⁻¹⁰,
    at l = 869 (cor:is-flat: μ♭_Z, and "above 4.2406·10⁻¹⁰").
  - On ℬ♭: μ♭ = 5.01913624·10⁻⁸ at β = λ_♯; the next is 1.388886·10⁻⁷ (β = 2); near 2, m♭(0.4901) = 2.446358·10⁻⁷
    and m♭(0.4901 − 𝔡₀) = 2.446364·10⁻⁷; y/𝔡₁ = 1470297.26609 and 1470293.26609 at 0.4901 − 𝔡₀ and 0.4901 − 2𝔡₀.
  - The n⁺ column of the table of thm:is-gap was reproduced row by row; with 1470297 and 1470293 the sum is 59,377,256.
  - 2541391𝔡₁ < 0.84712961.
  - ½∫f_B x^(−1/2) dx = 0.72854612… and ½∫f_P x^(−1/2) dx = ½(11/15)^(3/2) = 0.31399457…, in closed form. The same
    method gives the constants of lem:tr-z3 (b): 0.6262456 < 0.626246 and 0.1381576 < 0.138158.
  - 1/𝔡₁ < 3,000,002.583334; 426/𝔡₁ < 1,278,001,100.51; 3,000,002.5834 · 1.356537 = 4,069,614.5045.
  - The bound of prop:tr-flat-lambda (c) is 5.40708·10⁹ at h = 10⁻⁶ and 5.91211·10¹¹ at h_m (h_m^(−1/2) = 144,942.76).
  - 3ε_Υ + 2δ̂ + δ̄ = 2.01447·10⁻⁸; 3(1 − 2.02·10⁻⁸)/δ̂ = 2.0517871·10¹⁰; 21 · 2.0517·10¹⁰ = 4.30857·10¹¹.

*7. Checks.*

- Scratch trees were made by git archive of paper/reader, at HEAD and at aa181269:
  - /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/ptrf/ (HEAD);
  - …/scratchpad/reader/ptrf_work/tree_aa181269/.
- HEAD moved past aa181269 while this file was written (to 40140118, then 9a43974b, both outside chapters 71, 03 and
  90). The three chapters and the crosswalk touched here are byte-identical at all three commits.
- A script applied the Placement and the crosswalk rows by parsing this file. Every old text matched exactly once,
  and the new subsection went in at item 1.
- From each paper/reader root:
  - lint.py --chapters: 0 hits;
  - assemble.py --check: 0 problems;
  - the assembled-paper command prints [] 0.
- Crosswalk: each of the 287 labels of chapter 71 has exactly one row, and the rows are in chapter order.
- Every new line has at most 121 characters, also with the labels resolved. No continuation line starts with a
  Markdown marker.

### Crosswalk rows

Rows for crosswalk/71-explicit-constants.tsv, in its four columns, separated by tabs, in chapter order; they go
directly after the row of prop:tr-mu-small. The line numbers are those of this file:
    sec:tr-flat	paper/reader/proofs/P-TRF.md@PENDING:1	P-TRF, subsection heading	new; at the end of sec:tr, after the paragraph that follows prop:tr-mu-small; the smaller index sets ℰ^φ_ind, ℰ^(ι,φ)_ind at h ∈ [4.76·10⁻¹¹, 10⁻⁶)
    prop:tr-flat-serves	paper/reader/proofs/P-TRF.md@PENDING:15	P-TRF, Proposition (The smaller index sets at h.)	new: thm:is-flat-serves at every h ∈ (0, 10⁻⁶] (memberships, Λ^φ ⊂ Λ, increments, η_0, J_*), with k̄_0 = 3 and l_* = 50 off 𝖩 for h ≥ h_m; each input checked for h: □^Υ_b, the parity, c_b and ω̇_b(0, ·) do not involve h, the physical states add only exponents of real part > 3
    def:tr-flat-excess	paper/reader/proofs/P-TRF.md@PENDING:93	P-TRF, Definition (The least excess for the smaller index sets.)	new: m♭(y) = (⌊y/𝔡₁⌋ + 1)𝔡₁ − y, μ♭(h) = min({μ♭} ∪ {m♭(y_ι)}), N̄♭(h) = 59,377,257 + Σ(⌊y_ι/𝔡₁⌋ + 1); μ(h) ≤ μ♭(h) ≤ μ♭; at h = 10⁻⁶ they are μ♭_Z and 3,683,190,611
    prop:tr-flat-lambda	paper/reader/proofs/P-TRF.md@PENDING:104	P-TRF, Proposition (The set Λ^φ at h.)	new: prop:tr-lambda for Λ^φ: the part Λ^φ_ℬ below 3 + δ₂ is {β + q𝔡₁}, 31 numbers β, h-independent, least excess μ♭; (G) iff ε_K < μ♭(h), (G⁺) iff ε_+ < μ♭(h) for ε_K, ε_+ < ε_Υ; N_Λ ≤ 59,377,257 + Σ(⌊(y_ι + ε_+)/𝔡₁⌋ + 1); N̄♭(h) < 1.33738·10⁹ + 4.0697·10⁶h^(−1/2)
    thm:tr-flat	paper/reader/proofs/P-TRF.md@PENDING:199	P-TRF, Theorem (The bounds at other values of h for the smaller index sets.)	new: thm:tr-transfer (iii) with ℰ^φ_ind, ℰ^(ι,φ)_ind for 0 < ε_K < ε_+ < min(μ♭(h), ε_Υ), ε_K < 0.998ε_Υ, at N̄_Λ = N̄♭(h), k̄_0 = 3, J_* = 15,000,015, l_* = 50; at h = 10⁻⁶ it gives thm:uc-integer: N_Λ ≤ 3,683,190,611, d_NM < 1.42556·10³⁸, K < 3.13622·10³⁹
    prop:tr-flat-lower	paper/reader/proofs/P-TRF.md@PENDING:247	P-TRF, Proposition (Lower bounds for the smaller index sets.)	new: ε_K < μ♭(h), d_NM > 2.0517·10¹⁰/min(μ♭(h), ε_Υ) at every admissible h ≤ 10⁻⁶; μ♭(h) → 0 as h decreases to some h♭ ∈ (5·10⁻⁷, 10⁻⁶), through ι_B(390, h) + 2541391𝔡₁
    rem:tr-flat-scope	paper/reader/proofs/P-TRF.md@PENDING:280	P-TRF, Remark (What the bounds for the smaller index sets assume.)	admissibility, (R_h) and μ♭(h) decided or evaluated only at h = 10⁻⁶; N̄♭(h) < 5.913·10¹¹ < N̄(h), so the bound is at most that of thm:tr-transfer (iii) at every ε_K, ε_+ that it admits
