# READ-ch15d — Chapter 27 "Slack", unit main L7203–L7331 (§27.1–§27.5.1)

Chat 105, Phase R2. BUILD90 main / BUILD133 compendia. Line numbers are **member** lines of
`The_Method_1_6-2.md` (1-based, 11,855 lines). No corrections made; no Register entry written.
Instruments: `r2-ch15d` (computable, golden 556b83a6) and `r2-ch15e` (prose, golden a2c06d90).

**Chapter extent, measured by heading scan before a line was read:** `## 27. Slack` at **L7203**
(the L147 hit is the contents entry), next top-level heading `# PART VI` at **L7364**. Chapter 27
is **L7203–L7363, 161 lines, seven `###` subsections** — over the 141-line ceiling, so it cuts.
This unit is **L7203–L7331, 129 lines**: chapter head, §27.1, §27.2, §27.3, §27.4, §27.5, §27.5.1.
**§27.6 (L7332–L7363, 32 lines) is unread** and closes the chapter in the next section read.

---

## A. Deviations

**15d-01 — The same passage is printed twice, in two chapters, with two Register entries.**
§9.2 **L1961–L1990** and §27.5.1 **L7299–L7330** are one passage. Shared verbatim: the display
sentence *Between any two points there is an interval, and the method returns its measure*
(L1963 / L7314); the three-row interval table (L1970–L1974 / L7304–L7308), rows `[x∧y, x∨y]`,
`[min, max] output rank` and `[T(n−1), T(n+1)]` identical; *Theorem 18.2 permits it* (L1980 /
L7321); *…separately bounded and rarely both* (L1984 / L7327). §9.2 closes **Register 438**
(L1990); §27.5.1 closes **Register 446** (L7330). **Detail diverges in both directions**: §9.2
alone carries *five forms* (L1971), *range [3, 23]* (L1973), the universality clause over
pairwise monotone envelopes with §14.3 and §18.4.1 (L1986–L1989); §27.5.1 alone carries the
11.3 % / 24.7 % / 0.3 % split (L7316–L7317), §17.3's δ = f − ℓ as a *fourth instance* (L7328) and
the convexity remark (L7329). **Each copy presents itself as supplying what the other omits**:
L1977–L1978 *§27 already proves the three MEASURES are one quantity; what was missing is that the
three OBJECTS are one shape*, against L7301–L7302 *§27.2 proves that E, the void and V are one
quantity under three measures. What that leaves unsaid is why they should be.* R3 decides which
site holds the passage, merges the divergent detail into it, and reconciles 438 with 446 by a new
entry citing both — the Register is append-only and neither entry may be removed.

**15d-02 — §27.2's periodic-table log column, L7236.** The row prints ambient 126, actual 90,
slack 1.400, log slack **0.337**. MEASURED: 126/90 = 1.4 exactly, and ln(1.4) = 0.336472 →
**0.336** under ROUND_HALF_EVEN *and* ROUND_HALF_UP. log₁₀ gives 0.146, log₂ gives 0.485; no base
gives 0.337. The other four rows of the table are exact under ln (1.958, 0.019, 2.594, 3.977), so
the base is settled as e and this row alone misses in the last place. Inverting: exp(0.337) =
1.400739, so the printed log needs a ratio of **1.4007**, not the 1.4000 the row itself prints.
R3 corrects the column to 0.336 or states the ratio that gives 0.337.

**15d-03 — §27.5.1's percentages carry an unstated denominator convention, L7316–L7317.**
*The lattice order relates 11.3 % of Λ₉'s pairs and composition relates 24.7 %, and they share
0.3 %.* MEASURED on the rebuilt Λ₉ (1,654 cells) with the book's own order, `r2lib.leq`:
**309,526 unordered pairs are comparable**, which is **22.6422 %** of C(n,2) = 1,367,031 and
**11.3211 %** of n(n−1) = 2,734,062 — printed 11.3 reproduces **only against the ordered
denominator**, an unordered numerator over an ordered pair count. The 0.3 % overlap behaves the
same way (0.6496 % unordered, **0.3248 %** ordered). The section states neither denominator. R3
prints the convention or restates both figures on C(n,2). **Not a deviation, and recorded as such:
composition's 24.7 %**, which does not reproduce under my reconstruction of the relation
(tgt(a) = src(b) gives 3.03 % / 1.52 %) — under the standing rule the reconstruction is the
suspect, so 24.7 % is logged **NOT RECONSTRUCTED** and carried to R3 with the relation named.

**15d-04 — §27.1's table is shattered into fragments, L7208–L7224.** Column text is broken across
lines mid-word — `orde`/`r`, `geo`/`metr`/`y`, `calcu`/`lus` — and the header *in the / book / as
/ definition* is split over three lines. MEASURED against the Prints & Proofs original
(`The Method 1.6.md`, 738,550 B, md5 49900cf41f818ab789bb90fc596ac977, verified at fetch): the
block is **identical there**, at P7133–P7150. **Carried from the original input, not lost in this
build** — the chat-104 L7156 disposition. Adjacent and measured: of the chapter's five tables only
**§27.3 (L7251–L7257) is a markdown pipe table**; §27.1, §27.2, §27.4 and §27.5.1 are space-aligned
plain text and will not render as tables. R3 rebuilds all four.

**15d-05 — L7301 cites an assertion as a proof.** *§27.2 proves that E, the void and V are one
quantity under three measures.* §27.2 (L7228–L7243) is a formula line, a five-row table and a bold
assertion — the word *prove* does not occur in its span. The overstatement is shared by the
Register: **446's headline** reads *…§27.2 proved the first and never said why.* R3 repairs both
together, or authors the proof §27.2 is credited with.

**15d-06 — Ruling 45, two more members (the class reaches twenty-one).** **L7244** — *The name was
chosen before the quantity was analysed* — discloses the authoring order to the reader. **L7312** —
*Three sections computing one shape, none citing the other two* — is a remark on the book's own
citation practice. Both are editorial-process statements in a reader-facing volume. Tested and
**not** members: L7204 and L7232 (*this book has computed…*, scholarly voice, established
vocabulary) and L7261 (*in practice a teacher does*, an aside inside a substantive point).

---

## B. Verified — R3 does not re-derive these

- **The bounding box.** Λ₈'s per-coordinate widths measured on the rebuilt lattice are
  3 × 2 × 3 × 4 × 3 × 2 × 4 × 4 = **6,912**, and 6,912/976 = 7.081967 → **7.082**, ln → **1.958**.
  Both exact under both rounding conventions. 6,912 has 29 sites across five volumes.
- **The two bracket rows reproduce exactly from the book's own exact V.** L6237 states *The exact
  V is rational at every ν — 32/11, 54/13, 256/47, 250/37, 4000/299 — and 4ν/3 + 4/(9ν) is its
  asymptote.* All five rationals satisfy **V(ν) = 4ν³/(3ν² − 1)**, verified as exact fractions. At
  ν = 10 that is **4000/299 = 13.377926 → 13.378**; at ν = 40, **256000/4799 = 53.344447 →
  53.344**; ln of each gives **2.594** and **3.977**, log₂ gives **3.74** and **5.74**. The
  asymptote reproduces the same four figures. **The asymptotic 4ν/3 alone reproduces none of them**
  (13.333, 53.333) — see C-1.
- **The Rydberg charge of 1.54 is the floor in bits.** log₂(32/11) = **1.540568 → 1.54** under both
  conventions. 32/11 is Proposition 23.1's floor (L6237, L6381; docket 11). Not a single-witness
  figure and not unsourced.
- **The bits table, all four computable rows exact.** log₂C(126,36) = 105.0815 → **105.1**;
  log₂C(372,7) = 47.3930 → **47.4**; both E = 0 rows give **0.0** because C(N,0) = 1. The bits/cell
  column divides the bits by |X|, not by E: 105.1/90 → **1.168**, 47.4/365 → **0.130**.
- **The calendar and periodic-table slacks.** 372/365 = 1.019178 → **1.019**, ln → **0.019**;
  126/90 → **1.400**. Only the periodic table's log column misses (15d-02).
- **Prop. 23.1 in bits is an identity, not a measurement.** L7266's *V > 2 ⟺ log₂V > 1* holds
  because log₂2 = 1, for any V. **Structurally forced — not a finding either way**, and the reason
  census rows 1148/1149 dispose as artefacts.
- **d = ∏(|Δᵢ|+1) = τ(lcm/gcd)** (L7305): 4,000 sampled Λ₈ pairs, zero mismatches, and the two
  forms are the same product for any non-negative integer exponent vector. **Structurally forced.**
- **Every section pointer in the unit resolves to its claim**, tested on the raw line with the
  symbol as well as the word: §9.2 (L7226, L7295, L7310) → L1958, occupancy/metric found; §23.7
  (L7282) → L6321, *pole* found; §12.11.0.12 (L7310) → L2999, the quoted sentence found; §22.1
  (L7311) → L5943, *measurement* found; §25.6.3 (L7323) → L7039, *deduction*/*measured* found;
  §17.3 (L7328) → L4814, **δ found on the raw line**; §18.6 (L7322) → L5303. **Docket 9 gains no
  member from this unit.**
- **Theorem 18.2 (L7321) is a theorem number, not a section pointer** — stated at **main L4940**,
  and §18.2 (L4970) is *ν is inadmissible as an axis*, a different object. The citation is correct.
- **Figure 27.1** (L7269) references `figures/figure-27.1.png` and is named at exactly two sites,
  its own reference and its own caption. The caption (L7271–L7274) states facts only — Ruling 45
  clean — and both figures it describes are verified above.

---

## C. Incidentals

1. **L7308 prints the asymptote as the price.** *w, priced at V = 4ν/3* — while §27.2's own table
   two pages earlier uses the exact rational. The volume states the distinction at L6237, so this
   is the truncation-printed-as-equality shape (docket 12) rather than a wrong figure.
2. **The subnet's two inputs are unprinted.** §27.3's *subnet with a hole* row prints E = 8, 48.5
   bits and 0.196 bits/cell but neither |ℛ(X)| nor |X|. Inverting the bits column gives
   |ℛ(X)| ∈ {**255, 256**}; the bits/cell column rounds to 0.196 at **both** 247 and 248, so the
   section fixes neither input. Docket 10.
3. **L7283's word differs from its target's.** *E(X) = 0 ⟹ nothing to forecast* points at §25.6,
   whose 127 lines never use *forecast*; the section's word is *prediction*. The claim resolves in
   substance.
4. **Incoming pointers are lopsided.** §27.2 has four (main L7301, L7357, reg L1485, L1657) and
   §27.4 has two (main L11438, L11442); **§27.1, §27.3, §27.5, §27.5.1 and §27.6 have none.**
   §27.5.1 is cited by nothing, which is what makes 15d-01 survivable in the book as printed.
5. **The 17 % / 264 row is corroborated, not a single witness** — main L1972 prints it and L3016
   supplies its population (*264 distinct (rank a, rank b) inputs*). Only §9.2's copy carries the
   *range [3, 23]*.
6. **Single witnesses, all internally reproduced above**: 7.082, 1.958, 13.378, 53.344, 2.594,
   3.977, 47.4, 1.168, 0.130, 0.196, 3.74, 5.74. None is recorded as unverifiable.

---

## Instrument faults, self-caught and rewritten, none trimmed

1. **The one that mattered.** r2-ch15d's first draft tested the bracket rows against the asymptotic
   4ν/3 only, reported a 0.33 % miss at ν = 10, and would have recorded **13.378, 53.344 and 1.54
   as three unreproducible figures**. The excess scaled as 1/ν², which named the next term; the
   volume then supplied the exact rational at L6237. Grepping the volume before recording a figure
   as unreproducible is what saved three false deviations.
2. r2-ch15d B5 measured the order relation without the composition relation beside it, so it could
   not tell a wrong numerator from a denominator convention shared by both.
3. r2-ch15d's first draft held the log base at e; three bases are now swept on every log column.
4. r2-ch15e tested claim tokens in spelled form only, so **δ** was reported absent from §17.3,
   which prints the symbol. Symbols are now tested beside their names, on the raw line.
5. r2-ch15e treated *Theorem 18.2* as a pointer to §18.2 and resolved it to the wrong section.
   A theorem number is not a section number.
6. The first census selector keyed on a column named `volume`; the file's column is `member`, and
   the selector silently returned zero rows in range where seven exist.
7. The first heading scan matched `## 27. Slack` at L147, the contents entry, and measured the
   chapter as three lines. Both occurrences must be resolved before an extent is taken.
