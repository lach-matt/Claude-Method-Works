# P-GRD13: writer's report (sec:tl5-hfe, the thirteenth sharpening)

**File:** research/warp-drive/paper/reader/proofs/P-GRD13.md, md5 f1467bc970c05eb14befdcd0cc378d75, 403 lines.
Not committed. Base: HEAD 16fb423f, chapter 87 md5 b8c2cff2 (7265 lines). Drafted under scratchpad/reader/pgrd13/
(src.md one-line source, chapter.md wrapped, rest.md, tools/ adapted from pgrd12, calc/counts.py). Nothing under
method/, drive/, extracted/ or recovered/ was read.

Layout: chapter text 1–237 (10 labels), Placement 239–260, Comparison 262–388, Crosswalk rows 390–403.
Assembled: Section 57.28; Lemma 57.235 (lem:tl5-hfe-face), Lemma 57.236 (lem:tl5-hfe-rho), Definition 57.237,
Theorem 57.238, Remark 57.239; displays (57.163)–(57.166).

## What is proved

**1. A weight in the transport along the curves (lem:tl5-hfe-face).** Every face inequality carries the leaf
integrals from the initial leaf along γ_ω using (d/dv)|B|₀² = 2⟨B, ℒ_(∂γ)B⟩₀ ≤ |B|₀² + |ℒ_(∂γ)B|₀². Replaced by
2xy ≤ 𝔲x² + 𝔲⁻¹y², with 𝔲 a positive continuous function on D̄:
- (a) eq:tl5-hf-cs-r (intrinsic, weighted, leaf constant C_(E,0)(𝔶)) holds with 𝔲 + 2r²𝔲⁻¹|D̂∂γ|² and 2𝔲⁻¹|∂γ|² in
  place of 1 + 2r²|D̂∂γ|² and 2|∂γ|² (display eq:tl5-hfe-face);
- (b) lem:tl5-hf-sobolev (C_S) holds with (𝔲 + 8𝔲⁻¹|D̂∂γ|²)/(2Ω̂²z̲) + 2𝔲⁻¹𝔨₁ in place of (1 + 8|D̂∂γ|²)/(2Ω̂²z̲) + 2𝔨₁;
- (c) the second inequality of eq:tl5-hfu-face holds with 𝔱_(r,0)(t; 𝔲), 𝔱_(r,1)(t; 𝔲).
For 𝔲 = 1 these are exactly the forms the constants with index d use. The proof is self-contained (leaf inequality on
the leaf of p, transport of each g_J, comparisons, as in lem:tl5-hft-face / lem:tl5-hf4-face).

Why it matters: in the first-order bracket the |ℒ^J A|² part carries X = (μ^½ + ϖ′^½)² (the weights 𝔶_(|J|)μ^(b+3) ≤
μ·μ^(|JB|) leave a factor μ), while the |D̂ℒ^J A|² part carries Y ≈ 2|∂γ|²𝔩′² with the recovery constant. The bracket
𝔲X + 𝔲⁻¹Y is least at 𝔲 = (Y/X)^½ with value 2(XY)^½, against X + Y: so C₁² gains a factor of order μ^½, C₁ of order
μ^¼. This is the 2xy ≤ x² + y² step the handoff named; it has no free parameter in the earlier forms.

**2. The parts with ϱ counted over the second derivatives (lem:tl5-hfe-rho).** Verified the handoff's lead, and more:
the ε-part with ϱ of the products comes only from monomials whose energy factor Φ₂ is a second derivative (its
recovery residual). In the second expansion the only monomials with a factor D̂²Ψ are those of H₁^(λσ)D̂²h and
H₂^(λσ)D̂²h that take the leading term D̂²Ψ_K of ℒ^K D̂²h (2𝔮̂, 2𝔮 − 2𝔮̂: first derivatives; 2𝔠(H)h: none; the other
terms of ℒ^K D̂²h: D̂Ψ or Ψ). Their count is

    𝔠^ϱ_n(ν′) = Σ⁴_n λ^♮_(k₁)(ν′)λ^♮_(k₃)(ν′) − 1 + 𝔰_♭(Σ⁶_n b^♮_g(k₁, ν′)λ^♮_(k₃)(ν′)λ^♮_(k₅)(ν′) − 𝔤₀),

proved 0 ≤ 𝔠^ϱ_n ≤ 𝔠^♮_n − 𝔠^D_n (so strictly better than the handoff's 𝔠^♮ − 𝔠^D), and the ϱ terms of
lem:tl5-hfs-products, lem:tl5-hft-products and lem:tl5-hfq-theta (hence 𝔡_n, 𝔡′ of eq:tl5-hfd-words) hold with
𝔠^ϱ at the same argument (1, μ, ν). At Λ = 0: 𝔠^ϱ_n + 1 = 2^n against 𝔠^♮_n + 1 = 81·2^n (up to 𝔰_♭ terms), i.e.
−1.91 decades on every term of 𝔤_ϱ; computed exactly in calc/counts.py (𝔠^♮₄ + 1 = 1304.14 at 𝔰_♭ = 10⁻⁴ reproduces
G0n's floor 1303).

## The new constants and the closing condition (def:tl5-hfe-constants, thm:tl5-hfe)

Weights 𝔲₀ (zeroth-order steps), 𝔲₁ (first-order steps), 𝔲_M (N = 4, the Y₁ step of the products with no factor at a
point), positive continuous on D̄.
- C_S^l² = C_(E,0)(𝔶)²𝔴₀(p)⁴ sup 𝔳₀⁴R⁻³((𝔲₀ + 8𝔲₀⁻¹|D̂∂γ|²)/(2Ω̂²z̲) + 2𝔲₀⁻¹𝔨₁);
- C₁^(U,l)(𝔚)², C₁^(D,l)(𝔚)², C₁^(J,l)(𝔚)²: C₁^U, C₁^D, C₁^J with (𝔲₁ + 18𝔲₁⁻¹|D̂∂γ|²) and 2𝔲₁⁻¹|∂γ|²;
  C₁^l(𝔚) = min(C₁^(U,l), C₁^(D,l) + C₁^(J,l)); C₁^l, C₁^(Γ,l) from it;
- C_(1,ϱ)^l: C_(1,ϱ)^p with 2𝔲₁⁻¹|∂γ|²;
- 𝔜^l_(1,t) = (μ𝔱_(3,0)(t; 𝔲_M) + 𝔱_(3,1)(t; 𝔲_M)[𝔩(𝔙₂)]_t²)^½, 𝔜′^l_(1,t) = 7(μ/ν)^(3/2)𝔱_(3,1)(t; 𝔲_M)^½ς_t;
- 𝔤^l_(ϱ,s), 𝔤^l_(ϱ,t), 𝔤^l_(ϱ,q): 𝔤_(ϱ,s), μ^(−½)𝔤_(𝒥,s), 𝔤_(ϱ,q) with 𝔠^ϱ_(j′) + 1 in place of 𝔠^♮_(j′) + 1;
  𝔤_ϱ^l as 𝔤_ϱ^v (option (a) / (b) / min at N = 4);
- ε^l = 𝒮[s_N[2R̂ic] + 𝔰₁^v(1 − 𝔵^z)⁻¹𝔤_ϱ^l k₂^z ϱ]; S_F^l, S_M^l, ε_M^l, 𝔯^l (and 𝔯_M^l) formed with these;
- η_l = 1 − max(ϑ₁, ϑ₂) − 𝔯^l, A_l = η_l^(−½)δ_w + η_l⁻¹(ε^l + ε_M^l), B_l = η_l⁻¹(S_F^l + S_M^l), 𝔰_*^l.

**Closing condition** (eq:tl5-hfe-closing): 4A_lB_l = 4η_l^(−3/2)(δ_w + η_l^(−½)(ε^l + ε_M^l))(S_F^l + S_M^l) < 1, with
η_l > 0, 𝔰_*^l < 𝔰₁^v, η₀ < 𝔰₁^v and the rates (1 − ϑ₁)a_o, (1 − ϑ₂)a_i admissible. Conclusions of thm:tl5-hf (N ≥ 6)
or thm:tl5-hf4 (N = 4) with A_l, 𝔰_*^l.

**Containment.** For 𝔲₀ = 𝔲₁ = 𝔲_M = 1 every constant with index l is the index-d one, ε^l ≤ ε^z, η_l = η_d,
A_l ≤ A_d, B_l = B_d, 𝔰_*^l ≤ 𝔰_*^d; so the hypotheses of thm:tl5-hfd imply those of thm:tl5-hfe. No earlier theorem
is edited. (No minimum is needed: the weights are free, and 1 recovers the old constants; one weight serves all parts
of its step, ℰ_g, ϱ and η₀, so per-constant minima over different weights would not be valid.)

## Deduced effect (in the Comparison; not evaluated)

Assumptions: G0o's optima; Y ≥ 13 at C₁'s supremum (from G0l's anatomy: k-part 93–95.5 %), X ≈ μ.
- **Level 4, 𝔲₁:** C₁ × at most (2(μ/13)^½)^½: −1.38 / −1.13 / −1.63 / −1.38 decades or more. C_P^v (led by 𝔨_rec^p)
  falls until 2C_S leads (margins 1.29 / 1.37 / 1.44 / 1.55): up to +1.29 / +1.13–1.37 / +1.44 / +1.38–1.55 at the 1:1
  rate. Without 𝔲_M, S_M would cap the D_A cases at about +1.09 and +0.94–1.03 (counting the closing's spare); 𝔲_M
  lowers S_M's 𝔠^Mq₁ term by the same mechanism (not priced, the S_M split is not reported).
- **𝔲₀ on C_S:** about −0.07 to −0.3 decades on plausible numbers; acts once 2C_S leads.
- **𝔠^ϱ:** ε's ϱ coefficient falls −1.06 to −1.9 at level 4 (priced × 0.1 at +0.08–0.23 by G0o); at level 6, where ϱ
  binds, −1.91 at the floor, priced × 0.1 at +0.85–1.0, so up to about +0.85 to +1.9 until f or the 𝔯 budget binds.
- At level 6 the two changes act on different factors and add while ϱ binds.

## Not done, and why

- **Target 3** (word sums for the other monomials): not attempted. Upper bound +0.21 / +0.34 in two cases, 0 in two,
  capped by 𝔰_*, before family costs that fall on 𝔨_A, 𝔨_B — the factors that remain in 𝔎 once C_P is lowered; it
  needs thm:tl5-hfe evaluated first.
- **Minkowski for |ℒ_(∂γ)B| ≤ |∂γ||D̂B| + r|D̂∂γ||B|** (in place of (x + y)² ≤ 2x² + 2y²): at the optimal 𝔲₁ worth at
  most 2^(−¼) on C₁ (−0.075), and nothing once 2C_S leads.
- **𝔨₂** (1/z̲ split): worthless at the supremum (G0m); not redone, as instructed.
- **𝔴₀, 𝔳₀:** the evaluation already searches α : β : ρ per face and per constant (G0f); no lever claimed. With the
  weights the face function g of each constant changes, so that search should use the new g.
- **√7 on 𝔞_𝔄(Γ):** ≤ 0.03; skipped.
- **𝔜_(2,t)** and leaf-only steps: no gain from the weight (both parts at the step's weight / no transport).
- k₁^D → √5K_rec: sharp in this argument.

## Checks (scratch tree from git archive HEAD 16fb423f, Placement applied by tools/merge.py)

- Item 2's two old lines found exactly once, at 87:7264–7265 (end of file); pointer line 117 characters; chapter grows
  to 7504 lines.
- `python3 lint.py --chapters`: 62 files, 5311 labels (5301 + 10), **0 hits**.
- `python3 assemble.py --check`: **0 problems** (plain assemble.py not run).
- In-memory assembled check: **`[] 0`**.
- Re-run on the repository copy proofs/P-GRD13.md: same three results.
- Numbering: none of the 5301 existing printed numbers changes; 10 added (Section 57.28 etc.).
- Crosswalk: 10 rows, each `@PENDING:<line>` holds its label (lines 1, 20, 29, 69, 75, 126, 142, 164, 169, 215);
  merged crosswalk 460 rows = 460 chapter labels, same order; rows ASCII.
- Chapter text: longest line 120; no wrapped line starts with a forbidden marker; labels lowercase; no file/program
  names, code or AI language. Notes lines ≤ 121.

## For the readers

- Pitfall checked: the summaries state the mechanism exactly as proved (one 𝔲 per step, shared by the ℰ_g, ϱ and η₀
  parts; 𝔠^ϱ bounds a superset of the monomials with a ϱ part).
- The weights are functions on D̄ fixed in advance (like 𝔶, θ, ϑ); continuity gives finite suprema.
- Index letter l (not e: |A|_e, A_e are the Euclidean components; not λ: λ₀ := 1, λ^♮_k, H^(λσ) are taken). Weights
  𝔲 (Fraktur u, unused in the chapter).
