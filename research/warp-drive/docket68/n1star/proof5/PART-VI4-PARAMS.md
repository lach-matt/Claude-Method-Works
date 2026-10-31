# Part VI.C: the parameters

*Status.* Amended (D327-D328: section 3's argument by enumeration, restated after verifier 144 found its first premise
too narrow), read by verifier 150 (D331: the conclusion holds; the premise is widened to $v_C$, $e_C$ and $C_0$, fixed
once by row c1, with the checks G4-G5), read by verifier 151, correct, its three nits seated; proved (D332). Written
(D320); amended (D322: rows d1-d2 take III.I$''''''''''$'s (H4), finding (VI.C4)); verified (D323: verifier 140's two
minor findings and four notes repaired, finding (VI.C5)); proved (D324: verifier 141 read the repairs, correct; one note
seated). Parts III-VI state conditions on the parameters they leave open: the constraint damping gauge $E_C$, the
gauge-modification parameters $E_\Upsilon$, the weights at $\mathscr I^+$, $\iota^+$ and $K^+$, the data classes, and
the Myers-Perry parameter set. This part lists every such condition with its source (section 1), and shows that they can
all be met, in an order in which each threshold depends only on choices already made (Theorem 2.1). It also records two
checks of quantifiers (section 3). Theorem 1.1 of III.E is proved at one point of $(v_C,e_C,C_0)$ and for
$\gamma_C>1/h_*$ outside a countable set, and every part uses one value of $\gamma_C$, chosen once. The open item of
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
| u1 | $c_\Upsilon$, $c_{\Upsilon,H}$, $c_C$ | the fixed 1-forms of III.B Definition 6.1, in the radial forms the proofs use, and III.D Lemma 5.1 | PART-III-B-FAMILY.md:425-433; PART-III-D3-SYMSTATES.md:30-32; PART-IV5-CDMODES.md:36-38; PART-III-D-GAUGEPOT.md:249 | c1 |
| u2 | $\gamma_{\Upsilon,H}$ | $\gamma_{\Upsilon,H}\in(0,\epsilon_0]$ (III.D$'$ Proposition 4.1) | PART-III-D2-ZEROENERGY.md:197-200 | none |
| u3 | $e_\Upsilon$ | $e_\Upsilon\in(0,\min(\epsilon_1,\epsilon_L))$, $\epsilon_L$ of III.D Lemma 7.1 | PART-III-D2-ZEROENERGY.md:197-200; PART-III-D-GAUGEPOT.md:439, 465; PART-III-F2-INDICIAL.md:374 | $\epsilon_1$: u2; $\epsilon_L$: c1-c2 |
| u4 | $\gamma_\Upsilon$ | $0<\gamma_\Upsilon<\min(\epsilon_1,\epsilon_L,\gamma_1,\frac38,\frac12s_C,\frac14)$, $s_C := (1-e_C)(1-v_C)\gamma_C$; $\epsilon_L$ contains the bound $C'|\gamma_\Upsilon|\le\frac12$ of its proof | PART-III-D2-ZEROENERGY.md:200; PART-III-D-GAUGEPOT.md:439, 461-462; PART-III-F2-INDICIAL.md:375-377, 429; PART-III-G3-GRAFT.md:29; PART-III-I10-CORR4.md:44 | $\gamma_1$: c1-c3, u2-u3; $\epsilon_L$: c1-c2 |
| u5 | $\gamma_\Upsilon$ | $z_\Upsilon := 4e_\Upsilon\gamma_\Upsilon^2\in(0,\frac12]\setminus\mathsf Z_{\mathrm{exc}}$, $\mathsf Z_{\mathrm{exc}}$ countable | PART-III-F2-INDICIAL.md:103, 126-127, 178, 501; PART-III-G3-GRAFT.md:30; PART-III-G5-TF.md:51 | $\mathsf Z_{\mathrm{exc}}$: c1-c3; u3 |
| b1 | $b$ | $b$ in the ball $\mathcal B_{\mathrm{VI}}$ of Part VI, on which (Dyn) holds | PART-VI3-TRAPPING.md:460-469 (Theorem 5.1) | none |
| b2 | $b$ | $b\in\mathcal B(\gamma_{\Upsilon,H})$ (III.D$'$ Proposition 4.1); $c_0$ of III.H Corollary 4.3, then $b\in\mathcal B(c_0)$ (III.F$''$ Proposition 4.1) and in III.H Corollaries 4.3-4.4's neighbourhood; and $b$ near $b_0$ as III.E, III.F$'$, III.F$''$, III.J ask | PART-III-D2-ZEROENERGY.md:197-200; PART-III-F3-MODES.md:248-252; PART-III-H-AUGMENT.md:466-468, 492-493; PART-III-E-CONSTRAINT.md:38; PART-III-F2-INDICIAL.md:376; PART-III-J-PARAM.md:39, 404 | c1-c2, u1-u5 |
| b3 | $\mathcal B_*$ | open, $\bar{\mathcal B}_*\subset\mathcal B_1$, and (B5): $\|P-2L_b\|_{(0;d)}<\epsilon_0$ on $\bar{\mathcal B}_*$; the only condition on $\mathcal B_*$ there; III.I(16) shrinks it further (row b4) | PART-III-H3-UNIFORM.md:61-65 | b2, u1-u5 |
| b4 | $\mathcal B_*$ | III.I(16) shrinks $\mathcal B_*$ so that the rows at $b$ are jointly injective and $-\mathrm{id}+A_k$ is invertible; both depend on the row set and on the levels up to $\alpha$ | PART-III-I16-BASEPOINTS.md:97-102, 402-403; PART-III-H3-UNIFORM.md:64-65 | b3, w1-w2, d1-d2 |
| w1 | $\epsilon_+$, $\epsilon_K$ | $0<\epsilon_K<\epsilon_+<\min(\delta_\sharp,\epsilon_{\mathrm{ind}},\ell_I-3)$, $\epsilon_+<\frac14$, and (G+) after decreasing $\epsilon_+$ ($\Lambda$ contains $\pi_1\mathcal E^C_I$, PART-III-I11-SPACETIME.md:66, so it is fixed after rows d1-d2); $\delta_\sharp = (1-e_\Upsilon)\gamma_\Upsilon$; $\epsilon_{\mathrm{ind}}$ is III.G$''''$ Proposition 5.1's, that is III.F$'$ Proposition 2.3 (f)'s gap (2.2), $<3\times10^{-6}$ at the record's parameter point [D390: printed as $\min\mathrm{Re}\,\mathcal E^\iota_{\mathrm{ind}}$ before, which is not (1.1)'s $\epsilon_{\mathrm{ind}}$] | PART-III-I10-CORR4.md:32-48; PART-III-I11-SPACETIME.md:38; PART-III-G5-TF.md:190; PART-III-F2-INDICIAL.md:130-136; PART-III-I6-ALMOSTBDD.md:118-119; PART-III-J-PARAM.md:34, 48-51, 56; PART-III-I11-SPACETIME.md:45, 66 | u1-u5, d1-d2 |
| w2 | $\alpha$ | admissible $\alpha$, dense in $(4+\epsilon_K-\epsilon'_0,4+\epsilon_K]$ | PART-III-J-PARAM.md:52-57 | w1, d1-d2 ((A$_J$) involves $\Lambda$) |
| d1 | $\mathcal E_0$, $\ell_0$ | $\min\mathrm{Re}\,\mathcal E_0>\frac32+2\gamma_\Upsilon$, $j\mathcal E_0\subset\mathcal E_0$, $\ell_0>3$ (so that row d2 is nonempty), $\ell_0\notin\mathrm{Re}\,\pi_1\mathcal E_0$ | PART-III-C2-POLYHOM.md:19, 133-140; PART-III-K-NONLINEAR.md:54-56; PART-III-I11-SPACETIME.md:45 | u4 |
| d2 | $\ell_I$ | $3<\ell_I<\min(\ell_0,\frac32+s_C)$, with row w1's $\epsilon_+<\ell_I-3$ (III.C$'$ Theorem 3.1 asks $\frac32<\ell_I<\ell_0$, III.I$''''''''''$ (H4) asks $\ell_I>3+\epsilon_+$, and III.K uses one $\ell_I$), off (H4)'s exclusion sets, which are discrete: for $\ell_I$ in a bounded interval $\mathcal E^C_I$ ranges over finitely many index sets (PART-III-C2-POLYHOM.md:256-259), and $\ell_I\notin\mathrm{Re}\,\pi_1\mathcal E^C_I$ avoids their real parts; $\ell_I\notin\frac32+\sigma_\Upsilon$, $\sigma_\Upsilon = \{0,(1-e_\Upsilon)\gamma_\Upsilon,\gamma_\Upsilon,2\gamma_\Upsilon\}$ | PART-III-C2-POLYHOM.md:135-136; PART-III-C-EXTERIOR.md:146; PART-III-I11-SPACETIME.md:45-48; PART-III-K-NONLINEAR.md:56-57; PART-III-I2-SCRI.md:166-167 | c1-c2, u3-u4, d1 |
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

(3) The data classes: $\mathcal E_0$ and $\ell_0>3$ as in row d1, then $\ell_I$ in row d2's interval
$(3,\min(\ell_0,\frac32+s_C))$ minus the four points $\frac32+\sigma_\Upsilon$ and (H4)'s exclusion sets. This fixes
$\mathcal E^C_I$ (III.C$'$ Theorem 3.1) and $\Lambda$. For the route, Part VII takes $\mathcal E_0 = \{(j,0):j\ge2\}$,
$\ell_0\in(3,4)$ and $\ell_I\in(3,\ell_0)$ (PART-VII-ASSEMBLY.md (0.1)).

(4) The weights: $\delta_\sharp>0$ and $\epsilon_{\mathrm{ind}}>0$ are fixed by step (2). Choose
$\epsilon_+<\min(\delta_\sharp,\epsilon_{\mathrm{ind}},\frac14,\ell_I-3)$, decreased for (G+) (possible: no
$\lambda\in\Lambda$ has real part in $(3,3+\epsilon_+]$ for $\epsilon_+$ small, PART-III-J-PARAM.md:48-51), then
$\epsilon_K$, as in row w1; then $\alpha$ as in row w2. (H4) holds as $\epsilon_+<\ell_I-3$, and decreasing $\epsilon_+$
keeps rows d1-d2.

(5) The parameter set. The gauge being fixed, take $c_0$ of III.H Corollary 4.3 (uniform near $b_0$), then $\mathcal
B(c_0)$ of III.F$''$ Proposition 4.1, which fixes the modification parameters first and then allows every $c_0>0$
(PART-III-F3-MODES.md:248-249). Let $\mathcal B_*$ be an open ball about $b_0$ whose closure lies in $\mathcal
B_{\mathrm{VI}}$, in every neighbourhood of row b2, and in $\mathcal B_1$, with (B5). These are finitely many
neighbourhoods of $b_0$, fixed by steps (0)-(4). Balls are taken in the norm $|\mu-\mu_0|+|A|$, $|A|$ the Frobenius
norm, which is invariant under conjugation by $O(4)$, so every parameter ball is $O(4)$-invariant (Part VII Lemma 3.1
uses this). III.H3 imposes no lower bound on $\mathcal B_*$ (PART-III-H3-UNIFORM.md:64), so shrinking it is allowed.
Every operator family of Parts I-IV is then taken over $\bar{\mathcal B}_*$, a compact set on which (Dyn) holds (step
0), as (H5) and its extensions ask. Last, $\mathcal B_*$ is shrunk as III.I(16) asks (row b4), which depends on steps
(3)-(4) only.

(6) $\epsilon$ and $d_1$ of III.K Theorem 4.3, which depend on all of the above.

*Proof.* Each step's existence claim is the cited statement, read with the quantifiers it has; the table's last column
records that no threshold depends on a later choice. In step (2), III.D$'$ Proposition 4.1's $\epsilon_0$ is uniform,
while its $\epsilon_1$ and $\mathcal B(\gamma_{\Upsilon,H})$ come after $\gamma_{\Upsilon,H}$, so the order
$\gamma_{\Upsilon,H}$, $e_\Upsilon$, $\gamma_\Upsilon$ meets it. The only low-frequency radius that depends on the gauge
is III.H's $c_0$, and it is used only after the gauge is fixed, through III.F$''$ Proposition 4.1, whose neighbourhood
is then chosen. In step (5), each neighbourhood of rows b2 and b4 is open and contains $b_0$, so their intersection with
$\mathcal B_{\mathrm{VI}}$ contains a ball. Part VI's ball depends on no gauge parameter, as the dynamical hypotheses
concern the metric alone (VI.A section 0). Part VI.B$'$ proves (K3) for every $\epsilon$ (Proposition 3.4), so
$\epsilon_{\mathrm{VI}}$ does not depend on the regularity $d_0$ of II.C$'$, nor on $k$ of its Theorem 1.1. $\square$

## 3. Two quantifier checks

*III.E Theorem 1.1.* It is stated for fixed $v_C\in(0,1)$, $C_0>0$ and all sufficiently large $\gamma_C$
(PART-III-E-CONSTRAINT.md:36-38). Part IV$''''$ proves it at $(v_C,e_C,C_0) = (\frac12,\frac1{102400},\le100)$ and for
$\gamma_C>1/h_*$ outside a countable set (PART-IV5-CDMODES.md:235-243, finding (IV$''''$1)). The proved range is what
the parts use. This is proved by enumeration, not found by search (D327-D328; a search for quantifiers stood here).
Every statement derived from III.E Theorem 1.1 (III.E sections 2-3, III.E$'$, and (C1)-(C5)) concerns $\Box^C_b$ at the
parameters fixed in III.E (PART-III-E-CONSTRAINT.md:69), rows c1-c4. To apply one of them at another value a part must
write an operator with another damping parameter, and the damping enters $\Box^C_b$, $\delta^*_{g,E_C}$ and $E^C$ only
through $\gamma_C$; so such a use names $\gamma_C$, $s_C := \gamma_C(1-e_C)(1-v_C)$, $h := \gamma_C^{-1}$ (the variable
of IV$''''$-IV$''''''$, which prove the theorem), or a rescaled $E_C$. The other constants of the damping, $v_C$, $e_C$
and $C_0$, enter $\Box^C_b$ too; they are fixed once, by row c1, at the point where Part IV$''''$ proves the theorem,
and no part varies them: `checks/gammac5.py` G4 lists, with its class, every line its pattern finds setting, bounding,
ranging or quantifying one of them, and fails on any line it does not list (42 lines: 15 uses of the fixed point, 19 in
Parts IV$''''$-IV$''''''$, 2 definitions, the 2 lines of III.E's statement, and 4 where $C_0$ names another constant;
`checks/damping5.tsv`; verifier 150's m2, D331). $c_C$, chosen with III.E Theorem 1.1 too, is fixed by Part IV$''''$
(PART-IV5-CDMODES.md:35-38) and varied by no part (verifier 151's A5; verifier 152's n4). And $h := \gamma_C^{-1}$ is
introduced in Part IV$''''$ alone (G5). `checks/gammac5.py` lists every line of PART-*.md naming $\gamma_C$ or $s_C$ or
citing III.E Theorem 1.1 (also across a line break), with its class, and fails on any line it does not list: 55
identities valid for every $\gamma_C$; 56 conditions on, or uses of, the one fixed value; 17 citations of the theorem at
that value; 3 lines of III.F$'$'s homotopy $(\tau\gamma_C,\tau\gamma_\Upsilon)$, $\tau\in[0,1]$, which uses III.F Lemma
2.1's proof and III.E section 1, not the theorem; III.E's statement; the theorem's proof in IV$''''$ and IV$''''''$
(IV$'''''$, written in $h$, names neither); and the records, among them the record's computation at its own point
$\gamma_C = 10^6$, outside the proved set. It also checks that no rescaled $E_C$ or $E^C$ occurs: the six lines that
pair $E_C$, $E^C$ or $\Box^C$ with a family are spectral families in the frequency or a time range. So every part takes
one value of $\gamma_C$, chosen once: III.F$'$ fixes $\gamma_C$ before $\gamma_1$ (PART-III-F2-INDICIAL.md:429), III.K
takes $\gamma_C$ large with $s_C>100$ (PART-III-K-NONLINEAR.md:49-50), III.G$'$ and III.C$'$ use $s_C$ as a fixed
number. So the restriction costs nothing.

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

(VI.C4) *The data weight* (found in writing Part VII, D322). III.C$'$ Theorem 3.1 asks $\ell_I<\ell_0$ and
III.I$''''''''''$ (H4) asks $\ell_I>3+\epsilon_+$, for the one $\ell_I$ that III.K uses (PART-III-K-NONLINEAR.md:56-57).
So the data weight must satisfy $\ell_0>3+\epsilon_+$: at spatial infinity the data must have their terms of order 2 and
3 polyhomogeneous, with a conormal remainder beyond order 3. Rows d1-d2 as written at D320 listed only $\ell_0>\frac32$
and $\frac32<\ell_I$. Repaired (D322); the order is corrected in (VI.C5).

(VI.C5) *The order after (VI.C4)* (verifier 140, D323). (G+) and $\alpha$'s condition (A$_J$) involve $\Lambda$, which
contains $\pi_1\mathcal E^C_I$ (PART-III-I11-SPACETIME.md:66), and $\mathcal E^C_I$ depends on $\mathcal E_0$, $\ell_0$
and $\ell_I$ (PART-III-C2-POLYHOM.md:256-259). With (H4) in row d2, the D322 order, weights before data classes, was
circular. Now the data classes come first, with $\ell_0>3$ and $\ell_I>3$, and $\epsilon_+<\ell_I-3$ is chosen with the
weights; decreasing $\epsilon_+$ only weakens (H4) and rows d1-d2. III.I(16) shrinks $\mathcal B_*$ further, depending
on the row set and the levels up to $\alpha$ (PART-III-I16-BASEPOINTS.md:97-102, 402-403); it is row b4, and the
parameter set is now chosen last, as (VI.C2) says.

*Sources.* No new reading. Inputs: the rows of section 1.
