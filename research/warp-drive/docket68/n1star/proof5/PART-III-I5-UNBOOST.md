# Part III.I$''''$. Undoing the boost, n = 4 ([Hin26] section 11.4.2)

*Status.* Proved (D263: verifier 111 read the D261 repairs). Verified (D261: the hundred-and-tenth verifier; no major
finding, two minor ones and nine nits seated, to be read). Written (D260). This part proves, at spatial dimension $n =
4$, [Hin26] section 11.4.2 (pp. 241-247): the correction terms that let a source generate the boost term of Part
III.I$'''$ (Definition 11.23, Lemma 11.24), the identity (11.76)-(11.78b) behind them, the augmented gauge-fixed
Einstein operator (Definition 11.25), its linearisation in the boost parameter (Lemma 11.28), and the elimination of
boosts (Proposition 11.30 and (11.95)): the map from the parameter of the source term to the boost parameter of the
forward solution is invertible near the identity, so a forward solution with no boost term, growing like
$t_*^{2-\alpha_K} = o(t_*)$, can be found.

*What n = 4 changes.* The scheme is the source's. Four things differ. There are no logarithms: the correction $h^{(-1)}$
has index set $(2,0)\cup(2+\mathcal E_{\mathrm{ind}})$ at $\iota^+$, and its linearised curvature has
$(4,0)\cup(4+\mathcal E_{\mathrm{ind}})$ with nothing to cancel, where the source must cancel a $(3,1)$-coefficient (its
(11.82)). The source terms at $\iota^+$ begin at order 4, the source's 3, above every weight Part III.I$'''$ uses, so
the source's splitting of the source term (its (11.86), Remark 11.29) and its special treatment of $(3,0)$-terms are not
needed. III.B's boosts are centred at $t = 0$ and III.D$''$'s model states at $\bar t = 0$; $\bar t-t\to C'$, a
translation, and the generalised state is re-centred accordingly (Lemma 1.2). And the augmented operator is taken in the
form of the source's Remark 11.27, so that its linearisation is exactly III.I's operator with a shifted perturbation,
and Parts III.I-III.I$'''$ apply to it as stated. Everything is at $b = b_0$, as in III.I Theorem 5.3. Notation: Parts
II.E, III.B, III.D$''$, III.F$'''$, III.H and III.I-III.I$'''$; no instrument is used.

## 1. Setting

*Cut-offs.* $\chi^\flat_K,\chi_K,\chi^\sharp_K,\chi_{\mathrm{IVP}},\chi^\sharp_{\mathrm{IVP}},\chi_r$ are III.B section
5's, with III.I (1.2). In this part $\chi_K$ is III.B's: smooth on $M$, equal to 1 near $K^+$ (on
$\mathrm{supp}\,\chi^\flat_K\supset\{|x|<t/10,\ t>60R_1\}$) and to 0 near $\mathscr I^+$
($\mathrm{supp}\,\chi_K\subset\{|x|<t/2\}$), supported in $\{t^\flat_*\ge10\}$, with Cartesian derivatives
$\partial\chi_K\in\rho_+C^\infty$ near $(\iota^+)^\circ$ (III.I Lemma 4.3's proof). Write $\chi^H_K :=
\chi_+(t_*)\chi_c(|x|/t_*)$ for III.H's cut-off (1.2), the one in Part III.I$'''$ Proposition 2.1, and
$$\mathcal C := \mathrm{supp}\,\chi_K\cap\mathrm{supp}(1-\chi_K),$$
whose closure meets $\partial M$ only in a compact subset of $(\iota^+)^\circ$ (III.I Lemma 4.3's proof). Every
derivative of $\chi_K$ is supported in $\mathcal C$, and $\chi^\flat_K = 0$ on $\mathcal C$, as
$\mathrm{supp}\,\chi^\flat_K\subset\mathrm{int}\,\chi_K^{-1}(1)$.

*Boosts.* For $S = S_w\in\mathcal S_1$ (III.B section 5) let $\bar\omega(S) := t\,d(|x|S)-|x|S\,dt = t\,w\cdot
dx-(w\cdot x)dt$, $\eta := -dt^2+dx^2$, $X_S := \eta^{-1}\bar\omega(S)$, $\Theta :=
\chi_r(|x|)\chi^\sharp_{\mathrm{IVP}}(1-\chi^\flat_K)$, $V(S) := \frac12\Theta X_S$ and $\phi_S := \exp V(S)$ (III.B
Lemma 5.1), and
$$g_S := g_{b_0,b_0,-S} = (1-\chi_K)\phi^*_{-S}g_{b_0}+\chi_Kg_{b_0}\tag{1.1}$$
(III.I (1.1) at $b = b_0$). $\Theta = 1$ on $\mathcal C\cap\{t\ge T_1\}$ for some $T_1$: there $\chi^\flat_K = 0$,
$|x|\ge t/10$ (so $\chi_r = 1$ once $t\ge60R_1$), and $t_{\mathrm{IVP}} = t-C''>-|x|/10$ (so $\chi^\sharp_{\mathrm{IVP}}
= 1$). Put
$$w(S) := g_{b_0}(X_S,\cdot) = g_{b_0}\eta^{-1}\bar\omega(S),\qquad\text{so that}\quad g_{b_0}(V(S),\cdot) =
\tfrac12\Theta w(S).$$

*Conventions.* $\delta^*_g$ is the symmetrised covariant derivative and $\delta_gh = -\nabla^\kappa h_{\kappa\mu}$
(III.B section 6), so $\mathcal L_Xg = 2\delta^*_g(g(X,\cdot))$, and with $a\otimes_sb := \frac12(a\otimes b+b\otimes
a)$,
$$[\delta^*_g,\chi]\omega = d\chi\otimes_s\omega,\qquad[\delta_g,\chi]h = -\iota_{g^{-1}d\chi}h.\tag{1.2}$$
$P(g,g_0)$, $\Upsilon^{E_\Upsilon}(g,g_0)$, $\delta^*_{g_0,E_C}$ and $\delta_{g_0,E_\Upsilon}$ are III.B Definition
6.1's, and $L^{g,g_0} := D_1P(\cdot,g_0)$ at $g$ (III.B's $L_{g,g_0}$), $L_b := L^{g_b,g_b} =
D_{g_b}\mathrm{Ric}+\delta^*_{g_b,E_C}\delta_{g_b,E_\Upsilon}G_{g_b}$ (III.B (6.8)). Three identities are used
throughout. (i) $\Upsilon^{E_\Upsilon}(g,g) = 0$ for every $g$ (III.B (6.3): $\Gamma(g)-\Gamma(g) = 0$, $g-g = 0$), so
$(D_1+D_2)\Upsilon^{E_\Upsilon}(g,g) = 0$ and $P(g,g) = \mathrm{Ric}(g)$. (ii) $D_1\Upsilon^{E_\Upsilon}(g,g) =
-\delta_{g,E_\Upsilon}G_g$: by III.B's $\Upsilon^0(g,g_0) = g\,g_0^{-1}\delta_gG_gg_0$ (section 6, the source's
(4.3)-(4.4)) and (6.3), $D_1\Upsilon^0(g,g)k = D(\delta_gG_g)(k)\,g = -\delta_gG_gk$, as $\delta_gG_gg = 0$ for every
$g$, and the $E^\Upsilon$-term contributes $-E^\Upsilon_gG_gk$ (III.B (6.6) at $g_0 = g$ says the same). (iii) If
$\mathrm{Ric}(g) = 0$, then $D_g\mathrm{Ric}(\mathcal L_Yg) = \mathcal L_Y\mathrm{Ric}(g) = 0$ for every smooth vector
field $Y$ (differentiate $\mathrm{Ric}(\psi_\epsilon^*g) = \psi_\epsilon^*\mathrm{Ric}(g)$ along the flow of $Y$); in
particular $D_g\mathrm{Ric}\circ\delta^*_g = 0$.

*The boost states.* By III.D$''$ Proposition 3.1 at $b_0$, with $\omega_{\mathrm s1}(S) := \omega^{(0)}_{b_0,\mathrm
s1}(S)$ and $\breve\omega(S) := \breve\omega^{(0),1}_{b_0,\mathrm s1}(S)$, stationary and linear in $S$:
$$\omega_{\mathrm s1}(S)-\bar\omega_{\mathrm s1}(S)\in\mathcal A^{(2,0)\cup(2+\mathcal
E_{\mathrm{ind}})},\qquad\breve\omega(S)-\breve{\bar\omega}_{\mathrm s1}(S)\in\mathcal A^{(1,0)\cup(1+\mathcal
E_{\mathrm{ind}})},$$
$\bar\omega_{\mathrm s1}(S) = d(|x|S)$, $\breve{\bar\omega}_{\mathrm s1}(S) = |x|\,d(|x|S)-|x|S\,d\bar t$, $\bar t =
t_*+|x|$ (III.D$''$ (1.2)); $h(S) := \delta^*_{g_{b_0}}\omega_{\mathrm s1}(S)\in\mathcal A^{(3,0)\cup(3+\mathcal
E_{\mathrm{ind}})}$, and $h^{\le1}(S) = t_*h(S)+\breve h(S) = \delta^*_{g_{b_0}}(t_*\omega_{\mathrm
s1}(S)+\breve\omega(S))$, $\breve h(S)\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}$, is III.H section 1's
generalised state; $h(S)$ and $h^{\le1}(S)$ lie in the kernels of $D_{g_{b_0}}\mathrm{Ric}$ and of
$\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}$. Near infinity $\bar t = t+C'-8\mu_0|x|^{-1}$ (III.D$''$ section 1, from III.B
(3.6)) and $g_{b_0}-\eta\in|x|^{-2}C^\infty$ (III.B (3.5), Proposition 3.6); $C'$ is that constant. III.D$''$
Proposition 3.1 assumes (Dyn) (III.D), as every part from III.D$''$ on does.

**Definition 1.1 (the re-centred state).** $\omega^{\le1}_\natural(S) := (t_*-C')\omega_{\mathrm s1}(S)+\breve\omega(S)$
and $h^{\le1}_\natural(S) := \delta^*_{g_{b_0}}\omega^{\le1}_\natural(S) = h^{\le1}(S)-C'h(S)$, in the same two kernels.

**Lemma 1.2 (the time origin).** (a) Near infinity, $(t_*-C')\bar\omega_{\mathrm s1}(S)+\breve{\bar\omega}_{\mathrm
s1}(S)-\bar\omega(S) = -8\mu_0|x|^{-1}\big(d(|x|S)+S\,d|x|\big)\in|x|^{-1}C^\infty(\bar X;T^*)$.

(b) Let $\ell_I\in\mathbb R$, $\beta_+<2$ and $\alpha_K<2$. If $u = \chi^H_Kh^{\le1}(\dot S)+\tilde u$ with $\tilde u\in
H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta_+,\alpha_K-2}_{\mathrm b}(\Omega_*)^{\bullet,-}$, then $u =
\chi_Kh^{\le1}_\natural(\dot S)+\tilde u'$ with $\tilde u'$ in the same space, linear and continuous in $(\dot S,\tilde
u)$.

*Proof.* (a) $(t_*-C')d(|x|S)+|x|\,d(|x|S)-|x|S\,d\bar t-t\,d(|x|S)+|x|S\,dt = (\bar t-C'-t)\,d(|x|S)-|x|S\,d(\bar
t-t)$, and $\bar t-C'-t = -8\mu_0|x|^{-1}$, $d(\bar t-t) = 8\mu_0|x|^{-2}d|x|$. Both $|x|^{-1}d(|x|S) = |x|^{-1}w\cdot
dx$ and $S\,d|x|$ have Cartesian components in $|x|^{-1}C^\infty$, resp. $C^\infty$, homogeneous of degree $-1$, resp. 0.

(b) $\tilde u' := u-\chi_Kh^{\le1}_\natural(\dot S)$ vanishes near $\{t^\flat_* = 1\}$, as $u$ does and $\chi_K = 0$ for
$t^\flat_*<10$, and $\tilde u'-\tilde u = (\chi^H_K-\chi_K)h^{\le1}(\dot S)+C'\chi_Kh(\dot S)$. Both cut-offs are smooth
on $M$, equal to 1 near $K^+$ ($\chi^H_K = 1$ on $\{|x|\le t_*/4,\ t_*\ge2\}$) and to 0 near $\mathscr I^+$; so
$\chi^H_K-\chi_K$ is supported in a set whose closure meets $\partial M$ in a compact subset of $(\iota^+)^\circ$.
There, $|x|\sim t_*$ and functions in $\mathcal A^{\mathcal E}(\bar X)$ are in $\mathcal A^{\mathcal E}$ at $\iota^+$
($\langle x\rangle^{-1}$ being $\rho_+$ times a positive smooth function), so $h^{\le1}(\dot S) = t_*h(\dot S)+\breve
h(\dot S)\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}$, which lies in $H^{\infty,2-\epsilon}_{\mathrm b}$ at
$\iota^+$, with no condition at $\mathscr I^+$ or $K^+$; the compact part is smooth. And $\chi_Kh(\dot S)$ vanishes near
$\mathscr I^+$, is bounded and stationary near $K^+$ ($K^+$-weight $-\epsilon$ for every $\epsilon>0$, above
$\alpha_K-2<0$), and is $O(\langle x\rangle^{-3})$ with b-derivatives near $\iota^+$ ($\iota^+$-weight $3-\epsilon$). As
$\beta_+<2$, both terms lie in the space of $\tilde u$. $\square$

## 2. The correction terms and the augmented operator ([Hin26] (11.76)-(11.85))

**Definition 2.1 ([Hin26] Definition 11.23 at n = 4).** For $S\in\mathcal S_1$,
$$h^{(-1)}(S) := -[\delta^*_{g_{b_0}},\chi_K]\big(\omega^{\le1}_\natural(S)-\Theta w(S)\big) =
-d\chi_K\otimes_s\big(\omega^{\le1}_\natural(S)-\Theta w(S)\big),$$
$$\vartheta^{(-1)}(S) := [\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}},\chi_K]h^{\le1}_\natural(S) =
-\iota_{g_{b_0}^{-1}d\chi_K}G_{g_{b_0}}h^{\le1}_\natural(S),$$
$$\vartheta_\sharp(S) := \vartheta^{(-1)}(S)+D_1\Upsilon^{E_\Upsilon}(g_{b_0},g_{b_0})h^{(-1)}(S) =
\vartheta^{(-1)}(S)-\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}h^{(-1)}(S).$$
All three are linear in $S$. The source's $h^{(-1)}$ has $\bar\omega^{(0),\le1}_{\mathrm s1}$ and no factor $\Theta$;
here $w(S)$ is the 1-form of III.B's boost family, so that (2.3) below is exact, and $\Theta = 1$ where it matters
(Lemma 2.2). $\vartheta_\sharp$ carries the counterterm of the source's Remark 11.27.

**Lemma 2.2 ([Hin26] Lemma 11.24 at n = 4).** $h^{(-1)}(S)$, $\vartheta^{(-1)}(S)$ and $\vartheta_\sharp(S)$ are
supported in $\mathcal C$, smooth, and, with $\mathcal G := (2,0)\cup(2+\mathcal E_{\mathrm{ind}})$, near
$(\iota^+)^\circ$
$$h^{(-1)}(S)\in\mathcal A^{\mathcal G},\qquad D_{g_0}\mathrm{Ric}\big(h^{(-1)}(S)\big)\in\mathcal A^{\mathcal
G+2},\qquad\vartheta^{(-1)}(S),\ \vartheta_\sharp(S)\in\mathcal A^{\mathcal G+1},\tag{2.1}$$
for every metric $g_0$ smooth on $M$ near $(\iota^+)^\circ$ with $g_0-\eta\in\rho_+C^\infty$ there; the seminorms are
$O(|S|)$.

*Proof.* Each is a differential expression with a factor $d\chi_K$, so it is supported in $\mathcal C$; it is smooth, as
$\omega^{\le1}_\natural$, $w$, $\Theta$ and $h^{\le1}_\natural$ are. Near $(\iota^+)^\circ$, on $\mathcal C\cap\{t\ge
T_1\}$, $\Theta = 1$ and $|x|\ge t/10$, and
$$\omega^{\le1}_\natural-w = (t_*-C')(\omega_{\mathrm s1}-\bar\omega_{\mathrm
s1})+(\breve\omega-\breve{\bar\omega}_{\mathrm s1})+\big((t_*-C')\bar\omega_{\mathrm s1}+\breve{\bar\omega}_{\mathrm
s1}-\bar\omega\big)+(\eta-g_{b_0})\eta^{-1}\bar\omega$$
(omitting $S$). With $t_*\in\rho_+^{-1}C^\infty$ there, the four terms lie in $\mathcal A^{(1,0)\cup(1+\mathcal
E_{\mathrm{ind}})}$, $\mathcal A^{(1,0)\cup(1+\mathcal E_{\mathrm{ind}})}$, $\rho_+C^\infty$ (Lemma 1.2 (a)) and
$\rho_+^2C^\infty\cdot\rho_+^{-1}C^\infty = \rho_+C^\infty$ (the components of $\bar\omega$ are $tw$ and $-w\cdot x$).
So $\omega^{\le1}_\natural-w\in\mathcal A^{(1,0)\cup(1+\mathcal E_{\mathrm{ind}})}$, with no logarithm, and
$d\chi_K\in\rho_+C^\infty$ gives $h^{(-1)}\in\mathcal A^{\mathcal G}$. $D_{g_0}\mathrm{Ric}$ is a second-order operator
whose coefficients are smooth functions of $g_0^{-1}$, $g_0$ and its first two Cartesian derivatives, and Cartesian
derivatives lie in $\rho_+\mathcal V_{\mathrm b}$, so $D_{g_0}\mathrm{Ric}\in\rho_+^2\mathrm{Diff}^2_{\mathrm b}$ with
smooth coefficients near $(\iota^+)^\circ$, and it maps $\mathcal A^{\mathcal G}$ into $\mathcal A^{\mathcal G+2}$.
$h^{\le1}_\natural = (t_*-C')h+\breve h\in\mathcal A^{\mathcal G}$ near $(\iota^+)^\circ$, and
$\iota_{g_{b_0}^{-1}d\chi_K}$ has coefficients in $\rho_+C^\infty$, so $\vartheta^{(-1)}\in\mathcal A^{\mathcal G+1}$.
$\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}\in\rho_+\mathrm{Diff}^1_{\mathrm b}$ there ($\delta$ by the Cartesian count;
$E^\Upsilon_{g_{b_0}}$ has coefficients $c_\Upsilon\in|x|^{-1}C^\infty$ and $c_{\Upsilon,H}$, which vanishes for
$|x|\ge5R_1$, III.B (6.1)), so $\vartheta_\sharp\in\mathcal A^{\mathcal G+1}$. $\square$

The source's (11.79)-(11.81) have $(1,1)\cup(1+\mathcal E_{\mathrm{ind}})$, $(3,0)\cup(3+\mathcal E_{\mathrm{ind}})$ and
$(2,0)\cup(2+\mathcal E_{\mathrm{ind}})$; its middle membership needs the vanishing of a $(3,1)$-coefficient ((11.82)).
At $n = 4$ there is no logarithm ((I$''''$2)).

**Definition 2.3 ([Hin26] Definition 11.25 at n = 4, in the form of its Remark 11.27).** For small $S\in\mathcal S_1$,
$b$ near $b_0$ and $h\in\mathcal X^\infty$ (III.I (1.4)) with small $\mathcal X^d$-norm, with $g_0 := g_{b_0,b,-S}$ and
$g' := g_0+h^{(-1)}(S)+h$, put
$$P_1(h,S,b) := \mathrm{Ric}(g')-\delta^*_{g_0,E_C}\Big(\Upsilon^{E_\Upsilon}(g',g_0)-\vartheta_\sharp(S)\Big),\qquad
L_{h,S} := D_hP_1(\cdot,S,b_0)\ \text{at }h.\tag{2.2}$$
$P_1(0,0,b_0) = P(g_{b_0},g_{b_0}) = 0$. The source's (11.83) has $\Upsilon^{E_\Upsilon}(g_0+h,g_0)$ and
$\vartheta^{(-1)}$; its Remark 11.27 notes that the present form makes the linearisation in $h$ exactly a gauge-fixed
linearised Einstein operator ((I$''''$4)).

**Lemma 2.4 (the boost identity; [Hin26] (11.76)-(11.78b) at n = 4).** For $\dot S\in\mathcal S_1$,
$$D_SP_1(0,S,b_0)\big|_{S=0}(\dot S) = L_{b_0}\big(\chi_Kh^{\le1}_\natural(\dot S)\big) =
-D_{g_{b_0}}\mathrm{Ric}\big([\delta^*_{g_{b_0}},\chi_K]\omega^{\le1}_\natural(\dot
S)\big)+\delta^*_{g_{b_0},E_C}\vartheta^{(-1)}(\dot S).\tag{2.3}$$

*Proof.* *The background.* $s\mapsto\phi_{-s\dot S} = \exp(-sV(\dot S))$ is the flow of $-V(\dot S)$, so
$\partial_S\phi^*_{-S}g_{b_0}|_{S=0}(\dot S) = -\mathcal L_{V(\dot S)}g_{b_0} = -\delta^*_{g_{b_0}}(\Theta w(\dot S))$,
and with (1.2)
$$\dot g := \partial_Sg_S|_{S=0}(\dot S) = -(1-\chi_K)\delta^*_{g_{b_0}}(\Theta w) =
-\delta^*_{g_{b_0}}\big((1-\chi_K)\Theta w\big)-[\delta^*_{g_{b_0}},\chi_K](\Theta w).$$
*The curvature term.* At $S = 0$, $g' = g_{b_0}$ ($h = 0$, $h^{(-1)}(0) = 0$). By (iii), $D_{g_{b_0}}\mathrm{Ric}(\dot
g) = -D_{g_{b_0}}\mathrm{Ric}([\delta^*,\chi_K](\Theta w))$, and adding $D_{g_{b_0}}\mathrm{Ric}(h^{(-1)}(\dot S)) =
-D_{g_{b_0}}\mathrm{Ric}([\delta^*,\chi_K](\omega^{\le1}_\natural-\Theta w))$ gives $\partial_S\mathrm{Ric}(g') =
-D_{g_{b_0}}\mathrm{Ric}([\delta^*,\chi_K]\omega^{\le1}_\natural(\dot S))$. *The gauge term.* At $S = 0$ the bracket in
(2.2) is $\Upsilon^{E_\Upsilon}(g_{b_0},g_{b_0})-0 = 0$, so only its derivative counts: by (i) and the definition of
$\vartheta_\sharp$,
$$D_1\Upsilon(\dot g+h^{(-1)}(\dot S))+D_2\Upsilon(\dot g)-\vartheta_\sharp(\dot S) = D_1\Upsilon\,h^{(-1)}(\dot
S)-\vartheta^{(-1)}(\dot S)-D_1\Upsilon\,h^{(-1)}(\dot S) = -\vartheta^{(-1)}(\dot S),$$
with $D_j\Upsilon := D_j\Upsilon^{E_\Upsilon}(g_{b_0},g_{b_0})$; so the gauge term contributes
$+\delta^*_{g_{b_0},E_C}\vartheta^{(-1)}(\dot S)$. This is the right side of (2.3). *The left side.* $h^{\le1}_\natural
= \delta^*\omega^{\le1}_\natural$ lies in both kernels, so with (1.2) and (iii),
$$L_{b_0}(\chi_Kh^{\le1}_\natural) =
D\mathrm{Ric}\big(\delta^*(\chi_K\omega^{\le1}_\natural)-[\delta^*,\chi_K]\omega^{\le1}_\natural\big)
+\delta^*_{E_C}\big(\chi_K\delta_{E_\Upsilon}Gh^{\le1}_\natural+[\delta_{E_\Upsilon}G,\chi_K]h^{\le1}_\natural\big),$$
which is $-D\mathrm{Ric}([\delta^*,\chi_K]\omega^{\le1}_\natural)+\delta^*_{E_C}\vartheta^{(-1)}$. $\square$

As in the source, (2.3) says that the source term $D_SP_1(0,0,b_0)(\dot S)$, supported in $\mathcal C$, generates the
forward solution $\chi_Kh^{\le1}_\natural(\dot S)$: the final black hole boosted along $-\dot S$, without an initial
boost.

**Lemma 2.5 (the linearisation in $h$; [Hin26] (11.84)-(11.85) at n = 4).** Assume
$$2+\mathcal E_{\mathrm{ind}}\subset\mathcal E_+.\tag{2.4}$$
($\mathcal E_{\mathrm{ind}}$ is the index set of III.D$''$ Proposition 3.1 at $b_0$, fixed once, so (2.4) is a condition
on $\mathcal E_+$.) Then $h^{(-1)}(S)\in\mathcal X^\infty$ with $\|h^{(-1)}(S)\|_{\mathcal X^k}\le C_k|S|$, and
$$L_{h,S} = L^{g',g_0},\qquad g' = g_0+h',\quad h' := h^{(-1)}(S)+h,\quad g_0 = g_S.$$
So for $|S|$ and $\|h\|_{\mathcal X^d}$ small, $L_{h,S}$ is the operator of III.I Theorem 5.3 with $(S,h')$ for $(S,h)$,
and III.I Propositions 3.4, 4.1, Corollary 5.2, Theorem 5.3, III.I$'$ Propositions 2.1, 3.1, III.I$''$
Proposition 5.1 and III.I$'''$ Proposition 2.1 hold for it, with their constants for $(S,h')$.

*Proof.* $\vartheta_\sharp(S)$ does not depend on $h$, so $D_hP_1 =
D_{g'}\mathrm{Ric}-\delta^*_{g_0,E_C}D_1\Upsilon^{E_\Upsilon}(g',g_0) = L^{g',g_0}$ (III.B's formula for $L_{g,g_0}$).
By Lemma 2.2, $h^{(-1)}(S)$ vanishes near $\mathscr I^+$ and $K^+$ and for $t^\flat_*<10$, is smooth, and near
$(\iota^+)^\circ$ lies in $\mathcal A^{\mathcal G}$; $\mathcal G\subset\mathcal E_+$ by $(2,0)\in\mathcal E_+$ (III.I
(1.3)) and (2.4), so it lies in $H^{\infty,(\mathcal E_+,a_+)}_{\mathrm b}$ at $\iota^+$ for every $a_+$, with norms
$O(|S|)$. $\square$

The source asks $\mathcal E_+\supset1+\mathcal E_{\mathrm{ind}}$ and $j(\mathcal E_+\cup(1,1))\subset\mathcal
E_+\cup(1,1)$ ((11.85)), the latter for its logarithm; at $n = 4$, (2.4) and III.I (1.3) suffice.

## 3. The linearisation in the boost parameter ([Hin26] Lemma 11.28 at n = 4)

Let $\mathcal K := H^{\infty,(\langle(3,0)\rangle_0,\infty),((2,0),\infty),\infty}_{\mathrm b}(\Omega_*)$, the class of
III.I Lemma 3.6, contained in $\mathcal X^\infty$ (III.I Proposition 3.4's proof). By III.I Lemma 3.6, $k_S :=
g_S-g_{b_0}\in\mathcal K$; its proof rests on III.B Lemma 5.2's (5.3), with $h_{S_w}$ smooth in $w$, and on III.B Lemma
5.1's pullbacks, smooth in $w$, so $S\mapsto k_S\in\mathcal K$ is smooth and $k' := \partial_Sk_S(S')\in\mathcal K$ with
seminorms $O(|S'|)$; $k'$ vanishes on $\mathrm{int}\,\chi_K^{-1}(1)$, a neighbourhood of $K^+$.

**Lemma 3.1 (the derivative of the operator family).** Let $|S|$, $\|h\|_{\mathcal X^5}$ be small, $h\in\mathcal X^k$,
$k\ge5$, $s\in[0,1]$, $S'\in\mathcal S_1$, and $\dot L := \partial_S\big[L^{g_S+sh,g_S}\big](S')$, the derivative of the
coefficients. Then $\dot L$ vanishes near $K^+$, satisfies III.I (3.6), and for $\frac32<\ell_I<a_I+\frac12$,
$0<\ell_+\le\max(a_+,\min\mathrm{Re}\,\mathcal E_+)$, $\ell_+<a_++\min\mathrm{Re}\,\mathcal E_+$ and every $\epsilon>0$,
$$\dot L:H^{k,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_+,\ell_+),\ell_K}_{\mathrm b}\to H^{k-2,(\langle\mathcal
E^C_I+1\rangle',\ell_I+1),(2\mathcal E_++2,\ell_++2+m_+-\epsilon),\infty}_{\mathrm b},\tag{3.1}$$
with norm $O(|S'|)$, uniformly in $s$; $m_+ = \min(a_+,\min\mathrm{Re}\,\mathcal E_+)$.

*Proof.* $g_S+sh-g_{b_0} = k_S+sh$ and $g_S-g_{b_0} = k_S$, both in $\mathcal X^k$. In III.I Proposition 3.4's proof,
$L^{g,g_0}-L_{b_0}$ is a sum of terms in which smooth functions of $g^{-1}$, $g_0^{-1}$ and of the background multiply
Cartesian derivatives, of total order two with the operator's own, of the differences $g-g_{b_0}$, $g_0-g_{b_0}$ (III.B
(6.6)-(6.8)), at least one factor in each term being a difference, and III.C Lemma 4.3 counts them. $\dot L$ is the sum
of the same terms with one factor replaced by $k'$ or one of its derivatives (or $g^{-1}$ by $-g^{-1}k'g^{-1}$);
$k'\in\mathcal K\subset\mathcal X^\infty$ is counted as a difference. So $\dot L$ is of the class (3.6). In III.I
Proposition 4.1's proof of (4.1) near $\mathscr I^+$, $L^{g,g_0}$ is the leading part
$\rho_+^2\rho_I(X_+-X_I)(X_I-\frac32-\bar A)$, which does not depend on $(g,g_0)$, plus the $C^\infty$ error of
$L_{b_0}$, plus the perturbation error, in which the background difference $k_S\in\mathcal K\subset\mathcal X^\infty$ is
counted with $h$, as in III.I Proposition 3.4's proof; the first two do not depend on $S$, and $\dot L$ is the
$S$-derivative of the perturbation error, which is of the same kind, and the counts given there for the perturbation
error ($2\mathcal E^{\mathrm{tot}}_I\subset\mathcal E^C_I+1$ at weight $\ell_I+1$, $2\mathcal E_++2$ at weight
$\ell_++2$, by III.C Lemma 2.1) apply to it. Away from $\mathscr I^+$, (4.2)'s count, from (3.6) and III.C Lemma 2.1,
gives the $\iota^+$-data, and $\dot L = 0$ near $K^+$, as $g_S = g_{b_0}$ there. Linearity in $k'$ gives the $O(|S'|)$
bound. $\square$

**Lemma 3.2 ([Hin26] Lemma 11.28 at n = 4).** Assume (2.4). Let $|S|$, $\|h\|_{\mathcal X^5}$ be small, $h\in\mathcal
X^k$, $k\ge5$, and $f_{h,S}(S') := D_SP_1(h,S,b_0)(S')$, $S'\in\mathcal S_1$. Put
$$\tilde{\mathcal E}_+ := \mathcal G\cup(\mathcal E_++\mathcal G),\qquad\mathcal G = (2,0)\cup(2+\mathcal
E_{\mathrm{ind}}).\tag{3.2}$$
Then $f_{h,S}(S')$ is linear in $S'$, vanishes on $\mathrm{int}\,\chi_K^{-1}(1)$ (a neighbourhood of $K^+$); if $h$
vanishes for $t^\flat_*<c$, $c\le10$, so does $f_{h,S}(S')$; and for every $\epsilon>0$
$$f_{h,S}(S')\in H^{k-2,(\langle\mathcal E^C_I+1\rangle',a_I+1),((\tilde{\mathcal E}_+\cup2\mathcal E_+)+2,\
a_++2+\min(2,m_+)-\epsilon),\infty}_{\mathrm b}(\Omega_*),\tag{3.3}$$
with norm $O(|S'|)$, continuous in $(h,S)$ with $h\in\mathcal X^k$. In particular its $\iota^+$-weight is $4-\epsilon$
at worst, and $f_{0,0}(S') = L_{b_0}(\chi_Kh^{\le1}_\natural(S'))$ is supported in $\mathcal C$.

*Proof.* Write $g_0 = g_S$, $g' = g_0+h^{(-1)}(S)+h$, $k_0 := \partial_Sg_S(S') = k'$, $h^{(-1)\prime} := h^{(-1)}(S')$,
$\vartheta' := \vartheta_\sharp(S')$. Differentiating (2.2),
$$f = D_{g'}\mathrm{Ric}\big(k_0+h^{(-1)\prime}\big)
-\big(\partial_S\delta^*_{g_0,E_C}\big)\big(\Upsilon(g',g_0)-\vartheta_\sharp(S)\big)
-\delta^*_{g_0,E_C}\Big(D_1\Upsilon(g',g_0)\big(k_0+h^{(-1)\prime}\big)
+D_2\Upsilon(g',g_0)k_0-\vartheta'\Big),\tag{3.4}$$
$\Upsilon := \Upsilon^{E_\Upsilon}$. Cover $\Omega_*$ by the open sets $U_K := \mathrm{int}\,\chi_K^{-1}(1)$, $U_I :=
\mathrm{int}\,\chi_K^{-1}(0)$, a neighbourhood $U_\iota$ of $\mathcal C\cap\{t\ge T_1\}$ near $(\iota^+)^\circ$ on which
$|x|\ge t/20$ and $\Theta = 1$, and a set with compact closure in $M^\circ$; multiplication by a subordinate partition
of unity of functions smooth on $M$ preserves the spaces.

*On $U_K$:* $g_0 = g_{b_0}$, $h^{(-1)}(S) = 0$ and $\vartheta_\sharp(S) = 0$ near each point, so $P_1(h,S,b_0)$ does not
depend on $S$, and $f = 0$.

*On $U_I$:* $g_0 = \phi^*_{-S}g_{b_0}$ is Ricci flat and $h^{(-1)}$, $\vartheta_\sharp$ vanish, so $P_1(h,S,b_0) =
P(g_0+h,g_0) = P(g_0+h,g_0)-P(g_0,g_0) = \int_0^1L^{g_0+sh,g_0}h\,ds$ by (i), and
$$f = \int_0^1\dot L_sh\,ds,\qquad\dot L_s := \partial_S\big[L^{g_S+sh,g_S}\big](S'),$$
which vanishes where $h$ vanishes on a neighbourhood. Lemma 3.1 with $u = h$, $(\ell_I,\ell_+,\ell_K) = (a_I,a_+,a_K)$
(the hypotheses hold: $\frac32<a_I<a_I+\frac12$, $0<a_+\le\max(a_+,\cdot)$, $a_+<a_++\min\mathrm{Re}\,\mathcal E_+$)
gives the $\mathscr I^+$-data $(\langle\mathcal E^C_I+1\rangle',a_I+1)$ and the $\iota^+$-data $(2\mathcal
E_++2,a_++2+m_+-\epsilon)$, uniformly in $s$.

*On $U_\iota$,* every term of (3.4) is counted near $(\iota^+)^\circ$, where Cartesian derivatives lie in
$\rho_+\mathcal V_{\mathrm b}$. The inputs: $\phi_{-S}$ is the exact boost on $\mathrm{supp}(1-\chi_K)$ near
$(\iota^+)^\circ$ (III.I Lemma 3.6's proof), so $g_0-\eta\in\rho_+^2C^\infty$ and $k_0\in\rho_+^2C^\infty$
($g_{b_0}-\eta\in|x|^{-2}C^\infty$ and $|x|\ge t/20$); $h^{(-1)}(S),h^{(-1)\prime}\in\mathcal A^{\mathcal G}$ and
$\vartheta_\sharp(S),\vartheta'\in\mathcal A^{\mathcal G+1}$ (Lemma 2.2); $h\in H^{k,(\mathcal E_+,a_+)}_{\mathrm b}$;
so $g'-\eta\in H^{k,(\mathcal E_+,a_+)}_{\mathrm b}$ ($\rho_+^2C^\infty\subset\mathcal A^{(2,0)}$, (2.4)), and products
stay in this class ($2\mathcal E_+\subset\mathcal E_+$). Three counts, with $\mathcal A^{\mathcal G}\subset\mathcal A^2$
(no logarithm at order 2) so that multiplication by it raises $H_{\mathrm b}$-weights by 2:

(1) $D_{g'}\mathrm{Ric}\in\rho_+^2(C^\infty+H^{k-2,(\mathcal E_+,a_+)}_{\mathrm b})\mathrm{Diff}^2_{\mathrm b}$, applied
to $k_0+h^{(-1)\prime}\in\mathcal A^{\mathcal G}$: index set $(\mathcal G+2)\cup(\mathcal E_++\mathcal G+2)$, weight
$a_++4$.

(2) $\partial_S\delta^*_{g_0,E_C}$ is of order zero with coefficients in $\rho_+^3C^\infty$: $\partial_S\Gamma(g_0)$
involves $g_0^{-1}\partial k_0$ and $k_0\,\partial g_0$, and $\partial_SE^C_{g_0}$ involves $k_0$ and
$c_C\in|x|^{-1}C^\infty$ (III.B (6.2)). $\Upsilon(g',g_0)$ is a smooth function of $g',g_0$ times
$\Gamma(g')-\Gamma(g_0)$, plus $-E^\Upsilon_{g_0}G_{g_0}(g'-g_0)$, so with $g'-g_0 = h^{(-1)}(S)+h$ it lies in
$H^{k-1,(\mathcal E_++1,a_++1)}_{\mathrm b}$, as does $\vartheta_\sharp(S)$ ($\mathcal G+1\subset\mathcal E_++1$).
Product: $(\mathcal E_++4,a_++4)$.

(3) By (i), $D_1\Upsilon(g',g_0)k_0+D_2\Upsilon(g',g_0)k_0 = [(D_1+D_2)\Upsilon(g',g_0)-(D_1+D_2)\Upsilon(g_0,g_0)]k_0$,
a smooth function of $(g',\partial g')$ vanishing at $g' = g_0$, hence (Taylor's formula in $g'$) linear in
$(g'-g_0,\partial(g'-g_0))$ with smooth coefficients, applied to $(k_0,\partial k_0)$, of total derivative order one
($c_\Upsilon$ counting as one): $(\mathcal E_++3,a_++3)$. By the definition of $\vartheta_\sharp$,
$D_1\Upsilon(g',g_0)h^{(-1)\prime}-\vartheta' =
[D_1\Upsilon(g',g_0)-D_1\Upsilon(g_{b_0},g_{b_0})]h^{(-1)\prime}-\vartheta^{(-1)}(S')$, linear in
$(g'-g_{b_0},g_0-g_{b_0})$ and their first derivatives (both in $H^{k,(\mathcal E_+,a_+)}_{\mathrm b}$) times
$\rho_+\mathcal A^{\mathcal G}$, plus $\mathcal A^{\mathcal G+1}$: index set $(\mathcal E_++\mathcal G+1)\cup(\mathcal
G+1)$, weight $a_++3$. $\delta^*_{g_0,E_C}\in\rho_+\mathrm{Diff}^1_{\mathrm b}$ adds 1.

So on $U_\iota$, $f$ has $\iota^+$-index set $(\mathcal G+2)\cup(\mathcal E_++\mathcal G+2)\cup(\mathcal E_++4) =
\tilde{\mathcal E}_++2$ ($\mathcal E_++4\subset\mathcal E_++\mathcal G+2$ as $(2,0)\in\mathcal G$) at weight $a_++4$,
and no $\mathscr I^+$ or $K^+$ condition. On the compact part $f$ is in $H^{k-2}$. Together, (3.3), with
$\min\mathrm{Re}(2\mathcal E_++2)>4$, $\min\mathrm{Re}(\tilde{\mathcal E}_++2) = 4$ and $a_++2+\min(2,m_+)>4$. Each term
of (3.4) and of $\int_0^1\dot L_sh\,ds$ is linear in $S'$ and a product of factors continuous in $(h,S)$, with the
bounds of III.C Lemma 2.1, so $f$ is continuous in $(h,S)$. If $h = 0$ for $t^\flat_*<c$, $c\le10$, then
$\{t^\flat_*<c\}\subset U_I$ ($\mathrm{supp}\,\chi_K\subset\{t^\flat_*\ge10\}$) and $f = \int_0^1\dot L_sh\,ds = 0$
there. $f_{0,0}$ is (2.3). $\square$

The source's (11.86)-(11.87) split $f$ into $f^1$, with $\iota^+$-index set $\mathcal E_++3$, and a term with
$\tilde{\mathcal E}_++2\ni(3,0)$ supported where $(1-\chi^\flat_K)\chi^\sharp_K\ne0$, to keep $(3,0)$-terms away from
$\mathscr I^+$ (its Remark 11.29). At $n = 4$ the least exponent is 4 and the weight needed below is $\alpha_++2<4$, so
no splitting is made ((I$''''$3)). The finer index sets of (3.3) are recorded for the later steps.

## 4. Elimination of boosts ([Hin26] Proposition 11.30 and (11.95) at n = 4)

Fix $\ell_I$ with III.I$''$ (5.1) ($2\le\ell_I<\min(a_I+\frac12,\ell_I^{\max})$, $\ell_I\notin\mathrm{Re}\,\pi_1\mathcal
E^C_I\cup(\frac32+\sigma_\Upsilon)$) and $\ell_I\le a_I$, which needs $a_I\ge2$ ((I$''''$5)); and
$\alpha_K\in(1,\min(a_K-1,\frac32))$, $\alpha_+\in(\alpha_K,2)$.

**Proposition 4.1 ([Hin26] Proposition 11.30 at n = 4, at $b_0$).** Assume (2.4). There are $d\in\mathbb N$ and
$\epsilon_1>0$ such that for $|S|<\epsilon_1$ and $h\in\mathcal X^\infty$ vanishing near $\{t^\flat_* = 1\}$ (the
source's (11.91)) with $\|h\|_{\mathcal X^d}<\epsilon_1$:

(1) (*Asymptotics.*) For $f\in H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),\alpha_++2,\alpha_K}_{\mathrm
b}(\Omega_*;S^2T^*)^{\bullet,-}$, the forward solution of $L_{h,S}u = f$ is
$$u = \chi_Kh^{\le1}_\natural(\dot S(f))+\tilde u,\qquad\dot S(f)\in\mathcal S_1,\quad\tilde u\in
H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta_+,\alpha_K-2}_{\mathrm b}(\Omega_*)^{\bullet,-}\ \text{for every
}\beta_+<\min(\alpha_+,\tfrac32,\min\mathrm{Re}\,\mathcal E_+),\tag{4.1}$$
with $\dot S(f)$ and $\tilde u$ depending linearly and continuously on $f$.

(2) (*The boost parameter.*) $S^{(-1)}_{h,S}\in\mathcal L(\mathcal S_1)$, $S'\mapsto\dot S(f_{h,S}(S'))$, with $f_{h,S}$
of Lemma 3.2 (which lies in the space of (1) by (3.3), as $\ell_I\le a_I$ and $\alpha_+<2$), is invertible.

The source's (11.92) admits $f = f^1+(1-\chi^\flat_K)f^2$ with $f^2$ of $\iota^+$-index set $(3,0)$, and its Remark
11.31 a further $f^2$ with $K^+$-weight $1+\epsilon_K$; at $n = 4$ both kinds of term have $\iota^+$-order 4 and lie in
the space of (1). Its (11.93) has the $\iota^+$-weight $1-\epsilon$ and $\alpha_K\in(1,1+\epsilon_K)$.

*Proof of (1).* Lemma 2.5 and III.I$'''$ Proposition 2.1 (its hypotheses: $\ell_I$ with III.I$''$ (5.1),
$\alpha_K\in(1,\min(a_K-1,\frac32))$, $\alpha_+>\alpha_K$) give $u = \chi^H_Kh^{\le1}(\dot S)+\tilde u$ with $\tilde u$
in the space of (4.1), continuously in $f$, for $\|h'\|_{\mathcal X^d}$ and $|S|$ small; Lemma 1.2 (b)
($\beta_+<\frac32<2$, $\alpha_K<2$) gives (4.1). $\dot S(f)$ is determined by $u$: $\tilde u$ has $K^+$-weight
$\alpha_K-2>-1$, so $h(\dot S)$ is the coefficient of $t_*$ in $u$ at $K^+$, and $S\mapsto h(S)$ is injective
(III.F$'''$ Proposition 4.1 (1)). $\square$

**Lemma 4.2 (the boost parameter depends continuously on the operator).** Write $\dot S_{h,S}(f)$ for the $\dot S(f)$ of
(4.1). There are $k_0\in\mathbb N$ and $C$ such that, for $(h,S)$ as in Proposition 4.1,

(a) $|\dot S_{h,S}(f)|\le C\|f\|_{H^{k_0,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),\alpha_++2,\alpha_K}_{\mathrm b}}$;

(b) if $\ell_I>2$, or if $f$ vanishes near $\mathscr I^+$, then for fixed $f$ the map $(h,S)\mapsto\dot S_{h,S}(f)$ is
continuous, $h$ in the $\mathcal X^d$-topology with $d\ge k_1+d_T+7$, $d_T$ the $d$ of III.I Theorem 5.3 and $k_1$ below.

*Proof.* In III.I$'''$ Proposition 2.1's proof (with $L := L_{h,S}$), $\dot S = S_0$ is obtained from $f' :=
f-(L-L_{b_0})u$ alone: $u_I$ by III.I$'$ Proposition 3.1's construction for $L_{b_0}$, $f^\flat := f'-L_{b_0}u_I$, and
$S_0$ the $\mathcal S_1$-component of $\tilde L_{b_0}(0)^{-1}(\hat f^\flat(0),0,0)$ (III.I$'''$ (2.4)). So $\dot S = \Pi
f'$ with a linear map $\Pi$ that depends on $L_{b_0}$ only and is bounded on $H^{k_1,(\langle\mathcal
E^C_I+1\rangle',\ell_I+1),\alpha^\sharp_++2,\alpha_K}_{\mathrm b}$ for some $k_1$ (III.I$'$ Proposition 3.1's
construction loses finitely many derivatives; (2.25a) and III.H Proposition 3.2 for $\hat f^\flat(0)$ and $\tilde
L_{b_0}(0)^{-1}$). Moreover $\dot S$ is determined by $u$, so it does not depend on the auxiliary weights
$(\alpha'_K,\beta'_+,\alpha^\sharp_+,\ell_I)$ of that proof, which may be taken with room: $\alpha'_K>\alpha_K-(a_K-2)$
strictly and $\ell_I>2$ strictly, so that lowering the weights of $u$ by a small $\varsigma>0$ keeps $f'$ in a space on
which some such $\Pi$ is bounded. If $\ell_I = 2$ and $f$ vanishes near $\mathscr I^+$, $f$ lies in the space for any
$\ell''_I\in(2,\min(a_I+\frac12,\ell_I^{\max}))$ off III.I$''$ (5.1)'s excluded set, and the argument runs there; $\dot
S$ is the same, being determined by $u$.

(a) $\|f'\|\le\|f\|+\|(L-L_{b_0})u\|\le\|f\|+C\|u\|$, by III.I Proposition 4.1 (4.2) with the coefficient bounds of
III.I Proposition 3.4, uniform for small $(S,h')$, and $\|u\|\le C\|f\|$ in the space (5.2) of III.I$''$ Proposition
5.1, whose constant is locally uniform in $(S,h')$ (its continuity paragraph). With $\|h'\|_{\mathcal
X^d}\le\|h\|_{\mathcal X^d}+C|S|$ (Lemma 2.5) this gives (a), $k_0$ the sum of the losses.

(b) For $(h_1,S_1)$ near $(h,S)$, $L_1 := L_{h_1,S_1}$, $u_1$ its forward solution with source $f$,
$$\dot S_{h_1,S_1}(f)-\dot S_{h,S}(f) = -\Pi\big((L_1-L)u_1+(L-L_{b_0})(u_1-u)\big).$$
The coefficients of $L^{g,g_0}-L_{b_0}$ are polynomial in the differences and their derivatives, with coefficients
smooth in $g^{-1}$, $g_0^{-1}$ (Lemma 3.1's proof), so $L_1-L$ has coefficients in the class (3.6) of norm $o(1)$ as
$(h_1,S_1)\to(h,S)$ ($h'_1\to h'$ in $\mathcal X^d$, Lemma 2.2), and (4.2)'s bound is linear in the coefficient norms
(III.C Lemma 2.1); $u_1$ is bounded in (5.2) by (a)'s argument. So $(L_1-L)u_1\to0$. III.I$''$ Proposition 5.1's
continuity gives $u_1\to u$ in (5.2) with weights lowered by $\varsigma$, at the regularity $k_1+2$ that $\Pi$ needs
once $d\ge k_1+d_T+7$ (III.I Theorem 5.3's continuity, through (3.7)), and (4.2) gives $(L-L_{b_0})(u_1-u)\to0$ in the
space of $f'$ with weights lowered by $\varsigma$, on which $\Pi$ is bounded by the choice of room. $\square$

*Proof of (2).* By Lemma 2.4, $f_{0,0}(S') = L_{b_0}(\chi_Kh^{\le1}_\natural(S'))$, and $\chi_Kh^{\le1}_\natural(S')$
vanishes for $t^\flat_*<10$, so it is the forward solution (II.E Proposition 3.4); it has the form (4.1) with $\tilde u
= 0$, so $S^{(-1)}_{0,0} = \mathrm{id}$. For $S'$ in a basis of $\mathcal S_1$,
$$S^{(-1)}_{h,S}(S')-S' = \dot S_{h,S}\big(f_{h,S}(S')-f_{0,0}(S')\big)+\big(\dot S_{h,S}-\dot
S_{0,0}\big)\big(f_{0,0}(S')\big).$$
The first term tends to 0 as $(h,S)\to0$ by Lemma 4.2 (a) and the continuity in Lemma 3.2 (with $k = d$, $d\ge k_0+2$;
$f_{h,S}\in H^\infty$ for $h\in\mathcal X^\infty$, and its convergence is in $H^{d-2}$); the second by Lemma 4.2 (b),
$f_{0,0}(S')$ vanishing near $\mathscr I^+$ (it is supported in $\mathcal C$). So $S^{(-1)}_{h,S}$ is close to the
identity on $\mathcal S_1\cong\mathbb R^4$ for small $(h,S)$, hence invertible. $\square$

**Corollary 4.3 ([Hin26] (11.95) at n = 4).** For $(h,S)$ and $f$ as in Proposition 4.1 (1), put $S'' :=
(S^{(-1)}_{h,S})^{-1}\dot S(f)$. The forward solution $u$ of
$$D_{(h,S)}P_1(\cdot,\cdot,b_0)(u,S'') = L_{h,S}u+f_{h,S}(S'') = f\tag{4.2}$$
lies in $H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta_+,\alpha_K-2}_{\mathrm b}(\Omega_*)^{\bullet,-}$ for
every $\beta_+<\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal E_+)$; in compact spatial sets it grows at most like
$t_*^{2-\alpha_K} = o(t_*)$ (b-Sobolev embedding at $K^+$).

*Proof.* $f-f_{h,S}(S'')$ lies in the space of (1) (Lemma 3.2), so $u = \chi_Kh^{\le1}_\natural(\dot S)+\tilde u$ with
$\dot S = \dot S(f)-S^{(-1)}_{h,S}(S'') = 0$ by linearity. $\square$

The source then introduces $P'(h,S,b) := P(\chi_-h_{-S}+h,S,b)$ ((11.90)), which carries the initial data, and works
with $h$ vanishing for $t_*<1$ ((11.91)), restoring $\chi_-h_{-S}$ only at its Definition 11.63 and Corollary 11.66. The
same is done here: $P'$ belongs to the part that writes those, and every statement above is for $h$ vanishing near
$\{t^\flat_* = 1\}$.

## 5. Findings, labels and sources

### 5.1 Findings

(I$''''$1) *The time origin.* III.B's boosts (the source's (3.38)) are centred at $t = 0$, and III.D$''$'s model states
at $\bar t = 0$, with $\bar t-t = C'-8\mu_0|x|^{-1}$ near infinity. Built with $h^{\le1}$, the correction $h^{(-1)}$
would contain $-C'd\chi_K\otimes_s\bar\omega_{\mathrm s1}$, of $\iota^+$-order 1, outside $\mathcal X$ as
$\min\mathrm{Re}\,\mathcal E_+>1$. The re-centred state $h^{\le1}_\natural = h^{\le1}-C'h$ removes it (Lemma 1.2 (a)),
and changes the forward solutions' leading term by $C'\chi_Kh(\dot S)$, a term of the remainder's class (Lemma 1.2 (b)).

(I$''''$2) *No logarithms.* $h^{(-1)}\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}$ and
$D\mathrm{Ric}(h^{(-1)})\in\mathcal A^{(4,0)\cup(4+\mathcal E_{\mathrm{ind}})}$ directly (Lemma 2.2), where the source
has $(1,1)\cup(1+\mathcal E_{\mathrm{ind}})$ and must cancel a $(3,1)$-coefficient ((11.82)); its (11.85) is not needed,
and its $\mathcal E_+\supset1+\mathcal E_{\mathrm{ind}}$ becomes (2.4). The cause is III.D$''$ Proposition 3.1's absence
of a logarithm at $n = 4$.

(I$''''$3) *No splitting of the source.* The parameter derivative has $\iota^+$-order 4 at worst (Lemma 3.2), the
source's 3, so its split into $f^1$ and a $(3,0)$-term supported away from $\mathscr I^+$ and $K^+$ ((11.86), Remark
11.29), the special treatment of that term in Proposition 11.30 (1), and Remark 11.31 are not needed: Part III.I$'''$'s
$\iota^+$-weight $\alpha_++2$ needs $\alpha_+<2$ only.

(I$''''$4) *The form of $P_1$.* The source's Remark 11.27 form is used, $h^{(-1)}$ also in $\Upsilon$'s first argument
and the counterterm in $\vartheta_\sharp$, so that $L_{h,S}$ is exactly III.I's $L^{g',g_0}$ with $h' = h^{(-1)}(S)+h$
(Lemma 2.5) and Parts III.I-III.I$'''$ apply as stated. The source's own (11.83) needs the further observation that
$D_{g'}\mathrm{Ric}-D_{g_0+h}\mathrm{Ric}$ is of the error class. Later parts use $P_1$.

(I$''''$5) *The weights.* Proposition 4.1 needs $a_I\ge2$, since III.I$'''$ Proposition 2.1 needs $\ell_I\ge2$ and the
parameter derivative has $\mathscr I^+$-weight $a_I+1$; the source's $a_I = 3+\epsilon_I$ meets it. Its $\iota^+$-weight
is $\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal E_+)-\epsilon$, the source's $1-\epsilon$ (III.I$'''$ (I$'''$2)).

(I$''''$6) *Two steps the source states in a line.* The parameter derivative near $\mathscr I^+$ is $\int_0^1\dot
L_sh\,ds$ with Lemma 3.1 (the source: "and thus so does its linearization in $S$"), and the continuity of $\dot S$ in
$(h,S)$ goes through $\dot S = \Pi(f-(L-L_{b_0})u)$ with $\Pi$ fixed by $L_{b_0}$ (Lemma 4.2), where the source cites
the continuity of its Theorem 11.12 persisting through the subsequent arguments.

### 5.2 Labels

Proved: Lemmas 1.2, 2.2, 2.4, 2.5, 3.1, 3.2, 4.2, Proposition 4.1 and Corollary 4.3, given the parts cited. Comparisons
with the source are commentary. READ: the source's statements quoted from pp. 241-247. Inputs: II.E Proposition 3.4;
III.B (3.5)-(3.6), Proposition 3.6, section 5 (Lemmas 5.1-5.2, (5.3)), Definition 6.1, (6.1)-(6.3), (6.6), (6.8); III.D
(Dyn); III.C Lemmas 2.1, 4.3; III.D$''$ section 1, (1.2), Proposition 3.1; III.F$'''$ Proposition 4.1; III.H section 1,
(1.2), Proposition 3.2; III.I (1.1)-(1.4), Lemmas 3.6, 4.3, Propositions 3.4, 4.1, Corollary 5.2, Theorem 5.3;
III.I$'$ Propositions 2.1, 3.1; III.I$''$ (5.1), Proposition 5.1; III.I$'''$ Proposition 2.1 and its proof.

### 5.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 11.4.2 (pp. 241-247:
(11.76)-(11.95), Definitions 11.23, 11.25, Lemmas 11.24, 11.28, Remarks 11.22, 11.26, 11.27, 11.29, 11.31, Proposition
11.30). N1STAR-PROOF.md 10.45 (b) and 10.61 (b) (the deductions this part replaces).
