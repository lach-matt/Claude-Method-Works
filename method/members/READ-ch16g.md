# READ-ch16g — chat 118 — main L8575–L8699 (§30.4 – §31.2.5)

Unit: **§30.4, §30.4.1, §30.4.2 (closing chapter 30), chapter 31 head, §31.1, §31.1.1, §31.1.2,
§31.2, §31.2.1 – §31.2.5** — 125 member lines. Cut chosen over HANDOFF-70's proposed 84-line cut
because the 84-line cut ends inside chapter 31's string movement; this one closes chapter 30 and
the whole of §31.1 and §31.2, leaving §31.3 to open clean.

Instruments: `r2-ch16e` (computable, 9,894 B · d816d8ea · 145 lines) and `r2-ch16f` (prose,
30,925 B · 969b3a10 · 343 lines). Both banked. Every figure below measured in this chat from the
members; nothing carried from HANDOFF-70.

---

## A — DEVIATIONS

**16g-01 — §30.4 derives a consequence its own printed relation set does not entail.**
L8577–L8578 print: *From {V = 4ν/3h, λ² = (2/3)T, w·V = 8λ², T = Z²R/ν²} the closure yields
w/T = 4(h/ν), e/T = 3(h/ν)²…*. MEASURED by ideal membership (sympy, lex order, nine variables):

| tested | in the ideal of the four? |
|---|---|
| w·ν − 4Th  (i.e. w/T = 4h/ν) | **True** |
| V·e − w | **False** |
| e·ν² − 3Th² (i.e. e/T = 3(h/ν)²) | **False** |

The symbol *e* does not occur in the four printed relations. `e/T = 3(h/ν)²` follows only once
`V·e = w` is added — and §30.4.1 at L8586, nine lines later, lists `V·e = w` among the relations
that *reduce to zero that did not before*. The two sections cannot both stand: either §30.4's
list is short by the relation `w = V·e` (printed at L4349), or §30.4.1 is wrong that `V·e = w` is
new. Both consequences are true under `e = w/V`; the defect is in the entailment claim, not the
algebra. **Docket 12 (an assertion that is not a derivation), docket 34.**
*Candidate repair:* add `w = V·e` to §30.4's printed set and strike `V·e = w` from §30.4.1's
list of newly-reducing relations, which then names six, not seven.

**16g-02 — *at least nine* over an enumeration of eight (L8588–L8591).**
The colon at L8588 opens the enumeration; MEASURED items: `A^m(x^p) = (−1)^m x^p/(p−1)^m`,
`V = 2/tanh(kh/2)`, self-concordance, the modular rank law, `Σ_q‖A_q‖·‖B_q‖ = |Λ|`, `F(−1) = 2`,
`E(X)` as non-pairwise content, the reorderability theorem — **eight**. The same *nine
non-polynomial* is printed a second time at §30.4.2 L8600 and a third at main **L7636**, and no
site anywhere enumerates nine. **Docket 21, docket 10.**

**16g-03 — *This chapter contains five enumerations* where three of the five rows are in the next
chapter (L8597–L8604).** MEASURED: the sentence sits in §30.4.2, `enclosing` = 30.4.2, chapter 30
spans L8316–L8608. The table's five rows cite §30.4 and §30.2 (inside chapter 30) and **§31.1
(L8614), §31.2 (L8659) and §31.3 (L8700) — all inside chapter 31**. This is docket 21's 15h-12
item, and the same claim is printed a second time at **main L7641** (*Five lists in one chapter*),
byte-present in Prints & Proofs at **P7564** — so it is authoring, not production, at both sites.
*Candidate repair:* *this part* rather than *this chapter*, at both sites; Part VII contains both
chapters.

**16g-04 — the fifth row is not a member of the class its own column names (L8604).**
Column header is *what it omitted*; the row reads *§31.3's statistic — stated against the wrong
denominator*. A wrong denominator is not an omission. Same shape as chat 117's 16d-04 and chat
115's *five unlocated results*. **Docket 21.**

**16g-05 — a sign pattern that fails on the second of the two subjects it names (L8646–L8647).**
Printed: *L1 and L3 alternate −, +, −, +; L2 alternates +, −, +, −*. MEASURED on the grid
μ = 0.01…0.08, step 0.01, by difference order:

| point | d¹ | d² | d³ | d⁴ | pattern |
|---|---|---|---|---|---|
| L1 | − | + | − | + | **−, +, −, + — exact** |
| L2 | + | − | + | − | **+, −, +, − — exact** |
| L3 | − | + | **+** | + | **−, +, +, + — breaks at the third difference** |

L3's third differences are positive at every window measured (3.46 × 10⁻⁷ to 3.82 × 10⁻⁷), never
negative. The sentence's own next clause — *assuming the Rydberg pattern produces bounds that
cross* — is the reason the alternation matters, so the error is load-bearing. **Docket 21,
docket 19.**

**16g-06 — *where Titius–Bode fails worst* is false (L8630–L8631).**
The row reads *monotone, not convex — the third difference changes sign between Jupiter and
Saturn, where Titius–Bode fails worst*. MEASURED Titius–Bode errors on the standard slots:
Mercury 3.36 %, Venus 3.18 %, Earth 0.00 %, Mars 4.99 %, Ceres 1.23 %, **Jupiter 0.06 %**,
**Saturn 4.85 %**, Uranus 2.13 %, **Neptune 29.04 %**. The law fails worst at **Neptune**, by a
factor of six over Saturn; Jupiter is its single best fit. MEASURED separately, the third
difference of the semi-major axes changes sign **three** times (entering Saturn, Uranus and
Neptune), so *changes sign between Jupiter and Saturn* is true but not the definite event the
sentence makes it. **Docket 19, docket 21.**

**16g-07 — two table figures reproducible from no grid the section prints (L8628–L8629).**
The Hill-radius row prints V = 47.9 and the Roche row V = 17.9. V is defined at §23.10 L6203 as
w/e with w = d₀ + d₁ and e = |d₀ − d₁|/2. MEASURED at **the grid this section itself prints**
(x = 0.030, h = 0.010, from L8635): Hill (μ/3)^{1/3} → **V = 17.6**; Roche ρ^{−1/3} → **V = 8.9**.
Under §23.9.2 L6388's closed form V ≈ 4x/(h|p−1|), the printed 47.9 needs x/h = 7.98 on the Hill
row and the printed 17.9 needs x/h = 5.97 on the Roche row — two different, unprinted grids.
**The value the Hill row would take on the section's own grid, 17.6, is the value printed on the
Roche row.** Recorded as measured, without asserting a transposition. **Docket 10, docket 17.**

**16g-08 — a correction announced against a section that carries no notice of it and no Register
entry (L8639).** *Which corrects §18.5.* §18.5 read in full (L5294–L5302): it prices a guarantee
at a pole as costing *infinitely more than the thing it guarantees* and states *The method has no
domain at p = 1*. The correcting claim is therefore faithful — §18.5 does hold the position being
corrected. But MEASURED: §18.5's body carries **zero** forward notices, and **no Register line
names §18.5 at all**. Nine lines later, §31.2.2's convex→concave correction of its own earlier
text **is** recorded, at register 1787, exact and on point. Two corrections in one chapter, one
registered and one not. **Docket 23, docket 2/3 (a correction with no Register entry).**

**16g-09 — three count words with no enumeration behind them (L8584–L8585, L8623).**
*the eight polynomial relations the book now states* — MEASURED: `eight polynomial` has **one
site in six volumes**, this one; the eight are nowhere listed. *a Gröbner basis of 18* — the
eight being unlisted, 18 is uncheckable; the companion figure **6 for the original four is EXACT**
(measured below). *18 of 18 containments at orders 1–3* — the containment convention (which
brackets, which orders, ordered or unordered) is printed nowhere; 3 points × 3 orders = 9, and no
printed convention doubles it. **Docket 10.**

**16g-10 — order-3 bracket widths not reproducible (L8625).**
*widths 6.9 × 10⁻⁴ (L1), 3.6 × 10⁻⁹ (L3)*. MEASURED third-difference spans on the section's own
μ-grid: L1 3.55 × 10⁻⁴ … 5.70 × 10⁻³, L3 3.46 × 10⁻⁷ … 3.82 × 10⁻⁷. The L1 figure is inside the
measured range but not equal to any window; **the L3 figure is two orders of magnitude below the
smallest measured value**. Neither the grid nor the width convention is printed. `6.9` and `3.6`
each have zero main-volume sites outside this unit. **Docket 10, docket 17.**

---

## B — VERIFIED, EXACT

1. **The Gröbner basis of the original four is 6** — MEASURED, lex order, eight variables
   (V, λ, w, T, Z, R, ν, h): basis size **6**, matching L8585 exactly. Convention named because
   grevlex on the same four gives 5.
2. **w/T = 4(h/ν)** — exact on four independent rational instances and by ideal membership.
3. **Routh's threshold.** *L4/L5 are linearly stable for μ < 0.0385209* — MEASURED
   (9 − √69)/18 = **0.0385208965**, agreeing at the printed seven decimals. Earth–Moon 0.0121443
   and Sun–Jupiter 0.0009537 both qualify. The same figure is printed at main L9918 and pc L332,
   consistent.
4. **V at the collinear points.** MEASURED at μ = 0.030, h = 0.010: **L1 24.6, L2 12.4,
   L3 16,422.8 → 16,423**. All three printed values exact. L3's magnitude is explained by the
   printed reason: its second difference is 5.07 × 10⁻⁷ against a width of 8.33 × 10⁻³.
5. **L4/L5 sit on the pole exactly** — (1/2 − μ, ±√3/2), the first linear and the second
   constant, both with second difference identically zero.
6. **The nucleon index closes.** (N, L, 2j, occ) with occ ≤ 2j+1, 384 cells: **zero join leaks,
   zero meet leaks over 73,536 pairs, E(X) = 0** measured with `Rset`, not by re-applying the
   defining filter. Shell-order filling gives cumulative 2, 6, 8, 14, 16, 20, 28, 32, 38, 40, 50,
   58, 64, 68, 70, 82 — **all six printed magic numbers present**.
7. **Three objects on the pole.** In exact rational arithmetic all three have second difference
   identically 0 and V = ∞: m² linear in N, the Regge trajectory, and c = D.
8. **The string degeneracy, four figures.** d(N) from ∏(1 − qⁿ)^{−24}: first differences positive,
   second negative, third positive throughout N = 1…40. Second difference **−0.3125 at N = 2**
   (printed −0.31) and **−0.0324 at N = 15** (printed −0.03); **V = 146.6 at N = 14** (printed
   ≈ 147). Every figure in §31.2.2 reproduces at the source's precision.
9. **Λ closes at every dimension 2–8 with E = 0** — MEASURED sizes 5, 12, 33, 99, 165, 319, 976;
   |ℛ(Λ_d)| = |Λ_d| at every d; zero join and zero meet leaks at every d.
10. **The projection ladder is exact and onto, with fibres 1 to 4** — measured fibre sizes
    {2,3}, {2,3,4}, {3}, {1,2}, {1,2,3,4}, {2,3,4} at d = 2…7, every projection surjective.
    *fibres of 1 to 4 preimages* is exact.
11. **The rank sequence.** 976 cells over ranks 3–20: 1, 5, 15, 34, 59, 87, 108, 121, **122**,
    115, 100, 79, 57, 37, 21, 10, 4, 1 — **peak 122 at rank 11, exact**, and log-concave at every
    interior rank with zero failures.
12. **The Sperner claim holds.** MEASURED by Dilworth on 115,162 comparable pairs: maximum
    matching 854, minimum chain cover 976 − 854 = **122 = the largest rank**. Λ₈ is Sperner.
13. **§2.10 is quoted correctly.** L8606 says *§2.10 reads enumerate targets before searching*;
    §2.10 L623 reads *Enumerate targets from the index before searching.*
14. **Three pointers that hold, read in full rather than probed.** §18.5 carries the position
    §31.1.1 corrects (see 16g-08 for the separate defect); **§16.7.1 carries the 7/8 cut** —
    *every resonance of order ≤ 7 in the belt is occupied; every one of order ≥ 8 is empty*, with
    the index inferring it from the cells alone; **§11.7 carries three facts**, and the count word
    *three* is exact.
15. **Chapter 36 keeps §31.1.1's promise.** L8648 promises the families are indexed, the index
    closes, and the closure is why nothing touches Poincaré. MEASURED at the body occurrence
    L9892–L9938: L9898 quotes the very sentence, L9906 supplies *a complete index has E = 0*, and
    L9916 supplies the five points from §14.5's seed. The pointer resolves under both resolvers.
16. **Register 1787 is exact and on point** — headline: *§31.2.2 called log d(N) convex; its
    second differences are negative at every level computed…*, matching L8676–L8678 exactly.
17. **Zero duplicated sections** — 67 long lines of the unit swept against all six volumes,
    **0 recur**. Twelve consecutive clean units (chats 106–118).
18. **Zero Ruling 46 sites and zero first-person pronouns** in the unit, tested case-sensitively
    and word-bounded. Chats 112–118: zero.

---

## C — INCIDENTALS

1. **The §31.2 heading finishes in the body** — L8659 *String theory — the pole, the generating
   function, and a* / L8660 *disanalogy*. Already docket 18's known member; confirmed in place.
2. **Prints & Proofs offsets vary across this unit** — −82 at L8576, L8583, L8597, L8610, L8619;
   **−85** at L8663; **−88** at L8694. One global offset would mis-anchor the string sections by
   six lines. Every witness above is anchored on its own text.
3. **L8676's *An earlier version of this line said convex* has no Prints & Proofs site** — the
   sentence is new in production, and it is the one correction in this unit that is registered.
   Docket 15's class, but a clean instance: narrated past state with its Register entry present.
4. **§11.7 names them *facts*, not *conditions*** (L2252), and does not itself mention
   independence; the degenerate-case claim is made only at §31.2.3 L8683. The count survives; the
   framing is the citing section's.
5. **§11.7 cites itself by number** — L2260: *§11.7 measures 89,864 join failures when one is
   tried*. A section pointing at itself for its own measurement. Outside the unit; deferred.
6. **Roche, Titius, Bode, Regge, Hagedorn and Gröbner are unbibliographed** — each with one
   main-volume site, none in `## References` at its body occurrence L11503 and none in R.7
   L11806. Mardling & Aarseth, Poincaré, Lagrange, Euler, Hill, Rydberg and Sperner are all
   bibliographed. **Seven of thirteen** attributions in this unit resolve. Docket 36.
7. **Single-witness figures in this unit**: 47.9, 16,423, 6.9 × 10⁻⁴, 3.6 × 10⁻⁹ — each with one
   site in six volumes. Of these 16,423 is **recomputed here and exact**, so under chat 115's
   refinement only 47.9, 6.9 and 3.6 are single-witness in the strict sense.
8. **The chapter-31 head's count word holds.** *four subjects it was not built for* against
   §31.1 (celestial mechanics **and** the nucleus — two), §31.2 (string theory) and §31.3
   (the Calabi–Yau catalogue) = four. Chapter 31 has exactly three top-level sections; the count
   is of subjects, not sections, and it is right.
9. **d(N) ~ exp(4π√N)** — MEASURED log d(N)/(4π√N) = 0.510, 0.587, 0.658 at N = 10, 20, 40,
   rising towards 1 as the sub-exponential factor is shed. The asymptotic form is consistent at
   the precision the sentence uses; recorded as consistent, not as verified to leading order.

---

## Census rows

Three in range, not the two HANDOFF-70 carried — measured on the `member` column of
DEFECT-CENSUS.tsv. See CENSUS-CLOSURES-ch16g.tsv.

## Instrument faults, self-caught and rewritten in place, none trimmed — five

1. The nucleus E(X) test re-applied the index's own defining filter instead of measuring
   ℛ-closure, so E = 0 was true by construction. Rewritten to use `Rset`.
2. The projection-ladder fibre count compared Λ_d with itself and returned the constant 1.
   Rewritten to count preimages in Λ_{d+1}; the true fibres are 1 to 4 and the book is right.
3. The Regge row was measured in floating point and returned second differences of ±8.9 × 10⁻¹⁶
   and a finite V of 4 × 10¹⁵. Rewritten in `Fraction`; the true second difference is exactly 0.
4. The third-difference windows for the planetary row were labelled by the wrong pair of planets.
5. The Prints & Proofs probe for §31.1.2 used a typographic apostrophe and scored **zero on the
   main volume itself** — its own source. Rewritten to a substring carrying no apostrophe.

**The book was right and the instrument wrong three times** (faults 1, 2, 3 each would have
recorded a true claim as a defect). Chat 110 five, 111 three, 112 zero, 113 one, 114 one, 115 two,
116 three, 117 four, **118 three**.
