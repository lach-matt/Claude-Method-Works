# R-CO: confirming reading of the coordinator's applied edits (nine commits)

Reader R-CO (independent; changed nothing in the repository). Input: scratch/r_co/coordinator-edits.diff, which holds
the hunks of d2a664e9, b2e9b0da, 8fb85522, 88dcbf3d, adf3d7a0, ca183990, 9790953e, 80d46901 and b1b87ba8. Read first:
READER-BRIEF.md, STYLE.md, and the reviews whose texts were applied (R-96, R5-82, R-DB-3, R-96b, R-I2, R2-DB-a).
Sources read: AN00 (Math. Z. 234 (2000), pp. 777–805; the author's copy, pp. 786–789) and arXiv:2408.06651v1 pp. 27–37
and 52 (alphaXiv full-page text). Private work in scratch/r_co/ (words.py: word-sequence diffs; the files before and
after each commit, taken with git show; a snapshot of the reader tree at b1b87ba8 for the tool runs).

## Method

- **Same words.** For every rewrapped paragraph I compared the whitespace-split word sequence before and after the
  commit, or against the reviewer's fenced text with the old text spliced around it. Where a reviewer gave the lines
  verbatim, I also compared lines byte for byte.
- **Contract.** I counted line lengths in code points and checked line starts on every added line of the diff, and again
  on the touched lines of the current files. Every touched file has maximum 121 outside table rows.
- **Current files.** The current files are the committed versions in every region read here. The later commits
  d1509feb and 04e80763 touched chapter 90 only at 53–73, so the sentence of 88dcbf3d now sits at 90:174–178.

## Per commit

**d2a664e9 — 35:1341.** The marker [[pending:literature-page-AN00]] is deleted and nothing else changes. The sentence
states AN00's Theorem 3.1 correctly. On p. 787 the source says: "In the following, Ω ⊂ C is open and X is a Banach
space. Theorem 3.1 Let f : Ω → X be a locally bounded function such that ϕ ◦ f is holomorphic for all ϕ ∈ W where
W ⊂ X′ is separating. Then f is holomorphic." Just before, "a subset W of X′ is called separating if for every
x ∈ X∖{0} there exists ϕ ∈ W such that ϕ(x) ≠ 0".
- The edition's version is the source's: a locally bounded map on an open subset of ℂ, and "a subspace of X* that
  separates the points of X", a special case of the source's separating subset. No connectedness is needed in either.
- The use is right. The functionals of the larger space, restricted to the ℓ_I-weighted space, are a separating
  subspace of its dual, because the inclusion is continuous and injective (cf. AN00, Corollary 3.4).
- 98:10 gives the paper's correct authors, title, journal, volume and pages.
- The page is now readable: see nit 1.

**b2e9b0da and 8fb85522 — 96:2053–2059 (opening of sec:cone-tables; 96:1106–1114 at 8fb85522).** Compared with the text before
b2e9b0da, the word sequence differs by exactly R-96 nit 1 ("belong to" → "carry the numbers used in") and R-96 nit 2
("Tables" → "The tables of"). The other 120 words are identical.
- b2e9b0da left one line of 146 characters, and 8fb85522 rewrapped it. The result has every line at most 121 (two at
  exactly 121) and no forbidden start; one line starts "1/2 and v(r) = 7/2", which is not a list marker.
- True in place: sec:cone-approximant (87:68), def:cone-approximant (87:205, whose S is Σ C_(ij) T_i T_j) and the
  tables sec:cone-table-c1/-c2 (96:2064, 96:2276) are what the sentence names.

**88dcbf3d and adf3d7a0 — 90:174–178.** Against the text before 88dcbf3d, the only change is that
"[[pending:scope-two-dust-radial]]." is replaced by "([[cor:vlasov-two-dust]], [[rem:vlasov-radial-scope]]).". That is
R5-82's proposal, verbatim, and adf3d7a0 put it on one line of 55 characters. The sentence says what the two results
state (82:2321–2330 and 82:2403–2411):
- the two radial dusts of thm:two-dusts are added to a field of amplitude εF, ε ≤ ε_* ("a small restricted field");
- the hypothesis {u1 ≤ ϕ_out ≤ u2} ∩ Ω₂ ∩ {R = a} = ∅ ("the outgoing packet does not reach the inner sphere");
- the solution exists on its adapted domain;
- it is a weak limit of class vacuum metrics on Ω₂′, a domain of the type [[eq:omega]] inside the adapted domain,
  narrower through a′ > a and V′ < V ("only on narrower domains of the type of Ω inside it");
- "the high-frequency step is not carried out there" (on the adapted domain);
- "No uniqueness of g_ε is stated".

The other hunks of 88dcbf3d are outside this reading; see the end of this section.

**ca183990 — P-U71-IS and P-U71-SP.** Diff 231–235 → 231–237 and 654–660 → 656–662 in IS, and the single line 285 in SP;
nothing else.
- IS 230–237 and 656–662 are R-DB-3's two fenced texts, byte for byte. The lines before them (229 and 655) are
  unchanged.
- I checked the new sentence of DB3-IS-2 mathematically, and it holds. At a step with m = 1, u₀ contributes only the
  exponent 1. The right side of u₁, after u₀ is subtracted, has exponents 2, 3, … of order 0. So [[lem:is-count]] (b)
  gives order ord(2) = 0 at the exponent 2 (offset 1), and 2 is not a root ([[lem:is-roots]] (a)).
- u₂ has exponents only at real part ≥ 2 + 𝔡₁, from 𝒢 ⊂ {Re ≥ 3} and R + ℕ₀. At 2 + 𝔡₀ and 2 + 𝔡₁ that is the root
  alone, so [[eq:is-l1]] gives ℓ̂ = 1 and k = 0.
- So the offsets 1, 1 + 𝔡₀ and 1 + 𝔡₁ have order 0, as stated. This is what "a chain of at most three later steps
  starting from order 0" needs, for (1) (later steps m = −2, −3, −4) and for the class 1 − l at l = 2 (K = 3).
- DB3-IS-1 keeps the content of the old sentence and fixes its count. 650 names a first undecided item (the
  multiplicities below −101), so "Two further things" is right.
- SP 285 reads "(δ̄k)_β = −Σ_j ∂_jk_(βj)". β occurs nowhere else in SP, and no other line writes the divergence with an
  index.

**9790953e — 96:1108–1116, 96:1515–1518, 83:2364–2365.** The word diffs are exactly R-96b's three insertions:
- "The notation is that of [[sec:bg-below]].";
- "The notation is that of [[sec:margins]].";
- "of [[sec:table-bump]]".

Everything else in the rewrapped lines is word-identical, with lines of at most 121 and no forbidden start. True in
place:
- sec:bg-below is at 83:1664 and sec:margins at 83:2176.
- sec:table-bump is at 96:1520; its table defines y_j, C̃_j and D̃_j, which 83:2364–2367 uses.

**80d46901 — chapters 30, 81, 95.**
- *R-I2 finding 1, 30:1289–1300.* The new paragraph equals the old one with R-I2's fenced text spliced in from "this is
  the usual Sobolev norm up to" to "for k ≥ 1.", word for word, rewrapped. I checked the derivation completely:
  - With all scalings 1, 𝒱 = 𝒲, and on a compact manifold with a finite b.g. structure that is all smooth vector fields:
    each point lies in some φ_β⁻¹([−1 + δ, 1 − δ]ⁿ) for a fixed δ > 0, and the transition functions are bounded in C^∞
    both ways.
  - By [[rem:std-sbg-sobolev]] (Remark 3.15, source p. 35), H^k_𝒱 with w = 1 is the usual uniform Sobolev space, and its
    norm squared is equivalent to Σ_α of the sums (3.15).
  - *Upper bound.* Each X_i ∈ 𝒱 maps H^s_𝒱 → H^(s−1)_𝒱 boundedly (p. 36, quoted in the remark). Iterating l ≤ k times,
    and using that the H^0_𝒱 norm is comparable to ∫|u|²μ (χ_α = 1 on the covering cubes, finitely many charts, μ
    smooth and positive), gives ‖u‖_(H^k) ≤ C‖u‖_(H^k_𝒱).
  - *Lower bound.* On U_α some n of the X_i form a frame, so ∂_(x^j) = Σ c^i_j X_i with c^i_j smooth on U_α and bounded
    with all derivatives on supp χ_α, which is compact in U_α. Leibniz and induction on |β| bound |∂^β(χ_α u)_α| by
    finitely many |X_(i₁)⋯X_(i_l)u|, l ≤ k. This bounds the chart sums by ‖u‖²_(H^k), the ℓ¹ and ℓ² sums over the
    finitely many terms being equivalent.
  - The identity ‖u‖_(H^k) = ‖u‖_(L²) + Σ_i ‖X_iu‖_(H^(k−1)) holds exactly: the terms with l ≥ 1 are the terms of the
    second sum.
  - The derivation is complete and true. There is one wording imprecision in it: nit 2.
- *Uses.* 30:1321–1323 and 30:1347–1349 cite the equivalence through [[rem:std-sbg-sobolev]]. That remark contains the
  p. 36 boundedness, and 1349 points to the derivation ("as on ∂M above"). Both are true as they stand; see nit 3 for
  an optional pointer. (EE) at 1354 now has both directions it needs, including the bound on ‖Pv‖.
- *R-I2 nit 4, 30:1321–1335.* A pure rewrap: 312 words, identical sequence.
- *R-I2 nit 5, 30:1486–1496.* The only word change is "ℋ)" → "ℋ), ℋ a Hilbert space,". The breaks fall inside
  formulas ("∫ / e^(ιs)", "(χ − / 1_[0,1])", "k(F, / ι)"), which render with the spaces the old text had; no line starts
  with a list marker.
- *R-I2 nit 2, 81:1018–1024.* R-I2's text verbatim ("here"; "[[ch:vlasov]] carries the solve out for its own data,
  with constants independent of λ, [[prop:vlasov-scaled-correction]]"), and nothing else changed. Both claims hold:
  - lem:vlasov-symmetrizer (82, "The symmetrizer on every slice") holds for every Riemannian γ and every α with
    1 + αγ^(rr) > 0;
  - prop:vlasov-scaled-correction solves 𝔉(U) = 0 for chapter 82's data, with η and C "not on λ".
- *R-I2 nit 3, 95:1065–1071.* The quotations match arXiv:2408.06651v1 p. 36 word for word:
  - "(up to equivalence of norms) when defined with respect to a b.g. structure compatible with ρB";
  - "correspondingly, these spaces are unchanged when defined with respect to a scaled b.g. structure compatible
    with B^×" (the edition starts the quotation at "these spaces");
  - the "Similarly, …" passage and "One can then easily show that every V ∈ V defines a bounded linear map
    V : wH^s_V(M) → wH^(s−1)_V(M)".

  The unquoted subject paraphrases the source's "H^s_V(M), and thus also wH^s_V(M), as a Hilbert space, is unchanged"
  correctly, and "((S13))" points to the definition of ρ𝓑. R-I2's optional extra (weights, w = 1) was not applied,
  and nothing needs it.

**b1b87ba8 — P-U71-close 350.** The only change is "α admissible" → "α ≥ 3 admissible" (R2-DB-a N1, verbatim), with
347–353 rewrapped and the word sequence otherwise identical. It agrees with the proof of lem:uc-admissible ("An
admissible α ≥ 3 is a number in (4 + ε_K − ε′_0, 4 + ε_K]") and with the spacings 0.999(α − 4) > 0.

**Outside this reading (checked for the contract only).** The coordinator listed only chapter 90 for 88dcbf3d and only
the opening of sec:cone-tables for b2e9b0da, so the hunks below were checked only for line length and line starts, and pass both:
- *88dcbf3d's hunks in 32, 36 and 43.* These are I-1's integration items: the (E3) clauses, ρ → ψ for the tower rows,
  ψ → ϖ, and "finitely many windows". R-I1b read them, its 36:1622 finding was fixed in 9cbb2b5c, and R-I2 confirmed
  the fix.
- *b2e9b0da's hunk at 96:1–16.* These are R-M33's nits n4 and n5, confirmed by R2-M33.
- *80d46901's changes to P-U71-cstar and P-U71-forward.* Not in the diff, and not read.

## Findings

**1. nit — 35:1341: the page of [AN00, Theorem 3.1] can now be given.**
- *Evidence.* The marker was removed because the page could not be read. In the author's copy of the paper, the
  running head "Vector-valued holomorphic functions 787" comes just before §3 and Theorem 3.1, and the head "788" comes
  after Corollary 3.4. So the theorem is on p. 787.
- The cut also left line 1341 at 81 characters inside a paragraph of 114–118. That breaks no rule.
- *Fix (optional).* "([AN00, Theorem 3.1, p. 787])", and rewrap 1341–1342.

**2. nit — 30:1292: "let 𝓑 be a finite atlas of ∂M with all scalings 1".**
- *Evidence.* 𝓑 is used in the sense of [[thm:std-sbg-calculus]] (S1) and [[rem:std-sbg-sobolev]]: charts onto
  (−2, 2)ⁿ whose inner cubes cover, with transition functions uniformly bounded in C^∞. An arbitrary finite atlas is
  not such a structure.
- For an arbitrary finite atlas, the parenthesis "(so that 𝒱 consists of all smooth vector fields)" can fail: the
  components of a smooth field in a chart that degenerates at the edge of its domain need not have bounded derivatives.
- Every compact manifold has a finite b.g. structure with arbitrarily small charts, for instance restrictions of
  charts defined near the closures. For such a 𝓑 every step holds, so the mathematics is unchanged.
- *Fix.* "let 𝓑 be a b.g. structure of ∂M with finitely many charts ((S1) of [[thm:std-sbg-calculus]]; for instance
  restrictions of charts defined near their closures), with all scalings 1 (so that …", rewrapped within 121.

**3. nit (optional) — 30:1323: the bracket names two of the three places the equivalence uses.**
- *Evidence.* The derivation above (1292–1297) uses Definition 3.14, Remark 3.15 and the boundedness of V on p. 36.
  1323 cites "[Hin26d, Definition 3.14 and Remark 3.15] ([[rem:std-sbg-sobolev]])".
- The remark it cites contains p. 36, so nothing is missing; and 1349 already adds "as on ∂M above".
- *Fix (optional).* At 1323: "[Hin26d, Definition 3.14, Remark 3.15 and p. 36] ([[rem:std-sbg-sobolev]]), as shown
  above".

There is no Major and no minor finding. Every applied text is the reviewer's, or differs from it only in wrapping. Each
is true in place. No rewrap changes another word. No touched line exceeds 121 characters, and none starts with "+ ",
"- ", "* ", "> ", "#", "=" or "|".

## Tools

- *At b1b87ba8, the ninth commit* (snapshot of the reader tree in scratch). `python3 lint.py --chapters`: 62 files, 4406
  labels, 1 hit, 90:66 [[pending:scope-d-…]], in no hunk of this reading; the scope-two-dust-radial marker is gone.
  `python3 assemble.py --check`: labels 4406, computations cited 0, problems 0.
- *On the live tree at my last run* (HEAD 04e80763, after the later commits d1509feb and 04e80763).
  - `lint.py --chapters`: 6 hits. `assemble.py --check`: problems 6.
  - Every hit is an undefined reference to thm:uc-integer, prop:fwd-calculus or cor:uc-two-offsets, at 01:153, 03:354,
    23:1072, 23:1470, 90:65 and 90:68.
  - These labels are defined in proofs/P-U71-close.md and proofs/P-U71-forward.md, which are not yet merged into the
    chapters. The references come from the later commits and from the concurrent work; none is in a hunk of this
    reading.
- Both tools were run with PYTHONDONTWRITEBYTECODE=1; git status of reader/ was unchanged by the runs.

## Verdict

**CONFIRMED** (0 Major, 0 minor, 3 nits).
