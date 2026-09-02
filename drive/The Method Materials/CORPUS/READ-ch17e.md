# READ-ch17e — chat 130 — main volume L9892–L9936 (Chapter 36, closed)

**Unit.** `## 36. Three bodies, and what a complete index is allowed to say` body L9892 to `# APPENDICES` L9937: §36.1
L9896 · §36.2 L9900 · §36.3 L9904 · §36.4 L9924 · §36.5 L9928 · §36.6 L9932. **45 lines**; closes Chapter 36 and
the main volume's chapters. BUILD90 live. Instruments **r2-ch17e** (computable, 104 output lines) and **r2-ch17f**
(prose, 69), both banked; r2-ch17e imports r2-tb1 (this chat's intake golden) by path. Main volume now **83.8 % read
at L9936 of 11,855** (MEASURED: 9936/11855 = 0.8381, HALF_UP 3 places).

**Boundary, MEASURED by own heading scan.** `## 36.` hits [159, 9892] (contents, body); `# APPENDICES` [161, 9937].
`section_span(M, '36')` = (9892, 11856) — it steps into the appendices and was not used; the six `body_range`s tile the
unit after the italic opener L9893–L9895. Agrees with HANDOFF-82.

**Prints & Proofs.** PP carries no `## 36.` and no `### 36.1` (0 body occurrences). The unit is post-PP: stated once,
not diffed. PP does carry §21.5.1 (P5647: treewidth 2, strong 3-consistency, *exactly one level*) and §12.11.2
(P3333), which witnesses L9934's *the book had already computed that precision before the problem was posed*.

## A. Deviations

### 17e-01 — `tb_audit.py` (1756) at L9902: a citation with no Register entry, and a script name in a reader-facing line
**Volume L9902:** *… the six are named A–F in the paper's §8 audit paragraph and rerun by `tb_audit.py`, 1756).*
**Register:** 1755 and 1758 exist; **1756 ABSENT** (Register lines containing `tb_audit`: none). The 78/78 lives at
1717. The companion paper member cites the same absent entry at its L146 (`1756`, `tb_audit`), and REQUEST-THREEBODY.md
item 1 carried it. Two classes at one site: **docket 9(c)** (citation with no entry — 1710's kin, 17b-01) and **docket 6**
(Ruling 46: the only backticked script name in the unit). The delivery names the file `audit.py` (README object 1).

### 17e-02 — L9914 *§31.1.1 had already named the brackets: zero-velocity surfaces, Hill regions, KAM tori* — the target says nothing of two of the three
**§31.1.1 (L8618–L8650):** *zero-velocity* 0 · *KAM* 0 · *Hill* 3 (Hill stability L8626, Hill radius L8628, L8633).
**Where the claim lives:** §18.4.1 **L5155–L5156** — *Jacobi's zero-velocity surfaces, Hill spheres and KAM tori are all
brackets in §22's sense.* Main sites of KAM: L5156, L9914, L11832 (R.7); of zero-velocity: L5155, L9914. **Docket 9(b)**
(citation whose target says nothing of the claim), with the wording pair *Hill regions* (L9914, companion 1) / *Hill
spheres* (L5156) for docket 34.

## B. Verified findings

1. **§36.2's figures, every one, against 1716/1717/1718/1719 and the intake golden.** 13 × 6 = 78; cap 8 = 344 / 8,385
   meet / 0 join; the printed caps 3–12 list (10 values) equals r2-tb1's own operator at every cap; join 0 throughout;
   two-body chain 0 at every cap (the delivered operator counts *either kind* in one number — convention named).
   The per-cap list has no Register site (*90,705*: main L9902 only); 1716 carries the cap-8 triple and *caps 3–12 as in
   `3B.tri`*. *One inherited polynomial wrong, replaced* = 1719's withdrawal.
2. **Register existence.** 1713–1724 all present (L9894's range); every entry the unit names (784, 1713, 1717, 1718,
   1722, 1723, 1724) present except 1756 (A). No WARNING on any of 1713–1724. Two *Registers* cites (counted), two
   lowercase *register* names (G0i).
3. **Pointers to the claim.** §31.1.1 carries *nothing here touches Poincaré* verbatim (1) and the threshold L8642–L8644
   (μ < 0.0385209, *silent on thresholds*; Routh unnamed there or anywhere in the six volumes); §12.11.2 carries
   join-closed / meet-broken / sum / difference / symmetric; §21.5.1 L5692–L5693 treewidth 2 / strong 3-consistency /
   ℛ reaches level 2 / *exactly one level*; §25.6 L7041 *E(Λ) = 0: the index proposes none*; §18.4.1 *realised
   closure* 3, *certificate* 9, and its open-object table L5022 has **5 DATA rows** = *the book's own five* (L9908);
   §12.11.3 *dichotomy* / *envelope*; §12.11.1.3 *time column* / *moves* (its heading is the claim); §12.11.0.2
   *clock* / *assumption*; §12.11.4 (5 lines) *path-dependent* / *physics is not*; §14.5 *seed* 31; §2.14 *computed* /
   *written*; §E.5 body L11143; audit 7 among §3's seven described audits (17c B5).
4. **Count words.** L9906's strata list = 5 items = 1713's *FIVE ASYMPTOTIC CLASSES*; *five points* = 3 + 2; *13 of 13* =
   1718; *wrong in two coefficients*: U⁴ and U² both differ from the norm (1719 names both); *order 6, 2 or 1* = the
   mass-preserving permutation group's order at three / two / no coincident masses (r2-tb1: realised 1 · 6 · 6 cases);
   *cannot … close a meet, or open a join*: join 0 and meet > 0 at every cap 3–12 under the mass-free operator.
5. **Arithmetic.** (9 − √69)/18 = 0.0385209 at 7 places HALF_UP (L9918; also L8642, PC L332). c_ij as printed is the
   coded `(m[i]*m[j])**1.5/np.sqrt(m[i]+m[j])`.
6. **Rulings 45/46, first person, structure.** R46: one site (17e-01). First person zero (probe carries mine/myself;
   witness fires on 1723). Ten bold lead-ins read as paragraphs: nine in §36.3, each opening with a § pointer to ten
   distinct sections; the tenth is §36.4's *Mass-uniformity.* Whole-line italics L9894, L9934; no tables, rules or
   unmarked sub-headings; 9 lines over 400 chars; **docket 27: 0 of 45 recurring** (twenty-fourth consecutive clean unit).
7. **§36.5's negatives, each with a witness.** *No trajectory*: the only hits are the negative itself (L9906 *no
   trajectory formula exists*; companion L164 *the absence of a trajectory formula*). *No prediction*: 0 positive
   predictions in unit or companion. *No extension to n ≥ 4*: the only n ≥ 4 hit is the clause itself. *Nothing that
   touches Poincaré*: L9898 (quotation), L9894/L9930 (the negative), companion L13/L207 (scope). ℳ_per: the negative
   only; Moore and Chenciner in the companion.
8. **Cross-volume phrases.** *coordinates come from the subject or from nowhere* (L9926) has one Index of Indices site
   (IoI L1557) and one companion site; not marked as a quotation. *envelope precision only* (L9898) reads on the join
   at §18.4.1 L5154–L5155; L9898 attributes it to §12.11.2, whose span carries *envelope* (2) — the fuller sentence is
   §18.4.1's L5152–L5154 (incidental, C3).
9. **The companion paper member** (216 lines) carries 78 of 78, 344, 8,385/8385, 90705, 0.0385209, 13/13 (4), *thirteen*
   (5), *order-type* (4), Mass-uniformity (3), Brudno, Saari, Painlevé, Xia, *measure zero*, *figure-eight*, *resolvent*,
   *hyper-radius*; names checks A, B, E as *check X* (C, D, F by other forms); Routh 0.

## C. Incidentals

1. **Wording pair (docket 34):** L9902 *Eight attribution questions, eight closed* / 1721 *seven closed to named owners*
   / L9922 *Seven belonged to others; the eighth … turned out to be classical* — eight = seven to others + one to prior
   art (1720 Lagrange 1770); both counts reproduce under their own convention; no figure moves.
2. **Count word without a witness in the volume (docket 17):** L9908 *a fourth open object outside the book's own five* —
   the three earlier outside objects are not named anywhere in main (the phrase's only site is the unit).
3. L9898 attributes *envelope precision only* to §12.11.2; the sentence is §18.4.1's (B8).
4. *six numbers* (L9926): three c_ij scalars + three rays b_ij — a ray is a unit vector on S²; the count is of objects.
5. **Docket 36 (unbibliographed):** **Xia** (L9930, *Xia 1992*, n = 5) has no References-body or R.7 line — sole site in
   the six volumes. Also absent from the References body L11503–L11805 while present in R.7: Saari, Painlevé, Brudno,
   Montgomery, Chenciner, Jacobi, Maupertuis. **Routh** unnamed anywhere (the threshold is printed at three sites
   without its author).
6. Ruling 45 candidates in the unit — *register* (L9894, L9902, L9922: the Register itself), *audit* (L9902, L9920 ×2,
   L9922), *rerun* (L9902), *run* (L9920), *ledger* (L9922): the chapter's declared subject is the method's own run on
   the problem, as §34.10 and §35.4 — recorded for chat 115's split (docket 5).
7. **1725 ABSENT** (17b-01's neighbour); no unit site cites it.
8. The reconstruction-versus-record ledger (docket 37) gains two entries from the intake: intake1-01 (13 labels, 12
   orderings) and **intake1-04** (the reconstruction's withdrawn constant term also differs from the norm — three
   degrees differ, the record prints only the U⁴ term and calls U² *likewise wrong*; *two coefficients* is untestable
   against the record beyond those two). Findings about the reconstruction; flagged to the three-body project.
9. L7000 (§25.6) is a post-PP forward pointer to Chapter 36 (*E(Λ₃) = 0 … Brudno's theorem*) — 1714's text; not a
   unit site.

## Instrument faults (self-caught, rewritten in place before banking)

- r2-ch17e fault 1: *two coefficients* was asserted as a literal (`'two coefficients:', 2`); rewritten to compute the
  differing degrees — which exposed the third (intake1-04). Fault 2: §21.5.1's *level 2* test failed on bold markup;
  rewritten markup-stripped. Fault 3: §25.6 was probed for *E = 0*, which the section writes as *E(Λ) = 0*; rewritten.
  Fault 4: *the book's own five* was probed as a token; rewritten to count the §18.4.1 table's DATA rows. Fault 5:
  §31.1.1's brackets were scored 0 without locating the claim; rewritten to find its home (17e-02). Fault 6: seven
  §36.3 paragraph labels printed one line low (M[] indexes right, labels wrong); rewritten. Fault 7: the companion's
  title was read from a blank first line.
- r2-ch17f fault 1: the §36.3 lead-in count included §36.4's; restricted to the section. Fault 2: the recurrence test
  counted the chapter heading's contents entry; headings excluded. Fault 3: two negative-witness sites (L9906, companion
  L164) were listed unread; read and stated.
- CENSUS-CLOSURES-ch17e.tsv row 1200's first draft cited *8,385* sites not measured; deleted and rewritten on *90,705*.
