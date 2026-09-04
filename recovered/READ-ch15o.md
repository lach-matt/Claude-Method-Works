# READ-ch15o — chat 115 — main L8238–L8346 (§29.12, `## 30.` head, §30.1)

Unit cut in chat 115 from a heading scan taken this session: §29.12 L8238, `## 30.` L8316,
§30.1 L8321, §30.2 L8347. The cut runs **L8238–L8346, 109 lines** — it closes chapter 29 and
takes §30.1 entire, stopping one line short of §30.2 so that §30.2.1–§30.2.3 are not orphaned
from their parent. §28.10 (L8222, read in chat 111) is stepped over. Every heading resolved to
its **body** occurrence; the contents entries at L150–L152 name chapters only.

Instruments: `r2-ch15x` (computable, 79 lines banked), `r2-ch15y` (prose, 188 lines banked).

---

## A — Deviations

**15o-01 — the heading's count word fails against its own body.** L8238 prints *Five unlocated
results, defined, with the test that would settle each*. The body prints five U-blocks
(L8245, L8266, L8277, L8288, L8301), of which **U1 is marked LOCATED** in its own headline
(L8245: *U1 — E(X) as a defect measure. **LOCATED**, and the test that found it was the one
printed here*), leaving **four** unlocated. The opening sentence takes the same damage:
L8239–L8240 calls the list *statements this work computed, for which these searches returned no
source*, and U1 names its source — Kimura, Makino, Yamada and Yoshizumi, 2024, and the property
*2-decomposability*. U1 does narrow what remains unlocated to **the count** (E as a graded
measure rather than the predicate), so the entry is defensible; the **heading and the framing
sentence are not**. R3 either restates the heading to four, or re-frames the list as *five
results, one since located*. Docket 21 / 31 — the count-word class, which has now fired in
seven of ten units.

**15o-02 — U4 carries no *Test.*, against the universal the section opens with.** L8241–L8243:
*Each carries a definition, the search already run, the test that would confirm it, and the
observation that would destroy it.* MEASURED over the five blocks: definition **5/5**, search
**5/5**, falsifier **5/5**, test **4/5**. U4 (L8288–L8299) prints *Definition · Searched ·
Proved · Falsifier* and no test. The second universal at L8243 — *a result with no stated
falsifier is not on this list* — **holds**, 5/5. R3 supplies U4's test or narrows L8242.
Docket 19 / 21.

**15o-03 — *a twenty-three-fold rise* is a magnitude read as a ratio.** L8341, against the
section's own table at L8336–L8339. MEASURED with `Decimal.quantize`, ROUND_HALF_UP:
23.40 / 1.05 = **22.29**, 23.40 / 6.90 = 3.39, and the 0.50–1.00 bucket is 0.00, which yields
no ratio at all. No baseline in the table produces twenty-three. *Twenty-three* is the value
23.40 itself — a mean backtrack count, not a multiple. R3 prints *twenty-two-fold* against the
0.20–0.50 bucket or restates the sentence as a magnitude. Docket 34.

**15o-04 — *The earlier figure of 139* has no antecedent anywhere in the six volumes.** L8329.
MEASURED, digit-bounded, all six volumes: 139 has **14 sites**. Every one is something else —
the seed compression *139 to 1* (main L3775, L3935; mc L96, L119, L724), the register range
*123–139* (main L7619), a Register heading (reg L627), a table cell (ioi L519), and figures in
reg L1733/L1885/L2397/L6062 and main L11419. **No site prints 139 as a count of reorderable
instances.** The sentence corrects a figure the reader has never been shown. Docket 15
(narrated past state) and docket 10 (unprinted input).

**15o-05 — four process / past-state remarks.** L8329 *The earlier figure of 139*, L8330 *the
instances were re-drawn*, L8311 *the three exact sets §12.11.1 **now states***, L8293 *the proof
corrects **the guess that preceded it***. Docket 5 (Ruling 45) with docket 15. Reported apart
from **nine** further phrases in the unit — L8245, L8274, L8283, L8310, L8319, L8239, L8298,
L8313, L8243 — which are plain self-reference to the book's own subject matter and are **not**
Ruling 45 sites; a flat sweep would overstate the class by more than a factor of three.

---

## B — Verified, so R3 does not re-derive

1. **U3, the E1 puncture, exact.** T = {(2J,2J′) : |2J−2J′| ≤ 2} is closed under componentwise
   max and min at every cap 4–24 (0 join leaks, 0 meet leaks). T ∖ {(0,0)} fails meet-closure
   by **exactly four unordered pairs at every cap tested, and all four meets are (0,0)** —
   (0,1)∧(1,0), (0,1)∧(2,0), (0,2)∧(1,0), (0,2)∧(2,0). The count is **cap-independent**, so
   L8283's *confirm the count stays four* beyond 20 is confirmed to 24.
2. **U4's failing meets, all four exact.** Caps 6/8/10/12 → **2,862 / 12,489 / 40,887 /
   110,229**, on the unordered-pair convention (ordered is twice each; the denominator is
   named, not assumed).
3. **U4's lower/upper split, all six exact.** Caps 8/12/16 → **8,326 / 4,163 · 73,486 / 36,743
   · 363,384 / 181,692**, ratio exactly **2.00** at every cap including 6 and 10, and **no meet
   fails both bounds** (both = 0) — which is why the split sums to the total.
4. **U4's join closure holds.** 0 join failures at caps 6, 8, 10, 12 and 16; the falsifier
   L8299 states is not met at any cap tested.
5. **U4's cell counts.** 369 / 1,105 / 2,465 = caps 8 / 12 / 16 exactly.
6. **Both witness meets are as printed.** (0,1,1) ∧ (1,0,1) = (0,0,1) fails the **upper**
   bound; (4,0,4) ∧ (2,2,0) = (2,0,0) fails the **lower**.
7. **The parity congruence breaks join**, as L8291 says: 1,848 / 7,650 / 24,090 / 63,063 join
   failures at caps 6/8/10/12.
8. **U1's non-negativity.** X ⊆ ℛ(X) on all five test sets and E ≥ 0 throughout; E is **graded**
   (0, 168, 736, 817, 840), which is the property U1 says the literature's predicate lacks.
9. **L8312's seventh figure is legitimate.** 1,561 = **Λ₉′** = Λ₉ ∩ {2S′ ≤ 2f+1}, rebuilt here
   from `r2lib.lam9p(build9((3,3,1,3,1)))`; the other six are the core gate's tower. The list is
   printed in **tower order, not numeric order** — 1,561 following 1,654 is correct, not a
   transposition. Λ₉′ has four further sites (main L2938, L3035, L3097, L3100).
10. **All seven §-pointers resolve and carry their claim**, under `body_range` **and**
    `section_span`, heading line excluded. §29.1, §29.10, §7.1 and §7.4 **COINCIDE** under both
    resolvers; §12.11.1, §30.2 and §18.4 **DIFFER** and carry under both. A.18's heading is
    lettered, so `heading_line` returns None; the line window finds it at **L10073 — *The
    triangle region is join-closed and meet-broken***, which is exactly what L8293 cites it for.
11. **Every attribution in the unit is bibliographed.** MEASURED against `## References`
    **L11503–L11855** (body occurrence; the L173 hit is the contents entry) and against **R.7
    L11806–L11855**: Kimura, Makino, Yamada and Yoshizumi all at L11561; Helly at L11767;
    *row-convex* ×3 and *2-decomposab\** ×3 inside References. **Docket 36's first entirely
    clean unit** — recorded so the class is not made to look worse than the book is.
12. **L8310's *nothing else* holds.** The three sections it names carry what the entry test
    needs, including the Λ₉′ constraint: §12.11.1 prints `2f+1` three times inside its own span.
13. **§30.1's tree premise holds.** Λ₈ = 8 coordinates, 7 constraints, tree **True**; Λ₉ = 9
    and 8, **True**. g carries two parents (f and q) and the graph is still acyclic — the
    *tight two-parent form* U5 says destroys the factorisation (L8303). Chapter 15's span
    (L4270–L4331) carries *recover* ×8, *order* ×13, *tree* ×5.
14. **L8296's universal is true.** *At every cap tested the lower bound fails exactly twice as
    often as the upper* — measured 2.00 exactly at all five caps.
15. **Zero first-person pronouns. Duplicated-passage sweep 0 of 75 long lines** — the ninth
    consecutive clean unit (chats 106–115: 0 of 71, 55, 32, 44, 70, 38, 51, 76, 75).

---

## C — Incidental

1. **Census row 1179** (main L8303, C9-OVERGENERALISATION-WORD, token *at every cap*) — the
   flagged token is the section's own scope statement about a computation it reports, the C7/C9
   regex-artefact precedent. **Not a defect.** Witnesses **1178 (L8231)** and **1180 (L8553)**
   are contiguous either side, so no row in range was missed.
2. **Nine single-witness figures** — 8,326 · 4,163 · 73,486 · 36,743 · 363,384 · 181,692 ·
   2,465 · 23.40 · 6.90 each have exactly one site in six volumes. All nine are **recomputed
   exactly** here, so they are verified rather than unverifiable; docket 17 should keep the two
   states apart when it reports.
3. **L8325 *Complete under a targeted attack.*** is a sentence fragment standing as a paragraph
   head inside body prose — docket 18's shape one level down.
4. **Zero Ruling 46 sites.** The apparent `BUILD` hit at L8311 is *rebuilds*.
5. **L8281 *Selection rules are universally known*** is a universal about the literature, not
   about the book, and is **unmeasurable** rather than refuted — docket 19's rule.
6. **U5 is scoped narrowly by the book itself** (L8304: *least likely to be general — it is a
   property of one constructed object*), which is the correct treatment and worth keeping as a
   positive witness against the false-universal class.

---

## Instrument faults — three, all self-caught, rewritten in place, none trimmed

1. **`## References` resolved to the contents entry.** The first `## References` is L173; the
   body is **L11503**. Taking the first would have reported all four of the unit's attributions
   unbibliographed — **false for every one of them**. Same shape as chat 114's Appendix F fault:
   the book was right and the instrument wrong.
2. **`BUILD` matched *rebuilds*** at L8311 under a case-insensitive phrase test. The Ruling 46
   test is now word-bounded and case-sensitive; the unit has **zero** Ruling 46 sites.
3. A mangled f-string in the count-word verdict raised `KeyError` before printing.

Instrument wrong before the book: **twice** this chat, against once in 114, once in 113, zero
in 112, three in 111, five in 110.
