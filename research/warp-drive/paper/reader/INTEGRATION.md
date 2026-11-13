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
