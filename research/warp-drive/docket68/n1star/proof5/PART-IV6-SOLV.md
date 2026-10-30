# Part IV$'''''$. Constraint damping II: solvability on weighted 3b-spaces, n = 4 ([Hin26a] sections 2.1-2.3, 5.2)

*Status.* Written (D308). This part proves [Hin26a] Theorem 5.2 at $n = 4$ (Theorem 7.3 below). The setting is the
constraint propagation operator of Part IV$''''$ on the Myers-Perry metrics, $b$ near $b_0$, with the 1-form $c_C$ and
the parameters of Part IV$''''$ (0.1) and the weights of its (2.1). The theorem gives the forward problem and the
initial value problem solved on weighted semiclassical 3b-Sobolev spaces, with the a priori estimate (5.79) and the
adjoint estimate (5.81), for all $h<h_0$ with $h_0$ uniform in $b$. Part IV$''''$ Theorem 2.1 rests on it. The source's
section 5.2 is a chain of semiclassical estimates, each an identity of symbols or a pairing in which the dimension does
not appear. Each is written out below at $n = 4$, and every place where $n$ enters is named and discharged: the
compactification and the 3sc structure of the metric (section 0, from III.B), the volume density (Lemma 0.2 (b)), the
causal facts (Lemma 0.3), the fibre algebra (Lemma 0.4, from Part IV$''''$ Lemma 1.1) and the 1-form (Lemma 0.5, from
Part IV$''''$ Lemma 1.4). The source uses three families of estimates without stating them: the propagation through the
interior of $\Omega$ in both directions, along $\mathrm{sf}$ between its critical sets, and along $K^+$ outward from the
saddle. These are stated and proved as Propositions 5.2-5.3. Source: [Hin26a] (arXiv:2606.27658v2) pp. 12-17 (sections
2.1-2.2), 25-28 (section 3), 37-39 (Proposition 5.1), 41-66 (section 5.2), read at source. Verified (D311): verifier 134
read it in full; two minor findings and two nits, seated as findings (IV$'''''$6)-(IV$'''''$7) and in Propositions
7.1-7.2 and Theorem 7.3 (c); to be read. Proved (D312): verifier 135 read the D311 repairs, correct.

## 0. Setting

Throughout $n = 4$. $\mu_0$, $R_1 = \mu_0^{1/2}$, $\mathcal B$ and $b_0 = (\mu_0,0)$ are III.B's (section 3.1).
$r_\sharp := \frac12R_1$ (III.B's $r_0$) is the inner radius, the source's $m$. $r_c := 100R_1$ is the radius of the
saddle point of $c_C$, the source's $r_0$ (10.14's $r_0 = 100$ at $\mu = 1$, rescaled; Part IV$''''$ section 0). $v :=
v_C = \frac12$ and $e := e_C = \frac1{102400}$ (Part IV$''''$ (0.1)).

*Coordinates.* We work in the Kerr-Schild coordinates $(t,x)$ of III.B (3.2), with $r := |x|$. For $b\in\mathcal B$, $g
:= g^{\mathrm{KS}}_b = \eta+H_bk_b\otimes k_b$ is defined and smooth with $H_b>0$ on $\mathbb
R_t\times\{r\ge\frac12r_\sharp\}$, smoothly in $b$. Indeed III.B section 3.1's estimate, run at $r = \frac14R_1$ with
$\|A\|^2<\frac1{100}R_1^2$, gives $|x|^2>2\|A\|^2\ge s$ and $r_A^2\ge(\frac1{16}-\frac1{100})R_1^2$; under these Lemma
3.3 (c)'s condition $\|A\|^2(r_A^2+\|A\|^2)<r_A^4$ holds. III.B's $g_b$ is $\Phi_\mu^*g$ with $\Phi_\mu(t,x) =
(t-T_\mu(|x|),x)$ (III.B (3.3)), and Remark 7.4 transfers the results to it. $c := c_C$ is 10.14's 1-form
(10.48)-(10.49), defined in these coordinates on $\{r\ge r_\sharp\}$ (Part IV$''''$ section 0). We extend it to
$\{r\ge\frac12r_\sharp\}$ as a stationary smooth past timelike 1-form; such an extension exists, the past timelike
covectors at a point forming an open convex cone.

**Definition 0.1 (the compactification and the spaces; [Hin26a] Definitions 2.1, 2.2, 2.5, (2.2)-(2.3), (2.10), (2.11),
(5.19) at n = 4).** Let $M_0 := [\overline{\mathbb R^{1+4}};k_+,k_-]$, where $k_\pm$ are the poles of the radial
compactification at future and past timelike infinity. Let $M^\flat :=
\mathrm{cl}_{M_0}\big(M_0^\circ\setminus\mathrm{cl}(\{r<r_\sharp\}\cup\{t<-\frac12r\})\big)$. Its faces are:

- the Kerr face $K^+ := M^\flat\cap\beta^{-1}(k_+)$;

- the side face $\mathrm{sf} := \partial M^\flat\cap(\partial M_0\setminus(K^+)^\circ)$;

- $X_0 := \mathrm{cl}\{t = 0\}$ and $\Sigma^\sharp := \mathrm{cl}\{r = r_\sharp\}$;

- the domain $\Omega := \mathrm{cl}\{t\ge0\} = \{\tau\ge0\}$, with $\tau := t/r$.

($M^\flat$ is the source's $M$ at $n = 4$; III.B's $M$ is a different compactification and is not used here.) $M^\flat$
is covered by the source's three charts with $\mathbb S^3$ for $\mathbb S^2$:

- $[r_\sharp,\infty)_r\times[-\frac12,\infty)_\tau\times\mathbb S^3$;

- $[0,r_\sharp^{-1}]_{\rho_{\mathrm{sf}}}\times[0,2]_{\rho_K}\times\mathbb S^3$, with $(t,r) =
(\rho_{\mathrm{sf}}^{-1}\rho_K^{-1},\rho_{\mathrm{sf}}^{-1})$;

- $[0,r_\sharp^{-1}]_{\rho_{\mathrm{sf}}}\times[-\frac12,\infty)_\tau\times\mathbb S^3$.

On $\{t>\frac12r\}$ we use $\rho_K = r/t$ and $\rho_{\mathrm{sf}} = 1/r$.

- $\mathcal T$, $\mathcal T^*$ are the pullbacks of the scattering bundles of $\overline{\mathbb R^{1+4}}$ (the 3sc
bundles; $dt,dx^1,\dots,dx^4$ is a frame of $\mathcal T^*$).

- $\mathcal V_{3\mathrm b}(M^\flat)$ is the $C^\infty(M^\flat)$-span of $r\partial_{z^\mu}$, $\mu = 0,\dots,4$. With it
come ${}^{3\mathrm b}TM^\flat$, ${}^{3\mathrm b}T^*M^\flat$ (frame $dz^\mu/r$) and $\mathrm{Diff}^k_{3\mathrm b}$ with
weights. By the source's computation, $\partial_{z^\mu}\in\rho_{\mathrm{sf}}\mathcal V_{3\mathrm b}(M^\flat)$.

- The projection $(t,x)\mapsto x$ extends to a smooth map $\pi:M^\flat\to\bar X_\sharp := \bar X\cap\{r\ge r_\sharp\}$,
so $\pi^*C^\infty(\bar X_\sharp)\subset C^\infty(M^\flat)$.

The semiclassical 3b-pseudodifferential calculus $\Psi_{3\mathrm b,\hbar}(M^\flat)$ carries with it the following: its
principal symbols, the operator wave front set $\mathrm{WF}'_{3\mathrm b,\hbar}$, the elliptic set
$\mathrm{Ell}_{3\mathrm b,\hbar}$, elliptic parametrices, the sharp Gårding inequality, and the Sobolev spaces
$H^s_{3\mathrm b,h}$. It is constructed on $\mathbb R_t\times\mathbb R^{n}_x$ for every $n$ ([Hin23d]), and on manifolds
of bounded geometry of every dimension ([Hin26d]; his section 2.3.1). This is record 10.65 (a), READ. Write
$H^{s,(\beta_{\mathrm{sf}},\beta_K)}_{3\mathrm b,h} :=
\rho_{\mathrm{sf}}^{\beta_{\mathrm{sf}}}\rho_K^{\beta_K}H^s_{3\mathrm b,h}(M^\flat;\mathcal T^*)$ (his (5.19)), normed
with the density $|dg|$ and the fibre inner product $B$ of Lemma 0.4. On $\Omega$ there are three kinds of space:

- $H^{s,(\cdot)}_{3\mathrm b,h}(\Omega)^{\bullet,-}$: restrictions to $\Omega^\circ$ of elements with support in
$\{t\ge0\}$, so supported at $X_0$ and extendible at $\Sigma^\sharp$;

- $(\cdot)^{-,\bullet}$: extendible at $X_0$ and supported at $\Sigma^\sharp$;

- $\bar H$: extendible at both.

These are his section 2.3's spaces. In all of these constructions the dimension enters only as the number of coordinates.

**Lemma 0.2 (the metric and the 1-form as 3sc objects; [Hin26a] Lemmas 2.3-2.4, (2.12)-(2.14), Lemma 5.3 at n = 4).**
For $b\in\mathcal B$:

(a) $g\in C^\infty(M^\flat;S^2\mathcal T^*)$ is a stationary nondegenerate Lorentzian 3sc-metric, $g^{-1}\in
C^\infty(M^\flat;S^2\mathcal T)$, and $g-\eta$, $g^{-1}-\eta^{-1}$ lie in $\rho_{\mathrm{sf}}^2C^\infty$, smoothly in
$b$;

(b) $|dg| = |dt\,dx| = r^3|dt\,dr\,d\slashed g| = r^4|d\tau\,dr\,d\slashed g|$, $d\slashed g$ the round density of
$\mathbb S^3$;

(c) the Christoffel symbols of $g$ in $(t,x)$ lie in $\rho_{\mathrm{sf}}C^\infty(M^\flat)$; so
$\nabla\in\rho_{\mathrm{sf}}\mathrm{Diff}^1_{3\mathrm b}(M^\flat;\mathcal T^{p,q},\mathcal T^*\otimes\mathcal T^{p,q})$,
$\Box_g\in\rho_{\mathrm{sf}}^2\mathrm{Diff}^2_{3\mathrm b}$, and
$\delta^*_g,\delta_g\in\rho_{\mathrm{sf}}\mathrm{Diff}^1_{3\mathrm b}$;

(d) $c\in\rho_{\mathrm{sf}}C^\infty(M^\flat;\mathcal T^*)$ is stationary, $h^2\Box_g\in
h^2\rho_{\mathrm{sf}}^2\mathrm{Diff}^2_{3\mathrm b}(M^\flat;\mathcal T^*)$ and $L_h := L_{g,c,e,h}\in
h\rho_{\mathrm{sf}}^2\mathrm{Diff}^1_{3\mathrm b}(M^\flat;\mathcal T^*)$; the semiclassical 3b-principal symbol of $P_h
:= h^2\Box^C_b = h^2\Box_g-iL_h$ is $p = G-i\ell$, with $G(\zeta) = g^{-1}(\zeta,\zeta)$ and $\ell := \ell_{g,c,e}$ of
his (3.3).

*Proof.* (a) In $(t,x)$ the components of $g$ do not depend on $t$, are smooth on $\{r\ge\frac12r_\sharp\}$, and near
infinity lie in $C^\infty(\bar X)$ with $g-\eta\in|x|^{-2}C^\infty(\bar X)$. This is III.B Proposition 3.6 and its
proof, which establishes (3.5) for $g^{\mathrm{KS}}_b$ first; its Lemma 3.5 (c) is only the transfer to $g_b$. The same
holds for the inverse, which is $\eta^{-1}-H_bk_b^\sharp\otimes k_b^\sharp$ (III.B Lemma 3.3 (d)). Through $\pi$ these
components are smooth functions on $M^\flat$, and $|x|^{-2} = \rho_{\mathrm{sf}}^2$. In the frame $dz^\mu$ this gives
$g\in C^\infty(M^\flat;S^2\mathcal T^*)$ and likewise for $g^{-1}$. Since $k_b$ is $\eta$-null (III.B Lemma 3.3 (a)),
$\det(\eta+H_bk_b\otimes k_b) = \det\eta\,(1+H_b\eta^{-1}(k_b,k_b)) = -1$ identically. So $g$ is nondegenerate on all of
$M^\flat$. It is Lorentzian on $M^\flat$: at finite points this is the metric itself, and at $\mathrm{sf}$ its
components are $\eta$'s. Smoothness in $b$ is III.B's.

(b) $\det g = -1$ in $(t,x)$ gives $|dg| = |dt\,dx|$. Polar coordinates on $\mathbb R^4$ give $|dx| = r^3|dr\,d\slashed
g|$, and $dt = r\,d\tau+\tau\,dr$ gives $|dt\,dr| = r|d\tau\,dr|$.

(c) $\Gamma^\kappa_{\mu\nu} = \frac12g^{\kappa\lambda}(\partial_\mu g_{\nu\lambda}+\partial_\nu
g_{\mu\lambda}-\partial_\lambda g_{\mu\nu})$, with $g^{\kappa\lambda}\in C^\infty(M^\flat)$ and $\partial_\mu
g_{\nu\lambda}\in\rho_{\mathrm{sf}}C^\infty(M^\flat)$ because $\partial_{z^\mu}\in\rho_{\mathrm{sf}}\mathcal V_{3\mathrm
b}$. The rest is the source's (2.13)-(2.14), with the same proof. (For Tangherlini the record finds
$\Gamma\in\mu\rho^3C^\infty$, Proposition 10.19 (i).)

(d) $c$ is stationary and smooth on $\{r\ge\frac12r_\sharp\}$, and equals $r^{-1}(dt-v\,dr)$ for $r\ge3r_c$ (10.14 (b);
10.22 (a)). Its components $(r^{-1},-vr^{-1}\hat x)$ lie in $|x|^{-1}C^\infty(\bar X)$, so
$c\in\rho_{\mathrm{sf}}C^\infty(M^\flat;\mathcal T^*)$. By Part IV$''''$ section 0, the trace weight $\frac23$ gives
$hG_gC$ the source's form, so $L_h = 4ih\,\delta_g(c\otimes_s\cdot)+2ihe\,d\iota_{c^\sharp}$ is his (3.2). Now
$\delta_g$ and $d$ lie in $\rho_{\mathrm{sf}}\mathrm{Diff}^1_{3\mathrm b}$ by (c), and multiplication by $c$ or
$\iota_{c^\sharp}$ lies in $\rho_{\mathrm{sf}}C^\infty$; so $L_h\in h\rho_{\mathrm{sf}}^2\mathrm{Diff}^1_{3\mathrm b}$.
The principal symbols are his Lemma 3.2, a pointwise computation free of $n$. $\square$

**Lemma 0.3 (the causal facts; [Hin26a] p. 15 and the uses in Propositions 5.6, 5.16 at n = 4).** Let $\hat r :=
\frac34R_1$ and $T_0 := \frac12$. There is a neighbourhood $U\subset\mathcal B$ of $b_0$ such that for $b\in U$:

(a) for every $\beta\in(-1,1]$, $d(t-\beta r)$ is past timelike on $\{r\ge\frac12r_\sharp\}$, with
$g^{-1}(dt-\beta\,dr,dt-\beta\,dr)\le-(1-\beta^2)$; in particular $dt$, $d(t\pm\kappa r)$ for $\kappa\in(0,1)$, are past
timelike, $X_0$ is spacelike, and future timelike vectors point into $\Omega$ at $X_0$;

(b) $r^2g^{-1}(d\tau,d\tau)\le-\frac34$ on $\tau^{-1}([0,T_0])$; so $d\tau$ is past timelike for $g_{3\mathrm b} :=
\rho_{\mathrm{sf}}^2g$ there, uniformly up to $\mathrm{sf}$;

(c) on $\{\frac12r_\sharp\le r\le\hat r\}$, $dr$ is future timelike, with $g^{-1}(dr,dr)\le-\frac12$; so $\Sigma^\sharp$
is spacelike, future timelike vectors point out of $\Omega$ there, and $-dr$ is past timelike;

(d) $d\rho_K/\rho_K^2 = -dt$ with $\rho_K = t^{-1}$ near $(K^+)^\circ$, and $d\rho_{\mathrm{sf}}/\rho_{\mathrm{sf}}^2 =
-dr$.

*Proof.* (a) The time orientation is the one in which $dt$ is past timelike (the source's convention, p. 14). III.B
Lemma 3.3 (e) gives $g^{-1}(dt-\beta\,dr,dt-\beta\,dr) = -(1-\beta^2)-H_b(1+\beta r_A/|x|)^2<0$ for $\beta\in(-1,1]$,
wherever (c)'s condition holds, which is all of $\{r\ge\frac12r_\sharp\}$. The family $s\mapsto d(t-s\beta r)$,
$s\in[0,1]$, is timelike throughout and starts at $dt$, so it stays in the past cone. A future timelike $V$ has
$dt(V)>0$, since $dt$ is past timelike.

(b) $d\tau = r^{-1}(dt-\tau\,dr)$, so $r^2g^{-1}(d\tau,d\tau)$ is (a)'s quantity at $\beta = \tau\in[0,\frac12]$. It is
at most $-(1-\frac14)$. As $g_{3\mathrm b}^{-1} = r^2g^{-1}$, this is the claim; for Tangherlini it is the record's
Proposition 10.19 (ii).

(c) At $b_0$, $g^{-1}(dr,dr) = 1-\mu_0r^{-2}\le1-\frac{16}9$ on $[\frac12r_\sharp,\hat r]$ and $g^{-1}(dr,dt) =
\mu_0r^{-2}>0$ (Proposition 10.19 (iii)). The second says that the timelike covectors $dr$ and $dt$ lie in opposite
cones, so $dr$ is future timelike. Both strict inequalities hold on a compact set, and $g^{-1}$ is continuous in $b$
there, so they persist on a neighbourhood $U$ of $b_0$. A future timelike $V$ has $dr(V)<0$, so $V$ points out of
$\{r\ge r_\sharp\}$.

(d) is direct. $\square$

**Lemma 0.4 (the fibre algebra and the subprincipal symbol; [Hin26a] Lemmas 3.3-3.9, Corollary 3.6 at n = 4).** At every
point of $M^\flat$, his Lemmas 3.3-3.8 and Corollary 3.6 hold for $(g,c,e)$, with $B :=
g^{-1}-(1+e)G(c)^{-1}c^\sharp\otimes c^\sharp$. The skew-adjoint part $S := (2ih)^{-1}(L_h-L_h^*)$, adjoint for $|dg|$
and $B$, is the bundle map of his Lemma 3.9, with the same formula. There is $C>0$, uniform for $b\in U$, such that
$C(\rho_{\mathrm{sf}}^{-2}\ell(\zeta))^2+\rho_{\mathrm{sf}}^{-2}G(\zeta)$ is $B$-positive definite for
$0\ne\zeta\in{}^{3\mathrm b}T^*_\Omega M^\flat$.

*Proof.* Lemmas 3.3-3.8 are Part IV$''''$ Lemma 1.1 (record 10.13 (i)); Corollary 3.6 follows from Lemma 3.5 on one
fibre, as his proof does. For Lemma 3.9, his proof evaluates $(L_h-L_h^*)\omega$ at a point $p$ for an $\omega$
covariantly constant at $p$. It uses (3.10), the formula $(2ih)^{-1}L_h^{*g^{-1}} =
-ec\,\delta_g-2\iota_{c^\sharp}\delta^*_g$, which follows from (3.2), and the map $\tilde b_{g,c,e}$ of (3.7). These are
index computations in which the dimension appears only as the range of summation, and the metric adjoint is taken with
$|dg|$ in every dimension. For the uniform $C$, note that $\rho_{\mathrm{sf}}^{-2}G$ and $\rho_{\mathrm{sf}}^{-2}\ell$
are smooth homogeneous functions on ${}^{3\mathrm b}T^*M^\flat$ (Lemma 0.2 (a), (d)), and $B$ is continuous on the
compact $\Omega$, $K^+$ and $\mathrm{sf}$ included. Corollary 3.6 at each point and compactness of the unit sphere
bundle over $\Omega$ give one $C$ (his p. 47), and continuity in $b$ gives it for $b\in U$, shrinking $U$. $\square$

**Lemma 0.5 (the 1-form; [Hin26a] Proposition 5.1 at n = 4).** Let $(\alpha_{\mathrm{sf}},\alpha_K) = (-C_0-\frac52,1)$
with $C_0\in[0,100]$, the weights (2.1) of Part IV$''''$. Put $w :=
\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}+1}\rho_K^{\alpha_K}$ and $w' := \rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}+1}$.
Shrinking $U$, there are $\delta_r\in(0,(4r_c)^{-1})$ and $\delta_{\mathrm{sf}} = \frac1{100}$ such that for $b\in U$,
$c$ satisfies his Proposition 5.1 (1)-(6) with $r_c$ for $r_0$ and $r_\sharp$ for $m$. The positivity statements (3)-(6)
hold with lower bounds uniform in $b\in U$.

*Proof.* Part IV$''''$ Lemma 1.4 (record 10.14; 10.22 (c), (iv)), with the reading of (4)-(5) recorded in (IV$'''''$3).
Each positivity is a strict inequality for a continuous function of $(b,\text{point})$ on a compact set, or holds at
$\mathrm{sf}$, where every $g$, $b\in U$, has the 3sc model $\eta$ (Lemma 0.2 (a)); so the lower bounds are uniform
after shrinking $U$, $\delta_r$ and keeping $\delta_{\mathrm{sf}}$. $\square$

*Notation (his (5.19)).* $P_h = \Box_h-iL_h$, with $\Box_h := h^2\Box_g$, $\ell$, $B$ and $S$ as above.
$\langle\cdot,\cdot\rangle$ is the $L^2(M^\flat,|dg|;\mathcal T^*)$-pairing with $B$. Schwartz kernels of
pseudodifferential operators are supported in $\Omega'\times\Omega'$, $\Omega' :=
\Omega\setminus(X_0\cup\Sigma^\sharp)$. $\Sigma\subset{}^{3\mathrm b}T^*M^\flat$ is the closure of $G^{-1}(0)$, the
characteristic set of $h^2\rho_{\mathrm{sf}}^{-2}\Box_g$; $\partial\Sigma = \partial\Sigma_+\sqcup\partial\Sigma_-$ are
its components at fibre infinity, the future and past light cones; $o$ is the zero section. $|\cdot|$ is a fixed fibre
norm on ${}^{3\mathrm b}T^*M^\flat$. A *square root* below is always of a $B$-self-adjoint endomorphism field that is
positive semidefinite on the support in question, and it is smooth wherever the argument is a smooth function times a
positive definite field, or is positive definite. The source arranges this through the cut-off conditions
$(\mp\chi\chi')^{1/2}\in C^\infty$.

## 1. Elliptic estimates and the characteristic set at fibre infinity ([Hin26a] section 5.2.1)

**Lemma 1.1 ([Hin26a] Lemma 5.4).** The semiclassical 3b-characteristic set of $\rho_{\mathrm{sf}}^{-2}P_h$ is
$\partial\Sigma\cup o$.

*Proof.* $\rho_{\mathrm{sf}}^{-2}G$ and $\rho_{\mathrm{sf}}^{-2}\ell$ are homogeneous of degrees 2 and 1 on the fibres
(Lemma 0.2), so the symbol vanishes on $o$. At finite $\zeta\ne0$, $p(\zeta)$ is invertible by Lemma 0.4 (his Lemma
3.7). At fibre infinity $G$ is principal and $\ell$ subprincipal, so the characteristic set there is $\partial\Sigma$.
$\square$

*Cut-offs.* With $T := T_0$ of Lemma 0.3 and $\hat r$ for the source's $r_+$, let $\chi_{\tau,j}(\tau)$ and
$\chi_{r,j}(r)$, $j = 0,1,2$, be his (5.20):

- $\chi_{\tau,j} = 0$ for $\tau\le\frac{j+1/4}{10}T$ and $\chi_{\tau,j} = 1$ for $\tau\ge\frac{j+3/4}{10}T$;

- $\chi_{r,j} = 0$ for $r\le r_\sharp+\frac{j+1/4}{10}(\hat r-r_\sharp)$ and $\chi_{r,j} = 1$ for $r\ge
r_\sharp+\frac{j+3/4}{10}(\hat r-r_\sharp)$;

- $\chi'_{\bullet,j}\ge0$ and $(\chi_{\bullet,j}\chi'_{\bullet,j})^{1/2}\in C^\infty$.

So $\chi_{\bullet,j} = 1$ near $\mathrm{supp}\,\chi_{\bullet,j+1}$,
$\mathrm{supp}\,d\chi_{\tau,j}\subset\tau^{-1}([0,T_0))$, and $\mathrm{supp}\,d\chi_{r,j}\subset r^{-1}([r_\sharp,\hat
r))$.

**Proposition 1.2 ([Hin26a] Proposition 5.5).** Let $B_0,B_1\in\Psi^0_{3\mathrm b,\hbar}(M^\flat)$ with
$\mathrm{WF}'_{3\mathrm b,\hbar}(B_j)\cap(o\cup\partial\Sigma) = \emptyset$ and $\mathrm{WF}'_{3\mathrm
b,\hbar}(B_0)\subset\mathrm{Ell}_{3\mathrm b,\hbar}(B_1)$. Then for all $s,N$ there is $C$ with
$$\|B_0\chi_{\tau,2}\chi_{r,2}\omega\|_{H^{s,(\alpha_{\mathrm{sf}},\alpha_K)}_{3\mathrm b,h}}\le
C\big(\|B_1\chi_{\tau,1}\chi_{r,1}P_h\omega\|_{H^{s-2,(\alpha_{\mathrm{sf}}+2,\alpha_K)}_{3\mathrm
b,h}}+h^N\|\chi_{\tau,0}\chi_{r,0}\omega\|_{H^{-N,(\alpha_{\mathrm{sf}},\alpha_K)}_{3\mathrm b,h}}\big),$$
and the same for $P_h^*$.

*Proof.* Put $\omega' := \chi_{\tau,0}\chi_{r,0}\omega$. Then $\chi_{\tau,1}\chi_{r,1}P_h\omega' =
\chi_{\tau,1}\chi_{r,1}P_h\omega$ and $\chi_{\tau,2}\chi_{r,2}\omega = \chi_{\tau,2}\chi_{r,2}\omega'$. By Lemma 1.1,
$\rho_{\mathrm{sf}}^{-2}P_h$ is elliptic on $\mathrm{WF}'(B_1)$. A microlocal parametrix in the calculus of Definition
0.1 gives the estimate; the weights only add terms of lower order, since $w^{-1}[P_h,w]\in
h\rho_{\mathrm{sf}}^2\mathrm{Diff}^1_{3\mathrm b}$ for $w = \rho_{\mathrm{sf}}^{\beta}\rho_K^{\beta'}$. $\square$

**Proposition 1.3 ([Hin26a] Proposition 5.6).** The statement of his Proposition 5.6, (5.21) and (5.22), holds on
$(M^\flat,g,c)$ with the cut-offs above, in the strong sense stated there.

*Proof.* We prove (5.21) for $\omega\in H^{s,(\alpha_{\mathrm{sf}},\alpha_K)}_{3\mathrm b,h}$; the strong sense follows
by the standard regularisation (his p. 45). By Proposition 1.2 it suffices to work in an $h$-independent neighbourhood
of $\partial\Sigma_\pm$; replace $\omega$ by $\chi_{\tau,0}\chi_{r,0}\omega$. Let $\hat\rho$ define fibre infinity,
$\hat G := \hat\rho^2\rho_{\mathrm{sf}}^{-2}G$, $\chi\in C^\infty_c(\mathbb R)$ equal to 1 near 0, and $\chi_\pm$
localise near $\partial\Sigma_\pm$. Take the commutant (5.24),
$$a := \rho_{\mathrm{sf}}^{-\alpha_{\mathrm{sf}}-1}\rho_K^{-\alpha_K}\hat\rho^{-s+\frac12}\chi_\pm\chi(\mathfrak
X\hat\rho)\chi(\mathfrak X\hat G)\chi_{\tau,1}\chi_{r,1},$$
and a quantisation $A = A^*$ with $\mathrm{WF}'(A) = \mathrm{supp}\,a$. Then (5.25) holds:
$$\mp\mathrm{Im}\langle P_h\omega,A^2\omega\rangle =
\big\langle\big(\pm(\mathrm{Re}\,L_h-\mathrm{Im}\,\Box_h)A^2\mp\tfrac i2[P_h,A^2]\big)\omega,\omega\big\rangle.$$

*The main term.* On $\mathrm{supp}\,a$, for $\mathfrak X$ large, the covectors are close to future (for $+$), resp. past
(for $-$) lightlike covectors. $c$ is past timelike (Lemma 0.5 (1)), so Lemma 0.4 (his Lemma 3.5) makes
$\pm\rho_{\mathrm{sf}}^{-2}\ell$ positive definite there, with a lower bound fixed by compactness.
$\mathrm{Im}\,\Box_h\in h\mathrm{Diff}^1_{3\mathrm b,\hbar}$ is semiclassically subprincipal, $\Box_h$ having real
scalar principal symbol. This gives (5.26): $\pm(\mathrm{Re}\,L_h-\mathrm{Im}\,\Box_h)A^2 = A(\tilde B_0^*\tilde
B_0+c_0\Lambda^*\Lambda)A+hE$.

*The commutator and the cut-offs.* $\mp\frac i2[P_h,A^2]$ has principal symbol $\mp aH_Ga$ at order $h$ (5.27). In
(5.29) it is split as follows:

- differentiation of $\chi_\pm$ and $\chi(\mathfrak X\hat G)$ lands off the characteristic set, so these terms are
$hAQP_h$;

- differentiation of $\chi(\mathfrak X\hat\rho)$ gives order $-\infty$;

- differentiation of the weights gives bounded multiples of $a^2$, the term $hA\tilde B_2A$;

- $\mp\chi_{\tau,1}H_G\chi_{\tau,1} = \mp\chi_{\tau,1}\chi'_{\tau,1}H_G\tau = -e_T^2$, because $H_G\tau =
2g^{-1}(\zeta,d\tau)$ is positive at future and negative at past lightlike $\zeta$ over
$\mathrm{supp}\,d\chi_{\tau,1}\subset\tau^{-1}([0,T_0))$, where $d\tau$ is past timelike (Lemma 0.3 (b));

- $\mp\chi_{r,1}H_G\chi_{r,1} = +e_R^2$, because $H_Gr = 2g^{-1}(\zeta,dr)$ is negative at future and positive at past
lightlike $\zeta$ over $\mathrm{supp}\,d\chi_{r,1}\subset r^{-1}([r_\sharp,\hat r))$, where $dr$ is future timelike
(Lemma 0.3 (c)).

*Conclusion.* Cauchy-Schwarz on the left of (5.25) gives (5.30). Drop $\|E_R\omega\|^2$, which has the sign of the main
term, and absorb $h\langle\tilde B_2A\omega,A\omega\rangle\le Ch\|\tilde B_0A\omega\|^2+h^N\|\omega\|^2$. Iterate in
$h^{1/2}$ on the error term $h^{1/2}\|\tilde B'_0\omega\|$, whose wave front set lies near $\mathrm{supp}\,a$. This
proves (5.21); the a priori term is $h^{1/2}\|E_T\omega\|$, supported over $\mathrm{supp}\,d\chi_{\tau,1}$.

For (5.22), $P^*_h = \Box^*_h+iL^*_h$ with $\Box^*_h-\Box_h\in h\mathrm{Diff}^1$ and $L^*_h-L_h\in h\mathrm{Diff}^0$,
and (5.28) has main term $\mp\rho_{\mathrm{sf}}^{-2}\ell$, now negative definite. The weights in $a$ become
$(-\alpha_{\mathrm{sf}}-2,-\alpha_K)$. (5.29) holds for $P^*_h$, as only $\Box^*_h$, with principal symbol $G$, entered
it. Now $-e_T^2$ has the sign of the main term and $e_R^2$ needs the a priori term. $\square$

## 2. The saddle point at r = r_c ([Hin26a] section 5.2.2)

By Lemma 0.4 there is $C$ with $C(\rho_{\mathrm{sf}}^{-2}\ell)^2+\rho_{\mathrm{sf}}^{-2}G>0$ on ${}^{3\mathrm
b}T^*_\Omega M^\flat\setminus o$. As in his (5.31)-(5.32), define
$$\mathcal L_h := -i(1+iCL^*_h\rho_{\mathrm{sf}}^{-2})P_h = -L_h+J-iQ\in\rho_{\mathrm{sf}}^2\mathrm{Diff}^3_{3\mathrm
b,\hbar},\tag{2.1}$$
with $J = h^2J_0+h^3J_1$, $J_0 = \mathrm{Im}\,\Box_g$, $J_1 = Ch^{-3}\mathrm{Re}(L^*_h\rho_{\mathrm{sf}}^{-2}\Box_h)$,
$Q = h^2Q_0+h^3Q_1$, $Q_0 = h^{-2}\mathrm{Re}(\Box_h+CL^*_h\rho_{\mathrm{sf}}^{-2}L_h)$ and $Q_1 =
-Ch^{-3}\mathrm{Im}(L^*_h\rho_{\mathrm{sf}}^{-2}\Box_h)$. The memberships $J_0\in\rho^2\mathrm{Diff}^1_{3\mathrm b}$,
$J_1\in\rho^2\mathrm{Diff}^3_{3\mathrm b}$, $Q_0\in\rho^2\mathrm{Diff}^2_{3\mathrm b}$ and
$Q_1\in\rho^2\mathrm{Diff}^2_{3\mathrm b}$ follow from Lemma 0.2 (d) and the self-adjointness of $\ell$.
$1+iCL^*_h\rho_{\mathrm{sf}}^{-2}$ is semiclassically elliptic everywhere, its principal symbol $1+iC\rho^{-2}\ell$
being invertible ($\ell$ self-adjoint). The symbol $j$ of $J$ is homogeneous of degree 3 and vanishes cubically at $o$.
Near $(K^+)^\circ$, $\rho_K := t^{-1}$, and the weight at $\mathrm{sf}$ and the differential order are dropped.

**Proposition 2.1 ([Hin26a] Proposition 5.8).** The statement of his Proposition 5.8, (5.33) and (5.34), holds with
$r_c$ for $r_0$.

*Proof.* (1) By Proposition 1.2 and the ellipticity of $1+iCL^*_h\rho_{\mathrm{sf}}^{-2}$ it suffices to prove (5.33)
with $\mathcal L_h$ for $P_h$, near $o$. With $\chi_0$, $\chi_K$ and $\psi$ as in his (5.35) ($r_c$ for $r_0$), take the
commutant (5.36), $a = \rho_K^{-\alpha_K}\psi(r)\chi_K(\mathfrak X\rho_K)\chi_0(\mathfrak X|\zeta|)$, and $A = A^*$. The
pairing is (5.37)-(5.38):
$$h^{-1}\mathrm{Im}\langle\mathcal L_h\omega,A^2\omega\rangle = \langle\mathcal C\omega,\omega\rangle,\qquad\mathcal C =
\big(\tfrac i{2h}[-L_h+J,A^2]-h^{-1}(\mathrm{Im}\,L_h)A^2\big)-h^{-1}AQA-\tfrac1{2h}[A,[A,Q]].$$
The bracket has principal symbol $aH_{-\ell+j}a-Sa^2$. As $\ell$ is linear in the fibre, $H_{-\ell}f = -\ell(df)$ for a
function $f$ on $M^\flat$. This gives (5.39), $aH_{-\ell+j}a-Sa^2 = -c_0a^2-b_0^2-b_R^2+e^2+f$, with $b_0$, $b_R$, $e$
and $f$ his (5.40)-(5.43). Their square roots exist for the following reasons.

- $b_0$: $S$ is positive definite on $\{|r-r_c|\le\frac65r_c\sqrt e/v\}$ (Lemma 0.5 (3)), so $S\ge2c_0$ there.
$\ell(d\rho_K/\rho_K^2) = -\ell(dt)$ and $H_j\rho_K^{-1}$ are bounded on $\mathrm{supp}\,\chi_0(\mathfrak X|\zeta|)$ and
carry the factor $\rho_K\lesssim\mathfrak X^{-1}$.

- $b_R$: on $\mathrm{supp}\,\psi'\cap\{\pm(r-r_c)>0\}$, $-\ell(\pm dr)\ge2c_1$ (Lemma 0.5 (6)), and $|H_jr| =
O(|\zeta|^2)<c_1$ on $\mathrm{supp}\,\chi_0(\mathfrak X|\zeta|)$ for $\mathfrak X$ large.

- $e$: $d\rho_K/\rho_K^2 = -dt$ is future timelike (Lemma 0.3 (d)), so $\ell(-dt)$ is positive definite (Lemma 0.4), and
$-\chi_K\chi'_K\ge0$; $e$ is supported away from $\rho_K = 0$.

- $f$ is supported off $o$, where Proposition 1.2 applies.

For $Q$:

- $Q_0$ has the positive definite principal symbol $G+C\rho_{\mathrm{sf}}^{-2}\ell^2$ (Lemma 0.4), so $Q_0 =
\Theta^*\Theta+R$ with $R\in\Psi^{-\infty}_{3\mathrm b}$, which is (5.44).

- The symbol of $h^{-1}h^3Q_1$ vanishes quadratically at $o$, so it is $O(\mathfrak X^{-2})$ on $\mathrm{supp}\,a$,
which gives (5.45) by Gårding.

- The double commutator lies in $h\Psi$ and gives (5.46).

Collecting, fix $\mathfrak X$ large and then $h$ small to absorb $\|A\omega\|^2$. Then (5.47), with
$\mathrm{WF}'(F)\subset\mathrm{Ell}(\mathcal L_h)$, gives (5.48), and finitely many iterations in $h^{1/2}$ give (5.33),
with $\delta := \mathfrak X^{-1}$.

(2) Replace $P^*_h$ by $\mathcal L^*_h = iP^*_h(1-iC\rho_{\mathrm{sf}}^{-2}L_h) = -L^*_h+J+iQ$ and take $a =
\rho_K^{\alpha_K}\psi\chi_K(\mathfrak X\rho_K)\chi_0(\mathfrak X|\zeta|)$. The main symbol is $aH_{-\ell+j}a+Sa^2 =
c_0a^2+b_0^2+b_K^2-e^2+f$ with his $b_0,b_K,e,f$. The same three facts give the square roots, now with $b_K$ from
$-\ell(dt)$'s sign and $e$ from Lemma 0.5 (6) on $\mathrm{supp}\,\psi'$. $Q$ enters with a lower bound by (5.44)-(5.45),
and the iteration is the same. $\square$

## 3. The saddle point at the corner $\partial K^+$ ([Hin26a] section 5.2.3)

From here on, $\rho_K = r/t$ and $\rho_{\mathrm{sf}} = 1/r$.

**Proposition 3.1 ([Hin26a] Proposition 5.9).** The statement of his Proposition 5.9, (5.51) and (5.52), holds with the
weights of Lemma 0.5.

*Proof.* (1) Replace $P_h$ by $\mathcal L_h$. With $\chi_{\mathrm{sf}}$, $\chi_K$ and $\chi_0$ as in his proof, take the
commutant (5.53), $a = w^{-1}\chi_{\mathrm{sf}}(\mathfrak X\rho_{\mathrm{sf}})\chi_K(\rho_K)\chi_0(\mathfrak X|\zeta|)$.
Then $\mathcal C\in\rho_{\mathrm{sf}}^{-2\alpha_{\mathrm{sf}}}\rho_K^{-2\alpha_K}\Psi_{3\mathrm b}$, and (5.54) holds:
$aH_{-\ell+j}a-Sa^2 = -c_0\rho_{\mathrm{sf}}^2a^2-b_0^2-b_{\mathrm{sf}}^2+e^2+f$, with his $b_0$, $b_{\mathrm{sf}}$, $e$
and $f$. Their square roots exist for the following reasons.

- $b_0$: $\rho_{\mathrm{sf}}^{-2}(-\ell(dw/w)+S)$ is positive definite on
$\{\rho_{\mathrm{sf}}\le2\delta_r,\rho_K\le2\delta_r\}$ (Lemma 0.5 (4)), with a fixed lower bound.
$\rho_{\mathrm{sf}}^{-2}w^{-1}H_jw$ vanishes at $o$, since $\rho_{\mathrm{sf}}^{-2}j$ vanishes cubically there.

- $b_{\mathrm{sf}}$: on $\mathrm{supp}\,\chi'_K$, $\rho_K\in[\frac54\delta_r,\frac32\delta_r)$, and Lemma 0.5 (6) on
$\mathrm{sf}\cap\{r/t\in[\delta_r,v(1-\delta_{\mathrm{sf}})]\}$ gives $\rho_{\mathrm{sf}}^{-2}(-\ell(d\rho_K))>0$ near
$\mathrm{sf}$ for $\mathfrak X$ large.

- $e$: $d\rho_{\mathrm{sf}}/\rho_{\mathrm{sf}}^2 = -dr$ and $-\ell(dr)$ is positive definite for $r\ge r_c+r_c\sqrt e/v$
(Lemma 0.5 (6)); $H_jr$ vanishes at $o$.

$e$ is supported away from $\mathrm{sf}$ and gives the a priori term. Estimating the left side by
$c_0^{-1}h^{-2}\|\rho_{\mathrm{sf}}^{-1}A\mathcal L_h\omega\|^2+\frac14c_0\|\rho_{\mathrm{sf}}A\omega\|^2$ produces the
weights of (5.51). The rest is the proof of Proposition 2.1, with $\delta := \mathfrak X^{-1}$.

(2) Take $a = w\chi_{\mathrm{sf}}(\mathfrak X\rho_{\mathrm{sf}})\chi_K(\rho_K)\chi_0(\mathfrak X|\zeta|)$ and the
pairing with $\mathcal L^*_h$. Then $aH_{-\ell+j}a+Sa^2 = c_0\rho_{\mathrm{sf}}^2a^2+b_0^2+b_K^2-e^2+f$, with his
symbols. These are (1)'s with $-\alpha_{\mathrm{sf}}-2$ for $\alpha_{\mathrm{sf}}$; $b_0$ comes from Lemma 0.5 (4), and
the a priori term from $\mathrm{supp}\,\chi'_K$. $\square$

## 4. The sink in $\mathrm{sf}^\circ$ ([Hin26a] section 5.2.4)

**Proposition 4.1 ([Hin26a] Proposition 5.11).** The statement of his Proposition 5.11, (5.55) and (5.56), holds with
$w' = \rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}+1}$ and $\delta_{\mathrm{sf}}$ of Lemma 0.5.

*Proof.* (1) The commutant is $a = (w')^{-1}\chi_{\mathrm{sf}}(\mathfrak
X\rho_{\mathrm{sf}})\chi_R(\frac{r/t}v-1)\chi_0(\mathfrak X|\zeta|)$, with $\chi_R$ supported in
$(-2\delta_{\mathrm{sf}},2\delta_{\mathrm{sf}})$ and equal to 1 on
$[-\frac54\delta_{\mathrm{sf}},\frac54\delta_{\mathrm{sf}}]$. Then (5.57) holds: $aH_{-\ell+j}a-Sa^2 =
-c_0\rho_{\mathrm{sf}}^2a^2-b_0^2+e_1^2+e_2^2+f$. Their square roots exist for the following reasons.

- $b_0$: Lemma 0.5 (5), for $\mathfrak X$ large.

- $e_1$: $d\rho_{\mathrm{sf}}/\rho_{\mathrm{sf}}^2 = -dr$, $H_j(\rho_{\mathrm{sf}}^{-1}) = H_jr$, and Lemma 0.5 (6) for
large $r$.

- $e_2$: on $\mathrm{supp}\,d\chi_R$, $|\frac{r/t}v-1|\in[\frac54\delta_{\mathrm{sf}},2\delta_{\mathrm{sf}}]$, where the
sign of $-r^2\ell(d(r/t))$ is that of $\chi'_R$ (Lemma 0.5 (6) on the two sides of the sink).

$e_1$ and $e_2$ are supported away from $\{|\frac{r/t}v-1|\le\delta_{\mathrm{sf}},\rho_{\mathrm{sf}}\le\mathfrak
X^{-1}\}$ and give $\|E\omega\|$. The rest is Proposition 2.1's proof.

(2) Take $a = w'\chi_{\mathrm{sf}}(\mathfrak X\rho_{\mathrm{sf}})\chi_R(\frac{r/t}v-1)\chi_0(\mathfrak X|\zeta|)$. Then
$aH_{-\ell+j}a+Sa^2 = c_0\rho_{\mathrm{sf}}^2a^2+b_0^2+b_1^2+b_2^2+f$. Every term except $f$, which is elliptic, has the
sign of the main term, by the same three facts. So (5.56) carries no a priori term. $\square$

## 5. Propagation between the critical sets ([Hin26a] section 5.2.5, and what it leaves to the reader)

**Proposition 5.1 ([Hin26a] Proposition 5.12).** The statement of his Proposition 5.12, (5.58) and (5.59), holds with
$r_3 := r_c-\frac{52}{50}r_c\sqrt e/v$, $r_4 := r_c-\frac{51}{50}r_c\sqrt e/v$ and $r_\sharp<r_1<r_2<r_3$, near $K^+$
with $\rho_K = t^{-1}$.

*Proof.* (1) The commutant is $a = \rho_K^{-\alpha_K}\chi_1(r-r_1)\chi_2(r)\chi_K(\rho_K)\chi_0(\mathfrak X|\zeta|)$,
where $\chi_1(x) = e^{-\mathfrak X/x}$ for $x>0$, so $\chi'_1(x) = \mathfrak Xx^{-2}\chi_1(x)$. Then (5.60) holds:
$aH_{-\ell+j}a-Sa^2 = -a^2-b_0^2+e_R^2+e_T^2+f$, with his $b_0$, $e_R$, $e_T$ and $f$. The square roots exist for the
following reasons.

- $b_0$: on $[r_1,r_4]\subset[r_\sharp,r_c-r_c\sqrt e/v]$, $-\ell(-dr)$ is positive definite (Lemma 0.5 (6)), so
$-\mathfrak X(r-r_1)^{-2}(-\ell(dr)+H_jr)\ge C$ for any fixed $C$ once $\mathfrak X$ is large.

- $e_R$: $\chi_2$ is decreasing and $\ell(dr)$ is positive definite there.

- $e_T$: $d\rho_K/\rho_K^2 = -dt$ is future timelike, so $\ell(-dt)>0$ (Lemmas 0.3 (d), 0.4).

$e_R$ (on $\mathrm{supp}\,\chi'_2\chi_K$) and $e_T$ (on $\mathrm{supp}\,\chi_2\chi'_K$) give $\|E\omega\|$. The rest is
as before.

(2) Take $a = \rho_K^{\alpha_K}\chi_1(r_4-r)\tilde\chi_2(r)\chi_K(\rho_K)\chi_0(\mathfrak X|\zeta|)$, with $\tilde\chi_2
= 0$ near $(-\infty,r_1]$ and $1$ near $[r_2,\infty)$. Then $aH_{-\ell+j}a+Sa^2 = a^2+b_0^2+b_T^2-e_R^2+f$, and the only
a priori term is $e_R$, on $\mathrm{supp}\,\tilde\chi'_2$. $\square$

The source states the next propagations as "completely analogous" and leaves them to the reader (pp. 57-58). They are
stated and proved here, both directions included, since the combination in section 7 uses each.

**Proposition 5.2 (propagation along $K^+$ outward, and along $\mathrm{sf}$).** Let $B_0,B_1,E\in\Psi_{3\mathrm
b,\hbar}$ have compact operator wave front sets in $\{|\zeta|<2\}$ and Schwartz kernels supported in a compact $\mathcal
K$ as specified, with $\chi = 1$ on $\mathcal K$. Each item asserts estimate (1) for $P_h$, of the form (5.58), and
estimate (2) for $P_h^*$, of the form (5.59). In each the sf-weight $\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}$ (resp.
$\rho_{\mathrm{sf}}^{-\alpha_{\mathrm{sf}}-2}$) is included in (b)-(c), and $P_h\omega$ carries two more powers of
$\rho_{\mathrm{sf}}$ as in (5.55).

(a) (*Along $K^+$, $r>r_c$.*) Let $r'_1 := r_c+\frac{51}{50}r_c\sqrt e/v<r'_2 := r_c+\frac{52}{50}r_c\sqrt
e/v<r'_3<r'_4<\infty$ and $0<t_1<t_2<t_3$, with $\rho_K = t^{-1}$. Let $\mathrm{WF}'(B_0)\subset\{\rho_K\le
t_2^{-1},r'_1<r<r'_4,|\zeta|<1\}$, $\mathrm{Ell}(B_1)\supset\{\rho_K\le t_1^{-1},r'_1\le r\le r'_4,|\zeta|<2\}$, and in
(1)
$$\mathrm{Ell}(E)\supset\{t_3^{-1}\le\rho_K\le t_1^{-1},r'_1\le r\le r'_4,|\zeta|<1\}\cup\{\rho_K\le t_1^{-1},r'_1\le
r\le r'_2,|\zeta|<1\},$$
while in (2) $\mathrm{Ell}(E)\supset\{\rho_K\le t_1^{-1},r'_3\le r\le r'_4,|\zeta|<1\}$.

(b) (*Along $\mathrm{sf}$, below the sink.*) Let $s := r/t$, $\delta_r\le s_1<s_2<s_3<s_4 := v(1-\delta_{\mathrm{sf}})$
and $\delta'>0$ small. Let $\mathrm{WF}'(B_0)\subset\{s_1<s<s_4,\rho_{\mathrm{sf}}\le\delta',|\zeta|<1\}$ and
$\mathrm{Ell}(B_1)\supset\{s_1\le s\le s_4,\rho_{\mathrm{sf}}\le2\delta',|\zeta|<2\}$. In (1),
$$\mathrm{Ell}(E)\supset\{s_1\le s\le s_2,\rho_{\mathrm{sf}}\le2\delta'\}\cup\{s_1\le s\le
s_4,\delta'\le\rho_{\mathrm{sf}}\le2\delta'\}$$
(intersected with $|\zeta|<1$), and in (2) $\mathrm{Ell}(E)\supset\{s_3\le s\le
s_4,\rho_{\mathrm{sf}}\le2\delta',|\zeta|<1\}$.

(c) (*Along $\mathrm{sf}$, above the sink.*) The same as (b) with $s_4 := v(1+\delta_{\mathrm{sf}})<s_3<s_2<s_1\le10$
and the inequalities in $s$ reversed.

*Proof.* Each is the proof of Proposition 5.1 with a different escape function $\phi$ and, in (b)-(c), the sf-cut-off
and weight of Proposition 4.1. The escape functions are $\phi = r$ in (a), $\phi = s$ in (b) and $\phi = -s$ in (c).
Each satisfies $-\ell(d\phi)$ positive definite on the support in question, by Lemma 0.5 (6): $-\ell(dr)>0$ for $r\ge
r_c+r_c\sqrt e/v$, $-r^2\ell(ds)>0$ on $\mathrm{sf}\cap\{s\in[\delta_r,v(1-\delta_{\mathrm{sf}})]\}$, and
$-r^2\ell(-ds)>0$ on $\mathrm{sf}\cap\{s\in[v(1+\delta_{\mathrm{sf}}),10]\}$. The last two persist to
$\{\rho_{\mathrm{sf}}\le2\delta'\}$ for $\delta'$ small, by continuity on the compact $s$-intervals. With $\phi_1 <
\phi_4$ the values of $\phi$ at the two ends (in (a) $r'_1$, $r'_4$; in (b) $s_1$, $s_4$; in (c) $-s_1$, $-s_4$), take
in (1)
$$a = W^{-1}\chi_1(\phi_4-\phi)\tilde\chi_2(\phi)\chi_\star\chi_0(\mathfrak X|\zeta|),$$
with $\chi_1(x) = e^{-\mathfrak X/x}$ as before, $\tilde\chi_2 = 0$ near $\phi\le\phi_1$ and $1$ near $\phi\ge\phi_2$,
and
$$(W,\chi_\star) = (\rho_K^{\alpha_K},\chi_K(\rho_K))\ \text{in (a)},\qquad(W,\chi_\star) =
(w',\chi_{\mathrm{sf}}(\rho_{\mathrm{sf}}/\delta'))\ \text{in (b)-(c)}.$$
The terms of $aH_{-\ell+j}a$ are signed as follows.

- *Main term.* $H_{-\ell}\chi_1(\phi_4-\phi) = -\chi'_1(\phi_4-\phi)\,(-\ell(d\phi))$, which is negative definite with
$\chi'_1/\chi_1 = \mathfrak X(\phi_4-\phi)^{-2}\ge\mathfrak X(\phi_4-\phi_1)^{-2}$. For $\mathfrak X$ large it dominates
$S$, the weight term $W^{-1}H_{-\ell}W$ and the $j$-terms. These are bounded on $\mathrm{supp}\,a$ in the rescaled
sense: $\rho_{\mathrm{sf}}^{-2}S$, $\rho_{\mathrm{sf}}^{-2}\ell(dw'/w')$ and $\rho_{\mathrm{sf}}^{-2}H_j$ of functions
are bounded near $\mathrm{sf}$ (Lemma 0.2 (d)), and $j = O(|\zeta|^3)$. This gives $-a^2-b_0^2$.

- *$\tilde\chi_2$.* $H_{-\ell}\tilde\chi_2(\phi) = \tilde\chi'_2(-\ell(d\phi))\ge0$, of the opposite sign. It is
supported near the start, where (1) assumes control.

- *$\chi_\star$ in (a).* $H_{-\ell}\chi_K(t^{-1}) = \chi'_K\,\ell(dt)t^{-2}$, with $\chi'_K\le0$ and $\ell(dt)<0$ ($dt$
past timelike), so it is $\ge0$; it is supported at $\rho_K\in[t_3^{-1},t_1^{-1}]$, where (1) assumes control.

- *$\chi_\star$ in (b)-(c).* $H_{-\ell}\chi_{\mathrm{sf}}(\rho_{\mathrm{sf}}/\delta') =
\delta'^{-1}\chi'_{\mathrm{sf}}\rho_{\mathrm{sf}}^2\ell(dr)$, with $\chi'_{\mathrm{sf}}\le0$ and $\ell(dr)<0$ for large
$r$, so it is $\ge0$; it is supported at $\rho_{\mathrm{sf}}\in[\delta',2\delta']$, where (1) assumes control.

Each positive term is the square of a smooth symbol by the cut-off conditions of the notation, and gives $\|E\omega\|$.
The rest is the proof of Proposition 2.1: $\mathcal L_h$, the $Q$-terms (5.44)-(5.46), and the iteration.

In (2) the commutant is $W\chi_1(\phi-\phi_1)\tilde\chi_3(\phi)\chi_\star\chi_0$, with $\tilde\chi_3 = 1$ near
$\phi\le\phi_3$ and $0$ near $\phi\ge\phi_4$. The main term $H_{-\ell}\chi_1(\phi-\phi_1) = \chi'_1\,(-\ell(d\phi))$ is
now positive, the sign the adjoint pairing (5.49) needs. The $\chi_\star$-terms, $\ge0$, now have the sign of the main
term. The $\tilde\chi_3$-term, $\le0$, needs control at the far end. $\square$

**Proposition 5.3 (propagation through the interior of $\Omega$).** Weights play no role here, all supports being
compact in $\Omega\setminus(K^+\cup\mathrm{sf})$.

(1) (*Forward.*) Let $\kappa\in(0,1)$, $\phi := t+\kappa r$ and $T_2>0$. Let $\mathcal D := \{t\ge0,\phi\le T_2\}$,
which is compact, and let $0<\epsilon_X\le T_0r_\sharp/2$ and $\epsilon_r := \frac1{10}(\hat r-r_\sharp)$. Let
$\mathrm{WF}'(B_0)\subset\{\phi<T_2-\epsilon,\ t>\epsilon_X,\ r>r_\sharp+\epsilon_r,\ |\zeta|<1\}$ for some
$\epsilon>0$, let $B_1$ be elliptic on $\mathcal D\cap\{|\zeta|\le2\}$ away from $X_0\cup\Sigma^\sharp$, and let
$\mathrm{Ell}(E)\supset\{\frac12\epsilon_X\le t\le\epsilon_X,\ \phi\le T_2,\ |\zeta|<1\}$. Then
$$\|B_0\omega\|_{L^2}\le C\big(h^{-1}\|B_1P_h\omega\|_{L^2}+\|E\omega\|_{L^2}+h^N\|\chi\omega\|_{H^{-N}_{3\mathrm
b,h}}\big).$$
$\mathrm{Ell}(E)$ lies in $\tau^{-1}([0,T_0])$, since $t\le\epsilon_X$ and $r\ge r_\sharp$ give $\tau\le T_0/2$.

(2) (*Backward.*) Let $\kappa := \frac19$, $0<t_1<t_2$ and $c_1>0$. Let $\mathcal D' := \{t_1\le t\le t_2+1,\ t-\kappa
r\ge-c_1\}$, which is compact. Let $\mathrm{WF}'(B_0)\subset\{2t_1<t<t_2,\ t-\kappa r>0,\
r>r_\sharp+\epsilon_r,\ |\zeta|<1\}$, let $B_1$ be elliptic on $\mathcal D'\cap\{|\zeta|\le2\}$ away from
$\Sigma^\sharp$, and let
$$\mathrm{Ell}(E)\supset\big(\{t_2\le t\le t_2+1\}\cup\{r_\sharp+\tfrac12\epsilon_r\le r\le
r_\sharp+\epsilon_r\}\big)\cap\mathcal D'\cap\{|\zeta|<1\}.$$
Then the same estimate holds for $P^*_h$.

*Proof.* (1) $d\phi$ and $dt$ are past timelike (Lemma 0.3 (a)), so $-\ell(d\phi)$ and $-\ell(dt)$ are positive definite
on $\mathcal D$ (Lemma 0.4, his Lemma 3.5), with a lower bound by compactness. On
$\mathrm{supp}\,\chi'_r\subset[r_\sharp,r_\sharp+\epsilon_r]$, $-\ell(-dr)>0$ (Lemma 0.5 (6),
$r_\sharp+\epsilon_r<r_c-r_c\sqrt e/v$). Take
$$a = \chi_1(T_2-\phi)\,\tilde\chi(t)\,\chi_r(r)\,\chi_0(\mathfrak X|\zeta|),$$
with $\tilde\chi = 0$ on $t\le\frac12\epsilon_X$ and $1$ on $t\ge\epsilon_X$, and $\chi_r = 0$ near $r\le
r_\sharp+\frac12\epsilon_r$ and $1$ on $r\ge r_\sharp+\epsilon_r$, both non-decreasing. The terms of $aH_{-\ell+j}a$ are
signed as follows.

- $H_{-\ell}\chi_1(T_2-\phi) = -\chi'_1(-\ell(d\phi))$ is the negative main term, dominating $S$ and $j$ for $\mathfrak
X$ large.

- $H_{-\ell}\tilde\chi(t) = \tilde\chi'(-\ell(dt))\ge0$ needs control on
$\mathrm{supp}\,\tilde\chi'\subset\mathrm{Ell}(E)$.

- $H_{-\ell}\chi_r(r) = \chi'_r(-\ell(dr)) = -\chi'_r(-\ell(-dr))\le0$ has the sign of the main term and is dropped.

The rest is Proposition 2.1's proof. The supports avoid $X_0$ and $\Sigma^\sharp$, as the source's convention requires.

(2) $d(t-\kappa r)$ is past timelike (Lemma 0.3 (a), $\beta = \kappa$). Take
$$a = \chi_1(t-t_1)\,\chi_{\mathrm{late}}(t)\,f(t-\kappa r)\,\chi_r(r)\,\chi_0(\mathfrak X|\zeta|),$$
with $\chi_{\mathrm{late}}$ non-increasing, $1$ on $t\le t_2$ and $0$ on $t\ge t_2+1$, and $f$ non-decreasing, $0$ on
$(-\infty,-c_1]$ and $1$ on $[0,\infty)$. In the adjoint pairing (5.49) the main term must be positive. The terms are
signed as follows.

- $H_{-\ell}\chi_1(t-t_1) = \chi'_1(-\ell(dt))$ is positive and dominant.

- $H_{-\ell}f = f'(-\ell(d(t-\kappa r)))\ge0$ has its sign and is dropped.

- $H_{-\ell}\chi_{\mathrm{late}} = \chi'_{\mathrm{late}}(-\ell(dt))\le0$ needs control on $\{t_2\le t\le t_2+1\}$.

- $H_{-\ell}\chi_r\le0$ needs control near $\Sigma^\sharp$.

On $\mathrm{supp}\,a$, $r\le(t+c_1)/\kappa$ and $t\le t_2+1$, so the support is compact, and $\chi_1(t-t_1)$ is bounded
below on $\mathrm{WF}'(B_0)$. The rest is as in (1), with $\mathcal L^*_h$. $\square$

## 6. Energy estimates ([Hin26a] section 5.2.6)

His Lemma 5.14 is stated for an arbitrary time-oriented Lorentzian vector space, and his Corollary 5.15 on $\mathbb
R^{1+n}$ for every $n$ and on $n$-dimensional manifolds of bounded geometry (pp. 58-60). Both are used as stated, with
$n = 4$. Near $X_0$ the bounded geometry is that of $\tau$-level sets, with preferred charts products of charts on
$\mathbb S^3$ with dyadic intervals in $r$. Near $\Sigma^\sharp$ it is that of $r$-level sets, with charts on $\mathbb
S^3$ times unit intervals in $t$. The data required to lie in a compact subset of $C^\infty(I\times B_3)$ are $g$, $B$,
a 3b-connection, $\ell$ and $\phi$; they do so by Lemma 0.2 (a), (c), (d), uniformly for $b\in U$. The hypothesis on
$\ell$, positive definite on future causal covectors, is Lemma 0.4 (his Lemma 3.5).

**Proposition 6.1 ([Hin26a] Proposition 5.16 at n = 4).** His statements (5.66)-(5.69) hold with $T := T_0$, with $m\le
r_1<r_2<r_3<r_+$ read as $r_\sharp\le r_1<r_2<r_3\le\hat r$, and with the level-set density $r^4|dr\,d\slashed g|$ for
his $r^3|dr\,d\slashed g|$ in the norms on $\tau^{-1}(T)$. Moreover, at fixed $h$, for
$\omega\in\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}\bar H^2_{3\mathrm b}$ without support condition,
$$\|\omega\|_{\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}\bar H^1_{3\mathrm b}(\tau^{-1}([0,T_0]))}\le
C_h\big(\|P_h\omega\|_{\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}+2}L^2(\tau^{-1}([0,T_0]))}+\|(\omega,r\mathcal
L_{\partial_t}\omega)|_{X_0}\|_{\mathcal H_{\mathrm{data}}}\big),\tag{6.1}$$
where $\mathcal H_{\mathrm{data}} := \rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}\bar H^1_{\mathrm b}(X_0,r^4|dr\,d\slashed
g|)\oplus\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}\bar H^0_{\mathrm b}(X_0,r^4|dr\,d\slashed g|)$.

*Proof.* (5.66). Take the multiplier $a^2L_h$ with
$$a = \rho_{\mathrm{sf}}^{-\alpha_{\mathrm{sf}}-2}e^{-\mathfrak X\tau}H(T_0-\tau)H(r-r_\sharp)$$
($H$ the Heaviside function), and the pairing (5.70), $h^{-1}\mathrm{Im}\langle P_h\omega,a^2L_h\omega\rangle =
\langle\mathcal C\omega,\omega\rangle-h^{-1}\|aL_h\omega\|^2$. The principal symbol of $\mathcal C$ is
$aT_{G,da,\ell}-a^2E$ in the notation of (5.61), since $H_Ga = 2g^{-1}(\zeta,da)$. This leads to the decomposition
(5.71), whose derivation only expands $\frac i2(\Box^*_hbL_h-L^*_hb\Box_h)$ in local coordinates with $b = a^2$. Then
$a\,da$ is (5.72), and the weight identity (5.73) holds: $aT_{G,-da,\ell} =
\rho_{\mathrm{sf}}^4T_{\rho_{\mathrm{sf}}^{-2}G,-a\,da,\rho_{\mathrm{sf}}^{-2}\ell}$, by bilinearity, free of $n$.

$-a\,da$ is past timelike for $\mathfrak X$ large, since $d\tau$ is past timelike with
$r^2g^{-1}(d\tau,d\tau)\le-\frac34$ (Lemma 0.3 (b)) and the $\delta(r-r_\sharp)$-part of $-a\,da$ is a positive multiple
of $-dr$, past timelike (Lemma 0.3 (c)). So Corollary 5.15 is integrated over $\{r\ge r_\sharp,0\le\tau\le T_0\}$ twice:
with $d\tau$ and $\phi^2 = \mathfrak Xa^2+\rho_{\mathrm{sf}}^{-2\alpha_{\mathrm{sf}}-4}e^{-2\mathfrak
X\tau}\delta(T_0-\tau)$, and with $-dr$ and $\phi^2 =
\rho_{\mathrm{sf}}^{-2\alpha_{\mathrm{sf}}-4}e^{-2\mathfrak X\tau}\delta(r-r_\sharp)$. Here the level sets of $\tau$
carry $r^4|dr\,d\slashed g|$, which tensored with $|d\tau|$ is $|dg|$ (Lemma 0.2 (b)). This gives (5.74).

The other terms of (5.71) carry the total weight $\rho_{\mathrm{sf}}^4$ of $\nabla^*T\nabla$ and are bounded by (5.75)
and its companions. The left side of (5.70) is at least $-\frac12h^{-1}(\|aP_h\omega\|^2+\|aL_h\omega\|^2)$, which gives
(5.76). The fundamental theorem of calculus for $L_h$, (5.77), uses Lemma 0.4 (his Lemma 3.5) for the future timelike
covector $\rho_{\mathrm{sf}}a\,d(\rho_{\mathrm{sf}}a)$. It gives the bulk term $C\mathfrak X\rho_{\mathrm{sf}}^4a^2$ and
the two positive $\delta$-terms, hence (5.78). Adding (5.76) and (5.78) and absorbing for $h$ small gives (5.66).

(5.68) follows by the same argument with $a = \rho_K^{-\alpha_K}e^{\mathfrak Xr}H(r-r_1)$, applied to $\chi\omega$
($\chi = 1$ on $r\le r_2$, $0$ on $r\ge r_3$), as $-dr$ is past timelike on $[r_\sharp,\hat r]$ (Lemma 0.3 (c)). (5.67)
and (5.69) are the same arguments for $P^*_h = \Box^*_h+iL^*_h$, whose damping acts backwards, as his proof says.

(6.1). Run the proof of (5.66) at fixed $h$ with $a$ multiplied by $H(\tau)$. The boundary $\tau = 0$ then adds to
(5.74) and (5.77) the terms of the boundary $\tau = T_0$ with the opposite sign. Each is a quadratic form in
$(\omega,\partial_\tau\omega)|_{\tau = 0}$ with bounded coefficients in the 3b frame, so it is bounded by
$C\|(\omega,r\mathcal L_{\partial_t}\omega)|_{X_0}\|^2_{\mathcal H_{\mathrm{data}}}$. Here $\partial_\tau = r\partial_t$
at fixed $(r,\omega)$, and the weight matches by Lemma 0.2 (b): $\rho_{\mathrm{sf}}^{\alpha+\frac12}\bar H^k_{\mathrm
b}(X_0,r^3|dr\,d\slashed g|) = \rho_{\mathrm{sf}}^\alpha\bar H^k_{\mathrm b}(X_0,r^4|dr\,d\slashed g|)$. $\square$

## 7. Combination: [Hin26a] Theorem 5.2 at n = 4 ([Hin26a] section 5.2.7)

Fix $(\alpha_{\mathrm{sf}},\alpha_K)$ as in Lemma 0.5 and $b\in U$.

**Proposition 7.1 ([Hin26a] Proposition 5.17 at n = 4).** For $s\ge1$ there are $h_0>0$ and $C$ such that for
$h\in(0,h_0)$ and $\omega\in H^{s+1,(\alpha_{\mathrm{sf}},\alpha_K)}_{3\mathrm b,h}(\Omega)^{\bullet,-}$,
$$\|\omega\|_{H^{s,(\alpha_{\mathrm{sf}},\alpha_K)}_{3\mathrm b,h}(\Omega)^{\bullet,-}}\le
Ch^{-1}\|P_h\omega\|_{H^{s-1,(\alpha_{\mathrm{sf}}+2,\alpha_K)}_{3\mathrm b,h}(\Omega)^{\bullet,-}}.\tag{5.79}$$

*Proof.* Take $s = 1$ first. Every microlocal estimate below bounds $\|B_0\omega\|$ by $h^{-1}\|B_1P_h\omega\|$, an a
priori term $\|E\omega\|$ and $h^N\|\chi\omega\|_{H^{-N}}$. Each step's a priori set lies in the elliptic sets of the
$B_0$'s of earlier steps, so the estimates chain. The $B_0$'s of all the steps together are elliptic on a neighbourhood
of $o$ over $\mathrm{supp}\,\chi_{\tau,2}\chi_{r,2}$. The steps are:

(i) (5.66) on $\tau^{-1}([0,T_0])$.

(ii) Propositions 1.2-1.3 off $o$; the a priori term of (5.21) lies in $\tau^{-1}([0,\frac{2.75}{10}T_0])$, covered by
(i).

(iii) Proposition 5.3 (1) on every $\mathcal D$, with $\kappa = \frac12$ and $T_2$ arbitrary, from (i). This covers $o$
over every compact subset of $\Omega\setminus(K^+\cup\mathrm{sf})$, since $\{t\le T',r\le R'\}\subset\{\phi<T'+R'\}$.

(iv) Proposition 5.2 (c) along $\mathrm{sf}$ from $s\in[5,10]$, where $\tau\le\frac15<T_0$ and (i) applies, to
$s>v(1+\delta_{\mathrm{sf}})$. Its interior a priori set $\{\delta'\le\rho_{\mathrm{sf}}\le2\delta'\}$ is compact in
$\Omega^\circ$ and covered by (iii).

(v) Proposition 2.1 (1) at $r = r_c$; its $E$ lies at finite $t\in[\frac1{3\delta},\frac1\delta]$, covered by (iii).

(vi) Proposition 5.1 (1) towards $r_\sharp$, with $r_1 := r_\sharp+\frac2{10}(\hat r-r_\sharp)$ and $t_1\ge\delta^{-1}$;
its $E$ is near $r_c$, by (v), or at finite times, by (iii).

(vii) Proposition 5.2 (a) (1) outward to $r'_4 := 2\delta_0^{-1}$, with $r'_3 := \delta_0^{-1}$, where $\delta_0$ is
Proposition 3.1's $\delta$; its $E$ is near $r_c$, by (v), or at finite times, by (iii).

(viii) Proposition 3.1 (1) at $\partial K^+$; its $E$ lies at $\rho_{\mathrm{sf}}\in[\frac54\delta_0,2\delta_0]$,
$\rho_K\le2\delta_r$, covered by (vii) where $t$ is large and by (iii) where $t$ is finite.

(ix) Proposition 5.2 (b) (1) along $\mathrm{sf}$ from $s\in[\delta_r,\frac54\delta_r]$, by (viii), to
$s<v(1-\delta_{\mathrm{sf}})$, its interior part by (iii).

(x) Proposition 4.1 (1) at the sink, with its $\delta\le\delta'/2$. Its $E$ lies at $|\frac
sv-1|\in[\frac54\delta_{\mathrm{sf}},2\delta_{\mathrm{sf}}]$, covered by (iv) and (ix), or at
$\rho_{\mathrm{sf}}\ge\frac54\delta$ with $r$ finite, covered by (iii).

Together this is (5.80)'s first form:
$$\|\omega\|_{H^{1,(\alpha_{\mathrm{sf}},\alpha_K)}_{3\mathrm
b,h}(\tau^{-1}([0,T_0]))}+\|\chi_{\tau,2}\chi_{r,2}\omega\|_{H^{1,(\alpha_{\mathrm{sf}},\alpha_K)}_{3\mathrm b,h}}\le
C\big(h^{-1}\|P_h\omega\|_{H^{0,(\alpha_{\mathrm{sf}}+2,\alpha_K)}_{3\mathrm
b,h}(\Omega)^{\bullet,-}}+h^N\|\chi_{\tau,0}\chi_{r,0}\omega\|_{H^{-N,(\alpha_{\mathrm{sf}},\alpha_K)}_{3\mathrm
b,h}}\big).$$
Then (5.68) with $r_1 = r_\sharp$, $r_2 := r_\sharp+\frac{2.75}{10}(\hat r-r_\sharp)$ and $r_3 := \frac12(r_2+\hat r)$
estimates $\omega$ on $r^{-1}([r_\sharp,r_2])$ by the region just controlled. This gives (5.80), and absorbing the $h^N$
term for $h$ small gives (5.79) at $s = 1$.

For $s>1$, the energy estimates are the only step restricted to $s = 1$; the remedy is to extend and restrict, as his
proof does. Extend $f := P_h\omega$ to $\tilde f$ on $\tilde\Omega := \mathrm{cl}\{t\ge0,r\ge\frac34r_\sharp\}$ with the
same quotient norm, and $g$, $c$ as in section 0. The forward solution $\tilde\omega\in
H^{0,(\alpha_{\mathrm{sf}},\alpha_K)}_{3\mathrm b,h}(\tilde\Omega)^{\bullet,-}$ exists with $\|\tilde\omega\|\le
Ch^{-1}\|\tilde f\|_{H^{-1}}$, by Proposition 7.2 at $s' = 1$ on $\tilde\Omega$ and duality. On $\tilde\Omega$ the
argument runs with two changes (amended D311, finding (IV$'''''$6)). Proposition 5.1 is used with $r_1\ge r_\sharp$, and
Proposition 5.3's $\chi_r$ transition is placed in $\{r\ge r_\sharp\}$, where $c$ is 10.14's 1-form and Lemma 0.5 (6)
holds. On $\{\frac34r_\sharp\le r\le r_3\}$, $r_3<\hat r$, the estimates (5.68)-(5.69) of Proposition 6.1 are used, with
$\frac34r_\sharp$ for $r_\sharp$; they need only Lemma 0.3 (c) and Lemma 0.4, which hold for every stationary past
timelike extension of $c$, Lemma 0.3 holding on $\{r\ge\frac12r_\sharp\}$. Proposition 1.3 needs only Lemma 0.3 (c)
there. Moreover $\tilde\omega = \omega$ on $\Omega$, by uniqueness of forward solutions: $\Sigma^\sharp$ is spacelike
with future timelike vectors pointing out, and $X_0$ is spacelike (Lemma 0.3 (a), (c)). The microlocal estimates of
sections 1-5 hold for every $s$ in the strong sense; near the zero section the order is irrelevant. They apply to
$\tilde\omega$ on $\{r\ge\frac78r_\sharp\}$, where $\Sigma^\sharp$ is now interior. Near $\tau = 0$ they propagate from
$\tau<0$, where $\tilde\omega = 0$, by Proposition 5.3 (1) and Proposition 1.3 with the cut-offs moved below $\tau = 0$.
Restriction to $\Omega$ gives (5.79) for $s\ge1$. $\square$

**Proposition 7.2 (the adjoint estimate (5.81) at n = 4).** For $s'\ge1$ there are $h_0>0$ and $C$ such that for
$h\in(0,h_0)$,
$$\|\omega'\|_{H^{s',(-\alpha_{\mathrm{sf}}-2,-\alpha_K)}_{3\mathrm b,h}(\Omega)^{-,\bullet}}\le
Ch^{-1}\|P^*_h\omega'\|_{H^{s'-1,(-\alpha_{\mathrm{sf}},-\alpha_K)}_{3\mathrm b,h}(\Omega)^{-,\bullet}}.\tag{5.81}$$

*Proof.* At $s' = 1$ the estimates chain as follows, each later a priori set covered by earlier steps.

(i) Proposition 4.1 (2) at the sink, free.

(ii) Proposition 5.2 (b) (2) and (c) (2) along $\mathrm{sf}$ outward from the sink, to
$s\in[\delta_r,v(1-\delta_{\mathrm{sf}})]$ and $[v(1+\delta_{\mathrm{sf}}),10]$. Their a priori sets are at the sink, by
(i), and their sf-cut-off terms have the good sign.

(iii) Proposition 3.1 (2) at $\partial K^+$; its $E$ at $\rho_K\in[\frac54\delta_r,2\delta_r]$ is covered by (ii).

(iv) Proposition 5.2 (a) (2) along $K^+$ inward from $r'_4 := 2\delta_0^{-1}$ to $r'_1$, with $r'_3 := \delta_0^{-1}$
and $\delta_0$ Proposition 3.1's $\delta$; its $E$ at $[r'_3,r'_4]$, where $\rho_{\mathrm{sf}}\le\delta_0$, is covered
by (iii).

(v) (5.69) near $\Sigma^\sharp$, free on supported spaces.

(vi) Proposition 5.1 (2) from $\Sigma^\sharp$ towards $r_c$; its $E$ near $r_\sharp$ is covered by (v).

(vii) Proposition 2.1 (2) at $r_c$; its $E$ at $|r-r_c|\in[\frac{55}{50},\frac{60}{50}]r_c\sqrt e/v$ is covered by (iv)
and (vi).

At this point a neighbourhood of $o$ over
$\{\rho_K\le\epsilon_1\}\cup(\{\rho_{\mathrm{sf}}\le\epsilon_1\}\cap\{s\le10\})\cup\{r\le r_\sharp+\epsilon_r\}$ is
controlled, for some $\epsilon_1>0$. Here $\rho_K = r/(t+r)$ globally.

(viii) Proposition 5.3 (2) with $\kappa = \frac19$, $t_1<\frac14T_0r_\sharp$ and $t_2\ge\max(\epsilon_1^{-2},10c_1)$.
Its late set $\{t_2\le t\le t_2+1\}\cap\mathcal D'$ is covered by (i)-(vii). Points there with $r\le\epsilon_1^{-1}$
have $\rho_K\le\epsilon_1$; the others have $\rho_{\mathrm{sf}}\le\epsilon_1$ and $s = r/t\le(t+c_1)/(\kappa t)\le10$
once $t_2\ge10c_1$. Its set near $\Sigma^\sharp$ is covered by (v). It controls $o$ over $\{t\ge2t_1,t\ge\kappa r\}$ up
to $t_2$, which covers $\{\tau\ge\kappa\}$ there; and $\kappa = \frac19<\frac14 = \frac12T_0$. A point with
$\tau\ge\frac12T_0$ has $t\ge\frac12T_0r_\sharp>2t_1$.

(ix) Propositions 1.2-1.3 (the adjoint (5.22)) off $o$; the a priori term is near $\Sigma^\sharp$, by (v).

(x) (5.67) on $\tau^{-1}([0,\frac12T_0])$, from $\tau^{-1}([\frac12T_0,T_0])$, which is covered by (ii) near
$\mathrm{sf}$, by (viii) elsewhere, and by (ix) off $o$.

Absorbing $h^N$ gives (5.81) at $s' = 1$. For $s'>1$, extend and restrict as in Proposition 7.1.

The parameters of
Propositions 7.1-7.2 are ordered so that each a priori set lies where an earlier step applies (verifier 134's A-n1). In
Proposition 7.1 (ix), $2\delta'\le\delta_0$, so that the start set of Proposition 5.2 (b) (1) lies in Proposition 3.1's
$B_0$. In (ii) above, $2\delta'$ is at most the sink's $\delta$ and $s_3\ge v(1-\frac54\delta_{\mathrm{sf}})$. In (iv)
above, $t_1\ge2/(\delta_0\delta_r)$, so that $[r'_3,r'_4]$ at $\rho_K = 1/t\le t_1^{-1}$ lies in
$\{r/t\le\frac54\delta_r\}$. $\square$

**Theorem 7.3 ([Hin26a] Theorem 5.2 at n = 4).** Let $(\alpha_{\mathrm{sf}},\alpha_K)$ be as in Lemma 0.5 and $C_1>0$.
There is $h_0>0$, uniform for $b\in U$ (Lemma 8.1), such that for $h\in(0,h_0)$, $s\in[-C_1,C_1]$ and $b\in U$:

(a) the forward problem $\Box^C_b\omega = f\in H^{s-1,(\alpha_{\mathrm{sf}}+2,\alpha_K)}_{3\mathrm
b}(\Omega)^{\bullet,-}$ has a unique solution $\omega\in H^{s,(\alpha_{\mathrm{sf}},\alpha_K)}_{3\mathrm
b}(\Omega)^{\bullet,-}$, with the semiclassical bound (5.18), $\|\omega\|_{H^s_{3\mathrm b,h}}\le
Ch^{-1}\|h^2f\|_{H^{s-1}_{3\mathrm b,h}}$ in these weights;

(b) the initial value problem
$$\Box^C_b\omega = f\in\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}+2}\rho_K^{\alpha_K}\bar H^0_{3\mathrm
b}(\Omega,|dg|),\qquad(\omega,r\mathcal
L_{\partial_t}\omega)|_{X_0}\in\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}+\frac12}\bar H^1_{\mathrm
b}(X_0,r^3|dr\,d\slashed g|)\oplus\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}+\frac12}\bar H^0_{\mathrm
b}(X_0,r^3|dr\,d\slashed g|)\tag{5.16}$$
has a unique solution $\omega\in\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}\rho_K^{\alpha_K}\bar H^1_{3\mathrm
b}(\Omega,|dg|)$, the densities on $X_0$ being Euclidean (his footnote 15);

(c) (5.79) and (5.81) hold for $s,s'\in[1,C_1+1]$ and $h\in(0,h_0)$, with constants uniform for $b\in U$ ($h_0$ depends
on $C_1$; verifier 134's A-n2).

*Proof.* (c) is Propositions 7.1-7.2 with Lemma 8.1.

(a) *Existence for $s\le0$.* Take $s' := 1-s\ge1$. For $\omega'$ in
$H^{s',(-\alpha_{\mathrm{sf}}-2,-\alpha_K)}_{3\mathrm b,h}(\Omega)^{-,\bullet}$, the functional
$P^*_h\omega'\mapsto\langle h^2f,\omega'\rangle$ is well defined and bounded by $Ch^{-1}\|h^2f\|\,\|P^*_h\omega'\|$, by
(5.81). The spaces $H^{s-1,(\alpha_{\mathrm{sf}}+2,\alpha_K)}(\Omega)^{\bullet,-}$ and
$H^{1-s,(-\alpha_{\mathrm{sf}}-2,-\alpha_K)}(\Omega)^{-,\bullet}$ are dual under $\langle\cdot,\cdot\rangle$, and so are
$H^{s,(\alpha_{\mathrm{sf}},\alpha_K)}(\Omega)^{\bullet,-}$ and
$H^{-s,(-\alpha_{\mathrm{sf}},-\alpha_K)}(\Omega)^{-,\bullet}$ (his section 2.3). So Hahn-Banach gives $\omega\in
H^{s,(\alpha_{\mathrm{sf}},\alpha_K)}_{3\mathrm b,h}(\Omega)^{\bullet,-}$ with $P_h\omega = h^2f$ and the bound (5.18).

*$s>0$.* Higher regularity follows by extension and restriction with the propagation estimates, as in Proposition 7.1.

*Uniqueness*, for every distribution $\omega$ on $\Omega$ supported in $\{t\ge0\}$ with $P_h\omega = 0$, by the
classical duality argument. For $\varphi\in C^\infty_c(\Omega^\circ)$, the backward solution $\psi$ of $P^*_h\psi =
\varphi$ is smooth, with support in the causal past of $\mathrm{supp}\,\varphi$. That set is compact, since $t$
decreases and $|dr/dt|$ is bounded along causal curves. It is disjoint from $\Sigma^\sharp$: along past-directed causal
curves $r$ increases inside $\{r\le\hat r\}$ (Lemma 0.3 (c)), so $r$ stays above
$\min(\min_{\mathrm{supp}\,\varphi}r,\hat r)$. Pairing the extension of $\omega$ by zero across $X_0$ with $\psi$ gives
$\langle\omega,\varphi\rangle = \langle P_h\omega,\psi\rangle = 0$.

(b) First, by Lemma 0.2 (b) the data space is $\mathcal H_{\mathrm{data}}$ of (6.1), with the density $r^4|dr\,d\slashed
g|$ that tensors with $d\tau$ to $|dg|$. This is the $n = 4$ form of his remark on p. 65; the shift $\frac12$ does not
depend on $n$.

*Smooth data.* Take $f$ and data smooth with compact support in $\Omega^\circ\cup X_0^\circ$. The initial value problem
then has a solution $\omega$ smooth on $\Omega\setminus(K^+\cup\mathrm{sf})$, for the following reasons. $\Box^C_b$ has
scalar principal symbol $G\,\mathrm{Id}$ (Lemma 0.2 (d)). Every past-inextendible causal curve in $\Omega^\circ$ meets
$X_0$: $t$ decreases along it (Lemma 0.3 (a)), $r$ increases along it inside $\{r\le\hat r\}$ (Lemma 0.3 (c)), and
$|dr/dt|$ is bounded along causal curves, since $g$ is a 3sc-metric. So the classical theory of the Cauchy problem for
linear wave equations with scalar principal symbol applies; his p. 42 calls this automatic. By finite speed of
propagation, $\omega$ vanishes on $\tau^{-1}([0,T_0])$ near $\mathrm{sf}$, the speed being $1+O(r^{-2})$ and $T_0<1$; so
$\omega\in\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}\bar H^2_{3\mathrm b}(\tau^{-1}([0,T_0]))$ and (6.1) applies. Let
$\chi = \chi(\tau)$ equal 1 for $\tau\ge\frac12T_0$ and 0 for $\tau\le\frac14T_0$. Then $P_h(\chi\omega) = h^2\chi
f+[P_h,\chi]\omega\in H^{0,(\alpha_{\mathrm{sf}}+2,\alpha_K)}(\Omega)^{\bullet,-}$, with norm bounded by $\|f\|$ and by
$\|\omega\|_{\rho^{\alpha_{\mathrm{sf}}}\bar H^1(\tau^{-1}([0,T_0]))}$. By the uniqueness in (a), which holds for
distributions, $\chi\omega$ is the forward solution, so it lies in $H^{1,(\alpha_{\mathrm{sf}},\alpha_K)}$. Using (6.1),
$$\|\omega\|_{\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}\rho_K^{\alpha_K}\bar H^1_{3\mathrm b}(\Omega)}\le
C\big(\|f\|+\|(\omega,r\mathcal L_{\partial_t}\omega)|_{X_0}\|_{\mathcal H_{\mathrm{data}}}\big).$$

*General data.* Approximate $f$ and the data in their spaces by such smooth data. By this estimate the solutions
converge in $\rho^{\alpha_{\mathrm{sf}}}_{\mathrm{sf}}\rho^{\alpha_K}_K\bar H^1_{3\mathrm b}(\Omega)$. Near $X_0$ they
also converge in $C([0,T_0]_\tau;\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}\bar H^1_{\mathrm b})\cap
C^1([0,T_0]_\tau;\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}\bar H^0_{\mathrm b})$: the boundary term at $\tau = T$ of
(5.74) and (5.77), run at every $T\in[0,T_0]$ in the proof of (6.1), bounds the norm of
$(\omega,\partial_\tau\omega)|_{\tau = T}$ by the right side of (6.1). So the limit takes the data and solves (5.16).
For uniqueness, let $\omega\in\rho^{\alpha_{\mathrm{sf}}}_{\mathrm{sf}}\rho^{\alpha_K}_K\bar H^1_{3\mathrm b}(\Omega)$
solve (5.16) with $f = 0$ and vanishing data. Its extension by zero across $X_0$ is a distribution supported in
$\{t\ge0\}$ with $P_h\omega = 0$, the vanishing data leaving no layer on $X_0$; so $\omega = 0$ by the uniqueness in (a)
(amended D311, finding (IV$'''''$7)). $\square$

**Remark 7.4 (in III.B's coordinates).** III.B's $g_b = \Phi_\mu^*g$, with $\Phi_\mu(t,x) = (t-T_\mu(|x|),x)$ and
$T_\mu\in|x|^{-1}C^\infty(\bar X)$ near infinity (III.B Lemma 3.5 (a)). $\Phi_\mu$ commutes with $\partial_t$ and acts
on 1-forms by $dt\mapsto dt-T'_\mu\,dr$, where $T'_\mu\in|x|^{-2}C^\infty$. Hence $\Phi_\mu$ intertwines $\Box^C$ for
$(g,c_C)$ with $\Box^C$ for $(g_b,\Phi_\mu^*c_C)$, and it preserves stationarity, $\mathcal A^\gamma(\bar X;E)$, the
weighted b-spaces on $\bar X$, and integrals over $[0,\infty)_t\times A$ for an annulus $A$, up to the shift by the
bounded $T_\mu$. Part IV$''''$ Theorem 2.1 uses Theorem 7.3 through this intertwining, with its initial data at
$\{t_{\mathrm{KS}} = 0\}$ (Part IV$''''$, amended D308).

## 8. Uniformity in b

**Lemma 8.1.** The constants $C$ and the thresholds $h_0$ in Propositions 1.2-7.2 and Theorem 7.3 can be taken uniform
for $b\in U$.

*Proof.* Every estimate above is proved from three kinds of input, each uniform on $U$:

- finitely many seminorms of the coefficients of $P_h$ as an element of
$h^2\rho_{\mathrm{sf}}^2\mathrm{Diff}^2_{3\mathrm b}+h\rho_{\mathrm{sf}}^2\mathrm{Diff}^1_{3\mathrm b}$ in the frames
$r\partial_{z^\mu}$, which are continuous in $b$ (Lemma 0.2 (a), (d); III.B's smooth dependence);

- the lower bounds in the positivity statements: Lemma 0.3 (exact in (a)-(b) for all $b\in\mathcal B$, by continuity in
(c)), Lemma 0.4 (the constant $C$ and the margin of his Lemma 3.5 on compact sets) and Lemma 0.5 (uniform by its
statement);

- the cut-offs, commutants and the parameters $\mathfrak X$, $\delta$, $\delta'$, $t_j$, $r_j$, $\kappa$, chosen from
these bounds alone, hence independently of $b$.

The calculus estimates used (composition, elliptic parametrices, the sharp Gårding inequality, $L^2$-boundedness) have
constants depending on finitely many seminorms of the symbols involved, which depend continuously on $b$. Each
absorption step needs $h$ below a threshold determined by these quantities. So each $h_0$ and $C$ is uniform on $U$,
after shrinking $U$ to a compact neighbourhood. $\square$

## 9. Findings, labels and sources

(IV$'''''$1) *The time function.* The source's time function is of Kerr-star type, with $dt$ timelike everywhere. At $n
= 4$ the Kerr-Schild time of III.B (3.2) serves. In it, 10.14's $c$ and 10.22's computations are made, and III.B Lemma
3.3 (e) makes $d(t-\beta r)$ timelike for every $\beta\in(-1,1]$ and every $b\in\mathcal B$, which gives Lemma 0.3
(a)-(b) exactly. III.B's own $t = t_{\mathrm{KS}}+T_\mu$ is not used. Part IV$''''$ Theorem 2.1's initial data are
accordingly taken at $\{t_{\mathrm{KS}} = 0\}$ (amended D308).

(IV$'''''$2) *Estimates the source leaves unstated.* The proof of his Proposition 5.17 propagates "inside of
$\Omega^\circ$" and along $\mathrm{sf}$, and the adjoint chain reaches "towards $\tau = 0$". Propositions 5.2-5.3 state
and prove these estimates, in both directions:

- the interior with the escape functions $t+\kappa r$ and $t$, and the cut-off $t-\kappa r$, $\kappa = \frac19$;

- along $\mathrm{sf}$ with $\pm r/t$;

- along $K^+$ outward with $r$.

The chains of Propositions 7.1-7.2 list each step's a priori set and the step that covers it. The propagation along
$\mathrm{sf}$ from the energy region needs the two to meet. With his $T$ "sufficiently small" and his Proposition 5.1
(6) stated only up to $r/t = 10$, they meet when $T\ge\frac1{10}$. At $n = 4$, $T_0 = \frac12$ by Lemma 0.3 (b).

(IV$'''''$3) *Part IV$''''$ Lemma 1.4's reading of (4)-(5).* Its sentence "$T$ is positive definite on all of
$\mathrm{sf}$ with $\rho_K\le10$ for every $C_0\in[0,100]$" overstates 10.22 Proposition 10.19 (iv). That proposition
gives two things: for every $C_0\ge0$, the positivity at $\partial K^+$ and at the sink $R_v$; and, at $C_0 = 100$, $T$
on all of $\mathrm{sf}$ with $\rho_K\le10$. His Proposition 5.1 (4)-(5) need only the first. (4) holds near $\partial
K^+$ by continuity, and (5) holds on $|\frac{r/t}v-1|\le2\delta_{\mathrm{sf}}$ because $T'$ at the sink does not depend
on $\rho_K$ (10.22 (c)). Part IV$''''$ Lemma 1.4 is amended to say so (D308). No conclusion changes.

(IV$'''''$4) *Uniformity in $b$.* The source fixes one Kerr metric. III.K's iteration varies $b$, and Part IV$''''$'s
set $\mathsf H$ is defined through $h_0$, so $h_0$ must be uniform; Lemma 8.1 gives this.

(IV$'''''$5) *The inner radius.* $r_\sharp = \frac12R_1$ is III.B's $r_0$ and 10.14's $m$. $\hat r = \frac34R_1$
replaces the source's $r_+$ in the cut-offs and the energy estimates near $\Sigma^\sharp$, since only the future
timelike character of $dr$ on $[r_\sharp,\hat r]$ is used (Lemma 0.3 (c)). The horizon of $g_b$ is not
located.

(IV$'''''$6) *The extended domain* (verifier 134's A-m1). The extension to $\tilde\Omega$ in Proposition
7.1's proof read that the whole argument runs there with $\frac34r_\sharp$ for $r_\sharp$. Proposition 5.1 and the
dropped $\chi_r$ term of Proposition 5.3 (1) use Lemma 0.5 (6), which is not known for the extension of $c$ below
$r_\sharp$. They are kept in $\{r\ge r_\sharp\}$, and $[\frac34r_\sharp,r_3]$ is covered by (5.68)-(5.69), which use
only Lemma 0.3 (c) and Lemma 0.4.

(IV$'''''$7) *General data* (verifier 134's A-m2). The passage to general data in
Theorem 7.3 (b) read the traces as continuous on $\bar H^1$ and uniqueness as the estimate itself. The trace of
$r\mathcal L_{\partial_t}\omega$ is not continuous on $\bar H^1$, and the estimate was proved for smooth solutions.
Repaired by the energy identity's boundary term at every $\tau\in[0,T_0]$, and by uniqueness from (a) for the extension
by zero.

*Labels.* The labels map to the source as follows:

| Here | [Hin26a] |
|---|---|
| Definition 0.1 | Definitions 2.1, 2.2, 2.5, (5.19) |
| Lemma 0.2 | Lemmas 2.3, 2.4, (2.12)-(2.14), Lemma 5.3 |
| Lemma 0.4 | Lemmas 3.3-3.9, Corollary 3.6 |
| Lemma 0.5 | Proposition 5.1 |
| Lemma 1.1 | Lemma 5.4 |
| Propositions 1.2, 1.3 | Propositions 5.5, 5.6 |
| Proposition 2.1 | Proposition 5.8 |
| Proposition 3.1 | Proposition 5.9 |
| Proposition 4.1 | Proposition 5.11 |
| Proposition 5.1 | Proposition 5.12 |
| Propositions 5.2, 5.3 | his pp. 57-58 and 64, stated here |
| Proposition 6.1 | Proposition 5.16 |
| Proposition 7.1 | Proposition 5.17 |
| Proposition 7.2 | (5.81) |
| Theorem 7.3 | Theorem 5.2 |

*Sources.* [Hin26a] pp. 12-17 (Definition 2.1, its charts, (2.2)-(2.14), Lemmas 2.3-2.4, Definition 2.5, Remark 2.6),
25-28 (Definition 3.1, Lemmas 3.2-3.9, Corollary 3.6), 37-39 (Proposition 5.1), 41-66 (Theorem 5.2, footnote 15, Lemma
5.3 to the end of section 5.2.7), read at source. Inputs:

- III.B section 3.1, (3.2)-(3.3), Lemmas 3.3, 3.5, Proposition 3.6;

- Part IV$''''$ section 0, Lemmas 1.1, 1.4, (0.1), (2.1);

- record 10.13 (i), 10.14, 10.22 (Proposition 10.19 (i)-(iv), (a)-(d)), 10.65 (a).
