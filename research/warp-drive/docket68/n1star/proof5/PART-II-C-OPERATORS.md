# Part II.C. Wave-type operators, the time function and the order functions, at n = 4

*Status.* Verified. Written out in full (D198). Read line by line by the eighty-second verifier, which re-derived every
computation and confirmed (C1)-(C3) at source; its one minor finding (the form of the Minkowski metric stated in the
proof of Lemma 1.3, on which the argument for $\omega^\mu\bar\Gamma_{\kappa\mu\nu} = 0$ rested; the claim holds) and
seven nits are seated (D200). The part is labelled proved once the next reader has confirmed them. This part proves, at
spatial dimension $n = 4$, [Hin26c] section 5 (pp. 100-110) and section 6 (pp. 110-114) except its Proposition 6.3, the
stable and unstable trapped sets of perturbed metrics, which is the subject of Part II.C$'$ (in writing). The source is
[Hin26c] = P. Hintz, arXiv:2606.28008v1 (printed page numbers). Part I.A (`PART-I-SPECTRAL.md`) is cited as I.A, Part I.B
(`PART-I-B-HIGHENERGY.md`) as I.B, Part I.C (`PART-I-C-LOWENERGY.md`) as I.C, Part II.A (`PART-II-A-SETUP.md`) as II.A
and Part II.B (`PART-II-B-DYNAMICS.md`) as II.B.

*Method.* Section 5 of the source consists of definitions and three lemmas. The definitions are restated at $n = 4$: the
constant 1 of its form (5.1a) becomes $\frac32 = \frac{n-1}2$, the weight $\alpha_{\mathrm{sf}}+\frac32$ of its
tf-admissibility becomes $\alpha_{\mathrm{sf}}+2$, and the stationary model is that of II.B, a metric satisfying
(K1)-(K4) with Part I's (H1)-(H8), in place of Kerr. The three lemmas are proved. Of section 6, Proposition 6.1 is proved
from II.B. Proposition 6.4, which the source proves by citation to the construction of [Hin23c] = P. Hintz, *Linear waves
on non-stationary asymptotically flat spacetimes. I*, arXiv:2302.14647v1, Lemma 5.8 and Appendix C (pp. 106-107,
150-154), is proved here by that construction, written out in the coordinates of II.B and with the error terms of the
present class.

*How it is organised.* Section 1: stationary wave-type operators. Section 2: admissibility of the stationary model.
Section 3: asymptotically stationary metrics, the time function and admissible wave-type operators. Section 4: the global
dynamics of perturbed metrics. Section 5: order functions. Section 6: what this part found.

## 1. Stationary wave-type operators

### 1.1 The class

Throughout, $g$ is the stationary metric of II.B section 1.1, which satisfies (K1)-(K4), $E_X := \tilde X\times\mathbb
C^N$ is the trivial bundle of I.A section 1.2, and $E := \pi_X^*E_X$ its pullback along $\pi_X(t_*,x) := x$. Sections of
$E$ are $\mathbb C^N$-valued functions, and $\partial_{t_*}$ and $\rho\partial_\rho$ act componentwise; the connection of
[Hin26c] Remark 5.3, needed for non-trivial bundles, is not needed here. $G(\zeta) := g^{-1}(\zeta,\zeta)$, $\rho :=
r^{-1}$, and $\rho_1$ is that of I.A section 1.1. The density is $|dt_*\,dx| = |dt\,dx|$, the Euclidean density of I.A
section 1.1 times $|dt_*|$, and for a fibre inner product $h$ (I.A section 1.2), $A^{*h}$ and $\mathrm{Im}_hA :=
(A-A^{*h})/2i$ are taken with respect to it.

**Definition 1.1 ([Hin26c] Definition 5.1 at $n = 4$).** A $t_*$-translation-invariant $P_0\in\mathrm{Diff}^2(\mathbb
R_{t_*}\times\tilde X^\circ;E)$ is a *stationary wave-type operator* (for $g$) if (1) $\sigma_2(P_0) = G\,\mathrm{Id}$,
and (2) on $\{\rho<\rho_1\}$,
$$P_0 = -2\partial_{t_*}\rho\big(\rho\partial_\rho-\tfrac32-S\big)+\hat P_0(0)+Q\partial_{t_*}-g_{00}\partial_{t_*}^2,
\tag{1.1}$$
with $g_{00} := g^{-1}(dt_*,dt_*)$ and, all $t_*$-independent, $\hat P_0(0)\in\rho^2\mathrm{Diff}^2_b(\bar X;E)$, $S\in
C^\infty(\bar X;\mathrm{End}\,\mathbb C^N)$ and $Q\in\rho^3\mathrm{Diff}^1_b(\bar X;E)$. Put
$$\bar S := \inf_{p\in\partial X}\ \min\mathrm{Re}\,\mathrm{spec}\,S(p)\qquad\text{([Hin26c] (5.2))}.$$

*Remarks.* (a) $g_{00}\in\rho^2C^\infty(\bar X)$ by (K1): $\bar g^{-1}(dt_*,dt_*) = 0$, and the components of
$g^{-1}-\bar g^{-1}$ in the frame $\partial_{t_*},\partial_x$ lie in $\rho^2C^\infty(\bar X)$ (II.B Lemma 1.1, the
inverses). (b) The representation (1.1) is not unique: a zeroth-order term may be moved between $2\rho S\partial_{t_*}$
and $Q\partial_{t_*}$ ([Hin26c] Remark 5.2). $S|_{\partial X}$ is determined by $P_0$. Indeed, if $(S,Q)$ and $(S',Q')$
both represent $P_0$, the parts linear in $\sigma$ of the spectral families (Lemma 1.2) give $2\rho(S-S') = -(Q-Q')$; the
left side is of order 0, so $Q-Q'$ is a multiplication by an element of $\rho^3C^\infty$, and $S-S'\in\rho^2C^\infty$.

**Lemma 1.2 (the spectral family; [Hin26c] (5.10)).** Let $P_0$ be a stationary wave-type operator. Then $\hat P(\sigma)
:= e^{i\sigma t_*}P_0e^{-i\sigma t_*} = \hat P_0(0)+\sigma T+\sigma^2g_{00}$ with $T :=
2i\rho(\rho\partial_\rho-\frac32-S)-iQ$ on $\{\rho<\rho_1\}$, and $\hat P$ satisfies (H1) and (H2) of I.A and (H6) of
I.B, with this $g$. Conversely, if a family $\hat P(\sigma) = \hat P(0)+\sigma T+\sigma^2P_2$ satisfies (H1), (H2) and
(H6), then $P_0 := \hat P(0)+T\,i\partial_{t_*}-P_2\partial_{t_*}^2$ (I.B section 1.2) is a stationary wave-type operator
for the metric of (H6).

*Proof.* $e^{i\sigma t_*}\partial_{t_*}e^{-i\sigma t_*} = \partial_{t_*}-i\sigma$ acts as $-i\sigma$ on $t_*$-independent
sections, which gives the form and $T$; and $P_0 = \hat P(0)+T\,i\partial_{t_*}-g_{00}\partial_{t_*}^2$. The principal
symbol of $P_0$ at $-\sigma\,dt_*+\zeta$ is $\sigma_2(\hat P(0))(\zeta)+\sigma\,\sigma_1(T)(\zeta)+\sigma^2g_{00}$, as
$\sigma_1(i\partial_{t_*})(-\sigma\,dt_*+\zeta) = i\cdot i\cdot(-\sigma) = \sigma$. By I.B (1.1), $G(-\sigma\,dt_*+\zeta)
= G_0(\zeta)+\sigma\tau_1(\zeta)+\sigma^2g_{00}$, so Definition 1.1 (1) is equivalent to the three identities of (H1)
($\sigma_2(\hat P(0)) = G_0\,\mathrm{Id}$, $\sigma_1(T) = \tau_1\,\mathrm{Id}$, $P_2 = g_{00}\,\mathrm{Id}$), the parts
of different degree in $\sigma$ being separate. (H2): the first two equations of I.A (1.2) are the form of $T$ and $\hat
P(0) = \rho^2P^{(0)}$ with $P^{(0)}\in\mathrm{Diff}^2_b$, and $g_{00}\in\rho^2C^\infty$ is Remark (a). For the
normalisation of $P^{(0)}$: write spatial covectors as $\xi\,dr+\eta = \xi_b\frac{d\rho}\rho+\eta$, so $\xi_b = -r\xi$;
then $\sigma_2(\rho^2((\rho D_\rho)^2+\Delta_{\mathbb S^3})) = \rho^2(\xi_b^2+|\eta|^2) = \xi^2+r^{-2}|\eta|^2 = \bar
g^{-1}(\zeta,\zeta)$ for $\zeta = \xi\,dr+\eta$. The components of $\zeta$ in the frame $dt_*,dx$ are bounded by
$C(|\xi|+r^{-1}|\eta|)$, so by Remark (a), $G_0(\zeta)-\bar g^{-1}(\zeta,\zeta)\in\rho^2\cdot\rho^2P^{[2]}({}^bT^*\bar
X)$, $P^{[2]}$ the fibrewise quadratic polynomials with smooth coefficients. Hence
$\sigma_2(P^{(0)})-(\xi_b^2+|\eta|^2)\in\rho^2P^{[2]}$, and $P^{(0)}-((\rho D_\rho)^2+\Delta_{\mathbb
S^3})\mathrm{Id}\in\mathrm{Diff}^1_b+\rho^2\mathrm{Diff}^2_b$. (H6) is a hypothesis on $g$, which (K2) includes. The
converse reads the same identities backwards: the form of $T$ in (H2) gives (1.1). $\square$

So the stationary wave-type operators for $g$ are the operators whose spectral families satisfy (H1), (H2) and (H6), and
(K2) asks (H3)-(H5), (H7)-(H8) of them in addition.

### 1.2 Tensor wave operators

**Lemma 1.3 ([Hin26c] Example 5.4 at $n = 4$).** Identify $(p,q)$-tensors on $\mathbb R^{1+4}$ with $\mathbb C^N$-valued
functions, $N = 5^{p+q}$, by the coordinate frame of $(t_*,x^1,\dots,x^4)$ (for 1-forms the frame $dt_*,dx^i$ of I.A
section 1.2). Let $\nabla$ be the Levi-Civita connection of $g$ and $\square^{(p,q)}_g :=
-g^{\mu\nu}\nabla_\mu\nabla_\nu$. Then $\square^{(p,q)}_g$ is a stationary wave-type operator for $g$ with $S = 0$, so
$\bar S = 0$, and
$$\widehat{\square^{(p,q)}_g}(0)-\widehat{\square^{(p,q)}_{\bar g}}(0)\in\rho^4\mathrm{Diff}^2_b(\bar X;E).\tag{1.2}$$
For the scalar operator,
$$\square_{\bar g} = -2\partial_{t_*}\rho\big(\rho\partial_\rho-\tfrac32\big)+\rho^2\big(-(\rho\partial_\rho)^2+
2\rho\partial_\rho+\Delta_{\mathbb S^3}\big).\tag{1.3}$$

*Proof.* (1.3): $\square_{\bar g} = \partial_t^2-\partial_r^2-3r^{-1}\partial_r+r^{-2}\Delta_{\mathbb S^3}$
($\Delta_{\mathbb S^3}\ge0$). In $(t_*,r)$, $\partial_t = \partial_{t_*}$ and $\partial_r|_t =
\partial_r-\partial_{t_*}$, so $\square_{\bar g} =
2\partial_{t_*}\partial_r+3r^{-1}\partial_{t_*}-\partial_r^2-3r^{-1}\partial_r+r^{-2}\Delta_{\mathbb S^3}$; with
$\partial_r = -\rho(\rho\partial_\rho)$, $2\partial_{t_*}\partial_r+3\rho\partial_{t_*} =
-2\partial_{t_*}\rho(\rho\partial_\rho-\frac32)$, and $-\partial_r^2-3r^{-1}\partial_r =
-r^{-2}((r\partial_r)^2+2r\partial_r) = \rho^2(-(\rho\partial_\rho)^2+2\rho\partial_\rho)$.

In the coordinates $z = (t_*,x)$, $\bar g = -dt_*^2-2\omega_i\,dt_*\,dx^i+(\delta_{ij}-\omega_i\omega_j)dx^idx^j$,
$\omega := x/|x|$, from $dt = dt_*+\omega_i\,dx^i$ (D200; an earlier version printed $\delta_{ij}$ for the last
coefficient). Write $D_j := \partial_{x^j}|_{t_*}$; as $D_j = \omega_j\partial_r+r^{-1}Y_j$ with $Y_j$ smooth vector
fields on $\mathbb S^3$, $D_j\in\rho\mathcal V_b(\bar X)$, and $D_j$ maps $\rho^kC^\infty(\bar X)$ into
$\rho^{k+1}C^\infty(\bar X)$. The metric components of $\bar g$ are functions of $\omega$ (homogeneous of degree 0), so
the Christoffel symbols $\bar\Gamma$ lie in $\rho C^\infty(\bar X)$, and by (K1) and II.B Lemma 1.1 those of $g$ satisfy
$\Gamma-\bar\Gamma\in\rho^3C^\infty$ on $\{\rho<\rho_1\}$ (on the compact set $\{R^{-1}\le\rho\le\rho_1\}$, if it is
non-empty, every smooth function lies in $\rho^kC^\infty$ for every $k$, so the restriction $r>R$ in (K1) costs nothing;
D200), $g^{\mu\nu}-\bar g^{\mu\nu}\in\rho^2C^\infty$. In the frame, $\nabla_\mu = \partial_\mu+A_\mu$ on the tensor
indices, $A_\mu$ linear in $\Gamma$, and
$$\square^{(p,q)}_g = -g^{\mu\nu}\big((\partial_\mu+A_\mu)(\partial_\nu+A_\nu)-\Gamma^\lambda_{\mu\nu}(\partial_\lambda+
A_\lambda)\big).$$
The terms without $A$ form the scalar operator $\square_g$ acting componentwise. *The model.* For $\bar g$,
$\omega^\mu\bar\Gamma_{\kappa\mu\nu} = 0$ for all $\kappa,\nu$, where $\omega^\mu\partial_\mu = \partial_r$ ($\omega^0 :=
0$). In $\bar\Gamma_{\kappa\mu\nu} = \frac12(\partial_\mu\bar g_{\kappa\nu}+\partial_\nu\bar
g_{\kappa\mu}-\partial_\kappa\bar g_{\mu\nu})$, the first term gives $\omega^\mu\partial_\mu\bar g_{\kappa\nu} = 0$, the
components being homogeneous of degree 0 in $x$. For the others, $\omega^\mu\bar g_{\kappa\mu} = -\delta_{\kappa0}$ is
constant, so $\omega^\mu\partial_\nu\bar g_{\kappa\mu} = -T_{\kappa\nu}$ with $T_{\kappa\nu} :=
(\partial_\nu\omega^\mu)\bar g_{\kappa\mu}$, which is $r^{-1}(\delta_{\kappa\nu}-\omega_\kappa\omega_\nu)$ for spatial
$\kappa,\nu$ and 0 otherwise, as $\partial_\nu\omega^\mu = r^{-1}(\delta^\mu_\nu-\omega_\nu\omega^\mu)$; likewise
$\omega^\mu\partial_\kappa\bar g_{\mu\nu} = -T_{\nu\kappa}$. $T$ is symmetric, so $\omega^\mu\bar\Gamma_{\kappa\mu\nu} =
\frac12(-T_{\kappa\nu}+T_{\nu\kappa}) = 0$ (the eighty-second verifier's M1, D200). Hence $\omega^\mu\bar A_\mu = 0$. The
$\partial_{t_*}$-coefficient of $-2\bar g^{\mu\nu}\bar A_\mu\partial_\nu$ is $-2\bar g^{\mu t_*}\bar A_\mu =
2\omega^i\bar A_i = 0$, since $\bar g^{-1}(dt_*,dt_*) = 0$ and $\bar g^{-1}(dt_*,dx^i) = -\omega^i$. The remaining terms
with $\bar A$ are $-2\bar g^{\mu j}\bar A_\mu D_j\in\rho^2\mathrm{Diff}^1_b$ and zeroth-order terms in $\rho^2C^\infty$.
So $\square^{(p,q)}_{\bar g}$ is (1.3) componentwise plus an element of $\rho^2\mathrm{Diff}^1_b$, which is (1.1) with $S
= 0$, $Q = 0$, $g_{00} = 0$. *The difference.* $\square^{(p,q)}_g-\square^{(p,q)}_{\bar g}$ is a sum of:
$-(g^{\mu\nu}-\bar g^{\mu\nu})\partial_\mu\partial_\nu$; first-order terms $B^\lambda\partial_\lambda$ with
$B^\lambda\in\rho^3C^\infty$ (from $(g-\bar g)^{-1}\bar\Gamma$, $\bar g^{-1}(\Gamma-\bar\Gamma)$, $(g-\bar g)^{-1}A$,
$\bar g^{-1}(A-\bar A)$); and zeroth-order terms in $\rho^4C^\infty$. With $\partial_\mu\in\{\partial_{t_*},D_j\}$: the
$\partial_{t_*}^2$-term is $-(g^{-1}-\bar g^{-1})(dt_*,dt_*)\partial_{t_*}^2 = -g_{00}\partial_{t_*}^2$; the mixed terms
$\rho^2C^\infty\cdot\partial_{t_*}D_j$ lie in $\rho^3\mathrm{Diff}^1_b\,\partial_{t_*}$;
$B^{t_*}\partial_{t_*}\in\rho^3C^\infty\partial_{t_*}$; together they form $Q\partial_{t_*}$,
$Q\in\rho^3\mathrm{Diff}^1_b$. The spatial terms lie in $\rho^2(\rho\mathcal V_b)^2+\rho^3\rho\mathcal
V_b+\rho^4C^\infty\subset\rho^4\mathrm{Diff}^2_b$, which gives (1.2). $\sigma_2 = G\,\mathrm{Id}$ holds for every
connection Laplacian. $\square$

*Remark.* The source obtains $S\in\rho C^\infty$ and $\rho^3$ in (1.2), from the rate $r^{-1}$ of Kerr; (K1)'s $r^{-2}$
gives $S = 0$ and $\rho^4$ (section 6, (C4)).

### 1.3 $P_0$ on the compactifications

**Lemma 1.4 ([Hin26c] Lemma 5.7 at $n = 4$).** Let $P_0$ be a stationary wave-type operator. (a) $P_0\in\langle
x\rangle^{-2}\mathrm{Diff}^2_{3b}(\tilde M_0;E)$ over $\{r>r_0-2\delta_0\}$. (b) On $\Omega$, $P_0\in
x_I^2\rho_+^2\mathrm{Diff}^2_{e3b}(M;E)$. (c) Near $\mathscr I^+\cap\Omega$, in the coordinates $\rho_+ =
t_*^{-1}\in(0,1]$, $x_I = (t_*/r)^{1/2}$, $\omega$ of II.A section 1,
$$2x_I^{-2}\rho_+^{-2}P_0\equiv-\big(x_I\partial_{x_I}-3-2S\big)\big(x_I\partial_{x_I}-2\rho_+\partial_{\rho_+}\big)+
2x_I^2\Delta_{\mathbb S^3}\mod x_I\mathrm{Diff}^2_{eb}.\tag{1.4}$$

The weight $\rho_0^2$ of the source is omitted: $\Omega$ does not meet $I^0$, and $\rho_0$ is bounded below on it (II.A
section 1, (C)).

*Proof.* (a) ${}^{3b}T\tilde M_0$ is spanned by $\langle x\rangle\partial_t$, $\langle x\rangle\partial_{x^i}$ (II.A
Definition 2.1). Near $K^+$ away from sf, $\langle x\rangle$ is bounded above and below, and $P_0$ is a $t_*$-independent
differential operator with smooth coefficients in $x$, a combination of products of $\partial_{t_*} = \partial_t$ and
$\partial_{x^i}|_{t_*} = \partial_{x^i}|_t+\omega^i\partial_t$. Near sf, $r\partial_{t_*}$, $r\partial_r =
-\rho\partial_\rho$ and $\partial_\omega$ are 3b-vector fields, so $\mathcal V_b(\bar X)\subset\mathcal V_{3b}$ and
$\rho^2\mathrm{Diff}^2_b(\bar X)\subset r^{-2}\mathrm{Diff}^2_{3b}$. In (1.1),
$\partial_{t_*}\rho(\rho\partial_\rho-\frac32-S) = r^{-2}(r\partial_{t_*})(-r\partial_r-\frac32-S)$,
$Q\partial_{t_*}\in\rho^3\mathrm{Diff}^1_b\cdot r^{-1}(r\partial_{t_*})\subset r^{-4}\mathrm{Diff}^2_{3b}$ and
$g_{00}\partial_{t_*}^2\in\rho^2r^{-2}(r\partial_{t_*})^2$. (b), (c) Away from $\mathscr I^+$, (b) is (a), $x_I$ being
bounded below there and $\rho_+$ comparable to $\langle x\rangle^{-1}$ near $K^+\cap\iota^+$. Near $\mathscr I^+$, by
II.A section 2.3, $\partial_{t_*} = \rho_+(-\rho_+\partial_{\rho_+}+\frac12x_I\partial_{x_I})$ and $\partial_r =
-\frac12\rho_+x_I^2\cdot x_I\partial_{x_I}$, and $\rho = \rho_+x_I^2$. Hence
$$\rho\partial_{t_*} = \tfrac12x_I^2\rho_+^2\big(x_I\partial_{x_I}-2\rho_+\partial_{\rho_+}\big),
\qquad\rho\partial_\rho = -r\partial_r = \tfrac12x_I\partial_{x_I},\qquad\rho^2\partial_\omega = x_I^3\rho_+^2
\cdot x_I\partial_\omega,$$
each in $x_I^2\rho_+^2\mathcal V_{eb}$ or better ([Hin26c] (5.6)). As $\partial_{t_*}$ commutes with $\rho$, the first
term of (1.1) is $-2(\rho\partial_{t_*})(\rho\partial_\rho-\frac32-S) = -\frac12x_I^2\rho_+^2A(x_I\partial_{x_I}-3-2S)$
with $A := x_I\partial_{x_I}-2\rho_+\partial_{\rho_+}$. $A\rho = 2\rho-2\rho = 0$, so $A$ commutes with $S$, a function
of $(\rho,\omega)$, and $A(x_I\partial_{x_I}-3-2S) = (x_I\partial_{x_I}-3-2S)A$. Next, $\hat P_0(0) = \rho^2P^{(0)}$ with
$P^{(0)}\equiv(\rho D_\rho)^2+\Delta_{\mathbb S^3}$ modulo $\mathrm{Diff}^1_b+\rho\,\mathrm{Diff}^2_b$ (Lemma 1.2):
$2x_I^{-2}\rho_+^{-2}\rho^2\Delta_{\mathbb S^3} = 2x_I^2\Delta_{\mathbb S^3}$, while $2x_I^{-2}\rho_+^{-2}\rho^2(\rho
D_\rho)^2 = -\frac12x_I^2(x_I\partial_{x_I})^2$, and $2x_I^{-2}\rho_+^{-2}\rho^2\mathrm{Diff}^1_b =
2x_I^2\mathrm{Diff}^1_b(\bar X)\subset x_I\mathrm{Diff}^1_{eb}$ (as $x_I^2\partial_\omega = x_I\cdot
x_I\partial_\omega$), and likewise $2x_I^2\rho\,\mathrm{Diff}^2_b(\bar X)\subset x_I^2\mathrm{Diff}^2_{eb}$. Finally
$2x_I^{-2}\rho_+^{-2}Q\partial_{t_*}\in x_I^3\rho_+^2\mathrm{Diff}^2_{eb}$ and
$2x_I^{-2}\rho_+^{-2}g_{00}\partial_{t_*}^2\in x_I^2\rho_+^2\mathrm{Diff}^2_{eb}$. This is (1.4), uniformly on
$\{\rho_+\le1\}$, and $x_I^2\Delta_{\mathbb S^3}\in\mathrm{Diff}^2_{eb}$ gives (b) near $\mathscr I^+$. $\square$

The constant 3 in (1.4) is the source's $2$ in "$2(1+S)$" at $n = 4$.

## 2. Admissibility of the stationary model

### 2.1 Trapping

**Definition 2.1 ([Hin26c] Definition 5.8 at $n = 4$).** $P_0$ is *trapping admissible* if, for $z_0 = 1$ and $z_0 = -1$,
(Γ.4) of I.B section 1.5 holds with $\gamma_-<0$: there is a fibre inner product $h_\Gamma$ over $\Gamma_{z_0}$ with
$\sup_{\Gamma_{z_0}}\lambda_{\max}(p_1^\Gamma)<\frac12\nu_{\min}$. It is *strongly trapping admissible* if, for each
$z_0$ and every $\epsilon>0$, there is such an $h_\Gamma$ with $\sup_{\Gamma_{z_0}}\lambda_{\max}(p_1^\Gamma)<\epsilon$.

**Lemma 2.2.** (a) Under (K2), $P_0$ is trapping admissible. (b) At a point $-\sigma\,dt_*+\zeta$ with $\sigma>0$ and
$(x,\zeta/\sigma)\in\Gamma_1$, and with $\rho_\infty := \sigma^{-1}$,
$\rho_\infty\sigma_1(\mathrm{Im}_hP_0)(-\sigma\,dt_*+\zeta) = p_1(1)(x,\zeta/\sigma)$, $p_1$ as in I.B Lemma 1.1. So the
case $z_0 = 1$ of Definition 2.1 is the condition [Hin26c] (5.8) at the stationary extension of $\Gamma_1$, with
$\mathrm{Im}$ taken for the density $|dt_*\,dx|$ and the inner product $h_\Gamma$ extended to be stationary and
homogeneous of degree 0.

*Proof.* (a) (H7) assumes $\gamma_-<0$ in (Γ.4). (b) The density $|dt_*\,dx|$ is $t_*$-invariant, so
$(T\,i\partial_{t_*})^{*h} = i\partial_{t_*}T^{*h}$, and $i\partial_{t_*}$ commutes with $T^{*h}$; hence
$\mathrm{Im}_h(T\,i\partial_{t_*}) = (\mathrm{Im}_hT)\,i\partial_{t_*}$, while $g_{00}\partial_{t_*}^2$ is $h$-symmetric.
So $\sigma_1(\mathrm{Im}_hP_0)(-\sigma\,dt_*+\zeta) = \sigma_1(\mathrm{Im}_h\hat
P(0))(\zeta)+\sigma\,\sigma_0(\mathrm{Im}_hT)$, homogeneous of degree 1 in $(\sigma,\zeta)$; at $\sigma = 1$ it is
$p_1(1)(\zeta)$ by I.B Lemma 1.1 (b). $\square$

The source's [Hin26c] (5.9), a conjugation by an elliptic operator realising (5.8) for a fixed inner product ([Hin17]
Proposition 3.12), is not used here; the inner product $h_\Gamma$ enters the trapping estimates directly, as in I.B
section 6. The source's (5.8) uses the density $|dg|$. A change of density by a smooth factor $f$ changes
$\mathrm{Im}\,P_0$ by a first-order term with principal symbol $\frac12f^{-1}H_Gf$, so the two conditions need not
coincide pointwise; Definition 2.1 is the one I.B's trapping estimate uses.

### 2.2 The transition face

**Definition 2.3 ([Hin26c] Definition 5.10 at $n = 4$).** $P_0$ is *tf-admissible with weight* $\beta$ if its spectral
family is, in the sense of I.C Definition 5.1.

By I.C Corollary 5.2 (c), tf-admissibility with one weight in an indicial gap implies it for every weight in that gap.
I.C section 5.1 records how Definition 2.3 relates to the source's Definition 5.10.

### 2.3 Orders

Over $K^+$ the phase space is the 3b-cosphere bundle of the stationary model, ${}^{3b}S^*\tilde M_0$ (II.B section 2),
and $t_*$-translations act on it. On $\partial\Sigma^\pm$ the future field is $\pm\mathsf H$, $\mathsf H$ the field (1.4)
of II.B. The radial sets $\partial R_{\mathcal H^+}$ and $\partial R_{\partial K^+,\mathrm{in/out}}$ are those of II.B
Definitions 4.1 and 3.1. For a fibre inner product $h$ on $E_X$,
$$\vartheta_{\mathrm{out}} :=
\inf_{R^K_{\mathrm{out}}}\lambda_{\min}\big(-\rho_\infty\sigma^1_{3b}(r^2\mathrm{Im}_hP_0)\big),
\qquad\vartheta^{3b}_{\mathrm{in}} :=
\sup_{R^K_{\mathrm{in}}}\lambda_{\max}\big(\rho_\infty\sigma^1_{3b}(r^2\mathrm{Im}_hP_0)\big),\tag{2.1}$$
with $R^K_{\mathrm{in/out}} := \partial R_{\partial K^+,\mathrm{in/out}}$ (II.B Proposition 8.1) and $\rho_\infty :=
-\sigma_{3b}^{-1}$ ([Hin26c] (5.18) and after). $r^2\mathrm{Im}_hP_0\in\mathrm{Diff}^1_{3b}$ near sf by Lemma 1.4 (a), as
its principal symbol of order 2 vanishes, and its principal symbol is an $h$-self-adjoint endomorphism, degree 1 in the
fibres. $\vartheta_{\mathcal H}$ is the threshold of I.A (1.5) at the horizon: $\partial R_{\mathcal H^+}$ lies in
$\{\sigma = 0\}$, where $\sigma_1(\mathrm{Im}_hP_0) = \sigma_1(\mathrm{Im}_h\hat P(0))$ by the computation in the proof
of Lemma 2.2.

**Definition 2.4 ([Hin26c] Definition 5.11 at $n = 4$).** A $t_*$-translation-invariant $\mathsf s\in
C^\infty({}^{3b}S^*\tilde M_0)$, over $\{r>r_0-2\delta_0\}$, is *stationary-$P_0$-admissible with weights*
$\alpha_{\mathrm{sf}}$, $\alpha_K$ *and margin* $\eta\ge0$ if:

(1) (*Monotonicity.*) $\pm\mathsf H\mathsf s\le0$ on $\partial\Sigma^\pm$: $\mathsf s$ is non-increasing along the future
flow.

(2) (*Evenness.*) $\mathsf s(-\zeta) = \mathsf s(\zeta)$.

(3) (*Black hole and trapping.*) $\mathsf s$ is constant over $\{r\le r_\Gamma\}$, for some $r_\Gamma>r_h$ with
$\Gamma_{\pm1}\subset T^*\{r<r_\Gamma\}$.

(4) (*Horizon.*) $\mathsf s$ is constant near $\partial R_{\mathcal H^+}$, and $\mathsf s>\frac12+\vartheta_{\mathcal
H}+\eta$ there.

(5) (*Outgoing radial set.*) $\mathsf s$ is constant near $\partial R_{\partial K^+,\mathrm{out}}$, and $\mathsf
s+\alpha_{\mathrm{sf}}<\frac12(-1+\vartheta_{\mathrm{out}})+\alpha_K-\eta$ there.

(6) (*Incoming radial set.*) $\mathsf s$ is constant near $\partial R_{\partial K^+,\mathrm{in}}$, and $\mathsf
s+\alpha_{\mathrm{sf}}>\frac12(-1+\vartheta^{3b}_{\mathrm{in}})+\alpha_K+\eta$ there.

Each threshold is computed in a fibre inner product chosen for its radial set. The source states (1) as "non-decreasing"
(section 6, (C2)).

**Lemma 2.5 (inner products adapted to $S$; [Hin23c] Proposition B.1).** Let $S\in C^\infty(\bar X;\mathrm{End}\,\mathbb
C^N)$ and $\epsilon>0$. There is a fibre inner product $h$ on $E_X$ with $\lambda_{\min}(\frac12(S+S^{*h}))\ge\bar
S-\epsilon$ on $\partial X$. For every fibre inner product, $\inf_{\partial X}\lambda_{\min}(\frac12(S+S^{*h}))\le\bar
S$.

*Proof.* For $p\in\partial X$ write $S(p) = A(D+N)A^{-1}$ in Jordan form, $D$ diagonal and $N$ with entries 0 or 1 on the
first superdiagonal. With $\Lambda := \mathrm{diag}(1,\delta^{-1},\dots,\delta^{1-N})$, $\Lambda N\Lambda^{-1} = \delta
N$. Put $h_p(v,w) := \langle\Lambda A^{-1}v,\Lambda A^{-1}w\rangle_{\mathbb C^N}$; for $u := \Lambda A^{-1}v$,
$\mathrm{Re}\,h_p(S(p)v,v) = \mathrm{Re}\langle(D+\delta
N)u,u\rangle\ge(\min\mathrm{Re}\,\mathrm{spec}\,S(p)-\delta)|u|^2\ge(\bar S-\delta)h_p(v,v)$. As
$\lambda_{\min}(\frac12(S+S^{*h})) = \min_{h(v,v) = 1}\mathrm{Re}\,h(Sv,v)$, the constant inner product $h_p$ gives
$\lambda_{\min}\ge\bar S-2\delta$ on a neighbourhood $U_p$ of $p$, by continuity of
$(q,v)\mapsto\mathrm{Re}\,h_p(S(q)v,v)$ on $\{h_p(v,v) = 1\}$. Take a finite cover of $\partial X$ by such $U_{p_k}$, a
subordinate partition of unity $\chi_k$ on a neighbourhood of $\partial X$, and $h := \sum_k\chi_kh_{p_k}$ there,
extended to $\bar X$ by a convex combination with a fixed inner product away from $\partial X$. Then
$\mathrm{Re}\,h(Sv,v) = \sum_k\chi_k\mathrm{Re}\,h_{p_k}(Sv,v)\ge(\bar S-2\delta)h(v,v)$ on $\partial X$; $\delta :=
\epsilon/2$. Conversely, the eigenvalues of $S(p)$ depend continuously on $p$, so $\bar S$ is attained: $S(p_*)v = \mu
v$, $\mathrm{Re}\,\mu = \bar S$. Then $\mathrm{Re}\,h(S(p_*)v,v) = \bar S\,h(v,v)$ for every $h$. $\square$

**Lemma 2.6 ([Hin26c] Lemma 5.12 at $n = 4$).** For every fibre inner product $h$, $\vartheta_{\mathrm{out}} =
2\inf_{\partial X}\lambda_{\min}(\frac12(S+S^{*h}))\le2\bar S$, and for the $h$ of Lemma 2.5,
$\vartheta_{\mathrm{out}}\ge2\bar S-2\epsilon$. Moreover $\vartheta^{3b}_{\mathrm{in}} = \vartheta_{\mathrm{in}}$, the
threshold of I.A (1.5) at $R_{\mathrm{in}}$.

*Proof.* Use the 3b-covectors of II.B (3.1), $\sigma_{3b}\frac{dt_*}r+\xi_{3b}\frac{dr}r+\eta_{3b}$, so that
$\sigma_1(r\partial_{t_*}) = i\sigma_{3b}$, $\sigma_1(r\partial_r) = i\xi_{3b}$, and $-\sigma\,dt_*+\xi\,dr+\eta$ has
$\sigma_{3b} = -r\sigma$, $\xi_{3b} = r\xi$. Compute $\sigma^1_{3b}(r^2\mathrm{Im}_hP_0)$ at sf term by term in (1.1).

(i) $-2\partial_{t_*}\rho(\rho\partial_\rho-\frac32)$ is symmetric for $|dt_*\,dx| = \rho^{-5}|dt_*\,d\rho\,d\omega|$:
$(\rho\partial_\rho)^* = -\rho\partial_\rho+4$ for $\rho^{-5}d\rho$, $\partial_{t_*}^* = -\partial_{t_*}$, so
$(\partial_{t_*}\rho(\rho\partial_\rho-c))^* = -(-\rho\partial_\rho+4-c)\rho\partial_{t_*} =
\partial_{t_*}\rho(\rho\partial_\rho-3+c)$, which equals $\partial_{t_*}\rho(\rho\partial_\rho-c)$ exactly for $c =
\frac32$. With $h$, the adjoint acquires $H^{-1}[\,\cdot\,,H]$-terms. As $H$ is $t_*$-independent and $\rho\partial_\rho
H\in\rho C^\infty$, they lie in $\rho\cdot\rho\,\partial_{t_*}C^\infty\subset r^{-3}\mathrm{Diff}^1_{3b}$, which vanish
at sf after the factor $r^2$.

(ii) $2\partial_{t_*}\rho S = 2\rho S\partial_{t_*}$ has $\mathrm{Im}_h = \frac1i\rho(S+S^{*h})\partial_{t_*}$, as
$(2\rho S\partial_{t_*})^{*h} = -2\rho S^{*h}\partial_{t_*}$. Its symbol at $-\sigma\,dt_*+\zeta$ is
$\frac1i\rho(S+S^{*h})(-i\sigma) = -\rho\sigma(S+S^{*h}) = \rho^2\sigma_{3b}(S+S^{*h})$, so $r^2$ times it is
$\sigma_{3b}(S+S^{*h})$, and $\mp\rho_\infty$ times that is $\pm(S+S^{*h})$.

(iii) $r^2\mathrm{Im}_h\hat P_0(0)\in\mathrm{Diff}^1_b(\bar X)$ (I.A Remark (a) after (H5)). Its 3b-principal symbol is
that of a spatial operator, linear in $(\xi_{3b},\eta_{3b})$. At $\partial R_{\partial K^+,\mathrm{out}}$, where
$\xi_{3b} = \eta_{3b} = 0$, it vanishes. At $\partial R_{\partial K^+,\mathrm{in}}$, where $\xi_{3b} = 2\sigma_{3b}$,
$\eta_{3b} = 0$: write the scattering symbol of $\rho^{-1}\mathrm{Im}_h\hat P_0(0)\in\rho\mathrm{Diff}^1_b =
\mathrm{Diff}^1_{\mathrm{sc}}$ at $\partial X$, at $\xi\,dr$, as $\xi a$; then $\sigma(r^2\mathrm{Im}_h\hat
P_0(0))(\xi\,dr) = r\xi a = \xi_{3b}a$ at sf, and $\rho_\infty\xi_{3b}a = -\hat\xi a = -2a$, which is $p_{\mathrm{in}} =
\sigma(\rho^{-1}\mathrm{Im}_h\hat P(0))|_{\xi = -2,\eta = 0}$ of I.A (1.5).

(iv) $Q\partial_{t_*},g_{00}\partial_{t_*}^2\in r^{-4}\mathrm{Diff}^2_{3b}$ (Lemma 1.4), so $r^2\mathrm{Im}_h$ of them
lies in $r^{-2}\mathrm{Diff}^1_{3b}$ and vanishes at sf.

Hence $-\rho_\infty\sigma^1_{3b}(r^2\mathrm{Im}_hP_0) = S+S^{*h}$ at $\partial R_{\partial K^+,\mathrm{out}}$, whose base
is all of $\partial K^+\cap\mathrm{sf}\cong\partial X$, and $\rho_\infty\sigma^1_{3b}(r^2\mathrm{Im}_hP_0) =
p_{\mathrm{in}}-(S+S^{*h})$ at $\partial R_{\partial K^+,\mathrm{in}}$. The first gives $\vartheta_{\mathrm{out}}$ by
Lemma 2.5, the second $\vartheta^{3b}_{\mathrm{in}} = \sup\lambda_{\max}(p_{\mathrm{in}}-(S+S^{*h})) =
\vartheta_{\mathrm{in}}$. $\square$

So the thresholds of Definition 2.4 at $\partial K^+$ are those of I.A (1.5) and I.B section 1.4 written in 3b-terms:
$\frac12(-1+\vartheta_{\mathrm{out}})\approx-\frac12+\bar S$ and $\frac12(-1+\vartheta_{\mathrm{in}})$.

### 2.4 The spaces and $\aleph$-admissibility

For an order $\mathsf s$, $k\in\mathbb N_0$ and weights, $H^{(\mathsf
s;k),(\alpha_{\mathrm{sf}},\alpha_K)}_{3b;b}(\Omega;E)^{\bullet,-}$ is the space of II.A section 7 (the restrictions to
$\{r>r_0\}$ of elements of the weighted mixed 3b-space supported in $\{t_*\ge1\}$), with local defining functions
$\rho_{\mathrm{sf}} = r^{-1}$, $\rho_K = r/(t_*+r)$ on $\Omega$ ([Hin26c] (5.21)). On $\Omega$, $r\partial_x$ and
$t_*\partial_{t_*}$ form a global frame of $\mathcal V_b$ (II.A section 2.1), so b-regularity is tested by
$(t_*\partial_{t_*})^j(r\partial_x)^\alpha$.

**Definition 2.7 ([Hin26c] Definition 5.13 at $n = 4$).** Let $\aleph,\delta\ge0$, $\alpha_{\mathrm{sf}}\in\mathbb R$.
$P_0$ is *$\aleph$-admissible with sf-weight $\alpha_{\mathrm{sf}}$ and sf-loss $\delta$* if, for every
stationary-$P_0$-admissible order $\mathsf s$ with weights $\alpha_{\mathrm{sf}}$, $-\aleph$ and margin 0: (1) $P_0$ is
trapping admissible; (2) $P_0$ is tf-admissible with weight $\alpha_{\mathrm{sf}}+2$; (3) for every $k\in\mathbb N_0$ and
$f\in H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}(\Omega;E)^{\bullet,-}$, the forward solution of $P_0u = f$ lies
in $H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}-\delta,-\aleph)}_{3b;b}(\Omega;E)^{\bullet,-}$, with
$$\|u\|_{H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}-\delta,-\aleph)}_{3b;b}}
\le C_k\|P_0u\|_{H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}}.\tag{2.2}$$
The relaxed version with margin $d_\aleph\ge0$ ([Hin26c] Remark 5.14) asks (1)-(2) for orders with margin $d_\aleph$ and
(3) with $\mathsf s-d_\aleph$ in place of $\mathsf s$ on the left.

The weight in (2) is the source's $\alpha_{\mathrm{sf}}+\frac32$ at $n = 4$: by I.C Remark (a) after (TF), the spatial
weight $\alpha$ of an $L^2(|dx|)$-based space is the b-weight $\alpha+2$ at $n = 4$ (that is, $\alpha+\frac n2$). In
particular $\alpha_{\mathrm{sf}}+2$ lies in an indicial gap of $\hat P_0(0)$; for the scalar wave operator the gap is
$(0,2)$, the indicial roots of (1.3) at $\ell = 0$ being $0$ and $2$, so $\alpha_{\mathrm{sf}}\in(-2,0)$, where the
source has $(-\frac32,-\frac12)$.

## 3. Asymptotically stationary metrics and wave-type operators

From here on the stationary metric of section 1 is written $g_0$, and $G_0(\zeta) := g_0^{-1}(\zeta,\zeta)$ on spacetime
covectors (on spatial covectors, $G_0$ of I.A is its restriction). On $\Omega$ we use the e3b-structure of II.A section
2.4, the weight $w_{(\alpha)} = x_I^{2\alpha_I}\rho_+^{\alpha_+}\rho_K^{\alpha_K}$ and the spaces
$C^{(d_0;k),(\cdot)}_{e3b;b}$ of II.A Definition 8.1, for sections of a bundle in a fixed smooth frame.

**Definition 3.1 ([Hin26c] Definition 5.15 at $n = 4$).** Let $\ell_I\in[0,\frac12]$, $\ell_+\in[0,1]$, $\ell_K\ge0$,
$d_0,k\in\mathbb N_0$.
$$\tilde{\mathcal G}^{(d_0;k),(2\ell_I,\ell_+,\ell_K)}_{e3b;b} := x_I^{-2}\rho_+^{-2}
C^{(d_0;k),(2\ell_I,\ell_+,\ell_K)}_{e3b;b}(\Omega;S^2\,{}^{e3b}T^*_\Omega M),
\qquad\mathcal G^{(d_0;k),(2\ell_I,\ell_+,\ell_K)}_{e3b;b} := g_0+
\tilde{\mathcal G}^{(d_0;k),(2\ell_I,\ell_+,\ell_K)}_{e3b;b},$$
with the norm of $C^{(d_0;k),(2\ell_I+2,\ell_++2,\ell_K)}_{e3b;b}$ on the first and the induced metric on the second.
Subscripts are dropped for $d_0 = 0$ ("e3b") or $k = 0$ ("b").

*Remarks.* (a) $g_0-\bar g\in x_I^{-2}\rho_+^{-2}C^{\infty,(2,2,0)}(\Omega;S^2\,{}^{e3b}T^*_\Omega M)$ by II.B (1.2), as
$\rho_0$ is bounded below on $\Omega$, so $g_0-\bar g$ lies in $\tilde{\mathcal G}^{\infty,(2\ell_I,\ell_+,0)}$ for all
admissible $\ell_I,\ell_+$; the source has the weights $(1,0,0)$ for Kerr ([Hin26c] Remark 5.17). (b) If
$h\in\tilde{\mathcal G}^{0,(0,0,0)}_{e3b}$ has small norm, then $x_I^2\rho_+^2(g_0+h)$ is a non-degenerate section of
$S^2\,{}^{e3b}T^*_\Omega M$ of Lorentzian signature, and $g_0+h$ is a Lorentzian metric on $\Omega^\circ$. Indeed
$x_I^2\rho_+^2g_0$ is non-degenerate of signature $(1,4)$ and continuous up to the boundary on the compact closure of
$\Omega$ in ${}^{e3b}T^*M$ (II.B Lemma 1.1 (3)), so its inverse is bounded, and $x_I^2\rho_+^2h$ is small in $C^0$. The
source prints $x_I^{-2}\rho_+^{-2}$ here (section 6, (C1)). $g_0+h$ is time-oriented by Lemma 3.2 below, which makes
$dt^\flat_*$ past timelike when $h$ is small in $\tilde{\mathcal G}^{0,(2\ell_I,0,0)}$, $\ell_I>0$.

**Lemma 3.2 ([Hin26c] Lemma 5.16 at $n = 4$).** Let $\ell := \ell_I\in(0,\frac12]$ and $r^\natural := \frac12(r_0+r_2)$.
There are $\epsilon_G>0$, $C'\in(0,1)$, $r'_0>r_2$ and $t^\flat_*\in C^\infty(\Omega^\circ)$ with

(a) $t^\flat_* = t_*(1-(t_*/r)^\ell)$ where $t_*/r$ is small;

(b) $C't_*\le t^\flat_*\le t_*$;

(c) $t^\flat_* = C't_*+C'r'_0$ for $r\le r'_0-1$;

such that for every $g = g_0+h$ with $\|h\|_{\tilde{\mathcal G}^{0,(2\ell,0,0)}_{e3b}}<\epsilon_G$: (1) $dr$ is future
timelike for $g$ on $\{r_0\le r\le r^\natural\}$; (2) $dt^\flat_*$ is past timelike for $g$ on $\Omega^\circ$.

*Proof.* *Bounds on $g^{-1}$.* By II.A Lemma 2.5, near $\mathscr I^+$ the covectors $x_I^{-1}dt_*$, $x_Idr$, $r\,d\omega$
span $\rho_+^{-1}x_I^{-1}C^\infty({}^{eb}T^*)$, so the pointwise dual vectors $x_I\partial_{t_*}$, $x_I^{-1}\partial_r$,
$r^{-1}\partial_\omega$ span $\rho_+x_IC^\infty({}^{eb}T)$, and the symmetric products
$$\rho_I\partial_{t_*}^2,\quad\partial_{t_*}\otimes_s\partial_r,\quad x_I\partial_{t_*}\otimes_sr^{-1}\partial_\omega,
\quad\rho_I^{-1}\partial_r^2,\quad x_I^{-1}\partial_r\otimes_sr^{-1}\partial_\omega,
\quad r^{-1}\partial_\omega\otimes_sr^{-1}\partial_\omega,\qquad\rho_I := x_I^2 = t_*/r,$$
span $x_I^2\rho_+^2C^\infty(S^2\,{}^{eb}T)$. As $x_I^2\rho_+^2g_0$ has a bounded inverse, $g^{-1}-g_0^{-1}$ (by a Neumann
series) lies in $x_I^2\rho_+^2\cdot x_I^{2\ell}C^0(S^2\,{}^{e3b}T)$ with norm $\le C\|h\|$; and $g_0^{-1}-\bar g^{-1}\in
x_I^4\rho_+^4C^\infty(S^2\,{}^{e3b}T)$ (II.B Lemma 1.1, the inverses). Since $\rho_+\le1$ on $\Omega$, the coefficients
of $g^{-1}-\bar g^{-1}$ in the basis above are bounded by $C_1(\epsilon_G+\rho_I^{1-\ell})\rho_I^\ell$. Away from
$\mathscr I^+$, where $x_I$ is bounded below, the same membership gives $|(g^{-1}-g_0^{-1})(\alpha,\alpha)|\le
C\epsilon_G(|\alpha_t|+|\alpha_r|+r^{-1}|\alpha_\omega|)^2$ for $\alpha = \alpha_tdt+\alpha_rdr+\alpha_\omega$: near
$K^+\cap\iota^+$ the 3b-vectors $r\partial_t$, $r\partial_x$ span ${}^{3b}T$ and $x_I^2\rho_+^2\sim r^{-2}$ there; near
$K^+$ away from sf, $\partial_t,\partial_x$ span it and $x_I,\rho_+$ are bounded below; near $\iota^+\cap\mathscr I^+$
with $x_I\ge c$, $dt$ and $dr$ evaluated on the eb-frame are $O(t+r) = O(\rho_+^{-1}x_I^{-2})$.

*The function near $\mathscr I^+$.* With $\rho := \rho_I$ and $F_1(\rho) := 1-\rho^\ell$, $d(t_*F_1(\rho_I)) =
A\,dt_*+B\,dr$ with $A = 1-(1+\ell)\rho^\ell$, $B = \ell\rho^{\ell+1}$, as $d\rho_I = \rho_I(dt_*/t_*-dr/r)$. Since $\bar
g^{-1}(dt_*,dt_*) = 0$, $\bar g^{-1}(dt_*,dr) = -1$ and $\bar g^{-1}(dr,dr) = 1$, the covector $A\,dt_*+B\,dr$ has $\bar
g^{-1}$-square $-2AB+B^2$, and $-2AB\le-2\ell\rho^{\ell+1}(1-2\rho^\ell)$ as $1+\ell\le2$. The basis elements evaluated
on $(A\,dt_*+B\,dr)^{\otimes2}$ give $\rho A^2$, $O(|AB|)$, $0$, $\rho^{-1}B^2$, $0$, $0$, all at most $\rho$ in size for
$\rho\le1$. So
$$g^{-1}(d(t_*F_1),d(t_*F_1))\le-2\ell\rho^{\ell+1}(1-2\rho^\ell)+\rho^{2\ell+2}+C_2(\epsilon_G+
\rho^{1-\ell})\rho^{\ell+1}\le-\ell\rho^{\ell+1}$$
for $\rho\le\rho_a$ and $\epsilon_G\le\epsilon_a$, with $\rho_a,\epsilon_a$ small depending on $\ell$ and $C_2$ (the
error is of the order of the main term, which is why $\epsilon_G$ must be small). This is timelike. It is past directed:
$V := t\partial_t+r\partial_r$ is future timelike for $g$ on $\{r\ge R_2\}\cap\Omega$ (II.B section 7 for $g_0$; for $g$,
$|h(V,V)|\le C\epsilon_Gx_I^{2\ell}rt_*$ against $|g_0(V,V)|\ge\frac12(t_*^2+2t_*r)$, and the orientation is continuous
along $g_0+\tau h$), and $d(t_*F_1)(V) = At_*+Br>0$, as $Vt_* = t_*$, $Vr = r$; a covector that is positive on a future
timelike vector and is timelike is past timelike.

*The function away from $\mathscr I^+$.* $dt = dt_*+dr$ has $\bar g^{-1}(dt,dt) = -1$, $|(g_0^{-1}-\bar
g^{-1})(dt,dt)|\le Cr^{-2}$ by (K1), and $|(g^{-1}-g_0^{-1})(dt,dt)|\le C\epsilon_G$ where $x_I\ge c$, by the bounds
above. So $g^{-1}(dt,dt)\le-\frac12$ on $\{r\ge r'_0-1, x_I\ge c\}$ for $r'_0$ large and $\epsilon_G$ small, and $dt$ is
past timelike there ($dt(V) = t>0$). On $\{r_0\le r\le r'_0+1\}$, $g_0^{-1}(dt_*,dt_*) = g_{00}\le-c_0<0$ by (H6) and
compactness, so $g^{-1}(dt_*,dt_*)\le-\frac12c_0$ for $\epsilon_G$ small, and $dt_*$ is past timelike there, for $g_0$ by
(H6) and for $g$ by continuity.

*Gluing.* Fix $C$ large (below), $C' := (1-C^{-\ell})/(1+C)$, and $F_2(\rho) := C'(1+\rho^{-1})$, so $t_*F_2(\rho_I) =
C'(t_*+r) = C't$ and $F_1 = F_2$ at $\rho = 1/C$. The function $\varphi(\rho) := F_2(\rho)-F_1(\rho)$ satisfies
$\varphi(1/C) = 0$ and $\varphi'(\rho) = -C'\rho^{-2}+\ell\rho^{\ell-1}<0$ on $(0,2/C]$ for $C$ large (as
$C'\ge(4C)^{-1}$ and $\ell\rho^{\ell+1}\le\ell(2/C)^{\ell+1}$), and $F_1/F_2\ge\frac32$ at $\rho = 2/C$. Let $m_\kappa$
be smooth, even, convex, with $m_\kappa(y) = |y|$ for $|y|\ge\kappa$, and $M(a,b) := \frac12(a+b-m_\kappa(a-b))$, a
smooth minimum: $M = \min(a,b)$ when $|a-b|\ge\kappa$, and $\partial_aM,\partial_bM\in[0,1]$ with
$\partial_aM+\partial_bM = 1$. Put $F := \exp M(\log F_1,\log F_2)$ with $\kappa\le\frac14$ small; then $F = F_1$ on
$(0,\rho_-]$ and $F = F_2$ on $[\rho^+,\infty)$ for some $\rho_-<1/C<\rho^+<2/C$, and $F'/F = \theta
F_1'/F_1+(1-\theta)F_2'/F_2$ with $\theta\in[0,1]$. Hence
$$d(t_*F(\rho_I)) = F\big[(1+\rho F'/F)dt_*-\rho^2(F'/F)dr\big] = F\Big[\theta\frac{d(t_*F_1)}{F_1}+
(1-\theta)\frac{d(t_*F_2)}{F_2}\Big],$$
a positive combination of two past timelike covectors, hence past timelike, wherever both are. On the transition interval
$[\rho_-,\rho^+]$, choosing $\kappa$ so small that $\rho_-\ge1/(2C)$: $d(t_*F_1)$ is past timelike as
$\rho^+\le2/C\le\rho_a$, and $d(t_*F_2) = C'dt$ is, by the previous paragraph with $c := (2C)^{-1/2}$ (so $x_I =
\rho_I^{1/2}\ge c$) and $\epsilon_G$ small depending on $C$. Let $\tilde R(r)$ be a smooth maximum of $r$ and $r'_0$,
equal to $r'_0$ for $r\le r'_0-1$ and to $r$ for $r\ge r'_0+1$, with $\tilde R'\in[0,1]$. Define
$$t^\flat_* := C'\big(t_*+\tilde R(r)\big)\ \text{on}\ \{r\le Ct_*/2\},\qquad t^\flat_* :=
t_*F(t_*/r)\ \text{on}\ \{r\ge r'_0+1\}.$$
For $C>2(r'_0+1)$ and $t_*\ge1$ the overlap $\{r'_0+1\le r\le Ct_*/2\}$ is where both are defined, and there both equal
$C'(t_*+r)$, as $\rho_I\ge2/C$ gives $F = F_2$. On $\{r\le Ct_*/2\}$, $dt^\flat_* = C'((1-\tilde R')dt_*+\tilde R'\,dt)$,
a positive combination of $dt_*$ (past timelike for $r\le r'_0+1$) and $dt$ (past timelike for $r\ge r'_0-1$, $x_I\ge c$,
as $\rho_I\ge2/C$ there). On $\{r\ge r'_0+1\}$ the previous paragraph applies. This proves (2), and (a), (c) hold by
construction. (b): $t_*F_1\in[(1-C^{-\ell})t_*,t_*]$ for $\rho\le1/C$, $t_*F_2 =
C't_*(1+\rho^{-1})\in[C't_*,(1-C^{-\ell})t_*]$ for $\rho\ge1/C$. A smooth convex even $m_\kappa$ equal to $|y|$ for
$|y|\ge\kappa$ satisfies $|y|\le m_\kappa\le\kappa$ on $[-\kappa,\kappa]$, so $e^{-\kappa/2}\min(F_1,F_2)\le
F\le\min(F_1,F_2)$; on the transition interval $\min(F_1,F_2)\ge C'(1+C/2)$ (for $C$ large, $F_1\ge\frac12$ there, and
$C'(1+C/2)\le\frac12$ as $C^\ell\le2+C$ for $\ell\le1$; D201), and $e^{-1/8}(1+C/2)\ge1$, so $C'\le F\le1$ (D200; an
earlier version said that $F$ lies between $F_1$ and $F_2$, which is false inside the transition). And $C'(t_*+\tilde
R)\le C'(t_*+r'_0+r)\le t_*$ where $r\le Ct_*/2$ and $r'_0\le C/2$. (1): $g_0^{-1}(dr,dr) = G_0(dr)<0$ on
$\{r_0-2\delta_0<r<r_2\}$ by (H4), so $\le-c_1<0$ on the compact $\{r_0\le r\le r^\natural\}$; the perturbation is
$O(\epsilon_G)$ there, and $dr$ is future timelike for $g_0$ ($\nabla r$ is future timelike, I.B section 1.2) and for $g$
by continuity. $\square$

The source takes "a smoothing" of the piecewise function; the gluing above makes it explicit (section 6, (C5)). By (b),
$\Omega_* := \mathrm{cl}_M\{t^\flat_*\ge1\}\subset\Omega$ ([Hin26c] (6.2)).

**Definition 3.3 ([Hin26c] Definition 5.18 at $n = 4$).** Let $\aleph,\delta\ge0$ and $\ell_I\in(0,\frac12]$,
$\ell_+>\delta$, $\ell_K>\aleph$ ((5.23)). Let $P_0$ be $\aleph$-admissible with sf-weight $\alpha_{\mathrm{sf}}$ and
sf-loss $\delta$. $P\in\mathrm{Diff}^2(\Omega^\circ;E)$ is *admissible* (relative to $P_0$) *of class*
$((d_0;k),(2\ell_I,\ell_+,\ell_K))$ if:

(1) $\sigma_2(P) = G\,\mathrm{Id}$, $G(\zeta) = g^{-1}(\zeta,\zeta)$ for some $g\in\mathcal
G^{(d_0;k),(2\ell_I,\ell_+,\ell_K)}_{e3b;b}$;

(2) with a cut-off $\chi_I = \chi_I(x_I)$, equal to 1 near 0 and supported in $\{x_I<1\}$, there are
$$p_0,\ \tilde p_1\in\rho_+^{\ell_+}C^{k+d_0}_b(\mathscr I^+\cap\Omega;\mathrm{End}\,\mathbb C^N)\tag{3.1}$$
(extended to $\mathrm{supp}\,\chi_I$ independently of $x_I$) with
$$\tilde P := P-\Big[P_0+\chi_I\tfrac12x_I^2\rho_+^2\big(2\tilde p_1(x_I\partial_{x_I}-2\rho_+\partial_{\rho_+})+
p_0\big)\Big]\in x_I^2\rho_+^2C^{(d_0;k),(2\ell_I,\ell_+,\ell_K)}_{e3b;b}\mathrm{Diff}^2_{e3b}(\Omega;E);\tag{3.2}$$

(3) there is a splitting $\mathbb C^N = \bigoplus_{j = 1}^J E_j$, over $\partial X$, in which $p_1 := S|_{\partial
X}+\tilde p_1$ is lower triangular with diagonal blocks of real spectrum, and $p_0$ is strictly lower triangular.

$P$ is *weakly admissible* if only $\ell_I\in(0,\frac12]$, $\ell_+>0$, $\ell_K>0$ ((5.26)).

Here $S|_{\partial X}$ is pulled back to $\mathscr I^+$ along its fibration over $\partial X\cong Y^+$ (II.A section 1),
and the operators in (3.2) are those of II.A section 8.2 with coefficients in the stated space.

**Lemma 3.4 ([Hin26c] (5.27) at $n = 4$).** For $P$ as in Definition 3.3, near $\mathscr I^+\cap\{\rho_+\le1\}$,
$$2x_I^{-2}\rho_+^{-2}P-\Big[-\big(x_I\partial_{x_I}-3-2p_1\big)\big(x_I\partial_{x_I}-2\rho_+\partial_{\rho_+}\big)+
2x_I^2\Delta_{\mathbb S^3}+p_0\Big]\in C^{(d_0;k),(2\ell_I,0)}_{eb;b}\mathrm{Diff}^2_{eb}.\tag{3.3}$$
The characteristic exponents of $x_I\partial_{x_I}-3-2p_1$ are $3+2\mu$, $\mu\in\mathrm{spec}\,p_1$ (the source's
$2(1+\mu)$).

*Proof.* Where $\chi_I = 1$, $2x_I^{-2}\rho_+^{-2}P = 2x_I^{-2}\rho_+^{-2}P_0+2\tilde
p_1(x_I\partial_{x_I}-2\rho_+\partial_{\rho_+})+p_0+2x_I^{-2}\rho_+^{-2}\tilde P$. Insert (1.4); $S-S|_{\partial
X}\in\rho C^\infty = x_I^2\rho_+C^\infty$, so replacing $S$ by $S|_{\partial X}$ costs $x_I\mathrm{Diff}^1_{eb}$, and
$-(x_I\partial_{x_I}-3-2S|_{\partial X})A+2\tilde p_1A = -(x_I\partial_{x_I}-3-2p_1)A$ with $A =
x_I\partial_{x_I}-2\rho_+\partial_{\rho_+}$. The remainders are $x_I\mathrm{Diff}^2_{eb}\subset
C^{\infty,(2\ell_I,0)}\mathrm{Diff}^2_{eb}$ (as $2\ell_I\le1$) and $2x_I^{-2}\rho_+^{-2}\tilde P\in
x_I^{2\ell_I}\rho_+^{\ell_+}C^{(d_0;k)}_{e3b;b}\mathrm{Diff}^2_{eb}$ (near $\mathscr I^+$ the e3b- and eb-structures
agree). $\square$

**Definition 3.5 ([Hin26c] Definition 5.20).** $\bar p_1 := \inf_{p\in\mathscr
I^+}\min\mathrm{Re}\,\mathrm{spec}\,p_1(p)$.

The lower bounds on $\ell_+$, $\ell_K$ in (5.23) matter only when estimates for $P$ are closed with the mapping
properties of $P_0$ ([Hin26c] Remark 5.21); the regularity of $p_0$, $\tilde p_1$ in (3.1) is the source's choice
([Hin26c] Remark 5.22).

**Definition 3.6 ([Hin26c] Definition 5.23).** $\|P-P_0\|_{(d_0;k),(2\ell_I,\ell_+,\ell_K)}$ is the sum of the norms of
$p_0$, $\tilde p_1$ in (3.1) and of a representation of $\tilde P$ in (3.2) (II.A section 8.2); on $\Omega'\subset\Omega$
the suprema are taken over $\Omega'$.

**Lemma 3.7.** $\|g-g_0\|_{\tilde{\mathcal G}^{(d_0;k),(2\ell_I,\ell_+,\ell_K)}_{e3b;b}}\le
C\|P-P_0\|_{(d_0;k),(2\ell_I,\ell_+,\ell_K)}$ when the right side is small, and likewise on subsets.

*Proof.* The bracket in (3.2) has the principal symbol of $P_0$, the $\chi_I$-terms being of first order. So $G-G_0 =
\sigma_2(\tilde P)$, and $g^{-1}-g_0^{-1}\in x_I^2\rho_+^2C^{(d_0;k),(2\ell_I,\ell_+,\ell_K)}_{e3b;b}(S^2\,{}^{e3b}T)$
with norm $\le C\|\tilde P\|$. Then $g-g_0 = -g_0(g^{-1}-g_0^{-1})g_0+\dots$, a convergent Neumann series in
$x_I^{-2}\rho_+^{-2}C^{(d_0;k),(2\ell_I,\ell_+,\ell_K)}_{e3b;b}$, by II.A Lemma 8.2 (c)-(d). $\square$

## 4. The global dynamics of perturbed metrics

Fix $\ell_I\in(0,\frac12]$, $\ell_+\in(0,1]$, $\ell_K>0$ ([Hin26c] (6.1)) and $d_0\ge2$, and consider
$$g = g_0+h,\qquad h\in\tilde{\mathcal G}^{d_0,(2\ell_I,\ell_+,\ell_K)}_{e3b}(\Omega_*),\qquad\|h\|<\epsilon_G\le1,
\tag{4.1}$$
with $\epsilon_G$ at most that of Lemma 3.2. Write $w := x_I^{2\ell_I}\rho_+^{\ell_+}\rho_K^{\ell_K}$, $G(\zeta) :=
g^{-1}(\zeta,\zeta)$, $G_{e3b} := x_I^{-2}\rho_+^{-2}G$, and, with $\rho_\infty$ a defining function of fibre infinity,
$$\mathsf H_G := \rho_\infty H_{G_{e3b}},\tag{4.2}$$
which on the characteristic set equals $\rho_\infty x_I^{-2}\rho_+^{-2}H_G$, the field II.B (1.4) ([Hin26c] (6.4b)).
$\Sigma := \{G_{e3b} = 0\}\subset{}^{e3b}T^*_{\Omega_*}M\setminus o$; $\Sigma^+$ is the closure of the set of null
covectors $\nu$ over $\Omega_*^\circ$ with $g^{-1}(\nu,dt^\flat_*)>0$, that is, with $\nu^\sharp$ future directed, as
$dt^\flat_*$ is past timelike (Lemma 3.2); $\Sigma^- := -\Sigma^+$. The source prints $g^{-1}(\zeta,dt^\flat_*)\le0$
(section 6, (C3)).

**Lemma 4.1.** (a) $G_{e3b}-G_{0,e3b}\in\epsilon_GwC^{d_0}P^{[2]}({}^{e3b}T^*_{\Omega_*}M)$, and $\mathsf H_G-\mathsf
H_{G_0}$ is a $C^{d_0-1}$ b-vector field on ${}^{e3b}\bar T^*_{\Omega_*}M$ in $\epsilon_GwC^{d_0-1}\mathcal V_b$, tangent
to fibre infinity. In particular $\Sigma$ and $\mathsf H_G$ agree with those of $g_0$ over $\Omega_*\cap\partial M$, and
$\mathsf H_G$ is $C^1$, so its integral curves are unique. (b) $\Sigma^+\cap\Sigma^- = \emptyset$, and $\Sigma^\pm$ agree
with those of $g_0$ over $\partial M$.

*Proof.* (a) $g^{-1}-g_0^{-1}\in x_I^2\rho_+^2\epsilon_GwC^{d_0}(S^2\,{}^{e3b}T)$ (Neumann series, as in the proof of
Lemma 3.7), which is the first statement. For $p\in wC^{d_0}P^{[2]}$, $H_p$ is a first-order e3b-differential operator
applied to $p$ (II.A section 2.5); b-vector fields preserve $wC^0$, so $H_p\in wC^{d_0-1}\mathcal V_b({}^{e3b}T^*M)$, and
$\rho_\infty H_p$ is tangent to fibre infinity by homogeneity. $w$ vanishes on $\mathscr I^+$, $\iota^+$ and $K^+$ as
$\ell_I,\ell_+,\ell_K>0$. (b) Over $\Omega_*^\circ$ a nonzero null covector is not orthogonal to the timelike
$dt^\flat_*$. Over $\partial M$, by (a) and II.B section 1.3. $\square$

**Proposition 4.2 ([Hin26c] Proposition 6.1 at $n = 4$).** Let $\gamma:I\to\partial\Sigma^+$ be a maximal integral curve
of $\mathsf H_G$ over $\Omega_*\cap\{r\ge r_0\}$. Then either $\gamma$ lies over $(\Omega_*\cap\mathscr
I^+)\cup\iota^+\cup K^+$, where it is an integral curve of $\mathsf H_{G_0}$ and is described by II.B Proposition 8.1; or
$\gamma$ reaches $\{t^\flat_* = 1\}$ backward at a finite parameter, and forward either reaches $\{r = r_0\}$ at a finite
parameter, where $\mathsf H_Gr<0$, or tends to ${}^{e3b}S^*M$ over $(\Omega_*\cap\mathscr I^+)\cup\iota^+\cup K^+$.

*Proof.* The boundary faces are invariant, as $\mathsf H_G$ is a b-vector field; over them $\mathsf H_G = \mathsf
H_{G_0}$ (Lemma 4.1). Let $\gamma$ lie over $M^\circ$. At $\nu\in\Sigma^+$ over $M^\circ$, $H_Gt^\flat_* =
2g^{-1}(\nu,dt^\flat_*)>0$, and $\mathsf H_Gt^\flat_*$ is bounded below by a positive constant on each compact subset of
$\partial\Sigma^+$ over $\Omega_*\cap M^\circ$, by continuity. *Forward.* If $t^\flat_*\circ\gamma$ is unbounded, its
limit points lie over $\{t^\flat_* = \infty\}\cap\Omega_* = \iota^+\cup K^+$. Otherwise, either $\gamma$ reaches $\{r =
r_0\}$, or $\sup I = \infty$ and a limit point over $M^\circ$ would be visited infinitely often, each visit to a fixed
small neighbourhood lasting a parameter time bounded below and raising $t^\flat_*$ by a fixed amount, so
$t^\flat_*\to\infty$; hence the limit points lie over $\partial M$ at bounded $t_*$, which in $\Omega_*$ is $\mathscr
I^+$. At $\{r = r_0\}$, $H_Gr = 2g^{-1}(\nu,dr)<0$ for future null $\nu$, as $dr$ is future timelike there (Lemma 3.2
(1)), so $\gamma$ leaves $\{r\ge r_0\}$ there. *Backward.* Suppose $\gamma$ does not reach $\{t^\flat_* = 1\}$. As
$\mathsf H_Gr<0$ at $\{r = r_0\}$, $r$ increases backward there, so $\gamma$ does not leave through $\{r = r_0\}$
backward (D200). Then $\inf I = -\infty$ and $t^\flat_*\circ\gamma\downarrow L\ge1$, and as before the $\alpha$-limit set
$\mathcal A$ lies over $\mathscr I^+\cap\{t^\flat_* = L\}$. Over $\mathscr I^+$, $t^\flat_* = t_*$ by Lemma 3.2 (a), so
$\rho_+ = L^{-1}$ on $\mathcal A$. $\mathcal A$ is non-empty, compact and invariant under $\mathsf H_{G_0}$, and every
curve in it has $\rho_+$ constant, so by II.B (7.5) $\hat\xi = 0$ and then $\hat\eta = 0$: $\mathcal A\subset\partial
R_{\mathscr I^+,\mathrm{out}}$. Near $\partial R_{\mathscr I^+,\mathrm{out}}$, by II.B (7.4) and Lemma 4.1 (a),
$\sigma_{eb}^{-1}H_{G_{eb}}x_I = (\hat\xi-1)x_I+O(x_I^{1+2\ell_I})\le-\frac12x_I$ for $x_I$ small (with $\sigma_{eb}>0$
on $\Sigma^+$ there, Lemma 5.3 below, for $\epsilon_G$ small). So on a tail $(-\infty,s_1]$, $x_I\circ\gamma>0$ increases
as $s$ decreases and cannot tend to 0, a contradiction. $\square$

The source does not prove the backward statement; II.B Proposition 8.2 proves it for $g_0$, and the argument carries over
by Lemma 4.1. The event horizon of $(\Omega_*,g)$, graphical over that of $g_0$ ([Hin26c] Remark 6.2, citing [CK24,
Hin24c]), is not used here.

## 5. Order functions

**Proposition 5.1 ([Hin26c] Proposition 6.4 at $n = 4$).** Let $P_0$ be a stationary wave-type operator for $g_0$,
$\eta\ge0$ and $\alpha_+,\alpha_K\in\mathbb R$, and let $\ell_I,\ell_+,\ell_K$ be as in section 4. There are $\mathsf
s\in C^\infty({}^{e3b}S^*_\Omega M)$ and $\epsilon_G>0$ such that:

(1) $\mathsf s$ over $K^+$, identified with a $t_*$-translation-invariant function on ${}^{3b}S^*\tilde M_0$ (over $K^+$
the e3b- and 3b-cosphere bundles agree), is stationary-$P_0$-admissible with margin $\eta$ and $\alpha_{\mathrm{sf}} =
\alpha_+$;

(2) for every $g = g_0+h$ with $\|h\|_{\tilde{\mathcal G}^{1,(2\ell_I,\ell_+,\ell_K)}_{e3b}(\Omega)}<\epsilon_G$,
$\pm\mathsf H_G\mathsf s\le0$ on $\partial\Sigma^\pm$ over $\Omega_*$;

(3) $\mathsf s$ is invariant under the dilations $(t_*,r,\omega)\mapsto(\lambda t_*,\lambda r,\omega)$ in a neighbourhood
of $\iota^+\cap\{r/t_*\in[1,10]\}$;

(4) (1) holds also for every stationary wave-type operator $P_1$ near $P_0$ (coefficients close in $C^1$), and (1)-(2)
hold for the stationary models of nearby parameters $b$ (K4);

(5) $\mathsf s$ is constant near $\partial R_{\mathscr I^+,\mathrm{out}}$ and near $\partial R_{\mathscr
I^+,\mathrm{in},+}$ (II.B Definition 7.1).

**Definition 5.2 ([Hin26c] Definition 6.5).** Order functions with (1)-(5) are *admissible* for $P_0$ with weights
$\alpha_+$, $\alpha_K$ and margin $\eta$.

Item (5) is part of [Hin23c] Lemma 5.8 (3), and is recorded here because the radial estimates at $\mathscr I^+$ of Part
II.D use it.

### 5.1 The characteristic set near $\mathscr I^+$ and near $\iota^+$

*Near $\mathscr I^+$.* $\Omega_I := \Omega\cap\{x_I\le\epsilon_I\}$, with the eb-coordinates of II.B section 7: $\rho_+ =
t_*^{-1}\in(0,1]$, $x_I = (t_*/r)^{1/2}$, covectors $\nu =
\sigma_{eb}\frac{d\rho_+}{\rho_+}+\xi_{eb}\frac{dx_I}{x_I}+\eta_{eb}\frac{d\omega}{x_I}$, $|\nu|_{eb}^2 :=
\sigma_{eb}^2+\xi_{eb}^2+|\eta_{eb}|^2$, $G_{eb} := x_I^{-2}\rho_+^{-2}G$. Let $\bar G_{eb}$ be II.B (7.1) and $G^0_{eb}
:= \frac12\xi_{eb}(\xi_{eb}-2\sigma_{eb})+|\eta_{eb}|^2$. For $g$ as in Proposition 5.1 (2), with $\epsilon_G\le1$, II.B
section 7 and Lemma 4.1 (a) at $d_0 = 1$ (its first assertion holds verbatim at $d_0 = 1$ and over $\Omega$, its proof
being the Neumann series; D200) give
$$G_{eb}-G^0_{eb} = \tfrac14x_I^2\xi_{eb}^2+(G_{eb}-\bar G_{eb})\in x_I^{2\ell_I}C^1P^{[2]},\tag{5.1}$$
with norm bounded independently of $g$, as $x_I^2\le x_I^{2\ell_I}$ and $\rho_+\le1$.

*Near $\iota^+$.* $\Omega_\iota := \Omega\cap\{\rho_K\le C_\iota,\ \varrho\le\epsilon_\iota\}$ with the 3b-coordinates of
II.B section 3: $\rho_K := r/t_*$, $\varrho := r^{-1}$, $\nu = \sigma_{3b}\frac{dt_*}r+\xi_{3b}\frac{dr}r+\eta_{3b}$,
$|\nu|_{3b}^2 := \sigma_{3b}^2+\xi_{3b}^2+|\eta_{3b}|^2$, $G_{3b} := r^2G$, $\bar G_{3b}$ of II.B (3.2). (II.B writes
$\rho_+$ for $\varrho$ there.) On $\Omega_\iota$, $x_I^2 = \rho_K^{-1}\ge C_\iota^{-1}$, so the e3b-defining function of
$\iota^+$ is comparable to $\varrho$, and II.B section 3 and Lemma 4.1 (a) give
$$G_{3b}-\bar G_{3b}\in w_\iota C^1P^{[2]},\qquad w_\iota := \varrho^{\ell_+},\tag{5.2}$$
with norm bounded in terms of $C_\iota$, as $\varrho^2\le\varrho^{\ell_+}$ and $\rho_K^{\ell_K}x_I^{2\ell_I}$ is bounded
on $\Omega$.

**Lemma 5.3.** For $\epsilon_I$ small and $\epsilon_\iota$ small (depending on $C_\iota$), and every $g$ as in
Proposition 5.1 (2) with $\epsilon_G\le\epsilon_1$ small: on $\Sigma$ over $\Omega_I$, $|\sigma_{eb}|\ge0.3|\nu|_{eb}$,
and $\sigma_{eb}>0$ on $\Sigma^+$; on $\Sigma$ over $\Omega_\iota$, $|\sigma_{3b}|\ge0.3|\nu|_{3b}$, and $\sigma_{3b}<0$
on $\Sigma^+$.

*Proof.* $2\bar G_{eb} = (\xi_{eb}-\sigma_{eb})^2-\sigma_{eb}^2+2|\eta_{eb}|^2+\frac12x_I^2\xi_{eb}^2$. If
$|\sigma_{eb}|<0.3|\nu|_{eb}$, then $(\xi-\sigma)^2\ge\frac12\xi^2-\sigma^2$ gives $2\bar
G_{eb}\ge\frac12(|\nu|^2-\sigma^2)-2\sigma^2\ge(\frac12-2.5\cdot0.09)|\nu|^2>\frac14|\nu|^2$, while $|2G_{eb}-2\bar
G_{eb}|\le C\epsilon_I^{2\ell_I}|\nu|^2<\frac14|\nu|^2$ by (5.1) for $\epsilon_I$ small: so $G_{eb}\ne0$. The 3b case is
the same, with $\bar G_{3b} = (\xi_{3b}-\sigma_{3b})^2+|\eta_{3b}|^2-\sigma_{3b}^2$ and (5.2). *Signs.* $\sigma_{eb} =
\nu(\rho_+\partial_{\rho_+}) = -\nu(V)$ with $V := t\partial_t+r\partial_r$ (II.B section 7). On $\Omega_I$, $r =
t_*x_I^{-2}\ge\epsilon_I^{-2}\ge R_2$, so $V$ is future timelike for $g_0$, and for $g$: $V =
-\rho_+\partial_{\rho_+}\in\mathcal V_{eb}$ and $h\in x_I^{-2}\rho_+^{-2}\epsilon_Gx_I^{2\ell_I}C^0(S^2\,{}^{eb}T^*)$
give $|h(V,V)|\le C\epsilon_Gx_I^{2\ell_I}x_I^{-2}\rho_+^{-2} = C\epsilon_Gx_I^{2\ell_I}rt_*$, small against
$|g_0(V,V)|\ge\frac12(t_*^2+2t_*r)$; the orientation is continuous along $g_0+\tau h$. For $\nu\in\Sigma^+$ over
$M^\circ$, $\nu(V) = g(\nu^\sharp,V)<0$, so $\sigma_{eb}>0$, and by the first part and continuity also over $\partial M$.
Likewise $\sigma_{3b} = r\nu(\partial_{t_*})$, and $\partial_{t_*}$ is future timelike for $g_0$ on $\{r\ge R_1\}$ (II.B
Lemma 1.2 (b)) and for $g$, as $|h(\partial_{t_*},\partial_{t_*})|\le C\epsilon_G$ on $\Omega_\iota$ ($r\partial_{t_*}$
is a 3b-vector field and $x_I^{-2}\rho_+^{-2}\sim r^2$ there). $\square$

On $\Sigma^+$ over $\Omega_I$ put $\hat\xi := \xi_{eb}/\sigma_{eb}$, $\hat\eta := \eta_{eb}/\sigma_{eb}$ and $\mathsf
H^{eb} := \sigma_{eb}^{-1}H_{G_{eb}}$; over $\Omega_\iota$, $\hat\xi_{3b} := \xi_{3b}/\sigma_{3b}$, $\hat\eta_{3b} :=
\eta_{3b}/\sigma_{3b}$ and $\mathsf H^{3b} := -\sigma_{3b}^{-1}H_{G_{3b}}$. On $\Sigma^+$ each is a positive multiple of
$\mathsf H_G$, as $G_{eb}$ and $G_{3b}$ are positive multiples of $G_{e3b}$ there ($x_I$ bounded below on
$\Omega_\iota$); signs of derivatives along them agree with those along $\mathsf H_G$. By Lemma 5.3,
$|\hat\xi|+|\hat\eta|\le7$ on $\Sigma$ over $\Omega_I$, and likewise in the 3b-coordinates over $\Omega_\iota$.

**Lemma 5.4 (near $\mathscr I^+$).** For $\epsilon_I$ small, on $\Sigma^+$ over $\Omega_I\cap\{|\hat\xi|\le\frac12\}$:
(a) $\hat\xi\ge-\frac18$ and $|\hat\eta|^2\le\frac32$; (b) $\mathsf H^{eb}\hat\xi\le-\frac14$ where
$\hat\xi\in[\frac14,\frac12]$; (c) $\mathsf H^{eb}x_I\le-\frac14x_I$.

*Proof.* By (5.1), $\mathsf H^{eb} = \mathsf H^0+\mathsf H^e$ with $\mathsf H^0 := \sigma_{eb}^{-1}H_{G^0_{eb}}$, given
exactly by II.B (7.4), and $\mathsf H^e := \sigma_{eb}^{-1}H_{G_{eb}-G^0_{eb}}$. By II.A (2.2), $\mathsf H^e$ applied to
$\hat\xi$ is $O(x_I^{2\ell_I})$ and applied to $x_I$ is $(\partial_{\xi_{eb}}(G_{eb}-G^0_{eb}))\sigma_{eb}^{-1}x_I =
O(x_I^{1+2\ell_I})$, uniformly where $|\hat\xi|+|\hat\eta|\le7$. On $\Sigma$, $\sigma_{eb}^{-2}G_{eb} = 0$ gives
$|\hat\eta|^2 = \frac12\hat\xi(2-\hat\xi)+E$ with $|E|\le C_3\epsilon_I^{2\ell_I}$. (a) For
$\hat\xi\in[-\frac12,-\frac18)$, $\frac12\hat\xi(2-\hat\xi)\le-\frac18$, so $|\hat\eta|^2<0$ once
$C_3\epsilon_I^{2\ell_I}<\frac18$; and for $|\hat\xi|\le\frac12$,
$|\hat\eta|^2\le\frac38+C_3\epsilon_I^{2\ell_I}\le\frac32$. (b) For $\hat\xi\in[\frac14,\frac12]$,
$|\hat\eta|^2\ge\frac7{32}-C_3\epsilon_I^{2\ell_I}\ge\frac3{16}$, and $\mathsf H^0\hat\xi = -2|\hat\eta|^2\le-\frac38$.
(c) $\mathsf H^0x_I = (\hat\xi-1)x_I\le-\frac12x_I$. The errors are absorbed for $\epsilon_I$ small. $\square$

**Lemma 5.5 (near $\iota^+$; [Hin23c] (C.8)-(C.9)).** Put $f_T := \varrho^{-1}(1-\hat\xi_{3b})$ and $f_W :=
-\hat\xi_{3b}$. Let $\delta\in(0,1]$. For $\epsilon_\iota$ small depending on $\delta$ and $C_\iota$, on $\Sigma^+$ over
$\Omega_\iota\cap\{|\hat\xi_{3b}|\le\frac\delta2\}$: (a) $\mathsf H^{3b}f_T\ge\varrho^{-1}$; (b)
$\hat\xi_{3b}\ge-\frac\delta8$, $|\hat\eta_{3b}|^2\ge|\hat\xi_{3b}|-\frac\delta8$ and $|\hat\eta_{3b}|^2\le3\delta$; (c)
$\mathsf H^{3b}f_W\ge\frac\delta8$ where $\hat\xi_{3b}\in[\frac\delta4,\frac\delta2]$.

*Proof.* Write $\mathsf H^{3b} = \bar{\mathsf H}+\mathsf H^e$, $\bar{\mathsf H} := -\sigma_{3b}^{-1}H_{\bar G_{3b}}$
given exactly by II.B (3.4) (with $\rho_+ = \varrho$), and $\mathsf H^e := -\sigma_{3b}^{-1}H_{G_{3b}-\bar G_{3b}}$,
which by (5.2) is a b-vector field with coefficients $O(w_\iota)$; it maps $\varrho$ into $\varrho\,O(w_\iota)$ and
$\hat\xi_{3b}$ into $O(w_\iota)$. (a) By (3.4), $\bar{\mathsf H}\varrho^{-1} = 2(1-\hat\xi)\varrho^{-1}$ and
$\bar{\mathsf H}\hat\xi = -2(2-\hat\xi)\hat\xi$, so
$$\bar{\mathsf H}f_T = 2\varrho^{-1}\big((1-\hat\xi)^2+(2-\hat\xi)\hat\xi\big) = 2\varrho^{-1}$$
exactly; and $|\mathsf H^ef_T|\le C\varrho^{-1}w_\iota$, so $\mathsf
H^{3b}f_T\ge(2-C\epsilon_\iota^{\ell_+})\varrho^{-1}\ge\varrho^{-1}$. (b) On $\Sigma$, $\sigma_{3b}^{-2}G_{3b} =
\hat\xi^2-2\hat\xi+|\hat\eta|^2+O(w_\iota) = 0$, so $|\hat\eta|^2 = \hat\xi(2-\hat\xi)+E$, $|E|\le
C\epsilon_\iota^{\ell_+}\le\frac\delta{16}$. For $\hat\xi\in[-\frac\delta2,-\frac\delta8)$,
$\hat\xi(2-\hat\xi)\le2\hat\xi<-\frac\delta4$, impossible. For $\hat\xi\in[0,\frac\delta2]$,
$\hat\xi(2-\hat\xi)\ge\hat\xi$; for $\hat\xi\in[-\frac\delta8,0)$, $|\hat\eta|^2\ge0\ge|\hat\xi|-\frac\delta8$. And
$\hat\xi(2-\hat\xi)\le3|\hat\xi|$ for $|\hat\xi|\le\frac12$, so $|\hat\eta|^2\le3|\hat\xi|+\frac\delta{16}\le3\delta$.
(c) For $\hat\xi\in[\frac\delta4,\frac\delta2]$, $\bar{\mathsf H}f_W = 2(2-\hat\xi)\hat\xi\ge2\hat\xi\ge\frac\delta2$, so
$\mathsf H^{3b}f_W\ge\frac\delta2-C\epsilon_\iota^{\ell_+}\ge\frac\delta8$ (D200). $\square$

### 5.2 The construction

Fix, all with values in $[0,1]$ (D200): $\phi\in C^\infty_c((-\frac12,\frac12))$ even, $\phi = 1$ on
$[-\frac14,\frac14]$, $\phi'\le0$ on $[0,\infty)$; $\psi\in C^\infty_c((-3,3))$ with $\psi = 1$ on $[-2,2]$;
$\tilde\psi\in C^\infty(\mathbb R)$ with $\tilde\psi = 0$ on $(-\infty,4]$, $\tilde\psi = 1$ on $[5,\infty)$,
$\tilde\psi'\ge0$; $\psi_0\in C^\infty([0,\infty))$ with $\psi_0 = 1$ on $[0,\frac12\epsilon_I]$, $\psi_0 = 0$ on
$[\epsilon_I,\infty)$, $\psi_0'\le0$; and $\Psi\in C^\infty(\mathbb R)$ with $\Psi = 0$ on $(-\infty,0.04]$ and $\Psi =
1$ on $[0.09,\infty)$. Choose, in this order: $\epsilon_I$ (Lemmas 5.3-5.4, and $\epsilon_I^2<\frac1{10}$, used in (3);
D200), $C_\iota := 8\epsilon_I^{-2}$, $\delta := \epsilon_I^2/32$, and $\epsilon_\iota$ (Lemmas 5.3, 5.5) so small that
also $1/(\epsilon_\iota\delta)>r_\Gamma$ for some $r_\Gamma$ as in Definition 2.4 (3), and
$1/(\epsilon_\iota\delta)>r_h+1$. Define
$$\chi_I := \phi(\hat\xi)\,\psi(|\hat\eta|^2)\,\Psi(\sigma_{eb}^2/|\nu|_{eb}^2),\qquad\chi_\iota := \phi(f_W/\delta)\,
\tilde\psi(\epsilon_\iota\delta f_T)\,\psi\big(|\hat\eta_{3b}|^2/(2\delta)\big)\,\Psi(\sigma_{3b}^2/|\nu|_{3b}^2),$$
$$\chi := \psi_0(x_I)\chi_I+(1-\psi_0(x_I))\chi_\iota,\qquad\mathsf s :=
s_{\mathrm{in}}-(s_{\mathrm{in}}-s_{\mathrm{out}})\chi,\tag{5.3}$$
with constants $s_{\mathrm{out}}\le s_{\mathrm{in}}$ chosen below.

*Smoothness.* $\chi_I$ is smooth on ${}^{eb}S^*$ over $\{x_I<\epsilon_I\}\supset\mathrm{supp}\,\psi_0(x_I)$, the ratios
being smooth where $\Psi\ne0$, that is, where $|\sigma_{eb}|\ge0.2|\nu|_{eb}$. $\chi_\iota$ is a function of $t_*$, $r$
and the 3b-fibre coordinates, which are smooth on ${}^{3b}S^*$ away from $\mathscr I^+$; on
$\mathrm{supp}(1-\psi_0(x_I))$, $x_I\ge\frac12\epsilon_I$, so $\rho_K = x_I^{-2}\le4\epsilon_I^{-2}<C_\iota$. Where
$\phi(f_W/\delta)\ne0$, $|\hat\xi_{3b}|<\frac\delta2\le\frac12$, so $\epsilon_\iota\delta
f_T\ge\frac12\epsilon_\iota\delta\varrho^{-1}\to\infty$ as $\varrho\to0$, and $\tilde\psi(\epsilon_\iota\delta f_T) = 1$
near $\varrho = 0$. Where $\tilde\psi(\epsilon_\iota\delta f_T)\ne0$ as well, $f_T>4/(\epsilon_\iota\delta)$ and $\varrho
= (1-\hat\xi_{3b})/f_T<\frac5{16}\epsilon_\iota\delta$, inside $\Omega_\iota$. Near a point with $\varrho = 0$ and
$|\hat\xi_{3b}|\ge\frac\delta2$, $\phi(f_W/\delta)$ vanishes on a neighbourhood, $\mathrm{supp}\,\phi$ being a compact
subset of $(-\frac12,\frac12)$. So $(1-\psi_0)\chi_\iota$ is smooth and supported in
$\Omega_\iota\cap\{\varrho<\epsilon_\iota\delta\}$, and $\chi\in C^\infty({}^{e3b}S^*_\Omega M)$, $0\le\chi\le1$. Every
factor is even under $\nu\mapsto-\nu$.

*Monotonicity.* Let $g$ be as in Proposition 5.1 (2) with $\epsilon_G\le\epsilon_1$, and work on $\partial\Sigma^+$. On
$\Sigma$ over $\Omega_I\cap\mathrm{supp}\,\phi(\hat\xi)$, $|\hat\eta|^2\le\frac32$ and $|\sigma_{eb}|\ge0.3|\nu|_{eb}$
(Lemmas 5.3-5.4), so $\psi(|\hat\eta|^2) = 1$ and $\Psi = 1$ on a neighbourhood of these points in $\partial\Sigma^+$,
and $\mathsf H\chi_I = \phi'(\hat\xi)\mathsf H\hat\xi$ there. Where $\phi'(\hat\xi)\ne0$,
$|\hat\xi|\in[\frac14,\frac12]$, so $\hat\xi\in[\frac14,\frac12]$ by Lemma 5.4 (a), $\phi'\le0$ and $\mathsf
H^{eb}\hat\xi<0$ (Lemma 5.4 (b)): $\mathsf H\chi_I\ge0$. Likewise on $\Sigma$ over $\Omega_\iota$ the factors $\psi$ and
$\Psi$ of $\chi_\iota$ equal 1 near $\mathrm{supp}\,\phi(f_W/\delta)$ (Lemma 5.5 (b):
$|\hat\eta_{3b}|^2/(2\delta)\le\frac32$), and
$$\mathsf H^{3b}\chi_\iota = \delta^{-1}\phi'(f_W/\delta)\tilde\psi\,\mathsf H^{3b}f_W+\epsilon_\iota\delta\,\phi\,
\tilde\psi'\,\mathsf H^{3b}f_T.$$
Where $\phi'(f_W/\delta)\ne0$, $|\hat\xi_{3b}|\in[\frac\delta4,\frac\delta2]$, hence
$\hat\xi_{3b}\in[\frac\delta4,\frac\delta2]$ (Lemma 5.5 (b)), so $f_W/\delta\in[-\frac12,-\frac14]$, where $\phi'\ge0$,
and $\mathsf H^{3b}f_W>0$ (Lemma 5.5 (c)). The second term is $\ge0$ by Lemma 5.5 (a). So $\mathsf H\chi_\iota\ge0$ on
$\partial\Sigma^+$ over $\mathrm{supp}(1-\psi_0)$.

*Gluing.* $\mathsf H\chi = \psi_0\mathsf H\chi_I+(1-\psi_0)\mathsf H\chi_\iota+\psi_0'(x_I)(\mathsf
Hx_I)(\chi_I-\chi_\iota)$, and the last term lives on $U := \{\frac12\epsilon_I\le x_I\le\epsilon_I\}$. Two facts on
$\partial\Sigma^+$ over $U$:

(U1) where $\chi_\iota\ne0$, $\chi_I = 1$. Indeed there $|\hat\xi_{3b}|<\frac\delta2 = \epsilon_I^2/64$ and $u := x_I^2 =
t_*/r\in[\frac14\epsilon_I^2,\epsilon_I^2]$. The two systems of fibre coordinates are related by $\sigma_{eb} =
-\sigma_{3b}(u+\hat\xi_{3b})$, $\xi_{eb} = -2\xi_{3b}$, $\eta_{eb} = x_I\eta_{3b}$, an identity of coordinates proved in
II.B Lemma 7.3 that holds wherever both are defined. So $\hat\xi = 2\hat\xi_{3b}/(u+\hat\xi_{3b})$, and
$u+\hat\xi_{3b}\ge\epsilon_I^2/8$ gives $|\hat\xi|\le\frac14$: $\phi(\hat\xi) = 1$, and $\psi = \Psi = 1$ as before.

(U2) where $\chi_I\ne0$, $\mathsf Hx_I<0$: there $|\hat\xi|<\frac12$, and Lemma 5.4 (c) applies.

Where $\chi_I = 0$, (U1) gives $\chi_\iota = 0$ and the last term vanishes. Where $\chi_I>0$, $\psi_0'\mathsf Hx_I\ge0$
by (U2), and $\chi_I-\chi_\iota\ge0$, since either $\chi_\iota = 0$ or $\chi_I = 1\ge\chi_\iota$. Hence $\mathsf
H\chi\ge0$ on $\partial\Sigma^+$, and $\mathsf H\mathsf s = -(s_{\mathrm{in}}-s_{\mathrm{out}})\mathsf H\chi\le0$. On
$\partial\Sigma^-$: the antipodal map $A:\nu\mapsto-\nu$ maps $\Sigma^+$ onto $\Sigma^-$, $G$ is even, so $H_G$ and
$\mathsf H_G$ are odd ($A_*\mathsf H_G = -\mathsf H_G$), and $\mathsf s\circ A = \mathsf s$; hence $\mathsf H_G\mathsf
s(A\nu) = -\mathsf H_G\mathsf s(\nu)\ge0$, which is $-\mathsf H_G\mathsf s\le0$ on $\partial\Sigma^-$. This proves (2),
with $\epsilon_G := \epsilon_1$; the case $h = 0$ restricted to $K^+$ is Definition 2.4 (1).

*Values.* Over $K^+$, $x_I = (t_*/r)^{1/2} = \infty$, so $\psi_0(x_I) = 0$ and $\chi = \chi_\iota$, a function of
$\varrho$ and the 3b-fibre coordinates, hence $t_*$-translation-invariant there; it vanishes over
$\{\varrho\ge\epsilon_\iota\delta\}$, a set containing $\{r\le r_\Gamma\}$ and a neighbourhood of the horizon: $\mathsf s
= s_{\mathrm{in}}$ there. Near $\partial R_{\partial K^+,\mathrm{in}}$ ($\hat\xi_{3b} = 2$), $\phi(f_W/\delta) = 0$, so
$\mathsf s = s_{\mathrm{in}}$. Near $\partial R_{\partial K^+,\mathrm{out}} = \{\rho_K = \varrho = 0,\ \hat\xi_{3b} = 0,\
\hat\eta_{3b} = 0\}$: $\phi(f_W/\delta) = 1$ for $|\hat\xi_{3b}|\le\frac\delta4$, $\tilde\psi = 1$ for $\varrho$ small,
$\psi = 1$ for $\hat\eta_{3b}$ small, and $\Psi = 1$ as $|\sigma_{3b}| = |\nu|_{3b}$ at the set: $\mathsf s =
s_{\mathrm{out}}$ on a neighbourhood. Near $\partial R_{\mathscr I^+,\mathrm{out}}$ ($x_I = 0$, $\hat\xi = 0$, $\hat\eta
= 0$), $\psi_0 = 1$ and $\chi_I = 1$: $\mathsf s = s_{\mathrm{out}}$. Near $\partial R_{\mathscr I^+,\mathrm{in},+}$
($\hat\xi = 2$), $\psi_0 = 1$ and $\chi_I = 0$: $\mathsf s = s_{\mathrm{in}}$. Choose
$$s_{\mathrm{in}}>\max\Big(\tfrac12+\vartheta_{\mathcal H}+\eta,\ \tfrac12(-1+\vartheta^{3b}_{\mathrm{in}})+\alpha_K+
\eta-\alpha_+\Big)+1,\qquad s_{\mathrm{out}}<\min\Big(s_{\mathrm{in}},\ \tfrac12(-1+\vartheta_{\mathrm{out}})+
\alpha_K-\eta-\alpha_+\Big)-1,$$
each threshold in a fibre inner product chosen for its radial set (for $\vartheta_{\mathrm{out}}$, that of Lemma 2.5).
Then, with $\mathsf s := s_{\mathrm{in}}$ over $\{r_0-2\delta_0<r<r_0\}$ (where nothing else is defined), Definition 2.4
(1)-(6) hold, which is (1), and (5) holds.

*(3).* In a neighbourhood of $\iota^+\cap\{\rho_K\in[1,10]\}$, $x_I^2 = \rho_K^{-1}\ge\frac1{10}>\epsilon_I^2$, so
$\psi_0(x_I) = 0$, and $\varrho$ is small, so $\tilde\psi(\epsilon_\iota\delta f_T) = 1$ on
$\mathrm{supp}\,\phi(f_W/\delta)$: $\chi =
\phi(-\hat\xi_{3b}/\delta)\psi(|\hat\eta_{3b}|^2/(2\delta))\Psi(\sigma_{3b}^2/|\nu|_{3b}^2)$ there. The 3b-covectors
$\frac{dt_*}r$, $\frac{dr}r$, $d\omega$ are invariant under the dilations, so are their coefficients' ratios and
$|\nu|_{3b}^2$ (with the round metric on $\mathbb S^3$).

*(4).* The thresholds $\vartheta_{\mathcal H}$, $\vartheta^{3b}_{\mathrm{in}}$, $\vartheta_{\mathrm{out}}$ are extreme
eigenvalues of endomorphisms depending continuously on the coefficients, over compact sets, so they move by less than 1
for $P_1$ near $P_0$ (with fixed inner products), and the margins of 1 above keep (4)-(6) of Definition 2.4. (1)-(3) of
the definition do not depend on the operator beyond its metric. For nearby parameters $b$, the stationary metrics satisfy
(K1) with uniform constants (K4), so (5.1)-(5.2) and Lemmas 5.3-5.5 hold uniformly; the horizon radius and $\Gamma$ vary
continuously (II.B Remark 8.3), so $\{\varrho\ge\epsilon_\iota\delta\}$ still contains them after shrinking
$\epsilon_\iota$. $\square$

*Remark (the construction of [Hin23c]).* [Hin23c] Appendix C also multiplies $\chi_I$ by a localisation $\chi_t$ in a
time function, with a further small parameter $\rho_{+,\mathrm{lo}}$, because its error term in $\mathsf Hx_I$ is
$C\rho_+^{\ell_+}x_I$. Here the error carries $x_I^{2\ell_I}$ by (5.1) (II.B's rate $x_I^2$ for the stationary part, and
the weight $x_I^{2\ell_I}$ of the perturbation), so Lemma 5.4 (c) holds at all $\rho_+\le1$ and $\chi_t$ is not needed.
The source's own text ([Hin26c] p. 114) cites that construction and adds that only the dynamics over $\iota^+$ matter;
section 5.2 confirms this, the trapped set and the horizon lying where $\mathsf s$ is constant.

## 6. What this part found

(C0) *The constants at $n = 4$.* (5.1a)'s 1 is $\frac32$ (Definition 1.1); (5.7)'s $2(1+S)$ is $3+2S$ ((1.4)); the
characteristic exponents $2(1+\mu)$ are $3+2\mu$ (Lemma 3.4); the tf-weight $\alpha_{\mathrm{sf}}+\frac32$ is
$\alpha_{\mathrm{sf}}+2$ (Definition 2.7); the scalar wave operator's sf-weights $(-\frac32,-\frac12)$ are $(-2,0)$. The
thresholds at $\partial K^+$ keep their form: the symmetry of $-2\partial_{t_*}\rho(\rho\partial_\rho-c)$ for the density
$\rho^{-n-1}d\rho$ forces $c = \frac{n-1}2$, and with it Lemma 2.6.

(C1) *[Hin26c] p. 107, after Definition 5.15.* "$x_I^{-2}\rho_+^{-2}(g_{m,a}+h)$ is a non-degenerate Lorentzian signature
section of $S^2\,{}^{e3b}T^*_\Omega M$" should read $x_I^2\rho_+^2(g_{m,a}+h)$:
$g_{m,a}\in\rho_0^{-2}x_I^{-2}\rho_+^{-2}C^\infty(S^2\,{}^{e3b}T^*M)$ is non-degenerate there (its Lemma 4.4 (3)), so the
normalised section carries the positive powers (Definition 3.1, Remark (b)).

(C2) *[Hin26c] Definition 5.11 (1).* "monotonically non-decreasing along the future null-bicharacteristic flow"
contradicts the parenthesis "$\pm H_G\mathsf s\le0$ on $\partial\Sigma^\pm$" and the source's section 6.2 ("monotonically
decreasing along the future-directed null-bicharacteristic flow"): the order must be non-increasing, high at the sources
and low at the sinks (Definition 2.4 (1)).

(C3) *[Hin26c] (6.5).* "$(z,\zeta)\in\Sigma$ lies in $\Sigma^+$ if and only if $g^{-1}(\zeta,dt^\flat_*)\le0$": with
$dt^\flat_*$ past timelike, a covector $\zeta$ with $\zeta^\sharp$ future directed null has $g^{-1}(\zeta,dt^\flat_*) =
g(\zeta^\sharp,(dt^\flat_*)^\sharp)>0$, a future and a past causal vector having positive product; and the source's own
$\Sigma^+$ has $\sigma_{3b}<0$ over $\iota^+$ (its p. 81), which is the future set (II.B Lemma 1.2). The sign is
reversed; Lemma 4.1 uses $>0$.

(C4) *[Hin26c] Example 5.4 at $n = 4$.* With (K1)'s rate, $S = 0$ in the coordinate frame and (1.2) holds with $\rho^4$;
the source's $S\in\rho C^\infty$ and $\rho^3$ are Kerr's rate $r^{-1}$ (Lemma 1.3).

(C5) *[Hin26c] Lemma 5.16.* The proof takes "a smoothing" of a piecewise function; a smoothing preserves timelikeness
only if its differential stays in the past cone. Lemma 3.2 glues by a smooth minimum in $\log$ and a smooth maximum in
$r$, whose differentials are convex combinations of the pieces'. The source's proof also leaves the comparison of the
pieces at $r = Ct_*$ implicit; it is $\varphi'<0$ above.

(C6) *[Hin26c] Proposition 6.1.* The backward statement ("$\gamma$ crosses $\{t^\flat_* = 1\}$ in the backward
direction") is stated without proof; Proposition 4.2 proves it by the repulsion of $\partial R_{\mathscr
I^+,\mathrm{out}}$ in $x_I$ backward.

(C7) *[Hin26c] Proposition 6.4.* Proved by the construction it cites, written out (section 5.2), with item (5) added and
the localisation $\chi_t$ of [Hin23c] shown unnecessary in this class. The bound on the characteristic set that the cited
appendix states as its (C.1) is replaced by Lemma 5.3, which proves the form used.

(C8) *Changes of statement.* Definition 2.1 takes the threshold of trapping admissibility from I.B's (Γ.4), for the
density of I.A, in place of (5.8) for $|dg|$, and does not use (5.9); Definition 2.3 is I.C's tf-admissibility (I.C
section 5.1 compares it with the source's). Proposition 4.2 is stated over $\{r\ge r_0\}$, where the perturbation is
defined, with "reaches $\{r = r_0\}$" for the source's "crosses $\{r = m\}$".

## Sources

[Hin26c] P. Hintz, *(Non-)linear waves on asymptotically flat spacetimes. II*, arXiv:2606.28008v1. READ: pp. 100-115
(section 5: Definitions 5.1, 5.8, 5.10, 5.11, 5.13, 5.15, 5.18, 5.20, 5.23, Remarks 5.2, 5.3, 5.5, 5.6, 5.9, 5.14, 5.17,
5.19, 5.21, 5.22, Example 5.4, Lemmas 5.7, 5.12, 5.16, (5.1)-(5.27); section 6: Propositions 6.1, 6.3, 6.4, Definition
6.5, (6.1)-(6.7); the start of section 7, (7.1)-(7.4), for the use of Proposition 6.4).

[Hin23c] P. Hintz, *Linear waves on non-stationary asymptotically flat spacetimes. I*, arXiv:2302.14647v1. READ: pp.
97-100 (the radial sets (5.4), Lemma 5.3, $W_{\mathrm{out}}$ (5.14)), 106-108 (Lemma 5.8, Remarks 5.9-5.11, Proposition
5.12), 150-154 (Proposition B.1 and Appendix C). The construction of Appendix C is written out in section 5.2 and Lemma
2.5; no statement of [Hin23c] is used as an input.

Part I.A: sections 1.1-1.4 ((H1)-(H5), (1.5)). Part I.B: sections 1.2-1.5 ((H6)-(H8), Lemma 1.1). Part I.C: section 1.2
and Definition 5.1, Corollary 5.2. Part II.A: sections 1, 2.1-2.5 (Definitions 1.2-1.3, 2.1, 2.4, 2.8, Lemma 2.5,
(2.1)-(2.2)), 7, 8.1-8.2 (Definition 8.1, Lemma 8.2). Part II.B: sections 1-3, 7-8 ((K1)-(K4), Lemmas 1.1-1.2,
(3.1)-(3.4), Definition 3.1, Lemma 3.2, Definitions 4.1, 7.1, (7.1)-(7.5), Lemma 7.3, Propositions 8.1-8.2, Remark 8.3).
