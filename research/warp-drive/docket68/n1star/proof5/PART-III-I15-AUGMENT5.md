# Part III.I$''''''''''''''$. Absorbing the expansion into the operator, n = 4 ([Hin26] section 11.8.3)

*Status.* Written (D279); verified (D281: verifier 120's findings seated, to be read). This part proves, at spatial
dimension $n = 4$, the content of [Hin26] section 11.8.3 (pp. 292-296): the parameters of the partial expansion of
III.I$''''''''''''$ become arguments of an augmented gauge-fixed Einstein operator $P_5$ (Definition 1.2, the source's
Definition 11.63), its linearisation in the black hole parameters has the full order of decay at $K^+$ (Lemma 2.4 (c),
the source's Lemma 11.65), and the linearised equation at $(h,\vec p,q)$ has, for every source, a unique choice of $\vec
p\,'$ for which the solution splits as $h_{\mathrm{rem}}(q')+h'$ with $h'$ of the decay assumed of $h$ (Theorem 3.1, the
source's Corollary 11.66).

*What n = 4 changes.* (1) *The linearisation is taken at $h$, not at $h+h_{\mathrm{rem}}(q)$.* The source proves
Corollary 11.66 by applying Theorem 11.59 at the background $h+h_{\mathrm{rem}}(q)$, whose $K^+$-order is only
$2+\epsilon_K$ (its Remark 11.61). At $n = 4$ that background has $K^+$-order $\alpha-2-\epsilon$, and
III.I$'''''''''''$ Theorem 4.1 needs $a_K\ge4+\epsilon_K$, its rows' remainders $r^\nu$ need
$a_K>\alpha+1-\lambda_\sharp$ (III.I$'''''''''$ Lemma 2.6 (c)), and a perturbation series in $q$ around it loses
derivatives. Instead the forward solution $u$ at $h+h_{\mathrm{rem}}(q)$, which exists and is smooth, satisfies
$L_{h,\vec p}u = F-D_{\vec p}P_5(\vec p\,')-R_qu$, and its decay is raised level by level through the levels of
III.I$'''''''''''''$, each step an expansion at $h$, where $a_K\ge4+\epsilon_K$; the new coefficients at each level are
the new parameters up to a small error, as in III.I$'''''''''''$ Theorem 4.1 (Theorem 3.1). (2) *The losses.* The
classes are read with the orders "$w-$", every order below $w$ (Definition 1.1), and the constructions of
III.I$'''''''''''$-III.I$'''''''''''''$ accept sources of $K^+$-order $\alpha-$ and do not depend on the loss (Lemma
2.5); this is what makes the class of $h'$ that of $h$ (Remark 3.2). (3) *Rotation rows.* At the non-rotating $b_0$
every rotation is Killing, so the v1 terms of exponent below 2 carry no row (III.I$'''''''''$ section 1) and the
source's treatment would put them into $q$; but at a rotating $b$ near $b_0$ the rotation state $h_{b,\mathrm v1}$ does
not vanish, and such a coefficient would give the linearisation in $b$ the $K^+$-order $\alpha-2+\lambda_\sharp$ only.
They are carried instead by rows of all rotations (Definition 1.3), fixed in Theorem 3.1 by the expansion (Step 4'). (4)
$h_{-S} := 0$, as the source permits ("the reader may as well only consider the case that $h_{-S} = 0$"); the exterior
part III.C$'$ adds $\chi_-h_{-S}$. The source's Corollary 11.67 (linear stability, sketched there and not used later)
rests on the exterior result and is deferred to after III.C$'$. Notation: Parts II.E, III.A, III.D$'''$, III.F$'$,
III.F$''''$, III.G$''$, III.G$''''$, III.H, III.I, III.I$'''''''$-III.I$'''''''''''''$; no instrument is used.

## 1. Setting

Everything of III.I$''''''''''''$ (with $w_\rho = 3+\eta_2-2\epsilon-d_\rho$, D277) and of III.I$'''''''''''''$ is kept;
$\alpha\in(4,4+\epsilon_K]$ is admissible in the sense of III.I$''''''''''$ Definition 1.3 (where III.I$'''''''''''$
Theorem 4.1 and III.I$''''''''''''$ Theorem 3.1 are proved; III.I$'''''''''''''$ Definition 1.1 serves the intermediate
levels), III.I$''''''''''''$'s $\delta_+$ is taken $\le\eta_E := \min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}>0$, so that
$3+\eta_2+\eta_E>3+\epsilon_+$, and the theorems are at $b = b_0$, with derivatives in $b$ taken at $b_0$. The class
$\mathcal X$ is restricted by two requirements, the source's Remark 11.64 (2): $\mathcal E_+\supset(\mathcal
E_\sharp\cup\mathcal E^\natural)\cap\{\mathrm{Re}<3+\epsilon_+\}$, which can be imposed with (H1)-(H3) as both sets do
not depend on $\mathcal E_+$ below $3+\epsilon_+$ (III.I$''''''''''$ Lemma 1.2 (b), as in III.I$''''''''''''$ section
1); and

(H5) $a_+<3+\eta_2$.

For a weight $w$, "order $w-$" means order $w-\epsilon$ for every $\epsilon>0$, and $\dot H^{\infty,w-}_{\mathrm b} :=
\bigcap_\epsilon\dot H^{\infty,w-\epsilon}_{\mathrm b}$, $\mathcal Y^\natural(\alpha-) := \bigcap_\epsilon\mathcal
Y^\natural(\alpha-\epsilon)$, and so on.

**Definition 1.1 (the coefficients; the source's (11.227)).** For $\rho\in\mathcal R'$ let $\mathcal E^\alpha_\rho :=
\{(z,k)\in\mathcal E_\sharp-d_\rho:\mathrm{Re}\,z>2\}$ ($\rho\ne\mathrm v1$) and $\mathcal E^\alpha_{\mathrm v1} :=
\mathcal E_\sharp\cap\{\mathrm{Re}\ge2\}$: the v1 terms of exponent in $\mathcal M$ are carried by the rotation rows of
Definition 1.3. $\mathcal Q$ is the real vector space of the conjugation-symmetric tuples $q =
(S_{\mathrm{rem}},b_{\mathrm{rem}},(Y_\rho)_{\rho\in\mathcal R'})$ with
$$S_{\mathrm{rem}}\in\dot H^{\infty,(\alpha-2)-}_{\mathrm b}([1,\infty];\mathcal S_1),\quad b_{\mathrm{rem}}\in\dot
H^{\infty,(\alpha-1)-}_{\mathrm b}([1,\infty];\mathfrak b),\quad Y_\rho\in\bigcap_{\epsilon>0}\dot H^{\infty,\mathcal
Q(\mathcal E^\alpha_\rho,\,3+\eta_2-2\epsilon-d_\rho)}_{\mathrm b}([1,\infty];\mathcal Y_{\rho,\mathbb C}).\tag{1.1}$$
"$q$ small" means small in one fixed seminorm of large order, at a $K^+$-weight $a'_K<\alpha-2$ above the level
$\alpha_1$ of Theorem 3.1's Step 1, so that $h+h_{\mathrm{rem}}(q)$ is small in III.I$''''''''$'s $\mathcal X^d$ with
$a_K = a'_K$. The rate of a polyhomogeneous term $t_*^{-z}$ of $Y_\rho$ is $\mathrm{Re}\,z>2$ ($\rho\ne\mathrm v1$; for
v1 it is $\mathrm{Re}\,z+1\ge3$ at $b_0$, where $h_{b_0,\mathrm v1} = 0$, and $\mathrm{Re}\,z\ge2$ at a rotating $b$),
so by (G) it exceeds $2+\epsilon_K\ge\alpha-2$ at $b_0$, and is $\ge2$ at every $b$ near $b_0$.

**Definition 1.2 (augmentation #5; the source's Definition 11.63).** For $q\in\mathcal Q$ and $b$ near $b_0$ let
$$h_{b,\mathrm{rem}}(q) := \chi_K\Big(h^{\le1}_{b,\mathrm s1}\big(S_{\mathrm{rem}}(t_*)\big)+\dot
g_b\big(b_{\mathrm{rem}}(t_*)\big)+\sum_{\rho\in\mathcal R'}T_{\rho,b}\big(Y_\rho(t_*)\big)\Big),\tag{1.2}$$
with the towers $T_{\rho,b}$ of III.G$''$ Table 1.1 for $L_b$ (III.G$''$ Definition 2.5, chosen by Lemma 2.1),
$h^{\le2}_{b,\mathrm v1}$ for v1, and $\dot g_b(\dot b) := \dot\mu\,\dot g^\Upsilon_b(1,0)+\dot g^\Upsilon_b(0,\dot A)$
(III.H section 1); at $b = b_0$ it is the $\chi_Ku_{\exp}$ of III.I$''''''''''''$ (3.1) with the coefficients $q$. For
$\vec p\in\mathcal P$ with black hole parameter $b$, $h$ and $q$ small, put
$$P_5(h,\vec p,q) := P_4\big(h+h_{b,\mathrm{rem}}(q),\vec p\big)\tag{1.3}$$
(III.I$'''''''''$ (2.3)), the source's (11.228) with $h_{-S} = 0$: $q$ and $h$ enter only through
$h+h_{b,\mathrm{rem}}(q)$, both in the Ricci term and in the gauge term. Hence, at $b = b_0$, with $h' :=
h+h_{b_0,\mathrm{rem}}(q)$,
$$D_hP_5(h,\vec p,q) = L_{h',\vec p},\qquad D_qP_5(h,\vec p,q)(q') = L_{h',\vec
p}\big(h_{b_0,\mathrm{rem}}(q')\big),\tag{1.4}$$
the source's (11.231), and we write $R_q := L_{h',\vec p}-L_{h,\vec p}$ and $\Delta_q := D_{\vec p}P_5(h,\vec
p,q)-D_{\vec p}P_4(h,\vec p)$.

**Definition 1.3 (rotation rows).** Let $\mathcal N_{\mathrm{rot}} := \{(\mathrm v1,\lambda,k):(\lambda,k)\in\mathcal
M\}$, each with the coefficient space $\mathcal V_{1,\mathbb C}$ of all rotations (not III.I$'''''''''$'s complement
$\mathcal V'$ of the Killing ones, which is 0 at $b_0$), and for $\nu\in\mathcal N_{\mathrm{rot}}$ let $a_\nu = r_\nu =
t_*^{-\lambda}(\log t_*)^k$, $\omega_\nu$, $m_\nu$, $h_\nu$, $\vartheta_\nu$ and $\vartheta_{\nu,\sharp}$ be given by
III.I$'''''''''$ Definition 2.1, which III.I$''''''''''$ section 1 extends verbatim to every triple. From here on
$\mathcal P$ is III.I$'''''''''$'s space enlarged by the conjugation-symmetric tuples $(W_\nu)_{\nu\in\mathcal
N_{\mathrm{rot}}}$, and $h_{\mathrm{tot}}(\vec p)$, $\vartheta_{\mathrm{tot}}(\vec p)$ (III.I$'''''''''$ Definition 2.3)
are summed over $\mathcal N\cup\mathcal N_{\mathrm{rot}}$; so $P_4$ and $P_5$ take $\vec p$ in the enlarged $\mathcal
P$. A rotation row is given the rate $\mathrm{Re}\,\lambda+1$: at $b_0$ every rotation is Killing, so $h_{\mathrm v1} =
0$ and $m_\nu(W)$ has $K^+$-weight $\mathrm{Re}\,\lambda+1-\epsilon>\alpha-2$ (III.I$'''''''''$ Lemma 2.2 (e)), and no
level of III.I$'''''''''''$ or Theorem 3.1 eliminates it; its coordinate is fixed in Theorem 3.1 by the expansion (Step
4'). The parts III.I$''''''''$-III.I$'''''''''''''$ hold with the enlarged $\mathcal P$: III.I$'''''''''$ Lemmas 2.2 and
2.4-2.6 hold for $\nu\in\mathcal N_{\mathrm{rot}}$ (with $e_\nu = \lambda$ and $\kappa_\nu = \mathrm{Re}\,\lambda+4$);
each $h_\nu(W)$ is supported in $\mathcal C$ with $\iota^+$-exponents $(\lambda,k)+\mathcal F$, in $\mathcal M$ below 2
(III.I$''''''''$ (1.1)) and in $\mathcal E_\sharp$ above (III.I$''''''''''''$ section 1), so (H3) holds and
$h_{\mathrm{tot}}(\vec p)\in\mathcal X^\infty$; and $f^\nu_{h,\vec p} = L_{h,\vec p}m_\nu+r^\nu_{h,\vec p}$ with
$r^\nu_{h,\vec p}$ of $K^+$-weight $\mathrm{Re}\,\lambda+a_K-\epsilon>\alpha$ and plain $\iota^+$-weight
$\mathrm{Re}\,\lambda+2+\lambda_\sharp-\epsilon>w_+$ (III.I$'''''''''$ (2.5)), so these rows enter the constructions
exactly as the rows of $\mathcal N$ do.

## 2. The augmented operator

**Lemma 2.1 (towers near $b_0$).** For $b$ near $b_0$ the states of III.G$''$ Table 1.1 for $L_b$ and their companions
$\breve h^{(\mu),j}_{b,\tau}$ can be chosen smooth in $b$, equal at $b_0$ to those of III.G$''$, with leading terms at
$\partial X$ that do not depend on $b$; the rotation state $h_{b,\mathrm v1}\in\mathcal A^3$ is smooth in $b$, vanishes
at $b_0$ and not at a rotating $b$; and $\dot g_b$ is smooth in $b$. Then $\partial_b\breve
h^{(\mu),j}_{b,\tau}(Y)\in\mathcal A^{(\mu-j)+\mathcal E_{\mathrm{ind}}}$, and for $a = \chi_+t_*^{-z}(\log t_*)^k$ the
tensor $\partial_b(\chi_KT_{\rho,b}(a))$ is polyhomogeneous at $\iota^+$ with exponents in $z+d_\rho+\mathcal
E_{\mathrm{ind}}$ and, for v1, $z+3$; all lie in $z+d_\rho$ plus at most two increments of $\Lambda$ ($(2,0)\in\mathcal
E_{\mathrm{ind}}$, III.I$'''''''''$ section 1).

*Proof.* The pure gauge states and their companions are $\delta^*_{g_b}\omega^{\le k}_b$ with $\omega^{\le
k}_b\in\ker\Box^\Upsilon_b$ polynomial in $t_*$ and smooth in $b$ (III.D$'''$ Proposition 3.1); by the remark closing
III.D$'''$ Lemma 2.1 their leading terms at $\partial X$ are the Minkowski model solutions, which do not depend on $b$
and which (R4) fixes uniquely, no root lying at $\mu-k$. (The tower relations (2.1) alone fix a companion's leading term
only modulo the indicial kernel at $\mu-j$, III.G$''$ Lemma 2.2; it is III.D$'''$'s construction that fixes it.) The
physical states at $-2$ ($K = 0$) are III.F$''''$ Proposition 5.1's, smooth in $b$ with the $b$-independent leading term
$\bar h_\tau(Y)$. Composing each family with the inverse of the smooth invertible map $Y\mapsto$ (its leading
coefficient), normalised to be the identity at $b_0$, keeps everything at $b_0$, so Definition 1.2 at $b_0$ is
III.I$''''''''''''$'s $\chi_Ku_{\exp}$. The corrections lie in $\mathcal A^{(\mu-j)+\mathcal E_{\mathrm{ind}}}$ with
$\mathcal E_{\mathrm{ind}}$ independent of $b$ (III.G$''$ section 2, III.D$'''$ Proposition 3.1, III.F$''''$ Proposition
5.1), so their $b$-derivatives do too. The rotation state $h_{b,\mathrm v1}(V) = \delta^*_{g_b}\omega^{(-1)}_{b,\mathrm
v1}(V)\in\mathcal A^3$ vanishes at $b_0$, where every rotation is Killing, but not at a rotating $b$ (III.D$'''$
Proposition 3.1 (3)); its $b$-derivative lies in $\mathcal A^3$ and gives the $\iota^+$-exponent $z+3$. $\dot
g^\Upsilon_b$ is the gauge-corrected derivative of the Myers-Perry family, smooth in $b$; its leading term may depend on
$b$ (through the mass), which is harmless, $b_{\mathrm{rem}}$ having order $(\alpha-1)-$. The $\iota^+$-statement
follows as in III.I$''''''''''''$ section 1 (the leading part of $T_\rho(a)$ is homogeneous of degree $-z-d_\rho$).
$\square$

**Lemma 2.2 (the augmentation; the source's Remark 11.64).** Let $q\in\mathcal Q$.

(a) At $b = b_0$, $h_{\mathrm{rem}}(q) := h_{b_0,\mathrm{rem}}(q)$ is real, linear in $q$, supported in
$\mathrm{supp}\,\chi_K\cap\{t^\flat_*\ge10\}$, so away from $\mathscr I^+$, of $K^+$-order $(\alpha-2)-$, and at
$\iota^+$ partially polyhomogeneous with exponents in $\mathcal E_\sharp\cup\mathcal E^\natural$ to the order
$(3+\eta_2)-$, of plain weight $\ge\lambda_\sharp$; each seminorm is bounded by one of $q$.

(b) For $b$ near $b_0$, $L_bh_{b,\mathrm{rem}}(q)$ has $K^+$-order $\alpha-$, uniformly and smoothly in $b$.

(c) Let $\psi\in C^\infty(M)$ vanish near $K^+$ and equal 1 near $\mathrm{supp}(1-\chi_K)$ (a closed set disjoint from a
neighbourhood of $K^+$). Then $h+\psi h_{\mathrm{rem}}(q)\in\mathcal X^\infty$, small for $(h,q)$ small.

*Proof.* (a) III.I$''''''''''''$ section 1: $h^{\le1}_{b_0,\mathrm s1}(S_{\mathrm{rem}})$ has $K^+$-order $(\alpha-2)-$
and $\iota^+$-order $(\alpha+1)-$ ($h_{b_0,\mathrm s1}\in\mathcal A^3$, $\breve h^1_{b_0,\mathrm s1}\in\mathcal A^2$);
$\dot g(b_{\mathrm{rem}})$ has $K^+$-order $(\alpha-1)-$ and $\iota^+$-order $(\alpha+1)-$ (weights 2 and 3, III.H
section 1); a polyhomogeneous term $t_*^{-z}$ of $Y_\rho$ gives $K^+$-rate $>\alpha-2$ (Definition 1.1) and
$\iota^+$-exponent $z+d_\rho\in\mathcal E_\sharp$, plus the profiles' corrections, in $\mathcal E^\natural$; a conormal
part of order $(3+\eta_2-d_\rho)-$ gives $\iota^+$-order $(3+\eta_2)-$ and $K^+$-order above $\alpha-2$.
$\mathrm{supp}\,\chi_K\subset\{t^\flat_*\ge10\}$ by III.I (1.2). (b) By the tower relations for $L_b$ (III.G$''$ Lemma
2.6), $L_bT_{\rho,b}(Y)$ consists, near $K^+$, of the terms with $Y^{(k_\mu+1)}$ and $Y^{(k_\mu+2)}$, of $K^+$-order at
least the rate plus $k_\mu+1$, which is $\ge\lambda_\sharp+3>\alpha$ for the polyhomogeneous parts and $>\alpha$ for the
conormal ones (as in III.I$''''''''''''$ Lemma 2.4's proof); $L_bh^{\le1}_{b,\mathrm s1}(S) = S''(L_2h+L_1\breve
h^1)+S'''L_2\breve h^1$, of $K^+$-order $(\alpha-2)-+2$; $L_b\dot g_b(b_{\mathrm{rem}}) = b_{\mathrm{rem}}'L_1\dot
g_b+b_{\mathrm{rem}}''L_2\dot g_b$, of $K^+$-order $(\alpha-1)-+1$; and $[L_b,\chi_K]$ is supported away from $K^+$.
Smoothness in $b$ by Lemma 2.1. (c) $\psi h_{\mathrm{rem}}(q)$ vanishes near $K^+$ and near $\mathscr I^+$ and for
$t_*<1$, and by (a), the requirement $\mathcal E_+\supset(\mathcal E_\sharp\cup\mathcal
E^\natural)\cap\{\mathrm{Re}<3+\epsilon_+\}$ and (H5) it has the $\iota^+$-data $(\mathcal E_+,a_+)$. $\square$

**Lemma 2.3 (the perturbation).** Let $u\in\bigcap_\epsilon H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\beta'_+,w-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}$ with $w>0$ and
$\beta'_+\in(\frac32-(\delta_\sharp-\epsilon_+),\frac32)$. Then $R_qu$ is supported in $\mathrm{supp}\,\chi_K$, vanishes
near $\mathscr I^+$, and lies in $\mathcal Y^0_2(\beta)$ for every $\beta<w+\alpha-2$; each seminorm is bounded by
$C\|q\|$ times a seminorm of $u$, uniformly for $(h,\vec p,q)$ small.

*Proof.* $L_{h'',\vec p} = L^{g'',g_0}$ with $g'' = g_0+h_{\mathrm{tot}}(\vec p)+h''$ (III.I$'''''''''$ Lemma 2.5), and
$R_q = \int_0^1\partial_sL^{g_0+h_{\mathrm{tot}}(\vec p)+h+sh_{\mathrm{rem}}(q),g_0}\,ds$. The coefficients of
$L^{g,g_0}$ are smooth functions of $g$ and its first two derivatives (and of $g_0$), so $R_q$ is a second-order
operator whose coefficients are linear in $h_{\mathrm{rem}}(q)$ and its first two derivatives, times smooth functions;
it is supported in $\mathrm{supp}\,\chi_K$. As in III.I Proposition 4.1 (4.2), with $h_{\mathrm{rem}}(q)$ in place of
$h$: at $K^+$ the coefficients have the weight $(\alpha-2)-$ of $h_{\mathrm{rem}}(q)$ (Lemma 2.2 (a)), so $R_qu$ has
$K^+$-weight $(w+\alpha-2)-$; at $\iota^+$ they have weight $\ge\lambda_\sharp$ and each derivative gives a factor
$\rho_+$, so $R_qu$ has the plain weight $\beta'_++2+\lambda_\sharp-\epsilon>w_+$ (as
$\beta'_+>\frac32-\delta_\sharp+\epsilon_+$); near $\mathscr I^+$ it vanishes. These are the requirements of $\mathcal
Y^0_2(\beta)$ (III.I$'''''''''$ section 1), the $\iota^+$-index set being void below $w_+$. $\square$

**Lemma 2.4 (the parameter derivatives; the source's Lemma 11.65 and Remark 11.64).** At $b = b_0$, for $(h,\vec p,q)$
small:

(a) for a row $\nu$ and $W\in\mathcal W_{\tau,\mathbb C}$, $\Delta_q(W_\nu = W) = R_q(h_\nu(W))$, which has $K^+$-order
$\infty$ and plain $\iota^+$-weight $>w_+$, and lies in $\mathcal Y^0_2(\beta)$ for every $\beta$, with norm
$O(\|q\||W|)$;

(b) in the directions $S$, $S^{(0)}_1$, $\Delta_q$ takes values in the sections supported in $\mathrm{supp}\,\chi_K$
away from $K^+$ and $\mathscr I^+$, of plain $\iota^+$-weight $>w_+$, so in every $\mathcal Y^0_2(\beta)$, with norm
$O(\|q\|)$;

(c) in the direction $b$, $\Delta_q(b')\in\mathcal Y^\natural_2(\alpha-)$ with norm $O(\|q\||b'|)$; so $D_bP_5(h,\vec
p,q)(b')\in\mathcal Y^\natural(\alpha-)$: the linearisation in $b$ has the full $K^+$-order, the source's Lemma 11.65.

*Proof.* (a) $P_4$ depends on $W_\nu$ through $h_\nu(W_\nu)$ in $g'$ and $\vartheta_{\nu,\sharp}(W_\nu)$ in
$\vartheta_{\mathrm{tot}}$ (III.I$'''''''''$ (2.3)), so $D_{W_\nu}P_5(h,\vec p,q)(W) = L_{h',\vec
p}h_\nu(W)+\delta^*_{g_0,E_C}\vartheta_{\nu,\sharp}(W)$, and $\Delta_q = R_q(h_\nu(W))$. $h_\nu(W)$ is supported in
$\mathcal C$, whose closure meets $\partial M$ only in a compact subset of $(\iota^+)^\circ$, and lies in $\mathcal
A^{(\lambda,k)+\mathcal F}$ there (III.I$'''''''''$ Lemma 2.5); Lemma 2.3's computation gives the $\iota^+$-weight
$\ge\lambda_\sharp+\mathrm{Re}\,\lambda+2-\epsilon>w_+$.

(b) $h_{\mathrm{rem}}(q)$ does not depend on $S$, $S^{(0)}_1$, so $\Delta_q(S') =
\int_0^1(D_SL_{h+sh_{\mathrm{rem}}(q),\vec p})(S')\big(h_{\mathrm{rem}}(q)\big)\,ds$, where $D_SL$ is the derivative of
$L^{g'',g_0}$ in $S$ through $g_0$ and $h_{\mathrm{tot}}(\vec p)$. By III.I$'''''''$ (1.3) $g_0$ depends on $S$,
$S^{(0)}_1$ only on $\mathrm{supp}(1-\chi_K)$, and the terms of $h_{\mathrm{tot}}$ that depend on them are supported in
$\mathcal C$ (III.I$'''''''$ Lemma 2.2); their derivatives have $\iota^+$-order $\ge2$ ($\partial_Sg_{\vec
p}\in\rho_+^2C^\infty$ near $(\iota^+)^\circ$, III.I$'''''''$ Lemma 1.3 (c); $h^{(0)}_{\mathrm s1}(S)\in\mathcal
A^{\mathcal G+1}$, III.I$'''''''$ Lemma 2.2). So $\Delta_q(S')$ is supported in
$\mathrm{supp}\,\chi_K\cap(\mathrm{supp}(1-\chi_K)\cup\bar{\mathcal C})$, whose closure meets $\partial M$ only in
$(\iota^+)^\circ$, with $\iota^+$-weight $\ge2+\lambda_\sharp+2-\epsilon>w_+$.

(c) On the interior of $\chi_K^{-1}(1)$, a neighbourhood of $K^+$, $g_0 = g_b$ and $h_{\mathrm{tot}}(\vec p)$ consists
of terms supported in $\mathcal C$, and
$$P_5(h,\vec p,q)-P_4(h,\vec p) = \int_0^1L_{h+sh_{b,\mathrm{rem}}(q),\vec p}\big(h_{b,\mathrm{rem}}(q)\big)\,ds =
L_bh_{b,\mathrm{rem}}(q)+\int_0^1\big(L_{h+sh_{b,\mathrm{rem}}(q),\vec p}-L_b\big)\big(h_{b,\mathrm{rem}}(q)\big)\,ds$$
near $K^+$, $L_b$ the linearisation at $g_b$. The second term has coefficients of $K^+$-order $(\alpha-2)-$ ($h$ has
$a_K\ge4+\epsilon_K$, $h_{\mathrm{rem}}$ has $(\alpha-2)-$, the $\mathcal C$-terms vanish near $K^+$), applied to a
tensor of $K^+$-order $(\alpha-2)-$, so $K^+$-order $(2\alpha-4)-$, above $\alpha$ ($\alpha>4$); the first has
$K^+$-order $\alpha-$ by Lemma 2.2 (b), uniformly and smoothly in $b$, so its $b$-derivative has $K^+$-order $\alpha-$.
The $b$-derivative of the second at $b_0$ is a sum of products of a factor of $K^+$-order $(\alpha-2)-$ (from
$h_{b_0,\mathrm{rem}}(q)$, or from $h$, of order $\alpha-$) with $\partial_bh_{b,\mathrm{rem}}(q)b'$ or with
$\partial_bg_b(b')$; and $\partial_bh_{b,\mathrm{rem}}(q)b'$ has $K^+$-order $\ge2-\epsilon$: every coefficient of $q$
has rate $\ge2$ at every $b$ near $b_0$ (Definition 1.1: $\mathrm{Re}\,z>2$ for $\rho\ne\mathrm v1$;
$\mathrm{Re}\,z\ge2$ for v1, whose state $h_{b,\mathrm v1}$ gives the rate $\mathrm{Re}\,z$ once $b$ rotates; the
conormal parts have rate $>3$; $S_{\mathrm{rem}}$ and $b_{\mathrm{rem}}$ the rates $(\alpha-2)-$ and $(\alpha-1)-$), and
the states are smooth in $b$ (Lemma 2.1). So these products have $K^+$-order $\ge(\alpha-2)-+2 = \alpha-$. This is the
source's argument, with one change: a v1 coefficient of exponent $z\in\mathcal M$ would give only
$(\alpha-2+\mathrm{Re}\,z)-<\alpha$, which is why those terms are carried by the rotation rows (Definition 1.3). Away
from $K^+$, $\Delta_q(b')$ is supported in $\mathrm{supp}\,\chi_K$, away from $\mathscr I^+$, and is
$\int_0^1\big((\partial_bL)(b')h_{b_0,\mathrm{rem}}(q)+L(\partial_bh_{b,\mathrm{rem}}(q)b')\big)ds$ up to terms
quadratic in $h_{\mathrm{rem}}$: $\partial_bL$ has coefficients of $\iota^+$-order $\ge2$ ($\partial_bg_b$, of weight 2,
III.H section 1; $h^{(0)}(\dot b)\in\mathcal A^{\mathcal G}$, III.I$'''''''$ Lemma 2.2), giving the plain weight
$\ge2+\lambda_\sharp+2-\epsilon>w_+$; and $\partial_bh_{b,\mathrm{rem}}(q)$ has the $\iota^+$-exponents of Lemma 2.1, in
$\mathcal E^\natural$ (below 2 in $\mathcal M$: there $\mathcal E_\sharp$ is $\mathcal M$, III.I$''''''''''''$ section
1, and $\mathcal M+\mathcal E_{\mathrm{ind}}$ stays in $\mathcal M$ below 2), which $L$ maps to the exponents $\mathcal
E^\natural+2$ (the expansion of $L$ at $\iota^+$ adding elements of $\mathcal E^\iota_{\mathrm{ind}}$, increments of
$\Lambda$); its conormal parts are the $b$-derivatives of $T_{\rho,b}(Y^c_\rho)$ for the rows with $\mu_\rho\in(-1,0]$
(III.I$''''''''''''$ Step 4), of $\iota^+$-order $(3+\eta_2+\eta_E)-$ by Lemma 2.1 (the leading terms do not depend on
$b$, the corrections lie $\eta_E$ further), which $L$ maps to the weight $(5+\eta_2+\eta_E)->w_+$ (section 1), and those
of $S_{\mathrm{rem}}$, $b_{\mathrm{rem}}$, of $\iota^+$-order $(\alpha+3)-$. The terms quadratic in $h_{\mathrm{rem}}$
are as in Lemma 2.3. $\square$

**Lemma 2.5 (sources of order $\alpha-$; the losses).** III.I$'''''''''''$ Proposition 3.1, Lemma 3.2 and Theorem 4.1,
III.I$''''''''''''$ Theorem 3.1, and III.I$'''''''''''''$ Proposition 2.1 and Lemma 2.2 at the level $\alpha$, hold for
sources in $\mathcal Y^\natural(\alpha-)$, with the same conclusions; and the decomposition (3.1) of III.I$''''''''''''$
Theorem 3.1 can be taken independent of $\epsilon$, so that its coefficients lie in the classes (3.2) and $\tilde u$ in
(3.3) for every $\epsilon>0$ at once.

*Proof.* The conclusions are statements for every small $\epsilon>0$, and the source's $K^+$-weight enters the
constructions only through III.I$''$ Lemma 4.1 and III.A Proposition 4.2 (1) with $\beta_K = \alpha-\epsilon$
(III.I$'''''''''''$ Proposition 3.1's Step 0), through Step 0 of the expansion lemmas ($f'$ of $K^+$-weight
$\alpha-\epsilon$), and through the zf-weights $\alpha-1-j-\epsilon$ of the Taylor levels; a source of $K^+$-weight
$\alpha-\epsilon'$ for every $\epsilon'>0$ meets each of these for every $\epsilon$. For the independence: fix
$\epsilon_0>0$ such that no exponent at hand (of the pieces' coefficients and of the rows) has real part in
$[\alpha-2-3\epsilon_0,\alpha-2)\cup[\alpha-\epsilon_0,\alpha)$ (finitely many below every bound, and none at $\alpha-2$
or $\alpha$ by admissibility). For $\epsilon<\epsilon_0$ the constructions do not depend on $\epsilon$: the zero-energy
solves, III.G$''''$ Propositions 4.4 and 5.1 and the last-level inversion are applied to the same sources (the
thresholds $2+\eta_1$, $2+\eta_2$ and $\delta$ are fixed; the rounds of the level-3 loop stop when $\tau>\alpha-2$;
$\epsilon$ enters only the weights in which their outputs are estimated), the pairs removed in III.I$''''''''''''$ Lemma
2.4 with $\beta = \alpha-\epsilon$ are those of real part below $\alpha-\epsilon_0$, and the exponents dropped in its
Step 2 have zero coefficients. The level-3 construction depends on $\epsilon$ also through the weights $\tau_i(\epsilon)
= 1+\eta_2+i\epsilon_{\mathrm{ind}}-(2+i)\epsilon$, the switch $\alpha_\tau = \min(\tau,2-\delta)$ ($\delta$ fixed
independent of $\epsilon$), the order $\mu_3 = \tau-\epsilon$ of the expansions recorded in the zero-energy solve, and
the lowering of $\tau$ in III.I$'''''''''''$ Proposition 3.1's Step 4. We take $\epsilon_0$ so small that, for
$\epsilon<\epsilon_0$, none of these crosses an exponent at hand, a root, or a value excluded in III.G$''''$ Proposition
5.1 (finitely many conditions on the values at $\epsilon = 0$). III.G$''''$ Proposition 5.1 solves (5.3) by Mellin
inversion on $\mathrm{Re}\,\lambda = \alpha_\tau-2-j$, and moving that line without crossing a root does not change the
solution; the recorded expansions and the switch are then the same for every $\epsilon<\epsilon_0$. So the pieces, the
coefficients of (3.1) and $\tilde u$ are the same for every $\epsilon<\epsilon_0$, and the estimates hold for each.
$\square$

## 3. The decay of forward solutions ([Hin26] Corollary 11.66 at n = 4)

**Theorem 3.1 ([Hin26] Corollary 11.66 at n = 4).** Let $h\in\mathcal X^\infty$, $\vec p\in\mathcal P$ ($b = b_0$) and
$q\in\mathcal Q$ be small, and $F\in\mathcal Y^\natural(\alpha-)$. There is a unique $\vec p\,'\in\mathcal P$ (rotation
rows included, Definition 1.3) such that the forward solution $u$ of
$$L_{h+h_{\mathrm{rem}}(q),\vec p}\,u = F-D_{\vec p}P_5(h,\vec p,q)(\vec p\,')\tag{3.1}$$
satisfies III.I$'''''''''''$ (4.2): $u\in\bigcap_\epsilon H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\beta_+,\alpha-2-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}$ for every
$\beta_+<\min(\frac32,\min\mathrm{Re}\,\mathcal E_+)$, and $u = h_{\mathrm{rem}}(q')+h'$ with $q'\in\mathcal Q$ (so the
v1 coefficient has no term of exponent in $\mathcal M$) and
$$h'\in\bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal
E_\sharp,3+\eta_2-2\epsilon),\alpha-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-},\qquad D_hP_5(h,\vec p,q)(h') =
F-D_{\vec p}P_5(h,\vec p,q)(\vec p\,')-D_qP_5(h,\vec p,q)(q').\tag{3.2}$$
$\vec p\,'$, $q'$ and $h'$ are linear in $F$, with bounds uniform for $(h,\vec p,q)$ small.

*Proof.* Write $u(\vec p\,')$ for the forward solution of (3.1), and $\mathcal Z_\beta$ for the space of
III.I$'''''''''''$ (4.2) at the level $\beta$, or III.I$''''''''$ (4.2) for $\beta<3$.

*Step 0 (the forward solution).* $L_{h+h_{\mathrm{rem}}(q),\vec p} = L^{g'',g_0}$ is a wave operator with smooth
coefficients, close to $L_{h,\vec p}$ in every $C^k$ on every slab $\Omega_{1,T_1}$; II.E Proposition 3.4 gives a unique
forward solution on each slab, as for $L_{h,\vec p}$ (III.I$'''''''''$ Lemma 2.4), and these agree. So $u(\vec p\,')$
exists, is smooth, and is affine in $\vec p\,'$.

*Step 1 (the base level, at $h+h_{\mathrm{rem}}(q)$).* Fix an admissible $\alpha_1\in(2,\alpha-2)$ in III.I$''''''''$'s
sense. III.I$''''''''$'s hypotheses on the background ask $K^+$-order only above $\alpha_1$ (III.I$''''''''$ Proposition
4.1: $\alpha_1<\min(a_K,3)$; its Lemmas 3.1-3.2 take steps below $a_K-2$), so they hold for $h+h_{\mathrm{rem}}(q)$, of
$K^+$-order $(\alpha-2)-$ and with the other data of $\mathcal X$ (Lemma 2.2 (a), (c)). Split $\vec p\,' = \vec
p\,'_{<}\oplus\vec W$ with $\vec p\,'_<\in\mathcal P_{\alpha_1}$ (III.I$'''''''''''$ section 4) and $\vec W =
(W_\nu)_{\nu\in\mathcal N'}$. As in III.I$'''''''''''$ Theorem 4.1's proof (*III.I$''''''''$ Proposition 4.1 for
$P_4$*), III.I$''''''''$ Proposition 4.1 holds for $P_5$ at $(h,\vec p,q)$: $P_5$ is $P_3$ at
$(h+h_{\mathrm{rem}}(q)+\sum_\nu h_\nu(W_\nu),\vec p_3)$, the sum over the rows other than the motions (the rotation
rows included), up to the term $(\partial\delta^*_{g_0,E_C})\vartheta_{\mathrm{rows}}$, and in the direction $b$ also up
to $L(\partial_bh_{b,\mathrm{rem}}(q)b')$, of $K^+$-order $>2+\epsilon_K>\alpha_1$ (every coefficient of $q$ has rate
$>2+\epsilon_K$ at $b_0$, by (G) and Definition 1.1, and $\widehat{L_{b_0}}(0)\partial_bh_{b,\mathrm v1} = 0$ as
$h_{b_0,\mathrm v1} = 0$, so the v1 part has rate $\ge3$); all of these lie in III.I$''''''''$'s $\mathcal Y(\alpha_1)$
and are $O(|\vec W|+\|q\|)$, and so does $D_{\vec W}P_5 = D_{\vec W}P_4+\Delta_q$ (Lemma 2.4 (a); III.I$'''''''''$ Lemma
2.6 (b)) and $F$ (III.I$'''''''''''''$ Lemma 2.2's last sentence). So for every $\vec W$ there is a unique $\vec
p\,'_<(\vec W)\in\mathcal P_{\alpha_1}$, affine in $\vec W$, with $u(\vec p\,'_<(\vec W)\oplus\vec W)\in\mathcal
Z_{\alpha_1}$. Let $\mathcal P_0$ be the set of these $\vec p\,'$: the graph of $\vec W\mapsto\vec p\,'_<(\vec W)$.

*Step 2 (one level).* Choose admissible levels $\alpha_1 = \beta_0<\beta_1<\dots<\beta_K = \alpha$ (III.I$''''''''$'s
below 3, III.I$'''''''''''''$ Definition 1.1 above 3) with $\beta_{k+1}-\beta_k<\alpha-4$ and $\beta_{K-1}>4$; this is
possible as the admissible levels are dense. Let $\vec p\,'\in\mathcal P$ with $u := u(\vec p\,')\in\mathcal
Z_{\beta_k}$. By (3.1),
$$L_{h,\vec p}u = \tilde G-D_{\vec p}P_4(h,\vec p)(\vec p\,'),\qquad\tilde G := F-\Delta_q(\vec p\,')-R_qu,\tag{3.3}$$
and $\tilde G\in\mathcal Y^\natural(\beta_{k+1})$, resp. $\mathcal Y^\natural(\alpha-)$ for $k+1 = K$: $R_qu\in\mathcal
Y^0_2(\beta)$ for $\beta<\beta_k+\alpha-4$ (Lemma 2.3 with $w = \beta_k-2$; for $k = K-1$,
$\beta_{K-1}+\alpha-4>\alpha$), and $\Delta_q(\vec p\,')\in\mathcal Y^\natural(\alpha-)$ (Lemma 2.4). The rows enter
(3.3) through $D_{\vec p}P_4$ at $h$, whose defects $r^\nu_{h,\vec p}$ have the orders of III.I$'''''''''$ Lemma 2.6
(c), as $a_K\ge4+\epsilon_K$; at $h+h_{\mathrm{rem}}(q)$ the row directions differ from these by exactly $\Delta_q(\vec
W) = R_q(h_\nu(\vec W))$ (Lemma 2.4 (a)), supported in $\mathcal C$, so no row defect of the background
$h+h_{\mathrm{rem}}(q)$ enters. For $\beta_{k+1}>3$, $u_0 := u+\sum_{\nu\in\mathcal N\cup\mathcal
N_{\mathrm{rot}}}m_\nu(W'_\nu)$ ($W'_\nu$ the row components of $\vec p\,'$, the motions and the rotation rows included)
solves
$$L_{h,\vec p}u_0 = G' := \tilde G-f^S_{h,\vec p}(S')-f^b_{h,\vec p}(b')-f^{\mathrm s1}_{h,\vec
p}(S^{(0)\prime}_1)-\sum_{\nu\in\mathcal N\cup\mathcal N_{\mathrm{rot}}}r^\nu_{h,\vec p}(W'_\nu)\in\mathcal
Y^\natural(\beta_{k+1})$$
(III.I$'''''''''$ Lemma 2.6 (a), (c); III.I$''''''''''$ section 1; resp. $\mathcal Y^\natural(\alpha-)$), and has
$K^+$-weight $\min(\beta_k-2,\lambda_\sharp-1)-\epsilon>0$, with $\min(\beta_k-2,\lambda_\sharp-1)+a_K>\beta_{k+1}$, and
$\iota^+$-weight $\beta'_+$. III.I$'''''''''''''$ Lemma 2.2 (with Lemma 2.5 for $k+1 = K$) gives
$$u = \sum_{\nu\in\mathcal N_{\beta_{k+1}}}m_\nu\big(C^{k+1}_\nu(\vec p\,')\big)+\tilde u,\qquad\tilde u\in\mathcal
Z_{\beta_{k+1}},\qquad C^{k+1}_\nu(\vec p\,') := S^{h,\vec p,\beta_{k+1}}_\nu(G')-W'_\nu,\tag{3.4}$$
the $m_\nu(W'_\nu)$ of the rows outside $\mathcal N_{\beta_{k+1}}$ and of the rotation rows, of $K^+$-weight above
$\beta_{k+1}-2$ (Definition 1.3), being part of $\tilde u$. For $\beta_{k+1}<3$, III.I$''''''''$ Lemma 3.2 (transferred
to $P_4$ as in Step 1, with $\beta_{k+1}-\beta_k<a_K-2$) applied to $u$ gives (3.4) with the motion rows of $\mathcal
M_{\beta_{k+1}}\setminus\mathcal M_{\beta_k}$ and $C^{k+1}_\nu$ the $K^+$-coefficient $S_{\lambda,k}$ of $u$. In both
cases the coefficients of the rows of $\mathcal N_{\beta_k}$ vanish (III.I$''''''''''$ Corollary 2.3, as $u\in\mathcal
Z_{\beta_k}$), and $u\in\mathcal Z_{\beta_{k+1}}$ if and only if $C^{k+1}_\nu(\vec p\,') = 0$ for the rows $\nu$ of rate
in $[\beta_k-2,\beta_{k+1}-2)$, the *new rows* of the level.

*Step 3 (the elimination, level by level).* Let $\mathcal P_k := \{\vec p\,'\in\mathcal P_0:u(\vec p\,')\in\mathcal
Z_{\beta_k}\}$. We show by induction that $\mathcal P_k$ is the graph of an affine map from the coordinates $W_\nu$ of
the rows of rate $\ge\beta_k-2$ to the others. For $k = 0$ this is Step 1. On $\mathcal P_k$, $C^{k+1}$ is an affine
function of the free coordinates; we claim that in the coordinates of the new rows it is $-\mathrm{id}+A_k$, with
$A_k\to0$ as $(h,\vec p,q)\to(0,0,0)$. At the base point, $D_{\vec p}P_4(0,0)(W_\nu = W) = L_{b_0}m_\nu(W)$
(III.I$'''''''''$ Lemma 2.4) and $\Delta_q = 0$, $R_q = 0$, so $u(\vec p\,') = u_F-\sum_\nu m_\nu(W_\nu)$ with $u_F$ the
forward solution of $L_{b_0}u_F = F-D_{\vec p}P_4(0,0)(\vec p\,'_<)$; and $\vec p\,'_<$, and the coordinates fixed at
the earlier levels, do not depend on the coordinates of rows of higher rate, as $m_\nu(W_\nu)$ has no $K^+$-coefficient
at lower rows (as in III.I$'''''''''''$ Theorem 4.1's proof, *At $(0,0)$*). So $C^{k+1}_\nu = C^{k+1}_\nu(0)-W_\nu$
there. Near the base point, $C^{k+1}$ depends continuously on $(h,\vec p,q)$, uniformly for $\vec p\,'$ bounded: by
III.I$''''''''$ Proposition 4.1 (ii) and Lemma 3.3 (the levels below 3), III.I$'''''''''''''$ Lemma 2.3 and
III.I$'''''''''''$ Lemma 3.3 for the coefficients, III.I$'''''''''$ Lemma 2.6 for the $r^\nu$, and Lemmas 2.3-2.4 for
$R_q$ and $\Delta_q$, which are $O(\|q\|)$; $u(\vec p\,')$ is bounded in $\mathcal Z_{\beta_k}$ on bounded subsets of
$\mathcal P_k$ by the induction (finitely many levels, each losing finitely many derivatives). So $-\mathrm{id}+A_k$ is
invertible for $(h,\vec p,q)$ small, and $C^{k+1} = 0$ on $\mathcal P_k$ solves for the new coordinates as an affine
function of those of higher rate: $\mathcal P_{k+1}$ is a graph. At $k = K$ the free coordinates left are those of the
rotation rows ($\mathcal N_\alpha = \mathcal N$; a rotation row is a new row at no level, its rate
$\mathrm{Re}\,\lambda+1$ exceeding $\alpha-2$, Definition 1.3): $\mathcal P_K$ is the graph of an affine map $\vec
W^{\mathrm{rot}}\mapsto\vec p\,'(\vec W^{\mathrm{rot}})$. *Uniqueness:* if $u(\vec p\,'')\in\mathcal Z_\alpha$, then
$u(\vec p\,'')\in\mathcal Z_{\beta_k}$ for all $k$, so $\vec p\,''\in\mathcal P_0$ by Step 1's uniqueness and then $\vec
p\,''\in\mathcal P_K$; Step 4' fixes the rotation coordinates.

*Step 4' (the rotation coordinates).* For $\vec p\,'\in\mathcal P_K$, $u = u(\vec p\,')\in\mathcal Z_\alpha$ solves
(3.3), and III.I$''''''''''''$ Theorem 3.1 (as in Step 4) gives the v1 coefficient $\dot Y_{\mathrm v1}$ of its
expansion; let $C^{\mathrm{rot}}(\vec p\,')$ be the tuple of its polyhomogeneous coefficients at the exponents in
$\mathcal M$, an affine function of $\vec W^{\mathrm{rot}}$. The polyhomogeneous coefficients of III.I$''''''''''''$
(3.1) of rate below $\alpha-\epsilon$ are determined by $u$: if two such sums of towers differ by a tensor of
$K^+$-order $\alpha-\epsilon$, their lowest terms cancel, and the leading terms of the towers of distinct rows of
III.G$''$ Table 1.1 are linearly independent (distinct roots, types or degrees) and injective (III.G$''$ Lemma 1.2). At
$(0,0,0)$, $u = u_F-\sum_\nu m_\nu(W_\nu)$ (Step 3), and for $\nu = (\mathrm v1,\lambda,k)\in\mathcal N_{\mathrm{rot}}$,
$m_\nu(W)$ is $\chi_KT_{\mathrm v1}(t_*^{-\lambda}(\log t_*)^kW)$ up to $K^+$-order $\ge\mathrm{Re}\,\lambda+4>\alpha$
(III.I$''''''''''$ Lemma 2.1 (a): the terms $i\le2$ of $\sum_ia_\nu^{(i)}\breve h^i_{\mathrm v1}(W)$ are the v1 tower of
III.G$''$ Definition 2.5 at $b_0$, both being $\delta^*_{g_{b_0}}$ of the polynomial gauge 1-forms of III.D$'''$ (3),
with $\breve h^0_{\mathrm v1} = h_{b_0,\mathrm v1} = 0$; the term $i = 3$ and the $dt_*$-term have $K^+$-order
$\ge\mathrm{Re}\,\lambda+4$). So $C^{\mathrm{rot}}$ has derivative $-\mathrm{id}$ in $\vec W^{\mathrm{rot}}$ at
$(0,0,0)$; it depends continuously on $(h,\vec p,q)$, uniformly for $\vec p\,'$ bounded, by the lemmas of Step 3 and
III.I$''''''''''$ Proposition 3.1 for the exponents below 2. Hence for $(h,\vec p,q)$ small there is a unique $\vec
W^{\mathrm{rot}}$ with $C^{\mathrm{rot}} = 0$, and this fixes $\vec p\,'$.

*Step 4 (the expansion).* With $\vec p\,'$ of Step 4', $u\in\mathcal Z_\alpha$ solves (3.3) with $\tilde G\in\mathcal
Y^\natural(\alpha-)$, and $R_qu$ has $K^+$-weight $(2\alpha-4)-$. By the uniqueness in III.I$'''''''''''$ Theorem 4.1
(Lemma 2.5), $\vec p\,' = \vec p\,'_{h,\vec p}(\tilde G)$, so III.I$''''''''''''$ Theorem 3.1 (Lemma 2.5,
III.I$'''''''''''''$ Proposition 2.4) applies: $u = \chi_Ku_{\exp}+\tilde u$, with an $\epsilon$-independent
decomposition. Its coefficients $q' := (\dot S_{\mathrm{rem}},\dot b_{\mathrm{rem}},(\dot Y_\rho))$ lie in $\mathcal Q$:
(3.2) of III.I$''''''''''''$ for every $\epsilon$; every term of $\chi_Ku_{\exp}$ has $K^+$-order
$\ge\alpha-2-\epsilon$, so the polyhomogeneous coefficients of rate $\le2<\alpha-2-\epsilon$ vanish, which is Definition
1.1's $\mathrm{Re}\,z>2$, and $\dot Y_{\mathrm v1}$ has no exponent in $\mathcal M$ (Step 4'), which is its $\mathcal
E^\alpha_{\mathrm v1}$; conjugation symmetry by III.I$''''''''''''$ Step 6. Put $h' := \tilde u$, which satisfies
(3.2)'s first statement by III.I$''''''''''''$ (3.3). As $\chi_Ku_{\exp} = h_{\mathrm{rem}}(q')$ (Definition 1.2 at
$b_0$), (1.4) gives $D_hP_5(h')+D_qP_5(q') = L_{h+h_{\mathrm{rem}}(q),\vec p}(h'+h_{\mathrm{rem}}(q')) =
L_{h+h_{\mathrm{rem}}(q),\vec p}u$, which is (3.2) by (3.1). *Linearity and bounds:* every map used is linear and
bounded, uniformly for $(h,\vec p,q)$ small, and the inverses $(-\mathrm{id}+A_k)^{-1}$ are bounded. $\square$

**Remark 3.2 (orders; the source's Remark 11.64 (1) and the sentence after Corollary 11.66).** (1) *The background.*
$h+h_{\mathrm{rem}}(q)$ has $K^+$-order $(\alpha-2)-$ only, against $a_K\ge4+\epsilon_K$ for $h$; Theorem 3.1 never uses
the linear theory at it beyond III.I$''''''''$'s levels below $\alpha-2$ (Step 1), which ask no more. (2) *The class
reproduces.* $h'$ has the $\mathscr I^+$-data $(\langle\mathcal E^C_I\rangle,\ell_I)$, the $\iota^+$-data $(\mathcal
E_\sharp,(3+\eta_2)-)$ and the $K^+$-order $\alpha-$. This is the class of $h$ if (H2) is read as "$K^+$-order
$\alpha-$" with $\alpha\le4+\epsilon_K$ the level used, $a_I = \ell_I$ (off the exclusion sets of III.I$''''''''''$
(H4)), and $a_+<3+\eta_2$ by (H5): every use of $a_K$ in III.I$''''''''$-III.I$'''''''''''''$ is a strict inequality at
an admissible level, or the membership of $f^b_{h,\vec p}$ in $\mathcal Y_2(\alpha)$ (III.I$'''''''''$ Lemma 2.6 (a)),
which becomes $\mathcal Y_2(\alpha-)$ and is accepted by Lemma 2.5. So Theorem 3.1 proves for $h'$ the decay at
$\mathscr I^+$, $\iota^+$ and $K^+$ that it assumes of $h$, as the source's Corollary 11.66 does. (3) *Nonlinear
errors.* As in the source, $P_5(h,\vec p,q)$ for general small $(h,\vec p,q)$ is not of the class of $F$; the
parameterisation that accounts for this is section 12, the next part.

## 4. Findings, labels and sources

(I$''''''''''''''$1) *Linearise at $h$.* The source applies Theorem 11.59 at $h+h_{\mathrm{rem}}(q)$ "verbatim". At $n =
4$ three steps would fail there: III.I$'''''''''''$'s one step to the order $\alpha$ needs $a_K\ge4+\epsilon_K$,
III.I$'''''''''$'s $r^\nu$ needs $a_K>\alpha+1-\lambda_\sharp$, and a series in $q$ around $h$ loses two derivatives per
term. Taking the exact forward solution at $h+h_{\mathrm{rem}}(q)$ (no loss) and raising its decay with the theory at
$h$, level by level (III.I$'''''''''''''$), avoids all three: the steps are shorter than $\alpha-4$, $r^\nu$ is only
ever taken at $h$, and the rows' derivatives differ only by $R_q(h_\nu(W))$, supported away from $K^+$.

(I$''''''''''''''$2) *Towers near $b_0$.* The source's Lemma 11.65 uses towers for $L_b$ at $b$ near $b_0$; at $n = 4$
the states are smooth in $b$ (III.D$'''$ Proposition 3.1, III.F$''''$ Proposition 5.1), and normalised by their leading
terms, which the Minkowski model fixes, their $b$-derivatives carry only the increments of $\Lambda$ at $\iota^+$. This
is what keeps the linearisation in $b$ inside the log count (III.I$'''''''''''''$ Lemma 1.3).

(I$''''''''''''''$3) *The losses.* The $n = 4$ linear theory loses an $\epsilon$ at $K^+$; read with the orders $w-$ and
with constructions independent of $\epsilon$ (Lemma 2.5), the class of $h'$ is that of $h$ (Remark 3.2 (2)). With a
fixed loss, the boost and black hole parameter coefficients would lose an $\epsilon$ at each application.

(I$''''''''''''''$5) *Rotation rows (D281).* At the non-rotating $b_0$ the v1 rows carry no parameter
(III.I$'''''''''$), and a v1 term of exponent $z\in\mathcal M$ of the expansion has rate $z+1>\alpha-2$, so the source's
bookkeeping puts it into $q$. But $h_{b,\mathrm v1}\ne0$ at a rotating $b$, where the same term has rate $z<2$, and the
$b$-derivative of $P_5$ then has $K^+$-order $(\alpha-2+z)-<\alpha$. Rows of all rotations at the exponents of $\mathcal
M$ (Definition 1.3) carry these terms; they enter $P_5$ through $h_\nu$, supported away from $K^+$, and $\vartheta_\nu$,
of $K^+$-weight $\mathrm{Re}\,\lambda+4$, and are fixed by the expansion (Step 4'). Whether the source's Lemma 11.65
meets the same term at a non-rotating Kerr $b_0$ was not adjudicated.

(I$''''''''''''''$4) *Deferred.* $h_{-S} = 0$ here (the source allows it); the exterior part III.C$'$ adds
$\chi_-h_{-S}$, supported in $t_*\le2$. The source's Corollary 11.67 is sketched there, uses the exterior linear
stability, and is not used later; it is deferred to after III.C$'$.

*Labels.* Definitions 1.1-1.2 and (1.4) are the source's (11.227)-(11.229) and (11.231) at $n = 4$; Lemma 2.2 is its
Remark 11.64; Lemma 2.4 (c) its Lemma 11.65; Theorem 3.1 its Corollary 11.66 without the tame estimates (which section
13 at $n = 4$ takes from the parts it uses); Lemmas 2.1, 2.3, 2.5, Definition 1.3, Step 4' and Remark 3.2 (2) are new at
$n = 4$.

*Sources.* [Hin26] pp. 292-296 (section 11.8.3: Definition 11.63, Remark 11.64, (11.225)-(11.232), Lemma 11.65,
Corollaries 11.66-11.67) and p. 279 (Remarks 11.61-11.62), read at source. Inputs: II.E Proposition 3.4; III.A
Proposition 4.2; III.D$'''$ Lemma 2.1, Proposition 3.1; III.F$'$ section 2; III.F$''''$ Proposition 5.1; III.G$''$ Table
1.1, Lemma 1.2, section 2, Definition 2.5, Lemma 2.6; III.G$''''$ Propositions 4.4, 5.1; III.H section 1; III.I (1.2),
Proposition 4.1; III.I$''$ Lemmas 4.1-4.2; III.I$'''''''$ (1.3), Lemmas 1.3, 2.2; III.I$''''''''$ (4.2), Lemmas 3.2-3.3,
Proposition 4.1; III.I$'''''''''$ (2.3), Lemmas 2.4-2.6; III.I$''''''''''$ section 1, Lemmas 1.2, 2.1, Corollary 2.3,
Proposition 3.1; III.I$'''''''''''$ section 4, Proposition 3.1, Lemmas 3.2-3.3, Theorem 4.1; III.I$''''''''''''$ section
1, Lemma 2.4, Theorem 3.1; III.I$'''''''''''''$ Definition 1.1, Lemmas 1.3, 2.2-2.3, Propositions 2.1, 2.4.
