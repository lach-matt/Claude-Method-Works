# READ-ch18a — chat 131 — main volume L9939–L10053 (Appendix A, part 1: opener, A.3, A.8–A.13)

**Unit.** `## Appendix A — Proofs` body L9939 to `### A.15` L10054 (split at an A.n boundary; the whole appendix is L9939–L10164,
226 lines, larger than one cadence unit). **115 lines**; seven proofs, each with its Statement and ∎. BUILD90 live. Instruments
**r2-ch18a** (computable, 166 output lines, 20,364 B · d5b741a9) and **r2-ch18b** (prose, 70 lines, 9,256 B · 0d29a486), both
banked and re-run deterministic. Main volume now **84.8 % read at L10053 of 11,855** (MEASURED: 10053/11855 = 0.848, HALF_UP 3 places).
Part 2 (A.15, A.18, A.19, A.19.0, A.19.1: L10054–L10164, 111 lines) is the next unit.

**Boundary, MEASURED by own heading scan.** `## Appendix A` hits [162, 9939]; `## Appendix B` [163, 10165]; twelve `### A.n`
headings inside the appendix (ten one-dot, two two-dot). `lettered(M, 'A.1')` = [] — A.1 has no heading, only a table row.

**Prints & Proofs (the appendix is pre-PP; r2-ch18a §10).** PP `# APPENDICES` P9590; PP's appendix heading is `# Appendix A` and its
A.n headings are unmarked plain lines (P9609 A.3 … P9688 A.13). All seven section titles equal after stripping the number; all seven
Statement first lines equal. **Three post-PP rewrites inside the unit:** (i) the opener — PP *Ten proofs … The remaining seven …
seventeen in all* → volume *Nine … ten … nineteen* (PP's own table had nine rows and ten sections; the volume's count is exact,
§1); (ii) **A.9's proof was replaced**: PP argued that a non-antichain interval "decomposes as a direct product with a chain factor
of length ≥ 2" (false in general); the volume argues by the crosscut theorem (Rota 1964) — the rewritten proof reproduces (B3);
(iii) A.8's two displayed equations and A.10's two leaf formulas are one line in PP, two in the volume (layout only).

## A. Deviations

### 18a-01 — the index row `A.6 adjunction never repairs closure — §24.2, in full` (L9950): the target says nothing of the claim
**§24.2 (L6653–L6667, both resolvers coinciding):** *The largest contributors* — a seven-row species/cells table and Figure 24.2;
hits for adjunction / adjoin / repair / closure: **0**. **Where the claim lives:** §17.2 **L4806** *Theorem 17.1 (adjunction never
repairs). For any h : S → H, with S′ = {(x, h(x))}: S′ closed ⇒ S …*; Appendix D L10558 itself says *Theorem 17.1 is A.6*. The A.11
proof (L10018) cites A.6 for exactly this theorem. **Docket 9(a)** (wrong target), a second misdirected row beside 13l-03's A.7 →
§16.3 (re-measured: *may precede* 0 in §16.3, 3 in §15.3). DEFERRED's *the other eight rows resolve correctly* (C1/ch13n) was not
measured for this row; A.1, A.2, A.4, A.5, A.14, A.16, A.17 resolve (r2-ch18a §2: 1 / 1 / 5 / 5 / 2 / 7 / 2 hits).

### 18a-02 — A.12 Consequence L10035 sends *the antiprotonic-helium cells* to **§25.6**, which carries none
§25.6 (L6991–L7117): *antiprotonic* **0**. The cells' sites: §2.8 L612, §16.4 (per 14h-05), §19.2 L5401/L5416 (the worked case and
Figure 19.1), §22.3 L6135, §32 L8793. L6135 is the same sentence word for word (*This is not a technicality — it is what allowed
the antiprotonic-helium cells of §25.6, where the relevant threshold is ambiguous*) — **14h-05 holds it (a target must be chosen,
not corrected); the appendix site is its second member.** Docket 9(a), twin site; with 14h-02 (*ν, δ and V all require I*, L6133 /
L10035) the two Consequence sentences move together.

### 18a-03 — A.13's Statement says *iff*; the proof says *to leading order*
**Statement L10038–L10041:** *The bracket fails at a cell iff a perturbation displaces the level by more than half the local spacing:
|ΔT| > 2Z²R/ν³.* **Proof L10043:** *… so the half-spacing is 2Z²R/ν³ to leading order.* MEASURED (Decimal, R = 109,737.316, Z = 2):
the interval [T(n+1), T(n−1)] is not centred on T(n); the smaller one-sided gap is **0.775 × 2Z²R/ν³ at ν = 5.3** (4,567 vs 5,897
cm⁻¹), 0.656 at ν = 3, 0.811 at ν = 6.6. A displacement between the one-sided gap and 2Z²R/ν³ reorders the level while the Statement
says it cannot. The substance (an O(1/ν) statement) is right; the *iff* is exact only to leading order. Docket 12 (a truncation
printed as an equality) / docket 34 wording; the Inversion's *|ΔT| < 2Z²R/ν³ … an upper bound* inherits the same caveat.

## B. Verified findings

1. **The opener's count.** Table DATA rows 9 (A.1, A.2, A.4–A.7, A.14, A.16, A.17); one-dot `### A.n` sections 10; 9 + 10 = 19; the
   two label sets partition A.1–A.19 exactly (C1/ch13n re-measured: the nine rows are exactly the statements without a section).
2. **A.1 and A.3 on the rebuilt lattice.** Λ₈ (976) closed under ∨ and ∧ on all 952,576 ordered pairs; every one of the 255 non-empty
   projections π_F(Λ₈) closed (convention: componentwise ∨/∧ of every pair in the set). The Remark's converse witnessed by
   {(0,1),(1,0)}: both projections closed, the join absent. §18.4 carries *projection* at L4983–L4994.
3. **A.9 on Λ₈.** 115,162 comparable pairs, 3,749 covering; **17 join-irreducibles** (L2017's *17-element poset*, A.19's *seventeen*);
   distributive identity on 20,000 seeded triples; Birkhoff check exact (976 distinct down-sets, x ≤ y ⟺ J(x) ⊆ J(y) on all pairs);
   **recursive μ = antichain formula on 200 of 200 seeded comparable pairs** (intervals of 2–319 cells), values {−1, 0, 1}; μ = −1 on
   all 3,749 covers; formula non-zero on 18,103 of 115,162; the crosscut clause (μ = 0 ⟺ Q not an antichain ⟺ atoms' join ≠ top)
   holds on the 140 non-covering test pairs. The *47 comparable pairs* has no population and no Register site (main L2017, L9996).
4. **A.10.** The seven binary Heaviside constraints as tower-2 codes them (l≤n−1, k≤4l+2, q≤k, f≤e−1, g≤4f+2, g≤q, 2S≤k) give 7
   edges on 8 nodes, connected — a tree. Direct count = factorised count on **40 of 40 seeded boxes and the full box (976)**; both leaf
   formulas' bounds hold on every cell and are attained. *Eight random intervals* (L2071, L10013): no population, no Register site.
5. **A.8.** On the 28 coordinate-pair projections of Λ₈: necessity 28/28; may-precede total on 28/28; **antisymmetry fails on 19 of
   28** (ties where two fibres coincide) — 13l-01 stands at the appendix site: the relation is a total *preorder*, and *that order is
   the relabelling* is non-unique under ties. Sufficiency on 914 of 914 seeded sets whose relation is total. *120 / 274 of 274*: no
   population, no Register site (L4302, L9981).
6. **A.11.** Under δ = f − ℓ (§17.3), ν(x∨y) ≠ max(ν(x), ν(y)) on 262,656 ordered pairs — the Statement's witness. *86 violations*:
   9,894 comparable / 384 covering decreases at Λ₈ — 13t-04 stands (fifteen readings, none 86). *ν grades every chain*: 384 covering
   steps decrease ν under that δ; 13t-05 holds the definition open — recorded, not re-scored.
7. **A.12.** The min/max reversal is an identity (I cancels); 5,000 of 5,000 seeded Decimal triples. *ν, δ and V all require I* —
   14h-02 (L6133 twin). Part V heading L5937 (*the bracket of Part V*).
8. **A.13's figures.** d/dν(Z²R/ν²) = −2Z²R/ν³ exact; ν_fail = (2Z²R/|ΔT|)^{1/3} = **6.639 → 6.6** at Z = 2, ΔT = 3,000 cm⁻¹, R =
   109,737.316 (main L5987, L11846); 4.2 at Z = 1 — the §25.6 table L6942 prints *4.2 | 6.6*. *ν = 5.3* at L6936/L6947 (Hg II).
9. **Pointers.** A.2 → §14.1 L3683 *Theorem 14.1 (A.2). X is closed iff X = ℛ(X)*; A.4 → §16.1 (ⅅ, 5); A.5 → §16.5 (χ, 5); A.14/A.16 →
   §12.11.2 (envelope 2, triangle 7); A.17 → §12.11.3 (dichotomy 2; *per coupling axis* L3401 — A.16 is not named there). Rota 1964
   and the crosscut theorem are in the References body L11664–L11665 (named as §A.9's); Birkhoff has a References line.
10. **Rulings 45/46, first person, structure, recurrence.** R46 zero (no backticks, scripts, builds). First person zero: the four
    `I` hits are the ionisation limit. Sixteen bold lead-ins (Proof., Verified, Measured., Consequence., Inversion., Critical depth.,
    For Λ); no italic whole lines, no markdown tables (the three `|` code lines are absolute-value bars), no unmarked sub-headings;
    seven Statement / seven ∎; two lines over 400 chars. **Docket 27: 0 of 40 sentences recur** (twenty-fifth consecutive clean unit);
    the appendix's Verified lines restate L2017 / L2071 / L4302 / L4971 by design.
11. **Negatives witnessed.** *converse fails* (B2); *no inclusion–exclusion* (B4); *equivalent for any I* (B7); *no channel in this
    work enters the failure regime* — the §25.6 ν_fail table L6940–L6945 and L6947 (single witness, docket 17 kind).

## C. Incidentals

1. **A.10's "leaves 2S and g":** in the constraint tree g has degree 2 (neighbours q and f); the factorisation still holds because g
   is innermost with both neighbours fixed. Wording (docket 34).
2. **A.13's *anticorrelated in nature*** (L10051) is an empirical universal with no population in the unit; its §25.6 sites L6839,
   L6950. Docket 19 kind, recorded with 18a-03's site.
3. **Register:** no entry names A.3 or A.8–A.13 (1321 names *A.8–A.11* as ledger rows, an audit entry); the appendix cites no entry;
   the words Möbius, crosscut, may precede, limit-free, ν_fail have no Register line; *tree factor* entries 228, 347, 353, 394, 1359,
   1488 and *join-irreducible* 70, 75, 467 carry no WARNING.
4. **Ruling 45 candidates** — *Verified* (L9981, L9996, L10013), *Measured.* (L10020): the appendix's declared form for its own checks;
   chat 115's split (docket 5).
5. A.3 L9963 *Meets are identical with ∧ throughout* — reads as "the meet case is identical, with ∧" (wording only).
6. Rota is absent from R.7 and from the Register; §A.9 is his only citing site in the six volumes (the References line is present).

## Instrument faults (self-caught, rewritten in place before banking)

- r2-ch18a fault 1: a syntax error on the A.10 leaf-formula line (unbalanced parentheses); rewritten as three statements. Fault 2:
  A.2's probe matched only `ℛ(X) = X` and scored §14.1 zero; the section prints `X = ℛ(X)` — rewritten to both forms (the book was
  right, the instrument wrong). Fault 3: the §25.6 probe reported zero without locating the cells; rewritten to print every site with
  its enclosing section (18a-02).
- r2-ch18b fault 1: the markdown-table probe fired on three code lines whose first character is the absolute-value bar; read and
  excluded. Fault 2: *a cylinder over ν and not one graded by it* was tested with its bold markup unstripped and scored 0; rewritten
  markup-stripped (1). Fault 3: the Birkhoff verdict was printed as a conditional; rewritten as the measured verdict.
