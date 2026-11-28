# P-GRD13: not started; notes for a fresh writer

I did not start round 13. My context already carries rounds 10, 11 and 12, so I am handing the round over, as the coordinator asked.

## Tools that can be reused

All under scratchpad/reader/pgrd12/tools/:
- `wrap.py` wraps one-line paragraphs at 120 columns. A `~` in the source is a non-breaking space.
- `pad.py` pads labelled display lines to 120 characters.
- `merge.py` applies the Placement to a scratch tree. Edit its OLD/NEW strings and the proof name.
- `check.sh` builds a fresh scratch tree from `orig/` and runs `merge.py`, lint, check and the in-memory `[] 0` test. Re-extract `orig/` from the new HEAD (cee5c801 or later) first.
- `numcheck.py` confirms that no existing label number changes.
- `build.py` assembles the proof file with the crosswalk rows `@PENDING:N`.

## Where the factors of C_P^v and 𝔨_rec^p come from

1. **C₁'s bracket** comes from lem:tl5-hfp-c1, which builds on lem:tl5-hfx-c1 and eq:tl5-hf-cs-r.
   - The factors 2|∂_γ|² and 1 + 2r²|D̂∂_γ|² come from |ℒ_∂γ A| ≤ |∂_γ||D̂A| + r|D̂∂_γ||A|, squared with (x + y)² ≤ 2x² + 2y².
   - The step (d/dv)|A|₀² ≤ |A|₀² + |ℒ_∂γ A|₀² uses 2xy ≤ x² + y² with no free parameter.
   - Both steps are candidates for a Minkowski or weighted split, as sec:tl5-hfz did for C₁ itself.
2. **𝔨₂** = (1/z̲ + max(1/c, 1/κ′))/(2Ω̂²), from eq:tl5-hf-coercive. G0m found the 𝒟_g split worth 0 at the supremum.
3. **𝔴₀ and 𝔳₀** compare the k-norm with h₀, and h₀ = α²du² + β²dv² + ρ²γ₀ is chosen per face (lem:tl5-hft-face). The best α, β, ρ for each face may already be optimised by G0's face4opt; check before claiming a lever.
4. **𝔨_rec^p** is defined in def:tl5-hfp-constants. Its couplings keep √7 through 𝔞_𝔄(Γ) ≤ (301/2)^½α_𝔄. A Schur bound per word, (Σ 𝔞_𝔄({Z})²)^½, is already allowed. G0n prices it at ≤ 0.03.

## Target 2: the ϱ coefficient

- It is 𝒮[𝔰₁^v(1 − 𝔵^z)⁻¹𝔤_ϱ^v k₂^z ϱ].
- 𝔤_(ϱ,s), and 𝔤_(ϱ,q) at level 4, carry 7^(j′/2)(𝔠^♮_(j′) + 1), the count of the ϱ parts of the products. No Sobolev constant enters them, so the leaf constant does not reach them.
- For the D̂Ψ·D̂Ψ monomials of lem:tl5-hfd-words the ϱ part is 0. So the count in 𝔤_ϱ could at least drop 𝔠^D, giving 𝔠^♮ − 𝔠^D in place of 𝔠^♮.
- At Λ = 0, 𝔠^♮₄ − 𝔠^D₄ is 15 against 1295. This looks cheap and possibly large, and it acts at level 6, where ϱ binds.
- Separately, k₂^z = q₁/(1 − 𝔰₁^v) is a per-word residual coupling, and it might take a family operator norm.

## Target 3

The other monomials are H₁D̂²h, the terms with R̂, the 2𝔮̂ terms that have a background letter inside β₁, and R₃. In these:
- When Φ₂ = D̂²Ψ, the family needs 𝔩(𝔙_k) ≤ 7^(k/2)𝔨_A.
- When Φ₂ = Ψ_C, the family needs (Σ_Z 𝔷_Z²)^½ ≤ √7𝔷.

My estimate in the P-GRD12 Comparison is that these costs eat part of the gain.
