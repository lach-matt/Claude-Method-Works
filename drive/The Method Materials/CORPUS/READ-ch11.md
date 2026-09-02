# READ-ch11 — Phase R2, main volume Chapter 11 "The single expression" (chat 71)

Member The_Method_1_6-2.md (BUILD90 main, md5 4aef772b…), L2075–L2303 (229 lines), read in full against (i) each cited section and Register entry, (ii) the rebuilt tower (tower-2.py, c0bce27a…), (iii) the chapter instrument r2-ch11.py (beside tower-2.py; general claims measured on all 976 cells / all 475,800 pairs / all 131,072 words) and r2-tools.py. Rulings applied as in READ-ch7. Census rows in range: 1050–1055 (all C9), closed in CENSUS-CLOSURES-ch11.tsv.

## A. Deviations (both texts)

**11-01 · L2187, L2271–2272, L2276 — "palindromic if and only if self-dual".** PRINTED L2276: `A rank polynomial is palindromic if and only if the poset is self-dual.` (L2187: `F is not palindromic ⟺ the poset is not self-dual`; L2271 the same.) MEASURED (r2-ch11.py): only *self-dual ⟹ palindromic* holds. Counterexample, exhaustively checked: the graded poset with 0̂, three atoms, three coatoms, 1̂ and covers 0̂ < a,b,c; a < A,B,C; b < A; c < B; A,B,C < 1̂ has rank sequence 1, 3, 3, 1 (palindromic) and admits no order-reversing bijection (all 8! tested). For Λ₈: not palindromic (5 against 4 at rank 4), hence not self-dual — the valid direction, and the only one the book uses. READING: an "iff" stated where one implication holds; the conclusion drawn from it is correct. Defect, subject-matter (same class as 8-02 and 9-01). For R3: "a self-dual graded poset has a palindromic rank polynomial, so an asymmetric one is not self-dual".

**11-02 · L2302 — "A self-dual graded poset gives F(−1) = 0".** MEASURED: the three-element chain is graded and self-dual with F(z) = 1 + z + z², F(−1) = 1. The statement holds when the top rank M is odd (σ then flips parity); L2285 itself says M = 20 is even and "σ preserves rank parity". READING: false as printed and in tension with the chapter's own parity argument two paragraphs above. Defect, subject-matter. For R3: "a self-dual graded poset of odd height gives F(−1) = 0", or delete the sentence.

**11-03 · L2260–2261 — a self-pointer.** PRINTED: `A sum bound breaks the first — §11.7 measures 89,864 join failures when one is tried.` SOURCE: the measurement is at §17.4, L4887: `89,864 join failures in 979,300 sampled pairs, meets unaffected.` §11.7 (L2251) is the section the sentence sits in and contains no such measurement. Defect, pointer. For R3: §17.4. (The 979,300-pair sample is Chapter 17's; record-carried there.)

**11-04 · L2086, L2090, L2162, L2212–2213 — the expression omits its domain.** PRINTED: `ℤ⁸ ∩ {x : Ax ≤ b}, A a 7 × 8 matrix`; `{x ∈ ℤ⁸ : χ(x) = 1}, χ a product of seven Heaviside steps`; F's nesting with Σₙ and Σₑ unbounded and only ℓ ≤ n−1, k ≤ 4ℓ+2, f ≤ e−1 as limits. MEASURED: the seven steps alone are unbounded on ℤ⁸ (n and e free); on the §7.4 caps with k ≥ 1 they select exactly 976 (= Λ₈, on the 6,912-point box); with k ≥ 0, 1,001; the printed nesting with n, e ≤ 3 but no caps on ℓ, k, f gives 16,054. READING: "All six agree exactly" at 976 only with the five caps of §7.4 and the eighth condition k ≥ 1 (§10.2) understood; neither is in the expression or on the page. Same family as 7-01. Defect, subject-matter (definition incomplete at its home), lower because §7.4 exists. For R3: one clause at §11.1 — "within the box of §7.4, k ≥ 1".

**11-05 · L2240–2241.** PRINTED: `a reader given only the cell list would deduce g ≤ 2(2f+1) without being told it.` MEASURED: on the cells max g = 2 at f = 0 and 3 at f = 1 (q ≤ k ≤ 3 binds before 2(2f+1) = 6 does). READING: the list yields g ≤ 2 at f = 0 and g ≤ 3 at f = 1, not the formula; the bound's form is not recoverable where it does not bind. INFERRED overclaim; lower. For R3: "would deduce g ≤ 2 at f = 0".

**11-06 · L2271 (Figure 11.2 caption) — "never rejoin".** MEASURED: forwards and backwards rank sequences differ at ranks 4–19 and coincide at the two end points (1 and 1). Wording; minor. Census row 1054 closed as a defect on this measurement.

**11-07 · layout.** Twenty-nine four-space lines render as code (L2084–2298, r2-tools.py layout), including aphorisms (L2092, L2264–2266) and the binary definition (L2099–2101); the combination table at L2178–2205 is a space-aligned dump broken by three column-dumps (L2184–2185, L2189–2191) that scatter "box − Λ" and "E_bits = log₂ C(X)" across lines, and its header row repeats at L2200. Production.

## B. Verified (all MEASURED unless marked)

- L2085–2090 six languages at 976: order (E(Λ₈) = 0, minmax.py), algebra/geometry/logic (χ on the box: 976, see 11-04), analysis F(1,…,1) = 976, information (E = 0 — INFERRED, the same fact).
- L2099–2101, Register 258 (R L1007): 17 join-irreducibles; cell ↦ 17-bit word is a bijection; join = OR and meet = AND on all 475,800 pairs, 0 failures.
- L2113–2115, L2149: 17 bits; log₂ 976 = 9.9307; surplus 7.07; 976/131,072 = 0.7446 %.
- L2122–2132, Register 331 (R L1227): J(Λ₈) has 20 covers; of the 131,072 words exactly 976 satisfy the 20 implications and they are the cells; "depth of five" = the longest chain in J(Λ₈), 5 elements (4 covers) — the record prints no definition of the depth; INFERRED reading.
- L2143–2147 §12.11.0 (L2535): "41,682 pairs, associative" — record-carried to Chapter 12 (4 other main sites). "taken for seniority" is not in Register 331 — incidental.
- L2154–2158 Appendix D's language list (L10345: order · combinatorics · analysis · complexity · physics · algebraic geometry): matches; Register 233 (R L923) says E = 0 is reachable by refinement — consistent.
- L2162, L2164: the seven steps = the seven rows of A; each row two non-zeros; the constraint graph is the path n–ℓ–k–q–g–f–e with 2S pendant at k (degrees k 3, ℓ q g f 2, n e 2S 1): true (L2222–2229, L2227).
- L2168–2170, L2182, L2278: F(z) = z³(z¹⁷ + 4z¹⁶ + 10z¹⁵ + 21z¹⁴ + 37z¹³ + 57z¹² + 79z¹¹ + 100z¹⁰ + 115z⁹ + 122z⁸ + 121z⁷ + 108z⁶ + 87z⁵ + 59z⁴ + 34z³ + 15z² + 5z + 1); F(1) = 976; F′(1)/F(1) = 11.0666; F(−1) = 2; 122 at rank 11 then 121 at rank 10; forwards 1, 5, 15, 34, 59, 87 and backwards 1, 4, 10, 21, 37, 57: all true.
- L2172, L2180: gcd = meet, lcm = join on all pairs (r2-ch9.py, 0 violations) — the chapter's "random pairs" now exhaustive.
- L2184–2185: 6,912 − 976 = 5,936 — arithmetic; note this "void" is the whole box's, not §10's per-pair void (incidental).
- L2235: without g ≤ 2(2f+1) the build has 1,000 cells; the 24 extra all have f = 0, g = 3: true.
- L2247–2249: 2S removed leaves 319 seven-coordinate cells; their join/meet closure adds 0 (E = 0); each carries k + 1 spin values and Σ(k+1) = 976: true.
- L2280, L2285: x ↦ max − x has rank(σx) = 20 − rank(x) on all cells, M = 20 even; 8 survivors (ranks 6, 8, 8, 10, 10, 12, 12, 14), all even, Σ(−1)^rank = +8; no fixed point: true. "They are the same statement" (8 survivors, asymmetric ranks): two consequences of non-self-duality, not one statement — INFERRED, incidental.
- L2287–2298: F_box(−1) = 0 — the ℓ and f factors (two values each) vanish, as do q, g, 2S (four values each); the residue 2 survives because ℓ and f are bounded by n and e: true (census 1055).
- Figure 11.1 placed at L2220, second site L10439 (App. C, consistent); Figure 11.2 at L2268; FIGURE_ASSETS L15–16.
- Pointers §17 (L4789), A.19 (L10091), §8.3 (L1847), Ch. 16 (L4332), §32.4.1 (L9085), §12.11 (L2524), App. D (L10320), §7.4 (L1789): all resolve.

## C. Incidental

- L2229 "the simplest tree that is not a path": the four-node star is simpler; loose.
- L2138 P20's "close always in one pass … never closes by Gödel" is quoted from Chapter 2 (census 1051–1052) — its home reading is READ-ch2.
- The MC's rank-polynomial and language entries are read in the MC segment; only Chapter 11's own figures were reproduced here.
