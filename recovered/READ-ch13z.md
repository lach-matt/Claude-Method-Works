# READ-ch13z.md — chat 90 — Chapter 21, first part (main L5597–L5689)

Section read: `## 21. Translation, and what it costs` L5597; §21.1 L5599, §21.2 L5616, §21.3 L5624,
§21.4 L5636, §21.5 L5645; the read stops at L5689, §21.5.1 opening L5690. Ninety-three lines, five
headings, all boundaries MEASURED by heading scan before the read. Instruments: `r2-ch13z` (computable,
banked 4,238 B · 353f472e) and `r2-ch14a` (prose, banked 13,544 B · acb33948).

## A. Deviations

**21z-01 — L5685, "Λ's seed is **ten cells for 976**."** MEASURED seed(Λ₈) = **7**, by branch and bound
on §14.5.7's covering model (r2-ch13z §3). The volume itself says so at **§14.5.9 L3934**: *seed(Λ₈) = 7,
exactly, by branch and bound. This book reported ten to thirteen for twelve cycles.* Four further sites
agree at seven — main L3935, L4107, L4155, and mc L722/L724 (*Λ's seed — seven cells*). L5685 is the
**single surviving site of the withdrawn heuristic value**, five to one against. Repair is one
substitution plus the arithmetic that hangs off it (21z-04, 21z-05).

**21z-02 — L5676, the parity rule's seed printed 13.** MEASURED seed(ℛ(X)) = **7** for the 840-cell
parity object (r2-ch13z §7). Thirteen is the top of the same withdrawn *ten to thirteen* band. The row's
printed column 763 = 13 + 750 becomes 757; compression 840/757 = 1.1× is unchanged at one decimal, so
the table's arithmetic survives the correction and the seed column does not.

**21z-03 — L5606, "one object" under two namings.** MEASURED: {|Δℓ| = 1} is **840 cells at E = 750**;
{|Δℓ| ≤ 1} is **1,654 cells at E = 0** — the whole of Λ₉, closing because it excludes nothing. The second
naming holds **814 cells the first does not**; they are not one object. Extended beyond chat 89's
instance: **no relabelling of any coordinate's value alphabet takes the 840 cells to E = 0** — 118
relabellings swept over all nine coordinates, least E attained **114** (at *f*), never 0. §21.1's row 3
is the general form of 20x-01 and fails for the whole class at this index.

**21z-04 — L5682 against L5686, two seed estimates for the violation index in one section.** L5682: *a
seed near fifteen, so about forty-five cells for 2,370*. L5686: *likely nearer twenty for 2,370*.
15 + 30 = 45; 20 + 30 = 50. At Λ's printed ratio (10/976) the figure is **24.28**; at the measured ratio
(7/976), **17.00**. Neither printed estimate is the one the section's own ratio gives.

**21z-05 — L5683, "a seed near twenty-five carries all 199,130."** Unsupported by any ratio in the
section: 199,130 at the printed ratio gives **2,040**, at the measured ratio **1,428**. MEASURED seeds
are **7 / 8 / 9** at Λ₈ / Λ₉ / Λ₁₀, so the measured series suggests a seed near **twelve** at arity 13
(INFERRED by extrapolation, not measured). Twenty-five has no derivation in the section either way.

**21z-06 — L5604, "the 118 elements" is not the object measured.** Every other site prints the
periodic-table index at **90 cells** — main L1613, L3243, and §21.5's own row at L5674 — all at E = 36.
The row names the chemistry and measures the index.

**21z-07 — L5601, "Eight results in this book have the same shape."** MEASURED: **five** of the eight
rows (L5604–L5608) carry the header's one-object / two-naming / E shape; three (L5609, L5610, L5611)
carry no second naming and no E and run across the columns as single statements. Census row 1126.

**21z-08 — L5647, "audit 21."** The phrase occurs **once in the six volumes**, at this line; no member
names a numbered audit 21. The audit index is 21 cells (L3851, L5673), so the citation is presumably to
its last row, which is nowhere printed with a number.

**21z-09 — L5656 points to a section with no body.** MEASURED: **§14.5.3, §14.5.4, §14.5.5, §14.5.6 and
§14.5.7 are heading-only** — L3800–L3809, five consecutive headings, zero body lines each. §14.5.7 is
cited at L1203, L3812, L3919, L3923, L4107, **L5656**, L5799, L7799 and L11759 — nine sites citing an
empty section, one of them the load-bearing citation of §21.5's repair. Possibly a production class
(bodies lost at a build) rather than an authoring gap; it cannot be told from the file.

**21z-10 — L5678–5679, "E is the binding term."** MEASURED: compression is **not monotone in E/|X|**
across the table's own four rows. The audit index at E/|X| = 0.762 compresses 0.9×; the parity rule at
0.893 compresses 1.1×. The seed share differs by twenty-two times (0.333 against 0.015), and the second
clause — *the seed term is small at high dimension* — is what carries the claim. The table's own
low-dimension row is the counterexample to the first clause taken alone.

**21z-11 — L5611, "six languages agree; ten combinations hold."** Ten is C(5,2); C(6,2) = 15. The site
inherits chat 89's 20x-04 (six against seven languages) and 20x-09 (mc L81's C(5,2) against mc L1446's
own *C(6,2) = 15 exist; ten were put to P21*).

## B. Verified

1. §21.1 row 3's **first** naming, exactly: 840 cells, E = 750 (r2-ch13z §1).
2. §21.1 row 4's E = 16 for the audit set — agrees with L3851 (four coordinates, 21 cells, E 16, seed 7),
   L5025 and L5673. L5062's **17** stays the single outlier: **four sites to one**, strengthening 13t-02.
3. §21.5's four-row table: **seed + E = printed in all four rows**, and |X| / printed reproduces the
   printed compression to one decimal in all four (0.9 / 1.6 / 9.6 / 1.1).
4. §21.5's recovery claim: ℛ(X) \ X = **750 = E** exactly, and ℛ(X) minus those cells recovers X exactly.
5. §21.3's *thirteen coordinates*: arity 8…13 across the tower with q at index 3 at **every** index;
   factor_q(Λ₉) = 0.
6. Pointers §18.4.1, §16.7.1, §16.6 and §20.1 resolve to heading **and** claim. §3.7 carries *362
   comparisons* and *eight and a half million* exactly, at L1335–L1336.
7. Registers **326, 451, 452, 453** all resolve to seated entries (reg L1207, L1675, L1679, L1683).
8. ⅅ_ref, ⅅ_dict and ⅅ_gro are all defined inside §16.6 (L4482–L4519), four / three / two occurrences.
9. §19.5.1's forward pointer at L5492 (*this is §21.5's obstruction*) resolves into this section.
10. **§14.5.9's *seed(ℛ(X)) + E for open indexes* is in the SURVIVING list (L3953–L3954), not the
    withdrawn list (L3946–L3951).** §21.5's repair formula stands. Recorded because the first reading of
    that block took it for a withdrawal; it was corrected against the file before anything was written.
11. §21.4's *every number above is already proved elsewhere in this book*: all twenty figures tested
    occur outside the range — including 341,150 (6), 431,050 (9), 206,520 (7), 19,440 (3) and 2,370 (27).
12. Tower controls: 976 / 1,654 / 2,535 / 13,585 / 70,905 / 199,130, and E(Λ₉) = 0.

## C. Incidental

1. §16.6.1's own title is *The vocabulary of reference, as an index*; L5632 calls it *the reference
   index*, which is not the section's name.
2. L5682 runs long against the volume's wrap — a single source line carrying two sentences.
3. The audit index compresses at **0.9×**, a loss, and is still listed among the indexes that *recover
   exactly*. Recovery and compression are different claims and the section keeps them apart correctly.
4. **199,130 is both Λ₁₃'s cell count and the jK coupling count** printed at L5609 and L5653.
5. Chapter 21's first part cites the Register four times (L5639 lowercase *register 326*, L5643
   *Registers 451–453*) — against Chapter 20's zero.
