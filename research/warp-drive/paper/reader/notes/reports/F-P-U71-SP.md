# F-P-U71-SP: report

Base: the committed file (f38a4ee, 590 lines), which already held most of the lost attempt's work. Each finding was checked, re-verified and completed. Lines refer to the final file.

## Findings

- **F1 (Major), l. 385–401.** SP proves the distinctness itself:
  - l = 134, 135: signs −, +, − at a − 0.45, a, a + 0.45, so two real roots separated by a.
  - 136 ≤ l ≤ 172: 𝒬 > 2.87·10⁻³ on ℝ, so no real root; the two roots are a conjugate pair.
  - Text present; constants re-checked; P-U71-IS not used.
- **F3, l. 405–411.** Roots with hκ > 70, real part ≤ 5: non-real and simple, by conjugation with multiplicity. lem:sp-roots (b) (l. 413–419) derives multiplicity 1 for every polynomial involved.
- **F4.** cor:iii-g3-3-1 (1) is now also cited in statement (c), l. 543–546; the proof (l. 577–583) already used it.
- **F2, F6.**
  - (a), l. 527–534: M ≤ 7 and 39 ≤ L ≤ 50, so the least admissible l_* is L ∈ [39, 50]; we take l_* = 50. "The least ℰ^C_I" is now defined (lem:iii-c-3-2 (e), ℰ̃ = ∅).
  - (b), l. 536–541: K_ι ≤ 2 on Σ; the bounds 52 and 101 also hold.
  - Proof of (b), l. 562–575: from chapter 36 alone, the least ℰ^C_I has every logarithmic order 0 and contains (3, 0).
  - Proof of (a) adds prop:np-10-12 for (C1). Intro l. 16–20 rephrased ("multiplicities that the index sets carry" was wrong). Last sentence of rem:sp-scope clarified, l. 600–602.
- **F5, l. 548–551, 588–589.** 3 ∈ Λ as a generator; whether ι₁, a root of some P_l or such an ι + 1 lies in Λ is left undecided, and no bound uses it. *Departure:* the review's citation of prop:is-lambda is dropped, to stay within the allowed IS facts.
- **Nits, all present and correct:** N1 l. 176; N2 l. 197; N3 l. 132–140; N4 l. 489–491; N5 l. 548–549 (the "ι + 1 for Re ι ≤ 2 + ε_+" clause is kept, since roots with hκ > 70 are not located); N6 (tensor u, lem:sp-two-roots before l. 335, blocks D_0…D_q); N7 l. 184–187.

**IS citations** are now only prop:is-mult (M ≤ 7; simple on [−101, 5]) and prop:is-logs (L). Caveat: the lower bound 39 ≤ L, which you asked to be stated, also rests on prop:is-logs (b), which IS's fix round leaves untouched. prop:is-ci-pp and prop:is-lambda are gone.

## Renames (no clash in chapters 33–35, 71)

- N → 𝔫; 𝔪_k → 𝔮_k.
- λ → ϰ in cor:sp-lstar (λ_♯ kept).
- Finite-rank K_1 → 𝔉. Rejected: Φ (named operators in chapters 34 and 35); F_1 (F_j and F already taken).
- D_K → D_q.

## Private checks (exact rationals, sympy, mpmath)

- **Window constants:**
  - Δ_𝒬(0.01866) > 0 > Δ_𝒬(0.01867).
  - 𝒬 = 2(ι − a)² − Δ_𝒬/8 holds identically.
  - Δ_𝒬 = 0.093562114176 and 0.035476440025; U(a) = 0.0057943… and 0.0021967… = (2 − x)Δ_𝒬/32.
  - 𝒬(a ± 0.45) ≥ 0.3933; U(a − 0.45) ≤ −0.01787.
  - x/4 − 0.05 ≤ −0.042518; a + 0.45 ≤ 2.972446.
  - −Δ_𝒬(0.018768)/8 = 0.002879720272; 0.0425·0.00287 = 1.21975·10⁻⁴.
- **Sanity, from det(M⁰ + hM¹):**
  - l = 134: roots 2.437553, 2.589863. l = 135: 2.467337, 2.560486.
  - l = 136: 2.514116 ± 0.038575i.
  - Least separation over l = 130–174 is 0.0772; sampled |hW| on the discs ≤ 8.4·10⁻⁵.
- **Valuations:** c_1, c_2, c_3 and twelve c_0(q) exact; rows (−29, −26, −25, −18), (−44, −35, −28, −18), (−34, −29, −26, −18), (−30, −26, −22, −18); 3218988513000625 = 5⁴·17·23·13172331511.

## Contract

- `python3 lint.py`: 133 hits, all cross-chapter undefined labels; no other hit.
- Lines ≤ 121; no forbidden line starts; 26 lowercase labels; 11 proofs, 11 ∎.
- **Final length: 602 lines.** Only proofs/P-U71-SP.md was edited; nothing committed.
