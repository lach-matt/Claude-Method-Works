# Part VI.A: the dynamical hypotheses at Tangherlini

*Status.* Written (D314). Parts I-IV state their dynamical hypotheses for a class of metrics and leave their
verification for the record's metrics to Part VI (III.D's introduction: "we write (Dyn) for them"). These are: the
radial structure of the horizon in (H3) and (H4) (I.A section 1.3), the Lorentzian structure and the time function (H6),
the normally hyperbolic trapping (Γ.1)-(Γ.3) in (H7), the global dynamics (H8) (I.B sections 1.2 and 1.5), and
$r$-normal hyperbolicity (K3) with the decay (K1) (II.B section 1.1). This part proves them for five-dimensional
Schwarzschild-Tangherlini $g_{b_0}$, $b_0 = (\mu_0,0)$, with III.B's time function $t_*$ (Theorem 6.1). (H6) and (K1)
are proved for every $b\in\mathcal B$. Part VI.B carries the others to $b$ near $b_0$ with the uniformity (H5) and (K4);
Part VI.C collects the parameter conditions the parts leave open. The threshold in (H3) and the bound (Γ.4) in (H7)
involve the subprincipal symbol, so they are operator hypotheses, proved for each operator in III.D, III.F and Part
IV$''''$. The dynamical hypotheses concern the metric alone. Every operator whose principal symbol is
$g_b^{-1}\otimes\mathrm{Id}$ has them. The record's computations used here are N1STAR-PROOF.md 10.14 (Proposition 10.14
(ii)) and 10.19 (Proposition 10.16 (ii), (iv)). Each is re-derived below in closed form.

## 0. Coordinates and the spectral symbols

Write $\mu := \mu_0$, $f := 1-\mu r^{-2}$, $r_h := \mu^{1/2}$, $r_{\mathrm{ph}} := (2\mu)^{1/2}$, and let $\slashed g$
be the round metric of $\mathbb S^3$. By III.B (3.3) and Lemma 3.5, $g_{b_0}$ is $\Phi_\mu^*g^{\mathrm{KS}}_{\mu,0}$,
where $\Phi_\mu$ changes the time coordinate by a function of $r = |x|$, and $g^{\mathrm{KS}}_{\mu,0} = \eta+\mu
r^{-2}(dt+dr)^2$ (III.B Proposition 3.4). With $v := t_{\mathrm{KS}}+r$,
$$g_{b_0} = -f\,dv^2+2\,dv\,dr+r^2\slashed g\qquad\text{on }\mathbb R_v\times\{r\ge r_0\},\tag{0.1}$$
as a direct expansion shows: $-f\,dv^2+2\,dv\,dr = -(1-H)dt^2+2H\,dt\,dr+(1+H)dr^2$ with $H = \mu r^{-2}$. Every time
function used here has the form $\tau = v-\varphi(r)$ with $\varphi$ smooth: III.B's $t_*$ (III.B (3.6)) is one, and on
$\{r>r_h\}$ so is the static time $t_s := v-r_*$, $r_*' = f^{-1}$, in which $g_{b_0} = -f\,dt_s^2+f^{-1}dr^2+r^2\slashed
g$.

*The symbols.* For a time function $\tau$ with $d\tau$ timelike, I.B (1.1) defines $G_0$, $\tau_1$, $g_{00}$ by
$G(-\sigma\,d\tau+\zeta) = G_0(\zeta)+\sigma\tau_1(\zeta)+\sigma^2g_{00}$, $G := g^{-1}$, $\zeta\in T^*\tilde X$, and
for $z_0\in\{1,-1\}$, $G_{z_0}(\zeta) := G(-z_0\,d\tau+\zeta)$. Write $\zeta = \xi\,dr+\eta$ with $\eta\in T^*\mathbb
S^3$ and $C := |\eta|^2_{\slashed g}$. From (0.1), $G^{vv} = 0$, $G^{vr} = 1$, $G^{rr} = f$, and $d\tau =
dv-\varphi'dr$, so
$$G_0 = f\xi^2+r^{-2}C,\qquad\tau_1 = -2(1-\varphi'f)\xi,\qquad g_{00} = \varphi'^2f-2\varphi',\tag{0.2}$$
$$G^{(\varphi)}_{z_0} = f\xi^2+r^{-2}C-2z_0(1-\varphi'f)\xi+\varphi'^2f-2\varphi'.$$
At $\varphi = 0$ this is $f\xi^2-2z_0\xi+r^{-2}C$, regular for all $r>0$. At $\varphi = r_*$, on $r>r_h$, it is $G^s :=
f\xi^2+r^{-2}C-f^{-1}$, the static form of record Proposition 10.16 (ii).

**Lemma 0.1 (change of time function).** Let $\tau' = \tau-F(r)$, both time functions with timelike differential on a
region $U$. Then $G'_{z_0}(\zeta) = G_{z_0}(\zeta+z_0\,dF)$. The fibre translation
$T_F:(x,\zeta)\mapsto(x,\zeta+z_0\,dF(x))$ is a symplectomorphism of $T^*U$ that maps $\{G'_{z_0} = 0\}$ onto $\{G_{z_0}
= 0\}$ and intertwines the Hamilton fields. It preserves the time orientation of the null covectors $-z_0\,d\tau'+\zeta
= -z_0\,d\tau+(\zeta+z_0dF)$, and so the future fields on corresponding components. It preserves fibre infinity and $C$,
and it moves $\xi$ by $z_0F'(r)$.

*Proof.* $-z_0\,d\tau'+\zeta = -z_0\,d\tau+\zeta+z_0\,dF$. Translation by a closed 1-form is symplectic, and $G'_{z_0} =
G_{z_0}\circ T_F$, so $T_F$ maps Hamilton fields to Hamilton fields. The covector is the same spacetime covector. For a
null $\nu\ne0$, $g^{-1}(\nu,d\tau)$ and $g^{-1}(\nu,d\tau')$ have the same sign, since $d\tau$ and $d\tau'$ are timelike
with the same orientation. That sign fixes the component (I.B Lemma 1.1 (e)). $\square$

So every statement about the flow of $G_{z_0}$ on a region of $r$ may be proved in whichever time function is convenient
there: $v$ near and inside the horizon, $t_s$ on $\{r>r_h\}$, $t_*$ near infinity. The future field on
$\Sigma^{\pm}_{z_0}$ is $\pm H_{G_{z_0}}$ (I.B section 1.3). On $\{r>r_h\}$ in static variables, $q_{z_0} =
2G(-z_0dt_s+\zeta,dt_s) = 2z_0f^{-1}$, so only $\Sigma^{z_0}_{z_0}$ occurs there, with future field $\mathsf H^\flat :=
z_0H_{G^s}$.

## 1. The Lorentzian structure and the decay ((H6), (K1))

**Lemma 1.1.** For every $b\in\mathcal B$, with $\tau = t_*$: $g_b$ is a smooth Lorentzian metric of signature $(1,4)$
on $\mathbb R\times\{|x|\ge r_0\}$ with $t_*$-independent components, $g_{00} = g_b^{-1}(dt_*,dt_*)<0$, and
$G_0,\tau_1,g_{00}$ are given by I.B (1.1). On $\{r>3R_1\}$ the components of $g_b-\bar g$ in the frame $dt_*,dx^i$ lie
in $\rho^2C^\infty(\bar X)$, uniformly and smoothly in $b$. So (H6), (K1) and (K4)'s first clause hold.

*Proof.* III.B Proposition 3.6 gives smoothness and $g_b-\bar g\in|x|^{-2}C^\infty$, smoothly in $b$. III.B Lemma 3.7
(a) gives that $dt_*$ is timelike, and $t_*$-independence holds as $t_*-t$ is a function of $|x|$. In the frame
$dt_*,dx^i$ the components of $\bar g$ differ from those in $dt,dx^i$ by $\psi'(|x|)\hat x$-terms; III.B (3.6) has
$\psi'-1\in\rho^2C^\infty$ near infinity (II.B Remark (a) for $b_0$; the same $\psi$ for every $b$). $\square$

## 2. The horizon ((H3), (H4) at $b_0$)

Fix I.A's radii as follows: $r_0-2\delta_0 := \frac12R_1$ (III.B's inner radius), $\delta_0 := \frac18(r_h-\frac12R_1)$,
$r_0 := \frac12R_1+2\delta_0$, $r_2 := r_h-2\delta_0$, $r_e := r_h+\delta_0$. These are positive and ordered, as
$r_h>R_1/\sqrt2$ (III.B Proposition 3.4). $\mathcal H := \{r = r_h\}$, $\rho_\infty := |\xi|^{-1}$ near $N^*\mathcal H$,
and $\mathcal R_\pm := \{r = r_h,\eta = 0,\pm\xi>0\}$.

**Proposition 2.1.** With $\tau = t_*$, (H3) holds at $b_0$ with $\beta_0 = f'(r_h) = 2\mu^{-1/2}$, $\beta = 2/\beta_0 =
\mu^{1/2}$, $q_\pm := |\eta/\xi|^2_{\slashed g}$ restricted to $\partial\Sigma_0$ and $c = \beta_0$. (H4) holds with
these radii.

*Proof.* By (0.2), $G_0 = f\xi^2+r^{-2}C$ does not depend on $\varphi$. Its Hamilton field is
$$H_{G_0} = 2f\xi\,\partial_r-(f'\xi^2-2r^{-3}C)\,\partial_\xi+r^{-2}H^{\mathbb S^3}_C,\tag{2.1}$$
with $H^{\mathbb S^3}_C$ the geodesic spray of $\slashed g$, which preserves $C$. At fibre infinity, $\{G_0 = 0\}$
requires $f\le0$, and $\xi\ne0$ there. So $\partial\Sigma_0$ lies over $\{r\le r_h\}\subset\{r\le r_e\}$. It has the two
components $\pm\xi>0$, it is invariant under the dilations, and $N^*\mathcal H\setminus o\subset\Sigma_0$. The
future-directed rescaled field is $\mathsf H := \mathrm{sgn}(\xi)\rho_\infty H_{G_0}$: then $\mathsf Hr = 2f<0$ for
$r<r_h$, the future direction decreasing $r$ inside the horizon, as (H4) requires. On $\partial\mathcal R_\pm$: $\mathsf
H\rho_\infty = \mathrm{sgn}(\xi)|\xi|^{-1}(-f'\xi^2)\partial_\xi|\xi|^{-1} = f'|\xi|^{-1}$, so $\beta_0 =
\rho_\infty^{-1}\mathsf H\rho_\infty = f'(r_h) = 2\mu/r_h^3>0$. By (0.2), $\tau_1 = -2\xi$ at $r = r_h$ for every
$\varphi$, so $\mp\beta_0^{-1}\rho_\infty\tau_1 = 2/\beta_0$ on $\partial\mathcal R_\pm$, which gives $\beta$. On
$\partial\Sigma_0$, $|\eta/\xi|^2 = -fr^2$, so $(\omega,\hat\eta := \eta/\xi)$ are coordinates there with
$\partial\mathcal R_\pm = \{\hat\eta = 0\}$, and $q := |\hat\eta|^2$ is a quadratic defining function. As $H_{G_0}C =
0$, (2.1) gives
$$\mathsf Hq = \mathrm{sgn}(\xi)|\xi|^{-1}\cdot C\cdot(-2\xi^{-3})(-f'\xi^2+2r^{-3}C) = 2q\,(f'(r)-2r^{-3}q),$$
which is $\ge\beta_0q$ near $\partial\mathcal R_\pm$, where $f'(r)\to f'(r_h)$ and $q\to0$.

(H4): every maximal integral curve of $\mathsf H$ in $\partial\Sigma_0\setminus\partial\mathcal R_\pm$ lies in
$\{r<r_h\}$, where $\mathsf Hr = 2f<0$. Backward, $r$ increases, is bounded by $r_h$, and converges to a zero of $f$, as
$\dot r = 2f$; so $r\to r_h$. On $\partial\Sigma_0$, $q = -fr^2\to0$, so the curve tends to $\partial\mathcal R_\pm$.
Forward, $r$ decreases at the rate $|2f|\ge2|f(r)|$, bounded below once $r\le r_h-\epsilon$, so the curve reaches
$\{r<r_0-\delta_0\}$ at a finite parameter. On $\{r_0-2\delta_0<r<r_2\}$, $f<0$: $G_0 = f\xi^2+r^{-2}C$ is Lorentzian of
signature $(1,3)$, $G_0(dr) = f<0$, and $\mathsf Hr<0$ on $\partial\Sigma_0$. $\square$

## 3. The trapped set ((Γ.1)-(Γ.3) at $b_0$)

On $\{r>r_h\}$ use static variables (Lemma 0.1). Put $u(r) := 1-2\mu r^{-2}$ and, near $\Gamma$ and on $\Sigma^s :=
\{G^s = 0\}$,
$$\phi_1 := f\xi-u,\qquad\phi_2 := f\xi+u,\qquad\Gamma := \{r = r_{\mathrm{ph}},\ \xi = 0\}\cap\Sigma^s = \{r =
r_{\mathrm{ph}},\xi = 0,C = 4\mu\}.\tag{3.1}$$

**Proposition 3.1.** For $z_0\in\{1,-1\}$, with the future field $\mathsf H^\flat = z_0H_{G^s}$ on $\Sigma^s$:

(a) $\Gamma$ is compact, lies in $T^*\{r_2<r<\rho_1^{-1}\}$ for any $\rho_1<r_{\mathrm{ph}}^{-1}$, and is invariant;

(b) on $\Sigma^s$ near $\Gamma$, exactly,
$$\mathsf H^\flat\phi_1 = -\nu_1\phi_1,\qquad\mathsf H^\flat\phi_2 = \nu_2\phi_2,\qquad\nu_{1,2} =
\frac{2z_0\big(r^4\pm\xi(r^2-\mu)(r^2-2\mu)\big)}{r^3(r^2-\mu)},\tag{3.2}$$
with $\nu_1 = \nu_2 = 4z_0(2\mu)^{-1/2}$ on $\Gamma$;

(c) $\{\phi_1,\phi_2\} = (2/\mu)^{1/2}>0$ on $\Gamma$, and $dG^s\ne0$ there.

So (Γ.1)-(Γ.3) hold. For $z_0 = 1$ take $\phi_u := \phi_1$, $\phi_s := \phi_2$; for $z_0 = -1$ take $\phi_u := \phi_2$,
$\phi_s := -\phi_1$. Then $\nu_{\min} = 4(2\mu)^{-1/2}$ for both signs. $\Gamma_{u/s} = \{\phi_{u/s} = 0\}\cap\Sigma^s$
are the two branches of $\{C = 4\mu\}\cap\Sigma^s$.

*Proof.* On $\Sigma^s$, $C = r^2(f^{-1}-f\xi^2)$, so $(f\xi)^2 = 1-CW$ with $W := fr^{-2}$, conserved $C$, and $W' =
2(2\mu-r^2)r^{-5}$ (record Proposition 10.16 (iv)). $W$ has the single critical point $r_{\mathrm{ph}}$ on
$(r_h,\infty)$, a maximum $W = (4\mu)^{-1}$. (a) $\mathsf H^\flat r = 2z_0f\xi$ vanishes on $\Gamma$, and $\mathsf
H^\flat\xi = -z_0\partial_rG^s = -z_0(f'f^{-2}+f'\xi^2-2Cr^{-3})$ vanishes there: at $\xi = 0$, $\partial_rG^s =
f'f^{-2}-2Cr^{-3}$, which at $r_{\mathrm{ph}}$ ($f = \frac12$, $f' = 2\mu r_{\mathrm{ph}}^{-3}$) and $C = 4\mu$ is $8\mu
r_{\mathrm{ph}}^{-3}-8\mu r_{\mathrm{ph}}^{-3} = 0$. $C$ and the $\mathbb S^3$ flow preserve $\Gamma$.
$\Gamma\cong\{(\omega,\eta):|\eta|^2 = 4\mu\}$ is compact. (b) On $\Sigma^s$, $\{\phi_1 = 0\}$ means $f\xi = u$, and
then $C = r^2f^{-1}(1-u^2) = 4\mu$; likewise for $\phi_2$. So $\{\phi_1\phi_2 = 0\}\cap\Sigma^s = \{C =
4\mu\}\cap\Sigma^s$, and each branch is a union of orbits ($C$ is conserved, and the $(r,\xi)$-curve $f\xi = \pm u$ is
invariant under the reduced flow). The identities (3.2) are exact on $\Sigma^s$. The computation substitutes $C =
r^2(f^{-1}-f\xi^2)$ into $\mathsf H^\flat\phi_i$, with $r^4-3\mu r^2+2\mu^2 = (r^2-\mu)(r^2-2\mu)$ (sympy,
`d313/dyn5.py`; the record's $\nu = 4(2\mu)^{-1/2}$ at $\Gamma$, Proposition 10.16 (ii)). (c) $\{\phi_1,\phi_2\} =
\partial_\xi\phi_1\partial_r\phi_2-\partial_r\phi_1\partial_\xi\phi_2 = 2fu'$ at $\xi = 0$, which at $r_{\mathrm{ph}}$
is $2\cdot\frac12\cdot4\mu r_{\mathrm{ph}}^{-3} = (2/\mu)^{1/2}$. $\partial_\eta G^s = 2r^{-2}\eta^\sharp\ne0$, as
$|\eta|^2 = 4\mu$. For $z_0 = -1$ the roles of $\phi_1$ and $\phi_2$ exchange, and the sign of $\phi_s$ restores
$\{\phi_u,\phi_s\}>0$ without changing (Γ.2). $\Gamma$ and $\Gamma_{u/s}$ transfer to the time function $t_*$ by Lemma
0.1. $\square$

## 4. $r$-normal hyperbolicity ((K3) at $b_0$)

**Proposition 4.1.** (K3) holds at $b_0$: $\Gamma$ is eventually absolutely $r$-normally hyperbolic for every $r$, for
$\mathsf V := q_1^{-1}H_{G_1}$ on $\Sigma^\flat_1$.

*Proof.* Work in static variables (Lemma 0.1); $q_1 = 2f^{-1}$, so $\mathsf V = \frac f2H_{G^s}$, and on $\Gamma$,
$\mathsf V = \frac14H_{G^s}$ ($f(r_{\mathrm{ph}}) = \frac12$). Use the coordinates $(r,\xi,\omega,\eta)$ on $\Sigma^s$,
where $C$ is determined by $(r,\xi)$. On $\Gamma$ the flow is $\dot r = \dot\xi = 0$ and $(\omega,\eta)$ moves by
$\frac14r_{\mathrm{ph}}^{-2}H^{\mathbb S^3}_C$, the geodesic flow of the round $\mathbb S^3$ on the cosphere bundle
$\{|\eta|^2 = 4\mu\}$, reparametrised by a constant. Its orbits are periodic, so $De^{s\mathsf V}|_{T\Gamma}$ is bounded
uniformly in $s$, and the tangential bound holds with $C_\epsilon = C$. Normal directions: the linearisation of $\mathsf
V$ at $\Gamma$ is block triangular. The $(\delta r,\delta\xi)$-block is autonomous, with eigenvalues $\pm\frac14\nu$ by
(3.2) at $z_0 = 1$: on $\ker d\phi_2$, tangent to $\Gamma_s$, $d\phi_1$ decays forward at the rate $\frac14\nu$, and on
$\ker d\phi_1$, tangent to $\Gamma_u$, $d\phi_2$ decays backward. The $(\delta\omega,\delta\eta)$-block is driven by
$(\delta r,\delta\xi)$, with $r$ and $C$ entering the spray's speed. As the homogeneous tangential solutions are bounded
and the normal ones grow or decay at the rate $\frac14\nu\ne0$, each normal eigensolution $e^{\pm\nu s/4}v_\pm$ has a
unique tangential correction $e^{\pm\nu s/4}w_\pm$, found by solving the driven equation with the variation-of-constants
integral over $(-\infty,s]$ or $[s,\infty)$. This gives the invariant splitting (1.1) with $\bar N^u$ and $\bar N^s$
spanned by these solutions, continuous along $\Gamma$, with the rates $\mu = \frac14\nu$. $\square$

## 5. The global dynamics ((H8) at $b_0$)

The future integral curves of $G_{z_0}$ project to future null geodesics of $g_{b_0}$ with energy $-\nu(\partial_t) =
z_0$, and $C$ is their squared angular momentum. By Lemma 0.1 each statement below may be checked in the time function
named.

**Proposition 5.1.** (H8) (a) and (b) hold at $b_0$ for $z_0\in\{1,-1\}$, with $\bar\Gamma_u = \{\phi_u =
0\}\cap\Sigma^s\cap\{r>r_h\}$ and $\bar\Gamma_s = \{\phi_s = 0\}\cap\Sigma^s\cap\{r>r_h\}$, and every neighbourhood
$O\subset\{r>r_h\}$ of $\Gamma$.

*Proof.* *Outside the horizon* (static variables). Along $\mathsf H^\flat$, $\dot r = 2z_0f\xi$, $C$ is conserved and
$(f\xi)^2 = 1-CW(r)$, so the radial motion is that of a particle in the potential $CW$, which has a single maximum
$C/(4\mu)$ at $r_{\mathrm{ph}}$ and tends to 0 at $r_h$ and at $\infty$. Three cases.

- $C<4\mu$: $f\xi\ne0$ throughout, so $r$ is strictly monotone.

- $C>4\mu$: $\{CW>1\}$ is an interval $(r_-,r_+)\ni r_{\mathrm{ph}}$ with $r_h<r_-$. A curve stays in $(r_h,r_-]$ or in
$[r_+,\infty)$, with exactly one turning point, where $\xi = 0$ and $\dot\xi\ne0$.

- $C = 4\mu$: the curve lies on $\Gamma$ or on one of the four branches of $\{f\xi = \pm u\}$, along which $r$ is
monotone and tends to $r_{\mathrm{ph}}$ at one end.

In the first two cases the curve meets neither $\bar\Gamma_u$ nor $\bar\Gamma_s$, and $r$ tends, at each end, to $r_h$
or to $\infty$. In the third, the branches with $\phi_u = 0$ are backward asymptotic to $\Gamma$ and those with $\phi_s
= 0$ are forward asymptotic. This identifies $\bar\Gamma_{u/s}$ outside the horizon. Inside the horizon no curve tends
to $\Gamma$, as below.

*At infinity.* If $r\to\infty$ forward, then $(f\xi)^2\to1$ and $\dot r>0$ give $\xi\to z_0$ in static variables. Near
infinity $t_* = t_s-F(r)$ with $F' = 1+O(r^{-2})$ (III.B (3.6) and $r_*' = f^{-1}$), so in $t_*$ variables $\xi\to
z_0-z_0 = 0$, and $\eta/r\to0$ as $C$ is fixed. The curve enters every neighbourhood of $\{\xi = 0,\eta = 0\}$ over
$\partial X$, that is of $R_{\mathrm{out}}$ in the scattering phase space (I.A section 4). Its limit set is compact and
invariant, in the characteristic set over $\partial X$, and in $\{\xi\ge-\epsilon\}$ for every $\epsilon$. By I.A Lemma
4.5 the only such set is $R_{\mathrm{out}}$, so the curve tends to $R_{\mathrm{out}}$. Backward with $r\to\infty$,
$\xi\to-z_0$ and in $t_*$ variables $\xi\to-2z_0$, so the curve tends to $R_{z_0,\mathrm{in}}$ in the same way.

*At the horizon* ($v$ variables, regular across $r = r_h$). On $\{G^{(0)}_{z_0} = 0\}$, $f\xi^2-2z_0\xi+r^{-2}C = 0$.
The roots are $\xi = (z_0\pm(1-fCr^{-2})^{1/2})/f$. One root is regular at $f = 0$, where it tends to $C/(2z_0r_h^2)$;
the other is $\sim2z_0/f$. A future null covector with $\nu(\partial_t) = -z_0\ne0$ is not tangent to the null generator
$\partial_v$ at $\mathcal H$, so $dr(\dot\gamma)<0$ there: on the regular root a curve crosses $\mathcal H$ inward in
finite parameter. Inside, $dr$ is timelike ($G(dr) = f<0$) and $\dot r<0$ strictly. On compact subsets of
$\Sigma_{z_0}\cap\{r_0-\delta_0\le r\le r_h-\epsilon\}$, compactified at fibre infinity, $\dot r$ is bounded above by a
negative constant, including at fibre infinity by Proposition 2.1 ($\mathsf Hr = 2f$). So the curve reaches
$\{r<r_0-\delta_0\}$ in finite parameter. On the singular root, which near $\mathcal H$ is the component
$\Sigma^{-z_0}_{z_0}$ inside and the outgoing branch outside, $|\xi|\to\infty$ as $r\to r_h$ with $C$ fixed. So
$\eta/\xi\to0$ and the curve tends backward to $\partial\mathcal R_+\cup\partial\mathcal R_-$, reaching $r_h$ only
asymptotically.

So every curve not in $\bar\Gamma_u$ tends backward to $\partial\mathcal R_\pm$ or $R_{z_0,\mathrm{in}}$, and every
curve not in $\bar\Gamma_s$ tends forward to $R_{\mathrm{out}}$ or reaches $\{r<r_0-\delta_0\}$ in finite time.
*Uniformity on compact sets* $K$ disjoint from $\bar\Gamma_s$ (resp. $\bar\Gamma_u$): the set of initial points whose
forward curve enters $\{r>R\}\cap\{\xi>-\epsilon\}$ or $\{r<r_0-\delta_0\}$ before a time $T$ is open, these sets
increase with $T$ and cover $K$, so finitely many do. From there the convergence is uniform by I.A Lemma 4.5 and the
monotonicity above.

(b) $\bar\Gamma_u$ is the union of $\Gamma$ and the two branches of $\{\phi_u = 0\}$, on each of which $r$ is monotone.
So $\bar\Gamma_u\cap O = \{\phi_u = 0\}\cap\Sigma^s\cap O = \Gamma_u$ for every $O\subset\{r>r_h\}$, and likewise for
$\bar\Gamma_s$. $\square$

**Lemma 5.2 (an escape function).** On $\Sigma^s$, $\mathcal F := (r^2-2\mu)\xi$ satisfies
$$H_{G^s}\mathcal F = \frac{2r\big(\xi^2(r^2-\mu)^2+(r^2-2\mu)^2\big)}{(r^2-\mu)^2}\ \ge0,\tag{5.1}$$
with equality exactly on $\Gamma$.

*Proof.* For $\mathcal F = a(r)\xi$, $H_{G^s}\mathcal F = 2\xi^2r^{-2}((r^2-\mu)a'-ra)+2r(r^2-2\mu)(r^2-\mu)^{-2}a$ on
$\Sigma^s$, after substituting $C$. At $a = r^2-2\mu$ the first bracket is $r^3$. (Sympy, `d313/dyn5.py`.) $\square$

Lemma 5.2 is not needed at $b_0$, where Proposition 5.1 uses the conserved $C$. Part VI.B uses it, as $C$ is not
conserved at $b\ne b_0$. Exactly, $\phi_2^2-\phi_1^2 = 4f\xi u$, so $\mathcal F = \frac{r^2}{4f}(\phi_2^2-\phi_1^2)$,
and with the choices of Proposition 3.1, $z_0\mathcal F = \frac{r^2}{4f}(\phi_s^2-\phi_u^2)$ for both signs of $z_0$,
while $\mathsf H^\flat(z_0\mathcal F) = H_{G^s}\mathcal F\ge0$.

## 6. The theorem

**Theorem 6.1 ((Dyn) at $b_0$).** For $g_{b_0}$ with III.B's $t_*$ and the radii of section 2: (H6) and (K1) hold (Lemma
1.1, for every $b\in\mathcal B$); the dynamical parts of (H3) and all of (H4) hold (Proposition 2.1); (Γ.1)-(Γ.3) hold
with $\nu_{\min} = 4(2\mu_0)^{-1/2}$ and $\beta_0 = \frac12\min_\Gamma|q_{z_0}| = f(r_{\mathrm{ph}})^{-1} = 2$
(Proposition 3.1, in $t_*$ by Lemma 0.1); (K3) holds (Proposition 4.1); (H8) holds (Proposition 5.1). These hold for
every operator with principal symbol $G\,\mathrm{Id}$.

## 7. Findings, labels and sources

(VI.A1) *The separatrices are exact.* The record's $\phi_{s/u} = \xi\pm\frac\nu{2f}(r-r_{\mathrm{ph}})$ (Proposition
10.16 (ii)) are the linearised eigenvectors. (Γ.1)-(Γ.2) ask exact invariant hypersurfaces, which are $f\xi = \pm(1-2\mu
r^{-2})$ (3.1), the two branches of $\{C = 4\mu\}$, with exact rates (3.2).

(VI.A2) *$\beta_0$ in two senses.* (H3)'s $\beta_0 = f'(r_h)$ is the surface gravity times 2, and (Γ.4)'s $\beta_0 =
\frac12\min_\Gamma|q|$ is the record's "$\beta_0 = 1/f(r_{\mathrm{ph}}) = 2$". They are different quantities with the
same letter in I.A and I.B.

(VI.A3) *The horizon's radial set is not radial.* At $b\ne b_0$ the Killing field normal to the horizon is not
$\partial_t$, and the flow on $N^*\mathcal H$ moves the base point. (H3) asks only an invariant source set with the
stated rates, which Part VI.B proves by perturbation. At $b_0$ the flow on $\partial\mathcal R_\pm$ is the fibre
dilation alone.

*Labels.* Proposition 2.1: [Hin26c] section 9.2.1 (1)-(4) for Tangherlini; Proposition 3.1: [Hin26c] (Γ.1)-(Γ.3), the
source's Lemma 4.16 for Kerr; Proposition 4.1: [Hin26c] Proposition 4.19; Proposition 5.1: [Hin26c] Proposition 4.24 and
the paragraph after (9.5).

*Sources.* No new reading. Inputs: III.B Propositions 3.4, 3.6, Lemmas 3.5, 3.7, (3.3), (3.6); I.A section 1.3 and Lemma
4.5; I.B sections 1.2-1.5 and Lemma 1.1; II.B section 1.1; N1STAR-PROOF.md Propositions 10.14 (ii) and 10.16 (ii), (iv).
