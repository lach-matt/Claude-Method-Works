# P-GRD15: not started; notes for a fresh writer

I wrote P-GRD13 (sec:tl5-hfe) and P-GRD14 (sec:tl5-hfc), and I scoped round 14. My context is full, so I am handing
P-GRD15 over without drafting any of it. Base: HEAD 89f4425b. sec:tl5-hfc is merged at 203efd5e as Section 57.29,
87:7507–7642.

## Placement

The new section goes after the last line of rem:tl5-hfc-what, with a pointer line appended. The old text, 87:7641–7642:

    rates are unchanged. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfc]] are established in
    this paper for no background at 10 l5.

## Tools

All are under scratchpad/reader/pgrd14/tools/. Copy them to pgrd15/tools/ and re-extract orig/ from 89f4425b.
- `build.py`: edit the `notes` dict (ASCII only) and replace P-GRD14 by P-GRD15.
- `merge.py`: edit OLD/NEW.
- `check.sh`: edit the path.
- `wrap.py`, `pad.py` and `numcheck.py`: edit numcheck's neighbour labels.

The workflow is: one-line source src.md, then wrap.py, then pad.py, then build.py with rest.md (Placement, Comparison,
`@ROWS@`), then check.sh.

## Conventions learned (from readers R-P-GRD12/13/14)

- **Index letters.**
  - Taken: g s t q v w x y z p u d l c.
  - Free and reasonably safe: f, k?, m?, n?.
  - Avoid:
    - e, because of A_e and |A|_e, the Euclidean components;
    - h, the solution;
    - a, b, o, i and r, all used as variables;
    - λ, because λ₀ := 1, λ^♮_k and H^(λσ) are taken.
  - Weights: 𝔲₀ (zeroth-order steps), 𝔲₁ (first-order steps) and 𝔲_M (S_M) are taken.
- **Summaries must state the mechanism exactly as proved** (R-P-GRD12 m1). The readers check the opening paragraph and
  the Remark word by word against the proof.
- **The Comparison needs an "every supremum at one point" assumption**, and its gains must be marked as upper figures
  (R-P-GRD13 n3).
- **Cite report figures exactly.** R-P-GRD14 n1 and n3 caught figures attributed to the wrong report or range.
- **Containment:** a new theorem must reduce to the previous one at the old choices; say exactly where.

## What binds (G0p §G0p.1, §G0p.3; on P-GRD13, before P-GRD14)

**C_P^v at level 4.**
- Seed 1: 2C_S leads at the supremum. 𝔨_rec^p sits 0.195 (D_A) and 0.108 (D*) below 2C_S.
- Seed 2: 𝔨_rec^p leads the supremum by 0.11 (D_A) and 0.22 (D*).
- C₁ leads nowhere, at 0.35–0.72 below 2C_S. It acts only through 𝔨_rec^p's term 𝔨_♯K_rec C₁^Γ, which G0p writes as
  √7C₁^(G).
- P-GRD14's lever 2 (2C_S → 𝔤₁C_S) is therefore capped at seed 1 by 𝔨_rec^p (≤ 0.195 / 0.108), and pays about nothing at
  seed 2. **So 𝔨_rec^p is the next constant everywhere at level 4,** and lever 3a alone will pay little after P-GRD14.
  Check this against G0q when it lands.

**Level 6.** ε's coefficient of ϱ × 0.1 is worth +0.90 / +0.61 / +0.81 / +0.40. 𝔰_* sets ε 3.7–6.1 decades below the
closing, and f and ϱ lie within 0.02–0.06 of each other.

## Lever 3a: C_S's zeroth order through the shorter words

**Sites.**
- The zeroth-order step: lem:tl5-hfp-abs (c), 87:6692–6694 and its proof 87:6713–6723.
- C_S^l with 𝔲₀: def:tl5-hfe-constants, 87:7393 onward.
- The face form with the weight: lem:tl5-hfe-face (b).

**Why 𝔲₀ does almost nothing.** The step's weights satisfy 𝔶_kμ^(b+2) = μ^(|JB|) exactly. So the |Ψ_(JB)|² part, X =
1/(2Ω̂²z̲), has no factor μ, and it is of one size with Y = 8|D̂∂γ|²X + 2𝔨₁.

**Mechanism.**
- For a word ZC ≠ ∅, (∗) of lem:tl5-hfg-products (87:5211–5212) gives |Ψ_(ZC)| ≤ 𝔷(|D̂Ψ_C|² + |Ψ_C|²)^½.
- The step's weight satisfies 𝔶_kμ^(b+2) ≤ μ·μ^(|C|). So the X part of every word except h gains a factor μ.
- The cost is 𝔷²𝔨₂ (through eq:tl5-hf-coercive) and a count of preimages: ≤ 6 rotations as first letter of J, or 1
  when J = ∅ and B = ZB′.
- The part 8|D̂∂γ|²|B|² of Y can take the same route.

**Bookkeeping.**
- The face bound becomes a supremum over the face of the maximum, over the words, of the total coefficient that hits
  each word's energy. The L part hits word JB through 𝔨₁(e_o + κ′e_i); the X parts hit the shorter words through 𝔨₂.
- Redo the family version (lem:tl5-hfp-abs (c) for n words of one length) and 𝔐_p^(m) at N ≥ 6.

**The word h (B = ∅, J = ∅) has no shorter word.** μ|H| ≤ 𝔤₁μ|h| makes it the entry 𝔤₁C_S. Two options:
- give the step for B = ∅ its own leaf weight 𝔶₀ ≤ μ⁻²; the leaf inequality allows any weights per application. The
  n = 0 mode then costs 1/(2π²𝔶₀), negligible down to 𝔶₀ ~ 𝔶₁, and the h-word's X coefficient scales with 𝔶₀μ²;
- or keep h's X part as it is, and take the gain only for |B| ≥ 1.

**Deduced (my plan, unverified).** C_S falls about 0.5–0.8 decades. The assumptions:
- μ = 10⁻⁵;
- 𝔷 = 10^0.6–0.75 (G0g);
- 𝔨₂ = 10^2.6;
- Y between 6 and X;
- C(𝔶)² about ×2 for the separate weight.

G0p prices C_S ÷ 2 at +0.19 / +0.01 / +0.27 / 0.00 (level 4) and +0.22 / +0.06 / +0.18 / +0.02 (level 6), before
P-GRD14.

## 𝔨_rec^p's C₁ term (the coordinator's item 2): scope first, and say honestly if nothing is available

**Where it is.** 𝔨_rec^p := 𝔨_♯K_rec(C₁^Γ + 𝔷₁′μ^½C₁^p + 𝔷₂′μC_S^p) + (1 − 𝔰₁^v)⁻¹μ𝔯_♯C_S^p, in
def:tl5-hfp-constants 87:6675. It is used in lem:tl5-hfp-rec (87:6811–6820) and through lem:tl5-hfv-rec. C₁^Γ = C₁(Γ)
is the first-order bound for the family of the seven fields, from lem:tl5-hfp-c1 with n = 7 and b = 1, formed with 𝔲₁.

**What is sharp and what is open.**
- 𝔨_♯ → √5 and K_rec are sharp for their steps. rem:tl5-hfp-what, 87:6879–6882, says K_rec is the operator norm of
  (v_Z) ↦ (|T|⁻¹v_T, (Σc^ab_j v_(K_ab))_j).
- That remark also says a smaller constant "would need bounds that separate the words beginning with T from those
  beginning with a rotation, which 𝒥_g and 𝒟_g do not give."
- **The honest candidate** is a weighted family version of lem:tl5-hfp-c1 for 𝔚 = Γ, with per-word weights (|T|⁻¹ on T,
  the c^ab structure on the rotations). Its output would be the weighted sum the recovery actually needs,
  (|T|⁻²|D̂Ψ_T|² + |Σc^ab D̂Ψ_(K_ab)|²)^½, instead of K_rec times the unweighted family norm.
  - Whether it gains depends on |T|⁻¹ against λ_M^(−½) at the supremum. Ask G0 for those two numbers before drafting.
- **Other routes,** each to check:
  - a per-family 𝔲 for Γ: G0p says scaling 𝔲₁ by 2 or ½ only costs, so probably nothing;
  - 𝔨_♯ for the h equation at p with 𝔥 = 𝔰₁^v: already used.

## Lever 4: the level-6 ϱ term into 𝔯

**Where.**
- The ϱ part of the products is 2k₂𝔰ϱ per monomial: the energy factor's recovery residual times the at-point factor Φ₁,
  bounded by 𝔰. lem:tl5-hfs-products' proof, 87:5607: "With |Φ₁| ≤ 𝔰 in the term with ϱ(p)".
- sec:tl5-hfw (87:6281–6289) uses 𝔰 ≤ 𝔰₁^v, which puts it into ε^w. sec:tl5-hfy and sec:tl5-hfz carry (1 − 𝔵)⁻¹ and k₂^z;
  the count 𝔠^ϱ comes from sec:tl5-hfe.

**Mechanism.**
- Bound Φ₁ by its bound at the point instead, |Φ₁| ≤ μ^(−ℓ_P/2)𝔰_P (or 𝔰_P⁰). Step 3 gives 𝔰_P ≤ C_Pe^(φ/2)Y_s +
  C_(P,ϱ)ϱ + C_(P,0)η₀.
- The Y_s part turns ϱ·(√e_o + √c√e_i) into a term ϱ·Y_s·(…). Through the forcing estimate (prop:tl5-hf-linear and
  𝒮 in eq:tl5-hf-source; check that 𝒮 takes the factor e^(φ/2)), that is a Y_s² term in 𝔯, roughly
  ϱ·𝒮[𝔤_ϱ k₂ C_P μ^(−3/2) e^(φ/2)].
- The ϱ and η₀ parts give ϱ² and ϱη₀ terms in ε.
- At N = 6 this carries μ^(−3/2), where the ε route carries μ^(−N/2) through 𝔰_*.

**Both routes are valid, but they put the term in different places** (ε against 𝔯). So the theorem needs an explicit
choice, an option, rather than a minimum of constants.

**Deduced.** ϱ stops binding at level 6 and f takes all of ε: up to about G0p's × 0.1 price (+0.40 to +0.90), capped
where f binds (f is within 0.02–0.06 of ϱ). Check the 𝔯 budget: η = 1 − max(ϑ) − 𝔯, and 𝔯 is 0.001 at the optima.

## Keep valid and enter both constraints

- Keep the present closing conditions valid: each choice must reduce to thm:tl5-hfc.
- G0q may change whether 𝔰_* or the closing binds at level 4. C_S and 𝔨_rec^p enter both, through C_P^v in 𝔰_* and
  through 𝔎 and 𝔎^D in S_F, so a lever on them acts on both.
