# Integration list (working file): what the final consistency pass must settle

Items found while chapters were written in parallel; each is settled once, edition-wide, before assembly.

## Notation
- Chapter 4 writes 𝒦_m (a stage quantity); 𝒦 is the Kretschmann scalar (OUTLINE notation). Rename Chapter 4's symbol.
- Bundle rank and Sobolev orders in the stability chapters: S2 and S3 use N_E (rank) and M (large orders); S6 uses
  N′/N_E; S1, S4, S5 may still write N. Unify to N_E and M throughout files 20–48.
- The energy of chapter 6 is 𝒩; chapter 9 must not write it N.

## Numerical items held for the author (the no-code ruling)
- Chapter 7, computational-1: convergence rates and contraction ratios of the exact correction (no proof uses them).
- Chapter 9, computational-1: a numerical comparison (no proof uses it).
- Chapter 3, computational-1: two values at the numerical point (resolves when chapter 86 fixes the point's data).

## Cross-chapter
- Chapter 3: stability-parameters pending (Theorem 4's parameter hypotheses; resolve to S21–S23 keys).
- S9 replaces II.F1 Lemma 2.1 (b)'s enumeration by "condition (3) of admissibility not assumed": S6 confirmed; S7 to fold
  II.E's item (E2) into its section 1.3 (requested).
- S2 issue-1: the constant C_Γ of display (6.9) is undefined in the source (reader of S2 asked to determine it).
- S5: the symbol ∂Γ^{u/s}_{K⁺} read as Γ^{u/s}_{K⁺} (reader of S5 asked to decide).
- Literature: [Hö85] chapter 23 theorem number for the Cauchy problem (S9); [Hö83, Theorem 7.3.1] page (asked of the
  literature agent).

## From Ch 10 (Bondi)
- Ch 3 thm:bondi-law: "zero for v_B ≤ v_start" changed to "those of g0: all zero except W − 1 = −μ0 r_B^(−2)"
  (NP Theorem M(a)); the Ch 10 reader confirms.
- Ch 10 writes s = r_B^(−1/2), clashing with s = sin ϑ_B of Ch 2-3; rename in Ch 10 (reader proposes the letter).
- The derivative bound |∂(g_λ − g_app)| ≤ C λ^(K−4) t^(−2) (NP P-iii) is used by Ch 10 and absent from the statement
  of thm:past-construction; add it there if Ch 9 proves it.
- Ch 10 restates eq:bondi-law, eq:bondi-form, eq:flux-mean, eq:hawking-mass under its own keys; cite Ch 3's.
- 12 cross-chapter pending keys in Ch 10 (ch2-…, ch9-…) map to Ch 2 and Ch 9 labels; the reader gives the table.

## From the literature pass (scratchpad literature-statements.md: 37 appendix blocks)
- Merge the 37 blocks into 95-standard-results.md after W2's fix round; 31 confirmed at source, 2 from the record's
  wording only ([RS1] Thm VI.14, [DLMF] modified Bessel in S8), 4 not found ([Tay11] 3.6-3.7, [MM87], [Hö85],
  [Hö83] 7.3.1; [BGP] 3.2.11 an alternative for smooth data).
- [BH17] Thm 9.14 misquoted in the current appendix; [CBCL06] quoted without hypotheses; [0C] Prop 2.7 is p. 11.
- [CS06] Theorem 2 is stated on three-manifolds only; [Wu26] Theorem 2.1 is 3+1 vacuum only, yet the localised-data
  chapter applies both to five-dimensional data: investigate (agent launched).
- S11: a written proof that its Kerr-Schild Myers-Perry form matches [ER08] (42).

## Proof projects (maps/proof-projects.md)
- Written proofs in proofs/P-<project>.md, merged into their chapters by the chapter writers: A (C87, Theorem 4's
  epsilon_ind), B multipliers, C (lambda0 constants), F (edge theorem hypotheses), G (far-region exponents) launched.
- Held for the author: D (residuals at 10 l5), E (the families' example), B's band constant, class (b), class (c).

## The author's rulings of 2026-11-13 (STYLE.md section 1, lint, OUTLINE 96-tables.md)
- Class (b), 57 numerical experiments: kept as labelled remarks "(Numerical observation.)", one paragraph each.
  Every pending:computational-N marker already placed (Ch 3, 7, 9, 10) becomes such a remark or a written proof.
- Project E: proved at the record's own example (agents E-a background, E-b margins and bend).
- Constants: prove absolutely everything, including B's band constant (agent B2), A2 (sent to agent A), D1 at the
  record's approximant with the exact-data proposition beside it (agent D1), and D2-D4 with printed coefficients
  (agent D234, planning first; it stops above about 25,000 lines for a size confirmation).
- Class (c), 6 statements about a computational route: deleted; where needed, only what is not proved is said.

## From the S12 writer
- S13 cited the whole NP 10.17 and 10.19 as proved in S12; S12 carries 10.17 (ii), 10.19 (ii), (iv). The S13 writer
  was told to carry 10.17 (i), (iii)-(v) and 10.19 (iii) and re-key.

## From R-06-07
- Items 1-5 of the main theorem are proved in both Ch 3 and Ch 7: keep one proof (fix writer proposes which).
- Key choices to hold the later writers to: II.G Example 3.2 → rem:ii-g-3-2; II.G1 Proposition 2.8 → prop:ii-g1-2-8
  (S24, S27 cite them).
- S19: [Hin17, Proposition 4.1] needs an Appendix A entry with its page. S20 at b needs prop:iii-i2-5-1 at b (S25 asked
  to carry it). S23 leaves Lemmas 2.2(a), 2.2(c), 2.3, 2.4, Theorem 3.1 and J1 at b0; their forms at b in S25.
- S7 issue-1: positive integer orders in Props 4.4, 5.6 (b), Thm 6.1 (S9 wording change); issue-2: (4.4) weakened
  to Omega_(T_0, T_1+1).

## [CS06] and [Wu26] in five dimensions (scratchpad reports/WU26-CS06.md) -- for the writers of M Ch 19-22 (80-83)
- [CS06] Theorem 2 (three-manifolds) is used by Prop L', Thm Q'(ii), Thm X(b): replace by [CD03] Theorems 3.6, 3.9,
  5.9 (pp. 13, 14, 25; any dimension, p. 4) with ch:s28's continuity lemma (Part V Lemma 3.2) re-run on Part I's data
  (mind the converted-KID obstruction), or [CH20] Theorem 6.5 with Remark 6.7 (n >= 3). The continuity in the base
  must be proved in writing. The non-existence results do not use [CS06].
- [Wu26] Theorem 2.1 (3+1 vacuum): delete both uses; the cone-to-Sigma_tau0 route is superseded by Theorem L''.
  [CTG23] Theorem 1.1 covers 4+1 vacuum but not the null dust on N.

## Notation for null infinity
- Write ℐ⁺ and ℐ⁻ (U+2110) everywhere; S19 and S20 write 𝓘⁺, to be unified in the integration pass.
- S16-S20 write λ for the ι⁺ spectral parameter, against OUTLINE's λ = wavelength only: rename in the integration
  pass after a symbol census of files 20-60 (the S16 reader proposes a letter). [AN00, Theorem 3.1] needs a page for
  Appendix A. S16's window rests on NP 10.35's condition on the grafted order (S16 reader checks).
- S20, S22, S24 cite III.I(15) §§1-2.5 forward in S25. If S25 depends on nothing in S20-S24 (the S20 and S24 readers
  check), move S25 before S20 (rename to 38a-s25-base-points.md) so every reference points back.
- S24 drops the vacuous (E5): every "(E1)-(E5)" elsewhere becomes "(E1)-(E4)". Unify B_* (S19) to ℬ_* (S20-S24).
- The trapped-set constant is β_Γ (S6); S2 (21) and S5 (24) still write β_0: unify to β_Γ.
- Appendix A merged (37 blocks). Four entries unconfirmed ([Hö85] 23.2.4, [Tay11] 3.6-3.7, [MM87], [Hö83] 7.3.1):
  an agent is confirming, replacing or proving them. Bibliography: [BH17] needs its arXiv version (v3); [Mel93] lists
  the A K Peters printing while the page is the online 5.0E edition's.

## S4 Major 1 (tameness): a gap inherited from the record and from [Hin26c, Proposition 3.28]
- The seminorm index d_0 (and Proposition 2.4 (e)'s M) was claimed independent of k and of the auxiliary cut-offs,
  but the closed-graph proofs make it depend on them; the inductions of S4 §9 bring in new cut-offs at each level, and
  the tame estimates S9-S10 need rest on this. Fix round launched: Lemma 8.5 (b) by commutator iteration, Proposition
  2.4 (e) by the quantitative remainder bound of the calculus, every induction re-checked. Report to the author when
  settled.
- S25 is cited by S20-S24 and cites them: the S25 reader proposes the split that makes every reference point back.
- S12 review (R-S12): S11's ℬ and S12's ℬ_♭ are two parameter sets, neither containing the other, so S12's
  lem:vi-a-1-1 (‖A‖ < r_♭/4) cites prop:iii-b-3-6 outside S11's range. One parameter set for the whole edition is
  needed; held for the S11 reader (R-S11, checking S11's widening) and then one combined S11+S12 fix round. S12 also:
  line 226 f -> f² in prop:np-10-19-ii (a); lem:s12-ks-domain to be replaced by S11's lem:s11-ks-domain (re-key S19).
- [Hin17, Proposition 4.1] is on p. 20 of arXiv:1502.03183v2 (Appendix A entry from the S19 fix round).
- Ch 3 / Ch 7 duplicate proof of the main theorem's items 1-5: Ch 3 keeps it (Ch 9 cites lem:gauge-propagation);
  cut Ch 7's copy to a pointer after the Ch 0-3 fix round.
- S8: [MM87] does not state boundedness of the small 0-calculus on weighted 0-Sobolev spaces; S8 carries a pending
  marker until the literature agent supplies the right source (Mazzeo 1991 or another), or a proof.
- Ch 6 uses [BH17, Theorem 7.27, p. 56] (H¹ ⊂ L⁴): Appendix A entry requested.
- Ch 10: the letter for r_B^(-1/2) is chosen by the Ch 10 fix round (not ϖ, which Ch 7 and the S chapters use).
- S6 overloads for the integration pass: ϕ/φ, J, p_1, θ_ε; S6's four new nits (ρ_+ ≤ 1 -> bounded; q_1 twice;
  two citations needing their proofs). Ch 3's Theorem 4 should cite def:iii-j-g-plus (S23).
- S2 renamed K -> subscripts only: S8 (27, ~412-413) still cites S^(−K𝟏) from S2; update in integration.
- S5 nits for integration: ρ_a ≤ c_V² left implicit; ϵ₁ names two thresholds. Ch 4: rename φ1(X) to κ(X) (F-00-03).
- S3 nits for integration: line 33's stale 'N in [[sec:i-a-1-2]]' (now N_E); 'every other term' in remark (4); a missing |Y_0| factor in the sharpness proof; 'a' with three meanings in Lemma 6.2.

## From proof D1 and the S16 reading (2026-11-13)

- [Tre19] (Trefethen, Approximation Theory and Approximation Practice, Theorems 8.2 and 15.2) is a new citation, used
  by proof D1. Add it to the bibliography (98) and to Appendix A with its verbatim statements once the D1 reader quotes
  them at source.
- Proof D1 carries a pending marker for the Raychaudhuri identity; it resolves to chapter 87's identity when written.
- Proof D1 proves bounds far below the stated constants (sup|Ric_vv| 1.3e-8 / 6.3e-8 against 4.97e-5 / 2.28e-5). The
  chapters keep the stated constants; sharpening them is optional. Its optional corollary bounds |R_app - R|.
- Notation: the S16 reader proposes ϰ in place of λ for the ι⁺ parameter (S16-S21), with a caveat about κ. The S16 fix
  round applies it in S16 and lists the other chapters; the integration pass carries it.

## From the S1 confirming reading (2026-11-13)

- S1's six nits (R2-S01): N1 the initial-segment step for (H4)'s maximal curves on the smaller domain; N2 the
  parenthesis in Proposition 5.2 on where a derivative is negative; N3 Lemma 4.1 names C_y before y is defined; N4 the
  high-energy remark uses the cokernel description from Theorem 7.2 (3) as well as the Fredholm property; N5 the
  symbol r₂ := σ(ρ⁻¹R₂) collides with the radius r₂; N6 𝒩 names a kernel (reserved for an energy).
- The radii ordering r₀ + δ₀ < r₂ is now a standing hypothesis in S1 (margin at least 5R₁/16, sharp at r_♭ = ½R₁).
  Chapter 31 fixes the radii; carry the condition into chapters 21, 24, 25, 26, 28, 29, 31, 32 and 34 (38 optional).
- Rank still written ℂ^N in chapters 23, 24, 28 and 34, and "N" at chapter 22 line 33: change to N_E.
- Chapter 23 writes e^(−Mz); C_z would match S1.
- S21 reader: S25 §1 uses parts of S21 but not circularly; S25 cannot move before S20 (bears on the S25 order item).
  The λ census and the three S15 keys are in its review (R-S21).

## From proofs F and G (2026-11-13)

- Proof F proves the edge hypotheses on (v_s, v_s + 1/(96(N+4)²)] for every K ≥ 6, not on the source's fixed 1/200
  interval for N ≤ 14; its writer says nothing uses the interval width (the F reader checks this). Constants:
  c_R = 12/5, κ_k/κ ∈ [0.99, 1], c_j = 1, c_t = 2.139 (source 2.13951; the reader checks the direction of each use).
  Chapter 85's writer states the results on the proved interval with these constants.
- Proof G is for chapter 63 (not 64). Its window is (ℓ0 − 1, 3), the theorem's; the planner's max(ℓ0 − 1, 5/2) is
  outdated. Chapter 63's writer uses (ℓ0 − 1, 3).

## From the Ch 4-5 third fix and the S8 confirming reading (2026-11-13)

- Ch 4-5's energy bound is now Λ (not M, not Λ1). Chapter 06 line 198 "M1" must read Λ.
- [CBCL06] is cited by no chapter; its Appendix A entry is kept for now (drop at integration if still uncited).
- S8 (R2-S08): confirmed but for [[pending:issue-1]]. The source must state that the small 0-calculus Ψ^(−2)_0 maps
  x^α H^(m−2)_0 → x^α H^m_0 on the compact ball X̂ (n = 4) for every integer m and real α; the literature agent has
  this. [MM87, Lemma (5.10), p. 284] and [Hin23e, Section 2, p. 9] are confirmed. Optional nits: letters reused at
  line 1394, a stray c at line 1443, no label on L′_p.

## From S27, S28, S17 and the front matter (2026-11-13)

- S27 defines the forward keys S23 uses (def:iii-k-2-1, lem:iii-k-2-2, lem:iii-k-2-3) and cites ε_ind ≤ δ_50 through
  prop:np-10-52. Its writer raised three issues (translation parameter outside the class; Lemma 2.3's support step at
  level 7/8 below Ω_*; the gap (G) and (E1)-(E4) added to the parameter table); the S27 reader adjudicates them.
- S28's continuity lemma lem:v-3-2 is stated for a general compact manifold with hypothesis (Fin), for chapter 83 to
  cite. Its pending marker after-shell-mp-data-on-sigma-ivp (GLUEDECAY5 Lemma 4.1 (d)) is to be exported by chapter 61
  (asked for under lem:after-shell-mp-data). cor:vii-2-3 cites S30 forward; could move to chapter 60.
- S17 reader: α₅ = 2 is used by no proof and contradicted by S21/S23 (least ι⁺-exponent λ_♯ < 2); correctly omitted.
- Front matter (R2-00-03): λ* conflicts with the wavelength-only rule and with chapter 8's λ*; the second fix round
  decides and lists chapter 8's lines if a rename is needed.

## Chapters 6-7 and S10 confirmed (2026-11-13)

- Ch 6-7 (R2-06-07): confirmed. Appendix A must add [BH17, Theorem 7.27, p. 56] (statement matches arXiv v3 word for
  word; the text is in R2-06-07). The six nits, the Ch 7 pointer cut and 06:198 "M1" → Λ are being applied.
- S10 (R3-S10): confirmed. Optional nits: N5 say "bounded above"; N6 resolve the S̄ notation clash; N7 cite
  lem:iii-i2-4-2 for "takes their place". S10 depends on S4's tame estimate; re-check after the S4 repair.
- S2 (R2-S02): confirmed. The fixes add 4 optional nits; δ_O looks like δ_0 (rename). S8 lines 412-413, 513 and 632
  still use S2's old K notation (S16's lines are being brought up to date in its fix round).

## From the S19 fix (2026-11-13)

- Reverse the earlier "unify B_* to ℬ_*" item: S19 keeps B₁, B_*, because ℬ₁ would clash with S18's ℬ_k.
- S19 uses σ_C and s, not s_C (s_C is one number in S16/S17).
- [Hin17, Proposition 4.1, p. 20 of arXiv:1502.03183v2] is stated exactly in S19; its Appendix A block is in F-S19.
- F-S19 lists the S19 results that use S4's (L3), (L4) and d₀; re-check them after the S4 repair.
- S7 (R2-S07): confirmed. Nits: N1 line 1016 the cut-off φ₂ equals 1 only on the set, not on a neighbourhood; N2
  line 1019 the ν-term bound is justified in one direction only; N3 line 982 η₀ ≤ 1/2 is imposed inside a proof (move
  to the statement); N4 "near {r ≤ r₀}, over …" reads as two conditions.

## From S13, S15 and S20 (2026-11-13)

- S13 reader: NP 10.19 (i), 10.29 (iv) and 10.30 (vi) were carried by no chapter; the S13 fix round carries them with
  written proofs, and restores NP 10.15 (i) to the source's form (every z > 0, "≥ 3"). DLMF (10.17.5) sector and the
  [ER08]/[MP86] attribution corrected there.
- S15: the sources' gauge 1-forms carry a sign slip (doubling H_T and f_a); S15 writes the corrected sign; the reader
  adjudicates. NP 10.34 (iv) carried as prop:np-10-34-iv, its numeral replaced by ε_ind ≤ δ₅₀ via prop:np-10-52.
- S20: lem:s20-rows shrinks ℬ_* to radius ≤ 1/(2C_B); the S20 reader lists the chapters whose statements must carry the
  smaller ball. F-S20 lists citation changes S25 and S19 need.

## From S26, S22 and Ch 8-9 (2026-11-13)

- S26 carries NP 10.57 (d) as prop:np-10-57-d; it writes ε^(2j) where IV(1) Lemma 2.1 has ε^(−2j) (the reader
  rules). Black-hole mass letter: S26, S11 and OUTLINE use m₀; S17 writes μ₀ (μ0 is the seed mass): change S17.
  The S26 Part heading was shortened to fit 121 characters.
- S22 (R-S22): ℰ_col = ({(0,0),(1,0)} ∪ ℰ_ind ∪ (1+ℰ_ind)) + ℕ₀ is right; the source's 2 + ℰ_col is wrong. Chapter 44
  (S25) line 475 prints the wrong set: correct it in the S25 fix.
- Ch 8-9 fix: Ch 3 item 3 must read "on P, |g_λ − g_app| ≤ C λ^(K−3) t^(−2) and |∂(g_λ − g_app)| ≤ C λ^(K−4) t^(−2), with
  t = 1 + τ0 − τ ..." (sent to the front-matter fix round); Ch 10 must write h_P(τ) (sent to the Ch 10 fix round).
- S23 fix: S24 and S25 still use ρ for the rows (S22/S23 use ψ) and S24 still writes N_* (N_E rule). S23's inequality
  uses ε_ind as one constant across S13 (ϵ_ind) and S15 (ε_ind); the S23 confirming reader rules on it.

## S25 arrangement (decided 2026-11-13, from R-S25)

- No genuine circularity, but S25 cannot sit wholly before or after S20-S24. The reader's arrangement is adopted:
  new chapter 38a (ch:s25a, before S20): def:s25-at-b, (P1)-(P5), the s20 injectivity lemmas, rem:iii-i15-1-2,
  prop:iii-i2-5-1-b; S21 receives (P6); S22 receives Lemma 1.2 and E^ν's ♮-class; S23 receives Lemma 2.1, §2.7 (moved
  from S22) and §2.2-2.5 before III.J; chapter 44 keeps Theorem 3.1 and Corollary 3.2.
- Step 1 (running): 38a created, Majors 2-3 and the minors fixed in 44/38a. Step 2 (after the S21, S22 and S23 fix
  rounds and readings settle): move the listed parts into S21-S23 and re-read the four chapters' joins.

## From proof B, Ch 10 and S29 (2026-11-13)

- Proof B: φ = 1 − 2/r² admissible for l ≥ 1 and l = 0; constants B_1(3) = 93.78, summed H¹ at σ = 3 202.6, B_0(3) =
  585.53 (weaker than the source's 275.2), unweighted 1079.4. C256's decaying point values (σ = 3…96) and the band
  constant 11.477 pass to project B2 (sent P-B's report). Four chapter-70 results are cited as [[ch:resolvent-bounds]]
  and need keys when chapter 70 is written.
- Ch 10: the letter for r_B^(−1/2) is ς; rem:bondi-solver is a numerical-observation remark. Optional: rename
  prop:bondi-hierarchy. Ch 9 around line 564 may still imply item 3 lacks the derivative bound (the Ch 8-9 reader checks).
- S29: Part IX written at r_♭ (the source's inner-radius re-proof covers only the earlier version); the S29 reader
  checks every radius-dependent step. Notation clashes: Σ^IVP (chapters 30, 46) against Σ_(IVP,r₀) (45); 𝒦 for III.K's
  compact part against the Kretschmann 𝒦; Θ a cut-off in chapters 40 and 46.
- S24 fix: S25 "(E1)-(E5)" → "(Ex1)-(Ex4) and (A_K)" and δ₀ → δ_𝔹 (sent to the S25 fix); S23's base-points opening
  sentence cites S25 §3 (resolve in S25 step 2). S24's tame chain: cor:ii-a-9-7's d₀ feeds lem:iii-j2-2-1 (b) and
  lem:iii-j2-2-4; thm:ii-f1-1-1 feeds lem:iii-j2-2-1 (a) and lem:iii-j2-2-3; a k-dependent d₀ would break the
  k-independent loss d. This is what the S4 repair must deliver.
- Front matter second fix: chapter 2's bound on |g − g0| is ε_out (not λ*); proofs/P-C-lambda0.md calls it λ_out and
  must say ε_out when merged. Chapter 8's λ* (a wavelength threshold) stays. The item now reads "near the initial data
  of the two-dust background of [[thm:two-dusts]]" (the third reading rules); chapter 83 must then state thm:charge-sign
  for that background.
- Ch 6-7 nit pass: Ch 7's duplicate section is now a pointer to lem:gauge-propagation and sec:main-proof; Ch 3 should add
  the clause that g_λ is Lorentzian by lem:lorentz-margin (Ch 7 gave it). Appendix A must add, verbatim: [BH17, Theorem
  7.27, p. 56]: "Let Ω be a nonempty bounded open subset of Rⁿ with Lipschitz continuous boundary. Suppose 1 ≤ p, q < ∞
  … and 0 ≤ t ≤ s satisfy s − n/p ≥ t − n/q. Then W^(s,p)(Ω) ↪ W^(t,q)(Ω)."

## From S16, proofs A, D1, F and the literature pass (2026-11-13)

- S16 renamed the ι⁺ parameter λ → ϰ (and λ_♯ → ϰ_♯, λ_0 → ϰ_0, ∂_λ → ∂_ϰ, C_λ → C_ϰ); its Mellin variable κ → ζ.
  Chapters that must follow: S17, S20, S21, S22, S23, S24, S25, S27 (in S17 and S22 λ^Υ/λ^C → ι^Υ/ι^C; check κ before
  renaming in S17, S21, S22, S24, S25). Line counts in F-S16. The PDF font must distinguish ϰ from κ. S16 also uses 𝔥
  for the fibre inner product (adopt edition-wide) and 𝔐 for its operator.
- [AN00, Theorem 3.1]: page not found (paywalled); [[pending:literature-page-AN00]] in S16. Possible substitute
  [ABHN, Theorem A.7], p. 464 unconfirmed, not in the bibliography.
- Proof A: ε_ind(10⁻⁶) = δ_50 ∈ (1.941370568463, 1.941370568464)·10⁻⁸; prop:gap-sums (least excess
  (5.0190, 5.0193)·10⁻⁸) belongs in chapter 71. Every h ∈ (0, 10⁻⁶] and the remote roots: proof A3.
- Proof D1 reader: the metric class must be in the source's gauge G_x = R²e^(−2(P+Q))/(4(1 − x²)) for the Raychaudhuri
  identity; [Tre19] = Trefethen, ATAP Extended Edition, SIAM 2019, Thm 8.2 (8.3) p. 57, Thm 15.2 (15.8a) p. 109.
- Proof F reader: decision recorded — the source's fixed-interval part (a) of L.27 is dropped (no use needs it).
  L.24's m0′ bounds rested on sampled numbers: proof H. L.26 gets key prop:l-26 in chapter 85.
- Literature pass: Appendix A cites [BW15] (Cauchy, integer s only), [GO13] (Moser, new cor:std-moser-product),
  [Usu26] + [MM87] (0-calculus, new cor:std-zero-sobolev), [Hö90], [RS1] p. 201, new thm:std-bh17-embedding. [Hö83],
  [Hö85] now uncited (drop). S26 line 672 still cites [Tay11]: change to GO13's entry. Chapter 6 should cite
  thm:std-bh17-embedding where it uses [BH17, Theorem 7.27].
- S17 fix: a hat convention for spectral families is stated in S17 at L38-39 (n7); adopt it in the Notation list
  (OUTLINE) and check S16, S18, S22 use it the same way. S17 uses η for Minkowski space in sec:s17-exterior.
