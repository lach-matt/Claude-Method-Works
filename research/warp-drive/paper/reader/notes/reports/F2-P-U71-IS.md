# F2-P-U71-IS: fix round on proofs/P-U71-IS.md (second reading R2-P-U71-IS)

**Starting point.** HEAD (659 lines) is not the reviewed text (87a7cc7, 643 lines). The earlier attempt reached the
commit: HEAD already carried every R2 text. I checked each one against the review and the cited lemmas (P-A-indicial
sextic-split, -large (b), -count, majorant; ch. 33 prop:np-10-54), then completed the strip proof. My diff against HEAD
is 17+/16− lines, all at l. 342–358. No number moves: l_* = 50, K_ι ≤ 52, 39 ≤ L ≤ 50, M ≤ 7 on Re ≤ 5, M = 1 on
[−101, 5].

## Findings (line numbers of the final file)

- **F1 (Major).** At l. 332–358, written with ξ_x, Δ and P_l − U. The two roots in |ι − ξ_x| < 0.45 are real and
  separated by ξ_x at l = 134, 135, and a non-real conjugate pair at l ≥ 136. I added: lem:s14-majorant cited for the
  closed disc; x = 0.018224, 0.018495; Δ(0.018768) = −0.023037762176; "as Δ(x)/8 < 0.0125". Also applied: statement
  l. 306–312, prop:is-logs (c) l. 274–276, intro l. 6–8, rem:is-summary l. 646–652.
- **F2 (minor).** At hκ > 70 such a root is non-real and simple by conjugation (2m ≤ 3), l. 350–354. Existence stays
  open (l. 309–310). No "at most 3" remains.
- **N1** l. 429–431, 495–497. **N2** l. 15. **N3** l. 314–318. **N4** l. 32, 322. **N5** k_R ×7 (l. 237–243), ν₀ ×5
  (l. 518–521); M* kept. N1 and N3 use the reviewer's texts.

**Departures (from HEAD; kept after checking).**
(i) The intro also states the bound 7, which (IS) needs on the half-plane.
(ii) N4 is defined at l. 32, as N(L̂_b(0), ·) is first used at l. 274, before prop:is-mult.
(iii) l. 275–276 writes out why the order is 1: 1 < Re w ≤ 3, so [[eq:is-l1]] gives ℓ̂ ≤ 1 + 1.
(iv) rem:is-summary also states M ≤ 7, 39 ≤ L ≤ 50 and max(L, M) = L ≤ 50, as R2's L/M section and P-U71-SP do.

## Private checks

Exact rationals (sympy); sanity numerics marked.

- **Identities.** det(hN_l) = det(M⁰ + hM¹) at l = 134, 135, 136, 150, 172. det M⁰ = U; Δ is disc 𝒬.
- **Window.** x(133) = 0.017955, x(134) = 0.018224, x(172) = 0.029928, x(173) = 0.030275. Δ(0.01866) > 0 > Δ(0.01867).
  Δ′ vanishes only at 107.1875.
- **Δ.** At l = 134, 135, 136, 172: 0.093562114176, 0.035476440025, −0.023037762176, −2.414919314816.
- **U at l = 134, 135.** U(ξ_x) = 0.0057943, 0.0021968. U(ξ_x − 0.45) = −0.017873, −0.018176. U(ξ_x + 0.45) =
  −0.37185, −0.37869.
- **Constants.** 1.97·0.035/32 = 0.0021547; 0.0425·0.39 = 0.016575; ξ_x + 0.45 ≤ 2.9725; −Δ(0.018768)/8 = 0.0028797;
  0.0425·0.0028 = 1.19·10⁻⁴.
- **Disc bound.** Rigorous majorant Σ|coeff|·0.45^k of P_l − U about ξ_x, for each l = 134…172: largest
  9.3353·10⁻⁵ < 9.4·10⁻⁵. This confirms the cited bound independently.
- **Signs.** P_l at ξ_x − 0.45, ξ_x, ξ_x + 0.45: −, +, − at l = 134 and 135. Sturm counts of real roots on the
  closed diameter: 2 at l = 134, 135; 0 at each l = 136…172.
- **Roots (sanity).** 2.43755, 2.58986 (l = 134); 2.46734, 2.56049 (135); 2.51412 ± 0.03858i (136); 2.52249 ± 0.38857i
  (172). Least separation 0.07715 (l = 136).
- **F2 (sanity only).** At l = 8366, 8367, 9000, 10⁴, 3·10⁴, 10⁵, the least real part of the three roots above 19/10
  is 55.00, 55.02, 63.26, 77.51, 481.0, 5017.0. None is ≤ 6.

## Contract

- **Lint.** 118 hits, all "reference to undefined label" (cross-chapter keys). All 211 references resolve in
  chapters/ or proofs/.
- **Labels and proofs.** 32 labels, lowercase. 16 proofs, 16 ∎.
- **Lines.** Max 121. No wrapped line starts with a listed prefix; one my rewrap had created ("|P_l") was removed.
- **Length.** 660 lines.
