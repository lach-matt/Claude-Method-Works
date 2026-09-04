# READ-ch14j — Chapter 23 *The cost surface*, §23.1–§23.5.3 (main member L6178–L6302)

Chat 95. Unit **125 lines, ten headings**: §23.1 L6180, §23.2 L6196, §23.2.1 L6215, §23.3 L6221,
§23.4 L6239, §23.4.1 L6248, §23.4.2 L6261, §23.5 L6272, §23.5.1 L6279, §23.5.2 L6289, §23.5.3
L6296. Chapter 23 runs L6178–L6622 (445 lines, 37 headings); Chapter 24 opens L6623. Every
boundary re-measured on the member by heading scan before a line was read; all agree with
HANDOFF-47's opening scan. §23.6–§23.15 are **not** read and are owed to chat 96.

Instruments: **r2-ch14j** (computable, 50 verdicts) and **r2-ch14k** (prose, 19 verdicts). Both
banked. `section_span`, `has_token`, `enclosing` and `heading_line` were lifted into r2lib this
chat and are imported, not copied.

Findings are recorded, not repaired (chat 67 hold). No Register entry is written.

---

## A — Deviations

**14j-01 · §23.3 L6233 · the 32/11 floor does not survive §23.4's free *h*.**
The impossibility table prints *V* ≥ **32/11** — *no guarantee is ever cheaper than 2.909 ×* — as
one of four unconditional statements. MEASURED: d/dr [4r³/(3r²−1)] = 12r²(r²−1)/(3r²−1)², zero at
r = 1, so the exact expression is increasing for r > 1 and its infimum is **V = 2**, not 32/11.
32/11 is the value at r = 2. Two sections later §23.4 L6242 states *nothing forces h = 1* and
§23.4.1 runs *h* to 4; on the chapter's own numbers ν = 40 with h = 20 gives r = 2 and V = 2.909091
exactly, and any h > ν/2 goes below it. The three levels require h < ν, i.e. r > 1, so V > 2
strictly with 2 as the infimum. **32/11 is the floor of the h = 1 series, not of V.** The algebraic
floor of 2 (Proposition 23.1) is the one that survives free *h* — which §23.2 L6213 already says,
calling 32/11 "the tighter of two" without the scope that makes it true.

**14j-02 · §23.3 L6237 · "exact to four decimals by ν = 10" is false.**
MEASURED at ν = 10: exact 4000/299 = 13.3779264214, asymptote 4ν/3 + 4/(9ν) = 602/45 =
13.3777777778, absolute difference 1.486436 × 10⁻⁴. To four decimals (Decimal.quantize,
ROUND_HALF_UP) the two are **13.3779 against 13.3778** — not equal. They agree to **three**
decimals (13.378), and to four significant figures (13.38). Four decimals is first reached at
**ν = 16**. The companion claim in the same sentence, *low by 0.69 % at ν = 2*, reproduces exactly
(0.6944 %).

**14j-03 · §23.2 L6206 · "This holds for any monotone sequence whatever" is false of two classes.**
Proposition 23.1 hypothesises y₀ < y₁ < y₂ — strict monotonicity — and concludes V > 2. MEASURED:
for a monotone sequence with one vanishing step (d₀ = 0), w = d₁, e = d₁/2 and **V = 2 exactly**,
not > 2; for an arithmetic sequence (d₀ = d₁), e = 0 and **V is undefined**, not divergent. Both are
monotone. The sentence generalises the proposition past its own two hypotheses. §23.2.1's
Observation states the min/max condition correctly; L6206 does not.

**14j-04 · §23.1 L6189 · p = 0 lies inside the printed range and is degenerate.**
*Verified on power laws from p = −3 to +11.* MEASURED at p = 0: y = x⁰ is constant, so w = 0 and
e = 0 and V is 0/0, while the printed formula 4x/(h|p−1|) returns a finite 400 at x = 1000, h = 10.
The chapter names only **p = 1** as excluded (L6234, the pole). A constant sequence also fails
Proposition 23.1's strict-monotonicity hypothesis. Two degenerate exponents inside the range, one
of them named.

**14j-05 · §23.1 L6189 · "agreement under 1 %" is not testable as printed (unprinted-input class).**
The formula is asymptotic in h/x and the sentence prints neither. MEASURED worst deviation across
p = −3…+11 (p = 0, 1 excluded): h/x = 1/2 → 60.924 %, 1/5 → 24.893 %, 1/10 → 8.091 %, 1/50 →
0.358 %, 1/100 → 0.090 %, 1/500 → 0.004 %, worst always at p = +11. The claim holds for h/x ≤ 1/100
and fails at 1/10 and coarser. Joins DEFERRED's six-member unprinted-input class as its **seventh**.

**14j-06 · §23.5.1 L6283 · the printed w²/e is exact but sign-inverted against the book's own e.**
MEASURED symbolically for y = x⁻²: w²/e with **signed** e is exactly
16x⁴/(h⁶ − 5h⁴x² + 7h²x⁴ − 3x⁶), the printed rational, byte for byte. But L6181 and L6200 define
e with an absolute value, and for y = x⁻² the signed e is negative. At x = 1, h = 1/10 the printed
rational gives **−5.459821** where the book's own w²/|e| gives **+5.459821** and 8y′²/y″ gives
+5.333333. As h → 0 the printed form tends to −16/(3x²), the negative of 8y′²/y″, so the sentence
*equals 8y′²/y″ only as h → 0* is off by a sign. The h-dependence, which is the point of the
withdrawal, is unaffected.

**14j-07 · §23.5.1 L6287 · "the only h-free combination is a = 2, b = −1" is false as stated.**
h-free means a + 2b = 0, which has a one-parameter family of integer solutions. MEASURED with
|a|,|b| ≤ 6: (−6,3), (−4,2), (−2,1), (0,0), (2,−1), (4,−2), (6,−3). (4,−2) is (w²/e)² and (−2,1)
its reciprocal, both h-free; (0,0) trivially so. True only up to a common power and the trivial
case. The section's conclusion — that the leading-order invariant is unique — survives; the
uniqueness statement does not.

**14k-01 · §23.4.2 L6270 · the ν_V pointer resolves to the wrong section, at two sites.**
*the ν_V ceiling of §23.11.* MEASURED on §23.11 (span L6519–L6548, *The refusal pattern carries
four verdicts, not one*): **ν_V 0, ceiling 0, granularity 0, quotation 0, curvature 0, resolve 0**,
word-bounded and case-exact. The claim lives at **§23.15** *The second admission bound* (L6606–
L6621), which carries the formula ν_V = (3Z²R/5q)^{1/4}, the quotation granularity *q*, the ν_V
table and the failing cells. **The same wrong pointer stands at L6923** — *curvature too fine to
resolve (ν > ν_V, §23.11)*. The volume's own index at **L11448** reads *ν_V …… §2.3 · §23.14 ·
§23.15* and is right. Two prose sites against a correct index: a class of two, not a slip.

**14k-02 · §23.4.2 L6270 · the outlier attribution has no witness for Ga I.**
*Al I at n = 51 and Ga I at n = 53 both sit above the ν_V ceiling.* MEASURED: §23.15 L6619 gives
**Al I nf's four failing cells as n = 48, 51, 53, 54** — both 51 and 53 are Al I, not one Al I and
one Ga I. §23.15's ν_V table carries three channels (K I nd, Na I ns, Al I nf); **Ga I appears in
it zero times**, so no ν_V is printed for Ga I anywhere and "both sit above the ν_V ceiling" has no
witness for the second species. Ga I's one appearance in §23.11 is L6538, *Ga I 4s²np ²P°, 15
members, 1 refusal, a bifurcation* — a different test from a ν_V exceedance. The sentence appears
to have merged §23.11.1's refusal table with §23.15's ceiling table.

**14k-03 · §23.2.1 L6216 · "Observation 14.2" is numbered for the wrong chapter.**
MEASURED: the main volume declares **two** numbered statements on indented lines — Proposition 23.1
at L6199 (chapter 23, correct) and Observation 14.2 at L6216 (chapter 14, standing in §23.2.1).
One mismatch of two declarations. §14.2 exists (heading at L3711), so the label reads as a Chapter
14 back-reference rather than as this chapter's own observation. The five further
"Proposition 23.x" hits at L7273, L7583, App C.1, C.2 and E.2 are **citations of Proposition 23.1,
not declarations** — the first run of r2-ch14k scored them as mismatches and was wrong.

**14k-04 · §23.2.1 L6219 · the wrong clause of Rule 1 is cited.**
*the small step is produced by two channels interleaving, which Rule 1's second clause excludes.*
MEASURED against Rule 1 as printed at L6040–L6043: clause 1 is *bracket only cells belonging to the
same Rydberg sequence as their neighbours and sharing a term set with them*; clause 2 is *either
interior — a measured neighbour on each side — or above the highest measured member*; clause 3
forbids extrapolation below the lowest measured member. Interleaving channels are excluded by
**clause 1** (channel identity), not clause 2 (position within a channel). The book's own witness
is L6834 — *Cu II, core-excited configurations interleave the series* — which is a same-sequence
failure. Right rule, wrong clause.

---

## B — Verified

1. **Proposition 23.1's proof is exact** (L6199–L6204). Symbolically: w = d₀ + d₁; e = |d₀ − d₁|/2;
   V = 2(d₀+d₁)/|d₀−d₁|; V > 2 with zero violations over 3,422 strictly-monotone integer pairs;
   V → 2 monotonically from above as min/max → 0 (2.444444, 2.040404, 2.004004, 2.000400, 2.000040,
   2.000004); V diverges as d₀ → d₁.
2. **The exact cost is V = 4ν³/(h(3ν² − h²)) = 4r³/(3r² − 1)** (L6244), derived from
   T = I − RZ²/ν² and MEASURED identical. The substitution r = ν/h is exact, not approximate.
3. **I, R and Z all cancel identically** (L6246). MEASURED free symbols of V: {h, ν} only. This
   **confirms 14h-02 from the chapter rather than re-deriving it** — the ionisation limit is absent
   from V, so *ν, δ and V all need the ionisation limit* (main L6133, App A.12 L10035) is false of V.
4. **All five printed rationals** (L6237): ν = 2 → 32/11, 3 → 54/13, 4 → 256/47, 5 → 250/37,
   10 → 4000/299, each reproduced both from the closed form and from three Rydberg levels.
5. **4ν/3 + 4/(9ν) is the true expansion through 1/ν**; next term 4/(27ν³). *Low by 0.69 % at
   ν = 2* MEASURED 0.6944 %.
6. **The Figure 23.1 caption** (L6193–L6194): 32/11 = 2.909 (3 dp, HALF_UP); the asymptotic form at
   ν = 2 is exactly 26/9; low by 0.69 %; the gap falls 0.69444 → 0.13717 → 0.04340 → 0.01778 →
   0.00111 % across ν = 2, 3, 4, 5, 10, so *they converge by ν = 10* holds at under 0.01 %.
7. **The (ν, h) table to six figures** (L6250–L6257): (20,1), (40,2), (60,3), (80,4) all
   26.688907; (10,1), (40,4) both 13.377926; **identical across Z = 1, 2 and 6** as L6259 claims.
8. **V = 26.689 at ν = 20** (L6222), and V is invariant under a common shift of all three levels,
   so the three precisions agree **exactly**, not to six figures. σ = 10⁻² to 10⁻⁸ is six orders of
   magnitude as stated.
9. **w = 2y′h + O(h³) and e = y″h²/2 + O(h⁴)** (L6277): MEASURED by series — w has no h² term and
   e no h³ term, so both orders are right.
10. **The 2.2 % rise** (L6285): (374.5 − 366.3)/366.3 = 2.2386 % → 2.2 % (1 dp, HALF_UP), and the
    four values rise monotonically.
11. **dw/dh > 0 and dV/dh < 0** (L6290): zero violations over 90 steps in six families — x², x³,
    eˣ, −1/x, x⁻², and the Rydberg term itself — including the decreasing-convex ones. The Pareto
    reading at L6292 follows from the two signs.
12. **h\* = √(2β/(αy″))** (L6299) derived exactly; y′ cancels. At ν = 40, β/α = 10, R =
    109737.31568, Z = 1: |y″| = 6R/ν⁴ = 0.257197 and **h\* = 8.818246 → 8.82**, the printed value,
    reproduced from chat 93's settled constants. The *11 % miss* is 11.22 % taken against the
    formula value (12.64 % against the direct minimum); the three other pairs miss by 0.18 %,
    0.40 % and 1.59 %.
13. **1,033 = 560 + 473** (L6266–L6268), and the pooled median 0.69 % lies between the part medians
    0.49 % and 1.15 % as a pooled median must.
14. **53.3 and 13.4** (L6275) reproduce exactly at ν = 40 across h = 1 → 4 (53.3444, 26.6889,
    17.8112, 13.3779).
15. **L6211 stands**: MEASURED across the six volumes, every **live** printed V exceeds 2. The only
    sub-2 figures are the 0.24 data of the withdrawn Figure 15.3 / 23.3 (main L6483, L7585), whose
    cause §28.7.3 records as a rigged comparison — bracket and estimate drawn on different node
    sets — withdrawn at correction 97, which falls inside Chapter 28's 93–98 block as L6484 says.
16. **L6285's "recorded in Chapter 28" resolves**: main L7487, *50. A conservation law that is not
    one. w·V = 8y′²/y″ claimed independent of h.*
17. **L6259's §16.3 pointer resolves to the claim**, not just the heading: §16.3 (L4359–L4406,
    *D1 — D_phys catches a wrong value in the data*) carries Z_eff, charge, wrong ×3 and bracket ×3.
18. **Zero Register citations** in the 125 lines, upper or lower case — and **zero in the whole of
    Chapter 23** (L6178–L6622). Chapter 22's first 99 lines carried three.
19. **Rulings 45 and 46 hold** in the range: no build number, script name, chat reference or
    Register-entry remark in L6178–L6302.
20. **14h-06 confirmed from the chapter**: §22.6's *the only linearly rising quantity* (L6175)
    stands as printed, and §23.1's V(x, p) = 4x/(h|p−1|) is linear in x with slope 4/(h|p−1|) > 0
    for **every p ≠ 1** — one counterexample per exponent, on top of §22.4's L = n/3.
21. **Figure 23.1** is called once (L6191) and captioned once (L6193), appears in no other volume,
    and its file token `figure-23.1.png` appears once.

---

## C — Incidentals

- **C1 · Thirteen of thirty-two figures in the range appear exactly once in all six volumes**:
  26/9, 54/13, 256/47, 250/37, 4000/299, 26.689, 53.3, 0.1743, 0.1750, 2.7886, 2.7450, 8.82, 7.83.
  Internally consistent where a check exists (all five rationals and 8.82 reproduce), but nothing
  in the collection can contradict them. Same standing item as chat 94's C6 and chat 93's C-8.
- **C2 · 0.69 % carries two unrelated meanings twelve lines apart.** L6194 is the asymptote's error
  at ν = 2; L6268 is the pooled median deviation of 1,033 measured pairs. Identical digits, no
  relation. Worth a reader's confusion; not a defect.
- **C3 · The h = 2 median does not scale as the algebra predicts.** Deviation from 4r/3 is
  1/(3r² + 1), so 0.49 % implies r ≈ 8.23 and 1.15 % implies r ≈ 5.35. Halving r at equal ν would
  quadruple the deviation (0.49 → 1.96 %), against the printed 1.15 %; consistent only if the h = 2
  sample sits at higher ν. The level list is in no volume, so this is not checkable.
- **C4 · §23.5.1 is headed *A withdrawn proposition* but withdraws no numbered proposition.**
  MEASURED: the word "Proposition" appears zero times in the section body, and Chapter 23's only
  numbered proposition is 23.1, which stands. The withdrawn object is a conservation-law claim.
- **C5 · The 1,033-pair count is not restated in Chapter 24, *The collection*.** Chapter 24's own
  four-digit counts are 1,061, 1,105 and 1,442. Whether 1,033 should reconcile with any of them is
  a subject-matter question the read cannot answer.
- **C6 · "similarity law" (L6259) appears once in six volumes** and is not defined at its point of
  use. The Index of Indices does not carry it.
- **C7 · Five claims in 125 lines rest on data no volume carries**: L6189 (no h, no x), L6263 (the
  1,033 pairs), L6266 (the three medians), L6292 (the 172 monotone steps), L6301 (the three direct
  minimisations print no ν or β/α).
- **C8 · §23.10.2 L6483 and §28.7.3 L7585 are the volume's only sub-2 V figures**, both naming the
  withdrawn 0.24 data. L7583 adds that *241 of 570 ratios fell below 1*. R3 should note that
  L6211's universal claim is true but its only real test is a withdrawal the sentence does not cite.
- **C9 · Chapter 23 adds no third sense of σ.** MEASURED nine σ sites in the chapter (L6222, L6223,
  L6503, L6551, L6553, L6554, L6556, L6578, L6585); all are measurement or quotation uncertainty.
  §23.3 L6222 states *V contains no σ* and J3 confirms V's free symbols are {h, ν}. The collision
  DEFERRED opened (14h-01) is between §22.5 and Rule 4 only.
