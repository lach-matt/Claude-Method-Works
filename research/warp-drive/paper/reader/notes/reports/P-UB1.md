# Report P-UB1: a proved admissible choice for the repaired Λ

Proof file: research/warp-drive/paper/reader/proofs/P-UB1.md. It has 2898 lines and md5 a4e10a41efcf0b396490ffad095af7dd.
- The old texts are copied from the chapter files at HEAD bce54b51. Chapter 71 has md5 427412e0…, the file P-UB2 read; chapter 96 has md5 f577ca62….
- Nothing else in the repository was edited, and nothing was committed.

## Step 4 finding: no better route that the paper can prove
- **Omitting 𝔡₀ is still undecided.** thm:is-d0 reduces it to whether c_b(Ȧ), the ρ^(2+𝔡₀) coefficient of ω̇_b(0, Ȧ), vanishes at rotating b.
  - No symmetry forces it to vanish. Equivariance allows X_A = φ₊A₊ + φ₋A₋. Parity does not separate the two, and time reversal is not a symmetry of the operator.
  - It is a global connection coefficient: it goes through the horizon modification, whose parameter γ_(Υ,H) the paper does not fix. Even its first order in A has no closed form in the paper.
  - I rewrote cor:is-flat as a proved conditional statement of what vanishing would give:
    - μ♭_Z lies in (3.548125563, 3.548125564)·10⁻¹⁰, which is above ε_Υ. So (G) would cost nothing beyond ε_K < ε_Υ.
    - N_Λ would be at most 3,683,190,611.
    - d_NM would be about 10³⁸, against about 10⁵⁶ now.
- **Another value of h (numerical observation, not proved).** At nine values of h in [5·10⁻⁷, 10⁻⁶], h = 10⁻⁶ is unlucky. Elsewhere the least excess is 9 to 87 times larger, and Σy² is at most 11% larger.
  - At h = 9.6·10⁻⁷, d would drop by about a factor of 84.
  - I did not change h. Chapters 33 (sec:s14-pa, sec:s14-exc-point), 70 (prop:rb-quasimode-point), 71 (def:ec-point, prop:is-iota, prop:is-mult, sec:sp-point) and 96 (sec:tab-a, sec:tab-t49) would all need new proofs. They are listed in §2.2 of the file.

## Final inputs (exact)
- **ε_K = 1.6747·10⁻¹⁷ = 16747/10²¹.**
- **ε_+ = 1.67478·10⁻¹⁷ = 167478/10²².** This is below 10⁻¹³, as P-UB2 needs.
- **ε_Υ = 1.4619·10⁻¹⁰**, unchanged. The 0.999 factors are kept:
  - Δβ_0 = 1.6713522747·10⁻¹⁷ exactly.
  - Δτ_0 = 1.4604381·10⁻¹⁰.
  - ε′_0 = 4·10⁻²².
- **N̄_Λ = 909,507,124,095,312**, so N_Λ ≤ N̄_Λ (prop:is-count (a)). Also N_Λ > 1.85753·10¹⁴.
- **Unchanged and confirmed:** k̄_0 = 3, J_* = 15,000,015, l_* = 50, J′ = 765,000,816, η_0 = 𝔡₁.
- **thm:is-gap (same label):**
  - (G) holds if and only if ε_K < μ_Z, and (G⁺) holds if and only if ε_+ < μ_Z.
  - 1.6747856·10⁻¹⁷ < μ_Z < 1.6747859·10⁻¹⁷ (eq:is-mu-z).
  - So every ε_K with which (G) holds is below 1.6747859·10⁻¹⁷.
  - μ_Z is attained at ι_* + 356327𝔡₀ + 1116082𝔡₁, with ι_* a root of P_390. The next smallest excess is at least 1.1076·10⁻¹⁵.
- **prop:is-lambda:** non-real elements of Λ below 3 + ε_+ have real part above 2.514, and elements of real part at most 2.514 are real.

## What is proved and how
- **lem:is-z3 (new):** Z has exactly 2629 elements of real part below 3 (1269 real, 1360 non-real). Every other element has real part above 3 + 4.99·10⁻⁶. The count uses only existing lemmas of chapter 33.
- **lem:is-disc (new):** a Rouché disc criterion, proved once.
- **Each root is enclosed to 10⁻²¹.**
  - Real roots: a sign change of the integer polynomial 𝒫_l at two printed rationals.
  - Non-real roots: the disc criterion with M = 7·10²¹, checked by Gaussian-integer arithmetic.
- **lem:is-gap-z (new):** encloses ι_* to 10⁻²⁴ and gives the least excess of every root, by lem:is-reduction applied to each row.
- **Rewritten:** prop:is-lambda, thm:is-gap, prop:is-count (a), cor:is-flat, rem:is-summary, the sec:is opening, the end of rem:gap-sums, def:uc-choice and lem:uc-admissible.
- **cor:is-lower (new, optional):** at every admissible choice, 3R > 1.2250·10²⁷ and N_NM > 2.5725·10²⁸.
- **The file has 14 texts (T1–T14) and crosswalk rows for 10 new labels.**
  - They do not overlap P-UB2's blocks. I dropped my text for thm:uc-reduction (iii) because P-UB2's M8 covers it.
  - V-I11 §5.1–5.4 must not be applied together with these texts.

## Checks
- All enclosures and lattice data were certified in exact arithmetic, then re-checked independently from the printed tables.
- A scratch merge passes lint --chapters, assemble and lint --paper with 0 hits.
- A joint merge with P-UB2's main set gives 0 problems except four lines of P-UB2's own texts (M6, M7, M13) that exceed 121 characters after resolution. They do so with or without my texts and need rewrapping.

## New table
sec:tab-is in chapter 96 has 1269 + 680 rows, about 2000 source lines. I estimate about 35 A4 pages.

## Not proved
- c_b at rotating b, so dropping 𝔡₀ stays conditional.
- Whether 𝔡₁ can be omitted.
- Anything at another h.
- A lower bound for N_Λ that also counts the real families. It is not needed for any bound.
