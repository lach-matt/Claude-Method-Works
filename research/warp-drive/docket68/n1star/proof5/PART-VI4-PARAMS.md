# Part VI.C: the parameters

*Status.* Written (D320). Parts III-VI state conditions on the parameters they leave open: the constraint damping gauge
$E_C$, the gauge-modification parameters $E_\Upsilon$, the weights at $\mathscr I^+$, $\iota^+$ and $K^+$, the data
classes, and the Myers-Perry parameter set. This part lists every such condition with its source (section 1), and shows
that they can all be met, in an order in which each threshold depends only on choices already made (Theorem 2.1). It
also records two checks of quantifiers (section 3). Theorem 1.1 of III.E is proved at one point of $(v_C,e_C,C_0)$ and
for $\gamma_C>1/h_*$ outside a countable set, and every part uses one value of $\gamma_C$, chosen once. The open item of
III.F$''$ section 5 is closed by III.H Corollary 4.3.

## 1. The conditions

$\mu_0>0$ is fixed and $R_1 := \mu_0^{1/2}$ (III.B section 2). The table lists each condition with the file and line of
the write-out at D320 where it is stated or used, and what its threshold depends on. Conditions that only restate a
choice made in another row are omitted. (C1)-(C5) and (G+) are the labels of III.F$'$ section 1, III.I$''''''''''$ and
III.J.

| # | parameter | condition | source | threshold depends on |
|---|---|---|---|---|
| c1 | $v_C$, $e_C$, $C_0$ | $(v_C,e_C,C_0) = (\frac12,\frac1{102400},100)$, the point at which III.E Theorem 1.1 is proved | PART-IV5-CDMODES.md:30, 242-243; PART-III-F2-INDICIAL.md:30, 54; PART-IV7-TFACE.md:388 | none |
| c2 | $\gamma_C$ | $\gamma_C = h^{-1}$, $h\in\mathsf H = (0,h_*)\setminus\mathsf Z$, $h_* = \min(10^{-6},h_0,h_{\mathrm{tf}})$, $\mathsf Z$ countable | PART-IV5-CDMODES.md:32-34, 77-78, 163, 236-239; PART-IV7-TFACE.md:387 | c1 |
| c3 | $\gamma_C$ | (C1)-(C4): the indicial roots of $\Box^C_b$, simple, avoiding the listed sets, real at integer real part in $[3,51]$; these are III.E Theorem 1.1 (3)'s clauses | PART-III-F2-INDICIAL.md:36-55; PART-IV5-CDMODES.md:163 | c1, c2 |
| c4 | $\gamma_C$ | (C5) $\gamma_Cv_C\ge\frac12$, and $(1-e_C)(1-v_C)\gamma_C>100$ | PART-III-I11-SPACETIME.md:42; PART-III-F-LINEARISED.md:23-24; PART-III-K-NONLINEAR.md:49-50 | c1 |
| u1 | $c_\Upsilon$, $c_{\Upsilon,H}$, $c_C$ | the fixed 1-forms of III.D Definition 6.1 and Lemma 5.1 | PART-III-D-GAUGEPOT.md:249, 430-432 | c1 |
| u2 | $\gamma_{\Upsilon,H}$ | $\gamma_{\Upsilon,H}\in(0,\epsilon_0]$ (III.D$'$ Proposition 4.1) | PART-III-D2-ZEROENERGY.md:197-200 | none |
| u3 | $e_\Upsilon$ | $e_\Upsilon\in(0,\min(\epsilon_1,\epsilon_L))$, $\epsilon_L$ of III.D Lemma 7.1 | PART-III-D2-ZEROENERGY.md:197-200; PART-III-D-GAUGEPOT.md:439, 465; PART-III-F2-INDICIAL.md:374 | $\epsilon_1$: u2; $\epsilon_L$: c1-c2 |
| u4 | $\gamma_\Upsilon$ | $0<\gamma_\Upsilon<\min(\epsilon_1,\epsilon_L,\gamma_1,\frac38,\frac12s_C,\frac14)$, $s_C := (1-e_C)(1-v_C)\gamma_C$; $\epsilon_L$ contains the bound $C'|\gamma_\Upsilon|\le\frac12$ of its proof | PART-III-D2-ZEROENERGY.md:200; PART-III-D-GAUGEPOT.md:439, 461-462; PART-III-F2-INDICIAL.md:375-377, 429; PART-III-G3-GRAFT.md:29; PART-III-I10-CORR4.md:44 | $\gamma_1$: c1-c3, u3; $\epsilon_L$: c1-c2 |
| u5 | $\gamma_\Upsilon$ | $z_\Upsilon := 4e_\Upsilon\gamma_\Upsilon^2\in(0,\frac12]\setminus\mathsf Z_{\mathrm{exc}}$, $\mathsf Z_{\mathrm{exc}}$ countable | PART-III-F2-INDICIAL.md:103, 126-127, 178, 501; PART-III-G3-GRAFT.md:30; PART-III-G5-TF.md:51 | $\mathsf Z_{\mathrm{exc}}$: c1-c3; u3 |
| b1 | $b$ | $b$ in the ball $\mathcal B_{\mathrm{VI}}$ of Part VI, on which (Dyn) holds | PART-VI3-TRAPPING.md (Theorem 5.1) | none |
| b2 | $b$ | $b\in\mathcal B(\gamma_{\Upsilon,H})$ (III.D$'$ Proposition 4.1); $c_0$ of III.H Corollary 4.3, then $b\in\mathcal B(c_0)$ (III.F$''$ Proposition 4.1) and in III.H Corollaries 4.3-4.4's neighbourhood; and $b$ near $b_0$ as III.E, III.F$'$, III.F$''$, III.J ask | PART-III-D2-ZEROENERGY.md:197-200; PART-III-F3-MODES.md:248-252; PART-III-H-AUGMENT.md:466-468, 492-493; PART-III-E-CONSTRAINT.md:38; PART-III-F2-INDICIAL.md:376; PART-III-J-PARAM.md:39, 404 | c1-c2, u1-u5 |
| b3 | $\mathcal B_*$ | open, $\bar{\mathcal B}_*\subset\mathcal B_1$, and (B5): $\|P-2L_b\|_{(0;d)}<\epsilon_0$ on $\bar{\mathcal B}_*$; the only condition on $\mathcal B_*$ there | PART-III-H3-UNIFORM.md:61-64 | b2, u1-u5 |
| w1 | $\epsilon_+$, $\epsilon_K$ | $0<\epsilon_K<\epsilon_+<\min(\delta_\sharp,\epsilon_{\mathrm{ind}})$, $\epsilon_+<\frac14$, and (G+) after decreasing $\epsilon_+$; $\delta_\sharp = (1-e_\Upsilon)\gamma_\Upsilon$, $\epsilon_{\mathrm{ind}} = \min\mathrm{Re}\,\mathcal E^\iota_{\mathrm{ind}}>0$ | PART-III-I10-CORR4.md:32-45; PART-III-I6-ALMOSTBDD.md:118-119; PART-III-J-PARAM.md:34, 48-51, 56 | u1-u5 |
| w2 | $\alpha$ | admissible $\alpha$, dense in $(4+\epsilon_K-\epsilon'_0,4+\epsilon_K]$ | PART-III-J-PARAM.md:57 | w1 |
| d1 | $\mathcal E_0$, $\ell_0$ | $\min\mathrm{Re}\,\mathcal E_0>\frac32+2\gamma_\Upsilon$, $j\mathcal E_0\subset\mathcal E_0$, $\ell_0>\frac32$, $\ell_0\notin\mathrm{Re}\,\pi_1\mathcal E_0$ | PART-III-C2-POLYHOM.md:19, 133-140; PART-III-K-NONLINEAR.md:54-56 | u4 |
| d2 | $\ell_I$ | $\frac32<\ell_I<\min(\ell_0,\frac32+s_C)$, $\ell_I\notin\frac32+\sigma_\Upsilon$, $\sigma_\Upsilon = \{0,(1-e_\Upsilon)\gamma_\Upsilon,\gamma_\Upsilon,2\gamma_\Upsilon\}$ | PART-III-C2-POLYHOM.md:135-136; PART-III-C-EXTERIOR.md:146 | c1-c2, u3-u4, d1 |
| n1 | $\epsilon$, $d_1$ | the smallness and regularity of III.K Theorem 4.3 | PART-III-K-NONLINEAR.md:463-468 | all the above |

## 2. The choice

**Theorem 2.1.** The conditions of section 1 can be met together. Make the choices in this order; at each step the
thresholds depend only on the choices before it (last column of the table):

(0) $\mathcal B_{\mathrm{VI}} := \{|b-b_0|\le\epsilon_{\mathrm{VI}}\}$ of Part VI Theorem 5.1. It depends on the metrics
alone.

(1) $(v_C,e_C,C_0) := (\frac12,\frac1{102400},100)$ and $h\in\mathsf H$, $\gamma_C := h^{-1}$. Then III.E Theorem 1.1
holds at these values (Part IV$''''$ for (1)-(3), Part IV$''''''$ Theorem 4.1 for (4)), with (C1)-(C4) (row c3), and
(C5) and $s_C>100$ hold as $\gamma_C>10^6$.

(2) The gauge: $\epsilon_0$ of III.D$'$ Proposition 4.1 is uniform. Choose $\gamma_{\Upsilon,H}\in(0,\epsilon_0]$; this
fixes $\epsilon_1$ and $\mathcal B(\gamma_{\Upsilon,H})$. Choose $e_\Upsilon\in(0,\min(\epsilon_1,\epsilon_L))$; this
fixes $\gamma_1$ of III.F$'$ Proposition 3.3 (which fixes all parameters but $\gamma_\Upsilon$, and depends on the
orders, hence on $\gamma_C$; PART-III-F2-INDICIAL.md:429). $\mathsf Z_{\mathrm{exc}}$ is fixed by step (1). Choose
$\gamma_\Upsilon$ in the interval of row u4 with $4e_\Upsilon\gamma_\Upsilon^2\notin\mathsf Z_{\mathrm{exc}}$. This is
possible because the interval is nonempty and open, while $\{\gamma>0:4e_\Upsilon\gamma^2\in\mathsf Z_{\mathrm{exc}}\}$
is countable. Then $z_\Upsilon\in(0,\frac12]$, as $\gamma_\Upsilon<\frac14$ and $e_\Upsilon<1$. III.D Proposition 6.3
(invertibility of $\widehat{\Box^\Upsilon_b}(\sigma)$ for $|\sigma|\ge c_0$) is then implied, for every $c_0$ and
$b\in\mathcal B(\gamma_{\Upsilon,H})$, by III.D$'$ Proposition 4.1, which gives it for every $\sigma$ with
$\mathrm{Im}\,\sigma\ge0$; so it imposes no further condition.

(3) The parameter set. The gauge being fixed, take $c_0$ of III.H Corollary 4.3 (uniform near $b_0$), then $\mathcal
B(c_0)$ of III.F$''$ Proposition 4.1, which fixes the modification parameters first and then allows every $c_0>0$
(PART-III-F3-MODES.md:248-249). Let $\mathcal B_*$ be an open ball about $b_0$ whose closure lies in $\mathcal
B_{\mathrm{VI}}$, in every neighbourhood of row b2, and in $\mathcal B_1$, with (B5). These are finitely many
neighbourhoods of $b_0$, fixed by steps (0)-(2). III.H3 imposes no lower bound on $\mathcal B_*$
(PART-III-H3-UNIFORM.md:64), so shrinking it is allowed. Every operator family of Parts I-IV is then taken over
$\bar{\mathcal B}_*$, a compact set on which (Dyn) holds (step 0), as (H5) and its extensions ask.

(4) The weights: $\delta_\sharp>0$ and $\epsilon_{\mathrm{ind}}>0$ are fixed by step (2); choose $\epsilon_+$, then
$\epsilon_K$, as in row w1, decreasing $\epsilon_+$ for (G+) (possible: no $\lambda\in\Lambda$ has real part in
$(3,3+\epsilon_+]$ for $\epsilon_+$ small, PART-III-J-PARAM.md:48-51); then $\alpha$ as in row w2.

(5) The data classes: $\mathcal E_0$ and $\ell_0$ as in row d1, then $\ell_I$ in the nonempty open interval of row d2
minus the four points $\frac32+\sigma_\Upsilon$. For the data of the route, Part VII checks row d1.

(6) $\epsilon$ and $d_1$ of III.K Theorem 4.3, which depend on all of the above.

*Proof.* Each step's existence claim is the cited statement, read with the quantifiers it has; the table's last column
records that no threshold depends on a later choice. In step (2), III.D$'$ Proposition 4.1's $\epsilon_0$ is uniform,
while its $\epsilon_1$ and $\mathcal B(\gamma_{\Upsilon,H})$ come after $\gamma_{\Upsilon,H}$, so the order
$\gamma_{\Upsilon,H}$, $e_\Upsilon$, $\gamma_\Upsilon$ meets it. The only low-frequency radius that depends on the gauge
is III.H's $c_0$, and it is used only after the gauge is fixed, through III.F$''$ Proposition 4.1, whose neighbourhood
is then chosen. In step (3), each neighbourhood of row b2 is open and contains $b_0$, so their intersection with
$\mathcal B_{\mathrm{VI}}$ contains a ball. Part VI's ball depends on no gauge parameter, as the dynamical hypotheses
concern the metric alone (VI.A section 0). Part VI.B$'$ proves (K3) for every $\epsilon$ (Proposition 3.4), so
$\epsilon_{\mathrm{VI}}$ does not depend on the regularity $d_0$ of II.C$'$, nor on $k$ of its Theorem 1.1. $\square$

## 3. Two quantifier checks

*III.E Theorem 1.1.* It is stated for fixed $v_C\in(0,1)$, $C_0>0$ and all sufficiently large $\gamma_C$
(PART-III-E-CONSTRAINT.md:36-38). Part IV$''''$ proves it at $(v_C,e_C,C_0) = (\frac12,\frac1{102400},\le100)$ and for
$\gamma_C>1/h_*$ outside a countable set (PART-IV5-CDMODES.md:235-243, finding (IV$''''$1)). The proved range is what
the parts use. A search of PART-*.md for $\gamma_C$ together with "for all", "for every", "sufficiently large" or a
limit $\gamma_C\to\infty$ finds only III.E's statement and IV$''''$'s finding. Every other part takes one value of
$\gamma_C$, chosen once: III.F$'$ fixes $\gamma_C$ before $\gamma_1$ (PART-III-F2-INDICIAL.md:429), III.K takes
$\gamma_C$ large with $s_C>100$ (PART-III-K-NONLINEAR.md:49-50), III.G$'$ and III.C$'$ use $s_C$ as a fixed number. So
the restriction costs nothing.

*III.F$''$ section 5.* For $b\ne b_0$ and $0<|\sigma|<c_0$, the invertibility of $\widehat{L_b}(\sigma)$ was left open
there (PART-III-F3-MODES.md:261-265). III.H Corollary 4.3 proves it for $b$ near $b_0$ and $\sigma\in\Sigma_0$,
$|\sigma|\le c_0$ (PART-III-H-AUGMENT.md:466-468), and says it closes that item (:496). Its neighbourhood is one of row
b2, so the item holds on $\bar{\mathcal B}_*$.

## 4. Findings and sources

(VI.C1) *The order of the gauge parameters.* $\gamma_{\Upsilon,H}$ comes first, then $e_\Upsilon$, then
$\gamma_\Upsilon$: III.D$'$ Proposition 4.1's thresholds for $e_\Upsilon$ and $\gamma_\Upsilon$ depend on
$\gamma_{\Upsilon,H}$, and III.F$'$ Proposition 3.3 fixes everything but $\gamma_\Upsilon$. The record chose them
together; nothing changes, but the order is now explicit.

(VI.C2) *The parameter set is chosen last.* $\mathcal B_*$ is shrunk to lie in Part VI's ball and in every neighbourhood
the gauge choices produce. III.H3's (B5) is an upper bound only, so this is allowed.

(VI.C3) *Two conditions are ranges, not points.* $\gamma_C$ ranges over $\{1/h:h\in\mathsf H\}$ and $\gamma_\Upsilon$
over an interval minus a countable set. The record's point $(\frac12,\frac1{102400},10^6)$, at which III.F$'$ computes
(C1)-(C4), has $h = 10^{-6}$, which is not in $\mathsf H\subset(0,h_*)$ since $h_*\le10^{-6}$. It is a computation, not
the choice: Part IV$''''$ gives (C1)-(C4) for every $h\in\mathsf H$, and any such $h$ serves.

*Sources.* No new reading. Inputs: the rows of section 1.
