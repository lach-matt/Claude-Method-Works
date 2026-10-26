# Part III.I$'''''''''''$. The spectral phase and the elimination, n = 4 ([Hin26] Theorem 11.59, second half)

*Status.* Written (D273); amended before its verification (D274: Lemma 1.1, the column terms are polyhomogeneous at tf;
$\eta_1,\eta_2<\epsilon_+$; Lemmas 2.1-2.2 carried to the full remainder order); verified (D275: verifier 117's findings
seated); proved (D277: verifier 118 read the repairs and found them correct; its nits seated; D280: verifier 119's nit
seated). This part completes, at spatial dimension $n = 4$, Parts 1-3 of the proof of [Hin26] Theorem 11.59 (pp.
278-289), begun in III.I$''''''''''$: the forward solution of the linearised gauge-fixed Einstein equation with the
correction terms of III.I$'''''''''$, for a source of $K^+$-order $\alpha\le4+\epsilon_K$, has a $K^+$-expansion below
the order $\alpha-2$ consisting of rows (Lemma 3.2), and a unique choice of the modification parameters removes it
(Theorem 4.1, the source's (11.222)). III.I$''''''''''$ Proposition 3.1 reduced the expansion to a forward problem
$L_{b_0}v = f^\flat$ whose source is partially polyhomogeneous at $\iota^+$ from the order 4 on; here $v$ is expanded on
the spectral side (Proposition 3.1).

*What n = 4 changes.* (1) *The cascade.* The source reaches the order $\alpha_K = 4+\epsilon_K$ through zero-energy
solves (its Steps 2.A.3, 2.A.5, 2.A.7) and tf-model inversions between them, its Part 3 (5) calling the rest analogous.
The zf-Taylor expansion of $\hat f^\flat$ has four terms (orders $\sigma^0,\dots,\sigma^3$, as $\alpha-1>3$), and the
four zero-energy solves (levels 0-3) are written out here, with III.G$''''$ Proposition 4.4 at levels 1 and 2 for the
polyhomogeneous tf-terms and Proposition 5.1 at level 3 for the conormal ones. (2) *No assembly of the augmented
components.* The solution is written directly as a sum of physical pieces (Lemma 2.5): $\widehat{L_{b_0}}(\sigma)$ is
injective on $\mathcal X'_\sigma$ (III.I$''''''$ Lemma 1.2), so the rows of $\tilde L_{b_0}(\sigma)$ and the column
moves of III.I$''''''$ Lemma 1.4 are needed only at zero energy and at the last level. (3) *Rows from the spectral
side.* The $K^+$-terms below $\alpha-2$ come only from III.G$''''$ Proposition 4.4's pieces at levels 1 and 2, which are
homogeneous functions of $\sigma$ times the spectral towers (Lemma 2.3); III.I$''''''''''$ Lemma 2.4 (forward tails)
turns them into the rows $\mathcal N_\sigma$, including the boost rows at $\lambda = 3$ that the zero-energy mass state
produces. (4) *The elimination is a perturbation of the identity* (III.I$'''''''''$ Lemma 2.6 (c), III.I$''''''''''$
Corollary 2.3), not the source's "$\pm$ identity plus $o(1)$" of Step 2.B. Notation: Parts II.G$'$, III.A, III.D$'''$,
III.F$'$, III.F$'''$, III.F$''''$, III.G$''$, III.G$''''$, III.H, III.I-III.I$''''''''''$; no instrument is used.

## 1. Setting

Everything of III.I$''''''''''$ section 1 is kept: (C5), (H4), $\Lambda$, $K(\lambda)$, $\mathcal E_{\mathrm{par}}$,
(G), $\mathcal E^0_{\mathrm{src}}$ and $\mathcal Y^0(\alpha)$, and the rows $\mathcal N = \mathcal N_\iota\cup\mathcal
N_\sigma$ of its section 3. *Spectral notation* (III.I$''$ section 4, III.I$''''''$ sections 1-2):
$X^\pm_{\mathrm{sc}\text-\mathrm b}$ with the faces scf, tf, zf and $|\sigma| = \rho_{\mathrm{tf}}\rho_{\mathrm{zf}}$,
$\hat r = |\sigma|r$; $\chi_{\mathrm{zf}}$, $\chi_{\mathrm{tf}}$, $\chi^\sharp_{\mathrm{tf}}$;
$\widehat{L_{b_0}}(\sigma) = L_0-i\sigma L_1-\sigma^2L_2$ with $L_1$ of one order of decay at $\partial X$
(III.I$''''''$ Lemma 1.1); $\tilde L_{b_0}(\sigma)$ of III.H, $\tilde L_{b_0}(\sigma)(u,\dot b,S) =
(\widehat{L_{b_0}}(\sigma)u+\hat f_{\dot b}(\sigma)+\hat f_S(\sigma),r(u))$, with $\hat g^{\mathrm{aug}}(\sigma)(\dot b)
= i\sigma^{-1}G_1(\sigma)(\dot b)$ and $\hat h^{\mathrm{aug}}(\sigma)(S) = -\sigma^{-2}G_2(\sigma)(S)$, where
$$G_1(\sigma)(\dot b) := \Psi\dot g(\dot b),\qquad G_2(\sigma)(S) := \Psi
h(S)-\sigma\partial_\sigma\Psi\,h(S)-i\sigma\Psi\breve h(S)\tag{1.1}$$
(III.H Lemma 2.5, (2.6) there), $\Psi(\sigma,x) = \int e^{i\sigma t_*}\partial_{t_*}\chi_K\,dt_*$ entire in $\sigma$,
$\Psi(0,\cdot) = 1$; $\widehat{L_{b_0}}(\sigma)\hat g^{\mathrm{aug}}(\sigma)(\dot b) = \hat f_{\dot b}(\sigma)$,
$\widehat{L_{b_0}}(\sigma)\hat h^{\mathrm{aug}}(\sigma)(S) = \hat f_S(\sigma)$, and for $\mathrm{Im}\,\sigma>0$ these
are the Fourier transforms of $\chi_K\dot g(\dot b)$ and of $h^{\mathrm{aug}}(S)$. $\mathcal F$ is the Fourier transform
in $t_*$, $\hat w(\sigma) = \int e^{i\sigma t_*}w\,dt_*$.

*Dictionary.* (III.A Proposition 4.2, III.I$''''''$ Steps 3-5.) A zf-term $|\sigma|^z(\log|\sigma|)^m$ corresponds to
the $K^+$-term $t_*^{-z-1}(\log t_*)^{\le m}$, a zf-weight $w$ to the $K^+$-weight $w+1$; a tf-weight (exponent) $w$ of
$\hat u$ to the $\iota^+$-weight (exponent) $w+1$ of $u$; the $\iota^+$-exponent $\zeta+2$ of a source to the
tf-exponent $\zeta+1$ of its transform; and the Taylor coefficient of order $m$ at zf of a function of tf-weight $w$ has
weight $w-m$ at $\partial X$. *Levels.* At the Taylor level $j$ (after $j$ divisions by $\sigma$), a tf-exponent $\zeta$
of the current source corresponds to the $u$-exponent $\zeta+j-1$; a zero-energy solution at level $j$ with exponent $z$
at $\partial X$ to the $u$-exponent $z+j+1$. A row of $u$-exponent $\lambda$ has $K^+$-rate $\lambda-1$ (s1), $\lambda$
(s0, s2) or $\lambda+d_\tau$ (c0, c1).

*Constants.* Let $\alpha = 4+\epsilon_K-\epsilon'$ be admissible (III.I$''''''''''$ Definition 1.3;
$0<\epsilon'<\epsilon'_0<\epsilon_K$, so $\alpha>4$). Fix $\eta_1,\eta_2\in(\epsilon_K,\epsilon_+)$, $\eta_1<\eta_2$,
such that no $\lambda\in\Lambda$ has real part $2+\eta_1$ or $3+\eta_2$; below $\epsilon_+$, so that every exponent
treated has $u$-exponent below $3+\epsilon_+$, where the source is polyhomogeneous and III.I$''''''''''$ Lemma 1.2 (c)
counts the logs. *The exclusion set of III.I$''''''''''$ Definition 1.3* is the finite set of $\epsilon'$ for which one
of the conditions (4.2) of III.G$''''$ Proposition 4.4 fails at the levels 1 and 2 below (for the finitely many
$\alpha_0$ treated there, with $\ell_{\mathrm{zf}} = \alpha-1-j-\epsilon$), one of the conditions of its Proposition 5.1
fails at level 3 (finitely many rounds), or $\alpha-4-\epsilon$ is a real part excluded in III.I$''$ Lemma 4.2 or III.H
(1.1); $\epsilon>0$ is then taken small, with $2\epsilon<\epsilon_+-\eta_2$, and off a finite set as well. The orders
$\mu_j\in(2,3)$ of the zero-energy solves are chosen off the real parts of the exponents at hand.

*The a priori facts.* $f^\flat$ is III.I$''''''''''$ Proposition 3.1 (c)'s source for $f\in\mathcal Y^0(\alpha)$, and
$v$ the forward solution of $L_{b_0}v = f^\flat$. In section 3, $v = u-u_I-u_\iota$ with $u$ as in Lemma 3.2's
hypothesis, so $v$ has $K^+$-weight $w_v>0$ and $\iota^+$-weight $\beta'_+$ (III.I$''''''''''$ Proposition 3.1 (a)-(b):
$u_I$ vanishes near $K^+$, and the rows of $\mathcal N_\iota$ have rates $\ge\lambda_\sharp-1>0$).

**Lemma 1.1 (the column terms at $b_0$).** On $\{r\ge1\}$, $\hat f_{\dot b}(\sigma) = r^{-3}G(\sigma r,x)$ and $\hat
f_S(\sigma) = r^{-3}G(\sigma r,x)$ (on $\{r\ge1\}$, $f_{\dot b}$ and $f_S$ are supported in $\{2r\le t_*\le4r\}$, III.H
Lemma 2.2 (b)'s proof, and $G$ is as in III.H (2.3) with $f$ in place of $f_\infty$; $G = G_{\dot b}$, resp. $G_S$,
linear in $\dot b$, resp. $S$), where $G(\zeta,x) = \int_2^4e^{i\zeta s}F(s,x)\,ds$ and $F$ is smooth in $s$, supported
in $s\in[2,4]$, and polyhomogeneous at $\partial X$ with all its $s$-derivatives, with an index set $\mathcal
E_{\mathrm{col}}\subset\{\mathrm{Re}\ge0\}$ that does not depend on $\dot b$, $S$. Hence $G(\zeta,\cdot)$ is
polyhomogeneous with the index set $\mathcal E_{\mathrm{col}}$, its coefficients and remainders entire in $\zeta$ and
$O(\langle\zeta\rangle^{-N})$ on $\{\mathrm{Im}\,\zeta\ge0\}$ for every $N$; $\hat f_{\dot b}(0),\hat f_S(0)\in\mathcal
A^{3+\mathcal E_{\mathrm{col}}}$ near $\partial X$; and on $X^\pm_{\mathrm{sc}\text-\mathrm b}$ near tf, where
$\rho_{\mathrm{tf}} = r^{-1}$ up to a factor smooth in $\hat r$ and $\sigma r = \pm\hat r$, $\hat f_{\dot b}$ and $\hat
f_S$ are polyhomogeneous at tf with the index set $3+\mathcal E_{\mathrm{col}}$, smooth in $\hat r$ up to zf and rapidly
decaying at scf.

*Proof.* On $\{r\ge1\}$, $\chi_K = \chi_c(r/t_*)$ (III.H (1.2)), and $L_{b_0}\dot g(\dot b) = 0$,
$L_{b_0}(t_*h(S)+\breve h(S)) = 0$ (III.H section 2), so there $f = L_{b_0}(\chi_Kw) = [L_{b_0},\chi_K]w$ with $w = \dot
g(\dot b)$, resp. $t_*h(S)+\breve h(S)$. On sections $a(t_*)w(x)$, $L_{b_0} = L_0+L_1\partial_{t_*}+L_2\partial^2_{t_*}$
($L_1 = [L_{b_0},t_*]$, $L_2 = \frac12[[L_{b_0},t_*],t_*]$; III.I$''''''$ section 1), with
$L_k\in\rho^{2-k}\mathrm{Diff}^{2-k}_{\mathrm b}(\bar X)$ of smooth coefficients (III.I$'''$ Lemma 1.1, as it is applied
to them there). The $t_*$-derivatives and the b-derivatives in $x$ of $\chi_c(r/t_*)$ are sums of terms
$r^{-k}\phi(t_*/r)$, $k\in\{0,1,2\}$, with $\phi$ smooth and, when at least one derivative falls on $\chi_c$, supported
in $[2,4]$; for instance $r\partial_r[\chi_c(r/t_*)] = (r/t_*)\chi'_c(r/t_*)$ and $\partial_{t_*}[\chi_c(r/t_*)] =
-r^{-1}(r/t_*)^2\chi'_c(r/t_*)$. So $[L_{b_0},\chi_K]w$ is a finite sum of terms $r^{-k}\phi(t_*/r)t_*^m(Qw_m)(x)$ with
$m\in\{0,1\}$, $Q\in\rho^q\mathrm{Diff}_{\mathrm b}$ of smooth coefficients, and $w_m$ among $\dot g(\dot b)$, $h(S)$,
$\breve h(S)$, which are polyhomogeneous at $\partial X$: $\dot g^\Upsilon_{b_0}(1,0)\in\mathcal A^{(2,0)\cup(2+\mathcal
E_{\mathrm{ind}})}$ and $\dot g^\Upsilon_{b_0}(0,\dot A)\in\mathcal A^{(3,0)\cup(3+\mathcal E_{\mathrm{ind}})}$
(III.F$'''$ Proposition 2.2 (2.2)), $h(S)\in\mathcal A^{(3,0)\cup(3+\mathcal E_{\mathrm{ind}})}$ (III.F$'''$ Proposition
4.1 (4.2)), and $\breve h(S)$ is built from the tower of III.D$'''$ Proposition 3.1 (2) (III.I$''''''''''$ Lemma 2.1
(b)), whose index sets $\mathcal E_{\mathrm{ind}}$ contains (III.I$''''''''$ section 1). With $t_* = sr$, $F(s,x) =
r^4f(sr,x)$ is a finite sum of terms $\phi(s)s^mr^{4-k+m}(Qw_m)(x)$: smooth in $s$, supported in $[2,4]$, and
polyhomogeneous in $x$ with an index set $E$ independent of $\dot b$, $S$. $F$ is bounded (III.H Lemma 2.4 (a) and its
proof), so its coefficients at the exponents of real part $<0$ vanish, and $\mathcal E_{\mathrm{col}} :=
E\cap\{\mathrm{Re}\ge0\}$ will do. The statements on $G$ follow by integrating the expansion of $F$ against $e^{i\zeta
s}$, with integrations by parts in $s$ for the decay in $\zeta$ ($\mathrm{Im}\,\zeta\ge0$, $s>0$), and $r^{-3}G(\sigma
r,x) = \rho^3_{\mathrm{tf}}G(\pm\hat r,x)$. $\square$

## 2. Lemmas

**Lemma 2.1 (zero energy with expansions).** Let $\mu\in(2,3)$, $\mu'\in(\mu,5]$, and let $F\in
H^{\infty,(E,\mu')}_{\mathrm b}(\bar X)$, partially polyhomogeneous at $\partial X$ with an index set $E$,
$\min\mathrm{Re}\,E>\mu$. Then $(\hat u,\dot b,S) := \tilde L_{b_0}(0)^{-1}(F,0,0)$ (III.H Proposition 3.2 with its
weight $\alpha_{\mathrm H} := \mu-4$, so that its $\alpha_{\mathrm H}+2 = \mu-2\in(0,1)$ is the $L^2$-b-weight of a
source of conormal order $\mu$) has $\hat u\in H^{\infty,(E',\mu'-2)}_{\mathrm b}(\bar X)$, where $E'$ is the index set
that III.A Lemma 1.4 builds from $(E-2)\cup(1+\mathcal E_{\mathrm{col}})$ and the indicial roots of
$\widehat{L_{b_0}}(0)$ (III.F$'$ Proposition 2.3) with real part in $(\mu-2,\mu'-2)$. Below the real part 3 the only
such root is 2 (type s0, the mass), so $E'$ lies in the extended union of $(E-2)\cup(1+\mathcal E_{\mathrm{col}})$ and
$(2,l_*)$, plus $\mathbb N_0$; in $u$-exponents at level $j$ these are $\Lambda$-valued (III.I$''''''''''$ Lemma 1.2).

*Proof.* III.H Proposition 3.2 gives $\hat u\in H^{\infty,\mu-2}_{\mathrm b}$ (conormal order $\mu-2$, as in
III.I$''''''$ Step 3.1). Near $\partial X$, $\widehat{L_{b_0}}(0) = \rho^2A$ with $A$ an elliptic b-operator (III.F$'$
section 2, as III.F$''''$ Proposition 5.1's proof uses it), and $\widehat{L_{b_0}}(0)\hat u = F-\hat f_{\dot b}(0)-\hat
f_S(0)$ there, with $\hat f_{\dot b}(0),\hat f_S(0)\in\mathcal A^{3+\mathcal E_{\mathrm{col}}}$ (Lemma 1.1). III.A Lemma
1.4 with $\alpha = \mu-2$ and $F$ replaced by $\rho^{-2}$ times the right side (index set $(E-2)\cup(1+\mathcal
E_{\mathrm{col}})$, remainder $\mu'-2$), applied finitely many times, each time from the remainder order the previous
application gave (each gains less than 1), gives the expansion up to $\mu'-2$. The roots: III.F$'$ Proposition 2.3 (a)
(none in $(0,1]$) and its list (decaying roots: 2 for s0; 3, $1+\lambda^\Upsilon_{\mathrm s1,2}$,
$1+\lambda^\Upsilon_{\mathrm s1,3}$, $5$ for s1; $3,4$ for v1; $l+2\ge4$ and above for $l\ge2$;
$1+\lambda^\Upsilon_{\mathrm s0,2}\in(3,3+\frac{z_\Upsilon}3]$, 4 for s0). $\square$

**Lemma 2.2 (one level).** Let $j\in\{0,1,2,3\}$, $g\in H^{\infty,(\frac52-\epsilon,(E,\tau),((0,0),z))}_{\mathrm
b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$ with $z>0$, its zf-coefficient $g(0)\in H^{\infty,(E,\tau)}_{\mathrm b}(\bar
X)$, and $(\hat u,\dot b,S)$ as in Lemma 2.1 for $F = g(0)$ and $\mu' = \tau$ (the same for both signs, or separately).
Put
$$g^{+1} := \sigma^{-1}\Big(g-\widehat{L_{b_0}}(\sigma)(\chi_{\mathrm{zf}}\hat u)-\hat f_{\dot b}(\sigma)-\hat
f_S(\sigma)\Big).\tag{2.1}$$
Then $g^{+1}\in H^{\infty,(\frac52-\epsilon,(E^{+1},\tau-1),((0,0),z-1))}_{\mathrm b}$ and
$$E^{+1}\subset(E-1)\cup(E'+1)\cup(2+\mathcal E_{\mathrm{col}}),$$
$E'$ the index set of $\hat u$; its zf-coefficient is $g_1+iL_1\hat u+(\ldots)$, where $g_1$ is the
$\sigma^1$-coefficient of $g$, and the exact formula is
$$g^{+1} = \sigma^{-1}\big(g-\chi_{\mathrm{zf}}g(0)\big)-\sigma^{-1}[L_0,\chi_{\mathrm{zf}}]\hat
u+i\chi_{\mathrm{zf}}L_1\hat u+i[L_1,\chi_{\mathrm{zf}}]\hat u+\sigma\chi_{\mathrm{zf}}L_2\hat u-\sigma^{-1}\big(\hat
f_{\dot b}(\sigma)+\hat f_S(\sigma)-\chi_{\mathrm{zf}}(\hat f_{\dot b}(0)+\hat f_S(0))\big).$$

*Proof.* $\widehat{L_{b_0}}(\sigma)(\chi_{\mathrm{zf}}\hat u) = \chi_{\mathrm{zf}}L_0\hat u+[L_0,\chi_{\mathrm{zf}}]\hat
u-i\sigma(\chi_{\mathrm{zf}}L_1\hat u+[L_1,\chi_{\mathrm{zf}}]\hat u)-\sigma^2\chi_{\mathrm{zf}}L_2\hat u$ exactly, and
$L_0\hat u+\hat f_{\dot b}(0)+\hat f_S(0) = g(0)$; this gives the formula. The terms:
$\sigma^{-1}(g-\chi_{\mathrm{zf}}g(0))$ has the tf-index set $E-1$ (division by $\sigma =
\rho_{\mathrm{tf}}\rho_{\mathrm{zf}}$) and zf $((0,0),z-1)$; the commutators are supported where $\hat r\sim1$, away
from zf, and by III.I$'''$ Lemma 1.1 (b) both have the tf-index set $E'+1$ ($E'+2-1$ for
$\sigma^{-1}[L_0,\chi_{\mathrm{zf}}]\hat u$; $E'+1$ for $[L_1,\chi_{\mathrm{zf}}]\hat u$, as
$L_1\in\rho\mathrm{Diff}^1_{\mathrm b}$); $\chi_{\mathrm{zf}}L_1\hat u$ has $E'+1$, and $\sigma\chi_{\mathrm{zf}}L_2\hat
u$ has $E'+1$ ($L_2$ without decay, $\sigma$ adding one at tf); all are polynomial in $\sigma$ at zf. The column terms:
by Lemma 1.1, on $\{r\ge1\}$, $\sigma^{-1}(\hat f(\sigma)-\chi_{\mathrm{zf}}\hat f(0)) = r^{-2}H(\sigma r,x)$ with
$H(\zeta,x) := (G(\zeta,x)-\chi(|\zeta|)G(0,x))/\zeta$, $\chi_{\mathrm{zf}} = \chi(\hat r)$, which is smooth in $\zeta$
up to 0 ($G$ is entire), polyhomogeneous in $x$ with the index set $\mathcal E_{\mathrm{col}}$, and rapidly decaying as
$|\zeta|\to\infty$; near tf, $r^{-2} = \rho^2_{\mathrm{tf}}$ and $\zeta = \pm\hat r$, so this has the tf-index set
$2+\mathcal E_{\mathrm{col}}$, Taylor expansions at zf and rapid decay at scf. On $\{r\le2\}$, $\hat f_c$ is entire
(III.H Lemma 2.4 (a)) and $\chi_{\mathrm{zf}} = 1$ there for $|\sigma|$ small, so that part is polynomial at zf. The
tf-weights: $\tau-1$ and $\mu'_{\hat u}+1 = \tau-1$ ($\mu'_{\hat u} = \tau-2$ the remainder order of $\hat u$); the
columns are polyhomogeneous. $\square$

**Lemma 2.3 (III.G$''''$ Proposition 4.4's pieces in compact sets).** Let $u$ be the solution of III.G$''''$ Proposition
4.4 for a source with tf-leading term at $(\alpha_0,k)$, $k = 0$ (for $k>0$ apply the following to the
$\alpha_0$-derivatives). On $\{r\le R\}$ and for $0<\pm\sigma\le c_R$, $u = |\sigma|^{\alpha_0-2}u_b$ (there
$\chi_{\mathrm{zf}} = 1$, and $\chi_{\mathrm{tf}} = \chi_2(\rho+|\sigma|) = 0$ if $R<2/\rho_0$, III.G$''''$ section 1;
for larger $R$ the tf-part adds integer-degree, log-free terms $\sigma^j|\sigma|^kc(x)$ and a zf-remainder of weight
$\ell_{\mathrm{zf}}+j$; the total $\chi\hat v$ leaves no $K^+$-tail by III.I$''''''''''$ Lemma 2.4 (b), although a
sign-odd term $\sigma^j|\sigma|^kc(x)$ alone has a two-sided one, which III.I$''''''''''''$ Theorem 3.1's (vi) records,
so the conclusions below are unchanged), and
$$|\sigma|^{\alpha_0-2}u_b = \sum_\tau c_\tau(\sigma)\,T_\tau(\sigma)+P_{\mathrm{int}}(\sigma),\tag{2.2}$$
where: $T_{\mathrm s1}(\sigma) := h^{\le3}_{b_0,\mathrm s1}(\sigma,S^{(-1)}_1) = \sum_{i\le3}(-i\sigma)^i\breve
h^i_{\mathrm s1}(S^{(-1)}_1)$ and $c_{\mathrm s1}(\sigma) := |\sigma|^{\alpha_0-1}\sigma^{-2}/(2-\alpha_0)$
($-|\sigma|^{-1}\log|\sigma|$ at $\alpha_0 = 2$); for the other rows $(\mu,\tau)$ of III.G$''$ Table 1.1,
$T_\tau(\sigma) := h^{(\mu),\le c_\mu}_{b_0,\tau}(\sigma,Y^{(\mu)}_\tau)$ and $c_\tau(\sigma) :=
-|\sigma|^{\alpha_0-2-\mu}/\beta_\mu(\alpha_0)$ ($|\sigma|^{\lfloor-\mu\rfloor}\log|\sigma|$ if $\beta_\mu(\alpha_0) =
0$, which for c0, c1 happens at $\alpha_0 = 2+\mu\in(1,2)$, and for the class rows in $(-\frac54,-1)$ and
$(-\frac94,-2)$ at $\alpha_0 = 3+\mu$ and $4+\mu$), $\beta_\mu(\alpha_0) = 2-\alpha_0-\{-\mu\}$ (III.G$''''$ (3.2)); the
v1 term has $h_{b_0,\mathrm v1}(V) = 0$ (every $V$ Killing at $b_0$), so it carries $\sigma$ at least once; and
$P_{\mathrm{int}}$ is a finite sum of terms $|\sigma|^m\,\mathrm{sgn}(\sigma)^{\delta}q(\sigma,x)$ with $m\in\mathbb Z$,
$\delta\in\{0,1\}$, $q$ polynomial in $\sigma$ (and $\log r$), without $\log|\sigma|$: namely
$-|\sigma|^{-1}h(S^{(-1)}_1)/(2-\alpha_0)$ (for $\alpha_0\ne2$; at $\alpha_0 = 2$ it is part of $c_{\mathrm s1}$),
$i\,\mathrm{sgn}(\sigma)r^{2-\alpha_0}\breve h^{\le3}_{b_0,\mathrm s1}(\sigma,S^{(-1)}_1)/(2-\alpha_0)$ (with $\log r$
in place of $r^{2-\alpha_0}/(2-\alpha_0)$ at $\alpha_0 = 2$), and
$|\sigma|^{\lfloor-\mu\rfloor}r^{\beta_\mu}T_\tau(\sigma)/\beta_\mu$ (with $\log r\,|\sigma|^{\lfloor-\mu\rfloor}T_\tau$
when $\beta_\mu = 0$). The towers $T_\tau(\sigma)$ are the first sum of (2.3) of III.I$''''''''''$ Lemma 2.1 (d),
without its top term $(-i\sigma)^{K+1}dt_*\otimes_s\breve\omega^K$, for the corresponding 1-form towers (the rows are
unaffected: that term has rate $e_\nu+K+1$).

*Proof.* III.G$''''$ (4.4) with $l_\beta(\hat r) = (|\sigma|^\beta r^\beta-1)/\beta$ (III.G$''''$ Definition 2.3) and
$G^{\mathrm{exc}}_{\mathrm s1} = -|\sigma|\sigma^{-2}h(S)$, $G_{\mathrm s1} = |\sigma|i\sigma^{-1}\breve
h^{\le3}_{b,\mathrm s1}(\sigma,S)$, $G_{\mu,\tau} = |\sigma|^{-\mu}h^{(\mu),\le c_\mu}_{b,\tau}(\sigma,Y)$ (III.G$''''$
Lemma 4.3). The s1 terms: $|\sigma|^{\alpha_0-2}\big(-l_{2-\alpha_0}(|\sigma|)|\sigma|\sigma^{-2}h+l_{2-\alpha_0}(\hat
r)|\sigma|i\sigma^{-1}\breve h^{\le3}\big)$ equals $(2-\alpha_0)^{-1}$ times
$-|\sigma|^{-1}h+|\sigma|^{\alpha_0-1}\sigma^{-2}h+i\,\mathrm{sgn}(\sigma)r^{2-\alpha_0}\breve
h^{\le3}-i|\sigma|^{\alpha_0-1}\sigma^{-1}\breve h^{\le3}$, and $|\sigma|^{\alpha_0-1}\sigma^{-2}(h-i\sigma\breve
h^{\le3}) = c_{\mathrm s1}(2-\alpha_0)h^{\le3}(\sigma,S)$ (III.G$''''$ (5.2)'s definition). The other rows:
$|\sigma|^{\alpha_0-2-\mu}l_{\beta_\mu}(\hat r) =
(|\sigma|^{\alpha_0-2-\mu+\beta_\mu}r^{\beta_\mu}-|\sigma|^{\alpha_0-2-\mu})/\beta_\mu$ with $\alpha_0-2-\mu+\beta_\mu =
\lfloor-\mu\rfloor$. At $\beta = 0$, $l_0(\hat r) = \log|\sigma|+\log r$. The towers: III.G$''''$ Definition 4.1 defines
them as $\sum_j(-i\sigma)^j\breve h^{(\mu),j}_b$ with III.G$''$'s companions, which are those of III.I$''''''''''$ Lemma
2.1 (b) (for s0 with the shift of index). $\square$

**Lemma 2.4 (the column pieces).** For $\dot b\in\mathfrak b_{\mathbb C}$, $S\in\mathcal S_{1,\mathbb C}$ and
$j\in\mathbb N_0$, the distributions $\sigma^j\hat g^{\mathrm{aug}}(\sigma)(\dot b)$, $\sigma^j\hat
h^{\mathrm{aug}}(\sigma)(S)$ on $\mathbb R$ (boundary values from $\mathrm{Im}\,\sigma>0$) are the Fourier transforms of
$(i\partial_{t_*})^j(\chi_K\dot g(\dot b))$ and $(i\partial_{t_*})^jh^{\mathrm{aug}}(S)$. In $\{r\le R\}$, for large
$t_*$: the first is $\chi_K\dot g(\dot b)$ for $j = 0$ and vanishes for $j\ge1$; the second is $t_*h(S)+\breve h(S)$ for
$j = 0$, $ih(S)$ for $j = 1$, and vanishes for $j\ge2$. If $\dot b(\sigma)$, $S(\sigma)$ lie in $H^{\infty,a}_{\mathrm
b}(\pm(0,c],|\frac{d\sigma}\sigma|)$, then $\chi\sigma^j\hat g^{\mathrm{aug}}(\dot b(\sigma))$ and $\chi\sigma^j\hat
h^{\mathrm{aug}}(S(\sigma))$ have inverse transforms of $K^+$-weight $a+j$ and $a+j-1$ and $\iota^+$-weight
$\frac32-\epsilon$ (III.I$''$ Lemma 4.3 for their classes on $X^\pm_{\mathrm{sc}\text-\mathrm b}$, III.A Proposition 4.2
(2) for the inverse transforms).

*Proof.* III.H Lemma 2.5 (a) and $\partial_{t_*}\leftrightarrow-i\sigma$; $\chi_K = 1$ near $K^+$ in $\{r\le R\}$, and
$h^{\mathrm{aug}}(S) = \chi_K(t_*h(S)+\breve h(S))$ (III.H section 2). The last statement is III.I$''$ Lemma 4.3 with
$a$ (for $\hat g^{\mathrm{aug}}$, which carries $\sigma^{-1}$, and $\hat h^{\mathrm{aug}}$, which carries $\sigma^{-2}$,
the weights $a+j-1+1$ and $a+j-2+1$). $\square$

**Lemma 2.5 (the decomposition).** Let $\hat f\in H^{\infty,(\frac52-\epsilon,\tau,((0,0),z))}_{\mathrm b}$ on
$\pm(0,c]$, and suppose that $\hat f = \sum_{i\in I}\widehat{L_{b_0}}(\sigma)P_i+\sigma^Jg_J$ on $0<|\sigma|\le c$,
where each $P_i(\sigma)$ lies in $\mathcal X'_\sigma$ of III.I$''''''$ Lemma 1.2 for $\sigma\ne0$ (a section smooth on
$X^\circ$ and b-conormal at $\partial X$, or a sum of $\hat g^{\mathrm{aug}}$ and $\hat h^{\mathrm{aug}}$ terms), and
let $(\hat u_f,\dot b_f,S_f) := \tilde L_{b_0}(\sigma)^{-1}(g_J,0,0)$. Then the outgoing inverse satisfies, for
$0<|\sigma|\le c$,
$$\widehat{L_{b_0}}(\sigma)^{-1}\hat f = \sum_iP_i+\sigma^J\big(\hat u_f+\hat g^{\mathrm{aug}}(\sigma)(\dot b_f)+\hat
h^{\mathrm{aug}}(\sigma)(S_f)\big).\tag{2.3}$$

*Proof.* Apply $\widehat{L_{b_0}}(\sigma)$: the right side maps to
$\sum_i\widehat{L_{b_0}}P_i+\sigma^J(\widehat{L_{b_0}}\hat u_f+\hat f_{\dot b_f}+\hat f_{S_f}) = \hat f$, by III.H Lemma
2.5 (c) and the first component of $\tilde L_{b_0}(\sigma)(\hat u_f,\dot b_f,S_f) = (g_J,0)$. Every term lies in
$\mathcal X'_\sigma$ (III.H Lemma 2.5 (b), III.I$''''''$ Lemma 1.2), on which $\widehat{L_{b_0}}(\sigma)$ is injective,
and $\widehat{L_{b_0}}(\sigma)^{-1}\hat f$ is the element of $\mathcal X_\sigma\subset\mathcal X'_\sigma$ with this
image. $\square$

The rows $r(\cdot)$ and the columns of $\tilde L_{b_0}$ thus enter only through the zero-energy solves (Lemma 2.1) and
the last level; no assembly of the augmented components, as in III.I$''''''$ (2.8) and III.I$''''''''$ (3.3), is needed.

## 3. The spectral phase and the expansion ([Hin26] Theorem 11.59, Steps 2.A.3-2.A.8 and Part 3, at n = 4)

**Proposition 3.1 (the spectral phase).** Let $\alpha$ be admissible, $\alpha>4$, and $f^\flat$, $v$ as in section 1.
Then there are $S_\nu\in\mathcal W_{\tau,\mathbb C}$, $\nu\in\mathcal N_\sigma$, linear and continuous in $f$, with
$$v-\sum_{\nu\in\mathcal N_\sigma}m_\nu(S_\nu)\in\bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\beta'_+,\alpha-2-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}.\tag{3.1}$$

*Proof.* *Step 0 (decomposition and transform; III.I$''''''$ Step 3).* $v = v_{\mathrm{hi}}+v_{\mathrm{low}}$, $\mathcal
Fv_{\mathrm{low}} = \chi(|\sigma|)\hat v$; III.I$''$ Lemma 4.1 ($\beta^f_I = \ell_I$, $\beta_\iota = w_+-2-\epsilon$,
$\beta_K = \alpha-\epsilon$; $\ell_I+1\ge w_+-\epsilon-(1-\epsilon_1)$ by (H4)) gives $v_{\mathrm{hi}}\in
H^{\infty,(\frac32-\epsilon,N,N)}_{\mathrm b}(M')$. III.A Proposition 4.2 (1) with $\beta_I = \ell_I+1$, $\beta_\iota =
w_+-\epsilon$, $E_\iota = \mathcal E^\flat+2$, $E_I = \emptyset$, $\beta_K = \alpha-\epsilon$, $E_K = \emptyset$ (its
(4.2): $\ell_I+1>w_+-1-\epsilon$ by (H4)) gives
$$g_0 := \hat f^\flat|_{\pm(0,c]}\in H^{\infty,(\frac52-\epsilon,(\mathcal
E^\flat+1,w_+-1-\epsilon),((0,0),\alpha-1-\epsilon))}_{\mathrm b},$$
tf-exponents of real part $\ge3$, $u$-exponents (level 0) in $\Lambda$. We construct pieces $P_i$ and $g_J$, $J = 3$, as
in Lemma 2.5.

*Step 1 (level 0; the source's Step 2.A.3).* Lemma 2.1 with $\mu_0 := 3-\epsilon$, $\mu' := w_+-1-\epsilon$, $F =
g_0(0)$, gives $(\hat u_0,\dot b_0,S_0)$, the same for both signs; $\hat u_0$ has the exponents $(\mathcal
E^\flat-1)\cup(1+\mathcal E_{\mathrm{col}})\cup(2,\cdot)$ (and their $\mathbb N_0$-shifts) below $\mu'-2 =
2+\epsilon_+-\epsilon$, the root 2 being the mass. $S_0 = 0$ by III.I$''''''$ Step 3.1's argument ($f^\flat$ lies in the
space of III.I$'''''$ Proposition 2.1's Step 3, and $v$ has $K^+$-weight $>-1$). Pieces: $\chi_{\mathrm{zf}}\hat u_0$,
$\hat g^{\mathrm{aug}}(\dot b_0)$. Lemma 2.2 gives $g_1$: tf-exponents of real part $\ge2$, $u$-exponents in $\Lambda$
(level 1), tf-weight $3+\epsilon_+-\epsilon$, zf $((0,0),\alpha-2-\epsilon)$.

*Step 2 (level 1; Steps 2.A.4-2.A.5).* For each tf-exponent $(\alpha_0,k)$ of $g_1$ with
$2\le\mathrm{Re}\,\alpha_0<2+\eta_1$ (finitely many), III.G$''''$ Proposition 4.4 with $\ell_{\mathrm{zf}} :=
\alpha-2-\epsilon$, $\ell_{\mathrm{scf}} := \frac32-\epsilon$ applies (admissibility), to the corresponding term (with
its whole tf-coefficient), and gives $u_{(\alpha_0,k)}$; the pieces are $\sigma u_{(\alpha_0,k)}$. The remainder
$g_1-\sum\widehat{L_{b_0}}(\sigma)u_{(\alpha_0,k)}$ has tf-exponents in $((\alpha_0,k)+\mathcal
E_{\mathrm{ind}})\cup((4,k+1)+\mathcal F)$ (III.G$''''$ (4.3)), of real part $\ge2+\epsilon_{\mathrm{ind}}>2+\eta_1$,
and the other exponents of $g_1$, $\ge2+\eta_1$ by the choice of $\eta_1$; zf unchanged. Lemma 2.1 with $\mu_1 :=
2+\eta_1$, $\mu' := 3+\epsilon_+-\epsilon$ on its zf-coefficient (both signs separately) gives $(\hat u_1,\dot
b_1,S_1)^\pm$; pieces $\sigma(\chi_{\mathrm{zf}}\hat u_1+\hat g^{\mathrm{aug}}(\dot b_1)+\hat h^{\mathrm{aug}}(S_1))$;
and Lemma 2.2 gives $g_2$, with tf-exponents of real part $\ge1+\eta_1$ (those of $\hat u_1$, at least $\eta_1$, plus
one; the remainder's, at least $2+\eta_1$, minus one; the columns' $2+\mathcal E_{\mathrm{col}}$), tf-weight
$2+\epsilon_+-\epsilon$, zf $((0,0),\alpha-3-\epsilon)$.

*Step 3 (level 2; Steps 2.A.6-2.A.7).* For each tf-exponent $(\alpha_0,k)$ of $g_2$ with
$1+\eta_1\le\mathrm{Re}\,\alpha_0<2+\eta_2$, III.G$''''$ Proposition 4.4 with $\ell_{\mathrm{zf}} := \alpha-3-\epsilon$;
its remainder exponents $\alpha_0+\mathcal E_{\mathrm{ind}}$ may again lie below $2+\eta_2$, and are treated in turn
(finitely many rounds, the real parts rising by $\ge\epsilon_{\mathrm{ind}}$); $(4,k+1)$ lies above. Pieces
$\sigma^2u_{(\alpha_0,k)}$. Then Lemma 2.1 with $\mu_2 := 2+\eta_2$, $\mu' := 2+\epsilon_+-\epsilon$, pieces
$\sigma^2(\chi_{\mathrm{zf}}\hat u_2+\hat g^{\mathrm{aug}}(\dot b_2)+\hat h^{\mathrm{aug}}(S_2))$, and Lemma 2.2 gives
$g_3$, of tf-weight $\tau_3 := 1+\eta_2-2\epsilon$ (conormal; its expansion is not needed), zf $((0,0),\ell_3)$, $\ell_3
:= \alpha-4-\epsilon\in(0,\epsilon_K)$.

*Step 4 (level 3; Step 2.A.8 and Part 3).* Fix $\delta>0$ with $\delta+\ell_3+2\epsilon<\epsilon_{\mathrm{ind}}$. While
the tf-weight $\tau$ of the current level-3 source is at most $2+\ell_3+\epsilon$, apply III.G$''''$ Proposition 5.1
with $\alpha_\tau := \min(\tau,2-\delta)\in(1,2)$ (the source has tf-weight $\alpha_\tau$), $\ell_{\mathrm{zf}} :=
\ell_3$, $k_0 := 0$, $w = \ell_3-\alpha_\tau+2\in(0,1)$ ($\alpha_\tau\ge\tau_3>1+\ell_3$ as $\eta_2>\epsilon_K>\ell_3$);
its conditions $w\ne-\mu$, $2-\alpha_\tau+j\ne-\mu$ hold for $\epsilon$ off a finite set (admissibility) and, when
$\alpha_\tau = 2-\delta$, for $\delta$ off the finite set $\{-\mu-j\}$, which we impose on $\delta$. It gives $u =
\chi_{\mathrm{zf}}u_b+\chi^\sharp_{\mathrm{tf}}\tilde u\in
H^{\infty,(\frac32-2\epsilon,\alpha_\tau-2,\alpha_\tau-3)}_{\mathrm b}$ with remainder of tf-weight
$\alpha_\tau+\epsilon_{\mathrm{ind}}-\epsilon$, which exceeds $\tau$ by $\epsilon_{\mathrm{ind}}-\epsilon$ when
$\alpha_\tau = \tau$, and, when $\alpha_\tau = 2-\delta<\tau$, exceeds $2+\ell_3+\epsilon$ (as
$\delta+\ell_3+2\epsilon<\epsilon_{\mathrm{ind}}$), after which the loop ends; pieces $\sigma^3u$. After finitely many
rounds $\tau>2+\ell_3+\epsilon$; lowering $\tau$ if necessary (a source of tf-weight $\tau$ has every smaller
tf-weight), $\tau\in(2+\ell_3+\epsilon,3)$. Lemma 2.1 with $\mu_3 := \tau-\epsilon$, $\mu' := \tau$ and $E = \emptyset$
gives $(\hat u_3,\dot b_3,S_3)^\pm$ and pieces $\sigma^3(\chi_{\mathrm{zf}}\hat u_3+\hat g^{\mathrm{aug}}(\dot b_3)+\hat
h^{\mathrm{aug}}(S_3))$; the rest,
$$g_J := \text{the level-3 source}-\widehat{L_{b_0}}(\sigma)(\chi_{\mathrm{zf}}\hat u_3)-\hat f_{\dot b_3}-\hat
f_{S_3}\in H^{\infty,(\frac52-\epsilon,\tau-\epsilon,\ell_3)}_{\mathrm b}$$
(zf-coefficient removed, the next Taylor order being 1; tf by Lemma 2.2's computation without the division), is inverted
by III.I$''$ Lemma 4.2 with $\beta_{\mathrm{scf}} := \frac32-2\epsilon$, $\beta_{\mathrm{tf}} := \tau-2-\epsilon$,
$\beta_{\mathrm{zf}} := \ell_3$, $\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}}\in(0,1)$: $\hat u_f\in
H^{\infty,(\frac32-3\epsilon,\tau-2-\epsilon,\ell_3)}_{\mathrm b}$, $\dot b_f,S_f\in H^{\infty,\ell_3}_{\mathrm
b}(\pm(0,c],|\frac{d\sigma}\sigma|)$.

*Step 5 (matching, and the pieces at $K^+$).* By Lemma 2.5, on $0<|\sigma|\le c$, $\hat v$ is the sum of the pieces and
$\sigma^3(\hat u_f+\hat g^{\mathrm{aug}}(\dot b_f)+\hat h^{\mathrm{aug}}(S_f))$. The data at levels 1-3 were found for
each sign; write $S_1^\pm = S_e\pm S_o$. *Matching* (as in III.I$''''''$ Step 5, and the source's "minor caveat" on p.
287). Multiplied by $\sigma$, every piece is bounded near $\sigma = 0$: $\sigma\cdot\sigma\hat h^{\mathrm{aug}}(S_1^\pm)
= -G_2(\sigma)(S_1^\pm)$ and $\sigma\cdot\sigma\hat g^{\mathrm{aug}}(\dot b_1^\pm) = i\sigma\Psi\dot g(\dot b_1^\pm)$ by
(1.1), $\sigma\hat g^{\mathrm{aug}}(\dot b_0) = i\Psi\dot g(\dot b_0)$, the columns of levels 2-3 carry $\sigma^{\ge2}$,
and the other pieces have degree $\ge0$ (Lemma 2.3: $\sigma^{j+1}c_\tau(\sigma)$ has degree $\ge\alpha_0-2+j\ge0$,
$\sigma^{j+1}P_{\mathrm{int}}$ degree $\ge j\ge1$) or zf-weight $>0$ (Step 4, the last level). So $\mathcal
F(\partial_{t_*}v_{\mathrm{low}}) = -i\sigma\chi\hat v$ and $-i\sigma\chi$ times the sum differ by a distribution
supported at 0, whose inverse transform, a polynomial, tends to 0 as $t_*\to-\infty$ ($\partial_{t_*}v_{\mathrm{low}} =
-\partial_{t_*}v_{\mathrm{hi}} = O(|t_*|^{-\infty})$ there, $v = 0$ for $t_*<1$; the other by the Riemann-Lebesgue
lemma) and so vanishes. Near $\sigma = 0$, $-i\sigma\chi$ times the sum is $i\chi\,\mathrm{sgn}(\sigma)h(S_o)$ ($G_2(0)
= h$, III.H Lemma 2.5 (b)) plus terms whose inverse transforms have $K^-$-weight $>1$ in $\{r\le R\}$: the sign-even
part of $iG_2(\sigma)(S_1^\pm)$ and $\Psi\dot g(\dot b_0)$ (the $-i\sigma$-multiples of the terms above) are smooth in
$\sigma$; every other piece times $\sigma$ is, in $\{r\le R\}$, a sum of
$\mathrm{sgn}(\sigma)^\delta|\sigma|^z(\log|\sigma|)^m$ times smooth sections with $\mathrm{Re}\,z>0$ (Lemma 2.3, with
$\chi_{\mathrm{zf}} = 1$ there for $|\sigma|\le c_R$), whose inverse transforms are
$O(|t_*|^{-1-\mathrm{Re}\,z}\log^m)$, or of zf-weight $>0$ (II.G$'$ (2.26a)). The inverse transform of
$\chi\,\mathrm{sgn}(\sigma)$ is $c\,t_*^{-1}(1+o(1))$ as $t_*\to-\infty$, $c\ne0$. Hence $h(S_o) = 0$ on $\{r\le R\}$,
$S_o = 0$ (III.H (3.1)), and $S_1$ is the same for both signs. We then read the pieces of $\hat v$ itself, the column
pieces with constant coefficients as boundary values (Lemma 2.4) and the others locally integrable: as before, $\chi\hat
v$ and $\chi$ times their sum differ by a distribution supported at 0, a polynomial in $t_*$ after inverse transform,
which tends to 0 as $t_*\to-\infty$ ($v_{\mathrm{low}} = -v_{\mathrm{hi}}$ there, the column pieces with constant
coefficients vanish there as $\chi_K = 0$, the others by Riemann-Lebesgue) and so vanishes. We sort the inverse
transforms in $\{r\le R\}$, for large $t_*$:

(i) *Zero-energy pieces* $\sigma^j\chi_{\mathrm{zf}}\hat u_j^\pm$: in $\{r\le R\}$, $\chi_{\mathrm{zf}} = 1$ for
$|\sigma|\le c_R$, so they are $\mathrm{sgn}(\sigma)^\delta$ times polynomials in $\sigma$ there (the data of levels 1-3
may depend on the sign): integer degree, no $\log|\sigma|$.

(ii) *Column pieces* (Lemma 2.4): $\chi_K\dot g(\dot b_0)$ from level 0; $ih(S_1)$ from $\sigma\hat
h^{\mathrm{aug}}(S_1)$ at level 1 ($S_1$ sign-independent); $\sigma\hat g^{\mathrm{aug}}(\dot b_1^\pm) = i\Psi\dot
g(\dot b_e)\pm i\Psi\dot g(\dot b_o)$, whose first part contributes nothing for large $t_*$ and whose second is
$\mathrm{sgn}(\sigma)$ times a function smooth in $\sigma$ (integer degree, no $\log|\sigma|$); and at levels 2 and 3
the sign-even parts contribute nothing for large $t_*$, the sign-odd parts being again $\mathrm{sgn}(\sigma)$ times
smooth functions of $\sigma$.

(iii) *The last level.* $\sigma^3\hat u_f$ has zf-weight $\ell_3+3$, $\sigma^3\hat g^{\mathrm{aug}}(\dot b_f)$ and
$\sigma^3\hat h^{\mathrm{aug}}(S_f)$ give $K^+$-weights $\ell_3+3$ and $\ell_3+2 = \alpha-2-\epsilon$ (Lemma 2.4); the
level-3 pieces of Step 4 have zf-weight $\alpha_\tau-3+3\ge\tau_3 = 1+\eta_2-2\epsilon$, so $K^+$-weight
$\ge2+\eta_2-2\epsilon>\alpha-2$ ($\eta_2>\epsilon_K$), by III.A Proposition 4.2 (2) (on $\{r\le R\}$, II.G$'$ (2.26a)).

(iv) *The tf-model pieces at levels 1 and 2*, by Lemma 2.3: $\sigma^j\big(\sum_\tau
c_\tau(\sigma)T_\tau(\sigma)+P_{\mathrm{int}}(\sigma)\big)$. The terms of $\sigma^jP_{\mathrm{int}}$ are, in $\{r\le
R\}$, finite sums of $|\sigma|^m\mathrm{sgn}(\sigma)^\delta$ times polynomials in $\sigma$, $m+j\ge0$ ($m\ge-1$,
$j\ge1$): integer degree, no $\log|\sigma|$. The terms $\sigma^jc_\tau(\sigma)(-i\sigma)^i\breve h^i_\tau$ have degree
$\alpha_0-3+j+i$ for s1 ($c_{\mathrm s1}$ has degree $\alpha_0-3$) and $\alpha_0-2-\mu+j+i$ for the other rows, with
$\log|\sigma|$ at integer degree when $\alpha_0$ or $\beta_\mu$ is critical.

Now apply III.I$''''''''''$ Lemma 2.4 to $\chi\hat v$ in $\{r\le R\}$ ($V = C^\infty(\{r\le R\})$), with $\beta :=
\alpha-3-2\epsilon$ ($\epsilon$ off a finite set, so that $\beta\notin\mathbb N_0$); the hypothesis at $t_*\to-\infty$
holds as above ($v$ is forward). The terms of (i), the sign-odd column pieces of (ii) and those with $j\ge1$ in $\hat
g^{\mathrm{aug}}$ and $j\ge2$ in $\hat h^{\mathrm{aug}}$, and $\sigma^jP_{\mathrm{int}}$ have integer degree and no
$\log|\sigma|$, so contribute no tail (its (b)); (iii) contributes $O(t_*^{-\alpha+2+3\epsilon})$, as $\sigma^3\hat
h^{\mathrm{aug}}(S_f)$ has zf-weight $\ell_3+1 = \alpha-3-\epsilon>\beta$. So, for large $t_*$ in $\{r\le R\}$,
$$v = \chi_K\dot g(\dot b_0)+ih(S_1)+\sum_{\text{pieces (iv)}}\sum_{i}\big(\mathcal T_+c_\tau\big)^{(i)}(t_*)\,\breve
h^i_\tau+O(t_*^{-\alpha+2+3\epsilon}),$$
where $\mathcal T_+c$ is the $t_*\to+\infty$ tail of the forward part of $\sigma^jc(\sigma)$ (III.I$''''''''''$ Lemma
2.4 (b): a combination of $t_*^{-z-1}(\log t_*)^l$, $z = \alpha_0-3+j$ for s1 and $\alpha_0-2-\mu+j$ otherwise), and the
derivatives come from $(-i\sigma)^i\leftrightarrow\partial^i_{t_*}$, as $(\sigma+i0)^z\sigma^i = (\sigma+i0)^{z+i}$: the
tail of a tower piece is the tower $\sum_ia^{(i)}\breve h^i_\tau$ of $a := \mathcal T_+c$.

*Step 6 (the stationary terms and the rows).* $v$ has $K^+$-weight $w_v>0$, and every other term above decays
($\mathrm{Re}\,z+1>0$); so the stationary tensor $\dot g(\dot b_0)+h(iS_1)$ ($S_1$ sign-independent by Step 5) vanishes,
and $\dot b_0 = 0$, $S_1 = 0$ (III.H (3.1)), as in III.I$''''''''$ Lemma 3.2's Step 6. The towers: at level 1 ($j = 1$,
$2\le\mathrm{Re}\,\alpha_0<2+\eta_1$, $u$-exponent $\alpha_0$) the s1 tower has rate $\alpha_0-1$ and is the row
$(\mathrm s1,\alpha_0,\cdot)$; the s0 and s2 towers have rate $\alpha_0$, below $\alpha-2$ only for
$\mathrm{Re}\,\alpha_0 = 2$ by (G) (rows $(\mathrm s0,2,\cdot)$, $(\mathrm s2,2,\cdot)$); the c0, c1 towers have rate
$\alpha_0+d_\tau>2+\epsilon_K$ by (G); the v1 term and the rows outside $\mathcal T$ have rate $\ge\alpha_0+1$. At level
2 ($u$-exponent $\alpha_0+1$, $\mathrm{Re}\in[2+\eta_1,3+\eta_2)$) only the s1 tower has rate $\alpha_0<2+\epsilon_K$
possible, and by (G) then $\mathrm{Re}(\alpha_0+1)\le3$; the s0, s2 towers have rate
$\alpha_0+1\ge2+\eta_1>2+\epsilon_K$. So the towers of rate below $\alpha-2$ are those of the rows $\mathcal N_\sigma$,
with $(\lambda,k)\in\mathcal E_{\mathrm{par}}$ by III.I$''''''''''$ Lemma 1.2 (c). By III.I$''''''''''$ Lemma 2.1, each
such tower is $m_\nu(S_\nu)$ in $\{r\le R\}$ for large $t_*$, up to terms with $a^{(i)}$, $i\ge4$ (s1), $i\ge3$ (s0,
s2), of rate $\ge\mathrm{Re}\,e_\nu+3>\alpha-2$; and the towers of rate $\ge\alpha-2$ are
$O(t_*^{-\alpha+2+3\epsilon})$. Hence $v-\sum_{\nu\in\mathcal N_\sigma}m_\nu(S_\nu) = O(t_*^{-\alpha+2+3\epsilon})$ in
$\{r\le R\}$, with all $t_*\partial_{t_*}$ and spatial derivatives.

*Step 7 (joint weights).* The sum of the pieces other than the columns with constant coefficients lies in a space
$H^{\infty,(\frac32-3\epsilon,(E_{\mathrm{tf}},\beta'_+-1),((0,0)\bar\cup(E_K-1),\alpha-3-\epsilon))}_{\mathrm b}$ on
each half, with $E_K$ the $K^+$-exponents of Step 5 (the polyhomogeneous zf-terms of III.G$''''$ Proposition 4.4's $u$,
with coefficients polyhomogeneous at tf by III.G$''''$ Lemma 4.3 and (4.4), and the zero-energy pieces), and the
matching (4.4) of III.A Proposition 4.2 holds, by III.I$''''''''''$ Lemma 2.4 (a) applied to the zf-coefficients in
$\{r\le R\}$ for every $R$. III.A Proposition 4.2 (2) gives $v_{\mathrm{low}}$ (minus the stationary columns, which
vanish) in $H^{\infty,\frac32-4\epsilon,(E_\iota,\beta'_+),(E_K,\alpha-2-\epsilon)}_{\mathrm b}(M')$. Its
$K^+$-coefficients are functions on $K^+$ determined in $K^+\cap\{r\le R\}$ by Step 6, where they equal those of
$\sum_{\mathcal N_\sigma}m_\nu(S_\nu)$, which is itself partially polyhomogeneous at $K^+$ with these coefficients
(III.I$'''''''''$ Lemma 2.2 (b), (e), (2.1) there). So $v-\sum m_\nu(S_\nu)$ has $K^+$-weight $\alpha-2-\epsilon$. Its
$\iota^+$-weight is $\beta'_+$ ($v$ and the $m_\nu$ have it), and its $\mathscr I^+$-data are those of $v$: near
$\mathscr I^+$, $\chi_K = 0$, and III.I$'$ Proposition 2.1 applies as in III.I$''''''''$ Lemma 3.2's Step 8. *Linearity,
continuity:* every map used is linear and bounded (Lemmas 2.1-2.5, III.G$''''$ Propositions 4.4, 5.1, III.I$''$ Lemmas
4.1-4.3, III.A Proposition 4.2), and the $S_\nu$ are the coefficients of the tails. $\square$

**Lemma 3.2 (the expansion; [Hin26] Theorem 11.59, Parts 1-3, the extraction).** Let $\alpha>4$ be admissible, $\vec
p\in\mathcal P$ ($b = b_0$) and $h\in\mathcal X^\infty$ small, and $G\in\mathcal Y^0(\alpha)$. Suppose the forward
solution $u$ of $L_{h,\vec p}u = G$ lies in $\bigcap_\epsilon H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\beta'_+,w_0-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}$ with $w_0>0$, $w_0+a_K>\alpha$, and
$\beta'_+\in(\frac32-(\delta_\sharp-\epsilon_+),\frac32)$. Then
$$u = \sum_{\nu\in\mathcal N}m_\nu(S_\nu)+\tilde u,\qquad\tilde u\in\bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\beta_+,\alpha-2-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}\tag{3.2}$$
for every $\beta_+<\min(\frac32,\min\mathrm{Re}\,\mathcal E_+)$, with $S_\nu = S^{h,\vec p}_\nu(G)\in\mathcal
W_{\tau,\mathbb C}$ determined by $u$ (Corollary 2.3 of III.I$''''''''''$), conjugation-symmetric, linear and continuous
in $G$, with bounds uniform for $(h,\vec p)$ small.

*Proof.* *Step 0.* $f' := G-(L-L_{b_0})u$: by III.I Proposition 4.1 (4.2) (for $L = L_{h,\vec p}$, III.I$'''''''''$
Lemma 2.5), $(L-L_{b_0})u$ has the $\mathscr I^+$-data $(\langle\mathcal E^C_I+1\rangle',\ell_I+1)$, the plain
$\iota^+$-weight $\beta'_++2+\lambda_\sharp-\epsilon>w_+$ (as $\beta'_+>\frac32-\delta_\sharp+\epsilon_+$; $m_+ =
\lambda_\sharp$ by (H1)) and the $K^+$-weight $w_0-\epsilon+a_K\ge\alpha-\epsilon$. So $f'\in\mathcal Y^0(\alpha)$ for
$\epsilon<w_0+a_K-\alpha$ and $L_{b_0}u = f'$. *Steps 1-2.* III.I$''''''''''$ Proposition 3.1 gives $u_I$, $u_\iota$,
$(S_\nu)_{\mathcal N_\iota}$ and $f^\flat$; $v := u-u_I-u_\iota$ is the forward solution of $L_{b_0}v = f^\flat$ and has
$K^+$-weight $\min(w_0,\lambda_\sharp-1)-\epsilon>0$. *Step 3.* Proposition 3.1 gives $(S_\nu)_{\mathcal N_\sigma}$.
Summing gives (3.2) with $\iota^+$-weight $\min(\beta'_+,\lambda_\sharp)-\epsilon$; the weight $\beta_+$ for every
$\beta_+<\min(\frac32,\min\mathrm{Re}\,\mathcal E_+)$ follows as in III.I$''''''''$ Lemma 3.2 (the $\iota^+$-terms of
$\tilde u$ below $\frac32$ are those of $u$, by III.I$'''''$'s Step 1 with $\breve\ell_+<\frac32$). *Determination.* If
two such expansions hold, their difference is a sum of $m_\nu$ of $K^+$-weight $\alpha-2-\epsilon$, which is 0 by
III.I$''''''''''$ Corollary 2.3 ($\mathrm{Re}\,e_\nu\le2<\alpha-2$). *Reality:* $u$ real, $m_{\bar\nu}(\bar W) =
\overline{m_\nu(W)}$, and uniqueness. *Bounds:* every map is linear and bounded, uniformly by III.I$'''''''''$ Lemma
2.5. $\square$

**Lemma 3.3 (the coefficients near the base point).** In Lemma 3.2, if $(h_j,\vec p_j)\to(0,0)$, $G_j\to G$ in $\mathcal
Y^0(\alpha)$, and the forward solutions $u_j$ of $L_{h_j,\vec p_j}u_j = G_j$ and $u$ of $L_{b_0}u = G$ satisfy the
hypothesis with the same $w_0$, $\beta'_+$, $u_j$ bounded there, then $S^{h_j,\vec p_j}_\nu(G_j)\to S^{0,0}_\nu(G)$.

*Proof.* As III.I$''''''''$ Lemma 3.3: $u_j-u$ is the forward solution of $L_{b_0}(u_j-u) = R_j :=
G_j-G-(L_j-L_{b_0})u_j\to0$ in $\mathcal Y^0(\alpha)$ (Step 0's count, coefficients $o(1)$), and the coefficients are
linear: $S^{h_j,\vec p_j}_\nu(G_j)-S^{0,0}_\nu(G) = S^{0,0}_\nu(R_j)\to0$. $\square$

## 4. Elimination ([Hin26] Theorem 11.59, Step 2.B and Part 3, (11.222), at n = 4)

For an admissible $\alpha'\in(2,3)$ (III.I$''''''''$), $\mathcal P_{\alpha'}$ is III.I$''''''''$'s space (the parameters
$\vec p_{\le0}$ and the motions of $K^+$-rate below $\alpha'-2$), and $\mathcal N' := \mathcal N\setminus\{(\mathrm
s1,\lambda,k):(\lambda,k)\in\mathcal M_{\alpha'}\}$, the rows of III.I$'''''''''$ not in $\mathcal P_{\alpha'}$. For
$\vec W = (W_\nu)_{\nu\in\mathcal N'}$, conjugation-symmetric, write $D_{\vec p}P_4(h,\vec p)(\vec W) :=
\sum_{\nu\in\mathcal N'}f^\nu_{h,\vec p}(W_\nu)$, and $\mathcal P^{\mathrm{full}}$ for $\mathcal P_{\alpha'}\oplus\{\vec
W\}$, which is $\mathcal P$ of III.I$'''''''''$.

**Theorem 4.1 ([Hin26] Theorem 11.59, Parts 1-3, at n = 4: (11.222)).** Let $\alpha>4$ be admissible, and $\vec
p\in\mathcal P$ ($b = b_0$) and $h\in\mathcal X^\infty$ small. For every $F\in\mathcal Y^0(\alpha)$ there is a unique
$\vec p\,' = \vec p\,'_{h,\vec p}(F)\in\mathcal P$ such that the forward solution of
$$L_{h,\vec p}u = F-D_{\vec p}P_4(h,\vec p)(\vec p\,')\tag{4.1}$$
satisfies
$$u\in\bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta_+,\alpha-2-\epsilon}_{\mathrm
b}(\Omega_*;S^2T^*)^{\bullet,-}\quad\text{for every }\beta_+<\min(\tfrac32,\min\mathrm{Re}\,\mathcal E_+).\tag{4.2}$$
Moreover $\vec p\,'_{h,\vec p}$ is linear with bounds uniform for $(h,\vec p)$ small, and continuous at $(0,0)$ as in
III.I$''''''''$ Proposition 4.1 (ii). In compact spatial sets $u = O(t_*^{-2-\epsilon_K+\epsilon'+\epsilon})$: for
$\epsilon'\to0$ along admissible values, the source's (11.222) at $K^+$, with the plain $\iota^+$-weight $\beta_+$; its
$\iota^+$-index set $(\tilde{\mathcal E}_\sharp,3+\epsilon_+)$ is part of Part 4, in the next part.

*Proof.* Fix an admissible $\alpha'\in(2,3)$. III.I$''''''''$ (4.2) holds for every $\beta_+<\frac32$, so $\beta'_+$ can
be taken in $(\frac32-(\delta_\sharp-\epsilon_+),\frac32)$, and $w_0 := \min(\alpha'-2,\lambda_\sharp-1)$ satisfies
$w_0+a_K>\alpha$ ($a_K\ge4+\epsilon_K$, (H2), and $w_0>0$).

*III.I$''''''''$ Proposition 4.1 for $P_4$.* That proposition is stated for $P_3$ at $(h,\vec p_3)$. For $\vec
p\in\mathcal P$ with row components $(W_\nu)_{\nu\notin\mathcal M}$ put $h' := h+\sum_{\nu\notin\mathcal
M}h_\nu(W_\nu)$, in $\mathcal X^\infty$ and small (III.I$'''''''''$ Lemma 2.5); then $L_{h,\vec p}$ is $P_3$'s
linearised operator at $(h',\vec p_3)$ (III.I$'''''''''$ Lemma 2.5), and in the directions $S$, $b$, $S^{(0)}_1$ the
derivatives $D_{\vec p}P_4(h,\vec p)$ and $D_{\vec p}P_3(h',\vec p_3)$ differ by
$(\partial\delta^*_{g_0,E_C})\vartheta_{\mathrm{rows}}$ (III.I$'''''''''$ Lemma 2.6 (a)), which is linear in the
direction, lies in $\mathcal Y_2(\alpha)\subset\mathcal Y(\alpha')$ and is $O(|\vec W|)$; in the motion directions they
agree. So the finite-dimensional maps of III.I$''''''''$'s base and induction steps stay within $O(|\vec W|)$ of $\pm$
the identity, and its Proposition 4.1, with (i)-(ii), holds for $(L_{h,\vec p},D_{\vec p}P_4)$ at $\vec p$ small; this
is the form used below.

*The map.* For $\vec W$ put $F(\vec W) := F-D_{\vec p}P_4(h,\vec p)(\vec W)$; by III.I$'''''''''$ Lemma 2.6 (b) it lies
in III.I$''''''''$'s $\mathcal Y(\alpha')$, so III.I$''''''''$ Proposition 4.1 gives $\vec q(\vec W) := \vec
p\,'_{h,\vec p,\alpha'}(F(\vec W))\in\mathcal P_{\alpha'}$, and the forward solution $u(\vec W)$ of
$$L_{h,\vec p}u(\vec W) = F(\vec W)-D_{\vec p}P_4(h,\vec p)(\vec q(\vec W))$$
lies in III.I$''''''''$ (4.2) at $\alpha'$. Write $D_{\vec p}P_4(\vec q) = f^S(q_S)+f^b(q_b)+f^{\mathrm s1}(q_{\mathrm
s1})+\sum_{\nu\in\mathcal M_{\alpha'}}f^\nu(q_\nu)$, and use III.I$'''''''''$ Lemma 2.6 (c), $f^\nu = L_{h,\vec
p}m_\nu+r^\nu$, for every row: then $u(\vec W) = u_0(\vec W)-\sum_{\nu\in\mathcal N'}m_\nu(W_\nu)-\sum_{\nu\in\mathcal
M_{\alpha'}}m_\nu(q_\nu(\vec W))$, where $u_0(\vec W)$ is the forward solution of $L_{h,\vec p}u_0 = G(\vec W)$,
$$G(\vec W) := F-\sum_{\nu\in\mathcal N'}r^\nu(W_\nu)-f^S(q_S)-f^b(q_b)-f^{\mathrm s1}(q_{\mathrm
s1})-\sum_{\nu\in\mathcal M_{\alpha'}}r^\nu(q_\nu)\in\mathcal Y^0(\alpha)$$
(III.I$''''''''''$ section 1: $r^\nu\in\mathcal Y_2(\alpha)$ without index set, $f^S,f^{\mathrm s1}\in\mathcal
Y^0(\alpha)$, $f^b\in\mathcal Y^0_2(\alpha)$). $u_0(\vec W) = u(\vec W)+\sum m_\nu$ has $K^+$-weight
$\min(\alpha'-2,\lambda_\sharp-1)-\epsilon>0$ and the other properties of Lemma 3.2's hypothesis (the $m_\nu$ have
$\iota^+$-weight $\lambda_\sharp>\frac32$). By Lemma 3.2,
$$u(\vec W) = \sum_{\nu\in\mathcal N}m_\nu\big(C_\nu(\vec W)\big)+\tilde u,\qquad C_\nu(\vec W) := S^{h,\vec
p}_\nu(G(\vec W))-W_\nu\ (\nu\in\mathcal N'),\quad S^{h,\vec p}_\nu(G(\vec W))-q_\nu(\vec W)\ (\nu\in\mathcal
M_{\alpha'}).$$
As $u(\vec W)$ lies in III.I$''''''''$ (4.2) at $\alpha'$, the coefficients $C_\nu(\vec W)$, $\nu\in\mathcal
M_{\alpha'}$, vanish by III.I$''''''''''$ Corollary 2.3: the rows of $K^+$-rate below $\alpha'-2$ are exactly those of
$\mathcal M_{\alpha'}$ (the s0, s2, c0, c1 rows have rates $\ge\lambda_\sharp>1>\alpha'-2$, every s1 row of rate above
$\alpha'-2$ is in $\mathcal N'$, and none has rate $\alpha'-2$, by III.I$''''''''$'s admissibility), so
$\sum_{\nu\in\mathcal M_{\alpha'}}m_\nu(C_\nu(\vec W))$, the difference of $u(\vec W)$ and terms of $K^+$-weight above
$\alpha'-2$, has $K^+$-weight $\alpha'-2-\epsilon$. So $u(\vec W)$ satisfies (4.2) at $\alpha$ iff $C_\nu(\vec W) = 0$
for $\nu\in\mathcal N'$ (by III.I$''''''''''$ Corollary 2.3 again, all rates being $\le2<\alpha-2$; $\tilde u$ and the
$m_\nu$ have the $\iota^+$- and $\mathscr I^+$-data of (4.2)).

*At $(0,0)$.* $r^\nu = 0$, and $\vec q(\vec W)$ does not depend on $\vec W$: $F(\vec W) = F-\sum L_{b_0}m_\nu(W_\nu)$,
and the forward solution $m_\nu(W_\nu)$ of $L_{b_0}m = L_{b_0}m_\nu(W_\nu)$ lies in III.I$''''''''$ (4.2) at $\alpha'$
for $\nu\in\mathcal N'$ (rate $\ge\alpha'-2$ and $\ne\alpha'-2$ by admissibility; III.I$'''''''''$ Lemma 2.2), so $\vec
p\,'_{0,0,\alpha'}(L_{b_0}m_\nu(W_\nu)) = 0$ by uniqueness at $\alpha'$. Hence $G(\vec W) = G(0)$ and $C(\vec W) =
C(0)-\vec W$ on $\mathcal N'$: the equation has the unique solution $\vec W = S^{0,0}(G(0))$.

*Near $(0,0)$.* $C(\vec W) = C(0)-T_{h,\vec p}\vec W$ with $T_{h,\vec p}\vec W := \vec W-S^{h,\vec p}(G(\vec W)-G(0))$,
linear on the finite-dimensional space of $\vec W$. $G(\vec W)-G(0) = -\sum r^\nu(W_\nu)-(\text{the }\vec q\text{-terms
of }\vec q(\vec W)-\vec q(0))$; the first is $O(|\vec W|(\|h\|+|\vec p|))$ in $\mathcal Y_2(\alpha)$ (III.I$'''''''''$
(2.5)), and $\vec q(\vec W)-\vec q(0) = -\vec p\,'_{h,\vec p,\alpha'}(D_{\vec p}P_4(h,\vec p)(\vec W))$ tends to $-\vec
p\,'_{0,0,\alpha'}(\sum L_{b_0}m_\nu(W_\nu)) = 0$ as $(h,\vec p)\to(0,0)$, for fixed $\vec W$ (III.I$''''''''$
Proposition 4.1 (ii), with III.I$'''''''''$ Lemma 2.6 (b)-(d) for the convergence of the sources in $\mathcal
Y(\alpha')$). With the uniform bounds of Lemma 3.2 and of III.I$''''''''$ Proposition 4.1 (i), $T_{h,\vec
p}\to\mathrm{id}$, so $T_{h,\vec p}$ is invertible for $(h,\vec p)$ small; put $\vec W := T_{h,\vec p}^{-1}C(0)$ and
$\vec p\,' := \vec q(\vec W)\oplus\vec W$. Conjugation symmetry is preserved, as $L$, $F$ are real and $T$ commutes with
the conjugation of III.I$'''''''''$ section 1.

*Uniqueness.* If $\vec p\,''$ also gives (4.2) at $\alpha$, its solution lies in III.I$''''''''$ (4.2) at $\alpha'$, so
its $\mathcal P_{\alpha'}$-part is $\vec q(\vec W'')$ by uniqueness at $\alpha'$ (III.I$''''''''$ Proposition 4.1),
where $\vec W''$ is its $\mathcal N'$-part; then $C(\vec W'') = 0$, so $\vec W'' = \vec W$. *Linearity, bounds,
continuity:* by construction, from those of III.I$''''''''$ Proposition 4.1, Lemma 3.2 and $T^{-1}_{h,\vec p}$;
continuity at $(0,0)$ as in III.I$''''''''$ Proposition 4.1 (ii), with Lemma 3.3. $\square$

The source's statement (11.222) also records the $\iota^+$-index set $(\tilde{\mathcal E}_\sharp,3+\epsilon_+)$ of $u$;
at $n = 4$ it follows from the same construction by recording the $\iota^+$-terms of the pieces (III.A Proposition 4.2
(2) with the tf-index sets), and it enters only Part 4 and section 11.8.3, which the next part writes out.

## 5. Findings, labels and sources

(I$'''''''''''$1) *Four Taylor levels, made explicit.* The order $\alpha_K = 4+\epsilon_K$ needs four zero-energy
solves, the source's 2.A.3, 2.A.5, 2.A.7 and one at $\sigma^3$ ($\alpha-1>3$), which its Part 3 (5) leaves implicit (at
$n = 3$ as well). The tf-model is used at levels 1 and 2 in its polyhomogeneous form (III.G$''''$ Proposition 4.4) and
at level 3 in its conormal form (Proposition 5.1); the outputs of level 3 lie above the order $\alpha-2$ because
$\eta_2>\epsilon_K$.

(I$'''''''''''$2) *The physical decomposition* (Lemma 2.5) replaces the source's combination (11.217) and the assemblies
III.I$''''''$ (2.8), III.I$''''''''$ (3.3): the augmented system is inverted only at zero energy and at the last level,
and the rows never need to be corrected.

(I$'''''''''''$3) *The mass produces boost rows.* The root 2 of $\widehat{L_{b_0}}(0)$ (the mass) gives $\hat u_0$ a
$\rho^2$-term, hence a tf-exponent 2 at level 2 through $L_1$ and the level-1 columns, and III.G$''''$ Proposition 4.4
at $\alpha_0 = 2$ turns it into the boost row at $\lambda = 3$, rate 2; this is why $3\in\Lambda$ (III.I$''''''''''$
Definition 1.1). The source's analogue is the $t^{-2}_*$-term of its Part 3 (5).

(I$'''''''''''$4) *No logarithmic s0 row at the $\dot g$-columns.* At $n = 4$, $\hat g^{\mathrm{aug}}$ is exactly
$i\sigma^{-1}\Psi\dot g$ (III.H Lemma 2.5), without the source's $\log\hat r$-term (its Part 3 (5)); the $\dot
g$-columns contribute only stationary or compactly supported terms (Lemma 2.4), and the s0 rows at $\lambda = 2$ come
from the tf-model alone.

(I$'''''''''''$5) *Elimination.* With the exact linearisation, the coefficient map is the identity at $(0,0)$ (the
source's Step 2.B has $\pm$ the identity), and one step from an admissible $\alpha'\in(2,3)$ reaches $\alpha$, as
$a_K-2\ge2+\epsilon_K$.

(I$'''''''''''$6) *Deferred.* The $\iota^+$-polyhomogeneity of $u$ in (11.222) and Part 4 (the expansion modulo
$K^+$-order $4+\epsilon_K$, (11.196)) are the next part.

(I$'''''''''''$7) *The column terms are polyhomogeneous at tf* (Lemma 1.1; D274). III.H Lemma 2.4 and III.I$''''''$
Lemma 1.1 (b) give the column terms at tf only conormally (weight $3-\epsilon$); the cascade needs their tf-expansion up
to the level-2 order $2+\eta_2$, which a conormal remainder of weight 3 at level 0 would cap at 2 after two divisions by
$\sigma$. At $b_0$ the cut-off $\chi_c(r/t_*)$, the operator and the states $\dot g$, $h$, $\breve h$ are
polyhomogeneous, and so are the columns; their exponents $2+\mathcal E_{\mathrm{col}}$ join $\Lambda$ (III.I$''''''''''$
Definition 1.1).

*Labels.* Lemmas 1.1 and 2.1-2.5 are new at $n = 4$; Proposition 3.1 and Lemma 3.2 are the source's Steps 2.A.3-2.A.8
and Part 3 at $n = 4$; Theorem 4.1 is (11.222) at $K^+$.

*Sources.* [Hin26] pp. 278-289 (Theorem 11.59 and its proof, Parts 1-3), read at source. Inputs: II.G$'$ (2.26a); III.A
Proposition 4.2, Lemma 1.4; III.F$'$ Proposition 2.3; III.F$''''$ Proposition 5.1's proof; III.G$''$ Table 1.1,
Definition 2.5; III.G$''''$ (3.2), Definitions 2.3, 4.1, Lemma 4.3, Propositions 4.4, 5.1; III.H (1.2), (2.3), section
2, Lemmas 2.3-2.5, Proposition 3.2, (3.1); III.D$'''$ Proposition 3.1 (2); III.F$'''$ Propositions 2.2, 4.1; III.I
Proposition 4.1; III.I$'$ Proposition 2.1; III.I$''$ Lemmas 4.1-4.3; III.I$'''$ Lemma 1.1; III.I$'''''$ Proposition 2.1;
III.I$''''''$ Lemmas 1.1-1.2, Steps 3.1, 5; III.I$''''''''$ Lemmas 3.2-3.3, Proposition 4.1; III.I$'''''''''$ Lemmas
2.2, 2.5, 2.6; III.I$''''''''''$.
