# P-ADM: admissible points of the damping and gauge parameters

Deliverable: `research/warp-drive/paper/reader/proofs/P-ADM.md` (1,050 lines). I edited no chapter or crosswalk file
and made no commit. The working files are in
`/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/padm-work/`. The proof
file is generated from `texts.py` by `gen.py`. `run.sh` builds the merged scratch tree and runs the checks.

## 1. The lead: confirmed

Every use of simplicity of indicial roots of L̂_b(0) in the chapters concerns roots with real part in (−3, 0]. The same
holds for every use of z ∉ 𝖹_exc, of (C2), of (C3) and of row u5. I searched chapters 20–48 and 60–71, followed every
citation of prop:iii-f1-2-3 by part, and checked every citation of lem:iii-g4-1-1, lem:iii-g2-1-2, thm:iii-g2-3-1 and
sec:iii-g2-1. The uses are:

- **(c), root 0:** lem:iii-f1-2-5 and lem:iii-g1-1-3 (b).
- **Root −2 at s2, v2 and t2:** sec:iii-f4-5.
- **𝒲(ℓ_K) with ℓ_K < 3:** lem:iii-g2-1-2 and thm:iii-g2-3-1.
- **lem:iii-g4-1-1 (2):** stated at every root, but used only through lem:iii-g4-3-4, thm:iii-g4-3-1 and
  prop:iii-g4-5-1, all with weights w₀, w < 3.
- **lem:iii-i12-2-3:** exponents > −3.

Places that meet roots outside this window allow any finite multiplicity: ℰ_K, the count l_* of def:iii-i10-1-1, and
the lem:iii-a-1-4 expansions.

**Proof.** The proof is a new part (g) of prop:iii-f1-2-3, written in full. Every root with real part in [−101, 0] is
real and occurs once in its type's list, so it is a simple zero of det N_L. This holds for every z ∈ (0, ½], given
(C1). The argument uses:
- (d) together with lem:iii-f1-2-2, which puts −2 − 2γ_Cv_C = ι^C_(v1,≪) − 1 below −101;
- the bounds eq:iii-d-4-2. At s1, −5/4 < 2 − ι^Υ_(s1,3) < −1 < −¼ < 2 − ι^Υ_(s1,2) < 0. At sl, the chain
  −l − ¼ < … < 1 − l < 2 − l. At s0, 2 − ι^Υ_(s0,2) ∈ [−z/3, 0).

**Consequences:**
- u5, (C2), (C3) and global simplicity are dropped.
- The sites that used them now cite (g). These are 35:1422–1426, 35:1493, 35:1636, 36:1138, lem:iii-g4-1-1 (2) and
  its proof, 36:1360, 36:1423 and 41:1203–1206.
- (e) stays. It is true and no longer used.

## 2. What changed

### def:vi-c-admissible (ch. 46)

The definition is placed before row c1. A point is (h, γ_(Υ,H), e_Υ, γ_Υ) ∈ (0, ∞)⁴.

- **(P0)** h ≤ 10⁻⁶, e_Υ < 1, γ_Υ < ¼. From these, s_C > 100, (C5), (C1) (by lem:iv4-1-3 (a)), z ∈ (0, ¼) and
  γ_Υ < min(⅜, ½s_C) all follow.
- **(P1)** thm:iii-e-1-1 (1)–(2) for b near b₀.
- **(P2)** (C4′): every non-real root of □^C with |ι − 1| ≤ 50 has non-integer real part. This is a new clause in
  sec:iii-f1-1. It is implied by (C1) and (C4), and it is the hypothesis of (f) now.
- **(P3)** The conclusion of prop:iii-d1-4-1 on a neighbourhood ℬ(γ_(Υ,H)).
- **(P4)** P-T78's Λ_tf(γ_Υ, e_Υ) < 1, together with tf-admissibility of □^C_b at the weights in (1, 2). That second
  condition is part of thm:iii-e-1-1 (4), and Step 4 of prop:iii-f1-3-3 still needs it. Then prop:iii-f1-3-3 (P-T78's
  version) gives the tf-admissibility of L_b.

**Choice: h ≤ 10⁻⁶ instead of (C1) + s_C > 100.**
- thm:settling uses h ≤ 10⁻⁶ only through s_C > 100 and (C1).
- Using those two in place of the cap would enlarge the set only by points with h ∈ (10⁻⁶, 5·10⁻³). Nothing in the
  paper certifies such points.
- Keeping the cap makes the merged P-LB bound (thm:ec-lb-proved) hold at every admissible point. Without it, roughly ten
  confirmed P-LB sentences would need "with h ≤ 10⁻⁶".
- The definition says this openly.

### prop:vi-c-adm-exist: (i)

The points with h ∈ 𝖧, γ_(Υ,H) ≤ ϵ_0, e_Υ ≤ min(ϵ_1, ½) and γ_Υ < min(ϵ_1, ¼) are admissible. They exist with h, e_Υ
and γ_Υ arbitrarily small. They include the old choice: the rows as P-T78 leaves them, and with z ∉ Z_exc and the
threshold of lem:iii-d-7-1 (b).

### thm:vi-c-adm-holds: (ii)

The following hold at every admissible point, with their proofs:
- every result of ch:s13 from sec:iii-d2-1 on, and lem:iii-d1-5-1;
- ch:s14 from sec:iii-e-2 to sec:iii-e1-3;
- ch:s15–ch:s29.

The proof goes through each use, site by site, in groups:
- **Damping:** thm:iii-e-1-1 (1)–(2); (C1); (C4) through (f); (C2)–(C3) and Z_exc through (e) only, which is replaced
  by (g); thm:iii-e-1-1 (4) only in Step 4 of prop:iii-f1-3-3; s_C > 100; (C5); and 𝖧, h_0, h_tf and 𝖹.
- **Gauge:** mode stability (P3); tf-admissibility of L_b (prop:iii-f1-3-3 at the point); lem:iii-d-7-1 (b) only inside
  prop:iii-d1-4-1; and the explicit inequalities.
- **Continuity on compact sets.**
- **Everything else.** Every remaining smallness in ch. 37–48 concerns the data, b-neighbourhoods, Nash–Moser or
  gluing.

Then thm:vi-c-2-1, thm:iii-k-4-3, cor:s27-rate, thm:settling-precise and thm:settling hold.

### Replacements in ch. 46

- Rows c2–c4 and u2–u5 become the definition and row a1.
- The thresholds of rows b2, b3, w1, d1 and d2 are re-keyed.
- Steps (1)–(2) become (1) "an admissible point" and (2) "the numbers it fixes". The numbering is kept, because
  thm:settling and ch. 60 cite steps (3)–(6).
- The proof sentence of thm:vi-c-2-1 is updated.
- sec:iii-k-0 *Parameters* is rewritten.

### Other edits

- **ch. 34:** one sentence added to sec:iii-f-1.
- **ch. 35:** the (C5) sentence, which cited "γ_C > 10⁶".
- **ch. 41:124 and 42:559:** the side-finding repairs.
- **ch. 70:1695, ch. 71 (opening, rem:ec-point-outside, rem:ec-not-evaluated), abstract, ch. 1, ch. 3, ch. 90:**
  "outside the proved set" becomes "not shown to lie in". The definition no longer excludes the point.
- **ch. 71, P-LB's merged section:** six items re-key rows c1–c3 and u5, and restate thm:ec-lb-proved at an admissible
  point. No number changes.

### Totals

44 placement items, 3 new labels, crosswalk rows and notes.

## 3. The computational point (rem:ec-point-outside, combined text)

**Holds:**
- (P0);
- in (P1), (H1)–(H4) with ½ + ϑ_ℋ < −C_0 (lem:iv4-1-5 and lem:iv4-1-6);
- (P2), by prop:s14-damping-distance, and also by thm:t49-point;
- in (P4), Λ_tf < 1.0111·10⁻⁴ (P-T78).

**Open, stated precisely:**
1. thm:iii-e-1-1 (1) and the invertibility in (2) at γ_C = 10⁶. thm:iv5-7-3's h_0 is existential.
2. tf-admissibility of □^C_b at γ_C = 10⁶ for weights in (1, 2). thm:iv6-3-1's h_tf is existential. This is T3.
3. (P3): mode stability of □^Υ_b at (1/100, 1/100) for some γ_(Υ,H) on a neighbourhood of b₀. lem:iii-d-7-1 (a) now
   supplies (TF) there, so (P3) reduces to its case b = b₀, by Step 2 of the proof of prop:iii-d1-4-1.

Simplicity, 𝖹 and Z_exc are no longer conditions. P-T49 shows they hold at the point anyway, and this is cited.

## 4. Interactions

The interactions section of the file gives exact texts.

- **P-LB.** Merged at a722cb42. My old texts are copied from the merged chapters.
- **P-T78.** Its items 1, 2, 4 and 5 must merge before mine or with it, because I cite eq:tf-lambda,
  eq:tf-lambda-point, prop:tf-gauge-explicit, lem:tf-lin-reduction, lem:iii-d-7-1 (a)/(b) and the explicit
  prop:iii-f1-3-3. Its items 6–10 (rows u3/u4, step (2), rem:ec-point-outside, rem:ec-not-evaluated and
  sec:scope-constants) are replaced by my combined items 21, 27, 31, 32 and 44, which carry its content. R-P-T78 has just
  reviewed it (4 minor). If its texts change, the combined items should be re-checked.
- **P-T49.** Its item 7 is folded into my item 31, which cites thm:t49-point, so P-T49 item 1 must merge first or with
  mine. A fallback without P-T49 is given. Two of its chapter texts name rows I remove: rem:t49-sets (d) and
  rem:t49-scope. Replacements are given. Its results let me drop nothing further, since the definition already asks
  none of (C2), (C3), Z_exc and 𝖹.
- **P-K.** Unmerged and still changing. Four phrase substitutions change "lies outside" to "not shown to lie in". Its
  text 8 gets new old/new lines because of my item 43.
- **Other proof files.** No overlap.
- **Chapter 33.** Not edited. Three stale sentences get suggested texts: sec:iv4-0 "so do all later chapters", the
  opening of sec:s14-pa, and the first sentence of rem:s14-eps-ind-scope.

## 5. Side findings

**Verified:**
1. 41:124 and 42:559 credit "s_C large" to (C1). This is wrong. At v1, (C1) gives only γ_Cv_C > 49.5. The source is
   sec:iii-f-1. Repaired.
2. 𝖹₂ and 𝖹₃ are defined at z = 4·10⁻⁶ while h is chosen before the gauge. This is true; the excision was superfluous.
   P-T49 shows 𝖹₂ = ∅.
3. 46:92 omits lem:iii-d-7-1. True, and consistent.

**New, not repaired:**
- lem:iii-i11-2-1 (41:575–590) says "below real part 3 the only such root is 2". This ignores the □^C roots
  ι^C_(·,+) − 1 in (1, 3). Examples are ι₂(h) − 1 ∈ (1, 1 + 40h/13) (lem:ec-lb-ind), and at h = 10⁻⁶ the roots of C and
  P_l in (2, 3). Its E′ and its "Λ-valued" claim need checking. This does not concern simplicity.
- The setting of sec:iii-d2-1 tacitly needs ϵ_1 small for z ≤ ½. This is harmless under (P0).

## 6. Checks

The scratch tree was built in this order: the current chapters (P-LB merged), then P-T78 items 1, 2, 4 and 5, then
P-T49 items 1 and 2, then all 44 of my items. Every old text occurs exactly once.

- **`lint.py --chapters`:** 1 hit, the `[[pending:computational-1]]` in P-T49's rem:t49-count. It is not mine.
- **`assemble.py --check`:** 4647 labels, 0 problems.
- **Line lengths:** all new lines are ≤ 121 characters, also with every label resolved to a worst-case length.
- **Line starts:** no wrapped line starts with a forbidden prefix.
- **`lint.py proofs/P-ADM.md`:** only hits of the expected kinds in the merge notes:
  - cross-file labels;
  - labels defined in both Parts and Placement;
  - file names in the crosswalk rows and the notes.
