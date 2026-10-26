# Part III.H$'$. 2-admissibility of $L_b$ at n = 4 ([Hin26] section 10.2, Theorem 10.1)

*Status.* Verified (D252: the hundred-and-fifth verifier; no major finding, three minor findings and nine nits
seated, to be read). Written (D250). This part proves, at spatial dimension $n = 4$, [Hin26] Theorem 10.1 (pp. 199-201)
by the argument of its section 10.2 (pp. 212-217): the forward solution of $L_bu = f$ on $\Omega$ is represented by a
contour integral of $\widehat{L_b}(\sigma)^{-1}$ (Lemma 2.1), split into high frequencies (Lemma 3.1), a regular
low-frequency part (Lemma 4.1) and the contribution of the zero energy states (Lemma 5.1), which is controlled by
integrating twice in $t_*$ (Lemma 6.2). The conclusion (Theorem 1.3) is 2-admissibility with sf-weight
$\alpha_{\mathrm{sf}}$, $\alpha_{\mathrm{sf}}+2\in(0,1)$, margin 1 and *sf-loss 0*, for orders of a class $\mathcal O_c$
(Definition 1.1), at $b_0$ for every $k$ and, for $b\ne b_0$, for $k$ up to a bound fixed by the neighbourhood of $b_0$.

*What n = 4 changes.* At $n = 3$ the zero energy states decay like $r^{-1}$, the derivatives $\partial_{t_*}\dot g$,
$\partial^2_{t_*}h_{\mathrm s1}$ of their contributions have sf-weights $-\frac12-\epsilon$ and $\frac12-\epsilon$, and
the two integrations in $t_*$ end at $-\frac32-\epsilon$, below $\alpha_{\mathrm{sf}}$: the source's sf-loss
$\delta>\alpha_{\mathrm{sf}}+\frac32$. At $n = 4$ the states decay one order faster and the augmentation of III.H uses
states cut off in a cone inside $\iota^+$, whose Fourier transforms decay rapidly at scf (III.H Lemma 2.5): the
derivatives have sf-weights below $0$ and $1$, which is room for $\alpha_{\mathrm{sf}}+1$ and $\alpha_{\mathrm{sf}}+2$,
and the integrations return to $\alpha_{\mathrm{sf}}$ itself (Lemma 5.1, section 7). No splitting at $I^+$ (the source's
(10.57)) and no condition at the outgoing radial set (the source's use of its Remark 10.2 in Lemma 10.12) is needed.
Three points of the source's argument need more than it states, at $n = 3$ as at $n = 4$ ((H$'$2), (H$'$3), (H$'$6)):
the incoming threshold, the neighbourhood of $b_0$, and the variable-order step of its Lemma 10.13. Notation is that of
Parts II.A, II.C, I.A-I.C and III.H; no instrument is used, every step being by hand.

## 1. Setting, orders and the statement

*Spaces.* $\tilde M_0$ is the 3b-compactification of $\mathbb R_{t_*}\times\mathbb R^4$ of II.A section 5 (the source's
$[\overline{\mathbb R^4};k^+,k^-]$ at $n = 4$), with boundary hypersurfaces sf and $K^\pm$, $M_0 := \mathrm{cl}_{\tilde
M_0}\{r\ge r_0\}$ with $X = \{r\ge r_0\}$ as in III.H section 1, and ([Hin26] (10.2) at $n = 4$)
$$\Omega := \mathrm{cl}_{M_0}\{t_*\ge1\},\qquad\Omega_- := \mathrm{cl}_{M_0}\{t_*\le1\}.$$
On $M_0$, $\rho_{\mathrm{sf}} = r^{-1}$ and, near $K^+$, $\rho_K = r/(t_*+r)$ are defining functions, and
$r\partial_{t_*}$, $r\partial_r$, $\partial_\omega$ span $\mathcal V_{3b}$ over $C^\infty_b$ (equivalently
$\langle x\rangle\partial_{t_*}$, $\langle x\rangle\partial_{x_i}$: the scaled bounded geometry of II.A (S9) with scale
$\langle x\rangle$ in all directions). $H^{(\mathsf s;k),(\beta,\gamma)}_{3b;b} := \rho_{\mathrm{sf}}^\beta\rho_K^\gamma
H^{(\mathsf s;k)}_{3b;b}$ with $H^{(\mathsf s;k)}_{3b;b}$ of II.A Lemma 5.2 (test with up to $k$ of $\partial_{t_*}$,
$t_*\partial_{t_*}$, $\langle x\rangle\partial_x$), on $L^2(|dt_*\,dx|)$; on $\Omega$ the spaces are supported at $\{t_*
= 1\}$ and extendible at $\{r = r_0\}$ (superscript ${}^{\bullet,-}$), on $M_0$ extendible at $\{r = r_0\}$, on
$\Omega_-$ extendible (bar). As $\rho_K\le1$, $H^{(\mathsf s;k),(\beta,0)}_{3b;b}\subset H^{(\mathsf
s;k),(\beta,-\ell)}_{3b;b}$ for $\ell\ge0$, and $\partial_{t_*} =
\rho_{\mathrm{sf}}\cdot r\partial_{t_*}$ maps $H^{(\mathsf s;k),(\beta,\gamma)}_{3b;b}$ to
$H^{(\mathsf s-1;k),(\beta+1,\gamma)}_{3b;b}$.

*The operator and the weight.* $L_b$ is the linearised gauge-fixed Einstein operator of III.H section 1, $b$ near $b_0$,
and throughout
$$\alpha_{\mathrm{sf}}\in\mathbb R,\qquad\alpha_{\mathrm{sf}}+2\in(0,1),\tag{1.1}$$
the weight $\alpha$ of III.H (1.1) (II.A Lemma 5.1: a spacetime sf-weight $\beta$ with $K$-weight 0 is the spectral
weight $(\cdot+\beta,\beta,0)$, so III.H's spectral weight $\alpha$ is $\alpha_{\mathrm{sf}}$; II.C Definition 2.7's
tf-weight $\alpha_{\mathrm{sf}}+2$ is the source's $\alpha_{\mathrm{sf}}+\frac32$). $\mathcal P$ is the compactified
phase space of I.B section 2.4 and $\Phi_{z_0}:\mathcal P\to{}^{3b}S^*_{K^+}M_0$ the map of II.B Definition 2.2, under
which characteristic sets and flows correspond (II.B Lemma 2.3) and fibre infinity of $\mathcal P$ goes to $\{\sigma =
0\}$.

**Definition 1.1 (the orders).** $\mathcal O_c = \mathcal O_c(\alpha_{\mathrm{sf}})$ is the set of
$t_*$-translation-invariant $\mathsf s\in C^\infty({}^{3b}S^*\tilde M_0)$ which are stationary-$L_b$-admissible with
weights $\alpha_{\mathrm{sf}}$, $-2$ and margin 1 (II.C Definition 2.4) and moreover

(C1) $\mathsf s$ is constant, $=: s_c$, on $\{\sigma = 0\} = \Phi_{z_0}(\text{fibre infinity of }\mathcal P)$;

(C2) $\mathsf s$ is constant over $\{r\le r_2-\delta_0\}$, with $r_2$, $\delta_0$ those of I.B section 1.4 (in II.C
Definition 2.4 (3), $r_\Gamma\ge r_2-\delta_0$);

(C3) the monotonicity II.C Definition 2.4 (1) holds on a neighbourhood of the characteristic set, not only on it.

(C2) is implied by II.C Definition 2.4 (3), as $\Gamma$ lies over $\{r>r_2\}$ (so $r_\Gamma>r_2$); it is listed as a
reminder of what I.B uses. $\mathcal O_c$ is a restriction: II.C Definition 2.7 asks its (3) for all admissible
orders ((H$'$7)).

For $\mathsf s\in\mathcal O_c$ and $z_0 = \pm1$ put $S_{z_0} := \mathsf s\circ\Phi_{z_0}$ on $\mathcal P$. The order
induced at $\sigma\in\mathbb R\setminus0$ (II.A Lemma 5.1: the restriction of $\mathsf s$ to $-\sigma\,dt_*+T^*\tilde
X$) is $\mathsf s_\sigma(x,\xi) = S_{z_0}(x,\xi/|\sigma|)$, $z_0$ the sign fixed by the conventions of II.A Lemma 5.1
and II.B Definition 2.2 (by II.C Definition 2.4 (2) the choice is immaterial): $\mathsf s$ is homogeneous of degree 0 in
the 3b covector $(\sigma_{3b},\xi_{3b},\eta_{3b}) = (-r\sigma,r\xi,r\eta)$ (II.C Lemma 2.6, proof). By (C1), $\mathsf
s_\sigma = s_c$ at fibre infinity, and its decay order is $\mathsf r_\sigma := \mathsf s_\sigma$ on the face over
$\partial X$.

**Lemma 1.2 (the induced orders).** Let $\mathsf s\in\mathcal O_c$, $\mathsf r := S_{z_0}$ on the face over $\partial X$,
and $\mathsf b := S_{z_0}$.

(a) For $\sigma\ne0$ real, the order pairs $(s_c,\mathsf r_\sigma)$ and $(s_c+1,\mathsf r_\sigma+1)$ are admissible for
$\sigma$ in the sense of I.A (O1)-(O3), with weights $\alpha_{\mathrm{sf}}+1$, resp. $\alpha_{\mathrm{sf}}$; that is,
with the decay order $\mathsf s_\sigma+\alpha_{\mathrm{sf}}+1$ in both cases, and with margin at the thresholds.

(b) $\mathsf r$ (with weight $\alpha_{\mathrm{sf}}+1$) and $\mathsf b$ are admissible for $z_0$ in the sense of I.B
section 1.4, and $\mathsf r_\sigma$ is $\mathsf r_h(x,\xi) = \mathsf r(x,h\xi)$ at $h = |\sigma|^{-1}$ (I.B section 8.4).

(c) $\mathsf r_\sigma$ is the dilated order $\mathsf r_\varsigma$ of I.C Definition 6.1, $\varsigma = |\sigma|$; and
$(s_c+1,
\mathsf r+1)$ with weight $\alpha_+ := \alpha_{\mathrm{sf}}$ is admissible at $\sigma_0 = \pm1$ and, by (C3), near it,
which is what III.H Corollary 4.2 and Theorem 4.1 (3) use on $\Sigma' = \Sigma_0\cap\mathbb R$ (I.C's orders are
admissible on $J_\pm = \{|\sigma_0\mp1|<\frac14\}$, which enters off the real axis; there only pairings are used,
section 4).

*Proof.* Under $\Phi_{z_0}$ the radial sets correspond: $\partial R_{\mathcal H^+}$ (at fibre infinity, inside
$\{\sigma = 0\}$), $\partial R_{\partial K^+,\mathrm{in}}$ and $\partial R_{\partial K^+,\mathrm{out}}$ are the images of
$\partial\mathcal R_\pm$, $R_{z_0,\mathrm{in}}$ and $R_{\mathrm{out}}$, as sources and sinks of corresponding flows (II.B
Lemma 2.3), and the thresholds agree: $\vartheta^{3b}_{\mathrm{in}} = \vartheta_{\mathrm{in}}$ and
$\vartheta_{\mathrm{out}}\le2\bar S$ (II.C Lemma 2.6). Constancy: near $\partial\mathcal R_\pm$ by (C1), near
$\Gamma_{z_0}$ and over $\{r_0-\delta_0\le r\le r_2-\delta_0\}$ by II.C Definition 2.4 (3) and (C2), near
$R_{z_0,\mathrm{in}}$ and $R_{\mathrm{out}}$ by II.C Definition 2.4 (5)-(6). Monotonicity on a neighbourhood of the
characteristic set: (C3). As $\mathsf s$ is $t_*$-invariant and $G$ is $t_*$-independent, $\mathsf H_G\mathsf s$ at
$\sigma = z_0$ is $\mathsf H_{G_{z_0}}S_{z_0}$ identically, and II.B (1.4)'s and I.B's $\mathsf H_{z_0}$ are, up to
terms vanishing on the characteristic set (which shrink the neighbourhood), positive multiples of these Hamilton fields;
so (C3) transfers to a neighbourhood in $\mathcal P$ (II.B Lemma 2.3 relates the fields on $\Sigma_{z_0}$). Thresholds:
by II.C Definition 2.4 (4)-(6) with $\alpha_K = -2$ and margin 1, $s_c>\frac32+\vartheta_{\mathcal H}$; $\mathsf
r+\alpha_{\mathrm{sf}}>\frac12(-1+\vartheta_{\mathrm{in}})-1$ at $R_{z_0,\mathrm{in}}$; $\mathsf
r+\alpha_{\mathrm{sf}}<\frac12(-1+\vartheta_{\mathrm{out}})-3\le-\frac12+\bar S-3$ at $R_{\mathrm{out}}$. Hence $\mathsf
r+\alpha_{\mathrm{sf}}+1$ lies strictly between $\frac12(-1+\vartheta_{\mathrm{in}})$ at $R_{z_0,\mathrm{in}}$ and
$-\frac12+\bar S$ at $R_{\mathrm{out}}$, and $s_c$, $s_c+1>\frac12+\vartheta_{\mathcal H}$: (O3) and the thresholds of
I.B section 1.4 hold. (b) is then I.B section 1.4, and its identification is section 8.4 there. (a): I.B section 1.4
asks more than I.A (O2), and $(s_c,\mathsf r_h)$ is admissible for $\sigma_0 = z_0/h$ for every $h>0$ (I.B section 1.4,
last sentence), that is, for every real $\sigma\ne0$. (c): I.C Lemma 6.2 (c), $\mathsf r$ being admissible for $z_0$ and
constant near $R_{\mathrm{out}}$ with the threshold there. $\square$

*Neighbourhoods.* $\mathcal B$ is the neighbourhood of $b_0$ of III.H Corollary 4.4 (invertibility of
$\widehat{L_b}(\sigma)$ for all $\sigma\ne0$, $\mathrm{Im}\,\sigma\ge0$), on which III.H Corollaries 4.2-4.3 hold. For
$k\in\mathbb N_0$, $\mathcal B^{\mathrm{hi}}_k$ is a neighbourhood of $b_0$ on which $\delta_\Gamma(0)<\frac1{2(k+1)}$
(III.F Proposition 4.1, which gives $\delta_\Gamma(0)$ as small as wished on a neighbourhood, and at $b_0$ for every
bound); $\mathcal B_k := \mathcal B\cap\mathcal B^{\mathrm{hi}}_k$, so $b_0\in\mathcal B_k$ for every $k$.

**Theorem 1.3 ([Hin26] Theorem 10.1 at n = 4).** Let $\alpha_{\mathrm{sf}}$ be as in (1.1), $k\in\mathbb N_0$,
$b\in\mathcal B_k$ and $\mathsf s\in\mathcal O_c$. For
$f\in H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}(\Omega,|dt_*dx|;S^2T^*)^{\bullet,-}$ the forward solution $u$
of $L_bu = f$ satisfies
$$\|u\|_{H^{(\mathsf s-1;k),(\alpha_{\mathrm{sf}},-2)}_{3b;b}(\Omega)^{\bullet,-}}\le C\|f\|_{H^{(\mathsf
s;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}(\Omega)^{\bullet,-}}.\tag{1.2}$$
So, with II.C Definition 2.7 in its relaxed form with margin $d_\aleph = 1$: $L_{b_0}$ is 2-admissible with sf-weight
$\alpha_{\mathrm{sf}}$, sf-loss 0 and margin 1, for orders in $\mathcal O_c$ (a restriction of Definition 2.7, which asks
all admissible orders; Part II's uses must take orders in $\mathcal O_c$, (H$'$7)) ((1) by III.F Proposition 4.1, (2) by
III.F$'$ Proposition 3.3 at the weight $\alpha_{\mathrm{sf}}+2$, (3) by (1.2)); and for $b\in\mathcal B_K$, $b\ne b_0$,
(3) holds for $k\le K$.

The source's (10.3) has $\mathsf s-1$ and $(\alpha_{\mathrm{sf}}-\delta,-2)$ with $\delta>\alpha_{\mathrm{sf}}+\frac32$;
(1.2) has $\delta = 0$ ((H$'$1)). The proof is in section 7.

## 2. The representation of the forward solution

By density ([Hin26] p. 212) it suffices to take $f\in C^\infty_c(\Omega^\circ;S^2T^*)$, with $t_*\ge t_1>1$ on
$\mathrm{supp}\,f$; then $\hat f(\sigma) := \int e^{i\sigma t_*}f\,dt_*$ is entire with values in $C^\infty_c(X^\circ)$
and $\|\hat f(\sigma)\|\le C_N\langle\sigma\rangle^{-N}e^{-t_1\mathrm{Im}\,\sigma}$ in every norm, for
$\mathrm{Im}\,\sigma\ge0$. Fix $k$, $b\in\mathcal B_k$, $\mathsf s\in\mathcal O_c$. Let $c\in(0,\varsigma_1]$
($\varsigma_1$ of II.G$'$ (4.5a)) be at most the $c_{j,k'}$ of III.H Theorem 4.1 (3) for $\tilde L_b$ on $\Sigma' =
\Sigma_0\cap\mathbb R$ with the orders $(s_c+1,\mathsf r+1)$ of Lemma 1.2 (c), $j+k'\le k$ (III.H Corollary 4.3), and
fix $\chi\in C^\infty_c([0,c))$ with $\chi = 1$ on $[0,\frac c2]$. Put $\gamma_- := (-\infty,-\frac c2]$, $\gamma_0 :=
\frac c2e^{i[\pi,0]}$, $\gamma_+ := [\frac c2,\infty)$.

**Lemma 2.1 (the source's (10.4)).** The forward solution $u$ of $L_bu = f$ satisfies $\hat u(\sigma) =
\widehat{L_b}(\sigma)^{-1}\hat f(\sigma)$ for $\mathrm{Im}\,\sigma>0$ and
$$u(t_*,\cdot) = \frac1{2\pi}\int_{\gamma_-\cup\gamma_0\cup\gamma_+}e^{-i\sigma t_*}\widehat{L_b}(\sigma)^{-1}\hat
f(\sigma)\,d\sigma,\tag{2.1}$$
as distributions on $\mathbb R_{t_*}\times X^\circ$.

*Proof.* The argument of [Hin26c] Theorem 12.2 ([Hin26] p. 200), with these inputs. *High energy.* For $|\sigma|\ge C_0$,
$\mathrm{Im}\,\sigma\ge0$, $\widehat{L_b}(\sigma)$ is invertible (I.B Theorem 1.3 (3)), and $\|\widehat{L_b}(\sigma)^{-1}
g\|\le C|\sigma|^{-1+\delta}\|g\|$ in the norms of (1.8) there ($j = k = 0$), $\delta = \delta_\Gamma(\mathrm{Im}\,
\sigma-\epsilon)\le1$, uniformly for $\mathrm{Im}\,\sigma$ in compact sets, and $\delta = 0$ for $\mathrm{Im}\,\sigma$
large; at fixed $|\sigma|$ the semiclassical norms are equivalent to the fixed ones with constants polynomial in
$|\sigma|$. *Paley-Wiener.* Let $\gamma\ge C_0$ be large and $\tilde u(t_*) := \frac1{2\pi}\int_{\mathrm{Im}\,\sigma =
\gamma}e^{-i\sigma t_*}\widehat{L_b}(\sigma)^{-1}\hat f(\sigma)\,d\sigma$, absolutely convergent by the decay of $\hat
f$. By holomorphy on $\{\mathrm{Im}\,\sigma\ge\gamma\}$ and the bounds there, the integral does not depend on $\gamma'
\ge\gamma$; for $t_*<t_1$ the integrand is $O(\langle\sigma\rangle^{-N}e^{(t_*-t_1)\gamma'})$, so letting $\gamma'\to
\infty$, $\tilde u = 0$ for $t_*<t_1$. As $\partial_{t_*}$ becomes $-i\sigma$ (III.A (2.2)), $L_b\tilde u = f$ by Fourier
inversion on $\mathrm{Im}\,\sigma = \gamma$. $\widehat{L_b}(\sigma)^{-1}\hat f(\sigma)$ lies in $\mathcal X_\sigma$ for
every admissible choice of orders (I.A Theorem 7.2 (3): the kernel and range do not depend on them), so $\tilde u$ is
smooth, with $e^{\gamma t_*}$ growth; $\tilde u-u$ solves $L_b(\tilde u-u) = 0$ and vanishes for $t_*<1$, so $\tilde u
= u$ by the uniqueness of II.E Proposition 3.4 on each slab $\{t_*\le T\}$. *Shifting.* $\widehat{L_b}(\sigma)^{-1}$
exists for every $\sigma\ne0$ with $\mathrm{Im}\,\sigma\ge0$ (III.H Corollary 4.4), is holomorphic in $\mathrm{Im}\,
\sigma>0$ (I.A Theorem 7.2 (6)) and polynomially bounded for $|\mathrm{Re}\,\sigma|\ge C_0$ uniformly in
$\mathrm{Im}\,\sigma\in[0,\gamma]$; with the decay of $\hat f$, Cauchy's theorem moves the contour to $\mathrm{Im}\,
\sigma = \gamma''\in(0,\gamma)$, and then to $\gamma_-\cup\gamma_0\cup\gamma_+$: on $|\mathrm{Re}\,\sigma|\ge\frac c2$,
$\widehat{L_b}(\sigma)^{-1}$ is continuous up to the real axis (I.A Theorem 7.2 (6) at each real $\sigma_*\ne0$, where it
is invertible), with the polynomial bounds above for dominated convergence. $\square$

## 3. High frequencies ([Hin26] Lemma 10.9 at n = 4)

**Lemma 3.1.** Let $u_{\mathrm{hi}}(t_*,\cdot) := \frac1{2\pi}\int_{\mathbb R\setminus[-\frac c2,\frac
c2]}e^{-i\sigma t_*}(1-\chi(|\sigma|))\widehat{L_b}(\sigma)^{-1}\hat f(\sigma)\,d\sigma$. Then
$$\|u_{\mathrm{hi}}\|_{H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}+1-2\epsilon,0)}_{3b;b}(M_0)}\le
C_\epsilon\|f\|_{H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}(\Omega)^{\bullet,-}}\tag{3.1}$$
for every $\epsilon>0$ below the margins of Lemma 1.2 (a).

This is the source's (10.44) with $\alpha_{\mathrm{sf}}+1-2\epsilon$ in place of $\alpha_{\mathrm{sf}}$; the source's
weight $\alpha_{\mathrm{sf}}$ would need the stronger incoming threshold ((H$'$2)).

*Proof.* Write $\beta := \alpha_{\mathrm{sf}}+1$. By II.A Lemma 5.2 ($\hat u_{\mathrm{hi}}$ is supported in $|\sigma|\ge
\frac c2$; on $\frac c2\le|\sigma|\le1$ the sc-b norm at $\sigma$ and the semiclassical norm at $h = |\sigma|^{-1}$ are
both equivalent to the fixed norm, uniformly on this compact set: the parametrised calculus, II.A (S7)),
$$\|u_{\mathrm{hi}}\|^2\sim\sum_{j_1+j_2\le k}\int_{|\sigma|\ge\frac c2}\|\sigma^{j_1}(\sigma\partial_\sigma)^{j_2}\hat
u_{\mathrm{hi}}(\sigma)\|^2_{(\mathsf s_\sigma;k-j_1-j_2),\mathsf s_\sigma+\beta,\mathsf s_\sigma}\,d\sigma,$$
in the semiclassical norms of II.A Lemma 5.2 with $h = |\sigma|^{-1}$. By Leibniz,
$(\sigma\partial_\sigma)^{j_2}\hat u_{\mathrm{hi}}$ is a combination of bounded functions of $\sigma$ (from $1-\chi$)
times $\big((\sigma\partial_\sigma)^{j'}\widehat{L_b}^{-1}\big)(\sigma)(\sigma\partial_\sigma)^{j_3}\hat f(\sigma)$,
$j'+j_3\le j_2$. *$|\sigma|\ge C_0$.* I.B Theorem 1.3 (5) with the orders of Lemma 1.2 (b), weight $\beta$, $j'$ and $k-
j_1-j_2$: with $\delta := \delta_\Gamma(-\epsilon)$,
$$\|(\sigma\partial_\sigma)^{j'}\widehat{L_b}(\sigma)^{-1}g\|_{(s_c;k-j_1-j_2),\mathsf r+\beta,\mathsf b;+}\le
C|\sigma|^{-1+(j'+1)\delta}\|g\|_{(s_c-1;k-j_1-j_2+j'),\mathsf r+\beta+1,\mathsf b;+},$$
the left side bounding the norm above ($s_c+j'\ge s_c$; the subscript $+$ only adds terms). The $+$ norm on the right is
at most $C\sum_{j_4\le k-j_1-j_2+j'}|\sigma|^{j_4}\|g\|_{(s_c-1;k-j_1-j_3-j_4),\mathsf r+\beta+1,\mathsf b}$ (it tests in
addition with multiplication by $h^{-1} = |\sigma|$), and $(s_c-1)$-norms are bounded by $s_c$-norms. As $\delta_\Gamma$
is continuous and $\delta_\Gamma(0)<\frac1{2(k+1)}$ on $\mathcal B^{\mathrm{hi}}_k$, $\epsilon>0$ can be fixed with
$(k+1)\delta\le1$; then $|\sigma|^{2(j_1-1+(j'+1)\delta+j_4)}\le|\sigma|^{2(j_1+j_4)}$, and the integrand is bounded by
$C\sum|\sigma|^{2(j_1+j_4)}\|(\sigma\partial_\sigma)^{j_3}\hat f(\sigma)\|^2_{(\mathsf s_\sigma;k-j_1-j_3-j_4),\mathsf
s_\sigma+\beta+1,\mathsf s_\sigma}$, with $j_1+j_4+j_3\le k$. *$\frac c2\le|\sigma|\le C_0$.* $\widehat{L_b}(\sigma)$ is
invertible there (III.H Corollary 4.4). As $\sigma\mapsto
\mathsf r_\sigma$ is continuous into $C^\infty$, the compact set is covered by finitely many intervals $I_m\ni\sigma_m$
on which $|\mathsf r_\sigma-\mathsf r_{\sigma_m}|\le\epsilon$ and on which the fixed pair $(s_c,\mathsf r_{\sigma_m}-
\epsilon)$ is admissible for every $\sigma\in I_m$ with weight $\beta$ (the margins of Lemma 1.2 (a) exceed $\epsilon$,
and the constancy neighbourhoods and (C3)'s neighbourhood of the characteristic set persist for $\sigma$ near $\sigma_m$;
I.A Lemma 7.1). With these orders held fixed, I.A Theorem 7.2 (6) gives (7.1) and (7.3) without their last terms
uniformly for $\sigma\in I_m$, and the proof of (7.6), which uses only these, gives $\partial_\sigma^{j'}\widehat{L_b}
(\sigma)^{-1}:\bar H^{(s_c-1;k'+j'),\mathsf r_{\sigma_m}-\epsilon+\beta+1}\to\bar H^{(s_c+j';k'),\mathsf r_{\sigma_m}-
\epsilon+\beta}$ uniformly on $I_m$. As $\mathsf r_\sigma+\beta+1\ge\mathsf r_{\sigma_m}-\epsilon+\beta+1$ and
$\mathsf r_\sigma+\beta-2\epsilon\le\mathsf r_{\sigma_m}-\epsilon+\beta$ on $I_m$, the output is bounded in the decay
order $\mathsf r_\sigma+\beta-2\epsilon$ by the input in $\mathsf r_\sigma+\beta+1$: the loss $2\epsilon$ of (3.1).
$(\sigma\partial_\sigma)^{j'}$ is a combination of $\sigma^i\partial_\sigma^i$, $i\le j'$, with bounded coefficients. The
integrand is bounded as before, without powers of $|\sigma|$, and on $|\sigma|\ge C_0$ the bound at the weight $\beta$
gives it at $\beta-2\epsilon$. *Conclusion.* By II.A Lemma 5.2 again, with the weight
$\beta+1 = \alpha_{\mathrm{sf}}+2$, the integral is at most $C\|f\|^2_{H^{(\mathsf
s;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}}$. $\square$

$u_{\mathrm{hi}}$ is not supported in $\Omega$, so its norm is on $M_0$ (the source's footnote 100). The derivative
loss (regularity $\mathsf s$ for $f$ and for $u_{\mathrm{hi}}$) is the trapping loss.

## 4. Low frequencies: the regular part ([Hin26] Lemmas 10.10-10.11 at n = 4)

For $|\sigma|\le c$, $\sigma\ne0$, $\mathrm{Im}\,\sigma\ge0$, put (III.H Definition 3.1, Corollary 4.2)
$$\big(\hat u_{\mathrm{reg},1}(\sigma),\hat b_1(\sigma),\hat S_1(\sigma)\big) := \tilde
L_b(\sigma)^{-1}\big(\hat f(\sigma),0,0\big).\tag{4.1}$$
By III.H (4.6), for these $\sigma$,
$$\widehat{L_b}(\sigma)^{-1}\hat f(\sigma) = \hat u_{\mathrm{reg},1}(\sigma)+\hat g^{\mathrm{aug}}(\sigma)(\hat
b_1(\sigma))+\hat h^{\mathrm{aug}}(\sigma)(\hat S_1(\sigma)).\tag{4.2}$$
*Properties.* By the formula in the proof of III.H Theorem 4.1 (3), $(\hat b_1,\hat S_1) = M(\sigma)^{-1}(\langle
R(\sigma)\hat f(\sigma),\phi_j\rangle_h)_j$ (there with $e = 0$), with $R = \widehat{L_b}^{-1}$ and $M(\sigma)_{ji}
= \langle R(\sigma)F_i(\sigma),\phi_j\rangle$; $R$ is holomorphic in $\mathrm{Im}\,\sigma>0$ (I.A Theorem 7.2 (6)), the
columns $F_i = \hat f_{\dot b},\hat f_S$ are holomorphic there with values in every $\bar H^{m,M}_{\mathrm b}$ (III.H
Lemma 2.4 (d)), and $\hat f$ is entire. So $\hat b_1$, $\hat S_1$ and $\hat u_{\mathrm{reg},1} = R(\sigma)(\hat f-\sum
c_iF_i)$ (paired with any $\phi\in C^\infty_c(X^\circ)$) are holomorphic in $\mathrm{Im}\,\sigma>0$, continuous down to
$[-c,c]\setminus0$ (I.A Theorem 7.2 (6) at real $\sigma_*$), and bounded uniformly by III.H (4.5) (with any orders of
I.C section 6: these are statements about pairings with test sections, which do not depend on the orders), as $\|\hat
f(\sigma)\|_{(s_c;k),(\mathsf r+\alpha_{\mathrm{sf}}+2,\alpha_{\mathrm{sf}}+2,0),|\sigma|}$ is bounded for $|\sigma|\le1$
($\hat f(\sigma)$ is supported in a fixed compact set of $X^\circ$, I.C Lemma 6.2 (a)).

**Lemma 4.1 (the regular part).** $u_{\mathrm{reg}}(t_*,\cdot) := \frac1{2\pi}\int_{\gamma_-\cup\gamma_0\cup
\gamma_+}e^{-i\sigma t_*}\chi(|\sigma|)\hat u_{\mathrm{reg},1}(\sigma)\,d\sigma$ satisfies
$$\|u_{\mathrm{reg}}\|_{H^{(\mathsf s+1;k),(\alpha_{\mathrm{sf}},0)}_{3b;b}(M_0)}\le
C\|f\|_{H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}(\Omega)^{\bullet,-}}.\tag{4.3}$$

The source has $\mathsf s$ on the left and $\mathsf s-1$ on the right; here $f$ is used at its regularity $\mathsf s$,
and the gain is the elliptic one ((H$'$2)).

*Proof.* As $\chi = 1$ on $[0,\frac c2]$ and the integrand is bounded near 0 and holomorphic inside $\gamma_0$, Cauchy's
theorem moves $\gamma_0$ to $[-\frac c2,\frac c2]$ (pairing with test sections; the small semicircle around 0 contributes
$o(1)$). So $\hat u_{\mathrm{reg}} = \chi\hat u_{\mathrm{reg},1}$ on $\mathbb R$, supported in $[-c,c]$. By II.A Lemma
5.2 with the order $\mathsf s+1$ and the weight $\alpha_{\mathrm{sf}}$, and II.A Lemma 5.3 (the norms of I.C Definition
6.1),
$$\|u_{\mathrm{reg}}\|^2\sim\sum_{j\le k}\int_{-c}^c\|(\sigma\partial_\sigma)^j(\chi\hat u_{\mathrm{reg},1})\|^2_{(s_c+1;
k-j),(\mathsf r+1+\alpha_{\mathrm{sf}},\alpha_{\mathrm{sf}},0),|\sigma|}\,d\sigma.$$
By Lemma 1.2 (c) and III.H Corollary 4.3, III.H Theorem 4.1 (3) applies to $\tilde L_b$ on $\Sigma' =
\Sigma_0\cap\mathbb R$ with the orders $(s_c+1,\mathsf r+1)$ and $\alpha_+ = \alpha = \alpha_{\mathrm{sf}}$: by Leibniz
and (4.2) of III.H, for $|\sigma|\le c$,
$$\|(\sigma\partial_\sigma)^j(\chi\hat u_{\mathrm{reg},1})\|_{(s_c+1;k-j),\dots}\le
C\sum_{j_2\le j}\|(\sigma\partial_\sigma)^{j_2}\hat f(\sigma)\|_{(s_c;k-j_2),(\mathsf r+1+\alpha_{\mathrm{sf}}+1,
\alpha_{\mathrm{sf}}+2,0),|\sigma|},$$
each derivative falling on $\tilde L_b^{-1}$ costing one order of b-regularity of $\hat f$. The decay order $\mathsf
r+\alpha_{\mathrm{sf}}+2$ and the regularity $s_c$ are those of $\mathsf s+\alpha_{\mathrm{sf}}+2$ and $\mathsf s$, so by
II.A Lemma 5.2 with the weight $\alpha_{\mathrm{sf}}+2$ the integral is at most $C\|f\|^2_{H^{(\mathsf
s;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}}$. $\square$

**Lemma 4.2 (the coefficients).** $\sum_{j\le k}\int_{-c}^c\big(|(\sigma\partial_\sigma)^j\hat b_1(\sigma)|^2
+|(\sigma\partial_\sigma)^j\hat S_1(\sigma)|^2\big)\,d\sigma\le C\|f\|^2_{H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}+2,
0)}_{3b;b}(\Omega)^{\bullet,-}}$.

*Proof.* As for Lemma 4.1, with the moduli of the second and third components in III.H (4.2). $\square$

## 5. The singular part ([Hin26] Lemma 10.12 at n = 4)

With $\hat g^{\mathrm{aug}}$, $\hat h^{\mathrm{aug}}$ of III.H (2.6), put
$$\dot g(t_*,\cdot) := \frac1{2\pi}\int_{\gamma_-\cup\gamma_0\cup\gamma_+}e^{-i\sigma t_*}\chi(|\sigma|)\hat
g^{\mathrm{aug}}(\sigma)(\hat b_1(\sigma))\,d\sigma,\qquad h_{\mathrm s1}(t_*,\cdot) := \frac1{2\pi}\int_{\gamma_-\cup
\gamma_0\cup\gamma_+}e^{-i\sigma t_*}\chi(|\sigma|)\hat h^{\mathrm{aug}}(\sigma)(\hat S_1(\sigma))\,d\sigma.\tag{5.1}$$
By Lemma 2.1, (4.2) and $\chi(|\sigma|) = 1$ on $\gamma_0$,
$$u = u_{\mathrm{hi}}+u_{\mathrm{reg}}+u_{\mathrm{sing}},\qquad u_{\mathrm{sing}} := \dot g+h_{\mathrm s1}.\tag{5.2}$$
On $\gamma_0$, $|e^{-i\sigma t_*}| = e^{t_*\mathrm{Im}\,\sigma}$, so (5.1) grows at most like $e^{ct_*/2}$; the poles of
$\hat g^{\mathrm{aug}}$, $\hat h^{\mathrm{aug}}$ at 0 prevent moving $\gamma_0$ to the real axis. Their
$t_*$-derivatives do not have them.

**Lemma 5.1 (bounds for derivatives).** For every $m,k\in\mathbb N_0$,
$$\partial_{t_*}\dot g\in H^{(m;k),(\alpha_{\mathrm{sf}}+1,0)}_{3b;b}(M_0),\qquad\partial^2_{t_*}h_{\mathrm s1}\in
H^{(m;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}(M_0),\tag{5.3}$$
with norms at most $C_m\|f\|_{H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}(\Omega)^{\bullet,-}}$.

The source's (10.51)-(10.52) have the sf-weights $-\frac12-\epsilon$ and $\frac12-\epsilon$ and the regularity $\mathsf
s$ only, under the condition $\mathsf s'+\alpha'<-\frac12$ at $R_{\mathrm{out}}$; here any constant regularity and no
condition at $R_{\mathrm{out}}$, as the transforms decay rapidly at scf.

*Proof.* *The transforms.* Differentiating (5.1) under the integral, $\partial_{t_*}$ brings $-i\sigma$, and by III.H
(2.6), $-i\sigma\hat g^{\mathrm{aug}}(\sigma)(\dot b) = \Psi(\sigma,\cdot)\dot g(\dot b)$ and
$$-\sigma^2\hat h^{\mathrm{aug}}(\sigma)(S) = \big(\Psi-\sigma\partial_\sigma\Psi\big)h(S)-i\sigma\Psi\,\breve
h(S),\tag{5.4}$$
with $\Psi(\sigma,x) = \int e^{i\sigma t_*}\partial_{t_*}\chi_K\,dt_*$, entire in $\sigma$ for each $x$ (the support of
$\partial_{t_*}\chi_K(\cdot,x)$ is compact). So $\partial_{t_*}\dot g = \frac1{2\pi}\int e^{-i\sigma t_*}\chi\,\Psi\dot
g(\hat b_1)\,d\sigma$ over the same contour, and the integrand is bounded near 0 and holomorphic inside $\gamma_0$; as in
Lemma 4.1, $\gamma_0$ moves to $[-\frac c2,\frac c2]$, and $\mathcal F(\partial_{t_*}\dot g) = \chi\Psi\dot g(\hat b_1)$
on $\mathbb R$. Likewise $\mathcal F(\partial^2_{t_*}h_{\mathrm s1})$ is $\chi$ times (5.4) at $S = \hat S_1$.

*Uniform bounds.* For $r\ge1$, $\Psi = \Phi(\sigma r)$ (III.H Lemma 2.5 (b)), $\Phi$ entire with $|\partial^j_\zeta\Phi|
\le C_{j,N}\langle\zeta\rangle^{-N}$ on $\{\mathrm{Im}\,\zeta\ge0\}$. So, with $\zeta = \sigma r$,
$$\Psi\dot g = r^{-2}\Phi(\zeta)\big(r^2\dot g\big),\qquad(5.4) = r^{-3}\Big(\big(\Phi(\zeta)-\zeta\Phi'(\zeta)\big)r^3h-
i\zeta\Phi(\zeta)\,r^2\breve h\Big),$$
where $r^2\dot g$, $r^3h$, $r^2\breve h$ are bounded with all b-derivatives (weights 2 or 3, 3 and 2; III.H section 1).
Each is $r^{-q}G(\sigma r,x)$ with $q = 2$, resp. 3, and $G$ smooth, with $|(\zeta\partial_\zeta)^j(r\partial_r)^a
\partial_\omega^\beta G|\le C\langle\zeta\rangle^{-N}$ for $\zeta$ real; $\sigma\partial_\sigma$ acts as
$\zeta\partial_\zeta$. The proof of III.H Lemma 2.4 (b), with $r^{-3}$ replaced by $r^{-q}$, gives
$\sup_{0<|\sigma|\le1}\|(\sigma\partial_\sigma)^j(\cdot)\|_{H^{k',(N,\beta_{\mathrm{tf}},0)}_{\mathrm
b,|\sigma|}}<\infty$ for every $k'$, $N$ and $\beta_{\mathrm{tf}}<q$ (the bound
$\rho_{\mathrm{tf}}^{q-\beta_{\mathrm{tf}}}$ is square integrable for $\mu_{\mathrm b}$ uniformly iff
$\beta_{\mathrm{tf}}<q$); for $r\le1$, $\Psi$ and its $\sigma$- and $x$-derivatives are
bounded uniformly for $|\sigma|\le1$ (the proof of III.H Lemma 2.5 (d): $\partial^j_\sigma\Psi = \int(it_*)^je^{i\sigma
t_*}\partial_{t_*}\chi_K\,dt_*$). By II.G$'$ (4.5a), with $l+4 =
\beta_{\mathrm{tf}}$, for every constant order pair, for $|\sigma|\le\varsigma_1$ ($c\le\varsigma_1$, section 2):
$$\sup_{0<|\sigma|\le c}\sum_{j\le k}\|(\sigma\partial_\sigma)^j(\Psi\dot g(e_i))\|_{(m;k),(m+\beta',\beta',0),|\sigma|}+
\|(\sigma\partial_\sigma)^j(5.4)(e'_i)\|_{(m;k),(m+\beta'',\beta'',0),|\sigma|}<\infty$$
for basis elements $e_i$, $e'_i$, every $m$, $\beta'<0$ and $\beta''<1$. Take $\beta' := \alpha_{\mathrm{sf}}+1<0$ and
$\beta'' := \alpha_{\mathrm{sf}}+2<1$ ((1.1)).

*Inverse transform.* By II.A Lemma 5.2 with the constant order $m$ and the weight $\beta'$, and Leibniz,
$$\|\partial_{t_*}\dot g\|^2\sim\sum_{j\le k}\int_{-c}^c\|(\sigma\partial_\sigma)^j(\chi\Psi\dot g(\hat
b_1))\|^2_{(m;k-j),(m+\beta',\beta',0),|\sigma|}d\sigma\le C\sum_{j\le k}\int_{-c}^c|(\sigma\partial_\sigma)^j\hat
b_1|^2d\sigma,$$
and Lemma 4.2 bounds the right side; likewise for $\partial^2_{t_*}h_{\mathrm s1}$ with $\beta''$ and $\hat S_1$.
$\square$

Uniformly for $b$ near $b_0$ the same holds by III.H Remark 2.6, as $\beta'<0$ and $\beta''<1$ hold with room.

## 6. Integration in $t_*$ ([Hin26] Lemma 10.13 at n = 4)

**Lemma 6.1 (translation-invariant elliptic operators).** Let $\mathsf s\in C^\infty({}^{3b}S^*\tilde M_0)$ be
$t_*$-translation-invariant, $J\in\mathbb N$ and $\theta_0>0$. There are $t_*$-translation-invariant operators
$A\in\tilde\Psi^{\mathsf s}_{3b}$, elliptic, $B'\in\tilde\Psi^{-\mathsf s}_{3b}$ and $R\in\tilde\Psi^{-J}_{3b}$ with
$$I = B'A+R^2,\tag{6.1}$$
whose Schwartz kernels are supported in $\{|t_*-t'_*|\le\theta_0\langle x\rangle,\ |x-x'|\le\theta_0\langle x\rangle\}$.
They act on $H^{\mathsf s',(\beta,\gamma)}_{3b}$ with the orders shifted by their own, for all $\beta,\gamma$. (Only $k
= 0$: for variable orders, commutators with b-vector fields carry logarithmic factors; Lemma 6.2 reduces to $k = 0$
first.)

*Proof.* In the frame $\langle x\rangle\partial_{t_*}$, $\langle x\rangle\partial_{x_i}$, which is $t_*$-invariant, a 3b
covector has fibre coordinates $\zeta\in\mathbb R^5$, and a $t_*$-translation-invariant function on the 3b-cotangent
bundle is a function of $(x,\zeta)$; in particular $\mathsf s = \mathsf s(x,\zeta)$. For a symbol $a(x,\zeta)$ of
variable order (II.A's symbol classes) put, with $\psi\in C^\infty_c(\mathbb R^5)$ equal to 1 near 0, supported in
$\{|y|\le\theta_1\}$,
$$\mathrm{Op}(a)u(t_*,x) := (2\pi)^{-5}\int e^{i((t_*-t'_*)\tau+(x-x')\cdot\xi)}\psi\Big(\frac{(t_*-t'_*,x-x')}{\langle
x\rangle}\Big)a\big(x,\langle x\rangle(\tau,\xi)\big)u(t'_*,x')\,dt'_*dx'\,d\tau\,d\xi.$$
In a unit cell of the scaled bounded geometry (II.A (S9); cells of size $\langle x_\alpha\rangle$), after rescaling by
$\langle x_\alpha\rangle$, this is the quantization with the cut-off of [SBG] (3.26) (II.A section 8.3) of the symbol
$a(x,(\langle x\rangle/\langle x_\alpha\rangle)\tilde\zeta)$, which lies in the same class ($\langle x\rangle/\langle
x_\alpha\rangle$ is bounded above and below with bounded scaled derivatives), with the cut-off rescaled by the same
factor; a change of cut-off changes the operator by one with smooth kernel supported within bounded cell distance and
rapidly decaying in the scaled variables, a residual operator localized near the diagonal. So $\mathrm{Op}(a)\in\tilde
\Psi^{\mathrm{ord}\,a}_{3b}$, localized near the diagonal (kernel range $\theta_1\langle x\rangle$). Its kernel depends
on $(t_*-t'_*,x,x')$, so $\mathrm{Op}(a)$ commutes with $t_*$-translations; compositions of such operators commute with
them and have kernel ranges that add. Take $a := \langle\zeta\rangle^{\mathsf s}$, $A := \mathrm{Op}(a)$,
$B_0 := \mathrm{Op}(a^{-1})$. Then $B_0A = I-R_1$ with $R_1\in\tilde\Psi^{-(1-2\delta)}_{3b}$ (the calculus with variable
orders loses $\delta>0$ in the remainder), translation-invariant. With $J'(1-2\delta)\ge J$, $B := \sum_{j<J'}R_1^jB_0$
gives $BA = I-R_1^{J'} =: I-R$, and $I = BA+R = (B+RB)A+R^2$: $B' := B+RB$. All are translation-invariant, with kernel
range at most $4J'(1+\theta_1)\theta_1\langle x\rangle\le\theta_0\langle x\rangle$ for $\theta_1$ small (compositions
add ranges, with $\langle x'\rangle\le(1+\theta_1)\langle x\rangle$ on them). For the weights $w =
\rho_{\mathrm{sf}}^\beta\rho_K^\gamma$, $w^{-1}Aw$ has kernel $K_A(z,z')w(z')/w(z)$, and on the kernel's support
$w(z')/w(z)$ is smooth, bounded with bounded scaled derivatives (the logarithmic 3b-derivatives of
$\rho_{\mathrm{sf}},\rho_K$ are bounded): an operator of the same class. $\square$

**Lemma 6.2 ([Hin26] Lemma 10.13 at n = 4).** Let $\mathsf s$ be a $t_*$-translation-invariant 3b order, constant over
$\{r\le r_0+1\}$ (as orders in $\mathcal O_c$ are, by II.C Definition 2.4 (3)), $k\in\mathbb N_0$, $\beta\in\mathbb R$,
$\ell>\frac12$. If $u$ is a distribution on $M_0^\circ$ with
$$u|_{\Omega_-}\in\bar H^{(\mathsf s;k),(\beta-1,-\ell)}_{3b;b}(\Omega_-),\qquad\partial_{t_*}u\in H^{(\mathsf
s;k),(\beta,-\ell+1)}_{3b;b}(M_0),$$
then $u\in H^{(\mathsf s;k),(\beta-1,-\ell)}_{3b;b}(M_0)$, with norm at most $C$ times the sum of those two norms. The
density is $|dt_*|$ times any weighted b-density on $X$ (a change of density is a shift of $\beta$).

*Proof.* *Cut-off.* Let $\chi\in C^\infty(\mathbb R)$ equal 1 on $[-\frac14,\infty)$ and 0 on $(-\infty,-\frac12]$, and
$u' := \chi(t_*/r)u$. Then $u-u'$ is supported in $\{t_*\le-r/4\}\subset\Omega_-$, away from $\{t_* = 1\}$, so it lies in
$H^{(\mathsf s;k),(\beta-1,-\ell)}_{3b;b}(M_0)$; $\chi(t_*/r)$ is homogeneous of degree 0, a 3b multiplier; and
$\partial_{t_*}u' = \chi(t_*/r)\partial_{t_*}u+r^{-1}\chi'(t_*/r)u$, whose last term is supported in $\Omega_-$ away from
$\{t_* = 1\}$ and $K^\pm$ and lies in $H^{(\mathsf s;k),(\beta,-\ell+1)}_{3b;b}$ ($r^{-1} = \rho_{\mathrm{sf}}$ there).
So we may assume $u = 0$ for $t_*\le-r/2$, and then only $\partial_{t_*}u =: f$ enters. *b-regularity.*
$\partial_{t_*}$ and $\langle x\rangle\partial_x$ commute with $\partial_{t_*}$, and $\partial_{t_*}(t_*\partial_{t_*}u)
= t_*\partial_{t_*}f+f$, preserving the support condition; by induction it suffices to take $k = 0$.

*The case $\mathsf s = 0$, with $u = 0$ for $t\le\theta r$, $t := t_*+r$, $\theta\in(0,1)$.* On $\{t\ge\theta r\}$,
$\rho_{\mathrm{sf}} = r^{-1}$ and $\rho_K = r/t$ are defining functions up to bounded factors ($r\ge r_0$). As
$\partial_{t_*}$ commutes with powers of $r$ we may take $\beta = 0$; dropping the angular variables (the density is
$|dt\,dr|$ after the shift of $\beta$), $f = \rho_K^{1-\ell}f_0 = r^{1-\ell}t^{\ell-1}f_0$ with $f_0\in L^2(|dt\,dr|)$,
and $u(t,r) = \int_{\theta r}^tf(t',r)\,dt'$. Fix $\alpha\in(-\frac12,\ell-1)$ (possible as $\ell>\frac12$). Then
$$\|\rho_{\mathrm{sf}}\rho_K^\ell u\|^2 = \int_{r_0}^\infty\!\!\int_{\theta r}^\infty t^{-2\ell}\Big|\int_{\theta
r}^tt'^{\ell-1}f_0(t',r)\,dt'\Big|^2dt\,dr\le\int\!\!\int t^{-2\ell}\frac{t^{2\alpha+1}}{2\alpha+1}\int_{\theta
r}^tt'^{2\ell-2-2\alpha}|f_0|^2dt'\,dt\,dr,$$
by Cauchy-Schwarz with $t'^{\alpha}\cdot t'^{\ell-1-\alpha}$, and exchanging the integrals, $\int_{t'}^\infty
t^{-2\ell+2\alpha+1}dt = t'^{-2\ell+2\alpha+2}/(2\ell-2\alpha-2)$, so the right side is at most $C\|f_0\|^2_{L^2} =
C\|f\|^2 _{H^{0,(0,1-\ell)}_{3b}}$. Nothing here depends on the dimension.

*Near $r = r_0$.* Let $\chi_1 = \chi_1(r)$ equal 1 near $\{r = r_0\}$ and vanish on $\{r\ge\min(r_0+1,\frac32r_0)\}$;
it commutes with $\partial_{t_*}$, so $\chi_1u$ and $(1-\chi_1)u$ both satisfy the hypotheses. For $(1-\chi_1)u$ the
argument below applies with $\theta_0$ so small that the kernels stay away from $\{r = r_0\}$. Over
$\mathrm{supp}\,\chi_1$ the order is a constant $s_0$; extend $\chi_1u$ across $\{r = r_0\}$ by an extension operator
$E$ acting in $x$ only (Seeley's reflection in $r$, into $\{r>\frac12r_0\}$, bounded on the extendible spaces of order
$s_0$ and on the weighted $L^2$ spaces), which commutes with $\partial_{t_*}$; $E\chi_1u$ is supported in $\{t_*\ge-C\}$
and at bounded $r$ the weights are those of $t_*$, so the argument below applies to it with the constant order $s_0$ and
$t := t_*+r+C'$ for a constant $C'$ making $t\ge\theta r$ on its support; restriction to $\{r\ge r_0\}$ is bounded. (The
source has the same point.)

*General $\mathsf s$.* Take $A,B',R$ of Lemma 6.1 with $J\ge\sup|\mathsf s|+|\inf\mathsf s|$ and $\theta_0$ so small that
$z\in\mathrm{supp}\,K_A$ or $\mathrm{supp}\,K_R$ (as a function of its first variable, its second in $\mathrm{supp}\,u
\subset\{t_*\ge-r/2\}$) forces $t_*\ge-\frac34r$, i.e. $t\ge r/4$ (with $\langle x\rangle\le Cr$ on $r\ge r_0$). The
operators are localized near the diagonal, hence act on all distributions, and (6.1) holds on them. $Au$ and $Ru$ vanish
for $t\le r/4$, and $\partial_{t_*}(Au) = Af\in H^{0,(\beta,-\ell+1)}_{3b}$, $\partial_{t_*}(Ru) = Rf\in H^{\mathsf s+J,
(\beta,-\ell+1)}_{3b}\subset H^{0,(\beta,-\ell+1)}_{3b}$; by the case $\mathsf s = 0$ with $\theta = \frac14$, $Au$,
$Ru\in H^{0,(\beta-1,-\ell)}_{3b}$, and $u = B'(Au)+R(Ru)\in H^{\mathsf s,(\beta-1,-\ell)}_{3b}$, with the estimate.
$\square$

The source proves the case $\mathsf s = 0$ and refers the rest to [Hin26c] Lemma 14.6, whose proof applies the case
$\mathsf s = 0$ to $Au$; this needs $A$ translation-invariant (so that $\partial_{t_*}Au = Af$) and localized near the
diagonal (so that $Au$ keeps a support condition), which Lemma 6.1 supplies ((H$'$6)).

## 7. Proof of Theorem 1.3

Let $f\in C^\infty_c(\Omega^\circ)$ as in section 2, and $u = u_{\mathrm{hi}}+u_{\mathrm{reg}}+u_{\mathrm{sing}}$ as in
(5.2). Write $\|f\| := \|f\|_{H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}(\Omega)^{\bullet,-}}$.

(i) By Lemmas 3.1 (with $\epsilon<\frac12$) and 4.1, $u_{\mathrm{hi}}+u_{\mathrm{reg}}\in H^{(\mathsf
s;k),(\alpha_{\mathrm{sf}},0)}_{3b;b}(M_0)$ with norm $\le C\|f\|$ (as
$\alpha_{\mathrm{sf}}<\alpha_{\mathrm{sf}}+1-2\epsilon$ and $\mathsf s<\mathsf s+1$).

(ii) $u = 0$ for $t_*<t_1$, $t_1>1$, so $u_{\mathrm{sing}} = -(u_{\mathrm{hi}}+u_{\mathrm{reg}})$ on $\Omega_-$:
$$u_{\mathrm{sing}}|_{\Omega_-}\in\bar H^{(\mathsf s;k),(\alpha_{\mathrm{sf}},0)}_{3b;b}(\Omega_-),\qquad\partial_{t_*}
u_{\mathrm{sing}}|_{\Omega_-}\in\bar H^{(\mathsf s-1;k),(\alpha_{\mathrm{sf}}+1,0)}_{3b;b}(\Omega_-).$$

(iii) By Lemma 5.1 with $m\ge\sup\mathsf s$, $\partial^2_{t_*}u_{\mathrm{sing}} = \partial_{t_*}(\partial_{t_*}\dot g)+
\partial^2_{t_*}h_{\mathrm s1}\in H^{(\mathsf s-1;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}(M_0)$.

(iv) Lemma 6.2 for $\partial_{t_*}u_{\mathrm{sing}}$, with the order $\mathsf s-1$, $\beta = \alpha_{\mathrm{sf}}+2$,
$\ell = 1$ (the data (ii) lie in $(\alpha_{\mathrm{sf}}+1,0)\subset(\beta-1,-1)$): $\partial_{t_*}u_{\mathrm{sing}}\in
H^{(\mathsf s-1;k),(\alpha_{\mathrm{sf}}+1,-1)}_{3b;b}(M_0)$.

(v) Lemma 6.2 for $u_{\mathrm{sing}}$, with $\mathsf s-1$, $\beta = \alpha_{\mathrm{sf}}+1$, $\ell = 2$ (the data (ii)
lie in $(\alpha_{\mathrm{sf}},0)\subset(\beta-1,-2)$, at regularity $\mathsf s\ge\mathsf s-1$): $u_{\mathrm{sing}}\in
H^{(\mathsf s-1;k),(\alpha_{\mathrm{sf}},-2)}_{3b;b}(M_0)$.

(vi) So $u\in H^{(\mathsf s-1;k),(\alpha_{\mathrm{sf}},-2)}_{3b;b}(M_0)$ with norm $\le C\|f\|$, every bound being linear
in $\|f\|$; as $u$ is supported in $\Omega$, this is (1.2). For general $f$, (1.2) follows by density and the uniqueness
of forward solutions (II.E Proposition 3.4). $\square$

Each step needed only the weights of (1.1): $\alpha_{\mathrm{sf}}+1<0$ in (iii) through $\beta'$, and
$\alpha_{\mathrm{sf}}+2<1$ through $\beta''$. At $n = 3$ the same steps stop at $\beta' = -\frac12-\epsilon$, below
$\alpha_{\mathrm{sf}}+1$, which is the source's loss.

## 8. Findings, labels and sources

### 8.1 Findings

(H$'$1) *No sf-loss at n = 4.* [Hin26] Theorem 10.1 has sf-loss $\delta>\alpha_{\mathrm{sf}}+\frac32$ at $n = 3$; at
$n = 4$, with $\alpha_{\mathrm{sf}}+2\in(0,1)$, the loss is 0 (Theorem 1.3). The reason is the states' extra order of
decay and the cone support of $\chi_K$ (III.H Lemma 2.5), by which the transforms of $\partial_{t_*}\dot g$ and
$\partial^2_{t_*}h_{\mathrm s1}$ are uniformly bounded at sf-weights $<0$ and $<1$ with rapid decay at scf (Lemma 5.1),
against the source's $-\frac12-\epsilon$, $\frac12-\epsilon$ and its condition at $R_{\mathrm{out}}$.

(H$'$2) *The incoming threshold.* II.C Definition 2.4 (6) with $\alpha_K = -2$ and margin 1 gives
$\mathsf s+\alpha_{\mathrm{sf}}>\frac12(-1+\vartheta_{\mathrm{in}})-1$ at the incoming radial set
($\vartheta^{3b}_{\mathrm{in}} = \vartheta_{\mathrm{in}}$, II.C Lemma 2.6), while the spectral estimates for
$u\in H^{\mathsf s,(\alpha_{\mathrm{sf}},0)}_{3b}$ need $\mathsf s+\alpha_{\mathrm{sf}}>\frac12(-1+
\vartheta_{\mathrm{in}})$ (I.A (1.5), I.B section 1.4). The source's Lemmas 10.9-10.10 measure $u_{\mathrm{hi}}$ and
$u_{\mathrm{reg}}$ at the weight $\alpha_{\mathrm{sf}}$ and regularity $\mathsf s$, which the hypothesis does not cover
when $\mathsf s+\alpha_{\mathrm{sf}}\le\frac12(-1+\vartheta_{\mathrm{in}})$ there; its Remark 10.2 checks only the
outgoing set, where the condition of Definition 2.4 (5) is $\mathsf s+\alpha_{\mathrm{sf}}<\frac12(-1+
\vartheta_{\mathrm{out}})+\alpha_K-1 = \frac12(-1+\vartheta_{\mathrm{out}})-3$ (the remark states $-\frac12-1$, without
$\alpha_K$). Here $u_{\mathrm{hi}}$ is measured at $\alpha_{\mathrm{sf}}+1$ (Lemma 3.1) and $u_{\mathrm{reg}}$ at
regularity $\mathsf s+1$ (Lemma 4.1): both use the margin, and nothing is lost in the end. The same change repairs the
source's argument at $n = 3$, as far as this reading goes.

(H$'$3) *The neighbourhood of $b_0$ depends on $k$.* The high-energy estimate with $k$ orders of b-regularity needs
$(k+1)\delta_\Gamma(-\epsilon)\le1$; strong trapping admissibility is proved at $b_0$ only (III.F Proposition 4.1), and
near $b_0$ it holds with $\delta_\Gamma(0)$ small on a neighbourhood $\mathcal B^{\mathrm{hi}}_k$ that shrinks with $k$.
Theorem 1.3 is therefore stated at $b_0$ for all $k$ and on $\mathcal B_K$ for $k\le K$. The source states Theorem 10.1
for $b$ near $b_0$ with its Proposition 8.3 (strong trapping admissibility near $b_0$ at $n = 3$).

(H$'$4) *The class of orders.* $\mathcal O_c$ adds to II.C Definition 2.4 the conditions (C1)-(C3) under which the
induced spectral orders satisfy the hypotheses of Part I: constant regularity (I.A (O1), Remark 1.1; I.C), constancy of
the semiclassical order over $\{r\le r_2-\delta_0\}$ and monotonicity on a neighbourhood of the characteristic set (I.B
section 1.4, [Hin26c] footnote 78). The source applies [Hin26c] Theorems 9.16 and 9.41 to the induced orders without
stating these.

(H$'$5) *Bounded frequencies.* On $\frac c2\le|\sigma|\le C_0$ the source cites only [Hin26c] Theorem 9.16 (5), a
high-energy statement; here I.A Theorem 7.2 (6), (7.6), with the invertibility of III.H Corollary 4.4, covers them. As
I.A's estimates are uniform only for orders held fixed near each point, the induced orders are frozen on finitely many
intervals, at a cost $2\epsilon$ in the weight of $u_{\mathrm{hi}}$ (Lemma 3.1), which section 7 does not feel.

(H$'$6) *[Hin26] Lemma 10.13 for variable orders.* Its reduction to $\mathsf s = 0$ through [Hin26c] Lemma 14.6 needs an
elliptic operator commuting with $\partial_{t_*}$ and localized near the diagonal (so that $Au$ keeps a forward support
condition, for which the case $\mathsf s = 0$ is proved with $t\ge\theta r$, any $\theta>0$); Lemma 6.1 constructs it by
a translation-invariant quantization in II.A's calculus.

(H$'$7) *Obligations for later parts.* The part that applies II.C Definition 2.7 at $n = 4$ ([Hin26c] Theorem 11.1, used
in [Hin26] section 11) must use orders in $\mathcal O_c$, and for $b\ne b_0$ the bound $k\le K$ of (H$'$3); in exchange
it may use sf-loss 0.

### 8.2 Labels

Proved: Lemmas 1.2, 2.1, 3.1, 4.1, 4.2, 5.1, 6.1, 6.2 and Theorem 1.3, given the parts cited. The comparisons with the
source are commentary. READ: [Hin26] Theorem 10.1, Remark 10.2 and section 10.2 (pp. 199-201, 212-217); [Hin26c] Lemma
14.6 and the proofs of Theorems 12.2 and 14.2 as cited there. Inputs: I.A (O1)-(O3), (1.5), Theorem 7.2 (3), (6);
I.B sections 1.4, 8.4 and Theorem 1.3 (3), (5); I.C Definition 6.1 and Lemma 6.2; II.A (S9), section 8.3, Lemmas 5.1-5.3
and 8.4; II.B Definition 2.2 and Lemma 2.3; II.C Definitions 2.4, 2.7 and Lemma 2.6; II.E Proposition 3.4; II.G$'$
(4.5a); III.A (2.2); III.F Proposition 4.1; III.F$'$ Proposition 3.3; III.H Lemmas 2.4-2.5, Remark 2.6, Definition 3.1,
Theorem 4.1 (3) and Corollaries 4.2-4.4.

### 8.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: Theorem 10.1, Remark 10.2,
section 10.2 (Lemmas 10.9-10.13, (10.42)-(10.64)).

[Hin26c] P. Hintz, (Non-)linear waves on asymptotically flat spacetimes. II: Lemma 14.6 and the proofs of Theorems 12.2
and 14.2.

[SBG] the scaled bounded geometry calculus as II.A cites it ((3.26)).
