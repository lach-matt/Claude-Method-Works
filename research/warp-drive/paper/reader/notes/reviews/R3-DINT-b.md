# R3-DINT-b: confirming reading of f8a5e9ff (chapter 71: N1–N3 and the four conjugates; chapter 03: the qualifier)

Reader R3-DINT-b. I changed nothing in the repository. Tree read at HEAD f8a5e9ff.
- chapters/03-theorems.md and chapters/71-explicit-constants.md in the working tree are byte-identical to f8a5e9ff
  (cmp). Chapter 71 has 4,383 newline-terminated lines (4,381 before; N1 and the rewrap at l. 568–575 each add one).
- During my reading, chapters/90-scope.md acquired an uncommitted change in the working tree (mtime 10:02:50 UTC). It
  is not part of f8a5e9ff and not mine. To keep the tool results attributable, I ran the three tools both in the working
  tree and in a clean export of f8a5e9ff (git archive); the last lines are the same.
- Scratch work: `.../scratchpad/reader/scratch/r3_dint_b/` (parent and commit copies of both chapters, the word-diff
  script, the snapshot).

## Verdict

**CONFIRMED: 0 Major, 0 minor, 0 nits.**
- N1–N3 of R2-DINT-b are resolved, in the reviewer's words, and each new sentence is true where it stands.
- The four starred formulas are correct, and they are correct for matrix-valued symbols, which the old barred forms
  were not. The rest of each proof is unaffected.
- The chapter 03 qualifier is true and now matches 00:33, 01:154, 71:20–21 and 90:70.
- No text was lost or duplicated in any rewrapped paragraph. The contract holds.

## One row per edit

| edit | site | resolved / correct | note |
|---|---|---|---|
| N3 | 71:3–8 | yes | Reviewer's words verbatim (word sequence identical to R2-DINT-b's replacement; the coordinator rewrapped from l. 3, so the paragraph stays 6 lines, not 7). True: [[thm:ii-g-2-1]] (29:78–79) lets ε depend on d, δ, η_0, C_1, C_2 and the C_k, C_(s,t) with k, s, t ≤ N_NM. It matches thm:loss-d (71:1430) and 46:1252, 1264 and 1527–1528. It no longer reads as a data order (the data are asked small up to N_NM + k″, 46:1252–1253). |
| N1 | 71:28–31 | yes | Verbatim, line for line (source lengths 116, 109, 105, 63). True, see check (b). |
| N2 | 71:512 | yes | Verbatim. "both" = [[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]]. [[prop:fwd-calculus]] (71:898–915) proves (a)–(f) of the first and (a), (b) of the second with counts, so "We prove both again" is true. |
| conj. 1 | 71:570–571 | correct | K(x, y) = (2π)^(−n) ∫ e^(i(x−y)·ξ) p_I(x, ξ) p_(I′)(y, ξ)^* dξ. Derivation in check (c). The gloss "the star denoting the conjugate transpose" is the first statement of the convention in reading order. |
| conj. 2 | 71:577 | correct | L(ξ, η) = ∫ e^(ix·(η−ξ)) p_I(x, ξ)^* p_(I′)(x, η) dx. The factors are in the right order for matrices. This is the kernel with respect to (2π)^(−n)dη (observation 1). |
| conj. 3 | 71:673 | correct | η̃^*(x, y) := (ψη_0)(Φ(x, y)(y − x))^* is the complex conjugate of the scalar cut-off. That agrees with 71:672 (the star on g) and 71:964 ("the conjugate for scalar a"). It is exactly the cut-off that the adjoint kernel produces, see check (d). |
| conj. 4 | 71:685–686 | correct | The L²(μ_α dx) adjoint of an operator with kernel K^#(x, y) has kernel μ_α(x)⁻¹ K^#(y, x)^* μ_α(y). The same substitution then gives c^* of [[eq:fwd-transport]] term by term (check (d)). |
| qualifier | 03:351–357 | yes | "at one admissible choice of the weights, orders and inner products ([[thm:uc-integer]])". True: thm:uc-integer (71:2452–2454) holds at the weights of def:uc-choice and the free orders and inner products of def:cs-choices (a)–(h). This closes R2-DINT-b's observation 2: all four summaries now name the orders and inner products. |

## What I checked

### (a) No text lost or duplicated

I ran a word-level diff (difflib, autojunk off) of each chapter at f8a5e9ff^ against f8a5e9ff, over whitespace-split
words, so a rewrap shows as no change.
- Chapter 03: one change site, "weights" → "weights, orders and inner products" (5,551 → 5,555 words).
- Chapter 71: eleven change sites (68,952 → 68,980 words), and each one is an edit of the commit:
  - N3: "is" inserted, "asks smallness in" → "applied at", and "6." → "6, the order up to which its smallness threshold
    reads the constants of its hypotheses.";
  - N1: "Other" → "Apart from the chapters that restate its bounds, two", and "it," → "it:";
  - N2: "them" → "both";
  - the four conjugates, with the gloss "the star denoting the conjugate transpose." appended at the first one.
- No other word moved in the rewrapped paragraphs 71:3–8, 71:28–31, 71:568–575 and 03:351–357.

### (b) N1 is true where it stands

- Outside chapter 71, its labels are cited at 01:150, 154, 187; 03:353, 354, 357; 23:1072, 1470; 25:30; 33:3236;
  62:577; and 90:58–82, 228.
- Explicit values from chapter 71 appear outside it only in two places:
  - restatements of its bounds at 00:34, 01:153–154 and 90:59–71;
  - the values of chapters 23 and 25: d_0 = 200Θ + 100 (23:1071), M := 200Θ + 98 (23:1467), and N′ = 13 (25:29).
- [[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]] are both defined in chapter 23, and [[ch:s06]] is chapter 25. So "two
  chapters" is exact.
- 33:3236 and 62:577 cite labels but state no value, and the remaining hits for these numbers, in chapter 96, are
  coincidental table entries.
- "these values are used only in this chapter" still holds: 23:1072, 1470 and 25:29–30 are parenthetical, and no proof
  outside chapter 71 uses them.

### (c) The kernels of lem:fwd-l2

The chapter sets Op(p)u(x) = (2π)^(−n) ∫ e^(ix·ξ) p(x, ξ) û(ξ) dξ (71:513) and T_I := Op(p_I) (71:563). The adjoint is
that of L²(ℝⁿ, dx), with the conjugate transpose on fibres.

1. **The kernel of T_I.** With û(ξ) = ∫ e^(−iy·ξ) u(y) dy, T_I has kernel (2π)^(−n) ∫ e^(i(x−y)·ξ) p_I(x, ξ) dξ.
2. **The adjoint T_(I′)^*.** Its kernel is the conjugate transpose of T_(I′)'s kernel at (y, x):
   (2π)^(−n) ∫ e^(i(x−y)·ξ) p_(I′)(y, ξ)^* dξ.
   Hence (T_(I′)^*v)^(ξ) = ∫ e^(−iy·ξ) p_(I′)(y, ξ)^* v(y) dy, which is supported in the ξ-support of p_(I′), as
   71:568 says.
3. **The product T_I T_(I′)^*.** Inserting step 2 into T_I gives
   T_I T_(I′)^*v(x) = (2π)^(−n) ∫∫ e^(i(x−y)·ξ) p_I(x, ξ) p_(I′)(y, ξ)^* v(y) dy dξ.
   That is the kernel printed at 71:570, with the factors in the order T_I, T_(I′)^*.
4. **The product T_I^*T_(I′) on the Fourier side.** Inserting T_(I′)u into the formula of step 2 (with I in place
   of I′) gives
   (T_I^*T_(I′)u)^(ξ) = ∫ L(ξ, η) û(η) (2π)^(−n) dη, with L(ξ, η) = ∫ e^(ix·(η−ξ)) p_I(x, ξ)^* p_(I′)(x, η) dx.
   That is 71:577 exactly, with respect to the measure (2π)^(−n)dη.

**The old forms.** The barred forms p_I p̄_(I′) and p̄_I p_(I′) agree with these only for scalar symbols. For
matrix-valued symbols they lack the transpose. The starred forms are right in both cases.

**The rest of the proof.**
- The ξ-derivatives of p_(I′)(y, ξ)^* are (∂_ξ p_(I′))^*, with the same norms. So the twelve integrations by parts,
  the bound CA²b^(n−12), Schur's test and the sum over I′ (71:571–575) are unchanged.
- Likewise for the x-integrations in L and the two cases |j − j′| ≤ 2 and |j − j′| ≥ 3 (71:577–584).

### (d) The adjoint in lem:fwd-transport

**The adjoint in L²(μ_α dx).** Let A have kernel K^#(x, y) with respect to dy. From ⟨Au, v⟩_μ = ⟨u, A^*v⟩_μ,
A^*v(x) = μ_α(x)⁻¹ ∫ K^#(y, x)^* μ_α(y) v(y) dy.
So the kernel is μ_α(x)⁻¹ K^#(y, x)^* μ_α(y), as at 71:685–686. μ_α is a positive scalar, so its place in the product
does not matter.

**The two kernels.** In the chart α, O^ε_β(g) has kernel K^#(x, y) = K(κ(x), κ(y))|det Dκ(y)| (71:684). Here
K(X, Y) = (2π)^(−n) ∫ e^(i(X−Y)·ξ) (ψη_0)(X − Y) g_β(X, ξ) dξ.
Therefore
K(κ(y), κ(x))^* = (2π)^(−n) ∫ e^(−i(κ(y)−κ(x))·ξ) [(ψη_0)(κ(y) − κ(x))]^* g_β(κ(y), ξ)^* dξ.

**The substitution.**
- κ(y) − κ(x) = Φ(x, y)(y − x).
- So the phase is i(x − y)·Φ^Tξ, and the cut-off is (ψη_0)(Φ(x, y)(y − x))^* = η̃^*(x, y).
- With ξ = Φ^(−T)η, dξ = |det Φ|⁻¹ dη.
- Multiplying by θ(x) gives
  θ(x) η̃^*(x, y) (μ_α(y)/μ_α(x)) g_β(κ(y), Φ^(−T)η)^* |det Φ|⁻¹ |det Dκ(x)|.
  That is c^* of [[eq:fwd-transport]] (71:668–670), factor by factor.

**The star on η̃^*.** It is the complex conjugate of a scalar. That is the chapter's convention at 71:964, "a^* the
conjugate transpose (the conjugate for scalar a)".

**The rest of the proof.** At y = x, η̃^*(x, x) = ((ψη_0)(0))^* = 1. So the term of index 0 is still θ((χ_β g)^*)_α.
The derivative count (71:686–696) does not depend on whether the cut-off is conjugated, so it is unchanged.

### (e) The qualifier and its neighbours

- "One admissible choice" is now uniform across the paper:
  - 00:33, 01:154 and 03:354 say "of the weights, orders and inner products";
  - 71:20–21 and 90:70 say "of the weights and of the free orders and inner products".
- No sentence stating the upper bound names the weights alone any more. The lower bound sentences (01:153, 90:67,
  71:2468) rightly keep "every admissible choice of the weights": eq:uc-lower holds for every choice of the weights.

## Contract

- **Line length.** At most 121 characters (Python len) in both changed files: chapter 71 maximum 121, chapter 03
  maximum 120. The same holds after label resolution with assemble.py's own number() and resolve(), run on the
  snapshot (121 and 120). The changed lines are 109–121 (source) and 96–121 (resolved), except the paragraph tails
  "[[lem:fwd-orders]]; …" (63), "CA." (3) and "([[ch:explicit-constants]])." (30).
- **Line starts.** No wrapped line in any changed paragraph starts with "+ ", "- ", "* ", "> ", "#", "=" or "|", in
  source or after resolution. The only such starts near the hunks are headings (71:1, 71:509) and the list items 03:351
  and 03:358.
- **Backslashes.** None anywhere in chapters/*.md (0 hits), so the four \overline forms are gone.
- **Whitespace.** No tab, CR, trailing blank or double blank line in either file, and each ends in one newline.
- **Language.** The new words contain no file, program, code or AI language. The verb "reads" in N3 matches the
  paper's own usage (46:1264, 1538; 71:1702).
- **Tools.** Working tree and clean export of f8a5e9ff:
  - `python3 lint.py --chapters`, last line: `chapters: 62 file(s), 4570 label(s) defined, 0 hit(s)` (exit 0)
  - `python3 lint.py --selftest`, last line: `selftest: PASS` (exit 0)
  - `python3 assemble.py --check`, last line: `labels 4570, computations cited 0, problems 0` (exit 0)

## Observations outside the count

1. **The measure of L.** 71:577 calls L "its kernel on the Fourier side". That is exact with respect to
   (2π)^(−n)dη, the measure for which the Fourier transform is an isometry from L²(dx). With respect to dη, the kernel
   is (2π)^(−n)L.
   - Schur's test then differs by the constant (2π)^(−n), which C absorbs, so no bound moves.
   - The text predates the commit; the commit changed only the conjugate. I make no request.
2. **The name η̃^*.** Φ is symmetric, Φ(y, x) = Φ(x, y) (substitute t → 1 − t). So η̃^*(x, y) = η̃(y, x)^*. That is
   the kernel adjoint of η̃, not its pointwise conjugate.
   - This matches c^*, the amplitude for the adjoint, which is also a name rather than a conjugate of c.
   - The definition at 71:673 is explicit, so no reader is left to guess.
3. **The orphan "CA."** The rewrap leaves "CA." alone on 71:575, because 71:571–574 are at 121 characters. This is
   only a matter of where the source lines break.
4. **The barred roots.** 71:3559 and 71:3587–3588 write the conjugate of a root of a real polynomial as ι̅ (Unicode
   combining overline). That is plain Unicode, outside the edit's scope (TeX bars), and consistent: a bar on a complex
   number, a star on symbols and kernels.
5. **The working-tree change to chapter 90.** Its uncommitted change (seen at about 10:03 UTC) rewords 90:76 to "are
   used only in [[ch:explicit-constants]], whose opening states both", together with two rewrapped paragraphs. It is
   outside this reading and I did not review it.
