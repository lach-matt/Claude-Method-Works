# Part II.B. The null-bicharacteristic dynamics of the stationary model in e3b-phase space, at n = 4

*Status.* Proved (D326: verifier 142 read the D197 repairs, correct; one nit seated). Verified. Written out in full
(D196). Read line by line by the eighty-first verifier, which recomputed every flow and linearisation and confirmed
(B1)-(B4) at source; its one minor finding, that the statement of Lemma 3.3 (4) repeated the slip of the source which
its proof corrects, and four nits are seated (D197). The part is labelled proved once the next reader has confirmed
them; verifier 142 did (D326), and verifier 143 confirmed the D326 nit (D327). This part proves, at spatial dimension $n
= 4$, the content of [Hin26c] section 4 (pp. 77-99) that the later parts use: the radial sets, the horizon, the trapped
set and the global null-bicharacteristic dynamics of the stationary model in e3b-phase space over the domain $\Omega$ of
Part II.A. The source works on subextremal Kerr. Here the stationary model is any metric satisfying the hypotheses of
Part I together with (K1)-(K4) of section 1. Part I.A (`PART-I-SPECTRAL.md`) is cited as I.A, Part I.B
(`PART-I-B-HIGHENERGY.md`) as I.B, Part II.A (`PART-II-A-SETUP.md`) as II.A.

*Method.* The source computes the Kerr dynamics from the explicit metric: Carter's constant, the potential of the
radial motion, the expansion rates, and Dyatlov's proof of $r$-normal hyperbolicity. At $n = 4$ there is no explicit
metric to compute from. The dynamics the later parts need is instead read off from the stationary spectral theory of
Part I, whose hypotheses (H3), (H4), (H7), (H8) describe the flow at each frequency. The link is section 2: over the
interior of the Kerr face the 3b-phase space is the stationary phase space with the frequency $\sigma$ as a conserved
variable, and the map $\Phi_{z_0}$ identifies the semiclassical phase space $\mathcal P$ of I.B at frequency sign $z_0$
with the part of the 3b-cosphere bundle over $K^+$ where $z_0\sigma\ge0$, flows included. Near $\iota^+$, $\mathscr I^+$
and the corner $\partial K^+$ the metric is Minkowski to second order (K1), and there the flows are solved in closed form
(sections 3 and 7). $r$-normal hyperbolicity of the trapped set is the hypothesis (K3), to be checked for the record's
metrics in Part VI with the rest of the dynamical hypotheses.

*How it is organised.* Section 1: the stationary model and the hypotheses (K1)-(K4). Section 2: the Kerr face and the
stationary phase space. Section 3: the 3b-dynamics near $\partial K^+$ and over $\iota^+$. Section 4: the horizon.
Section 5: the trapped set. Section 6: the dynamics over the Kerr face. Section 7: the eb-dynamics near $\mathscr I^+$.
Section 8: the global dynamics in e3b-phase space. Section 9: findings.

## 1. The stationary model

### 1.1 The metric and the hypotheses

Let $\hat P$, $E$, $\tilde X$ and $g$ be as in I.A section 1 and I.B section 1.2, satisfying (H1)-(H8). Thus $g$ is a
Lorentzian metric of signature $(1,4)$ on $\mathbb R_{t_*}\times\tilde X^\circ$, $\tilde X^\circ = \{r>r_0-2\delta_0\}$,
with $t_*$-independent components, $dt_*$ is past timelike, and $G(\zeta) := g^{-1}(\zeta,\zeta)$ satisfies
$G(-\sigma\,dt_*+\zeta) = G_0(\zeta)+\sigma\tau_1(\zeta)+\sigma^2g_{00}$ for $\zeta\in T^*\tilde X^\circ$ (I.B (1.1)).
The time function of Part I is written $t_*$ here. Points $(t_*,x)$ are identified with points of $\mathbb R^{1+4}$ by $t
:= t_*+r$, as in [Hin26c] p. 80, so that $t_* = t-r$ is the function $t_*$ of II.A section 1 and $g$ becomes a metric on
$\tilde M^\circ\cap\{r>r_0-2\delta_0\}$. $\bar g := -dt^2+dx^2 = -dt_*^2-2\,dt_*\,dr+r^2\slashed g$ is the Minkowski
metric, $\slashed g$ the round metric on $\mathbb S^3$. The further hypotheses are these.

(K1) (*Decay.*) There is $R>r_2$ such that on $\{r>R\}$ the components of $g-\bar g$ in the frame $dt_*,dx^1,\dots,dx^4$
lie in $\rho^2C^\infty(\bar X)$, $\rho = r^{-1}$.

(K2) (*Part I.*) (H1)-(H8) hold for the spectral family $\hat P$ of an operator whose principal symbol is $G$ (I.B
section 1.2).

(K3) (*$r$-normal hyperbolicity.*) Let $\Gamma = \Gamma_1\subset\Sigma^\flat_1$ be the trapped set of (H7) for $z_0 = 1$,
$q_1 = 2g^{-1}(-dt_*+\zeta,dt_*)$ as in I.B Lemma 1.1, and $\mathsf V := q_1^{-1}H_{G_1}$ on $\Sigma^\flat_1$ near
$\Gamma$, where $G_1(\zeta) = G(-dt_*+\zeta)$. Then $\Gamma$ is eventually absolutely $r$-normally hyperbolic for every
$r$ for the flow of $\mathsf V$ within $\Sigma^\flat_1$ ([HPS77] Definition 4): there is a continuous splitting
$$T_\Gamma\Sigma^\flat_1 = T\Gamma\oplus\bar N^u\oplus\bar N^s\tag{1.1}$$
preserved by $De^{s\mathsf V}$ for all $s\in\mathbb R$, and constants $\mu,C>0$ and, for every $\epsilon>0$,
$C_\epsilon$, with $|De^{s\mathsf V}v|\le Ce^{-\mu|s|}|v|$ for $v\in\bar N^u$, $s\le0$, and for $v\in\bar N^s$, $s\ge0$,
and $|De^{s\mathsf V}v|\le C_\epsilon e^{\epsilon|s|}|v|$ for $v\in T\Gamma$, $s\in\mathbb R$. Here $|\cdot|$ is any
fixed fibre metric.

(K4) (*Parameters.*) When $\hat P$ depends on $b\in\mathcal B$ as in (H5), so does $g$, and $\rho^{-2}(g-\bar g)$ is
bounded in $C^\infty(\bar X\cap\{r\ge R\})$ uniformly and continuously in $b$; the splitting (1.1) depends continuously
on $b$, and $\mu$, $C$, $C_\epsilon$ are uniform.

*Remarks.* (a) (K1) is [Hin26c] (4.4) and Lemma 4.4 at $n = 4$, with the rate $r^{-2}$ that the mass term $\mu r^{-2}$
of a five-dimensional metric gives; Kerr has $r^{-1}$. For five-dimensional Schwarzschild-Tangherlini with
$t_* = t-T(r)$, $T' = (1+\tilde T)(1-\mu r^{-2})^{-1}$ and $\tilde T$ vanishing quadratically at $r^{-1} = 0$, the
components of $g-\bar g$ are $\mu r^{-2}$ (in $dt_*^2$), $-2\tilde T$ (in $dt_*\,dr$) and $-(2+\tilde T)\tilde T(1-\mu
r^{-2})^{-1}$ (in $dr^2$), all in $\rho^2C^\infty$. Unlike four dimensions, no logarithm enters $T$. (b) (K3) is
[Hin26c] Proposition 4.19, which the source proves for Kerr from Carter's integrability. The splitting and the normal
rates follow from (H7) as in the source's proof of its parts (1)-(2); the tangential bound is the substance of the
hypothesis. Both are checked for the record's metrics in Part VI. (c) (K4) is [Hin26c] Remark 4.25.

### 1.2 The metric on the compactifications

**Lemma 1.1 ([Hin26c] Lemma 4.4 at $n = 4$).** $dt_*$ is everywhere past timelike. Moreover:

(1) $g\in C^\infty(M;S^2\mathcal T^*)$ is non-degenerate on $M\cap\{r>r_0-2\delta_0\}$, and $g-\bar g\in
r^{-2}C^\infty(M;S^2\mathcal T^*)$ near $\partial M$, where $\mathcal T$ is the pullback of the scattering tangent bundle
(II.A section 2.1).

(2) $g\in\rho_{\mathrm{sf}}^{-2}C^\infty(M_0;S^2\,{}^{3b}T^*M_0)$ is non-degenerate, and $\rho_{\mathrm{sf}}^2(g-\bar g)
\in\rho_{\mathrm{sf}}^2C^\infty(M_0;S^2\,{}^{3b}T^*M_0)$.

(3) $g\in\rho_0^{-2}x_I^{-2}\rho_+^{-2}C^\infty(M;S^2\,{}^{e3b}T^*M)$ is non-degenerate, and
$$\rho_0^2x_I^2\rho_+^2(g-\bar g)\in\rho_0^2x_I^2\rho_+^2C^\infty(M;S^2\,{}^{e3b}T^*M).\tag{1.2}$$
The same holds for the inverses: $g^{-1}-\bar g^{-1}\in r^{-2}C^\infty(M;S^2\mathcal T)$, and
$\rho_0^{-2}x_I^{-2}\rho_+^{-2}(g^{-1}-\bar g^{-1})\in\rho_0^2x_I^2\rho_+^2C^\infty(M;S^2\,{}^{e3b}TM)$.

*Proof.* $dt_*$ is past timelike by (H6) (I.B section 1.2). (1) The components of $g$ in the frame $dt_*,dx$ are
$t_*$-independent and, by (K1), smooth functions on $\bar X$; by II.A Lemma 2.10 a $t_*$-independent function that is
smooth on $\bar X$ is smooth on $M_1$, and the blow-down $M\to M_1$ is smooth. $dt_* = dt-dr$, $dr = \omega\cdot dx$ and
$dx$ are smooth sections of $\mathcal T^*$ (with $\omega = x/|x|$ smooth on $\bar X$ near $\partial X$). This gives (1),
and on $\{r\le R\}$ there is nothing to prove, $r^{-2}$ being bounded there. (2) By II.A Definition 2.1, ${}^{3b}TM_0$ is
spanned by $r\partial_t$, $r\partial_x$ over $M_0$, so $\mathcal T^* = r\,{}^{3b}T^*M_0$ and $C^\infty(M_0;S^2\mathcal
T^*) = r^2C^\infty(M_0;S^2\,{}^{3b}T^*M_0)$ near sf. Hence $g-\bar g\in C^\infty(M_0;S^2\,{}^{3b} T^*M_0)$, and $r^{-1}$
is a defining function of sf. Non-degeneracy: $\rho_{\mathrm{sf}}^2\bar g$ is non-degenerate (II.A section 2.2) and the
perturbation vanishes at sf; over $M_0^\circ$, $g$ is Lorentzian. (3) Near $K^+$ away from $\mathscr I^+$, this is (2),
$\rho_+$ and $\rho_{\mathrm{sf}}$ being comparable there and $x_I$, $\rho_0$ positive. Near $\mathscr I^+$, II.A Lemma
2.5 shows that $C^\infty(M;S^2\mathcal T^*)$, spanned by $dt_*^2$, $dt_*\,dr$, $dr^2$, $dt_*\,r\,d\omega$,
$dr\,r\,d\omega$ and $r\,d\omega\,r\,d\omega$, lies in $\rho_0^{-2}x_I^{-4}\rho_+^{-2} C^\infty(M;S^2\,{}^{e3b}T^*M)$,
the worst term being $dr^2 = x_I^{-2}\cdot x_I^2dr^2$. Near $\mathscr I^+\cap\iota^+$, $r = \rho_+^{-1}x_I^{-2}$, and
near $\mathscr I^+\cap I^0$, $r = \rho_0^{-1}x_I^{-2}$ (II.A section 1). So $r^{-2}\in \rho_0^2x_I^4\rho_+^2C^\infty$
near $\mathscr I^+$, and $g-\bar g\in C^\infty(M;S^2\,{}^{e3b}T^*M)$ there, which is (1.2). Non-degeneracy as in (2),
with $\rho_0^2x_I^2\rho_+^2\bar g$ non-degenerate (II.A Definition 2.8). The inverses: $\bar g$ has constant components
in the frame $dt,dx$, so $g^{-1} = \bar g^{-1}-\bar g^{-1}h\bar g^{-1}+\dots$, $h := g-\bar g$, converges for $r$ large,
and its terms after the first lie in $r^{-2}C^\infty(M;S^2\mathcal T)$. In e3b-terms, $\mathcal T\subset\rho_+{}^{e3b}TM$
near $\mathscr I^+\cap\iota^+$ by $\partial_{t_*} = \rho_+(-\rho_+\partial_{\rho_+}+ \frac12x_I\partial_{x_I})$,
$\partial_r = -\frac12\rho_+x_I^2\,x_I\partial_{x_I}$ and $r^{-1}\partial_\omega = \rho_+x_I\cdot x_I\partial_\omega$
(II.A section 2.3), and likewise with $\rho_0$ near $\mathscr I^+\cap I^0$; so $g^{-1}-\bar g^{-1}\in
r^{-2}\rho_0^2\rho_+^2C^\infty(S^2\,{}^{e3b}TM) = \rho_0^4x_I^4\rho_+^4C^\infty$ near $\mathscr I^+$, and near $K^+$ the
same follows from (2). $\square$

The improvement over [Hin26c] (4.9), where the factor on the right of (1.2) is $\rho_0x_I^2\rho_+$, is the rate $r^{-2}$
of (K1). Nothing below needs more than the source's rate, except that errors vanish to second order at $\iota^+$ and
$\partial K^+$, which shortens two proofs.

### 1.3 Characteristic sets

Following [Hin26c] (4.11), put $g^{-1}_{e3b} := \rho_0^{-2}x_I^{-2}\rho_+^{-2}g^{-1}$ and
$$\Sigma := \{\zeta\in{}^{e3b}T^*M\setminus o: g^{-1}_{e3b}(\zeta,\zeta) = 0\} = \Sigma^+\sqcup\Sigma^-,\tag{1.3}$$
where $\zeta\in\Sigma^+\cap T^*M^\circ$ if and only if $g^{-1}(\zeta,\cdot)$ is a future directed null vector; $\Sigma^-
= -\Sigma^+$, and $\Sigma^\pm$ are the closures in ${}^{e3b}T^*M\setminus o$. $\partial\Sigma^\pm\subset{}^{e3b}S^*M$ are
their boundaries at fibre infinity. Fix defining functions $\rho_\infty$ of ${}^{e3b}S^*M$ and $x_I$, $\rho_+$ of
$\mathscr I^+$, $\iota^+$, and put, as in [Hin26c] (4.71),
$$\mathsf H_G := \rho_\infty x_I^{-2}\rho_+^{-2}H_G,\tag{1.4}$$
an e3b-vector field on ${}^{e3b}T^*_\Omega M$ tangent to ${}^{e3b}S^*M$; on $\Sigma$ it equals $\rho_\infty
H_{x_I^{-2}\rho_+^{-2}G}$. Near $K^+$ it is a positive smooth multiple of the rescaled 3b-fields of sections 2-6, and
near $\mathscr I^+$ of the eb-field of section 7, on $\Sigma$: positive multiples of a vector field have the same
integral curves up to an increasing reparametrisation, and all statements below are invariant under that.

**Lemma 1.2 (future covectors).** (a) For every $\zeta\in\Sigma^+\cap T^*M^\circ$, $H_Gt_*>0$. (b) There is $R_1\ge R$
such that $\partial_{t_*}$ is future directed timelike on $\{r\ge R_1\}$; there, every $-\sigma\,dt_*+\zeta\in\Sigma^+$
has $\sigma>0$. (c) For a null covector $\nu = -\sigma\,dt_*+\zeta$ over $\tilde X^\circ$, $\nu\in\Sigma^+$ if and only
if $g^{-1}(\nu,dt_*)>0$.

*Proof.* (c) $-\nabla t_*$ is future directed timelike (I.B section 1.2), and a future directed null vector has negative
inner product with it, so $\nu^\sharp$ is future directed if and only if $g(\nu^\sharp,-\nabla t_*)<0$, that is
$g^{-1}(\nu,dt_*)>0$. (a) $H_Gt_* = 2g^{-1}(\nu,dt_*)$ at $\nu$; use (c). (b) By (K1), $g(\partial_{t_*},\partial_{t_*})
= -1+O(r^{-2})$, so $\partial_{t_*}$ is timelike for $r$ large; it is future directed since $g(\partial_{t_*},-\nabla
t_*) = -dt_*(\partial_{t_*}) = -1$. For $\nu\in\Sigma^+$ there, $\nu(\partial_{t_*}) = g(\nu^\sharp,\partial_{t_*})<0$,
and $\nu(\partial_{t_*}) = -\sigma$. $\square$

By (c), in the notation of I.B Lemma 1.1, $\Sigma^+\cap\{\sigma = z_0\}$ is the component $\Sigma^+_{z_0} = \Sigma_{z_0}
\cap\{q_{z_0}>0\}$, on which the future field is $+H_{G_{z_0}}$ (I.B section 1.3), and the future component of the
characteristic set at fibre infinity of $T^*\tilde X^\circ$ is $\partial\Sigma_0^+$, the one containing $\partial\mathcal
R_+$, with future field $+\rho_\infty H_{G_0}$ ((H3), I.B Lemma 1.1 (e)).

## 2. The Kerr face and the stationary phase space

### 2.1 The 3b-phase space over $K^+$

Over $M_0\cap\{r>r_0-2\delta_0\}$ write 3b-covectors as $-\sigma\,dt_*+\zeta$, $\zeta\in T^*\tilde X^\circ$; by II.A
Definition 2.1 the 3b-fibre coordinates are $r(-\sigma,\zeta)$ in the frame dual to $r\partial_{t_*}$, $r\partial_x$, so
$(\sigma,\zeta)$ are fibre coordinates up to the positive factor $r$, smooth over $M_0^\circ$. Near $(K^+)^\circ$, with
$\rho_K := t_*^{-1}$, the 3b-vector fields are spanned by $\partial_{t_*} = -\rho_K^2\partial_{\rho_K}$ and $\partial_x$
(II.A section 2.2; [Hin26c] section 6.1).

**Lemma 2.1 (the field over $K^+$).** The Hamilton vector field $H_G$ on ${}^{3b}T^*M_0$ over $\{r>r_0-2\delta_0\}$ is
tangent to ${}^{3b}T^*_{K^+}M_0$, annihilates $\sigma$, and its restriction to ${}^{3b}T^*_{(K^+)^\circ}M_0 = \mathbb
R_\sigma\times T^*\tilde X^\circ$ is, at each fixed $\sigma$, the Hamilton vector field of $\zeta\mapsto G(-\sigma\,dt_*
+\zeta)$ on $T^*\tilde X^\circ$.

*Proof.* In canonical coordinates $(t_*,x;\tau,\zeta)$, $\tau = -\sigma$, $H_G = (\partial_\tau
G)\partial_{t_*}+(\partial _\zeta G)\partial_x-(\partial_{t_*}G)\partial_\tau-(\partial_xG)\partial_\zeta$. $G$ is
$t_*$-independent, so the $\partial_\tau$-component vanishes and $H_G\sigma = 0$, and $\partial_{t_*} =
-\rho_K^2\partial_{\rho_K}$ vanishes at $\rho_K = 0$. The remaining components are those of the Hamilton field of
$G(\tau,\cdot)$ on $T^*\tilde X^\circ$ at fixed $\tau$. $\square$

### 2.2 The identification

The 3b-cosphere bundle over $K^+$ is ${}^{3b}S^*_{K^+}M_0 = K^+\times\mathbb S^4$: II.A Definition 2.1 trivialises
${}^{3b}TM_0$ globally, and $K^+\cong\overline{\mathbb R^4}$ (II.A Lemma 2.10), with boundary $\partial K^+ = K^+\cap
\iota^+$, defined within $K^+$ by $\rho_+ = r^{-1}$. In the trivialisation, the class of $-\sigma\,dt_*+\zeta$ is
$[\sigma:\zeta]$ (homogeneous coordinates, up to positive multiples), since the trivialisation differs from
$(\sigma,\zeta)$ by the positive factor $r$ and the smooth fibre-linear map from $dt$ to $dt_*$ ($dt = dt_*+\omega\cdot
dx$, smooth on $\bar X$). Recall $\mathcal P = \overline{\mathbb R^4}\times\overline{\mathbb R^4}$ (I.B section 2.4),
with fibre infinity $\overline{\mathbb R^4}\times\partial\overline{\mathbb R^4}$ and the face over $\partial X$.

**Definition 2.2.** For $z_0\in\{1,-1\}$, $\Phi_{z_0}:\mathcal P\to{}^{3b}S^*_{K^+}M_0$ is $\Phi_{z_0}(x,\zeta) :=
(x,[z_0:\zeta])$, the class of the covector $-z_0\,dt_*+\zeta$, extended to fibre infinity by $\Phi_{z_0}(x,\theta\infty)
:= (x,[0:\theta])$.

**Lemma 2.3.** (a) $\Phi_{z_0}$ is a diffeomorphism of manifolds with corners onto
$K^+\times\{[\sigma:\zeta]:z_0\sigma\ge 0\}$, mapping fibre infinity onto $\{\sigma = 0\}$ and the face over $\partial X$
onto the part over $\partial K^+$.

(b) Put $G_{3b} := r^2G$, which near sf is a smooth fibre-quadratic function on ${}^{3b}T^*M_0$ (Lemma 1.1 (2)), and let
$\tilde\rho_\infty := r^{-1}(\sigma^2+|\zeta|^2)^{-1/2}$, a defining function of 3b-fibre infinity over $K^+$. Then
$\tilde\rho_\infty^2G_{3b}\circ\Phi_{z_0} = a\,\hat G_{z_0}$ with $a$ smooth and positive on $\mathcal P$, $\hat G_{z_0}
= \rho_\infty^2G_{z_0}$ as in I.B Lemma 4.1. So $\Phi_{z_0}$ maps $\Sigma_{z_0}\subset\mathcal P$ onto the characteristic
set of $G_{3b}$ in $K^+\times\{z_0\sigma\ge0\}$.

(c) On $\Sigma_{z_0}$, $(\Phi_{z_0})_*\mathsf H_{z_0} = a'\,\tilde\rho_\infty H_{G_{3b}}$ with $a'$ smooth and positive,
where $\mathsf H_{z_0} = \mu^{-1}H_{G_{z_0}}$ is the field of I.B (4.1).

(d) $\Phi_{z_0}$ maps $\Sigma^+_{z_0}\cap T^*\tilde X^\circ$ onto
$\Sigma^+\cap{}^{3b}T^*_{(K^+)^\circ}\cap\{z_0\sigma>0\}$ (classes), and $\partial\Sigma_0^+$ onto $\Sigma^+\cap\{\sigma
= 0\}$ at fibre infinity. Over $\partial K^+$, $\Sigma^+$ lies in $\{\sigma>0\}$, and $\Phi_1$ maps $\Sigma_1\cap\{\rho =
0\}$, the characteristic set of I.A (4.7) at $\sigma_0 = 1$, onto it. $\Sigma^+\cap\{\sigma\le0\}$ lies over $\{r<R_1\}$.

*Proof.* (a) $\overline{\mathbb R^4}_\zeta$ is diffeomorphic to the closed hemisphere $\{z_0\sigma\ge0\}\subset\mathbb
S^4$ by $\zeta\mapsto[z_0:\zeta]$: this is the standard model of the radial compactification, whose boundary $\{|\zeta| =
\infty\}$ goes to the equator $\{\sigma = 0\}$, smoothly with smooth inverse ($[z_0:\zeta] =
[z_0|\zeta|^{-1}:\zeta/|\zeta|]$ near the equator, and $|\zeta|^{-1}$ is a boundary defining function of
$\overline{\mathbb R^4}$). In the base it is the identity of $\bar X\cong K^+$, which maps $\partial X$ to $\partial
K^+$. (b) $G_{3b}(-z_0\,dt_*+\zeta) = r^2G_{z_0}(x,\zeta)$ and $\tilde\rho_\infty = r^{-1}\langle\zeta\rangle^{-1}$ at
$\sigma = \pm1$, so $\tilde\rho_\infty^2G_{3b} = \langle \zeta\rangle^{-2}G_{z_0} = \hat G_{z_0}$ with the choice
$\rho_\infty = \langle\zeta\rangle^{-1}$ of I.B; for another choice of $\rho_\infty$ the quotient is smooth and positive.
Both sides are homogeneous of degree 0 in $(\sigma,\zeta)$, so the identity extends to fibre infinity and to the face
over $\partial X$ by continuity. (c) By the Leibniz rule, $H_{G_{3b}} = r^2H_G+GH_{r^2}$, and on the characteristic set
$G = 0$, so $H_{G_{3b}} = r^2H_G$ there. $H_G$ at a covector with $\sigma = z_0$ is tangent to $\{\sigma = z_0\}$ and, in
the coordinates $(x,\zeta)$ there, is $H_{G_{z_0}}$ (Lemma 2.1); and $\Phi_{z_0}$ restricted to $\{\sigma = z_0\}$ is the
projection to the cosphere bundle. Since $H_G$ is homogeneous of degree 1 in the fibre, $\tilde\rho_\infty H_{G_{3b}}$
descends to the cosphere bundle, and at points of $\Phi_{z_0}(\Sigma_{z_0} \cap T^*\tilde X^\circ)$
$$\tilde\rho_\infty H_{G_{3b}} = r^{-1}\langle\zeta\rangle^{-1}r^2H_{G_{z_0}} = r\langle\zeta\rangle^{-1}\mu\,\mathsf
H_{z_0}.$$
With $\mu = \langle\zeta\rangle\langle x\rangle^{-1}$ (I.B Lemma 4.1 (c): $H_p\in\mu\,\rho_\infty^{2-k}\mathcal V_b$ for
order $(k,0)$), $a' = \langle x\rangle r^{-1}$, smooth and positive on $\mathcal P$. The identity extends by continuity
to the faces of $\mathcal P$, both sides being smooth vector fields there (I.B Lemma 4.1 (c); Lemma 1.1 (2)). (d) The
first two statements are Lemma 1.2 (c) and the paragraph after it, with (H3) at fibre infinity. Over $\partial K^+$,
$\rho_+ = 0$ and $G_{3b}$ is the Minkowski function $\bar G_{3b} = -2\sigma_{3b}\xi_{3b}+\xi_{3b}^2+|\eta_{3b}|^2$ of
section 3, on whose characteristic set $\sigma_{3b}<0$ on $\Sigma^+$ ([Hin26c] p. 81: $dt_*$ is past causal for $\bar
g$), with $\sigma_{3b} = -r\sigma$ (section 3), so $\sigma>0$. The last statement is Lemma 1.2 (b). $\square$

Hence the future 3b-flow over $K^+$ splits into three invariant pieces: $\{\sigma>0\}$, the image under $\Phi_1$ of the
future component $\Sigma^\flat_1 = \Sigma^+_1$ of I.B with its face over $\partial X$; $\{\sigma = 0\}$, the image of
$\partial\Sigma_0^+$ at fibre infinity; and $\{\sigma<0\}$, the image under $\Phi_{-1}$ of $\Sigma^+_{-1}$, which lies
over $\{r<R_1\}$. On each, the rescaled future 3b-field is a positive multiple of the future field of Part I: $+\mathsf
H_1$, $+\rho_\infty H_{G_0}$, resp. $+\mathsf H_{-1}$ (Lemma 2.3 (c), Lemma 1.2 and the paragraph after it).

## 3. The 3b-dynamics near $\partial K^+$ and over $\iota^+$

### 3.1 The Minkowski model

Near $K^+\cap\iota^+$ use $\rho_K := r/t_*$, $\rho_+ := r^{-1}$, $\omega$. (In sections 2 and 4, $\rho_K$ is $t_*^{-1}$,
a defining function of $K^+$ away from $\iota^+$, and in sections 7 and 8, $\rho_+$ is $t_*^{-1}$, a defining function of
$\iota^+$ near $\mathscr I^+$; the two meanings of each meet only over $\iota^+$, where both vanish; D197.) Write
3b-covectors as
$$\zeta = \sigma_{3b}\frac{dt_*}r+\xi_{3b}\frac{dr}r+\eta_{3b},\qquad\eta_{3b}\in T^*\mathbb S^3,\tag{3.1}$$
so that $-\sigma\,dt_*+\xi\,dr+\eta$ has $\sigma_{3b} = -r\sigma$, $\xi_{3b} = r\xi$, $\eta_{3b} = \eta$. In the
scattering coordinates $\xi\,dr+r\eta_{\mathrm{sc}}$ of I.A section 1.4, $\eta_{\mathrm{sc}} = r^{-1}\eta$. The
Minkowski function is
$$\bar G_{3b} := r^2\bar g^{-1}(\zeta,\zeta) = -2\sigma_{3b}\xi_{3b}+\xi_{3b}^2+|\eta_{3b}|^2\tag{3.2}$$
([Hin26c] (4.13), with $|\cdot|$ the round norm on $\mathbb S^3$; from $\bar g^{-1} =
-2\partial_{t_*}\otimes_s\partial_r+ \partial_r^2+r^{-2}\slashed g^{-1}$). By Lemma 1.1 (the inverses) and $\mathcal T =
r^{-1}\,{}^{3b}TM_0$, $g^{-1}-\bar g^{-1}\in r^{-4}C^\infty(S^2\,{}^{3b}TM_0)$, so $G_{3b}-\bar
G_{3b}\in\rho_+^2P^{[2]}({}^{3b}T^*M_0)$ near $K^+\cap\iota^+$, $P^{[2]}$ the fibrewise quadratic polynomials with smooth
coefficients. By II.A (2.1), with $r\partial_{t_*} = -\rho_K^2\partial_{\rho_K}$ and $r\partial_r =
\rho_K\partial_{\rho_K}-\rho_+\partial_{\rho_+}$,
$$H_{\bar G_{3b}} = 2(\xi_{3b}-\sigma_{3b})(\rho_K\partial_{\rho_K}-\rho_+\partial_{\rho_+}+\sigma_{3b}
\partial_{\sigma_{3b}})+2\sigma_{3b}\xi_{3b}\partial_{\xi_{3b}}+2\xi_{3b}\rho_K^2\partial_{\rho_K}+H_{|\eta_{3b}|^2}.$$
The error $H_{G_{3b}-\bar G_{3b}}$ lies in $\rho_+^2\mathcal V_b({}^{3b}T^*M_0)$: for $p = \rho_+^2q$, $H_p =
\rho_+^2H_q+ 2q\rho_+H_{\rho_+}$, and $H_{\rho_+} = -((r\partial_r)\rho_+)\partial_{\xi_{3b}} =
\rho_+\partial_{\xi_{3b}}$ by (2.1). (The source has $\rho_+$ in place of $\rho_+^2$.)

$\bar G_{3b} = (\xi_{3b}-\sigma_{3b})^2+|\eta_{3b}|^2-\sigma_{3b}^2$, so $\sigma_{3b}\ne0$ on $\Sigma$ over $\iota^+$,
and $\sigma_{3b}<0$ on $\Sigma^+$ there ([Hin26c] p. 81). Near $\partial\Sigma^+$ over a neighbourhood of $\iota^+$ use
$$\rho_\infty := -\sigma_{3b}^{-1},\qquad\hat\xi := \xi_{3b}/\sigma_{3b},\qquad\hat\eta := \eta_{3b}/\sigma_{3b}.
\tag{3.3}$$
Then $\rho_\infty^2\bar G_{3b} = \hat\xi^2-2\hat\xi+|\hat\eta|^2$, and $\bar{\mathsf H} := \rho_\infty H_{\bar G_{3b}}$
satisfies, exactly,
$$\begin{gathered}\bar{\mathsf H}\rho_K = 2(1-\hat\xi)\rho_K-2\hat\xi\rho_K^2,\quad\bar{\mathsf H}\rho_+ = -2(1-\hat\xi)
\rho_+,\quad\bar{\mathsf H}\rho_\infty = -2(1-\hat\xi)\rho_\infty,\\ \bar{\mathsf H}\hat\xi = -2(2-\hat\xi)\hat\xi,\quad
\bar{\mathsf H}\hat\eta = -2(1-\hat\xi)\hat\eta+\partial_\omega|\hat\eta|^2,\quad\bar{\mathsf H}\omega =
-\partial_{\hat\eta}|\hat\eta|^2,\end{gathered}\tag{3.4}$$
which is [Hin26c] (4.15). For instance $H_{\bar G_{3b}}\xi_{3b} = 2\sigma_{3b}\xi_{3b}$ and $H_{\bar G_{3b}}\sigma_{3b} =
2(\xi_{3b}-\sigma_{3b})\sigma_{3b}$ give $H_{\bar G_{3b}}\hat\xi = 2\sigma_{3b}\hat\xi(2-\hat\xi)$, and $\rho_\infty =
-\sigma_{3b}^{-1}$. The full rescaled field $\mathsf H := \rho_\infty H_{G_{3b}}$ is $\bar{\mathsf H}+\tilde{\mathsf H}$,
$\tilde{\mathsf H}\in\rho_+^2\mathcal V_b$, tangent to ${}^{3b}S^*M_0$ and to the boundary faces. In particular
$\tilde{\mathsf H}\rho_+\in\rho_+^3C^\infty$, $\tilde{\mathsf H}\rho_K\in\rho_+^2\rho_KC^\infty$, and over
$\iota^+$ the flow of $\mathsf H$ is that of $\bar{\mathsf H}$. All of this is dimension-free.

**Definition 3.1 ([Hin26c] Definition 4.5).** $\partial R_{\partial K^+,\mathrm{in}} := \{\rho_K = \rho_+ = 0,\ \hat\xi =
2,\ \hat\eta = 0\}$ and $\partial R_{\partial K^+,\mathrm{out}} := \{\rho_K = \rho_+ = 0,\ \hat\xi = 0,\ \hat\eta = 0\}$,
subsets of $\partial\Sigma^+$ over $\partial K^+$; their conic extensions are $\{\xi_{3b} = 2\sigma_{3b}<0,\eta_{3b} =
0\}$ and $\{\xi_{3b} = 0,\sigma_{3b}<0,\eta_{3b} = 0\}$ over $\partial K^+$.

Under $\Phi_1$ these are $R_{1,\mathrm{in}}$ and $R_{\mathrm{out}}$ of I.A (4.6) at $\sigma_0 = 1$: there $\xi =
-2\sigma_0$, $\eta = 0$, resp. $\xi = 0$, $\eta = 0$, and $\hat\xi = \xi_{3b}/\sigma_{3b} = -\xi/\sigma$.

*Linearisation* ([Hin26c] (4.16)). $\mathsf H$ vanishes on both sets. On $\partial\Sigma^+$, $\hat\xi$ is near each a
smooth function of $(\rho_K,\rho_+,\hat\eta)$, and by (3.4) and the error bounds, the linearisation of $\mathsf H$ on the
conormal spaces is $d\rho_K\mapsto-2d\rho_K$, $d\rho_+\mapsto2d\rho_+$, $d\hat\eta\mapsto2d\hat\eta$ at
$\partial R_{\partial K^+,\mathrm{in}}$, and $d\rho_K\mapsto2d\rho_K$, $d\rho_+\mapsto-2d\rho_+$,
$d\hat\eta\mapsto-2d\hat\eta$ at $\partial R_{\partial K^+,\mathrm{out}}$ (the term $\partial_\omega|\hat\eta|^2$ is
quadratic in $\hat\eta$, and $\tilde{\mathsf H}$ vanishes to second order at $\rho_+ = 0$). Also $\rho_\infty^{-1}\mathsf
H\rho_\infty = 2$, resp. $-2$, there.

### 3.2 The flow over $\iota^+$ and over $\partial K^+$ in closed form

**Lemma 3.2.** (a) (*Over $\partial K^+$.*) On $\partial\Sigma^+$ over $\partial K^+$, $\hat\xi\in[0,2]$, and every
maximal integral curve of $\mathsf H$ not contained in $\partial R_{\partial K^+,\mathrm{in}}\cup\partial
R_{\partial K^+,\mathrm{out}}$ is, after a shift of the parameter, $\hat\xi(s) = 2/(1+e^{4s})$, defined for all $s$,
tending to $\partial R_{\partial K^+,\mathrm{in}}$ as $s\to-\infty$ and to $\partial R_{\partial K^+,\mathrm{out}}$ as
$s\to\infty$.

(b) (*Over $\iota^+$.*) On $\partial\Sigma^+$ over $(\iota^+)^\circ$, use $u := t_*/r = \rho_K^{-1}\in(0,\infty)$. Along
a maximal integral curve of $\mathsf H$,
$$\hat\xi' = -2(2-\hat\xi)\hat\xi,\qquad u' = -2(1-\hat\xi)u+2\hat\xi,\qquad|\hat\eta|^2 = \hat\xi(2-\hat\xi).
\tag{3.5}$$
Exactly one of the following holds. (i) $\hat\xi\equiv0$, $\hat\eta\equiv0$, $u = u_0e^{-2s}$: the curve lies in
$\partial W_{\mathrm{out}} := \{\rho_+ = 0,\hat\xi = 0,\hat\eta = 0\}$, tends to $\partial R_{\partial K^+,\mathrm{out}}$
($u\to\infty$) as $s\to-\infty$ and to $\mathscr I^+$ ($u\to0$) as $s\to\infty$. (ii) $\hat\xi\equiv2$,
$\hat\eta\equiv0$, $u = Ae^{2s}-2$, $A>0$, $s>\frac12\log(2/A)$: the curve lies in $\partial W_{\mathrm{in}} := \{\rho_+
= 0,\hat\xi = 2, \hat\eta = 0\}$, tends to $\partial R_{\partial K^+,\mathrm{in}}$ as $s\to\infty$, and reaches $u = 0$
as $s$ decreases to $\frac12\log(2/A)$. (iii) After a shift of the parameter, $\hat\xi = 2/(1+e^{4s})$ and
$$u = \frac{C-e^{-2s}}{\cosh2s},\qquad C>0,\qquad s>-\tfrac12\log C;\tag{3.6}$$
$u\to0$ both as $s\downarrow-\frac12\log C$ and as $s\to\infty$, and $u$ has one interior maximum.

(c) The angular coordinates converge at each end of each curve in (a) and (b).

*Proof.* Over $\iota^+$, $\mathsf H = \bar{\mathsf H}$ and $\rho_\infty^2G_{3b} = \hat\xi^2-2\hat\xi+|\hat\eta|^2$ there,
so on $\partial\Sigma^+$, $|\hat\eta|^2 = \hat\xi(2-\hat\xi)$ and $\hat\xi\in[0,2]$. (3.5) is (3.4) with $u =
\rho_K^{-1}$: $u' = -\rho_K^{-2}\rho_K' = -2(1-\hat\xi)u+2\hat\xi$. The logistic equation for $\hat\xi$ has the constant
solutions $0$, $2$ and, on $(0,2)$, the solutions $2/(1+e^{4(s-s_1)})$. (a) Over $\partial K^+$ ($\rho_K = \rho_+ = 0$)
only $\hat\xi$, $\hat\eta$, $\omega$ move; $\hat\xi\in\{0,2\}$ forces $\hat\eta = 0$, a zero of $\mathsf H$, so a
non-constant curve has $\hat\xi\in(0,2)$. (b) The linear equation for $u$: if $\hat\xi\equiv0$, $u' = -2u$; if
$\hat\xi\equiv2$, $u' = 2u+4$; otherwise, with $\hat\xi = 2/(1+e^{4s})$, $1-\hat\xi = \tanh2s$, the homogeneous solution
is $\exp(-2\int\tanh2s\,ds) = (\cosh2s)^{-1}$, and $p := -e^{-2s}/\cosh2s$ is a particular solution: $p'$ and
$-2(1-\hat\xi)p+2\hat\xi$ both equal $2/\cosh^22s$, by $\cosh2s+\sinh2s = e^{2s}$ and $2\hat\xi = 4/(1+e^{4s}) =
2e^{-2s}/\cosh2s$. So $u = (C-e^{-2s})/\cosh2s$, positive if and only if $C>e^{-2s}$; $C\le0$ is excluded. In case (iii),
as $s\to\infty$, $u\sim2Ce^{-2s}\to0$, and at $s = -\frac12\log C$, $u = 0$. As $u>0$ on the open interval and $u\to0$ at
both ends, $u$ has an interior maximum, unique by Lemma 3.3 (3) below. In cases (i) and (ii) the limits are read off. (c)
By (3.4), $|\omega'|\le2|\hat\eta|$ in the round metric, and $|\hat\eta|^2 = \hat\xi(2-\hat\xi)$ decays exponentially at
each infinite end ($\hat\xi\sim2e^{-4s}$ or $2-\hat\xi\sim2e^{4s}$) and is bounded on the finite ends, so $\omega$
converges. $\square$

The finite end in (b) (ii) and (iii) is not a limit point in ${}^{e3b}S^*M$: as $u = x_I^2\to0$ the 3b-coordinates
degenerate, and the curve continues over $\mathscr I^+\cap\iota^+$ in the eb-coordinates of section 7, where the end is
reached only as the eb-parameter tends to $-\infty$ (Lemma 7.3).

### 3.3 Convexity and invariant manifolds

**Lemma 3.3 ([Hin26c] Lemma 4.6 at $n = 4$).** The flow of $\mathsf H$ on $\partial\Sigma^+$ over $K^+\cup\iota^+$ near
$\partial K^+$ has the following properties.

(1) (*Convexity in $K^+$.*) There is $\epsilon>0$ such that over $K^+$, if $\mathsf H\rho_+ = 0$ and $0<\rho_+<\epsilon$,
then $\mathsf H^2\rho_+<0$.

(2) (*Curves over $K^+$.*) Let $\gamma:I\to\partial\Sigma^+$ be a maximal integral curve over $K^+$, not contained in
$\partial R_{\partial K^+,\mathrm{in}}\cup\partial R_{\partial K^+,\mathrm{out}}$, with $\rho_+(\gamma(0))<\epsilon$. If
$\frac d{ds}\rho_+(\gamma(s))|_{s = 0}\le0$, then $\gamma(s)\to\partial R_{\partial K^+,\mathrm{out}}$ as $s\to\infty$;
if $\ge0$, then $\gamma(s)\to\partial R_{\partial K^+,\mathrm{in}}$ as $s\to-\infty$.

(3) (*Convexity in $\iota^+$.*) Over $\iota^+$, if $\mathsf H\rho_K = 0$ and $\rho_K>0$, then $\mathsf H^2\rho_K>0$.

(4) (*Invariant manifolds over $\iota^+$.*) $\partial W_{\mathrm{out}}$ is the unstable manifold of $\partial
R_{\partial K^+,\mathrm{out}}$ and $\partial W_{\mathrm{in}}$ the stable manifold of $\partial R_{\partial
K^+,\mathrm{in}}$ over $\iota^+$ (Lemma 3.2 (b)). Their conic extensions are, within $\Sigma^+$, the characteristic sets
of $r\partial_r$ and $2r\partial_{t_*}-r\partial_r$ over $\iota^+$ (D326: $\Sigma^+$, not $\Sigma$, which also holds the
half $\sigma_{3b}>0$) (D197; this statement printed the source's $r\partial_{t_*}-2r\partial_r$, which the proof
corrects).

*Proof.* (1) Over $K^+$ ($\rho_K = 0$), $\mathsf H\rho_+ = -2(1-\hat\xi)\rho_++\rho_+^3a$ with $a$ smooth, by section
3.1. So $\mathsf H\rho_+ = 0$ with $\rho_+>0$ gives $1-\hat\xi = \frac12\rho_+^2a$, and on $\partial\Sigma^+$,
$\hat\xi^2-2\hat\xi+|\hat\eta|^2 = O(\rho_+^2)$, so $\hat\xi = 1+O(\rho_+^2)$. Then
$$\mathsf H^2\rho_+ = 2\rho_+\mathsf H\hat\xi-2(1-\hat\xi)\mathsf H\rho_++\mathsf H(\rho_+^3a) = 2\rho_+\big(-2(2-\hat
\xi)\hat\xi+O(\rho_+^2)\big)+O(\rho_+^3) = -4\rho_++O(\rho_+^3),$$
using $\mathsf H\rho_+ = 0$ at the point and $\tilde{\mathsf H}\hat\xi = O(\rho_+^2)$. This is negative for $\rho_+<
\epsilon$, $\epsilon$ small. ((4.18) of the source has the factor $-2$ in place of $-4$; the sign is the same; section 9,
(B3).)

(2) If $\rho_+(\gamma(0)) = 0$, $\gamma$ lies over $\partial K^+$ (the face is invariant, $\mathsf H\rho_+\in\rho_+
C^\infty$), and Lemma 3.2 (a) applies. Let $\rho_+(\gamma(0))\in(0,\epsilon)$ and $f := \rho_+\circ\gamma$, with
$f'(0)\le0$. Then $f>0$ throughout, $\{\rho_+ = 0\}$ being invariant. At any $s$ with $f'(s) = 0$ and $f(s)<\epsilon$,
$f''(s)<0$ by (1). Hence $f'<0$ on $(0,\sup I)$: if $f'(0)<0$, or $f'(0) = 0$ and then $f''(0)<0$, $f'<0$ on some
$(0,\delta)$; at a first zero $s_1>0$ of $f'$, $f(s_1)<f(0)<\epsilon$, so $f''(s_1)<0$, while $f'<0$ on $(0,s_1)$ forces
$f''(s_1)\ge0$. So $f$ is strictly decreasing for $s>0$ (where the source says "strictly increasing"; section 9, (B1)),
$\gamma$ stays in the compact set $\{\rho_+\le\epsilon\}\cap\partial\Sigma^+$ over $K^+$, $\sup I = \infty$, and $f\to
L\in[0,\epsilon)$. The $\omega$-limit set $\Omega_\gamma$ is non-empty, compact and invariant, and $\rho_+ = L$ on it. If
$L>0$, the curve through a point of $\Omega_\gamma$ has $\rho_+\equiv L$, so $\mathsf H\rho_+ = \mathsf H^2\rho_+ = 0$
there, against (1). So $L = 0$. For $s>0$, $\mathsf H\rho_+<0$, that is $1-\hat\xi>\frac12\rho_+^2a$, so $\hat\xi\le1+C
\epsilon^2$ along $\gamma$ and on $\Omega_\gamma$. $\Omega_\gamma$ lies over $\partial K^+$, where the flow is that of
Lemma 3.2 (a). If $\Omega_\gamma$ contained a point with $\hat\xi\in(0,2)$, it would contain its backward orbit, on which
$\hat\xi\to2$, against $\hat\xi\le1+C\epsilon^2$. So $\hat\xi = 0$, hence $\hat\eta = 0$, on $\Omega_\gamma$:
$\Omega_\gamma\subset\partial R_{\partial K^+,\mathrm{out}}$, which is the claim. The case $f'(0)\ge0$ is the same with
$-\mathsf H$, for which (1) holds as well since $(-\mathsf H)^2 = \mathsf H^2$, and the roles of $\hat\xi = 0$ and $2$
exchanged.

(3) Over $\iota^+$, $\mathsf H = \bar{\mathsf H}$. If $\mathsf H\rho_K = 0$, then $1-\hat\xi = \hat\xi\rho_K$ and
$$\mathsf H^2\rho_K = -2\rho_K(1+\rho_K)\mathsf H\hat\xi+\big(2(1-\hat\xi)-4\hat\xi\rho_K\big)\mathsf H\rho_K =
4\rho_K(1+\rho_K)\hat\xi(2-\hat\xi) = 4\rho_K(1+\rho_K)|\hat\eta|^2.$$
If $\hat\eta = 0$, then $\hat\xi\in\{0,2\}$ and $\mathsf H\rho_K = 2\rho_K$, resp. $-2\rho_K-4\rho_K^2$, which is not
zero for $\rho_K>0$. So $\mathsf H^2\rho_K>0$.

(4) By Lemma 3.2 (b), the curves over $\iota^+$ that tend to $\partial R_{\partial K^+,\mathrm{out}}$ as $s\to-\infty$
are those of (i), and those that tend to $\partial R_{\partial K^+,\mathrm{in}}$ as $s\to\infty$ are those of (ii). The
conic extensions are $\{\xi_{3b} = 0,\eta_{3b} = 0,\sigma_{3b}<0\}$ and $\{\xi_{3b} = 2\sigma_{3b},\eta_{3b} =
0,\sigma_{3b}<0\}$ over $\iota^+$, the intersections with $\Sigma^+$ of the characteristic sets of $r\partial_r$ and of
$2r\partial_{t_*}-r\partial_r$ (on $\Sigma$, $\xi_{3b} = 0$ and $\xi_{3b} = 2\sigma_{3b}$ each force $\eta_{3b} = 0$ by
(3.2)), with which a 3b-covector (3.1) pairs to $\xi_{3b}$, resp. $2\sigma_{3b}-\xi_{3b}$. In the coordinates $(t,r)$,
$t = t_*+r$, these fields are $r(\partial_t+ \partial_r)$ and $r(\partial_t-\partial_r)$, the outgoing and incoming null
fields of $\bar g$: $\partial_t|_r = \partial_{t_*}$ and $\partial_r|_t = \partial_r-\partial_{t_*}$. (The source prints
$\xi_{3b} = -2\sigma_{3b}$ for the second set and $r\partial_{t_*}-2r\partial_r$ for the second field; neither matches
its own $\partial W^+_{\mathrm{in}} = \{\hat\xi_{3b} = 2\}$ nor its $r(\partial_t-\partial_r)$; section 9, (B2).)
$\square$

The uniqueness of the interior maximum of $u$ in Lemma 3.2 (b) (iii) is (3): $u = \rho_K^{-1}$, and at a zero of
$\mathsf H\rho_K$, $\mathsf H^2u = -\rho_K^{-2}\mathsf H^2\rho_K<0$, so every critical point of $u$ is a strict local
maximum, and there is at most one.

## 4. The horizon at $K^+$

**Definition 4.1 ([Hin26c] Definition 4.8).** $R_{\mathcal H^+} := \{\rho_K = 0,\ \sigma = 0,\ \zeta\in\mathcal
R_+\}\subset {}^{3b}T^*_{(K^+)^\circ}M_0\setminus o$, with $\mathcal R_+$ the component of $N^*\mathcal H\setminus o$ of
(H3), and $\partial R_{\mathcal H^+}$ its boundary at fibre infinity, which is $\Phi_{\pm1}(\partial\mathcal R_+)$.

Near $\partial R_{\mathcal H^+}$ let $\rho_\infty$ be the function of (H3), positive and homogeneous of degree $-1$ in
$\zeta$, put $\hat\sigma := \sigma\rho_\infty$, and $\mathsf H := \rho_\infty H_G$; on $\Sigma$ this is a positive
multiple of (1.4). As $\zeta\ne0$ there, $(x,[\zeta],\hat\sigma)$, $[\zeta]\in S^*\tilde X^\circ$, are coordinates on
${}^{3b}S^*_{(K^+)^\circ}M_0$ near $\partial R_{\mathcal H^+}$, in which $\partial R_{\mathcal H^+} = \{\hat\sigma =
0\}\times \partial\mathcal R_+$.

**Lemma 4.2 ([Hin26c] Lemma 4.9 and (4.28)).** Let $\tilde q$ be the function of I.A Lemma 4.1 for $\mathcal R = \mathcal
R_+$, regarded as a function of $(x,[\zeta])$. There are $K,c>0$ and a neighbourhood $W$ of $\partial R_{\mathcal H^+}$
in ${}^{3b}S^*_{(K^+)^\circ}M_0$ such that $F := \tilde q+K\hat\sigma^2$ is a quadratic defining function of $\partial
R_{\mathcal H^+}$ and $\mathsf HF\ge cF$ on $W$. At $\partial R_{\mathcal H^+}$,
$$\rho_\infty^{-1}\mathsf H\rho_\infty = \beta_0>0,\qquad\rho_K^{-2}\mathsf H\rho_K = \rho_\infty\tau_1\le
-\beta\beta_0<0,\tag{4.1}$$
with $\beta_0$, $\beta$ of (H3). So $\partial R_{\mathcal H^+}$ is a source for the flow within
${}^{3b}S^*_{(K^+)^\circ}M_0$ (not only within $\partial\Sigma^+$), $\rho_\infty$ grows along the flow near it, and
$\rho_K$ decays.

*Proof.* For a function $f(x,[\zeta])$, independent of $\sigma$ and $t_*$ and homogeneous of degree 0 in $\zeta$, Lemma
2.1 and $G = G_0+\sigma\tau_1+\sigma^2g_{00}$ give
$$\mathsf Hf = \mathsf H_0f+\hat\sigma\,H_{\tau_1}f+\hat\sigma^2\rho_\infty^{-1}H_{g_{00}}f,\qquad\mathsf
H_0 := \rho_\infty H_{G_0},\tag{4.2}$$
where $H_{\tau_1}f$ and $\rho_\infty^{-1}H_{g_{00}}f = -\rho_\infty^{-1}(\partial_xg_{00})\cdot\partial_\zeta f$ are
homogeneous of degree 0 and smooth near $\partial\mathcal R_+$. $\mathsf H_0$ is the field of (H3), extended off
$\Sigma_0$ by the same formula, as in I.A Lemma 4.1, which gives $\mathsf H_0\tilde q\ge c'\tilde q$ on a neighbourhood
of $\partial\mathcal R_+$ in $S^*\tilde X^\circ$. As $\tilde q$ is smooth and vanishes quadratically at $\partial\mathcal
R_+$, with $\tilde q\ge c''\mathrm{dist}^2$, $|d\tilde q|\le C\tilde q^{1/2}$, so $|H_{\tau_1}\tilde q|\le C\tilde
q^{1/2}$. Hence $\mathsf H\tilde q\ge c'\tilde q-C|\hat\sigma|\tilde q^{1/2}-C\hat\sigma^2\ge\frac{c'}2\tilde
q-C_1\hat\sigma^2$. Next, $\mathsf H\sigma = 0$ (Lemma 2.1), so $\mathsf H\hat\sigma = \hat\sigma\rho_\infty^{-1}\mathsf
H\rho_\infty$, and
$$\rho_\infty^{-1}\mathsf H\rho_\infty = H_G\rho_\infty = \beta_0+\hat\sigma\rho_\infty^{-1}H_{\tau_1}\rho_\infty+
\hat\sigma^2\rho_\infty^{-2}H_{g_{00}}\rho_\infty,\qquad\beta_0 := \rho_\infty^{-1}\mathsf H_0\rho_\infty,$$
the last two coefficients being homogeneous of degree 0. By (H3), $\beta_0\ge b_0>0$ near $\partial\mathcal R_+$, so on
$\{|\hat\sigma|\le\delta\}$, $\rho_\infty^{-1}\mathsf H\rho_\infty\ge b_0/2$ and $\mathsf H(\hat\sigma^2)\ge
b_0\hat\sigma^2$. With $K\ge2(C_1+1)/b_0$,
$$\mathsf HF\ge\tfrac{c'}2\tilde q+(Kb_0-C_1)\hat\sigma^2\ge\tfrac{c'}2\tilde q+\tfrac{Kb_0}2\hat\sigma^2\ge\min(\tfrac
{c'}2,\tfrac{b_0}2)F.$$
In the coordinates $(x,[\zeta],\hat\sigma)$, $\tilde q$ is a quadratic defining function of $\partial\mathcal R_+$ in
$S^*\tilde X^\circ$ (I.A Lemma 4.1), so $F$ is one of $\{\hat\sigma = 0\}\times\partial\mathcal R_+$. For (4.1): at
$\hat\sigma = 0$, $\rho_\infty^{-1}\mathsf H\rho_\infty = \beta_0$. With $\tau := -\sigma$ the dual variable of $t_*$,
$H_Gt_* = \partial_\tau G = -\tau_1-2\sigma g_{00}$, so $\mathsf Ht_* = -\rho_\infty\tau_1$ at $\sigma = 0$, and
$\mathsf H\rho_K = -\rho_K^2\mathsf Ht_*$. By (H3), $-\beta_0^{-1}\rho_\infty\tau_1\ge\beta$ on $\partial\mathcal R_+$.
$\square$

In the source's Kerr coordinates $F$ corresponds to $\hat\sigma_0^2+\rho_\infty^2\mathscr C$ of its Lemma 4.9.

## 5. The trapped set at $K^+$

**Definition 5.1 ([Hin26c] (4.63)).** $\partial\Gamma_{K^+} := \Phi_1(\Gamma)$, with $\Gamma = \Gamma_1$ the trapped set
of (H7) at $z_0 = 1$, and $\partial\bar\Gamma^{u/s}_{K^+} := \Phi_1(\bar\Gamma_{u/s})$, with $\bar\Gamma_{u/s}\subset
\Sigma^\flat_1$ the global backward and forward trapped sets of (H8); $\Gamma^{u/s}_{K^+} := \Phi_1(\Gamma_{u/s})$ for
the local sets of (H7) in $O$.

**Lemma 5.2.** (a) $\partial\Gamma_{K^+}$ is a compact invariant subset of
$\partial\Sigma^+\cap{}^{3b}S^*_{(K^+)^\circ}M_0$, lying over $\{r_2<r<\rho_1^{-1}\}$ and in $\{\sigma>0\}$: $\sigma$ is
positive, hence elliptic, there ([Hin26c] (4.64)). (b) $\partial\bar\Gamma^{u/s}_{K^+}$ are invariant, and consist of the
points whose integral curves tend to $\partial\Gamma_{K^+}$ backward, resp. forward. Near $\partial\Gamma_{K^+}$,
$\Gamma^u_{K^+}$ and $\Gamma^s_{K^+}$ are smooth hypersurfaces of $\partial\Sigma^+\cap\{\sigma>0\}$, tangent to the
flow, meeting transversally in $\partial\Gamma_{K^+}$, and, after shrinking $O$,
$\partial\bar\Gamma^{u/s}_{K^+}\cap\Phi_1(O) = \Gamma^{u/s}_{K^+}$. (c) No integral curve tends to $\partial\Gamma_{K^+}$
in both directions unless it lies in $\partial\Gamma_{K^+}$. (d) Under $\Phi_1$, the field $\mathsf V$ of (K3) is the
projection of $H_G/(H_Gt_*)$ at $\sigma = 1$, so (K3) is [Hin26c] Proposition 4.19 for the stationary model, with the
quotient by $t_*$-translations and fibre dilations realised by the slice $\{\sigma = 1\}$ of
${}^{3b}T^*_{(K^+)^\circ}M_0$.

*Proof.* (a), (b): $\Phi_1$ is a diffeomorphism onto its image which maps $\Sigma^+_1 = \Sigma^\flat_1$ into
$\partial\Sigma^+ \cap\{\sigma>0\}$ and the future field to a positive multiple of the future field (Lemma 2.3 (c), (d));
(H7) and (H8) (b) transfer, and $\Gamma\subset T^*\{r_2<r<\rho_1^{-1}\}$ is compact by (H7). (c) Let $\gamma$ tend to
$\partial\Gamma_{K^+}$ in both directions. Then $\gamma\subset\partial\bar\Gamma^u_{K^+}\cap\partial\bar\Gamma^s_{K^+}$,
and for $|s|$ large $\gamma(s)\in\Phi_1(O)$, so $\gamma(s)\in\Gamma^u_{K^+}\cap\Gamma^s_{K^+} = \partial\Gamma_{K^+}$ by
(b) and (H7) ($\Gamma_u\cap \Gamma_s = \Gamma$ within $O$). $\partial\Gamma_{K^+}$ is invariant, so
$\gamma\subset\partial\Gamma_{K^+}$. (d) At $\sigma = 1$, $H_Gt_* = -\tau_1-2g_{00} = q_1$ (proof of Lemma 4.2; I.B Lemma
1.1 (b)), and by Lemma 2.1 the restriction of $H_G$ to $\{\sigma = 1\}$ acts on $(x,\zeta)$ as $H_{G_1}$. $\square$

[Hin26c] Lemma 4.20 (rescalings and linearisations) serves in the source only to prove its Proposition 4.19 (3) from the
Carter flow, and is not needed here, (K3) being assumed for $\mathsf V$ itself; section 9, (B4).

## 6. The dynamics over the Kerr face

**Proposition 6.1 ([Hin26c] Proposition 4.21 at $n = 4$).** Let $\gamma:I\to\partial\Sigma^+\cap{}^{3b}S^*_{K^+}M_0$,
over $\{r>r_0-2\delta_0\}$, be a maximal integral curve of the field (1.4), not contained in $\partial R_{\partial
K^+,\mathrm{in}}$, $\partial R_{\partial K^+,\mathrm{out}}$, $\partial R_{\mathcal H^+}$ or $\partial\Gamma_{K^+}$. Then:

(1) as $s$ increases, $\gamma$ tends to $\partial\Gamma_{K^+}$ or to $\partial R_{\partial K^+,\mathrm{out}}$, or reaches
$\{r<r_0-\delta_0\}$ at a finite parameter;

(2) as $s\to-\infty$, $\gamma$ tends to $\partial\Gamma_{K^+}$, to $\partial R_{\partial K^+,\mathrm{in}}$ or to
$\partial R_{\mathcal H^+}$;

(3) $\gamma$ does not tend to $\partial\Gamma_{K^+}$ in both directions.

Moreover, $\gamma$ tends to $\partial\Gamma_{K^+}$ forward (backward) if and only if it lies in $\partial\bar
\Gamma^s_{K^+}$ ($\partial\bar\Gamma^u_{K^+}$); a curve over $\partial K^+$ goes from $\partial R_{\partial
K^+,\mathrm{in}}$ to $\partial R_{\partial K^+,\mathrm{out}}$; and a curve in $\{\sigma\le0\}$ goes from $\partial
R_{\mathcal H^+}$ to $\{r<r_0-\delta_0\}$.

"Tends to $A$" means that every limit point lies in $A$; for a set $A$ of fixed points this is the convergence of
[Hin26c].

*Proof.* The sign of $\sigma$ is constant along $\gamma$ (Lemma 2.1, the rescaling being positive), and the faces
$\partial K^+$ and $(K^+)^\circ$ are invariant. A curve in a compact set has a non-empty, compact, connected and
invariant $\omega$-limit set, and likewise $\alpha$-limit set; so "tends to $A\cup B$", with $A$, $B$ disjoint compact
sets, means "tends to $A$ or tends to $B$".

*$\sigma>0$.* By Lemma 2.3, $\gamma = \Phi_1\circ\tilde\gamma$ up to an increasing reparametrisation, with $\tilde\gamma$
a maximal integral curve of the future field $\mathsf H_1$ in $\Sigma^+_1 = \Sigma^\flat_1$, finite or over $\partial X$.
Over $\partial X$ (that is, $\gamma$ over $\partial K^+$), I.A Lemma 4.5 at $\sigma_0 = 1$, or Lemma 3.2 (a), gives the
claim. Otherwise $\tilde\gamma$ lies in $\Sigma_1\cap T^*\{r>r_0-2\delta_0\}$, and (H8) (a) applies. If $\tilde\gamma\not
\subset\bar\Gamma_u$, it tends backward to $\partial\mathcal R_+\cup\partial\mathcal R_-$ or to $R_{1,\mathrm{in}}$; not
to $\partial\mathcal R_-$, since at fibre infinity $\hat q_1 = -\rho_\infty\tau_1$ is negative near $\partial\mathcal
R_-$ by (H3) while $q_1>0$ along $\tilde\gamma$. Under $\Phi_1$, $\partial\mathcal R_+$ is $\partial R_{\mathcal H^+}$
and $R_{1, \mathrm{in}}$ is $\partial R_{\partial K^+,\mathrm{in}}$ (Definition 3.1). If
$\tilde\gamma\not\subset\bar\Gamma_s$, it tends forward to $R_{\mathrm{out}}$, which is $\partial R_{\partial
K^+,\mathrm{out}}$, or reaches $\{r<r_0-\delta_0\}$. If $\tilde\gamma\subset\bar\Gamma_u$ (resp. $\bar\Gamma_s$), it
tends to $\Gamma$ backward (forward), by the definition of these sets. (3) is Lemma 5.2 (c).

*$\sigma = 0$.* $\gamma$ lies in $\Phi_{\pm1}(\partial\Sigma_0^+)$ at fibre infinity of the stationary phase space, with
the future field $+\rho_\infty H_{G_0}$ up to a positive factor (Lemma 2.3). By (H4) it tends backward to
$\partial\mathcal R_+\cup\partial\mathcal R_-$, hence to $\partial\mathcal R_+$, the components $\partial\Sigma_0^\pm$
being disjoint, compact and invariant; and it reaches $\{r<r_0-\delta_0\}$ forward at a finite parameter.

*$\sigma<0$.* $\gamma = \Phi_{-1}\circ\tilde\gamma$ with $\tilde\gamma$ a maximal integral curve of the future field in
$\Sigma^+_{-1}$, which lies over $\{r<R_1\}$ (Lemma 2.3 (d)), so its limit points are not over $\partial X$. $\Gamma_{-1}
\subset\Sigma^\flat_{-1} = \Sigma^-_{-1}$, and $q_{-1}\le-2\beta_0<0$ near $\Gamma_{-1}$ by (Γ.4), while $q_{-1}>0$ on
$\tilde\gamma$; so $\tilde\gamma$ lies in neither $\bar\Gamma_u$ nor $\bar\Gamma_s$. By (H8) (a), $\tilde\gamma$ tends
backward to $\partial\mathcal R_+$ (not $\partial\mathcal R_-$, as before, nor $R_{-1,\mathrm{in}}$, over $\partial X$),
and reaches $\{r<r_0-\delta_0\}$ forward (not $R_{\mathrm{out}}$, over $\partial X$). $\square$

## 7. The eb-dynamics near $\mathscr I^+$

Near $\mathscr I^+\cap\iota^+$ use $\rho_+ = t_*^{-1}$, $x_I = (t_*/r)^{1/2}$, $\omega$ (II.A section 1) and eb-covectors
$\sigma_{eb}\frac{d\rho_+}{\rho_+}+\xi_{eb}\frac{dx_I}{x_I}+\eta_{eb}\frac{d\omega}{x_I}$ (II.A Definition 2.4), and put
$G_{eb} := x_I^{-2}\rho_+^{-2}G$. Since $\frac{d\rho_+}{\rho_+} = -\rho_+\,dt_*$ and $\frac{dx_I}{x_I} =
\frac12\rho_+(dt_*-x_I^2\,dr)$, the covector is $\nu =
\rho_+(\frac12\xi_{eb}-\sigma_{eb})\,dt_*-\frac12\rho_+x_I^2\xi_{eb} \,dr+x_I^{-1}\eta_{eb}\,d\omega$, and $\bar
g^{-1}(\nu,\nu) = -2\nu_{t_*}\nu_r+\nu_r^2+r^{-2}|\nu_\omega|^2$ with $r^{-2} = \rho_+^2x_I^4$ gives
$$\bar G_{eb} = \tfrac12\xi_{eb}(\xi_{eb}-2\sigma_{eb})+|\eta_{eb}|^2+\tfrac14x_I^2\xi_{eb}^2.\tag{7.1}$$
This is the inverse of II.A's form of $\bar g$ near $\mathscr I^+\cap\iota^+$, with the angular term
$\frac{\slashed g}{2x_I^2}$ there (section 9, (B6)). By Lemma 1.1 (the inverses), $G_{eb}-\bar G_{eb}\in x_I^2\rho_+^2
P^{[2]}({}^{eb}T^*M)$, so $G_{eb}\equiv G^0_{eb} := \frac12\xi_{eb}(\xi_{eb}-2\sigma_{eb})+|\eta_{eb}|^2$ modulo
$x_I^2P^{[2]}$, and as $H_{x_I} = -x_I\partial_{\xi_{eb}}$ by II.A (2.2), $H_{G_{eb}}\equiv H_{G^0_{eb}}$ modulo
$x_I^2\mathcal V_{eb}({}^{eb}T^*M)$, where, by (2.2),
$$H_{G^0_{eb}} = -\xi_{eb}\rho_+\partial_{\rho_+}+(\xi_{eb}-\sigma_{eb})(x_I\partial_{x_I}+\eta_{eb}
\partial_{\eta_{eb}})-2|\eta_{eb}|^2\partial_{\xi_{eb}}+x_IH_{|\eta_{eb}|^2}\tag{7.2}$$
([Hin26c] p. 96, here on $T^*\mathbb S^3$).

*The sign of $\sigma_{eb}$.* $\sigma_{eb} = \nu(\rho_+\partial_{\rho_+})$, and at fixed $x_I$, $\rho_+\partial_{\rho_+} =
-(t_*\partial_{t_*}+r\partial_r) = -(t\partial_t+r\partial_r)$. $V := t\partial_t+r\partial_r$ has $\bar g(V,V) =
-t_*^2-2t_*r$, and by (K1), $|g(V,V)-\bar g(V,V)|\le Cr^{-2}(t_*+r)^2\le\frac12(t_*^2+2t_*r)$ on $\Omega\cap\{r\ge R_2\}$
for $R_2$ large ($t_*\ge1$). So $V$ is timelike there, and future directed: $g(V,-\nabla t_*) = -dt_*(V) = -t_*<0$. For
$\nu\in\Sigma^+$ over $M^\circ$ there, $\nu(V)<0$, so $\sigma_{eb} = -\nu(V)>0$; on $\Sigma$ over $\mathscr I^+$,
$\sigma_{eb} = 0$ would force $\frac12\xi_{eb}^2+|\eta_{eb}|^2 = 0$, so $\sigma_{eb}>0$ on $\Sigma^+$ near $\mathscr I^+
\cap\iota^+$ ([Hin26c] p. 96). Put
$$\rho_\infty := \sigma_{eb}^{-1},\qquad\hat\xi := \xi_{eb}/\sigma_{eb},\qquad\hat\eta := \eta_{eb}/\sigma_{eb},\qquad
\mathsf H := \rho_\infty H_{G_{eb}}.\tag{7.3}$$
Then $\rho_\infty^2G^0_{eb} = \frac12\hat\xi(\hat\xi-2)+|\hat\eta|^2$, and $\mathsf H^0 := \rho_\infty H_{G^0_{eb}}$
satisfies, exactly ($H_{G^0_{eb}}\sigma_{eb} = 0$),
$$\mathsf H^0\rho_+ = -\hat\xi\rho_+,\quad\mathsf H^0x_I = (\hat\xi-1)x_I,\quad\mathsf H^0\rho_\infty =
0,\quad\mathsf H^0\hat\xi = -2|\hat\eta|^2,\quad\mathsf H^0\hat\eta = (\hat\xi-1)\hat\eta-x_I
\partial_\omega|\hat\eta|^2,\tag{7.4}$$
which is [Hin26c] (4.67); $\mathsf H-\mathsf H^0\in x_I^2\mathcal V_{eb}$, tangent to ${}^{eb}S^*M$.

**Definition 7.1 ([Hin26c] Definition 4.22).** $\partial R_{\mathscr I^+,\mathrm{out}} := \{x_I = 0,\hat\xi = 0,\hat\eta
= 0\}$ over $\mathscr I^+$ (all $\rho_+$), and $\partial R_{\mathscr I^+,\mathrm{in},+} := \{\rho_+ = 0,x_I = 0,\hat\xi =
2,\hat \eta = 0\}$ over $\mathscr I^+\cap\iota^+$; their conic extensions lie in $\{\sigma_{eb}>0\}$.

By (7.4), with $\hat\xi$ a function of $(\rho_+,x_I,\hat\eta)$ on $\partial\Sigma^+$ near each set, the linearisation of
$\mathsf H$ is $dx_I\mapsto-dx_I$, $d\hat\eta\mapsto-d\hat\eta$ at $\partial R_{\mathscr I^+,\mathrm{out}}$, and
$d\rho_+\mapsto-2d\rho_+$, $dx_I\mapsto dx_I$, $d\hat\eta\mapsto d\hat\eta$ at $\partial R_{\mathscr I^+,\mathrm{in},+}$
([Hin26c] (4.69)); the error vanishes to second order at $x_I = 0$. So the first is a sink transversally to its
$\rho_+$-fibres, the second a saddle.

**Lemma 7.2 ([Hin26c] Lemma 4.23 at $n = 4$).** (1) (*Over $\mathscr I^+$.*) On $\partial\Sigma^+$ over $\mathscr I^+$,
$\hat\xi\in[0,2]$ and $|\hat\eta|^2 = \frac12\hat\xi(2-\hat\xi)$, and along integral curves
$$\hat\xi' = -\hat\xi(2-\hat\xi),\qquad\rho_+' = -\hat\xi\rho_+.\tag{7.5}$$
A maximal integral curve over $\mathscr I^+\cap\Omega$ not contained in $\partial R_{\mathscr I^+,\mathrm{out}}\cup
\partial R_{\mathscr I^+,\mathrm{in},+}$ is one of: (i) $\hat\xi = 2/(1+e^{2s})$, $\rho_+ = A(1+e^{-2s})$ with $0<A<1$:
forward it tends to $\partial R_{\mathscr I^+,\mathrm{out}}$ (at $\rho_+ = A$), backward it reaches $\{t_* = 1\}$ at a
finite parameter; (ii) the same with $A = 0$, over $\mathscr I^+\cap\iota^+$: from $\partial R_{\mathscr I^+,\mathrm{in},
+}$ to $\partial R_{\mathscr I^+,\mathrm{out}}$; (iii) $\hat\xi\equiv2$, $\hat\eta\equiv0$, $\rho_+ = \rho_+(0)e^{-2s}$,
$\rho_+(0)>0$: forward it tends to $\partial R_{\mathscr I^+,\mathrm{in},+}$, backward it reaches $\{t_* = 1\}$.

(2) (*Convexity in $\iota^+$.*) Over $\iota^+$, if $\mathsf Hx_I = 0$ and $x_I>0$, then $\mathsf H^2x_I<0$.

(3) (*Invariant manifolds.*) $\partial W_{\mathscr I^+} := \{\hat\xi = 2,\hat\eta = 0\}$ over $\mathscr I^+$ is the
stable manifold of $\partial R_{\mathscr I^+,\mathrm{in},+}$ within $\partial\Sigma^+$ over $\mathscr I^+$; in the
present coordinates, $\partial W_{\mathrm{out}}$ of Lemma 3.3 (4) is $\{\rho_+ = 0,\hat\xi = 0,\hat\eta = 0\}$.

*Proof.* (1) Over $\mathscr I^+$, $\mathsf H = \mathsf H^0$ and $\rho_\infty^2G_{eb} = \frac12\hat\xi(\hat\xi-2)+|\hat
\eta|^2$, so on $\partial\Sigma^+$, $|\hat\eta|^2 = \frac12\hat\xi(2-\hat\xi)$, and (7.4) gives (7.5). If $\hat\xi(0)\in
\{0,2\}$ then $\hat\eta = 0$; $\hat\xi\equiv0$ gives a point of $\partial R_{\mathscr I^+,\mathrm{out}}$, and
$\hat\xi\equiv2$ gives (iii) or, at $\rho_+ = 0$, a point of $\partial R_{\mathscr I^+,\mathrm{in},+}$. Otherwise
$\hat\xi = 2/(1+e^{2s})$ after a shift, $\rho_+'/\rho_+ = -2/(1+e^{2s})$, and $\rho_+ = A(1+e^{-2s})$. On $\Omega$,
$\rho_+\le1$, so $A<1$ if $A>0$, and $\rho_+\uparrow$ as $s\downarrow$ reaches $1$ at a finite parameter. The angular
coordinates: $|\omega'|\le2x_I|\hat\eta| = 0$ over $\mathscr I^+$, and the limits of $\hat\xi$, $\hat\eta$, $\rho_+$ are
read off. (2) Over $(\iota^+)^\circ$, $x_I^2 = u = \rho_K^{-1}$, and by Lemma 7.3 below $\mathsf H$ is a positive
multiple $c\,\mathsf H^{3b}$ of the field of section 3 on $\Sigma$. At a zero of $\mathsf Hx_I$, $\mathsf H^{3b}\rho_K =
0$, and $\mathsf H^2x_I = c^2(\mathsf H^{3b})^2 x_I = -\frac12c^2\rho_K^{-3/2}(\mathsf H^{3b})^2\rho_K<0$ by Lemma 3.3
(3). (3) $\partial W_{\mathscr I^+}$ is invariant by (7.5) and consists of the curves (iii) and the points of $\partial
R_{\mathscr I^+,\mathrm{in},+}$; curves over $\mathscr I^+$ with $\hat\xi\ne2$ tend to $\partial R_{\mathscr
I^+,\mathrm{out}}$ by (1). The last statement is Lemma 7.3 at $\hat\xi_{3b} = 0$. $\square$

**Lemma 7.3 (3b and eb over $\iota^+$).** Over $(\iota^+)^\circ$, with $u = x_I^2 = t_*/r$ and the 3b-coordinates (3.1),
(3.3), $\sigma_{eb} = -\sigma_{3b}(u+\hat\xi_{3b})$, $\xi_{eb} = -2\xi_{3b}$, $\eta_{eb} = x_I\eta_{3b}$; hence
$$\hat\xi_{eb} = \frac{2\hat\xi_{3b}}{u+\hat\xi_{3b}},\qquad\hat\eta_{eb} = -\frac{x_I\hat\eta_{3b}}{u+\hat
\xi_{3b}},\qquad\mathsf H = \frac u{u+\hat\xi_{3b}}\,\mathsf H^{3b}\ \text{on}\ \Sigma,\tag{7.6}$$
with $\mathsf H^{3b} := -\sigma_{3b}^{-1}H_{G_{3b}}$ as in section 3. Consequently, in Lemma 3.2 (b), the curves (ii) and
(iii) tend to $\partial R_{\mathscr I^+,\mathrm{in},+}$ as the eb-parameter tends to $-\infty$, and the curves (i) and
(iii) tend to $\partial R_{\mathscr I^+,\mathrm{out}}$ as $s\to\infty$.

*Proof.* $-\sigma\,dt_*+\xi\,dr+\eta = \sigma_{3b}\frac{dt_*}r+\xi_{3b}\frac{dr}r+\eta_{3b}$ and the formula for $\nu$
above give $\sigma_{eb} = \sigma t_*-\xi r = -\sigma_{3b}u-\xi_{3b}$, $\xi_{eb} = -2\xi r = -2\xi_{3b}$, $\eta_{eb} =
x_I\eta_{3b}$. On $\Sigma^+$ over $\iota^+$, $\sigma_{3b}<0$ and $\hat\xi_{3b}\in[0,2]$, so $u+\hat\xi_{3b}>0$. $G_{eb} =
x_I^{-2}\rho_+^{-2}G = rt_*G = uG_{3b}$, so $H_{G_{eb}} = uH_{G_{3b}}$ on $\Sigma$, and $\sigma_{eb}^{-1} =
-\sigma_{3b}^{-1} (u+\hat\xi_{3b})^{-1}$. For the limits: in (ii) and (iii) the 3b-parameter reaches the end $s_0$ with
$u\to0$ and $\hat \xi_{3b}\to\hat\xi_0\in(0,2]$; by (3.5), $u' = 2\hat\xi_0+O(u)$ there, so $u\sim2\hat\xi_0(s-s_0)$, and
the eb-parameter $\int(u+\hat\xi_{3b})u^{-1}ds$ diverges to $-\infty$; along the way $\hat\xi_{eb}\to2$,
$\hat\eta_{eb}\to0$ by (7.6), and $\omega$ converges (Lemma 3.2 (c)): the limit is in $\partial R_{\mathscr
I^+,\mathrm{in},+}$. As $s\to\infty$ in (iii), $\hat\xi_{3b}\sim2e^{-4s}$, $|\hat\eta_{3b}|\sim2e^{-2s}$ and
$u\sim2Ce^{-2s}$, so $\hat\xi_{eb}\sim\frac2Ce^{-2s}\to0$ and $|\hat\eta_{eb}|\lesssim e^{-s}\to0$; in (i), $\hat\xi_{3b}
= 0$ and $\hat\xi_{eb} = \hat\eta_{eb} = 0$ while $u\to0$. In both cases $\rho_+ = 0$ and $x_I\to0$: the limit is in
$\partial R_{\mathscr I^+,\mathrm{out}}$. $\square$

## 8. The global dynamics in e3b-phase space

**Proposition 8.1 ([Hin26c] Proposition 4.24 at $n = 4$, curves over the boundary).** Let $\gamma$ be a maximal integral
curve of (1.4) in $\partial\Sigma^+$ over $\partial\tilde M\cap\Omega\cap\{r>r_0-2\delta_0\}$, that is over $(\mathscr
I^+\cap\Omega)\cup\iota^+\cup K^+$. Say $\gamma$ is of type $(A,B)$ if it tends to $A$ backward (or reaches $A$ at a
finite parameter, for $A = \{t_* = 1\}$) and to $B$ forward (or reaches $B$, for $B = \{r<r_0-\delta_0\}$). Then $\gamma$
lies in one of $\partial R_{\mathcal H^+}$, $\partial R_{\mathscr I^+,\mathrm{in},+}$, $\partial R_{\partial
K^+,\mathrm{in}}$, $\partial\Gamma_{K^+}$, $\partial R_{\partial K^+,\mathrm{out}}$, $\partial R_{\mathscr
I^+,\mathrm{out}}$, or it is of one of the following types, where $R^K_{\mathrm{in/out}} := \partial R_{\partial
K^+,\mathrm{in/out}}$, $R^I_{\mathrm{in}} := \partial R_{\mathscr I^+,\mathrm{in},+}$, $R^I_{\mathrm{out}} := \partial
R_{\mathscr I^+,\mathrm{out}}$, $R_{\mathcal H} := \partial R_{\mathcal H^+}$, $\Gamma_K := \partial\Gamma_{K^+}$ and
$r_- := \{r<r_0-\delta_0\}$.

| over | $A$ | $B$ |
|---|---|---|
| $(\mathscr I^+)^\circ\cap\Omega$ | $\{t_* = 1\}$ | $R^I_{\mathrm{in}}$, $R^I_{\mathrm{out}}$ |
| $\mathscr I^+\cap\iota^+$ | $R^I_{\mathrm{in}}$ | $R^I_{\mathrm{out}}$ |
| $(\iota^+)^\circ$ | $R^I_{\mathrm{in}}$ | $R^K_{\mathrm{in}}$, $R^I_{\mathrm{out}}$ |
| $(\iota^+)^\circ$ | $R^K_{\mathrm{out}}$ | $R^I_{\mathrm{out}}$ |
| $\partial K^+$ | $R^K_{\mathrm{in}}$ | $R^K_{\mathrm{out}}$ |
| $(K^+)^\circ$ | $R_{\mathcal H}$, $R^K_{\mathrm{in}}$ | $r_-$, $\Gamma_K$, $R^K_{\mathrm{out}}$ |
| $(K^+)^\circ$ | $\Gamma_K$ | $r_-$, $R^K_{\mathrm{out}}$ |

In the order $\{t_* = 1\}$, $\partial R_{\mathcal H^+}$, $\partial R_{\mathscr I^+,\mathrm{in},+}$, $\partial
R_{\partial K^+,\mathrm{in}}$, $\partial\Gamma_{K^+}$, $\partial R_{\partial K^+,\mathrm{out}}$, $\{r<r_0-\delta_0\}$,
$\partial R_{\mathscr I^+,\mathrm{out}}$, every curve goes from an earlier set to a later one, as in [Hin26c] Figure 4.3;
with Proposition 8.2 below this holds for every curve over $\Omega$.

*Proof.* $(1.4)$ is a b-vector field on ${}^{e3b}S^*M$, so it is tangent to every boundary hypersurface, and each open
stratum of the boundary is invariant: $(\mathscr I^+)^\circ$, $\mathscr I^+\cap\iota^+$, $(\iota^+)^\circ$, $\partial K^+
= K^+\cap\iota^+$ and $(K^+)^\circ$ (within $\Omega$). Over $(K^+)^\circ$ and $\partial K^+$: Proposition 6.1. Over
$(\iota^+)^\circ$: Lemma 3.2 (b), with the ends at $u = 0$ identified by Lemma 7.3; case (i) of Lemma 3.2 (b) is the
fourth row, (ii) and (iii) the third. Over $\mathscr I^+$: Lemma 7.2 (1). $\square$

**Proposition 8.2 (curves over the interior; [Hin26c] Proposition 6.1 for the stationary model).** Let $\gamma$ be a
maximal integral curve of (1.4) in $\partial\Sigma^+$ over $M^\circ\cap\Omega\cap\{r>r_0-\delta_0\}$, extended maximally
within $\{r>r_0-2\delta_0\}\cap\Omega$. Then $\gamma$ reaches $\{t_* = 1\}$ backward at a finite parameter, and forward
either reaches $\{r<r_0-\delta_0\}$ at a finite parameter or tends to the e3b-cosphere bundle over $(\mathscr I^+\cap
\Omega)\cup\iota^+\cup K^+$: over $\iota^+\cup K^+$ if $t_*\to\infty$ along $\gamma$, over $\mathscr I^+$ otherwise.

*Proof.* On $\partial\Sigma^+$ over $M^\circ$, $\rho_\infty H_Gt_* = 2\rho_\infty g^{-1}(\nu,dt_*)>0$ for the null
covectors $\nu$ there (Lemma 1.2 (c)), so (1.4) increases $t_*$, at a rate bounded below by a positive constant on
compact subsets of $\partial\Sigma^+$ over $M^\circ\cap\{r>r_0-2\delta_0\}$. On $\{r<r_2\}$, $H_Gr = 2g^{-1}(\nu,dr)<0$
for future null $\nu$, as $dr$ is future timelike there ((H4); I.B section 1.2: $\nabla r$ is future timelike, so
$\nu(\nabla r)<0$); so backward $r$ increases while $r<r_2$, and $\gamma$ cannot leave through $\{r = r_0-2\delta_0\}$
backward. The faces at infinity are invariant, so $\gamma$ is defined until it reaches $\{t_* = 1\}$ or
$\{r<r_0-\delta_0\}$.

*Forward.* If $t_*\to\infty$, every limit point lies over $\{t_* = \infty\}\cap\Omega = \iota^+\cup K^+$. If $t_*$ stays
bounded and $\gamma$ does not reach $\{r<r_0-\delta_0\}$, then $\sup I = \infty$, and a limit point $p$ over $M^\circ$
would be visited infinitely often, each visit to a fixed small neighbourhood of $p$ lasting a parameter time bounded
below (the field is bounded) and increasing $t_*$ by a fixed amount: so $t_*\to\infty$, a contradiction. The limit points
therefore lie over $\partial\tilde M$ at finite $t_*\ge1$, which within $\Omega$ is $\mathscr I^+$.

*Backward.* Suppose $\gamma$ does not reach $\{t_* = 1\}$; then $\inf I = -\infty$ and $t_*\downarrow L\ge1$. As above,
no limit point lies over $M^\circ$, so the $\alpha$-limit set $\mathcal A$ lies over $\mathscr I^+\cap\{t_* = L\}$; it is
non-empty, compact and invariant, and $\rho_+ = L^{-1}$ on it. A curve in $\mathcal A$ has $\rho_+$ constant, hence
$\hat\xi = 0$ by (7.5) ($\rho_+>0$), hence $\hat\eta = 0$: $\mathcal A\subset\partial R_{\mathscr I^+,\mathrm{out}}$.
Near $\partial R_{\mathscr I^+,\mathrm{out}}$, $\mathsf Hx_I = (\hat\xi-1)x_I+O(x_I^3)\le-\frac12x_I$, so on a tail
$(-\infty,s_1]$ of $\gamma$ the function $x_I\circ\gamma>0$ increases as $s$ decreases and cannot tend to 0, a
contradiction. $\square$

*Remark 8.3 ([Hin26c] Remark 4.25).* The sets of Propositions 8.1-8.2 that depend on the stationary model are $\partial
R_{\mathcal H^+}$, through $\mathcal R_+$, and $\partial\Gamma_{K^+}$, through $\Gamma$. Under (H5), extended to
(H6)-(H8) in I.B, and (K4), both depend continuously on the parameter $b$, with the constants of Lemma 4.2 and of (K3)
uniform; the radial sets over $\partial K^+$ and $\mathscr I^+$ do not depend on $b$.

## 9. What this part found

(B1) *[Hin26c] Lemma 4.6 (2), proof.* Under $\frac d{ds}\rho_+(\gamma(0))\le0$, part (1) makes $\rho_+\circ\gamma$
strictly *decreasing* for $s>0$ (a critical point is a strict local maximum); the proof says "strictly increasing". The
argument is otherwise as stated; Lemma 3.3 (2) gives it in full, including why $\rho_+\to0$.

(B2) *[Hin26c] Lemma 4.6 (4).* The conic extension of $\partial W^+_{\mathrm{in}} = \{\hat\xi_{3b} = 2\}$ is $\{\xi_{3b}
= 2\sigma_{3b}\}$, printed as $\xi_{3b} = -2\sigma_{3b}$, and within $\Sigma^+$ it is the characteristic set of
$2r\partial_{t_*}-r\partial_r = r(\partial_t-\partial_r)$, printed as $r\partial_{t_*}-2r\partial_r$. The source's
$(t,r)$-form $r(\partial_t-\partial_r)$ is right.

(B3) *[Hin26c] (4.18).* $2\rho_+\mathsf H\hat\xi = -4\rho_+(1+O(\epsilon))$, printed with $-2$. The sign, which is all
that is used, is right.

(B4) *[Hin26c] Lemma 4.20.* Its proof bounds $D\varphi\circ De^{s'V_1}$ by the hypothesis, which bounds only $f\circ
De^{s'V_1}$, and its last step $e^{\lambda\psi}\le e^{\lambda se^{\sup\varphi}}$ needs $\lambda\ge0$. In the source's one
use, the proof of its Proposition 4.19 (3), both hold: every component of $De^{sV_1}v$ grows subexponentially there and
$\lambda = \epsilon>0$. Not used here.

(B5) *The rate at $n = 4$.* (K1) has $r^{-2}$ where Kerr has $r^{-1}$, and no logarithm enters the hyperboloidal time.
The error classes improve accordingly: (1.2) has $\rho_0^2x_I^2\rho_+^2$ for the source's $\rho_0x_I^2\rho_+$;
$H_{G_{3b}}- H_{\bar G_{3b}}\in\rho_+^2\mathcal V_b$; $G_{eb}-\bar G_{eb}\in x_I^2\rho_+^2P^{[2]}$. Nothing uses more
than the source's rates except the shortened proofs of Lemma 3.3 (1)-(2).

(B6) *[Hin26c] (4.67) and (2.27).* The angular coefficient 1 in $G^0_{eb}$ follows from the angular term
$\frac{\slashed g}{2x_I^2}$ of II.A's corrected form of (2.27) (II.A section 10); the printed $\frac{\slashed g}{x_I^2}$
would give $\frac12|\eta_{eb}|^2$. (4.67) is therefore consistent with the correction, and (7.1) is computed directly.

(B7) *Changes of statement, not of substance.* The Kerr computations of [Hin26c] Lemmas 4.1-4.3, 4.7, 4.10-4.18 and
Proposition 4.19 are replaced by the hypotheses (H3), (H4), (H7), (H8) of Part I and (K3), from which section 2 recovers
the dynamics over the Kerr face; Part VI checks them for the record's metrics. The first row of [Hin26c] (4.72), curves
over $M^\circ$, is replaced by Proposition 8.2, the form the source states as its Proposition 6.1 and uses later (it says
on p. 111 that the finer statement is not needed). Whether the later parts use more of section 4 than Propositions 6.1,
8.1, 8.2, Lemmas 3.3, 4.2, 5.2, 7.2 and (K3) is checked where they are written (Parts II.C-II.F).

## Sources

[Hin26c] P. Hintz, *(Non-)linear waves on asymptotically flat spacetimes. II*, arXiv:2606.28008v1. READ: pp. 77-99
(section 4: Lemmas 4.1-4.23, Definitions 4.5, 4.8, 4.13, 4.15, 4.17, 4.22, Propositions 4.19, 4.21, 4.24, Remark 4.25,
(4.11)-(4.17), (4.63)-(4.72)), pp. 110-113 (Propositions 6.1, 6.3).

[HPS77] M. W. Hirsch, C. C. Pugh, M. Shub, *Invariant manifolds*, Lecture Notes in Math. 583 (1977). Cited for the
definition in (K3), as the source cites it; not READ here.

Part I.A: section 1 ((H1)-(H5)), Lemma 4.1, Lemmas 4.4-4.5 ((4.4)-(4.7)). Part I.B: sections 1.2-1.5 ((H6)-(H8), Lemma
1.1), 2.4 ($\mathcal P$), Lemma 4.1. Part II.A: sections 1-2 (coordinates, Definitions 2.1, 2.4, 2.8, Lemmas 2.5 and
2.10, (2.1)-(2.2)), section 10.

Standard facts used by name: existence and uniqueness for ordinary differential equations, the solution of linear
first-order equations, and the $\alpha$- and $\omega$-limit sets of a curve in a compact metric space (non-empty,
compact, connected, invariant).
