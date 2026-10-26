# Part III.D′. The gauge potential operator at zero energy, at n = 4 ([Hin26] section 6.4)

*Status.* Written (D222). This part proves, at spatial dimension $n = 4$ and for the Myers-Perry metrics $g_b$ of Part
III.B with $b$ near the Tangherlini parameter $b_0$, what [Hin26] section 6.4 and Lemma 6.13 establish (pp. 119-125):
the kernel and cokernel of the unmodified 1-form wave operator at zero energy (his Lemma 6.10, which he takes from
[AHW24] Theorem 5.1 (2)), the two pairings at the horizon (Lemma 6.11), mode stability of the gauge potential wave
operator at every frequency of the closed upper half plane (Proposition 6.12), and the invertibility of its zero energy
operator with polyhomogeneous inverse images (Lemma 6.13). Part III.D is cited as III.D, Parts I.A-I.C as I.A-I.C, Part
III.A as III.A, Part III.A$'$ as III.A$'$, Part III.B as III.B. Computations cited as *computed* are exact (sympy) and
rerun by the instruments named (D222).

*How it differs from the source.* Lemma 6.10 is proved here on five-dimensional Tangherlini, the kernel by energy
identities for the mode equations and the cokernel by a distributional identity at the horizon, with the index from I.C.
Step 1 of Proposition 6.12 is done by a Grushin problem with a fixed compactly supported augmentation, to which I.C
Theorems 6.4 and 7.1 apply as proved; its Schur complement is computed from the two pairings alone, so the source's
augmented estimate (6.27) with a joint parameter, and the decay of $\partial_\sigma\widehat\Box(0)\omega_{(0)}$ that
makes it work (his footnote 69), are not needed. Step 2 is done at every frequency at once around a base point at which
invertibility is already known, which closes a step the source asserts (finding (D$'$4)). Findings are in section 6.

## 1. Setting

$\mathcal B$, $g_b$, $t_*$, $\rho$, $E_\Upsilon =
(c_\Upsilon,e_\Upsilon,\gamma_\Upsilon;c_{\Upsilon,H},\gamma_{\Upsilon,H})$ and $\Box^\Upsilon_b$ are as in III.D
section 1, with $c_{\Upsilon,H} := -\frac12\chi(r)\,dr$ as in III.D section 5.1 ($\chi\in C_c^\infty$, $\chi = 1$ near
$r_h$, $\mathrm{supp}\,\chi\cap U_\Gamma = \emptyset$) and $c_\Upsilon$ as in III.D section 1. Write $\mathsf p :=
(b,e_\Upsilon,\gamma_\Upsilon,\gamma_{\Upsilon,H})$, $\hat P_{\mathsf p}(\sigma) := \widehat{\Box^\Upsilon_b}(\sigma)$,
$\mathsf p_0 := (b_0,0,0,0)$ and $\hat P := \hat P_{\mathsf p_0}$, the spectral family of the 1-form wave operator $\Box
:= \Box_{g_{b_0}} = d\delta+\delta d$ (III.D (1.1)). On $g_{b_0}$, $f = 1-\mu_0/r^2$, $r_h = \mu_0^{1/2}$, $v = t+r_*$
is the ingoing time and $t_*-v$ is a smooth function of $r$ near $r_h$ (III.B (3.6)); in the ingoing chart
$(v,r,\omega)$, $g = -f\,dv^2+2\,dv\,dr+r^2\slashed g$, so $g^{vv} = 0$, $g^{vr} = 1$, $g^{rr} = f$, and $|dg| =
r^3|dv\,dr\,d\omega|$.

*The spaces.* For $\sigma\ne0$, $\mathrm{Im}\,\sigma\ge0$: $\mathcal X_\sigma$, $\mathcal Y_\sigma$ of I.C (6.4) (those
of I.A Theorem 7.2 with the orders of I.B Theorem 1.3 (3)); at $\sigma = 0$: $\mathcal X_0$, $\mathcal Y_0$ of I.C
(3.1), with the Euclidean density, so that the b-weight of $\bar H^{s,\alpha}_{\mathrm b}$ is $\alpha+2$ (I.C Remark (a)
after section 1.2). By III.D sections 2-5 and 7 and (Dyn), every $\hat P_{\mathsf p}$, $\mathsf p$ in a compact
neighbourhood $\mathcal K$ of $\mathsf p_0$ with $e_\Upsilon\ge0$, satisfies (H1)-(H5) with $\vartheta_{\mathcal H} = 1$
(III.D Lemma 5.1), (G) for every $\alpha$ with $\alpha+2\in(0,2)$ (III.D Lemma 4.1: $(0,2)$ lies in the gap
$(0,\lambda^\Upsilon_{\mathrm s1,2})$, which is $(0,2)$ when $e_\Upsilon\gamma_\Upsilon^2 = 0$), (TF) (III.D Lemma 7.1),
and has index 0 at $\sigma\ne0$ (I.B Theorem 1.3 (3), as in III.D Proposition 6.1). We fix such an $\alpha$ and a
constant $s>\frac52$; by I.C Theorem 3.1 (3)-(4) and I.A Theorem 7.2 (3), kernels, annihilators of ranges and
invertibility do not depend on these choices.

*The horizon functional.* Let $\omega^* := d\big(H(r-r_h)\big) = \delta(r-r_h)\,dr$, $H$ the Heaviside function, a
stationary distributional 1-form supported on the horizon sphere, and

$$\ell(v) := \int_Xg^{-1}(v,\omega^*)\,|dg_X| = r_h^3\int_{\mathbb S^3}v(\partial_{t_*})\big|_{r = r_h}\,
d\omega,\tag{1.1}$$

where $|dg| = |dt_*|\otimes|dg_X|$, so $|dg_X| = r^3|dr\,d\omega|$ near $r_h$, and $g^{-1}(v,dr) = v(\nabla r) =
v(\partial_v+f\partial_r)$ equals $v(\partial_{t_*})$ at $r_h$. $\ell$ is continuous on $H^{s'}$ near the horizon sphere
for $s'>\frac12$ (the trace theorem), so on $\mathcal Y_0$ and $\mathcal Y_\sigma$ as $s-1>\frac12$; it is the source's
pairing with $\omega^*_{(0)}$.

*The modified divergence at the horizon.* With the trace weight $\frac23$ of III.B Definition 6.1, $E_{H}h :=
2\iota_{c_{\Upsilon,H}^\sharp}h-\frac23c_{\Upsilon,H}\,\mathrm{tr}_gh$ (the source's $E^\Upsilon_{g_b,H^+,1}$, (6.22)),
and since $\mathrm{tr}_gG_gh = -\frac32\mathrm{tr}_gh$ at $D = 5$,

$$E_HG_g = 2\iota_{c^\sharp_{\Upsilon,H}},\tag{1.2}$$

as $E_{H^+,1}G = 2\iota_{c^\sharp}$ at $D = 4$ with the weight 1 (III.D (D2)). The horizon part of $\Box^\Upsilon_b$ is
$2\gamma_{\Upsilon,H}E_HG\delta^*$.

## 2. Kernel and cokernel at zero energy ([Hin26] Lemma 6.10 at n = 4)

Let

$$W^* := r^{-2}\,dt+r_hr^{-3}f^{-1}\,dr = r^{-2}\,dv-\frac{dr}{r(r+r_h)}.\tag{2.1}$$

The second form shows that $W^*$ is smooth on $\{r>0\}$ in the ingoing chart, so on $\bar X$ up to $\partial_\sharp X$;
near infinity $dt = dt_*+(f^{-1}+O(r^{-2}))\,dr$ with all derivatives (III.B (3.6)), so $W^*\in\mathcal A^2(\bar X;E)$,
and $W^*\in\bar H^{s,\alpha}_{\mathrm b}$ for $\alpha+2<2$. $dW^* = 2r^{-3}\,dt\wedge dr$, and $\delta W^* = 0$:
$\delta(a(r)\,dt) = 0$ for the static metric, and $\delta(b(r)\,dr) = -r^{-3}(r^3fb)'$ vanishes for $b =
r_hr^{-3}f^{-1}$. $\delta dW^* = 0$ because $r^3F^{rt}$ is constant for $F = 2r^{-3}dt\wedge dr$ ($F^{rt} =
g^{rr}g^{tt}F_{rt}$, $g^{rr}g^{tt} = -1$). So $\Box W^* = 0$ on $\{r>r_h\}$, and on $\{r>0\}$ since the components of
$\Box W^*$ in the ingoing chart are real-analytic in $r$. (*Computed:* `gaugepot5.py` G4, which also finds $W^*$ as the
only $l = 0$ kernel element smooth at the future horizon and decaying.)

**Lemma 2.1.** Assume (Dyn) at $b_0$. (1) For every stationary $u\in C^\infty(\bar X;E)$ (indeed every $u$ smooth near
the horizon sphere), $\ell(\hat P(0)u) = 0$. (2) $\ker_{\mathcal X_0}\hat P(0) = \mathrm{span}\{W^*\}$. (3) The
annihilator of the range of $\hat P(0):\mathcal X_0\to\mathcal Y_0$ is spanned by $\ell$.

*Proof.* (1) *Symmetry.* For stationary smooth 1-forms $u$, $w$ with $w$ compactly supported in $X^\circ$, $B(u,w) :=
\int_Xg^{-1}(u,\bar w)|dg_X|$ satisfies $B(\Box u,w) = B(u,\Box w)$. Indeed, let $\theta\in C_c^\infty(\mathbb R)$ with
$\int\theta = 1$ and $W := \theta(t_*)w$. As $\Box = -\nabla^\mu\nabla_\mu$, two integrations by parts against the
compactly supported $W$ give $\int g^{-1}(\Box u,\bar W)|dg| = \int g^{-1}(u,\Box\bar W)|dg|$. The left side is $B(\Box
u,w)$. On the right, $\Box(\theta w) = \theta\Box w+(\Box_0\theta)w-2\nabla_{\nabla\theta}w$ with $\Box_0 =
-\nabla^\mu\nabla_\mu$ on functions, and $\nabla\theta = \theta'\nabla t_*$, $\Box_0\theta =
-\theta''g^{-1}(dt_*,dt_*)+\theta'\Box_0t_*$; the coefficients of $\theta'$ and $\theta''$ are stationary, and
$\int\theta' = \int\theta'' = 0$, so the right side is $B(u,\Box w)$. By continuity the identity extends to $w$ a
stationary distribution with compact support in $X^\circ$ ($u$ smooth). *The identity.* Since $\Box = d\delta+\delta d$
and $\delta^2 = 0$, $\Box d = d\delta d = d\Box_0$ on functions, as operators on distributions. In the ingoing chart,
$H(r-r_h)$ is a $v$-independent distribution, and

$$\Box_0H(r-r_h) = -r^{-3}\partial_\mu\big(r^3g^{\mu r}\delta(r-r_h)\big)
= -r^{-3}\partial_r\big(r^3f\,\delta(r-r_h)\big) = 0,$$

as $\partial_v$ annihilates it, $g^{Ar} = 0$, and $r^3f\,\delta(r-r_h) = r_h^3f(r_h)\delta(r-r_h) = 0$. So $\Box\omega^*
= d\Box_0H(r-r_h) = 0$, and $\ell(\Box u) = B(\Box u,\omega^*) = B(u,\Box\omega^*) = 0$; on stationary $u$, $\Box u =
\hat P(0)u$. Only $u$ near the horizon sphere enters. (*Computed:* `gaugepot5.py` G5 checks $\ell\circ\hat P(0) = 0$
type by type.)

(2) $W^*\in\mathcal X_0$ and $\hat P(0)W^* = 0$, by the above. Conversely let $u\in\mathcal X_0$, $\hat P(0)u = 0$. By
I.C Theorem 3.1 (2), with the gap $(0,2)$, $u$ is smooth up to $\partial_\sharp X$, hence across the horizon, and
$u\in\mathcal A^\beta$ near $\partial X$ for every $\beta<2$; fix $\beta\in(1,2)$. Let $\omega := u$, a stationary
1-form, and work first on $\{r>r_h\}$ in the static chart, expanding in harmonics on $\mathbb S^3$ (III.A$'$ Lemma 1.6;
the projections act in the angles and preserve smoothness at $r_h$ in the ingoing chart and the conormal bounds at
infinity). Three facts are used. The *scalar identity*: for a stationary function $\phi$, $\delta d\phi =
-r^{-3}(r^3f\phi')'+r^{-2}\slashed\Delta\phi$, from $|g|^{1/2} = r^3|\slashed g|^{1/2}$, $g^{rr} = f$ and $g^{AB} =
r^{-2}\slashed g^{AB}$; so a degree-$l$ component $\phi_l$ of a solution of $\delta d\phi = 0$ solves $(r^3f\phi_l')' =
\kappa r\phi_l$, $\kappa = l(l+2)$. The *energy fact*: if $-\Phi_{**}+V\Phi = 0$ on $(r_h,\infty)$, $\Phi_* = f\Phi'$,
with $V>0$ continuous, $\Phi$ of class $C^1$ in $r$ up to $r_h$, and $\Phi_*\bar\Phi\to0$ as $r\to\infty$, then $\Phi =
0$: integrating $\bar\Phi$ times the equation over $r_*\in[r_*(r_1),r_*(R)]$ gives $\int(|\Phi_*|^2+V|\Phi|^2)\,dr_* =
[\Phi_*\bar\Phi]$, whose endpoint terms tend to 0 as $r_1\to r_h$ ($\Phi_* = f\Phi'\to0$) and $R\to\infty$. The *mode
equations* (M3)-(M4) of III.D section 6, which hold for every $\sigma$ (computed, `modes5.py` M3-M4) and are used at
$\sigma = 0$.

*(a) The divergence.* $\phi := \delta\omega$ is a smooth stationary function in $\mathcal A^{\beta+1}$ near infinity,
and $\delta d\phi = \delta(\Box\omega-\delta d\omega) = 0$. Multiplying $(r^3f\phi_l')' = \kappa r\phi_l$ by
$\bar\phi_l$ and integrating over $[r_1,R]$: $[r^3f\phi_l'\bar\phi_l]_{r_1}^R = \int_{r_1}^R(r^3f|\phi_l'|^2+\kappa
r|\phi_l|^2)\,dr$. As $r_1\to r_h$ the bracket tends to 0 ($f\to0$, $\phi_l$ smooth in $r$ there); as $R\to\infty$ it is
$O(R^{3-(\beta+2)-(\beta+1)}) = O(R^{-2\beta})$. So $\phi_l' = 0$ and $\kappa\phi_l = 0$; at $l = 0$, $\phi_0$ is a
decaying constant. So $\delta\omega = 0$.

*(b) The field.* $F := d\omega\in\mathcal A^{\beta+1}$ and $\delta F = \Box\omega-d\delta\omega = 0$. *Vector type.* A
component $r^{-1/2}\Phi(r)Y$ of $\omega$, $Y\in\mathcal V_l$, $l\ge1$, has $\slashed\delta\slashed dY = \lambda Y$ with
$\lambda = (l+1)^2\ge4$ (III.D section 6 (b)); by (M3) at $\sigma = 0$, $-\Phi_{**}+V_1\Phi = 0$ with $V_1 = \frac
f{r^2}(\lambda-\frac14+\frac{5\mu_0}{4r^2})>0$. $\Phi$ is smooth in $r$ at $r_h$ (angular components are the same in the
static and the ingoing chart), and since $|Y|$ is $r^{-1}$ in the Euclidean metric, $\Phi = O(r^{3/2-\beta})$, $\Phi_* =
O(r^{1/2-\beta})$, so $\Phi_*\bar\Phi = O(r^{2-2\beta})\to0$. The energy fact gives $\Phi = 0$. *Scalar type, $l\ge1$.*
In the notation of (M4), $W := r^3F_{tr}$ solves $R[W] = (r^2M_t)' = 0$ ($M = \delta d\omega = 0$), so $\Phi :=
r^{-1/2}W$ solves $-\Phi_{**}+V_2\Phi = 0$ with $V_2 = \frac f{r^2}(\kappa+\frac34-\frac{7\mu_0}{4r^2})>0$
($\kappa\ge3$, $\mu_0/r^2<1$). $F_{tr} = F_{vr}$ is smooth at $r_h$, and $\Phi = r^{5/2}F_{tr} = O(r^{3/2-\beta})$,
$\Phi_* = O(r^{1/2-\beta})$; so $\Phi = 0$, $F_{tr} = 0$, and with $M = 0$, (M4) gives $a = b = 0$: this part of
$\omega$ is $d(cS)$ for a function $c(r)$. *Scalar type, $l = 0$.* $\kappa = 0$ and $R[W] = (fW'/r)' = 0$, so $fW'/r$ is
constant; it vanishes at $r_h$, as $W$ is smooth there; so $W = q$, a constant, $F_{tr} = qr^{-3}$, and the $l = 0$ part
$a(r)\,dt+b(r)\,dr$ of $\omega$ has $-a' = F_{tr}$. Altogether $d\omega = qr^{-3}\,dt\wedge dr = \frac q2dW^*$.

*(c) The gauge.* $\omega' := \omega-\frac q2W^*$ is smooth across $r_h$, in $\mathcal A^\beta$ near infinity, closed on
$\{r>r_h\}$ and has $\delta\omega' = 0$. With $T = \partial_t$, Cartan's formula and stationarity give $d(\omega'(T)) =
\mathcal L_T\omega'-\iota_Td\omega' = 0$, so $\omega'(T)$ is a constant; it decays, so it is 0. $\{r>r_h\}$ is simply
connected, so $\omega' = d\phi$ with $\partial_t\phi = \omega'(T) = 0$; in the ingoing chart $\omega'$ has no $dv$
component and its $dr$ component $\partial_r\phi$ is smooth at $r_h$, so $\phi$ is smooth in $(r,\omega)$ up to $r_h$.
$d\phi\in\mathcal A^\beta$ gives a constant $\phi_\infty$ with $\phi-\phi_\infty = O(r^{1-\beta})$, and $\delta d\phi =
0$. At $l = 0$, $r^3f\phi_0'$ is constant and vanishes at $r_h$, so $\phi_0$ is constant. At $l\ge1$, the equation
$(r^3f\phi_l')' = \kappa r\phi_l$ has at $r = \infty$ a regular singular point (in $\rho = 1/r$:
$\rho^2f\phi_{\rho\rho}+\rho(\rho f_\rho-f)\phi_\rho-\kappa\phi = 0$, $f = 1-\mu_0\rho^2$) with indicial equation
$\nu^2-2\nu-\kappa = 0$, roots $\nu = l+2$ and $\nu = -l$ for $\phi\sim\rho^\nu$; by Frobenius' theorem every solution
is $c_1\rho^{l+2}a(\rho)+c_2(\rho^{-l}b(\rho)+c_3\log\rho\,\rho^{l+2}a(\rho))$ with $a$, $b$ analytic and $a(0) = b(0) =
1$, and $\phi_l = O(\rho^{\beta-1})$ forces $c_2 = 0$. So $\phi_l = O(r^{-l-2})$, $\phi_l' = O(r^{-l-3})$, and the
energy identity of (a) gives $\phi_l = 0$. So $\omega' = 0$ on $\{r>r_h\}$.

*(d) Inside the horizon.* $u-\frac q2W^*$ lies in $\ker\hat P(0)$, is smooth on $\bar X$ and vanishes on $\{r>r_h\}$;
the argument of III.D Proposition 6.2 (d), which uses only these properties (at $\sigma = 0$), shows that it vanishes on
$\{r_0<r<r_h\}$. So $u = \frac q2W^*$.

(3) By (1) and density, $\ell(\hat P(0)u) = 0$ for $u\in\mathcal X_0$: near the horizon sphere $u\in H^s$, smooth
$u_j\to u$ in $H^s$ there give $\hat P(0)u_j\to\hat P(0)u$ in $H^{s-2}$, and $\ell$ is continuous on $H^{s-2}$ as
$s>\frac52$. $\ell\ne0$ on $\mathcal Y_0$ (for instance $\ell(\zeta(r)\,dt_*) = 2\pi^2r_h^3$ for $\zeta\in C_c^\infty$
with $\zeta(r_h) = 1$). By I.C Corollary 6.6, whose hypotheses hold by section 1, $\hat P(0):\mathcal X_0\to\mathcal
Y_0$ has index 0, so by (2) the annihilator of its range (I.C Theorem 3.1 (1)) is one-dimensional, and it is spanned by
$\ell$. $\square$

## 3. The pairings at the horizon ([Hin26] Lemma 6.11 at n = 4)

**Lemma 3.1.** (1) $\ell([\Box,t_*]W^*) = 4\pi^2$. (2) With $c_{\Upsilon,H} = -\frac12\chi\,dr$ as in section 1,
$\ell(2E_HG\delta^*W^*) = 4\pi^2$. (The source's values are $4\pi$ and $(3\pi,5\pi)$; at $n = 4$ both are $(n-2)|\mathbb
S^{n-1}| = 2\cdot2\pi^2$, at $n = 3$ the first is $1\cdot4\pi$.)

*Proof.* We compute in the ingoing chart at $r = r_h$, where $\ell(v) = r_h^3\int_{\mathbb S^3}v_v\,d\omega$ by (1.1),
$v_v := v(\partial_v)$, and $W^*_v = r^{-2}$, $W^*_r = -(r(r+r_h))^{-1}$. The Christoffel symbols used are, from $g_{vv}
= -f$, $g_{vr} = 1$: $\Gamma^\lambda_{rv} = \frac12g^{\lambda v}\partial_rg_{vv}$, so $\Gamma^r_{rv} = -\frac{f'}2$,
$\Gamma^v_{rv} = 0$; and $\Gamma^\lambda_{vv} = -\frac12g^{\lambda r}\partial_rg_{vv}$, so $\Gamma^v_{vv} = \frac{f'}2$,
$\Gamma^r_{vv} = \frac{ff'}2$. At $r_h$, $f = 0$ and $f' = 2\mu_0r_h^{-3} = 2/r_h$.

(1) $t_*-v = F(r)$ near $r_h$, and $\ell([\Box,F]W^*) = \ell(\Box(FW^*))-\ell(F\Box W^*) = 0$ by Lemma 2.1 (1) and $\Box
W^* = 0$; so $t_*$ may be replaced by $v$. For a function $\varphi$, $\Box(\varphi w) = \varphi\Box
w+(\Box_0\varphi)w-2\nabla_{\nabla\varphi}w$, so $[\Box,v]W^* = (\Box_0v)W^*-2\nabla_{\nabla v}W^*$, with $\nabla v =
g^{vr}\partial_r = \partial_r$ and $\Box_0v = -r^{-3}\partial_r(r^3g^{rv}) = -3/r$. $(\nabla_{\partial_r}W^*)_v =
\partial_rW^*_v-\Gamma^r_{rv}W^*_r = -2r^{-3}-\frac{f'}{2r(r+r_h)}$, which at $r_h$ is $-\frac5{2r_h^3}$. So
$([\Box,v]W^*)_v(r_h) = -\frac3{r_h^3}+\frac5{r_h^3} = \frac2{r_h^3}$ and $\ell = 2|\mathbb S^3| = 4\pi^2$.

(2) By (1.2), $2E_HG\delta^*W^* = 4\iota_{c^\sharp}\delta^*W^*$ with $c := c_{\Upsilon,H}$, and at $r_h$, $c^\sharp =
-\frac12\nabla r = -\frac12(\partial_v+f\partial_r) = -\frac12\partial_v$. So $(4\iota_{c^\sharp}\delta^*W^*)_v =
-2(\delta^*W^*)_{vv}$, and $(\delta^*W^*)_{vv} = \nabla_vW^*_v = -\Gamma^v_{vv}W^*_v-\Gamma^r_{vv}W^*_r =
-\frac1{r_h^3}$ at $r_h$. So $\ell = r_h^3\cdot\frac2{r_h^3}\cdot2\pi^2 = 4\pi^2$. $\square$

*Computed:* `gaugepot5.py` G6 gives both values, $\ell(2E_HG\delta^*W^*) = -12\pi^2c_v-8\pi^2c_r$ for $c_{\Upsilon,H} =
c_v\,dv+c_r\,dr$ at $r_h$, and reproduces the source's $4\pi$ in four dimensions as a control.

## 4. Mode stability ([Hin26] Proposition 6.12 at n = 4)

**Proposition 4.1.** Assume (Dyn). There is $\epsilon_0>0$ such that for every $\gamma_{\Upsilon,H}\in(0,\epsilon_0]$
there are $\epsilon_1>0$ and a neighbourhood $\mathcal B(\gamma_{\Upsilon,H})$ of $b_0$ such that, for $b\in\mathcal
B(\gamma_{\Upsilon,H})$, $e_\Upsilon\in[0,\epsilon_1]$ and $|\gamma_\Upsilon|<\epsilon_1$,
$\widehat{\Box^\Upsilon_b}(\sigma)$ is invertible for every $\sigma$ with $\mathrm{Im}\,\sigma\ge0$: as a map $\mathcal
X_\sigma\to\mathcal Y_\sigma$ when $\sigma\ne0$, and when $\sigma = 0$ as a map $\mathcal X_0\to\mathcal Y_0$ for every
$s>\frac32$ and every $\alpha$ with $\alpha+2\in(0,\lambda^\Upsilon_{\mathrm s1,2})$. In particular
$\widehat{\Box^\Upsilon_b}(0)$ has trivial kernel on $\mathcal A^\epsilon(\bar X;E)$ for every $\epsilon>0$.

*Proof. Step 1: the horizon modification alone, at $b_0$.* For $\gamma\in[0,1]$ let $\mathsf p_\gamma :=
(b_0,0,0,\gamma)$ and $\hat P_\gamma := \hat P_{\mathsf p_\gamma}$, so

$$\hat P_\gamma(\sigma) = \hat P(\sigma)+2\gamma E_HG\widehat{\delta^*}(\sigma),\qquad\widehat{\delta^*}(\sigma)
= \delta^*+\sigma\delta^*_1,\quad\delta^*_1w := -i\,dt_*\otimes_sw,$$

and $\hat P(\sigma) = \hat P(0)+\sigma T+\sigma^2P_2$ (I.A section 1) with $T = \partial_\sigma\hat P(0) = -i[\Box,t_*]$
(as $e^{i\sigma t_*}\Box e^{-i\sigma t_*} = \Box-i\sigma[\Box,t_*]+O(\sigma^2)$) and $P_2$ of order 0. Fix $\psi,\phi\in
C_c^\infty(X^\circ;E)$ with $\ell(\psi)\ne0$ (section 2, (3)) and $\langle W^*,\phi\rangle_h = 1$, and let $\mathcal
P_\gamma(\sigma)$ be the augmented operator of I.C (6.5) with $m_1 = m_2 = 1$,

$$\mathcal P_\gamma(\sigma)(u,c) := \big(\hat P_\gamma(\sigma)u+c\psi,\ \langle u,\phi\rangle_h\big).$$

*(Z$_{\mathcal P}$) at $\gamma = 0$.* $\mathcal P_0(0):\mathcal X_0\oplus\mathbb C\to\mathcal Y_0\oplus\mathbb C$ is
invertible. If $\hat P(0)u+c\psi = 0$ and $\langle u,\phi\rangle_h = 0$, applying $\ell$ gives $c\,\ell(\psi) = 0$
(Lemma 2.1 (3)), so $c = 0$, $u = kW^*$ (Lemma 2.1 (2)) and $k = \langle u,\phi\rangle_h = 0$. Given $(f,e)$, $c :=
\ell(f)/\ell(\psi)$ makes $f-c\psi$ annihilated by $\ell$, so $f-c\psi = \hat P(0)u_0$ (the range is closed and its
annihilator is spanned by $\ell$), and $u := u_0+(e-\langle u_0,\phi\rangle_h)W^*$ solves $\mathcal P_0(0)(u,c) =
(f,e)$.

*Uniform low-energy theory.* The family $\gamma\mapsto\hat P_\gamma$, $\gamma\in[0,1]$, satisfies (H1)-(H5), (G) and
(TF) (section 1; the horizon term is compactly supported in $X^\circ$, so the normal operators at $\partial X$ and at tf
do not depend on $\gamma$). By I.C Theorem 7.1 at $\gamma = 0$ and I.C Theorem 6.4, there are $\gamma_1\in(0,1]$,
$c_0>0$ and $C$ such that for $\gamma\in[0,\gamma_1]$: $\mathcal P_\gamma(\sigma)$ is invertible for $|\sigma|\le c_0$,
$\mathrm{Im}\,\sigma\ge0$ ($\sigma = 0$ by Theorem 7.1 (1), $\sigma\ne0$ by Theorem 6.4 (3)); $\|(u,c)\|\le C\|\mathcal
P_\gamma(0)(u,c)\|$ on $\mathcal X_0\oplus\mathbb C$ (proof of Theorem 7.1); and (6.6) of Theorem 6.4 (1) with $k = 0$
holds with the constant $C$ for $0<|\sigma|\le c_0$. Let

$$(u_{\sigma,\gamma},c_{\sigma,\gamma}) := \mathcal P_\gamma(\sigma)^{-1}(0,1).$$

*The Schur complement.* If $c_{\sigma,\gamma}\ne0$, then $\hat P_\gamma(\sigma)$ is invertible (on $\mathcal
X_\sigma\to\mathcal Y_\sigma$, or $\mathcal X_0\to\mathcal Y_0$ at $\sigma = 0$). Write $(u,c) :=
(u_{\sigma,\gamma},c_{\sigma,\gamma})$, so $\hat P_\gamma(\sigma)u = -c\psi$ and $\langle u,\phi\rangle_h = 1$. If $\hat
P_\gamma(\sigma)w = 0$, then $\mathcal P_\gamma(\sigma)(w,0) = \langle w,\phi\rangle_h(0,1)$, so $(w,0) = \langle
w,\phi\rangle_h(u,c)$, whence $\langle w,\phi\rangle_hc = 0$, $\langle w,\phi\rangle_h = 0$ and $w = 0$. Given $f$, let
$(w,d) := \mathcal P_\gamma(\sigma)^{-1}(f,0)$; then $\hat P_\gamma(\sigma)(w-\frac dcu) = f-d\psi+d\psi = f$.

*The expansion.* By Lemma 2.1 (1) and density, $\ell(\hat P(0)v) = 0$ for every $v$ that is $H^s$ near the horizon
sphere ($s>\frac52$), so applying $\ell$ to $\hat P_\gamma(\sigma)u+c\psi = 0$ gives

$$c_{\sigma,\gamma}\,\ell(\psi)
= -\sigma\,\ell(Tu)-\sigma^2\ell(P_2u)-2\gamma\,\ell(E_HG\delta^*u)-2\gamma\sigma\,\ell(E_HG\delta^*_1u),\qquad u
= u_{\sigma,\gamma}.\tag{4.1}$$

*Claim:* as $(\sigma,\gamma)\to(0,0)$ with $|\sigma|\le c_0$, $\mathrm{Im}\,\sigma\ge0$, $\gamma\in[0,\gamma_1]$,
$c_{\sigma,\gamma}\to0$ and $u_{\sigma,\gamma}\to W^*$ in $H^{s'}(K)$ for every compact $K\subset X^\circ$ and $s'<s$.
Let $(\sigma_j,\gamma_j)\to(0,0)$, and $(u_j,c_j)$ the corresponding pairs; $|c_j|\le C$. Let $\varphi\in
C^\infty([0,\infty))$ vanish on $[0,1]$ and equal 1 on $[2,\infty)$, and put $w_j := \varphi(\rho/\varsigma_j)u_j$,
$\varsigma_j = |\sigma_j|$ (and $w_j := u_j$ if $\sigma_j = 0$). By I.C Lemma 6.2 (b) and (a) (with $q = 0$, $l =
\alpha$), $w_j$, supported in $\{\rho\ge\varsigma_j\}$, has $\|w_j\|_{\bar H^{s,\alpha}_{\mathrm b}}\le
C'\|u_j\|_{s,(\mathsf r+\alpha_+,\alpha,0),\varsigma_j}\le C'C$, uniformly in $j$. Pass to a subsequence with
$w_j\rightharpoonup w$ weakly in $\bar H^{s,\alpha}_{\mathrm b}$ and $c_j\to c$. As $w_j = u_j$ on
$\{\rho>2\varsigma_j\}$, on each compact $K'\subset X^\circ$ the $u_j$ equal the $w_j$ for large $j$ and are bounded in
$H^s(K')$; so $u_j\to w$ in distributions on $\bar X\setminus\partial X$, and by Rellich $u_j\to w$ in $H^{s'}(K)$. The
coefficients of $\hat P_{\gamma}(\sigma)$ depend polynomially on $(\sigma,\gamma)$, so $\hat P(0)w+c\psi = 0$, whence
$w\in\mathcal X_0$, and $\langle w,\phi\rangle_h = \lim\langle u_j,\phi\rangle_h = 1$. So $\mathcal P_0(0)(w,c) =
(0,1)$, and $(w,c) = (W^*,0)$. The limit does not depend on the subsequence, which proves the claim.

Since $\ell$ involves only the values at the horizon sphere of $Tu$ and $E_HG\delta^*u$, first-order operators, the
claim with $s'\in(\frac32,s)$ gives $\ell(Tu_{\sigma,\gamma})\to\ell(TW^*) = -i\,\ell([\Box,t_*]W^*) = -4\pi^2i$ and
$2\ell(E_HG\delta^*u_{\sigma,\gamma})\to2\ell(E_HG\delta^*W^*) = 4\pi^2$ (Lemma 3.1), while $\ell(P_2u)$ and
$\ell(E_HG\delta^*_1u)$ stay bounded. So (4.1) reads

$$c_{\sigma,\gamma}\,\ell(\psi) = -4\pi^2(-i\sigma+\gamma)+o(|\sigma|+\gamma).$$

For $\mathrm{Im}\,\sigma\ge0$ and $\gamma\ge0$, $|{-i\sigma}+\gamma|^2
= |\sigma|^2+2\gamma\,\mathrm{Im}\,\sigma+\gamma^2\ge\frac12(|\sigma|+\gamma)^2$. So there are $c_1\in(0,c_0]$ and
$\gamma_2\in(0,\gamma_1]$ with $c_{\sigma,\gamma}\ne0$ whenever $|\sigma|\le c_1$, $\gamma\in[0,\gamma_2]$,
$\mathrm{Im}\,\sigma\ge0$ and $(\sigma,\gamma)\ne(0,0)$. By the Schur complement, *for $\gamma\in(0,\gamma_2]$, $\hat
P_\gamma(\sigma)$ is invertible for all $|\sigma|\le c_1$ with $\mathrm{Im}\,\sigma\ge0$, $\sigma = 0$ included*; $c_1$
does not depend on $\gamma$.

*Step 2: the whole family, at every frequency.* Let $\epsilon$ and $\mathcal B''$ be those of III.D Proposition 6.3 for
its $c_0 := c_1$, and $\epsilon_0 := \min(\gamma_2,\frac12\epsilon)$. Fix $\gamma\in(0,\epsilon_0]$. At $\mathsf
p_\gamma$, $\hat P_\gamma(\sigma)$ is invertible for every $\sigma$ with $\mathrm{Im}\,\sigma\ge0$: for $|\sigma|\le
c_1$ by Step 1, for $|\sigma|\ge c_1$ by III.D Proposition 6.3 ($\gamma<\epsilon$, $b_0\in\mathcal B''$). Now vary
$\mathsf p = (b,e_\Upsilon,\gamma_\Upsilon,\gamma)$ near $\mathsf p_\gamma$, $e_\Upsilon\ge0$. (i) *Low energies.* (Z)
holds at $\mathsf p_\gamma$, so by I.C Theorem 7.1 (with $m_1 = m_2 = 0$, base point $\mathsf p_\gamma$) and Theorem 6.4
(3) there are $c_0(\gamma)>0$ and a neighbourhood $N_1$ of $\mathsf p_\gamma$ on which $\hat P_{\mathsf p}(0)$ is
invertible and $\hat P_{\mathsf p}(\sigma)$ is invertible for $0<|\sigma|\le c_0(\gamma)$. (ii) *High energies.* By
III.D Proposition 6.1 there is $C_0$ with invertibility for $|\sigma|\ge C_0$ and all $\mathsf p$ in $\mathcal K$. (iii)
*The compact middle.* On $\{c_0(\gamma)\le|\sigma|\le C_0,\ \mathrm{Im}\,\sigma\ge0\}$, compact, $\hat P_{\mathsf
p_\gamma}(\sigma)$ is invertible at each point, and invertibility is open in $(\sigma,\mathsf p)$ (I.A Theorem 8.1, as
in the proof of III.D Proposition 6.3); finitely many neighbourhoods cover it, giving $N_2$. On $N_1\cap N_2\cap\mathcal
K$, which contains $\mathcal B(\gamma)\times[0,\epsilon_1]\times(-\epsilon_1,\epsilon_1)\times\{\gamma\}$ for some
neighbourhood $\mathcal B(\gamma)$ and $\epsilon_1>0$, invertibility holds for every $\sigma$. At $\sigma = 0$ it holds
for one pair $(s,\alpha)$, hence for all $s>\frac32$ and all $\alpha$ with $\alpha+2$ in the gap
$(0,\lambda^\Upsilon_{\mathrm s1,2})$ (I.C Theorem 3.1 (4)); for $\sigma\ne0$ the kernel and the annihilator of the
range do not depend on the admissible orders (I.A Theorem 7.2 (3)).

*The kernel on $\mathcal A^\epsilon$.* $\mathcal A^\epsilon(\bar X;E)\subset\bar H^{s,\alpha}_{\mathrm b}$ when
$\alpha+2<\epsilon$: its elements are smooth up to $\partial_\sharp X$, and near $\partial X$ they and their
b-derivatives are $O(\rho^\epsilon)$, which lies in $\rho^{\alpha+2}L^2(\mu_{\mathrm b}) = \bar H^{0,\alpha}_{\mathrm
b}$ (I.C Remark (a) after section 1.2); and $\alpha+2\in(0,\min(\epsilon,\lambda^\Upsilon_{\mathrm s1,2}))$ is allowed;
a kernel element there lies in $\mathcal X_0$ and vanishes. $\square$

*Remarks.* (a) The source states triviality of the nullspace on $\mathcal A^\alpha$ for every $\alpha$ also when
$\sigma\ne0$. That needs $\mathcal A^\alpha\subset\mathcal X_\sigma$ for suitable admissible orders, which I.A states
only for the weight $\frac32+\bar S-\epsilon$ (Theorem 7.2 (5)); it is not claimed here and is not used in this proof.
(b) The neighbourhood $\mathcal B(\gamma_{\Upsilon,H})$ of $b_0$ depends on $\gamma_{\Upsilon,H}$, as $\epsilon_1$ does
in the source; the later parts fix $\gamma_{\Upsilon,H}$ once and then work near $b_0$.

## 5. The zero energy operator ([Hin26] Lemma 6.13 at n = 4)

**Lemma 5.1.** Assume (Dyn), and let $E_\Upsilon$ and $b$ be as in Proposition 4.1. Use an unweighted b-density near
$\partial X$ to define $L^2$, so that $\bar H^{s,\alpha}_{\mathrm b}$ here is I.C's $\bar H^{s,\alpha-2}_{\mathrm b}$.
(1) For $s>\frac32$ and $\alpha\in(0,\lambda^\Upsilon_{\mathrm s1,2})$, $\widehat{\Box^\Upsilon_b}(0):\{u\in\bar
H^{s,\alpha}_{\mathrm b}:\widehat{\Box^\Upsilon_b}(0)u\in\bar H^{s-1,\alpha+2}_{\mathrm b}\}\to\bar
H^{s-1,\alpha+2}_{\mathrm b}$ is invertible. (2) If $f\in\mathcal A^{2+\mathcal E}(\bar X;E)$ for an index set $\mathcal
E$ with $\min\mathrm{Re}\,\mathcal E>0$, then $\widehat{\Box^\Upsilon_b}(0)^{-1}f\in\mathcal A^{\mathcal E'}(\bar X;E)$
for an index set $\mathcal E'$ with $\min\mathrm{Re}\,\mathcal E'>0$.

*Proof.* (1) With $\alpha' := \alpha-2$, the map is $\mathcal X_0\to\mathcal Y_0$ of I.C (3.1) with the weight
$\alpha'$, $\alpha'+2 = \alpha$ in the gap; this is Proposition 4.1 at $\sigma = 0$. The threshold is $\frac32$ for
every $\gamma_{\Upsilon,H}$ (III.D Lemma 5.1; the source's footnote 71 has $\frac32$ at $\gamma_{\Upsilon,H} = 0$ and
nearby values otherwise).

(2) Fix $\alpha\in(0,\min(\min\mathrm{Re}\,\mathcal E,\lambda^\Upsilon_{\mathrm s1,2}))$. Then $f\in\bar
H^{s-1,\alpha+2}_{\mathrm b}$ for every $s$ (in b-densities $\rho^{2+z}\in H^{\infty,\alpha+2}_{\mathrm b}$ near
$\partial X$ when $\mathrm{Re}\,z>\alpha$, and $f$ is smooth up to $\partial_\sharp X$). Let $u_s$ be the inverse image
given by (1) for the regularity $s$. For $s'>s$, $u_{s'}$ lies in the domain for $s$ and solves the same equation, so
$u_{s'} = u_s =: u$, and $u\in\bigcap_s\bar H^{s,\alpha}_{\mathrm b}$: smooth up to $\partial_\sharp X$, and of class
$H^{\infty,\alpha}_{\mathrm b}$ near $\partial X$. Near $\partial X$, $\widehat{\Box^\Upsilon_b}(0) = \rho^2A$ with $A
:= P^{(0)}$ an elliptic b-operator on the trivial bundle (I.C (1.1)-(1.3)), and $\chi Au = \chi\rho^{-2}f\in\mathcal
A^{\mathcal E}\subset H^{\infty,(\mathcal E,\beta)}_{\mathrm b}$ for every $\beta$. III.A Lemma 1.4 then gives
$\tilde\chi u\in H^{\infty,(\mathcal E_\beta,\beta)}_{\mathrm b}$ for every
$\beta\notin\mathrm{Re}\,\mathrm{spec}_{\mathrm b}(A)$, where the index set built there from $E(\alpha)$ (the boundary
spectrum with $\mathrm{Re}\,\lambda>\alpha$), $\mathcal E$ and their shifts by $\mathbb N_0$ is independent of $\beta$
(Lemma 1.4's $E$); call it $\mathcal E'$. So $u\in\mathcal A^{\mathcal E'}$, and $\min\mathrm{Re}\,\mathcal
E'\ge\min(\alpha,\min\mathrm{Re}\,\mathcal E)>0$. Lemma 1.4 is stated for scalar operators; its proof uses $A$ only
through the meromorphy of $N(A,\lambda)^{-1}$ with the bounds of its proof's (M2) and (E1)-(E2) on vertical strips,
which hold for the matrix-valued indicial family $I(\lambda)$ of I.C (1.3) by I.C Lemma 2.4, so it applies verbatim on
$E$. $\square$

## 6. Findings, labels and sources

### 6.1 Findings

(D$'$1) *[AHW24] replaced at zero energy.* On five-dimensional Tangherlini the kernel of the 1-form wave operator at
zero energy on the weighted spaces is spanned by $W^* = r^{-2}dt+r_hr^{-3}f^{-1}dr$, smooth across the future horizon
and decaying like $r^{-2}$, and the annihilator of the range by the pairing with $d(H(r-r_h))$. The kernel is proved by
the energy identities of the stationary mode equations (Lemma 2.1 (2)); the cokernel by the distributional identity
$\Box_0H(r-r_h) = 0$, which says that the horizon is characteristic for the stationary operator, together with $\Box d =
d\Box_0$ and the index 0 of I.C Corollary 6.6. The source takes both from [AHW24] Theorem 5.1 (2).

(D$'$2) *The pairings.* $\ell([\Box,t_*]W^*) = 4\pi^2$ and, with $c_{\Upsilon,H} = -\frac12\chi\,dr$,
$\ell(2E_HG\delta^*W^*) = 4\pi^2$ exactly: $(n-2)|\mathbb S^{n-1}|$, the source's $4\pi$ at $n = 3$. The first does not
depend on the choice of $t_*$ near the horizon (Lemma 3.1 (1)). With the trace weight $\frac23$, $E_HG =
2\iota_{c^\sharp}$, as at $n = 3$ with the weight 1.

(D$'$3) *Step 1 by a Grushin problem.* With a fixed compactly supported augmentation (I.C (6.5)) the uniform low-energy
theory of I.C Theorems 6.4 and 7.1 applies as proved, and the Schur complement $c_{\sigma,\gamma}$ is computed from the
two pairings alone: $c_{\sigma,\gamma}\ell(\psi) = -4\pi^2(-i\sigma+\gamma)+o(|\sigma|+\gamma)$, the counterpart of the
source's (6.26). The source's augmentation $\widehat{\Box_\gamma}(\sigma)(\lambda^{-1}\omega_{(0)})$ depends on the
joint parameter, which needs the estimate (6.27) to be reproved for it and the decay $\rho^3$ of
$\partial_\sigma\widehat\Box(0)\omega_{(0)}$ (his footnote 69, the reason he adds the modification at infinity only in
Step 2); neither is needed here. At $n = 4$ that decay holds anyway, by the dimension (supplement 10.15 (vi)).

(D$'$4) *Step 2 and the size of the low-energy region.* The source's Step 2 asserts that the radius $c_0$ of the
low-energy region is independent of $\gamma_{\Upsilon,H}$, $e_\Upsilon$ and $\gamma_\Upsilon$, with $c_0$ "as in
[Hin26c] Theorem 9.41" for the operator with the horizon modification $\gamma_{\Upsilon,H}$; as written, that radius is
the one of Theorem 9.41 for each such operator and may depend on $\gamma_{\Upsilon,H}$, and the independence is needed
to apply Proposition 6.9 with a fixed $c_0$. The step is closed here by perturbing around a base point at which
invertibility already holds at every frequency (Step 1 on $|\sigma|\le c_1$ with $c_1$ independent of $\gamma$,
Proposition 6.3 at $c_1$), at low, middle and high frequencies separately. The conclusion is the source's.

(D$'$5) *Lemma 6.13.* The infinite regularity of the inverse image, which Lemma 2.13 (III.A Lemma 1.4) requires, comes
from the invertibility at every regularity order; Lemma 2.13 is applied on the bundle, where its proof holds verbatim.
The threshold is $\frac32$ for every $\gamma_{\Upsilon,H}$ (III.D (D6)).

### 6.2 Labels

Proved here, assuming (Dyn) (Part VI): Lemmas 2.1, 3.1, 5.1 and Proposition 4.1. Computed (exact; rerun D222):
`gaugepot5.py` G4-G6, `modes5.py` M3-M4. Standard facts used: integration by parts, the trace theorem, Rellich's
theorem, Frobenius' theorem at a regular singular point, Cartan's formula, and the simple connectivity of
$(r_h,\infty)\times\mathbb S^3$.

### 6.3 Sources

READ: [Hin26] pp. 119-125 (section 6.4 from its first paragraph through Proposition 6.12 and its proof, (6.20)-(6.28),
and Lemma 6.13 with footnotes 65-71), arXiv:2606.28253v2, full text. The record's supplement 10.15 (N1STAR-PROOF.md) for
the computed statements (G4-G6). Not relied on: [AHW24] Theorem 5.1 (replaced by Lemma 2.1 and III.D Proposition 6.2),
[Hin24b] Propositions 3.7, 3.12 and Lemma 3.8 (whose arguments the source follows; replaced by sections 3-4).
