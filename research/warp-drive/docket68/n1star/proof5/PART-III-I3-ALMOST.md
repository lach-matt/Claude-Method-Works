# Part III.I$''$. Almost linear bounds, n = 4 ([Hin26] section 11.3)

*Status.* Verified (D258: the hundred-and-eighth verifier; no major finding, three minor ones and nine nits seated, to
be read). Written (D255). This part proves, at spatial dimension $n = 4$, [Hin26] section 11.3 (pp. 231-238): the
improvement of the forward solutions of $L^{g,g_0}u = f$ at $\iota^+$ and $K^+$ for sources with more decay there
(Proposition 11.17), with the two integration lemmas it rests on (Lemmas 11.18 and 11.19).

*What n = 4 changes.* The scheme is the source's: the forward solution of Theorem 11.12 is improved by rewriting
$L_bu = f-(L^{g,g_0}-L_b)u$, solving away the null infinity terms (Proposition 11.16), splitting $L_b^{-1}$ by the
Fourier transform in $t_*$ into high, regular low and singular low frequencies, integrating the singular part twice in
$t_*$, and recovering the null infinity expansion (Proposition 11.14). At $n = 4$ the cut-off zero energy states of
III.H have Fourier transforms that decay rapidly at scf and lie one order deeper at tf (Lemma 4.3), so the singular part
does not limit the decay at $\iota^+$: the forward solutions keep the $\iota^+$-weight $\min(\alpha_+,\frac32,\min
\mathrm{Re}\,\mathcal E_+)-\epsilon$ for every $K^+$-weight $\alpha_K-2$, $\alpha_K\in[\frac12,1)$, where the source's
is $\alpha_K-\epsilon$ (Proposition 5.1). The cap $\frac32$ is the transport from $\mathscr I^+$, the source's 1 (its
$\tilde\alpha_+\le\alpha_+<1$, p. 232; "limited by 1 due to transport from $\mathscr I^+$", p. 238). The bookkeeping
window of the iteration is $(0,1)$, III.H (1.1)'s window inside the gap of $\widehat{L_b}(0)$ (III.F$'$ Proposition 2.3
(a)), where the source's is $(0,\epsilon_{\mathrm{ind}})$. As in III.I Theorem 5.3, everything is at $b = b_0$ ((I3) of
III.I). Notation: Parts II.G$'$, III.A, III.C, III.H, III.H$'$, III.I and III.I$'$; no instrument is used.

## 1. Setting

*The manifold.* $X = \{r\ge r_0\}$ as in III.H section 1 and $M' := [\overline{\mathbb R}_{t_*}\times\bar X;\{\pm\infty\}
\times\partial\bar X]$, II.G$'$ section 3.1's $M$ over $\bar X$ (its Remark 3.7; III.A section 4 at $n = 4$), with
faces $I$ (the lift of $\overline{\mathbb R}\times\partial\bar X$; its part in $t_*>0$ is the source's $\mathscr I^+$),
$\iota = \iota^+\cup\iota^-$ (the front faces) and $K = K^+\cup K^-$ (the lifts of $\{\pm\infty\}\times\bar X$), and the
artificial boundary $\{r = r_0\}$, at which all spaces are extendible. $H^{k,\beta_I,\beta_\iota,\beta_K}_{\mathrm
b}(M')$, with index sets where written, are the spaces of III.A section 4 for the b-density
$|\frac{dt_*}{\langle t_*\rangle}|\mu_{\mathrm b}$, $\mu_{\mathrm b} = |dx|/\langle x\rangle^4$; on $\Omega_*$ they are
III.I's spaces (II.G$'$ Corollary 4.5, last paragraph). Put $\Omega_- := \mathrm{cl}_{M'}\{t_*\le1\}$ and, for $C>0$,
$\Omega_< := \mathrm{cl}_{M'}\{t_*\le-Cr\}$, with $\bar H$ for restrictions. $X^\pm_{\mathrm{sc}\text-\mathrm b}$ and its
spaces, with faces scf, tf, zf and weights listed in that order, are III.A section 4's (II.G$'$ (3.2)).

*Coordinates.* With $r = |x|$:

(a) near $I\cap\iota^+$, on $\{t_*>0\}$: $\rho_I := t_*/r$, $\rho_+ := 1/t_*$ (the source's (3.4e)), and
$t_*\partial_{t_*} = \rho_I\partial_{\rho_I}-\rho_+\partial_{\rho_+}$;

(b) near $\iota^+\cap K^+$: $\rho_+ := 1/r$, $\rho_K := r/t_*$ (the source's (3.4g)), and near all of $K^+$, $\rho_K :=
\langle x\rangle/t_*$ with $x\in\bar X$; in both, $t_*\partial_{t_*} = -\rho_K\partial_{\rho_K}$ at fixed $x$;

(c) near $I\cap\iota^-$, on $\{t_*<2\}$: $\rho_0 := (2-t_*)^{-1}$, $\rho_I := (2-t_*)/r$, and $(2-t_*)\partial_{t_*} =
\rho_0\partial_{\rho_0}-\rho_I\partial_{\rho_I}$.

(Direct computation: in (a), $t_*\partial_{t_*}\rho_I = \rho_I$, $t_*\partial_{t_*}\rho_+ = -\rho_+$; in (c),
$\partial_{t_*}\rho_0 = \rho_0^2$ and $\partial_{t_*}\rho_I = -1/r$.) The source's chart (3.4c) uses $t_*+2$, whose
field $-(t_*+2)\partial_{t_*}$ vanishes at $t_* = -2$; (c) covers $\{t_*<2\}$ in one chart. In all three,
$\partial_{t_*}\in\rho_\iota\rho_K\mathcal V_{\mathrm b}(M')$ ($\rho_\iota$, $\rho_K$ defining functions of $\iota$,
$K$), so $\partial_{t_*}$ raises the $\iota$- and $K$-weights by 1 and keeps the $I$-weight.

*The operator.* $L_b := L_{b_0}$; $g_0 := g_{b_0,b_0,-S}$, $g := g_0+h$, $L := L^{g,g_0}$, with $|S|<\epsilon_0$ and
$h\in\mathcal X^\infty$ (III.I (1.4)), $\|h\|_{\mathcal X^d}<\epsilon_0$, $\epsilon_0$ and $d$ those of III.I Theorem
5.3. $\widehat{L_b}(\sigma)$ is invertible for real $\sigma\ne0$ (III.H Corollary 4.4), and $\tilde L_b(\sigma)$, the
augmented operator of III.H Definition 3.1, for $0<|\sigma|\le c_k$ (III.H Corollary 4.2). $\ell_I^{\max}$ is III.I$'$
(1.1) and $\sigma_\Upsilon$ III.I$'$ section 1.

*The gap.* By III.F$'$ Proposition 2.3 (a) (no indicial root has real part in $(0,1]$),
$(0,1)$ lies in the indicial gap of $\widehat{L_b}(0)$ for $\mu_{\mathrm b}$; III.H (1.1) takes its weight $\alpha$ with
$\alpha+2\in(0,1)$, and so does this part.

## 2. Integration of $\partial_{t_*}$ ([Hin26] Lemma 11.18 at n = 4)

**Lemma 2.1 ([Hin26] Lemma 11.18 at n = 4).** Let $k\in\mathbb N_0$, $\beta_I,\beta_\iota,\beta_K\in\mathbb R$ with
$\beta_K\ne0$, $\mathcal E_K$ an index set, and $C>0$.

(1) (*From $t_* = 1$.*) If $u|_{\Omega_-}\in\bar H^{k,\beta_I,\beta_\iota,(\mathcal E_K,\beta_K)}_{\mathrm b}(\Omega_-)$
and $\partial_{t_*}u\in H^{k,\beta_I,\beta_\iota+1,(\mathcal E_K+1,\beta_K+1)}_{\mathrm b}(M')$, then for every
$\epsilon>0$
$$u\in H^{k,\beta_I,\min(\beta_\iota,\beta_I-\epsilon),(\mathcal E_K\bar\cup\{(0,0)\},\beta_K)}_{\mathrm
b}(M').\tag{2.1}$$

(2) (*From $t_* = -Cr$.*) If $u|_{\Omega_<}\in\bar H^{k,\infty,\beta_\iota,\beta_K}_{\mathrm b}(\Omega_<)$ and
$(\partial_{t_*}u)|_{\Omega_-}\in\bar H^{k,\beta_I,\beta_\iota+1,\beta_K+1}_{\mathrm b}(\Omega_-)$, then for every
$\epsilon>0$
$$u|_{\Omega_-}\in\bar H^{k,\min(\beta_I,\beta_\iota-\epsilon),\beta_\iota,\beta_K}_{\mathrm b}(\Omega_-),\tag{2.2}$$
and likewise with $(\mathcal E_K,\beta_K)$, $(\mathcal E_K+1,\beta_K+1)$ for $\beta_K$, $\beta_K+1$.

As $\Omega_<\cap I = \emptyset$, the first weight on $\Omega_<$ is immaterial; the $K^-$-weight in (2.2) is the a priori
one, (2.2)'s content being the $I$-weight.

*Proof.* (1) *Near $I\cap\iota^+$.* In the chart (a), with $x := \rho_I/C'$ and $y := \rho_+/2$ for a large $C'$, so
that $\{y\ge\frac12\} = \{t_*\le1\}$ and $\{x<2\}$ covers $\{t_*<2C'r\}$, the hypotheses read $(x\partial_x-y\partial_y)u
= t_*\partial_{t_*}u\in H^{k,\beta_I,\beta_\iota}_{\mathrm b}$ (as $t_* = \rho_+^{-1}$ is a defining function of
$\iota^+$ to the power $-1$ there) and $u\in H^{k,\beta_I}_{\mathrm b}$ on $\{y\ge\frac12\}$. III.A Lemma 3.2 with $z =
0$, $E = F = \emptyset$, $\alpha := \beta_I$ and the target weight $\beta := \beta_\iota' := \min(\beta_\iota,\beta_I-
\epsilon)$ (so $\alpha>\beta$ and $f\in H^{k,\alpha,\beta}_{\mathrm b}$) gives $u\in H^{k,\beta_I,\beta'_\iota}_{\mathrm
b}$ there. (The flow of $x\partial_x-y\partial_y$ preserves $xy$ and increases $x$ as $y$ decreases, so the value at a
point depends on the data at smaller $x$ only; the end $x = 2$ plays no role. Where the square $[0,2)^2$ of the chart
meets $\{r<r_0\}$, $u$ is first extended across $\{r = r_0\}$ by II.G$'$ Remark 3.7's Seeley extension, which acts in
the spatial variable and commutes with $\partial_{t_*}$; the characteristics being the sets $\{r = \mathrm{const}\}$,
nothing propagates across $\{r = r_0\}$.) This holds on every set $\{t_*\le C'r\}$, that is, off any neighbourhood of
$K^+$. *Near $K^+$.* In the chart (b) with $\rho_K = \langle x\rangle/t_*$ and $x\in\bar X$, $\rho_K\partial_{\rho_K}u =
-t_*\partial_{t_*}u\in H^{k,(\mathcal E_K,\beta_K),\beta_\iota}_{\mathrm b}$ ($t_* = \langle x\rangle\rho_K^{-1}$), and
on $\{\rho_K\ge\frac12\}$, a set of the previous kind, $u$ has the $\iota^+$-weight $\beta_\iota'\le\beta_\iota$. III.A
Lemma 1.2 with $z = 0$ ($\beta_K\ne0$), $H := \bar X$ (the $\iota^+$-face $\partial\bar X$ carrying the weight
$\beta'_\iota$; its solution operators act in $\rho_K$ alone and commute with the extension at $\{r = r_0\}$) gives
$u\in H^{k,(\mathcal E_K\bar\cup\{(0,0)\},\beta_K),\beta'_\iota} _{\mathrm b}$ near $K^+$. Away from $I\cup\iota^+\cup
K^+$ in $t_*\ge1$ the set is compact, and $u(t_*) = u(1)+\int_1^{t_*}
\partial_{t_*}u$ gives $H^k$ there. With the hypothesis on $\Omega_-$ this is (2.1).

(2) $\Omega_-\setminus\Omega_<$ is covered by the chart (c) on $\{r\ge R\}$, where $\rho_I\le C+2/R$, and by the compact
set $\{r\le R,\ -CR\le t_*\le1\}$, on which $u(t_*) = u(-CR)+\int_{-CR}^{t_*}\partial_{t_*}u$ gives the claim. In the
chart (c), with $x := \rho_0$ and $y := \rho_I/C''$, $C''>2C$, $\{y\ge\frac12\}\cap\{r\ge R\}\subset
\Omega_<$ for $R$ large, and $(x\partial_x-y\partial_y)u = (2-t_*)\partial_{t_*}u\in H^{k,\beta_\iota,\beta_I}_{\mathrm
b}$ ($2-t_* = \rho_0^{-1}$, a defining function of $\iota^-$ to the power $-1$); III.A Lemma 3.2 with $z = 0$,
$E = F = \emptyset$, $\alpha := \beta_\iota$ and the target weight $\min(\beta_I,\beta_\iota-\epsilon)<\alpha$ at $y = 0$
gives (2.2) near $I$ (applied to $\psi(r)u$, $\psi = 1$ on $[R,\infty)$ and $0$ on $[0,\frac R2]$, so that the square of
the chart meets only $\{r\ge\frac R2\}$; $\psi(r)$ commutes with $\partial_{t_*}$ and changes nothing on $\{r\ge R\}$).
The $K^-$-weight: near $K^-$, $\Omega_-$ lies in $\Omega_<$ for every constant. Index sets at $K$ pass through
unchanged. $\square$

## 3. Integration with a moment condition ([Hin26] Lemma 11.19 at n = 4)

**Lemma 3.1 ([Hin26] Lemma 11.19 at n = 4).** Let $\Omega_< := \mathrm{cl}_{M'}\{t_*<-r\}$ and $\beta_I,\beta_\iota,
\beta_K\in\mathbb R$ with $\beta_\iota>\beta_I$, $\beta_K\le\beta_\iota-\beta_I$ and $\beta_K\in(-1,1)\setminus\{0\}$.
Suppose $u|_{\Omega_<}\in\bar H^{k,\infty,\beta_\iota,\beta_K}_{\mathrm b}(\Omega_<)$, $\mathcal Fu$ is supported in
$[-c_0,c_0]\times X$ for some $c_0<\frac12$, and
$$\mathcal F(\partial_{t_*}u)|_{\pm(0,1]}\in H^{k+\ell,(\beta_I,\beta_\iota,((0,0),\beta_K))}_{\mathrm b}
(X^\pm_{\mathrm{sc}\text-\mathrm b}),\tag{3.1}$$
with $\ell$ a $k$-independent integer depending on the weights, the restrictions to zf of the two signs agreeing when
$\beta_K>0$. Then $u\in H^{k,\beta_I,\beta_\iota-\epsilon,((0,0),\beta_K)}_{\mathrm b}(M')$ for every $\epsilon>0$.

The source states $\beta_K<1$, $\beta_K\ne0$; $\beta_K>-1$ is needed for (2.26a) below, whose $K$-weight $\beta_K+1$ must
lie in $(0,\infty)\setminus\mathbb N$ (II.G$'$ Proposition 3.5), and is implicit there. By (2.26a) alone (3.1) gives
$\partial_{t_*}u$ the $I$-weight $\beta_I-\epsilon$, and Lemma 2.1 would then give $u$ the $\iota$-weight $\beta_I-
2\epsilon$ only; the moment condition (3.4) below is what gives $\beta_\iota-\epsilon$. The source asks $\mathcal Fu$
supported in $[-1,1]\times X$; its proof treats $f_2$ by (2.26a), whose cut-off (II.G$'$ Proposition 3.5 (1)) is 1 only
near $[-\frac12,\frac12]$, and $f_1$ by II.G$'$ Definition 2.7, which asks regularity across $\sigma = \pm1$, where
$\mathcal Ff$ may jump. Support in $[-c_0,c_0]$, $c_0<\frac12$, meets both ((I$''$5)), and the application in section 5
has it.

*Proof.* Let $\chi = \chi(t_*/r)$ equal 0 on $(-\infty,-3]$ and 1 on $[-2,\infty)$, and $f := \partial_{t_*}u$. As
$\partial_{t_*}\chi = r^{-1}\chi'(t_*/r)$ is supported in $\{-3r\le t_*\le-2r\}\subset\Omega_<$, away from $I$ and $K$,
$$\partial_{t_*}(\chi u) = f'+\chi f,\qquad f' := (\partial_{t_*}\chi)u\in H^{k,\infty,\beta_\iota+1,\infty}_{\mathrm
b}(M').\tag{3.2}$$
Let $\chi_{\mathrm{scf}}\in C^\infty_c([0,2))$ equal 1 on $[0,1]$, regarded as $\chi_{\mathrm{scf}}(\rho/|\sigma|)$ on
$X^\pm_{\mathrm{sc}\text-\mathrm b}$, $\rho = \langle x\rangle^{-1}$ (1 near scf, 0 near zf), and $f_1 := \mathcal
F^{-1}(\chi_{\mathrm{scf}}\mathcal Ff)$, $f_2 := \mathcal F^{-1}((1-\chi_{\mathrm{scf}})\mathcal Ff)$. Since
$(1-\chi_{\mathrm{scf}})\mathcal Ff\in H^{k+\ell,(\infty,\beta_\iota,((0,0),\beta_K))}_{\mathrm b}$ (it vanishes near
scf), (2.26a) (II.G$'$ Proposition 3.5 (1), with $K$-weight $\beta_K+1\in(0,2)\setminus\{1\}$; for $\ell$ large) gives
$$f_2,\ \chi f_2\in H^{k,\beta_\iota+1-\epsilon,\beta_\iota+1,\beta_K+1}_{\mathrm b}(M'),\tag{3.3}$$
$\chi$ being bounded and conormal on $M'$. As $\chi u = 0$ for $t_*\le-3r$, $\chi u = F'+F_1+F_2$ with $F' :=
\int_{-\infty}^{t_*}f'$, $F_j := \int_{-\infty}^{t_*}\chi f_j$.

*$F'$ and $F_2$.* $F'$ vanishes for $t_*\le-3r$; by Lemma 2.1 (2) with $C = 3$ and (3.2), $F'|_{\Omega_-}\in\bar H^{k,
\beta_\iota-\epsilon,\beta_\iota,\infty}_{\mathrm b}$, and Lemma 2.1 (1) (with $K$-weight a large non-zero number)
gives $F'\in H^{k,\beta_\iota-\epsilon,\beta_\iota-2\epsilon,(0,0)}_{\mathrm b}(M')$. Likewise, by (3.3),
$F_2|_{\Omega_-}
\in\bar H^{k,\beta_\iota-\epsilon,\beta_\iota,\infty}_{\mathrm b}$ and $F_2\in H^{k,\beta_\iota-\epsilon,\beta_\iota-
2\epsilon,((0,0),\beta_K)}_{\mathrm b}(M')$ ($\beta_K\ne0$).

*$F_1$.* As $\chi_{\mathrm{scf}}$ vanishes near zf, $\mathcal Ff_1 = \chi_{\mathrm{scf}}\mathcal Ff\in H^{k+\ell,
(\beta_I,\beta_\iota,\infty)}_{\mathrm b}$; on its support, near tf$\cap$scf, $\rho_{\mathrm{scf}} = \rho/|\sigma|$ and
$\rho_{\mathrm{tf}} = |\sigma|$ (III.A Lemma 4.1's proof), and near scf$^\circ$ $\rho_{\mathrm{scf}}\sim\rho$, so with
$\gamma := \beta_\iota-\beta_I$ if this is not an integer, and $\gamma := \beta_\iota-\beta_I-\epsilon'$ with
$0<\epsilon'<\min(\epsilon,1-\beta_K)$ if it is (then it is at least 1), so that $\gamma\notin\mathbb N$,
$\gamma\ge\beta_\iota-\beta_I-\epsilon$ and $\gamma\ge\beta_K$,
$$\mathcal Ff_1 = \rho^{\beta_I}|\sigma|^\gamma w,\qquad w\in H^{k+\ell}_{\mathrm b}\big(\pm[0,1]_\sigma\times
\bar X;|\tfrac{d\sigma}\sigma|\mu_{\mathrm b}\big).$$
So $(\mathcal Ff_1|_{(-\infty,0)},\mathcal Ff_1|_{(0,\infty)})$ lies in II.G$'$ Definition 2.7's $X^{k',\gamma}$ with
vanishing polynomial part, with values in $\rho^{\beta_I}H^{k''}_{\mathrm b}(\bar X,\mu_{\mathrm b})$, and II.G$'$
Proposition 2.8 (2) with $\beta = \gamma+1\notin\mathbb N$, applied to $V^\alpha\mathcal Ff_1$ for the b-fields $V$ on
$\bar X$ ($\mathcal F$ commutes with them), gives $f_1\in\rho^{\beta_I}\langle t_*\rangle^{-\gamma-1}H^k_{\mathrm b}
(\overline{\mathbb R}_{t_*}\times\bar X)$, in II.G$'$'s convention $H^{k,\beta}_{\mathrm b}(\mathbb R) =
\langle t_*\rangle^{-\beta}H^k_{\mathrm b}(\mathbb R,|dt_*/\langle t_*\rangle|)$; so does $\chi f_1$. As $\gamma>0$,
$f_1(\cdot,x)$ is integrable in $t_*$ (Cauchy-Schwarz with $\langle t_*\rangle^{-2\gamma-1}$), and $|\mathcal
Ff_1(\sigma)|\le C|\sigma|^\gamma$ (Sobolev embedding in $\log|\sigma|$, $\ell\ge1$), so
$$\int_{\mathbb R}f_1(t_*,x)\,dt_* = \mathcal Ff_1(0,x) = 0.\tag{3.4}$$
*For $t_*\le1$:* integrating $\chi f_1$ from $-\infty$ (III.A Lemma 1.2 in $\tau = |t_*|^{-1}$, where
$t_*\partial_{t_*} = -\tau\partial_\tau$, with weight $\gamma>0$ and the solution vanishing at $\tau = 0$),
$F_1|_{\{t_*\le 1\}}\in\rho^{\beta_I}\langle t_*\rangle^{-\gamma}\bar H^k_{\mathrm b}([-\infty,1]\times\bar X) = \bar
H^{k,\beta_I,\beta_I+\gamma,\gamma}_{\mathrm b}(\Omega_-)$: near $I$, $\rho\sim\rho_I$; near $\iota^-$, $\rho$ and
$\langle t_*\rangle^{-1}$ are both $\sim\rho_\iota$; near $K^-$, $\langle t_*\rangle^{-1}\sim\rho_K$; and the b-fields of
$\overline{\mathbb R}\times\bar X$ lift to span those of $M'$. *For $t_*\ge-1$:* by (3.4),
$$F_1(t_*) = -\int_{t_*}^\infty f_1(s)\,ds+F_3(t_*),\qquad F_3(t_*) :=
\int_{-\infty}^{t_*}\big((\chi-1)f_1\big)(s)\,ds.$$
The first term lies in $\rho^{\beta_I}\langle t_*\rangle^{-\gamma}\bar H^k_{\mathrm b}([-1,\infty]\times\bar X)$, which
is of weights $(\beta_I,\beta_I+\gamma,\gamma)$ at $(I,\iota^+,K^+)$, by the same integration from $+\infty$.
$(\chi-1)f_1$ is supported in $\{t_*\le-2r\}$, so $F_3|_{\Omega_<}\in\bar H^{k,\infty,\beta_I+\gamma,\gamma}_{\mathrm b}$
as above, and $\partial_{t_*}F_3 = (\chi-1)f_1\in H^{k,\infty,\beta_I+\gamma+1,\gamma+1}_{\mathrm b}(M')$; Lemma 2.1 (2)
(with $C = 1$) gives $F_3|_{\Omega_-}\in\bar H^{k,\beta_I+\gamma-\epsilon,\beta_I+\gamma,\gamma}_{\mathrm b}$, and Lemma
2.1 (1) ($\gamma\ne0$) $F_3\in H^{k,\beta_I+\gamma-\epsilon,\beta_I+\gamma-2\epsilon,((0,0),\gamma)}_{\mathrm b}(M')$.
Altogether, as $\beta_I+\gamma-\epsilon\ge\beta_I$ for $\epsilon$ small and $\beta_I+\gamma\ge\beta_\iota-\epsilon$,
$F_1\in H^{k,\beta_I,\beta_\iota-3\epsilon,((0,0),\gamma)}_{\mathrm b}(M')$.

*Conclusion.* $\chi u = F'+F_1+F_2\in H^{k,\beta_I,\beta_\iota-3\epsilon,((0,0),\beta_K)}_{\mathrm b}$, as
$\gamma\ge\beta_K$. $(1-\chi)u$ is supported in $\{t_*\le-2r\}\subset\Omega_<$, of weights
$(\infty,\beta_\iota,\beta_K)$. Renaming $\epsilon$ gives the claim. $\square$

## 4. The three frequency ranges

Fix $k$. Let $c\in(0,\frac12]$ be at most $\varsigma_1$ (II.G$'$ (4.5a)), the $c_{k'}$ of III.H Corollary 4.2 and the
$c_{j,k'}$ of III.H Theorem 4.1 (3) for $j+k'\le k+\ell_0$, $\ell_0$ the losses below, and $\chi\in C^\infty_c([0,c))$
equal 1 on $[0,\frac c2]$, as in III.H$'$ section 2. So $c$ depends on $k$, and through III.H's weight $\alpha$ (Lemma
4.2) on the step of section 5 in which it is used. The memberships (5.5)-(5.9) below hold at order $k$ for that $c$, the
losses $\ell_0$ being independent of $k$; $u$, $u_I$ and $u^\flat$ do not depend on $c$, so their memberships hold at
every order. $H^\infty$ in (5.5)-(5.9) is to be read in this sense. For $f\in C^\infty_c(\Omega_*^\circ)$, III.H$'$
Lemma 2.1, (4.1)-(4.2) and (5.1)-(5.2) give the forward solution of $L_bu = f$ as $u =
u_{\mathrm{hi}}+u_{\mathrm{reg}}+u_{\mathrm{sing}}$, with $\mathcal Fu_{\mathrm{hi}} =
(1-\chi(|\sigma|))\widehat{L_b}(\sigma)^{-1}\hat f(\sigma)$ on $\mathbb R$, $\mathcal Fu_{\mathrm{reg}} =
\chi(|\sigma|)\hat u_{\mathrm{reg},1}(\sigma)$ on $\mathbb R$ (III.H$'$ Lemma 4.1's proof), $(\hat
u_{\mathrm{reg},1},\hat b_1,\hat S_1) := \tilde L_b(\sigma)^{-1}(\hat f(\sigma),0,0)$, and $u_{\mathrm{sing}} =
\dot g+h_{\mathrm s1}$ of III.H$'$ (5.1), with (III.H$'$ Lemma 5.1's proof)
$$\mathcal F(\partial_{t_*}\dot g) = \chi(|\sigma|)G_1(\sigma)(\hat b_1(\sigma)),\qquad\mathcal F(\partial^2_{t_*}
h_{\mathrm s1}) = \chi(|\sigma|)G_2(\sigma)(\hat S_1(\sigma)),\tag{4.1}$$
$$G_1(\sigma)(\dot b) := \Psi(\sigma,\cdot)\dot g(\dot b),\qquad G_2(\sigma)(S) := (\Psi-\sigma\partial_\sigma\Psi)h(S)-
i\sigma\Psi\breve h(S),$$
$\Psi$ of III.H Lemma 2.5. The bounds below are linear in $f$, and the forward solution map is continuous (III.I Theorem
5.3 with $h = 0$, $S = 0$), so the decomposition and the bounds extend by density to the spaces stated. (These spaces
are extendible at $\{r = r_0\}$, where $C^\infty_c(\Omega_*^\circ)$ is not dense: one approximates an extension of $f$
across $\{r = r_0\}$, vanishing for $t_*<1$, by smooth compactly supported functions, for which the decomposition holds,
and restricts; the forward solution on $\{r\ge r_0\}$ depends on $f$ there only, $\{r = r_0\}$ being spacelike. III.H$'$
uses the same convention.)

**Lemma 4.1 (high and bounded frequencies; the source's (11.44)).** Let $f\in H^{\infty,(\beta_I^f+1,\beta_\iota+2,
\beta_K)}_{\mathrm b}(\Omega_*)^{\bullet,-}$ with $\beta_K\in(0,\infty)\setminus\mathbb N$, $\beta^f_I\ge\frac32$ and
$\beta^f_I+1\ge\beta_\iota+2-\min(\beta_K,1-\epsilon_1)$ for some $\epsilon_1\in(0,1)$. Then $u_{\mathrm{hi}}\in
H^{\infty,(\frac32-\epsilon,N,N)}_{\mathrm b}(M')$ for every $N$ and $\epsilon>0$.

*Proof.* Let $\chi_{C_0}$ be II.G$'$ Corollary 4.5's cut-off (1 on $[-C_0,C_0]$, supported in $[-C_0',C_0']$). The piece
$\mathcal F^{-1}((1-\chi_{C_0})\widehat{L_b}^{-1}\hat f)$ lies in $H^{\infty,(\beta'_I,N,N)}_{\mathrm b}(M')$ for every
$\beta'_I<\min(\beta^f_I,\frac32+\bar S) = \frac32$ by II.G$'$ Corollary 4.5 (with I.B's hypotheses for $2L_{b_0}$, as in
III.H$'$ section 3; $\bar S = 0$, III.I Theorem 5.3's proof). The rest is $w := (\chi_{C_0}-\chi(|\sigma|))\widehat{L_b}
^{-1}\hat f$, supported in $J := \{\frac c2\le|\sigma|\le C'_0\}$. By (2.25a) and (2.25b) (II.G$'$ Proposition 3.3 (1),
(2); the hypotheses on the weights are those of (1)), $\hat f$ lies on $\pm(0,1]$ in
$H^{\infty,(\min(\beta^f_I+1,\beta_\iota+2)-\epsilon,
\beta_\iota+1,\cdot)}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$ and on $\pm[\frac12,\infty)$ in the high-frequency
space with the scf-weight $\beta^f_I+1$; on functions supported in the compact set $J$, away from tf and zf, both norms
are equivalent to that of $\bar H^{\infty,\beta}_{\mathrm b}(J\times\bar X)$ of II.G$'$ Corollary 4.2 (2), with $\beta$
the scf-weight. So $\hat f|_J\in\bar H^{\infty,\frac52-\epsilon}_{\mathrm b}(J\times\bar X)$, as
$\beta_\iota+2\ge\frac52$ and $\beta_I^f+1\ge\frac52$ (if $\beta_\iota<\frac12$ use the weaker weight
$\beta_\iota+2-\epsilon$ in place of $\frac52-\epsilon$ throughout; in the applications $\beta_\iota>\frac12$). II.G$'$
Corollary 4.2 (2) with $\beta_{\mathrm{scf}} := \frac32-\epsilon<\frac32+\bar S$ ($\widehat{L_b}(\sigma)$ invertible on
$\bar J$, III.H Corollary 4.4) gives $w\in\bar H^{\infty,\frac32-2\epsilon}_{\mathrm b}(J\times\bar X)$. With $\chi'$
the cut-off of II.G$'$ Proposition 3.5, $\chi'w$, supported away from tf and zf, lies in
$H^{\infty,(\frac32-2\epsilon,N,N)}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$ for every $N$ (and has no Taylor
coefficients at 0), so Proposition 3.5 (1) gives $\mathcal F^{-1}(\chi'w)\in H^{\infty,(\frac32-3\epsilon,N,N)}_{\mathrm
b}(M')$; and $(1-\chi')w$, supported in $\pm[\frac12,C'_0]$, lies in the high-frequency space with every
$\sigma$-weight, so Proposition 3.5 (2) gives $\mathcal F^{-1}((1-\chi')w)\in
H^{\infty,(\frac32-2\epsilon,N,N)}_{\mathrm b}(M')$. Each step loses finitely many derivatives, depending on $N$; the
space is $H^\infty$. $\square$

**Lemma 4.2 (low frequencies; [Hin26c] Proposition 13.18 for $\tilde L_b$, the source's (11.45)).** Let $\alpha$ be as
in III.H (1.1), $\beta_{\mathrm{scf}}<\frac32$, $\epsilon\in(0,1)$, and $\beta_{\mathrm{tf}},\beta_{\mathrm{zf}}$ with
$\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}} = \alpha+2$. There is $\ell$ such that for $\hat f\in H^{k+\ell,(\beta_{\mathrm
{scf}}+1,\beta_{\mathrm{tf}}+2,\beta_{\mathrm{zf}})}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$ (over $\pm[0,c]$)
and $(\hat u,\hat b,\hat S)(\sigma) := \tilde L_b(\sigma)^{-1}(\hat f(\sigma),0,0)$,
$$\hat u\in H^{k,(\beta_{\mathrm{scf}}-\epsilon,\beta_{\mathrm{tf}},\beta_{\mathrm{zf}})}_{\mathrm
b}(X^\pm_{\mathrm{sc}\text-\mathrm b}),\qquad\hat b,\hat S\in H^{k,\beta_{\mathrm{zf}}}_{\mathrm b}
(\pm(0,c],|\tfrac{d\sigma}\sigma|),\tag{4.2}$$
with norms bounded by that of $\hat f$.

*Proof.* II.G$'$ Proposition 4.7's proof, with III.H Corollary 4.2 and Theorem 4.1 (3) for $\tilde L_b$ in place of I.C
Theorem 6.4 (4)-(5). Division by the scalar $|\sigma|^{\beta_{\mathrm{zf}}}$, which commutes with $\tilde
L_b(\sigma)^{-1}$ (componentwise, $\tilde L_b^{-1}$ being linear) and satisfies $\sigma\partial_\sigma|\sigma|^{\beta
_{\mathrm{zf}}} = \beta_{\mathrm{zf}}|\sigma|^{\beta_{\mathrm{zf}}}$, reduces to $\beta_{\mathrm{zf}} = 0$,
$\beta_{\mathrm{tf}} = \alpha+2$. Take $\alpha_+ := 0$, $\mathsf r_{\mathrm{out}} := \beta_{\mathrm{scf}}-2-\frac
\epsilon2$, below the outgoing threshold $-\frac12+\bar S = -\frac12$, and the orders of I.C section 6 built from it,
equal to $\mathsf r_{\mathrm{out}}$ near the zero section over sctf (as III.H Corollary 4.2's proof uses them). For
$0<|\sigma|\le c$ and $j\le k$, III.H Theorem 4.1 (3) (its (4.2), as III.H$'$ Lemmas 4.1-4.2 use it) bounds
$\|(\sigma\partial_\sigma)^j\tilde L_b^{-1}g\|$ in $\|\cdot\|_{(s+j;m),(\mathsf r,\alpha,0),\varsigma}$ plus the moduli
of the last two components by $C\|g\|_{(s-1;m+j),(\mathsf r+1,\alpha+2,0),\varsigma}$, $\varsigma = |\sigma|$. II.G$'$
(4.5b) and (4.5a) with $l = \alpha$ and $\frac\epsilon2$ convert the left side to $H^{m-\tilde\ell,(\beta_{\mathrm{scf}}
-\epsilon,\alpha+2,0)}_{\mathrm b,\varsigma}$ and the right side to $H^{m+j+\ell_a,(\beta_{\mathrm{scf}}+1,\alpha+4,0)}
_{\mathrm b,\varsigma}$, as $\mathsf r_{\mathrm{out}}+2-\frac\epsilon2 = \beta_{\mathrm{scf}}-\epsilon$ and
$\mathsf r_{\mathrm{out}}+3+\frac\epsilon2 = \beta_{\mathrm{scf}}+1$. Leibniz' rule and integration in
$|d\sigma/\sigma|$ (II.G$'$ section 4.3's description of the norm) give (4.2), with $\ell := \ell_a+\tilde\ell$; for the
moduli, $\int\sum_{j\le k}|(\sigma\partial_\sigma)^j\hat b|^2|d\sigma/\sigma|$ is bounded the same way. $\square$

**Lemma 4.3 (the cut-off states; the source's (11.47)-(11.48)).** Let $a\in\mathbb R$ and $\hat b\in H^{\infty,a}
_{\mathrm b}(\pm(0,c],|\frac{d\sigma}\sigma|;\mathfrak b_{\mathbb C})$, $\hat S\in H^{\infty,a}_{\mathrm b}
(\pm(0,c],|\frac{d\sigma}\sigma|;\mathcal S_{1,\mathbb C})$. Then for every $N$ and $\epsilon>0$,
$$\chi(|\sigma|)G_1(\sigma)(\hat b(\sigma))\in H^{\infty,(N,a+2-\epsilon,a)}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-
\mathrm b}),\qquad\chi(|\sigma|)G_2(\sigma)(\hat S(\sigma))\in H^{\infty,(N,a+3-\epsilon,a)}_{\mathrm b}(X^\pm_{\mathrm
{sc}\text-\mathrm b}).\tag{4.3}$$

The source's (11.47) has the orders $(1-\epsilon,1-\epsilon,\cdot)$ and $(1-\epsilon,2-\epsilon,\cdot)$ for the
uncut states, so its (11.48) has $(1-\epsilon,a+1-\epsilon,a)$ and $(1-\epsilon,a+2-\epsilon,a)$.

*Proof.* *Pointwise bounds.* By III.H section 1 the states $\dot g(\dot b)$ lie in $\mathcal A^q$ with $q = 2$ ($\dot
\mu$) or $3$ ($\dot A$), and $h(S)\in\mathcal A^3$, $\breve h(S)\in\mathcal A^2$. For $r\ge1$, $\Psi = \Phi(\sigma r)$,
$\Phi$ entire with $|\partial^j_\zeta\Phi|\le C_{j,M}\langle\zeta\rangle^{-M}$ (III.H Lemma 2.5 (b)), $\sigma\partial
_\sigma\Psi = \zeta\Phi'(\zeta)$ and $r\partial_r\Psi = \zeta\Phi'(\zeta)$, $\zeta = \sigma r$; so $G_1(\dot b) =
\Phi(\zeta)\dot g$ and $G_2(S) = (\Phi-\zeta\Phi')(\zeta)h-i\zeta\Phi(\zeta)\,r^{-1}\breve h$, with $r^{-1}\breve h\in
\mathcal A^3$. For $r\le1$, $\Psi$ and its $\sigma$- and $x$-derivatives are bounded for $|\sigma|\le1$ (III.H Lemma
2.5 (d) and its proof). Hence, with $q_1 := 2$, $q_2 := 3$ and $V$ any product of $\sigma\partial_\sigma$ and b-fields on
$\bar X$, $|VG_i|\le C_{V,M}\langle|\sigma|\langle x\rangle\rangle^{-M}\langle x\rangle^{-q_i}$ on basis elements.
*Weights.* By II.G$'$ section 4.3 the norm of $H^{K,\beta}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$ is equivalent
to $(\sum_{K'\le K}\int\|(\sigma\partial_\sigma)^{K'}v(\sigma)\|^2_{H^{K-K',\beta}_{\mathrm b,|\sigma|}}|\frac{d\sigma}
\sigma|)^{1/2}$, with $\|v\|_{H^{m,\beta}_{\mathrm b,\varsigma}} = \|w_\beta(\varsigma)^{-1}v\|_{\bar H^m_{\mathrm b}
(\bar X,\mu_{\mathrm b})}$ and (II.G$'$ Lemma 4.6's proof) $w_\beta(\varsigma)\sim\varsigma^{\beta_{\mathrm{tf}}}
W_\beta(\hat\rho)$, $\hat\rho := \langle x\rangle^{-1}/\varsigma$, $W_\beta(\hat\rho) = (\frac{\hat\rho}{1+\hat\rho})
^{\beta_{\mathrm{scf}}}(1+\hat\rho)^{\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}}}$, with bounded logarithmic derivatives.
Take $\beta = (N,a+q_i-\epsilon,a)$, so $\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}} = q_i-\epsilon$. Where $\varsigma\langle
x\rangle\ge1$ ($\hat\rho\le1$), $W_\beta^{-1}\le C(\varsigma\langle x\rangle)^N$, and with $M = N+q_i$,
$|W_\beta^{-1}VG_i|\le C\varsigma^{q_i}(\varsigma\langle x\rangle)^{-2q_i}$, whose square is
$\mu_{\mathrm b}$-integrable there with integral $\le C\varsigma^{2q_i}$. Where $\varsigma\langle x\rangle\le1$,
$W_\beta^{-1}\le C(\varsigma\langle x\rangle)^{q_i-\epsilon}$, so $|W_\beta^{-1}VG_i|\le C\varsigma^{q_i-\epsilon}
\langle x\rangle^{-\epsilon}$, and $\int\langle x\rangle^{-2\epsilon}\mu_{\mathrm b}<\infty$. So
$\|W_\beta^{-1}VG_i(\sigma)
\|_{L^2(\mu_{\mathrm b})}\le C|\sigma|^{q_i-\epsilon}$, and by Leibniz' rule
$$\|\chi G_1(\hat b)\|^2_{H^{K,\beta}}\le C\sum_{K'\le K}\int|\sigma|^{-2(a+q_1-\epsilon)}|\sigma|^{2(q_1-\epsilon)}
\,|(\sigma\partial_\sigma)^{K'}\hat b|^2|\tfrac{d\sigma}\sigma| = C\|\hat b\|^2_{H^{K,a}_{\mathrm b}},$$
and likewise for $G_2$. $\square$

## 5. Almost linear bounds ([Hin26] Proposition 11.17 at n = 4)

**Proposition 5.1 ([Hin26] Proposition 11.17 at n = 4, at $b_0$).** Let $\mathcal E^C_I$, $\mathcal E_+$ be as in
III.I Definition 1.1, $L$ as in section 1, and
$$2\le\ell_I<\min(a_I+\tfrac12,\ell_I^{\max}),\qquad\ell_I\notin\mathrm{Re}\,\pi_1\mathcal E^C_I,\quad\ell_I\notin
\tfrac32+\sigma_\Upsilon.\tag{5.1}$$
Let $\alpha_K\in[\frac12,1)$, $\alpha_+>\alpha_K$ and $\beta_+<\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal E_+)$.
For $f\in H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),\alpha_++2,\alpha_K}_{\mathrm b}(\Omega_*;S^2T^*)
^{\bullet,-}$, the forward solution $u$ of $Lu = f$ satisfies
$$u\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta_+,\alpha_K-2}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-}.
\tag{5.2}$$
Moreover $u$ depends continuously on $(S,h)$ in the space (5.2) with every weight lowered by $\varsigma$, for every
$\varsigma>0$.

The source has $\iota^+$-weight $\alpha_K-\epsilon$ and the $\mathscr I^+$-weight $3+\epsilon_I$. Its proof notes
that the decay would be $\alpha_+$ but for the singular terms at $\sigma = 0$; at $n = 4$ they do not limit it, and the
cap is $\frac32$ ((I$''$1)). $\ell_I\ge2$ serves (2.25a) in Lemma 4.1 and Step 2; the source's $3+\epsilon_I$ meets it.

*Proof.* *Step 0 (the start).* By III.C Definition 3.1 (2), $\min\mathrm{Re}\,\mathcal E^C_I>\frac32+2\gamma_\Upsilon$,
so the $\mathscr I^+$-exponents of $f$ ($\mathcal E^C_I+1$, and $\mathcal F_{I,11}\subset1+(\mathcal E^C_I\cup
(\frac32+(1-e_\Upsilon)\gamma_\Upsilon,0))$ for $\pi_{11}$) have real parts $>\frac52$, and $f\in
H^{\infty,(\frac52-\epsilon,\alpha_++2,\alpha_K)}_{\mathrm b}$. Fix $\beta^{(0)}_+\in(\frac12,\min(\alpha_+,\frac32,
\min\mathrm{Re}\,\mathcal E_+))$ and $\beta^{(0)}_I\in(\beta^{(0)}_+,\frac32)$; III.I Theorem 5.3 ($\alpha_K\ge\frac12$)
gives $u\in H^{\infty,(\beta^{(0)}_I,\beta^{(0)}_+,-\frac32)}_{\mathrm b}$. III.I$'$ Proposition 2.1 with $\ell_+ :=
\beta^{(0)}_+$ (below $\min\mathrm{Re}\,\mathcal E_+$, so $(\mathcal E_+,\ell_+)$ is the weight $\ell_+$ and
$\ell_+<a_++\min\mathrm{Re}\,\mathcal E_+$, $a_+>0$; $\ell_+$ is not in $\mathrm{Re}\,\pi_1\mathcal E_+$ nor in
$\mathrm{Re}\,\pi_1\mathcal E^{\mathrm{tot}}_I$, whose least real part is $\frac32$; $\ell_+<\frac32<\ell_I$), $f$
having $\iota^+$-weight $\alpha_++2\ge\ell_++2$, gives the expansion at $\mathscr I^+$ near $\mathscr I^+$; away from
$\mathscr I^+$ nothing changes. So
$$u\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta'_+,\alpha'_K-2}_{\mathrm b}\tag{5.3}$$
holds with $(\alpha'_K,\beta'_+) = (\frac12,\beta^{(0)}_+)$.

*The iteration.* Suppose (5.3) with $\alpha'_K\in[\frac12,\alpha_K]$ and $\beta'_+\in(\frac12,\min(\alpha_+,\frac32,\min
\mathrm{Re}\,\mathcal E_+))$. Put $\tilde\alpha_K := \min(\alpha'_K+a_K-2,\alpha_K)$ and fix
$$\gamma_+\in\big(\alpha_K,\ \min(\alpha_+,\tfrac32,\min\mathrm{Re}\,\mathcal E_+)\big),\qquad\epsilon>0\ \text{with}\
\gamma_+<\tfrac32-5\epsilon,\ \gamma_+-4\epsilon>\max(\tfrac12,\alpha_K).\tag{5.4}$$
Then $\gamma_+-\tilde\alpha_K\in(0,1)$ ($\tilde\alpha_K\le\alpha_K<\gamma_+<\frac32\le\tilde\alpha_K+1$) and $\gamma_+<
\tilde\alpha_K+1-\epsilon$.

*Step 1 (the source's (11.41)).* By III.I Proposition 4.1 (4.2), whose hypotheses hold ($\frac32<\ell_I<a_I+\frac12$;
$0<\beta'_+<\min\mathrm{Re}\,\mathcal E_+\le\max(a_+,\min\mathrm{Re}\,\mathcal E_+)$), $(L-L_b)u$ has $\mathscr
I^+$-data $(\langle\mathcal E^C_I+1\rangle',\ell_I+1)$, $\iota^+$-weight $\beta'_++2+m_+-\epsilon$ (with no expansion
term, as $\beta'_++m_+<2\min\mathrm{Re}\,\mathcal E_+$) and $K^+$-weight $\alpha'_K-2+a_K$. As $\beta'_++m_+-\epsilon>
\frac12+1-\epsilon>\gamma_+$,
$$L_bu = f' := f-(L-L_b)u\in H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),\gamma_++2,\tilde\alpha_K}_{\mathrm b}
(\Omega_*)^{\bullet,-}.$$

*Step 2a (null infinity; the source's (11.42)).* III.I$'$ Proposition 3.1 with $\breve{\mathcal E}_+ := \emptyset$ and
$\breve\ell_+ := \gamma_+$ ($\gamma_+<\frac32<\min\mathrm{Re}\,\mathcal E^C_I$, $\gamma_+\ne\frac32+(1-e_\Upsilon)
\gamma_\Upsilon$; $\ell_I$ by (5.1)) gives $u_I$ vanishing on $\{t_*<1\}\cup\{\rho_I>\frac12c_I\}$, with $\mathscr
I^+$-data $(\langle\mathcal E^C_I\rangle,\ell_I)$ and $\iota^+$-data $(\mathcal E^\sharp_+,\gamma_+)$, which is the
weight $\gamma_+$ as $\min\mathrm{Re}\,\mathcal E^\sharp_+\ge\min(\frac32+(1-e_\Upsilon)\gamma_\Upsilon,\min\mathrm{Re}\,
\mathcal E^C_I)>\frac32$ (III.I$'$ (3.2)); and $f^\flat := f'-L_bu_I\in H^{\infty,\ell_I+1,\gamma_++2,\tilde\alpha_K}
_{\mathrm b}(\Omega_*)^{\bullet,-}$, the $K^+$-weight unchanged as $u_I$ is supported near $\mathscr I^+$. $u^\flat :=
u-u_I$ vanishes for $t_*<1$ and solves $L_bu^\flat = f^\flat$, so it is the forward solution (II.E Proposition 3.4).

*Step 2b (the Fourier transform; the source's (11.43)-(11.52)).* Decompose $u^\flat = u_{\mathrm{hi}}+u_{\mathrm{reg}}
+u_{\mathrm{sing}}$ as in section 4, with $f^\flat$ for $f$. (2.25a) (II.G$'$ Proposition 3.3 (1) with
$(\beta_I,\beta_\iota,\beta_K) = (\ell_I+1,\gamma_++2,\tilde\alpha_K)$; $\tilde\alpha_K\in(0,1)$, and
$\ell_I+1\ge\gamma_++2-\min(\tilde\alpha_K,1-\epsilon_1)$ for $\epsilon_1<1-\tilde\alpha_K$, as
$\ell_I\ge2>\gamma_++1-\tilde\alpha_K$) gives
$$\hat f^\flat|_{\pm(0,1]}\in H^{\infty,(\min(\ell_I+1,\gamma_++2)-\epsilon,\gamma_++1,\tilde\alpha_K-1)}_{\mathrm
b}(X^\pm
_{\mathrm{sc}\text-\mathrm b}),$$
the zf index set $(0,0)$ dropping as $\tilde\alpha_K-1<0$.

*High frequencies.* Lemma 4.1 ($\beta^f_I = \ell_I$, $\beta_\iota = \gamma_+$, $\beta_K = \tilde\alpha_K$; its weight
condition is the one just checked) gives $u_{\mathrm{hi}}\in H^{\infty,(\frac32-\epsilon,N,N)}_{\mathrm b}(M')$.

*The regular part.* Lemma 4.2 with $\beta_{\mathrm{scf}} := \frac32-\epsilon$, $\beta_{\mathrm{tf}} := \gamma_+-1$,
$\beta_{\mathrm{zf}} := \tilde\alpha_K-1$ ($\alpha+2 := \gamma_+-\tilde\alpha_K\in(0,1)$; the source space contains
$\hat f^\flat$, as $\frac52-\epsilon\le\min(\ell_I+1,\gamma_++2)-\epsilon$) gives
$$\hat u_{\mathrm{reg},1}\in H^{\infty,(\frac32-2\epsilon,\gamma_+-1,\tilde\alpha_K-1)}_{\mathrm b},\qquad\hat b_1,
\hat S_1\in H^{\infty,\tilde\alpha_K-1}_{\mathrm b}(\pm(0,c],|\tfrac{d\sigma}\sigma|).\tag{5.5}$$
$\chi(|\sigma|)\hat u_{\mathrm{reg},1}$ is supported where II.G$'$ Proposition 3.5's cut-off is 1 ($c\le\frac12$), and
its Taylor condition is void ($K$-weight $\tilde\alpha_K$, $\tilde\alpha_K-1<0$); (2.26a) gives
$$u_{\mathrm{reg}}\in H^{\infty,(\gamma_+-\epsilon,\gamma_+,\tilde\alpha_K)}_{\mathrm b}(M').\tag{5.6}$$

*The singular part.* By (4.1), Lemma 4.3 with $a = \tilde\alpha_K-1$ and (5.5), and $\mathcal F(\partial_{t_*}v) =
-i\sigma\mathcal Fv$, which raises the tf- and zf-weights by 1,
$$\mathcal F(\partial^2_{t_*}u_{\mathrm{sing}}) = -i\sigma\chi G_1(\hat b_1)+\chi G_2(\hat S_1)\in H^{\infty,(N,\tilde
\alpha_K+2-\epsilon,\tilde\alpha_K-1)}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b}).\tag{5.7}$$
(The source's (11.49) has $(1-\epsilon,\tilde\alpha_K+1-\epsilon,\tilde\alpha_K)$; its zf-weight $\tilde\alpha_K$ is a
slip for $\tilde\alpha_K-1$, which its (11.48) gives and with which its Lemma 11.19 is then applied.) As $u^\flat = 0$
for $t_*<1$, $u_{\mathrm {sing}} = -(u_{\mathrm{hi}}+u_{\mathrm{reg}})$ there, so by (5.6) and the high-frequency bound,
with $\gamma_+<\frac32-
\epsilon$,
$$u_{\mathrm{sing}}|_{\Omega_-}\in\bar H^{\infty,\gamma_+-\epsilon,\gamma_+,\tilde\alpha_K}_{\mathrm b},\qquad
\partial_{t_*}u_{\mathrm{sing}}|_{\Omega_-}\in\bar H^{\infty,\gamma_+-\epsilon,\gamma_++1,\tilde\alpha_K+1}_{\mathrm
b}.\tag{5.8}$$
*First integration.* Lemma 3.1 applies to $v := \partial_{t_*}u_{\mathrm{sing}}$ with $\beta_I := \frac32$,
$\beta_\iota := \gamma_++1$, $\beta_K := \tilde\alpha_K-1$: $\beta_\iota>\beta_I$ ($\gamma_+>\frac12$);
$\beta_K<0<\beta_\iota-\beta_I$; $\beta_K\in[-\frac12,0)$; $v|_{\Omega_<}$ has the weights $(\cdot,\gamma_++1,\tilde
\alpha_K+1)$, at least $(\infty,\beta_\iota,\beta_K)$, by (5.8); $\mathcal Fv$ is $\chi(|\sigma|)$ times the boundary
value from $\mathrm{Im}\,\sigma>0$ of a function holomorphic inside $\gamma_0$ with at most a pole at 0 (III.H$'$
section 5), a distribution supported in a compact subset of $(-c,c)$, $c\le\frac12$, as Lemma 3.1 asks; and $\mathcal
F(\partial_{t_*}v)$ is (5.7), whose tf-weight $\tilde
\alpha_K+2-\epsilon$ is at least $\beta_\iota = \gamma_++1$ ($\gamma_+<\tilde\alpha_K+1-\epsilon$) and whose
zf-weight is $\beta_K$, with no zf index term as $\beta_K<0$. So
$$\partial_{t_*}u_{\mathrm{sing}}\in H^{\infty,\frac32,\gamma_++1-\epsilon,\tilde\alpha_K-1}_{\mathrm b}(M').$$
(The source takes $\beta_\iota = \tilde\alpha_K+1-\epsilon$, from (11.49) and $\min(\tilde\alpha_++1,\tilde\alpha_K+1-
\epsilon)$ in (11.50); here the tf-weight of (5.7) exceeds the a priori bound (5.8), which sets $\beta_\iota$.)
*Second integration.* Lemma 2.1 (1) for $u_{\mathrm{sing}}$ with $(\beta_I,\beta_\iota,\beta_K) := (\gamma_+-\epsilon,
\gamma_+-\epsilon,\tilde\alpha_K-2)$, $\mathcal E_K = \emptyset$ ($\tilde\alpha_K-2\ne0$): the hypotheses are (5.8) and
the last display ($\frac32\ge\gamma_+-\epsilon$). So
$$u_{\mathrm{sing}}\in H^{\infty,\gamma_+-\epsilon,\gamma_+-2\epsilon,\tilde\alpha_K-2}_{\mathrm b}(M'),\tag{5.9}$$
the $(0,0)$ at $K$ lying above the weight $\tilde\alpha_K-2<0$. With (5.6) and the high-frequency bound,
$u^\flat\in H^{\infty,\gamma_+-\epsilon,\gamma_+-2\epsilon,\tilde\alpha_K-2}_{\mathrm b}(\Omega_*)^{\bullet,-}$, and
$u = u^\flat+u_I$ has the same $\iota^+$- and $K^+$-weights.

*Step 3 (the source's recovery at $\mathscr I^+$).* III.I$'$ Proposition 2.1 with $\ell_+ := \gamma_+-2\epsilon$
(below $\min\mathrm{Re}\,\mathcal E_+$ and $a_++\min\mathrm{Re}\,\mathcal E_+$, below $\ell_I$, below
$\min\mathrm{Re}\,\mathcal E^{\mathrm{tot}}_I = \frac32$; $f$ has $\iota^+$-weight $\alpha_++2>\ell_++2$; the a priori
$\mathscr I^+$-weight $\gamma_+-\epsilon$) gives (5.3) with $(\alpha'_K,\beta'_+)$ replaced by $(\tilde\alpha_K,
\gamma_+-2\epsilon)$, again in the range of the iteration by (5.4).

*Conclusion.* Each step raises $\alpha'_K$ by $\min(a_K-2,\alpha_K-\alpha'_K)$, $a_K>2$, so finitely many reach
$\alpha'_K = \alpha_K$, with $\iota^+$-weight $\gamma_+-2\epsilon$; given $\beta_+$ as in the proposition, choose
$\gamma_+>\beta_++2\epsilon$ in (5.4). This is (5.2). Each step loses finitely many b-derivatives, and the spaces are
$H^\infty$ (section 4: at each order $k$, with the $c$ of that order).

*Continuity.* The maps of the scheme are linear in $f$ and $u$; $u_I$, $u_{\mathrm{hi}}$, $u_{\mathrm{reg}}$ and
$u_{\mathrm{sing}}$ depend on $f'$ only, through maps bounded between the spaces above (III.I$'$ Proposition 3.1's
construction by III.A Lemma 1.2, and Lemmas 2.1, 3.1, 4.1-4.3 with (2.25a), (2.26a), each with bounds). $(S,h)$ enters
through $L-L_b$, whose coefficients in (3.6) of III.I depend continuously on $(S,h)$ (III.I Proposition 3.4 and the
expansion of $g^{-1}$ after it), with (4.2)'s bound uniform for $(S,h)$ small; through the start, which III.I Theorem
5.3 gives continuously in $(S,h)$ at weights lowered by $\varsigma$; and through III.I$'$ Proposition 2.1 in Steps 0 and
3, whose proof is constructive (III.A Lemmas 1.2 and 3.2 with their bounds, the products by III.C Lemma 2.1 with the
coefficient norms of the operator), so that its bound depends on $L$ only through coefficient norms, which III.I
Proposition 3.4 bounds locally uniformly in $(S,h)$. (A closed graph argument would give a bound for each fixed $L$
only.) So every constant of the scheme, and the bound of $u$ in (5.2) by $f$, is locally uniform in $(S,h)$. For two
parameters, $L(u-u') = (L'-L)u'$ with $u'$ bounded in (5.2) uniformly and $(L'-L)u'$ small in the source space of Step 1
at the lowered weights; the bounds of the scheme for the difference give the claim, for $\varsigma$ below the room in
(5.4). $\square$

## 6. Findings, labels and sources

### 6.1 Findings

(I$''$1) *The $\iota^+$-weight does not fall to $\alpha_K$.* At $n = 4$ the transforms of the cut-off states
(III.H's $\chi_K$-states) decay rapidly at scf and have tf-orders $a+2$ and $a+3$ against the source's $a+1$, $a+2$
(Lemma 4.3), so the singular part's $\iota^+$-weight is set by the a priori bound on $\{t_*<1\}$, $\gamma_+-\epsilon$,
not by $\tilde\alpha_K-\epsilon$ (Step 2b); Proposition 5.1 keeps the $\iota^+$-weight $\min(\alpha_+,\frac32,\min
\mathrm{Re}\,\mathcal E_+)-\epsilon$ at every $K^+$-weight $\alpha_K-2$, where the source's is $\alpha_K-\epsilon$. The
cap $\frac32$ is Lemma 4.1's and Lemma 4.2's scf-weight, the transport of the radiation field's order from $\mathscr
I^+$; the source's corresponding cap is 1 (its p. 232; p. 238 names the transport).

(I$''$2) *The window.* The source relaxes the $\iota^+$-weight to $\tilde\alpha_+\in(\tilde\alpha_K,\tilde\alpha_K+
\epsilon_{\mathrm{ind}})$ to stay in the indicial gap at zero energy. At $n = 4$ the gap of $\widehat{L_b}(0)$ contains
$(0,1]$ (III.F$'$ Proposition 2.3 (a)), III.H (1.1)'s window $(0,1)$ lies inside it, and
$\gamma_+-\tilde\alpha_K\in(0,1)$ throughout (5.4); no relaxation is needed.

(I$''$3) *Lemma 11.19's range.* Its proof applies (2.26a) at the $K$-weight $\beta_K+1$, which must lie in
$(0,\infty)\setminus\mathbb N$: $\beta_K>-1$ is needed and not stated (Lemma 3.1). In Proposition 11.17 the source uses
$\beta_K = \tilde\alpha_K-1\in[-\frac12,0)$, inside the range.

(I$''$4) *The weight at null infinity.* (2.25a) in Step 2b needs $\ell_I+1\ge\gamma_++2-\tilde\alpha_K$; with the
$\iota^+ $-weights up to $\frac32$ this is $\ell_I\ge2$, which (5.1) asks and the source's $3+\epsilon_I$ meets; and
III.I Proposition 4.1's range (III.I (I6)) asks $\ell_I<a_I+\frac12$.

(I$''$5) *Lemma 11.19's support.* The source asks $\mathcal Fu$ supported in $[-1,1]\times X$; its proof needs the
support where II.G$'$ Proposition 3.5's cut-off is 1, and regularity across $\sigma = \pm1$ (II.G$'$ Definition 2.7).
Lemma 3.1 asks support in $[-c_0,c_0]$, $c_0<\frac12$, which its application has.

### 6.2 Labels

Proved: Lemmas 2.1, 3.1, 4.1-4.3 and Proposition 5.1, given the parts cited. Comparisons with the source are
commentary. READ: the source's statements quoted from pp. 231-238. Inputs: II.E Proposition 3.4; II.G$'$ section 3.1,
Remark 3.7, Definition 2.7, Proposition 2.8, Propositions 3.3, 3.5, Corollaries 4.2, 4.5, section 4.3, Lemma 4.6 and
Proposition 4.7's proof; III.A Lemmas 1.2, 3.2, 4.1 and section 4; III.C Definition 3.1; III.F$'$ (the gap); III.H
section 1, Lemma 2.5, Definition 3.1, Corollaries 4.2, 4.4, Theorem 4.1 (3); III.H$'$ sections 2-5; III.I Definition
1.1, (1.4), Propositions 3.4, 4.1, Theorem 5.3; III.I$'$ (1.1), Propositions 2.1, 3.1.

### 6.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 11.3 (pp. 231-238:
(11.38)-(11.62), Proposition 11.17, Lemmas 11.18-11.19, Figures 11.1-11.2, footnotes 105-109). N1STAR-PROOF.md 10.45
(b) and 10.61 (b) (the deductions this part replaces, in and without the class).
