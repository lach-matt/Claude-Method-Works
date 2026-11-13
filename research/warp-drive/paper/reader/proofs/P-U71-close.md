### The inputs of the upper bound for d {#sec:uc-close}

This section takes the inputs that [[prop:ec-upper]] leaves free and decides, for each, whether this paper determines
it. Two are determined. The loss of the inverse of the transition face model is 1 at every weight at which the
construction uses it, so ℓ_tf = 1 ([[prop:uc-ltf]]); and the order of the background terms may be taken to be
d_BG = 11 ([[prop:uc-dbg]]). The others are not: the admissible ε_K of the gap condition (G), the counts n(E, β) of
the index sets entering the Fourier steps of the levels ([[lem:uc-fourier-count]]), and the loss of the map Φ of
[[thm:iii-j-2-4]], which governs the two other components of d_NM ([[lem:uc-phi-loss]]), are fixed by the index sets
that define the set Λ of [[def:iii-i10-1-1]], and this paper specifies those index sets by their least real parts
only. From its statements no positive number is an admissible ε_K ([[prop:uc-no-eps]]), and if both offsets of the class
roots are increments of Λ, every admissible ε_K lies below 1.6417·10⁻¹⁴ ([[cor:uc-two-offsets]]). Consequently the
statements of this paper bound d from below and not from above ([[thm:uc-reduction]]); [[rem:uc-missing]] states the
one statement that an integer upper bound needs. Throughout we work at the computational point of [[def:ec-point]], so
z = 4·10⁻⁶ = 1/250000 and λ_♯ = 15099/10000, and 𝔡₀ = d_c0, 𝔡₁ = d_c1 are the offsets of [[sec:ec-gap-sums]].

#### The index sets of the gap condition {#sec:uc-index-sets}

The gap condition (G) of [[def:iii-i10-1-3]] quantifies over the set Λ and over the offsets 𝔡₀ and 𝔡₁ of the two class
roots ([[def:iii-i9-gap]]). By [[def:iii-i10-1-1]], Λ is the smallest set, closed under conjugation, that contains the
generators

- π_1ℰ_++, with ℰ_++ the least index set of [[eq:iii-i8-1-1]]: the closure of ℰ^♯_+ ∩ {Re < 2} under the addition of
  ℰ^ι_ind ∪ ℰ_ind ∪ ℰ_+, where ℰ^♯_+ is the set [[eq:iii-i1-3-2]] of [[prop:iii-i1-3-1]] with Ĕ_+ = ∅
  ([[sec:iii-i8-1]]);
- π_1𝒢, with 𝒢 = (2, 0) ∪ (2 + ℰ_ind) ([[eq:iii-i7-1-1]]);
- π_1ℰ^C_I, the index set at 𝓘⁺ of the class, subject to (2)–(3) of [[def:iii-c-3-1]] ([[def:iii-i-1-1]]);
- λ_♯ and 3;
- 2 + π_1ℰ_col, with ℰ_col = ({(0, 0), (1, 0)} ∪ ℰ_ind ∪ (1 + ℰ_ind)) + ℕ₀ ([[lem:iii-i11-1-1]]), a subset of
  π_1𝒢 + ℕ₀;

and that is closed under the addition of the increments

- π_1ℰ_ind, where ℰ_ind is the union of the index sets of [[prop:iii-d2-3-1]] and [[prop:iii-f3-2-2]]
  ([[sec:iii-i7-1]]), of [[prop:iii-d3-3-1]] (2) ([[sec:iii-i8-1]]), and of [[prop:iii-d3-3-1]] (1), (3), (4)–(7)
  and (2, 0) ([[sec:iii-i9-1]]), taken at b₀ and serving at every b near b₀ ((P3) of [[lem:iii-i15-1-1]]);
- π_1ℰ^ι_ind, the index set of [[thm:iii-g2-4-2]] ([[eq:iii-g2-4-4]]);
- 1.

Each of these sets enters the statements of this paper only through memberships of the form u ∈ 𝒜^E (or a partially
polyhomogeneous space with the index set E) and through a lower bound for its real parts: [[sec:iii-d2-1]] lets ℰ_ind
denote an index set with min Re ℰ_ind ≥ ε_Υ which may change from line to line, [[thm:iii-g2-4-2]] asserts ℰ^ι_ind with
min Re ℰ^ι_ind > 0, and [[def:iii-c-3-1]] constrains ℰ^C_I by a lower bound and a closure property. A space with an
index set E is contained in the space with any index set E′ ⊃ E, the coefficients at the added exponents being 0.

**Proposition {#prop:uc-no-eps}** (The statements fix no admissible ε_K.) Let t > 0 and

    E_t := ℰ_ind ∪ {(3 − λ_♯ + t + j, 0) : j ∈ ℕ₀}.

Then E_t is an index set with min Re E_t ≥ ε_Υ, every membership that [[prop:iii-d2-3-1]], [[prop:iii-d3-3-1]],
[[prop:iii-f3-2-2]] and [[thm:iii-g2-4-2]] assert with ℰ_ind holds with E_t in its place, and for the set Λ_t that
[[def:iii-i10-1-1]] builds from E_t, (G) fails for every ε_K ≥ t. So no positive number can be shown to be an admissible
ε_K from information about ℰ_ind that consists of such memberships and of the bound min Re ℰ_ind ≥ ε_Υ; the exponents
of ℰ_ind themselves are needed.

*Proof.* E_t is a union of two index sets, so it has finitely many exponents below each bound, finitely many
logarithms at each, and is closed under (z, k) ↦ (z + 1, k); its new exponents have real part at least
3 − λ_♯ = 1.4901 > ε_Υ. A membership with ℰ_ind implies the same membership with E_t ⊃ ℰ_ind. In Λ_t, λ_♯ is a
generator and 3 − λ_♯ + t ∈ π_1E_t is an increment, so 3 + t ∈ Λ_t. Its real part lies in (3, 3 + ε_K] as soon as
ε_K ≥ t, which (G) excludes. ∎

The same enlargement, by any finite set of exponents of real part at least ε_Υ, with any logarithmic orders, raises the
number of points of Λ below 3 + ε_+ and the bounds l_* and k̄_0 of [[def:iii-i10-1-1]] (the latter through 𝒢) beyond
any given bound; so the statements do not bound these numbers either.

**Lemma {#lem:uc-two-offsets}** (Two class offsets near 3.) Let a := 1,109,655 and b := 31,682. Then

    1.6415·10⁻¹⁴ < λ_♯ + a𝔡₀ + b𝔡₁ − 3 < 1.6417·10⁻¹⁴.                                               {#eq:uc-two-offsets}

*Proof.* *The offsets.* 𝔡₀ = (9/4 + z)^(1/2) − 3/2 ([[sec:ec-gap-sums]]), and 9/4 + z = 562501/250000, so
𝔡₀ = (√562501 − 750)/500. By [[lem:iii-d-4-1]] and its proof, ι^Υ_(s1,2) = ½ + (¼ + s_(1,1))^(1/2), where s_(1,1) is
the smaller root of Q_1(s) = s² − (8 + z)s + 12 + 3z (κ = 3), whose discriminant is 16 + 4z + z² = D/250000² with
D := 1000001000001. So 4(¼ + s_(1,1)) = 17 + 2z − √D/125000 =: I, ι^Υ_(s1,2) = ½ + ½√I, and 𝔡₁ = (√I − 3)/2.

*The square roots.* Squaring the decimal numbers below gives

    750.0006666663703706337445² = 562500.99999999999999999990500…,
    750.0006666663703706337446² = 562501.00000000000000000005500…,
    1000000.500000374999812500² = 1000001000000.99999999999995312…,
    1000000.500000374999812501² = 1000001000001.00000000000195312…,

so √562501 and √D lie strictly between the two numbers squared. With 2z = 0.000008 and
1000000.500000374999812500/125000 = 8.0000040000029999985, the second pair gives

    9.000003999997000001499992 < I < 9.0000039999970000015,

and, as 3.0000006666660925929701631² = 9.00000399999700000149999177…, which is below the lower bound for I, and
3.0000006666660925929701645² = 9.00000399999700000150000017…, which is above the upper one, √I lies strictly between
3.0000006666660925929701631 and 3.0000006666660925929701645.

*The sum.* Hence

    1.333332740741267489·10⁻⁶ < 𝔡₀ < 1.3333327407412674892·10⁻⁶,
    3.3333304629648508155·10⁻⁷ < 𝔡₁ < 3.3333304629648508225·10⁻⁷,

and, multiplying the four bounds exactly,

    1.479539342427251175506295 < a𝔡₀ < 1.479539342427251175728226,
    0.0105606575727652403536671 < b𝔡₁ < 0.0105606575727652403758445.

Adding, a𝔡₀ + b𝔡₁ − 1.4901 lies between 1.64158599…·10⁻¹⁴ and 1.64161040…·10⁻¹⁴. As 3 − λ_♯ = 1.4901, this is
[[eq:uc-two-offsets]]. (Also a𝔡₀ + (b − 1)𝔡₁ < 1.4901, by 𝔡₁ > 3.3·10⁻⁷, so b is the least integer that works with
this a.) ∎

**Corollary {#cor:uc-two-offsets}** (The gap condition when both offsets are increments.) Suppose that 𝔡₀ and 𝔡₁ lie in
π_1(ℰ_ind ∪ ℰ^ι_ind). Then every ε_K with which (G) holds satisfies ε_K < 1.6417·10⁻¹⁴; in particular (G) does not hold
at ε_K = 1.46·10⁻¹⁰, the value assumed in [[rem:ec-upper-point]]. For every admissible choice of the weights, the
number R of [[prop:ec-rounds]] then satisfies R > 4.1659·10²³, so that d_NM ≥ d_acc > 1.2497·10²⁴ and
N_NM = 21d_NM + 6 > 2.624·10²⁵.

*Proof.* λ := λ_♯ + a𝔡₀ + b𝔡₁, with a and b of [[lem:uc-two-offsets]], is obtained from the generator λ_♯ by a + b
additions of increments, so λ ∈ Λ, and Re λ − 3 < 1.6417·10⁻¹⁴ by [[eq:uc-two-offsets]]. If ε_K ≥ 1.6417·10⁻¹⁴, then
Re λ ∈ (3, 3 + ε_K], against (G). By [[prop:ec-rounds]], R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂) with δ̂ = 1.46214·10⁻¹⁰ and
δ̄ = 1.94137057·10⁻⁸, and the right side decreases in ε_K. At ε_K = 1.6417·10⁻¹⁴ the numerator exceeds
1 − 1.98·10⁻⁸ > 0.99999998 and ε_Kδ̂ = 2.400395…·10⁻²⁴ < 2.4004·10⁻²⁴, so R > 4.16597·10²³. By [[thm:loss-d]] (ii),
d_NM ≥ d_acc ≥ 3R > 1.2497·10²⁴, and 21 · 1.2497·10²⁴ > 2.624·10²⁵. ∎

**Remark {#rem:uc-offset-d0}** (The offset 𝔡₀ as an increment.) [[rem:gap-sums]] lets 𝔡₀ enter Λ through the increment
1 + 𝔡₀ only, and [[prop:gap-sums]] shows that the windows of (G) are then not met by the sums it considers for
ε_K < 5.019·10⁻⁸. Whether 𝔡₀ itself is an exponent of ℰ_ind ∪ ℰ^ι_ind is not decided by the statements of this
paper. The root ι^Υ_(s0,2) = 2 + 𝔡₀ of (□^Υ_b)^(0) lies above the weights in (0, ι^Υ_(s1,2)) at which
[[prop:iii-d2-3-1]] solves for the corrections of the states, and these corrections start at the order (2, 0), so a
term at that root would contribute the exponent 𝔡₀ to ℰ_ind. At b₀ the operator commutes with the rotations, and the
corrections of the states of types s1 and v1 do not meet the roots of type s0. At a rotating b the metric couples the
angular types at the order |x|⁻³ ([[eq:iii-d2-2-2]]), and ℰ_ind is one index set serving at every b near b₀. So
[[cor:uc-two-offsets]] is a case that a proof of (G) at an explicit ε_K has to settle, by computing these coefficients
or by admitting 𝔡₀.

#### The loss of the inverse of the transition face model {#sec:uc-ltf}

**Lemma {#lem:uc-spec-as}** (The endomorphism of the incoming threshold.) Let A + S be the endomorphism of
[[eq:ec-theta-in-l]]. At every point of ∂X its characteristic polynomial on the fibre of S²T* is

    ν⁵ (ν − (1 + v_C)γ_C)³ (ν − 2(1 + v_C)γ_C) (ν − (1 − e_C)(1 + v_C)γ_C)
       · (ν − γ_Υ)³ (ν − 2γ_Υ) (ν − (1 − e_Υ)γ_Υ).                                                     {#eq:uc-spec-as}

In particular every eigenvalue of A + S is real and non-negative.

*Proof.* We follow the proof of [[lem:iii-f-3-1]], with the null covector ℓ := dt̄ + d|x| = ζ in place of dt_*. Put
Z := ḡ⁻¹ℓ and Y := ḡ⁻¹dt̄; then ℓ(Z) = 0, dt_*(Z) = ḡ⁻¹(dt̄ − d|x|, dt̄ + d|x|) = −2, ℓ(Y) = dt_*(Y) = −1, and
dt̄ = ½(ℓ + dt_*). Write c := c̄_C/ρ = ½(1 − v_C)ℓ + ½(1 + v_C)dt_* (the proof of [[lem:iii-f-3-1]]), so that
c(Z) = −(1 + v_C) and ⟨c, dt_*⟩ = −(1 − v_C). By [[eq:iii-b-6-5]], ρ⁻¹ḠĒ^Cω = γ_C(2c ⊗_s ω − e_C ḡ⟨c, ω⟩) and
ρ⁻¹Ē^ΥḠh = −γ_Υ(2ι_Y h − e_Υ dt̄ tr h). By [[eq:ec-theta-in-l]], A + S = UV with U := (U_1 U_2) : T* ⊕ T* → S²T*,
U_1 := −ρ⁻¹Ē^C, U_2 := ℓ ⊗_s ·, and V := (V_1; V_2), V_1 := ι_Z Ḡ, V_2 := ρ⁻¹Ē^ΥḠ. So det(ν − UV) = ν⁵ det(ν − VU).
Since ι_Z(ℓ ⊗_s ω) = ½ω(Z)ℓ, tr(ℓ ⊗_s ω) = ω(Z) and ι_Z ḡ = ℓ, V_1U_2 = 0, and det(ν − VU) = det(ν − V_1U_1)
det(ν − V_2U_2). Now

    V_1U_1ω = −γ_C ι_Z(2c ⊗_s ω − e_C ḡ⟨c, ω⟩) = γ_C((1 + v_C)ω − ω(Z)c + e_C⟨c, ω⟩ℓ),
    V_2U_2η = −γ_Υ(ℓ(Y)η + η(Y)ℓ − e_Υ η(Z) dt̄) = γ_Υ(η − η(Y)ℓ + e_Υ η(Z) dt̄).

On angular covectors (annihilated by Z and Y) both are multiplication by (1 + v_C)γ_C, resp. γ_Υ. On ℓ:
V_1U_1ℓ = γ_C(1 + v_C − e_C(1 + v_C))ℓ = (1 − e_C)(1 + v_C)γ_Cℓ and V_2U_2ℓ = 2γ_Υℓ. On dt_*:
V_1U_1dt_* = γ_C((1 + v_C)dt_* + 2c − e_C(1 − v_C)ℓ) = γ_C(2(1 + v_C)dt_* + (1 − e_C)(1 − v_C)ℓ) and
V_2U_2dt_* = γ_Υ(dt_* + ℓ − 2e_Υdt̄) = (1 − e_Υ)γ_Υ(dt_* + ℓ). Both maps are triangular in the bases (angular, ℓ, dt_*),
with the diagonals that give [[eq:uc-spec-as]]. As γ_C, γ_Υ > 0, v_C ∈ (0, 1) and e_C, e_Υ ∈ (0, 1), the roots are
real and non-negative. By the homogeneity of [[lem:ec-theta-in]] (b) the same holds at every point of ∂X. ∎

**Lemma {#lem:uc-theta-in}** (An inner product with a small incoming threshold.) For every δ > 0 there is a smooth
fibre inner product h on S²T* over ∂X with Re h((A + S)u, u) > −δ h(u, u) for all u ≠ 0. For it, the incoming
threshold ϑ_in of (2L_b)^(σ), and that of N_tf((2L_b)^(·), ±1), satisfies ϑ_in < 2δ.

*Proof.* At a point ω ∈ ∂X, by [[lem:uc-spec-as]] the matrix of A + S in a Jordan basis has real non-negative diagonal
entries; rescaling the basis vectors makes its off-diagonal entries at most δ/2 in modulus. For the inner product h_ω
in which this basis is orthonormal, Re h_ω((A + S)u, u) ≥ −(δ/2)h_ω(u, u). The strict inequality
Re h((A + S + δ)u, u) > 0 for u ≠ 0 persists at the points near ω, and it is preserved by convex combinations of inner
products; a partition of unity on ∂X glues the h_ω, as in the proof of [[cor:iii-f1-3-4]] for S̄. By [[eq:ec-theta-in]],
p_in − (S + S^(∗h)) = −2Re_h(A + S), whose eigenvalues are then below 2δ at every point; ∂X is compact, so the
supremum ϑ_in is below 2δ. For N_tf the endomorphism A + S is the same, and (a) of [[lem:ec-theta-in]] applies with
ρ̂ for ρ ((b) of that lemma). ∎

**Proposition {#prop:uc-ltf}** (The loss of [[cor:iii-f1-3-4]] is 1.) Let β_sctf ∈ [1, 3/2) and β_ztf ∈ [−1, 0). The
proof of [[cor:iii-f1-3-4]] runs with the regularity s := 1, the weight α_+ := 0, the incoming order 𝗋_in := −¼ and, at
the incoming radial sets, the inner product of [[lem:uc-theta-in]] with δ = 1/8, and gives [[eq:iii-f1-3-3]] with
ℓ = 1, for every k ∈ ℕ₀ and every ϵ ∈ (0, ¼(3/2 − β_sctf)). So with these choices the loss of [[cor:iii-f1-3-4]] is 1,
which is the value of ℓ_tf in [[lem:ec-closed-forms]] (d), and its least possible value there. Every application of
[[cor:iii-f1-3-4]] in the construction of [[thm:iii-i14-3-1]] and of [[thm:iii-j1-2-1]] has β_sctf = 3/2 − ε with
0 < ε < ¼; so ℓ_tf = 1 at all of them, and in [[prop:ec-upper]] and [[lem:ec-round-charges]] ℓ_tf = 1.

*Proof.* *The regularity.* [[prop:iii-f1-3-3]] gives the tf-admissibility of L_b^(·) with every weight in (0, 1], in
particular with β := −β_ztf. By [[def:i-c-5-1]], tf-admissibility does not depend on the choices of s, α_+ and the
orders, and [[cor:i-c-5-2]] (a)–(b) holds with s and α_+ as in [[thm:i-c-4-3]], which takes s and α_+ in ℝ and uses
the order pair of [[lem:i-a-7-1]] only through its decay order at the boundary face of tf. The face tf carries no
event horizon, so the condition s > ½ + ϑ_ℋ that [[prop:iii-f1-3-3]] meets for the spectral families on X (whence its
"s large") does not enter the bound on tf. So [[eq:i-c-5-1]] holds at
s = 1 and α_+ = 0, and with [[thm:i-c-4-3]] (4) for k further b-derivatives, N_tf(±1)⁻¹ is bounded from
H^((s−2;k),(𝗋+1,q−2))_(sc,b;b) to H^((s;k),(𝗋,q))_(sc,b;b), as in the proof of [[cor:iii-f1-3-4]].

*The orders.* That proof takes δ_0 := ¼(3/2 − β_sctf) ∈ (0, 1/8], ϵ < δ_0, the outgoing order
𝗋_out := β_sctf − 2 − ϵ/2, and the orders 𝗋_± of [[lem:i-a-7-1]] at σ_* = ±1 with that outgoing value; it arranges
𝗋_out < −½ + S̄_L at R_out with an inner product there. [[lem:i-a-7-1]] also asks 𝗋_in > (−1 + ϑ_in)/2 − α_+ and
𝗋_in ≥ 𝗋_out, with ϑ_in in an inner product of our choice at the incoming radial sets ((O3) of [[sec:i-a-1-4]]). With
the inner product of [[lem:uc-theta-in]] at δ = 1/8, ϑ_in < 1/4, so (−1 + ϑ_in)/2 < −3/8 < −¼ = 𝗋_in; and
𝗋_out < −½ < 𝗋_in. The order of [[lem:i-a-7-1]] is 𝗋 = 𝗋_out + (𝗋_in − 𝗋_out)Θχ_c with 0 ≤ Θχ_c ≤ 1, equal to
𝗋_out near R_out and to 𝗋_in near the incoming radial sets; so inf 𝗋 = 𝗋_out and sup 𝗋 = 𝗋_in.

*The losses.* In [[lem:ii-g1-4-1]] at s = 1, ⌈(s − 1)_+⌉ = ⌈(−s)_+⌉ = 0, so ℓ = ⌈sup 𝗋 − 𝗋_out⌉ and
ℓ̃ = ⌈𝗋_out − inf 𝗋⌉ = 0. Here 0 < sup 𝗋 − 𝗋_out = 𝗋_in − 𝗋_out = 7/4 − β_sctf + ϵ/2 < 3/4 + 1/16 < 1, as β_sctf ≥ 1
and ϵ < 1/8; so ℓ = 1 for every such ϵ, and the last step of the proof of [[cor:iii-f1-3-4]] (k replaced by k + ℓ̃,
ℓ made independent of ϵ) changes nothing. Near ztf the two spaces are H^(s−2+k)_(b,β_ztf−2) = H^(k−1)_(b,β_ztf−2) and
H^(s+k)_(b,β_ztf) = H^(k+1)_(b,β_ztf), which the input order k + 1 and the output order k accommodate. So
[[eq:iii-f1-3-3]] holds with ℓ = 1. The expression of [[lem:ec-closed-forms]] (d) at these orders is ℓ + ℓ̃ = 1, and it
is at least 1 at every choice.

*The applications.* [[thm:iii-g4-3-1]] uses [[cor:iii-f1-3-4]] with β_sctf = ℓ_scf, and [[prop:iii-g4-4-4]] and
[[prop:iii-g4-5-1]] use it through [[thm:iii-g4-3-1]] or directly with β_sctf = ℓ_scf. The construction applies them
with ℓ_scf := 3/2 − ε: in Step 3.2 of the proof of [[prop:iii-i6-2-1]], in Step 3.4′ of the proof of
[[lem:iii-i8-3-2]], at level 1 of the proof of [[prop:iii-i11-3-1]], and at levels 2 and 3 there and in
[[prop:iii-i13-2-1]] and [[prop:iii-j3-4-3]], whose forcings keep the scf-order 5/2 − ε of Step 0
([[lem:iii-i11-2-2]]). In each of them ε is a loss that the proof takes small, and the bounds on it there give ε < ¼:
ε < ½ε_g < ¼ in [[lem:iii-i8-3-2]], 2ε < ε_+ − η_2 in [[sec:iii-i11-1]], and 5ε ≤ 5ε_1 < ε_+ in [[sec:iii-j2-1]],
with ε_+ < δ_♯ < ¼ ([[eq:iii-i9-1-1]]). So β_sctf = 3/2 − ε ∈ (1, 3/2). ∎

#### The order of the background terms {#sec:uc-dbg}

**Proposition {#prop:uc-dbg}** (d_BG = 11 serves.) For ‖β‖_(d_0) small, with d_0 ≥ 11, every family A of
[[lem:iii-j2-2-1]] (b) applied to a solution satisfies

    ‖Au‖_k ≤ C_k (‖u‖_(k+2) + ‖β‖_(k+11) ‖u‖_2),                                                       {#eq:uc-dbg}

and each family v_β of sources in [[lem:iii-j2-2-1]] (b) satisfies ‖v_β‖_k ≤ C_k(1 + ‖β‖_(k+11)). So the families of
[[lem:iii-j2-2-1]] (b) have split loss (2; 11, 2) in the sense of [[lem:ec-split-loss]], the bound of
[[lem:iii-j2-2-1]] (b) holds with d = 11, and the charge max(2, d_BG) of [[rem:ec-other-losses]] may be taken to be 11.

*Proof.* *The background as a metric.* The families depend on β = (h, p⃗, q) through h̃ := h + h_tot(p⃗) + h_(b,rem)(q)
and through p⃗. By [[lem:iii-i9-2-5]], ‖h_tot(p⃗)‖_(𝒳^k) ≤ C_k|p⃗|. By [[eq:iii-i14-1-2]] and [[def:iii-g2-2-5]],
h_(b,rem)(q) is a finite sum of fixed smooth tensors times the components of q and their t_*-derivatives of order at most
3 (the towers use the derivatives a^((j)), j ≤ k_μ ≤ 3, [[lem:iii-g2-2-6]]). On functions of t_*,
∂_(t_*) = t_*⁻¹(t_*∂_(t_*)), and t_*∂_(t_*) is the b-vector field of the spaces of [[eq:iii-i14-1-1]], while t_*⁻¹ only
adds decay; so ‖h_(b,rem)(q)‖_(𝒳^k) ≤ C_k‖q‖_(𝒬^(k+3)). Hence ‖h̃‖_m ≤ C_m‖β‖_(m+3) for every m.

*The coefficients.* By [[lem:iii-j2-2-1]] (b), A is a b-differential operator of order at most 2 whose coefficients, in
the frame and in local b-coordinates on a finite atlas, are polynomials in the metric, its inverse and their
derivatives, the background g_0 being smooth in p⃗; the derivatives of the metric are of order at most 2, A being a
difference of linearisations of the second-order operator P of [[eq:iii-b-6-4]], or such a difference applied to a
fixed section. Let A′ be A with h̃ replaced by 0; its coefficients are smooth in x and p⃗ alone, so
‖A′u‖_k ≤ C_k‖u‖_(k+2). Then A = A′ + Σ_(|γ|≤2) Φ_γ(x, p⃗, w) D^γ_b, where w := (h̃, D_b h̃, D²_b h̃) and Φ_γ is
smooth with Φ_γ(x, p⃗, 0) = 0.

*The estimates.* We use [[lem:ii-g-4-1]] on the five-dimensional manifold with corners, with d = 3 > 5/2, after a
finite partition of unity (on which the norms are equivalent) and after factoring the weights, whose powers of the
defining functions commute with b-derivatives up to smooth factors. The proof of its (3), by the chain rule and
[[eq:ii-g-4-1]], applies verbatim to a smooth function Φ(x, p⃗, w) of a vector w with Φ(x, p⃗, 0) = 0 and bounded
derivatives in x and p⃗ on the chart domains; so ‖Φ_γ(·, p⃗, w)‖_m ≤ C_m‖w‖_(m+3) ≤ C_m‖h̃‖_(m+5) for ‖w‖_3 small. By its
(2), with Φ_γ in the place of the factor measured at the high order,

    ‖Φ_γ D^γ_b u‖_k ≤ C_k (‖Φ_γ‖_3 ‖u‖_(k+2) + ‖Φ_γ‖_(k+3) ‖u‖_2) ≤ C_k (‖h̃‖_8 ‖u‖_(k+2) + ‖h̃‖_(k+8) ‖u‖_2),

and ‖h̃‖_8 ≤ C‖β‖_11 ≤ C‖β‖_(d_0), ‖h̃‖_(k+8) ≤ C_k‖β‖_(k+11). This is [[eq:uc-dbg]] on the remainders. At a face
where the spaces carry an expansion, the coefficients of a product are finite sums of products of coefficients, and
the coefficients of Φ_γ(·, p⃗, w) are polynomials in those of w, functions on a face of dimension at most 4, which
(2) and (3) of [[lem:ii-g-4-1]] bound with the same d = 3 > 4/2; so the coefficient norms obey the same bound. The
sources are the case of a fixed section u, or of a fixed operator applied to the background. ∎

#### The Fourier steps and the map Φ {#sec:uc-counts}

**Lemma {#lem:uc-fourier-count}** (The Fourier step of a level above 3.) At a level β ∈ (3, α] of
[[thm:iii-i14-3-1]], Step 0 of the proof of [[prop:iii-i11-3-1]] (through [[prop:iii-i13-2-1]] when β < 4) applies
[[prop:iii-a-4-2]] (1) with E_ι = ℰ^♭ + 2, β_ι = w_+ − ε, E_I = E_K = ∅ and β_K = β − ε. Its loss, by
[[lem:ec-closed-forms]] (g), is

    l = 1 + n_ι + 2⌊β − ε⌋,     n_ι = n(ℰ^♭ + 2, w_+ − ε),                                         {#eq:uc-fourier-count}

and n_ι is the number of pairs (λ, k) ∈ ℰ^♭ with Re λ ≤ 3 + ε_+ − ε. [[prop:iii-i10-3-1]] (c) fixes ℰ^♭ only by
π_1(ℰ^♭ ∩ {Re < 3 + ε_+}) ⊂ Λ ∩ {Re ≥ 2} and the logarithmic order at most k̄(λ) at λ. So, with
N_Λ := |Λ ∩ {Re < 3 + ε_+}| and l_*, k̄_0, J_* of [[def:iii-i10-1-1]],

    n_ι ≤ N_Λ(k̄_0 + 1) + (J_* + 1)(l_* + 1)N_Λ²,     J_* ≤ ⌈5/ε_Υ⌉ + 2,

and at ε_Υ = 1.4619·10⁻¹⁰, J_* ≤ 34,202,065,807. The single-step loss c(β) of [[prop:ec-upper]] at such a level is at
least 1 + n_ι.

*Proof.* The data of Step 0 are those printed there. By the case E_I = ∅ of [[lem:ec-closed-forms]] (g),
l = 1 + n_ι + 2(n_K + ⌊β_K⌋) with n_K = n(∅, β_K) = 0. By the definition of n(E, β) before [[lem:ec-closed-forms]],
n(E_ι, β_ι) counts the pairs (z, m′) ∈ ℰ^♭ + 2 with Re z ≤ w_+ − ε = 5 + ε_+ − ε. At an exponent λ of ℰ^♭ of
logarithmic order m there are m + 1 pairs, and m ≤ k̄(λ) = k̄_0 + (J_* + 1)(l_* + 1)(n(λ) + 1) with n(λ) ≤ N_Λ − 1; at
most N_Λ exponents occur. This gives the bound for n_ι. By [[lem:ec-iota-gap]], η_0 ≥ ε_Υ, so
J_* = ⌈5/η_0⌉ + 2 ≤ ⌈5/ε_Υ⌉ + 2, and 5/(1.4619·10⁻¹⁰) = 500000000000000/14619 = 34202065804.77…, whose ceiling is
34,202,065,805. The level step composes this map with maps of non-negative loss, so by [[def:ec-accounted-loss]] its
charge is at least l ≥ 1 + n_ι. ∎

**Lemma {#lem:uc-phi-loss}** (The loss of Φ and the two other components of d_NM.) Let 3 < ℓ_I < 3.5, and let the
strips of [[cor:iii-g3-3-1]] used in the proof of [[thm:iii-j-2-4]] be taken with λ₋ ∈ (ℓ_I − 2, 3/2) and
δ_ι < 3.5 − ℓ_I. The proof of [[thm:iii-j-2-4]] fixes its loss d as the sum, over its steps, one for each λ₀ in
Λ_* = Λ ∩ {Re < 3 + ε_+}, of the loss l′ of [[cor:iii-g3-3-1]], the loss 2 of the functionals of [[thm:iii-g2-3-1]] and
the loss l of [[prop:iii-g3-3-7]], plus 2; so it is

    d_Φ = 62N_Λ + 2.                                                                                  {#eq:uc-phi-loss}

The losses d_FM of [[prop:iii-j2-4-3]] and d_Ψ of [[lem:iii-k-2-2]], as their proofs fix them from d_Φ and
[[lem:ii-g-4-1]], are at most d_Φ + 8 = 62N_Λ + 10, and d_NM = max(d_R, d_FM, d_Ψ), with d_R ≥ d_acc the accounted loss
of [[lem:iii-k-2-3]], and N_NM = 21d_NM + 6.

*Proof.* By [[lem:ec-closed-forms]] (f), l′ = 30 under these conditions, and l = l′ ((f) and its proof), so each step
contributes 30 + 2 + 30 = 62, and the steps are indexed by Λ_*, which has N_Λ elements; this is [[eq:uc-phi-loss]]. The
proof of [[prop:iii-j2-4-3]] bounds P_5(Φ(U)) by [[lem:ii-g-4-1]]: P_5(h, p⃗, q) is a smooth function, vanishing at 0,
of w = (h″, D_b h″, D²_b h″), h″ := h + h_(b,rem)(q), with coefficients smooth in p⃗. As in the proof of
[[prop:uc-dbg]], its order-k norm is at most C_k‖w‖_(k+3) ≤ C_k‖h″‖_(k+5) ≤ C_k‖Φ(U)‖_(k+8), and
‖Φ(U)‖_(k+8) ≤ C_k‖U‖_(𝒟^(k+8+d_Φ)); its first two derivatives are bounded in the same way, being polynomial in the
derivatives of Φ by the chain rule. So d_FM ≤ d_Φ + 8. [[lem:iii-k-2-2]] (c) is the same bound for Ψ(U), which
differs from Φ(U) by fixed tensors smooth in the finite-dimensional components of U, on the exact scales, where
[[prop:iii-j3-5-4]] follows the proof of [[thm:iii-j-2-4]] step by step; so d_Ψ ≤ d_Φ + 8 as well. d_NM is the largest
of the losses of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]], that of [[lem:iii-k-2-3]] accounted by
[[def:ec-accounted-loss]] and at least d_acc ([[thm:loss-d]]), and N_NM = 21d_NM + 6 is the regularity of
[[thm:ii-g-2-1]] at that loss ([[thm:loss-d]], [[eq:ii-g-2-5]]). ∎

#### What the statements give {#sec:uc-reduction}

**Theorem {#thm:uc-reduction}** (Bounds for d from the statements of this paper.) At the computational point:

(i) In [[prop:ec-upper]], [[lem:ec-round-charges]] and [[rem:ec-other-losses]] one may take ℓ_tf = 1 and d_BG = 11
([[prop:uc-ltf]], [[prop:uc-dbg]]); the explicit part of the bound of [[rem:ec-upper-point]] is then
9.394·10¹⁹ + 1.2923·10²¹ < 1.3863·10²¹, under the hypothesis made there that (G) holds at ε_K = 1.46·10⁻¹⁰.

(ii) d_NM = max(d_R, d_FM, d_Ψ) with d_R ≥ d_acc and d_FM, d_Ψ ≤ 62N_Λ + 10, N_NM = 21d_NM + 6, and every term of the
bound of [[prop:ec-upper]] other than the single-step losses is explicit in ε_K and the other weights; the single-step
losses at the levels above 3 are at least 1 + n_ι, with n_ι bounded by [[lem:uc-fourier-count]] in N_Λ, l_* and k̄_0.

(iii) The admissible ε_K (through (G)), N_Λ, l_* and k̄_0 are fixed by the index sets of [[sec:uc-index-sets]], and
the statements of this paper fix none of them: for every M > 0 there is a choice of ℰ_ind compatible with every
membership in which it is asserted, as in [[prop:uc-no-eps]], for which every ε_K satisfying (G) is below
1/M and, for every admissible choice of the weights, d_NM ≥ d_acc > 2M · 10¹⁰.

So the statements of this paper give the lower bound of [[thm:loss-d]] (ii) and no upper bound for d_acc, d_NM or
N_NM.

*Proof.* (i) is [[prop:uc-ltf]] and [[prop:uc-dbg]] substituted into [[prop:ec-upper]] and [[rem:ec-upper-point]]:
9.394·10¹⁹ · 1 + 1.2923·10²¹ = 1.38624·10²¹. (ii) is [[lem:uc-phi-loss]], the counts of [[lem:ec-counts]] and
[[prop:ec-upper]], and [[lem:uc-fourier-count]]. (iii) [[def:iii-i10-1-1]] and [[def:iii-i10-1-3]] define N_Λ, l_*,
k̄_0 and (G) from these index sets and from ε_+, so they are fixed by them. Let M > 0 and t := min(1/M, 10⁻¹⁰). By
[[prop:uc-no-eps]], with E_t in place of ℰ_ind, (G) fails for every ε_K ≥ t, so every admissible ε_K is below t. By
[[prop:ec-rounds]], R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂) > (1 − 3·10⁻¹⁰ − 2δ̂ − δ̄)/(tδ̂), and the numerator exceeds
0.99999997, so R > 0.99999997/(1.46214·10⁻¹⁰ t) > 6.8·10⁹ M, as 1/t ≥ M. By [[thm:loss-d]] (ii),
d_NM ≥ d_acc ≥ 3R > 2·10¹⁰ M. ∎

**Remark {#rem:uc-missing}** (The statement an integer upper bound needs.) An integer D with d ≤ D follows from
[[prop:ec-upper]], [[thm:uc-reduction]] and the closed forms of [[lem:ec-closed-forms]] once the following is proved:

(IS) at the computational point and at every b near b₀, the index sets ℰ_ind (with all its enlargements), ℰ^ι_ind, the
least ℰ^C_I of [[def:iii-c-3-1]] and the least ℰ_++ have explicitly listed exponents of real part at most 5, with
explicit bounds for their logarithmic orders there.

From (IS) the set Λ ∩ {Re ≤ 3 + ε_+} is an explicit finite set; (G) then holds at an explicit ε_K by a lower bound for
the distances from 2 and from 3 of finitely many sums of explicit algebraic numbers, of the kind of [[prop:gap-sums]]
and [[lem:uc-two-offsets]]; and N_Λ, l_*, k̄_0, J_* and the counts n(E, β) of every application of [[prop:iii-a-4-2]]
follow, so that c(β), c_b, c′_b, c_0 and the losses of [[lem:uc-phi-loss]] become integers, each a finite sum of the
closed forms of [[lem:ec-closed-forms]], [[rem:ec-other-losses]], [[prop:uc-dbg]], [[prop:uc-ltf]] and of the forward
loss of [[thm:fwd-loss]]. (IS) is not a consequence of the statements of this paper ([[prop:uc-no-eps]]). It is a
statement about the proofs of [[prop:iii-d2-3-1]], [[prop:iii-d3-3-1]], [[prop:iii-f3-2-2]], the physical states of
[[ch:s15]] and [[thm:iii-g2-4-2]], which solve for the corrections of the states with the inverses of (□^Υ_b)^(0),
(□^C_b)^(0) and L̂_b(0) and record only the least real part of what they produce. Proving it means carrying those
proofs again with the exponents recorded: for each state, the indicial roots of these three operators that its
corrections meet below the real part 5 above its leading term, at every angular type that the coupling of the types by
a rotating g_b reaches there ([[rem:uc-offset-d0]]), with the roots of L̂_b(0) at those types, which [[ch:s14]] bounds
only by their distance δ_50 from the integers. Then (G) is a question about the closeness to 2 and 3 of sums of several
independent small offsets, whose scale [[lem:uc-two-offsets]] shows for two of them.
