# Part II.F. The normal operator at future timelike infinity, and forward solutions on e3b-spaces, at n = 4

*Status.* Written out in full (D208). Not yet read by an independent verifier; nothing here is labelled proved. This part
proves, at spatial dimension $n = 4$, [Hin26c] section 10 (pp. 200-227): Theorem 10.1, which solves forward problems for
the stationary model $P_0$ on edge-3b-Sobolev spaces with decay at $\iota^+$ and the loss $\aleph$ at $K^+$, and the
ingredients: the normal operator $N_{\iota^+}(P_0)$ at $\iota^+$ and its Mellin-transformed family (Definition 10.3,
Lemma 10.5, Proposition 10.6, Lemmas 10.7-10.10), forward solutions of $N_{\iota^+}(P_0)$ (Proposition 10.12), and
forward solutions of the modified operator $P_+$ (Definition 10.13, Proposition 10.14). The source is [Hin26c] = P.
Hintz, arXiv:2606.28008v1 (printed page numbers). Part I.B (`PART-I-B-HIGHENERGY.md`) is cited as I.B, Part I.C
(`PART-I-C-LOWENERGY.md`) as I.C, Part II.A (`PART-II-A-SETUP.md`) as II.A, Part II.A$'$ as II.A$'$, Part II.B as II.B,
Part II.C as II.C, Part II.D as II.D, Part II.D$'$ as II.D$'$ and Part II.E (`PART-II-E-ENERGY.md`) as II.E.

*Method.* The dimension enters the source's argument through the constant $c := \frac{n-1}2$ of the stationary model's
normal form, $\frac32$ here (II.C (1.1)), and through the densities, which shift weights by $\frac n2 = 2$ and
$\frac{n+1}2 = \frac52$ (II.A Lemma 6.1). Every threshold is a sum of these, and each is recomputed at $n = 4$; the
record's instrument `iplusnorm5.py` (N1-N9) computes the same numerals by machine, and agrees. The analysis of the
Mellin-transformed family at high frequencies is a semiclassical one on $\iota^+$, in the parameterised scaled bounded
geometry calculus READ in II.A section 3 ([SBG] = arXiv:2408.06651v1). The source states it "briefly" and leaves "the
statements of standalone propagation estimates to the reader". Here the positive commutator scheme of I.B is carried over
to that calculus (section 2); each radial estimate then reduces to a computation of symbols at the radial set, which is
written out. The bounded frequencies use the parametrix of the 0-calculus, READ in [0C] = P. Hintz, *Elliptic
parametrices in the 0-calculus of Mazzeo and Melrose*, arXiv:2112.08130v1 (Definition 1.2, Theorem 3.4 and Corollary 3.6,
stated on manifolds of every dimension). Everything else is proved here or in the earlier parts.

*Organisation.* Section 1: coordinates, weights, the normal operator at $\iota^+$ and its family. Section 2: the calculi
on $\iota^+$ and the positive commutator scheme. Sections 3-4: high frequencies (Proposition 10.6 (2)), without and with
b-regularity. Section 5: bounded frequencies (Proposition 10.6 (1), Lemmas 10.9-10.10). Section 6: forward solutions of
$N_{\iota^+}(P_0)$ (Proposition 10.12). Section 7: the modified operator $P_+$ (Definition 10.13, Proposition 10.14).
Section 8: Theorem 10.1. Section 9: findings, gaps closed, and sources.

## 1. Setting

### 1.1 Coordinates and weights

$n = 4$ and $c := \frac32$ throughout. Near $(\iota^+)^\circ$ use $\tau := t_*^{-1}$ and $R := r/t_*$ (II.A Lemma 2.11),
so $\rho = r^{-1} = \tau/R$; $v := R^{-1} = t_*/r$, and near $\iota^+\cap\mathscr I^+$
$$x_I := R^{-1/2} = (t_*/r)^{1/2},$$
which is the $x'_I$ of II.B section 7 and II.D (it differs from the $x_I = r^{-1/2}$ of II.E section 1 by $t_*^{1/2}$).
$\iota^+ = [0,\infty]_R\times\mathbb S^3$, with boundary faces $\iota^+\cap K^+ = \{R = 0\}$ and $\iota^+\cap\mathscr I^+
= \{x_I = 0\}$; $\rho_K := R/(1+R)$ and $x_I$ (or $(1+R)^{-1/2}$) are defining functions of them. In $(t_*,r)$ and
$(\tau,R)$,
$$t_*\partial_{t_*}|_r = -\tau\partial_\tau-R\partial_R,\qquad r\partial_r|_{t_*} = R\partial_R = -\tfrac12x_I
\partial_{x_I},\qquad\rho\partial_\rho|_{t_*} = -R\partial_R.\tag{1.1}$$

*Weights.* Let $\mu_b$ be a smooth positive b-density on $\iota^+$, e.g. $|\frac{dR}R\,d\slashed g|$. By II.A Lemma 6.1,
near $\iota^+$ (on the support of a cut-off $\chi$ to $\mathrm{cl}\{r\ge1,t_*\ge1\}$),
$H^{0,(2\alpha_I,\alpha_+,\alpha_K)}_{e3b}(|dt\,dx|) =
H^{0,(2(\alpha_I+2),\alpha_++\frac52,\alpha_K+\frac12)}_{e3b}(|\frac{d\tau}\tau|\mu_b)$, and as $\tau\sim\rho_+\rho_K$
near $\iota^+$, the weights $\rho_+^{\alpha_++\frac52}\rho_K^{\alpha_K+\frac12}$ are
$\tau^{\alpha_++\frac52}\rho_K^{\alpha_K-\alpha_+-2}$. So, with b-densities on $[0,\infty)_\tau\times\iota^+$, the
weights of this part are
$$\gamma_I := \alpha_I+2\ \text{at}\ \mathscr I^+,\qquad\gamma_+ := \alpha_++\tfrac52\ \text{at}\ \tau = 0,\qquad\gamma_{
\mathrm{cf}} := -(\alpha_++2)\ \text{at}\ \iota^+\cap K^+\ (\text{for}\ \alpha_K = 0).\tag{1.2}$$
At $n = 3$ the source has $\alpha_I+\frac32$, $\alpha_++2$, $-(\alpha_++\frac32)$. The weight $\alpha_{\mathrm{sf}}+2$
with which $P_0$ is tf-admissible (II.C Definition 2.7 (2)) is $-\gamma_{\mathrm{cf}}$.

*Indicial gap.* $(\beta_-,\beta_+)$ is the indicial gap of $\hat P_0(0)$ that contains $-\gamma_{\mathrm{cf}} =
\alpha_++2$ (II.C Definitions 2.3, 2.7 (2); I.C Definition 1.1). By II.C section 2.4 it is the b-weight of $\hat P_0(0)$
at $\partial X$ for $L^2(|dx|)$ at $n = 4$.

*The Mellin transform.* In this part, as in [Hin26c] section 10,
$$(\mathcal Mu)(\sigma,\cdot) := \int_0^\infty\tau^{-i\sigma}u(\tau,\cdot)\,\frac{d\tau}\tau,\qquad\mathcal M(\tau
\partial_\tau u) = i\sigma\,\mathcal Mu.\tag{1.3}$$
This is the transform of II.A section 6.2 at $-\sigma$. For $u = \tau^{\gamma}w$, $(\mathcal Mu)(\sigma-i\gamma) =
(\mathcal Mw)(\sigma)$ for real $\sigma$: the Plancherel line of the weight $\tau^\gamma$ is $\mathrm{Im}\,\sigma =
-\gamma$ (II.A Lemma 6.2 with $\sigma\mapsto-\sigma$; its line $\mathrm{Im}\,\sigma = +\beta_+$ is for $\tau^{i\sigma}$).

### 1.2 The normal operator at $\iota^+$

By II.C Definition 1.1, on $\{\rho<\rho_1\}$,
$$P_0 = -2\partial_{t_*}\rho\big(\rho\partial_\rho-c-S\big)+\rho^2P^{(0)}(\rho,\omega,\rho\partial_\rho,
\partial_\omega)+Q\partial_{t_*}-g_{00}\partial_{t_*}^2,\tag{1.4}$$
with $S\in C^\infty(\bar X;\mathrm{End}\,\mathbb C^N)$, $P^{(0)}\in\mathrm{Diff}^2_b(\bar X;E)$, $P^{(0)}\equiv((\rho
D_\rho)^2+\Delta_{\mathbb S^3})\mathrm{Id}$ modulo $\mathrm{Diff}^1_b+\rho\,\mathrm{Diff}^2_b$ (II.C Lemma 1.2),
$Q\in\rho^3\mathrm{Diff}^1_b$, $g_{00}\in\rho^2C^\infty(\bar X)$. We write
$P^{(0)}(0,\omega,\rho\partial_\rho,\partial_\omega)$ for the operator whose coefficients are those of $P^{(0)}$ frozen
at $\rho = 0$ (its normal operator at $\partial X$, $N(P^{(0)})$ of I.C (4.1)), and $S_0 := S|_{\partial X}$.

**Definition 1.1 ([Hin26c] Definition 10.3 at $n = 4$).** The *$\iota^+$-normal operator* of $P_0$ is $N_{\iota^+}(P_0)
:= t_*^{-2}N^0$ on $(0,\infty)_\tau\times(\iota^+)^\circ$, with
$$N^0 := -2R^{-1}(\tau\partial_\tau+R\partial_R)\big(R\partial_R+c+S_0\big)+R^{-2}P^{(0)}(0,\omega,-R\partial_R,
\partial_\omega).\tag{1.5}$$
Its *Mellin-transformed family* is
$$N^0(\sigma) := -2R^{-1}(i\sigma+R\partial_R)\big(R\partial_R+c+S_0\big)+R^{-2}P^{(0)}(0,\omega,-R\partial_R,
\partial_\omega) = x_I^2\Big[-\tfrac12(x_I\partial_{x_I}-2i\sigma)\big(x_I\partial_{x_I}-2(c+S_0)\big)+x_I^2P^{(0)}
\big(0,\omega,\tfrac12x_I\partial_{x_I},\partial_\omega\big)\Big],\tag{1.6}$$
so that $\mathcal M(N^0u)(\sigma) = N^0(\sigma)(\mathcal Mu)(\sigma)$ by (1.3).

The second form of (1.6) follows from $R\partial_R = -\frac12x_I\partial_{x_I}$ and $R^{-1} = x_I^2$:
$i\sigma+R\partial_R = -\frac12(x_I\partial_{x_I}-2i\sigma)$ and $R\partial_R+c+S_0 =
-\frac12(x_I\partial_{x_I}-2(c+S_0))$. The source prints $N_{\iota^+}(P_0) = t_*^2N^0$; the correct factor, which its use
in Proposition 10.12 ("$N^0_{\iota^+}(P_0)u = t_*^2f$") and the homogeneity of degree $-2$ require, is $t_*^{-2}$
(section 9, (F1)).

In $(t_*,r,\omega)$, by (1.1), $\tau\partial_\tau+R\partial_R = -t_*\partial_{t_*}$ and $R^{-1} = t_*/r$, so
$$N_{\iota^+}(P_0) = 2r^{-1}\partial_{t_*}\big(r\partial_r+c+S_0\big)+r^{-2}P^{(0)}(0,\omega,-r\partial_r,
\partial_\omega):\tag{1.7}$$
the operator (1.4) with $Q = 0$, $g_{00} = 0$ and its coefficients frozen at $\rho = 0$. It is $t_*$-translation
invariant, homogeneous of degree $-2$ under $(t_*,x)\mapsto(\lambda t_*,\lambda x)$, and its principal symbol is the dual
metric function of the Minkowski metric $\bar g$: by II.C Lemma 1.2, $\sigma_2(\rho^2P^{(0)}) = \bar g^{-1}$ on spatial
covectors up to $\rho^2P^{[2]}$, and $\sigma_2(-2\partial_{t_*}\rho\rho\partial_\rho) =
\sigma_2(2\partial_{t_*}\partial_r)$, which with the frozen part gives $-2\zeta_{t_*}\zeta_r+\zeta_r^2+r^{-2}|\eta|^2 =
\bar g^{-1}(\zeta,\zeta)$ (II.E Lemma 2.4's proof). In $(\tau,R)$ this is the dual metric
$$g^{-1}_{\iota^+} = \tau^{-2}\bar g^{-1} = 2R^{-1}(\tau\partial_\tau+R\partial_R)\otimes_sR\partial_R+R^{-2}\big((R
\partial_R)^2+\slashed g^{-1}\big),\tag{1.8}$$
with $a\otimes_sb := \frac12(a\otimes b+b\otimes a)$, and $d(\log\tau) = -\frac{dt_*}{t_*}$ is null for it, as $dt_*$ is
for $\bar g$.

**Lemma 1.2 ([Hin26c] Lemma 10.5 at $n = 4$).** Let $\chi\in C^\infty(M)$ equal 1 near $\iota^+$, supported in a small
collar of $\iota^+$. Then
$$\chi N_{\iota^+}(P_0)\in x_I^2\rho_+^2\mathrm{Diff}^2_{e3b}(M),\qquad\chi\big(P_0-N_{\iota^+}(P_0)\big)\in x_I^2
\rho_+^3\mathrm{Diff}^2_{e3b}(M).\tag{1.9}$$

*Proof.* The first membership is checked as II.C Lemma 1.4 (b), which uses of $P_0$ only the form (1.4), and
$N_{\iota^+}(P_0)$ has that form. For the second, $t_*^2(P_0-N_{\iota^+}(P_0)) = t_*^2P_0-N^0$, and by (1.1),
$t_*^2\cdot(-2\partial_{t_*}\rho(\rho\partial_\rho-c-S_0))$ and
$t_*^2\rho^2P^{(0)}(0,\omega,\rho\partial_\rho,\partial_\omega)$ are the two terms of (1.5): $\partial_{t_*} =
-\tau(\tau\partial_\tau+R\partial_R)$, which commutes with $\rho = \tau/R$, and $\rho\partial_\rho = -R\partial_R$, so
$-2\rho\partial_{t_*}(\rho\partial_\rho-c-S_0) = -2\tau^2R^{-1}(\tau\partial_\tau+R\partial_R)(R\partial_R+c+S_0)$, and
$t_*^2\rho^2 = R^{-2}$. The remaining terms are, near $\mathscr I^+$ with $x_I = v^{1/2}$: (i)
$-2t_*^2\partial_{t_*}\rho\cdot\rho(S_0-S)$, with $S-S_0\in\rho C^\infty$: of the form $\tau
R^{-2}(\tau\partial_\tau+R\partial_R)\cdot C^\infty$, which vanishes at $\tau = 0$ and to order $R^{-2} = x_I^4$ at
$\mathscr I^+$; (ii) $t_*^2\rho^2(P^{(0)}(\rho,\cdot)-P^{(0)}(0,\cdot))\in t_*^2\rho^3\mathrm{Diff}^2_b(\bar X)$, of the
schematic form $\tau R^{-3}(R\partial_R,\partial_\omega)^{\le2}$, hence
$x_I^4\tau(x_I\partial_{x_I},x_I\partial_\omega)^{\le2}$, as $R^{-3}\partial_\omega^2 = x_I^4(x_I\partial_\omega)^2$;
(iii) $t_*^2Q\partial_{t_*}\in t_*^2\rho^3\mathrm{Diff}^1_b(\bar X)\partial_{t_*}$, of the form
$\tau^2R^{-3}(\tau\partial_\tau+R\partial_R)(R\partial_R,\partial_\omega)^{\le1}$; (iv) $t_*^2g_{00}\partial_{t_*}^2$,
$g_{00}\in\rho^2C^\infty$, of the form $\tau^2R^{-2}(\tau\partial_\tau+R\partial_R)^{\le2}$. Each lies in $\tau
x_I^4\mathrm{Diff}^2$ of the fields $\tau\partial_\tau$, $x_I\partial_{x_I}$, $x_I\partial_\omega$ near
$\iota^+\cap\mathscr I^+$ and in $\tau\mathrm{Diff}^2_b$ near $\iota^+\cap K^+$, with $R\le C$ there. Multiplying by
$t_*^{-2} = \tau^2$ and using $\tau\sim\rho_+$ near $\iota^+\cap\mathscr I^+$ and $\tau\sim\rho_+\rho_K$ near
$\iota^+\cap K^+$, together with the e3b-spanning sets of II.A section 2.4, gives (1.9). The powers of $\rho$ in (i)-(iv)
do not depend on $n$. $\square$

### 1.3 The family on $\iota^+$, and its semiclassical rescaling

By (1.6), $N^0(\sigma)\in x_I^2\rho_K^{-2}\mathrm{Diff}^2_{0,b}(\iota^+)$: near $\iota^+\cap K^+$ it is $R^{-2}$ times a
b-differential operator in $(R,\omega)$, near $\iota^+\cap\mathscr I^+$ it is $x_I^2$ times a 0-differential operator in
the fields $x_I\partial_{x_I}$, $x_I\partial_\omega$ (II.A section 6.2: $C^\infty_b\mathcal V_{0,b}(\iota^+)$). Its
0,b-principal symbol is, with 0-covectors $\xi_0\frac{dx_I}{x_I}+\eta_0\frac{d\omega}{x_I}$,
$$x_I^2\big(\tfrac12\xi_0^2+|\eta_0|^2+\tfrac14x_I^2\xi_0^2\big)\mathrm{Id},\tag{1.10}$$
since $-\frac12(x_I\partial_{x_I})^2\mapsto\frac12\xi_0^2$ and
$x_I^2P^{(0)}(0,\omega,\frac12x_I\partial_{x_I},\partial_\omega)\mapsto x_I^2(\frac14\xi_0^2)+|\eta_0|^2$
($\Delta_{\mathbb S^3}\ge0$); near $\iota^+\cap K^+$ the b-principal symbol is $R^{-2}$ times that of
$(RD_R)^2+\Delta_{\mathbb S^3}$ plus the term $-2R^{-1}(R\partial_R)^2\mapsto2R^{-1}\xi_b^2$, positive definite. So
$N^0(\sigma)$ is elliptic in the 0,b-sense, for every $\sigma\in\mathbb C$.

For $h\in(0,1]$ and $z\in\mathbb C$ with $|z|\in[\frac12,2]$ put
$$P_{\iota,h,z} := h^2N^0(h^{-1}z) = x_I^2\Big[-\tfrac12\big(hx_I\partial_{x_I}-2iz\big)\big(hx_I\partial_{x_I}-2h(c+S_0)
\big)+h^2x_I^2P^{(0)}\big(0,\omega,\tfrac12x_I\partial_{x_I},\partial_\omega\big)\Big]\tag{1.11}$$
$$\phantom{P_{\iota,h,z}} = -2R^{-1}\big(iz+hR\partial_R\big)\big(hR\partial_R+h(c+S_0)\big)+h^2R^{-2}P^{(0)}(0,\omega,-R
\partial_R,\partial_\omega).\tag{1.12}$$
It is a family in the semiclassical 0- and cone calculus on $\iota^+_{0\hbar,c\hbar}$ of II.A section 6.2, of
differential order 2, with weights $x_I^2$ at the face over $\iota^+\cap\mathscr I^+$ and $\rho_{\mathrm{cf}}^{-2}$ at
cf, and orders 0 at sf and tf ([Hin26c] (3.55a)-(3.55b)). Near $\iota^+\cap\mathscr I^+$ we use semiclassical 0-covectors
$\xi\frac{dx_I}{hx_I}+\eta\frac{d\omega}{hx_I}$, near $\iota^+\cap K^+$ semiclassical cone covectors
$\xi_{c\hbar}\frac{h+R}h\frac{dR}R+\frac{h+R}h\eta_{c\hbar}$; over sf ($h = 0$) near cf these are
$\xi_{c\hbar}\frac{dR}h+\frac Rh\eta_{c\hbar}$. The principal symbol at sf is
$$G_{\iota,z} = x_I^2\Big[\tfrac12(\xi-2z)\xi+|\eta|^2+\tfrac14x_I^2\xi^2\Big] = 2(z+R\xi_{c\hbar})\xi_{c\hbar}+\xi_{c
\hbar}^2+|\eta_{c\hbar}|^2,\tag{1.13}$$
from (1.11) with $hx_I\partial_{x_I}\mapsto i\xi$, $hx_I\partial_\omega\mapsto i\eta$, and from (1.12) with
$hR\partial_R\mapsto iR\xi_{c\hbar}$, $h\partial_\omega\mapsto iR\eta_{c\hbar}$ over sf:
$-2R^{-1}(iz+iR\xi_{c\hbar})(iR\xi_{c\hbar}) = 2(z+R\xi_{c\hbar})\xi_{c\hbar}$ and
$h^2R^{-2}((RD_R)^2+\Delta)\mapsto\xi_{c\hbar}^2+|\eta_{c\hbar}|^2$. The term $\frac14x_I^2\xi^2$, which the source's
(10.21) omits, vanishes at $\mathscr I^+$ and changes none of its conclusions there. At fibre infinity of the
semiclassical phase space the symbol is that of (1.10), positive definite, so the semiclassical characteristic set is a
compact subset of the face sf over $\iota^+$, away from fibre infinity ([Hin26c] section 10.1.1).

*Real $z$.* For $z = \pm1$ the characteristic set and the flow over sf are the pull-back of II.B Proposition 8.1
([Hin26c] Proposition 4.24) along the identification of the semiclassical phase space with the e3b-phase space over
$\iota^+$ at the time frequency $\mp1$ ([Hin26c] section 10.1.1). Its radial sets are
$$R_{I^+,\pm1,\mathrm{in}} := \{x_I = 0,\ \xi = \pm2,\ \eta = 0\},\qquad R_{I^+,\mathrm{out}} := \{x_I = 0,\ \xi = 0,\
\eta = 0\},$$
$$R_{\mathrm{cf},\pm1,\mathrm{in}} := \{R = 0,\ \xi_{c\hbar} = \mp2,\ \eta_{c\hbar} = 0\},\qquad R_{\mathrm{cf},
\mathrm{out}} := \{R = 0,\ \xi_{c\hbar} = 0,\ \eta_{c\hbar} = 0\},\tag{1.14}$$
all over sf. At $z = 1$: on $\{x_I = 0\}$, $G_{\iota,1}/x_I^2 = \frac12(\xi-1)^2-\frac12+|\eta|^2$; its Hamilton field in
the coordinates $(x_I,\omega;\xi,\eta)$ is
$$\mathsf H_I := H_{x_I^{-2}G_{\iota,1}} = (\xi-1)\big(x_I\partial_{x_I}+\eta\cdot\partial_\eta\big)-2|\eta|^2
\partial_\xi+x_IH_{|\eta|^2}\quad\text{at}\ x_I = 0\ \text{to first order},\tag{1.15}$$
with $H_{|\eta|^2} = 2\eta\cdot\partial_\omega$ at the centre of normal coordinates ([Hin26c] section 10.1.2 (1.2.1); the
computation is that of II.B (7.4) at the time frequency $-1$). It vanishes exactly at $R_{I^+,\pm1,\mathrm{in}}$ and
$R_{I^+,\mathrm{out}}$ on the characteristic set over $\{x_I = 0\}$, where $\xi(\xi-2) = -2|\eta|^2$. Near $\iota^+\cap
K^+$, with $\hat h := h/R$, the field of $G_{\iota,1}$ in the covectors
$\xi_{c\hbar}\frac{dR}h+\eta_{c\hbar}\frac{R\,d\omega}h$ is ([Hin26c] section 10.1.2 (1.3.1), by the change of variables)
$$\mathsf H_{\mathrm{cf}} := \hat h\Big(\big(2(1+2R)\xi_{c\hbar}+2\big)\big(R\partial_R-\eta_{c\hbar}\partial_{\eta_{c
\hbar}}\big)+2\big(|\eta_{c\hbar}|^2-R\xi_{c\hbar}^2\big)\partial_{\xi_{c\hbar}}+H_{|\eta_{c\hbar}|^2}\Big).\tag{1.16}$$
Up to the factor $\hat h$, it vanishes over $\{R = 0\}$ on the characteristic set exactly at
$R_{\mathrm{cf},1,\mathrm{in}}$ and $R_{\mathrm{cf},\mathrm{out}}$. The future flow has the types $(A,B)$ ($A$ the
$\alpha$-, $B$ the $\omega$-limit set): $A = R_{I^+,\pm1,\mathrm{in}}$ and $B = R_{I^+,\mathrm{out}}$ or
$R_{\mathrm{cf},\pm1,\mathrm{in}}$; $A = R_{\mathrm{cf},\pm1,\mathrm{in}}$ and $B = R_{\mathrm{cf},\mathrm{out}}$; $A =
R_{\mathrm{cf},\mathrm{out}}$ and $B = R_{I^+,\mathrm{out}}$ (II.B Proposition 8.1, the entries over $\iota^+$, pulled
back). $R_{I^+,\pm1,\mathrm{in}}$ is a source, $R_{I^+,\mathrm{out}}$ a sink, and $R_{\mathrm{cf},\pm1,\mathrm{in}}$,
$R_{\mathrm{cf},\mathrm{out}}$ are saddles: the stable manifold of $R_{\mathrm{cf},\pm1,\mathrm{in}}$ lies over $R>0$
(the curves from $R_{I^+,\pm1,\mathrm{in}}$), its unstable manifold over $R = 0$, which is the stable manifold of
$R_{\mathrm{cf},\mathrm{out}}$, whose unstable manifold lies over $R>0$ (the curves to $R_{I^+,\mathrm{out}}$).

*Complex $z$.* If $\mathrm{Im}\,z\ne0$, $\mathrm{Im}\,G_{\iota,z} = 2(\mathrm{Im}\,z)\xi_{c\hbar}$ (resp.
$-x_I^2(\mathrm{Im}\,z)\xi$) vanishes only where $\xi_{c\hbar} = 0$, and then $\mathrm{Re}\,G_{\iota,z}
= |\eta_{c\hbar}|^2$ forces $\eta_{c\hbar} = 0$; likewise in the 0-variables. So the characteristic set is the zero
section over sf, and the flow of the Hamilton field of $\mathrm{Re}(z^{-1}G_{\iota,z})$ on it, $2\hat hR\partial_R =
2h\partial_R$ near $R = 0$ and $-x_I\partial_{x_I}$ near $x_I = 0$ (up to positive factors), runs from
$R_{\mathrm{cf},\mathrm{out}}$, now a source, to the sink $R_{I^+,\mathrm{out}}$ ([Hin26c] (10.22), Figure 10.1).

*Orders.* Let $\mathsf s$ be an order function admissible for $P_0$ with weights $\alpha_+$, $0$ and margin 0 (II.C
Definition 5.2). It induces, as in [Hin26c] section 10.1.1 (via its pull-back along the identifications above), a
differential order $\mathsf s_{0,b}$ on ${}^{0,b}S^*\iota^+$, a differential order $\mathsf s_{0\hbar,c\hbar}$ at fibre
infinity of the semiclassical phase space, and semiclassical orders $\mathsf b_\pm$ on the face sf for
$\sigma\to\pm\infty$ ([Hin26c] (10.12)-(10.13)). By II.C Proposition 5.1 and Definition 2.4, pulled back: $\mathsf b_\pm$
is non-increasing along the future flow over sf, constant near the radial sets (1.14), and
$$\mathsf b_\pm+\alpha_+>\tfrac12(-1+\vartheta_{\mathrm{in}})\ \text{at}\ R_{\mathrm{cf},\pm1,\mathrm{in}},\qquad
\mathsf b_\pm+\alpha_+<-\tfrac12+\bar S\ \text{at}\ R_{\mathrm{cf},\mathrm{out}},\tag{1.17}$$
with the fibre inner products chosen as in II.C Definition 2.4 and Lemma 2.6 (up to any margin): these are Definition 2.4
(5)-(6) with $\alpha_{\mathrm{sf}} = \alpha_+$, $\alpha_K = 0$, as the 3b-regularity order at the radial sets over
$\partial K^+$ is the semiclassical order here ([Hin26c] (10.28) and after).

## 2. The semiclassical calculus on $\iota^+$, and the positive commutator scheme

The source's high-frequency analysis ([Hin26c] section 10.1.2) runs positive commutator arguments in the semiclassical 0-
and cone calculus on $\iota^+$ and "leave[s] the statements of standalone propagation estimates to the reader". This
section supplies them. The calculus is a parameterised scaled b.g. calculus, READ in II.A section 3; the positive
commutator scheme of I.B sections 2-5, proved there for the semiclassical scattering calculus on $\mathbb R^n$, uses of
its calculus only a short list of properties, and each holds here. The one structural difference is that remainders gain
only at the semiclassical face sf and in the differential order, not at the faces 0f, cf, tf; the dictionary (D1)-(D9)
below records what changes.

### 2.1 The space, the calculus and the orders

$\iota^+_\hbar := \iota^+_{0\hbar,c\hbar} = [[0,1)_h\times\iota^+;\{0\}\times(\iota^+\cap K^+)]$ (II.A section 6.2) has
four boundary hypersurfaces: sf, the lift of $\{h = 0\}$; tf, the front face; cf, the lift of $[0,1)\times(\iota^+\cap
K^+)$; and 0f, the lift of $[0,1)\times(\iota^+\cap\mathscr I^+)$. With $\rho_K = R/(1+R)$ as in section 1.1 we use the
defining functions
$$\rho_{\mathrm{sf}} := \frac h{h+\rho_K},\qquad\rho_{\mathrm{tf}} := h+\rho_K,\qquad\rho_{\mathrm{cf}} := \frac{
\rho_K}{h+\rho_K},\qquad\rho_{0\mathrm f} := (1+R)^{-1/2}.\tag{2.1}$$
$\rho_{0\mathrm f} = x_I(1+x_I^2)^{-1/2}$ near $\iota^+\cap\mathscr I^+$. Near $\mathrm{sf}\cap\mathrm{tf}$ the functions
$\hat h := h/R$ and $R$ are local defining functions of sf and tf, and $\rho_{\mathrm{sf}}/\hat h = R/\rho_K\cdot(1+\hat
h\,R/\rho_K)^{-1}$ is smooth and positive, equal to 1 at $\hat h = R = 0$; near $\mathrm{sf}\cap0\mathrm f$, $h$ and
$x_I$ are, and $\rho_{\mathrm{sf}}/h$, $\rho_{0\mathrm f}/x_I$ are smooth and positive, equal to 1 at $h = x_I = 0$. The
face sf is a copy of $\iota^+$: the centre $\{0\}\times(\iota^+\cap K^+)$ of the blow-up is a boundary hypersurface of
$\{0\}\times\iota^+$, and blowing one up does not change a manifold with corners.

*The structure.* By II.A section 6.2 ([Hin26c] section 3.2.4), for $h\in(0,1]$ the semiclassical 0- and cone structure is
the parameterised scaled b.g. structure (S7) on $(\iota^+)^\circ$ with the cells $U_{2,jk\pm}$, $U_{3,jk\pm}$ of II.A
section 6.2 (and finitely many cells covering a compact subset of $(\iota^+)^\circ$), the coefficient Lie algebra
$C^\infty_b\mathcal V_b(\iota^+)$, which does not depend on $h$, and the scalings $(1+\rho_K|\sigma|)^{-1}$, resp.
$(\langle\sigma\rangle^{-1},x_I\langle\sigma\rangle^{-1})$ at $|\sigma| = h^{-1}$: up to factors bounded above and below,
$h/(h+2^{-j})$ in every direction on $U_{2,jk\pm}$, $h$ in $x_I$ and $2^{-j}h$ in $\omega$ on $U_{3,jk\pm}$, and $h$ on
the interior cells. Its operator Lie algebra $\mathcal V_\hbar$ is spanned over $C^\infty_b(\iota^+)$, uniformly in $h$,
by $\frac h{h+\rho_K}\rho_K\partial_{\rho_K}$ and $\frac h{h+\rho_K}\partial_\omega$ near $\iota^+\cap K^+$, by
$hx_I\partial_{x_I}$ and $hx_I\partial_\omega$ near $\iota^+\cap\mathscr I^+$, and by $h\mathcal V(\iota^+)$ in between.

**Lemma 2.1.** (a) The scaling weight $\bar\rho$ of this structure (S1) satisfies $C^{-1}\rho_{\mathrm{sf}}\le\bar\rho\le
C\rho_{\mathrm{sf}}$ with $C$ independent of $h$. (b) For $a,c,l\in\mathbb R$, $\rho_{0\mathrm
f}^a\rho_{\mathrm{cf}}^c\rho_{\mathrm{tf}}^l$ and $\rho_{\mathrm{sf}}$ are weights (S2), uniformly in $h$. (c)
$P_{\iota,h,z}\in\rho_{0\mathrm f}^2\rho_{\mathrm{cf}}^{-2}\mathrm{Diff}^2_{\mathcal V_\hbar}$, with coefficients affine
in $z$ and bounded uniformly for $|z|\le2$ and $h\in(0,1]$.

*Proof.* (a) On $U_{2,jk\pm}$, $\rho_K\in(2^{-j-2},2^{-j+2})$, so $h/(h+2^{-j})$ and $\rho_{\mathrm{sf}}$ agree up to a
factor in $[\frac14,4]$. On $U_{3,jk\pm}$ the largest scaling is $h$, and $\rho_K\in[\frac12,1]$ there, so
$h\le2\rho_{\mathrm{sf}}\le2h$; likewise on the interior cells. (b) Put $\vartheta := \rho_K/(h+\rho_K)\in[0,1]$. Then
$\rho_K\partial_{\rho_K}\log\rho_{\mathrm{tf}} = \vartheta$, $\rho_K\partial_{\rho_K}\log\rho_{\mathrm{cf}} =
1-\vartheta$, $\rho_K\partial_{\rho_K}\log\rho_{\mathrm{sf}} = -\vartheta$ and $\rho_K\partial_{\rho_K}\vartheta =
\vartheta(1-\vartheta)$, so every derivative of the logarithms of these functions along $C^\infty_b\mathcal V_b(\iota^+)$
is a polynomial in $\vartheta$ with coefficients bounded uniformly in $h$; $\log\rho_{0\mathrm f}$ is $\log x_I$ plus a
smooth function near $\mathscr I^+$, and $x_I\partial_{x_I}\log x_I = 1$. So $Ww/w\in C^\infty_{\mathrm{uni}}$ uniformly
for each of these $w$. (c) Near $\iota^+\cap K^+$ (where we may use $R$ in place of $\rho_K$, the two being smooth
multiples of each other) put $V_1 := \frac h{h+R}R\partial_R$, $V_\omega := \frac h{h+R}\partial_\omega$. Then
$hR\partial_R = (h+R)V_1$, $R^{-1}(h+R) = \rho_{\mathrm{cf}}^{-1}$ and $R^{-1}h =
\rho_{\mathrm{sf}}\rho_{\mathrm{cf}}^{-1}$ up to smooth positive factors, $V_1(h+R) = \rho_{\mathrm{sf}}R$, so in (1.12)
$R^{-1}(iz+hR\partial_R)\in\rho_{\mathrm{cf}}^{-1}\mathrm{Diff}^1_{\mathcal V_\hbar}$,
$hR\partial_R+h(c+S_0)\in\mathrm{Diff}^1_{\mathcal V_\hbar}$ and
$h^2R^{-2}P^{(0)}(0,\omega,-R\partial_R,\partial_\omega)\in\rho_{\mathrm{cf}}^{-2}\mathrm{Diff}^2_{\mathcal V_\hbar}$.
Near $\iota^+\cap\mathscr I^+$, (1.11) is $x_I^2$ times a polynomial of degree 2 in $hx_I\partial_{x_I}$,
$hx_I\partial_\omega$ with coefficients bounded uniformly ($h^2x_I^2(x_I\partial_{x_I})^2 = x_I^2(hx_I\partial_{x_I})^2$,
$h^2x_I^2\partial_\omega^2 = (hx_I\partial_\omega)^2$, $h^2x_I^2\partial_\omega = hx_I\cdot hx_I\partial_\omega$).
$\square$

*Orders and spaces.* An *order* is $\mathbf o = (\mathsf s;a,c,l;\mathsf b)$: $a,c,l\in\mathbb R$ are the weights at 0f,
cf and tf, and $\mathsf s$ (the differential order) and $\mathsf b$ (the order at sf) are smooth functions on the
fibre-radially compactified phase space ${}^{0\hbar,c\hbar}\overline T^*\iota^+_\hbar$ of the structure, variable orders
in the sense of (S8). Put
$$w_{\mathbf o} := \langle\zeta\rangle^{\mathsf s}\rho_{0\mathrm f}^{-a}\rho_{\mathrm{cf}}^{-c}\rho_{\mathrm{tf}}^{-l}
\rho_{\mathrm{sf}}^{-\mathsf b},\qquad\mathbf e := (1;0,0,0;1),\qquad\mathbf e_1 := (1;0,0,0;0),\qquad
\mathbf m := (2;-2,2,0;0),\tag{2.2}$$
$\langle\zeta\rangle$ the fibre weight of the structure. $\Psi^{\mathbf o}$ is the class (S4)-(S5), (S8) with the weight
$\rho_{0\mathrm f}^{-a}\rho_{\mathrm{cf}}^{-c}\rho_{\mathrm{tf}}^{-l}$, differential order $\mathsf s$ and decay order
$\mathsf b$ at the scaling weight $\bar\rho\asymp\rho_{\mathrm{sf}}$ (Lemma 2.1), acting on $\mathbb C^N$-valued
functions componentwise, and taken in the subalgebra of (S10); $S^{\mathbf o}$ is its symbol class. $H^{\mathbf o} :=
\rho_{0\mathrm f}^a\rho_{\mathrm{cf}}^c\rho_{\mathrm{tf}}^l\rho_{\mathrm{sf}}^{\mathsf b}H^{\mathsf s}_\hbar$, with norm
$\|\cdot\|_{\mathbf o}$, is the space $H^{\mathsf s,(a,c,l,\mathsf b)}_{0\hbar,c\hbar,h}(\iota^+)$ of II.A section 6.2
and [Hin26c] (3.56), with $L^2 := L^2(\iota^+,\mu_b;\mathbb C^N)$ for the b-density $\mu_b$ of section 1.1 and a fibre
inner product $\mathfrak e$ on $\mathbb C^N$ (smooth on $\iota^+$); adjoints $A^*$ and the parts $\mathrm{Re}\,A :=
\frac12(A+A^*)$, $\mathrm{Im}\,A := \frac1{2i}(A-A^*)$ are taken in this $L^2$. By Lemma 2.1 (c),
$P_{\iota,h,z}\in\Psi^{\mathbf m}$. Orders are compared componentwise; $\mathbf o-K\mathbf e$ lowers the differential and
sf orders by $K$ and keeps the weights. For fixed $h>0$, $H^{\mathbf o}$ is the space $H^{\mathsf
s,(a,c)}_{0,b}(\iota^+)$ with an $h$-dependent equivalent norm ([Hin26c] after (10.31)): $\rho_{\mathrm{sf}}$ and
$\rho_{\mathrm{tf}}$ are then bounded above and below, and $\rho_{\mathrm{cf}}\asymp\rho_K$.

*Phase space.* $\mathcal P_\iota := {}^{0\hbar,c\hbar}\overline
T^*_{\mathrm{sf}}\iota^+_\hbar\cup{}^{0\hbar,c\hbar}S^*\iota^+_\hbar$ is the fibre-compactified phase space over sf
together with fibre infinity over all of $\iota^+_\hbar$; it is compact. The part over sf is a manifold with corners
whose boundary hypersurfaces are fibre infinity, $F_I$ (over $\mathrm{sf}\cap0\mathrm f = \{x_I = 0\}$) and $F_K$ (over
$\mathrm{sf}\cap\mathrm{tf} = \{R = 0\}$); $F_I\cap F_K = \emptyset$. On it we use the semiclassical 0-covectors
$\xi\frac{dx_I}{hx_I}+\eta\frac{d\omega}{hx_I}$ near $F_I$ and the semiclassical cone covectors of section 1.3 near
$F_K$, over sf $\xi_{c\hbar}\frac{dR}h+\eta_{c\hbar}\frac{R\,d\omega}h$. $\mathrm{WF}'(A)$ and
$\mathrm{Ell}(A)\subset\mathcal P_\iota$ are defined as in I.B Definition 2.9, with $S^{-K\mathbf e}$ in place of
$S^{-K\mathbf 1}$: $\varpi\notin\mathrm{WF}'(A)$ if the symbol of $A$ lies in $S^{-K\mathbf e}$ on a neighbourhood of
$\varpi$ in ${}^{0\hbar,c\hbar}\overline T^*\iota^+_\hbar$ for every $K$. The principal symbol of $A\in\Psi^{\mathbf o}$
is its symbol modulo $S^{\mathbf o-(1-\epsilon)\mathbf e}$, $\epsilon>0$ small (S8); over sf at finite frequencies it is
determined by its restriction to $\mathcal P_\iota$, as a symbol $w_{\mathbf o}a$ with $a$ smooth and vanishing at sf
lies in $S^{\mathbf o-(0;0,0,0;1)}$, which at finite frequencies is $S^{\mathbf o-\mathbf e}$.

**Lemma 2.2 (the calculus).** Uniformly for $h\in(0,1]$:
(a) $A\in\Psi^{\mathbf o'}$ maps $H^{\mathbf o}\to H^{\mathbf o-\mathbf o'}$ with norm bounded by a seminorm of $A$.
(b) $\Psi^{\mathbf o}\Psi^{\mathbf o'}\subset\Psi^{\mathbf o+\mathbf o'}$ with multiplicative principal symbols;
$(\Psi^{\mathbf o})^*\subset\Psi^{\mathbf o}$, the principal symbol of $A^*$ being the $\mathfrak e$-adjoint of that of
$A$; and if $A\in\Psi^{\mathbf o}$, $B\in\Psi^{\mathbf o'}$ have scalar principal symbols,
$A-\mathrm{Op}(a\,\mathrm{Id})\in\Psi^{\mathbf o-(1-\epsilon)\mathbf e}$ and
$B-\mathrm{Op}(b\,\mathrm{Id})\in\Psi^{\mathbf o'-(1-\epsilon)\mathbf e}$, then
$i[A,B]-\mathrm{Op}(H_ab\,\mathrm{Id})\in\Psi^{\mathbf o+\mathbf o'-(2-2\epsilon)\mathbf e}$, where $H_a$ is the Hamilton
field of the canonical symplectic form of $T^*(\iota^+)^\circ$ and $H_ab\in S^{\mathbf o+\mathbf o'-(1-\epsilon)\mathbf
e}$.
(c) (*Elliptic estimate.*) If $A\in\Psi^{\mathbf m'}$, $B,G\in\Psi^0$ and
$\mathrm{WF}'(B)\subset\mathrm{Ell}(A)\cap\mathrm{Ell}(G)$, then $\|Bu\|_{\mathbf o}\le C(\|GAu\|_{\mathbf o-\mathbf
m'}+\|u\|_{\mathbf o-K\mathbf e})$ for every $K$.
(d) I.B Lemma 2.2 holds for the classes $S^{\mathbf o}$, with the gains $(|\beta|,|\alpha|,0)$ of its (d) replaced by
$|\beta|\mathbf e_1$ for fibre derivatives and 0 for derivatives along the coefficient Lie algebra; a smooth function of
finitely many symbols in $S^0$, defined on a neighbourhood of the closure of their joint range, lies in $S^0$.
(e) I.B Lemma 2.12 holds with $L_h$ replaced by $L := 1+\log\langle\zeta\rangle+\log\rho_{\mathrm{sf}}^{-1}$.
(f) (*Localisation near sf.*) (i) If $a\in S^{\mathbf o}$ is supported in $\{\rho_{\mathrm{sf}}\ge\delta_0,\ |\zeta|\le
C_0\}$, then $a\in S^{\mathbf o-K\mathbf e}$ for every $K$, with seminorms bounded by $C_K\delta_0^{-K}$ times seminorms
of $a$. (ii) Let $\chi_0\in C^\infty(\mathbb R)$, $\chi_0 = 1$ on $(-\infty,1]$, $\chi_0 = 0$ on $[2,\infty)$, and $\phi
:= \chi_0(\rho_{\mathrm{sf}}/\delta_0)$. For $\delta\in(0,1]$, every order $\mathbf t$ and every $K$ there is $C$,
independent of $\delta_0\in(0,\frac18]$, with $\|\phi v\|_{\mathbf t-\delta\mathbf e}\le C\delta_0^\delta\|v\|_{\mathbf
t}+C\|v\|_{\mathbf t-K\mathbf e}$.
(g) (*Density.*) For fixed $h>0$, $z$ and orders $\mathbf o$, $C^\infty_c((\iota^+)^\circ)$ is dense in $\{u\in
H^{\mathbf o} : P_{\iota,h,z}u\in H^{\mathbf o-\mathbf m+\mathbf e}\}$ with the graph norm, and likewise for
$P^*_{\iota,h,z}$ and the orders $-\mathbf o+\mathbf m-\mathbf e$.

*Proof.* (a) is (S5) with (S7), (S8) and (S11), the weights by Lemma 2.1 (b) and the decay order at
$\bar\rho\asymp\rho_{\mathrm{sf}}$ by Lemma 2.1 (a). The density $\mu_b$ is $\bar\rho^4$ times a uniformly positive
$\mathcal V_\hbar$-density (the scalings multiply to $\bar\rho^4$ up to bounded factors, as $\dim\iota^+ = 4$), so
$L^2(\mu_b)$ is $\rho_{\mathrm{sf}}^{-2}$ times the $L^2$ space of (S3), up to an equivalent norm: a constant shift of
the sf order. (b) is (S5) and (S8): the principal symbol is taken modulo $\bigcap_\delta\bar\rho^{-\mathsf
b+1-2\delta}S^{\mathsf s-1+2\delta}$, and $\sigma(i[A_1,A_2]) = H_{\sigma(A_1)}\sigma(A_2)$. Adjoints with respect to
$\mu_b$ and $\mathfrak e$ differ from those of (S5) (the $\mathcal V_\hbar$-density and the Euclidean inner product) by
conjugation with the weight $\rho_{\mathrm{sf}}^{-4}$ and with the matrix of $\mathfrak e$, which preserve $\Psi^{\mathbf
o}$ and the principal symbol, by (b) itself and Lemma 2.1 (b). For the commutators, with $A' :=
A-\mathrm{Op}(a\mathrm{Id})$, $B' := B-\mathrm{Op}(b\mathrm{Id})$:
$[\mathrm{Op}(a\mathrm{Id}),\mathrm{Op}(b\mathrm{Id})]$ is a commutator of scalar operators acting componentwise, with
principal symbol $-iH_ab$ (S5); $[\mathrm{Op}(a\mathrm{Id}),B']$ and $[A',\mathrm{Op}(b\mathrm{Id})]$ are, entry by
entry, commutators of scalar operators, so gain $(1-\epsilon)\mathbf e$ beyond the product order $\mathbf o+\mathbf
o'-(1-\epsilon)\mathbf e$; and $A'B'$, $B'A'$ are each of order $\mathbf o+\mathbf o'-(2-2\epsilon)\mathbf e$. In the
scaled charts, $H_a = \sum_i\bar\rho_i(\partial_{\xi_i}a\,\partial_{x^i}-\partial_{x^i}a\,\partial_{\xi_i})$ with
$\bar\rho_i\le\bar\rho$ the scalings and $(x,\xi)$ the chart coordinates of (S4), whence $H_ab\in S^{\mathbf o+\mathbf
o'-\mathbf e}$. (c) is the microlocal elliptic estimate of (S5), with (S8) for variable orders, localised by the
composition calculus as in the proof of I.B Proposition 2.10. (d) The proof of I.B Lemma 2.2 uses only the form $\log
w_{\mathbf o} = \mathsf s\log\langle\zeta\rangle+\dots+\mathsf b\log\rho_{\mathrm{sf}}^{-1}$ and the chain rule;
derivatives along the coefficient Lie algebra of $\log\rho_F$ are bounded (Lemma 2.1 (b)) and fibre derivatives of
$\log\langle\zeta\rangle$ gain $\langle\zeta\rangle^{-1}$. A smooth function of $S^0$ symbols is in $S^0$ by the chain
rule. (e) The proof of I.B Lemma 2.12 uses (d) and the Cauchy formula only; (S8) admits the logarithmic factors (II.A
(S8), D195). (f) (i) On the support, $w_{\mathbf o-K\mathbf e}/w_{\mathbf o} =
\langle\zeta\rangle^{-K}\rho_{\mathrm{sf}}^K\ge(1+C_0)^{-K}\delta_0^K$, and the derivatives are handled by (d). (ii)
$\phi$ is a function on $\iota^+$ depending on $h$ whose derivatives along $C^\infty_b\mathcal V_b(\iota^+)$ are bounded
uniformly in $h$ and $\delta_0$ (on $\mathrm{supp}\,\chi_0'(\rho_{\mathrm{sf}}/\delta_0)$,
$\rho_{\mathrm{sf}}/\delta_0\in[1,2]$, and the derivatives of $\log\rho_{\mathrm{sf}}$ are bounded by (b) of Lemma 2.1);
so $\phi\in S^0$ with seminorms uniform in $\delta_0$, and $\mathrm{Op}(\phi)$ is multiplication by $\phi$, the
quantisation of (S4) being a left quantisation with $\psi(0) = 1$. Let $\phi_1 :=
\chi_0(\rho_{\mathrm{sf}}/(2\delta_0))$, which is 1 on $\mathrm{supp}\,\phi$, is supported in
$\{\rho_{\mathrm{sf}}\le4\delta_0\}$ and has the same uniformity. With $W_{\mathbf t} := \mathrm{Op}(w_{\mathbf t})$ and
$\phi_1\phi = \phi$,
$$W_{\mathbf t-\delta\mathbf e}\phi v = \rho_{\mathrm{sf}}^\delta\phi_1\cdot W_{\mathbf t-\delta\mathbf e}\rho_{
\mathrm{sf}}^{-\delta}\phi v+T'\phi v,\qquad T' := [W_{\mathbf t-\delta\mathbf e},\rho_{\mathrm{sf}}^\delta\phi_1]\rho_{
\mathrm{sf}}^{-\delta}.$$
Multiplication by $\rho_{\mathrm{sf}}^\delta\phi_1$ has $L^2$ norm at most $(4\delta_0)^\delta$; $W_{\mathbf
t-\delta\mathbf e}\rho_{\mathrm{sf}}^{-\delta}\phi\in\Psi^{\mathbf t-\delta\mathbf e_1}$ maps $H^{\mathbf t}$ to $L^2$
with norm $C$ by (a); and $T'\in\Psi^{\mathbf t-(\delta+1-\epsilon)\mathbf e}$ by (b), as
$\rho_{\mathrm{sf}}^\delta\phi_1\in S^{(0;0,0,0;-\delta)}$ and $\rho_{\mathrm{sf}}^{-\delta}\in S^{(0;0,0,0;\delta)}$;
all seminorms are uniform in $\delta_0$. So $\|\phi v\|_{\mathbf t-\delta\mathbf e}\le C(4\delta_0)^\delta\|v\|_{\mathbf
t}+C\|\phi v\|_{\mathbf t'-\mathbf e}$, $\mathbf t' := \mathbf t-(\delta-\epsilon)\mathbf e\le\mathbf t$ after decreasing
$\epsilon<\delta$. The same inequality with $\delta = 1$ at the order $\mathbf t'$ bounds the last norm by
$C(4\delta_0)\|v\|_{\mathbf t}+C\|\phi v\|_{\mathbf t'-(2-\epsilon)\mathbf e}$; after $N\ge K/(1-\epsilon)$ such steps
what remains is $C\|\phi v\|_{\mathbf t-K\mathbf e}\le C\|v\|_{\mathbf t-K\mathbf e}$, and
$(4\delta_0)\le(4\delta_0)^\delta$ as $4\delta_0\le1$. (g) For fixed $h$, $P_{\iota,h,z} = h^2N^0(h^{-1}z)$ is elliptic
in $x_I^2\rho_K^{-2}\mathrm{Diff}^2_{0,b}(\iota^+)$ (section 1.3), and the spaces are weighted 0,b-Sobolev spaces with
fixed weights. Let $J_\epsilon\in\Psi^{-\infty}_{0,b}$, $\epsilon\in(0,1]$, be uniformly bounded in $\Psi^0_{0,b}$, with
$J_\epsilon\to I$ strongly on every weighted 0,b-Sobolev space and $[N^0(\sigma),J_\epsilon]$ uniformly bounded in
$x_I^2\rho_K^{-2}\Psi^1_{0,b}$ and tending to 0 in $x_I^2\rho_K^{-2}\Psi^{1+\delta}_{0,b}$ (quantisations of
$\chi(\epsilon|\zeta|)$, (S5)); and let $\chi_j := \chi_0(-j^{-1}\log\rho_K)\chi_0(-j^{-1}\log x_I)$, whose b-, resp.
0-derivatives are $O(j^{-1})$, so that $[N^0(\sigma),\chi_j]$ tends to 0 in $x_I^2\rho_K^{-2}\mathrm{Diff}^1_{0,b}$ with
uniformly bounded coefficients. Then $u_{j,\epsilon} := \chi_jJ_\epsilon u\in C^\infty_c((\iota^+)^\circ)$ converges to
$u$ in the graph norm as $\epsilon\to0$ and then $j\to\infty$, as in the proof of I.B Lemma 3.1; the weights
$x_I^a\rho_K^c$ commute with $\chi_j$ and conjugate $J_\epsilon$ into a family with the same properties. $\square$

### 2.2 The positive commutator scheme

*Dictionary.* I.B sections 2.4-5 are written for the semiclassical scattering calculus. We read them in the semiclassical
calculus on $\iota^+$ with the following replacements.

(D1) The phase space $\mathcal P$ is $\mathcal P_\iota$; "Schwartz $u$" is $u\in C^\infty_c((\iota^+)^\circ)$, and
estimates proved for such $u$ extend to the graph spaces of Lemma 2.2 (g), every term being continuous there.

(D2) Orders $(s,\mathsf r,\mathsf b)$ are orders $\mathbf o$ as above, with $w_{\mathbf o}$ from (2.2); $\mathbf 1$ is
$\mathbf e$; $\mathbf m$ is (2.2); "$\Psi^0$" means $\Psi^{(0;0,0,0;0)}$.

(D3) The commutator carries no factor $h^{-1}$: (3.1) of I.B is replaced by
$$2\,\mathrm{Im}\langle\check APu,\check Au\rangle = \langle Cu,u\rangle,\qquad C := i[\mathrm{Re}\,P,\check A^2]+
\check A^2\,\mathrm{Im}\,P+\mathrm{Im}\,P\,\check A^2,\tag{2.3}$$
the gain $(1,1,0)$ of $h^{-1}[\cdot,\cdot]$ is $\mathbf e$, so (3.2) of I.B becomes $\mathbf k := \mathbf
o-\frac12(\mathbf m-\mathbf e)$, and every term $h^{-1}\|GPu\|_{\mathbf o-\mathbf m+(1,1,0)}$ becomes $\|GPu\|_{\mathbf
o-\mathbf m+\mathbf e}$. In I.B (4.3) and Lemma 5.1 (ii) the decomposition $h^{-1}\mathrm{Im}_h\mathbf P =
\epsilon_\flat(\mathcal P_1-\lambda\mathcal A)$ becomes $\mathrm{Im}\,\mathbf P = \epsilon_\flat(\mathcal
P_1-\lambda\mathcal A)$ with $\mathcal P_1\in\Psi^{\mathbf m-\mathbf e}$, $\lambda\in[0,2]$ a constant and $\mathcal
A\in\Psi^{\mathbf m-\mathbf e_1}$ (I.B: $\lambda\in[0,2h^{-1}]$ and $\mathcal A\in\Psi^{(1,0,0)}$, one order $h^{-1}$
above $\mathcal P_1$, as here $\mathcal A$ is one order $\rho_{\mathrm{sf}}^{-1}$ above).

(D4) The residual error $\|u\|_{-K\mathbf 1}$ is $\|u\|_{\mathbf o-K\mathbf e}$ (the weights at 0f, cf, tf are never
lowered).

(D5) Iteration lowers all of $\mathbf o$: in place of Lemma 3.4 of I.B, which lowers only the semiclassical order, the
iteration of I.B Corollary 4.6$'$ is used, applying Lemma 3.3 at the orders $\mathbf o-\frac{J-j}4\mathbf e$, $j =
1,\dots,J$; it needs the decomposition (3.3) of I.B at each of these orders, on the same nested sets, and leaves the
error $\|Gu\|_{\mathbf o-\frac J4\mathbf e}$ in place of $h^N\|Gu\|_{\mathbf o}$. The constant semiclassical scaling used
in I.B section 3.3 is not available here: $\rho_{\mathrm{sf}}$ is not constant on $\iota^+$ at fixed $h$.

(D6) The rescaled Hamilton field is $\mathsf H := w_{\mathbf m-\mathbf e}^{-1}H_{\mathrm{Re}\,G_{\iota,z}}$ in place of
$\mu^{-1}H$, so that $w_{\mathbf m-\mathbf e}w_{\mathbf k}^2 = w_{2\mathbf o}$ as $\mu w_{\mathbf k}^2 = w_{2\mathbf o}$
in I.B. It is a smooth vector field on ${}^{0\hbar,c\hbar}\overline T^*\iota^+_\hbar$ near $\mathcal P_\iota$, tangent to
sf, to fibre infinity and to the lifts of 0f and tf (its component along $\rho_{\mathrm{sf}}$ is
$\rho_{\mathrm{sf}}\mathsf H\log\rho_{\mathrm{sf}}$, as $H$ acts at fixed $h$); I.B Lemma 4.1 (c) is replaced by this
statement, which is checked in section 3.1.

(D7) Logarithms: $\log w_{\mathbf k} = (\mathsf s_{\mathbf k})\log\langle\zeta\rangle+k_{0\mathrm f}\log\rho_{0\mathrm
f}^{-1}+k_{\mathrm{cf}}\log\rho_{\mathrm{cf}}^{-1}+k_{\mathrm{tf}}\log\rho_{\mathrm{tf}}^{-1}+\mathsf b_{\mathbf
k}\log\rho_{\mathrm{sf}}^{-1}$. In the proofs of I.B Proposition 4.5 and Lemma 5.1, the term $2(\mathsf
r+\frac12)\varsigma\mathsf H\log\langle x\rangle$ of $\beta$ becomes $2\sum_Fk_F\varsigma\mathsf
H\log\rho_F^{-1}+2\mathsf b_{\mathbf k}\varsigma\mathsf H\log\rho_{\mathrm{sf}}^{-1}$ (the sum over 0f, cf, tf), smooth
near $\mathcal P_\iota$ by (D6); the weights $a,c,l$ are constants, so the terms $(\mathsf H\mathsf r)\log\langle
x\rangle$ and $\lambda_r$ are absent; and $\log\frac1h$ is $\log\rho_{\mathrm{sf}}^{-1}$, so $\lambda_b :=
-2\tilde\chi(\varsigma\mathsf H\mathsf b)\log\rho_{\mathrm{sf}}^{-1}\ge0$ satisfies the hypotheses of Lemma 2.2 (e).

(D8) The principal symbol $G_{\iota,z}$ of $P_{\iota,h,z}$ is affine in $z$ ((1.13)), so the field of
$\mathrm{Re}\,G_{\iota,z}$ depends only on $\mathrm{Re}\,z$: $\mathsf H_z = \mathsf H_{\mathrm{Re}\,z}$ in I.B (4.1), and
the term $c_b$ of I.B Proposition 4.5 vanishes.

(D9) *Localisation near sf.* Every commutant is multiplied by $\phi = \chi_0(\rho_{\mathrm{sf}}/\delta_0)$, with
$\delta_0\in(0,\frac18]$ fixed small; so every commutant is supported in $\{\rho_{\mathrm{sf}}\le2\delta_0\}$, where the
functions used to build it need only be defined. Near $F_I$ and over compact subsets of the interior of sf,
$\rho_{\mathrm{sf}}\le2h$, so $\phi = 1$ there once $h<\delta_0/2$. The new terms in $2\varphi\,\varsigma\mathsf
H\varphi$ produced by $\chi_0'$ are supported in $\{\delta_0\le\rho_{\mathrm{sf}}\le2\delta_0\}$ at finite frequencies,
and, whatever their sign, contribute at most $C_{\delta_0}\|u\|^2_{\mathbf o-K\mathbf e}$, by Lemma 2.2 (f) (i) and (a).
Where I.B absorbs a term because it carries a positive power of $h$ (the middle term in *Positivity of absorbing terms*,
I.B section 3.3), Lemma 2.2 (f) (ii) is used instead, with $\delta_0$ small. Constants below depend on $\delta_0$.

**Proposition 2.3 (transfer).** Under (D1)-(D9), the following statements of I.B hold for the semiclassical calculus on
$\iota^+$, for every family of operators $\mathbf P$ in $\Psi^{\mathbf m}$ with real scalar principal symbol for
$\mathrm{Re}\,\mathbf P$, uniformly for the parameters in compact sets as there, with the proofs given there: Proposition
2.10 (with Lemma 2.2 (c)), Lemmas 2.11 and 2.12, Lemma 3.2 and the paragraph after it, Lemma 3.3, the iteration of (D5),
the paragraph *Positivity of absorbing terms* of section 3.3 (with (D9)), Lemmas 4.3 and 4.4, Proposition 4.5 with Remark
4.7, Corollaries 4.6 and 4.6$'$, and Lemma 5.1.

*Proof.* The proofs in I.B use of the calculus: the mapping property (Proposition 2.8), the composition and adjoint
theorems with the principal symbols of products, adjoints and commutators (Theorems 2.4, 2.5 and (2.5)), the elliptic
estimate (Proposition 2.10), the symbol properties of Lemma 2.2, the square roots of Lemma 2.11 and Lemma 2.12, and the
$L^2$ pairing of $H^{\mathbf o}$ with $H^{-\mathbf o}$. These are Lemma 2.2 (a)-(e) here, the pairing being (S3) and
(S11) with the weight shift of the proof of Lemma 2.2 (a). Lemmas 4.3 and 4.4 are statements about vector fields on a
manifold with corners of codimension at most 2 and about one function of one variable; $\mathcal P_\iota$ over sf has
codimension at most 2 ($F_I\cap F_K = \emptyset$). The remainder classes of I.B are of the form $\Psi^{2\mathbf
o-\theta\mathbf 1+\epsilon\mathbf 1}$, $\theta\in\{\frac12,1\}$; here they are $\Psi^{2\mathbf o-\theta\mathbf
e+\epsilon\mathbf e}$, by Lemma 2.2 (b) with (D3), and every place where I.B bounds such a remainder uses only its order
in the scale $\mathbf 1$, now $\mathbf e$, against the error $\|Gu\|_{\mathbf o-\frac14\mathbf e}$, which the iteration
(D5) carries down to $\|Gu\|_{\mathbf o-\frac J4\mathbf e}$. Two places use more. (1) In *Positivity of absorbing terms*
the middle term $C\|\check Aw\|^2_{\mathbf t-\frac12(1-\epsilon)\mathbf e}$ is bounded, after the factor $\phi$ of (D9)
is put into $\check A$ (so that $(1-\phi_1)\check A$ is residual, $\phi_1 = \chi_0(\rho_{\mathrm{sf}}/(2\delta_0))$), by
$C(C_1(2\delta_0)^{(1-\epsilon)/2}\|\check Aw\|_{\mathbf t}+C_2\|\check Aw\|_{\mathbf t-K\mathbf e})^2$ (Lemma 2.2 (f)
(ii) applied to $\phi_1\check Aw$); for $\delta_0$ small the first part is absorbed by $\frac c2\|\check Aw\|^2_{\mathbf
t}$, and the second is bounded by $C\|Gw\|^2_{\mathbf k+\mathbf t-K\mathbf e}$. With $\lambda\le2$ (D3), $\langle
Fw,w\rangle\ge-C\|Gw\|^2_{\mathbf k+\mathbf t-K\mathbf e}$, which is of the class of the residual errors for $K$ large.
(2) In I.B Proposition 4.5 and Lemma 5.1 the semiclassical weight $h^{-\mathsf b}$ is a constant on phase space at fixed
$h$; here $\rho_{\mathrm{sf}}^{-\mathsf b}$ is not, and its derivative along $\mathsf H$ is the term $2\mathsf b_{\mathbf
k}\varsigma\mathsf H\log\rho_{\mathrm{sf}}^{-1}$ of (D7), smooth near $\mathcal P_\iota$: it is part of $\beta$, bounded
on $U_1$ in Proposition 4.5 (absorbed by $M$) and evaluated at the radial set in Lemma 5.1, exactly as the term with
$\log\langle x\rangle$ is in I.B. Nothing else in those proofs depends on $\mathsf b$ being multiplied by a constant.
$\square$

We state the consequences used in sections 3-4. Let $Z\subset\{|z|\in[\frac12,2]\}$ be compact, $c_z\in\{1,z^{-1}\}$,
$J\ge1$, and $P' := P_{\iota,h,z}\otimes\mathrm{Id}_{\mathbb C^J}+P''$ with $P''\in\Psi^{\mathbf m-\mathbf e}$ (acting on
$\mathbb C^N\otimes\mathbb C^J$, with the fibre inner product $\mathfrak e^{\oplus J}$), continuous in $z$; let $\mathbf
P$ be one of $c_zP'$, $(c_zP')^*$, with $\epsilon_\flat := 1$, resp. $-1$. ($P'' = 0$, $J = 1$ in section 3.)

**Proposition 2.4 (radial estimate; I.B Lemma 5.1).** Let $F\in\{F_I,F_K\}$ with defining function $\varrho$ ($x_I$,
resp. $R$) on $\mathcal P_\iota$, $Z'\subset Z$ compact, $\Lambda\subset F$ compact, $U_0\subset\mathcal P_\iota$ a
neighbourhood of $\Lambda$ at finite frequencies with compact closure, and $\varsigma\in\{1,-1\}$. Suppose, uniformly for
$z\in Z'$:
(i) $\mathrm{Re}\,\mathbf P-\mathrm{Op}(p_z\mathrm{Id})\in\Psi^{\mathbf m-\mathbf e}$ with $p_z$ real, continuous in $z$;
$\mathsf H^{\mathbf P}_z := w_{\mathbf m-\mathbf e}^{-1}H_{p_z}$ vanishes on $\Lambda$; and $\beta_\varrho :=
\varrho^{-1}\varsigma\mathsf H^{\mathbf P}_z\varrho$ satisfies $\beta_\varrho\ge\beta_*$ on $U_0$ (*$\varrho$-source*) or
$\beta_\varrho\le-\beta_*$ on $U_0$ (*$\varrho$-sink*), $\beta_*>0$.
(ii) $\mathrm{Im}\,\mathbf P = \epsilon_\flat(\mathcal P_1-\lambda\mathcal A)$ as in (D3), $\mathcal P_1$ self-adjoint
with principal symbol $p_1$, and either (A) $\epsilon_\flat\varsigma\mathcal A$ is self-adjoint with principal symbol
$\ge c_0w_{\mathbf m-\mathbf e_1}\mathrm{Id}$ on $U_0$; or (B) $\epsilon_\flat\varsigma = 1$ and $\mathcal A =
\sum_{j,k}W_j^*\tilde M_{jk}W_k+\mathcal A_0+\mathcal A_1$ with $W_j\in\mathrm{Diff}^1_{\mathcal V_\hbar}$ scalar, acting
componentwise, $\tilde M = (\tilde M_{jk})\ge0$ and $\mathcal A_0\ge0$ matrix functions (for $\mathfrak e^{\oplus J}$,
resp. $\mathfrak e$, pointwise), and $\mathcal A_1$ a differential operator whose coefficients vanish near the base
projection of $\bar U_0$.
(iii) There are real $g,\phi$, smooth near $\mathcal P_\iota$ and continuous in $z$, $\phi\ge0$, with $\Lambda = \bar
U_0\cap\{\varrho = 0,\ \phi = 0,\ g = 0\}$, $|w_{\mathbf m}^{-1}\mathbf g_z|\ge c|g|-C\varrho$ on $U_0$ ($\mathbf g_z$
the principal symbol of $\mathbf P$), and, on $U_0$, either $\varsigma\mathsf H^{\mathbf P}_z\phi\ge
c_1\phi-C_1(\varrho+g^2)$ (*$\phi$-source*) or $\varsigma\mathsf H^{\mathbf P}_z\phi\le-c_1\phi+C_1(\varrho+g^2)$
(*$\phi$-sink*).
(iv) $\mathsf b$ is constant on $U_0$. Let $\tilde\kappa$ be the exponent with $w_{\mathbf k} = \varrho^{-\tilde\kappa}f$
near $\Lambda$, $f>0$ smooth near $\Lambda$ up to a factor depending on $h$ only ($\tilde\kappa = k_{0\mathrm f} = a+1$
at $F_I$, where $\rho_{\mathrm{sf}}\asymp h$; $\tilde\kappa = k_{\mathrm{tf}}-\mathsf b_{\mathbf k} = l-\mathsf
b-\frac12$ at $F_K$, where $\rho_{\mathrm{tf}}^{-k_{\mathrm{tf}}}\rho_{\mathrm{sf}}^{-\mathsf b_{\mathbf k}} = R^{\mathsf
b_{\mathbf k}-k_{\mathrm{tf}}}h^{-\mathsf b_{\mathbf k}}$ times a smooth positive factor).
(v) (*Threshold.*) On $\Lambda$, $\mathcal T := 2\tilde\kappa\beta_\varrho\mathrm{Id}-2\varsigma\epsilon_\flat w_{\mathbf
m-\mathbf e}^{-1}p_1\ge c_{\mathcal T}\mathrm{Id}$, $c_{\mathcal T}>0$.
Then for every $J\in\mathbb N$ such that (iv)-(v) also hold with $\mathsf b$ replaced by $\mathsf b-\frac j4$, $0\le j\le
J-1$ (only $\mathsf b$ moves $\tilde\kappa$, and only at $F_K$; for $J = 1$ this is no further condition), there are a
neighbourhood $U_*$ of $\Lambda$ and a compact $K_E\subset\bar U_0\setminus\Lambda$ such that for $B_*$ microsupported in
$U_*$, $G$ elliptic on $\bar U_0$, $E'$ elliptic on $K_E$, all $K$, $z\in Z'$, $h<h_0$ and $u\in
C^\infty_c((\iota^+)^\circ)$,
$$\|B_*u\|_{\mathbf o}\le C\big(\|G\mathbf Pu\|_{\mathbf o-\mathbf m+\mathbf e}+\delta\|E'u\|_{\mathbf o}+\|Gu\|_{
\mathbf o-\frac J4\mathbf e}+\|u\|_{\mathbf o-K\mathbf e}\big),\tag{2.4}$$
with $\delta := 0$ if $\Lambda$ is a $\varrho$-source and a $\phi$-source, and $\delta := 1$ otherwise; $K_E$ lies in
$\{\varrho\ge\delta_1\}$ when only the $\varrho$-part is a sink, and in $\{\phi\ge\delta_2\}$ when only the $\phi$-part
is.

*Proof.* This is I.B Lemma 5.1 under the dictionary (Proposition 2.3), with one generalisation: there the $\varrho$-part
and the $\phi$-part are both sources or both sinks; here they may differ. In that proof the derivative of the cut-off is
$k_1+k_2+k_3$, and $k_1$ (from $\chi_0(\varrho/\delta_1)$) has the sign of $-\beta_\varrho\varrho$, $k_2$ (from
$\chi_0(\phi/\delta_2)$) that of $\mp1$, each on its own support; each is written as $-f_i^2$ or $e_i^2$ according to its
own sign, with the same square roots. The threshold uses only $\beta_\varrho$ (the derivative of $w_{\mathbf k}$ at
$\Lambda$, where $\mathsf H^{\mathbf P}_z$ vanishes), so (v) is unchanged; the sets carrying $e_i$ are
$\mathrm{supp}\,k_i$, closed and disjoint from $\Lambda$. The iteration (D5) needs the commutant at each order $\mathbf
o-\frac{J-j}4\mathbf e$, $1\le j\le J$, that is at $\mathsf b-\frac i4$, $0\le i\le J-1$: the cut-offs do not depend on
the order, $\mathsf s$ does not enter at finite frequencies, and the threshold at the lowered orders is the hypothesis on
$J$. $\square$

**Proposition 2.5 (propagation; I.B Proposition 4.5, Corollary 4.6 and Remark 4.7).** Let $\varsigma$ be a sign, $z_*\in
Z$, and $\gamma:[-T,0]\to\mathcal P_\iota$ an integral curve of $\varsigma\mathsf H_{z_*}$, at finite frequencies, on
which $\mathsf H_{z_*}\ne0$, where $\mathsf H_z := w_{\mathbf m-\mathbf e}^{-1}H_{\mathrm{Re}(c_zG_{\iota,z})}$. Let
$U_0$ be a neighbourhood of $\gamma([-T,0])$ on which $\varsigma\mathsf H_z\mathsf b\le0$ for $z\in Z$. Suppose
$\mathrm{Im}\,\mathbf P = \epsilon_\flat(\mathcal P_1-\lambda\mathcal A)$ as in (D3) with either $|\lambda|\le Ch$ (then
$\lambda\mathcal A\in\Psi^{\mathbf m-\mathbf e}$, as $h\le2\rho_{\mathrm{sf}}$, and is part of $\mathcal P_1$), or (A) of
Proposition 2.4 on $U_0$, or (B) of Proposition 2.4 on $U_0$. Then for every neighbourhood $W$ of $\gamma(-T)$ there are
a neighbourhood $Z_0$ of $z_*$ in $Z$, a neighbourhood $U_*$ of $\gamma(0)$ and a compact $K_E\subset W$ such that for
all $J$, $K$, $B_*$ microsupported in $U_*$, $E'$ elliptic on $K_E$, $G$ elliptic on $\bar U_0$, $z\in Z_0$, $h<h_0$ and
$u\in C^\infty_c((\iota^+)^\circ)$,
$$\|B_*u\|_{\mathbf o}\le C\big(\|G\mathbf Pu\|_{\mathbf o-\mathbf m+\mathbf e}+\|E'u\|_{\mathbf o}+\|Gu\|_{\mathbf o-
\frac J4\mathbf e}+\|u\|_{\mathbf o-K\mathbf e}\big).\tag{2.5}$$

*Proof.* I.B Proposition 4.5, Corollaries 4.6 and 4.6$'$ under the dictionary; Remark 4.7 (a) for $|\lambda|\le Ch$ and
(b) for case (B). In case (A) the hypothesis $\epsilon_\flat\varsigma\hat q_{z_*}>0$ of I.B Proposition 4.5 is the
positivity in (A). By (D8), $\mathsf H_z$ depends on $z$ only through $\mathrm{Re}\,z$ when $c_z = 1$; when $c_z =
z^{-1}$ it is a polynomial in $\mathrm{Re}\,z^{-1}$ and $\mathrm{Im}\,z^{-1}$, smooth in $z$, and the flow boxes of I.B
Lemma 4.3 are taken with the parameter $(\mathrm{Re}\,z,\mathrm{Im}\,z)$, as there. The monotonicity is needed for
$\mathsf b$ only, the weights being constant (D7). $\square$

**Proposition 2.6 (elliptic estimate; I.B Proposition 4.2).** If $K\subset\mathcal P_\iota$ is compact, $w_{\mathbf
m}^{-1}c_zG_{\iota,z}$ is bounded away from 0 on $K$ for $z\in Z$, $\mathrm{WF}'(B)\subset K$ and $G$ is elliptic on $K$,
then $\|Bu\|_{\mathbf o}\le C(\|G\mathbf Pu\|_{\mathbf o-\mathbf m}+\|u\|_{\mathbf o-K\mathbf e})$, uniformly for $z\in
Z$ and $h<h_0$. Fibre infinity of $\mathcal P_\iota$ lies in $\mathrm{Ell}(P')$ for every $z$, by (1.10), $P''$ being of
lower order.

*Proof.* Lemma 2.2 (c) and the compactness argument of I.B Proposition 4.2. At fibre infinity the principal symbol of
$P_{\iota,h,z}$ is $h^2$ times that of $N^0(h^{-1}z)$ in the rescaled fibre variables, which is (1.10), positive definite
and independent of $z$; the terms involving $z$ are of lower differential order, and the principal symbol of $\mathbf P$
is $c_zG_{\iota,z}$ (or its conjugate) times the identity, $P''$ being of lower order. $\square$

## 3. High frequencies without b-regularity ([Hin26c] Proposition 10.6 (2), $k = 0$)

### 3.1 The statement

Throughout this section and the next we assume
$$\gamma_I<\tfrac32+\bar S,\qquad\gamma_+<\gamma_I,\tag{3.1}$$
with $\gamma_I,\gamma_+,\gamma_{\mathrm{cf}} = -(\alpha_++2)$ as in (1.2). The orders are those of section 1.3: an order
$\mathsf s'$ at fibre infinity (any variable order; $P_{\iota,h,z}$ is elliptic there), and at sf the orders $\mathsf
b_\pm$ with (1.17), together with a constant $\mathsf b_{\mathrm{mid}}$ with $\mathsf
b_{\mathrm{mid}}+\alpha_+<-\frac12+\bar S$. The parameters are
$$\mathcal Z^\pm_h := \{\pm1+iy : -h\gamma_+\le y\le1\},\qquad\mathcal Z^i := \{x+i : |x|\le1\},\tag{3.2}$$
with $\mathsf b := \mathsf b_\pm$ for $z\in\mathcal Z^\pm_h$ and $\mathsf b := \mathsf b_{\mathrm{mid}}$ for
$z\in\mathcal Z^i$ (a point $\pm1+i$ of both families is taken with either order), and
$$\mathbf o := (\mathsf s';2\gamma_I,\gamma_{\mathrm{cf}},\gamma_{\mathrm{cf}};\mathsf b),\qquad Y_{\mathbf o} := H^{(
\mathsf s'-2;2\gamma_I+2,\gamma_{\mathrm{cf}}-2,\gamma_{\mathrm{cf}};\mathsf b+1)}.\tag{3.3}$$
Every $\sigma\in\mathbb C$ with $\mathrm{Im}\,\sigma\ge-\gamma_+$ and $|\sigma|\ge\sqrt2h_0^{-1}$ is $h^{-1}z$ with
$h\in(0,h_0)$ and $z$ in one of the families: if $|\mathrm{Re}\,\sigma|\ge\mathrm{Im}\,\sigma$, $h
:= |\mathrm{Re}\,\sigma|^{-1}$ and $z := \pm1+ih\,\mathrm{Im}\,\sigma$; otherwise $h := (\mathrm{Im}\,\sigma)^{-1}$ and
$z := h\,\mathrm{Re}\,\sigma+i$.

**Proposition 3.1 ([Hin26c] Proposition 10.6 (2) at $n = 4$, $k = 0$).** Assume (3.1). There are $h_0>0$ and $C$ such
that for $h\in(0,h_0)$ and $z$ in $\mathcal Z^\pm_h$ or $\mathcal Z^i$, with the orders above,
$$\|u\|_{\mathbf o}\le C\|P_{\iota,h,z}u\|_{Y_{\mathbf o}},\tag{3.4}$$
and $P_{\iota,h,z}:H^{\mathbf o}\to Y_{\mathbf o}$ is invertible. Equivalently, $N^0(h^{-1}z):H^{\mathsf
s',(2\gamma_I,\gamma_{\mathrm{cf}})}_{0,b}(\iota^+)\to H^{\mathsf
s'-2,(2\gamma_I+2,\gamma_{\mathrm{cf}}-2)}_{0,b}(\iota^+)$ is invertible (for fixed $h$ these are the same spaces,
section 2.1).

The source states (2) for all $|z|\in[\frac12,2]$ with $\mathrm{Im}\,z\ge-h\gamma_+$, with $\mathsf b = \mathsf b_\pm$
where $|z\mp1|\le\frac12$ and $\mathsf b$ "an arbitrary constant otherwise". Its argument does not give that. $\mathsf
b_\pm$ is adapted to the radial sets of the real part at $\mathrm{Re}\,z = \pm1$, (1.14); for real $z\ne\pm1$ they lie at
$\xi_{c\hbar} = \mp2z$, where $\mathsf b_\pm$ need be neither constant nor monotone (the order adapted there is $\mathsf
b_\pm$ dilated by $z$, by the scaling $P_{\iota,h,z} = z^2P_{\iota,h/z,1}$, $z>0$). And a constant order must satisfy the
threshold at $R_{\mathrm{cf},\mathrm{out}}$, which for $\mathrm{Im}\,z\ge\nu$ is a source of the flow on the zero section
(Lemma 3.3 (R4)). The families (3.2) keep $\mathrm{Re}\,z = \pm1$ near the real axis and cover every $\sigma$; this is
what section 6 uses (section 9, (F2)).

### 3.2 Symbols

$\mu_b := |\frac{dR}R\,d\slashed g|$ on all of $\iota^+$ (a b-density at both ends, as $\frac{dR}R =
-2\frac{dx_I}{x_I}$), and fibre inner products $\mathfrak e$ are taken to depend on $\omega$ only near both ends; each
radial estimate below uses its own $\mathfrak e$ (the norms are equivalent). Write $\mathrm{Re}\,S_0 :=
\frac12(S_0+S_0^{*\mathfrak e})$, $P := P_{\iota,h,z}$ and $\tilde P := z^{-1}P$.

**Lemma 3.2.** (a) $N^0(\sigma) = N^0(0)+\sigma\,\partial_\sigma N^0$ with $\partial_\sigma N^0 =
-2iR^{-1}(R\partial_R+c+S_0)$, so $P = h^2N^0(0)+hz\,\partial_\sigma N^0$. With $Q_0 := \mathrm{Im}\,\partial_\sigma N^0$
and $Q_1 := -h\,\mathrm{Re}\,\partial_\sigma N^0$,
$$\mathrm{Im}\,P = \mathcal P_1(\mathrm{Re}\,z)-(\mathrm{Im}\,z)Q_1,\qquad\mathcal P_1(x) := h^2\,\mathrm{Im}\,N^0(0)+x
\,hQ_0,\tag{3.5}$$
$$\mathrm{Im}\,\tilde P = \tilde{\mathcal P}_1(z)-\frac{\mathrm{Im}\,z}{|z|^2}\mathcal A,\qquad\tilde{
\mathcal P}_1(z) := hQ_0+\mathrm{Re}(z^{-1})\,h^2\,\mathrm{Im}\,N^0(0),\qquad\mathcal A := h^2\,\mathrm{Re}\,N^0(0).
\tag{3.6}$$
(b) $Q_0 = -R^{-1}(4+2\,\mathrm{Re}\,S_0)$ exactly, on all of $\iota^+$ ($R^{-1} = x_I^2$ near $\mathscr I^+$).
$Q_1\in\Psi^{\mathbf m-\mathbf e_1}$, $\mathcal P_1,\tilde{\mathcal P}_1\in\Psi^{\mathbf m-\mathbf e}$ and $\mathcal
A\in\Psi^{\mathbf m}$, uniformly for $|z|\le2$, $|z|\ge\frac12$ in (3.6).
(c) Over sf: $\sigma(Q_1) = -2\xi_{c\hbar}$ near $F_K$ and $x_I^2\xi$ near $F_I$ (consistently: $\xi_{c\hbar} =
-\frac12x_I^2\xi$ where both are defined); $\sigma(\mathcal A) = (1+2R)\xi_{c\hbar}^2+|\eta_{c\hbar}|^2$ near $F_K$ and
$x_I^2(\frac12\xi^2+|\eta|^2+\frac14x_I^2\xi^2)$ near $F_I$. Moreover $\mathcal A = \sum_{j,k}W_j^*\tilde
M_{jk}W_k+\mathcal A'$ with $W_j\in\mathrm{Diff}^1_{\mathcal V_\hbar}$ scalar, acting componentwise, $\tilde M\ge0$ a
scalar matrix function, and $\mathcal A'\in\Psi^{\mathbf m-\mathbf e}$ self-adjoint with principal symbol vanishing on
the zero section over sf.
(d) With $\varpi := hx_I^2$ near $F_I$ and $\varpi := \rho' := h/(h+R)$ near $F_K$, at $R = 0$, resp. $x_I = 0$, over sf,
and $\mathrm{Re}\,z = 1$:
$$\varpi^{-1}\sigma(\mathcal P_1(1)) = \big(\tfrac52+\mathrm{Re}\,S_0\big)\xi-(4+2\,\mathrm{Re}\,S_0)\quad
\text{near }F_I,\tag{3.7}$$
$$\varpi^{-1}\sigma(\mathcal P_1(1)) = -\big(\tfrac12p_{\mathrm{in}}+4\big)\xi_{c\hbar}+b\cdot\eta_{c\hbar}-(4+2\,
\mathrm{Re}\,S_0)\quad\text{near }F_K,\tag{3.8}$$
and $\varpi^{-1}\sigma(\tilde{\mathcal P}_1(z)) = -(4+2\,\mathrm{Re}\,S_0)$ on the zero section at $F_I$ and at $F_K$,
for every $z$. Here $p_{\mathrm{in}}(\omega)$ is the endomorphism of I.A (1.5) (II.C Lemma 2.6), $\xi a$ with $a =
-\frac12p_{\mathrm{in}}$ being the scattering symbol at $\partial X$, at $\xi\,dr$, of $\rho^{-1}\mathrm{Im}\,\hat P(0)$
for the Euclidean density, and $b(\omega)$ an endomorphism-valued covector.

*Proof.* (a) (1.6) is affine in $\sigma$. $\mathrm{Im}(zA) =
\mathrm{Re}\,z\,\mathrm{Im}\,A+\mathrm{Im}\,z\,\mathrm{Re}\,A$ gives (3.5); for (3.6), $\tilde P =
z^{-1}h^2N^0(0)+h\,\partial_\sigma N^0$, and $\mathrm{Im}(z^{-1}) = -\mathrm{Im}\,z/|z|^2$.

(b) $\partial_\sigma N^0 = iY$ with $Y := -2R^{-1}(R\partial_R+c+S_0)$, so $Q_0 = \mathrm{Re}\,Y$. For $\mu_b$,
$(R\partial_R)^* = -R\partial_R$ and $[R\partial_R,R^{-1}] = -R^{-1}$, so $\mathrm{Re}(R^{-1}R\partial_R) =
\frac12(R^{-1}R\partial_R-R\partial_RR^{-1}) = \frac12R^{-1}$; $\mathfrak e$ does not depend on $R$, so
$\mathrm{Re}(R^{-1}S_0) = R^{-1}\mathrm{Re}\,S_0$. Hence $Q_0 = -R^{-1}(1+2c+2\,\mathrm{Re}\,S_0)$, and $1+2c = 4$. The
classes follow from Lemma 2.1 (c) and the factor $h\le2\rho_{\mathrm{sf}}$ in $hQ_0$ and in the terms of
$h^2\,\mathrm{Im}\,N^0(0)$, which are $h$ times semiclassical operators of first order (the imaginary part of a
second-order operator with real scalar principal symbol has first order).

(c) $Q_1 = h\,\mathrm{Im}\,Y$ ($\mathrm{Re}(iY) = -\mathrm{Im}\,Y$), and $h\,(-2R^{-1}R\partial_R) =
-2R^{-1}(hR\partial_R)$ with $hR\partial_R\mapsto i(h+R)\xi_{c\hbar} = iR(1+\hat h)\xi_{c\hbar}$ in the covectors of
section 1.3, so its symbol is $-2i(1+\hat h)\xi_{c\hbar}$, whose imaginary part is $-2(1+\hat h)\xi_{c\hbar}$, $=
-2\xi_{c\hbar}$ over sf. Near $F_I$, $\partial_\sigma N^0 = ix_I^2(x_I\partial_{x_I}-2(c+S_0))$ by (1.6), and
$hx_I\partial_{x_I}\mapsto i\xi$ gives $x_I^2\xi$. $\sigma(\mathcal A)$ is the real part of the symbol of $h^2N^0(0)$,
which is (1.13) with $z = 0$. For the decomposition: by II.C Lemma 1.2,
$P^{(0)}(0,\omega,\rho\partial_\rho,\partial_\omega) = ((\rho D_\rho)^2+\Delta_{\mathbb S^3})\mathrm{Id}+P^{(0)}_1$ with
$P^{(0)}_1\in\mathrm{Diff}^1_b$, so near $\iota^+\cap K^+$
$$h^2N^0(0) = h^2R^{-2}\big((1+2R)(RD_R)^2+\Delta_{\mathbb S^3}\big)\mathrm{Id}-2h^2R^{-1}(R
\partial_R)(c+S_0)+h^2R^{-2}P^{(0)}_1.$$
With $V_1 := \frac h{h+R}R\partial_R$ and $V_a := \frac h{h+R}Z_a$, $Z_a$ the six rotation fields of $\mathbb S^3$
($\Delta_{\mathbb S^3} = \sum Z_a^*Z_a$), $hRD_R = -i\rho_{\mathrm{cf}}^{-1}RV_1$ and $hZ_a =
\rho_{\mathrm{cf}}^{-1}RV_a$ up to the factor $R/\rho_K\to1$, so the first term is $\sum W^*_j\tilde M_{jk}W_k$ with $W =
(V_1,V_a)$ and $\tilde M = \mathrm{diag}((1+2R)\rho_{\mathrm{cf}}^{-2},\rho_{\mathrm{cf}}^{-2},\dots)\ge0$, modulo terms
in which a derivative falls on a coefficient or on the matrix of $\mathfrak e$ (in $W^*_j$); these are first-order
operators with an extra factor $\rho_{\mathrm{sf}}$, in $\Psi^{\mathbf m-\mathbf e}$, with symbols linear in
$(\xi_{c\hbar},\eta_{c\hbar})$. The other two terms are $h$ times first-order semiclassical operators, also linear in the
fibre variables at the level $\mathbf m-\mathbf e$ (the term $-2h^2R^{-1}R\partial_R(c+S_0) = -2\hat hR(1+\hat
h)iV_1(\dots)$ even vanishes at $R = 0$), plus zeroth-order terms in $\Psi^{\mathbf m-2\mathbf e}$. The real part of all
this is $\mathcal A'$. Near $\mathscr I^+$ the same with (1.11):
$h^2x_I^2[-\frac12(x_I\partial_{x_I})^2+x_I^2(\frac14(x_I\partial_{x_I})^2+\Delta)]$ is a sum of squares of
$hx_I\partial_{x_I}$, $hx_IZ_a$ with the factors $x_I^2(\frac12+\frac14x_I^2)$, $x_I^2$.

(d) *Near $F_I$.* With $D := x_I\partial_{x_I}$, $D^* = -D$ for $\mu_b$, and $(x_I^2D^2)^* = D^2x_I^2 = x_I^2(D+2)^2$, so
$\mathrm{Im}(-\frac12x_I^2D^2) = -ix_I^2(D+1)$, and $h^2$ times it has symbol $hx_I^2\xi$. For $X := x_I^2(hD)(c+S_0)$,
of principal symbol $x_I^2\,i\xi(c+S_0)$, the principal symbol of $\mathrm{Im}\,X$ is
$\frac1{2i}(x_I^2i\xi(c+S_0)+x_I^2i\xi(c+S_0^{*\mathfrak e})) = x_I^2(c+\mathrm{Re}\,S_0)\xi$, and
$h^2\,\mathrm{Im}(x_I^2D(c+S_0)) = h\,\mathrm{Im}\,X$. The term
$h^2x_I^4P^{(0)}(0,\omega,\frac12x_I\partial_{x_I},\partial_\omega)$ contributes $O(hx_I^3)$: its second-order part has
imaginary part $x_I^4$ times a first-order b-operator (the conjugation of $(x_I\partial_{x_I})^2$ by $x_I^4$, and of
$\Delta_{\mathbb S^3}$ by the matrix of $\mathfrak e$), and its first-order part is $x_I^4\mathrm{Diff}^1_b\subset
x_I^3\mathrm{Diff}^1_0$. So $\sigma(h^2\mathrm{Im}\,N^0(0)) = hx_I^2(1+c+\mathrm{Re}\,S_0)\xi+O(hx_I^3)$, and with (b),
$\sigma(hQ_0) = -hx_I^2(4+2\,\mathrm{Re}\,S_0)$; $1+c = \frac52$. *Near $F_K$.* The term
$-2h^2R^{-1}R\partial_R(R\partial_R+c+S_0)$ of $h^2N^0(0)$ is $R\cdot O(1)$ in $\Psi^{\mathbf m}$ (as
$h^2R^{-1}(R\partial_R)^2 = R(1+\hat h)^2V_1^2$ up to bounded factors), so its imaginary part has symbol $O(R\hat h)$,
which vanishes at $R = 0$ relative to $\varpi$. For $h^2R^{-2}P^{(0)}(0,\omega,-R\partial_R,\partial_\omega)$: at $t_* =
1$, $R = r$ and this is $h^2$ times the frozen operator $N(\hat P(0)) =
\rho^2P^{(0)}(0,\omega,\rho\partial_\rho,\partial_\omega)$, $\rho = r^{-1}$. For the Euclidean density $R^4\mu_b$,
$\rho^{-1}\mathrm{Im}\,N(\hat P(0))\in\rho\,\mathrm{Diff}^1_b = \mathrm{Diff}^1_{\mathrm{sc}}$ has scattering symbol at
$\partial X$ linear in $(\xi,\eta)$ (the zeroth-order part of $\rho\,\mathrm{Diff}^1_b$ vanishes at $\partial X$), say
$\xi a+b\cdot\eta$, and $p_{\mathrm{in}} = -2a$ by the definition of $p_{\mathrm{in}}$ (II.C Lemma 2.6, proof of (iii);
the symbol is that of $\hat P(0)$, the two differing by $\rho\,\mathrm{Diff}^2_b$ at $\partial X$, I.C section 4.1 (a)).
Over sf the canonical covector is $\zeta_R = \xi_{c\hbar}/h$, so $h^2\rho\,\xi_{\mathrm{sc}}a\mapsto
h^2R^{-1}a\xi_{c\hbar}/h = \hat ha\xi_{c\hbar}$, and likewise $\hat hb\cdot\eta_{c\hbar}$. For $\mu_b$ instead of
$R^4\mu_b$, $A^{*\mu_b} = R^4A^{*}R^{-4}$, so $\mathrm{Im}_{\mu_b}A = \mathrm{Im}\,A-\frac1{2i}R^4[A^*,R^{-4}]$; for $A =
h^2R^{-2}(RD_R)^2$, $[RD_R,R^{-4}] = 4iR^{-4}$, so $R^4[A^*,R^{-4}] = 8ih^2R^{-2}RD_R$ modulo $\Psi^{\mathbf m-2\mathbf
e}$, and the correction has symbol $-4h^2R^{-2}R\zeta_R = -4\hat h\xi_{c\hbar}$ (it is $-n\hat h\xi_{c\hbar}$ at
dimension $n$; [Hin26c]'s $-3\hat h\xi_{c\hbar}$ at $n = 3$). With $\sigma(hQ_0) = -\hat h(4+2\,\mathrm{Re}\,S_0)$ and
$\rho'/\hat h\to1$ at $R = 0$ this gives (3.8). For $\tilde{\mathcal P}_1(z)$: on the zero section the first-order
symbols vanish, leaving $\sigma(hQ_0)$. $\square$

*The Hamilton fields.* Let $p$ be the real principal symbol of $\mathrm{Re}\,P$ or $\mathrm{Re}\,\tilde P$ over sf: $p =
\mathrm{Re}\,G_{\iota,z}$, resp. $\mathrm{Re}(z^{-1}G_{\iota,z})$. $w_{\mathbf m-\mathbf e}$ is $\varpi$ times a smooth
positive function at finite frequencies near $F_I$, resp. $F_K$, so replacing $w_{\mathbf m-\mathbf e}$ by $\varpi$ in
Proposition 2.4 multiplies $\mathsf H^{\mathbf P}_z$ and $w^{-1}_{\mathbf m-\mathbf e}p_1$ by the same positive function
and changes none of the signs in its (i), (iii) and (v); we compute with $\mathsf H := \varpi^{-1}H_p$. Near $F_I$, in
the coordinates $(x_I,\omega;\xi,\eta)$ of the semiclassical 0-covectors, the canonical coordinates are $\zeta_x =
\xi/(hx_I)$, $\zeta_\omega = \eta/(hx_I)$, and for a function $g(x_I,\omega,\xi,\eta)$ (in local coordinates on $\mathbb
S^3$; $H^{\mathbb S^3}_g := \partial_\eta g\cdot\partial_\omega-\partial_\omega g\cdot\partial_\eta$)
$$h^{-1}H_g = \partial_\xi g\,(x_I\partial_{x_I}+\eta\cdot\partial_\eta)-(x_I\partial_{x_I}g+\eta\cdot\partial_\eta g)
\partial_\xi+x_IH^{\mathbb S^3}_g.\tag{3.9}$$
For $p = x_I^2g$, $H_p = x_I^2H_g+gH_{x_I^2}$ and $H_{x_I^2} = -2hx_I^2\partial_\xi$, so $\mathsf H =
h^{-1}H_g-2g\partial_\xi$; on $\{p = 0\}$ this is (1.15) up to $O(x_I^2)$. For $\mathrm{Re}\,z = 1$, $g =
\frac12\xi^2-\xi+|\eta|^2+\frac14x_I^2\xi^2$, and at $x_I = 0$
$$\mathsf H = (\xi-1)(x_I\partial_{x_I}+\eta\cdot\partial_\eta)+(2\xi-\xi^2-4|\eta|^2)\partial_\xi\quad(x_I = 0),
\qquad x_I^{-1}\mathsf Hx_I = \xi-1+\tfrac12x_I^2\xi.\tag{3.10}$$
Near $F_K$ the canonical coordinates are $\zeta_R = \xi_{c\hbar}(h+R)/(hR)$, $\zeta_\omega = \eta_{c\hbar}(h+R)/h$ (the
covectors of section 1.3), and $\mathsf H = \rho'^{-1}H_p$ is, in the coordinates $(\hat
h,R,\omega,\xi_{c\hbar},\eta_{c\hbar})$ of the phase-space family,
$$\mathsf H = \partial_\xi p\,V-(Vp)\,\partial_\xi+H^{\mathbb S^3}_p,\qquad V := R\partial_R-\hat h\partial_{\hat h}+
\rho'\xi\partial_\xi-(1-\rho')\eta\cdot\partial_\eta,\tag{3.11}$$
($\xi = \xi_{c\hbar}$, $\eta = \eta_{c\hbar}$), as $\partial_{\zeta_R} = R\rho'\partial_\xi$, $\partial_{\zeta_\omega} =
\rho'\partial_\eta$ and $R\partial_R|_{\zeta,h} =
R\partial_R|_{\xi,\eta,h}+\rho'\xi\partial_\xi-(1-\rho')\eta\cdot\partial_\eta$, with $R\partial_R|_h =
R\partial_R|_{\hat h}-\hat h\partial_{\hat h}$. It is a smooth b-vector field, tangent to $\{\hat h = 0\}$ (sf) and to
$\{R = 0\}$; this is (D6). At $\hat h = 0$, for $\mathrm{Re}\,z = 1$, $p = 2\xi+(1+2R)\xi^2+|\eta|^2$, and (3.11) is
(1.16) divided by $\hat h$:
$$\mathsf H = \big(2(1+2R)\xi+2\big)(R\partial_R-\eta\cdot\partial_\eta)+2(|\eta|^2-R\xi^2)\partial_\xi+H^{
\mathbb S^3}_{|\eta|^2},\qquad R^{-1}\mathsf HR = 2(1+2R)\xi+2.\tag{3.12}$$
For $\tilde P$ with $\mathrm{Re}\,z = 1$ or $z\in\mathcal Z^i$: $p = 2\xi+\mathrm{Re}(z^{-1})((1+2R)\xi^2+|\eta|^2)$ near
$F_K$ and $p = x_I^2(-\xi+\mathrm{Re}(z^{-1})(\frac12\xi^2+|\eta|^2+\frac14x_I^2\xi^2))$ near $F_I$.

*Symmetry.* $G_{\iota,-z}(R,\omega;-\xi,-\eta) = G_{\iota,z}(R,\omega;\xi,\eta)$, $\sigma(Q_1)$ and (3.7)-(3.8) are odd
under $(\xi,\eta,\mathrm{Re}\,z)\mapsto(-\xi,-\eta,-\mathrm{Re}\,z)$ (with $p_{\mathrm{in}}$ at $\xi = +2$ for $z = -1$,
I.A (1.5)), and the fibre reflection reverses Hamilton fields. So every statement below for $\mathcal Z^+_h$ and its
radial sets holds for $\mathcal Z^-_h$ with $\xi\mapsto-\xi$, $\eta\mapsto-\eta$ and $\varsigma\mapsto-\varsigma$; we
write out $\mathcal Z^+_h$.

### 3.3 The radial estimates

We apply Proposition 2.4 with $J = 1$ (one application of I.B Lemma 3.3), so only the thresholds at $\mathsf b$ itself
are needed; the error is $\|Gu\|_{\mathbf o-\frac14\mathbf e}$.

**Lemma 3.3.** For $z\in\mathcal Z^+_h$ with $y = \mathrm{Im}\,z\le\nu$, $\nu\in(0,1]$ small, the estimate (2.4) holds
at:
(R1) $\Lambda = R_{I^+,1,\mathrm{in}}$, for $\mathbf P = P$, $\varsigma = +1$, as a source ($\delta = 0$);
(R2) $\Lambda = R_{I^+,\mathrm{out}}$, for $\mathbf P = \tilde P$, $\varsigma = +1$, as a sink ($\delta = 1$, $K_E$ in a
punctured neighbourhood of $\Lambda$), and this for every $z\in\mathcal Z^+_h\cup\mathcal Z^i$;
(R3) $\Lambda = R_{\mathrm{cf},1,\mathrm{in}}$, for $\mathbf P = P$, $\varsigma = +1$, with $K_E\subset\{R\ge\delta_1\}$
($\varrho$-sink, $\phi$-source);
(R4) $\Lambda = R_{\mathrm{cf},\mathrm{out}}$, for $\mathbf P = \tilde P$, $\varsigma = +1$, with
$K_E\subset\{\phi\ge\delta_2\}$ ($\varrho$-source, $\phi$-sink), and this for every $z\in\mathcal Z^+_h\cup\mathcal Z^i$;
where $\mathrm{Im}\,z\ge\nu$, $K_E$ lies in the elliptic set of $\tilde P$.

*Proof.* In each case $\mathsf b$ is constant near $\Lambda$ ((1.17); $\mathsf b_{\mathrm{mid}}$ is constant), and
$\mathsf H$ vanishes on $\Lambda$, by (3.10), (3.12) and their analogues for $\tilde P$ (for $\tilde P$ at the zero
section $\partial_\xi p = -x_I^2$, resp. $2$, and the $\partial_\xi$-component is quadratic in $(\xi,\eta)$). We check
(i)-(v) of Proposition 2.4. Write $\mathrm{Re}\,S_0\ge\bar S-\epsilon$ for the inner product of II.C Lemma 2.5 (used at
(R2), (R4)), and use at (R3) the inner product in which $\vartheta_{\mathrm{in}}$ is computed.

(R1) $\varrho = x_I$, $\beta_\varrho = \xi-1+\frac12x_I^2\xi\to1$ at $\Lambda = \{x_I = 0,\xi = 2,\eta = 0\}$: a
$\varrho$-source. (ii): for $y\in[-h\gamma_+,h\nu_1]$, with $\nu_1 := 1+\max(0,-\gamma_I)$, put $-yQ_1$ into $\mathcal
P_1$: it is $h\cdot(y/h)Q_1\in\Psi^{\mathbf m-\mathbf e}$ with $|y/h|\le\max(\gamma_+,\nu_1)$, and $\lambda = 0$. For
$y\in[h\nu_1,\nu]$ put $-h\nu_1Q_1$ into $\mathcal P_1$ and take (A) with $\lambda := y-h\nu_1\in[0,1]$, $\mathcal A :=
Q_1$, whose principal symbol $x_I^2\xi\ge x_I^2$ near $\xi = 2$ is $\ge c_0w_{\mathbf m-\mathbf e_1}$ there. (iii): $g :=
\frac12\xi^2-\xi+|\eta|^2+\frac14x_I^2\xi^2$ ($|x_I^{-2}G_{\iota,z}|\ge|g|$), $\phi := (\xi-2)^2+|\eta|^2$. By (3.10) at
$x_I = 0$, $\mathsf H\phi = -2\xi(\xi-2)^2-8(\xi-2)|\eta|^2+2(\xi-1)|\eta|^2$; from $g =
\frac12\xi(\xi-2)+|\eta|^2+O(x_I^2)$, $(\xi-2)^2\le C(g^2+|\eta|^4+x_I^4)$ near $\Lambda$, so $\mathsf
H\phi\ge|\eta|^2-C(g^2+x_I)\ge\frac12\phi-C_1(\varrho+g^2)$ near $\Lambda$ ($x_I$-dependent terms are $O(x_I)$): a
$\phi$-source. (iv) $\tilde\kappa = 2\gamma_I+1$. (v) $p_1 = \sigma(\mathcal P_1(1))-\frac yh\cdot hx_I^2\xi$ in the
first case, $\sigma(\mathcal P_1(1))-\nu_1hx_I^2\xi$ in the second; by (3.7) at $\xi = 2$, $\varpi^{-1}p_1 = 1-2y/h$,
resp. $1-2\nu_1$, so
$$\mathcal T = 2(2\gamma_I+1)-2\big(1-2\tfrac yh\big) = 4\big(\gamma_I+\tfrac yh\big)\ge4(\gamma_I-\gamma_+),\qquad
\text{resp.}\quad\mathcal T = 4(\gamma_I+\nu_1)\ge4,$$
positive by (3.1). This is the computation of [Hin26c] (1.2.1), whose total
$-4x_I^{-4\gamma_I}(\gamma_I+h^{-1}\mathrm{Im}\,z)$ is $-\mathcal T$.

(R2) $\varrho = x_I$, $p = x_I^2g$ with $g := -\xi+\mathrm{Re}(z^{-1})(\frac12\xi^2+|\eta|^2+\frac14x_I^2\xi^2)$,
$\Lambda = \{x_I = 0,\xi = \eta = 0\}$; $\beta_\varrho = \partial_\xi g\to-1$: a $\varrho$-sink. (ii): by (3.6) and Lemma
3.2 (c), $\mathrm{Im}\,\tilde P = (\tilde{\mathcal P}_1-\lambda\mathcal A')-\lambda\sum W^*_j\tilde M_{jk}W_k$ with
$\lambda := \mathrm{Im}\,z/|z|^2$: case (B) when $\lambda\ge0$; when $\lambda<0$, $|\lambda|\le h\gamma_+$ and
$\lambda\mathcal A$ is part of $\mathcal P_1$, its symbol $(\lambda/h)\varpi\cdot\frac12\xi^2+\dots$ vanishing at
$\Lambda$. In both cases $\lambda\mathcal A'$ lies in $\Psi^{\mathbf m-\mathbf e}$ with symbol vanishing at $\Lambda$.
(iii): $|x_I^{-2}z^{-1}G_{\iota,z}|\ge|g|$; $\phi := \xi^2+|\eta|^2$. At $x_I = 0$, $\mathsf H = \partial_\xi
g(x_I\partial_{x_I}+\eta\partial_\eta)-(\eta\cdot\partial_\eta g+2g)\partial_\xi$ by (3.9), and $\mathsf H\phi =
-4\xi\,\mathrm{Re}(z^{-1})|\eta|^2-4\xi g+2\partial_\xi g|\eta|^2 = -2|\eta|^2+O(|\xi||\eta|^2)-4\xi g$. From $\xi =
\mathrm{Re}(z^{-1})(\frac12\xi^2+|\eta|^2)-g$, $|\xi|\le C(|\eta|^2+|g|)$ near $\Lambda$
($\mathrm{Re}(z^{-1})\in[-\frac12,1]$), so $\mathsf H\phi\le-|\eta|^2+Cg^2\le-\frac12\phi+C_1(g^2+\varrho)$: a
$\phi$-sink. (iv) $\tilde\kappa = 2\gamma_I+1$. (v) By Lemma 3.2 (d), $\varpi^{-1}\tilde p_1 = -(4+2\,\mathrm{Re}\,S_0)$
at $\Lambda$, so
$$\mathcal T = 2(2\gamma_I+1)(-1)+2(4+2\,\mathrm{Re}\,S_0) = 6-4\gamma_I+4\,\mathrm{Re}\,S_0\ge4\big(\tfrac32+\bar S-
\epsilon-\gamma_I\big),$$
positive by (3.1) for $\epsilon$ small. ([Hin26c] (1.2.2) at $n = 3$: $(4\gamma_I+2)-4(1+\mathrm{Re}\,S)-2<0$; at $n = 4$
the middle term is $-4(\frac32+\mathrm{Re}\,S)$.)

(R3) $\varrho = R$, $\Lambda = \{R = 0,\xi_{c\hbar} = -2,\eta_{c\hbar} = 0\}$ over sf, $\beta_\varrho =
2(1+2R)\xi+2\to-2$ by (3.12): a $\varrho$-sink. (ii): for $y\le0$, $-yQ_1$ is part of $\mathcal P_1$, with
$\varpi^{-1}(-y)\sigma(Q_1) = 2y\xi(1+\hat h)^2R/h$, which is bounded by $C\gamma_+R$ ($|y|\le h\gamma_+$) and vanishes
at $R = 0$; for $y\in[0,\nu]$, (A) with $\lambda := y$, $\mathcal A := Q_1$, $\sigma(Q_1) = -2\xi\ge3$ near $\Lambda$,
and $w_{\mathbf m-\mathbf e_1}$ bounded above and below there. (iii): $g := 2\xi+(1+2R)\xi^2+|\eta|^2$, $\phi :=
(\xi+2)^2+|\eta|^2$. At $R = 0$, by (3.12), $\mathsf H\phi = 2(\xi+2)\cdot2|\eta|^2-2(2\xi+2)|\eta|^2 = 4|\eta|^2$ (with
$H^{\mathbb S^3}_{|\eta|^2}|\eta|^2 = 0$), and $(\xi+1)^2 = 1-|\eta|^2+g$ there gives $|\xi+2|\le C(|\eta|^2+|g|)$; so
$\mathsf H\phi\ge4|\eta|^2-CR\ge c_1\phi-C_1(\varrho+g^2)$: a $\phi$-source. (iv) $w_{\mathbf k}$ at $F_K$:
$\rho_{\mathrm{tf}}^{-k_{\mathrm{tf}}}\rho_{\mathrm{sf}}^{-\mathsf b_{\mathbf k}} = R^{\mathsf b_{\mathbf
k}-k_{\mathrm{tf}}}h^{-\mathsf b_{\mathbf k}}$ times a smooth positive factor ($\rho_{\mathrm{tf}}/R$,
$\rho_{\mathrm{sf}}/\hat h$ smooth and positive near $\hat h = R = 0$), with $k_{\mathrm{tf}} = \gamma_{\mathrm{cf}}$,
$\mathsf b_{\mathbf k} = \mathsf b+\frac12$: $\tilde\kappa = \gamma_{\mathrm{cf}}-\mathsf b-\frac12$. (v) By (3.8) at
$\xi = -2$, $\eta = 0$: $\varpi^{-1}p_1 = 4+p_{\mathrm{in}}-(S_0+S_0^{*\mathfrak e})$, so, with $\gamma_{\mathrm{cf}} =
-(\alpha_++2)$,
$$\mathcal T = 2\big(\gamma_{\mathrm{cf}}-\mathsf b-\tfrac12\big)(-2)-2\big(4+p_{\mathrm{in}}-(S_0+S_0^{*\mathfrak e})
\big) = 4(\mathsf b+\alpha_+)+2-2\big(p_{\mathrm{in}}-(S_0+S_0^{*\mathfrak e})\big),$$
and $\lambda_{\max}(p_{\mathrm{in}}-(S_0+S_0^{*\mathfrak e}))\le\vartheta_{\mathrm{in}}$ on $\partial X$ (II.C Lemma
2.6), so $\mathcal T\ge4(\mathsf b+\alpha_+)+2-2\vartheta_{\mathrm{in}}>0$ by (1.17). (At $n = 3$ the source's total is
$-4\mathsf b+4\gamma_{\mathrm{cf}}-2+2(3+\vartheta_{\mathrm{in}})$ with $\gamma_{\mathrm{cf}} = -(\alpha_++\frac32)$, the
same condition (10.28); the dimension cancels.) In case (A) the commutant carries the factor
$\chi_0(\rho_{\mathrm{sf}}/\delta_0)$ of (D9).

(R4) $\varrho = R$, $\Lambda = \{R = 0,\xi_{c\hbar} = \eta_{c\hbar} = 0\}$, $p =
2\xi+\mathrm{Re}(z^{-1})((1+2R)\xi^2+|\eta|^2)$, $\beta_\varrho = \partial_\xi p\to2$: a $\varrho$-source. (ii) as in
(R2). (iii): $g := p$ ($|z^{-1}G_{\iota,z}|\ge|p|$), $\phi := \xi^2+|\eta|^2$; at $R = 0$, $\mathsf H\phi =
2\xi\cdot2\,\mathrm{Re}(z^{-1})|\eta|^2-2\partial_\xi p\,|\eta|^2 = -4|\eta|^2$, and $|\xi|\le C(|g|+|\eta|^2)$ near
$\Lambda$, so $\mathsf H\phi\le-2\phi+C(g^2+|\eta|^4)+CR\le-c_1\phi+C_1(\varrho+g^2)$: a $\phi$-sink. (iv) $\tilde\kappa
= \gamma_{\mathrm{cf}}-\mathsf b-\frac12$. (v) $\varpi^{-1}\tilde p_1 = -(4+2\,\mathrm{Re}\,S_0)$ at $\Lambda$, so
$$\mathcal T = 2\big(\gamma_{\mathrm{cf}}-\mathsf b-\tfrac12\big)\cdot2+2(4+2\,\mathrm{Re}\,S_0) = -4(\mathsf b+
\alpha_+)-2+4\,\mathrm{Re}\,S_0\ge-4(\mathsf b+\alpha_+)-2+4(\bar S-\epsilon)>0$$
by (1.17) for $\mathsf b_\pm$ and by the choice of $\mathsf b_{\mathrm{mid}}$, for $\epsilon$ small. The source prints
the total as $4\mathsf b+4\alpha_++2+4\,\mathrm{Re}\,S$ and requires it negative, which would give $\mathsf
b+\alpha_+<-\frac12-\mathrm{Re}\,S$; its own next sentence states $\mathsf b+\alpha_+<-\frac12+\mathrm{Re}\,S$, which is
what the computation gives (section 9, (F4)). Where $\mathrm{Im}\,z\ge\nu$: on $\{\phi\ge\delta_2\}$ near $\Lambda$,
$|\mathrm{Im}(z^{-1}G_{\iota,z})| = \frac{\mathrm{Im}\,z}{|z|^2}((1+2R)\xi^2+|\eta|^2)\ge\frac\nu2\delta_2-CR$, so $K_E$
is in the elliptic set; likewise in (R2). $\square$

### 3.4 Step 1: the symbolic estimate

**Lemma 3.4.** Fix $N\ge1-\inf\mathsf s'$. There are $h_0$ and $C$ such that for $h<h_0$, $z\in\mathcal Z^+_h\cup\mathcal
Z^i$ (with the orders of section 3.1) and $u\in C^\infty_c((\iota^+)^\circ)$,
$$\|u\|_{\mathbf o}\le C\big(\|Pu\|_{Y_{\mathbf o}}+\|u\|_{(-N;2\gamma_I,\gamma_{\mathrm{cf}},\gamma_{\mathrm{cf}};
\mathsf b-\frac14)}\big).\tag{3.13}$$

*Proof.* (a) *Fibre infinity and the elliptic set.* By Proposition 2.6, fibre infinity of $\mathcal P_\iota$ lies in
$\mathrm{Ell}(P)$, and so does every point over sf where $G_{\iota,z}\ne0$, uniformly for $z$ in compact sets: for
$z\in\mathcal Z^+_h$, $|G_{\iota,z}|\ge|\mathrm{Re}\,G_{\iota,z}| = |G_{\iota,1}|$ ($G$ is affine in $z$), so the
elliptic set contains the complement of $\Sigma_1 := \{G_{\iota,1} = 0\}$; for $\mathrm{Im}\,z\ge\nu$ and on $\mathcal
Z^i$, $|\mathrm{Im}(z^{-1}G_{\iota,z})| = \frac{\mathrm{Im}\,z}{|z|^2}\,\sigma(\mathcal A)$ shows that the characteristic
set over sf is the zero section $o_{\mathrm{sf}}$.

(b) *The dynamics.* For $\mathrm{Re}\,z = 1$ the Hamilton field of $\mathrm{Re}\,G_{\iota,z} = G_{\iota,1}$ is that of
section 1.3; on $\Sigma_1$, $q := \sigma(Q_1) = -2\xi_{c\hbar}$ ($= x_I^2\xi$ near $F_I$) satisfies $q\ge0$ with equality
exactly on $o_{\mathrm{sf}}$, since $G_{\iota,1} = 0$ gives $2\xi_{c\hbar} = -((1+2R)\xi_{c\hbar}^2+|\eta_{c\hbar}|^2)$
over sf. The future flow is $\mathsf H$ ($\varsigma = +1$), and every integral curve in $\Sigma_1$ has its $\alpha$-limit
in $R_{I^+,1,\mathrm{in}}\cup R_{\mathrm{cf},1,\mathrm{in}}\cup R_{\mathrm{cf},\mathrm{out}}$ and its $\omega$-limit in
$R_{\mathrm{cf},1,\mathrm{in}}\cup R_{\mathrm{cf},\mathrm{out}}\cup R_{I^+,\mathrm{out}}$, with the types of section 1.3.
The curves from $R_{\mathrm{cf},\mathrm{out}}$ to $R_{I^+,\mathrm{out}}$ are the fibres of $o_{\mathrm{sf}}$ over
$(\iota^+)^\circ$: $o_{\mathrm{sf}}\subset\Sigma_1$, and on it $\mathsf H = 2R\partial_R$ near $F_K$ and
$-x_I\partial_{x_I}$ near $F_I$ by (3.11)-(3.12) and (3.9), as the unstable manifold of the saddle
$R_{\mathrm{cf},\mathrm{out}}$ is one-dimensional over each $\omega$ (its linearisation is
$2R\partial_R-2\eta\cdot\partial_\eta$ plus terms quadratic in $(\xi,\eta)$). The curves from
$R_{\mathrm{cf},1,\mathrm{in}}$ to $R_{\mathrm{cf},\mathrm{out}}$ lie in $F_K$. For $\mathrm{Im}\,z\ge\nu$ and on
$\mathcal Z^i$, the field of $\mathrm{Re}(z^{-1}G_{\iota,z})$ on $o_{\mathrm{sf}}$ is the same, $2R\partial_R$, resp.
$-x_I\partial_{x_I}$, since the quadratic part does not contribute there.

(c) *Propagation.* Along curves in $\Sigma_1\setminus o_{\mathrm{sf}}$ use Proposition 2.5 for $\mathbf P = P$,
$\varsigma = +1$: for $y\le h\nu_1$ with $|\lambda|\le Ch$ (the term $-yQ_1$ in $\mathcal P_1$), for $y\in[h\nu_1,\nu]$
with (A), $\lambda = y$, $\mathcal A = Q_1$, as $q>0$ there; $\mathsf b_+$ is non-increasing along $\mathsf H$ on a
neighbourhood of these curves by (1.17) (II.C Definition 2.4 (1) pulled back). Along $o_{\mathrm{sf}}$ use Proposition
2.5 for $\mathbf P = \tilde P$, $\varsigma = +1$, with (B) for $\mathrm{Im}\,z\ge0$ and $|\lambda|\le Ch$ for
$\mathrm{Im}\,z<0$ (Lemma 3.3, proof of (R2)); $\mathsf b_+$ is non-increasing along $\mathsf H = 2R\partial_R$ on
$o_{\mathrm{sf}}$ (the same flow at $z = 1$), and $\mathsf b_{\mathrm{mid}}$ is constant.

(d) *Assembly for $y\le\nu$.* Cover the compact set $\Sigma_1$ over sf by finitely many open sets in which (2.4) or (2.5)
holds, in this order. (1) A neighbourhood $U_1$ of $R_{I^+,1,\mathrm{in}}$, by (R1), with no control term. (2) For each
point of $\Sigma_1\setminus o_{\mathrm{sf}}$ over $\mathrm{sf}^\circ\cup F_I^\circ$ whose backward curve enters $U_1$:
Proposition 2.5 from $U_1$. These cover a neighbourhood of the stable manifold of $R_{\mathrm{cf},1,\mathrm{in}}$ over
$R>0$, minus a neighbourhood of $\Lambda$, and of the incoming curves to $R_{I^+,\mathrm{out}}$ in $\Sigma_1\setminus
o_{\mathrm{sf}}$. (3) A neighbourhood $U_3$ of $R_{\mathrm{cf},1,\mathrm{in}}$ by (R3), whose control set
$K_E\subset\{R\ge\delta_1\}$ near $\Lambda$ lies in the set covered in (2), after shrinking $\delta_1$ (points of
$\Sigma_1$ near $\Lambda$ with $R>0$ lie on curves from $R_{I^+,1,\mathrm{in}}$, and points off $\Sigma_1$ are elliptic).
(4) The curves in $F_K$ from $R_{\mathrm{cf},1,\mathrm{in}}$ to $R_{\mathrm{cf},\mathrm{out}}$, by Proposition 2.5 from
$U_3$, with (D9) for (A). (5) A neighbourhood $U_5$ of $R_{\mathrm{cf},\mathrm{out}}$ by (R4), whose
$K_E\subset\{\phi\ge\delta_2\}$ near $\Lambda$ consists of points of $\Sigma_1\cap F_K$ on the curves of (4), of points
of $\Sigma_1$ over $R>0$ near them, which lie on curves from $R_{I^+,1,\mathrm{in}}$ or from
$R_{\mathrm{cf},1,\mathrm{in}}$ and so are covered by (2) or by (4) with Proposition 2.5 once more, and of elliptic
points. (6) $o_{\mathrm{sf}}$ over $(\iota^+)^\circ$, by Proposition 2.5 for $\tilde P$ from $U_5$. (7) A neighbourhood
of $R_{I^+,\mathrm{out}}$ by (R2), whose punctured control set lies in the sets of (2) and (6) and in the elliptic set.
The finitely many operators $B_*$ so obtained, together with elliptic ones, are jointly elliptic on $\mathcal P_\iota$; a
microlocal partition of unity gives $\|u\|_{\mathbf o}\le C(\sum_i\|B_{*,i}u\|_{\mathbf o}+\|u\|_{\mathbf o-K\mathbf
e})$. Each estimate has its $\|G\mathbf Pu\|_{\mathbf o-\mathbf m+\mathbf e}$ (or $\|GPu\|_{\mathbf o-\mathbf m}$ for
elliptic ones) bounded by $C\|Pu\|_{Y_{\mathbf o}}$ ($|z|^{-1}\le1$ for $\tilde P$; the operators $G$ at finite
frequencies see only the sf order $\mathsf b+1$ of $Y_{\mathbf o}$, those at fibre infinity only its differential order
$\mathsf s'-2$), its $\|E'u\|_{\mathbf o}$ by an earlier estimate, and its error $\|Gu\|_{\mathbf o-\frac14\mathbf e}$,
with $G$ microsupported at finite frequencies, by $C\|u\|_{(-N;\dots;\mathsf b-\frac14)}+C\|u\|_{\mathbf o-K\mathbf e}$.
The constants are uniform in $z$: Propositions 2.4-2.5 give them on neighbourhoods of each $z_*$ in the compact set
$\{1+iy:0\le y\le\nu\}$ (the $h$-dependent points $y\in[-h\gamma_+,0)$ are covered by the case $|\lambda|\le Ch$ near $y
= 0$).

(e) *Assembly for $\mathrm{Im}\,z\ge\nu$ and on $\mathcal Z^i$.* The characteristic set is $o_{\mathrm{sf}}$: (R4) at
$R_{\mathrm{cf},\mathrm{out}}$ with its $K_E$ in the elliptic set, Proposition 2.5 for $\tilde P$ with (B) along
$o_{\mathrm{sf}}$, (R2) at $R_{I^+,\mathrm{out}}$, and the elliptic estimate elsewhere, uniformly for $z$ in the compact
sets $\{1+iy:\nu\le y\le1\}$ and $\mathcal Z^i$.

Finally $\|u\|_{\mathbf o-K\mathbf e}\le\|u\|_{(-N;\dots;\mathsf b-\frac14)}$ for $K\ge\max(N+\sup\mathsf s',\frac14)$.
$\square$

### 3.5 Step 2: the transition face

The error term in (3.13) is not small as $h\to0$: its weight at tf is that of the left side. It is improved by the
transition face normal operator.

*The face.* In the coordinate $\hat R := R/h$, by (1.12),
$$P_{\iota,h,z} = N_{\mathrm{tf}}(z)-2h^2R^{-1}R\partial_R(R\partial_R+c+S_0),\qquad N_{\mathrm{tf}}(z) := -2iz
\hat R^{-1}(\hat R\partial_{\hat R}+c+S_0)+\hat R^{-2}P^{(0)}(0,\omega,-\hat R\partial_{\hat R},\partial_\omega),
\tag{3.14}$$
since $-2R^{-1}(iz+hR\partial_R)h(R\partial_R+c+S_0) = -2izhR^{-1}(\dots)-2h^2R^{-1}R\partial_R(\dots)$ and $hR^{-1} =
\hat R^{-1}$, $R\partial_R = \hat R\partial_{\hat R}$, $h^2R^{-2} = \hat R^{-2}$. With $\hat\rho := \hat R^{-1}$,
$N_{\mathrm{tf}}(z) = 2iz\hat\rho(\hat\rho\partial_{\hat\rho}-\frac32-S_0)+\hat\rho^2N(P^{(0)})$ is I.C (4.1) at
$\hat\sigma = z$ on $\mathrm{tf} = [0,\infty]_{\hat R}\times\mathbb S^3$ (I.C section 4.1, with $\mathrm{ztf}$ at $\hat R
= 0$ and $\mathrm{sctf}$ at $\hat R = \infty$). The remainder lies in
$\rho_{\mathrm{tf}}\rho_{\mathrm{cf}}^{-1}\mathrm{Diff}^2_{\mathcal V_\hbar}$: $h^2R^{-1}(R\partial_R)^2 =
R^{-1}(h+R)^2V_1^2$ up to lower terms of the same class, and $R^{-1}(h+R)^2 = \rho_{\mathrm{tf}}\rho_{\mathrm{cf}}^{-1}$
near $K^+$ (up to smooth positive factors).

*Orders.* Let $2\delta_\flat\in(0,\frac14]$ be so small that $\mathsf b_\flat := \mathsf b-2\delta_\flat$ still satisfies
(1.17) ($\mathsf b_\pm$ is constant near the radial sets with strict inequalities, and a constant shift keeps the
monotonicity); for $\mathsf b_{\mathrm{mid}}$ any $\delta_\flat$ will do. Put $\mathbf o_\flat :=
(-N;2\gamma_I,\gamma_{\mathrm{cf}},\gamma_{\mathrm{cf}};\mathsf b_\flat)$; then $\|u\|_{(-N;\dots;\mathsf
b-\frac14)}\le\|u\|_{\mathbf o_\flat}$.

**Lemma 3.5 (the tf-normal operator at $n = 4$).** Assume $P_0$ tf-admissible with weight $\alpha_++2$ (II.C Definition
2.3; $\alpha_++2 = -\gamma_{\mathrm{cf}}$ lies in the gap $(\beta_-,\beta_+)$), and let $q := -\alpha_+$. For
$\hat\sigma\in\{\pm1+iy:0\le y\le1\}$ let $\mathsf r := \mathsf b_{\flat}|_{F_K}$ (for $\mathsf b = \mathsf b_\pm$), and
for $\hat\sigma\in\mathcal Z^i$ let $\mathsf r := \mathsf b_{\mathrm{mid}}-2\delta_\flat$. Then
$N_{\mathrm{tf}}(\hat\sigma)$ is invertible between the spaces of I.C Theorem 4.3 with these orders, any $s$, and
$$\|w\|_{H^{s,(\mathsf r+\alpha_+,q)}_{\mathrm{sc},b}}\le C\|N_{\mathrm{tf}}(\hat\sigma)w\|_{H^{s-2,(\mathsf r+
\alpha_++1,q-2)}_{\mathrm{sc},b}},\qquad\|w\|_{H^{-s+2,(-\mathsf r-\alpha_+-1,-q+2)}_{\mathrm{sc},b}}\le C\|N_{
\mathrm{tf}}(\hat\sigma)^{*}w\|_{H^{-s,(-\mathsf r-\alpha_+,-q)}_{\mathrm{sc},b}},\tag{3.15}$$
uniformly in $\hat\sigma$ in each family.

*Proof.* *The order.* $F_K$, the face of $\mathcal P_\iota$ over $\mathrm{sf}\cap\mathrm{tf}$, is the face of the
scattering phase space of tf over sctf (II.A section 6.2, the paragraph on the tf-normal operator: the
$0\hbar,c\hbar$-fields become the b,sc-fields of tf), with the same fibre variables, and at $R = 0$ the symbol (1.13) is
$2\hat\sigma\xi+\xi^2+|\eta|^2$, I.B Lemma 4.1's boundary symbol of I.A at $\sigma = \hat\sigma$. So for $\hat\sigma =
\pm1+iy$ the real part of the symbol is that at $\sigma_0 = \pm1$, and $\mathsf r$ is a decay order admissible at
$\sigma_0 = \pm1$ with weight $\alpha_+$ in the sense of I.A section 1.4: non-increasing along the boundary flow (the
restriction to $F_K$ of the flow over sf) and constant near $R_{\mathrm{in}}$, $R_{\mathrm{out}}$ with the thresholds
$\mathsf r+\alpha_+>\frac12(-1+\vartheta_{\mathrm{in}})$, $\mathsf r+\alpha_+<-\frac12+\bar S$, which are (1.17) at
$F_K$. *Fredholm estimates.* The proof of I.C Theorem 4.3 (1) with $\hat\sigma$ in place of $e^{i\theta}$: near sctf it
uses I.A Theorem 7.2 (1), which applies with $I = \{\pm1\}$, $\nu = 1$ and the order pair $(s,\mathsf r)$, admissible for
$\sigma_0 = \pm1$, to $\sigma = \pm1+iy$; near ztf Lemmas 2.5-2.6 of I.C, which hold for $\hat\sigma$ in compact sets; in
the interior ellipticity. So (4.3)-(4.4) of I.C hold uniformly for $y\in[0,1]$. For $\hat\sigma\in\mathcal Z^i$,
$\mathrm{Im}\,\hat\sigma = 1$ and I.A Theorem 7.2 (2) applies with the constant order. *Kernel and index.* By I.C (4.2),
$N_{\mathrm{tf}}(\hat\sigma) = |\hat\sigma|^2S_{|\hat\sigma|}^{-1}N_{\mathrm{tf}}(e^{i\theta})S_{|\hat\sigma|}$, $\theta
= \arg\hat\sigma$. An element of the kernel lies in $\mathcal A^{\frac32+\bar S-\epsilon,-\beta}(\mathrm{tf})$ for all
$\epsilon>0$, $\beta\in(\beta_-,\beta_+)$ (I.A Theorem 7.2 (5) near sctf at $\sigma = \hat\sigma$, I.C Lemma 2.7 near
ztf, as in I.C Theorem 4.3 (5)); $S_{|\hat\sigma|}$ preserves that space, which lies in $\mathcal
X_{\mathrm{tf},\theta}$, so the kernel is trivial by I.C Corollary 5.2 (a). The index is independent of $y\in[0,1]$
(local constancy, as in I.C Theorem 4.3 (3), with the uniform estimates), and at $y = 0$, $\hat\sigma = \pm1 =
e^{i\theta}$ with $\theta\in\{0,\pi\}$, where it is 0 by I.C Corollary 5.2 (a), the index not depending on the admissible
orders. So $N_{\mathrm{tf}}(\hat\sigma)$ is invertible, and (3.15) holds uniformly by the contradiction argument of I.C
Corollary 5.2 (b). For $\mathcal Z^i$, $\theta\in[\frac\pi4,\frac{3\pi}4] = \Sigma_m$ and $|\hat\sigma|\in[1,\sqrt2]$;
$S_{|\hat\sigma|}$ is an isomorphism of the spaces with constant orders, with norms bounded uniformly ($\hat r^{q-2}$ and
$\hat\rho^{\mathsf r+\alpha_+}$ are homogeneous, and dilations preserve the b- and sc-structures), so (3.15) is I.C
Corollary 5.2 (b) on $\Sigma_m$ with $\mathsf r_{\mathrm{mid}} := \mathsf r$. $\square$

**Lemma 3.6.** There are $h_0$, $C$ such that for $h<h_0$, $z$ as in Lemma 3.4, and $u\in C^\infty_c((\iota^+)^\circ)$,
$$\|u\|_{\mathbf o_\flat}\le C\|Pu\|_{Y_{\mathbf o}}+Ch^{\delta_\flat}\|u\|_{\mathbf o}.\tag{3.16}$$

*Proof.* Let $\chi\in C^\infty(\mathbb R)$, $\chi = 1$ on $(-\infty,\frac12]$, $\chi = 0$ on $[1,\infty)$, and ([Hin26c]
Step 2)
$$\chi_{\mathrm{tf}} := \chi(\rho_{\mathrm{tf}})\,\chi(\rho_{\mathrm{tf}}/\rho_{\mathrm{sf}}).$$
On its support $\rho_{\mathrm{tf}}<1$ and $\rho_{\mathrm{tf}}<\rho_{\mathrm{sf}}$; near cf, for $h<\frac12$,
$\chi_{\mathrm{tf}} = 1$. It is a function on $\iota^+$ depending on $h$, with derivatives along $C^\infty_b\mathcal
V_b(\iota^+)$ bounded uniformly ($\rho_K\partial_{\rho_K}\log(\rho_{\mathrm{tf}}/\rho_{\mathrm{sf}}) = 2\vartheta$, Lemma
2.1 (b)). Note $\rho_{\mathrm{tf}}\rho_{\mathrm{sf}} = h$.

*Away from tf.* On $\mathrm{supp}(1-\chi_{\mathrm{tf}})$, either $\rho_{\mathrm{tf}}\ge\frac12$, so $\rho_{\mathrm{sf}} =
h/\rho_{\mathrm{tf}}\le2h$, or $\rho_{\mathrm{tf}}\ge\frac12\rho_{\mathrm{sf}}$, so $\rho_{\mathrm{sf}}^2\le2h$. In both
cases $\rho_{\mathrm{sf}}^{2\delta_\flat}\le(2h)^{\delta_\flat}$, and $m_h :=
h^{-\delta_\flat}\rho_{\mathrm{sf}}^{2\delta_\flat}(1-\chi_{\mathrm{tf}})\in S^0$ with seminorms bounded uniformly in $h$
(its derivatives are of the same form, or carry derivatives of $\chi_{\mathrm{tf}}$, supported where the same bounds
hold). As $\|(1-\chi_{\mathrm{tf}})u\|_{\mathbf o_\flat} =
\|\rho_{\mathrm{sf}}^{2\delta_\flat}(1-\chi_{\mathrm{tf}})u\|_{(-N;\dots;\mathsf b)}$, Lemma 2.2 (a) gives
$\|(1-\chi_{\mathrm{tf}})u\|_{\mathbf o_\flat}\le Ch^{\delta_\flat}\|u\|_{\mathbf o}$.

*Near tf.* By II.A section 6.2 ([Hin26c] (3.60)), for functions supported in $\mathrm{supp}\,\chi_{\mathrm{tf}}$,
$\|w\|_{H^{s,(2\alpha_I,\alpha_{\mathrm{cf}},l,\mathsf b)}_{0\hbar,c\hbar,h}}\sim
h^{-l}\|w\|_{H^{s,(\alpha_{\mathrm{cf}},\mathsf b-l)}_{b,sc}(\mathrm{tf})}$ uniformly (the weight at 0f is immaterial
there), where on the right $\mathsf b$ is read on the b,sc phase space of tf. Our sf orders depend on $R$; on
$\mathrm{supp}\,\chi_{\mathrm{tf}}$, $\rho_{\mathrm{tf}}^2\le\rho_{\mathrm{tf}}\rho_{\mathrm{sf}} = h$, so $R\le
Ch^{1/2}$ and $\mathsf b_\flat$ differs from its restriction to $F_K$ by $O(h^{1/2})$ with all derivatives;
$\rho_{\mathrm{sf}}^{\pm O(h^{1/2})}$ is then a symbol of order 0 with bounded seminorms ($h^{1/2}\log h^{-1}\to0$), so
the norms with $\mathsf b_\flat$ and with $\mathsf r := \mathsf b_\flat|_{F_K}$ are equivalent there, uniformly. The
b-density on tf is $\hat R^{-4}$ times the Euclidean one, so $\|w\|_{L^2(|\frac{d\hat R}{\hat R}d\slashed g|)} = \|\hat
R^{-2}w\|_{L^2(\hat R^4|\frac{d\hat R}{\hat R}d\slashed g|)}$, and $\hat R = \rho_{\mathrm{cf}}/\rho_{\mathrm{sf}}$ on tf
up to smooth positive factors; so the b,sc weights $(\alpha_{\mathrm{cf}},\mathsf r-l)$ for the b-density are
$(\alpha_{\mathrm{cf}}+2,\mathsf r-l-2)$ for the Euclidean one (at $n = 3$, the source's shift $\frac32$). With $l =
\gamma_{\mathrm{cf}}$, $\alpha_{\mathrm{cf}} = \gamma_{\mathrm{cf}}$: the Euclidean weights (at cf, at sf) are
$(\gamma_{\mathrm{cf}}+2,\mathsf r-\gamma_{\mathrm{cf}}-2) = (-\alpha_+,\mathsf r+\alpha_+) = (q,\mathsf r+\alpha_+)$,
which in the notation of I.C (sctf first) is the space $H^{s,(\mathsf r+\alpha_+,q)}_{\mathrm{sc},b}$. Lemma 3.5 then
gives, with all differential orders $-N$, resp. $-N-2$,
$$\|\chi_{\mathrm{tf}}u\|_{\mathbf o_\flat}\le Ch^{-\gamma_{\mathrm{cf}}}\|\chi_{\mathrm{tf}}u\|_{H^{-N,(\mathsf r+
\alpha_+,q)}_{\mathrm{sc},b}}\le Ch^{-\gamma_{\mathrm{cf}}}\|N_{\mathrm{tf}}(\hat\sigma)\chi_{\mathrm{tf}}u\|_{H^{-N-2,(
\mathsf r+\alpha_++1,q-2)}_{\mathrm{sc},b}}\le C\|N_{\mathrm{tf}}(\hat\sigma)\chi_{\mathrm{tf}}u\|_{Y_\flat},$$
$Y_\flat := H^{(-N-2;-N,\gamma_{\mathrm{cf}}-2,\gamma_{\mathrm{cf}};\mathsf b_\flat+1)}$, converting back: the Euclidean
weights (at cf, at sf) $(q-2,\mathsf r+\alpha_++1)$ are the b-weights $(\gamma_{\mathrm{cf}}-2,\mathsf
r-\gamma_{\mathrm{cf}}+1)$, which are $(\alpha_{\mathrm{cf}},\mathsf b'-l)$ for $\alpha_{\mathrm{cf}} =
\gamma_{\mathrm{cf}}-2$, $l = \gamma_{\mathrm{cf}}$, $\mathsf b' = \mathsf r+1$. ([Hin26c] prints the orders of this last
space as $(-N,\gamma_{\mathrm{cf}},\gamma_{\mathrm{cf}}-2,\mathsf b_\flat+1)$, interchanging cf and tf.) Here $\hat\sigma
:= z$ if $\mathrm{Im}\,z\ge0$ and $\hat\sigma := \mathrm{Re}\,z = \pm1$ if $\mathrm{Im}\,z<0$.

*From $N_{\mathrm{tf}}$ to $P$.* $N_{\mathrm{tf}}(\hat\sigma)\chi_{\mathrm{tf}}u =
\chi_{\mathrm{tf}}Pu+[P,\chi_{\mathrm{tf}}]u-(P-N_{\mathrm{tf}}(z))\chi_{\mathrm{tf}}u+(N_{\mathrm{tf}}(\hat
\sigma)-N_{\mathrm{tf}}(z))\chi_{\mathrm{tf}}u$. (1) $\|\chi_{\mathrm{tf}}Pu\|_{Y_\flat}\le C\|Pu\|_{Y_{\mathbf o}}$, as
$Y_\flat$ has lower orders. (2) By (3.14),
$P-N_{\mathrm{tf}}(z)\in\rho_{\mathrm{tf}}\rho_{\mathrm{cf}}^{-1}\mathrm{Diff}^2_{\mathcal V_\hbar}$, so its contribution
is bounded by $C\|\chi_{\mathrm{tf}}u\|_{(-N;\cdot,\gamma_{\mathrm{cf}}-1,\gamma_{\mathrm{cf}}-1;\mathsf b_\flat+1)}$. On
$\mathrm{supp}\,\chi_{\mathrm{tf}}$, $\rho_{\mathrm{tf}}<\rho_{\mathrm{sf}}$, so
$\rho_{\mathrm{tf}}\rho_{\mathrm{sf}}^{2\delta_\flat-1} =
\rho_{\mathrm{tf}}^{2\delta_\flat}\rho_{\mathrm{tf}}^{1-2\delta_\flat}\rho_{\mathrm{sf}}^{2\delta_\flat-1}\le(
\rho_{\mathrm{tf}}\rho_{\mathrm{sf}})^{2\delta_\flat} = h^{2\delta_\flat}$, and $\rho_{\mathrm{cf}}\le1$; the weight of
this norm divided by that of $\mathbf o$ is $\rho_{\mathrm{cf}}\rho_{\mathrm{tf}}\rho_{\mathrm{sf}}^{2\delta_\flat-1}\le
h^{2\delta_\flat}$, and as for $m_h$ above it is bounded by $Ch^{2\delta_\flat}\|u\|_{\mathbf o}$. (3)
$\chi_{\mathrm{tf}} = 1$ near cf, and the derivatives of $\chi_{\mathrm{tf}}$ along $\mathcal V_\hbar =
\rho_{\mathrm{sf}}C^\infty_b\mathcal V_b$ are $\rho_{\mathrm{sf}}$ times bounded functions supported where
$\rho_{\mathrm{tf}}\in[\frac12,1]$ (there $\rho_{\mathrm{sf}}\le2h$) or
$\rho_{\mathrm{tf}}/\rho_{\mathrm{sf}}\in[\frac12,1]$ (there $\rho_{\mathrm{sf}}^2\le2h$). So
$[P,\chi_{\mathrm{tf}}]\in\rho_{\mathrm{sf}}\mathrm{Diff}^1_{\mathcal V_\hbar}$ with coefficients supported there and
vanishing near cf, and its contribution is at most $C\|\rho_{\mathrm{sf}}^{2\delta_\flat}\tilde\chi
u\|_{(-N;\dots;\mathsf b)}\le C(2h)^{\delta_\flat}\|u\|_{\mathbf o}$, $\tilde\chi$ a cut-off to that support. (4) If
$\mathrm{Im}\,z<0$, $N_{\mathrm{tf}}(\hat\sigma)-N_{\mathrm{tf}}(z) = -i\,\mathrm{Im}\,z\,\partial_zN_{\mathrm{tf}}$ with
$|\mathrm{Im}\,z|\le\gamma_+h = \gamma_+\rho_{\mathrm{tf}}\rho_{\mathrm{sf}}$ and $\partial_zN_{\mathrm{tf}} = -2i\hat
R^{-1}(\hat R\partial_{\hat R}+c+S_0) = h\,\partial_\sigma N^0\in\Psi^{\mathbf m-\mathbf e_1}$ near tf with weight
$\rho_{\mathrm{cf}}^{-1}$; its contribution is bounded by
$C\|\chi_{\mathrm{tf}}u\|_{(-N+1;\cdot,\gamma_{\mathrm{cf}}-1,\gamma_{\mathrm{cf}}-1;\mathsf b_\flat)}$, and
$\rho_{\mathrm{cf}}\rho_{\mathrm{tf}}\rho_{\mathrm{sf}}^{2\delta_\flat}\le h^{2\delta_\flat}$
($\rho_{\mathrm{tf}}\le\rho_{\mathrm{tf}}^{2\delta_\flat}$). Summing, $\|u\|_{\mathbf
o_\flat}\le\|\chi_{\mathrm{tf}}u\|_{\mathbf o_\flat}+\|(1-\chi_{\mathrm{tf}})u\|_{\mathbf o_\flat}$ gives (3.16).
$\square$

### 3.6 Proof of Proposition 3.1

By Lemmas 3.4 and 3.6, $\|u\|_{\mathbf o}\le C\|Pu\|_{Y_{\mathbf o}}+Ch^{\delta_\flat}\|u\|_{\mathbf o}$ for $u\in
C^\infty_c((\iota^+)^\circ)$, and for $h$ small the last term is absorbed: (3.4) for such $u$, and by Lemma 2.2 (g) for
every $u\in H^{\mathbf o}$ with $Pu\in Y_{\mathbf o}$ (the norm of $Y_{\mathbf o}$ is that of $H^{\mathbf o-\mathbf
m+\mathbf e}$ at finite frequencies and of $H^{\mathbf o-\mathbf m}$ at fibre infinity, and Lemma 2.2 (g) at the two
orders, with a microlocal partition of unity, gives the density). For $\mathcal Z^-_h$ use the symmetry of section 3.2.

*The adjoint.* The same steps for $P^* = P^*_{\iota,h,z}$ on the dual spaces: with $\mathbf o^* := -\mathbf o+\mathbf
m-\mathbf e+\mathbf e_1$, so that $H^{\mathbf o^*} = Y_{\mathbf o}^*$ and $H^{-\mathbf o}$ is the dual of $H^{\mathbf o}$
((S3), (S11)),
$$\|v\|_{\mathbf o^*}\le C\|P^*v\|_{-\mathbf o}.\tag{3.17}$$
Every radial estimate of Lemma 3.3 holds for $\mathbf P^*$ ($\epsilon_\flat = -1$) with $\varsigma\mapsto-\varsigma$ at
the dual order: the dual of the order $\mathbf k$ of (D3) is $-\mathbf k$, so $\tilde\kappa\mapsto-\tilde\kappa$, while
$\beta_\varrho\mapsto-\beta_\varrho$ and $\varsigma\epsilon_\flat$ is unchanged; so $\mathcal T$ is the same, and sources
and sinks (in $\varrho$ and in $\phi$) are interchanged. The absorbing terms keep their sign ($\epsilon_\flat\varsigma$
unchanged); the dual sf order $-\mathsf b-1$ is non-increasing along $-\mathsf H$. So the assembly runs backwards: from
$R_{I^+,\mathrm{out}}$ (now a source), along $o_{\mathrm{sf}}$ and $\Sigma_1\setminus o_{\mathrm{sf}}$ backwards, to
$R_{\mathrm{cf},\mathrm{out}}$, $R_{\mathrm{cf},1,\mathrm{in}}$ and $R_{I^+,1,\mathrm{in}}$; at the saddles the roles of
$\varrho$ and $\phi$ interchange, and the control sets are the unstable manifolds, reached from the earlier steps. In
Step 2 the second estimate of (3.15) replaces the first, with $[P^*,\chi_{\mathrm{tf}}]$ and $P^*-N_{\mathrm{tf}}(z)^*$
bounded as before; $Y_\flat$ and $\mathbf o_\flat$ are replaced by their duals shifted in the same way.

*Invertibility.* For fixed small $h$, (3.4) shows that $P:H^{\mathbf o}\to Y_{\mathbf o}$ is injective with closed range.
If $v\in Y^*_{\mathbf o} = H^{\mathbf o^*}$ annihilates the range, then $P^*v = 0$ in $H^{-\mathbf o}$ (the pairing
$\langle Pu,v\rangle = \langle u,P^*v\rangle$ holds for $u\in C^\infty_c((\iota^+)^\circ)$, dense in $H^{\mathbf o}$), so
$v = 0$ by (3.17) and Lemma 2.2 (g) for $P^*$. So $P$ is surjective. $\square$

## 4. High frequencies with b-regularity ([Hin26c] Proposition 10.6 (2), $k\ge1$)

### 4.1 The b-vector fields and the commuted operator

Let $W_1 := R\partial_R$ ($= -\frac12x_I\partial_{x_I}$ near $\mathscr I^+$) and $W_{1+a} := Z_a$, $a = 1,\dots,6$, the
rotation fields of $\mathbb S^3$. They span $\mathcal V_b(\iota^+)$ over $C^\infty(\iota^+)$ at both ends and in between
($R\partial_R$ and $\partial_\omega$ near $\iota^+\cap K^+$, $x_I\partial_{x_I}$ and $\partial_\omega$ near
$\iota^+\cap\mathscr I^+$, and the $Z_a$ span $T\mathbb S^3$ at every point). For a word $\alpha =
(\alpha_1,\dots,\alpha_k)\in\{1,\dots,7\}^k$ put $W^\alpha := W_{\alpha_1}\cdots W_{\alpha_k}$, $|\alpha| := k$,
$j_\alpha := \#\{i:\alpha_i = 1\}$, and $W^\alpha_\sharp$ the same product with each $W_1$ replaced by $W_1+2$. For $v$
on $\iota^+$ and orders $\mathbf o$ put
$$\|v\|_{\mathbf o;k} := \sum_{|\alpha|\le k}\|W^\alpha v\|_{\mathbf o},\qquad\|v\|_{\mathbf o;k,+} :=
\sum_{j = 0}^kh^{-j}\|v\|_{\mathbf o;k-j}.\tag{4.1}$$
$\|\cdot\|_{\mathbf o;k}$ is the norm of $H^{(\mathsf s;k),(a,c,l,\mathsf b)}_{(0\hbar,c\hbar,h);b}$ (k orders of
b-regularity, (S3) with $\mathcal W = C^\infty_b\mathcal V_b(\iota^+)$), up to equivalence uniform in $h$. The norm
$\|\cdot\|_{\mathbf o;k,+}$, with the constant factors $h^{-j}$, is the one Proposition 6.1 (the source's 10.12) needs:
under the Mellin transform $\tau\partial_\tau$ becomes $i\sigma$, $|\sigma| = |z|h^{-1}$, which is the factor
$|\sigma|^j$ of [Hin26c] (10.47) (section 9, (F5)).

With $L := 2hR^{-1}(iz+hR\partial_R)$ and the decomposition $P^{(0)}(0,\omega,\rho\partial_\rho,\partial_\omega) = ((\rho
D_\rho)^2+\Delta_{\mathbb S^3})\mathrm{Id}+P^{(0)}_1$ of section 3.2, $P^{(0)}_1 =
A(\omega)\rho\partial_\rho+\sum_bB_b(\omega)Z_b+C(\omega)$ ($\partial_\omega$ written in the spanning family $Z_b$, with
smooth coefficients):

**Lemma 4.1.** (a) $[W_1,P_{\iota,h,z}] = -2P_{\iota,h,z}-L(W_1+c+S_0)$ and $[W_1,L] = -L$. (b) $[Z_a,P_{\iota,h,z}] =
-L(Z_aS_0)+h^2R^{-2}\big(\sum_bc_{ab}W_b+c_{a0}\big)$ with $c_{ab},c_{a0}\in C^\infty(\mathbb S^3;\mathrm{End}\,\mathbb
C^N)$, and $[Z_a,L] = 0$. (c) For every word $\alpha$ with $|\alpha| = k\ge1$ and $u\in C^\infty_c((\iota^+)^\circ)$,
$$(P-j_\alpha L)W^\alpha u = W^\alpha_\sharp Pu+\sum_{|\beta| = k}\mathcal C_{\alpha\beta}W^\beta u+\sum_{|\beta|\le k-1}
\mathcal R_{\alpha\beta}W^\beta u,\qquad P := P_{\iota,h,z},\tag{4.2}$$
where each $\mathcal C_{\alpha\beta}$ is multiplication by an element of $h^2R^{-1}C^\infty(\mathbb
S^3)+h^2R^{-2}C^\infty(\mathbb S^3)$ and each $\mathcal R_{\alpha\beta}$ by an element of $hR^{-1}C^\infty(\mathbb
S^3)+h^2R^{-1}C^\infty(\mathbb S^3)+h^2R^{-2}C^\infty(\mathbb S^3)$ (endomorphism-valued, polynomial in $z$). In
particular $\mathcal C_{\alpha\beta}\in\Psi^{\mathbf m-2\mathbf e}$ and $\mathcal R_{\alpha\beta}\in\Psi^{\mathbf
m-\mathbf e}$.

*Proof.* (a) $P = -2R^{-1}B+h^2R^{-2}P^{(0)}(0,\omega,-R\partial_R,\partial_\omega)$ with $B :=
(iz+hR\partial_R)(hR\partial_R+h(c+S_0))$ by (1.12); $B$ and $P^{(0)}(\dots)$ commute with $R\partial_R$, and
$[R\partial_R,R^{-m}] = -mR^{-m}$. So $[W_1,P] = 2R^{-1}B-2h^2R^{-2}P^{(0)} = -2P-2R^{-1}B$, and $-2R^{-1}B =
-L(R\partial_R+c+S_0)$. (b) $Z_a$ commutes with $R$, $R\partial_R$ and $\Delta_{\mathbb S^3}$; $[Z_a,-2R^{-1}B] =
-2R^{-1}(iz+hR\partial_R)h(Z_aS_0) = -L(Z_aS_0)$, and $[Z_a,P^{(0)}_1] =
(Z_aA)\rho\partial_\rho+\sum_b((Z_aB_b)Z_b+B_b[Z_a,Z_b])+Z_aC$, a first-order operator in the $W$'s with coefficients in
$C^\infty(\mathbb S^3)$, as $[Z_a,Z_b]$ is a combination of the $Z$'s. (c) Induction on $k$. Write $\alpha =
(\alpha_1,\alpha')$ and $v := W^{\alpha'}u$. By (a), $P(W_1v) = (W_1+2)Pv+LW_1v+L(c+S_0)v$; by (b), $P(Z_av) =
Z_aPv+L(Z_aS_0)v-h^2R^{-2}(\sum_bc_{ab}W_bv+c_{a0}v)$. Insert (4.2) for $Pv$ ($v = u$ for $k = 1$). The term
$j_{\alpha'}LW^{\alpha'}u$ becomes $(W_1+2)j_{\alpha'}LW^{\alpha'}u = j_{\alpha'}L(W_1+1)W^{\alpha'}u$ (by $[W_1,L] =
-L$), resp. $j_{\alpha'}LZ_aW^{\alpha'}u$; together with $LW_1v$ this gives $j_\alpha LW^\alpha u$, plus
$j_{\alpha'}LW^{\alpha'}u$. Write $L = 2izhR^{-1}+2h^2R^{-1}W_1$: acting on a word of length $k-1$, the first part is of
$\mathcal R$-type and the second of $\mathcal C$-type (a word of length $k$ with the coefficient $h^2R^{-1}$); likewise
$L(c+S_0)v$ and $L(Z_aS_0)v$, after commuting the coefficient past $W_1$ (which produces $\mathcal R$-type terms). The
terms $h^2R^{-2}c_{ab}W_bv$ are of $\mathcal C$-type and $h^2R^{-2}c_{a0}v$ of $\mathcal R$-type. Applying $W_1+2$ or
$Z_a$ to the $\mathcal C$- and $\mathcal R$-terms of level $k-1$: $W(\mathcal Cw) = \mathcal C(Ww)+(W\mathcal C)w$ and
likewise for $\mathcal R$, where $W\mathcal C$, $W\mathcal R$ are of the same type ($R\partial_R(h^aR^{-b}c) =
-bh^aR^{-b}c$, $Z_a(h^aR^{-b}c) = h^aR^{-b}Z_ac$); the $\mathcal R$-terms of level $k-1$ act on words of length at most
$k-2$, so after one more letter at most $k-1$; the $\mathcal C$-terms of level $k-1$ act on words of length $k-1$, giving
$\mathcal C$-terms on words of length $k$ and terms $W\mathcal C$, of $\mathcal R$-type ($\mathcal C$-type coefficients
lie in the $\mathcal R$-type class), on words of length $k-1$. The classes: near $F_K$, $hR^{-1} = \hat
h\asymp\rho_{\mathrm{sf}}$, $h^2R^{-1} = \hat h^2R$, $h^2R^{-2} = \hat h^2$; near $F_I$, $hR^{-1} = hx_I^2$, $h^2R^{-1} =
h^2x_I^2$, $h^2R^{-2} = h^2x_I^4$; and $w_{\mathbf m-\mathbf e} = \varpi$ ($\hat h$, resp. $hx_I^2$) and $w_{\mathbf
m-2\mathbf e}$ at differential order 0 is $\varpi\rho_{\mathrm{sf}}$ up to smooth positive factors at finite frequencies;
as multiplication operators they have differential order 0. $\square$

*The commuted system.* For $k\ge1$ let $U_k := (W^\alpha u)_{|\alpha| = k}$, with values in $\mathbb C^N\otimes\mathbb
C^{7^k}$ and the fibre inner product $\mathfrak e^{\oplus7^k}$, and
$$P^{(k)} := \mathrm{diag}_\alpha(P-j_\alpha L)-(\mathcal C_{\alpha\beta})_{\alpha\beta}\in P\otimes\mathrm{Id}+\Psi^{
\mathbf m-\mathbf e},\qquad P^{(k)}U_k = F_k := \Big(W^\alpha_\sharp Pu+\sum_{|\beta|\le k-1}\mathcal R_{\alpha
\beta}W^\beta u\Big)_\alpha.\tag{4.3}$$

**Lemma 4.2 (the thresholds of the system).** With $p^{(k)}_1$ and $\tilde p^{(k)}_1$ the principal symbols (at the level
$\mathbf m-\mathbf e$) of the imaginary parts of $P^{(k)}$ and $z^{-1}P^{(k)}$, decomposed as in Lemma 3.3 with the same
$\lambda$ and $\mathcal A$, at the four radial sets ($\mathrm{Re}\,z = 1$, resp. on the zero section):
$$\varpi^{-1}p^{(k)}_1 = \varpi^{-1}p_1\otimes\mathrm{Id}-\mathrm{diag}(j_\alpha)\cdot\begin{cases}0&\text{at }R_{I^+,1,
\mathrm{in}},\\2&\text{at }R_{\mathrm{cf},1,\mathrm{in}},\end{cases}\qquad\varpi^{-1}\tilde p^{(k)}_1 = \varpi^{-1}
\tilde p_1\otimes\mathrm{Id}-2\,\mathrm{diag}(j_\alpha)\ \text{at }R_{I^+,\mathrm{out}},R_{\mathrm{cf},\mathrm{out}}.$$
So the threshold quantities $\mathcal T^{(k)}$ of Proposition 2.4 satisfy $\mathcal T^{(k)}\ge\mathcal
T\otimes\mathrm{Id}$ at each of the four radial sets, and (R1)-(R4) of Lemma 3.3 hold for $P^{(k)}$, resp.
$z^{-1}P^{(k)}$, with the same orders.

*Proof.* $\mathcal C$ is in $\Psi^{\mathbf m-2\mathbf e}$, so does not contribute at the level $\mathbf m-\mathbf e$.
Near $F_K$, $hR\partial_R\mapsto iR(1+\hat h)\xi_{c\hbar}$, so $L$ has symbol $2i\hat h(z+R(1+\hat h)\xi_{c\hbar})$ and
$z^{-1}L$ has symbol $2i\hat h(1+z^{-1}R(1+\hat h)\xi_{c\hbar})$; at $R = 0$ their imaginary parts are $2\hat
h\,\mathrm{Re}\,z = 2\hat h$ and $2\hat h$. Near $F_I$, $hR\partial_R = -\frac12hx_I\partial_{x_I}\mapsto-\frac i2\xi$,
so $L$ has symbol $ihx_I^2(2z-\xi)$, with imaginary part $hx_I^2(2\,\mathrm{Re}\,z-\xi)$, which is 0 at $\xi = 2$,
$\mathrm{Re}\,z = 1$; and $z^{-1}L$ has symbol $ihx_I^2(2-z^{-1}\xi)$, with imaginary part $2hx_I^2$ at $\xi = 0$. The
case (A) parts ($\lambda Q_1$) and case (B) parts ($\lambda\mathcal A$) are untouched; $L$ and its imaginary part lie in
$\Psi^{\mathbf m-\mathbf e}$, so enter $\mathcal P_1$, resp. $\tilde{\mathcal P}_1$, only. In $\mathcal T =
2\tilde\kappa\beta_\varrho-2\varsigma\epsilon_\flat\varpi^{-1}p_1$ ($\varsigma = \epsilon_\flat = 1$), lowering
$\varpi^{-1}p_1$ by $2j_\alpha$ raises $\mathcal T$ by $4j_\alpha$. $\square$

### 4.2 The estimate

**Proposition 4.3 ([Hin26c] Proposition 10.6 (2) at $n = 4$).** Assume (3.1), and let $h_0$, the families (3.2) and the
orders be as in Proposition 3.1. For every $k\in\mathbb N_0$ there is $C_k$ such that for $h<h_0$ (after decreasing $h_0$
depending on $k$) and $z$ in the families,
$$\|u\|_{\mathbf o;k}\le C_k\|P_{\iota,h,z}u\|_{Y_{\mathbf o};k},\qquad\|u\|_{\mathbf o;k,+}\le C_k\|P_{\iota,h,z}u
\|_{Y_{\mathbf o};k,+},\tag{4.4}$$
and $P_{\iota,h,z}:\{u\in H^{\mathbf o}:\|u\|_{\mathbf o;k}<\infty\}\to\{f\in Y_{\mathbf o}:\|f\|_{Y_{\mathbf
o};k}<\infty\}$ is invertible. Equivalently, $N^0(h^{-1}z)$ is invertible between the spaces $H^{(\mathsf
s';k),(2\gamma_I,\gamma_{\mathrm{cf}})}_{0,b;b}(\iota^+)$ and $H^{(\mathsf
s'-2;k),(2\gamma_I+2,\gamma_{\mathrm{cf}}-2)}_{0,b;b}(\iota^+)$.

The second estimate of (4.4) follows from the first at the levels $0,\dots,k$: $h^{-j}\|u\|_{\mathbf o;k-j}\le
C_{k-j}h^{-j}\|Pu\|_{Y_{\mathbf o};k-j}$, and the sum of the right sides is $\|Pu\|_{Y_{\mathbf o};k,+}$ up to the
constants.

**Lemma 4.4 (regularity at fixed $h$).** For fixed $h\in(0,h_0)$ and $z$, if $u\in H^{\mathbf o}$ and $\|Pu\|_{Y_{\mathbf
o};k}<\infty$, then $\|u\|_{\mathbf o;k}<\infty$.

*Proof.* It suffices to take the fibre order $\mathsf s'$ of $\mathbf o$ constant, equal to $s_1 := \inf\mathsf s'$: if
$W^\alpha u$ lies in the space of fibre order $s_1$ for $|\alpha|\le k$, then by induction on $|\alpha|$, $PW^\alpha u =
W^\alpha Pu-[W^\alpha,P]u$, where $[W^\alpha,P] = \sum_{|\beta|<|\alpha|}A_{\alpha\beta}W^\beta$ with $A_{\alpha\beta}\in
x_I^2\rho_K^{-2}\mathrm{Diff}^2_{0,b}(\iota^+)$ (each $[W_i,P]$ is of that class, and b-fields normalise 0,b-fields; at
fixed $h$ no semiclassical order is tracked, unlike in (4.3)); so $PW^\alpha u\in Y_{\mathbf o}$, and elliptic regularity
at fibre infinity (Lemma 2.2 (c), at this fixed $h$) puts $W^\alpha u$ in $H^{\mathbf o}$. So let $\mathsf s'$ be
constant. For fixed $h$, $H^{\mathbf o}$ and $Y_{\mathbf o}$ are then weighted 0,b-Sobolev spaces with fixed weights and
a constant order (section 2.1), on which the dilations $(D_\lambda v)(R,\omega) := v(\lambda R,\omega)$,
$\lambda\in[\frac12,2]$, and the rotations of $\mathbb S^3$ act boundedly, uniformly: they preserve $\iota^+$, its faces
and the 0,b-structure ($x_I = R^{-1/2}$ is multiplied by $\lambda^{-1/2}$), and multiply the weights $x_I^a\rho_K^c$ and
the density by functions bounded above and below. For each letter let $G^{(i)}_\theta$ be the group it generates
($D_{e^\theta}$ for $W_1$, the rotations $e^{\theta Z_a}$ for $W_{1+a}$) and $T^{(i)}_\theta :=
\theta^{-1}(G^{(i)}_\theta-1)$, $0<|\theta|\le1$; for a word $\alpha$ and $\theta\in[-1,1]^k\setminus\{0\}$-coordinates
put $T^\alpha_\theta := T^{(\alpha_1)}_{\theta_1}\cdots T^{(\alpha_k)}_{\theta_k}$. By (1.12), $G_\theta PG_\theta^{-1}$
is $e^{-\theta}(-2R^{-1}B)+e^{-2\theta}h^2R^{-2}P^{(0)}$ for dilations, and $P$ with $S_0$, $P^{(0)}_1$ transported by
the rotation for rotations; in both cases a family of second-order operators of the class of $P$ depending smoothly on
$\theta$. Hence $[T^{(i)}_\theta,X] = \theta^{-1}(G_\theta XG_\theta^{-1}-X)G_\theta$, for $X$ of that class, is again
uniformly of that class composed with $G_\theta$, and so are the iterated commutators; all are bounded $H^{\mathbf o}\to
Y_{\mathbf o}$ uniformly (for fixed $h$ the sf orders are immaterial, and the weights at 0f and cf of $P$ are those of
$\mathbf o-Y_{\mathbf o}$). By the Leibniz rule for these commutators, $PT^\alpha_\theta u = T^\alpha_\theta Pu+\sum
X_{\alpha,\theta,S}T^{\alpha_S}_{\theta_S}u$, the sum over proper subsets $S\subsetneq\{1,\dots,k\}$, $\alpha_S$ the
subword, with $X_{\alpha,\theta,S}$ uniformly bounded $H^{\mathbf o}\to Y_{\mathbf o}$. Induction on $k$: if $W^\beta
u\in H^{\mathbf o}$ for $|\beta|<k$, then $T^{\alpha_S}_{\theta_S}u = \int G\cdots W^{\alpha_S}u$ (an average of
transported copies of $W^{\alpha_S}u$, by $T_\theta v = \theta^{-1}\int_0^\theta G_{\theta'}Wv\,d\theta'$) is bounded in
$H^{\mathbf o}$, and $T^\alpha_\theta Pu$ is bounded in $Y_{\mathbf o}$ as $W^\alpha Pu\in Y_{\mathbf o}$. So
$PT^\alpha_\theta u$ is bounded in $Y_{\mathbf o}$, and by (3.4) (at this fixed $h$, $T^\alpha_\theta u\in H^{\mathbf
o}$), $T^\alpha_\theta u$ is bounded in $H^{\mathbf o}$; a weak limit point as $\theta\to0$ is $W^\alpha u$, which
therefore lies in $H^{\mathbf o}$. $\square$

*Proof of Proposition 4.3.* The case $k = 0$ is Proposition 3.1. Let $k\ge1$ and assume (4.4) at the levels below $k$. By
density (Lemma 2.2 (g) for the norms $\|\cdot\|_{\mathbf o;k}$, whose proof is the same: the mollifiers $J_\epsilon$ and
the cut-offs $\chi_j$ commute with the $W$'s up to operators of the same kind, uniformly bounded and tending to 0) it
suffices to take $u\in C^\infty_c((\iota^+)^\circ)$.

*Step 1.* Lemma 3.4 holds for the system (4.3) in place of $P$: its proof uses Propositions 2.4-2.6 for $\mathbf P =
c_zP^{(k)}$ (with $P'' := P^{(k)}-P\otimes\mathrm{Id}\in\Psi^{\mathbf m-\mathbf e}$), whose hypotheses at the four radial
sets hold by Lemma 4.2, along the flow because $P''$ is of lower order (it enters only $\beta$ in Proposition 2.5), and
at fibre infinity and on the elliptic set because the principal symbol is $G_{\iota,z}\mathrm{Id}$. So
$$\|U_k\|_{\mathbf o}\le C\big(\|F_k\|_{Y_{\mathbf o}}+\|U_k\|_{(-N;2\gamma_I,\gamma_{\mathrm{cf}},\gamma_{\mathrm{cf}};
\mathsf b-\frac14)}\big).$$
By (4.3), $\|F_k\|_{Y_{\mathbf o}}\le C\|Pu\|_{Y_{\mathbf o};k}+C\sum_{|\beta|\le k-1}\|\mathcal R_{\alpha\beta}W^\beta
u\|_{Y_{\mathbf o}}$, and $\mathcal R_{\alpha\beta}\in\Psi^{\mathbf m-\mathbf e}$ maps $H^{\mathbf o-\mathbf e_1}\to
H^{\mathbf o-\mathbf m+\mathbf e-\mathbf e_1} = Y_{\mathbf o}$ (Lemma 2.2 (a)), so these terms are at most
$C\|u\|_{\mathbf o;k-1}\le C\|Pu\|_{Y_{\mathbf o};k-1}$ by the induction hypothesis. And $\|U_k\|_{(-N;\dots;\mathsf
b-\frac14)}\le\sum_{|\alpha| = k}\|W^\alpha u\|_{\mathbf o_\flat}$.

*Step 2.* Lemma 3.6 holds with $k$ b-derivatives:
$$\|u\|_{\mathbf o_\flat;k}\le C\|Pu\|_{Y_{\mathbf o};k}+Ch^{\delta_\flat}\|u\|_{\mathbf o;k}.\tag{4.5}$$
Indeed, Lemma 3.5 holds with $k$ b-derivatives on both sides of (3.15), with constants uniform as there: for $\hat\sigma
= \pm1+iy$ by I.A Theorem 7.2 (4) near sctf (at $\sigma_0 = \pm1$) and I.C Lemma 2.5 at the order $s+k$ near ztf, as in
the proof of I.C Theorem 4.3 (4), and the contradiction argument of I.C Corollary 5.2 (b) with I.C (4.5); for $\mathcal
Z^i$ by I.C Corollary 5.2 (b) with $k$. The b-vector fields of tf are spanned by $\hat R\partial_{\hat R} = R\partial_R$
and the $Z_a$, the same $W$'s, so the norms of I.C with $k$ b-derivatives are those of (4.1) on functions supported near
tf. In the proof of Lemma 3.6, apply $W^\alpha$, $|\alpha|\le k$: $[W,\chi_{\mathrm{tf}}]$ and $[W,1-\chi_{\mathrm{tf}}]$
are multiplications by functions of the same kind as the derivatives of $\chi_{\mathrm{tf}}$ (b-derivatives of
$\rho_{\mathrm{tf}}$, $\rho_{\mathrm{tf}}/\rho_{\mathrm{sf}}$ are bounded multiples of them, Lemma 2.1 (b)); $W^\alpha$
applied to $P-N_{\mathrm{tf}}(z) = -2h^2R^{-1}W_1(W_1+c+S_0)$, to $[P,\chi_{\mathrm{tf}}]$ and to
$\partial_zN_{\mathrm{tf}}$ gives sums of operators of the same classes applied to $W^\beta$, $|\beta|\le|\alpha|$ (by
Lemma 4.1 (a)-(b) and $[W_1,R^{-1}] = -R^{-1}$); and $m_h$ commutes with $W$ up to an element of the same symbol class.
Each estimate of that proof therefore holds with $\|\cdot\|_{\cdot;k}$ on both sides.

*Conclusion.* Combining, $\|u\|_{\mathbf o;k}\le\|u\|_{\mathbf o;k-1}+\|U_k\|_{\mathbf o}\le C\|Pu\|_{Y_{\mathbf
o};k}+Ch^{\delta_\flat}\|u\|_{\mathbf o;k}$, and for $h$ small the last term is absorbed. Invertibility: injectivity is
(4.4); given $f$ with $\|f\|_{Y_{\mathbf o};k}<\infty$, $u := P^{-1}f\in H^{\mathbf o}$ by Proposition 3.1, and
$\|u\|_{\mathbf o;k}<\infty$ by Lemma 4.4. $\square$

At $\mathscr I^+$ the source commutes with the e3b-fields of its Lemma 7.12 and reads the result on the Mellin side,
where the lower-order terms carry no factor $h$ and each b-derivative costs $h^{-1}$; here the b-fields $R\partial_R$,
$Z_a$ are used on all of $\iota^+$, the lower-order terms of (4.2) carry $hR^{-1}$ or $h^2R^{-2}$, which is the level
$\mathbf m-\mathbf e$ at both ends, and the estimate (4.4) holds without loss. Near $\iota^+\cap K^+$ this is the
source's Lemma 10.7 at $n = 4$, with $\mathcal V = (R\partial_R,Z_1,\dots,Z_6,I)$ there, and (4.2) is its
(10.32)-(10.33), its term $-2ikzhR^{-1}\delta_{\alpha,(k,0,\dots,0)}$ being the part $-2ij_\alpha zhR^{-1}$ of $-j_\alpha
L$.

## 5. Bounded frequencies ([Hin26c] Proposition 10.6 (1), Lemmas 10.9-10.10)

### 5.1 The statement

Throughout this section $\gamma_I<\frac32+\bar S$, $\gamma_{\mathrm{cf}} = -(\alpha_++2)$, and $(\beta_-,\beta_+)$ is the
indicial gap of $\hat P_0(0)$ that contains $-\gamma_{\mathrm{cf}}$ (section 1.1). We write $I(\lambda) :=
P^{(0)}(0,\omega,\lambda,\partial_\omega)$ for the Mellin symbol of $\hat P_0(0)$ at $\partial X$ and $\mathrm{spec}_b$
for the set of $\lambda$ at which $I(\lambda)$ is not invertible on $\mathbb S^3$ (I.C sections 1 and 2.5); so
$(\beta_-,\beta_+)\cap\mathrm{Re}\,\mathrm{spec}_b = \emptyset$. For an order $\mathsf s$ (a real number or a variable
order on ${}^{0,b}S^*\iota^+$) and $k\in\mathbb N_0$ put
$$\mathcal X^{\mathsf s}_k := H^{(\mathsf s;k),(2\gamma_I,\gamma_{\mathrm{cf}})}_{0,b;b}(\iota^+),\qquad\mathcal Y^{
\mathsf s}_k := H^{(\mathsf s;k),(2\gamma_I+2,\gamma_{\mathrm{cf}}-2)}_{0,b;b}(\iota^+),\qquad\mathcal X^{\mathsf s} :=
\mathcal X^{\mathsf s}_0,\ \mathcal Y^{\mathsf s} := \mathcal Y^{\mathsf s}_0,\tag{5.1}$$
with the b-density $\mu_b$ of section 1.1 (II.A section 6.2). The index $k$ counts b-derivatives along $W_1 =
R\partial_R$ and $W_{1+a} = Z_a$, $a = 1,\dots,6$, the rotation fields of $\mathbb S^3$ (section 4.1), which span the
b-vector fields of $\iota^+$ over $C^\infty(\iota^+)$. By (1.6), $N^0(\sigma)\in
x_I^2\rho_K^{-2}\mathrm{Diff}^2_{0,b}(\iota^+)$, and its commutators with the $W_i$ are of the same class (Lemma 4.4's
proof); so $N^0(\sigma):\mathcal X^{\mathsf s}_k\to\mathcal Y^{\mathsf s-2}_k$ is bounded.

**Proposition 5.1 ([Hin26c] Proposition 10.6 (1) at $n = 4$).** For every order $\mathsf s$, every $k\in\mathbb N_0$ and
every $\sigma\in\mathbb C$ with $\mathrm{Im}\,\sigma>-\gamma_I$,
$$N^0(\sigma):\mathcal X^{\mathsf s}_k\to\mathcal Y^{\mathsf s-2}_k\tag{5.2}$$
is Fredholm of index 0. If moreover $\mathrm{Im}\,\sigma>-1-\beta_+$, it is invertible.

The dimension enters only through $c = \frac32$: the upper bound $\gamma_I<c+\bar S$ ($1+\bar S$ at $n = 3$) is the upper
end of the weight interval of the 0-normal operator at $\mathscr I^+$ (Lemma 5.4), whose lower end gives
$\mathrm{Im}\,\sigma>-\gamma_I$ at every $n$; and $-1-\beta_+$ comes from the one-dimensional Fourier transform of Lemma
5.8, also at every $n$ (`iplusnorm5.py` N3, N5, N8).

*How this differs from the source.* The source builds a local left parametrix at $\iota^+\cap\mathscr I^+$ from [0C]
Theorem 1.5, which assumes a boundary spectrum independent of the boundary point, and uses the structure of its Schwartz
kernel for b-regularity. Here the parametrix is that of [0C] Theorem 3.4 (the 0-calculus with bounds, which needs no such
constancy), used only through the Fredholm property it gives on a compact manifold (Lemma 5.5), and b-regularity is
proved by difference quotients as in Lemma 4.4. The source's positivity argument for the reduced normal operator is
replaced by the asymptotics of modified Bessel functions (Lemma 5.4), and the Fourier transform bound the source quotes
from [Hin23d] Lemma 2.25 is proved (Lemma 5.7). The source's proof of Lemma 10.10 asks "$1+\mathrm{Im}\,\sigma<\beta_+$";
the condition its argument uses, and its statement asserts, is $-1-\mathrm{Im}\,\sigma<\beta_+$ (section 9, (F6)).

### 5.2 Two general facts

**Lemma 5.2 (Fredholm estimates with a weak remainder).** Let $T:X\to Y$ be a Fredholm operator between Banach spaces and
$j:X\to W$ a continuous injective linear map into a Banach space $W$. Then there is $C$ with $\|x\|_X\le
C(\|Tx\|_Y+\|jx\|_W)$ for all $x\in X$.

*Proof.* Let $e_1,\dots,e_m$ be a basis of $\ker T$. Since $j$ is injective, $je_1,\dots,je_m$ are linearly independent
in $W$, and the Hahn-Banach theorem gives $\ell_1,\dots,\ell_m\in W^*$ with $\ell_i(je_k) = \delta_{ik}$. Then $\Pi x :=
\sum_i\ell_i(jx)e_i$ is a continuous projection of $X$ onto $\ker T$, with $\|\Pi x\|_X\le C\|jx\|_W$. $T$ is injective
on the closed subspace $\ker\Pi$ and $T(\ker\Pi) = T(X)$ is closed, so by the open mapping theorem $\|x'\|_X\le
C\|Tx'\|_Y$ for $x'\in\ker\Pi$. Apply this to $x' := x-\Pi x$, for which $Tx' = Tx$, and add $\|\Pi x\|_X$. $\square$

**Lemma 5.3 (compact inclusions).** Let $\mathsf s'<\mathsf s$ (orders with $\sup(\mathsf s'-\mathsf s)<0$), $a'<a$ and
$c'<c$. Then $H^{\mathsf s,(a,c)}_{0,b}(\iota^+)\hookrightarrow H^{\mathsf s',(a',c')}_{0,b}(\iota^+)$ is compact. The
same holds for $x^aH^{\mathsf s}_0(\hat X)\hookrightarrow x^{a'}H^{\mathsf s'}_0(\hat X)$ on the compact manifold $\hat
X$ of section 5.3.

*Proof.* Let $\chi\in C^\infty([0,\infty))$ vanish on $[0,1]$ and equal 1 on $[2,\infty)$, and for
$\epsilon\in(0,\frac14)$ let $\chi_\epsilon := \chi(x_I/\epsilon)\chi(\rho_K/\epsilon)$. Its 0,b-derivatives are bounded
uniformly in $\epsilon$ ($x_I\partial_{x_I}$ and $\rho_K\partial_{\rho_K}$ of $\chi(\cdot/\epsilon)$ are
$(t\chi')(\cdot/\epsilon)$). With $w := x_I^{-a}\rho_K^{-c}u$, $x_I^{-a'}\rho_K^{-c'}(1-\chi_\epsilon)u = f_\epsilon w$,
$f_\epsilon := (1-\chi_\epsilon)x_I^{a-a'}\rho_K^{c-c'}$, and every $C^\infty_b$-seminorm of $f_\epsilon$ is at most
$C(2\epsilon)^\delta$, $\delta := \min(a-a',c-c')$, because $1-\chi_\epsilon$ is supported where $x_I\le2\epsilon$ or
$\rho_K\le2\epsilon$ and $x_I,\rho_K\le1$ on $\iota^+$ (after normalising the defining functions). Multiplication by
$f_\epsilon$ is bounded on $H^{\mathsf s'}_{0,b}$ with norm bounded by finitely many such seminorms (II.A (S5)-(S6)), so
$\|(1-\chi_\epsilon)u\|_{H^{\mathsf s',(a',c')}}\le C\epsilon^\delta\|u\|_{H^{\mathsf s,(a,c)}}$. And
$u\mapsto\chi_\epsilon u$ maps into distributions supported in a fixed compact subset of $(\iota^+)^\circ$, where all
these norms are the standard ones, so it is compact by Rellich's theorem. The inclusion is the norm limit of compact
operators as $\epsilon\to0$. On $\hat X$ the same argument with $\chi(x/\epsilon)$. $\square$

### 5.3 The model at $\mathscr I^+$

Near $\iota^+\cap\mathscr I^+$ use $(x,\omega) := (x_I,\omega)\in[0,4)\times\mathbb S^3$, which covers
$\{R>\frac1{16}\}$. By (1.6),
$$L_\sigma := x^{-2}N^0(\sigma) = -\tfrac12\big(x\partial_x-2i\sigma\big)\big(x\partial_x-2(c+S_0)\big)+x^2P^{(0)}\big(0,
\omega,\tfrac12x\partial_x,\partial_\omega\big)\in\mathrm{Diff}^2_0\tag{5.3}$$
there, with 0-principal symbol $(\frac12+\frac14x^2)\xi_0^2+|\eta_0|^2$ (section 1.3), positive definite.

*The compact model.* Let $\hat X := \{y\in\mathbb R^4:|y|\le8\}$, and identify $\{4<|y|\le8\}$ with $[0,4)_x\times\mathbb
S^3$ by $x = 8-|y|$, $\omega = y/|y|$; so $\partial\hat X = \{x = 0\}$, a compact manifold with boundary of dimension 4.
Let $\chi_3\in C^\infty_c([0,4))$ equal 1 on $[0,3]$, read as a function on $\hat X$ vanishing on $\{|y|\le4\}$, and put
$$\hat P := \chi_3L_\sigma+(1-\chi_3)\Delta_{\mathbb R^4}\in\mathrm{Diff}^2_0(\hat X;\mathbb C^N).\tag{5.4}$$
Its principal symbol is a convex combination of positive definite forms, so $\hat P$ is 0-elliptic, and $\hat P =
L_\sigma$ on $\{x<3\}$. Fix a smooth positive density $\nu_0$ on $\hat X^\circ$ equal to $x^{-4}|dx\,d\omega|$ on
$\{x<4\}$ (a 0-density) and put $\mu_b := x^3\nu_0$ there (a b-density, a constant multiple of that of $\iota^+$, as
$|\frac{dR}R| = 2|\frac{dx}x|$). The spaces $x^\alpha H^m_0(\hat X)$ are taken with $\mu_b$. Near $\partial\hat X$ they
coincide with the 0,b-spaces of $\iota^+$ near $\iota^+\cap\mathscr I^+$ (II.A section 6.2, the cells $U_{3,jk\pm}$), and
with the spaces of [0C] section 3.1 under the identification $g\mapsto g\nu_0^{1/2}$ of functions with 0-half-densities:
$x^\alpha L^2(\mu_b)$ corresponds to $\rho^{\alpha-\frac32}L^2(\hat X,{}^0\Omega^{\frac12})$, which is [0C] (3.23), and
for integer $m$ both families of norms are equivalent to $\sum_{|\gamma|\le m}\|x^{-\alpha}V^\gamma u\|_{L^2(\mu_b)}$
over products of the 0-fields $x\partial_x$, $xZ_a$ (elliptic regularity in either calculus), negative orders being the
duals. Under this identification $\hat P$ is an operator on 0-half-densities with the coefficients ([0C] (1.3)) it has on
functions. Only integer orders are used in this section's appeals to $\hat X$.

**Lemma 5.4 (the reduced normal operator).** Let $\sigma\in\mathbb C$, $\omega_0\in\mathbb S^3$ and $\alpha\in I_\sigma
:= (-2\,\mathrm{Im}\,\sigma,2(c+\bar S))$. Then $\hat P$ is fully elliptic at the weight $\alpha$ in the sense of [0C]
Definition 1.2, at every boundary point.

*Proof.* In normal coordinates $y$ on $\mathbb S^3$ centred at $\omega_0$, write $\hat P$ near $(0,\omega_0)$ in the form
[0C] (1.3). The coefficients of the terms with $|\beta|\le1$ or with $(x\partial_x)^jx^2$ factors vanish at $x = 0$,
except those of the first term of (5.3): $x^2P^{(0)}(0,\omega,\frac12x\partial_x,\partial_\omega)$ equals
$g^{ij}(y)(xD_{y_i})(xD_{y_j})$ plus terms with a factor $x$, because $P^{(0)}(0,\cdot)-((\rho D_\rho)^2+\Delta_{\mathbb
S^3})\mathrm{Id}\in\mathrm{Diff}^1_b$ (II.C Lemma 1.2) and $x^2\partial_\omega = x\cdot x\partial_\omega$,
$x^2(x\partial_x) = x\cdot x(x\partial_x)$. So [0C] (1.4)-(1.5) give the reduced normal operator
$$\hat N(\hat P,\omega_0,\hat\eta) = -\tfrac12\big(t\partial_t-2i\sigma\big)\big(t\partial_t-2(c+S_*)\big)+\kappa^2t^2,
\qquad S_* := S_0(\omega_0),\ \kappa^2 := g^{ij}(\omega_0)\hat\eta_i\hat\eta_j>0.$$
(1) The indicial operator is the first term, and $\det\big[-\frac12(z-2i\sigma)(z-2(c+S_*))\big] = 0$ exactly for $z =
2i\sigma$ and $z\in2(c+\mathrm{spec}\,S_*)$, with real parts $-2\,\mathrm{Im}\,\sigma$ and
$2(c+\mathrm{Re}\,\lambda)\ge2(c+\bar S)$ ($\bar S$ as in I.A (1.2)). With [0C]'s convention ($xD_x\mapsto\sigma'$, poles
at $\sigma' = -iz$) these are the points of $\mathrm{Spec}_b$, and none has real part $\alpha$.

(2) Let $u\in t^\alpha L^2((0,\infty),|\frac{dt}t|;\mathbb C^N)$ with $\hat Nu = 0$; $u$ is smooth, the equation being a
regular linear ODE on $(0,\infty)$. Choose a unitary $U$ with $U^{-1}S_*U$ upper triangular, with diagonal entries
$\lambda_1,\dots,\lambda_N$. The components $u_N,u_{N-1},\dots$ of $U^{-1}u$ satisfy, in this order, scalar equations
$-\frac12(t\partial_t-2i\sigma)(t\partial_t-2\mu)u_i+\kappa^2t^2u_i = f_i$, $\mu := c+\lambda_i$, where $f_i$ is a
combination of the $(t\partial_t-2i\sigma)u_j$, $j>i$; so by induction it suffices that the scalar equation with $f = 0$
has no nonzero solution in $t^\alpha L^2$. Put $u = t^pw$, $p := i\sigma+\mu$. Since
$(t\partial_t-2i\sigma)(t\partial_t-2\mu)t^p = t^p(t\partial_t+\nu)(t\partial_t-\nu)$ with $\nu := \mu-i\sigma$, the
equation becomes $((t\partial_t)^2-\nu^2-2\kappa^2t^2)w = 0$, which in $s := \sqrt2\kappa t$ is the modified Bessel
equation $s^2w''+sw'-(s^2+\nu^2)w = 0$. Here $\mathrm{Re}\,\nu = \mathrm{Re}\,\mu+\mathrm{Im}\,\sigma$, and $w\in
t^aL^2(|\frac{dt}t|)$ with $a := \alpha+\mathrm{Im}\,\sigma-\mathrm{Re}\,\mu$; $\alpha<2(c+\bar S)\le2\,\mathrm{Re}\,\mu$
gives $a<\mathrm{Re}\,\nu$, and $\alpha>-2\,\mathrm{Im}\,\sigma$ gives $a>-\mathrm{Re}\,\nu$. So
$\mathrm{Re}\,\nu>|a|\ge0$. The solutions are $w = AI_\nu(s)+BK_\nu(s)$ (DLMF 10.25.1; the Wronskian $\mathscr
W\{K_\nu,I_\nu\}(s) = 1/s$, DLMF 10.28.2, so this is the general solution for every $\nu$). As $s\to\infty$, $I_\nu(s) =
(2\pi s)^{-1/2}e^s(1+O(s^{-1}))$ and $K_\nu(s) = (\frac\pi{2s})^{1/2}e^{-s}(1+O(s^{-1}))$ (DLMF 10.40.1-10.40.2), so
$w\in t^aL^2$ near $\infty$ forces $A = 0$. As $s\to0$, for $\mathrm{Re}\,\nu>0$, $K_\nu(s)\sim\frac12\Gamma(\nu)(\frac
s2)^{-\nu}$ (DLMF 10.30.2), and $\Gamma(\nu)\ne0$; so $|w|\ge c|B|s^{-\mathrm{Re}\,\nu}$ near 0, which lies in
$s^aL^2(|\frac{ds}s|)$ near 0 only if $-\mathrm{Re}\,\nu>a$. Hence $B = 0$.

(3) The adjoint for $|\frac{dt}t|$ and the standard Hermitian form is $\hat N^* =
-\frac12(t\partial_t+2(c+S_*^*))(t\partial_t-2i\bar\sigma)+\kappa^2t^2$, as $(t\partial_t)^* = -t\partial_t$. In the same
basis $U^{-1}S_*^*U$ is lower triangular with diagonal $\bar\lambda_i$, so the components are solved in the order
$1,2,\dots$, and the scalar equation $-\frac12(t\partial_t+2\bar\mu)(t\partial_t-2i\bar\sigma)v = -\kappa^2t^2v$ becomes,
with $v = t^pw$, $p := i\bar\sigma-\bar\mu$, the modified Bessel equation of order $\bar\nu$, $\mathrm{Re}\,\bar\nu =
\mathrm{Re}\,\nu$. Now $v\in t^{-\alpha}L^2$ gives $w\in t^{-a}L^2$, as $\mathrm{Re}\,p =
\mathrm{Im}\,\sigma-\mathrm{Re}\,\mu$, and $|{-a}|<\mathrm{Re}\,\bar\nu$; the argument of (2) gives $v = 0$. $\square$

**Lemma 5.5 (the model's Fredholm property).** Let $\mathrm{Im}\,\sigma>-\gamma_I$. (a) For every $m\in\mathbb Z$, $\hat
P:x^{2\gamma_I}H^m_0(\hat X)\to x^{2\gamma_I}H^{m-2}_0(\hat X)$ is Fredholm, and so is the formal adjoint $\hat P^*$ (for
$\mu_b$ and the standard Hermitian form) $:x^{-2\gamma_I}H^{2-m}_0(\hat X)\to x^{-2\gamma_I}H^{-m}_0(\hat X)$. (b) For
$m\in\mathbb Z$, $N'\in\mathbb N$, $\beta<2\gamma_I$ and $\beta'<-2\gamma_I$ there is $C$ with
$$\|w\|_{x^{2\gamma_I}H^m_0}\le C\big(\|\hat Pw\|_{x^{2\gamma_I}H^{m-2}_0}+\|w\|_{x^\beta H^{-N'}_0}\big),\qquad\|w
\|_{x^{-2\gamma_I}H^{2-m}_0}\le C\big(\|\hat P^*w\|_{x^{-2\gamma_I}H^{-m}_0}+\|w\|_{x^{\beta'}H^{-N'}_0}\big).\tag{5.5}$$

*Proof.* (a) $2\gamma_I\in I_\sigma$: $2\gamma_I>-2\,\mathrm{Im}\,\sigma$ by assumption and $2\gamma_I<2(c+\bar S)$.
Choose $\alpha_0<2\gamma_I<\alpha_1$ and $\epsilon>0$ with $[\alpha_0-\epsilon,\alpha_1+\epsilon]\subset I_\sigma$. By
Lemma 5.4, $\hat P$ is fully elliptic at every weight there, and [0C] Theorem 3.4 (with its $n = \dim\hat X = 4$, so $n-1
= 3$) gives $Q,Q'\in\Psi^{-2}_0+\Psi^{-\infty,(\alpha_1,3-\alpha_0)}_0+\Psi^{-\infty,(\alpha_1,3-\alpha_0)}$ with $\hat
PQ = I-R$, $Q'\hat P = I-R'$, $R\in\Psi^{-\infty,(\infty,3-\alpha_0)}$ and $R'\in\Psi^{-\infty,(\alpha_1,\infty)}$ (fully
residual operators on $\hat X^2$). Put $\alpha := 2\gamma_I$. A Schwartz kernel $k\,\pi_L^*\nu_0^{1/2}\pi_R^*\nu_0^{1/2}$
acts on functions by $g\mapsto\int k(\cdot,z')g(z')\nu_0(z')$, so $T_{\alpha_L,\alpha_R} := x^{-\alpha_L}Tx^{\alpha_R}$
has the kernel $\kappa := x^{-\alpha_L}k\,x'^{\alpha_R-3}$ against $\mu_b(z')$.

(i) *Fully residual kernels.* If $|k|\le Cx^ax'^b$ on $\hat X^2$ with $a>\alpha_L$ and $b>3-\alpha_R$, then
$\int|\kappa|\mu_b(z')\le Cx^{a-\alpha_L}\int x'^{b+\alpha_R-3}\mu_b(z')\le C$ and $\int|\kappa|\mu_b(z)\le
Cx'^{b+\alpha_R-3}\int x^{a-\alpha_L}\mu_b(z)\le C$, as $\int_0x^\delta\frac{dx}x<\infty$ for $\delta>0$; by Schur's test
$T_{\alpha_L,\alpha_R}$ is bounded on $L^2(\mu_b)$.

(ii) *Kernels on the 0-double space.* Let $k$ satisfy $|k|\le C\rho_{\mathrm{lb}}^a\rho_{\mathrm{rb}}^b$ on $\hat X^2_0$
with $a>\alpha$, $b>3-\alpha$ and $\alpha_L = \alpha_R = \alpha$. Near the boundary diagonal, in coordinates
$(x,y,x',y')$, $\rho_{\mathrm{lb}}\sim x/r$, $\rho_{\mathrm{rb}}\sim x'/r$, $r := x+x'+|y-y'|$. For fixed $z = (x,y)$
substitute $z' = (xs,y+xY)$: $\mu_b(z') = x^3s^{-1}ds\,dY$, $r = x(1+s+|Y|)$, and $\int|\kappa|\mu_b(z')\le
C\int_0^\infty\int_{\mathbb R^3}s^{\alpha+b-4}(1+s+|Y|)^{-a-b}dY\,ds$; the $Y$-integral is $C(1+s)^{3-a-b}$ (as $a+b>3$),
and $\int_0s^{\alpha+b-4}ds<\infty$ (as $\alpha+b>3$), $\int^\infty s^{\alpha-a-1}ds<\infty$ (as $a>\alpha$). For fixed
$z'$ substitute $z = (x's,y'+x'Y)$: $\mu_b(z) = x'^3s^{-1}ds\,dY$, and $\int|\kappa|\mu_b(z)\le C\int
s^{a-\alpha-1}(1+s+|Y|)^{-a-b}dY\,ds<\infty$ as $a>\alpha$ and $\alpha+b>3$. Away from the boundary diagonal $|k|\le
Cx^ax'^b$, covered by (i). So $T_{\alpha,\alpha}$ is bounded.

With $a = \alpha_1$, $b = 3-\alpha_0$, (i) and (ii) bound the residual parts of $Q$ and $Q'$ on $x^\alpha L^2(\mu_b)$.
Their kernels are conormal ([0C] section 2: $\mathcal A^{(\alpha_{\mathrm{lb}},\alpha_{\mathrm{rb}})}$ is stable under
the vector fields tangent to lb and rb), and the 0-fields of either factor lift to $\hat X^2_0$ tangent to lb, rb and ff
([0C] section 1); so the same bounds hold after applying them on either side, and these parts map $x^\alpha H^{m-2}_0$ to
$x^\alpha H^m_0$ for every integer $m$. The part in $\Psi^{-2}_0$ does so by the boundedness of the small 0-calculus on
weighted 0-Sobolev spaces ([MM87], which [0C] Corollary 3.3 uses in the same way). By (i) with $\alpha_R = \alpha$ and
$\alpha<\alpha_L<\alpha_1$, $R'$ maps $x^\alpha H^m_0$ boundedly into $x^{\alpha_L}H^{m+1}_0$, which embeds compactly in
$x^\alpha H^m_0$ (Lemma 5.3); likewise $R$ ($a = \infty$, $b = 3-\alpha_0>3-\alpha$) is compact on $x^\alpha H^{m-2}_0$.
So $Q'\hat P = I-R'$ and $\hat PQ = I-R$ make $\hat P$ Fredholm at the weight $\alpha = 2\gamma_I$: finite-dimensional
kernel and closed range from the first, finite codimension from the second. This is [0C] Corollary 3.6 at $\alpha =
2\gamma_I$, whose proof [0C] leaves to the reader. Under the $L^2(\mu_b)$ pairing the duals of $x^{2\gamma_I}H^m_0$ and
$x^{2\gamma_I}H^{m-2}_0$ are $x^{-2\gamma_I}H^{-m}_0$ and $x^{-2\gamma_I}H^{2-m}_0$ (II.A Lemma 7.1), and the Banach
adjoint of $\hat P$ acts on them as the formal adjoint $\hat P^*$ (test against $C^\infty_c(\hat X^\circ)$, which is
dense). The adjoint of a Fredholm operator is Fredholm.

(b) Lemma 5.2 with the injections $x^{2\gamma_I}H^m_0\hookrightarrow x^\beta H^{-N'}_0$ and
$x^{-2\gamma_I}H^{2-m}_0\hookrightarrow x^{\beta'}H^{-N'}_0$. $\square$

### 5.4 The Fredholm property ([Hin26c] Lemma 10.9)

Under the $L^2(\mu_b)$ pairing (II.A Lemma 7.1), $(\mathcal X^{\mathsf s})^* = H^{-\mathsf
s,(-2\gamma_I,-\gamma_{\mathrm{cf}})}_{0,b}$ and $(\mathcal Y^{\mathsf s-2})^* = H^{2-\mathsf
s,(-2\gamma_I-2,2-\gamma_{\mathrm{cf}})}_{0,b}$; $N^0(\sigma)^*$ denotes the formal adjoint for $\mu_b$ and the standard
Hermitian form on $\mathbb C^N$, which is the Banach adjoint of (5.2) at $k = 0$ on these spaces.

**Lemma 5.6 ([Hin26c] Lemma 10.9 at $n = 4$).** Let $\mathrm{Im}\,\sigma>-\gamma_I$, let $\mathsf s$ be an order and
$N\in\mathbb N$ with $N>\sup|\mathsf s|+1$. Put $\mathcal Z_N := H^{-N,(2\gamma_I-1,\gamma_{\mathrm{cf}}-1)}_{0,b}$ and
$\mathcal Z^*_N := H^{-N,(-2\gamma_I-3,1-\gamma_{\mathrm{cf}})}_{0,b}$.

(a) There is $C$ with
$$\|u\|_{\mathcal X^{\mathsf s}}\le C\big(\|N^0(\sigma)u\|_{\mathcal Y^{\mathsf s-2}}+\|u\|_{\mathcal Z_N}\big),\qquad u
\in\mathcal X^{\mathsf s},\tag{5.6}$$
$$\|v\|_{(\mathcal Y^{\mathsf s-2})^*}\le C\big(\|N^0(\sigma)^*v\|_{(\mathcal X^{\mathsf s})^*}+\|v\|_{\mathcal Z^*_N}
\big),\qquad v\in(\mathcal Y^{\mathsf s-2})^*,\tag{5.7}$$
and the inclusions $\mathcal X^{\mathsf s}\hookrightarrow\mathcal Z_N$, $(\mathcal Y^{\mathsf
s-2})^*\hookrightarrow\mathcal Z^*_N$ are compact.

(b) $N^0(\sigma):\mathcal X^{\mathsf s}\to\mathcal Y^{\mathsf s-2}$ is Fredholm of index 0.

(c) If $u\in\mathcal X^{\mathsf s}$ and $N^0(\sigma)u\in\mathcal Y^{\mathsf s'-2}_k$ with $\mathsf s'\ge\mathsf s$ and
$k\in\mathbb N_0$, then $u\in\mathcal X^{\mathsf s'}_k$.

*Proof.* (a) *Step 1: the elliptic estimate.* $N^0(\sigma)$ is elliptic in $x_I^2\rho_K^{-2}\mathrm{Diff}^2_{0,b}$
(section 1.3), so microlocal elliptic regularity in the calculus of the structure of II.A section 6.2 ((S5), with (S8)
for variable orders, and $B = I$) gives, as in II.A Lemma 8.4 (c),
$$\|u\|_{\mathcal X^{\mathsf s}}\le C\big(\|N^0(\sigma)u\|_{\mathcal Y^{\mathsf s-2}}+\|u\|_{\mathcal X^{-N}}\big)
\tag{5.8}$$
(the remainder of (S5) is bounded by $\|u\|_{\mathcal X^{-N}}$). Let $\chi\in C^\infty_c([0,2))$ equal 1 on $[0,1]$, read
as $\chi(R)$, and $\chi_1(x_I)$ the same function of $x_I$. Since $1-\chi(R)$ is supported in $\{R\ge1\} = \{x_I\le1\}$,
where $\chi_1(x_I) = 1$, $\|u\|_{\mathcal X^{-N}}\le\|\chi(R)u\|_{\mathcal X^{-N}}+C\|\chi_1(x_I)u\|_{\mathcal X^{-N}}$.

*Step 2: near $\iota^+\cap K^+$.* There the 0,b-structure is the b-structure of the end $\varrho = R$, $t = -\log R$, in
the sense of I.C section 2.2 (II.A section 6.2, the cells $U_{2,jk\pm}$), and $\|\chi u\|_{\mathcal X^{-N}}\sim\|\chi
u\|_{H^{-N}_{b,\gamma_{\mathrm{cf}}}}$. The operator $L_K := R^2N^0(\sigma) =
-2R(i\sigma+R\partial_R)(R\partial_R+c+S_0)+P^{(0)}(0,\omega,-R\partial_R,\partial_\omega)$ is of the form of I.C section
2.5 on $\{R<4\}$, with $B_j$ polynomial in $R$, normal operator $P^{(0)}(0,\omega,-R\partial_R,\partial_\omega)$, Mellin
symbol $J(\lambda) = I(-\lambda)$, $\mathrm{spec}_J = -\mathrm{spec}_b$, as for the operator at ztf in I.C section 4.1
(c); and it is b-elliptic, its principal symbol in $(t,\omega)$ being $(1+2R)\tau^2+|\eta|^2$. As
$-\gamma_{\mathrm{cf}}\in(\beta_-,\beta_+)$, $\gamma_{\mathrm{cf}}\notin\mathrm{Re}\,\mathrm{spec}_J$, and I.C Lemma 2.6
(2.3) with $m = -N$, $c = \gamma_{\mathrm{cf}}$ gives, with $\tilde\chi\in C^\infty_c([0,3))$ equal to 1 on $[0,2]$,
$$\|\chi u\|_{H^{-N}_{b,\gamma_{\mathrm{cf}}}}\le C\big(\|\tilde\chi L_Ku\|_{H^{-N-2}_{b,\gamma_{\mathrm{cf}}}}+\|\tilde
\chi u\|_{H^{-N}_{b,\gamma_{\mathrm{cf}}-1}}\big)\le C\big(\|N^0(\sigma)u\|_{\mathcal Y^{\mathsf s-2}}+\|u\|_{
\mathcal Z_N}\big),$$
since $R^2$ moves the weight $\gamma_{\mathrm{cf}}-2$ of $\mathcal Y$ to $\gamma_{\mathrm{cf}}$ and $-N-2\le\mathsf s-2$.

*Step 3: near $\iota^+\cap\mathscr I^+$.* $\chi_1u$ is supported in $\{x<2\}$ and lies in $x^{2\gamma_I}H^{-N}_0(\hat
X)$, transplanted. On $\{x<3\}$, $\hat P = L_\sigma = x^{-2}N^0(\sigma)$, so $\hat P(\chi_1u) =
x^{-2}(\chi_1N^0(\sigma)u+[N^0(\sigma),\chi_1]u)$, the commutator being a first-order operator with coefficients
supported in $\{1\le x_I\le2\}$, a compact subset of $(\iota^+)^\circ$. Lemma 5.5 (b) with $m = -N$, $N' = N$, $\beta =
2\gamma_I-1$ gives
$$\|\chi_1u\|_{\mathcal X^{-N}}\le C\big(\|\chi_1N^0(\sigma)u\|_{\mathcal Y^{-N-2}}+\|u\|_{H^{-N-1}(\{1\le x_I\le2\})}+\|
\chi_1u\|_{\mathcal Z_N}\big)\le C\big(\|N^0(\sigma)u\|_{\mathcal Y^{\mathsf s-2}}+\|u\|_{\mathcal Z_N}\big),$$
using that on a compact subset of $(\iota^+)^\circ$ all weights are equivalent.

Steps 1-3 give (5.6). For (5.7) the same three steps apply to $N^0(\sigma)^*$, which is elliptic with the same (real,
scalar) principal symbol. Near $K^+$: $N^0(\sigma)^* = L_K^*R^{-2}$, and $w := R^{-2}v$ has the b-weight
$-\gamma_{\mathrm{cf}}$ when $v$ has $2-\gamma_{\mathrm{cf}}$. $L_K^*$ (for $\mu_b = |\frac{dR}R\,d\omega|$, under which
$(R\partial_R)^* = -R\partial_R$) is of the same form, with Mellin symbol $J(-\bar\lambda)^*$, so $\mathrm{spec}_{J^*} =
\overline{\mathrm{spec}_b}$, and $-\gamma_{\mathrm{cf}}\notin\mathrm{Re}\,\mathrm{spec}_b$; I.C Lemma 2.6 at $c =
-\gamma_{\mathrm{cf}}$ applies (as I.C applies it to adjoints in sections 3.1 and 4.4), with remainder $\|\tilde\chi
R^{-2}v\|_{H^{-N}_{b,-\gamma_{\mathrm{cf}}-1}} = \|\tilde\chi v\|_{H^{-N}_{b,1-\gamma_{\mathrm{cf}}}}$. Near $\mathscr
I^+$: $N^0(\sigma)^* = L_\sigma^*x^2$, and $w := x^2v$ lies in $x^{-2\gamma_I}H_0$ when $v$ lies in
$x^{-2\gamma_I-2}H_0$; the second estimate of (5.5) with $m = N+2$ (so $2-m = -N$) and $\beta' = -2\gamma_I-1$ gives the
remainder $\|\chi_1x^2v\|_{x^{-2\gamma_I-1}H^{-N}_0}\sim\|\chi_1v\|_{x^{-2\gamma_I-3}H^{-N}_0}$, which is $\mathcal
Z^*_N$'s weight.

The inclusions are compact by Lemma 5.3: every weight drops by 1, and the orders drop from $\mathsf s$, resp. $2-\mathsf
s$, to $-N$, below both as $N>\sup|\mathsf s|+1$.

(b) By (5.6) and the compact inclusion, $N^0(\sigma)$ has finite-dimensional kernel and closed range (Peetre's lemma, as
in I.A section 7.3). By (5.7), the kernel of $N^0(\sigma)^*$ on $(\mathcal Y^{\mathsf s-2})^*$, which is the annihilator
of the range, is finite-dimensional. So (5.2) is Fredholm at $k = 0$. *Index.* The kernel does not depend on $\mathsf s$:
if $N^0(\sigma)u = 0$ with $u\in\mathcal X^{\mathsf s}$, then $u\in\mathcal X^{\mathsf s'}$ for every $\mathsf s'$ by
(c); likewise the kernel of the adjoint, by the same elliptic regularity for $N^0(\sigma)^*$. So the index does not
depend on $\mathsf s$, and we may take $\mathsf s$ constant. For $\sigma,\sigma'$ in the half-plane
$\{\mathrm{Im}\,\sigma>-\gamma_I\}$, $N^0(\sigma)-N^0(\sigma') = -2i(\sigma-\sigma')R^{-1}(R\partial_R+c+S_0)$, which
maps $\mathcal X^{\mathsf s}\to\mathcal Y^{\mathsf s-2}$ with norm $\le C|\sigma-\sigma'|$ ($R^{-1}$ is $x_I^2$ near
$\mathscr I^+$ and raises the weight $\gamma_{\mathrm{cf}}$ to $\gamma_{\mathrm{cf}}-1$, stronger than
$\gamma_{\mathrm{cf}}-2$, near $K^+$). So $\sigma\mapsto N^0(\sigma)$ is continuous into the Fredholm operators on the
connected half-plane, and the index is constant there. At $\sigma = i/h$, with $h$ small, Proposition 3.1 (with $z =
i\in\mathcal Z^i$, any $\gamma_+<\gamma_I$, and the constant fibre order $\mathsf s$) gives invertibility on these
spaces. So the index is 0.

(c) The elliptic parametrix of II.A Lemma 8.4 (b), whose proof uses only (S5) and applies verbatim to the structure of
section 6.2 with $B = I$, gives $I = QN^0(\sigma)+R_J$ with $Q$ of order $-2$ (weights $x_I^{-2}\rho_K^2$) and $R_J$ of
order $-J$; so $u = QN^0(\sigma)u+R_Ju\in\mathcal X^{\min(\mathsf s',\mathsf s+J)}$, and repeating, $u\in\mathcal
X^{\mathsf s'}$. For $k\ge1$ put $s_1 := \inf\mathsf s'$, a constant; $u\in\mathcal X^{s_1}$ and $N^0(\sigma)u\in\mathcal
Y^{s_1-2}_k$. *b-regularity at the constant order $s_1$.* Argue by induction on $k$ exactly as in the proof of Lemma 4.4,
with (5.6) at the order $s_1$ (and $N>|s_1|+2$) in place of (3.4). The dilations $D_\lambda$, $\lambda\in[\frac12,2]$,
and the rotations act boundedly and uniformly on $\mathcal X^{s_1}$, $\mathcal Y^{s_1-2}$ and $\mathcal Z_N$ (constant
orders; the weights $x_I^a\rho_K^c$ and $\mu_b$ change by factors bounded above and below). $G_\theta
N^0(\sigma)G_\theta^{-1}$ is
$e^{-\theta}(-2R^{-1}(i\sigma+R\partial_R)(R\partial_R+c+S_0))+e^{-2\theta}R^{-2}P^{(0)}(0,\omega,-R
\partial_R,\partial_\omega)$ for dilations and the transported operator for rotations, so the commutators
$[T_\theta,N^0(\sigma)]$ and their iterates are uniformly bounded $\mathcal X^{s_1}\to\mathcal Y^{s_1-2}$ after
composition with $G_\theta$. In the inductive step $T^\alpha_\theta u$ is an average of transported copies of
$W^{(\alpha_1)}T^{\alpha'}_{\theta'}u$ with $T^{\alpha'}_{\theta'}u$ bounded in $\mathcal X^{s_1}$, hence bounded in
$H^{s_1-1,(2\gamma_I-1,\gamma_{\mathrm{cf}})}_{0,b}\subset\mathcal Z_N$, because a b-field maps $\mathcal X^{s_1}$ there
($Z_a = x_I^{-1}\cdot x_IZ_a$ near $\mathscr I^+$). So (5.6) bounds $T^\alpha_\theta u$ in $\mathcal X^{s_1}$, and a weak
limit point as $\theta\to0$ is $W^\alpha u$; thus $u\in\mathcal X^{s_1}_k$. *The order $\mathsf s'$.* For $|\alpha|\le
k$, $[W^\alpha,N^0(\sigma)] = \sum_{|\beta|<|\alpha|}A_{\alpha\beta}W^\beta$ with $A_{\alpha\beta}\in
x_I^2\rho_K^{-2}\mathrm{Diff}^2_{0,b}$, as each $[W_i,N^0(\sigma)]$ is of that class and the b-fields normalise the
0,b-fields ($[\partial_\omega,x_I\partial_\omega]\in x_I\mathcal V(\mathbb S^3)$, $[x_I\partial_{x_I},x_I\partial_\omega]
= x_I\partial_\omega$). By induction on $|\alpha|$, $N^0(\sigma)W^\alpha u = W^\alpha N^0(\sigma)u-\sum
A_{\alpha\beta}W^\beta u\in\mathcal Y^{\mathsf s'-2}$ and $W^\alpha u\in\mathcal X^{s_1}$, so the elliptic regularity
just proved puts $W^\alpha u$ in $\mathcal X^{\mathsf s'}$. $\square$

### 5.5 The kernel ([Hin26c] Lemma 10.10)

**Lemma 5.7 (the Fourier transform of conormal functions).** Let $a>0$, $\lambda\in\mathbb R$, and let $f\in
C^\infty((0,\infty)_v\times\mathbb S^3;\mathbb C^N)$ satisfy, for all $j$ and $\alpha$,
$|(v\partial_v)^j\partial_\omega^\alpha f|\le C_{j\alpha}v^a$ on $\{v\le2\}$ and $\le C_{j\alpha}v^{-\lambda}$ on
$\{v\ge\frac12\}$. Let $f^\sharp$ be its extension by 0 to $v\le0$, a tempered distribution on $\mathbb R\times\mathbb
S^3$, and $\hat f(\hat r,\omega) := (\mathcal Ff^\sharp)(\hat r,\omega) = \int e^{i\hat rv}f^\sharp(v,\omega)\,dv$. Then
$\hat f$ is smooth on $\{\hat r\ne0\}$, and for every $\epsilon>0$, $j$ and $\alpha$
$$|(\hat r\partial_{\hat r})^j\partial^\alpha_\omega\hat f(\hat r,\omega)|\le C(1+|\hat r|)^{-1-a}\Big(\frac{|
\hat r|}{1+|\hat r|}\Big)^{\min(\lambda-1,0)-\epsilon},\qquad\hat r\ne0.\tag{5.9}$$

*Proof.* Let $\psi\in C^\infty_c((\frac12,2))$ with $\sum_{l\in\mathbb Z}\psi(2^{-l}v) = 1$ for $v>0$, and $f_l :=
\psi(2^{-l}v)f$. Then $f^\sharp = \sum_lf_l$ in $\mathcal S'$ ($f^\sharp$ is locally integrable, as $a>0$, and
polynomially bounded; dominated convergence). On $\mathrm{supp}\,f_l$, $v\sim2^l$, and as $\partial_v^m =
v^{-m}p_m(v\partial_v)$ for a polynomial $p_m$, $|\partial_v^m\partial^\alpha_\omega f_l|\le C2^{-lm}M_l$ with $M_l :=
2^{la}$ for $l\le0$ and $2^{-l\lambda}$ for $l\ge0$. Hence $|\partial^\alpha_\omega\mathcal Ff_l(\hat
r)|\le\int|\partial^\alpha_\omega f_l|\,dv\le C2^lM_l$ and, integrating by parts $m$ times, $\le C|\hat
r|^{-m}2^{l(1-m)}M_l$; so $|\partial^\alpha_\omega\mathcal Ff_l(\hat r)|\le C2^lM_l\min(1,(2^l|\hat r|)^{-m})$. Since
$\mathcal F(\partial_v(vg)) = -\hat r\partial_{\hat r}\mathcal Fg$ ($\mathcal F\partial_v = -i\hat r\mathcal F$,
$\mathcal Fv = -i\partial_{\hat r}\mathcal F$), $(\hat r\partial_{\hat r})^j\mathcal Ff_l = \mathcal
F((-v\partial_v-1)^jf_l)$, and $(v\partial_v+1)^jf_l$ is a sum of terms of the same dyadic form with the same bounds; so
the bound holds for $(\hat r\partial_{\hat r})^j\partial^\alpha_\omega\mathcal Ff_l$ too. Fix $\hat r\ne0$ and
$K\in\mathbb Z$ with $2^{-K}\le|\hat r|<2^{1-K}$, and take $m>\max(1+a,1-\lambda)$. If $|\hat r|\ge1$ ($K\le0$):
$\sum_{l\le K}2^{l(1+a)}\le C2^{K(1+a)}$; $\sum_{K<l\le0}2^{l(1+a)}(2^l|\hat r|)^{-m}\le C|\hat r|^{-m}2^{K(1+a-m)}$;
$\sum_{l>0}2^{l(1-\lambda)}(2^l|\hat r|)^{-m}\le C|\hat r|^{-m}$; all are $\le C|\hat r|^{-1-a}$. If $|\hat r|<1$
($K\ge1$): $\sum_{l\le0}2^{l(1+a)}\le C$; $\sum_{0<l\le K}2^{l(1-\lambda)}\le C(1+2^{K(1-\lambda)}+K)\le C|\hat
r|^{\min(\lambda-1,0)-\epsilon}$; $\sum_{l>K}2^{l(1-\lambda)}(2^l|\hat r|)^{-m}\le C|\hat r|^{-m}2^{K(1-\lambda-m)}\le
C|\hat r|^{\lambda-1}$, which is $\le C|\hat r|^{\min(\lambda-1,0)}$. So $\sum_l\mathcal Ff_l$ converges with all these
derivatives locally uniformly on $\{\hat r\ne0\}$, to a smooth function satisfying (5.9), which is $\hat f$ there because
$\mathcal F$ is continuous on $\mathcal S'$. $\square$

This is the bound (10.41) the source quotes from [Hin23d] Lemma 2.25; it is one-dimensional in $v$, the sphere being a
parameter, so free of $n$.

**Lemma 5.8 ([Hin26c] Lemma 10.10 at $n = 4$).** Let $\mathrm{Im}\,\sigma>-\gamma_I$ and
$\mathrm{Im}\,\sigma>-1-\beta_+$. Then $N^0(\sigma)$ has trivial kernel on $\mathcal X^{\mathsf s}$.

*Proof.* Let $N^0(\sigma)u = 0$, $u\in\mathcal X^{\mathsf s}$. By Lemma 5.6 (c), $u\in\mathcal X^{s'}_k$ for all $s'$ and
$k$; so $x_I^{-2\gamma_I}\rho_K^{-\gamma_{\mathrm{cf}}}W^\alpha u\in L^2(\mu_b)$ for every product $W^\alpha$ of b-fields
(the weights commute with b-fields up to bounded factors), and Sobolev embedding on the unit cells of the b-structure of
$\iota^+$ (dimension 4; as in the proof of I.A Lemma 7.4 (b)) gives $u\in
x_I^{2\gamma_I}\rho_K^{\gamma_{\mathrm{cf}}}C^\infty_b(\iota^+)$. In $v := R^{-1}\in[0,\infty]$, $x_I^2 = v$ and $\rho_K
= (1+v)^{-1}$, and the b-fields are spanned by $v\partial_v = -R\partial_R$ and the $Z_a$. So $u_0 := v^{-i\sigma}u$
satisfies the hypotheses of Lemma 5.7 with
$$a := \gamma_I+\mathrm{Im}\,\sigma>0,\qquad\lambda := \gamma_{\mathrm{cf}}-\mathrm{Im}\,\sigma,\tag{5.10}$$
as $|v^{-i\sigma}| = v^{\mathrm{Im}\,\sigma}$ and $v\partial_v(v^{-i\sigma}g) = v^{-i\sigma}(v\partial_v-i\sigma)g$.

*The operator in $v$.* Conjugation by $R^{i\sigma}$ replaces $R\partial_R$ by $R\partial_R-i\sigma$; with $R\partial_R =
-v\partial_v$ and $R(R\partial_R) = -\partial_v$,
$$N^1(\sigma) := R^{i\sigma}R^2N^0(\sigma)R^{-i\sigma} = -2\partial_v\big(v\partial_v+i\sigma-c-S_0\big)+P^{(0)}\big(0,
\omega,v\partial_v+i\sigma,\partial_\omega\big)\tag{5.11}$$
(`iplusnorm5.py` N8; the source's formula before (10.39), with $c = 1$ there), and $N^1(\sigma)u_0 =
R^{i\sigma}R^2N^0(\sigma)u = 0$ on $\{v>0\}$. Let $u^\sharp$ be the extension of $u_0$ by 0 to $v\le0$. Then
$N^1(\sigma)u^\sharp = 0$ on $\mathbb R\times\mathbb S^3$: for $\phi\in C^\infty_c(\mathbb R\times\mathbb S^3;\mathbb
C^N)$, $\langle u^\sharp,N^1(\sigma)^t\phi\rangle = \lim_{\epsilon\downarrow0}\int_{v>\epsilon}u_0\cdot
N^1(\sigma)^t\phi\,dv\,d\omega$, and Green's formula on $\{v>\epsilon\}$ turns this into
$\int_{v>\epsilon}(N^1(\sigma)u_0)\cdot\phi+B_\epsilon = B_\epsilon$, where $B_\epsilon$ is an integral over
$\{\epsilon\}\times\mathbb S^3$ of products of $(v\partial_v)^l\partial^\gamma_\omega u_0$, $l\le1$, $|\gamma|\le2$, with
derivatives of $\phi$, with bounded coefficients (each $v$-integration by parts of $\partial_v$ or of $v\partial_v$
leaves one boundary term, and the $\omega$-integrations by parts none). So $|B_\epsilon|\le C_\phi\epsilon^a\to0$.
$u^\sharp$ is tempered, and $\mathcal F(v\partial_vg) = -(\hat r\partial_{\hat r}+1)\mathcal Fg$, $\mathcal
F(\partial_vg) = -i\hat r\mathcal Fg$, so $\hat u := \mathcal Fu^\sharp$ satisfies, in $\mathcal S'(\mathbb
R\times\mathbb S^3)$,
$$\Big[2i\hat r\big(-\hat r\partial_{\hat r}+i\sigma-(c+1)-S_0\big)+P^{(0)}\big(0,\omega,-\hat r\partial_{\hat r}-1+i
\sigma,\partial_\omega\big)\Big]\hat u = 0,\tag{5.12}$$
the source's (10.40) with $i\sigma-2-S$ there ($c = 1$) and $i\sigma-\frac52-S_0$ here (`iplusnorm5.py` N8).

*Reduction to the transition face.* For $\hat r>0$ put $w_\pm(\hat r,\omega) := \hat u(\pm\hat r,\omega)$ and
$w^\flat_\pm := \hat r^{1-i\sigma}w_\pm$. Conjugation by $\hat r^{1-i\sigma}$ replaces $\hat r\partial_{\hat r}$ by $\hat
r\partial_{\hat r}-1+i\sigma$, and $\hat r\mapsto-\hat r$ changes the sign of the first term of (5.12) only; so on
$\{\hat r>0\}$, with $\hat\rho := \hat r^{-1}$ ($\hat r\partial_{\hat r} = -\hat\rho\partial_{\hat\rho}$) and after
multiplication by $\hat\rho^2$,
$$\Big[\pm2i\hat\rho\big(\hat\rho\partial_{\hat\rho}-c-S_0\big)+\hat\rho^2P^{(0)}\big(0,\omega,\hat\rho\partial_{\hat
\rho},\partial_\omega\big)\Big]w^\flat_\pm = N_{\mathrm{tf}}(\pm1)w^\flat_\pm = 0,\tag{5.13}$$
with $N_{\mathrm{tf}}$ of I.C (4.1), on $\mathrm{tf}^\circ = \mathbb R^4_{\hat x}\setminus0$, $\hat x = \hat r\omega$. By
Lemma 5.7 with (5.10), $|w_\pm|\le C(1+\hat r)^{-1-\gamma_I-\mathrm{Im}\,\sigma}(\frac{\hat r}{1+\hat
r})^{\min(\gamma_{\mathrm{cf}}-\mathrm{Im}\,\sigma-1,0)-\epsilon}$, with the same bound for $(\hat r\partial_{\hat
r})^jZ^\alpha w_\pm$; as $|\hat r^{1-i\sigma}| = \hat r^{1+\mathrm{Im}\,\sigma} = (1+\hat
r)^{1+\mathrm{Im}\,\sigma}(\frac{\hat r}{1+\hat r})^{1+\mathrm{Im}\,\sigma}$ is conormal,
$$w^\flat_\pm\in\mathcal A^{\gamma_I,-\beta}(\mathrm{tf}),\qquad\beta := \max(-\gamma_{\mathrm{cf}},-1-\mathrm{Im}\,
\sigma)+\epsilon,\tag{5.14}$$
in the notation of I.C section 4.1 ($\rho_{\mathrm{sctf}} = (1+\hat r)^{-1}$, $\rho_{\mathrm{ztf}} = \hat r/(1+\hat r)$).
Take $\epsilon>0$ so small that $\beta<\beta_+$; this uses $-\gamma_{\mathrm{cf}}<\beta_+$ and
$-1-\mathrm{Im}\,\sigma<\beta_+$, the second hypothesis. Also $\beta>-\gamma_{\mathrm{cf}}>\beta_-$.

*tf-admissibility.* Fix $\beta^*\in(\beta,\beta_+)$, $q := 2-\beta^*\in(2-\beta_+,2-\beta_-)$, and in the spaces of I.C
section 4.3 take I.C's real parameter $\alpha_+$ there equal to 0 and orders $\mathsf r_\pm$ admissible as there whose
value near $R_{\mathrm{out}}$, the zero section over sctf, is below $\gamma_I-2$: this is allowed, admissibility imposing
only an upper bound at $R_{\mathrm{out}}$ (I.A Lemma 7.1, as used in the proof of I.A Theorem 7.2 (5)). Then
$w^\flat_+\in\mathcal X_{\mathrm{tf},0}$ and $w^\flat_-\in\mathcal X_{\mathrm{tf},\pi}$: near sctf, $\varphi_\infty
w^\flat_\pm\in H^{s,\mathsf r_\pm}_{\mathrm{sc}}$ for every $s$ by I.A Lemma 7.4 (a) with $a = \gamma_I$, which concerns
a neighbourhood of the boundary face of $\overline{\mathbb R^4}$ only (as in the converse of I.C Theorem 4.3 (5)); near
ztf, $(1-\varphi_\infty)w^\flat_\pm\in\mathcal A^{-\beta}\subset H^\infty_{b,q-2}$ as $q-2 = -\beta^*<-\beta$ (I.C Lemma
2.2 (f)); in between $w^\flat_\pm$ is smooth; and $N_{\mathrm{tf}}(\pm1)w^\flat_\pm = 0$. $\hat P_0$ is tf-admissible
with the weight $\alpha_++2 = -\gamma_{\mathrm{cf}}\in(\beta_-,\beta_+)$ (II.C Definition 2.7 (2)), so by I.C Corollary
5.2 (a), $N_{\mathrm{tf}}(e^{i\theta}):\mathcal X_{\mathrm{tf},\theta}\to\mathcal Y_{\mathrm{tf},\theta}$ is invertible
at $\theta = 0$ and $\theta = \pi$ for these $q$ and orders. Hence $w^\flat_\pm = 0$, and $\hat u = 0$ on $\{\hat
r\ne0\}$.

*Conclusion.* For $\psi\in C^\infty(\mathbb S^3;\mathbb C^N)$, $g := \langle\hat u,\psi\rangle_{\mathbb S^3}\in\mathcal
S'(\mathbb R)$ is supported in $\{0\}$, hence a finite sum $\sum_lc_l\delta^{(l)}$; so its inverse transform $\langle
u^\sharp,\psi\rangle_{\mathbb S^3}$ is a polynomial in $v$. It vanishes on $\{v<0\}$, so it vanishes identically. As
$\psi$ is arbitrary, $u^\sharp = 0$, and $u = 0$. $\square$

### 5.6 Proof of Proposition 5.1

For $k = 0$, Lemma 5.6 (b) gives the Fredholm property with index 0, and if also $\mathrm{Im}\,\sigma>-1-\beta_+$, Lemma
5.8 gives a trivial kernel, so (5.2) is invertible. Let $k\ge1$. By Lemma 5.6 (c) with $N^0(\sigma)u = 0$, the kernel on
$\mathcal X^{\mathsf s}_k$ is the kernel on $\mathcal X^{\mathsf s}$; and by Lemma 5.6 (c), $N^0(\sigma)(\mathcal
X^{\mathsf s}_k) = \mathcal Y^{\mathsf s-2}_k\cap N^0(\sigma)(\mathcal X^{\mathsf s})$, which is closed in $\mathcal
Y^{\mathsf s-2}_k$ since the inclusion $\mathcal Y^{\mathsf s-2}_k\hookrightarrow\mathcal Y^{\mathsf s-2}$ is continuous.
The map $\mathcal Y^{\mathsf s-2}_k\to\mathcal Y^{\mathsf s-2}/N^0(\sigma)(\mathcal X^{\mathsf s})$ has exactly this
kernel, and it is onto: its image is dense, as $C^\infty_c((\iota^+)^\circ)\subset\mathcal Y^{\mathsf s-2}_k$ is dense in
$\mathcal Y^{\mathsf s-2}$, and the quotient is finite-dimensional. So the cokernels at $k$ and at 0 have the same
dimension, (5.2) is Fredholm of index 0, and it is invertible when the operator at $k = 0$ is. $\square$

**Corollary 5.9.** On $\{\mathrm{Im}\,\sigma>\max(-\gamma_I,-1-\beta_+)\}$, $\sigma\mapsto N^0(\sigma)^{-1}\in\mathcal
L(\mathcal Y^{\mathsf s-2}_k,\mathcal X^{\mathsf s}_k)$ is holomorphic.

*Proof.* $N^0(\sigma) = N^0(\sigma_0)-2i(\sigma-\sigma_0)R^{-1}(R\partial_R+c+S_0)$ is affine in $\sigma$ with values in
$\mathcal L(\mathcal X^{\mathsf s}_k,\mathcal Y^{\mathsf s-2}_k)$ (the second term commutes with the $W_i$ up to terms of
its own class), and invertible there by Proposition 5.1; near each $\sigma_0$ the inverse is the Neumann series
$\sum_{j\ge0}((\sigma-\sigma_0)A)^jN^0(\sigma_0)^{-1}$, $A := 2iN^0(\sigma_0)^{-1}R^{-1}(R\partial_R+c+S_0)$, convergent
for $|\sigma-\sigma_0|\,\|A\|<1$. $\square$

## 6. Forward solutions of the $\iota^+$-normal operator ([Hin26c] section 10.1.4)

Throughout sections 6-8, $P_0$ is a stationary wave-type operator as in II.C Definition 1.1 and in the setting of II.E
section 1.1, with $\gamma_I$, $\gamma_{\mathrm{cf}} = -(\alpha_++2)$ and $(\beta_-,\beta_+)$ as in section 5.

### 6.1 Edge-b-edge spaces

On $[0,\infty]_\tau\times\iota^+$, $\tau = t_*^{-1}$, we write, as the source does, $\iota^+$ for the face
$\{0\}\times\iota^+$, $\mathscr I^+$ for $[0,\infty]\times(\iota^+\cap\mathscr I^+)$, and $\mathrm{cf} :=
[0,\infty]\times(\iota^+\cap K^+)$, with defining functions $\rho_+ = \tau/(1+\tau)$ (or $\tau$), $x_I$, and
$\rho_{\mathrm{cf}} = R/(1+R)$. The face $\mathrm{cf} = \{R = 0\} = \{r = 0\}$ is the timelike curve of the spatial
origin, at each time; it is not $K^+$. The *ebe-vector fields* ([Hin26c] Definition 10.11) are the b-vector fields of
$[0,\infty]\times\iota^+$ tangent to the fibres of $\mathscr I^+\to\mathbb S^3$ and $\mathrm{cf}\to[0,\infty]_\tau$; with
$\chi\in C^\infty_c([0,3))$ equal to 1 on $[0,2]$ they are spanned over $C^\infty$ by
$$\chi(R)R\partial_R,\ \chi(R)Z_a,\ \chi(R)R\tau\partial_\tau,\qquad\chi(v)v\partial_v,\ \chi(v)\sqrt vZ_a,\ \chi(v)\tau
\partial_\tau,\qquad v = R^{-1},\tag{6.1}$$
the source's (10.42) with the rotation fields $Z_a$ of $\mathbb S^3$ for $\partial_\omega$ (`iplusnorm5.py` N9 counts
them). By (1.5) and $N_{\iota^+}(P_0) = \tau^2N^0$ (Definition 1.1), $R^{-1}\tau\partial_\tau =
R^{-2}(R\tau\partial_\tau)$ and $R^{-1}R\partial_R$ near cf, and (1.6) near $\mathscr I^+$,
$$N_{\iota^+}(P_0)\in x_I^2\rho_+^2\rho_{\mathrm{cf}}^{-2}\mathrm{Diff}^2_{\mathrm{ebe}}([0,\infty]\times\iota^+),
\tag{6.2}$$
the source's (10.43). The spaces of the source's (10.45)-(10.48) are, at $n = 4$,
$$H^{(\mathsf s;k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b} := x_I^{2\gamma_I}\tau^{\gamma_+}\rho_{
\mathrm{cf}}^{\gamma_{\mathrm{cf}}}H^{(\mathsf s;k)}_{\mathrm{ebe};b}\big((0,\infty)_\tau\times\iota^+;\big|\tfrac{d\tau}
\tau\big|\mu_b\big),\tag{6.3}$$
the Sobolev spaces of the product structure of II.A section 6.2 (cells: unit intervals in $t = -\log_2\tau$ times the
cells $U_{2,jk\pm}$, $U_{3,jk\pm}$ of $\iota^+$), with $k$ further b-derivatives along $\tau\partial_\tau$ and the $W_i$
of section 4.1; $\mathsf s$ may be variable, the weights are constant, and all densities are b-densities. $\dot
H(\dots[0,\tau_0]\times\iota^+)$ denotes the subspace of distributions supported in $\{\tau\le\tau_0\}$; there
$\tau^{\gamma_+}$ and $\rho_+^{\gamma_+}$ give equivalent norms. As in the source (its footnote 99), $\tilde u\in
H^{\mathsf s,\gamma_{\mathrm{cf}}}_{e,\mathrm{loc}}((0,\infty)_\tau\times\{R<R_0\})$ means $\chi\tilde u\in H^{\mathsf
s,(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe}}$ for all $\chi\in C^\infty_c((0,\infty)\times\{R<R_0\})$, the
orders at $\mathscr I^+$ and $\iota^+$ being irrelevant there.

*Orders.* As in the source's (10.12), let $\mathsf s$ be admissible for $P_0$ with weights $\alpha_+$, 0 and margin 0
(II.C Definition 5.2). Its restriction to ${}^{e3b}S^*_{\iota^+}M$, extended to be invariant under $\tau$-dilations, is
an order on ${}^{\mathrm{ebe}}S^*((0,\infty)\times\iota^+)$, again written $\mathsf s$ (the identification of the phase
spaces over $\iota^+$ is [Hin26c] section 10.1.1, with (10.44) near cf). Its induced orders are those of section 1.3:
$\mathsf s_{0,b}$ at fibre infinity for bounded frequencies, and, for $\pm\mathrm{Re}\,\sigma\ge1$, $\mathsf
s_{0\hbar,c\hbar}$ at fibre infinity and $\mathsf b_\pm$ at sf.

**Lemma 6.1 ([Hin26c] (10.47) at $n = 4$; Plancherel).** For $u$ in (6.3), with $\mathcal M$ of (1.3) and $\mathbf o_\pm
:= (\mathsf s_{0\hbar,c\hbar};2\gamma_I,\gamma_{\mathrm{cf}},\gamma_{\mathrm{cf}};\mathsf b_\pm)$,
$$\|u\|^2_{H^{(\mathsf s;k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b}}\sim\int_{-1}^1\|(\mathcal Mu)(
\zeta-i\gamma_+)\|^2_{H^{(\mathsf s_{0,b};k),(2\gamma_I,\gamma_{\mathrm{cf}})}_{0,b;b}}d\zeta+\sum_\pm\int_{\pm[1,
\infty)}\|(\mathcal Mu)(\zeta-i\gamma_+)\|^2_{\mathbf o_\pm;k,+}d\zeta,\tag{6.4}$$
with $h = |\zeta|^{-1}$ in the norm (4.1).

*Proof.* This is the proof of II.A Lemma 6.2 with b-densities throughout (so without the shifts of II.A Lemma 6.1): (S9)
for the product structure, after writing $u = \tau^{\gamma_+}w$, for which $(\mathcal Mu)(\zeta-i\gamma_+) = (\mathcal
Mw)(\zeta)$ by (1.3); the weights $x_I^{2\gamma_I}\rho_{\mathrm{cf}}^{\gamma_{\mathrm{cf}}}$ are functions on $\iota^+$
and pass through, the weight at tf being that at cf (II.A Lemma 6.2's spaces). The b-field $\tau\partial_\tau$ becomes
multiplication by $i\sigma$ ($\mathcal M(\tau\partial_\tau u) = i\sigma\mathcal Mu$), bounded for $|\zeta|\le1$ and
giving the factors $|\zeta|^j = h^{-j}$ of $\|\cdot\|_{\mathbf o;k,+}$ for $|\zeta|\ge1$; the spatial b-fields commute
with $\mathcal M$. For $|\zeta|\ge1$ the spectral orders are $\mathsf s_{0\hbar,c\hbar}$ at fibre infinity and the
restriction of $\mathsf s$ at sf, which is $\mathsf b_\pm$ (section 1.3); for $|\zeta|\le1$ the spectral structure is the
0,b-structure, in which only the fibre order $\mathsf s_{0,b}$ enters. $\square$

### 6.2 The statement

**Proposition 6.2 ([Hin26c] Proposition 10.12 at $n = 4$).** Let $\mathsf s$ be as above, $\gamma_I<\frac32+\bar S$,
$\gamma_+<\min(\gamma_I,1+\beta_+)$, $\gamma_{\mathrm{cf}} := -(\alpha_++2)$, $\tau_0\in(0,1]$ and $k\in\mathbb N_0$.

(1) (*Existence.*) For every $f\in\dot H^{(\mathsf
s-1;k),(2\gamma_I+2,\gamma_++2,\gamma_{\mathrm{cf}}-2)}_{\mathrm{ebe};b}([0,\tau_0]\times\iota^+)$ there is a unique
$u\in\dot H^{(\mathsf s;k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b}([0,\tau_0]\times\iota^+)$ with
$$N_{\iota^+}(P_0)u = f,\qquad\|u\|_{H^{(\mathsf s;k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b}}\le C
\|f\|_{H^{(\mathsf s-1;k),(2\gamma_I+2,\gamma_++2,\gamma_{\mathrm{cf}}-2)}_{\mathrm{ebe};b}},\tag{6.5}$$
$C$ independent of $\tau_0$ and $f$. Uniqueness holds in $H^{(\mathsf
s;k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b}((0,\infty)\times\iota^+)$.

(2) (*Strong uniqueness.*) Let $\tilde u\in\mathcal D'((0,\infty)\times(\iota^+)^\circ)$ be supported in
$\{\tau\le\tau_0\}$, with $N_{\iota^+}(P_0)\tilde u = 0$ and $\tilde u\in H^{\mathsf
s,\gamma_{\mathrm{cf}}}_{e,\mathrm{loc}}((0,\infty)\times\{R<R_0\})$ for some $R_0>0$. Then $\tilde u = 0$.

The source states (1) with $f$ of order $\mathsf s-2$. Its proof gives $\mathsf s-1$ (its (10.50)), which is also what
Proposition 10.14 feeds it; the loss of one order is the loss at the radial sets over sf, where the semiclassical
estimates (3.4) and (4.4) lose one power of $h$ (section 9, (F7)). The conditions on $\gamma_+$ make the line
$\mathrm{Im}\,\sigma = -\gamma_+$ lie in the region of Proposition 5.1 where $N^0(\sigma)$ is invertible:
$-\gamma_+>-\gamma_I$ and $-\gamma_+>-1-\beta_+$.

### 6.3 Solutions near $\mathscr I^+$ at finite times

The proof of (2) needs control at $\mathscr I^+$ of solutions with compactly supported sources. Near $\mathscr I^+$ at
finite times we use $(t_*,x_I,\omega)$, $x_I = r^{-1/2}$, the edge fields $\partial_{t_*}$, $x_I\partial_{x_I}$,
$x_I\partial_\omega$, and the spaces $H^{s,2\gamma}_e$ with the b-density $|dt_*\frac{dx_I}{x_I}d\omega|$; on a finite
$t_*$-range these are the spaces (6.3) near $\mathscr I^+$ (the ebe-fields $\tau\partial_\tau$, $v\partial_v$, $\sqrt
vZ_a$ are combinations of the edge fields with bounded coefficients and conversely, and $(t_*/r)^{1/2}$ and $r^{-1/2}$
differ by a smooth positive factor). In II.E's notation, with the metric density $|dg|\sim
x_I^{-8}|dt_*\frac{dx_I}{x_I}d\omega|$, the weight $2\alpha$ there is $2(\alpha+2)$ here (II.A Lemma 6.1), so II.E's
threshold $\alpha<-\frac12+\bar p_1$, with $\bar p_1 = \bar S$ for $P_0$ and the operators below (II.C Definition 3.5;
[Hin26c] Remark 10.2), is $\gamma<\frac32+\bar S$.

**Lemma 6.3 (the extension's control at $\mathscr I^+$).** Let $s'\in\mathbb R$, $T\in\mathbb R$, and $g\in H^{s'-1}_c$
with support in $\{T\le t_*\le T+2,\ 2\le r\le3\}$. There is a unique $u$ on $\{t_*<T+2\}$, vanishing for $t_*<T$ and for
$r<1$, with $N_{\iota^+}(P_0)u = g$ and $u\in H^{s'}_{\mathrm{loc}}$; and for every $\chi\in C^\infty_c((-\infty,T+2))$
and $\gamma<\frac32+\bar S$, $\chi(t_*)u\in H^{s',2\gamma}_e$ near $\mathscr I^+$.

*Proof.* *Existence and support.* By (1.7) the principal symbol of $N_{\iota^+}(P_0)$ is the dual Minkowski metric, and
its coefficients are smooth on $\{r>0\}$. Let $\tilde N$ be a second-order operator on $\mathbb R^{1+4}$ with smooth
coefficients and Minkowski principal symbol, equal to $N_{\iota^+}(P_0)$ on $\{r>\frac12\}$. The forward solution $\tilde
u$ of $\tilde N\tilde u = g$ (vanishing for $t<T+2$, $t = t_*+r$ the Minkowski time) exists in $H^{s'}_{\mathrm{loc}}$
and is unique, by the standard theory of the Cauchy problem for hyperbolic operators of second order ([Hö85] chapter 23),
and it is supported in the Minkowski causal future of $\mathrm{supp}\,g$. Along a future causal curve $dt\ge|dr|$, so
both $t_* = t-r$ and $t+r = t_*+2r$ are non-decreasing. On $\mathrm{supp}\,g$, $t_*\ge T$ and $t_*+2r\ge T+4$; so a point
of $\mathrm{supp}\,\tilde u$ has $t_*\ge T$ and $t_*+2r\ge T+4$, and if $t_*<T+2$ then $r>1$. So $u := \tilde
u|_{\{t_*<T+2\}}$ vanishes for $r<1$, solves $N_{\iota^+}(P_0)u = g$, and does not depend on the choice of $\tilde N$;
any other such solution agrees with it by the same uniqueness.

*Control at $\mathscr I^+$.* By $t_*$-translation invariance we may take $T\ge1$. By the homogeneity of
$N_{\iota^+}(P_0)$ (section 1.2), $(D_\lambda u)(t_*,x) := u(t_*/\lambda,x/\lambda)$ satisfies $N_{\iota^+}(P_0)D_\lambda
u = \lambda^{-2}D_\lambda g$; $D_\lambda$ preserves the spaces $H^{s',2\gamma}_e$ near $\mathscr I^+$ at finite times (it
maps the edge fields to constant multiples of themselves and $x_I^{2\gamma}$ to $\lambda^{\gamma}x_I^{2\gamma}$). So we
may replace $g$ by $D_\lambda g$, supported in $\{T'\le t_*\le T'+2\lambda,\ 2\lambda\le r\le3\lambda\}$, $T' := \lambda
T\ge1$, with $\lambda\ge1$ to be chosen; by the support argument above, $u$ vanishes on $\{t_*<T'+2\lambda,\
r<\lambda\}$. Let $\psi\in C^\infty(\mathbb R)$ vanish on $(-\infty,\frac12]$ and equal 1 on $[1,\infty)$, $\tilde\psi\in
C^\infty(\mathbb R)$ equal 1 on $(-\infty,T'+2\lambda]$ and 0 on $[T'+2\lambda+1,\infty)$, and on $\Omega$ put
$$P_\lambda := P_0+\psi(r/\lambda)\tilde\psi(t_*)\big(N_{\iota^+}(P_0)-P_0\big).$$
The second term is supported in $\{r\ge\frac\lambda2,\ t_*\le T'+2\lambda+1\}$, near $\mathscr I^+$ at finite times.
There, by the terms (i)-(iv) in the proof of Lemma 1.2 (with $\tau$ bounded below), $N_{\iota^+}(P_0)-P_0\in
x_I^4\mathrm{Diff}^2_e$ with coefficients smooth in $(t_*,x_I,\omega)$, and the principal symbols differ by $\bar
G-G_0\in x_I^2\cdot x_I^2P^{[2]}_e$ (II.C Definition 3.1, Remark (a)). As $x_I^2\le2/\lambda$ on the support and
$\ell_I\le\frac12$, $P_\lambda$ is weakly admissible relative to $P_0$ (II.C Definition 3.3, with $p_0 = \tilde p_1 = 0$,
$p_1 = S|_{\partial X}$ as for $P_0$) of class $((d_0;0),(2\ell_I,\ell_+,\ell_K))$ for every $d_0$, with
$\|P_\lambda-P_0\|\le C_{d_0}\lambda^{-(1-\ell_I)}$, and its metric is in $\mathcal G$ with $\|g_\lambda-g_0\|\le
C\lambda^{-(1-\ell_I)}$. Fix $\lambda$ so large that $P_\lambda$ satisfies the smallness hypotheses of II.E section 1.1
(in particular II.C Lemma 3.2 gives the time function $t^\flat$ for $g_\lambda$). By II.E Proposition 3.4 (ii), on the
slab $\Omega' := \Omega_{T',T'+2\lambda}$, with the constant (slab) order $s'$ and $\alpha := \gamma-2<-\frac12+\bar S$,
the forward solution $u_\lambda\in H^{s',2\alpha}(\Omega')^{\bullet,-}$ of $P_\lambda u_\lambda = D_\lambda g$ exists
(the source lies in every weighted space, being compactly supported in $M^\circ$). On $\{t_*<T'+2\lambda\}$, $u$ vanishes
where $P_\lambda\ne N_{\iota^+}(P_0)$ ($r<\lambda$), so $P_\lambda u = D_\lambda g$ there; $u-u_\lambda$ solves
$P_\lambda(u-u_\lambda) = 0$ on $\Omega'^\circ$, vanishes for $t^\flat<T'$, and lies in $H^{\min(s',0)}_{\mathrm{loc}}$;
$dt^\flat$ is timelike for $g_\lambda$ and, for each point $p$, the set of points of $\{t^\flat\ge T'\}$ in the causal
past of $p$ is compact, so $u = u_\lambda$ by the domain-of-dependence uniqueness for distributional solutions of
hyperbolic operators with smooth coefficients ([Hö85] chapter 23). Hence $\chi u\in H^{s',2\gamma}_e$ near $\mathscr I^+$
for $\chi$ supported in $t_*<T'+2\lambda$, and undoing $D_\lambda$ gives the claim. $\square$

### 6.4 Proof of Proposition 6.2 (1)

*The equation on the Mellin side.* By Definition 1.1, $N_{\iota^+}(P_0)u = f$ is $N^0u = \tau^{-2}f$, and $\tau^{-2}f$
lies in $H^{(\mathsf s-1;k),(2\gamma_I+2,\gamma_+,\gamma_{\mathrm{cf}}-2)}_{\mathrm{ebe};b}$ with the same norm as $f$ in
the space of (6.5), the $\tau$-weight being $\tau^{\gamma_+}$. For $\sigma$ on the line $\mathrm{Im}\,\sigma =
-\gamma_+$, which lies in $\{\mathrm{Im}\,\sigma>\max(-\gamma_I,-1-\beta_+)\}$, define
$$(\mathcal Mu)(\sigma) := N^0(\sigma)^{-1}\mathcal M(\tau^{-2}f)(\sigma),\tag{6.6}$$
which is well defined by Corollary 5.9.

*Bounds on the line.* Write $\sigma = \zeta-i\gamma_+$. (i) For $|\zeta|\ge h_0^{-1}$ put $h := |\zeta|^{-1}$ and $z :=
h\sigma = \pm1-ih\gamma_+\in\mathcal Z^\pm_h$. By Proposition 4.3 (the second estimate of (4.4)) and $P_{\iota,h,z} =
h^2N^0(\sigma)$,
$$\|(\mathcal Mu)(\sigma)\|_{\mathbf o_\pm;k,+}\le C_k\|h^2\mathcal M(\tau^{-2}f)(\sigma)\|_{Y_{\mathbf o_\pm};k,+} = C_k
\|\mathcal M(\tau^{-2}f)(\sigma)\|_{(\mathsf s_{0\hbar,c\hbar}-2;2\gamma_I+2,\gamma_{\mathrm{cf}}-2,\gamma_{
\mathrm{cf}}-2;\mathsf b_\pm-1);k,+},$$
since multiplication by $h^2 = \rho_{\mathrm{tf}}^2\rho_{\mathrm{sf}}^2$ lowers the tf- and sf-orders by 2, and
$Y_{\mathbf o} = H^{(\mathsf s'-2;2\gamma_I+2,\gamma_{\mathrm{cf}}-2,\gamma_{\mathrm{cf}};\mathsf b+1)}$ (3.3). The last
norm is at most $C$ times the norm with the fibre order $\mathsf s_{0\hbar,c\hbar}-1$, which is the spectral norm of
Lemma 6.1 for the order $\mathsf s-1$ and the weights $(2\gamma_I+2,\gamma_+,\gamma_{\mathrm{cf}}-2)$ of $\tau^{-2}f$:
its sf-order is $\mathsf b_\pm-1$, its tf-order equals its cf-weight $\gamma_{\mathrm{cf}}-2$. (ii) For $|\zeta|\le
h_0^{-1}$, $\sigma\mapsto N^0(\sigma)^{-1}\in\mathcal L(\mathcal Y^{\mathsf s_{0,b}-2}_k,\mathcal X^{\mathsf s_{0,b}}_k)$
is continuous (Corollary 5.9), hence bounded on this compact segment; for $1\le|\zeta|\le h_0^{-1}$ the norms
$\|\cdot\|_{\mathbf o;k,+}$ at $h = |\zeta|^{-1}\in[h_0,1]$ are equivalent to the 0,b-norms uniformly (section 2.1), and
$\mathcal Y^{\mathsf s_{0,b}-2}_k\supset H^{(\mathsf s_{0,b}-1;k),(2\gamma_I+2,\gamma_{\mathrm{cf}}-2)}_{0,b;b}$
continuously. Squaring, integrating in $\zeta$ and using (6.4) for $u$ (at the order $\mathsf s$) and for $\tau^{-2}f$
(at the order $\mathsf s-1$): the function $u$ with Mellin transform (6.6) on the line lies in $H^{(\mathsf
s;k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b}((0,\infty)\times\iota^+)$, with (6.5). Since $\mathcal
M(N^0u)(\sigma) = N^0(\sigma)(\mathcal Mu)(\sigma) = \mathcal M(\tau^{-2}f)(\sigma)$ on the line (by (1.6) for $u\in
C^\infty_c$, and by continuity), $N^0u = \tau^{-2}f$. Conversely, if $N_{\iota^+}(P_0)u = 0$ with $u$ in this space, then
$N^0(\sigma)(\mathcal Mu)(\sigma) = 0$ for almost every $\sigma$ on the line, so $\mathcal Mu = 0$ and $u = 0$: this is
the uniqueness.

*Support (Paley-Wiener).* The solution map $f\mapsto u$ is bounded by (6.5). The functions $f\in
C^\infty_c((0,\tau_0)\times(\iota^+)^\circ)$ are dense in the space of (6.5) on $[0,\tau_0]\times\iota^+$: the dilations
$f\mapsto f(\lambda\cdot,\cdot)$, $\lambda\downarrow1$, are translations in $t$, strongly continuous on (6.3) as $\mathsf
s$ is dilation-invariant, and move the support into $\{\tau\le\tau_0/\lambda\}$; then multiply approximations in
$C^\infty_c((0,\infty)\times(\iota^+)^\circ)$ by a cut-off in $\tau$ equal to 1 on $[0,\tau_0/\lambda]$ and supported in
$[0,\tau_0)$. As $\{\mathrm{supp}\,u\subset\{\tau\le\tau_0\}\}$ is a closed condition, it suffices to take $f\in
C^\infty_c$, $\mathrm{supp}\,f\subset[\tau_1,\tau_-]\times K$ with $0<\tau_1<\tau_-<\tau_0$, $K\subset(\iota^+)^\circ$
compact. Then $F(\sigma) := \mathcal M(\tau^{-2}f)(\sigma)\in C^\infty_c(K)$ is entire, and for
$\mathrm{Im}\,\sigma\ge-\gamma_+$ and $L\in\mathbb N_0$, as $\mathcal M((1+(\tau D_\tau)^2)^Lg) = (1+\sigma^2)^L\mathcal
Mg$ and $|\tau^{-i\sigma}| = \tau^{\mathrm{Im}\,\sigma}\le\max(\tau_-^{\mathrm{Im}\,\sigma},\tau_1^{-\gamma_+})$ on the
support,
$$\|F(\sigma)\|_{H^N}\le C_{N,L}|1+\sigma^2|^{-L}\max(\tau_-^{\mathrm{Im}\,\sigma},\tau_1^{-\gamma_+}).$$
Let $\phi\in C^\infty_c((\iota^+)^\circ)$. By Corollary 5.9, $\sigma\mapsto\langle(\mathcal Mu)(\sigma),\phi\rangle$,
defined by (6.6) with $N^0(\sigma)^{-1}$, is holomorphic on
$\{\mathrm{Im}\,\sigma>\max(-\gamma_I,-1-\beta_+)\}\supset\{\mathrm{Im}\,\sigma\ge-\gamma_+\}$. There is $N_1$ with
$$|\langle(\mathcal Mu)(\sigma),\phi\rangle|\le C\langle\sigma\rangle^{N_1}\|F(\sigma)\|_{H^{N_1}},\qquad\mathrm{Im}\,
\sigma\ge-\gamma_+:$$
for $|\sigma|\ge\sqrt2h_0^{-1}$, $\sigma = h^{-1}z$ with $z$ in one of the families (3.2) (section 3.1), and (3.4) bounds
$(\mathcal Mu)(\sigma)$ in $H^{\mathbf o}$ by $h^2F(\sigma)$ in $Y_{\mathbf o}$; on compact subsets of $(\iota^+)^\circ$
the semiclassical norms of $H^{\mathbf o}$ and $Y_{\mathbf o}$ are bounded above and below by standard Sobolev norms
times powers of $h$ (the orders are bounded, and the weights are bounded above and below there), and $\langle(\mathcal
Mu)(\sigma),\phi\rangle$ only sees $\mathrm{supp}\,\phi$; for $|\sigma|\le\sqrt2h_0^{-1}$,
$\mathrm{Im}\,\sigma\ge-\gamma_+$, a compact set, use the continuity of Corollary 5.9. Fix $L$ with $N_1-2L<-1$. By
Mellin inversion, $\langle u(\tau,\cdot),\phi\rangle = \frac1{2\pi}\int_{\mathrm{Im}\,\sigma =
-\gamma}\tau^{i\sigma}\langle(\mathcal Mu)(\sigma),\phi\rangle d\sigma$ for $\gamma = \gamma_+$; the integrand is
holomorphic on $\{\mathrm{Im}\,\sigma\ge-\gamma_+\}$ and $O(\langle\sigma\rangle^{N_1-2L})$ uniformly on
$\{|\mathrm{Re}\,\sigma|\ge2\}$ in each horizontal strip ($|1+\sigma^2|\ge\frac12|\sigma|^2$ there), so the contour may
be moved to $\mathrm{Im}\,\sigma = \gamma$ for every $\gamma\ge2$. There $|\tau^{i\sigma}| = \tau^{-\gamma}$, and for
$\tau>\tau_-$ the integral is at most $C(\tau_-/\tau)^\gamma\to0$ as $\gamma\to\infty$. So $\langle
u(\tau,\cdot),\phi\rangle = 0$ for $\tau>\tau_-$, for every $\phi$: $\mathrm{supp}\,u\subset\{\tau\le\tau_-\}$. $\square$

### 6.5 A support lemma, and the proof of Proposition 6.2 (2)

*Fixed-$\sigma$ transforms.* Let $m\in\mathbb Z$ and $v\in H^{m,(a,b,c)}_{\mathrm{ebe}}$ with $\tau$-support in a compact
$[\tau_1,\tau_2]\subset(0,\infty)$. Then $\sigma\mapsto(\mathcal Mv)(\sigma)$ is entire with values in
$H^{m,(a,c)}_{0,b}(\iota^+)$ and
$$\|(\mathcal Mv)(\sigma)\|_{H^{m,(a,c)}_{0,b}}\le C\langle\sigma\rangle^{|m|}\max(\tau_1^{\mathrm{Im}\,\sigma},\tau_2^{
\mathrm{Im}\,\sigma})\|v\|_{H^{m,(a,b,c)}_{\mathrm{ebe}}}.\tag{6.7}$$
Indeed, the spatial fields among (6.1) ($R\partial_R$, $Z_a$ near cf; $v\partial_v$, $\sqrt vZ_a$ near $\mathscr I^+$)
are the 0,b-fields of $\iota^+$ at bounded frequency and commute with $\mathcal M$, while $\tau\partial_\tau$ and
$R\tau\partial_\tau$ become $i\sigma$ and $i\sigma R$; for $m\ge0$, (6.7) without the factor $\langle\sigma\rangle^{|m|}$
follows from the Cauchy-Schwarz inequality in $\tau$ on $[\tau_1,\tau_2]$; for $m<0$ write $v =
\sum_{|\alpha|\le|m|}V^\alpha v_\alpha$ with $V^\alpha$ products of the fields (6.1) and $v_\alpha\in H^{0,(a,b,c)}$
supported in a slightly larger compact $\tau$-interval, $\sum\|v_\alpha\|\le C\|v\|$; the weights commute with the fields
up to bounded factors.

*Comparison of norms at fixed $h$.* For constant orders and $h\in(0,1]$, the norms of $H^{(m;a,c,l;\mathsf
b)}_{(0\hbar,c\hbar,h)}$ and of $H^{m,(a,c)}_{0,b}$ are equivalent with constants $Ch^{-K}$ and $C^{-1}h^K$, $K$
depending on $|m|$, $|a|$, $|c|$, $|l|$ and $\sup|\mathsf b|$: the cells of the structure at parameter $h$ are those of
the 0,b-structure rescaled by factors in $[h,1]$ (the scalings $(1+\rho_K|\sigma|)^{-1}$, $\langle\sigma\rangle^{-1}$,
$x_I\langle\sigma\rangle^{-1}$ of II.A section 6.2 against $1$, $1$, $x_I$), and the weights
$\rho_{\mathrm{cf}}^c\rho_{\mathrm{tf}}^l\rho_{\mathrm{sf}}^{\mathsf b}$ differ from $\rho_K^c$ by factors in
$[h^K,h^{-K}]$, as $\rho_{\mathrm{tf}} = h+\rho_K$, $\rho_{\mathrm{sf}} = h/(h+\rho_K)$, $\rho_{\mathrm{cf}} =
\rho_K/(h+\rho_K)$ (section 2.1).

**Lemma 6.4 (support).** Let $m\in\mathbb Z$, $T>0$, and let $w\in
H^{m,(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe}}$ have $\tau$-support in a compact subset of $(0,\infty)$,
with $N_{\iota^+}(P_0)w\in H^{m-1,(2\gamma_I+2,\gamma_++2,\gamma_{\mathrm{cf}}-2)}_{\mathrm{ebe}}$ supported in $\{t_*\ge
T\}$. Then $w$ is supported in $\{t_*\ge T\}$.

*Proof.* Let $f := N_{\iota^+}(P_0)w$, so that $N^0w = \tau^{-2}f$, and let
$\mathrm{supp}\,w\subset\{\tau_1\le\tau\le\tau_2\}$. $W(\sigma) := (\mathcal Mw)(\sigma)$ and $F(\sigma) := \mathcal
M(\tau^{-2}f)(\sigma)$ are entire, $N^0(\sigma)W(\sigma) = F(\sigma)$ by (1.6), and by (6.7), as $\tau\le T^{-1}$ on
$\mathrm{supp}\,f$,
$$\|F(\sigma)\|_{H^{m-1,(2\gamma_I+2,\gamma_{\mathrm{cf}}-2)}_{0,b}}\le C\langle\sigma\rangle^{|m-1|}T^{-\mathrm{Im}\,
\sigma},\qquad\mathrm{Im}\,\sigma\ge0.$$
For $\mathrm{Im}\,\sigma\ge-\gamma_+$, $W(\sigma)\in\mathcal X^m$, and Proposition 5.1 (invertibility on $\mathcal X^m$;
any order) gives $W(\sigma) = N^0(\sigma)^{-1}F(\sigma)$. Let $\phi\in C^\infty_c((\iota^+)^\circ)$. For
$|\sigma|\ge\sqrt2h_0^{-1}$, $\mathrm{Im}\,\sigma\ge0$, write $\sigma = h^{-1}z$ with $z$ in one of the families (3.2)
(section 3.1). At this fixed $h$, $W(\sigma)\in H^{\mathbf o}$ with the fibre order $m$ (any order is allowed there) and
the sf-orders of section 3.1, and (3.4) gives $\|W(\sigma)\|_{\mathbf o}\le C\|h^2F(\sigma)\|_{Y_{\mathbf o}}$; with the
comparison of norms and the compact support of $\phi$ in $(\iota^+)^\circ$, $|\langle W(\sigma),\phi\rangle|\le
Ch^{-K}\|F(\sigma)\|_{H^{m-1,(2\gamma_I+2,\gamma_{\mathrm{cf}}-2)}_{0,b}}$. On the compact set
$\{|\sigma|\le\sqrt2h_0^{-1},\ \mathrm{Im}\,\sigma\ge0\}$ use the continuity of Corollary 5.9. Hence
$$|\langle W(\sigma),\phi\rangle|\le C\langle\sigma\rangle^{N_1}T^{-\mathrm{Im}\,\sigma},\qquad\mathrm{Im}\,\sigma\ge0.$$
In $t := -\log\tau$, the Mellin transform (1.3) of the compactly supported distribution $\tau\mapsto\langle
w(\tau,\cdot),\phi\rangle$ is its Fourier transform $\int e^{i\sigma t}\langle w,\phi\rangle\,dt$, as $\tau^{-i\sigma} =
e^{i\sigma t}$; it is entire and, the support lying in $t\in[-\log\tau_2,-\log\tau_1]$, bounded by
$C\langle\sigma\rangle^{N_1}e^{(\log\tau_1)\mathrm{Im}\,\sigma}$ for $\mathrm{Im}\,\sigma\le0$ ($|e^{i\sigma t}| =
e^{-t\,\mathrm{Im}\,\sigma}$, largest at $t = -\log\tau_1$). With the last bound for $\mathrm{Im}\,\sigma\ge0$ it is
bounded by $C\langle\sigma\rangle^{N_1}e^{H(\mathrm{Im}\,\sigma)}$, $H(\eta) := \sup\{-t\eta:t\in[\log T,-\log\tau_1]\}$;
this is [Hö83]'s supporting function of that interval for the transform $\sigma\mapsto\hat u(-\sigma)$, $\hat u(\zeta) =
\int e^{-it\zeta}u\,dt$. By the Paley-Wiener-Schwartz theorem ([Hö83] Theorem 7.3.1) the support lies in $\{t\ge\log T\}
= \{t_*\ge T\}$. As $\phi$ is arbitrary, $\mathrm{supp}\,w\subset\{t_*\ge T\}$. $\square$

*Proof of Proposition 6.2 (2).* The proof uses only the integer order $s'' := \lfloor\inf\mathsf s\rfloor$, and not part
(1).

*Reduction.* Work in $(t_*,r,\omega)$, in which $N := N_{\iota^+}(P_0)$ is (1.7): translation-invariant in $t_*$ and
homogeneous under $D_\lambda$ (section 6.3). $\tilde u$ is a distribution on $\{t_*>0,r>0\}$, supported in
$\{t_*\ge\tau_0^{-1}\}$, and on $\{r<R_0t_*\}$ it lies locally in the edge space of order $s''$ with weight
$\gamma_{\mathrm{cf}}$ at $r = 0$. Pick $\lambda\ge1$ with $\lambda\tau_0^{-1}\ge4R_0^{-1}$, replace $\tilde u$ by
$D_\lambda\tilde u$ (same properties with $\tau_0/\lambda$ for $\tau_0$, as $\{R<R_0\}$ is $D_\lambda$-invariant), and
then translate $t_*$ by $1-\lambda\tau_0^{-1}$. The new $\tilde u$ solves $N\tilde u = 0$ on $\{r>0\}$, vanishes for
$t_*<1$, and on $\{t_*\ge1,\ r<4\}$, which lies in the old $\{R<R_0\}$ because the old $t_*$ is
$\ge\lambda\tau_0^{-1}\ge4R_0^{-1}$ there, it is locally of edge order $s''$ with weight $\gamma_{\mathrm{cf}}$ at $r =
0$. We show $\tilde u = 0$ on $\{t_*<2\}$. The same argument after a further translation by 1 (the properties persist,
the region $\{t_*\ge1,r<4\}$ moving into itself) then gives $\tilde u = 0$ on $\{t_*<j\}$ for every $j$, so $\tilde u =
0$.

*The extension.* Let $\chi_{t_*}\in C^\infty(\mathbb R)$ equal 1 near $(-\infty,2]$ and 0 near $[3,\infty)$, $\chi_r\in
C^\infty_c([0,3))$ equal 1 near $[0,2]$, and $\chi^\flat_{t_*}\in C^\infty(\mathbb R)$ equal 1 on $(-\infty,2]$ and
supported in $\{\chi_{t_*} = 1\}$. $g := \chi_{t_*}[N,\chi_r]\tilde u\in H^{s''-1}_c$ is supported in $\{1\le t_*\le3,\
2\le r\le3\}$; let $u_{\mathrm{ext}}$ be the solution of $Nu_{\mathrm{ext}} = g$ on $\{t_*<3\}$ of Lemma 6.3 ($T = 1$,
$s' = s''$), which vanishes where $t_*+2r<5$ (the support argument there) and satisfies
$\chi^\flat_{t_*}u_{\mathrm{ext}}\in H^{s'',2\gamma_I}_e$ near $\mathscr I^+$. Put
$$w := \chi_{t_*}\chi_r\tilde u-\chi^\flat_{t_*}u_{\mathrm{ext}},\qquad f := Nw = [N,\chi_{t_*}](\chi_r\tilde u)+
\chi_{t_*}(1-\chi^\flat_{t_*})[N,\chi_r]\tilde u-[N,\chi^\flat_{t_*}]u_{\mathrm{ext}}.$$
$w$ is supported in $\{1\le t_*\le3\}$, i.e. $\tau\in[\frac13,1]$, and lies in
$H^{s'',(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe}}$ (any $\tau$-weight): near $r = 0$ it is
$\chi_{t_*}\tilde u$, near $\mathscr I^+$ it is $-\chi^\flat_{t_*}u_{\mathrm{ext}}$, and in between it is in
$H^{s''}_{\mathrm{loc}}$. Each term of $f$ is supported in $\{2\le t_*\le3\}$, i.e. $\tau\in[\frac13,\frac12]$, and $f\in
H^{s''-1,(2\gamma_I+2,\gamma_+,\gamma_{\mathrm{cf}}-2)}_{\mathrm{ebe}}$ by (6.2) (the commutators are first-order
ebe-operators with the weights of $N$, or better).

*Support.* By Lemma 6.4 with $m = s''$ and $T = 2$, $w$ is supported in $\{t_*\ge2\}$.

*Conclusion.* On $\{t_*<2\}$, $\chi_{t_*} = \chi^\flat_{t_*} = 1$, so $\chi_r\tilde u = u_{\mathrm{ext}}$ there, and
$u_{\mathrm{ext}} = 0$ where $t_*+2r<5$, which contains $\{t_*<2,\ r<\frac32\}$. Hence $\tilde u = 0$ on $\{t_*<2,\
r<\frac32\}$. Let $p\in\{t_*<2\}$ with $r(p)\ge\frac32$. As $t_*$ is non-decreasing along future causal curves, the
causal past $J^-(p)$ lies in $\{t_*\le t_*(p)\}$, where $\tilde u = 0$ on $\{r<\frac32\}\cup\{t_*<1\}$; and
$J^-(p)\cap\{t_*\ge1\}$ is compact, as there $r = t-t_*\le t(p)-1$. On $\{r>1\}$, $N$ has smooth coefficients and
Minkowski principal symbol, and the domain-of-dependence uniqueness for distributional solutions ([Hö85] chapter 23),
with the Minkowski time $t$, on a neighbourhood of $J^-(p)\cap\{t_*\ge1,\ r\ge\frac32\}$ in $\{r>1\}$ whose remaining
boundary lies where $\tilde u = 0$, gives $\tilde u = 0$ near $p$. So $\tilde u = 0$ on $\{t_*<2\}$. $\square$

The source proves this part by solving $Nw' = f$ with part (1) and comparing $w$ with $w'$ by uniqueness. That needs $f$
in the space of part (1), with the variable admissible order $\mathsf s$ near $\mathscr I^+$, where the extension
$u_{\mathrm{ext}}$ is controlled only at a constant order; Lemma 6.4 avoids this, using only Proposition 5.1 at a
constant order and the high-energy estimate (3.4).

## 7. The modified operator $P_+$ ([Hin26c] section 10.2)

### 7.1 Definition and structure

**Definition 7.1 ([Hin26c] Definition 10.13 at $n = 4$).** Let $\chi\in C^\infty_c([0,2))$, $0\le\chi\le1$, equal 1 near
$[0,1]$, and write $\chi = \chi(R)$. Let $T_+ := \max(2,2r_0)$. On $\{t_*>T_+\}\times\iota^+$, i.e. on
$(0,T_+^{-1})_\tau\times\iota^+$,
$$P_+ := \chi N_{\iota^+}(P_0)+(1-\chi)P_0.$$
On $\mathrm{supp}(1-\chi)$, $R\ge1$, so $r = Rt_*>T_+\ge2r_0$ lies in the domain of $P_0$ (II.C Definition 1.1);
$N_{\iota^+}(P_0)$ is defined on $\{r>0\}$ by (1.7). (The source takes $\{t_*>1\}$; $T_+$ only keeps $P_0$'s domain in
view.)

**Lemma 7.2.** (a) $P_+\in x_I^2\tau^2\rho_{\mathrm{cf}}^{-2}\mathrm{Diff}^2_{\mathrm{ebe}}([0,T_+^{-1})\times\iota^+)$.
(b) $P_+-N_{\iota^+}(P_0)\in x_I^2\tau^3\rho_{\mathrm{cf}}^{-2}\mathrm{Diff}^2_{\mathrm{ebe}}$: $N_{\iota^+}(P_0)$ is the
normal operator of $P_+$ at $\tau = 0$ ([Hin26c] (10.51)). (c) $P_+$ is principally scalar with principal symbol $G_\chi
:= \chi\bar G+(1-\chi)G_0$, the dual metric function of $g_\chi^{-1} := \chi\bar g^{-1}+(1-\chi)g_0^{-1}$, which is
Lorentzian on $\{\tau<\tau_1\}$ for some $\tau_1>0$; $dt_*$ is past causal for $g_\chi$; and $g_\chi = \bar g$ on
$\{R\le1\}$.

*Proof.* (a) On $\{R<1\}$, $P_+ = N_{\iota^+}(P_0)$ and (6.2) applies. On $\{R>\frac12\}$, $(\tau,R,\omega)\mapsto(t_* =
\tau^{-1},r = R\tau^{-1},\omega)$ identifies $[0,T_+^{-1})\times\iota^+$ with a neighbourhood of
$\iota^+\cap\{R>\frac12\}$ in $M$, away from $K^+$; there the ebe-fields (6.1) are the e3b-fields (II.A section 2.4:
b-fields over $(\iota^+)^\circ$, eb-fields near $\iota^+\cap\mathscr I^+$), $\rho_+\sim\tau$, and $P_0\in
x_I^2\rho_+^2\mathrm{Diff}^2_{e3b}$ (II.C Lemma 1.4 (b)), as is $N_{\iota^+}(P_0)$ by Lemma 1.2. (b)
$P_+-N_{\iota^+}(P_0) = (1-\chi)(P_0-N_{\iota^+}(P_0))$, supported in $\{R\ge1\}$, and (1.9). (c) The principal symbols
are $\bar G\,\mathrm{Id}$ for $N_{\iota^+}(P_0)$ ((1.7)-(1.8)) and $G_0\,\mathrm{Id}$ for $P_0$ (II.C Definition 1.1). By
II.C Definition 3.1, Remark (a), $g_0-\bar g\in x_I^{-2}\rho_+^{-2}C^{\infty,(2,2,0)}$, so on
$\mathrm{supp}\,\chi\cap\mathrm{supp}(1-\chi)\subset\{1\le R\le2\}$, near $\iota^+$,
$x_I^2\rho_+^2(g_\chi^{-1}-g_0^{-1})$ (as a section of $S^2\,{}^{e3b}TM$) is $O(\rho_+^2)$, and the convex combination is
Lorentzian for $\tau$ small (II.C Definition 3.1, Remark (b)). $\bar G(dt_*) = 0$ ($dt_*$ is null for $\bar g$, section
1.2) and $G_0(dt_*)<0$ with $dt_*$ past directed on $\{r\ge T_+\}$ (II.B Lemma 1.1, [Hin26c] Lemma 4.4), so
$G_\chi(dt_*)\le0$, past directed. $\square$

### 7.2 Orders

Let $\mathsf s$ be admissible for $P_0$ with weights $\alpha_+$, 0 and margin 0 (II.C Definition 5.2), and let it meet
the lower thresholds (4) and (6) of II.C Definition 2.4 with margin 1. (An order admissible with margin 1 does, and so
does its sum with 1, which has margin 0 at the upper threshold (5); section 8 uses both.) Let $\mathsf s_I$ be the
$\tau$-dilation-invariant extension of $\mathsf s|_{{}^{e3b}S^*_{\iota^+}M}$ (section 6.1), and
$$\mathsf s' := \chi(R)\mathsf s_I+(1-\chi(R))\mathsf s\quad\text{on }{}^{\mathrm{ebe}}S^*([0,T_+^{-1})\times\iota^+).
\tag{7.1}$$
Fix $\eta_1>0$ so small that $\mathsf s_\flat := \mathsf s-1-\eta_1$ is admissible with weights $\alpha_+$, 0 and margin
0: the threshold conditions of II.C Definition 2.4 (4)-(6) are strict inequalities for the constant values of $\mathsf s$
near finitely many radial sets, $\mathsf s$ meets the lower ones (4), (6) with margin 1, and lowering $\mathsf s$ only
helps at the upper one (5); (1)-(3) and II.C Proposition 5.1 (2)-(5) are unaffected by subtracting a constant. Let
$\mathsf s_{\flat,I}$ be its $\tau$-dilation-invariant extension.

**Lemma 7.3.** There is $\tau_1\in(0,T_+^{-1})$ such that on $\{\tau\le\tau_1\}$:

(a) $\mathsf s' = \mathsf s_I$ on $\{R\le10\}$, $\mathsf s' = \mathsf s$ on $\{R\ge1\}$, and $\mathsf
s_{\flat,I}+1\le\mathsf s'$.

(b) $\mathsf s'$ is non-increasing along the future null-bicharacteristic flow of every principally scalar operator whose
dual metric is $g^{-1} = g_\chi^{-1}+k$ with $k$ supported in $\{\tau\le\tau_1\}\cap\{R\ge1\}$ and small in the norm of
II.C Proposition 5.1 (2), or with $k = 0$.

(c) $\mathsf s'$ is constant near the radial sets $R_{\mathscr I^+,\mathrm{in},+}$, $R_{\mathscr I^+,\mathrm{out}}$ (over
$\iota^+\cap\mathscr I^+$; II.B Definition 7.1) and near $R_{\mathrm{cf},\mathrm{in}}$, $R_{\mathrm{cf},\mathrm{out}}$,
the $\tau$-invariant extensions over cf of $\partial R_{\partial K^+,\mathrm{in}}$, $\partial R_{\partial
K^+,\mathrm{out}}$ under the identification (10.44) of the source (${}^{\mathrm{ebe}}T^*_{\iota^+\cap\mathrm{cf}} =
{}^{3b}T^*_{\iota^+\cap K^+}M_0$), and satisfies there the thresholds of II.C Definition 2.4 (5)-(6) with
$\alpha_{\mathrm{sf}} = \alpha_+$, $\alpha_K = 0$, margin 0. The same holds for $\mathsf s_{\flat,I}$ in place of
$\mathsf s'$ near $R_{\mathrm{cf},\mathrm{in/out}}$ and $R_{\mathscr I^+,\mathrm{in},+}$.

*Proof.* (a) By II.C Proposition 5.1 (3), $\mathsf s$ is invariant under $(t_*,r,\omega)\mapsto(\lambda t_*,\lambda
r,\omega)$ on a neighbourhood of $\iota^+\cap\{R\in[1,10]\}$, which contains $\{\tau\le\tau_1,\ R\in[1,10]\}$ for
$\tau_1$ small; there $\mathsf s = \mathsf s_I$, which gives the first two claims (on $\{1\le R\le2\}$, $\mathsf s' =
\chi\mathsf s+(1-\chi)\mathsf s$). For the third: on $\{R\le10\}$, $\mathsf s_{\flat,I}+1 = \mathsf s_I-\eta_1<\mathsf
s_I = \mathsf s'$; on $\{R\ge1\}$, $\mathsf s' = \mathsf s$, and $\mathsf s$ is uniformly continuous on the compact set
${}^{\mathrm{ebe}}S^*_{\{\tau\le T_+^{-1}/2,\,R\ge1\}}$ (where it is a smooth function on ${}^{e3b}S^*M$) and equals
$\mathsf s_I$ at $\tau = 0$, so $|\mathsf s-\mathsf s_I|\le\eta_1$ there for $\tau_1$ small, and $\mathsf s_{\flat,I}+1 =
\mathsf s_I-\eta_1\le\mathsf s$.

(b) On $\{R\le1\}$ the metric is $\bar g$ (also for $g$, as $k$ vanishes there) and $\mathsf s' = \mathsf s_I$. $\bar G$
and $\mathsf s_I$ are invariant under $\tau$-dilations, so the rescaled Hamilton derivative $\mathsf H_{\bar G}\mathsf
s_I$ is dilation-invariant; at $\tau = 0$ it equals $\mathsf H_{G_0}\mathsf s$ over $\iota^+$, since $N_{\iota^+}(P_0)$
is the normal operator of $P_0$ at $\iota^+$ and their principal symbols agree there (Lemma 1.2, (1.9)), and $\pm\mathsf
H_{G_0}\mathsf s\le0$ on $\partial\Sigma^\pm$ (II.C Definition 2.4 (1), Proposition 5.1 (2) with $h = 0$). Every point is
a limit of its dilates towards $\tau = 0$, so $\pm\mathsf H_{\bar G}\mathsf s_I\le0$ everywhere. On $\{R\ge1\}$, $\mathsf
s' = \mathsf s$ by (a), and $g^{-1}-g_0^{-1} = \chi(\bar g^{-1}-g_0^{-1})+k$; with a cut-off $\psi(\tau/\tau_1)$ in time
($\psi = 1$ on $[0,1]$, supported in $[0,2)$), the dual metric $g_0^{-1}+\psi(\tau/\tau_1)\big(\chi(\bar
g^{-1}-g_0^{-1})+k\big)$ on $\Omega$ equals $g^{-1}$ on $\{\tau\le\tau_1\}$, and its difference from $g_0^{-1}$ has, with
norm in $\tilde{\mathcal G}^{1,(2\ell_I,\ell_+,\ell_K)}$ ($\ell_+\le1$) at most $C\tau_1^{2-\ell_+}$ plus that of $k$, as
$\bar g-g_0$ has relative decay $\rho_+^2$ and $\chi$ localises to $\{R\le2\}$ near $\iota^+$. For $\tau_1$ and $k$
small, II.C Proposition 5.1 (2) gives $\pm\mathsf H_G\mathsf s\le0$ on $\partial\Sigma^\pm$.

(c) Near $\iota^+\cap\mathscr I^+$, $\mathsf s' = \mathsf s$, constant near those radial sets by II.C Proposition 5.1
(5). Near cf, $\mathsf s' = \mathsf s_I$, the dilation-invariant extension of $\mathsf s$ restricted to the phase space
over $\iota^+\cap K^+$ identified by (10.44); $\mathsf s$ is constant near $\partial R_{\partial K^+,\mathrm{in/out}}$
with the thresholds of II.C Definition 2.4 (5)-(6) (II.C Proposition 5.1 (1)), and so is $\mathsf s_I$ near their
$\tau$-invariant extensions, with the same values. For $\mathsf s_{\flat,I}$ the same, by the choice of $\eta_1$.
$\square$

### 7.3 The statement

Fix $\tau_0\in(0,\tau_1]$, to be decreased in section 7.6. Spaces are those of (6.3) on $[0,\tau_0]\times\iota^+$.

**Proposition 7.4 ([Hin26c] Proposition 10.14 at $n = 4$).** Let $\mathsf s$, $\mathsf s'$ be as in section 7.2. There is
$\tau_0\in(0,\tau_1]$ such that, for all $\gamma_I<\frac32+\bar S$, $\gamma_+<\min(\gamma_I,1+\beta_+)$,
$\gamma_{\mathrm{cf}} := -(\alpha_++2)$ and $k\in\mathbb N_0$:

(1) (*Existence.*) For every $f\in\dot H^{(\mathsf
s'-1;k),(2\gamma_I+2,\gamma_++2,\gamma_{\mathrm{cf}}-2)}_{\mathrm{ebe};b}([0,\tau_0]\times\iota^+)$ there is a forward
solution $u\in\dot H^{(\mathsf
s';k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b}([0,\tau_0]\times\iota^+)$ of $P_+u = f$, with $\|u\|\le
C\|f\|$ in these norms.

(2) (*Strong uniqueness.*) If $\tilde u\in\mathcal D'((0,\infty)\times(\iota^+)^\circ)$ is supported in
$\{\tau\le\tau_0\}$, $P_+\tilde u = 0$, and $\tilde u\in H^{\mathsf
s',\gamma_{\mathrm{cf}}}_{e,\mathrm{loc}}((0,\infty)_\tau\times\{R<R_0\})$ for some $R_0>0$, then $\tilde u = 0$.

$\tau_0$ depends on $\mathsf s$ and $P_0$ only through section 7.6; the dependence on the weights is only through the
constants. The hypotheses on $(\gamma_I,\gamma_+)$ are those of Proposition 6.2.

### 7.4 Strong uniqueness

*Proof of Proposition 7.4 (2).* As for Proposition 6.2 (2), only the region near $r = 0$ is non-standard. Let $s'' :=
\lfloor\inf\mathsf s'\rfloor$. In $(t_*,r,\omega)$, for $t_*\ge t_{*,0}$ with $t_{*,0}>3$ and $t_{*,0}\ge\tau_0^{-1}$,
$\{r\le3\}\subset\{R<1\}$, where $P_+ = N := N_{\iota^+}(P_0)$. After a translation in $t_*$ we may assume that $\tilde u
= 0$ for $t_*<t_{*,0}$ (the support condition) and show $\tilde u = 0$ on $\{t_*<t_{*,0}+\frac12\}$; iterating in steps
of $\frac12$ gives $\tilde u = 0$. (Here no rescaling is needed: on $\{t_*\ge t_{*,0},\ r<3\}$ we have $R<1$, and the
regularity hypothesis gives edge order $s''$ with weight $\gamma_{\mathrm{cf}}$ at $r = 0$ on
$\{r<R_0t_*\}\supset\{r<3\}$ once $t_{*,0}\ge3/R_0$, which we also assume.)

Let $\chi_r\in C^\infty_c([0,3))$ equal 1 near $[0,2]$. Then $N(\chi_r\tilde u) = P_+(\chi_r\tilde u) =
[P_+,\chi_r]\tilde u =: g$ on $\{t_*\ge t_{*,0}\}$, with $g$ supported in $\{2\le r\le3\}$ and in
$H^{s''-1}_{\mathrm{loc}}$. Let $\chi_g\in C^\infty(\mathbb R)$ equal 1 on $(-\infty,t_{*,0}+1]$ and 0 on
$[t_{*,0}+\frac32,\infty)$, and let $u_{\mathrm{mid}}$ solve $Nu_{\mathrm{mid}} = -\chi_gg$ on $\{t_*<t_{*,0}+2\}$ as in
Lemma 6.3 (translated, with $T = t_{*,0}$, $s' = s''$): it vanishes for $t_*<t_{*,0}$ and where $t_*+2r<t_{*,0}+4$, and
is in $H^{s'',2\gamma_I}_e$ near $\mathscr I^+$ for $t_*<t_{*,0}+2$. Then $N(\chi_r\tilde u+u_{\mathrm{mid}}) = 0$ on
$\{t_*\le t_{*,0}+1\}$. Let $\chi_{t_*}\in C^\infty(\mathbb R)$ equal 1 on $(-\infty,t_{*,0}+\frac12]$ and 0 on
$[t_{*,0}+1,\infty)$, and $w := \chi_{t_*}(\chi_r\tilde u+u_{\mathrm{mid}})$. $w$ has compact $\tau$-support, lies in
$H^{s'',(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe}}$ (near $r = 0$ by hypothesis, near $\mathscr I^+$ by
Lemma 6.3, in between $H^{s''}_{\mathrm{loc}}$), and $Nw = [N,\chi_{t_*}](\chi_r\tilde u+u_{\mathrm{mid}})$ is supported
in $\{t_*\ge t_{*,0}+\frac12\}$. By Lemma 6.4, $w$ is supported in $\{t_*\ge t_{*,0}+\frac12\}$. So on
$\{t_*<t_{*,0}+\frac12\}$, $\chi_r\tilde u = -u_{\mathrm{mid}}$, which vanishes where $t_*+2r<t_{*,0}+4$, in particular
on $\{t_*<t_{*,0}+\frac12,\ r<\frac74\}$; hence $\tilde u = 0$ there. On the rest of $\{t_*<t_{*,0}+\frac12\}$ (where
$r\ge\frac74$), $P_+$ has smooth coefficients and the Lorentzian principal symbol $G_\chi$ (Lemma 7.2 (c)). For such a
point $p$, the causal past of $p$ for $g_\chi$ meets $\{t_*\ge t_{*,0}\}$ in a compact set: on $\{R\le1\}$, $g_\chi =
\bar g$, for which $t_*$ is non-decreasing and $r = t-t_*\le t(p)-t_{*,0}$ along past causal curves from $p$, and on
$\{R\ge1\}$, $g_\chi$ is a small perturbation of $g_0$, whose causal cones are those of $\bar g$ up to $O(r^{-1})$,
$dt_*$ being past causal for both. Its part in $\{r<\frac74\}\cup\{t_*<t_{*,0}\}$ lies where $\tilde u = 0$, so the
domain-of-dependence uniqueness for distributional solutions of hyperbolic operators with smooth coefficients ([Hö85]
chapter 23), applied on a neighbourhood of the rest in $\{r>1\}$, gives $\tilde u = 0$ near $p$. $\square$

### 7.5 Finite-time solvability

**Lemma 7.5 (forward solutions on finite intervals).** Let $f$ be as in Proposition 7.4 (1) and $T\ge\tau_0^{-1}$. There
is a unique $u$ on $\{\tau_0^{-1}\le t_*<T\}$, vanishing near $t_* = \tau_0^{-1}$, with $P_+u = f$ there and
$\psi_Tu\in\dot H^{(\mathsf s';k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b}$ for every $\psi_T\in
C^\infty_c((-\infty,T))$ (a function of $t_*$), with $\|\psi_Tu\|\le C_{T,\psi_T}\|f\|$. The same holds for the operators
$P^\epsilon_+$ of section 7.6, $\epsilon\in(0,\tau_0]$, in place of $P_+$, with constants independent of $\epsilon$.

*Proof.* *Uniqueness* follows from Proposition 7.4 (2), proved above: the difference of two solutions, cut off by
$\psi_T$ near $t_* = T$, solves $P_+v = 0$ on $\{t_*<T'\}$ for $T'<T$, and the argument of section 7.4 is local in time.

*Existence, one step.* Let $t_{*,0}\ge\tau_0^{-1}$ and $f_0\in\dot H^{(\mathsf
s'-1;k),(2\gamma_I+2,\gamma_++2,\gamma_{\mathrm{cf}}-2)}_{\mathrm{ebe};b}$, supported in $\{t_*\ge t_{*,0}\}$. By Lemma
7.3 (a), $\mathsf s' = \mathsf s_I$ on $\{R\le10\}$, so $\chi f_0\in\dot H^{(\mathsf
s_I-1;k),(\infty,\gamma_++2,\gamma_{\mathrm{cf}}-2)}$, and Proposition 6.2 (1) gives the forward solution
$u_{\mathrm{cf}}$ of $Nu_{\mathrm{cf}} = \chi f_0$, with $\chi u_{\mathrm{cf}}\in\dot H^{(\mathsf
s_I;k),(\infty,\gamma_+,\gamma_{\mathrm{cf}})}$. Let $\chi^\flat = \chi^\flat(R)$ equal 1 near $[0,1]$, supported in
$\chi^{-1}(1)$. As $P_+ = N$ on $\{\chi = 1\}^\circ$,
$$f_1 := f_0-P_+(\chi^\flat u_{\mathrm{cf}}) = (1-\chi^\flat)f_0-[N,\chi^\flat](\chi u_{\mathrm{cf}})\in\dot H^{(
\mathsf s'-1;k),(2\gamma_I+2,\gamma_++2,\infty)},$$
supported in $\{R\ge1\}\cap\{t_*\ge t_{*,0}\}$, with norm $\le C\|f_0\|$. Next we solve $P_+u_{\mathrm{mid}} = f_1$ on
$\{t_*\le2t_{*,0}\}$. Let $\psi,\tilde\psi\in C^\infty(\mathbb R)$, $\psi = 0$ on $(-\infty,\frac12]$, $\psi = 1$ on
$[1,\infty)$, $\tilde\psi = 1$ on $(-\infty,2]$, $\tilde\psi = 0$ on $[3,\infty)$, and on $\Omega$
$$P_{\mathrm{aux}} := P_0+\psi(8r/t_{*,0})\tilde\psi(t_*/t_{*,0})(P_+-P_0).$$
$P_+-P_0 = \chi(N-P_0)$ is supported in $\{R\le2\}$; on the support of the cut-offs, $r\ge t_{*,0}/16$ and
$t_*\le3t_{*,0}$, and as $\chi(R) = 0$ for $R\ge2$, also $t_*\ge t_{*,0}/32$; so the second term lives where $\rho_+\sim
t_{*,0}^{-1}$ and $R\in[\frac1{48},2]$, near $(\iota^+)^\circ$. There $N-P_0\in x_I^2\rho_+^3\mathrm{Diff}^2_{e3b}$
(Lemma 1.2) and the principal symbols differ by $O(\rho_+^2)$ relative to $G_0$ (II.C Definition 3.1, Remark (a)); the
cut-offs, functions of $r/t_{*,0}$ and $t_*/t_{*,0}$ with $r\sim t_*\sim t_{*,0}$ on their supports, have e3b-derivatives
bounded uniformly in $t_{*,0}$. Hence $P_{\mathrm{aux}}$ is weakly admissible relative to $P_0$ (II.C Definition 3.3,
$p_0 = \tilde p_1 = 0$) with $\epsilon_P\le Ct_{*,0}^{-(1-\ell_+)}$ ($\ell_+<1$), and its metric is close to $g_0$; for
$t_{*,0}$ large (i.e. $\tau_0$ small), the hypotheses of II.E section 1.1 and of II.C Proposition 5.1 (2) hold for
$P_{\mathrm{aux}}$, so $\mathsf s$ is a slab order for it. Let $\Omega' = \Omega_{T_0,T_1}$ be a slab containing
$\{t_{*,0}\le t_*\le2t_{*,0},\ r\ge t_{*,0}/4\}$ and with $f_1$ supported in $\{t^\flat\ge T_0\}$ there. $f_1\in
H^{(\mathsf s-1;k),2\alpha+2}(\Omega')^{\bullet,-}$, $\alpha := \gamma_I-2<-\frac12+\bar S$ ($\mathsf s' = \mathsf s$ on
$\{R\ge1\}$, and the weight shift is II.A Lemma 6.1, as in section 6.3), and II.E Proposition 4.3 gives the forward
solution $u_{\mathrm{aux}}\in H^{(\mathsf s;k),2\alpha}(\Omega')^{\bullet,-}$ of $P_{\mathrm{aux}}u_{\mathrm{aux}} =
f_1$, with norm $\le C\|f_1\|$.

*Support and order of $u_{\mathrm{aux}}$.* A future causal curve for $g_{\mathrm{aux}}$ from
$\mathrm{supp}\,f_1\subset\{R\ge1,\ t_*\ge t_{*,0}\}$ that enters $\{R<1\}$ does so at a point with $r = t_*\ge t_{*,0}$,
hence with $t+r = t_*+2r\ge3t_{*,0}$; within $\{R\le1,\ r\ge t_{*,0}/8\}$ the metric is $\bar g$ and $t+r$ is
non-decreasing, so while $t_*\le2t_{*,0}$ the curve stays in $\{r\ge t_{*,0}/2\}$. So $u_{\mathrm{aux}}$ vanishes on
$\{t_*\le2t_{*,0},\ r<t_{*,0}/2\}$, and on $\{t_*\le2t_{*,0}\}$ it solves $P_+u_{\mathrm{aux}} = f_1$, as
$P_{\mathrm{aux}} = P_+$ on $\{t_*\le2t_{*,0},\ r\ge t_{*,0}/8\}$. Its order is $\mathsf s$; on $\{R\ge1\}$ that is
$\mathsf s'$. On $\{t_{*,0}/2\le r,\ R\le1,\ t_*\le2t_{*,0}\}$, an interior region where $P_+ = N$ has smooth
coefficients, we upgrade to the order $\mathsf s'$ by real principal type propagation (II.A$'$; in the interior
b-regularity is regularity, and the $k$ b-derivatives are handled by the commuted systems of II.D$'$ Lemmas 2.1 and 2.5):
$\mathsf s'$ is non-increasing along the future flow (Lemma 7.3 (b)), $P_+u_{\mathrm{aux}} = f_1\in H^{(\mathsf
s'-1;k)}$, there are no radial points over the interior, and every backward null bicharacteristic from a point of this
region reaches, within $\{t_*\le2t_{*,0}\}$, either $\{r<t_{*,0}/2\}$ (where $u_{\mathrm{aux}} = 0$) or $\{R\ge1\}$
(where it is of order $\mathsf s = \mathsf s'$): radially outgoing ones keep $t_*$ and decrease $r$ backward, the others
leave every compact subset of $\{t_*\ge t_{*,0}\}$ backward. With $\chi_{t_*}$ equal to 1 for $t_*\le\frac32t_{*,0}$ and
0 for $t_*\ge2t_{*,0}$, $u_{\mathrm{mid}} := \chi_{t_*}u_{\mathrm{aux}}\in\dot H^{(\mathsf
s';k),(2\gamma_I,\infty,\infty)}_{\mathrm{ebe};b}$ with norm $\le C_{t_{*,0}}\|f_0\|$ (near $\mathscr I^+$ by II.A Lemma
6.1 and the identification of e3b- and ebe-spaces there), and
$$f_2 := f_1-P_+u_{\mathrm{mid}} = -[P_+,\chi_{t_*}]u_{\mathrm{aux}}$$
is supported in $\{t_*\ge\frac32t_{*,0}\}$, with norm $\le C_{t_{*,0}}\|f_0\|$ in the space of $f_0$. Thus $\chi^\flat
u_{\mathrm{cf}}+u_{\mathrm{mid}}$ solves $P_+u = f_0$ on $\{t_*<\frac32t_{*,0}\}$, with an error $f_2$ supported in
$\{t_*\ge\frac32t_{*,0}\}$.

*Iteration.* Apply the step to $f_2$ with $\frac32t_{*,0}$ in place of $t_{*,0}$, and so on; after $j$ steps the sum of
the partial solutions solves $P_+u = f$ on $\{t_*<(\frac32)^j\tau_0^{-1}\}$, and $(\frac32)^j\to\infty$. The bounds
follow step by step. The same argument applies to $P^\epsilon_+$ of section 7.6, which equals $N$ on $\{R\le1\}$ and
differs from $P_+$ only on $\{\tau\le2\epsilon\}$ by a term of the class (7.6), so that $P_{\mathrm{aux}}$ built from it
satisfies the same smallness uniformly in $\epsilon$. $\square$

### 7.6 The a priori estimate, and the proof of Proposition 7.4 (1)

*Radial estimates at cf.* Near cf, by (10.44) of the source, the ebe-phase space over $\{\tau = 0,R = 0\}$ is the
3b-phase space over $\partial K^+ = \iota^+\cap K^+$, and $P_+ = N$ is $\tau$-dilation-invariant on $\{R<1\}$; its
rescaled Hamilton field is the dilation-invariant extension of $\bar{\mathsf H}$ over $\partial K^+$ (II.B section 3),
with radial sets $R_{\mathrm{cf},\mathrm{in}}$, $R_{\mathrm{cf},\mathrm{out}}$ over all of cf: a saddle whose stable
manifold lies over $\{R>0\}$ (radially infalling null geodesics) and whose unstable manifold lies over $\{R = 0\}$, which
is the stable manifold of $R_{\mathrm{cf},\mathrm{out}}$, whose unstable manifold lies over $\{R>0\}$ (radially outgoing
null geodesics) ([Hin26c] p. 223; II.B Lemma 3.3 over $\iota^+$, extended by invariance). With $\tilde\tau :=
(t_*+r)^{-1} = \tau/(1+R)$, whose differential is timelike for $\bar g$, let $\psi_+\in C^\infty([0,\infty))$ equal 1
near $[0,\tau_2]$, vanish on $[2\tau_2,\infty)$, be non-increasing, and have $\sqrt{-\psi_+\psi'_+}$ smooth.

**Lemma 7.6 (radial estimates at cf; [Hin26c] p. 223).** Let $\mathsf t$ be an order on ${}^{\mathrm{ebe}}S^*$,
$\tau$-dilation-invariant and constant near $R_{\mathrm{cf},\mathrm{in}}$ (resp. $R_{\mathrm{cf},\mathrm{out}}$), with
the threshold (3.3) (resp. (3.5)) of II.D Proposition 3.2 (resp. 3.3) there for $\alpha_K = 0$. Then Propositions 3.2 and
3.3 of II.D, and their b-regular versions II.D$'$ Proposition 5.2, hold for $L = N$, $P_+$ or $P^\epsilon_+$ near
$R_{\mathrm{cf},\mathrm{in}}$ (resp. $R_{\mathrm{cf},\mathrm{out}}$) over $\mathrm{cf}\cap\{\tau\le\tau_2\}$, with the
ebe-weights $(\gamma_+,\gamma_{\mathrm{cf}})$ for $(\alpha_+,\alpha_K)$ (via $\alpha_+-\alpha_K =
-\gamma_{\mathrm{cf}}-2$, II.A Lemma 6.2), for $u$ vanishing on $\{\tilde\tau\ge\tau_2\}$. In place of II.D's condition
(4): at $R_{\mathrm{cf},\mathrm{in}}$ the Schwartz kernel of $E$ is supported away from cf; at
$R_{\mathrm{cf},\mathrm{out}}$, $\mathrm{WF}'(E)$ is disjoint from the unstable manifold of
$R_{\mathrm{cf},\mathrm{out}}$ (the $\tau$-invariant extension of $\partial W_{\mathrm{out}} = \{\hat\xi = 0,\hat\eta =
0\}$, over $\{R>0\}$); in both cases there is an additional term microsupported over
$\mathrm{supp}\,\psi'_+(\tilde\tau)$, which vanishes for such $u$.

*Proof.* The proofs of II.D Propositions 3.2-3.3 with $\Psi := \psi(\mathfrak M_Rq)\psi_+(\tilde\tau)\psi(\mathfrak
M\rho_{\mathrm{cf}})$ in place of $\psi(\mathfrak M_Rq)\psi(\mathfrak M\rho_+)\psi(\mathfrak M\rho_K)$. The quantities at
the radial set are unchanged: $\mathsf H$ is the dilation-invariant extension of $\bar{\mathsf H}$, so $\rho^{-1}\mathsf
H\rho$, $\mathsf Hq$ and the imaginary part $\mathfrak p'$ (that of $N$, which at $R = 0$ is that of $P_0$ at $\partial
K^+$, its coefficients being $P_0$'s frozen) take the values used there at every $\tau$; the weight $w =
\tau^{\gamma_+}\rho_{\mathrm{cf}}^{\gamma_{\mathrm{cf}}} = \rho_+^{\alpha_+}\rho_K^{\alpha_K}\cdot(\text{smooth
positive})$ under (10.44) gives the same contribution, $\tau$ being dilation-invariant ($\tau^{-1}\mathsf H\tau = 0$ at
the radial set, as $\rho_+^{-1}\mathsf H\rho_++\rho_K^{-1}\mathsf H\rho_K = 2-2$ there). The factor $\psi(\mathfrak
M\rho_{\mathrm{cf}})$ plays the role of $\psi(\mathfrak M\rho_K)$, with the same signs. The factor $\psi_+(\tilde\tau)$
replaces $\psi(\mathfrak M\rho_+)$: $\mathsf H(\psi_+^2) = 2\psi_+\psi'_+\mathsf H\tilde\tau$, and on the future
characteristic set $\mathsf H\tilde\tau\le0$ ($\tilde\tau$ decreases along future causal curves), so this is
$(\sqrt{-\psi_+\psi'_+})^2\cdot2(-\mathsf H\tilde\tau)\ge0$, a term $+e^*e$ microsupported over
$\mathrm{supp}\,\psi'_+(\tilde\tau)\subset\{\tilde\tau\ge\tau_2\}$, where $u = 0$. For $P_+$ and $P^\epsilon_+$ on
$\{R<1\}$ the operator is $N$. $\square$

**Lemma 7.7 (the symbolic estimate; [Hin26c] (10.54)-(10.55)).** For $\tau_0\le\tau_2/2$ small and every
$\epsilon\in(0,\tau_0]$, with $C$ independent of $\epsilon$, every $u\in\dot H^{(\mathsf
s_{\flat,I};k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b}([0,\tau_0]\times\iota^+)$ with
$P^\epsilon_+u\in\dot H^{(\mathsf s'-1;k),(2\gamma_I+2,\gamma_++2,\gamma_{\mathrm{cf}}-2)}_{\mathrm{ebe};b}$ lies in
$\dot H^{(\mathsf s';k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b}$ and
$$\|u\|_{(\mathsf s';k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}\le C\big(\|P^\epsilon_+u\|_{(\mathsf s'-1;k),(2
\gamma_I+2,\gamma_++2,\gamma_{\mathrm{cf}}-2)}+\|u\|_{(\mathsf s_{\flat,I};k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}
\big).\tag{7.2}$$
Here $P^\epsilon_+ := \chi_0(\tau/\epsilon)N+(1-\chi_0(\tau/\epsilon))P_+$, $\chi_0\in C^\infty_c([0,2))$ equal to 1 on
$[0,1]$.

*Proof.* $P^\epsilon_+-P_+ = -\chi_0(\tau/\epsilon)(P_+-N)$, and by Lemma 7.2 (b)
$$\{P^\epsilon_+-N:\epsilon\in(0,1]\}\ \text{is bounded in}\ x_I^2\tau^3\rho_{\mathrm{cf}}^{-2}C^\infty_b
\mathrm{Diff}^2_{\mathrm{ebe}},\qquad P^\epsilon_+\to P_+\ \text{in}\ x_I^2\tau^2\rho_{\mathrm{cf}}^{-2}C^\infty_b
\mathrm{Diff}^2_{\mathrm{ebe}},\tag{7.6}$$
as $\chi_0(\tau/\epsilon)$ is bounded in $C^\infty_b([0,\infty)_\tau)$ and $\tau\chi_0(\tau/\epsilon) = O(\epsilon)$
there ([Hin26c] (10.56)). The dual metric of $P^\epsilon_+$ is $g_\chi^{-1}+k_\epsilon$, $k_\epsilon =
\chi_0(\tau/\epsilon)(1-\chi)(\bar g^{-1}-g_0^{-1})$, supported in $\{\tau\le2\epsilon,R\ge1\}$ and small; so Lemma 7.3
(b) applies to it. Now combine, in the ebe-phase space over $[0,\tau_0]\times\iota^+$, the following estimates, each
valid for $P^\epsilon_+$ uniformly in $\epsilon$, in the strong sense, with the orders $\mathsf s'$ (target) and $\mathsf
s_{\flat,I}$ (a priori), and with $k$ b-derivatives: (i) elliptic estimates off the characteristic set of $G_\chi$
(II.A$'$); (ii) real principal type propagation along the future flow (II.A$'$; with $k$ b-derivatives through the
commuted systems of II.D$'$ Lemmas 2.1 and 2.5), using Lemma 7.3 (b); (iii) at $R_{\mathscr I^+,\mathrm{in},+}$, the
radial saddle estimate II.D Proposition 3.5 (II.D$'$ Proposition 3.2), where $P^\epsilon_+ = P_0$ (on $\{R\ge2\}$) up to
a term vanishing at $\iota^+$ in the class allowed there, with control on its stable manifold from (ii) along $\mathscr
I^+$ (II.B Lemma 7.2 (3)); (iv) at $R_{\mathrm{cf},\mathrm{in}}$, Lemma 7.6 (in), with control on its stable manifold
(over $\{R>0\}$: radially infalling null bicharacteristics, which come backward from $\{t_*<\tau_0^{-1}\}$ or, over
$\iota^+$, from the unstable manifold of $R_{\mathscr I^+,\mathrm{in},+}$) from (ii) and (iii); (v) at
$R_{\mathrm{cf},\mathrm{out}}$, Lemma 7.6 (out); (vi) at $R_{\mathscr I^+,\mathrm{out}}$, the radial sink estimate II.D
Proposition 3.6 (II.D$'$ Proposition 3.2). The thresholds hold for $\mathsf s'$ and $\mathsf s_{\flat,I}$ by Lemma 7.3
(c) (at the incoming sets the a priori order $\mathsf s_{\flat,I}$ is above threshold, at the outgoing sets the target
order $\mathsf s'$ is below it), and with $\gamma_I<\frac32+\bar S$ at $\mathscr I^+$ (II.D Propositions 3.5-3.6 at the
weight $\alpha_I = \gamma_I-2$). The flow over $\iota^+$ is that of II.B Proposition 8.1 (pulled back by
$\tau$-invariance near cf), and $t_*$ is non-decreasing along the future flow (Lemma 7.2 (c)); so every point of the
characteristic set over $[0,\tau_0]\times\iota^+$ is reached, backward along the flow, either from $\{t_*<\tau_0^{-1}\}$,
where $u = 0$, or from one of the radial sets, in the order (iii)-(vi) ([Hin26c] Figure 10.3). The constants depend on
finitely many seminorms of $P^\epsilon_+$ in the class of (7.6) and on the margins, so they are uniform in $\epsilon$;
$\tau_0\le\tau_2/2$ makes the $\psi_+$-terms of Lemma 7.6 vanish for $u$ supported in $\{\tau\le\tau_0\}$ (there
$\tilde\tau\le\tau<\tau_2$). $\square$

*Inversion of the normal operator.* For $u$ as in Lemma 7.7, $u\in\dot H^{(\mathsf
s_{\flat,I};k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}$ and
$$Nu = P^\epsilon_+u-(P^\epsilon_+-N)u,\qquad\|(P^\epsilon_+-N)u\|_{(\mathsf s_{\flat,I}-1;k),(2\gamma_I+2,\gamma_++2,
\gamma_{\mathrm{cf}}-2)}\le C\|u\|_{(\mathsf s_{\flat,I}+1;k),(2\gamma_I,\gamma_+-1,\gamma_{\mathrm{cf}})}$$
by (7.6) (the factor $\tau^3$ against $\tau^2$ shifts the $\tau$-weight by one). As $\mathsf s_{\flat,I}$ is the
dilation-invariant extension of an order admissible with weights $\alpha_+$, 0 and margin 0, the uniqueness and the
estimate of Proposition 6.2 (1) at the order $\mathsf s_{\flat,I}$ give
$$\|u\|_{(\mathsf s_{\flat,I};k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}\le C\|Nu\|_{(\mathsf s_{\flat,I}-1;k),(2
\gamma_I+2,\gamma_++2,\gamma_{\mathrm{cf}}-2)}\le C\big(\|P^\epsilon_+u\|_{(\mathsf s'-1;k),\dots}+\|u\|_{(
\mathsf s';k),(2\gamma_I,\gamma_+-1,\gamma_{\mathrm{cf}})}\big),$$
using $\mathsf s_{\flat,I}+1\le\mathsf s'$ (Lemma 7.3 (a)). With (7.2),
$$\|u\|_{(\mathsf s';k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}\le C\big(\|P^\epsilon_+u\|_{(\mathsf s'-1;k),(2
\gamma_I+2,\gamma_++2,\gamma_{\mathrm{cf}}-2)}+\|u\|_{(\mathsf s';k),(2\gamma_I,\gamma_+-1,\gamma_{\mathrm{cf}})}\big).
\tag{7.3}$$

*Absorption.* Multiplication by $\chi_0(\tau/\delta)$ maps $H^{(\mathsf s';k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}$
to $H^{(\mathsf s';k),(2\gamma_I,\gamma_+-1,\gamma_{\mathrm{cf}})}$ with norm $\le C\delta$, as it equals
$\tau\chi_0(\tau/\delta)$ times the identity of weights, and $\tau\chi_0(\tau/\delta) =
\delta\cdot(\tau/\delta)\chi_0(\tau/\delta)$ has $C^\infty_b$-seminorms $O(\delta)$. Fix $\delta$ with $C\cdot
C\delta\le\frac12$ in (7.3). For $\epsilon<\delta/2$, $P^\epsilon_+ = P_+$ on $\{\tau\ge\delta\}$, and
$(1-\chi_0(\tau/\delta))u$ is controlled by Lemma 7.5 for $P^\epsilon_+$ on $\{t_*<\delta^{-1}\}$, with constants
independent of $\epsilon$ (with $T = \delta^{-1}$ and $\psi_T$ adapted; the support of $1-\chi_0(\tau/\delta)$ lies in
$\{t_*\le\delta^{-1}\}$, where $u$ is the finite-time solution by uniqueness). Hence, for $u$ in the space of Lemma 7.7
and $\epsilon<\delta/2$,
$$\|u\|_{\dot H^{(\mathsf s';k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b}}\le C\|P^\epsilon_+u\|_{
\dot H^{(\mathsf s'-1;k),(2\gamma_I+2,\gamma_++2,\gamma_{\mathrm{cf}}-2)}_{\mathrm{ebe};b}},\tag{7.4}$$
$C$ independent of $\epsilon$ ([Hin26c] (10.58)); the absorbed term is finite because Lemma 7.7 places $u$ in the space
of order $\mathsf s'$.

*Existence.* Let $f$ be as in Proposition 7.4 (1) and $\epsilon<\delta/2$. Let $u^\epsilon_{\mathrm{ini}}$ be the
finite-time solution of $P^\epsilon_+u = f$ on $\{t_*<2\epsilon^{-1}\}$ (Lemma 7.5 for $P^\epsilon_+$), and
$\chi_{\epsilon/2} := \chi_0(2\tau/\epsilon)$. As $P^\epsilon_+ = N$ on
$\mathrm{supp}\,\chi_{\epsilon/2}\subset\{\tau\le\epsilon\}$,
$$u^\epsilon := (1-\chi_{\epsilon/2})u^\epsilon_{\mathrm{ini}}+N^{-1}\big(\chi_{\epsilon/2}f+[N,\chi_{
\epsilon/2}]u^\epsilon_{\mathrm{ini}}\big),$$
with $N^{-1}$ the forward solution operator of Proposition 6.2 (1), solves $P^\epsilon_+u^\epsilon = f$ ([Hin26c]
(10.59)): on $\{\tau\le\epsilon\}$, $P^\epsilon_+u^\epsilon =
N((1-\chi_{\epsilon/2})u^\epsilon_{\mathrm{ini}})+\chi_{\epsilon/2}f+[N,\chi_{\epsilon/2}]u^\epsilon_{ \mathrm{ini}} =
(1-\chi_{\epsilon/2})f+\chi_{\epsilon/2}f$, and on $\{\tau\ge\epsilon\}$, $u^\epsilon = u^\epsilon_{\mathrm{ini}}$.
Proposition 6.2 (1) is applied at the order $\mathsf s_I-\eta_1$, the dilation-invariant extension of $\mathsf s-\eta_1$,
which is admissible with margin 0: on $\{\tau\le\tau_1\}$, $\mathsf s'\ge\mathsf s_I-\eta_1$ by the proof of Lemma 7.3
(a), so the source lies in its space; so $u^\epsilon\in\dot H^{(\mathsf
s_I-\eta_1;k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}\subset\dot H^{(\mathsf s_{\flat,I};k),\dots}$, and Lemma 7.7
places $u^\epsilon$ in the space of order $\mathsf s'$. By (7.4), $\|u^\epsilon\|\le C\|f\|$ uniformly in $\epsilon$. A
subsequence $u^{\epsilon_j}$, $\epsilon_j\to0$, converges weakly to some $u\in\dot H^{(\mathsf
s';k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b}([0,\tau_0]\times\iota^+)$ with $\|u\|\le C\|f\|$. Since
$P^\epsilon_+ = P_+$ on $\{\tau\ge2\epsilon\}$, $P_+u = f$ on $\{\tau>2\epsilon_j\}$ for every $j$, hence on
$\{\tau>0\}$. $\square$

## 8. Forward solutions of $P_0$ on e3b-spaces ([Hin26c] Theorem 10.1)

**Theorem 8.1 ([Hin26c] Theorem 10.1 at $n = 4$).** Let $P_0$ be a stationary wave-type operator (II.C Definition 1.1),
in the setting of II.E section 1.1. Let $\alpha_I,\alpha_+\in\mathbb R$ with
$$\alpha_I<-\tfrac12+\bar S,\qquad\alpha_+<\alpha_I-\tfrac12.\tag{8.1}$$
Assume that $P_0$ is $\aleph$-admissible with sf-weight $\alpha_+$ and sf-loss $\delta$ (II.C Definition 2.7), and let
$\mathsf s\in C^\infty({}^{e3b}S^*M)$ be admissible with weights $\alpha_+$, $-\aleph$ and margin 0, and with weights
$\alpha_+$, 0 and margin 1 (II.C Definition 5.2). Then for every $k\in\mathbb N_0$ there is $C_k$ such that the forward
solution of $P_0u = f$ on $\Omega$ satisfies
$$\|u\|_{H^{(\mathsf s;k),(2\alpha_I,\alpha_+-\delta,-\aleph)}_{e3b;b}(\Omega;E)^{\bullet,-}}\le C_k\|P_0u\|_{H^{(
\mathsf s;k),(2\alpha_I+2,\alpha_++2,0)}_{e3b;b}(\Omega;E)^{\bullet,-}}.\tag{8.2}$$

The thresholds (8.1) are those of the source at every $n$: in the b-density weights of section 1.1, $\gamma_I =
\alpha_I+2<\frac32+\bar S = c+\bar S$, and $\gamma_+ = \alpha_++\frac52<\gamma_I$ (`iplusnorm5.py` N4-N5). [Hin26c]
Remark 10.2 applies: for $P = P_0$, $p_1 = S|_{\partial X}$, so $\bar p_1 = \bar S$, and (8.1) is the threshold of II.D
at $\mathscr I^+$.

### 8.1 The weights

With the metric density $|dt\,dx|$ on $\Omega$ and the b-densities of section 6.1, II.A Lemma 6.1 identifies near
$\iota^+$
$$H^{0,(2\alpha_I,\alpha_+,\alpha_K)}_{e3b}(|dt\,dx|) = H^{0,(2(\alpha_I+2),\alpha_++\frac52,\alpha_K+\frac12)}_{e3b}(|
\tfrac{d\tau}\tau|\mu_b),$$
and, on functions supported away from $K^+$ (near $\mathscr I^+$ and $(\iota^+)^\circ$), the e3b-spaces are the
ebe-spaces of (6.3) with the weights
$$\gamma_I := \alpha_I+2,\qquad\gamma_+ := \alpha_++\tfrac52,\qquad\gamma_{\mathrm{cf}} := -(\alpha_++2)\tag{8.3}$$
(the orders transported by the identification of Lemma 7.2 (a); near $\iota^+$, $\tau\sim\rho_+$ on $\{R\ge\frac12\}$).
They satisfy the hypotheses of Propositions 6.2 and 7.4: $\gamma_I<\frac32+\bar S$ and $\gamma_+<\gamma_I$ by (8.1); and
$\gamma_+-\frac12 = \alpha_++2 = -\gamma_{\mathrm{cf}}$ lies in $(\beta_-,\beta_+)$, as $P_0$ is tf-admissible with the
weight $\alpha_++2$ (II.C Definition 2.7 (2)), so $\gamma_+<\beta_++\frac12<1+\beta_+$. The source's footnote 100
explains the buffer $\frac12$: pointwise decay at $\iota^+$ is governed by the resonances, excluded in
$\mathrm{Im}\,\sigma>-1-\beta_+$ (Proposition 5.1), whereas the 3b-regularity order limits the decay obtainable by
Sobolev embedding.

### 8.2 Proof

*Step 0: late sources.* Let $\tau_0$ be as in Proposition 7.4, for the orders $\mathsf s$ and $\mathsf s+1$ (both meet
its hypotheses: $\mathsf s+1$ is admissible with weights $\alpha_+$, 0 and margin 0 and meets the lower thresholds with
margin 2, as $\mathsf s$ has margin 1). Let $T := \tau_0^{-1}$ and $\psi_T\in C^\infty(\mathbb R)$ equal 1 on
$(-\infty,T]$ and 0 on $[T+1,\infty)$, a function of $t_*$. By II.E Proposition 4.3 (with $P = P_0$, the slab order
$\mathsf s$, the weight $\alpha_I$ and a slab containing $\{1\le t_*\le T+1\}$), the forward solution $u_0$ of $P_0u_0 =
f$ on that slab satisfies $\|u_0\|_{H^{(\mathsf s;k),2\alpha_I}}\le C\|f\|$; at finite times the weights at $\iota^+$ and
$K^+$ are irrelevant. Then $f_1 := f-P_0(\psi_Tu_0) = (1-\psi_T)f-[P_0,\psi_T]u_0$ is supported in $\{t_*\ge T\}$, with
$\|f_1\|\le C\|f\|$ in the space of (8.2), and the forward solution of $P_0u = f$ is $\psi_Tu_0+u_1$ with $P_0u_1 = f_1$.
So it suffices to prove (8.2) when $\mathrm{supp}\,f\subset\{t_*\ge\tau_0^{-1}\}$, which we assume.

For $j = 1,2,3,4$ let $\chi_j\in C^\infty_c([0,j+1))$ equal 1 near $[0,j]$, regarded as functions of $R = r/t_*$ on
$\Omega$, with $\chi_1 = \chi$ of Definition 7.1.

*Step 1: a solution near $\mathscr I^+$.* $(1-\chi_2)f$ is supported in $\{R\ge2\}$ and defines a function on
$[0,\infty)_\tau\times\iota^+$ vanishing near cf; by section 8.1,
$$(1-\chi_2)f\in\dot H^{(\mathsf s;k),(2\gamma_I+2,\gamma_++2,\infty)}_{\mathrm{ebe};b}([0,\tau_0]\times\iota^+),$$
with norm $\le C\|f\|$. Apply Proposition 7.4 (1) at the order $\mathsf s+1$, for which $(\mathsf s+1)' = \mathsf s'+1$
equals $\mathsf s+1$ on $\{R\ge1\}$ (Lemma 7.3 (a)), so that $(1-\chi_2)f$ lies in the space of its source: the forward
solution $u_I$ of $P_+u_I = (1-\chi_2)f$ satisfies
$$u_I\in\dot H^{(\mathsf s'+1;k),(2\gamma_I,\gamma_+,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b}([0,\tau_0]\times\iota^+),
\qquad\|u_I\|\le C\|f\|.\tag{8.4}$$
On $\mathrm{supp}(1-\chi_3)\subset\{R\ge3\}$, $P_0 = P_+$ and $\chi_2 = 0$, so
$$f' := f-P_0\big((1-\chi_3)u_I\big) = f-(1-\chi_3)f+[P_0,\chi_3]u_I = \chi_3f+[P_0,\chi_3]u_I.$$
$f'$ is supported in $\{R\le4\}$, away from $\mathscr I^+$, so it is a function on $\tilde M_0$ near $\iota^+\cup K^+$;
$[P_0,\chi_3]$ is a first-order e3b-operator with the weight $\rho_+^2$ of $P_0$ (II.C Lemma 1.4), supported in $\{3\le
R\le4\}$, and $u_I$ has order $\mathsf s+1$ there, so with the identification of e3b- and 3b-spaces away from $\mathscr
I^+$,
$$f'\in H^{(\mathsf s;k),(\alpha_++2,0)}_{3b;b}(\Omega)^{\bullet,-},\qquad\mathrm{supp}\,f'\subset\{t_*\ge\tau_0^{-1},\ R
\le4\},\qquad\|f'\|\le C\|f\|.\tag{8.5}$$

*Step 2: the solution sourced by $f'$.* Let $u'$ be the forward solution of $P_0u' = f'$. By $\aleph$-admissibility (II.C
Definition 2.7 (3), (2.2)), for the order $\mathsf s$, which over $K^+$ is stationary-$P_0$-admissible with weights
$\alpha_+$, $-\aleph$ and margin 0 (II.C Proposition 5.1 (1)),
$$u'\in H^{(\mathsf s;k),(\alpha_+-\delta,-\aleph)}_{3b;b}(\Omega)^{\bullet,-},\qquad\|u'\|\le C\|f'\|.\tag{8.6}$$

*Step 3: $u'$ near $\mathscr I^+$.* We show that $(1-\chi_4)u'$, regarded on $M$, is e3b-regular near $\mathscr I^+$. As
$(1-\chi_4)f' = 0$,
$$P_0\big((1-\chi_4)u'\big) = -[P_0,\chi_4]u' =: f'',$$
supported in $\{4\le R\le5\}$, away from $\mathscr I^+$ and from cf; on $[0,\infty)\times\iota^+$, by (8.6) and section
8.1 with $\alpha_+-\delta$ for $\alpha_+$,
$$f''\in\dot H^{(\mathsf s-1;k),(\infty,\gamma_+-\delta+2,\infty)}_{\mathrm{ebe};b}([0,\tau_0]\times\iota^+).$$
On $\mathrm{supp}(1-\chi_4)\subset\{R\ge4\}$, $P_0 = P_+$. Let $u''$ be the forward solution of $P_+u'' = f''$ given by
Proposition 7.4 (1) at the order $\mathsf s$ and with $\gamma_+-\delta$ in place of $\gamma_+$ (allowed, $\delta\ge0$;
$\mathsf s' = \mathsf s$ on $\mathrm{supp}\,f''$):
$$u''\in\dot H^{(\mathsf s';k),(2\gamma_I,\gamma_+-\delta,\gamma_{\mathrm{cf}})}_{\mathrm{ebe};b}([0,\tau_0]\times
\iota^+),\qquad\|u''\|\le C\|f''\|\le C\|f\|.$$
$\tilde u := u''-(1-\chi_4)u'$, extended by 0 to $\{\tau>\tau_0\}$, is a distribution on
$(0,\infty)\times(\iota^+)^\circ$ supported in $\{\tau\le\tau_0\}$ with $P_+\tilde u = f''-f'' = 0$; near cf it equals
$u''$, as $(1-\chi_4)u'$ vanishes on $\{R\le4\}$, so $\tilde u\in H^{\mathsf
s',\gamma_{\mathrm{cf}}}_{e,\mathrm{loc}}((0,\infty)\times\{R<4\})$. By Proposition 7.4 (2), $\tilde u = 0$. Hence, as
$\mathsf s' = \mathsf s$ on $\{R\ge1\}$ and by section 8.1,
$$(1-\chi_4)u' = u''\in H^{(\mathsf s;k),(2\alpha_I,\alpha_+-\delta,\infty)}_{e3b;b}(\Omega)^{\bullet,-},\qquad\|(1-
\chi_4)u'\|\le C\|f\|.\tag{8.7}$$

*Step 4: conclusion.* $P_0((1-\chi_3)u_I+u') = (f-f')+f' = f$, and both terms are supported in $\{t_*\ge\tau_0^{-1}\}$;
by the uniqueness of forward solutions on slabs (II.E Proposition 3.4 (i), the terms lying in the slab spaces by (8.4),
(8.6) and (8.7)) this is the forward solution:
$$u = (1-\chi_3)u_I+\chi_4u'+(1-\chi_4)u'.$$
By (8.4), $(1-\chi_3)u_I\in H^{(\mathsf s+1;k),(2\alpha_I,\alpha_+,\infty)}_{e3b;b}(\Omega)^{\bullet,-}\subset
H^{(\mathsf s;k),(2\alpha_I,\alpha_+-\delta,\infty)}_{e3b;b}$ ($\mathsf s'+1 = \mathsf s+1$ on $\{R\ge1\}$); by (8.6),
$\chi_4u'\in H^{(\mathsf s;k),(\infty,\alpha_+-\delta,-\aleph)}_{e3b;b}(\Omega)^{\bullet,-}$, as $\chi_4u'$ is supported
in $\{R\le5\}$, away from $\mathscr I^+$, where 3b- and e3b-spaces agree; and (8.7). The three bounds give (8.2).
$\square$

**Remark 8.2 ([Hin26c] Remark 10.17 at $n = 4$).** If $P_0$ is $\aleph$-admissible with margin $d_\aleph$ (the relaxed
version after II.C Definition 2.7), then (8.2) holds with $\mathsf s-d_\aleph$ in place of $\mathsf s$ on the left, when
$\mathsf s$ is admissible with weights $\alpha_+$, $-\aleph$ and margin $d_\aleph$, and with weights $\alpha_+$, 0 and
margin $1+d_\aleph$: $\aleph$-admissibility enters only (8.6), which then gives the order $\mathsf s-d_\aleph$, and the
loss persists through Steps 3-4 (Proposition 7.4 is applied in Step 3 at the order $\mathsf s-d_\aleph$, which meets its
hypotheses).

## 9. Findings, and the sources

### 9.1 Findings against the source

Each item records a place where [Hin26c] section 10, read at $n = 4$, prints something other than what its argument gives
or uses; none changes a conclusion of the section, and the numerals at $n = 4$ are those of `iplusnorm5.py` N1-N9.

(F1) Definition 10.3 prints $N_{\iota^+}(P_0) = t_*^2N^0$; the factor is $t_*^{-2}$, as the homogeneity of degree $-2$
and the use in Proposition 10.12 ("$N^0_{\iota^+}(P_0)u = t_*^2f$") require (section 1.2).

(F2) Proposition 10.6 (2) is stated for all $|z|\in[\frac12,2]$ with $\mathrm{Im}\,z\ge-h\gamma_+$, with $\mathsf b =
\mathsf b_\pm$ near $z = \pm1$ and "an arbitrary constant otherwise". The argument does not give this: away from
$\mathrm{Re}\,z = \pm1$ the adapted orders are dilates of $\mathsf b_\pm$, and a constant order must meet the threshold
at $R_{\mathrm{cf},\mathrm{out}}$, a source for $\mathrm{Im}\,z>0$. The families (3.2) cover every $\sigma$ the section
uses (section 3.1).

(F3) The source's (10.21) omits the term $\frac14x_I^2\xi^2$ of the symbol (1.13); it vanishes at $\mathscr I^+$ and
changes nothing there (section 1.3).

(F4) In the radial estimate at $R_{\mathrm{cf},\mathrm{out}}$ the source's sum prints $+4\,\mathrm{Re}\,S$ where the
computation gives $-4\,\mathrm{Re}\,S$; its stated threshold $\mathsf b+\alpha_+<-\frac12+\mathrm{Re}\,S$ is the one the
computation gives (section 3.3; `iplusnorm5.py` N7).

(F5) The Plancherel identity (10.47) prints $|\sigma|^j$ against squared norms; it is $|\sigma|^{2j}$ (II.A Lemma 6.2),
and the norm with the factors $h^{-j}$ of (4.1), not one with $\rho_{\mathrm{sf}}^{-j}$, is what it requires and what
section 4 proves (section 4.1). Its first integral prints $(\mathsf s;k-j)$ for $(\mathsf s;k)$.

(F6) The proof of Lemma 10.10 asks "$1+\mathrm{Im}\,\sigma<\beta_+$"; the condition it uses, and the one in Proposition
10.6 (1), is $-1-\mathrm{Im}\,\sigma<\beta_+$ (section 5.5).

(F7) Proposition 10.12 (1) takes $f$ of order $\mathsf s-2$; its proof gives (10.50) with $\mathsf s-1$, which is also
what Proposition 10.14 supplies; the loss of one order is that of the radial estimates over sf (section 6.2). The right
side of (10.50) prints the weights $(2\gamma_I,\gamma_++2,\gamma_{\mathrm{cf}}-2)$ for $\tau^{-2}f$; they are
$(2\gamma_I+2,\gamma_+,\gamma_{\mathrm{cf}}-2)$.

(F8) In the proof of Proposition 10.12 (2), "$t_*\ge4R_0$" is $t_*\ge4/R_0$, and "$\tilde u$ vanishes for $t_*\le2$ when
$r>\frac32$" is $r<\frac32$ (section 6.5).

(F9) In the proof of Theorem 10.1, $f'$ is placed in $H^{(\mathsf s;k),(2\alpha_I,\alpha_+,0)}_{e3b;b}$; its weight at
$\iota^+$ is $\alpha_++2$, as (10.62) then states (section 8.2, (8.5)).

### 9.2 Gaps in the source's arguments, and how they are closed here

(G1) *The parametrix at $\iota^+\cap\mathscr I^+$.* The source applies [0C] Theorem 1.5, which assumes that the boundary
spectrum is independent of the boundary point (with its logarithmic multiplicities), without checking it; here
$\mathrm{Spec}_b(\hat P,\omega_0) = \{2i\sigma\}\cup2(c+\mathrm{spec}\,S_0(\omega_0))$ with the Jordan structure of
$S_0(\omega_0)$. Section 5.3 uses [0C] Theorem 3.4, the calculus with bounds, which needs no constancy, and proves the
Fredholm property it implies ([0C] Corollary 3.6, whose proof [0C] leaves to the reader) by the Schur test; b-regularity
comes from difference quotients rather than from the structure of the parametrix's kernel. The reduced normal operator's
invertibility is shown by Bessel asymptotics (Lemma 5.4) in place of the source's positivity identity, and the triangular
reduction is done directly rather than by deforming $S_0(\omega_0)$ to a diagonal matrix.

(G2) *The Fourier transform bound.* (10.41) is quoted from [Hin23d] Lemma 2.25; Lemma 5.7 proves it.

(G3) *Strong uniqueness for $N_{\iota^+}(P_0)$.* The source compares $w$ with the solution $w'$ of part (1) by
uniqueness. Part (1) needs the source in a space of variable admissible order near $\mathscr I^+$, where the extension
$u_{\mathrm{ext}}$ is controlled only at a constant order. Lemma 6.4 replaces the comparison by a Paley-Wiener-Schwartz
argument at a constant order, using only Proposition 5.1 and (3.4). The control of $u_{\mathrm{ext}}$ at $\mathscr I^+$,
which the source takes from its Proposition 8.3 "applied without change" to $N_{\iota^+}(P_0)$, is proved in Lemma 6.3 by
rescaling and an auxiliary operator in the class of II.E.

(G4) *Dilation invariance of the error orders.* In the proof of Proposition 10.14, Proposition 10.12 is applied at the
orders $\mathsf s'_\flat$ (inversion of the normal operator) and $\mathsf s'$ (the solutions (10.59)), which are not
$\tau$-dilation-invariant, while Proposition 10.12's Plancherel argument needs invariance. Section 7 uses the invariant
orders $\mathsf s_{\flat,I}$ and $\mathsf s_I-\eta_1$, with $\mathsf s_\flat := \mathsf s-1-\eta_1$ and the slack
$\eta_1$ absorbing the difference on $\{\tau\le\tau_1\}$ (Lemma 7.3 (a)), and the symbolic estimate in the strong sense
(Lemma 7.7) to return to $\mathsf s'$.

(G5) *Finite-time solvability.* The source solves $P_+u_{\mathrm{mid}} = f'$ and takes control at $\mathscr I^+$ from its
Proposition 8.6; $P_+$ is not of the class of that proposition. Lemma 7.5 builds an auxiliary operator $P_{\mathrm{aux}}$
in that class, equal to $P_+$ where the solution lives, and upgrades the order from $\mathsf s$ to $\mathsf s'$ by
propagation.

(G6) *The radial estimates at cf.* The source describes them as minimal modifications of its Propositions 7.6-7.7 with a
cut-off $\psi_+(\tilde\tau)$; Lemma 7.6 states them and records which terms change.

(G7) *Domain of $P_+$.* Definition 10.13 uses $\{t_*>1\}$; $P_0$ is defined where $r\ge r_0$, so $T_+ = \max(2,2r_0)$ is
used (Definition 7.1).

### 9.3 Sources

[Hin26c] P. Hintz, *(Non-)linear waves on asymptotically flat spacetimes. II*, arXiv:2606.28008v1, section 10 (pp.
200-227), read in full in the record's text extraction.

[0C] P. Hintz, *Elliptic parametrices in the 0-calculus of Mazzeo and Melrose*, arXiv:2112.08130v1: READ Definition 1.2
(p. 5), Theorem 1.5 (p. 6, not used), section 2's definitions of the calculus with bounds and Proposition 2.7 (p. 9),
Corollary 3.3 (p. 31), Theorem 3.4, Remark 3.5 and Corollary 3.6 (pp. 33-34); the dimension $n\ge1$ is arbitrary there
(p. 1).

[MM87] R. Mazzeo, R. Melrose, *Meromorphic extension of the resolvent on complete spaces with asymptotically constant
negative curvature*, J. Funct. Anal. 75 (1987): the boundedness of the small 0-calculus on weighted 0-Sobolev spaces, as
used in [0C] Corollary 3.3 (cited, not read).

[DLMF] NIST Digital Library of Mathematical Functions, release 1.2.8: (10.25.1), (10.28.2), (10.30.1)-(10.30.2),
(10.40.1)-(10.40.2), READ.

[Hö83] L. Hörmander, *The Analysis of Linear Partial Differential Operators I*, Theorem 7.3.1 (Paley-Wiener-Schwartz).

[Hö85] L. Hörmander, *The Analysis of Linear Partial Differential Operators III*, chapter 23 (the strictly hyperbolic
Cauchy problem): existence and domain-of-dependence uniqueness for second-order hyperbolic operators with smooth
coefficients.

The earlier parts are cited as in the header; [SBG] enters through II.A section 3.
