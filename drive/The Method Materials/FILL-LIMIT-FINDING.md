# FILL-LIMIT — THE TOWER'S LIMIT IS UNDECIDABLE FROM ADMISSIBILITY ALONE

Computed by `fill_limit.py` over `tower-1.py`. Answers `REQUEST-to-method-project-FILL-LIMIT.md`
(book-build chat 61, MC-33) against §12.11.0.11 and R 333: *the limit lies in [0, 0.42%] while its
value does not follow.* The request asks which of (A) a convergence theorem, (B) a rate law for
admissibility, or (C) a certified-open verdict is true. **(C) is true and is now proved; (B) is settled
in its counterexample branch; (A) is answered in the negative.** Method project, 2026-08-29.

## 0 · The verdict, for MC-33

**The construction's own admissibility criterion leaves L anywhere in [0, fill(Λ₁₃)).** Under that
criterion — a new coordinate is admissible iff its bounds are lattice morphisms of the stage below
(`A.morph`, M §18.4.1, Birkhoff 1940) — there are continuations of Λ₁₃ with **L = 0** (Σ(1 − ratio)
diverges), continuations with **L = 0.031146% > 0** (Σ converges, ratio → 1), and continuations with
**L arbitrarily close to fill(Λ₁₃) = 0.416801%**. No constrained continuation attains fill(Λ₁₃), because
the book's own law makes the fourteenth ratio strictly below one. So the bracket is tight at both ends:
*0 is attained, 0.416801% is the supremum and is not attained.* The one sharpening the construction
supports is that the bracket is right-open. **What decides L is the clause the exhibits lack by
construction: a bound "derives from a law independent of the index" (M, the envelope clause, ch. 18).**
That law is the physics that stopped being supplied at thirteen. The existence of L is the law's; its
value is the world's.

## 1 · Definitions, as the corpus states them

For stage D: cells(D) = |Λ_D|; box(D) = product of each coordinate's realised value-count;
fill(D) = cells/box; ratio(D) = fill(D)/fill(D−1) = (mean multiplicity of the new axis)/(its value-count).
A new axis t is a range [lo(x), hi(x)] on each cell x of the stage below. It is **admissible** iff lo and hi
are lattice morphisms of that stage, which makes the new stage a sublattice of its box — E = 0 (§14.1,
Bergman; E2). It is **constrained** iff the range is not the same on every cell; the book's law
(§12.11.0.11) is that a constrained axis has ratio < 1.

The tower's five axes are all of this form, and there are only three types among them:
a cap by a projection (2S′ ≤ g; 2J_c ≤ φ̂(k)), a chain (2S′ ≤ v ≤ g), a translated cap
(2K ≤ 2J_c + 2f_max) and a window (|2J − 2K| ≤ 1). **The three exhibits below are these types,
iterated past Λ₁₃. Nothing is adjoined that the tower has not already adjoined.**

## 2 · The tower, rebuilt (route 1 of the request's table)

    D      cells          box      fill%     ratio
    8        976          6,912   14.1204
    9      1,654         27,648    5.9823    0.4237
    10     2,535        110,592    2.2922    0.3832
    11    13,585        663,552    2.0473    0.8932
    12    70,905      5,308,416    1.3357    0.6524
    13   199,130     47,775,744    0.4168    0.3120

*Every figure in the request reproduces exactly from `tower-1.py`.* The closure instrument of
`fill_limit.py` (E = |ℛ(X)| − |X| against every cell of the box) returns **E = 0 at Λ₈, Λ₉, Λ₁₀, Λ₁₁** —
R 249 reproduced — before it is pointed at anything new. The g-distribution of Λ₁₃, on which every
closed form below rests, is *c(g) = 35,630 · 72,480 · 76,140 · 14,880 for g = 0, 1, 2, 3.*

## 3 · Theorem

Let Λ₁₃ be the tower's top. Under morphism-admissibility:

(i) **There is an admissible continuation with L = 0.** Q: t₁ ∈ [0, g], t_i ∈ [0, t_{i−1}].
(ii) **There is an admissible continuation with L > 0.** P: t_i ∈ [0, g] for every i.
(iii) **For every ε > 0 there is an admissible continuation with L > fill(Λ₁₃) − ε.**
T: t_i ∈ [0, g + M_i], M_i = M₀·2^{i−1}.
(iv) **No constrained continuation attains fill(Λ₁₃)**, since ratio(14) < 1 by the book's law.

Hence inf L = 0 (attained), sup L = fill(Λ₁₃) (not attained), and the ratio of an admissible constrained
axis is not confined to any interval [r₀, r] with r < 1: it approaches 1 in P and T and stays at 1/4 in Q.
**No law relating an admissible axis's mean multiplicity to its value-count follows from admissibility.**

## 4 · Proofs

**Closure, all three.** Each stage is {(x, t₁ … t_m) : x ∈ Λ₁₃, lo_i ≤ t_i ≤ hi_i}, where every lo_i and hi_i
is a projection, or a translate of a projection, of coordinates below it. Joins and meets in a product of
chains are componentwise max and min, and projections commute with both; so the join and the meet of two
cells satisfy the same bounds, and the stage is a sublattice of its box. E = 0. This is exactly the E2 /
`A.morph` condition, and it was also measured: *23 exhaustive closure tests on P, Q and T over the bases
Λ₈–Λ₁₁ (boxes to 2.65 million), E = 0 in every case; the eight tests whose box exceeded the bound were
refused, not run.* Λ₈ + P¹ has 1,654 cells and Λ₈ + Q² has 2,535 — **the continuations reproduce Λ₉
and Λ₁₀ because they are the tower's own operations.**

**P (L > 0, ratio → 1).** Multiplicity depends on g only, so cells(13+m) = Σ_g c(g)(g+1)^m and
box(13+m) = box(13)·4^m; fill(13+m) = Σ_g c(g)((g+1)/4)^m / box(13) → c(3)/box(13).
1 − ratio(13+m) = Σ_{g<3} c(g)(g+1)^{m−1}(3−g) / (4 Σ_g c(g)(g+1)^{m−1}) = O((3/4)^m), so Σ(1 − ratio) < ∞.
*L_P = 14,880 / 47,775,744 = 0.031146%.* Measured: ratio 0.5882, 0.6664, … 0.9547 (m = 12), 0.9947 (m = 20),
0.99998 (m = 40); fill 0.2452% → 0.031146%.

**Q (L = 0, ratio → 1/4).** cells(13+m) = Σ_g c(g)·C(g+m, m) ≤ 199,130·C(m+3, 3), a cubic in m, against
box(13)·4^m; so fill → 0. ratio(13+m) = cells(13+m) / (4 cells(13+m−1)) → 1/4 because
C(g+m, m)/C(g+m−1, m−1) = (g+m)/m → 1; hence Σ(1 − ratio) = ∞. Measured: ratio 0.5882, 0.4582, … 0.2993
(m = 12), 0.2669 (m = 40); fill 1.8e−6 % at m = 12, 4.4e−22 % at m = 40.

**T (L → fill(Λ₁₃)).** The axis t_i ∈ [0, g + M_i] realises M_i + 4 values and has multiplicity g + M_i + 1,
so 1 − ratio = (3 − ḡ)/(M_i + 4) ≤ 3/M_i with ḡ the stage's mean g. With M_i = M₀·2^{i−1},
Σ(1 − ratio) ≤ 6/M₀ and L_T ≥ fill(Λ₁₃)·(1 − 6/M₀). Measured L_T / fill(Λ₁₃): *0.8358 (M₀ = 16) ·
0.9516 (64) · 0.9873 (256) · 0.9968 (1024)*, each above its bound. The axis is constrained (cells with g < 3
carry fewer values), so the book's law holds at every step and (iv) applies: L_T < fill(Λ₁₃).

**Stage 14 is shared.** P and Q adjoin the same fourteenth axis: *468,530 cells, ratio 0.5882, fill
0.2452%.* They part at stage 15. **The fourteenth stage does not know which limit it is heading for.**
Six built stages could not fix the asymptotics, and the theorem says why: neither can any finite number.

## 5 · What this does and does not say

- It proves the sentence the book already prints — *nothing in the construction forbids them approaching
  one and the limit settling above zero* — and upgrades "the question the construction leaves open" to
  **provably undecidable from the morphism criterion alone**, which is the request's outcome (C).
- It is not a statement about the fourteenth axis. §32.1.4: ℛ never produces a coordinate. P, Q and T are
  admissible drawings, not laws; none is proposed as physics. Where no certificate exists, **E measures
  the world, not the drawing** — and here the world has not yet supplied the axis.
- It does not touch A.cert. The tower adjoins coordinates to a closed index and stays closed (E2); A.cert's
  refusal of add-a-coordinate concerns repairing an OPEN index (Theorem 10.1). Different operations.
- The prior art is all standard and the book already cites the half of it that matters: the infinite-product
  criterion Π aᵢ → 0 iff Σ(1 − aᵢ) = ∞; Bergman / Baker–Pixley 1975 for the closure test; Birkhoff 1940 for
  the morphism criterion; Weierstrass for the limit. No novelty is claimed for the machinery. The content is
  two-sided tightness under the corpus's own admissibility criterion.

## 6 · Downstream flags, closed

- The request's line reference ("line 2972") is a BUILD56 line; in the pressed book text the law sits at
  L3320 and §12.11.0.11 at L3327–3357. Different builds, not a fault — cite by section.
- 0.42% (book, R 333) and 0.417% (request) are both roundings of 0.416801%.
- **Self-correction.** The first run of `fill_limit.py` was piped through `head`, which closed the pipe at
  sixty lines and killed the process mid-segment 4; the results file was truncated at Λ₈. Rerun to file.
  No figure changed. Registered here rather than hidden.
- `tower-1.py` is banked with this finding unchanged, under its uploaded name; `fill_limit.py` loads it by
  path.

## 7 · Files

`fill_limit.py` · `FILL-LIMIT-RESULTS.txt` (83 lines, the full measurement) · `tower-1.py` ·
`REQUEST-to-method-project-FILL-LIMIT.md` · slip `01-fill-limit.md`.
