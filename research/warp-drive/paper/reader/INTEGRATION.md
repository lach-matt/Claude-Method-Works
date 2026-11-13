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

## Ch 4-5 confirmed (2026-11-13, R3-04-05)

- Six notation nits: in lem:linear-wave D (Cauchy development) clashes with the gauge field, C is both the coefficient
  matrix and a generic constant, d should be N_E; 𝒦_m clashes with the Kretschmann 𝒦; φ1, φ2 name the Hopf angles and
  the phase corrections, Ψ names two objects; ∂_r at 04:441 means x̂·∂_x (the stage-0 section uses the
  Eddington–Finkelstein ∂_r); typo "Its oscillating part" 04:468; drop "or profile m" 05:93. If nits 1-3 are adopted,
  Ch 8 (08:406-410) and Ch 9 (09:200-216) follow.
- Σ_τ: Ch 2:250 and 282 write Σ_τ0 := {τ = τ0}, against 02:255 and Ch 4-5 (the annulus A(τ0)); Ch 9 uses Σ_τ for whole
  level sets at τ < τ0 (sent to the readers of 00-03 and 08-09).
- S19 second reading: what S4 must deliver for S19 — d₀ = d₀(m, 𝗌, N) independent of the cut-offs and of k (S19
  fixes the orders once for every b). Uses: thm:iii-i-5-3, rem:iii-i-5-5, thm:iii-h2-3-1 (b)-(c), thm:iii-h2-4-1,
  cor:iii-h2-5-1 with (B5), prop:iii-i2-5-1. If S4 gives only cut-off-dependent d₀, k-independence and compactness over
  B̄₁ would have to be written.

## From S14, S20 and chapter 60 (2026-11-13)

- S20 confirmed (R2-S20). Nits: lem:iii-i6-1-3 gives the zf-weight 0 where it should be −ε; c in lem:s20-injective
  clashes with the frequency bound c; B_r beside B(b) in Step 3.5. The smaller ball (radius ≤ 1/(2C_B)) must be carried
  by S22 (41:65; sent), S23 (42:1008), S24 (43:48, 69-70), S25 (44:42, 580; sent) and S27 (row b4); S19 (38:560) and
  S21 (40:62) need only a pointer. If the S4 repair makes d_T depend on regularity, re-read eq:s20-d.
- S14 (R-S14): 7 Majors; the fix round cites cor:s14-eps-ind-point (proof A) for δ_50, leaves marker 1 for proof A3,
  writes marker 3's proof (table possibly to Appendix B), deletes marker 4.
- Chapter 60: lem:np-10-50-a duplicates chapter 61's prop:after-shell-profiles (a); keep 60's (sent to the 61 writer).
  Chapter 03 points to ch:after-shell where lem:vii-1-2 (60) and cor:vii-2-3 (47) are meant, and its ε_K conditions
  omit (E1)-(E2) of row w1 (sent to the 00-03 reader; the 60 reader rules).
- S21 fix: Lemma iii-i9-2-6 (c) is at b₀ only; new part (e) gives the form at b. Uses of (c) at b must cite (e): S22
  (41:38, 924, 1607; sent to its fix), S25 (44:120, 153, 429; sent), S23 (42:29, 198, 199, 418, 426; sent to its reader).
  Chapter 3 should add def:iii-i10-1-1 at "parameter exponent z". S21 left λ, ϑ, 𝒩, ℱ, 𝒢, M as shared with S22, S23,
  S25 (integration). The material folded into S21 from the source's dropped closing section stays (decided).
- Proof E-b (margins): C2 (the computed approximation's grid values) is used by no theorem (the reader checks); by the
  ruling it becomes a "(Numerical observation.)" remark in chapter 83, or is dropped. The seed-region spline is one
  quintic. E-a and E-b must print the same n = 160 coefficients (sent to E-a).

## From S18, the front matter and chapter 62 (2026-11-13)

- S18 confirmed (R2-S18). Optional nits: the weak limit at 367-368 credited to the wrong result; the reason for weight
  β → β − 2ϵ at 863-864 incomplete; ϵ undefined at 789; broken source line 1131. S19 line 757 may write ϵ′.
- Two-dust correction confirmed (R3-00-03 §2): chapter 83 must state thm:charge-sign for the two-dust background of
  thm:two-dusts (radial bands; f < 0 is the apparent horizon, not the black-hole region; Q = −E; existence for small
  amplitude; no data at second order where f > 0; the continuity step proved in four space dimensions since [CS06] is
  three-dimensional); nothing for the single-dust background. Chapter 80's statement must fix the background too.
- Chapter 62: [[pending:issue-1]] — B taken open (the source's closed B makes the glued space not a manifold at the
  edge of Σ); accepted provided the reader confirms. One unproved, unused clause of BEYOND5 Proposition 6.1 dropped.
  [Sbi15] is a new Appendix A entry (arXiv:1309.7591v3, pages in W-62). Chapter 62 exports lem:interior-far-part,
  lem:interior-where, eq:interior-placing, def:half-class, eq:half-class, lem:half-class, rem:half-class-changes for
  chapter 63.

## S27 (R-S27, 2026-11-13): decisions

- Major 1 (translation parameter): decided to carry the translation in the initial family (ψ_T ∘ φ_S, a translation
  term beside e_S) so the theorem holds without symmetry; not to restrict Theorem 4.3 to the class. Chapters 47, 48
  and 60 must follow (F-S27 lists the passages).
- Major 2: the support argument runs on ΠU′. Major 3: a lemma extending lem:ii-c-3-2 to t_* > ½ is inserted in S27.
- S27 needs an Appendix A entry for local well-posedness and Cauchy stability of the compact part (F-S27 names it).
- S27's dependence on the S4 tame estimate is only through S24 (and S9/S19 behind it): Lemma 2.2 (c), Lemma 2.3,
  Theorem 3.2 (ii), (iii) and the smallness step.
- S8/S9 literature update: S8's last pending marker replaced (cor:std-zero-sobolev entry by entry, thm:std-mazzeo-
  melrose, Usula 5.20 (1)); S9's Cauchy use is at s ∈ ℤ and lem:ii-f-6-3 narrowed to s′ ∈ ℤ (decided: every use is at
  an integer order). New label eq:ii-f-lp-prime (S29 at 48:283-286 may cite it; add a crosswalk row at integration).
  A reader checks both changes.
- Chapter 61: lem:after-shell-mp-data (d) replaces S28's pending marker (sent to the S28 reader); chapter 61 adds the
  hypothesis m(z_i) ≤ 1 to GLUEDECAY5's bilinear bound (5.1) (the reader rules); S28's prop:v-2-3 should hold "at every
  (m, 0, 0, 0)"; chapter 61 fixes the norm ‖·‖_(d_1) (def:after-shell-norm) that chapter 46 leaves open — chapter 46
  may point to it; thm:after-shell-reach for chapter 03's further results and chapter 60's rem:settling-class;
  rem:after-shell-bump for chapter 47's rem:s28-mass-bound.

## Two ε_ind constants; proof C2a; Ch 8-9 and S23 second readings (2026-11-13)

- S13's ϵ_ind (indicial roots of □^Υ) and S15's ε_ind (eq:iii-f1-2-2, roots of L̂_b(0)) are different constants
  (S15 34:1113-1116 says so; the S23 reader found a counterexample to identifying them). Decision: S13's becomes ε_Υ;
  S17, S22 (and S14's δ_50) state which they need, min(ε_Υ, ε_ind) where both (sent to the S13, S14, S22 fixers and the
  S17 reader). S23 no longer uses the identification (its inequality uses δ_+ ≤ η_E and S22's η_2 > ε_+ − δ_+).
  S25's prop:iii-i15-2-5 should cite S21's (e).
- Ch 8-9: Ch 9 gets Σ̂_τ := {τ(X) = τ} for whole level sets; Ch 10 line 31 should take that name. Optional Ch 3 item 5:
  "with item 1" → "with g = g0 on P ∩ {v ≤ v_start}". (The earlier INTEGRATION note "Chapter 9, computational-1" should
  read Ch 8.)
- Proof C2a: 10 of the source's 15 envelope bounds e_k proved as printed; 5 printed values are below the true supremum
  (rounded to nearest) — proved instead e_0 ≤ 1.3241, e_2 ≤ 18.61, e_7 ≤ 3.842e5, e_10 ≤ 3.734e8, e_12 ≤ 4.215e10. Only
  the D[n] bounds (C261, project C2b) use them, and no result uses D[n]. The λ0 norms 0.0024433, 0.0019079, 0.0012228
  are proved; prop:lambda0-norms holds for any m1 and uses only c ≥ 1.32404. Reader to start when C2b finishes.

## S16 confirmed; S11+S12 combined fix (2026-11-13)

- S16 (R2-S16) confirmed. Optional nits: lem:iii-i8-3-1 missing from the window paragraph's list; v as coordinate and
  adjoint function in sec:iii-g-4; name the domain of 𝒞 in lem:iii-g-4-2; ℂ^N → ℂ^(N_E); two early line breaks. The
  [AN00] page stays pending.
- S11 (R-S11): [ER08] (42) confirmed verbatim and the change to Kerr-Schild form proved, so that integration item is
  closed. One parameter set for S11 and S12 (decided): defined once in S11, containing ℬ_♭ and every base point S12
  uses; S12's duplicates removed.
- Proof B (R-P-B): mathematics correct, but several constants weaker than the source's certified values (l = 0 summed H¹
  202.6 vs 184.82, X_0(3) 202.6 vs 158.57, unweighted 1079.4 vs 986.4, master rows C, S4, S3, T2). Decision: first try
  the source's multipliers (l = 0: 43 sech² bumps, coefficients printed in Appendix B) to reach the source's values;
  where that fails, state the edition's proved constants and carry them downstream (listed by the fix). No written
  chapter needs B_0(3) = 275.2; the band constants 963.4 and 1516 depend on these and on B2's 11.477.

## S4 repaired; S24, S8 confirmed; B2, Appendix A, envelope (2026-11-13)

- S4 repair (F-S04): d₀ fixed before k by the orders alone in (L3), (L4), lem:ii-a-8-5, lem:ii-a-8-6, prop:ii-a-9-1,
  prop:ii-a-9-2, prop:ii-a-9-6, cor:ii-a-9-7, prop:ii-a-9-8, prop:ii-a-9-9; Theorem 3.1 two-sided with smooth
  localisers. Chapter 25 (S6) must switch to the two-sided form at lines 178, 203-206, 216-220, 240, 733-745; Appendix A
  needs (S12)-(S14). After the S4 confirming reading, re-check S6, S9, S10, S19-S24 (their dependence lists are in the
  readings).
- S24 confirmed (R2-S24): nits — m5's pointer should be thm:vi-b1-5-1; d with two meanings in lem:iii-j2-2-1 (a) (d′ at
  278 undefined, as in the source); a parenthetical in thm:iii-j2-4-1; prop:iii-i2-5-1-b and cor:iii-h2-5-1 not cited
  at b; quantifiers in cor:iii-j3-3-2/lem:iii-j3-3-3 and a k clash at 1072. Citation cycle S24 → sec:s23-base-points →
  thm:iii-i15-3-1 → S24 (logically acyclic) to be repaired in S25 step 2.
- S8's last citation resolved and confirmed; S9 narrowed to integer orders, confirmed (R-N-27-28). Nits: 27:1467 still
  "c = −γ_cf"; crosswalk rows for eq:ii-f-lp-prime and the s′ ∈ ℤ narrowing; 48:285 may cite eq:ii-f-lp-prime.
- Proof B2: band constant 11.477 proved (proof's max 10.579); radial-derivative constants 283.06 / 305.31 / 308.46
  (source 963.4, 1516); C256 point values at σ = 3, 6 better than the source, from σ = 12 up weaker, the σ^(−1/2) decay
  not proved; the B2 reader decides whether any proof uses them (else numerical observations).
- Appendix A reading (R-95): Major in chapter 45 (S26) 670-673 — cites [Tay11]/thm:std-moser-taylor where
  cor:std-moser-product (2)-(3) (integer s) is needed (sent to the S26 reader). [Usu26] = Usula, Ars Inven. Anal. 2026,
  arXiv:2412.06084v2, confirmed. [RS1] cite the 1980 revised edition.
- S17 second reading: S17 needs ε_ind at windows/pairing and ε_Υ at tf-gains, never the minimum. S20, S21, S22 and S27
  quote ε_ind as prop:iii-g4-5-1's constant; where they use its gain they need min(ε_Υ, ε_ind) — or S15 fixes
  ε_ind ≤ ε_Υ once (to decide after the S15 reading).
- S22 fix added two conditions, ε_K < ε_Υ and η_1 < ε_g (ε_g := min(ε_Υ, ε_ind)); the S22 confirming reader rules.
- Envelope: sin⁴(π(v − ½)/3) is C³, not C⁴; used at 10:820, 62:109-110, possibly chapter 86 and the λ0 statements.
  Chapter 2 (388-391) now says the thresholds use only the support and ∫env². An audit (A-envelope) decides what
  regularity the main theorem needs and which envelope λ0 uses.
- Proof H (L.24): the source's m0′ − |S′| ≥ 0.93κm0 at R ≤ 1.1 is false (0.9000 at R = 1.1); 0.89 is proved and L.24's
  per-period decrease 1.7πλκm0 still holds, so chapter 85 replaces 0.93 by 0.89 and cites P-H's results; chapter 85 must
  supply |S′| ≤ 1.001κ|S| and |S| ≤ 1.001Rm0 (first-degree horizon value). The source's sampled check also misreported
  m0′/(κm0) (quadrature error). The reader rules on 'm0 ≥ cε²' (source ~2137).
- Chapter 60 (R-60): Major F1, the quantifier order (domain and K fixed before ε_m, as chapter 3 has it), being fixed.
  Ruling on chapter 3's ε_K clause: not false; chapter 3 should say "ε_K chosen in the stability theory (thm:vi-c-2-1
  step (4)) ... for some ε_+ and some ℓ_I admissible in row d2". Chapter 46 renames (E1)-(E2) to (Ex1)-(Ex2).
- Proof F: chapter 85 should keep R_k (L.27's x²κ_k) and rename L.16 (b)'s bound to ℛ_2(v) at its three sites.
- S26 (R-S26): 3 Majors — the smallness threshold must be in H^(N_NM) (k₀ := 153, k₁ := 153 + k), as [Hin23a, Cor. 3.36]
  requires; S27 line ~345 has the same claim (sent to the S27 fix). The energy identity is the symmetric sum of squares
  (the source and [Hin23a, (3.25)] share a slip). The Moser lemma needs cor:std-moser-product (2)-(3) at integer orders
  and a Gagliardo-Nirenberg-Moser product-of-derivatives estimate in Appendix A (sent to the Appendix A fix). NP 10.57
  (c) is superseded by thm:iv2-2-4 (crosswalk note). ε^(2j) confirmed. Mass letter: S14 as well as S17 must write m₀.
- Proof D1 fix: the Raychaudhuri identity is proved in the edition (lem:cone-raychaudhuri), so chapter 87 carries
  nothing. Decision on sup s: the edition states the proved enclosures (1.00-1.46 × 10⁻³ at seed 1, 5.0-6.3 × 10⁻⁴ at
  seed 2), not the source's sampled 1.20 × 10⁻³, 5.28 × 10⁻⁴ or "4.1-4.3 %".
- Proof A (R-P-A): A1 and A2 proved; computational-2 (33:2179) discharged. h = 10⁻⁶ may not lie in 𝖧 = (0, h_*)∖𝖹,
  the set the theorems use (the A fix and A3 resolve it). Remaining gap of computational-1 sent to A3.
- Chapters 8-9 confirmed (R3-08-09). Nits: l.46 "(a) is [[lem:domain]] (a)" holds for Ω's slices only, so give the
  contraction itself; l.58 should read "Σ̂_τ1 ∩ P ∩ {v ≤ v_start}".
- Proof F closed: ℬ_k for the bound (no b_ left), 𝒫_k for Lemma (a)'s local quantity, the Remark's percentages
  (12/5 and 21/10 are 3.9 % and 5 % above their limits; 2.13951 is 7.4 % below 4/√3). Chapter 85 renames to match.
- Proof A3 written (proofs/P-A3-every-h.md): every h ∈ (0, 10⁻⁶] and l ≥ 1, three roots with Re < −1/(2h), three with
  Re ≥ 2, so 𝖧 is covered. On confirmation, chapter 33's marker (~285) becomes the sentence citing
  prop:s14-scalar-every-h, and the section goes before prop:np-10-54.
- S13 fixed (F-S13): ε_Υ defined once (sec:iii-d2-1); the reflection is Ξ (D means ρ∂_ρ); new keys prop:np-10-19-i,
  lem:s13-dim-four, rem:s13-kerr-frame. Renames to follow in ch. 34 (1113-1117, 1155-1158, 1517, 1830-1832), ch. 36
  (1416) and ch. 42 (114, which mixes ℰ_ind with S15's ε_ind). S12 writes the static time t_s, S13 writes t.
- S21 second reading (R2-S21): E^ν's ι⁺-class unproved in (e); the parameter ball should point to S20's
  (lem:s20-rows); lem:iii-i8-3-2's "continuous in F" overclaims, so lem:iii-i8-3-3's "→ 0" at b ≠ b₀ needs (i) at α′.
  S22 line ~885 copies the same pattern (for the S22 round). S21 cites (P6) six times, and 38a has no (P6) yet: S25
  step 2 must carry (P6) into S21 or 38a.
- S19 second fix (F2-S19): new lem:s19-products and lem:s19-inverse; prop:iii-i-3-3 now expands around its own g_1
  (δ = h). Crosswalk two rows short (108 labels, 106 rows).
- Chapters 6-7 (R3-06-07): Step 8 correct; 0 Major. The minor is in Ch 3 (03:131-132), for the Ch 3 round: replace
  "Taking λ0 so small that C λ0 ≤ ε1, [[lem:gauge-propagation]] gives D(g_λ) = 0 and Ric(g_λ) = 0." by "Taking λ0 so
  small that C λ0 ≤ ε1, g_λ is within ε1 of g0, hence Lorentzian by [[lem:lorentz-margin]] (ε1 < s0), and it is smooth
  by [[thm:uniform-existence]], the data of [[thm:data]] being smooth; so [[lem:gauge-propagation]] gives D(g_λ) = 0
  and Ric(g_λ) = 0. λ0 and C depend only on (l5, μ0, A, env, T, τ0, K) and a, through Ω, the profiles, C_R and C_D."
  Nits for the integration pass: L also names the torus period at 06:336 and L⁴ the Lebesgue space at 06:431-436
  (rename, e.g. Θ); name the C in λ_ext; state |β| ≤ 2L; state Hadamard's inequality; (iii) uses C M λ0^(K−3) ≤ ε2/2
  with ε2 independent of λ, unstated; N3 paraphrase "continuous, with continuous first derivatives in t and u"
  (optional); 07:83 "hypotheses … on Σ_τ0".
- Chapter 10 confirmed (R3-10). Nit: line 172, "the region between {v = v_start} and Σ̂_τ" should say P⁺ ∩ {τ′ ≤ τ}.
  Chapter 8's numerical remark also uses the sin⁴ profile (for the envelope audit).
- S28 (R-S28): 3 Majors. [CD03, p. 11] projects with L²_ψ(g) onto 𝒦₀^(⊥g) in the current metric; the chapter used the
  fixed 𝒦₀^(⊥g₀) (the source's V7 and the WU26-CS06 note share the misreading). Fix by Option A, every citation literal.
  lem:s28-setting (b) and Appendix A's block omit [CD03, Prop. 5.10]'s smallness hypothesis. (Fin) is automatic for a
  background smooth to the boundary; [CD03] holds for all n ≥ 2; no circularity with chapter 60. Chapter 83 needs the
  review's five conditions once the projection is fixed. prop:v-2-3 holds at every point (m, 0, 0, 0).
- Chapter 62 (R-62): issue-1 ruled — the open B is correct and needed (with the closed B the glued space is not a
  manifold at the edge of Σ). Major: prop:interior needs the stability theory at every inner radius r_♭; chapter 33's
  sec:iv5-0 fixed r_♯ := ½R₁. Fix in chapter 33 (r_♯ := r_♭, prop:np-10-14 (i)-(ii) for every r > 0; sent to the S14
  fix) and one clause in chapter 62 at three places. [Sbi15] entries added to Appendix A. Chapter 63 asked to cite
  lem:interior-far-part rather than prove copies.
- S23 confirmed (R3-S23): prop:iii-i15-2-12 added to the ball-shrinking list (1019) and "with m_ν built at b" (200).
  S22's ball sentence (41-s22:64-66) omits prop:iii-i15-2-12 the same way (for the S22 round).
- S17 second fix (F2-S17): "Two constants" paragraph at the head of sec:iii-g4-1 (ε_ind for windows and pairing, ε_Υ
  for the gain at tf); μ₀ → m₀ and the bare black-hole μ → m (and H^m_b → H^l_b in the exterior section).
  prop:iii-g4-5-1's conclusion now carries ε_Υ, so S20, S21, S22, S27 need ε_g := min(ε_Υ, ε_ind) where they use its
  gain (sent to the S21 and S27 fixes; S20 and S22 at their next rounds); S15 34:1113-1116 still writes ε_ind for S13's
  constant (S15 round).
- Chapter 61 (R-61): Major at 474-476 (the Myers–Perry data on Kerr–Schild slices lie in the class, but not near the
  data of (i)). The bilinear bound needs m(z_i) ≤ 1 (the source's bound is false; counterexample in the review) and
  large radii (R_λ := max(r_χ, R_F, 1)). Line 141's flux claim is false on Σ^IVP when m ≠ μ_end. For chapter 47
  (sent to its fix): prop:v-2-3 at every (m, 0, 0, 0) with |m − m₀| < ½m₀, and rem:v-3-4's sign of ∇²f reworded.
- Chapter 60 fixed (F-60): quantifiers ε_t → (α, steps (5)-(6), R, Ω′) → ε_m → (λ_1, δ); C_𝔟 ≥ 1 compares the two
  norms on 𝔟 (1 if chapter 46 fixes |m| + |A|). For the Ch 3 round: "with K = d_1 + 14, d_1 the regularity of
  [[thm:iii-k-4-3]]", and the ε_K clause: "Fix ℓ0 ∈ (3, 4); let ε_K be the decay parameter chosen in the stability
  theory ([[thm:vi-c-2-1]], step (4), with the data class [[eq:vii-0-1]] at step (3)). It satisfies 0 < ε_K < ε_+ <
  min(δ_♯, ε_ind, ℓ_I − 3, 1/4) for some ε_+ and some ℓ_I ∈ (3, ℓ0) admissible in row d2 of [[sec:vi-c-1]], …"
  ("chosen" is needed: the list omits ε_K < ε_Υ of def:iii-i10-1-3). If S27's translation parameter enters
  thm:iii-k-4-3 (4) or eq:s27-rate, chapter 60 item (ii) must carry it.
- Proof D1 confirmed (R2-P-D1). [Tre19] still missing from the bibliography and Appendix A. Nits: "bounded on E_ϱ"
  (260, 307); the 1.6e−14 margin truncated; ρ beside ϱ.
- Proof A3 (R-P-A3): correct and complete; covers every h ∈ (0, 10⁻⁶], so all of 𝖧. Minor: which facts use the exact
  e. The reader suggests moving cor:s14-remote-point into P-A at merge.
- Proof E margins (R-P-E-margins): every result true; two printed sums miss by a digit; the lens corollary was
  circular. C2 ruled unused: deleted, and the paper's clause "and for its computed approximation in a stated
  interpolant" goes at integration. Pending-marker names must be unique (computational-1 was used three times).
- Proof B2 (R-P-B2): C256's point values, C287 and the σ^(−1/2) decay are used by no proof (class b, a numerical
  remark); only 11.477, 963.4 and 1516 are used. Proof B keeps its present l = 0 multiplier (the source's would make
  305.31 about 1515). Chapter 71 recomputes its ratio sentences from prop:band-points.
- Proofs D2-D4 written: the source's D4a bound 2.41 × 10⁻³ is false (largest point value 2.414 × 10⁻³); the edition
  states 2.42 × 10⁻³. Decision: tables rounded to 10⁻¹⁸ (about 12,000 lines) with the rounding carried into the proof.
  D4b ("unbounded" describes one bounding method) is dropped unless cited.
- Chapter 64 written. Notation to reconcile: ṁ (Ch 3 μ̇), K := r⁻²dv² with K_V, R_H for [HKW18]'s R_1, 𝔪 for
  Kodama–Ishibashi's m (Ch 34 p). [KI03] and [HKW18] statements (thm:rw-ki, thm:rw-hkw) to fold into Appendix A.
  support8 K8 and [Hol08] belong with chapter 61's source.
