# P-RI: the index-0 step of prop:iv6-1-1 (chapter 33), proved

This is a proof file for the coordinator. No file was written in chapters/ or crosswalk/, and none in proofs/ except
this one. Every old text below is copied from the chapters at HEAD, after the P-ADM and P-G1 merges:
- chapters/33-s14-constraint-damping.md, md5 d2184d75289047ef76ee866214fda5d0, last changed at the P-G1 merge
  (86df0ccb, which added sec:iv5-calc);
- chapters/34-s15-linearised.md, md5 5dbbf88718c43171095a90cf0a4009c8, last changed at the P-ADM merge (54350a5d).

Both are also the working-tree files. Each old text occurs exactly once in its chapter, as whole lines, and the line
numbers are those of these files. The crosswalk rows are those of crosswalk/33-s14-constraint-damping.tsv (md5
5b4e25fe9509983f89fa7072a9d2ac89) and crosswalk/34-s15-linearised.tsv (md5 6995e64abbb9be09675faa8c8b9efc3a). The
texts were applied to scratch copies and checked there (section 7).

## 1. Summary

**The gap.** The index-0 part of the proof of prop:iv6-1-1 moves the b-weight at r = 0 sector by sector. It reads the
change of index off thm:std-relative-index ([Mel93, Theorem 6.5]), which is stated for b-elliptic operators on a compact
manifold with boundary. At r = ∞ the operator is a scattering operator with radial sets, so the theorem does not cover
the step. The rewrite also closes two further points in the old text:
- Step (ii) asserts the Fredholm property at a weight β₁ that is root-free for one sector only. But the estimates of the
  chapter, and those of chapter 22, need a weight that is root-free for the whole indicial family.
- Steps (i) and (iii) need the rank of each root (the dimension of its formal solutions) to equal its multiplicity as a
  zero of the determinant of the sector's indicial matrix.

**The route: (iii).** It is route (i) as the paper already carries it out. Chapter 34 proves the relative index formula
that route (i) asks for. It does so for the transition face normal operator N_tf(P̂, e^(iθ)) of any P̂ satisfying
(H1)–(H2), on the spaces of thm:i-c-4-3.
- **lem:iii-f1-3-1 (Relative index).** For tf weights β_1 < β_2 < β_1 + 1, neither the real part of a root,
  ind(β_2) − ind(β_1) = dim F.
  - Its Steps 1–2 are the localisation at r = 0: a Mellin contour shift with residues, the formal solutions cut off near
    ztf, and a right inverse of the normal operator on a line.
  - It restricts to steps of width < 1. That is why formal solutions of the normal operator alone are enough, and no
    higher-order formal solutions are needed.
  - Its *Multiplicity* paragraph proves that the rank equals the order of vanishing of the determinant, on each isotypic
    block, by the Smith form over the ring of germs of holomorphic functions. This is the identity rank = ord det that
    the reader of P-G24b (R-P-G24b, M1 (β)) and the coordinator's note ask for. It is stated and proved there, in the
    generality needed here.
  - Its statement asks only s ∈ ℤ. But Steps 1–2 take the Mellin transform of an element of H^(s−2)_b, which the paper
    defines (sec:i-c-2-3, eq:i-c-2-1) only for weighted L² functions, so the proof needs s ≥ 2. P-RI-3 adds s ≥ 2 to
    the hypothesis. Every use of the lemma meets it, the new one included (section 4, "Uses of lem:iii-f1-3-1").
- **lem:iii-f1-2-4 (Roots in a strip, uniformly) and *Types and representations* (sec:iii-f1-1).** Together they reduce
  the count to the type-wise matrices, uniformly in a compact parameter set.
- **The proof of prop:iii-f1-3-3 (iii).** It deforms chapter 34's operator to the free operator, using the invariant
  G(τ) = ind_τ(β″) − Σ_π (n_π(τ, β″) − dim W_π). That argument never needs a weight below all roots.

The new text runs the same argument for □^C_b, with γ_C deformed to 0 and s := 2. As the coordinator's note asks, it
combines this with chapter 33's own counts, lem:iv4-1-3 (a) and prop:np-10-54 (i), which count the roots of P_0, P_l and
p_(v) with multiplicity. Every weight it uses is root-free for the whole indicial family. So the Fredholm property at
every λ comes directly from thm:i-c-4-3 (3).

**Options weighed.**
- **Route (i), written out in chapter 33.** This means a sector-wise Mellin lemma plus a companion-matrix or Smith-form
  count. It works, and I drafted it. But it duplicates lem:iii-f1-3-1, and it still needs a separate argument for the
  Fredholm property at weights that are root-free for one sector only. Section 3.6 describes the draft; it is not
  proposed.
- **Route (ii), a homotopy at fixed weight to an invertible model.** It fails as stated. As h⁻¹ runs from 0 to h_f⁻¹,
  the paper proves nothing about the roots at intermediate h. So it cannot exclude that a root of the sector crosses
  the fixed weight line during the deformation, which would break the Fredholm property. The invariant G is what makes
  the deformation work, and G needs the relative index formula.
- **Route (iii), the paper's own lemmas.** Chosen. Two texts of chapter 33 change, and one hypothesis of chapter 34 is
  made explicit (P-RI-3). No label is added, and no new Appendix A entry is needed.

**Not circular.**
- lem:iii-f1-3-1 and lem:iii-f1-2-4 are general lemmas. Their proofs use thm:i-c-4-3, lem:i-c-2-3 to lem:i-c-2-5,
  eq:i-c-2-1 and eq:i-c-2-2 (chapter 22), and the representation theory of SO(4) in sec:iii-f1-1 (with the type bases of
  chapter 30, eq:iii-a1-2-9). They use nothing of chapter 33.
- Chapter 34 cites chapter 33 in several places, but none of them in lem:iii-f1-2-4, lem:iii-f1-3-1, *Types and
  representations* or the *Weights* paragraph of sec:iii-f1-3, which are what the new text uses; these four use none of
  the data that chapter 34 fixes. The results of chapter 33 that rest on prop:iv6-1-1 reach chapter 34 by two routes:
  - thm:iv6-3-1 and thm:iv6-4-1, hence thm:iii-e-1-1 (4), which chapter 34 uses only at Step 4 of
    prop:iii-f1-3-3 (ii) (line 739);
  - the threshold h_tf of thm:iv6-3-1, which enters the bound h_* of eq:iv4-0-1 and so the constraint damping data
    that chapter 34 fixes "in sec:iv4-0" (lines 75–77).
  Neither route reaches the four pieces above. And prop:iv6-1-1 holds for every h ∈ (0, 10⁻⁶] (sec:iv6-0), not only
  for h below h_*. The other citations of thm:iii-e-1-1 in chapter 34 are of its setting (lines 77, 212, 275, 281,
  1935) and of its clauses (1)–(3) (lines 285, 1148, 1500, 1937).
- Chapter 33 already cites chapter 34 (prop:iii-f1-2-3, sec:iii-f1-1, lem:iii-f-2-1, eq:iii-f1-2-2).
- If the coordinator prefers no forward citation in a proof step, the "Weights" paragraph of sec:iii-f1-3, lem:iii-f1-2-4
  and lem:iii-f1-3-1 can move unchanged to chapter 22, after thm:i-c-4-3. That is an editorial choice; correctness does
  not need it.

## 2. The new chapter text

No new lemma is needed. The index-0 part of the proof of prop:iv6-1-1 becomes the text below; it ends the proof, so it
ends with ∎. The overview sentence of sec:iv6 now names the formula used, and lem:iii-f1-3-1 states s ≥ 2. Section 4
gives the exact old and new texts.

```text
*Index 0.* As the index does not depend on the admissible orders, we find it for s := 2, the given β and ℓ the order
of [[ch:s03]] for the free operator at this σ = e^(iθ): that of [[lem:i-a-7-1]] with ϑ_in = 0 and S̄ = 0 for
θ ∈ {0, π}, which is > −½ at R_in and < −½ at R_out, or a constant 𝗋_mid < −½ for θ ∈ (0, π), where only R_out
enters ([[def:iv6-0-2]]); so it is admissible for every h⁻¹ ≥ 0. For λ ∈ [0, 1] let P̂_λ be the spectral family of
□^C_b with γ_C replaced by λh⁻¹. It satisfies (H1)–(H2) of [[sec:i-a-1-3]], by the proof of [[lem:iv4-1-6]], whose
(H1)–(H2) part does not use the value of γ_C. Its transition
face normal operator N_tf(P̂_λ, ·) is (□^C)^(·) with h⁻¹ replaced by λh⁻¹, by the proof of [[lem:iv6-0-1]] (d); at
λ = 0 it is the spectral family of □_η = 2δ_ηG_ηδ*_η, which acts componentwise in the frame dt, dx^i
([[lem:s14-box-c]], Ric(η) = 0). The thresholds of P̂_λ at R_out and at R_in are −½ + λh⁻¹(1 − e)(1 − v) ≥ −½ and
−½ − λh⁻¹(1 − e)(1 + v) ≤ −½ ([[prop:np-10-21]], [[eq:s14-theta-in]]). So these orders are allowed in
[[thm:i-c-4-3]] (1)–(2) for every λ, and with them the map [[eq:iv6-1-1]], with N_tf(P̂_λ, e^(iθ)) in place of
(□^C)^(σ), is the map 𝒳_(tf,θ) → 𝒴_(tf,θ) of [[sec:i-c-4]] for P̂_λ at q = β ([[sec:iv6-4]]). For γ ∈ ℝ that is
not the real part of an indicial root of P̂_λ(0), let ind_λ(γ) be the index of this map at q = 2 − γ, which is
Fredholm by [[thm:i-c-4-3]] (3); this is the index of [[sec:iii-f1-3]] at the weight γ. The index to be found is
ind_1(2 − β), and 2 − β ∈ [−C_0, 2).

For λ ∈ [0, 1] let I_λ be the indicial family ([[eq:i-c-1-3]]) of P̂_λ(0). It is that of ρ⁻²(□^C)^(0) with h⁻¹
replaced by λh⁻¹ (the proof of [[lem:iv4-1-3]]), of the form of [[lem:i-c-2-4]], with coefficients affine in λ that
commute with the action of SO(4) rotating both 𝕊³ and the Cartesian components. For an irreducible representation π
of SO(4) let W_π, the π-isotypic subspace of C^∞(𝕊³; ℂ⁵), and d(π) be as in [[lem:iii-f1-2-4]]; sums over π below
run over the π with W_π ≠ 0. For γ ∈ ℝ let n_π(λ, γ) be the number of roots of I_λ on W_π with real part < γ, with
multiplicity. By *Types and representations* in [[sec:iii-f1-1]], W_π is ℂ^k ⊗ π for the type and degree of π, with
k = 2 at scalar type 0, k = 3 at scalar type l ≥ 1 and k = 1 at vector type, and I_λ(ι) acts on W_π as N(ι) ⊗ Id_π
for a k × k matrix N(ι). So det(I_λ(ι)|_(W_π)) = det(N(ι))^(dim π), and the roots on W_π are those of det N, each
with its multiplicity multiplied by dim π. At λ = 1, in the basis S dt, S dr, r dS (resp. rV) of [[prop:np-10-12]]
(ii), N is N_0, N_l or N_(v,l), so that det N is h⁻²P_0, h⁻³P_l or h⁻¹p_(v) ([[prop:np-10-12]] (iii)).

Let γ_* := C_0 + 2. By [[lem:iii-f1-2-4]] with 𝒯 = [0, 1], there is d_0 > γ_* such that for every λ and every π
with d(π) ≥ d_0 no root of I_λ on W_π has real part in [−γ_*, γ_*]. For λ ∈ [0, 1] and γ ∈ [−γ_*, γ_*] not the real
part of a root of I_λ put

    G(λ, γ) := ind_λ(γ) − Σ_π (n_π(λ, γ) − dim W_π).

The sum is finite. Each H_d ⊗ ℂ⁵, H_d the harmonics of degree d ((K4) of [[sec:i-c-2-1]]), is invariant under the
action of SO(4), so W_π is the sum of its intersections with these spaces, which vanish for d < d(π). At λ = 0, on
H_d ⊗ ℂ⁵, I_0(ι) = −ι² + 2ι + d(d + 2) = −(ι + d)(ι − d − 2), the free operator acting componentwise (the proof of
[[prop:i-c-5-3]]). So at λ = 0, W_π carries dim W_π roots ≤ −d(π) and dim W_π roots ≥ d(π) + 2; hence
n_π(0, γ) = dim W_π for γ ∈ (0, 2), and for every γ ∈ [−γ_*, γ_*] if d(π) ≥ d_0. In the latter case the roots on
W_π, which depend continuously on λ ([[lem:iii-f1-2-4]]), never have real part in [−γ_*, γ_*], so n_π(λ, γ) = dim W_π
for every λ. So the terms with d(π) ≥ d_0 vanish, and only finitely many π have d(π) < d_0.

G(λ, γ) does not depend on γ. Let γ₁ < γ₂ be two such weights, and choose γ₁ = w_0 < w_1 < … < w_M = γ₂ with
w_(i+1) − w_i < 1, none of them the real part of a root of I_λ; this is possible, as only finitely many roots have
real part in [γ₁, γ₂] ([[lem:i-c-2-4]] (b)). By [[lem:iii-f1-3-1]], applied to each pair (w_i, w_(i+1)) as its
weights (β_1, β_2), ind_λ(w_(i+1)) − ind_λ(w_i) is the number of roots of I_λ with real part in (w_i, w_(i+1)), with
multiplicity. Adding, ind_λ(γ₂) − ind_λ(γ₁) is the number of roots with real part in (γ₁, γ₂), which is the change of
the sum.

G(λ, γ) does not depend on λ. Let λ_0 ∈ [0, 1]. Only the finitely many W_π with d(π) < d_0 carry roots with real part
in [−γ_*, γ_*], and these roots depend continuously on λ; so there is γ ∈ (−γ_*, γ_*) that is not the real part of a
root of I_λ for any λ near λ_0. The terms with the factor λh⁻¹, namely −2iσλh⁻¹ρS̄ in [[eq:iv6-0-2]] and the part of
(□^C)^(0) that comes from λh⁻¹𝓛_c ([[lem:s14-box-c]]), which lies in ρ²Diff¹_b ([[lem:s14-tf-inputs]] (i)), map
H^(s,(ℓ,q))_(sc,b) boundedly into H^(s−2,(ℓ+1,q−2))_(sc,b). So the domain of the map does not depend on λ, the map
is continuous in λ in operator norm, and, being Fredholm, it has an index that is constant near λ_0; and every
n_π(λ, γ) is constant near λ_0, as no root crosses the line Re ι = γ. So G is constant near λ_0, and as [0, 1] is
connected, G(1, ·) = G(0, ·).

At λ = 0 and γ ∈ (0, 2), ind_0(γ) = 0: at ρ = 0, P̂_0 has the data of □_η acting componentwise, so it is
tf-admissible with every weight in (0, 2) ([[prop:i-c-5-3]]), and N_tf(P̂_0, e^(iθ)) is invertible at q = 2 − γ by
[[cor:i-c-5-2]] (a). As n_π(0, γ) = dim W_π for every π, G(0, γ) = 0. At λ = 1 and γ = 2 − β, no indicial root of
P̂_1(0) has real part in [−100, 2) ([[lem:iv4-1-3]] (a)), so n_π(1, 2 − β) is the number of roots on W_π with real
part < −100. With multiplicity, P_0 has two such roots, P_l (l ≥ 1) three and p_(v) one ([[prop:np-10-54]] (i)); so
n_π(1, 2 − β) = k dim π = dim W_π for every π. Hence ind_1(2 − β) = G(1, 2 − β) = G(0, 1) = 0, and the index of
[[eq:iv6-1-1]] is 0. ∎
```

## 3. Notes for the readers (not chapter text)

### 3.1 Each input, and why it applies

- **P̂_λ satisfies (H1)–(H2).** The proof of lem:iv4-1-6 gives both.
  - (H1) comes from the principal symbol of □_(g_b) ⊗ Id, as E^C has order 0.
  - (H2) comes from lem:iv4-1-2, whose proof, from prop:np-10-21 (i), holds for any value of the damping constant.
  - Only the statement "spectrum … all positive" of lem:iv4-1-2 uses γ_C > 0, and (H2) does not ask for it.
  - The (H3) part of that proof does use γ_C: it is lem:iv4-1-5, the horizon threshold, which needs h small. Hence
    "whose (H1)–(H2) part" in the new text. Neither thm:i-c-4-3 nor lem:iii-f1-3-1 asks (H3).
  - At λ = 0, P̂_0 is the spectral family of 2δGδ* = □_(g_b) on 1-forms.
- **N_tf(P̂_λ, ·).** This is lem:iv6-0-1 (d) and its proof.
  - N_tf is built from S_0 and N(P^(0)) only.
  - lem:iv4-1-2 gives these as λh⁻¹S̄ and the normal operator of the model with damping λh⁻¹.
  - thm:i-c-4-3 and lem:iii-f1-3-1 use only these data (first paragraph of sec:iii-f1-3).
- **The orders.** For θ ∈ {0, π} the free order is > −½ at R_in and < −½ at R_out. For θ ∈ (0, π) it is a constant
  𝗋_mid < −½, and def:iv6-0-2 asks a condition at R_out only (σ is not ±1). This stays true after P-G24b's T23, which
  says "For Im σ > 0 nothing is asked off R_out".
  - The thresholds of P̂_λ are −½ + λh⁻¹(1 − e)(1 − v) at R_out and −½ − λh⁻¹(1 − e)(1 + v) at R_in. These are
    prop:np-10-21 (i) and eq:s14-theta-in with λh⁻¹ for h⁻¹.
  - So the order pair of lem:i-a-7-1 with the free thresholds is an admissible 𝗋_± for every P̂_λ: thm:i-c-4-3 (1),
    with θ ∈ {0, π} ⊂ Θ_±.
  - The constant 𝗋_mid < −½ ≤ −½ + λh⁻¹(1 − e)(1 − v) is allowed in thm:i-c-4-3 (2), with I = {θ}.
  - With these orders the map of eq:iv6-1-1 is the map 𝒳_(tf,θ) → 𝒴_(tf,θ) of sec:i-c-4 at q = β. sec:iv6-4
    identifies the spaces for any such orders.
- **s = 2.** lem:iii-f1-3-1 asks s ∈ ℤ, and with P-RI-3 also s ≥ 2.
  - Step 1 of its proof takes the Mellin transform of f := N(L)v ∈ H^(s−2)_(b,c_1), with the line bounds eq:i-c-2-1,
    and Step 2 that of f := χ′r̂²y ∈ H^(s−2)_(b,c_2). sec:i-c-2-3 defines the transform, and eq:i-c-2-1 holds, only for
    v with e^(c_0 t)v ∈ L². So both steps need s − 2 ≥ 0. With s = 2 these f are weighted L² functions.
  - The choice costs nothing: the index of eq:iv6-1-1 does not depend on the admissible (s, ℓ, β), by the paragraph
    before "Index 0" in the proof of prop:iv6-1-1.
- **ind_λ(γ) is the ind of sec:iii-f1-3,** the index at q = 2 − γ, with tf weight γ.
  - lem:iii-f1-3-1 gives ind(β_2) − ind(β_1) = dim F.
  - dim F is the number of roots ι of I with β_1 < Re ι < β_2, with multiplicity. This is its last sentence: "when J is
    an indicial family as in lem:iii-f1-2-4, it is the multiplicity of −μ as a root of I on those components".
  - I_λ is such a family. It has the form of lem:i-c-2-4, by (H2) and eq:i-c-1-3. Its coefficients are affine in λ.
    It is SO(4)-equivariant on 1-forms in the Cartesian frame; lem:iii-f1-2-4 covers T* of ℝ^(1+4) explicitly.
- **W_π and the type-wise matrices.**
  - For 1-forms, *Types and representations* gives W_π = ℂ^k ⊗ π, with k = n_C = 2, 3, 3, 1, 1 at s0, s1, sl, v1, vl
    (sec:iii-f1-2). I_λ acts on it as N ⊗ Id_π.
  - At λ = 1, the map (A, B, C) ⊗ S ↦ A S dt + B S dr + C r dS from ℂ³ ⊗ ℋ_l is SO(4)-equivariant and injective, with
    image of dimension 3 dim π. So its image is W_π.
  - In that basis prop:np-10-12 (ii) gives N = N_l. Its determinant is det N_l = h⁻³P_l, as P_l := det(hN_l)
    (prop:np-10-12 (iii)).
  - Likewise for N_0, with det N_0 = h⁻²P_0.
  - 𝒱_l has two vector-type components, ((l + 1)/2, (l − 1)/2) and ((l − 1)/2, (l + 1)/2). Each has
    N = N_(v,l) = h⁻¹p_(v).
- **The count at λ = 1.** This is the coordinator's "combine with lem:iv4-1-3 (a)".
  - By lem:iv4-1-3 (a), no root has real part in [−100, 2). Here γ = 2 − β ∈ [−C_0, 2) ⊂ [−100, 2). So the roots with
    real part < γ are those with real part < −100.
  - prop:np-10-54 (i) counts them with multiplicity: two for P_0, three for P_l (l ≥ 1), and one for p_(v).
  - On W_π each is multiplied by dim π, which gives k dim π = dim W_π.
  - So every term of the sum is 0 at (1, 2 − β), and G(1, 2 − β) is the index sought.
- **The count at λ = 0.**
  - The free operator acts componentwise, so I_0(ι) = −(ι + d)(ι − d − 2) on H_d ⊗ ℂ⁵ (proof of prop:i-c-5-3).
  - W_π is the sum of its intersections with these invariant spaces, and the intersections are nonzero only for
    d ≥ d(π). So W_π carries dim W_π roots ≤ −d(π) and dim W_π roots ≥ d(π) + 2.
  - Type by type these are the roots of lem:iii-a1-2-3 on 1-forms. With the sign changed, they are those of
    lem:s14-tf-inputs (v).
  - For γ ∈ (0, 2) every term is 0.
  - ind_0(γ) = 0 by prop:i-c-5-3 and cor:i-c-5-2 (a): the free gap is (0, 2), and q = 2 − γ ∈ (0, 2).
  - The end of the proof evaluates G at λ = 0 at the weight 1. It lies in (0, 2) and in [−γ_*, γ_*], and it is
    root-free at λ = 0, the roots there being the integers −d ≤ 0 and d + 2 ≥ 2. The weight 2 − β of the λ = 1 end need
    not be root-free at λ = 0: for β = 2 it is 0 = −d at d = 0.
- **Finiteness and continuity.**
  - lem:iii-f1-2-4, with its X taken to be γ_* = C_0 + 2, gives d_0, taken > γ_*. Beyond it, no root on W_π meets
    {|Re ι| ≤ γ_*}, for any λ. The new text writes γ_* rather than X because X := [ℝ̄⁴; {0}] is the manifold of
    sec:iv6-0, on which the spaces of this proof live.
  - The roots on each W_π depend continuously on λ: the determinant there has degree 2 dim W_π and leading coefficient
    (−1)^(dim W_π).
  - So the terms with d(π) ≥ d_0 vanish for all λ. And near any λ_0 there is one weight γ ∈ (−γ_*, γ_*) that is
    root-free for all λ near λ_0.
- **Local constancy of ind_λ(γ).**
  - The λ-dependent terms of N_tf(P̂_λ, e^(iθ)) are −2iσλh⁻¹ρS̄ (eq:iv6-0-2) and λh⁻¹ times the stationary part of
    𝓛_c (lem:s14-box-c).
  - The stationary part of 𝓛_c is a first-order operator. Its coefficients of order k are homogeneous of degree k − 2
    (lem:s14-tf-inputs (i), which the new text cites at this point). So r² times it is a dilation-invariant element of
    Diff¹_b(X), and it lies in ρ²Diff¹_b.
  - Both terms map H^(s,(ℓ,q))_(sc,b) into H^(s−1,(ℓ+1,q−2))_(sc,b). At the scattering end, ρ²Diff¹_b ⊂ ρDiff¹_sc.
    Near r = 0, ρ = r⁻¹ lowers the b-weight by 1, and ρ² lowers it by 2.
  - So the domain does not depend on λ, and the family is affine in λ in operator norm.
  - A norm-continuous family of Fredholm operators has locally constant index. Chapters 20, 22 and 34 use this too.

### 3.2 What the new text replaces, and why the old steps could not be kept

- **Steps (i) and (iii).** The old text cites [Mel93, Theorem 6.5] outside its hypotheses. lem:iii-f1-3-1 replaces it.
- **Step (ii).** The old text claims the Fredholm property at β₁ "by the estimates above". There β₁ lies below all roots
  of one sector, for all h⁻¹.
  - Those estimates, like thm:i-c-4-3, need β − 2 not to be the real part of any root of the full family.
  - β₁ is not of that kind in general: it is chosen from one sector's roots, and nothing in the paper places the other
    sectors' roots at intermediate h⁻¹, so the line Re ι = β₁ − 2 cannot be shown root-free for the whole family.
  - The new text uses only weights that are root-free for the whole family, at each λ.
- **The counts.** The old counts "with multiplicity" (j = 2, 3, 1 per sector) left out the multiplicity dim π of the
  harmonics. This did not affect the conclusion, as the same factor occurs on both sides. The new count is per isotypic
  block, with the factor dim π explicit.

### 3.3 Repairs inside the rewritten sentence

The old sentence reads "that of [[lem:i-a-7-1]] with θ_in = 0 and S̄ = 0 for θ ∈ {0, π}, or r_mid for θ ∈ (0, π). It is
invariant under the rotations of 𝕊³, > −½ at R_in and < −½ at R_out, so it is admissible for every h⁻¹ ≥ 0".
- The threshold of lem:i-a-7-1 is ϑ_in, so the new sentence writes "ϑ_in = 0".
- The constant order of chapter 22 is 𝗋_mid (cor:i-c-5-2 (b)), so the new sentence writes "a constant 𝗋_mid < −½".
- "> −½ at R_in and < −½ at R_out" is true of the order for θ ∈ {0, π} only; the constant 𝗋_mid is < −½ everywhere.
  The conclusion holds, because for θ ∈ (0, π) def:iv6-0-2 asks nothing at R_in. The new sentence attaches the clause
  to θ ∈ {0, π} and says, for θ ∈ (0, π), that only R_out enters.

### 3.4 Effect on other items

- **lem:s14-tf-inputs (v).** Only the old step (iii) cited it (line 3043). After the change no chapter cites it. It stays
  correct; the coordinator may keep it as a check of the λ = 0 count, or remove it. The new text cites
  lem:s14-tf-inputs (i).
- **thm:std-relative-index.** It stays in Appendix A. The overview sentence of sec:iv6 cites it as attribution: it is the
  formula for b-elliptic operators on compact manifolds with boundary. No proof step uses it. Before the change no
  chapter cites the label; the old step (i) cites "[Mel93, Theorem 6.5]" directly.
- **The sector decomposition.** prop:iv6-1-1 no longer uses it, and no longer cites ch:s11.
  - Nothing else in chapter 33 depends on the removed sentences.
  - Elsewhere in the chapter, "sector" occurs only in lem:s14-tf-inputs (v) (lines 2823–2824) and, at line 3169 in
    thm:iv6-3-1, as an angular sector of σ; P-G24b's T39 rewrites that line without the word.
- **lem:iii-f1-3-1.** P-RI-3 adds s ≥ 2 to its hypothesis. Its proof is unchanged, and every use meets the hypothesis
  (section 4).
- **P-G24b.** This file settles its §6.1 (its lines 1475–1499), the row of its §2 table for [Mel93, Thm 6.5] and
  [Hin26a, p. 91] (its line 127, at chapter lines 2412–2413 of md5 147ca162…, which are lines 3033–3034 at HEAD), and
  the (c) item of its summary (its lines 16–17). The two citations of the old step (i), [Mel93, Theorem 6.5] and
  [Hin26a, p. 91], go with the old text.

### 3.5 The coordinator's note

For route (i), the note asks for an identity: the rank of an indicial root equals the order of vanishing of the
determinant of the indicial family there. The note asks for it to be stated and proved in the paper, or quoted, and
combined with lem:iv4-1-3 (a).
- **The paper proves the identity.** It is the *Multiplicity* paragraph of the proof of lem:iii-f1-3-1.
  - On each isotypic block it writes J = E diag((ι − μ)^(k_i)) F′, the Smith form.
  - The space F_μ of formal solutions at μ then has dimension Σ k_i = ord_μ det J.
- **The localisation (α) of R-P-G24b M1** is Steps 1–3 of the same proof.
- **The new text** cites lem:iii-f1-3-1 for both. At λ = 1 it combines them with lem:iv4-1-3 (a) and
  prop:np-10-54 (i).
- So no Appendix A quotation is needed.

### 3.6 The self-contained alternative (drafted, not proposed)

The draft works in one sector, with coefficient space 𝔼 and indicial family J(μ) = −μ² + μa + b at r = 0.
1. **Formal solutions.** The space of formal solutions r^μ p(log r) at μ has dimension ord_μ det J. The reason: the
   companion matrix of the Euler system has characteristic polynomial (−1)^(dim 𝔼) det J, and the formal solutions at μ
   correspond to its generalised eigenspace.
2. **The domain.** For β − β₁ ≤ 1, the Mellin argument gives {u ∈ X_β₁ : Pu ∈ Y_β} = X_β ⊕ χF.
3. **The index.** An elementary computation then gives the relative index formula, given the Fredholm property at β₁. It
   uses two facts: Y_β is dense, so the range at β₁ meets Y_β in a subspace of the same codimension; and the domain is
   a finite-dimensional extension of X_β.
4. **The Fredholm property at β₁.** At a weight root-free for the sector only, it needs either a sector version of
   lem:i-c-2-6 or a detour through a weight that is root-free for the whole family.

All of this is lem:iii-f1-3-1 again, so it is not proposed.

## 4. Placement

Each old text is quoted exactly between the fences, as whole lines, and each new text replaces it as a whole, with the
line breaks shown. The three texts are pairwise disjoint and may be applied in any order.

### P-RI-1. The overview of sec:iv6 (chapter 33, lines 2791–2792)

Old (2 lines):

```text
three steps, as in [Hin26a, Appendix B, pp. 85–98]: the Fredholm property and index 0 ([[sec:iv6-1]]), by radial
estimates and Melrose's relative index theorem, sector by sector on 𝕊³; solvability on edge-b spaces
```

New (4 lines):

```text
three steps, as in [Hin26a, Appendix B, pp. 85–98]: the Fredholm property and index 0 ([[sec:iv6-1]]), by radial
estimates and the relative index formula of [[lem:iii-f1-3-1]] (for b-elliptic operators on compact manifolds with
boundary this is Melrose's [[thm:std-relative-index]]), with the indicial roots counted by type and degree on 𝕊³;
solvability on edge-b spaces
```

The next line is unchanged: "([[sec:iv6-2]]), by the arguments of [[sec:iv5]]; and the kernel argument of [Hin26a,
Section B.4] ([[sec:iv6-3]])."

### P-RI-2. prop:iv6-1-1, the index-0 part of the proof (chapter 33, lines 3017–3049)

Old (33 lines, from "*Index 0.*" to the end of the proof):

```text
*Index 0.* (□^C)^(σ) commutes with the rotations of 𝕊³, and with the dilations up to the factor of (a). Decompose
sections of 𝒯*_X by harmonics on 𝕊³ ([[ch:s11]]): scalar type of degree l ≥ 0 (three components for l ≥ 1, the dt, dr
and gradient parts; two for l = 0), and vector type of degree l ≥ 1 (one component, the co-closed 1-forms on 𝕊³). The
projections onto a type and degree are bounded on the spaces with rotation-invariant orders (the proof of
[[prop:i-c-5-3]]), and (□^C)^(σ) commutes with them. So [[eq:iv6-1-1]] is the direct sum of its restrictions to the
sectors. Each restriction is Fredholm, and only finitely many have nonzero kernel or cokernel, as the kernel and the
cokernel of the sum are finite-dimensional. Fix a sector and write I
for its index on [[eq:iv6-1-1]], with ℓ a variable order > −½ at R_in and < −½ at R_out. Take for ℓ the order of
[[ch:s03]] for the free operator at this σ = e^(iθ): that of [[lem:i-a-7-1]] with θ_in = 0 and S̄ = 0 for θ ∈ {0, π},
or r_mid for θ ∈ (0, π). It is invariant under the rotations of 𝕊³, > −½ at R_in and < −½ at R_out, so it is admissible
for every h⁻¹ ≥ 0; as the index does not depend on the admissible orders, I is the index of the sector for all of them.

(i) *Lowering β.* In the sector, (□^C)^(0) has finitely many indicial roots at r = 0, continuous in
h⁻¹ ∈ [0, h_f⁻¹], h_f ∈ (0, 10⁻⁶] the value at hand ([[eq:iv6-0-2]]: they are the roots of the sector's indicial
polynomial, whose coefficients are polynomial in h⁻¹ with leading coefficient free of it). Fix β₁ below all of them for
all such h⁻¹. Moving the weight from β to β₁ raises the index by the number of roots, with multiplicity, whose real
part lies in [β₁ − 2, β − 2). This is Melrose's relative index theorem [Mel93, Theorem 6.5], a theorem on b-operators
in every dimension ([Hin26a, p. 91]). These are the roots −ι with Re ι ≥ 2: two in the scalar sector l = 0, three in
each scalar sector l ≥ 1, one in each vector sector ([[lem:iv4-1-3]] (a)). The index becomes I + j, with j = 2, 3, 1.

(ii) *Removing the damping.* Deform h⁻¹ to 0 at the weight β₁. The family is continuous in operator norm between the
fixed spaces, as the h⁻¹-terms (2iσρh⁻¹S̄, and the first-order part h⁻¹ρ²Q̃ of (□^C)^(0) from L_h) map H^(s,(ℓ,β₁))
boundedly to H^(s−2,(ℓ+1,β₁−2)). It stays Fredholm, by the estimates above, whose thresholds hold for every h⁻¹ ≥ 0
with this ℓ and whose weight β₁ stays root-free. So the index I + j is kept at h⁻¹ = 0. There the operator is
2δ_ηG_ηδ*_η = □_η on 1-forms (Ric(η) = 0, [[lem:s14-box-c]]), acting componentwise in the frame dt, dx^i.

(iii) *Raising β for the free operator.* Its roots at r = 0 are those of [[lem:s14-tf-inputs]] (v), and the window
between the groups contains (−2, 0). Raising β₁ to β₂ with β₂ − 2 ∈ (−2, 0) crosses 2, 3 or 1 roots and lowers the
index by as many, to I. On these spaces (□_η)^(σ) is invertible: it is N_tf of the free operator, which is
tf-admissible with every weight in (0, 2) ([[prop:i-c-5-3]], whose data are those of □_η componentwise). By
[[cor:i-c-5-2]] (a) it is invertible on the spaces of [[sec:i-c-4]] with q ∈ (0, 2), the free gap being (0, 2), and
these are the spaces here with β = q and ℓ the order fixed above ([[sec:iv6-4]]); take β₂ := q. So I = 0 in every
sector, and the index of [[eq:iv6-1-1]] is 0. ∎
```

New (64 lines):

```text
*Index 0.* As the index does not depend on the admissible orders, we find it for s := 2, the given β and ℓ the order
of [[ch:s03]] for the free operator at this σ = e^(iθ): that of [[lem:i-a-7-1]] with ϑ_in = 0 and S̄ = 0 for
θ ∈ {0, π}, which is > −½ at R_in and < −½ at R_out, or a constant 𝗋_mid < −½ for θ ∈ (0, π), where only R_out
enters ([[def:iv6-0-2]]); so it is admissible for every h⁻¹ ≥ 0. For λ ∈ [0, 1] let P̂_λ be the spectral family of
□^C_b with γ_C replaced by λh⁻¹. It satisfies (H1)–(H2) of [[sec:i-a-1-3]], by the proof of [[lem:iv4-1-6]], whose
(H1)–(H2) part does not use the value of γ_C. Its transition
face normal operator N_tf(P̂_λ, ·) is (□^C)^(·) with h⁻¹ replaced by λh⁻¹, by the proof of [[lem:iv6-0-1]] (d); at
λ = 0 it is the spectral family of □_η = 2δ_ηG_ηδ*_η, which acts componentwise in the frame dt, dx^i
([[lem:s14-box-c]], Ric(η) = 0). The thresholds of P̂_λ at R_out and at R_in are −½ + λh⁻¹(1 − e)(1 − v) ≥ −½ and
−½ − λh⁻¹(1 − e)(1 + v) ≤ −½ ([[prop:np-10-21]], [[eq:s14-theta-in]]). So these orders are allowed in
[[thm:i-c-4-3]] (1)–(2) for every λ, and with them the map [[eq:iv6-1-1]], with N_tf(P̂_λ, e^(iθ)) in place of
(□^C)^(σ), is the map 𝒳_(tf,θ) → 𝒴_(tf,θ) of [[sec:i-c-4]] for P̂_λ at q = β ([[sec:iv6-4]]). For γ ∈ ℝ that is
not the real part of an indicial root of P̂_λ(0), let ind_λ(γ) be the index of this map at q = 2 − γ, which is
Fredholm by [[thm:i-c-4-3]] (3); this is the index of [[sec:iii-f1-3]] at the weight γ. The index to be found is
ind_1(2 − β), and 2 − β ∈ [−C_0, 2).

For λ ∈ [0, 1] let I_λ be the indicial family ([[eq:i-c-1-3]]) of P̂_λ(0). It is that of ρ⁻²(□^C)^(0) with h⁻¹
replaced by λh⁻¹ (the proof of [[lem:iv4-1-3]]), of the form of [[lem:i-c-2-4]], with coefficients affine in λ that
commute with the action of SO(4) rotating both 𝕊³ and the Cartesian components. For an irreducible representation π
of SO(4) let W_π, the π-isotypic subspace of C^∞(𝕊³; ℂ⁵), and d(π) be as in [[lem:iii-f1-2-4]]; sums over π below
run over the π with W_π ≠ 0. For γ ∈ ℝ let n_π(λ, γ) be the number of roots of I_λ on W_π with real part < γ, with
multiplicity. By *Types and representations* in [[sec:iii-f1-1]], W_π is ℂ^k ⊗ π for the type and degree of π, with
k = 2 at scalar type 0, k = 3 at scalar type l ≥ 1 and k = 1 at vector type, and I_λ(ι) acts on W_π as N(ι) ⊗ Id_π
for a k × k matrix N(ι). So det(I_λ(ι)|_(W_π)) = det(N(ι))^(dim π), and the roots on W_π are those of det N, each
with its multiplicity multiplied by dim π. At λ = 1, in the basis S dt, S dr, r dS (resp. rV) of [[prop:np-10-12]]
(ii), N is N_0, N_l or N_(v,l), so that det N is h⁻²P_0, h⁻³P_l or h⁻¹p_(v) ([[prop:np-10-12]] (iii)).

Let γ_* := C_0 + 2. By [[lem:iii-f1-2-4]] with 𝒯 = [0, 1], there is d_0 > γ_* such that for every λ and every π
with d(π) ≥ d_0 no root of I_λ on W_π has real part in [−γ_*, γ_*]. For λ ∈ [0, 1] and γ ∈ [−γ_*, γ_*] not the real
part of a root of I_λ put

    G(λ, γ) := ind_λ(γ) − Σ_π (n_π(λ, γ) − dim W_π).

The sum is finite. Each H_d ⊗ ℂ⁵, H_d the harmonics of degree d ((K4) of [[sec:i-c-2-1]]), is invariant under the
action of SO(4), so W_π is the sum of its intersections with these spaces, which vanish for d < d(π). At λ = 0, on
H_d ⊗ ℂ⁵, I_0(ι) = −ι² + 2ι + d(d + 2) = −(ι + d)(ι − d − 2), the free operator acting componentwise (the proof of
[[prop:i-c-5-3]]). So at λ = 0, W_π carries dim W_π roots ≤ −d(π) and dim W_π roots ≥ d(π) + 2; hence
n_π(0, γ) = dim W_π for γ ∈ (0, 2), and for every γ ∈ [−γ_*, γ_*] if d(π) ≥ d_0. In the latter case the roots on
W_π, which depend continuously on λ ([[lem:iii-f1-2-4]]), never have real part in [−γ_*, γ_*], so n_π(λ, γ) = dim W_π
for every λ. So the terms with d(π) ≥ d_0 vanish, and only finitely many π have d(π) < d_0.

G(λ, γ) does not depend on γ. Let γ₁ < γ₂ be two such weights, and choose γ₁ = w_0 < w_1 < … < w_M = γ₂ with
w_(i+1) − w_i < 1, none of them the real part of a root of I_λ; this is possible, as only finitely many roots have
real part in [γ₁, γ₂] ([[lem:i-c-2-4]] (b)). By [[lem:iii-f1-3-1]], applied to each pair (w_i, w_(i+1)) as its
weights (β_1, β_2), ind_λ(w_(i+1)) − ind_λ(w_i) is the number of roots of I_λ with real part in (w_i, w_(i+1)), with
multiplicity. Adding, ind_λ(γ₂) − ind_λ(γ₁) is the number of roots with real part in (γ₁, γ₂), which is the change of
the sum.

G(λ, γ) does not depend on λ. Let λ_0 ∈ [0, 1]. Only the finitely many W_π with d(π) < d_0 carry roots with real part
in [−γ_*, γ_*], and these roots depend continuously on λ; so there is γ ∈ (−γ_*, γ_*) that is not the real part of a
root of I_λ for any λ near λ_0. The terms with the factor λh⁻¹, namely −2iσλh⁻¹ρS̄ in [[eq:iv6-0-2]] and the part of
(□^C)^(0) that comes from λh⁻¹𝓛_c ([[lem:s14-box-c]]), which lies in ρ²Diff¹_b ([[lem:s14-tf-inputs]] (i)), map
H^(s,(ℓ,q))_(sc,b) boundedly into H^(s−2,(ℓ+1,q−2))_(sc,b). So the domain of the map does not depend on λ, the map
is continuous in λ in operator norm, and, being Fredholm, it has an index that is constant near λ_0; and every
n_π(λ, γ) is constant near λ_0, as no root crosses the line Re ι = γ. So G is constant near λ_0, and as [0, 1] is
connected, G(1, ·) = G(0, ·).

At λ = 0 and γ ∈ (0, 2), ind_0(γ) = 0: at ρ = 0, P̂_0 has the data of □_η acting componentwise, so it is
tf-admissible with every weight in (0, 2) ([[prop:i-c-5-3]]), and N_tf(P̂_0, e^(iθ)) is invertible at q = 2 − γ by
[[cor:i-c-5-2]] (a). As n_π(0, γ) = dim W_π for every π, G(0, γ) = 0. At λ = 1 and γ = 2 − β, no indicial root of
P̂_1(0) has real part in [−100, 2) ([[lem:iv4-1-3]] (a)), so n_π(1, 2 − β) is the number of roots on W_π with real
part < −100. With multiplicity, P_0 has two such roots, P_l (l ≥ 1) three and p_(v) one ([[prop:np-10-54]] (i)); so
n_π(1, 2 − β) = k dim π = dim W_π for every π. Hence ind_1(2 − β) = G(1, 2 − β) = G(0, 1) = 0, and the index of
[[eq:iv6-1-1]] is 0. ∎
```

The line before the old text is blank, and before it is the paragraph "So [[eq:iv6-1-1]] is Fredholm, …" (lines
3011–3015), which ends "Hence the index does not depend on the admissible orders." and which the new text uses in its
first sentence. Neither this file nor P-G24b changes that paragraph.

### P-RI-3. lem:iii-f1-3-1, the hypothesis on s (chapter 34, lines 595–596)

Old (2 lines):

```text
**Lemma {#lem:iii-f1-3-1}** (Relative index.) Let β_1 < β_2 < β_1 + 1, neither the real part of a point of spec_b,
and s ∈ ℤ. Then ind(β_2) − ind(β_1) = dim F, where F := ⊕_μ F_μ over the roots μ of J with −β_2 < Re μ < −β_1 and
```

New (2 lines):

```text
**Lemma {#lem:iii-f1-3-1}** (Relative index.) Let β_1 < β_2 < β_1 + 1, neither the real part of a point of spec_b,
and s ∈ ℤ, s ≥ 2. Then ind(β_2) − ind(β_1) = dim F, where F := ⊕_μ F_μ over the roots μ of J with −β_2 < Re μ < −β_1 and
```

Only the second line changes ("s ∈ ℤ." becomes "s ∈ ℤ, s ≥ 2."); it has 120 characters and no label. The proof is
unchanged. Steps 1–2 now meet the condition under which their Mellin transforms are defined (section 3.1, "s = 2").

### Uses of lem:iii-f1-3-1

A search of every chapter source (chapters/*.md) at HEAD for "lem:iii-f1-3-1" finds the label (chapter 34, line 595)
and one citation. With this file there are two more. No other file in proofs/ cites the lemma.

- **Chapter 34, line 760, the proof of prop:iii-f1-3-3 (iii).** "by [[lem:iii-f1-3-1]] (through intermediate
  weights, finitely many roots lying between)". The index ind_τ(β″) there is that of N_tf(P̂_τ, 1) "at θ = 0 with the
  common orders", at the s fixed at line 716: "Fix α_+, s ∈ ℤ large". This meets s ≥ 2: s is taken large, and nothing
  in the proof bounds it above.
- **Chapter 33, the new text of P-RI-2, paragraph "G(λ, γ) does not depend on γ".** "By [[lem:iii-f1-3-1]], applied to
  each pair (w_i, w_(i+1)) as its weights (β_1, β_2)". The index ind_λ(γ) is taken at s := 2, fixed in the first
  sentence of the new text. This meets s ≥ 2.
- **Chapter 33, the new text of P-RI-1, the overview of sec:iv6.** "the relative index formula of [[lem:iii-f1-3-1]]".
  It applies nothing itself: it names the formula that the proof of prop:iv6-1-1 applies, with s = 2.

### Interplay with P-G24b and P-G1

**P-G1.** Its merge is in the base of this file (chapter 33 md5 d2184d75…), so there is nothing left to compose with.

**P-G24b** (md5 a44f9f97a98e435754cf15153bedef33, 45 texts T1–T45). Its line numbers are those of chapter 33 at md5
147ca162…, before the P-G1 merge. Its T41 is to be used in variant A after P-G1 (its §8). Its texts are all in
chapter 33, so P-RI-3 does not meet them. None of its 45 old texts meets the old texts of P-RI-1 and P-RI-2:
- P-RI-1 (lines 2791–2792 at HEAD) lies between T21 (lines 2752–2754 at HEAD) and T23 (lines 2937–2939). In P-G24b's
  numbering T21 is at 2135–2137, T23 at 2316–2318, and P-RI-1 at 2170–2171.
- P-RI-2 (lines 3017–3049) lies between T29 (lines 3005–3008) and T30 (lines 3080–3082). In P-G24b's numbering T29 is
  at 2384–2387, T30 at 2458–2460, and P-RI-2 at 2396–2428. T29's old text ends inside line 3008, after "…[[lem:i-a-7-1]]
  are.", and that line goes on with "Near r = 0 the normal operator …"; P-RI-2 starts nine lines later.
- A script applied the 45 texts of P-G24b (T41 in variant A) to the HEAD chapter and then this file's three texts, and
  in the other order. Each old text of either file was found exactly once at its turn, and the two orders give the same
  chapter (section 7).
- If P-G24b is merged, nothing in the chapter texts here needs adjusting. The new text does not cite the "estimates
  above" at all: the Fredholm property at each λ comes from thm:i-c-4-3 (3). After T23 rewrites def:iv6-0-2, the
  clause "where only R_out enters ([[def:iv6-0-2]])" stays true.
- For the crosswalk both files append to the note of the row of prop:iv6-1-1; section 6 states this file's change as
  an append, so the two compose in either order.
- P-G24b §6.1 should be dropped, or marked as closed by this file, with the items listed in section 3.4.

**Other proof files.** No other file in proofs/ quotes any line of the three old texts.

## 5. Appendix A

No new entry. thm:std-relative-index is kept, and is now cited only for attribution (P-RI-1).

## 6. Crosswalk

No label is added, so no row is added. Two notes are added to existing rows, each as an append, never as a whole-row
replacement.

**crosswalk/33-s14-constraint-damping.tsv, the row of prop:iv6-1-1** (line 127 of md5 5b4e25fe…, four tab-separated
fields). Append to its fourth field, after whatever it then ends with, the text below. It starts with "; ".

```text
; P-RI: index 0 by the relative index formula lem:iii-f1-3-1 (localisation at ztf and the Smith-form count rank = order of the zero of the determinant) and lem:iii-f1-2-4, through the invariant G of the proof of prop:iii-f1-3-3 (iii), with gamma_C deformed to 0 in the spectral family of box^C_b; counts at gamma_C = 1/h from lem:iv4-1-3 (a) and prop:np-10-54 (i) with multiplicity, at 0 from the componentwise free operator; replaces the sector argument and the use of [Mel93, Theorem 6.5] outside its hypotheses; theta_in -> vartheta_in and r_mid -> sans-serif r_mid in the rewritten sentence, and its R_in clause restricted to theta in {0, pi}
```

P-G24b's §9 appends "; P-G24b: dual estimate displayed …" to the same field. Each append adds to the end of the field,
so either order leaves one line with four fields and both notes in full; only the order of the two notes differs.

**crosswalk/34-s15-linearised.tsv, the row of lem:iii-f1-3-1** (line 29 of md5 6995e64a…, four tab-separated fields,
the fourth empty at HEAD). Put the text below into the fourth field. If a note has been added there first, append "; "
and then the text.

```text
P-RI: s >= 2 added to the hypothesis (Steps 1-2 take the Mellin transform of an element of H^(s-2)_b, defined for weighted L^2 functions); its uses take s large (prop:iii-f1-3-3 (iii)) and s = 2 (prop:iv6-1-1)
```

## 7. Checks (on scratch copies)

The scratch copies are in
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/fpri/.
Each is the reader directory as committed at HEAD (ecd1a428), whose chapters 33 and 34 and both crosswalk files are the
files named at the top of this file.
- **base/**: HEAD, unchanged.
- **A/**: P-RI alone, that is P-RI-1 to P-RI-3 and the two crosswalk notes.
- **B/**: the 45 texts of P-G24b (T41 in variant A, as its §8 says) and its note on the row of prop:iv6-1-1, then P-RI.
- **C/**: P-RI first, then P-G24b as in B.

Before (base/):

    $ python3 lint.py --chapters
    chapters: 62 file(s), 4665 label(s) defined, 0 hit(s)
    $ python3 assemble.py --check
    labels 4665, computations cited 0, problems 0

After P-RI alone (A/):

    $ python3 lint.py --chapters
    chapters: 62 file(s), 4665 label(s) defined, 0 hit(s)
    $ python3 assemble.py --check
    labels 4665, computations cited 0, problems 0
    $ python3 assemble.py && python3 lint.py --paper
    PAPER.md: 0 hit(s)

After P-G24b and P-RI (B/, and the same in C/):

    $ python3 lint.py --chapters
    chapters: 62 file(s), 4681 label(s) defined, 0 hit(s)
    $ python3 assemble.py --check
    labels 4681, computations cited 0, problems 0
    $ python3 assemble.py && python3 lint.py --paper
    PAPER.md: 0 hit(s)

The 16 further labels are those P-G24b adds. The plain assemble.py was run only in the scratch copies.

Further checks:
- **Old texts.** Each of the three old texts occurs exactly once in its chapter at HEAD, as whole lines, and again after
  P-G24b. In B and C each of P-G24b's 45 old texts was found exactly once at its turn. P-G24b quotes its old texts as
  exact strings, and five of them do not end at a line end: T7, T16, T29 and T45 end inside a line, and T15 starts and
  ends inside one.
- **Orders.** B and C give byte-identical chapters 33 and 34. Their crosswalk files differ only in the row of
  prop:iv6-1-1, by the order of the two notes; in both the row has four fields and carries both notes in full.
- **Line lengths.** No line exceeds 121 characters in chapters 33 and 34 or in PAPER.md, in A, B or C. In PAPER.md the
  new index-0 text has lines of at most 117 characters, the overview at most 113, and the changed line of the lemma 120.
  With every label replaced by "Proposition 33.123", no line of the three new texts exceeds 121.
- **Typography.** No line of the new texts starts with "+ ", "- ", "* ", "> ", "#", "=", "|" or "<". There is no
  backslash, and no label is added or changed.
- **Citations after the change (A and B).** "[Mel93" and "[Hin26a, p. 91]" no longer occur in chapter 33.
  lem:s14-tf-inputs (v) is cited nowhere. [[thm:std-relative-index]] is cited once (P-RI-1). [[lem:iii-f1-3-1]] is
  cited at chapter 34 line 760 and at two places in chapter 33 (P-RI-1 and P-RI-2).
- **The new text of P-RI-2.** Section 2 is the same text. It is the reader's consolidated replacement (R-P-RI) unchanged:
  its md5, taken without the final newline as the reader took it, is 3ff2456e854726636c603698c5441504.
