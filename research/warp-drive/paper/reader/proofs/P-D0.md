# P-D0: the coefficient c_b, the free choices, and the offset 𝔡₀

Proof file for the coordinator. Nothing in chapters/, crosswalk/ or elsewhere in the repository was edited; this is
the only file written there, and nothing was committed. Every old text in section 6 is copied from the chapters at
HEAD 99e16794 (P-TR merged; equal to the working tree for these files): chapter 71 md5
bb53f3e845095a3cd821bf51f8c12414; chapter 34 (read, not changed) md5 86555dcd5b63c36b3c3266b8c7e14a3d. Each old text
occurs once, as whole lines, and no two overlap. All sixteen texts were applied together to a scratch copy of the
reader directory: lint --chapters 0 hits, assemble --check 0 problems, and, in the scratch copy only, assemble
followed by lint --paper 0 hits (section 8).

Revised after the review R-P-D0 (no Major), which read this file at ace76b95:

- m1: new texts T14 and T15 qualify the title of thm:is-d0 and add one sentence to its (c) pointing to
  thm:is-flat-serves.
- m2: lem:iii-i7-4-1 added to the list of lem:is-flat-uses (T3) and to the audit of section 3.2.
- m3: new text T16 makes thm:tr-transfer (iii) take the index sets as constructed, so it stays true once T6 lands.
- n1, n2 and n3 in T3 (cor:is-flat proof, rem:is-cb-open); n4 in T5; n5 in section 7; n6 in section 5.
- m4: the list of sites in section 4 is replaced by a pointer to the chain's evaluation step, which handles them.
- The line numbers of section 6 are those of HEAD (the edafc288 numbers + 13 for T1–T13).

## 0. Outcome

- **The question asked (c_b at a rotating b): (d).** The paper cannot decide whether c_b vanishes. What is proved
  (new prop:is-cb-normal): by O(4)-equivariance, reflections included, c_b on ker ad_A is one real function
  𝔠(m, a₁, a₂) = ½c_((m,a₁J₁₂+a₂J₃₄))(J₁₂), odd in a₁ and even in a₂, with X_((m,A)) = 𝔠(m, a₁, a₂)J₁₂ +
  𝔠(m, a₂, a₁)J₃₄ in the normal form; so "c_b = 0 near b₀" is the single identity 𝔠 ≡ 0 (the two functions φ± of the
  earlier analysis are one function, by the reflections, which that analysis did not use). 𝔠 depends on γ_(Υ,H) and on
  the free radial functions ζ_∞ and χ of c_Υ and c_(Υ,H) (section 1), through the global inverse of (□^Υ_b)^(0). At the
  computational point that inverse is not even known to exist: its invertibility is part of (AP3), which
  rem:ec-point-outside lists as undecided. No finite computation of values can show 𝔠 ≡ 0; one certified non-zero
  value would show c_b ≢ 0 for the data at which it is taken (section 2.3 says which computation and its size). So
  neither (a) nor (b) can be established by the paper's means, and (c) cannot be established for every admissible
  choice either; (b) would need one function of three variables to vanish identically by the choice of one number and
  two functions of one variable.
- **The goal behind the question (drop 𝔡₀): dropped in full, by another route, whatever c_b is.** thm:is-d0 (c) is an
  "if and only if" only for the memberships in the form ω̇_b(0, Ȧ) ∈ 𝒜^((2,0)∪(2+ℰ_ind)), that is with the terms of
  ω̇_b(0, ·) recorded relative to its own leading order 2. The terms of ω̇_b(0, ·) at 2 + 𝔡₀ + ℕ₀ may instead be recorded
  relative to the order 1, where they are the offsets 1 + 𝔡₀ + ℕ₀ that ω̇_b(1, 0) contributes anyway (with the same
  logarithmic orders). Every use in the paper of the memberships of ω̇_b(0, ·) and ġ^Υ_b(0, ·) allows this: they are
  used only combined with the mass state (𝒢 = (2, 0) ∪ (2 + ℰ_ind), ω̇(ḃ) ∈ 𝒜^((1,0)∪(1+ℰ_ind))), through the column
  index set ℰ_col, and through their weights and leading terms (section 3, an audit of every citation). The rotation
  state never enters a formal solution, a tower or a row, where an offset becomes an increment of Λ. So the index set
  ℰ′_ind of the proof of thm:is-d0 (c) (here ℰ^φ_ind) serves unconditionally (new thm:is-flat-serves), and
  cor:is-flat holds without its hypothesis c_b = 0.
- **What it gives at h = 10⁻⁶, nothing else moved.** (G) holds exactly for ε_K < μ♭_Z, 3.548125563·10⁻¹⁰ < μ♭_Z
  < 3.548125564·10⁻¹⁰, which exceeds ε_Υ, so (G) costs nothing beyond ε_K < ε_Υ; and N_Λ ≤ 3,683,190,611 (against
  909,507,124,095,312). The chain as merged (prop:uc-dependence) asks ε_K < ε_+ < 10⁻¹³ and 4k̄_max + 24 > I_base +
  22,119. At the inputs below it gives **d_NM < 9.12529·10⁴³** (now 7.57245·10⁵⁵: a factor 8.3·10¹¹), N_NM <
  1.91631·10⁴⁵, K ≤ 22D_NM + 345 < 2.00757·10⁴⁵ (section 4). The second hypothesis is what forces N̄_Λ up to
  77,112,616,084; if the chain could drop it, N̄_Λ = 3,683,190,611 would give d_NM ≈ 2.08·10⁴¹, and if it could also
  allow ε_+ up to just below ε_Υ, about 1.5·10³⁸ (estimates from the same formulas, not drafted).
- **For S-HPT.** 𝔡₀ is dropped, so by that report's own sequence h should not be moved: at h = 10⁻⁶ the lattice in
  𝔡₁ alone has least excess μ♭_Z > ε_Υ.

**Inputs for the chain (exact).** ε_K = 9.99·10⁻¹⁴ = 999/10¹⁶, ε_+ = 9.995·10⁻¹⁴ = 9995/10¹⁷, N̄_Λ = 77,112,616,084
(the proved count is N_Λ ≤ 3,683,190,611; the larger integer is needed only for the inequality of prop:uc-dependence),
k̄_0 = 3, J_* = 15,000,015, l_* = 50, J′ = 765,000,816, ε_Υ = 1.4619·10⁻¹⁰ unchanged. Then Δβ_0 = 0.999²ε_K =
9.97002999·10⁻¹⁴ exactly, Δτ_0 = 1.4604381·10⁻¹⁰, ε′_0 = 2.5·10⁻¹⁷ < 0.001ε_K, η_0 = 𝔡₁.

## 1. The free choices of the paper, and which of them c_b depends on

- e_Υ, γ_Υ (z = 4e_Υγ_Υ², hence 𝔡₀, 𝔡₁): where it is made: def:iii-b-6-1, sec:iii-d2-1; at the computational point:
  fixed, 1/100 and 1/100 (def:ec-point); enters c_b: yes
- γ_(Υ,H) ∈ (0, ϵ₀]: where it is made: prop:iii-d1-4-1, sec:iii-d2-1; at the computational point: not fixed
  (rem:ec-point-outside); enters c_b: yes
- c_Υ = ζ_∞(|x|)|x|⁻¹dt: ζ_∞ = 1 for large |x|, otherwise free (support condition off U_Γ on {|x| < 5R₁}): where it is
  made: def:iii-b-6-1, sec:iii-d-1, sec:iii-d2-1; at the computational point: free; enters c_b: yes
- c_(Υ,H) = −½χ(|x|)d|x|: χ ∈ C_c^∞({|x| < 5R₁}), χ = 1 near r_h, support off U_Γ: where it is made: sec:iii-d1-1,
  lem:iii-d-5-1; at the computational point: free; enters c_b: yes
- trace weight 2/3 of E_Υ: where it is made: def:iii-b-6-1; at the computational point: forced (rem:s13-trace-weight:
  weight 1 puts the s0 root 2 into the gap); enters c_b: —
- E_C = (c_C, e_C, γ_C; v_C): where it is made: def:iii-b-6-1, ch 33; at the computational point: γ_C = 10⁶, (v_C, e_C) =
  (1/2, 1/102400); c_C free inside; enters c_b: no (ω̇_b uses only □^Υ_b and ġ_b)
- t_* = t − ψ(|x|): where it is made: eq:iii-b-3-6; at the computational point: fixed by its formula; enters c_b: no
  ((□^Υ_b)^(0) acts on stationary sections)
- weight α of the inverse of (□^Υ_b)^(0): where it is made: lem:iii-d1-5-1; at the computational point: any in the gap;
  enters c_b: no (lem:iii-d1-5-1)
- inner radius r_0: where it is made: chapter 32, opening; at the computational point: parameter; enters c_b: not
  examined; not needed
- Kerr–Schild family g_b and its parameters b = (m, A): where it is made: prop:iii-b-3-6; at the computational point:
  fixed; enters c_b: yes, through ġ_b(0, Ȧ)
- the basis ġ^Υ_b(ḃ) of the zero energy states: where it is made: prop:iii-f3-2-2, sec:iii-h-1; at the computational
  point: fixed; enters c_b: defines c_b
- index sets ℰ_ind, ℰ^ι_ind, ℰ_++, ℰ^C_I, ℰ_+: where it is made: sec:uc-index-sets, def:uc-choice; at the computational
  point: free as long as they serve; enters c_b: no — the route of section 3 uses this freedom
- weights, levels, orders, inner products, cut-offs: where it is made: def:uc-choice, def:cs-choices, ch 37–42; at the
  computational point: chosen; enters c_b: no

So the data on which c_b depends and which the paper leaves open are γ_(Υ,H), ζ_∞ and χ. rem:is-cb-open (new) states
this in the paper. Changing the family g_b by a smooth stationary diffeomorphism whose generator is decaying leaves c_b
unchanged (ġ_b changes by 2δ*V♭, ω̇_b by −2V♭, which has integer exponents); this is not placed in the paper.

## 2. The coefficient c_b

### 2.1 Why no symmetry or local quantity decides it

prop:is-cb-normal (section 6, T3) is the complete symmetry reduction: X_b ∈ ker ad_A from the vanishing on im ad_A;
the maximal torus of rotations in the two planes of A forces X_((m,A)) into the Cartan algebra span{J₁₂, J₃₄}; the
exchange of the planes and the two reflections diag(1, −1, 1, 1), diag(1, 1, 1, −1) give 𝔠₂(a₁, a₂) = 𝔠₁(a₂, a₁),
oddness in a₁ and evenness in a₂. Nothing further follows from symmetry: time reversal is not a symmetry of the
problem (the horizon regularity selects the future horizon, and c_Υ is odd under t ↦ −t), and every other isometry of
g_((m,A)) is used.

### 2.2 A numerical observation (guidance only; no proof uses it; not for the paper)

The natural way to decide c_b for small γ_(Υ,H) is the Schur complement of the proof of prop:iii-d1-4-1: the
unmodified operator has the cokernel ℓ_b (the horizon functional, ℓ_b(w) = ∮ w(K) dA over a horizon section, K the
horizon generator), and ℓ_b((□^Υ_b)^(0)u) = γ_(Υ,H)ℓ_b(2E_HGδ*u) when c_Υ vanishes near the horizon. So c_b would have a
term ℓ_b(η_b(0, Ȧ))/(4π²γ_(Υ,H)) times the ρ^(2+𝔡₀) coefficient of the kernel element W*, and if
ℓ_b(2δ_(g_b)G_(g_b)ġ_b(0, Ȧ)) were of first order in A, c_b ≠ 0 would follow for all small γ_(Υ,H). It is not. With
the exact Kerr–Schild Myers–Perry metric of def:iii-b-3-2, 50-digit finite differences and Gauss–Legendre quadrature
over the exact horizon r_A = r₊ (m = 1): ℓ_b(2δGġ_b(1, 0)) = −39.4784176043574 = −4π² at A = 0 and at A = 0.2J₁₂;
ℓ_b(2δGġ_b(0, J₁₂)) and ℓ_b(2δGġ_b(0, J₃₄)) are below 10⁻²⁰ in modulus at A = 0.1J₁₂, 0.2J₁₂ and 0.3J₁₂ + 0.1J₃₄;
the first-order integrand is −4cos 2η on the horizon sphere, a pure degree-2 harmonic. So the pairing appears to be
−4π²ṁ exactly, the 1/γ_(Υ,H) term of c_b vanishes, and small γ_(Υ,H) does not decide c_b at leading order: c_b stays a
bounded global connection coefficient.

### 2.3 The computation that would decide it, and its size

To show c_b ≢ 0 for one set of data it suffices to show 𝔠 ≠ 0 at one point, for instance its first-order coefficient
in a₁ at b₀. That needs, at fixed explicit ζ_∞, χ, γ_(Υ,H) (and e_Υ = γ_Υ = 1/100): (1) the vector type 1 radial
solution of (□^Υ_(b₀))^(0)ω = −η_(b₀)(0, J₁₂) (prop:iii-f3-2-2 (4): ω = r²B(r)V_i dz^i, one scalar second-order ODE on
r > r_h with the c_Υ and c_(Υ,H) terms, regular at the horizon, decaying); (2) the scalar type 0 part of the first-order
terms in a₁ of η_((m₀,a₁J₁₂))(0, J₁₂) + (□^Υ_((m₀,a₁J₁₂)))^(0)ω (explicit from the second-order Kerr–Schild expansion
and B); (3) the decaying solution, regular at the horizon, of the 2 × 2 second-order system of scalar type 0 with that
right side, and its coefficient of ρ^(2+𝔡₀) (roots 2 + 𝔡₀ and 3 at infinity, separated by about one power of ρ). Two
linear ODE boundary value problems with one regular singular point at r_h and one at infinity: a certified enclosure
with interval Taylor integration over a few thousand steps on [r_h, R] and matched asymptotic series at R. Before it,
(AP3) at the chosen data (invertibility of (□^Υ_b)^(σ) on the closed upper half plane) would have to be established,
which is itself undecided at the computational point and is the larger task (all frequencies and harmonics). Under
the no-code ruling the enclosure would have to be printed as written inequalities with tables. Showing c_b ≡ 0 is
beyond any finite computation; it would need an identity, and section 2.1 shows no symmetry gives one. None of this is
needed for the bound, by section 3.

## 3. Dropping 𝔡₀ whatever c_b is

### 3.1 The argument

1. thm:is-d0 (b), (c) give, unconditionally: with the boundary spectrum typed by parity (lem:is-typed), no
   construction other than ω̇_b(0, ·) has an offset 𝔡₀ relative to its leading order, and the rotation corrections have
   no term at 2 + 𝔡₀ + ℕ₀ (lem:is-rot-s0 and the comparison of coefficients). So ℰ^φ_ind (= the ℰ′_ind of that proof)
   serves every construction except ω̇_b(0, ·) and the tensors built from it.
2. ω̇_b(0, Ȧ)'s typed index set relative to 2 is ℰ^φ_ind plus pairs at 𝔡₀ + j of logarithmic order at most j
   (eq:is-l1: only the j + 1 points 2 + 𝔡₀ + j − i of the typed E(α) count). These form the index set
   ℰ_(𝔡₀) := {(𝔡₀ + j, l) : l ≤ j}. And 1 + ℰ_(𝔡₀) ⊂ ℰ^φ_ind: ω̇_b(1, 0) has the pairs (1 + 𝔡₀ + j, j) by the same count.
3. Hence ω̇_b(0, Ȧ) ∈ 𝒜^((2,0)∪(2+(ℰ^φ∪ℰ_(𝔡₀)))) ⊂ 𝒜^((1,0)∪(1+ℰ^φ)) and ġ^Υ_b(0, Ȧ) ∈ 𝒜^((3,0)∪(3+(ℰ^φ∪ℰ_(𝔡₀)))) ⊂
   𝒜^((2,0)∪(2+ℰ^φ)) = 𝒜^(𝒢^φ), and r²ġ^Υ_b(0, Ȧ) ∈ 𝒜^(ℰ^φ_col). The forms keep the leading orders 2 and 3 without
   logarithms and the next exponents at 2 + 𝔡₁, 3 + 𝔡₁.
4. Audit (section 3.2): these memberships are used only in those three ways. The increments of Λ arise where a state's
   correction, relative to the normalisation of a row or tower, is added to an exponent (thm:iii-g2-4-2, the towers
   of sec:iii-g2-1 and def:iii-g2-2-5, the rotation rows); ġ^Υ_b(0, ·) at a spin change outside im ad_(A(b)) is none of
   these (the v1 terms are h_(b,v1)(V) = ½ġ^Υ_b(0, [A, A_V]), where c_b vanishes); the parameter states enter only
   through 𝒢 and ℰ_col, i.e. as generators (chapter 42: "F_0(λ₀) vanishes unless λ₀ ∈ π_1𝒢", "the parameters
   p⃗_(≤0) enter at the u-exponents of 𝒢"). Note 3 + 𝔡₀ = 2 + (1 + 𝔡₀) ∈ π_1𝒢^φ, so the parameter terms' exponents stay
   generators.
5. So Λ^φ (increments π_1(ℰ^φ ∪ ℰ^(ι,φ)) ∪ {1}, 𝔡₀ not among them) serves, Λ^φ ⊂ Λ, and cor:is-flat's analysis (already
   in the chapter, from P-UB1) applies verbatim: μ♭_Z and 1,283,560,912 ≤ N_Λ ≤ 3,683,190,611.

Why the same device does not remove 𝔡₁: the translation corrections are among the states of the formal solutions at ι⁺
(the s1 terms of thm:iii-g2-4-2); their term at ρ^(2+𝔡₁), relative to the Minkowski translation, makes a remainder
at ϰ + 2 + 𝔡₁ and so a new exponent at ϰ + 𝔡₁: 𝔡₁ is a genuine increment. The rotation state ġ^Υ_b(0, ·) is a zero energy
parameter state and enters no such iteration.

### 3.2 The audit: every citation of the memberships of ω̇_b(0, ·) and ġ^Υ_b(0, ·)

Found by searching all chapters for prop:iii-f3-2-2, eq:iii-f3-2-1, eq:iii-f3-2-2, eq:iii-f3-4-2, prop:iii-f3-4-1,
rem:iii-f3-2-3, "ω̇", "Ȧ", "ġ_b(0", "ġ(0", "ġ_b(ḃ)", 𝒢 and ℰ_ind in chapters 32–46, 38a, 65, 71.

- 34:1255–1260, 1277: result: prop:iii-f3-2-2 (1), (2); what it uses: the statement itself; holds with ℰ^φ because:
  replaced by eq:is-flat-memb (lem:is-flat-memberships (b))
- 34:1299: result: rem:iii-f3-2-3, proof; what it uses: ω̇_b(0, W) decays: D ∈ 𝒜^ϵ; holds with ℰ^φ because: (iii):
  positive least real part
- 34:1450–1453, 1467–1468, 1506, 1536–1552: result: prop:iii-f3-4-1 (eq:iii-f3-4-2); what it uses: states smooth, O(ρ²),
  in the kernel; ω′_π ∈ 𝒜^(β−1); continuity in b; holds with ℰ^φ because: (iii)
- 34:1620–1621: result: sec:iii-f4-1; what it uses: weight 3 of ġ^Υ_b(0, Ȧ); holds with ℰ^φ because: (iii)
- 34:1752–1794: result: lem:iii-f4-3-1; what it uses: weights, excesses, leading term 2m|x|⁻⁴(dt̄ + d|x|) ⊗_s V(Ȧ); holds
  with ℰ^φ because: (iii): leading term unchanged, remainders of higher weight
- 34:1862–1873: result: lem:iii-f4-4-1; what it uses: leading term of ġ^Υ_b(0, Ȧ) independent of A; holds with ℰ^φ
  because: (iii)
- 37:84–90: result: sec:iii-h-1; what it uses: weights 2, 3; holds with ℰ^φ because: (iii)
- 37:297–301: result: rem:iii-h-2-6; what it uses: bounds in 𝒜^(3−δ); holds with ℰ^φ because: (iii)
- 37:628: result: lem:iii-h-5-2; what it uses: O(ρ³) of ġ(0, Ȧ); holds with ℰ^φ because: (iii)
- 38:1656: result: lem:iii-i2-4-3; what it uses: 𝒜^q, q = 3; holds with ℰ^φ because: (iii)
- 39:89–99: result: (BP3), sec:s20-setting; what it uses: 𝒜^(q−δ) with q = 3; holds with ℰ^φ because: (iii)
- 40:125–148, 282, 444, 532: result: sec:iii-i7-1 (eq:iii-i7-1-1), lem:iii-i7-2-2, sec:iii-i15-2-8, lem:iii-i7-4-1 (b)
  (ι⁺-order 2 of χ_K ġ_b(ḃ_j), χ_K h_b(Ṡ⁽⁰⁾_j)); what it uses: ω̇(ḃ) ∈ 𝒜^((1,0)∪(1+ℰ)), ġ(ḃ) ∈ 𝒜^𝒢; holds with ℰ^φ
  because: (i)
- 41:560–564: result: lem:iii-i11-1-1; what it uses: r²ġ_b(0, Ȧ) ∈ 𝒜^((1,0)∪(1+ℰ)) ⊂ ℰ_col; holds with ℰ^φ because: (ii)
- 42:154, 330–345, 676–690: result: def:iii-i14-1-2, lem:iii-i14-2-4, lem:iii-j-2-1; what it uses: ġ_b(ḃ) combined;
  ι⁺-exponents in 𝒢; ∂_b h_(b,rem); holds with ℰ^φ because: (i), b-independent index sets
- 43:995–998: result: prop:iii-j3-5-2; what it uses: ġ(b_rem) linear, weights; holds with ℰ^φ because: (iii)
- 44:548–562: result: (iii) of sec:iii-i15-3; what it uses: ℰ_col from (3,0)∪(3+ℰ) for ġ_b(0, Ȧ); holds with ℰ^φ because:
  (ii)
- 38a:61, 93–120: result: lem:iii-i15-1-1 (P3); what it uses: index sets of ġ_b (in 𝒢), smoothness, parity; holds with
  ℰ^φ because: (i)
- 65:678: result: lem:gd-r3-5; what it uses: h_tot ∈ 𝒜^𝒢; holds with ℰ^φ because: (i)
- 71 (sec:is, sec:uc-index-sets, cor:uc-two-offsets, thm:is-d0): result: statements about ℰ_ind as constructed; what it
  uses: unchanged; holds with ℰ^φ because: true as they stand

thm:iii-g2-4-2's ℰ^ι_ind collects the index sets of the states that enter u_(b,0) (proof of prop:is-iota: the table rows
and the s1 and v1 terms); ġ^Υ_b is not among them. The physical states (prop:iii-f4-5-1) have offsets at least 1
relative to −2.

### 3.3 The new and changed results (texts in section 6)

- prop:is-cb-normal, rem:is-cb-open (c_b: the reduction and the decision (d)).
- def:is-flat-set (ℰ^φ_ind, ℰ^(ι,φ)_ind, eq:is-flat-d0), lem:is-flat-memberships (eq:is-flat-memb), lem:is-flat-uses
  (the audit), thm:is-flat-serves (the index sets serve; Λ^φ ⊂ Λ; increments; k̄_0, l_*, η_0, J_* admissible).
- cor:is-flat: hypothesis c_b = 0 replaced by the index sets of thm:is-flat-serves; the proof's first sentence and
  "for ℰ′_ind" changed; everything else verbatim.
- def:uc-choice, lem:uc-admissible, lem:uc-gaps, lem:uc-lambda: the new choice; thm:uc-reduction (iii), sec:is
  opening, sec:is-smaller opening, rem:is-summary, rem:uc-offset-d0: the narrative.
- thm:is-d0 (T14, T15): the title says "with the memberships as stated", and (c) ends by pointing to
  thm:is-flat-serves; its "if and only if" concerns the memberships in their original form and is unchanged.
- thm:tr-transfer (iii) (T16): "and with the index sets as constructed", so that (iii) names one index set once
  def:uc-choice takes ℰ^φ_ind; at h other than 10⁻⁶ the paper does not prove thm:is-flat-serves, and (iii) is
  proved, as before, for the index sets as constructed.
- Unchanged and still true: cor:uc-two-offsets, cor:is-lower, thm:is-gap, prop:is-count, prop:is-lambda (all about
  the index sets as constructed); Λ^φ ⊂ Λ, so prop:is-lambda's "every element of real part at most 2.514 is real"
  holds for Λ^φ, which lem:cs-fourier (b) uses.

## 4. The new choice and what the chain gives

lem:uc-admissible's conditions at ε_K = 9.99·10⁻¹⁴, ε_+ = 9.995·10⁻¹⁴: eq:iii-i9-1-1 (ε_+ < δ_50 < δ_♯) yes; (G) and
(G⁺) by cor:is-flat (ε_+ < μ♭_Z); ε_K < ε_Υ; ε′_0 = ½(ε_+ − ε_K) = 2.5·10⁻¹⁷ < 0.001ε_K = 9.99·10⁻¹⁷, so
0.999ε_K ≤ α − 4 ≤ ε_K; Step 4 of prop:iii-i11-3-1: ε_K + ε ≤ 9.99·10⁻¹⁴ + 1.4619·10⁻¹³ < ε_g. prop:uc-dependence: ε_+ <
10⁻¹³ yes; 4k̄_max + 24 = 235,964,856,912,618,898,212 > 235,964,856,912,243,213,665 = I_base + 22,119 at N̄_Λ =
77,112,616,084 (and it fails at N̄_Λ = 77,112,616,083, and at the proved count 3,683,190,611 by a factor 21). The
formulas of prop:uc-dependence, evaluated in exact rational arithmetic (they reproduce the chapter's integers at the
present choice exactly), with D_e := 2.06834·10²³ ≥ F_1 = 2.0683343797…·10²³:

| quantity | value |
|---|---|
| L_<, L_>, R_b | 10,030,060,100,150, 10,030,060,100,152, 10,030,060,100,152 |
| N_ι | 2,274,483,427,581,842,436,178,649,809,456 |
| k̄_max, d̄_Φ | 58,991,214,228,154,724,547, 4,780,982,197,210 |
| C_lev | 4,548,966,855,163,684,872,434,412,235,525 |
| I_base, R_base | 235,964,856,912,243,191,546, 235,964,856,912,243,213,643 |
| T_12 | 4,548,966,855,399,649,729,381,299,963,589 |
| C_* | 13,646,900,934,872,993,882,693,355,228,178 |
| D′_* | 45,626,410,950,895,746,537,368,729,412,029,739,775,077,379 |
| D_acc | 45,626,410,950,904,844,471,104,575,139,346,875,130,945,114 < 4.56265·10⁴³ |
| D_NM | 91,252,821,901,800,591,008,473,304,551,381,395,888,219,703 < 9.12529·10⁴³ |
| 21D_NM + 6 | 1,916,309,259,937,812,411,177,939,395,579,009,313,652,613,769 < 1.91631·10⁴⁵ |
| 22D_NM + 345 | 2,007,562,081,839,613,002,186,412,700,130,390,709,540,833,811 < 2.00757·10⁴⁵ |
| 3R at the choice (prop:ec-rounds) | > 2.0538·10²³; D_e < 1.0071 · 3R |

These are guidance for the chain's own evaluation step, which produces the printed integers and changes every site
that quotes the bound or the choice: in chapter 71, in sec:tr (beyond T16) and in the chapters 00, 01, 03 and 90.
Those sites are not drafted here; their list at HEAD, including the ones P-TR added, is the review's (R-P-D0, m4) and
goes with that step. cor:is-lower stays true but no longer bounds the chosen index sets from below.

## 5. Merge notes

- T1–T16 are in chapter 71, pairwise disjoint, at HEAD line numbers; apply from the bottom up, or by matching the old
  texts, which are unique.
- T3 replaces cor:is-flat as a whole and inserts the six new results before it, after thm:is-d0; T14 and T15 change
  thm:is-d0 itself.
- T16 is outside the thirteen texts of the original file: it keeps thm:tr-transfer (iii) true after T6. The rest of
  sec:tr that would change if 𝔡₀ were dropped at other values of h too (the review's m3) needs a proof at h and is
  not drafted.
- T12 (lem:uc-lambda) fixes N̄_Λ = 77,112,616,084 so that prop:uc-dependence applies as merged. If the chain's
  inequality 4k̄_max + 24 > I_base + 22,119 is removed or replaced, T12 may take N̄_Λ := 3,683,190,611 and its (c), (d)
  become k̄_max = 2,817,643,822,898,538,579, d̄_Φ = 228,357,817,884 and 62N̄_Λ + 10 = 228,357,817,892.
- Symbols introduced: ℰ^φ_ind, ℰ^(ι,φ)_ind, Λ^φ, ℰ_(𝔡₀), 𝔠, X_b. None occurs in chapters 71, 34 or 40–46 before (the
  chapters' ℰ^♭ of prop:iii-i10-3-1 is a different set; 𝔠 occurs only in chapters 46, 63, 64, 82 and 87, unrelated).

## 6. Placement

This part and the crosswalk rows are instructions for merging; they are not chapter text. Each old text is quoted
exactly between the fences, and each new text replaces it as a whole, with the line breaks shown. The line numbers
are those of chapter 71 at HEAD 99e16794 (P-TR merged) and serve only to find the place. Order of the texts below:
the section sec:is in the chapter's order (T1, T2, T14, T15, T3, T4), then the choice (T5, T13, T6–T12), then sec:tr
(T16). T14–T16 answer the review (m1, m3).

### T1. sec:is, the opening paragraph: its last part, chapter 71 lines 2911–2919

Old (9 lines):

```old
It gives 1.85753·10¹⁴ < N_Λ ≤ 909,507,124,095,312, k̄_0 = 3 and J_* = 15,000,015 ([[prop:is-count]]), and it raises the
lower bound for d_acc at every admissible choice of the weights to 1.2250·10²⁷ ([[cor:is-lower]]). Finally it decides
when ℰ_ind can omit 𝔡₀ ([[thm:is-d0]]): an admissible ℰ_ind that omits 𝔡₀ exists if and only if one explicit family of
coefficients c_b vanishes at every b near b₀; c_b vanishes at b₀, at every non-rotating b and on the image of ad_(A(b)),
and this paper does not determine it elsewhere. If c_b vanishes, (G) holds exactly for ε_K < μ♭_Z, where
3.548125563·10⁻¹⁰ < μ♭_Z < 3.548125564·10⁻¹⁰, so for every ε_K < ε_Υ ([[def:iii-i10-1-3]]), and N_Λ ≤ 3,683,190,611
([[cor:is-flat]]). Whether an admissible ℰ_ind can omit 𝔡₁ is not decided either. Neither question enters an upper bound
for the loss d: the index sets as constructed serve with every ε_K < μ_Z, and the two questions decide only whether
smaller index sets, with a larger ε_K and a smaller N_Λ, are available.
```

New (12 lines):

```new
It gives 1.85753·10¹⁴ < N_Λ ≤ 909,507,124,095,312, k̄_0 = 3 and J_* = 15,000,015 ([[prop:is-count]]), and it raises the
lower bound for d_acc at every admissible choice of the weights, for the index sets as constructed, to 1.2250·10²⁷
([[cor:is-lower]]). Finally it removes the offset 𝔡₀ from the increments of Λ. With the memberships in the form that
[[sec:uc-index-sets]] gives them, an index set omitting 𝔡₀ exists if and only if one explicit family of coefficients c_b
vanishes at every b near b₀ ([[thm:is-d0]]); c_b vanishes at b₀, at every non-rotating b and on the image of ad_(A(b)),
it is fixed by one function of three variables ([[prop:is-cb-normal]]), and this paper does not determine it at a
rotating b ([[rem:is-cb-open]]). But the terms of ω̇_b(0, ·) at the exponents 2 + 𝔡₀ + ℕ₀ may be recorded relative to
the order 1, where the offset 1 + 𝔡₀ is present anyway, and every use of the memberships of ω̇_b(0, ·) and ġ^Υ_b(0, ·)
allows this ([[lem:is-flat-uses]]). So the index sets ℰ^φ_ind and ℰ^(ι,φ)_ind of [[def:is-flat-set]], which omit 𝔡₀,
serve whatever c_b is ([[thm:is-flat-serves]]); with them (G) holds exactly for ε_K < μ♭_Z, where
3.548125563·10⁻¹⁰ < μ♭_Z < 3.548125564·10⁻¹⁰, so for every ε_K < ε_Υ ([[def:iii-i10-1-3]]), and N_Λ ≤ 3,683,190,611
([[cor:is-flat]]). The choice of [[def:uc-choice]] takes them. Whether an admissible ℰ_ind can omit 𝔡₁ is not decided.
```

### T2. sec:is-smaller, the opening paragraph, chapter 71 lines 3632–3633

Old (2 lines):

```old
The index sets as constructed take the boundary spectrum at every type ([[cor:uc-two-offsets]] (b)). A smaller
index set serves wherever the coefficients at the omitted exponents vanish. Two symmetries give such vanishing.
```

New (4 lines):

```new
The index sets as constructed take the boundary spectrum at every type ([[cor:uc-two-offsets]] (b)). A smaller
index set serves wherever the coefficients at the omitted exponents vanish. Two symmetries give such vanishing. A term
may also be recorded relative to a lower order, at which its exponent is an offset that is present anyway; this removes
𝔡₀ whatever the coefficients c_b are ([[thm:is-flat-serves]]).
```

### T14. thm:is-d0, the title and (a), chapter 71 lines 3670–3671

Old (2 lines):

```old
**Theorem {#thm:is-d0}** (When ℰ_ind can omit 𝔡₀.) (a) For ℰ_ind as constructed, 𝔡₀ ∈ π_1ℰ_ind
([[cor:uc-two-offsets]] (b)), at every b.
```

New (2 lines):

```new
**Theorem {#thm:is-d0}** (When ℰ_ind can omit 𝔡₀ with the memberships as stated.) (a) For ℰ_ind as constructed,
𝔡₀ ∈ π_1ℰ_ind ([[cor:uc-two-offsets]] (b)), at every b.
```

### T15. thm:is-d0 (c), its last sentence, chapter 71 lines 3681–3682

Old (2 lines):

```old
and at every b with A = 0, and c_(m,OAOᵀ)(OȦOᵀ) = c_(m,A)(Ȧ) for O ∈ SO(4). This paper does not determine c_b at a
rotating b.
```

New (3 lines):

```new
and at every b with A = 0, and c_(m,OAOᵀ)(OȦOᵀ) = c_(m,A)(Ȧ) for O ∈ SO(4). This paper does not determine c_b at a
rotating b. With the memberships of ω̇_b(0, ·) and ġ^Υ_b(0, ·) read relative to the order 1, index sets that omit 𝔡₀
serve whatever c_b is ([[thm:is-flat-serves]]).
```

### T3. six new results before cor:is-flat, and cor:is-flat rewritten, chapter 71 lines 3715–3749

Old (35 lines):

```old
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
increments only those of real part below 1, for ℰ′_ind 𝔡₁ alone; so every element of Λ ∖ Λ_ℬ has real part greater
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

New (234 lines):

```new
**Proposition {#prop:is-cb-normal}** (The coefficients c_b in normal form.) Fix the indicial solution of type s0 at
2 + 𝔡₀ in [[def:is-cb]], so that each c_b(Ȧ) is a real number, and for b = (m, A) near b₀ let X_b ∈ 𝔰𝔬(4) be the
matrix with c_b(W) = −tr(X_bW) for every W ∈ 𝔰𝔬(4). Then X_b ∈ ker ad_A, and X_((m,OAOᵀ)) = OX_((m,A))Oᵀ for every
O ∈ O(4). For A = a₁J₁₂ + a₂J₃₄,

    X_((m,A)) = 𝔠(m, a₁, a₂)J₁₂ + 𝔠(m, a₂, a₁)J₃₄,     𝔠(m, a₁, a₂) := ½c_((m,A))(J₁₂),               {#eq:is-cb-normal}

and 𝔠(m, −a₁, a₂) = −𝔠(m, a₁, a₂) = −𝔠(m, a₁, −a₂); in particular 𝔠(m, 0, a₂) = 0. So, for δ > 0, c_b vanishes on
ker ad_A for every b = (m, A) with |m − m₀| < δ and ‖A‖ < δ if and only if 𝔠(m, a₁, a₂) = 0 for all m, a₁ and a₂ with
max(|m − m₀|, |a₁|, |a₂|) < δ.

*Proof.* The metrics g_b, the operators and the 1-forms η_b(0, Ȧ) are real ((P3) of [[lem:iii-i15-1-1]]), and the
indicial solution may be chosen real; so c_b(Ȧ) is real, and it is linear in Ȧ ([[def:is-cb]]). ⟨X, Y⟩ := −tr(XY) is
an inner product on 𝔰𝔬(4), so X_b exists and is unique. ad_A is skew for it, as ⟨[A, X], Y⟩ = −⟨X, [A, Y]⟩; so
im ad_A is the orthogonal complement of ker ad_A, and, as c_b vanishes on im ad_A ([[thm:is-d0]] (c)), X_b ∈ ker ad_A.

*Equivariance.* Let O ∈ O(4) and φ_O(t, x) := (t, Ox). By [[lem:iii-e1-2-1]], φ_O*g_((m,OAOᵀ)) = g_((m,A)), and
differentiating in A gives φ_O*ġ_((m,OAOᵀ))(0, OWOᵀ) = ġ_((m,A))(0, W). φ_O* commutes with δ, G and δ* of corresponding
metrics, and it fixes t_*, c_Υ = ζ_∞(|x|)|x|⁻¹dt and c_(Υ,H) = −½χ(|x|)d|x| ([[sec:iii-d2-1]]); so it intertwines
η_((m,OAOᵀ))(0, OWOᵀ) with η_((m,A))(0, W) and (□^Υ_((m,OAOᵀ)))^(0) with (□^Υ_((m,A)))^(0), and it preserves the b-spaces
on which these are inverted. Hence φ_O*ω̇_((m,OAOᵀ))(0, OWOᵀ) = ω̇_((m,A))(0, W). The indicial solution of type s0 is
ρ^(2+𝔡₀) times a combination of dt_* and d|x| with constant coefficients, which φ_O* fixes; so
c_((m,OAOᵀ))(OWOᵀ) = c_((m,A))(W) for every W, that is tr(X_((m,OAOᵀ))OWOᵀ) = tr(X_((m,A))W), which is
X_((m,OAOᵀ)) = OX_((m,A))Oᵀ.

*The normal form.* Let A = a₁J₁₂ + a₂J₃₄. The rotations O = R(θ₁) ⊕ R(θ₂), by θ₁ in the (x¹, x²)-plane and by θ₂ in the
(x³, x⁴)-plane, have OAOᵀ = A, so X_((m,A)) = OX_((m,A))Oᵀ. In 2 × 2 blocks the off-diagonal block B of X_((m,A))
satisfies R(θ₁)BR(θ₂)ᵀ = B for all θ₁, θ₂, so B = 0 (take θ₂ = 0 and θ₁ = π), and the diagonal blocks are
antisymmetric; so X_((m,A)) = 𝔠₁J₁₂ + 𝔠₂J₃₄ with real 𝔠₁, 𝔠₂, and c_((m,A))(J₁₂) = −tr(X_((m,A))J₁₂) = 2𝔠₁, as
tr(J₁₂²) = −2 and tr(J₃₄J₁₂) = 0. The permutation P of the coordinates with x¹ ↔ x³ and x² ↔ x⁴ has PJ₁₂Pᵀ = J₃₄,
PJ₃₄Pᵀ = J₁₂ and PAPᵀ = a₂J₁₂ + a₁J₃₄, so equivariance gives 𝔠₂(m, a₁, a₂) = 𝔠₁(m, a₂, a₁). The reflections
Q₁ := diag(1, −1, 1, 1) and Q₂ := diag(1, 1, 1, −1) have Q₁J₁₂Q₁ᵀ = −J₁₂, Q₁J₃₄Q₁ᵀ = J₃₄, Q₂J₁₂Q₂ᵀ = J₁₂ and
Q₂J₃₄Q₂ᵀ = −J₃₄, so equivariance gives 𝔠₁(m, −a₁, a₂) = −𝔠₁(m, a₁, a₂) and 𝔠₁(m, a₁, −a₂) = 𝔠₁(m, a₁, a₂). With
𝔠 := 𝔠₁ this is [[eq:is-cb-normal]] and the symmetries.

*The equivalence.* Every A is OA′Oᵀ with O ∈ SO(4) and A′ = a₁J₁₂ + a₂J₃₄, max(|a₁|, |a₂|) = ‖A‖ ([[sec:iii-b-3-1]]),
and X_((m,A)) = OX_((m,A′))Oᵀ. As X_b ∈ ker ad_A and c_b(X_b) = −tr(X_b²) = ⟨X_b, X_b⟩, c_b vanishes on ker ad_A if and
only if X_b = 0, that is, by [[eq:is-cb-normal]], if and only if 𝔠(m, a₁, a₂) = 𝔠(m, a₂, a₁) = 0. ∎

**Remark {#rem:is-cb-open}** (What the coefficients c_b depend on, and what would decide them.) The coefficients c_b are
fixed by g_b, by □^Υ_b and by the decay of ω̇_b(0, Ȧ) ([[eq:iii-f3-2-1]]). The constraint damping E_C, the time function
t_* and the weight at which (□^Υ_b)^(0) is inverted ([[lem:iii-d1-5-1]]) do not enter them; the gauge parameters e_Υ,
γ_Υ and γ_(Υ,H) and the radial functions ζ_∞ and χ of c_Υ and c_(Υ,H) ([[sec:iii-d2-1]]) do. [[def:ec-point]] fixes e_Υ
and γ_Υ and leaves γ_(Υ,H), ζ_∞ and χ free, and at the computational point the invertibility of (□^Υ_b)^(0) for some
γ_(Υ,H), on which the definition of ω̇_b rests, is part of the condition (AP3) of [[rem:ec-point-outside]], which this
paper does not decide. By [[prop:is-cb-normal]], c_b = 0 near b₀ is the identity 𝔠 = 0 between functions of
(m, a₁, a₂), which no finite set of values decides, while one non-zero value of 𝔠 shows c_b ≠ 0 for the data at which it
is taken. To first order in a₁, 𝔠 is read from two radial boundary value problems on {r > r_h}, with regularity at the
horizon sphere and decay at infinity, posed at given ζ_∞, χ and parameters: the problem of vector type 1 that
ω̇_(b₀)(0, J₁₂) solves ([[prop:iii-f3-2-2]] (4)), and a problem of scalar type 0 for (□^Υ_(b₀))^(0), two equations of
second order whose indicial matrix at infinity is N_s0 (the upper left block of [[eq:s13-nsl]] at κ = 0), with right
side minus the scalar type 0 part of the
terms of first order in a₁ of η_((m₀,a₁J₁₂))(0, J₁₂) + (□^Υ_((m₀,a₁J₁₂)))^(0)ω̇_(b₀)(0, J₁₂); the coefficient of ρ^(2+𝔡₀)
of the second solution gives it. No statement of this paper solves these problems, and no bound of this chapter needs
them ([[thm:is-flat-serves]]).

**Definition {#def:is-flat-set}** (The index sets ℰ^φ_ind and ℰ^(ι,φ)_ind.) Let ℰ^φ_ind be the union, over the
constructions (c1)–(c6) of [[sec:is-ind]], of the index sets that [[lem:iii-a-1-4]] and [[lem:iii-a-1-5]] build when E(α)
and ord are taken from N(A, ·)⁻¹½(1 + φ) for the even constructions and from N(A, ·)⁻¹½(1 − φ) for the odd ones
([[lem:is-typed]]; the parities are those of the proof of [[thm:is-d0]] (b)), the right sides being recorded through
ℰ^φ_ind itself, each index set taken relative to the leading order of its construction as in [[sec:is-ind]], and with
the pairs at the offsets 𝔡₀ + ℕ₀ removed from the index sets of the rotation corrections and of ω̇_b(0, ·). It is the
index set ℰ′_ind of the proof of [[thm:is-d0]] (c). Let ℰ^(ι,φ)_ind be the index set of [[thm:iii-g2-4-2]] built in the
same way from the index sets of the states of its proof, and put

    ℰ_(𝔡₀) := {(𝔡₀ + j, l) : j ∈ ℕ₀, 0 ≤ l ≤ j}.                                                      {#eq:is-flat-d0}

**Lemma {#lem:is-flat-memberships}** (The memberships with ℰ^φ_ind.) At every b near b₀:

(a) every construction of the union ℰ_ind of [[sec:uc-index-sets]] other than ω̇_b(0, ·), and every tensor built from
such a construction, lies in the space that its construction asserts ([[prop:iii-d2-3-1]], [[prop:iii-d3-3-1]],
[[prop:iii-f3-2-2]]) with ℰ^φ_ind in place of ℰ_ind;

(b) for every Ȧ ∈ 𝔰𝔬(4),

    ω̇_b(0, Ȧ) ∈ 𝒜^((2,0)∪(2+(ℰ^φ_ind∪ℰ_(𝔡₀)))),     ġ^Υ_b(0, Ȧ) ∈ 𝒜^((3,0)∪(3+(ℰ^φ_ind∪ℰ_(𝔡₀))));     {#eq:is-flat-memb}

(c) 1 + ℰ_(𝔡₀) ⊂ ℰ^φ_ind; 𝔡₁ ∈ π_1ℰ^φ_ind ∩ π_1ℰ^(ι,φ)_ind and 𝔡₀ ∉ π_1(ℰ^φ_ind ∪ ℰ^(ι,φ)_ind); and
ℰ^φ_ind ∪ ℰ_(𝔡₀) ⊂ ℰ_ind and ℰ^(ι,φ)_ind ⊂ ℰ^ι_ind for ℰ_ind and ℰ^ι_ind as constructed. So
min Re ℰ^φ_ind = min Re ℰ^(ι,φ)_ind = 𝔡₁, the logarithmic orders of ℰ^φ_ind and ℰ^(ι,φ)_ind are at most those of ℰ_ind
and ℰ^ι_ind as constructed, and their exponents of real part at most 3/2 are among 1 and the numbers of [[eq:is-low]]
other than 𝔡₀.

*Proof.* (a) Each construction is even or odd at every b, and so is its right side ((P3) of [[lem:iii-i15-1-1]] and the
proof of [[thm:is-d0]] (b)); so [[lem:is-typed]] with ½(1 ± φ) puts it in the space built from the typed boundary
spectrum, whose index set, relative to its leading order, is part of ℰ^φ_ind. For the rotation corrections the
coefficients of ρ^(2+𝔡₀+j)(log ρ)^k vanish for all j, k ∈ ℕ₀ (proof of [[thm:is-d0]] (b) and (c): at j = 0 the
coefficient lies in the kernel of N(A, 2 + 𝔡₀), which is of type s0, and has no scalar type 0 part by
[[lem:is-rot-s0]]; at j ≥ 1 by comparing coefficients, 2 + 𝔡₀ + j being no root), so the removed pairs are not needed. A
tensor built from a construction carries its index set shifted by 1 ([[sec:is-ind]]).

(b) ω̇_b(0, Ȧ) is even, and [[lem:iii-f3-2-1]] with k = 2 and [[lem:is-typed]] give ω̇_b(0, Ȧ) ∈ 𝒜^((2,0)∪(2+E)), E its
typed index set relative to 2. The pairs of E at offsets outside 𝔡₀ + ℕ₀ lie in ℰ^φ_ind by [[def:is-flat-set]]. At the
offset 𝔡₀ + j, [[eq:is-l1]] with F = (2, 0) counts no point of F, as 2 + 𝔡₀ + j − i is not an integer, and no point of
the typed E(α) other than the 2 + 𝔡₀ + j − i, 0 ≤ i ≤ j: every root of real part above α > 0 lies in R
([[lem:is-roots]] (a)), and no element of R other than 2 + 𝔡₀ differs from 2 + 𝔡₀ by an integer, as
0 < d₂(l) < d₁(l) ≤ δ′₁ < 𝔡₀ < 1.34·10⁻⁶ for every l ≥ 1 and 𝔡₁ = d₂(1) ([[lem:is-roots]] (b)). So
ℓ̂_E(2 + 𝔡₀ + j) ≤ j + 1, the logarithmic order there is at most j, and E ⊂ ℰ^φ_ind ∪ ℰ_(𝔡₀). As
ġ^Υ_b(0, Ȧ) = ġ_b(0, Ȧ) + δ*_(g_b)ω̇_b(0, Ȧ), with ġ_b(0, Ȧ) ∈ ρ³C^∞ and δ*_(g_b) ∈ ρDiff¹_b (proof of
[[prop:iii-f3-2-2]] (1) and (2)), the second membership follows.

(c) ω̇_b(1, 0) is even, of leading order 1 ([[lem:iii-f3-2-1]] with k = 1), and its typed index set is part of ℰ^φ_ind,
with nothing removed. At 2 + 𝔡₀ + j, [[eq:is-l1]] with F = (1, 0) counts no point of F and the j + 1 points
2 + 𝔡₀ + j − i, 0 ≤ i ≤ j, of the typed E(α), which contains (2 + 𝔡₀, 0), 2 + 𝔡₀ being a root of the even type s0
([[lem:is-roots]] (b), (c)); so the logarithmic order there is j, (1 + 𝔡₀ + j, j) ∈ ℰ^φ_ind, and 1 + ℰ_(𝔡₀) ⊂ ℰ^φ_ind by
[[eq:s11-index-set]]. The translation corrections are odd, of leading order 2, and their typed E(α) contains
(2 + 𝔡₁, 0), 2 + 𝔡₁ being a root of the odd type s1; so 𝔡₁ ∈ π_1ℰ^φ_ind, and 𝔡₁ ∈ π_1ℰ^(ι,φ)_ind, as the translation
corrections enter the s1 terms of [[thm:iii-g2-4-2]]. By the proof of [[thm:is-d0]] (b), an offset 𝔡₀ arises only at the
root 2 + 𝔡₀, so only for an even construction, and only at the leading order 2, a leading order m ≤ 1 giving offsets
2 + 𝔡₀ − m + j ≥ 1 + 𝔡₀; the even constructions of leading order 2 are the rotation corrections and ω̇_b(0, ·), whose
pairs at 𝔡₀ + ℕ₀ are removed. So 𝔡₀ ∉ π_1ℰ^φ_ind. The states of the proof of [[thm:iii-g2-4-2]] are those of the table of
[[sec:iii-g2-1]] and the s1 and v1 terms (proof of [[prop:is-iota]]); none is ω̇_b(0, ·), and their offsets are offsets
of constructions of [[sec:is-ind]] other than ω̇_b(0, ·), integers, and numbers of real part at least 1 coming from the
physical states (proof of [[prop:is-logs]] (c)); so 𝔡₀ ∉ π_1ℰ^(ι,φ)_ind. The typed E(α) and the typed orders are at most
the untyped ones, and the rules [[eq:is-l1]] and [[lem:is-count]] (b) are monotone in E(α), ord and F; by induction over
the constructions each typed index set lies in the one as constructed, and removing pairs only shrinks it. By the count
of (b) with the untyped E(α), (𝔡₀ + j, j) lies in the index set of ω̇_b(0, ·) as constructed, so ℰ_(𝔡₀) ⊂ ℰ_ind. This
gives the inclusions, hence the bounds for the logarithmic orders. The least real parts and the exponents below 3/2
follow from the inclusions, from [[eq:is-low]], [[prop:is-iota]] and [[lem:uc-gaps]], and from
𝔡₁ ∈ π_1ℰ^φ_ind ∩ π_1ℰ^(ι,φ)_ind and 𝔡₀ ∉ π_1(ℰ^φ_ind ∪ ℰ^(ι,φ)_ind). ∎

**Lemma {#lem:is-flat-uses}** (The uses of the memberships of ω̇_b(0, ·) and ġ^Υ_b(0, ·).) Outside [[sec:is]], the
memberships of ω̇_b(0, Ȧ) and ġ^Υ_b(0, Ȧ) of [[prop:iii-f3-2-2]] (1), [[eq:iii-f3-2-2]] and [[eq:iii-f3-4-2]] are used in
[[rem:iii-f3-2-3]], [[prop:iii-f3-4-1]], [[sec:iii-f4-1]], [[lem:iii-f4-3-1]], [[lem:iii-f4-4-1]], [[sec:iii-h-1]],
[[rem:iii-h-2-6]], [[lem:iii-h-5-2]], [[lem:iii-i2-4-3]], (BP3) of [[sec:s20-setting]], [[sec:iii-i7-1]],
[[lem:iii-i11-1-1]], (P3) of [[lem:iii-i15-1-1]] and (iii) of [[sec:iii-i15-3]], and, through [[eq:iii-i7-1-1]], in
[[lem:iii-i7-2-2]], [[lem:iii-i7-4-1]], [[sec:iii-i15-2-8]], [[def:iii-i14-1-2]], [[lem:iii-i14-2-4]], [[lem:iii-j-2-1]],
[[prop:iii-j3-5-2]] and [[lem:gd-r3-5]]; and they are used there only through the following statements, each of which
holds with ℰ^φ_ind in place of ℰ_ind when ω̇_b(0, ·) and ġ^Υ_b(0, ·) are taken in the forms [[eq:is-flat-memb]]:

(i) for every ḃ ∈ 𝔟, ω̇_b(ḃ) ∈ 𝒜^((1,0)∪(1+ℰ_ind)) and ġ^Υ_b(ḃ) ∈ 𝒜^𝒢 with 𝒢 = (2, 0) ∪ (2 + ℰ_ind) ([[eq:iii-i7-1-1]]
at b₀ and, by (P3), at b);

(ii) r²ġ^Υ_b(0, Ȧ) ∈ 𝒜^(ℰ_col) with ℰ_col = ({(0, 0), (1, 0)} ∪ ℰ_ind ∪ (1 + ℰ_ind)) + ℕ₀ ([[lem:iii-i11-1-1]] and (iii)
of [[sec:iii-i15-3]]);

(iii) ω̇_b(0, Ȧ) and ġ^Υ_b(0, Ȧ) are polyhomogeneous with an index set of positive least real part, with weights 2 and 3
and leading terms at ρ² and ρ³ free of logarithms, the latter that of ġ_b(0, Ȧ) plus δ* of that of ω̇_b(0, Ȧ).

Moreover none of the states of the table of [[sec:iii-g2-1]], of the towers of [[def:iii-g2-2-5]] and of the rotation
rows of [[def:iii-i14-1-3]] is ω̇_b(0, ·) or ġ^Υ_b(0, ·) at a spin change outside im ad_(A(b)).

*Proof.* The list of uses is that of the citations of [[prop:iii-f3-2-2]] (1)–(2), [[eq:iii-f3-2-2]] and
[[eq:iii-f3-4-2]] and of the places that state the index sets of ġ_b(0, Ȧ) or ω̇_b(0, Ȧ). In [[rem:iii-f3-2-3]] the
membership of ω̇_b(0, W) gives D ∈ 𝒜^ϵ; in [[prop:iii-f3-4-1]] the states are smooth sections that are O(ρ²), and
ω′_π ∈ 𝒜^(β−1); in [[sec:iii-f4-1]], [[lem:iii-f4-3-1]] and [[lem:iii-f4-4-1]] they enter through their weights and
leading terms; in [[sec:iii-h-1]], [[rem:iii-h-2-6]], [[lem:iii-h-5-2]], [[lem:iii-i2-4-3]] and (BP3) through the weights
2 and 3 and the bounds in 𝒜^(q−δ). These are (iii). [[sec:iii-i7-1]], (P3) and the results that use
[[eq:iii-i7-1-1]] use (i), except [[prop:iii-j3-5-2]], which uses the weights, and [[lem:iii-i11-1-1]] and (iii) of
[[sec:iii-i15-3]] use (ii). Now take ℰ_ind := ℰ^φ_ind. (i): by [[lem:is-flat-memberships]] (a),
ω̇_b(1, 0) ∈ 𝒜^((1,0)∪(1+ℰ^φ_ind)) and ġ^Υ_b(1, 0) ∈ 𝒜^((2,0)∪(2+ℰ^φ_ind)); by [[eq:is-flat-memb]] and (c) there,
(2, 0) ∪ (2 + (ℰ^φ_ind ∪ ℰ_(𝔡₀))) ⊂ (1, 0) ∪ (1 + ℰ^φ_ind), as 2 + ℰ^φ_ind = 1 + (1 + ℰ^φ_ind) ⊂ 1 + ℰ^φ_ind and
2 + ℰ_(𝔡₀) = 1 + (1 + ℰ_(𝔡₀)) ⊂ 1 + ℰ^φ_ind, and likewise (3, 0) ∪ (3 + (ℰ^φ_ind ∪ ℰ_(𝔡₀))) ⊂ (2, 0) ∪ (2 + ℰ^φ_ind); so
(i) follows by linearity in ḃ. (ii): r²ġ^Υ_b(0, Ȧ) ∈ 𝒜^((1,0)∪(1+ℰ^φ_ind)∪(1+ℰ_(𝔡₀))), and 1 + ℰ_(𝔡₀) ⊂ ℰ^φ_ind lies in
the ℰ_col built from ℰ^φ_ind. (iii): min Re(ℰ^φ_ind ∪ ℰ_(𝔡₀)) = 𝔡₁ > 0, and in [[eq:is-flat-memb]] the orders 2 and 3
carry no logarithm and the next exponents have real part at least 2 + 𝔡₁ and 3 + 𝔡₁; the leading terms are those of
[[prop:iii-f3-2-2]]. Finally, the states of the table, the towers and the rotation rows are the constructions of
[[prop:iii-d2-3-1]], [[prop:iii-d3-3-1]] and [[prop:iii-f4-5-1]] and their symmetric gradients (proof of
[[lem:iii-i10-2-1]] (b), [[def:iii-i14-1-3]]); the rotation state is h_(b,v1)(V) = ½ġ^Υ_b(0, [A(b), A_V])
([[rem:iii-f3-2-3]]), at a spin change in im ad_(A(b)). ∎

**Theorem {#thm:is-flat-serves}** (Index sets without the offset 𝔡₀.) Whatever the coefficients c_b are, ℰ^φ_ind and
ℰ^(ι,φ)_ind may be taken for ℰ_ind and ℰ^ι_ind in [[sec:uc-index-sets]]: every proof of this paper that uses ℰ_ind and
ℰ^ι_ind holds with them, the memberships of ω̇_b(0, ·) and ġ^Υ_b(0, ·) being read in the forms [[eq:is-flat-memb]].
Let Λ^φ be the set that [[def:iii-i10-1-1]] builds from them, with the least ℰ^C_I and the least ℰ_++. Then Λ^φ ⊂ Λ, Λ
the set built from the index sets as constructed; the only increment of Λ^φ of real part below 1 is 𝔡₁; every increment
of real part at most 3/2 is a sum of the increments 𝔡₁, 1, 1 + δ′₁, 1 + δ₂, 1 + 𝔡₀ and 1 + 2𝔡₀; and k̄_0 = 3, l_* = 50,
η_0 = 𝔡₁ and J_* = 15,000,015 are admissible for them.

*Proof.* *The memberships.* ℰ_ind and ℰ^ι_ind enter the statements of this paper through memberships and lower bounds for
their real parts ([[sec:uc-index-sets]]). ℰ^φ_ind does not depend on b, and min Re ℰ^φ_ind = 𝔡₁ ≥ ε_Υ
([[lem:is-flat-memberships]] (c), [[lem:ec-gauge-gap]]). By [[lem:is-flat-memberships]] (a) every membership of
[[sec:uc-index-sets]] holds with ℰ^φ_ind except those of ω̇_b(0, ·) and ġ^Υ_b(0, ·); these hold in the forms
[[eq:is-flat-memb]], and by [[lem:is-flat-uses]] every statement that the other proofs draw from them holds with
ℰ^φ_ind. ℰ^(ι,φ)_ind is the index set of [[thm:iii-g2-4-2]] for the states of its proof, whose memberships hold with
ℰ^φ_ind by [[lem:is-flat-memberships]] (a) and [[lem:is-flat-uses]]; for a spin change Ȧ ∈ im ad_(A(b)), c_b(Ȧ) = 0
([[thm:is-d0]] (c)). The conditions on ℰ_+ ([[eq:iii-i7-1-2]], [[eq:iii-i8-1-1]], (H3)) are conditions on ℰ_+ alone, met
by the least index set of the proof of [[lem:iii-i10-1-2]] (b) built from ℰ^φ_ind and ℰ^(ι,φ)_ind. The constructions that
[[lem:iii-i10-1-2]] (c) summarises add elements of ℰ_ind to exponents through the memberships of the states, towers and
companions of [[sec:iii-g2-1]], [[def:iii-g2-2-5]] and [[def:iii-i14-1-3]] and of the corrections in
[[thm:iii-g2-4-2]], none of which is ω̇_b(0, ·) or ġ^Υ_b(0, ·) at a spin change outside im ad_(A(b)), and the states
ġ_b(ḃ) enter through 𝒢 and ℰ_col only ((i) and (ii) of [[lem:is-flat-uses]]), that is through the generators π_1𝒢 and
2 + π_1ℰ_col of [[def:iii-i10-1-1]]. So every exponent that they produce with real part at most 3 + ε_+ lies in Λ^φ, with
the logarithmic orders bounded as there.

*The increments.* The increments of Λ^φ are π_1(ℰ^φ_ind ∪ ℰ^(ι,φ)_ind) ∪ {1}. By [[lem:is-flat-memberships]] (c) those of
real part at most 3/2 are among 1, 𝔡₁, 1 + δ₂, 1 + 𝔡₁, 1 + δ′₁, 1 + 2𝔡₁, 1 + 𝔡₀, 1 + 𝔡₀ + 𝔡₁ and 1 + 2𝔡₀
([[eq:is-low]] without 𝔡₀), each a sum of the six numbers listed, and the only one below 1 is 𝔡₁. The six are
increments: 𝔡₁ and 1 + δ′₁ come from the translation corrections (roots 2 + 𝔡₁ and 3 + δ′₁ of type s1), 1 and 1 + δ₂
from the rotation corrections (roots 3 of types s0 and v1 and 3 + δ₂ of type s2), 1 + 𝔡₀ from ω̇_b(1, 0) and 1 + 2𝔡₀ from
the class μ_s0 = −1 − 𝔡₀, whose first step has the leading order 1 − 𝔡₀ (root 2 + 𝔡₀ in both); none of these offsets is
removed in [[def:is-flat-set]].

*Λ^φ ⊂ Λ and the numbers.* By [[lem:is-flat-memberships]] (c), ℰ^φ_ind ⊂ ℰ_ind and ℰ^(ι,φ)_ind ⊂ ℰ^ι_ind; so the sets 𝒢
and ℰ_col built from ℰ^φ_ind lie in those built from ℰ_ind, and the least ℰ_++, the closure of ℰ^♯_+ ∩ {Re < 2} under
fewer additions, lies in the one as constructed. The generators and increments of Λ^φ are therefore among those of Λ,
and Λ^φ ⊂ Λ. The logarithmic orders that l_* and k̄_0 bound ([[def:iii-i10-1-1]]) are at most those as constructed, and
the pole orders and multiplicities are unchanged; so k̄_0 = 3 and l_* = 50 remain admissible ([[prop:is-count]] (b),
[[cor:sp-lstar]]). η_0 is the least real part of the increments, 𝔡₁, and J_* = ⌈5/𝔡₁⌉ + 2 = 15,000,015
([[prop:is-count]] (c)). ∎

**Corollary {#cor:is-flat}** (The gap condition without 𝔡₀.) Take ℰ_ind := ℰ^φ_ind and ℰ^ι_ind := ℰ^(ι,φ)_ind
([[thm:is-flat-serves]]), and let Λ := Λ^φ. Then (G) holds if and only if ε_K < μ♭_Z, and (G⁺) if and only if
ε_+ < μ♭_Z, where μ♭_Z := (n + 1)𝔡₁ − y, with y := 3 − Re ι for the root ι of P_700 of positive imaginary part
([[lem:is-z3]]) and n := ⌊y/𝔡₁⌋ = 394194, satisfies

    3.548125563·10⁻¹⁰ < μ♭_Z < 3.548125564·10⁻¹⁰.

As [[def:iii-i10-1-3]] asks ε_K < ε_Υ, and ε_Υ < 1.46214·10⁻¹⁰ < μ♭_Z ([[lem:ec-gauge-gap]]), (G) then imposes
nothing beyond the other conditions of [[def:iii-i10-1-3]] and [[eq:iii-i9-1-1]]. For ε_+ ∈ (0, μ♭_Z),
1,283,560,912 ≤ N_Λ ≤ 3,683,190,611. On the part Λ_ℬ of Λ built from the generators other than 1 + 𝒵, (G) holds if and
only if ε_K < μ♭ := λ_♯ + 4470304𝔡₁ − 3 ∈ (5.0190·10⁻⁸, 5.0193·10⁻⁸) ([[prop:gap-sums]]).

*Proof.* The increments: by [[thm:is-flat-serves]], every increment of real part at most 3/2 is a sum of 𝔡₁, 1,
1 + δ′₁, 1 + δ₂, 1 + 𝔡₀ and 1 + 2𝔡₀, each of which is an increment, and the only increment of real part below 1 is 𝔡₁.
*The part Λ_ℬ.* As in [[thm:is-gap]], the targets are
y = 1.4901, 0.4901, 0.4901 − δ′₁, 0.4901 − δ₂, 0.4901 − 𝔡₀, 0.4901 − 2𝔡₀ (third window and λ_♯ + 1 + 𝔡₀ + ℕ₀𝔡₁ near
3), 1 − c and 1/2 − c, and the least excess is ⌈y/𝔡₁⌉𝔡₁ − y. By the column "frac" of the table of [[thm:is-gap]] and
the values 1470297.2661 and 1470293.2661 of y/𝔡₁ at 0.4901 − 𝔡₀ and 0.4901 − 2𝔡₀, (1 − frac)𝔡₁ is least at y = 1.4901,
where it is μ♭, and every other is above 1.3888·10⁻⁷. *The elements of Z₃.* The proof of [[prop:is-lambda]] uses of the
increments only those of real part below 1, here 𝔡₁ alone; so every element of Λ ∖ Λ_ℬ has real part greater
than 2 + 2.932·10⁻⁶, and one of real part at most 3 + 10⁻⁸ is ι + q𝔡₁ or its conjugate with ι ∈ Z₃ and q ∈ ℕ₀, of real
part 3 + q𝔡₁ − y_ι. So the first window is missed, the third adds nothing, and the least positive excess in the second
for ι is (n⁺ + 1)𝔡₁ − y_ι, with n⁺ = ⌊y_ι/𝔡₁⌋ from the rows of [[sec:tab-is]] (proof of [[lem:is-gap-z]]). Bounding it
there by the bounds of [[lem:is-offsets]] (b) gives in every row a number above 4.2406·10⁻¹⁰, except for the row l = 700
of the second table, where y lies in (0.1313982198300303806313, 0.1313982198300303806333) and n⁺ = 394194, which
gives μ♭_Z with the bounds stated. As μ♭_Z < μ♭, the least excess of Λ over the windows is μ♭_Z, which gives both
equivalences. *N_Λ.* Each β ∈ ℬ♭ (the 26 rational β < 3, λ_♯ + 1 + 𝔡₀, λ_♯ + 1 + 2𝔡₀, λ_♯ + 1 + δ′₁, λ_♯ + 1 + δ₂
and 3) contributes ⌊(3 − β)/𝔡₁⌋ + 1 points, as no point lies in [3, 3 + ε_+); the sets of the first 28 and of β = 3
are pairwise disjoint by [[lem:is-offsets]] (c); the sums without and with λ_♯ + 1 + δ′₁ and λ_♯ + 1 + δ₂ give
56,436,656 and 59,377,257. Each ι ∈ Z₃ contributes the n⁺ + 1 points ι + q𝔡₁, 0 ≤ q ≤ n⁺, as ε_+ < μ♭_Z; the sum of the
n⁺ + 1 over Z₃ is 3,623,813,354, and over its 1360 non-real elements 1,227,124,256, whose points are not real and
pairwise distinct (proof of [[prop:is-count]] (a)). So 56,436,656 + 1,227,124,256 ≤ N_Λ ≤ 59,377,257 +
3,623,813,354. ∎
```

### T4. rem:is-summary, its last part, chapter 71 lines 3770–3774

Old (5 lines):

```old
1.67472·10¹³ elements below 3 + ε_+. Two further things are not determined by this paper: the coefficient c_b of
[[def:is-cb]] at a rotating b, which for index sets that keep 𝔡₁ decides whether ε_K may be taken up to ε_Υ
([[cor:is-flat]]) or only below μ_Z ([[thm:is-gap]]), and whether an admissible ℰ_ind can omit 𝔡₁. Neither enters an
upper bound for d: the index sets as constructed serve with every ε_K < μ_Z, and the two decide only whether smaller
index sets, with a larger ε_K and a smaller N_Λ, are available.
```

New (5 lines):

```new
1.67472·10¹³ elements below 3 + ε_+. The index sets ℰ^φ_ind and ℰ^(ι,φ)_ind of [[def:is-flat-set]] omit 𝔡₀ whatever
the coefficients c_b of [[def:is-cb]] are ([[thm:is-flat-serves]]); with them (G) holds for every ε_K < μ♭_Z, so for
every ε_K < ε_Υ, and N_Λ ≤ 3,683,190,611 ([[cor:is-flat]]), and the choice of [[def:uc-choice]] takes them. Two things
are not determined by this paper: the coefficients c_b at a rotating b ([[prop:is-cb-normal]], [[rem:is-cb-open]]),
which no bound of this chapter uses, and whether an admissible ℰ_ind can omit 𝔡₁.
```

### T5. rem:uc-offset-d0, its second half, chapter 71 lines 2419–2427

Old (9 lines):

```old
with ℰ_ind as constructed, (G) fails at every ε_K ≥ 1.6417·10⁻¹⁴ ([[cor:uc-two-offsets]]). Whether a smaller
admissible ℰ_ind omits 𝔡₀ is not decided by this paper; [[thm:is-d0]] reduces it to the vanishing of one family of
coefficients. The root ι^Υ_(s0,2) = 2 + 𝔡₀ of (□^Υ_b)^(0) lies above the weights in (0, ι^Υ_(s1,2)) at which
[[prop:iii-d2-3-1]] solves for the corrections of the states, and these corrections start at the order (2, 0), so a
smaller admissible ℰ_ind keeps the exponent 𝔡₀ wherever a term at that root has a nonzero coefficient. At b₀ the
operator commutes with the rotations, and the corrections of the states of types s1 and v1 do not meet the roots of
type s0. At a rotating b the metric couples the angular types at the order |x|⁻³ ([[eq:iii-d2-2-2]]), and ℰ_ind is one
index set serving at every b near b₀. So (G) at an ε_K ≥ 1.6417·10⁻¹⁴ needs a smaller admissible ℰ_ind ∪ ℰ^ι_ind that
omits 𝔡₀ or 𝔡₁; omitting 𝔡₀ means the vanishing of these coefficients at every b near b₀.
```

New (11 lines):

```new
with ℰ_ind as constructed, (G) fails at every ε_K ≥ 1.6417·10⁻¹⁴ ([[cor:uc-two-offsets]]). The root
ι^Υ_(s0,2) = 2 + 𝔡₀ of (□^Υ_b)^(0) lies above the weights in (0, ι^Υ_(s1,2)) at which [[prop:iii-d2-3-1]] solves for the
corrections of the states, and these corrections start at the order (2, 0), so an index set in which they are recorded
relative to their leading orders keeps the offset 𝔡₀ wherever a term at that root has a nonzero coefficient. At b₀ the
operator commutes with the rotations, and the corrections of the states of types s1 and v1 do not meet the roots of
type s0. At a rotating b the metric couples the angular types at the order |x|⁻³ ([[eq:iii-d2-2-2]]), and ℰ_ind is one
index set serving at every b near b₀. Of the constructions of leading order 2 only ω̇_b(0, ·) can have such a term, with
the coefficients c_b of [[def:is-cb]] ([[thm:is-d0]]), which this paper does not determine at a rotating b. Recorded
relative to the order 1, as the terms of ω̇_b(1, 0) at the same root are, these terms need only the offsets
1 + 𝔡₀ + ℕ₀, and the index sets ℰ^φ_ind and ℰ^(ι,φ)_ind obtained so omit 𝔡₀ and serve whatever c_b is
([[thm:is-flat-serves]]). With them (G) holds for every ε_K < μ♭_Z, where μ♭_Z > ε_Υ ([[cor:is-flat]]).
```

### T13. thm:uc-reduction (iii), chapter 71 lines 2583–2588

Old (6 lines):

```old
(iii) N_Λ, k̄_0, l_*, J_* and the admissible ε_K (through (G)) are fixed by the exponents and logarithmic orders of the
index sets of [[sec:uc-index-sets]] and by the orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5. For the index
sets as constructed and the least ℰ^C_I, (G) holds exactly for ε_K < μ_Z, where 1.6747856·10⁻¹⁷ < μ_Z < 1.6747859·10⁻¹⁷
([[thm:is-gap]], [[eq:is-mu-z]]); N_Λ ≤ 909,507,124,095,312, k̄_0 = 3 is the least admissible bound and J_* = 15,000,015
([[prop:is-count]]); and l_* = 50 is admissible ([[cor:sp-lstar]]). Memberships and least real parts alone fix no
admissible ε_K ([[prop:uc-no-eps]]).
```

New (8 lines):

```new
(iii) N_Λ, k̄_0, l_*, J_* and the admissible ε_K (through (G)) are fixed by the exponents and logarithmic orders of the
index sets of [[sec:uc-index-sets]] and by the orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5. For the index
sets as constructed and the least ℰ^C_I, (G) holds exactly for ε_K < μ_Z, where 1.6747856·10⁻¹⁷ < μ_Z < 1.6747859·10⁻¹⁷
([[thm:is-gap]], [[eq:is-mu-z]]); N_Λ ≤ 909,507,124,095,312, k̄_0 = 3 is the least admissible bound and J_* = 15,000,015
([[prop:is-count]]); and l_* = 50 is admissible ([[cor:sp-lstar]]). For the index sets ℰ^φ_ind and ℰ^(ι,φ)_ind of
[[def:is-flat-set]], which omit 𝔡₀, (G) holds exactly for ε_K < μ♭_Z, where μ♭_Z > 3.548125563·10⁻¹⁰ > ε_Υ, and
N_Λ ≤ 3,683,190,611 ([[cor:is-flat]]); k̄_0 = 3, l_* = 50 and J_* = 15,000,015 are admissible for them
([[thm:is-flat-serves]]). Memberships and least real parts alone fix no admissible ε_K ([[prop:uc-no-eps]]).
```

### T6. def:uc-choice, the opening and the display eq:uc-choice, chapter 71 lines 2606–2610

Old (5 lines):

```old
**Definition {#def:uc-choice}** (An admissible choice.) At the computational point take ℰ_ind and ℰ^ι_ind as
constructed ([[sec:is]]), ℰ^C_I the least index set satisfying (2)–(3) of [[def:iii-c-3-1]], ℰ_++ the least choice in
[[eq:iii-i8-1-1]] ([[prop:is-ci-pp]]), and

    ε_Υ := 1.4619·10⁻¹⁰,     ε_K := 1.6747·10⁻¹⁷,     ε_+ := 1.67478·10⁻¹⁷,     l_* := 50,     k̄_0 := 3.
```

New (5 lines):

```new
**Definition {#def:uc-choice}** (An admissible choice.) At the computational point take ℰ_ind := ℰ^φ_ind and
ℰ^ι_ind := ℰ^(ι,φ)_ind ([[def:is-flat-set]], [[thm:is-flat-serves]]), ℰ^C_I the least index set satisfying (2)–(3) of
[[def:iii-c-3-1]], ℰ_++ the least choice in [[eq:iii-i8-1-1]], and

    ε_Υ := 1.4619·10⁻¹⁰,     ε_K := 9.99·10⁻¹⁴,     ε_+ := 9.995·10⁻¹⁴,     l_* := 50,     k̄_0 := 3.
```

### T7. lem:uc-admissible, the display eq:uc-deltas, chapter 71 lines 2627

Old (1 lines):

```old
    Δβ_0 := 0.999²ε_K = 1.6713522747·10⁻¹⁷,     Δτ_0 := 0.999ε_Υ = 1.4604381·10⁻¹⁰.                    {#eq:uc-deltas}
```

New (1 lines):

```new
    Δβ_0 := 0.999²ε_K = 9.97002999·10⁻¹⁴,     Δτ_0 := 0.999ε_Υ = 1.4604381·10⁻¹⁰.                      {#eq:uc-deltas}
```

### T8. lem:uc-admissible, proof: the constants, (G) and (G⁺), chapter 71 lines 2633–2638

Old (6 lines):

```old
0 < ε_K < ε_+ < min(δ_♯, ε_ind), and 1.6747·10⁻¹⁷ < 1.67478·10⁻¹⁷ < 1.9413·10⁻⁸ < δ_50, while
δ_♯ = λ_♯ − 3/2 = 0.0099. *(G).* By [[thm:is-gap]], for the set Λ that [[def:iii-i10-1-1]] builds from the index sets
of [[def:uc-choice]], (G) holds if and only if ε_K < μ_Z, and μ_Z > 1.6747856·10⁻¹⁷ > 1.6747·10⁻¹⁷ = ε_K by
[[eq:is-mu-z]]. Also ε_K < ε_Υ, as [[def:iii-i10-1-3]] asks. *(G⁺) and the exactness conditions.* By [[thm:is-gap]],
ι_* + 356327𝔡₀ + 1116082𝔡₁ = 3 + μ_Z has the least real part above 3 of the elements of Λ, and
ε_+ = 1.67478·10⁻¹⁷ < μ_Z ([[eq:is-mu-z]]); so no λ ∈ Λ has real part in (3, 3 + ε_+], which is (G⁺) of
```

New (6 lines):

```new
0 < ε_K < ε_+ < min(δ_♯, ε_ind), and 9.99·10⁻¹⁴ < 9.995·10⁻¹⁴ < 1.9413·10⁻⁸ < δ_50, while
δ_♯ = λ_♯ − 3/2 = 0.0099. *(G).* By [[cor:is-flat]], for the set Λ that [[def:iii-i10-1-1]] builds from the index sets
of [[def:uc-choice]], (G) holds if and only if ε_K < μ♭_Z, and μ♭_Z > 3.548125563·10⁻¹⁰ > 9.99·10⁻¹⁴ = ε_K. Also
ε_K < ε_Υ, as [[def:iii-i10-1-3]] asks. *(G⁺) and the exactness conditions.* By [[cor:is-flat]] and its proof, μ♭_Z is
the least excess above 3 of the real parts of the elements of Λ, and ε_+ = 9.995·10⁻¹⁴ < μ♭_Z; so no λ ∈ Λ has real
part in (3, 3 + ε_+], which is (G⁺) of
```

### T9. lem:uc-admissible, proof: ε and α, chapter 71 lines 2648–2650

Old (3 lines):

```old
δ₄ + ℓ_3 + 2ε < ε_g, where ℓ_3 = α − 4 − ε < ε_K; it exists, as ε_K + ε ≤ 1.6747·10⁻¹⁷ + 1.4619·10⁻¹³ < ε_g. *α.* An
admissible α ≥ 3 is a number in (4 + ε_K − ε′_0, 4 + ε_K], ε′_0 = ½ min(ε_K, ε_+ − ε_K) = ½(ε_+ − ε_K) =
4·10⁻²², off a finite set ([[def:iii-i10-1-3]]), and (A_J), (Ex3) and (Ex4) exclude finitely many more
```

New (3 lines):

```new
δ₄ + ℓ_3 + 2ε < ε_g, where ℓ_3 = α − 4 − ε < ε_K; it exists, as ε_K + ε ≤ 9.99·10⁻¹⁴ + 1.4619·10⁻¹³ < ε_g. *α.* An
admissible α ≥ 3 is a number in (4 + ε_K − ε′_0, 4 + ε_K], ε′_0 = ½ min(ε_K, ε_+ − ε_K) = ½(ε_+ − ε_K) =
2.5·10⁻¹⁷, off a finite set ([[def:iii-i10-1-3]]), and (A_J), (Ex3) and (Ex4) exclude finitely many more
```

### T10. lem:uc-gaps, statement, chapter 71 lines 2669–2671

Old (3 lines):

```old
**Lemma {#lem:uc-gaps}** (The least real parts of the increments.) For the index sets as constructed,
min Re ℰ_ind = min Re ℰ^ι_ind = η_0 = 𝔡₁. Hence [[lem:ec-counts]] (d) and (e) hold with 𝔡₁ in place of ε_Υ, and
[[prop:ec-upper]] holds with
```

New (3 lines):

```new
**Lemma {#lem:uc-gaps}** (The least real parts of the increments.) For the index sets as constructed, and for those of
[[def:uc-choice]], min Re ℰ_ind = min Re ℰ^ι_ind = η_0 = 𝔡₁. Hence [[lem:ec-counts]] (d) and (e) hold with 𝔡₁ in place
of ε_Υ, and [[prop:ec-upper]] holds with
```

### T11. lem:uc-gaps, proof: the first sentences, chapter 71 lines 2675–2677

Old (3 lines):

```old
*Proof.* By [[eq:is-low]] the least exponent of ℰ_ind is 𝔡₁; by [[prop:is-iota]] the exponents of ℰ^ι_ind of real part
at most 5 are those of ℰ_ind, the integers 1, …, 5 and numbers of real part greater than 3; so both least real parts
are 𝔡₁, and η_0 = 𝔡₁ ([[prop:is-count]] (c)). The proof of [[lem:ec-counts]] (d) uses ε_Υ only as a lower bound for
```

New (5 lines):

```new
*Proof.* By [[eq:is-low]] the least exponent of ℰ_ind is 𝔡₁; by [[prop:is-iota]] the exponents of ℰ^ι_ind of real part
at most 5 are those of ℰ_ind, the integers 1, …, 5 and numbers of real part greater than 3; so both least real parts
are 𝔡₁, and η_0 = 𝔡₁ ([[prop:is-count]] (c)). For ℰ^φ_ind and ℰ^(ι,φ)_ind both least real parts are 𝔡₁, and η_0 = 𝔡₁,
by [[lem:is-flat-memberships]] (c) and [[thm:is-flat-serves]]. The proof of [[lem:ec-counts]] (d) uses ε_Υ only as a
lower bound for
```

### T12. lem:uc-lambda, statement and proof, chapter 71 lines 2685–2700

Old (16 lines):

```old
**Lemma {#lem:uc-lambda}** (The numbers of [[def:iii-i10-1-1]].) At the choice of [[def:uc-choice]]:

(a) N_Λ = #(Λ ∩ {Re < 3 + ε_+}) is an integer with N_Λ ≤ N̄_Λ := 909,507,124,095,312;

(b) k̄_0 = 3, l_* = 50, η_0 = 𝔡₁ and J_* = 15,000,015, so that J′ := (J_* + 1)(l_* + 1) = 765,000,816;

(c) listed in an order of non-decreasing real part as λ_1, …, λ_(N_Λ), the elements of Λ ∩ {Re < 3 + ε_+} have n(λ_i) ≤
i − 1 and k̄(λ_i) ≤ k̄_0 + J′i ≤ k̄_max := k̄_0 + J′N̄_Λ = 695,773,692,090,726,941,774,595;

(d) d_Φ = 62N_Λ + 2 ≤ d̄_Φ := 62N̄_Λ + 2 = 56,389,441,693,909,346, and d_FM, d_Ψ ≤ 62N̄_Λ + 10 = 56,389,441,693,909,354.

*Proof.* (a) is [[prop:is-count]] (a). (b) [[prop:is-count]] (b), (c) give k̄_0 = 3 as the least admissible bound,
η_0 = 𝔡₁ and J_* = 15,000,015; l_* = 50 is admissible by [[cor:sp-lstar]] (a); and 15,000,016 · 51 = 765,000,816. (c)
The λ′ ∈ Λ with Re λ′ < Re λ_i lie in Λ ∩ {Re < 3 + ε_+} and come before λ_i in the list, so n(λ_i) ≤ i − 1; then
[[def:iii-i10-1-1]] gives k̄(λ_i) = k̄_0 + J′(n(λ_i) + 1) ≤ k̄_0 + J′i, and i ≤ N_Λ ≤ N̄_Λ. (d) is [[lem:uc-phi-loss]]
with (a), as 62 · 909,507,124,095,312 = 56,389,441,693,909,344. ∎
```

New (18 lines):

```new
**Lemma {#lem:uc-lambda}** (The numbers of [[def:iii-i10-1-1]].) At the choice of [[def:uc-choice]]:

(a) N_Λ = #(Λ ∩ {Re < 3 + ε_+}) is an integer with N_Λ ≤ 3,683,190,611 < N̄_Λ := 77,112,616,084;

(b) k̄_0 = 3, l_* = 50, η_0 = 𝔡₁ and J_* = 15,000,015, so that J′ := (J_* + 1)(l_* + 1) = 765,000,816;

(c) listed in an order of non-decreasing real part as λ_1, …, λ_(N_Λ), the elements of Λ ∩ {Re < 3 + ε_+} have n(λ_i) ≤
i − 1 and k̄(λ_i) ≤ k̄_0 + J′i ≤ k̄_max := k̄_0 + J′N̄_Λ = 58,991,214,228,154,724,547;

(d) d_Φ = 62N_Λ + 2 ≤ d̄_Φ := 62N̄_Λ + 2 = 4,780,982,197,210, and d_FM, d_Ψ ≤ 62N̄_Λ + 10 = 4,780,982,197,218.

*Proof.* (a) N_Λ ≤ 3,683,190,611 is [[cor:is-flat]], as ε_+ < μ♭_Z. N̄_Λ is taken larger, so that 4k̄_max + 24 exceeds
I_base + 22,119 ([[prop:uc-dependence]], [[eq:cs-iterations]]): with R_b = 10,030,060,100,152 ([[eq:uc-levels]]),
I_base + 22,119 = 235,964,856,912,243,213,665 < 235,964,856,912,618,898,212 = 4k̄_max + 24. (b) [[thm:is-flat-serves]]
gives that k̄_0 = 3, η_0 = 𝔡₁, J_* = 15,000,015 and l_* = 50 are admissible; and 15,000,016 · 51 = 765,000,816. (c) The
λ′ ∈ Λ with Re λ′ < Re λ_i lie in Λ ∩ {Re < 3 + ε_+} and come before λ_i in the list, so n(λ_i) ≤ i − 1; then
[[def:iii-i10-1-1]] gives k̄(λ_i) = k̄_0 + J′(n(λ_i) + 1) ≤ k̄_0 + J′i, and i ≤ N_Λ ≤ N̄_Λ. (d) is [[lem:uc-phi-loss]]
with (a), as 62 · 77,112,616,084 = 4,780,982,197,208. ∎
```

### T16. thm:tr-transfer (iii), chapter 71 lines 5587–5588

Old (2 lines):

```old
for any ε_K, ε_+ with 0 < ε_K < ε_+ < μ(h), the choice of [[def:uc-choice]] with these ε_K and ε_+, and that
of [[def:cs-choices]], is admissible, and d_acc ≤ d_R ≤ D_acc, d_NM ≤ D_NM and N_NM ≤ 21D_NM + 6, with D_acc and D_NM of
```

New (3 lines):

```new
for any ε_K, ε_+ with 0 < ε_K < ε_+ < μ(h), the choice of [[def:uc-choice]] with these ε_K and ε_+ and with the
index sets as constructed, and that of [[def:cs-choices]], is admissible, and d_acc ≤ d_R ≤ D_acc, d_NM ≤ D_NM and
N_NM ≤ 21D_NM + 6, with D_acc and D_NM of
```

## 7. Crosswalk

New rows for the crosswalk of chapter 71, one per bullet; in the file the four fields (label, source, source name,
note) are separated by tabs. Insert them after the row of thm:is-d0, in this order. The source lines are those of this
file at ace76b95, the version the review read. In this revision the same labels are at lines 405, 410, 444, 461, 470,
472, 480, 526, 566; the texts of rem:is-cb-open and lem:is-flat-uses differ from ace76b95 by n2, n3 and m2. If the
merge cites the commit that carries this revision, take these lines instead.

- prop:is-cb-normal | paper/reader/proofs/P-D0.md@ace76b95:356 | P-D0, Proposition (The coefficients c_b in normal form.)
  | new; O(4)-equivariance with reflections reduces c_b on ker ad_A to one function 𝔠(m, a₁, a₂), odd in a₁, even in a₂
- eq:is-cb-normal | paper/reader/proofs/P-D0.md@ace76b95:361 | P-D0, display of prop:is-cb-normal | new
- rem:is-cb-open | paper/reader/proofs/P-D0.md@ace76b95:395 | P-D0, Remark (What the coefficients c_b depend on, and what
  would decide them.) | new; c_b depends on γ_(Υ,H), ζ_∞, χ (free) and e_Υ, γ_Υ; (AP3) undecided at the point; 𝔠 ≡ 0 not
  decidable by values
- def:is-flat-set | paper/reader/proofs/P-D0.md@ace76b95:411 | P-D0, Definition (The index sets ℰ^φ_ind and ℰ^(ι,φ)_ind.)
  | new; the ℰ′_ind of the proof of thm:is-d0 (c), named; ℰ_(𝔡₀)
- eq:is-flat-d0 | paper/reader/proofs/P-D0.md@ace76b95:420 | P-D0, display of def:is-flat-set | new
- lem:is-flat-memberships | paper/reader/proofs/P-D0.md@ace76b95:422 | P-D0, Lemma (The memberships with ℰ^φ_ind.) | new;
  ω̇_b(0, ·), ġ^Υ_b(0, ·) in ℰ^φ_ind ∪ ℰ_(𝔡₀); 1 + ℰ_(𝔡₀) ⊂ ℰ^φ_ind; 𝔡₀ ∉ π_1
- eq:is-flat-memb | paper/reader/proofs/P-D0.md@ace76b95:430 | P-D0, display of lem:is-flat-memberships | new
- lem:is-flat-uses | paper/reader/proofs/P-D0.md@ace76b95:476 | P-D0, Lemma (The uses of the memberships of ω̇_b(0, ·)
  and ġ^Υ_b(0, ·).) | new; every citation of prop:iii-f3-2-2 (1)–(2), eq:iii-f3-2-2, eq:iii-f3-4-2 listed, lem:iii-i7-4-1
  among them (P-D0 review); only (i) 𝒢, (ii) ℰ_col, (iii) weights
- thm:is-flat-serves | paper/reader/proofs/P-D0.md@ace76b95:516 | P-D0, Theorem (Index sets without the offset 𝔡₀.) |
  new; ℰ^φ_ind, ℰ^(ι,φ)_ind serve whatever c_b is; Λ^φ ⊂ Λ; increments below 3/2 generated by 𝔡₁, 1, 1 + δ′₁, 1 + δ₂, 1 +
  𝔡₀, 1 + 2𝔡₀

Notes to append to existing rows: cor:is-flat ("P-D0 T3: hypothesis c_b = 0 replaced by the index sets of
thm:is-flat-serves"), def:uc-choice and lem:uc-admissible ("P-D0 T6–T9: ℰ^φ_ind, ε_K = 9.99·10⁻¹⁴, ε_+ = 9.995·10⁻¹⁴"),
lem:uc-gaps (T10, T11), lem:uc-lambda (T12: N̄_Λ = 77,112,616,084), thm:uc-reduction (T13), sec:is (T1),
sec:is-smaller (T2), rem:is-summary (T4), rem:uc-offset-d0 (T5), eq:uc-choice ("P-D0 T6: ε_K = 9.99·10⁻¹⁴, ε_+ =
9.995·10⁻¹⁴"), eq:uc-deltas ("P-D0 T7: Δβ_0 = 9.97002999·10⁻¹⁴"), thm:is-d0 ("P-D0 review: title qualified; last
sentence of (c) points to thm:is-flat-serves"; T14, T15), thm:tr-transfer ("P-D0 review: (iii) with the index sets
as constructed"; T16).

## 8. Checks run

- Every old text was read from chapter 71 at HEAD 99e16794 at the stated lines and asserted equal before
  replacement; the four lines of cor:is-flat that T3 retypes (y = 1.4901 … *The elements of Z₃.*) were asserted equal
  to the chapter, and n1 was asserted to occur once in T3's verbatim tail.
- A scratch copy of the reader directory at HEAD with T1–T16 applied: lint --chapters 62 files, 5072 labels, 0 hits;
  assemble --check: 5072 labels, 0 problems; assemble (in the scratch copy) then lint --paper: 0 hits, and no line of
  the assembled paper exceeds 121 characters. Every new line has at most 121 characters, and no wrapped line starts
  with a Markdown marker.
- The same scratch copy with the nine rows of section 7 inserted after thm:is-d0 in the crosswalk of chapter 71:
  every label of chapter 71 has exactly one row, the rows are in the chapter's order, and each has four fields.
- The chain formulas of prop:uc-dependence, coded in exact rational arithmetic, reproduce the chapter's D_acc, D_NM and
  21D_NM + 6 at the present choice to every digit; section 4 is their value at the new inputs.
- Section 2.2 is a numerical observation (50-digit arithmetic with finite differences, not certified); no proof uses it.
