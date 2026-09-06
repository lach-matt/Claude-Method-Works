# READ-ch13j.md — Phase R2, chat 82 — main §14.5.8 through §14.6.6 (L3810–L4269)

The first section read under the chat-81 ruling: the whole section read first, its claims censused into
two kinds, then exactly two instrument batches — **r2-ch13j.py** (computable) and **r2-ch13k.py** (prose).
Both banked (`r2-ch13j.out` 9,907 B md5 2eff9e97…, 87 lines; `r2-ch13k.out` 14,981 B md5 0b0feb5a…, 153 lines).

**Clerical correction to HANDOFF-34, MEASURED.** The section does not end at L4157. `### 14.6.4` opens at
L4179, `### 14.6.5` at L4210, `### 14.6.6` at L4240, and `## 15.` at **L4270**. The section read is
L3810–L4269, 460 lines, and Chapter 15 begins at L4270.

## The claim census

**Computable (r2-ch13j):** the two seed laws and the family table L3814–3818; the tower seed table
L3826–3829 and L3871–3875; the four indexes L3850–3854; the five-way axis table L3890–3898 and the
three-point table L3903–3906; the closure of the two-parent sets L3912; the eight-column heuristic table
L3928–3932; the four cells, their marginal coverage and the 102 elements L3964–3985; the unique-coverage
test L3973–3976; the completions L3992–3993; the 219 covers and six conditions L4012–4027; the fifth
position L4034–4049; the binary table L4056–4071; the theorem and both Cl(U) tables L4084–4137.

**Prose (r2-ch13k):** the six pointers into §14.5.7; §4.6; §28.9; §11.5 and §7.1; the §8.2/§8.4/§10.1
pointers of §14.6.6; the self-counts of §14.6.3–§14.6.6; the thirty-four Register citations; the figure
census; the attributions of §14.6 and §14.6.5; the Ruling 45/46 candidates.

---

## A — deviations

**13j-01 (R3; §14.5.12 is the primary site, §14.5.11 and §14.5.13 inherit).** *The 219 is not a count of
minimum covers, and the four cells are not in every one.* L4012–4014 reads `219 distinct minimum covers
were found, and the same four appear in every one`; L4016 `Four cells appear in 219 of 219 covers`; the
heading L4010 `What every minimum seed contains`. MEASURED by exhaustive branch and bound on the
set-cover reduction: **Λ₈ has 24,585 minimum covers** (13,468 as reduced masks). The four printed cells
appear in **14,492 / 6,826 / 24,585 / 3,370** of them; only `(2,1,3,3,2,1,3,0)` is in every one, and
`(3,1,1,0,3,1,0,0)` is in **13.7 %**. All four together occur in **519** covers — **2.1 %**. The 519 is
exactly §14.5.11's `519 triples`, so the two subsections are counting the same set under two different
descriptions, and the 219 is neither: it is 62 + 157, the completions whose fifth cell has e ∈ {1, 3}
(13j-02). What is true is the weaker statement §14.5.10 makes: the four are a stable attractor of greedy
covering. What is false is `every minimum seed`.

**13j-02 (R3; §14.5.13).** *Three cells match the fifth-position pattern, not two, and it is not in every
cover.* L4034: `Every one of the 219 covers contains a cell matching (3, 0, 1, 1, *, 0, 1, 1)` with
L4035 `the target shell e free at 1 or 3`. MEASURED: Λ₈ contains **three** such cells — e = 1, e = 2,
e = 3 — and over the 519 completions they appear in **62, 28 and 157**. `247 of 519` contain one. The
printed 62 and 157 are each exact; the e = 2 cell and its 28 completions are omitted, and 62 + 157 = 219
is the figure §14.5.12 reports as a cover count. L4045's `a fork between exactly two elements` is a fork
between three.

**13j-03 (R3; §14.5.12).** *One of the six channel conditions is not 100 %.* Over the 519 completions
(l the source, f the target): s → p, p → s, p → p, the NULL transition q = 0 and the FULL transfer q = k
all hold in **519 of 519**; **s → s holds in 475 of 519 (91.5 %)**. L4022 prints 100 %.

**13j-04 (R3; §14.5.8 L3912–3915, Register 497 inherits).** *The two-parent sets are not ℛ-closed.*
L3912: `And the two-parent sets are still ℛ-closed — the seed construction found them, which requires
closure.` MEASURED on the base the section names (the 35-cell staircase in four coordinates, whose cell
counts 56 / 119 / 140 / 161 / 182 all reproduce exactly): `|y − x₀| ≤ x₁` gives **E = 26** and
`y ≤ x₀ + x₁` gives **E = 5**. Both one-parent constructions give E = 0. The inference at L3913 —
`A second parent does not break closure; it multiplies the seed` — fails on its own examples in both
halves: the exact seed costs are **+2 and +2**, not +10 and +11.

**13j-05 (R3; §14.5.8 L3831 and the L3826–3829 table).** *Λ₉ and Λ₁₀ do not seed identically.* The
printed set-cover column reads 7 / 9 / 9. MEASURED exactly: **seed(Λ₈) = 7, seed(Λ₉) = 8, seed(Λ₁₀) = 9**,
each with a witness verified to close (ℛ(G) = Λ). The 9 at Λ₉ is greedy's. L3831's `Λ seeds well below
the down-set law` survives (7, 8, 9 against 11, 12, 13); `Λ₉ and Λ₁₀ seed identically` does not.

**13j-06 (R3; §14.5.9 L3937–3939 and §14.5.8 L3815–3816).** *The full-box law fails, and the box rows of
§14.5.8 are refuted throughout.* `A down-set seeds at d + c − 1 and a full box at d + c − 2, both
confirmed by branch and bound.` MEASURED: the down-set law holds exactly at c = 4 and c = 5 for
d = 2…5 (5 6 7 8 and 6 7 8 9, reproducing §14.5.8's rows). The **box law fails at 3⁵ — measured 5 where
d + c − 2 gives 6** — and holds at 3², 3³, 3⁴, 4², 4³, 4⁴. §14.5.8's box rows (`2d`: 4 6 8 10 12 and
`3d`: 6 9 12 15 18) measure **3 4 5 5** and **4 5 6**: at 3³ the section prints 6 where the exact seed is
4 and where §14.5.9's own prune column prints 5. 4⁵, 4⁶ and 3⁶ were not attempted in this batch.

**13j-07 (R3; §14.5.9 L3928–3932).** *The heuristic columns and the spread are not reproducible as
printed.* The **EXACT column reproduces exactly** — 7, 7, 4, 5 — as does the down-set's LB = EXACT.
Nothing else does: greedy cover measures 8 at Λ₈ against the printed 7; the printed `reverse 40` is not
reverse-ordered prune (r2-ch13h measured 11 there) and is not worst-first greedy either (measured 23 over
the non-dominated cells, 27 over all); the LB measures 2 against the printed 5. Since `spread` is defined
at L3942–3944 as the range across these heuristics, **the 33 rests on instruments the section does not
define**. The claim L3942 makes — that the spread is the quantity to report — is unaffected.

**13j-08 (R3; §14.6.6 L4256, and §10.1).** *§10.1 has no V6 row.* L4256–4257: `§10.1's table nonetheless
reports V6 CLOSED at 14 cells in a box of 24`. MEASURED: §10.1 is L2026–L2031, six lines, one sentence
on the excluded cells; it contains no `V6`, no `14`, no `24` and no table. `V6` occurs at exactly three
lines in the main volume — L4256, L4259 (both this section) and **L5917**, which carries
`V6's box 24 = 2·2·2·3`. The object the section is describing is at §22-region L5917, not §10.1; and
L4259's `§10.1 is stated in the language §8.4 replaced` inherits the same misdirection.

**13j-09 (R3; §14.6.6 L4254, L4257, L4259).** *Three bare `§8.4` pointers resolve to the wrong §8.4.*
L4246 and L4250 qualify the pointer correctly — `T §8.2 (Appendix G)`, `T §8.4 (Appendix G)`. The three
later sites drop the qualifier. Main §8.4 is L1873 `Sperner, and not symmetric`; it states nothing about
vocabularies or the achronal ANEC. The phrase `achronal ANEC` occurs on exactly one line of the main
volume — L4255, inside this section. Appendix G (L11361–L11408) carries **one table row each** for 8.2
and 8.4 (L11396, L11397), so `Verified against T §8.2 (Appendix G)'s own table` names a table Appendix G
does not print: the arity-2 / arity-3 / arity-4 defect figures of L4246–4248 are stated in no member.

**13j-10 (R3; §14.5.8 L3856–3858; §28.9).** *§28.9 has no body.* L3858: `the register classifier used
here gives 32 cells and E = 7 where §28.9 gives 33 and 6`. MEASURED: `### 28.9 The register, indexed and
closed` is at L7772 and the next heading follows immediately — **zero non-blank body lines**. This is the
13i-01 class at a second site outside §14.5.

**13j-11 (R3; §14.6.3–§14.6.6, the self-count block).** *Five running counts, none consistent with
another.* MEASURED arithmetic:
- L4151 `It stood at 248 objects … 265 objects and eighteen roots at this build` against L4164's
  parenthetical `the register now holds 197, 191 settled, 6 unfinished`. **Both are stated as the live
  count, twelve lines apart.**
- L4164 `248 · 246 · 2 · 12 % open`: 246 + 2 = 248 ✓, but 2 of 248 is **0.8 %**, not 12 %; the section's
  own breakdown (L4174–4177: six modular, nine computed, six definitional, one graded OPEN) sums to
  **22**, which is 8.9 %, and L4181 then reads `§14.6.3 reports twenty-two unfinished`.
- L4192 and L4267 print `248 · 246 · 2 · 3 % open`. The **3 % is the parenthetical's**: 6 of 197 = 3.0 %.
  Two different registers are being reported in one headline.
- L4234 `179 → 170 settled · twelve unfinished · 7 % open`: 179 − 170 = **9**, 170 + 12 = **182**, and
  12 of 179 = 6.7 %. The base 179 appears without derivation from the 248 or the 197.
- L4267 repeats the §14.6.4 headline unchanged after §14.6.5 reported a different base and §14.6.6 closed
  two further objects: **the running count does not move when the section closes objects.**
- L4195 `18,288 constraint tests across all 118`: 18,288 / 118 = 154.98, not an integer per element. The
  figure is record-carried (Register 487 → the entry at Register L1977) and is at five other sites.

**13j-12 (R3; §14.5.10 L3987–3988, with 13f-01).** `the coordinate carrying g ≤ min(q, 4f+2), which §11.5
identifies as the single non-product term … and the only place the Pauli principle enters`. §11.5 (L2231)
and L2224 support the non-product half exactly. The Pauli half collides with §7.1, whose table gives
**two** constraints the Pauli origin — `k ≤ 2(2ℓ+1)` at L1755 and `g ≤ 2(2f+1)` at L1758 — and whose
L1762 reads `Seven constraints, four origins`. Same collision as 13f-01, at a new site.

**13j-13 (R3, attribution / R-ATTR).** Of the twenty names this section relies on, six have **no entry in
the References region**: Brunetti, Fredenhagen and Verch (L4250–4251, the four-part vocabulary the whole
of §14.6.6 turns on), Reeh (L4215), Takesaki (L4217, L4219) and Sorce (L4238). Colomb, Irlande, Raynaud,
Caspard, Monjardet, Kuznetsov, Obiedkov, Chandrasekaran, Flanagan, Wiesbrock, Borchers, Carathéodory,
Janet and Birkhoff all carry one. Chandrasekaran & Flanagan is cited with an arXiv number (L4229) where
its neighbours are cited by name and year.

**13j-14 (R3, Ruling 45 residue).** L4169 `the filling script is gone` and L4260–4261 `the reconstruction
was begun here before the reading caught it` are session and process remarks in a reader-facing volume.
L3823, L3832, L3877, L4001 and L4006 are the withdrawal-and-correction class M has ruled is preserved
(both states kept), not this class.

---

## B — verified

- **The covering model is exactly the book's.** Λ₈'s reduction gives 200 raw elements = 25 value slots +
  175 envelope steps, of which **77 raise the envelope**; 25 + 77 = **102**, the figure L3981 prints.
- **The four cover 87 of 102 = 85.3 %** (L3981), and the fifteen they miss are exactly the printed
  fifteen: envelope steps **g 4 · n 3 · 2S 2 · e 1 · k 1 · q 1** and alphabet values **2S 1 · g 1 · q 1**
  (L3984–3985).
- **Their marginal coverage is 23, 18, 12, 17 with 0 substitutes** (L3968–3971), each exact.
- **No envelope element is covered by exactly one cell** — 0 of 102 at Λ₈, 0 of 261 at Λ₉, 0 of 330 at
  Λ₁₀ (L3974–3976; `zero at Λ₉` verified, and the same at Λ₁₀).
- **519 completions from 66 distinct cells, min 3, median 12, max 157, ratio 13.08 to 1** (L3992–3993),
  every figure exact, and none of the 66 appears in all 519.
- **seed(Λ₈) = 7 exactly**, witness verified (L3934; confirms 13h-04).
- **The down-set law d + c − 1 is exact** at c = 4 and c = 5 for d = 2…5, and the down-set's lower bound
  equals its upper bound (L3937–3938). The `down-set` of §14.5.8 and §14.5.9 is identified as the
  **staircase** — non-increasing d-tuples over {0…c−1} — which is ℛ-closed; the simplex reading has the
  same cell counts but E > 0 and is not an index at all.
- **The five axis constructions reproduce every printed cell count** — 56, 119, 140, 161, 182 — on that
  base, which fixes the construction beyond doubt (see 13j-04 for what they measure).
- **The binary table is exact.** Per-coordinate min/max over Λ₈ are (1,0,1,0,1,0,0,0) and (3,1,3,3,3,1,3,3);
  all five printed rows reproduce bit for bit, corner 1 / corner 2 and corner 3 / unit 5 are complementary
  in **3 of 3** specified positions, corner 4 = **11001100** is the only fully specified row, and every
  one of the eight columns carries both a 0 and a 1 (L4058–4071).
- **§14.6's two tables are exact in every figure.** |Cl(U)| = 13, 38, 74, 147, 506, 320, 732 and
  E = 3, 26, 182, 365, 3,590, 3,776, 64,804 at (2,2), (3,2), (2,2,2), (3,3), (4,3), (2,2,3), (2,2,2,2);
  **ℛ(Cl(U)) = 2^U in all seven**; intersection closed at 100 % everywhere; **12 of 12, 56 of 56, 72 of 72
  separating ordered pairs** (and 30, 132, 132, 240 at the other ambients); every envelope constant at 1;
  64,804 + 732 = 65,536; 64,804 / 732 = 88.5.
- **The union rates 65.3 / 68.8 / 32.7 % are the unordered-pair reading** (ordered gives 65.8 / 69.0 /
  32.8 %). The denominator is not stated in the text; both readings support `escapes at a third to two
  thirds`.
- **§4.6 resolves correctly.** It is Chapter 4's protocol row L1447, `a test that could not fail — exhibit
  the failure mode before trusting the pass`; r2-tools reports it UNRESOLVED because Chapter 4's rows are
  not headings. L4006 uses it exactly as L1447 states it.
- L4167's component arithmetic is exact: 162 + 9 + 2 + 2 + 1 = 176 over 220 edges, five components.
- L4200–4203's seventeen is exact: 8 + 6 + 2 + 1 = 17 = 22 − 5; L4236's remainder 6 + 2 + 1 + 2 + 1 = 12.
- Every one of the thirty-four Register entries this section cites **has a heading in the Register**.
- L3886–3888's `still 7,000×`: 199,130 / 28 = 7,111.8.

---

## C — incidental

- **§14.5.8 and §14.5.9 are a section and its own retraction, printed in sequence.** L3919 withdraws every
  seed size in the two sections; L3823, L3832 and L3877 mark three of them in place; the family table
  L3814–3818, the four-index table L3850–3854, the L3880 headline (`A counting axis costs the seed one
  cell. A coupling axis costs five`), the L3886–3888 Λ₁₃ projection and the L3903–3906 three-point table
  are **not** marked, and all five are seed sizes or fitted to them. Register 497 is cited affirmatively
  at L3915 and withdrawn at L3946, eight lines apart, inside one section.
- L3915's `Register 497` and L3946's withdrawal of `497 through 500 and 502` are the same entry; Register
  511 (L1907) is itself a correction of §14.5.8's headline, and Register 501 (L1867) survives, as L3955
  says.
- The four synthetic indexes of L3850–3854 (audit, register, reference, bibliography) are reconstructions
  the section itself discounts at L3856–3860; their coordinates and constraints are printed in no member,
  so the `predicted` column is not re-measurable. Only the audit row is offered as a test, and 13j-10
  shows the register row's comparison target is empty.
- `24,585`, the true count of minimum covers, has six existing sites in the Mathematical Compendium and
  Physics Compendium — all of them a different object; do not conflate at R3.
- §14.6.3's `the Mathematical Compendium prints the live count, register 1739` resolves: Register 1739
  (L6465) is the eighteenth-root entry and does correct stale root lines to the file.
