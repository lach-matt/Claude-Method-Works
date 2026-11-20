# F-DB-b: R-DB-1 findings 1–9 and 11–15 applied to P-U71-cstar.md and P-U71-forward.md

Baseline d7580340 (later snapshot commits hold only my edits). No printed integer moves; C_* and thm:uc-integer's
integers are unchanged.

## Findings (line numbers in the new files)

- **1, Major (cstar l. 70–71, 85–91, 453–461).** I took the first fix. New def:cs-choices (f): an admissible
  α′ ∈ (2, 2 + ε_g − 2ε), with levels α_0 < α′. It is admissible:
  - thm:iii-i11-4-1 takes any admissible α′ ∈ (2, 3), and the admissible levels avoid only a finite set.
  - α′ − α_0 < 1 < a_K − 2.
  - Every result built on it uses α′ only through w_(α′) > 0.
  - At a rotating b, the base is prop:iii-i15-2-5 at α_1.

  The Step 4′ text cites (f): τ_0 > α′ − ε′, so item (6)'s argument applies and the base has no transition-face round.
  The alternative (+20,541,783,003) was not needed; it would also stay below C_*.
- **2, Major.** Below; cited in lem:cs-elem (e), l. 151–154.
- **3 (l. 28–50).** max(A_ℓ, A_M + 11), with the A_M + 11 case; the next paragraph says why A_ℓ ≤ A_M.
- **4 (l. 62, 82–84, 209–211, 225–228).** N := 21/4, with N ∉ ℕ stated. The charges stay 5, 5, 6, 20, 30.
- **5 (l. 146–149).** E^ν is charged 11 by its structure (reviewer's text).
- **6 (l. 73–74, 92–93, 170–175).** New (g): the decrease of γ plus δ′ is at most ¼. The count to 4 steps is written out.
- **7 (l. 473–476).** X_12 now follows from the largest-part rule: 4k̄_max + 9 < X_12.
- **8 (l. 11–12, 452–457, 519–521).** G̃_0 is written out and stated to be affine in W⃗′^rot. Wording changed to
  "whose bound counts three runs".
- **9 (l. 518–519).** The 1.74·10²⁸ now refers to the bound of eq:cs-cstar. Added: C_* − 6N_ι < 3.63·10³⁰.
- **10, cstar part (l. 10–11).** The intro now gives the bound in the form "C_lev = 2N_ι + N̄_Λ + 529".
- **11–15.** Applied (l. 286–289, 301, 103/129, 226, 342–343).
  - One departure, in nit 11: I also list the exponent α_0 + j. Step 1.1 of prop:iii-g4-4-4 gives both 2 and α_0.

## The extension (Major 2): new cor:fwd-near-b0, forward l. 798–859

**Statement.** Take the (B4) order to be that of lem:fwd-orders. Then thm:iii-h2-4-1, with margin 1, holds with
d = 20,175 on B̄_1. cor:iii-h2-5-1 holds with d = 20,180 on B̄_* ⊃ ℬ̄_*.

**Proof outline.** At b, the d is D_0 + D_1 + d′ + d″ + 1 for P_0 = 2L_b. P_0 enters the proof of thm:fwd-loss in
three places, and each is unchanged at b:

1. **The orders.** (B4) reuses the b₀ order, admissible for 2L_b with the same weights and margin. So d′ = 10,
   d″ = 11 and N′ = 13.
   - The radial sets over ∂K⁺ and ℐ⁺ are defined in coordinates, so they do not depend on b.
   - 𝗌 = 11 on {r ≤ r_Γ} ⊃ horizon ∪ Γ_b, so the constant orders (12, 8), (11, 8), (−10, −13) are unchanged.
2. **The cited results.** D_1 = 49, from closed forms free of P_0. D_0 ≤ 20,104:
   - the calculus involves no operator;
   - the sites of lem:fwd-box are the same, at the same parameters;
   - the increments are structural;
   - thm:iii-h2-3-1 and thm:iii-h2-2-1 use 2L_b only as a smooth operator, so they are not sites.
3. **The +1 and +5.** thm:iii-h2-2-1 gives margin 1. The +5 is the tame count, and its constant term
   O(|b − b₀| + |S|) (lem:iii-i-3-6) is absorbed as at b₀.

No pending marker was needed.

## Numbers (exact integers)

Rechecked, unchanged: k̄_max, N_ι, C_lev, the step sums (497, 529, 466, 469, 43, 1,914), I_lev, I_base, the seven-number
sum, and:
- The bound 643,676,388,469,322,172,480,826,383,357,103,759 < C_*, with margin 3.61·10³⁰.

New:
- C_* − 6N_ι = 3,628,919,841,642,544,595,212,800,000,024.
- Bound − 6N_ι = 17,389,163,815,025,421,596,157,103,783.
- 20,104 + 49 + 10 + 11 + 1 = 20,175, and + 5 = 20,180.

## Sentences for the coordinator (P-U71-assembly.md, current line numbers)

- **l. 138–139, thm:loss-d (i).** "which is at most 20,180 ([[thm:fwd-loss]]);" → "which is at most 20,180 at every
  base point ([[thm:fwd-loss]] at b₀, [[cor:fwd-near-b0]] at b ∈ ℬ̄_*);"
- **l. 168–169.** "The elementary losses do not depend on the base point ([[lem:iii-j2-2-1]]: only its constants do)." →
  append "; for the forward solution operators this is [[cor:fwd-near-b0]]".
- **l. 172–173.** "…[[lem:ec-round-loss]] and [[thm:fwd-loss]]." → "…, [[thm:fwd-loss]] and [[cor:fwd-near-b0]]."
- **l. 258–259 (split loss).** "d_F the loss d of [[thm:iii-i-5-3]] ([[eq:iii-i-5-2]]), at most 20,180
  ([[thm:fwd-loss]])" → "d_F the loss d of [[thm:iii-i-5-3]] and of [[cor:iii-h2-5-1]] ([[eq:iii-i-5-2]]), at most
  20,180 ([[thm:fwd-loss]], [[cor:fwd-near-b0]])".
- **l. 621 (rem:ec-upper-open).** "at most 20,180 ([[thm:fwd-loss]])" → add "[[cor:fwd-near-b0]]".

## Contract

- `lint.py` on the two files: 594 hits, all cross-file label references, all resolving in chapters/ and proofs/.
- Lines ≤ 121 characters, no forbidden wrapped-line starts, labels lowercase and unique.
- Diff: /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/f_db_b/f_db_b.diff
