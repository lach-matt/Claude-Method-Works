# READ-ch1 — Phase R2, main Chapter 1 "The principles" (member L241–567), chat 69, against BUILD90 main / BUILD93 compendia

Labels: MEASURED (command or instrument named) · INFERRED (my reasoning; not a measurement) · record-carried (the printed figure rests on the Register or another chapter, not re-measurable here). Line numbers are member-relative (The_Method_1_6-2.md; Register member = R). Nothing was corrected.

## A. Deviations and defects (numbered)

**D1.1 — the seven operations, two incompatible lists.** INFERRED from MEASURED texts.
L291: "**Seven are operations** — P3, P4, P5, P6, P11, P14, P15 — and §5's table is their evidence." L292–294: "Six of the seven have a recorded failure behind them; **P16 is the exception**". L345–355 "Procedural — seven": P4, P5, P6, P11, P14, P15, P16. §5 L1503–1509: P16 "is the only one in this book that is" corroborated by construction; "Register 421". The L291 list excludes P16 and includes P3, so "P16 is the exception" among "the seven" cannot hold as printed; the Procedural table's seven is the set §5 describes.

**D1.2 — relations counted as mechanisms.** INFERRED from MEASURED texts.
L307–308: "**Two are relations** — P7 and P17 … a relation is not a mechanism." L311: "**And four mechanisms were stated without something they need.**" followed by P2 (L313), P7 (L320), P17 (L329), P22 (L336). P22's expression is "—" (L370–371), so under the chapter's own taxonomy (mechanism = has an expression, L282–288) it is not a mechanism either.

**D1.3 — the Formalised table prints expressions the prose withdraws.** INFERRED from MEASURED texts.
Table L254 P7 "∃N : Ω_N = ∅ — terminal, not monotone"; L275 P17 "following a bound costs 1/N of searching the volume". L307–309: both "lose their expressions"; L333–334: "The corrected form carries no N". The table is left in its pre-correction state.

**D1.4 — P2 strengthened from implication to equivalence.** Texts MEASURED; logic INFERRED.
Source §16.1 L4344: "Corollary. dim q > dim p ⇒ ⅅ ≥ 1." Chapter 1 L314: "**ⅅ ≥ 1 exactly when dim q > dim p**". R417: "ⅅ ≥ 1 requires dim q > dim p". With ⅅ = dim q − rank ∂Φ/∂p the converse needs rank ∂Φ/∂p = dim p; a rank-deficient Jacobian gives ⅅ ≥ 1 with dim q ≤ dim p. §16.1 states only the valid direction. The figures dim p = 4, dim q = 6, rank 4, ⅅ = 2 reproduce §16.1 L4347 exactly (MEASURED grep).

**D1.5 — P9's "where" is the wrong section.** MEASURED (grep).
Table L258: P9 → §24.2. §24.2 "The largest contributors" (L6653–6700): rank / log / P9 — 0 hits. rank(log q) = 1 is printed once, at §26.1 L7145, with "fifteen Rydberg quantities and forty values of ν" at L7142; Chapter 1's own prose (L297) cites §26.1. Census C1 missed it because §24.2 exists.

**D1.6 — P1's and P2's "where" appear crossed.** MEASURED (grep); crossing INFERRED.
Table L246–249: P1 ℛ(Λ) = Λ → "§16.1, Ch. 8"; P2 ⅅ → "Ch. 9". §16.1 (L4335–4358): ⅅ 5 sites, ℛ 0. Ch. 9 (L1936–2020): ⅅ 0, ℛ(Λ) = Λ 0. Ch. 8 (L1796–1935): ℛ(Λ) = Λ / self-referencing 0. ℛ(Λ) = Λ is printed at L15 and L2240 (Ch. 11). §16.1's content is P2's; neither Ch. 8 nor Ch. 9 carries the expression cited to it.

**D1.7 — P12's "where" carries no ρ.** MEASURED (grep).
Table L264–267 (wrapped): P12 "ρ = 0 certain ⟺ n = |Λ|" → B.2. Appendix B.2 is "Channels" (L10190); ρ in Appendix B (L10165–10229): 0 hits. ρ is defined as retrieval redundancy at Ch. 19 L5390 (and L357 cites Ch. 19 for it). The expression has no source at the cited pointer.

**D1.8 — unsourced figures: 120 sublattices, 40 intervals.** MEASURED (grep).
L546–547: "475,800 pairs, 120 sublattices, 40 intervals, six construction rules, twenty-eight projections." Neither "120…sublattice" nor "40/forty…interval" occurs in main outside Chapter 1 or in the Register (patterns: sublattice within 40 chars of a 2–3-digit number; interval within 20 chars of 40/forty). 475,800 = C(976,2), 28 = C(8,2) (l-ch1.py); six construction rules L742.

**D1.9 — unsourced sequence 5 → 4 → 3 → 4 → 3 → 7 → 3 → 3.** MEASURED (grep).
L279: "across this work it ran 5 → 4 → 3 → 4 → 3 → 7 → 3 → 3." No site in main or the Register; Appendix E (L10898–11221) carries no open-count series.

**D1.10 — the 13 → 10 movement contradicts the cited section.** MEASURED texts.
Chapter 1 L324–326: "Checked against §29.2.1's own movement, where six items' stake fell to nothing: the count went 13 → 10 and the multiset decreased". R418 L1557: "Verified against §29.2.1: count 13 → 10 while the multiset strictly decreased." §29.2.1 L7911–7916: "**six of the eleven items in Q had novelty as their only stake** — B, C, F, G, K and N … Those six now block nothing. They remain open … Q loses more than half its stake while **losing none of its length**." Appendix E L10961: "Every *blocks* value of *novelty* fell to *nothing* under §29.2.1 — six of the thirteen." Three counts (eleven / thirteen / 13 → 10) and two statements about the length (fell to 10 / did not fall). Chapter 1 carries R418's figure; the cited section says the opposite.

**D1.11 — "§16.3's five failures".** MEASURED (grep).
L565: "§16.3's five failures are all of the same kind". §16.3 + §16.3.1 (L4359–4406): one worked case (Al II, K II, 56 of 56); "five" 0 hits (only "Referee flag 5"). The count is not in the cited section.

**D1.12 — "§30.3. Twenty-two formulations".** MEASURED (grep). Minor.
L526. §30.3 (L8399–8574): twenty-two / 22 / formulation — 0 hits. The count is printed at L751 and §5 L1495 ("§30.3, 22 formulations"). Attribution of the case is right; the count is sourced elsewhere in main.

**D1.13 — "spin multiplicity 2" names the possible state, not the impossible one.** INFERRED (physics); cell MEASURED.
L475–477: "y = (n=1, ℓ=0, k=1, q=0, e=1, f=0, g=0, 2S=2) — one electron with spin multiplicity 2, which no atom has." Same wording at §16.7 L4621 and §16.8.2 L4665 (Chapter 1 reproduces its source). 2S = 2 is S = 1, multiplicity 2S+1 = 3; a one-electron atom has multiplicity 2 (doublet). The impossible feature is S = 1 for k = 1, which is what the constraint 2S ≤ k (§7.1 L1760) forbids. y ∉ Λ₈ (l-ch1.py). Wording at three sites.

**D1.14 — the forged rule's 225 needs an unstated cap.** MEASURED (l-ch1.py).
L504: "2S ≤ k becomes 2S ≤ k+1, admitting 225 cells". On the rebuilt Λ₈: 2S ≤ k+1 within the box (2S ≤ 3) admits exactly 225 new cells (|X| = 1,201); uncapped it admits 319. The figure is right under the box cap, which Chapter 1 does not state.

**D1.15 — deletion/addition figures with no source.** record-carried; source MEASURED absent.
L448: "30 deletions, 0 failures. 20 additions, 20 absorbed. Fixed point exact at 976." Only site in the main volume is L448 (grep "30 deletions|20 additions|20 absorbed"); no Register pointer; not re-measurable from Chapter 1's text (the closure operator "intersection of all valid such bounds" is not specified here — §16.4's form; to be measured at the Chapter 16 read).

**D1.16 — "no register entry" beside a Register entry.** MEASURED texts. Wording.
L293: P16 has "no register entry"; §5 L1504 the same, then L1509 "Register 421"; R421 L1569: "P16 IS CORROBORATED BY CONSTRUCTION AND BY NO FAILURE … having three realisations and no register entry". The intended sense is "no failure entry"; as printed it is contradicted by the citation.

**D1.17 — P21 table "rank(x) 13" names no x.** Note, MEASURED.
L427. rank = Σxᵢ (Ch. 9 L1947); on the rebuilt Λ₈ rank runs 3–20 and 100 cells have rank 13. Not checkable as printed. Mean rank 11.0666 reproduces (l-ch1.py; source §11.2 L2182).

## B. Reproduced (no deviation) — all MEASURED unless marked
|Λ| = 976 in every language (l-ch1.py) · mean rank 11.0666 · void 6,912 − 976 = 5,936 (§11.2 L2184) · E(periodic table) = 36 (L1589, L7253) · E_bits = log₂ C(126, 36) = 105.1, |ℛ| = 126 = 90 + 36, 105.1/1.168 = 90.0 (l-ch1.py; L7253) · gcd/lcm = meet/join (L2180) · F′(1)/F(1) = mean rank (L2182) · 7/976, 7/199,130 (tower-2.py) · seven comparisons (§10.3 L2056, L2019) · 7.07 bits (§11.1.1 L2115) · dim p = 4, dim q = 6, rank 4, ⅅ = 2 (§16.1 L4347) · Edlén footnote 78 (L7884, L11621) · "carried more than it needed" (L2150) · 0.00018 s / 0.010 s, factor 55 (§21 L5565; 0.010/0.00018 = 55.6) · 74 further cells + y = 75 (l-ch1.py: rule 2S ≤ 2 at k = 1 admits 75) · 1,442 cells (Ch. 24 L6744) · 475,800 = C(976,2) · 28 = C(8,2) · six construction rules (L742) · E(Λ) = 0 in Ch. 7 (1 site, L1724–1795) · N absent from §18.4 and Ch. 12 ("1/N" 0 hits in L4980–5380 and L2304–3000) · §16.6 names ⅅ_gro (L4498) · R417, R418, R419, R420, R429 each match the Chapter 1 claim they support (record-carried) · Appendix E `blocks` ordering (L10911) · §28.8 "36 cells, closed, E = 0" (L7740) · §26.6 Aitken (L7172) · §17.3 E3 (L4814) · §7.1 monotone one-coordinate bounds (L1765) · Ch. 32 for P18 (L8798) · Ch. 19 ρ (L5390) · §16.8.2 (L4665–4669) · P3's wrapped "§23.1 / 3" = §23.13 Inversion (L6569) · twenty-three = 10 + 7 + 5 + P23 (P23 has no table row).

## C. Format (production, not subject matter; INFERRED from the member text)
Fixed-width tables survive as broken columns at L242–277, L285–289, L361–371, L423–431, L455–460, L529–540: P-numbers split across lines (P1 as "P/1", P12 as "P/1/2"), P2's digit absent (L249), "§23.1/3", "B/./2", |Λ| rendered "\ Λ\" (L264, L425, L539). Markdown tables at L347, L377, L400, L482 are intact.
