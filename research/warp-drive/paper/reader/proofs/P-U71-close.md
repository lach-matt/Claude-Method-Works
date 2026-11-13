### The inputs of the upper bound for the accounted loss {#sec:uc-close}

This section takes the inputs that [[prop:ec-upper]] leaves free and decides, for each, whether this paper determines
it. Two are determined. The loss of the inverse of the transition face model is 1 at the weights at which the
construction may use it, so ℓ_tf = 1 ([[prop:uc-ltf]]); and the order of the background terms may be taken to be
d_BG = 11 ([[prop:uc-dbg]]). The others are not evaluated here: the admissible ε_K of the gap condition (G), the counts
n(E, β) of the index sets entering the Fourier steps of the levels ([[lem:uc-fourier-count]]), and the loss of the map
Φ of [[thm:iii-j-2-4]], which governs the two other components of d_NM ([[lem:uc-phi-loss]]), are fixed by the index
sets that define the set Λ of [[def:iii-i10-1-1]], whose exponents the constructions of this paper fix, while its
statements record only memberships and least real parts, which alone fix no admissible ε_K ([[prop:uc-no-eps]]); and if
both offsets of the class roots are increments of Λ, as they are for the index sets that the proofs construct, every
admissible ε_K lies below 1.6417·10⁻¹⁴ ([[cor:uc-two-offsets]]). The counts depend besides, through the number l_* of
[[def:iii-i10-1-1]], on the orders of the poles of N_ι⁺(L̄, ·)⁻¹, which this paper does not determine. Consequently the
statements of this paper bound d from below, and from above only through numbers that it does not evaluate
([[thm:uc-reduction]]); [[rem:uc-missing]] states the two statements that an integer upper bound needs. Throughout we
work at the computational point of [[def:ec-point]], so z = 4·10⁻⁶ = 1/250000 and λ_♯ = 15099/10000, and 𝔡₀ = d_c0,
𝔡₁ = d_c1 are the offsets of [[sec:ec-gap-sums]].

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

Each of these sets enters the statements of this paper through memberships of the form u ∈ 𝒜^E (or a partially
polyhomogeneous space with the index set E) and a lower bound for its real parts, and it is fixed by a construction.
ℰ_ind is built in the proofs of [[prop:iii-d2-3-1]] ((F1) there), [[lem:iii-f3-2-1]] and [[lem:iii-d3-2-1]] by
[[lem:iii-a-1-4]], from the indicial roots of (□^Υ_b)^(0), which [[lem:iii-d-4-1]] and [[prop:np-10-52]] (i) give in
closed form, and from exponents of the right sides that are integers or such roots shifted by integers. ℰ^ι_ind collects the index
sets of the states of [[ch:s13]] and [[ch:s15]], 2 + ℕ₀ and (2, 1) (the proof of [[thm:iii-g2-4-2]]); the physical
states of [[ch:s15]] are built by [[lem:iii-a-1-4]] from the roots of L_b^(0) ([[prop:iii-f1-2-3]]), among them ι^C − 1
for the roots ι^C of the polynomials of [[prop:np-10-12]] (the proof of [[prop:iii-f4-5-1]]). The least ℰ^C_I is
generated from σ_Υ by (3) of [[def:iii-c-3-1]], and the least ℰ_++ by [[eq:iii-i8-1-1]]. So the exponents of these sets
below the real part 5 are algebraic numbers fixed by this paper, which it does not list. A space with an index set E is
contained in the space with any index set E′ ⊃ E, the coefficients at the added exponents being 0.

**Proposition {#prop:uc-no-eps}** (Memberships fix no admissible ε_K.) Let t > 0 and

    E_t := ℰ_ind ∪ {(3 − λ_♯ + t + j, 0) : j ∈ ℕ₀}.

Then E_t is an index set with min Re E_t ≥ ε_Υ, every membership that [[prop:iii-d2-3-1]], [[prop:iii-d3-3-1]] and
[[prop:iii-f3-2-2]] assert with ℰ_ind holds with E_t in its place, the conditions [[eq:iii-i7-1-2]], [[eq:iii-i8-1-1]]
and (H3) on ℰ_+ being met by enlarging ℰ_+, and for the set Λ_t that [[def:iii-i10-1-1]] builds from E_t, (G) fails for
every ε_K ≥ t. So no positive number can be shown to be an admissible ε_K from information about ℰ_ind that consists of
such memberships and of the bound min Re ℰ_ind ≥ ε_Υ; the exponents of ℰ_ind themselves are needed. The proposition
concerns enlargements of ℰ_ind: enlarging an admissible index set, like decreasing ε_K, only lowers the admissible ε_K,
so it bounds neither the admissible ε_K of the index sets that the proofs construct nor d from above.

*Proof.* E_t is a union of two index sets, so it has finitely many exponents below each bound, finitely many
logarithms at each, and is closed under (z, k) ↦ (z + 1, k); its new exponents have real part at least
3 − λ_♯ = 1.4901 > ε_Υ. A membership with ℰ_ind implies the same membership with E_t ⊃ ℰ_ind. The conditions
[[eq:iii-i7-1-2]], [[eq:iii-i8-1-1]] and (H3) involve ℰ_ind only through lower bounds for ℰ_+ and for ℰ_++ ⊂ ℰ_+, which
an enlargement of ℰ_ind only strengthens ([[sec:iii-i8-1]]). The proof of [[lem:iii-i10-1-2]] (b), which uses of ℰ_ind
only that its exponents have positive real parts, shows that they are conditions on ℰ_+ alone, met by the least index
set that contains ℰ_+, 2 + E_t and ℰ_par + ℱ, with ℰ_par built from Λ_t, and that is closed under the addition of
ℰ^ι_ind ∪ E_t and of itself. In Λ_t, λ_♯ is a generator and 3 − λ_♯ + t ∈ π_1E_t is an increment, so 3 + t ∈ Λ_t. Its
real part lies in (3, 3 + ε_K] as soon as ε_K ≥ t, which (G) excludes. ∎

Enlargements of the same kind, by finitely many exponents of real parts in [ε_Υ, 1), each with its translates by ℕ₀
and with any logarithmic orders, raise the number of points of Λ below 3 + ε_+ and the bounds l_* and k̄_0 of
[[def:iii-i10-1-1]] beyond any given bound: each such exponent z gives the point λ_♯ + z < 3 of Λ, and the exponent
2 + z < 2λ_♯ of 𝒢 with its logarithmic order. So memberships and least real parts alone do not bound these numbers
either.

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

**Corollary {#cor:uc-two-offsets}** (The gap condition when both offsets are increments.) (a) Suppose that 𝔡₀ and 𝔡₁
lie in π_1(ℰ_ind ∪ ℰ^ι_ind), as they do for ℰ_ind as constructed ((b) and [[rem:uc-offset-d0]]). Then every ε_K with
which (G) holds satisfies ε_K < 1.6417·10⁻¹⁴; in particular (G) does not hold at ε_K = 1.46·10⁻¹⁰, the value assumed in
[[rem:ec-upper-point]]. For every admissible choice of the weights, the number R of [[prop:ec-rounds]] then satisfies
R > 4.1659·10²³, so that d_NM ≥ d_acc > 1.2497·10²⁴ and N_NM = 21d_NM + 6 > 2.624·10²⁵.

(b) For ℰ_ind as the proof of [[prop:iii-d2-3-1]] constructs it, 𝔡₀ and 𝔡₁ lie in π_1ℰ_ind. So the hypothesis of (a)
holds for the index sets as constructed, and for them (G) does not hold at ε_K = 1.46·10⁻¹⁰.

*Proof.* (a) λ := λ_♯ + a𝔡₀ + b𝔡₁, with a and b of [[lem:uc-two-offsets]], is obtained from the generator λ_♯ by
a + b additions of increments, so λ ∈ Λ, and Re λ − 3 < 1.6417·10⁻¹⁴ by [[eq:uc-two-offsets]]. If
ε_K ≥ 1.6417·10⁻¹⁴, then Re λ ∈ (3, 3 + ε_K], against (G). By [[prop:ec-rounds]],
R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂) with δ̂ = 1.46214·10⁻¹⁰ and δ̄ = 1.94137057·10⁻⁸, and the right side decreases in ε_K.
At ε_K = 1.6417·10⁻¹⁴ the numerator exceeds 1 − 1.98·10⁻⁸ > 0.99999998 and ε_Kδ̂ = 2.400395…·10⁻²⁴ < 2.4004·10⁻²⁴, so
R > 4.16597·10²³. By [[thm:loss-d]] (ii), d_NM ≥ d_acc ≥ 3R > 1.2497·10²⁴, and 21 · 1.2497·10²⁴ > 2.624·10²⁵.

(b) The step of the proof of [[prop:iii-d2-3-1]] that corrects the translations applies the fact (F1) of that proof
with k = 2. There [[lem:iii-a-1-4]] is applied with a weight α ∈ (2 − ε_Υ, 2), and the index set ℰ it gives contains
E(α), the smallest index set that contains the elements (ι, 0) of the boundary spectrum of ρ⁻²(□^Υ_b)^(0), of every
type, with Re ι > α. By [[lem:iii-d-4-1]], ι^Υ_(s0,2) = 2 + 𝔡₀ (type s0) and ι^Υ_(s1,2) = 2 + 𝔡₁ (type s1) are simple
roots, and their real parts exceed 2 > α. (F1) writes ℰ as (2, 0) ∪ (2 + ℰ_ind), and 2 + 𝔡₀ and 2 + 𝔡₁ differ from 2;
so (𝔡₀, 0) and (𝔡₁, 0) lie in that ℰ_ind, which is part of the union ℰ_ind of [[sec:uc-index-sets]]. ∎

**Remark {#rem:uc-offset-d0}** (The offset 𝔡₀ as an increment.) [[rem:gap-sums]] lets 𝔡₀ enter Λ through the increment
1 + 𝔡₀ only, and [[prop:gap-sums]] shows that the windows of (G) are then not met by the sums it considers for
ε_K < 5.019·10⁻⁸. For ℰ_ind as the proof of [[prop:iii-d2-3-1]] constructs it, 𝔡₀ and 𝔡₁ are exponents: (F1) there,
with k = 2, takes the boundary spectrum above a weight in (2 − ε_Υ, 2), at every type ([[cor:uc-two-offsets]] (b)). So
with ℰ_ind as constructed, (G) fails at 1.46·10⁻¹⁰ ([[cor:uc-two-offsets]]). Whether a smaller admissible ℰ_ind omits
𝔡₀ is not decided by this paper. The root ι^Υ_(s0,2) = 2 + 𝔡₀ of (□^Υ_b)^(0) lies above the weights in (0, ι^Υ_(s1,2))
at which [[prop:iii-d2-3-1]] solves for the corrections of the states, and these corrections start at the order (2, 0),
so a smaller admissible ℰ_ind keeps the exponent 𝔡₀ wherever a term at that root has a nonzero coefficient. At b₀ the
operator commutes with the rotations, and the corrections of the states of types s1 and v1 do not meet the roots of
type s0. At a rotating b the metric couples the angular types at the order |x|⁻³ ([[eq:iii-d2-2-2]]), and ℰ_ind is one
index set serving at every b near b₀. So (G) at an ε_K ≥ 1.6417·10⁻¹⁴ needs a smaller admissible ℰ_ind ∪ ℰ^ι_ind that
omits 𝔡₀ or 𝔡₁; omitting 𝔡₀ means the vanishing of these coefficients at every b near b₀.

#### The loss of the inverse of the transition face model {#sec:uc-ltf}

**Proposition {#prop:uc-ltf}** (The loss of [[cor:iii-f1-3-4]] is 1.) Let β_sctf ∈ [1, 3/2) and β_ztf ∈ [−1, 0). The
proof of [[cor:iii-f1-3-4]] runs with the regularity s := 1, the weight α_+ := 0, the incoming order 𝗋_in := −¼ and, at
the incoming radial sets, the inner product of [[lem:ec-theta-in-zero]], and gives [[eq:iii-f1-3-3]] with ℓ = 1, for
every k ∈ ℕ₀ and every ϵ ∈ (0, ¼(3/2 − β_sctf)). So with these choices the loss of [[cor:iii-f1-3-4]] is 1, which is
the value of ℓ_tf in [[lem:ec-closed-forms]] (d), and its least possible value there. Every application of
[[cor:iii-f1-3-4]] in the construction of [[thm:iii-i14-3-1]] and of [[thm:iii-j1-2-1]] can be made with
β_sctf = 3/2 − ε, with 0 < ε < ¼; so ℓ_tf = 1 at all of them, and in [[prop:ec-upper]] and [[lem:ec-round-charges]]
ℓ⁺_tf = 1.

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
the inner product of [[lem:ec-theta-in-zero]], ϑ_in = 0, so (−1 + ϑ_in)/2 = −½ < −¼ = 𝗋_in; and
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
[[prop:iii-g4-5-1]] use it through [[thm:iii-g4-3-1]] or directly with β_sctf = ℓ_scf. The construction may apply them
with ℓ_scf := 3/2 − ε, as [[lem:ec-tf-loss]] takes it: in Step 3.2 of the proof of [[prop:iii-i6-2-1]], in Step 3.4′
of the proof of [[lem:iii-i8-3-2]], at level 1 of the proof of [[prop:iii-i11-3-1]], and at levels 2 and 3 there and in
[[prop:iii-i13-2-1]] and [[prop:iii-j3-4-3]], whose forcings keep the scf-order 5/2 − ε of Step 0
([[lem:iii-i11-2-2]]), which allows ℓ_scf := 3/2 − ε there. In each of them ε is a loss that the proof takes small, and
the bounds on it there give ε < ¼: ε < ½ε_g < ¼ in [[lem:iii-i8-3-2]], 2ε < ε_+ − η_2 in [[sec:iii-i11-1]], and
5ε ≤ 5ε_1 < ε_+ in [[sec:iii-j2-1]], with ε_+ < δ_♯ < ¼ ([[eq:iii-i9-1-1]]). So β_sctf = 3/2 − ε ∈ (1, 3/2) at every
application; and an application at another sctf-weight in [1, 3/2), such as the weight 3/2 − 2ε of the level-3
solution, has ℓ = 1 as well, by the first part of the proof. ∎

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
[[prop:iii-a-4-2]] (1) with E_ι = ℰ^♭ + 2, β_ι = w_+ − ε, E_I = E_K = ∅ and β_K = β − ε. Its loss, by the case
E_I = ∅ of the proof of [[lem:ec-closed-forms]] (g), is

    l = 1 + n_ι + 2⌊β − ε⌋,     n_ι = n(ℰ^♭ + 2, w_+ − ε),                                         {#eq:uc-fourier-count}

and n_ι is the number of pairs (λ, k) ∈ ℰ^♭ with Re λ ≤ 3 + ε_+ − ε. [[prop:iii-i10-3-1]] (c) states of ℰ^♭ that
π_1(ℰ^♭ ∩ {Re < 3 + ε_+}) ⊂ Λ ∩ {Re ≥ 2} and that its logarithmic order at λ is at most k̄(λ). So, with
N_Λ := |Λ ∩ {Re < 3 + ε_+}| and l_*, k̄_0, J_* of [[def:iii-i10-1-1]],

    n_ι ≤ N_Λ(k̄_0 + 1) + (J_* + 1)(l_* + 1)N_Λ²,     J_* ≤ ⌈5/ε_Υ⌉ + 2,

and at ε_Υ = 1.4619·10⁻¹⁰, J_* ≤ 34,202,065,807. The single-step loss c(β) of [[prop:ec-upper]] at such a level is at
least 1 + n_ι.

*Proof.* The data of Step 0 are those printed there. By the case E_I = ∅ of the proof of [[lem:ec-closed-forms]] (g)
(the formula (1) of (g), which holds for every E_I, gives 1 + n_ι + 10 here),
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
proof of [[prop:iii-j2-4-3]] bounds P_5(Φ(U)) by [[lem:ii-g-4-1]]: P_5(h, p⃗, q) − P_5(0, p⃗, 0) is a smooth function,
vanishing at 0, of w = (h″, D_b h″, D²_b h″), h″ := h + h_(b,rem)(q), with coefficients smooth in p⃗, and P_5(0, p⃗, 0)
is a fixed tensor smooth in p⃗. As in the proof of [[prop:uc-dbg]], its order-k norm is at most
C_k‖w‖_(k+3) ≤ C_k‖h″‖_(k+5) ≤ C_k‖Φ(U)‖_(k+8), with [[lem:iii-j2-2-4]] for the coefficients at the faces, and
‖Φ(U)‖_(k+8) ≤ C_k‖U‖_(𝒟^(k+8+d_Φ)); its first two derivatives are bounded in the same way, being polynomial in the
derivatives of Φ by the chain rule. So d_FM ≤ d_Φ + 8. [[lem:iii-k-2-2]] (c) is the same bound for Ψ(U), which
differs from Φ(U) by fixed tensors smooth in the finite-dimensional components of U, on the exact scales, where
[[prop:iii-j3-5-4]] follows the proof of [[thm:iii-j-2-4]] step by step; so d_Ψ ≤ d_Φ + 8 as well. d_NM is the largest
of the losses of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]], that of [[lem:iii-k-2-3]] accounted by
[[def:ec-accounted-loss]] and at least d_acc ([[thm:loss-d]]), and N_NM = 21d_NM + 6 is the regularity of
[[thm:ii-g-2-1]] at that loss ([[thm:loss-d]], [[eq:ii-g-2-5]]). ∎

#### What the statements give {#sec:uc-reduction}

**Theorem {#thm:uc-reduction}** (Bounds for d from the statements of this paper.) At the computational point:

(i) In [[prop:ec-upper]], [[lem:ec-round-charges]] and [[rem:ec-other-losses]] one may take ℓ⁺_tf = 1 and d_BG = 11
([[prop:uc-ltf]], [[prop:uc-dbg]]); the explicit part of the bound of [[rem:ec-upper-point]] is then
9.394·10¹⁹ + 1.2923·10²¹ < 1.3863·10²¹, under the hypothesis made there that (G) holds at ε_K = 1.46·10⁻¹⁰, which
fails for the index sets as constructed ([[cor:uc-two-offsets]]).

(ii) d_NM = max(d_R, d_FM, d_Ψ) with d_R ≥ d_acc and d_FM, d_Ψ ≤ 62N_Λ + 10, N_NM = 21d_NM + 6, and every term of the
bound of [[prop:ec-upper]] other than the single-step losses is explicit in ε_K and the other weights; the single-step
losses at the levels above 3 are at least 1 + n_ι, with n_ι bounded by [[lem:uc-fourier-count]] in N_Λ, l_* and k̄_0.

(iii) N_Λ, k̄_0 and the admissible ε_K (through (G)) are fixed by the exponents and logarithmic orders of the index
sets of [[sec:uc-index-sets]], which this paper fixes and does not list; and l_* bounds also the orders of the poles
of N_ι⁺(L̄, ·)⁻¹ at real part at most 5, of which this paper states only that they lie in {Re ≥ 2}, finitely many
below each bound ([[lem:iii-g1-4-2]] (a)). Memberships and least real parts alone fix no admissible ε_K
([[prop:uc-no-eps]]).

So this paper gives the lower bound of [[thm:loss-d]] (ii), and an upper bound for d_acc, d_NM and N_NM, at levels
more than ½(α − 4) apart, only in terms of these numbers; it evaluates none of them and proves no integer upper bound.

*Proof.* (i) is [[prop:uc-ltf]] and [[prop:uc-dbg]] substituted into [[prop:ec-upper]] and [[rem:ec-upper-point]]:
9.394·10¹⁹ · 1 + 1.2923·10²¹ = 1.38624·10²¹; the failure of (G) is [[cor:uc-two-offsets]] (b). (ii) is
[[lem:uc-phi-loss]], the counts of [[lem:ec-counts]] and [[prop:ec-upper]], and [[lem:uc-fourier-count]]. (iii)
[[def:iii-i10-1-1]] and [[def:iii-i10-1-3]] define N_Λ, l_*, k̄_0 and (G) from these index sets, from the orders of
the poles of N_ι⁺(L̄, ·)⁻¹ and from ε_+; the index sets are those of [[sec:uc-index-sets]], and of the poles
[[lem:iii-g1-4-2]] (a) gives what is stated. The last assertion is [[prop:ec-upper]] with (i), (ii) and
[[lem:uc-fourier-count]]. ∎

**Remark {#rem:uc-missing}** (What an integer upper bound needs.) An integer D with d ≤ D follows from
[[prop:ec-upper]], [[thm:uc-reduction]] and the closed forms of [[lem:ec-closed-forms]] once the following are
established at the computational point:

(IS) the exponents of real part at most 5 of ℰ_ind (with its enlargements in [[sec:iii-i8-1]] and [[sec:iii-i9-1]]),
ℰ^ι_ind, the least ℰ^C_I and the least ℰ_++, as the constructions of [[sec:uc-index-sets]] give them, listed with
bounds for their logarithmic orders there, and the multiplicities of the indicial roots of L̂_b(0) of real part at most
5 ([[prop:iii-f1-2-3]]);

(SP) a bound for the orders of the poles of N_ι⁺(L̄, ·)⁻¹ at the points of real part at most 5 (it suffices at the
points of Λ with 2 ≤ Re λ ≤ 3 + ε_+), in particular which of these lie in spec_ι⁺(L̄).

From (IS) the set Λ ∩ {Re ≤ 3 + ε_+} is an explicit finite set, and (G) holds at an explicit ε_K by a lower bound for
the distances from 2 and from 3 of finitely many sums of explicit algebraic numbers, of the kind of [[prop:gap-sums]]
and [[lem:uc-two-offsets]]; with (SP), N_Λ, l_*, k̄_0, J_* and the counts n(E, β) of every application of
[[prop:iii-a-4-2]] follow, so that c(β), c_b, c′_b, c_0 and the losses of [[lem:uc-phi-loss]] become integers, each a
finite sum of the closed forms of [[lem:ec-closed-forms]], [[rem:ec-other-losses]], [[prop:uc-dbg]], [[prop:uc-ltf]]
and of the forward loss of [[thm:fwd-loss]]. (IS) asks no new estimate: the constructions state the rule that produces
the exponents ([[lem:iii-a-1-4]], the boundary spectrum above the weight together with the source's index set; (3) of
[[def:iii-c-3-1]] for ℰ^C_I; [[eq:iii-i8-1-1]] for ℰ_++), and the roots are given by [[lem:iii-d-4-1]],
[[prop:np-10-52]] (i), [[prop:iii-f1-2-3]] and the polynomials of [[prop:np-10-12]]; it asks that these constructions
be carried out with the exponents kept, over the finitely many types whose roots meet the strip ([[prop:np-10-54]]
(iii)). (SP) needs an analysis that this paper does not contain: of spec_ι⁺(L̄) it states only [[lem:iii-g1-4-2]] (a).
Then (G) is a question about the closeness to 2 and 3 of sums of several small offsets, whose scale
[[lem:uc-two-offsets]] shows for two of them.
