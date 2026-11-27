# P-GRD report

File: research/warp-drive/paper/reader/proofs/P-GRD.md, md5 68240c7f7c76de1ec19edb0737c6741b, 595 lines
(chapter text lines 1-403: sec:tl5-hfg "The sharpened constants", 24 labels; then Placement, Comparison and the
factors for the evaluation, Crosswalk rows with PENDING line numbers). Not committed.

Checks (scratch tree = git archive HEAD 1fb4b941 + P-GRD placement items 1-3, by
scratchpad/phf34/tools/mergegrd.py): lint.py --chapters 0 hits (labels 5141 -> 5165, +24); assemble.py --check
problems 0; in-memory check prints [] 0.

Placement (against chapters/87-ten-l5.md at HEAD 1fb4b941, unchanged since 8ceedd0e, both sec:tl5-hf and sec:tl5-hf4
merged): (1) the section inserted after the last line of rem:tl5-hf4-level (87:5006); (2) pointer sentence appended to
the paragraph after thm:tl5-hf (87:4594-4596); (3) clause added in rem:tl5-hf4-level (87:4992-4994). Additive, not a
rewrite: the merged closing conditions stay valid and either set may be used; reason: the new constants interlock
(choice of expansion, s_flat, s0*, s1* enter hypothesis (a) as well as (c)), and rewriting merged numbered lemmas would
change statements other text cites.

Closing conditions:
  level 6 sharpened: 8 (sqrt2 delta_w + 2 eps_(w,g)) S_(F,g) < 1, with r_(w,g) <= 1/4, eta0 < s1*, s_(*,g) < s1*.
  level 4 sharpened: 8 (sqrt2 delta_w + 2 eps_(w,g) + 2 eps_(M,g)) (S_(F,g) + S_(M,g)) < 1, with r_(w,g) + r_(M,g) <= 1/4.
Leading mu: S_(F,g) mu^(-3/2) at both levels (was mu^-6 / mu^-4); graded level-4 triple S_M, r_M, eps_M all
mu^(-3/2) (ungraded triple mu^-2, 1, mu^2 also allowed); r_(w,g) mu^(-3/2); s_(*,g) keeps mu^(-N/2).

Levers: (1) proved: Lambda_k per factor's own letters in Lemma G (c^g_n), Lambda_2 in C1, C_(1,0), X_t; k1 graded by
level k1^(j). (2) proved: count l_P + l_E <= n + 3. (3a) proved in part: point factor never D^2 Psi_B with |B| >= 2,
so C_P uses k1^(m_P) (level <= 1; none at level 4) and M^(m_P) = 57 / 8; top k1 still in k_g and in C1 (deduced why).
(3b) C1 vs C_S: not sharpened beyond Lambda_2; remains (component Sobolev, 258 count). (3c) proved: c^Q_n (exact
quadratic part, Leibniz, no Bell numbers) + s_flat c^(3)_n; seed value (81 + 5|R|) 2^n - 1; remains 7^(j'/2), q_jj',
80 vs 9. (3d) proved for S_F: sqrt(114) for N >= 5; smallness keeps M.

All factor formulas: section "Every factor, as a formula" of the file.
