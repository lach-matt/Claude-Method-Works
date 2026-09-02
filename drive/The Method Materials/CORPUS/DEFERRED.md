# DEFERRED.md — cross-chapter items deferred during Phase R2 (append-only)

Do not re-derive; settle each item in the chapter named. An item is closed by a later line that cites the READ file closing it — never by deletion. This member replaces the deferred paragraph of the handoff (chat 74, ruling 3).

## As of HANDOFF-25 (chat 74), verbatim

All of HANDOFF-24's list stands (none closed this chat): L8794/L11107 "eight items" vs App. E; §16.4 "form"; Chapter 21; §32.2 wording; "§16.3's five failures"; §30.3 in Chapter 2; the D = 5 declines; L7804/L7820 vs §4.4; the seed's exactness §14.5.7–9; MC "Order dimension" as L1394's unpointed source; Janet and helium-at-2 in the References; the ionization table's source pointer; the "0.3 %" of L1965/L1982; §12.11.0.12's "17 % of 264 …"; the 27,873 setting; the '975'/'977' variant sites; Ch. 15's "20 of 20"; Ch. 16's two-route protection; §17.4's "979,300 sampled pairs" (Ch. 17); A.10 neither pointed to by §10.4 nor pointing back (Appendix A); §11.1's "depth of five" (Register 331 segment); the §12.11.1 segment's three items (the tower amendment L2406–2408 and the implied 2S′ ≤ g edge; the Figure 12.4 caption's "constraint tree" against Register 1790's 13 nodes / 14 edges; L3067's "3.5 %"); the §12.11.3 segment (axis 9 exact or envelope, 12e-05); the §12.11.5 segment (12c-01's L3466); Chapter 13 (12c-04's L3662); Appendix E (a Q item owed for 12d-01); §12.11.0.8 (L2842–2897) carries 389 at L2886/L2909/L2915 — r2-ch12f's 182,719 : 9,331 split is the measurement to read it against; §12.11.1.2 (L3205–3232) recomputes the conservative share — name both denominators (904 of 1,654; 739 of 1,169); the Chapter 14 segment carries §14.4's stub (12h-01) and §14.5's "seventeen-bit" sites if any; Chapter 6's L1673–1674 sites under 12f-01/02 and its "Register 348" pointer; the §12.11.8 heading at L3543 inside Chapter 13. **Added by chat 74:** the §12.11.5 segment settles what "the balance at a cut" (L2727) names (INFERRED: the factorisation over the transfer, L3463) and reads L3466's "hangs off one side of the tree" against 12i-02; the §7.2 / §8.5 sites (L1774 "Three results", L1908, L1910) and §18.4.1 L5150 carry 12i-01/02; the Chapter 15 segment reads §15.4 L4308–4327 as the propagation the tree makes sound (r2-ch12j's separator test is the measurement); §12.11.3.1 (L3409–3461) carries 12j-01's provenance column and its "three values, not two"; Appendix E's L10989 "Eleven items: one nonexistent, two buildable, eight retrievable" and the missing prior classification of K (12j-02); §12.11.0.5 L2779 "fourth" before §12.11.0.7 L2838 "third" — an ordering matter for the Chapter 12 close; MC L1304–1310 (the decay theorem entry, marked Proved) inherits 12k-01/02 — for the MC segment.

## Chat 74 additions (instruments)

- r2lib.py lifts, verbatim by AST, the functions of r2-ch12f (build9, src, tgt, leq, tarjan, analyse), r2-ch12d (is_tree), r2-ch12i (closure, factor_q, ci, components, separates), r2-ch12j (support, direct, composed) and r2-ch12k (mi, ci_sets — parameterised). The functions of r2-ch12c (closure/leq/jn/mt/E_np), r2-ch12e (comp/sep/cyc), r2-ch12g (encode/closed/pairs) and r2-ch12h (reach/price) are not yet lifted: lift them into r2lib when a segment next needs them, verbatim, with provenance comments.
- r2-ch12c.py is not banked as a golden (it prints wall-clock time); its figures stand as recorded in W-108 and READ-ch12c.md. All other instruments of chats 71–74 are banked (fifteen NAME.out members) and reproduce deterministically.

## Chat 75 additions (30 August 2026)

- **Closed:** §12.11.0.8's 389 at L2886 — READ-ch12l.md (set identity with r2-ch12f's cycle cells); the 389 at L2909/L2915 — READ-ch12m.md (the intersection Λ₉ ∩ rev(Λ₉) is the same 389); the 182,719 : 9,331 split has no site in §12.11.0.8 or §12.11.0.9 (both READ files). §12.11.0.12's "17 % of 264 …" — READ-ch12p.md (46 of 264 rank inputs = 17.4 %; the denominator is the inputs, by pairs 0.4 %).
- **MC segment inherits:** MC L1314 (final sentence, "the exactness ⇒ not-a-triangle theorem … proved separately"), L1318 (Proved) and L1330 (prior-art line, "That E(Λ) = 0 therefore proves … a tree") carry 12l-01; MC L1314 also carries 12l-02 ("two independent sources"); MC L1334 carries 12m-01 (the sign extension without a population); MC L1074, L1354, L1364 carry 12o-01 (two quantities named "surplus"; 9.93 / 2.82 / 17.60 sites).
- **Chapter 12 close:** the exact/envelope half of the tower table's grading column (L2936–2942, two values) against §12.11.3.1's provenance column (12j-01, "three values, not two") — settle in the §12.11.3.1 segment; the L2779 "fourth" / L2838 "third" ordering stands.
- **Instruments:** lift into r2lib when next needed, verbatim with provenance — r2-ch12m's `closure_chunked` (r2lib.closure's semantics in 200-row chunks; needed above ~2,000 cells) and `fixed_point` (iterated join-and-meet closure), r2-ch12n's `length` (lattice length = |J| by a greedy cover chain), `fibre_check` and `criterion` (exact closure of an interval-fibred stage), r2-ch12o's two surpluses. r2-ch12m.out reproduces in ≈ 150 s — include it in a gate run list only when its figures are in question; r2-ch12n ≈ 60 s; r2-ch12l/o/p under 5 s.

## Chat 76 additions (30 August 2026)

- **Closed (the §12.11.1 segment's three items):** the tower amendment L2405–2408 and the implied 2S′ ≤ g edge, and the Figure 12.4 caption's "constraint tree" against Register 1790's 13 nodes / 14 edges — READ-ch12q.md (12q-04, 12q-05: the table's bounds give 13 edges and one triangle 2S′–g–v from Λ₁₀; Register 1790's 14 edges include the f–K edge L3066 excludes); L3067's "3.5 %" — READ-ch12q.md (12q-06: the withdrawn 2,475 / 70,905). **Also closed:** Register 249's box-exhaustive closure form, left unreproduced by chat 75 — READ-ch12r.md B (|ℛ(Λ)| = |Λ| at all six stages against every cell of each ambient box, 47,775,744 at Λ₁₃).
- **MC segment inherits:** MC L1736 ("The axis density": the six figures, "three non-obvious exact sets required") carries 12q-01 (the unstated v ≡ g mod 2) and 12r-01 (the conjugation ceiling v ≤ 4f+2−g) by its pointer to M §12.11.1; MC L1244 ("The six axes of the tower": the five coupling bounds, the closure sweep of 47,775,744) inherits 12q-04 only if it names the tree — read it at the MC pass.
- **Register 434, 241 and 1790 sites (for R3, no withdrawal):** 434's "12.7 % against 31.4 %" pairs two populations (12q-03); 241's "the ⅔ §12.11.1 states as nominal" points to a claim with no site (12s-02); 1790's edge count reads K with two parents (12q-04) — L3152's "K's parents are J_c and f" (12s-04) is the same reading inside §12.11.1 against L3066.
- **§32.1.1 segment:** L8855 "§12.11.5's four-cap sweep" — the sweep is at §12.11.1 L3121–3124 (READ-ch12r C).
- **§12.11.3 / §12.11.3.1 segment:** L3136–3137's "counting axes stay exact and all three coupling axes stay envelopes" restates the classification 12j-01's "three values, not two" concerns; settle there.
- **§12.11.4 segment:** its figures (12 of 12 recoupled channels; 64.4 % through K, 39.4 % direct — the direct bound is the one-sided 2J ≤ 2J_c + 2f_max + 1 over Λ₁₁; 25 points) are already reproduced in READ-ch12s.md B; read the prose only.
- **Instruments — lift into r2lib when next needed, verbatim with provenance:** r2-ch12q's `terms` (LS terms of ℓᵏ by microstate enumeration), `new_terms` (the seniority multiset difference), `jc_values`; r2-ch12r's `TERMS` (cache), `L8_at` / `phi_at` (the tower at arbitrary caps (n_max, e_max, ℓ_max, k_max, f_max)), `Rbox` (|ℛ(X)| by the ambient-box sweep; the sliced form for a 13-coordinate box), the multiplicity-weighted `densities`. r2-ch12r.out reproduces in ≈ 25 s, r2-ch12q in ≈ 10 s, r2-ch12s in ≈ 2 s — all fit a gate run list.

## Chat 77 additions (30 August 2026)

- **§12.11.1.1 (READ-ch12t.md):** 12t-03 (the standard credited to F.3 — `recomputed under variation` as its fourth column — against F.3's printed four columns, whose fourth is the refutation) has further sites §6.2.1 L1681–1684 (already read; not in READ-ch6), §22.1.1.1 L5982 and L9150 (`registers 388, 391 and 392`) — read those segments and Appendix F's against it. Registers 388 and 389 carry 12t-01 (`as the d shell opens`), 12t-02 (§12.11.1.1's interval density against §12.11.1's realised density, 77.9 against 17.0 at the same caps) and 12t-03 — for R3, no withdrawal. 50.3 % at L3264 / L3292 is the earlier conservative share, not the axis-11 density.
- **§12.11.1.2 (READ-ch12u.md):** 12u-01 (the d shell absent at the 37.1 % row), 12u-02 (`less than a point across a fiftyfold growth` joins two ranges: 25.3 points over 50.5×, 0.8 points over 4.3×) and 12u-03 (the conservative share named `reversibility`; the reverse-edge share is 33.3 / 11.0 / 11.2 / 11.3) — Registers 392 and 393 carry them, for R3, no withdrawal. **Structural identity for the MC pass:** conservative-among-composable = edges (one cell per joined object pair at q = g) at every cap; MC's sites of 739 / 63.2 % (MC L1374 region) inherit it as a source note, not a defect.
- **§12.11.1.3 (READ-ch12v.md):** 12v-01 (`The twenty-point jump` heads the 70.7-point jump; Register 623's headline carries the same residue) and 12v-02 (Register 625 attributes the withdrawn 50.3 % to Register 623, whose printed body says 0 % — the correction chain as printed is broken) — for the Register segment and R3, no withdrawal. Register 620's `exactly 64%` is 63.9 / 64.1.
- **§12.11.1.4–.5 (READ-ch12w.md):** 12w-01 (the Λ₁₁ matching rule — the newest momentum as the target's fifth coordinate — is unstated; the plain reading gives 0.8171 and breaks the no-exception claim), 12w-02 (Registers 625/626's Λ₁₂/Λ₁₃ fractions 0.6394/0.6186 against the section's reproduced 0.6592/0.6381; no tested reading yields them) and 12w-03 (Register 627's Λ₁₃ split 24,518 = 11,188 + 5,116 + 8,214 matches neither the section's exact 72,060 nor Λ₁₂'s 24,165 nor 625's implied 75,948) — a Register-segment cluster with 12v-02 (623/625). MC `The composability peak` (L2280), `The dead ends, defined` (L2208) and IoI L49 carry the section's figures, verified here — B for their passes; MC L2208's `occupancy floor (§10.2)` against the main's L.c8 naming, for the MC pass. **Closed:** DEFERRED's §12.11.1.2 item (name both denominators) — L3208 names both, READ-ch12u.md B.
- **§12.11.1.6–.7 (READ-ch12x.md):** 12x-01 — the 4,325-cell (Z, …) population (the 118 real configurations, Register 529) is named but printed in no member; the eight base counts and E = 972,862 / 28,503 are record-carried and not re-measurable; every derived ratio, sum and partition is internally exact. For R3: M rules the data into the record or rules Register 529's sourcing sufficient; Registers 628–629 and MC L2574 restate and inherit. The 77.9 % numeral collision (EM-forbidden across rate against §12.11.1.1's axis-11 density) is cross-noted so R3 does not conflate them. §12.11.1.1–.7 is now read in full (chats 76–77).

## Chat 78 additions (30 August 2026)

- **Closed:** 12e-05 (axis 9 exact or envelope) — READ-ch12z.md: exact in the closure sense (E(Λ₉) = 0 by the box sweep) and as graded, an envelope in the dichotomy's bound sense (16 admitted / 9 realised, r2-ch12y); both measured, sense-dependent. The L3136–3137 restatement item — absorbed as a 12z-02 site (READ-ch12z.md). 12j-01 and the tower-table grading-column item (L2936–2942 against the provenance column) — READ-ch13a.md: the boxed rule per axis fails at D13 only (law-taken, graded envelope); per chain, with L3436–3437's inheritance, all five rows agree; grading = law-chain intact vs extent/weakened at or below.
- **Added (12h-01 further sites, for the Chapter 14 segment):** main L3367 "so §14.4 cannot carry it" and MC L1254 "the admissibility condition (§14.4)" — §14.4 as printed is the two-line stub; the admissibility door as printed is §17.2 L4800–4802.
- **Added (12z-02 vocabulary sites, for R3):** L2937–2942 (grading), L3136–3137, L3395–3396 (dichotomy), L3444–3445 (boxed rule), A.15 L10070–10071 ("carried exactly"); MC L1264 ("Law versus extent") is the printed harmonisation and candidate resolution.
- **Added (13a-01 residue sites, for R3):** L914, L2533, L3067, L3434 carry the 2,475 that L3477 withdraws ("the 2,475 previously printed here is withdrawn"); L3434 additionally cites §A.15 and register 230, neither of which prints the figure. With 12q-06.
- **§12.11.5 segment carries:** the section-product identity behind 15,150 / 45,450 (the tight-K cuts measured in r2-ch13a: Λ₁₂ 70,905 → 55,755, Λ₁₃ 199,130 → 153,680; 21.4 % / 22.8 % arithmetic consistent with product = the weak stage's count — verify Σ_q |A(q)|·|B(q)| there). Its earlier items ("the balance at a cut" L2727 → L3463; L3466 against 12i-02 and 12c-01) stand.
- **Appendix A segment carries:** A.15's one-sided band C fails 12,654 meets at cap 8 (L10065) against the two-sided T's 12,489 (r2-ch12y) — distinct regions, near-colliding numerals; neither corrects the other.
- **MC pass inherits:** MC L1254 — 12y-01 twice ("Two constraint forms ... (§17.2)"; "precisely §17.2's two exclusions"); it omits the five-presentation list and the J = ½ manufacture (main-only content), and its scope line L1256 fixes "unordered pairs at box caps" — the four-cap quadruple and 1,848 verified (r2-ch12y). MC L1264 — 12z-01 ("The origins table (§7.1) has four rows"); correct on "the largest 2J_c" where main L3439 slips (13a-02); its 15,150 / 45,450 / 39,375 figures anchored by r2-ch13a.
- **Instruments:** r2-ch12y, r2-ch12z, r2-ch13a banked and deterministic (≈ 30 s / 3 s / 2 s). terms and jc_values (r2-ch12q) and Rbox (r2-ch12r) copied verbatim with provenance into this chat's instruments; still owed to r2lib when next needed, with r2-ch12y's first_fail and failing_pairs (unordered-pair closure diagnostics) added to the owed list.

## Chat 79 additions (30 August 2026)

- **Closed:** 12c-01's §12.11.5 site — READ-ch13b.md 13b-02 (⟨q⟩ measured exactly at every stage: 1.4631 Λ₈ · 1.6850 · 1.8304 · **1.8874 Λ₁₁** · 1.9141 · **1.9159 Λ₁₃**; the printed 1.887 is Λ₁₁'s, at L3466 and at Figure 12.3's caption L2431–2432, one correction at two sites). The §12.11.5 item "what *the balance at a cut* (L2727) names" — READ-ch13b.md B: it is the factorisation over the transfer at L3463, and chat 74's INFERRED reading is now MEASURED (Σ_q |A(q)|·|B(q)| − |Λ| = 0 at all six stages). L3466 against 12i-02 — READ-ch13b.md B: the bridge census finds **no** edge crossing the A and B sides in the built tower, so "every coupling axis hangs off one side of the tree" is measured true at its §12.11.5 site. Chat 78's addition, Σ_q |A(q)|·|B(q)| against the tight-K cuts — READ-ch13b.md B: the one-sided tight K's **cut equals its factorisation defect**, 15,150 at Λ₁₂ and 45,450 at Λ₁₃, and "the product" is the untightened Σ|A||B| (= 70,905 / 199,130), giving 21.3666 % and 22.8243 %.
- **Added, 13b-01 (for R3 and the MC pass):** "the tight two-parent K" names two rules. The one-sided 2K ≤ 2J_c + 2f (main L3038 / L3066 / L3425 / L3432 / L3475, MC L1264 `the law for K`) cuts 15,150 / 45,450 with defect 15,150 / 45,450; MC L1696's *The recoupling bound* entry gives the exact rule as |2J_c−2f| ≤ 2K ≤ 2J_c+2f step 2 (Wigner 1931, Racah 1942), which cuts 48,630 / 134,840 with defect 13,410 / 37,695. Every printed figure is exact for the one-sided form; the form is not named at L3475. MC L1264 and MC L1696 are the MC-pass sites; MC L1264's `39,375 of Λ₁₂'s 70,905 cells sit at an f below the cap` is MEASURED 39,375 (B).
- **Added, 13c-01 (Chapter 12 close and R3):** §12.11.7 L3496–3498 reports the 2J_c ≤ k question as one of the two still open; §12.11.0.6's heading L2783 reads `Q item K, **closed**` and its body answers it. MEASURED: the bound fails at exactly four terms — p¹ ²P, p² ¹D, p² ³P, p³ ²D — and at three occupancies (k = 1, 2, 3; largest physical 2J_c = 3, 4, 5), so §12.11.7's "four cases" and §12.11.0.6's "at every occupancy" are both exact in different units. Reconcile the status of item K and name the unit.
- **Added, 13c-02 (R3, third site):** L3499 `reported at §12.11.2 and §12.11.5` — §12.11.5 contains no occurrence of `cap` at all; the tower's four-cap sweep is at §12.11.1 L3121–3124, and §12.11.2 L3385–3386's four-cap check is a different object at different caps (6, 8, 10, 12). With §32.1.1 L8855 (READ-ch12r C), this is the third site of the same misdirection.
- **Added, 13c-03 / 13c-04 / 13c-05 (R3):** L3503's `Figures 7.2–7.5` names figures that do not exist — the four described are **Figures 12.2–12.5** (L2385, L2428, L2529, L3469) and the only 7-series figure in the main volume is Figure 7.1 (L1771). L3505–3506's `(fig-sections)`, `(fig-pareto)`, `(fig-tree)`, `(fig-silhouette)` are internal file references (Ruling 46) and `the build now fails on any missing glyph rather than warning` is a build remark (Ruling 45). L3500's `resolved **there**` points at §12.11.2 / §12.11.5, but the self-duality count is resolved inside §8.4 itself at L1887–1891.
- **Added, 13d-01 (R3; Register 455 inherits):** Chapter 13's L3531 `§12.11.4 is the proof` and L3537 `which §12.11.4 forbids` attribute the four-scheme identity and the 2.17-fold spread to §12.11.4, which contains neither; both are §12.11.8's, at L3610 and L3614, and §12.11.8 itself cites §12.11.4 correctly as saying it `one level down`. Register 455 (Register L1691) carries the same attribution. Separate "scheme" from "route": L3537's `no privileged scheme` against L3618's `The privileged route exists`.
- **Added, 13d-02 (R3, self-description class):** the 1,635 is MEASURED exact as the Register's entry-heading count (1,660 distinct numbers, extent 1 to 1792, 132 unheaded), but L3514 calls them `withdrawals` where kinds.py classifies 33 as withdrawals; fifteen sites use eight different nouns (entries L20/L646/L7900, corrections L89, claims that were wrong L202/L7367, withdrawn claims L9376, failures L9055/L9381, errors L10296, withdrawals L3514, and four bare). READ-ch1-A recorded L523 against the extent; the entry-count reading supersedes it.
- **§31.3.4 segment carries (cross-notes, found resolving L3490's pointer):** the subsection at L8737 is numbered `24.3.4.1` inside Chapter 31; L8729's `a gzipped file this session could not read` is a session remark (Ruling 45).
- **§12.11.8 segment (chat 80's first) carries:** the misplaced `### 12.11.8` heading at L3543 inside Chapter 13 (DEFERRED, chat 74, still open); the `fifteen configurations` of L3612; the 2.17 spread and the four cell counts at L3614; L3618's `The privileged route exists`; Register 433.
- **Chapter 13 §13.1–13.4 segment carries:** 12c-04's L3662; L3518–3519's `Fifty sections across fourteen chapters`, whose predicate has no mechanical criterion as printed.
- **Instruments:** r2-ch13b (≈ 2 s), r2-ch13c (< 1 s), r2-ch13d (< 1 s) banked and deterministic — all three fit any gate run list. `terms` (r2-ch12q) was copied verbatim with provenance a second time, into r2-ch13c; still owed to r2lib. **Newly owed to r2lib, verbatim when next needed:** r2-ch13b's `sections(X, w)` (generalises r2lib.factor_q from the 9-coordinate layout to any stage width, returning q → (|A(q)|, |B(q)|, |Λ(q)|)) and r2-ch13c's `R(X)` (join-and-meet closure to a fixed point on a two-coordinate index, so E(X) = |R(X)| − |X|) and `failing(X, op)` (the unordered failing pairs and their values).

## Chat 80 additions (30 August 2026)

- **Closed:** the misplaced `### 12.11.8` heading at L3543 (DEFERRED, chat 74) — READ-ch13e.md C: the measured facts for M's disposition. `## 13.` opens at L3508, `### 12.11.8` at L3543, `### 13.1` at L3626, so §12.11.8's 83 lines sit between Chapter 13's opening prose and its first subsection; the contents list (L120–L135) is chapter-level only and is unaffected; §12.11.8 is cited by number at main L5901 and MC L1378, L1387, L1397, L1455, L2586, L2588, L2598, L2608, L2616, L2618, L2628, L2638, L2647 — thirteen external pointers, all of the form `§12.11.8`, all of which survive a move to the end of Chapter 12 and all of which break under renumbering into Chapter 13. Nothing moved; the choice is M's at R3. **Also closed:** the `fifteen configurations` of L3612 and Register 433 (13e-04); 12c-04's L3662 site (13f-01, and refuted there); 12h-01, the §14.4 stub and its four dependent sites (13g-02); MC L1376's four-cap sizes `carried from the record`, now measured (READ-ch13e B).
- **Added, 13e-01 (R3, MC L1385 and L1389 inherit):** E = 3,900 for the adjunction of the electromagnetic coordinates to Λ₉ does not reproduce under any of ten readings, measured under both closure operators, which agree wherever both were run: |Δℓ|,|ΔS| → 9,278; Δℓ,ΔS signed → 11,178; with the multipole → 9,278 / 11,578 / 21,610; single coordinates → 1,654 (Δℓ), 4,962 (ΔS), 3,812 (|ΔS|, the nearest). E(Λ₉) = 0 reproduces, and the direction of the claim is true under every reading. No Register entry prints 3,900.
- **Added, 13e-02 (R3, three sites):** L3591's `§12.11.0's transit condition 2S′ ≤ g admits 1,169 cells` — 2S′ ≤ g is Λ₉'s build condition, admitting all 1,654; the 1,169 is L3207's composable set (target a legal source, = g ≥ 1 here). Register 444 and L3276's table row carry the same misnaming. The 0.0004-of-0.633 pair is reproduced exactly and fixes the unnamed electromagnetic predicate as **E1 and ΔS = 0** (264 cells, H = 0.6334).
- **Added, 13e-03 (R3):** L3582's `the fourth instance of §12.11.2's second excluded form` — §12.11.2's second *form* is differences; the object is the congruence, second in that section's *machines* list. MC L1374 names it correctly and states no ordinal.
- **Added, 13e-04 (R3; Register 433 and MC L1399 inherit):** the four-scheme J-multiset claim at L3610 rests on a three-chain witness (jK, LS, jj) and fifteen configurations printed in no member. MEASURED: the identity holds across all four chains including LK, in all 16 two-electron configurations ℓ₁ℓ₂ with ℓ ≤ 3. Register 433 states the narrower three-scheme claim; MC L1399 the wider one.
- **Added, 13f-01 (R3; §12.9 L2467–2472 is the primary site):** `the most active constraint is the coupling` is refuted on the book's own Box measure and population — control reproduces 115,162 comparable pairs and 31,604 boxes = 27.4 % exactly, and on it **q ≤ k binds 34.1 % against g ≤ q's 32.6 %**, with the three printed rates 35.6 / 33.0 / 4.9 measuring 32.6 / 34.1 / 3.8. By tightness the two tie at 461 cells. `The least is the Pauli bound` is true of g ≤ 4f+2 (3.8 %) but §7.1 gives the Pauli origin to two constraints, the other binding 30.6 %. Supersedes nothing in 12c-04; enlarges it.
- **Added, 13f-02 (R3):** L3627–3629 lists the Kreuzer–Skarke frontier among the indexes that close; §31.3.4 L8736 measures E(X) = 540 there and §32 L8885 calls the 540 unverified. The nucleon index (L8653) and Appendix D (L10322) do carry a measured E = 0; no closure figure was found for `the string partition function`.
- **Added, 13f-03 (R3; census row 1076 closed as a defect):** L3647's `Chapter 7 … never says the pair is the object` against Chapter 7 L1725–1726, which says exactly that in its second sentence.
- **Added, 13f-04 (R3, production and content):** §13.3's second table row (L3657–3660) is corrupted into four interleaved fragments. Content recovered and measured on Λ₈: |A_q| = 33, 33, 23, 8 and |B_q| = 5, 10, 15, 17 — B rises strictly, A does **not** fall strictly (tied at q = 0 → 1).
- **Added, 13f-05 (R3):** L3673's `Chapter 17's measured levels` — Chapter 17 is `Extension — cells, axes, constraints`; the measured levels are Chapter 24's 1,442 (L564, L6799).
- **Added, 13g-01 (R3):** §14.3's `80/80 agreement` for bundled against decomposed presentations does not reproduce: of the 28 coordinate pairs of Λ₈ folded by lexicographic rank, **26 give E > 0** (8 to 554) against the decomposed E = 0, and only (k, 2S) and (q, g) — the pairs already joined by a constraint — agree. The claim `bundling hides structure` is confirmed; the evidence offered for it is not. The 80 sets are printed nowhere.
- **For the References pass:** the Bergman entry (main L11704) carries no year and no venue where its neighbours carry both; §14.1 dates Baker and Pixley but not Bergman (R-ATTR).
- **Instruments:** r2-ch13e (≈ 30 s), r2-ch13f (≈ 3 s), r2-ch13g (≈ 3 s) banked and deterministic — all three fit any gate run list. `Rbox` (r2-ch12r) was copied verbatim with provenance twice more, into r2-ch13e and — as `Rset`, returning the set rather than its size — into r2-ch13g; still owed to r2lib, and the set-returning form should be lifted alongside it. **Newly owed to r2lib, verbatim when next needed:** r2-ch13e's `Rn(X)` (the width-general join-and-meet fixed point, chunked in numpy; generalises r2-ch13c's `R(X)` from two coordinates to any width) and r2-ch13f's `sections(X, w)` in its 8-to-13 coordinate form together with the interval Box/binding measure of its §3 (which reproduces the recorded 115,162 / 31,604 / 27.4 % census).

## Chat 81 additions (30 August 2026)

- **Closed:** §14.5's "seventeen-bit" item (DEFERRED, chat 74, for the Chapter 14 segment) — no `seventeen-bit` site exists in §14.5; the seventeen in the section is Birkhoff's join-irreducible count at L3782, verified (READ-ch13h.md B). **Also closed:** the disposition of the six bare headings §14.5.2–§14.5.7 (HANDOFF-32's opening item) — READ-ch13i.md: measured, not displaced, 41 pointers into them.
- **Added, 13h-01 (R3):** L3756's `§8.4 already counts those [the meet-irreducibles] for Λ under a different name` — §8.4 (L1873–1899) counts the largest antichain, log-concavity, the skew and the self-duality survivors, and no irreducibles of any kind. §8.3 has the seventeen join-irreducibles (L1848, L1851, L1869; L10092 confirms); the only meet-irreducible count for Λ is Appendix D.5.7 L10735. L3756 also slides between the meet-irreducibles of the Moore family (closed sets) and of the lattice (cells).
- **Added, 13h-03 (R3):** L3787's `about 1.25 per cell` — MEASURED 12/8 = 1.5000, 14/9 = 1.5556, 20/16 = 1.2500; only the 16-cell ambient. The counts 12, 14, 20 and their generation of the family are exact.
- **Added, 13h-04 (R3; Registers 467 and 505 inherit):** `a compression of 139 to 1, exactly` (L3775) — 976/7 = 139.4286, 976 = 7·139 + 3. Register 467's correction line reads `seven cells and 139 to 1, exact`, fixing the reading against the text; its own superseded `89 to 1` is 976/11 = 88.7273 and §14.5.8 L3821 repeats it as `compresses 89×`. **The seven itself is exact** — re-measured independently of §14.5.9 by exhaustive branch and bound on the set-cover reduction (no seed of size 1…6; a seven-cell witness with ℛ(G) = Λ₈).
- **Added, 13h-05 (R3; census row 1077 closed as a defect):** L3795's `has never cited Carathéodory` against this volume's own References L11765–11769, MC L650–658 (Caratheodory 1911, with prior art) and MC L3411's bibliography table; Register 468's body records the entry being made (`Entered.`) and §14.5.8 L3836 then calls it `already in this book's References`.
- **Added, 13h-06 (R3, residue):** References L11767–11768 carries `§14.5.1's eleven-cell generating set` — the eleven Register 467 marks superseded by Register 505's seven. With 13h-04.
- **Added, 13i-01 … 13i-05 (R3; the block, not a line):** §14.5.2–§14.5.7 carry **zero body lines** and are cited **41 times on 40 lines** across five members — §14.5.7 alone 25 times. Forty are in the four reader-facing volumes (main 14, MC 12, Register 13, IoI 1). **Five MC entries carry an R-FORM `Proved —` / `Computed —` chain whose first link is one of the six** (L466, L500 → §14.5.5; L510, L560 → §14.5.4; L788 → §14.5.7), as does the MC notation table (L63, L64, L66, L69) and the MC's opening line L15. The content is **absent, not displaced**: over L3810–4075 the probes `ℛ₄`/`orientation`, `840`, `750`, `localis`, `two pairwise operators`, `cycle` and `anti-exchange` all return zero lines. `anti-exchange` occurs nowhere in the main volume although MC L130 cites `§14.5.7's anti-exchange failure`; the seed definition `G is a seed iff φ̂(G) = φ̂(X)` occurs on exactly one line, L3923, inside §14.5.9's report of §14.5.7. L11563 attributes the 840-cell / E = 750 witness to §14.5.3; it is §13's parity rule at L3577–3579 and L5676, and its figures are exact (r2-ch13e). **This is the one finding of the review so far that blocks a volume rather than a line** and it cannot be repaired by re-pointing.
- **§14.5.9 segment carries:** L3929's table gives Λ₈ a `reverse` figure of **40** and a spread of **33**; prune in descending cell order measures **11** (r2-ch13h §2), so the 40 comes from reverse-delete proper, not order-reversed prune, and the 33 rests on it — measure it there. Also L3934's `ten to thirteen for twelve cycles` against Register 467's `12, 11, 12` and the measured prune spread 9–12.
- **§14.5.10 segment carries:** L3961's `§14.5.7 records that zero cells are forced` and L3979's `§14.5.7 stands unamended` — both report the content of an empty section (13i-03); Register L2225's withdrawal (`NO CELL OF THE SEED IS NECESSARY, AND §14.5.7 WAS RIGHT`, four cells in all 140 sampled seeds) is the same dependency.
- **MC pass inherits:** MC L15, L63, L64, L66, L69, L130, L466, L500, L510, L560, L684, L788 — all twelve resolve into the empty block (13i-01/02); MC L650–658 (the Carathéodory lower bound entry, `seed ≥ the Carathéodory number = the breadth = d for a product of d chains`) is the live citation that refutes main L3795 (13h-05). **IoI pass inherits:** L281 (`the same pair ℛ₄ refuses at §14.5.6`).
- **References pass inherits:** L11765–11769's Carathéodory entry (13h-05, 13h-06) — it is present, it names no work, and it carries the withdrawn eleven.
- **Instruments:** r2-ch13h (≈ 38 s) and r2-ch13i (< 1 s) banked and deterministic; both fit any gate run list. `Rset` (r2-ch13g, from r2-ch12r's `Rbox`) was copied verbatim with provenance a third time, into r2-ch13h; still owed to r2lib. **Newly owed to r2lib, verbatim when next needed:** r2-ch13h's `closure_mask` (the bitmask form of the box sweep for small ambients, validated against `Rset` on every non-empty subset of the 8- and 9-cell ambients), its `prune` (prune-greedy against a fixed target), and its **exact set-cover reduction** (envelope steps + value slots as elements, two exact reductions, branch and bound) — the last is the instrument that makes any seed claim in §14.5.7–§14.5.14 re-measurable.

## Chat 82 additions (30 August 2026)

- **Closed:** the r2lib lift owed since chat 74 — `Rset`, `cover_model`, `cover_reduce`, `exact_seed`, `enum_min_covers`, `closure_mask` and `staircase` are appended to r2lib.py this build, verbatim with provenance. Still owed and untouched: r2-ch12c/e/g/h's functions; chat 75's `closure_chunked`, `fixed_point`, `length`, `fibre_check`, `criterion`; chat 76's `terms`, `new_terms`, `jc_values`, `TERMS`, **`L8_at` / `phi_at`** (the tower at arbitrary caps — the next batch that needs a cap sweep needs these first), the multiplicity-weighted `densities`; chat 77's stage-composability sets; chat 78's `first_fail` / `failing_pairs`; chat 79's `sections(X, w)` and `R(X)` / `failing(X, op)`; chat 80's `Rn(X)` and the interval Box/binding measure. **Also closed:** §14.5.9's `reverse = 40` and `spread = 33` (DEFERRED, chat 81) — READ-ch13j 13j-07: 40 is neither order-reversed prune (11, r2-ch13h) nor worst-first greedy (23 over the non-dominated cells, 27 over all), and the section defines no heuristic, so the 40 and the 33 that rests on it are not re-measurable; recorded as a defect, not identified. **Also closed:** §14.5.10's two dependencies on the empty §14.5.7 (DEFERRED, chat 81) — READ-ch13j 13j-01: L3961 and L3979 report the content of a body-less section, and the substance they report (`zero cells are forced`) is MEASURED true at Λ₈, Λ₉ and Λ₁₀, so the defect is the pointer and not the claim.
- **Added, 13j-01 … 13j-14 (R3):** see READ-ch13j.md. The two that block more than a line: **13j-01**, where §14.5.12's `219 of 219` is a sample of 24,585 and the section heading `What every minimum seed contains` is false as printed — three of the four cells are in 59 %, 28 % and 14 % of minimum covers; and **13j-11**, where §14.6.3–§14.6.6 print five running object counts (248/246/2 at 12 %, the same at 3 %, 265, 197/191/6, 179/170/12 at 7 %) no two of which agree and none of whose percentages follows from its own numerator.
- **§14.5.9 L3934's `ten to thirteen for twelve cycles`** (DEFERRED, chat 81) is **still open**: measured prune spreads are 12/13 in the cover model and 11/12 by Rset prune, but the twelve cycles are a record of past sessions and are not re-measurable. Settle at R3 against Register 467.
- **Chapter 15 segment carries (chat 83's first work):** §15.4 L4308–4327 read as the propagation the tree makes sound (DEFERRED, chat 74; r2-ch12j's separator test is the measurement), and Ch. 15's `20 of 20` (DEFERRED, chat 74). Chapter 15 opens at **L4270**, not L4158 as HANDOFF-34 states.
- **Chapter 16 segment carries:** §16.4 "form" and the two-route protection (DEFERRED, chat 74); §16.6 L4482 `multiverse dimension ⅅ_gro`, which §14.6.1 L4115–4116 cites as a term with no referent, against §29.2.2 L7922.
- **Chapter 17 segment carries:** §17.4's `979,300 sampled pairs` (DEFERRED, chat 74). Note 13j-01's shape when reading it: a sampled figure printed as a population is now a measured class in this volume, not a suspicion.
- **§10.1 segment / Chapter 10 carries:** 13j-08. §10.1 is six lines (L2026–L2031) and carries no table at all; four sections cite it as though it did — L4256, L4259 here, and its own chapter's neighbours are unread. Read §10.1's chapter before R3 disposes of 13j-08.
- **§28.9 carries:** 13j-10 — zero body lines, cited from §14.5.8 L3858 for figures it does not print. The 13i-01 class outside §14.5; when the Chapter 28 segment opens, census the pointers into §28.9 first.
- **Appendix G segment carries:** 13j-09 — Appendix G (L11361–L11408) is a one-row-per-item table; §14.6.6 cites `T §8.2 (Appendix G)'s own table` for arity-2/3/4 defect figures printed in no member, and drops the `T` qualifier at three later sites where main §8.4 is a different section.
- **References pass inherits:** 13j-13 — Brunetti, Fredenhagen, Verch, Reeh, Takesaki and Sorce carry no References entry although §14.6.5 and §14.6.6 turn on them; Chandrasekaran & Flanagan is cited by arXiv number where its neighbours carry name and year. With 13h-05 and 13h-06.
- **Register pass inherits (no withdrawal):** Register 497 is cited affirmatively at L3915 and withdrawn at L3946, eight lines apart in one section; Registers 498–500 and 502 are withdrawn at L3946 and were not opened here; Register 487 → L1977 is the source of the 18,288 tests, which is record-carried and not re-measurable (12x-01 class).
- **Instruments:** r2-ch13j (≈ 60 s) and r2-ch13k (≈ 2 s) banked and deterministic; r2-ch13k fits any gate run list, r2-ch13j fits one alongside at most one other long instrument. r2-ch13j's `enum_min_covers` over the full mask list is the instrument that makes any "found by search" claim in §14.5 re-measurable as a population; use it before accepting a count of covers, seeds or completions anywhere in the volume.

## Chat 83 additions (30 August 2026)

- **Closed:** §15.4's propagation (DEFERRED, chat 74) — READ-ch13l B6. Twenty seeded trials at each of two cap settings, all eight axes independently permuted: an order found 20 of 20 and a found order closes globally 20 of 20, with **zero** candidate orders passing every parent–child local test and then failing global closure. The tree makes the propagation sound **on this index** — measured at Λ₈ and at the 216-cell index, not proved in general. **Also closed:** Chapter 15's `20 of 20` (DEFERRED, chat 74) — reproduced exactly at both cap settings, and the four cap settings of L1786 (216 / 976 / 1,636 / 2,394) all rebuild. **Also closed:** part of the r2lib lift — **`L8_at`** is appended to r2lib.py this build, verbatim from r2-ch12r.py with provenance. Its companion `phi_at` is **not** lifted: it depends on `TERMS`, still owed. Still owed and untouched otherwise: r2-ch12c/e/g/h's functions; chat 75's `closure_chunked`, `fixed_point`, `length`, `fibre_check`, `criterion`; chat 76's `terms`, `new_terms`, `jc_values`, `TERMS`, `phi_at`, the multiplicity-weighted `densities`; chat 77's stage-composability sets; chat 78's `first_fail` / `failing_pairs`; chat 79's `sections(X, w)` and `R(X)` / `failing(X, op)`; chat 80's `Rn(X)` and the interval Box/binding measure.
- **Added, 13l-01 … 13l-09 (R3):** see READ-ch13l.md. The one that blocks more than a line is **13l-01**: the d = 2 criterion at §15.3 L4302 and at **A.8 L9969–9970** is false under the literal reading of "a total order" (124 mismatches on 490 sets, 1,297 on 4,067, exhaustive) and exact under the total-preorder reading (0 mismatches on both). Two sites must move together, and "that order **is** the relabelling" must weaken with them, since ties make the relabelling non-unique. The substance is true; only the statement fails. 13l-02 is its witness inside the book's own object: may-precede is non-antisymmetric on axes n, e and 2S of Λ₈.
- **Appendix A carries inherits:** **13l-03** — the Appendix A index at L9951 sends `A.7 "may precede" is necessary` to `§16.3, in full`; §16.3 contains zero occurrences of the phrase and §15.3 contains three. The other eight rows of that index resolve correctly, so this is one misdirected row, not a drifted table. When the Appendix A segment opens, re-census that index against the claims rather than the headings. **13l-01's second site (A.8) is in the same appendix** — take them together.
- **Chapter 18 segment carries:** **13l-05** — §15.3 L4305 sends the reader to §18.4 for the development of "a total order on every axis separately is necessary and not sufficient"; §18.4 and §18.4.1 together contain zero occurrences of "may precede", "total order", "order on" or "recover". §18.4's own statement is the closure analogue. Decide at R3 whether §18.4 gains the order paragraph or §15.3 loses the pointer. The reciprocal direction is sound: A.7's remark at L9965 cites §18.4 for the converse failing, which §18.4 does exhibit.
- **Figures pass inherits:** **13l-07** — FIGURE_ASSETS.md and FIGURE_MAP.md give a line number for every figure and **32 of 32 are wrong**, offsets −11 to +29 (Figure 15.1 registered at 4290, placed at L4319). Both are process members, not reader-facing, so this is a production defect; the consequence is that R3 must not use that column to place anything. Recompute the column from the `![Figure N.N]` placements before any figure work.
- **References / attribution pass inherits:** **13l-04** — Chapter 15 prints A.7 and A.8 and cites Appendix A zero times, A.7 and A.8 zero times, and no Register entry in 62 lines, while Register 1597, 1633 and 1913 carry its subject matter and the Mathematical Compendium attributes its corollary to Moore 1910 at mc L352 and L634. With 13h-05, 13h-06 and 13j-13.
- **Not re-measurable, recorded not identified:** **13l-09** — §15.4 L4317's `0 of 12`, `42 %` and `25 %`. The two rates carry no denominator and neither failed method is specified anywhere in the section; 42 % = 5/12 rounded and 25 % = 3/12 is arithmetic that fits, INFERRED only. The 13j-07 class. **13l-06** — L4302's `120 sets` and `274 of 274` against L9981's differently worded restatement of the same verification; the population behind "120 sets" is not stated at either site. The exhaustive measurement in 13l-01 supersedes both as evidence.
- **Chapter 16 segment carries (chat 84's first work):** §16.4 "form" and the two-route protection (DEFERRED, chat 74); §16.6 L4482 `multiverse dimension ⅅ_gro`, which §14.6.1 L4115–4116 cites as a term with no referent, against §29.2.2 L7922. Note also that §16.1, §16.3 and §16.5 are the "in full" targets of A.4, A.7 and A.5: 13l-03 is settled for A.7, but A.4 → §16.1 and A.5 → §16.5 should be resolved to the claim while that chapter is open.
- **Instruments:** r2-ch13l (≈ 7 s, computable) and r2-ch13m (≈ 1 s, prose) banked and deterministic; both fit any gate run list. r2-ch13l's exhaustive d = 2 sweep is the instrument that makes any "the criterion is exact" claim re-measurable as a population rather than as a sample; its `recover()` is the first implementation of §15.4's propagation in this project and is the measurement for any later order-recovery claim, including Chapter 30's `384 of 384`.
## Chat 84 additions (30 August 2026)

- **Closed:** both chat-74 Chapter 16 items. **§16.4 "form"** closes as a defect — READ-ch13n A/13o-01: the sentence *"one coordinate bounded by a monotone function of one other"* occurs at exactly two main-volume lines, **L1765** (where the constraint form is defined) and **L7740** (where it is glossed *"That is §16.4 form"*); §16.4 at L4407–4430 contains it zero times and contains "monotone" zero times. Eight sites carry the label — **L261, L653, L4475, L4525, L4899, L7740, L8803, L11417** — and L4886 carries it negated. R3 decides: §16.4 gains the form, or all eight re-point to L1765's section. **The two-route protection** closes affirmatively — READ-ch13n B4: the 540.0/1215.0 pair is exactly 9/4 apart, as V = 4ν/3 against w = 3ν·e requires; the apparatus pair agrees at 0.0895σ, printed 0.09σ; and Λ₈'s constraint graph is a tree with exactly one path between each of the 28 coordinate pairs, so ⅅ_def must indeed be built from derived quantities.
- **Added, 13n-01, 13n-02, 13o-01 … 13o-05 (R3):** see READ-ch13n.md. **13n-01** is the one that moves two sites together — L4442's *"That is ⅅ = 0, in the special case dim q = dim p"* and its restatement at L11622 assert an equality the counting argument does not entail; the argument gives ⅅ ≥ 0, and ⅅ = 0 additionally needs full Jacobian rank. Measured: full rank in 60 of 60 random maps at dim q = dim p = 4, so the claim is generically true, but a constructed map with a functionally dependent output has rank 3 and ⅅ = 1. The substance is Edlén's and is sound; only the equality fails.
- **Chapter 16 segment carries (the next section read, §16.6–§16.8, main L4482–L4788, 307 lines):** §16.6 L4482's `multiverse dimension ⅅ_gro`, which §14.6.1 L4115–4116 cites as a term with no referent, against §29.2.2 L7922 — **not opened in chat 84**. Also **L4525's "constraints of §16.4 form"**, one of 13o-01's eight sites, falls in that range. **Boundary, MEASURED chat 84:** Chapter 16 runs L4332–L4788 and Chapter 17 opens at **L4789**; HANDOFF-36's L4477/L4478 is wrong, as HANDOFF-34's L4157 was.
- **Appendix A segment inherits:** **C1 of READ-ch13n** — the Appendix A index at L9945–9954 carries nine rows, and those nine are exactly the statements with **no** `### A.N` section; the ten statements that do have sections (A.3, A.8, A.9–A.13, A.15, A.18, A.19) appear in no row. Coherent as a design, but A.8 — the site of 13l-01 — is unfindable from the index heading its own appendix. Take with 13l-03 (A.7 → §16.3) and 13l-01's A.8 site. **A.4 → §16.1 and A.5 → §16.5 are cleared** (READ-ch13n B8): both resolve to the claim, so 13l-03 remains one misdirected row.
- **Headings pass inherits:** **13o-04** — four `###` headings are truncated with their remainder rendering as body text: **L4407/4408** (`…but only under two` || `routes`), **L7721/7722** (`…and naming the` || `dependency names the coordinate`), **L6582/6583** (`…the book has been calling them` || `one`), **L8659/8660** (`…the generating function, and a` || `disanalogy`). Every contents list and running head built from these carries the truncated title. Seven further heading-plus-indented-line pairs were measured and are legitimate display lines: L574, L579, L4277, L6606, L6634, L7207, L10173. Recompute, do not re-derive.
- **Figures pass inherits:** **13o-05** — Figure 16.1 is registered at 4342 in both FIGURE_ASSETS.md (L23) and FIGURE_MAP.md (L20) and placed at **L4373**, offset **−31**, outside 13l-07's measured −11 to +29. The column stays unusable for placement.
- **References / attribution pass inherits:** **13o-02** — the antiprotonic-helium figures 804,633,059.0 ± 8.2 MHz and 804,633,057.8 ± 10.6 MHz occur at exactly two sites in the whole work (L4423, L4424) with no source named anywhere in the section; the only named sources in 150 lines are Edlén and Rydberg. A published laboratory result used as the worked case for path-disjointness "realised in hardware". With 13h-05, 13h-06, 13j-13 and 13l-04.
- **Not re-measurable, recorded not identified:** **13n-02** — L4475 and L7740's *"36 cells, closed, E = 0"* for the index (step, visible, alternatives, committed): 32 alphabet readings give exactly 36 cells and all 32 close with E = 0, but the alphabets are printed at neither site; only 3 readings also admit L7742's witness cell (2,2,3,0), all requiring committed ∈ {0,1}. **13o-03** — L4368's *"the fifty cells"* against L4363's *"56 of 56"* and L4371's *"fifty-six wrong cells"*, with *"ten members"* as a third undefined population in the same paragraph; "fifty cells" occurs nowhere else in any volume. The 13j-07 / 13l-09 class. **C2** — L4352 and L4357's four laws and four perturbations name neither parameterisation, so "verdicts identical" is recorded, not measured.
- **Instruments:** r2-ch13n (computable, ≈ 8 s) and r2-ch13o (prose, ≈ 1 s), banked and deterministic; both fit any gate run list. r2-ch13n carries three things later batches will want: a self-contained numeric Jacobian and pivoted-elimination `rank`, a Slater-determinant term/seniority engine (`dets`, `allowed_2S`, `terms`, `seniorities`) that is the measurement for any LS-coupling claim in Chapters 8–12 and the Spectra Compendium, and an alphabet-sweep that measures a printed cell count against every plausible reading of an unstated alphabet. None is lifted to r2lib this build; add them to the owed list.

## Chat 85 additions (31 August 2026)

- **Closed:** the chat-74 Chapter 16 item **§16.6 L4482's `multiverse dimension ⅅ_gro`** — READ-ch13p A/13p-05, as a **defect**. §14.6.1 L4115–4116 states that §16.6 grades *multiverse dimension* with ⅅ_gro; MEASURED, *multiverse* occurs **zero** times in §16.6 (L4482–L4519) and exactly three times in the whole main volume (L4116, L7347, L9303), none of them inside Chapter 16. §16.6's only ⅅ_gro instance is ***q*, this book's transfer coordinate** (L4512–4514), asserted there as *"the one with no instance anywhere until now"* — which a second graded instance would falsify. The §29.2.2 half of L4115–4116 is sound (*not posable* is at L7348). R3 decides: §16.6 gains the second instance and L4512 weakens, or L4115–4116 re-points to §29.2.2 alone. **Also closed:** L4525's *"constraints of §16.4 form"*, 13o-01's eighth site, resolved to the claim at **L1765** without re-deriving 13o-01. **Still owed to r2lib and untouched:** r2-ch12c/e/g/h's functions; chat 75's `closure_chunked`, `fixed_point`, `length`, `fibre_check`, `criterion`; chat 76's `terms`, `new_terms`, `jc_values`, `TERMS`, `phi_at`, the multiplicity-weighted `densities`; chat 77's stage-composability sets; chat 78's `first_fail` / `failing_pairs`; chat 79's `sections(X, w)` and `R(X)` / `failing(X, op)`; chat 80's `Rn(X)` and the interval Box/binding measure; chat 84's numeric-Jacobian `rank` pair, Slater-determinant term engine and alphabet sweep; **and now chat 85's `therm`/`untherm` (thermometer bit-packing, under which join is bitwise OR and meet is bitwise AND — the reason the 5,936-cell population sweep fits one call), `lat_closure`, `Rtree` (the box sweep on a given edge set) and `pushback`.**
- **Added, 13p-01 … 13p-13 (R3):** see READ-ch13p.md. The two that block more than a line: **13p-01**, where §16.8.4's amplification floor of **59** is printed at L4693 and L4703 while the population minimum is **15** (86 cells below 59) and the section's own Figure 16.2 caption prints 15 eleven lines later — a class minimum for the *2S ≤ k* violators carried into a sentence quantifying over every insertion, with neither printed median (340, 352) reproducing against a measured 309; and **13p-04**, where *"fifty-one terms"* at **L4523 and L5192** is stale by exactly the six terms Chapters 35–36 added, the Index's own extent line at **L11419** reading *"57 terms, 311 entries, 44 specialisation relations"* and naming the cause in the same sentence.
- **Löwdin / three-body residue, first instance measured:** 13p-04 is the first place R2 has found a figure left stale **by the absorption of Chapters 35–36 itself**. Before R3 closes, sweep every extent-like count in the reader-facing volumes against its post-absorption value; the pattern to look for is a figure that was exact before Part VII and was not restated forward.
- **Chapter 17 segment carries (the next section read, §17.1–§17.3, main L4789–L4872):** §17.2's Theorem 17.1 is **cleared** (READ-ch13p B9) — it is stated and proved at L4806 and L4534's use of it is sound. Still open there: §17.2 L4802's *"100 % over 424 tests"* and L4809's *"seven functions including the identity and a constant"*; §17.4's `979,300 sampled pairs` (DEFERRED, chat 74) — take it with 13j-01's shape, a sampled figure printed as a population being now a measured class in this volume. **Boundary, MEASURED chat 85 by heading scan:** Chapter 17 opens **L4789**, §17.1 L4794, §17.2 L4799, §17.3 L4814, §17.4 L4873.
- **Chapter 6 / Chapter 19 segment carries:** **13p-06** — §16.7.1 L4615 attributes the Janet table to **§6.2**; MEASURED the table is at main **L1581–1585** and its reading at L1587, both inside **§6.1.1** (opens L1552), and §6.2 (opens L1594) contains *"Janet"* zero times. The 13d-01 / 13l-03 / 13o-01 class, off by one subsection. **13p-07** — §16.7.1 L4593's *"the same 118 elements"* against the book's own table at L1581–1585, which prints cell counts **90 / 118 / 120** for those three conventions; the E column (36 / 106 / 0) agrees exactly with §16.7.1 L4589–4591, so only the cell count is misrestated. Read §6.1–§6.2 before R3 disposes of either. **§19.5 is cleared** (READ-ch13p B10): it names Edlén 1964, Ritz 1908, Paschen & Götze 1922 and Dunz 1911 in that order at ρ ≤ 2, and *stated gap* / *unexplained absence* occur together at main L628, L4551 and L5545.
- **Chapter 29 / the ⅅ = 0 pass inherits:** **13p-08** — §16.6.2 L4568–4569 calls *verdict* *"the first coordinate anywhere in this book below the ⅅ ≥ 1 floor"*; MEASURED, ⅅ(x) = 0 occurs at main L4562, L4565 and **L7865**, and ⅅ = 0 at main **L1589**, L4442, L4558, L7884 and L11622. L4562 — two lines above the primacy claim — cites §29.1 as *already proving* ⅅ(novelty) = 0, and L4565 derives verdict's from it. A derived instance cannot be first, and L1589 is earlier still. The substance (verdict is undefendable and caps all twenty-eight terms) is untouched.
- **Ruling 45 / 46 pass inherits:** **C8 of READ-ch13p** — main **L11419**, inside the reader-facing `## Index`, carries *"Regenerated from the text on 2026-08-24 (`index_gen.py`)"* and a paragraph on which locators the previous index used. A build remark and a script name in a reader-facing volume. R3 must lift the extent figures out of that paragraph (they are 13p-04's evidence) before removing it.
- **Figures pass inherits:** **C7 of READ-ch13p** — Figure 16.2 is registered at **4679** in FIGURE_ASSETS.md (L24) and FIGURE_MAP.md (L21) and placed at main **L4712**: offset **+33**, outside 13l-07's measured −11 to +29 band and opposite in sign to 13o-05's −31 for Figure 16.1. The column stays unusable for placement; recompute it from the `![Figure N.N]` placements.
- **References / attribution pass inherits:** **C5 of READ-ch13p** — L4611's *"Resonance strength enters at e^|p−q|"* is the physical warrant for the whole asteroid-belt case and carries no source; the only names in the section's 307 lines are Racah (L4510) and the four unretrieved documents at L4550, which are cited as gaps rather than as authorities. With 13h-05, 13h-06, 13j-13, 13l-04 and 13o-02.
- **Not re-measurable, recorded not identified:** **13p-11** — L4721–4722's *A ≈ fibre × (0.972 − 0.154 · descendants)*, corr **−0.942**, median error 7 %, worst 24 %. *Fibre* is defined nowhere in the section; two readings swept. Under *fibre = cells breaking exactly that constraint*, and using the A figures the book prints at L4780–4782, ℓ ≤ n−1 gives 0.386 (printed 0.39) and k ≤ 4ℓ+2 gives 0.477 (printed 0.48), while all three descendants-0 rows give 0.397 / 0.244 / 0.625 against a printed 0.96–0.99; corr measures +0.284 under that reading and +0.819 under the alphabet-size reading. **13p-12** — L4710's *"jumps 397 %"*: measured, dropping the rival g ≤ q takes the class median A from **15** to **193** (+1,187 %), which does land in the band (median 179 over all single-constraint violators); 397 % would take 15 to 74.6. **13p-13** — L4537's *38 cells, box 144, density 26.4 %, E = 0*: **156** of 9,000 monotone readings of the stated bounds give exactly 38 with E = 0, and the *"cycle access–referent–checked"* of L4538–4539 does not follow from the two edges the text names, which form a path on three nodes. The 13j-07 / 13l-09 / 13n-02 class.
- **Owed before Chapter 6 or Chapter 19 opens:** the periodic table and the asteroid-belt catalogues are not in r2lib, so §16.7.1's E figures (36 / 106 / 0 and 2 / 1 / 1), its *0 of 6* and *36 of 36* admission counts, and §16.6.1's *"thirteen cells occupied of thirty-eight, E = 11"* were checked only for arithmetic and cross-site agreement, not re-measured on their own data. Add both catalogues to r2lib before either chapter is read.
- **Instruments:** r2-ch13p (computable, ≈ 93 s) and r2-ch13q (prose, ≈ 1 s), banked and deterministic; r2-ch13q fits any gate run list, r2-ch13p fits one alongside at most one other long instrument. r2-ch13p's population sweep over all 5,936 insertions is the instrument that makes any *"minimum / median cost"* claim in the volume re-measurable as a population rather than a sample — use it before accepting an amplification, insertion or removal figure anywhere; and its `Rtree` is the first implementation in this project of the tree operator §16.8.6 contrasts with the full pairwise ℛ.

## Chat 86 additions (31 August 2026)

- **Closed:** the chat-74 Chapter 17 item **§17.4's `979,300 sampled pairs`** — READ-ch13r A/13r-01, as a **defect**, and it closes without needing the construction rebuilt. MEASURED: the volume's all-pairs convention is C(N, 2), exact at three sites — 1,367,031 = C(1654, 2) and 540,280 = C(1040, 2), both printed as *all*, and 979,300 = C(1400, 2). L4904 states the repair is a **bijection** onto the repaired lattice, which forces L4887's lattice and L4901's 1,040 cells to have equal counts; 1,400 ≠ 1,040. Read instead as a true sample the figure is impossible outright: 979,300 pairs cannot be drawn from 1,040 cells, whose entire pair set is 540,280. MC L1494 restates the 89,864 and L1496 repeats *sampled*, so both volumes move together in R3. **Also closed:** the record-carried chat-67 Sweep C item on §17.2's classification line — 13r-03, measured, and it is **two** classes not one (maxima 10 of 28, minima 10 of 28).
- **Added, 13r-01 … 13r-10 (R3):** see READ-ch13r.md. The two that block more than a line: **13r-02**, where §17.4's 45,690 / 1,040 cells rebuild under **none of 1,728 monotone readings** of the construction as printed (at Λ₈'s own caps it gives 7,908 and 5,790), and where 45,690 and 1,040 each occur exactly once in the six volumes, so R3 must have the construction stated before either count can be disposed of; and **13r-04**, where §17.3's L4815 ends *"The criterion is:"* and prints no criterion — the E3 criterion is at L4860, forty-five lines and four sub-arguments later.
- **Chapter 12 / Chapter 7 segments inherit:** **13r-06** — main **L3364** says *"Chapter 17 excluded two constraint forms — sums and differences"* where §17.2 L4802 excludes three and §17.3 **L4868** says *"Sums and products fail"*. L4854's own pointer to §12.11.2's *second* excluded form is sound under §12.11.2's numbering; the count at L3364 is what moves. **13r-05** — L4894's *"which §7.1 excludes"*: §7.1 runs **L1750–L1763**, is the constraint table, and its only *exclu* tokens are the two Pauli-exclusion provenance cells at L1755 and L1758. It states no exclusion of any constraint form. The 13d-01 / 13l-03 / 13o-01 / 13p-06 class; the rule itself is sound and printed at L4868.
- **The tower-axis pass inherits: 13r-07** — *conjugation ceiling* occurs at exactly three sites, main **L3368**, **L3382** and **L4857**. The first two attach it to **seniority**, which this volume places at **axis 10** (L2566, L3080, L3149); L4857 places it at **axis 12** on the same line that places seniority *parity* at axis 10. Either two mechanisms share an axis and the second index is wrong, or one mechanism is duplicated across two.
- **Not re-measurable, recorded not identified:** **13r-08** — §17.1's *"100 % over 288 tests"*: MEASURED, of the **5,936** cells of the ambient box outside Λ₈, **zero** may be added while keeping closure, so E1 admits nothing on this object and 288 is neither population nor result. **C7 of READ-ch13r** — L4802's *424* and L4862's *2,513* likewise print a bare test count with no population; the class sweep over Λ₈ generates 14,366 (h, value-pair) tests and no natural sub-count of it is 424. **13r-09** — §17.3's 8.2 % / 10.3 % / 0.8 % reproduce **exactly** (6/73, 15/146, 6/731) under **one** coordinate difference and not under all (21.9 % / 10.3 % / 4.2 %); the 3 × 3 ambient agrees under both, which is what hid the ambiguity. The figures are right and the defining term is unstated — the 13j-07 / 13l-06 / 13n-02 / 13p-11 class.
- **References / attribution pass inherits: 13r-10** — Chapter 17 names one person in 133 lines, **Janet** at L4841, and that names a table rather than an authority, while the chapter states the graph-sublattice criterion, the interval-map property and the convexity criterion, all of which the Mathematical Compendium attributes elsewhere (Birkhoff 1937 at MC L1490; Freuder 1982, Rota 1964, Lauritzen 1996 at MC L1498). With 13h-05, 13h-06, 13j-13, 13l-04, 13o-02 and C5 of READ-ch13p.
- **Pointer pass inherits: C1 of READ-ch13r** — L4834's *§4.6* is UNRESOLVED at a second site; R3 decides once whether Chapter 4's protocol rows take headings. **C5** — L4920's *"the cost surface of Chapter 23 carries none beyond ν"* returns zero lines in Chapter 23 (L6178–L6622) for four phrasings; open, not measured as a defect.
- **13o-01 gains no new sites:** MEASURED, *"of §16.4 form"* has **eight** sites across the six volumes — main L261, L653, L4525, **L4886**, **L4899**, L7740, L8803, L11417. The two in Chapter 17 are inside the existing class and take chat 85's resolution to the claim at L1765.
- **Boundary correction, MEASURED by heading scan:** Chapter 17 runs **L4789–L4921** and has **five** sections — §17.1 L4794, §17.2 L4799, §17.3 L4814, §17.4 L4873, **§17.5 L4914** — and Chapter 18 opens **L4922**, not HANDOFF-38's inferred L4899. Third consecutive handoff to misplace a chapter boundary.
- **Chapter 18 segment carries (the next section read, main L4922 onward):** §18.1's product-structure theorem and its three sub-sections, §18.2's *86 violations at the caps tested* (L4971, already read here as the target of L4849 and sound as a pointer, not yet re-measured as a figure), §18.3 depth, §18.4 closure not locally determined and §18.4.1 the law of realised closure — which DEFERRED already carries under 12i-01/02 (chat 74's L5150 item) and under 13l-05 (§18.4 lacks the development §15.3 promises). **Verify both boundaries by heading scan before reading.**
- **Still owed to r2lib and untouched:** r2-ch12c/e/g/h's functions; chat 75's `closure_chunked`, `fixed_point`, `length`, `fibre_check`, `criterion`; chat 76's `terms`, `new_terms`, `jc_values`, `TERMS`, `phi_at`, the multiplicity-weighted `densities`; chat 77's stage-composability sets; chat 78's `first_fail` / `failing_pairs`; chat 79's `sections(X, w)` and `R(X)` / `failing(X, op)`; chat 80's `Rn(X)` and the interval Box/binding measure; chat 84's numeric-Jacobian `rank` pair, Slater-determinant term engine and alphabet sweep; chat 85's `therm` / `untherm`, `lat_closure`, `Rtree` and `pushback` — `therm` / `untherm` were carried verbatim again this chat, which is the second instrument to copy them.
- **Instruments:** r2-ch13r (computable, ≈ 9 s) and r2-ch13s (prose, ≈ 1 s), banked and deterministic; both fit any gate run list together. r2-ch13r's homomorphism reduction is worth reusing: for h a function of coordinates (i, j), the (i, j) part of a join is (max, max) and of a meet is (min, min), so quantifying over the realised value pairs of the projection is **exhaustive** over all cell pairs and costs ≤ 256 tests instead of 475,800 — this is what let the whole E2 class sweep run in under a second.
## Chat 87 additions (31 August 2026)

- **Closed:** the chat-74 §18.4.1 item **12i-01/02 at L5150** — READ-ch13t A/13t-08, as a **defect**,
  and it closes without the three-body material being re-derived. MEASURED: `three central results`
  occurs **once in the main volume, at L5150 itself**; §7.1 (L1750–L1763) is the seven-row constraint
  table closing *"Seven constraints, four origins, and nothing else"*, and the statement L5150 and
  L5244 both attribute to it — every bound single-argument, xᵢ ≤ φ(xⱼ) — is **§7.2 L1764–1766**.
  Both pointers are one section short and R3 moves them together. **Also closed:** 13l-05 (chat 83),
  confirmed from the file — none of §15.3's four criterion phrases (*may precede*, *total order*,
  *relabelling*, *d = 2*) occurs anywhere in §18.4 L4980–L4998, so the promised development is absent
  as measured, not merely thin.
- **Added, 13t-01 … 13t-11 (R3):** see READ-ch13t.md. The three that block more than a line:
  **13t-01**, §18.1.3's *"Theorems 11.1 and 11.2"* — MEASURED **zero sites in the six volumes**,
  against Theorem 18.1 at three sites and Theorem 18.2 at seven, so R3 must decide whether the
  disclaimer renumbers to 18.1/18.2 or whether two theorems were lost in an earlier renumbering;
  **13t-04**, §18.2 L4971 and A.11 L10020's *86 violations*, which reproduce under **none of fifteen
  readings** (three definitions × comparable / covering / unit-step / join-homomorphism / projection)
  at three cap settings — Λ₈ gives 9,894 comparable and 384 covering — so the figure cannot be
  disposed of until the definition is fixed; and **13t-05**, ν printed as **e − δ** at main L4849,
  L4971 and A.11 L10016 and as **n − δ** at main L6422, with δ given as **f − ℓ** at §17.3 L4819/L4825
  and reg L1637 but as a *value* rather than a coordinate function at §18.6.3 L5362. 13t-04 and
  13t-05 move together and neither can be repaired alone.
- **Chapter 6 / Chapter 16 segments inherit:** **13t-02** — the audits row prints **E = 16** at
  L5025 and **E = 17** at L5062, ten lines apart inside §18.4.1, with Register 275 (reg L1055)
  carrying neither figure. One must move, and the choice fixes which of the two tables is authoritative
  for the other eight rows they share. **13t-03** — L5126's *"all ten indexed objects"* against a
  table classifying **3 + 5 = 8**; the E table above it does list exactly ten rows, so *ten* is the
  population and two objects are unclassified.
- **The self-count pass inherits: 13t-09 and 13t-10.** L4923 forecloses a positive result — *"every
  one of them is negative"* — where §18.6.1's fifth row (L5321–5323) prints one and calls it *"the
  only place in this book where a prediction is both available and true"*. And §18.6 L5304 counts
  **five** limitations above it, which is exact (§18.1–§18.5), while §18.6.4 L5373 calls **itself**
  *"the fifth and largest of the negatives"*. With 13j-11, 13p-03, 13p-09 and 13t-03.
- **Not re-measurable, recorded not identified:** **13t-06** — the *conserving poset* carries the
  chapter's only non-componentwise witness (28 of 511 joins, L4948) and occurs at **exactly two sites
  in the six volumes, L4947 and L4955, both inside §18.1.1**, which is the section the pointer sends
  the reader to. The object is defined nowhere; R3 must supply the definition before either figure
  can be checked. **No impossibility is claimed** — a poset need not have all joins, so 511 may be a
  sub-count of a larger pair set (C9 discipline, chat 85).
- **Production pass inherits: 13t-11** — the back-matter Index prints **59 entry rows** carrying
  **57 distinct term names**, the duplicates being *interiority* (plain L11429, italic L11432) and
  *index, self-referencing*. The extent line L11419 is **exact on both counts it states** (57 terms,
  44 specialisation relations = the 44 sub-term rows measured), so this is presentational only and
  does not disturb 13p-04, whose second site (L5192's *fifty-one*) is confirmed here.
- **Ratio pass inherits: 13t-07** — L4990's *"roughly one in five"* measures **0.2991** exhaustively
  (35 of 117 subsets of the 2³ cube passing every proper-projection test) and **0.4566** at d = 4 over
  20,000 seeded samples. The population the ratio is taken over is not printed.
- **Catalogues still owed to r2lib, third chat running:** the periodic table, Janet, the audits and
  the bibliography. §18.4.1's certificate table (L5022–5027), its E table (L5052–5062) and §18.6.1's
  prediction-budget table (L5315–5321) were checked for arithmetic and cross-site agreement only.
  Owed before Chapter 6 or Chapter 19. The asteroid-belt figure (L5336, against §16.7.1's L4597/4599/
  4609) and the subnet figure (L5319, against main L1609/L7255) were not compared.
- **Still owed to r2lib and untouched:** r2-ch12c/e/g/h's functions; chat 75's `closure_chunked`,
  `fixed_point`, `length`, `fibre_check`, `criterion`; chat 76's `terms`, `new_terms`, `jc_values`,
  `TERMS`, `phi_at`, the multiplicity-weighted `densities`; chat 77's stage-composability sets;
  chat 78's `first_fail` / `failing_pairs`; chat 79's `sections(X, w)` and `R(X)` / `failing(X, op)`;
  chat 80's `Rn(X)` and the interval Box/binding measure; chat 84's numeric-Jacobian `rank` pair,
  Slater-determinant term engine and alphabet sweep; chat 85's `therm` / `untherm`, `lat_closure`,
  `Rtree` and `pushback`. **Nothing was carried verbatim this chat** — r2-ch13t and r2-ch13u use only
  r2lib's own API (`closure`, `Rset`, `L8_at`, `load_tower`), and the two functions r2-ch13t defines
  (`failcount`, `parts`) are new and should be lifted with `viol`'s four readings when a batch next
  needs them.
- **Instruments:** r2-ch13t (computable, ≈ 81 s) and r2-ch13u (prose, ≈ 1 s), banked and
  deterministic. r2-ch13t's `viol` is worth reusing: it reports a function's non-monotonicity under
  five readings at once — comparable pairs, covering pairs, unit steps, join-homomorphism failures
  and the projection over realised value tuples — which is what let 13t-04 be stated as *no reading
  reproduces it* rather than *one reading does not*. Its cap-table sweep and its Cesàro reconstruction
  are the same shape as chat 86's 1,728-reading sweep and both found the printed reading exactly.
- **Chapter 19 segment carries (the next section read, main L5381 onward):** §19.1 The formalisation
  at L5386, and §19.5.1 at L5443 (*ρ is a property of (document, route)*), which Chapter 18 touches
  twice — L4978 sends depth to Chapter 19, and §18.6.1's bibliography row indexes on retrieval
  redundancy ρ. **Verify both boundaries by heading scan before reading**, and note that Chapter 18's
  own extent was mis-stated by every handoff that inferred it.
## Chat 88 additions (31 August 2026)

- **Closed:** the three-chat debt on the **bibliography catalogue**. `bibcat()` in r2-ch13v parses the
  main volume's References (L11503–L11855) into **103 entries across seven subsections** — R.1 7,
  R.2 3, R.3 11, R.4 9, R.5 25, R.6 9, R.7 29 — carrying line, subsection, year and read-in-full flag,
  with 99 dated entries from 1744 to 2026 and 39 pre-1970. **Lift into r2lib with provenance
  "r2-ch13v.bibcat, chat 88".** The parse is sensitive to two things found the hard way and both fixed:
  entry heads may carry a bold prefix (`**Edlén, B.**`), and the author-name class must be all Unicode
  letters, not a hand-listed set — the first draft silently dropped Edlén and Paschen & Götze, which
  are exactly the entries Chapter 19 is about. The three catalogues still owed are the periodic table,
  Janet and the audits.
- **Added, 19v-01 … 19v-07 (R3):** see READ-ch13v.md. The two that block more than a line:
  **19v-01**, L5488's *twenty-seven of the forty-nine cells in the table above*, where seven readings
  were swept and **the only reading giving 49 is seven cells × seven route types and the only reading
  giving 27 is 49 − 22**, both figures being §18.6.1 L5325's (*twenty-two sources over seven cells*)
  and neither describing the table at L5450–5454, which is 4 × 5 = 20 cells; and **19v-02**, where
  §18.6.1 gives the bibliography **E = 6** over **seven** cells indexed on *era, ρ, access, depth of
  entry*, while §19.5.3 gives **E = 0** fibred and unfibred over a **pooled 6** cells indexed on
  *age · language · access* fibred by route. R3 must rule whether these are one index or two before
  either figure moves; 19v-01 depends on the ruling, since its exact reading is built from §18.6.1's.
- **Chapter 18 inherits: 19v-03.** §18.3 L4977–4978 sends *depth* to Chapter 19 — *"Chapter 19 makes
  that precise"* — and MEASURED over L5381–L5548, **depth, channel and measured members each occur
  zero times**. §18.6.1 nevertheless keeps *depth of entry* as a coordinate of the index §19.5.3
  rebuilds without it, so 19v-03 and 19v-02 move together. The 13l-05 class, sharper.
- **Chapter 16 inherits: 19v-05.** L4550–L4551's *"§19.5 already says otherwise: a blocked ρ = 1 cell
  is a stated gap, not an unexplained absence"* — MEASURED, that sentence occurs once in Chapter 19,
  at **L5545**, inside **§19.6 step 6**; §19.5 is L5432–5442. The chapter-level site at L628 is sound.
  The 13d-01 / 13l-03 / 13o-01 / 13p-06 / 13r-05 / 13t-08 class.
- **Production pass inherits: 19v-04.** Figure 19.1's caption (L5416–5417) prints the four German
  documents at *one or two apiece, all closed* against §19.5.1's own ρ = 0, 2, 3, 3 and its
  *three of the four are retrievable*. §19.5.1 names §19.5's sentence and its law as wrong and never
  names the caption. Co-located stale text, chat 70's ruling.
- **References pass inherits: 19v-06 and C3.** The volume cites *Edlén's **Handbuch** chapter
  (**1964**)* at L5433 and L5453 and §29.5's heading, while the References carry **Handbuch der Physik
  27 at 1960** (L11621) and **Encyclopedia of Physics at 1964** (L11624) — no single entry carries the
  pair the chapter cites twice. And Dunz 1911's *Seriengesetze der Linienspektr**a*** differs by one
  letter from Paschen & Götze 1922's *Seriengesetze der Linienspektr**en***; **no conflation is
  claimed**, but the Dunz title needs an external witness before repair, since Dunz is also the one
  citation the book says cannot be confirmed.
- **The tables pass inherits: 19v-07.** §19.6 step 2 lists **seven** route types (EXACT); the §19.5.1
  table prints **five** columns, omitting preprint and database; the §19.5.3 fibre table prints
  **six**, omitting database. Neither omission is stated, and L5488's *forty-nine* is computed against
  all seven.
- **Not re-measurable, recorded not identified:** *nine searches* (L5436) and *three coverage gaps*
  (L5430), each one site in the six volumes, bare counts with no population and no witness. And
  §18.6.1's *twenty-two sources*, one site, against a catalogue of 103 entries (74 excluding R.7) —
  the population is unstated, which matters because 19v-01's exact reading is built on it.
- **For R4:** **no compendium volume points into Chapter 19.** MEASURED across mc, pc, ioi and sc:
  zero section-level pointers. Incoming pointers are main L357, L628, L4550, L4978, L7410, L8039 and
  index rows L11468–L11472, plus Register L1505, L2121, L2125, L2133, L2149, L2153, L2157, L2161,
  L2165, L2169.
- **Still owed to r2lib and untouched:** r2-ch12c/e/g/h's functions; chat 75's `closure_chunked`,
  `fixed_point`, `length`, `fibre_check`, `criterion`; chat 76's `terms`, `new_terms`, `jc_values`,
  `TERMS`, `phi_at`, the multiplicity-weighted `densities`; chat 77's stage-composability sets;
  chat 78's `first_fail` / `failing_pairs`; chat 79's `sections(X, w)` and `R(X)` / `failing(X, op)`;
  chat 80's `Rn(X)` and the interval Box/binding measure; chat 84's numeric-Jacobian `rank` pair,
  Slater-determinant term engine and alphabet sweep; chat 85's `therm` / `untherm`, `lat_closure`,
  `Rtree` and `pushback`; chat 87's `viol`, `failcount` and `parts`. **New this chat and worth
  lifting: `bibcat`**, and r2-ch13w's **exact-token heading resolver** — `re.match(r'^#{1,4}
  (\d+(?:\.\d+)*)\.? ', t)` compared for equality, with an extent that stops at the next heading of
  the same or a higher level. The prefix resolver every earlier prose batch used sends §19.5 to
  §19.5.3, §21.5 to §21.5.5 and Chapter 28 to A.28; this was self-caught here before banking, but
  earlier chats' pointer verdicts on multi-level numbers should be re-run against the fixed resolver
  when R3 opens.
- **Instruments:** r2-ch13v (computable, ≈ 3 s) and r2-ch13w (prose, ≈ 0 s), banked and deterministic;
  both fit any gate run list together. r2-ch13v's exhaustive set-system sweep is worth reusing for any
  claim of the form *k redundancy survives k−1 losses*: 65,536 systems on four cells and four sources
  settles it outright, and it generalised §19.1's theorem to all k at no cost.
- **Chapter 20 segment carries (the next section read, main L5551 onward):** PART IV — THE LANGUAGES
  opens at **L5549** and Chapter 20 *The languages, and what each one can close* at **L5551**, with
  §20.1 L5556, §20.2 L5571, §20.3 L5582 and Chapter 21 opening **L5597** — MEASURED by heading scan
  this chat. Chapter 20 is 46 lines and Chapter 21 is long (§21.5 alone runs L5645–L5873 with five
  subsections), so **Chapters 20 and 21 are not one section read**; take Chapter 20 whole and verify
  Chapter 21's extent by its own scan. §19.5.1 L5492 sends *this is §21.5's obstruction* forward, and
  §21.5.1's *the three-body count is exactly one* is executed carried state's residue — check it
  against W-107 rather than re-opening the Phase 0–4 plan.

## Chat 89 — deferred out of the Chapter 20 read

- **20x-12, §20.1's *fifty sections*, not measurable as printed.** *Makes a claim about language* is
  defined nowhere in the volume. The word proxy measures 40 of 515 numbered sections carrying
  *language(s)*, 13 of them before L5551 — an over-count on one reading and a lower bound on another.
  R3 must either define the predicate or replace the figure with a measured one; it cannot be checked
  as it stands.
- **20x-C2, the endpoint restoration.** L5594–5595 promises that a language moving the hole to an
  endpoint restores closure. On Λ₉ the only band available for the parity rule is |Δℓ| ≤ 1, which is
  the whole index — it closes because it excludes nothing. Whether a **non-trivial** endpoint
  restoration of this rule exists at any index of the tower was not settled; Λ₁₀ upward is where to
  look, and r2-ch13x's E-over-relabellings sweep is the instrument to extend.
- **20x-06 and 20x-05 are repairs that cannot be made line-local.** Logic's status and the naming of
  the six languages each disagree across main, Register and Mathematical Compendium. R3 cannot fix
  either at the citing line; both need a ruling on which doctrine stands before any site is touched,
  and the Register's L4381 is append-only, so the correction path runs forward through a new entry.
- **The chat-88 resolver repair is confirmed, not discharged.** r2-ch13y used the exact-token resolver
  on §11.1, §11.1.1, §12.11.2, §12.11.8, §14.4, §16, §17.3, §21, §27, §29 and §29.1 and resolved every
  one correctly; under the old prefix resolver §21 would have gone to §21.5.5 and §16 to §16.6.1. The
  standing item — re-run earlier prose batches' multi-level pointer verdicts against the fixed
  resolver when R3 opens — stands unchanged.
- **Instruments:** r2-ch13x (computable, ≈ 16 s) and r2-ch13y (prose, ≈ 0 s), banked and
  deterministic; both fit any gate run list together. r2-ch13x's two reusable pieces are the
  **relabelling sweep** — recompute (|X|, E) over every bijection of a coordinate's value alphabet,
  which settles any claim of the form *this notation makes the law monotone* at the cost of one E per
  relabelling — and the **convexity-versus-closure sweep** over every coordinate pair and every subset
  of an attained range, 686 preimages on Λ₉, which is the general form of §17.3's criterion.
- **Chapter 21 segment carries (the next section read, main L5597 onward)** — MEASURED by heading scan
  this chat: Chapter 21 *Translation, and what it costs* opens **L5597**; §21.1 L5599, §21.2 L5616,
  §21.3 L5624, §21.4 L5636, §21.5 L5645, §21.5.1 L5690, §21.5.2 L5708, §21.5.3 L5761, §21.5.4 L5797,
  §21.5.5 L5835, §21.6 L5874, §21.6.1 L5905, §21.6.2 L5924; **PART V — THE METHOD opens L5937** and
  Chapter 22 *The bracket* at L5939. The chapter is **340 lines and thirteen headings**, which is
  larger than any single read in Phase R2 so far, so it splits: **L5597–L5689** (§21.1–§21.5 opening,
  93 lines) is one read and **L5690–L5936** (§21.5.1–§21.6.2, 247 lines, the three-body material and
  the coordinate-relativity sections) is at least one more. §19.5.1 L5492 sends *this is §21.5's
  obstruction* forward into it, and §21.5.1's *the three-body count is exactly one* is executed
  carried state's residue — check it against W-107, not by re-opening the Phase 0–4 plan.
- **Chapter 21 inherits Chapter 20's open findings.** §21.1's title, *One object, two namings, and E
  is the price*, is the general form of the claim 20x-01 refutes in its instance, and Chapter 21 names
  the |Δℓ| ≤ 1 band at L5606 and the E / void / slack identification at L5610. Both were measured this
  chat and can be carried in rather than re-measured: the band is the whole of Λ₉ with E = 0, and the
  trio agrees with §27.
## Chat 90 — deferred out of the Chapter 21 first-part read

- **The seed class is one repair, not four.** 21z-01 (L5685 *ten cells for 976*, measured **7**), 21z-02
  (L5676 the parity rule's seed 13, measured **7**, printed column 763 → 757), 21z-04 (L5682 *near
  fifteen* against L5686 *nearer twenty*, totals 45 against 50) and 21z-05 (L5683 *a seed near
  twenty-five carries all 199,130*, the printed ratio giving 2,040) all descend from the same withdrawn
  *ten to thirteen* band that §14.5.9 L3934 retired. R3 repairs them together or not at all: the two
  estimates are derived from the ratio, so correcting L5685 alone leaves L5682/L5686 wrong in a new way.
  The compression column is unchanged at one decimal by the correction — MEASURED, not assumed.
  **The class recurs downstream:** L5799 (*§14.5.7 makes the seed a covering problem*) and L5826 (*the
  seed is MONOTONE in S*) are inside chat 91's range and must be measured against the same 7.
- **§14.5.3–§14.5.7 carry no body** — five consecutive headings, L3800–L3809, zero body lines each,
  MEASURED. §14.5.7 is cited from nine sites (L1203, L3812, L3919, L3923, L4107, L5656, L5799, L7799,
  L11759), one of which is the citation §21.5's repair rests on. Whether this is a production loss at a
  build or an authoring gap **cannot be told from the file**, and the two have different repairs — the
  first is recovered from an earlier build in Prints & Proofs, the second is written. R3 cannot open this
  without a ruling from M, and the Prints & Proofs witness (Ruling 56) is where the evidence is.
- **The relabelling class is closed at this index, open above it.** No relabelling of any coordinate's
  value alphabet takes the 840-cell parity object to E = 0 (118 relabellings, nine coordinates, least E
  **114** at *f*). This settles the general form of 20x-01 on Λ₉ and settles §21.1's row 3. Chat 89's
  **20x-C2** — whether a *non-trivial* endpoint restoration exists anywhere in the tower — is **advanced
  but not closed**: the sweep shows renaming values cannot do it, which leaves genuinely different bands
  at Λ₁₀ and above as the only remaining place to look.
- **The periodic table is 118 or 90 and the volume prints both.** L5604 names *the 118 elements*; L1613,
  L3243 and L5674 all measure 90 cells, all at E = 36. Cross-chapter: the repair touches Chapter 1's
  table and Chapter 12's as well as Chapter 21's two.
- **audit 21 does not resolve.** The phrase occurs once in the six volumes (L5647). The audit index is 21
  cells (L3851, L5673) and §3.7 L1315 splits the order into *ten audits, nine, and a pair*, but no member
  prints a numbered audit list. R3 needs the numbering settled before the citation can be repaired or
  removed; it is a citation to an object the reader cannot reach.
- **Doctrine items unchanged from chat 89, now with a second citing site.** 20x-04 (six languages against
  seven) and 20x-09 (C(5,2) against C(6,2)) are both re-asserted at L5611, which prints *six languages
  agree; ten combinations hold*. Still needs M's ruling on which doctrine stands before any site moves.
- **13t-02 strengthened, not closed.** The audit set's E is **16 at four sites** (L3851, L5025, L5607,
  L5673) and **17 at one** (L5062). The majority reading is now measured, and L5062 is the outlier.
- **Owed to r2lib:** `seed_of(cells)` — the cover_model → cover_reduce → exact_seed wrapper used four
  times this chat — and the **all-coordinate relabelling sweep** generalising r2-ch13x's single-coordinate
  version. Both are copied verbatim inside r2-ch13z.py with provenance comments until lifted.
- **Chapter 21 second part (chat 91, main L5690–L5936, 247 lines, seven headings)** — boundaries MEASURED
  by heading scan in chat 89 and re-confirmed this chat: §21.5.1 L5690, §21.5.2 L5708, §21.5.3 L5761,
  §21.5.4 L5797, §21.5.5 L5835, §21.6 L5874, §21.6.1 L5905, §21.6.2 L5924, PART V L5937, Chapter 22
  L5939. §21.5.1's *the three-body count is exactly one* is executed carried state's residue — **check it
  against W-107, do not re-derive it and do not re-open the Phase 0–4 plan.** The range is longer than any
  single read so far and may need splitting again at §21.5.5 or §21.6.

## Chat 91 — deferred out of the Chapter 21 second-part read

- **The Λ₁₃ constraint-graph repair is already specified by the record and needs no new measurement.**
  Register 1790 (reg L6603) withdrew §21.5.3's table and figure 21.1's caption and states the measured
  graph: 13 nodes, 14 edges, cycle rank 2, girth 3, one triangle 2S′–g–v from Λ₁₀ onward, diameter 6,
  radius 4, treewidth 2, hub k at degree 4 with g also at 4, degrees 4, 4, 3, 3, 2, 2, 2, 2, 2, 1, 1,
  1, 1, leaves n, e, 2S, 2J, second cycle 2J_c–2K–f–g–q–k at Λ₁₂. Chat 91 reproduced all ten fields
  independently from tower-2.py's bounds. **Three sites carry the withdrawn figures: main L5745
  (caption), main L5765 (table), reg L1953 (Register 523).** Register 523 is append-only and is
  corrected by 1790, not edited (Ruling 29 does not apply — this is not a pointer removal). R3 repairs
  the two main-volume sites. **Figure 21.1's artwork is part of the repair**: 1790 records that the
  drawing omits Λ₉'s 2S′ and gives v the parents 2S and g, so the image is wrong in the same way the
  caption is, and redrawing needs M's instruction.
- **Census row 1128 is inside this class.** *"the one place in this work where ℛ has never been the
  right operator"* (L5699) is false once the tower itself carries a K₃ from Λ₁₀; closed as a defect
  and repaired with 14b-05 or not at all.
- **The star-seed class is two sentences, and the rest of §21.5.4 is already correct.** L5813–L5814
  (*the path and the star at eight and seven*) and L5818–L5819 (*seeds 8, 7, 6, 6, 6, 5*) are the only
  survivors of the withdrawn 7; the table, the monotone-in-S list and the closing paragraph all carry
  6. MEASURED exact seeds 8, 6, 6, 6, 6, 5. This is the same class as chat 90's L5685 seed band, and
  the two should be repaired in one pass.
- **"The largest orientation cost anywhere in this book" is a superlative with two counterexamples**
  (main L5843 at 15, mc L462 and reg L1773 at 750). R3 must decide whether the sentence loses the
  superlative or gains a scope; the sites are main L5785 only, but the neighbouring claim at L5786
  (*the first object on which the second operator is the only one that works*) is untested and should
  be measured before the sentence is rewritten.
- **Three pointers do not resolve and each needs a target, not a deletion.** L5692 → §32.3 (the claim
  is Register 489's); L5753–L5755 → §18.4.1 for a sparsity statement that section does not make, and
  it is the stated ground for not reading twenty-three absent constraints as predictions, so removing
  the pointer removes the argument; L5860 → §17.1, which is two lines about which cells may be added.
  R3 cannot fix these by grep — each needs the intended section identified.
- **L5704's "Registers 487–489" over-cites by two entries** (487 and 488 are off topic; 489 carries
  the claim). Cross-check when the citation counts are recomputed: register_cites.py counts the range,
  so narrowing it changes the count.
- **§14.5.7 remains heading-only and is still the ninth citing site's target** (L5799). Re-measured
  from the file this chat: zero body lines. Chat 90's item stands unchanged and still needs M's ruling
  on production loss versus authoring gap before R3 can open it; Prints & Proofs is the witness.
- **L5854's "eight rows of twenty-eight" leaves twenty against a table of twenty-four**, and
  Register 532 carries the same wording, so the gap of four is in the record as well as the volume.
  A repair to the volume alone would leave the two disagreeing.
- **Register 487 prints "Λ's eight constraints"** where §21.5.2 and tower-2.py give seven binary
  bounds. Out of range, unmeasured beyond the count itself, and it touches every site that states Λ's
  constraint count. Flagged for the cross-volume pass (R4), not for R3.
- **Owed to r2lib:** `greedy_seed(cells)` (the tie-break-sensitive greedy cover, useful for testing
  any further "greedy was wrong here" claim), the exact `treewidth(nv, E)` elimination DP, and the
  `girth` / `ecc` / `is_caterpillar` graph primitives. All are inside r2-ch14b.py with provenance
  comments until lifted. `seed_of()` is still owed from chat 90 and is now used by two instruments.
- **Method note for chat 92, from an error made this chat:** before recording any printed figure as
  unreproducible, grep the Register for a later entry naming the section. Register 1790 supersedes
  §21.5.3 and was found only after the disagreement had been written up as a reconstruction failure.
  The Register's late entries (1780–1792) are corrections to earlier chapters and are not indexed from
  the sections they correct.
- **Chapter 21 third part / Chapter 22 (chat 92, main L5874–L5936, 63 lines, three headings)** —
  boundaries MEASURED by heading scan this chat: §21.6 L5874, §21.6.1 L5905, §21.6.2 L5924, PART V
  L5937, Chapter 22 L5939, §22.1 L5943, §22.1.1 L5953, §22.1.1.1 L5982. The range is short, so
  §21.6–§21.6.2 and Chapter 22's opening may fit one chat; confirm every boundary by scan first.
## Chat 92 — deferred out of the close of Chapter 21 (main L5874–L5936)

- **The companion-citation form is a class, not three sites** (14d-01). §10.4 at L5928, §8.1 at
  L5932 and §10.1 at L5933 print companion sections in the bare `§N.N` form, and all three numbers
  exist as main-volume sections with unrelated content. The marked form `T §N (App. G)` is already
  in use — 2× main, 8× Register, 3× Mathematical Compendium, and at mc L2498 for this very claim.
  R3 must sweep the whole main volume for bare companion pointers, not just these three: the two
  existing `T §` sites in the main volume prove the form is known there but not applied. A grep for
  every `§N.N` whose resolved main-volume section is off-topic is the census R3 needs, and it has
  not been run outside this range.
- **L5911's envelope-step count** (14d-03) is the one false term of a five-term claim whose other
  four hold. R3's repair is a narrowing — to the reduced model, or to the seed — not a withdrawal.
  The same sentence's *same seed* is true and is the interesting half. Note that the rebuild of the
  book's 102-element model (25 value slots + 77 raising steps) is an independent confirmation of
  L3981's *87 of 102* and should be cited when that figure is next touched.
- **L5917's missing scope** (14d-02) cannot be fixed by inserting *of the companion's four* alone:
  §21.6.2's own heading names **five**, and no site in any of the six volumes enumerates the five.
  R3 needs the enumeration before the sentence can be scoped, and the enumeration is companion-side.
  Register 547 and Register 548 disagree in the same way (four against five) and both are
  append-only, so a new entry citing both is the only correction path.
- **The retired V-numbering** (14d-04) reaches further than §21.6.1. Main L4256–L4257 and Register
  544 record that §8.4 retired it and that V6 is not a vocabulary index at all; §21.6.1 uses V6 and
  V3 with no caveat. Every site naming a V-index under the old numbering needs the same treatment,
  and that census has not been taken. The arithmetic drawn from those boxes is sound — 24, 48 and 64
  each force their rung multiset uniquely — so this is a naming repair, not a numerical one.
- **"V3 geometry" is named twice and defined nowhere** (C-3), both sites inside this section, and it
  is the only row of the L5880 table with no second site in any volume. Either it is defined
  elsewhere under another name, or the row rests on an object the reader cannot reach. R4.
- **The periodic table's two counts** (C-4). §21.6 L5881 and main L1613 give 90 cells at E = 36;
  §21.1 L5604 names the same object *the 118 elements* at the same E = 36. Only the 90-cell reading
  is consistent with 7 × 18 = 126. §21.1 is chat 90's range and was not re-opened; this is a
  cross-chapter item and must be settled in one pass with L5881, not separately.
- **"a random 26-cell set, E = 38"** (C-2) has one site in six volumes and no printed set. R3 either
  supplies the set or drops the row; the row's own arithmetic (2 × 13, E = 0) is verified and can
  stand on any 26-cell example.
- **Companion-side claims recorded as unverified, not as deviations**: *one cell from where
  half-sided modular inclusion is proved* (L5929–L5930), *§8.1 prints five chargers*, *§10.1 counts
  six*. The companion is not a member of either bundle. If it is ever seated as a member these three
  become measurable in one pass; until then they cannot be closed either way, and R4 should say so
  rather than leave them open-looking.
- **§14.5.7 remains heading-only**, zero body lines, still the target of the ninth citing site
  (L5799) and of the construction §21.5.4 rests on. Unchanged from chats 90 and 91 and now three
  chats old. It needs M's ruling on production loss versus authoring gap before R3 can open it;
  Prints & Proofs is the witness.
- **Owed to r2lib**, still unlifted and now used by more than one instrument: `seed_of()` (chat 90),
  `greedy_seed(cells)`, the exact `treewidth(nv, E)` elimination DP, and the `girth` / `ecc` /
  `is_caterpillar` primitives (chat 91). Chat 92 adds `rung_multisets(box, letters, lo)` — the
  factorisation enumerator behind [D4] and [D5] — and the `E(X)` / `grid(X)` pair built on
  `r2lib.Rset`, all inside r2-ch14d.py with provenance comments.
- **Method note for chat 93, from this chat's own errors.** Two of the six instrument faults were
  keyword tests that would have recorded a *resolving* pointer as a failure, and one was a substring
  match that inverted a verdict. Before recording any pointer as unresolved, read the target section
  and test for the claim as that section words it, not as the citing sentence words it; and test
  case-exact and word-bounded, since `STAT` matches *state* and `four` matches *four letters*.
- **Chapter 22 (chat 93, main L5939 onward)** — boundaries MEASURED by heading scan this chat:
  PART V L5937, Chapter 22 L5939, §22.1 L5943, §22.1.1 L5953, §22.1.1.1 L5982, **§22.1.2 L6006**.
  Confirm every boundary by scan again before reading a line; the range beyond L6006 was not scanned.

## Chat 93 — deferred out of the Chapter 22 read (main L5937–L6035)

- **F.3's four-column standard is a class test, not a Chapter 22 item** (14f-01). §22.1.1.1 claims
  *F.3's highest standard* on three columns. F.3 (main L11278–L11300) states four — the method, the
  input set, the inputs, the refutation — and says a statement carrying fewer than four is a different
  kind of object. R3 must grep **every site that cites F.3 or claims its standard** and test each for
  all four columns; that census has not been taken. The repair for this site is either supplying the
  refutation (a level failing containment is the available falsifier, and the table's *contained*
  column could have printed less than 9) or dropping *highest*. The decision is M's, but the census is
  R3's and is wider than one section.
- **The printed-input standard is broken one subsection after it is claimed** (C-1). §22.1.1.1 prints
  its input set in full; §22.1.2's seven widths are reproducible only at δ = 0.35, which the section
  never prints. Same for M in §22.1.1 (C-2), which the *N ≈ √(M/m)* bound needs and which solves to
  the deuteron mass. Both are one-word repairs, but they belong with the F.3 sweep above rather than
  as isolated fixes, because the standard is what makes them defects.
- **Register 319's placement, and the entry that does not exist** (14f-03). Moving the pointer to the
  end of L5975 fixes the citation. It does not fix the gap it exposes: **no Register entry carries the
  one-dimensional refinement of §18.4.1's criterion** — *for a bracket on one chain, monotone in
  either direction suffices; only closure in a product requires increasing*. That is a subject-matter
  claim standing without a record. Register entries are append-only and this one is missing, not
  wrong, so R3 writes a new entry rather than correcting 319. Held until the review closes.
- **The "single run" §22.1.1.1 improves on has no printed site** (14f-02). Before L6004 can be
  repaired, R3 must determine whether a one-defect containment run is printed anywhere in the six
  volumes or whether the comparison should read *what a single defect could not distinguish*. A grep
  for a containment run outside §22.1.1.1 has not been made; §22.1 itself prints none, which is what
  this chat measured.
- **§33.4 and §22.1.1 are an unlinked conceptual twin** (C-5). *An index is closed when its output
  class is a singleton* against *a bracket whose admissible set is a singleton*. Same structure,
  different objects, and neither section points at the other — tested both ways. R4: either a
  cross-reference in both directions, or a single sentence naming the relation and its limit. Note
  that the Index of Indices (ioi L1609–L1611) and the Mathematical Compendium (mc L3753) both carry
  the output rule and neither carries the bracket use, so the compendia would need the same link.
- **The companion paper is cited, listed and unmeasurable** (C-8). *Muon-Catalysed Fusion*, Lach 2026,
  is at References R.3 (main L11598–L11601) and is **not a member of either bundle**. Three claims in
  this range are companion-side: the paper's own 61 / 4.2 / 1.03, the first observed r_ℓ exit
  predicted from ν⁻³ scaling, and the reference line's own list of reproduced figures (cycle cap
  2.6 × 10⁸ s⁻¹, breakeven sticking 0.203/0.262/0.292 %, decay lengths 11.2 m and 623 m). This is the
  same standing item chat 92 recorded for the *other* companion: if either paper is ever seated as a
  member these close in one pass, and R4 should say they are unverifiable rather than leave them
  looking open. This book's own recomputation of the trio **is** verified (14f-B6).
- **Register 391's markup** (C-6). Five unbalanced emphasis runs (`* **`) inside one entry, closing
  the wrong span mid-sentence. Production class, noted not repaired, per M's standing priority — but
  the Register is reader-facing and this is the second entry found with the fault, so R3 should sweep
  the Register for the pattern rather than fixing one entry.
- **L6003's order-of-magnitude claim** (C-4) is true of the output energies (107×) and loose for the
  input δ (7.57× between the nonzero extremes, undefined from zero). Register 391 restates it in the
  same form. If R3 tightens the sentence it must tighten the Register entry's successor too — the
  entry itself is append-only.
- **Owed to r2lib**, unchanged from chat 92 and not added to this chat: `seed_of()`, `greedy_seed()`,
  the exact `treewidth(nv, E)` DP, the `girth` / `ecc` / `is_caterpillar` primitives,
  `rung_multisets()`, and the `E(X)` / `grid(X)` pair on `r2lib.Rset`. Chat 93's instruments needed
  none of them — Chapter 22 is arithmetic on a Rydberg series and pointer resolution, with no tower
  computation at all, which is why r2-ch14f does not import r2lib.
- **Method note for chat 94, from this chat's own errors.** Four instrument faults, all caught before
  banking. The one to carry: **after writing any verdict that compares two measured numbers, re-read
  the comparison against the numbers.** F11 printed *LARGER* for 0.29 % against 2.72 % and drew the
  opposite conclusion from the correct measurement. This is chat 92's inverted-verdict class in a new
  form — there a substring match, here a comparison word — and in both chats the arithmetic was right
  while the sentence built on it was wrong. Also: a summary line that generalises over a list must be
  written after the list is printed, not before (G8 described nineteen sites it had not yet classified).
- **Chapter 22 remainder (chat 94, main L6036 onward)** — boundaries MEASURED by heading scan this
  chat: §22.2 L6036, §22.2.1 L6056, §22.2.2 L6071, §22.2.3 L6087, §22.2.4 L6101, §22.2.5 L6107,
  §22.3 L6129, §22.4 L6138, §22.4.1 L6148, §22.5 L6168, §22.6 L6175, chapter ends L6178 (Chapter 23
  opens L6179). 143 lines, eleven headings. Confirm every boundary by scan again before reading a
  line. §22.2's *four rules* and §22.2.1's ablation are the computable core; §22.3's *limit-free* and
  §22.4's *price of limit-freedom* are where the prose batch will sit.
## Chat 94 — deferred out of the Chapter 22 remainder read (main L6036–L6177)

- **§32.3 is a citation class, not a site** (14h-05). Four prose citations of §32.3 exist in the
  main volume and three disagree with the section: L5692 cites it for ℛ reaching level 2 (chat 91),
  L6138 for presenting limit-freedom as pure gain (this chat), and L7492's erratum speaks of its
  *four clauses* where three are printed (ⅅ_def, ⅅ_phys, D3). The three index entries at
  L11472/L11476/L11477 resolve. R3 should treat this as one docket: read §32.3 once, then test all
  four prose citations against it, rather than repairing sites as they are met. The candidate target
  for L6138 is **App A.12** (*The bracket is limit-free*, L10022) or **§22.3** itself, both of which
  carry the claim; the decision is M's and the census is R3's.
- **"ν, δ and V all need the ionisation limit" stands at two sites** (14h-02): main L6133 and App
  A.12 L10035, worded almost identically. V = w/e is invariant under T = I − E by the same
  cancellation A.12 proves for containment. One decision, two sites, and App A.12's Consequence is
  the more load-bearing of the two because it is the theorem's own statement. Note that the repair
  is not simply deleting V from the list: V *expressed as* 4ν/3 does need the limit to evaluate,
  while V *measured as* w/e does not, and the sentence needs to say which it means.
- **The σ collision is chapter-wide, not §22.5-local** (14h-01). Rule 4 (L6047) and §22.5 (L6168)
  use σ for different quantities. Before R3 rewrites either, it must grep every σ in Chapters 22–23
  and in App A, because the cost surface of Chapter 23 uses the same symbol again and the
  admissibility ratio is quoted in the Spectra Compendium. Whether *r falls as ν⁻³* survives depends
  entirely on which σ the book means, and that is a subject-matter decision.
- **The unprinted-input class now has six members and should be repaired as one class, not six
  edits** (14h-08, 14h-09, and chat 93's C-1/C-2). §22.1.2 needs δ = 0.35; §22.4.1 needs δ₂ = 0.06;
  L6060's 446×, L6068's 1,577, L6093's 3.47 % and L6104's *factor of 17* each need an input more
  precise than the one printed beside them. §22.1.1.1 claims F.3's highest standard, whose columns
  include the input set. R3's census is: **every site in the six volumes that prints a derived
  figure beside its inputs, tested for whether the printed inputs reproduce it.** That census has
  not been taken and is wider than Chapter 22.
- **Seventeen single-witness figures in 141 lines** (C6). 69.6, 41.3, 12,942, 0.8189, 0.7129,
  0.7376, 0.7835, 3.47, 14,602, 4,329, 4,267, 1.387, 1.386, 68.06, 0.00102, 0.0210, 7.613 appear at
  no other site in any of the six volumes. They are internally consistent where a check exists
  (H5, H12, H13 all reproduce from them) but nothing in the collection can contradict them. This is
  the same standing item as chat 93's C-8 and chat 92's companion-paper note: R4 should state which
  figures are unverifiable rather than leaving them looking checked.
- **§25.6's vocabulary is unsettled inside itself** (C4). Its title and §25.6.3 deny that the Sc VI
  value is a prediction; its own opening line at L6992 and §25.6.6's title use the word. Ten uses
  against three of *deduction*. Chapter 22's L6098 follows the second usage, so the citing site
  cannot be judged until §25.6 settles. R3 must fix §25.6 before it touches L6098, and the order
  matters — repairing the citation first would lock in the usage the section is trying to withdraw.
- **The antiprotonic-helium pointer needs a target chosen, not corrected** (14h-05). L6135's cells
  are at §16.4 (L4419) and §19.2 (L5401, L5416); §2.8's L612 already names §16.4 for the same
  check, so the book has a working form to copy. But §16.4 and §19.2 use the case for different
  purposes — an apparatus check and a retrieval-redundancy count — and only M can say which one
  limit-freedom is supposed to have admitted.
- **§22.6's *only linearly rising quantity* and Chapter 23** (14h-06). The counterexample is
  §22.4's L = n/3, and §23.1's general V(x, p) = 4x/(h|p − 1|) adds one per p ≠ 1. Chapter 23 has
  not yet been read, so R3 should not repair the sentence until the cost surface is read — the
  qualification it needs may already be stated there.
- **Row 4 of the ablation table** (C2). ±1σ coverage 96.2 % against 69.6 %, with the nominal at
  68.3 % unstated. The row is the only one where the larger number is the violation, and it reads
  as a defect of the table rather than of the rule. R3 should consider printing the nominal.
- **Owed to r2lib**, unchanged and again not added: `seed_of()`, `greedy_seed()`, the exact
  `treewidth(nv, E)` DP, the `girth` / `ecc` / `is_caterpillar` primitives, `rung_multisets()`, and
  the `E(X)` / `grid(X)` pair on `r2lib.Rset`. Chapter 22 needed none of them; neither instrument
  this chat imports r2lib. **Newly owed, and used twice this chat:** `section_span()` by dotted-number
  extension (rank fails because the book sets §25.6 and §25.6.1 at the same `###` depth),
  `has_token()` word-bounded matching, and an appendix-aware `enclosing()`. All three are in
  r2-ch14i.py with provenance comments and should be lifted before the next prose batch rather than
  copied a third time.
- **Method note for chat 95, from this chat's own errors.** Seven instrument faults, all caught
  before banking. The one to carry: **an instrument that contradicts a measurement already taken
  from the file is wrong until proved otherwise.** Twice this chat an instrument reported a pointer
  failing that the hand reading had already resolved, and both times the instrument was at fault —
  once through a span rule, once through a substring match. Second: **never round with Python's
  `round()` in an instrument**; it is binary and returns 17.2 for 17.25 and 2.1 for 2.15. Use
  `Decimal.quantize` and name the convention, because three of this chat's faults were that alone.
- **Chapter 23 (chat 95, main L6178 onward)** — boundaries MEASURED by heading scan this chat only
  for the chapter's opening: §23.1 L6180, §23.2 L6196, §23.2.1 L6215; the chapter runs to L6622 and
  Chapter 24 opens L6623. **445 lines, far larger than any section read yet closed** (93, 63, 99,
  141), so chat 95 must scan the headings forward, confirm every boundary on the member, and take
  §23.1–§23.2.x as the first unit rather than the chapter. Chapter 23 contains Proposition 23.1
  (L6199–L6204) with a printed proof, a figure at L6191 with a caption carrying 32/11 = 2.909 and
  26/9 and 0.69 %, and a pole at p = 1 — the computable core. Note that 14h-02 and 14h-06 both
  resolve against Chapter 23's definitions, so the read should confirm them rather than re-derive.

## Chat 95 — deferred out of the Chapter 23 first read (main L6178–L6302)

- **Chapter 23 is a third read, not one** (boundaries MEASURED this chat, whole chapter). The
  chapter runs **L6178–L6622, 445 lines, 37 headings**; Chapter 24 opens L6623. Chat 95 read
  **§23.1–§23.5.3, L6178–L6302, 125 lines, ten headings**. **Unread and owed: §23.6 L6303 through
  §23.15 L6606–L6622 — 320 lines, 26 headings.** Section starts, measured: §23.6 6303, §23.7 6321,
  §23.8 6333, §23.8.1 6336, §23.8.2 6349, §23.8.3 6365, §23.8.4 6372, §23.9 6383, §23.9.1 6387,
  §23.9.2 6404, §23.9.3 6421, §23.10 6434, §23.10.1 6438, §23.10.2 6452, §23.10.3 6486, §23.10.4
  6500, §23.11 6519, §23.11.1 6533, §23.11.2 6543, §23.12 6549, §23.13 6569, §23.14 6582, §23.14.1
  6595, §23.15 6606. **Re-scan them anyway** — this list is a measurement of this chat, not a
  licence to skip the scan.
- **The ν_V pointer is a class of two against a correct index** (14k-01). Main **L6270** and
  **L6923** both cite §23.11 for ν_V; §23.11 (*The refusal pattern carries four verdicts, not one*)
  carries ν_V, ceiling, granularity, quotation, curvature and resolve **zero times each**. The
  claim is at **§23.15** *The second admission bound* (L6606–L6621) and the index at **L11448**
  already reads *ν_V …… §2.3 · §23.14 · §23.15*. R3 should take this as one docket — read §23.15
  once, then test both citing sites against it — and should note that §23.14 also carries ν_V
  (L6585), so the index's three targets are all live and neither citing site is a near miss.
  §23.11 is now the second section in this book to be a **citation class rather than a site**,
  after chat 94's §32.3.
- **The Ga I attribution needs a subject-matter decision, not a correction** (14k-02). L6270 names
  *Al I at n = 51 and Ga I at n = 53* as the outliers sitting above the ceiling. §23.15 L6619 gives
  **Al I nf's four failing cells as n = 48, 51, 53, 54**; §23.15's ν_V table carries K I nd, Na I
  ns and Al I nf only, and **Ga I appears in §23.15 zero times**, so no ν_V exists for Ga I to sit
  above. Ga I's one nearby appearance is §23.11.1 L6538 — *Ga I 4s²np ²P°, 15 members, 1 refusal, a
  bifurcation*, a different test. Either the sentence merged two tables and should name Al I twice,
  or Ga I has a ν_V that no volume prints. Only M can say which, and the repair differs.
- **The 32/11 floor is a scope question spanning three sections and possibly two volumes**
  (14j-01). §23.3 L6233 prints *V ≥ 32/11 — no guarantee is ever cheaper than 2.909 ×* in a table
  of four unconditional impossibilities; §23.2 L6213 already qualifies it as *the tighter of two*;
  §23.4 L6242 then makes *h* free, and 4r³/(3r²−1) is minimised at r = 1 with **V = 2**. Before R3
  edits the table it must grep 32/11 and 2.909 across all six volumes — MEASURED this chat: main 8
  and 3, Mathematical Compendium 2 and 1, elsewhere zero — and decide whether the floor is stated
  for the h = 1 series or for V. The four-row impossibility table is quoted structure, so a scope
  clause added to one row may need the other three checked for the same defect.
- **The unprinted-input class now has seven members** (14j-05 joins chat 94's six). §23.1 L6189's
  *agreement under 1 %* needs h/x and prints neither: MEASURED, it holds at h/x ≤ 1/100 and fails
  at 1/10 (8.09 %) and 1/2 (60.92 %), worst always at p = +11. The R3 census DEFERRED already
  names — *every site in the six volumes that prints a derived figure beside its inputs* — should
  be widened to include figures whose inputs are a **regime** rather than a number.
- **The sign convention on e is chapter-wide and unstated** (14j-06). L6181 and L6200 define e with
  an absolute value; §23.5.1 L6283's printed w²/e is exactly the **signed** quantity, and for
  y = x⁻² that is the negative of the positive form, so *equals 8y′²/y″ only as h → 0* is off by a
  sign as the book defines e. Before R3 repairs L6283 it must find every site that writes w²/e,
  8y′²/y″ or w·V — main L7487 (Chapter 28's withdrawal), L8052 and L8577 are three, MEASURED — and
  decide once whether e carries its absolute value into the algebra or only into the definition.
- **The overgeneralisation pair is one repair, not two** (14j-03 and census row **1135**, which is
  upheld as a defect rather than closed as an artefact — the first row this phase to be upheld).
  §23.2 L6206's *This holds for any monotone sequence whatever* and L6208's blockquote *always more
  than twice* both drop Proposition 23.1's two hypotheses: strict monotonicity, and unequal steps.
  MEASURED, V = 2 exactly when a step vanishes and V is **undefined** when the steps are equal, an
  arithmetic sequence being monotone. §23.2.1's Observation states the condition correctly twelve
  lines below, so the book already contains its own repair wording.
- **p = 0 is a second degenerate exponent and the chapter names only p = 1** (14j-04). Inside the
  printed range p = −3…+11, y = x⁰ gives w = e = 0 while the formula returns a finite value.
  Whether the range should read *p = −3 to +11, p ≠ 0, 1* or whether p = 0 was never tested is a
  subject-matter answer; the sentence as printed claims it was verified there.
- **"Observation 14.2" in §23.2.1** (14k-03). MEASURED: the main volume declares exactly two
  numbered statements on indented lines — Proposition 23.1 (L6199, correct) and Observation 14.2
  (L6216, standing in Chapter 23). §14.2 exists at L3711. R3 should check whether Chapter 14
  declares observations at all before renumbering: if the label is a back-reference the repair is
  a citation, and if it is this chapter's own observation the repair is a number. The five
  *Proposition 23.x* hits at L7273, L7583, App C.1, C.2 and E.2 are **citations of Proposition
  23.1**, not declarations, and must not be swept into the same docket.
- **Rule 1's clauses are cited by ordinal and the ordinal is wrong once** (14k-04). L6219 credits
  *Rule 1's second clause* with excluding interleaving channels; clause 1 (same Rydberg sequence,
  shared term set) is what excludes them, clause 2 being interiority. R3 should check every
  by-ordinal citation of a rule's clause across the six volumes before repairing this one — the
  rules are printed as running prose at L6040–L6055, so an ordinal has to be counted rather than
  read, and this is the class of error that produces.
- **Thirteen single-witness figures in 125 lines** (C1): 26/9, 54/13, 256/47, 250/37, 4000/299,
  26.689, 53.3, 0.1743, 0.1750, 2.7886, 2.7450, 8.82, 7.83. Same standing R4 item as chat 94's C6
  and chat 93's C-8. Note that 8.82 is single-witness but **reproducible** — it recomputes exactly
  from R = 109737.31568, Z = 1, ν = 40, β/α = 10 — so the class should distinguish *unverifiable*
  from *uncorroborated*.
- **0.69 % carries two unrelated meanings twelve lines apart** (C2): L6194 the asymptote's error at
  ν = 2, L6268 the pooled median deviation of 1,033 measured pairs. Not a defect; a reader-facing
  collision worth a note in the R2 audit.
- **Owed to r2lib — four discharged, six still owed.** Lifted this chat: `heading_line()`,
  `section_span()`, `has_token()`, `enclosing()`, with `M` as an explicit first argument.
  **Still owed:** `seed_of()`, `greedy_seed()`, the exact `treewidth(nv, E)` DP, the `girth` /
  `ecc` / `is_caterpillar` primitives, `rung_multisets()`, and the `E(X)` / `grid(X)` pair on
  `r2lib.Rset`. Chapter 23 needed none of them.
- **Method note for chat 96, from this chat's own errors.** Thirteen instrument faults, all caught
  before banking, all rewritten. The three to carry: (1) **a formula numerator is not a value** —
  a bare `V = ([0-9.]+)` read *V = 2(d₀+d₁)/|d₀−d₁|* as an empirical V of 2 and reported three
  sites below a floor that has none, after the hand reading had already resolved the line; (2)
  **word-bounding applies to numbers too** — `str.count('2.2')` returned 71 main-volume sites for a
  figure that has six, reading it out of *§2.2* and *12.25*, and the first fix then excluded a
  trailing comma and deleted every figure printed in a list; (3) **a citation is not a
  declaration** — five *Proposition 23.x* references were scored as chapter-number mismatches. All
  three are the same fault as chat 94's *gain* inside *against*: a test that matches text without
  asking what the text is doing.

## Chat 95B — the §14.5 authoring gap, measured and closed as a question

- **§14.5.2–§14.5.7 are an authoring gap, not a production loss** — MEASURED against the Prints &
  Proofs original `The Method 1.6.md` (738,550 B · md5 49900cf41f818ab789bb90fc596ac977), where the
  six headings sit at P3764, P3766, P3768, P3770, P3772, P3774, each two lines from the next, with
  **zero non-blank body lines**. BUILD90 has the identical shape at L3798–L3809. §14.5 (22 body
  lines), §14.5.1 (24) and §14.5.8 (79) are intact in both. **Do not re-derive this and do not
  search for an earlier print** — the text never existed at the input, so no print carries it.
- **The class is six sections, not five, and §14.5.7 carries 24 citations, not nine.** The figures
  in HANDOFF-43 through HANDOFF-47 were carried, not measured. Corrected count, exact-token,
  heading lines excluded: §14.5.2 → 4 (Reg 3, Maths 1); §14.5.3 → 1 (main); §14.5.4 → 4 (Reg 1,
  Maths 3); §14.5.5 → 4 (Maths 4); §14.5.6 → 3 (main 2, IoI 1); §14.5.7 → 24 (main 11, Reg 9,
  Maths 4). **Forty citations in four volumes resolve to empty headings.**
- **The repair is authoring six sections, and it is R3's largest single item.** The titles state
  what each owes: *Two pairwise operators, and this book has used one name for both* (§14.5.3);
  *What E measures, exactly* (§14.5.4); *ℛ₄ — the four orientations, adopted* (§14.5.5); *What the
  second operator localises, and what it leaves undetermined* (§14.5.6); *The seed is constructible,
  and it is a size rather than a set* (§14.5.7); *The seed, and the expression of the cycle*
  (§14.5.2). §14.5.9's *the seed of Λ, exactly* and chat 90's settled **seed(Λ₈) = 7** are the
  material §14.5.7 is cited for; §21.5.4's whole construction rests on it.
- **Order matters for R3.** §14.5.7 is cited by the Register nine times, and Register entries are
  append-only — a section written to satisfy nine existing entries must be written to what those
  entries already say, not the other way round. Read the nine Register citations first, then
  §21.5.4, then author. The Mathematical Compendium's twelve citations across §14.5.4, §14.5.5 and
  §14.5.7 are the second constraint set.
- **This item is closed as a question and open as a repair.** Under the chat-95 ruling it is not
  put to M again.

## Chat 96 — deferred out of the Chapter 23 second read (main L6303–L6433)

- **§23.8.3's reason is a repair of a reason, not a figure** (14l-16). L6368 gives affine invariance
  as the cause of the Z/R cancellation; §23.8.1 L6345's λ² = (2/3)Z²R/ν² scales by Z² (MEASURED
  45.7239 / 182.8955 / 1646.0597 at Z = 1, 2, 6, ν = 40). Before R3 rewrites the passage it must
  decide **which invariance the chapter is claiming**: the Newton decrement is affine-invariant under
  maps of the domain, and V is invariant under rescaling because it is a ratio of two quantities
  homogeneous of degree 1 in Z²R. Both are true and only the second explains what §23.4 observed.
  Grep every site that offers affine invariance as a reason before repairing this one — §29.2
  (L7881), App D.4.1 (L10377) and §29.7 (L8052) are the three places the Nesterov material recurs,
  MEASURED, and any of them may carry the same reasoning.
- **The §25.6 pointer has no correct target** (14m-01). Unlike chat 95's 14k-01, which redirected to
  §23.15, nothing in the main volume carries *the field abandoned the variable*: *abandon\** has
  three sites, L1479 (§5), L3435 (§12.11.3.1) and L6319 itself. R3 chooses between **authoring the
  explanation** (in §25.6 or wherever the literature question belongs) and **dropping the clause**.
  Note the clause is load-bearing for the novelty claim beside it — *It is not in the literature* —
  so dropping the pointer leaves an unsupported negative.
- **The unprinted-input class now has eight members** (14l-24 joins chat 95's seven). §23.9.3 prints
  three V-on-T figures reproducible **only** under ν = n − 1.35, h = 1 (δ = 1.35 unique in [0, 3) at
  0.01) and three V-on-ν figures reproducible under **nothing** — the implied Ritz δ₂ is 0.034 at
  n = 10 and 0.046 at n = 20, so no single model fits the column. R3 must decide whether the column
  is wrong or its inputs are merely missing; the two repairs differ, and only the second is
  cosmetic. This is the first member of the class whose figures cannot be reproduced **at all**, as
  against reproduced-once-the-input-is-guessed.
- **The truncation-printed-as-equality class opens here** (14l-02, 14l-03). §23.6 L6306 prints two
  asymptotic forms with "=" and its own table then carries the exact values, which differ. §23.8.4
  L6381 then claims the asymptote *4ν/3* as an original result without saying it is the asymptote of
  the book's own exact V = 4r³/(3r²−1). R3 should sweep for the same pattern: **every display
  equation whose own table disagrees with it**. Related to but distinct from the 32/11 scope docket.
- **32/11 now has six main-volume sites, measured** (14m-10, extending 14j-01): L6193 (§23.1), L6213
  (§23.2), L6233 and L6237 (§23.3), **L6381 (§23.8.4)**, L10245 (App C.1); plus 2.909 at four main
  sites and the compendia counts chat 95 recorded. L6381 is the site that claims the floor as an
  original result, so it must be repaired **after** the scope decision 14j-01 owes, not with it.
- **The Nesterov attribution is five forms in five places** (14m-07): L6341 *Nesterov and
  Nemirovskii (1994)*, L7881 *Nesterov & Nemirovskii*, L8052 *Nesterov 1994*, L10377
  *Nesterov–Nemirovskii*, L11653 *Nesterov, Y.* One is substantive — **L8052 credits Nesterov alone**
  for λ² = f′²/f″, which §23.8.1 credits to both. R3 should treat the name-form sweep as one docket
  across all six volumes rather than repairing this chapter's site alone, and should check whether
  other attributions (Moore, IEEE 1788) vary the same way.
- **Two unattributed quotations inside the attribution section** (C3). §23.8.4 quotes *114% of
  optimal width* (L6375) and a full sentence at L6378–L6379 with no source. The section exists to
  make attributions; these two are the only claims in it that make none.
- **The bold 2.0000 rows need a margin note, not a correction** (C1). §23.9.2 prints V = 2.0000 at
  p = 300 and 10,000 against Prop. 23.1's strict V > 2; measured V(300) − 2 = 1.759 × 10⁻⁶, so the
  table is right and only its presentation hides the point the table exists to make.
- **Table conventions are mixed inside 131 lines** (14m-13): 17 pipe-table lines against 14
  space-aligned, and §23.9.1's one ranked list printed as two blocks with the header repeated at
  L6395. Whether this is a chapter-wide or book-wide defect is unmeasured; R3 or the reader audit
  should count both conventions across all six volumes **at press**, not at source (G0w).
- **Chapter 23's third and last read** — MEASURED this chat by heading scan: §23.10 opens **L6434**,
  §23.15 opens L6606, Chapter 24 opens L6623. **Unread: L6434–L6622, 189 lines, fifteen headings** —
  §23.10, §23.10.1–.4, §23.11, §23.11.1–.2, §23.12, §23.13, §23.14, §23.14.1, §23.15. Re-scan them
  anyway. §23.15 is where chat 95's ν_V docket (14k-01, 14k-02) lands: read it once, then test both
  citing sites (L6270, L6923) and the Ga I attribution against it in the same read.
- **Method notes for chat 97, from this chat's eleven faults.** (1) **A verdict is re-read against
  the numbers printed immediately above it** — 14m-14 asserted the opposite of its own printed list.
  (2) **The object under test is never its own witness**: a claiming sentence and a heading were both
  counted as evidence for the claim they announce. (3) **A bound is not a measurement** — a
  self-concordance threshold was read as a channel depth. (4) `Decimal(str(Fraction))` raises
  ConversionSyntax; convert exact rationals numerator/denominator. (5) A boundary case is not a
  violation: p = 41 **is** the crossing point, and testing `p > 41` at 41 records a true sentence as
  a deviation.

## Chat 97 — deferred out of the Chapter 23 third read (main L6434–L6548)

- **A banked golden may not read a bundle** (gate fault, chat 96's r2-ch14l / r2-ch14m). Both name
  `The_Method_1_6_BUILD124_compendia_papers_audits.md` and died at chat 97's gate. Two reasons, and
  the second is the one that matters: the bundle's name carries a build number that changes every
  chat, **and the bundle comes to contain the instrument's own banked output**, so a whole-bundle
  census is self-poisoning and cannot reproduce even under a correct path. R3 and every future
  instrument read the six volume **members** by name. The two chat-96 goldens still reproduce
  byte-identically when BUILD124 is supplied, so nothing they recorded is in doubt; but they are
  un-rerunnable without a retired build, which is a reason to keep BUILD124 on Drive until R3 has
  either re-banked them against members or accepted them as historical.
- **The Register has no entry for the correction two main-volume sites cite** (14n-A3). L6455 *the
  correction is recorded at 96–98* and L6484 *withdrawn at correction 97*. Registers 96, 97, 98 are
  each the single line *SUPERSEDED (Λ₈ successor development); see register 313*, and 313 is about
  iteration in Λ₉. MEASURED across the Register: "V = 2" 0 sites, "Figure 23.3" 0 sites, "matched
  order" 0 sites. Append-only, so this is a **missing entry**, not a wrong one — the same shape as
  the §18.4.1 item, and it joins that item in the set written when the chat-67 hold lifts. R3 must
  decide whether the missing entry is authored to what §23.10.2 already says or whether the two
  citations are dropped; note the caption citation is also a Ruling 45 item (14n-A12), so the two
  repairs interact.
- **The pointer-off-by-one class now has three members in one chapter.** 14n-A1 (§23.13 cited for
  what §23.14 L6585 carries), 14n-A2 (§23.11 cited twice for what §23.15 carries in four places),
  14n-A7 (§25.5 cited for a figure at L6958, §25.4, four lines above the named section). Chat 95's
  14k-01 and chat 96's 14m-01 are the same class. R3 should sweep **every §-pointer in the six
  volumes against the claim rather than the heading**, and the sweep is cheap now that
  `enclosing` resolves a line to its section: the test is *find the claim's sites, resolve each to
  its section, compare with the section cited*. This is the single largest recurring class of the
  phase and it has never yet been swept as a class.
- **The ν_V docket, half closed** (chat 95's 14k-01). All fifteen main-volume ν_V sites are now
  resolved to their sections and are in READ-ch14n B/A2; §23.11 carries ν_V, ceiling, granularity,
  quotation, curvature and resolve zero times each. **What remains for chat 98:** read §23.15 as
  its own section, test L6270's *Al I at n = 51 and Ga I at n = 53* against §23.15's failing cells
  (chat 96 measured Al I nf as n = 48, 51, 53, 54 with no ν_V printed for Ga I anywhere), and close
  the Ga I attribution (14k-02). Note §23.11.1 L6538 **does** name Ga I — 15 members, one refusal,
  a bifurcation — so the Ga I question is not "does §23.11 mention Ga I" but "does any section give
  Ga I a ν_V".
- **The classifier's vocabulary does not survive its own first application** (14n-A8, 14n-A9). The
  §23.11 table offers five verdicts from four refusal patterns; the heading says four verdicts and
  the prose says four patterns, so the heading is the wrong one of the two. Then §23.11.1 returns
  *repeated structure*, which is none of the five and occurs once in six volumes. R3 repairs the
  heading with one word and must then decide whether Li I's six irregular refusals are the table's
  *chaotic* row or whether the table owes a sixth row — a subject-matter decision that the six
  refusals' spacing settles, not a preference.
- **The unprinted-input class reaches nine** (14n-A13). §23.10.3's displacement row reproduces
  exactly as *the distance from the value to the nearer bracket end* — 0.128732 → 0.129 and
  4.2675 × 10⁻⁶ → 4.3 × 10⁻⁶ — and the definition is nowhere printed. Unlike chat 96's §23.9.3
  member, this one reproduces once the definition is guessed, so it is the cosmetic repair of the
  two the class now contains. The census R3 owes is unchanged: every site in the six volumes that
  prints a derived figure beside its inputs.
- **Two unsourced counts in one sentence** (14n-A6, 14n-A7). L6517's *619 refusals* matches no entry
  and no sum in the table above it (19 + 101 + 145 = 265), and its *1,061 order-1 bounds* sits
  against the same table's 499 admitted at order 1. R3 cannot repair either without recomputing the
  collection at matched order; this is the first item of the phase that needs a **recomputation of
  the collection**, not a correction of a printed figure, and it should be sized before it is
  scheduled.
- **The "held" column** (14n-A5) repeats "admitted" in all three rows of L6507–L6511. Either the
  unresolved count was never computed or it was lost in production; the Prints & Proofs original
  settles which, and under the chat-95 ruling that folder is read before the question is asked.
  Chat 98 or R3 should read it there in the same call that answers anything else owed from
  Chapter 23.
- **Truncation printed as equality, third and fourth sites** (14n-A10, extending chat 96's 14l-02
  and 14l-03). L6497 prints *V = 4ν/3*, which is the asymptote of the book's own exact
  V = 4r³/(3r²−1) — 53.344447 against 53.333333 at ν = 40. The sweep chat 96 set — every display
  equation whose own table disagrees with it — should now also catch every site printing 4ν/3.
- **Method notes for chat 98, from this chat's eleven faults.** (1) **Re-read every verdict against
  the numbers the instrument printed below it**, not only above it — 14n-05 asserted a figure
  unreproducible two lines above its own reproduction. (2) **A sign convention is not a magnitude**:
  an error term carried as −0.128598 was reported as reproducing 0.129 and poisoned two ratios
  downstream. (3) **A token count cannot settle a pointer** — resolve to the section's own claim
  lines and print them. (4) `r2lib.heading_line` requires a trailing space after the number, so
  bare `### 96` Register headings return None; locate Register entries with an explicit
  `^#{1,4}\s*N\s*$` match until r2lib is lifted again. (5) A truncated print is a lost measurement:
  two citing sites cut at 150 characters hid the evidence they carried.

## Chat 98 — deferred out of the Chapter 23 fourth read (main L6549–L6622), which closes the chapter

- **A main-volume table disagrees with the data volume about the data volume's own rows** (14p-19).
  §23.15's "ν reached" column: Al I *n*f 55.0 is exact against the Spectra Compendium row; Na I *n*s
  is printed at 20.0 where its own row reaches 18.7 (20.0 is what *n*d, *n*f and *n*g reach); K I
  *n*d is printed at 45.7 where the nd row reaches 12.7 and no K I channel in the six volumes passes
  15.8. Two readings are open and only R3 can choose: either the column was built from a longer
  series than the compendium tabulates — in which case the **compendium** is short and the repair is
  there — or the figures were taken from sibling channels, in which case the repair is the table.
  **The K I case decides it**: a 45.7 cannot come from a sibling channel of a species that tops out
  at 15.8, so at least that row points outside the six volumes. R3 should resolve K I first and let
  the answer set the class. This is the first finding of the phase where the main volume and the
  Spectra Compendium contradict each other on a measured quantity, and it should be swept as a class:
  **every figure the main volume attributes to a named channel, against that channel's compendium
  row.**
- **The pointer-off-by-one class reaches five members inside Chapter 23** (14q-02, 14q-03, 14q-04,
  and chat 97's 14n-A1, 14n-A2, 14n-A7). L6501 → §23.13 for objects at §23.14 L6585; L6270 and L6923
  → §23.11 for ν_V that lives at §23.15. All three retarget within the same chapter, which is what
  makes the class cheap to sweep and expensive to leave: a reader following any of them lands on a
  section that does not carry the object. The sweep is unchanged from chat 97's statement — resolve
  every §-pointer in the six volumes **to the claim, not the heading**, using `enclosing` — and it is
  now the single largest recurring class of the phase at eight known members.
- **The Ga I attribution is closed as a finding and open as a repair** (14k-02, closed at 14q-03).
  MEASURED: no site in the six volumes gives Ga I a ν_V. §23.15 gives Al I *n*f four failing cells,
  n = 48, 51, 53, 54; L6270 names "Al I at *n* = 51 and Ga I at *n* = 53", taking 53 out of Al I's own
  list. R3 repairs L6270 against §23.15. Note the trap that nearly caught this chat: §25.5 L6976
  prints Ga I 4s²np 54 **51.7**, which reads like a ν_V until its header at L6972 is read and the
  column turns out to be ν. **Read the header, never the neighbourhood.**
- **The unprinted-input class reaches twelve, and the newest member is a convention** (14p-03b,
  14p-11, 14p-12). §23.12's Δ^(k+1)T column reproduces exactly — R/n², the volumes' own R, no quantum
  defect, on the m+1 levels nearest ν with ties broken downward — but the window is never stated, and
  the value moves across the admissible anchors by more than the rows differ from each other. That is
  a one-clause repair. The other two new members are not: the +0.86 Hill-radius slope (two sites,
  L6598 and L8633, no planetary data anywhere in the six volumes) and the Kirkwood detection floor,
  which "order 7 exactly" implies to lie in (1.709 × 10⁻⁶, 1.139 × 10⁻⁵] and which is printed nowhere.
  R3 should split the class in two when it schedules it: **conventions unstated** (cheap, local) and
  **inputs absent** (each needs data brought back into the volumes or the claim scoped).
- **A universal over 477 rows resting on three** (14q-09). "Curvature washes out before separation,
  in every channel in this work" — the Spectra Compendium tabulates 477 channel rows and a ν_V is
  printed for three. The three satisfy it. Repair: scope the sentence, or print *q* for the rest.
  Same shape as chat 97's 14n-A8/A9 vocabulary items: the sentence is true of what was measured and
  false of what it says.
- **Heading sentences that finish in the body** (14q-06). Four sites in the main volume: L4407
  (+ "routes"), L6582 (+ "one"), L6634 (+ a table header, not a sentence), L8659 (+ "disanalogy").
  R3 reads all four before repairing any, since one of them is not the same object as the others.
  A production class, not a subject-matter one — noted, not a concern, per M's standing priority.
- **Method notes for chat 99, from this chat's eleven faults.** (1) **A negative result from a sweep
  is a statement about the sweep**: a two-anchor sweep called a column unreproducible that reproduces
  under every row when all anchors are tried. Before recording "reproduces under nothing", state what
  was swept. (2) **Re-read every verdict against the numbers printed below it as well as above** —
  chat 97's note, and this chat still hit it twice (the planets, the 94). (3) **ν is not n**: 41.8 is
  the ν a series reaches, not its last principal quantum number. (4) **Read the header, never the
  neighbourhood** — a number beside a species is not that species' ν_V. (5) A single-witness census
  cannot use bare integers; test the phrase. (6) Correcting a banked golden works: delete-only call
  to remove the `.out`, then `gate.py bank` again. Exercised here for the first time.
- **What Chapter 23 leaves behind, now that it is closed.** Four reads, chats 95–98, main L6178–L6622
  (445 lines, 32 headings). The chapter contributed to the docket: the §23.8.3 affine-invariance
  *reason* item, the §25.6 pointer with no target, five pointer-off-by-one members, the missing
  Register entry for the correction §23.10.2 cites, the Ruling 45 caption at L6483, the two unsourced
  counts of L6517 needing a recomputation at matched order, four members of the unprinted-input
  class, and now the main-volume/Spectra contradiction of 14p-19. R3 should schedule the chapter as
  one unit: its items interact more with each other than with anything outside it.

## Chat 99 — deferred out of the Chapter 24 first read (main L6623–L6740, §24 through §24.7)

- **The collection's headline totals are stale, not wrong, and the sweep widens** (14r-01). Chapter 24
  prints 546 of 789 interior cells at 69.2 %, 243 failures over 62 channels, and four further counts
  at L6632 (1,442 / 1,105 / 869 / 930). **Register 673 registers 869 to 930 interior cells and
  Register 797 registers the 789**, so the chapter and the Register agree with each other. The
  Spectra Compendium now states, in its own words at spectra-member L900, **596 channel rows across
  28 elements · 2,269 interior cells**, and its bracket columns sum to **1,577 of 1,738, 161 failures
  over 98 channels, 90.7 %**. A sweep of five row-filters, sixteen ionisation-stage thresholds and
  two ℓ caps returns none of the six printed figures; the sweep is stated in full in `r2-ch14r.out`
  so the negative is a statement about a named sweep. **R3 cannot repair this with a corrected digit
  — it needs a recomputation at the current basis**, and it must decide first whether the compendium's
  **six double-tabulated channels (68 interior cells, 14r-19)** are counted in the 2,269. This is
  chat 98's 14p-19 class arriving at the collection's headline numbers; the two sweeps merge.
- **The bases must be named wherever a count is printed.** Measured: the channel table holds **596
  rows, of which 477 carry three or more levels and 119 are two-member channels**. HANDOFF-51 carried
  477 and chat 99's first reading called it stale; it is not, it names the ≥3-level subset. Four
  chats running have now mis-stated a count inside a document about not mis-stating counts (chats
  95, 96, 97 and this one). The operative rule: **a carried figure that disagrees with a fresh count
  is not wrong until the two bases are compared**, and any count entering a volume must name its
  basis.
- **The pointer-off-by-one class reaches ten** (14r-21, 14r-22, joining chat 98's five in Chapter 23
  and chat 97's three). L6686 → §24.7 for the *ab initio QED versus Ritz series* distinction, which
  §24.7 does not carry — *Ritz* has 31 main-volume sites, none in L6725–L6740. L6666 → §24.12 for a
  structural exclusion, and §24.12 carries *exclude* zero times against one site in the whole main
  volume. The sweep is unchanged: resolve every §-pointer in the six volumes **to the claim, not the
  heading**, with `enclosing`. It remains the largest recurring class of the phase.
- **The unprinted-input class reaches fourteen, and one member has no data anywhere** (14r-05,
  14r-10). §24.7 gives H I *5 cells* and a *median error of 0.006 cm⁻¹* and calls hydrogen *one row
  of the collection*; swept across all six volumes there is **no H I channel row at all** — hydrogen
  appears only as an ionisation energy in the Löwdin supply at spectra L1119, which does corroborate
  R_H = 109,678.7717. That is an *inputs absent* member alongside the Hill slope and the Kirkwood
  floor. Li II's printed s→f progression is a *conventions unstated* member: s and p match the
  triplet rows exactly and d and f match neither singlet nor triplet, so the selection rule is
  unstated. **Be II's four reproduce exactly**, which is what makes Li II's failure legible.
- **A figure that two sections of one chapter give differently** (14r-06). L6729 *H I gives 5 cells*;
  L6781 *Computed on H I … only 13 of 64 interior cells — 20 %*. The percentage is internally sound
  (13/64 = 20.3 %), so the two cell counts cannot both stand. **Chat 100's unit contains L6781** and
  should resolve it there rather than leaving it to R3 blind.
- **§24.3's monotone claim, and the two channels its evidence omits** (14r-07). L6669 states the
  defect falls monotonically with ℓ; the nine He I rows break signed monotonicity at p→d and rise in
  magnitude at four consecutive steps from ¹D onward. L6671 prints **seven means for nine channels**,
  omitting 1snd ¹D (+0.0007) and 1snh ¹H° (−0.0015) — and the omitted h is the step that exposes the
  reversal. Figure 24.1's caption at L6648 scopes the same claim correctly. **R3 should repair the
  section to the caption's scope, not the caption to the section.** Same shape as chat 98's 14q-09.
- **Vocabulary that changes meaning inside one sentence** (14r-08). L6672's *twenty members for ni
  and twenty-three for the two ns channels*: ni carries levels 20 / interior 18, ns carries levels 25
  / interior 23, so *members* is levels in the first clause and interior in the second. R3 should fix
  the word across the phase, not the figures — the compendium's columns are *levels* and *interior*
  and neither is called *members* there. Related: the table's tenth column is headed **fits** and
  holds the ionisation stage (values to 16).
- **Ruling 45 and Ruling 46 sites, now sweepable as one pass** (14r-17, 14r-18). Ruling 45: L6628 and
  L6632, both *An earlier version of this chapter read …*, joining chat 97's L6453 and the Figure
  23.3 caption at L6483. Ruling 46: **Build 9** at main L6693 and L7659, and five sites in the
  Register (L20, L31, L65, L68 and one further). Seven build references in reader-facing volumes. The
  pass is cheap and should be run as a class, not per chapter.
- **A compendium defect found from the main volume** (14r-19). Ar II tabulates L326–L328 and L331
  again at L367–L369 and L366 under a second configuration notation, and Si I tabulates L811, L812
  and L836 again at L839, L841 and L837 — same species, same normalised series, same n range, same
  levels, same limit, one copy bracket-tested and the other `untested`, two of the Si I pairs
  differing in δ in the fourth place. **68 interior cells counted twice.** R3 must fix this before it
  recomputes anything from the table.
- **Method notes for chat 100, from this chat's thirteen faults.** (1) **Compare bases before
  calling a carried figure wrong** — 596 and 477 are both right. (2) **Match a printed figure at the
  source's precision, not at yours** — a 5 × 10⁻⁸ tolerance against a two-significant-figure table
  fails every row. (3) **A convention stated in the source is not a defect** — the compendium's
  two-member rows print interior 1 where levels − 2 would give 0, and it says so. (4) **Key a
  duplicate test on the object, not on a coincidence of ranges** — species plus n range gave 120
  false positives, a normalised series gave six real ones. (5) **Read the scope before the species** —
  Ne I's *two limits* is true of the ²P° core and false of all Ne I rows, and the sentence names the
  core. (6) **Sweep before recording an absence** — the tabulated He II limit and the hydrogen row
  both needed a six-volume sweep first, and they came out opposite ways.
## Chat 100 — deferred out of the Chapter 24 second read (main L6741–L6816, §24.8 and §24.9)

- **The retired-basis class, and it is new** (14t-01). Chapter 24 **retires its own headline figures
  in print** at L6632 — *An earlier version of this chapter read "1,442 interior cells across 35
  atomic systems, the bracket holds in every one"* — and states the figure matches neither Appendix
  B's totals line (1,105) nor its table (869) nor the present tested count (930). MEASURED across
  the chapter: **1,442 appears 13 times, twelve of them in §24.8–§24.9**; *thirty-five* appears
  twice, once at L6632 and once at **L6792**; the retired no-failure claim is restated in the unit's
  own words at L6746 and L6750; and **1,105, 869 and 930 appear once each, at L6632 alone**. The
  current basis is named once; the retired basis carries the argument. **30 main-volume sites for
  1,442** overall. This subsumes chat 99's 14r-01: the class is not undetected staleness but
  staleness **retired in the same chapter and left load-bearing 109 lines later**. R3 needs a
  recomputation on a settled basis, and L6632 records that the twenty reconciling rows are owed.
  Sweep the other retired-quotation sites (L6628 is a second one in the same chapter) as a class
  before repairing any of them.
- **14r-06 is settled and should not be re-opened** (14t-B3). Register 437 carries H I at *38 %
  plain, 13 of 64 interior cells independent*, and the nd series at *six plain levels of ten and not
  one clean triple*, corroborating L6781 in full. **§24.7's *H I gives 5 cells* at L6729 stands
  alone** against both L6781 and the Register. R3 repairs L6729, not L6781. There is still no H I
  channel row anywhere in the six volumes, so neither figure can be checked against the compendium —
  say so rather than leaving it open.
- **Unretired text surviving its own correction — a class the phase has not named before** (14t-03,
  14t-04, 14t-05). Three instances inside one 65-line section. (1) L6760–L6762 withdraws the reading
  of `[ ]` as ab initio and L6767 concludes He I's 189 cells are *not independent tests*, while
  L6807–L6809 and **L6815, the section's closing paragraph**, still call them *ab initio QED
  calculations* and *genuine tests*; **Register 436 sides with L6767** and names the
  `[ ]`-as-ab-initio reading as the error. (2) L6791 says the blockquote *supersedes "an unknown
  proper subset"*; L6811 prints that phrase as the honest form twenty lines later. (3) L6801 *The
  book has never counted the three* against L6781's count and L6791's *two species are done*. The
  shape is always the same: a correction inserted mid-section, with the superseded paragraphs left
  standing beneath it. **R3 should sweep for the shape, not the wording** — a section that says
  *supersedes*, *and it does not*, or *sharper than it was written* is a section with stale text
  below it.
- **The main-volume/compendium contradiction class takes three more members** (14t-02, 14t-07,
  14t-08, widening 14p-19 and 14r-01). *None produced a failure* (L6750) against **98 failing
  channels, 161 failing cells, 1,577 of 1,738 at 90.7 %** and against the chapter's own *243
  failures across 62 channels* at L6626. *Ne I's sixteen … 131* (L6746) against Ne I 7/39 and Ne II
  37/69 — the same pair chat 99 found in §24.2, so it is a class. *The largest single block*
  (L6767) against **Si I's 290** interior cells. He I's **nine channels / 189 cells is exact** and
  is the only one of the four that reproduces.
- **A claim contradicted by both computations available** (14t-10). L6783's *the collection is worse
  than scattered*: the section's own (1−f)³ model predicts 5.49 % at H I's 38 % plain against L6781's
  measured 20.3125 % — **3.70× better**; and over all C(10,4) = 210 arrangements clean triples run
  **0 to 4**, with alternation (the scattered case, and the nd series itself) giving 0 and clustering
  giving 4. **Scattering is the worst case, so clustering is not "worse than scattered."** The claim
  can only rest on derived values co-locating with the *tested* cells, which is computed nowhere.
  R3 must decide whether to compute that or drop the sentence.
- **The pointer-off-by-one class reaches eleven** (14t-06). L6809 → *§18's exclusions*: §18
  (L4922–L5380, 459 lines) carries *exclusion* and *exclusions* zero times; a whole-volume sweep
  returns eight *exclusions* sites, none in §18; the target is **§25.2**, which the front matter at
  L62 already pairs with the decline modes. §24.11 in the same sentence resolves.
- **The unprinted-input class takes two more, both *inputs absent*** (14t-C1, 14t-C3). **No volume
  records per-level provenance** — spectra provenance-column rows 0; lines carrying both *observed*
  and *derived* are main 4, register 5, math 1, physics 1, index 0, spectra 0 — so L6753–L6754's Al I
  comparison and the three-way split of the 1,442 cannot be recomputed from the six volumes at all.
  That is precisely what **Q item P** (L10958, *one claim / retrievable / hours*) records as owed, so
  the class and the Q index agree and should be repaired together. Separately, the survival table's
  fourth row is its only tie — 0.5³ = **0.125 exactly**, printed **0.12**, which is HALF_EVEN or
  truncation and is what Python's `round()` returns — a *conventions unstated* member.
- **Ruling 45 reaches thirteen sites, and the worst is an instruction to the author** (14t-11).
  Seven in these 76 lines: L6748, L6756, L6791, L6801, L6803, L6810–L6812 and L6813. **L6812 —
  *it should be written that way wherever the figure carries weight* — is a directive to the writer
  printed in a reader-facing volume.** L6813 prints the Q index's cost grading (*obstacle
  retrievable, cost hours*) to the reader. Sweep Ruling 45 and Ruling 46 as one pass, as chat 99
  already proposed; this unit doubles the docket.
- **Method notes for chat 101, from this chat's two faults and the handoff's one.** (1) **A Register
  line number is not a Register entry number** — HANDOFF-52's *Register 1625* was Register-member
  line 1625, inside entry **437**'s body; the book's own citation at L6792 was right all along. A
  handoff naming an entry must print the entry's headline beside the number. (2) **Bound every table
  parse to its section's measured span** — an unbounded row regex silently absorbed Section V's
  capture-groups table and returned 600 rows / 2,317 cells / 32 elements against the compendium's own
  596 / 2,269 / 28. The compendium states its own totals at spectra L900; **check a parse against
  that line before trusting a single figure from it.** (3) **When a chapter quotes its own earlier
  wording, read the quotation as a retirement notice and grep the retired figures forward** — 14t-01
  was invisible until L6632 was read as data rather than as prose.
## Chat 101 — deferred out of the Chapter 24 third read (main L6817–L6883, §24.10–§24.13), which closes the chapter

- **The false-universal class, and this is its cleanest member** (14v-01). L6882 — *every sequence in
  this work was entered through its neutral or first ion. It was not convenience; it was forced* —
  is refuted by the collection's own channel table. MEASURED over all 596 rows using the `fits`
  column, which carries the ionisation stage: 28 elements, **18 enter at I, 4 at II, and six enter
  above the first ion** — Ge, O, S, Sc, Ti at III and **Fe at XV**. R3 must decide whether the claim
  is about the *sequences* §24.13 treats (in which case it needs that restriction printed) or about
  the collection (in which case it is false). The *it was forced* clause is load-bearing for the
  section's conclusion and cannot be repaired by softening alone. **Sweep the volumes for every
  *every … in this work* construction**; this is the second such universal the phase has broken
  (chat 99's monotone-fall claim over He I was the first).
- **The absent-member class — new, and sharper than *inputs absent*** (14v-02). §24.13 holds each of
  four points out of the lithium-like sequence; its Z = 4 member is C IV; the compendium carries
  **36 carbon channels — C I, C II, C III and C V — and no C IV row anywhere in six volumes.** The
  printed column 11.1 / 1.4 / 0.8 / 1.8 therefore has no basis at all. This is distinct from
  *conventions unstated* and from *inputs absent*: the input is not merely unrecorded, the species is
  missing from a collection that carries its neighbours on both sides. R3 should sweep for **every
  sequence the main volume treats as complete against the compendium's stage list for that element**;
  C IV is unlikely to be the only gap, and the gap is invisible from the main volume.
- **The sodium-like column reproduces in shape and in no digit** (14v-03). Exact three-point solves
  on the compendium's ns rows give 24.6 / 2.6 / 1.4 / 2.6 % against printed 23.4 / 2.4 / 1.3 / 2.5 %;
  J-resolved rows give 19.5 / 2.0 / 1.1 / 2.1; the np series 34.7 / 3.5 / 1.8 / 3.5; *Z* as nuclear
  charge 2.5 / 0.9 / 0.9 / 2.7. **Every printed value sits below the ns measurement by 0.1 to 1.2
  points** — a systematic offset, not scatter, consistent with per-level δ rather than the channel
  means the compendium prints. R3 must name the δ basis and the fit's residual convention before
  recomputing; do not adjust a digit. Pair this with the survival table's 0.125-printed-0.12
  (chat 100) as *conventions unstated*.
- **A table column with no base in the data** (14v-04). §24.11's bare `cells` column reproduces as
  bracket-*tested* cells for Ne II 0, Ar II 10, Cu II 0 and P II 1, and under **no base** for Si I 4
  (33 rows, 290 interior, 105 tested), Bi II 0 (16 interior, 10 tested, 4 passed) and Bi III 0
  (11 interior, 9 tested, 9 passed). R3 labels the column and recomputes it. Note the reader-facing
  consequence: **Si I is the collection's largest block at 290 interior cells and appears in the
  decline table at 4**, eleven lines from §24.9's *largest single block*.
- **A claim whose second half is outside its own witness's computation** (14v-05). L6842 predicts the
  outcome *for every open-d and open-f sequence … which the census of §24.12 confirms independently*.
  MEASURED with emphasis stripped: **open-f has exactly one site in six volumes — the claim itself**;
  the census's five excluded are all 3d; *lanthanide* has zero main-volume sites; and the census
  totals 27 + 12 + 5 = **44 sequences** with its range stated nowhere. The census confirms the open-d
  half and cannot reach the other. R3 either extends the census and prints its range, or drops the
  open-f clause. **The census's range being unstated is itself a defect** — a reader cannot tell what
  44 sequences covers.
- **The main-volume/compendium contradiction class takes a provenance member** (14v-06). L6818 holds
  Al I and Al II *from two independent sources — the NIST compilations and the ASD*; the compendium's
  **B.1 Sources (spectra L975–L986)** draws Al I and Al II from **Kaufman & Martin 1991, JPCRD 20,
  775** alone, and its NIST ASD row names neither. The ASD value the cross-check turns on (47379.7)
  has one site in six volumes and no provenance row. This is the same hole as chat 100's 14t-C1 seen
  from the other side: **B.1 exists and is per-species, but nothing records a species held from two
  sources**, so no cross-check in the book can be verified. Repair B.1's shape and Q item P together.
- **§24.13's end rule overstates against its own table** (14v-07). L6877 *at an end — δ not
  determined* and L6879 *the ends always must* against the table's own upper end at **1.8 % and
  2.5 %**, 6.2× and 9.4× better than the neutral end and within a factor two of the interior band.
  The section's prose is right where it is specific (L6869, and the L6855 caption: *extrapolation to
  the neutral does not*); the summary row and the blockquote generalise from one end to both. R3
  repairs L6877 and L6879, not L6869. **Related to the retired-basis shape but not the same**: here
  the correct statement and the overstatement sit side by side from the start, neither superseding
  the other.
- **A rule whose own quantity admits its worked example** (14v-08). §24.12 defines D as the J-level
  count of the (N−1)-electron ground configuration and excludes on D ≥ 19; §24.11 offers Cu II as the
  rule's first instance. Cu II is Ni-like, but L6837 prints its channel as **3d⁹5s**, and D(3d⁹) = 2
  by the same enumeration — the rule's admission threshold. D = 19 arises for Ni-like only at the
  neutral member, whose core is 3d⁷. **D is member-dependent along a sequence and §24.12 does not say
  which member it is computed on.** The five sequences do reproduce 19–37 on ionic 3d³…3d⁷ cores, so
  the arithmetic is sound and only the anchor is missing. R3 states the anchor; until it does, the
  census's own worked example falls on the wrong side of its threshold.
- **Method notes for chat 102, from this chat's six faults.** (1) **A fixed enumeration of a domain
  is a fault waiting for the datum that exceeds it** — a six-entry Roman map died on `IX`, and the
  collection carries a stage **XV**, which was the finding. (2) **Match by term before taking a ratio
  between two-electron species**: averaging He I's ¹S with its ³S moved the printed 0.53 to 0.59 and
  would have recorded a verified span as a deviation. (3) **A count sweep on numerals must be
  digit-bounded** — raw substring counting returned 14 chapter sites for *1,442* against chat 100's
  13, and chat 100 was right. (4) **Strip markdown emphasis before any word-bounded token test**;
  `open-*f*` is invisible to `has_token`. (5) A handoff naming N sites for a token must name **the
  form each site carries**: *thirty-five* appears once (L6792), not twice — L6632 carries **35**.

## Chat 102 — deferred out of the Chapter 25 first read (main L6884–L6990, §25 through §25.5)

- **The Register rules against the volume's own body text** (14x-02). **Register 1751, Ruling 21**
  (dated 2026-08-24) rules the Figure 25.1 caption to read *each of the 1,061 cells that yield a
  perturbation bound*, records that the superseded caption said *each of 1,105 verified cells*, that
  1,105 is Appendix B's totals line, and that *the plot, §25.5 and seven other places count 1,061
  perturbation bounds*. §25.5's body then says the opposite twice: L6970 *Every verified cell yields a
  bound. Of the 1,442…* and L6986 *1,442 cells, each yielding an upper bound*. MEASURED: 1,061 at
  seven main sites (L60, L6517, L6683, L6958, L9354, L10266, L10277) and one register site; the
  difference is **381 cells**. R3 repairs L6970 and L6986, **not the caption**. **New shape: a ruled
  correction applied to a caption and not to the prose it captions.** R3 should sweep every Register
  ruling that names a caption or a figure and check the surrounding text moved with it.
- **A quantity that does not follow from the inputs printed beside it, in a section whose own table
  does** (14x-03). L6936 prints Hg II's half-spacing as **24,634 cm⁻¹** *computed from 2Z²R/ν³ at the
  measured ν = 5.3*. MEASURED at *Z* = 2, R = 109,737.31568: **5,896.8**. The figure needs ν = 3.291
  at *Z* = 2 or *Z* = 4.088 at ν = 5.3. The same section's ν_fail table (L6940–L6945) reproduces
  **8 of 8 exactly** from that formula and constant, so neither is in doubt. The dependent clause
  moves: *displaced by a tenth* is 0.122 against the printed figure but **0.509 and 0.339** against
  the measured one. **L6947's conclusion survives** — ν = 5.3 is below the table's own ν_fail of 6.6.
  R3 recomputes the figure and the *tenth*; it does not touch L6947.
- **A factor of two unreconciled across three consecutive lines** (14x-04). L6932 gives the failure
  condition as |ΔT| > 2*Z*²*R*/ν³; L6934 says reordering needs a shift exceeding **half** the local
  spacing; L6936 calls 2*Z*²*R*/ν³ itself *the half-spacing*. 2*Z*²*R*/ν³ is the derivative of
  *Z*²*R*/ν², the **full** spacing. Either the condition carries an uncorrected factor of two or the
  label does. **This is load-bearing beyond §25**: the same condition is inverted into the 1,061
  bounds at L9354 and defended at L10266, so R3 must settle it before any bound is restated.
- **The absent-member class takes a member with a measurement attached** (14x-05). §25.2's exclusion
  (i) is worked on **Sr I** 5s²¹S₀ → 5s*n*p ¹P₁ and prints *coverage across the node: 79%* and *100%
  on 11 cells*. MEASURED: **no Sr row at any ionisation stage anywhere in six volumes** — Sr I has 2
  main sites, 6 register, 1 math, 0 spectra — and the channel table parses to 596 / 28 / 2,269,
  agreeing with its own L900. Coverage requires bracketed cells; none exist. **No k/n with n < 40
  gives 79.0 %** (nearest 11/14, 15/19, 19/24, 23/29). Sharper than C IV (14v-02), where the
  neighbours were present. R3 must either seat Sr I's channels in the compendium or drop the
  percentages; the factor-of-60 collapse at n = 6 is likewise unwitnessed.
- **An exclusion whose base cannot be formed from the collection** (14x-06). L6903–L6905 gives Ca II
  *n*d 2 of 7 steps, Ba II *n*d 2 of 6, Ba II *n*p 3 of 6, and *coverage over the 17 interior cells is
  58.8 %*. A fine-structure splitting needs **both J components** at each n; MEASURED, the table
  carries **one J component only** for each named channel (Ca II *n*d J=3/2 L525, Ba II *n*d J=3/2
  L402, Ba II *n*p J=1/2 L405) and **no partner row exists**. Separately the printed steps
  7 + 6 + 6 = 19 imply 22 members and **16** interior cells, not 17. The three percentages do share
  one base exactly (58.8 = 10/17, 41.2 = 7/17, 35.3 = 6/17), so the 17 is internally consistent and
  externally unsourced. Unprinted-input class with an off-by-one above it.
- **Two more failed pointers, both in one sentence** (14x-07). L6922–L6923 sends *r < 5* to §25.6 and
  *ν > ν_V* to §23.11. MEASURED on the **raw** line: `r < 5` has one site in the whole main volume,
  **L6922 itself**; `ν_V` has 15 main sites and **none in §23.11** (L6519–L6549) — its definition is
  L580–L582 and its working cluster L6585–L6621. The pointer-off-by-one class (docket 9) is now
  **thirteen members**. Note the method point: the target test must run on the raw line.
- **An attribution missing where the name is already taken** (14x-08). L6896's *Cooper-type node* is
  unattributed; MEASURED, `Cooper` has 4 sites in six volumes and the other three are the
  Mathematical Compendium's **Cooper 1989, k-consistency, Artif. Intell. 41** (math L252, L254,
  L3517). A reader following the only Cooper in the bibliography lands on a constraint-satisfaction
  paper. R-ATTR requires the attribution and the collision requires disambiguation. **R3 should sweep
  every physics eponym in the volumes against the bibliography for the same collision.**
- **Two compendium data defects, both found from the main volume** (14x-09, 14x-10). (a) Spectra
  **L562** prints Ga I 4s²*n*p ²P° high as `n 41–5` — the upper endpoint below the lower, the only
  malformed *n* range in 596 rows; 15 levels and ν 38.8–52.7 fix it as **41–55**. (b) A whole-table
  sweep on identical (species, series label) returns **9 duplicated keys, 18 rows**: Ba III *n*d J=2
  (L417/L419), **Ca II *n*s J=1/2 (L524/L530)**, and seven Si I channels (L811/L839, L812/L841,
  L832/L834, L833/L835, L836/L837, L838/L842, L840/L843). **In every pair one copy is bracket-tested
  and the other untested** — 14r-19's exact shape, which recorded six channels and 68 interior cells
  for Ar II and Si I. This sweep keys on the identical label and cannot see Ar II's second-notation
  copies: **the two sweeps are complementary and both must run before any recount.** Ba III and Ca II
  are new to the class.
- **Method notes for chat 103, from this chat's seven faults.** (1) **Emphasis-stripping destroys the
  underscore**, so `ν_V` is invisible to a stripped test — run symbol tests on the **raw** line, and
  assume this fault hides every subscripted symbol in the volumes. (2) **Case matters**: a
  case-sensitive search for *four* missed §24.11's own heading word *Four* and would have recorded
  the front matter's L62 as unsupported. (3) **Match a printed figure at the source's precision** —
  test the band the printed ν's own decimal allows, and compare **at that precision**, because a
  boundary case is not a violation; this rule alone saved Al I and Ga I from being recorded as
  deviations. (4) **Identify the base before comparing**: a fine-structure splitting is not a channel
  row, and the first version of the test compared 17 against 29 before the question was asked
  correctly. (5) **Grep the Register before recording a figure as unreproducible** — Register 1751
  turned a suspected caption defect into the witness against the body text.

## Chat 103 — deferred out of the Chapter 25 second read (main L6991–L7116, §25.6–§25.6.6), which closes the chapter

- **The Register rules against a whole section, not a caption** (14z-01). Register **801** —
  *BUT THERE ARE TWO BRACKETS IN THE BOOK, AND ONLY ONE OF THEM IS A DEDUCTION* — quotes §25.6.1's
  own sentence and rules that §22.1's bracket is the deduction and §25.6.1's is not, closing *the
  book calls the bracket "a deduction, not a prediction" — true of the first, false of the second.*
  Register **802** measures the premise: across 209 channels δ is monotone in 147, **91 fall and 56
  rise**; where δ's range exceeds 0.1 it is 32 falling to 4 rising, **16 of those 52 are not monotone
  at all**, and below a range of 0.01 the split is chance. Register **803** states the trade-off in
  general. §25.6's body has not moved: the heading L6991, the *structural fact* at L7005, the
  *deductive bracket* at L7018, and L7042 and L7055. **R3 must settle what §25.6 may call its result
  before any of the section's prose is touched**, and the decision reaches §22.1, §23.10.1 and
  Figure 25.2's caption. Same class as 14x-02, one section wide instead of one caption.
- **A bracket that inherits the estimate its own section forbids** (14z-02). L7050's 7s bracket
  [784,128, 785,209]: solving the lower edge at n = 7 gives **δ = 0.967887**, the *estimated*
  δ(6s) = 0.967891. L7057 states *a bracket that inherits an estimate is not a bracket*. From the last
  measured defect δ(5s) the edge would be **783,646**. R3 restates the edge or withdraws the
  distinction.
- **A false universal and its dependent clause, both broken** (14z-03, 14z-04). L7075: *Every verified
  cell in this book lies at Z_eff between 1 and 3* and *Z_eff = 6 — double the highest charge state
  tested*. MEASURED on bracket-tested rows only: **60 rows, 172 bracketed cells above stage 3**, in
  B IV, Be IV, O IV, P IV, S IV, Si IV, B V, C V, S V, S VI, Ti XI, Fe XV, Fe XVI; **highest stage
  tabulated and tested = 16**. Docket 19.
- **Three failed pointers, with their real targets located** (14z-05, 14z-06, 14z-07). L7097 → §24.2
  for *3.5% / 17% / tight end*: §24.2 carries none; **3.5% lives at §22.2.3 (L6096–L6098), whose own
  text names §25.6 and Sc VI**, and *tight end* at §22.2.2 L6075. **17% has four main sites and the
  other three are all "17% of 264 inputs"** — a different quantity, so the clause is unsupported in
  six volumes. L7069 → §24.2 for Rule 4a: Rule 4a's four sites are L6049, L6110, L7068, L7485, none in
  Chapter 24. L7115 → §24.6 for *the deductive bracket*: §24.6 is **The isoelectronic pairs** and the
  sentence's "it" is the isoelectronic route, so the pointer names the thing it says the bracket does
  not depend on; candidates are §23.10.1 L6438, §22.2.5 L6114 and §25.6.1–§25.6.2. **The
  pointer-off-by-one class now has sixteen members. R3's sweep must carry a claim-locator: a token
  test on the target says only that the pointer failed, not where the claim went.**
- **14m-01 closed as a finding, not repairable by redirection** (14z-08). §23.6 **L6319** sends *the
  field abandoned the variable* to §25.6. The unit, read in full: *abandon\**, *variable*,
  *literature*, *field*, *neglect\**, *disuse*, *no longer*, *out of use*, *dropped*, *unfashionab\**
  all **0×**. *abandon\** has three main sites in total (L1479, L3435, L6319). R3 authors the
  explanation or drops the clause; the clause is load-bearing for the novelty claim beside it.
- **14x-07's live half closed** (14z-09). L6922's *r < 5* → §25.6, tested on raw lines as `r < 5`,
  `5:1`, *ratio*, *separat\**, *threshold*, *too close* and *r* with any relation: **0× in every
  form**. The unit's three *five* sites are species counts. `r < 5` has one main site, L6922 itself.
- **A section that contradicts its own heading on the word the heading rules** (14z-10). *predict\**
  10 sites, *deduct\** 6 sites in 126 lines; L6992 *which makes it a prediction* against L6991 and
  L7040; L7093, L7087 and L7111 all call it a prediction. Repair with 14z-01, not separately.
- **A second route whose base is a different term** (14z-11). Target L7045 is **³S°₁**; L7099's route
  needs the **(⁴S°)4s ⁵S°₂** level of the lower members, and L7093 calls it *the same prediction*.
  Separately **the unit never states which series δ(4s) = 1.0057 and δ(5s) = 0.9812 belong to** — six
  sites, none naming a term. The 14x-06 shape: unprinted input with a base mismatch above it.
- **An ordinal against the section's own list** (14z-12). L7097 prints six sequence members and
  prices the extension as *a fifth member*; Sc VI is the sixth. Electron counts all correct at 16.
- **The absent-member class takes an entire sequence** (14z-13). Sc VI: **30 main sites, 0 in all five
  other volumes**; Sc appears in the channel table only as **Sc III, 11 rows**; and **none of S I,
  Cl II, Ar III, K IV, Ca V has any row**. L7099's *both tabulated for all five* and L7106's *five
  other species* rest on species the collection does not carry. Widens 14x-05 (Sr I) and 14v-02 (C IV):
  docket 20 now covers a whole isoelectronic sequence.
- **Ruling 45 class, three new members in 126 lines** (14z-14). **L6999** *That is stated here so a
  referee does not have to ask*; **L6993–L6994** *the book states it as a bracket … because Rule 3
  requires that and an earlier version violated it*; **L7040** *calling it one was a category error
  against the book's own law*. The class stands at eighteen.
- **Unprinted inputs, four** (14z-15). L7105's **± 1,594** and L7106's **± 2,169** match nothing
  within 13 out of **84 bases swept** (four slopes 2RZ²/ν³ at n = 4…7 × nine defect spreads, plus every
  bracket half-width); the limit **892,700 ± 400** has one main site, L6914, and none in the Register;
  *thirty-five other species* against **70 species, 61 bracket-tested** — though the same sentence is
  quoted inside Register 801, so it is internally sourced and externally unmeasured; and the series
  term of the two defects. Docket 10.
- **A single cause offered for a two-cause effect** (14z-16). L7051's *tighter than 6s because the
  spacing has fallen as ν⁻³*: the slope ratio is **1.729**, the δ-range ratio **1.438**, product
  **2.487** against the observed **2.486**. The stated cause carries 1.73 of 2.49.
- **Method notes for chat 104, from this chat's four faults.** (1) **Identify the population before
  comparing** — *verified*, *tested* and *interior* are three different bases (596 rows / 2,269
  interior / 1,577 bracketed) and the first version of the computable batch used the wrong one.
  (2) **Print a window around the match, not the head of the line** — these volumes carry lines past
  200 characters and two clauses under test were invisible in the first output. (3) **Filter compound
  numerals** — *thirty-five* returned 20 main sites, fifteen of them *one thousand six hundred and
  thirty-five*. (4) **Sweep both numeral forms** in the Register. (5) **A token test that fails names
  no target** — add a claim-locator to every pointer test. (6) **Grep before recording a single
  witness**: δ(4s), δ(5s) and δ̄ all recur at L6114, which would have made three single-witness entries
  wrong.
## Chat 104 — deferred out of the Chapter 26 read (main L7117–L7202, *Collective sections*), which closes the chapter

- **A spliced sentence, its source located, and the class bounded to one site** (15b-01, 15b-02).
  L7156 prints *measuring C₆ to 1% fixes ν to about 0.0the searched bound of §29.8 — from 1/p_eff
  at n =*. The string *the searched bound of §29.8* is a verbatim cell of §29.8's own claims table
  at main **L8089**. **Prints & Proofs carries the identical line at P7082** (md5
  `49900cf41f818ab789bb90fc596ac977`), so this is an **authoring defect, not production loss**.
  The lost figure is recoverable and not in doubt: 1/p_eff(100) = 0.087416, so the sentence read
  **about 0.09 %**. R3 restores the figure **and** cuts the spliced cell — both halves, or the
  sentence still does not parse. **The class has exactly one member**: sweeping six volumes for
  the shape with paths, URLs and filenames excluded gives main 1 (L7156), reg 4 (all URLs or
  archive names), mc/pc/ioi/sc 0. Do not open a sweep that is already closed.
- **The Aitken table uses a Rydberg constant the book does not use** (15b-03). Under the window
  (n−1, n, n+1) — the only one of four that reproduces anything — the Aitken column is **4/4 exact
  at R = 109737.30** and **3/4 at the book's R = 109737.31568**, where T(10) prints 1097.3730
  against 1097.3732 under both HALF_EVEN and HALF_UP. The T column agrees: at 109737.30 all four
  rows reproduce, T(20) requiring HALF_UP. R3 recomputes the table at the book's constant or
  states the one it used. **The window itself must be stated too** — (n, n+1, n+2) reproduces 0/4.
- **A truncation inside a rounded table** (15b-04). T(20)/3 = 91.44775 → **91.4478** under either
  convention; the table prints **91.4477**. One row, one place. Docket 12.
- **σ₁ = 9.49 × 10¹ is unreproducible over 120 bases and single-witness** (15b-05). Five exponent
  sets × six ν grids × two centrings × two log bases; nearest 91.59, span 11.98–505.1. Inverted,
  the fifteen exponents would need ‖p‖ = 17.40 on ν = 1..40 or 33.64 on ν = 10..49, against 35.21
  for p = 1..15. **Neither the fifteen quantities nor the forty ν values is printed** — the table
  names eight observables. `9.49` has one site in six volumes. Dockets 10 and 17.
- **σ₂ = 1.8 × 10⁻¹⁴ constrains nothing, and the volume already says so** (15b-06). Row-centring
  log q = p log ν + const leaves p ⊗ v exactly, so rank 1 and a double-precision σ₂ follow for
  **any** inputs; measured true-SVD σ₂ ran 9.17 × 10⁻¹⁵ to 1.31 × 10⁻¹³ across the same 120 bases.
  **Main L297 calls the result *a tautology once §26.1's* rule is granted**, while §26.2 presents
  it as a measurement and mc **L2078** repeats σ₂ as a compendium finding. **Same shape as 14z-01:
  R3 must settle what §26.2 may claim before touching its prose, and mc L2078 moves with it.**
- **Two pointer failures, both with located targets** (15b-07, 15b-08). L7185's *exactly λ² of
  §23.11* → §23.11 is *The refusal pattern carries four verdicts, not one* with **zero λ, zero
  2/3, zero Newton**; λ² = (2/3)T lives at **§23.8.1 L6345** and **App D.4.1 L10368**. And
  mc **L1932**'s *Proved — M §24.6* → §24.6 is *The isoelectronic pairs* with **Aitken 0, limit 0,
  bias 0**, while §26.6 carries Aitken 7, limit 4, bias 2. **Docket 9 now stands at eighteen**,
  and §24.6 has now absorbed two pointers meant elsewhere — chat 103's 14z-07 was the first.
  R3 should test §24.6 as a magnet for mis-aimed pointers, not just as a target.
- **The chapter's only empirical test is priced on an absent species** (15b-09). §26.5 tests
  Singer's Rb ns–ns parameterisation; **Rb has zero rows in the Spectra Compendium** and the token
  appears 0 times in sc, mc, pc and ioi. Docket 20, after Sr, C IV and the sulphur-like sequence.
- **"Bracket 66 of 66" has no population of 66, and the only 66-population in the book is
  withdrawn** (15b-10). §26.5 states nine points twice; C(9,2) = 36, 9 × 9 = 81. The phrase
  *66 of 66* occurs at reg L4617, mc L3370, pc L591 and pc L653 — all the **triplet-above-singlet
  pair** count, and pc L653 records it *Withdrawn at register 1168*. R3 states §26.5's population
  or drops the clause.
- **The cost law is never stated** (15b-11). *cost law* / *cost-law* has two sites in six volumes,
  L7170 and L10278, neither defining it. Fitted as A·nᵖ to Singer's own C₆ over nine points: p
  free gives median 4.415 % / max 9.017 % at exponent 11.9934; p fixed at 11 gives 23.702 % /
  98.589 %. **Neither reproduces the printed 1.05 % / 1.83 %**, both of which are single-witness.
- **Ruling 45's nineteenth member** (15b-12): L7201, *A domain restriction found by testing, and
  stated rather than discovered by a reader.* L7189–L7190 is adjacent and recorded as an
  incidental, not a member.
- **Closed as negatives, with their witnesses, so R3 does not re-derive them:** docket 19 gains no
  member (all three universals are about the algebra, not the collection); 14q-06 stays at three;
  Ruling 46 is clean in the chapter; Singer and Aitken are both fully attributed in the
  bibliography (main L11589, main L11634); and **Figure 19.1 is a live, different figure** at main
  L5414/L5416, so the renumbering to 26.1 left no stale citation.


## Chat 105 — deferred out of the Chapter 27 first read (main L7203–L7331, §27.1–§27.5.1)

1. **The duplicated-section class opens (15d-01).** §9.2 L1961–L1990 and §27.5.1 L7299–L7330 are
   one passage in two chapters with two Register entries (438 and 446). R3 must decide which site
   holds it, merge the detail unique to each, and reconcile the two entries with a **new** entry
   citing both. **Sweep owed:** every other passage in the six volumes that appears twice — the
   test that found this one is a normalised phrase match on the display sentence and the table
   rows, not a line-identity check (only 2 of 24 lines are byte-identical because the two copies
   are wrapped differently). Adjacent and distinct from the spliced-text class (15b-01/02), which
   was one member long.
2. **A section cited as having proved what it asserts (15d-05).** L7301 and **Register 446's own
   headline** both credit §27.2 with a proof; §27.2 is a formula, a table and a bold assertion, and
   the word *prove* does not occur in its span. R3 sweeps every *proves / proved / it was shown*
   in the six volumes against the cited span, and pairs this with docket 23 — the Register and the
   prose must move together.
3. **The unstated-denominator class (15d-03).** 11.3 % and 0.3 % reproduce only against n(n−1)
   while the text says *pairs*. R3 sweeps every percentage-of-pairs figure in the six volumes for
   its denominator and prints the convention once. **Composition's 24.7 % is NOT RECONSTRUCTED** —
   R3 must first locate the composition relation §12.11.0 defines (mc L1284 describes it with a
   direction, source signature (n, ℓ, k, 2S) against target (e, f, g, 2S′)) and re-measure before
   any verdict. Do not carry my 3.03 % forward as a finding.
4. **Four of five tables in Chapter 27 are space-aligned plain text (15d-04)**, and §27.1's is
   shattered mid-word. Identical in Prints & Proofs, so it is an authoring/production defect of the
   source. R3 rebuilds §27.1, §27.2, §27.4 and §27.5.1 as markdown tables; §27.3 is already one.
   **Sweep owed:** every space-aligned table in the six volumes, and every table whose column text
   breaks mid-word — the §27.1 signature is `orde`/`r`, `geo`/`metr`/`y`, `calcu`/`lus`.
5. **§27.2's log column, L7236 (15d-02)** — 0.337 printed where ln(126/90) = 0.336 under both
   rounding conventions and no base gives 0.337. One row of five; the other four are exact. Repair
   with the truncation class (docket 12).
6. **Ruling 45's twentieth and twenty-first members: L7244 and L7312.** L7244 discloses the
   authoring order (*The name was chosen before the quantity was analysed*); L7312 remarks on the
   book's own citation practice (*Three sections computing one shape, none citing the other two*).
   L7312 also **states the duplication of item 1 in the volume's own voice** — repair the two
   together, because removing the remark without merging the sections leaves the defect unsaid.
7. **The unprinted-input class gains two (docket 10):** §27.3's *subnet with a hole* prints neither
   |ℛ(X)| nor |X|; inversion gives |ℛ(X)| ∈ {255, 256} and the bits/cell column rounds alike at
   247 and 248, so neither is fixed by the section.
8. **Incoming-pointer imbalance (incidental 4).** §27.1, §27.3, §27.5, §27.5.1 and §27.6 have zero
   incoming §-pointers from any of the six volumes; §27.2 has four and §27.4 two. R4 should measure
   this across every chapter — a section nothing points at is where a duplicate survives.
9. **§27.6 is unread** — main L7332–L7363, 32 lines, and it carries census row **1155** (L7359,
   C9-OVERGENERALISATION-WORD, token *never*, in *The three languages were never in competition*).
   The next section read closes Chapter 27 and disposes of that row.
## Chat 106 — deferred out of the unit main L7332–L7457 (§27.6 closing Chapter 27; PART VI; §28–§28.5)

1. **The per-cell σ coverage has two printed values (15f-01).** §22.2.1 L6063 gives 69.6 %, §28.4
   L7442 gives 68.1 % and calls it *the expected figure*; the expected figure is 68.2689 %, which
   quantizes to 68.3 under both conventions. R3 settles which coverage was measured, repairs the
   other site, and drops or corrects the word *expected*. **Sweep owed:** every ±1σ coverage figure
   in the six volumes, and every place a figure is called *expected* — the expected value of a
   stated distribution is computable and must be checked as such.
2. **The Register's own size is printed three ways in one chapter (15f-02).** L7367/L7373 print
   1,635 (a heading count), L7658 prints 1,631, and the entries number **1,660** — 1,628 bare
   headings plus seven grouped headings carrying 32 numbers. R3 must decide what the book counts —
   headings or entries — state the convention once, and drive every site to it. **This interacts
   with the kinds table and the extent sites**, which are recomputed after any Register addition.
   Grouped headings are also a Register *form* question the R4 audit should record.
3. **Chapter 28's head sentence undercounts its own chapter (15f-03).** *Twenty-six … listed at
   §28.7–28.7.2* is exact for the three sections it names, but §28.7.3/28.7.4/28.7.6/28.7.7 list
   75 + 40 + 2 + 119 more, for 262. Repair with docket 21 (a summary that does not match the prose
   below it) and with item 2 — both are the chapter describing its own size.
4. **Ruling 46 is measurably wider than the docket carried (15f-04).** MEASURED 17 main-volume
   sites: L994 (*zeno.py*, *.zeno/*), L1401 (*audits.py*), L4151, L6693, **L7373 (*at this build
   (2026-08-29)*)**, **L7374 (*generated by `register_gen.py`*)**, L7658, L7659 (*since Build 9*)
   and nine further. Docket 6 should be re-scoped to this measurement before R3 sweeps it, and run
   with docket 5 (Ruling 45) in one pass.
5. **§28.10 is printed inside Chapter 29 (15f-05)** — heading at L8222, between §29.11.2 (L8179)
   and §29.12 (L8238). R3 moves it to the end of Chapter 28 or renumbers it, and re-checks the
   contents list, the Index of Indices and every pointer that assumes source order. **Sweep owed:**
   run the heading-order test over every chapter of the six volumes; this is the first
   out-of-order section the review has measured.
6. **"Exactly one infinity in the whole construction" is false as stated (15f-06).** Two structural
   counter-witnesses: the c → ∞ twin index Λ_cinf (pc L225/L231/L603, mc L3214, ioi L1933, main
   L9772/L9866) and **L = −∞ at the node floor** (main L9668/L9787, pc L741, sc L227), which is a
   second boundary convention of exactly the kind the sentence says is unique. Repair L7338–40
   **and Register 447**, which carries the same claim. False-universal class, docket 19.
7. **§6.1 does not state `max ∅ = −∞` (15f-07).** The convention lives at mc L326; §6.1 (L1532–93)
   defines φ̂ without it. Both main L7340 and Register 447's headline cite §6.1. R3 either states
   the convention in §6.1 or re-points both sites at the Mathematical Compendium — and the Register
   entry is corrected by a **new** entry citing 447, never edited. Docket 9 and docket 23 together.
8. **Two formatting classes (15f-08, 15f-09).** A mid-sentence paragraph break at L7405–07, and
   **30** main-volume sections whose body opens in lower case directly under the heading (L7367 is
   Chapter 28's). Both are sweepable in one pass with docket 28's table work.
9. **§27.6's "Every number in §27.2 was computed elsewhere in this book" is false by exactly one
   witness** — 0.337 (15d-02), which reproduces under no base and no rounding convention. Repairing
   15d-02 repairs the universal; if 0.337 cannot be recovered, the universal must be qualified.
10. **Single-witness additions:** *2,163* (L7429) and *473 million* (L7338) each have one site in
    six volumes. Docket 17.
## Chat 107 — deferred out of the unit main L7458–L7558 (§28.6, §28.7, §28.7.1, §28.7.2)

1. **An orphan item numbered 59 sits under §28.7.2's heading (15g-01).** L7533's *59. The cheapest
   undetectable forgery in Λ is 60 cells, not one.* duplicates §28.7.1's item 59 at L7517 and is
   not one of the twelve the heading counts (63–74, which are exact). MEASURED in Prints & Proofs
   at P7457, under `### 28.7.2 From more from the structural and audit work` — the count word was a
   placeholder in the original input and was filled in later without seeing the block above it.
   R3 renumbers the orphan or moves it to §16.3, which it cites. **Sweep owed: every §28.7.x
   heading numeral against its own body, and every placeholder heading in the six volumes that has
   since been filled in — PP is the witness for which counts post-date the input.**
2. **Item 74 is truncated mid-sentence, in the original input too (15g-02).** L7556–57 ends
   *median 340 induced cells, minimum* and the chapter moves to §28.7.3. PP P7480–81 is identical.
   Authoring gap, not production loss. The lost figure is the minimum of a distribution whose
   median is printed, so R3 recomputes rather than transcribes. **Sweep owed: every numbered item
   in the six volumes whose final line lacks terminal punctuation — chapter 28 has three (L7487,
   L7496, L7556), and only the third loses content.**
3. **§28.6's distribution table sums to 20 against no stated population (15g-03).** Rows 4, 3, 2,
   3, 4, ~3, 0, 1. The chapter's own candidates are 19 printed pre-closure items, 26 post-closure
   items, and *the first forty-eight*. R3 states which population the table sorts and drives the
   rows to it. Docket 10, and 15f-02's *unit of a count unstated* sub-class. **The `~3` is the
   review's first approximate entry inside a count table** — an approximation in a distribution is
   its own repair question.
4. **The numbering has no printed antecedent (15g-04).** *The first forty-eight* (L7482–83,
   wrapped) has no items 1–48 anywhere: chapter 28 prints no numeral below 49 and the Register,
   Mathematical Compendium, Index of Indices and Spectra Compendium carry none. R3 either prints
   the antecedent list, renumbers 49–164 from one, or drops the ordinal framing. **Interacts with
   the Register's own size (15f-02) — both are the work counting itself in a unit it never
   states.**
5. **Four failed pointers, all with targets located (15g-05 to 15g-08).** §32.5 for falsification
   conditions, which live at §32.6 — **and L7896 (§29.2) repeats the same failed pointer**; §32.1
   for *the dominant pattern*, which is §28.1's heading three pages up; §32.3 for *four clauses*,
   which §32.3 no longer has (it states thirty checkable and *there is no fourth*); §16.3 for
   *five recorded failures*, where §16.3 records one worked case — **asserted twice, at L7535–36
   and at L4645 (§16.7.4)**. Dockets 9, 15 and 23 together; §29.2's table row and §16.7.4 are the
   two places a repair of the prose alone would miss.
6. **Two closing notes count corrections of corrections without witnesses (15g-09).** L7502 and
   L7527 each say *two*; the only explicit numeral cross-reference among items 49–74 is 66 → 65,
   in a section claiming nothing of the sort, and item 54 corrects item 53 by wording only. R3
   either names the members or drops the count. Docket 21 at paragraph scale. **Sweep owed: every
   *N of these M* sentence in the six volumes against the items it counts.**
7. **A second duplicate item numeral, outside this unit.** Item 118 appears at L7604 inside the
   range *112–118* and again at L7608 as its own item, both in §28.7.3. Recorded so the §28.7.3
   read treats it as known; R3 repairs it with 15g-01 in one numbering pass.
8. **Three more Ruling 45 candidates (docket 5).** The heading tags *— retained in the compendium*
   at L7481, L7506 and L7531, joining L7426; the volume carries seven (also L7559, L7644, L7774).
   Adjacent: L7478's *originally written as no available mechanism* and L7677's *in the
   collaborator's hand*.
9. **§28.6's table header is shattered mid-word in the original input (docket 28).** L7462–64
   splits *count* into *co* · *un* · *t*; PP P7386–88 is identical. Repaired with §27.1's shattered
   table, not separately.
10. **Single-witness additions (docket 17):** *30 of 30* (L7554) and *60 cells* (L7533); and *129*
    (L7550), whose apparent corroboration in the Register and the Mathematical Compendium is entry
    numbers, not the claim. **A numeral sweep must be read for what the numeral means at each
    site, not counted.**

## Chat 108 — deferred out of the unit main L7559–L7643 (§28.7.3)

1. **Twelve item numerals are missing from a section whose heading says *all printed* (15h-01,
   15h-02).** 99–105 and 140–144 are absent from §28.7.3 and from the whole of chapter 28
   (numerals 49–164, 104 distinct). PP P7483–P7566 has the identical gaps — authoring gap, not
   production loss — and PP P7482 prints the **placeholder heading** *### 28.7.3 From more from the
   audit work of the final session, all printed*, so *Seventy-five* was computed later from
   149 − 75 + 1 rather than counted. R3 either prints the twelve, renumbers the block, or drops
   *all printed*. **Sweep owed: every count word in the six volumes that PP prints as a
   placeholder — this is the second instance of DEF-107 item 1 and the first with a mechanism.**
2. **§28.7.4's heading says *Forty more* and its numerals are 150–164, fifteen (15h-03).** A
   junction measurement only; §28.7.4 is unread. The next chat measures it in its own read before
   this is treated as closed.
3. **Two corrections are printed twice under different numerals (15h-06, 15h-07).** Item 89
   (L7571) recurs word for word as the third of *90–92* (L7577); items 110–111 (L7599) recur as two
   of the four in *119–122* (L7614). Twelve numerals for ten corrections, in the same list that is
   twelve numerals short. R3 repairs these with 15g-01's orphan 59 and DEF-107 item 7's duplicate
   118 **in one numbering pass over chapter 28**, then re-checks every count word against its body.
4. **Two closing notes four lines apart count the same population differently (15h-08).** L7573–75
   says *fifteen corrections, eleven in test harnesses and four in the book*; L7579–80 says
   *twenty corrections, fifteen in test harnesses*. Three numerals (90–92) lie between them. R3
   states one population and drives both notes to it. Docket 21.
5. **Four register self-citations, corroborated under neither reading (15h-09).** L7601–02 cites
   the register's *first* and *hundred-and-tenth* entries, L7616–17 its *hundred-and-nineteenth*
   and *third*. Register compendium entries 1 and 3 are about the origin and about families as
   spatial neighbourhoods; 110 and 119 are both *SUPERSEDED … see register 313*. Read instead as
   chapter 28's own withdrawal numbering, items 110 and 119 are printed here and fit, but 1 and 3
   fall in the unprinted 1–48 range (15g-04). **The phrase *written past the number beside it* has
   two sites in six volumes, both in this section.** R3 must fix which register these notes cite
   before either can be checked — this is 15g-04's gap made load-bearing.
6. **§31.1 carries the correlation the unit says it never carried (15h-10, census row 1165).**
   L7636–37 calls §31.1's object list *missing six — including the Hill-radius correlation measured
   in §23.14.1 and never carried across*; §31.1 L8626/L8628/L8633 print Hill stability, the Hill
   radius and *satellite counts vs Hill radius — log–log +0.86 across six planets — §23.14.1's
   capacity bound*. Docket 15's shape: a withdrawal narrated against a section since rewritten past
   it. **Sweep owed: every withdrawal item in chapter 28 that describes another section's state,
   re-read against that section as it now stands.**
7. **Three failed pointers with homes located (15h-11).** §6.2 for the Janet table, which is
   §6.1.1's at L1585/L1587; §30.3.1 for the characterisation, which is §2.15.2's at L703; and
   §23.10/§31.1 for *matched-order V oscillates about Proposition 23.1's floor*, whose home is
   §23.10.2 L6453 in different words (*V stays near 2 at matched order*) and which §31.1 does not
   state at all. Docket 9, now four members richer again. **Recorded only after testing under both
   `body_range` and `section_span`: §31.2 and §31.3 resolve under the second and are not findings.**
8. **Two count words against their own bodies (15h-04, 15h-05).** *75–79. Four hypotheses* spans
   five numerals, names four rules and prices them with three figures (652 %, 560 %, 1,156 %);
   *80–83 … wrong three times* spans four numerals and names three failures.
9. **A mid-sentence break inside item 123–139 (15h-13).** L7621 ends *…four times; a*, blank line,
   L7623 *criterion proved against…*. 15f-08's class; repaired with §27.1's and §28.6's shattered
   tables in one formatting pass. Docket 26/28.
10. **Ruling 45, docket 5, reaches twenty-five members** with §28.7.3's own heading tag (L7559).
    Seven further sites of the same vocabulary inside the unit: *the final session* (L7559), *in one
    hour* (L7582), *the person operating it* (L7575), *I hardcoded it* (L7597), *for an hour*
    (L7614), *for one message that was recorded as evidence* (L7631), *in the same session and not
    written down* (L7638).
11. **Docket 15 gains a ninth site in a new word-form.** L7584 prints ***The** earlier version's
    Figure 15.3*; the eight carried sites are all *An earlier version*. A sweep on the indefinite
    form alone misses it. Figure 15.3 has one site in six volumes — its own.
12. **Single-witness addition (docket 17):** **1,156 %** (L7562), the only figure in the unit with
    one site across the six volumes.

## Chat 109 — deferred out of the unit main L7644–L7720 (§28.7.4 … §28.7.9)

1. **The count-word class is now three members and the mechanism is proved twice more (15i-01,
   15i-02).** §28.7.4's *Forty more* is the numeral span 150–189 (40 exactly) against a body of
   fifteen; §28.7.7's *119, printed individually* is the span 203–321 (119 exactly) against a body
   that names 203–288 and **prints nothing at all**. With §28.7.3's *Seventy-five* (span 75, body
   63) the rule is: **the heading counts the span, the body carries part of it.** PP prints
   §28.7.3's and §28.7.4's headings as placeholders and already carries §28.7.7's 119 — so the
   sweep owed at DEF-108 item 1 must distinguish count words filled in later from those in the
   input. R3 repairs all three in the one numbering pass over chapter 28.

2. **§28.7.6 is a heading with no body, and PP has it empty too (15i-03).** Authoring gap, not
   production loss. **The first member of docket 1's heading-only class outside §14.5**, and it is
   cited from the line immediately below it. R3 authors it to what §2.19.1 and §28.7.7 already say —
   but they disagree (see 3).

3. **Seven counts for two sections that have no body between them (15i-04, 15i-05).** §28.7.6:
   heading *Two*, §28.7.7's *three*, §2.19.1's *four*. §28.7.7: heading *119*, body *203 to 288*
   (86), §2.19.1's *eighty-seven* and *a hundred and twenty*. The factor arithmetic sides with
   three (86 ÷ 3 = 28.67 against 86 ÷ 2 = 43.00), and the block shift 199–284 → 203–288 sides with
   four. R3 states one population per section and drives every site to it. Docket 21 and docket 31.

4. **§2.19.1 declares the repair done on a citation that does not support it (15i-06, 15i-07).**
   It cites **Register 286**, which sits in the grouped entry `### 203, 215, 218, 259, 280, 283,
   284, 286, 291` whose body is §4.2 *wrote into a structure without reading it* and lists nine
   instances, none a false heading count. **Register 289 is the entry that states it** — *§28.7.3 IS
   TITLED FIFTEEN MORE AND COVERS SEVENTY-FIVE ENTRY NUMBERS*. §2.19.1 also names *Fifteen more* as
   a live §28.7 heading where the volume prints *Seventy-five more*, and **§2.19.1 is identical in
   PP**. **Sweep owed: every section that declares a defect repaired, re-read against the sections
   it names and against the entry it cites.** This is docket 23 at its most load-bearing — a repair
   recorded as done, on a citation off by three, over a heading that still states a span.

5. **Register 571 is cited twice and does not exist (15i-09).** L7719 *Registers 571–572* and
   §32.6.1 L9274. 572 corroborates word for word. `register_cites.py` already measures the whole
   class — *cited but no entry* — so R3 has the instrument; the list begins 344, 571, 1002, 1149,
   1223, 1257. Docket 9 at Register scale.

6. **An attribution whose target does not exist (15i-08).** *§3's CONSISTENCY audit exists because
   of 186. Its exhaustiveness clause exists because of 189.* §3 carries CONSISTENCY (audit 3,
   L1049) and **no `exhaustiv*` anywhere in its 78 lines**; *exhaustiveness clause* has one site in
   six volumes, the claim itself. Adjacent and owed: §3 prints numbered rows **1–7** while stating
   *twenty-two audits* and naming twelve more, so **§2.19.1's *audit 15 ENUMERATION* has no row 15
   to point at** — R3 numbers §3's audits before either citation can be checked.

7. **Ruling 46 reaches the Register's purpose paragraph (15i-10).** L7658–L7661 carries *since
   Build 9*, *whose file is the source* and *at this build* twice, inside the paragraph that states
   what the Register is for. Docket 6, run with docket 5's two new prose sites (L7669, L7677).

8. **Two of the ten mechanism names cannot be resolved against §4 (15i-12).** *detector artifact*
   and *claimed completion* are the **Register's** names (reg L1333, L1337) for §4.7 *a flag is a
   hypothesis* and §4.3 *a claim of completion is a claim*. The other eight match §4's wording.
   **Sweep owed: every place the book names one of the ten mechanisms, against §4's printed names.**

9. **The chapter's item numerals are Register entry numbers — settled for this block (15i-13).**
   *see 186 below* has nothing numbered 186 below it (the chapter stops at 164) and resolves to
   Register 186, *TWENTY-EIGHT CROSS-REFERENCES, NOT TWO*, corroborating exactly; 189 corroborates
   §28.7.5's second audit entry likewise. **This closes the reading question 15g-04 and 15h-09 left
   open for §28.7.4–§28.7.5**, and it means every unprinted numeral in the chapter names a real
   Register entry that the chapter promised and did not print.

10. **§4 is a table, not a set of sections (15i's F2).** §4.1–§4.10 are indented rows at
    L1441–L1452, invisible to `heading_line`. Any pointer sweep that resolves §4.x by heading will
    report ten false absences. **r2lib owes a table-row resolver alongside `body_range`.**

11. **Single-witness additions (docket 17):** *the direction the register has been maintained*
    (L7680), *it keeps recording an index as a scalar* (L7714), *ρ collapsed route into a number*
    (L7715), *an interpretation written before the number above it was read* (L7645) and
    *exhaustiveness clause* (L7673) each have exactly one site in six volumes.

12. **Verified and not to be re-derived:** §28.7.9's 3 + 3 + 4 = 10 and 7 + 15 + 18 = 40 partition
    §4's ten exactly once each, corroborated at §4 L1454–58 and Register 572; L7661's *392 entries
    cited in main* is exact under `register_cites.py`; §32.6.1 states all three faults attributed to
    it in its own words; §24.4 now carries exactly one incoming pointer in the main volume.

## Chat 110 — deferred out of the unit main L7721–L7855 (§28.8, §28.9, §28.9.1)

1. **The heading-only class now has three members outside §14.5, and one of them is load-bearing
   twice over (15j-01, 15j-02).** §2.22 *A corroborable entry must carry its object, and the object
   must carry it* — L1145, zero body lines, empty in PP — is cited at L7809 as the thing the
   withdrawals register **closes through** and at L7835 as the reason §2.22 *is a requirement and not
   a tidiness*. §28.9 — L7772, zero body lines, empty in PP — is cited at L7806 for an envelope
   printed in its own subsection at L7831. With §28.7.6 (15i-03) the class outside §14.5 is three.
   **R3 must author §2.22 first**: two later sections already state what it must say, and its title
   states it exactly. Docket 1.

2. **A pointer whose true home is verbatim (15j-07).** L7740's *That is §16.4 form — one coordinate
   bounded by a monotone function of one other* is the sentence printed at **§7.2 L1765**, whose
   heading is *Every constraint is of one form*. §16.4 is the ⅅ_def two-routes section and carries no
   such form; App F.4.3 L11379 states the same closure rule. Identical in PP. **Sweep owed: every
   *§N form* construction in six volumes against the section that prints the form.** Docket 9(a).

3. **An event with three attributed homes and a fourth where it is described (15j-08).** The
   anchoring error is **described** at §28.4 L7444; attributed to **§25.6** at L7472 and L7723 and to
   **§28.6** at L8080. §25.6 is *The one deduction, and why it is not a prediction* and carries no
   anchoring content, in the volume or in PP. Docket 8 already records a separate failing pointer
   into §25.6, which makes §25.6 a second magnet alongside §24.6. **R3 fixes the home once and
   drives all four sites to it.**

4. **Two figures that cannot both stand, in adjacent sentences (15j-03, 15j-04).** 210 + 93 + 10 + 7
   = 320 against *Of 319 entries*, and *67.5% recorded but not repaired* against 210/319 = 65.8 %.
   67.5 % is exact only at 216 of 320. R3 recomputes the classifier's four counts, states one
   population, and drives L7803, L7804, L7851 and the growth table to it. Docket 31.

5. **A false superlative that has already propagated into the Register (15j-05).** *The densest
   object in this book after the periodic table's 71.4%* fails against §12.11.1.1 L3189, where the
   eleventh axis at the book's caps is 10,585/13,585 = **77.9 %**. **Register 416 states the same
   superlative in its own words.** The 71.4 % comparison has exactly one site in six volumes and is
   never computed. **Sweep owed: every *densest / largest / strongest / only* superlative against the
   printed tables, and every Register entry that restates one.** Docket 19 and docket 14 together;
   the Register entry is corrected by a new entry citing 416, never by editing it.

6. **A count word against the items it introduces, one level down from a heading (15j-06).** *The six
   cells the register admits and lacks* lists three, or four at the most generous reading. The
   count-word rule proved three times in chats 108–109 was about headings; this is the same shape in
   **body prose**. Docket 21.

7. **Ruling 46 reaches a reader-facing sentence about the classifier (15j-09).** L7852 *stated here
   as a reading whose conditions are the regex*. Run with docket 6's seventeen main-volume sites and
   15i-10's Register purpose paragraph.

8. **Docket 15 gains a new word-form (15j-10).** *An earlier draft* at L7727, against the nine sites
   of *an earlier version*. R3's sweep must cover both forms and *a previous draft* before it can
   claim completeness.

9. **Docket 5's heading-tag sub-sweep is COMPLETE.** The volume's seven *retained in the compendium*
   heading tags are L7426, L7481, L7506, L7531, L7559, L7644 and **L7774**, all now recorded. The
   prose sites of the Ruling 45 class remain open.

10. **The chapter's numbering, measured from a corrected instrument.** 41 item lines, 17 heading a
    range, 104 distinct numerals covered, maximum 164, 59 printed twice, 60 numerals below the
    maximum never covered, and **155 numerals above 164 never printed at all** against L7780's *319
    entries*. **Any future sweep must match the bold form `**58.` and the range form `**112–118.`** —
    a plain numeral regex reads 8 items out of 41 lines. Docket 31.

11. **Three of four fibres carry figures (15j-13).** LAW 44/11/E = 1, REFERENCE 23/11/E = 8, OBJECT
    80/–/E = 19; **PROCEDURE is never printed**, nor is OBJECT's cell count. 147 of 248 or of 319 is
    accounted for. Docket 10.

12. **Verified and not to be re-derived:** 47 + 105 = 152; 20 + 19 + 6 + 1 + 1 = 47; 33/48 = 68.8 %
    under both conventions; the box of 48 counted from the printed coordinate lists (4 × 3 × 4);
    319 − 248 = 71; *the two rarest values* holds on the printed counts; Register 416 and 486 both
    exist and support their citations; §16.5, §18.4.1 and §2.18 all resolve to their claims; 0 of 70
    long lines recur; L7774 is the last heading tag; §14.5.7 measures 24 citations across six
    volumes, exactly as chat 95 recorded.

13. **Instrument rules earned here, owed to r2lib with the three already listed.** A **stem test must
    be left-bounded only** (`has_token` is letter-bounded and reads nothing for *corroborat*); a
    **claim test must exclude the heading line**, or a body-less section resolves on its own title;
    a **pointer-site regex must use `(?!\d)(?!\.\d)`**, never `(?![\d.])`, which rejects a pointer at
    the end of a sentence; and a **token test is not a claim test** — §2.18 was called unresolved on
    a word I chose, and reading the section verified it.


## Chat 111 — deferred out of the unit main L7856–L7939 (§29–§29.2.2) with L8222–L8237 (§28.10)

1. **A count with no home, against four the book does state (15k-01).** L7911's *six of the eleven
   items in Q* fails against every enumerated size: **seven** asserted by §32.2 (quoted at E.4.1
   L11133), **eight** enumerated (main L1285, E.4.1 heading L11132, E.4.2 L11139, Register L841),
   **thirteen** current (E.4.1 L11135, E.4.2 L11140, main L10906) and **fourteen** (Register L6447,
   *Q RE-CLOSED AT FOURTEEN*). *Eleven* co-occurs with Q at one site in six volumes — L7911 itself.
   The six letters are all correct. R3 fixes the total alone and states which state of Q the
   sentence speaks from. Docket 30's shape at a second object; docket 17.

2. **A pointer whose subject the target does not carry, and nothing else does either (15k-02).**
   L7916's *the shape §29.4 already describes — Q growing at nearly every step while its scope
   falls*. §29.4 is *On priority for V = 4ν/3*; both phrases have exactly one main-volume site,
   L7917. Nearest recorded statement: E.4.2 L11139–L11140. **Sweep owed: every *the shape §N
   describes* construction against the section that prints the shape.** Docket 9(a).

3. **A second quotation whose true home is verbatim elsewhere (15k-03).** L7907–L7908 attributes
   *E(X) is deliberately not claimed as novel* to §29.3; §29.3 carries neither *E(X)* nor
   *deliberately*, and the phrase is printed at **L8094, inside §29.8**. Identical shape to 15j-07
   (§16.4 → §7.2). Two in two chats — the class is not incidental. Docket 9(a).

4. **A citation that carries two owners the target does not (15k-04).** L7890's *Four independent
   owners … quoted and cited at §23.8.4*: §23.8.4 (L6372–L6382, body and span identical) carries
   Moore and IEEE; **Manski and Shannon are absent under both resolvers** and are cited at §29.7.
   Docket 9(a) and docket 23.

5. **The count-word rule at blockquote scale (15k-05).** *Four independent owners* is followed by
   three named in the prose (Moore, Manski, Shannon); the table row L7883 names four, and IEEE 1788
   is the one the prose drops. With 15j-06 this makes **three scales** of the class: heading, body
   prose, and now blockquote-against-table. Docket 21.

6. **A heading count word against its own table, found outside the unit while resolving it
   (15k-06).** §29.6 L8029 *The three documents we could not reach* over a table of **four** —
   Edlén 1964 L8034, Ritz 1908 L8035, Paschen & Götze 1922 L8036, Dunz 1911 L8037. In PP at P7951.
   Docket 21 and docket 32. **Chapter 29's remaining sections are not yet read; this one is already
   measured and must not be re-derived.**

7. **A repair declared, three-quarters made (15k-07).** L8227–L8228's *Each is now cited where its
   finding is* names four homes. Three verify — §30.3.9 (Lubiw L8565, Anstee and Hoffman L8564),
   §14.6 (Kuznetsov L4080, Caspard L4079, Colomb L4078), §30.3 (Van Isacker L8401). **§12.11 carries
   none of the eight under either resolver** (body 2524–2535, span 2524–3508); the pair it must mean,
   Chandrasekaran & Flanagan, is at **L4229, §14.6.5**; and *modular interval* has one site in six
   volumes, the claim itself. Docket 23's largest new member, and docket 9.

8. **Docket 30 gains its fifth and most repeated figure (15k-08).** The Register's size is printed
   **in words at fifteen main-volume sites** — L20, 89, 104, 202, 523, 646, 3514, 7367, 7900, 8918,
   9055, 9364, 9376, 9381, 10296 — and **zero times in Prints & Proofs**, so the spelled form was
   introduced after the input. Against it: '1,635' main L7373, '1,631' main L7658, reg '1635' L6,
   L65, L6127, L6133, reg '1628' L6109, L6115, reg '1660' L6221, L6251, and a measured **1,628 bare
   + 7 grouped = 1,660 distinct entry numbers, maximum 1792**. R3 fixes the unit of the count once
   and drives **all twenty-three sites** to it, spelled and numeric together.

9. **A fifth figure for chapter 28's size, from an entry this unit cites (15k-09).** Register 658
   reg L2431: *Chapter 28 held **273 entries** and 187,432 characters*, against L7780's *319* and
   chat 110's partition summing to **320**. Docket 31 now has three populations and a percentage
   that matches none of them.

10. **Two pointers recorded as R3 reads, not as deviations, because a token test is not a claim
    test.** §12.11.0.10 (*Every Λ in one table*, span 2932–2957) carries neither *promotion* nor
    *branch*, and L7934–L7935's figures — 12.14 at L3006, 185 at L3012 and L3027 — lie **outside its
    span**. §32.5 (*The book satisfies its own method*) carries *falsif* 0 under both resolvers
    against L7896's *does it state its falsification conditions? yes, §32.5*. **R3 reads both
    sections before either is called a defect.**

11. **Docket 15's new word-form is confirmed as a class, not a one-off.** *An earlier draft* now
    measures **seven main sites** — L6453, 7727, **7857**, 8365, 9065, 9311, 11566 — against *an
    earlier version*'s eight raw and one join. L7857 is a chapter's opening sentence. R3's sweep
    covers both forms and *a previous draft* (zero sites) before claiming completeness.

12. **Docket 29 is measured directly and PP settles its origin.** §29.11.2 L8179 → §28.10 L8222 →
    §29.12 L8238, with the contents list printing only `## 28.` L150 and `## 29.` L151. **PP prints
    §28.10 at P8144 in the same position**, so the out-of-order placement is original, not a
    production artefact. R3 moves or renumbers and re-checks the contents list, the Index of Indices
    and every pointer assuming source order.

13. **Verified and not to be re-derived:** Register 238, 335, 658 and 659 all exist and support
    their citations (headlines quoted in READ-ch15k.md §B); L7874's four search figures reproduce
    exactly against §29.7.1's corrected statement at L8076–L8078; *Three things* → three bold leads;
    *Those five* → five rows; *Eight references* → eight names, matching Register 659; the six Q
    letters B, C, F, G, K, N all enumerate in Appendix E (K at L10954 is *the earlier bound
    2J_c ≤ k, tested for containment*, matching the unit's *2J_c containment claim*); the attribution
    table is eight component rows over eleven indented lines; 12.14 and 185 both have other homes;
    seven of the eight orphaned references land in a named home; every §-pointer in the unit resolves
    to a body heading.

14. **Instrument rules earned here, owed to r2lib.** A **left-bounded stem matcher** — `has_token`
    is letter-bounded on both sides and scores every stem zero on its inflected forms, which is the
    same fault the handoff recorded for *corroborat* and which fired three times here. A **raw symbol
    test**, because a symbol is not a word. And the standing rule made procedural: **an absence found
    under `body_range` is retested under `section_span` before it is written down**, since
    `body_range` truncates at the first subsection heading.


## Chat 112 — deferred out of the unit main L7940–L8028 (§29.3–§29.5.5)

1. **Two page counts, two conventions, four lines apart (15l-01).** *A six-page expert review*
   (L8021) is inclusive and exact for 805–810; *Absence from 140 pages* (L8025) is exclusive for
   80–220, which is **141** inclusive. Each figure has one site in six volumes. R3 fixes the
   convention, states it once, and drives both sites to it. **Sweep owed: every page range in the
   six volumes against the count word that reports it.** Docket 17.

2. **A heading that is a false universal against its own table (15l-02).** §29.5.1 *Every equation
   in the review is a fit* over a status column marking (2) *theoretical α's* and (4)–(5)
   *definitions* — 3 of 7 numerals not fitted. The body's *Not one is a bound* is correct and
   untouched; the repair is to the heading alone. Second heading-against-table instance in two
   chats after 15k-06. Docket 19 and docket 21.

3. **Principle 8 cited for a status it does not assign, and never enumerated (15l-03).** L7947
   attributes the superseded-not-false doctrine to Principle 8; the only other site, L9316, states
   it as *any true answer, good or bad, is a bound* with *supersed\** 0 and *every* 0. The literal
   form `Principle N` returns **only** `Principle 8` across six volumes, and chapter 1 carries no
   numbered list in which an eighth principle can be located. R3 must either number the principles
   or restate the citation. Docket 9(b) and docket 10.

4. **Docket 16 is six times larger than carried (15l-04).** Edlén is dated **1960 at 4 lines**
   (main L6676, L7884, L7886, L11621) and **1964 at 25** (main L4550, L5433, L5453, L7961, L8015,
   L8034, L11624; reg L2129, L2149, L3497, L3513, L4569; mc L184, L188, L2370, L2372, L2810,
   L2814, L2822, L2826, L2872, L3106, L3471; pc L569; ioi L1508), against L8018's *this book cites
   it accordingly*. §29.5's own heading L7961 is one of the 25. One pass over all 29 sites.

5. **One work, two bibliography entries, two dates, two titles (15l-05).** App F.4.3 L11621
   *Edlén, B. (1960). Handbuch der Physik 27, 80.* and L11624 *Edlén, B. (1964). Encyclopedia of
   Physics.* — the same chapter, three lines apart, the second pointing at §29.5. **Sweep owed:
   every bibliography entry against every other for one work under two titles.**

6. **A third verbatim-elsewhere pointer in three chats (15l-06).** L7995 cites §23.3 for *V has no
   use in a fitting paradigm*; §23.3's body carries *fitting* 0, *paradigm* 0, *use* 0 under both
   resolvers, and the sentence is printed at L9356 in §32.7. Unlike 15k-03 the target does support
   the substance (L6228, *V is not an instrument*), so R3 may repair by redirection or by rewording
   rather than by relocation. Docket 9(a).

7. **Both age statements for the chapter are stale, and disagree (15l-07).** The book's present is
   **2026**; L6683's *sixty-five years old* on the 1960 manuscript should read sixty-six, and
   Register L3497's *sixty years old* on a 1964 dating should read the same. **Sweep owed: every
   "N years old" statement in the six volumes against a stated present of 2026** — the scan already
   surfaces main L3691, L6381, L8136 and reg L897, L3393, L3497, L5225, L5449, L6079. Docket 16 and
   docket 14.

8. **A drafting-history remark to a reader (15l-08).** L8018 *having previously been stated from
   recollection*, in PP at P7939. Docket 5 and docket 15.

## Chat 113 — deferred out of the unit main L8029–L8097 (§29.6–§29.8)

1. **A section restates the sentence its own cited chapter withdrew (15m-01).** §29.6 L8039
   prints *ρ ≤ 2 for each; every route closed*, the exact clause of §19.5 L5433–34, and cites
   *the analysis of Chapter 19* for it. §19.5.1 L5445–46 quotes the clause and rules **both
   are wrong**; its table L5450–54 prints ρ = **3, 3, 2, 0**, so *ρ ≤ 2* fails at two of four;
   L5456 states *three of the four are retrievable*; L5490 states *Edlén and Ritz are UNKNOWN,
   not closed*. §16.6.1 L4550 already flags the conflict from the other side. R3 rewrites
   L8039 to §19.5.1's coordinates or deletes it. Docket 23, at chapter scale — the largest
   member after 15l-04. **Sweep owed: every section that cites another for a figure the cited
   section later withdrew.**

2. **"Four owners of the cost-of-rigour framing" — three statements, no common reading
   (15m-02).** L8064's count word is four and its colon-list names three; the tables mark the
   framing at three rows naming five works; L8066 makes the book *the fourth*; L8085 says four
   owners were *found*. R1 breaks L8085, R2 breaks the colon-list and L8066, R3 breaks both.
   R3 must fix the unit of "owner" and drive L8064, L8066 and L8085 to it. Docket 21, 14.

3. **A universal refuted by the table beneath it, over a partition never printed (15m-03).**
   L8043–44's *the ones sharing this book's mathematics also supplied new derivations* fails
   at Richardson extrapolation (*attribution only*) and regression curvature; WKB (*different
   quantities*), and no row is labelled mathematics or philosophy. Third
   statement-against-its-own-table in three chats after 15k-06 and 15l-02. Docket 19, 21, 10.

4. **A cited figure that exists nowhere but its own citation (15m-04).** L8070's *§29.7
   reported 7/7 on controls*: §29.7's body under `body_range` carries *control* 0, *controls*
   0, *calibration* 0 and raw *7/7* 0; the `section_span` hits are the citing section itself.
   `7/7` has one main-volume site — L8070. **The two resolvers differ and the difference is
   decisive; record that.** Docket 9(b), 10.

5. **A fourth attributed home for the anchoring failure (15m-05).** L8080 attributes it to
   §28.6; §28.6's own L7472 attributes it to §25.6; §28.8 L7723 likewise; §28.4 L7444 is where
   it is described. Extends 15j-08 into chapter 29. Docket 9(a), 9(d).

6. **Docket 7 resolved as a finding (15m-06).** The affine-invariance reason is stated at
   **§23.8.3 L6368** itself. Neither carried target holds it: §29.7 L8052 is an attribution row
   naming self-concordance without a reason, and the App D.4.1 window L10371–L10395 carries
   *affine* 0, *invarian* 0, *reason* 0. 14l-16 should be re-stated in those terms rather than
   left open.

7. **A four-author survey with three authors nowhere else and no bibliography entry
   (15m-07).** L8096's *Habib, Nourine, Raynaud & Thierry, Theoretical Computer Science 312
   (2004), 401–431*: Habib, Nourine and Thierry each have **one site in six volumes — L8096 —
   and no Appendix F entry**, while Stahl & Wille (L11771) and Yannakakis (L11774), cited in
   the same sentence, both have entries. Docket 17, 20. **Sweep owed: every attribution in the
   six volumes against Appendix F for an entry.**

8. **A count word right about rows and wrong about members (15m-08).** *Nine literatures* is
   exact over 6 + 3 rows, but the ninth row is *regression curvature; WKB* — nine rows, ten
   named literatures — and the figure is restated at L8076 and L8085. Docket 21, 31.

9. **A partition covering seven of nine, with unprinted membership (15m-09).** L8074's
   1 + 4 + 2 = 7 against nine entered; which four and which two is never printed, and L8076's
   *most by one or two searches* leaves four with no stated depth. Docket 10.

10. **The two-line-join sweep in r2-ch15r/s double-reports every hit.** A phrase lying wholly
    on line *i* is also inside the join of *i−1* and *i*. The function is one of those owed to
    r2lib; **R3 must lift the repaired form carried in r2-ch15t/u, not the carried one.** Any
    count taken from the faulty version is doubled.


## Chat 114 — deferred out of the unit main L8098–L8221 (§29.9–§29.11.2)

1. **A parsed total contradicting its own partition and four later figures (15n-01).** L8190's
   *103 designations parsed* against L8196's *ten* + *ninety-two* = 102, and against L8199,
   L8209's *one hundred and two*, L8209's *forty-eight left out* and the 53 %. R3 drives L8190
   to 102 or explains the one designation that was parsed and then dropped. Docket 14, 10.

2. **A growth factor printed at 5.5 that measures 5.4 (15n-02).** L8200's *a factor of five and
   a half* against 54/10. R3 prints 5.4 or restates the base. Docket 34.

3. **Registers 253 and 254 cited for a claim their entry does not carry (15n-03).** L8213. The
   grouped entry `### 227, 253, 254, 305` (reg L1327) is headlined *§4.6 — A TEST THAT COULD NOT
   FAIL*. Register **1578** is where Appendix B L10205 puts the parent-term wall. R3 redirects.
   Docket 9(b).

4. **Register 251 cited at the wrong paragraph (15n-04).** L8220 pairs it with 252 for the
   referee-flag-5 regrade; 251 is the quantum-mechanics category search of L8156–62, which
   carries no citation. R3 moves it. Docket 9(a).

5. **"Fifty years" against 1975 and a 2026 present (15n-05).** L8136, L8141, and §14.1 L3691 and
   reg L897 with it — four sites, measured 51. R3 drives all four to one figure and to one
   convention. Docket 15, 16.

6. **Kurucz, VALD, BRASS, Hasse and QSAR: named claims, no bibliography entry, no R.7 exemption
   (15n-06).** MEASURED against `## References` L11503–L11855. BRASS carries two specific
   findings at L8168–70 and Kurucz a quantitative estimate at L8170–71. R3 adds entries or names
   them in R.7. Docket 36, 17, 20.

7. **Appendix B cited for a channel total Appendix B records as overtaken (15n-07).** L8189's
   *153 channels* against B.2's *596 channel rows across 28 elements and 70 species* (L10195–97),
   the withdrawal at L10203–08, and the arbiter at spectra L900. R3 restates §29.11.2's
   denominator. **Docket 35's second member**, and here the withdrawal sits four lines below the
   withdrawn figure in the same appendix.

8. **E(search) incremented twice, valued never (15n-08).** Six main sites, all inequalities or
   growth statements. R3 either prints a value and a base or stops incrementing it. Docket 10.

9. **Eight Ruling 45 process remarks (15n-09).** L8180, L8184, L8186 ×2, L8187, L8195, L8208,
   L8220, with L8186 the strongest — the drafting tooling, not the subject matter. Docket 5.

10. **Negative witness worth keeping.** Appendix D's precedent coordinate for A.2 **has** been
    executed — App D.5.2 L10575 prints *proved · exhaustive · found*, as L8137 declares. Docket 23
    should record the case that closed correctly alongside the cases that did not.
## Chat 115 — deferred out of the unit main L8238–L8346 (§29.12, ch30 head, §30.1)

1. **A heading count word its own body refutes (15o-01).** L8238's *Five unlocated results*
   over five U-blocks of which **U1 is marked LOCATED** at L8245, leaving four. L8239–L8240's
   framing — *statements … for which these searches returned no source* — fails on U1 by the
   same measure, since U1 names Kimura, Makino, Yamada and Yoshizumi (2024) and the literature
   term *2-decomposability*. U1's own narrowing (what remains unlocated is **the count**) is
   sound; the heading and the framing sentence are not. R3 restates the heading to four or
   re-frames the list as *five results, one since located*. Docket 21, 31.

2. **A universal the section's own fifth item breaks (15o-02).** L8241–L8243 says each result
   carries a definition, the search, **the test that would confirm it**, and the falsifier.
   MEASURED: definition 5/5, search 5/5, falsifier 5/5, **test 4/5** — U4 (L8288–L8299) prints
   *Definition · Searched · Proved · Falsifier* and no test. R3 supplies U4's test or narrows
   L8242. The falsifier universal at L8243 HOLDS. Docket 19, 21.

3. **A magnitude printed as a ratio (15o-03).** L8341's *a twenty-three-fold rise* against the
   table at L8336–L8339: 23.40 / 1.05 = **22.29**, 23.40 / 6.90 = 3.39, and the 0.50–1.00
   bucket is 0.00 and yields no ratio. Twenty-three is the value 23.40 itself. R3 prints
   twenty-two-fold or restates it as a magnitude. Docket 34.

4. **A corrected figure with no antecedent anywhere (15o-04).** L8329's *The earlier figure of
   139 was a random sample*. MEASURED digit-bounded across six volumes: 139 has **14 sites**,
   every one of them the seed compression *139 to 1* (main L3775, L3935; mc L96, L119, L724),
   the register range *123–139* (main L7619), a Register heading (reg L627), a table cell
   (ioi L519), or an unrelated figure. **No site prints 139 as a count of reorderable
   instances.** R3 prints the earlier figure or drops the correction. Docket 15, 10.

5. **Four process / past-state remarks (15o-05).** L8329 *The earlier figure of 139*, L8330
   *the instances were re-drawn*, L8311 *the three exact sets §12.11.1 **now states***, L8293
   *the proof corrects **the guess that preceded it***. Docket 5, 15. **Reported apart from
   nine plain self-references** (L8239, L8243, L8245, L8274, L8283, L8298, L8310, L8313,
   L8319) which are subject matter, not process — a flat sweep overstates this class by more
   than three to one, and R3 should apply the same split to the standing Ruling 45 list.

6. **Negative witnesses worth keeping, so two classes are not made to look worse than the book
   is.** (a) **Docket 36's first entirely clean unit**: every attribution here is bibliographed
   — Kimura, Makino, Yamada, Yoshizumi at `## References` L11561, Helly at L11767, *row-convex*
   and *2-decomposab\** three times each inside References L11503–L11855. (b) **L8312's seventh
   figure is legitimate**: 1,561 is Λ₉′ = Λ₉ ∩ {2S′ ≤ 2f+1}, and the list is printed in tower
   order, not numeric order. (c) L8310's *nothing else* holds — §12.11.1 carries the Λ₉′
   constraint (`2f+1` ×3 in span). (d) U5 scopes itself narrowly at L8304 rather than
   overclaiming.

7. **Nine single-witness figures that are nevertheless verified (docket 17 refinement).**
   8,326 · 4,163 · 73,486 · 36,743 · 363,384 · 181,692 · 2,465 · 23.40 · 6.90 each have one
   site in six volumes, and all nine were **recomputed exactly** in `r2-ch15x`. Docket 17 must
   keep *single-witness* and *unverifiable* apart when R4 reports, or it will mark verified
   arithmetic as unchecked.

8. **A sentence fragment heading body prose (incidental 3).** L8325 *Complete under a targeted
   attack.* — docket 18's shape one level down, in a paragraph rather than a heading.

9. **An unmeasurable universal, recorded as unmeasurable and not as refuted.** L8281
   *Selection rules are universally known* is a claim about the literature, not about the book.
   Docket 19's rule applies: R3 softens rather than tests.

10. **Instrument correction carried forward.** `## References` has **two** occurrences — the
    contents entry at **L173** and the body at **L11503**. Any bibliography sweep must take the
    LAST, exactly as `heading_line` does; taking the first reports every attribution
    unbibliographed. This is the same shape as chat 114's Appendix F fault and belongs in
    r2lib when the owed functions are lifted.


## Chat 116 — deferred out of the unit main L8347–L8450 (§30.2–§30.3.2)

1. **Two count words in one section, both refuted by their own tables, both original (16b-01,
   16b-02).** L8367's *six invariants discovered since* over a table of **four** data rows
   (three structural, one the density itself); L8392's *on five points* over a table of **four**
   rows (d = 2, 3, 4, 5). MEASURED against Prints & Proofs P8291–P8296 and P8307–P8311: the same
   four rows in both. **Authoring gap, not production loss.** L8366 separately names four things
   discovered since. R3 prints four, or supplies the rows. Docket 21, 31.

2. **A regression unreproducible from its own table (16b-03).** L8391–L8392: *the log–log slope is
   2.29 … with R² between 0.37 and 0.42*. MEASURED on the four printed points: **slope 2.33,
   R² 1.00** (Decimal, HALF_UP, 2 dp). Alternatives: log max vs log d = 1.95; log (max/d²) = −0.05.
   An R² near 0.4 belongs to a per-instance fit over the **1,480 instances** of L8383, which are
   nowhere printed. R3 prints the inputs or restates the fit. Docket 10, 34.

3. **A pointer whose target carries none of the claim (16b-04).** L8396's *§30.3.3 completes this
   reading* — the landscape reading of §30.2.3 (E as a potential, transposition as a move, density
   as the size of the basin). §30.3.3 READ IN FULL at L8451–L8475 is *What the interval machinery
   was*; `body_range` and `section_span` **COINCIDE** at (8451, 8476) and carry *interval* 9 against
   *landscape / basin / potential / descent / stall* all **0**. **Where the claim does live**, six
   volumes: *basin* main L8333 and L8396 only; *landscape* main L693, L805, L8394; *descent* main
   L686, L693, L8396, **L8541**; *stall* main L686, L8396; *transposition* main L693, L3704, L8395.
   The completion is at **main L686–L693**, and *descent* recurs in **§30.3.7 at L8541**. R3
   redirects or authors the completion. Docket 9(a).

4. **A caption denominator matching no measurable population (16b-05).** L8446–L8447's *114 of 141
   at arity 4*. At arity k the constraint is on k−1 XOR-difference variables. MEASURED at arity 4:
   **256** relations, **254** non-constant, **164** bijunctive, **80** axis-permutation orbits.
   Neither 141 nor 114 is among them. The arity-3 figure is by contrast **exact** (14 non-constant,
   14 bijunctive). R3 states the population that *arises*. Docket 10.

5. **A splice and a broken paragraph, both present in Prints & Proofs (16b-06, 16b-07).** L8401
   inserts *Van Isacker's survey gives the seniority reduction chains* between L8400's *…cycles, can*
   and L8402's *its coordinate order be recovered?*, which join cleanly without it. L8419–L8422 puts
   a **blank line inside a sentence** and then runs a second sentence onto L8421 with **three runs of
   ≥ 3 consecutive spaces**. The unit is byte-identical to PP for L8347–L8443 at offset −78, so both
   are **authoring, not production**. Docket 26, 28.

6. **Six Ruling 45 sites in 104 lines — the densest cluster measured (16b-08).** L8363 (heading)
   *enumerated once*; L8365 *An earlier draft concluded*; L8366 *the list predates*; L8379–L8380
   *The earlier reading had the second link*; L8411 *a draft withdrew them*; L8412 *The withdrawal is
   withdrawn*. **None of the plain self-reference kind** that chat 115 split off — all six are
   drafting history. L8365 is already one of docket 15's seven *an earlier draft* sites. Docket 5, 15.

7. **Negative witnesses, so three classes are not made to look worse than the book is.**
   (a) **Docket 23's executed case**: PP P8366 prints *Figure 23.1* and the volume prints
   **Figure 30.1** — the caption number was corrected in production, and the volume additionally
   inserts the image reference PP lacks. (b) **Docket 36's second consecutive clean unit**: all seven
   attributions — Van Isacker, Rival, Larson, Siggers, Stahl, Wille, Yannakakis — are in
   `## References` at its **BODY** occurrence L11503, none in R.7; Stahl & Wille (L11771) and
   Yannakakis (L11774) name §30.3 in their own entries. (c) **L8412's reversal leaves no stale
   sibling**: *interval problem* has exactly one site in six volumes, L8412 itself, and L8096
   independently states the same prior art.

8. **Verified so R3 does not re-derive.** Ten named invariants = ten; the density table is strictly
   monotone in both columns and carries L8361; all four max/d² cells recompute exactly
   (2.00, 1.11, 2.25, 1.56) and *the ratio does not climb* holds; 0.606/0.31 = **1.95**, so *by
   twofold* holds as a rounding; 0.883 > 0.628, so the two-link claim holds; **475,800 = C(976,2)
   UNORDERED** (952,576 / 951,600 are the ordered conventions) with **zero join and zero meet leaks**;
   ℛ-closure ≡ join/meet closure on **2,128 independent instances, 0 disagreements**; arity ≤ 3
   **entirely bijunctive** (2/2 and 14/14, matching *all 14* exactly); exactly-one-of-three fails all
   six Schaefer tests. Zero first-person pronouns, zero Ruling 46 sites, zero register citations,
   **zero census rows in range** (witnessed 1179 at L8303 / 1180 at L8553, ids contiguous), and the
   duplicated-section sweep **0 of 53** — the tenth consecutive clean unit.

9. **Docket 17 additions with chat 115's refinement applied.** Single-witness in six volumes:
   **3,781 · 1,487 · 928 · 211 · 1,480 · 396 · 0.883 · 0.628**. The correlations were recomputed or
   cross-checked here; the five **population counts** are not recomputable from the book and are
   single-witness in the strict sense. **0.606 and 0.31 are corroborated** at main L7634–L7635.

10. **Two spellings of one correlation, fourteen lines apart (incidental).** L8352's **−0.68** over
    211 instances against L8374's **−0.628** over 928. Different populations, so not a contradiction,
    but a reader will read the second as a restatement. R3 states the population beside each.

11. **Figure references are a production layer absent from PP (incidental).** The volume carries
    **33** inline `![Figure …]` references and **PP carries none**; no `.png` is a bundle member.
    The unresolvable path at L8444 is **not** a defect of the text and must not be recorded as one.

12. **Instrument correction carried forward.** A digit-bounded numeral sweep must use
    `(?<![\d.,])N(?![\d,])(?!\.\d)`. The form `(?![\d.,])` treats a **sentence-ending period** as a
    digit boundary and scores a decimal figure **zero sites in the very unit that prints it** — it
    reported `2.29` absent from L8391. This belongs in r2lib with the other owed functions. Also:
    canonicalise set orbits over **sorted tuples**, never with `min` over frozensets, which is a
    subset partial order and returns an arbitrary representative.
## Chat 117 — deferred out of the unit main L8451–L8574 (§30.3.3–§30.3.9)

1. **Rival's bound printed in the vacuous orientation, two sites (16d-01).** L8497 and L8500 both
   print |K| <= (3/2)|L| for a maximal sublattice. With K a sublattice of L this holds always and
   bounds nothing; Rival 1973 is |L| <= (3/2)|K|. MEASURED: the adjacent claim *the Boolean case is
   tighter* has content only under the standard orientation, 2/3 = 0.67 < 3/4 = 0.75 (Decimal,
   HALF_UP, 2 dp). The letters are never bound to lattice and sublattice. R3 reverses or binds.
   Docket 12, 34.

2. **A total reachable only by rounding up (16d-02).** L8530's *267,000 subsets* against the table's
   own 256 + 4,096 + 262,144 = **266,496**. Nearest thousand and three significant figures both give
   266,000; only ceiling-to-the-thousand gives 267,000. The three row figures are each exact
   (2^8, 2^12, 2^18 on 8, 12 and 18 cells). Docket 34.

3. **Dilworth cited for a decomposition Dilworth does not produce (16d-03).** MEASURED on the rebuilt
   lattice: |J(Lambda)| = 17, width of J(Lambda) = 7, axes = 8, and 17 = sum of (|A_i| - 1). *width
   7 <= 8* is EXACT; the definite article in *the chain decomposition of J(Lambda) IS the axis
   system* is not, since Dilworth yields the minimum, 7 chains. Docket 19.

4. **A count word right about its rows and wrong about its own labels (16d-04).** L8559's *Three
   walls* over three items of which two name walls; the third is named as the FPT bound BETWEEN
   them. Same shape as chat 115's *five unlocated results*. Docket 21.

5. **The clearest splice yet, and it is ORIGINAL (16d-05).** L8563 ends *Every sublattice and*, L8566
   begins *interval of Lambda has E = 0*, and they join cleanly; L8564 and L8565 insert two complete
   prior-art sentences between them. MEASURED against Prints & Proofs P8481-P8485: the five-line
   block is byte-identical. Authoring, not production. Docket 26.

6. **An unbibliographed attribution (16d-06).** NextClosure at L8510: one site in six volumes, absent
   from ## References at its BODY occurrence L11503 and absent from R.7 L11806; Ganter has zero sites
   in six volumes. The unit's other nineteen attributions are all bibliographed. Docket 36.

7. **Three count words on bodies that do not enumerate them (16d-07).** *nine rounds* (L8510);
   *Three reduction attempts* (L8552), whose sentence gives the shared direction and no enumeration;
   *nine recovered extra edges* (L8563), where the tree MEASURES 7 edges on 8 vertices and 21
   non-edges, and *nine recovered* / *extra edge* have one site each in six volumes. Docket 10, 17.

8. **Two unprinted inputs (16d-08, 16d-09).** L8531's *the 19 canonical forms reduce to 12*, where
   the table prints 30 / 210 / 4,168 and 19 appears only in that sentence; and L8509's *in 47.8 s
   against 86*, where the 86 carries no unit. Docket 10.

9. **Negative witnesses, recorded so three classes are not made to look worse than the book is.**
   (a) **Docket 23's executed case, second consecutive unit**: PP P8413 prints *Figure 23.2*, the
   volume prints **Figure 30.2** and adds the image reference PP lacks — and *Figure 23.2* is LIVE
   elsewhere in the volume at L6328 and L6330, so the renumbering resolved a real collision.
   (b) **Register 247 is exact and on point**, headlined *§30.3.3's FOURTH LEMMA, LEFT ON A CITATION
   AND NOW PROVED IN FULL*. (c) **All four §-pointers hold**, including §2.15.2, whose body at
   (680,716) is titled *Worked, on §30.3* and derives the exact R-closed characterisation.

10. **Verified so R3 does not re-derive.** 2,354 interval sets MEASURED exactly, zero counterexamples
    to the nesting characterisation, and exactly 1,098 refutations under the ordinary-containment
    reading — three printed figures, three exact. prod |A_i|! = 11,943,936 exact. |J| = 17 = height.
    Constraint graph is_tree True on 8 vertices and 7 edges. Twelve boxes = 8 + 3 + 1; steps 1, 2, 4
    against 2^(d-2), and 8 at d = 5; 3*2^(d-2) is 0.75 of the box at d = 2..5 with the caption's
    3, 6, 12, 24 exact. Three method classes over three class paragraphs plus one lead-in. Three
    preserving rules over three arrows. 2^d - 1 hyperedges on a complete hypergraph. E = 0 on 4,112
    intervals sampled 1-in-28 from 115,162 ordered strict comparable pairs, zero leaks. Zero Ruling
    46 sites; duplicated-section sweep 0 of 65 long lines, the eleventh consecutive clean unit.

11. **The step-law table prints its header twice (incidental).** L8480 and L8483 identical, splitting
    three rows into 1 + 2, and MEASURED at P8400 and P8403 in PP — authoring, not production.
    Docket 28.

12. **Instrument correction carried forward, and it is the costliest class again.** A digit-bounded
    numeral sweep must be `(?<![\d.,])N(?!\d)(?!,\d)(?!\.\d)`. Chat 116 corrected the
    trailing-PERIOD half of this boundary; the trailing-COMMA half is corrected here, because
    `(?![\d,])` rejects a LIST comma as well as a thousands separator and scored *2,047* and *86* at
    zero sites in L8455 and L8510, the lines that print them. Only a comma FOLLOWED BY A DIGIT is a
    separator. Also: a symbol is tested RAW and never transliterated — testing *Gamma* where the text
    prints the raw Gamma character would have recorded the holding §2.15.2 pointer as a defect. Also:
    a colon-terminated lead-in is not a list item. Also: one global Prints & Proofs offset cannot
    span a unit into which production inserted a line — anchor each witness on its own text.


## Chat 118 — deferred out of the unit main L8575–L8699 (§30.4 – §31.2.5)

1. **A derivation its own printed set does not entail (16g-01).** §30.4 L8577–L8578 says the closure
   of {V = 4ν/3h, λ² = (2/3)T, w·V = 8λ², T = Z²R/ν²} yields e/T = 3(h/ν)². MEASURED by ideal
   membership, sympy lex order over (V, λ, w, T, Z, R, ν, h, e): w·ν − 4Th IS in the ideal; V·e − w
   is NOT; e·ν² − 3Th² is NOT. The symbol e does not occur in the four. §30.4.1 L8586 lists V·e = w
   among the relations that reduce to zero only now. Repair: add w = V·e (printed at L4349) to
   §30.4's set and strike it from §30.4.1's list, which then names six, not seven. Docket 12, 34.

2. **"At least nine" over eight (16g-02).** L8588–L8591 enumerate eight non-polynomial relations
   after the colon. *nine non-polynomial* is printed again at §30.4.2 L8600 and at main L7636; no
   site enumerates nine. Repair moves all three together. Docket 21, 10.

3. **"This chapter contains five enumerations" spanning two chapters (16g-03).** MEASURED: chapter
   30 = L8316–L8608; the rows cite §31.1 L8614, §31.2 L8659 and §31.3 L8700, all chapter 31. The
   same claim is printed at main L7641 and is byte-present in Prints & Proofs at P7564 — authoring,
   not production, at both sites. This is docket 21's 15h-12 item, now measured and closed as a
   finding. Repair: *this part* at both sites. Docket 21.

4. **A row that is not a member of its column's class (16g-04).** L8604 under the header *what it
   omitted* reads *§31.3's statistic — stated against the wrong denominator*. Docket 21.

5. **A sign pattern broken on its second subject (16g-05).** L8646 prints *L1 and L3 alternate −, +,
   −, +*. MEASURED on μ = 0.01…0.08 step 0.01: L1 −,+,−,+ exact; L2 +,−,+,− exact; **L3 −,+,+,+**,
   third differences positive at every window (3.46e−7 … 3.82e−7). Docket 21, 19.

6. **A superlative on the wrong planet (16g-06).** L8631's *where Titius–Bode fails worst*. MEASURED
   errors: Jupiter 0.06 %, Saturn 4.85 %, **Neptune 29.04 %**. Separately, the third difference of
   the semi-major axes changes sign three times, not once. Docket 19, 21.

7. **Two V values with no printed grid (16g-07).** L8628 Hill 47.9 and L8629 Roche 17.9. MEASURED at
   the grid the section itself prints at L8635 (x = 0.030, h = 0.010): Hill **17.6**, Roche **8.9**.
   Under V ≈ 4x/(h|p−1|) the printed values need x/h = 7.98 and 5.97 respectively. The value the
   Hill row takes on the section's own grid is the value printed on the Roche row; recorded as
   measured, no transposition asserted. Docket 10, 17.

8. **A correction announced with no notice at its target and no Register entry (16g-08).** L8639
   *Which corrects §18.5*. §18.5 L5294–L5302 read in full: it does hold the corrected position
   (*no domain at p = 1*; a guarantee *costs infinitely more than the thing it guarantees*), so the
   correcting claim is faithful — but §18.5 carries zero forward notices and **no Register line names
   §18.5 at all**, while §31.2.2's correction nine lines later is registered at 1787. Docket 23, and
   the missing-entry class of dockets 2 and 3.

9. **Three count words with nothing behind them (16g-09).** *the eight polynomial relations* —
   `eight polynomial` has one site in six volumes and the eight are never listed, so the companion
   *Gröbner basis of 18* is uncheckable; the paired *the original four gave 6* is EXACT under lex on
   eight variables (grevlex gives 5, so the convention must be stated). *18 of 18 containments at
   orders 1–3* — no printed convention reaches 18; 3 points × 3 orders = 9. Docket 10.

10. **Bracket widths not reproducible (16g-10).** L8625's *6.9 × 10⁻⁴ (L1), 3.6 × 10⁻⁹ (L3)* against
    measured third-difference spans L1 3.55e−4 … 5.70e−3 and L3 3.46e−7 … 3.82e−7. The L3 figure is
    two orders below the smallest measured value. Neither grid nor convention is printed. Docket 10,
    17.

11. **§11.7 cites itself by number (incidental, outside the unit).** L2260: *§11.7 measures 89,864
    join failures when one is tried*, inside §11.7. A section pointing at itself for its own
    measurement. Docket 9.

12. **Six unbibliographed attributions (incidental).** Roche, Titius, Bode, Regge, Hagedorn and
    Gröbner, one main-volume site each, absent from `## References` at its BODY occurrence L11503
    and from R.7 L11806. Mardling & Aarseth, Poincaré, Lagrange, Euler, Hill, Rydberg and Sperner
    are all bibliographed — seven of thirteen resolve. Docket 36.

13. **Prints & Proofs offsets over this unit are −82, −85 and −88** — a single global offset
    mis-anchors the string sections by six lines. Anchor every witness on its own text.
## Chat 119 — deferred out of the unit main L8700–L8789 (§31.3 – §31.3.4)

1. **A count word its own volume contradicts (16j-01).** L8783 *The 24 excluded values* over the
   twelve it then lists — 102, 103, 115, 117 and 119–126. MEASURED: 12 values, 24 cells,
   232 − 208 = 24. **L11070 prints *less twelve exclusions* for the same slice.** Repair one of
   the two sites, and they must move together. Docket 21, 14.

2. **A criterion cited and departed from (16j-02).** L8716–L8717 *By §16.7.1's test the absence is
   removable — not by re-coordinatising but by re-constructing — so it is a defect of the index.*
   §16.7.1 read in full L4578–L4617: the discriminator printed there is re-coordinatisation
   (L4593, L4614–L4615), under which an absence surviving every re-coordinatisation is a feature
   of the world. Repair must move either the inference or the criterion. Docket 12, 9(b).

3. **A pointer whose target carries none of the claim (16j-03).** L8785 attributes to §10 a
   structural/accidental distinction and a normal-form behaviour. §10 swept over its whole span
   L2021–L2074: zero sites for *structural*, *accidental* or *normal form*. Locate the claim's
   real home before repairing — §16.7.1 and §6.2 are the candidates. Docket 9(b).

4. **One work, two author lists (16j-04).** Text L8732 *Candelas, de la Ossa, He & Szendroi*;
   bibliography L11804 *Candelas, P., de la Ossa, X. & Rodriguez-Villegas, F.* One entry is for a
   different paper. This is why Szendroi scores unbibliographed. Docket 16, 36.

5. **An unanchored ordinal (16j-05).** L8755 *The fourth falsification test*. §32.6 prints three
   conditions; L10280 and L11072 and register 387 all print *three*. Two readings survive and
   neither is printed. Record both; do not assert falsity. Docket 21, 33.

6. **Stale sub-numbering, and it is authoring (16j-06).** L8738, L8755, L8777 print 24.3.4.1–3
   inside §31.3.4. §24.3.4 does not exist; §24.3 is L6668. Not markdown headings. The **only**
   three lines in the main volume whose N.N.N.N number disagrees with its enclosing chapter, and
   the only 24.3.4.x sites in six volumes. **Present in PP at P8650 — authoring, not production.**
   Repair to 31.3.4.1–3 as `####`. Docket 31, 28, 32.

7. **Ruling 45, three sites (16j-07).** L8729 *this session could not read*, L8757 *The file is
   missing*, L8788 *a file, and an afternoon*. The same register recurs at L11076. Docket 5.

8. **Klemm unbibliographed (16j-08).** L8715, one main site, absent from `## References` L11503
   and R.7 L11806 and from the other five volumes. Kreuzer and Skarke both resolve at L11797.
   Docket 36.

9. **Two closure conventions in one line (incidental).** L8736's 498 + 498 are one-step failures;
   its 540 is the fixed-point closure. Both exact; neither convention printed. One clause fixes it,
   and R3 should add it, because a reader recomputing one step gets 534. Docket 34.

10. **An unfalsifiable falsification row (incidental).** L8765–L8766's thin-tip row: the slice's
    minimum sum is 26, so nothing could ever land below 22. True, and not a test. Docket 19.

11. **§31.3 carries zero body lines** — alone among the parent sections of chapters 30–31
    (§30.4 five, §31.1 two, §31.2 one). Consistency, not a gap. Docket 1's weakest form.

12. **Reverse-direction bibliography claim (incidental).** L11801 says Huang & Taylor's counts are
    *used in §31.3.1*; §31.3.1 attributes them to nobody. R3's docket-36 sweep runs both ways.

13. **Prints & Proofs offset over this unit is a uniform −88** on eight independent anchors —
    unlike chat 118's −82/−85/−88 across 125 lines. Still anchor per witness.

## Chat 120 --- deferred out of the unit main L8790-L8888 (ch.32 head, 32.1, 32.1.1)

1. **16m-01** joins docket 15 and docket 14's internal form: the self-index's boxes (1,681 and 861)
   are computed on 41 units; the volume carries 43 (36 chapters, 7 appendices).  R3 must recompute
   the whole table or date it explicitly.  The densities are exact on the printed boxes.
2. **16m-02** joins docket 33 (cited by one enumeration, printed under another): *seven things* over
   ten bolded flag items, three of them ordinals the count word does not reach.  32.1.2's heading
   anchors *the seven* to the numbered list.
3. **16m-03** joins docket 34: 162/400 = 40.5 printed as 40 per cent (truncation) on the same line
   as 58/138 = 42.03 printed as 42 (half-up).  Two conventions, one sentence.
4. **16m-04** joins docket 9(b): three parked questions attributed to chapters 15 and 17, which
   carry none of the three under a full-span sweep with three loosened probes each.  Antiprotonic
   helium's real home is 16.4's worked apparatus case at L4419.
5. **16m-05** joins docket 9(b) and 12: 16.4 cited for an ordering-and-inheritance form it does not
   carry; its own subject is D2 and disjoint routes.
6. **16m-06** joins docket 23 and 35: the chapter head cites Appendix E at eight items where the
   appendix now carries fourteen with ten open, and itself records three live counts at L10923.
7. **16m-07** joins docket 10 and 17: *three hundred and sixty-eight withdrawals* against a measured
   54 entries and 83 stem occurrences in the Register; *roughly thirty-seven from a single late
   session* is unmeasurable there.  R3 must name the object counted.
8. **16m-08** joins docket 36's reverse direction: L11555 and L11799 both cite 32.2 for a listing of
   unobtained works that 32.2 does not carry.
9. **16m-09** joins docket 6: `bookindex.py` at L8816, the first Ruling 46 site since chat 111, and
   absent from Prints & Proofs.
10. **16m-10** joins docket 5: eight Ruling 45 sites in 99 lines --- L8792, L8816, L8819, L8826,
    L8827, L8841, L8842, L8872.  The Ruling 45 class now stands at **seventy-seven members**.
11. **Out of unit, for the class record:** first-person prose at L4415 (*I wrote*), found while
    reading 16.4 in full; docket 5's pronoun sub-sweep must cover chapter 16.
12. **Open thread carried to chat 121:** 32.6 at L9205 prints *The three conditions are tested
    here* while 31.3.4 L8755 names *the fourth falsification test*; 32.6 L9220 records a FAILED
    check and a chapter written as 31 against a contents list that read 21.  Read against the
    contents list as it now stands.

## Chat 121 --- deferred out of the unit main L8889-L9029 (32.1.2 - 32.1.4.1)

1. **16o-01 joins the stale-self-measurement class opened by 16m-01.** An S3 baseline computed over
   twenty-five chapters where the volume carries 36. R3 must recompute the multiple (9.53x, not
   6.5x) and note that the stale figure understates the result. Sweep every denominator the book
   takes from its own size.
2. **16o-02 joins the arithmetic-convention class (docket 34).** Two of three rows of the 32.1.3
   table sum to 98, which three rounded percentages of a partition cannot reach. The third sums to
   99 and is rounding-consistent. R3 recovers the true column values or restates the rows.
3. **16o-03 joins the count-word class (docket 33).** *Six indices* over a table naming five, and
   *only two closed* over three under the fibred reading and one under the section's own honest-
   number rule. Both readings recorded; the repair needs the author's choice of rule, and the choice
   is between two defensible repairs of a defect, not a question about whether the defect exists.
4. **16o-04 joins docket 30.** *The register is a quarter of it* against 35.8 % by lines and 60.8 %
   by bytes. A page-count basis is unmeasurable in this container; R3 measures it at press (G0aa)
   before choosing the repair.
5. **16o-05 joins docket 14 and docket 15.** *The two companion papers* at L8945 and L11853 against
   *the third companion paper* at L1338 and L9001. R3 fixes the count once across all four sites.
6. **16o-06 is the third member of 16m-05's shape (16j-02, 16m-05, 16o-06) and joins docket 9(b).**
   22.4 cited for a closing result about language; 22.4 read whole under both resolvers is the price
   of limit-freedom. *no language for* has one site in the volume --- L8994 itself --- so the claim
   has no home to point at and R3 must either write one or drop the attribution.
7. **16o-07 joins docket 26 and docket 14.** The corrupt sentence at L8908-L8912: a duplicated
   clause, an E(Q) clause with no number, and an E(Appendix D) figure that reads against 32.1.4's own
   table. In PP at offset -94, so production loss is excluded. R3 repairs the sentence before it
   repairs the figure.
8. **16o-08 joins docket 33 and docket 15.** The audit set at nineteen (L8992-93), twenty (L8949)
   and twenty-two (four sites, L79, L1004, L1399, L9824). The unit's two are coherent past states
   carrying no state marker, inside a section arguing that figures about the book are true of a
   state. R3 marks them rather than restating them.
9. **Carried for R3's 7.4 pass (incidental, not a defect of this unit).** 7.4 names four cap
   coordinates where the enlargement table uses five, and cites a twenty-eight-fold range in cell
   count where 32.1.2's own table spans 511-fold.
10. **Ruling 45 grows by twelve** (L8909, 8911, 8912, 8915, 8919, 8949, 8958, 8998, 9001, 9002,
    9004, 9024), all present in PP. The class now stands at eighty-nine members. Chapter 32 remains
    the densest measured region, and chat 115's discriminator must be applied to the whole standing
    list before any of it is repaired.
11. **Ruling 46 adds nothing:** zero sites in 141 lines, swept case-sensitively for .py, BUILD<n>,
    MANIFEST, .tsv and .md.
12. **Docket 27's clean run reaches fifteen consecutive units:** 95 long lines swept, none recur.

## Chat 122 --- deferred out of the unit main L9030-L9156 (32.2 - 32.4.2)

1. **16q-01 joins docket 33 and docket 14, and is the class's first CROSS-VOLUME member with the
   Register on the wrong side.** *Nine of nine move* over a seven-row table and *Six of six
   identities hold* over a five-row table, both repeated verbatim in register 394's headline, whose
   own body enumerates five identities and eight values. Six is reachable only by splitting *closed
   under join and meet*; nine is reachable from no reading of either volume. R3 must fix the count
   once across main L9135, main L9147 and reg L1465 --- and decide whether the tables lost rows or
   the count words were written to an earlier table, since the Register's eight values sit between
   the table's seven and the printed nine.
2. **16q-02 joins docket 30 and docket 14.** L9055 makes 1,635 a count of measured levels that
   failed; chapter 28's own head (L7367) makes it the count of the book's own wrong claims, and
   L7372 says the entries are not printed there at all. Fourteen of the fifteen word-form sites are
   the register's size. R3 repairs the referent and the verb together.
3. **16q-03 joins docket 9(a).** *Chapter 28 names three documents and one section that could not
   be reached*: an eleven-token sweep over chapter 28's whole span returns zero, and 29.6 is
   literally *The three documents we could not reach*. A one-word repair, 28 to 29, but it must be
   made in the same pass as item 4 because both sit in the same sentence at L9057.
4. **16q-04 joins docket 9(b) and is the fourth member of 16m-05's shape** (16j-02, 16m-05, 16o-06,
   16q-04). *Chapter 29 names the single open item* against chapter 29 naming six that remain open
   (L7911-L7914) and adding a seventh at L8105. *single open* has one site in the volume --- the
   citing line. R3 either writes the single item or restates the sentence to the six.
5. **16q-05 joins docket 9(b).** 18 cited for *no differences, no sums, no symmetric bounds*;
   *symmetric bounds* has zero sites inside 18's span and its home is 12.11.2 L3364, which names
   chapter 17 for the other two. The adjacent clause already cites 12.11, so the cheapest repair is
   to move the triple to that clause.
6. **16q-06 joins docket 36.** Knaster and Tarski invoked as authority at L9107-L9108 and absent
   from the References body occurrence, while register 279's headline names Knaster. R3 adds the
   entry when it sweeps the six volumes against References and R.7.
7. **Ruling 46 adds one: `rclose.py` at L9107, absent from PP.** The class stands at nineteen
   main-volume sites. Two consecutive units have now added a site that is not original, which is a
   change from chats 111-119 and should be watched as the chapter-32 self-audit region continues.
8. **Ruling 45 grows by twelve** (L9036, L9041, L9045, L9050, L9057, L9065, L9083, L9108, L9120,
   L9136, L9147, L9148), all present in PP. The class now stands at one hundred and one members.
   Chapter 32 remains the densest measured region. L9065 (*an earlier draft of this section got it
   wrong*) is also a docket 15 member.
9. **Docket 28 adds two rows to the formatting pass:** the recursion table's level-3 row carries no
   label where levels 0-2 are named, and neither 32.4.2 table carries a rule between header and
   body.
10. **Carried as an incidental, not a defect.** The fourth printed identity (rank modularity) is
    entailed by the third under the book's own rank convention, so it is not an independent test
    although it is printed in the same voice and with the same *tested by pairs* qualifier. If R3
    touches the identities table it should say so.
11. **Docket 17 adds 2,873** (L9107): one site in six volumes, draw-dependent, and not reproducible
    without the original sampler --- the same experiment at seed 122 gives 2,955 of 3,000. The three
    new cap-setting figures 19,109, 35,789 and 2,742 are also one-site but were recomputed exactly,
    so under chat 115's refinement they are not single-witness.
12. **Docket 27's clean run reaches sixteen consecutive units:** 45 long lines swept, none recur.


## Chat 123 --- deferred out of the unit main L9157-L9306 (32.5 - 32.6.1)

1. **Docket 1 gains a citing site.** §32.6.1 L9281 cites **§14.5.6** for the *outside · dishonest*
   pair and ℛ₄'s refusal. §14.5.6 is heading-only in BUILD90 (L3806 heading, L3807 blank) and in
   Prints & Proofs (P3772-P3775). The pair's home is **register 573**, which prints it verbatim.
   R3 authors §14.5.6 to what already cites it, or repoints L9281 at register 573.

2. **Docket 9(b) gains two members.** §32.5.3 L9193 cites §16.5 for *every claim supported, cited,
   or marked open*; §16.5 read whole (L4449-L4470) states totality as χ_Λ total on the ambient box,
   verified on all 6,912 points, and carries none of those three words. §32.6.1 L9281's §14.5.6 is
   the second. **Docket 9(c) gains a citing site:** register **571**, cited at L9274 inside
   *Registers 571-573* and absent from the Register (main L7719 is the first citing site).

3. **Docket 14 gains two cross-volume members.** (a) *All 1,061* at L9188 as a count of brackets:
   1,061 is the perturbation-bound count (main L6517 supersedes *§25.5's 1,061 order-1 bounds*;
   L6683, L6958, L9354, L10266 all read it that way), while Appendix B prints the bracket at
   **1,105 of 1,105** at its head and **1,577 of 1,738 cells across 392 rows** at §B.2. Register
   6487 already ruled on 1,105 in Figure 25.1's caption. (b) *four indices* at L9268 and L9302 over
   the five terms printed at L9270, with register **396** carrying the identical *across the four*
   over the same five terms. Neither the four-reading nor the five-reading closes: the four-reading
   breaks L9286's *the other three*.

4. **Docket 35 gains a member.** §32.5 L9165's *all 153 channels* re-asserts Appendix B's head
   figure, which Appendix B itself (L10203-L10208) records as overtaken and which §B.2 replaces with
   596 rows / 2,269 interior cells, matching the spectra arbiter's L900. 15n-07 had already named
   this figure superseded; L9165 is a new re-assertion site.

5. **A stale self-measurement, and the check it belongs to still passes.** §32.6 L9219's *figures
   embedded / captions 18 / 18*: the volume now carries **33 embeds, 33 distinct tags, 0 unpaired**.
   R3 restates the row; the test's verdict does not change.

6. **A count word its own table refutes.** §32.6 L9239 / L9262's *thirty-nine claims … each has been
   given one*, against a table showing 7 bare before repair and 3 after — four repairs. The same
   paragraph says the 54 %-89 % move happened *before a single repair was made*. R3 reconciles the
   prose to the table or the table to the prose; both cannot stand.

7. **§32.6.1's ten open items against §E.1.4's eleven.** L9294 gives 8 + 1 (no measurement) + 1
   (unbounded) = 10; §E.1.4 L10989 gives 8 retrievable + 1 nonexistent + 2 buildable = 11; §E.1.2's
   heading says *ten open of 14*. The eight agree, the residue does not.

8. **A backwards range.** §32.5 L9158's *§32.1-24.4*: §24.4 is (6688, 6699), §32.1 is (8801, 8808),
   and chapter 32 has no §32.4.4 — its self-audit run ends at §32.4.2 (9120, 9157).

9. **Docket 28 gains a member, measured outside the unit by the unit's own test.** Chapters **20 and
   21** are the only two of thirty-six whose contents entries are plain body lines (L138-L139) rather
   than `## N.` headings. A heading-based contents scan sees 34 of 36. Adjacent: §31.3.4's
   sub-headings are numbered **24.3.4.1 / 24.3.4.2 / 24.3.4.3** at L8738, L8755, L8777.

10. **Docket 19 gains a member.** L9304's *are not open items and never will be* — a universal over
    all future states of the index, where §E.1.4 L10998-L11001 names the extension (a fourth obstacle
    value, box 18 to 24 cells, E from 4 to 10) under which they would become expressible. Census row
    1193, disposed **defect**.

11. **16j-05 CLOSED as a finding, chat 123.** §31.3.4 L8755's *fourth falsification test* is the
    fourth of §32.6's three conditions plus its own. The enumeration exists and is printed 450 lines
    later; no enumeration precedes the ordinal. Forward reference, not a phantom. R3 either numbers
    the tests where they are first run or drops the ordinal.

12. **Owed to r2lib, added to the standing list.** An **appendix body-occurrence resolver** (the
    volume heads appendices `## Appendix X --- …`, twice: contents L110-L175 and body) and a
    **lettered-pointer resolver** `§([A-Z]\.\d+(?:\.\d+)*)`. `heading_line` is numeric-only and
    returns None for §E.1.4, which the volume heads at L10986. Both carried with provenance comments
    in r2-ch16q/r.

13. **Instrument cautions earned this chat.** A line-anchored caption regex misses a caption form —
    pair each embed against a following window instead. `\b(I|my|we|our)\b` matches the Roman numeral
    in *He I*. A literal `Sc VI` probe scores zero in the Spectra Compendium, which carries Sc rows
    at L800-L810: a literal-string probe is not a species test.

14. **Ruling 45, twelve further sites**, all present in PP: L9168, 9169, 9172, 9226, 9235, 9236,
    9237, 9239, 9240, 9242, 9244, 9261, 9262, 9265, 9269, 9271, 9272 (seventeen in 150 lines).
    **Ruling 46, one further main-volume site:** L9169 *this book's own markdown*.
## Chat 124 --- deferred out of the unit main L9307-L9392 (32.7)

1. **Docket 9(a) gains a member.** §32.7 **L9356** cites **§24.2** for *the four unreachable
   documents*. §24.2 (L6653-L6667, both resolvers coinciding) is *The largest contributors*, a
   species / core / channels / cells table carrying zero occurrences of *document*, *reach*,
   *unreachable*, *Edlén*, *Ritz*, *Paschen* or *Dunz*. The home is **§29.6** (L8029-L8040), which
   carries all of them. R3 repoints L9356.

2. **Docket 33 gains a member, and it is a THREE-SITE tangle.** §29.6's heading (L8029) reads
   *The three documents we could not reach*; its table lists **four** data rows (L8034-L8037:
   Edlén 1964, Ritz 1908, Paschen & Götze 1922, Dunz 1911). The unit's L9356 says **four**,
   agreeing with the table against the heading. Chat 122's L9057 (*Chapter 28 names three
   documents … that could not be reached*, zero sweep hits in Chapter 28) is the third site.
   R3 settles the count once and propagates it to the heading, to L9057 and to L9356.

3. **Docket 19 gains a member.** L9318's *Five worked cases, **all from this book's own record***.
   Four trace (§32.3 L9049, §32.3 L9050, L7419, L7404); the fifth — L9326's *projections offered as
   a closure criterion | 22 of 60 | closure is d-dimensional* — has `22 of 60` at **L9326 only**
   across six volumes, no loose 22…60 pairing, and *closure criterion* nowhere else. Adjacent to
   docket 2, the §18.4.1 one-dimensional refinement.

4. **Docket 17 gains two members.** **-0.00128** and **-0.00159** (L9323) have one site each in six
   volumes, the summary table itself; §32.3 L9050 tells the case in words and prints no figures.

5. **Docket 28 gains two members and one adjacent.** L9338 (*On the word "unprecedented"*) and
   L9367 (*And the form, which is the stronger claim*) are plain body lines reading as sub-headings
   — neither markdown headings nor bold — both present in PP at -94. Adjacent, measured outside the
   unit: the principles table header is **shattered mid-word at main L243-L244** (*principle
   expression wher* / *e*).

6. **Docket 15 gains L9311** (*An earlier draft called this the class of error no automated test
   will find, and left it there*). **Ruling 45 (docket 5): nine candidate sites in 86 lines** —
   L9311, 9318, 9335, 9342, 9344, 9352, 9358, 9364, 9370 — of which only L9311 and L9364 are
   unambiguous; the rest are *this book* / *the author* self-reference awaiting chat 115's
   discriminator. **Ruling 46 (docket 6): zero sites in the unit.**

7. **A citation-form inconsistency, new.** The book numbers its principles **P1-P23 with P10, P12
   and P18 unassigned** (L233). The phrase *Principle N* occurs **twice in six volumes, both as
   *Principle 8*** (L7947, L9316); no other numbered principle is ever written that way. L9316's
   referent is **exact** — L666 prints *P8 says any true answer, good or bad, is a bound* — so this
   is a form repair, not a pointer repair, and it partially clears 15l-03 for this site.

8. **Docket 30, two measurements that settle rather than extend it.** The Register carries **1,635
   numeral headings (1,628 bare + 7 grouped)** and **1,660 distinct entry numbers**, maximum 1792:
   the printed 1,635 is the heading count and the 1,660 is the distinct-number count, so both
   figures are right about different objects. And the unit's three word-form sites (L9364, L9376,
   L9381) are on the book's **canonical** referent, fixed by L202, L7367 and L7900 as *withdrawn
   claims*; chat 122's L9055 remains the single outlier.

9. **A retired-basis datum from Prints & Proofs, not a defect.** PP prints **one thousand one
   hundred and seventy-one** at P9270 and P9282 where the volume prints *one thousand six hundred
   and thirty-five* at L9364 and L9376. This is why those two witnesses fail an exact match; read
   at -94 they are the same sentences, giving sixteen for sixteen at a uniform offset.

10. **Docket 11 closed to a population.** *4ν/3* is **24 sites across all six volumes**,
    emphasis-normalised: main 22, mc 1, sc 1. The carried figure was right but unpopulated.

11. **Instrument caution earned this chat, and it is about a resolver.** `section_span` runs to the
    next **numbered** heading and steps over a `# PART N` divider: for §32.7 it returns (9307,
    **9399**) against `body_range`'s (9307, **9393**), overshooting into Part VII and Chapter 33.
    **A section that ends a Part cannot be bounded by `section_span`.** HANDOFF-76 predicted the two
    would coincide; they do not, and the unit was bounded by `body_range`.

12. **A handoff omission, re-measured.** HANDOFF-76's chapter-33 heading list omits **§33.5
    (L9477)**. Measured heading lines: §33.1 L9404, §33.2 L9427, §33.3 L9440, §33.4 L9455,
    **§33.5 L9477**, `## 34.` body L9494.

## Chat 125 --- deferred out of the unit main L9393-L9493 (PART VII divider, ch.33 head, 33.1-33.5)

1. **Docket 23 gains its sharpest member, and the Register supplies the repair text.** §33.3
   **L9449** cites *Chapter 27's terms* for *an index closes when its cells are enumerable, and what
   it cannot supply is exactly what requires an operator*. Chapter 27 is *Slack* (L7203-L7365, both
   resolvers coinciding) and carries **zero** occurrences of *enumerable*, *operator*, *index
   closes* or *cannot supply*. **Register 1755 (reg L6491) diagnosed this exact sentence**: its
   verbatim home is register 1327, and in the current numbering it is printed in Chapter 33, not 27.
   §35.1 was repaired accordingly and **L9729 now reads "Chapter 33 said"**. L9449 is the unrepaired
   twin, and it sits inside Chapter 33 citing another chapter for its own sentence. R3 repoints
   L9449 to the form §35.1 already carries.

2. **Docket 9(a) gains a member in the same three-line passage.** **L9451**'s *the indexes of §36*:
   §36 resolves to `## 36. Three bodies, and what a complete index is allowed to say` (L9892-L9938,
   47 lines), carrying **0** `Λ_`, **0** *expectation*, **0** *eleven*. The volume's own index
   (L11434) fixes §36 as *three bodies*. The claim's homes are **register 1327 (reg L4981)**,
   **mc L3659-L3662** (*The observability boundary*) and **ioi L1656-L1658**, all three in the unit's
   own words. Both stale pointers sit within three lines of each other and register 1755 names a
   renumbering as the cause of the first.

3. **Docket 15 gains a superseded denominator carried at three sites.** Register **1327** says
   *eleven closed indexes*; register **1347** (reg L5061), later and governing, says ***TWELVE CLOSED
   INDEXES*** and names all twelve (Λ · Λ_law · Λ_const · Λ_var · Λ_ryd · Λ_charge · Λ_cross ·
   Λ_descent · Λ_phys · Λ_amp · Λ_PCA · Λ_chem). *Nine of eleven* stands unmarked at **main L9451,
   mc L3660 and ioi L1656**. R3 settles the population once and propagates to all three volumes.
   The nine itself is not in question; only the denominator and the marker.

4. **Docket 14 gains a roster contradiction, and the outlier is not the unit.** §33.1's six
   languages (L9414-L9421, 6 DATA rows, count word exact) are **order, analysis, algebra, geometry,
   information, statistics**. §20.2 (L5573-L5574) prints a different six — **order, geometry,
   arithmetic, calculus, logic and the constraint language of §16** — sharing **two** names, and
   §33.1 opens by citing Chapter 20 for the principle. Chapter 1 carries two further five-row
   populations (L400-L406 mechanisms; L455-L460 closure operators) under L453's *all five languages*
   and L439's *five … and the sixth*. **MEASURED across the Index of Indices, the unit's roster is
   the operative one**: order 31, statistics 11, analysis 7, information 7, algebra 5, geometry 5
   sites, against *calculus* **0** and *logic* **1**. R3 repairs §20.2, not §33.1.

5. **Docket 9(b) gains a mis-ordinalled criterion.** **L9486** calls *Never fit across a language
   boundary* **the fourth question of the domain protocol**. Register **1336** (reg L5017) read in
   full: *Four questions before any fit: which single cell of Λ_phys · which carrier does Λ_law
   assign · points ≥ 3× parameters IN THIS CELL · **am I pooling***. The language boundary is not
   among the four; the phrase has two sites outside the unit in six volumes (reg L6275, pc L852),
   neither the protocol. **Docket 19 adjacent:** *the one that blocks the most* is unmeasurable
   against the protocol's own replay, which attributes its three BLOCKED outcomes to carriers,
   pooling and domain cells.

6. **Dockets 26 and 27 gain a three-times-printed clause.** **L9489-L9492** closes §33.5 with the
   Löwdin challenge epigraph; **L9496-L9498** opens Chapter 34 with the same sentence to a
   **126-character common prefix**, diverging only at *This **part*** / *This **chapter***; and
   **L9395-L9397** (the Part VII epigraph) carries the same closing clause a third time. **Register
   1359 (reg L5105)** fixes §33's five sections as ending at *what it cost to learn* and §34 as
   carrying *the challenge, the method and the solution entire* — the epigraph belongs to §34, which
   already has it. It is the **only** long unit line recurring outside the unit, 1 of 46.

7. **Docket 36 gains two.** Measured against the `## References` **body** occurrence
   (L11503-L11855, R.7 at L11806): **Schrödinger** (L9490) — 5 main, 6 reg, 2 pc, 1 ioi sites,
   **none inside the References body**; **Demkov-Ostrovsky** (L9468) — 1 main, 5 reg sites, **none
   inside the References body**, though the Register treats the pair substantively at reg L5449,
   L5453 and L6083. Löwdin passes at L11809 and L11810.

8. **Docket 5, and the density is down.** **Ruling 45: five candidate sites in 101 lines** —
   L9396, L9401, L9479, L9485, L9491 — of which **L9401, L9479 and L9485** are unambiguous
   (*it was not designed; it was noticed*, *was arrived at after the failure it explains*, *it is
   enforced in code*). Against §32.7's nine in 86 lines, chapter 32 remains the densest region
   measured. **Ruling 46 (docket 6): zero sites in the unit**, measured case-sensitively and
   word-bounded — the instructive contrast being that register 1336 does name `domain_protocol.py`,
   which is permitted in the Register and would not be in a reader-facing volume.

9. **A Prints & Proofs datum, and it is NOT a defect.** PP anchors at **-94** and the unit is **74
   for 74**: 69 body lines verbatim, and the five section headings present but **unnumbered** there
   (`### Where it came from` at P9310 against the volume's `### 33.1 Where it came from`). Section
   numbering is a production layer. **Zero unit lines are genuinely absent from PP.** Recorded
   because a whole-line comparison reports five phantom absences, which is exactly the instrument
   fault this chat caught.

10. **Docket 34 gains a convention that must be named before a figure can be scored.** §20.2's *ten
    of their combinations hold* over six languages: C(6,2) = 15, so *ten* is not a pair count over
    six and the claim needs its combination convention named before R3 can score it. Out of unit,
    in the chapter the unit cites.

11. **Docket 33 adjacent, out of unit.** The language-bounds claim is assigned to **P2** at L366 and
    headed **P20 — the language bounds the question** at L396, while §20.1 L5559 attributes it to
    P20. Same shape as chat 124's *Principle 8* finding, at a different object.

12. **Instrument cautions earned this chat, all three from self-caught faults.** (a) A roster or list
    that wraps across two lines must be read on the **whitespace-normalised join**, never on one
    line — the §20.2 parse returned three names of six. (b) **A heading absent from Prints & Proofs
    at its offset is not absent from PP**: the volume numbers its section headings and PP does not,
    so the test compares the heading's **title**, not its whole line. (c) An unmarked-sub-heading
    test must require a **blank line above**, or it catches the wrap tails of italic sentences and
    reports sub-headings that do not exist.

13. **Counter-case worth carrying against chat 124's resolver caution.** `body_range` and
    `section_span` **COINCIDE at five of five** here. The §32.7 divergence was caused by the section
    ending a Part, not by the resolvers disagreeing in general. Resolve under both, always; say so
    when they coincide.


## Chat 126 --- deferred out of the unit main L9494-L9608 (ch.34 head + epigraph, 34.1-34.4)

1. **A new docket item: a count read from a population that cannot contain it.** §34.1 **L9504**
   and §34.4 **L9592** both read the subshell opening order from *the 108 neutrals*. The printed
   sequence at **L9507** ends in **7p**. Deriving each opening's Z from that sequence and the unit's
   own capacity rule 2(2ℓ+1) puts **7p at Z = 113**. The derivation is validated on the book's own
   anchors, returning **5d at Z = 57** and **6d at Z = 89** exactly as L9509-L9510 print them. The
   chapter fixes its domain at Z <= 108 at four sites (L9504, L9592, **§34.9 L9663** *Z = 3 to 108*,
   **§35.2 L9746** *Z = 2-108*), and 106 and 107 are exact for those two ranges. **Present in Prints
   & Proofs unchanged (P9410, P9413), so authored, not produced.** R3 either lifts the population to
   the sequence or drops the sequence's last member; the two figures *seventeen of nineteen* and
   *89%* both move with it, so this repairs as one item, not three.

2. **Docket 34 gains a member where the convention decides between exact and false.** L9511's
   *Seventeen of nineteen openings agree; two do not*, against a Madelung order **generated** (n+l,
   then n) rather than recited: **position by position 15 of 19**, **longest common subsequence 17
   of 19**. The printed **89%** at L9514 and L9605 discriminates: 17/19 quantizes HALF_UP to 89,
   15/19 to 79. R3 names the convention -- displacement, not position -- and the figure stands.

3. **Docket 14 gains a main-volume/compendium contradiction the compendium wins.** Main **L9537**
   and its table L9539-L9546 place **eleven** variables on (body, role); the Index of Indices entry
   `## Λ_var — the variables` at **ioi L1598** says **twelve**, and its singleton rule at ioi
   L1609-L1612 turns on *both δ and n\* present*. **n\* is absent from the main-volume table**, so
   as printed the main volume cannot support the compendium's rule. E = 0, the body order and the
   empty nucleus+rydberg cell are all corroborated exactly (ioi L1599, L1869). R3 adds n\* to the
   main table rather than reducing the ioi, since the ioi's singleton rule depends on it.

4. **Docket 12 gains a definition that its own apposition contradicts.** L9524-L9525 (restated
   L9593): *The radicand is the count of states below: complete lower shells of the same ℓ...*
   MEASURED over n = 2..7, l = 0..3: n - l - 1 equals the number of complete lower subshells of the
   same l in every case and the number of **states** below in **none** of the 18 non-trivial cases,
   the two differing by the factor 2(2l+1). The apposition is exact; the head is not. No clash with
   the node-count reading at L9587/L9593, radial nodes being n - l - 1 as well.

5. **Docket 19 gains a false universal against the section it cites.** **L9596**: *the provenance of
   every term is §34.8's table*. §34.8 (L9649-L9660), read in full, carries five rows: n - l - 1,
   2(2l+1), l(l+1), the energy of a single state, the endpoints. **The occupancy q has no row and
   zero occurrences in the section** -- and q is the term §34.1 argues for at L9527-L9530. Also
   here: **L9576's *has never been traced***, which the census's own row 1195 flags and which no
   sweep can settle; the sweep covered *isotopic* at 1 main site, 6 reg, 3 ioi, 1 pc, 0 mc, 0 sc.

6. **Docket 16 gains a bibliography date contradiction.** **L9600** prints *Janet (1929)*;
   **References L11777** prints *Janet, C. (**1928**)*. The year 1929 has **zero** sites in the
   References body (L11503-L11855). Madelung is exact on both sides, L9599 (1936) against L11815.

7. **Docket 31/33 gains a count word that names one thing twice.** **L9523**: *Both Pauli quantities
   appear*, followed by exactly **one** distinct quantity, 2(2l+1), in two roles -- as the unit's own
   L9594 says: *antisymmetry the capacity 2(2l+1), **twice***.

8. **Docket 36 gains Klechkovskii.** Named at **L9600** as one of the three owners of the n+l rule;
   **absent from the References body**, where the other two, Madelung and Janet, both appear. Pauli
   (L9523, L9527, L9587) is the same shape, used adjectivally. Schrödinger at L9497 is chat 125's
   16v-07 at the epigraph's other copy and is not counted twice.

9. **Docket 5 gains five candidates, one unambiguous.** L9516, L9580, **L9593**, L9599, L9601.
   Under chat 115's discriminator only **L9593** -- *§34.10 gives the session that did it* -- names
   the work's own making; L9599 and L9601 are priority claims, which the class allows; L9516 and
   L9580 locate a statement inside the finished text. **The Ruling 45 class now stands at one
   hundred and thirty-three unambiguous-or-candidate members** counting L9593 alone from this unit.

10. **Docket 26 -- evidence, not a new member. Chat 125's 16v-06 must be re-read before it is
    repaired.** Prints & Proofs carries **both** epigraph copies, at **P9396-P9398** (Part frame:
    *This part states what the method delivered, what it cost...*) and **P9402-P9404** (chapter
    frame: *This chapter states the challenge...*). They are a Part frame and a chapter frame sharing
    a 126-character prefix, **present in the original and therefore not a splice**. The R3 repair is
    a rewording of the shared opening, not a deletion of one copy.

11. **A PP delta that is itself a docket 5 member.** The volume's offset against PP shifts from
    **-94** at L9511 to **-96** at L9532. The aligned diff of main L9512-L9531 against PP
    L9418-L9435 returns exactly one change: the volume adds *The rule that names the order exactly
    is stated, derived and attributed at §34.4; what follows here is the reading that found its
    shape.* at **L9515-L9516**. The clause about *the reading* is post-PP.

12. **Flagged for chat 127, not assumed.** §34.6 **L9624-L9626** prints **eighteen** resets as
    **8 subshell openings + 6 aufbau exceptions + 4 returns**; 8 + 6 + 4 = 18 is exact, but **8
    subshell openings** sits against the sequence's **19 openings** at L9507. Test it at §34.6
    against the population, and test **L9685's *the domain protocol blocked four fits*** against
    register 1336's own replay, which records three BLOCKED and two PASS.

13. **Not a defect, recorded so it is not re-opened.** **L9605's *Chapter 35 and the paper***:
    References **L11816** bibliographs *Lach, M. (2026). The Löwdin Solution. — the companion
    paper*, and **L11807** says the companion paper carries the full list. The reference resolves.

## Chat 127 --- deferred out of the unit main L9609-L9715 (34.5 - 34.10; closes Chapter 34)

1. **A new docket item at chapter scale: the volume prints a result the Register withdrew, with no
   marker anywhere in the volume.** §34.9 L9663 *Exceptionless on 106 elements*, §34.8 L9659 *No
   parameter is fitted*, and ν as *the law* throughout §34.5-§34.10 (and §34.4 L9580, chat 126's
   unit); Chapter 35 L9718 *Chapter 34 stated the law that names the order*; Appendix L10850-L10856
   lists the corridor, the nineteen surds, a_cross and the necessity of state as verified. Register
   1350 restates the unit and its WARNING withdraws it at 1460; 1437/1438 measure 99 of 106 in sample
   (Mn Tc Ce Gd Pa Cm Rf missed); 1445 measures 90 held out against Madelung's 96 and says the
   standing *should be quoted that way until it is not*; 1460 deactivates ν as a law and lists the
   nineteen surds, the corridor bounds, the recorded a values and the 99/90/72 as demoting with it.
   Main-volume sites for 1445, 1457, 1458, 1460, *held out* (in chs 34-35), *90 of 106*,
   *deactivated*, *retained as a form*: ZERO. W440 flagged §34 stale before R2 and named a
   superseding CHAPTER-LOWDIN.md that was never seated (Fishburn, additive representability: 0 main
   sites). **R3 repairs this as one item, not eleven**: the chapter's status sentence is 1445's and
   1460's, and the appendix rows and Chapter 35's opening move with it. Dockets 35, 14, 23.

2. **Docket 35/34 gains the reset count.** §34.6 L9624 *resets eighteen times* (8 + 6 + 4) is
   register 1328's node-only-form count; 1402 calls the eighteen *a property of one trajectory*
   (ten to thirty-three); 1403/1411/1413 ten; 1409/1438 fifteen; §34.10 L9697-L9700 in the same unit
   says the eighteen-on-surds result was withdrawn. Reconstruction: 10 (node-only) and 15 (finished
   form), never 18.

3. **Docket 14/34 gains the form mismatch inside the chapter.** §34.5's endpoints Δn(√p_g+√p_r)/
   (p_g−p_r) and *Nineteen distinct surds* are the node-only form's (1309); §34.4 L9580 declares the
   q/2(2ℓ+1) form for §34.5-§34.7, under which the endpoint is Δn/(√(p_g+q_g/c_g) − √(p_r+q_r/c_r))
   and the distinct endpoints number 121-138 (nineteen reproduces only node-only at generator
   n ≤ 8, 17 at n ≤ 7 -- name the generator).

4. **An arithmetic error at three sites.** L9620, register 1330 L4993, MC L3595: (√5+√2)/3 =
   1.2167605 printed 1.2168450; (√6+√3)/3 = 1.3938469 printed 1.3938270; all three say *four exact
   hits*. Exact at 4 dp. One repair, three sites, and the appendix row L10852 restates the formula.

5. **Docket 19 gains a false universal in the mathematics.** L9666 *At any f opening p = n−ℓ−1 = 0*:
   5f has p = 1. The one-sided corridor at Pa follows from admissibility (every smaller-n rival
   full), not from the node floor; register 1350 repeats the error, register 1403 calls Pa's floor
   *degenerate at zero*. Conclusion stands, reason fails at one of two openings.

6. **Docket 34 gains the entry-point figures.** L9641 *1.028 at p across four subshells and 1.785 at
   d across two … √3 to 0.19%* are MEDIANS of register 1337's values (means: 1.040, ratio 1.7153,
   0.97% BELOW √3); no site names the convention; register 1336's own rule calls a median across
   cells a pooled fit in disguise. L9645-L9647 then quotes the Λ_t p row (finished form, register
   1354, ioi L1759) as the same object; Λ_t's d row gives ratio 1.570.

7. **Docket 31/33 gains two count words.** L9685 *blocked four fits* over a body naming three
   (register 1336: three BLOCKED, two PASS; register 1355 holds the fourth, unnamed here). L9702-L9706
   *One object, six appearances* counts 1/(2ℓ+1) as ℓ(ℓ+1); they are never equal at integer ℓ, and
   register 1340 keeps them as two objects (five and two).

8. **Docket 20 gains the four prior recordings.** L9702-L9703 names the gate, the collapse switch,
   the barrier and Seaton's ratio as prior recordings of ℓ(ℓ+1); each has ONE main-volume site,
   L9703 itself (Seaton: reg 33, mc 28, pc 14, main 1). **Docket 36 gains Seaton** (unbibliographed;
   Pauli L9617 and Schrödinger L9643 recur in this unit and are already listed).

9. **Docket 5 gains a first-person site: L9700 *the trajectory was mine*.** The class probe must
   include *mine* (chat 126's did not); out-of-unit *mine* sites main L25, L5865, L10771 are for their
   own units. Ruling 45 candidates L9675, L9681, L9687, L9698, L9702 are recorded for the chat-115
   split, not counted into the 133: §34.10's declared subject is the session.

10. **16x-01 disposed: NOT A DEFECT as stated (later line governs).** Register 1306 L4897: Lr =
    [Rn]5f¹⁴7s²7p, so 7p opens at Z = 103 inside the 108. Chat 126's Z = 113 came from complete
    sequential filling of the printed sequence, which the same arithmetic puts wrong at 4f (67
    against the printed 58) and 5f (99 against 91); its two anchors are the two openings where
    filling is complete. **DEF-126 item 1's repair must not be executed**; *seventeen of nineteen*
    and *89%* stand under 16x-02's convention. The chat-126 instrument r2-ch16w carries the
    derivation; its golden is not changed (G0c) -- the finding is recorded here.

11. **Prints & Proofs datum for chat 126's unit.** PP P9482 `### The rule` is heading-only and P9484
    is already `### The corridor`: the volume's §34.4 body L9580-L9607 is post-PP prose (offset −96
    → −125). 16x-05 (L9596) and 16x-06 (L9600) are post-PP authoring; *ν byte-identical at both
    printings* has one PP witness. The unit L9609-L9715 itself is in PP unchanged except the clause
    *— Chapter 36 takes this up* at L9712 and one `---`; PP ends Part VII at §34.10 and has no
    Chapter 35 or 36.

12. **Budget items, not negatives.** (a) The memoryless *104 of 106* does not reproduce under the
    corridor-non-empty convention (62/79 node-only, 71/85 finished); the record's convention *that
    subshell's own crossing value* is not reconstructible; register 1448 calls a self-consistency
    test of this shape vacuous -- R3 reads 1332 and 1448 together. (b) INFERRED: register 1463's
    fourteen emptying points reproduce only under the node-only form (finished form: eleven), so the
    record's walk figures may never have been re-taken under the q/cap form after 1348.

13. **Functions owed to r2lib, unchanged plus one:** body_range, htitle, joins, lettered_heading, an
    appendix body-occurrence resolver, a lettered-pointer resolver, numsites, regentry, an 8-tuple
    transfer factorisation, a meet-characterisation join-irreducible counter, the space-aligned table
    parser -- and now **a first-person probe carrying *mine* and *myself***, and **a NIST
    ground-configuration table with its validation block** (r2-ch16y §3), which any later walk
    instrument must import rather than retype.

14. **Not a defect, recorded so it is not re-opened.** Census rows 1196-1198 (C9) are live universals
    that measure true in the record and in both reconstructions (CENSUS-CLOSURES-ch16z.tsv). The
    Chapter 36 pointer at L9712 resolves (body L9892). Backticked `a` at five sites is docket 28
    formatting only.

## Chat 128 --- deferred out of the unit main L9716-L9805 (ch.35 head + epigraph, 35.1-35.3) and Segment A (held)

1. **The withdrawn-law class is HELD (RUL-128 item 2).** `r3-wl.py` + `r3-wl.out` specify the repair on BUILD90
   exactly (BUILD91 would be 1,984,829 B, md5 2e5e442b...; main shift +8 for L >= 9608; kinds 1,567 / corrections
   151; extent 1 to 1794 at main L7373, Register L6, L65). R3 executes it after docket 37's re-take, with
   `--write`; if the re-take moves 99/90, the SUBS change and the instrument is re-banked under a new name.
   New class site: L9792 *the corridor's law* (add to R3-CLASS-WL's table). Pre-existing states the dry run
   measured, none repaired: build.py's Register SUBS carry five dead anchors (`*The Build 16 column...`,
   `Build 9, 2026-08-26. **1629 entries, 1 to 1786**`, `*A REBUILD --- see PROVENANCE.md.*`, ``**`QUEUE.md`
   required this...``, `*Removed: `.zeno`...`) -- the Register press would assert-fail at BUILD90 (docket 28 /
   press); census.py L50 hard-codes `n>1792` (read the extent from Register L6 when census.py is next revised);
   gate.py's MAIN default names the BUILD90 path (pass `--main` after BUILD91); the load-bearing table L35-L49
   is stale at BUILD90 (571 vs 593 cited; 1649 9x vs 10; 1526 absent) and L6's *165 to 1791, 1,470 entries*
   disagrees with L65's *165-1792* (docket 30).

2. **Docket 34 gains two.** 17a-01: L9749-L9750 holds only with clause 1 under first-occupation and clause 2
   under never-occupied-rival; per step the exceptions are 1437's ten (S = Mo Rh Pd Au | La Gd Ac Th Cm Lr);
   name the convention. 17a-03: 0.058 - 0.083 = -0.025 Ha; the clearance is false under the plain reading,
   undecidable per row (REQUEST-LOWDIN item 10).

3. **Docket 14/35 gains 17a-02.** *every element with a measured ground configuration* Z = 2-108 (L9746) against
   register 1446 (edge 102; 103-108 listed, not measured); register 1712 repeats the 108 edge inside the
   record. Chat 129 reads 1446 before scoring §35.5's *unwitnessed* rows and §35.6.

4. **Docket 19 gains 17a-04**: 16z-05's universal at L9786-L9788 (5f: p = 1). Class member with L9666.

5. **Docket 9(c) / 30 gains register 1710** -- named only by the range *1701-1712* at five sites in four volumes
   (main L9723, L11807; mc L3150; pc L194; ioi L1900); and **1725 absent** (front matter L10, L68 name it).

6. **Docket 36 gains Schrödinger's L9721, L9775** (already listed from chat 125).

7. **The Löwdin chain is record-carried.** No member reproduces 107 of 107, the 106/107 scorer, Λ_chain,
   Λ_cinf, the collapse criterion, the g depths' counts, 1705's second order, 1707-1711's audit, or 1712's
   margins; REQUEST-LOWDIN.md asks for each by claim. The same for Chapter 36 (REQUEST-THREEBODY.md: tb_audit.py,
   3B.tri, N8, the mass-uniformity check, the stratification data). Intake protocol in RUL-128 item 4.

8. **Chat 129's unit, §35.4-§35.6 L9806-L9891 (86 lines), carries:** §E.5's *nine things* (count at §E.5's body);
   *the twenty-two audits* L9824 against §3 (docket 33); attributions Pulay / Griffin / Andrew / Cowan
   (References body 1 / 2 / 3 / 4, R.7 1 / 2 / 2 / 2, MEASURED in r2-ch17b); L9866-L9867 restating eleven
   elements and twelve rows; L9870 *No parameter is fitted. No observation enters upstream of the score* -- the
   derivation's own claim, a different object from §34.8's (not a 16z-01 site); *unwitnessed* against 1446.

9. **Functions owed to r2lib, plus two:** body_range (again), and **`rbody(n)`** (the Register entry body is the
   first non-blank line after `### N`, never `R[i+1]`) and `span_hits` (pattern hits inside a section_span).

10. **Not a defect, recorded so it is not re-opened.** 107 rows / 106 transitions are consistent under
    row/step (convention unnamed, C.3); L9797's *two coexisting solutions* is 1703's *two stationary
    solutions*; PP's `# APPENDICES` body is P9590 (own scan), not P9591.


## Chat 129 --- deferred out of the unit main L9806-L9891 (§35.4-§35.6, Chapter 35 closed), Segment A (the archive split) and the intake check

1. **Docket 34 gains 17c-01.** L9827 *nine things* (also main L68, L4051) against §E.5's ledger L11147-L11183: eleven
   left-column DATA rows under its own totals line L11185 *Nine components, nine precedents*; §30.3 has ten
   sub-headings. No printed convention yields nine. R3 names the convention or corrects the count at all sites
   (kin of docket 33's 16z-08).

2. **Docket 14/35 gains 17c-02** -- L9867 *twelve unwitnessed rows … past the last measurement* is 17a-02's second
   site (12 under 1712's edge at 108; 18 under 1446's edge at 102). Repair with 17a-02, one convention.

3. **Docket 5 gains §35.4's thirteen Ruling 45 tokens** (session L9823; instrument L9810, L9820; ruling L9830, L9853;
   review L9854; archive L9822; nightly L9825; hash/file L9813; ledger L9829, L9846; protocol L9812; collaborator
   L9851). The section's declared subject is the method's own run; chat 115's split decides them with §34.10's.

4. **Wording pairs, not counts:** L9824 *outside the work* vs L79 *outside the book*; L9865 *five close rows* vs
   1705 *five contested rows*. Docket 34's wording class; no figure moves.

5. **Production, out of unit:** §E.5 L11165-L11168 typesets the step-law row's right column as a broken four-line
   fraction. Docket 28 / press.

6. **The archive split is executed (chat-127 item 5).** ARCHIVE1 (5a5c0829…, 394 members) holds the 48 legacy
   handoffs, r2-ch12*-r2-ch15* instruments and goldens, READ/CENSUS-CLOSURES-ch12*-15*; `archive-split.py
   --verify-archive PATH` checks it on demand; its members are not extracted at the gate. Any R3 item that needs
   an archived instrument (docket 37's re-take may need r2-ch14l/14m from BUILD124) fetches ARCHIVE1 by title.

7. **Intake pending (RUL-128 item 4).** Deliveries arrived as zips at Materials root, not in the subfolders (which
   hold retired files): LOWDIN-DELIVERY-1-part1.zip 632f911b… (README.md, ground.py, MANIFEST.tsv, ground-run.log)
   and THREEBODY-DELIVERY-1.zip f30a60d2… (20 members). Chat 130 opens with intake: unzip into /home/claude/intake,
   read both READMEs and MANIFESTs first, run each instrument under timeout, a validation block against the
   Register's anchors per object, a golden, a Register entry per object seated only through a guarded build.
   `-part1` implies further Löwdin parts.

8. **Functions owed to r2lib, plus one:** body_range and rbody (again), and a lettered heading resolver
   (`§[A-Z].N`, exact token, last hit = body) -- r2-ch17c carries `lettered()`.

9. **Not a defect, recorded so it is not re-opened.** §2.14's body says *computed before the sentence describing
   it is written*; the maxim *state the number before the interpretation* is the book's paraphrase at L29, L7668,
   L9810. L9870 is the derivation's own claim, not a 16z-01 site. The four refusals are enumerated at L50-L55.
   *prediction file* wraps L9812-L9813 (read on the join).


## Chat 130 --- deferred out of the intake (Segment A) and the unit main L9892-L9936 (Chapter 36 closed)

1. **Docket 9(c)/6 gains 17e-01.** L9902 cites `tb_audit.py` (1756); **1756 is ABSENT** (1755, 1758 exist; no Register
   line contains `tb_audit`). The companion member cites the same at its L146; REQUEST-THREEBODY.md item 1 carried it.
   The delivery names the file `audit.py`. R3: point the citation at 1717 (the 78/78) or seat the drafted 1796, and
   remove the script name under Ruling 46 — one repair, three sites (main, companion, request).

2. **Docket 9(b) gains 17e-02.** L9914 *§31.1.1 had already named the brackets: zero-velocity surfaces, Hill regions,
   KAM tori* — §31.1.1 carries Hill only; the sentence is §18.4.1 L5155-L5156 (*Jacobi's zero-velocity surfaces, Hill
   spheres and KAM tori*). R3: re-point to §18.4.1; docket 34 wording pair *Hill regions* / *Hill spheres*.

3. **Docket 36 gains Xia** (L9930 *Xia 1992*, the only site in six volumes; no References-body or R.7 line) **and
   Routh** (the threshold 0.0385209 printed at main L8642, L9918 and PC L332 without its author anywhere). Names in R.7
   but absent from the References body L11503-L11805: Saari, Painlevé, Brudno, Montgomery, Chenciner, Jacobi,
   Maupertuis (the body/R.7 convention of 17c B2 applies).

4. **Docket 34 wording, no figure moves:** L9902 *eight closed* / 1721 *seven closed to named owners* / L9922 *Seven
   belonged to others; the eighth … classical* (eight = seven + Lagrange 1770). **Docket 17:** L9908 *a fourth open
   object outside the book's own five* — the three earlier outside objects are named nowhere in main. **C3:** L9898
   credits *envelope precision only* to §12.11.2; the sentence is §18.4.1 L5152-L5155.

5. **Docket 37 (reconstruction-versus-record) gains intake1-01 and intake1-04.** (i) The delivered `cases` dict: 13
   labels, 12 distinct weak orderings (x<z<y at both (1,3,2) and (1,3,2.5)); z<x<y untested — passes all six checks
   when appended. (ii) The reconstructed withdrawn polynomial's constant term (S₂²−S₄)² − 64u₁²u₂²u₃² also differs from
   the norm's (p²−4q)²: three degrees differ where the record names two and prints only the U⁴ term. Both are findings
   about the reconstruction (no original instrument exists); flagged to the three-body project through M; the book's
   78/78 and *two coefficients* stand as printed.

6. **Docket 38 (record-carried) after the intake.** Löwdin: only object 3 is instrumented; 1701-1712 and every Chapter
   35 figure remain record-carried pending LOWDIN-HANDOFF-103.tgz (objects 1, 2, 4-8, 10), packs 93-103 (9), and M's
   copies (12); object 11 and the S104 part of 9 are NOT HELD (the delivery's own finding, FOUNDATIONAL). Three-body:
   objects 1-4, 7, 9 reproduced from labelled reconstructions; 5 by reading; 6 and 8 NOT HELD; 10's PDF
   (151Yg3WgY-aqx24jrlHdvtPK8a-rNgMKL, 340,837 B per README) not fetched — md5 it when the paper is next opened.
   R3 draft entries 1795-1798 are in READ-intake1.md §C, unseated. The five PNGs in the project knowledge (59,166 /
   40,235 / 38,598 / 61,552 / 27,036 B) may be the session's originals — INFERRED; ask nothing, compare when the
   three-body project next reports.

7. **Delivery form (for the next request):** `caps_table.log`'s sixth column is wall-clock — not bankable; logs must be
   deterministic. Deliveries arrive as zips; the small one inline (quoted heredoc + md5 assert), the large one as a
   spill file. Text members enter under a prefix with bytes unchanged; PNGs stay on Drive.

8. **Functions owed to r2lib, unchanged:** body_range, rbody, lettered (r2-ch17c). r2-ch17e imports r2-tb1 by path for
   the closure figures — the intake goldens are now upstream of an R2 instrument.

9. **Not a defect, recorded so it is not re-opened.** Census 1199 (*at every cap*: measured at all ten) and 1200 (*a grid
   the book never ran*: 90,705 has one main site). L7000 (§25.6) is a post-PP forward pointer to Chapter 36, 1714's
   text. *six numbers* (L9926) counts three scalars and three rays as objects. The chapter's R45 tokens (register,
   audit, rerun, run, ledger) describe the method's own run on the problem — docket 5, chat 115's split.

10. **After Chapter 36:** the main volume's chapters are all read; next are the appendices under chat-127 item 1
    (Appendices D-G as data), A-C and E-G as prose, the Index and References — then RUL-128 item 3's order.
## Chat 131 --- deferred out of the unit main L9939-L10053 (Appendix A part 1: opener, A.3, A.8-A.13)

1. **Docket 9(a) gains 18a-01.** The Appendix A index row L9950 sends `A.6 adjunction never repairs closure` to **§24.2, in full**;
   §24.2 (L6653-L6667) is *The largest contributors*, a species/cells table — 0 hits for adjunction/adjoin/repair/closure. The
   claim is **§17.2 L4806, Theorem 17.1 (adjunction never repairs)**; Appendix D L10558 names Theorem 17.1 as A.6. With 13l-03
   (A.7 → §16.3): two misdirected rows of nine. R3: re-point both rows (§17.2 and §15.3); C1/ch13n's *other eight resolve* is
   corrected to *seven resolve* (A.1, A.2, A.4, A.5, A.14, A.16, A.17 measured, r2-ch18a §2).

2. **Docket 9(a) gains 18a-02 as 14h-05's twin site.** A.12 Consequence L10035 = §22.3 L6135 word for word, both pointing the
   antiprotonic-helium cells at §25.6 (0 sites); the cells are at §2.8 L612, §16.4, §19.2 L5401/L5416, §32 L8793. One target
   chosen by M under 14h-05, applied at two sites — with 14h-02 (L6133 / L10035, *all require I*): the two Consequence sentences move
   together.

3. **Docket 12 / 34 gains 18a-03.** A.13 Statement L10038-L10041 *fails iff |ΔT| > 2Z²R/ν³* against its own proof's *to leading
   order* (L10043): the smaller one-sided gap is 0.775 × 2Z²R/ν³ at ν = 5.3 (4,567 vs 5,897 cm⁻¹), 0.656 at ν = 3, 0.811 at 6.6
   (Decimal HALF_UP, R = 109,737.316). R3 wording: *to leading order* into the Statement, or *iff* → *when*; the Inversion's bound
   inherits the caveat. Not a figure move: ν_fail 6.6 / 4.2 and ν = 5.3 reproduce.

4. **Docket 34 wording:** A.10 L10008 *leaves 2S and g* — g has degree 2 in the constraint tree (q, f); the factorisation holds
   with g innermost. **Docket 19:** L10051 *The two conditions are anticorrelated in nature* — no population in the unit; §25.6
   sites L6839, L6950. **Docket 17:** *no channel in this work enters the failure regime* rests on the §25.6 table alone.

5. **Standing at their appendix sites, re-measured:** 13l-01 (A.8: may-precede a total PREORDER — antisymmetry fails on 19 of 28
   pair projections of Λ₈; sufficiency 914/914); 13l-03 (A.7 → §16.3, 0 / §15.3, 3); 13t-04 and 13t-05 (A.11's 86: 9,894
   comparable / 384 covering decreases under δ = f − ℓ; not 86); 14h-02 (A.12 Consequence); 12a-01 (*24 of 70* has no site).
   The single-witness counts 120 / 274 of 274 (L4302, L9981), 47 comparable pairs (L2017, L9996), eight random intervals (L2071,
   L10013) have no Register site: docket 17.

6. **Post-PP changes recorded (not defects):** the opener's count (PP *Ten … seven … seventeen*; volume 9 + 10 = 19 exact);
   **A.9's proof replaced** — PP's *decomposes as a direct product with a chain factor* is not true of a general non-antichain
   interval; the volume's crosscut argument reproduces on 200/200 seeded pairs. Rota 1964 is in the References body L11664; absent
   from R.7 and the Register (docket 36: nothing owed).

7. **Functions owed to r2lib, unchanged:** body_range, rbody, lettered (now in r2-ch18a from r2-ch17e).

8. **Next unit:** Appendix A part 2, `### A.15` L10054 to `## Appendix B` L10165 (111 lines: A.15, A.18, A.19, A.19.0, A.19.1),
   under the same protocol; A.15's 12,654 / 12,489 (DEF chat-70 carry) and A.19's seventeen generators against r2-ch18a's 17
   join-irreducibles. Then Appendices B and C as prose, D-G as data (chat-127 item 1), the Index and References under docket 36.

## Chat 132 --- deferred out of the unit main L10054-L10164 (Appendix A part 2: A.15, A.18, A.19, A.19.0, A.19.1; Appendix A closed)

1. **Docket 9(b) gains 19a-01.** A.15 Remark L10071 cites Register 230 for *the ledger, which called C a join-closed sublattice*;
   230's body is Appendix D's kind coordinate (no WARNING). The phrase *join-closed sublattice* exists only at L10069; *join-closed*
   in the Register only at 1716; none of the ten *sublattice* entries (56-60, 78, 440, 441, 449, 471) nor the band entries names C or
   B_k. The corrected ledger text is not in the books and no entry records the correction. R3: locate or re-point; with 18a-01 and
   13l-03, Appendix A's third misdirected pointer.

2. **Docket 1 / 9(b) gains 19a-02.** §14.4 (L3729-L3731) is a heading and a colon-terminated lead-in (*Closure yields three
   properties, developed in the next three chapters:*) with no list — PP P3695 identical, so pre-PP. It is cited as the
   admissibility theorem for monotone single-coordinate bounds at main L2708, L3085, L3096, L3367, L5586, L10061 and MC L1254
   (seven sites, two volumes). The criterion lives at §7.2 L1765, §18.4.1 L5097 / L5121 and §29.12 L8267. R3: fill §14.4 or
   re-point the seven citers together, after the mathematics (RUL-128 item 1).

3. **Docket 5 gains** five Ruling 45 candidates in the unit: L10069 *This corrects the ledger*, L10155 *register 208 spent an entry
   on*, L10111 *what the book had not supplied*, L10162 *unique and unnamed until now*, L10094-L10095 *It never prints the seventeen
   ... left unwritten*; L10108 *Verified:* is the appendix's check form (as part 1). **Docket 34 wording:** L10148 *eleven ... one for
   each way chi's seven constraints bind at a value* is exact under the (constraint, value) reading (11) and reads as seven under
   the per-constraint reading. **Docket 17:** L10070 *what the tower relies on at axis 13 is B_1* — axis 13 sites L3153, L3168 name
   no band (single witness).

4. **DEF chat-70 carry CLOSED by measurement:** C (one-sided, |a − b| ≤ c) at cap 8 = 489 cells, 12,654 failing meets; T (two-sided
   triangle) at cap 8 = 369 cells, 12,489; same convention (unordered pairs, coordinates on [0, cap]); distinct regions; neither
   corrects the other. The convention reproduces every printed figure of A.15, A.18, §12.11.2 L3387, §29.12 U4 and MC L1254/L1260.

5. **Post-PP changes recorded (not defects):** *§3* → *§8* (L10087) and *§8.3* (L10092, L10109) — the volume's pointers resolve;
   A.19.1's property sentence (PP P9811) replaced by the measured one (8 of 8). The new split of T's failing meets by bound (upper
   954 / lower 1,908 at cap 6; 4,163 / 8,326 at cap 8; both 0) is an instrument datum, not a book figure.

6. **Functions owed to r2lib, unchanged:** body_range, rbody, lettered (now in r2-ch19a from r2-ch18a; rbody also in r2-ch19b).

7. **Next unit:** Appendix B, `## Appendix B` L10165 to `## Appendix C` L10230 (65 lines; heading lines to be re-taken), as prose
   under chat-127 item 1; then C (L10230-L10319) as prose, D-G as data, the Index and References under docket 36.

## Chat 133 --- deferred out of the unit main L10165-L10229 (Appendix B --- Data and provenance, B.1-B.4; Appendix B closed)

1. **Docket 35 / 23 gains 20a-01.** The opener L10169 prints *153 channels, 1105 interior cells, bracket 1105 of 1105* as the live headline;
   B.2 (L10195-L10202) states the collection as 596 rows / 2,269 cells / 1,577 of 1,738 (reproduced from the table), and Register 783 lists
   1,105 among four unreconciled figures (1,442 / 1,105 / 869 / 930) with the 100 % bracket never measured (796: 546 of 789). Eleven sites
   outside the unit carry 153 channels / 1,105 (L641, L1480, L2521, L3406, L6632, L6970, L8189, L8299, L9165, L10276, L10277). PP P9819 is
   the same line. R3: restate from the table after the mathematics; sweep the eleven sites with it.

2. **Docket 14 / 17 gains 20a-02.** L10171 *the 763 cells of the earlier verification ... the totals in Chapter 24 state the union*: 763 is
   nowhere a cell count (main L5676 parity column; Register 1829; IoI 1143 a tuple); Chapter 24 (L6623-L6883) has no 763 / union / earlier
   verification and L6970 gives 1,442 = 1,105 + 337. PP P9821 same. R3: with item 1, re-derive the union from the table and 783's split.

3. **Docket 35 / 19 gains 20a-03.** B.3 L10220 Si II 3s²np ²P° 0.272 has no row in the Part II table (Si II 3s2.np 2P* J=1/2 / J=3/2 at
   0.0878 / 0.0868); the σ(δ) > 0.25 population is four and the other four printed spreads reconcile at HALF_UP 3 places; *Every flag in
   this collection* (L10213) is false against the table. Register 1774 records the disagreement, restores the row from the witness, and
   leaves the flag's standing open. The 4ν/3 half of the criterion has no V column: BUDGET. R3 rules the row (the same block is SC L1005).

4. **Docket 5 / 6 / 15 gains** Ruling 46 sites L10204 (`spectra.py`), L10206 (*T8-J*); Ruling 45 candidates L10199 *ruling 26*, L10200
   *hash-verified captures*, L10203-L10208 (*This paragraph once read ... owed a rebuild ... disclosed rather than reconciled*).
   `COORDINATES-2.13` L10227 is the delivered file's reader-facing name (SC *The file*, Register 1727): not scored.

5. **Docket 34 wording:** the 392 bracket rows hold 1,748 interior cells against 1,738 bracket denominators (Ba II x2, Cd I, Cd II, S VI
   rows carry a denominator below interior) - the appendix's *1,577 of 1,738 cells* counts bracket cells, as it says; instrument datum for
   the Register WARNING sweep (RUL-128 item 3 ii). Register 905's *five of 49 species supply uncertainties* against B.4's *their stated
   uncertainties* as an input - wording.

6. **Post-PP changes recorded (not defects):** PART IV -> V (L10166); Chapters 13-14 -> 22-23 (L10224, targets moved with the text); KI ->
   K I (L10183); B.2 rewritten from the 133-row / spectra.py paragraph to the 596-row paragraph plus the italic retrospective; the
   COORDINATES sentence added (L10227-L10228); B.3's header un-split (Register 1774); PP's totals line P9849 dropped from B.2 but alive at
   L10169 (item 1).

7. **Functions owed to r2lib, unchanged:** body_range, rbody, lettered (now in r2-ch20a from r2-ch19a; rbody also in r2-ch20b).
   **Discipline:** chat 133's first turn hit its tool-call ceiling at its 46th call after banking; closed as failed with diagnosis and
   completed on *Continue* in the same container (W-173).

8. **Next unit:** Appendix C, `## Appendix C` L10230 to `## Appendix D` L10320 (90 lines; heading lines to be re-taken: C.1 L10236, C.2
   L10270, C.3 L10283, C.4 L10305), as prose under chat-127 item 1; then D-G as data, the Index and References under docket 36.

## Chat 134 --- deferred out of the unit main L10230-L10319 (Appendix C --- Margins, and what was recomputed, C.1-C.4; Appendix C closed)

1. **Docket 9(a) gains 21a-01.** *§24.2* cited at L10286 (twice) and L10303 for the rule-ablation costs, the Sr I figures and the Sc VI
   exclusion discussion; §24.2 *The largest contributors* L6653-L6667 carries none (both resolvers). Targets: §22.2.1 L6055 (ablation), §25.2 L6894
   (Sr I), L6910 (Ti I), L6914-L6917 (Sc VI, limit 892,700 +/- 400). PP P9933/P9950 identical. R3: retarget the three sites.

2. **Docket 15 / 20 gains 21a-02.** L10303 quotes §24.2 as stating *highest measured level is 5s at 696,400 cm-1*; `696[, ]?400` is absent
   outside the unit in six volumes; `highest measured` hits L6042 (Ritz) only. The arithmetic reproduces (r2-ch21a §4: limit 892,700 + R_inf ->
   delta 0.5139; delta 0.9812 -> 648,096). R3: retire the quotation or restore its source sentence.

3. **Docket 35 / 15 / 34 gains 21a-03.** L10299-L10301 *the book's single prediction ... §25.6's arithmetic was independently reproduced here ---
   735,091 against 735,092*: 735,091 is §25.6.4 L7064's *no* row, retired at L7066 (delta-bar 0.9934 exceeds delta(5s)); live is [735,860, 737,380] /
   736,688; 735,092 has no site anywhere. Wording: *single prediction* (one site) vs §25.6's title *not a prediction*. R3 with docket 37 (Sc VI chain).

4. **Docket 14 / 35 gains 21a-04.** 1,061 perturbation bounds live at L10251, L10266, L10277 (and L60, L6683, L6958 caption, L9188, L9354; Register
   L6487) while §23.10.4 L6517 *supersedes §25.5's 1,061 order-1 bounds* (34 bounds at 0.0164, 619 refusals). *tightest 1.40* = §25.5's 1.398. R3:
   settle the count in one direction after the mathematics.

5. **Docket 35 gains 21a-05** (20a-01's family): *1,442/1,442* at L10250, L10262 (absent elsewhere); Register 783 withdraws the 1,442 headline; §25.5
   L6970 *Of the 1,442, the 1,105* is the same class; B.2 states 1,577 of 1,738. L10276-L10277, L10288 are 20a-01/20a-02 sites, not re-scored.

6. **Docket 9(b) gains 21a-06.** L10287 *the multi-target failure counts of §16.3*: §16.3 L4359-L4378 (span L4407) has no *target* line; `multi-target`
   sites are L418, L7435, L10287 only; the counts' home is not located.

7. **Docket 15 / 35 gains 21a-07.** C.1 *chi_Lambda total --- 30,000 ambient points --- exact* and C.2 *on 30,000 uniformly sampled ambient points*
   after §16.5 L4454-L4457 and Register 248 retired the 30,000 sampling for the exhaustive 6,912 (no WARNING on 248); §3.3 L1242 and D.5.4 L10644 twin
   sites. R3: restate the statistic as the exhaustive count.

8. **Docket 30 gains 21a-08.** L10296 *one thousand six hundred and thirty-five errors* vs Chapter 28 L7373 *1,635 entries, 1 to 1792*; Register
   `### N` headings 1,628 (docket 30's 1,628 bare + 7 grouped); fourteen other main sites print 1,635. Wording pair errors / entries.

9. **Docket 23 candidate (out of unit):** §10.2 L2033 *seventeenfold range* and L2054 *2.17-fold spread* vs Figure 10.1's caption L2053 *hundredfold
   range*; the unit's *100x* follows the caption. **Docket 17:** *0.06%-4.4% median* and *coarse quotation* (L10254) no site in six volumes; *+0.35 at
   low l* (L10257) no prose site (SC L320 Ar I +0.3516, L429 Be I +0.3590 nearest).

10. **Docket 5 / 6 / 28 / 34:** R45 candidates L10270, L10271, L10284, L10290-L10292, L10295; R46 candidates L10291 (`figure.dpi`, f01-f18), L10306
    (Python 3, NumPy); C.1 is a whitespace table among 49 `|` rows in the appendices; wording *200 constructions* vs *200/200 covers*. **Docket 27:**
    twenty-eighth clean unit. **Docket 36:** nothing owed (Singer L11589). **Docket 11:** 32/11 site L10245.

11. **Post-PP changes recorded (not defects):** PART V -> VI title (L10231); Proposition 14.1 -> 23.1 (L10243, L10280); §32.3 -> §25.3 (L10262);
    Appendix C's tables / Part IV -> Appendix B's / Part V (L10272); 1,171 -> 1,635 (L10296). **Functions owed to r2lib, unchanged:** body_range,
    rbody, lettered (r2-ch21a; rbody also in r2-ch21b). **Discipline:** both goldens banked at the 31st call (budget 30th).

12. **Next unit:** Appendix D, `## Appendix D` L10320 to `## Appendix E` L10898 (578 lines; DATA under chat-127 item 1; heading lines to be
    re-taken), then E-G as data, the Index and References under docket 36.
## Chat 135 --- deferred out of the unit main L10320-L10461 (Appendix D part 1, D.1-D.4.4.3; split at `### D.5` L10462)

1. **Docket 34 / 14 gains 22a-01.** L10383 *ℛ recovers forty-eight bounds* vs *fifty-six* at L10416, L10421 and D.5.1 L10513; ℛ on Λ₈ = 56 ordered
   pairs (r2-ch22a §3); no convention gives 48. Register L1429 (385) and L5329 (1419) print forty-eight for other objects. PP P10030 identical. R3: 56.

2. **Docket 9(a) gains 22b-01.** L10353 *§16.7.1's diagnostic loop says a separating form in the excess means a missing constraint*: §16.7.1 L4578-L4618 carries
   none of loop / excess / separat under both resolvers; *diagnostic loop* and *separating form* have no other site in six volumes; PP P10000 cited §12 (post-PP
   retarget). R3: locate the loop by hand (Chapter 12 / 16) and retarget.

3. **Docket 34 gains 22a-02.** L10396 *976 of 976 — 100%* ties reproduce on the some-coordinate convention only (every-coordinate: 112); L10420 / L10513 *sixteen
   that constrain* = the 16 non-constant recovered bounds (sole-removal count is 7). Name the conventions.

4. **Carried to part 2 (L10462-L10897), unscored:** the serving line's *seventy-seven elements, twenty-four fibres* (L10321; sites L10496, L10508, L10863) and D.2's
   *thirty-two / sixteen of forty-two* (L10350; 42 = 7 x 6 reproduces) — the DATA table is D.5's; D.5.1 L10513-L10515 restates every ℛ figure of D.4.2-D.4.4.

5. **Post-PP changes recorded (not defects):** PART V -> VI (L10321); 32/16 -> 77/24 (L10321-L10322); §12 -> §16.7.1 (L10353); Figure 6.1 -> 11.1 (L10439).
   **Docket 11:** 4ν/3 site L10365. **Docket 27:** twenty-ninth clean unit. **Docket 36:** nothing owed (Nesterov-Nemirovskii in the References, L11653).
   **Functions owed to r2lib, unchanged:** body_range, rbody, lettered (both instruments). **Discipline:** goldens banked at the 29th call; two closure-file
   faults self-caught (rows closed before being read; a verdict set from a downstream site), each deleted in its own call and rewritten.

6. **Next unit:** Appendix D part 2, `### D.5` L10462 to `## Appendix E` L10898 (436 lines; DATA; 15 sub-headings D.5, D.5.1-D.5.10, D.6 — heading lines to be
   re-taken; split at a `### D.5.n` heading of your own scan only if the whole will not fit with the close), then E-G as data, the Index and References under docket 36.

## Chat 136 --- deferred out of the unit main L10462-L10897 (Appendix D part 2, D.5-D.6; Appendix D CLOSED)

1. **Docket 35 / 14 gains 23a-01.** L10644-L10645 *A.5 … proved · sampled, not proved · exhaustive* vs Register 222 (*now exhaustive*), 248 (every ambient point, 6,912), L10653-L10654's two cells and the E = 1 runs of D.5.6 / D.5.8 (reproduce only with A.5 exhaustive). R3: exhaustive; twin of 21a-07.
2. **Docket 23 / 35 gains 23a-02.** L10463 and L10526-L10527 *sixteen fibres* / *it prints sixteen* beside the 24-fibre, 77-element D.5 table; L10524-L10529 narrates the 27-row table in the present tense. Also L10350 (D.2, part 1) *thirty-two / sixteen* — the serving line was updated post-PP, D.2 was not.
3. **Docket 9(a) / 23 gains 23b-01.** L10546 §16.2 (no *closure operator*; heading *The split, and it is canonical*) vs L10567 §14.2 (*R is a closure operator*); PP P10180 / P10201 both §16.2. R3: §14.2.
4. **Docket 26 / 28 gains 23b-02.** L10500-L10502: *register 269* removed post-PP (PP P10119-P10121), leaving *which had to establish once* and *records that the table itself stayed wrong* subject-less.
5. **Docket 9(c) / 30 gains 23b-03.** Register 219, 220, 221 (L10501, L10530, L10658) and 305 (L10500) have no `### N` heading and no grouped heading; numerals appear only inside other entries. R3 reads the Register to establish whether they were merged into 222 or never written.
6. **Docket 36 gains Fourier and Motzkin** (L10867; absent from the References body). **Docket 5 / 6 gains** L10771 (*mine*), L10779, L10784, L10785 (first person), L10492 (*press … build*), L10723 (*The entry is kept*). **Docket 17:** *24 of 24* single site L10887. **Docket 11:** 4ν/3 sites L10571, L10640. **Docket 34 gains** L10880 (two of three box cells named). **Docket 37 gains 23a-03** (kind-only E = 2 → 1; D.5.9 E = 4 / 2 not reproduced under sixteen conventions; Register 233 / 1726 carry the record; the instrument is record-carried, docket 38).
7. **Owed re-probes (no finding recorded):** the pointers §12.11.0.1 / .0.2 / .0.5 / .0.6, §16.8.5, §30.3.3, §32.1.4 on their sections' own words (the element names are Appendix D's); the MC grade lines for 3B.five / 3B.pot at MC L3250 / L3268 (*PROVED with the check noted*, L10834); the 30 unprinted only-PP lines of the pre-PP diff (docket 27 clean-unit call is INFERRED from 12 of 42); r2-ch23b's 175 s (trim).
8. **Convention, one new:** a whitespace table row whose fibre column is long carries a 2-space gap before its last column (five rows: L10734, L10764, L10767, L10810, L10860) — parse the row on its own grammar, not the ≥ 3-space rule alone; print the rows the rule would drop.
9. **Post-PP changes recorded (not defects):** L10465 Chapter 16's → 18's two theorems; D.5 table 40 → 77; D.5.9-D.5.10 added; L10567 §16.2 → §14.2. **Functions owed to r2lib, unchanged:** rbody, body_range, lettered. **Discipline:** banked at the 34th / 43rd calls (budget 30th); one call timed out (re-issued).
10. **Next unit:** Appendix E, `## Appendix E` L10898 to `## Appendix F` (heading line to be re-taken; DATA under chat-127 item 1: Q indexed and closed — every item resolved to its site and its register); then F, G as data; the Index and References under docket 36; then RUL-128 item 3's order.

## Chat 137 --- deferred out of the unit main L10898-L11053 (Appendix E part 1, lead, E.1-E.1.5, E.2; split at `### E.3` L11054)

1. **Docket 35 / 14 gains 24a-01.** E.2 L11042 *518 at order 1, 34 at order 6* vs §23.10.4 L6509 *499*; 518 has no other main site. R3: 499, or the source's figure once §23.10 is re-taken under RUL-128 item 3.
2. **Docket 35 / 15 / 9(a) / 17 gains 24a-02.** E.2 L11048 *a Gröbner basis of eight … E(claim set) = 0. §29.8*: §29.8 has no Gröbner; §30.4.1 L8584-L8592 (basis 18 from eight relations; audit run once; nine non-polynomial relations never audited); §28.7.1 item 61 L7523. *E(claim set)* single witness. Gröbner not in the References body (docket 36, chat 118's item — twin site).
3. **Docket 9(b) / 17 gains 24a-03.** E.2 L11046 the accelerator identity *A^m(x^p) = (−1)^m x^p/(p−1)^m, m = 1…4; Richardson the exception* cited to §26.6 (Aitken on a Rydberg series only); the identity's other site is §30.4.1 L8589 (unaudited); Richardson at §29.7 L8051 / §36.6.
4. **Docket 9(a) gains 24b-01** (L11040 §23.11 → §23.12 L6550 / L6566; L11052 §16.7 → §16.8.4 L4721 / L4695) **and 24b-06** (L11023 *#P-complete (§29)* → §14.6 L4080 / §28.10 L8227 / F.4.3 L11762).
5. **Docket 28 / 32 / 9(c) gains 24b-02.** *E.4* cited at L10923, L10936; no `### E.4` heading; the heading text is an unmarked body line at main L11105 and PP P10618. R3: mark the heading (production layer). Part 2 reads L11105.
6. **Docket 9(c) / 30 gains 24b-03.** Register 239 (L10943) and 256 (L10962, L11014, L11018) have no `### N` and no grouped heading (numerals inside other entries only). 23b-03's family (219, 220, 221, 305). 256 holds the domain-assignment code E.1.5 describes: record-carried, docket 38.
7. **Docket 34 / 23 gains 24b-04** (lead L10905 *six times* post-PP vs E.1.1 L10922 *five times*; six lineage rows; lead *nine items* in no row) **and 24a-04** (E.1.4 L10989 *Eleven items: one nonexistent, two buildable, eight retrievable* vs ten open / 1 / 2 / 7; E.1.3 L10969 / L10978 the eleven-state in the present tense). 23a-02's class.
8. **Docket 9(a) / 23 gains 24b-05.** *F.3.1* at L10955, L10965, L10983 was *F.3.3* in PP (P10486, P10501, P10519); Register 371 names F.3.3; the volume has F.3 and F.3.1 only; F.3.1 carries no *nine stable cells* / *prose*. Resolve at the Appendix F read.
9. **Docket 37 / 38 / 34 gains 24a-05.** E.1.4 L10998-L10999 *E from 4 to 10* on the box 18 → 24: unreproducible under D.4.2's ℛ (an unoccupied value is covered by no φ; on the current ten ℛ·A E = 3 → 3); fourteen occupied cells from eleven items is impossible under a naive box count; the eleven-state coordinates are not printed. The record (256, 465, 1729) stands; the instrument is 256's code, not in the bundle. Resolve when E.3 prints K, M, N, O's coordinates, and at RUL-128 item 3 (ii).
10. **Docket 12 candidate:** 25.96 / 0.0164 = 1,582.93 at two-decimal inputs; *1,585-fold* printed at L11037 and §23.10.4 L6514 — the unrounded medians are not printed. Recorded, not scored.
11. **Docket 5 / 6:** L10940 *as this session leaves it* (R45, heading, pre-PP); *the code* L11014, L11016, L11021 (R46 candidates). **Docket 27:** thirty-first clean unit (MEASURED, all 34 only-PP lines read). **Docket 17:** *E(claim set) = 0* L11048; *518* L11042.
12. **Owed re-probes (no finding):** §12.11.3.1 and F.3.1 on their own words (*assert the law, compute the extent*; *a count … cannot be printed as prose*); §32.1.4 for ℛ(X) ⊆ ∏ Aᵢ(X) in symbols; E.1.5's *the mathematical fibre admits one cell* under 465's reading (needs N's coordinates); the thirteen-state E(Q) = 0 fibred / 1 unfibred (needs K, M, N, O — E.3).
13. **Conventions, two new:** a whitespace table row is parsed on a ≥ 2-space split when the ≥ 3-space split yields a different column count, and the difference is printed (generalises chat 136's long-fibre rule; the E.1.1 lineage row L10931 and the E.1.2 header / row N); a heading-form `E.n Title` line in PP without a blank line above is still a heading candidate and is read on its text (PP's E.1.1, E.1.3, E.4). **Functions owed to r2lib, unchanged:** rbody, body_range, lettered.
14. **Post-PP changes recorded (not defects):** the lead rewritten (PART V → PART VI — THE RECORD AND THE REACH; *nine* → *fourteen items*; *Amended by the tower* paragraph removed); E.1.2's domain column and *of 14*; lineage rows 3 (E and G → E and F), 5, 6; E.1.5 added (Register 1729). **Discipline:** banked at the 38th call (budget 30th); six faults self-caught.
15. **Next unit:** Appendix E part 2, `### E.3` L11054 to `## Appendix F` L11222 (168 lines, 7 headings: E.3, E.4.1, E.4.2, E.5, E.6, E.7, E.8 — heading lines to be re-taken; DATA); then F, G as data; the Index and References under docket 36; then RUL-128 item 3's order.

## Chat 138 --- deferred out of the unit main L11054-L11221 (Appendix E part 2, E.3-E.8; Appendix E CLOSED)

1. **Docket 34 / 23 / 33 gains 25a-01.** E.3 L11058-L11104 lists A B C D F G H I P; E.1.2 L10946-L10959 is open at A B C D F G H I P R; R (Register 1729, E.1.5) has no E.3 entry, against E.3's L11055 *the two must list the same items* and L11057 *audit 15 extended so the pair cannot drift again* (Register 384; audit 15's site §2.19.1 L970). PP P10477 / P10567 identical. R3: write R's E.3 entry from 1729; re-run the audit 384 describes.
2. **Docket 9(b) / 17 gains 25a-02.** E.4.1 L11133 *§32.2 asserted |Q| = 7*: §32.2 L9030-L9038 carries no Q, seven, assert; `|Q| = 7` has one site (E.4.1). Chapter 32's *seven* at L8809, L8830, L8872, L8889, L8930, L9093, L9199 — none a Q count. R3: locate the assertion (Register?) or retarget.
3. **Docket 23 / 35 gains 25a-03.** E.4.1 L11135 *the current thirteen is at E.1.2*, E.4.2 L11140 *holds at thirteen*: E.1.2 has 14 DATA rows; E.4.1's *E(Q) = 0 … 1 unfibred* is the thirteen-state (Register 256 / L10956), E.1.5 the fourteen-state. 23a-02 / 24a-04 class.
4. **Docket 9(a) gains 25b-01.** L11086-L11087 *§30.3.5 states the law, the procedure, and the residue — realisability*: §30.3.5 L8504-L8520 has procedure 1, law 0, residue 0, realisab 0; realisability at §30.3.8 L8552 / L8559.
5. **Docket 23 / 35 / 9(b) gains 25b-02.** E.7 L11209-L11210 *§2.10 … should have said, and now does: SEARCH BEFORE DERIVING*: §2.10 L623 still *Enumerate targets from the index before searching*; the phrase's sites are the front matter L70 and §35.4 L9827 only. R3 (prose, after the mathematics): either §2.10 gains the clause or E.7 drops *and now does*.
6. **Docket 34 / 12 gains 25b-03.** E.8 L11217 *Sixty-odd corrections come from §30.3 alone*: Chapter 28 L7619 *Seventeen from one question* + `### 28.7.4` L7644 *Forty more, from the session that closed §30.3 and §32.2* = 57; the forty are not §30.3's alone. Owed to R3: read §28.7.4's forty for their §30.3 share (a token probe found no numbered lines — not a reading).
7. **Docket 9(b) / 17 / 20 gains 25b-04.** L11066-L11067 item C's vocabulary at §29.7 (L8041-L8083): *excess width* L8054, *zero-error capacity* L8064 present; *Newton decrement* absent (sites §23.8.1-§23.8.3 L6336-L6368, D.4 L10365, G L11654); *partial identification* absent from the volume outside E.3 (single witness; absent-member candidate).
8. **Docket 17 / 20 gains 25b-05.** E.8 L11214 *Λ₉ passed six independent tests* — one site; §12.11.1 span L3032-L3363 names the axis *the target's multiplicity 2S′* (L3034), 0 × *target-spin* (sites §2.16.2 L761 / L769, E.8 L11213). Register 384 *the target-spin axis, answered at §12.11.1*. Re-measure notation-tolerantly before repair.
9. **Docket 15 / 35 / 9(d) candidate 25b-06 (INFERRED as a contradiction, MEASURED as sites).** E.6 L11190-L11199 (*This book has not read it … the claim "open" is a claim about this author's reading*) ↔ §30.3.9 L8572 (*§E.6 records that the complexity question may already be settled …*) — mutual citation for one open state; §30.3.8 L8549 *The language is NP-complete — … no Schaefer class covers it* and §29.8 L8096 (Stahl & Wille 1984, Yannakakis) state hardness results of their own. R3 reads §30.3.8-§30.3.9 with E.6 before touching either. Docket 36: nothing owed (Ryter, Schmid, Adams, Dwinger in the References body).
10. **Docket 9(a) / 23 gains a fourth 24b-05 site:** the grid row L11119 *the numbers index, nine stable cells* (no pointer; the eleven-state). **Docket 28 / 34:** L11219-L11220 *This chapter is where that is done* in an appendix (read on the join).
11. **Docket 37 / 38 / 34 — 24a-05 stays open (MEASURED):** K, M, N, O print no coordinates anywhere in E.3-E.8 (no item entry; no coordinate line); the thirteen-state (E(Q) = 0 fibred / 1 unfibred, Register 256 / 1729) and the eleven-state (E.1.3's *4 unfibred*, E.1.4's *4 → 10*) cannot be re-taken from the volume. The instrument is Register 256's code (not in the bundle); resolve at RUL-128 item 3 (ii). 465's *the mathematical fibre admits one cell* likewise waits on N's coordinates.
12. **Docket 10 candidate:** E.3 L11059 prints 91.338 eV (the eV of §25.6.3 L7045's point value 736,688 cm⁻¹ — reproduces by Decimal) beside the bracket [735,860, 737,380] without the point value; a reader cannot derive the eV from the page. **Docket 37 (Sc VI chain):** L11058 is a site of the 735,860 / 737,380 bracket (§25.6.1-§25.6.5, §32.5.1); 21a-03's 735,091 / 735,092 remain §25.6.4 / C.3's — a different figure.
13. **Docket 5:** L11057 *audit 15*, L11076 *this session could not reach*, L11099 *this session did not fetch*, L11197 *this author's reading*, L11213 *during this work* (R45 candidates). **Docket 6:** none. **Docket 27:** thirty-second clean unit (MEASURED, 21 of 21 only-PP lines read: one block, PP's E(G) 38 / 24 / 23 and *seventeen dominated, six not* paragraph citing Register 368, removed post-PP; Register 387 restates M at ten of eleven dominated). **Docket 17:** *partial identification* L11067, *six independent tests* L11214, `|Q| = 7` L11133, *Sixty-odd* L11217, *closed at d = 2* L11215 (d = 2 at §30.3 L8440 / L8452 / L8489 — resolves).
14. **Verified this unit, carried as counter-cases:** the grid's 8 / 1 / 2 of eleven (r2-ch25a §3); 13.5615-13.5895 nm and 91.338 eV (§4); 208 = 2·116 − 2·12, C(208,2) = 21,528, 26 / 262 as ℛ's closure ends (§5, §31.3.4 L8733-L8781); Λ₈ height 17 = Σ(|Aᵢ|−1), |J(Λ₈)| = 17, width 7 by exhaustive antichain search (§6); E.5's eleven ledger rows (17c-01's site, §8); E.2's eight paragraphs; §2.16.1's *four of them are one* = E.4's *they present one*; §24.9 L6800 for item P; *three quarters* in words at §30.3.4 L8497 (book right, instrument wrong: a numeral probe on a fraction printed as words); 384-387 with headings, no WARNING; census 715 / 716 / 1224 / 1225 not a defect.
15. **Conventions, two new:** a PP heading-form line may carry a leading space as well as lacking the blank line above — the heading probe is `^\s*(#{1,4}\s*)?E\.n\s+[A-Z]`; a section's rows may be question paragraphs (E.2) — a paragraph start is a non-blank line after a blank OR the line after the heading, fixed and printed before any count word. A fraction may be printed in words (*three quarters*) — probe both forms. **Functions owed to r2lib, unchanged:** rbody, body_range, lettered.
16. **Next unit:** Appendix F from `## Appendix F` L11222 (data; heading lines to be re-taken; measure and, if over ≈ 250 lines with the close, split at a `### F.n` heading before reading; 24b-05's F.3.3 → F.3.1 and 24b-06's F.4.3 / F.3.1 wording are its sites); then G as data; the Index and References under docket 36; then RUL-128 item 3's order.


## Chat 139 --- deferred out of the unit main L11222-L11360 (Appendix F, F.1-F.4.3; Appendix F CLOSED)

1. **Docket 9(b) / 23 gains 26a-01.** F.3 L11292-L11293 *Chapters 6, 12 and 24 state their central measurements to this standard*: F.3 is cited from §6.2.1 L1682, §12.11.1.1 L3179 / L3201, §22.1.1.1 L5984, E.1.5 L11024; Chapter 24 (L6623-L6884) carries 0 × F.3 / four columns / highest standard / refutation. R3: 24 → 22 (post-PP text).
2. **Docket 34 gains 26a-02 (a Register entry).** Register 1779 *the electron count Z − charge alone*: the file's charge column is the ionisation stage (SC L16 *1 for the neutral*; row (1, 1) *one electron*), so the count is Z − charge + 1. The claim holds (7,260 pairs, 120 electron counts, 0 exceptions, r2-ch26a §2). R3: a new entry citing 1779 with the convention corrected; F.2 L11266-L11269 needs no change.
3. **Docket 9(b) / 23 / 35 gains 26b-01 (24b-05 measured at its target).** E.1.2 L10955 and E.3 L11119 *nine stable cells, named at F.3.1*: the rebuilt F.3.1 L11301-L11327 names no cell, prints no *nine*; *cells* in the unit at L11242 / L11320 / L11355 only. The nine cells live in the Register (371 / 372 name the old F.3.3; 388 / 392 close item M). R3: E.1.2 / E.3 point at the Register entry, or F.3.1 names the cells.
4. **Docket 9(b) / 23 / 35 gains 26b-02.** §32.1.3 L8961 *§F.4.1's withdrawal ratio … Registers 320 and 321* and §32.1.4.1 L9023 *the ratios of F.4.1*: F.4.1 L11330-L11337 carries 0 × withdrawal ratio / method ratio (withdrawn as content L11332). Homes: Register 296 / 320 / 321 / 1762 (4.21 : 1). R3 (prose after the mathematics): cite the Register, or restore.
5. **Docket 23 / 35 / 12 gains 26b-03.** §32.1.4 L8974 *Appendix F, the numbers 3 33 thirty-three* and L9023 *the counts of Appendices D, E and F*: the rebuilt appendix prints 3 body numerals (6, 12, 24; appf.py's occurrence rule, r2-ch26a §3). The row counts the withdrawn appendix.
6. **Docket 17 / 19 gains 26b-04.** F.3 L11298-L11299 *several of the corrections the Register carries are exactly this rule firing*: Register matches for the rule's words or outcome 0 (token probe: *refuted by its own extent*; *extent* near *empty* / *whole of it*); E.1.5 L11024 names one (item R, 1729). Owed to R3: a reading of the Register for the rule's firings before the sentence is scored true or false.
7. **Docket 9(b) gains 26b-05; 24b-06's C item CLOSED.** F.3.1 L11313 *stated as the chapters cite it: Assert the law, compute the extent* — sites E.1.3 L10983 and F.3.1 only, no chapter. §12.11.3.1's rule in its own words: L3444 *A bound taken from the law closes exactly. A bound taken from the extent closes only …*, L3452 — the paraphrase resolves.
8. **Docket 15 / 34 gains 26b-06 (a Register entry).** Register 1786 *There was never an F.3.1 or an F.3.2*: PP P10761-P10991 carries `F.3.1 And the distribution is the finding` and `F.3.2 The tripwire` beside `F.3.3`; the rebuild (1780) removed them and left F.3.3. The renumbering stands; the history sentence is false. R3: a new entry citing 1786.
9. **Docket 5 / 15 / 9(b) gains 26b-07.** Ruling 45 sites L11225-L11227, L11291, L11332-L11334, L11340-L11341 (F.4.1 / F.4.2 entire are build narration); *the ruling that separates the record of the work from the work* is unnamed — *RULING 45* 0 sites, *record of the work* 0 sites in the Register. Docket 6: none.
10. **Docket 9(a) — 24b-06 corrected:** F.4.3 (L11343-L11360) carries 0 × #P; the sites are §14.6 L4080, §28.10 L8227, E.1.5 L11024, R.5 L11762-L11763. 24b-06 reads *#P-complete (§29)* → §14.6 / §28.10 (book right, instrument wrong).
11. **Verified this unit, carried as counter-cases:** kinds table 6 DATA rows = *Six kinds* = 1780; columns table 4 = *four columns*; 6 + 1 = *seventh* (F.1 ↔ F.4.3); clauses 3; F.2 (iii) HOLDS on 7,260 pairs / 120 electron counts, set sizes {1: 1,416, 2: 5,844}; §2.21 L1081-L1145 *By the law* 2 / *stable structure* 2 / F.3.1 3 under both resolvers; §6.2 L1659, §32.1.3 L8936, D.5.3 L10616, E.1.5 L11024 (*F.3's rule* verbatim at L11295) resolve; 18 Register entries (296, 297, 320, 321, 367, 371, 372, 388, 390, 392, 1729, 1734, 1755, 1762, 1779, 1780, 1781, 1786) headed, no WARNING; 1781 *Appendix F.2 cites 1779* = L11269; first-person 0; R46 0; census 1226-1230 not a defect; docket 27 thirty-third clean unit (0 of 24 paragraphs); docket 36 nothing owed (no author named). No 1,105 / 1,442 / 1,061 / Chapter 34 figure in the unit.
12. **Not read line by line:** the 188 only-PP lines of the withdrawn appendix (PP's F.2 *The coordinates*, F.3.1, F.3.2, F.4 *What closing it would establish*, F.4.2 *… is 1 : 1*, F.5 *And it needs its own falsification*) — Register 1780 is the witness of the removal; INFERRED that every removed figure has a Register home (296 / 297 / 320 / 321 / 1762 for the ratios). R3's pass on items 4-5 reads them. build.py L895's comment says appf.py was re-purposed at the rebuild (INFERRED from the comment).
13. **Conventions, two new:** the coordinate file's `charge` is the ionisation stage (1 = neutral) — an electron count from it is Z − charge + 1, and a pair test on Z − charge is a bijection that leaves set-equality tests unchanged but not parity tests; a `## Appendix X` unit is bounded by the LAST `## Appendix X+1` hit, not by `## References`. **Instrument artefact recorded, not re-banked:** r2-ch26b §1's *Chapter 2 span L568-L1003* ends before §2.21 (`heading_line('3')` resolves early); the finding rests on §2.21's own counts. **Functions owed to r2lib, unchanged:** rbody, body_range, lettered.
14. **Next unit:** Appendix G from `## Appendix G` L11361 to `## References` L11503 (LAST hit; ≈ 142 lines; data; heading lines to be re-taken; G is post-PP — PP has no Appendix G, so the pre-PP diff is empty and 1780-class entries are the witness); then the Index and References under docket 36; then RUL-128 item 3's order.

## Chat 140 --- deferred out of the span main L11361-L11502 (Appendix G L11361-L11406 and the Index L11409-L11502; both CLOSED)

1. **Docket 24 / 14 / 34 gains 27a-01 (a compendium row).** Index of Indices L2021 (Part XI, `# XI · TRANSITIONS, THE COMPLETE TABLE` L1990-L2094), row §1.7: statement ends *…value count while \\* — the tail *|X| stays fixed.* of G L11378 was lost when the escaped `\|X\|` was read as cell boundaries. 29 of 30 load-bearing rows byte-identical to G. Register 1778's *copied unchanged* false at one row. R3: regenerate the row from G with the escape preserved; a new entry citing 1778.
2. **Docket 9(b) / 35 gains 27a-02.** G rows 8.2 (*Register 1375, 1519, 1523, 1535, 1551*), 8.4 (*1375*), 10.4c (*1399, 1403*): 0 of the row's words in any cited entry (jurisdict* only at 543; presymplectic at 1511; null surface 547 / 548 / 550 / 1472 / 1479 / 1506 / 1510). Column is *what rests on it*: a token probe, stated as such. 1403 carries a WARNING (its eight a values are reconstructions) the row omits. Owed to R3: read the seven entries for dependence on T §8.2 / §8.4 / §10.4c before scoring; the MC's `M.C1` / `M.C2` lines cite 1019 / 1022 / 1035 / 1483 / 1484, `W.jur` / `W.rel` none — candidates for the row.
3. **Docket 9(a) gains 27a-03.** Rows 8.2 / 8.4 *Chapter 12*: Chapter 12 (L2304-L3508) jurisdict* 0, functor 0, covariant 0; the sites are §14.6.6 L4245-L4250 (*Verified against T §8.2 (Appendix G)*, *T §8.4 (Appendix G)*), and §18.4.1 L5199. R3: Chapter 12 → Chapter 14 (§14.6.6).
4. **Docket 13 / 17 gains 27a-04; docket 9(b) / 20 gains its second part.** L11363 *thirty-seven objects*: G column 32 (29 handles + 3 MC names); MC `App. G` 32 cites in 30 entries; main 2; Register 8. 1769 sources the 37 to R 1218-1230, which carry no *Transitions* / `T §`. Record-carried. Row 10.1 *Mathematical Compendium, the index vocabularies*: 0 MC lines (*the coordinate set* 3 body lines, *the split alphabet* 1; no headings). R3: re-measure notation-tolerantly; give the three MC objects their pointers.
5. **Docket 24 / 28 gains 27a-05.** Index L11429 *interiority* (plain) and L11432 *interiority* (italic) under *bracket*, both §22.2: *311 entries* counts the pair (distinct 310); *57 terms* only by collapsing it (59 term lines). R3: drop one, restate 310 or keep 311 with the duplicate removed and one entry added — the generator (`index_gen.py`, R46 site) decides.
6. **Docket 15 / 34 / 17 gains 27a-06.** L11419 *The previous index (57 terms, 139 entries, 44 relations)*: PP's Index P10994-P11066 prints *51 terms, 129 entries, 40 specialisation relations* (the old-numbering claim holds: PP §32.1 9 ×, §32.3 14 ×, §24.2 24 ×). R3: the sentence goes with 27b-01 (R45) or carries the witness's figures.
7. **Docket 5 / 6 / 15 gains 27b-01.** R45 / R46 sites: L11419 (`index_gen.py`; *2026-08-24*; *Regenerated*; *regenerated rather than repaired*; *90 locations … absent*; *The previous index*), L11363-L11364 (*until now … This appendix removes that*), L11369-L11370 (*left exactly as they were written … never edited … part of the record*), L11405 (*re-sourced inward*). Docket 6: one site (L11419). First person 0.
8. **Docket 36 gains 27b-02:** Borchers, Wiesbrock (row 10.4e), Hadamard (10.4d) absent from `## References` L11503-L11855; Pauli (2.2) already listed; ANEC an acronym, not owed. Freuder 3 / Montanari 2 / Killing 1 / Helly 1 / Moore 5 present.
9. **Docket 28 / 32 gains 27b-03.** The Index: 25 lines indented one space, 44 three; *Construction* L11412 and *Entries* L11425 unmarked heading-form lines; 15 italic / 29 plain sub-terms with no rule; `Index` (L11490-L11491) vs `*this page*` (L11498) for one location.
10. **Docket 9(b) gains 27b-04.** L11417 *a down-set condition in §16.4 form*: §16.4 (L4407, D2 — ⅅ_def) down 0 / ⊑ 0 / ⊆ 0 under both resolvers; the condition is stated at §2.23 L1162; *§16.4 form* has six other sites (L653, L4475, L4525, L4899, L7740, L8803) — INFERRED an idiom for ⅅ_def's form. R3 reads the six before repairing.
11. **Verified this unit, carried as counter-cases:** 30 DATA rows = *thirty* ×2; Transitions.md 77 numbered sections (0.1-0.4 in, A1… out), 47 unused; all 14 numerals in their own Transitions sections; Λ₉ 1,654 / Λ₁₂ 70,905 on tower-2, Λ₉ 9 coordinates; MC `App. G` 32 over exactly the 30 G §s in 30 entries, main 2, sum 34; Register `T §` 8 occurrences (7 lines: 543 / 549 / 550 / 584 / 585 / 588 / 592) = *eight*; 29 of 29 handles resolve in the MC; IoI Part XI 77 rows, 30 / 47, § set = Transitions'; Index 44 relations / 57 distinct terms / 311 printed locators / 0 down-set violations with `*this page*` ≡ `Index` / 110 of 110 § locators resolve / App A-F resolve; *Six terms and four relations* = the *three bodies* + *Löwdin* groups; S1 / S2 / S3 / D3 resolve (§15.1 / §15.3 / §15.2 / §16.5); *the law of this book* → §2.21; census 717 / 1231 not a defect; docket 27 thirty-fourth clean unit (0 of 76). No 1,105 / 1,442 / 1,061 / Chapter-34 figure; WARNING lines engaged by figure: none; by pointer: 1403 (item 2).
12. **Label correction:** DEF-138 item 7's *Newton decrement at G L11654* and READ-ch25a's *three quarters at G L11670* are `## References` lines (L11654 R.n *the Newton decrement and self-concordance, which λ² and §23.8.2 rediscover*; L11670 *the 3/2 bound … contains §30.3's measured 3/4*) — both live, both tested with the References unit.
13. **Informational (not scored):** the Index's occurrence test on 159 own § locations (convention printed in r2-ch27a §7; *density* unnamed on the page): 4 misses — *the four rules* §25.6, *isoelectronic law* §22.2, *alphabet recovery* §15.1, *decline modes* §24.11. **Conventions, three new:** a `## Appendix G` unit ends at `# END MATTER`, not at `## References` — the span between holds the Index; a table cell is split on UNESCAPED `|` only; a stem probe singularises before stemming (*bodies* → *body*, chat 140's fault 6). **Functions owed to r2lib, unchanged:** rbody, body_range, lettered.
14. **Next unit:** `## References` L11503 to end (L11855; R.1-R.7, R.7 at L11806) under docket 36 and the chat-81 cadence — the main volume's last unit; the two labelled sites of item 12 and every docket-36 name (Seaton, Xia, Routh, Fourier, Motzkin, Gröbner, Borchers, Wiesbrock, Hadamard, Pauli, Pulay, Griffin, Andrew, Cowan and the chat 113-126 list) tested there. Then RUL-128 item 3's order.

## Chat 141 --- deferred out of the unit main L11503-L11855 (the References; CLOSED; the main volume read in full)

1. **Docket 9(c) / 30 gains 28a-01.** Register 344 has no heading (`^#{1,4}\s*344\s*$` 0) inside L11609 *Registers 344-346*; PP P11170 *at register 344* was dropped post-PP at L11606, the range kept; 344 named at Register L5013 / L6403 / L6574. 1710 inside L11807's *1701-1712*: sixth site. R3: with 219 / 220 / 221 / 305 / 239 / 256 -- one entry citing the missing headings, never a relocation.
2. **Docket 9(c) gains 28a-02.** L11615 *§§12.11.1, 22.9*: §22.9 has no heading and no other site. R3 locates seniority's second home (candidates: §22.2, §22.5 -- unmeasured, INFERRED).
3. **Docket 9(b) / 9(a) / 1 gains 28a-03.** L11509 -> §12.11.4 (coupling types 0; the four-type set's home unlocated); L11545 -> §14.5.9 (*tightness* 0; L3914 in §14.5.8); L11563 -> §14.5.3 heading-only, witness at L3579; L11638 -> §26.6 (Richardson 0; 24a-03's twin); L11632 -> §23.1 (Boole 0); L11555 / L11799 -> §32.2 (no [unread] list, no Kreuzer; Q items B / F / N / R at L2758 / L2783 / L3757 / L8887 / L10658, 0 in §32.2). R3 re-points each after reading the target.
4. **Docket 17 / 38 gains 28a-04.** The muon paper's figures L11600-L11602 (2.6e8, 0.203 / 0.262 / 0.292, 11.2 m, 623 m, 1.2e12/15/18, 7.29) have one site and no instrument; Register 319 carries none; only [119, 918] is sited (§22.1.1 L5963 / L5965). *recomputed here and reproduces* is record-carried. R3 / item 38: ask the muon paper for its instrument or label the sentence.
5. **Docket 34 / 15 gains 28a-05.** L11726 *thirteen in this section*: R.5 has 23 paragraph entries, 31 with the inline works; PP's count in r2-ch28b §0. R3 restates or removes the count.
6. **Docket 17 / 37 gains 28a-06.** L11849 *Fifty-nine of them*: Register 1736 matched at *172 works*; 162 rows now; surname overlap bound 16 of 162. R3 re-matches by author AND year on the 162 rows before the figure is kept; 1736's own figure is a 172-row datum.
7. **Docket 16 gains 28a-07.** Montgomery (2014) / Monthly 122 (2015) on one line L11820; Janet 1928 (L11777) vs Register 1929 x3 (16x-06); Edlén 1960 *Handbuch der Physik* 27 (L11621) vs 1964 *Encyclopedia of Physics* (L11624) -- INFERRED one work, two titles, two dates (15l-04); Ritz 1903 vs main 1908 x2. R3 runs docket 16's sweep on the References first.
8. **Docket 36 gains 28b-01, the complete roll.** Cited and unbibliographed (33): Habib, Nourine, Thierry, Kurucz, VALD, BRASS, Hasse, QSAR, NextClosure, Roche, Titius, Bode, Regge, Hagedorn, Gröbner, Klemm, Knaster, Tarski, Schrödinger, Demkov, Ostrovsky, Klechkovskii, Pauli, Seaton, Xia, Fourier, Motzkin, Borchers, Wiesbrock, Hadamard (Routh unnamed anywhere; not owed). Bibliographed and uncited: Huang (& Taylor -- §31.3.1 prints their counts without them), Nash (& Monaghan), Ralchenko, Reader. R3: one References pass adds the 33 and cites the 4 (or removes them); every addition is a Register entry.
9. **Docket 26 / 28 / 32 gains 28b-02.** PP diff: shared 218 / only-main 42 (R.7's two blocks post-PP, Rota, Rydberg, L11606) / only-PP 9 (seven plain-line R.n titles now `###`; production layer). The lead-in L11554 after the two bold blocks is pre-PP (P11118). R3 moves the lead-in above the blocks.
10. **Docket 5 / 15 gains 28b-03.** R45 / narrated past state at L11530, L11537, L11549, L11566, L11628, L11683, L11726, L11772, L11775; [F] (L11518) and [S] (nine lines) undefined -- define at L11554 with [unread] or drop. First person 0; R46 0.
11. **Docket 28 / 32 gains 28b-04 and 28b-05.** Misfiled: Kimura under R.1; Dunz, Janet, Van Isacker / Racah 1954, Chandrasekaran-Flanagan under R.5. Formatting: split entries L11558/60, L11569/71, L11650/52; nine works inline L11727-L11765; bold/plain authors mixed (R.5 1/22); `Dunz, --` no initial; *Lach, M. & Claude (Anthropic)* x2 vs *Lach, M.* x3; [unread] placement; `§R.7` L11853. One formatting pass with 27b-03.
12. **Docket 9(b) / 17 gains 28b-06.** R.7's three-body block: Hsiang, Straume, Chazy, Fleischer, Knauf, McGehee, Kolmogorov, Arnold, Nash 0 in Chapter 36 (L9892-L9936) and 0 in 1713-1724; eight more only in 1721. Löwdin block: Koelling, Harmon, Gerratt, Mills 0 in Chapter 35; Madelung 0 in 1701-1712. R3 reads 1721 first, then decides whether the block or the chapter carries the attribution.
13. **Verified, carried as counter-cases:** Newton decrement / self-concordance at §23.8.2 (DEF-138 item 7 CLOSED at the References' pointer); *three quarters* at §30.3 (READ-ch25a's label corrected); #P at §14.6 / §28.10 / E.1.5; 33² = 1,089, 1654² = 2,735,716 (ordered, diagonal included -- convention unnamed on the page), 904/1654 = 54.7 %; time-paper figures all at §12.11.0.x; Moore families 1, 2, 7, 61, 2 480 by brute force; Hodge figures at §31.3.1; R at L5987; 162 rows / 1669-2026; [unread] 5 + Dunz; L11818's four names above; 37 of 39 cited entries headed, no WARNING; A.2 by hand-grep (L3683, L8132); P20 L396; census 718 / 719 not a defect; docket 27 thirty-fifth clean unit (0 of 241); docket 6 / 11: none.
14. **Conventions, two new:** a chapter that precedes `# APPENDICES` ends there, never at the member's end (section_span('36') runs to L11856); a bibliography entry is a paragraph start, and works joined by ` · **` inside one paragraph are counted under a second, named convention. **Functions owed to r2lib, unchanged:** rbody, body_range, lettered.
15. **Next:** the main volume is CLOSED. RUL-128 item 3 (ii): the Register WARNING sweep (DEF-133 item 5's 1,748 vs 1,738; 219 / 220 / 221 / 305 / 239 / 256 / 344 / 1710 headings; 1779 / 1786 wording; 1778's *copied unchanged*; 1403's omitted WARNING), then the computable re-derivations (Chapter 34 re-take under docket 37, the SCF chain, then 21a-02/-03, 23a-03, 24a-05, 25b-03, 26b-04, 26b-02/-03, 27a-02, 28a-06, 28b-06). The five compendia's own source-order reads remain the open question of the standing block (not put to M this chat).

## Chat 142 --- deferred out of the Register WARNING sweep (RUL-128 item 3 (ii), first half; not a section read)

1. **Docket 35 gains warn-02 and warn-03.** IoI L1861 *Registers 1379, 1380, 1385* cites 1385 (WARNING: the eighty-five row set UNVERIFIED; 4.55 / σ scan / +16 % rest on an unstated selection) with none of it carried in `## Λ_xray` L1831-L1862. Main L11400 G row 10.4c *Register 1399, 1403* carries none of 1403's WARNING (27a-02 measured); IoI L2074's twin row drops the Register pointer entirely. R3: each citer either restates the qualification or drops the citation; the IoI row regenerates from G.
2. **Docket 9(c) / 30 is re-measured (warn-04).** Under bare `### N` AND grouped `### N, N, …` headings the absent-and-cited class is 344 (main L11609), 571 (main L7719 / L9274), **1257 (Register L4857 *1249-1295*, new)**, 1710 (main L11807, MC L3150, PC L194 / L298, IoI L1900 -- five phrase sites; the record's sixth is outside a `[Rr]egister` phrase, INFERRED). 219 / 220 / 221 (L1323), 305 (L1327), 239 / 256 (L1335) ARE headed under grouped headings; every prior recording used the bare convention alone -- the finding is about the reconstruction. Fifteen grouped-only numbers are cited (r2-warn.out §3). R3 decides whether a grouped heading satisfies a range citation; not put to M. The 128 other absent numbers are cited in no register phrase (witness: r2-warn §3 PHRASE regex, six members).
3. **Docket 24 / 34 gains warn-05 (26a-02's second home).** SC L126 row *mult*: *the electron count Z − charge alone, holding on all 7,260 pairs* against SC L90 *Nₑ = Z − charge + 1*. R3's new entry citing 1779 re-points SC L126 with F.2 L11266-L11269 (unchanged) and 1779.
4. **Docket 15 / 35 gains warn-06 (a convention, unscored).** Extent spans naming withdrawn or absent entries: main L10835 / L10840 *registers 1249-1357* (spans 1309 deactivated, 1350 withdrawn, 1257 absent), Register L6455, MC L3150 / L3566 (same span), IoI L1561 *1249-1429* (19 WARNING'd, 6 absent), SC L1061 *1524-1677* (10 WARNING'd, 19 absent). R3 rules whether a reader-facing span needs a qualifier.
5. **Docket 35, owed:** 1396's MC citer (L3716's section) read for the six-and-five split against the twelve donor steps -- token probe only this chat. 1395's carried (B-02).
6. **The record corrected (warn-01):** the Register carries 38 WARNING'd entries / 39 `WARNING:` markers, not five; chat 140's five were unit-engaged. Every later WARNING-line list is taken fresh (never carried).
7. **Verified, carried as counter-cases:** IoI L1893 carries 1341's supersession (*as register 1341 supposed*); MC L3671-L3716 carries *Corrected at register 1426*; SC L1122's 1539 figure is not what 1539's WARNING qualifies; 31 of 47 Register citers carry the correction; 8 WARNING'd entries cited by number nowhere (1309, 1329, 1350, 1367, 1417, 1461, 1589, 1592); 1,748 unprinted as a cell count (R L3917 is P III's spread), 1,738 at main L10197 / R L6519 / SC L994; 1786 and 1778 single-site in the Register; G L11378 vs IoI L2021 byte-identical False (27a-01). Census: none engaged.
8. **Incidental (docket 5 / 46 / 15, one site):** MC's Λspectra-closure section carries *Corrected at register 1426*, *first reported as 47 / 11* and *ground.py* in a reader-facing volume (line INFERRED L3697; section MEASURED L3671-L3716).
9. **Conventions, two new:** a `WARNING:` marker is the colon form (headline words excluded); Register headings come in two forms and both are measured before any number is called unheaded. **Functions owed to r2lib, unchanged:** rbody, body_range, lettered.
10. **Next:** RUL-128 item 3 (ii), second half -- the computable re-derivations in order: the Chapter 34 re-take under docket 37 (read 1332, 1402, 1445, 1448, 1460, 1463 together first), the SCF chain, then 21a-02/-03 with E.3's bracket site, 23a-03, 24a-05, 25b-03, 26b-04, 26b-02/-03, 27a-02's seven entries, 28a-06's author-and-year match, 28b-06's reading of 1721. One instrument per figure family, each banked; none edits a volume.

## Chat 143 --- deferred out of the Chapter 34 re-take (RUL-128 item 3 (ii), second half, first family; docket 37; not a section read)

1. **Docket 12 (16z-04) confirmed by measurement — 34re-01.** Main L9620 and Register 1330 (L4993) print 1.2168450 / 1.3938270 for (√5+√2)/3 / (√6+√3)/3, which are 1.2167605 / 1.3938469 (7 dp, ROUND_HALF_EVEN). R3: a new Register entry citing 1330 with the corrected numerals; the main site follows it (mathematics first).
2. **Docket 34 / 37 / 38 gains 34re-02 (the 8 / 6 / 4 reset split).** On the delivered observed order (LW1-ground.py, Lr = 7p per Register 1306) the record's eighteen classify 9 / 4 / 5 or 8 / 5 / 5, Rf 104 a fifth return; Register 1333 counts *six exceptions (four of them also openings)* — overlapping, restated as a partition at main L9624–L9626. A finding about the reconstruction until walk.py is delivered (REQUEST-LOWDIN); the record stands. R3 reads 1333 against 1306.
3. **Docket 19 / 14 gains 34re-03.** *Never resets mid-subshell* (main L9626; Register 1333 / 1350) fails at Mo 42 and Rh 45 — members of 1401's own fourteen forced resets (4d after 4d, single-electron steps). Record-internal (1401 vs 1333 / 1350); R3's new entry cites all three.
4. **Docket 34 / 17 gains 34re-04.** Main L9641–L9642: 1.785 / 1.028 deviates 0.25 % from √3 at printed precision; Register 1337's *1.7354 — 0.19 %* implies 1.784 (INFERRED); *1.028 at p across four subshells* is no mean or median of the Λ_t p row (1.048 / 1.036) or of 1337's opening row (1.040). UNREPRODUCIBLE; budget: the per-element a values — REQUEST-LOWDIN. R3 after delivery.
5. **Docket 34 gains 34re-06.** *Seventeen of nineteen openings agree; two do not; 89 %* (L9511 / L9514 / L9605): 15 of 19 position-wise (78.9 %), 17 by adjacent inversions (89.5 %); the convention unnamed. No Register site. R3 names it.
6. **Docket 23 / 35 (16z-01 / 16z-02) re-confirmed at five sites — 34re-05:** L9596, L9659 *No parameter is fitted*; L9663 *Exceptionless*; L9616 *Nineteen distinct surds*; L9624 *resets eighteen times* — each qualified by 1350's WARNING or demoted by 1460. Executes with the held withdrawn-law class (RUL-128 item 2), no new class.
7. **Docket 19 (16z-05 / 17a-04) confirmed — 34re-07:** 5f opens at Pa 91 with p = 1, not 0.
8. **Docket 37, measured:** under form B (q/2(2ℓ+1) in the radicand) the forced-reset set is eleven (25, 43, 58, 64, 65, 87, 91, 96, 97, 103, 104) and differs from 1401's fourteen; the memoryless *104 of 106* gives 62 of 106 under a third named convention (midpoint of each candidate's own corridor). Both are findings about the reconstruction (G0c); no figure withdrawn.
9. **Verified, carried as counter-cases:** the opening sequence; 106 of 106 non-empty under both forms; 19 surds at n ≤ 8; the fourteen forced resets exact at N_MAX 7 and 8; 1403's eight a values 8 of 8 and its ten resets; 1402's nearest-endpoint ten; 1445's nine leak steps = five forced + four not (In 49 in no reset list); the six named surds all present; M = 2n − p − 1 on 22 candidates; census 1464 not a defect.
10. **Conventions, three new:** the entrant of a step is the subshell whose occupancy grows most (twelve steps move two subshells); a surd count is scored at 10 dp with the zero endpoint counted as one value; a mid-subshell reset is an entrant equal to the previous step's entrant. **Functions owed to r2lib, unchanged:** rbody, body_range, lettered.
11. **Next:** RUL-128 item 3 (ii), second half — the SCF chain (one instrument, banked), then 21a-02/-03 with E.3's bracket site, 23a-03, 24a-05, 25b-03, 26b-04, 26b-02/-03, 27a-02's seven entries, 28a-06's author-and-year match, 28b-06's reading of 1721.

## Chat 144 --- deferred out of the SCF chain (RUL-128 item 3 (ii), second half, second family; the first Cowork session; not a section read)

1. **Docket 34 gains scf-A-01.** The ordering law's clause 2 (*exceptions exactly La, Ac and Th*: main L9750, Register 1701, MC L3162, PC L279–L280) reproduces on the observed table (LW1-ground.py) only under the convention *rival never yet opened* (C′); under *rival empty at Z−1* the set is {La, Ac, Th, Lr} (6d empty from Pu 94 to No 102), under the opening order {La, Ac}, per step 17a-01's ten. PC L219–L221 states the scope; main, Register and MC do not. R3's new entry citing 1701 names the convention at all four sites.
2. **Docket 34 / 17 — 17a-03 gains three sites:** Register 1701 (*SO worst case 0.083 Ha under every margin*), Register 1712 (*cleared by all*), MC L3162; 0.058 − 0.083 = −0.025 Ha. Per row undecidable until REQUEST-LOWDIN item 10 is delivered.
3. **Docket 9(c) / 28 gains scf-A-03.** MC L3202 *Proved — M §35;.* cites no Register entry for the exact-quartic decomposition (1709, 1711 carry it); MC L3208 prints 1708's ratios 0.999992 / 1.000103 with 1708 outside the entry's chain. Census 365–368 disposed (367, 368 defect).
4. **Docket 36 / 28 gains scf-A-04.** Five of the eight MC LS objects lack the R-FORM prior-art blockquote (L3152, L3160, L3178, L3196, L3214; census 360, 361, 363, 366, 369 — defect). Attributable now: Koelling & Harmon 1977 (References L11811), the n+ℓ rule, the hydrogenic level; the attributions are R3's.
5. **Docket 5 / 6 gain MC L3150** (`mathverify.py` named; *a build task*) — the compendia's first R45/R46 sites recorded from a family read, not a section read (the standing block's open question, not raised). **Docket 37** gains main L9731–L9732 as a second site of the memoryless *104 of 106*.
6. **Environment (Cowork), for every later session:** the Drive spill path is `/root/.claude/projects/-home-claude/<session>/tool-results/mcp-Google_Drive-download_file_content-<ms>.txt` (JSON `{content, id, mimeType, title}`), inline below the harness cap; the sandbox needs the `/home/claude/bin/python3` launcher (3.11 for numpy, 3.12 for the ten f-string members); **r2-ch16n, r2-ch16s, r2-ch16t, r2-ch16u, r2-ch17c cannot be re-run in this sandbox** (3.12 syntax and numpy together; PyPI refused) — their goldens stand banked, unverified here; COORDINATES-2_13.csv must be attached or fetched (10.9 MB, above the chat cap; the spill path may carry it — untested) before r2-ch20a / r2-ch26a are re-run outside their BUDGET branch. BUILD174 is duplicated in Materials (two fileIds); M retires one.
7. **Verified, carried as counter-cases:** 119 = 107 + 12 rows; 106 transitions from 107 elements; −1/(2n²) at 5g–8g 4 of 4; the eleven = 2 + 2 + 4 + 1 + 2; the five contested Z; the Madelung continuation 6d / 7p / 8s = 1712's entrants; c = 137.035999 at four volumes; 1969 − 1950 = 19; the chapter's figures all homed in 1701–1712 with no later Register qualification; 4f / 5f first occupied at 58 / 91; census 359, 362, 364, 365, 1460, 1516 not a defect.
8. **Conventions, two new:** a *never-occupied rival* means first occupancy AFTER the step, not zero occupancy at Z−1 (a channel can empty and re-fill: 6d at Pu–No); a compendium section is bounded by exact heading text (`## LS.` to `## 3B.`; `# THE LÖWDIN-SOLUTION INDEXES` to `# Λ₃`), never by line numbers. **Functions owed to r2lib, unchanged:** rbody, body_range, lettered.
9. **Next:** DEF-143 item 11's order — 21a-02/-03 with E.3's bracket site, 23a-03, 24a-05, 25b-03, 26b-04, 26b-02/-03, 27a-02's seven entries, 28a-06's author-and-year match, 28b-06's reading of 1721 — one instrument per family, each banked.

## Chat 145 --- deferred out of the Sc VI bracket family (DEF-143 item 11's first re-derivation: 21a-02 / 21a-03 with E.3's bracket site; Cowork; not a section read)

1. **Docket 35 / 15 / 34 — 21a-03 gains a convention datum.** C.3 L10300–L10301 *735,091 against 735,092*: E(δ̄ = 0.99345, R∞) = 735,091 exactly (§25.6.4's retired row, restated at L7485); 735,092 reproduces under R = 109,737 alone (R∞ at integer precision) and has no site outside C.3 in six volumes. C.3's "independent reproduction" reproduced the retired δ̄ row at a coarser constant, not the live 736,688. R3 with docket 37 (Sc VI chain).
2. **Docket 15 / 20 — 21a-02 re-confirmed.** 696,400 has one site in six volumes (L10303); §24.2 carries neither the figure nor the phrase; C.3's own arithmetic (0.514; 648,096) reproduces exactly.
3. **Docket 9(c) / 30 gains the family.** The committed prediction of §25.6 / E.3 item A (736,688 in [735,860, 737,380]; the 7s figures; δ₂ / δ∞ / δ(6s)) has no Register entry, and none of its thirty-three figures a Register site (14z-13's *30 main sites, 0 in all five* re-confirmed at the same thirty lines). R3's Register entry for the family seats the derivation (both chains, the constant, Z_eff = 6) before any prose is touched (RUL-128 item 1).
4. **Docket 34 — the rounding-chain convention.** Every figure of §25.6.1–§25.6.4, §32.5.1 and E.3 reproduces with δ carried unrounded (chain U, 25 of 25); with δ quantized to the printed 4 dp (chain P) twelve differ by 1–7 in the last place (δ(6s) 0.9678, E 736,694, 738,550, 784,419 …). The book states neither chain; R3's entry names U. δ̄ = 0.9934 is 0.99345 at half-even (half-up would print 0.9935).
5. **Docket 10 / 34 — 14z-15 re-confirmed:** ± 1,398 (L7066), ± 1,594 (L7105), ± 2,169 (L7106) match none of eight further bases (half-widths; |735,091 − 736,688| = 1,597; dE/dδ × 3.5 % of δ(6s) / δ(5s) = 2,101 / 2,129; dE/dδ × (δ₄ − δ₅) = 1,519; the Rule-4 spreads 765 / 3,455); the limit 892,700 ± 400 keeps its single site L6914. **Docket 9(a) — 14z-07 re-confirmed** under both resolvers (L7115 → §24.6 carries no family figure).
6. **Docket 38 / 10 — 14x-05 / 14x-06 re-confirmed:** 79 % has no k/N with N ≤ 20 but 11/14 and 15/19; 58.8 / 35.3 / 41.2 % are 10 / 6 / 7 of 17 at printed precision; the Ti I 23 / 26 and Sc VI 6 / 10 inventories need their ASD captures (COORDINATES-2_13.csv not attached; the bracket instrument not a member) — UNREPRODUCIBLE with that budget. L7550's *129×* (§28 item 69) unreproducible from the page (relative widths 0.1; 62,007 cm⁻¹ per unit δ) — out of family, recorded.
7. **Verified, carried as counter-cases:** δ₂ 1.0889 · δ∞ 0.9376 · δ(6s) 0.9679 · 0.9567; 736,688 · 735,860 · 738,547 · 737,380 · 2,687 · 1,520 · 1.8; 784,416 · 784,128 · 785,209 · 1,081 · 784,605 · 478; 13.5743 · 13.5615–13.5895 nm · 91.338 eV (E.3 token for token, point value absent — DEF-138 item 12 re-measured); 0.9934 · 735,091 outside the bracket; 0.514 · 648,096; R_Sc and Z = 5 both DIFFER (R∞, Z_eff = 6 are the book's); §32.5.1 six of six; Register 384 / 387 no WARNING; L5355's cell admitted under the lifted caps (264 completions with (n, ℓ) = (6, 0); no coordinates printed).
8. **Environment (Cowork), measured this chat:** a bundle delivered by SendUserFile is NOT in Materials until M uploads it — the gate's title search finds zero hits and stops (this chat's first attempt); Graphify's workspace indexes only Python symbols of the private repo (no markdown, no bundles) and cannot substitute for Materials; a project-instruction CLAUDE.md that is not attached is fetched from Materials by title, and an inline Drive result is decoded byte-exact from the session transcript `/root/.claude/projects/-home-claude/<session>.jsonl` (the tool_result text) rather than re-typed. HANDOFF-97's §0a otherwise held as written.
9. **Conventions, two new:** a figure probe is digit-bounded on both sides (`(?<![\d.,])F(?![\d])`) — an unbounded "1,520" hits Register 1303's *11,520*; a re-derivation chain is scored under BOTH the unrounded and the printed-precision carry, and the chain the book used is named from the match. **Functions owed to r2lib, unchanged:** rbody, body_range, lettered.
10. **Next:** DEF-143 item 11's order continues — 23a-03, 24a-05, 25b-03, 26b-04, 26b-02/-03, 27a-02's seven entries, 28a-06's author-and-year match, 28b-06's reading of 1721 — one instrument per family, each banked.

## Chat 146 --- deferred out of 23a-03 (DEF-143 item 11's second re-derivation: Appendix D.5.9's E = 4 / E = 2 against docket 37; Cowork; not a section read)

1. **Docket 37 loses 23a-03 (i) — REVERSED by measurement.** D.5.5 L10681 *kind only 7 fibres E = 2* and Register 233's *2 by kind* reproduce under the volume's own operator (§6.1 L1540: φ̂ᵢⱼ(v) = max{xᵢ : xⱼ ≤ v}, a running maximum, ambient ∏ Âᵢ(X) — `r2lib.Rset`, lifted at chat 74) on the thirty-two as D.5.4 placed them (A.5 proved · sampled): 16 / 0 · 7 / 2 · 6 / 3 · 1 / 4, 8 of 8; the excess is the *measurement* kind's two cells. Chat 136's reconstruction (r2-ch23a.py §4) bound φ by EQUALITY (max{xᵢ : xⱼ = v}) and so gave 1. The finding was about the reconstruction (G0c); book right, instrument wrong. With A.5 exhaustive (Register 222) the table would read 0 / 2 / 2 / 3 — D.5.5 fibres the thirty-two as printed at D.5.4.
2. **Docket 37 loses 23a-03 (ii) as a non-reproduction; docket 34 gains it as an unprinted convention.** D.5.9 L10823 *E = 4, three cells in formula · analysis and one in theorem · analysis* reproduces under BOOK with 3B.five and 3B.pot entered **measured · sampled · found** (or 3B.five measured · exhaustive · found beside 3B.pot measured · sampled · found; two pairs of sixteen); L10827's *E = 2 … measured · sampled · none found and verified · sampled · none found* reproduces with exactly those two cells with 3B.five proved · exhaustive · found and 3B.pot **proved · sampled · found**; L10830's E = 0 as printed. The page and Register 1726 state *measured* and *sampled* but not the precedent or the first run's verification — R3's entry citing 1726 names the pair. Docket 38 unchanged: the appendix's instrument is still not a member; the reproduction is under the book's stated operator, not the original code.
3. **Docket 34 — 23a-03 (iii) re-confirmed:** L10880's *admits conjectured · exhaustive and proved · sampled* names two of the law · physics box's three unoccupied cells (verified · sampled · none found the third); ℛ admits none, E = 0 either way.
4. **Docket 34 — a convention datum for the whole D.5 chain:** the ambient of ℛ is ∏ Âᵢ(X) (the occupied value sets), not the interval hull — the hull leaves theorem · order open at E = 2 from D.5.7 on where the book prints 0; D.3's two constraints change no count at any stage (BOOK = BOOK+D3 everywhere).
5. **Verified, carried as counter-cases:** 27 / 32 / 36 / 40 / 48 / 65 / 77 elements and 16 / 16 / 16 / 16 / 16 / 22 / 24 fibres; the D.5 table's 24 rows / 77 cells / E 0 equal to the rebuilt index; D.5.9's LS 8 / 3B 9, six new fibres as named; D.5.10's two new fibres; theorem 15 / law 1; the narrated first runs D.5.6 / D.5.8 (E = 1 at proved · sampled · none found) and D.5.10 (E = 1 at verified · exhaustive · none found) 3 of 3; every stage E = 0 under BOOK; the ten cited Register entries headed with no WARNING (305 unheaded — 23b-03 unchanged); census 1215 not a defect, 1536–1545 defect (label form), chat 136's verdicts re-confirmed.
6. **Conventions, two new:** a `### D.x` unit resolves by `lettered` only (the numeric resolver returns None for a lettered heading; both `## Appendix D` hits measured, body = LAST); an E figure is scored under the volume's OWN operator (`r2lib.Rset`, §6.1) before any rival — a re-derivation of E that codes its own φ is a reconstruction. **Functions owed to r2lib, unchanged:** rbody, body_range, lettered.
7. **Environment (Cowork), measured this chat:** HANDOFF-98's §0a held as written; the gate ran in full on the first attempt with BUILD176 already in Materials; an attached handoff lands at `/root/.claude/uploads/<session-id>/<hash>-<name>` (17,443 B, byte-exact).
8. **Next:** DEF-143 item 11's order continues — 24a-05, 25b-03, 26b-04, 26b-02/-03, 27a-02's seven entries, 28a-06's author-and-year match, 28b-06's reading of 1721 — one instrument per family, each banked.
## Chat 147 --- deferred out of 24a-05 (DEF-143 item 11's third re-derivation: Appendix E's E(Q) chain against docket 37 / 38 / 34; Cowork; not a section read)

1. **Docket 37 keeps 24a-05 NARROWED to one sentence, re-confirmed under the book's own operator.** E.1.4 L10998–L10999 *grows the ambient box from 18 cells to 24 and takes E from 4 to 10* (Register 382 L1417 *six admitted combinations*): the box 18 → 24 reproduces; E does not move under BOOK (`r2lib.Rset`, §6.1: an unoccupied value is outside ∏ Âᵢ(X)) nor under the running maximum on a declared ambient carrying the offered value at either end of the order (DECL 4 → 4), nor under |box| − |ℛ(X)| (5 → 11) or |box| − |X| (9 → 15); seven of 108 assignments of the unprinted M, N give |box| − |ℛ(X)| = 4 → 10 and none of them reproduces any other figure of the chain. The sentence's +6 (every new cell admitted) is a convention none of the operator's readings yields; the record (382) carries it; the original instrument (256's code) is not a member (docket 38). Docket 34 keeps the convention item.
2. **DEF-138 item 11 REVERSED in part — the closed items' coordinates ARE in the volume, outside Appendix E, and the chain reproduces.** K *retrievable, hours* (§12.11.0.6 L2785); O *buildable, days* (§12.11.0.5 L2761; Register 364 L1353); M's cost *unbounded* rather than *days* (Register 371 L1373); K's and N's blocks *novelty → nothing* (§29.2.1 L7912; Register 238). Appendix E prints none (0 lines; DEF-138's measurement stands). Unprinted anywhere: M's blocks and obstacle, N's obstacle and cost, O's blocks — enumerated (108 / 864 assignments), **exactly one reproduces every other printed figure under BOOK: M = one claim · retrievable · unbounded, N = nothing · buildable · hours, O = one claim · buildable · days** — the eleven-state's obstacle census 1 / 2 / 8 (E.1.4, 382), fibred 0 and unfibred 4 (E.1.3, 372), Register 465's 4 → 3 on R as nothing · buildable · unbounded (unconstrained — E.1.5's word), the thirteen-state's fibred 0 in all four domains and unfibred 1 WITH the code's constraint *buildable ⟹ cost ≤ days* (3 without: E.1.5's *only the unfibred count was resting on it*, measured), the fourteen-state's fibred 0 (E.1.5, 1729), and R-as-nothing's mathematical fibre admitting exactly *one claim · buildable · unbounded* (E.1.5 L11029–L11031; DEF-137 item 12's owed re-probe, closed). Chat 137's r2-ch24a.py §4 bound φ by equality (the fault chat 146 found in r2-ch23a.py): its *unreproducible under D.4.2's ℛ* was the reconstruction's — book right / instrument wrong, 12 of 13 figures. **Docket 34 gains the four fixed-by-reproduction coordinates as unprinted conventions; docket 10 gains the eleven-state's M and N rows.**
3. **Docket 38 gains Register 396 / §32.6.1 L9270 *E(Q) = 5 unfibred* (a press readout at ten open items):** the ten printed open rows give BOOK 3 (+C 2), EQ 3 — the readout's state (before the domain column and R) is unprinted; a budget, not a negative. Register 2221 already records the figure as stale at a second passage.
4. **Docket 34 candidate (unscored):** §29.2.1 L7911 *six of the eleven items in Q* is an eleven at Register 238 (before N, O, P entered at 256), not E.1.3's eleven (after K, O closed) — two eleven-item states share a count word. **Budget (docket 38):** Register 212's fifteen-state *2 fibred, 1 unfibred*, §32.2's seven, E.4.1's eight and the twelve-state print no rows anywhere (E.4 L11107); E.1.3's *held at seven, eight, twelve* not re-taken.
5. **Verified, carried as counter-cases:** the table's 14 rows / ten open / four closed; per-domain 4 / 3 / 4 / 2 without R and 4 / 3 / 5 / 2 with (1729); the grid's eleven rows = the thirteen less K and O, M's *unbounded* and N's *reachable* consistent with 371 and the reproduction; R the only printed row refuting the constraint; §32.1.4 L8973's *4 1 one* and §32.1.4.1 L9011's *1 1 4* the thirteen's and eleven's figures; twenty-one cited entries headed, 239 / 256 grouped (24b-03 unchanged), 0 WARNING; no census row in E.1–E.4.2 (main L10908–L11142).
6. **Conventions, two new:** the coordinates of a closed item are searched in the whole volume and the Register before they are called unprinted (a closure entry states the row it closes: §12.11.0.5 / §12.11.0.6 / Register 364 / 371); an E chain whose inputs are partly unprinted is scored by enumerating the unprinted coordinates and reporting how many assignments reproduce every printed figure at once — one is a reproduction with a named budget, zero is a finding, many is an underdetermined page. **Functions owed to r2lib, unchanged:** rbody, body_range, lettered.
7. **Environment (Cowork), measured this chat:** HANDOFF-99's §0a held as written (attachment at `/root/.claude/uploads/<session-id>/a4dd0e54-HANDOFF99.md`, 19,688 B). **The session's GitHub credential is bound to no repository** (`api.github.com/repos/lach-matt/Claude-Method-Works` → 403 *not enabled for this session; use add_repo*; no such tool in Cowork; `gh` absent) — the repo route is a Claude Code route; Graphify (216 nodes, commit ce83a349) holds code symbols only (DEF-145 item 8 re-confirmed). M redirected the fetch to GitHub / Graphify and back to Drive for continuity; the three downloads then spilled as §0a describes and the gate passed on the first attempt.
8. **Next:** DEF-143 item 11's order continues — 25b-03, 26b-04, 26b-02/-03, 27a-02's seven entries, 28a-06's author-and-year match, 28b-06's reading of 1721 — one instrument per family, each banked.

## Chat 148 --- deferred out of 25b-03 (DEF-143 item 11's fourth re-derivation: E.8's *Sixty-odd corrections come from §30.3 alone* against Chapter 28's record; Cowork; not a section read)

1. **25b-03 CONFIRMED and NARROWED on a reading; DEF-138 item 6 DISCHARGED.** The forty of `### 28.7.4` L7644 are entries 150-189 (189 - 150 + 1 = 40; §28.7.5 names 186 and 189 as members). **They are fully readable and no budget is owed:** §28.7.4 prints the lead-ins for 150-164 only (two rows, fifteen numbers), and 165-189 are printed as entry bodies in the Register, which DEF-147 item 6 requires to be searched before an input is called unprinted. Under **SUBJ** (an entry is §30.3's when its own text is about the objects §30.3.1-§30.3.9 define — ℛ-closure / sublattice of chains, relabelling and order recovery, the alphabet, arity-2-SAT-linear-Schaefer, PQ-trees / C1P / intervals, d = 2 against d ≥ 3, the procedure and its cost, the residue, and §30.3.1's named sources Rival / Larson / Siggers; §32.2's when it is about self-reference; NEITHER when another section's or an audit's; UNATTRIBUTED when its own text decides neither — every verdict carrying a deciding phrase asserted present in that entry) the forty divide **§30.3 33 | §32.2 1 | NEITHER 4 | UNATTRIBUTED 2**. With 123-139's seventeen, **§30.3's share is 50, upper bound 52**. Against **BAND** (STRICT *sixty-odd* = 60-69; LOOSE = about sixty, 55-65): HEAD 17, SUBJ 50, SUBJ+ 52 outside both; BLOCK 57 in LOOSE only; BLOCK+30.4 62 in STRICT only. **No convention that respects *alone* reaches either band. The defective word is *alone*, not *Sixty-odd*** — §30.3 is given a block the chapter shares with §32.2 (and, at 62, §30.4's five as well). Docket 34 / 12 keep the item, now narrowed to that word.
2. **Docket 34 / 23 gains 25b-07.** `### 28.7 Six made after the register was closed, two printed here` L7481: **six** lead-ins are printed (49-54), and the block's own closing line L7502 reads *Two of these six are corrections of corrections*. The *Six* counts its rows; *two printed here* counts neither the rows nor that line.
3. **Docket 34 / 31 / 23 gains 25b-08.** `### 28.7.3 Seventy-five more from the audit work of the final session, all printed` L7559: the block's numbers span 75-149 = seventy-five, but **twelve are not printed (99-105, 140-144)** and **118 is printed twice** (L7604 inside *112-118*, again alone at L7608) — **63 of 75 printed**. The count word counts the RANGE, not the DATA rows, and *all printed* is false.
4. **Docket 31 gains 25b-09.** Entry **59 is printed twice**: L7517 in §28.7.1 (*Purity as a perturbation measure*) and L7533 in §28.7.2 (*The cheapest undetectable forgery in Λ is 60 cells, not one*). §28.7.1's block is 55-62 = eight and §28.7.2's is 63-74 = twelve — **both count words are right and the numeral is the defect.**
5. **Docket 17 gains 25b-10.** The Register is *the source* (front matter) and carries no entry text over 95-164 — all of 150-164 read **SUPERSEDED (Λ₈ successor development); see register 313**. Chapter 28's descriptions of 150-151 (*two cross-references to §24.4 for a theorem in §18.4*) and 152-164 (*thirteen implementation errors across nine attempts at a d ≥ 3 PQ-tree analogue*) are therefore **single-witness** and cannot be checked against the source. The front matter's band statement is verified exact over 150-189.
6. **Budget (docket 38):** §28.7.5's *Thirty-one of the forty are one error class* cannot be censused — only 165-189 (twenty-five of the forty) carry text. A budget, not a negative.
7. **Docket 34 / 15 candidate, recorded not scored (outside this family):** L962 states *§28.7 states a count in its title — Eight more, Twelve more, Fifteen more, Forty more*; **Fifteen more names no §28.7.x heading in this build** (Eight, Twelve, Seventy-five, Forty). **Docket 26 / 23 candidate:** L7614's *119-122. Four from the shape work* repeats L7599's *110-111* almost verbatim (the nuclear-index commentary beneath E(X) = 0; the re-coordinatisation that *broke a closure which had not been broken*, 0 became 27). Both belong to whatever unit reads §2.19 and §28.7.3 as sections.
8. **Verified this unit, carried as counter-cases:** §28.7.1's *Eight more* = 55-62; §28.7.2's *Twelve more* = 63-74; §28.7's *Six* = 49-54; §28.7.3's *Seventy-five* as the span 75-149; §28.7.4's heading naming both §30.3 and §32.2; 10 + 7 = 17 at L7619 / L7626; §28.7.5's *186 and 189*; the Register's *genesis 1-94, superseded 95-164, mature record 165-1792* over this band; 176-177 grouped under 175; no WARNING on any entry of 123-189 or 313; *sixty-odd* a single site in main + Register; none of the forty cited as *register N* in the main volume.
9. **Conventions, two new:** **BAND** — an English count word (*sixty-odd*) is scored under two stated readings, strict and loose, and the book is credited with the more favourable one before any figure is called unreproducible. **SUBJ** — where a block of entries is attributed to two sections at once, the share is read entry by entry and every verdict carries a deciding phrase the instrument asserts present in that entry's own text; entries whose own text decides neither are UNATTRIBUTED and reported as the reading's upper bound, never silently assigned. **A new discipline for an instrument:** book-versus-record deviations go through a `score()` path that records a finding, never through the integrity checker that fails the run — a run that fails on the book's defects cannot be banked. **Functions owed to r2lib, unchanged:** rbody, body_range, lettered.
10. **Environment (Cowork):** §0a held as written except that **the gate stopped at step 2 for a missing bundle and waited** — BUILD178 reached Materials at 14:09 UTC, four hours after HANDOFF-100 was written, and the title search then returned **two** hits (Materials, and a copy inside a *Claude Chats* export folder created under Materials at 13:47-13:54 UTC). A duplicate title in a Materials subfolder will stop a future gate on the *exactly one hit* rule: the export folders are a Drive action for M.
11. **Next:** DEF-143 item 11's order continues — 26b-04, 26b-02/-03, 27a-02's seven entries, 28a-06's author-and-year match, 28b-06's reading of 1721 — one instrument per family, each banked.
