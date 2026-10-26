# Part III.D. The gauge potential wave operator at n = 4 ([Hin26] section 6 to 6.3, Propositions 6.5 and 6.9)

*Status.* Verified (D226: the ninety-third verifier's findings are seated; the repairs are to be read). This part
proves, at spatial dimension $n = 4$ and for the Myers-Perry metrics $g_b$ of Part III.B with $b$ near the Tangherlini
parameter $b_0 = (\mu_0,0)$, what [Hin26] section 6 establishes up to and including section 6.3 and Proposition 6.9 (pp.
113-119): the structure of the gauge potential wave operator as a stationary wave-type operator (his Lemma 6.1), its
Minkowski model (Lemma 6.3), the input at the trapped set (Lemma 6.4) and the high-energy invertibility it gives
(Proposition 6.5), the indicial roots at zero energy (Lemma 6.6 with (6.17)), tf-admissibility (Lemma 6.8), and mode
stability away from zero frequency (Proposition 6.9), including the input he takes from [AHW24] Theorem 5.1, here proved
on five-dimensional Tangherlini. Section 6.4's zero-energy argument (Lemmas 6.10-6.11, Proposition 6.12, Lemma 6.13) is
Part III.D$'$, and section 6.5 (the large zero energy states) Part III.D$''$.

*Division of labour.* Parts I.A, I.B and I.C prove [Hin26c] section 9 at $n = 4$ for operators on a trivial bundle
satisfying hypotheses (H1)-(H8), (G), (Z), (TF), uniformly under (H5). Those hypotheses are of two kinds. The
*dynamical* ones concern the metric alone: the radial structure of the horizon in (H3), (H4), the existence of the time
function and the Lorentzian metric in (H6), the normally hyperbolic trapping (Γ.1)-(Γ.3) in (H7), and the global
dynamics (H8). As Parts I.B and II.B state, they are checked for $g_b$, $b$ near $b_0$, in Part VI; we write (Dyn) for
them. This part proves the *operator* hypotheses for the gauge potential operator: (H1)-(H2) with $\bar S$ (section 2),
the horizon threshold (section 5.1), the bound (Γ.4) at the trapped set (section 5.2), the gap (G) (section 4), and (TF)
(section 7). From these and (Dyn) it deduces [Hin26] Propositions 6.5 and 6.9. Part III.A$'$ is cited as III.A$'$, Part
III.B as III.B, Parts I.A-I.C as I.A-I.C. The computations cited as *computed* are exact (sympy) and rerun by the
instruments named; their statements are those of the record's supplement sections 10.15-10.20, whose instruments all
pass (D220).

## 1. The operator

Let $\mathcal B$ be III.B's parameter set near $b_0 = (\mu_0,0)$, $g_b$ the Myers-Perry metric (III.B Proposition 3.6),
$t_*$ the time function of III.B (3.6), $\rho := |x|^{-1}$ near infinity, and $E_\Upsilon =
(c_\Upsilon,e_\Upsilon,\gamma_\Upsilon;c_{\Upsilon,H},\gamma_{\Upsilon,H})$ as in III.B Definition 6.1 (trace weight
$\frac23$), with, as [Hin26] (6.1) demands, the supports of $c_{\Upsilon,H}$ and of $c_\Upsilon$ on $\{|x|<5R_1\}$
disjoint from a fixed neighbourhood $U_\Gamma$ of the projection of the trapped sets of all $g_b$, $b\in\mathcal B$ (by
(Dyn), these lie over a fixed compact subset of $\{r_h<|x|<5R_1\}$ near $|x|^2 = 2\mu_0$; section 5.2). The *gauge
potential wave operator* is
$$\Box^\Upsilon_b := \Box^\Upsilon_{g_b,E_\Upsilon} = 2\delta_{g_b,E_\Upsilon}G_{g_b}\delta^*_{g_b}
= \Box_{g_b}+2E^\Upsilon_{g_b}G_{g_b}\delta^*_{g_b},
\tag{1.1}$$
acting on 1-forms; here $\Box_g := 2\delta_gG_g\delta^*_g$, which on a Ricci-flat metric is the Hodge and the Bochner
d'Alembertian, $\Box_g = d\delta_g+\delta_gd = \nabla^*\nabla$. (Indeed $2(\delta_gG_g\delta^*_g\omega)_\nu =
-\nabla^\mu(\nabla_\mu\omega_\nu+\nabla_\nu\omega_\mu)+\nabla_\nu\nabla^\mu\omega_\mu =
-\nabla^\mu\nabla_\mu\omega_\nu-[\nabla^\mu,\nabla_\nu]\omega_\mu =
(\nabla^*\nabla\omega)_\nu-\mathrm{Ric}_\nu{}^\mu\omega_\mu$, and $d\delta+\delta d = \nabla^*\nabla+\mathrm{Ric}$ by
the Weitzenböck formula; computed on Tangherlini, `modes5.py` M1.) Its spectral family is
$\widehat{\Box^\Upsilon_b}(\sigma) := e^{i\sigma t_*}\Box^\Upsilon_be^{-i\sigma t_*}$, acting on stationary 1-forms on
$X$, which we trivialise by $dt_*,dx^1,\dots,dx^4$ (the bundle $E$ of I.A with $N = 5$).

## 2. Structure ([Hin26] Lemma 6.1 at n = 4)

The Minkowski model is $\bar g := -(dt_*+d|x|)^2+\sum_{i=1}^4(dx^i)^2$, Minkowski space in the time $\bar t := t_*+|x|$,
with $\bar c := |x|^{-1}d\bar t$, $\bar E h := -\gamma_\Upsilon(2\iota_{\bar g^{-1}\bar c}h-\frac23(1-e_\Upsilon)\bar
c\,\mathrm{tr}_{\bar g}h)$ and $\bar\Box^\Upsilon := 2(\bar\delta+\bar E)\bar G\bar\delta^*$. In $t_*$, $\rho$, $\omega
= x/|x|$ this is the Minkowski space of III.A$'$ section 2 with $t_* = \bar t-r$.

**Lemma 2.1.** (1) $\Box^\Upsilon_b$ is stationary with principal symbol $g_b^{-1}(\zeta,\zeta)\,\mathrm{Id}$, and
$\widehat{\Box^\Upsilon_b}(\sigma) = \hat P(0)+\sigma T+\sigma^2P_2$ satisfies (H1) and the operator part of (H6) of
I.A-I.B with $g = g_b$ and $t = t_*$: $P_2 = g_b^{00}\,\mathrm{Id}$, $g_b^{00} := g_b^{-1}(dt_*,dt_*)$, $\sigma_1(T) =
-2g_b^{-1}(dt_*,\cdot)\,\mathrm{Id}$, and $P_0-\Box_{g_b}\mathrm{Id}$ first order with $t_*$-independent coefficients.

(2) On $\{|x|>0\}$, exactly,
$$\bar\Box^\Upsilon
= -2\partial_{t_*}\rho\big(\rho\partial_\rho-\tfrac32-\bar S\big)+\widehat{\bar\Box^\Upsilon}(0),\tag{2.1}$$
with $\bar S$ and $\widehat{\bar\Box^\Upsilon}(0)\in\rho^2\mathrm{Diff}^2_{\mathrm b}$ given in Lemma 3.1, and no
$\partial_{t_*}^2$ term.

(3) On $\{|x|>3R_1\}$,
$$\Box^\Upsilon_b = \bar\Box^\Upsilon-g_b^{00}\partial_{t_*}^2+Q_b\partial_{t_*}+R_b,
\qquad g_b^{00}\in\rho^2C^\infty(\bar X),\quad
Q_b\in\rho^3\mathrm{Diff}^1_{\mathrm b},\quad R_b\in\rho^4\mathrm{Diff}^2_{\mathrm b},\tag{2.2}$$
all stationary and smooth in $b$ (and in $e_\Upsilon,\gamma_\Upsilon$). Hence (H2) holds with $S := \bar S$ near
infinity (in the Cartesian frame, $\Theta^{-1}\bar S\Theta$ with $\Theta = \Theta(\omega)$ the change from the null
splitting of III.A$'$ (2.2); its spectrum is that of $\bar S$), $Q := Q_b$, $P^{(0)} :=
\rho^{-2}(\widehat{\bar\Box^\Upsilon}(0)+R_b)$, and $P^{(0)}-((\rho D_\rho)^2+\Delta_{\mathbb
S^3})\mathrm{Id}\in\mathrm{Diff}^1_{\mathrm b}+\rho^2\mathrm{Diff}^2_{\mathrm b}$. The normal operator of $P^{(0)}$ at
$\rho = 0$, its indicial roots, and $\bar S$ do not depend on $b$.

*Proof.* (1) The terms $2E^\Upsilon G\delta^*$ and the connection terms of $\Box_{g_b}$ are of order at most 1, so the
principal part is $-g_b^{\mu\nu}\partial_\mu\partial_\nu\mathrm{Id}$ in the frame. Conjugating by $e^{-i\sigma t_*}$
replaces $\partial_{t_*}$ by $\partial_{t_*}-i\sigma$; the $\sigma^2$ term is $-g_b^{00}(-i\sigma)^2 =
\sigma^2g_b^{00}$, and the principal symbol of the $\sigma^1$ coefficient is $-2g_b^{-1}(dt_*,\zeta)$, times the
identity. $g_b^{00}<0$ on $X^\circ$ as $dt_*$ is timelike (III.B Lemma 3.7 (a)).

(2) By III.A$'$ Lemma 2.1 (1) at $N = 3$, $\bar\Box = -2\partial_{t_*}\rho(\rho\partial_\rho-\frac32)+{}^{\mathrm
b}\bar\Box(0)$, and by Lemma 3.1 below $2\bar E\bar G\bar\delta^* = 2\partial_{t_*}\rho\bar S+\gamma_\Upsilon\rho^2M_E$;
this is (2.1). The dual metric $\bar g^{-1} =
2\rho\partial_{t_*}\otimes_s\rho\partial_\rho+\rho^2((\rho\partial_\rho)^2+\slashed g^{-1})$ (III.A$'$ (2.3)) has no
$\partial_{t_*}\otimes\partial_{t_*}$ term, and $\bar E\bar G\bar\delta^*$ is of first order.

(3) *The metric.* By III.B Proposition 3.6, $g_b-\eta\in|x|^{-2}C^\infty$ with $\eta = -dt^2+dx^2$ in III.B's time $t$,
and $t_* = t-\psi(|x|)$ with $\psi' = 1-8\mu_0|x|^{-2}$ on $\{|x|\ge3R_1\}$ (III.B (3.6)). So $\eta-\bar g =
-(\psi'-1)d|x|\otimes_s(2dt_*+(\psi'+1)d|x|)\in\rho^2C^\infty$, and $k := g_b-\bar g\in\rho^2C^\infty(\bar X;S^2)$ in
the frame $dt_*,dx^i$, stationary; likewise $g_b^{-1}-\bar g^{-1}\in\rho^2C^\infty$, and $\bar g^{00} = 0$ gives
$g_b^{00}\in\rho^2C^\infty$. *Derivatives.* $\partial_{t_*}$ annihilates stationary coefficients and
$\partial_{x^i}\in\rho\mathcal V_{\mathrm b}(\bar X)$, so $\partial_{x^i}$ maps $\rho^aC^\infty(\bar X)$ to
$\rho^{a+1}C^\infty(\bar X)$. The coefficients of $\bar g$ are homogeneous of degree 0, so $\Gamma(\bar g)\in\rho
C^\infty$, and $\Gamma' := \Gamma(g_b)-\Gamma(\bar g)\in\rho^3C^\infty$. *The 1-form d'Alembertian.* $\Box_g\omega =
-g^{\mu\nu}(\partial_\mu\partial_\nu\omega-\dots)$ written out in Christoffel symbols has second-order coefficients
$g^{\mu\nu}$, first-order coefficients bilinear in $g^{-1}$ and $\Gamma$, and zeroth-order coefficients in
$g^{-1}\partial\Gamma$ and $g^{-1}\Gamma\Gamma$. Hence $\Box_{g_b}-\bar\Box$ has second-order coefficients in
$\rho^2C^\infty$ (vanishing in the $\partial_{t_*}\partial_{t_*}$ slot except for $g_b^{00}$), first-order coefficients
in $\rho^3C^\infty$ (from $\Gamma'$ and $(g_b^{-1}-\bar g^{-1})\Gamma(\bar g)$) and zeroth-order coefficients in
$\rho^4C^\infty$. *The modification.* Near infinity $c_\Upsilon = |x|^{-1}dt$ (III.B Definition 6.1) and
$c_\Upsilon-\bar c = |x|^{-1}(\psi'-1)d|x|\in\rho^3C^\infty$; with $g_b^{-1}-\bar g^{-1}\in\rho^2$ this gives
$E^\Upsilon_{g_b,\infty}-\bar E\in\rho^3C^\infty$ (zeroth order); $G_{g_b}-\bar G\in\rho^2C^\infty$;
$\delta^*_{g_b}-\bar\delta^*\in\rho^3C^\infty$ (zeroth order, by $\Gamma'$); $E^\Upsilon_{g_b,H} = 0$ there. So
$2E^\Upsilon G\delta^*-2\bar E\bar G\bar\delta^*$ is a sum of (zeroth-order $\rho^3$ coefficients) times $\partial$, and
of zeroth-order terms in $\rho^4$. *Sorting.* A Cartesian derivative is $\partial_{t_*}$ or lies in $\rho\mathcal
V_{\mathrm b}$. Terms $\rho^2\partial_{t_*}^2$ form $-g_b^{00}\partial_{t_*}^2$; terms
$\rho^2\partial_{t_*}\partial_{x^i}$ and $\rho^3\partial_{t_*}$ form $Q_b\partial_{t_*}$ with
$Q_b\in\rho^3\mathrm{Diff}^1_{\mathrm b}$; terms $\rho^2\partial_{x^i}\partial_{x^j}$, $\rho^3\partial_{x^i}$ and
$\rho^4$ form $R_b\in\rho^4\mathrm{Diff}^2_{\mathrm b}$. Smoothness in $b$ is that of $g_b$ (III.B). *(H2).* By (2), the
$\partial_{t_*}$-coefficient of $\Box^\Upsilon_b$ is $-2\rho(\rho\partial_\rho-\frac32-\bar S)+Q_b$, so $T =
2i\rho(\rho\partial_\rho-\frac32-\bar S)-iQ_b$. In the Cartesian frame $\bar\Box$ acts componentwise as the scalar
operator (III.A$'$ section 2.2, proof of Lemma 2.1), so ${}^{\mathrm b}\bar\Box(0) =
\rho^2(-(\rho\partial_\rho)^2+2\rho\partial_\rho+\Delta_{\mathbb S^3})\mathrm{Id}$ there, and
$\gamma_\Upsilon\rho^2M_E\in\rho^2\mathrm{Diff}^1_{\mathrm b}$ after the change of frame $\Theta(\omega)$, which
commutes with $\rho\partial_\rho$. With $(\rho D_\rho)^2 = -(\rho\partial_\rho)^2$ the last claim of (3) follows; the
normal operator of $P^{(0)}$ is that of $\rho^{-2}\widehat{\bar\Box^\Upsilon}(0)$, which does not involve $b$. $\square$

At $n = 3$ the source has $g_b-\bar g\in\rho C^\infty$ (the mass at $r^{-1}$) and so $S-\bar S\in\rho C^\infty$ and a
zero-energy difference in $\rho^3\mathrm{Diff}^2_{\mathrm b}$ ((6.7)); at $n = 4$ the mass enters at $\rho^2$, and each
difference gains one power.

## 3. The Minkowski model ([Hin26] Lemma 6.3 at n = 4)

**Lemma 3.1.** Let $N\ge2$ and $m := \frac2N$ (the trace weight $\frac2{D-2}$, $D = N+2$; $\frac23$ at $N = 3$). In the
splittings of III.A$'$ (2.2), with $D := \rho\partial_\rho$, $e := e_\Upsilon$, $\gamma := \gamma_\Upsilon$:
$$\bar c = \rho\big(\tfrac12,\tfrac12,0\big),\qquad\bar g^{-1}(\bar c) = -\rho(\partial_0+\partial_1),\qquad
\bar E = \gamma\rho\begin{pmatrix}2&2-2m(1-e)&0&0&0&\frac m2(1-e)\mathrm{tr}\\
0&2-2m(1-e)&0&2&0&\frac m2(1-e)\mathrm{tr}\\
0&0&2&0&2&0\end{pmatrix};\tag{3.1}$$
$$2\bar E\bar G\bar\delta^* = 2\partial_{t_*}\rho\bar S+\gamma\rho^2M_E,\qquad
\bar S = \gamma\begin{pmatrix}1-e&0&0\\1-e&2&0\\0&0&1\end{pmatrix},\qquad
M_E = \begin{pmatrix}-(1+e)D+Ne&-(1-e)D-Ne&-e\slashed\delta\\(1-e)D+Ne&(1+e)D-Ne&-e\slashed\delta\\
2d&2d&0\end{pmatrix};\tag{3.2}$$
so that $\bar\Box^\Upsilon = -2\partial_{t_*}\rho(D-\frac N2-\bar S)+\widehat{\bar\Box^\Upsilon}(0)$ with
$$\widehat{\bar\Box^\Upsilon}(0) = {}^{\mathrm b}\bar\Box(0)+\gamma\rho^2M_E.\tag{3.3}$$
At $N = 3$: $\bar E$ has the entries $\frac{2+4e}3$ and $\frac13(1-e)\mathrm{tr}$, and $M_E$ the constants $\pm3e$. At
$N = 2$, (3.1)-(3.3) are the source's (6.10)-(6.11). The spectrum of $\bar S$ is $\gamma(1-e)$, $2\gamma$, $\gamma$
(three times) at every $N$; so $\min\mathrm{Re}\,\mathrm{spec}\,\bar S = \gamma\min(1-e,1)$.

*Proof.* $d\bar t = \frac12(d\bar x^0+d\bar x^1)$ and $\bar g^{-1}(d\bar t) = -\partial_{\bar t} =
-(\partial_0+\partial_1)$ give the first two. For $h = (a,b,c,e',f,q)$: $\iota_{\bar g^{-1}\bar c}h =
-\rho(a+b,\,b+e',\,c+f)$ in the 1-form splitting, and $\mathrm{tr}\,h = -4b+\mathrm{tr}\,q$ (III.A$'$ section 2.1), so
$\bar Eh = -\gamma(2\iota h-m(1-e)\bar c\,\mathrm{tr}\,h)$ is (3.1). By III.B Lemma 6.2, $\bar E\bar Gh =
-\gamma(2\iota_{\bar g^{-1}\bar c}h-e\,\bar c\,\mathrm{tr}\,h)$, so
$$2\bar E\bar Gh = 2\gamma\rho\big(2a+2(1-e)b+\tfrac e2\mathrm{tr}\,q,\ 2(1-e)b+2e'+\tfrac e2\mathrm{tr}\,
q,\ 2(c+f)\big).$$
Insert $h = \bar\delta^*\omega$ from III.A$'$ Lemma 2.1 (1): $a = -\frac12\rho D\omega_0$, $b =
\frac12\partial_{t_*}\omega_0+\frac14\rho D(\omega_0-\omega_1)$, $c =
\rho(\frac12d\omega_0-\frac14(D+1)\slashed\omega)$, $e' = \partial_{t_*}\omega_1+\frac12\rho D\omega_1$, $f =
\frac12\partial_{t_*}\slashed\omega+\rho(\frac12d\omega_1+\frac14(D+1)\slashed\omega)$, $\mathrm{tr}\,q =
\rho(N(\omega_0-\omega_1)-\slashed\delta\slashed\omega)$ (as $\mathrm{tr}\,\slashed g = N$ and
$\mathrm{tr}\,\slashed\delta^* = -\slashed\delta$). The $\partial_{t_*}$-terms are
$2\gamma\rho\partial_{t_*}((1-e)\omega_0,\ (1-e)\omega_0+2\omega_1,\ \slashed\omega)$, which is $2\partial_{t_*}\rho\bar
S\omega$. The rest is $\gamma\rho^2$ times: in the first row
$-2D\omega_0+(1-e)D(\omega_0-\omega_1)+eN(\omega_0-\omega_1)-e\slashed\delta\slashed\omega$; in the second
$(1-e)D(\omega_0-\omega_1)+2D\omega_1+eN(\omega_0-\omega_1)-e\slashed\delta\slashed\omega$; in the third
$2d\omega_0+2d\omega_1$ (the $(D+1)\slashed\omega$ terms of $c$ and $f$ cancel). This is $M_E$. With III.A$'$ Lemma 2.1
(1) for $\bar\Box$ we get (3.3). $\bar S$ is lower triangular with diagonal $\gamma(1-e),2\gamma,\gamma$. At $N = 2$, $m
= 1$, $2-2m(1-e) = 2e$ and $\frac m2 = \frac12$, the source's (6.10); and $\pm Ne = \pm2e$, his (6.11). $\square$

*Checked by machine.* `harm5.py` K7: the type-wise matrices of $\widehat{\bar\Box^\Upsilon}(0)$ obtained from (3.3) and
III.A$'$ Lemma 1.5 equal, entry by entry, those of the Cartesian computation of $2(\bar\delta+\bar E)\bar G\bar\delta^*$
on static fields (`lin5.py` box_U, with the trace weight $\frac2{n-1}$), for the types s0, s1, s2, sl, v1, v2, vl, with
$l$, $\gamma$, $e$ symbolic, at $N = 2$ and $N = 3$; the $N = 2$ formula held against the $N = 3$ computation fails
(control).

## 4. Indicial roots ([Hin26] Lemma 6.6 and (6.17) at n = 4)

Write $z := 4e_\Upsilon\gamma_\Upsilon^2$, $\kappa := l(l+2)$ and, for $l\ge1$,
$$s_{l,1} := (l+1)^2+\tfrac z2-\Big((l+1)^2+z+\tfrac{z^2}4\Big)^{1/2},\qquad s_{l,2} := (l+1)^2+\tfrac z2+\Big((l+1)^2+z+
\tfrac{z^2}4\Big)^{1/2},$$
$$\lambda^\Upsilon_{\mathrm{s}l,l+j} := \tfrac12+\big(\tfrac14+s_{l,j}\big)^{1/2}\ (j = 1,2),\qquad
\lambda^\Upsilon_{\mathrm{s}0,2} := \tfrac12+\big(\tfrac94+z\big)^{1/2}.\tag{4.1}$$

**Lemma 4.1.** Let $z\in[0,\frac12]$. The indicial roots of $\widehat{\Box^\Upsilon_b}(0)$, which are those of
$\widehat{\bar\Box^\Upsilon}(0)$, are, in the terminology of III.A$'$ Definition 2.2:

s0: $1-\lambda^\Upsilon_{\mathrm{s}0,2}$, $0$, $\lambda^\Upsilon_{\mathrm{s}0,2}$, $3$;

sl, $l\ge1$: $1-\lambda^\Upsilon_{\mathrm{s}l,l+2}$, $1-\lambda^\Upsilon_{\mathrm{s}l,l+1}$, $1-l$,
$\lambda^\Upsilon_{\mathrm{s}l,l+1}$, $\lambda^\Upsilon_{\mathrm{s}l,l+2}$, $l+3$;

vl, $l\ge1$: $-l$, $l+2$.

All are real and simple (each a simple zero of the determinant of its type's indicial matrix, so the inverse of the
indicial family has at most simple poles). At $z = 0$, $\lambda^\Upsilon_{\mathrm{s}0,2} = 2$ and
$\lambda^\Upsilon_{\mathrm{s}l,l+j} = l+j$, the roots of III.A$'$ Lemma 2.3 for 1-forms. For $0<z\le\frac12$:
$$\lambda^\Upsilon_{\mathrm{s}l,l+j}\in\big(l+j,l+j+\tfrac14\big),\qquad\lambda^\Upsilon_{\mathrm{s}0,2}\in\big(2,
2+\tfrac z3\big],\qquad
2<\lambda^\Upsilon_{\mathrm{s}1,2}<\min\big(\lambda^\Upsilon_{\mathrm{s}0,2},3\big),\tag{4.2}$$
and $(0,\lambda^\Upsilon_{\mathrm{s}1,2})$ is an indicial gap (at $z = 0$ the gap is $(0,2)$). As $z\to0$,
$\lambda^\Upsilon_{\mathrm{s}0,2} = 2+\frac z3+O(z^2)$, $\lambda^\Upsilon_{\mathrm{s}l,l+1} =
l+1+\frac{lz}{2(l+1)(2l+1)}+O(z^2)$ and $\lambda^\Upsilon_{\mathrm{s}l,l+2} = l+2+\frac{(l+2)z}{2(l+1)(2l+3)}+O(z^2)$.
The s0 indicial solutions for the root 0 are spanned by $d\bar t$, and the s1 ones, for each $S\in\mathcal S_1$, by
$d(rS)$.

*Proof.* By Lemma 2.1 (3) the normal operator is that of the model, whose type-wise indicial matrices are read off from
(3.3) with III.A$'$ Lemma 1.5. Their determinants are (`harm5.py` K8, exact, $l$, $\gamma$, $e$ symbolic) a nonzero
constant times
$$\lambda(\lambda-3)(\lambda^2-\lambda-2-z)\ (\mathrm{s}0),\qquad(l+3-\lambda)(l+\lambda-1)\,
Q_l(\lambda^2-\lambda)\ (\mathrm{s}l),\qquad
(\lambda+l)(l+2-\lambda)\ (\mathrm vl),$$
$Q_l(s) := s^2-(2+2\kappa+z)s+\kappa(\kappa+1)+z\kappa$. The discriminant of $Q_l$ is $4(l+1)^2+4z+z^2>0$ (as $1+\kappa
= (l+1)^2$), so its roots are $s_{l,1}<s_{l,2}$, and $\lambda^2-\lambda = s$ gives $\lambda =
\frac12\pm(\frac14+s)^{1/2}$; $\lambda^2-\lambda = 2+z$ gives the s0 pair. This is the list. *Bounds.* $s_{l,1}\ge
l(l+1)$, with equality only if $lz = 0$: it is equivalent to $(l+1)+\frac z2\ge((l+1)^2+z+\frac{z^2}4)^{1/2}$, i.e. to
$(l+1)z\ge z$. As $\lambda\mapsto\lambda^2-\lambda$ increases on $\lambda>\frac12$,
$\lambda^\Upsilon_{\mathrm{s}l,l+1}\ge l+1$, strictly for $z>0$; and $\lambda^\Upsilon_{\mathrm{s}l,l+2}>l+2$ for $z>0$,
as $s_{l,2}>(l+1)(l+2)$. For the upper bounds, $\partial_zs_{l,j}\le\frac12+\frac{1+z/2}{2(l+1)}\le1+\frac z4$, so
$s_{l,j}-s_{l,j}|_{z=0}\le z(1+\frac z8)$, and $\lambda-(l+j)\le\frac{s-s|_{z=0}}{2(l+j)-1}\le\frac{z(1+z/8)}3<\frac14$
for $z\le\frac12$; similarly $(\frac94+z)^{1/2}\le\frac32+\frac z3$. *The ordering.*
$\lambda^\Upsilon_{\mathrm{s}1,2}<\lambda^\Upsilon_{\mathrm{s}0,2}$ iff $s_{1,1}<2+z$, iff $2-\frac
z2<(4+z+\frac{z^2}4)^{1/2}$, iff (squaring, $z<4$) $z>0$; $\lambda^\Upsilon_{\mathrm{s}1,2}>2$ iff $s_{1,1}>2$, iff
$2+\frac z2>(4+z+\frac{z^2}4)^{1/2}$, iff $z>0$; and $\lambda^\Upsilon_{\mathrm{s}1,2}<\frac94<3$. *The gap.* Every root
in the list other than $\lambda^\Upsilon_{\mathrm{s}1,2}$ is $\le0$ or $\ge\min(\lambda^\Upsilon_{\mathrm{s}0,2},3)$:
the negative ones are $1-\lambda\le-l$, $1-l\le0$, $-l$; the positive ones are $3$, $\lambda^\Upsilon_{\mathrm{s}0,2}$,
$l+3\ge4$, $l+2\ge3$, $\lambda^\Upsilon_{\mathrm{s}l,l+j}\ge l+j\ge3$ unless $(l,j) = (1,1)$. *Simplicity.* Within each
type the roots are distinct for $z\in[0,\frac12]$ by the bounds
($\lambda^\Upsilon_{\mathrm{s}l,l+1}<l+\frac54<l+2\le\lambda^\Upsilon_{\mathrm{s}l,l+2}<l+\frac94<l+3$, and the
negatives likewise), so each is a simple zero of a polynomial determinant, and $N(\lambda)^{-1} =
\mathrm{adj}\,N(\lambda)/\det N(\lambda)$ has at most a simple pole there. *Expansions.* $s_{l,1} =
l(l+1)+\frac{lz}{2(l+1)}+O(z^2)$, $s_{l,2} = (l+1)(l+2)+\frac{(l+2)z}{2(l+1)}+O(z^2)$, and $d\lambda/ds =
(2\lambda-1)^{-1}$. *Indicial solutions at 0.* $d\bar t$ and $d(rS)$ are Killing 1-forms of the model (translations),
homogeneous of degree 0, of types s0 and s1 (III.A$'$ Lemma 2.4); $\bar\Box^\Upsilon = 2(\bar\delta+\bar E)\bar
G\bar\delta^*$ annihilates them, and they are stationary, so they solve the indicial equation at $\lambda = 0$; the root
being simple, they span. $\square$

Compared with the source, where the s0 pair is $\pm(1+4e\gamma^2)^{1/2}$ about 0 and the gap is
$(0,\lambda^\Upsilon_{\mathrm{s}1,1})$, at $n = 4$ the roots do not pair about one point (D226; this sentence said
$\frac12$ before): the roots of $\lambda^2-\lambda = s$, the s0 pair and the $\lambda^\Upsilon_{\mathrm{s}l,\cdot}$ with
their partners $1-\lambda$, pair about $\frac12$, the vl roots $-l$, $l+2$ about 1, the s0 roots $0$, $3$ about
$\frac32$ and the sl roots $1-l$, $l+3$ about 2; the index of $\lambda^\Upsilon_{\mathrm{s}l,\cdot}$ is shifted by one,
and the gap is $(0,\lambda^\Upsilon_{\mathrm{s}1,2})$ with $\lambda^\Upsilon_{\mathrm{s}1,2}$ just above 2.

## 5. The subprincipal data

### 5.1 The horizon threshold

On five-dimensional Tangherlini, $f = 1-\mu_0/r^2$, $r_h = \mu_0^{1/2}$, in the ingoing chart $(v,r,\omega)$, let
$c_{\Upsilon,H} = c_v\,dv+c_r\,dr$ near $r_h$. *Computed* (`thresh5.py` U3; supplement Proposition 10.15 (iii)): at
$N^*\mathcal H$, $\zeta = \xi\,dr$, the subprincipal symbol of $\Box_{g_{b_0}}+2E^\Upsilon_{g_{b_0},H}G\delta^*$ (III.B
(6.1), whose $E^\Upsilon_H$ carries the factor $\gamma_{\Upsilon,H}$: $E^\Upsilon_HGh = 2\gamma_{\Upsilon,H}\iota h$ by
III.B Lemma 6.2; `thresh5` U3's $E_H$ is $E^\Upsilon_H/\gamma_{\Upsilon,H}$, and a second factor $\gamma_{\Upsilon,H}$
printed here before D226 was a double count), on half-densities by $|dg|$, is $i\xi f'(r_h)K$ with $K$ lower triangular,
its diagonal $1+c_v\gamma_{\Upsilon,H}r_h$, $-1+2c_v\gamma_{\Upsilon,H}r_h$ and $c_v\gamma_{\Upsilon,H}r_h$ (three
times), its angular block diagonal.

**Lemma 5.1 (the threshold).** Let $c_{\Upsilon,H} = -\frac12\chi(r)\,dr$ near $r_h$, $\chi = 1$ near $r_h$ (the choice
of Part III.D$'$). Then at $b_0$ the threshold quantity $\vartheta_{\mathcal H}$ of I.A (1.5), computed in a suitable
fibre inner product, is $1$ for every $\gamma_{\Upsilon,H}$, and the regularity condition $s>\frac12+\vartheta_{\mathcal
H}$ is $s>\frac32$. For every $\delta>0$ there is a neighbourhood of $b_0$ (and of
$(e_\Upsilon,\gamma_\Upsilon,\gamma_{\Upsilon,H})$ in a compact set) on which $\vartheta_{\mathcal H}<1+\delta$ in a
fixed fibre inner product.

*Proof.* $c_v = 0$, so $K$ has the distinct eigenvalues $1$, $-1$, $0$, the last with a diagonal block; $K$ is
diagonalisable, and in the inner product making the eigenvectors orthonormal its $h$-self-adjoint part is diagonal with
largest eigenvalue $1$. The normalisation of I.A (1.5), $\beta_0^{-1}p_{1,\pm}(0)$ with $p_{1,\pm} =
\pm\rho_\infty\sigma_1(\mathrm{Im}_h\hat P)$, divides $\xi f'(r_h)$ by the red-shift rate $\beta_0\rho_\infty^{-1}$,
which on Tangherlini is $\xi f'(r_h)$ up to the orientation sign that the $\pm$ removes; so $\vartheta_{\mathcal H}$ is
the largest eigenvalue, 1. The subprincipal symbol at $N^*\mathcal H_b$ and $\beta_0$ depend continuously on $b$ (the
horizon $\mathcal H_b$ and its conormal bundle depending smoothly on $b$, (Dyn)), so the largest eigenvalue in the fixed
inner product is continuous. $\square$

(At $n = 3$ the source's footnote 71 gives the threshold $\frac32$ for $\gamma_{\Upsilon,H} = 0$, "close to $\frac32$"
for small $\gamma_{\Upsilon,H}$. At $n = 4$ it is the same, and for this $c_{\Upsilon,H}$ it is exactly $\frac32$ for
every $\gamma_{\Upsilon,H}$.)

### 5.2 The trapped set ([Hin26] Lemma 6.4 at n = 4, in the form Part I.B uses)

The source proves that $\Box^\Upsilon_b$ is *strongly trapping admissible* ([Hin26c] Definition 5.8: for every
$\epsilon>0$ some fibre inner product makes the skew part at the trapped set smaller than $\epsilon$), at every
subextremal Kerr parameter, through a quasi-orthonormal frame special to Kerr. Part I.B does not use that property: its
Theorem 1.3 assumes (Γ.4), the condition $\gamma_-<0$, i.e. $\sup_\Gamma\lambda_{\max}(p_1^\Gamma)<\frac12\nu_{\min}$,
and its losses are governed by $\delta_\Gamma$ ((1.4) of I.B). That condition is open, and we prove it near $b_0$.

*Computed on Tangherlini* (`trap5.py` T0-T4, `hienergy5.py` V2-V3; supplement Propositions 10.14 and 10.16 (ii)-(iii)).
(a) $S_{\mathrm{sub}}(\Box_{g_{b_0}}) = -i\nabla^{\pi^*T^*}_{H_G}$ on half-densities by $|dg|$. (b) The trapped set in
the future characteristic set is $\{r^2 = 2\mu_0,\ \xi = 0\}$; at $z = 1$ in the semiclassical normalisation it is
$\{r^2 = 2\mu_0,\ \xi = 0,\ C = 4\mu_0\}$, $C = r^2|\eta|^2$ the Casimir of $\mathbb S^3$, with expansion rates
$\pm\nu$, $\nu = 4(2\mu_0)^{-1/2}$, $\{\phi_u,\phi_s\} = \nu/f>0$, $dG_1\ne0$, and $\beta_0 = 1/f(r_{\mathrm{ph}}) = 2$.
(c) On the characteristic set, the frame $e_0 = \zeta$, $e_1 = r(\zeta_{(1)}w^{(0)}+\zeta_{(0)}w^{(1)})$, $e_2 =
\frac{r^2}2(\zeta_{(0)}w^{(0)}+\zeta_{(1)}w^{(1)}-\eta)$ ($w^{(0)} = f^{1/2}dt$, $w^{(1)} = f^{-1/2}dr$) has Gram matrix
$CJ$, $J = ((0,0,-1),(0,1,0),(-1,0,0))$, and $\nabla_{H_G}e_0 = 0$, $\nabla_{H_G}e_1 = -2\sigma e_0$, $\nabla_{H_G}e_2 =
-2\sigma e_1$; an angular covector is orthogonal to all three iff it is orthogonal to $\eta$. (d) In the inner product
$\mathrm{diag}(1,\epsilon_1^{-1},\epsilon_1^{-2})$ on $\mathrm{span}\{e_0,e_1,e_2\}/C^{1/2}$ the endomorphism $p_1 =
-\frac12(M+M^*)$, $M$ the connection matrix of (c), has spectrum $0$, $\pm(2\epsilon_1)^{1/2}$.

**Lemma 5.2.** Assume (Dyn), with the trapped sets $\Gamma_b$ (at $z_0 = \pm1$) depending continuously on $b$ and
$\Gamma_{b_0}$ as in (b). For every $\epsilon>0$ there are a stationary fibre inner product $h_\Gamma$ on $\pi^*T^*$
over a neighbourhood of $\Gamma_{b_0}$ in phase space, homogeneous of degree 0 (it depends on the covector, as I.B (H7)
and II.C Definition 2.1 allow, I.B Lemma 6.0 reducing it to a standard one), and a neighbourhood $\mathcal B_\epsilon$
of $b_0$, such that for $b\in\mathcal B_\epsilon$ and every $E_\Upsilon$ as in section 1,
$\sup_{\Gamma_b}\lambda_{\max}(p_1^\Gamma)<\epsilon$. In particular (Γ.4) holds with $\gamma_-<0$ (take
$\epsilon<\frac12\nu_{\min}$), and $\delta_\Gamma(0)$, which by (1.4) of I.B tends to 0 with $\gamma_+$, is as small as
wished.

*Proof.* $E^\Upsilon$ vanishes over $U_\Gamma\supset\pi(\Gamma_b)$ (section 1), so $p_1^\Gamma$ is that of $\Box_{g_b}$.
*At $b_0$.* Near $\Gamma_{b_0}$, where $C>0$, split $\pi^*T^* = P\oplus V_\perp$ with
$P := \mathrm{span}\{e_0,e_1,e_2\}$ and $V_\perp$ its $g$-orthogonal complement, the angular covectors orthogonal to
$\eta$ (by (c)); $g$ is positive definite on $V_\perp$. $P$ is $\nabla_{H_G}$-invariant by (c), and as $\nabla$ is
metric, so is $V_\perp$, on which $\nabla_{H_G}$ is $g$-skew. Take
$h_\Gamma := \mathrm{diag}(1,\epsilon_1^{-1},\epsilon_1^{-2})$ on $P$ in the frame $e_j/C^{1/2}$ and $g$ on $V_\perp$;
it is stationary and homogeneous of degree 0, as $H_GC = 0$ and $C$ has degree 2. In these frames $h_\Gamma$ is
constant, $-iH_G$ is symmetric for the symplectic volume, and $H_G\sigma = 0$, so by (a) $p_1^\Gamma$ is
$-\frac12(M+M^*)$ on $P$ and $0$ on $V_\perp$, with largest eigenvalue $(2\epsilon_1)^{1/2}$ by (d) at the point
computed. The isometries of Tangherlini (time translations and $SO(4)$) act transitively on $\Gamma_{b_0}$ and preserve
the frame's construction, so this holds at every point. Choose $\epsilon_1$ with $(2\epsilon_1)^{1/2}<\epsilon/2$. *Near
$b_0$.* Extend $h_\Gamma$ to a stationary inner product on a neighbourhood of $\Gamma_{b_0}$. The endomorphism $p_1$ is
built from the subprincipal symbol of $\Box_{g_b}$ and $h_\Gamma$, continuous in $b$ uniformly near $\Gamma_{b_0}$, and
$\Gamma_b\to\Gamma_{b_0}$ by (Dyn); so $\sup_{\Gamma_b}\lambda_{\max}(p_1^\Gamma)<\epsilon$ for $b$ near $b_0$.
$\nu_{\min}$ and $\beta_0$ are continuous in $b$ by (Dyn) and positive at $b_0$. Two conventions, stated at D226:
$p_1^\Gamma$ is (6.0) of I.B Lemma 6.0 for this $h_\Gamma$, which in the frame $e_j/C^{1/2}$, where $h_\Gamma$ is
constant, is the $h_\Gamma$-imaginary part of the subprincipal operator, as computed; and (a) uses half-densities by
$|dg|$ while I.A's adjoints are for $|dx| = r^3dr\,d\omega$ and $dt_*$. On Tangherlini $|dg| = |dt_*|\,r^3dr\,d\omega$,
so the two agree at $b_0$; near $b_0$ the change of density by $f_b := |dg_b|/|dg_{b_0}|$ adds the scalar
$\frac12f_b^{-1}H_Gf_b = O(|b-b_0|)$ to $p_1$ (II.C, the remark after Lemma 2.2), which the continuity step absorbs.
$\square$

## 6. High energies and bounded frequencies ([Hin26] Propositions 6.5 and 6.9 at n = 4)

**Proposition 6.1 ([Hin26] Proposition 6.5).** Assume (Dyn). Fix $c_\Upsilon$ and $c_{\Upsilon,H}$ as in section 1.
There are $C_0$ and a neighbourhood $\mathcal B'$ of $b_0$ such that for $b\in\mathcal B'$ and
$(e_\Upsilon,\gamma_\Upsilon,\gamma_{\Upsilon,H})$ in a fixed compact set, $\widehat{\Box^\Upsilon_b}(\sigma):\mathcal
X_\sigma\to\mathcal Y_\sigma$ (I.A Theorem 7.2, orders as in I.B Theorem 1.3 (3)) is invertible for
$\mathrm{Im}\,\sigma\ge0$, $|\sigma|\ge C_0$.

*Proof.* Lemma 2.1 gives (H1), (H2) and the operator part of (H6); Lemma 5.1 the threshold in (H3) with
$s>\frac32+\delta$; Lemma 5.2 (Γ.4) with $\gamma_-<0$; (Dyn) the rest of (H3)-(H8), and the continuity in
$(b,e_\Upsilon,\gamma_\Upsilon,\gamma_{\Upsilon,H})$ of every datum is (H5), extended as in I.B. I.B Theorem 1.3 (3)
applies, with constants uniform in the parameters by I.B section 9. $\square$

Mode stability at bounded nonzero frequencies needs that of the unmodified operator at $b_0$, which [Hin26] takes from
[AHW24] Theorem 5.1 on Kerr. On five-dimensional Tangherlini it is three ordinary differential equation arguments. Write
$\Box := \Box_{g_{b_0}}$, $f = 1-\mu_0/r^2$, $r_* = r+\frac{r_h}2\log\frac{r-r_h}{r+r_h}$ (so $dr_*/dr = 1/f$ and $r_* =
r-\mu_0/r+O(r^{-3})$), $\Phi_* := d\Phi/dr_*$, $\kappa := l(l+2)$, and let $t$ be the static time. *Computed*
(`modes5.py` M1-M5; supplement Proposition 10.13), for $\sigma\in\mathbb C$, fields $e^{-i\sigma t}$ times stationary
ones, $r>r_h$:

(M1) $\Box = d\delta+\delta d$ on 1-forms.

(M2) For $u = r^{-3/2}\Phi(r)S$, $S\in\mathcal S_l$: $-fr^{3/2}(\delta du)/S = f(f\Phi')'+\sigma^2\Phi-V_0\Phi$, $V_0 =
\frac f{r^2}(\kappa+\frac34+\frac{9\mu_0}{4r^2})$.

(M3) For $A = r^{-1/2}\Phi(r)Y$, $Y$ a co-closed 1-form on $\mathbb S^3$ with $\slashed\delta\slashed dY = \lambda Y$:
$\delta A = 0$, and $\delta dA = 0$ is equivalent to $f(f\Phi')'+\sigma^2\Phi-V_1\Phi = 0$, $V_1 = \frac
f{r^2}(\lambda-\frac14+\frac{5\mu_0}{4r^2})$.

(M4) For $A = a(r)S\,dt+b(r)S\,dr$ (every scalar-type 1-form up to adding $d(cSe^{-i\sigma t})$, which does not change
$dA$), with $F_{tr} = -i\sigma b-a'$ and $M := \delta dA$: the function $W := r^3F_{tr}$ satisfies $R[W] :=
(fW'/r)'-\kappa W/r^3+\sigma^2W/(rf) = (r^2M_t)'+i\sigma r^2M_r$, and $fr^{1/2}R[r^{1/2}\Phi] =
f(f\Phi')'+\sigma^2\Phi-V_2\Phi$, $V_2 = \frac f{r^2}(\kappa+\frac34-\frac{7\mu_0}{4r^2})$; where $F_{tr} = 0$, $M_t =
\kappa a/r^2$ and $M_r = \kappa b/r^2$; at $l = 0$, $M_r = -i\sigma F_{tr}/f$.

(M5) $d\iota_T\omega+\iota_Td\omega = -i\sigma\omega$ for $T = \partial_t$ and every such $\omega$ (Cartan's formula).

The positivity used below is visible: $V_0>0$; $V_1>0$ when $\lambda\ge2$; $V_2>0$ when $\kappa\ge3$, as $\mu_0/r^2<1$
gives $\kappa+\frac34-\frac74\cdot1\ge2$.

**Proposition 6.2 (mode stability of $\Box$ on Tangherlini away from zero; replaces [AHW24] Theorem 5.1).** Assume (Dyn)
at $b_0$. For $\sigma\ne0$ with $\mathrm{Im}\,\sigma\ge0$, $\widehat\Box(\sigma):\mathcal X_\sigma\to\mathcal Y_\sigma$
is invertible.

*Proof.* By I.A Theorem 7.2 (3) and I.B Theorem 1.3 (3) (which apply to $\Box$, the case $E_\Upsilon = 0$ of sections
2-5), $\widehat\Box(\sigma)$ is Fredholm of index 0, so it suffices to show injectivity. Let $u\in\mathcal X_\sigma$,
$\widehat\Box(\sigma)u = 0$. By I.A Theorem 7.2 (5) with $\bar S = 0$, $u\in\mathcal A^{3/2-\epsilon}(\bar X)$ for every
$\epsilon>0$, smooth up to $\{|x| = r_0\}$, hence across the horizon $r = r_h>r_0$, and conormal at infinity. Let
$\omega := e^{-i\sigma t_*}u$, so $\Box\omega = 0$.

*The class.* III.B's $t_*$ is regular across the future horizon and outgoing at infinity: $t_* = v+F_H(r)$ near $r_h$
with $F_H$ smooth across $r_h$ in the ingoing chart ($v = t+r_*$), and $t_* = t-r_*+c_0+O(r^{-1})$, with all
derivatives, as $r\to\infty$ (III.B (3.6) and Lemma 3.5 at $A = 0$). So in the static chart
$\omega = e^{-i\sigma t}\omega_0$ with $\omega_0 = e^{-i\sigma r_*}\times$(smooth across $r_h$ in $(v,r)$) near $r_h$
and $\omega_0 = e^{i\sigma r_*}\times$(conormal, $O(r^{-3/2+\epsilon})$) near infinity. (In the static frame the
coefficients $a$, $b$ of (M4) are singular at $r_h$, $b = A_r+A_v/f$; the argument below uses only $F_{tr} = F_{vr}$ and
$\omega(T) = \omega(\partial_v)$, which are smooth across $r_h$.) Expanding in spherical harmonics on $\mathbb S^3$
(III.A$'$ Lemma 1.6; the projections act in the angles and preserve both properties, with bounds), every component
inherits them. We use repeatedly the following ODE fact: if $-\Phi_{**}+V\Phi = \sigma^2\Phi$ on $(r_h,\infty)$ with $V$
real, $V = O(r^{-2})$ with all derivatives at infinity and $V = O(f)$ near $r_h$, $\Phi = e^{-i\sigma r_*}h$ with $h$
smooth at $r_h$, and $\Phi = e^{i\sigma r_*}k$ with $k$ conormal and $O(r^{N})$ at infinity for some $N$, then
$\Phi = 0$, provided $V>0$. Indeed the solutions at infinity are $e^{\pm i\sigma r_*}(1+O(r^{-1}))$ (Volterra iteration,
$V\in L^1(dr_*)$ at infinity); the given form excludes $e^{-i\sigma r_*}$, which is $e^{i\sigma r_*}e^{-2i\sigma r_*}$
and $e^{-2i\sigma r_*}$ grows exponentially if $\mathrm{Im}\,\sigma>0$ and is not conormal if
$\sigma\in\mathbb R\setminus0$; so $\Phi = c\,e^{i\sigma r_*}(1+O(r^{-1}))$. If $\mathrm{Im}\,\sigma>0$, $\Phi$ and
$\Phi_*$ decay exponentially at both ends ($r_*\to\mp\infty$), and pairing with $\bar\Phi$ gives
$\int(|\Phi_*|^2+V|\Phi|^2)dr_* = \sigma^2\int|\Phi|^2dr_*$; if $\Phi\ne0$ the left side is positive, forcing
$\sigma^2>0$, i.e. $\sigma$ real: a contradiction. If $\sigma$ is real, the Wronskian $\mathrm{Im}(\bar\Phi\Phi_*)$ is
constant; at $r_h$, $\Phi_* = -i\sigma\Phi+e^{-i\sigma r_*}fh'$ gives $-\sigma|h(r_h)|^2$, and at infinity
$\sigma|c|^2$; so $c = 0$ and $\Phi = 0$.

*(a) The scalar step.* $\delta\omega$ solves $\delta d(\delta\omega) = \delta\Box\omega = 0$ by (M1). For each component
$r^{-3/2}\Phi S$ of $\delta\omega$, (M2) gives $-\Phi_{**}+V_0\Phi = \sigma^2\Phi$ (multiply by $f$), and the class
holds with the extra factor $r^{3/2}$ (polynomial growth); so $\Phi = 0$, and $\delta\omega = 0$.

*(b) The Maxwell step.* Then $\delta d\omega = \Box\omega-d\delta\omega = 0$. The vector-type components $r^{-1/2}\Phi
Y$ of $\omega$, $Y\in\mathcal V_l$, have $\slashed\delta\slashed dY = \lambda Y$ with $\lambda = (l+1)^2\ge4$ (the Hodge
eigenvalue on co-closed 1-forms of $\mathbb S^3$, III.A$'$ Lemma 1.4 (2) with Lemma 1.1: $\Delta_H = \slashed\Delta+2$,
$\slashed\Delta Y = (k_l^2-1)Y$), so (M3) and the ODE fact give $\Phi = 0$. For the scalar-type part at $l\ge1$, $W =
r^3F_{tr}$ solves $R[W] = 0$ by (M4) (as $M = 0$), so $\Phi := r^{-1/2}W$ solves the equation with $V_2>0$;
$F_{tr}\,dt\wedge dr = F_{vr}\,dv\wedge dr$ is a component of $d\omega$, so $\Phi$ is in the class, and $\Phi = 0$. Then
$F_{tr} = 0$ and $M = 0$ give $a = b = 0$ in the gauge of (M4), $\kappa\ne0$: that part of $\omega$ is a gradient. At $l
= 0$, $M_r = -i\sigma F_{tr}/f = 0$ gives $F_{tr} = 0$, which is all of $d\omega$ there. So $d\omega = 0$.

*(c) The gauge step.* By (M5) and $d\omega = 0$, $\omega = \frac i\sigma d\phi$ with $\phi := \omega(T)$, which is in
the scalar class. $\delta d\phi = -i\sigma\delta\omega = 0$, so $\phi = 0$ by (a), and $\omega = 0$ on $r>r_h$.

*(d) Inside the horizon.* So $u = 0$ on $\{r>r_h\}$; the horizon is null, so a Cauchy argument does not apply, and we
use the mode equations. Expand $u$ in harmonics (III.A$'$ Lemma 1.6): $\widehat\Box(\sigma)$ commutes with the
rotations, so the coefficients of each component of fixed type and degree $l$ form a vector $U(r)$ (at most three
functions on $(r_0,\infty)$), smooth across $r_h$, vanishing on $(r_h,\infty)$, which solves a system $-fU''+AU'+BU =
0$ with $A$, $B$ smooth on $(0,\infty)$. Indeed, in the ingoing chart $(v,r,\omega)$, regular across $r_h$, in which
$t_*-v$ is a function of $r$ (III.B (3.6)), $g^{vv} = 0$, $g^{vr} = 1$, $g^{rr} = f$ and $g^{rA} = 0$; conjugation by
$e^{-i\sigma t_*}$ turns $\partial_v$ into $-i\sigma$ and $\partial_r$ into $\partial_r-i\sigma\partial_rt_*$, so the
only second $r$-derivative of $\widehat\Box(\sigma)$ is $-f\partial_r^2$, and on a harmonic component the angular
derivatives are algebraic. Put $Y := (U,(r-r_h)U')$. Since $(r-r_h)/f = r^2/(r+r_h)$,
$$(r-r_h)Y' = MY,\qquad M = \begin{pmatrix}0&1\\ \frac{r^2(r-r_h)}{r+r_h}B&1+\frac{r^2}{r+r_h}A\end{pmatrix},$$
with $M$ smooth on $(0,\infty)$. For $r_0<r_1<r<r_h$ and $m := \max_{[r_1,r_h]}\|M\|$, wherever $Y\ne0$,
$\frac d{dr}\log|Y|^2 = \frac{2\mathrm{Re}\langle Y,MY\rangle}{(r-r_h)|Y|^2}\ge-\frac{2m}{r_h-r}$, so if $Y(r_1)\ne0$
then $|Y(r)|\ge|Y(r_1)|\big(\frac{r_h-r}{r_h-r_1}\big)^m$ on $[r_1,r_h)$ (the bound holds up to the first zero of $Y$
after $r_1$, if there is one, and by continuity keeps $|Y|$ positive there, so there is none), which contradicts the
vanishing of $Y$ to infinite order at $r_h$. So $Y(r_1) = 0$ for every $r_1\in(r_0,r_h)$, every component vanishes, and
$u = 0$. $\square$

**Proposition 6.3 ([Hin26] Proposition 6.9).** Assume (Dyn). Let $c_0>0$. There are $\epsilon>0$ and a neighbourhood
$\mathcal B''$ of $b_0$ such that if $|e_\Upsilon|,|\gamma_\Upsilon|,|\gamma_{\Upsilon,H}|<\epsilon$ and $b\in\mathcal
B''$, then $\widehat{\Box^\Upsilon_b}(\sigma)$ is invertible for all $\sigma$ with $\mathrm{Im}\,\sigma\ge0$,
$|\sigma|\ge c_0$.

*Proof.* Let $\mathsf p := (b,e_\Upsilon,\gamma_\Upsilon,\gamma_{\Upsilon,H})$, a parameter in a compact set, with
$\mathsf p_0 := (b_0,0,0,0)$, at which the operator is $\Box$. For $|\sigma|\ge C_0$ Proposition 6.1 applies. The set $K
:= \{c_0\le|\sigma|\le C_0,\ \mathrm{Im}\,\sigma\ge0\}$ is compact, and at each $\sigma\in K$, $\widehat\Box(\sigma)$ is
invertible by Proposition 6.2. By I.A Theorem 8.1 (invertibility is open in $(\sigma,\mathsf p)$, the hypotheses holding
uniformly by section 2 and (Dyn)), each $\sigma\in K$ has a neighbourhood $U_\sigma$ and $\epsilon_\sigma$ with
invertibility on $U_\sigma\times\{|\mathsf p-\mathsf p_0|<\epsilon_\sigma\}$; finitely many $U_\sigma$ cover $K$.
$\square$

## 7. tf-admissibility ([Hin26] Lemma 6.8 at n = 4)

**Lemma 7.1.** There is $\epsilon>0$ such that for $e_\Upsilon\in[0,\epsilon)$, $|\gamma_\Upsilon|<\epsilon$, every
$\gamma_{\Upsilon,H}$ and every $b\in\mathcal B$, $\widehat{\Box^\Upsilon_b}$ is tf-admissible (I.C Definition 5.1) with
every weight in the indicial gap $(0,\lambda^\Upsilon_{\mathrm{s}1,2})$ of Lemma 4.1 (with $(0,2)$ when
$e_\Upsilon\gamma_\Upsilon^2 = 0$).

*Proof.* The transition face operator $N_{\mathrm{tf}}(e^{i\theta})$ of I.C section 4 is built from the data of the
operator at $\rho = 0$ only: $S_0$, the normal operator $N(P^{(0)})$ and $H_0$. By Lemma 2.1 (3) these are the model's,
independent of $b$ and of the horizon modification; so it suffices to consider $\bar\Box^\Upsilon$. *At $\gamma_\Upsilon
= 0$.* The model is $\bar\Box$, which in the Cartesian frame has $S_0 = 0$, $N(P^{(0)}) =
(-(\rho\partial_\rho)^2+2\rho\partial_\rho+\Delta_{\mathbb S^3})\mathrm{Id}$ (Lemma 2.1 (3)) and, with the standard
inner product, $H_0 = \mathrm{Id}$: by I.C Proposition 5.3 it is tf-admissible with every weight in $(0,2)$. *Small
$\gamma_\Upsilon$.* Fix the weight $\beta = 1$, which lies in the gap for all small parameters (Lemma 4.1), and $q =
2-\beta$, and orders $s$, $\alpha_+$, $\mathsf r_\pm$ as in I.C Theorem 4.3, admissible with margins at $\gamma_\Upsilon
= 0$; as $\bar S = O(\gamma_\Upsilon)$ (Lemma 3.1) and the thresholds of I.A (1.5) move continuously, they remain
admissible for small parameters. The perturbation $N^\gamma_{\mathrm{tf}}-N^0_{\mathrm{tf}} = -2ie^{i\theta}\hat\rho\bar
S+\gamma_\Upsilon\hat\rho^2M_E(\hat\rho\partial_{\hat\rho},\partial_\omega)$ (the source's (6.18a) with Lemma 3.1) is
bounded from the space $H^{s,(\mathsf r+\alpha_+,q)}_{\mathrm{sc},b}$ of $\mathcal X_{\mathrm{tf},\theta}$ into that of
$\mathcal Y_{\mathrm{tf},\theta}$ with norm $O(|\gamma_\Upsilon|)$, uniformly in $\theta$: near the end $\hat\rho\to0$,
$\hat\rho\cdot(\text{order }0)$ gains one order of decay and $\hat\rho^2\mathrm{Diff}^1_{\mathrm b} =
\hat\rho\,\mathrm{Diff}^1_{\mathrm{sc}}$ gains one order of decay for one sc-derivative; near $\hat\rho\to\infty$ the
weights $q$ and $q-2$ allow the factors $\hat\rho$, $\hat\rho^2$. So $\mathcal X_{\mathrm{tf},\theta}$ is the same space
for all small $\gamma_\Upsilon$, and by I.C Corollary 5.2 (b) at $\gamma_\Upsilon = 0$, uniformly over the three
sectors, $\|w\|\le C\|N^0_{\mathrm{tf}}w\|\le C\|N^\gamma_{\mathrm{tf}}w\|+C'|\gamma_\Upsilon|\|w\|$; for
$C'|\gamma_\Upsilon|\le\frac12$ this gives injectivity of $N^\gamma_{\mathrm{tf}}(e^{i\theta})$ for all
$\theta\in[0,\pi]$, and the adjoint estimate (5.2) gives that of $N^\gamma_{\mathrm{tf}}(1)^{*h}$ in the same way. So
$\widehat{\bar\Box^\Upsilon}$ is tf-admissible with weight 1, and by I.C Corollary 5.2 (c) with every weight in the gap.
The condition $e_\Upsilon\ge0$ makes $z\ge0$, so that Lemma 4.1 describes the gap. $\square$

## 8. Findings, labels and sources

### 8.1 Findings

(D1) *The structure at $n = 4$.* [Hin26] Lemma 6.1 holds with $\rho\partial_\rho-\frac32$ for $\rho\partial_\rho-1$,
and, the mass of $g_b$ entering at $|x|^{-2}$, the deviations from the model gain a power: $S$ may be taken equal to
$\bar S$ near infinity, $Q\in\rho^3\mathrm{Diff}^1_{\mathrm b}$ as in the source, and the zero-energy difference lies in
$\rho^4\mathrm{Diff}^2_{\mathrm b}$ (source: $\rho^3$). The model is Minkowski space in $\bar t = t_*+|x|$, not in
III.B's $t$; the two differ by $8\mu_0|x|^{-1}$ plus a constant, which is harmless.

(D2) *The constants.* With the trace weight $\frac2{D-2}$ the modification acts through $E^\Upsilon G$ as at $D = 4$, so
$\bar S$ is the source's in every dimension; $\bar E$ itself carries $m = \frac2N$, and $\widehat{\bar\Box^\Upsilon}(0)$
the constants $\pm Ne$ ($\pm3e$ at $n = 4$, $\pm2e$ in the source).

(D3) *The indicial roots.* At $n = 4$ the roots of $\widehat{\Box^\Upsilon}(0)$ pair about four centres, $\frac12$, 1,
$\frac32$ and 2 by family (section 4; this said $\frac12$ before D226); the modified s0 pair is
$\frac12\pm(\frac94+4e\gamma^2)^{1/2}$, the sl roots move from $l+1$, $l+2$ (and their mirrors), the vl roots do not
move, and the gap is $(0,\lambda^\Upsilon_{\mathrm{s}1,2})$,
$\lambda^\Upsilon_{\mathrm{s}1,2} = 2+\frac{4e\gamma^2}{12}+O(e^2\gamma^4)$. The source's $z = e\gamma^2$ appears here
as $4e\gamma^2$.

(D4) *Trapping.* The source's Lemma 6.4 (strong trapping admissibility for every $\epsilon$) is not what Part I.B uses,
and it is not an open condition; what I.B uses, $\gamma_-<0$ with $\delta_\Gamma$ small, is open, and Lemma 5.2 proves
it near $b_0$ from the exact computation on Tangherlini. The record's supplement 10.60 (b) said that strong trapping
admissibility persists for $b$ near $b_0$ because "the inequalities are open"; for the all-$\epsilon$ property that is
not right, and it is not needed. The second angular direction of $\mathbb S^3$ (absent on $\mathbb S^2$) is carried by
metric compatibility.

(D5) *[AHW24] replaced.* On five-dimensional Tangherlini the mode stability of the unmodified operator away from zero
(Proposition 6.2) is three ordinary differential equation arguments with positive potentials, save the spherically
symmetric Maxwell sector, which its own equation settles; near $b_0$ it is carried by perturbation (Proposition 6.3). No
analysis of the Teukolsky-type equations of Myers-Perry is needed.

(D6) *The horizon threshold.* With $c_{\Upsilon,H} = -\frac12\chi\,dr$ the threshold is exactly $s>\frac32$ for every
$\gamma_{\Upsilon,H}$ (Lemma 5.1).

### 8.2 Labels

Proved here, assuming (Dyn) (Part VI): Lemmas 2.1, 3.1, 4.1, 5.1, 5.2, 7.1 and Propositions 6.1-6.3. Computed (exact;
rerun D220): `harm5.py` K7-K8, `thresh5.py` U3, `trap5.py` T0-T4, `hienergy5.py` V2-V3, `modes5.py` M1-M5. Standard
facts used: the Weitzenböck formula, Cartan's formula, the Volterra construction of solutions $e^{\pm i\sigma
r_*}(1+O(r^{-1}))$ for integrable potentials, Gronwall's inequality, and the
adjugate formula for the inverse of a matrix.

### 8.3 Sources

READ: [Hin26] pp. 113-119 (section 6 to (6.20) and Proposition 6.9, with footnotes 60-64), arXiv:2606.28253v2, full
text. The record's supplement sections 10.15-10.20 (N1STAR-PROOF.md) for the computed statements. Not relied on: [AHW24]
(replaced by Proposition 6.2), [Hin17] Proposition 4.1 (computed directly on Tangherlini in (a) of section 5.2),
[Hin24a] (the Kerr frame, not used at $n = 4$).
