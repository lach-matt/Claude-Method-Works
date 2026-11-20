# F-G3: thm:own-data (3), the maximal vacuum development

## Route taken, and why

The preferred route works: "maximal" is kept and proved, and nothing beyond what the paper and [Sbi15] already hold is needed.

- **(c) the inner boundary.** The data are taken on Σ̊ := Σ^IVP ∩ {r > r_♭}. This is a connected graph over {|x| > r_♭}, a manifold without boundary, as [Sbi15, p. 11] requires of initial data.
- **(a) existence.** [Sbi15, Theorem 2.8, p. 12] (Existence of MGHD) gives the maximal globally hyperbolic development (M̂, ĝ, ι̂) of (Σ̊, γ, k), unique up to isometry. I checked the number, the wording and the page against arXiv:1309.7591v3, whose pages Appendix A uses. The proof is on pp. 22–24. The original is Choquet-Bruhat–Geroch, Comm. Math. Phys. 14 (1969), 329–335.
- **(b) the constructed development is a GHD.** In the class, prop:vii-3-2 gives S = S⁰ = 0. So the development ǧ of thm:own-half-settling lives on Ω_* ∪ 𝒟_(0,0). Since Ω_* ⊂ {t_IVP ≥ 1}, this union is exactly {t_IVP ≥ 0}. It has a past boundary Σ^IVP and the inner boundary {r = r_♭}, so it is not itself a GHD.
- **The gluing.** I follow the chapter 62 template. Take any GHD (N, g_N, ι_N) of the data ([Sbi15, Theorem 2.6]) and its Cauchy time function h_N ([BGP, Theorem 1.3.13]). Glue the past half N₋ = {h_N ≤ 0} to M₊ = {r > r_♭, t_IVP ≥ 0} along Σ̊.
  - The charts, smooth structure, Ricci-flat metric, time orientation and acausality steps of the proof of lem:interior-one-spacetime transfer with a stated substitution list.
  - Hausdorffness and second countability, which chapter 62 got from its common coordinate chart, are proved directly from the charts.
- **M₊ lies in the domain of dependence D_gl of Σ̊.** This is the time-function argument the audit asked for, in three steps along a past-inextendible causal curve:
  1. t^♭_* falls to 3/2, using the compact sets of lem:iii-k-6-1 (c) and the argument of the proof of lem:ii-f-1-3, as in prop:iii-k-4-2.
  2. It stays at most 3/2.
  3. In {t^♭_* ≤ 3/2} ⊂ 𝒟, dt_IVP is past timelike and r is bounded (lem:iii-k-6-2 (a), (c)), so the curve converges in a compact set. It cannot converge into the open part or onto Σ̊. It cannot converge onto {r = r_♭} either: near that boundary dr is future timelike, so r decreases to the future.
- **Conclusion.** D_gl is a GHD ([BGP, Lemma A.5.9]; [Sbi15, Definition 2.1]). Maximality gives j : D_gl → M̂, and Ψ := j ∘ π embeds ({r > r_♭, t_IVP > 0}, ǧ) isometrically. The settling region {r_♭ < r ≤ R′, t_* ≥ t_1}, with t_1 ≥ 1, lies there, because t_IVP ≥ t_* there. So the bound carries over to Ψ^*ĝ.

**What changed in the statement.** Item (3) now states two things:
- the concrete development ǧ settles on {r_♭ ≤ r ≤ R′, t_* ≥ t_1}, exactly as before;
- the maximal development contains it, and settles on {r_♭ < r ≤ R′, t_* ≥ t_1}. The inner boundary r = r_♭ is not part of any development of Σ̊.

So the theorem is not weakened. It gains a precise meaning for "settles" on an abstract manifold, namely through Ψ, and t_1 ≥ 1 is recorded.

## New text and its location (chapters/63-own-data.md, current line numbers)

- **Lines 3–11:** the opening paragraph. The sentence about "the maximal vacuum development" is replaced: the data have a vacuum development that settles, and their maximal globally hyperbolic development, which contains it, settles with it. The paragraph is re-wrapped.
- **Lines 13–24:** the outline paragraph. The last sentence now also says that Section sec:own-proof places the development in the maximal one (lem:own-maximal). The paragraph is re-wrapped.
- Lines 59–65: statement item (3), rewritten (text below).
- Lines 1872–1972: new **Lemma {#lem:own-maximal}** (the development lies in the maximal one), with its proof, placed after prop:own-transfer and before the proof of thm:own-data (text below).
- Lines 2015–2024: proof item (3), rewritten (text below).
- **crosswalk/63-own-data.tsv:**
  - a new final row for lem:own-maximal, with source "G-SWEEP fix F-G3", in chapter order (checked);
  - a clause appended to the note of the thm:own-data row.

No other file was edited. Chapters 01, 03 and 90 were not touched, because their restatements stay correct (see below).

### Statement item (3)

```
(3) (γ, k) have a G-invariant vacuum development ǧ on {t_IVP ≥ 0}, t_IVP being the function of [[lem:iii-b-3-7]] (b),
with Σ^IVP = t_IVP⁻¹(0), which settles to a Tangherlini metric g_(m′,0) with |m′ − μ_end| < ε_m: on
{r_♭ ≤ r ≤ R′, t_* ≥ t_1}, |(t_*∂_(t_*))^i ∂_x^β (ǧ − g_(m′,0))| ≤ C t_*^(−2−ε_t) for every R′, i and β, with C and
t_1 ≥ 1 depending on them. The maximal globally hyperbolic vacuum development (M̂, ĝ, ι̂) of the data (γ, k) on the
surface without boundary Σ̊ := Σ^IVP ∩ {r > r_♭} contains it: there is a time-orientation-preserving isometric embedding
Ψ of ({r > r_♭, t_IVP > 0}, ǧ) into (M̂, ĝ) that extends continuously to Σ̊ by ι̂ ([[lem:own-maximal]]). So ĝ settles in
the same sense: |(t_*∂_(t_*))^i ∂_x^β (Ψ^*ĝ − g_(m′,0))| ≤ C t_*^(−2−ε_t) on {r_♭ < r ≤ R′, t_* ≥ t_1}.
```

### The new lemma and its proof

```
**Lemma {#lem:own-maximal}** (the development lies in the maximal one). Let (γ, k) be G-invariant vacuum data on Σ^IVP
as in [[thm:own-half-settling]], below its threshold, and let ǧ be the G-invariant vacuum development given there: the
metric of [[thm:iii-k-4-3]] on Ω_* ∪ 𝒟_(0,0), with S = S⁰ = 0 ([[prop:vii-3-2]]). Put Σ̊ := Σ^IVP ∩ {r > r_♭} and
M₊ := {r > r_♭, t_IVP ≥ 0}. Then ǧ is defined on M₊; (Σ̊, γ, k) is initial data in the sense of [Sbi15, p. 11], with
d = 4; its maximal globally hyperbolic development (M̂, ĝ, ι̂), a globally hyperbolic development that is an extension
of every other one, exists and is unique up to isometry [Sbi15, Theorem 2.8, p. 12]; and there is a
time-orientation-preserving isometric embedding Ψ : (M₊ ∖ Σ̊, ǧ) → (M̂, ĝ) that extends continuously to M₊ by ι̂ on Σ̊.

*Proof.* In this proof t is the time of the chart of [[lem:vii-1-2]], as in [[ch:s27]], and not the Kerr–Schild time of
the far region. *The development.* By [[thm:own-half-settling]] the results of [[ch:s27]] hold in the class ℰ_0^½, and
by [[prop:vii-3-2]] the map φ_(0,0) is the identity, so ǧ induces (γ, k) on Σ^IVP ([[thm:iii-k-4-3]] (2)); here
b₀ = (μ_end, 0), and g_(b₀) is g_b0 written in the chart of [[lem:vii-1-2]] ([[lem:interior-chart]] (a)). On Ω_*,
t_IVP ≥ t_* ≥ t^♭_* ≥ 1 (ψ_IVP ≤ ψ, with ψ of [[eq:iii-b-3-6]], by the proof of [[lem:iii-b-3-7]] (b), and
[[lem:ii-c-3-2]] (b)); and 𝒟_(0,0) = {t_IVP ≥ 0} ∩ {t^♭_* ≤ T̂ + 2} ([[prop:iii-k-1-2]]), while {t^♭_* > T̂ + 2} ⊂ Ω_*.
So Ω_* ∪ 𝒟_(0,0) is the part {t_IVP ≥ 0} of the spacetime of [[ch:s27]], which contains M₊. Where t^♭_* ≤ T̂ + ¼c_0, a
set containing {t^♭_* ≤ 3/2} as T̂ ≥ 2, ǧ = g_(b₀) + h_0 ([[prop:iii-k-4-2]] with S = S⁰ = 0; h_0 := h_(0,0)), the
metric g_(0,0) of [[lem:iii-k-6-2]] on the region 𝒟 of [[prop:iii-k-1-2]]; it is smooth on 𝒟 up to its boundary
(the proof of [[prop:iii-k-1-2]]), and dt_IVP is past timelike for it on 𝒟 ([[lem:iii-k-6-2]] (a)). So near each point
of Σ̊, ǧ is the restriction of a smooth Lorentzian metric, the future unit normal of Σ̊ points into M₊, and ǧ induces
(γ, k) on Σ̊ with respect to it. On Ω°_*, ǧ − g_(b₀) is small in 𝒢̃^(0,(1,0,0))_(e3b) and t^♭_* is a time function of ǧ,
as in the proof of [[prop:iii-k-4-2]] ([[lem:s27-below]] (iii)).

*The data, and a development of them.* Σ̊ is the graph t = ψ_IVP(|x|) over the connected set {|x| > r_♭} ⊂ ℝ⁴, an open
subset of Σ^IVP and, unlike Σ^IVP, which ends at {r = r_♭}, a manifold without boundary, as [Sbi15, p. 11] asks of
initial data; γ is Riemannian; and (γ, k) satisfies the constraint equations, by the Gauss and Codazzi equations for the
vacuum metric ǧ. So (Σ̊, γ, k) is initial data in the sense of [Sbi15, p. 11] ([[thm:std-sbierski]]), with d = 4, and
[Sbi15, Theorem 2.8, p. 12] gives (M̂, ĝ, ι̂). By [Sbi15, Theorem 2.6] ([[thm:std-sbierski]] (3)) the same data have a
globally hyperbolic development (N, g_N, ι_N). Σ_N := ι_N(Σ̊) is a smooth spacelike Cauchy hypersurface of N, γ being
Riemannian, so there is a Cauchy time-function h_N on N with Σ_N = h_N⁻¹(0) ([[thm:std-bgp-causal]] (3)); its gradient
is past directed timelike ([[thm:std-bgp-causal]] (2)), so dh_N is past timelike. We glue the past half of N to M₊, show
that the result contains a globally hyperbolic development of (Σ̊, γ, k) that contains M₊, and obtain Ψ from the
maximality of (M̂, ĝ, ι̂).

*The glued space.* N₋ := {h_N ≤ 0} and M₊ are manifolds with boundary Σ_N and Σ̊, as dh_N and dt_IVP do not vanish. Let
M_gl := (N₋ ⊔ M₊)/∼, where ι_N(y) ∼ y for y ∈ Σ̊, with the quotient topology and the projection π. π maps N₋ and M₊
homeomorphically onto closed subsets of M_gl: for a closed F ⊂ N₋, the preimage of π(F) is F together with
ι_N⁻¹(F ∩ Σ_N) ⊂ Σ̊, which is closed, and likewise for M₊. So π(N₋ ∖ Σ_N) and π(M₊ ∖ Σ̊) are disjoint open subsets of
M_gl, covering the complement of the closed set π(Σ̊), which we write Σ̊.

*Charts, smooth structure, metric, time orientation.* The paragraphs of the proof of [[lem:interior-one-spacetime]] from
*(i), the charts at Σ* to *(i), time orientation and connectedness* apply with Σ̊, M₊ and ǧ in place of Σ, B and g, and
with N₋, g_N, N, h_N, n_N and E_N(s, y) := exp^(g_N)_(ι_N(y))(s n_N), n_N the future unit normal of Σ_N, in place of A,
g_λ, V and D_V(Σ), t_IVP on the side of A, n_λ and E_λ, and with {|x| > r_♭} in place of the shell {r_♭ < |x| < R}. Of
the common chart of that lemma they use only the following, which hold here: dh_N(n_N) > 0, dh_N being past timelike,
and dt_IVP(n) > 0, n pointing into M₊; the coordinates x of the graph Σ̊, carried to Σ_N by ι_N, as the coordinates on
Σ̊ in every chart; that ǧ is near each point of Σ̊ the restriction of a smooth Lorentzian metric; that the two halves
are closed in M_gl and carried homeomorphically by π; and that a set W_Π is open when it meets the two halves in open
sets, which here is the definition of the quotient topology. For the connectedness of N₋: through a point p′ ∈ N₋ ∖ Σ_N
passes an inextendible timelike curve of N, which meets the Cauchy hypersurface Σ_N after p′, h_N increasing along it,
and between the two it lies in N₋. This gives charts Φ_Π : (−s_0, s_0) × Π → W_Π at the points of Σ̊, homeomorphisms
onto open sets which, with charts of the two open halves, form a smooth atlas
(M_gl is Hausdorff and second countable by the next paragraph, which uses only these charts); a smooth Ricci-flat
Lorentzian metric g_gl on M_gl, equal to g_N and to ǧ off Σ̊, which induces (γ, k) on the smooth spacelike hypersurface
Σ̊; a time orientation in which the unit normal of Σ̊ is future and which is that of ǧ on π(M₊ ∖ Σ̊); and the
connectedness of M_gl. Part *(ii)* of that proof then shows that Σ̊ is acausal in M_gl.

*Hausdorff and second countable.* Two points of π(N₋ ∖ Σ_N), or two of π(M₊ ∖ Σ̊), are separated in that open set, and a
point of each by these two disjoint open sets. Let y ∈ Σ̊ and z ≠ y. If z = π(p′), p′ ∈ N₋ ∖ Σ_N, take disjoint open
sets U′ ∋ p′ and U_y ∋ ι_N(y) of N with U′ ⊂ N₋ ∖ Σ_N, and Π and s_0 so small that E_N((−s_0, 0] × Π) ⊂ U_y, as
E_N(0, y) = ι_N(y); then π(U′) and W_Π are disjoint open sets. If z lies in π(M₊ ∖ Σ̊), the same holds with M₊ and the
map E of that proof in place of N and E_N. If z ∈ Σ̊, take disjoint neighbourhoods of ι_N(y) and ι_N(z) in N and of y
and z in M₊, and charts W_Π ∋ y and W_Π′ ∋ z whose halves lie in them; then W_Π ∩ W_Π′ = ∅. So M_gl is Hausdorff. Σ̊,
being second countable, is covered by countably many W_Π, and M_gl is the union of these and of the two open halves,
each second countable; so M_gl is second countable.

*The development D_gl.* Σ̊ is an acausal smooth spacelike hypersurface of the connected time-oriented Lorentzian
manifold M_gl. So D_gl := D_(M_gl)(Σ̊) is open and globally hyperbolic, with Σ̊ as a Cauchy hypersurface
([[thm:std-bgp-development]]); it is connected, every point of it being joined to Σ̊ within it as at the end of the
connectedness paragraph cited; and with the inclusion ι of Σ̊ it is a globally hyperbolic development of (Σ̊, γ, k)
[Sbi15, Definition 2.1] ([[thm:std-sbierski]] (1)): connected, time oriented, vacuum, with ι^*g_gl = γ and with second
fundamental form k with respect to the future normal.

*M₊ lies in D_gl.* Let p ∈ π(M₊ ∖ Σ̊) and let 𝔠 be an inextendible causal curve of M_gl through p, run from p to the
past. Suppose that 𝔠 does not meet Σ̊. Then it stays in the open set π(M₊ ∖ Σ̊) = {r > r_♭, t_IVP > 0}, the complement
of Σ̊ being the disjoint union of the two open halves, and it is past inextendible there. First, if t^♭_*(p) > 3/2, 𝔠
does not stay in {t^♭_* > 3/2}. The part of this set in {r > r_♭} lies in Ω°_*, and the argument of the proof of
[[lem:ii-f-1-3]] on Ω°_*, with τ := t^♭_*, the level 3/2 and the compact sets L_p ⊂ Ω°_* of [[lem:iii-k-6-1]] (c),
applied as in the proof of [[prop:iii-k-4-2]], shows that t^♭_* reaches 3/2 along every past directed causal curve from
p that is past inextendible in Ω°_*; 𝔠 would be one if it stayed in {t^♭_* > 3/2}. Second, from the first point p_1 of 𝔠
at which t^♭_* ≤ 3/2 (p_1 := p if t^♭_*(p) ≤ 3/2) on, t^♭_* stays at most 3/2: to exceed it, 𝔠 would run in
{t^♭_* > 3/2}, where t^♭_* is a time function, along an interval starting at a point where t^♭_* = 3/2, and t^♭_*
decreases to the past along such an interval. Third, beyond p_1, 𝔠 therefore lies in {t_IVP > 0, t^♭_* ≤ 3/2} ⊂ 𝒟, where
ǧ = g_(0,0): dt_IVP is past timelike there, and r ≤ R_𝔠 := max(R_s, r(p_1)) + 2t_IVP(p_1) along 𝔠 beyond p_1
([[lem:iii-k-6-2]] (a) and (c), the latter at the level 0; R_s is the radius R of that lemma). So 𝔠 lies in
L_𝔠 := {0 ≤ t_IVP ≤ t_IVP(p_1), r_♭ ≤ r ≤ R_𝔠, t^♭_* ≤ 3/2}, a closed set, bounded in the coordinates (t, x) as
t = t_IVP + ψ_IVP(r), hence compact, on which ǧ = g_(0,0) is continuous and dt_IVP is past timelike; parametrised by
t_IVP, it converges in L_𝔠 to a point q, as in the proof of [[lem:ii-f-1-3]]. q is not in {r > r_♭, t_IVP > 0}, in which
𝔠 is past inextendible, nor in Σ̊, where 𝔠 would have an end point in M_gl; so r(q) = r_♭. But
g_(b₀)⁻¹(dr, dr) ≤ −c_r < 0 on {r_♭ ≤ r ≤ r^♮}, with dr future timelike for g_(b₀) there
(the proof of [[lem:s27-below]] (iv)), and h_0 is small in C⁰ on the compact set 𝒟 ∩ {r ≤ R_s}
(the proof of [[lem:iii-k-6-2]] (a)), which contains 𝒟 ∩ {r ≤ r^♮}, as r^♮ = ½(r_♭ + 7R₁/8) < R₁ ([[def:s12-radii]])
while R_s ≥ 5R₁, t_IVP = t − C″ holding on {r ≥ R_s} and ψ_IVP = ψ increasing strictly on [3R₁, 5R₁]
([[lem:iii-b-3-7]] and its proof). So, as in the proof of [[lem:s27-below]] (iv), dr stays timelike for g_(b₀) + s h_0,
s ∈ [0, 1], on 𝒟 ∩ {r ≤ r^♮}, and it is future timelike for ǧ there, the time orientation of ǧ on 𝒟 being the one that
continues that of g_(b₀) ([[lem:iii-k-6-2]] (a)). Hence r increases strictly along 𝔠 towards q near q, and r(q) > r_♭, a
contradiction. So 𝔠 meets Σ̊, and π(M₊) ⊂ D_gl.

*The embedding.* By [Sbi15, Theorem 2.8], (M̂, ĝ, ι̂) is an extension of (D_gl, g_gl, ι): there is a
time-orientation-preserving isometric embedding j : D_gl → M̂ with j ∘ ι = ι̂ [Sbi15, Definition 2.2]
([[thm:std-sbierski]] (2)). Ψ := j ∘ π on M₊ is continuous and equal to ι̂ on Σ̊, and on M₊ ∖ Σ̊, where π is an isometry
of ǧ onto g_gl that preserves the time orientations, it is a time-orientation-preserving isometric embedding. ∎
```

### Proof item (3)

```
(3) The data are G-invariant (g is), vacuum, in the half-integer class and below the thresholds of [[prop:vii-3-2]] and
[[cor:s27-rate]]. By [[thm:own-half-settling]] they have a G-invariant vacuum development ǧ, the metric of
[[thm:iii-k-4-3]] with b = (m′, 0) and S = S⁰ = 0 ([[prop:vii-3-2]]), defined on {t_IVP ≥ 0} ([[lem:own-maximal]]),
which settles to g_(m′,0) with |m′ − μ_end| < ε_m (b₀ = (μ_end, 0)) at the rate O(t_*^(−2−ε_t)) of [[eq:s27-rate]] on
{r_♭ ≤ r ≤ R′, t_* ≥ t_1}, t_1 being the T′ of [[cor:s27-rate]] (c), taken at least 1. By [[lem:own-maximal]] the
maximal globally hyperbolic development (M̂, ĝ, ι̂) of (Σ̊, γ, k) exists, and Ψ embeds ({r > r_♭, t_IVP > 0}, ǧ) in it
isometrically, preserving the time orientation and extending continuously to Σ̊ by ι̂. On {r_♭ < r ≤ R′, t_* ≥ t_1},
t_IVP ≥ t_* ≥ 1, so this set lies in the domain of Ψ, and Ψ^*ĝ = ǧ there satisfies the same bound. No gluing is used,
and no value of λ ∈ (0, λ_2] is excluded: [[prop:own-transfer]] shows only that, off the exceptional set of
[[prop:own-tail]] (d), the half-integer class is needed. ∎
```

## Appendix A text needed (chapters/95-standard-results.md, thm:std-sbierski). Not applied; ch. 95 was not edited

**1. Header of thm:std-sbierski.** Replace the citation list with:

> (Globally hyperbolic developments; [Sbi15, Definitions 2.1, 2.2 and 2.4, p. 11; Theorems 2.6, 2.7 and 2.8, p. 12; Theorem 3.4, p. 14; Definition 3.5, p. 15; Theorem 3.13, p. 20; proof of Theorem 2.7, pp. 20–22].)

**2. New item after (6):**

> (7) Theorem 2.8 (Existence of MGHD): "Given initial data there exists a GHD M̃ that is an extension of any other GHD of the same initial data. The GHD M̃ is unique up to isometry and is called the maximal globally hyperbolic development (MGHD) of the given initial data." Its proof is on pp. 22–24. By the standing assumption of p. 10, the GHDs are smooth, and [Sbi15, p. 10] notes that the MGHD is "a priori, only maximal among smooth GHDs".

- **Source:** J. Sbierski, Ann. Henri Poincaré 17 (2016), 301–329, arXiv:1309.7591v3, Theorem 2.8, p. 12 of the arXiv version, read verbatim.
- **Bibliography:** [Sbi15] is already in ch. 98, so nothing is needed there.
- **Optional:** the original Choquet-Bruhat–Geroch could be added for history: Y. Choquet-Bruhat, R. Geroch, *Global aspects of the Cauchy problem in general relativity*, Comm. Math. Phys. 14 (1969), 329–335. The proof does not use it.
- **After item (7) is added:** the coordinator may append "([[thm:std-sbierski]] (7))" to the two citations "[Sbi15, Theorem 2.8, p. 12]" and the one "[Sbi15, Theorem 2.8]" in lem:own-maximal. I left this out so that the sub-item is not cited before it exists.

Every other external result the lemma uses is already quoted in Appendix A:
- [Sbi15] Definitions 2.1 and 2.2, p. 11, and Theorem 2.6, p. 12: thm:std-sbierski (1)–(3);
- [BGP] Corollary 1.3.12 and Theorem 1.3.13: thm:std-bgp-causal (2), (3);
- [BGP] Lemma A.5.9: thm:std-bgp-development.

## Uses of thm:own-data (3) checked

- **ch. 00:30, ch. 01:66 and 01:183, ch. 03:338–340, ch. 61:82–83, ch. 62:17, 62:586, ch. 90:95–96 and 90:126–131.** Each says "the development of g_λ's own data settles" or cites the threshold λ_2 or the class. All remain correct: the constructed development and the maximal one both settle, and "the development" reads naturally as the canonical one. No change is needed, so chapters 01, 03 and 90 were left untouched.
- **Grep for "maximal vacuum development" or "maximal development".** Outside ch. 63 the only hit is Appendix A's [CTG23] quotation, which is unrelated. Inside ch. 63 all three old occurrences (lines 4, 58 and 1911 of the original) are replaced.
- **No proof in another chapter uses item (3).** The external references are descriptive only. Inside ch. 63, item (3) is used only in its own proof.

## Diff (against the original, identical to commit 33ec62f3)

Note: the coordinator's work-in-progress snapshots captured this fix while I worked. Commit 62d531f5 has an intermediate build. The current HEAD, cb5e06d5, holds the final version, identical to the working tree. The diff below is taken against the pre-fix original.

```diff
--- a/chapters/63-own-data.md
+++ b/chapters/63-own-data.md
@@ -1,26 +1,27 @@
 ## The development of g_λ's own data settles {#ch:own-data}
 
 [[thm:settling]] (i) concerns data that agree with those of g_λ on a ball and are continued equivariantly to exact
-Tangherlini data beyond it. This chapter proves that the maximal vacuum development of the data that g_λ itself induces
-on Hintz's initial surface Σ^IVP settles to five-dimensional Tangherlini, with no gluing, for every λ below a threshold
-and with no exceptional set. The data class of [[thm:settling]] (ii) does not contain these data: after the shell the
-difference g_λ − g0 carries at past null infinity a coefficient of r^(−5/2), of size O(λ^∞) but, for every amplitude
-but at most one, nonzero for all λ off a set whose only possible accumulation point is λ = 0, and it reaches the data
-at spatial infinity as a term ρ^(5/2), ρ := 1/r. The class is therefore widened by the half-integer orders, and the
-stability theory runs in the wider class with the same index sets.
+Tangherlini data beyond it. This chapter proves that the data that g_λ itself induces on Hintz's initial surface Σ^IVP
+have a vacuum development that settles to five-dimensional Tangherlini, with no gluing, for every λ below a threshold
+and with no exceptional set, and that their maximal globally hyperbolic development, which contains it, settles with it.
+The data class of [[thm:settling]] (ii) does not contain these data: after the shell the difference g_λ − g0 carries at
+past null infinity a coefficient of r^(−5/2), of size O(λ^∞) but, for every amplitude but at most one, nonzero for all λ
+off a set whose only possible accumulation point is λ = 0, and it reaches the data at spatial infinity as a term
+ρ^(5/2), ρ := 1/r. The class is therefore widened by the half-integer orders, and the stability theory runs in the wider
+class with the same index sets.
 
 The argument has five parts. (1) The far part S := Σ^IVP ∩ {r ≥ 4R} of the initial surface has a past domain of
 dependence W for Tangherlini, bounded by S, by an ingoing null cone ℋ on which g_λ is known, and by past null infinity,
 where nothing comes in after the shell (Section [[sec:own-far-part]]). (2) The tail at r^(−5/2) is computed
 (Section [[sec:own-tail]]). (3) The stability theory holds in the half-integer class with the same index sets
-(Section [[sec:own-half-class]]). (4) The constants of the construction from past null infinity are polynomial in
-λ^(−1) at every order, which makes the data of g_λ on ℋ small at every weight that the estimate below uses
-(Sections [[sec:own-orders]] and [[sec:own-sigma]]). (5) After its self-similar terms through r^(−4) are subtracted,
-g_λ continues to W by one weighted energy estimate at a weight a ∈ (ℓ0 − 1, 3), run on bounded domains of dependence,
-whose exponents follow from homogeneity under a dilation; the continuation is vacuum, unique in a class of weight
-below ½, and its data on S lie in the half-integer class with small norm (Sections [[sec:far-homogeneity]],
-[[sec:cutoff-expansion]], [[sec:own-continuation]] and [[sec:own-vacuum]]). The theorem is assembled in Section
-[[sec:own-proof]].
+(Section [[sec:own-half-class]]). (4) The constants of the construction from past null infinity are polynomial in λ^(−1)
+at every order, which makes the data of g_λ on ℋ small at every weight that the estimate below uses
+(Sections [[sec:own-orders]] and [[sec:own-sigma]]). (5) After its self-similar terms through r^(−4) are subtracted, g_λ
+continues to W by one weighted energy estimate at a weight a ∈ (ℓ0 − 1, 3), run on bounded domains of dependence, whose
+exponents follow from homogeneity under a dilation; the continuation is vacuum, unique in a class of weight below ½, and
+its data on S lie in the half-integer class with small norm (Sections [[sec:far-homogeneity]], [[sec:cutoff-expansion]],
+[[sec:own-continuation]] and [[sec:own-vacuum]]). The theorem is assembled in Section [[sec:own-proof]], where the
+development is placed in the maximal globally hyperbolic development of the data ([[lem:own-maximal]]).
 
 *Notation.* We use the chart (τ, x) of [[sec:background]], v = τ + r, the background g0 of [[eq:background]] and the
 gauge of [[sec:gauge]]. Ω′ is the domain of the form [[eq:omega]], with constants (T′, δ′0) and inner radius a′ = q0 −
@@ -55,9 +56,13 @@
 (2) its data (γ, k) on Σ^IVP satisfy γ − γ_b0 ∈ H^(∞,(ℰ_0^½,ℓ0))_b, k − k_b0 ∈ H^(∞,(ℰ_0^½+1,ℓ0+1))_b, with
 ‖(γ − γ_b0, k − k_b0)‖_(d_1) < ε in the norm of [[sec:s27-class]] taken with ℰ_0 = ℰ_0^½;
 
-(3) the maximal vacuum development ĝ of (γ, k) settles to a Tangherlini metric g_(m′,0) with |m′ − μ_end| < ε_m: on
-{r_♭ ≤ r ≤ R′, t_* ≥ t_1}, |(t_*∂_(t_*))^i ∂_x^β (ĝ − g_(m′,0))| ≤ C t_*^(−2−ε_t) for every R′, i and β, with C and t_1
-depending on them.
+(3) (γ, k) have a G-invariant vacuum development ǧ on {t_IVP ≥ 0}, t_IVP being the function of [[lem:iii-b-3-7]] (b),
+with Σ^IVP = t_IVP⁻¹(0), which settles to a Tangherlini metric g_(m′,0) with |m′ − μ_end| < ε_m: on
+{r_♭ ≤ r ≤ R′, t_* ≥ t_1}, |(t_*∂_(t_*))^i ∂_x^β (ǧ − g_(m′,0))| ≤ C t_*^(−2−ε_t) for every R′, i and β, with C and
+t_1 ≥ 1 depending on them. The maximal globally hyperbolic vacuum development (M̂, ĝ, ι̂) of the data (γ, k) on the
+surface without boundary Σ̊ := Σ^IVP ∩ {r > r_♭} contains it: there is a time-orientation-preserving isometric embedding
+Ψ of ({r > r_♭, t_IVP > 0}, ǧ) into (M̂, ĝ) that extends continuously to Σ̊ by ι̂ ([[lem:own-maximal]]). So ĝ settles in
+the same sense: |(t_*∂_(t_*))^i ∂_x^β (Ψ^*ĝ − g_(m′,0))| ≤ C t_*^(−2−ε_t) on {r_♭ < r ≤ R′, t_* ≥ t_1}.
 
 The threshold λ_2 is not evaluated, and ε, d_1, λ_2 depend on the class. The order k_P is what the subtracted
 expansion of Section [[sec:own-sigma]] needs: a Cartesian derivative of order j of its terms costs 2j + 2 angular
@@ -1864,6 +1869,108 @@
 other term lies there. But if c ≠ 0 its modulus is at least |c|ρ²/2, and otherwise it is |a_(5/2)| ρ^(5/2); in either
 case ∫_0 |ρ^(−q)(ρ² c + ρ^(5/2) a_(5/2))|² dρ/ρ = ∞, as q > 5/2. ∎
 
+**Lemma {#lem:own-maximal}** (the development lies in the maximal one). Let (γ, k) be G-invariant vacuum data on Σ^IVP
+as in [[thm:own-half-settling]], below its threshold, and let ǧ be the G-invariant vacuum development given there: the
+metric of [[thm:iii-k-4-3]] on Ω_* ∪ 𝒟_(0,0), with S = S⁰ = 0 ([[prop:vii-3-2]]). Put Σ̊ := Σ^IVP ∩ {r > r_♭} and
+M₊ := {r > r_♭, t_IVP ≥ 0}. Then ǧ is defined on M₊; (Σ̊, γ, k) is initial data in the sense of [Sbi15, p. 11], with
+d = 4; its maximal globally hyperbolic development (M̂, ĝ, ι̂), a globally hyperbolic development that is an extension
+of every other one, exists and is unique up to isometry [Sbi15, Theorem 2.8, p. 12]; and there is a
+time-orientation-preserving isometric embedding Ψ : (M₊ ∖ Σ̊, ǧ) → (M̂, ĝ) that extends continuously to M₊ by ι̂ on Σ̊.
+
+*Proof.* In this proof t is the time of the chart of [[lem:vii-1-2]], as in [[ch:s27]], and not the Kerr–Schild time of
+the far region. *The development.* By [[thm:own-half-settling]] the results of [[ch:s27]] hold in the class ℰ_0^½, and
+by [[prop:vii-3-2]] the map φ_(0,0) is the identity, so ǧ induces (γ, k) on Σ^IVP ([[thm:iii-k-4-3]] (2)); here
+b₀ = (μ_end, 0), and g_(b₀) is g_b0 written in the chart of [[lem:vii-1-2]] ([[lem:interior-chart]] (a)). On Ω_*,
+t_IVP ≥ t_* ≥ t^♭_* ≥ 1 (ψ_IVP ≤ ψ, with ψ of [[eq:iii-b-3-6]], by the proof of [[lem:iii-b-3-7]] (b), and
+[[lem:ii-c-3-2]] (b)); and 𝒟_(0,0) = {t_IVP ≥ 0} ∩ {t^♭_* ≤ T̂ + 2} ([[prop:iii-k-1-2]]), while {t^♭_* > T̂ + 2} ⊂ Ω_*.
+So Ω_* ∪ 𝒟_(0,0) is the part {t_IVP ≥ 0} of the spacetime of [[ch:s27]], which contains M₊. Where t^♭_* ≤ T̂ + ¼c_0, a
+set containing {t^♭_* ≤ 3/2} as T̂ ≥ 2, ǧ = g_(b₀) + h_0 ([[prop:iii-k-4-2]] with S = S⁰ = 0; h_0 := h_(0,0)), the
+metric g_(0,0) of [[lem:iii-k-6-2]] on the region 𝒟 of [[prop:iii-k-1-2]]; it is smooth on 𝒟 up to its boundary
+(the proof of [[prop:iii-k-1-2]]), and dt_IVP is past timelike for it on 𝒟 ([[lem:iii-k-6-2]] (a)). So near each point
+of Σ̊, ǧ is the restriction of a smooth Lorentzian metric, the future unit normal of Σ̊ points into M₊, and ǧ induces
+(γ, k) on Σ̊ with respect to it. On Ω°_*, ǧ − g_(b₀) is small in 𝒢̃^(0,(1,0,0))_(e3b) and t^♭_* is a time function of ǧ,
+as in the proof of [[prop:iii-k-4-2]] ([[lem:s27-below]] (iii)).
+
+*The data, and a development of them.* Σ̊ is the graph t = ψ_IVP(|x|) over the connected set {|x| > r_♭} ⊂ ℝ⁴, an open
+subset of Σ^IVP and, unlike Σ^IVP, which ends at {r = r_♭}, a manifold without boundary, as [Sbi15, p. 11] asks of
+initial data; γ is Riemannian; and (γ, k) satisfies the constraint equations, by the Gauss and Codazzi equations for the
+vacuum metric ǧ. So (Σ̊, γ, k) is initial data in the sense of [Sbi15, p. 11] ([[thm:std-sbierski]]), with d = 4, and
+[Sbi15, Theorem 2.8, p. 12] gives (M̂, ĝ, ι̂). By [Sbi15, Theorem 2.6] ([[thm:std-sbierski]] (3)) the same data have a
+globally hyperbolic development (N, g_N, ι_N). Σ_N := ι_N(Σ̊) is a smooth spacelike Cauchy hypersurface of N, γ being
+Riemannian, so there is a Cauchy time-function h_N on N with Σ_N = h_N⁻¹(0) ([[thm:std-bgp-causal]] (3)); its gradient
+is past directed timelike ([[thm:std-bgp-causal]] (2)), so dh_N is past timelike. We glue the past half of N to M₊, show
+that the result contains a globally hyperbolic development of (Σ̊, γ, k) that contains M₊, and obtain Ψ from the
+maximality of (M̂, ĝ, ι̂).
+
+*The glued space.* N₋ := {h_N ≤ 0} and M₊ are manifolds with boundary Σ_N and Σ̊, as dh_N and dt_IVP do not vanish. Let
+M_gl := (N₋ ⊔ M₊)/∼, where ι_N(y) ∼ y for y ∈ Σ̊, with the quotient topology and the projection π. π maps N₋ and M₊
+homeomorphically onto closed subsets of M_gl: for a closed F ⊂ N₋, the preimage of π(F) is F together with
+ι_N⁻¹(F ∩ Σ_N) ⊂ Σ̊, which is closed, and likewise for M₊. So π(N₋ ∖ Σ_N) and π(M₊ ∖ Σ̊) are disjoint open subsets of
+M_gl, covering the complement of the closed set π(Σ̊), which we write Σ̊.
+
+*Charts, smooth structure, metric, time orientation.* The paragraphs of the proof of [[lem:interior-one-spacetime]] from
+*(i), the charts at Σ* to *(i), time orientation and connectedness* apply with Σ̊, M₊ and ǧ in place of Σ, B and g, and
+with N₋, g_N, N, h_N, n_N and E_N(s, y) := exp^(g_N)_(ι_N(y))(s n_N), n_N the future unit normal of Σ_N, in place of A,
+g_λ, V and D_V(Σ), t_IVP on the side of A, n_λ and E_λ, and with {|x| > r_♭} in place of the shell {r_♭ < |x| < R}. Of
+the common chart of that lemma they use only the following, which hold here: dh_N(n_N) > 0, dh_N being past timelike,
+and dt_IVP(n) > 0, n pointing into M₊; the coordinates x of the graph Σ̊, carried to Σ_N by ι_N, as the coordinates on
+Σ̊ in every chart; that ǧ is near each point of Σ̊ the restriction of a smooth Lorentzian metric; that the two halves
+are closed in M_gl and carried homeomorphically by π; and that a set W_Π is open when it meets the two halves in open
+sets, which here is the definition of the quotient topology. For the connectedness of N₋: through a point p′ ∈ N₋ ∖ Σ_N
+passes an inextendible timelike curve of N, which meets the Cauchy hypersurface Σ_N after p′, h_N increasing along it,
+and between the two it lies in N₋. This gives charts Φ_Π : (−s_0, s_0) × Π → W_Π at the points of Σ̊, homeomorphisms
+onto open sets which, with charts of the two open halves, form a smooth atlas
+(M_gl is Hausdorff and second countable by the next paragraph, which uses only these charts); a smooth Ricci-flat
+Lorentzian metric g_gl on M_gl, equal to g_N and to ǧ off Σ̊, which induces (γ, k) on the smooth spacelike hypersurface
+Σ̊; a time orientation in which the unit normal of Σ̊ is future and which is that of ǧ on π(M₊ ∖ Σ̊); and the
+connectedness of M_gl. Part *(ii)* of that proof then shows that Σ̊ is acausal in M_gl.
+
+*Hausdorff and second countable.* Two points of π(N₋ ∖ Σ_N), or two of π(M₊ ∖ Σ̊), are separated in that open set, and a
+point of each by these two disjoint open sets. Let y ∈ Σ̊ and z ≠ y. If z = π(p′), p′ ∈ N₋ ∖ Σ_N, take disjoint open
+sets U′ ∋ p′ and U_y ∋ ι_N(y) of N with U′ ⊂ N₋ ∖ Σ_N, and Π and s_0 so small that E_N((−s_0, 0] × Π) ⊂ U_y, as
+E_N(0, y) = ι_N(y); then π(U′) and W_Π are disjoint open sets. If z lies in π(M₊ ∖ Σ̊), the same holds with M₊ and the
+map E of that proof in place of N and E_N. If z ∈ Σ̊, take disjoint neighbourhoods of ι_N(y) and ι_N(z) in N and of y
+and z in M₊, and charts W_Π ∋ y and W_Π′ ∋ z whose halves lie in them; then W_Π ∩ W_Π′ = ∅. So M_gl is Hausdorff. Σ̊,
+being second countable, is covered by countably many W_Π, and M_gl is the union of these and of the two open halves,
+each second countable; so M_gl is second countable.
+
+*The development D_gl.* Σ̊ is an acausal smooth spacelike hypersurface of the connected time-oriented Lorentzian
+manifold M_gl. So D_gl := D_(M_gl)(Σ̊) is open and globally hyperbolic, with Σ̊ as a Cauchy hypersurface
+([[thm:std-bgp-development]]); it is connected, every point of it being joined to Σ̊ within it as at the end of the
+connectedness paragraph cited; and with the inclusion ι of Σ̊ it is a globally hyperbolic development of (Σ̊, γ, k)
+[Sbi15, Definition 2.1] ([[thm:std-sbierski]] (1)): connected, time oriented, vacuum, with ι^*g_gl = γ and with second
+fundamental form k with respect to the future normal.
+
+*M₊ lies in D_gl.* Let p ∈ π(M₊ ∖ Σ̊) and let 𝔠 be an inextendible causal curve of M_gl through p, run from p to the
+past. Suppose that 𝔠 does not meet Σ̊. Then it stays in the open set π(M₊ ∖ Σ̊) = {r > r_♭, t_IVP > 0}, the complement
+of Σ̊ being the disjoint union of the two open halves, and it is past inextendible there. First, if t^♭_*(p) > 3/2, 𝔠
+does not stay in {t^♭_* > 3/2}. The part of this set in {r > r_♭} lies in Ω°_*, and the argument of the proof of
+[[lem:ii-f-1-3]] on Ω°_*, with τ := t^♭_*, the level 3/2 and the compact sets L_p ⊂ Ω°_* of [[lem:iii-k-6-1]] (c),
+applied as in the proof of [[prop:iii-k-4-2]], shows that t^♭_* reaches 3/2 along every past directed causal curve from
+p that is past inextendible in Ω°_*; 𝔠 would be one if it stayed in {t^♭_* > 3/2}. Second, from the first point p_1 of 𝔠
+at which t^♭_* ≤ 3/2 (p_1 := p if t^♭_*(p) ≤ 3/2) on, t^♭_* stays at most 3/2: to exceed it, 𝔠 would run in
+{t^♭_* > 3/2}, where t^♭_* is a time function, along an interval starting at a point where t^♭_* = 3/2, and t^♭_*
+decreases to the past along such an interval. Third, beyond p_1, 𝔠 therefore lies in {t_IVP > 0, t^♭_* ≤ 3/2} ⊂ 𝒟, where
+ǧ = g_(0,0): dt_IVP is past timelike there, and r ≤ R_𝔠 := max(R_s, r(p_1)) + 2t_IVP(p_1) along 𝔠 beyond p_1
+([[lem:iii-k-6-2]] (a) and (c), the latter at the level 0; R_s is the radius R of that lemma). So 𝔠 lies in
+L_𝔠 := {0 ≤ t_IVP ≤ t_IVP(p_1), r_♭ ≤ r ≤ R_𝔠, t^♭_* ≤ 3/2}, a closed set, bounded in the coordinates (t, x) as
+t = t_IVP + ψ_IVP(r), hence compact, on which ǧ = g_(0,0) is continuous and dt_IVP is past timelike; parametrised by
+t_IVP, it converges in L_𝔠 to a point q, as in the proof of [[lem:ii-f-1-3]]. q is not in {r > r_♭, t_IVP > 0}, in which
+𝔠 is past inextendible, nor in Σ̊, where 𝔠 would have an end point in M_gl; so r(q) = r_♭. But
+g_(b₀)⁻¹(dr, dr) ≤ −c_r < 0 on {r_♭ ≤ r ≤ r^♮}, with dr future timelike for g_(b₀) there
+(the proof of [[lem:s27-below]] (iv)), and h_0 is small in C⁰ on the compact set 𝒟 ∩ {r ≤ R_s}
+(the proof of [[lem:iii-k-6-2]] (a)), which contains 𝒟 ∩ {r ≤ r^♮}, as r^♮ = ½(r_♭ + 7R₁/8) < R₁ ([[def:s12-radii]])
+while R_s ≥ 5R₁, t_IVP = t − C″ holding on {r ≥ R_s} and ψ_IVP = ψ increasing strictly on [3R₁, 5R₁]
+([[lem:iii-b-3-7]] and its proof). So, as in the proof of [[lem:s27-below]] (iv), dr stays timelike for g_(b₀) + s h_0,
+s ∈ [0, 1], on 𝒟 ∩ {r ≤ r^♮}, and it is future timelike for ǧ there, the time orientation of ǧ on 𝒟 being the one that
+continues that of g_(b₀) ([[lem:iii-k-6-2]] (a)). Hence r increases strictly along 𝔠 towards q near q, and r(q) > r_♭, a
+contradiction. So 𝔠 meets Σ̊, and π(M₊) ⊂ D_gl.
+
+*The embedding.* By [Sbi15, Theorem 2.8], (M̂, ĝ, ι̂) is an extension of (D_gl, g_gl, ι): there is a
+time-orientation-preserving isometric embedding j : D_gl → M̂ with j ∘ ι = ι̂ [Sbi15, Definition 2.2]
+([[thm:std-sbierski]] (2)). Ψ := j ∘ π on M₊ is continuous and equal to ι̂ on Σ̊, and on M₊ ∖ Σ̊, where π is an isometry
+of ǧ onto g_gl that preserves the time orientations, it is a time-orientation-preserving isometric embedding. ∎
+
 *Proof of [[thm:own-data]].* *The order k_P.* By [[cor:own-p-order]] the solution g_λ is the same at every order, and
 the proof uses its bounds at the order k_P = 2k1 + 14 at four places, each of which needs at most k_P. (a)
 [[lem:own-sigma-data]] (a) applies [[lem:own-e-flux]] (1) with i = 0 and |β| ≤ 2k1 + 10, which needs
@@ -1906,8 +2013,12 @@
 So ‖·‖_(d_1) ≤ C(λ + ε_B) < ε for λ ≤ λ_2.
 
 (3) The data are G-invariant (g is), vacuum, in the half-integer class and below the thresholds of [[prop:vii-3-2]] and
-[[cor:s27-rate]]. By [[thm:own-half-settling]] they have a G-invariant vacuum development settling to g_(m′,0)
-with |m′ − μ_end| < ε_m (b₀ = (μ_end, 0)) at the rate O(t_*^(−2−ε_t)) of [[eq:s27-rate]] on
-{r_♭ ≤ r ≤ R′, t_* ≥ t_1}; this development embeds in the maximal vacuum development of (γ, k), which therefore
-settles in the same sense. No gluing is used, and no value of λ ∈ (0, λ_2] is excluded: [[prop:own-transfer]] shows
-only that, off the exceptional set of [[prop:own-tail]] (d), the half-integer class is needed. ∎
+[[cor:s27-rate]]. By [[thm:own-half-settling]] they have a G-invariant vacuum development ǧ, the metric of
+[[thm:iii-k-4-3]] with b = (m′, 0) and S = S⁰ = 0 ([[prop:vii-3-2]]), defined on {t_IVP ≥ 0} ([[lem:own-maximal]]),
+which settles to g_(m′,0) with |m′ − μ_end| < ε_m (b₀ = (μ_end, 0)) at the rate O(t_*^(−2−ε_t)) of [[eq:s27-rate]] on
+{r_♭ ≤ r ≤ R′, t_* ≥ t_1}, t_1 being the T′ of [[cor:s27-rate]] (c), taken at least 1. By [[lem:own-maximal]] the
+maximal globally hyperbolic development (M̂, ĝ, ι̂) of (Σ̊, γ, k) exists, and Ψ embeds ({r > r_♭, t_IVP > 0}, ǧ) in it
+isometrically, preserving the time orientation and extending continuously to Σ̊ by ι̂. On {r_♭ < r ≤ R′, t_* ≥ t_1},
+t_IVP ≥ t_* ≥ 1, so this set lies in the domain of Ψ, and Ψ^*ĝ = ǧ there satisfies the same bound. No gluing is used,
+and no value of λ ∈ (0, λ_2] is excluded: [[prop:own-transfer]] shows only that, off the exceptional set of
+[[prop:own-tail]] (d), the half-integer class is needed. ∎
--- a/crosswalk/63-own-data.tsv
+++ b/crosswalk/63-own-data.tsv
@@ -1,6 +1,6 @@
 label	source	source_name	note
 ch:own-data	paper/RESPONSE-HL-5D.md:1757-1778; docket68/n1star/SETTLE-GLAM5.md:9-36	P Beyond the boundary (own data); SG section 0	intro composed from P's final wording
-thm:own-data	docket68/n1star/SETTLE-GLAM5.md:1942-1971	SG Theorem R5.1 (R6-E..R10-E status: proved)	k_P = 2k1+14 in place of k1+5 (issue-1, proved in the first step of the proof); rate region r_flat as cor:s27-rate; strip from R9.1(iii)(a); 4R >= 8 added to the notation
+thm:own-data	docket68/n1star/SETTLE-GLAM5.md:1942-1971	SG Theorem R5.1 (R6-E..R10-E status: proved)	k_P = 2k1+14 in place of k1+5 (issue-1, proved in the first step of the proof); rate region r_flat as cor:s27-rate; strip from R9.1(iii)(a); 4R >= 8 added to the notation; item (3) restated: the development on {t_IVP >= 0} settles and embeds in the maximal globally hyperbolic development of the data on the open surface (G-SWEEP fix F-G3, via lem:own-maximal)
 sec:own-far-part	docket68/n1star/SETTLE-GLAM5.md:3358-3483	SG R9-B setting	cites lem:interior-far-part (ch 62) for R9.1 (i)-(v)
 eq:own-wedge	docket68/n1star/SETTLE-GLAM5.md:1222-1236	SG R4-D setting	
 lem:own-wedge	docket68/n1star/SETTLE-GLAM5.md:1222-1236, 2779-2790	SG R4-D setting (B4e) and R7-A conormals	the wedge paragraph of proof project G is this lemma's (b)
@@ -122,3 +122,4 @@
 sec:own-proof	docket68/n1star/SETTLE-GLAM5.md:1444-1509, 1973-1974	SG R4-G with R5-E substitutions	
 prop:own-transfer	docket68/n1star/SETTLE-GLAM5.md:145-188	SG Proposition 4.1 and Corollary 4.2	now unconditional (the continuation is constructed); Remark 4.3 dropped
 eq:own-transfer	docket68/n1star/SETTLE-GLAM5.md:150-152, 176-178	SG Prop 4.1 T_p(l)	DLMF (15.4.28)
+lem:own-maximal	G-SWEEP fix F-G3	new	the development of thm:own-half-settling (S = S0 = 0) is defined on {t_IVP >= 0}; glued to the past half of a GHD of the data on Sigma^IVP minus its inner boundary, it lies in a GHD, hence in the maximal one [Sbi15, Theorem 2.8, p. 12]; closes gap G3
```

## Check outputs (run from the paper directory)

```
$ python3 lint.py --chapters
chapters: 62 file(s), 4585 label(s) defined, 0 hit(s)
$ python3 assemble.py --check
labels 4585, computations cited 0, problems 0
$ (resolved-label check of chapter 63: assemble.number/resolve in memory, nothing written)
problems []
resolved ch63 lines >121: []
source ch63 max len: 121  backslashes: 0
wrapped lines with bad start (resolved): []
lem:own-maximal -> Lemma 44.51 ; thm:own-data -> Theorem 44.1
crosswalk labels vs chapter labels, in order: identical
```

`assemble.py` was run only with `--check`. I made no commit; the snapshots are the coordinator's. Other workers' concurrent edits to ch. 84, 90, 95, 98 and STATUS were seen in the tree and were not touched.
