# P-UB1: a proved admissible choice for the repaired set Λ at the computational point

Proof file for the coordinator. Nothing in chapters/, crosswalk/ or elsewhere in the repository was edited; this is the
only file written there, and nothing was committed. Every old text below is copied from the chapter files at HEAD
bce54b51 (the same files as at b7553023, and equal to the working tree): 71-explicit-constants.md md5
427412e02c74261f1f87da24b60ddbca, 96-tables.md md5 f577ca6233dec4e08e68ef2262f451fb (the same 71 as P-UB2 read). Each old
text occurs exactly once in its file as whole lines, and no two overlap; line numbers are those of these files. All texts
were applied to scratch copies of chapters/ and checked there (section 8). The texts assume the repair of chapter 41 that
P-I11 carries (V-I11 §4.1): def:iii-i10-1-1 defines 𝒵, the indicial roots μ of L̂_b(0) with 0 < Re μ < 3, and lists 1 + 𝒵
among the generators of Λ.

## 0. The inputs for the rest of the chain

All exact; each is proved in the texts of section 5 (T-numbers) or unchanged at HEAD.

- **ε_K = 1.6747·10⁻¹⁷ = 16747/10²¹** (def:uc-choice, T3; admissible by lem:uc-admissible, T4–T6).
- **ε_+ = 1.67478·10⁻¹⁷ = 167478/10²²**, so ε_K < ε_+ < 10⁻¹³ (def:uc-choice; (G⁺) by thm:is-gap).
- ε_Υ = ε_g = 1.4619·10⁻¹⁰, unchanged.
- Δβ_0 = 0.999²ε_K = **1.6713522747·10⁻¹⁷** exactly (16713522747/10²⁷), the factor 0.999² kept (eq:uc-deltas, T4);
  Δτ_0 = 0.999ε_Υ = 1.4604381·10⁻¹⁰, unchanged; ε ≤ 10⁻³ε_g, unchanged.
- ε′_0 = ½(ε_+ − ε_K) = 4·10⁻²² < 0.001ε_K, so 0.999ε_K ≤ α − 4 ≤ ε_K as before (lem:uc-admissible, T6).
- **N̄_Λ = 909,507,124,095,312**: N_Λ ≤ N̄_Λ for every ε_+ ∈ (0, δ̄), and N_Λ > 1.85753·10¹⁴ (prop:is-count (a), T10,
  T11).
- **k̄_0 = 3** (the least admissible bound), **η_0 = 𝔡₁**, **J_* = 15,000,015**, **l_* = 50**, so
  **J′ = (J_* + 1)(l_* + 1) = 765,000,816**: all unchanged, confirmed (prop:is-count (b), (c), cor:sp-lstar; section 3).
- **The gap**: (G) ⟺ ε_K < μ_Z and (G⁺) ⟺ ε_+ < μ_Z, with 1.6747856·10⁻¹⁷ < μ_Z < 1.6747859·10⁻¹⁷; so every ε_K with
  which (G) holds is below 1.6747859·10⁻¹⁷ (thm:is-gap, label unchanged; eq:is-mu-z in the new lem:is-gap-z).
- **Non-real elements**: every non-real element of Λ ∩ {Re ≤ 3 + ε_+} has real part above 2.514, and every element of
  Λ of real part at most 2.514 is real (prop:is-lambda, T7).
- **Lower bound** (new, optional): at every admissible choice R > 4.0836·10²⁶, d_NM ≥ d_acc ≥ 3R > 1.2250·10²⁷ and
  N_NM > 2.5725·10²⁸; at the choice 3R > 1.2251·10²⁷ (cor:is-lower, T9).

For P-UB2's requirements (its §1.4): R1 holds (eq:uc-deltas, ε ≤ 10⁻³ε_g, ε_Υ, a♭_K − 2 ≥ Δβ_0 and ε_K < ε_+ < 10⁻¹³
are kept; lem:uc-admissible gives (G), (G⁺) and the hypotheses of prop:ec-upper). R2: prop:is-count (a) gives the
integer bound N_Λ ≤ 909,507,124,095,312, so lem:uc-lambda (a) can read N̄_Λ := 909,507,124,095,312; (b), (c) are
unchanged; lem:uc-gaps stands. R3: prop:is-lambda says more (real part above 2.514, not only above 2). R4: thm:is-gap,
under its old label, states that every ε_K with which (G) holds is below 1.6747859·10⁻¹⁷; P-UB2's texts that say
"below 1.67488·10⁻¹⁷" remain true and may keep that number or take 1.6747859·10⁻¹⁷. R5 is P-I11's. P-UB2's provisional
inputs differ from these only in ε_+ (1.67475·10⁻¹⁷ there) and N̄_Λ (910,000,000,000,000 there); its evaluation step is

    python3 mkproof.py 1.6747e-17 1.67478e-17 909507124095312 3 15000015 50 --final

(in its scratch directory). The chain's lem:uc-lambda (c) and lem:cs-fourier (b) are P-UB2's repairs and are not
touched here; the sec:is statements below allow non-real elements throughout.

## 1. Summary

- **Step 4 (smaller index sets, other h): no better route that the paper can prove.** Omitting 𝔡₀ from ℰ_ind is
  admissible exactly when the coefficient c_b of def:is-cb vanishes at every rotating b near b₀ (thm:is-d0); that
  coefficient is a global connection coefficient of the stationary gauge problem on the rotating background, and
  nothing in the paper, nor any symmetry, decides it (section 2.1). If it vanished, the gain would be enormous: (G)
  would hold for every ε_K < ε_Υ and N_Λ ≤ 3,683,190,611, d_NM of order 10³⁸ instead of 10⁵⁶ (cor:is-flat as rewritten
  here, a proved conditional statement). Another computational point h ∈ (0, 10⁻⁶) would, numerically, raise the
  least excess by up to a factor of about 90, but h = 10⁻⁶ enters proofs in chapters 33, 70 and 71 and the tables of
  chapter 96; it is not changed (section 2.2).
- **Step 1, the roots.** The set Z of prop:is-iota has exactly 2629 elements of real part below 3 (1269 real, 1360
  non-real, all from C and the P_l with l ≤ 999), and every other element has real part above 3 + 4.99·10⁻⁶
  (lem:is-z3, new). Each is enclosed to within 10⁻²¹: real roots by a sign change of the integer polynomial 𝒫_l at
  two printed 21-decimal rationals, non-real roots by a Rouché criterion proved once (lem:is-disc, new) and checked per
  row at a printed 22-decimal centre. The count uses only the existing location lemmas of chapter 33. The two tables
  (1269 and 680 rows) are a new section sec:tab-is of chapter 96.
- **Step 2, the least excess.** For each root the reduction lemma lem:is-reduction is run on the printed interval; the
  tables print the minimising (p, q) and a lower bound. The least excess over all of Λ is
  μ_Z = ι_* + 356327𝔡₀ + 1116082𝔡₁ − 3 with ι_* the real root of P_390 near 2.152870531513212732616134, and
  1.6747856·10⁻¹⁷ < μ_Z < 1.6747859·10⁻¹⁷ (lem:is-gap-z, new, ι_* enclosed to 10⁻²⁴); the next is above 1.1076·10⁻¹⁵.
  So (G) ⟺ ε_K < μ_Z and (G⁺) ⟺ ε_+ < μ_Z (thm:is-gap, rewritten), and the choice ε_K = 1.6747·10⁻¹⁷,
  ε_+ = 1.67478·10⁻¹⁷ is admissible (def:uc-choice, lem:uc-admissible).
- **Step 3, the counts.** 1.85753·10¹⁴ < N_Λ ≤ 909,507,124,095,312 (prop:is-count (a), rewritten: Λ_ℬ contributes at
  most 1.67472·10¹³ as before, the 2629 families ι + p𝔡₀ + q𝔡₁ at most 8.9276·10¹⁴). k̄_0 = 3, J_* = 15,000,015,
  l_* = 50, η_0 = 𝔡₁ are unchanged, with reasons in section 3.
- **Also proved.** The lower bound for the index sets as constructed rises from 1.2497·10²⁴ to 1.2250·10²⁷ at every
  admissible choice (cor:is-lower, new; optional, see section 4). R-V-I11's census figures (56 elements in
  (3, 3 + 1.6416·10⁻¹⁴], 1144 in (3, 3 + 4.2·10⁻¹³]) are reproduced by the tables.
- **Not proved.** c_b at a rotating b; whether ℰ_ind can omit 𝔡₁; anything at another h. A lower bound for N_Λ that
  counts the real families as well (it would need ι − ι′ ∉ ℤ𝔡₀ + ℤ𝔡₁ for real roots; not needed for any bound).

## 2. Step 4

### 2.1 Omitting 𝔡₀

thm:is-d0 (c) at HEAD: an index set serving everywhere with 𝔡₀ ∉ π_1ℰ′_ind exists iff c_b(Ȧ) = 0 for every
b = (m, A) near b₀ and every Ȧ ∈ ker ad_A, c_b(Ȧ) being the coefficient of ρ^(2+𝔡₀) in
ω̇_b(0, Ȧ) = −(□^Υ_b)^(0)⁻¹η_b(0, Ȧ) (eq:iii-f3-2-1). It vanishes at A = 0 and on im ad_A, and is SO(4)-equivariant.
What blocks a decision:

1. *Symmetry does not force it.* The equivariance makes X ↦ c_b(X) a linear form −tr(X_A ·) with X_A ∈ ker ad_A and
   X_(OAOᵀ) = OX_AOᵀ. Writing 𝔰𝔬(4) = 𝔰𝔬(3)₊ ⊕ 𝔰𝔬(3)₋, these conditions allow X_A = φ₊(|A₊|, |A₋|)A₊ + φ₋(|A₊|, |A₋|)A₋
   with arbitrary φ_±, so nothing of the form "X_A is equivariant and commutes with A" kills it. The parity φ does not
   separate (the rotation corrections and the type s0 root 2 + 𝔡₀ are both even, lem:is-roots (c)); time reversal is
   not a symmetry of the gauge-fixed operator (the damping 1-form c = r⁻¹(dt − v dr) and t_* single out the future).
2. *It is a global quantity.* The coefficient of the homogeneous solution ρ^(2+𝔡₀) is not determined by the expansion
   at ∂X: it is fixed by solving the stationary s0 problem on the whole exterior, through the horizon modification
   c_(Υ,H) (whose parameter γ_(Υ,H) the paper does not fix). Even its first order in A, the s0 part of the coupling of
   the v1 rotation correction to the background rotation at order |x|⁻³ fed through (□^Υ_(b₀))^(0)⁻¹ at type s0, has no
   closed form in the paper; a nonzero first-order value would show the omission impossible, and vanishing would have
   to hold at every order.

So the omission stays conditional. What it would buy is now proved (cor:is-flat, T12): with ℰ′_ind, the elements of
Λ near 3 from Z₃ are ι + q𝔡₁ only, the least excess is μ♭_Z = (n⁺ + 1)𝔡₁ − y at the non-real root of P_700, with
3.548125563·10⁻¹⁰ < μ♭_Z < 3.548125564·10⁻¹⁰ (the next 4.2406·10⁻¹⁰ at l = 869), above ε_Υ; so (G) would cost
nothing beyond ε_K < ε_Υ, and 1,283,560,912 ≤ N_Λ ≤ 3,683,190,611. With P-UB2's scaling d_NM ≈ 2J′N̄²/(0.998ε_K), that
is about 2·7.65·10⁸·(3.683·10⁹)²/(1.459·10⁻¹⁰) ≈ 1.4·10³⁸ (ε_K just below ε_Υ, which Step 4 of prop:iii-i11-3-1 caps
at about 0.998ε_Υ), against about 7.6·10⁵⁵ for the index sets as constructed. Omitting 𝔡₁ instead (also undecided)
would give the analogous one-offset lattice in 𝔡₀; not evaluated.

### 2.2 Another computational point

Why h = 10⁻⁶: sec:ec-point and rem:ec-point-outside take the right end of the interval (0, 10⁻⁶] on which
prop:np-10-52 (iii) defines ε_ind and on which the paper's root lemmas are stated; at it every location, simplicity
and exceptional-set statement was proved (sec:s14-pa, sec:s14-exc-point), and it gives the fewest roots below 3 (the
degrees with roots below 3 run up to l ≈ h^(−1/2)). Numerically (60 digits, not proved), the least excess over the roots
in (2, 3) and Σ(3 − Re ι)² are:

| h | roots in (2, 3) | least excess | next | Σ(3 − Re ι)² |
|---|---|---|---|---|
| 1·10⁻⁶ | 2629 | 1.6748·10⁻¹⁷ | 1.1076·10⁻¹⁵ | 793.56 |
| 9.9·10⁻⁷ | 2642 | 7.7731·10⁻¹⁶ | 1.7811·10⁻¹⁵ | 797.32 |
| 9.8·10⁻⁷ | 2655 | 1.5451·10⁻¹⁶ | 3.1115·10⁻¹⁶ | 801.14 |
| 9.7·10⁻⁷ | 2668 | 8.6169·10⁻¹⁶ | 9.1666·10⁻¹⁶ | 805.02 |
| 9.6·10⁻⁷ | 2683 | 1.4605·10⁻¹⁵ | 2.0143·10⁻¹⁵ | 808.96 |
| 9.5·10⁻⁷ | 2696 | 7.0909·10⁻¹⁶ | 7.0909·10⁻¹⁶ | 812.96 |
| 9·10⁻⁷ | 2771 | 4.1155·10⁻¹⁶ | 1.2599·10⁻¹⁵ | 833.97 |
| 8·10⁻⁷ | 2939 | 6.5076·10⁻¹⁶ | 6.5076·10⁻¹⁶ | 881.79 |
| 5·10⁻⁷ | 3719 | 1.1925·10⁻¹⁵ | 1.2435·10⁻¹⁵ | 1103.61 |

(the "next" equal to the least is the conjugate of a non-real root). h = 10⁻⁶ is an unlucky point: at the other eight
values the least excess is 9 to 87 times larger, while Σ(3 − Re ι)², which fixes N_Λ, grows by at most 11% down to
8·10⁻⁷. As d_NM scales like N̄_Λ²/ε_K, the best of these, h = 9.6·10⁻⁷, would lower it by a factor of about 84. Not
done, because every statement at h = 10⁻⁶ would have to be re-proved: chapter 33 sec:s14-pa
(lem:s14-delta50 does not depend on h; lem:s14-vector-distance, lem:s14-scalar-zero, lem:s14-sextic-split,
lem:s14-sextic-count, cor:s14-remote-point, lem:s14-sextic-small, lem:s14-sextic-large, lem:s14-crossings,
prop:s14-damping-distance, cor:s14-eps-ind-point, rem:s14-eps-ind-scope) and sec:s14-exc-point (prop:t49-simple,
prop:t49-pairs, thm:t49-point, cor:t49-right); chapter 70 prop:rb-quasimode-point and the remark near 70:1696
(γ_C = 10⁶); chapter 71 def:ec-point, rem:ec-point-outside, prop:is-iota, prop:is-mult, sec:sp-point (lem:sp-roots,
lem:sp-exceptional, thm:sp-spectrum, cor:sp-lstar), and this file's sec:is texts; chapter 96 sec:tab-a (all five
tables), sec:tab-t49 (the discriminant and resultant tables) and the new sec:tab-is; besides, 03:316, 63:70, 90:72–80
name the point. Each would need a new proof at the new h, and the new h must avoid the countable exceptional sets.

## 3. Why k̄_0, J_*, l_* and η_0 do not change

η_0 and J_* = ⌈5/η_0⌉ + 2 read the increments π_1(ℰ_ind ∪ ℰ^ι_ind) ∪ {1}; the repair adds the generator 1 + 𝒵 and no
increment. l_* bounds logarithmic orders of ℰ_ind ∪ ℰ^ι_ind ∪ ℰ^C_I, pole orders and multiplicities, none of which
involves Λ. k̄_0 bounds ℰ⁰_src ∪ ℰ_++ ∪ 𝒢 ∪ (2 + ℰ_col) below 2λ_♯; there ℰ⁰_src = 𝒢 ∪ (ℰ_rows ∩ {Re < 2}) and the
new rows (s1, 1 + μ, k) have λ = 1 + μ of real part above 2 + 2.9·10⁻⁶, so ℰ_rows ∩ {Re < 2} is unchanged, and
Λ ∩ {Re < 2} = π_1ℳ is unchanged (lem:iii-i10-1-2 (a) after V-I11 §4.4). So prop:is-count (b), (c) and cor:sp-lstar
stand as written, and N_Λ is the only count that moves.

## 4. Merge notes

- **Order and overlaps.** T1–T13 are in chapter 71, T14 in chapter 96; they are pairwise disjoint and may be applied in
  any order. They overlap none of P-UB2's blocks (its M1–M26, O1–O4, F1–F9, FO1–FO7): P-UB2's M8 covers thm:uc-reduction
  (iii), so this file has no text there.
- **Merged together with P-UB2's main set** (M1–M26, O1–O4) on a scratch copy, lint.py --chapters and assemble.py report
  0 problems, and lint.py --paper finds four lines over 121 characters after the labels resolve, all in P-UB2's texts
  and the same four with P-UB2's texts alone: in M6 (rem:ec-upper-open, the line "[[prop:cs-cstar]] bounds it by
  C_* < …"), M7 (sec:uc-close, the line "exponents of the index sets as constructed, and [[sec:sp]] …") and M13
  (rem:uc-missing, the lines "through the generators 1 + 𝒵 ([[prop:is-ind]], …" and "The single-step losses are
  bounded in [[sec:cs]], …"). They need rewrapping at merge (for P-UB2); nothing in this file's texts does.
- **V-I11 §5.1–5.4 must not be applied** together with these texts: they are the interim versions of T1 (rem:gap-sums),
  T7 (prop:is-lambda) and T8–T9 (thm:is-gap, its lem:is-gap-z and rem:is-gap-z); this file replaces them. The label
  lem:is-gap-z is reused here for the proved lemma; V-I11's rem:is-gap-z (a numerical observation) is not needed and
  does not appear. V-I11 §5.5 is superseded by P-UB2's M1, O1–O4.
- **Dependence on P-I11.** T1, T2, T7, T13 cite "the generator 1 + 𝒵 of [[def:iii-i10-1-1]]"; if P-I11 names the set
  differently, those four texts take its name.
- **cor:is-lower is optional.** It raises a lower bound that the brief keeps; if it is not wanted, drop it from T9 (the
  last paragraph) and drop the clause "and it raises the lower bound … ([[cor:is-lower]])" from T2. Nothing else cites
  it. If it is kept, thm:uc-integer's eq:uc-lower and the summaries that quote 1.2497·10²⁴ could cite it; that is P-UB2's
  and the coordinator's choice.
- **eq:is-mu** keeps its label and its display (μ_G, now the least excess of the part Λ_ℬ); the new threshold is
  eq:is-mu-z. Sites that cite eq:is-mu for the admissible ε_K at HEAD (lem:uc-admissible) are rewritten here (T5).

## 5. Placement

This part and the crosswalk rows are instructions for merging; they are not chapter text. Each old text is quoted
exactly between the fences, and each new text replaces it as a whole, with the line breaks shown. The line numbers are
those of the chapters at HEAD (md5s above) and serve only to find the place. Equation labels are right-aligned so that
no line exceeds 121 characters, also after the labels resolve.

### T1. rem:gap-sums, its last sentence, 71-explicit-constants.md lines 169–170

Old (2 lines):

```old
[[lem:sp-roots]] use the bounds on the offsets that its proof gives. For the index sets as the proofs construct them, Λ
contains further sums, and (G) holds exactly for ε_K < μ_G ≈ 1.6416·10⁻¹⁴ ([[thm:is-gap]]).
```

New (4 lines):

```new
[[lem:sp-roots]] use the bounds on the offsets that its proof gives. For the index sets as the proofs construct them, Λ
contains further sums and the elements that the generator 1 + 𝒵 of [[def:iii-i10-1-1]] produces, and (G) holds
exactly for ε_K < μ_Z ≈ 1.6748·10⁻¹⁷ ([[thm:is-gap]]); on the part of Λ built from the other generators the least
excess above 3 is μ_G ≈ 1.6416·10⁻¹⁴.
```

### T3. def:uc-choice, the display eq:uc-choice, 71-explicit-constants.md lines 2587–2587

Old (1 lines):

```old
    ε_Υ := 1.4619·10⁻¹⁰,     ε_K := 1.6416·10⁻¹⁴,     ε_+ := 1.64160217·10⁻¹⁴,     l_* := 50,     k̄_0 := 3.
```

New (1 lines):

```new
    ε_Υ := 1.4619·10⁻¹⁰,     ε_K := 1.6747·10⁻¹⁷,     ε_+ := 1.67478·10⁻¹⁷,     l_* := 50,     k̄_0 := 3.
```

### T4. lem:uc-admissible, the display eq:uc-deltas, 71-explicit-constants.md lines 2604–2604

Old (1 lines):

```old
    Δβ_0 := 0.999²ε_K = 1.6383184416·10⁻¹⁴,     Δτ_0 := 0.999ε_Υ = 1.4604381·10⁻¹⁰.                    {#eq:uc-deltas}
```

New (1 lines):

```new
    Δβ_0 := 0.999²ε_K = 1.6713522747·10⁻¹⁷,     Δτ_0 := 0.999ε_Υ = 1.4604381·10⁻¹⁰.                    {#eq:uc-deltas}
```

### T5. lem:uc-admissible, proof: the constants, (G) and (G⁺), 71-explicit-constants.md lines 2610–2615

Old (6 lines):

```old
0 < ε_K < ε_+ < min(δ_♯, ε_ind), and 1.6416·10⁻¹⁴ < 1.64160217·10⁻¹⁴ < 1.9413·10⁻⁸ < δ_50, while
δ_♯ = λ_♯ − 3/2 = 0.0099. *(G).* By [[thm:is-gap]], for the set Λ that [[def:iii-i10-1-1]] builds from the index sets
of [[def:uc-choice]], (G) holds if and only if ε_K < μ_G, and μ_G > 1.64160217197·10⁻¹⁴ > 1.6416·10⁻¹⁴ = ε_K by
[[eq:is-mu]]. Also ε_K < ε_Υ, as [[def:iii-i10-1-3]] asks. *(G⁺) and the exactness conditions.* By [[thm:is-gap]] and
its proof, λ_♯ + 1109655𝔡₀ + 31682𝔡₁ = 3 + μ_G has the least real part above 3 of the elements of Λ, and
ε_+ < 1.64160217197·10⁻¹⁴ < μ_G ([[eq:is-mu]]); so no λ ∈ Λ has real part in (3, 3 + ε_+], which is (G⁺) of
```

New (6 lines):

```new
0 < ε_K < ε_+ < min(δ_♯, ε_ind), and 1.6747·10⁻¹⁷ < 1.67478·10⁻¹⁷ < 1.9413·10⁻⁸ < δ_50, while
δ_♯ = λ_♯ − 3/2 = 0.0099. *(G).* By [[thm:is-gap]], for the set Λ that [[def:iii-i10-1-1]] builds from the index sets
of [[def:uc-choice]], (G) holds if and only if ε_K < μ_Z, and μ_Z > 1.6747856·10⁻¹⁷ > 1.6747·10⁻¹⁷ = ε_K by
[[eq:is-mu-z]]. Also ε_K < ε_Υ, as [[def:iii-i10-1-3]] asks. *(G⁺) and the exactness conditions.* By [[thm:is-gap]],
ι_* + 356327𝔡₀ + 1116082𝔡₁ = 3 + μ_Z has the least real part above 3 of the elements of Λ, and
ε_+ = 1.67478·10⁻¹⁷ < μ_Z ([[eq:is-mu-z]]); so no λ ∈ Λ has real part in (3, 3 + ε_+], which is (G⁺) of
```

### T6. lem:uc-admissible, proof: ε and α, 71-explicit-constants.md lines 2625–2627

Old (3 lines):

```old
δ₄ + ℓ_3 + 2ε < ε_g, where ℓ_3 = α − 4 − ε < ε_K; it exists, as ε_K + ε ≤ 1.6416·10⁻¹⁴ + 1.4619·10⁻¹³ < ε_g. *α.* An
admissible α ≥ 3 is a number in (4 + ε_K − ε′_0, 4 + ε_K], ε′_0 = ½ min(ε_K, ε_+ − ε_K) = ½(ε_+ − ε_K) =
1.085·10⁻²⁰, off a finite set ([[def:iii-i10-1-3]]), and (A_J), (Ex3) and (Ex4) exclude finitely many more
```

New (3 lines):

```new
δ₄ + ℓ_3 + 2ε < ε_g, where ℓ_3 = α − 4 − ε < ε_K; it exists, as ε_K + ε ≤ 1.6747·10⁻¹⁷ + 1.4619·10⁻¹³ < ε_g. *α.* An
admissible α ≥ 3 is a number in (4 + ε_K − ε′_0, 4 + ε_K], ε′_0 = ½ min(ε_K, ε_+ − ε_K) = ½(ε_+ − ε_K) =
4·10⁻²², off a finite set ([[def:iii-i10-1-3]]), and (A_J), (Ex3) and (Ex4) exclude finitely many more
```

### T2. sec:is, the opening paragraph after the list of results, 71-explicit-constants.md lines 2834–2846

Old (13 lines):

```old
([[rem:is-summary]]). From these it determines Λ ∩ {Re ≤ 3 + ε_+} ([[prop:is-lambda]]); it shows that (G) holds
exactly for ε_K < μ_G, where

    1.64160217197·10⁻¹⁴ < μ_G < 1.64160217198·10⁻¹⁴                                                   {#eq:is-mu}

([[thm:is-gap]]); and it gives 1.62066·10¹³ < N_Λ < 1.67472·10¹³, k̄_0 = 3 and J_* = 15,000,015 ([[prop:is-count]]).
Finally it decides when ℰ_ind can omit 𝔡₀ ([[thm:is-d0]]): an admissible ℰ_ind that omits 𝔡₀ exists if and
only if one explicit family of coefficients c_b vanishes at every b near b₀; c_b vanishes at b₀, at every
non-rotating b and on the image of ad_(A(b)), and this paper does not determine it elsewhere. If c_b vanishes, (G)
holds for every ε_K < 5.0190·10⁻⁸, so for every ε_K that [[eq:iii-i9-1-1]] allows ([[cor:is-flat]]). Whether an
admissible ℰ_ind can omit 𝔡₁ is not decided either. Neither question enters an upper bound for the loss d: the index
sets as constructed serve with every ε_K < μ_G, and the two questions decide only whether smaller index sets, with a
larger ε_K, are available.
```

New (18 lines):

```new
([[rem:is-summary]]). It locates, each to within 10⁻²¹, the 2629 elements of real part below 3 of the set Z of
[[prop:is-iota]], which enter Λ through the generator 1 + 𝒵 of [[def:iii-i10-1-1]] ([[lem:is-z3]], [[sec:tab-is]]). From
these it determines Λ ∩ {Re ≤ 3 + ε_+} ([[prop:is-lambda]]); it shows that (G) holds exactly for ε_K < μ_Z, and (G⁺)
exactly for ε_+ < μ_Z, where μ_Z := ι_* + 356327𝔡₀ + 1116082𝔡₁ − 3, ι_* being a real root of P_390 near 2.1528705,
satisfies 1.6747856·10⁻¹⁷ < μ_Z < 1.6747859·10⁻¹⁷ ([[lem:is-gap-z]], [[thm:is-gap]]); on the part Λ_ℬ of Λ built
from the other generators the least excess above 3 is μ_G, with

    1.64160217197·10⁻¹⁴ < μ_G < 1.64160217198·10⁻¹⁴.                                                  {#eq:is-mu}

It gives 1.85753·10¹⁴ < N_Λ ≤ 909,507,124,095,312, k̄_0 = 3 and J_* = 15,000,015 ([[prop:is-count]]), and it raises the
lower bound for d_acc at every admissible choice of the weights to 1.2250·10²⁷ ([[cor:is-lower]]). Finally it decides
when ℰ_ind can omit 𝔡₀ ([[thm:is-d0]]): an admissible ℰ_ind that omits 𝔡₀ exists if and only if one explicit family of
coefficients c_b vanishes at every b near b₀; c_b vanishes at b₀, at every non-rotating b and on the image of ad_(A(b)),
and this paper does not determine it elsewhere. If c_b vanishes, (G) holds exactly for ε_K < μ♭_Z, where
3.548125563·10⁻¹⁰ < μ♭_Z < 3.548125564·10⁻¹⁰, so for every ε_K that [[def:iii-i10-1-3]] allows, and N_Λ ≤ 3,683,190,611
([[cor:is-flat]]). Whether an admissible ℰ_ind can omit 𝔡₁ is not decided either. Neither question enters an upper bound
for the loss d: the index sets as constructed serve with every ε_K < μ_Z, and the two questions decide only whether
smaller index sets, with a larger ε_K and a smaller N_Λ, are available.
```

### T7. new sec:is-z (lem:is-disc, lem:is-z3) and the new prop:is-lambda, 71-explicit-constants.md lines 3214–3232

Old (19 lines):

```old
#### The set Λ below 3 + ε_+ {#sec:is-lambda}

**Proposition {#prop:is-lambda}** (Λ ∩ {Re ≤ 3 + ε_+}.) Let ℬ be the set of the 29 numbers

    λ_♯,   λ_♯ + 1 + δ′₁,   λ_♯ + 1 + δ₂,   2 + c (c ∈ σ^(2)),   5/2 + c (c ∈ σ^(3)),   3.

Then, for ε_+ < δ̄, Λ ∩ {Re ≤ 3 + ε_+} = {β + p𝔡₀ + q𝔡₁ ≤ 3 + ε_+ : β ∈ ℬ, p, q ∈ ℕ₀}. All its elements are real.

*Proof.* By [[def:iii-i10-1-1]], Λ is the set of g + w₁ + … + w_s and their conjugates, with g a generator and w_i
increments. Every generator and increment has real part at least λ_♯ > 3/2, resp. 𝔡₁ > 0, so below 3 + ε_+ only
generators below 3 + ε_+ and increments below 3 + ε_+ − λ_♯ < 1.5 enter, and all of these are real. The generators
there: π_1ℰ_++ gives λ_♯ plus increments ([[prop:is-ci-pp]] (b)); π_1𝒢 = {2} ∪ (2 + π_1ℰ_ind) + ℕ₀ gives 2 plus
increments; π_1ℰ^C_I gives 2 + c, 5/2 + c and 3 ([[prop:is-ci-pp]] (a)); λ_♯ and 3; and 2 + π_1ℰ_col ⊂ π_1𝒢 + ℕ₀.
The increments below 1.5 are those of [[eq:is-low]] ([[prop:is-ind]], [[prop:is-iota]]) and 1, each a sum of 𝔡₀, 𝔡₁,
1, 1 + δ′₁ and 1 + δ₂. A sum with an
increment of real part at least 1 added to a generator other than λ_♯ is at least 3, with equality only for 2 + 1;
added to λ_♯ it is λ_♯ + 1, λ_♯ + 1 + δ′₁ or λ_♯ + 1 + δ₂ plus 𝔡₀'s and 𝔡₁'s, and λ_♯ + 1 = 5/2 + a. Two such
increments give at least λ_♯ + 2. So every element below 3 + ε_+ is β + p𝔡₀ + q𝔡₁ with β ∈ ℬ, and each such sum lies
in Λ. ∎
```

New (128 lines):

```new
#### The elements of Z of real part below 3 {#sec:is-z}

The generator 1 + 𝒵 of [[def:iii-i10-1-1]] puts into Λ the numbers 1 + μ for the indicial roots μ of L̂_b(0) with
0 < Re μ < 3. At the computational point these numbers are 3 and the ι ∈ Z of [[prop:is-iota]] with Re ι < 4
([[prop:is-lambda]]), and those with Re ι < 3 give elements of Λ below 3 + ε_+. This subsection locates them, each to
within 10⁻²¹: the real ones by changes of sign at printed rationals, the non-real ones by the criterion of
[[lem:is-disc]] at printed centres; the data are the two tables of [[sec:tab-is]]. For l ≥ 1 we write
𝒫_l := 64·10¹⁸P_l = Σ_(k=0)^6 π_k(κ)ι^k, κ = l(l + 2), with the integer coefficients π_k of [[sec:tab-a-sextic]], and
𝒫_0 := 102400·10¹²C, so that, by [[eq:s14-c0]] at the computational point,

    𝒫_0(ι) = −102400ι³ − 307198795200ι² − 204794385598692800ι + 409605307200000000.                   {#eq:is-c-int}

**Lemma {#lem:is-disc}** (A simple root in a disc.) Let P be a polynomial, c ∈ ℂ, r > 0, and M ≥ |P″(ι)| for every
ι with |ι − c| ≤ r. If |P(c)| + Mr²/2 < r|P′(c)|, then P has exactly one root in the open disc |ι − c| < r, and it is
simple. This holds in particular if |Re P(c)| + |Im P(c)| + Mr²/2 < r max(|Re P′(c)|, |Im P′(c)|).

*Proof.* Put L(ι) := P(c) + P′(c)(ι − c). By Taylor's formula with integral remainder,
P(ι) − L(ι) = (ι − c)² ∫₀¹ (1 − t)P″(c + t(ι − c)) dt, so |P − L| ≤ Mr²/2 on the circle |ι − c| = r, where the
modulus of L is at least r|P′(c)| − |P(c)| > Mr²/2. By Rouché's theorem P and L have the same number of roots in the
open disc, counted with multiplicity, and L has exactly one, c − P(c)/P′(c), as |P(c)| < r|P′(c)|. The last assertion
follows from the inequalities |w| ≤ |Re w| + |Im w| and |w| ≥ max(|Re w|, |Im w|). ∎

**Lemma {#lem:is-z3}** (The elements of Z of real part below 3.) Let Z be the set of [[prop:is-iota]] and
Z₃ := {ι ∈ Z : Re ι < 3}.

(a) Every ι ∈ Z with Re ι ≥ 3 has Re ι > 3 + 4.99·10⁻⁶.

(b) Z₃ has 2629 elements, 1269 real and 1360 non-real. For each row (l, j, r) of the first table of [[sec:tab-is]],
𝒫_l takes values of opposite signs at r and at r + 10⁻²¹, and the interval (r, r + 10⁻²¹) contains exactly one root of
𝒫_l; for each row (l, a, b) of the second table, the disc |ι − (a + ib)| < 10⁻²¹ contains exactly one root of 𝒫_l,
and this root is not real. Z₃ consists of these 1269 real roots, these 680 non-real roots and their conjugates.

(c) The first table has one row for l = 0, two for l = 1, three for each 2 ≤ l ≤ 135 and one for each
136 ≤ l ≤ 999; the second has one row for each 136 ≤ l ≤ 815. Every ι ∈ Z₃ has 2 + 2.932·10⁻⁶ < Re ι < 3 − 1.439·10⁻⁵,
and every non-real ι ∈ Z₃ has Re ι > 2.514.

*Proof.* *The polynomials.* By [[prop:is-iota]], Z consists of the root of C greater than 2, the roots ι ≠ 2 of real
part greater than 19/10 of the P_l, l ≥ 1, and the larger roots ι_v of p_(v), l ≥ 2. By [[prop:np-10-54]] (i), (ii) and
its proof, C has exactly one root of real part greater than 19/10, and each P_l, l ≥ 1, exactly three, counted with
multiplicity, among them 2 when l = 1.

*The vector type.* By [[lem:s14-vector-distance]], ι_v = (Γ + (l + 1)²)^(1/2) − 499999 with Γ = 250002000000, which
increases with l. At l = 2, (500002 + 4.99·10⁻⁶)² = 250002000008.9900199… < 250002000009 = Γ + 9; so
ι_v > 3 + 4.99·10⁻⁶ for every l ≥ 2.

*The rows.* For a row of the first table, 10¹²⁶𝒫_l(r) and 10¹²⁶𝒫_l(r + 10⁻²¹) (10⁶³𝒫_0(r) and 10⁶³𝒫_0(r + 10⁻²¹) when
l = 0) are integers, and in every row their signs differ; so the interval holds a real root of P_l (of C when l = 0).
For a row of the second table put c := a + ib. In every row a < 3 and b < 3, so |ι| < 6 on the disc. For 1 ≤ l ≤ 815,
0 < κ ≤ 665855, and the coefficients of [[sec:tab-a-sextic]] give |π₂(κ)| ≤ 192κ² + 319992327003268κ +
895982956005094002579 < 1.10914·10²¹, |π₃(κ)| < 127994763015010999375 and |π₄(κ)| < 319994650002515; so on |ι| ≤ 6

    |𝒫_l″(ι)| ≤ 2|π₂(κ)| + 36|π₃(κ)| + 432|π₄(κ)| + 4320|π₅| + 38880|π₆|
              < 2.2183·10²¹ + 4.6079·10²¹ + 1.4·10¹⁷ + 1.2·10¹² + 3·10⁶ < 7·10²¹.

With M = 7·10²¹ and r = 10⁻²¹, so that Mr²/2 = 3.5·10⁻²¹, every row satisfies the last condition of [[lem:is-disc]]
for 𝒫_l: 10¹³²𝒫_l(c) and 10¹¹⁰𝒫_l′(c) are Gaussian integers, and in every row

    |Re 𝒫_l(c)| + |Im 𝒫_l(c)| + 3.5·10⁻²¹ < 10⁻²¹ max(|Re 𝒫_l′(c)|, |Im 𝒫_l′(c)|).

So the disc holds exactly one root of P_l. As b > 10⁻²¹ the disc lies in {Im ι > 0}, and the root is not real; its
conjugate is a root in the conjugate disc, P_l having real coefficients.

*Counting.* For each l the intervals and discs of its rows, with the conjugate discs, are pairwise disjoint (their
printed numbers differ by more than 2·10⁻²¹), lie in {2 < Re ι < 3}, and do not contain 2. So they hold distinct roots
of real part greater than 19/10, other than 2: one for l = 0; two for l = 1; three for 2 ≤ l ≤ 815 (for
136 ≤ l ≤ 815 a real root and a conjugate pair); one for 816 ≤ l ≤ 999. By the counts above, for l ≤ 815 every root of
C and of P_l of real part greater than 19/10, other than 2, lies in exactly one of these intervals and discs.

*The other roots of P_l.* Let l ≥ 816, so that x = hκ ≥ 0.667488. For l ≤ 8365, x ≤ 70, and [[lem:s14-sextic-large]]
gives the three roots of P_l of real part greater than 19/10 as ι_B, real, and ι_P, ῑ_P, not real ((c) there, as
x ≥ 0.03). By [[lem:s14-sextic-split]] (v), |Π − Π⁰| < 0.57 on [0, 35], and the convex quadratic Π⁰ is below −79.6
there, its values at 0 and at 35 being below −79.6 and −423; so Π < 0 on [0, 35]. For x ∈ [0.667488, 4] the row [0.5, 4]
of [[sec:tab-a-pieces]] gives e_P ≤ 11h, so Re ι_P ≥ a(x) − hΠ(x)/2 − e_P > a(x) − 11h, where
a(x) − 3 = 3(x − 2/3)/4 ≥ 6.16·10⁻⁴; so Re ι_P > 3 + 6·10⁻⁴. For x ∈ [4, 70], a(x) ≥ 11/2 and
h|Π(x)|/2 + e_P ≤ h(1990 + 4.17)/2 + 72h < 0.0011, so Re ι_P > 5.49. For x ≥ 1.002, that is l ≥ 1000, (a) there and the
rows of [[sec:tab-a-pieces]] give ι_B ≥ 2 + x − hc(x) − e_B, which is at least 3.002 − 39.004h > 3.0019 for x ≤ 4, at
least 6 − 321.1h for 4 ≤ x ≤ 16, and at least 18 − 5184h for 16 ≤ x ≤ 70. For l ≥ 8365, [[cor:t49-right]] gives three
roots of real part greater than 51. So for 816 ≤ l ≤ 999 the root in the interval of the first table, being real, is
ι_B, and the two other roots of real part greater than 19/10 have real part greater than 3 + 6·10⁻⁴; for l ≥ 1000 all
three have real part greater than 3 + 6·10⁻⁴.

*Conclusion.* In every row r + 10⁻²¹ < 3, resp. a + 10⁻²¹ < 3, so the roots of the tables lie in Z₃; every other element
of Z has real part greater than 3 + 4.99·10⁻⁶, by the last two steps and the vector type. This gives (a) and (b), the
counts of (b) being those of the rows. (c) is read off the tables: the least r is 2.000002932350446240725, at l = 2; the
numbers r + 10⁻²¹ and a + 10⁻²¹ are below 2.99998561, the largest being at l = 999; and every a exceeds 2.5141162, the
least being at l = 136. ∎

#### The set Λ below 3 + ε_+ {#sec:is-lambda}

**Proposition {#prop:is-lambda}** (Λ ∩ {Re ≤ 3 + ε_+}.) Let ℬ be the set of the 29 numbers

    λ_♯,   λ_♯ + 1 + δ′₁,   λ_♯ + 1 + δ₂,   2 + c (c ∈ σ^(2)),   5/2 + c (c ∈ σ^(3)),   3,

let Λ_ℬ be the smallest set, closed under conjugation, that contains the generators of [[def:iii-i10-1-1]] other than
1 + 𝒵 and satisfies Λ_ℬ + w ⊂ Λ_ℬ for every increment w of that definition, and for ι ∈ Z₃ ([[lem:is-z3]]) put
y_ι := 3 − Re ι. Then, for ε_+ < δ̄,

    Λ_ℬ ∩ {Re ≤ 3 + ε_+} = {β + p𝔡₀ + q𝔡₁ ≤ 3 + ε_+ : β ∈ ℬ, p, q ∈ ℕ₀},
    Λ ∩ {Re ≤ 3 + ε_+} = (Λ_ℬ ∩ {Re ≤ 3 + ε_+}) ∪ {ι + p𝔡₀ + q𝔡₁ : ι ∈ Z₃, p, q ∈ ℕ₀, p𝔡₀ + q𝔡₁ ≤ y_ι + ε_+}.

The elements of Λ_ℬ ∩ {Re ≤ 3 + ε_+} are real; ι + p𝔡₀ + q𝔡₁ is real exactly when ι is, and the non-real ones have
real part greater than 2.514. Every element of Λ of real part at most 2.514 is real, and every element of Λ ∖ Λ_ℬ has
real part greater than 2 + 2.932·10⁻⁶.

*Proof.* By [[def:iii-i10-1-1]], Λ is the set of the g + w₁ + … + w_s and their conjugates, with g a generator and w_i
increments; Λ_ℬ is the set of those with g a generator of Λ_ℬ, and their conjugates. Every generator of Λ_ℬ and
every increment has real part at least λ_♯ > 3/2, resp. 𝔡₁ > 0, so below 3 + ε_+ only such generators below 3 + ε_+
and increments below 3 + ε_+ − λ_♯ < 1.5 enter, and all of these are real. The generators there: π_1ℰ_++ gives λ_♯
plus increments ([[prop:is-ci-pp]] (b)); π_1𝒢 = {2} ∪ (2 + π_1ℰ_ind) + ℕ₀ gives 2 plus increments; π_1ℰ^C_I gives
2 + c, 5/2 + c and 3 ([[prop:is-ci-pp]] (a)); λ_♯ and 3; and 2 + π_1ℰ_col ⊂ π_1𝒢 + ℕ₀. The increments below 1.5 are
those of [[eq:is-low]] ([[prop:is-ind]], [[prop:is-iota]]) and 1, each a sum of 𝔡₀, 𝔡₁, 1, 1 + δ′₁ and 1 + δ₂. A sum
with an increment of real part at least 1 added to a generator other than λ_♯ is at least 3, with equality only for
2 + 1; added to λ_♯ it is λ_♯ + 1, λ_♯ + 1 + δ′₁ or λ_♯ + 1 + δ₂ plus 𝔡₀'s and 𝔡₁'s, and λ_♯ + 1 = 5/2 + a. Two such
increments give at least λ_♯ + 2. So every element of Λ_ℬ below 3 + ε_+ is β + p𝔡₀ + q𝔡₁ with β ∈ ℬ, and each such sum
lies in Λ_ℬ.

*The generator 1 + 𝒵.* At the computational point (C1) holds (the proof of [[prop:is-mult]]), and by
[[prop:iii-f1-2-3]] the indicial roots of L̂_b(0) of real part in (0, 3) are 2 and the ι^C_(·,+) − 1 of real part
below 3: in its list the other entries after the semicolons are integers at least 3 or numbers 1 + ι^Υ of real part
greater than 3, the root 3 of □^C at vector type 1 is removed there, and the entries before the semicolons have real
part at most 0. The ι^C_(·,+) are the elements of Z. So 1 + 𝒵 = {3} ∪ {ι ∈ Z : Re ι < 4}, and 3 ∈ ℬ. Let ι ∈ Z with
Re ι < 4. If Re ι ≥ 3, then Re ι > 3 + 4.99·10⁻⁶ > 3 + ε_+ ([[lem:is-z3]] (a)), and so is every g + w₁ + … + w_s with
g = ι. If Re ι < 3, then ι ∈ Z₃ and Re ι > 2 + 2.932·10⁻⁶ ([[lem:is-z3]] (c)); an increment of real part at least 1
then gives real part greater than 3 + 2.932·10⁻⁶ > 3 + ε_+, and the increments of real part below 1 are 𝔡₀ and 𝔡₁
([[eq:is-low]], [[prop:is-iota]]). So the sums with g = ι of real part at most 3 + ε_+ are the ι + p𝔡₀ + q𝔡₁ with
p𝔡₀ + q𝔡₁ ≤ y_ι + ε_+, and each lies in Λ, as 𝔡₀ and 𝔡₁ are increments ([[prop:is-ind]]). Z₃ is closed under
conjugation, the polynomials having real coefficients, and 𝔡₀ and 𝔡₁ are real; so the conjugates add nothing. The
statements on real parts follow from [[lem:is-z3]] (a), (c). ∎
```

### T8. new lem:is-gap-z; thm:is-gap, statement and first lines of the proof, 71-explicit-constants.md lines 3250–3262

Old (13 lines):

```old
**Theorem {#thm:is-gap}** (The admissible ε_K.) For Λ of [[prop:is-lambda]] (ℰ_ind and ℰ^ι_ind as constructed), (G)
of [[def:iii-i10-1-3]] holds if and only if ε_K < μ_G, where

    μ_G := λ_♯ + 1109655𝔡₀ + 31682𝔡₁ − 3

satisfies [[eq:is-mu]]. The next smallest excesses are 2.3181480·10⁻¹⁴ (above 3, from λ_♯ + 1 + δ′₁) and
8.0959353·10⁻¹⁴ (from λ_♯ + 1 + δ₂); every other element of Λ ∪ (Λ + 𝔡₀) ∪ (Λ + 𝔡₁) lies outside (2, 2 + 4.2·10⁻¹³]
∪ (3, 3 + 4.2·10⁻¹³]. As μ_G < δ_50 = ε_ind and μ_G < ε_Υ for the admissible choice ε_Υ = 1.4619·10⁻¹⁰ of
[[lem:ec-gauge-gap]], the other conditions of [[def:iii-i10-1-3]] on ε_K leave every ε_K ∈ (0, μ_G) available for a
suitable ε_+, and ε_K = 1.6416·10⁻¹⁴ is admissible.

*Proof.* *The windows.* By [[prop:is-lambda]] every element of Λ below 3 + 10⁻⁸ is β + p𝔡₀ + q𝔡₁ with β ∈ ℬ. As 𝔡₀ and
𝔡₁ are increments, Λ + 𝔡₀ and Λ + 𝔡₁ lie in Λ, so the third window of (G) is contained in the first. An element in
```

New (62 lines):

```new
**Lemma {#lem:is-gap-z}** (The least excesses of Z₃.) For ι ∈ Z₃ ([[lem:is-z3]]) let y_ι := 3 − Re ι, and let m be
the function of [[lem:is-reduction]]. Let ι_* be the root of P_390 in (r_*, r_* + 10⁻²⁴), where
r_* := 2.152870531513212732616134. Then

    m(y_(ι_*)) = μ_Z := ι_* + 356327𝔡₀ + 1116082𝔡₁ − 3,      1.6747856·10⁻¹⁷ < μ_Z < 1.6747859·10⁻¹⁷,      {#eq:is-mu-z}

and m(y_ι) ≥ 1.1076·10⁻¹⁵ for every other ι ∈ Z₃. Moreover, if ι ∈ Z₃ and p, q ∈ ℕ₀ satisfy
0 < p𝔡₀ + q𝔡₁ − y_ι < 1.1076·10⁻¹⁵, then ι = ι_*, p = 356327 and q = 1116082.

*Proof.* *The rows.* For a row (l, j, r) of the first table of [[sec:tab-is]], y_ι lies in (3 − r − 10⁻²¹, 3 − r); for
a row (l, a, b) of the second, y_ι and y_ῑ lie in (3 − a − 10⁻²¹, 3 − a + 10⁻²¹) ([[lem:is-z3]] (b)). In every row,
dividing the two ends of this interval by the bounds for 𝔡₁ and for 𝔡₀/4 of [[lem:is-offsets]] (b) gives the same
integer parts at both ends; so n⁺ = ⌊y_ι/𝔡₁⌋ and n⁻ = ⌊4y_ι/𝔡₀⌋ are determined, n⁺ − n⁻ ≤ 2, and y_ι/𝔡₁ and 4y_ι/𝔡₀
are not integers. For each integer n with n⁻ < n ≤ n⁺, dividing the ends of the interval for θ_n = y_ι − n𝔡₁ by the
bounds for ε₀ gives the same integer part, so p_n is determined. [[lem:is-reduction]] then gives m(y_ι) as the least
of at most three numbers, each bounded from below and from above by the bounds of [[lem:is-offsets]] (b). In every row
the least of them is attained at the printed pair (p, q) (with p = 0 and q = n⁺ + 1 when it is (n⁺ + 1)𝔡₁ − y_ι), it is
at least the printed number m, and the others are larger than m. Every printed m is at least 1.1076·10⁻¹⁵, except in
the row l = 390, j = 1 of the first table, whose m is 1.6747·10⁻¹⁷, at (p, q) = (356327, 1116082).

*The root ι_*.* With the coefficients of [[sec:tab-a-sextic]] at κ = 390·392 = 152880,

    𝒫_390(ι) = −64ι⁶ − 255998991ι⁵ − 319994620649555ι⁴ − 127994684740759511215ι³
               + 944903378469873089619ι² − 2546096242636821502034ι + 2379096657426967221840,

and 10¹⁴⁴𝒫_390(r_*) and 10¹⁴⁴𝒫_390(r_* + 10⁻²⁴) are integers, with 𝒫_390(r_*) > 2.155·10⁻⁴ and
𝒫_390(r_* + 10⁻²⁴) < −4.17·10⁻⁵. So P_390 has a root in (r_*, r_* + 10⁻²⁴); this interval lies in the interval of the
row l = 390, j = 1, which holds exactly one root ([[lem:is-z3]] (b)); so ι_* is the element of Z₃ of that row. Then
y_(ι_*) lies in (0.847129468486787267383865, 0.847129468486787267383866), and the reduction there has n⁺ = 2541390 and
n⁻ = 2541389, the single n = 2541390, and θ_n/ε₀ ∈ (356326, 356327), so p_n = 356327 and n − 4p_n = 1116082; the other
number of the minimum is 2541391𝔡₁ − y_(ι_*) > 1.35·10⁻⁷. By [[lem:is-offsets]] (b), multiplying the bounds exactly,

    0.4751024555101136205980347542 < 356327𝔡₀ < 0.4751024555101136205980347550,
    0.3720270129766736635336878158 < 1116082𝔡₁ < 0.3720270129766736635336889319,

so 0.84712946848678728413172257 < 356327𝔡₀ + 1116082𝔡₁ < 0.84712946848678728413172369, and subtracting the bounds
for y_(ι_*) gives μ_Z ∈ (1.674785657·10⁻¹⁷, 1.674785869·10⁻¹⁷), which is [[eq:is-mu-z]]; it is the least of the two
numbers, so m(y_(ι_*)) = μ_Z.

*The last assertion.* By the proof of [[lem:is-reduction]], a positive number p𝔡₀ + q𝔡₁ − y with n := 4p + q ≤ n⁺
is at least p_nε₀ − θ_n, with equality only for p = p_n, and otherwise exceeds ε₀ > 5.5·10⁻¹³; one with n > n⁺ is at
least (n⁺ + 1)𝔡₁ − y, with equality only for (p, q) = (0, n⁺ + 1). So every positive number p𝔡₀ + q𝔡₁ − y_ι below
1.1076·10⁻¹⁵ is one of the numbers of the minimum of [[lem:is-reduction]] for y_ι, and by the rows the only such number
below 1.1076·10⁻¹⁵ is μ_Z, at ι_* and (356327, 1116082). ∎

**Theorem {#thm:is-gap}** (The admissible ε_K.) For Λ of [[def:iii-i10-1-1]] (ℰ_ind and ℰ^ι_ind as constructed), (G)
of [[def:iii-i10-1-3]] holds if and only if ε_K < μ_Z, and (G⁺) of [[def:iii-j-g-plus]] holds if and only if
ε_+ < μ_Z, with μ_Z of [[eq:is-mu-z]]; in particular every ε_K with which (G) holds, and every ε_+ with which (G⁺)
holds, is below 1.6747859·10⁻¹⁷. The real number 3 + μ_Z = ι_* + 356327𝔡₀ + 1116082𝔡₁ is the only element of Λ with
real part in (3, 3 + 1.1076·10⁻¹⁵). On the part Λ_ℬ of [[prop:is-lambda]] the least excess over the windows of (G) is

    μ_G := λ_♯ + 1109655𝔡₀ + 31682𝔡₁ − 3,

which satisfies [[eq:is-mu]]; the next smallest excesses there are 2.3181480·10⁻¹⁴ (above 3, from λ_♯ + 1 + δ′₁) and
8.0959353·10⁻¹⁴ (from λ_♯ + 1 + δ₂), and every other element of Λ_ℬ ∪ (Λ_ℬ + 𝔡₀) ∪ (Λ_ℬ + 𝔡₁) lies outside
(2, 2 + 4.2·10⁻¹³] ∪ (3, 3 + 4.2·10⁻¹³]. As μ_Z < δ_50 = ε_ind and μ_Z < ε_Υ for the admissible choice
ε_Υ = 1.4619·10⁻¹⁰ of [[lem:ec-gauge-gap]], the other conditions of [[def:iii-i10-1-3]] on ε_K leave every
ε_K ∈ (0, μ_Z) available, with ε_+ ∈ (ε_K, μ_Z); ε_K = 1.6747·10⁻¹⁷ is admissible, and ε_K = 1.6416·10⁻¹⁴ is not.

*Proof.* *The part Λ_ℬ.* By [[prop:is-lambda]] every element of Λ_ℬ below 3 + 10⁻⁸ is β + p𝔡₀ + q𝔡₁ with β ∈ ℬ. As 𝔡₀
and 𝔡₁ are increments, Λ + 𝔡₀ and Λ + 𝔡₁ lie in Λ, and Λ_ℬ + 𝔡₀ and Λ_ℬ + 𝔡₁ in Λ_ℬ, so the third window of (G) is
contained in the first. An element of Λ_ℬ in
```

### T9. thm:is-gap, end of the proof; new cor:is-lower, 71-explicit-constants.md lines 3322–3325

Old (4 lines):

```old
(8.0959353086·10⁻¹⁴, 8.0959353088·10⁻¹⁴). So the least excess over all windows is μ_G, and (G) holds exactly for
ε_K < μ_G. Finally μ_G < 10⁻¹³ < 1.94·10⁻⁸ < δ_50 by [[lem:s14-delta50]], and μ_G < ε_Υ = 1.4619·10⁻¹⁰, the choice of
[[lem:ec-gauge-gap]], so that every ε_K < μ_G meets the condition ε_K < ε_Υ of [[def:iii-i10-1-3]], and ε_+ may be taken
in (ε_K, μ_G), as [[eq:iii-i9-1-1]] and (G⁺) of [[def:iii-j-g-plus]] ask. ∎
```

New (25 lines):

```new
(8.0959353086·10⁻¹⁴, 8.0959353088·10⁻¹⁴). So on Λ_ℬ the least excess over all windows is μ_G, and the other elements
of Λ_ℬ ∪ (Λ_ℬ + 𝔡₀) ∪ (Λ_ℬ + 𝔡₁) lie outside (2, 2 + 4.2·10⁻¹³] ∪ (3, 3 + 4.2·10⁻¹³].

*The other elements.* By [[prop:is-lambda]], every element of Λ ∖ Λ_ℬ has real part greater than 2 + 2.932·10⁻⁶, and
one of real part at most 3 + 10⁻⁸ is ι + p𝔡₀ + q𝔡₁ or its conjugate, with ι ∈ Z₃, of real part
3 + (p𝔡₀ + q𝔡₁ − y_ι). So no element of Λ ∖ Λ_ℬ lies in the first window when ε_K < 2.932·10⁻⁶, and the third window
is still contained in the first. By [[lem:is-gap-z]], 3 + μ_Z, which lies in Λ and is real, is the only element of
Λ ∖ Λ_ℬ with real part in (3, 3 + 1.1076·10⁻¹⁵), and μ_Z < 1.1076·10⁻¹⁵ < μ_G. Hence the least excess of Λ over the
windows of (G) is μ_Z, attained in the second window: (G) holds if and only if ε_K < μ_Z, and no element of Λ has real
part in (3, 3 + ε_+] if and only if ε_+ < μ_Z. Finally μ_Z < 10⁻¹⁶ < 1.94·10⁻⁸ < δ_50 by [[lem:s14-delta50]], and
μ_Z < ε_Υ = 1.4619·10⁻¹⁰, the choice of [[lem:ec-gauge-gap]], so that every ε_K < μ_Z meets the condition ε_K < ε_Υ of
[[def:iii-i10-1-3]], and ε_+ may be taken in (ε_K, μ_Z), as [[eq:iii-i9-1-1]] and (G⁺) of [[def:iii-j-g-plus]] ask.
By [[eq:is-mu-z]], 1.6747·10⁻¹⁷ < μ_Z < 1.6416·10⁻¹⁴. ∎

**Corollary {#cor:is-lower}** (The loss for the index sets as constructed.) For ℰ_ind and ℰ^ι_ind as constructed, every
ε_K with which (G) holds satisfies ε_K < μ_Z < 1.6747859·10⁻¹⁷. For every admissible choice of the weights, the number
R of [[prop:ec-rounds]] then satisfies R > 4.0836·10²⁶, so that d_NM ≥ d_acc ≥ 3R > 1.2250·10²⁷ and
N_NM = 21d_NM + 6 > 2.5725·10²⁸; at ε_K = 1.6747·10⁻¹⁷, 3R > 1.2251·10²⁷.

*Proof.* The first assertion is [[thm:is-gap]] with [[eq:is-mu-z]]. By [[prop:ec-rounds]],
R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂) with δ̂ = 1.46214·10⁻¹⁰ and δ̄ = 1.94137057·10⁻⁸, and the right side decreases in ε_K.
At ε_K = 1.6747859·10⁻¹⁷ the numerator exceeds 1 − 1.98·10⁻⁸, as 3ε_K + 2δ̂ + δ̄ < 10⁻¹⁶ + 2.93·10⁻¹⁰ + 1.9414·10⁻⁸,
and ε_Kδ̂ = 2.448771…·10⁻²⁷ < 2.44878·10⁻²⁷; so R > (1 − 1.98·10⁻⁸)/(2.44878·10⁻²⁷) > 4.0836·10²⁶. By [[thm:loss-d]]
(ii), d_NM ≥ d_acc ≥ 3R > 1.2250·10²⁷, so N_NM > 21 · 1.2250·10²⁷ = 2.5725·10²⁸. At ε_K = 1.6747·10⁻¹⁷,
ε_Kδ̂ = 2.448645…·10⁻²⁷ < 2.44865·10⁻²⁷, and 3(1 − 1.98·10⁻⁸)/(2.44865·10⁻²⁷) > 1.2251·10²⁷. ∎
```

### T10. prop:is-count (a), statement, 71-explicit-constants.md lines 3329–3329

Old (1 lines):

```old
(a) 1.62066·10¹³ < N_Λ < 1.67472·10¹³;
```

New (2 lines):

```new
(a) 1.85753·10¹⁴ < N_Λ ≤ 909,507,124,095,312 < 9.09508·10¹⁴, and the part Λ_ℬ of [[prop:is-lambda]] has more than
1.62066·10¹³ and fewer than 1.67472·10¹³ elements of real part below 3 + ε_+;
```

### T11. prop:is-count (a), proof, 71-explicit-constants.md lines 3335–3348

Old (14 lines):

```old
*Proof.* (a) For X > 0 let T(X) := #{(p, q) ∈ ℕ₀² : p𝔡₀ + q𝔡₁ < X}. The triangle {u, v ≥ 0, u𝔡₀ + v𝔡₁ < X} has area
X²/(2𝔡₀𝔡₁), and each of its points lies in the unit square with lower left corner (⌊u⌋, ⌊v⌋), a counted point; the
squares [p, p + 1) × [q, q + 1) of the counted points are disjoint and lie in the triangle with X + 𝔡₀ + 𝔡₁. So

    X²/(2𝔡₀𝔡₁) ≤ T(X) ≤ (X + 𝔡₀ + 𝔡₁)²/(2𝔡₀𝔡₁).

By [[prop:is-lambda]], N_Λ = #(Λ ∩ {Re < 3 + ε_+}) ≤ Σ_(β∈ℬ) T(3 + ε_+ − β). The 26 rational β < 3 of ℬ (λ_♯, 2 + c and
5/2 + c, which include λ_♯ + 1 = 5/2 + a) give disjoint sets of points, since by [[lem:is-offsets]] (c) two of them
differ by no non-zero p𝔡₀ + q𝔡₁, and the points of one are distinct; so N_Λ ≥ Σ_(rational β<3) T(3 − β). The 26
numbers 3 − β are 1.4901, 1 − c (c ∈ σ^(2)) and 1/2 − c (c ∈ σ^(3)), with
Σ (3 − β)² = 14.40589434 and Σ (3 − β) = 17.832; by [[lem:is-offsets]] (b), 1/(2𝔡₀𝔡₁) = 1125001468750.4…. So
N_Λ ≥ 14.40589434·1125001468750.4 > 1.62066·10¹³. For the upper bound, ε_+ + 𝔡₀ + 𝔡₁ < 1.69·10⁻⁶ =: ν₀, the two
irrational β contribute at most 2(0.4901 + ν₀)²/(2𝔡₀𝔡₁), and β = 3 contributes T(ε_+) = 1, as ε_+ < 𝔡₁; so
N_Λ ≤ (14.40589434 + 2ν₀·17.832 + 26ν₀² + 2(0.4901 + ν₀)²)·1125001468750.5 + 1 < 1.67472·10¹³.
```

New (28 lines):

```new
*Proof.* (a) For X > 0 let T(X) := #{(p, q) ∈ ℕ₀² : p𝔡₀ + q𝔡₁ < X}. The triangle {u, v ≥ 0, u𝔡₀ + v𝔡₁ < X} has area
X²/(2𝔡₀𝔡₁), and each of its points lies in the unit square with lower left corner (⌊u⌋, ⌊v⌋), a counted point; the
squares [p, p + 1) × [q, q + 1) of the counted points are disjoint and lie in the triangle with X + 𝔡₀ + 𝔡₁. So

    X²/(2𝔡₀𝔡₁) ≤ T(X) ≤ (X + 𝔡₀ + 𝔡₁)²/(2𝔡₀𝔡₁).

*The part Λ_ℬ.* Let N_ℬ := #(Λ_ℬ ∩ {Re < 3 + ε_+}). By [[prop:is-lambda]], N_ℬ ≤ Σ_(β∈ℬ) T(3 + ε_+ − β). The 26
rational β < 3 of ℬ (λ_♯, 2 + c and 5/2 + c, which include λ_♯ + 1 = 5/2 + a) give disjoint sets of points, since by
[[lem:is-offsets]] (c) two of them differ by no non-zero p𝔡₀ + q𝔡₁, and the points of one are distinct; so
N_ℬ ≥ Σ_(rational β<3) T(3 − β). The 26 numbers 3 − β are 1.4901, 1 − c (c ∈ σ^(2)) and 1/2 − c (c ∈ σ^(3)), with
Σ (3 − β)² = 14.40589434 and Σ (3 − β) = 17.832; by [[lem:is-offsets]] (b), 1/(2𝔡₀𝔡₁) = 1125001468750.4…. So
N_ℬ ≥ 14.40589434·1125001468750.4 > 1.62066·10¹³. For the upper bound, ε_+ + 𝔡₀ + 𝔡₁ < 1.69·10⁻⁶ =: ν₀, the two
irrational β contribute at most 2(0.4901 + ν₀)²/(2𝔡₀𝔡₁), and β = 3 contributes T(ε_+) = 1, as ε_+ < 𝔡₁; so
N_ℬ ≤ (14.40589434 + 2ν₀·17.832 + 26ν₀² + 2(0.4901 + ν₀)²)·1125001468750.5 + 1 < 1.67472·10¹³.

*The other elements.* By [[prop:is-lambda]], the elements of Λ ∖ Λ_ℬ of real part below 3 + ε_+ are among the
ι + p𝔡₀ + q𝔡₁ with ι ∈ Z₃ and p𝔡₀ + q𝔡₁ < y_ι + ε_+, so there are at most Σ_(ι∈Z₃) T(y_ι + ε_+) of them, and
T(y_ι + ε_+) ≤ (y_ι + ν₀)²/(2𝔡₀𝔡₁). Summing over the rows of the tables of [[sec:tab-is]] the upper ends of the
intervals for y_ι of the proof of [[lem:is-gap-z]], and their squares, a row of the second table counted twice, gives
S₁ := Σ_(ι∈Z₃) y_ι < 1207.93630800 and S₂ := Σ_(ι∈Z₃) y_ι² < 793.55925810. As Z₃ has 2629 elements, there are at most
(S₂ + 2ν₀S₁ + 2629ν₀²)·1125001468750.5 < 892,759,924,095,312.22 of them. So
N_Λ < 16,747,200,000,000 + 892,759,924,095,312.22, and N_Λ, an integer, is at most 909,507,124,095,312.
For the lower bound let ι ∈ Z₃ be non-real. The numbers ι + p𝔡₀ + q𝔡₁ with p𝔡₀ + q𝔡₁ < y_ι are pairwise distinct
([[lem:is-offsets]] (c)), lie in Λ ([[prop:is-lambda]]) and are not real, so they do not lie in Λ_ℬ ∩ {Re < 3 + ε_+};
and they differ from those of every other non-real ι′ ∈ Z₃, as Im ι′ ≠ Im ι: in the second table of [[sec:tab-is]]
the column b increases with l by more than 2·10⁻²¹, and conjugates have imaginary parts of opposite signs. Summing over
the rows of the second table the squares of the lower ends of the intervals for y_ι, each twice, gives
Σ y_ι² > 150.70791670 over the non-real ι ∈ Z₃; so N_Λ ≥ N_ℬ + 150.70791670·1125001468750.4 > 1.85753·10¹⁴.
```

### T12. cor:is-flat, statement and proof, 71-explicit-constants.md lines 3446–3465

Old (20 lines):

```old
**Corollary {#cor:is-flat}** (The gap condition without 𝔡₀.) Suppose c_b = 0 for every b near b₀, and take ℰ′_ind of
[[thm:is-d0]] (c), with ℰ^ι_ind built from the same states. Then the increments of Λ below 3/2 are generated by 𝔡₁, 1,
1 + δ′₁, 1 + δ₂, 1 + 𝔡₀ and 1 + 2𝔡₀, and (G) holds if and only if ε_K < μ♭, where

    μ♭ := λ_♯ + 4470304𝔡₁ − 3 ∈ (5.0190·10⁻⁸, 5.0193·10⁻⁸)

([[prop:gap-sums]]). As μ♭ > δ_50 > ε_+ > ε_K, (G) then imposes nothing beyond [[eq:iii-i9-1-1]]. For such ε_+,
56,436,656 ≤ N_Λ ≤ 59,377,257.

*Proof.* The increments: the odd constructions give 𝔡₁ and 1 + δ′₁ (translations, roots 2 + 𝔡₁ and 3 + δ′₁ of type s1),
1 + 𝔡₁ (boosts) and 1 + 2𝔡₁ (μ_(1,0)); the even ones give 1 and 1 + δ₂ (rotations and ω̇_b(0, ·), roots 3 of types s0
and v1 and 3 + δ₂ of type s2), 1 + 𝔡₀ (ω̇_b(1, 0), the time translation tower, the class 1 − l at l = 2) and 1 + 2𝔡₀
(μ_s0); all other offsets are at least 2 or are sums of these. As in [[thm:is-gap]], the targets are y = 1.4901,
0.4901, 0.4901 − δ′₁, 0.4901 − δ₂, 0.4901 − 𝔡₀, 0.4901 − 2𝔡₀ (third window and λ_♯ + 1 + 𝔡₀ + ℕ₀𝔡₁ near 3), 1 − c and
1/2 − c, and the least excess is ⌈y/𝔡₁⌉𝔡₁ − y. By the column "frac" of the table of [[thm:is-gap]] and the values
1470297.2661 and 1470293.2661 of y/𝔡₁ at 0.4901 − 𝔡₀ and 0.4901 − 2𝔡₀, (1 − frac)𝔡₁ is least at y = 1.4901, where it
is μ♭, and every other is above 1.3888·10⁻⁷. For N_Λ: each β ∈ ℬ♭ (the 26 rational β < 3, λ_♯ + 1 + 𝔡₀,
λ_♯ + 1 + 2𝔡₀, λ_♯ + 1 + δ′₁, λ_♯ + 1 + δ₂ and 3) contributes ⌊(3 − β)/𝔡₁⌋ + 1 points, as no point lies in
[3, 3 + ε_+); the sets of the first 28 and of β = 3 are pairwise disjoint by [[lem:is-offsets]] (c); the sums with
and without λ_♯ + 1 + δ′₁ and λ_♯ + 1 + δ₂ give the bounds. ∎
```

New (35 lines):

```new
**Corollary {#cor:is-flat}** (The gap condition without 𝔡₀.) Suppose c_b = 0 for every b near b₀, and take ℰ′_ind of
[[thm:is-d0]] (c), with ℰ^ι_ind built from the same states. Then the increments of Λ below 3/2 are generated by 𝔡₁, 1,
1 + δ′₁, 1 + δ₂, 1 + 𝔡₀ and 1 + 2𝔡₀, and (G) holds if and only if ε_K < μ♭_Z, and (G⁺) if and only if ε_+ < μ♭_Z,
where μ♭_Z := (n + 1)𝔡₁ − y, with y := 3 − Re ι for the root ι of P_700 of positive imaginary part ([[lem:is-z3]]) and
n := ⌊y/𝔡₁⌋ = 394194, satisfies

    3.548125563·10⁻¹⁰ < μ♭_Z < 3.548125564·10⁻¹⁰.

As [[def:iii-i10-1-3]] asks ε_K < ε_Υ, and ε_Υ < 1.46214·10⁻¹⁰ < μ♭_Z ([[lem:ec-gauge-gap]]), (G) then imposes
nothing beyond the other conditions of [[def:iii-i10-1-3]] and [[eq:iii-i9-1-1]]. For ε_+ ∈ (0, μ♭_Z),
1,283,560,912 ≤ N_Λ ≤ 3,683,190,611. On the part Λ_ℬ of Λ built from the generators other than 1 + 𝒵, (G) holds if and
only if ε_K < μ♭ := λ_♯ + 4470304𝔡₁ − 3 ∈ (5.0190·10⁻⁸, 5.0193·10⁻⁸) ([[prop:gap-sums]]).

*Proof.* The increments: the odd constructions give 𝔡₁ and 1 + δ′₁ (translations, roots 2 + 𝔡₁ and 3 + δ′₁ of type s1),
1 + 𝔡₁ (boosts) and 1 + 2𝔡₁ (μ_(1,0)); the even ones give 1 and 1 + δ₂ (rotations and ω̇_b(0, ·), roots 3 of types s0
and v1 and 3 + δ₂ of type s2), 1 + 𝔡₀ (ω̇_b(1, 0), the time translation tower, the class 1 − l at l = 2) and 1 + 2𝔡₀
(μ_s0); all other offsets are at least 2 or are sums of these. *The part Λ_ℬ.* As in [[thm:is-gap]], the targets are
y = 1.4901, 0.4901, 0.4901 − δ′₁, 0.4901 − δ₂, 0.4901 − 𝔡₀, 0.4901 − 2𝔡₀ (third window and λ_♯ + 1 + 𝔡₀ + ℕ₀𝔡₁ near
3), 1 − c and 1/2 − c, and the least excess is ⌈y/𝔡₁⌉𝔡₁ − y. By the column "frac" of the table of [[thm:is-gap]] and
the values 1470297.2661 and 1470293.2661 of y/𝔡₁ at 0.4901 − 𝔡₀ and 0.4901 − 2𝔡₀, (1 − frac)𝔡₁ is least at y = 1.4901,
where it is μ♭, and every other is above 1.3888·10⁻⁷. *The elements of Z₃.* The proof of [[prop:is-lambda]] uses of the
increments only those of real part below 1, which are now 𝔡₁ alone; so every element of Λ ∖ Λ_ℬ has real part greater
than 2 + 2.932·10⁻⁶, and one of real part at most 3 + 10⁻⁸ is ι + q𝔡₁ or its conjugate with ι ∈ Z₃ and q ∈ ℕ₀, of real
part 3 + q𝔡₁ − y_ι. So the first window is missed, the third adds nothing, and the least positive excess in the second
for ι is (n⁺ + 1)𝔡₁ − y_ι, with n⁺ = ⌊y_ι/𝔡₁⌋ from the rows of [[sec:tab-is]] (proof of [[lem:is-gap-z]]). Bounding it
there by the bounds of [[lem:is-offsets]] (b) gives in every row a number above 4.2406·10⁻¹⁰, except for the row l = 700
of the second table, where y lies in (0.1313982198300303806313, 0.1313982198300303806333) and n⁺ = 394194, which
gives μ♭_Z with the bounds stated. As μ♭_Z < μ♭, the least excess of Λ over the windows is μ♭_Z, which gives both
equivalences. *N_Λ.* Each β ∈ ℬ♭ (the 26 rational β < 3, λ_♯ + 1 + 𝔡₀, λ_♯ + 1 + 2𝔡₀, λ_♯ + 1 + δ′₁, λ_♯ + 1 + δ₂
and 3) contributes ⌊(3 − β)/𝔡₁⌋ + 1 points, as no point lies in [3, 3 + ε_+); the sets of the first 28 and of β = 3
are pairwise disjoint by [[lem:is-offsets]] (c); the sums with and without λ_♯ + 1 + δ′₁ and λ_♯ + 1 + δ₂ give
56,436,656 and 59,377,257. Each ι ∈ Z₃ contributes the n⁺ + 1 points ι + q𝔡₁, 0 ≤ q ≤ n⁺, as ε_+ < μ♭_Z; the sum of the
n⁺ + 1 over Z₃ is 3,623,813,354, and over its 1360 non-real elements 1,227,124,256, whose points are not real and
pairwise distinct (proof of [[prop:is-count]] (a)). So 56,436,656 + 1,227,124,256 ≤ N_Λ ≤ 59,377,257 +
3,623,813,354. ∎
```

### T13. rem:is-summary, 71-explicit-constants.md lines 3469–3487

Old (19 lines):

```old
**Remark {#rem:is-summary}** (What (IS) gives and what it leaves.) At the computational point, for the index sets as
constructed: the exponents of real part at most 5 are [[eq:is-ind]], [[prop:is-iota]] and [[prop:is-ci-pp]] (a), with
logarithmic orders at most 39 for ℰ_ind (attained), 50 for ℰ^ι_ind and 0 for the least ℰ^C_I; those of the least ℰ_++
below 2λ_♯ are [[prop:is-ci-pp]] (b); above 2λ_♯ they depend on ℰ_+, and none of Λ ∩ {Re ≤ 3 + ε_+}, l_* and k̄_0
uses them. Every indicial root of L̂_b(0) has multiplicity at most 7, and is simple on [−101, 5] ([[prop:is-mult]]);
[[def:iii-i10-1-1]] asks l_* to bound them at real part at most 5, a half-plane that contains the roots below −101; for
these the bound 7 serves, and their exact multiplicities, which are 1 ([[thm:t49-point]]), are not needed. So the
largest multiplicity M of an indicial root of L̂_b(0) of real part at most 5 satisfies M ≤ 7 ([[prop:iii-f1-2-3]] (b)),
the largest logarithmic order L of ℰ_ind ∪ ℰ^ι_ind ∪ ℰ^C_I at real part at most 5 satisfies 39 ≤ L ≤ 50, the order 39
being attained at (5, 39) ∈ ℰ_ind ([[prop:is-logs]], [[prop:is-ci-pp]] (a)), and the part of l_* that (IS) fixes,
max(L, M) = L, is at most 50: l_* = 50 is admissible for it. (G), N_Λ, k̄_0 and J_* are [[thm:is-gap]] and
[[prop:is-count]]. The orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5, statement (SP) of [[rem:uc-missing]],
are all 1 ([[cor:sp-lstar]] (a)), so they do not raise l_* above L. Two further things are not determined by this paper:
the coefficient c_b of [[def:is-cb]] at a rotating b, which for index sets that keep 𝔡₁ decides whether ε_K may be
taken up to μ♭ ([[cor:is-flat]]) or only below μ_G ([[thm:is-gap]]), and whether an admissible ℰ_ind can omit 𝔡₁. Neither
enters an upper bound for d: the index sets as constructed serve with every ε_K < μ_G, and the two decide only whether
smaller index sets, with a larger ε_K, are available. The individual roots ι ∈ Z of [[prop:is-iota]] are fixed by the
polynomials of [[prop:np-10-12]] and located by [[sec:s14-pa]]; they lie above 3 as exponents of ℰ^ι_ind and do not enter
Λ below 3 + ε_+.
```

New (22 lines):

```new
**Remark {#rem:is-summary}** (What (IS) gives and what it leaves.) At the computational point, for the index sets as
constructed: the exponents of real part at most 5 are [[eq:is-ind]], [[prop:is-iota]] and [[prop:is-ci-pp]] (a), with
logarithmic orders at most 39 for ℰ_ind (attained), 50 for ℰ^ι_ind and 0 for the least ℰ^C_I; those of the least ℰ_++
below 2λ_♯ are [[prop:is-ci-pp]] (b); above 2λ_♯ they depend on ℰ_+, and none of Λ ∩ {Re ≤ 3 + ε_+}, l_* and k̄_0
uses them. Every indicial root of L̂_b(0) has multiplicity at most 7, and is simple on [−101, 5] ([[prop:is-mult]]);
[[def:iii-i10-1-1]] asks l_* to bound them at real part at most 5, a half-plane that contains the roots below −101; for
these the bound 7 serves, and their exact multiplicities, which are 1 ([[thm:t49-point]]), are not needed. So the
largest multiplicity M of an indicial root of L̂_b(0) of real part at most 5 satisfies M ≤ 7 ([[prop:iii-f1-2-3]] (b)),
the largest logarithmic order L of ℰ_ind ∪ ℰ^ι_ind ∪ ℰ^C_I at real part at most 5 satisfies 39 ≤ L ≤ 50, the order 39
being attained at (5, 39) ∈ ℰ_ind ([[prop:is-logs]], [[prop:is-ci-pp]] (a)), and the part of l_* that (IS) fixes,
max(L, M) = L, is at most 50: l_* = 50 is admissible for it. (G), (G⁺), N_Λ, k̄_0 and J_* are [[thm:is-gap]] and
[[prop:is-count]]. The orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5, statement (SP) of
[[rem:uc-missing]], are all 1 ([[cor:sp-lstar]] (a)), so they do not raise l_* above L. The roots ι ∈ Z of
[[prop:is-iota]] are fixed by the polynomials of [[prop:np-10-12]] and located by [[sec:s14-pa]]; as exponents of
ℰ^ι_ind they lie above 3, and the 2629 of them of real part below 3 enter Λ through the generator 1 + 𝒵 of
[[def:iii-i10-1-1]]. They decide (G), (G⁺) and N_Λ: [[lem:is-z3]] locates them to within 10⁻²¹, and [[lem:is-gap-z]]
gives their least excesses; on the part Λ_ℬ alone (G) would hold for every ε_K < μ_G, and Λ_ℬ has fewer than
1.67472·10¹³ elements below 3 + ε_+. Two further things are not determined by this paper: the coefficient c_b of
[[def:is-cb]] at a rotating b, which for index sets that keep 𝔡₁ decides whether ε_K may be taken up to ε_Υ
([[cor:is-flat]]) or only below μ_Z ([[thm:is-gap]]), and whether an admissible ℰ_ind can omit 𝔡₁. Neither enters an
upper bound for d: the index sets as constructed serve with every ε_K < μ_Z, and the two decide only whether smaller
index sets, with a larger ε_K and a smaller N_Λ, are available.
```

### T14. new sec:tab-is with sec:tab-is-real and sec:tab-is-complex, before sec:tab-t49, 96-tables.md lines 260–260

Old (1 lines):

```old
### Tables for the exceptional sets {#sec:tab-t49}
```

New (1996 lines):

```new
### Tables for the roots of the damping polynomials below the real part 3 {#sec:tab-is}

The two tables of this section locate the 2629 elements of real part below 3 of the set Z of [[prop:is-iota]], each to
within 10⁻²¹, and give the least excess of each above the lattice p𝔡₀ + q𝔡₁. They are used in [[lem:is-z3]],
[[lem:is-gap-z]], [[thm:is-gap]], [[prop:is-count]] and [[cor:is-flat]].

Throughout, (v, e, h) = (1/2, 1/102400, 10⁻⁶), κ = l(l + 2), 𝒫_l = 64·10¹⁸P_l = Σ_(k=0)^6 π_k(κ)ι^k for l ≥ 1, with
the integer coefficients π_k of [[sec:tab-a-sextic]], and 𝒫_0 = 102400·10¹²C, the cubic [[eq:is-c-int]]. For a root ι
of the row, y := 3 − Re ι, n⁺ := ⌊y/𝔡₁⌋, n⁻ := ⌊4y/𝔡₀⌋, and m(y) is the least positive number p𝔡₀ + q𝔡₁ − y with
p, q ∈ ℕ₀ ([[lem:is-reduction]]). The column (p, q) gives the pair at which m(y) is attained, p = 0 meaning
m(y) = (n⁺ + 1)𝔡₁ − y with q = n⁺ + 1, and the column m a lower bound for m(y), rounded down to five significant
figures.

*Checks.* For a row (l, j, r) of the first table, 10¹²⁶𝒫_l(r) and 10¹²⁶𝒫_l(r + 10⁻²¹) are integers (for l = 0,
10⁶³𝒫_0(r) and 10⁶³𝒫_0(r + 10⁻²¹)), and their signs differ. For a row (l, a, b) of the second table, with c := a + ib,
10¹³²𝒫_l(c) and 10¹¹⁰𝒫_l′(c) are Gaussian integers, and

    |Re 𝒫_l(c)| + |Im 𝒫_l(c)| + 3.5·10⁻²¹ < 10⁻²¹ max(|Re 𝒫_l′(c)|, |Im 𝒫_l′(c)|).

For every row, y lies in (3 − r − 10⁻²¹, 3 − r), resp. (3 − a − 10⁻²¹, 3 − a + 10⁻²¹). Dividing the two ends by the
bounds for 𝔡₁ and for 𝔡₀/4 of [[lem:is-offsets]] (b) gives the same integer parts n⁺ and n⁻ at both ends, with
n⁺ − n⁻ ≤ 2; for each integer n with n⁻ < n ≤ n⁺, dividing the ends of the interval for θ_n = y − n𝔡₁ by the bounds for
ε₀ gives the same integer part p_n − 1; and of the numbers of [[lem:is-reduction]], bounded by the bounds of
[[lem:is-offsets]] (b), the least is the one at (p, q), it is at least m, and the others exceed m.

#### The real roots {#sec:tab-is-real}

*Object.* For each row, the j-th real root, in increasing order, of real part in (2, 3) of P_l (of C for l = 0); it
lies in (r, r + 10⁻²¹). The rows are those of [[lem:is-z3]] (c).

| l | j | r | p | q | m |
|---|---|---|---|---|---|
| 0 | 1 | 2.000074743820359123145 | 211008 | 2155746 | 1.5502·10⁻¹³ |
| 1 | 1 | 2.000120195037164481266 | 598747 | 604653 | 8.4760·10⁻¹⁴ |
| 1 | 2 | 2.999958048936330986539 | 0 | 126 | 4.8900·10⁻⁸ |
| 2 | 1 | 2.000002932350446240725 | 471765 | 1112933 | 1.3632·10⁻¹³ |
| 2 | 2 | 2.000193021897207162014 | 310287 | 1758275 | 5.4513·10⁻¹³ |
| 2 | 3 | 2.999894789954402687824 | 0 | 316 | 1.2319·10⁻⁷ |
| 3 | 1 | 2.000008683387173269218 | 319890 | 1720416 | 1.1100·10⁻¹³ |
| 3 | 2 | 2.000293348844440012805 | 321626 | 1712618 | 2.8459·10⁻¹³ |
| 3 | 3 | 2.999806212290427501888 | 0 | 582 | 2.1212·10⁻⁷ |
| 4 | 1 | 2.000016922372164741530 | 489704 | 1041135 | 1.7392·10⁻¹⁴ |
| 4 | 2 | 2.000421521720728264450 | 10250 | 2957738 | 1.9945·10⁻¹³ |
| 4 | 3 | 2.999692300840556363355 | 0 | 924 | 3.0057·10⁻⁷ |
| 5 | 1 | 2.000027439390591954434 | 159055 | 2363700 | 1.9604·10⁻¹³ |
| 5 | 2 | 2.000577769880984919988 | 163319 | 2344993 | 4.1427·10⁻¹⁴ |
| 5 | 3 | 2.999553036164704742893 | 0 | 1341 | 3.5779·10⁻⁸ |
| 6 | 1 | 2.000040118925257073918 | 135873 | 2456390 | 2.1830·10⁻¹³ |
| 6 | 2 | 2.000762232634418936528 | 530077 | 877407 | 1.8786·10⁻¹³ |
| 6 | 3 | 2.999388394470861236883 | 0 | 1835 | 6.0610·10⁻⁸ |
| 7 | 1 | 2.000054897472911286330 | 534464 | 861981 | 1.4258·10⁻¹³ |
| 7 | 2 | 2.000975001647455576959 | 345524 | 1614981 | 2.8505·10⁻¹³ |
| 7 | 3 | 2.999198347595849064562 | 0 | 2405 | 1.3572·10⁻⁸ |
| 8 | 1 | 2.000071738944739850682 | 219789 | 2120631 | 2.8374·10⁻¹³ |
| 8 | 2 | 2.001216145566073338251 | 86097 | 2651966 | 3.7860·10⁻¹³ |
| 8 | 3 | 2.998982862982504087418 | 0 | 3052 | 1.9543·10⁻⁷ |
| 9 | 1 | 2.000090621980943234948 | 430294 | 1278554 | 2.2375·10⁻¹⁴ |
| 9 | 2 | 2.001485722727671565486 | 246788 | 2008393 | 2.6405·10⁻¹³ |
| 9 | 3 | 2.998741903653226058859 | 0 | 3775 | 2.3590·10⁻⁷ |
| 10 | 1 | 2.000111533425805499334 | 589661 | 641023 | 1.5378·10⁻¹³ |
| 10 | 2 | 2.001783787716127935609 | 129347 | 2477263 | 3.5818·10⁻¹³ |
| 10 | 3 | 2.998475428179852757195 | 0 | 4574 | 9.3533·10⁻⁸ |
| 11 | 1 | 2.000134464875388551239 | 713016 | 147534 | 6.9761·10⁻¹⁴ |
| 11 | 2 | 2.002110394847964761453 | 236003 | 2049659 | 1.3342·10⁻¹³ |
| 11 | 3 | 2.998183390649799426653 | 0 | 5450 | 5.5752·10⁻⁸ |
| 12 | 1 | 2.000159410783046521427 | 210344 | 2158148 | 1.9437·10⁻¹³ |
| 12 | 2 | 2.002465600104494869192 | 465991 | 1128641 | 3.7006·10⁻¹³ |
| 12 | 3 | 2.997865740628398523744 | 0 | 6403 | 7.2123·10⁻⁸ |
| 13 | 1 | 2.000186367380392547452 | 288427 | 1845735 | 2.1699·10⁻¹³ |
| 13 | 2 | 2.002849462252387419451 | 113530 | 2537334 | 3.8919·10⁻¹³ |
| 13 | 3 | 2.997522423117367112743 | 0 | 7433 | 8.7650·10⁻⁸ |
| 14 | 1 | 2.000215332040662105881 | 351994 | 1591380 | 4.4424·10⁻¹³ |
| 14 | 2 | 2.003262043525790094573 | 266598 | 1923824 | 2.1964·10⁻¹³ |
| 14 | 3 | 2.997153378509321346182 | 0 | 8540 | 4.2724·10⁻⁸ |
| 15 | 1 | 2.000246302890704334337 | 404416 | 1381599 | 5.0226·10⁻¹³ |
| 15 | 2 | 2.003703410063864966982 | 206145 | 2164312 | 1.1774·10⁻¹⁴ |
| 15 | 3 | 2.996758542538249274455 | 0 | 9725 | 2.0641·10⁻⁷ |
| 16 | 1 | 2.000279278567423086198 | 448146 | 1206580 | 7.2116·10⁻¹⁴ |
| 16 | 2 | 2.004173632208013568651 | 405557 | 1365253 | 2.3493·10⁻¹³ |
| 16 | 3 | 2.996337846225844721650 | 0 | 10987 | 1.7640·10⁻⁷ |
| 17 | 1 | 2.000314258060753952961 | 485004 | 1059043 | 2.0010·10⁻¹³ |
| 17 | 2 | 2.004672784716811044690 | 730267 | 64915 | 5.0559·10⁻¹⁴ |
| 17 | 3 | 2.995891215823596109590 | 0 | 12327 | 2.1228·10⁻⁷ |
| 18 | 1 | 2.000351240609956786552 | 516358 | 933516 | 1.4575·10⁻¹³ |
| 18 | 2 | 2.005200946931985215009 | 437462 | 1234551 | 5.1352·10⁻¹³ |
| 18 | 3 | 2.995418572750514873868 | 0 | 13745 | 2.3547·10⁻⁷ |
| 19 | 1 | 2.000390225633606788458 | 543255 | 825811 | 1.5070·10⁻¹³ |
| 19 | 2 | 2.005758202915182491949 | 575828 | 679415 | 2.7147·10⁻¹³ |
| 19 | 3 | 2.994919833526378457080 | 0 | 15241 | 1.6248·10⁻⁷ |
| 20 | 1 | 2.000431212681387038917 | 566506 | 732684 | 4.5339·10⁻¹³ |
| 20 | 2 | 2.006344641567552913852 | 385345 | 1439588 | 3.6100·10⁻¹³ |
| 20 | 3 | 2.994394909700352746068 | 0 | 16816 | 2.3820·10⁻⁷ |
| 21 | 1 | 2.000474201400288463988 | 586745 | 651599 | 2.6683·10⁻¹³ |
| 21 | 2 | 2.006960356739694050612 | 297081 | 1790797 | 4.5713·10⁻¹³ |
| 21 | 3 | 2.993843707774848199294 | 0 | 18469 | 3.5806·10⁻⁸ |
| 22 | 1 | 2.000519191510517630147 | 4477 | 2980537 | 2.0304·10⁻¹³ |
| 22 | 2 | 2.007605447336810313631 | 133006 | 2445162 | 2.4939·10⁻¹³ |
| 22 | 3 | 2.993266129124452742294 | 0 | 20202 | 1.2332·10⁻⁷ |
| 23 | 1 | 2.000566182788063143114 | 620104 | 517887 | 3.3847·10⁻¹⁴ |
| 23 | 2 | 2.008280017422305579861 | 305806 | 1751938 | 1.1076·10⁻¹⁵ |
| 23 | 3 | 2.992662069909772744801 | 0 | 22014 | 6.3590·10⁻⁸ |
| 24 | 1 | 2.000615175051904415517 | 33954 | 2862341 | 3.6081·10⁻¹³ |
| 24 | 2 | 2.008984176322006464435 | 618695 | 498269 | 2.8279·10⁻¹⁴ |
| 24 | 3 | 2.992031420986000980462 | 0 | 23906 | 8.0790·10⁻⁸ |
| 25 | 1 | 2.000666168154506144327 | 46290 | 2812844 | 2.0970·10⁻¹³ |
| 25 | 2 | 2.009718038730567117385 | 265223 | 1909956 | 4.3776·10⁻¹³ |
| 25 | 3 | 2.991374067806017352672 | 0 | 25878 | 6.0378·10⁻⁸ |
| 26 | 1 | 2.000719161974670820987 | 657331 | 368520 | 4.9603·10⁻¹⁴ |
| 26 | 2 | 2.010481724821191320600 | 229076 | 2052253 | 3.3831·10⁻¹³ |
| 26 | 3 | 2.990689890317814287494 | 0 | 27931 | 2.1563·10⁻⁷ |
| 27 | 1 | 2.000774156412105404755 | 67259 | 2728644 | 2.4855·10⁻¹³ |
| 27 | 2 | 2.011275360359538567014 | 283877 | 1830668 | 4.4111·10⁻¹³ |
| 27 | 3 | 2.989978762856023981128 | 0 | 30064 | 8.7559·10⁻⁸ |
| 28 | 1 | 2.000831151383249048218 | 676222 | 292620 | 6.7897·10⁻¹⁴ |
| 28 | 2 | 2.012099076822505660746 | 192967 | 2191837 | 4.7479·10⁻¹³ |
| 28 | 3 | 2.989240554027309074258 | 0 | 32279 | 2.1142·10⁻⁷ |
| 29 | 1 | 2.000890146818038880959 | 684348 | 259939 | 1.0584·10⁻¹³ |
| 29 | 2 | 2.012953011522461853575 | 309183 | 1724411 | 2.3729·10⁻¹³ |
| 29 | 3 | 2.988475126589361731903 | 0 | 34575 | 1.1666·10⁻⁷ |
| 30 | 1 | 2.000951142657380835359 | 91743 | 2630177 | 1.5718·10⁻¹³ |
| 30 | 2 | 2.013837307737443210624 | 374625 | 1459990 | 4.5798·10⁻¹⁴ |
| 30 | 3 | 2.987682337323238451941 | 0 | 36954 | 3.2671·10⁻⁷ |
| 31 | 1 | 2.001014138851155520758 | 98497 | 2602972 | 4.0251·10⁻¹³ |
| 31 | 2 | 2.014752114847767683688 | 120409 | 2474110 | 2.7966·10⁻¹³ |
| 31 | 3 | 2.986862036898739117610 | 0 | 39414 | 2.5585·10⁻⁸ |
| 32 | 1 | 2.001079135356633825249 | 104686 | 2578021 | 1.8492·10⁻¹³ |
| 32 | 2 | 2.015697588479507756144 | 466406 | 1087285 | 1.5314·10⁻¹³ |
| 32 | 3 | 2.986014069732518750813 | 0 | 41958 | 5.7689·10⁻⁸ |
| 33 | 1 | 2.001146132137208947432 | 110377 | 2555056 | 1.1981·10⁻¹³ |
| 33 | 2 | 2.016673890655246916652 | 520977 | 866072 | 4.9965·10⁻¹³ |
| 33 | 3 | 2.985138273838599006657 | 0 | 44586 | 2.6104·10⁻⁷ |
| 34 | 1 | 2.001215129161374758391 | 115627 | 2533849 | 3.6772·10⁻¹³ |
| 34 | 2 | 2.017681189952545912007 | 580680 | 624238 | 2.1037·10⁻¹³ |
| 34 | 3 | 2.984234480670923558627 | 0 | 47297 | 1.3376·10⁻⁷ |
| 35 | 1 | 2.001286126401897365890 | 120484 | 2514208 | 3.6140·10⁻¹³ |
| 35 | 2 | 2.018719661670552250834 | 329978 | 1623931 | 1.7153·10⁻¹³ |
| 35 | 3 | 2.983302514957577030691 | 0 | 50093 | 1.6724·10⁻⁷ |
| 36 | 1 | 2.001359123835139285672 | 124991 | 2495961 | 3.5225·10⁻¹³ |
| 36 | 2 | 2.019789488005200131452 | 640917 | 376965 | 2.5565·10⁻¹⁴ |
| 36 | 3 | 2.982342194526260898144 | 0 | 52974 | 1.7932·10⁻⁷ |
| 37 | 1 | 2.001434121440504961315 | 129185 | 2478960 | 3.0026·10⁻¹³ |
| 37 | 2 | 2.020890858233466758718 | 572799 | 646133 | 1.0830·10⁻¹⁴ |
| 37 | 3 | 2.981353330120591650901 | 0 | 55941 | 3.1406·10⁻⁷ |
| 38 | 1 | 2.001511119199983387472 | 733098 | 63076 | 1.2219·10⁻¹³ |
| 38 | 2 | 2.022023968907174189808 | 371831 | 1446606 | 5.1352·10⁻¹³ |
| 38 | 3 | 2.980335725206756324481 | 0 | 58993 | 4.1606·10⁻⁸ |
| 39 | 1 | 2.001590117097768901159 | 136760 | 2448192 | 2.2904·10⁻¹³ |
| 39 | 2 | 2.023189024056852970645 | 270755 | 1847415 | 7.5837·10⁻¹⁴ |
| 39 | 3 | 2.979289175770028072286 | 0 | 62133 | 1.5793·10⁻⁷ |
| 40 | 1 | 2.001671115119945255745 | 740194 | 34212 | 8.2351·10⁻¹⁴ |
| 40 | 2 | 2.024386235406214650000 | 488471 | 972959 | 4.2415·10⁻¹³ |
| 40 | 3 | 2.978213470100609577518 | 0 | 65360 | 1.1800·10⁻⁷ |
| 41 | 1 | 2.001754113254221203335 | 143424 | 2421044 | 1.2418·10⁻¹³ |
| 41 | 2 | 2.025615822597814686435 | 29620 | 2804675 | 1.6532·10⁻¹³ |
| 41 | 3 | 2.977108388568234563842 | 0 | 68675 | 3.5522·10⁻⁸ |
| 42 | 1 | 2.001839111489708217022 | 746468 | 8612 | 6.6006·10⁻¹⁴ |
| 42 | 2 | 2.026878013430525302871 | 284165 | 1782708 | 3.8190·10⁻¹³ |
| 42 | 3 | 2.975973703384917218575 | 0 | 72079 | 1.6028·10⁻⁸ |
| 43 | 1 | 2.001926109816732856801 | 149345 | 2396844 | 1.8994·10⁻¹³ |
| 43 | 2 | 2.028173044109479589287 | 226935 | 2007743 | 4.2975·10⁻¹⁴ |
| 43 | 3 | 2.974809178355195724071 | 0 | 75573 | 1.5666·10⁻⁷ |
| 44 | 1 | 2.002015108226677748937 | 152069 | 2385681 | 1.0638·10⁻¹³ |
| 44 | 2 | 2.029501159509193772720 | 17157 | 2842871 | 2.6541·10⁻¹⁴ |
| 44 | 3 | 2.973614568613169008347 | 0 | 79157 | 2.1255·10⁻⁷ |
| 45 | 1 | 2.002106106711846303164 | 154655 | 2375064 | 3.0207·10⁻¹³ |
| 45 | 2 | 2.030862613450624294439 | 397952 | 1315606 | 2.6727·10⁻¹⁴ |
| 45 | 3 | 2.972389620345574950722 | 0 | 82832 | 2.6323·10⁻⁷ |
| 46 | 1 | 2.002199105265347206324 | 157115 | 2364945 | 5.5236·10⁻¹³ |
| 46 | 2 | 2.032257668992970443764 | 295814 | 1719973 | 3.1208·10⁻¹³ |
| 46 | 3 | 2.971134070500103254349 | 0 | 86598 | 4.5643·10⁻⁸ |
| 47 | 1 | 2.002294103880995458934 | 159459 | 2355284 | 2.2780·10⁻¹³ |
| 47 | 2 | 2.033686598741092138399 | 420052 | 1218734 | 4.3479·10⁻¹⁴ |
| 47 | 3 | 2.969847646478076629313 | 0 | 90458 | 2.8717·10⁻⁷ |
| 48 | 1 | 2.002391102553227303518 | 161699 | 2346033 | 4.3130·10⁻¹³ |
| 48 | 2 | 2.035149685169476409414 | 262214 | 1845697 | 4.9074·10⁻¹³ |
| 48 | 3 | 2.968530065810569379328 | 0 | 94410 | 3.8711·10⁻⁸ |
| 49 | 1 | 2.002490101277026861729 | 163842 | 2337164 | 3.5870·10⁻¹⁴ |
| 49 | 2 | 2.036647220963755699280 | 495463 | 908208 | 4.8443·10⁻¹³ |
| 49 | 3 | 2.967181035816962466573 | 0 | 98457 | 7.5561·10⁻⁹ |
| 50 | 1 | 2.002591100047862675485 | 165898 | 2328637 | 6.5601·10⁻¹⁴ |
| 50 | 2 | 2.038179509380856728139 | 573937 | 589715 | 4.0926·10⁻¹³ |
| 50 | 3 | 2.965800253244858104286 | 0 | 102600 | 2.2379·10⁻⁷ |
| 51 | 1 | 2.002694098861632654128 | 167874 | 2320424 | 3.0729·10⁻¹³ |
| 51 | 2 | 2.039746864628941006272 | 532061 | 752517 | 3.7259·10⁻¹³ |
| 51 | 3 | 2.964387403890194297136 | 0 | 106838 | 3.9890·10⁻⁸ |
| 52 | 1 | 2.002799097714616179599 | 169776 | 2312501 | 3.7365·10⁻¹³ |
| 52 | 2 | 2.041349612268387720405 | 383826 | 1340649 | 4.8188·10⁻¹³ |
| 52 | 3 | 2.962942162196309849747 | 0 | 111174 | 1.3028·10⁻⁷ |
| 53 | 1 | 2.002906096603432326134 | 171610 | 2304844 | 2.1710·10⁻¹³ |
| 53 | 2 | 2.042988089635167427505 | 122026 | 2382934 | 3.2971·10⁻¹³ |
| 53 | 3 | 2.961464190830612453203 | 0 | 115608 | 1.5764·10⁻⁷ |
| 54 | 1 | 2.003015095525003318919 | 173382 | 2297429 | 9.3184·10⁻¹⁴ |
| 54 | 2 | 2.044662646288061569204 | 317455 | 1596194 | 2.5234·10⁻¹³ |
| 54 | 3 | 2.959953140237395711967 | 0 | 120141 | 1.0575·10⁻⁷ |
| 55 | 1 | 2.003126094476522494646 | 175098 | 2290232 | 5.2857·10⁻¹³ |
| 55 | 2 | 2.046373644481299187972 | 318055 | 1588661 | 1.8330·10⁻¹³ |
| 55 | 3 | 2.958408648165234467152 | 0 | 124775 | 2.7901·10⁻⁷ |
| 56 | 1 | 2.003239093455426141453 | 176760 | 2283245 | 7.0664·10⁻¹⁴ |
| 56 | 2 | 2.048121459664309407838 | 648016 | 263573 | 6.0636·10⁻¹⁵ |
| 56 | 3 | 2.956830339167260475869 | 0 | 129510 | 3.0199·10⁻⁷ |
| 57 | 1 | 2.003354092459368690880 | 178375 | 2276440 | 2.6277·10⁻¹³ |
| 57 | 2 | 2.049906481010427387149 | 6827 | 2822975 | 2.8799·10⁻¹³ |
| 57 | 3 | 2.955217824072481266497 | 0 | 134347 | 1.1884·10⁻⁷ |
| 58 | 1 | 2.003471091486200813735 | 179945 | 2269809 | 6.6700·10⁻¹⁴ |
| 58 | 2 | 2.051729111976543848292 | 68263 | 2571763 | 3.5235·10⁻¹³ |
| 58 | 3 | 2.953570699426152513107 | 12999 | 87292 | 3.6102·10⁻¹³ |
| 59 | 1 | 2.003590090533950037992 | 181475 | 2263332 | 2.8772·10⁻¹³ |
| 59 | 2 | 2.053589770895855388098 | 79324 | 2521937 | 2.3438·10⁻¹³ |
| 59 | 3 | 2.951888546897047107155 | 0 | 144335 | 1.7213·10⁻⁷ |
| 60 | 1 | 2.003711089600803562416 | 182967 | 2257001 | 2.2417·10⁻¹³ |
| 60 | 2 | 2.055488891606056202384 | 459102 | 997127 | 3.2886·10⁻¹³ |
| 60 | 3 | 2.950170932649280619318 | 0 | 149488 | 2.2307·10⁻⁷ |
| 61 | 1 | 2.003834088685092986299 | 184425 | 2250800 | 4.2986·10⁻¹³ |
| 61 | 2 | 2.057426924115513453579 | 397581 | 1237397 | 2.9907·10⁻¹³ |
| 61 | 3 | 2.948417406676151202126 | 0 | 154748 | 2.8924·10⁻⁸ |
| 62 | 1 | 2.003959087785280715134 | 185851 | 2244721 | 4.7830·10⁻¹³ |
| 62 | 2 | 2.059404335310190341204 | 254366 | 1804325 | 4.8903·10⁻¹³ |
| 62 | 3 | 2.946627502093230113815 | 0 | 160118 | 1.2280·10⁻⁷ |
| 63 | 1 | 2.004086086899947835347 | 187247 | 2238756 | 6.1705·10⁻¹⁴ |
| 63 | 2 | 2.061421609704325338264 | 357329 | 1386421 | 8.0853·10⁻¹⁴ |
| 63 | 3 | 2.944800734387694607200 | 0 | 165598 | 2.0188·10⁻⁸ |
| 64 | 1 | 2.004215086027783279506 | 188617 | 2232889 | 9.1208·10⁻¹⁴ |
| 64 | 2 | 2.063479250238145676164 | 401179 | 1204848 | 2.1408·10⁻¹³ |
| 64 | 3 | 2.942936600620625279546 | 0 | 171191 | 2.1814·10⁻⁷ |
| 65 | 1 | 2.004346085167574127479 | 189963 | 2227112 | 4.6500·10⁻¹³ |
| 65 | 2 | 2.065577779126190991831 | 45928 | 2619557 | 2.3749·10⁻¹³ |
| 65 | 3 | 2.941034578578692124299 | 0 | 176897 | 1.9446·10⁻⁷ |
| 66 | 1 | 2.004479084318196909479 | 191285 | 2221425 | 5.9634·10⁻¹⁴ |
| 66 | 2 | 2.067717738760152492190 | 115270 | 2335769 | 2.9305·10⁻¹³ |
| 66 | 3 | 2.939094125871324063550 | 0 | 182718 | 7.3424·10⁻⁸ |
| 67 | 1 | 2.004614083478609794514 | 192587 | 2215812 | 5.5479·10⁻¹⁴ |
| 67 | 2 | 2.069899692670497906932 | 194849 | 2010907 | 1.1906·10⁻¹³ |
| 67 | 3 | 2.937114678969091806829 | 0 | 188657 | 2.9148·10⁻⁷ |
| 68 | 1 | 2.004751082647845562731 | 193870 | 2210269 | 4.0877·10⁻¹⁴ |
| 68 | 2 | 2.072124226551557290207 | 430415 | 1061969 | 1.4190·10⁻¹³ |
| 68 | 3 | 2.935095652178629077066 | 0 | 194714 | 2.6295·10⁻⁷ |
| 69 | 1 | 2.004890081825005273059 | 195136 | 2204788 | 2.2799·10⁻¹³ |
| 69 | 2 | 2.074391949355194414753 | 325854 | 1473410 | 4.0347·10⁻¹³ |
| 69 | 3 | 2.933036436548967548813 | 0 | 200891 | 4.5552·10⁻⁸ |
| 70 | 1 | 2.005031081009252548672 | 196386 | 2199365 | 3.3601·10⁻¹³ |
| 70 | 2 | 2.076703494458688814340 | 541084 | 605555 | 4.8163·10⁻¹⁵ |
| 70 | 3 | 2.930936398703660520343 | 0 | 207191 | 5.8988·10⁻⁹ |
| 71 | 1 | 2.005174080199808412348 | 197621 | 2193996 | 1.4151·10⁻¹³ |
| 71 | 2 | 2.079059520913011040958 | 489815 | 803563 | 3.3741·10⁻¹³ |
| 71 | 3 | 2.928794879592512821098 | 0 | 213616 | 1.5161·10⁻⁷ |
| 72 | 1 | 2.005319079395946612093 | 198843 | 2188673 | 2.9357·10⁻¹⁴ |
| 72 | 2 | 2.081460714778295948401 | 137136 | 2207076 | 4.5151·10⁻¹³ |
| 72 | 3 | 2.926611193156112202490 | 0 | 220167 | 1.2996·10⁻⁷ |
| 73 | 1 | 2.005466078596989384580 | 200054 | 2183388 | 4.3288·10⁻¹³ |
| 73 | 2 | 2.083907790554014458287 | 596946 | 360494 | 1.5621·10⁻¹³ |
| 73 | 3 | 2.924384624895661808430 | 0 | 226847 | 2.2644·10⁻⁷ |
| 74 | 1 | 2.005615077802303610166 | 201253 | 2178145 | 1.6341·10⁻¹³ |
| 74 | 2 | 2.086401492712123290410 | 529196 | 624013 | 4.7626·10⁻¹⁴ |
| 74 | 3 | 2.922114430339834289967 | 0 | 233657 | 2.9938·10⁻⁸ |
| 75 | 1 | 2.005766077011297318682 | 202443 | 2172932 | 2.9565·10⁻¹³ |
| 75 | 2 | 2.088942597342346071565 | 336923 | 1385482 | 6.2882·10⁻¹⁴ |
| 75 | 3 | 2.919799833399494190672 | 0 | 240601 | 9.7671·10⁻⁸ |
| 76 | 1 | 2.005919076223416509908 | 203624 | 2167749 | 2.7560·10⁻¹³ |
| 76 | 2 | 2.091531913919721411824 | 363071 | 1273122 | 4.6782·10⁻¹³ |
| 76 | 3 | 2.917440024600153049885 | 0 | 247681 | 2.8683·10⁻⁷ |
| 77 | 1 | 2.006074075438142256762 | 204797 | 2162592 | 1.3988·10⁻¹³ |
| 77 | 2 | 2.094170287205659421426 | 287067 | 1569223 | 5.4206·10⁻¹³ |
| 77 | 3 | 2.915034159180915782634 | 0 | 254898 | 8.6015·10⁻⁸ |
| 78 | 1 | 2.006231074654988062849 | 205964 | 2157453 | 5.1311·10⁻¹³ |
| 78 | 2 | 2.096858599294995715815 | 321139 | 1424870 | 3.7831·10⁻¹³ |
| 78 | 3 | 2.912581355047429317059 | 0 | 262257 | 2.7977·10⁻⁷ |
| 79 | 1 | 2.006390073873497449165 | 207124 | 2152336 | 3.8325·10⁻¹³ |
| 79 | 2 | 2.099597771822942175014 | 6343 | 2675837 | 3.1178·10⁻¹³ |
| 79 | 3 | 2.910080690564934248318 | 0 | 269759 | 2.7980·10⁻⁷ |
| 80 | 1 | 2.006551073093241747528 | 208279 | 2147233 | 4.3275·10⁻¹³ |
| 80 | 2 | 2.102388768347431067680 | 8273 | 2659744 | 3.8199·10⁻¹³ |
| 80 | 3 | 2.907531202175922921110 | 0 | 277407 | 1.2254·10⁻⁷ |
| 81 | 1 | 2.006714072313818080761 | 209429 | 2142144 | 2.5872·10⁻¹³ |
| 81 | 2 | 2.105232596924162295836 | 312427 | 1434596 | 4.8658·10⁻¹³ |
| 81 | 3 | 2.904931881825094204763 | 0 | 285205 | 1.3329·10⁻⁷ |
| 82 | 1 | 2.006879071534847511763 | 210575 | 2137065 | 3.7805·10⁻¹⁴ |
| 82 | 2 | 2.108130312893726144433 | 219190 | 1798851 | 2.8305·10⁻¹³ |
| 82 | 3 | 2.902281674172232594594 | 0 | 293156 | 2.5669·10⁻⁷ |
| 83 | 1 | 2.007046070755973345547 | 211719 | 2131988 | 5.2439·10⁻¹³ |
| 83 | 2 | 2.111083021902525699749 | 138397 | 2113165 | 6.7952·10⁻¹⁵ |
| 83 | 3 | 2.899579473571287491475 | 0 | 301262 | 5.3764·10⁻⁸ |
| 84 | 1 | 2.007215069976859569953 | 212859 | 2126921 | 2.7137·10⁻¹³ |
| 84 | 2 | 2.114091883181910890050 | 383431 | 1124002 | 4.1765·10⁻¹³ |
| 84 | 3 | 2.896824120791240720462 | 0 | 309528 | 3.1945·10⁻⁸ |
| 85 | 1 | 2.007386069197189422251 | 213997 | 2121856 | 7.3091·10⁻¹⁴ |
| 85 | 2 | 2.117158113113015415301 | 564802 | 389319 | 2.6605·10⁻¹³ |
| 85 | 3 | 2.894014399451271034471 | 45266 | 136893 | 3.2998·10⁻¹³ |
| 86 | 1 | 2.007559068416664070161 | 215134 | 2116789 | 1.8627·10⁻¹³ |
| 86 | 2 | 2.120282989108324644974 | 183167 | 1906485 | 2.3474·10⁻¹³ |
| 86 | 3 | 2.891149032139187535463 | 0 | 326554 | 2.7173·10⁻⁷ |
| 87 | 1 | 2.007734067635001396960 | 216270 | 2111720 | 3.2879·10⁻¹³ |
| 87 | 2 | 2.123467853845075532621 | 421704 | 942782 | 1.2379·10⁻¹³ |
| 87 | 3 | 2.888226676178030974757 | 0 | 335321 | 2.4659·10⁻⁷ |
| 88 | 1 | 2.007911066851934881401 | 217405 | 2106649 | 2.3414·10⁻¹³ |
| 88 | 2 | 2.126714119890292817572 | 537791 | 468695 | 2.1087·10⁻¹³ |
| 88 | 3 | 2.885245919001038671413 | 0 | 344263 | 1.5351·10⁻⁷ |
| 89 | 1 | 2.008090066067212564090 | 218540 | 2101572 | 2.0590·10⁻¹³ |
| 89 | 2 | 2.130023274762712208401 | 253892 | 1594364 | 4.4323·10⁻¹³ |
| 89 | 3 | 2.882205273089722362389 | 0 | 353385 | 1.7165·10⁻⁷ |
| 90 | 1 | 2.008271065280596092767 | 219675 | 2096489 | 5.7419·10⁻¹⁵ |
| 90 | 2 | 2.133396886483166944697 | 347566 | 1209547 | 4.2096·10⁻¹³ |
| 90 | 3 | 2.879103170423482595492 | 0 | 362691 | 6.6317·10⁻⁸ |
| 91 | 1 | 2.008454064491859839692 | 220812 | 2091392 | 5.1912·10⁻¹³ |
| 91 | 2 | 2.136836609672383662688 | 240494 | 1627516 | 4.8426·10⁻¹³ |
| 91 | 3 | 2.875937956381813746364 | 0 | 372187 | 1.8288·10⁻⁷ |
| 92 | 1 | 2.008639063700790084976 | 221949 | 2086289 | 4.2122·10⁻¹³ |
| 92 | 2 | 2.140344192263746607406 | 386392 | 1033401 | 8.0415·10⁻¹⁴ |
| 92 | 3 | 2.872707883031540622991 | 0 | 381877 | 1.0675·10⁻⁷ |
| 93 | 1 | 2.008826062907184260287 | 223087 | 2081176 | 6.5038·10⁻¹⁴ |
| 93 | 2 | 2.143921482908689435460 | 457687 | 737489 | 4.8641·10⁻¹³ |
| 93 | 3 | 2.869411101721427419215 | 19315 | 314507 | 4.1363·10⁻¹³ |
| 94 | 1 | 2.009015062110850247890 | 224228 | 2076045 | 3.6954·10⁻¹³ |
| 94 | 2 | 2.147570439164259206701 | 530771 | 434206 | 4.5409·10⁻¹³ |
| 94 | 3 | 2.866045654894614424042 | 0 | 401864 | 2.0621·10⁻⁷ |
| 95 | 1 | 2.009206061311605730434 | 225370 | 2070904 | 4.1327·10⁻¹⁴ |
| 95 | 2 | 2.151293136566434162115 | 469677 | 667414 | 4.9274·10⁻¹³ |
| 95 | 3 | 2.862609467015300893950 | 0 | 412172 | 1.5373·10⁻⁸ |
| 96 | 1 | 2.009399060509277587338 | 226515 | 2065745 | 1.8368·10⁻¹⁴ |
| 96 | 2 | 2.155091778709418242539 | 507931 | 503002 | 9.5568·10⁻¹⁴ |
| 96 | 3 | 2.859100334489451137795 | 0 | 422700 | 2.1315·10⁻⁷ |
| 97 | 1 | 2.009594059703701333991 | 227663 | 2060568 | 1.3618·10⁻¹³ |
| 97 | 2 | 2.158968708470942951459 | 628351 | 9691 | 1.1835·10⁻¹³ |
| 97 | 3 | 2.855515914439493214805 | 0 | 433453 | 1.2335·10⁻⁷ |
| 98 | 1 | 2.009791058894720600350 | 228814 | 2055373 | 2.3841·10⁻¹³ |
| 98 | 2 | 2.162926420547282154176 | 540479 | 349306 | 2.1683·10⁻¹⁴ |
| 98 | 3 | 2.851853712169304656829 | 0 | 444440 | 2.5126·10⁻⁷ |
| 99 | 1 | 2.009990058082186645773 | 229968 | 2050160 | 1.7630·10⁻¹³ |
| 99 | 2 | 2.166967575490106999528 | 255319 | 1477823 | 4.3714·10⁻¹³ |
| 99 | 3 | 2.848111067127358031766 | 0 | 455668 | 2.6966·10⁻⁷ |
| 100 | 1 | 2.010191057265957907272 | 231126 | 2044925 | 3.6385·10⁻¹³ |
| 100 | 2 | 2.171095015471585302470 | 56955 | 2258897 | 4.9545·10⁻¹³ |
| 100 | 3 | 2.844285137141622012745 | 0 | 467145 | 3.0537·10⁻⁹ |
| 101 | 1 | 2.010394056445899578556 | 232287 | 2039672 | 1.1070·10⁻¹³ |
| 101 | 2 | 2.175311782045669298309 | 470585 | 591726 | 2.3259·10⁻¹³ |
| 101 | 3 | 2.840372880658274044840 | 0 | 478882 | 7.6534·10⁻⁸ |
| 102 | 1 | 2.010599055621883217502 | 233453 | 2034393 | 3.9951·10⁻¹³ |
| 102 | 2 | 2.179621136224113511299 | 426384 | 755602 | 5.4829·10⁻¹⁴ |
| 102 | 3 | 2.836371036665682869005 | 0 | 490888 | 2.2909·10⁻⁷ |
| 103 | 1 | 2.010806054793786379878 | 234623 | 2029092 | 5.5229·10⁻¹³ |
| 103 | 2 | 2.184026581247727869170 | 218514 | 1573866 | 5.2898·10⁻¹³ |
| 103 | 3 | 2.832276101923155773824 | 76511 | 197128 | 3.4440·10⁻¹³ |
| 104 | 1 | 2.011015053961492277332 | 235797 | 2023769 | 4.5224·10⁻¹³ |
| 104 | 2 | 2.188531888509684941190 | 258459 | 1400570 | 4.0030·10⁻¹³ |
| 104 | 3 | 2.828084305037631699461 | 0 | 515748 | 1.5699·10⁻⁷ |
| 105 | 1 | 2.011226053124889457820 | 236976 | 2018420 | 5.4348·10⁻¹³ |
| 105 | 2 | 2.193141127182253573150 | 421704 | 733762 | 4.1052·10⁻¹³ |
| 105 | 3 | 2.823791576836947922243 | 0 | 528626 | 9.1768·10⁻⁸ |
| 106 | 1 | 2.011439052283871506822 | 238159 | 2013049 | 1.6402·10⁻¹³ |
| 106 | 2 | 2.197858698216231082061 | 586530 | 60305 | 1.1623·10⁻¹³ |
| 106 | 3 | 2.819393516370408158746 | 0 | 541820 | 2.7514·10⁻⁸ |
| 107 | 1 | 2.011654051438336767797 | 239348 | 2007648 | 3.2334·10⁻¹³ |
| 107 | 2 | 2.202689373530352775892 | 563477 | 138025 | 9.2310·10⁻¹⁴ |
| 107 | 3 | 2.814885351719373325609 | 0 | 555345 | 1.9231·10⁻⁷ |
| 108 | 1 | 2.011871050588188080491 | 240542 | 2002221 | 3.6870·10⁻¹³ |
| 108 | 2 | 2.207638341395097256484 | 13650 | 2322487 | 2.0030·10⁻¹³ |
| 108 | 3 | 2.810261894613456498309 | 0 | 569215 | 6.4561·10⁻⁸ |
| 109 | 1 | 2.012090049733332535789 | 241741 | 1996768 | 2.0720·10⁻¹³ |
| 109 | 2 | 2.212711259253742006372 | 153641 | 1747304 | 4.6547·10⁻¹⁵ |
| 109 | 3 | 2.805517487609467569481 | 23751 | 488444 | 5.3773·10⁻¹⁴ |
| 110 | 1 | 2.012311048873681245944 | 242946 | 1991285 | 3.0551·10⁻¹³ |
| 110 | 2 | 2.217914315529807505883 | 44280 | 2169139 | 3.4218·10⁻¹³ |
| 110 | 3 | 2.800645942283969361598 | 0 | 598063 | 1.0395·10⁻⁷ |
| 111 | 1 | 2.012534048009149129085 | 244156 | 1985776 | 2.2994·10⁻¹⁴ |
| 111 | 2 | 2.223254302366918651222 | 59696 | 2091455 | 2.2456·10⁻¹³ |
| 111 | 3 | 2.795640466493416424380 | 77070 | 304799 | 4.6826·10⁻¹³ |
| 112 | 1 | 2.012759047139654706986 | 245373 | 1980233 | 3.8927·10⁻¹³ |
| 112 | 2 | 2.228738701766256723440 | 532276 | 184681 | 1.3677·10⁻¹³ |
| 112 | 3 | 2.790493578236703268042 | 0 | 628520 | 6.4494·10⁻⁸ |
| 113 | 1 | 2.012986046265119915197 | 246595 | 1974664 | 2.1519·10⁻¹³ |
| 113 | 2 | 2.234375788272711736051 | 367827 | 825566 | 1.5393·10⁻¹³ |
| 113 | 3 | 2.785197002969012205565 | 0 | 644410 | 1.5133·10⁻⁷ |
| 114 | 1 | 2.013215045385469924653 | 247824 | 1969061 | 5.3701·10⁻¹³ |
| 114 | 2 | 2.240174752277069476709 | 423631 | 584953 | 3.0120·10⁻¹³ |
| 114 | 3 | 2.779741550299626489396 | 0 | 660776 | 2.7299·10⁻⁸ |
| 115 | 1 | 2.013446044500632974001 | 249058 | 1963432 | 1.7187·10⁻¹³ |
| 115 | 2 | 2.246145849239875394977 | 239843 | 1302192 | 3.9571·10⁻¹³ |
| 115 | 3 | 2.774116964768066591357 | 0 | 677650 | 1.0359·10⁻⁷ |
| 116 | 1 | 2.013679043610540211895 | 250299 | 1957769 | 1.6202·10⁻¹³ |
| 116 | 2 | 2.252300581837738536021 | 111627 | 1796592 | 3.5872·10⁻¹³ |
| 116 | 3 | 2.768311743697786426661 | 0 | 695066 | 2.1085·10⁻⁷ |
| 117 | 1 | 2.013914042715125548595 | 251547 | 1952072 | 4.4138·10⁻¹³ |
| 117 | 2 | 2.258651924385794954043 | 85196 | 1883262 | 3.9906·10⁻¹³ |
| 117 | 3 | 2.762312912773710088868 | 0 | 713062 | 4.1431·10⁻⁸ |
| 118 | 1 | 2.014151041814325516258 | 252801 | 1946345 | 3.9093·10⁻¹³ |
| 118 | 2 | 2.265214602206199391673 | 54947 | 1984570 | 3.2521·10⁻¹³ |
| 118 | 3 | 2.756105746673740310214 | 0 | 731684 | 2.0332·10⁻⁷ |
| 119 | 1 | 2.014390040908079137322 | 254062 | 1940584 | 5.0524·10⁻¹³ |
| 119 | 2 | 2.272005443364903658658 | 330335 | 862645 | 1.0162·10⁻¹³ |
| 119 | 3 | 2.749673417331980214530 | 0 | 750981 | 2.0177·10⁻⁷ |
| 120 | 1 | 2.014631039996327800474 | 255329 | 1934793 | 1.7014·10⁻¹³ |
| 120 | 2 | 2.279043827136446529993 | 228637 | 1248322 | 2.2855·10⁻¹³ |
| 120 | 3 | 2.742996545473943543145 | 16503 | 704999 | 3.7236·10⁻¹³ |
| 121 | 1 | 2.014874039079015143695 | 256604 | 1928964 | 4.4039·10⁻¹³ |
| 121 | 2 | 2.286352263893121020251 | 31147 | 2016357 | 2.3104·10⁻¹³ |
| 121 | 3 | 2.736052620727387497518 | 0 | 791843 | 6.0105·10⁻⁸ |
| 122 | 1 | 2.015119038156086943922 | 257885 | 1923105 | 1.5065·10⁻¹³ |
| 122 | 2 | 2.293957156872199441279 | 211997 | 1270142 | 2.3608·10⁻¹³ |
| 122 | 3 | 2.728815239855087791867 | 0 | 813555 | 6.3348·10⁻⁹ |
| 123 | 1 | 2.015366037227491012912 | 259174 | 1917208 | 3.5984·10⁻¹³ |
| 123 | 2 | 2.301889820920493364136 | 204415 | 1276672 | 5.4576·10⁻¹³ |
| 123 | 3 | 2.721253088010278795378 | 0 | 836242 | 1.8131·10⁻⁷ |
| 124 | 1 | 2.015615036293177098907 | 260470 | 1911277 | 4.6216·10⁻¹³ |
| 124 | 2 | 2.310187873000887817513 | 97808 | 1678206 | 3.4875·10⁻¹³ |
| 124 | 3 | 2.713328548230119432114 | 57527 | 629907 | 2.2235·10⁻¹³ |
| 125 | 1 | 2.015866035353096793734 | 261773 | 1905312 | 4.0919·10⁻¹³ |
| 125 | 2 | 2.318897175308478055941 | 140155 | 1482690 | 4.0586·10⁻¹³ |
| 125 | 3 | 2.704995758319556505709 | 0 | 885014 | 1.7095·10⁻⁷ |
| 126 | 1 | 2.016119034407203444998 | 263083 | 1899313 | 1.5429·10⁻¹³ |
| 126 | 2 | 2.328074626119667981076 | 0 | 2015778 | 4.7517·10⁻⁸ |
| 126 | 3 | 2.696197820002226365893 | 194890 | 131847 | 3.4465·10⁻¹³ |
| 127 | 1 | 2.016374033455452073058 | 264401 | 1893276 | 2.0802·10⁻¹³ |
| 127 | 2 | 2.337792300239666515501 | 485991 | 42660 | 2.6389·10⁻¹³ |
| 127 | 3 | 2.686862658472958617707 | 0 | 939413 | 5.5493·10⁻⁸ |
| 128 | 1 | 2.016631032497799292479 | 265727 | 1887201 | 5.2702·10⁻¹³ |
| 128 | 2 | 2.348143835373717493135 | 106705 | 1528750 | 2.6601·10⁻¹³ |
| 128 | 3 | 2.676896636026546309648 | 0 | 969311 | 2.4465·10⁻⁸ |
| 129 | 1 | 2.016890031534203237702 | 267060 | 1881092 | 5.1384·10⁻¹³ |
| 129 | 2 | 2.359254763282525933912 | 219247 | 1045249 | 1.8134·10⁻¹³ |
| 129 | 3 | 2.666174220902319733316 | 119806 | 522254 | 9.2546·10⁻¹⁴ |
| 130 | 1 | 2.017151030564623492660 | 268400 | 1874949 | 1.2809·10⁻¹³ |
| 130 | 2 | 2.371300252099132586040 | 0 | 1886101 | 4.4051·10⁻⁸ |
| 130 | 3 | 2.654520244967271951543 | 94553 | 658228 | 2.2379·10⁻¹³ |
| 131 | 1 | 2.017414029589021024111 | 269749 | 1868764 | 4.4183·10⁻¹³ |
| 131 | 2 | 2.384538032164086104528 | 296071 | 662103 | 1.3557·10⁻¹³ |
| 131 | 3 | 2.641676977880886686531 | 0 | 1074970 | 2.6582·10⁻⁹ |
| 132 | 1 | 2.017679028607358118464 | 271105 | 1862545 | 3.0624·10⁻¹³ |
| 132 | 2 | 2.399376268376472776422 | 447890 | 10312 | 4.8842·10⁻¹³ |
| 132 | 3 | 2.627236254744108657791 | 119245 | 641312 | 2.9254·10⁻¹³ |
| 133 | 1 | 2.017946027619598321886 | 272469 | 1856288 | 2.4043·10⁻¹³ |
| 133 | 2 | 2.416536454331754090603 | 86572 | 1404104 | 2.8698·10⁻¹³ |
| 133 | 3 | 2.610476581961506072231 | 156231 | 543647 | 2.0025·10⁻¹³ |
| 134 | 1 | 2.018215026625706383507 | 273841 | 1849993 | 2.0914·10⁻¹³ |
| 134 | 2 | 2.437553436854780217350 | 85454 | 1345525 | 1.6257·10⁻¹³ |
| 134 | 3 | 2.589863112708257201401 | 0 | 1230412 | 9.2868·10⁻⁸ |
| 135 | 1 | 2.018486025625648201531 | 275221 | 1843660 | 1.7826·10⁻¹³ |
| 135 | 2 | 2.467337485700205514062 | 0 | 1597989 | 2.7018·10⁻⁸ |
| 135 | 3 | 2.560485577229734929651 | 242234 | 349608 | 7.6675·10⁻¹⁴ |
| 136 | 1 | 2.018759024619390772082 | 276609 | 1837289 | 1.1481·10⁻¹³ |
| 137 | 1 | 2.019034023606902140647 | 278006 | 1830876 | 5.4237·10⁻¹³ |
| 138 | 1 | 2.019311022588151355939 | 279410 | 1824429 | 3.1888·10⁻¹³ |
| 139 | 1 | 2.019590021563108426069 | 280823 | 1817940 | 5.2547·10⁻¹³ |
| 140 | 1 | 2.019871020531744276871 | 282243 | 1811417 | 2.1954·10⁻¹⁴ |
| 141 | 1 | 2.020154019494030712287 | 283673 | 1804848 | 4.4679·10⁻¹³ |
| 142 | 1 | 2.020439018449940376672 | 285110 | 1798245 | 1.0596·10⁻¹³ |
| 143 | 1 | 2.020726017399446718926 | 286556 | 1791600 | 8.4038·10⁻¹⁴ |
| 144 | 1 | 2.021015016342523958355 | 288011 | 1784913 | 3.5522·10⁻¹³ |
| 145 | 1 | 2.021306015279147052155 | 289474 | 1778188 | 3.3893·10⁻¹³ |
| 146 | 1 | 2.021599014209291664444 | 290945 | 1771425 | 1.0820·10⁻¹⁴ |
| 147 | 1 | 2.021894013132934136748 | 292426 | 1764616 | 4.5834·10⁻¹³ |
| 148 | 1 | 2.022191012050051459870 | 293915 | 1757769 | 5.4738·10⁻¹³ |
| 149 | 1 | 2.022490010960621247067 | 295412 | 1750884 | 2.5554·10⁻¹³ |
| 150 | 1 | 2.022791009864621708462 | 296918 | 1743957 | 1.1660·10⁻¹³ |
| 151 | 1 | 2.023094008762031626636 | 298433 | 1736988 | 1.0933·10⁻¹³ |
| 152 | 1 | 2.023399007652830333327 | 299957 | 1729977 | 2.1307·10⁻¹³ |
| 153 | 1 | 2.023706006536997687184 | 301490 | 1722924 | 4.0768·10⁻¹³ |
| 154 | 1 | 2.024015005414514052525 | 303031 | 1715833 | 1.1796·10⁻¹³ |
| 155 | 1 | 2.024326004285360279040 | 304582 | 1708696 | 4.3588·10⁻¹³ |
| 156 | 1 | 2.024639003149517682403 | 306141 | 1701521 | 2.3164·10⁻¹³ |
| 157 | 1 | 2.024954002006968025729 | 307709 | 1694304 | 4.2564·10⁻¹⁴ |
| 158 | 1 | 2.025271000857693501854 | 309287 | 1687041 | 4.0638·10⁻¹³ |
| 159 | 1 | 2.025589999701676716382 | 310873 | 1679740 | 1.9461·10⁻¹³ |
| 160 | 1 | 2.025910998538900671467 | 312469 | 1672393 | 5.0135·10⁻¹³ |
| 161 | 1 | 2.026233997369348750296 | 314073 | 1665008 | 1.9888·10⁻¹³ |
| 162 | 1 | 2.026558996193004702229 | 315687 | 1657577 | 3.8206·10⁻¹³ |
| 163 | 1 | 2.026885995009852628582 | 317310 | 1650104 | 4.7943·10⁻¹³ |
| 164 | 1 | 2.027214993819876968999 | 318942 | 1642589 | 4.7543·10⁻¹³ |
| 165 | 1 | 2.027545992623062488407 | 320583 | 1635032 | 3.5484·10⁻¹³ |
| 166 | 1 | 2.027878991419394264507 | 322233 | 1627433 | 1.0271·10⁻¹³ |
| 167 | 1 | 2.028213990208857675790 | 323893 | 1619788 | 2.6000·10⁻¹³ |
| 168 | 1 | 2.028550988991438390047 | 325562 | 1612101 | 2.5681·10⁻¹³ |
| 169 | 1 | 2.028889987767122353347 | 327240 | 1604372 | 7.9090·10⁻¹⁴ |
| 170 | 1 | 2.029230986535895779470 | 328928 | 1596597 | 2.6860·10⁻¹³ |
| 171 | 1 | 2.029573985297745139764 | 330625 | 1588780 | 2.5627·10⁻¹³ |
| 172 | 1 | 2.029918984052657153411 | 332331 | 1580921 | 2.8812·10⁻¹⁴ |
| 173 | 1 | 2.030265982800618778089 | 334047 | 1573016 | 1.2873·10⁻¹³ |
| 174 | 1 | 2.030614981541617200998 | 335773 | 1565065 | 5.4323·10⁻¹³ |
| 175 | 1 | 2.030965980275639830248 | 337507 | 1557076 | 1.4860·10⁻¹³ |
| 176 | 1 | 2.031318979002674286585 | 339251 | 1549041 | 4.3571·10⁻¹⁴ |
| 177 | 1 | 2.031673977722708395438 | 341005 | 1540960 | 2.1596·10⁻¹³ |
| 178 | 1 | 2.032030976435730179281 | 342768 | 1532837 | 9.8257·10⁻¹⁴ |
| 179 | 1 | 2.032389975141727850287 | 344541 | 1524668 | 2.3420·10⁻¹³ |
| 180 | 1 | 2.032750973840689803268 | 346323 | 1516457 | 5.6662·10⁻¹⁴ |
| 181 | 1 | 2.033113972532604608882 | 348115 | 1508200 | 1.0974·10⁻¹³ |
| 182 | 1 | 2.033478971217461007107 | 349917 | 1499897 | 3.8218·10⁻¹³ |
| 183 | 1 | 2.033845969895247900949 | 351728 | 1491552 | 3.0734·10⁻¹³ |
| 184 | 1 | 2.034214968565954350403 | 353549 | 1483161 | 4.2984·10⁻¹³ |
| 185 | 1 | 2.034585967229569566626 | 355379 | 1474728 | 1.8331·10⁻¹³ |
| 186 | 1 | 2.034958965886082906340 | 357219 | 1466249 | 1.1269·10⁻¹³ |
| 187 | 1 | 2.035333964535483866434 | 359069 | 1457724 | 2.0746·10⁻¹³ |
| 188 | 1 | 2.035710963177762078767 | 360929 | 1449153 | 4.5725·10⁻¹³ |
| 189 | 1 | 2.036089961812907305166 | 362798 | 1440540 | 2.9628·10⁻¹³ |
| 190 | 1 | 2.036470960440909432603 | 364677 | 1431881 | 2.6999·10⁻¹³ |
| 191 | 1 | 2.036853959061758468548 | 366566 | 1423176 | 3.6838·10⁻¹³ |
| 192 | 1 | 2.037238957675444536489 | 368464 | 1414429 | 2.6018·10⁻¹⁴ |
| 193 | 1 | 2.037625956281957871616 | 370373 | 1405632 | 3.4425·10⁻¹³ |
| 194 | 1 | 2.038014954881288816658 | 372291 | 1396793 | 2.0231·10⁻¹³ |
| 195 | 1 | 2.038405953473427817868 | 374219 | 1387908 | 1.4621·10⁻¹³ |
| 196 | 1 | 2.038798952058365421148 | 376157 | 1378977 | 1.6648·10⁻¹³ |
| 197 | 1 | 2.039193950636092268316 | 378105 | 1370000 | 2.5377·10⁻¹³ |
| 198 | 1 | 2.039590949206599093499 | 380063 | 1360977 | 3.9881·10⁻¹³ |
| 199 | 1 | 2.039989947769876719655 | 382030 | 1351912 | 3.6878·10⁻¹⁴ |
| 200 | 1 | 2.040390946325916055214 | 384008 | 1342797 | 2.6998·10⁻¹³ |
| 201 | 1 | 2.040793944874708090835 | 385996 | 1333636 | 5.3355·10⁻¹³ |
| 202 | 1 | 2.041198943416243896276 | 387993 | 1324433 | 2.6312·10⁻¹³ |
| 203 | 1 | 2.041605941950514617368 | 390000 | 1315184 | 5.3745·10⁻¹⁵ |
| 204 | 1 | 2.042014940477511473098 | 392018 | 1305885 | 3.0709·10⁻¹³ |
| 205 | 1 | 2.042425938997225752784 | 394045 | 1296544 | 4.8454·10⁻¹⁴ |
| 206 | 1 | 2.042838937509648813349 | 396083 | 1287153 | 3.3192·10⁻¹³ |
| 207 | 1 | 2.043253936014772076686 | 398130 | 1277720 | 3.7821·10⁻¹⁴ |
| 208 | 1 | 2.043670934512587027113 | 400188 | 1268237 | 2.6873·10⁻¹³ |
| 209 | 1 | 2.044089933003085208905 | 402256 | 1258708 | 4.6064·10⁻¹³ |
| 210 | 1 | 2.044510931486258223919 | 404333 | 1249137 | 4.9617·10⁻¹⁴ |
| 211 | 1 | 2.044933929962097729287 | 406421 | 1239516 | 1.3840·10⁻¹³ |
| 212 | 1 | 2.045358928430595435190 | 408519 | 1229849 | 1.6317·10⁻¹³ |
| 213 | 1 | 2.045785926891743102706 | 410627 | 1220136 | 1.1567·10⁻¹³ |
| 214 | 1 | 2.046214925345532541721 | 412746 | 1210373 | 5.4327·10⁻¹³ |
| 215 | 1 | 2.046645923791955608917 | 414874 | 1200568 | 3.2671·10⁻¹³ |
| 216 | 1 | 2.047078922231004205814 | 417012 | 1190717 | 1.3471·10⁻¹⁴ |
| 217 | 1 | 2.047513920662670276884 | 419161 | 1180816 | 1.5102·10⁻¹³ |
| 218 | 1 | 2.047950919086945807722 | 421320 | 1170869 | 1.7581·10⁻¹³ |
| 219 | 1 | 2.048389917503822823272 | 423489 | 1160876 | 7.9867·10⁻¹⁴ |
| 220 | 1 | 2.048830915913293386111 | 425669 | 1150833 | 4.1079·10⁻¹³ |
| 221 | 1 | 2.049273914315349594793 | 427858 | 1140748 | 4.9584·10⁻¹⁴ |
| 222 | 1 | 2.049718912709983582231 | 430058 | 1130613 | 9.9484·10⁻¹⁴ |
| 223 | 1 | 2.050165911097187514146 | 432269 | 1120428 | 5.5265·10⁻¹³ |
| 224 | 1 | 2.050614909476953587549 | 434489 | 1110201 | 2.9019·10⁻¹³ |
| 225 | 1 | 2.051065907849274029283 | 436720 | 1099924 | 4.1542·10⁻¹³ |
| 226 | 1 | 2.051518906214141094599 | 438961 | 1089601 | 3.6505·10⁻¹³ |
| 227 | 1 | 2.051973904571547065780 | 441212 | 1079232 | 1.3136·10⁻¹³ |
| 228 | 1 | 2.052430902921484250814 | 443474 | 1068813 | 2.6221·10⁻¹³ |
| 229 | 1 | 2.052889901263944982090 | 445746 | 1058348 | 1.9439·10⁻¹³ |
| 230 | 1 | 2.053350899598921615154 | 448029 | 1047833 | 4.7580·10⁻¹³ |
| 231 | 1 | 2.053813897926406527486 | 450322 | 1037272 | 5.4325·10⁻¹³ |
| 232 | 1 | 2.054278896246392117322 | 452625 | 1026665 | 3.8917·10⁻¹³ |
| 233 | 1 | 2.054745894558870802508 | 454938 | 1016012 | 5.9528·10⁻¹⁵ |
| 234 | 1 | 2.055214892863835019393 | 457263 | 1005305 | 4.9715·10⁻¹³ |
| 235 | 1 | 2.055685891161277221746 | 459597 | 994556 | 1.8855·10⁻¹³ |
| 236 | 1 | 2.056158889451189879713 | 461942 | 983757 | 1.8374·10⁻¹³ |
| 237 | 1 | 2.056633887733565478802 | 464298 | 972908 | 4.7519·10⁻¹³ |
| 238 | 1 | 2.057110886008396518893 | 466664 | 962013 | 4.9987·10⁻¹³ |
| 239 | 1 | 2.057589884275675513286 | 469040 | 951072 | 2.5027·10⁻¹³ |
| 240 | 1 | 2.058070882535394987769 | 471427 | 940081 | 2.7448·10⁻¹³ |
| 241 | 1 | 2.058553880787547479715 | 473824 | 929044 | 9.4932·10⁻¹⁵ |
| 242 | 1 | 2.059038879032125537207 | 476232 | 917957 | 3.3927·10⁻¹⁵ |
| 243 | 1 | 2.059525877269121718186 | 478651 | 906820 | 2.4874·10⁻¹³ |
| 244 | 1 | 2.060014875498528589622 | 481080 | 895637 | 1.8256·10⁻¹³ |
| 245 | 1 | 2.060505873720338726712 | 483520 | 884404 | 3.5297·10⁻¹³ |
| 246 | 1 | 2.060998871934544712100 | 485970 | 873125 | 1.9701·10⁻¹³ |
| 247 | 1 | 2.061493870141139135114 | 488431 | 861796 | 2.6281·10⁻¹³ |
| 248 | 1 | 2.061990868340114591032 | 490903 | 850417 | 5.4297·10⁻¹³ |
| 249 | 1 | 2.062489866531463680365 | 493385 | 838992 | 4.7455·10⁻¹³ |
| 250 | 1 | 2.062990864715179008157 | 495877 | 827521 | 5.0138·10⁻¹⁴ |
| 251 | 1 | 2.063493862891253183306 | 498381 | 815996 | 3.7345·10⁻¹³ |
| 252 | 1 | 2.063998861059678817912 | 500895 | 804425 | 3.2600·10⁻¹³ |
| 253 | 1 | 2.064505859220448526628 | 503420 | 792804 | 4.5596·10⁻¹³ |
| 254 | 1 | 2.065014857373554926042 | 505955 | 781137 | 2.0038·10⁻¹³ |
| 255 | 1 | 2.065525855518990634065 | 508501 | 769420 | 1.0744·10⁻¹³ |
| 256 | 1 | 2.066038853656748269347 | 511058 | 757653 | 1.6976·10⁻¹³ |
| 257 | 1 | 2.066553851786820450700 | 513626 | 745836 | 3.7995·10⁻¹³ |
| 258 | 1 | 2.067070849909199796540 | 516204 | 733973 | 1.7508·10⁻¹³ |
| 259 | 1 | 2.067589848023878924342 | 518793 | 722060 | 1.0332·10⁻¹³ |
| 260 | 1 | 2.068110846130850450113 | 521393 | 710097 | 1.5729·10⁻¹³ |
| 261 | 1 | 2.068633844230106987877 | 524004 | 698084 | 3.2960·10⁻¹³ |
| 262 | 1 | 2.069158842321641149171 | 526625 | 686025 | 5.7319·10⁻¹⁴ |
| 263 | 1 | 2.069685840405445542561 | 529258 | 673912 | 4.4414·10⁻¹³ |
| 264 | 1 | 2.070214838481512773166 | 531901 | 661753 | 3.7158·10⁻¹³ |
| 265 | 1 | 2.070745836549835442193 | 534555 | 649544 | 3.8779·10⁻¹³ |
| 266 | 1 | 2.071278834610406146487 | 537220 | 637285 | 4.8536·10⁻¹³ |
| 267 | 1 | 2.071813832663217478096 | 539895 | 624980 | 1.0133·10⁻¹³ |
| 268 | 1 | 2.072350830708262023840 | 542582 | 612621 | 3.3940·10⁻¹³ |
| 269 | 1 | 2.072889828745532364893 | 545279 | 600216 | 8.1050·10⁻¹⁴ |
| 270 | 1 | 2.073430826775021076383 | 547988 | 587757 | 4.2994·10⁻¹³ |
| 271 | 1 | 2.073973824796720726994 | 550707 | 575252 | 2.6755·10⁻¹³ |
| 272 | 1 | 2.074518822810623878578 | 553437 | 562697 | 1.4200·10⁻¹³ |
| 273 | 1 | 2.075065820816723085785 | 556178 | 550092 | 4.5827·10⁻¹⁴ |
| 274 | 1 | 2.075614818815010895694 | 558931 | 537433 | 5.2714·10⁻¹³ |
| 275 | 1 | 2.076165816805479847457 | 561694 | 524728 | 4.6737·10⁻¹³ |
| 276 | 1 | 2.076718814788122471953 | 564468 | 511973 | 4.1460·10⁻¹³ |
| 277 | 1 | 2.077273812762931291447 | 567253 | 499168 | 3.6136·10⁻¹³ |
| 278 | 1 | 2.077830810729898819261 | 570049 | 486313 | 3.0015·10⁻¹³ |
| 279 | 1 | 2.078389808689017559453 | 572856 | 473408 | 2.2349·10⁻¹³ |
| 280 | 1 | 2.078950806640280006501 | 575674 | 460453 | 1.2387·10⁻¹³ |
| 281 | 1 | 2.079513804583678644999 | 578504 | 447444 | 5.4932·10⁻¹³ |
| 282 | 1 | 2.080078802519205949355 | 581344 | 434389 | 3.8121·10⁻¹³ |
| 283 | 1 | 2.080645800446854383503 | 584195 | 421284 | 1.6756·10⁻¹³ |
| 284 | 1 | 2.081214798366616400617 | 587058 | 408125 | 4.5638·10⁻¹³ |
| 285 | 1 | 2.081785796278484442836 | 589931 | 394920 | 1.2900·10⁻¹³ |
| 286 | 1 | 2.082358794182450940989 | 592816 | 381661 | 2.8896·10⁻¹³ |
| 287 | 1 | 2.082933792078508314337 | 595712 | 368352 | 3.7312·10⁻¹³ |
| 288 | 1 | 2.083510789966648970311 | 598619 | 354993 | 3.7390·10⁻¹³ |
| 289 | 1 | 2.084089787846865304260 | 1537 | 2741585 | 1.3368·10⁻¹³ |
| 290 | 1 | 2.084670785719149699211 | 604466 | 328125 | 9.4860·10⁻¹⁴ |
| 291 | 1 | 2.085253783583494525626 | 7407 | 2714613 | 2.0535·10⁻¹³ |
| 292 | 1 | 2.085838781439892141165 | 10359 | 2701050 | 3.5196·10⁻¹³ |
| 293 | 1 | 2.086425779288334890466 | 13322 | 2687437 | 3.7703·10⁻¹³ |
| 294 | 1 | 2.087014777128815104915 | 16296 | 2673774 | 2.7290·10⁻¹³ |
| 295 | 1 | 2.087605774961325102432 | 19281 | 2660061 | 3.1885·10⁻¹⁴ |
| 296 | 1 | 2.088198772785857187257 | 22278 | 2646294 | 2.0183·10⁻¹³ |
| 297 | 1 | 2.088793770602403649744 | 25286 | 2632477 | 2.1949·10⁻¹³ |
| 298 | 1 | 2.089390768410956766159 | 28305 | 2618610 | 7.7143·10⁻¹⁴ |
| 299 | 1 | 2.089989766211508798477 | 31336 | 2604689 | 3.2258·10⁻¹³ |
| 300 | 1 | 2.090590764004051994197 | 34378 | 2590718 | 3.9252·10⁻¹³ |
| 301 | 1 | 2.091193761788578586147 | 37431 | 2576697 | 2.7919·10⁻¹³ |
| 302 | 1 | 2.091798759565080792301 | 640495 | 162625 | 1.2479·10⁻¹³ |
| 303 | 1 | 2.092405757333550815600 | 43571 | 2548501 | 2.7109·10⁻¹⁴ |
| 304 | 1 | 2.093014755093980843776 | 646658 | 134325 | 2.2754·10⁻¹⁴ |
| 305 | 1 | 2.093625752846363049176 | 49757 | 2520097 | 5.9461·10⁻¹⁴ |
| 306 | 1 | 2.094238750590689588602 | 52867 | 2505818 | 2.3832·10⁻¹⁴ |
| 307 | 1 | 2.094853748326952603137 | 55989 | 2491485 | 3.1356·10⁻¹³ |
| 308 | 1 | 2.095470746055144217991 | 59122 | 2477102 | 3.6522·10⁻¹³ |
| 309 | 1 | 2.096089743775256542344 | 62266 | 2462669 | 1.7092·10⁻¹³ |
| 310 | 1 | 2.096710741487281669187 | 65422 | 2448182 | 2.7831·10⁻¹³ |
| 311 | 1 | 2.097333739191211675179 | 68589 | 2433645 | 1.2390·10⁻¹³ |
| 312 | 1 | 2.097958736887038620496 | 71768 | 2419054 | 2.5532·10⁻¹³ |
| 313 | 1 | 2.098585734574754548686 | 74958 | 2404413 | 1.0906·10⁻¹³ |
| 314 | 1 | 2.099214732254351486536 | 78160 | 2389718 | 2.3269·10⁻¹³ |
| 315 | 1 | 2.099845729925821443927 | 81373 | 2374973 | 6.2668·10⁻¹⁴ |
| 316 | 1 | 2.100478727589156413704 | 84598 | 2360174 | 1.4654·10⁻¹³ |
| 317 | 1 | 2.101113725244348371545 | 87835 | 2345321 | 4.7629·10⁻¹³ |
| 318 | 1 | 2.101750722891389275830 | 91083 | 2330418 | 4.8831·10⁻¹³ |
| 319 | 1 | 2.102389720530271067519 | 94342 | 2315465 | 1.7455·10⁻¹³ |
| 320 | 1 | 2.103030718160985670026 | 97613 | 2300458 | 8.2492·10⁻¹⁴ |
| 321 | 1 | 2.103673715783524989102 | 100896 | 2285397 | 2.0403·10⁻¹³ |
| 322 | 1 | 2.104318713397880912715 | 104191 | 2270282 | 5.3105·10⁻¹³ |
| 323 | 1 | 2.104965711004045310936 | 107497 | 2255117 | 4.9989·10⁻¹³ |
| 324 | 1 | 2.105614708602010035827 | 110814 | 2239902 | 1.0238·10⁻¹³ |
| 325 | 1 | 2.106265706191766921331 | 114144 | 2224629 | 4.4146·10⁻¹³ |
| 326 | 1 | 2.106918703773307783162 | 117485 | 2209306 | 3.9786·10⁻¹³ |
| 327 | 1 | 2.107573701346624418703 | 120838 | 2193929 | 5.1891·10⁻¹³ |
| 328 | 1 | 2.108230698911708606901 | 124202 | 2178502 | 2.4085·10⁻¹³ |
| 329 | 1 | 2.108889696468552108165 | 127578 | 2163021 | 1.1099·10⁻¹³ |
| 330 | 1 | 2.109550694017146664270 | 130966 | 2147486 | 1.2106·10⁻¹³ |
| 331 | 1 | 2.110213691557483998257 | 134366 | 2131897 | 2.6280·10⁻¹³ |
| 332 | 1 | 2.110878689089555814341 | 137778 | 2116254 | 5.2790·10⁻¹³ |
| 333 | 1 | 2.111545686613353797816 | 141201 | 2100561 | 3.5250·10⁻¹³ |
| 334 | 1 | 2.112214684128869614966 | 144636 | 2084814 | 2.8382·10⁻¹³ |
| 335 | 1 | 2.112885681636094912975 | 148083 | 2069013 | 3.1351·10⁻¹³ |
| 336 | 1 | 2.113558679135021319841 | 151542 | 2053158 | 4.3319·10⁻¹³ |
| 337 | 1 | 2.114233676625640444287 | 155012 | 2037253 | 7.8923·10⁻¹⁴ |
| 338 | 1 | 2.114910674107943875684 | 158495 | 2021290 | 3.5339·10⁻¹³ |
| 339 | 1 | 2.115589671581923183964 | 161989 | 2005277 | 1.3707·10⁻¹³ |
| 340 | 1 | 2.116270669047569919539 | 165496 | 1989206 | 5.3262·10⁻¹³ |
| 341 | 1 | 2.116953666504875613229 | 169014 | 1973085 | 4.2046·10⁻¹³ |
| 342 | 1 | 2.117638663953831776179 | 172544 | 1956910 | 3.4765·10⁻¹³ |
| 343 | 1 | 2.118325661394429899784 | 176086 | 1940681 | 3.0569·10⁻¹³ |
| 344 | 1 | 2.119014658826661455619 | 179640 | 1924398 | 2.8604·10⁻¹³ |
| 345 | 1 | 2.119705656250517895365 | 183206 | 1908061 | 2.8016·10⁻¹³ |
| 346 | 1 | 2.120398653665990650734 | 186784 | 1891670 | 2.7949·10⁻¹³ |
| 347 | 1 | 2.121093651073071133408 | 190374 | 1875225 | 2.7542·10⁻¹³ |
| 348 | 1 | 2.121790648471750734961 | 193976 | 1858726 | 2.5936·10⁻¹³ |
| 349 | 1 | 2.122489645862020826802 | 197590 | 1842173 | 2.2268·10⁻¹³ |
| 350 | 1 | 2.123190643243872760102 | 201216 | 1825566 | 1.5672·10⁻¹³ |
| 351 | 1 | 2.123893640617297865734 | 204854 | 1808905 | 5.2823·10⁻¹⁴ |
| 352 | 1 | 2.124598637982287454209 | 208505 | 1792186 | 4.5784·10⁻¹³ |
| 353 | 1 | 2.125305635338832815614 | 212167 | 1775417 | 2.5197·10⁻¹³ |
| 354 | 1 | 2.126014632686925219554 | 215842 | 1758590 | 5.3757·10⁻¹³ |
| 355 | 1 | 2.126725630026555915088 | 219528 | 1741713 | 1.9480·10⁻¹³ |
| 356 | 1 | 2.127438627357716130677 | 223227 | 1724778 | 3.2599·10⁻¹³ |
| 357 | 1 | 2.128153624680397074123 | 226938 | 1707789 | 3.6679·10⁻¹³ |
| 358 | 1 | 2.128870621994589932515 | 230661 | 1690746 | 3.0839·10⁻¹³ |
| 359 | 1 | 2.129589619300285872172 | 234396 | 1673649 | 1.4196·10⁻¹³ |
| 360 | 1 | 2.130310616597476038592 | 238144 | 1656494 | 4.1420·10⁻¹³ |
| 361 | 1 | 2.131033613886151556400 | 241903 | 1639289 | 5.1197·10⁻¹⁵ |
| 362 | 1 | 2.131758611166303529293 | 245675 | 1622026 | 1.6931·10⁻¹⁴ |
| 363 | 1 | 2.132485608437923039992 | 249460 | 1604705 | 4.4072·10⁻¹³ |
| 364 | 1 | 2.133214605701001150192 | 253256 | 1587334 | 1.5644·10⁻¹³ |
| 365 | 1 | 2.133945602955528900511 | 257065 | 1569905 | 2.6624·10⁻¹³ |
| 366 | 1 | 2.134678600201497310449 | 260886 | 1552422 | 2.0558·10⁻¹³ |
| 367 | 1 | 2.135413597438897378331 | 264720 | 1534881 | 5.2102·10⁻¹³ |
| 368 | 1 | 2.136150594667720081270 | 268565 | 1517290 | 9.2434·10⁻¹⁴ |
| 369 | 1 | 2.136889591887956375117 | 272423 | 1499641 | 2.1873·10⁻¹⁴ |
| 370 | 1 | 2.137630589099597194418 | 276294 | 1481934 | 3.0027·10⁻¹³ |
| 371 | 1 | 2.138373586302633452374 | 280177 | 1464173 | 3.6300·10⁻¹³ |
| 372 | 1 | 2.139118583497056040789 | 284072 | 1446358 | 2.0094·10⁻¹³ |
| 373 | 1 | 2.139865580682855830041 | 287980 | 1428485 | 3.6053·10⁻¹³ |
| 374 | 1 | 2.140614577860023669029 | 291900 | 1410558 | 2.7705·10⁻¹³ |
| 375 | 1 | 2.141365575028550385142 | 295833 | 1392573 | 4.9689·10⁻¹³ |
| 376 | 1 | 2.142118572188426784214 | 299778 | 1374534 | 4.5529·10⁻¹³ |
| 377 | 1 | 2.142873569339643650487 | 303735 | 1356441 | 1.4305·10⁻¹³ |
| 378 | 1 | 2.143630566482191746573 | 307705 | 1338290 | 1.0647·10⁻¹³ |
| 379 | 1 | 2.144389563616061813415 | 311688 | 1320081 | 3.3631·10⁻¹³ |
| 380 | 1 | 2.145150560741244570254 | 315683 | 1301818 | 2.6773·10⁻¹³ |
| 381 | 1 | 2.145913557857730714590 | 319691 | 1283497 | 4.4697·10⁻¹³ |
| 382 | 1 | 2.146678554965510922147 | 323711 | 1265122 | 3.0916·10⁻¹³ |
| 383 | 1 | 2.147445552064575846839 | 327744 | 1246689 | 4.0050·10⁻¹³ |
| 384 | 1 | 2.148214549154916120736 | 331789 | 1228202 | 1.5609·10⁻¹³ |
| 385 | 1 | 2.148985546236522354029 | 335847 | 1209657 | 1.2207·10⁻¹³ |
| 386 | 1 | 2.149758543309385134999 | 339918 | 1191054 | 2.8904·10⁻¹³ |
| 387 | 1 | 2.150533540373495029986 | 344001 | 1172397 | 9.2008·10⁻¹⁴ |
| 388 | 1 | 2.151310537428842583351 | 348097 | 1153682 | 7.7075·10⁻¹⁴ |
| 389 | 1 | 2.152089534475418317454 | 352206 | 1134909 | 2.3476·10⁻¹³ |
| 390 | 1 | 2.152870531513212732616 | 356327 | 1116082 | 1.6747·10⁻¹⁷ |
| 391 | 1 | 2.153653528542216307092 | 360462 | 1097193 | 4.7442·10⁻¹³ |
| 392 | 1 | 2.154438525562419497042 | 364609 | 1078250 | 5.3733·10⁻¹³ |
| 393 | 1 | 2.155225522573812736501 | 368768 | 1059253 | 1.7917·10⁻¹³ |
| 394 | 1 | 2.156014519576386437351 | 372941 | 1040194 | 5.0147·10⁻¹³ |
| 395 | 1 | 2.156805516570130989292 | 377126 | 1021081 | 3.8351·10⁻¹³ |
| 396 | 1 | 2.157598513555036759817 | 381324 | 1001910 | 3.7121·10⁻¹³ |
| 397 | 1 | 2.158393510531094094182 | 385535 | 982681 | 4.5491·10⁻¹³ |
| 398 | 1 | 2.159190507498293315382 | 389758 | 963398 | 6.9384·10⁻¹⁴ |
| 399 | 1 | 2.159989504456624724124 | 393995 | 944053 | 3.1603·10⁻¹³ |
| 400 | 1 | 2.160790501406078598801 | 398244 | 924654 | 7.4045·10⁻¹⁴ |
| 401 | 1 | 2.161593498346645195467 | 402507 | 905193 | 4.4476·10⁻¹³ |
| 402 | 1 | 2.162398495278314747814 | 406782 | 885678 | 3.0733·10⁻¹³ |
| 403 | 1 | 2.163205492201077467143 | 411070 | 866105 | 2.0750·10⁻¹³ |
| 404 | 1 | 2.164014489114923542348 | 415371 | 846474 | 1.3547·10⁻¹³ |
| 405 | 1 | 2.164825486019843139885 | 419685 | 826785 | 8.1404·10⁻¹⁴ |
| 406 | 1 | 2.165638482915826403753 | 424012 | 807038 | 3.5442·10⁻¹⁴ |
| 407 | 1 | 2.166453479802863455470 | 428353 | 787229 | 5.4326·10⁻¹³ |
| 408 | 1 | 2.167270476680944394050 | 432706 | 767366 | 4.8385·10⁻¹³ |
| 409 | 1 | 2.168089473550059295986 | 437072 | 747445 | 4.0285·10⁻¹³ |
| 410 | 1 | 2.168910470410198215220 | 441451 | 727466 | 2.9030·10⁻¹³ |
| 411 | 1 | 2.169733467261351183129 | 445843 | 707429 | 1.3624·10⁻¹³ |
| 412 | 1 | 2.170558464103508208502 | 450249 | 687330 | 4.8624·10⁻¹³ |
| 413 | 1 | 2.171385460936659277520 | 454667 | 667177 | 2.1917·10⁻¹³ |
| 414 | 1 | 2.172214457760794353732 | 459099 | 646962 | 4.3609·10⁻¹³ |
| 415 | 1 | 2.173045454575903378042 | 463543 | 626693 | 1.5859·10⁻¹⁴ |
| 416 | 1 | 2.173878451381976268685 | 468001 | 606362 | 5.9482·10⁻¹⁴ |
| 417 | 1 | 2.174713448179002921209 | 472472 | 585973 | 1.3074·10⁻¹⁵ |
| 418 | 1 | 2.175550444966973208456 | 476957 | 565522 | 3.8676·10⁻¹³ |
| 419 | 1 | 2.176389441745876980543 | 481454 | 545017 | 9.4588·10⁻¹⁴ |
| 420 | 1 | 2.177230438515704064847 | 485965 | 524450 | 2.2572·10⁻¹³ |
| 421 | 1 | 2.178073435276444265983 | 490489 | 503825 | 2.1441·10⁻¹³ |
| 422 | 1 | 2.178918432028087365788 | 495026 | 483142 | 5.0441·10⁻¹⁴ |
| 423 | 1 | 2.179765428770623123306 | 499577 | 462397 | 2.7912·10⁻¹³ |
| 424 | 1 | 2.180614425504041274766 | 504141 | 441594 | 3.3464·10⁻¹³ |
| 425 | 1 | 2.181465422228331533572 | 508718 | 420733 | 2.0670·10⁻¹³ |
| 426 | 1 | 2.182318418943483590279 | 513309 | 399810 | 4.4056·10⁻¹³ |
| 427 | 1 | 2.183173415649487112582 | 517913 | 378829 | 4.7032·10⁻¹³ |
| 428 | 1 | 2.184030412346331745301 | 522530 | 357790 | 2.8564·10⁻¹³ |
| 429 | 1 | 2.184889409034007110361 | 527161 | 336689 | 4.3168·10⁻¹³ |
| 430 | 1 | 2.185750405712502806778 | 531805 | 315530 | 3.4250·10⁻¹³ |
| 431 | 1 | 2.186613402381808410647 | 536462 | 294313 | 7.6644·10⁻¹⁵ |
| 432 | 1 | 2.187478399041913475122 | 541134 | 273030 | 5.2783·10⁻¹³ |
| 433 | 1 | 2.188345395692807530407 | 545818 | 251693 | 2.2588·10⁻¹³ |
| 434 | 1 | 2.189214392334480083737 | 550516 | 230294 | 2.0243·10⁻¹³ |
| 435 | 1 | 2.190085388966920619365 | 555228 | 208833 | 4.4695·10⁻¹³ |
| 436 | 1 | 2.190958385590118598549 | 559953 | 187314 | 3.9335·10⁻¹³ |
| 437 | 1 | 2.191833382204063459538 | 564691 | 165737 | 3.1087·10⁻¹⁴ |
| 438 | 1 | 2.192710378808744617559 | 569444 | 144094 | 4.6066·10⁻¹³ |
| 439 | 1 | 2.193589375404151464802 | 574209 | 122397 | 4.8130·10⁻¹⁵ |
| 440 | 1 | 2.194470371990273370407 | 578989 | 100634 | 3.1957·10⁻¹³ |
| 441 | 1 | 2.195353368567099680453 | 583782 | 78813 | 2.8317·10⁻¹³ |
| 442 | 1 | 2.196238365134619717945 | 588589 | 56930 | 4.4050·10⁻¹³ |
| 443 | 1 | 2.197125361692822782800 | 593409 | 34989 | 2.2529·10⁻¹³ |
| 444 | 1 | 2.198014358241698151834 | 598243 | 12986 | 1.8239·10⁻¹³ |
| 445 | 1 | 2.198905354781235078754 | 3091 | 2390922 | 1.5104·10⁻¹³ |
| 446 | 1 | 2.199798351311422794142 | 7953 | 2368795 | 4.2047·10⁻¹³ |
| 447 | 1 | 2.200693347832250505446 | 12828 | 2346610 | 2.7434·10⁻¹³ |
| 448 | 1 | 2.201590344343707396966 | 17717 | 2324363 | 2.5738·10⁻¹³ |
| 449 | 1 | 2.202489340845782629844 | 22620 | 2302054 | 3.5876·10⁻¹³ |
| 450 | 1 | 2.203390337338465342053 | 27536 | 2279687 | 1.2071·10⁻¹⁴ |
| 451 | 1 | 2.204293333821744648386 | 32467 | 2257254 | 3.1751·10⁻¹³ |
| 452 | 1 | 2.205198330295609640444 | 37411 | 2234763 | 1.5309·10⁻¹³ |
| 453 | 1 | 2.206105326760049386628 | 42369 | 2212210 | 6.3412·10⁻¹⁴ |
| 454 | 1 | 2.207014323215052932125 | 47341 | 2189595 | 3.7529·10⁻¹⁴ |
| 455 | 1 | 2.207925319660609298899 | 52327 | 2166918 | 6.4464·10⁻¹⁴ |
| 456 | 1 | 2.208838316096707485683 | 57327 | 2144179 | 1.3321·10⁻¹³ |
| 457 | 1 | 2.209753312523336467966 | 62341 | 2121378 | 2.3275·10⁻¹³ |
| 458 | 1 | 2.210670308940485197984 | 67369 | 2098515 | 3.5203·10⁻¹³ |
| 459 | 1 | 2.211589305348142604710 | 72411 | 2075590 | 4.7999·10⁻¹³ |
| 460 | 1 | 2.212510301746297593847 | 77466 | 2052607 | 4.9976·10⁻¹⁴ |
| 461 | 1 | 2.213433298134939047816 | 82536 | 2029558 | 1.6197·10⁻¹³ |
| 462 | 1 | 2.214358294514055825744 | 87620 | 2006447 | 2.4928·10⁻¹³ |
| 463 | 1 | 2.215285290883636763462 | 92718 | 1983274 | 3.0075·10⁻¹³ |
| 464 | 1 | 2.216214287243670673491 | 97830 | 1960039 | 3.0519·10⁻¹³ |
| 465 | 1 | 2.217145283594146345033 | 102956 | 1936742 | 2.5139·10⁻¹³ |
| 466 | 1 | 2.218078279935052543964 | 108096 | 1913383 | 1.2811·10⁻¹³ |
| 467 | 1 | 2.219013276266378012824 | 113251 | 1889958 | 4.7965·10⁻¹³ |
| 468 | 1 | 2.219950272588111470812 | 118419 | 1866475 | 1.8361·10⁻¹³ |
| 469 | 1 | 2.220889268900241613772 | 123602 | 1842926 | 3.3982·10⁻¹³ |
| 470 | 1 | 2.221830265202757114189 | 128799 | 1819315 | 3.8138·10⁻¹³ |
| 471 | 1 | 2.222773261495646621178 | 134010 | 1795642 | 2.9694·10⁻¹³ |
| 472 | 1 | 2.223718257778898760481 | 139235 | 1771907 | 7.5131·10⁻¹⁴ |
| 473 | 1 | 2.224665254052502134452 | 144475 | 1748106 | 2.6010·10⁻¹³ |
| 474 | 1 | 2.225614250316445322055 | 149729 | 1724243 | 2.8488·10⁻¹³ |
| 475 | 1 | 2.226565246570716878853 | 154997 | 1700318 | 1.3803·10⁻¹³ |
| 476 | 1 | 2.227518242815305337004 | 160280 | 1676327 | 3.6363·10⁻¹³ |
| 477 | 1 | 2.228473239050199205249 | 165577 | 1652274 | 3.9464·10⁻¹³ |
| 478 | 1 | 2.229430235275386968908 | 170888 | 1628159 | 2.1954·10⁻¹³ |
| 479 | 1 | 2.230389231490857089872 | 176214 | 1603978 | 3.8234·10⁻¹³ |
| 480 | 1 | 2.231350227696598006594 | 181554 | 1579735 | 3.1594·10⁻¹³ |
| 481 | 1 | 2.232313223892598134086 | 186908 | 1555430 | 8.7493·10⁻¹⁵ |
| 482 | 1 | 2.233278220078845863908 | 192277 | 1531059 | 4.7064·10⁻¹⁵ |
| 483 | 1 | 2.234245216255329564165 | 197661 | 1506622 | 2.9218·10⁻¹³ |
| 484 | 1 | 2.235214212422037579496 | 203059 | 1482123 | 3.0397·10⁻¹³ |
| 485 | 1 | 2.236185208578958231070 | 208471 | 1457562 | 2.8395·10⁻¹⁴ |
| 486 | 1 | 2.237158204726079816582 | 213898 | 1432935 | 9.3012·10⁻¹⁵ |
| 487 | 1 | 2.238133200863390610240 | 219340 | 1408242 | 2.3496·10⁻¹³ |
| 488 | 1 | 2.239110196990878862763 | 224796 | 1383487 | 1.3808·10⁻¹³ |
| 489 | 1 | 2.240089193108532801377 | 230267 | 1358666 | 2.6244·10⁻¹³ |
| 490 | 1 | 2.241070189216340629804 | 235752 | 1333783 | 4.0685·10⁻¹⁴ |
| 491 | 1 | 2.242053185314290528257 | 241252 | 1308834 | 1.6548·10⁻¹⁴ |
| 492 | 1 | 2.243038181402370653436 | 246767 | 1283819 | 1.7818·10⁻¹³ |
| 493 | 1 | 2.244025177480569138522 | 252297 | 1258738 | 5.1374·10⁻¹³ |
| 494 | 1 | 2.245014173548874093169 | 257841 | 1233595 | 4.5575·10⁻¹³ |
| 495 | 1 | 2.246005169607273603500 | 263400 | 1208386 | 5.4788·10⁻¹³ |
| 496 | 1 | 2.246998165655755732101 | 268973 | 1183115 | 2.2262·10⁻¹³ |
| 497 | 1 | 2.247993161694308518016 | 274561 | 1157778 | 2.3566·10⁻¹⁴ |
| 498 | 1 | 2.248990157722919976738 | 280165 | 1132371 | 4.9429·10⁻¹³ |
| 499 | 1 | 2.249989153741578100210 | 285783 | 1106902 | 5.1167·10⁻¹³ |
| 500 | 1 | 2.250990149750270856815 | 291415 | 1081371 | 6.3692·10⁻¹⁴ |
| 501 | 1 | 2.251993145748986191370 | 297063 | 1055770 | 2.4939·10⁻¹³ |
| 502 | 1 | 2.252998141737712025126 | 302726 | 1030103 | 5.0113·10⁻¹³ |
| 503 | 1 | 2.254005137716436255756 | 308403 | 1004374 | 2.5128·10⁻¹³ |
| 504 | 1 | 2.255014133685146757357 | 314095 | 978579 | 4.3244·10⁻¹⁴ |
| 505 | 1 | 2.256025129643831380438 | 319803 | 952714 | 4.2043·10⁻¹³ |
| 506 | 1 | 2.257038125592477951921 | 325525 | 926787 | 2.5957·10⁻¹³ |
| 507 | 1 | 2.258053121531074275133 | 331262 | 900794 | 1.0400·10⁻¹³ |
| 508 | 1 | 2.259070117459608129803 | 337015 | 874731 | 4.9708·10⁻¹³ |
| 509 | 1 | 2.260089113378067272055 | 342782 | 848606 | 3.1544·10⁻¹³ |
| 510 | 1 | 2.261110109286439434404 | 348564 | 822415 | 1.0237·10⁻¹³ |
| 511 | 1 | 2.262133105184712325755 | 354362 | 796154 | 4.0113·10⁻¹³ |
| 512 | 1 | 2.263158101072873631392 | 360174 | 769831 | 8.8315·10⁻¹⁴ |
| 513 | 1 | 2.264185096950911012980 | 366002 | 743438 | 2.6267·10⁻¹³ |
| 514 | 1 | 2.265214092818812108556 | 371845 | 716979 | 3.5629·10⁻¹³ |
| 515 | 1 | 2.266245088676564532528 | 377703 | 690454 | 3.5679·10⁻¹³ |
| 516 | 1 | 2.267278084524155875666 | 383576 | 663863 | 2.5177·10⁻¹³ |
| 517 | 1 | 2.268313080361573705105 | 389464 | 637206 | 2.8779·10⁻¹⁴ |
| 518 | 1 | 2.269350076188805564333 | 395368 | 610479 | 2.3092·10⁻¹³ |
| 519 | 1 | 2.270389072005838973193 | 401287 | 583686 | 2.9017·10⁻¹³ |
| 520 | 1 | 2.271430067812661427877 | 407221 | 556827 | 1.9401·10⁻¹³ |
| 521 | 1 | 2.272473063609260400918 | 413171 | 529898 | 4.8548·10⁻¹³ |
| 522 | 1 | 2.273518059395623341193 | 419135 | 502907 | 4.0913·10⁻¹⁴ |
| 523 | 1 | 2.274565055171737673915 | 425116 | 475842 | 5.1439·10⁻¹³ |
| 524 | 1 | 2.275614050937590800630 | 431111 | 448715 | 2.2667·10⁻¹³ |
| 525 | 1 | 2.276665046693170099211 | 437122 | 421518 | 2.7622·10⁻¹³ |
| 526 | 1 | 2.277718042438462923860 | 443148 | 394255 | 9.4855·10⁻¹⁴ |
| 527 | 1 | 2.278773038173456605098 | 449190 | 366922 | 2.2544·10⁻¹³ |
| 528 | 1 | 2.279830033898138449764 | 455247 | 339523 | 9.9754·10⁻¹⁴ |
| 529 | 1 | 2.280889029612495741014 | 461320 | 312054 | 2.6061·10⁻¹³ |
| 530 | 1 | 2.281950025316515738311 | 467408 | 284519 | 1.3973·10⁻¹³ |
| 531 | 1 | 2.283013021010185677429 | 473512 | 256914 | 2.7989·10⁻¹³ |
| 532 | 1 | 2.284078016693492770445 | 479631 | 229243 | 1.1276·10⁻¹³ |
| 533 | 1 | 2.285145012366424205734 | 485766 | 201502 | 1.8108·10⁻¹³ |
| 534 | 1 | 2.286214008028967147972 | 491917 | 173691 | 4.7201·10⁻¹³ |
| 535 | 1 | 2.287285003681108738127 | 498083 | 145814 | 4.1714·10⁻¹³ |
| 536 | 1 | 2.288357999322836093457 | 504264 | 117871 | 3.5957·10⁻¹⁵ |
| 537 | 1 | 2.289432994954136307508 | 510462 | 89854 | 3.2956·10⁻¹³ |
| 538 | 1 | 2.290509990574996450111 | 516675 | 61771 | 2.7101·10⁻¹³ |
| 539 | 1 | 2.291588986185403567376 | 522904 | 33618 | 3.7053·10⁻¹³ |
| 540 | 1 | 2.292669981785344681694 | 529148 | 5399 | 5.9613·10⁻¹⁴ |
| 541 | 1 | 2.293752977374806791727 | 0 | 2118743 | 3.5884·10⁻⁸ |
| 542 | 1 | 2.294837972953776872412 | 0 | 2115488 | 3.2397·10⁻⁸ |
| 543 | 1 | 2.295924968522241874954 | 0 | 2112227 | 2.8901·10⁻⁸ |
| 544 | 1 | 2.297013964080188726823 | 0 | 2108960 | 2.5397·10⁻⁸ |
| 545 | 1 | 2.298104959627604331753 | 0 | 2105687 | 2.1884·10⁻⁸ |
| 546 | 1 | 2.299197955164475569736 | 0 | 2102408 | 1.8362·10⁻⁸ |
| 547 | 1 | 2.300292950690789297025 | 0 | 2099123 | 1.4831·10⁻⁸ |
| 548 | 1 | 2.301389946206532346124 | 0 | 2095832 | 1.1292·10⁻⁸ |
| 549 | 1 | 2.302488941711691525790 | 0 | 2092535 | 7.7437·10⁻⁹ |
| 550 | 1 | 2.303589937206253621030 | 0 | 2089232 | 4.1863·10⁻⁹ |
| 551 | 1 | 2.304692932690205393095 | 0 | 2085923 | 6.2010·10⁻¹⁰ |
| 552 | 1 | 2.305797928163533579481 | 5320 | 2061328 | 5.1812·10⁻¹³ |
| 553 | 1 | 2.306904923626224893926 | 11771 | 2032203 | 3.4622·10⁻¹³ |
| 554 | 1 | 2.308013919078266026403 | 18238 | 2003008 | 1.3525·10⁻¹³ |
| 555 | 1 | 2.309124914519643643124 | 24722 | 1973739 | 4.2742·10⁻¹³ |
| 556 | 1 | 2.310237909950344386533 | 31221 | 1944404 | 9.8278·10⁻¹⁴ |
| 557 | 1 | 2.311352905370354875305 | 37737 | 1914995 | 2.4553·10⁻¹³ |
| 558 | 1 | 2.312469900779661704343 | 44269 | 1885516 | 3.0024·10⁻¹³ |
| 559 | 1 | 2.313588896178251444776 | 50817 | 1855967 | 2.4896·10⁻¹³ |
| 560 | 1 | 2.314709891566110643958 | 57381 | 1826348 | 7.8250·10⁻¹⁴ |
| 561 | 1 | 2.315832886943225825460 | 63962 | 1796655 | 3.3018·10⁻¹³ |
| 562 | 1 | 2.316957882309583489076 | 70559 | 1766892 | 4.3570·10⁻¹³ |
| 563 | 1 | 2.318084877665170110814 | 77172 | 1737059 | 3.8128·10⁻¹³ |
| 564 | 1 | 2.319213873009972142897 | 83801 | 1707156 | 1.5338·10⁻¹³ |
| 565 | 1 | 2.320344868343976013760 | 90447 | 1677179 | 2.9398·10⁻¹³ |
| 566 | 1 | 2.321477863667168128047 | 97109 | 1647132 | 2.3393·10⁻¹³ |
| 567 | 1 | 2.322612858979534866610 | 103788 | 1617011 | 5.1517·10⁻¹³ |
| 568 | 1 | 2.323749854281062586505 | 110482 | 1586824 | 1.2945·10⁻¹⁴ |
| 569 | 1 | 2.324888849571737620993 | 117194 | 1556559 | 3.8024·10⁻¹³ |
| 570 | 1 | 2.326029844851546279535 | 123922 | 1526224 | 4.9227·10⁻¹³ |
| 571 | 1 | 2.327172840120474847790 | 130666 | 1495819 | 3.3532·10⁻¹³ |
| 572 | 1 | 2.328317835378509587615 | 137427 | 1465340 | 4.5120·10⁻¹³ |
| 573 | 1 | 2.329464830625636737062 | 144204 | 1434791 | 2.7060·10⁻¹³ |
| 574 | 1 | 2.330613825861842510374 | 150998 | 1404168 | 3.3528·10⁻¹³ |
| 575 | 1 | 2.331764821087113097986 | 157808 | 1373475 | 7.5886·10⁻¹⁴ |
| 576 | 1 | 2.332917816301434666522 | 164635 | 1342708 | 3.4131·10⁻¹⁴ |
| 577 | 1 | 2.334072811504793358791 | 171479 | 1311867 | 1.9616·10⁻¹³ |
| 578 | 1 | 2.335229806697175293789 | 178340 | 1280952 | 5.4809·10⁻¹³ |
| 579 | 1 | 2.336388801878566566695 | 185217 | 1249967 | 5.2047·10⁻¹³ |
| 580 | 1 | 2.337549797048953248866 | 192110 | 1218912 | 9.9370·10⁻¹⁴ |
| 581 | 1 | 2.338712792208321387842 | 199021 | 1187779 | 3.8193·10⁻¹³ |
| 582 | 1 | 2.339877787356657007337 | 205948 | 1156576 | 2.4309·10⁻¹³ |
| 583 | 1 | 2.341044782493946107244 | 212892 | 1125299 | 2.2439·10⁻¹³ |
| 584 | 1 | 2.342213777620174663627 | 219853 | 1093948 | 3.1180·10⁻¹³ |
| 585 | 1 | 2.343384772735328628723 | 226831 | 1062523 | 4.9129·10⁻¹³ |
| 586 | 1 | 2.344557767839393930939 | 233825 | 1031028 | 1.9322·10⁻¹³ |
| 587 | 1 | 2.345732762932356474852 | 240837 | 999455 | 5.1461·10⁻¹³ |
| 588 | 1 | 2.346909758014202141203 | 247865 | 967812 | 3.3022·10⁻¹³ |
| 589 | 1 | 2.348088753084916786900 | 254910 | 936095 | 1.8148·10⁻¹³ |
| 590 | 1 | 2.349269748144486245014 | 261972 | 904304 | 5.4217·10⁻¹⁴ |
| 591 | 1 | 2.350452743192896324779 | 269052 | 872435 | 4.8978·10⁻¹³ |
| 592 | 1 | 2.351637738230132811586 | 276148 | 840496 | 3.6287·10⁻¹³ |
| 593 | 1 | 2.352824733256181466988 | 283261 | 808483 | 2.1478·10⁻¹³ |
| 594 | 1 | 2.354013728271028028693 | 290391 | 776396 | 3.1268·10⁻¹⁴ |
| 595 | 1 | 2.355204723274658210565 | 297539 | 744231 | 3.5358·10⁻¹³ |
| 596 | 1 | 2.356397718267057702621 | 304703 | 711996 | 5.6322·10⁻¹⁴ |
| 597 | 1 | 2.357592713248212171033 | 311885 | 679683 | 2.3625·10⁻¹³ |
| 598 | 1 | 2.358789708218107258120 | 319084 | 647296 | 3.2346·10⁻¹³ |
| 599 | 1 | 2.359988703176728582352 | 326300 | 614835 | 3.0356·10⁻¹³ |
| 600 | 1 | 2.361189698124061738348 | 333533 | 582300 | 1.6217·10⁻¹³ |
| 601 | 1 | 2.362392693060092296871 | 340784 | 549687 | 4.4039·10⁻¹³ |
| 602 | 1 | 2.363597687984805804831 | 348051 | 517004 | 1.2669·10⁻¹⁴ |
| 603 | 1 | 2.364804682898187785280 | 355337 | 484239 | 5.3119·10⁻¹³ |
| 604 | 1 | 2.366013677800223737412 | 362639 | 451404 | 3.1479·10⁻¹³ |
| 605 | 1 | 2.367224672690899136564 | 369959 | 418491 | 4.6005·10⁻¹³ |
| 606 | 1 | 2.368437667570199434209 | 377296 | 385504 | 3.9687·10⁻¹³ |
| 607 | 1 | 2.369652662438110057959 | 384650 | 352443 | 1.1068·10⁻¹³ |
| 608 | 1 | 2.370869657294616411563 | 392022 | 319304 | 1.4244·10⁻¹³ |
| 609 | 1 | 2.372088652139703874906 | 399412 | 286087 | 4.7753·10⁻¹³ |
| 610 | 1 | 2.373309646973357804005 | 406819 | 252796 | 5.4574·10⁻¹³ |
| 611 | 1 | 2.374532641795563531011 | 414243 | 219431 | 3.3241·10⁻¹³ |
| 612 | 1 | 2.375757636606306364205 | 421685 | 185988 | 3.7841·10⁻¹³ |
| 613 | 1 | 2.376984631405571587999 | 429144 | 152471 | 1.1346·10⁻¹³ |
| 614 | 1 | 2.378213626193344462933 | 436621 | 118876 | 7.8375·10⁻¹⁴ |
| 615 | 1 | 2.379444620969610225677 | 444116 | 85203 | 2.5839·10⁻¹³ |
| 616 | 1 | 2.380677615734354089022 | 451628 | 51456 | 8.3178·10⁻¹⁴ |
| 617 | 1 | 2.381912610487561241890 | 459158 | 17631 | 9.3468·10⁻¹⁴ |
| 618 | 1 | 2.383149605229216849322 | 0 | 1850553 | 7.4052·10⁻⁸ |
| 619 | 1 | 2.384388599959306052486 | 0 | 1846836 | 6.9849·10⁻⁸ |
| 620 | 1 | 2.385629594677813968667 | 0 | 1843113 | 6.5636·10⁻⁸ |
| 621 | 1 | 2.386872589384725691273 | 0 | 1839384 | 6.1413·10⁻⁸ |
| 622 | 1 | 2.388117584080026289832 | 0 | 1835649 | 5.7181·10⁻⁸ |
| 623 | 1 | 2.389364578763700809987 | 0 | 1831908 | 5.2938·10⁻⁸ |
| 624 | 1 | 2.390613573435734273500 | 0 | 1828161 | 4.8686·10⁻⁸ |
| 625 | 1 | 2.391864568096111678248 | 0 | 1824408 | 4.4423·10⁻⁸ |
| 626 | 1 | 2.393117562744817998224 | 0 | 1820649 | 4.0151·10⁻⁸ |
| 627 | 1 | 2.394372557381838183533 | 0 | 1816884 | 3.5869·10⁻⁸ |
| 628 | 1 | 2.395629552007157160392 | 0 | 1813113 | 3.1576·10⁻⁸ |
| 629 | 1 | 2.396888546620759831132 | 0 | 1809336 | 2.7274·10⁻⁸ |
| 630 | 1 | 2.398149541222631074192 | 0 | 1805553 | 2.2962·10⁻⁸ |
| 631 | 1 | 2.399412535812755744122 | 0 | 1801764 | 1.8640·10⁻⁸ |
| 632 | 1 | 2.400677530391118671578 | 0 | 1797969 | 1.4307·10⁻⁸ |
| 633 | 1 | 2.401944524957704663326 | 0 | 1794168 | 9.9653·10⁻⁹ |
| 634 | 1 | 2.403213519512498502237 | 0 | 1790361 | 5.6129·10⁻⁹ |
| 635 | 1 | 2.404484514055484947287 | 0 | 1786548 | 1.2503·10⁻⁹ |
| 636 | 1 | 2.405757508586648733557 | 5621 | 1760245 | 5.1178·10⁻¹³ |
| 637 | 1 | 2.407032503105974572231 | 13510 | 1724864 | 5.2954·10⁻¹³ |
| 638 | 1 | 2.408309497613447150595 | 21417 | 1689405 | 4.1625·10⁻¹³ |
| 639 | 1 | 2.409588492109051132038 | 29342 | 1653868 | 1.5659·10⁻¹³ |
| 640 | 1 | 2.410869486592771156046 | 37286 | 1618249 | 2.9074·10⁻¹³ |
| 641 | 1 | 2.412152481064591838209 | 45248 | 1582552 | 2.4776·10⁻¹³ |
| 642 | 1 | 2.413437475524497770212 | 53228 | 1546777 | 1.2262·10⁻¹⁴ |
| 643 | 1 | 2.414724469972473519840 | 61227 | 1510920 | 1.2434·10⁻¹³ |
| 644 | 1 | 2.416013464408503630974 | 69244 | 1474985 | 1.3005·10⁻¹⁴ |
| 645 | 1 | 2.417304458832572623590 | 77280 | 1438968 | 2.1832·10⁻¹³ |
| 646 | 1 | 2.418597453244664993761 | 85334 | 1402873 | 1.6923·10⁻¹³ |
| 647 | 1 | 2.419892447644765213652 | 93407 | 1366696 | 4.0576·10⁻¹³ |
| 648 | 1 | 2.421189442032857731522 | 101498 | 1330441 | 3.5680·10⁻¹³ |
| 649 | 1 | 2.422488436408926971725 | 109607 | 1294108 | 6.7941·10⁻¹⁵ |
| 650 | 1 | 2.423789430772957334702 | 117736 | 1257689 | 4.5123·10⁻¹³ |
| 651 | 1 | 2.425092425124933196988 | 125882 | 1221196 | 7.8275·10⁻¹⁵ |
| 652 | 1 | 2.426397419464838911208 | 134048 | 1184617 | 3.2760·10⁻¹³ |
| 653 | 1 | 2.427704413792658806073 | 142232 | 1147960 | 2.8377·10⁻¹³ |
| 654 | 1 | 2.429013408108377186386 | 150435 | 1111221 | 4.1621·10⁻¹³ |
| 655 | 1 | 2.430324402411978333036 | 158656 | 1074404 | 1.5362·10⁻¹³ |
| 656 | 1 | 2.431637396703446502998 | 166896 | 1037505 | 3.5837·10⁻¹⁴ |
| 657 | 1 | 2.432952390982765929334 | 175155 | 1000524 | 4.7076·10⁻¹⁴ |
| 658 | 1 | 2.434269385249920821190 | 183433 | 963461 | 1.7155·10⁻¹³ |
| 659 | 1 | 2.435588379504895363798 | 191730 | 926316 | 3.9345·10⁻¹³ |
| 660 | 1 | 2.436909373747673718472 | 200045 | 889093 | 1.4138·10⁻¹³ |
| 661 | 1 | 2.438232367978240022610 | 208380 | 851784 | 5.1059·10⁻¹³ |
| 662 | 1 | 2.439557362196578389692 | 216733 | 814397 | 3.7407·10⁻¹³ |
| 663 | 1 | 2.440884356402672909278 | 225105 | 776928 | 2.7148·10⁻¹³ |
| 664 | 1 | 2.442213350596507647011 | 233496 | 739377 | 1.8689·10⁻¹³ |
| 665 | 1 | 2.443544344778066644611 | 241906 | 701744 | 1.0432·10⁻¹³ |
| 666 | 1 | 2.444877338947333919881 | 250335 | 664029 | 7.8094·10⁻¹⁵ |
| 667 | 1 | 2.446212333104293466700 | 258784 | 626228 | 4.3689·10⁻¹³ |
| 668 | 1 | 2.447549327248929255024 | 267251 | 588349 | 2.6443·10⁻¹³ |
| 669 | 1 | 2.448888321381225230888 | 275737 | 550388 | 2.9935·10⁻¹⁴ |
| 670 | 1 | 2.450229315501165316403 | 284243 | 512341 | 2.7287·10⁻¹³ |
| 671 | 1 | 2.451572309608733409756 | 292768 | 474212 | 4.2159·10⁻¹³ |
| 672 | 1 | 2.452917303703913385208 | 301312 | 436001 | 4.5996·10⁻¹³ |
| 673 | 1 | 2.454264297786689093096 | 309875 | 397708 | 3.7184·10⁻¹³ |
| 674 | 1 | 2.455613291857044359829 | 318457 | 359333 | 1.4105·10⁻¹³ |
| 675 | 1 | 2.456964285914962987891 | 327059 | 320872 | 3.0695·10⁻¹³ |
| 676 | 1 | 2.458317279960428755837 | 335680 | 282329 | 2.9776·10⁻¹³ |
| 677 | 1 | 2.459672273993425418294 | 344320 | 243704 | 9.7240·10⁻¹⁴ |
| 678 | 1 | 2.461029268013936705962 | 352980 | 204993 | 2.4467·10⁻¹³ |
| 679 | 1 | 2.462388262021946325610 | 361659 | 166200 | 1.6820·10⁻¹³ |
| 680 | 1 | 2.463749256017437960076 | 370358 | 127321 | 4.0708·10⁻¹³ |
| 681 | 1 | 2.465112250000395268270 | 379076 | 88360 | 3.8940·10⁻¹³ |
| 682 | 1 | 2.466477243970801885170 | 387813 | 49317 | 9.8808·10⁻¹⁴ |
| 683 | 1 | 2.467844237928641421820 | 396570 | 10188 | 7.4460·10⁻¹⁴ |
| 684 | 1 | 2.469213231873897465334 | 0 | 1592362 | 1.0814·10⁻⁷ |
| 685 | 1 | 2.470584225806553578892 | 0 | 1588249 | 1.0325·10⁻⁷ |
| 686 | 1 | 2.471957219726593301741 | 0 | 1584130 | 9.8356·10⁻⁸ |
| 687 | 1 | 2.473332213634000149194 | 0 | 1580005 | 9.3447·10⁻⁸ |
| 688 | 1 | 2.474709207528757612628 | 0 | 1575874 | 8.8528·10⁻⁸ |
| 689 | 1 | 2.476088201410849159486 | 0 | 1571737 | 8.3597·10⁻⁸ |
| 690 | 1 | 2.477469195280258233275 | 0 | 1567594 | 7.8656·10⁻⁸ |
| 691 | 1 | 2.478852189136968253565 | 0 | 1563445 | 7.3703·10⁻⁸ |
| 692 | 1 | 2.480237182980962615990 | 0 | 1559290 | 6.8740·10⁻⁸ |
| 693 | 1 | 2.481624176812224692245 | 0 | 1555129 | 6.3766·10⁻⁸ |
| 694 | 1 | 2.483013170630737830089 | 0 | 1550962 | 5.8780·10⁻⁸ |
| 695 | 1 | 2.484404164436485353340 | 0 | 1546789 | 5.3784·10⁻⁸ |
| 696 | 1 | 2.485797158229450561881 | 0 | 1542610 | 4.8776·10⁻⁸ |
| 697 | 1 | 2.487192152009616731650 | 0 | 1538425 | 4.3758·10⁻⁸ |
| 698 | 1 | 2.488589145776967114650 | 0 | 1534234 | 3.8728·10⁻⁸ |
| 699 | 1 | 2.489988139531484938941 | 0 | 1530037 | 3.3687·10⁻⁸ |
| 700 | 1 | 2.491389133273153408641 | 0 | 1525834 | 2.8635·10⁻⁸ |
| 701 | 1 | 2.492792127001955703928 | 0 | 1521625 | 2.3572·10⁻⁸ |
| 702 | 1 | 2.494197120717874981038 | 0 | 1517410 | 1.8498·10⁻⁸ |
| 703 | 1 | 2.495604114420894372263 | 0 | 1513189 | 1.3413·10⁻⁸ |
| 704 | 1 | 2.497013108110996985955 | 0 | 1508962 | 8.3166·10⁻⁹ |
| 705 | 1 | 2.498424101788165906518 | 0 | 1504729 | 3.2088·10⁻⁹ |
| 706 | 1 | 2.499837095452384194415 | 3439 | 1486734 | 3.5186·10⁻¹³ |
| 707 | 1 | 2.501252089103634886164 | 12673 | 1445553 | 7.1869·10⁻¹⁴ |
| 708 | 1 | 2.502669082741900994339 | 21928 | 1404282 | 1.9617·10⁻¹³ |
| 709 | 1 | 2.504088076367165507567 | 31203 | 1362925 | 1.5220·10⁻¹³ |
| 710 | 1 | 2.505509069979411390529 | 40499 | 1321478 | 4.7849·10⁻¹³ |
| 711 | 1 | 2.506932063578621583961 | 49814 | 1279949 | 4.6867·10⁻¹⁴ |
| 712 | 1 | 2.508357057164779004652 | 59151 | 1238326 | 5.0690·10⁻¹³ |
| 713 | 1 | 2.509784050737866545444 | 68507 | 1196621 | 1.7483·10⁻¹³ |
| 714 | 1 | 2.511213044297867075230 | 77884 | 1154826 | 1.4463·10⁻¹³ |
| 715 | 1 | 2.512644037844763438957 | 87282 | 1112941 | 3.9915·10⁻¹³ |
| 716 | 1 | 2.514077031378538457621 | 96700 | 1070970 | 3.6565·10⁻¹³ |
| 717 | 1 | 2.515512024899174928272 | 106138 | 1028913 | 2.6932·10⁻¹⁴ |
| 718 | 1 | 2.516949018406655624008 | 115598 | 986762 | 4.7687·10⁻¹³ |
| 719 | 1 | 2.518388011900963293979 | 125077 | 944529 | 3.1565·10⁻¹⁴ |
| 720 | 1 | 2.519829005382080663385 | 134578 | 902202 | 3.4039·10⁻¹³ |
| 721 | 1 | 2.521271998849990433475 | 144099 | 859789 | 2.7494·10⁻¹³ |
| 722 | 1 | 2.522716992304675281545 | 153641 | 817286 | 3.7346·10⁻¹³ |
| 723 | 1 | 2.524163985746117860943 | 163203 | 774697 | 6.3042·10⁻¹⁴ |
| 724 | 1 | 2.525612979174300801064 | 172787 | 732014 | 4.3741·10⁻¹³ |
| 725 | 1 | 2.527063972589206707349 | 182391 | 689245 | 3.6808·10⁻¹³ |
| 726 | 1 | 2.528516965990818161290 | 192016 | 646386 | 3.9318·10⁻¹³ |
| 727 | 1 | 2.529971959379117720422 | 201662 | 603437 | 4.9527·10⁻¹³ |
| 728 | 1 | 2.531428952754087918331 | 211328 | 560402 | 1.0132·10⁻¹³ |
| 729 | 1 | 2.532887946115711264646 | 221016 | 517273 | 3.0496·10⁻¹³ |
| 730 | 1 | 2.534348939463970245044 | 230725 | 474054 | 5.3312·10⁻¹³ |
| 731 | 1 | 2.535811932798847321245 | 240454 | 430749 | 2.1270·10⁻¹³ |
| 732 | 1 | 2.537276926120324931018 | 250205 | 387350 | 4.3725·10⁻¹³ |
| 733 | 1 | 2.538743919428385488173 | 259976 | 343865 | 7.8087·10⁻¹⁴ |
| 734 | 1 | 2.540212912723011382567 | 269769 | 300286 | 2.2869·10⁻¹³ |
| 735 | 1 | 2.541683906004184980100 | 279583 | 256617 | 3.1588·10⁻¹³ |
| 736 | 1 | 2.543156899271888622717 | 289418 | 212858 | 3.2199·10⁻¹³ |
| 737 | 1 | 2.544631892526104628404 | 299274 | 169009 | 2.2936·10⁻¹³ |
| 738 | 1 | 2.546108885766815291194 | 309151 | 125070 | 2.0265·10⁻¹⁴ |
| 739 | 1 | 2.547587878994002881159 | 319050 | 81037 | 2.3253·10⁻¹³ |
| 740 | 1 | 2.549068872207649644414 | 328970 | 36914 | 2.9286·10⁻¹³ |
| 741 | 1 | 2.550551865407737803118 | 0 | 1348346 | 1.4504·10⁻⁷ |
| 742 | 1 | 2.552036858594249555471 | 0 | 1343891 | 1.3951·10⁻⁷ |
| 743 | 1 | 2.553523851767167075713 | 0 | 1339430 | 1.3396·10⁻⁷ |
| 744 | 1 | 2.555012844926472514127 | 0 | 1334963 | 1.2840·10⁻⁷ |
| 745 | 1 | 2.556503838072147997035 | 0 | 1330490 | 1.2283·10⁻⁷ |
| 746 | 1 | 2.557996831204175626800 | 0 | 1326011 | 1.1725·10⁻⁷ |
| 747 | 1 | 2.559491824322537481827 | 0 | 1321526 | 1.1166·10⁻⁷ |
| 748 | 1 | 2.560988817427215616557 | 0 | 1317035 | 1.0605·10⁻⁷ |
| 749 | 1 | 2.562487810518192061474 | 0 | 1312538 | 1.0043·10⁻⁷ |
| 750 | 1 | 2.563988803595448823100 | 0 | 1308035 | 9.4807·10⁻⁸ |
| 751 | 1 | 2.565491796658967883995 | 0 | 1303526 | 8.9165·10⁻⁸ |
| 752 | 1 | 2.566996789708731202758 | 0 | 1299011 | 8.3511·10⁻⁸ |
| 753 | 1 | 2.568503782744720714028 | 0 | 1294490 | 7.7845·10⁻⁸ |
| 754 | 1 | 2.570012775766918328479 | 0 | 1289963 | 7.2166·10⁻⁸ |
| 755 | 1 | 2.571523768775305932825 | 0 | 1285430 | 6.6476·10⁻⁸ |
| 756 | 1 | 2.573036761769865389816 | 0 | 1280891 | 6.0773·10⁻⁸ |
| 757 | 1 | 2.574551754750578538239 | 0 | 1276346 | 5.5058·10⁻⁸ |
| 758 | 1 | 2.576068747717427192920 | 0 | 1271795 | 4.9332·10⁻⁸ |
| 759 | 1 | 2.577587740670393144720 | 0 | 1267238 | 4.3593·10⁻⁸ |
| 760 | 1 | 2.579108733609458160534 | 0 | 1262675 | 3.7841·10⁻⁸ |
| 761 | 1 | 2.580631726534603983297 | 0 | 1258106 | 3.2078·10⁻⁸ |
| 762 | 1 | 2.582156719445812331978 | 0 | 1253531 | 2.6302·10⁻⁸ |
| 763 | 1 | 2.583683712343064901580 | 0 | 1248950 | 2.0515·10⁻⁸ |
| 764 | 1 | 2.585212705226343363144 | 0 | 1244363 | 1.4714·10⁻⁸ |
| 765 | 1 | 2.586743698095629363742 | 0 | 1239770 | 8.9026·10⁻⁹ |
| 766 | 1 | 2.588276690950904526485 | 0 | 1235171 | 3.0779·10⁻⁹ |
| 767 | 1 | 2.589811683792150450515 | 4967 | 1210698 | 4.7422·10⁻¹³ |
| 768 | 1 | 2.591348676619348711009 | 15495 | 1163975 | 8.5874·10⁻¹⁴ |
| 769 | 1 | 2.592887669432480859179 | 26046 | 1117154 | 1.3140·10⁻¹³ |
| 770 | 1 | 2.594428662231528422270 | 36619 | 1070239 | 3.6794·10⁻¹⁴ |
| 771 | 1 | 2.595971655016472903558 | 47215 | 1023226 | 3.3909·10⁻¹³ |
| 772 | 1 | 2.597516647787295782356 | 57833 | 976119 | 4.6422·10⁻¹³ |
| 773 | 1 | 2.599063640543978514007 | 68473 | 928918 | 3.9365·10⁻¹³ |
| 774 | 1 | 2.600612633286502529888 | 79135 | 881623 | 1.0880·10⁻¹³ |
| 775 | 1 | 2.602163626014849237406 | 89820 | 834230 | 1.4663·10⁻¹³ |
| 776 | 1 | 2.603716618729000020003 | 100528 | 786739 | 4.8853·10⁻¹³ |
| 777 | 1 | 2.605271611428936237152 | 111257 | 739158 | 4.7545·10⁻¹⁵ |
| 778 | 1 | 2.606828604114639224356 | 122010 | 691475 | 3.4329·10⁻¹³ |
| 779 | 1 | 2.608387596786090293151 | 132785 | 643698 | 3.7435·10⁻¹³ |
| 780 | 1 | 2.609948589443270731104 | 143582 | 595827 | 7.9216·10⁻¹⁴ |
| 781 | 1 | 2.611511582086161801813 | 154403 | 547854 | 5.5026·10⁻¹³ |
| 782 | 1 | 2.613076574714744744904 | 165245 | 499791 | 1.0206·10⁻¹³ |
| 783 | 1 | 2.614643567329000776038 | 176111 | 451626 | 3.8250·10⁻¹³ |
| 784 | 1 | 2.616212559928911086902 | 186999 | 403367 | 2.6166·10⁻¹³ |
| 785 | 1 | 2.617783552514456845216 | 197910 | 355010 | 2.7626·10⁻¹³ |
| 786 | 1 | 2.619356545085619194728 | 208844 | 306555 | 4.0744·10⁻¹³ |
| 787 | 1 | 2.620931537642379255216 | 219800 | 258006 | 8.0779·10⁻¹⁴ |
| 788 | 1 | 2.622508530184718122488 | 230780 | 209355 | 3.8846·10⁻¹³ |
| 789 | 1 | 2.624087522712616868380 | 241782 | 160610 | 2.0047·10⁻¹³ |
| 790 | 1 | 2.625668515226056540757 | 252807 | 111767 | 5.3399·10⁻¹⁴ |
| 791 | 1 | 2.627251507725018163514 | 263856 | 62822 | 4.8382·10⁻¹³ |
| 792 | 1 | 2.628836500209482736572 | 274927 | 13783 | 3.6163·10⁻¹³ |
| 793 | 1 | 2.630423492679431235883 | 0 | 1108731 | 1.7443·10⁻⁷ |
| 794 | 1 | 2.632012485134844613426 | 0 | 1103964 | 1.6825·10⁻⁷ |
| 795 | 1 | 2.633603477575703797207 | 0 | 1099191 | 1.6206·10⁻⁷ |
| 796 | 1 | 2.635196470001989691260 | 0 | 1094412 | 1.5586·10⁻⁷ |
| 797 | 1 | 2.636791462413683175648 | 0 | 1089627 | 1.4965·10⁻⁷ |
| 798 | 1 | 2.638388454810765106458 | 0 | 1084836 | 1.4342·10⁻⁷ |
| 799 | 1 | 2.639987447193216315808 | 0 | 1080039 | 1.3718·10⁻⁷ |
| 800 | 1 | 2.641588439561017611840 | 0 | 1075236 | 1.3092·10⁻⁷ |
| 801 | 1 | 2.643191431914149778723 | 0 | 1070427 | 1.2466·10⁻⁷ |
| 802 | 1 | 2.644796424252593576653 | 0 | 1065612 | 1.1838·10⁻⁷ |
| 803 | 1 | 2.646403416576329741853 | 0 | 1060791 | 1.1209·10⁻⁷ |
| 804 | 1 | 2.648012408885338986572 | 0 | 1055964 | 1.0578·10⁻⁷ |
| 805 | 1 | 2.649623401179601999082 | 0 | 1051131 | 9.9466·10⁻⁸ |
| 806 | 1 | 2.651236393459099443684 | 0 | 1046292 | 9.3134·10⁻⁸ |
| 807 | 1 | 2.652851385723811960704 | 0 | 1041447 | 8.6790·10⁻⁸ |
| 808 | 1 | 2.654468377973720166492 | 0 | 1036596 | 8.0432·10⁻⁸ |
| 809 | 1 | 2.656087370208804653424 | 0 | 1031739 | 7.4061·10⁻⁸ |
| 810 | 1 | 2.657708362429045989901 | 0 | 1026876 | 6.7677·10⁻⁸ |
| 811 | 1 | 2.659331354634424720349 | 0 | 1022007 | 6.1280·10⁻⁸ |
| 812 | 1 | 2.660956346824921365217 | 0 | 1017132 | 5.4870·10⁻⁸ |
| 813 | 1 | 2.662583339000516420981 | 0 | 1012251 | 4.8447·10⁻⁸ |
| 814 | 1 | 2.664212331161190360140 | 0 | 1007364 | 4.2010·10⁻⁸ |
| 815 | 1 | 2.665843323306923631217 | 0 | 1002471 | 3.5560·10⁻⁸ |
| 816 | 1 | 2.667476315437696658759 | 0 | 997572 | 2.9097·10⁻⁸ |
| 817 | 1 | 2.669111307553489843336 | 0 | 992667 | 2.2621·10⁻⁸ |
| 818 | 1 | 2.670748299654283561544 | 0 | 987756 | 1.6131·10⁻⁸ |
| 819 | 1 | 2.672387291740058165999 | 0 | 982839 | 9.6290·10⁻⁹ |
| 820 | 1 | 2.674028283810793985343 | 0 | 977916 | 3.1128·10⁻⁹ |
| 821 | 1 | 2.675671275866471324241 | 6150 | 948387 | 1.4716·10⁻¹⁴ |
| 822 | 1 | 2.677316267907070463378 | 17928 | 896340 | 4.7134·10⁻¹³ |
| 823 | 1 | 2.678963259932571659466 | 29729 | 844195 | 3.3002·10⁻¹³ |
| 824 | 1 | 2.680612251942955145237 | 41554 | 791948 | 1.2654·10⁻¹³ |
| 825 | 1 | 2.682263243938201129445 | 53404 | 739595 | 3.9666·10⁻¹³ |
| 826 | 1 | 2.683916235918289796869 | 65277 | 687144 | 9.4600·10⁻¹⁵ |
| 827 | 1 | 2.685571227883201308306 | 77175 | 634587 | 5.6205·10⁻¹⁴ |
| 828 | 1 | 2.687228219832915800580 | 89098 | 581924 | 5.1703·10⁻¹³ |
| 829 | 1 | 2.688887211767413386533 | 101044 | 529163 | 2.6095·10⁻¹³ |
| 830 | 1 | 2.690548203686674155029 | 113015 | 476296 | 3.7915·10⁻¹³ |
| 831 | 1 | 2.692211195590678170957 | 125010 | 423327 | 2.9616·10⁻¹³ |
| 832 | 1 | 2.693876187479405475223 | 137030 | 370252 | 5.4755·10⁻¹³ |
| 833 | 1 | 2.695543179352836084756 | 149073 | 317079 | 2.2465·10⁻¹⁵ |
| 834 | 1 | 2.697212171210949992507 | 161142 | 263796 | 3.0689·10⁻¹³ |
| 835 | 1 | 2.698883163053727167448 | 173235 | 210411 | 3.3036·10⁻¹³ |
| 836 | 1 | 2.700556154881147554569 | 185352 | 156924 | 5.2591·10⁻¹⁴ |
| 837 | 1 | 2.702231146693191074884 | 197494 | 103331 | 9.0564·10⁻¹⁵ |
| 838 | 1 | 2.703908138489837625426 | 209661 | 49632 | 1.7965·10⁻¹³ |
| 839 | 1 | 2.705587130271067079248 | 0 | 883240 | 2.1008·10⁻⁷ |
| 840 | 1 | 2.707268122036859285425 | 0 | 878197 | 2.0329·10⁻⁷ |
| 841 | 1 | 2.708951113787194069050 | 0 | 873148 | 1.9649·10⁻⁷ |
| 842 | 1 | 2.710636105522051231237 | 0 | 868093 | 1.8968·10⁻⁷ |
| 843 | 1 | 2.712323097241410549120 | 0 | 863032 | 1.8285·10⁻⁷ |
| 844 | 1 | 2.714012088945251775853 | 0 | 857965 | 1.7601·10⁻⁷ |
| 845 | 1 | 2.715703080633554640608 | 0 | 852892 | 1.6915·10⁻⁷ |
| 846 | 1 | 2.717396072306298848578 | 0 | 847813 | 1.6228·10⁻⁷ |
| 847 | 1 | 2.719091063963464080974 | 0 | 842728 | 1.5540·10⁻⁷ |
| 848 | 1 | 2.720788055605029995028 | 0 | 837637 | 1.4850·10⁻⁷ |
| 849 | 1 | 2.722487047230976223990 | 0 | 832540 | 1.4159·10⁻⁷ |
| 850 | 1 | 2.724188038841282377128 | 0 | 827437 | 1.3466·10⁻⁷ |
| 851 | 1 | 2.725891030435928039730 | 0 | 822328 | 1.2773·10⁻⁷ |
| 852 | 1 | 2.727596022014892773103 | 0 | 817213 | 1.2077·10⁻⁷ |
| 853 | 1 | 2.729303013578156114572 | 0 | 812092 | 1.1381·10⁻⁷ |
| 854 | 1 | 2.731012005125697577479 | 0 | 806965 | 1.0683·10⁻⁷ |
| 855 | 1 | 2.732722996657496651187 | 0 | 801832 | 9.9835·10⁻⁸ |
| 856 | 1 | 2.734435988173532801076 | 0 | 796693 | 9.2826·10⁻⁸ |
| 857 | 1 | 2.736150979673785468543 | 0 | 791548 | 8.5803·10⁻⁸ |
| 858 | 1 | 2.737867971158234071003 | 0 | 786397 | 7.8766·10⁻⁸ |
| 859 | 1 | 2.739586962626858001892 | 0 | 781240 | 7.1715·10⁻⁸ |
| 860 | 1 | 2.741307954079636630660 | 0 | 776077 | 6.4650·10⁻⁸ |
| 861 | 1 | 2.743030945516549302775 | 0 | 770908 | 5.7570·10⁻⁸ |
| 862 | 1 | 2.744755936937575339725 | 0 | 765733 | 5.0477·10⁻⁸ |
| 863 | 1 | 2.746482928342694039013 | 0 | 760552 | 4.3369·10⁻⁸ |
| 864 | 1 | 2.748211919731884674160 | 0 | 755365 | 3.6247·10⁻⁸ |
| 865 | 1 | 2.749942911105126494705 | 0 | 750172 | 2.9111·10⁻⁸ |
| 866 | 1 | 2.751675902462398726202 | 0 | 744973 | 2.1961·10⁻⁸ |
| 867 | 1 | 2.753410893803680570223 | 0 | 739768 | 1.4796·10⁻⁸ |
| 868 | 1 | 2.755147885128951204357 | 0 | 734557 | 7.6173·10⁻⁹ |
| 869 | 1 | 2.756886876438189782211 | 0 | 729340 | 4.2406·10⁻¹⁰ |
| 870 | 1 | 2.758627867731375433405 | 12211 | 675273 | 3.3342·10⁻¹³ |
| 871 | 1 | 2.760370859008487263578 | 25210 | 618048 | 2.4629·10⁻¹⁴ |
| 872 | 1 | 2.762115850269504354386 | 38236 | 560709 | 3.4331·10⁻¹³ |
| 873 | 1 | 2.763862841514405763499 | 51287 | 503264 | 1.5741·10⁻¹³ |
| 874 | 1 | 2.765611832743170524605 | 64364 | 445709 | 1.5347·10⁻¹⁵ |
| 875 | 1 | 2.767362823955777647407 | 77468 | 388040 | 4.1022·10⁻¹³ |
| 876 | 1 | 2.769115815152206117625 | 90597 | 330265 | 2.5137·10⁻¹³ |
| 877 | 1 | 2.770870806332434896993 | 103752 | 272380 | 5.9488·10⁻¹⁴ |
| 878 | 1 | 2.772627797496442923264 | 116934 | 214381 | 3.6906·10⁻¹³ |
| 879 | 1 | 2.774386788644209110202 | 130141 | 156276 | 4.7905·10⁻¹⁴ |
| 880 | 1 | 2.776147779775712347590 | 143375 | 98057 | 1.8601·10⁻¹³ |
| 881 | 1 | 2.777910770890931501227 | 156635 | 39728 | 2.0669·10⁻¹³ |
| 882 | 1 | 2.779675761989845412924 | 0 | 660974 | 2.3893·10⁻⁷ |
| 883 | 1 | 2.781442753072432900510 | 0 | 655673 | 2.3153·10⁻⁷ |
| 884 | 1 | 2.783211744138672757828 | 0 | 650366 | 2.2412·10⁻⁷ |
| 885 | 1 | 2.784982735188543754736 | 0 | 645053 | 2.1670·10⁻⁷ |
| 886 | 1 | 2.786755726222024637109 | 0 | 639734 | 2.0926·10⁻⁷ |
| 887 | 1 | 2.788530717239094126833 | 0 | 634409 | 2.0180·10⁻⁷ |
| 888 | 1 | 2.790307708239730921812 | 0 | 629078 | 1.9433·10⁻⁷ |
| 889 | 1 | 2.792086699223913695963 | 0 | 623741 | 1.8685·10⁻⁷ |
| 890 | 1 | 2.793867690191621099219 | 0 | 618398 | 1.7935·10⁻⁷ |
| 891 | 1 | 2.795650681142831757526 | 0 | 613049 | 1.7184·10⁻⁷ |
| 892 | 1 | 2.797435672077524272846 | 0 | 607694 | 1.6431·10⁻⁷ |
| 893 | 1 | 2.799222662995677223153 | 0 | 602333 | 1.5677·10⁻⁷ |
| 894 | 1 | 2.801011653897269162438 | 0 | 596966 | 1.4921·10⁻⁷ |
| 895 | 1 | 2.802802644782278620704 | 0 | 591593 | 1.4163·10⁻⁷ |
| 896 | 1 | 2.804595635650684103970 | 0 | 586214 | 1.3405·10⁻⁷ |
| 897 | 1 | 2.806390626502464094265 | 0 | 580829 | 1.2644·10⁻⁷ |
| 898 | 1 | 2.808187617337597049638 | 0 | 575438 | 1.1883·10⁻⁷ |
| 899 | 1 | 2.809986608156061404146 | 0 | 570041 | 1.1119·10⁻⁷ |
| 900 | 1 | 2.811787598957835567863 | 0 | 564638 | 1.0355·10⁻⁷ |
| 901 | 1 | 2.813590589742897926876 | 0 | 559229 | 9.5890·10⁻⁸ |
| 902 | 1 | 2.815395580511226843285 | 0 | 553814 | 8.8212·10⁻⁸ |
| 903 | 1 | 2.817202571262800655204 | 0 | 548393 | 8.0520·10⁻⁸ |
| 904 | 1 | 2.819011561997597676760 | 0 | 542966 | 7.2813·10⁻⁸ |
| 905 | 1 | 2.820822552715596198094 | 0 | 537533 | 6.5090·10⁻⁸ |
| 906 | 1 | 2.822635543416774485358 | 0 | 532094 | 5.7352·10⁻⁸ |
| 907 | 1 | 2.824450534101110780720 | 0 | 526649 | 4.9600·10⁻⁸ |
| 908 | 1 | 2.826267524768583302360 | 0 | 521198 | 4.1832·10⁻⁸ |
| 909 | 1 | 2.828086515419170244470 | 0 | 515741 | 3.4049·10⁻⁸ |
| 910 | 1 | 2.829907506052849777255 | 0 | 510278 | 2.6250·10⁻⁸ |
| 911 | 1 | 2.831730496669600046936 | 0 | 504809 | 1.8437·10⁻⁸ |
| 912 | 1 | 2.833555487269399175742 | 0 | 499334 | 1.0608·10⁻⁸ |
| 913 | 1 | 2.835382477852225261917 | 0 | 493853 | 2.7648·10⁻⁹ |
| 914 | 1 | 2.837211468418056379718 | 9170 | 451686 | 1.2796·10⁻¹³ |
| 915 | 1 | 2.839042458966870579415 | 23344 | 389497 | 7.6777·10⁻¹⁴ |
| 916 | 1 | 2.840875449498645887287 | 37546 | 327190 | 2.6447·10⁻¹³ |
| 917 | 1 | 2.842710440013360305630 | 51775 | 264769 | 1.1348·10⁻¹³ |
| 918 | 1 | 2.844547430510991812748 | 66032 | 202230 | 1.5736·10⁻¹³ |
| 919 | 1 | 2.846386420991518362960 | 80317 | 139573 | 3.7405·10⁻¹³ |
| 920 | 1 | 2.848227411454917886598 | 94629 | 76802 | 1.8593·10⁻¹³ |
| 921 | 1 | 2.850070401901168290002 | 108969 | 13913 | 1.2646·10⁻¹³ |
| 922 | 1 | 2.851915392330247455527 | 0 | 444255 | 2.6481·10⁻⁷ |
| 923 | 1 | 2.853762382742133241540 | 0 | 438714 | 2.5681·10⁻⁷ |
| 924 | 1 | 2.855611373136803482419 | 0 | 433167 | 2.4880·10⁻⁷ |
| 925 | 1 | 2.857462363514235988554 | 0 | 427614 | 2.4077·10⁻⁷ |
| 926 | 1 | 2.859315353874408546347 | 0 | 422055 | 2.3272·10⁻⁷ |
| 927 | 1 | 2.861170344217298918210 | 0 | 416490 | 2.2466·10⁻⁷ |
| 928 | 1 | 2.863027334542884842569 | 0 | 410919 | 2.1659·10⁻⁷ |
| 929 | 1 | 2.864886324851144033861 | 0 | 405342 | 2.0850·10⁻⁷ |
| 930 | 1 | 2.866747315142054182532 | 0 | 399759 | 2.0039·10⁻⁷ |
| 931 | 1 | 2.868610305415592955043 | 0 | 394170 | 1.9227·10⁻⁷ |
| 932 | 1 | 2.870475295671737993863 | 0 | 388575 | 1.8413·10⁻⁷ |
| 933 | 1 | 2.872342285910466917475 | 0 | 382974 | 1.7598·10⁻⁷ |
| 934 | 1 | 2.874211276131757320371 | 0 | 377367 | 1.6781·10⁻⁷ |
| 935 | 1 | 2.876082266335586773056 | 0 | 371754 | 1.5962·10⁻⁷ |
| 936 | 1 | 2.877955256521932822044 | 0 | 366135 | 1.5142·10⁻⁷ |
| 937 | 1 | 2.879830246690772989863 | 0 | 360510 | 1.4321·10⁻⁷ |
| 938 | 1 | 2.881707236842084775047 | 0 | 354879 | 1.3497·10⁻⁷ |
| 939 | 1 | 2.883586226975845652147 | 0 | 349242 | 1.2673·10⁻⁷ |
| 940 | 1 | 2.885467217092033071719 | 0 | 343599 | 1.1846·10⁻⁷ |
| 941 | 1 | 2.887350207190624460334 | 0 | 337950 | 1.1018·10⁻⁷ |
| 942 | 1 | 2.889235197271597220572 | 0 | 332295 | 1.0189·10⁻⁷ |
| 943 | 1 | 2.891122187334928731023 | 0 | 326634 | 9.3578·10⁻⁸ |
| 944 | 1 | 2.893011177380596346288 | 0 | 320967 | 8.5251·10⁻⁸ |
| 945 | 1 | 2.894902167408577396979 | 0 | 315294 | 7.6907·10⁻⁸ |
| 946 | 1 | 2.896795157418849189719 | 0 | 309615 | 6.8547·10⁻⁸ |
| 947 | 1 | 2.898690147411389007140 | 0 | 303930 | 6.0172·10⁻⁸ |
| 948 | 1 | 2.900587137386174107884 | 0 | 298239 | 5.1780·10⁻⁸ |
| 949 | 1 | 2.902486127343181726605 | 0 | 292542 | 4.3372·10⁻⁸ |
| 950 | 1 | 2.904387117282389073966 | 0 | 286839 | 3.4949·10⁻⁸ |
| 951 | 1 | 2.906290107203773336641 | 0 | 281130 | 2.6509·10⁻⁸ |
| 952 | 1 | 2.908195097107311677312 | 0 | 275415 | 1.8053·10⁻⁸ |
| 953 | 1 | 2.910102086992981234673 | 0 | 269694 | 9.5808·10⁻⁹ |
| 954 | 1 | 2.912011076860759123429 | 0 | 263967 | 1.0925·10⁻⁹ |
| 955 | 1 | 2.913922066710622434291 | 13342 | 204866 | 1.6813·10⁻¹³ |
| 956 | 1 | 2.915835056542548233985 | 28680 | 137775 | 5.0601·10⁻¹³ |
| 957 | 1 | 2.917750046356513565241 | 44046 | 70566 | 1.6119·10⁻¹³ |
| 958 | 1 | 2.919667036152495446804 | 59442 | 3231 | 2.2181·10⁻¹³ |
| 959 | 1 | 2.921586025930470873426 | 0 | 235243 | 2.9174·10⁻⁷ |
| 960 | 1 | 2.923507015690416815869 | 0 | 229480 | 2.8315·10⁻⁷ |
| 961 | 1 | 2.925430005432310220905 | 0 | 223711 | 2.7455·10⁻⁷ |
| 962 | 1 | 2.927354995156128011315 | 0 | 217936 | 2.6593·10⁻⁷ |
| 963 | 1 | 2.929281984861847085890 | 0 | 212155 | 2.5729·10⁻⁷ |
| 964 | 1 | 2.931210974549444319430 | 0 | 206368 | 2.4864·10⁻⁷ |
| 965 | 1 | 2.933141964218896562744 | 0 | 200575 | 2.3997·10⁻⁷ |
| 966 | 1 | 2.935074953870180642652 | 0 | 194776 | 2.3129·10⁻⁷ |
| 967 | 1 | 2.937009943503273361981 | 0 | 188971 | 2.2259·10⁻⁷ |
| 968 | 1 | 2.938946933118151499570 | 0 | 183160 | 2.1387·10⁻⁷ |
| 969 | 1 | 2.940885922714791810264 | 0 | 177343 | 2.0514·10⁻⁷ |
| 970 | 1 | 2.942826912293171024920 | 0 | 171520 | 1.9639·10⁻⁷ |
| 971 | 1 | 2.944769901853265850402 | 0 | 165691 | 1.8762·10⁻⁷ |
| 972 | 1 | 2.946714891395052969584 | 0 | 159856 | 1.7884·10⁻⁷ |
| 973 | 1 | 2.948661880918509041348 | 0 | 154015 | 1.7004·10⁻⁷ |
| 974 | 1 | 2.950610870423610700587 | 0 | 148168 | 1.6122·10⁻⁷ |
| 975 | 1 | 2.952561859910334558202 | 0 | 142315 | 1.5239·10⁻⁷ |
| 976 | 1 | 2.954514849378657201101 | 0 | 136456 | 1.4354·10⁻⁷ |
| 977 | 1 | 2.956469838828555192203 | 0 | 130591 | 1.3467·10⁻⁷ |
| 978 | 1 | 2.958426828260005070435 | 0 | 124720 | 1.2579·10⁻⁷ |
| 979 | 1 | 2.960385817672983350732 | 0 | 118843 | 1.1689·10⁻⁷ |
| 980 | 1 | 2.962346807067466524040 | 0 | 112960 | 1.0797·10⁻⁷ |
| 981 | 1 | 2.964309796443431057310 | 0 | 107071 | 9.9043·10⁻⁸ |
| 982 | 1 | 2.966274785800853393505 | 0 | 101176 | 9.0092·10⁻⁸ |
| 983 | 1 | 2.968241775139709951594 | 0 | 95275 | 8.1125·10⁻⁸ |
| 984 | 1 | 2.970210764459977126556 | 0 | 89368 | 7.2141·10⁻⁸ |
| 985 | 1 | 2.972181753761631289378 | 0 | 83455 | 6.3140·10⁻⁸ |
| 986 | 1 | 2.974154743044648787056 | 0 | 77536 | 5.4122·10⁻⁸ |
| 987 | 1 | 2.976129732309005942592 | 0 | 71611 | 4.5087·10⁻⁸ |
| 988 | 1 | 2.978106721554679054999 | 0 | 65680 | 3.6035·10⁻⁸ |
| 989 | 1 | 2.980085710781644399297 | 0 | 59743 | 2.6966·10⁻⁸ |
| 990 | 1 | 2.982066699989878226514 | 0 | 53800 | 1.7880·10⁻⁸ |
| 991 | 1 | 2.984049689179356763687 | 0 | 47851 | 8.7776·10⁻⁹ |
| 992 | 1 | 2.986034678350056213861 | 617 | 39428 | 4.7138·10⁻¹³ |
| 993 | 1 | 2.988021667501952756089 | 0 | 35936 | 3.2385·10⁻⁷ |
| 994 | 1 | 2.990010656635022545430 | 0 | 29969 | 3.1469·10⁻⁷ |
| 995 | 1 | 2.992001645749241712955 | 0 | 23996 | 3.0552·10⁻⁷ |
| 996 | 1 | 2.993994634844586365739 | 0 | 18017 | 2.9633·10⁻⁷ |
| 997 | 1 | 2.995989623921032586868 | 0 | 12032 | 2.8713·10⁻⁷ |
| 998 | 1 | 2.997986612978556435434 | 0 | 6041 | 2.7791·10⁻⁷ |
| 999 | 1 | 2.999985602017133946538 | 0 | 44 | 2.6867·10⁻⁷ |

*Used in* [[lem:is-z3]], [[lem:is-gap-z]], [[thm:is-gap]], [[prop:is-count]] and [[cor:is-flat]].

#### The non-real roots {#sec:tab-is-complex}

*Object.* For each row, the root of P_l of positive imaginary part and real part in (2, 3); it lies in the disc of
centre a + ib and radius 10⁻²¹, and its real part in (a − 10⁻²¹, a + 10⁻²¹). The columns p, q and m hold for it and for
its conjugate. The column b increases with l, each entry exceeding the one before by more than 2·10⁻²¹.

| l | a | b | p | q | m |
|---|---|---|---|---|---|
| 136 | 2.5141162881969976652708 | 0.0385753719698459447844 | 234366 | 520188 | 4.4154·10⁻¹³ |
| 137 | 2.5143225449776135358472 | 0.0719169217917912030709 | 0 | 1457034 | 1.2675·10⁻⁷ |
| 138 | 2.5145303018068298026990 | 0.0942486658096933715917 | 209226 | 619506 | 1.1252·10⁻¹³ |
| 139 | 2.5147395586846579297394 | 0.1123403810543393205545 | 346522 | 69694 | 3.9065·10⁻¹³ |
| 140 | 2.5149503156111088965165 | 0.1280027111283430130756 | 183728 | 720238 | 5.0831·10⁻¹³ |
| 141 | 2.5151625725861932180235 | 0.1420415760203332465967 | 320843 | 171141 | 7.0456·10⁻¹⁴ |
| 142 | 2.5153763296099209635452 | 0.1548990212669278964287 | 157869 | 822396 | 4.8266·10⁻¹⁴ |
| 143 | 2.5155915866823017745908 | 0.1668483930268930572626 | 294805 | 274006 | 4.5828·10⁻¹⁴ |
| 144 | 2.5158083438033448819653 | 0.1780725905398306832959 | 131652 | 925968 | 4.7792·10⁻¹³ |
| 145 | 2.5160266009730591220263 | 0.1887010607026164309152 | 268408 | 378289 | 3.9229·10⁻¹³ |
| 146 | 2.5162463581914529521687 | 0.1988293601645533436859 | 105074 | 1030966 | 2.0293·10⁻¹³ |
| 147 | 2.5164676154585344655815 | 0.2085303808588435102538 | 241650 | 483998 | 6.7941·10⁻¹⁴ |
| 148 | 2.5166903727743114053126 | 0.2178612079328622433300 | 78137 | 1137382 | 4.0061·10⁻¹³ |
| 149 | 2.5169146301387911776816 | 0.2268675225391377799886 | 214533 | 591125 | 2.4726·10⁻¹³ |
| 150 | 2.5171403875519808650718 | 0.2355865448194782208465 | 50839 | 1245224 | 2.0502·10⁻¹⁴ |
| 151 | 2.5173676450138872381367 | 0.2440490681130961544995 | 187056 | 699674 | 4.3267·10⁻¹³ |
| 152 | 2.5175964025245167674491 | 0.2522809053343515712132 | 23182 | 1354484 | 2.2913·10⁻¹³ |
| 153 | 2.5178266600838756346241 | 0.2603039425737323423579 | 159218 | 809649 | 1.2161·10⁻¹³ |
| 154 | 2.5180584176919697429404 | 0.2681369228319678719095 | 0 | 1445826 | 2.6866·10⁻⁹ |
| 155 | 2.5182916753488047274877 | 0.2757960397894092437995 | 131021 | 921042 | 4.7354·10⁻¹³ |
| 156 | 2.5185264330543859648635 | 0.2832953949841047290243 | 0 | 1444422 | 1.8452·10⁻⁸ |
| 157 | 2.5187626908087185824410 | 0.2906473549130075323486 | 102463 | 1033861 | 4.2143·10⁻¹³ |
| 158 | 2.5190004486118074672321 | 0.2978628335715942673182 | 0 | 1443000 | 3.4417·10⁻⁸ |
| 159 | 2.5192397064636572743621 | 0.3049515186015761810252 | 73544 | 1148106 | 5.3523·10⁻¹⁵ |
| 160 | 2.5194804643642724351793 | 0.3119220542072076167081 | 0 | 1441560 | 5.0583·10⁻⁸ |
| 161 | 2.5197227223136571650143 | 0.3187821905199535259994 | 44266 | 1263769 | 3.7276·10⁻¹³ |
| 162 | 2.5199664803118154706075 | 0.3255389066310878794683 | 0 | 1440102 | 6.6949·10⁻⁸ |
| 163 | 2.5202117383587511572207 | 0.3321985127458052099690 | 14627 | 1380858 | 4.4547·10⁻¹³ |
| 164 | 2.5204584964544678354488 | 0.3387667356266980419853 | 0 | 1438626 | 8.3515·10⁻⁸ |
| 165 | 2.5207067545989689277442 | 0.3452487905461545755054 | 0 | 1437881 | 8.5408·10⁻⁹ |
| 166 | 2.5209565127922576746695 | 0.3516494422594035331609 | 0 | 1437132 | 1.0028·10⁻⁷ |
| 167 | 2.5212077710343371408902 | 0.3579730569757361459399 | 0 | 1436378 | 2.5407·10⁻⁸ |
| 168 | 2.5214605293252102209205 | 0.3642236468981342932058 | 0 | 1435620 | 1.1724·10⁻⁷ |
| 169 | 2.5217147876648796446325 | 0.3704049085880207965222 | 0 | 1434857 | 4.2474·10⁻⁸ |
| 170 | 2.5219705460533479825418 | 0.3765202561683807968442 | 358050 | 1889 | 2.1286·10⁻¹³ |
| 171 | 2.5222278044906176508779 | 0.3825728501878623487465 | 0 | 1433318 | 5.9742·10⁻⁸ |
| 172 | 2.5224865629766909164501 | 0.3885656228180278434360 | 326788 | 125389 | 1.1820·10⁻¹³ |
| 173 | 2.5227468215115699013194 | 0.3945012999363516618333 | 0 | 1431761 | 7.7210·10⁻⁸ |
| 174 | 2.5230085800952565872823 | 0.4003824205518617909509 | 295166 | 250311 | 4.1302·10⁻¹³ |
| 175 | 2.5232718387277528201789 | 0.4062113539532415639538 | 0 | 1430186 | 9.4878·10⁻⁸ |
| 176 | 2.5235365974090603140298 | 0.4119903148967429813389 | 263182 | 376663 | 1.5348·10⁻¹⁵ |
| 177 | 2.5238028561391806550111 | 0.4177213771003523791931 | 0 | 1428593 | 1.1274·10⁻⁷ |
| 178 | 2.5240706149181153052751 | 0.4234064852689295784108 | 230838 | 504437 | 8.0553·10⁻¹⁵ |
| 179 | 2.5243398737458656066222 | 0.4290474658406774298465 | 0 | 1426982 | 1.3081·10⁻⁷ |
| 180 | 2.5246106326224327840317 | 0.4346460366168544685810 | 198134 | 633633 | 4.4380·10⁻¹³ |
| 181 | 2.5248828915478179490567 | 0.4402038154129897793189 | 331646 | 98768 | 3.0758·10⁻¹³ |
| 182 | 2.5251566505220221030903 | 0.4457223278501022043721 | 165068 | 764259 | 2.0703·10⁻¹³ |
| 183 | 2.5254319095450461405076 | 0.4512030143878541332365 | 298400 | 230105 | 2.9305·10⁻¹³ |
| 184 | 2.5257086686168908516888 | 0.4566472366876138666423 | 131642 | 896307 | 4.1644·10⁻¹³ |
| 185 | 2.5259869277375569259294 | 0.4620562833816019205755 | 264793 | 362868 | 1.7231·10⁻¹³ |
| 186 | 2.5262666869070449542419 | 0.4674313753142854048938 | 97855 | 1029781 | 5.2238·10⁻¹³ |
| 187 | 2.5265479461253554320530 | 0.4727736703136601271101 | 230826 | 497053 | 5.0604·10⁻¹³ |
| 188 | 2.5268307053924887618014 | 0.4780842675427770904703 | 63707 | 1164681 | 5.2923·10⁻¹³ |
| 189 | 2.5271149647084452554406 | 0.4833642114756276697764 | 196497 | 632668 | 1.8671·10⁻¹³ |
| 190 | 2.5274007240732251368496 | 0.4886144955361346970204 | 29198 | 1301007 | 4.3983·10⁻¹³ |
| 191 | 2.5276879834868285441564 | 0.4938360654343684954545 | 161808 | 769705 | 3.2760·10⁻¹³ |
| 192 | 2.5279767429492555319775 | 0.4990298222301044335705 | 0 | 1416071 | 3.1513·10⁻⁹ |
| 193 | 2.5282670024605060735766 | 0.5041966251503677082752 | 126758 | 908168 | 3.7392·10⁻¹³ |
| 194 | 2.5285587620205800629461 | 0.5093372941845932299135 | 0 | 1414325 | 2.2723·10⁻⁸ |
| 195 | 2.5288520216294773168148 | 0.5144526124783978458950 | 91347 | 1048057 | 3.2514·10⁻¹³ |
| 196 | 2.5291467812871975765839 | 0.5195433285446633851888 | 0 | 1412561 | 4.2496·10⁻⁸ |
| 197 | 2.5294430409937405101953 | 0.5246101583086154970203 | 55575 | 1189372 | 1.7950·10⁻¹³ |
| 198 | 2.5297408007491057139340 | 0.5296537870018155597654 | 0 | 1410779 | 6.2470·10⁻⁸ |
| 199 | 2.5300400605532927141678 | 0.5346748709184276090151 | 19443 | 1332109 | 4.8962·10⁻¹³ |
| 200 | 2.5303408204063009690266 | 0.5396740390457508380441 | 0 | 1408979 | 8.2644·10⁻⁸ |
| 201 | 2.5306430803081298700237 | 0.5446518945797965088012 | 0 | 1408072 | 9.4729·10⁻⁹ |
| 202 | 2.5309468402587787436208 | 0.5496090163356153435569 | 0 | 1407161 | 1.0301·10⁻⁷ |
| 203 | 2.5312521002582468527406 | 0.5545459600611298750713 | 0 | 1406245 | 2.9947·10⁻⁸ |
| 204 | 2.5315588603065333982266 | 0.5594632596623805465921 | 0 | 1405325 | 1.2359·10⁻⁷ |
| 205 | 2.5318671204036375202544 | 0.5643614283473414202440 | 0 | 1404400 | 5.0622·10⁻⁸ |
| 206 | 2.5321768805495582996950 | 0.5692409596947898196936 | 340137 | 42922 | 2.0853·10⁻¹³ |
| 207 | 2.5324881407442947594322 | 0.5741023286541142769978 | 0 | 1402537 | 7.1497·10⁻⁸ |
| 208 | 2.5328009009878458656367 | 0.5789459924814082565808 | 302381 | 192074 | 2.8214·10⁻¹³ |
| 209 | 2.5331151612802105289967 | 0.5837723916167158902091 | 0 | 1400656 | 9.2573·10⁻⁸ |
| 210 | 2.5334309216213876059089 | 0.5885819505068639315900 | 264264 | 342652 | 2.2112·10⁻¹³ |
| 211 | 2.5337481820113758996296 | 0.5933750783779257059156 | 0 | 1398757 | 1.1384·10⁻⁷ |
| 212 | 2.5340669424501741613885 | 0.5981521699610130742299 | 225786 | 494656 | 1.6107·10⁻¹⁴ |
| 213 | 2.5343872029377810914658 | 0.6029136061747770514777 | 0 | 1396840 | 1.3532·10⁻⁷ |
| 214 | 2.5347089634741953402343 | 0.6076597547677129349608 | 186948 | 648082 | 2.1245·10⁻¹³ |
| 215 | 2.5350322240594155091686 | 0.6123909709231082984043 | 317394 | 125328 | 4.9524·10⁻¹³ |
| 216 | 2.5353569846934401518205 | 0.6171075978292390645060 | 147749 | 802934 | 2.4363·10⁻¹³ |
| 217 | 2.5356832453762677747645 | 0.6218099672172075093518 | 278014 | 280895 | 1.6169·10⁻¹³ |
| 218 | 2.5360110061078968385121 | 0.6264983998686241996738 | 108189 | 959212 | 9.7875·10⁻¹⁴ |
| 219 | 2.5363402668883257583978 | 0.6311732060951615051812 | 238274 | 437884 | 2.0060·10⁻¹³ |
| 220 | 2.5366710277175529054369 | 0.6358346861918476789747 | 68269 | 1116912 | 3.1824·10⁻¹³ |
| 221 | 2.5370032885955766071561 | 0.6404831308658259760625 | 198173 | 596299 | 4.3567·10⁻¹⁴ |
| 222 | 2.5373370495223951483983 | 0.6451188216421714760507 | 27988 | 1276038 | 3.3597·10⁻¹³ |
| 223 | 2.5376723104980067721023 | 0.6497420312482379387239 | 157712 | 756136 | 2.3259·10⁻¹³ |
| 224 | 2.5380090715224096800583 | 0.6543530239778970341983 | 0 | 1385974 | 7.0301·10⁻⁹ |
| 225 | 2.5383473325956020336402 | 0.6589520560369316562907 | 116890 | 917399 | 1.9790·10⁻¹³ |
| 226 | 2.5386870937175819545148 | 0.6635393758707528583330 | 0 | 1383940 | 2.9809·10⁻⁸ |
| 227 | 2.5390283548883475253301 | 0.6681152244755254480507 | 75708 | 1080084 | 4.8019·10⁻¹³ |
| 228 | 2.5393711161078967903821 | 0.6726798356937097283928 | 0 | 1381888 | 5.2788·10⁻⁸ |
| 229 | 2.5397153773762277562614 | 0.6772334364949556338332 | 34165 | 1244195 | 5.0841·10⁻¹³ |
| 230 | 2.5400611386933383924804 | 0.6817762472432200113468 | 0 | 1379818 | 7.5968·10⁻⁸ |
| 231 | 2.5404084000592266320814 | 0.6863084819509175146038 | 0 | 1378776 | 4.2997·10⁻⁹ |
| 232 | 2.5407571614738903722269 | 0.6908303485208600531036 | 0 | 1377730 | 9.9347·10⁻⁸ |
| 233 | 2.5411074229373274747718 | 0.6953420489766885450838 | 0 | 1376679 | 2.7779·10⁻⁸ |
| 234 | 2.5414591844495357668187 | 0.6998437796824534852006 | 0 | 1375624 | 1.2292·10⁻⁷ |
| 235 | 2.5418124460105130412573 | 0.7043357315519572128889 | 0 | 1374564 | 5.1459·10⁻⁸ |
| 236 | 2.5421672076202570572871 | 0.7088180902484304454356 | 335925 | 29799 | 3.5629·10⁻¹³ |
| 237 | 2.5425234692787655409250 | 0.7132910363750783409093 | 0 | 1372431 | 7.5340·10⁻⁸ |
| 238 | 2.5428812309860361854988 | 0.7177547456569968262455 | 292760 | 200317 | 4.2265·10⁻¹³ |
| 239 | 2.5432404927420666521252 | 0.7222093891149279346280 | 0 | 1370280 | 9.9421·10⁻⁸ |
| 240 | 2.5436012545468545701749 | 0.7266551332312932346750 | 249234 | 372261 | 1.3946·10⁻¹³ |
| 241 | 2.5439635164003975377235 | 0.7310921401089169117134 | 0 | 1368111 | 1.2370·10⁻⁷ |
| 242 | 2.5443272783026931219902 | 0.7355205676228245056628 | 205348 | 545627 | 4.3184·10⁻¹⁴ |
| 243 | 2.5446925402537388597633 | 0.7399405695654795632653 | 333270 | 32843 | 9.6535·10⁻¹⁴ |
| 244 | 2.5450593022535322578138 | 0.7443522957857983810412 | 161102 | 720415 | 1.1423·10⁻¹³ |
| 245 | 2.5454275643020707932976 | 0.7487558923222624684997 | 288844 | 208342 | 2.4375·10⁻¹³ |
| 246 | 2.5457973263993519141457 | 0.7531515015304292292230 | 116496 | 896625 | 3.3254·10⁻¹³ |
| 247 | 2.5461685885453730394439 | 0.7575392622051235312391 | 244058 | 385263 | 5.2803·10⁻¹³ |
| 248 | 2.5465413507401315598018 | 0.7619193096975762176768 | 71529 | 1074261 | 1.2204·10⁻¹³ |
| 249 | 2.5469156129836248377110 | 0.7662917760277601026115 | 198911 | 563610 | 3.7305·10⁻¹³ |
| 250 | 2.5472913752758502078941 | 0.7706567899921595214775 | 26202 | 1253319 | 1.7285·10⁻¹⁴ |
| 251 | 2.5476686376168049776434 | 0.7750144772671959836334 | 153404 | 743379 | 3.1315·10⁻¹³ |
| 252 | 2.5480474000064864271504 | 0.7793649605085198361551 | 0 | 1355859 | 1.0824·10⁻⁸ |
| 253 | 2.5484276624448918098269 | 0.7837083594463660279724 | 107537 | 924570 | 3.2670·10⁻¹³ |
| 254 | 2.5488094249320183526158 | 0.7880447909771610026137 | 0 | 1353573 | 3.6406·10⁻⁸ |
| 255 | 2.5491926874678632562952 | 0.7923743692515573913844 | 61310 | 1107183 | 3.9160·10⁻¹³ |
| 256 | 2.5495774500524236957730 | 0.7966972057590634764613 | 0 | 1351269 | 6.2188·10⁻⁸ |
| 257 | 2.5499637126856968203738 | 0.8010134094094252987978 | 14723 | 1291218 | 4.8537·10⁻¹³ |
| 258 | 2.5503514753676797541185 | 0.8053230866109107561932 | 0 | 1348947 | 8.8170·10⁻⁸ |
| 259 | 2.5507407380983695959958 | 0.8096263413456370329967 | 0 | 1347779 | 1.7902·10⁻⁸ |
| 260 | 2.5511315008777634202268 | 0.8139232752420751883568 | 0 | 1346607 | 1.1435·10⁻⁷ |
| 261 | 2.5515237637058582765223 | 0.8182139876448586711116 | 0 | 1345430 | 4.4184·10⁻⁸ |
| 262 | 2.5519175265826511903338 | 0.8224985756820158953510 | 0 | 1344249 | 1.4073·10⁻⁷ |
| 263 | 2.5523127895081391630969 | 0.8267771343297407726704 | 0 | 1343063 | 7.0666·10⁻⁸ |
| 264 | 2.5527095524823191724694 | 0.8310497564748092286602 | 298833 | 146540 | 5.4128·10⁻¹³ |
| 265 | 2.5531078155051881725622 | 0.8353165329747442076692 | 0 | 1340678 | 9.7347·10⁻⁸ |
| 266 | 2.5535075785767430941647 | 0.8395775527158264685733 | 250626 | 336974 | 4.7576·10⁻¹³ |
| 267 | 2.5539088416969808449643 | 0.8438329026690435741068 | 0 | 1338275 | 1.2422·10⁻⁷ |
| 268 | 2.5543116048658983097598 | 0.8480826679440648576790 | 202059 | 528830 | 3.0828·10⁻¹³ |
| 269 | 2.5547158680834923506699 | 0.8523269318413257963701 | 327641 | 25289 | 4.9378·10⁻¹³ |
| 270 | 2.5551216313497598073356 | 0.8565657759023011101079 | 153132 | 722108 | 1.3830·10⁻¹⁴ |
| 271 | 2.5555288946646974971183 | 0.8607992799580420292073 | 278534 | 219278 | 1.2635·10⁻¹³ |
| 272 | 2.5559376580283022152918 | 0.8650275221760495109504 | 103846 | 916804 | 1.2258·10⁻¹³ |
| 273 | 2.5563479214405707352301 | 0.8692505791055517271495 | 229068 | 414685 | 1.4931·10⁻¹³ |
| 274 | 2.5567596849014998085905 | 0.8734685257212508760661 | 54200 | 1112922 | 5.3277·10⁻¹⁴ |
| 275 | 2.5571729484110861654916 | 0.8776814354656012819139 | 179243 | 611510 | 5.3676·10⁻¹³ |
| 276 | 2.5575877119693265146868 | 0.8818893802896778225320 | 4195 | 1310458 | 3.3537·10⁻¹³ |
| 277 | 2.5580039755762175437343 | 0.8860924306926909604650 | 129057 | 809761 | 1.5135·10⁻¹³ |
| 278 | 2.5584217392317559191615 | 0.8902906557602020351489 | 0 | 1324736 | 2.5650·10⁻⁸ |
| 279 | 2.5588410029359382866265 | 0.8944841232010899952806 | 78512 | 1009430 | 7.7616·10⁻¹⁴ |
| 280 | 2.5592617666887612710750 | 0.8986728993833184024942 | 0 | 1322216 | 5.3830·10⁻⁸ |
| 281 | 2.5596840304902214768933 | 0.9028570493685493124221 | 27608 | 1210517 | 2.8862·10⁻¹³ |
| 282 | 2.5601077943403154880576 | 0.9070366369456485298766 | 0 | 1319678 | 8.2210·10⁻⁸ |
| 283 | 2.5605330582390398682799 | 0.9112117246631247344826 | 0 | 1318402 | 1.3142·10⁻⁸ |
| 284 | 2.5609598221863911611498 | 0.9153823738605430753155 | 0 | 1317122 | 1.1079·10⁻⁷ |
| 285 | 2.5613880861823658902733 | 0.9195486446989520320302 | 0 | 1315837 | 4.1821·10⁻⁸ |
| 286 | 2.5618178502269605594081 | 0.9237105961903606300833 | 0 | 1314548 | 1.3956·10⁻⁷ |
| 287 | 2.5622491143201716525952 | 0.9278682862263014737590 | 0 | 1313254 | 7.0701·10⁻⁸ |
| 288 | 2.5626818784619956342883 | 0.9320217716055135179610 | 296612 | 125507 | 2.7741·10⁻¹³ |
| 289 | 2.5631161426524289494788 | 0.9361711080607770335680 | 0 | 1310653 | 9.9780·10⁻⁸ |
| 290 | 2.5635519068914680238188 | 0.9403163502849318273109 | 244090 | 332985 | 3.9090·10⁻¹⁴ |
| 291 | 2.5639891711791092637408 | 0.9444575519561084515935 | 0 | 1308034 | 1.2905·10⁻⁷ |
| 292 | 2.5644279355153490565745 | 0.9485947657622008787058 | 191210 | 541877 | 4.8726·10⁻¹³ |
| 293 | 2.5648681999001837706611 | 0.9527280434246079139208 | 314634 | 46860 | 2.5016·10⁻¹⁴ |
| 294 | 2.5653099643336097554642 | 0.9568574357212694797200 | 137970 | 752191 | 4.8184·10⁻¹³ |
| 295 | 2.5657532288156233416790 | 0.9609829925090228157344 | 261215 | 257881 | 3.3739·10⁻¹³ |
| 296 | 2.5661979933462208413384 | 0.9651047627453026029913 | 84371 | 963923 | 5.4911·10⁻¹³ |
| 297 | 2.5666442579253985479166 | 0.9692227945092080339646 | 207436 | 470324 | 1.5216·10⁻¹³ |
| 298 | 2.5670920225531527364304 | 0.9733371350219589091496 | 30412 | 1177077 | 1.0393·10⁻¹³ |
| 299 | 2.5675412872294796635381 | 0.9774478306667619439713 | 153299 | 684181 | 5.5068·10⁻¹³ |
| 300 | 2.5679920519543755676365 | 0.9815549270081076145084 | 0 | 1296025 | 1.3280·10⁻⁸ |
| 301 | 2.5684443167278366689546 | 0.9856584688105170545868 | 98802 | 899460 | 3.9185·10⁻¹³ |
| 302 | 2.5688980815498591696464 | 0.9897585000567577382514 | 0 | 1293307 | 4.3656·10⁻⁸ |
| 303 | 2.5693533464204392538807 | 0.9938550639655459385161 | 43946 | 1116157 | 2.0089·10⁻¹³ |
| 304 | 2.5698101113395730879294 | 0.9979482030087532438302 | 0 | 1290571 | 7.4231·10⁻⁸ |
| 305 | 2.5702683763072568202531 | 1.0020379589281337361548 | 0 | 1289196 | 6.2605·10⁻⁹ |
| 306 | 2.5707281413234865815856 | 1.0061243727515877873183 | 0 | 1287817 | 1.0500·10⁻⁷ |
| 307 | 2.5711894063882584850158 | 1.0102074848089778118764 | 0 | 1286433 | 3.7134·10⁻⁸ |
| 308 | 2.5716521715015686260679 | 1.0142873347475107236202 | 0 | 1285045 | 1.3597·10⁻⁷ |
| 309 | 2.5721164366634130827804 | 1.0183639615467012777746 | 0 | 1283652 | 6.8207·10⁻⁸ |
| 310 | 2.5725822018737879157822 | 1.0224374035329299405478 | 299125 | 85754 | 1.2833·10⁻¹³ |
| 311 | 2.5730494671326891683680 | 1.0265076983936084107998 | 0 | 1280853 | 9.9480·10⁻⁸ |
| 312 | 2.5735182324401128665715 | 1.0305748831909654240527 | 242655 | 308826 | 2.4343·10⁻¹³ |
| 313 | 2.5739884977960550192371 | 1.0346389943754649957904 | 0 | 1278036 | 1.3095·10⁻⁷ |
| 314 | 2.5744602632005116180900 | 1.0387000677988688079454 | 185826 | 533316 | 1.5462·10⁻¹³ |
| 315 | 2.5749335286534786378048 | 1.0427581387269540086953 | 307277 | 46092 | 1.3067·10⁻¹³ |
| 316 | 2.5754082941549520360726 | 1.0468132418518972802526 | 128639 | 759220 | 3.8534·10⁻¹³ |
| 317 | 2.5758845597049277536666 | 1.0508654113043356313695 | 249911 | 272703 | 5.0902·10⁻¹³ |
| 318 | 2.5763623253034017145058 | 1.0549146806651139899648 | 71093 | 986542 | 3.4763·10⁻¹³ |
| 319 | 2.5768415909503698257185 | 1.0589610829767293058282 | 192185 | 500736 | 4.7072·10⁻¹⁴ |
| 320 | 2.5773223566458279777030 | 1.0630046507544805230317 | 13188 | 1215282 | 8.7970·10⁻¹⁵ |
| 321 | 2.5778046223897720441879 | 1.0670454159973334457730 | 134102 | 730179 | 3.7867·10⁻¹³ |
| 322 | 2.5782883881821978822911 | 1.0710834101985091992222 | 0 | 1265136 | 2.5041·10⁻⁸ |
| 323 | 2.5787736540231013325767 | 1.0751186643558046779169 | 75660 | 961040 | 3.5965·10⁻¹³ |
| 324 | 2.5792604199124782191117 | 1.0791512089816530777375 | 0 | 1262220 | 5.7608·10⁻⁸ |
| 325 | 2.5797486858503243495210 | 1.0831810741129323229426 | 16860 | 1193315 | 5.1221·10⁻¹³ |
| 326 | 2.5802384518366355150409 | 1.0872082893205289265924 | 0 | 1259286 | 9.0375·10⁻⁸ |
| 327 | 2.5807297178714074905723 | 1.0912328837186645604421 | 0 | 1257812 | 2.3499·10⁻⁸ |
| 328 | 2.5812224839546360347318 | 1.0952548859739923585424 | 0 | 1256334 | 1.2334·10⁻⁷ |
| 329 | 2.5817167500863168899027 | 1.0992743243144697368873 | 0 | 1254851 | 5.6564·10⁻⁸ |
| 330 | 2.5822125162664457822839 | 1.1032912265380142790551 | 0 | 1253364 | 1.5650·10⁻⁷ |
| 331 | 2.5827097824950184219389 | 1.1073056200209490144758 | 0 | 1251872 | 8.9828·10⁻⁸ |
| 332 | 2.5832085487720305028426 | 1.1113175317262432013363 | 258238 | 217423 | 4.9461·10⁻¹³ |
| 333 | 2.5837088150974777029279 | 1.1153269882115545198097 | 0 | 1248875 | 1.2329·10⁻⁷ |
| 334 | 2.5842105814713556841313 | 1.1193340156370783829239 | 197826 | 456065 | 4.4413·10⁻¹³ |
| 335 | 2.5847138478936600924371 | 1.1233386397732098816082 | 0 | 1245860 | 1.5695·10⁻⁷ |
| 336 | 2.5852186143643865579211 | 1.1273408860080236969567 | 137056 | 696121 | 3.7720·10⁻¹³ |
| 337 | 2.5857248808835306947933 | 1.1313407793545771362092 | 256537 | 216678 | 5.0302·10⁻¹³ |
| 338 | 2.5862326474510881014394 | 1.1353383444580412790793 | 75928 | 937591 | 2.5880·10⁻¹³ |
| 339 | 2.5867419140670543604620 | 1.1393336056026650575674 | 195230 | 458855 | 3.4567·10⁻¹³ |
| 340 | 2.5872526807314250387207 | 1.1433265867185769350251 | 14442 | 1180475 | 5.3651·10⁻¹⁴ |
| 341 | 2.5877649474441956873708 | 1.1473173113884286987144 | 133565 | 702446 | 8.3839·10⁻¹⁴ |
| 342 | 2.5882787142053618419027 | 1.1513058028538857342016 | 0 | 1235165 | 2.6334·10⁻⁸ |
| 343 | 2.5887939810149190221787 | 1.1552920840219680093968 | 71543 | 947447 | 2.3742·10⁻¹³ |
| 344 | 2.5893107478728627324704 | 1.1592761774712458606782 | 0 | 1232069 | 6.0890·10⁻⁸ |
| 345 | 2.5898290147791884614946 | 1.1632581054578945431106 | 9163 | 1193862 | 2.1496·10⁻¹³ |
| 346 | 2.5903487817338916824491 | 1.1672378899216113810826 | 0 | 1228955 | 9.5645·10⁻⁸ |
| 347 | 2.5908700487369678530468 | 1.1712155524913992345425 | 0 | 1227391 | 2.9763·10⁻⁸ |
| 348 | 2.5913928157884124155505 | 1.1751911144912198792385 | 0 | 1225823 | 1.3059·10⁻⁷ |
| 349 | 2.5919170828882207968056 | 1.1791645969455207867725 | 0 | 1224250 | 6.4816·10⁻⁸ |
| 350 | 2.5924428500363884082732 | 1.1831360205846386817071 | 301649 | 16076 | 5.1329·10⁻¹³ |
| 351 | 2.5929701172329106460618 | 1.1871054058500831482413 | 0 | 1221091 | 1.0006·10⁻⁷ |
| 352 | 2.5934988844777828909592 | 1.1910727728997034579603 | 238017 | 267436 | 1.4393·10⁻¹³ |
| 353 | 2.5940291517710005084626 | 1.1950381416127416926997 | 0 | 1217914 | 1.3551·10⁻⁷ |
| 354 | 2.5945609191125588488093 | 1.1990015315947751425239 | 174029 | 520202 | 5.4502·10⁻¹³ |
| 355 | 2.5950941865024532470063 | 1.2029629621825508680507 | 291900 | 47118 | 2.2701·10⁻¹³ |
| 356 | 2.5956289539406790228588 | 1.2069224524487152287440 | 109682 | 774386 | 1.2620·10⁻¹⁴ |
| 357 | 2.5961652214272314809992 | 1.2108800212064410942119 | 227375 | 302005 | 4.7153·10⁻¹⁴ |
| 358 | 2.5967029889621059109147 | 1.2148356870139553738779 | 44979 | 1029976 | 1.7590·10⁻¹³ |
| 359 | 2.5972422565452975869747 | 1.2187894681789694215184 | 162494 | 558298 | 5.4413·10⁻¹³ |
| 360 | 2.5977830241768017684575 | 1.2227413827630147949809 | 0 | 1206652 | 1.1156·10⁻⁸ |
| 361 | 2.5983252918566136995768 | 1.2266914485856867778013 | 97254 | 816009 | 1.3423·10⁻¹⁴ |
| 362 | 2.5988690595847286095075 | 1.2306396832287979983390 | 0 | 1203394 | 4.7499·10⁻⁸ |
| 363 | 2.5994143273611417124106 | 1.2345861040404444133357 | 31658 | 1075126 | 8.3579·10⁻¹⁴ |
| 364 | 2.5999610951858482074587 | 1.2385307281389858564032 | 0 | 1200118 | 8.4041·10⁻⁸ |
| 365 | 2.6005093630588432788595 | 1.2424735724169432877555 | 0 | 1198473 | 1.9052·10⁻⁸ |
| 366 | 2.6010591309801220958805 | 1.2464146535448148194504 | 0 | 1196824 | 1.2078·10⁻⁷ |
| 367 | 2.6016103989496798128717 | 1.2503539879748125304061 | 0 | 1195170 | 5.5891·10⁻⁸ |
| 368 | 2.6021631669675115692892 | 1.2542915919445220274385 | 0 | 1193512 | 1.5771·10⁻⁷ |
| 369 | 2.6027174350336124897172 | 1.2582274814804866524536 | 0 | 1191849 | 9.2929·10⁻⁸ |
| 370 | 2.6032732031479776838904 | 1.2621616724017181816437 | 249261 | 193137 | 4.5099·10⁻¹³ |
| 371 | 2.6038304713106022467159 | 1.2660941803231358100293 | 0 | 1188510 | 1.3016·10⁻⁷ |
| 372 | 2.6043892395214812582940 | 1.2700250206589351638754 | 182059 | 458597 | 5.2484·10⁻¹³ |
| 373 | 2.6049495077806097839395 | 1.2739542086258890343427 | 0 | 1185153 | 1.6759·10⁻⁷ |
| 374 | 2.6055112760879828742019 | 1.2778817592465814781481 | 114500 | 725467 | 4.3014·10⁻¹³ |
| 375 | 2.6060745444435955648858 | 1.2818076873525768849433 | 230587 | 259429 | 5.5303·10⁻¹³ |
| 376 | 2.6066393128474428770706 | 1.2857320075875255665277 | 46584 | 993747 | 1.2724·10⁻¹³ |
| 377 | 2.6072055812995198171298 | 1.2896547344102073798331 | 162493 | 528412 | 4.0887·10⁻¹³ |
| 378 | 2.6077733497998213767500 | 1.2935758820975148538099 | 0 | 1176681 | 1.2049·10⁻⁸ |
| 379 | 2.6083426183483425329497 | 1.2974954647473772498455 | 94043 | 798801 | 5.5213·10⁻¹³ |
| 380 | 2.6089133869450782480974 | 1.3014134962816269461294 | 0 | 1173261 | 5.0175·10⁻⁸ |
| 381 | 2.6094856555900234699301 | 1.3053299904488094983782 | 25236 | 1070600 | 3.8702·10⁻¹³ |
| 382 | 2.6100594242831731315704 | 1.3092449608269386925251 | 0 | 1169823 | 8.8500·10⁻⁸ |
| 383 | 2.6106346930245221515443 | 1.3131584208261978693030 | 0 | 1168097 | 2.4404·10⁻⁸ |
| 384 | 2.6112114618140654337977 | 1.3170703836915887660860 | 0 | 1166367 | 1.2702·10⁻⁷ |
| 385 | 2.6117897306517978677139 | 1.3209808625055290878456 | 0 | 1164632 | 6.3026·10⁻⁸ |
| 386 | 2.6123694995377143281293 | 1.3248898701903999865999 | 0 | 1162893 | 1.6574·10⁻⁷ |
| 387 | 2.6129507684718096753500 | 1.3287974195110445972515 | 0 | 1161149 | 1.0184·10⁻⁷ |
| 388 | 2.6135335374540787551673 | 1.3327035230772187471757 | 231606 | 232976 | 1.7066·10⁻¹³ |
| 389 | 2.6141178064845163988735 | 1.3366081933459949273216 | 0 | 1157648 | 1.4086·10⁻⁷ |
| 390 | 2.6147035755631174232772 | 1.3405114426241205838778 | 161196 | 511106 | 5.8081·10⁻¹⁴ |
| 391 | 2.6152908446898766307181 | 1.3444132830703317617047 | 275858 | 50696 | 3.2780·10⁻¹³ |
| 392 | 2.6158796138647888090818 | 1.3483137266976231037278 | 90431 | 790638 | 5.2274·10⁻¹³ |
| 393 | 2.6164698830878487318143 | 1.3522127853754751842767 | 204914 | 330935 | 2.3210·10⁻¹³ |
| 394 | 2.6170616523590511579365 | 1.3561104708320401289279 | 19309 | 1071580 | 4.1177·10⁻¹³ |
| 395 | 2.6176549216783908320577 | 1.3600067946562864487357 | 133614 | 612580 | 9.5378·10⁻¹⁴ |
| 396 | 2.6182496910458624843894 | 1.3639017683001039927896 | 0 | 1145252 | 2.8983·10⁻⁸ |
| 397 | 2.6188459604614608307593 | 1.3677954030803698997939 | 61959 | 895627 | 4.3106·10⁻¹³ |
| 398 | 2.6194437299251805726239 | 1.3716877101809764068034 | 0 | 1141670 | 6.8890·10⁻⁸ |
| 399 | 2.6200429994370163970818 | 1.3755787006548213513478 | 0 | 1139872 | 5.5850·10⁻⁹ |
| 400 | 2.6206437689969629768865 | 1.3794683854257621819085 | 0 | 1138070 | 1.0899·10⁻⁷ |
| 401 | 2.6212460386050149704591 | 1.3833567752905342710634 | 0 | 1136263 | 4.5788·10⁻⁸ |
| 402 | 2.6218498082611670219001 | 1.3872438809206343055593 | 0 | 1134452 | 1.4929·10⁻⁷ |
| 403 | 2.6224550779654137610024 | 1.3911297128641695080949 | 0 | 1132636 | 8.6190·10⁻⁸ |
| 404 | 2.6230618477177498032623 | 1.3950142815476734266778 | 258363 | 97363 | 4.5057·10⁻¹³ |
| 405 | 2.6236701175181697498919 | 1.3988975972778890090372 | 0 | 1128991 | 1.2678·10⁻⁷ |
| 406 | 2.6242798873666681878305 | 1.4027796702435196617212 | 185107 | 386733 | 4.4055·10⁻¹³ |
| 407 | 2.6248911572632396897554 | 1.4066605105169489761531 | 0 | 1125328 | 1.6758·10⁻⁷ |
| 408 | 2.6255039272078788140939 | 1.4105401280559297870620 | 111495 | 677509 | 1.1174·10⁻¹³ |
| 409 | 2.6261181972005801050335 | 1.4144185327052432123181 | 224556 | 223422 | 1.2945·10⁻¹³ |
| 410 | 2.6267339672413380925329 | 1.4182957341983283072741 | 37529 | 969683 | 5.3166·10⁻¹³ |
| 411 | 2.6273512373301472923327 | 1.4221717421588829512338 | 150412 | 516299 | 3.5176·10⁻¹³ |
| 412 | 2.6279700074670022059656 | 1.4260465661024365686189 | 0 | 1116091 | 2.0441·10⁻⁸ |
| 413 | 2.6285902776518973207668 | 1.4299202154378952727702 | 75912 | 810582 | 1.4588·10⁻¹³ |
| 414 | 2.6292120478848271098838 | 1.4337926994690600060936 | 0 | 1112365 | 6.1928·10⁻⁸ |
| 415 | 2.6298353181657860322866 | 1.4376640273961182364221 | 1057 | 1106267 | 2.3214·10⁻¹⁴ |
| 416 | 2.6304600884947685327770 | 1.4415342083171097560119 | 0 | 1108621 | 1.0361·10⁻⁷ |
| 417 | 2.6310863588717690419985 | 1.4454032512293671164989 | 0 | 1106742 | 4.1196·10⁻⁸ |
| 418 | 2.6317141292967819764456 | 1.4492711650309312204143 | 0 | 1104859 | 1.4549·10⁻⁷ |
| 419 | 2.6323433997698017384728 | 1.4531379585219425774695 | 0 | 1102971 | 8.3176·10⁻⁸ |
| 420 | 2.6329741702908227163040 | 1.4570036404060087217734 | 262367 | 51610 | 2.4843·10⁻¹³ |
| 421 | 2.6336064408598392840414 | 1.4608682192915482744186 | 0 | 1099182 | 1.2535·10⁻⁷ |
| 422 | 2.6342402114768458016738 | 1.4647317036931121244643 | 186270 | 352200 | 3.4374·10⁻¹³ |
| 423 | 2.6348754821418366150861 | 1.4685941020326821902422 | 0 | 1095375 | 1.6772·10⁻⁷ |
| 424 | 2.6355122528548060560668 | 1.4724554226409482121015 | 109818 | 654192 | 3.2073·10⁻¹³ |
| 425 | 2.6361505236157484423172 | 1.4763156737585630171940 | 221459 | 205713 | 3.5763·10⁻¹³ |
| 426 | 2.6367902944246580774591 | 1.4801748635373766866579 | 33011 | 957586 | 1.3402·10⁻¹³ |
| 427 | 2.6374315652815292510432 | 1.4840330000416500455913 | 144475 | 509806 | 3.4974·10⁻¹³ |
| 428 | 2.6380743361863562385567 | 1.4878900912492478865005 | 0 | 1085778 | 2.4528·10⁻⁸ |
| 429 | 2.6387186071391333014315 | 1.4917461450528123274564 | 67136 | 815301 | 1.0961·10⁻¹³ |
| 430 | 2.6393643781398546870515 | 1.4956011692609166969901 | 0 | 1081908 | 6.7592·10⁻⁸ |
| 431 | 2.6400116491885146287607 | 1.4994551715992003287941 | 0 | 1079966 | 5.8651·10⁻⁹ |
| 432 | 2.6406604202851073458700 | 1.5033081597114846405673 | 0 | 1078020 | 1.1085·10⁻⁷ |
| 433 | 2.6413106914296270436652 | 1.5071601411608708628375 | 0 | 1076069 | 4.9224·10⁻⁸ |
| 434 | 2.6419624626220679134135 | 1.5110111234308197753105 | 0 | 1074114 | 1.5431·10⁻⁷ |
| 435 | 2.6426157338624241323712 | 1.5148611139262138002274 | 0 | 1072154 | 9.2781·10⁻⁸ |
| 436 | 2.6432705051506898637905 | 1.5187101199744017943458 | 243660 | 95549 | 2.8995·10⁻¹³ |
| 437 | 2.6439267764868592569261 | 1.5225581488262268735006 | 0 | 1068221 | 1.3653·10⁻⁷ |
| 438 | 2.6445845478709264470423 | 1.5264052076570375962332 | 164727 | 407339 | 3.7715·10⁻¹³ |
| 439 | 2.6452438193028855554196 | 1.5302513035676828257029 | 0 | 1064270 | 1.8048·10⁻⁷ |
| 440 | 2.6459045907827306893611 | 1.5340964435854905820010 | 85440 | 720527 | 5.3209·10⁻¹³ |
| 441 | 2.6465668623104559421990 | 1.5379406346652311900765 | 195663 | 277648 | 2.4105·10⁻¹³ |
| 442 | 2.6472306338860553933009 | 1.5417838836900650217445 | 5798 | 1035117 | 1.5201·10⁻¹³ |
| 443 | 2.6478959055095231080764 | 1.5456261974724751236783 | 115845 | 592933 | 4.0902·10⁻¹³ |
| 444 | 2.6485626771808531379825 | 1.5494675827551850168828 | 0 | 1054313 | 4.1220·10⁻⁸ |
| 445 | 2.6492309489000395205304 | 1.5533080462120619469008 | 35673 | 909616 | 5.2633·10⁻¹³ |
| 446 | 2.6499007206670762792912 | 1.5571475944490058579166 | 0 | 1050299 | 8.5859·10⁻⁸ |
| 447 | 2.6505719924819574239015 | 1.5609862340048243579806 | 0 | 1048285 | 2.4918·10⁻⁸ |
| 448 | 2.6512447643446769500695 | 1.5648239713520939367897 | 0 | 1046267 | 1.3069·10⁻⁷ |
| 449 | 2.6519190362552288395805 | 1.5686608128980076918071 | 0 | 1044244 | 6.9852·10⁻⁸ |
| 450 | 2.6525948082136070603026 | 1.5724967649852098129982 | 0 | 1042217 | 1.7572·10⁻⁷ |
| 451 | 2.6532720802198055661921 | 1.5763318338926170710826 | 0 | 1040185 | 1.1498·10⁻⁷ |
| 452 | 2.6539508522738182972991 | 1.5801660258362275489585 | 202284 | 229012 | 3.7549·10⁻¹³ |
| 453 | 2.6546311243756391797726 | 1.5839993469699168508417 | 0 | 1036108 | 1.6030·10⁻⁷ |
| 454 | 2.6553128965252621258658 | 1.5878318033862220186697 | 120520 | 551982 | 2.2611·10⁻¹³ |
| 455 | 2.6559961687226810339415 | 1.5916634011171133804475 | 229506 | 113988 | 4.9011·10⁻¹³ |
| 456 | 2.6566809409678897884770 | 1.5954941461347545504631 | 38403 | 876346 | 3.1619·10⁻¹³ |
| 457 | 2.6573672132608822600691 | 1.5993240443522507966596 | 147212 | 439051 | 4.0380·10⁻¹³ |
| 458 | 2.6580549856016523054390 | 1.6031531016243859859214 | 0 | 1025836 | 2.4482·10⁻⁸ |
| 459 | 2.6587442579901937674375 | 1.6069813237483483136177 | 64565 | 765508 | 4.8340·10⁻¹³ |
| 460 | 2.6594350304265004750494 | 1.6108087164644450194271 | 0 | 1021696 | 7.0495·10⁻⁸ |
| 461 | 2.6601273029105662433983 | 1.6146352854568062872597 | 0 | 1019619 | 1.0242·10⁻⁸ |
| 462 | 2.6608210754423848737514 | 1.6184610363540785229796 | 0 | 1017538 | 1.1670·10⁻⁷ |
| 463 | 2.6615163480219501535241 | 1.6222859747301071996182 | 0 | 1015452 | 5.6549·10⁻⁸ |
| 464 | 2.6622131206492558562843 | 1.6261101061046094558458 | 0 | 1013362 | 1.6311·10⁻⁷ |
| 465 | 2.6629113933242957417568 | 1.6299334359438366296457 | 0 | 1011267 | 1.0305·10⁻⁷ |
| 466 | 2.6636111660470635558281 | 1.6337559696612269053933 | 222518 | 119095 | 8.8058·10⁻¹⁵ |
| 467 | 2.6643124388175530305502 | 1.6375777126180482488940 | 0 | 1007064 | 1.4975·10⁻⁷ |
| 468 | 2.6650152116357578841453 | 1.6413986701240318013680 | 138283 | 451823 | 4.9935·10⁻¹³ |
| 469 | 2.6657194845016718210095 | 1.6452188474379958998861 | 246032 | 18714 | 1.1976·10⁻¹³ |
| 470 | 2.6664252574152885317173 | 1.6490382497684608883615 | 53694 | 785949 | 3.2630·10⁻¹³ |
| 471 | 2.6671325303766016930256 | 1.6528568822742548798737 | 161267 | 353535 | 1.5153·10⁻¹³ |
| 472 | 2.6678413033856049678776 | 1.6566747500651106278600 | 0 | 996477 | 1.7359·10⁻⁸ |
| 473 | 2.6685515764422920054066 | 1.6604918582022536605323 | 76150 | 689746 | 5.5492·10⁻¹³ |
| 474 | 2.6692633495466564409404 | 1.6643082116989818297804 | 0 | 992211 | 6.4745·10⁻⁸ |
| 475 | 2.6699766226986918960045 | 1.6681238155212364227917 | 0 | 990071 | 5.1784·10⁻⁹ |
| 476 | 2.6706913958983919783263 | 1.6719386745881649816587 | 0 | 987927 | 1.1232·10⁻⁷ |
| 477 | 2.6714076691457502818385 | 1.6757527937726759733523 | 0 | 985778 | 5.2857·10⁻⁸ |
| 478 | 2.6721254424407603866831 | 1.6795661779019854496102 | 0 | 983625 | 1.6010·10⁻⁷ |
| 479 | 2.6728447157834158592147 | 1.6833788317581558335284 | 0 | 981467 | 1.0073·10⁻⁷ |
| 480 | 2.6735654891737102520044 | 1.6871907600786269669405 | 225461 | 77460 | 1.0289·10⁻¹³ |
| 481 | 2.6742877626116371038428 | 1.6910019675567395500289 | 0 | 977138 | 1.4880·10⁻⁷ |
| 482 | 2.6750115360971899397439 | 1.6948124588422511020322 | 138758 | 419934 | 4.3490·10⁻¹³ |
| 483 | 2.6757368096303622709484 | 1.6986222385418445693858 | 0 | 972791 | 1.9707·10⁻⁷ |
| 484 | 2.6764635832111475949268 | 1.7024313112196297051683 | 51702 | 763802 | 3.0050·10⁻¹³ |
| 485 | 2.6771918568395393953831 | 1.7062396813976373413113 | 158042 | 336257 | 2.8797·10⁻¹³ |
| 486 | 2.6779216305155311422577 | 1.7100473535563066726694 | 0 | 966236 | 1.9836·10⁻⁸ |
| 487 | 2.6786529042391162917309 | 1.7138543321349656697444 | 70458 | 682210 | 1.8960·10⁻¹³ |
| 488 | 2.6793856780102882862259 | 1.7176606215323047345939 | 0 | 961844 | 6.8592·10⁻⁸ |
| 489 | 2.6801199518290405544118 | 1.7214662261068437122545 | 0 | 959641 | 9.7100·10⁻⁹ |
| 490 | 2.6808557256953665112071 | 1.7252711501773923678459 | 0 | 957434 | 1.1754·10⁻⁷ |
| 491 | 2.6815929996092595577822 | 1.7290753980235044374124 | 0 | 955222 | 5.8758·10⁻⁸ |
| 492 | 2.6823317735707130815627 | 1.7328789738859253584932 | 0 | 953006 | 1.6668·10⁻⁷ |
| 493 | 2.6830720475797204562324 | 1.7366818819670337843905 | 0 | 950785 | 1.0800·10⁻⁷ |
| 494 | 2.6838138216362750417361 | 1.7404841264312769841290 | 211144 | 103983 | 3.9663·10⁻¹³ |
| 495 | 2.6845570957403701842823 | 1.7442857114056002281648 | 0 | 946330 | 1.5744·10⁻⁷ |
| 496 | 2.6853018698919992163462 | 1.7480866409798702580096 | 121977 | 456187 | 2.5144·10⁻¹³ |
| 497 | 2.6860481440911554566728 | 1.7518869192072929360840 | 227262 | 32808 | 3.9247·10⁻¹³ |
| 498 | 2.6867959183378322102788 | 1.7556865501048251703017 | 32459 | 809777 | 3.8181·10⁻¹³ |
| 499 | 2.6875451926320227684562 | 1.7594855376535812061131 | 137568 | 387093 | 3.6275·10⁻¹³ |
| 500 | 2.6882959669737204087744 | 1.7632838857992333769990 | 0 | 935113 | 3.1895·10⁻⁸ |
| 501 | 2.6890482413629183950832 | 1.7670815984524074027104 | 47523 | 742764 | 5.2809·10⁻¹³ |
| 502 | 2.6898020157996099775149 | 1.7708786794890723228826 | 0 | 930595 | 8.2017·10⁻⁸ |
| 503 | 2.6905572902837883924874 | 1.7746751327509251520289 | 0 | 928329 | 2.3819·10⁻⁸ |
| 504 | 2.6913140648154468627065 | 1.7784709620457703403226 | 0 | 926059 | 1.3233·10⁻⁷ |
| 505 | 2.6920723393945785971683 | 1.7822661711478941230174 | 0 | 923784 | 7.4234·10⁻⁸ |
| 506 | 2.6928321140211767911617 | 1.7860607637984338398307 | 0 | 921505 | 1.8284·10⁻⁷ |
| 507 | 2.6935933886952346262711 | 1.7898547437057423041155 | 0 | 919221 | 1.2484·10⁻⁷ |
| 508 | 2.6943561634167452703781 | 1.7936481145457473001886 | 179598 | 198540 | 9.9577·10⁻¹⁴ |
| 509 | 2.6951204381857018776648 | 1.7974408799623062857426 | 0 | 914640 | 1.7565·10⁻⁷ |
| 510 | 2.6958862130020975886153 | 1.8012330435675563748720 | 87973 | 560450 | 1.9417·10⁻¹³ |
| 511 | 2.6966534878659255300183 | 1.8050246089422596758649 | 192029 | 141924 | 3.1273·10⁻¹³ |
| 512 | 2.6974222627771788149696 | 1.8088155796361440565678 | 0 | 907734 | 2.2240·10⁻⁹ |
| 513 | 2.6981925377358505428738 | 1.8126059591682394088118 | 99878 | 505911 | 5.0792·10⁻¹³ |
| 514 | 2.6989643127419337994470 | 1.8163957510272094820987 | 0 | 903108 | 5.3516·10⁻⁸ |
| 515 | 2.6997375877954216567188 | 1.8201849586716793554784 | 7376 | 871284 | 5.1595·10⁻¹³ |
| 516 | 2.7005123628963071730343 | 1.8239735855305586153125 | 0 | 898464 | 1.0500·10⁻⁷ |
| 517 | 2.7012886380445833930562 | 1.8277616350033603054048 | 0 | 896135 | 4.7487·10⁻⁸ |
| 518 | 2.7020664132402433477673 | 1.8315491104605157147890 | 0 | 893802 | 1.5668·10⁻⁷ |
| 519 | 2.7028456884832800544719 | 1.8353360152436850673022 | 0 | 891464 | 9.9266·10⁻⁸ |
| 520 | 2.7036264637736865167985 | 1.8391223526660641759283 | 0 | 889122 | 2.0856·10⁻⁷ |
| 521 | 2.7044087391114557247013 | 1.8429081260126871237805 | 0 | 886775 | 1.5124·10⁻⁷ |
| 522 | 2.7051925144965806544623 | 1.8466933385407250324939 | 130858 | 360991 | 1.1588·10⁻¹³ |
| 523 | 2.7059777899290542686935 | 1.8504779934797809777288 | 0 | 882068 | 2.0340·10⁻⁷ |
| 524 | 2.7067645654088695163383 | 1.8542620940321811104285 | 36780 | 732587 | 5.3645·10⁻¹³ |
| 525 | 2.7075528409360193326740 | 1.8580456433732620414509 | 139609 | 318906 | 3.9381·10⁻¹³ |
| 526 | 2.7083426165104966393132 | 1.8618286446516545461769 | 0 | 874973 | 3.2027·10⁻⁸ |
| 527 | 2.7091338921322943442060 | 1.8656111009895636447124 | 45005 | 692579 | 3.2842·10⁻¹³ |
| 528 | 2.7099266678014053416414 | 1.8693930154830451123281 | 0 | 870221 | 8.4682·10⁻⁸ |
| 529 | 2.7107209435178225122496 | 1.8731743912022784738305 | 0 | 867838 | 2.7749·10⁻⁸ |
| 530 | 2.7115167192815387230033 | 1.8769552311918365346257 | 0 | 865451 | 1.3753·10⁻⁷ |
| 531 | 2.7123139950925468272197 | 1.8807355384709515003220 | 0 | 863059 | 8.0696·10⁻⁸ |
| 532 | 2.7131127709508396645623 | 1.8845153160337777358229 | 0 | 860663 | 1.9057·10⁻⁷ |
| 533 | 2.7139130468564100610424 | 1.8882945668496512139814 | 0 | 858262 | 1.3383·10⁻⁷ |
| 534 | 2.7147148228092508290209 | 1.8920732938633457030282 | 161136 | 211312 | 3.3856·10⁻¹³ |
| 535 | 2.7155180988093547672099 | 1.8958514999953257411375 | 0 | 853447 | 1.8717·10⁻⁷ |
| 536 | 2.7163228748567146606745 | 1.8996291881419964456713 | 64958 | 591200 | 2.6789·10⁻¹³ |
| 537 | 2.7171291509513232808341 | 1.9034063611759502038260 | 166738 | 181661 | 3.0651·10⁻¹³ |
| 538 | 2.7179369270931733854642 | 1.9071830219462102906121 | 0 | 846190 | 1.7538·10⁻⁸ |
| 539 | 2.7187462032822577186981 | 1.9109591732784714593166 | 70036 | 563618 | 3.4545·10⁻¹³ |
| 540 | 2.7195569795185690110283 | 1.9147348179753375488299 | 0 | 841330 | 7.1359·10⁻⁸ |
| 541 | 2.7203692558020999793079 | 1.9185099588165561514707 | 0 | 838893 | 1.5008·10⁻⁸ |
| 542 | 2.7211830321328433267524 | 1.9222845985592503842035 | 0 | 836452 | 1.2537·10⁻⁷ |
| 543 | 2.7219983085107917429410 | 1.9260587399381478054224 | 0 | 834006 | 6.9120·10⁻⁸ |
| 544 | 2.7228150849359379038182 | 1.9298323856658065187646 | 0 | 831556 | 1.7958·10⁻⁷ |
| 545 | 2.7236333614082744716950 | 1.9336055384328385047243 | 0 | 829101 | 1.2342·10⁻⁷ |
| 546 | 2.7244531379277940952507 | 1.9373782009081302201528 | 178828 | 111329 | 2.1486·10⁻¹³ |
| 547 | 2.7252744144944894095343 | 1.9411503757390605050632 | 0 | 824178 | 1.7792·10⁻⁷ |
| 548 | 2.7260971911083530359653 | 1.9449220655517158355026 | 80555 | 499489 | 3.5087·10⁻¹³ |
| 549 | 2.7269214677693775823361 | 1.9486932729511029606084 | 181287 | 94088 | 8.3430·10⁻¹⁴ |
| 550 | 2.7277472444775556428123 | 1.9524640005213589613356 | 0 | 816759 | 1.0037·10⁻⁸ |
| 551 | 2.7285745212328797979348 | 1.9562342508259587677215 | 82491 | 484313 | 3.5727·10⁻¹³ |
| 552 | 2.7294032980353426146210 | 1.9600040264079201709449 | 0 | 811791 | 6.5021·10⁻⁸ |
| 553 | 2.7302335748849366461657 | 1.9637733297900063658417 | 0 | 809300 | 9.2526·10⁻⁹ |
| 554 | 2.7310653517816544322430 | 1.9675421634749260589518 | 0 | 806805 | 1.2019·10⁻⁷ |
| 555 | 2.7318986287254884989070 | 1.9713105299455311765980 | 0 | 804305 | 6.4526·10⁻⁸ |
| 556 | 2.7327334057164313585937 | 1.9750784316650122069331 | 0 | 801801 | 1.7556·10⁻⁷ |
| 557 | 2.7335696827544755101215 | 1.9788458710770912093378 | 0 | 799292 | 1.1999·10⁻⁷ |
| 558 | 2.7344074598396134386933 | 1.9826128506062125240090 | 183958 | 60946 | 4.8110·10⁻¹³ |
| 559 | 2.7352467369718376158967 | 1.9863793726577312140444 | 0 | 794261 | 1.7565·10⁻⁷ |
| 560 | 2.7360875141511404997063 | 1.9901454396180992718051 | 83593 | 457366 | 3.6346·10⁻¹³ |
| 561 | 2.7369297913775145344841 | 1.9939110538550496208251 | 183280 | 56091 | 3.9018·10⁻¹³ |
| 562 | 2.7377735686509521509808 | 1.9976762177177779440326 | 0 | 786680 | 9.5114·10⁻⁹ |
| 563 | 2.7386188459714457663374 | 2.0014409335371223685488 | 82393 | 454572 | 4.2683·10⁻¹³ |
| 564 | 2.7394656233389877840857 | 2.0052052036257410368505 | 0 | 781604 | 6.5656·10⁻⁸ |
| 565 | 2.7403139007535705941501 | 2.0089690302782875935984 | 0 | 779059 | 1.0468·10⁻⁸ |
| 566 | 2.7411636782151865728482 | 2.0127324157715846169690 | 0 | 776510 | 1.2199·10⁻⁷ |
| 567 | 2.7420149557238280828920 | 2.0164953623647950228663 | 0 | 773956 | 6.6903·10⁻⁸ |
| 568 | 2.7428677332794874733892 | 2.0202578722995914699368 | 0 | 771398 | 1.7852·10⁻⁷ |
| 569 | 2.7437220108821570798442 | 2.0240199478003237928697 | 0 | 768835 | 1.2353·10⁻⁷ |
| 570 | 2.7445777885318292241591 | 2.0277815910741844910260 | 176548 | 60075 | 4.7985·10⁻¹³ |
| 571 | 2.7454350662284962146346 | 2.0315428043113722990149 | 0 | 763696 | 1.8035·10⁻⁷ |
| 572 | 2.7462938439721503459714 | 2.0353035896852538654130 | 74095 | 464739 | 1.5674·10⁻¹³ |
| 573 | 2.7471541217627838992710 | 2.0390639493525235654126 | 172739 | 67582 | 4.9875·10⁻¹³ |
| 574 | 2.7480158996003891420366 | 2.0428238854533614727757 | 0 | 755953 | 1.5947·10⁻⁸ |
| 575 | 2.7488791774849583281745 | 2.0465834001115895160768 | 69765 | 474303 | 3.3461·10⁻¹³ |
| 576 | 2.7497439554164836979947 | 2.0503424954348258438234 | 0 | 750769 | 7.3251·10⁻⁸ |
| 577 | 2.7506102333949574782119 | 2.0541011735146374226602 | 0 | 748170 | 1.8642·10⁻⁸ |
| 578 | 2.7514780114203718819467 | 2.0578594364266908924863 | 0 | 745567 | 1.3074·10⁻⁷ |
| 579 | 2.7523472894927191087265 | 2.0616172862309017019429 | 0 | 742959 | 7.6236·10⁻⁸ |
| 580 | 2.7532180676119913444863 | 2.0653747249715815473659 | 0 | 740347 | 1.8843·10⁻⁷ |
| 581 | 2.7540903457781807615696 | 2.0691317546775841379401 | 0 | 737730 | 1.3402·10⁻⁷ |
| 582 | 2.7549641239912795187296 | 2.0728883773624493094405 | 156622 | 108620 | 3.8252·10⁻¹³ |
| 583 | 2.7558394022512797611299 | 2.0766445950245455085988 | 0 | 732483 | 1.9200·10⁻⁷ |
| 584 | 2.7567161805581736203452 | 2.0804004096472106697992 | 52086 | 521508 | 4.1062·10⁻¹³ |
| 585 | 2.7575944589119532143627 | 2.0841558231988915054677 | 149688 | 128465 | 5.1001·10⁻¹³ |
| 586 | 2.7584742373126106475825 | 2.0879108376332812311977 | 0 | 724578 | 2.9332·10⁻⁸ |
| 587 | 2.7593555157601380108189 | 2.0916654548894557463286 | 44631 | 543410 | 1.3447·10⁻¹³ |
| 588 | 2.7602382942545273813008 | 2.0954196768920082903806 | 0 | 719286 | 8.7792·10⁻⁸ |
| 589 | 2.7611225727957708226727 | 2.0991735055511825954372 | 0 | 716633 | 3.3762·10⁻⁸ |
| 590 | 2.7620083513838603849958 | 2.1029269427630045542613 | 0 | 713976 | 1.4644·10⁻⁷ |
| 591 | 2.7628956300187881047485 | 2.1066799904094124236312 | 0 | 711314 | 9.2512·10⁻⁸ |
| 592 | 2.7637844087005460048273 | 2.1104326503583855820884 | 0 | 708648 | 2.0529·10⁻⁷ |
| 593 | 2.7646746874291260945478 | 2.1141849244640718609973 | 0 | 705977 | 1.5145·10⁻⁷ |
| 594 | 2.7655664662045203696452 | 2.1179368145669134675349 | 124204 | 206485 | 7.8479·10⁻¹⁴ |
| 595 | 2.7664597450267208122752 | 2.1216883224937715179463 | 0 | 700622 | 2.1058·10⁻⁷ |
| 596 | 2.7673545238957193910149 | 2.1254394500580491991267 | 17589 | 627581 | 4.1194·10⁻¹³ |
| 597 | 2.7682508028115080608634 | 2.1291901990598135763223 | 114151 | 238644 | 2.4287·10⁻¹³ |
| 598 | 2.7691485817740787632427 | 2.1329405712859160644729 | 0 | 692555 | 4.9651·10⁻⁸ |
| 599 | 2.7700478607834234259983 | 2.1366905685101115804615 | 7016 | 661793 | 1.5391·10⁻¹³ |
| 600 | 2.7709486398395339634002 | 2.1404401924931763932752 | 0 | 687155 | 1.0926·10⁻⁷ |
| 601 | 2.7718509189424022761431 | 2.1441894449830246888334 | 0 | 684448 | 5.5813·10⁻⁸ |
| 602 | 2.7727546980920202513480 | 2.1479383277148238659858 | 0 | 681737 | 1.6907·10⁻⁷ |
| 603 | 2.7736599772883797625619 | 2.1516868424111085799433 | 0 | 679021 | 1.1571·10⁻⁷ |
| 604 | 2.7745667565314726697593 | 2.1554349907818935491616 | 0 | 676301 | 2.2907·10⁻⁷ |
| 605 | 2.7754750358212908193425 | 2.1591827745247851414622 | 0 | 673576 | 1.7581·10⁻⁷ |
| 606 | 2.7763848151578260441425 | 2.1629301953250917549430 | 79320 | 353566 | 2.8642·10⁻¹³ |
| 607 | 2.7772960945410701634195 | 2.1666772548559330090034 | 0 | 668113 | 2.3610·10⁻⁷ |
| 608 | 2.7782088739710149828637 | 2.1704239547783477605823 | 0 | 665374 | 1.6317·10⁻⁸ |
| 609 | 2.7791231534476522945959 | 2.1741702967414009604891 | 66154 | 398015 | 3.4561·10⁻¹³ |
| 610 | 2.7800389329709738771682 | 2.1779162823822893644881 | 0 | 659884 | 7.6893·10⁻⁸ |
| 611 | 2.7809562125409714955648 | 2.1816619133264461135849 | 0 | 657132 | 2.3919·10⁻⁸ |
| 612 | 2.7818749921576369012022 | 2.1854071911876441977533 | 0 | 654376 | 1.3766·10⁻⁷ |
| 613 | 2.7827952718209618319304 | 2.1891521175680988171334 | 0 | 651615 | 8.4783·10⁻⁸ |
| 614 | 2.7837170515309380120332 | 2.1928966940585686545300 | 0 | 648850 | 1.9862·10⁻⁷ |
| 615 | 2.7846403312875571522287 | 2.1966409222384560728389 | 0 | 646080 | 1.4583·10⁻⁷ |
| 616 | 2.7855651110908109496703 | 2.2003848036759062508344 | 132411 | 113661 | 2.0771·10⁻¹³ |
| 617 | 2.7864913909406910879472 | 2.2041283399279052705548 | 0 | 640527 | 2.0708·10⁻⁷ |
| 618 | 2.7874191708371892370847 | 2.2078715325403771693362 | 21994 | 549767 | 3.3238·10⁻¹³ |
| 619 | 2.7883484507802970535450 | 2.2116143830482799693546 | 116656 | 168331 | 3.4398·10⁻¹³ |
| 620 | 2.7892792307700061802282 | 2.2153568929757006973543 | 0 | 632163 | 4.9315·10⁻⁸ |
| 621 | 2.7902115108063082464719 | 2.2190990638359494070580 | 5721 | 606482 | 7.3903·10⁻¹⁴ |
| 622 | 2.7911452908891948680529 | 2.2228408971316522165778 | 0 | 626565 | 1.1104·10⁻⁷ |
| 623 | 2.7920805710186576471869 | 2.2265823943548433729687 | 0 | 623759 | 5.8643·10⁻⁸ |
| 624 | 2.7930173511946881725296 | 2.2303235569870563558960 | 0 | 620949 | 1.7295·10⁻⁷ |
| 625 | 2.7939556314172780191769 | 2.2340643864994140322167 | 0 | 618134 | 1.2065·10⁻⁷ |
| 626 | 2.7948954116864187486657 | 2.2378048843527178731084 | 0 | 615315 | 2.3506·10⁻⁷ |
| 627 | 2.7958366920021019089744 | 2.2415450519975362452161 | 0 | 612491 | 1.8286·10⁻⁷ |
| 628 | 2.7967794723643190345232 | 2.2452848908742917871242 | 64737 | 350714 | 5.1193·10⁻¹³ |
| 629 | 2.7977237527730616461752 | 2.2490244024133478823022 | 0 | 606830 | 2.4525·10⁻⁷ |
| 630 | 2.7986695332283212512360 | 2.2527635880350942395172 | 0 | 603992 | 2.6527·10⁻⁸ |
| 631 | 2.7996168137300893434554 | 2.2565024491500315915508 | 45880 | 417630 | 9.9760·10⁻¹⁴ |
| 632 | 2.8005655942783574030269 | 2.2602409871588555229076 | 0 | 598304 | 8.9209·10⁻⁸ |
| 633 | 2.8015158748731168965886 | 2.2639792034525394370522 | 0 | 595453 | 3.7289·10⁻⁸ |
| 634 | 2.8024676555143592772239 | 2.2677170994124166735662 | 0 | 592598 | 1.5208·10⁻⁷ |
| 635 | 2.8034209362020759844616 | 2.2714546764102617854702 | 0 | 589738 | 1.0025·10⁻⁷ |
| 636 | 2.8043757169362584442769 | 2.2751919358083709868166 | 0 | 586874 | 2.1514·10⁻⁷ |
| 637 | 2.8053319977168980690913 | 2.2789288789596417805151 | 0 | 584005 | 1.6341·10⁻⁷ |
| 638 | 2.8062897785439862577734 | 2.2826655072076517762181 | 98872 | 185643 | 1.7523·10⁻¹³ |
| 639 | 2.8072490594175143956395 | 2.2864018218867367079574 | 0 | 578254 | 2.2677·10⁻⁷ |
| 640 | 2.8082098403374738544539 | 2.2901378243220676610869 | 0 | 575371 | 8.5181·10⁻⁹ |
| 641 | 2.8091721213038559924292 | 2.2938735158297275179596 | 77437 | 262736 | 3.9082·10⁻¹³ |
| 642 | 2.8101359023166521542272 | 2.2976088977167866316331 | 0 | 569593 | 7.2155·10⁻⁸ |
| 643 | 2.8111011833758536709589 | 2.3013439712813777367731 | 0 | 566697 | 2.0712·10⁻⁸ |
| 644 | 2.8120679644814518601852 | 2.3050787378127701067992 | 0 | 563797 | 1.3598·10⁻⁷ |
| 645 | 2.8130362456334380259175 | 2.3088131985914429661909 | 0 | 560892 | 8.4636·10⁻⁸ |
| 646 | 2.8140060268318034586178 | 2.3125473548891581667549 | 0 | 557983 | 2.0000·10⁻⁷ |
| 647 | 2.8149773080765394351991 | 2.3162812079690321365307 | 0 | 555069 | 1.4875·10⁻⁷ |
| 648 | 2.8159500893676372190264 | 2.3200147590856071098951 | 124416 | 54486 | 2.1304·10⁻¹³ |
| 649 | 2.8169243707050880599165 | 2.3237480094849216473133 | 0 | 549228 | 2.1305·10⁻⁷ |
| 650 | 2.8179001520888831941386 | 2.3274809604045804530631 | 8495 | 512320 | 9.5498·10⁻¹⁴ |
| 651 | 2.8188774335190138444151 | 2.3312136130738234991547 | 100406 | 141744 | 1.3052·10⁻¹³ |
| 652 | 2.8198562149954712199215 | 2.3349459687135944635509 | 0 | 540432 | 5.9871·10⁻⁸ |
| 653 | 2.8208364965182465162869 | 2.3386780285366084906866 | 0 | 537491 | 8.9051·10⁻⁹ |
| 654 | 2.8218182780873309155948 | 2.3424097937474192821792 | 0 | 534546 | 1.2465·10⁻⁷ |
| 655 | 2.8228015597027155863831 | 2.3461412655424855255152 | 0 | 531596 | 7.3781·10⁻⁸ |
| 656 | 2.8237863413643916836444 | 2.3498724451102366683929 | 0 | 528642 | 1.8962·10⁻⁷ |
| 657 | 2.8247726230723503488270 | 2.3536033336311380463014 | 0 | 525683 | 1.3884·10⁻⁷ |
| 658 | 2.8257604048265827098347 | 2.3573339322777553708112 | 0 | 522720 | 2.5478·10⁻⁷ |
| 659 | 2.8267496866270798810273 | 2.3610642422148185859571 | 0 | 519752 | 2.0410·10⁻⁷ |
| 660 | 2.8277404684738329632213 | 2.3647942645992850999900 | 23750 | 421779 | 3.2324·10⁻¹³ |
| 661 | 2.8287327503668330436898 | 2.3685240005804023996845 | 114804 | 54586 | 3.3451·10⁻¹⁴ |
| 662 | 2.8297265323060711961633 | 2.3722534512997700542875 | 0 | 510821 | 5.2348·10⁻⁸ |
| 663 | 2.8307218142915384808298 | 2.3759826178914011161041 | 0 | 507835 | 1.8575·10⁻⁹ |
| 664 | 2.8317185963232259443352 | 2.3797115014817829246232 | 0 | 504845 | 1.1808·10⁻⁷ |
| 665 | 2.8327168784011246197839 | 2.3834401031899373209932 | 0 | 501850 | 6.7685·10⁻⁸ |
| 666 | 2.8337166605252255267388 | 2.3871684241274802795711 | 0 | 498851 | 1.8400·10⁻⁷ |
| 667 | 2.8347179426955196712218 | 2.3908964653986809631777 | 0 | 495847 | 1.3370·10⁻⁷ |
| 668 | 2.8357207249119980457142 | 2.3946242281005202086060 | 0 | 492839 | 2.5011·10⁻⁷ |
| 669 | 2.8367250071746516291573 | 2.3983517133227484488445 | 0 | 489826 | 1.9990·10⁻⁷ |
| 670 | 2.8377307894834713869519 | 2.4020789221479430783920 | 30448 | 365016 | 5.1929·10⁻¹³ |
| 671 | 2.8387380718384482709598 | 2.4058058556515652679577 | 120647 | 1198 | 1.2315·10⁻¹³ |
| 672 | 2.8397468542395732195031 | 2.4095325149020162347586 | 0 | 480760 | 4.9577·10⁻⁸ |
| 673 | 2.8407571366868371573651 | 2.4132589009606929745459 | 791 | 474565 | 4.5494·10⁻¹³ |
| 674 | 2.8417689191802309957906 | 2.4169850148820434614120 | 0 | 474694 | 1.1625·10⁻⁷ |
| 675 | 2.8427822017197456324860 | 2.4207108577136213213511 | 0 | 471654 | 6.6337·10⁻⁸ |
| 676 | 2.8437969843053719516198 | 2.4244364304961399854713 | 0 | 468610 | 1.8313·10⁻⁷ |
| 677 | 2.8448132669371008238228 | 2.4281617342635263286770 | 0 | 465561 | 1.3330·10⁻⁷ |
| 678 | 2.8458310496149231061885 | 2.4318867700429737995681 | 0 | 462508 | 2.5019·10⁻⁷ |
| 679 | 2.8468503323388296422735 | 2.4356115388549950472272 | 0 | 459450 | 2.0045·10⁻⁷ |
| 680 | 2.8478711151088112620975 | 2.4393360417134740504937 | 28604 | 341971 | 2.9777·10⁻¹⁴ |
| 681 | 2.8488933979248587821441 | 2.4430602796257177552524 | 0 | 453321 | 2.6780·10⁻⁷ |
| 682 | 2.8499171807869630053603 | 2.4467842535925072251928 | 0 | 450249 | 5.1548·10⁻⁸ |
| 683 | 2.8509424636951147211579 | 2.4505079646081483114259 | 0 | 447173 | 2.0066·10⁻⁹ |
| 684 | 2.8519692466493047054128 | 2.4542314136605218462772 | 0 | 444093 | 1.1917·10⁻⁷ |
| 685 | 2.8529975296495237204659 | 2.4579546017311333665062 | 0 | 441008 | 6.9730·10⁻⁸ |
| 686 | 2.8540273126957625151230 | 2.4616775297951623711366 | 0 | 437919 | 1.8699·10⁻⁷ |
| 687 | 2.8550585957880118246554 | 2.4654001988215111190155 | 0 | 434825 | 1.3764·10⁻⁷ |
| 688 | 2.8560913789262623708001 | 2.4691226097728529711549 | 0 | 431727 | 2.5500·10⁻⁷ |
| 689 | 2.8571256621105048617599 | 2.4728447636056802828452 | 0 | 428624 | 2.0574·10⁻⁷ |
| 690 | 2.8581614453407299922039 | 2.4765666612703518504680 | 18237 | 352568 | 2.8763·10⁻¹³ |
| 691 | 2.8591987286169284432678 | 2.4802883037111399178724 | 0 | 422405 | 2.7403·10⁻⁷ |
| 692 | 2.8602375119390908825538 | 2.4840096918662767471181 | 0 | 419288 | 5.8254·10⁻⁸ |
| 693 | 2.8612777953072079641314 | 2.4877308266680007583298 | 0 | 416167 | 9.1852·10⁻⁹ |
| 694 | 2.8623195787212703285372 | 2.4914517090426022433456 | 0 | 413042 | 1.2682·10⁻⁷ |
| 695 | 2.8633628621812686027756 | 2.4951723399104686577852 | 0 | 409912 | 7.7854·10⁻⁸ |
| 696 | 2.8644076456871934003186 | 2.4988927201861294961059 | 0 | 406778 | 1.9559·10⁻⁷ |
| 697 | 2.8654539292390353211065 | 2.5026128507783007541565 | 0 | 403639 | 1.4671·10⁻⁷ |
| 698 | 2.8665017128367849515477 | 2.5063327325899289836836 | 0 | 400496 | 2.6454·10⁻⁷ |
| 699 | 2.8675509964804328645194 | 2.5100523665182349431905 | 0 | 397348 | 2.1576·10⁻⁷ |
| 700 | 2.8686017801699696193677 | 2.5137717534547568494919 | 0 | 394195 | 3.5481·10⁻¹⁰ |
| 701 | 2.8696540639053857619077 | 2.5174908942853932342562 | 87007 | 43010 | 2.7304·10⁻¹³ |
| 702 | 2.8707078476866718244238 | 2.5212097898904454097733 | 0 | 387877 | 6.9685·10⁻⁸ |
| 703 | 2.8717631315138183256701 | 2.5249284411446595481333 | 0 | 384711 | 2.1087·10⁻⁸ |
| 704 | 2.8728199153868157708705 | 2.5286468489172683779489 | 0 | 381541 | 1.3920·10⁻⁷ |
| 705 | 2.8738781993056546517191 | 2.5323650140720325027073 | 0 | 378366 | 9.0700·10⁻⁸ |
| 706 | 2.8749379832703254463800 | 2.5360829374672813447817 | 0 | 375187 | 2.0891·10⁻⁷ |
| 707 | 2.8759992672808186194882 | 2.5398006199559537190874 | 0 | 372003 | 1.6050·10⁻⁷ |
| 708 | 2.8770620513371246221494 | 2.5435180623856380403180 | 0 | 368815 | 2.7880·10⁻⁷ |
| 709 | 2.8781263354392338919401 | 2.5472352655986121676465 | 0 | 365622 | 2.3049·10⁻⁷ |
| 710 | 2.8791921195871368529084 | 2.5509522304318828907320 | 0 | 362424 | 1.5558·10⁻⁸ |
| 711 | 2.8802594037808239155735 | 2.5546689577172250608244 | 58793 | 124050 | 3.0422·10⁻¹³ |
| 712 | 2.8813281880202854769267 | 2.5583854482812203707128 | 0 | 356016 | 8.5830·10⁻⁸ |
| 713 | 2.8823984723055119204308 | 2.5621017029452957872198 | 0 | 352805 | 3.7704·10⁻⁸ |
| 714 | 2.8834702566364936160210 | 2.5658177225257616398961 | 0 | 349590 | 1.5629·10⁻⁷ |
| 715 | 2.8845435410132209201048 | 2.5695335078338493695286 | 0 | 346370 | 1.0825·10⁻⁷ |
| 716 | 2.8856183254356841755623 | 2.5732490596757489400304 | 0 | 343146 | 2.2694·10⁻⁷ |
| 717 | 2.8866946099038737117462 | 2.5769643788526459172355 | 0 | 339917 | 1.7900·10⁻⁷ |
| 718 | 2.8877723944177798444825 | 2.5806794661607582180850 | 64001 | 80679 | 1.1582·10⁻¹³ |
| 719 | 2.8888516789773928760701 | 2.5843943223913725336411 | 0 | 333446 | 2.4993·10⁻⁷ |
| 720 | 2.8899324635827030952815 | 2.5881089483308804293320 | 0 | 330203 | 3.5468·10⁻⁸ |
| 721 | 2.8910147482337007773627 | 2.5918233447608141257845 | 22107 | 238528 | 2.7597·10⁻¹³ |
| 722 | 2.8920985329303761840337 | 2.5955375124578819635640 | 0 | 323705 | 1.0668·10⁻⁷ |
| 723 | 2.8931838176727195634883 | 2.5992514521940035550999 | 0 | 320449 | 5.9025·10⁻⁸ |
| 724 | 2.8942706024607211503947 | 2.6029651647363446270371 | 0 | 317189 | 1.7808·10⁻⁷ |
| 725 | 2.8953588872943711658952 | 2.6066786508473515562141 | 0 | 313924 | 1.3051·10⁻⁷ |
| 726 | 2.8964486721736598176072 | 2.6103919112847856024319 | 0 | 310655 | 2.4967·10⁻⁷ |
| 727 | 2.8975399570985772996226 | 2.6141049468017568411380 | 0 | 307381 | 2.0220·10⁻⁷ |
| 728 | 2.8986327420691137925081 | 2.6178177581467577991157 | 21395 | 218522 | 7.3723·10⁻¹⁴ |
| 729 | 2.8997270270852594633061 | 2.6215303460636967962293 | 0 | 300820 | 2.7407·10⁻⁷ |
| 730 | 2.9008228121470044655340 | 2.6252427112919309962419 | 0 | 297532 | 6.0077·10⁻⁸ |
| 731 | 2.9019200972543389391848 | 2.6289548545662991696862 | 0 | 294240 | 1.2796·10⁻⁸ |
| 732 | 2.9030188824072530107273 | 2.6326667766171541717338 | 0 | 290944 | 1.3222·10⁻⁷ |
| 733 | 2.9041191676057367931063 | 2.6363784781703951379730 | 0 | 287643 | 8.5041·10⁻⁸ |
| 734 | 2.9052209528497803857426 | 2.6400899599474994009721 | 0 | 284338 | 2.0456·10⁻⁷ |
| 735 | 2.9063242381393738745332 | 2.6438012226655541304712 | 0 | 281028 | 1.5747·10⁻⁷ |
| 736 | 2.9074290234745073318519 | 2.6475122670372877000113 | 0 | 277714 | 2.7709·10⁻⁷ |
| 737 | 2.9085353088551708165488 | 2.6512230937711007827779 | 0 | 274395 | 2.3009·10⁻⁷ |
| 738 | 2.9096430942813543739509 | 2.6549337035710971794036 | 0 | 271071 | 1.6473·10⁻⁸ |
| 739 | 2.9107523797530480358623 | 2.6586440971371143804411 | 54779 | 48627 | 3.7310·10⁻¹³ |
| 740 | 2.9118631652702418205642 | 2.6623542751647538661882 | 0 | 264411 | 8.9374·10⁻⁸ |
| 741 | 2.9129754508329257328150 | 2.6660642383454111465139 | 0 | 261074 | 4.2561·10⁻⁸ |
| 742 | 2.9140892364410897638507 | 2.6697739873663055433054 | 0 | 257733 | 1.6246·10⁻⁷ |
| 743 | 2.9152045220947238913851 | 2.6734835229105097181225 | 0 | 254387 | 1.1574·10⁻⁷ |
| 744 | 2.9163213077938180796096 | 2.6771928456569789476211 | 0 | 251037 | 2.3573·10⁻⁷ |
| 745 | 2.9174395935383622791937 | 2.6809019562805801492718 | 0 | 247682 | 1.8911·10⁻⁷ |
| 746 | 2.9185593793283464272851 | 2.6846108554521206598755 | 43442 | 70554 | 3.0778·10⁻¹⁴ |
| 747 | 2.9196806651637604475095 | 2.6883195438383767693470 | 0 | 240959 | 2.6266·10⁻⁷ |
| 748 | 2.9208034510445942499716 | 2.6920280221021220122087 | 0 | 237590 | 4.9514·10⁻⁸ |
| 749 | 2.9219277369708377312542 | 2.6957362909021552192092 | 0 | 234217 | 3.0752·10⁻⁹ |
| 750 | 2.9230535229424807744193 | 2.6994443508933283314547 | 0 | 230840 | 1.2334·10⁻⁷ |
| 751 | 2.9241808089595132490075 | 2.7031522027265739794125 | 0 | 227458 | 7.7004·10⁻⁸ |
| 752 | 2.9253095950219250110388 | 2.7068598470489328291192 | 0 | 224072 | 1.9737·10⁻⁷ |
| 753 | 2.9264398811297059030121 | 2.7105672845035806979002 | 0 | 220681 | 1.5111·10⁻⁷ |
| 754 | 2.9275716672828457539060 | 2.7142745157298554418805 | 0 | 217286 | 2.7158·10⁻⁷ |
| 755 | 2.9287049534813343791785 | 2.7179815413632836175407 | 0 | 213886 | 2.2542·10⁻⁷ |
| 756 | 2.9298397397251615807672 | 2.7216883620356069195467 | 0 | 210481 | 1.2642·10⁻⁸ |
| 757 | 2.9309760260143171470897 | 2.7253949783748083970564 | 0 | 207073 | 2.9991·10⁻⁷ |
| 758 | 2.9321138123487908530434 | 2.7291013910051384506816 | 0 | 203659 | 8.7224·10⁻⁸ |
| 759 | 2.9332530987285724600061 | 2.7328076005471406122592 | 0 | 200241 | 4.1252·10⁻⁸ |
| 760 | 2.9343938851536517158356 | 2.7365136076176771095596 | 0 | 196819 | 1.6199·10⁻⁷ |
| 761 | 2.9355361716240183548701 | 2.7402194128299542180403 | 0 | 193392 | 1.1611·10⁻⁷ |
| 762 | 2.9366799581396620979286 | 2.7439250167935474017237 | 0 | 189961 | 2.3694·10⁻⁷ |
| 763 | 2.9378252447005726523104 | 2.7476304201144262452585 | 0 | 186525 | 1.9116·10⁻⁷ |
| 764 | 2.9389720313067397117959 | 2.7513356233949791792010 | 38242 | 30116 | 4.3220·10⁻¹³ |
| 765 | 2.9401203179581529566465 | 2.7550406272340380005266 | 0 | 179640 | 2.6639·10⁻⁷ |
| 766 | 2.9412701046548020536043 | 2.7587454322269021903629 | 0 | 176190 | 5.4081·10⁻⁸ |
| 767 | 2.9424213913966766558931 | 2.7624500389653630309118 | 0 | 172736 | 8.4817·10⁻⁹ |
| 768 | 2.9435741781837664032178 | 2.7661544480377275235060 | 0 | 169278 | 1.2959·10⁻⁷ |
| 769 | 2.9447284650160609217647 | 2.7698586600288421097245 | 0 | 165815 | 8.4087·10⁻⁸ |
| 770 | 2.9458842518935498242018 | 2.7735626755201161974692 | 0 | 162348 | 2.0529·10⁻⁷ |
| 771 | 2.9470415388162227096790 | 2.7772664950895454938847 | 0 | 158876 | 1.5987·10⁻⁷ |
| 772 | 2.9482003257840691638278 | 2.7809701193117351469816 | 0 | 155400 | 2.8117·10⁻⁷ |
| 773 | 2.9493606127970787587619 | 2.7846735487579226978041 | 0 | 151919 | 2.3585·10⁻⁷ |
| 774 | 2.9505223998552410530770 | 2.7883767839960008449607 | 0 | 148433 | 2.3916·10⁻⁸ |
| 775 | 2.9516856869585455918511 | 2.7920798255905400233182 | 0 | 144944 | 3.1202·10⁻⁷ |
| 776 | 2.9528504741069819066444 | 2.7957826741028107986395 | 0 | 141449 | 1.0017·10⁻⁷ |
| 777 | 2.9540167613005395155000 | 2.7994853300908060799239 | 0 | 137950 | 5.5037·10⁻⁸ |
| 778 | 2.9551845485392079229430 | 2.8031877941092631511928 | 0 | 134447 | 1.7661·10⁻⁷ |
| 779 | 2.9563538358229766199818 | 2.8068900667096855244408 | 0 | 130939 | 1.3157·10⁻⁷ |
| 780 | 2.9575246231518350841073 | 2.8105921484403646154562 | 0 | 127427 | 2.5324·10⁻⁷ |
| 781 | 2.9586969105257727792935 | 2.8142940398464012441954 | 0 | 123910 | 2.0829·10⁻⁷ |
| 782 | 2.9598706979447791559974 | 2.8179957414697269613761 | 5900 | 96788 | 9.6832·10⁻¹⁴ |
| 783 | 2.9610459854088436511592 | 2.8216972538491252029386 | 0 | 116863 | 2.8519·10⁻⁷ |
| 784 | 2.9622227729179556882025 | 2.8253985775202522740029 | 0 | 113332 | 7.3720·10⁻⁸ |
| 785 | 2.9634010604721046770342 | 2.8290997130156581639362 | 0 | 109797 | 2.8956·10⁻⁸ |
| 786 | 2.9645808480712800140449 | 2.8328006608648071941231 | 0 | 106258 | 1.5090·10⁻⁷ |
| 787 | 2.9657621357154710821086 | 2.8365014215940985000172 | 0 | 102714 | 1.0623·10⁻⁷ |
| 788 | 2.9669449234046672505832 | 2.8402019957268863490338 | 0 | 99166 | 2.2827·10⁻⁷ |
| 789 | 2.9681292111388578753105 | 2.8439023837835002958272 | 0 | 95613 | 1.8369·10⁻⁷ |
| 790 | 2.9693149989180322986162 | 2.8476025862812651764784 | 0 | 92056 | 3.0582·10⁻⁷ |
| 791 | 2.9705022867421798493102 | 2.8513026037345209431052 | 0 | 88494 | 2.6134·10⁻⁷ |
| 792 | 2.9716910746112898426863 | 2.8550024366546423403867 | 0 | 84927 | 5.0234·10⁻⁸ |
| 793 | 2.9728813625253515805228 | 2.8587020855500584254810 | 0 | 81356 | 5.8398·10⁻⁹ |
| 794 | 2.9740731504843543510825 | 2.8624015509262719327982 | 0 | 77781 | 1.2815·10⁻⁷ |
| 795 | 2.9752664384882874291124 | 2.8661008332858784850748 | 0 | 74201 | 8.3856·10⁻⁸ |
| 796 | 2.9764612265371400758444 | 2.8697999331285856521795 | 0 | 70617 | 2.0626·10⁻⁷ |
| 797 | 2.9776575146309015389950 | 2.8734988509512318590680 | 0 | 67028 | 1.6205·10⁻⁷ |
| 798 | 2.9788553027695610527653 | 2.8771975872478051442848 | 0 | 63435 | 2.8456·10⁻⁷ |
| 799 | 2.9800545909531078378416 | 2.8808961425094617703991 | 0 | 59837 | 2.4044·10⁻⁷ |
| 800 | 2.9812553791815311013950 | 2.8845945172245446877447 | 0 | 56234 | 2.9706·10⁻⁸ |
| 801 | 2.9824576674548200370820 | 2.8882927118786018528209 | 0 | 52628 | 3.1901·10⁻⁷ |
| 802 | 2.9836614557729638250438 | 2.8919907269544044026946 | 0 | 49016 | 1.0837·10⁻⁷ |
| 803 | 2.9848667441359516319073 | 2.8956885629319646867331 | 0 | 45400 | 6.4437·10⁻⁸ |
| 804 | 2.9860735325437726107847 | 2.8993862202885541569792 | 0 | 41780 | 1.8721·10⁻⁷ |
| 805 | 2.9872818209964159012736 | 2.9030836994987211184699 | 0 | 38155 | 1.4337·10⁻⁷ |
| 806 | 2.9884916094938706294574 | 2.9067810010343083407827 | 0 | 34526 | 2.6625·10⁻⁷ |
| 807 | 2.9897028980361259079047 | 2.9104781253644705320834 | 0 | 30892 | 2.2250·10⁻⁷ |
| 808 | 2.9909156866231708356705 | 2.9141750729556916769334 | 0 | 27253 | 1.2133·10⁻⁸ |
| 809 | 2.9921299752549944982951 | 2.9178718442718022391024 | 0 | 23611 | 3.0181·10⁻⁷ |
| 810 | 2.9933457639315859678052 | 2.9215684397739962306192 | 0 | 19963 | 9.1534·10⁻⁸ |
| 811 | 2.9945630526529343027132 | 2.9252648599208481482799 | 0 | 16311 | 4.7971·10⁻⁸ |
| 812 | 2.9957818414190285480177 | 2.9289611051683297788204 | 0 | 12655 | 1.7111·10⁻⁷ |
| 813 | 2.9970021302298577352037 | 2.9326571759698268739484 | 0 | 8994 | 1.2764·10⁻⁷ |
| 814 | 2.9982239190854108822423 | 2.9363530727761556964151 | 0 | 5329 | 2.5088·10⁻⁷ |
| 815 | 2.9994472079856769935911 | 2.9400487960355794382972 | 0 | 1659 | 2.0750·10⁻⁷ |

*Used in* [[lem:is-z3]], [[lem:is-gap-z]], [[thm:is-gap]], [[prop:is-count]] and [[cor:is-flat]].

### Tables for the exceptional sets {#sec:tab-t49}
```

## 6. Other sites that quote the old gap or count

None needs a text from this file; listed so that nothing is missed.

- 71:1491, thm:loss-d: "(G) asks ε_K < μ_G ([[thm:is-gap]])". Still true (Λ ⊃ Λ_ℬ, μ_Z < μ_G); it may read μ_Z
  (P-UB2 §1.3 item 5 leaves it).
- 71:1815, rem:ec-lb-unbounded: the bound 1.2497·10²⁴ "rests on (G) … ([[lem:uc-two-offsets]], [[thm:is-gap]])". True;
  P-UB2's M4 rewrites the line.
- 71:2208–2224, rem:ec-upper-point and rem:ec-upper-open: μ_G and 1.62066·10¹³ < N_Λ < 1.67472·10¹³. P-UB2's M5, M6.
- 71:2256, sec:uc-close: "(G) holds exactly for ε_K < μ_G". P-UB2's M7.
- 71:2559–2563, thm:uc-reduction (iii): μ_G and N_Λ. P-UB2's M8.
- 71:2662–2680, lem:uc-lambda: N_Λ and "the elements … are real". P-UB2's M9, with N̄_Λ := 909,507,124,095,312.
- 71:4396, lem:cs-fourier (b): "Λ ∩ {Re ≤ 3 + ε_+} is real ([[prop:is-lambda]])". P-UB2's M15a; prop:is-lambda (T7)
  gives what it cites.
- 71:2368–2403, cor:uc-two-offsets and rem:uc-offset-d0: admissible ε_K below 1.6417·10⁻¹⁴. True, and weaker than
  thm:is-gap.
- proofs/P-TR.md transfers the upper bound to h ∈ [4.76·10⁻¹¹, 10⁻⁶) with N_Λ and μ_G unchanged in h. That fails for
  the repaired Λ: Z₃, μ_Z and N_Λ move with h (section 2.2).
- PAPER.md, STATUS.md:53, 88 and INTEGRATION.md:1360 quote the old bound: regenerate, resp. record.

## 7. Crosswalk

New rows, in the four tab-separated columns, the source pinned as "paper/reader/proofs/P-UB1.md@PENDING:N", N the
line of this file that carries the label. Each row goes after the row of the label named, which keeps each file in
chapter order.

| new label | crosswalk file | goes after the row of |
|---|---|---|
| sec:is-z | crosswalk/71-explicit-constants.tsv | prop:is-ci-pp |
| eq:is-c-int | crosswalk/71-explicit-constants.tsv | sec:is-z |
| lem:is-disc | crosswalk/71-explicit-constants.tsv | eq:is-c-int |
| lem:is-z3 | crosswalk/71-explicit-constants.tsv | lem:is-disc |
| lem:is-gap-z | crosswalk/71-explicit-constants.tsv | lem:is-reduction |
| eq:is-mu-z | crosswalk/71-explicit-constants.tsv | lem:is-gap-z |
| cor:is-lower | crosswalk/71-explicit-constants.tsv | thm:is-gap |
| sec:tab-is | crosswalk/96-tables.tsv | sec:tab-a-vector |
| sec:tab-is-real | crosswalk/96-tables.tsv | sec:tab-is |
| sec:tab-is-complex | crosswalk/96-tables.tsv | sec:tab-is-real |

```text
sec:is-z	paper/reader/proofs/P-UB1.md@PENDING:339	P-UB1, subsection: The elements of Z of real part below 3	new; the roots 1 + 𝒵 of the repaired def:iii-i10-1-1 at the computational point
eq:is-c-int	paper/reader/proofs/P-UB1.md@PENDING:349	P-UB1, display: the cubic C with integer coefficients	new; 102400·10¹²C at (v, e, h) = (1/2, 1/102400, 10⁻⁶)
lem:is-disc	paper/reader/proofs/P-UB1.md@PENDING:351	P-UB1, Lemma (A simple root in a disc.)	new; Rouché against the linear Taylor polynomial, with a sufficient condition by real and imaginary parts
lem:is-z3	paper/reader/proofs/P-UB1.md@PENDING:361	P-UB1, Lemma (The elements of Z of real part below 3.)	new; 2629 elements, enclosed to 10⁻²¹ by the tables of sec:tab-is; count from prop:np-10-54, lem:s14-sextic-large, cor:t49-right, lem:s14-vector-distance
lem:is-gap-z	paper/reader/proofs/P-UB1.md@PENDING:492	P-UB1, Lemma (The least excesses of Z₃.)	new; replaces V-I11 §5.4 (same label); ι_* enclosed to 10⁻²⁴; μ_Z ∈ (1.6747856, 1.6747859)·10⁻¹⁷; every other excess ≥ 1.1076·10⁻¹⁵
eq:is-mu-z	paper/reader/proofs/P-UB1.md@PENDING:496	P-UB1, display: μ_Z and its bounds	new
cor:is-lower	paper/reader/proofs/P-UB1.md@PENDING:584	P-UB1, Corollary (The loss for the index sets as constructed.)	new, optional; prop:ec-rounds at ε_K < μ_Z: 3R > 1.2250·10²⁷
sec:tab-is	paper/reader/proofs/P-UB1.md@PENDING:797	P-UB1, tables section: the roots of the damping polynomials below the real part 3	new; checks stated per row
sec:tab-is-real	paper/reader/proofs/P-UB1.md@PENDING:822	P-UB1, table: the 1269 real roots	new; sign changes at r, r + 10⁻²¹; least excess (p, q, m)
sec:tab-is-complex	paper/reader/proofs/P-UB1.md@PENDING:2101	P-UB1, table: the 680 non-real roots of positive imaginary part	new; lem:is-disc at a + ib, radius 10⁻²¹; least excess (p, q, m)
```

Notes to append to the existing rows of crosswalk/71-explicit-constants.tsv (fourth column, after a "; "):

- rem:gap-sums: P-UB1 T1: last sentence: (G) exactly for ε_K < μ_Z ≈ 1.6748·10⁻¹⁷ for the repaired Λ; μ_G for the part
  without 1 + 𝒵.
- sec:is: P-UB1 T2: opening paragraph rewritten for the repaired Λ (Z₃, μ_Z, N_Λ, cor:is-lower, conditional cor:is-flat).
- eq:is-mu: P-UB1 T2: kept; now the least excess of the part Λ_ℬ.
- def:uc-choice: P-UB1 T3: ε_K = 1.6747·10⁻¹⁷, ε_+ = 1.67478·10⁻¹⁷ (repaired Λ).
- eq:uc-deltas: P-UB1 T4: Δβ_0 = 1.6713522747·10⁻¹⁷.
- lem:uc-admissible: P-UB1 T5, T6: (G), (G⁺) by thm:is-gap with μ_Z; ε′_0 = 4·10⁻²².
- sec:is-lambda: P-UB1 T7: heading kept, after the new sec:is-z.
- prop:is-lambda: P-UB1 T7: Λ_ℬ and the families ι + p𝔡₀ + q𝔡₁, ι ∈ Z₃; non-real elements have real part > 2.514;
  replaces V-I11 §5.2.
- thm:is-gap: P-UB1 T8, T9: (G) ⟺ ε_K < μ_Z, (G⁺) ⟺ ε_+ < μ_Z; the old table is the part Λ_ℬ; replaces V-I11 §5.3.
- prop:is-count: P-UB1 T10, T11: (a) 1.85753·10¹⁴ < N_Λ ≤ 909,507,124,095,312; (b), (c) unchanged.
- cor:is-flat: P-UB1 T12: under c_b = 0 for the repaired Λ: μ♭_Z ∈ (3.548125563, 3.548125564)·10⁻¹⁰, N_Λ ≤ 3,683,190,611.
- rem:is-summary: P-UB1 T13: the roots of Z below 3 enter Λ; μ_Z; c_b decides ε_K up to ε_Υ.

## 8. Checks run

All scratch work is in the session scratchpad, directory pub1 (scripts and outputs); nothing of it is cited by the texts.

- **The polynomials.** The table 64·10¹⁸P_l = Σ π_k(κ)ι^k of sec:tab-a-sextic equals 64·10¹⁸ det(hN_l(ι)) of eq:s14-nl at
  (v, e, h) = (1/2, 1/102400, 10⁻⁶) identically in κ, and P_0 + (ι − 2)C = 0 with 102400·10¹²C the cubic eq:is-c-int
  (symbolic expansion).
- **The roots.** All roots of C and of P_l, l ≤ 1100, at 80 digits: 3301 of real part above 19/10; 2629 in (2, 3),
  1269 real and 1360 non-real, all at l ≤ 999, as V-I11 and R-V-I11 found; the least real part above 3 is 3.000672 at
  l = 816 (besides the vector roots, the least 3 + 4.99998·10⁻⁶ at l = 2).
- **The enclosures, exactly.** Every row of both tables was certified in integer and Gaussian-rational arithmetic: the
  1269 sign changes of 10¹²⁶𝒫_l (10⁶³𝒫_0) at r, r + 10⁻²¹; for the 680 discs the inequality of lem:is-disc with
  M = 7·10²¹ (the largest majorant Σ k(k − 1)|π_k|6^(k−2) over l ≤ 815 is 6.826·10²¹), the ratio of its two sides
  being at most 0.097; and |a| + |b| + 10⁻²¹ < 6. ι_* was enclosed to 10⁻²⁴ by the same sign test.
- **The least excesses, exactly.** For each row the reduction of lem:is-reduction was run on the interval for y with
  the bounds of lem:is-offsets (b) (and ε₀ checked against them): n⁺, n⁻ and every p_n are determined in every row,
  n⁺ − n⁻ ≤ 2, the minimiser is unique with a margin in every row (its upper bound below the others' lower bounds). The
  least is 1.6747722570·10⁻¹⁷ (lower bound, row l = 390), the next 1.1076143078·10⁻¹⁵ (l = 23), then 1.3074·10⁻¹⁵
  (l = 417); 56 elements lie in (3, 3 + 1.6416·10⁻¹⁴] and 1144 in (3, 3 + 4.2·10⁻¹³], R-V-I11's figures.
- **An independent re-check from the printed tables.** A second routine parsed the two tables as they stand in the
  merged chapter 96 and redid every per-row check from the printed numbers only (sign changes, disc inequality, the
  reduction with the printed (p, q) and m), the row pattern of lem:is-z3 (c), the column b increasing by more than
  2·10⁻²¹, the sums S₁ < 1207.93630800, S₂ < 793.55925810 and Σ_(non-real) y² > 150.70791670, the least r, the largest
  r + 10⁻²¹ and a + 10⁻²¹, the least a, the one-offset excesses of cor:is-flat and the sums 3,623,813,354 and
  1,227,124,256 of n⁺ + 1. All pass.
- **Every other number in the texts** (the majorant bounds for π₂, π₃, π₄ and 𝒫_l″, the vector root, a(x) − 3 at
  l = 816, the bounds for ι_B and ι_P beyond, μ_Z from the printed bounds, N_Λ < 909,507,124,095,312.22, N_Λ >
  1.85753·10¹⁴, the numbers of cor:is-lower, Δβ_0 = 1.6713522747·10⁻¹⁷ exactly, ε′_0 = 4·10⁻²², μ♭_Z) was rechecked in
  exact rational arithmetic.
- **Placement.** Every old text occurs exactly once in its file as whole lines; the fourteen blocks are disjoint. All
  were applied to a scratch copy of chapters/: lint.py --chapters 0 hits (4675 labels, ten new); assemble.py in that
  scratch tree 0 problems; lint.py --paper on the scratch PAPER.md 0 hits, no line over 121 characters after the
  labels resolve. No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|"; labels are lowercase. assemble.py
  was not run in the real directory.
- **Step 4 numbers** (section 2.2) are a 60-digit numerical scan at nine values of h, used by no text.
