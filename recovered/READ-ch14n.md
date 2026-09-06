# READ-ch14n — Chapter 23, §23.10 to §23.11.2 (main member L6434–L6548)

Chat 97. 115 lines, eight headings (L6434, 6438, 6452, 6486, 6500, 6519, 6533, 6543), boundaries
re-scanned on `The_Method_1_6-2.md` this chat. Instruments: `r2-ch14n` (computable, golden
5,540 B · 0259aeae · 49 lines) and `r2-ch14o` (prose, 9,247 B · 9923bc2d · 89 lines). Every figure
below is MEASURED by one of the two unless marked INFERRED. R = 109737.31568, the only Rydberg
constant either bundle prints. Rounding is `Decimal.quantize` ROUND_HALF_UP throughout; exact
rationals converted numerator/denominator.

## A. Deviations

**14n-A1 — L6501's pointer names the one section that carries neither of its two objects, and the
right section is measured.** Printed: *§23.13 gives r ≥ 5 for the spacing and ν_V for the
curvature.* §23.13 is "Inversion" (L6569–L6581) and carries **ν_V 0, curvature 0, spacing 0,
admissible 0**, and the literal `r ≥ 5` **0** times. Both objects live at **L6585, §23.14** — the
only other `r ≥ 5` site in the volume (the third is Phys L573). Repair: retarget to §23.14.

**14n-A2 — the ν_V ceiling is cited to §23.11 twice, and §23.11 does not carry it.** Closes chat
95's 14k-01 on the §23.11 side. All fifteen main-volume ν_V sites, resolved: §2.3 (L580, L582),
§23.3 (L6235), §23.4.2 (L6270), §23.10.4 (L6501), §23.14 (L6585), §23.14.1 (L6600), §23.15 (L6607,
6609, 6613, 6621), §25.2 (L6923), §29.8 (L8087), App C.4 (L10312), App F.4.3 (L11448). §23.11
(L6519–L6548) carries ν_V, ceiling, granularity, quotation, curvature and resolve **zero times
each**, word-bounded; §23.10.4 carries ν_V 1, quotation 1, curvature 1, unresolved 1. The two
citing sites are **L6270** (§23.4.2: *Al I at n = 51 and Ga I at n = 53 both sit above the ν_V
ceiling of §23.11, where quotation granularity destroys the second difference*) and **L6923**
(§25.2: *curvature too fine to resolve (ν > ν_V, §23.11)*). §23.15 carries four ν_V sites and is
the target; §23.10.4 is the nearer one. The index at L11448 already reads §2.3 · §23.14 · §23.15
and is correct. **The Ga I half of the docket stays open for chat 98**, which reads §23.15.

**14n-A3 — two sites cite Register entries that carry no such correction.** L6455: *the correction
is recorded at 96–98.* L6484 (figure caption): *is withdrawn at correction 97.* MEASURED in the
Register member: **96 at L455, 97 at L459, 98 at L463 are each the single line "SUPERSEDED (Λ₈
successor development); see register 313"**, and Register 313 (L1163) is *TIME MUST NOT ENTER Λ
WAS A MISSTATEMENT*, about iteration in Λ₉. Searched the whole Register for the correction the two
sites describe: **"V = 2" 0 sites, "Figure 23.3" 0 sites, "matched order" 0 sites.** The Register
is append-only, so this is a missing entry, not a wrong one — the same shape as the §18.4.1 item.

**14n-A4 — "1,585-fold" is not the quotient of the two figures it stands between.** L6514 prints
*the bound tightens 1,585-fold* under a table whose median bounds are 25.96 (order 1) and 0.0164
(order 6). MEASURED 25.96 / 0.0164 = **1582.9268**, 1583 to the nearest integer; the printed figure
is high by 2.0732. Restated with the same pair at **App E.2 L11037–L11038**, so the class has two
sites.

**14n-A5 — the "held" column repeats the "admitted" column in every row.** L6507–L6511: order 1
499/499, order 3 187/187, order 6 34/34. The prose distinguishes three outcomes (admitted;
*unresolved* below the quotation floor; *refused* on a wrong sign), so three columns are owed and
two are identical. The three columns do not partition a fixed collection either — the rows sum to
1,017, 475 and 213 — which is expected as the node demand rises with order, and is not itself the
defect.

**14n-A6 — "619 refusals" matches nothing in the table above it.** L6517. The section's own refusal
column is 19, 101, 145, summing **265**; 619 is no entry and no sum of entries. Second unsourced
figure in the same sentence as A7.

**14n-A7 — "§25.5's 1,061 order-1 bounds" is not in §25.5.** MEASURED: §25.5 is L6962–L6990 and
carries "1,061" **0** times, "499" 0 times, and *order-1 / order 1* 0 times. The figure sits at
**L6958, §25.4**, four lines above the section named. Separately, the same sentence sets 1,061
order-1 bounds against this table's **499** admitted at order 1 — two order-1 counts of one
collection, differing by 562, with no reconciliation printed.

**14n-A8 — the heading counts verdicts and gets the pattern count.** L6519 *The refusal pattern
carries four verdicts, not one*; L6521 *the count is one number; the PATTERN is four.* MEASURED on
the table at L6523–L6529: **5 rows, 4 distinct refusal patterns** (none; one; regularly spaced;
dense and irregular) **and 5 distinct verdicts** (exact; a smooth channel; a bifurcation; an
oscillation; chaotic). The prose sentence is right and the heading is wrong: *none* splits into two
verdicts by V. Repair is one word in the heading.

**14n-A9 — §23.11.1 returns a verdict the classifier does not offer.** L6539 gives Li I np the
verdict *repeated structure*; the five verdicts are exact / a smooth channel / a bifurcation / an
oscillation / chaotic. Six irregular refusals should read *chaotic* under the table's own
dense-and-irregular row, or the table owes a sixth row. "repeated structure" occurs **once in all
six volumes** (main L6539), so it is not vocabulary established elsewhere.

**14n-A10 — L6497 prints the asymptote as an equality.** *V = 4ν/3 is the price of certainty.*
MEASURED against the book's own exact V = 4r³/(3r²−1): ν = 10 gives 13.377926 against 13.333333
(0.3333 %), ν = 40 gives 53.344447 against 53.333333 (0.0208 %), ν = 100 gives 133.337778 against
133.333333 (0.0033 %). New site of chat 96's truncation-printed-as-equality class (14l-02, 14l-03).

**14n-A11 — the operative rule of §23.10.1 is printed with its sentence break missing.** L6443,
verbatim: `sign( f(n) − p(n) ) = (−1)^(k+1) · (−1)^m, with m nodes above n k+1+m even → a lower
bound.` Two sentences run together at *above n k+1+m even*, and *Odd → an upper bound* on the next
line is left without a subject. The rule is correct as reconstructed (see B2) — the defect is
production, in the one display the section turns on.

**14n-A12 — Ruling 45 class, three sites, one of them a figure caption.** L6453 *An earlier draft
claimed…*; L6483–L6484 *An earlier version of this figure drew a floor at V = 2 through data
reaching 0.24, and is withdrawn at correction 97.* Captions state facts only; the book's own draft
history is not a fact about the figure. Repairing A3 and A12 together is the economical order.

**14n-A13 — the displacement row's definition is nowhere printed (unprinted-input class, ninth
member).** L6492's row reproduces exactly once the definition is supplied — see B4 — but the text
gives neither the definition nor the node set. Joins the eight members carried in DEFERRED.

**14n-A14 — three costs named, two witnessed.** L6495: *Higher order buys absolute precision and
pays in robustness, domain and resolution.* The table above (L6489–L6493) carries three rows:
bracket width (the precision bought), displacement tolerated (robustness), cells from a 10-member
channel (resolution). **Domain has no row**, and *domain* occurs once in §23.10.3 — in that
sentence. Either the claim drops a word or the table owes a row.

## B. Verified

**B1 — the sign rule.** L6439's *every derivative has known sign, sign(f^(j)) = (−1)^j* for
T = Z²R/ν²: EXACT at j = 0…6 and ν = 8, 40, 119, zero exceptions (f^(j) = (−1)^j (j+1)! Z²R ν^−(2+j)).

**B2 — 560 containments, zero failures.** L6446–L6448. MEASURED over ν = 8…119 and k = 1…5 in exact
rational arithmetic, Lagrange interpolants on nearest nodes: **560 target–order pairs, 560
containments, 0 failures**, and every choice of m obeying the parity rule bounds on the side the
rule states. The printed count is also the arithmetic of the sweep: (119 − 8 + 1) × 5 = 560.

**B3 — both printed widths reproduce.** L6450 and L6491 agree with each other and with the
bracket built from the section's own sign rule on nearest nodes at ν = 40: order 1 = **0.3620**
→ 0.362, order 5 = **8.9350 × 10⁻⁶** → 8.9 × 10⁻⁶.

**B4 — both displacement figures reproduce as the distance to the nearer bracket end.** Order 1
**0.128732** → 0.129; order 5 **4.2675 × 10⁻⁶** → 4.3 × 10⁻⁶. Half the width would be 0.180986 and
4.4675 × 10⁻⁶, which is neither. The classical order-1 error term 3R/ν⁴ = 0.128598 also rounds to
0.129, a coincidence at order 1 only: the order-5 classical term is 4.2196 × 10⁻⁶ → 4.2 × 10⁻⁶.

**B5 — 8 and 4 cells from a 10-member channel.** L6493. A two-sided bracket at order k spends k+1
nodes off the target: 10 − 2 = 8 at order 1, 10 − 6 = 4 at order 5.

**B6 — the refusal percentages.** L6514's *3.7 % to 81 %*: refused/(admitted+refused) = 3.7 % at
order 1 and 81.0 % at order 6. Order 3, unprinted, is 35.1 %.

**B7 — V grows with order.** L6467. Monotone in k across every printed row of L6459–L6465, and
(not claimed, measured) monotone in ν at fixed k.

**B8 — the Figure 23.3 caption's endpoints.** L6481's *from 157 to 3.2 × 10⁶* are the table's own
min and max, ratio 20,382.2, drawn from two different rows (ν = 20 k = 1; ν = 40 k = 5).

**B9 — the logistic-map witness.** L6546. At r = 2.5 the orbit converges to 1 − 1/r = 0.6
(measured 0.600000000000000); residual first differences are float noise of size 1.110 × 10⁻¹⁶ and
change sign 11 times in 11 steps, which an exact-zero test reads as a periodic signal. The caution
reproduces.

**B10 — the admissibility rule is one rule.** L6503's |Δ^(k+1)T| > 5·2^(k+1)·σ carries noise factor
2^(k+1) = 4, 16, 128 at k = 1, 3, 6, so it is r > 5 with r = |Δ^(k+1)T| / (2^(k+1)σ) — the two
instances L6501 claims, k-indexed. The rule is sound; only its pointer (A1) fails.

**B11 — L6531's §16.7.1 pointer resolves to a claim of the right shape.** §16.7.1 is *A missing
cell — and the index can tell whether the gap is real* (L4578–L4617); its claim lines are L4585
*the index distinguishes them, by asking whether E is removable* and L4593. A structure-level
question, as L6531 says.

**B12 — L6477's scope restriction matches the proposition as stated.** Proposition 23.1
(L6199–L6204) is built on three consecutive cells at equally spaced index and *two-point linear
interpolation from the same neighbours* — first order by construction. L6477's *applies to the
classical bracket only* is a correct reading, not a new restriction. Prop 23.1 is cited at L6199,
6477, 7273, 7583, 10243, 10280, 11044.

**B13 — Ga I's row obeys the classifier.** L6538 gives Ga I 4s²np ²P° 15 members, 1 refusal,
*a bifurcation*, which is the table's one-refusal row.

**B14 — chapter figures.** Figures 23.1, 23.2, 23.3 and 23.4 are named in the main volume; the
Figure 23.3 asset line is L6479.

## C. Incidental

**C1** — words broken across lines inside two space-aligned tables: L6528–L6529 *undefine / d*,
L6535–L6536 *membe / rs*. Production.

**C2** — mixed table conventions inside 115 lines: 10 pipe-table lines against three space-aligned
blocks (L6459–L6465, L6523–L6529, L6535–L6539). New sites of chat 96's 14m-13; the count is owed at
press, not at source (G0w).

**C3** — the ν = 80 row of L6465 carries "—" at k = 4 and k = 5 with no note saying why.

**C4** — the median-bound column gives its unit once (cm⁻¹ at order 1); 0.715 and 0.0164 are bare.

**C5** — 0.6779 (L6541) is corroborated, not single-witness: Register L2549, L3177, L6543 and
Spectra L609.

**C6** — `r2lib.heading_line` requires a trailing space after the number, and the Register sets its
entries as a bare `### 96`, so it returns None there. Located directly in this batch; owed to the
r2lib docket.

**C7** — Q9 exists as a named object, at L6453 and L7589 only.

**C8** — the local spacing at ν = 40 is 3.3048 cm⁻¹ and half of it is 1.6524, against L6492's 0.129
(7.78 % of half the spacing). L6497's *survives a perturbation of half the local spacing* and
L6492's displacement row are different quantities on the page; recorded as measured, not as a
contradiction.

**C9 — single-witness class.** Fourteen figures in these 115 lines are printed once and nowhere
corroborated: the five ν = 20 V values, the three ν = 80 values, 0.129, 4.3 × 10⁻⁶, 187, 101, 34,
145. Chat 96 counted seventeen in 131 lines, chat 95 thirteen in 125.

## Instrument faults, self-caught and rewritten (eleven)

The three to carry: (1) **a verdict must be re-read against the numbers printed below it** —
14n-05 asserted 4.3 × 10⁻⁶ did not reproduce while the nearer-end distance printed two lines below
reproduced it exactly; chat 96's class in new dress. (2) **A sign convention is not a magnitude** —
the order-1 error term was carried as −0.128598 and reported as reproducing 0.129, which poisoned
two downstream ratios. (3) **A token count cannot settle a pointer** — §16.7.1 was first tested by
counting *whole*, *structure*, *cell*, *pair* and had to be re-run against the section's own claim
lines. Also: a stray trailing comma left a format string unformatted and printed `%s` as a verdict;
two citing sites were truncated at 150 characters, before the evidence they carry; and
`heading_line` returned None on Register headings for a reason that had to be read, not guessed.
