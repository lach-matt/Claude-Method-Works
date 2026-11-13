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
- Proof H (R-P-H): every constant correct; the source's 0.93 (and its m0′/(κm0) ≥ 2.001 / 2.003) false at R = 1.1,
  0.89 suffices (0.89 · 2 · 25/26 = 89/52 ≥ 1.7). For chapter 85: ε in the source's L.24 proof is ε_(M*) (M* = 2N + 8),
  so "m0 ≥ cε²" is false; use ε² ≤ Cλ^(−1/8)·m0 (the source's Lemma L.5). Copying that sentence would be a Major.
- Proof G fixed (F-P-G): renames ρ → κ_Σ, R → R′, v_1 → v1 (sent to the chapter 63 writer); far-wedge geometry cites
  lem:interior-far-part (i); five markers remain for chapter 63 to supply.
- Writers started: chapter 65 (M Ch 15) and chapter 70 (M Ch 17, merging proofs B and B2).
- S15 (R-S15): the edition's sign (B = +2H_T/k_V) is correct and the sources' minus sign doubles H_T and f_a; no
  conclusion changes. The source's numeral 1 + 2.93e-6 is a root location, not a bound; prop:np-10-52's ε_ind ≤ δ₅₀ is
  stronger and proved. The two ε_ind bounds differ by a factor of about 5.
- S25 second reading (R2-S25): order acyclic; lem:s25a-ball correct and independent of S20. Step 2 must repoint the
  11 citations of "lem:iii-i15-1-1 (P6)" in S21, S22, S24. The S24 cycle is repaired inside 44 (a new corollary).
- Appendix A second fix (F2-95): [BW15] Corollary 12 dropped (the slab norm is undefined there); eq:std-slab proved
  from [BW15, Def. 7, Thm 8, p. 13]. n = dim X throughout the 0-calculus. thm:std-gn-moser proved in the appendix
  (ℝⁿ and ℝ^k × N; S26's domains stay with S26). [Hö83], [Hö85], [Ho85] removed; [Tre19], [KP88] added; [RS1] 1980.
  Citations to change in other chapters: 45 (654, 670-673), 06, 09, 22, 35, 62 and proof D1 (list in F2-95). Chapter
  46 cites an undefined thm:std-ds-stability (S27's entry, still to be written).
- S22 second reading (R2-S22): ℰ_col and the ε split right. Rulings: ε_K < ε_Υ is needed (without it Step 4's
  level-3 loop cannot finish); S27 states it, but chapter 03 (thm:settling) and chapter 60's parameter paragraph must
  add it (Ch 3 round; chapter 60's next round) — or S15 proves ε_ind ≤ ε_Υ. η_1 < ε_g is needed only inside S22.
  ε_g := min(ε_Υ, ε_ind) is defined once in S21 under def:s21-eps-g; S22 and later cite it.
- ε sweep still to do (confirmed chapters): S20, S23 and S24 use ε_ind as the gain that S17 now gives as ε_Υ; they need
  ε_g where they use the gain. One small fix round with a confirming check, after S21 and S22 settle.
- S17 confirmed (R3-S17). Nits: L1069 and L1433 "min Re ℰ_ind ≥ ε_Υ" should cite S13 and prop:iii-f4-5-1; L590,
  L731-732, L931 treat λ_♯ as a pole without λ_♯ < ℓ_I; the tensor index m beside the mass m (L1768, L1879,
  prop:np-10-64); two masses called m at L1792-1794. S20:1269 still calls the gain ε_ind (ε sweep).
- Chapter 63 written (W-63). issue-1: the past construction's order raised from k1 + 5 to k_P := 2k1 + 14 (K*
  unchanged) — to be confirmed by the reader. issue-2 (serious): the source's Step 6 checks small energy near the
  cut-off band only for the uncommuted field; the twice Z-commuted field's energy appears to grow like |T|^(2a−4) and
  diverge on the whole window. An independent reader and a proof project (proofs/P-I-cutoff.md) run in parallel.
  prop:own-same-index-sets answers rem:half-class-changes (log orders do not rise, for every m). Proof G needs three
  rewordings (F_p smooth only up to s = 0; h_R does not vanish beyond the band on the initial slice, same exponent
  2a − 6; chapter 63 uses the flat Σ_4). Notation: N for the null boundary clashes with OUTLINE's N; proof G's k := dv
  clashes with the data's k. DLMF (15.10.1), (15.5.1), (15.4.28) for Appendix A.
- Proof E background (R-P-E-background): every result true (about 140 rows recomputed; the true k = 2 error 8.403e-4
  against the bound 8.558e-4); the λ > 0 argument was circular (repaired by Ŝ ≥ 0.6112). Every bound is stronger than
  its uses need (tube margins ×33, ×4, ×35, ×56). One copy of the quintic and μ_s: sec:table-seed-profile; E-a's
  sec:tab-bg-spline deleted. T4 (rem:bg-grid) is used by no proof.
- Chapter 60 confirmed (R2-60). Nits: prop:iii-k-1-2 now defines 𝒟_(S,S⁰); lines 65-66 fix A and the envelope after
  choices that depend on them; T′, R′, k each name two objects; the comparison at 287-293 omits ε_K < ε_Υ.
  Follow-up when S27 is confirmed: carry S⁰ at chapter 60 lines 83, 96-97, 101, 260-261, 278-279, 312 (the "without
  symmetry" half) and in chapter 3's item (ii).
- S27 fixed (F-S27): translation parameter S⁰, φ_(S,S⁰) := ψ_(S⁰) ∘ φ_S; new lem:s27-translated-exterior (chapter 45
  is boosts only), lem:s27-below, sec:s27-local from [DS23, Thm 2.5, p. 5] (thm:std-ds-stability, being added). Chapter
  48 must carry the translation in its Theorem (2)-(6) and the class corollary (h_(S,S⁰), 𝒟_(S,S⁰)). Open question
  for the S27 reader: whether S13-S25 state their (C3)-choice uses for any choice meeting the listed conditions.
- S21 third fix (F3-S21): def:s21-eps-g at line ~151; lem:iii-i8-3-3 gains ‖u_j − u‖ → 0; S22 has the same gap in
  lem:iii-i11-3-3 and lem:iii-i13-2-3 (sent to the S22 fix). S20 still uses ε_ind in prop:iii-i6-2-1 and
  eq:iii-i6-2-7 (ε sweep).
- S13 second reading (R2-S13): Major — ε_Υ undefined over all roots (gaps → 0); restore |Re ι| ≤ 10. NP 10.30 (ii)
  for all z > 0. Proof A3 fixed: the exact e enters only through lem:s14-small-h (a); placement after sec:s14-model.
- S14 fixed (F-S14): r_♯ := r_♭ ∈ (0, ½R₁] (chapter 62's Major); eq:s14-s general; strip finiteness in
  prop:np-10-54 (iii); δ_50 cited from cor:s14-eps-ind-point (chapter 34 line ~448 to cite it too — sent to the S15
  fix); proof A's corollary to absorb rem:s14-pa-low-types (sent to the proof A fix); 110 μ → m renames. Crosswalk rows
  for renamed and new labels are in F-S14 (integration).
- Chapter 61 fixed (F-61): depends on chapter 47's prop:v-2-3 change landing.
- S19 third reading (R3-S19): Major — eq:iii-i-3-7's L² class fails at ℓ_I = ½ (π̸₀h's radiation coefficient);
  ℓ_I ∈ (0, ½) as [Hin26]. The fix lists other chapters relying on ½.
- thm:std-ds-stability added to Appendix A ([DS23] Thm 2.5, p. 5, arXiv:2308.09851v1, word for word).
- Chapter 62 fixed (F-62): thm:std-sbierski extended (p. 10 assumptions, footnote 19, arXiv:1309.7591v3). Still open
  elsewhere: chapter 62's nit 18 is in chapter 3; [Chr11] is uncited (drop from 98 or cite); chapter 60's 𝒟_0 and T′.
- S4 second reading (R2-S04): the tameness deliverable holds. Chapter 25 (S6) must adopt the localisers and global
  error terms of the new Lemma 4.1 at §ii-d-4 Steps 1-4 (693-880), lines 395, 509 and the earlier list (178, 203-206,
  216-220, 240, 733-745) — after S4's second fix. Appendix A must add [Hin26c, Lemma 3.5] to (S6), or chapter 27 line
  1280 must cite (S5) only. Optional citation fixes: chapter 26 line 258, chapter 28 line 1411.
- S26 fixed (F-S26): thm:iii-c2-3-1 (1) holds only near the interior of Σ_(IVP,r₁); S27 lines 712-716 and ~790 to be
  checked (sent to the S27 reader). Nit n1 needs an OUTLINE.md change.
- S11-S12 fixed (F-S11-S12): one parameter set def:s11-parameters; lem:s12-ks-domain removed (S19's two citations sent
  to the S19 fix); (E1) for integer s ≥ 0 from [Hin26d, Prop. 3.55 (3), p. 57] and Example 3.63 — S24 line 640 writes
  H^s (check integer); Appendix A's thm:std-sbg-calculus could quote them. Nit 14 (ḡ) at integration.
- Proof C complete (C2b): S = −(4/9)A²env²h² sin 2ϑ r⁻³(dv⊗dϑ + dϑ⊗dv); D[n] bounds 0.43× the record's or better; no
  result uses them (reader to rule on class).
- Proof A fixed (F-P-A): h = 10⁻⁶ ∉ 𝖧; ε_ind(h) = δ_50 does not hold on all of 𝖧 (rem:s14-eps-ind-scope); 𝔡₀, 𝔡₁
  (= chapter 40's d_c0, d_c1), 𝒬. Chapter 33's proof of prop:np-10-52 (iii) defines d_s0 again (rename at integration).
- Proof H fixed (F-P-H): S-bounds where R ≥ 1/2 rest on chapter 85's first-degree horizon value (pending ch85-s-bounds);
  rem:l-24-eps for chapter 85.
- Envelope audit (A-envelope): the proof needs env ∈ C_c^∞ (def:approximant, thm:main's smoothness); about K + 10
  derivatives are used and K ≥ 6, so sin⁴ (C³) is covered for no admissible K. Every λ0 constant uses
  env_C = c·cos¹²(πy/2)·exp(−y²/(1−y²)), y = (2v−4)/3 (same support, ∫env² = 105/128); no proved constant uses sin⁴.
  Repairs: ch 10 moves sin⁴ into rem:bondi-solver; P-D1 says the cone results do not use thm:main; P-F's envelope is
  env_C; ch 86 states its numerical point with env_C; ch 63 gets a closed form for the transform ("ω = 10, …, 320"
  holds only on 10, 20, …, 320; ê vanishes exactly at 2πn/3); ch 3 an optional remark. Do not swap env_C into the sin⁴
  sites (∫env′² differs; P-D1 needs sin⁴'s analyticity at the ends).
- S29 (R-S29): Part IX holds at r_♭ as written. Major: the S27 translation follow-up (ġ⁰ = −ℒ_(V⁰(S′^(0)_1))g); chapter
  3 line ~288 follows (sent to the Ch 3 fix). Σ^IVP is right: chapter 45 must rename Σ_IVP → Σ^IVP and
  Σ_(IVP/fut/past,r₀) → Σ^IVP/fut/past_(r₀). Θ(k) → −Υ̇⁰(k) (lem:iii-b-6-3); chapters 64 and 66 follow. Decision
  pending: chapters 46 and 48 use 𝒦 for a set, clashing with OUTLINE's Kretschmann 𝒦 — choose one new letter for both
  chapters at integration (grep for an unused one).
- Appendix A and bibliography confirmed (R2-95). Nits: bracket the re-indexed exponent inside the [Usu26] quotation;
  a [BW15] hypothesis left to "so do we"; equation numbers in the S-heading; Chebyshev quoted for n ≥ 0 but its points
  defined for n ≥ 1; 46 bibliography entries are cited nowhere (prune at integration). Still to read: the [CD03]
  Prop. 5.10 block (after the S28 fix) and the extended thm:std-sbierski; add [Hin26c, Lemma 3.5] to (S6).
- S25 third fix (F3-S25): new cor:s25-tame holds the S24 material (the cycle repaired); (P6) is lem:s25-p6 (44:73).
  Step 2 re-key, after the S21 reading: "lem:iii-i15-1-1 (P6)" → [[lem:s25-p6]] at S21 lines 72, 86, 269, 444, 870,
  1503 and S24 lines 181, 248, 368, 420 (S22:75 already done).
- Proof A3 confirmed (R2-P-A3): the exact-e clause now names cor:s14-remote-point's dependence on
  lem:s14-sextic-count (a) (applied by the coordinator); μ = 34133/13653; INTEGRATION's earlier A3 placement line is
  superseded (the section goes at the end of sec:s14-model, before sec:iv4-1).
- Envelope texts applied and checked by the coordinator: chapter 10's sin⁴ material is now inside rem:bondi-solver
  (the fourth derivative jumps by 8π⁴/27; (2/9)∫p′² = 5π²/108); proof D1 says it uses no thm:main and that env_C is not
  entire (essential singularities at v = 1/2, 7/2); proof F's envelope is eq:envelope (lem:envelope-constant).
- S28 fixed (F-S28): n9 (forward reference to chapter 60) kept by decision — logically acyclic; n10 (Appendix A's
  [CD03] Theorem 3.6 gloss) and the crosswalk row for rem:v-3-4 (cite chapter 61) at the next Appendix A round.
  Chapter 61's step (2) should bound C^(k_g+2) (the S28 reader checks).
- S21 confirmed (R3-S21). Nits: β′_+ in ‖·‖_(α′) never fixed; line 151 "different constants"; lines 1025-1028 say why
  the minimum is taken. S20 still writes ε_ind at 39:1269-1369 (ε sweep).
- S22 third fix (F3-S22): the "→ 0" repair keeps the hypotheses of lem:iii-i11-3-3 and lem:iii-i13-2-3 and proves
  ‖u_j − u‖ → 0 from uniqueness; chapters 42-44 need no change (reader checks).
- Chapter 61 confirmed (R2-61). Nits: the distance claim "for the members" needs one clause (496-498);
  cor:after-shell-every-rate should say δ depends on ε (251-254).
- Proof E margins fixed (F-P-E-margins): the Rácz converse cites [Rác…] (4.22), which Appendix A lacks (next Appendix
  A round, if the reader rules it needed). The interpolant clause is only in maps/registry-notes.md:244 (no chapter).
- S25 step 2, the (P6) part, done: ten citations in chapters 40 and 43 now cite lem:s25-p6 (each checked against the
  lemma's statement). The remaining step-2 moves (Lemma 1.2/E^ν into S22, Lemma 2.1 and §2.2-2.5, §2.7 into S23) are
  optional now that the citation order is acyclic; decide at integration.
- Proof H confirmed (R2-P-H): the reader's paragraph (R decreasing on the band; −1.7κ ≤ (log R)′ ≤ −0.89κ; two
  consecutive periods in 1/2 ≤ R ≤ 1.1) seated after line 251, checked by the coordinator. Nits: intro wording; the
  λ-range in the pending hypothesis; Λ ≤ λ at every band point; undefined γ; "cannot be lowered" overstated; where ε_c
  is evaluated in rem:l-24-eps.
- Proof G second reading (R2-P-G): a new Major — off the band the commuted fields are nonzero (∂_t̃²h_R =
  2P(Σ)/g⁻¹(dt̃, dt̃)); far-sigma-data asks jets beyond chapter 63's k1 + 4; the sourced Σ_4 is proved nowhere; (v)'s
  a < 9/2 against chapter 63's a < 3. Sent to the cut-off proof project; proof G's next fix waits on it.
- S19 third fix (F3-S19): ℓ_I ∈ (0, ½); no other chapter relies on ℓ_I = ½ for this class (28-s09:165's P_Λ is a
  sup-based class).
- Proof B2 confirmed (R2-P-B2): all 503 Bernstein coefficients exact and positive; B♯(6) printed as < 4.683 (the exact
  p_I gives 4.681994, the decimal 0.50776 gives 4.682008); the two markers now cite prop:resolvent-outgoing and
  prop:resolvent-above-barrier (chapter 70). Nits: the remark's "not proved" sentence must not read as including
  11.477; T-B2's needless cor:band-one-derivative; symbol clashes s, C, c, v/ν; one C² wording with proof B at merge.
- Ch 3 fourth fix (F4-00-03): settling theorem now K = d_1 + 14, the ε_K clause, ε_K < ε_Υ, chapter 60's quantifier
  order, the translation S⁰ in (ii) and lines 312-316; rem:envelope-regularity; nit 18. Chapter 60 still lacks S⁰
  (follow-up after the S27 reading).
- S27 second reading (R2-S27): translation, ΠU′ and the ε split confirmed; def:s21-eps-g exists; N_ex = 153 matches
  chapter 45; [DS23, Thm 2.5] verbatim. Major: lem:s27-below (iii) on {½ ≤ t_* ≤ 1} (short fix with
  g_(b₀)⁻¹(dt_*, dt_*) ≤ 0). Minors: Prop. 1.2 (1) on all of 𝒟 (chapter 45's new argument); the projection on the slab;
  (L) for forcing in H^k and k < 4; Prop. 1.2 (3) only a modulus of continuity; (C3) needs the companions' leading terms
  (lem:iii-i14-2-1); lem:s27-boost-move two-sided radius.
- S11/S12 confirming reading (R2-S11-S12): one parameter set ℬ, ℬ_* ⊂ B̄_1 ⊂ ℬ, ℬ_VI ⊂ ℬ; (E1) for integer s, (E2)'s
  analytic Fredholm and finite-rank proofs; S12's identity, simplicity of r₊, transversality, signature all correct.
  S12 CONFIRMED. S11 minors: (E1), (E2), (EE), lem:iii-a-1-4-5 proved for scalar operators only but used on bundles in
  S14, S15, S22, S24; (E2) gives the derivative gain only for negative-power coefficients. Nits: Theorem 3.21 on p. 38;
  uP → uΠ (S12:783); r₋ ≤ ‖A‖ (equality at A = 0); 𝒩 clashes with OUTLINE's energy (rename); sampled m in the remark.
- S13 third reading (R3-S13) CONFIRMED: ℳ uses roots with |Re ι| ≤ 10 (every sl, vl root has |Re ι| ≥ l − 1); every
  use of ε_Υ (chapters 32, 34, 36, 40, 41, 46) needs only those roots; NP 10.30 (ii) for every z > 0. Nits for
  integration: line 1197 justify the upper bound z/2 and ι + l > 0; remark (d) 1993-1996 add that in 3 + 1 dimensions
  μ_s0 + 1 = 0 is a root at z = 0.
- Proof A confirmed (R2-P-A): all 17 first-reading findings fixed, every changed number exact. N1 (rem:s14-eps-ind-scope:
  prop:gap-sums depends on the gauge parameters (e_Υ, γ_Υ), not on z alone) applied in the reviewer's words; N2-N5
  applied (real part at distance; the opening sentence's scope; R̄_j and the re-expansions printed, M̄ their majorants;
  lem:s14-crossings in T-A's two "Used in" lines). For other chapters: 33:2557 and 34:453 cite lem:s14-delta50 for the
  value of δ_50 (h-free); chapter 34 must NOT cite cor:s14-eps-ind-point for ε_ind ≤ δ_50 at h ∈ 𝖧 (keep
  prop:np-10-52 (iii)); 46:1110 gets the value from lem:s14-delta50; 33:2541 d_s0 clash.
- S26 second reading (R2-S26): the first reading's 3M 9m 6n resolved; M1 checked at source ([Hin23a, Cor. 3.36] and its
  footnote 17, which Appendix A does not quote: add it). New Major N1: thm:iv2-2-4 Step 4 needs P_iu₂ ∈ L^∞, true only
  for k ≥ 3. Minor m1: thm:iii-c2-3-1 must state the high-norm smallness h_S needs. Second fix running.
- Proof D2-D4 (P-D234): coefficients rounded to 10⁻¹⁸ with a closed-form lemma |∂^γ(F − F̃)| ≤ ε₀M_γ; every row
  recomputed with interval coefficients: points 2.4143e-3 ≤ 2.42e-3 and 3.728e-5 ≤ 3.73e-5, D3 2.980e-4,
  D2b ≤ 4.914e-4; the proved movement of a point value is 1.3·10⁻⁷ (2·10⁻¹¹ was a measurement). D4b cited nowhere,
  dropped. The figure 2.41·10⁻³ (false; the proved value is 2.42·10⁻³) appears in no chapter; chapter 87, when written,
  must print 2.42·10⁻³.
- S25 and 38a third reading (R3-S25) CONFIRMED: u^rot_β consists only of terms (a), (b) identify; cor:s25-tame's
  inputs are all cited by S24 and the citation order is acyclic; 38a cites nothing after S19. Nits for integration:
  44:531 E^ν is lem:iii-j2-2-1 (b), not (c); 44:569 "rates of q exceed 2 + ε_K" only for the polyhomogeneous terms;
  44:563 the pointer should include *The augmentation at b*; 38a:156 name the weight α. Not counted:
  sec:s23-base-points (4) points forward to cor:iii-i15-3-2.
- Ch 64 first reading (R-64): every identity redone, KI03 and HKW18 quoted correctly at source, hypotheses hold in
  4 + 1; the Remark is used by no proof. Minors: the set at line 84 contains r = r_♭; Theorem (a)'s int N ∩ M°_♭
  clause unproved; XΦ for a rotation X; the ∂_u² formula only on the cone; "uniformly in l" fails for the 𝔪Φ
  coefficient; lem:np-10-1b (b) needs a density step. Nits: ṁ vs chapter 3's μ̇, 𝔪 vs chapter 34's p, K, τ, ω, c, s,
  t, Y. Fix round running (with Θ(k) → −Υ̇⁰(k)).
- S22 third reading (R3-S22): N1-N5 and the ball sentence fixed; lem:s25-p6 states what S22 uses; def:s21-eps-g ties
  ε_ind, ε_Υ to prop:iii-g4-5-1 only; the "→ 0" repair correct. Minor: Step 6 now bounds by ‖F‖ through
  thm:iii-i11-4-1, so cor:iii-i15-2-10 "uniformly in b" / "Steps 5-6 unchanged" and the remark at 1430 give no valid
  bound at b; the same in chapter 44 (lem:iii-i15-2-4, def:iii-i15-2-3, prop:iii-i15-2-5 Step 3 claim bounds by G
  alone). Nits: 1035 leftover phrase; seminorm for (i); sec:iii-g4-1 pointer; v1 in lem:iii-i10-2-1 (b). Third fix
  running on 41 and 44 together; S25 reopened for that minor only.
- Ch 62 second fix (F2-62): V has dt_IVP timelike and in the cone of dτ (dτ past by lem:domain (e)); new lem:interior-chart
  proves lem:vii-1-2 (a) on {|x| ≥ ½r_♭} and the g_λ vs g_(b₀) bound, inverse included; 8 nits applied. Chapter 60's
  optional widening is no longer needed (drop it from the follow-ups).
- Ch 70 written (W-70): exports part:constants and ch:resolvent-bounds; B2 merged (with 4.683; markers resolved to
  prop:resolvent-outgoing, prop:resolvent-above-barrier); T-B2 tables kept in the chapter (may move to Appendix B);
  P-B merged at its pre-fix state, so re-merge after the proof B fix lands; gap: cor:morawetz-one-derivative (c)-(d)
  uses u = Σu_l undefined. The source's certified multiplier constants replaced by proofs B/B2's. The e2lower5 lower
  bounds are left to chapter 71. Markers computational-1 (scalar-type indicial roots and singular values at the
  computational point) and computational-2 (M₃₃ = −(5000r − 1)/r³): proof project running. Notation: mass m; source
  F; multiplier profile Θ; V_0, V_1, V_2 → V^□, V^v, V^s; λ := 1677/2048 → e₀; Wronskian 𝒲; sgn σ → ϵ_σ.
- Proof E background confirmed (R2-P-E-background): the λ > 0 argument no longer circular (0.6112 ≥ S − I/2 > 0 without
  μ; λ(u2) ≥ 0.5295335571); the four-digit ε entries 2.681e-5, 5.681e-6 deliberate and needed; region III rows, the
  lemma, the sign and the interior errors confirmed; the seed rest 2·10⁻¹⁰ right. Minor (series order 8 → 9, as Φ̃′
  and each 𝒟 lower the order) and nit ("rest" is not a column) applied in the reviewer's words.
- S15 confirmed (R2-S15): sign of B and ζ₁ checked by sympy on 5D Tangherlini; ε_ind ≤ δ_50 rests only on the s50 root
  (prop:np-10-52 (i), (iii)); ε_Υ correct at four places. Nits for integration: 519-521 ℂ^k, "k dim π" → n_W, n_L;
  407-409 "give twice" does not fit v1; 453 may cite lem:s14-delta50.
- S29 fix (F-S29): translated background throughout; Θ(k) → −Υ̇⁰(k) via lem:iii-b-6-3; principal part ½□_g with
  symbol ½g⁻¹(ζ,ζ). Cross-chapter edits it made: 64:64-65 N → N_ν; 45 Σ_IVP → Σ^IVP and Σ_(IVP/fut/past,r₀) →
  Σ^(IVP/fut/past)_(r₀); chapter 3 line 312 already right. For integration: chapter 65 defines its own Θ := δGk (rename
  edition-wide); chapter 45's κ (second fundamental form) shares a letter with chapter 46's gauge 1-form κ. Two
  chapter 46 items (sign in sec:s27-local; lem:s27-cover (c) omits Σ^past_(r_1)) sent to the S27 second fix.
- Proof C first reading (R-P-C): C2a correct (930 node coefficients, 23 cells, 15 peak rows exact; e_k outward-rounded;
  the source's e_k fall below the true values at k = 0, 2, 7, 10, 12); all 385 T-C261 entries exact upward roundings;
  S re-derived for any μ, h(ϑ) and zero-mean χ; D[n] below the source's at every order (largest ratio 0.435); no
  Cauchy estimate needs env smoother than C^14. Major: the cubic term of C_0·C_1 dropped at 487 (zero mean; cite
  lem:first-mean-forcing). Minors: the opening's dependence claim; rem:energy-one-sided vs (c); c and w doubled;
  Poisson summation uncited; lem:epsilon-one duplicates chapter 02. The C261 chain, e_k and the energy constant are
  used by no result: keep as proved results only if a planned chapter cites them, else drop. Fix running.
- S19 fourth reading (R4-S19): eq:iii-i-3-7 proved for ℓ_I < ½ with the failure at ½ explained; the survey sites hold.
  Major: 46:34, 487, 541 and 48:50 build Ω_* with ℓ = ½ and apply chapter 38 there; S27's smoothing lemma needs ½.
  Fourth fix: decouple the time-function parameter (½) from the class ℓ_I, plus a remark in S9. Nit: non-degeneracy
  in 𝒢⁺'s definition (213).
- Ch 3 fourth reading (R4-00-03): thm:main proof, ε_K clause with ε_K < ε_Υ, K = d_1 + 14, the slice
  φ_S(ψ_(S⁰)(Σ^IVP)), the chapter 48 paragraph, the envelope remark (c ≈ 1.3240873, ∫ = 105/128) and nit 18 confirmed;
  chapters 0-2 agree. Minor M1: thm:settling chooses ε_K before the data and r_♭ (chapter 60 fixes them first) and
  does not name the Tangherlini background of mass μ_end. Nits N1-N4. Fifth fix running together with chapter 60's S⁰
  (about eight sites).
- Proof E margins second reading (R2-P-E-margins): both Majors and the 13 other items repaired; bend sum exactly
  −0.0011595971 ≥ −0.0011596; μ ≤ 3.79033576 ≤ 3.79034; lens proof sound with R_p ≥ R_*; cascaded constants hold
  (0.1084602, |g′| 0.01569509); every Σ_τ0, Σ′ and seed row reproduces (worst cell −3.04218·10⁻⁴); row 99 right; C2,
  its marker and the interpolant clause gone. Minors: Σ_τ0 acausal below R_* for the lens's closing sentence; Rácz
  (4.22) (arXiv p. 13) into Appendix A with the complex-roots line. Second fix running (adds the Appendix A entry).
- Ch 63 first reading (R-63): issue-1 settled: k_P = 2k1 + 14 is needed (each s-derivative of F_p costs two angular
  derivatives, ∂_y^i ₂F₁ at 0 grows like l^(2i), sharp) and enough (K* unchanged), consistent with chapters 3, 8, 9.
  issue-2 is a real gap, also in the source: on the cut-off band ∂_t² of the true solution differs from the cut-off
  profile by −2P/g⁻¹(dt̃,dt̃) ≈ 6χ′r^(−11/2)G_9(v1); E_T[Z^k h_R] grows like |T|^(2a+2k−8) and diverges for every a in
  the window. It breaks Steps 3-5 of thm:own-continuation, hence prop:own-vacuum, prop:own-transfer,
  prop:own-uniqueness and thm:own-data as stated; the first four sections, thm:own-half-settling and a conditional
  theorem (assuming a continuation) survive. Forwarded to the cut-off proof project. prop:own-same-index-sets correct;
  three DLMF formulas exact. Minors include cor:own-p-order on Ω′ and lem:vii-1-1 used only through its proof. Ch 63's
  fix round waits on the cut-off proof project.
- S28 confirmed (R2-S28): the projection, transport through π_(g′), (5.11), (3.13), Theorems 3.6, 3.9, 5.9, Corollary
  5.11 and (8.6) quoted literally (checked against [CD03] page images); 𝒞 gone; "close to zero" is the source's meaning
  (Theorem 3.9 via Prop. G.1); the smallness restored in lem:s28-setting (b) and Appendix A; the Jacobian at every
  (m,0,0,0) matches in sympy; rem:v-3-4's sign right; n9 acyclic. Chapter 61 step (2) should bound C^(k_g+2) (the same
  right side bounds it). Open nits for integration: n10 (Appendix A, Theorem 3.6 gloss) not applied; k₀ has two
  meanings; a ψ-sign remark against [CD03] p. 25.
- Ch 65 written (W-65): keys for chapter 66: prop:np-10-2, prop:gd-2-1, lem:gd-2-2, thm:gd-2-3, gd-r2-1..7, 9..11, 13,
  gd-r3-1/2/4/5/6, gd-r4-1/2/3/4/6, gd-r5-1/2. States the t^(−1/2) rates only; chapter 66 must state the faster rates
  of the later amendments. NP 10.2 (v)-(vi) dropped (they serve only Hung's route). Lemma R4.1 (c) proved in general
  (the source computed one parameter point): its reader checks it. Notation: GD's K → K_V; the III.H cut-off χ^H_K;
  the augmentation row φ_*; its own Θ := δGk (rename edition-wide); ϰ_♯ cites eq:iii-g3-0-1, which S17 may still
  print as λ_♯ (check at integration). The word "Source" followed by a space trips the lint ("forcing term" used).
- Proof B fixed (F-P-B): five polynomial multipliers F_A, F_B, F_2, F_C, F_T in z = 1 − 2/r², weights positive by
  Bernstein coefficients (proofs/T-B.md, sec:tb-morawetz); l = 0 at |σ| ≥ 1 by chapter 70's bound above the barrier.
  Source → edition: B_0 at 0+, 1, 3, 10: 164.5, 183.5, 275.2, 725.0 → 70.17, 7.82, 1.33, 0.38; X_0(3) 158.57 → 23.36
  (≤ 83.85 on 0 < |σ| ≤ 3); summed H¹ constant 184.82 → 179.26; unweighted 986.4 → 568.55; B_l(3), B_l(10) (l ≥ 6)
  19.22, 26.80 → 11.36, 25.56; rows A, B, C, S4, S3, T2 and the 15/16 transfers at or below the source. Not reached:
  C256's decaying point values (σ = 3 to 96); prop:band-points (B2) is the edition's statement there. B2's 283.06,
  305.31, 308.46 stand. B̃ is now B*_l of prop:morawetz-harmonics; K_l → J_l. lem:morawetz-identity now reads "a
  solution, with u and u′ locally absolutely continuous, of −u″ + (V − σ²)u = f (almost everywhere)", allows any
  bounded φ, and proves R(σ)f is one: B2 must use exactly this wording. Chapter 70 must be re-merged with the fixed
  proof B (its corollary, master-operator and large-frequency results changed) and lem:morawetz-complex must add the
  hypothesis |φ| ≤ 1. The figures 202.6 and B_0(3) 585.53 recorded earlier in this file are superseded by these.
- Ch 3 fifth fix with chapter 60 (F5-00-03): thm:settling now fixes l5, μ0, A, env, τ0, then the theory at b₀ = (μ_end, 0),
  r_♭ ∈ (0, ½√μ_end], ℓ0, ε_K; R and Ω′ depend only on ε and r_♭, λ1 and δ moreover on ε_m; thm:settling-precise in
  the same order; its (Ex1)-(Ex2) argument shortened to "step (4) imposes them" (the reader checks it). N1-N4 applied
  (χ dv ⊗ dv ∝ env²; thm:data's threshold and items 6-7; α for ε; r_0 → r_♭). Chapter 60 carries S⁰ at 11 sites:
  slice φ_S(ψ_(S⁰)(Σ^IVP)), φ_(−S,−S⁰)⁻¹ = φ_S ∘ ψ_(S⁰); 𝒟_0 := 𝒟_(0,0) kept (chapter 62 cites it). R4 §3 notes 3-5
  concern other chapters (integration).
- Proof E margins second fix (F2-P-E-margins): the lens corollary states Σ_τ0 acausal, proved via e^ψ f < 1 along the
  slice (below R_* from the proof of prop:bg-slice); new Appendix A remark rem:std-racz-characteristic quoting Rácz
  (4.19), the common-symmetrizer definition (p. 12), (4.22), (4.23) (p. 13) of arXiv:1508.01810v3; P computes the roots
  ξ_n = ±i|ξ_S|√(κK^l_l)/K^l_l and shows no common symmetrizer exists. For integration: add rem:std-racz-characteristic
  (and the older Rácz keys) to OUTLINE.md; [Rac16] in the references gives only the journal version while Appendix A
  cites arXiv pages (add the arXiv identifier and version). P now also cites eq:bg-chart. 8 pending-marker lines remain
  in P (forward references; the reader checks each).
- Ch 62 third reading (R3-62): earlier findings fixed (V in the cone of dτ; lem:interior-chart with the 25C_Jλ bound and
  the inverse by Neumann series; R2 nits 3-10); every computation incl. the Ricci formula checked; citations from
  chapters 1, 3, 48, 60, 63 and P-G-far satisfied. Minors: "the (common) domain of dependence" overclaims
  lem:interior-one-spacetime (glues along Σ, maximal common development U); m := μ_end r⁻² used where v < v_end
  (use μ(v)r⁻²; bounds need only 0 ≤ m ≤ 1/400). Nits: [BGP] for "connected"; λ_1 (lem:vii-1-1) vs λ1; J unnamed; ε
  doubled. Third fix running.
- Proof C fixed (F-P-C): the C261 chain, the e_k, the energy constant, prop:stage-zero-bounds and part of
  lem:lambda0-point dropped (cited by nothing; chapter 86 needs only the λ0 norms; the energy constant served only the
  M_22 a posteriori estimate, class (c)); T-C261.md and T-C.md deleted (recoverable at 85478dd^); P-C 854 → 238 lines;
  no value changed. Envelope constant renamed c_e (tied to chapter 03's c); Poisson summation stated and proved from
  Fejér's theorem; lem:epsilon-one replaced by chapter 02's items (i)-(iii). S is now only chapter 08's
  lem:first-mean-forcing (any zero-mean χ; the report offers an optional sentence for chapter 08). Follow-ups:
  proofs/P-F-edge.md line 9. The earlier report to the author that the source's e_k are rounded down stays true of the
  source but no longer concerns the edition, which states no e_k.
- Ch 80 written (W-80): 1,240 lines, 70 crosswalk rows, no markers; exports part:further, ch:two-dusts, thm:two-dusts;
  defines sec:two-dust-background and lem:two-dust-identities (for proofs E). thm:two-dusts carries the full theorem
  (E₂ is thm:two-dust-uniform; OUTLINE to be updated); item 6's conditions on μ0 restored with the equality case; the
  source's mixed gauge symbol sign corrected (+e^(−2σ)n1n2 for B_g); twelve programs replaced by derivations, twobg5
  and twodomainx5 kept as Numerical observation remarks. Notation: σ, 𝒜, ℬ, 𝒞_in, 𝒞_out, 𝒩₂, θ1, θ2; proof E's s, α
  and 𝒩 must follow on merge into chapter 83.
- S26 second fix (F2-S26): thm:iv2-2-4 kept for every k (chapter 46's thm:iv3-2-1 relies on it); Step 4 split: j ≥ 5 by
  Moser, 2 ≤ j ≤ 4 by Leibniz (new eq:iv2-2-5-low, constant from the H⁸ bound of h); eq:iii-c1-2-2 at k = 0 repaired by
  no-tame-term clauses added to lem:iv2-2-2 (s ≤ 3) and lem:iv2-2-3 (m = 3); thm:iii-c2-3-1 assumes ‖h_j‖ in H^(k₂)
  below ε₂, k₂ = 2N_NM + 2 = 308, and proves h_S exists, is unique, with a threshold uniform in small S; four nits.
  Suggestion for chapter 46: lem:s27-translated-exterior (c) could add "pull-back bounded, uniformly in (S, S⁰)". The
  fixer found two further gaps at k ≥ 7 (an unstated interpolation inequality; two commutator bounds without tame
  terms) and is adding them before the confirming reading.
- Cut-off project (P-I-cutoff): issue-2 confirmed a third time (G_9(v1) independent of v on the band gives forcing
  −3χ′r^(−11/2)G_9(v1); E_T[Z^k h_R] ~ |T|^(2a+2k−8); flat 4+1 model slope −3.5 vs −4.5). Repair: beyond the band the
  data are g_b0 + Σ + Σ′_J, J ≥ 2k1 + 7; new lemma: after the shell each G_k is a polynomial in v of degree ≤ k/2 − 2
  whose weight > −4 parts are Σ's Taylor coefficients, so Σ′_J is homogeneous of degree ≤ −4 and the band mismatch is
  O(r^(−(J+1)/2)); |Γ^α h_R| ≤ Cr⁻⁴, |∂Γ^α h_R| ≤ Cr⁻⁵ uniformly in T; cap ≤ C|T|^(2a−6); Step 4 at every order with J
  per order, uniqueness makes the limit independent of J; no sourced Σ_4, no larger K*. Chapter 63 replaces lines
  648-653, 660-663, 682-688, 738, 784-786, 800-809, 852-857 and drops the issue-2 marker; proof G changes
  prop:far-window's initial-slice hypothesis. Separate defect reported: lem:own-exterior's tail bound (L² part ~ϱ⁻⁴)
  fails for a > 2 (the reader checks it). Independent reader running before the chapter 63 fix round.
- S4 second fix (F2-S04): all 5 minors and 8 nits; the cut-offs section rewritten (auxiliary operators truncated near
  the diagonal by [Hin26d, Lemma 3.42, p. 51] and placed in the carriers with explicit room; χ_* needs no margin; nested
  inner cut-offs h(χ), h = 0 near 0, h(1) = 1, need no room). Lemma 4.1 changed only in (iii): "for every w ∈ H^(K′)".
  Chapter 25's analogues (lines ~168, 211, 231) must drop "carried by χ" (the S6 two-sided update, after the S4 reading).
- S29 second reading (R2-S29): the translation Major fixed (g_(p⃗), V⁰, ġ⁰ = −ℒ_(V⁰)g through thm:viii-2-2, lem:s29-g-on-n,
  cor:viii-2-3, cor:ix-2-3; composition order, signs, derivatives of κ rederived); Θ(k) → −Υ̇⁰(k) sign right (exact
  check); prop:viii-1-2's principal part ½□_g with symbol +½g⁻¹(ζ,ζ). Minor: lem:s29-g-on-n glues only across smooth
  hypersurfaces but the cover has edges inside 𝒟 ({r = r_1, t_IVP = 0}). Nits: (L) at 13; lem:iii-b-3-9 for K's sign
  at 483; 241; 183; a factor 2 with lem:ii-f-1-3. Second fix running. Chapter 46 (in flux): lem:s27-cover (c) omits a
  past-slab boundary piece and the backward problem, and sec:s27-local's symbol sign (both already sent to the S27 fix).
  Chapter 45: prop:iii-c2-4-1 uses κ = −g(∇_Xν, Y), opposite to lem:iii-b-3-9 and chapter 48's K (sent to the S26
  fixer). Chapter 64: N → N_ν at 64, line 84 restrict to r > r_♭ (sent to the chapter 64 fixer). Chapter 65: ġ_0 →
  ġ_(p⃗′) as in chapter 48, "S′ = 0" → "S′ = S⁰′ = 0", N → N_ν, and Θ attributed to sec:ix-0 (for its fix round).
- S11 second fix (F2-S11): (E1), (E2), (EE), lem:iii-a-1-4, lem:iii-a-1-5 for ℂ^(N_E)-valued functions (componentwise
  spaces, matrix symbols, ellipticity as invertibility, bundles framed as in sec:i-a-1-2); (EE) now quotes
  [Shu92, Appendix 1, Lemma 1.4, pp. 69-70] (taken from the numdam PDF through a fetch connector) in place of
  [Hin26d, Proposition 3.55 (3)]; (E2) every Laurent coefficient maps H^s → H^(s+m), inverse uniformly bounded on
  compact pole-free sets; Theorem 3.21 at p. 38; w → v; 𝒩 → 𝖭 (S11), 𝒩 → 𝔑 (S12); S12 nits 1-6. Crosswalk:
  def:s11-parameters and rem:s12-convexity-sample added, lem:s12-ks-domain removed. For Appendix A (small round): add
  [Shu92, Appendix 1, Lemma 1.4] with its statement and pages. Open in other chapters (R2-S11-S12's O items): O2 at
  S14:2399, O3 at S24:640, O4 at S13:1149-1151 (details in F2-S11.md); for those chapters' next rounds.
- Ch 3 and chapter 60 fifth reading (R5-00-03) CONFIRMED after the coordinator applied both minors in the reviewer's
  words: 03 "Beyond the boundary" now names r_♭ := ½(√72 μ_end l5²)^(1/4) and "between r_♭ and R"; 61:252 "fixes before
  them". Checked: quantifier order and dependences match chapter 60; (Ex1)-(Ex2) imposed by step (4); S⁰ at the 11
  sites agrees with chapters 46 and 62; N1-N4. Nits for integration: 60:264 and 60:283 cite lem:iii-b-5-1 and
  lem:iii-i7-1-1 (a) beside eq:s27-motion for ψ_0 = φ_0 = id and the inverses; chapter 60's A means amplitude and spin
  (name the spin A_b or add a notation sentence); optional "depending only on ε and on the quantities fixed before it".
  Still open elsewhere (R4 §3 notes 3-5): λ1 against λ_Ω in chapters 5, 6, 9 (06:22-24 "λ1 := min(1, δ0)/10"); the
  translations at 01:61; env_C in chapter 86. Chapter 60 has two λ_1 (lem:vii-1-1 and thm:settling-precise), consistent.
- Ch 62 third fix (F3-62): the lemma's wording; m := μ(v)r⁻² with 0 < m ≤ μ_end r⁻² ≤ 1/400 on r ≥ 4R; nits. Not
  edited, for chapter 63's fix round: 63:670-672 writes μ_end (as 𝔪) where g0's coefficient is μ(v), on sets reaching
  v < v_end (inequalities still hold; notation only).
- S22 third fix (F3-S22): cor:iii-i15-2-10 states and proves C‖G‖_(𝒴^♮(α−ε)) + C(‖h‖ + |p⃗|)‖u_0‖_(w) + CΣ|W_ν| with C
  uniform in b (the Σ|W_ν| term beyond R3's proposal, bounded by C‖F‖ at both application sites); the remark after
  thm:iii-i12-3-1 reduces it to C‖F‖ at b_0; chapter 44's def:iii-i15-2-3, lem:iii-i15-2-4, prop:iii-i15-2-5 Step 3
  and cor:s25-tame's proof (592-594) bound by G plus the solution term, the A_k bound unchanged so chapter 46's citations
  keep their strength; four nits. Fourth reading running.
- Proof E margins CONFIRMED (R3-P-E-margins): Σ_τ0 acausal proved; 3.3·10⁻⁴ rad fully proved; Rácz (4.19), the
  symmetrizer definition (p. 12), (4.22)-(4.23) (p. 13) match arXiv v3 word for word, (4.22) an exact factor of the
  characteristic polynomial by (4.20); roots and the no-symmetrizer argument right. [Rac16] already lists
  arXiv:1508.01810v3 (no fix). Nits at merge into chapter 83: add "e^ψ f < 1" to prop:bg-slice and thm:bg-margins (c)
  in P-E-background and cite it directly; P:38 "symmetric positive definite"; optionally quote (4.20) or one
  factorisation line; resolve the marker at P:17 to lem:bg-identities and eq:bg-field (chapter 80 now defines them);
  OUTLINE.md: one line exporting the Appendix A std- keys (exact text in R3-P-E-margins). The pending Rácz-formulas lemma
  must include the ψ ≠ 0 forms of κ, K^l_l, N_κ (checked) and the Γ/E² identity.
- S14 second reading (R2-S14): all seven Major repairs hold (r_♭ throughout; the general S formula checked on a random
  metric with a failing control; strip finiteness; θ-bounds; M + 2N = D M_(−v) D with ϑ_in; the Tangherlini table
  coefficient for coefficient); lines 302-305 are P-A3's own consequence (P-A3:194-196). Minors: 674's reason (vanish at
  η = 0, not O(ρ²)); 355-356 and 469-471 the e = 0 trace and determinant are limits not shown to exist. Second fix
  running (also O2 at 2399 and proof A's 2557, 2541 items). Other files to update: S27:1276, 62:52, 71:74 (details in
  R2-S14.md) at their next rounds or at integration.
- Ch 71 written (W-71): 503 lines, 32 labels, 32 crosswalk rows; exports thm:loss-d, ch:explicit-constants. Proved:
  d as the number lem:iii-j2-1-2's rules assign (def:ec-accounted-loss); closed forms of the elementary losses; R >
  2.6532×10¹⁵ rounds so d > 5.306×10¹⁵, and d > 7.959×10¹⁵, N_NM > 1.671×10¹⁷ when ϑ_in ≥ 0; δ ≤ 2^−(32d+9), λ1 < δ,
  log₁₀ δ < −7.666×10¹⁶; the test-function principle. prop:gap-sums and rem:gap-sums merged here from P-A: do NOT merge
  P-A's copy of that section into chapter 33 (labels would be defined twice). Open: [[pending:issue-1]] (ϑ_in ≥ 0 for
  N_tf(L_b, ±1) only computed in the source) and the upper bound d ≤ 46,236,517,538,883,361 (N_NM ≤ 9.710×10¹⁷), now a
  Numerical observation; chapter 3 lines 347-349 cite thm:loss-d for "explicit upper bounds" and must change unless a
  written upper bound is proved. Proof project running on both. Other observation remarks: the figures at the source's
  weights, root-avoidance checks, the constants 2.81 and 3.94, trapped-set data, η < 16.48γ_C^(−1/2), resolvent lower
  bounds from degree-159 test functions (ratios to prop:band-points 19.8 to 93.5). lem:ec-closed-forms (f) to check
  against chapter 36.
- Ch 64 fix (F-64): six minors and 13 nits: set limited to r > r_♭; int N clause kept and proved (no use needs it);
  XΦ only for T^a, rotations via ΣĚ(Ω_iΨ) = λĚ and Σ_ijĚ(Ω_iΩ_jΨ) = λ²Ě (thm:rwg-2 Steps 1-3 rewritten); T² on the cone
  from T = (𝒱∂_𝒱 − 𝒰∂_𝒰)/r_h; uniformity in l with 𝔭Φ as a jet; the density step for lem:np-10-1b (b). Renames in
  chapter 64: K → K̄, 𝔪 → 𝔭, τ → 𝓉, ω → 𝔷, t_s, Y_H, v_Σ, 𝔠, ϱ, N → N_ν. ṁ kept (chapter 3's μ̇ is out of line: rename
  at integration). Chapter 65 needs K → K̄. Confirming reader running.
- S27 second fix (F2-S27): Major lem:s27-below (iii) reproved by g_(b₀)⁻¹(dt_*, dt_*) ≤ 0 with exact Tangherlini values;
  chapter 24's gluing constant renamed C_g and taken ≥ max(4(r′₀+1), 32, 16R₁). Minors: (1) on all of 𝒟 by chapter 45's
  argument; ℐ⁺_♮ on the slab; (L) needs k ≥ 4, Duhamel, unique in H² (not H¹); (3) a modulus ω_k; (C3) item (iv);
  two-sided boost-move bound; sign of ½□; Σ^past_(r₁) in lem:s27-cover (c). Chapter 48 cites changed statements
  (lem:s27-cover (c); (L) in H²; thm:iv3-2-1 now k ≥ 1; lem:iii-k-2-2 (d)): update at S29's next round. Chapters 3, 60:
  no cited statement changed. Open: chapter 38's class at ℓ_I < ½ against chapter 46's time function at ℓ = ½ (S19
  decoupling round running). Third reading running.
- Proof B CONFIRMED (R2-P-B): 0M 0m 7n; every weight polynomial and all 2,643 Bernstein coefficients of T-B recomputed
  in exact arithmetic; lem:morawetz-identity's new form holds; five chapter-70 citations match. Nits at re-merge:
  T-B:7 "five significant digits" (integers printed to the unit); "product" columns are rounded unrounded products;
  part (c)'s 61.37, 129.87, X_0 = 26.71, 23.72 come from the rows' constants, not the two-decimal table; f for both
  1 − 1/r² and the right-hand side (chapter 70 writes F); M := at line 90 uses a reserved letter; part (c) does not say
  Σ u_l converges; R(σ) for other potentials needs only a real integrable V, cite lem:rb-flux for 𝒲 ≠ 0. Re-merge:
  chapter 70's lem:morawetz-complex must add |φ| ≤ 1; rem:rb-multiplier-observed reads oddly against the proved values;
  P-B2 line 319 B_l → B*_l. Re-merge waits for the chapter 70 proof project (same file).
- S26 addenda (F2-S26): lem:s26-interpolation added (smoothing operators of thm:iv2-3-1 (i); s₀ = 8, b = 9, a = k + 2)
  for ‖u₂‖_(H⁵) carrying ‖h‖_(H⁹) at k ≥ 7; thm:iv2-2-4's estimate written step by step; tame terms in
  eq:s26-commutator and [L, χ]; prop:iii-c2-4-1 sign error real: lem:iii-b-3-9's convention, letter k, k̃ term flips;
  prop:iii-c2-4-2 writes k^BL. Chapter 48 lines 128 and 133: drop "κ̃ there" (add to S29's next round). Third reading
  running.
- Chapter 70 markers (P-K70): all three written. Roots 1.0000747438, 1.0000029324, 1.0000169224 bracketed by
  lem:rb-roots-point (exact Taylor coefficients at 2, sign changes; independent of the pending l ≥ 1 part of
  prop:np-10-54). The printed least singular values were rounded to nearest, not up, and cannot be proved as printed;
  proved replacements by prop:rb-quasimode-point (six integer test vectors) with lem:rb-indicial-explicit:
  3.1412·10⁻⁶ → 3.1413·10⁻⁶, 2.6180·10⁻⁷ → 2.6181·10⁻⁷, 1.4955·10⁻⁶ → 1.4956·10⁻⁶, 0.020 → 0.0204, 0.015 → 0.0149,
  0.012 → 0.0121 (3.81·10⁶ unchanged; no other citation). lem:rb-m33: M₃₃ = −(γ_C a r − 1)/r³. FOR THE FINAL REPORT
  TO THE USER: the source's singular-value bounds were rounded the wrong way. Citation of formulas inside chapter 30
  proofs: allowed as "the formula [[eq:...]] in the proof of [[lem:...]]" when labelled; unlabelled ones restated in
  chapter 70. Re-merge of proof B running (also crosswalk rows for the seven new labels).
- Proof D2-D4 reading (R-P-D234): NOT CONFIRMED 1M 3m 8n, mathematics right. Every row of both tables and the 1,160
  field constants recomputed exactly; the closed-form residual matches a direct 5D Ricci computation; 2.4143e-3 ≤
  2.42e-3, 3.728e-5 ≤ 3.73e-5, B* 2.978e-4 ≤ 2.99e-4, B2 ≤ 4.912e-4 hold. Major: the 1.3e-7 widths and five named
  intervals (and the lower bounds 2.414 / 2.387 / 2.347 / 1.095e-3) are printed nowhere. Minors: headers say "smallest
  integer" (tables used a larger centre radius; 1,231 point and 30,853 box rows would be smaller by the text's rule);
  enclosure order leaves cosh/tanh, ϑ, R⁴, 1/Ω² open; R > 0 cited to a lemma that assumes it. Fix running.
- Ch 62 CONFIRMED (R4-62, 0M 0m 4n). Coordinator applied all four nits: prop:interior now fixes l5, μ0, A, env, τ0,
  takes r_♭ = ½q_end and lets the other constants be chosen in thm:settling's order; g0 = g_(b₀) on {v ≥ v_end, |x| ≥
  ½r_♭}; rem:interior-one-spacetime's U is the maximal common globally hyperbolic development; stage index m → j at 533.
  Ch 1:144-145: "with its inner radius taken as half the radius of the curvature boundary after the shell" (the
  abstract keeps its summary). Ch 63:64, 670-672: μ(v)/r² for μ_end/r² (inequalities still hold) — at ch 63's fix round.
- S19 fourth fix (F4-S19): time function with exponent ½; class parameter ℓ_I ∈ (0, ½) separate; chapter 28's
  rem:ii-f1-7-4 proves thm:ii-f1-1-1 for any time-function exponent in [ℓ_I, ½] under one smallness condition (the two
  compared only in lem:ii-f1-2-6 (b)); 12 citations from 46, 48 hold; optional note at 46:95 (ℓ_I there is the
  b-weight). Fifth reading running on 38 and 28.
- S29 second fix (F2-S29): edge gluing written in lem:s29-g-on-n (i)-(ii); nits. Its note on the same edge gluing in
  chapter 46 sent to the S27 third reader. Third S29 fix waits for R3-S27's list of chapter 48 lines.
- Ch 65 reading (R-65): 0M 8m 15n; Lemma R4.1 (c) general proof holds; NP 10.2 (v)-(vi) rightly dropped. Fix running.
- S11/S12 third reading (R3-S11-S12): S12 CONFIRMED (0.80 → about 0.79); S11 two minors (poles of N(A,·)⁻¹ are the
  indicial roots — used by S13:1862, S14:2399, S17:1622; H^∞_loc claim) and one nit; [Shu92, App. 1, Lemma 1.4, pp.
  69-70] quotation verbatim. Third fix running (also labels for chapter 30 formulas cited by chapter 70).
- S4 third reading (R3-S04): 0M 3m 3n; all R2 findings fixed; the three cut-off claims hold against [Hin26d] v1
  (Lemma 3.42 quoted correctly; χ_* needs no margin; h(χ) needs no room); Lemma 4.1's change satisfied (Proposition 5.3
  proves (iii) for every w; d₀ fixed before k). Minors: add (S15) for the truncation results (Prop 2.3, (2.3)/(2.5),
  Lemma 3.42 p. 52, p. 75); Prop 9.2 "do not accumulate" false (they grow by each level's room); name χ_1 in Prop 9.2.
  Chapter 25 changes listed (l. 168, 205-206, 211, 221, 231, 235-236, 241, 278, 393-395, 508-512, 716-721, 1030).
  Chapters 28, 29, 38-43 need nothing. Third fix running on S4 and chapter 25 together; Appendix A (S15) entry text to
  be carried at integration if the fixer lists it.
- S22 CONFIRMED (R4-S22): cor:iii-i15-2-10's Σ|W_ν| term right and needed; both application sites bound it by C‖F‖
  through |p⃗′|. S25 (chapter 44): R3's I1 fixed, induction bound proved, A_k bound in its old form, chapter 46's
  citations keep their strength; minors: ‖δG′‖ ≤ Cη|δW′| needs the motion coordinates to move by O(η) (pre-existing;
  uniqueness at α_1); line 595 starts "+ A_k" (pandoc drops the sign). Fix running (also ch 41's two nits).
  INTEGRATION CHECK: before assembly, scan every chapter for wrapped lines starting with "+ ", "- ", "* ", "> ", "#",
  "=" or "|" in running text (lint.py should gain this check).
- Proof C confirming reading (R2-P-C): 0M 2m 3n. The drop is safe: no remaining statement and nothing chapter 86 must
  state cites a dropped label or number; every kept number holds exactly except 16.127552² = 260.0979335… (printed
  ...337); rem:lambda0-norms-c's "upper end of c_e enters nowhere" is false. Nits: K clash, φ1 and s double meanings, ζ
  for cos 2ϑ. Chapter 08's lem:first-mean-forcing needs no sentence. Follow-ups in the fix: P-F-edge:9 "c_e the constant
  of [[eq:envelope]]"; chapter 03's remark cites lem:envelope-constant (b). Earlier INTEGRATION lines about C127-C129,
  C259, C261 (proof C's e_k and the energy constant) are superseded by this entry. Second fix running.
- Ch 80 reading (R-80): NOT CONFIRMED 1M 4m 11n. Every identity checks (Ricci, Kretschmann, (i)-(vi), chart,
  commutator, trace identity of eq:two-dust-cpw by computer algebra; transport, slice, horizon, mass by hand);
  departures (a)-(e) correct; B_g mixed symbol +e^(−2σ)n1n2 confirmed. Major: gauge hierarchy (a) claims O(λ²) where
  two families give −λe^(−4σ)[χ_out] + O(λ²) (conclusion holds). Minors: n = ±2 in stage zero (d); K and F clashes;
  lem:linear-wave needs g0 around the domain; cone reparametrisation for P-E's gauge e^(2s) = 1/2. Fix running; P-E
  files may need symbol updates after the K/F renames.
- Ch 82 written (W-82): 912 lines, 62 labels, exports thm:vlasov. Non-vacuity proved with a separable family on
  Tangherlini (Jacobian ≥ 1, b = 0.36, δ = 0.265); the source's family (grid-checked only) is a Numerical observation
  remark. Choices: injectivity in the label; amplitude F with q = F²; n dusts (N the stage count); labels α ∈ S¹.
  Open: (V3) uses chapter 7's symmetrizer derived for small γ_rA. Pending keys: 9 to chapter 80 (labels mapped in
  W-82), 2 to chapter 81 (class-augmented-system, class-adapted-domain). Independent reader running.
- Ch 81 written (W-81): 965 lines, 56 labels; exports thm:class-stability (N′), also thm:class-kato,
  thm:class-kato-stability (K′). Five computations replaced by written derivations; two Numerical observation
  remarks. [[pending:issue-1]]: linear symmetric hyperbolic existence with A⁰ ≠ I (proposed repair: S = (A⁰)^(1/2)
  reduces to A⁰ = I, then [IT20, Proposition 3.8] and commuted derivatives). cor:class-two-dust (N′1): the outgoing
  packet not reaching R = a is now a hypothesis (the source used a computed example) — check chapters 3, 60, 82. Ch 82's
  two pending keys class-augmented-system, class-adapted-domain to map to chapter 81's labels at integration.
  Independent reader running.
- Ch 64 CONFIRMED (R2-64): all six minors and thirteen nits of R-64 fixed correctly; the one new minor ([HKW18]
  Lemma 11 and Theorem 16 quoted without their hypotheses) applied by the coordinator in the reviewer's exact words.
  Nits for integration: ϱ and ρ near each other; σ names two numbers in one sentence of the remark; lem:rwg-cone writes
  both L_i and L_(Ω_i); the ψ / F(r) / g(𝒰) clashes deferred by F-64. Chapter 65: K at 65:33 and about twenty later
  lines, ω at 65:343 for 𝔷 — sent to the chapter 65 fix round.
- S14 second fix (F2-S14): both minors and the nits applied; O1, O2, O4 and 2635 ("has real part at distance");
  four lint hits are labels in proof A not yet merged (prop:s14-scalar-every-h, lem:s14-delta50,
  cor:s14-eps-ind-point); crosswalk notes for np-10-54, np-10-14, np-10-52 say "pending" (update at integration).
  Third reading running.
- Ch 71 proof project (P-L71): issue-1 proved (lem:ec-theta-in: p_in − (S + S^∗h) = −2Re_h(A + S); for 2L_b a kernel of
  dimension ≥ 5; ϑ_in ≥ 0 in every fibre inner product, ℓ_tf ≥ 1); thm:loss-d (ii) d_acc ≥ 3R > 7.959×10¹⁵, N_NM >
  1.671×10¹⁷; prop:ec-delta-cap log₁₀δ < −7.666×10¹⁶. NO explicit upper bound on d is provable as the edition stands
  (the forward solution operators' loss D_0 + D_1 + d′ + d″ + 6 has no value; the source's FWD ≤ 877 rests on an order
  count the edition does not carry); rem:ec-integer-bound stays a Numerical observation. FOR THE FINAL REPORT TO THE
  USER: the source's "explicit upper bound d ≤ 46,236,517,538,883,361" is not proved and is reported as a numerical
  observation. Chapter 3 (coordinator, exact text from the report): "explicit lower bounds … and, through them, upper
  bounds for δ and λ1". Crosswalk: lem:ec-theta-in, eq:ec-theta-in, eq:ec-theta-in-l added; thm:loss-d,
  lem:ec-closed-forms, rem:ec-other-losses notes amended (35 rows, labels in order). Notes outside: chapter 34 line about
  170 (Y := ḡ⁻¹dt̄ with ρ in one term only — nit); rem:ec-other-losses's "2" for background terms is tame with loss
  max(2, d) (minor, affects only an upper bound). Independent reader running.
- Ch 66 written (W-66): 1,118 lines, 53 labels; exports thm:harmonic-rate (t_*^(−α), α < min(p_0, 3/2); t_*^(−1+ε)
  for a change of mass beyond a ball; t_*^(−3/2−κ) for compact data with an exact t_*^(−2) l = 0 term; l ≥ 2 always
  t_*^(−3/2−κ), κ < δ_♯). cor:hr-compact-rates and cor:gd-r5-3 supply chapter 65's rates. Issues: Def R8.1's equality
  with ran Π_≥2 replaced by the inclusion (Π_cl := Π_G(1 − Π_0)); Cor R7.7 (b) via thm:ix-2-2 and lem:gd-1-4 (c); p_0
  as "every p < q − 1". Notation: K for r⁻²dv² (chapter 64 writes K̄) and −Υ̇⁰ for Θ — to align with chapters 64/65 at
  the fix round. Independent reader running.
- Proof C second fix (F2-P-C): 75 exact checks pass, one decimal was wrong (260.0979335…). Minor 2 by repair (b):
  lem:lambda0-point (c) is V − q_end ≤ τ_end ≤ V − q0 (no bound on c_e); (d) and X* ∈ Ω rest on (c); monotonicity in a
  new item (e). Nits: K → α*, phase ψ with φ1 the phase shift of thm:approximant, ζ = cos 2ϑ. Follow-ups applied:
  P-F-edge:9-11 "c_e the constant of [[eq:envelope]]"; chapter 03 line 64 cites lem:envelope-constant (b) (a proof-file
  label: --chapters reports it undefined, the joint run resolves it; resolves at assembly). Third reading running.
- Ch 84 written (W-84): 1,248 lines; exports thm:layer, cor:layer, lem:layer-interpolation and the new
  cor:layer-interpolation-band (ε_c² ≤ C λ^(−1/8) E² at m = 56c; ≤ C λ^(−1/8) m0 for m ≥ 84c). FOR THE FINAL REPORT TO
  THE USER: the source's λ_L < 2.71·10⁻¹² rested on Chebyshev nodes, the Duffin–Schaeffer inequality and a certified
  bound on M_1456, none carried by the edition; the edition proves λ_L ≤ 10^(−430) at the numerical point instead. L.12
  now proved for every K ≥ 6 (source: ledgers on grids). L.14 dropped (conclusion withdrawn; reader to say whether its
  numerics stay as a remark); Remark E.6's heuristic dropped (the source shows it false). Notation: ν for K, d_1, β_2,
  β_Φ, 𝒯, 𝔖, g0°. Independent reader running; chapter 85 writer launched on its exports.
- AUTHOR'S DIRECTIVE (2026-11-13): "Cannot be proved: the source's explicit upper bound d ≤ 46,236,517,538,883,361.
  It needs the loss of the forward solution operators, which the paper shows exists but never evaluates. - if it
  exists then our task is to evaluate and then prove it, so the paper may include it." Two proof projects: P-U71-forward
  (evaluate D_0, D_1, d′, d″ and prove d_FWD ≤ N from chapters 26-28; statement strengthenings listed for those
  chapters) and P-U71-assembly (every elementary loss, step counts, index-set log orders, the background-term loss
  max(2, d), and the explicit integer bound on d and N_NM). Chapter 71 and chapter 3 change when they report.
- S27 third reading (R3-S27): second Major fixed (exact Tangherlini values; C_g consistent in 24, 26, 46 and all
  citing chapters); all six R2 minors and coordinator items and eight nits fixed. NEW Major (also in the source IV(3)):
  thm:iv3-2-1/thm:iv3-2-2 take independent data on Σ_c and Σ^fut meeting at E′; repair: slab problem on Ω_ext ∪ 𝒦⁺ ∪ 𝒮
  with data on Σ^IVP only (as chapter 65) and edge compatibility in (L). Minors: edge gluing lemma (chapter 48's method);
  forward uniqueness region beyond R_ν; (L)'s tame form, uniformity and trace orders. Chapter 48 needs four edits (128,
  133, 182-183, 197-198); chapter 71 lines 437-439, 447, 455 use a linear A from lem:iii-k-2-2 (d), which now gives only
  ω_k. Chapters 3 and 60 need nothing. Third fix running; the S29 third round waits for it.
- Ch 83 written (W-83): 2,612 lines; proof E (background, margins) and tables merged with all markers resolved and the
  reader nits applied; lem:racz-split-formulas (ψ ≠ 0, N_s√G = 1, vacuum form); thm:charge-identity proved pointwise
  with both boundary terms; exports thm:charge-sign. Pending: thm-class-kato-stability → chapter 81's
  thm:class-kato-stability (map at integration); issue-1 twice (seed continuity of the correction: [CS06] is 3D only;
  proof project P-K83a); computational-1 (tensor-type charge identity) and computational-2 (scalar-mode identities)
  and the sliver of region III beyond R = 1.861 (proof project P-K83b). Independent reader running.
- S11 third fix (F3-S11): (E3) stated and proved in sec:iii-a-1-1 (poles of N(A,·)⁻¹ exactly the indicial roots;
  bijective off spec_b(A); finitely many roots per strip; a version with a commuting projection Π). Citing sites to
  update at their rounds or integration: 32-s13:1862-1863 "(E3) of [[sec:iii-a-1-1]]" with Π the projection onto the
  types of f_(m_*); 33-s14:2465-2471 cite (E3) in place of the local proof; 36-s17:1621-1623 "(E1)–(E3) of
  [[sec:iii-a-1-1]]"; optional 36-s17:1307-1308, 43-s24:640. S12's 0.80 → 0.788 (infimum 0.78811, not attained). New
  label eq:s11-box-tensors for chapter 70 (sent to the chapter 70 re-merge). Fourth reading running.
- S19 fifth reading (R5-S19): crux holds; minor: ϵ_G must cover {t_* ≥ ½} (collar outside Ω); nits: mass-term sign at
  38:711; renames G → 𝖦, C_♭ → K_♭, ε_♭ → η_♭ (clashes with chapters 46, 48, def:s11-parameters, 27, 35); (B) users list
  adds ch:s06 and lem:ii-e-4-1 (a). Optional note at 46:98 (ℓ_I there is the b-weight). Fifth fix running.
- Ch 70 re-merge (F-70-merge): confirmed proof B in place of the pre-fix copy; seven R2-P-B nits; B2 band fix in both
  files; T-B tables as sec:tb-morawetz beside sec:tb2 (crosswalk: "to transfer to Appendix B"); lem:morawetz-complex
  requires |φ| ≤ 1 (scaled form for |φ| ≤ p_φ); every master potential ≥ 0 proved; rem:rb-multiplier-observed reworded;
  F_2 → Θ_E, p → p_φ; summation in cor:morawetz-one-derivative (c)-(d) written. Chapter 30 citations
  [[eq:s11-box-tensors]] and [[eq:iii-b-6-5]]; Gauss formula and chapter 34's composition rule restated with derivations.
  Open: lem:rb-horizon-exponents cites content inside the proof of lem:iii-f2-1-1 (chapter 34) — reader A to settle.
  INTEGRATION CHECK: label keys must be lowercase — sec:tb-morawetz-mM in the proofs files, eq:bondi-calS at
  02-setting.md:568; lint.py should reject uppercase keys. Two readers running on chapter 70.
