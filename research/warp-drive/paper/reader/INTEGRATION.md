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
