# R2-F-G3: confirming review of the G3 fixes (lem:own-maximal, thm:own-data (3)) and the chapter 62 Seeley sentence

## Verdict

**CONFIRMED.** All eight findings of R-F-G3 (m1, m2, m3, n1–n5) are resolved, and each replacement reads correctly in
context. The chapter 62 Seeley sentence is correct. lem:own-maximal and its proof still hold together line by line. New
findings: Major 0, minor 0, nit 3. Two of the nits concern the new Seeley sentences: the theorem as quoted in Appendix A
applies to a function on a whole half-space, so the local use needs a cut-off, which chapter 48 states and these two
sentences leave out. The third nit is a third site of the n4 imprecision.

Line numbers refer to HEAD 9467a875. chapters/62-interior.md and chapters/63-own-data.md are unchanged since c6816ec3
(`git diff c6816ec3 HEAD` is empty for both), and so are the Appendix A entries cited here (thm:std-seeley,
thm:std-sbierski, thm:std-bgp-causal and thm:std-bgp-development). A word-level diff of c6816ec3 shows that the re-wraps
dropped or changed no words. The only text changes are the eight replacements, the n1 edit at the third site and the
chapter 62 sentence.

## 1. The eight findings

### m1: resolved

63:1875–1876: "Then ǧ is defined on {t_IVP ≥ 0}, which contains M₊; (Σ̊, γ, k) is initial data in the sense of [Sbi15,
p. 11], with d = 4;"

- The statement now contains what the proof establishes at 63:1886–1887: "So Ω_* ∪ 𝒟_(0,0) is the part {t_IVP ≥ 0} of
  the spacetime of [[ch:s27]], which contains M₊." That is correct: 𝒟_(0,0) = {t_IVP ≥ 0} ∩ {t^♭_* ≤ T̂ + 2}, and
  {t^♭_* > T̂ + 2} ⊂ Ω_* ⊂ {t_IVP ≥ 1}.
- "{t_IVP ≥ 0}" is taken in M = cl{|x| ≥ r_♭, t ≥ −½|x|} ([[eq:iii-b-2-1]]), so it does contain
  M₊ = {r > r_♭, t_IVP ≥ 0}.
- Proof item (3) at 63:2019–2020, "defined on {t_IVP ≥ 0} ([[lem:own-maximal]])", now points at a statement of the lemma.
- Statement (3) at 63:59 ("ǧ on {t_IVP ≥ 0}") agrees with it.

### m2: resolved

63:1889–1894: "it is smooth on 𝒟 up to its boundary (the proof of [[prop:iii-k-1-2]]), and dt_IVP is past timelike for it
on 𝒟 ([[lem:iii-k-6-2]] (a)). So near each point of Σ̊, ǧ is the restriction of a smooth Lorentzian metric: of g_(0,0)
where r > R_ν, 𝒟 being a two-sided neighbourhood of Σ^IVP there, and, where r ≤ R_ν, of an extension of g_(0,0) across
{t_IVP = 0} in the coordinates (t_IVP, x) by [[thm:std-seeley]], which is Lorentzian near Σ̊; the future unit normal of Σ̊
points into M₊, and ǧ induces (γ, k) on Σ̊ with respect to it."

The text is the reviewer's replacement word for word. It continues with "; the future unit normal …", which joins the
original continuation correctly.

- *The two cases match [[prop:iii-k-1-2]].* There 𝒟 = N_ν ∩ {t^♭_* ≤ T̂ + 3} with N_ν = {t_IVP ≥ −ν(r)}, ν = 0 on
  [0, R_ν] and ν > 0 on (R_ν, ∞) (46:218–223). Item (1) states: "𝒟, a two-sided neighbourhood of Σ^IVP off
  {r ≤ R_ν}; on {r ≤ R_ν}, 𝒟 ends at Σ^IVP" (46:233–234). A point of Σ̊ with r = R_ν falls under the Seeley case.
  This is correct: near such a point, g_(0,0) restricted to {t_IVP ≥ 0} is smooth up to {t_IVP = 0}.
- *Near Σ̊, ǧ = g_(0,0) on {t_IVP ≥ 0}.* t^♭_* ≤ t_* ≤ t_IVP, by 46:83 and [[lem:ii-c-3-2]] (b). So a neighbourhood
  of Σ^IVP in {t_IVP ≥ 0} lies in {t^♭_* ≤ T̂ + ¼c_0}, where ǧ = g_(b₀) + h_0.
- *Smooth up to the boundary.* The proof of [[prop:iii-k-1-2]] ends with "h_(S,S⁰) is smooth on 𝒟, up to its boundary"
  (46:1105). This is the hypothesis of [[thm:std-seeley]], once a cut-off localises it (nit N2 below).
- *The coordinates.* (t_IVP, x) = (t − ψ_IVP(|x|), x) is a diffeomorphism, since ψ_IVP is smooth by
  [[lem:iii-b-3-7]] (b), and it carries Σ^IVP to {t_IVP = 0}.
- *"Lorentzian near Σ̊".* The extension agrees with g_(0,0) on {t_IVP = 0}, where that metric is Lorentzian, and the
  Lorentzian condition is open. The sentence does not say "by continuity", as chapter 62 does; see N2.
- *Labels.* [[thm:std-seeley]] resolves to Theorem A.33, Seeley's extension theorem.

The reviewer's alternative "(the template sentence 62:231–232 has the same omission)" is also dealt with, by the
chapter 62 edit (section 2).

### m3: resolved

63:2024–2026: "No data are glued (the gluing in [[lem:own-maximal]] joins two developments of the same data), and no value
of λ ∈ (0, λ_2] is excluded: [[prop:own-transfer]] shows only that, off the exceptional set of [[prop:own-tail]] (d), the
half-integer class is needed. ∎"

- The sentence no longer contradicts the step before it.
- The parenthesis is accurate: the lemma glues N₋, the past half of the development N of (Σ̊, γ, k), to M₊, part of the
  development ǧ of the same data.
- The colon clause after it still attaches to "no value … is excluded".

The opening's "with no gluing" (63:5) refers to how the development is obtained, so it does not conflict.

### n1: resolved at all three sites

- 63:1874–1875: "with vanishing boost and translation parameters, S = S⁰ = 0 in the notation of [[ch:s27]]
  ([[prop:vii-3-2]])."
- 63:1888: "([[prop:iii-k-4-2]] with vanishing boost and translation; h_0 := h_(0,0))"
- 63:2019: "the metric of [[thm:iii-k-4-3]] with b = (m′, 0) and vanishing boost and translation ([[prop:vii-3-2]])"

Checks:
- The order "boost and translation" matches S = boost and S⁰ = translation. See 46:40–41, 46:1625 ("S its boost,
  S⁰ := S^(0)_1 its translation") and [[thm:iii-k-4-3]] at 46:1665–1666.
- [[prop:vii-3-2]] (46:1987) gives "b = (m′, 0), S = S⁰ = 0".
- [[ch:s27]] resolves to Chapter 38, where S and S⁰ are introduced.
- The subscripts (0,0) on 𝒟_(0,0), φ_(0,0) and h_(0,0), used from 63:1874 on, are explained by the first site.
- No bare "S = S⁰ = 0" is left in chapter 63 (grep). So S again means only the far part Σ^IVP ∩ {r ≥ 4R}.

The third site (63:1888) was not in the reviewer's replacement list, but it was listed under "Where". The coordinator's
wording there agrees with the other two sites, and the sentence still parses: "ǧ = g_(b₀) + h_0 ([[prop:iii-k-4-2]] with
vanishing boost and translation; h_0 := h_(0,0)), the metric g_(0,0) of [[lem:iii-k-6-2]] …".

### n2: resolved

63:1971: "*The embedding.* By [Sbi15, Theorem 2.8] ([[thm:std-sbierski]] (7)), (M̂, ĝ, ι̂) is an extension of
(D_gl, g_gl, ι):"

Item (7) of [[thm:std-sbierski]] (Theorem A.13; 95:328–331) is Theorem 2.8, quoted. All three Theorem 2.8 citations
(63:1878, 1901, 1971) now carry the pointer.

### n3: resolved

63:1965–1966: "as r^♮ = ½(r_♭ + 7R₁/8) < R₁ ([[lem:ii-c-3-2]], [[def:s12-radii]]) while R_s ≥ R_5 ≥ 3R₁ ([[lem:iii-k-6-2]],
[[sec:iii-k-0]])."

Each cited result says what is used:
- [[lem:ii-c-3-2]] (24:946) defines r^♮ := ½(r₀ + r₂).
- [[def:s12-radii]] (31:45) gives r₀ = r_♭ and r₂ = 7R₁/8, with r_♭ ≤ ½R₁. So r^♮ ≤ 11R₁/16 < R₁.
- [[lem:iii-k-6-2]] (46:1015) states "There is R ≥ R_5".
- [[sec:iii-k-0]] (46:83) defines R_5 := max(R₃, 3R₁).
- So r^♮ < R₁ ≤ R_s, and 𝒟 ∩ {r ≤ r^♮} ⊂ 𝒟 ∩ {r ≤ R_s}.

The removed clause was used nowhere else. [[sec:iii-k-0]] resolves to Section 38.1.

### n4: resolved at both sites listed

- 63:6–7: "and that their maximal globally hyperbolic development, which contains it off the inner boundary, settles with
  it." Here "it" is "a vacuum development" (63:5), which is correct.
- 63:63–64: "contains ǧ off the inner boundary {r = r_♭}: there is a time-orientation-preserving isometric embedding Ψ of
  ({r > r_♭, t_IVP > 0}, ǧ) into (M̂, ĝ) that extends continuously to Σ̊ by ι̂ ([[lem:own-maximal]])."

Both now match the lemma's Ψ : (M₊ ∖ Σ̊, ǧ) → (M̂, ĝ). A third site with the same imprecision, 63:24, was not listed;
see N3.

### n5: resolved

63:1917–1919: "with N₋ in place of A, g_N in place of g_λ, N in place of both V and D_V(Σ), h_N in place of t_IVP on the
side of A, n_N in place of n_λ, and E_N(s, y) := exp^(g_N)_(ι_N(y))(s n_N), n_N the future unit normal of Σ_N, in place of
E_λ, and with {|x| > r_♭} in place of the shell {r_♭ < |x| < R}."

The pairs are now explicit, and I checked each against the template paragraphs 62:228–303:
- O_N ⊂ N stands in for O_λ ⊂ D_V(Σ).
- O_N ∩ {h_N ≤ 0} = O_N ∩ N₋ stands in for O_λ ∩ {t_IVP ≤ 0} = O_λ ∩ A.
- dh_N(n_N) > 0 stands in for dt_IVP(n_λ) > 0.
- E_N(0, y) = ι_N(y), and E_N^*g_N = −ds² + h^N_s with h^N_0 = ι_N^*g_N = γ.

The closing "and with {|x| > r_♭} …" also applies, word for word, to the shell as written in the new chapter 62 Seeley
sentence ("in which Σ is {0} × {r_♭ < |x| < R}"). With the substitutions, that sentence becomes the Seeley argument for ǧ
on M₊, which holds (ǧ is smooth on M₊ up to Σ̊). 63:1919–1922 lists "that ǧ is near each point of Σ̊ the restriction of a
smooth Lorentzian metric" among the facts used, and 63:1890–1893 establishes it. So the two do not conflict.

## 2. The chapter 62 Seeley sentence (62:231–234)

Current text: "Near p, g is the restriction to B of a smooth Lorentzian metric g̃ on an open set of ℝ × ℝ⁴, g being smooth
up to Σ: in the coordinates (t − ψ_IVP(|x|), x), in which Σ is {0} × {r_♭ < |x| < R}, [[thm:std-seeley]] extends each
component of g smoothly across Σ, and the extension is Lorentzian near Σ by continuity."

**Correct, with one omission (nit N1).**

- *The coordinates flatten Σ as stated.*
  - Σ is the graph t = ψ_IVP(|x|) over the open shell (62:229–230). (t, x) ↦ (t − ψ_IVP(|x|), x) is a
    diffeomorphism of ℝ × {r_♭ < |x| < R}, with inverse (s, x) ↦ (s + ψ_IVP(|x|), x), since ψ_IVP is smooth
    ([[lem:iii-b-3-7]] (b)). It carries Σ onto {0} × {r_♭ < |x| < R}.
  - By *A and B are manifolds with boundary Σ* (62:213–216), B ∩ N = N ∩ {t_IVP ≥ 0} for a neighbourhood
    N ⊂ {r_♭ < |x| < R} of a point of Σ. So B is the closed half {s ≥ 0} near p.
- *What [[thm:std-seeley]] gives* (Theorem A.33, 95:730–734). Let S₊ = ℝⁿ × {t > 0}, and let D₊ be the functions smooth
  on S₊ whose derivatives all have continuous limits as t → 0+. Seeley gives an extension operator
  E : D₊ → C^∞(ℝ^(n+1)) with Ef = f for t > 0. "g is smooth on B up to Σ" (62:217) is the D₊ condition, held locally.
  But g is defined only on B, not on the whole of {s > 0} × ℝ⁴. So the theorem applies to χg_ij, where χ is a cut-off
  that equals 1 near p and is supported in ℝ × {r_♭ < |x| < R}. Then χg_ij, extended by zero, lies in D₊ (n = 4), and
  E(χg_ij) is smooth and equals g_ij near p on {s ≥ 0}.
  - The extension is symmetric, since E is linear.
  - Chapter 48 states this step in its own use of the theorem: "apply Seeley's extension operator ([[thm:std-seeley]])
    in each chart {t_IVP ≥ 0}, after a cut-off, and patch" (48:422–424).
  - The sentence omits the cut-off. With the cut-off, the extension is a metric only near p, not "near Σ".
  - The sentence's scope ("Near p, g is …") makes the intended reading clear. The step is routine, so this is a nit.
- *"Lorentzian near Σ by continuity" is justified.* Ef is continuous and equals f for s > 0, so the extension equals g
  on Σ near p. There g is Lorentzian: Σ is spacelike for it (62:217), and B carries the Lorentzian metric g up to Σ.
  The Lorentzian symmetric matrices form an open set, so the extension is Lorentzian near p.
- *Use downstream.* Only the existence of some smooth extension g̃ is used. The geodesics Ẽ(σ, x), σ ∈ [0, s], lie in
  B, where g̃ = g, "whatever the extension g̃" (62:244–245).
- *Typography.* Every line is at most 121 characters, both in the source and after label resolution. No line starts with
  a forbidden marker, and the label resolves.

## 3. lem:own-maximal and its proof, end to end (63:1872–1974)

I found no error, gap or unjustified step. The argument still holds together after the edits. Checked step by step:

- **Statement (1872–1879).**
  - Hypotheses and the definition of ǧ are as in [[thm:own-half-settling]] (63:272–278) and [[thm:iii-k-4-3]]
    (46:1665–1667) with S = S⁰ = 0.
  - The conclusions are (a) ǧ on {t_IVP ≥ 0}, (b) initial data in the sense of Sbi15, (c) the MGHD, and (d) Ψ. Each
    is proved below.
- ***The development* (1881–1895).**
  - t_IVP ≥ t_* ≥ t^♭_* ≥ 1 on Ω_*, since ψ_IVP ≤ ψ by the proof of [[lem:iii-b-3-7]] (b) (30:854–857).
  - The union is {t_IVP ≥ 0} (m1).
  - ǧ = g_(b₀) + h_0 on {t^♭_* ≤ T̂ + ¼c_0}, by [[prop:iii-k-4-2]] (46:1628) with ĝ_(0,0) = g_(b₀). T̂ ≥ 2 and
    c_0 > 0, so this set contains {t^♭_* ≤ 3/2}.
  - The m2 sentence: see section 1.
  - On Ω°_*, the time function t^♭_* and the smallness are as in the proof of [[prop:iii-k-4-2]] (46:1647–1651).
- ***The data* (1897–1907).**
  - Σ̊ ≅ {|x| > r_♭} ⊂ ℝ⁴ is connected and has no boundary. γ is Riemannian. The constraints hold by Gauss–Codazzi.
  - Theorem 2.6 gives N. ι_N is an embedding and ι_N(Σ̊) is Cauchy (Definition 2.1). So Σ_N is a smooth spacelike
    Cauchy hypersurface.
  - BGP Theorem 1.3.13 gives h_N. Its gradient is past directed timelike, by the definition quoted in
    [[thm:std-bgp-causal]] (2), so h_N increases to the future.
- ***The glued space* (1909–1913).**
  - For closed F ⊂ N₋, π⁻¹(π(F)) = F ⊔ ι_N⁻¹(F ∩ Σ_N). This set is closed, since ι_N : Σ̊ → Σ_N is a homeomorphism and
    Σ̊ is closed in M₊.
  - π is injective on each half, so each half is carried homeomorphically onto a closed set. The two open halves
    cover the complement of π(Σ̊).
- ***Charts, …* (1915–1930).** These are the template paragraphs with the substitutions (n5).
  - W_Π is open: its preimage is (O_N ∩ N₋) ⊔ (O ∩ M₊), since O_N ∩ Σ_N = E_N({0} × Π) = ι_N(Π) = ι_N(O ∩ Σ̊).
  - N₋ is connected by the replacement sentence.
  - M₊ ∖ Σ̊ is connected, as the region above a graph.
  - Part (ii) needs only that s increases along future causal curves in each chart and that Σ̊ is closed.
- ***Hausdorff and second countable* (1932–1939).**
  - All three cases hold. In the first, π(U′) misses W_Π because π is injective on N₋ and U′ ∩ U_y = ∅.
  - Σ̊ is Lindelöf, so countably many W_Π cover it. Each W_Π is homeomorphic to (−s_0, s_0) × Π.
- ***D_gl* (1941–1946).**
  - [[thm:std-bgp-development]] applies to the acausal smooth spacelike Σ̊ and gives an open, globally hyperbolic D_gl
    with Σ̊ Cauchy.
  - D_gl is connected by the "later use" argument (62:294–303).
  - It satisfies Definition 2.1 with ι.
- ***M₊ lies in D_gl* (1948–1969).**
  - *Reduction.* The past half 𝔠 from p, if it misses Σ̊, stays in the open set π(M₊ ∖ Σ̊), because the complement of Σ̊
    is two disjoint open sets and 𝔠 is connected. It is then past inextendible there.
  - *First step.* {t^♭_* > 3/2} ∩ {r > r_♭} ⊂ Ω°_* ⊂ π(M₊ ∖ Σ̊). So a curve that stays there is past inextendible in
    Ω°_*.
    - L_p of [[lem:iii-k-6-1]] (c) (46:965–967) lies in Ω°_*, since t^♭_* ≥ 3/2 > 1 and r ≥ min(r(p), r^♮) > r_♭ on it.
    - The argument at 27:262–267 then gives a contradiction.
  - *Second step.* Take a component of {t^♭_* > 3/2} along 𝔠 after p_1. Its end towards p_1 has t^♭_* = 3/2, because
    the boundary of the open set {t^♭_* > 3/2} lies in {t_* ≥ 3/2}, where t^♭_* is defined and continuous. t^♭_*
    strictly decreases to the past on the component, which is a contradiction.
  - *Third step.*
    - {t_IVP > 0, t^♭_* ≤ 3/2} ⊂ 𝒟, and ǧ = g_(0,0) there.
    - t_IVP decreases to the past.
    - [[lem:iii-k-6-2]] (c) at c = 0 gives R_𝔠.
    - L_𝔠 is closed and bounded in (t, x), hence compact.
    - The t_IVP-parametrised curve converges, as at 27:263–267.
    - q ∉ π(M₊ ∖ Σ̊), by past inextendibility there. q ∉ Σ̊, since π is continuous on M₊, so 𝔠 would have an end point
      in M_gl. Hence r(q) = r_♭.
    - dr is future timelike for ǧ on 𝒟 ∩ {r ≤ r^♮} (n3 and the proof of [[lem:s27-below]] (iv)). So r increases
      strictly to the past near q, and r(q) > r_♭, a contradiction.
- ***The embedding* (1971–1974).**
  - j comes from Theorem 2.8 and Definition 2.2. Ψ = j ∘ π is defined on M₊ because π(M₊) ⊂ D_gl.
  - Ψ is continuous, and Ψ = j ∘ ι = ι̂ on Σ̊.
  - On M₊ ∖ Σ̊, π is an orientation-preserving isometric diffeomorphism onto an open subset of D_gl. j is an isometric
    embedding, that is, a diffeomorphism onto its image (Sbierski's footnote 19). So Ψ is an isometric embedding there.

Proof item (3) of [[thm:own-data]] (63:2017–2027) uses exactly this: on {r_♭ < r ≤ R′, t_* ≥ t_1}, t_IVP ≥ t_* ≥ 1 > 0,
so the set lies in M₊ ∖ Σ̊, the domain of Ψ.

## New findings

### N1 (nit). Chapter 62: the Seeley extension needs a cut-off, and is Lorentzian near p, not near Σ

- **Where:** 62:233–234.
- **What is wrong:**
  - [[thm:std-seeley]] extends functions in D₊, which are defined on the whole half-space ℝ⁴ × {s > 0}.
  - g is defined only on B. Applied "to each component of g", the theorem needs a cut-off near p first, as chapter 48
    states at 48:423 ("after a cut-off").
  - After the cut-off, the extension is a Lorentzian metric near p, not near all of Σ.
- **Replacement (re-wrap the paragraph; a greedy wrap at 120 gives eight lines, none starting with a marker):**
  - old: "[[thm:std-seeley]] extends each component of g smoothly across Σ, and the extension is Lorentzian near Σ by
    continuity."
  - new: "[[thm:std-seeley]], applied to each component of g multiplied by a cut-off that equals 1 near p and is supported
    in a neighbourhood of p in ℝ × {r_♭ < |x| < R}, extends that component smoothly across Σ near p, and the extension
    is Lorentzian near p by continuity."

### N2 (nit). Chapter 63: the same cut-off, and an ambiguous "which"

- **Where:** 63:1892–1893.
- **What is wrong:**
  - The cut-off is omitted, as in N1.
  - "by [[thm:std-seeley]], which is Lorentzian near Σ̊" lets "which" attach to the theorem, the nearest noun, rather
    than to "an extension".
  - Unlike chapter 62, the sentence gives no reason for "Lorentzian".
- **Replacement (re-wrap the paragraph 63:1881–1895; a greedy wrap at 120 gives fifteen lines, none starting with a
  marker):**
  - old: "of an extension of g_(0,0) across {t_IVP = 0} in the coordinates (t_IVP, x) by [[thm:std-seeley]], which is
    Lorentzian near Σ̊;"
  - new: "of an extension of g_(0,0) across {t_IVP = 0}, given in the coordinates (t_IVP, x) by [[thm:std-seeley]] applied
    after a cut-off near the point, and Lorentzian near the point by continuity;"

### N3 (nit). A third site of the n4 imprecision

- **Where:** 63:24, at the end of the overview: "where the development is placed in the maximal globally hyperbolic
  development of the data ([[lem:own-maximal]])."
- **What is wrong:** n4 corrected "contains it" at 63:6 and 63:63, because only the part of ǧ over {r > r_♭} embeds.
  "is placed in" says the same as the old wording.
- **Replacement (re-wrap 63:23–24, for example as "… where the" / "development is placed, off its inner boundary, in the
  maximal globally hyperbolic development of the data" / "([[lem:own-maximal]]).", which keeps every line under 121
  characters):**
  - old: "where the development is placed in the maximal globally hyperbolic development of the data
    ([[lem:own-maximal]])."
  - new: "where the development is placed, off its inner boundary, in the maximal globally hyperbolic development of the
    data ([[lem:own-maximal]])."

*Not counted.* The ragged wrap at 63:1903–1905 that R-F-G3 noted ("…h_N⁻¹(0)" / "([[thm:std-bgp-causal]] (3)); its
gradient" / "is past directed …") is unchanged. It is cosmetic and does not break the contract.

## Checks run (from the reader directory; nothing written to the repository)

- `python3 lint.py --chapters` → `chapters: 62 file(s), 4593 label(s) defined, 0 hit(s)`. The chapter 33 hit mentioned
  in the brief did not appear at this HEAD.
- `python3 assemble.py --check` → `labels 4593, computations cited 0, problems 0`.
- I resolved all labels of chapters 62 and 63 in memory with the assembler's `number`, using the same substitution as its
  `resolve`.
  - No unresolved label.
  - No line over 121 characters.
  - The labels resolve to: lem:own-maximal = Lemma 44.51, thm:own-data = Theorem 44.1, thm:std-sbierski = Theorem A.13,
    thm:std-seeley = Theorem A.33, lem:ii-c-3-2 = Lemma 15.35, def:s12-radii = Definition 22.1,
    lem:iii-k-6-2 = Lemma 38.14, sec:iii-k-0 = Section 38.1, ch:s27 = Chapter 38.
- No line in 63:1–12, 55–66, 1870–1975, 2015–2028 or 62:225–240 starts with "+ ", "- ", "* ", "> ", "#", "=" or "|",
  except the chapter heading at 63:1.
