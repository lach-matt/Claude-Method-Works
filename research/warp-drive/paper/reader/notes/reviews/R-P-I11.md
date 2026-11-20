# R-P-I11: adversarial reading of proofs/P-I11.md (Λ gains 1 + 𝒵; lem:s22-c-roots; 13 placement items)

Read: proofs/P-I11.md (md5 bf3b7c4c7414c32a51bcb4c98d94e246, 859 lines), notes/reports/P-I11.md, and in full
notes/reports/V-I11.md and notes/reviews/R-V-I11.md, against the chapters at HEAD c9b40e22 (chapters 33, 34, 40–44, 46,
62, 63, 65 and 71 are byte-identical to d6310fe2, the HEAD of the file, and 33, 34, 41–44 and 71 are unchanged at the
later HEAD 31936331). Read in the chapters: 41 (lines 1–1765, all of it), 42 (70–150, 205–260, 377–1048), 43 (36–50,
525–560, 760–920, 970–1010 and the Λ-sites listed below), 44 (50–420, 492–580, 680–705), 33 (91–320, 860–1030,
1120–1160, 4525–4540), 34 (263–560, 1184–1215, 1425–1500), 36 (1098–1130, 1250–1380, 1470–1530, 1607–1634), 30
(1124–1175, 1470–1560), 40 (1300–1372), 46 (1717–1725, 1782–1870, 1900–1915, 2150–2157), 62 (572–590), 63 (228–292),
65 (632–636), 60 (286–300), 71 (1600–1700) and 03 (274–290). Nothing under method/, drive/, extracted/ or recovered/
was read. No repository file was edited; nothing was committed. Scratch work:
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/rpi11calc/ (poly.py,
merge.py, P.pkl) and the merge directories
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/rpi11/ and
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/rpi11fix/.

## Verdict

**NOT CONFIRMED as it stands: 0 Major, 1 minor, 5 nits.** The repair itself is right. The generator 1 + 𝒵 is the right
one, lem:s22-c-roots is correct to the last inequality, the 13 items place cleanly and every result that R-V-I11 lists
holds after the repair with the proofs the file gives (§4.1) or the existing ones. The minor is a missing hypothesis in
the rewritten lem:iii-i11-2-1 (q′ − 2 must not be the real part of an indicial root). The enlarged 𝒵 makes it bite at
levels 0–1 of ch. 41 exactly as item 12 shows it bites in ch. 43. With the two-place text fix below (tested in scratch:
lint and assembly clean) I would confirm.

The claim "no statement outside chapter 71 is false after the repair" is refuted only in this narrow sense.
lem:iii-i11-2-1 as stated (old and new) is false for q′ = 4 and q′ = 5, where q′ − 2 is the root 2, resp. 3. Unless the
choice of ε says so, its uses at levels 0–1 are unproved for a root of 𝒵 with |μ| > 50 at real part 2 + ε_+ − ε or
1 + ε_+ − ε. No statement that uses Λ, Λ_*, ℰ_par, 𝒩, ℰ_♯, E′ or the Λ-valued claim is false. I found no further gap.

## Minor

**m1. lem:iii-i11-2-1 needs q′ − 2 off the real parts of the roots, and the levels 0–1 of ch. 41 must choose ε so.**

*Where.* proofs/P-I11.md:327–328 (item 7, new statement of lem:iii-i11-2-1). chapters/41-s22-kerr-face.md:522–523
(sec:iii-i11-1, *Constants*), which the file does not touch.

*Current text* (P-I11.md:327–328):

    **Lemma {#lem:iii-i11-2-1}** (Zero energy with expansions.) Let q ∈ (2, 3), q′ ∈ (q, 5], and let F ∈ H^(∞,(E,q′))_b(X̄)
    be partially polyhomogeneous at ∂X with an index set E, min Re E > q. Then (û, ḃ, S) := L̃_b(0)⁻¹(F, 0, 0)

*What is wrong.* The proof expands û by lem:iii-a-1-4 up to β = q′ − 2. That lemma (30:1499–1503) assumes "β ≠ Re ι for
all ι ∈ spec_b(A)", and it needs this: by def:s11-b-analysis (5) the expansion runs over Re z ≤ β with remainder in
H^(∞,β), and a root met at Re ι = β (log terms from a resonance with F included) is neither in E′, which takes the roots of
real part in the open interval (q − 2, q′ − 2), nor in H^(∞,β). The statement allows every q′ ∈ (q, 5]. At q′ = 4 the
s0 root 2 sits at β. For F with a ρ⁴-term of type s0 the resonance puts ρ² log ρ into û, and E′ does not contain it (the
root 2 is not among the roots of (q − 2, 2)), so the conclusion fails. q′ = 5 meets the roots 3 of s1 and v1. These two values are used nowhere.

The uses that matter are q′ − 2 = 2 + ε_+ − ε (Step 1 of prop:iii-i11-3-1) and q′ − 2 = 1 + ε_+ − ε (Step 2), the same
in prop:iii-i13-2-1 and through lem:iii-i11-2-2 ("q′ = κ") in everything after. Before the repair the lemma's sentence
"below the real part 3 the only such root is 2" made these look safe. After it they are not proved safe. eq:iii-f1-2-2
keeps the roots with |μ| ≤ 50 at distance ε_ind > ε_+ from ℤ, so away from these two numbers. It says nothing about the
others. (G) excludes Re μ ∈ (1, 1 + ε_K] ∪ (2, 2 + ε_K] only, and 2 + ε_+ − ε > 2 + ε_K. So a root of 𝒵 with |μ| > 50
at real part 2 + ε_+ − ε or 1 + ε_+ − ε is excluded by nothing written. The sentence "ε > 0 is taken small … and off a
finite set as well" (41:521–522) does not name these values.

This is the ch.-41 counterpart of what item 12 repairs in ch. 43: there ε = 0, and the file closes it with (Ex1). R-V-I11
saw only h = 10⁻⁶, where every □^C root of real part in (2, 3) has |ι| < 4.3, but the theorems hold for every h ∈ 𝖧. At smaller
h, R-V-I11 §2 itself finds numerically non-real □^C roots of imaginary part 21 and 210 with real part ≈ 2.725, so roots of 𝒵 with
|μ| > 50 occur.

*Replacement 1* (item 7, P-I11.md:327–328 become three lines). Item 7 then has 59 new lines, not 58. lem:s22-c-roots
moves to P-I11 line 356, or further if Replacement 2 is inserted before item 7. Update the item's "New, the 58 lines",
the crosswalk pin PENDING:355 (P-I11.md:827) and the line number in notes/reports/P-I11.md.

```new
**Lemma {#lem:iii-i11-2-1}** (Zero energy with expansions.) Let q ∈ (2, 3) and q′ ∈ (q, 5], with q′ − 2 not the real
part of an indicial root of L̂_b(0), and let F ∈ H^(∞,(E,q′))_b(X̄) be partially polyhomogeneous at ∂X with an index
set E, min Re E > q. Then (û, ḃ, S) := L̃_b(0)⁻¹(F, 0, 0)
```

*Replacement 2* (a new placement item, before item 7 or numbered 6a: [[ch:s22]], sec:iii-i11-1, *Constants*,
chapters/41-s22-kerr-face.md:522–523). The old text occurs once, as whole lines, and overlaps no other item.

```old
taken small, with 2ε < ε_+ − η_2, and off a finite set as well. The orders q_j ∈ (2, 3) of the zero energy solves are
chosen off the real parts of the exponents at hand.
```

```new
taken small, with 2ε < ε_+ − η_2, and off a finite set as well; that set contains the ε for which 2 + ε_+ − ε or
1 + ε_+ − ε is the real part of an indicial root of L̂_b(0), finitely many by [[lem:iii-f1-2-4]], as [[lem:iii-i11-2-1]]
asks at the levels 0 and 1 below (at the levels 2 and 3, q′ − 2 lies in (0, 1), where there is no root). The orders
q_j ∈ (2, 3) of the zero energy solves are chosen off the real parts of the exponents at hand.
```

(Widths 112, 120, 115 and 94 characters; no wrapped line starts with a forbidden marker.) prop:iii-i13-2-1 takes ε
"off a finite set as there" (def:iii-i13-1-1 (c)), so it inherits the exclusion. Item 12 already verifies the hypothesis
at ε = 0 in ch. 43, and lem:iii-j1-1-1 (level 2, q′ − 2 = ε_+ − ε ∈ (0, 1)) needs nothing. Optionally, F1 of §4 can say
the same in one clause. Tested: both replacements applied to the scratch merge, then lint.py --chapters (0 hits, 4752
labels), assemble.py --check (0 problems), assemble.py and lint.py --paper (0 hits).

## Nits

**n1. A wrap splits {Re < 2} twice, and a wrapped line starts with "<"** (P-I11.md:240–242, item 4). It is not a
forbidden marker, but it breaks the set notation across lines. Same line count:

```old
into ℰ^♯_+ and ℰ_++ ⊃ ℰ^♯_+ ∩ {Re < 2} by (H1); 𝒢, 3, 2 + π_1ℰ_col and 1 + 𝒵 have real part at least 2. And π_1ℰ_++ ∩ {Re
< 2} is closed under the increments below 2 ([[eq:iii-i8-1-1]]; adding 1 leaves {Re < 2}, as λ_♯ + 1 > 2). So Λ ∩ {Re <
2} = π_1ℳ.
```

```new
into ℰ^♯_+ and ℰ_++ ⊃ ℰ^♯_+ ∩ {Re < 2} by (H1); 𝒢, 3, 2 + π_1ℰ_col and 1 + 𝒵 have real part at least 2. And
π_1ℰ_++ ∩ {Re < 2} is closed under the increments below 2 ([[eq:iii-i8-1-1]]; adding 1 leaves {Re < 2}, as
λ_♯ + 1 > 2). So Λ ∩ {Re < 2} = π_1ℳ.
```

**n2. "the order there being then the multiplicity of the root less 1"** (P-I11.md:297, item 6). The logarithmic order
of a lone root term is the pole order of N(A, ·)⁻¹ less 1 (Spec_b(A), 30:1481). That is at most the multiplicity
and can be smaller. Replace the line

    being then the multiplicity of the root less 1, below l_* ([[def:iii-i10-1-1]]). As n(λ) ≥ n(λ′) + 1,

by

    being then at most the multiplicity of the root less 1, so below l_* ([[def:iii-i10-1-1]]). As n(λ) ≥ n(λ′) + 1,

(112 characters). The same words in §1 item 1 (P-I11.md:33) can follow.

**n3. "Re μ ∈ [2, …) gives a tower of rate above α − 2" is wrong at μ = 2** (P-I11.md:50, and notes/reports/P-I11.md:46,
"the roots with Re μ ≥ 2"). The root 2 gives the boost row (s1, 3, ·), of rate 2 < α − 2. Item 9 itself has it right
("below α − 2 exactly when Re μ ≤ 2"). Notes only. For P-I11.md:50–51:

    a root with Re μ ∈ (2, 2 + ε_+ − ε) gives a tower of rate above α − 2, the root 2 giving the boost row (s1, 3, ·).
    Item 9 covers both. The sentence is needed, not optional: it is the point where Step 6 met the false claim.

and in the report: "level 1, and the roots with Re μ > 2, whose towers have rate above α − 2 (the root 2 gives the
boost row)."

**n4. The site table misses one Λ-site** (§4.2, P-I11.md:655–738, and the report's table). Missing:
chapters/60-settling-proof.md:290–295, the proof of thm:settling, *The parameters*. It states (G⁺) and (G) and asks
(Ex1)–(Ex2) of row w1, which are conditions over Λ. Status H: the conditions are smallness conditions over a set that is
fixed before the constants (§2 (iii), (v), (viii)). Add the row after the row 46:2150–2156:

    | 60:290–295 | proof of thm:settling, *The parameters* | (G⁺), (G), (Ex1)–(Ex2) of row w1 | H (§2 (iii), (v), (viii)) |

The count is then 83. I found no other missing site. I searched every chapter for def:iii-i10-1-1, lem:iii-i10-1-2,
ℰ_par, ℰ_♯, Λ_*, lem:iii-i11-2-1, def:iii-i10-1-3, (G), (G⁺) and (Ex1), and for "∈ Λ", "⊂ Λ", "set Λ", "Λ ∩", "Λ +" and
"Λ-valued".

**n5. The new crosswalk row is printed with a four-space indent** (P-I11.md:827). It is a display there, but the other
proof files print their rows unindented (e.g. proofs/P-CIVP3.md:1072). The merge must drop the indent. The writer's
scratch merge did.

## Observations outside the file (no action asked of P-I11)

- o1. lem:iii-a-1-4 (30:1501–1503) states E_(k+1) := E(α) ∪̄ (F ∪̄ (E_k + 1)). Its proof sums two expansions
  (f′ ∈ H^(∞,(F∪̄(E_0+1),β)), 30:1542). That gives F ∪ (E_k + 1): at a common exponent the order is the maximum, not the
  sum plus 1. The stated set over-counts. The count of lem:iii-i10-1-2 (c) matches the proof's sharper set and the true
  expansion (below). This predates the repair, and the writer flags it too.
- o2. The list in lem:iii-i10-1-2 (c) of the raises at a treated exponent names "by 1 (prop:iii-g4-4-4 at α_0 = 2,
  rem:iii-g4-4-5)". It omits the other critical cases of lem:iii-i11-2-3, β_μ(α_0) = 0: c0 and c1 at α_0 = 2 + μ_c, and
  the class rows at 3 + μ and 4 + μ, which put log|σ| on the tower coefficient. Each is a raise by 1 within one Taylor
  level, so the J_* count holds. The enumeration is incomplete, and this predates the repair. A root μ ∈ 𝒵 treated at
  level 2 with μ = 2 + μ_c is one more instance of the same kind.
- o3. Coordination. After items 1–13 are merged, the upper bounds that 00-front.md:36–37, 01-introduction.md:156–157,
  03-theorems.md:316–319 and 363–364 and 90-scope.md:76–79 quote from thm:uc-integer rest on def:uc-choice. For the
  enlarged Λ that choice is not admissible (lem:is-gap-z of V-I11 §5.4, exact). P-I11 §6 says so and leaves these sites
  to P-UB2. So P-I11 should not reach the published edition before P-UB2 or the interim texts of V-I11 §5.5. The
  edition would otherwise state an upper bound with no proof.

## What I checked and found correct

**lem:s22-c-roots, by exact arithmetic** (sympy, poly.py). I multiplied out det(hN_l(ι)) of eq:s14-nl symbolically. The
following hold exactly:

- P_0 = −(ι − 2)C, with C as in eq:s14-c0.
- At v = 1/2: C(2) = 3(h + 2h² + 5e + 2eh) and C(3) = −2 + 20e − 6h + 12eh.
- eq:s14-f-two is identical to P_l(2 + w).
- At κ = 3: P_1(2) = 0, ∂_ιP_1(2) = f₁ = −24e − 6h − 54eh − 36h² − 12eh² − 48h³, P_1(3) = −9e + (4 − 10e)h + 15h², and
  P_1(5/2) is the printed cubic in h. All are identities in (e, h).

The inequalities hold on all of (0, 10⁻⁶] at e = 1/102400:

- 9e = 8.789·10⁻⁵ > 8.7·10⁻⁵ > 4h + 15h², and the −10eh term only helps.
- 1/4 − 71e/8 = 0.24991, 21/16 − 83e/4 > 0, and (55/16 + 189e/32)h² + 945h³/64 ≤ 3.44·10⁻¹² < 10⁻¹¹.
- 20e + 12eh < 2·10⁻⁴.
- P̃_1(3) = P_1(3) and P̃_1(5/2) = 2P_1(5/2).

The identifications are right:

- C has exactly one root of real part above 2: the proof of prop:np-10-54, the other two lying below −100.
- P_1 has exactly three roots of real part at least 2, the simple root 2 among them (prop:s14-scalar-every-h). So the two
  real roots of P̃_1 found are its two roots of real part above 2.
- (C1) with C_0 = 100 is lem:iv4-1-3 (a), for h ∈ (0, 10⁻⁶] and b near b₀. Its counts are (C1)'s.
- The roots of □^C at scalar type l are those of P_l (proof of lem:iv4-1-3).
- prop:iii-f1-2-3 (z ∈ (0, ½], (C1)) lists the ι^C_(·,+) − 1 at s0, s1 and s2. D removes only 1 at s0 and s1 and 2 at v1.

Numerically at h = 10⁻⁶ the roots are 2.0000747 (s0), 2.0001202 ∈ (2, 5/2) and 2.9999580 ∈ (5/2, 3) (s1), and
2.00000293 ∈ (2 + 2.923·10⁻⁶, 2 + 3.077·10⁻⁶) (s2, ι₂ of lem:ec-lb-ind).

The type-s3 root used in §4.1 lies in (2, 2 + 10h) for every h ≤ 10⁻⁶: P_3(2) = 9h(1638400h² − 102399h + 3)/5120 > 0,
and P_3(2 + 10h)/h has constant term −3/5120, with the rest below 1.6·10⁻⁴.

**What 𝒵 is.** Below the real part 3 the list after the semicolons of prop:iii-f1-2-3 gives the root 2 of s0 and the
ι^C_(·,+) − 1, and nothing else. With the bounds of its proof the other entries are 1 + ι^Υ_(s0,2) ∈ (3, 3 + z/3], 4; 3,
5, (3, 13/4), (4, 17/4); 3, 4 at v1; and l + 2, l + 3, l + 4 and (l + j + 1, l + j + 5/4) at l ≥ 2. The vector roots
ι^C_(vl,+) − 1 lie in (2, 3) exactly when l(l + 2) < 8 + γ_C (p_(v)(3) = h(κ − 3), p_(v)(4) = h(κ − 8) − 1). So item 7's
proof list is complete and exact. The four roots of the lemma are claimed as "at least four", never as all.

**Circularity.** The root part of lem:ec-lb-ind uses only eq:s14-f-two and prop:np-10-12 (ch. 33). Its "consequences"
paragraph uses prop:np-10-52, sec:s14-simple, lem:iv4-1-3, prop:iii-f1-2-3 and eq:iii-f1-2-2 (ch. 33–34). lem:s22-c-roots
uses only the root part. Chapters 33 and 34 cite no label of ch. 41–44. Their one citation of ch. 71 (33:4537) is a
remark, used by no step. The ch:s24 citation in ch. 32 (32:2187) is a remark too. So there is no cycle.

**lem:iii-i11-2-1 and the dictionary (F2).** At the Taylor level j, the exponent ζ − 2 of û, ζ ∈ E, is the u-exponent
ζ + j − 1 of the forcing; 1 + c is 2 + c + j; a root μ is μ + j + 1. Their ℕ₀-shifts stay in Λ, as Λ + 1 ⊂ Λ. The last
sentence keeps the Λ-valuedness that lem:iii-j1-1-1 cites.

**The windows (F1).** Level 0 is (1 − ε, 2 + ε_+ − ε). Level 1 is (η_1, 1 + ε_+ − ε), which meets only roots with
|μ| > 50, by eq:iii-f1-2-2 and ε_+ < ε_ind. Levels 2 and 3 lie in (0, 1) and meet none.

**The logarithmic count against the true expansion.** In the contour shift of lem:iii-a-1-4 the residue at a root μ has
pole order at most ord(N(A, ·)⁻¹, μ) + (log order of the forcing at μ) + 1. So a root met raises the order at its
exponent by the pole order, at most l_*, once per Taylor level. Distinct types at one value give a block-diagonal N, so
the order is the maximum, not the sum. The ℕ₀-shifts carry orders unchanged to the next exponent. Within one level at
one u-exponent there is at most one raise: at level 0 only roots; at level 1, α_0 = 2 (u-exponent 2) and roots
(u-exponent > 3); at level 2, α_0 = 2 (u-exponent 3) and no roots. So "a root met counts as one raise", the J_* bound and
k̄_0 + J_*(l_* + 1) ≤ k̄(λ) are right. A lone root gives order at most l_* − 1 (n2).

**Step 6 and thm:iii-i11-4-1 (item 9, F3, §4.1).** A root μ met at level 0 gives g_1 the tf-exponent μ + 1. There are
three cases:

- Re μ < 1 + η_1, possible only for |μ| > 50 and, by (G), Re μ > 1 + ε_K. Level 1 treats it at α_0 = μ + 1. The s1 tower
  has the rate μ and the u-exponent 1 + μ. The s0 and s2 towers have the rate μ + 1 > 2 + ε_K by (G), the c0 and c1
  towers μ + 1 + d_c > 2 + ε_K, and the v1 tower μ + 1.
- Re μ ∈ [1 + η_1, 2 + η_2). The level-1 solve gives û_1 the exponent μ − 1, so g_2 gets μ from E − 1 and from E′ + 1.
  Level 2 treats it at α_0 = μ. The s1 tower has the rate μ and the u-exponent 1 + μ. The other towers have rate at least
  μ + 1.
- Re μ ∈ [2 + η_2, 2 + ε_+ − ε). It is not treated, and the level-2 solve absorbs it. Re μ = 1 + η_1 and
  Re μ = 2 + η_2 are impossible, as 1 + μ ∈ Λ and no element of Λ has real part 2 + η_1 or 3 + η_2.

The rate Re μ is below α − 2 exactly when Re μ ≤ 2, by (G), and Re μ = 2 forces μ = 2 by (C4). Then (1 + μ, k) ∈ ℰ_par
with k ≤ k̄(1 + μ), and ν = (s1, 1 + μ, k) ∈ 𝒩_σ. The towers of the remainders α_0 + ℰ_ind and the roots met at level 1
(u-exponent μ + 2) are covered by the existing sentence "only the s1 tower can have a rate α_0 < 2 + ε_K, and by (G) then
Re(α_0 + 1) ≤ 3". That sentence now holds because α_0 + 1 ∈ Λ.

In thm:iii-i11-4-1 the new rows have rate above 1 > α′ − 2 (*The map*, *At (0, 0)*). The identification with m_ν is by
lem:iii-i10-2-1 (c), λ_0 ≠ 0, 1. cor:iii-i10-2-3 allows complex exponents. Only s1 rows are new: s0, s2, v1, c0 and c1
rows at the new λ have rate above 2.

**prop:iii-g4-4-4 at the new α_0** (§2 (vi)). eq:iii-g4-4-2 asks Re α_0 ∈ (1, 2 + ε_ind) and three conditions on ℓ_zf,
which I re-derived at both levels. Its root condition concerns real roots in (−3, 0), finitely many. lem:iii-g4-3-4 uses
ε_ind only for the roots in (−3, 0]. So no condition on d(Re α_0, ℤ) enters, as the file says. R-V-I11's mention of
d(Re μ, ℤ) ≥ ε_ind there is not needed.

**The counterexample of R-V-I11 §2, re-run.** At b₀ with F of scalar type 3, p⃗′ = 0 still holds: the new rows are of
type s1 with coefficient space 𝒮_1, so Schur applies. u has an ι⁺-term at 1 + μ_*, μ_* the s3 root in
(1, 1 + 10γ_C⁻¹). Now 1 + μ_* ∈ 1 + 𝒵 ⊂ Λ, its real part exceeds 2, and its order is at most k̄(1 + μ_*) by F1. So it lies
in ℰ_♯, and eq:iii-i12-3-3 holds. The strengthened example (non-real roots of real part ≈ 2.725, μ ≈ 1.725 + i·y) is
admitted the same way. (G) then asks ε_K < Re(1 + μ_*) − 2 < 10h, a smallness condition. A new counterexample would
need an exponent produced outside (1 + 𝒵) + ℕ₀ + increments. I found none. The candidates I checked are the
tf-pieces (u-exponents of α_0 plus ℰ_ind), the zf-terms of (vi) and (viii), the columns, the ℕ₀-shifts of
lem:iii-a-1-4, the reductions of lem:iii-i12-2-3 and lem:iii-i15-2-9 (windows in (−3, 1)), and the level-3 solves.

**The results R-V-I11 lists** (P = §4.1 checked step by step against the chapter):

- thm:iii-i12-3-1, Steps 0–5 (P).
- thm:iii-i14-3-1, Steps 1–4 and 4′: the new rows enter Step 2 at levels β_k > 3 only (P).
- cor:iii-i15-2-10 and lem:iii-i15-2-9 (P, F4).
- prop:iii-i13-2-1, Step 6 at β < 4 via def:iii-i13-1-1 (a), and lem:iii-i13-2-2 (P).
- lem:iii-j1-1-1: (G⁺) for the enlarged Λ; the "last sentence" citation (P).
- thm:iii-j-2-4: the step at λ₀ ∈ (1 + 𝒵) + increments, and lem:iii-j-2-3 (P).
- thm:iii-j1-2-1: Cases A and B at λ₀ = 1 + μ (P).
- prop:iii-i15-2-5: item (3), "rate above 1 > α_1 − 2" (P).
- thm:iii-i15-3-1: items (ii), (iii) and (vi) (P).
- cor:s25-tame: (Ex3) at b (P).
- prop:iii-i15-2-2 (b): level 1, by (G) on the new α_0.
- The ch.-43 uses: def:iii-j3-1-3, lem:iii-j3-1-4, prop:iii-j3-4-3 with items 12–13, and prop:iii-j3-4-6.
- lem:iii-i12-2-3 (a), item 10: 𝒜¹ ⊂ H̄_b^(s,α) for α < 1 with the b-density of sec:iii-f3-1; prop:iii-f3-4-1 (1) at
  α ∈ (0, 1].

**Λ after the repair.** It is finite below every bound: lem:iii-f1-2-4 on |Re ι| ≤ 3, each W_π contributing a polynomial
of degree 2 dim W_π. It is closed under conjugation. It does not depend on b (P2), on ε_K or ε_+, on the class or on the
data class. It is fixed at steps (1)–(3) of thm:vi-c-2-1, so before step (4); rows w1 and w2 of sec:vi-c-1 and
rem:half-class-changes and prop:own-same-index-sets are unaffected. Λ ∩ {Re ≤ 2} is unchanged.

The conditions stay satisfiable:

- (G): δ_G > 0, and the third window lives on π_1ℳ.
- (G⁺) and (Ex1): ε_+ below a positive minimum, independent of ε_+.
- (Ex2)–(Ex4), (A_J) and (A_K): finite or discrete exclusions.
- η_1 and η_2: finitely many values excluded.
- def:iii-i13-1-1 (a)–(c): discrete; and every admissible α ≥ 3 stays admissible there.
- η_0, J_*, l_* and k̄_0: unchanged (§2 (xi)).

**Placement.** From a git archive of HEAD c9b40e22, every old text of items 1–13 occurs exactly once as whole lines, at
41:140, 165, 179, 190, 204, 215, 571, 721, 823, 1223, 42:898 and 43:794, 805. These are the lines the items name. The
blocks do not overlap. The new blocks have exactly the stated line counts (6, 10, 11, 8, 10, 8, 58, 8, 17, 4, 1, 4, 3).
Every new line has at most 121 characters (counted in code points). No wrapped new line starts with "+ ", "- ", "* ",
"> ", "#", "=" or "|". One starts with "<" (n1). The style word list is not hit.

After applying the items in scratch:

- lint.py --chapters: 0 hits, 4752 labels.
- assemble.py --check: 0 problems.
- assemble.py, then lint.py --paper: 0 hits. lem:s22-c-roots is Lemma 33.11.
- The merged chapters 41–43 have no line over 121.

**Table rows sampled** (status H in §4.2, each read against the chapter): 03:276–286; 40:1306–1310, 1318–1324,
1326–1370; 41:21–28, 147–163, 223–235, 401–408, 410–488, 492–523 (but see m1), 590–620, 853–895, 1086–1096,
1474–1477, 1479–1491, 1493–1499, 1501–1520, 1604–1635, 1662–1705; 42:76–84, 110–118, 129–147, 207–227, 229–258,
552–556, 565–568, 570–574, 598–632, 636–686, 688–786, 787–802, 884–889; 43:465–485, 529–545, 547–557, 869–918, 975–990,
991–1005; 44:55–59, 73–105, 140–206, 228–262; 46:1807–1820, 1852–1860, 1909–1912, 2150–2156; 62:574–586; 63:232–274;
65:634. That is 49 rows, all correct as H. Also checked: every row marked P and every row marked I.

## Confirmation

Read: proofs/P-I11.md at md5 931e26d50bd8928098a3a870c6c15e62 (898 lines; committed at 8574b722), diffed against the
version read above (bf3b7c4c…); notes/reports/P-I11.md at 0138b84e…. Scratch merges from a git archive of HEAD
12c58adb (chapters 41–43, 71 and 96 are byte-identical to c9b40e22): P-I11 alone in
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/rpi11c/,
and P-I11 + P-UB1 (md5 58b580faf8acbc14503d7c5e33c0b087) + P-UB2 (md5 4b2831564a19e1572794761ce2ef77da) in
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/rpi11joint/
(script: rpi11calc/jmerge.py). No repository file edited.

**Verdict on P-I11: CONFIRMED.** m1 and n1–n5 are resolved; nothing else moved.

**The delta (diff bf3b7c4c → 931e26d5), chapter text.** Every changed or new block, and nothing else:
- Item 4: its last three lines are n1's text, word for word. The line count is unchanged at 8.
- Item 6: its last line is n2's text, word for word.
- New item 6a (41:522–523): m1 Replacement 2, word for word, at 4 lines.
- Item 7:
  - The statement opens with m1 Replacement 1, word for word. Once the hypothesis is taken out, the joined statement
    paragraph is identical to the old one.
  - The proof gains the writer's sentence "[[lem:iii-a-1-4]] asks that the order up to which it expands not be the real
    part of a root: the intermediate orders are chosen so, the roots being finitely many in every strip
    ([[lem:iii-f1-2-4]]), and q′ − 2 is so by hypothesis." Once that sentence is taken out, the joined proof paragraph
    equals the old one, so the rest is a rewrap only.
  - Item 7 has 61 new lines, as stated.
- Items 1–3, 5 and 8–13 are byte-identical.

**The writer's sentence is correct and in the right place.** The hypothesis of lem:iii-a-1-4 (30:1501) concerns the
order β up to which it expands. lem:iii-i11-2-1 applies it finitely many times. Each intermediate stopping order can be
taken off the real parts of the roots, because only finitely many roots lie in every strip |Re ι| ≤ X (lem:iii-f1-2-4,
as in prop:iii-f1-2-3 (f)). The final order q′ − 2 is off them by the new hypothesis. The sentence also agrees with
71:4536–4540 ("decreased slightly unless it is the target q′ − 2"), which now holds by that hypothesis.

**The delta, notes.** These match the coordinator's list:
- The header names the new HEAD and credits items 6a, 4 and 6.
- §1 item 1 has n2's wording, item 5 has n3's, and item 6 (d) is new.
- §2 (vii) adds the ε exclusion. Its wording "besides its finite set" sits oddly beside 6a's "that set contains", but it
  is harmless and in notes only.
- F1 states that q′ − 2 is off the roots at every level.
- Two table rows are edited, and the row 60:290–295 is added: 83 rows, counted.
- §5 gains the def:uc-choice bullet. 71:2592–2593 reads "besides the conditions that [[sec:iii-j2-1]],
  [[sec:iii-i11-1]] and [[def:iii-i13-1-1]] place on it", so the choice inherits 6a. P-UB1's lem:uc-admissible proof
  also takes ε "off finite sets" of those sections.
- §6 names P-UB1 and P-UB2 and asks that this file be merged with them, which settles my o3.
- The crosswalk row is unindented, with the pin PENDING:386. lem:s22-c-roots is at P-I11 line 386. The notes number
  eight.
- §8 is updated.

**P-I11 alone.** At HEAD 12c58adb all 14 old texts occur exactly once, as whole lines, at 41:140, 165, 179, 190, 204,
215, 522, 571, 721, 823, 1223, 42:898 and 43:794, 805. They are pairwise disjoint, and every "New, the N lines" count
matches its block. Every new line has at most 121 characters. No wrapped new line starts with "+ ", "- ", "* ", "> ",
"#", "=", "|", "− " or "<". After the merge:
- lint.py --chapters: 0 hits, 4834 labels.
- assemble.py --check: 0 problems.
- assemble.py, then lint.py --paper: 0 hits.
- lem:iii-i11-2-1 is Lemma 33.10 and lem:s22-c-roots Lemma 33.11.

**The joint merge P-I11 + P-UB1 + P-UB2.** I parsed 71 blocks: P-I11's 14, P-UB1's T1–T14, and P-UB2's 43 main blocks
(M1–M26 with their parts, O1–O4, L2–L5 and L4b). P-UB2's retired fallback set is no longer in the file.
- Every old text occurs exactly once at HEAD 12c58adb, including O1–O4 and L5 in 00, 01, 03 and 90, which changed
  since c9b40e22.
- No two blocks overlap. P-I11 touches chapters 41–43 only; P-UB1 and P-UB2 touch 00, 01, 03, 71, 90 and 96, so no
  file is shared between P-I11 and the other two.
- No new line exceeds 121 characters.
- Merged together, lint.py --chapters gives 0 hits and 4846 labels (4833 + 13), and assemble.py --check gives 0
  problems. assemble.py, then lint.py --paper, gives 0 hits. No line of the merged chapters exceeds 121.
- The texts agree: P-UB1's "the generator 1 + 𝒵 of [[def:iii-i10-1-1]]" and "1 + 𝒵 = {3} ∪ {ι ∈ Z : Re ι < 4}" match
  P-I11's definition and its "𝒵 consists of the root 2 and the ι^C_(·,+) − 1".

**Open for the joint merge (not in P-I11's items; in chapter 71).** P-I11 §5 lists every chapter-71 site for that
chapter's writer. P-UB1 and P-UB2 between them cover all of them except three, and those three then read wrong in the
merged edition. Exact texts follow, each tested on the joint scratch merge. After all three, lint gives 0 hits, assembly
0 problems and lint --paper 0 hits. None overlaps a block of the three files.

*J1 (minor). sec:uc-index-sets misquotes def:iii-i10-1-1* (71:2267–2280). It says "By [[def:iii-i10-1-1]], Λ is the
smallest set … that contains the generators" and lists five, without 1 + 𝒵. After P-I11 this misquotes the definition.
Old (71:2277–2278), then new (3 lines; widths 109, 12, 92):

```old
- 2 + π_1ℰ_col, with ℰ_col = ({(0, 0), (1, 0)} ∪ ℰ_ind ∪ (1 + ℰ_ind)) + ℕ₀ ([[lem:iii-i11-1-1]]), a subset of
  π_1𝒢 + ℕ₀;
```

```new
- 2 + π_1ℰ_col, with ℰ_col = ({(0, 0), (1, 0)} ∪ ℰ_ind ∪ (1 + ℰ_ind)) + ℕ₀ ([[lem:iii-i11-1-1]]), a subset of
  π_1𝒢 + ℕ₀;
- 1 + 𝒵, with 𝒵 the set of the indicial roots μ of L̂_b(0) with 0 < Re μ < 3 ([[sec:is-z]]);
```

(sec:is-z is P-UB1's T7.)

*J2 (minor). lem:cs-fourier (b), tf, misstates lem:iii-i11-2-1* (71:4379–4381). It says "By [[lem:iii-i11-2-1]], û_0
has at ∂X the exponents of (ℰ^♭ − 1) ∪ (1 + ℰ_col) ∪ (2, ·)". After P-I11 the lemma also gives the (μ, ·) for the roots
μ ∈ 𝒵 below 2 + ε_+ − ε. The conclusion "of real part at least 1" still holds, as 𝒵 ⊂ {Re > 1}. P-UB2's M15a and M15b
touch only 4396–4406. Old (71:4380–4381), then new (3 lines; widths 113, 113, 93):

```old
(ℰ^♭ − 1) ∪ (1 + ℰ_col) ∪ (2, ·) and their ℕ₀-shifts, of real part at least 1, as ℰ^♭ ⊂ {Re ≥ 2} and ℰ_col ⊂ {Re ≥ 0}
([[lem:iii-i11-1-1]]); for j ≥ 1, û_j has exponents of real part at least η_1 > 0 (Step 2), and the factor σ^j adds j at
```

```new
(ℰ^♭ − 1) ∪ (1 + ℰ_col) and (μ, ·) for the roots μ ∈ 𝒵 with Re μ < 2 + ε_+ − ε, and their ℕ₀-shifts, of real part
at least 1, as ℰ^♭ ⊂ {Re ≥ 2}, ℰ_col ⊂ {Re ≥ 0} ([[lem:iii-i11-1-1]]) and 𝒵 ⊂ {Re > 1} ([[def:iii-i10-1-1]]); for
j ≥ 1, û_j has exponents of real part at least η_1 > 0 (Step 2), and the factor σ^j adds j at
```

*J3 (nit). sec:sp (d) calls a question open that P-I11 has decided* (71:4039–4040). The text says "whether ι₁, a root ι
of some P_l or such an ι + 1 lies in Λ is not decided here". After P-I11 all of them lie in Λ:
- ι₁ − 1 and ι − 1 lie in 𝒵, ι₁ being the simple root of C above 2 (71:3905) and 2 < Re ι ≤ 3 + ε_+.
- So ι₁ and the roots ι lie in 1 + 𝒵, and the ι + 1 lie in Λ + 1 ⊂ Λ.
- The proof's "no statement of this section uses whether another pole … lies in Λ" (71:4078–4079) stays true.

Old, then new (3 lines; widths 116, 114, 70):

```old
simple. Of these poles, 3 lies in Λ ([[def:iii-i10-1-1]]); whether ι₁, a root ι of some P_l or such an ι + 1 lies in
Λ is not decided here, and no bound depends on it, each raise being at most 1 by (c). The numbers λ_♯ + j,
```

```new
simple. All of them lie in Λ ([[def:iii-i10-1-1]]): 3 is a generator; ι₁ and the roots ι lie in the generator 1 + 𝒵,
as ι₁ − 1 and ι − 1 are indicial roots of L̂_b(0) of real part in (1, 3); and the ι + 1 lie in Λ + 1 ⊂ Λ. No bound
depends on it, each raise being at most 1 by (c). The numbers λ_♯ + j,
```

The other chapter-71 sites in P-I11 §5 that no block touches stand as written:
- the lem:iii-i11-2-1 charges of lem:cs-elem (71:4164, 4220, 4266, 4452–4462): the step count depends on weights, not
  on the roots met, and the residues are charged 0;
- lem:uc-fourier-count and lem:uc-phi-loss: general formulas in N_Λ;
- prop:is-iota and prop:is-mult;
- rem:ec-not-evaluated: def:uc-choice is admissible again with P-UB1.

**Reply: P-I11 is CONFIRMED.** The joint merge is mechanically clean: no overlaps, lint and assembly clean. Open before
the three are merged into the edition: J1 and J2 (minor) and J3 (nit), three chapter-71 texts that none of the three
files carries.
