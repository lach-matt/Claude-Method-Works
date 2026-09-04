# READ-ch14f.md — Chapter 22, *The bracket* — main L5937–L6035 (chat 93)

Section read: **PART V opening (L5937), Chapter 22 (L5939), §22.1 (L5943), §22.1.1 (L5953),
§22.1.1.1 (L5982), §22.1.2 (L6006)** — 99 lines, five headings, closing at the line before §22.2
(L6036). Every boundary measured by heading scan before a line was read. Instruments: **r2-ch14f**
(computable, golden 7,784 B · md5 35f7068c · 125 lines) and **r2-ch14g** (prose, golden 14,016 B ·
md5 436ae11b · 192 lines). Both banked and reproducing.

Line numbers are member line numbers (`The_Method_1_6-2.md`, 1-based). The bundle file numbers each
line one higher because of its `<<<FILE:` header; the handoff, r2-tools and every prior chat use the
member numbering, and so does this file.

---

## A — deviations

### 14f-01 · §22.1.1.1 claims F.3's highest standard on three of its four columns

**Printed, L5983–L5985:** *§22.1 brackets a level from its two measured neighbours and reports the
result once. **This states it to F.3's highest standard**: the method named with its input set, every
input printed, and the test recomputed at four quantum defects rather than one.*

**Measured (r2-ch14g [G2]).** F.3 (L11278–L11300, 22 body lines) states a four-column standard: **the
method · the input set · the inputs · the refutation**, and says in its own words that a statement
carrying fewer than four *is not a weaker version of the same claim; it is a different kind of
object*. The citing sentence names the first three and puts the recomputation at four defects where
the fourth column belongs. Word-bounded search for `refut` across the whole section read (L5937–
L6035) returns **nothing**: the refutation column is neither named nor supplied.

The recomputation is a robustness demonstration, not a refutation: it shows the result survives
variation of its input, which is the opposite move from naming the test that would kill the claim.
A refutation is available here — a level failing containment would be one, and the table's
*contained* column could have printed less than 9 — but the section never says so.

**Class:** self-description, overstated against a standard the book itself defines. R3 either adds
the refutation column or drops *highest*.

### 14f-02 · two sentences attribute to §22.1 a run it does not contain

**Printed, L5983:** *§22.1 brackets a level from its two measured neighbours and reports the result
once.* **Printed, L6004:** *…which is what §22.1's single run could not distinguish.*

**Measured (r2-ch14g [G3]).** §22.1's body is **L5944–L5952, nine lines**. It contains **two digits**
in total, both inside the display `T(n) lies between T(n−1) and T(n+1)`; **zero** mentions of a defect
or δ; **zero** numbers of three digits or more. There is no computed run in §22.1: no series, no
defect, no energy, no count.

L5983's *reports the result once* can be read as *returns one interval*, which §22.1 does claim
(*returns an interval rather than a value*, L5950). L6004's *§22.1's single run* has no such reading:
it stands in explicit contrast with *four quantum defects rather than one*, so it asserts one
computation where the section performs none.

**Class:** pointer resolving to the heading and not to the claim. The claim §22.1.1.1 improves on is
real but lives elsewhere or nowhere; R3 must name where the one-defect run is printed, or restate the
comparison as *what a single defect could not distinguish*.

### 14f-03 · Register 319 is cited one paragraph late

**Printed, L5977–L5981:** *And it refines §18.4.1's criterion in one direction. Both bounds decrease
in m, and a decreasing cap breaks joins in a product — the coordination-number result. … The
criterion was stated for products and this is the one-dimensional case of it. **Register 319.***

**Measured (r2-ch14g [G4]).** Register 319 reads: *A SECOND COMPANION PAPER, ON MUON-CATALYSED
FUSION. Its structural window is a bracket whose admissible set is a singleton — the same operation
reads as a deduction or a uniqueness proof depending only on how many cells the interval holds. Every
computed figure reproduced.* Tested against the citing paragraph's six topic tokens — `criterion`,
`product`, `increasing`, `monotone`, `coordination`, `one-dimensional` — **0 of 6 are present**.

The entry is not off-topic for the *section*: it states L5970–L5975's claim almost word for word, and
the References line at L11599 names it as *the source of §22.1.1's singleton bracket*. It is attached
to the wrong paragraph. By contrast Register 391 scores **5 of 5** against its citing sentence and
Register 328 **4 of 4**.

**Class:** citation placement. R3 moves the pointer to the end of L5975 or adds a second entry
covering the one-dimensional refinement, which no Register entry currently carries.

### 14f-04 · the printed 918 and the printed 207 do not give the printed 4.44

**Printed, L5966–L5968:** *The pion at 273 is absorbed by the nucleus before it can catalyse; the muon
at 207 remains, interior by 1.74× below and 4.44× above…*

**Measured (r2-ch14f [F3]).**

| from | m/119 | 918/m |
|---|---|---|
| muon 207 (the page's own figure) | 1.7395 → **1.74** | 4.4348 → **4.43** |
| muon 206.7683 (PDG) | 1.7375 → **1.74** | 4.4398 → **4.44** |

The lower factor is 1.74 from either mass. The upper factor 4.44 requires the unrounded mass; a
reader dividing the two figures the same sentence prints gets 4.43. Both numbers are individually
correct — this is an internal-closure failure, not a wrong value.

**Class:** arithmetic presentation. R3 prints 4.43, or prints the mass to the precision the factor
uses.

---

## B — verified

**14f-B1 · the whole containment table recomputes exactly (r2-ch14f [F5]).** R = 109,737.31568 cm⁻¹,
Z = 1, T(n) = Z²R/(n − δ)², n = 4…14 → 11 levels, **9 interior**. At every one of δ = 0.00, 0.35,
1.35, 2.65: **9 of 9 contained**, and both printed energy extremes reproduce to the printed decimal —
559.9 / 6,858.6 · 589.0 / 8,237.0 · 685.8 / 15,626.5 · 851.8 / 60,212.5. Total **36 of 36**, and
4 × 9 = 36. The span 60,212.5 / 559.9 = 107.5× is *two orders of magnitude* as printed.

**14f-B2 · seven interior held, at every defect (r2-ch14f [F7]).** For n = 4…12 (9 levels) the
interior count is **7**, and 7 are contained with **zero failures** at all four defects — the result
is defect-independent, which is stronger than the single series the sentence claims.

**14f-B3 · the seven widths and their six ratios (r2-ch14f [F8], [F9]).** The widths 4,799 · 2,594 ·
1,562 · 1,015 · 697 · 499 · 370 reproduce at **δ = 0.35** with a maximum deviation of **0.0** against
the printed rounding; the other three defects miss by 989, 5,752 and 45,635. Seven widths give six
ratios (arithmetic checked), and all six reproduce: 0.5404 · 0.6024 · 0.6495 · 0.6865 · 0.7164 ·
0.7410 against the printed 0.540 · 0.602 · 0.650 · 0.687 · 0.716 · 0.741. The rise is monotone —
*a clean pattern* is exact.

**14f-B4 · the extrapolation figures, including the percentage (r2-ch14f [F10]).** True next width
T(11) − T(13) = **281.7474** → printed 281.7. The presumed width is the *unrounded* last ratio times
the last width, **274.10** → printed 274.1 (the printed rounding would give 274.17). The error against
the true width is **2.715 % → 2.72 %**, exact to the printed precision; against the presumed width it
would have been 2.79 %, so the base is the true width and the book has it right.

**14f-B5 · the ν⁻³ law-derived ratio (r2-ch14f [F11]).** ((n − δ)/(n + 1 − δ))³ at n = 11 gives
**0.7640** → printed 0.764, against the observed 0.7410 → printed 0.741. Applying the law-derived
ratio to the last width gives 282.6 against the true 281.7, an error of **0.29 %** — the law-derived
presumption is not merely the legitimate one but the **more accurate**, by a factor of 9.3 over the
pattern-derived 2.72 %. The section argues the point on legitimacy alone; the measurement supports it
on accuracy as well.

**14f-B6 · the muon window closes on an unprinted deuteron mass (r2-ch14f [F1], [F2]).** The upper
bound comes from N ≈ √(M/m) with at least two bound states, i.e. m ≤ M/4. Solving M from the printed
918 gives 3,672 mₑ; the deuteron is 3,670.4833 mₑ and M/4 = 917.62 → **918**. The same M carries the
whole trio: √(M/m) = 60.585 · 4.2133 · 1.0274 for electron, muon and tau against the printed **60.6 ·
4.21 · 1.03**. Solving M back out of each printed value gives 3,672.4 · 3,664.8 · 3,689.0 mₑ, a spread
of 0.50 % — rounding, not disagreement.

**14f-B7 · "two known particles" (r2-ch14f [F4]).** In [119, 918] mₑ: muon 206.77 **inside**, charged
pion 273.13 **inside**, charged kaon 966.10 **outside** by 48 mₑ, tau 3,477.23 outside. The count of
two is right, and the kaon's exclusion is what makes it right.

**14f-B8 · §12.11.3.1 resolves to its claim, and points back (r2-ch14g [G1]).** Its D-table gives
D9 *vector coupling on the target — law*, D10 *seniority, Racah 1943 — law*, **D11 2J_c ≤ φ̂(k), the
envelope of the realised maxima — extent**, and it states in its own words that *a bound taken from
the law closes exactly. A bound taken from the extent closes only to an envelope.* It also carries a
reciprocal pointer: *it is the same distinction §22 draws between a deduction and a fit.*

**14f-B9 · §18.4.1 carries the coordination-number result (r2-ch14g [G1]).** Its 248 body lines carry
`coordination` (*coordination number ≤ f(radius ratio) — no, decreases, breaks*), `increasing`,
`monotone`, `product` and `cap`. The refinement §22.1.1 claims is a refinement of something the target
actually states.

**14f-B10 · §12.11.0 carries the composition claim (r2-ch14g [G1]).** *Define b ∘ a when a's target
equals b's source*, and *composition is time — not a stamp on a cell but an order*. The citing phrase
*a composable index makes before and after an order* resolves.

**14f-B11 · Registers 391 and 328 carry their citing sentences exactly (r2-ch14g [G4], [G5]).**
Register 391 has all four defects, *thirty-six of thirty-six*, energies *560 to 60,213 cm⁻¹* (the
table's 559.9 and 60,212.5 rounded), *ninefold*, *order of magnitude* and *monotonicity* — 5 of 5
tokens. Register 328 has *seven interior cells*, *fit*, *2.72 %* and *between two observations* — 4 of
4.

**14f-B12 · the companion attribution matches the References (r2-ch14g [G6]).** L5955 cites
*Muon-Catalysed Fusion*, Lach 2026; R.3 at L11598 gives *Lach, M. (2026). Muon-Catalysed Fusion:
definition, procedure, and two gaps, draft v1.1*. Title and year agree, and L11599–L11600 name it as
the source of §22.1.1's singleton bracket and record that the window [119, 918] mₑ reproduces.

**14f-B13 · "a use this book had not stated" stands (r2-ch14g [G8]).** Nineteen sites carry
`singleton` or `uniqueness proof` across the six volumes. Eleven are the **singleton-output rule**
(§33.4, Register 4873, mc L3753, ioi L1609–L1611) — an index whose *output class* has one element.
Two are records of this section (Register 319, References L11599). Four are unrelated uses (K
collapsing to a singleton, axis 12 degenerating). **No site outside this section states the bracket
use**, so the claim is true as printed.

---

## C — incidental

**C-1 · §22.1.2 never prints the δ its seven widths use.** The series is given as *T(n) = Z²R/(n − δ)²*
with δ unnamed; the widths are reproducible only after solving for δ = 0.35 ([F8]). This sits one
subsection after §22.1.1.1's boast that **the input set is printed**, and against F.3's *the inputs:
every input printed, not summarised*. Recorded as incidental rather than a deviation because every
figure is correct at the solved δ, but it is the same standard 14f-01 turns on.

**C-2 · M is never printed in §22.1.1.** The bound *N ≈ √(M/m)* uses an M the section does not define
([F2]). The trio 60.6 / 4.21 / 1.03 is not reproducible from the page alone.

**C-3 · "a factor of nine" holds on two of four readings.** L6001's *stretches the series by a factor
of nine between the first row and the last*, measured ([F6]): top energy 8.78×, energy span
(max − min) 9.42×, bottom energy 1.52×, span ratio 5.77×. *Stretches the series* most nearly names the
span, which gives nine. Register 391 prints the same claim as *ninefold*.

**C-4 · "its own input being varied by an order of magnitude" (L6003) is loose.** The input is δ,
which runs 0.00 → 2.65: the ratio between the nonzero extremes is 7.57×, and from zero it is
undefined. The claim is exactly true of the *output* energies (107×, already stated at L5998 as two
orders). Not a false figure; a sentence whose subject is the input and whose measurement is the
output.

**C-5 · §33.4 and §22.1.1 are the same idea about different objects, unlinked.** §33.4 *The singleton
criterion* — *an index is closed when its output class is a singleton* — and §22.1.1's bracket whose
admissible set is a singleton. Neither section points at the other ([G8], measured both ways). For the
cross-volume pass.

**C-6 · Register 391 carries five unbalanced emphasis runs** (`* **`), which close the wrong markup
span mid-entry ([G5]). Production class; noted, not a concern, per M's standing priority.

**C-7 · §18.6's pointer resolves to the naming, not to the asymmetry.** L6033–L6034 calls the
inward/outward asymmetry *the same limit §18.6 states when it calls E(X) a prediction budget rather
than a prediction*. §18.6's nine body lines carry `prediction` and the heading carries *prediction
budget*, but `after`, `last`, `extrapolat*` and `beyond` are all absent ([G1]): the temporal asymmetry
is not in §18.6. It is in Register 328, which the same sentence also cites, so the paragraph is
supported — but by its second pointer, not its first.

**C-8 · companion-side claims, unverifiable here.** The paper is cited and listed but is **not a
member of either bundle** ([G6]): *the paper's 61, 4.2 and 1.03* (L5968) and *the companion paper's
first observed r_ℓ exit was predicted in advance from that same ν⁻³ scaling and then occurred*
(L6024–L6026). Recorded as unverified, not as deviations, per chat 92's precedent. This book's own
recomputation of the trio is verified at 14f-B6; what cannot be checked is the paper's own printed
values.

**C-9 · no lowercase `register NNN` in range** ([G10]); the three citations are all capitalised —
Registers 319, 391, 328 — and all were resolved.

---

## Instrument faults, self-caught and rewritten

Four, all found before banking, all repaired by rewriting the test rather than trimming it.

1. **F11's comparison was written backwards.** The draft printed *LARGER than the pattern's* for an
   error of 0.29 % against 2.72 % and concluded the book's argument was undercut. The measurement was
   right; the sentence inverted it. Corrected: the law-derived presumption is the more accurate, by
   9.3×, and the finding moved from A to B.
2. **G8's summary asserted what its own measurement denied.** It described all nineteen `singleton`
   sites as records of this section; eleven are the unrelated singleton-output rule. Rewritten to
   classify the sites into three kinds and print them, which is what produced C-5.
3. **F3 printed a bare `CHECK`** from a compound condition without naming which half failed. Rewritten
   to print both masses, both quotients and the verdict — which is 14f-04.
4. **F6 asserted a reading of L6003 it had never measured.** Rewritten to measure δ's spread and the
   energies' spread separately, which is C-4.

The first is the one to carry forward: it is chat 92's inverted-verdict class recurring in a different
form — there a substring match, here a comparison word — and both times the arithmetic was correct
while the sentence built on it was not.
