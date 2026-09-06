# READ-ch14h — Chapter 22 remainder, *The four rules* to *What the bracket costs*

Main member `The_Method_1_6-2.md` **L6036–L6177 — 141 lines, eleven headings**, read whole in
chat 94. Boundaries measured by heading scan before any line was read; the chapter ends L6176,
Chapter 23 opens L6178. Instruments: `r2-ch14h` (computable, 17,870 B · md5 b788fa4d · 263 lines)
and `r2-ch14i` (prose, 14,454 B · md5 de696a7a · 208 lines). Census rows in range: 1, closed in
`CENSUS-CLOSURES-ch14h.tsv`.

**A boundary correction recorded before the read.** HANDOFF-46 carried §22.2.1–§22.6 at
L6056–L6175 and the chapter end at L6178. Measured on the member: **§22.2.1 L6055, §22.2.2 L6070,
§22.2.3 L6086, §22.2.4 L6100, §22.2.5 L6106, §22.3 L6128, §22.4 L6137, §22.4.1 L6147, §22.5 L6167,
§22.6 L6174**, chapter ends L6176, Chapter 23 opens L6178. Every figure after §22.2 was one high.
§22.2 (L6036) was chat 93's own end boundary and was measured on the member; the forward scan of
the remainder was taken on the bundle, which numbers one higher because of its `<<<FILE:` header.
This is the third time the project has met this collision and the first time inside a handoff that
warns about it.

---

## A — deviations

**14h-01 · §22.5's admissibility ratio cancels against the chapter's own σ (L6047, L6168–L6172).**
§22.5 states `r = 2Z²R/(ν³σ) ≥ 5` and that *r* falls as ν⁻³. Rule 4, 121 lines earlier, defines
**σ = 2R Z_eff² · SE_pred / ν³**. Substituting Rule 4's σ into §22.5's r cancels ν³ identically:

> r = 2Z²R / (ν³ · 2R Z_eff² SE_pred / ν³) = Z² / (Z_eff² · SE_pred)

MEASURED at ν = 10, 20, 40, 80: r = 100.000000 at every ν, constant. Under the other reading — σ
as the measured levels' own uncertainty, which is what "separated by more than their uncertainty"
(L6168) says — r falls as ν⁻³ exactly, each doubling of ν dividing r by 8. **The chapter uses one
symbol for two quantities and never says which is meant**, and the section's scaling claim is true
under one and false under the other. The admissibility rule is the chapter's stated domain
boundary, so which σ is meant decides where every channel leaves the domain.

**14h-02 · "ν, δ and *V* all need the ionisation limit" is false of *V* (L6133; also App A.12
L10035).** V is defined at §23.1 L6183 as **V = w/e**, with w = |T(n+1) − T(n−1)| a first
difference and e = |T(n) − ½(T(n−1) + T(n+1))| a second. An additive constant cancels from both,
so V is unchanged by T = I − E at every I. MEASURED at I = 0, 100,000 and 1,000,000 on the same
three levels: w = 5000.0000, e = 500.0000, V = 10.000000 in all three cases, including I unknown.
This is the same cancellation App A.12 proves for containment at L10029–L10033 and the same one
§22.4 states for δ₀ at L6142. ν = Z√(R/T) and δ = n − ν do need the limit; V does not. The claim
stands in two places — main L6133 and App A.12 L10035, worded almost identically — so the repair is
one decision applied at two sites.

**14h-03 · §22.2.2's "same magnitude of asymmetry" is false by a factor of 193 (L6077–L6080).**
The n row gives 446× toward the loose end and 0.28× toward the tight end, an asymmetry of
**1,592.86**. The Z row gives 17.3 % and 2.1 %, an asymmetry of **8.24**. The two differ by
**193×**. *Same sign* holds on the reading the sentence uses — both axes cost more toward the loose
end — and the cause claim is not tested here. The magnitude claim does not hold. Two further facts
belong with it: the two rows carry **different kinds of quantity in the same three columns** (the n
row is a ratio with interpolate = 1×, the Z row an absolute error with interpolate = 1.3 %), and on
the ratio reading the tight ends fall on opposite sides of their own baselines — 0.28× is below
interpolation on n, 1.62× is above it on Z.

**14h-04 · "Agreement to four figures" is claimed of two pairs, one of which shares one digit
(L6148–L6149).** The section prints measured against predicted at two n: **4,329 vs 4,267** at
n = 8 and **1.387 × 10⁶ vs 1.386 × 10⁶** at n = 55. Both pairs are *quoted* to four significant
figures and **neither agrees to four**. The n = 55 pair shares three digits and differs by one unit
in the fourth (0.072 %); the n = 8 pair shares **one** and differs by 62 units in the fourth
(1.453 %), twenty times worse. One phrase covers both.

**14h-05 · Two pointers of five do not resolve to their claim.**
- **L6135 → §25.6, "the antiprotonic-helium cells of §25.6".** MEASURED: ten sites in the main
  volume name antiprotonic helium and **none falls inside §25.6** (L6991–L7116), which is Sc VI
  throughout. The worked cells are §16.4 (L4419) and §19.2 (L5401, L5416); §2.8 L612 names §16.4
  for the same check. This is the stated payoff of limit-freedom and it points at the wrong section.
- **L6138 → §32.3, "§32.3 presents limit-freedom as pure gain".** §32.3 is *Self-defence*
  (L9038–L9058) and carries ⅅ_def, ⅅ_phys and D3. MEASURED word-bounded in its body: *limit* 0,
  *threshold* 0, *ionisation* 0, *gain* 0, *bracket* 0, *free* 0. §22.4's whole premise is a
  correction of what §32.3 supposedly says. **This is the second failed prose citation of §32.3** —
  chat 91 recorded the first at L5692 (§32.3 cited for ℛ reaching level 2). Of the four prose
  citations of §32.3 in the volume, two fail on content and a third (L7492) miscounts its clauses;
  the three index entries resolve.

The other three resolve, and two of them exactly: **L6114 → §25.6** (§25.6.1 prints the same two
defects 1.0057 / 0.9812 at L7004 and the bracket 0.9376 < δ(6s) < 0.9812 at L7014, which excludes
the constant form's 0.9934), and **L6098 → §25.6** (§25.6.6 *A second route to the same prediction*
carries the isoelectronic route at L7106 with 3.5 % printed on it). **L6175 → Chapter 23** resolves.

**14h-06 · §22.6's closing sentence has a counterexample thirty-two lines above it (L6142,
L6175).** *"the price is the only linearly rising quantity in the structure."* The price is
V = 4ν/3 (L6183), linear. But §22.4 prints **L = |δ′/δ″| = n/3** at L6142, also linear in n, with
V/L = 4.0000 at every n. §23.1's general form V(x, p) = 4x/(h|p − 1|) supplies a further linearly
rising quantity for each p ≠ 1. Either *only* is unqualified or the quantities it excludes must be
named.

**14h-07 · "true for some species, false for others" has no witness among its own two ranges
(L6165).** The sentence prints the collection's tightest bracket, **1.398 cm⁻¹**, and its limit
uncertainties, **0.001 to 0.4 cm⁻¹**. The δ route wins where the limit is known better than the
bracket. Worst printed case, with the limit entering at both edges: 2 × 0.4 = **0.8 cm⁻¹** against
the narrowest printed bracket **1.398 cm⁻¹** — the δ route still wins, by 1.75×. For it to lose, a
channel would need σ_limit ≥ 0.699 cm⁻¹ against a bracket at the collection minimum, above the
printed maximum. The *false for others* half of the conditional is unwitnessed by the two ranges
the sentence itself supplies. (1.398 cm⁻¹ is confirmed as the tightest at main L6974, Al I 3s²nf
n = 54, and L6987.)

**14h-08 · Five printed figures do not follow from their own printed inputs.** The class chat 93
opened at §22.1.1.1 recurs five times in 141 lines:

| site | printed | from the printed inputs | needs |
|---|---|---|---|
| L6060 | **446×** | 206 / 0.46 = 447.83 (rounds to 448) | an unrounded median 0.4619 |
| L6068 | **1,577** | 206 / 0.13 = 1,584.62 (rounds to 1,585) | inputs other than 206 and 0.13 |
| L6093 | **3.47 %** | \|0.7376 − 0.7129\|/0.7129 = 3.4647 % (rounds to 3.46 %) | a predicted δ of 0.737638 |
| L6104 | **a factor of 17** | 0.14 / 0.008 = 17.5 (rounds to 18) | an unrounded 0.136 |
| L6114 | **0.9934** | (1.0057 + 0.9812)/2 = 0.99345 (half-up 0.9935) | truncation, not rounding |

The 1,577 case is the hardest of the five: the asymmetry is **baseline-independent** — (206/m)/(0.13/m)
= 206/0.13 for every median m — so no choice of the unprinted baseline recovers it. The printed
206 and 0.13 are irreconcilable with the printed 1,577 at 0.48 %.

**14h-09 · §22.4.1's predicted column needs a δ₂ the section never prints (L6148–L6158).** The
narrowing factor n³/(2δ₂) reproduces the printed predicted column only at **δ₂ = 0.06**: 512/(2 ×
0.06) = 4,266.7 → 4,267 and 166,375/(2 × 0.06) = 1,386,458 → 1.386 × 10⁶. The same δ₂ reproduces
the table two paragraphs later — w_T/w_δ = 66,725 against 66,667 at n = 20, and 532,378 against
533,333 at n = 40. δ₂ appears nowhere in §22.4 or §22.4.1. This is chat 93's C-2 (the unprinted
δ = 0.35) in the same chapter, one section further on, and it is the same repair.

**14h-10 · "its neighbours are two principal quantum numbers away" is true of the span, not the
neighbours (L6121–L6124).** The section names the Kr I (²P°₁⁄₂) *n*p series as 5p, 6p, 7p with 6p
interior. Each neighbour is **one** principal quantum number from 6p; the bracket **spans** two.
The 14,602 cm⁻¹ width is attributed to the neighbours' distance, which is one, not two.

---

## B — verified

- **B1.** The fit table's error column, L6090–L6094: 14.9 % and 9.9 % reproduce exactly from the
  printed predicted/true pairs (14.8688 %, 9.9032 %). Two of three; the third is 14h-08.
- **B2.** L6096's *factor of 1.7*: 3.5/2.1 = 1.6667 → 1.7, and the table's 3.47/2.1 = 1.6524 → 1.7.
  The factor follows from the rounded figures the sentence itself uses.
- **B3.** The ablation table's other three ratios reproduce: 0.13/0.46 = 0.2826 → 0.28;
  588/200 = 2.94 → 2.9; 41.3/12.8 = 3.2266 → 3.2, which is also §22.2.4's 3.2× at L6101.
- **B4.** L6084's hold-outs are the constituents of the L6078 Z row: mean(11.1, 23.4) = 17.25 and
  mean(1.8, 2.5) = 2.15. Both means land exactly on a rounding boundary; the loose end reproduces
  under half-up, the tight end under neither convention (recorded as C1, not as a defect of the
  arithmetic).
- **B5.** Rule 4a operates exactly as §22.2.5 works it: the channel is decreasing (0.9812 < 1.0057),
  Rule 4a requires δ̄ ≤ δ(last measured) = 0.9812, and δ̄ = 0.9934 exceeds it, so the constant form
  is inadmissible. The section's *above δ(5s)* is correct.
- **B6.** L6121's 0.12σ: 70.9/602 = 0.11777 → 0.12. Reproduces.
- **B7.** L6142's **L = |δ′/δ″| = n/3, "the same as T's"** holds analytically and numerically at
  n = 4, 8, 20, 40, 55: for δ = δ₀ + δ₂/n², |δ′/δ″| = n/3 independently of δ₂ and of δ₀; for
  T = Z²R/ν², |T′/T″| = ν/3 independently of Z²R. Both reduce to the same expression.
- **B8.** L6142's **δ₀ cancels from both w and e** holds exactly as worded — on w and e built from
  δ, which is the section's subject (L6140). MEASURED at δ₀ = 0.00, 0.35, 0.85, 5.00:
  w = 0.0004837491 and e = 0.0000451153 at every δ₀.
- **B9.** The limit-uncertainty table's last column is the via-δ width **plus 2σ** at both n:
  0.00102 + 0.02 = 0.02102 → 0.0210, and 0.0000143 + 0.02 = 0.020014 → 0.0200. The limit enters at
  both edges, which is the correct treatment.
- **B10.** §22.3's containment argument: T = I − E reverses order and exchanges min with max, so
  betweenness is preserved. Verified against App A.12's proof at L10025–L10033.
- **B11.** L6160's *three orders*: 0.01 / 1.43 × 10⁻⁵ = 699.3 = 2.845 orders. Rounds to three.
- **B12.** Four negative claims in the range, four separate witnesses, each measured apart from its
  claim: §22.2.2 (the Z axis and the two hold-out sequences), §22.2.4 (Sc III 3d, 3.2× and 0.14
  against 0.008), §22.3 (App A.12's proof), §22.5 (r's ν⁻³ fall). Two hold outright; two hold only
  under a reading the text does not fix — those are 14h-01 and 14h-02.
- **B13.** No printed pair count appears in the range, so this volume's C(N, 2) convention has no
  site here.

---

## C — incidental

- **C1.** Both Z-row entries at L6078 are means of the two printed hold-outs and both land exactly
  on a rounding boundary (17.25, 2.15). No single convention produces both: half-up gives 17.3/2.2,
  half-even gives 17.2/2.2, against the printed 17.3/2.1. The interpolate column (1.3 %) has no
  printed constituents anywhere in the chapter.
- **C2.** The ablation table's *cost* column carries four baselines — a median of 0.46 (rows 1–2),
  an rms of 200 (row 3), a coverage fraction (row 4) and a median of 12.8 (row 5) — and does not
  say that they differ. Row 4 is also the only row where the larger number is the violation:
  ±1σ coverage 96.2 % against 69.6 %, where the nominal for 1σ is 68.3 %. The per-cell figure is
  1.3 points from nominal, the pooled figure 27.9 points from it; the row would read more clearly
  against the nominal it is implicitly using.
- **C3.** **Zero Register citations in 141 lines.** MEASURED against neighbours: Chapter 21
  L5597–L5936 carries 11 (3.24 per 100 lines), Chapter 22's first 99 lines carry 3 (3.03), this
  range carries 0, Chapter 23's 445 lines carry 0. Chapter 22's two halves differ in kind and not
  only in rate — the first half states results and cites them, the second states rules and does not.
- **C4.** §25.6 is not settled on its own vocabulary, which is why L6098's *the Sc VI prediction*
  cannot be judged against it. §25.6's title (*and why it is not a prediction*) and §25.6.3 (*The
  value below is not a prediction, and calling it one was a category error*) deny the word; §25.6's
  own opening line at L6992 (*which makes it a prediction*) and §25.6.6's title (*A second route to
  the same prediction*) use it. MEASURED inside §25.6: *prediction* 10, *deduction* 3.
- **C5.** L7492's erratum states *§32.3's four clauses*; §32.3 prints **three** labelled clauses
  (ⅅ_def, ⅅ_phys, D3). Outside this read's range; recorded because it surfaced while resolving the
  §32.3 pointer, and it is the third of the four prose citations of §32.3 to disagree with the
  section.
- **C6.** **Seventeen of the twenty-four figures checked appear at no other site in any of the six
  volumes** — 69.6, 41.3, 12,942, 0.8189, 0.7129, 0.7376, 0.7835, 3.47, 14,602, 4,329, 4,267,
  1.387, 1.386, 68.06, 0.00102, 0.0210, 7.613. Each is a single-witness figure: internally
  consistent where it can be checked, and uncontradictable by anything in the collection. R4 should
  say so rather than leave them looking checked.
- **C7.** L6066's withdrawal of the earlier 3.7× figure (18.8× on rms, 4.6× on median, 0.5×
  without the two worst cells, one 12,942 cm⁻¹ outlier) rests entirely on data held outside the six
  volumes. It is the model of a correction the book makes well, and none of its four numbers can be
  re-measured here.
- **C8.** §22.2.3 is the second site in two chapters to price a route at 3.5 % rather than 2.1 %,
  and §25.6.6 carries it at L7106. The two agree.

---

## Instrument faults, self-caught, all rewritten rather than trimmed

Seven this chat; the class is unchanged from chats 92 and 93 and now has two new forms.

1. **H4, H5, H12 — verdicts contradicting their own printed numbers.** Three summary lines
   asserted the opposite of the rows above them. H5 printed *DOES NOT reproduce* on one row and
   then *All three error entries reproduce*; H12 measured three shared digits and then wrote that
   the four-figure claim was *true* of that pair. Both were caught by re-reading each comparison
   against its numbers, which is chat 93's carried rule doing its work.
2. **H4, H6, H8 — Python's `round()` is binary and unreliable on .5 boundaries.** `round(17.25, 1)`
   returns 17.2 and `round(2.15, 1)` returns 2.1, neither of which is the decimal answer. Every
   rounding in the batch now goes through `Decimal.quantize` with the convention named. This is
   what turned C1 from a wrong verdict into a correct one.
3. **H11 measured something §22.4 does not claim.** It tested δ₀ cancellation on w and e built from
   *T*, where δ₀ does not cancel, and would have recorded a deviation. The section's subject is
   bracketing δ (L6140). Rewritten to test the claim as the section words it: it holds exactly.
4. **H3 asserted a sign disagreement on a reading the text does not use.** *Asymmetry* means loose
   end against tight end, and on that reading the signs agree. The instrument now prints both
   readings and confines the verdict to magnitude.
5. **I1's `section_span` truncated §25.6 at its own first subsection.** The book sets §25.6 and
   §25.6.1 at the same `###` depth, so a rank rule ends the parent at L7002 and three pointers were
   reported as failing that this chat had already measured as resolving from the file. Span is now
   taken by dotted-number extension, compared component-wise so 25.61 is not read as a child of
   25.6.
6. **I1/I2 matched `gain` inside `against`** and returned *RESOLVES* for the §32.3 pointer — chat
   92's substring class exactly. All token tests are now word-bounded.
7. **I4's enclosing-heading resolver matched numbered headings only**, so it labelled App A.12,
   App C.2 and App F.4.3 as §36.6. Now appendix-aware.

Fault 5 is the one to carry: **an instrument that contradicts a measurement already taken from the
file is wrong until proved otherwise.** In both 5 and 6 the file had already been read by hand and
the hand reading was right.
