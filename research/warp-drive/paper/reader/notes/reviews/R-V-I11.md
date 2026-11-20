# R-V-I11: adversarial check of V-I11 (lem:iii-i11-2-1 and the roots that come from □^C)

Read at HEAD c442093b (the commit that added notes/reports/V-I11.md). Line numbers are those of that commit. I read the
report in full and formed the judgments below from the chapters: 33 (sec:iv4-0, prop:np-10-12, prop:np-10-54,
sec:s14-every-h-two, prop:s14-scalar-every-h), 34 (sec:iii-f1-1, sec:iii-f1-2, lem:iii-f1-2-1, prop:iii-f1-2-3 and its
proof, prop:iii-f4-5-1), 36 (prop:iii-g4-4-4 and eq:iii-g4-4-2), 37 (prop:iii-h-3-2), 40 (sec:iii-i9-1), 41 (whole of
sec:iii-i10-1 to sec:iii-i12-3), 42 (thm:iii-i14-3-1, def:iii-j-g-plus), 71 (sec:ec-point, rem:gap-sums,
lem:ec-lb-ind, rem:ec-lb-unbounded, rem:ec-upper-point/-open, sec:uc-close to sec:is-summary, sec:cs, sec:uc-data-order)
and 96 (sec:tab-a). Nothing under method/, drive/, extracted/ or recovered/ was read. No chapter, crosswalk or proof file
was edited; nothing was committed.

## Verdicts

| claim | verdict | in one line |
|---|---|---|
| (1) the ι^C_(·,+) − 1 are indicial roots of L̂_b(0) in (1, 3), several in (1, 2), met at level 0, generically nonzero | **CONFIRMED** | prop:iii-f1-2-3 lists them; every location re-derived exactly; no exclusion anywhere in the paper; the paper itself uses them elsewhere |
| (2) E′ and the "Λ-valued" claim are wrong; thm:iii-i12-3-1 fails as stated; thm:iii-i11-4-1 has a proof gap | **CONFIRMED** (one part PARTLY) | the counterexample survives every check; it can be strengthened to every admissible h; "every result with ℰ_♯ or Λ_* inherits" is right as a proof dependency, shown false as a statement only for some |
| (3) adding 1 + 𝒵 to the generators of Λ makes ch. 41–44 hold by their existing proofs | **CONFIRMED in substance, PARTLY as to "by their existing proofs"** | the generator is the right one and in a sense forced; at every site where the new exponents land the existing arguments go through; not every site of 42–44 was re-read |
| (4) after the fix (G), (G⁺) fail at def:uc-choice; the upper bound and its chain fall; the lower bounds stand | **CONFIRMED** | exact sign change and exact excess bounds reproduced; 56 elements of the repaired Λ lie in (3, 3 + ε_K]; no admissible choice in ch. 71's framework restores 1.57157·10⁵⁰; re-evaluated the bound is of order 10⁵⁶ |

## 1. Are the □^C roots indicial roots of L̂_b(0) in the window? (claim (1))

**What the paper says.** L̂_b(0) = L_0 = L_b^(0) (sec:iii-i11-1). lem:iii-f1-2-1 factors det N_L(ι) as
(ι + l)(ι − l − 2) det N_Υ(ι − 1) det N_C(ι + 1)/D(ι), with D = (ι − 1)² at s0, s1, ι(ι − 2) at v1 and 1 at sl, vl
(l ≥ 2). So at every type the roots of L_b^(0) include the roots of □^C minus 1, and D removes only the root 2 of □^C at
s0 and s1 (giving 1) and the root 3 at v1 (giving 2). prop:iii-f1-2-3 prints these roots in its list after the
semicolons: ι^C_(s0,+) − 1 at s0, ι^C_(s1,+,1) − 1 and ι^C_(s1,+,2) − 1 at s1, ι^C_(sl,+,j) − 1 at sl (l ≥ 2),
ι^C_(vl,+) − 1 at vl (l ≥ 2). Its proof (Bounds) says they have real part above 1. lem:iii-i11-2-1 quotes "the indicial
roots of L̂_b(0) (prop:iii-f1-2-3)", and its proof's list (41:586–588) gives the left-hand entries only. So the lemma's
own definition of E′ includes these roots, and the sentence "Below the real part 3 the only such root is 2" is false
exactly when some ι^C_(·,+) has real part in (2, 4).

**Where they lie (re-derived, exactly).** I multiplied out det(hN_l(ι)) of eq:s14-nl symbolically (sympy) and checked it
against sec:tab-a's π_k (identical), against eq:s14-f-two (identical) and P_0 = −(ι − 2)C with eq:s14-c0 (identical).
At (v, e) = (1/2, 1/102400) and every 0 < h ≤ 10⁻⁶:

- C(2) = 3(h + 2h² + 5e + 2eh) > 0 and C(3) = −2 + 20e − 6h + 12eh < 0, and C has exactly one root above 2 (proof of
  prop:np-10-54); so ι^C_(s0,+) ∈ (2, 3): a type-s0 root of L̂_b(0) in (1, 2) (≈ 1.0000747 at h = 10⁻⁶).
- P_1(3) = −9e + (4 − 10e)h + 15h² < 0, P_1(5/2) = 1/4 − 71e/8 + … > 0, P̃_1(2) = f₁ < 0: roots of P̃_1 in (2, 5/2) and
  (5/2, 3), the two ι^C_(s1,+,j) (≈ 2.0001202 and 2.9999580 at h = 10⁻⁶).
- lem:ec-lb-ind: ι₂(h) ∈ (2 + (40/13)h(1 − 5·10⁴h), 2 + (40/13)h), a type-s2 root.
- P_3(2) = 180h(3e − h + eh + 16h²) > 0 and P_3(2 + 10h) = −60eh − (160 + 1880e)h² + (200 − 3940e)h³ + … < 0: a type-s3
  root in (2, 2 + 10h).

All four statements are exact polynomial identities in h and hold on all of (0, 10⁻⁶], hence at every admissible damping
point (𝖧 ⊂ (0, 10⁻⁶)). At h = 10⁻⁶ a 60-digit census over C and all P_l (I ran l ≤ 8400; prop:is-mult/cor:t49-right
exclude roots in [2, 51] beyond hκ = 70) gives **2629 roots with real part in (2, 3), 1269 real and 1360 non-real, all at
l ≤ 999, all with |ι| < 4.3**: the report's numbers exactly. None of the larger p_(v) roots lies below 3.

**Are they met at level 0?** Step 1 of prop:iii-i11-3-1 takes q_0 = 3 − ε, q′ = w_+ − 1 − ε, so the window is
(1 − ε, 2 + ε_+ − ε): every one of the roots above is in it. (Level 1: (η_1, 1 + ε_+ − ε); at h = 10⁻⁶ every root with
Re < 3 has |μ| ≤ 50, so (f) of prop:iii-f1-2-3 keeps them out; levels 2 and 3 lie in (0, 1], where (a) says there are none.)

**Do they enter with nonzero coefficients?** Yes, generically. The report's argument (w = χρ^μ k, K_w = L̂_b(0)w ∈
C_c^∞ + ρ^(Re μ+3 or more), injectivity of L̃_b(0), density of C_c^∞ in ρ^a H^∞_b) is sound. One point the report
glosses: the rows ⟨·, f*_1⟩, ⟨·, f*_2⟩ of eq:iii-h-3-1 are arbitrary compactly supported test sections, not necessarily
SO(4)-equivariant, so "r(w) = 0 for τ ∉ {s0, s1, v1}" need not hold. It does not matter: subtract a compactly supported v
with r(v) = r(w) (the rows are linearly independent functionals); w − v still has ρ^μ-coefficient k and solves an
admissible forcing. A second, structural reason: η := δ_(g,E_Υ)G_g û solves P^C_b η = 2δ_gG_g(F − columns), and for a
generic F this has a nonzero ρ^(ι^C) term; since δ_(E_Υ)G lowers the decay by exactly one, û must carry the ρ^(ι^C − 1)
term. The damping is designed so that the constraint decays at the □^C rates; it does not make those rates disappear.

**Searched for an exclusion and found none.**
- Projection/rows: L̃_b(0) differs from L̂_b(0) by finite rank (eleven columns, eleven compactly supported rows); the
  nullspace it removes is spanned by the states, whose index sets are (2, 0) ∪ (2 + ℰ_ind) and (3, 0) ∪ (3 + ℰ_ind),
  none at a □^C root below 2.
- Gauge component killed: prop:iii-f4-5-1 Step 4 kills η only for kernel elements (□^C invertible on the homogeneous
  problem). For the inhomogeneous solve η ≠ 0.
- Weight convention: the lemma, prop:iii-f1-2-3 and prop:iii-f4-5-1 all use r^(−ι) = ρ^ι (the mass at 2); no shift.
- Parameter conditions: (C1)–(C5), z ∈ (0, ½], γ_C = 1/h with h ∈ 𝖧 and (v_C, e_C) fixed in eq:iv4-0-1. None moves these
  roots; as h → 0 they converge to the roots of (ι − 2)Q_5, near 2 and just below 3 (lem:s14-small-h), so no admissible
  choice pushes them above 4.
- The paper itself counts them as roots of L̂_b(0) in (1, 2): prop:iii-f4-5-1 Step 3 ("This index set contains the roots
  ι^C_(·,+) − 1, whose real parts exceed 1"), lem:ec-lb-ind (ι₂(h) − 1 as a non-integer indicial root of L_b^(0), used for
  ε_ind), prop:is-iota and prop:is-mult. P-ADM point 4 (proofs/P-ADM.md:1241–1249) flagged the same omission.
- Why it arose: the reader's edition fixes Λ in advance (def:iii-i10-1-1; change (2) of ch. 41's introduction), where
  [Hin26] builds Ẽ′_++ after the proof by its (11.186), which would collect these exponents automatically.

## 2. Downstream (claim (2))

**E′ and lem:iii-i10-1-2 (c).** E′ must contain (μ, ·) for these μ. A root met at level 0 gives the u-exponent μ + 1
(dictionary, sec:iii-i11-1). Λ ∩ {Re < 3}, at every admissible point, is generated by real numbers built from the □^Υ
roots, σ_Υ and integers, with increments of real part below 3/2 from ℰ_ind (real; its □^C-derived offsets ι^C + 1 lie
above 3) and ℰ^ι_ind (likewise); so it is real and independent of h. A non-real μ + 1 is never in Λ. So
lem:iii-i10-1-2 (c) ("every exponent produced with 2 ≤ Re λ ≤ 3 + ε_+ has λ ∈ Λ") is false as stated. CONFIRMED.

**thm:iii-i12-3-1.** I checked the counterexample step by step.
- F = φ(t_*)K(x), compactly supported, real, lies in 𝒴⁰(α) (it lies in every weighted class with empty index sets).
- p⃗′(F) = 0: at (h, p⃗) = (0, 0), L_(b₀), the states, m_ν, f^ν, f^S, f^b are SO(4)-equivariant, and p⃗′ is unique, so
  p⃗′ is equivariant; 𝒫 has types s0, s1, s2, v1 only (𝒮_1, 𝔟 = ℝ ⊕ 𝔰𝔬(4), 𝒲_s0 = 𝒲_c0 = 𝒮_0, 𝒲_s1 = 𝒲_c1 = 𝒮_1,
  𝒲_s2 = 𝒮_2, 𝒲_v1 = 0, sec:iii-i9-1); Schur gives p⃗′ = 0 for K of scalar type 3.
- ḃ_0 = S_0 = 0 holds even with non-equivariant rows: pairing with the eleven dual states (types s0, s1, v1) annihilates
  K, and the 11 × 11 matrix of prop:iii-h-3-2 is invertible. û_0 is then the s3 solution plus a state, the state having
  no term at ρ^(μ*).
- The tf-coefficient of v̂ at ρ_tf^(μ*) has, at the corner with zf, the ρ^(μ*)-coefficient of û_0 as its zf⁰ term (the
  higher levels carry σ^j and enter that coefficient only at zf-order ≥ 1; at type s3 there is no s1 tower at zf-order 0).
  So it is not zero, and u has a nonzero ι⁺-term at 1 + μ*. Its coefficient solves N_ι⁺(L̄, 1 + μ*)W = 0 (no lower
  ι⁺-term feeds it at type s3, F having none), an ODE on (0, 1), so W does not vanish on {R > ½}, where ũ = u.
- 1 + μ* ∈ (2, 2 + 10h]. The report shows it is in Λ for finitely many h only.

The argument holds. It can be made free of the exceptional set: at every small h a degree l with x = hκ ≈ 0.3 carries a
non-real pair of roots of P_l with real part ≈ (3x + 10)/4 ≈ 2.725 (I checked h = 3.7·10⁻⁷, 10⁻⁸, 10⁻¹⁰: real parts
2.7253, 2.7251, 2.7251, imaginary parts 3.36, 21.0, 210; at h = 10⁻⁶ this is lem:s14-sextic-large (c) for 173 ≤ l ≤ 773).
The same forcing at that type gives a non-real ι⁺-exponent of real part ≈ 2.725, never in Λ. This is a numerical
observation for general h (the paper's enclosures are at h = 10⁻⁶ only); the report's s3 version is the one the paper's
own lemmas prove at every admissible h. Either way: **thm:iii-i12-3-1 fails as stated.** CONFIRMED.

**What inherits.** The same counterexample refutes, as stated, every statement that asserts the ι⁺-index set ℰ_♯ (up to
3 + η_2 − 2ε) for the solution of an arbitrary forcing at a base point that may be (0, 0) at b₀: cor:iii-i15-2-10 (b₀ ∈
ℬ̄_*, 𝒩″ = ∅, G = F; its hypotheses hold at type s3 with p⃗′ = 0) and thm:iii-i14-3-1 (h′ ∈ H^(…,(ℰ_♯,3+η_2−2ε),…);
u = h_rem(q′) + h′ with q′ = 0 at type s3). prop:iii-i13-2-1 and lem:iii-i13-2-2 state only plain ι⁺-weights, so their
statements stand; their proofs use the false Λ-valuedness ("as Step 1"). The others the report lists (lem:iii-j1-1-1,
thm:iii-j-2-4, thm:iii-j1-2-1, prop:iii-i15-2-5, thm:iii-i15-3-1, cor:s25-tame, the uses in ch. 43) rest on
lem:iii-i10-1-2 (c) or on Λ_* exhausting the ι⁺-exponents; their proofs have the gap, but I did not establish that each
statement is false. So "inherits" is CONFIRMED as a dependency, PARTLY as a claim of failure.

**thm:iii-i11-4-1.** At level 1, g_1 has the tf-exponent μ + 1 > 2 + η_1, which goes into the level-1 zero energy solve;
û_1 gets μ − 1 ∈ (0, 1); g_2 has μ ∈ (1, 2); level 2 applies prop:iii-g4-4-4 at α_0 = μ (its hypotheses
eq:iii-g4-4-2 hold, μ being a root with d(Re μ, ℤ) ≥ ε_ind). That produces an s1 tower of K⁺-rate μ < α − 2 for the
type-s1 roots (two at every admissible point). As written, (s1, 1 + μ, k) ∉ ℰ_par, so no parameter removes it, and Step 6's
"the towers of rate below α − 2 … are those of the rows of 𝒩_σ" rests on the false Λ-valuedness. Whether the statement
fails depends on the tf connection coefficient of that s1 tower, which the paper does not compute. **Proof gap
CONFIRMED; failure of the statement undecided**, as the report says.

## 3. The fix (claim (3))

The generator 1 + 𝒵, 𝒵 = {indicial roots of L̂_b(0) with 0 < Re < 3}, is right, and in a sense forced: by the
counterexample, any Λ for which thm:iii-i12-3-1 holds must contain 1 + μ for every root μ met at level 0 with a nonzero
coefficient, which is generically every root with Re μ < 2 + ε_+. Taking all of (0, 3) keeps Λ independent of ε_+, as
(G⁺) and def:iii-j-g-plus need (Λ fixed before the constants are decreased). 𝒵 is finite (lem:iii-f1-2-4), closed under
conjugation, independent of b (P2) and of ε_K, ε_+. The roots in [2 + ε_+ − ε, 3) (vector types) give elements of Λ in
(3, 4) at distance at least about 5h above 3, so they add no (G) or (G⁺) violation.

Checked at the sites where the new exponents land:
- lem:iii-i10-1-2 (a): 1 + 𝒵 ⊂ {Re > 2}; Λ ∩ {Re < 2} = π_1ℳ unchanged. (b): ℰ_par stays an index set; its part below 3
  gains only (1 + μ, k); "if Re(λ + j) ≤ 3 with j ≥ 1 then Re λ = 2" unchanged. Independence of ℰ_+ unchanged.
- (c): level 0 gives μ + 1 ∈ 1 + 𝒵; level 1 (any root with |μ| > 50 that the paper does not exclude) gives
  μ + 2 ∈ (1 + 𝒵) + 1 ⊂ Λ; levels 2, 3 meet none. The logarithmic count is unchanged (a root met is one raise, already
  bounded by l_* + 1).
- Step 6: the s1 towers at α_0 = μ give the rows (s1, 1 + μ, k), with Re e_ν = Re μ ≤ 2, so in 𝒩 and removed by the
  elimination; thm:iii-i11-4-1's map is still id − o(1) on the enlarged finite row space; rows at non-real λ are already
  provided for (W_ν̄ = W̄_ν).
- (G), (G⁺), (A_J), the choices of η_1, η_2 and the admissibility exclusions all quantify over Λ ∩ {Re ≤ 4}, which stays
  finite; def:iii-i10-1-3's "possible by lem:iii-i10-1-2 (a)" still applies.
- Ch. 42–43 use Λ_* (finite; complex λ₀ were already allowed by the definition) and the Λ-valued sentence, which hold
  after the fix.

I found no site where the existing proof breaks after the fix, but I did not re-read every Λ-site of ch. 42–44
line by line; "every statement of ch. 41–44 holds by its proof after the edits of report §4" is plausible and consistent
with every site I read, not independently certified. The proposed new lemma lem:s22-c-roots is correct (its four root
locations are exactly what I re-derived). The repair leaves the s1 transition face coefficient question moot rather than
answered.

## 4. Independent computations (claim (4))

All scripts are in /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/rv-i11/
(poly.py, roots.py, excess.py, exact.py, loc.py, census.py, census2.py, window.py, cplx.py, est.py).

- **The polynomial.** det(hN_l(ι)) of eq:s14-nl at (v, e, h) = (1/2, 1/102400, 10⁻⁶), times 64·10¹⁸, equals sec:tab-a's
  Σ π_k(κ)ι^k identically in κ. At l = 390, κ = 152880:
  64·10¹⁸P_390 = −64ι⁶ − 255998991ι⁵ − 319994620649555ι⁴ − 127994684740759511215ι³ + 944903378469873089619ι²
  − 2546096242636821502034ι + 2379096657426967221840, as the report prints.
- **The sign change (exact rational arithmetic).** At r₁ = 2.152870531513212732616 the value is +0.034694920477…, at
  r₂ = r₁ + 10⁻²¹ it is −0.222613896306…. Root: ι_* = 2.152870531513212732616134837666704…, real. The other two roots of
  real part above 19/10 are 2.614703575563… ± 1.340511442624…i. ι_* ∈ Z (prop:is-iota), ι_* − 1 ∈ 𝒵 (type s390, D = 1).
- **The element of Λ.** With the bounds of lem:is-offsets (b), exactly,
  1.674772257·10⁻¹⁷ < ι_* + 356327𝔡₀ + 1116082𝔡₁ − 3 < 1.674872369·10⁻¹⁷; to 80 digits it is 1.6747857852449·10⁻¹⁷. The
  reduction of lem:is-reduction returns (p, q) = (356327, 1116082) as the least excess for y = 3 − ι_*, and the same
  routine returns μ_G = 1.6416021719713·10⁻¹⁴ at (1109655, 31682), as eq:is-mu.
- **(G) and (G⁺).** 𝔡₀ and 𝔡₁ are increments for ℰ_ind as constructed (cor:uc-two-offsets (b)), so this number is in the
  repaired Λ, with real part in (3, 3 + 1.675·10⁻¹⁷). def:uc-choice has ε_K = 1.6416·10⁻¹⁴ and ε_+ = 1.64160217·10⁻¹⁴, so
  (G) and (G⁺) fail there. It is not an isolated witness: over the 2629 roots, **56** elements ι + p𝔡₀ + q𝔡₁ have real
  part in (3, 3 + 1.6416·10⁻¹⁴], and 1144 in (3, 3 + 4.2·10⁻¹³] (the window thm:is-gap says is otherwise empty).
- **Least excess (numerical, not proved).** The least over all 2629 roots is the l = 390 value; the next are
  1.1076·10⁻¹⁵ (l = 23) and 1.3074·10⁻¹⁵ (l = 417), as the report states. Σ(3 − Re ι) = 1207.94 gives an expected least
  excess 𝔡₀𝔡₁/Σ ≈ 3.7·10⁻¹⁶, so the l = 390 value is an unlucky outlier, but at this kind of point admissible ε_K are of
  order 10⁻¹⁶ at best.
- **The count.** Σ(3 − Re ι)² = 793.559, so about 8.928·10¹⁴ new elements below 3, and N_Λ ≈ 9.095·10¹⁴ (against
  < 1.67472·10¹³).

**Rescue?** No admissible choice inside ch. 71's framework (index sets as constructed) restores the bound:
- a smaller ε_K is forced (ε_K < 1.67488·10⁻¹⁷ is proved at h = 10⁻⁶, ≈ 1.6748·10⁻¹⁷ numerically), and the level and
  round counts M_c, K̄, D_e scale like 1/ε_K (×≈ 980);
- N_Λ counts Λ ∩ {Re < 3 + ε_+}, which contains every ι + p𝔡₀ + q𝔡₁ below 3 whatever ε_K is, so N_Λ rises ×≈ 54 and
  N_ι, C_lev, C_* ≈ 6N_ι scale like N_Λ² (×≈ 2950), J_*, l_*, k̄_0 being unchanged;
- a different Λ: dropping 1 + 𝒵 makes thm:iii-i12-3-1 false; keeping only the roots met changes nothing near 3 (ι_* is
  met); omitting 𝔡₀ from ℰ_ind is the question rem:uc-offset-d0 leaves open and is not "as constructed";
- another nearby h moves the roots but not the mechanism: the expected least excess stays of order 10⁻¹⁶ and N_Λ of order
  10¹⁵.

Re-evaluating the same chain at ε_K ≈ 1.6747·10⁻¹⁷ (my estimate, assuming prop:ec-upper and sec:cs carry over with N_Λ
and ε_K replaced): N_ι ≈ 3.16·10³⁸, C_* ≈ 1.90·10³⁹, M_c ≈ 2.39·10¹⁷, so **D_acc ≈ 4.5·10⁵⁶** (×≈ 2.9·10⁶ over
1.57157·10⁵⁰), the level-by-level form of lem:cs-sharp ≈ 7.6·10⁵⁵, and K ≤ 22D + 345 ≈ 10⁵⁸. Even at an optimistic
ε_K ≈ 10⁻¹⁵ the N_Λ² factor alone keeps it above 10⁵⁴. These are orders of magnitude, not proved bounds; an honest
bound needs the new pass the report describes (the ι ∈ Z with Re ι < 3 enclosed to about 10⁻²⁰, a proved least excess,
the new N_Λ, then lem:uc-admissible onward).

**Lower bounds.** They stand. cor:uc-two-offsets (a) needs only λ_♯ + a𝔡₀ + b𝔡₁ ∈ Λ and (G); a larger Λ only forces ε_K
smaller, and R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂) is decreasing in ε_K, so d > 1.2497·10²⁴ and N_NM > 2.624·10²⁵ remain true
(and could be raised to about 1.2·10²⁷). thm:loss-d, thm:ec-lb-proved (whose Θ_g even uses ι₂(h) − 1 as a root),
lem:ec-lb-ind, lem:ec-lb-rounds, prop:ec-rounds, prop:ec-delta-cap and the lower halves of prop:uc-data-order (d)
(K > 22d > 2.7493·10²⁵, K* > 1.0078·10⁵¹) are unaffected.

**The two-branch point.** For Λ exactly as def:iii-i10-1-1 writes it, thm:is-gap, prop:is-lambda and prop:is-count are
true statements about that set; but that set is not what the constructions produce (lem:iii-i10-1-2 (c) is false), and
lem:uc-n-iota / lem:uc-fourier-count bound the Fourier counts only for index sets whose exponents below 3 + ε_+ lie in Λ.
With the repaired Λ the choice is not admissible. Either way thm:uc-integer's d < 1.57157·10⁵⁰ is not established.

## 5. Affected statements and merged texts (task item 5)

**Ch. 41 (by the error, repaired by report §4):** lem:iii-i11-2-1 (sentence and proof list), lem:iii-i10-1-2 (c),
def:iii-i10-1-1 (generators), Step 1 and Step 6 of prop:iii-i11-3-1, thm:iii-i12-3-1 (false), cor:iii-i15-2-10 (false),
prop:iii-i13-2-1 / lem:iii-i13-2-2 (statements stand; proofs "as Step 1"), thm:iii-i11-4-1 (proof gap). Ch. 42: thm:iii-i14-3-1 (false as stated),
lem:iii-j1-1-1 (false premise) and the Λ_* chain. Ch. 43–44: premises of the Λ-valued sites.

**Ch. 71 statements that fail or lose their support after the fix:** rem:gap-sums (last sentence, 71:161–162);
thm:is-gap ("if and only if ε_K < μ_G", the "every other element lies outside (2, 2 + 4.2·10⁻¹³] ∪ (3, 3 + 4.2·10⁻¹³]"
sentence, "ε_K = 1.6416·10⁻¹⁴ is admissible"); prop:is-lambda (set equality, "All its elements are real"); prop:is-count
(a); thm:uc-reduction (iii) ("(G) holds exactly for ε_K < μ_G", N_Λ); def:uc-choice (no longer admissible);
lem:uc-admissible; lem:uc-lambda (a), (c), (d); lem:uc-n-iota; lem:uc-phi-loss's numbers; prop:uc-explicit (arithmetic
right, choice inadmissible); lem:cs-levels (b) and C_lev; prop:cs-cstar; lem:cs-sharp (2.6193·10⁴⁹); prop:uc-d-small
(b)–(d) (2.6193·10⁴⁹, 5.2386·10⁴⁹, 1.10009·10⁵¹); thm:uc-integer (1.57157·10⁵⁰, 3.30029·10⁵¹, C_lev at levels above 3);
prop:uc-data-order (d) upper halves (K ≤ 22D_acc + 345 < 3.45745·10⁵¹, d_1 ≤ 22D_acc + 331, N ≤ 22D_acc + 348,
K < 5.7624·10⁵⁰, K < 1.15248·10⁵¹, k1 ≤ 22D_acc + 340, K* < 4.78156·10¹⁰³); rem:uc-missing; rem:ec-upper-point;
rem:ec-upper-open (1); rem:is-summary; rem:cs-sharpness; rem:ec-not-evaluated (its reference to def:uc-choice as "the
choices for the weights" now names an inadmissible choice). rem:ec-lb-unbounded (71:1796–1801) stays true as arithmetic
but calls 1.57157·10⁵⁰ "the bound of thm:uc-integer".

**Merged texts quoting the upper bound or D_acc** (grep for 1.57157, 3.30029, 3.45745, 4.78156, 5.7624, 1.15248,
D_acc, thm:uc-integer):
- chapters/00-front.md:36 ("1.2497 × 10²⁴ < d < 1.57157 × 10⁵⁰").
- chapters/01-introduction.md:154–156 ("d < 1.57157 × 10⁵⁰ at one admissible choice …").
- chapters/03-theorems.md:315–318 (d below 1.57157 × 10⁵⁰, K below 3.45745 × 10⁵¹) and 362–363 ("explicit upper bounds
  for d and N_NM … thm:uc-integer").
- chapters/90-scope.md:74–78 (d below 1.57157 × 10⁵⁰, N_NM below 3.30029 × 10⁵¹, K below 3.45745 × 10⁵¹).
- chapters/71: the chapter summary 71:21–28 and 31–33 (K below 3.45745 × 10⁵¹); 71:417; the closing paragraph of the
  statement of thm:loss-d, 71:1483–1491 (its parts (i)–(iii) and its lower bounds stand; its last sentence quotes
  thm:uc-integer, so the report's "thm:loss-d unaffected" needs that sentence excepted); 71:1800; rem:ec-upper-point 71:2196–2205; rem:ec-upper-open 71:2207–2230; sec:uc-close 71:2240–2251;
  thm:uc-reduction 71:2551–2564; sec:uc-eval 71:2573–2787; rem:uc-missing 71:2788–2813; sec:is 71:2815–2835;
  sec:cs 71:4084–4110, 4592–4650, 4652–4913; sec:uc-data-order prop:uc-data-order (d) 71:5112–5120 and its proof
  71:5195–5225.
- Not chapters, but stale on the same point: PAPER.md (assembled; regenerate), STATUS.md:53 and 88, INTEGRATION.md:1360
  ("the bound stands"/CONFIRMED records), proofs/P-TR.md (transfers thm:uc-integer to h ∈ [4.76·10⁻¹¹, 10⁻⁶) and uses
  D_acc in prop:tr-fail; it inherits the failure), proofs/P-ADM.md:1241–1249 (the earlier flag).

The report's §5.5 interim texts for 00, 01, 03, 90 and 71:23–28 keep exactly the lower bounds that stand and remove the
upper ones; I found no further merged site outside ch. 71.

## 6. Minor remarks on the report

- §1 "r(w) vanish for τ ∉ {s0, s1, v1}": the rows need not be equivariant; the conclusion holds after subtracting a
  compactly supported correction (above).
- §3 "every statement that carries ℰ_♯ or Λ_* … inherits": correct as a dependency; refuted as statements only for those
  listed in §2 above.
- §3 counterexample "for all but finitely many γ_C": can be strengthened to every admissible point with a non-real root
  (numerically; proved by the paper's lemmas only at h = 10⁻⁶).
- §5 "(G) fails … at def:uc-choice" is a statement about the repaired Λ; for Λ as written the chapter's statements are
  true of that set but do not support the upper bound. The report says this, more briefly.
- §5 lists thm:loss-d as unaffected and, separately, 71:1489–1491 among the summaries to fix; that paragraph is the end
  of thm:loss-d's statement, so the theorem's statement does change (one sentence), though nothing it proves does.
- Not checked by me: the report's §4–§5 OLD/NEW texts line by line (exact string matches, line widths, label
  resolution), the crosswalk notes, and every Λ-site of ch. 42–44.
