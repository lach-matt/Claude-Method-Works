# READ-ch2 — Phase R2, main Chapter 2 "The protocols" (member L568–1002), chat 69, against BUILD90 main / BUILD93 compendia

Labels as READ-ch1: MEASURED · INFERRED · record-carried. Line numbers member-relative (main; R = Register member). Nothing was corrected.

## A. Deviations and defects (numbered)

**D2.1 — the withdrawn 2,475 survives at L914.** MEASURED texts. Census C7 (the L3477 row's "two other main sites") — confirmed for this site.
Withdrawal, §14 L3476–3478: "it breaks the factorisation by **15,150 cells at Λ₁₂ and 45,450 at Λ₁₃**, 21.4% and 22.8% of the product — recomputed; the 2,475 previously printed here is withdrawn." Chapter 2 L913–914: "The tight K has two parents and costs the cylinder 2,475 cells." (The other survival is L3434, Chapter 14's read.)

**D2.2 — the ten §30.3 failures tallied as twelve.** MEASURED (kind column, L684–699).
Table kinds as printed: upper, lower, negative, structural, upper, method, negative, lower, structural, structural = 2 upper · 2 lower · 2 negative · 3 structural · 1 methodological = 10. Prose L701: "Two lower bounds, two upper, two negatives, **five** structural, one methodological" = 12.

**D2.3 — the §30.3 grid: "eight empty cells" against four.** MEASURED (L737–744).
L732: "An open question with eight unfilled requirements"; L734: "Worked on §30.3: eight empty cells, four rows deep, at d ≥ 3." The grid has eight requirements (rows) and four "·" cells (characterisation, decision procedure, hardness, data structure at d ≥ 3). L746 "Three rows are full at every d" leaves the NO-certificate row (both cells filled: "Tucker — unbounded" / "unbounded") unclassified.

**D2.4 — "The seven prime audits of §3.1–7".** MEASURED (Ch. 3 headings).
L878–879: "**The seven prime audits of §3.1–7 test computable claims**". Chapter 3 is titled "The twenty-two prime audits" (L1003); §3.1–3.8 are narrative sections (L1219–1366), §3.7.1 "The twenty-first audit — INPUT"; §3.8's table has seven audits only "as first stated" (L1371). Stale. Related: L995 "the twenty write their state" and Ch. 3 L1112 "The twenty, with their coordinates" against the title's twenty-two — the audit count is to be settled at the Chapter 3 read.

**D2.5 — "E(audits) at 11, 0 and 19" is a stale partial list.** MEASURED texts.
L857–858. §3.8 table L1370–1381: 11 (7 audits, 3 coords) · 0 (18 audits) · 19 (18 audits, 4 coords) · 18 (19 audits) · 17 (20 audits); L1385: "E(audits) read 11, then 0, then 19, then 17". The two latest values are absent from Chapter 2's list, and no value is printed for 21 or 22 audits.

**D2.6 — §3.8 does not end as Chapter 2 says.** MEASURED (grep).
L841–842: "§3.8 ends by saying a coordinate system answers to two masters and only one of them is computable." §3.8 (L1366–1434) ends on the audit script ("it cannot audit itself … Register 300"); "masters" — 0 hits in the main volume.

**D2.7 — §28.7.6/§28.7.7 counts stale against the current headings.** MEASURED texts.
L963–966: "§28.7.6 was titled 'Three from the tower session' and contained eighty-six entries, 199 to 284 … It is now four — the tower's three … and §28.7.7 the eighty-seven written afterwards." Current L7677: "28.7.6 Two from the tower session and its repair, in the collaborator's hand"; L7678: "28.7.7 The results of the sessions after the tower — 119, printed individual…". Also 4 + 87 ≠ 86 (284 − 199 + 1 = 86 reproduces).

**D2.8 — the §30.3 characterisation is printed only here.** MEASURED (grep).
L705–706: "X is ℛ-closed iff X = {(r,c) : c ≤ M(r) and r ≤ N(c)}, with M, N the running maxima of its own row and column maxima." §30.3 (L8399–8574): "closed iff" / "running maxim" / "row and column maxima" — 0 hits; the only "closed iff" sites are Theorem 14.1 (L3104, L3683) and §17.2 (L4795, L4800). A worked section that does not state the result it is worked on.

**D2.9 — 39 % / 49.5 % without a pointer.** record-carried; source MEASURED.
L823–825 and L821 "three corrections were caught in a single session": no site in main outside Chapter 2; Register 187 (R L813) carries "Measured: 39% at d = 3 and 49.5% …". Chapter 2 cites no entry.

**D2.10 — "six properties confirmed" against seven listed.** INFERRED count; properties MEASURED.
L769–772 lists E = 0, sublattice, rank-modular, exact projection onto Λ₈, constraint graph a tree, F extended by one pendant factor, F(−1) = 2 unchanged — seven — then "six properties confirmed". On the rebuilt Λ₉ (l-ch2.py): 1,654 cells; exact projection; F(−1) = 2; join/meet closed on all 1,367,031 pairs (sublattice, E = 0 — stronger than the printed 200,000-pair sample); rank-modularity identically true for coordinatewise max/min with rank = Σxᵢ; the pendant edge is 2S′ ≤ g by construction.

**D2.11 — overlapping Register ranges.** record-carried. L879–881: "the seventeenth through twentieth entries … and the twentieth through fortieth" — the twentieth is in both; Register 277 cited.

**D2.12 — "Nineteen quantities" (L852).** Note. The list L852–859 separates eighteen items by semicolons (nineteen if "closure through the f shell … and exhaustively to 47,775,744 ambient ones" counts two).

**D2.13 — "Si I to four cells and P II to one" (L572).** record-carried. No site states these counts (grep "Si I…four", "P II…one"); §5 L1469 names Si I, P II as the instance. Appendix B's read settles it.

## B. Reproduced (no deviation)
r = 2Z²R/(ν³σ) ≥ 5 (L6170) · ν_V = (3Z²R/5q)^{1/4} (L6607) · Ne II fails at five J levels and two shells; Ar II five and three; Bi I five and five (L6708) · 27 admitted · 12 exceptional depth · 5 excluded (L6848) · four refusal verdicts, §23.11 (L6519) · ρ ≤ 3/n at 95 % with no certification of ρ = 0 (rule of three; statistically exact) · 0.09σ, no shared step (§16.4 L4426) · 153 channels (Appendix B ×2, L1480, L3406) · 1,635 entries (worded) · §28.8 "36 cells, closed, E = 0" (L7740) · §25.6 the one deduction · §30.4's five enumerations = 1 + 1 + 3 · E(periodic table) = 36 · Λ₉ figures (above, l-ch2.py) · |Λ₈| = 976, E(Λ) = 0 over 475,800 pairs · 131,072 = 2¹⁷ · 47,775,744 (L2942) · 499,246 (L8900) · 2,354 interval sets (L8467) · 150 of 216 (§16.3.1 L4396) · 86 = 284 − 199 + 1 · Appendix E item H (L10952) · Registers 219–222 (grouped heading R L1323), 232, 270, 275, 277, 278, 286 (grouped R L1319), 343, 407, 432 all present · §3.8's E(audits) table exists (L1370).

## C. Format (production)
Fixed-width tables at L672–674, L683–699, L736–744, L756–762, L780–785, L802–813, L923–929 with wrapped cells ("negati/ve", "struct/ural", "metho/d"); "\|Q\|" escapes at L772.
