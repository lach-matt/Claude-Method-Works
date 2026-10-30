# Part IV. Exterior estimates I: the edge-b structure and the basic energy estimate, n = 4 ([Hin23a] sections 3.1-3.2)

*Status.* Written (D301). Part IV writes out [Hin23a] section 3 at spatial dimension $n = 4$, on the exterior region of
III.C, for [Hin26]'s gauge-fixed operator. Its outputs are III.C$'$ Theorem 2.1 (with its continuation on a slab near
$\mathscr I^+$, III.K (K2)) and the energy estimates behind it. This first part covers the edge-b structure at $\mathscr
I^+$ (the source's sections 3.1-3.2: Definitions 3.1-3.3, Lemmas 3.6, 3.12-3.16, Corollary 3.14) and the basic energy
estimate (Proposition 3.17), together with the estimate near the interior of $I_0$ that the source cites from [HV20,
Proposition 4.3]. Later parts cover the tensor operator, the tame estimates and the Nash-Moser step (sections 3.3-3.6).
N1STAR-PROOF.md 10.64 records where $n$ enters; here each place is written into the proof. Source: [Hin23a]
(arXiv:2302.13804v1) pp. 9-17, read at source.

## 0. Setting and the edge-b calculus

*The region.* $U$, $(\rho_0,\rho_I,\omega)$, $X_0 = \rho_0\partial_{\rho_0}$, $X_I = \rho_I\partial_{\rho_I}$, the null
coordinates $x^0 = t+|x|$, $x^1 = t-|x|$ and $\rho = \rho_0\rho_I = |x|^{-1}$ are those of III.C section 1 (Lemma 1.1,
(1.2)-(1.5)), with $\omega\in\mathbb S^3$. Put $x_I := \rho_I^{1/2}$ and let $M_\sharp$ be $U$ with the smooth structure
in which $(\rho_0,x_I,\omega)$ are coordinates near $\mathscr I^+$ (the source's (3.6), there with $\rho_0$ and $x_I$ of
Schwarzschild's null coordinates). The faces of $M_\sharp$ at infinity are $I_0 = \{\rho_0 = 0\}$ and $\mathscr I^+ =
\{x_I = 0\}$, and $\mathscr I^+$ is fibred by $(\rho_0,\omega)\mapsto\omega$ over $\mathbb S^3$, with fibres the
$\rho_0$-lines (the source's Definition 3.7).

*Edge-b objects* ([Hin23a] Definitions 3.1-3.4, which are stated on any manifold with two faces and a fibration of one
of them, and involve no dimension). $\mathcal V_{\mathrm b}(M_\sharp)$ is spanned over $C^\infty(M_\sharp)$ by $X_0$,
$X_I = \frac12x_I\partial_{x_I}$ and the vector fields on $\mathbb S^3$. $\mathcal
V_{\mathrm{e,b}}(M_\sharp)\subset\mathcal V_{\mathrm b}(M_\sharp)$, the vector fields whose restriction to $\mathscr
I^+$ is tangent to its fibres, is spanned by $X_0$, $X_I$ and $x_I\Omega$, $\Omega\in\mathcal V(\mathbb S^3)$ (the
source's (3.9)). The operator classes $\mathrm{Diff}^{k,(\alpha_0,\alpha_1)}_{\mathrm{e,b}}$ and
$\mathrm{Diff}^{m;k}_{\mathrm{e,b;b}}$, the Sobolev spaces $H^{k,(\alpha_0,\alpha_1)}_{\mathrm{e,b}}$ and
$H^{(m;k),(\alpha_0,\alpha_1)}_{\mathrm{e,b;b}}$, the weights being powers of $\rho_0$ and $x_I$, and the classes
$\mathcal F\mathcal D$ of operators with coefficients in a space $\mathcal F$ are the source's. The b-spaces are those
of III.C. $\mathcal V_{\mathrm b}$ and the b-density are the same in the coordinates $\rho_I$ and $x_I$
($|d\rho_I/\rho_I| = 2|dx_I/x_I|$), and $x_I^{2\alpha} = \rho_I^\alpha$. So $H^{k,(\alpha_0,2\alpha_I)}_{\mathrm b}$ in
$(\rho_0,x_I)$ is III.C's $H^{k,(\alpha_0,\alpha_I)}_{\mathrm b}$ in $(\rho_0,\rho_I)$. In the source's (3.3), $\dim
M_\sharp = 5$:
$$H^{s,(\alpha_0,\alpha_1)}_{\mathrm b}(M_\sharp)\hookrightarrow\rho_0^{\alpha_0}x_I^{\alpha_1}L^\infty,\qquad
s>\tfrac52,\tag{0.1}$$
by the change of variables $z_0 = \log\rho_0$, $z_1 = \log x_I$ and Sobolev's embedding on $\mathbb R^2\times\mathbb
S^3$ (N1STAR-PROOF.md 10.64 X6: $s = 3$ serves at $n = 3$ and at $n = 4$).

*The metric.* $g_{b_0}$ is Schwarzschild-Tangherlini, $b_0 = (\mu_0,0)$ (III.B section 3), in the coordinates of III.B,
and $\eta = -dx^0dx^1+|x|^2\slashed g$ is Minkowski's. On $U$, the components of $g_{b_0}-\eta$ in the rescaled null
frame of III.C (1.6) lie in $\rho^2C^\infty(U)$ (III.C Lemma 1.3 and III.B (4.2)).

## 1. The frame as edge-b covectors ([Hin23a] Lemma 3.13, Corollary 3.14)

**Lemma 1.1.** For $\slashed\omega\in C^\infty(\mathbb S^3;T^*\mathbb S^3)$,
$$dx^0\in\rho_0^{-1}x_I^{-2}C^\infty(M_\sharp;{}^{\mathrm{e,b}}T^*M_\sharp),\quad
dx^1\in\rho_0^{-1}C^\infty(M_\sharp;{}^{\mathrm{e,b}}T^*M_\sharp),
\quad|x|\slashed\omega\in\rho_0^{-1}x_I^{-1}C^\infty(M_\sharp;{}^{\mathrm{e,b}}T^*M_\sharp),$$
and the products of the frame (1.6) of III.C have the source's orders (3.13): $(dx^0)^2\in\rho_0^{-2}x_I^{-4}C^\infty$,
$dx^0dx^1$ and $|x|^2\slashed h\in\rho_0^{-2}x_I^{-2}C^\infty$,
$dx^0\otimes_s|x|\slashed\omega\in\rho_0^{-2}x_I^{-3}C^\infty$, $(dx^1)^2\in\rho_0^{-2}C^\infty$,
$dx^1\otimes_s|x|\slashed\omega\in\rho_0^{-2}x_I^{-1}C^\infty$, sections of $S^2\,{}^{\mathrm{e,b}}T^*M_\sharp$.

*Proof.* By III.C (1.5), $\partial_0 = -\frac12\rho_0\rho_IX_I$ and $\partial_1 = \rho_0(X_0-X_I+\frac12\rho_IX_I)$, and
$|x|^{-1}e_a = \rho_0x_I\cdot x_Ie_a$ for an orthonormal frame $e_a$ of $\mathbb S^3$. So
$(\partial_0,\partial_1,|x|^{-1}e_a) = \rho_0\,D\,B\,(X_0,X_I,x_Ie_a)$ with $D =
\mathrm{diag}(x_I^2,1,x_I\mathrm{Id}_3)$ and
$$B = \begin{pmatrix}0&-\frac12&0\\1&-1+\frac12x_I^2&0\\0&0&\mathrm{Id}_3\end{pmatrix},\qquad\det B = \tfrac12.$$
$B$ is smooth and invertible up to $x_I = 0$, and $(X_0,X_I,x_Ie_a)$ is a frame of ${}^{\mathrm{e,b}}TM_\sharp$. The
dual coframe of $(\partial_0,\partial_1,|x|^{-1}e_a)$ is $(dx^0,dx^1,|x|e^a)$. So $(dx^0,dx^1,|x|e^a) =
\rho_0^{-1}D^{-1}(B^{-1})^T$ applied to the dual eb-coframe, which gives the three memberships, and the products follow.
$\square$

**Corollary 1.2 (the source's Lemma 3.12 and Corollary 3.14).**
$g_{b_0}\in\rho_0^{-2}x_I^{-2}C^\infty(M_\sharp;S^2\,{}^{\mathrm{e,b}}T^*M_\sharp)$ is nondegenerate of Lorentzian
signature up to $I_0\cup\mathscr I^+$, and
$$\rho_0^2x_I^2g_{b_0}\equiv2\Big(\frac{d\rho_0}{\rho_0}\Big)^2
+2\frac{d\rho_0}{\rho_0}\otimes_s\frac{d\rho_I}{\rho_I}+x_I^{-2}\slashed g,\qquad
\rho_0^{-2}x_I^{-2}g_{b_0}^{-1}\equiv2X_I\otimes_s(X_0-X_I)+x_I^2\slashed g^{-1},$$
modulo $x_IC^\infty(M_\sharp;S^2\,{}^{\mathrm{e,b}}T^*M_\sharp)$, resp.
$x_IC^\infty(M_\sharp;S^2\,{}^{\mathrm{e,b}}TM_\sharp)$.

*Proof.* For $\eta$: $dx^1 = \rho_0^{-1}\,d\rho_0/\rho_0$ and $d|x| = -|x|(d\rho_0/\rho_0+d\rho_I/\rho_I)$ from $x^1 =
2-\rho_0^{-1}$ and $|x| = (\rho_0\rho_I)^{-1}$; with $dx^0 = dx^1+2d|x|$,
$$\rho_0^2\rho_I\eta =
2\Big(\frac{d\rho_0}{\rho_0}\Big)^2+2\frac{d\rho_0}{\rho_0}\otimes_s\frac{d\rho_I}{\rho_I}
-\rho_I\Big(\frac{d\rho_0}{\rho_0}\Big)^2+\rho_I^{-1}\slashed g$$
exactly, and $\rho_I^{-1}\slashed g = x_I^{-2}\slashed g$ is a smooth eb-tensor ($d\omega/x_I$ being an eb-covector).
The dual statement for $\eta^{-1} = -4\partial_0\otimes_s\partial_1+|x|^{-2}\slashed g^{-1}$ follows from (1.5) of III.C
in the same way. By §0, the components of $g_{b_0}-\eta$ in the null frame are $O(\rho^2)$; by Lemma 1.1 the worst frame
product, $(dx^0)^2$, lies in $\rho_0^{-2}x_I^{-4}C^\infty$, and $\rho^2 = \rho_0^2x_I^4$. So $g_{b_0}-\eta\in C^\infty =
\rho_0^{-2}x_I^{-2}\cdot\rho_0^2x_I^2C^\infty$, which lies in the error class. Nondegeneracy and the signature follow
from the leading form, which is that of $\eta$. $\square$

*Remark 1.3 (the source's Remark 3.15).* As $\mathcal V_{\mathrm{e,b}}$ is a Lie algebra and differentiation along it
preserves $\rho_0^{\ell_0}x_I^{\ell_I}C^\infty$, the Koszul formula gives
$\nabla^{g_{b_0}}\in\mathrm{Diff}^1_{\mathrm{e,b}}$ on eb-tensor bundles, and
$$\Box_{g_{b_0}}\in\rho_0^2x_I^2\mathrm{Diff}^2_{\mathrm{e,b}}(M_\sharp;{}^{\mathrm{e,b}}T^{p,q}M_\sharp)\tag{1.1}$$
(the source's (3.14)). Nothing here depends on the dimension.

## 2. The scalar wave operator ([Hin23a] Lemma 3.16)

At $n = 4$ the conjugation that removes the first-order term is by $\rho^{3/2} = |x|^{-3/2}$, against the source's
$\rho$ at $n = 3$ (10.64 X1).

**Lemma 2.1 (the density).** $\mu_{\mathrm b} := \rho_0^5\rho_I^4|dg_{b_0}|$ is a smooth positive b-density on
$M_\sharp$. For $\eta$ it is exactly $|\frac{d\rho_0}{\rho_0}\frac{d\rho_I}{\rho_I}d\slashed g|$. The operator
$$L := \rho_I\rho^{-7/2}\,\Box_{g_{b_0}}\,\rho^{3/2}\tag{2.1}$$
is formally self-adjoint on $L^2(M_\sharp;\mu_{\mathrm b})$. (The source has $\rho_0^4\rho_I^3$ and
$\rho_I\rho^{-3}\Box\rho$ at $n = 3$; 10.64 X2.)

*Proof.* $|d\eta| = |x|^3|dt\,d|x|\,d\slashed g|$ with $t = x^1+|x|$, and $|dx^1\wedge d|x|| =
\rho_0^{-2}|x|\,|d\rho_0\wedge d\rho_I/\rho_I| = \rho_0^{-1}|x|\,|\frac{d\rho_0}{\rho_0}\wedge\frac{d\rho_I}{\rho_I}|$.
So $|d\eta| = |x|^4\rho_0^{-1}|\frac{d\rho_0}{\rho_0}\frac{d\rho_I}{\rho_I}d\slashed g| =
\rho_0^{-5}\rho_I^{-4}|\ldots|$. $|dg_{b_0}| = |d\eta|(1+O(\rho^2))$ with a smooth factor, by §0. For the
self-adjointness,
$$\langle Lu,v\rangle_{L^2(\mu_{\mathrm b})} = \int\big(\Box\rho^{3/2}u\big)\,v\,\rho_I\rho^{-7/2}\rho_0^5\rho_I^4\,|dg|
= \int\big(\Box\rho^{3/2}u\big)\big(\rho^{3/2}v\big)|dg|,$$
as $\rho_I\rho^{-7/2}\rho_0^5\rho_I^4 = \rho^{-7/2}\rho^5 = \rho^{3/2}$, and $\Box$ is symmetric on $L^2(|dg|)$.
$\square$

**Lemma 2.2 (L as an eb-operator; commutators; the source's Lemma 3.16 at n = 4).**
$L\in\mathrm{Diff}^2_{\mathrm{e,b}}(M_\sharp)$, and
$$L = -2X_I(X_0-X_I)+x_I^2\big(\slashed\Delta+\tfrac34\big)+\tilde L,\qquad\tilde L\in
x_I\mathrm{Diff}^2_{\mathrm{e,b}}(M_\sharp),\tag{2.2}$$
with $\slashed\Delta = -\slashed{\mathrm{tr}}\slashed\nabla^2\ge0$ the Laplacian of $\mathbb S^3$. For every vector
field $\Omega$ on $\mathbb S^3$,
$$[L,X_0],\ [L,X_I],\ [L,\Omega]\in x_I\mathrm{Diff}^{1,1}_{\mathrm{e,b;b}}(M_\sharp).\tag{2.3}$$

*Proof.* *Minkowski.* With $\Box = -\mathrm{tr}\nabla^2$, $\Box_\eta =
4\partial_0\partial_1-\frac3{|x|}\partial_{|x|}+|x|^{-2}\slashed\Delta$ on functions, and conjugation by $|x|^{-3/2}$
removes the first-order term:
$$|x|^{3/2}\Box_\eta|x|^{-3/2} = 4\partial_0\partial_1+|x|^{-2}\big(\slashed\Delta+\tfrac34\big),$$
the constant being $\frac{(n-1)(n-3)}4 = \frac34$ (10.64 X1; 0 at $n = 3$). By III.C (1.5) and $X_I\rho_0 = 0$,
$X_I\rho_I = \rho_I$,
$$4\partial_0\partial_1 = -2\rho_0\rho_IX_I\,\rho_0\big(X_0-X_I+\tfrac12\rho_IX_I\big) =
-2\rho_0^2\rho_IX_I(X_0-X_I)-\rho_0^2\rho_I^2(X_I+1)X_I.$$
Multiplying by $\rho_I\rho^{-2} = \rho_0^{-2}\rho_I^{-1}$ (with $|x|^{-2} = \rho_0^2\rho_I^2$) gives
$$L_\eta = -2X_I(X_0-X_I)+x_I^2\big(\slashed\Delta+\tfrac34\big)-x_I^2(X_I+1)X_I,$$
and $x_I^2(X_I+1)X_I\in x_I^2\mathrm{Diff}^2_{\mathrm{e,b}}$, $X_I$ being an eb-vector field.

*The mass.* $\Box_g$ modulo $\rho_0^2x_I^3\mathrm{Diff}^2_{\mathrm{e,b}}$ depends only on $g$ modulo
$\rho_0^{-2}x_I^{-1}C^\infty(S^2\,{}^{\mathrm{e,b}}T^*)$, by (1.1) and the Koszul formula. By Corollary 1.2's proof,
$g_{b_0}-\eta\in\rho_0^{-2}x_I^{-2}\cdot\rho_0^2x_I^2C^\infty$, which lies in that class. Conjugation by $\rho^{3/2}$
and multiplication by $\rho_I\rho^{-2}$ preserve the classes up to the factor $\rho_0^{-2}x_I^{-2}$. So $L-L_\eta\in
x_I\mathrm{Diff}^2_{\mathrm{e,b}}$, which is (2.2).

*Commutators.* This is the source's argument, which uses only (2.2) and the structure of $\mathcal V_{\mathrm{e,b}}$:

- $[L,X_0] = [\tilde L,X_0]\in x_I\mathrm{Diff}^2_{\mathrm{e,b}}$, as $X_0$ commutes with the leading part of (2.2)
($[X_0,x_I^2] = 0$) and $\mathcal V_{\mathrm{e,b}}$ is a Lie algebra. - $[L,X_I] =
-\rho_I(\slashed\Delta+\frac34)+[\tilde L,X_I]$, as $[x_I^2,X_I] = -x_I^2$. - Write $\slashed\Delta =
\sum_k\Omega_{k,1}\Omega_{k,2}+\Omega_\flat+f$, with $\Omega$'s vector fields on $\mathbb S^3$ and $f\in
C^\infty(\mathbb S^3)$. As $\mathcal V(\mathbb S^3)\subset x_I^{-1}\mathcal V_{\mathrm{e,b}}\cap\mathcal V_{\mathrm b}$,
$$\rho_I\big(\slashed\Delta+\tfrac34\big) =
x_I\sum_k(x_I\Omega_{k,1})\Omega_{k,2}+x_I(x_I\Omega_\flat)+x_I^2\big(f+\tfrac34\big)\in
x_I\mathrm{Diff}^{1,1}_{\mathrm{e,b;b}}$$
(the source's (3.18)).

- $[L,\Omega] = \rho_I[\Omega,\slashed\Delta]+[\tilde L,\Omega]$, and the first term lies in
$x_I\mathrm{Diff}^{1,1}_{\mathrm{e,b;b}}$ in the same way. For the second, lifts of vector fields on $\mathbb S^3$
preserve the eb-classes. In coordinates, $\Omega = \sum_j\Omega^j(y)\partial_{y^j}$ and $V =
a^0X_0+a^1X_I+\sum_ja^jx_I\partial_{y^j}$, and
$$[\Omega,V] = (\Omega a^0)X_0+(\Omega a^1)X_I+x_I\sum_j[\Omega,a^j\partial_{y^j}]\in\mathcal V_{\mathrm{e,b}}$$
(the source's (3.19a)). So $[-,\Omega]$ maps $\mathrm{Diff}^{2,(\alpha_0,\alpha_1)}_{\mathrm{e,b}}$ to itself (its
(3.19b)), and $[\tilde L,\Omega]\in x_I\mathrm{Diff}^2_{\mathrm{e,b}}$.

The term $\frac34x_I^2$ commutes with $X_0$ and $\Omega$, and $[\frac34x_I^2,X_I] = -\frac34x_I^2$ lies in
$x_I\mathrm{Diff}^0$. $\square$

## 3. The basic energy estimate near $\mathscr I^+$ ([Hin23a] Proposition 3.17)

*Domains.* Let $c_\sharp>0$ be so small that, on $\{x_I<c_\sharp\}\cap\{\rho_0\le1\}$:

- $|x| = \rho_0^{-1}x_I^{-2}>c_\sharp^{-2}\ge4R_1$, so the set lies in $U$;

- the level sets of $x_I$ are spacelike for $g_{b_0}$;

- the multiplier $V$ below is future timelike for $g_{b_0}$.

This is possible. For $\eta$, $d\rho_I = |x|^{-1}\big(-\frac12\rho_Idx^0-(1-\frac12\rho_I)dx^1\big)$, so
$$\eta^{-1}(d\rho_I,d\rho_I) = -2|x|^{-2}\rho_I\big(1-\tfrac12\rho_I\big)<0\quad(\rho_I<2)\tag{3.1}$$
(the source's (3.8), with $\eta^{-1}(dx^0,dx^1) = -2$, $\eta^{-1}(dx^0,dx^0) = \eta^{-1}(dx^1,dx^1) = 0$). The
correction from $g_{b_0}-\eta$ is $O(\rho^2)$ relative to $\rho_I|x|^{-2}$ by Corollary 1.2, so (3.1) persists for
$\rho_0x_I^2$ small; this is the role of the source's $\bar x_I\le1/\sqrt{8m}$, at $n = 4$ $\bar x_I\le1/(2\mu_0^{1/4})$
(10.64 X8).

Let $\Omega\subset\{x_I<c\}\cap\{\rho_0<1\}$, $c<c_\sharp$, be open. Its boundary in the interior consists of two smooth
hypersurfaces: $\Sigma_{\mathrm{in}}$, spacelike for $g_{b_0}$, and $\Sigma_{\mathrm{fin}}$, spacelike or null for
$g_{b_0}$, with $\Omega$ to the future of $\Sigma_{\mathrm{in}}$ and to the past of $\Sigma_{\mathrm{fin}}$. Every
integral curve of $X_I$ in $\Omega$ (at fixed $\rho_0,\omega$, $\rho_I$ decreasing) begins on $\Sigma_{\mathrm{in}}$.
The source's $\{x_I<c,\rho_0<1\}$ with $\Sigma_{\mathrm{in}} = x_I^{-1}(c)$ and $\Sigma_{\mathrm{fin}} = \rho_0^{-1}(1)$
is an example. So is $\Omega_{\mathrm{ext},r_0}\cap\{x_I<c\}\cap\{t_{\mathrm{IVP}}\ge0\}$, whose part of
$\Sigma_{\mathrm{IVP}}$ is spacelike and whose $\Sigma_{\mathrm{fut},r_0}$ is spacelike (III.C$'$ Lemma 1.1), together
with the part of $x_I^{-1}(c)$ in it; an outgoing ray at fixed $x^1$ enters it across $\Sigma_{\mathrm{IVP}}$ or
$x_I^{-1}(c)$.

**Proposition 3.1 (the energy estimate; [Hin23a] Proposition 3.17 at n = 4).** Let $\Omega$ be as above, $k\in\mathbb
N_0$, and $\alpha_0,\alpha_I\in\mathbb R$ with $\alpha_I<\min(\alpha_0,0)$. Let $f\in
H^{k,(\alpha_0,2\alpha_I)}_{\mathrm b}(\Omega) = \rho_0^{\alpha_0}\rho_I^{\alpha_I}H^k_{\mathrm b}(\Omega)$ vanish near
$\Sigma_{\mathrm{in}}$. Then the forward solution $u$ of $Lu = f$ (vanishing Cauchy data on $\Sigma_{\mathrm{in}}$) lies
in $H^{(1;k),(\alpha_0,2\alpha_I)}_{\mathrm{e,b;b}}(\Omega)$, and
$$\|u\|_{H^{(1;k),(\alpha_0,2\alpha_I)}_{\mathrm{e,b;b}}(\Omega)}\le C\|f\|_{H^{k,(\alpha_0,2\alpha_I)}_{\mathrm
b}(\Omega)},\tag{3.2}$$
with $C$ depending on $k$, $\alpha_0$, $\alpha_I$, $c$ and the geometry of $\Sigma_{\mathrm{in}}$,
$\Sigma_{\mathrm{fin}}$. Away from $\mathscr I^+$ (on $\{x_I\ge c/2\}$) the same holds with $H^{k+1}_{\mathrm b}$ on the
left.

*Proof.* *The multiplier* (the source's (3.22)). Let
$$W := w^2V,\qquad w := \rho_0^{-\alpha_0}\rho_I^{-\alpha_I},\qquad V := X_0-(1+\kappa)X_I,\quad\kappa>0.$$
$V$ is future timelike. With III.C (1.4)-(1.5), $V = \rho_0^{-1}\big(\partial_t+2\kappa\rho_I^{-1}\partial_0\big)$, a
positive combination of the future timelike $\partial_t$ and the future null $\partial_0$, near $\mathscr I^+$ for
$\eta$, hence for $g_{b_0}$ by Corollary 1.2. By the leading form of Corollary 1.2,
$g_{b_0}(V,V)\equiv\rho_0^{-2}x_I^{-2}(2-2(1+\kappa)) = -2\kappa\rho_0^{-2}x_I^{-2}$ modulo
$\rho_0^{-2}x_I^{-1}C^\infty$, so $V$ is uniformly timelike in the eb-sense.

*The identity* (the source's (3.23)). For $u$ smooth with support as in the statement,
$$2\,\mathrm{Re}\langle wLu,wVu\rangle_{L^2(\Omega,\mu_{\mathrm b})} = \langle Qu,u\rangle+\mathcal
B_{\mathrm{fin}}(u),\qquad Q := L^*W+W^*L = [L,W]-(\mathrm{div}_{\mu_{\mathrm b}}W)L.$$
Here $\mathcal B_{\mathrm{fin}}$ is the boundary term at $\Sigma_{\mathrm{fin}}$; there is none at
$\Sigma_{\mathrm{in}}$, where $u$ vanishes to second order, and none at $I_0\cup\mathscr I^+$ for $u$ of compact support
in $M_\sharp$, the general case following by density. $\mathcal B_{\mathrm{fin}}(u)\ge0$: it is the flux through
$\Sigma_{\mathrm{fin}}$ of the energy current of the future timelike $W$, and $\Sigma_{\mathrm{fin}}$ is spacelike or
null with $\Omega$ to its past.

*The principal symbol of Q.* Modulo $\rho_0^{-2\alpha_0}x_I^{-4\alpha_I+1}\mathrm{Diff}^2_{\mathrm{e,b}}$, $L$ may be
replaced by the leading part $L_0$ of (2.2), and $\mu_{\mathrm b}$ by $\bar\mu_{\mathrm b}
:= |\frac{d\rho_0}{\rho_0}\frac{d\rho_I}{\rho_I}d\slashed g|$ (Lemma 2.1). Then $-\mathrm{div}_{\bar\mu_{\mathrm b}}W =
-[V,w^2] = w^2(-2(1+\kappa)\alpha_I+2\alpha_0)$, and
$$Q\equiv\bar Q := w^2\Big(-4\alpha_I(\rho_0D_{\rho_0}-\rho_ID_{\rho_I})^2+4\kappa(\alpha_0-\alpha_I)(\rho_ID_{\rho_I})^2
+\big(1+2(\alpha_0-\alpha_I)+\kappa(1-2\alpha_I)\big)x_I^2\big(\slashed\Delta+\tfrac34\big)\Big).\tag{3.3}$$
This is the source's (3.25) with $\slashed\Delta+\frac34$ in place of $\slashed\Delta$, computed in 10.64 X3 by applying
$[L_0,W]-(\mathrm{div}W)L_0$ to $e^{i(\xi_0\log\rho_0+\xi_I\log\rho_I)}$. The constant $\frac34$ enters only through the
angular term: $x_I^2\cdot\frac34$ commutes with $X_0$, and its commutator with $X_I$ is of order 0. As $\alpha_I<0$,
$\kappa>0$, $\alpha_0-\alpha_I>0$ and $\slashed\Delta+\frac34\ge\frac34>0$, $\bar Q$ is a positive elliptic element of
$\rho_0^{-2\alpha_0}x_I^{-4\alpha_I}\mathrm{Diff}^2_{\mathrm{e,b}}$ (the constant term only increasing it). So
$$\langle\bar Qu,u\rangle\ge c_0\sum_{V'}\|wV'u\|^2_{L^2_{\mathrm b}},$$
the sum over $V'\in\{X_0,X_I,x_I\Omega_j\}$ with $\Omega_j$ spanning $T\mathbb S^3$.

*Poincaré.* Along each integral curve of $X_I$ in $\Omega$, which begins on $\Sigma_{\mathrm{in}}$ where $u = 0$, with
$s := -\log\rho_I$ and $\rho_0$ fixed,
$$\int e^{2\alpha_Is}|u|^2\,ds\le\alpha_I^{-2}\int e^{2\alpha_Is}|\partial_su|^2\,ds\qquad(\alpha_I<0),$$
by $u(s) = \int_{s_0}^s\partial_su$ and the weighted Cauchy-Schwarz inequality. The constant does not depend on where
the curve ends, so integrating in $\rho_0$ and $\omega$ gives $\|wu\|_{L^2_{\mathrm b}}\le C\|wX_Iu\|_{L^2_{\mathrm b}}$.

*Conclusion for k = 0.* The error $Q-\bar Q$ is bounded by $Cc$ times the right side of the positivity bound, for $c$
small (it carries a factor $x_I<c$). Cauchy-Schwarz on the left of the identity, $\mathcal B_{\mathrm{fin}}\ge0$, and
absorption give $\|wu\|_{H^1_{\mathrm{e,b}}}\le C\|wf\|_{L^2_{\mathrm b}}$, which is (3.2) for $k = 0$. Existence of the
forward solution, smooth in $\Omega$, is standard for the wave equation with smooth coefficients on $\Omega$.

*Higher b-regularity* (the source's induction). Let $X_0$, $X_1 := X_I$, $X_2,\dots,X_7$ the six rotation fields of
$\mathbb S^3$ (spanning $T\mathbb S^3$ pointwise), and $X_8 := 1$. These span $\mathrm{Diff}^1_{\mathrm b}$ over
$C^\infty$. By (2.3), $[L,X_j] = \sum_kx_IY_{jk}X_k$ with $Y_{jk}\in\mathrm{Diff}^1_{\mathrm{e,b}}$. Assume (3.2) at
$k$. Applying it to $L(X_ju) = X_jf+[L,X_j]u$ (the support condition is preserved, the $X_j$ being tangent to the faces
and commuting with restriction to $\Sigma_{\mathrm{in}}$ up to terms vanishing there) gives
$$\|X_ju\|_{H^{(1;k)}_{\mathrm{e,b;b}}}\le C\Big(\|X_jf\|_{H^k_{\mathrm
b}}+\sum_k\|x_IX_ku\|_{H^{(1;k)}_{\mathrm{e,b;b}}}\Big),$$
with the weights. Summing over $j$, the last sum is absorbed for $c$ small. This gives (3.2) at $k+1$. The statement on
$\{x_I\ge c/2\}$ holds as $\mathcal V_{\mathrm{e,b}} = \mathcal V_{\mathrm b}$ there, so (3.2) gives one b-derivative
more. $\square$

*Remark 3.2 (the source's Remark 3.18).* In the coordinates $(t,|x|)$, modulo lower-order terms, $W
= |x|^{2\alpha_I}(2-x^1)^{2(\alpha_0-\alpha_I)}\big((2-x^1)\partial_t+\kappa|x|(\partial_t+\partial_{|x|})\big)$.

## 4. The estimate near the interior of $I_0$ (the source's citation of [HV20, Proposition 4.3])

Near the interior of $I_0$, away from $\mathscr I^+$, III.B's coordinates are $(\tau,\rho) = (t/|x|,|x|^{-1})$ with
$\tau\in[-\frac12,1-\delta]$ (III.C Lemma 1.1's proof), and $\rho_I = 1-\tau+2\rho\ge\delta$.

**Proposition 4.1 (b-energy estimate near $I_0$).** Let $\delta>0$ and
$\Omega_0\subset\{\rho\le\rho_1\}\cap\{\tau_0\le\tau\le1-\delta\}$ be open, with interior boundary consisting of $\{\tau
= \tau_0\}$ (initial) and a hypersurface $\Sigma_{\mathrm{fin}}$ that is spacelike or null for $g_{b_0}$ (final). Let
$k\in\mathbb N_0$, $\alpha_0\in\mathbb R$, and $f\in\rho^{\alpha_0}H^k_{\mathrm b}(\Omega_0)$ vanish near $\{\tau =
\tau_0\}$. Then for $\rho_1$ small the forward solution of $Lu = f$ satisfies $\|u\|_{\rho^{\alpha_0}H^{k+1}_{\mathrm
b}(\Omega_0)}\le C\|f\|_{\rho^{\alpha_0}H^k_{\mathrm b}(\Omega_0)}$.

*Proof.* In $(\tau,\rho,\omega)$, $\partial_t = \rho\partial_\tau$ and $\partial_{|x|} =
-\rho(\tau\partial_\tau+\rho\partial_\rho)$, so the coordinate fields of $\eta$ are $\rho$ times b-vector fields.
$\eta^{-1}$ is $\rho^2$ times a smooth nondegenerate Lorentzian b-metric $G_{\mathrm b}$ on $\{\rho\le\rho_1\}$:
$$G_{\mathrm b} = -\partial_\tau^2+(\tau\partial_\tau+\rho\partial_\rho)^2+\slashed g^{-1}.$$
$G_{\mathrm b}(d\tau,d\tau) = -(1-\tau^2)<0$ for $|\tau|<1$, so $\tau$ is a b-time function there.
$g_{b_0}^{-1}-\eta^{-1}$ is $O(\rho^2)$ relative (§0). So $L = \rho_I\rho^{-7/2}\Box\rho^{3/2}$ lies in
$\mathrm{Diff}^2_{\mathrm b}$, with principal symbol $\rho_IG_{\mathrm b}$ up to $O(\rho)$ and $\rho_I\ge\delta$.

Use the multiplier $W_0 := w_0^2V_0$, with $w_0 := \rho^{-\alpha_0}e^{-\Lambda\tau}$ and $V_0 := -G_{\mathrm
b}(d\tau,\cdot)$, a future timelike b-vector field. In the identity $2\mathrm{Re}\langle w_0Lu,w_0V_0u\rangle = \langle
Q_0u,u\rangle+\mathcal B_{\mathrm{fin}}$: - the boundary term at $\Sigma_{\mathrm{fin}}$ is $\ge0$, as in Proposition
3.1; - $Q_0 = [L,W_0]-(\mathrm{div}W_0)L$.

The term of $Q_0$ from differentiating $e^{-2\Lambda\tau}$ is $2\Lambda w_0^2$ times the energy-momentum quadratic form
of $V_0$ and $d\tau$ in $\rho_IG_{\mathrm b}$. It is positive definite in the b-gradient, as $V_0$ and $-\nabla\tau$ are
future timelike (the dominant energy condition for the scalar wave equation). The other terms are bounded by
$C(1+|\alpha_0|)w_0^2|{}^{\mathrm b}\nabla u|^2+Cw_0^2|u|^2$ with $C$ independent of $\Lambda$. The $|u|^2$ term is
controlled by integrating $\partial_\tau$ from $\{\tau = \tau_0\}$, where $u = 0$, over the compact $\tau$-interval. For
$\Lambda$ large this gives the estimate for $k = 0$, with $e^{\pm\Lambda\tau}$ bounded on $[\tau_0,1-\delta]$.

Higher b-regularity follows by commuting $\rho\partial_\rho$ and the rotation fields: their commutators with $L$ lie in
$\mathrm{Diff}^2_{\mathrm b}$ and are of first order in the commuted derivatives, since $L$ is a b-operator. The
induction closes on the compact $\tau$-interval with the same $\Lambda$-argument, the commutator terms entering as
sources. Commuting $\partial_\tau$ is not needed: a b-derivative transversal to the level sets of $\tau$ is recovered
from the equation, $L$ being strictly hyperbolic with respect to $\tau$. $\square$

*Remark 4.2 (gluing).* Proposition 3.1 near $\mathscr I^+\cup(I_0\cap\mathscr I^+)$, Proposition 4.1 near the interior
of $I_0$, and the standard energy estimate on compact sets cover $\Omega_{\mathrm{ext},r_0}$ near infinity. The forward
problem is solved successively: on a region whose past boundary is $\Sigma_{\mathrm{IVP}}$, then on the next region with
the previous solution as data. The data enter as sources after subtracting an extension of the Cauchy data, cut off near
the initial surface. The regions are ordered by domain of dependence (II.F Lemma 1.3), as in the source ("cut and paste
energy estimates using domain of dependence properties", p. 16). Where two estimates apply, the solutions agree, and the
norms are equivalent on the overlaps, each overlap lying away from the face that distinguishes the two calculi. The
global estimate for the tensor operator, with weights at both faces, is the next part's.

## 5. Findings and sources

(IV1) *The conjugation and the density at n = 4.* $L = \rho_I\rho^{-7/2}\Box\rho^{3/2}$ is symmetric on
$L^2(\rho_0^5\rho_I^4|dg|)$, against the source's $\rho_I\rho^{-3}\Box\rho$ and $\rho_0^4\rho_I^3|dg|$ (Lemma 2.1). The
conjugated operator carries the constant $\frac34 = \frac{(n-1)(n-3)}4$ with the spherical Laplacian (Lemma 2.2). This
only increases the angular term of $\bar Q$, which stays positive under the source's conditions (3.3).

(IV2) *The coordinates.* The source works with Schwarzschild's null coordinates, $r_* = r+2m\log(r-2m)$; here the
coordinates are III.C's Minkowski null coordinates, in which $g_{b_0}-\eta$ has frame components $O(\rho^2)$. The mass
then enters $L$ only through the error class $x_I\mathrm{Diff}^2_{\mathrm{e,b}}$ (Lemma 2.2), and the level sets of
$\rho_0$ are null only for $\eta$. Proposition 3.1 therefore takes a final boundary that is spacelike or null for
$g_{b_0}$, and the region's own spacelike boundaries serve (Proposition 3.1's examples).

(IV3) *The region near $I_0$.* The source cites [HV20, Proposition 4.3] for the estimate away from $\mathscr I^+$.
Proposition 4.1 writes it out on the compact $\tau$-range of III.B's chart, with an exponential weight in $\tau$.

*Labels.* Lemma 1.1 is the source's Lemma 3.13, Corollary 1.2 its Lemma 3.12 and Corollary 3.14, Remark 1.3 its Remark
3.15, Lemma 2.1 the density in Proposition 3.17's proof, Lemma 2.2 its Lemma 3.16, Proposition 3.1 its Proposition 3.17,
Remark 3.2 its Remark 3.18. Proposition 4.1 and Remark 4.2 are new at $n = 4$ (the source cites them).

*Sources.* [Hin23a] pp. 9-17 (sections 3.1-3.2: Definitions 3.1-3.5, 3.7, 3.10-3.11, Lemmas 3.6, 3.12-3.13, 3.16,
Corollary 3.14, Remarks 3.8-3.9, 3.15, 3.18, Proposition 3.17 with (3.20)-(3.25)), read at source. Inputs: III.B (4.2),
section 3; III.C section 1 (Lemmas 1.1, 1.3, (1.2)-(1.6)); III.C$'$ Lemma 1.1; II.F Lemma 1.3; N1STAR-PROOF.md 10.64
(`exterior5.py` X1-X3, X6, X8).
