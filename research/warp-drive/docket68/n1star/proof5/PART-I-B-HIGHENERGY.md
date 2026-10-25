# Part I.B. The spectral family at high frequencies, at n = 4, on bundles

*Status.* Written out in full (D188). Not yet read by an independent verifier; nothing here is labelled proved. This
part replaces, for the statements it covers, the deductions of `../N1STAR-PROOF.md` 10.84 and 10.86 that re-ran
[Hin26c] section 9.3 on bundles at proof level. The source is [Hin26c] = P. Hintz, arXiv:2606.28008v1. Part I.A is
`PART-I-SPECTRAL.md`; its sections are cited as I.A section 4.5, I.A Theorem 7.2, and so on.

*What is proved here.* Theorem 1.3: [Hin26c] Theorem 9.16 at $n = 4$, for operators on a trivial bundle of any rank,
with constants uniform in the operator (section 9). As in Part I.A the regularity order is constant (I.A Remark 1.1);
the decay and semiclassical orders may vary. Every input is proved here or in Part I.A, except the facts of Fourier
analysis used in section 2 and the statements of [HJS] that Part I.A READ. In particular the semiclassical calculus,
for which no text could be READ, is proved in section 2.

*How it is organised.* Section 1 fixes the hypotheses and states the theorem. Section 2 proves the calculus. Section 3
gives the positive commutator scheme, which here needs no regularisation. Sections 4-7 prove the estimates: real
principal type, radial points, the trapped set, and the artificial boundary. Section 8 proves the theorem and section 9
its uniformity. Section 10 lists what the write-out found.

## 1. Setting, hypotheses and the theorem

### 1.1 Data from Part I.A

The space $\bar X\subset\overline{\mathbb R^4}$, the radii $r_0,\delta_0,r_2,r_h$, the bundle $E = \tilde X\times
\mathbb C^N$, fibre inner products $h = \langle H\cdot,\cdot\rangle$ and $h$-adjoints $A^{*h} = H^{-1}A^*H$, and the
family $\hat P(\sigma) = \hat P(0)+\sigma T+\sigma^2P_2$ are those of I.A section 1, and (H1)-(H5) are assumed. We
write $\rho = |x|^{-1}$ near $\partial X$, scattering covectors as $\xi\,dr+r\eta$, and use I.A Lemma 4.4: at the
boundary face $T$ has principal symbol $2\xi\,\mathrm{Id}$, and
$\mathrm{Im}_hT = -\rho(S+S^{*h})+T_2$ with $T_2\in\Psi^{1,-2}$.

### 1.2 The Lorentzian structure

(H6) (*[Hin26c] Definitions 9.3-9.4.*) There is a smooth Lorentzian metric $g$ on $\mathbb R_t\times\tilde X^\circ$,
of signature $(1,4)$, with $t$-independent components, such that for $\zeta\in T^*\tilde X^\circ$

$$G_0(\zeta) = g^{-1}(\zeta,\zeta),\qquad\tau_1(\zeta) = -2g^{-1}(dt,\zeta),\qquad g_{00} = g^{-1}(dt,dt).\tag{1.1}$$

$g_{00}\le0$ everywhere and $g_{00}<0$ on $\tilde X^\circ$: $dt$ is timelike; we time-orient $g$ so that $-\nabla t$ is
future directed ("$dt$ is past timelike" in [Hin26c]). Thus $G(-\sigma\,dt+\zeta) := g^{-1}(-\sigma\,dt+\zeta,
-\sigma\,dt+\zeta) = G_0(\zeta)+\sigma\tau_1(\zeta)+\sigma^2g_{00}$ is the principal symbol of $\hat P(\sigma)$ jointly
in $(\sigma,\zeta)$. The stationary operator $P_0 := \hat P(0)+T\,i\partial_t-P_2\partial_t^2$ satisfies $P_0(e^{-i\sigma
t}v) = e^{-i\sigma t}\hat P(\sigma)v$, and $P_0-\square_g\mathrm{Id}$ is a first order operator with $t$-independent
coefficients, where $\square_g := -\nabla^\mu\nabla_\mu$ acts componentwise.

On $\{r_0-2\delta_0<r<r_2\}$, (H4) gives $G_0(dr)<0$: $dr$ is timelike for $g$ as a covector annihilating $\partial_t$,
and the future direction decreases $r$. Write $X := \nabla r = g^{-1}(dr,\cdot)$; it is a future directed timelike
vector field there (I.A section 6.2, where $\mathfrak g^{-1}$ is the restriction of $g^{-1}$ to $T^*\tilde X$).

### 1.3 The semiclassical family

For $h\in(0,1]$ and $z\in\mathbb C$, $|z|\in[\frac12,2]$, put $\sigma := z/h$ and

$$P_{h,z} := h^2\hat P(z/h) = h^2\hat P(0)+hzT+z^2g_{00}\,\mathrm{Id}.\tag{1.2}$$

**Lemma 1.1 ([Hin26c] Lemmas 9.20-9.21 on $E$).** Fix a fibre inner product $h$.
(a) $P_{h,z} = \mathrm{Op}_h(p_{h,z})$ on $\tilde X^\circ$, with $p_{h,z}$ a polynomial of degree 2 in $\zeta$ whose
coefficients are smooth on the compactification near $\partial X$; its principal symbol, modulo
$S^{1,-1,-1}$, is $G_z\,\mathrm{Id}$ with $G_z(x,\zeta) := G(-z\,dt+\zeta)$.
(b) Exactly,

$$h^{-1}\mathrm{Im}_hP_{h,z} = \mathcal P_1(z)-\frac{\mathrm{Im}\,z}h\,\mathcal Q,\qquad\mathcal P_1(z) := h\,
\mathrm{Im}_h\hat P(0)+(\mathrm{Re}\,z)\,\mathrm{Im}_hT,\qquad\mathcal Q := -h\,\mathrm{Re}_hT-2(\mathrm{Re}\,z)g_{00}.
\tag{1.3}$$

$\mathcal P_1(z)$ and $\mathcal Q$ are $h$-self-adjoint semiclassical differential operators of order 1. The principal
symbol of $\mathcal Q$ is $q_z\,\mathrm{Id}$, $q_z(\zeta) := -\tau_1(\zeta)-2(\mathrm{Re}\,z)g_{00} =
2g^{-1}(-(\mathrm{Re}\, z)dt+\zeta,dt)$, and that of $\mathcal P_1(z)$ is $p_1(z) := \sigma_1(\mathrm{Im}_h\hat
P(0))(\zeta)+(\mathrm{Re}\,z) \sigma_0(\mathrm{Im}_hT)$, an $h$-self-adjoint endomorphism. (c) $\mathrm{Re}\,G_z =
G_{\mathrm{Re}\,z}-(\mathrm{Im}\,z)^2g_{00}$ and $\mathrm{Im}\,G_z = -(\mathrm{Im}\,z)q_z$. (d) If $\mathrm{Im}\,z>0$,
then $G_z\ne0$ on $T^*\tilde X^\circ$: the characteristic set of $P_{h,z}$ over $\tilde X^\circ$ lies at fibre infinity.
(e) For $z_0\in\{1,-1\}$, $q_{z_0}\ne0$ on $\Sigma_{z_0} := \{G_{z_0} = 0\}\subset T^*\tilde X^\circ$, and $\rho_\infty
q_{z_0}\ne0$ on its boundary $\partial\Sigma_0$ at fibre infinity. We write $\Sigma^\pm_{z_0} := \Sigma_{z_0}\cap\{\pm
q_{z_0}>0\}$; at fibre infinity this labelling agrees with that of (H3)-(H4).

*Proof.* (a) $h^2\hat P(0)$ is a semiclassical scattering differential operator with principal symbol $G_0(\zeta)$
([Hin26c] (3.37)); $hT$ has semiclassical symbol $\tau_1(\zeta)$ plus $h$ times an order-0 symbol; $z^2g_{00}$ is
order 0. At the boundary face the lower terms gain $\rho$ (I.A Lemma 4.4). (b) $\mathrm{Im}_h(cA) = (\mathrm{Re}\,c)
\mathrm{Im}_hA+(\mathrm{Im}\,c)\mathrm{Re}_hA$, $g_{00}\mathrm{Id}$ is $h$-self-adjoint, and $\mathrm{Im}(z^2) =
2\,\mathrm{Re}\,z\,\mathrm{Im}\,z$: $h^{-1}\mathrm{Im}_hP_{h,z} = h\,\mathrm{Im}_h\hat
P(0)+(\mathrm{Re}\,z)\mathrm{Im}_hT+(\mathrm{Im}\,z)\mathrm{Re}_hT+ 2h^{-1}\mathrm{Re}\,z\,\mathrm{Im}\,z\,g_{00}$,
which is (1.3). $\mathrm{Re}_hT$ has principal symbol $\tau_1$ (by (H1)), so $h\,\mathrm{Re}_hT$ has semiclassical
principal symbol $\tau_1(\zeta)$; $\mathrm{Im}_hT$ has order 0; $\mathrm{Im}_h\hat P(0)$ has order 1 (I.A Remark (a)).
(c) Expand $G(-(\mathrm{Re}\,z+i\,\mathrm{Im}\,z)dt+\zeta)$. (d) If $\mathrm{Re}\,G_z = 0$ then
$G(-(\mathrm{Re}\,z)dt+\zeta) = (\mathrm{Im}\,z)^2g_{00}<0$, so $\nu := -(\mathrm{Re}\,z)dt+ \zeta$ is timelike, hence
$g^{-1}(\nu,dt)\ne0$ ($dt$ is timelike, and two timelike covectors are never orthogonal), and $\mathrm{Im}\,G_z =
-2(\mathrm{Im}\,z)g^{-1}(\nu,dt)\ne0$. (e) A nonzero null covector is not orthogonal to the timelike $dt$; at fibre
infinity the same holds for the null covectors $\zeta\in T^*\tilde X^\circ$ with $G_0(\zeta) = 0$, and $q_{z_0}$ is
$-\tau_1$ plus a term of lower degree. (H3) gives $\mp\tau_1>0$ on $\partial\mathcal R_\pm$, so the component of
$\partial\Sigma_0$ containing $\partial\mathcal R_\pm$ is the one on which $\pm q>0$. $\square$

The *future-directed* field on $\Sigma^\pm_{z_0}$ is $\pm H_{G_{z_0}}$ (rescaled, $\pm\rho_\infty H_{G_{z_0}}$, near
fibre infinity). Where $\partial_t$ is future directed timelike, a null $\nu = -z_0dt+\zeta$ has $\nu(\partial_t) =
-z_0$, so $\nu^\sharp$ is future directed iff $z_0>0$, and $q_{z_0} = 2\nu(\nabla t)$ then has the sign of $z_0$, as
$-\nabla t$ is future directed: only the component $\Sigma^{z_0}_{z_0}$ occurs away from an ergoregion ([Hin26c] footnote
80).

### 1.4 Orders and thresholds

*Orders.* $s\in\mathbb R$ is constant. A *decay order* $\mathsf r$ and a *semiclassical order* $\mathsf b$ are orders in
the sense of section 2.1 that are smooth on the compactified phase space $\mathcal P$ of section 2.4. Let
$z_0\in\{1,-1\}$, let $\mathsf H_{z_0}$ be the rescaled Hamilton field of section 4.1 and $\hat q_{z_0} :=
\langle\zeta\rangle^{-1}q_{z_0}$, and on $\{\hat q_{z_0}\ne0\}$ put $\mathsf H^\natural := \mathrm{sgn}(\hat
q_{z_0})\mathsf H_{z_0}$, the future field of section 1.3. $\mathsf r$ is *admissible for $z_0$ with weight $\alpha_+$*
if it is constant near $R_{z_0,\mathrm{in}}$ and near $R_{\mathrm{out}}$, if there is a neighbourhood $W$, within the
face over $\partial X$, of the characteristic set $\Sigma^\partial_{z_0}$ there, with $\mathsf H^\natural\mathsf r\le0$
on $W\cap\{\hat q_{z_0}\ne0\}$, and if $\mathsf r+\alpha_+>\frac12(-1+\vartheta_{\mathrm{in}})$ at $R_{z_0,\mathrm{in}}$
and $\mathsf r+\alpha_+<-\frac12+\bar S$ at $R_{\mathrm{out}}$ (each in the fibre inner product of (O3), up to any
margin; Propositions 5.3 and 5.5). $\mathsf b$ is *admissible for $z_0$* if it is constant near $\partial\mathcal R_\pm$,
near $\Gamma_{z_0}$ of (H7), near $R_{z_0,\mathrm{in}}$ and $R_{\mathrm{out}}$, and over $\{r_0-\delta_0\le r\le
r_2-\delta_0\}$ ([Hin26c] footnote 78), and if there is a neighbourhood $W$ of $\Sigma_{z_0}$ in $\mathcal P$ with
$\mathsf H^\natural\mathsf b\le0$ on $W\cap\{\hat q_{z_0}\ne0\}$. Constant orders are admissible. The monotonicity is
asked on a neighbourhood of the characteristic set, not on the set alone: Proposition 4.5 needs it on the support of a
commutant, where the factor $\log\frac1h$ multiplies $\mathsf H\mathsf b$. It is stronger than I.A (O2), so $\mathsf
r_h(x,\xi) := \mathsf r(x,h\xi)$ satisfies I.A (O2)-(O3) at $\sigma_0 = z_0/h$ (section 8.4).

*Thresholds.* $\vartheta_{\mathcal H}$, $\vartheta_{\mathrm{in}}$ and $\bar S$ are those of I.A (1.5), each computed in a
fibre inner product chosen for its radial set. The regularity order satisfies $s>\frac12+\vartheta_{\mathcal H}$.

### 1.5 The trapped set and the global dynamics

(H7) (*Normally hyperbolic trapping, [Hin26c] (Γ.1)-(Γ.4) on $E$.*) For $z_0\in\{1,-1\}$ write $\Sigma^\flat_{z_0} :=
\Sigma^{z_0}_{z_0}$ and $\mathsf H_{z_0} := z_0H_{G_{z_0}}$, the future field on it. There are a compact set $\Gamma =
\Gamma_{z_0}\subset\Sigma^\flat_{z_0}\cap T^*\{r_2<r<\rho_1^{-1}\}$, a neighbourhood $O$ of $\Gamma$ and real functions
$\phi_u,\phi_s\in C^\infty(O)$ such that, with $\Gamma_{u/s} := \{\phi_{u/s} = 0\}\cap\Sigma^\flat_{z_0}\cap O$: (Γ.1)
$\Gamma_u$, $\Gamma_s$ are smooth hypersurfaces of $\Sigma^\flat_{z_0}$ meeting transversally in $\Gamma$, and $\mathsf
H_{z_0}$ is tangent to both; (Γ.2) $\mathsf H_{z_0}\phi_u = -\nu_u\phi_u$ and $\mathsf H_{z_0}\phi_s = \nu_s\phi_s$ on
$\Sigma^\flat_{z_0}\cap O$, with $\nu_{\min} := \min(\inf_\Gamma\nu_u,\inf_\Gamma\nu_s)>0$; (Γ.3) $\{\phi_u,\phi_s\}>0$
and $dG_{z_0}\ne0$ on $\Gamma$; (Γ.4) with $\beta_0 := \frac12\min_\Gamma|q_{z_0}|>0$, a fibre inner product $h_\Gamma$,
$p_1^\Gamma := z_0\,p_1(z_0)|_\Gamma$ (an $h_\Gamma$-self-adjoint endomorphism) and $q^\Gamma :=
z_0q_{z_0}|_\Gamma\ge2\beta_0$, the function $f(\eta) := \sup_{\varpi\in\Gamma}\lambda_{\max}(p_1^\Gamma(\varpi)-\eta
q^\Gamma(\varpi))$ is continuous and decreases at least at the rate $2\beta_0$; let

$$f(\gamma_+) = 0,\qquad f(\gamma_-) = \tfrac12\nu_{\min},\qquad\delta_\Gamma(\eta) :=
\min\Big(1,\max\Big(\frac{\gamma_+-\eta}{\gamma_+-\gamma_-},0\Big)\Big)\in[0,1],\tag{1.4}$$

and assume $\gamma_-<0$, that is, $\sup_\Gamma\lambda_{\max}(p_1^\Gamma)<\frac12\nu_{\min}$. Then $\gamma_-<\gamma_+$.

The factors $z_0$ make (1.4) the same for both signs: the future field on $\Sigma^\flat_{z_0}$ is $z_0H_{G_{z_0}}$, and
section 6 works with $z_0p_1$ and $z_0q$ throughout. For $z_0 = 1$, scalar operators and $q_{z_0}$ constant on $\Gamma$,
(1.4) is [Hin26c] (9.79)-(9.81); in general $\gamma_\pm$ are the exact thresholds that the proof uses, and $\gamma_-<0$
is what Theorem 1.3 (1) needs at $\mathrm{Im}\,z = 0$ (section 10, (F4)-(F5)).

(H8) (*Global dynamics, [Hin26c] section 9.1.2.*) For $z_0\in\{1,-1\}$ and every maximal integral curve $\gamma$ of the
future field in $\Sigma_{z_0}\cap T^*\{r>r_0-2\delta_0\}$ (finite covectors): if $\gamma\not\subset\Gamma_u$, then
$\gamma(t)$ tends, as $t\to-\infty$, to $\partial\mathcal R_+\cup\partial\mathcal R_-$ (at fibre infinity) or to
$R_{z_0,\mathrm{in}}$ (over $\partial X$); and if $\gamma\not\subset\Gamma_s$, then as $t$ increases $\gamma$ either
tends to $R_{\mathrm{out}}$ or reaches $\{r<r_0-\delta_0\}$ in finite time. Here "tends to" is in $\mathcal P$, and the
convergence is uniform on compact sets of initial points away from $\Gamma_u$ (resp. $\Gamma_s$). Together with (H4) at
fibre infinity and I.A Lemma 4.5 over $\partial X$, this describes the flow on the whole characteristic set.

(H5) is extended to (H6)-(H8): $g$, $\Gamma$, $\phi_{u/s}$, $\nu_{u/s}$ and $h_\Gamma$ may depend continuously on the
parameter $b\in\mathcal B$ (into $C^\infty$), with $\nu_{\min}$, $\beta_0$, $\gamma_\pm$ and the convergence in (H8)
uniform. For the record's operators these hypotheses are checked in Part VI from the record's computed items (10.19,
10.36, 10.60); they are not checked here.

### 1.6 The spaces and the theorem

With the semiclassical Sobolev spaces $H^{s,\mathsf r,\mathsf b}_h$ of section 2.3 on $\mathbb R^4$, let
$\bar H^{s,\mathsf r,\mathsf b}_h$ and $\dot H^{s,\mathsf r,\mathsf b}_h$ be their extendible and supported versions at
$\partial_\sharp X$ (I.A section 6.1, with the quotient norm, resp. the induced norm; the constructions there are
local at $\partial_\sharp X$ and do not see $h$). For $k\in\mathbb N_0$, let
$\bar H^{(s;k),\mathsf r,\mathsf b}_h$ be the space of $u$ with $(\langle x\rangle D_x)^\alpha u\in\bar H^{s,\mathsf r,
\mathsf b}_h$ for $|\alpha|\le k$, normed by the sum, and ([Hin26c] (9.58))

$$\|u\|_{(s;k),\mathsf r,\mathsf b;+} := \sum_{j=0}^kh^{-j}\|u\|_{\bar H^{(s;k-j),\mathsf r,\mathsf b}_h}.\tag{1.5}$$

**Theorem 1.3 ([Hin26c] Theorem 9.16, at $n = 4$ on $E$).** Assume (H1)-(H8). Let $\alpha_+\in\mathbb R$,
$z_0\in\{1,-1\}$, $s>\frac12+\vartheta_{\mathcal H}$, and let $\mathsf r$, $\mathsf b$ be admissible for $z_0$, the
first with weight $\alpha_+$. Write $\mathbf o := (s,\mathsf r+\alpha_+,\mathsf b)$ and $\mathbf o' := (s-1,\mathsf r+
\alpha_++1,\mathsf b)$.

(1) (*High-energy estimates, I.*) For $\nu\ge0$ there are $C$, $h_0>0$ such that for $z\in z_0+i[0,\nu]$ and
$h\in(0,h_0)$,

$$\|u\|_{\bar H^{\mathbf o}_h}\le Ch^{-2}\|P_{h,z}u\|_{\bar H^{\mathbf o'}_h},\qquad\|v\|_{\dot H^{-\mathbf o'}_h}\le
Ch^{-2}\|P^{*h}_{h,z}v\|_{\dot H^{-\mathbf o}_h},\tag{1.6}$$

for $u\in\bar H^{\mathbf o}_h$ with $P_{h,z}u\in\bar H^{\mathbf o'}_h$, and $v\in\dot H^{-\mathbf o'}_h$ with
$P^{*h}_{h,z}v\in\dot H^{-\mathbf o}_h$.

(2) (*High-energy estimates, II.*) For $\nu'>0$, (1.6) holds for $|z|\in[\frac12,2]$, $\mathrm{Im}\,z\ge\nu'$ and
$h\in(0,h_0)$, for every decay order $\mathsf r$ constant near $R_{\mathrm{out}}$ with $\mathsf r+\alpha_+<-\frac12+
\bar S$ there, and every constant $\mathsf b$.

(3) (*Invertibility.*) There is $C_0$ such that $\hat P(\sigma) : \mathcal X_\sigma\to\mathcal Y_\sigma$ (I.A Theorem
7.2) is invertible for every $\sigma$ with $\mathrm{Im}\,\sigma\ge0$ and $|\sigma|\ge C_0$, the orders at $\sigma$ being
those of (1) or (2) read at $h = |\mathrm{Re}\,\sigma|^{-1}$, resp. $h = |\sigma|^{-1}$ (section 8.4).

(4) (*Smaller losses; b-regularity.*) For $z,h_0$ as in (1) or (2), $k\in\mathbb N_0$ and $\epsilon>0$ there is $C$
with

$$\|u\|_{(s;k),\mathsf r+\alpha_+,\mathsf b;+}\le Ch^{-1-\delta_\Gamma(\mathrm{Im}(z/h)-\epsilon)}
\|P_{h,z}u\|_{(s-1;k),\mathsf r+\alpha_++1,\mathsf b;+}.\tag{1.7}$$

(5) (*Regularity in the spectral parameter.*) For $\sigma$ as in (3) and $j,k\in\mathbb N_0$, $\epsilon>0$, the inverse
$\hat P(\sigma)^{-1}$ is $j$ times differentiable along $\sigma\partial_\sigma$, and with $h := |\sigma|^{-1}$ and
$\delta := \delta_\Gamma(\mathrm{Im}\,\sigma-\epsilon)$,

$$\|(\sigma\partial_\sigma)^j\hat P(\sigma)^{-1}f\|_{(s+j;k),\mathsf r+\alpha_+,\mathsf b;+}\le
C|\sigma|^{-1+(j+1)\delta}
\|f\|_{(s-1;k+j),\mathsf r+\alpha_++1,\mathsf b;+}.\tag{1.8}$$

This is [Hin26c] Theorem 9.16 with $n = 4$; the two changes from the source are that the regularity order is constant
and that the hypotheses are stated for the spectral family on $E$. For $\mathrm{Im}(z/h)$ large, $\delta_\Gamma = 0$.

*Remark 1.4.* In (1), $h^{-2}$ is the case $k = 0$ of (1.7) with $\delta_\Gamma\le1$; we prove (4) and the adjoint half
of (1), and (1)-(2) follow. Both signs of $z_0$ are treated together: estimates for $P$ propagate along $\varsigma\mathsf
H$ with $\varsigma = \mathrm{sgn}\,q$ (section 4.4), the future field on each component, which for $z_0 = -1$ on
$\Sigma^\flat_{z_0}$ is $-H_{G_{-1}}$ rescaled.

## 2. The semiclassical scattering calculus

The high-energy estimates need the semiclassical scattering calculus of Vasy and Zworski. [Hin26c] (3.33)-(3.36)
defines it and refers to [VZ00] and [Hin25a] section 6.6; [HJS] treats only the non-semiclassical calculus; and no
text stating the semiclassical calculus with matrix-valued symbols and variable orders could be READ here (the proxy
refuses the publishers' and authors' sites). So it is proved in this section, on $\mathbb R^n$ for every $n\ge1$,
from Fourier analysis, integration by parts and Schur's test. The proofs are the standard ones.

Throughout, $h\in(0,1]$, matrices are $N\times N$ with the operator norm $|\cdot|$, and a *family* is a map
$h\mapsto a_h$; estimates are uniform in $h$. Put $L_h(x,\zeta) := 1+\log\langle x\rangle+\log\langle\zeta\rangle+
\log(1/h)$.

### 2.1 Symbols and orders

An *order* is a real function $\mathsf o$ on $\mathbb R^n_x\times\mathbb R^n_\zeta$, independent of $h$, with
$|\partial_x^\alpha\partial_\zeta^\beta\mathsf o|\le C_{\alpha\beta}\langle x\rangle^{-|\alpha|}\langle\zeta\rangle^
{-|\beta|}$. Every function smooth on $\overline{\mathbb R^n}\times\overline{\mathbb R^n}$ (the product of the radial
compactifications) is an order, since derivatives of a smooth function of $(\langle x\rangle^{-1},x/\langle x\rangle)$
gain $\langle x\rangle^{-1}$, and likewise in $\zeta$. For orders $s,\mathsf r,\mathsf b$ put

$$w_{s,\mathsf r,\mathsf b}(x,\zeta) := \langle\zeta\rangle^{s(x,\zeta)}\langle x\rangle^{\mathsf r(x,\zeta)}
h^{-\mathsf b(x,\zeta)}:$$

$s$ is the regularity order, $\mathsf r$ the decay order and $\mathsf b$ the semiclassical order, as in [Hin26c] (3.33).
We write $\mathbf o = (s,\mathsf r,\mathsf b)$, $w_{\mathbf o}$, and $\mathbf 1 := (1,1,1)$.

**Definition 2.1.** $S^{\mathbf o}$ is the space of families of smooth $a_h:\mathbb R^{2n}\to\mathbb C^{N\times N}$ with
$|a_h|\le Cw_{\mathbf o}$ and, for each $(\alpha,\beta)\ne0$, constants $C_{\alpha\beta}$, $\mu_{\alpha\beta}\ge0$ with

$$|\partial_x^\alpha\partial_\zeta^\beta a_h(x,\zeta)|\le C_{\alpha\beta}\,w_{\mathbf o}(x,\zeta)\,\langle x
\rangle^{-|\alpha|}\langle\zeta\rangle^{-|\beta|}L_h(x,\zeta)^{\mu_{\alpha\beta}}.\tag{2.1}$$

The best constants with $|\alpha|+|\beta|\le k$ (and fixed exponents) are the seminorms. $S^{-\infty} :=
\bigcap_KS^{-K\mathbf 1}$. Note $h^KS^{\mathbf o} = S^{\mathbf o-(0,0,K)}$.

**Lemma 2.2.** For orders $\mathbf o,\mathbf o'$: (a) $w_{\mathbf o}\mathrm{Id}\in S^{\mathbf o}$, and $w_{\mathbf
o}^{-1} = w_{-\mathbf o}$. (b) $S^{\mathbf o}S^{\mathbf o'}\subset S^{\mathbf o+\mathbf o'}$. (c) If $\mathbf o\le\mathbf
o'$ pointwise in each component, $S^{\mathbf o}\subset S^{\mathbf o'}$. (d) For $a\in S^{\mathbf o}$ and $\epsilon>0$,
$\partial_x^\alpha\partial_\zeta^\beta a\in S^{\mathbf o-(|\beta|,|\alpha|,0)+ \epsilon\mathbf 1}$. (e) If $a\in
S^{\mathbf o}$, $U$ is open, and for $h<h_0$, $a_h$ is invertible on $U$ with $|a_h^{-1}|\le Cw_{\mathbf o}^{-1}$, then
$\phi\,a^{-1}\in S^{-\mathbf o}$ for every $\phi\in S^{0}$ supported in $U$ (and set to 0 for $h\ge h_0$).

*Proof.* (a) $\log w = s\log\langle\zeta\rangle+\mathsf r\log\langle x\rangle+\mathsf b\log(1/h)$. A derivative of $\log
w$ falls on an order, gaining that variable's weight and leaving one logarithm, or on $\log\langle\cdot\rangle$, whose
derivatives of order $k\ge1$ are $O(\langle\cdot\rangle^{-k})$. So for $(\alpha,\beta)\ne0$,
$|\partial_x^\alpha\partial_\zeta^\beta\log w|\le C\langle x\rangle^{-|\alpha|}\langle\zeta\rangle^{-|\beta|}L_h$. By the
chain rule $\partial^\gamma w$ is $w$ times a sum of products of such derivatives with multi-indices adding to $\gamma$.
(b) Leibniz, as $w_{\mathbf o}w_{\mathbf o'} = w_{\mathbf o+\mathbf o'}$. (c) $w_{\mathbf o}\le w_{\mathbf o'}$. (d)
$L_h^\mu\le C_{\mu,\epsilon}\langle x\rangle^\epsilon\langle\zeta\rangle^\epsilon h^{-\epsilon}$. (e) The derivatives of
$a^{-1}$ are sums of products $a^{-1}(\partial^{\gamma_1}a)a^{-1}\cdots(\partial^{\gamma_k}a)a^{-1}$. $\square$

### 2.2 Quantisation, composition, adjoints

For $a\in S^{\mathbf o}$ and $u\in\mathcal S(\mathbb R^n;\mathbb C^N)$,

$$\mathrm{Op}_h(a)u(x) := (2\pi h)^{-n}\int\!\!\int e^{i(x-x')\cdot\zeta/h}a_h(x,\zeta)u(x')\,dx'\,d\zeta = (2\pi h)^{-n}
\int e^{iz\cdot\zeta/h}a_h(x,\zeta)\,\mathcal F_hu(\zeta)\,d\zeta,$$

with $\mathcal F_hu(\zeta) := \int e^{-iz'\cdot\zeta/h}u(x')\,dx'$, Schwartz. $\Psi^{\mathbf o} :=
\mathrm{Op}_h(S^{\mathbf o})$. $\mathrm{Op}_h(a)$ maps $\mathcal S$ to itself: $x^\gamma e^{iz\cdot\zeta/h} =
(-ih\partial_\zeta)^\gamma e^{iz\cdot\zeta/h}$, and integrating by parts gives
$|x^\gamma\partial_x^\kappa\mathrm{Op}_h(a)u(x)|\le C_{\gamma\kappa}\langle x\rangle^{\sup\mathsf
r+|\kappa|}L_h(x,0)^\mu$ for some $\mu$ and every $\gamma$.

**Lemma 2.3 (oscillatory integrals).** Let $F\in C^\infty(\mathbb R^{2n}_{w,\eta};\mathbb C^{N\times N})$ satisfy
$|\partial_w^\gamma\partial_\eta^\kappa F|\le A_{\gamma\kappa}\langle w\rangle^M\langle\eta\rangle^M$. Fix $\chi\in
C_c^\infty(\mathbb R^n)$ with $\chi(0) = 1$. Then

$$I(F) := \lim_{\epsilon\to0}(2\pi)^{-n}\int\!\!\int e^{-iw\cdot\eta}\chi(\epsilon w)\chi(\epsilon\eta)F(w,\eta)\,dw\,
d\eta$$

exists, does not depend on $\chi$, and for $2k>M+n$

$$I(F) = (2\pi)^{-n}\int\!\!\int e^{-iw\cdot\eta}\langle\eta\rangle^{-2k}(1-\Delta_w)^k\big[\langle w\rangle^{-2k}(1-
\Delta_\eta)^kF\big]\,dw\,d\eta,\qquad|I(F)|\le C_{n,M}\max_{|\gamma|,|\kappa|\le2k}A_{\gamma\kappa}.\tag{2.2}$$

Moreover $I(w^\gamma F) = I(D_\eta^\gamma F)$, and $I(F) = F(\cdot,0)$ if $F$ does not depend on $w$.

*Proof.* $(1-\Delta_\eta)e^{-iw\cdot\eta} = \langle w\rangle^2e^{-iw\cdot\eta}$ and $(1-\Delta_w)e^{-iw\cdot\eta} =
\langle\eta\rangle^2e^{-iw\cdot\eta}$. Integrating by parts $k$ times in each variable in the regularised integral gives
(2.2) with $F$ replaced by $\chi(\epsilon w)\chi(\epsilon\eta)F$; the derivatives falling on the cut-offs are bounded
for $\epsilon\le1$ and tend to 0 pointwise, and the integrand is dominated by $C\langle w\rangle^{M-2k}\langle\eta
\rangle^{M-2k}$, integrable. Dominated convergence gives the limit and (2.2). The identity $w^\gamma e^{-iw\cdot\eta} =
(i\partial_\eta)^\gamma e^{-iw\cdot\eta}$ gives $I(w^\gamma F) = I(D_\eta^\gamma F)$. If $F = F(\eta)$, then
$(2\pi)^{-n}\int e^{-iw\cdot\eta}\chi(\epsilon w)\,dw = \epsilon^{-n}\check\chi(\eta/\epsilon)$ with $\int\check\chi =
\chi(0) = 1$, an approximate identity, so $I(F) = F(0)$. $\square$

**Theorem 2.4 (composition).** For $a\in S^{\mathbf o}$ and $b\in S^{\mathbf o'}$, $\mathrm{Op}_h(a)\mathrm{Op}_h(b) =
\mathrm{Op}_h(a\#b)$ with

$$a\#b(x,\zeta) = I\big(F_{x,\zeta}\big),\qquad F_{x,\zeta}(w,\eta) := a_h(x,\zeta+\eta)\,b_h(x+hw,\zeta).\tag{2.3}$$

$a\#b\in S^{\mathbf o+\mathbf o'}$, and for every $K\ge1$

$$a\#b-\sum_{|\alpha|<K}\frac{h^{|\alpha|}}{\alpha!}\,\partial_\zeta^\alpha a\,D_x^\alpha b\in S^{\mathbf o+\mathbf o'-
\frac K2\mathbf 1}.\tag{2.4}$$

Each seminorm of $a\#b$ and of the remainder is bounded by a product of seminorms of $a$ and $b$. The term with $\alpha$
lies in $S^{\mathbf o+\mathbf o'-|\alpha|\mathbf 1+\epsilon\mathbf 1}$ for every $\epsilon>0$.

*Proof.* The kernel of $\mathrm{Op}_h(a)\mathrm{Op}_h(b)$ is $(2\pi h)^{-2n}\int e^{i(x-y)\cdot\theta/h+i(y-x')\cdot\zeta
/h}a(x,\theta)b(y,\zeta)\,dy\,d\theta\,d\zeta$. Writing $e^{i(y-x')\cdot\zeta/h} = e^{i(x-x')\cdot\zeta/h}e^{-i(x-y)\cdot
\zeta/h}$, it is the kernel of $\mathrm{Op}_h(c)$ with $c(x,\zeta) = (2\pi h)^{-n}\int\!\!\int e^{i(x-y)\cdot(\theta-
\zeta)/h}a(x,\theta)b(y,\zeta)\,dy\,d\theta$, and $\theta = \zeta+\eta$, $y = x+hw$ (so $dy\,d\theta = h^n\,dw\,d\eta$)
give (2.3). On $u\in\mathcal S$ the manipulations are justified by inserting $\chi(\epsilon w)\chi(\epsilon\eta)$ and
letting $\epsilon\to0$.

*The expansion.* By Taylor's formula,
$b(x+hw,\zeta) = \sum_{|\alpha|<K}\frac{(hw)^\alpha}{\alpha!}\partial_x^\alpha b(x,\zeta)+K\sum_{|\alpha| = K}\frac{(hw)^
\alpha}{\alpha!}\int_0^1(1-t)^{K-1}\partial_x^\alpha b(x+thw,\zeta)\,dt$. Lemma 2.3 gives
$I(w^\alpha a(x,\zeta+\eta)\,\partial_x^\alpha b(x,\zeta)) = (D_\zeta^\alpha a)(x,\zeta)\,\partial_x^\alpha b(x,\zeta)$,
and $D_\zeta^\alpha a\,\partial_x^\alpha b = \partial_\zeta^\alpha a\,D_x^\alpha b$: these are the terms of (2.4). The
remainder is $R_K = K\sum_{|\alpha| = K}\frac{h^K}{\alpha!}\int_0^1(1-t)^{K-1}I(G_{\alpha,t})\,dt$ with
$G_{\alpha,t}(w,\eta) := (D_\zeta^\alpha a)(x,\zeta+\eta)\,(\partial_x^\alpha b)(x+thw,\zeta)$.

*The remainder, with constant orders.* Let $\mathbf o_+$, $\mathbf o'_+$ be the componentwise suprema. Since
$\langle x+y\rangle^t\le2^{|t|/2}\langle x\rangle^t\langle y\rangle^{|t|}$ (Peetre) and $L_h(x+y,\zeta+\eta)\le
L_h(x,\zeta)\langle y\rangle\langle\eta\rangle$, and using $(th)^{|\gamma|}\le1$, $\langle x+thw\rangle^{-|\gamma|}\le1$
and $\langle\zeta+\eta\rangle^{-|\kappa|}\le1$, for $|\gamma|,|\kappa|\le2k$

$$|\partial_w^\gamma\partial_\eta^\kappa G_{\alpha,t}|\le C\,w_{\mathbf o_++\mathbf o'_+}(x,\zeta)\langle x\rangle^{-K}
\langle\zeta\rangle^{-K}L_h(x,\zeta)^\mu\langle w\rangle^{M}\langle\eta\rangle^{M},\qquad M := |\mathsf r'_+-K|+|s_+-K|+
\mu+1,$$

with $\mu$ depending on $K$ and $k$. By (2.2) with $2k>M+n$, $|I(G_{\alpha,t})|$ obeys the same bound without the last
two factors. A derivative of $R_K$ in $x$ or $\zeta$ falls on $a$ or $b$ inside $I$; it gains $\langle x\rangle^{-1}$
or $\langle\zeta\rangle^{-1}$ up to a factor $L_h\langle w\rangle\langle\eta\rangle$, which (2.2) absorbs with a larger
$k$. So $R_K\in S^{\mathbf o_++\mathbf o'_+-K\mathbf 1+\epsilon\mathbf 1}$ for every $\epsilon>0$, the factor $h^K$
being the gain in the semiclassical order.

*Variable orders.* Let $\omega$ be the sum over the three components of $\sup(\mathbf o+\mathbf o')-\inf(\mathbf
o+\mathbf o')$. For $K\ge2\omega+2$, $\mathbf o_++\mathbf o'_+-K\mathbf 1+\epsilon\mathbf 1\le\mathbf o+\mathbf o'-\frac
K2\mathbf 1$ pointwise, so $R_K\in S^{\mathbf o+\mathbf o'-\frac K2\mathbf 1}$ by Lemma 2.2 (c). The terms with
$|\alpha|<K$ lie in $S^{\mathbf o+\mathbf o'-|\alpha|\mathbf 1+\epsilon\mathbf 1}$ by Lemma 2.2 (b), (d). Applying this
with $K' := \max(K,2\omega+2)$ and moving the terms with $K\le|\alpha|<K'$ into the remainder gives (2.4) for every $K$,
and $a\#b\in S^{\mathbf o+\mathbf o'}$. $\square$

**Theorem 2.5 (adjoints).** For $a\in S^{\mathbf o}$, the formal adjoint in $L^2(\mathbb R^n;\mathbb C^N)$ is
$\mathrm{Op}_h(a)^* = \mathrm{Op}_h(a^\natural)$ with $a^\natural(x,\zeta) = I(a_h(x+hw,\zeta+\eta)^*)$, and
$a^\natural-\sum_{|\alpha|<K}\frac{h^{|\alpha|}}{\alpha!}\partial_\zeta^\alpha D_x^\alpha a^*\in S^{\mathbf o-\frac K2
\mathbf 1}$.

*Proof.* The kernel of $\mathrm{Op}_h(a)^*$ is $(2\pi h)^{-n}\int e^{i(x-x')\cdot\zeta/h}a(x',\zeta)^*\,d\zeta$, the
kernel of $\mathrm{Op}_h(c)$ with $c(x,\theta) = (2\pi h)^{-n}\int\!\!\int
e^{iy\cdot(\zeta-\theta)/h}a(x-y,\zeta)^*\,dy\, d\zeta$; substitute $\zeta = \theta+\eta$, $y = -hw$. The expansion
follows as in Theorem 2.4. $\square$

*Consequences.* (i) $\mathrm{Op}_h$ is injective on symbols (the symbol is a partial Fourier transform of the kernel).
(ii) For $a\in S^{\mathbf o}$, $b\in S^{\mathbf o'}$ and every $\epsilon>0$,

$$\tfrac ih[\mathrm{Op}_h(a),\mathrm{Op}_h(b)]-\mathrm{Op}_h\big(\tfrac ih(ab-ba)+\{a,b\}\big)\in\Psi^{\mathbf o+\mathbf
o'
-(2,2,1)+\epsilon\mathbf 1},\tag{2.5}$$

with $\{a,b\} := \sum_j(\partial_{\zeta_j}a\,\partial_{x_j}b-\partial_{\zeta_j}b\,\partial_{x_j}a)$ (products in the
written order). If $a = p\,\mathrm{Id}$ is scalar, the symbol is $H_pb$, $H_p := \partial_\zeta p\cdot\partial_x-
\partial_zp\cdot\partial_\zeta$. If $a$ is scalar only modulo $S^{\mathbf o-\mathbf 1}$, the left side of (2.5) is still
in $\Psi^{\mathbf o+\mathbf o'-(1,1,0)+\epsilon\mathbf 1}$. (iii) If $\mathrm{Op}_h(a)$ is self-adjoint, then
$a-a^*\in S^{\mathbf o-\mathbf 1+\epsilon\mathbf 1}$. (iv) If $a$ vanishes on an open set $U$, then $a\#b$ and $b\#a$,
restricted to any open $U'$ with $\overline{U'}\subset U$, obey the bounds of $S^{-K\mathbf 1}$ for every $K$: every term
of (2.4) vanishes there, and the remainder lies in $S^{\mathbf o+\mathbf o'-\frac K2\mathbf 1}$ for every $K$.

*Fibre inner products.* For a fibre inner product $h = \langle H\cdot,\cdot\rangle$ ($H$ smooth on the compactification,
so $H^{\pm1/2}\in S^0$), $u\mapsto H^{1/2}u$ is unitary from $L^2_h$ to $L^2$, and $A\mapsto H^{1/2}AH^{-1/2}$ preserves
every $\Psi^{\mathbf o}$, conjugates principal symbols, and maps $A^{*h}$ to $(H^{1/2}AH^{-1/2})^*$. So everything in
this section holds with $\langle\cdot,\cdot\rangle_h$ and ${}^{*h}$ in place of $\langle\cdot,\cdot\rangle$ and ${}^*$.

### 2.3 Boundedness and Sobolev spaces

**Lemma 2.6 (Schur).** Let $\beta\in\mathbb R$ and $c\in S^{(-n-1,-\epsilon_0,\beta)}$ for some $\epsilon_0>0$. Then
$\|\mathrm{Op}_h(c)\|_{L^2\to L^2}\le Ch^{-\beta}$, with $C$ a seminorm of $c$.

*Proof.* The kernel is $k(x,x') = (2\pi h)^{-n}\int e^{i(x-x')\cdot\zeta/h}c(x,\zeta)\,d\zeta$, and
$(1-h^2\Delta_\zeta)e^{i(x-x')\cdot\zeta/h} = \langle(x-x')/h\rangle^2e^{i(x-x')\cdot\zeta/h}$, so

$$|k(x,x')|\le(2\pi h)^{-n}\langle(x-x')/h\rangle^{-2n-2}\int|(1-h^2\Delta_\zeta)^{n+1}c(x,\zeta)|\,d\zeta.$$

$(1-h^2\Delta_\zeta)^{n+1}c$ is $c$ plus terms $h^{2j}\Delta_\zeta^jc$, $j\ge1$, bounded by $Ch^{2j-\beta}\langle
x\rangle^{-\epsilon_0}\langle\zeta\rangle^{-n-1-2j}L_h^\mu\le Ch^{-\beta}\langle\zeta\rangle^{-n-1-j}$, since
$h^{2j}\langle x\rangle^{-\epsilon_0}\langle\zeta\rangle^{-j}L_h^\mu$ is bounded. Hence $|k(x,x')|\le
Ch^{-n-\beta}\langle(x-x')/h\rangle^{-2n-2}$, so $\sup_x\int|k|\,dx'$ and $\sup_{x'}\int|k|\,dx$ are at most
$Ch^{-\beta}$, and Schur's test gives the claim. $\square$

**Theorem 2.7 ($L^2$ bound).** Let $a\in S^{0}$ (all orders 0) and $\epsilon>0$. There is $C$ with

$$\|\mathrm{Op}_h(a)u\|\le\big(\sup|a|+\epsilon\big)\|u\|+Ch^{1/4}\|u\|,\qquad u\in\mathcal S,$$

the supremum over $(x,\zeta)$ and $h$. In particular $\Psi^0$ acts on $L^2$, uniformly in $h$.

*Proof.* Put $M := \sup|a|^2+\epsilon^2$ and $e := M-a^*a\ge\epsilon^2$, a Hermitian symbol in $S^0$. Its positive square
root $b_0 := e^{1/2} = \frac1{2\pi i}\oint_\Gamma\lambda^{1/2}(\lambda-e)^{-1}\,d\lambda$, $\Gamma$ a circle in
$\mathrm{Re}\,\lambda>0$ around $[\epsilon^2,M]$, lies in $S^0$ (differentiate under the integral; each derivative of
$(\lambda-e)^{-1}$ is a sum of products of resolvents and derivatives of $e$), as does $b_0^{-1}$. By Theorems 2.4-2.5,
$\mathrm{Op}_h(b_0)^*\mathrm{Op}_h(b_0)+\mathrm{Op}_h(a)^*\mathrm{Op}_h(a) = M+\mathrm{Op}_h(r_1)$ with $r_1\in
S^{-\frac12\mathbf 1}$, $\mathrm{Op}_h(r_1)$ self-adjoint. Given $b_0+\dots+b_{j-1}$ with self-adjoint remainder
$\mathrm{Op}_h(r_j)$, $r_j\in S^{-\frac j2\mathbf 1}$, put $b_j := -\frac14b_0^{-1}(r_j+r_j^*)$; then $b_0^*b_j+b_j^*b_0
= -\frac12(r_j+r_j^*)$ and, by (iii) and Theorem 2.4, the new remainder lies in $S^{-\frac{j+1}2\mathbf 1+\epsilon\mathbf
1}$ (we absorb the $\epsilon$ by taking two steps per half order). With $J := 4n+8$ and $B :=
\mathrm{Op}_h(b_0+\dots+b_J)$, $\|\mathrm{Op}_h(a)u\|^2 =
M\|u\|^2-\|Bu\|^2+\langle\mathrm{Op}_h(r_{J+1})u,u\rangle\le(M+Ch^{1/2})\|u\|^2$ by Lemma 2.6 with $\beta = -\frac12$,
since $r_{J+1}\in S^{-(n+1)\mathbf 1}\subset S^{(-n-1,-1,-\frac12)}$. Take square roots. $\square$

*Sobolev spaces.* For orders $\mathbf o$ let $W_{\mathbf o} := \mathrm{Op}_h(w_{\mathbf o}\mathrm{Id})$. By Lemma 2.2 and
Theorem 2.4, $\mathrm{Op}_h(w_{-\mathbf o})W_{\mathbf o} = I+\mathrm{Op}_h(e)$ and $W_{\mathbf
o}\mathrm{Op}_h(w_{-\mathbf o}) = I+\mathrm{Op}_h(e')$ with $e,e'\in S^{-\frac12\mathbf 1}$, so by Theorem 2.7 there is
$h_0>0$ such that for $h<h_0$ both are invertible on $L^2$ with inverses bounded uniformly. For $h<h_0$ define
$H_h^{\mathbf o} := \{u\in\mathcal S':W_{\mathbf o}u\in L^2\}$, $\|u\|_{\mathbf o} := \|W_{\mathbf o}u\|_{L^2}$. For
constant orders $H_h^{\mathbf o} = h^{\mathsf b}\langle x\rangle^{-\mathsf r}\langle hD\rangle^{-s}L^2$ with uniformly
equivalent norm. For each fixed $h$, $H^{\mathbf o}_h$ is the scattering Sobolev space of [HJS] Definition 10.2 with the
decay order $\mathsf r(x,h\zeta)$ and the constant regularity order $s$ (when $s$ is constant), with a norm equivalent
for that $h$: $h^{-\mathsf b(x,h\zeta)}$ is a symbol of order 0 at fixed $h$. This is how fixed-frequency results of Part
I.A are used.

**Proposition 2.8 (mapping).** For $A\in\Psi^{\mathbf m}$ and orders $\mathbf o$, $\|Au\|_{\mathbf o-\mathbf m}\le C
\|u\|_{\mathbf o}$ for $h<h_0$. *Proof.* $\|Au\|_{\mathbf o-\mathbf m} = \|W_{\mathbf o-\mathbf m}AW_{\mathbf o}^{-1}
(W_{\mathbf o}u)\|$, $W_{\mathbf o}^{-1} = \mathrm{Op}_h(w_{-\mathbf o})(I+\mathrm{Op}_h(e'))^{-1}$, and
$W_{\mathbf o-\mathbf m}A\,\mathrm{Op}_h(w_{-\mathbf o})\in\Psi^0$ by Theorem 2.4. $\square$

The $L^2$ pairing extends to $H^{\mathbf o}_h\times H^{-\mathbf o}_h$ with $|\langle u,v\rangle|\le C\|u\|_{\mathbf o}
\|v\|_{-\mathbf o}$: $\langle u,v\rangle = \langle W_{\mathbf o}u,(W_{\mathbf o}^{-1})^*v\rangle$, and
$(W_{\mathbf o}^{-1})^*$ maps $H^{-\mathbf o}_h$ to $L^2$ by Proposition 2.8 and Theorem 2.5.

### 2.4 Microlocalisation

$\mathcal P := \overline{\mathbb R^n}\times\overline{\mathbb R^n}$ is the semiclassical scattering phase space (the face
${}^{\mathrm{sc},\hbar}\overline T^*_{\mathrm{sf}}$ of [Hin26c] (3.34), identified with ${}^{\mathrm{sc}}\overline T^*
\overline{\mathbb R^n}$ as in his (3.36)). Its boundary faces are fibre infinity $\overline{\mathbb R^n}\times\partial
\overline{\mathbb R^n}$ and the face $\partial\overline{\mathbb R^n}\times\overline{\mathbb R^n}$ over spatial infinity.

**Definition 2.9.** For $A = \mathrm{Op}_h(a)\in\Psi^{\mathbf o}$: $\varpi\in\mathcal P$ is *not* in $\mathrm{WF}'_h(A)$
if it has a neighbourhood $U$ in $\mathcal P$ on which $a$ obeys the bounds of $S^{-K\mathbf 1}$ for every $K$; it is in
$\mathrm{Ell}_h(A)$ if it has a neighbourhood $U$ and $h_0>0$ with $a_h$ invertible and $|a_h^{-1}|\le Cw_{\mathbf
o}^{-1}$ on $U\cap\mathbb R^{2n}$ for $h<h_0$.

By (iv), $\mathrm{WF}'_h(AB)\subset\mathrm{WF}'_h(A)\cap\mathrm{WF}'_h(B)$. Ellipticity at $\varpi$ depends only on $a$
modulo symbols that are small compared with $w_{\mathbf o}$ near $\varpi$: modulo $S^{\mathbf o-(0,0,\frac12)}$
anywhere (for small $h$), modulo $S^{\mathbf o-(0,\frac12,0)}$ near the face over spatial infinity, and modulo
$S^{\mathbf o-(\frac12,0,0)}$ near fibre infinity. The *principal symbol* of $A\in\Psi^{\mathbf o}$ is its symbol modulo
$S^{\mathbf o-\mathbf 1+\epsilon\mathbf 1}$ for small $\epsilon>0$; by (2.4) it is multiplicative.

**Proposition 2.10 (microlocal elliptic estimate).** Let $A\in\Psi^{\mathbf m}$, $B,G\in\Psi^0$ with
$\mathrm{WF}'_h(B)\subset\mathrm{Ell}_h(A)\cap\mathrm{Ell}_h(G)$. Then for all orders $\mathbf o$ and all $K$,
$\|Bu\|_{\mathbf o}\le C(\|GAu\|_{\mathbf o-\mathbf m}+\|u\|_{-K\mathbf 1})$.

*Proof.* Let $\phi\in S^0$ equal 1 near $\mathrm{WF}'_h(B)$, supported where $a$ and $g$ are uniformly invertible. $q_0
:= \phi\,a^{-1}g^{-1}\in S^{-\mathbf m}$ by Lemma 2.2 (e), and $\mathrm{Op}_h(q_0)GA = \mathrm{Op}_h(\phi)+\mathrm{Op}_h
(r)$ with $r\in S^{-\frac12\mathbf 1}$ near $\mathrm{WF}'_h(B)$. Corrections $q_j\in S^{-\mathbf m-\frac j2\mathbf 1}$
supported in $\mathrm{supp}\,\phi$ remove the error to any order: $QGA = \mathrm{Op}_h(\phi)+R$ with $R\in S^{-K\mathbf
1}$ near $\mathrm{WF}'_h(B)$. Then $B = BQGA-BR+B(I-\mathrm{Op}_h(\phi))$, the last term in $\Psi^{-K\mathbf 1}$ by (iv),
and Proposition 2.8 bounds the rest. $\square$

**Lemma 2.11 (positivity).** Let $A = A^*\in\Psi^{2\mathbf m}$ with principal symbol $\mathsf a$, and $B\in\Psi^0$.
Suppose $\mathsf a\ge c\,w_{\mathbf m}^2\mathrm{Id}$, $c>0$, on a neighbourhood of $\mathrm{WF}'_h(B)$. Then for all $K$
and small $\epsilon>0$, $\langle ABu,Bu\rangle\ge\frac c2\|Bu\|^2_{\mathbf m}-C\|Bu\|^2_{\mathbf
m-\frac12(1-\epsilon)\mathbf 1}-C\|u\|^2_{-K\mathbf 1}$.

*Proof.* Let $\tilde{\mathsf a}\in S^{2\mathbf m}$ be Hermitian, equal to $\mathsf a$ near $\mathrm{WF}'_h(B)$ and
$\ge\frac34cw_{\mathbf m}^2$ everywhere. Put $q := w_{\mathbf m}(w_{\mathbf m}^{-2}\tilde{\mathsf a}-\frac c2)^{1/2}\in
S^{\mathbf m}$ (positive square root, as in Theorem 2.7). Then $A = \mathrm{Op}_h(q)^*\mathrm{Op}_h(q)+\frac c2W_{\mathbf
m}^*W_{\mathbf m}+E$ with $E\in\Psi^{2\mathbf m-(1-\epsilon)\mathbf 1}$ near $\mathrm{WF}'_h(B)$, so
$\langle ABu,Bu\rangle\ge\frac c2\|Bu\|^2_{\mathbf m}+\langle EBu,Bu\rangle$, and Proposition 2.8 bounds the last term.
$\square$

**Lemma 2.12 (square roots with logarithmic growth).** Let $Q_0\in S^0$ be Hermitian with $Q_0\ge M\,\mathrm{Id}$,
$M>0$, and let $\lambda\ge0$ be a real scalar function with $\lambda\le CL_h$ and $|\partial_x^\alpha\partial_\zeta^\beta
\lambda|\le C_{\alpha\beta}\langle x\rangle^{-|\alpha|}\langle\zeta\rangle^{-|\beta|}L_h^{\mu_{\alpha\beta}}$ for
$(\alpha,\beta)\ne0$. Let $Q := Q_0+\lambda\,\mathrm{Id}$. Then $Q^{1/2}\in S^{\epsilon\mathbf 1}$ for every
$\epsilon>0$ and $Q^{-1/2}\in S^0$. If $b := w_{\mathbf o}\phi\,Q^{1/2}$ with $\phi\in S^0$ scalar, then $b\in
S^{\mathbf o+\epsilon\mathbf 1}$ for every $\epsilon$, and wherever $\phi\ge c>0$ on an open set $U$, $\phi'b^{-1}\in
S^{-\mathbf o}$ for $\phi'\in S^0$ supported in $U$; Proposition 2.10 then holds with $A := \mathrm{Op}_h(b)$, at the
order $\mathbf o$, on $U$.

*Proof.* $Q = (1+\lambda)\tilde Q$ with $\tilde Q := (Q_0+\lambda)/(1+\lambda)$, whose values lie in
$[\min(M,1),\max(\sup|Q_0|,1)]$ and whose derivatives obey (2.1) with order 0. So $\tilde Q^{\pm1/2}\in S^0$ by the
Cauchy formula of Theorem 2.7 over a fixed contour. $(1+\lambda)^{1/2}\le CL_h^{1/2}\le C_\epsilon w_{\epsilon\mathbf
1}$, and its derivatives $\frac12(1+\lambda)^{-1/2}\partial\lambda$ and higher obey (2.1); $(1+\lambda)^{-1/2}\le1$
likewise. This gives the first two claims, and $b^{-1} = w_{-\mathbf o}\phi^{-1}Q^{-1/2}$ on $U$. In the proof of
Proposition 2.10 with $q_0 := \phi'b^{-1}\in S^{-\mathbf o}$, $q_0\#b-\phi'$ lies in $S^{-\frac12\mathbf 1}$ near
$\mathrm{supp}\,\phi'$, since each term of (2.4) with $|\alpha|\ge1$ gains $|\alpha|\mathbf 1$ up to logarithms and the
logarithmic growth of $b$ is one factor $L_h^{1/2}$; the iteration is unchanged. $\square$

## 3. The positive commutator scheme

All operators below have Schwartz kernels supported in $\{r>r_0-\frac32\delta_0\}^2$. The coefficients of $P_{h,z}$ on
$\tilde X^\circ$ are extended to $\mathbb R^4$ arbitrarily (smoothly); no estimate below sees the extension. Orders are
triples $\mathbf o = (s,\mathsf r,\mathsf b)$ with $s$ constant, and $\mathbf m := (2,0,0)$ is the order of $P_{h,z}$.
For a fibre inner product $h$, pairings and adjoints are those of $L^2_h$ (section 2.2).

### 3.1 A priori estimates, and why no regularisation is needed

In Part I.A the commutants were regularised because the estimates there are also regularity statements: they are
applied to $u$ known only in a weaker space. Here every estimate is proved for Schwartz $u$, and is then extended by
density to the spaces where it is used.

**Lemma 3.1 (density).** Fix $h\in(0,h_0)$, $z$, and orders $\mathbf o$. Let $\mathcal G := \{u\in H^{\mathbf o}_h :
P_{h,z}u\in H^{\mathbf o-\mathbf m+(1,1,0)}_h\}$ with the graph norm. Then $\mathcal S$ is dense in $\mathcal G$. The
same holds with the b-regular norms of (1.5) and for $P^{*h}_{h,z}$ with $\mathbf o$ replaced by $-\mathbf o+\mathbf
m-(1,1,0)$.

*Proof.* At fixed $h$, $H^{\mathbf o}_h$ is the space $H^{s,\mathsf r_h}_{\mathrm{sc}}$ of [HJS] with $\mathsf r_h(x,\xi)
:= \mathsf r(x,h\xi)$, with an equivalent norm (section 2.3), and $P_{h,z} = h^2\hat P(z/h)\in\Psi^{2,0}_{\mathrm{sc}}$.
With $T_t$ from I.A (C8), $T_tu\to u$ in $H^{\mathbf o}_h$, and $P_{h,z}T_tu = T_tP_{h,z}u+[P_{h,z},T_t]u$. Here
$T_tP_{h,z}u\to P_{h,z}u$, and $[P_{h,z},T_t]$ is bounded in $\Psi^{1,-1}_{\mathrm{sc}}$ and tends to 0 in
$\Psi^{1+\delta,-1+\delta}_{\mathrm{sc}}$ for every $\delta>0$ (I.A Lemma 2.1 (c), (C8)). So it is uniformly bounded from
$H^{s,\mathsf r_h}$ to $H^{s-1,\mathsf r_h+1}$ and tends to 0 on the dense subspace $H^{s+\delta,\mathsf r_h+\delta}$,
hence strongly. $T_tu$ is Schwartz. For the b-regular norms, $[\langle x\rangle D_x,T_t]$ is likewise bounded in
$\Psi^{0,0}_{\mathrm{sc}}$ and tends to 0 strongly. $\square$

Every term of the estimates below ($\|Bu\|_{\mathbf o}$, $h^{-1}\|GP_{h,z}u\|_{\mathbf o-\mathbf m+(1,1,0)}$,
$\|Eu\|_{\mathbf o}$, $\|u\|_{-K\mathbf 1}$, with $B,G,E\in\Psi^0$) is continuous on $\mathcal G$. So an estimate proved
for Schwartz $u$ holds on $\mathcal G$, with the same constant, for each $h$. Near $\partial_\sharp X$ the estimates are
applied to $\chi u$ with $\chi\in C_c^\infty(\{r>r_0-\delta_0\})$; then $P_{h,z}(\chi u) = \chi P_{h,z}u+[P_{h,z},\chi]u$
with $[P_{h,z},\chi] = h\cdot\mathrm{Diff}^1_h$.

### 3.2 The identity and one step

**Lemma 3.2 (the commutator identity, [Hin26c] (9.66)).** Let $P\in\Psi^{\mathbf m}$ and $\check A = \check A^{*h}$.
For Schwartz $u$,

$$\frac2h\,\mathrm{Im}\langle\check APu,\check Au\rangle_h = \langle Cu,u\rangle_h,\qquad C := \frac ih[\mathrm{Re}_hP,
\check A^2]+\frac1h\big(\check A^2\,\mathrm{Im}_hP+\mathrm{Im}_hP\,\check A^2\big).\tag{3.1}$$

*Proof.* $2i\,\mathrm{Im}\langle\check A^2Pu,u\rangle = \langle(\check A^2P-P^{*h}\check A^2)u,u\rangle$, and
$\check A^2P-P^{*h}\check A^2 = [\check A^2,\mathrm{Re}_hP]+i(\check A^2\mathrm{Im}_hP+\mathrm{Im}_hP\,\check A^2)$.
Divide by $ih$. $\square$

We use $X\check A^2+\check A^2X = 2\check AX\check A+[[X,\check A],\check A]$. If $\mathrm{Re}_hP$ has principal symbol
$p\,\mathrm{Id}$ with $p$ real, $\check A$ has principal symbol $\check a\,\mathrm{Id}$ with $\check a$ real, and
$h^{-1}\mathrm{Im}_hP\in\Psi^{\mathbf m-(1,1,0)}$ has principal symbol $p_I$ (an $h$-self-adjoint endomorphism), then by
(2.5) and Theorem 2.4 the principal symbol of $C$ is $H_p(\check a^2)\mathrm{Id}+2\check a^2p_I$, and the remainders lie
in $\Psi^{\mathbf m+2\mathbf k-(2,2,1)+\epsilon\mathbf 1}$, where $\check A\in\Psi^{\mathbf k}$. With

$$\mathbf k := \mathbf o-\tfrac12\big(\mathbf m-(1,1,0)\big) = \mathbf o-(\tfrac12,-\tfrac12,0),\tag{3.2}$$

$C\in\Psi^{2\mathbf o}$ and the remainders lie in $\Psi^{2\mathbf o-\mathbf 1+\epsilon\mathbf 1}$.

**Lemma 3.3 (one step).** Let $P\in\Psi^{\mathbf m}$, $\mathbf o$ an order and $\mathbf k$ as in (3.2). Let $K_1$ be a
closed subset of $\mathcal P$ and $G\in\Psi^0$ elliptic on $K_1$. Suppose $\check A = \check A^{*h}\in\Psi^{\mathbf k}$
and that, for a sign $\varsigma$ and $C$ as in (3.1),

$$\varsigma C = -B^{*h}B-F+E^{*h}E+JP+R,\tag{3.3}$$

where: $B\in\Psi^{\mathbf o}$ and $\check A = ZB+Y$ with $Z\in\Psi^{-\frac12(\mathbf m-(1,1,0))}$, $Y\in\Psi^{\mathbf k-
\frac12\mathbf 1}$; $\langle Fw,w\rangle_h\ge-C_F\|w\|^2_{-K\mathbf 1}$ for Schwartz $w$; $E\in\Psi^{\mathbf o}$ is
microsupported in a closed set $K_E$; $J\in\Psi^{2\mathbf o-\mathbf m}$ with $\mathrm{WF}'_h(J)\subset\mathrm{Ell}_h(P)$;
$R\in\Psi^{2\mathbf o-\frac12\mathbf 1}$; and $\check A,B,E,J,R$ are microsupported in $K_1$. Let $E'\in\Psi^0$ be
elliptic on $K_E$. Then for Schwartz $u$ and $h<h_0$,

$$\|Bu\|^2\le C\big(h^{-2}\|GPu\|^2_{\mathbf o-\mathbf m+(1,1,0)}+\|E'u\|^2_{\mathbf o}+\|Gu\|^2_{\mathbf o-\frac14
\mathbf 1}+\|u\|^2_{-K\mathbf 1}\big).\tag{3.4}$$

$C$ depends on $C_F$ and on seminorms of the operators involved.

*Proof.* By (3.1) and (3.3), $\|Bu\|^2 = -\varsigma\frac2h\mathrm{Im}\langle\check APu,\check Au\rangle-\langle
Fu,u\rangle+ \|Eu\|^2+\langle JPu,u\rangle+\langle Ru,u\rangle$. Microlocalise first: let $\Phi\in\Psi^0$ be microlocally
the identity near $K_1$, with $\mathrm{WF}'_h(\Phi)\subset\mathrm{Ell}_h(G)$; then $\check A(I-\Phi)$ and
$(I-\Phi)^{*h}\check A$ are residual, and $\|\Phi f\|_{\mathbf t}\le C(\|Gf\|_{\mathbf t}+\|f\|_{-K\mathbf 1})$ by
Proposition 2.10. (a) $\langle\check APu,\check Au\rangle = \langle Z^{*h}\check APu,Bu\rangle+\langle\check
APu,Yu\rangle$, and $Z^{*h}\check A\in\Psi^{\mathbf o-\mathbf m+(1,1,0)}$, $\check A$ maps $H^{\mathbf o-\mathbf
m+(1,1,0)}$ to $H^{-\frac12(\mathbf m-(1,1,0))}$, $Y$ maps $H^{\mathbf o-\frac12\mathbf 1}$ to $H^{\frac12(\mathbf
m-(1,1,0))}$. So $\frac2h|\langle\check APu,\check Au\rangle|\le\frac12\|Bu\|^2+Ch^{-2}\|GPu\|^2_{\mathbf o-\mathbf
m+(1,1,0)}+C\|Gu\|^2_ {\mathbf o-\frac12\mathbf 1}+C\|u\|^2_{-K\mathbf 1}$. (b) $-\langle Fu,u\rangle\le
C_F\|u\|^2_{-K\mathbf 1}$. (c) $\|Eu\|\le C(\|E'u\|_{\mathbf o}+\|u\|_{-K\mathbf 1})$ by Proposition 2.10. (d) Let
$\Phi_J\in\Psi^0$ be microlocally the identity near $\mathrm{WF}'_h(J)$ with
$\mathrm{WF}'_h(\Phi_J)\subset\mathrm{Ell}_h(P)\cap\mathrm{Ell}_h(G)$; then $\langle JPu,u\rangle = \langle
JPu,\Phi_Ju\rangle+O(\|u\|^2_{-K\mathbf 1}+\|GPu\|^2)$, $\|JPu\|_{-\mathbf o}\le C(\|GPu\|_ {\mathbf o-\mathbf
m}+\|u\|_{-K\mathbf 1})$, and $\|\Phi_Ju\|_{\mathbf o}\le C(\|GPu\|_{\mathbf o-\mathbf m}+\|u\|_{-K \mathbf 1})$ by
Proposition 2.10; and $\|GPu\|_{\mathbf o-\mathbf m}\le\|GPu\|_{\mathbf o-\mathbf m+(1,1,0)}\le h^{-1} \|GPu\|_{\mathbf
o-\mathbf m+(1,1,0)}$. (e) $|\langle Ru,u\rangle|\le C\|Gu\|^2_{\mathbf o-\frac14\mathbf 1}+C\|u\|^2_{-K \mathbf 1}$.
Absorb $\frac12\|Bu\|^2$. $\square$

### 3.3 Iteration in the semiclassical order

The error term $\|Gu\|_{\mathbf o-\frac14\mathbf 1}$ is at most $\|Gu\|_{\mathbf o-(0,0,\frac14)} =
h^{1/4}\|Gu\|_{\mathbf o}$. Lowering only the semiclassical order keeps every threshold, because $\mathsf b$ enters a
commutant only through the factor $h^{-2\mathsf b}$, which at an order $\mathbf o-(0,0,\beta)$ is multiplied by the
constant $h^{2\beta}$: a decomposition (3.3) at $\mathbf o$ gives one at $\mathbf o-(0,0,\beta)$ by multiplying every
operator by $h^\beta$, with the same seminorms in the shifted classes.

**Lemma 3.4 (iteration).** Let $\Lambda\subset\mathcal P$ be closed and $U_0$ an open neighbourhood. Suppose that for
every open $U$ with $\Lambda\subset U\subset U_0$ there are $\check A$ and a decomposition (3.3) at the order
$\mathbf o$, with $K_1\subset U$, $K_E = K_E(U)$ a closed subset of $\bar U_0\setminus\Lambda$ (or no $E$ term), and $B$
elliptic on the closure of an open neighbourhood $U'$ of $\Lambda$. Let $G$ be elliptic on $\bar U_0$ and $N\in
\mathbb N$. Then there are a neighbourhood $U_*$ of $\Lambda$ and a closed set $K_E^*\subset\bar U_0\setminus\Lambda$
such that for every $B_*\in\Psi^0$ microsupported in $U_*$, every $E'$ elliptic on $K_E^*$, and Schwartz $u$,

$$\|B_*u\|_{\mathbf o}\le C\big(h^{-1}\|GPu\|_{\mathbf o-\mathbf m+(1,1,0)}+\|E'u\|_{\mathbf o}+h^N\|Gu\|_{\mathbf o}+
\|u\|_{-K\mathbf 1}\big).\tag{3.5}$$

*Proof.* Let $J := 4N$. Choose $U_0\supset U_1\supset\dots\supset U_J\supset\Lambda$, $U_j$ the $U'$ of the hypothesis
for $U_{j-1}$, with $B^{(j)}$ elliptic on $\bar U_j$ and $K_E^* := \bigcup_jK_E(U_{j-1})$. Let $G_0 := G$ and, for
$j\ge1$, $G_j\in\Psi^0$ elliptic on $\bar U_j$ with $\mathrm{WF}'_h(G_j)\subset\mathrm{Ell}_h(B^{(j)})$, so that
$\|G_ju\|_{\mathbf t}\le C(\|B^{(j)}u\|_{\mathbf t-\mathbf o}+\|u\|_{-K\mathbf 1})$ (with $B^{(j)}$ at the shifted
order). Apply Lemma 3.3 at the order $\mathbf o-(0,0,\frac{J-j}4)$ with $(U_{j-1},G_{j-1})$, using the scaling above:

$$\|G_ju\|_{\mathbf o-(0,0,\frac{J-j}4)}\le C\big(h^{-1}\|GPu\|_{\mathbf o-\mathbf m+(1,1,0)}+\|E'u\|_{\mathbf
o}+\|G_{j-1}
u\|_{\mathbf o-(0,0,\frac{J-j+1}4)}+\|u\|_{-K\mathbf 1}\big).$$

Chaining from $j = J$ down to $j = 1$ leaves $\|G_0u\|_{\mathbf o-(0,0,\frac J4)} = h^N\|Gu\|_{\mathbf o}$. Take
$U_* := U_J$ and use $\|B_*u\|_{\mathbf o}\le C(\|G_Ju\|_{\mathbf o}+\|u\|_{-K\mathbf 1})$. $\square$

*Positivity of absorbing terms.* Suppose $h^{-1}\mathrm{Im}_hP$ contains $-\lambda\mathcal A$ with $\lambda\ge0$ a
constant, $\lambda\le Ch^{-1}$, and $\mathcal A = \mathcal A^{*h}$ such that $\varsigma\mathcal A\in\Psi^{2\mathbf t}$
has principal symbol $\ge c\,w_{\mathbf t}^2$ on a neighbourhood of $\mathrm{WF}'_h(\check A)$, for some order $\mathbf
t$. Then $\varsigma C$ contains $-\lambda\varsigma(\check A^2\mathcal A+\mathcal A\check A^2) =
-F-\lambda\varsigma[[\mathcal A,\check A],\check A]$ with $F := 2\lambda\check A(\varsigma\mathcal A)\check A$. The
double commutator lies in $\lambda\Psi^{2\mathbf k+2\mathbf t-2\mathbf 1}$, which for the orders below is in the class of
$R$. And $F$ satisfies the hypothesis of Lemma 3.3: Lemma 2.11, whose proof does not use the order of $B$, gives
$\langle\varsigma\mathcal A\check Aw,\check Aw\rangle\ge\frac c2\|\check Aw\|^2_{\mathbf t}-C\|\check Aw\|^2_{\mathbf
t-\frac12(1-\epsilon)\mathbf 1}-C\|w\|^2_{-K\mathbf 1}$, and the middle term is at most $Ch^{1-\epsilon}\|\check Aw\|^2_
{\mathbf t}$, which the first absorbs for $h$ small. So $\langle Fw,w\rangle\ge-C\lambda\|w\|^2_{-K\mathbf
1}\ge-C\|w\|^2_ {-(K-1)\mathbf 1}$. This is [Hin26c] (9.69).

In Lemma 3.3 we also allow $B\in\bigcap_\epsilon\Psi^{\mathbf o+\epsilon\mathbf 1}$ of the form of Lemma 2.12 (a variable
order contributes a factor $(1+\lambda)^{1/2}$ with $\lambda$ logarithmic); the proof is unchanged, and Lemma 2.12 gives
$\|B_*u\|_{\mathbf o}\le C(\|Bu\|+\|u\|_{-K\mathbf 1})$ for $B_*$ microsupported where $B$'s cut-offs equal 1, which is
what Lemma 3.4 uses.

## 4. Elliptic and real principal type estimates

Throughout, $Z\subset\{z\in\mathbb C : |z|\in[\frac12,2],\ \mathrm{Im}\,z\ge0\}$ is compact, $P := P_{h,z}$ with $z\in
Z$, $\lambda := \mathrm{Im}\,z/h\in[0,2h^{-1}]$, and $\mathbf o = (s,\mathsf r,\mathsf b)$ with $s$ constant. Constants
are uniform in $z\in Z$ unless said otherwise. We write $\rho := \langle x\rangle^{-1}$, $\rho_\infty :=
\langle\zeta\rangle^{-1}$ and $\mu := \langle\zeta\rangle\langle x\rangle^{-1} = w_{(1,-1,0)}$. A function $a$ on
$\mathbb R^{2n}$ is *classical of order* $(k,l)$ if $\rho_\infty^k\rho^la$ extends smoothly to $\mathcal P$; then $a\in
S^{(k,l,0)}$, as derivatives of a smooth function on $\mathcal P$ gain $\langle x\rangle^{-1}$ in $x$ and
$\langle\zeta\rangle^{-1}$ in $\zeta$ (section 2.1). $\mathcal V_b(\mathcal P)$ denotes the smooth vector fields on
$\mathcal P$ tangent to both boundary faces.

### 4.1 The operator and its Hamilton field

**Lemma 4.1.** Assume (H1), (H2) and (H6).
(a) $G_0$, $\tau_1$ and $g_{00}$ are classical of orders $(2,0)$, $(1,0)$ and $(0,-2)$, and $\hat G_z :=
\rho_\infty^2G_z\in C^\infty(\mathcal P)$ depends polynomially on $z$. $P = \mathrm{Op}_h(p_{h,z})$ with
$p_{h,z}-G_z\mathrm{Id}\in S^{(1,-1,-1)}$, seminorms bounded uniformly for $z\in Z$; $\mathrm{Re}_hP$ has principal
symbol $\mathrm{Re}\,G_z\,\mathrm{Id}$.
(b) $\mathcal P_1(z)\in\Psi^{(1,-1,0)}$ and $\mathcal Q\in\Psi^{(1,0,0)}$, both $h$-self-adjoint and depending only on
$\mathrm{Re}\,z$; their principal symbols $p_1(z)$ and $q_z\mathrm{Id}$ satisfy $\mu^{-1}p_1(z)\in S^0$ and $\hat q_z :=
\rho_\infty q_z\in C^\infty(\mathcal P)$. At the face over $\partial X$, $q_z = -2\xi$.
(c) If $p$ is real and classical of order $(k,0)$, $k\le2$, then $\mu^{-1}H_p$ extends from $\mathbb R^{2n}$ to an
element of $\rho_\infty^{2-k}\mathcal V_b(\mathcal P)$. Hence
$$\mathsf H_z := \mu^{-1}H_{\mathrm{Re}\,G_z} = \mathsf H^{(0)}+(\mathrm{Re}\,z)\mathsf
H^{(1)}+\big((\mathrm{Re}\,z)^2-(\mathrm{Im}\,z)^2\big)\mathsf H^{(2)},\tag{4.1}$$
with $\mathsf H^{(0)} := \mu^{-1}H_{G_0}\in\mathcal V_b(\mathcal P)$, $\mathsf H^{(1)} :=
\mu^{-1}H_{\tau_1}\in\rho_\infty\mathcal V_b(\mathcal P)$ and $\mathsf H^{(2)} :=
\mu^{-1}H_{g_{00}}\in\rho^2\rho_\infty^2\mathcal V_b(\mathcal P)$. Thus $\mathsf H_z$ is a smooth vector field on
$\mathcal P$, tangent to both faces, depending polynomially on $(\mathrm{Re}\,z,\mathrm{Im}\,z)$; at fibre infinity it
does not depend on $z$, and $\mathsf H_z-\mathsf H_{\mathrm{Re}\,z} = -(\mathrm{Im}\,z)^2\mathsf H^{(2)}$ vanishes at
both faces. For $a\in C^\infty(\mathcal P)$, $H_{\mathrm{Re}\,G_z}a = \mu\,\mathsf H_za$, and $\mathsf
H_z\log\langle\zeta\rangle$, $\mathsf H_z\log\langle x\rangle$ lie in $C^\infty(\mathcal P)$.

Here $\mathsf H_{\mathrm{Re}\,z}$ is (4.1) at the real point $\mathrm{Re}\,z$. On the characteristic set over $\tilde
X^\circ$ and at fibre infinity $\mathsf H_{z_0}$ is, up to the positive factor $\mu^{-1}$, resp. $\rho^{-1}$, the field
$H_{G_{z_0}}$, resp. $\rho_\infty H_{G_0}$, of section 1.3 and (H3); over $\partial X$ it is
$\langle\zeta\rangle^{-1}\mathsf V_{G_{z_0}}$, with $H_p = \rho\mathsf V_p$ as in I.A Lemma 4.4 (c), so on the
characteristic set over $\partial X$ it vanishes exactly on $R_{z_0,\mathrm{in}}\cup R_{\mathrm{out}}$ (I.A Lemma 4.5,
read at $\sigma_0 = z_0$ in the variable $\zeta = h\xi$; the boundary symbol is homogeneous of degree 2 in
$(\sigma,\xi,\eta)$).

*Proof.* (a) By (H2), $\hat P(0) = \rho^2P^{(0)}$ with $P^{(0)}\in\mathrm{Diff}^2_b$, and a b-vector field is $\rho^{-1}$
times a scattering vector field; so $G_0$ is classical of order $(2,0)$. Likewise
$T\in\rho\mathrm{Diff}^1_b+\rho^3\mathrm{Diff}^1_b$ gives $\tau_1$ of order $(1,0)$, and $g_{00}\in\rho^2C^\infty$. The
rest is Lemma 1.1 (a) and Theorem 2.5: the $h$-adjoint of $\mathrm{Op}_h(G_z\mathrm{Id})$ is $\mathrm{Op}_h(\bar
G_z\mathrm{Id})$ modulo $S^{(1,-1,-1)}$. (b) $\sigma_1(T) = \tau_1\mathrm{Id}$ is real and scalar (H1), so
$\mathrm{Im}_hT$ has differential order 0: by I.A Lemma 4.4 (b) it is the matrix function $-\rho(S+S^{*h})+T_2$,
$T_2\in\rho^2C^\infty$, of order $(0,-1,0)$. $\mathrm{Im}_h\hat
P(0)\in\rho^2\mathrm{Diff}^1_b\subset\rho\,\mathrm{Diff}^1_{\mathrm{sc}}$, so $h\,\mathrm{Im}_h\hat
P(0)\in\Psi^{(1,-1,0)}$. $\mathcal Q = -h\,\mathrm{Re}_hT-2(\mathrm{Re}\,z)g_{00}$ has order $(1,0,0)$ and principal
symbol $-\tau_1-2(\mathrm{Re}\,z)g_{00}$, which is $-2\xi$ at the face by I.A Lemma 4.4 (a) and
$g_{00}\in\rho^2C^\infty$. (c) Near the face over $\partial X$, in polar coordinates $x = \omega/\rho$,
$\partial_{x_j}\in\rho\,\mathcal V_b(\overline{\mathbb R^n})$; near fibre infinity
$\partial_{\zeta_j}\in\rho_\infty\mathcal V_b(\overline{\mathbb R^n})$. For $p = \rho_\infty^{-k}\hat p$ with $\hat p$
smooth, $\partial_\zeta p\in\rho_\infty^{1-k}C^\infty(\mathcal P)$ and $\partial_xp = \rho_\infty^{-k}\partial_x\hat
p\in\rho_\infty^{-k}\rho\,C^\infty(\mathcal P)$, since b-vector fields preserve $C^\infty(\mathcal P)$. So
$H_p\in\rho_\infty^{1-k}\rho\,\mathcal V_b = \mu\,\rho_\infty^{2-k}\mathcal V_b$. For $g_{00}\in\rho^2C^\infty$ the
$x$-derivative gains a further $\rho^2$. Finally $\mathsf H_z\log\langle\zeta\rangle = -\rho_\infty^{-1}\mathsf
H_z\rho_\infty$ is smooth since $\mathsf H_z\rho_\infty\in\rho_\infty C^\infty$, and likewise for $\log\langle x\rangle =
-\log\rho$. $\square$

The *characteristic set* of $P$ is $\Sigma_z := \{\hat G_z = 0\}\subset\mathcal P$, closed. Over $\tilde X^\circ$ at
finite frequencies, $\Sigma_z = \emptyset$ for $\mathrm{Im}\,z>0$ (Lemma 1.1 (d)); at fibre infinity $\Sigma_z =
\partial\Sigma_0$ for every $z$; over $\partial X$, with $G_z = 2z\xi+\xi^2+|\eta|^2$ (I.A Lemma 4.4 (a)),
$\Sigma_z\cap\{\rho = 0\}$ is the sphere $\{(\xi+z_0)^2+|\eta|^2 = z_0^2\}$ if $z = z_0\in\mathbb R$, and the zero
section $R_{\mathrm{out}} := \{\rho = 0,\ \zeta = 0\}$ alone if $\mathrm{Im}\,z>0$ (the imaginary part
$2(\mathrm{Im}\,z)\xi$ forces $\xi = 0$, and then $|\eta| = 0$). For $z_0\in\{\pm1\}$ the radial sets over $\partial X$
are $R_{z_0,\mathrm{in}} := \{\rho = 0,\ \xi = -2z_0,\ \eta = 0\}$ and $R_{\mathrm{out}}$, and $\hat q_{z_0}$ has the
sign of $z_0$ on $\Sigma_{z_0}\cap\{\rho = 0\}\setminus R_{\mathrm{out}}$ and vanishes at $R_{\mathrm{out}}$.

### 4.2 The elliptic estimate

**Proposition 4.2.** Let $K\subset\mathcal P$ be compact with $\hat G_z\ne0$ on $K$ for every $z\in Z$, and
$B,G\in\Psi^0$ with $\mathrm{WF}'_h(B)\subset K$ and $G$ elliptic on $K$. Then for all orders $\mathbf o$ and all $K'$,
uniformly for $z\in Z$ and $h<h_0$,
$$\|Bu\|_{\mathbf o}\le C\big(\|GPu\|_{\mathbf o-\mathbf m}+\|u\|_{-K'\mathbf 1}\big)\le C\big(\|GPu\|_{\mathbf
o-\mathbf m+(1,1,0)}+\|u\|_{-K'\mathbf 1}\big).\tag{4.2}$$
The same holds for $P^{*h}$.

*Proof.* By compactness of $K\times Z$ there are a neighbourhood $U$ of $K$ and $c>0$ with $|\hat G_z|\ge c$ on $U$ for
$z\in Z$. Since $p_{h,z}-G_z\mathrm{Id}\in S^{(1,-1,-1)}$ is bounded by $Chw_{\mathbf m}$, $p_{h,z}$ is invertible on $U$
with $|p_{h,z}^{-1}|\le2c^{-1}w_{\mathbf m}^{-1}$ for $h<h_0$. Proposition 2.10 applies, with constants depending on
seminorms and on $c$ only. The second inequality is $\|f\|_{\mathbf o-\mathbf m}\le C\|f\|_{\mathbf o-\mathbf m+(1,1,0)}$
(Proposition 2.8). For $P^{*h}$ the symbol is $\bar G_z$ modulo $S^{(1,-1,-1)}$. $\square$

The second form is better by a factor $h$ than the estimates below, whose first term is $h^{-1}\|GPu\|_{\mathbf o-\mathbf
m+(1,1,0)}$.

### 4.3 Flow boxes with a parameter, and cut-offs

**Lemma 4.3.** Let $\Pi\subset\mathbb R^d$ be open and $(V_\pi)_{\pi\in\Pi}$ a family in $\mathcal V_b(\mathcal P)$
depending smoothly on $\pi$ (jointly smooth on $\mathcal P\times\Pi$). Let $\varpi_0\in\mathcal P$, $\pi_*\in\Pi$ and
$V_{\pi_*}(\varpi_0)\ne0$. Then there are neighbourhoods $\Pi_0$ of $\pi_*$ and $U$ of $\varpi_0$, $\tau>0$, and
functions $t,y_1,\dots,y_{2n-1}$ smooth on $U\times\Pi_0$ such that for each $\pi\in\Pi_0$: $(t,y)(\cdot,\pi)$ is a
diffeomorphism of $U$ onto $(-\tau,\tau)\times Y_\pi$ with $Y_\pi$ open in $[0,\infty)^k\times\mathbb R^{2n-1-k}$, where
$k\in\{0,1,2\}$ is the number of faces through $\varpi_0$ and the first $k$ components of $y$ are defining functions of
those faces; $V_\pi t = 1$ and $V_\pi y = 0$; and $t(\varpi_0,\pi) = 0$, $y(\varpi_0,\pi) = y_0$ independent of $\pi$.
The same coordinates serve every point $\varpi\in U$ with $|t(\varpi,\pi)|<\tau/2$, after translation in $t$, with
$\tau/2$ in place of $\tau$.

*Proof.* Choose coordinates $(\varrho_1,\dots,\varrho_k,w)$ near $\varpi_0$ with $\varrho_i$ defining the faces through
$\varpi_0$, and extend $V_\pi$ smoothly to a neighbourhood of $\varpi_0$ in $\mathbb R^{2n}$ (allowing $\varrho_i<0$).
Tangency gives $V_\pi\varrho_i = \varrho_if_i$ with $f_i$ smooth, so $V_{\pi_*}(\varpi_0)$ lies in the span of the
$\partial_w$; after a linear change of $w$, $V_{\pi_*}(\varpi_0) = \partial_{w_1}$. Let $S := \{w_1 = 0\}$ and
$\Phi(t,\sigma,\pi) := \exp(tV_\pi)(\sigma)$ for $\sigma\in S$ near $\varpi_0$. $\Phi$ is smooth, and
$(t,\sigma)\mapsto\Phi$ has invertible differential at $(0,\varpi_0,\pi_*)$; the inverse function theorem applied to
$(t,\sigma,\pi)\mapsto(\Phi(t,\sigma,\pi),\pi)$ gives a smooth inverse on a neighbourhood. Take $y :=
(\varrho_1,\dots,\varrho_k,w_2,\dots)$ of $\sigma$. Along the flow $\varrho_i(\Phi(t,\sigma,\pi)) =
\varrho_i(\sigma)\exp\int_0^tf_i$, so the flow preserves each face and each side of it: the inverse maps $\mathcal P$ to
$\{\varrho_i(\sigma)\ge0\}$, and $y_i = \varrho_i(\sigma)$ is a positive smooth multiple of $\varrho_i$. $V_\pi t = 1$,
$V_\pi y = 0$ by construction. The last statement is the translation $t\mapsto t-t(\varpi)$. $\square$

**Lemma 4.4.** There is $\chi\in C^\infty(\mathbb R)$ with $\chi = 0$ on $(-\infty,0]$, $\chi = 1$ on $[1,\infty)$,
$\chi'\ge0$, and $\sqrt{\chi\chi'}\in C^\infty(\mathbb R)$.

*Proof.* Let $\psi_1\in C^\infty((0,\infty))$, $\psi_1\ge0$, with $\psi_1(s) = 1/s$ on $(0,\frac12]$ and $\psi_1 = 0$ on
$[1,\infty)$. On $(0,\infty)$ put $\phi(t) := \int_t^1\psi_1(s)^2\,ds$ and $\chi := e^{-\phi}$. Then $\phi = 1/t+c$ near
$0$, so $\chi$ and all its derivatives tend to 0 as $t\to0^+$; set $\chi := 0$ on $(-\infty,0]$. $\chi' =
\psi_1^2\chi\ge0$, $\chi = 1$ on $[1,\infty)$, and $\sqrt{\chi\chi'} = \psi_1e^{-\phi}$, whose derivatives are
polynomials in $1/t$ times $e^{-1/t}$ near 0. $\square$

### 4.4 Propagation

For $\epsilon_\flat\in\{1,-1\}$ write $P_{\epsilon_\flat} := P$ if $\epsilon_\flat = 1$ and $P^{*h}$ if $\epsilon_\flat =
-1$. Then $\mathrm{Re}_hP_{\epsilon_\flat} = \mathrm{Re}_hP$ and, by (1.3),
$$h^{-1}\mathrm{Im}_hP_{\epsilon_\flat} = \epsilon_\flat\mathcal P_1(z)-\lambda\,\epsilon_\flat\mathcal Q.\tag{4.3}$$

**Proposition 4.5 (propagation).** Let $\epsilon_\flat,\varsigma\in\{1,-1\}$, $z_*\in Z$ and $\varpi_0\in\mathcal P$ with
$\mathsf H_{z_*}(\varpi_0)\ne0$ and $\epsilon_\flat\varsigma\hat q_{z_*}(\varpi_0)>0$. Let $U_0$ be a neighbourhood of
$\varpi_0$ such that for $z\in Z$
$$\varsigma\mathsf H_{\mathrm{Re}\,z}\mathsf b\le0\ \text{on}\ U_0,\qquad\varsigma\mathsf H_{\mathrm{Re}\,z}\mathsf
r\le0\ \text{on}\ U_0\cap\{\rho = 0\}.\tag{4.4}$$
Let $\gamma$ be the integral curve of $\varsigma\mathsf H_{z_*}$ with $\gamma(0) = \varpi_0$. There is $T_0>0$ such that
for every neighbourhood $W$ of $\gamma(-T_0/2)$ there are a neighbourhood $Z_0$ of $z_*$ in $Z$, a neighbourhood $U_*$ of
$\gamma([-T_0/4,0])$ and a compact set $K_E\subset W$ with the following property: for $B_*\in\Psi^0$ microsupported in
$U_*$, $E'\in\Psi^0$ elliptic on $K_E$, $G\in\Psi^0$ elliptic on $\bar U_0$, all $N,K$, $z\in Z_0$, $h<h_0$ and Schwartz
$u$,
$$\|B_*u\|_{\mathbf o}\le C\big(h^{-1}\|GP_{\epsilon_\flat}u\|_{\mathbf o-\mathbf m+(1,1,0)}+\|E'u\|_{\mathbf
o}+h^N\|Gu\|_{\mathbf o}+\|u\|_{-K\mathbf 1}\big).\tag{4.5}$$

So estimates propagate along $\varsigma\mathsf H$ where $\varsigma$ has the sign of $\epsilon_\flat q$: for $P$, along
the future field $\mathrm{sgn}(q)\mathsf H$ of section 1.3; for $P^{*h}$, along the past field. The hypothesis (4.4) is
stated for $\mathsf H_{\mathrm{Re}\,z}$ and not $\mathsf H_z$; the difference is absorbed in the proof by the term
$\lambda\mathcal Q$, which is where $\mathrm{Im}\,z\ge0$ is used.

*Proof.* *Step 0: the box.* Apply Lemma 4.3 to $V_\pi := \varsigma\mathsf H_z$, $\pi = (\mathrm{Re}\,z,\mathrm{Im}\,z)$,
the formula (4.1) defining it for all $\pi\in\mathbb R^2$. This gives $\Pi_0$, $U_1\subset U_0$ and $\tau$; shrink them
so that $\bar U_1\subset U_0$ is compact and $\epsilon_\flat\varsigma\hat q_z\ge c_0>0$ on $U_1$ for $z\in Z_0 :=
Z\cap\Pi_0$ ($\hat q_z$ is continuous in $(\varpi,\mathrm{Re}\,z)$). Put $T_0 := \tau/4$. In the coordinates of $z_*$,
$\gamma(t) = (t,y_0)$.

*Step 1: one commutant.* Fix $z\in Z_0$, numbers $t_-<t_+$ in $(-3T_0,T_0)$, $\epsilon\in(0,T_0/8]$ and $\eta_1>0$ such
that $\{t\in[t_--\epsilon,t_++\epsilon],|y-y_0|\le\eta_1+\epsilon\}\subset U_1$ in the coordinates of $z$. With $\chi$
from Lemma 4.4 put $\chi_-(t) := \chi((t-t_-+\epsilon)/\epsilon)$, $\chi_+(t) := \chi((t_++\epsilon-t)/\epsilon)$,
$\psi(y) := \chi\big(((\eta_1+\epsilon)^2-|y-y_0|^2)/(2\eta_1\epsilon+\epsilon^2)\big)$, and
$$\varphi := e^{-Mt}\chi_-(t)\chi_+(t)\psi(y),\qquad\check a := w_{\mathbf k}\varphi,\qquad\check A :=
\tfrac12\big(\mathrm{Op}_h(\check a\mathrm{Id})+\mathrm{Op}_h(\check a\mathrm{Id})^{*h}\big),$$
with $\mathbf k$ from (3.2) and $M$ chosen below. $\varphi\in C_c^\infty(U_1)$, so $\check a\in S^{\mathbf k}$ with
seminorms uniform in $z\in Z_0$, and $\check A = \check A^{*h}$ has principal symbol $\check a\mathrm{Id}$. Let $C$ be
(3.1) for $P_{\epsilon_\flat}$. By (4.3), $C = C'-\lambda\epsilon_\flat(\check A^2\mathcal Q+\mathcal Q\check A^2)$ with
$C' := \frac ih[\mathrm{Re}_hP,\check A^2]+\epsilon_\flat(\check A^2\mathcal P_1+\mathcal P_1\check A^2)$, and by section
3.2 and Lemma 4.1 the principal symbol of $\varsigma C'$ is $\varsigma\mu\mathsf H_z(\check
a^2)+2\varsigma\epsilon_\flat\check a^2p_1(z)$, with remainder in $\Psi^{2\mathbf o-\mathbf 1+\epsilon'\mathbf 1}$. Since
$\mu w_{\mathbf k}^2 = w_{2\mathbf o}$, $\varsigma\mathsf H_zt = 1$ and $\mathsf H_z\psi = 0$,
$$\varsigma\mu\mathsf H_z(\check a^2)+2\varsigma\epsilon_\flat\check a^2p_1 = w_{2\mathbf
o}\big[2\varphi\partial_t\varphi+\varphi^2\big(\beta+2(\varsigma\mathsf H_z\mathsf r)\log\langle
x\rangle+2(\varsigma\mathsf H_z\mathsf b)\log\tfrac1h\big)\big],$$
$$\beta := 2(s-\tfrac12)\varsigma\mathsf H_z\log\langle\zeta\rangle+2(\mathsf r+\tfrac12)\varsigma\mathsf H_z\log\langle
x\rangle+2\varsigma\epsilon_\flat\mu^{-1}p_1(z),$$
using $\log w_{\mathbf k} = (s-\frac12)\log\langle\zeta\rangle+(\mathsf r+\frac12)\log\langle x\rangle+\mathsf
b\log\frac1h$. $\beta$ is bounded on $U_1$ uniformly in $z$ (Lemma 4.1) and $h$-self-adjoint. Next,
$2\varphi\partial_t\varphi = -2M\varphi^2+e^2-f_+^2$ with
$$e := e^{-Mt}\psi\chi_+\sqrt{2\chi_-\chi_-'},\qquad f_+ := e^{-Mt}\psi\chi_-\sqrt{-2\chi_+\chi_+'},$$
smooth by Lemma 4.4, $e$ supported in $\{t\in[t_--\epsilon,t_-]\}$ and $f_+$ in $\{t\in[t_+,t_++\epsilon]\}$.

*The decay order.* $f_r := \varsigma\mathsf H_{\mathrm{Re}\,z}\mathsf r$ is smooth on $\mathcal P$ and $\le0$ on
$U_0\cap\{\rho = 0\}$, so $f_r\le C_r\rho$ on $\bar U_1$, uniformly in $z$. By Lemma 4.1, $\varsigma\mathsf H_z\mathsf r
= f_r-\varsigma(\mathrm{Im}\,z)^2\mathsf H^{(2)}\mathsf r$ with $|\mathsf H^{(2)}\mathsf r|\le C\rho^2$. Let
$\tilde\chi\in C_c^\infty(U_1)$, $0\le\tilde\chi\le1$, equal 1 on a neighbourhood of every $\mathrm{supp}\,\varphi$
considered. Then on $\mathrm{supp}\,\varphi$
$$2(\varsigma\mathsf H_z\mathsf r)\log\langle x\rangle = -\lambda_r+\beta_r,\qquad\lambda_r :=
2\tilde\chi(C_r\rho-f_r)\log\langle x\rangle\ge0,$$
with $\beta_r := 2\big(C_r\rho-\varsigma(\mathrm{Im}\,z)^2\mathsf H^{(2)}\mathsf r\big)\log\langle x\rangle$ bounded with
all derivatives obeying (2.1).

*The semiclassical order.* $f_b := \varsigma\mathsf H_{\mathrm{Re}\,z}\mathsf b\le0$ on $U_0$; put $\lambda_b :=
-2\tilde\chi f_b\log\frac1h\ge0$. The rest is $-2\varsigma(\mathrm{Im}\,z)^2(\mathsf H^{(2)}\mathsf b)\log\frac1h =
-\lambda\,c_b$ with $c_b := 2\varsigma h(\mathrm{Im}\,z)\log\frac1h\,\mathsf H^{(2)}\mathsf b$; note $|c_b|\le
Ch\log\frac1h\,\rho^2\rho_\infty^2$.

Let $Q_0 := 2M-\beta-\beta_r$ on $U_1$, and choose $M$ with $Q_0\ge M\mathrm{Id}$ there for $z\in Z_0$; replace $Q_0$ by
$\tilde\chi Q_0+(1-\tilde\chi)M\mathrm{Id}$, which is $\ge M\mathrm{Id}$ everywhere. $\lambda_0 := \lambda_r+\lambda_b$
satisfies the hypotheses of Lemma 2.12. With
$$b := w_{\mathbf o}\varphi(Q_0+\lambda_0)^{1/2},\qquad B := \mathrm{Op}_h(b),\quad E := \mathrm{Op}_h(w_{\mathbf
o}e\,\mathrm{Id}),\quad F_+ := \mathrm{Op}_h(w_{\mathbf o}f_+\mathrm{Id}),$$
the principal symbol of $\varsigma C'$ is $-b^2+w_{2\mathbf o}e^2-w_{2\mathbf o}f_+^2-\lambda w_{2\mathbf
o}\varphi^2c_b$, and $b$ is $h$-self-adjoint, as $Q_0$ is. So
$$\varsigma C' = -B^{*h}B+E^{*h}E-F_+^{*h}F_+-\lambda\,\check A\,\mathrm{Op}_h(\mu c_b\tilde\chi)\check A+R_1,\qquad
R_1\in\Psi^{2\mathbf o-\frac12\mathbf 1}:$$
the principal symbols agree; $B\in\Psi^{\mathbf o+\epsilon'\mathbf 1}$ (Lemma 2.12), so $B^{*h}B$ is determined by its
principal symbol modulo $\Psi^{2\mathbf o-\mathbf 1+3\epsilon'\mathbf 1}$; and $\mu c_b\in S^{(1,-1,-1+\epsilon')}$, so
$\check A\,\mathrm{Op}_h(\mu c_b\tilde\chi)\check A$ is determined modulo $\Psi^{2\mathbf k+(1,-1,-1+\epsilon')-\mathbf
1+\epsilon'\mathbf 1} = \Psi^{2\mathbf o-(1,1,2)+2\epsilon'\mathbf 1}$, which $\lambda\le2h^{-1}$ turns into
$\Psi^{2\mathbf o-\mathbf 1+2\epsilon'\mathbf 1}$.

*The absorbing term.* By $X\check A^2+\check A^2X = 2\check AX\check A+[[X,\check A],\check A]$, $\varsigma C = \varsigma
C'-2\lambda\check A(\varsigma\epsilon_\flat\mathcal Q)\check A-\lambda\varsigma[[\epsilon_\flat\mathcal Q,\check
A],\check A]$. Let $\mathcal Q_\sharp$ be the $h$-self-adjoint part of $\varsigma\epsilon_\flat\mathcal
Q+\frac12\mathrm{Op}_h(\mu c_b\tilde\chi)$. Then $\varsigma C = -B^{*h}B-F+E^{*h}E+R$, where
$$F := 2\lambda\check A\mathcal Q_\sharp\check A+F_+^{*h}F_+,\qquad R := R_1-\lambda\varsigma[[\epsilon_\flat\mathcal
Q,\check A],\check A]-\lambda\check A\,\mathrm{Op}_h(\mu c_b\tilde\chi)^{\mathrm a}\check A,$$
the last term involving the anti-self-adjoint part $\mathrm{Op}_h(\mu c_b\tilde\chi)^{\mathrm
a}\in\Psi^{(0,-2,-2+\epsilon')}$ of $\mathrm{Op}_h(\mu c_b\tilde\chi)$ (its symbol is real, Theorem 2.5), hence in
$\Psi^{2\mathbf o-(1,1,1)+(0,0,\epsilon')}$.
$\mathcal Q_\sharp\in\Psi^{(1,0,0)}$ has principal symbol $\epsilon_\flat\varsigma q_z$ (the added term is of lower
order), which is $\ge c_0\langle\zeta\rangle$ on $U_1$; so by the paragraph *Positivity of absorbing terms* of section
3.3, with $\mathbf t = (\frac12,0,0)$, $\langle Fw,w\rangle\ge-C\|w\|^2_{-K\mathbf 1}$, and the double commutator lies in
$\lambda\Psi^{2\mathbf k+(1,0,0)-2\mathbf 1+\epsilon'\mathbf 1}\subset\Psi^{2\mathbf o-\frac12\mathbf 1}$. So
$R\in\Psi^{2\mathbf o-\frac12\mathbf 1}$. Finally $\check A = ZB+Y$ with $Z := \mathrm{Op}_h(w_{\mathbf k-\mathbf
o}\tilde\chi(Q_0+\lambda_0)^{-1/2})\in\Psi^{-\frac12(\mathbf m-(1,1,0))}$ (Lemma 2.12) and $Y\in\Psi^{\mathbf
k-\frac12\mathbf 1}$, since the principal symbol of $ZB$ is $\check a$. So (3.3) holds with $J = 0$, $K_1 :=
\mathrm{supp}\,\varphi$ and $K_E := \mathrm{supp}\,e$, and by Lemma 2.12, $B$ is elliptic, in the sense of Proposition
2.10, on $\{\varphi\ne0\}\supset\{t\in(t_--\epsilon,t_++\epsilon),\ |y-y_0|<\eta_1+\epsilon\}$. All seminorms and $C_F$
are uniform in $z\in Z_0$ and in the parameters $t_\pm,\epsilon,\eta_1$ on compact sets of them.

*Step 2: iteration.* Let $\eta>0$, to be fixed by $W$. In the coordinates of $z$ put $\Lambda_z :=
\{t\in[-T_0/2,0],|y-y_0|\le\eta\}$, $c_j := 2^{-j}c_0$ for $j = 0,\dots,J := 4N$, with $c_0\le T_0/4$, and $U_j(z) :=
\{t\in(-T_0/2-3c_j,2c_j),\ |y-y_0|<\eta+2c_j\}$, a decreasing sequence. The proof of Lemma 3.4 uses its hypothesis only
for the sets $U_0\supset\dots\supset U_J$ it chooses, the $j$-th being the set $U'$ for the $(j-1)$-st; here Step 1 with
$t_- := -T_0/2-2c_j$, $t_+ := c_j$, $\epsilon := c_j-c_{j+1}$, $\eta_1 := \eta+c_j$ gives a commutant microsupported in
$U_j(z)$ whose $B$ is elliptic on $\{t\in(-T_0/2-3c_j+c_{j+1},2c_j-c_{j+1}),\ |y-y_0|<\eta+2c_j-c_{j+1}\}\supset\bar
U_{j+1}(z)$, as $c_{j+1} = c_j/2$, with $K_E\subset\{t\in[-T_0/2-3c_j,-T_0/2-2c_j]\}$, disjoint from $\Lambda_z$. So
(3.5) holds for $B_*$ microsupported in $U_J(z)$ and $E'$ elliptic on $K^*_E(z) :=
\bigcup_jK_E\subset\{t\in[-T_0/2-3c_0,-T_0/2-2c_J],\ |y-y_0|\le\eta+2c_0\}$, uniformly in $z\in Z_0$.

*Step 3: removing $z$ from the sets.* Given $W$, choose $\eta$ and shrink $c_0$ (all $c_j$ by a common factor) so that,
in the coordinates of $z_*$, $\{t\in[-T_0/2-4c_0,-T_0/2],|y-y_0|\le\eta+3c_0\}\subset W$. As the coordinates depend
continuously on $z$ in $C^\infty$, there is a neighbourhood $Z_0'\subset Z_0$ of $z_*$ such that for $z\in Z_0'$ the set
$K_E^*(z)$ lies in the compact set $K_E := \{t_{z_*}\in[-T_0/2-4c_0,-T_0/2-c_J],|y_{z_*}-y_0|\le\eta+3c_0\}\subset W$,
and $U_J(z)$ contains $U_* := \{t_{z_*}\in(-T_0/4-c_J,c_J),|y_{z_*}-y_0|<\eta\}$, a neighbourhood of
$\gamma([-T_0/4,0])$. Then (4.5) holds for $z\in Z_0'$; rename $Z_0'$ as $Z_0$. $\square$

**Corollary 4.6 (propagation along a segment).** Let $\epsilon_\flat,\varsigma$ be signs, $z_*\in Z$, and
$\gamma:[-T,0]\to\mathcal P$ an integral curve of $\varsigma\mathsf H_{z_*}$ with $\mathsf H_{z_*}\ne0$ and
$\epsilon_\flat\varsigma\hat q_{z_*}>0$ on $\gamma([-T,0])$. Let $U_0$ be a neighbourhood of $\gamma([-T,0])$ on which
(4.4) holds. Then for every neighbourhood $W$ of $\gamma(-T)$ there are a neighbourhood $Z'$ of $z_*$, a neighbourhood
$U_*$ of $\gamma(0)$ and a compact $K_E\subset W$ such that (4.5) holds for $z\in Z'$, $B_*$ microsupported in $U_*$,
$E'$ elliptic on $K_E$ and $G$ elliptic on $\bar U_0$.

*Proof.* $U_0$ contains $\gamma([-T-\delta_0,\delta_0])$ for some $\delta_0>0$, and after shrinking $\delta_0$ the
hypotheses hold on that longer segment. The flow boxes of Lemma 4.3 at its points have sizes bounded below, since a box
at $\varpi$ serves a neighbourhood of $\varpi$ with half its size (Lemma 4.3); so Proposition 4.5 holds at every
$\gamma(t)$ with one $T_1>0$ in place of $T_0$, which we may decrease so that $T_1\le\delta_0/8$ and $L :=
4(T-T_1/2)/T_1\in\mathbb N$. Let $\tau_l := -T+T_1/2+(l-1)T_1/4$, $l = 1,\dots,L+1$, so $\tau_{L+1} = 0$. Apply
Proposition 4.5 at $\gamma(\tau_1)$ with $W_1 := W$, a neighbourhood of $\gamma(\tau_1-T_1/2) = \gamma(-T)$; this gives
$Z^{(1)}$, $U^{(1)}_*\supset\gamma([\tau_1-T_1/4,\tau_1])$ and $K_E^{(1)}\subset W$. For $l\ge2$ apply it at
$\gamma(\tau_l)$ with $W_l := U_*^{(l-1)}$, a neighbourhood of $\gamma(\tau_l-T_1/2) = \gamma(\tau_{l-1}-T_1/4)$. The
operator $E'_l$ elliptic on $K_E^{(l)}\subset U_*^{(l-1)}$ may be taken microsupported in $U_*^{(l-1)}$, so it is an
admissible $B_*$ at step $l-1$. Chaining the $L+1$ estimates, with $Z' := \bigcap_lZ^{(l)}$ and $U_* := U_*^{(L+1)}$,
gives the claim. $\square$

*Remark 4.7.* Over a compact subset of $T^*\tilde X^\circ$ at finite frequencies, Proposition 4.5 and Corollary 4.6 also
hold (a) for $z = z_0+iy$ with $y\in[-Ch,0]$: then $\lambda\in[-C,0]$, $\lambda\mathcal Q$ is a bounded term of the class
of $\mathcal P_1$ there, it is put into $\beta$, and the condition $\epsilon_\flat\varsigma\hat q>0$ is not needed (for
$|\lambda|\le C$ the same holds with either sign of $\mathrm{Im}\,z$); and (b) when $h^{-1}\mathrm{Im}_h\mathbf P$
contains a further term $-\theta h^{-1}W^{*h}W$, $\theta\in\{1,-1\}$, with $W\in\Psi^{(1,0,0)}$ scalar, and a further
bounded term of the class of $\mathcal P_1$, provided $\varsigma\theta = 1$: the first enters $\varsigma C$ as
$-2h^{-1}\check AW^{*h}W\check A$ plus a double commutator in $h\Psi$, a term $-F$ with $\langle Fw,w\rangle\ge0$
exactly, as in Lemma 5.1 (B), and the second is part of $\beta$. Both are used in section 6 only.

The admissibility of section 1.4 is used through (4.4): it requires the monotonicity on a *neighbourhood* $U_0$ of the
curves along which we propagate (for $\mathsf r$, a neighbourhood within the face over $\partial X$), not only on the
characteristic set. A logarithmic weight $\log\frac1h$ multiplies $\mathsf H\mathsf b$, so a positive value of $\mathsf
H\mathsf b$ off the characteristic set but on the support of a commutant could not be absorbed. Section 1.4 is stated in
this form.

## 5. Radial estimates

The three radial sets are $\partial\mathcal R_\pm$ at fibre infinity over the horizon, and $R_{z_0,\mathrm{in}}$,
$R_{\mathrm{out}}$ over $\partial X$. One lemma serves all three, for the operator and its adjoint. Notation is that of
section 4.

### 5.1 A radial estimate

Let $\mathbf P$ be one of $c_zP$, $(c_zP)^{*h}$, where $c_z\in\{1,z^{-1}\}$ is fixed, and let $\epsilon_\flat := 1$,
resp. $-1$. Then $\mathrm{Re}_h\mathbf P = \mathrm{Re}_h(c_zP)$ and $\mathrm{Im}_h\mathbf P =
\epsilon_\flat\mathrm{Im}_h(c_zP)$; since $|c_z|\in[\frac12,2]$, an estimate for $\mathbf P$ is one for $P$, resp.
$P^{*h}$.

**Lemma 5.1 (radial estimate).** Let $F$ be one of the two boundary faces of $\mathcal P$, with defining function
$\varrho$ ($\rho_\infty$ or $\rho$), $Z'\subset Z$ compact, $\Lambda\subset F$ compact, $U_0$ a neighbourhood of
$\Lambda$ with compact closure, and $\varsigma\in\{1,-1\}$. Suppose, uniformly for $z\in Z'$:
(i) $\mathrm{Re}_h\mathbf P-\mathrm{Op}_h(p_z\mathrm{Id})\in\Psi^{(1,-1,-1)}$, $p_z$ real and classical of order $(2,0)$,
continuous in $z$; $\mathsf H^{\mathbf P}_z := \mu^{-1}H_{p_z}$ (Lemma 4.1 (c)) vanishes at every point of $\Lambda$, and
$\beta_\varrho := \varrho^{-1}\varsigma\mathsf H^{\mathbf P}_z\varrho$ satisfies either $\beta_\varrho\ge\beta_*$ on
$U_0$ (*source*) or $\beta_\varrho\le-\beta_*$ on $U_0$ (*sink*), for some $\beta_*>0$.
(ii) $h^{-1}\mathrm{Im}_h\mathbf P = \epsilon_\flat(\mathcal P^{\mathbf P}_1-\lambda\mathcal A)$ with $\mathcal
P^{\mathbf P}_1\in\Psi^{(1,-1,0)}$ $h$-self-adjoint, of principal symbol $p^{\mathbf P}_1$, and either (A)
$\epsilon_\flat\varsigma\mathcal A\in\Psi^{(1,0,0)}$ is $h$-self-adjoint with principal symbol $\ge
c_0\langle\zeta\rangle\mathrm{Id}$ on $U_0$; or (B) $\bar U_0$ lies at finite frequencies, $\epsilon_\flat\varsigma = 1$
and $\mathcal A = \sum_{j,k}W_j^{*h}\tilde M_{jk}W_k+\mathcal A_0+\mathcal A_1$, where the $W_j\in\Psi^{(1,0,0)}$ are
scalar semiclassical differential operators acting componentwise, $\tilde M = (\tilde M_{jk})$ and $\mathcal A_0$ are
matrix functions with $\tilde M\ge0$ for $h^{\oplus J}$ and $\mathcal A_0\ge0$ for $h$ everywhere, and $\mathcal A_1$ is
a differential operator whose coefficients vanish near the base projection of $\bar U_0$.
(iii) There are real $g,\phi\in C^\infty(\mathcal P)$, continuous in $z$, $\phi\ge0$, with $\Lambda = \bar
U_0\cap\{\varrho = 0,\ \phi = 0,\ g = 0\}$, $|\rho_\infty^2\mathbf g_z|\ge c|g|-C\varrho$ on $U_0$ where $\mathbf g_z$ is
the principal symbol of $\mathbf P$, and on $U_0$
$$\varsigma\mathsf H^{\mathbf P}_z\phi\ge c_1\phi-C_1(\varrho+g^2)\ \ (\text{source}),\qquad\varsigma\mathsf H^{\mathbf
P}_z\phi\le-c_1\phi+C_1(\varrho+g^2)\ \ (\text{sink}).\tag{5.1}$$
(iv) $\mathsf r$ and $\mathsf b$ are constant on $U_0$. Put $\tilde\kappa := s-\frac12$ if $F$ is fibre infinity and
$\tilde\kappa := \mathsf r+\frac12$ if $F$ is the face over $\partial X$.
(v) (*Threshold.*) On $\Lambda$ the $h$-self-adjoint endomorphism
$$\mathcal T := 2\tilde\kappa\,\beta_\varrho\,\mathrm{Id}-2\varsigma\epsilon_\flat\,\mu^{-1}p^{\mathbf P}_1\tag{5.2}$$
satisfies $\mathcal T\ge c_{\mathcal T}\mathrm{Id}$, $c_{\mathcal T}>0$.
Then there are a neighbourhood $U_*$ of $\Lambda$ and a compact set $K_E\subset\bar U_0\setminus\Lambda$ such that for
$B_*\in\Psi^0$ microsupported in $U_*$, $G\in\Psi^0$ elliptic on $\bar U_0$, $E'\in\Psi^0$ elliptic on $K_E$, all $N,K$,
$z\in Z'$, $h<h_0$ and Schwartz $u$,
$$\|B_*u\|_{\mathbf o}\le C\big(h^{-1}\|G\mathbf Pu\|_{\mathbf o-\mathbf
m+(1,1,0)}+\delta_{\mathrm{sink}}\|E'u\|_{\mathbf o}+h^N\|Gu\|_{\mathbf o}+\|u\|_{-K\mathbf 1}\big),\tag{5.3}$$
where $\delta_{\mathrm{sink}} := 0$ in the source case and $1$ in the sink case.

So at a source the estimate needs no control near $\Lambda$, and at a sink it needs control on a punctured neighbourhood;
the threshold (5.2) decides which orders are allowed. In the source case (5.2) asks $\tilde\kappa$ to be large (a high
regularity or decay order), in the sink case small.

*Proof.* *The cut-offs.* Let $\chi_0(t) := \chi(2-t)$ with $\chi$ from Lemma 4.4: $\chi_0 = 1$ on $(-\infty,1]$, $\chi_0
= 0$ on $[2,\infty)$, $\chi_0'\le0$, $\sqrt{-\chi_0\chi_0'}$ smooth. For $\delta = (\delta_1,\delta_2,\delta_3)$ put
$$\varphi_\delta := \chi_0(\varrho/\delta_1)\,\chi_0(\phi/\delta_2)\,\chi_0(g^2/\delta_3)\ \text{on}\ U_0,\qquad
K_\delta := \bar U_0\cap\{\varrho\le2\delta_1,\ \phi\le2\delta_2,\ g^2\le2\delta_3\}.$$
The compact sets $K_\delta$ decrease to $\Lambda$ as $\delta\to0$, so $K_\delta\subset U_0$ for $\delta$ small, and then
$\varphi_\delta$, extended by 0, is smooth on $\mathcal P$ with support in $K_\delta$; and every neighbourhood of
$\Lambda$ contains $K_\delta$ for $\delta$ small. We take $\delta_1\le c_\delta\min(\delta_2,\sqrt{\delta_3})$ and
$\delta_3\le c_\delta\delta_2$, with $c_\delta := \min(c_1/(16C_1),c/(4C),1)$; this is preserved by
$\delta\mapsto\delta/4$. Then: on $\mathrm{supp}\,\chi_0'(\phi/\delta_2)\cap K_\delta$ we have $\phi\ge\delta_2$, so by
(5.1) $\pm\varsigma\mathsf H^{\mathbf P}_z\phi\ge c_1\delta_2-C_1(2\delta_1+2\delta_3)\ge\frac12c_1\delta_2$ (upper sign
at a source, lower at a sink); and on $\mathrm{supp}\,\chi_0'(g^2/\delta_3)\cap K_\delta$, $|\rho_\infty^2\mathbf g_z|\ge
c\sqrt{\delta_3}-2C\delta_1>0$, so $\mathbf P$ is elliptic there.

*The commutant.* $\check a := w_{\mathbf k}\varphi_\delta$, $\check A := \frac12(\mathrm{Op}_h(\check
a\mathrm{Id})+\mathrm{Op}_h(\check a\mathrm{Id})^{*h})$, $\mathbf k$ from (3.2). As in Step 1 of Proposition 4.5, with
$\mathsf r,\mathsf b$ constant on $U_0$, the principal symbol of $\varsigma C'$ (where $C =
C'-\lambda\epsilon_\flat(\check A^2\mathcal A+\mathcal A\check A^2)$) is $w_{2\mathbf o}[2\varphi_\delta\varsigma\mathsf
H^{\mathbf P}_z\varphi_\delta+\varphi_\delta^2\beta]$ with
$$\beta := 2(s-\tfrac12)\varsigma\mathsf H^{\mathbf P}_z\log\langle\zeta\rangle+2(\mathsf r+\tfrac12)\varsigma\mathsf
H^{\mathbf P}_z\log\langle x\rangle+2\varsigma\epsilon_\flat\mu^{-1}p^{\mathbf P}_1.$$
At $\Lambda\subset F$: one of $\log\langle\zeta\rangle,\log\langle x\rangle$ is $\log\varrho^{-1}$, with
$\varsigma\mathsf H\log\varrho^{-1} = -\beta_\varrho$; the other is smooth near $\Lambda$, so its derivative along
$\mathsf H^{\mathbf P}_z$ vanishes on $\Lambda$, where the vector field vanishes. So $\beta = -\mathcal T$ on $\Lambda$,
and $-\beta\ge\frac12c_{\mathcal T}\mathrm{Id}$ on $K_\delta$ for $\delta$ small, uniformly in $z\in Z'$. Let $Q_0 :=
\tilde\chi(-\beta)+(1-\tilde\chi)\frac12c_{\mathcal T}\mathrm{Id}$ with $\tilde\chi\in C_c^\infty(U_0)$ equal to 1 on
$K_\delta$, and $b := w_{\mathbf o}\varphi_\delta Q_0^{1/2}\in S^{\mathbf o}$.

*The cut-off terms.* $2\varphi_\delta\varsigma\mathsf H\varphi_\delta = \sum_{i=1}^3k_i$, where, with $a_1 := \varrho$,
$a_2 := \phi$, $a_3 := g^2$ and $\varphi_i := \chi_0(a_i/\delta_i)$, $k_i :=
2\varphi_i\chi_0'(a_i/\delta_i)\delta_i^{-1}(\varsigma\mathsf H a_i)\prod_{j\ne i}\varphi_j^2$. Since
$\chi_0\chi_0'\le0$: $k_1$ has the sign of $-\beta_\varrho\varrho$, and $k_2$ that of $\mp1$, on their supports; $k_3$ is
supported where $\mathbf P$ is elliptic. In the source case $k_1 = -f_1^2$, $k_2 = -f_2^2$ with
$$f_1 := \sqrt{-2\chi_0\chi_0'}(\varrho/\delta_1)\,(\beta_\varrho\varrho/\delta_1)^{1/2}\varphi_2\varphi_3,\qquad f_2 :=
\sqrt{-2\chi_0\chi_0'}(\phi/\delta_2)\,(\varsigma\mathsf H\phi/\delta_2)^{1/2}\varphi_1\varphi_3,$$
smooth, because $\beta_\varrho\varrho\ge\beta_*\delta_1$ and $\varsigma\mathsf H\phi\ge\frac12c_1\delta_2$ on a
neighbourhood of the supports (the square roots of positive smooth functions there). In the sink case $k_1 = e_1^2$, $k_2
= e_2^2$ likewise, with $-\beta_\varrho$, $-\varsigma\mathsf H\phi$ under the roots. Let $j_3 := w_{2\mathbf
o}k_3\,\mathbf g_z^{-1}\in S^{2\mathbf o-\mathbf m}$ (Lemma 2.2 (e)) and $J := \mathrm{Op}_h(j_3\mathrm{Id})$;
$\mathrm{WF}'_h(J)\subset\mathrm{supp}\,k_3\subset\mathrm{Ell}_h(\mathbf P)$, and $J\mathbf P$ has principal symbol
$w_{2\mathbf o}k_3$.

*The absorbing term.* In case (A) it is treated exactly as in Proposition 4.5 (here $c_b = 0$): $-2\lambda\check
A(\epsilon_\flat\varsigma\mathcal A)\check A$ is a term $-F_{\mathrm{abs}}$ with $\langle
F_{\mathrm{abs}}w,w\rangle\ge-C\|w\|^2_{-K\mathbf 1}$, and the double commutator is in $\Psi^{2\mathbf o-\frac12\mathbf
1}$. In case (B), $-\lambda(\check A^2\mathcal A+\mathcal A\check A^2) = -2\lambda\check A\mathcal A\check
A-\lambda[[\mathcal A,\check A],\check A]$, and for every $w$
$$\langle\check A\mathcal A\check Aw,w\rangle_h = \langle\tilde M\,W\check Aw,W\check Aw\rangle_{h^{\oplus
J}}+\langle\mathcal A_0\check Aw,\check Aw\rangle_h\ge0$$
exactly, the integrands being pointwise non-negative, where now $\mathcal A$ stands for $\mathcal A-\mathcal A_1$; so
$F_{\mathrm{abs}} := 2\lambda\check A(\mathcal A-\mathcal A_1)\check A$ satisfies $\langle
F_{\mathrm{abs}}w,w\rangle\ge0$. The terms with $\mathcal A_1$, $\lambda(\check A^2\mathcal A_1+\mathcal A_1\check A^2)$,
are residual: $\mathrm{WF}'_h(\mathcal A_1)$ lies over the support of its coefficients, disjoint from
$\mathrm{WF}'_h(\check A)$, and $\lambda\le2h^{-1}$. As $\check A$ is microsupported at finite frequencies, the order of
$\mathcal A$ in $\zeta$ does not matter, and $\lambda[[\mathcal A,\check A],\check A]\in\Psi^{2\mathbf
k-(2,2,1)+\epsilon'\mathbf 1}\subset\Psi^{2\mathbf o-\frac12\mathbf 1}$ near $\bar U_0$.

*Conclusion.* With $B := \mathrm{Op}_h(b)$, $F := F_{\mathrm{abs}}+\sum_iF_i^{*h}F_i$ and $E := $ the
$\mathrm{Op}_h(w_{\mathbf o}e_i\mathrm{Id})$ (source: $F_i := \mathrm{Op}_h(w_{\mathbf o}f_i\mathrm{Id})$, no $E$; sink:
no $F_i$, $E$ from $e_1,e_2$, with $E^{*h}E$ read as the sum), we get $\varsigma C = -B^{*h}B-F+E^{*h}E+J\mathbf P+R$
with $R\in\Psi^{2\mathbf o-\frac12\mathbf 1}$, since all principal symbols agree. $\check A = ZB+Y$ with $Z :=
\mathrm{Op}_h(w_{\mathbf k-\mathbf o}\tilde\chi Q_0^{-1/2})$, and $B$ is elliptic on $\{\varphi_\delta\ne0\}\supset
K_{\delta/2}$. The sets $\mathrm{supp}\,e_i$ lie in $\{\varrho\ge\delta_1\}\cup\{\phi\ge\delta_2\}$, closed and disjoint
from $\Lambda$. Lemma 3.3 applies, and Lemma 3.4 with $U_j := K_{4^{-j}\delta}^\circ$ (the hypothesis being used only for
these sets, as in Proposition 4.5) gives (5.3) with $U_* := K^\circ_{4^{-J}\delta}$ and $K_E := \bar
U_0\cap\bigcup_j\mathrm{supp}(e_1+e_2)$ at the $j$-th step. Uniformity in $z\in Z'$ holds because every symbol above, and
every lower bound used, is uniform. $\square$

### 5.2 The horizon

**Proposition 5.2 ([Hin26c] Proposition 9.18 at the horizon; cf. I.A Proposition 4.2).** Let
$s>\frac12+\vartheta_{\mathcal H}$, $Z$ compact as in section 4, and $\mathsf r,\mathsf b$ constant near
$\partial\mathcal R_+\cup\partial\mathcal R_-$. For each sign $\pm$ there are neighbourhoods $U_*\subset U_0$ of
$\partial\mathcal R_\pm$, with $U_0$ over $\{|r-r_h|<\delta_0\}$, and a compact $K_E\subset\bar
U_0\setminus\partial\mathcal R_\pm$, such that, uniformly in $z\in Z$, for $B_*$ microsupported in $U_*$ and $G$ elliptic
on $\bar U_0$:
$$\|B_*u\|_{\mathbf o}\le C\big(h^{-1}\|GPu\|_{\mathbf o-\mathbf m+(1,1,0)}+h^N\|Gu\|_{\mathbf o}+\|u\|_{-K\mathbf
1}\big),\qquad\mathbf o = (s,\mathsf r,\mathsf b),\tag{5.4}$$
$$\|B_*v\|_{\mathbf o^*}\le C\big(h^{-1}\|GP^{*h}v\|_{\mathbf o^*-\mathbf m+(1,1,0)}+\|E'v\|_{\mathbf
o^*}+h^N\|Gv\|_{\mathbf o^*}+\|v\|_{-K\mathbf 1}\big),\quad\mathbf o^* = (1-s,\mathsf r^*,\mathsf b^*),\tag{5.5}$$
for any orders $\mathsf r^*,\mathsf b^*$ constant near $\partial\mathcal R_\pm$, with $E'$ elliptic on $K_E$. The fibre
inner product may be chosen near $\partial\mathcal R_\pm$ as in (O3); the adjoint in (5.5) may be taken in any fibre
inner product (I.A Proposition 4.2).

*Proof.* Apply Lemma 5.1 with $c_z = 1$, $F$ fibre infinity, $\Lambda := \partial\mathcal R_\pm$, and $\varsigma :=
\pm\epsilon_\flat$. By (H3) and Lemma 1.1 (e), $\pm\hat q_z>0$ near $\partial\mathcal R_\pm$, uniformly in $z$ (at fibre
infinity $\hat q_z = -\rho_\infty\tau_1$ up to $O(\rho_\infty)$); so (A) holds with $\mathcal A = \mathcal Q$. At fibre
infinity $\mathsf H_z = \rho^{-1}\rho_\infty H_{G_0}$ does not depend on $z$, and $\pm\mathsf H_z$ is $\rho^{-1}$ times
the future field $\mathsf H$ of (H3); so $\beta_\varrho = \epsilon_\flat\beta'_0$ with $\beta'_0 := \rho^{-1}\beta_0>0$
on $\partial\mathcal R_\pm$, hence on a neighbourhood: a source for $P$ and a sink for $P^{*h}$. $\mathsf H_z$ vanishes
on $\partial\mathcal R_\pm$ as a vector field on $\mathcal P$: it is tangent to fibre infinity, vanishes on
$\partial\mathcal R_\pm$ within it (radial points), and $\mathsf H_z\rho_\infty = \beta_\varrho\rho_\infty = 0$ there.

For (iii) take $g := \hat G_0$, and $\phi := q_\pm\circ\pi$, where $q_\pm$ is the quadratic defining function of (H3) and
$\pi$ a smooth retraction of a neighbourhood of $\partial\mathcal R_\pm$ in $\mathcal P$ onto $\partial\Sigma_0$
(projecting along the level sets of a complement of $(\rho_\infty,\hat G_0)$ in a coordinate system, as in I.A Lemma
4.1). Ellipticity: $|\hat G_z|\ge|\mathrm{Re}\,\hat G_z|\ge|\hat G_0|-C\rho_\infty$. For (5.1): at a point $\varpi$,
$\mathsf H_z\phi(\varpi) = dq_\pm(\pi_*\mathsf H_z(\varpi))$ and $\pi_*\mathsf H_z(\varpi) = \mathsf
H_z(\pi\varpi)+O(|\hat G_0(\varpi)|+\rho_\infty(\varpi))$; and $|dq_\pm|\le C\sqrt{q_\pm}$, as $q_\pm\ge0$ is smooth (for
a non-negative $C^2$ function, $|\nabla f|^2\le2f\sup|\nabla^2f|$). With $\pm\mathsf H q_\pm\ge c\,q_\pm$ on
$\partial\Sigma_0$ (H3),
$$\varsigma\mathsf H_z\phi\ \gtrless\ \pm\epsilon_\flat\big(c\,\rho^{-1}\phi-C(|g|+\rho_\infty)\sqrt\phi\big),$$
and $C|g|\sqrt\phi\le\frac c4\rho^{-1}\phi+C'g^2$, $C\rho_\infty\sqrt\phi\le C'\rho_\infty$ on $U_0$; this is (5.1),
source for $\epsilon_\flat = 1$, sink for $\epsilon_\flat = -1$. (iv) holds by assumption. For (v): $\mu^{-1}p_1 =
\rho^{-1}\rho_\infty p_1$ and, at fibre infinity, $\rho_\infty p_1(z) = \rho_\infty\sigma_1(\mathrm{Im}_h\hat P(0))$, the
term $(\mathrm{Re}\,z)\mathrm{Im}_hT$ being of lower order there. With $\varsigma\epsilon_\flat = \pm1$ and $p_{1,\pm} :=
\pm\rho_\infty\sigma_1(\mathrm{Im}_h\hat P(0))$ (I.A (1.5)),
$$\mathcal T = 2\rho^{-1}\big(\tilde\kappa\,\epsilon_\flat\beta_0-p_{1,\pm}\big) =
2\rho^{-1}\beta_0\big(\epsilon_\flat\tilde\kappa-\beta_0^{-1}p_{1,\pm}\big)$$
(both $\beta_0$ and $p_{1,\pm}$ evaluated on $\partial\mathcal R_\pm$; $\beta_0^{-1}p_{1,\pm}$ is $h$-self-adjoint). For
$P$, $\tilde\kappa = s-\frac12$, and $\mathcal T>0$ iff $s-\frac12>\lambda_{\max}(\beta_0^{-1}p_{1,\pm})$, which holds as
$s>\frac12+\vartheta_{\mathcal H}$. For $P^{*h}$ at the order $\mathbf o^*$, $\tilde\kappa = \frac12-s$ and
$\epsilon_\flat = -1$: the same condition. Lemma 5.1 gives (5.4) and (5.5). $\square$

### 5.3 The incoming radial set

**Proposition 5.3 (cf. I.A Proposition 4.6).** Let $z_0\in\{1,-1\}$, $\nu_1>0$ and $Z_{\mathrm{in}} := z_0+i[0,\nu_1]$.
Let $\mathsf r$, $\mathsf b$ be constant near $R_{z_0,\mathrm{in}}$, with $\mathsf r>\frac12(-1+\vartheta_{\mathrm{in}})$
there, the fibre inner product chosen as in (O3). Then there are neighbourhoods $U_*\subset U_0$ of $R_{z_0,\mathrm{in}}$
at finite frequencies and a compact $K_E\subset\bar U_0\setminus R_{z_0,\mathrm{in}}$ such that (5.4) holds for $z\in
Z_{\mathrm{in}}$ with $\mathbf o = (s,\mathsf r,\mathsf b)$, and (5.5) holds with $\mathbf o^* = (s^*,-\mathsf
r-1,\mathsf b^*)$ for any $s^*$ and any $\mathsf b^*$ constant near $R_{z_0,\mathrm{in}}$.

*Proof.* Lemma 5.1 with $c_z = 1$, $F$ the face over $\partial X$, $\Lambda := R_{z_0,\mathrm{in}}$, $\varsigma :=
\epsilon_\flat z_0$. At the face $q_z = -2\xi = 4z_0$ on $\Lambda$, so (A) holds on a neighbourhood. At the face $\mathsf
H_z = \mathsf H_{z_0}$ (Lemma 4.1 (c)) is $\langle\zeta\rangle^{-1}\mathsf V_p$, $p = \xi^2+2z_0\xi+|\eta|^2$, and by
(4.4) of I.A, $\rho^{-1}\mathsf V_p\rho = -\partial_\xi p = 2z_0$ on $\Lambda$, where $\langle\zeta\rangle = \sqrt5$; so
$\beta_\varrho = \varsigma\cdot2z_0/\sqrt5 = 2\epsilon_\flat/\sqrt5$ on $\Lambda$, and $\mathsf H_z$ vanishes on
$\Lambda$ (there $\mathsf V_p = 2z_0\rho\partial_\rho+H^{\mathbb S^3}_p$ and both vanish at $\rho = 0$, $\eta = 0$).
Source for $P$, sink for $P^{*h}$.

For (iii) take $g := \xi^2+2z_0\xi+|\eta|^2$ and $\phi := |\eta|^2$ (round norm), extended to a neighbourhood of
$\Lambda$ in $\mathcal P$ as functions of $(\omega,\xi,\eta)$ in a collar. $\Lambda = \bar U_0\cap\{\rho = 0,\phi = 0,g =
0\}$ for $U_0$ near $\Lambda$ (the other solution of $\phi = g = 0$ is $R_{\mathrm{out}}$). $\mathrm{Re}\,G_z =
g+O(\rho)$ near the face, since $g_{00}\in\rho^2C^\infty$; so $|\hat G_z|\ge c|g|-C\rho$. By (4.4) of I.A, $\mathsf
V_p|\eta|^2 = -2(\partial_\xi p)|\eta|^2 = -4(\xi+z_0)|\eta|^2$, which near $\xi = -2z_0$ is
$4z_0|\eta|^2(1+O(|\xi+2z_0|))$; so $\varsigma\mathsf H_z\phi =
\epsilon_\flat\frac4{\langle\zeta\rangle}|\eta|^2(1+O(|\xi+2z_0|))+O(\rho)$, which gives (5.1) on a small $U_0$, with no
$g^2$ term needed. (iv) by assumption. For (v), at $\Lambda$, by Lemma 4.1 (b), $\mu^{-1}p_1 =
\langle\zeta\rangle^{-1}\rho^{-1}p_1 = \frac1{\sqrt5}\big(\sigma(\rho^{-1}\mathrm{Im}_h\hat
P(0))(-2z_0,0)-z_0(S+S^{*h})\big)$, and the first term is linear in $\zeta$ (I.A Lemma 4.4 (b)), so it equals
$z_0p_{\mathrm{in}}$ with $p_{\mathrm{in}}$ of I.A (1.5). Hence $\varsigma\epsilon_\flat\mu^{-1}p_1 = z_0\mu^{-1}p_1 =
\frac1{\sqrt5}(p_{\mathrm{in}}-(S+S^{*h}))$ for both signs of $z_0$, and
$$\mathcal T = \tfrac2{\sqrt5}\big(2\epsilon_\flat\tilde\kappa\,\mathrm{Id}-(p_{\mathrm{in}}-(S+S^{*h}))\big).$$
For $P$, $\epsilon_\flat\tilde\kappa = \mathsf r+\frac12$; for $P^{*h}$ at the decay order $-\mathsf r-1$,
$\epsilon_\flat\tilde\kappa = -(-\mathsf r-1+\frac12) = \mathsf r+\frac12$. In both cases $\mathcal T>0$ on $\Lambda$ iff
$2\mathsf r+1>\lambda_{\max}(p_{\mathrm{in}}-(S+S^{*h}))$ there, which holds as $\mathsf
r>\frac12(-1+\vartheta_{\mathrm{in}})$. $\square$

### 5.4 The outgoing radial set

Near $R_{\mathrm{out}}$ the absorbing term $\lambda\mathcal Q$ has no sign, as $q_z = -2\xi$ vanishes there. Dividing by
$z$ moves the large imaginary part onto an operator that is non-negative exactly.

**Lemma 5.4 ([Hin26c] (9.49), semiclassically).** Let $V_1 := \rho\partial_\rho$ and $\Omega_{ab} :=
x_a\partial_b-x_b\partial_a$ ($1\le a<b\le4$), and $W := (W_0,W_{ab})$ with $W_0 := h\rho\,V_1$, $W_{ab} :=
h\rho\,\Omega_{ab}$, acting componentwise; $J := 7$. Near $\partial X$, on $\{\rho<\rho_1\}$,
$$h^2\,\mathrm{Re}_h\hat P(0) = W^{*h}\tilde MW+hR^h_1,\qquad\tilde M = \mathrm{Id}+\rho m,\tag{5.6}$$
with $m$ a smooth $h^{\oplus J}$-self-adjoint matrix function, and $R^h_1\in h\rho^2\mathrm{Diff}^1_b$ $h$-self-adjoint,
whose semiclassical symbol divided by $\rho$ vanishes at $R_{\mathrm{out}}$. With $\tilde P := z^{-1}P$ and $\lambda =
\mathrm{Im}\,z/h$,
$$h^{-1}\mathrm{Im}_h\tilde P = \tilde{\mathcal P}_1-\lambda\mathcal A,\qquad\tilde{\mathcal P}_1 :=
\mathrm{Re}(z^{-1})h\,\mathrm{Im}_h\hat P(0)+\mathrm{Im}_hT-\frac{\mathrm{Im}\,z}{|z|^2}R^h_1,\qquad\mathcal A :=
\frac{W^{*h}\tilde MW}{|z|^2}-g_{00}.\tag{5.7}$$
$\tilde{\mathcal P}_1\in\Psi^{(1,-1,0)}$ is $h$-self-adjoint and $\mu^{-1}\sigma(\tilde{\mathcal P}_1) = -(S+S^{*h})$ at
$R_{\mathrm{out}}$; $\mathrm{Re}_h\tilde P$ has principal symbol $\tilde p_z := \mathrm{Re}(z^{-1}G_z) =
\mathrm{Re}(z^{-1})G_0+\tau_1+(\mathrm{Re}\,z)g_{00}$.

*Proof.* By (H2), $P^{(0)}-((\rho D_\rho)^2+\Delta_{\mathbb
S^3})\mathrm{Id}\in\mathrm{Diff}^1_b+\rho\,\mathrm{Diff}^2_b$, and $\Delta_{\mathbb S^3} =
\sum_{a<b}\Omega_{ab}^*\Omega_{ab}$, the rotations being divergence free for $dx$. Since $(\rho V_1)^* = -\rho
V_1+\rho\,C^\infty$ and $[\rho,V_1]\in\rho\,C^\infty$, $h^2\rho^2(\rho D_\rho)^2 = W_0^*W_0+h^2\rho^2\mathrm{Diff}^1_b$
and $h^2\rho^2\Omega_{ab}^*\Omega_{ab} = W_{ab}^*W_{ab}+h^2\rho^2\mathrm{Diff}^1_b$. An element of
$h^2\rho^3\mathrm{Diff}^2_b$ is $\sum W_j^*\rho m'_{jk}W_k$ modulo $h^2\rho^3\mathrm{Diff}^1_b$, the second order part
being spanned by products of the $V$'s. $W_j^{*h}-W_j^*$ is a matrix function times $h\rho$. Take $h$-self-adjoint parts:
the left side of (5.6) is $h$-self-adjoint, so replacing $m'$ by its $h^{\oplus J}$-self-adjoint part $m$ changes only
the remainder, which lies in $h^2\rho^2\mathrm{Diff}^1_b = h\cdot h\rho^2\mathrm{Diff}^1_b$. Its symbol:
$h\rho^2\mathrm{Diff}^1_b = \rho\cdot h\rho\,\mathrm{Diff}^1_b$, and $h\rho\,\mathrm{Diff}^1_b$ consists of $c\cdot h\rho
V+h\rho d$, with semiclassical symbol linear in $\zeta$ plus $O(\rho)$; so the symbol divided by $\rho$ vanishes at
$\zeta = 0$, $\rho = 0$. For (5.7): $\tilde P = z^{-1}h^2\hat P(0)+hT+zg_{00}$ by (1.2), and $\mathrm{Im}_h(cA) =
(\mathrm{Re}\,c)\mathrm{Im}_hA+(\mathrm{Im}\,c)\mathrm{Re}_hA$ with $\mathrm{Im}(z^{-1}) = -\mathrm{Im}\,z/|z|^2$. The
symbol of $\tilde{\mathcal P}_1$ at the face is $\rho$ times $\mathrm{Re}(z^{-1})r_3-(S+S^{*h})$ plus a term vanishing at
$R_{\mathrm{out}}$, $r_3 := \sigma(\rho^{-1}\mathrm{Im}_h\hat P(0))$ being linear (I.A Lemma 4.4 (b)); and $\mu = \rho$
at $\zeta = 0$. $\square$

**Proposition 5.5 ([Hin26c] Proposition 9.27; cf. I.A Proposition 4.9).** Let $Z$ be compact as in section 4, $\mathsf r$
and $\mathsf b$ constant near $R_{\mathrm{out}}$, and $h$ a fibre inner product with $\mathsf
r<-\frac12+\frac12\inf_{\partial X}\lambda_{\min}(S+S^{*h})$. Then there are neighbourhoods $U_*\subset U_0$ of
$R_{\mathrm{out}}$ at finite frequencies over $\{\rho<\rho_1\}$ and a compact $K_E\subset\bar U_0\setminus
R_{\mathrm{out}}$ such that, uniformly in $z\in Z$,
$$\|B_*u\|_{\mathbf o}\le C\big(h^{-1}\|GPu\|_{\mathbf o-\mathbf m+(1,1,0)}+\|E'u\|_{\mathbf o}+h^N\|Gu\|_{\mathbf
o}+\|u\|_{-K\mathbf 1}\big),\qquad\mathbf o = (s,\mathsf r,\mathsf b),\tag{5.8}$$
and (5.4) holds for $P^{*h}$ at $\mathbf o^* = (s^*,-\mathsf r-1,\mathsf b^*)$ for every $s^*$ and every $\mathsf b^*$
constant near $R_{\mathrm{out}}$, with $B_*,G,E'$ as in Lemma 5.1. By (O3) and I.A section 2.4, $h$ may be chosen so that
the condition reads $\mathsf r<-\frac12+\bar S$ up to any given margin.

*Proof.* Lemma 5.1 with $c_z = z^{-1}$, $F$ the face over $\partial X$, $\Lambda := R_{\mathrm{out}}$, $\varsigma :=
\epsilon_\flat$, case (B): by Lemma 5.4, $h^{-1}\mathrm{Im}_h\mathbf P = \epsilon_\flat(\tilde{\mathcal
P}_1-\lambda\mathcal A)$. Write $\tilde M = \tilde M_{\mathrm{ext}}+(1-\chi_1)(\tilde M-\mathrm{Id})$ with $\tilde
M_{\mathrm{ext}} := \chi_1\tilde M+(1-\chi_1)\mathrm{Id}$, where $\chi_1\in C^\infty(\bar X)$ is supported in
$\{\rho<\rho_2\}$ and equal to 1 near the base projection of $\bar U_0$, and $\rho_2$ is so small that $\tilde
M\ge\frac12\mathrm{Id}$ on $\{\rho<\rho_2\}$; then $\tilde M_{\mathrm{ext}}\ge\frac12\mathrm{Id}$ everywhere, and
$\mathcal A_1 := |z|^{-2}W^{*h}(1-\chi_1)(\tilde M-\mathrm{Id})W$ (with $\tilde M$ extended arbitrarily off
$\{\rho<\rho_1\}$, and the identity (5.7) used only near the base projection of $\bar U_0$). $\mathcal A_0 :=
-g_{00}\ge0$ by (H6). So (ii)(B) holds. By (4.4) of I.A, at the face $\mathsf H^{\mathbf P}_z =
\langle\zeta\rangle^{-1}\mathsf V_{\tilde g}$ with $\tilde g := 2\xi+\kappa(\xi^2+|\eta|^2)$, $\kappa :=
\mathrm{Re}(z^{-1})$, and (I.A (4.11)) $\rho^{-1}\mathsf V_{\tilde g}\rho = -2(1+\kappa\xi)$, $\mathsf V_{\tilde
g}(\xi^2+|\eta|^2) = -4|\eta|^2$, $\mathsf V_{\tilde g}\tilde g = 0$; $\mathsf V_{\tilde g}$ vanishes at
$R_{\mathrm{out}}$ as a vector field on $\mathcal P$. So $\beta_\varrho = -2\epsilon_\flat$ at $R_{\mathrm{out}}$, and
$\le-\epsilon_\flat$ near it: a sink for $P$, a source for $P^{*h}$.

For (iii), $g := \tilde g$ and $\phi := \xi^2+|\eta|^2$, extended in a collar.
$|\rho_\infty^2z^{-1}G_z|\ge|\mathrm{Re}(z^{-1}\hat G_z)|\ge|\tilde g|-C\rho$. On $\{\phi\le\kappa^{-2}\}$, $2\xi =
g-\kappa\phi$ gives $\xi^2\le\frac12(g^2+\kappa^2\phi^2)\le\frac12g^2+\frac12\phi$, hence
$|\eta|^2\ge\frac12\phi-\frac12g^2$ and $\varsigma\mathsf H^{\mathbf P}_z\phi =
-4\epsilon_\flat\langle\zeta\rangle^{-1}|\eta|^2+O(\rho)$, which is (5.1) with the sink sign for $P$ and the source sign
for $P^{*h}$. (iv) by assumption. For (v), by Lemma 5.4, $\varsigma\epsilon_\flat\mu^{-1}p^{\mathbf P}_1 = -(S+S^{*h})$
at $R_{\mathrm{out}}$, so
$$\mathcal T = -4\epsilon_\flat\tilde\kappa\,\mathrm{Id}+2(S+S^{*h}).$$
For $P$, $\tilde\kappa = \mathsf r+\frac12$, and $\mathcal T>0$ iff $2\mathsf r+1<\lambda_{\min}(S+S^{*h})$. For $P^{*h}$
at the decay order $-\mathsf r-1$, $-\epsilon_\flat\tilde\kappa = -\mathsf r-\frac12$, the same condition. $\square$

### 5.5 b-regularity at the outgoing radial set

Write $\mathcal V := (V_1,\Omega_{12},\dots,\Omega_{34})$, $V^\alpha$ for ordered products, $\alpha_1$ the number of
factors $V_1$, $A_k := \{|\alpha| = k\}$, and for $\alpha\in A_k$ with $\alpha_1\ge1$, $\alpha' := \alpha$ with one
factor $V_1$ removed. Let
$$\|u\|_{\mathbf o;k} := \sum_{|\alpha|\le k}\|(hV)^\alpha u\|_{\mathbf o}.\tag{5.9}$$
Then $\|u\|_{(s;k),\mathsf r,\mathsf b;+}$ of (1.5) and $h^{-k}\|u\|_{\mathbf o;k}$ are equivalent uniformly in $h$: by
$V^\alpha = h^{-|\alpha|}(hV)^\alpha$, (1.5) is $\sum_{j+|\alpha|\le k}h^{-j-|\alpha|}\|(hV)^\alpha u\|_{\mathbf o}$,
each term is at most $h^{-k}\|(hV)^\alpha u\|_{\mathbf o}$, and the terms with $j = k-|\alpha|$ are exactly
$h^{-k}\|(hV)^\alpha u\|_{\mathbf o}$. Here the $V$'s replace the $\langle x\rangle D_{x_j}$ of (1.5); on $\bar X$, where
$r>0$, both families span the b-vector fields over $C^\infty(\bar X)$, so the norms are equivalent.

**Lemma 5.6 (I.A Lemma 4.8, semiclassically).** On $\{\rho<\rho_1\}$, for Schwartz $u$ and $k\ge1$, $u^{(k)} :=
((hV)^\alpha u)_{\alpha\in A_k}$ satisfies
$$P\,u^{(k)}_\alpha+\sum_{\beta\in A_k}h\rho\,\mathcal K_{\alpha\beta}u^{(k)}_\beta = (hV)^\alpha
Pu-\alpha_1h\,(hV)^{\alpha'}Pu+\sum_{|\beta|\le k-1}h^{k-|\beta|}R^h_{\alpha\beta}(hV)^\beta u,\tag{5.10}$$
with $\mathcal K_{\alpha\beta}\in\Psi^{(1,0,0)}$ semiclassical differential operators whose symbols vanish at
$R_{\mathrm{out}}$, and $R^h_{\alpha\beta}\in\Psi^{(1,-1,0)}$; all depend polynomially on $z$.

*Proof.* Multiply (4.10) of I.A, with $\sigma = z/h$ and $f = \hat P(\sigma)u$, by $h^{2+k}$: $h^{2+k}V^\alpha =
h^2(hV)^\alpha$, $h^2\hat P(\sigma) = P$, and $h^{2+k}V^{\alpha'} = h\cdot h^2(hV)^{\alpha'}$. It remains to place
$h^2\tilde P_{\alpha\beta}$ and $h^{2+k}R_{\alpha\beta}V^\beta = h^{k-|\beta|}h^2R_{\alpha\beta}(hV)^\beta$, which needs
the dependence on $\sigma$ that the proof of I.A Lemma 4.8 produces. There $\hat P(\sigma) = 2i\sigma\rho V_1+\mathcal
R$, $\mathcal R = -2i\sigma\rho(\frac32+S)+\hat P(0)-i\sigma Q+\sigma^2g_{00}$, and the terms are sorted by origin. From
$\hat P(0) = \rho^2P^{(0)}$: $\sigma$-independent, in $\rho^2\mathrm{Diff}^1_b\circ V^\beta$; times $h^2$ this is
$h\rho\cdot(h\rho\,\mathrm{Diff}^1_b)$, and $h\rho\,\mathrm{Diff}^1_b$ has semiclassical symbol linear in $\zeta$ plus
$O(\rho)$. From $\sigma\rho(\frac32+S)$ and from the commutators of $2i\sigma\rho V_1$ beyond the diagonal term:
$\sigma\rho\,C^\infty$ times $V^\beta$ with $|\beta|\le k-1$ only; times $h^2$, $hz\rho\,C^\infty\in\Psi^{(0,-1,-1)}$.
From $\sigma Q$, $Q\in\rho^3\mathrm{Diff}^1_b$: $[V^\alpha,Q]$ and $QV^{\alpha'}$ lie in $\rho^3\mathrm{Diff}^k_b$, whose
part with $|\beta| = k$ has coefficients in $\rho^3C^\infty$; so $\sigma\rho^3C^\infty$ on the diagonal level and
$\sigma\rho^3\mathrm{Diff}^1_b$ below it; times $h^2$, $hz\rho^3C^\infty = h\rho\cdot z\rho^2C^\infty$ and $z\rho^2\cdot
h\rho\,\mathrm{Diff}^1_b\subset\Psi^{(1,-2,0)}$. From $\sigma^2g_{00}$, $g_{00}\in\rho^2C^\infty$: only below the
diagonal level, $\sigma^2\rho^2C^\infty$; times $h^2$, $z^2\rho^2C^\infty$. Collecting: $h^2\tilde P_{\alpha\beta} =
h\rho\mathcal K_{\alpha\beta}$ with $\mathcal K_{\alpha\beta}$ having symbol linear in $\zeta$ plus $O(\rho)$ at the
face, so vanishing at $R_{\mathrm{out}}$; and $h^2R_{\alpha\beta}\in\Psi^{(1,-1,0)}$. $\square$

**Proposition 5.7 ([Hin26c] (9.77)).** In the setting of Proposition 5.5, for $k\in\mathbb N_0$ there are $B_*$ elliptic
at $R_{\mathrm{out}}$, $G$ and a compact $K_E\subset\bar U_0\setminus R_{\mathrm{out}}$ such that for $E'$ elliptic on
$K_E$, uniformly in $z\in Z$,
$$\|B_*u\|_{\mathbf o;k}\le C\big(h^{-1}\|GPu\|_{\mathbf o-\mathbf m+(1,1,0);k}+\|E'u\|_{\mathbf
o+k(1,1,0)}+h^N\|Gu\|_{\mathbf o;k}+\|u\|_{-K\mathbf 1}\big).\tag{5.11}$$

*Proof.* Induction on $k$; $k = 0$ is (5.8). Let $k\ge1$. The system (5.10) is $\mathbf P^{(k)}u^{(k)} = f^{(k)}$ with
$\mathbf P^{(k)} := P\otimes\mathrm{Id}+h\rho\mathcal K$ on $\mathbb C^N\otimes\mathbb C^{A_k}$, inner product $h^{\oplus
A_k}$. Apply Lemma 5.1 to $\mathbf P := z^{-1}\mathbf P^{(k)}$ exactly as in Proposition 5.5. The added term changes
nothing that the lemma uses: $\mathrm{Re}_h(z^{-1}h\rho\mathcal K)\in\Psi^{(1,-1,-1)}$ is of lower order (its commutator
with $\check A^2$, divided by $h$, lies in $\Psi^{2\mathbf o-\mathbf 1+\epsilon'\mathbf 1}$, $\check A$ being scalar),
and $h^{-1}\mathrm{Im}_h(z^{-1}h\rho\mathcal K) = \mathrm{Im}_h(z^{-1}\rho\mathcal K)\in\Psi^{(1,-1,0)}$ is added to
$\tilde{\mathcal P}_1\otimes\mathrm{Id}$, with $\mu^{-1}$ times its symbol vanishing at $R_{\mathrm{out}}$. So the
threshold matrix is $\mathcal T\otimes\mathrm{Id}$, the same. This gives (5.8) for $u^{(k)}$, with $G\mathbf
P^{(k)}u^{(k)} = Gf^{(k)}$. Now $\|G(hV)^\alpha Pu\|_{\mathbf t}+\|G\,h(hV)^{\alpha'}Pu\|_{\mathbf t}\le C\|\tilde
GPu\|_{\mathbf t;k}+C\|u\|_{-K\mathbf 1}$, $\mathbf t := \mathbf o-\mathbf m+(1,1,0)$, with $\tilde G$ elliptic on
$\mathrm{WF}'_h(G)$; and, $G$ being microsupported at finite frequencies, $\|Gh^{k-|\beta|}R^h_{\alpha\beta}(hV)^\beta
u\|_{\mathbf t}\le Ch\|\tilde G(hV)^\beta u\|_{\mathbf o}+C\|u\|_{-K\mathbf 1}$, so $h^{-1}$ times it is bounded by
$\|\tilde Gu\|_{\mathbf o;k-1}$, which the induction hypothesis (applied with $\tilde G$ in place of $B_*$, after
shrinking) bounds. The term $\|E'u^{(k)}\|_{\mathbf o}$ is at most $C\|E''u\|_{\mathbf o+k(1,1,0)}+C\|u\|_{-K\mathbf 1}$,
since $(hV)^\alpha\in\Psi^{k(1,1,0)}$ (Proposition 2.8). Finally $\|B'_*u\|_{\mathbf o;k}\le C(\|B_*u^{(k)}\|_{\mathbf
o}+\|\tilde Gu\|_{\mathbf o;k-1}+\|u\|_{-K\mathbf 1})$ for $B'_*$ microsupported where $B_*$ is elliptic, since
$[B'_*,(hV)^\alpha]$ is a sum of terms $(hV)^\gamma[B'_*,hV](hV)^{\gamma'}$, $|\gamma|+|\gamma'| = k-1$, with
$[B'_*,hV]\in\Psi^{(0,0,-1)}$ by Theorem 2.4. $\square$

## 6. The trapped set

This section is [Hin26c] section 9.3.4 on $E$. Fix $z_0\in\{1,-1\}$ and $\Gamma = \Gamma_{z_0}$ of (H7). Near $\Gamma$
everything happens at finite frequencies over a compact set $K_\Gamma\subset\{r_2<r<\rho_1^{-1}\}$, where $\langle
x\rangle$ and $\langle\zeta\rangle$ are bounded above and below and an admissible $\mathsf b$ is constant (section 1.4).
So for operators microsupported there, every norm $\|\cdot\|_{\mathbf o}$ is $h^{-\mathsf b}$ times a norm equivalent to
that of $L^2$, and we state the estimates of this section in $L^2$ (that is, with $\mathbf o = 0$). $\chi_\Gamma\in
C_c^\infty$ equals 1 near $K_\Gamma$, and $\|u\|_{-N} := \|\chi_\Gamma u\|_{H^{-N}_h}$. Choosing an
$h_\Gamma$-orthonormal frame near $K_\Gamma$ we take $h_\Gamma$ to be the standard inner product there; adjoints are then
ordinary adjoints, and the adjoint in another fibre inner product is conjugate to this one by a matrix function (I.A
Proposition 4.2), which does not affect microlocal estimates.

### 6.1 Set-up

Let $\mathbf P\in\{P,P^*\}$, $\epsilon_\flat := \pm1$ accordingly, and $\varsigma := \epsilon_\flat z_0$. We take
$\mathrm{Re}\,z = z_0$ and $0\le\mathrm{Im}\,z\le\nu'$, $\nu'$ small: for $\mathrm{Im}\,z\ge\nu'$, $\mathbf P$ is
elliptic near $\Gamma$ by Lemma 1.1 (d), and Proposition 4.2 gives every estimate below with $h^{-1}$ replaced by $1$.
Write $H := H_{G_{z_0}}$, $\lambda := \mathrm{Im}\,z/h\ge0$, and, on a neighbourhood of $\Gamma$,
$$p^\natural := z_0\,p_1(z_0),\qquad q^\natural := z_0\,q_{z_0},\qquad V := \varsigma H.\tag{6.1}$$
$q^\natural\ge2\beta_0$ on $\Gamma$ by (H7) and Lemma 1.1 (e), $p^\natural$ is the endomorphism $p^\Gamma_1$ of (1.4) on
$\Gamma$, and both depend on $\mathrm{Re}\,z = z_0$ only (Lemma 1.1 (b)). For a real scalar $a\in C_c^\infty$ near
$\Gamma$ and $A = A^*$ quantising $a\mathrm{Id}$, the operator $C$ of (3.1) for $\mathbf P$ satisfies, by (4.3),
$$\sigma(\varsigma C) = \varsigma H_{\mathrm{Re}\,G_z}a+2a\big(p^\natural-\lambda q^\natural\big),\qquad\varsigma
H_{\mathrm{Re}\,G_z}a = Va+O((\mathrm{Im}\,z)^2)\tag{6.2}$$
(Lemma 4.1: $H_{\mathrm{Re}\,G_z}-H = -(\mathrm{Im}\,z)^2H_{g_{00}}$). $V$ is the field along which estimates for
$\mathbf P$ propagate (Proposition 4.5): the future field $z_0H$ for $P$, the past field for $P^*$. Accordingly put
$(\phi^\natural_u,\phi^\natural_s,\nu^\natural_u,\nu^\natural_s) := (\phi_u,\phi_s,\nu_u,\nu_s)$ if $\epsilon_\flat = 1$
and $(\phi_s,\phi_u,\nu_s,\nu_u)$ if $\epsilon_\flat = -1$, and $\Gamma^\natural_{u/s} := \{\phi^\natural_{u/s} =
0\}\cap\Sigma_{z_0}\cap O$. Then by (Γ.2), on $\Sigma_{z_0}\cap O$,
$$V\phi^\natural_u = -\nu^\natural_u\phi^\natural_u,\qquad V\phi^\natural_s =
\nu^\natural_s\phi^\natural_s,\qquad\{\phi^\natural_u,\phi^\natural_s\}\ne0\ \text{on}\ \Gamma,\tag{6.3}$$
with $\min(\inf_\Gamma\nu^\natural_u,\inf_\Gamma\nu^\natural_s) = \nu_{\min}$. Extend $\phi_{u/s}$ and $\nu_{u/s}$
smoothly to $O$. As $dG_{z_0}\ne0$ near $\Gamma$ (Γ.3), the differences in (6.3) are smooth multiples of $G_{z_0}$ off
$\Sigma_{z_0}$: $V\phi^\natural_u = -\nu^\natural_u\phi^\natural_u+j^\natural_uG_{z_0}$, $V\phi^\natural_s =
\nu^\natural_s\phi^\natural_s+j^\natural_sG_{z_0}$ on $O$. For $\delta\le\delta_0$ let
$$\Gamma(\delta) := \{|\phi_u|\le\delta,\ |\phi_s|\le\delta,\ |G_{z_0}|\le\delta\}\cap\bar O',$$
$O'\Subset O$ a neighbourhood of $\Gamma$; by (Γ.1), $\Gamma = \bigcap_\delta\Gamma(\delta)$, so the $\Gamma(\delta)$ are
compact neighbourhoods of $\Gamma$ shrinking to it, and $\delta_0$ is taken so small that $\Gamma(\delta_0)\subset O'$
and (6.3) and (Γ.3) hold, with $|\{\phi^\natural_u,\phi^\natural_s\}|\ge c_\Gamma>0$, on $\Gamma(\delta_0)$.

*Dynamics in $\Gamma(\delta_0)$.* Let $\gamma$ be an integral curve of $V$ in $\Sigma_{z_0}\cap\Gamma(\delta_0)$. Along
it $\phi^\natural_u(\gamma(t)) = \phi^\natural_u(\gamma(0))\exp(-\int_0^t\nu^\natural_u)$ and $\phi^\natural_s(\gamma(t))
= \phi^\natural_s(\gamma(0))\exp\int_0^t\nu^\natural_s$, with $\nu^\natural_{u/s}\ge\frac12\nu_{\min}$ on
$\Gamma(\delta_0)$ after shrinking $\delta_0$. So: (D1) if $\gamma(0)\notin\Gamma^\natural_u$, then $\gamma$ leaves
$\Gamma(\delta_0)$ in finite backward time; (D2) if $\gamma(0)\in\Gamma^\natural_u$, then as long as it stays in
$\Gamma(\delta_0)$ backward in time it stays in $\Gamma^\natural_u$, $|\phi^\natural_s|$ decreases exponentially, and
$\gamma(t)\to\Gamma$ as $t\to-\infty$ (the $\omega$-limit points lie in $\Gamma^\natural_u\cap\Gamma^\natural_s =
\Gamma$); (D3) if $\gamma(0)\in\Gamma^\natural_u\setminus\Gamma$, then $\gamma$ leaves $\Gamma(\delta_0)$ in finite
forward time. Combined with (H8): every backward $V$-curve from a point of $\Sigma_{z_0}$ near $\Gamma$ not on
$\Gamma^\natural_u$ leaves $\Gamma(\delta_0)$ and is then a curve of (H8), which tends to the radial sets.

### 6.2 The lossless estimate

**Proposition 6.1 ([Hin26c] (9.83)).** Let $\mathbf P' := \mathbf P+h\mathbf X$ with $\mathbf X\in\Psi^0$ microsupported
near $\Gamma$, and let $p'^\natural := p^\natural+\varsigma\,\sigma(\mathrm{Im}\,\mathbf X)$ (so that $\varsigma
h^{-1}\mathrm{Im}\,\mathbf P'$ has symbol $p'^\natural-\lambda q^\natural$). Let $\gamma\in\mathbb R$ with
$\sup_{\varpi\in\Gamma}\lambda_{\max}\big(p'^\natural(\varpi)-\gamma q^\natural(\varpi)\big)<0$. There are $\nu'>0$ and,
for every neighbourhood $U$ of $\Gamma$, operators $B,E,G\in\Psi^0$ microsupported in $U$, $B$ elliptic at $\Gamma$,
$\mathrm{WF}'_h(E)\cap\Gamma^\natural_u = \emptyset$, such that for $z\in z_0+i[h\gamma,\nu']$ with
$\mathrm{Im}\,z\ge-\nu'$, $h<h_0$ and all $N$,
$$\|Bu\|\le C\big(h^{-1}\|G\mathbf P'u\|+\|Eu\|+h^N\|u\|_{-N}\big).\tag{6.4}$$
For $\mathbf X = 0$ the condition is $\gamma>\gamma_+$, with $\gamma_+$ of (1.4).

*Proof.* With $\chi_0$ as in the proof of Lemma 5.1, let $\psi_u := \chi_0(M(\phi^\natural_u)^2)$, $\psi_s :=
\chi_0(M(\phi^\natural_s)^2)$, $\psi_\Sigma := \chi_0(M_\Sigma G_{z_0}^2)$ and $\check a := \psi_u\psi_s\psi_\Sigma$,
with $M_\Sigma\ge M\ge M_0$ large; $\mathrm{supp}\,\check a\subset\Gamma(\sqrt{2/M})$ (for $M_\Sigma\ge M$). Compute
(6.2) with $a = \check a^2$. First, with $\chi_0\chi_0'\le0$,
$$V\psi_u^2 = 4M\chi_0\chi_0'(M(\phi^\natural_u)^2)\,\phi^\natural_u\big(-\nu^\natural_u\phi^\natural_u+j^
\natural_uG_{z_0}\big),\qquad V\psi_s^2 =
4M\chi_0\chi_0'(M(\phi^\natural_s)^2)\,\phi^\natural_s\big(\nu^\natural_s\phi^\natural_s+j^\natural_sG_{z_0}\big).$$
On $\mathrm{supp}\,\chi_0'(M(\phi^\natural_u)^2)\cap\mathrm{supp}\,\psi_\Sigma$ we have $(\phi^\natural_u)^2\ge M^{-1}$
and $G_{z_0}^2\le2M_\Sigma^{-1}$, so $|j^\natural_uG_{z_0}|\le\frac14\nu_{\min}|\phi^\natural_u|$ once $M_\Sigma\ge C M$;
then $V\psi_u^2 = e_u^2\ge0$ with $e_u :=
2M^{1/2}\theta_u\,|\phi^\natural_u|(\nu^\natural_u-j^\natural_uG_{z_0}/\phi^\natural_u)^{1/2}$, $\theta_u :=
\sqrt{-\chi_0\chi_0'}(M(\phi^\natural_u)^2)$, smooth, and likewise $V\psi_s^2 = -f_s^2$. The $O((\mathrm{Im}\,z)^2)$ term
of (6.2) changes these by at most $C(\mathrm{Im}\,z)^2M|\phi|\cdot|\chi_0\chi_0'|$, which keeps the signs and smoothness
for $\mathrm{Im}\,z\le\nu'$, $\nu'$ small depending on $M$. The derivative of $\psi_\Sigma$ is supported where
$G_{z_0}^2\ge M_\Sigma^{-1}$, where $G_z$ is elliptic for $\nu'$ small; it gives a term $J\mathbf P'$ as in Lemma 5.1.
Next, on $\mathrm{supp}\,\check a$,
$$p'^\natural-\lambda q^\natural = (p'^\natural-\gamma q^\natural)-(\lambda-\gamma)q^\natural,$$
and $p'^\natural-\gamma q^\natural\le-c\,\mathrm{Id}$ there for $M$ large, by the hypothesis and continuity. So, with $b
:= \check a(-2(p'^\natural-\gamma q^\natural))^{1/2}$ (the positive square root of a positive definite smooth matrix
function, smooth),
$$\varsigma C = -B^*B-F_s^*F_s+E_u^*E_u+J\mathbf P'-2(\lambda-\gamma)\check A\,\varsigma\epsilon_\flat\mathcal Q\,\check
A+R,\qquad R\in h^{\frac12}\Psi^0,$$
where $\varsigma\epsilon_\flat\mathcal Q = z_0\mathcal Q$ has principal symbol $q^\natural\ge\beta_0$ on
$\mathrm{supp}\,\check a$; since $0\le\lambda-\gamma\le3h^{-1}$, the paragraph *Positivity of absorbing terms* of section
3.3 makes $2(\lambda-\gamma)\check Az_0\mathcal Q\check A$ a term $F$ of Lemma 3.3, with the double commutator in $R$.
Lemma 3.3 and Lemma 3.4, with $\Lambda := \Gamma$ and the sets $\Gamma(\sqrt{2/M})$ for an increasing sequence of $M$
(and $M_\Sigma := CM$), give (6.4) with $E$ elliptic on the union of the sets $\mathrm{supp}\,e_u$, which lie in
$\{(\phi^\natural_u)^2\ge M_0^{-1}\cdot\frac12\}$ and so avoid $\Gamma^\natural_u$. $\square$

### 6.3 Defect measures with values in matrices

In this section and the next, $h_j\to0$ is a sequence, $u_j$ are $\mathbb C^N$-valued, and we drop $j$. $U$ is an open
precompact set at finite frequencies over the interior of $K_\Gamma$. The family is *tempered on $U$* if $\|u\|_{-N_0}\le
Ch^{-N_0}$ for some $N_0$ and $\sup\|Gu\|<\infty$ for some $G\in\Psi^0$ elliptic on $\bar U$.

**Lemma 6.2 ([Hin26c] Lemma 9.30 on $E$).** If $(u_j)$ is tempered on $U$, a subsequence has a *defect measure* on $U$: a
positive semidefinite $\mathrm{End}(\mathbb C^N)$-valued Radon measure $\mu$ on $U$, such that $\langle
Bu,u\rangle\to\int_U\mathrm{tr}(b\,d\mu)$ for every $B\in\Psi^0$ with $\mathrm{WF}'_h(B)$ a compact subset of $U$ and
principal symbol $b\in C_c^\infty(U;\mathrm{End}\,\mathbb C^N)$. Write $\nu := \mathrm{tr}\,\mu\ge0$; then $d\mu =
M\,d\nu$ with $M\ge0$, $\mathrm{tr}\,M = 1$, $\nu$-a.e., and for every Hermitian continuous $p$,
$\mathrm{tr}(p\,d\mu)\le\lambda_{\max}(p)\,d\nu$.

*Proof.* (a) For $B$ as stated, $|\langle Bu,u\rangle|\le C_b+o(1)$ with $C_b := 2\sup|b\,g^{-1}|\cdot\sup\|Gu\|^2$: as
in [Hin26c] (9.87), $B = QG+R$ with $Q$ of principal symbol $bg^{-1}$ (Proposition 2.10's construction) and $R\in
h^\infty\Psi^{-\infty}$ near $\mathrm{WF}'_h(B)$, and $\|Q^*w\|\le(2\sup|q|)\|w\|+Ch^{\frac12}\|w\|_{-N}$ for $w$
microlocalised near $U$, by the square root construction: $4\sup|q|^2\mathrm{Id}-q^*q = s^*s$ with $s$ smooth (a positive
definite square root, as $4\sup|q|^2-q^*q\ge3\sup|q|^2$), so $4\sup|q|^2-QQ^*$ is a square plus $h\Psi^0$. (b) The value
depends only on $b$: two such $B$ with the same $b$ differ by $h\Psi^0$ plus residual terms, whose pairings tend to 0 by
(a). (c) A diagonal argument over a countable dense subset of $C_c^\infty(U;\mathrm{End}\,\mathbb C^N)$ (dense in $C_c$
in the supremum norm on each compact set) gives a subsequence along which $L(b) := \lim\langle\mathrm{Op}_h(b)u,u\rangle$
exists for all $b$ in that set, and by (a) $L$ extends to a linear functional on $C_c(U;\mathrm{End}\,\mathbb C^N)$,
continuous for the supremum norm on each compact set. By the Riesz representation theorem applied to each matrix entry,
$L(b) = \int\mathrm{tr}(b\,d\mu)$ for a matrix of complex Radon measures. (d) Positivity: let $b\ge0$ with
$\mathrm{supp}\,b\subset K\Subset U$, and $j\in C_c^\infty(U)$ scalar equal to 1 on $K$. For $\epsilon>0$, $b+\epsilon
j^2\mathrm{Id}$ is positive definite on $K$ and equal to $\epsilon j^2\mathrm{Id}$ off $K$, so it is
$q_\epsilon^*q_\epsilon$ with $q_\epsilon\in C_c^\infty(U)$ (on $K$ the positive square root; off $K$, $\sqrt\epsilon
j$); then $\mathrm{Op}_h(b)+\epsilon\mathrm{Op}_h(j)^*\mathrm{Op}_h(j) =
\mathrm{Op}_h(q_\epsilon)^*\mathrm{Op}_h(q_\epsilon)+hR'$, so
$\liminf\langle\mathrm{Op}_h(b)u,u\rangle\ge-\epsilon\limsup\|\mathrm{Op}_h(j)u\|^2\ge-C\epsilon$. Hence $L(b)\ge0$ for
$b\ge0$; taking $b = \phi\,vv^*$ with $\phi\ge0$ scalar and $v\in\mathbb C^N$ shows $v^*\mu v\ge0$, so $\mu$ is Hermitian
and positive semidefinite. Each entry is then absolutely continuous with respect to $\nu$ ($|\mu_{ab}|\le\nu$ for a
positive matrix measure), which gives $M$; and $\mathrm{tr}(pM)\le\lambda_{\max}(p)\mathrm{tr}\,M$ for $M\ge0$. $\square$

**Lemma 6.3 ([Hin26c] Lemmas 9.31-9.32 on $E$).** Let $(u_j)$ be tempered on $U$ with defect measure $\mu$, and $\mathbf
P_j := \mathbf P_{h_j,z_j}$ with $\mathrm{Im}\,z_j/h_j\to\eta\in[0,\infty)$.
(a) If $\|G\mathbf P_ju_j\| = o(1)$ with $G$ elliptic on $\bar U$, then $\mathrm{supp}\,\mu\subset\Sigma_{z_0}$.
(b) For real scalar $a\in C_c^\infty(U)$, and $Y\in\Psi^0$ microsupported in $U$ with
$\mathrm{WF}'_h(I-Y)\cap\mathrm{supp}\,a = \emptyset$,
$$\Big|\int_U\big(Va\,d\nu+2a\,\mathrm{tr}\big((p^\natural-\eta q^\natural)\,d\mu\big)\big)\Big|\le4\sup|a|\,\limsup
h^{-1}\|Y\mathbf Pu\|\,\|Yu\|.\tag{6.5}$$
(c) The same holds with $\mathbf P$ replaced by a self-adjoint $\Phi\in\Psi^0$ with real scalar principal symbol $\phi$,
with $Va$ replaced by $H_\phi a$ and with $p^\natural-\eta q^\natural$ replaced by 0.

*Proof.* (a) For $b\in C_c^\infty(U)$ with $\mathrm{supp}\,b\cap\Sigma_{z_0} = \emptyset$, $\mathbf P_j$ is elliptic on
$\mathrm{supp}\,b$ for $j$ large, so $\mathrm{Op}_h(b) = Q\mathbf P_j+R$ with $Q$ bounded and $R\in
h^\infty\Psi^{-\infty}$ near $\mathrm{supp}\,b$, and $\int|b|^2d\nu = \lim\|\mathrm{Op}_h(b)u\|^2 = 0$. (b) With $A =
A^*$ quantising $a\mathrm{Id}$ and $\mathrm{WF}'_h(A)\subset\mathrm{supp}\,a$, (3.1) gives
$\frac2h\mathrm{Im}\langle\mathbf Pu,Au\rangle = \langle Cu,u\rangle$, and by (6.2) the principal symbol of $\varsigma C$
is $Va+2a(p^\natural-\lambda_jq^\natural)+O((\mathrm{Im}\,z_j)^2)$, which converges in $C_c^\infty$ to
$Va+2a(p^\natural-\eta q^\natural)$; as $\langle\mathrm{Op}_h(c_j-c)u,u\rangle\to0$ when $c_j\to c$ uniformly (Lemma 6.2
(a)), $\langle\varsigma Cu,u\rangle\to\int\mathrm{tr}((Va+2a(p^\natural-\eta q^\natural))d\mu)$, and
$\mathrm{tr}(Va\,d\mu) = Va\,d\nu$ for scalar $a$. The left side is bounded by $\frac2h(\|Y\mathbf
Pu\|+O(h^\infty))(\|AYu\|+O(h^\infty))$ and $\|AYu\|\le2\sup|a|\,\|Yu\|+Ch^{\frac12}$ by the argument of Lemma 6.2 (a).
(c) is the same computation with $\mathrm{Im}\,\Phi = 0$. $\square$

### 6.4 The estimate with loss one

**Proposition 6.4 ([Hin26c] Theorem 9.28 with loss 1).** Let $\beta>\gamma_-$ and $U$ a neighbourhood of $\Gamma$. There
are $B,E,G\in\Psi^0$ microsupported in $U$, $B$ elliptic at $\Gamma$, $\mathrm{WF}'_h(E)\cap\Gamma^\natural_u =
\emptyset$, with: every backward $V$-curve from a point of $\mathrm{WF}'_h(B)\setminus\Gamma^\natural_u$ reaches
$\mathrm{Ell}_h(E)$ in finite time within $\mathrm{Ell}_h(G)$; $\Gamma\cup\mathrm{WF}'_h(B)\subset\mathrm{Ell}_h(G)$; and
for $z\in z_0+i[h\beta,\nu']$, $h<h_0$,
$$\|Bu\|\le C\big(h^{-2}\|G\mathbf Pu\|+h^{-1}\|Eu\|+h^N\|u\|_{-N}\big).\tag{6.6}$$

*Proof.* Fix $\gamma>\gamma_+$. For $\mathrm{Im}\,z\ge h\gamma$, (6.6) follows from (6.4). Choose $B,E,G$ for the
dynamics as stated, with $\mathrm{WF}'_h(B)\subset\Gamma(\delta_0)^\circ\subset\mathrm{Ell}_h(G)$; this is possible by
(D1)-(D2). Suppose (6.6) fails for every $C$ in the range $h\beta\le\mathrm{Im}\,z\le h\gamma$. Then there are $h_j\to0$,
$z_j$ and $u_j$ with
$$\|Bu\| = 1,\qquad\|G\mathbf Pu\| = o(h^2),\qquad\|Eu\| = o(h),\qquad h^N\|u\|_{-N} = o(1),\tag{6.7}$$
and after passing to a subsequence $\mathrm{Im}\,z_j/h_j\to\eta\in[\beta,\gamma]$ and $(u_j)$ has a defect measure $\mu$
on $U_1 := \mathrm{Ell}_h(B)$ ($B$ itself shows $(u_j)$ is tempered there). We use Proposition 4.5 and Corollary 4.6
(real principal type) for the $\mathbf P_j$, with constants uniform in $j$; for $\mathrm{Im}\,z_j<0$ they hold near
$\Gamma$ because $\lambda_j$ is bounded, so $\lambda_j\mathcal Q$ is a bounded term of the class of $\mathcal P_1$ over
the compact set $K_\Gamma$, and the absorbing sign is not needed (Remark 4.7).

*Localisation.* For $\varpi\in U_1\setminus\Gamma^\natural_u$, the backward $V$-curve from $\varpi$ reaches
$\mathrm{Ell}_h(E)$ within $\mathrm{Ell}_h(G)$, so Corollary 4.6 gives $\|B'u\|\le C(h^{-1}\|G\mathbf
Pu\|+\|Eu\|+h^N\|u\|_{-N}) = o(1)$ for $B'$ elliptic at $\varpi$; so $\varpi\notin\mathrm{supp}\,\mu$. With Lemma 6.3
(a), $\mathrm{supp}\,\mu\subset\Gamma^\natural_u\cap\Sigma_{z_0}$. By (D2), backward curves from
$\Gamma^\natural_u\cap\mathrm{WF}'_h(B)$ reach any neighbourhood of $\Gamma$; so with $E'$ elliptic on $\Gamma$,
$\|Bu\|\le C(h^{-1}\|G\mathbf Pu\|+\|Eu\|+\|E'u\|+h^N\|u\|_{-N})$, and it suffices to find such $E'$ with $\|E'u\|\to0$.
Taking $\mathrm{WF}'_h(E')\subset\Gamma(\delta)$, $\|E'u\|^2\to\int|e'|^2d\nu$, and it suffices to show $\mathsf
m(\delta) = 0$ for some $\delta>0$, where
$$\mathsf m(x) := \nu\big(\Gamma^\natural_u\cap\Gamma(\delta_0)\cap\{|\phi^\natural_s|<x\}\big).$$

*Step 1: an auxiliary equation.* Let $\Phi$, $N_u$, $J_u\in\Psi^0$ be self-adjoint quantisations of
$\phi^\natural_u\mathrm{Id}$, $\nu^\natural_u\mathrm{Id}$, $j^\natural_u\mathrm{Id}$, cut off to $U_1$ and equal to the
uncut quantisations modulo $h^\infty$ near $\Gamma(\delta_0)$. By Theorem 2.4 and (6.2) (the symbols being scalar, the
commutator of the matrix-valued lower order part of $\mathbf P$ with $\Phi$ is in $h^2\Psi$), $\varsigma\frac ih[\mathbf
P,\Phi] = -N_u\Phi+J_u\mathbf P+hR+R_{\mathrm{away}}$, with $R\in\Psi^0$ and $R_{\mathrm{away}}$ microsupported off
$\Gamma(\delta_0)$, as $\mathrm{Im}\,z = O(h)$. Hence $f := \mathbf Pu$ gives
$$(\mathbf P-i\varsigma hN_u)\Phi u = (\Phi-i\varsigma hJ_u)f-i\varsigma h^2Ru+R'_{\mathrm{away}}u.\tag{6.8}$$
The operator $\mathbf P' := \mathbf P-i\varsigma hN_u$ is of the form of Proposition 6.1 with $p'^\natural =
p^\natural-\nu^\natural_u$, and $\sup_\Gamma\lambda_{\max}(p^\natural-\beta
q^\natural-\nu^\natural_u)\le\sup_\Gamma\lambda_{\max}(p^\Gamma_1-\beta q^\natural)-\nu_{\min}<0$, because
$\beta>\gamma_-$ means $\sup_\Gamma\lambda_{\max}(p^\Gamma_1-\beta q^\natural)<\frac12\nu_{\min}$. So Proposition 6.1
applies to $\mathbf P'$ with $\gamma := \beta$, on a small neighbourhood of $\Gamma$, with operators $B_1,E_1,G_1$. Its
right side for $\Phi u$: $h^{-1}\|G_1(\ldots)\| = O(h)$ by (6.7) and $\sup\|G_1u\|<\infty$; $\|E_1\Phi u\|\le
C\|E_1'u\|+O(h^\infty)$ with $E'_1$ microsupported off $\Gamma^\natural_u$ near $\mathrm{WF}'_h(E_1)$, and $\|E'_1u\| =
o(h)$ by Corollary 4.6 as in the localisation; the last term is $O(h^\infty)$. So $\|B_1\Phi u\| = O(h)$.

*Step 2.* Lemma 6.3 (c) with $\Phi$ and $Y := B_1$-elliptic cut-off gives, for real $a\in
C_c^\infty(\mathrm{Ell}_h(B_1))$, $|\int H_{\phi^\natural_u}a\,d\nu|\le C_1\sup|a|$, $C_1$ independent of $a$. Take $a :=
a_0(\phi^\natural_u)a_1(\phi^\natural_s)\psi(G_{z_0})$ with $a_0,\psi\in C_c^\infty((-\delta_0,\delta_0))$ equal to 1
near 0, $|a_0|,|\psi|\le1$, and $a_1(t) := \theta(t/\delta)\chi_c(t)$, where $\theta$ is smooth, non-decreasing,
$\theta(s) = \mp1$ for $\pm s\le-2$, $\theta'\ge\frac12$ on $[-1,1]$, and $\chi_c\in C_c^\infty((-\delta_0,\delta_0))$
equals 1 on $[-\frac{\delta_0}2,\frac{\delta_0}2]$ with $|\chi_c'|\le4/\delta_0$. On
$\mathrm{supp}\,\nu\subset\Gamma^\natural_u\cap\Sigma_{z_0}$, $H_{\phi^\natural_u}a =
a_1'(\phi^\natural_s)\{\phi^\natural_u,\phi^\natural_s\}$ (the other terms contain $H_{\phi_u}\phi_u = 0$, or
$\psi'(G_{z_0})$, which vanishes near $\Sigma_{z_0}$). Replacing $a_1$ by $-a_1$ if
$\{\phi^\natural_u,\phi^\natural_s\}<0$, and using $a_1'\ge\frac1{2\delta}$ on $[-\delta,\delta]$, $a_1'\ge0$ on
$[-2\delta,2\delta]$ and $|a_1'|\le4/\delta_0$ elsewhere:
$$\frac{c_\Gamma}{2\delta}\,\mathsf m(\delta)\le C_1+\frac{4C_\Gamma}{\delta_0}\nu(U_1),\qquad\text{so}\qquad\mathsf
m(\delta)\le C_2\,\delta\tag{6.9}$$
with $C_2$ independent of $\delta\in(0,\delta_0/4)$.

*Step 3: propagation for logarithmic times.* Lemma 6.3 (b), with $\|G\mathbf Pu\| = o(h^2)$, gives
$\int(Va\,d\nu+2a\,\mathrm{tr}((p^\natural-\eta q^\natural)d\mu)) = 0$ for real $a\in C_c^\infty(\mathrm{Ell}_h(B))$. Let
$p_\eta := \lambda_{\max}(p^\natural-\eta q^\natural)$, continuous; for $a\ge0$ Lemma 6.2 gives
$\int(Va+2ap_\eta)\,d\nu\ge0$. Since $\eta\ge\beta$ and $q^\natural>0$, $p_\eta\le\lambda_{\max}(p^\natural-\beta
q^\natural)$, and $\beta>\gamma_-$ gives $\sup_\Gamma p_\eta<\frac12\nu_{\min}$; so we can fix $\lambda'$ with
$\sup_{\Gamma(\delta_0)}p_\eta^+/\nu^\natural_s<\lambda'<\frac12$ (shrinking $\delta_0$; $p_\eta^+ := \max(p_\eta,0)$).
Take $a := a_0(\phi^\natural_u)a_1(\phi^\natural_s)\psi(G_{z_0})$ with $a_0,\psi$ as before and $a_1(t) :=
|t|^{-2\lambda'}f(|t|)$, $f\in C_c^\infty((\frac\delta2,\delta_0))$, $f\ge0$, $f = 1$ on $[\delta,\frac{\delta_0}2]$,
$f'\le0$ on $[\delta,\infty)$, $|xf'(x)|\le4$ on $[\frac\delta2,\delta]$. On $\mathrm{supp}\,\nu$, by (6.3),
$V|\phi^\natural_s|^{-2\lambda'} = -2\lambda'\nu^\natural_s|\phi^\natural_s|^{-2\lambda'}$, so
$$Va+2ap_\eta = \nu^\natural_s|\phi^\natural_s|^{-2\lambda'}\Big(-2\big(\lambda'-\frac{p_\eta}{\nu^\natural_s}\big)f+|
\phi^\natural_s|f'(|\phi^\natural_s|)\Big).$$
This is $\le0$ where $|\phi^\natural_s|\ge\delta$, $\le-c_3$ on $\{\delta\le|\phi^\natural_s|\le\frac{\delta_0}2\}$ with
$c_3>0$ independent of $\delta$, and bounded by $C\delta^{-2\lambda'}$ on
$\{\frac\delta2\le|\phi^\natural_s|\le\delta\}$. Hence $c_3(\mathsf m(\frac{\delta_0}2)-\mathsf m(\delta))\le
C\delta^{-2\lambda'}\mathsf m(\delta)$.

*Step 4.* With (6.9), $\mathsf m(\frac{\delta_0}2)\le(1+C\delta^{-2\lambda'})C_2\delta\to0$ as $\delta\to0$, since
$2\lambda'<1$. So $\mathsf m(\frac{\delta_0}2) = 0$, contradicting $\|Bu\| = 1$ as explained. $\square$

The proof in [Hin26c] writes the range as $-\beta\le h^{-1}\mathrm{Im}\,z$ and $p_z\le p_1+2\beta\beta_0$, while its
theorem is stated for $\mathrm{Im}(h^{-1}z)\ge\beta$. With the range $\eta\ge\beta$ the bound used is
$p_\eta\le\lambda_{\max}(p^\natural-\beta q^\natural)$, and Steps 1 and 3 need exactly
$\sup_\Gamma\lambda_{\max}(p^\Gamma_1-\beta q^\natural)<\frac12\nu_{\min}$, which is the definition of $\beta>\gamma_-$
in (1.4). When $\beta<0$ this involves the largest value of $q^\natural$ on $\Gamma$, not the smallest, which is why
(1.4) defines $\gamma_\pm$ as these thresholds and not through $\beta_0$ alone (section 10, (F7)-(F8)). The steps and the
use of $\{\phi_u,\phi_s\}$ follow [Hin26c], which follows [Dya16]; the matrix-valued measure enters only through
$\mathrm{tr}$ and $\lambda_{\max}$ (Lemma 6.2).

### 6.5 Complex absorption

To interpolate between Propositions 6.1 and 6.4 we need an invertible problem depending holomorphically on $\sigma$,
equal to $\mathbf P$ near $\Gamma$. As in [Hin26c] the absorbing operator is built by averaging a symbol in the time
frequency, which makes it entire in $\sigma$; here it is also written as $W^*W$, so that its sign is exact. We write the
construction for $z_0 = 1$; for $z_0 = -1$, $\tilde q_1$ below is defined with $-\tau$ in place of $\tau$, and the factor
$z_0$ in (6.10) makes the absorbing sign the right one.

Let $\chi_0\in C_c^\infty((-1,1))$ equal 1 on $[-\frac12,\frac12]$ and $\Psi(\sigma) := (2\pi)^{-1}\int e^{-i\sigma
s}\chi_0(s)\,ds$: $\Psi$ is entire, $\int_{\mathbb R}\Psi(\tau+i\eta)\,d\tau = \chi_0(0) = 1$ for every $\eta$ (shift of
contour), and $|\partial^k\Psi(\tau+i\eta)|\le C_{k,N}\langle\tau\rangle^{-N}e^{|\eta|}$ (Paley-Wiener). Let $\tilde
q_0\in C^\infty(T^*\tilde X^\circ)$, $0\le\tilde q_0\le1$, with $\tilde q_0 = 0$ on $\Gamma(\frac{\delta_0}2)$ and
$\tilde q_0 = 1$ off $\Gamma(\frac34\delta_0)$. Put
$$a(x;\tau,\zeta) := \big(1-\chi_0(|(\tau,\zeta)|)\big)\,|(\tau,\zeta)|\,\tilde q_1(x;\tau,\zeta),\qquad\tilde q_1 :=
\begin{cases}\tilde q_0(x,\zeta/\tau),&\tau>0,\ (x,\zeta/\tau)\in\Gamma(\delta_0),\\1&\text{otherwise}.\end{cases}$$
$\tilde q_1$ is smooth and homogeneous of degree 0 on $(\tau,\zeta)\ne0$, because $\tilde q_0 = 1$ near the boundary of
$\Gamma(\delta_0)$ and $|\zeta/\tau|$ is large near $\tau = 0$, $\zeta\ne0$; so $a$ is a symbol of order 1 in
$(\tau,\zeta)$, homogeneous of degree 1 for $|(\tau,\zeta)|\ge1$. Let $a_\flat(x;\sigma,\zeta) :=
\int\Psi(\sigma-\tau)a(x;\tau,\zeta)\,d\tau$, entire in $\sigma$; for $|\mathrm{Im}\,\sigma|\le C$,
$a_\flat-a(\cdot;\mathrm{Re}\,\sigma,\cdot)$ is a symbol of order 0 in $(\mathrm{Re}\,\sigma,\zeta)$, uniformly, by
Taylor's formula in $\tau$ and $\int\Psi = 1$. Let $\chi\in C_c^\infty(\mathbb R^4)$, $0\le\chi\le1$, equal 1 near the
base projection of $\Gamma(\delta_0)$, and $\chi_1\in C_c^\infty$ equal 1 on $\mathrm{supp}\,\chi$, both supported in the
interior of $K_\Gamma$. With $\mathrm{Op}$ the standard quantisation in $x$ (dual variable $\zeta$, $\sigma$ a
parameter), acting componentwise,
$$\hat Q_\flat(\sigma) := \chi_1\mathrm{Op}(a_\flat(\cdot;\sigma,\cdot))\chi_1,\qquad\hat Q(\sigma) := \hat
Q_\flat(\bar\sigma)^*\hat Q_\flat(\sigma),$$
$$\hat P'(\sigma) := \chi\hat P(\sigma)\chi-iz_0\big(\chi\hat Q(\sigma)\chi+(1-\chi^2)(\sigma^2+\Delta)\big),\qquad
P'_{h,z} := h^2\hat P'(z/h),\tag{6.10}$$
on $\mathbb R^4$, $\Delta\ge0$ the Euclidean Laplacian. All three terms are entire in $\sigma$ ($\sigma\mapsto\hat
Q_\flat(\bar\sigma)^*$ is holomorphic, being antiholomorphic composed with the antilinear adjoint).

**Lemma 6.5.** Let $\mathrm{Re}\,z = z_0$ and $\mathrm{Im}\,z = h\eta$, $|\eta|\le C$. (a) $W := h\hat
Q_\flat(z/h)\in\Psi^{(1,0,0)}$ has principal symbol $w := \chi_1^2|(1,\zeta)|\tilde q_0$, and $h^2\hat Q(z/h) =
W^*W+hR_W$ with $R_W\in\Psi^{(1,0,0)}$. (b) $\mathrm{WF}'_h(W)\cap\Gamma(\frac{\delta_0}3) = \emptyset$; so
$P'_{h,z}-P_{h,z}$ is microlocally $O(h^\infty)$ near $\Gamma(\frac{\delta_0}3)$. (c) $P'_{h,z}$ is semiclassically
elliptic, in the scattering sense on all of $\mathcal P$, outside $\Gamma(\frac34\delta_0)$. (d) Over $\{\chi = 1\}$,
$h^{-1}\mathrm{Im}\,P'_{h,z} = h^{-1}\mathrm{Im}\,P_{h,z}-z_0h^{-1}W^*W-z_0\mathrm{Re}\,R_W$ and
$\mathrm{Re}\,P'_{h,z}-\mathrm{Re}\,P_{h,z} = z_0h\,\mathrm{Im}\,R_W$.

*Proof.* (a) For a symbol $b$ of order $m$ in $(\sigma,\zeta)$, $h^mb(x;z/h,\zeta/h)$ is a semiclassical symbol of order
$(m,0,0)$: its $\zeta$-derivatives of order $k$ are $h^{m-k}(\partial^kb)$ at $(z/h,\zeta/h)$, bounded by
$C(|z|^2+|\zeta|^2)^{(m-k)/2}$. Hence $h(a_\flat-a)(x;z/h,\zeta/h)\in hS^0$, and $h\,a(x;1/h,\zeta/h) = |(1,\zeta)|\tilde
q_1(x;1,\zeta) = |(1,\zeta)|\tilde q_0(x,\zeta)$ for $h\le1$ (homogeneity), with $\tilde q_0 := 1$ off
$\Gamma(\delta_0)$; and $\mathrm{Op}(b(x;\sigma,\zeta)) = \mathrm{Op}_h(b(x;\sigma,\zeta/h))$. $h\hat Q_\flat(\bar
z/h)-W\in h\Psi^0$ since $a_\flat(\bar\sigma)-a_\flat(\sigma)$ is of order 0; so $h^2\hat Q = W^*W+hR_W$ with $R_W :=
(h^{-1}(h\hat Q_\flat(\bar z/h)-W))^*W$. (b) If $(x,\zeta)\in\Gamma(\frac{\delta_0}3)$ and $|h\tau-1|\le\epsilon$, then
$(x,\zeta/(h\tau))\in\Gamma(\frac{\delta_0}2)$ for $\epsilon$ small (uniform continuity of $\phi_u,\phi_s,G_1$ on a
compact set), so $a(x;\tau,\zeta/h) = 0$; the rest of the integral defining $a_\flat(x;1/h+i\eta,\zeta/h)$ is over
$|\tau-1/h|\ge\epsilon/h$, where $|\Psi|\le C_N(h/\epsilon)^N$, and likewise for all derivatives. So the symbol of $W$ is
$O(h^\infty)$ in $S^{(1,0,0)}$ near $\Gamma(\frac{\delta_0}3)$, and so is $R_W$ (which ends in $W$). Near the base
projection of $\Gamma(\delta_0)$, $\chi = 1$ and $1-\chi^2 = 0$. (c) The principal symbol of $P'_{h,z}$ is
$\chi^2G_{z_0}-iz_0(1+|\zeta|^2)\big(\chi^2\tilde q_0^2+1-\chi^2\big)$, as $\chi_1 = 1$ on $\mathrm{supp}\,\chi$ and $z^2
= 1+O(h)$. Its imaginary part vanishes only where $\chi = 1$ and $\tilde q_0 = 0$, which is inside
$\Gamma(\frac34\delta_0)$; at fibre infinity $\tilde q_0 = 1$, and over $\partial X$, $\chi = 0$ and the symbol is
$-iz_0(z^2+|\zeta|^2)$. (d) $W^*W$ is self-adjoint, and $\mathrm{Im}(-iX) = -\mathrm{Re}\,X$, $\mathrm{Re}(-iX) =
\mathrm{Im}\,X$. $\square$

By (d), in the region $0<\tilde q_0<1$, $\mathbf P'\in\{P',P'^*\}$ has the structure of Proposition 4.5 with the
additional term $-\epsilon_\flat z_0h^{-1}W^*W$ in $h^{-1}\mathrm{Im}\,\mathbf P'$ and a bounded addition to $\mathcal
P_1$; since $\varsigma\epsilon_\flat z_0 = z_0^2 = 1$, Remark 4.7 (b) applies, and Proposition 4.5 holds for it.

**Lemma 6.6 (three lines).** Let $F$ be holomorphic near the rectangle $\mathcal R := [a-L,a+L]+i[0,1]$, with values in a
Hilbert space, $\|F\|\le M$ on $\mathcal R$, $\|F\|\le M_0$ on $\{\mathrm{Im}\,w = 0\}$ and $\|F\|\le M_1$ on
$\{\mathrm{Im}\,w = 1\}$, where $0<M_0,M_1\le M$. Then for $|\mathrm{Re}\,w-a|\le\frac L2$ and $y := \mathrm{Im}\,w$,
$$\|F(w)\|\le M_0^{1-y}M_1^y\exp\big(3\Lambda e^{-\pi L/4}\big),\qquad\Lambda := \log\frac M{\min(M_0,M_1)}.$$

*Proof.* $u := \log\|F\|$ is subharmonic, as the supremum over unit vectors $e$ of the subharmonic functions
$\log|\langle F,e\rangle|$, attained at each point, and upper semicontinuous. $v := (1-y)\log M_0+y\log M_1$ is harmonic,
and so is $k(w) := \cosh(\frac\pi2(x-a))\cos(\frac\pi2(y-\frac12))/\cos\frac\pi4$, $x := \mathrm{Re}\,w$; $k\ge1$ on
$\mathcal R$ and $k\ge\cosh(\frac\pi2L)$ on its vertical sides. So $u-v-\Lambda k/\cosh(\frac\pi2L)\le0$ on
$\partial\mathcal R$ ($u-v\le0$ on the horizontal sides and $\le\Lambda$ on the vertical ones), hence on $\mathcal R$ by
the maximum principle. For $|x-a|\le\frac L2$,
$k/\cosh(\frac\pi2L)\le\sqrt2\cosh(\frac\pi4L)/\cosh(\frac\pi2L)\le2\sqrt2e^{-\pi L/4}$. $\square$

**Proposition 6.7 ([Hin26c] Lemma 9.33).** Let $\gamma_-<\beta<\gamma_+<\beta'$. There is $h_0$ such that for $z\in
z_0+i[h\beta,h\beta']$ and $h<h_0$, $P'_{h,z}:H^{(2,0,0)}_h\to L^2$ is invertible, and
$$\|(P'_{h,z})^{-1}\|_{L^2\to L^2}\le Ch^{-1-(\beta'-\mathrm{Im}(z/h))/(\beta'-\beta)}.\tag{6.11}$$
Consequently, for every $\epsilon>0$ and $z\in z_0+i[h(\gamma_-+\epsilon),h(\gamma_++\epsilon)]$, $\|(P'_{h,z})^{-1}\|\le
C_\epsilon h^{-1-\delta_\Gamma(\mathrm{Im}(z/h)-\epsilon)}$.

*Proof.* (a) *A priori estimates.* Let $\mathbf P'\in\{P',P'^*\}$. Outside $\Gamma(\frac34\delta_0)$, Proposition 4.2
bounds $u$ by $\|\mathbf P'u\|_{H^{(-2,0,0)}_h}$. In $\Gamma(\delta_0)$: a point of the characteristic set not on
$\Gamma^\natural_u$ has a backward $V$-curve that leaves $\Gamma(\delta_0)$ (D1), crossing $\{0<\tilde q_0<1\}$ into
$\{\tilde q_0 = 1\}$, where $\mathbf P'$ is elliptic; Corollary 4.6 (with Remark 4.7) propagates the elliptic bound along
it. Near $\Gamma$, Proposition 6.4, applied with all its operators microsupported in $\Gamma(\frac{\delta_0}3)$, where
$\mathbf P' = \mathbf P$ modulo $O(h^\infty)$ (Lemma 6.5 (b)), with its term $\|Eu\|$ bounded by the propagation just
described. Altogether, for $z\in z_0+i[h\beta,h\beta']$,
$$\|u\|_{L^2}\le Ch^{-2}\|\mathbf P'u\|_{L^2}+Ch^N\|u\|_{-N\mathbf 1},$$
and with $h^{-1}$ in place of $h^{-2}$ at $\mathrm{Im}\,z = h\beta'$, using Proposition 6.1 there; the last term is
absorbed for $h<h_0$. (b) *Invertibility.* For fixed $h$, $P'_{h,z}$ is elliptic in the scattering sense at fibre
infinity and over $\partial X$ (Lemma 6.5 (c)), so it has a parametrix modulo an operator with symbol in $S^{-K\mathbf
1}$, $K$ large, which is compact on $L^2$; so $P'_{h,z}:H^{(2,0,0)}_h\to L^2$ is Fredholm, and by (a) it and its adjoint
are injective. (c) *Interpolation.* In terms of $\sigma = z/h$, (a) gives $\|\hat P'(\sigma)^{-1}\|_{L^2\to L^2}\le C$
for $\mathrm{Re}\,\sigma\ge h_0^{-1}$ and $\mathrm{Im}\,\sigma\in[\beta,\beta']$, and $\le C|\sigma|^{-1}$ on
$\mathrm{Im}\,\sigma = \beta'$ (here $\|\hat P'(\sigma)u\|_{L^2} = h^{-2}\|P'_{h,z}u\|_{L^2}$ with $h :=
|\mathrm{Re}\,\sigma|^{-1}$; for $z_0 = -1$ use $\mathrm{Re}\,\sigma\le-h_0^{-1}$). For $\sigma_0\ge h_0^{-1}$, $f\in
L^2$ and $\kappa := \beta'-\beta$, apply Lemma 6.6 to $F(w) := \hat P'(3\sigma_0+i\beta+\kappa w)^{-1}f$ on
$[-\frac{2\sigma_0}\kappa,\frac{2\sigma_0}\kappa]+i[0,1]$, with $M = M_0 = C\|f\|$, $M_1 = C\sigma_0^{-1}\|f\|$, $L =
2\sigma_0/\kappa$, $\Lambda = \log\sigma_0$; $\Lambda e^{-\pi L/4}\to0$, so $\|\hat P'(\sigma)^{-1}f\|\le
C\sigma_0^{-(\mathrm{Im}\,\sigma-\beta)/\kappa}\|f\|$ for $\mathrm{Re}\,\sigma\in[2\sigma_0,4\sigma_0]$, with $C$
independent of $\sigma_0$. With $|\sigma|\le5\sigma_0$ and $(P'_{h,z})^{-1} = h^{-2}\hat P'(z/h)^{-1}$ this is (6.11).
For the consequence take $\beta := \gamma_-+\epsilon$ and $\beta' := \gamma_++\epsilon$; then
$(\beta'-\eta)/(\beta'-\beta) = \delta_\Gamma(\eta-\epsilon)$ for $\eta\in[\beta,\beta']$. $\square$

### 6.6 The precise loss

**Theorem 6.8 ([Hin26c] Theorem 9.28 on $E$).** Let $\beta>\gamma_-$ and $U$ a neighbourhood of $\Gamma$. There are
$B,E,G\in\Psi^0$ microsupported in $U$, with $B$ elliptic at $\Gamma$, $\mathrm{WF}'_h(E)\cap\Gamma^\natural_u =
\emptyset$, $\Gamma\cup\mathrm{WF}'_h(B)\subset\mathrm{Ell}_h(G)$, and every backward $V$-curve from
$\mathrm{WF}'_h(B)\setminus\Gamma^\natural_u$ reaching $\mathrm{Ell}_h(E)$ within $\mathrm{Ell}_h(G)$, such that for
$z\in z_0+i[h\beta,\nu']$, $h<h_0$, $\epsilon>0$ and all $N$, with $\delta := \delta_\Gamma(\mathrm{Im}(z/h)-\epsilon)$,
$$\|Bu\|\le C_\epsilon\big(h^{-1-\delta}\|G\mathbf Pu\|+h^{-\delta}\|Eu\|+h^N\|u\|_{-N}\big).\tag{6.12}$$

*Proof.* For $\mathrm{Im}\,z\ge h(\gamma_++\epsilon)$ this is (6.4), with $\delta = 0$; for
$\mathrm{Im}\,z\in[h\beta,h(\gamma_-+\epsilon)]$ it is (6.6), as then $\delta = 1$. Let
$\mathrm{Im}\,z\in[h(\gamma_-+\epsilon),h(\gamma_++\epsilon)]$. We follow [HV16] Theorem 4.7 as recalled in [Hin26c]; all
operators have kernels supported over $\{\chi = 1\}^2$. Fix $c\in(0,\frac{\delta_0}{12})$. Choose $B$ elliptic at
$\Gamma$ with $\mathrm{WF}'_h(B)\subset\Gamma(\frac c2)$, and $B^\sharp\in\Psi^0$ with
$\mathrm{WF}'_h(B^\sharp)\subset\Gamma(c)$ and $\mathrm{WF}'_h(I-B^\sharp)\cap\Gamma(\frac{3c}4) = \emptyset$;
$\Gamma(c)\subset\Gamma(\frac{\delta_0}3)$. Then $B(I-B^\sharp)$ is residual and, by Lemma 6.5 (b),
$$Bu = B(P'_{h,z})^{-1}B^\sharp\mathbf Pu+B(P'_{h,z})^{-1}[\mathbf P,B^\sharp]u+O(h^\infty)\|u\|_{-N}$$
(for $\mathbf P = P^*$ use $(P'^*)^{-1}$). The first term is bounded by $C_\epsilon h^{-1-\delta}(\|G\mathbf
Pu\|+h^N\|u\|_{-N})$ by Proposition 6.7. The commutator is $h$ times an operator microsupported in
$\Gamma(c)\setminus\Gamma(\frac{3c}4)$. Let $X_u\in\Psi^0$ be microsupported in
$\Gamma(\delta_0)\cap\{|\phi^\natural_u|<c/8\}$, with $\mathrm{WF}'_h(I-X_u)$ disjoint from
$\Gamma^\natural_u\cap\Gamma(c)$, and such that backward $V$-curves from $\mathrm{WF}'_h(I-X_u)\cap\Gamma(c)$ reach
$\mathrm{Ell}_h(E)$ ((D1), choosing $E$ elliptic on $\Gamma(\delta_0)\cap\{|\phi^\natural_u|\ge c/16\}$). (i) By
Corollary 4.6, $\|(I-X_u)[\mathbf P,B^\sharp]u\|\le Ch(h^{-1}\|G\mathbf Pu\|+\|Eu\|+h^N\|u\|_{-N})$, and Proposition 6.7
turns this into a bound $C_\epsilon h^{-\delta}(h^{-1}\|G\mathbf Pu\|+\|Eu\|+h^N\|u\|_{-N})$ for
$B(P')^{-1}(I-X_u)[\mathbf P,B^\sharp]u$. (ii) $f_u := X_u[\mathbf P,B^\sharp]u$ is microsupported in $K_f :=
\Gamma(c)\setminus\Gamma(\frac{3c}4)\cap\{|\phi^\natural_u|<\frac c8\}$, where $|\phi^\natural_s|\ge\frac{3c}4$ or
$|G_1|\ge\frac{3c}4$. Let $\tilde Q\in\Psi^0$ be self-adjoint with non-negative principal symbol, elliptic on
$\Gamma(\frac c4)$ and microsupported in $\Gamma(\frac c2)$. Then every backward bicharacteristic of the characteristic
set in $\Gamma(\delta_0)$ reaches $\mathrm{Ell}_h(\tilde Q)$ (if on $\Gamma^\natural_u$, by (D2)) or the region $\tilde
q_0 = 1$, so the argument of (a) above (with $-i\tilde Q$ as a further absorbing term) gives $\|(P'-i\tilde Q)^{-1}\|\le
Ch^{-1}$, and Lemma 6.9 below applies to $P'-i\tilde Q$. The forward $V$-flowout of $K_f\cap\Sigma_{z_0}$ stays in
$\{|\phi^\natural_s|\ge\frac{3c}4\}$ while it remains in $\Gamma(\delta_0)$ (as $|\phi^\natural_s|$ increases forward),
and the part of $K_f$ off $\Sigma_{z_0}$ is elliptic; so the flowout misses $\mathrm{WF}'_h(\tilde
Q)\cup\mathrm{WF}'_h(B)\subset\Gamma(\frac c2)$. By Lemma 6.9, $\tilde Q(P'-i\tilde Q)^{-1}f_u$ and $B(P'-i\tilde
Q)^{-1}f_u$ are $O(h^\infty)\|u\|_{-N}$. Since $v := (P')^{-1}f_u-(P'-i\tilde Q)^{-1}f_u$ satisfies $P'v = -i\tilde
Q(P'-i\tilde Q)^{-1}f_u$, Proposition 6.7 gives $\|v\|\le C_Nh^N\|u\|_{-N}$; so $\|B(P')^{-1}f_u\|\le C_Nh^N\|u\|_{-N}$.
Summing (i) and (ii) gives (6.12). $\square$

**Lemma 6.9 (direction of propagation).** Let $\mathbf P''$ be $P'-i\tilde Q$ (or its adjoint, with forward replaced by
backward) with $\|(\mathbf P'')^{-1}\|\le Ch^{-1}$. Let $X\in\Psi^0$ be microsupported in a compact $K\subset T^*\tilde
X^\circ$, and let $\varpi$ not lie in the closure of the forward $V$-flowout of $K\cap\Sigma_{z_0}$ inside
$\Gamma(\delta_0)$. Then there is $B_\varpi$ elliptic at $\varpi$ with $\|B_\varpi(\mathbf P'')^{-1}Xf\|\le
C_Nh^N\|f\|_{-N\mathbf 1}$.

*Proof.* If $\varpi$ is in the elliptic set of $\mathbf P''$, Proposition 2.10 gives $\|B_\varpi w\|\le C(\|G\mathbf
P''w\|+h^N\|w\|)$ with $G$ microsupported near $\varpi$, off $K$. Otherwise the backward $V$-curve from $\varpi$ reaches
the elliptic set of the absorption without meeting $K$, and Corollary 4.6 gives $\|B_\varpi w\|\le C(h^{-1}\|G\mathbf
P''w\|+h^N\|w\|)$ with $G$ microsupported near that curve, again off $K$. Take $w := (\mathbf P'')^{-1}Xf$: $G\mathbf
P''w = GXf = O(h^\infty)$ and $\|w\|\le Ch^{-1}\|Xf\|$. $\square$

## 7. The artificial boundary

This is [Hin26c] Proposition 9.35, the semiclassical form of I.A section 6. The source proves the energy estimate for
$h^{-1}\mathrm{Im}\,z$ large and cites [Hin25a] Theorem 9.44 for bounded $h^{-1}\mathrm{Im}\,z$; here one argument covers
every $z$ with $\mathrm{Im}\,z\ge0$, the weight $e^{\lambda r}$ of I.A Proposition 6.3 supplying the positivity that the
weight in $t$ supplies there only for $h^{-1}\mathrm{Im}\,z$ large. The slab spaces $H^s(\Omega_{a,b})^{\bullet,-}$
(supported at $r = b$, extendible at $r = a$) and $H^s(\Omega_{a,b})^{-,\bullet}$ are those of I.A section 6.1, with the
semiclassical norms $\|u\|_{H^s_h} := \|\langle hD\rangle^su\|$; over the compact slabs used here the decay order plays
no role, and an admissible $\mathsf b$ is constant (section 1.4), so it enters only as the factor $h^{-\mathsf b}$.

### 7.1 The $H^1_h$ estimate

On $M := \mathbb R_t\times\{r_0-2\delta_0<r<r_2\}$ let $g$ be the metric of (H6), time-oriented so that $-\nabla t$ is
future directed, and $\square_g := -\nabla^\mu\nabla_\mu$ componentwise. $dr$ has no $dt$-component, and $g^{-1}(dr,dr) =
G_0(dr)<0$ (H4), so $dr$ is $g$-timelike; the future direction decreases $r$, so $X := \nabla^gr$ is future directed
timelike. For $\mathbb C^N$-valued $u'$ on $M$ let $T[u'](Y,Z) := \mathrm{Re}(\langle
Yu',Zu'\rangle-\frac12g(Y,Z)g^{-1}(\langle du',du'\rangle))$ and ${}^{(Y)}K[u'] := \frac12T[u']^{\mu\nu}(\mathcal
L_Yg)_{\mu\nu}$. I.A Lemma 6.2 holds on $M$ with the same proof: $\mathrm{div}_g(T[u'](W,\cdot)^\sharp) =
-\mathrm{Re}\langle\square_gu',Wu'\rangle+{}^{(W)}K[u']$, and ${}^{(wX)}K = w\,{}^{(X)}K+T(\nabla w,X)$. For future
causal $Y,Z$, $T(Y,Z)\ge0$, and on a compact set $T[u'](X,X)\ge c_0|du'|^2_R$ for a fixed Riemannian metric $R$ on $M$.

**Proposition 7.1.** Let $r_0-2\delta_0<a<b<r_2$ and $Z$ as in section 4. There is $C$ such that for $z\in Z$,
$h\in(0,1]$,
$$\|u\|_{H^1_h(\Omega_{a,b})}\le Ch^{-1}\|P_{h,z}u\|_{L^2(\Omega_{a,b})},\qquad u\in
H^2(\Omega_{a,b})^{\bullet,-},\tag{7.1}$$
and $\|v\|_{H^1_h(\Omega_{a,b})}\le Ch^{-1}\|P^{*h}_{h,z}v\|_{L^2(\Omega_{a,b})}$ for $v\in
H^2(\Omega_{a,b})^{-,\bullet}$. $C$ depends on bounds for the coefficients, on $\inf(-G_0(dr))$ over the slab and on $Z$.

*Proof.* By density (I.A Lemma 6.1 (c)) take $u$ smooth on $\bar\Omega_{a,b}$ and vanishing near $r = b$.
$P_0-\square_g\mathrm{Id} =: L_1$ is first order with $t$-independent coefficients (section 1.2), so $\hat L_1(\sigma) =
\hat L_1(0)+\sigma\ell_0$ with $\ell_0$ a matrix function and $|\hat L_1(z/h)u|\le C(|du|+h^{-1}|u|)$. Let $u'(t,x) :=
e^{-izt/h}u(x)$ on $D := [0,1]_t\times\Omega_{a,b}$, so that $\square_gu' = e^{-izt/h}(\hat P(z/h)-\hat L_1(z/h))u$, and
let $W := wX$ with $w := e^{-2(\mathrm{Im}\,z)t/h}e^{\lambda r}$. Then
$${}^{(W)}K[u'] = w\big({}^{(X)}K[u']+2h^{-1}(\mathrm{Im}\,z)\,T[u'](-\nabla t,X)+\lambda T[u'](X,X)\big)\ge w(\lambda
c_0-C_0)|du'|^2_R,$$
using $\mathrm{Im}\,z\ge0$, $T(-\nabla t,X)\ge0$ and $|{}^{(X)}K|\le C_0|du'|^2_R$. Since $du' =
e^{-izt/h}(du-ih^{-1}z\,u\,dt)$ and $|\alpha+\beta\,dt|_R^2\ge c(|\alpha|_R^2+|\beta|^2)$ for $\alpha$ without
$dt$-component, $w|du'|_R^2\ge c\,e^{\lambda r}(|du|^2+\frac14h^{-2}|u|^2)$, a function of $x$ only. Apply the divergence
theorem to $J := T[u'](W,\cdot)^\sharp$ on $D$. At $r = b$ nothing contributes. At $r = a$ the outward conormal is $-dr$,
and the flux is $-\int wT[u'](X,X)\le0$. At $t = 1$ and $t = 0$ the fluxes are $-E(1)$ and $E(0)$, $E(t) :=
\int_{\{t\}\times\Omega_{a,b}}T[u'](W,-\nabla t)$; as $T[u']$ carries the factor $|e^{-izt/h}|^2 =
e^{2(\mathrm{Im}\,z)t/h}$, which $w$ cancels, and $g$ is $t$-independent, $E(1) = E(0)$. Hence
$$\int_D{}^{(W)}K[u']\le\int_D\mathrm{Re}\langle\square_gu',Wu'\rangle,$$
and as $Wu' = we^{-izt/h}(Xu-ih^{-1}z(Xt)u)$ and the integrands are $t$-independent,
$$c(\lambda c_0-C_0)\int_\Omega e^{\lambda r}\big(|du|^2+\tfrac14h^{-2}|u|^2\big)\le C\int_\Omega e^{\lambda
r}\big(|\hat P(\tfrac zh)u|+|du|+h^{-1}|u|\big)\big(|du|+h^{-1}|u|\big).$$
For $\lambda$ large the terms without $\hat P$ on the right are absorbed, and then $\int e^{\lambda
r}(|du|^2+h^{-2}|u|^2)\le C\lambda^{-2}\int e^{\lambda r}|\hat P(z/h)u|^2$. With $e^{\lambda a}\le e^{\lambda r}\le
e^{\lambda b}$ and $\hat P(z/h) = h^{-2}P_{h,z}$, multiplying by $h^2$ gives (7.1). For $v$: $P^{*h}_{h,z} = h^2\hat
P(z/h)^{*h}$, and $\hat P(\sigma)^{*h}$ is the spectral family at $\bar\sigma$ of the formal adjoint $P_0^{*h}$ (with
respect to $dt\,dx$ and $h$), a stationary operator of the same form with principal symbol $G$. Under $t\mapsto-t$, with
the time orientation reversed, it becomes a stationary operator of this form at the spectral parameter $-\bar z/h$,
$\mathrm{Im}(-\bar z) = \mathrm{Im}\,z\ge0$, for which $-\nabla t$ is again future directed while $-\nabla r$ is now
future directed, the future increasing $r$. The argument above with $X$ replaced by $-\nabla r$, $e^{\lambda r}$ by
$e^{-\lambda r}$, and the roles of $r = a$ and $r = b$ exchanged gives the second estimate. $\square$

### 7.2 All orders

**Proposition 7.2.** For every $s\in\mathbb R$ and slab $\Omega_{a,b}$ with $r_0-\delta_0<a<b<r_2-\delta_0$, uniformly
for $z\in Z$ and $h<h_0$:
(i) $\|u\|_{H^s_h(\Omega_{a,b})^{\bullet,-}}\le Ch^{-1}\|P_{h,z}u\|_{H^{s-1}_h(\Omega_{a,b})^{\bullet,-}}$ for $u\in
H^s(\Omega_{a,b})^{\bullet,-}$;
(ii) $\|v\|_{H^s_h(\Omega_{a,b})^{-,\bullet}}\le Ch^{-1}\|P^{*h}_{h,z}v\|_{H^{s-1}_h(\Omega_{a,b})^{-,\bullet}}$ for
$v\in H^s(\Omega_{a,b})^{-,\bullet}$.

*Proof.* As in I.A Proposition 6.4, with the semiclassical estimates in place of the fixed-frequency ones; we prove (i).
Fix $a'\in(r_0-\delta_0,a)$ and $\Omega' := \Omega_{a',b}$. *Uniqueness* at each fixed $h$ is I.A Proposition 6.4 (iii)
at $\sigma = z/h$. *Existence with bounds, $s\ge0$.* For $f\in H^{s-1}_h(\Omega')^{\bullet,-}\subset
H^{-1}_h(\Omega')^{\bullet,-} = (H^1_h(\Omega')^{-,\bullet})^*$, the functional $P^{*h}_{h,z}\varphi\mapsto\langle
f,\varphi\rangle$ on $\{P^{*h}_{h,z}\varphi:\varphi\in H^2(\Omega')^{-,\bullet}\}\subset L^2$ is bounded by
$Ch^{-1}\|f\|_{H^{-1}_h}\|P^{*h}_{h,z}\varphi\|$, by Proposition 7.1 for the adjoint. Hahn-Banach and Riesz give $w\in
L^2(\Omega')$ with $\|w\|\le Ch^{-1}\|f\|_{H^{-1}_h}$ and $P_{h,z}w = f$, the extension $W$ of $w$ by 0 beyond $b$
satisfying $P_{h,z}W = F$ ($f$'s supported extension) on $\{r>a'\}$. *Regularity.* Over $\{a'<r<b+\delta_0\}$ every
characteristic point of $P_{h,z}$, at finite frequencies or at fibre infinity, lies on a bicharacteristic along which $r$
is strictly monotone: $H_Gr = 2g^{-1}(\nu,dr)\ne0$ for null $\nu\ne0$, $dr$ being timelike; and for $\mathrm{Im}\,z>0$
there is no characteristic point at finite frequencies there (Lemma 1.1 (d)). Its backward direction (in the sense of
Proposition 4.5 for $P$) increases $r$ and reaches $\{r>b\}$, where $W = 0$. Corollary 4.6 at the order $(s,0,0)$,
finitely many times (compactness), with Proposition 4.2 off the characteristic set, gives $\|W\|_{H^s_h(\{r>a\})}\le
C(h^{-1}\|F\|_{H^{s-1}_h}+\|W\|_{L^2})$, the terms $h^N\|GW\|_{H^s_h}$ being absorbed for $h$ small after enlarging the
cover once. So $\|w\|_{H^s_h(\Omega_{a,b})}\le Ch^{-1}\|f\|_{H^{s-1}_h(\Omega')}$. *Conclusion for $s\ge0$.* For $u\in
H^s(\Omega_{a,b})^{\bullet,-}$ extend $Pu$ to $f\in H^{s-1}_h(\Omega')^{\bullet,-}$ with at most twice its norm, solve as
above, and use uniqueness on $\Omega_{a,b}$: $w|_{\Omega_{a,b}} = u$. *$s<0$.* By (ii) for $P^{*h}$ at the order $1-s>0$,
the duality argument of I.A Proposition 6.4 with $(H^{1-s}_h(\Omega')^{-,\bullet})^* = H^{s-1}_h(\Omega')^{\bullet,-}$
gives a solution $w\in H^s_h(\Omega')^{\bullet,-}$ with $\|w\|\le Ch^{-1}\|f\|$; uniqueness concludes. (ii) is the same
with the ends exchanged. $\square$

**Corollary 7.3 (I.A Corollary 6.5, semiclassically).** Let $b',b'',\chi,\chi_1$ be as in I.A Corollary 6.5. For $z\in
Z$, $h<h_0$ and all $s$,
$$\|\chi u\|_{\bar H^s_h}\le C\big(h^{-1}\|P_{h,z}u\|_{\bar H^{s-1}_h(\{r_0<r<b''\})}+\|\chi_1u\|_{H^s_h}\big),\qquad
u\in\bar H^s_h,\tag{7.2}$$
$$\|v|_{\Omega_{r_0,b''}}\|_{H^{1-s}_h(\Omega_{r_0,b''})^{-,\bullet}}\le
Ch^{-1}\|(P^{*h}_{h,z}v)|_{\Omega_{r_0,b''}}\|_{H^{-s}_h(\Omega_{r_0,b''})^{-,\bullet}},\qquad v\in\dot
H^{1-s}_h.\tag{7.3}$$

*Proof.* $P_{h,z}(\chi u) = \chi P_{h,z}u+[P_{h,z},\chi]u$ and $[P_{h,z},\chi] = h\cdot\mathrm{Diff}^1_h$ is supported in
$\mathrm{supp}\,d\chi$, so $h^{-1}\|[P_{h,z},\chi]u\|_{H^{s-1}_h}\le C\|\chi_1u\|_{H^s_h}$. Apply Proposition 7.2 (i) on
$\Omega_{r_0,b''}$; (7.3) is Proposition 7.2 (ii). $\square$

## 8. Proof of Theorem 1.3

Fix $z_0$, $\alpha_+$, $s$ and admissible $\mathsf r,\mathsf b$, and write $\mathbf o := (s,\mathsf r+\alpha_+,\mathsf
b)$, $\mathbf o' := \mathbf o-\mathbf m+(1,1,0) = (s-1,\mathsf r+\alpha_++1,\mathsf b)$. The decay order of $u$ is
$\mathsf r+\alpha_+$, and the thresholds of section 1.4 are conditions on it.

### 8.1 Splitting off the artificial boundary

Choose $r_0<b'_0<b'_1<b'<b''<r_2-\delta_0$ and $\chi,\chi_1$ as in Corollary 7.3 for $b',b''$, and $\psi\in C^\infty$
with $\psi = 0$ on $\{r\le b'_0\}$ and $\psi = 1$ on $\{r\ge b'_1\}$. Over $\{r_0-2\delta_0<r<r_2\}$ the
bicharacteristics move strictly monotonically in $r$, the future direction decreasing it (section 7.2). So a backward
bicharacteristic from a point over $\{r\ge b'_1\}$ stays over $\{r\ge b'_1\}$: it increases $r$ while $r<r_2$, and it
cannot re-enter $\{r<r_2\}$, which it could only do with $r$ decreasing backward. Every estimate of sections 4-6 used
below at points over $\{r\ge b'_1\}$ for the direct problem therefore involves only operators microsupported over
$\{r>b'_0\}$, where $\psi = 1$; applied to $\psi u$, extended by 0 to $\mathbb R^4$, it has $G P\psi u = GPu$ modulo a
residual term.

### 8.2 The direct estimate at $k = 0$

**Proposition 8.1.** Let $\epsilon>0$. (a) There are $\nu_1>0$, $h_0$ and $C$ such that for $z\in z_0+i[0,\nu_1]$,
$h<h_0$ and $u\in\bar H^{\mathbf o}_h$ with $P_{h,z}u\in\bar H^{\mathbf o'}_h$, with $\delta :=
\delta_\Gamma(\mathrm{Im}(z/h)-\epsilon)$,
$$\|u\|_{\bar H^{\mathbf o}_h}\le Ch^{-1-\delta}\|P_{h,z}u\|_{\bar H^{\mathbf o'}_h}.\tag{8.1}$$
(b) For $\nu\ge\nu_1$, (8.1) holds for $z\in z_0+i[\nu_1,\nu]$ with $\delta = 0$. (c) In the setting of Theorem 1.3 (2),
(8.1) holds with $\delta = 0$.

*Proof.* By Lemma 3.1 (applied to $\psi u$, and on the slab by I.A Lemma 6.1) it suffices to take $u$ smooth up to
$\partial_\sharp X$ and Schwartz at $\partial X$, the constants being independent of the approximation.

(a) *The cover.* Let $K_\Sigma := \Sigma_{z_0}\cap\{r\ge b'_1\}\subset\mathcal P$, compact. Each $\varpi\in K_\Sigma$ is
of one of the following kinds, by (H8), (H4) at fibre infinity and I.A Lemma 4.5 over $\partial X$.
(R) $\varpi\in\partial\mathcal R_+\cup\partial\mathcal R_-\cup R_{z_0,\mathrm{in}}$: Propositions 5.2 and 5.3 give a
neighbourhood $U_\varpi$ and $\|B_*u\|_{\mathbf o}\le C(h^{-1}\|GPu\|_{\mathbf o'}+h^N\|Gu\|_{\mathbf o}+\|u\|_{-K\mathbf
1})$ for $B_*$ microsupported in $U_\varpi$, with no a priori term; here $s>\frac12+\vartheta_{\mathcal H}$ and $\mathsf
r+\alpha_+>\frac12(-1+\vartheta_{\mathrm{in}})$ at $R_{z_0,\mathrm{in}}$ are used.
(A) $\varpi$ is not of kind (R), not in $\Gamma_u$ and not $R_{\mathrm{out}}$: its backward curve tends to a set of kind
(R) (H8), so after finite time enters a neighbourhood $U_*$ given by (R); on the segment, $\mathsf H_{z_0}\ne0$, $\hat
q_{z_0}\ne0$ (Lemma 1.1 (e), and section 4.2 over $\partial X$ away from $R_{\mathrm{out}}$), and (4.4) holds by
admissibility. Corollary 4.6 gives an estimate at $\varpi$ with a priori term on a compact subset of $U_*$, which (R)
bounds.
(Γ) $\varpi\in\Gamma$: Theorem 6.8 (with $\beta := \frac12\gamma_-<0$, so that $\mathrm{Im}\,z\ge0\ge h\beta$) gives an
estimate near $\Gamma$ with loss $h^{-1-\delta}$ and a priori term $h^{-\delta}\|Eu\|$, $E$ microsupported off $\Gamma_u$
near $\Gamma$; the points of $\mathrm{WF}'_h(E)$ are of kind (A) or elliptic.
(U) $\varpi\in\Gamma_u\setminus\Gamma$: its backward curve tends to $\Gamma$ (D2), so Corollary 4.6 from a neighbourhood
given by (Γ).
(O) $\varpi = R_{\mathrm{out}}$: Proposition 5.5 with a priori term on a compact $K_E\subset\bar U_0\setminus
R_{\mathrm{out}}$, whose points are of kinds (A), (U) or elliptic (a backward curve from near $R_{\mathrm{out}}$ leaves
every small neighbourhood of it, $R_{\mathrm{out}}$ being a sink); here $\mathsf
r+\alpha_+<-\frac12+\frac12\inf\lambda_{\min}(S+S^{*h})$ is used.
Each kind is used only after the kinds its a priori terms need, and the order (R), (A), (Γ), (U), (O) is acyclic. By
compactness, finitely many of these neighbourhoods cover $K_\Sigma$, and each estimate holds for $z$ in a neighbourhood
of $z_0$ (Corollary 4.6; Propositions 5.2, 5.3, 5.5 for all $z$ in the sets stated; Theorem 6.8 for $z\in
z_0+i[h\beta,\nu']$). The complement in $\mathcal P|_{\{r\ge b'_1\}}$ of the union of the neighbourhoods is compact and
elliptic for $P_{h,z_0}$, hence for $P_{h,z}$, $|z-z_0|$ small (Proposition 4.2). Take $\nu_1$ so small that all of this
holds for $z\in z_0+i[0,\nu_1]$. A microlocal partition of unity $\sum_jB_j = I$ over $\{r\ge b'_1\}$, modulo a residual
operator, subordinate to the cover, and the chain of estimates give, with $\delta\le1$ and $h^{-\delta}\cdot h^{-1}\le
h^{-1-\delta}$,
$$\|\psi u\|_{H^{\mathbf o}_h}\le C\big(h^{-1-\delta}\|Pu\|_{\bar H^{\mathbf o'}_h}+h^N\|u\|_{\bar H^{\mathbf
o}_h}+\|u\|_{\bar H^{-K\mathbf 1}_h}\big).$$
*The artificial boundary.* By (7.2), $\|\chi u\|_{\bar H^{\mathbf o}_h}\le C(h^{-1}\|Pu\|_{\bar H^{\mathbf
o'}_h}+\|\chi_1u\|_{H^{\mathbf o}_h})$, the orders being constant there apart from $s$;
$\mathrm{supp}\,\chi_1\subset\{b'<r<b''\}$, where $\psi = 1$, so the last term is bounded by the previous display.
*Absorption.* $\|u\|_{\bar H^{-K\mathbf 1}_h}\le Ch\|u\|_{\bar H^{\mathbf o}_h}$ for $K\ge\max(-s,-\min(\mathsf
r+\alpha_+),1-\min\mathsf b)$, since $w_{-K\mathbf 1}/w_{\mathbf o}\le Ch$; so for $h<h_0$ the last two terms are
absorbed, which is (8.1).

(b) For $\mathrm{Im}\,z\ge\nu_1$, $P_{h,z}$ is elliptic at finite frequencies over $\tilde X^\circ$ (Lemma 1.1 (d)) and
over $\partial X$ except at $R_{\mathrm{out}}$ (section 4.1), uniformly for $\mathrm{Im}\,z\in[\nu_1,\nu]$ by
compactness. The characteristic set over $\{r\ge b'_1\}$ is $\partial\Sigma_0\cup R_{\mathrm{out}}$. On
$\partial\Sigma_0$, kinds (R) at $\partial\mathcal R_\pm$ and (A) along the curves of (H4); at $R_{\mathrm{out}}$, kind
(O), whose a priori set $K_E$ is now elliptic. No trapping estimate enters, so $\delta = 0$.

(c) The same as (b), with $\mathrm{Re}\,z$ varying in $[-2,2]$: at fibre infinity $\mathsf H_z$ does not depend on $z$,
$\mathsf b$ is constant, and only the constancy of $\mathsf r$ near $R_{\mathrm{out}}$ and the threshold there are used.
$\square$

### 8.3 The adjoint estimate

**Proposition 8.2.** In the settings of Proposition 8.1, for $v\in\dot H^{-\mathbf o'}_h$ with $P^{*h}_{h,z}v\in\dot
H^{-\mathbf o}_h$,
$$\|v\|_{\dot H^{-\mathbf o'}_h}\le Ch^{-1-\delta}\|P^{*h}_{h,z}v\|_{\dot H^{-\mathbf o}_h}.\tag{8.2}$$

*Proof.* The same argument for $\epsilon_\flat = -1$: estimates propagate along the past field. The kinds without a
priori term are now $R_{\mathrm{out}}$ (the adjoint half of Proposition 5.5, above threshold at the order $-\mathsf
r-\alpha_+-1$) and the artificial boundary ((7.3), with nothing on the right but $P^{*h}v$); $\Gamma$ is handled by
Theorem 6.8 for $P^*$, with a priori term off $\Gamma^\natural_u = \Gamma_s$; $\partial\mathcal R_\pm$ and
$R_{z_0,\mathrm{in}}$ are sinks for the past field, handled by (5.5) and Proposition 5.3 with a priori terms on punctured
neighbourhoods. By (H8), the forward (future) curve of a characteristic point not on $\Gamma_s$ tends to
$R_{\mathrm{out}}$ or reaches $\{r<r_0-\delta_0\}$, and at fibre infinity reaches $\{r<r_0-\delta_0\}$ (H4); so the
chains start at the sets without a priori term. The orders $-\mathbf o'$ satisfy the reversed monotonicity, $-\mathsf r$
and $-\mathsf b$ being non-increasing along the past field. Near $\partial_\sharp X$, $v$ restricted to
$\Omega_{r_0,b''}$ is bounded by (7.3); beyond, the microlocal estimates apply to $(1-\chi)v$, whose commutator term
$[P^{*h},\chi]v$ is supported where (7.3) already bounds $v$. $\square$

*Proof of Theorem 1.3 (1) and (2).* By Propositions 8.1 and 8.2, as $\delta_\Gamma\le1$. For
$\mathrm{Im}\,z\in[\nu_1,\nu]$ and in (2) the loss is $h^{-1}$.

### 8.4 Invertibility

*Proof of Theorem 1.3 (3).* Let $\sigma$ with $\mathrm{Im}\,\sigma\ge0$ and $|\sigma|\ge C_0$. If
$\mathrm{Im}\,\sigma\ge\nu'|\sigma|$, put $h := |\sigma|^{-1}$ and $z := h\sigma$, so $|z| = 1$ and
$\mathrm{Im}\,z\ge\nu'$ (part (2)). Otherwise $|\mathrm{Re}\,\sigma|\ge|\sigma|\sqrt{1-\nu'^2}$ and
$\mathrm{Im}\,\sigma<\nu'|\sigma|\le2\nu'|\mathrm{Re}\,\sigma|$; put $h := |\mathrm{Re}\,\sigma|^{-1}$, $z := h\sigma\in
z_0+i[0,2\nu']$ with $z_0 = \mathrm{sgn}\,\mathrm{Re}\,\sigma$ (part (1) with $\nu := 2\nu'$). In both cases $h<h_0$ for
$C_0$ large. At this fixed $h$, $H^{\mathbf o}_h$ is the space $H^{s,(\mathsf r+\alpha_+)_h}$ of I.A with $\mathsf
r_h(x,\xi) := \mathsf r(x,h\xi)$, up to an equivalent norm (section 2.3; $h^{-\mathsf b(x,h\xi)}$ is a symbol of order 0
at fixed $h$), and $\mathsf r_h$ is admissible for $\mathrm{Re}\,\sigma$ in the sense of I.A (O2)-(O3): the
characteristic set over $\partial X$ at $\sigma$ in the variable $\xi$ is that at $z$ in $\zeta = h\xi$, and section 1.4
asks more than (O2). So $\mathcal X_\sigma$ and $\mathcal Y_\sigma$ of I.A Theorem 7.2 are the spaces of (1.6), and (1.6)
shows that $\hat P(\sigma) = h^{-2}P_{h,z}$ is injective on $\mathcal X_\sigma$ and $\hat P(\sigma)^{*h}$ injective on
$\mathcal Y_\sigma^*$. By I.A Theorem 7.2 (3), $\hat P(\sigma)$ is Fredholm, so it is invertible. $\square$

### 8.5 b-regularity

*Proof of Theorem 1.3 (4).* By the equivalence after (5.9), (1.7) is
$$\|u\|_{\mathbf o;k}\le Ch^{-1-\delta}\|P_{h,z}u\|_{\mathbf o';k}\tag{8.3}$$
for $\mathbf o$ and $\mathbf o'$ read on $\bar X$ (the norm (5.9) with $\bar H$ in place of $H$). Induction on $k$; $k =
0$ is (8.1). Let $k\ge1$. (i) Over $\{r\le b''\}$, the $V$'s are smooth vector fields spanning $T\tilde X$ (there $r>0$),
so $\|\chi u\|_{\mathbf o;k}$ is equivalent to $\|\chi u\|_{\bar H^{\mathbf o+(k,0,0)}_h}$, and (7.2) at regularity $s+k$
bounds it by $h^{-1}\|Pu\|_{\bar H^{\mathbf o'+(k,0,0)}_h}+\|\chi_1u\|_{H^{\mathbf o+(k,0,0)}_h}$, the first term being
at most $Ch^{-1}\|Pu\|_{\mathbf o';k}$. (ii) Away from $R_{\mathrm{out}}$ and the zero section: the symbols of the $hV_j$
are $\rho^{-1}$ times the components of $\zeta$ in a frame (I.A Lemma 4.4), so $\sum_{|\alpha| =
k}((hV)^\alpha)^*(hV)^\alpha$ is elliptic of order $2k(1,1,0)$ wherever $|\zeta|\ge c>0$, including fibre infinity; there
$\|Bu\|_{\mathbf o;k}$ and $\|Bu\|_{\mathbf o+k(1,1,0)}$ bound each other modulo $\|\tilde Bu\|_{\mathbf
o;k-1}+\|u\|_{-K\mathbf 1}$, by Proposition 2.10. At the zero section over $\tilde X^\circ$, $G_z(x,0) = z^2g_{00}\ne0$,
so $P$ is elliptic there, and every order is controlled by $\|Pu\|$ (Proposition 4.2); at finite frequencies over a
compact set all orders are equivalent. (iii) So the chain of section 8.2 at the shifted order $\mathbf o_k := \mathbf
o+k(1,1,0)$ bounds $u$ microlocally on the cover except near $R_{\mathrm{out}}$, with $\|GPu\|_{\mathbf o_k-\mathbf
m+(1,1,0)}\le C(\|Pu\|_{\mathbf o';k}+\|u\|_{-K\mathbf 1})$ for the $G$ that occur (all microsupported where (ii)
applies). $\mathbf o_k$ satisfies every condition the chain uses away from $R_{\mathrm{out}}$:
$s+k>\frac12+\vartheta_{\mathcal H}$, $\mathsf r+\alpha_++k$ is above the threshold at $R_{z_0,\mathrm{in}}$, and the
monotonicity is unchanged by adding constants. (iv) Near $R_{\mathrm{out}}$, Proposition 5.7, whose term
$\|E'u\|_{\mathbf o+k(1,1,0)}$ is supported on $K_E$, bounded by (iii). (v) The error terms $h^N\|Gu\|_{\mathbf o_k}$ and
$h^N\|Gu\|_{\mathbf o;k}$ are bounded by $h^N\|u\|_{\mathbf o;k}$ and $h^N\|Pu\|$ by (ii), and absorbed for $h$ small;
the terms $\|\tilde Bu\|_{\mathbf o;k-1}$ are bounded by the induction hypothesis. This gives (8.3), uniformly in the
settings of (1) and (2). $\square$

### 8.6 Regularity in the spectral parameter

*Proof of Theorem 1.3 (5).* For $\sigma$ as in (3), $\hat P(\sigma)^{-1}$ is $C^\infty$ in $\sigma$ as a map between the
spaces of I.A Theorem 7.2 (6) (holomorphic for $\mathrm{Im}\,\sigma>0$), and on the overlaps the inverses at different
admissible orders agree, kernels and cokernels being trivial for all of them. So $\partial_\sigma\hat P^{-1} = -\hat
P^{-1}(\partial_\sigma\hat P)\hat P^{-1}$, and $(\sigma\partial_\sigma)^j\hat P^{-1}$ is a sum, with integer
coefficients, of products
$$\hat P^{-1}\,\mathcal T_{i_1}\,\hat P^{-1}\cdots\mathcal T_{i_l}\,\hat P^{-1},\qquad\mathcal T_i :=
(\sigma\partial_\sigma)^i\hat P(\sigma) = \sigma T+2^i\sigma^2g_{00},\quad i_1+\dots+i_l = j,\ 1\le l\le j.\tag{8.4}$$
By (H2), $\sigma T = 2i\sigma\rho(V_1-\frac32-S)-i\sigma Q$, so $\mathcal T_i = \sigma\rho\,\mathcal
V+\sigma\rho\,c+\sigma\rho^3\mathrm{Diff}^1_b+2^i\sigma^2g_{00}$ with $\mathcal V = 2iV_1$ and $c$ a matrix function.
Write $\|\cdot\|_{(s;k),\mathsf r;+}$ for (1.5) at decay order $\mathsf r$ (and $\mathsf b$ fixed), so that
$\|u\|_{(s;k),\mathsf r;+}\asymp h^{-k}\|u\|_{(s,\mathsf r,\mathsf b);k}$, $h := |\sigma|^{-1}$. Then:
(a) $\mathcal T_i$ maps $(s';k'+1),\mathsf r'$ to $(s';k'),\mathsf r'+1$ with norm $\le C|\sigma|$, for all $s',k'$ and
decay orders $\mathsf r'$: with $\sigma = zh^{-1}$, $\sigma\rho V_1 = h^{-2}z\,\rho\,(hV_1)$, and
$\|h^{-2}\rho(hV_1)u\|_{(s',\mathsf r'+1,\mathsf b);k'}\le Ch^{-2}\|u\|_{(s',\mathsf r',\mathsf b);k'+1}$ ($hV_1$ is one
of the module operators of (5.9), and $\rho$ raises the decay order by 1), so the norm is $h^{-k'}h^{-2}h^{k'+1} =
h^{-1}$; the other terms are smaller or equal: $\sigma\rho c$ and $\sigma\rho^3\mathrm{Diff}^1_b$ likewise, and
$\sigma^2g_{00} = h^{-2}z^2g_{00}$ with $g_{00}\in\rho^2C^\infty$ raises the decay order by 2 and costs $h^{-2}$ from
$(s';k')$, which is $h^{-1}$ from $(s';k'+1)$ as $\|\cdot\|_{(s';k'+1);+}\ge h^{-1}\|\cdot\|_{(s';k');+}$.
(b) $\hat P(\sigma)^{-1} = h^2P_{h,z}^{-1}$ maps $(s'-1;k'),\mathsf r+\alpha_++1$ to $(s';k'),\mathsf r+\alpha_+$ with
norm $\le C|\sigma|^{-1+\delta}$, for every $s'\ge s$ and $k'$, by (8.3) ($s'$ is admissible since
$s'>\frac12+\vartheta_{\mathcal H}$).
(c) $(s';k'+1);+$ embeds in $(s'+1;k');+$ with norm $\le C$: at fibre infinity the module operators are elliptic of order
$(1,1,0)$ (as in 8.5 (ii)), which gives one order of regularity, and at finite frequencies the regularity order is
immaterial.
In a product (8.4) with $l$ factors $\mathcal T$, apply (b) $l+1$ times, at the regularity orders $s,s+1,\dots,s+l$, and
(a) $l$ times, starting from $f$ in $(s-1;k+j)$, after converting $j-l$ module orders into regularity by (c) where
needed: each $\hat P^{-1}$ raises the regularity by one, each $\mathcal T$ lowers the module order by one and leaves the
regularity, and the target $(s+j;k)$ is reached after $j-l$ uses of (c). The norm is at most
$C|\sigma|^{(l+1)(-1+\delta)+l}\le C|\sigma|^{-1+(j+1)\delta}$, as $l\le j$ and $|\sigma|\ge1$. This is (1.8). $\square$

## 9. Uniformity in the operator

Let $\hat P$ depend on $b\in\mathcal B$ as in (H5)-(H8). Every constant above depends on finitely many seminorms of the
symbols involved and on finitely many lower bounds: ellipticity constants, $\beta_*$, $c_1$ and $c_{\mathcal T}$ in Lemma
5.1, the margins in the thresholds, $c_0$ in Proposition 4.5, $\nu_{\min}$, $\beta_0$, $c_\Gamma$ and the thresholds
$\gamma_\pm$ in section 6, the lengths of the curves in the chains of section 8, and the constants of Proposition 7.1.
Each depends continuously on $b$, by (H5)-(H8), and the constructions (flow boxes by Lemma 4.3 with $b$ among the
parameters; the commutants; the absorbing operator of section 6.5, with $\Gamma(\delta)$ defined through $\phi_{u/s}$,
which depend continuously on $b$) can be made with $b$ in a neighbourhood of each $b_0$; by compactness of $\mathcal B$,
finitely many suffice. The two arguments by contradiction (Proposition 6.4 and the absorption in Proposition 6.7 (a)) are
run with sequences $(h_j,z_j,b_j)$, $b_j\to b_\infty$ after passing to a subsequence: the defect measure is then that of
the limit operator, Lemma 6.3 holds with the limit symbols, and the dynamics (D1)-(D3) of $b_\infty$ give the
contradiction. Hence Theorem 1.3 holds with constants uniform in $b\in\mathcal B$. As in I.A section 8, Part VI checks
(H5)-(H8) for the record's operators; it is not done here.

## 10. What the write-out found

(F1) [Hin26c] Theorem 9.28 states that $B$ is semiclassically elliptic "at $\partial\mathcal R_+$"; the estimate is at
the trapped set, and $B$ is elliptic at $\Gamma$ (Theorem 6.8). A slip of the pen.

(F2) In the proof of [Hin26c] (9.83) the constant is fixed in $(\inf_\Gamma p_1/(2\beta_0),\gamma)$; positivity of
$-2p_1+4\beta_0\gamma_0$ on $\Gamma$ needs $\gamma_0>\sup_\Gamma p_1/(2\beta_0) = \gamma_+$. Proposition 6.1 avoids the
constant by writing $p-\lambda q = (p-\gamma q)-(\lambda-\gamma)q$.

(F3) The proof of [Hin26c] Theorem 9.28 with loss 1 takes $-\beta\le h^{-1}\mathrm{Im}\,z$ and $p_z\le
p_1+2\beta\beta_0$, while the theorem is stated for $\mathrm{Im}(h^{-1}z)\ge\beta$, $\beta>\gamma_-$. With the stated
range the bound is $p_\eta\le\lambda_{\max}(p^\natural-\beta q^\natural)$ (Proposition 6.4); the two readings agree for
$\beta\le0$ only when $q$ is constant on $\Gamma$.

(F4) $\gamma_-$ in [Hin26c] (9.80) divides by $2\beta_0 = \min_\Gamma q$. For $\mathrm{Im}\,\sigma<0$, which the
interpolation of [Hin26c] Lemma 9.33 uses on its lower line, $-\eta q\le|\eta|\max_\Gamma q$, so Steps 1 and 3 of the
loss-1 proof need $\sup_\Gamma\lambda_{\max}(p_1-\eta q)<\frac12\nu_{\min}$, which follows from the printed condition
only if $q$ is constant on $\Gamma$ (as for a static spherically symmetric metric, with $\Gamma$ at one radius). Theorem
1.3 therefore defines $\gamma_\pm$ as the exact thresholds (1.4); they agree with [Hin26c] (9.80) when $q$ is constant on
$\Gamma$. Downstream only $\delta_\Gamma(0)$ small is used, which holds for either definition when $\gamma_+$ is small.

(F5) [Hin26c] Theorem 9.16 (1) asserts the $h^{-2}$ estimate for $z\in\pm1+i[0,\nu]$, while Theorem 9.28 is proved for
$\mathrm{Im}(h^{-1}z)\ge\beta>\gamma_-$; at $\mathrm{Im}\,z = 0$ this needs $\gamma_-<0$. [Hin26c] notes that
$\gamma_-<0$ in its applications. Here $\gamma_-<0$ is part of (H7); Part VI must check it.

(F6) [Hin26c]'s step 2 of the b-regular estimate at $R_{\mathrm{out}}$ ((9.77)) again carries the diagonal term
$-2kihz\rho\delta_{\alpha,(k,0,\dots,0)}$ of (9.45), whose sign and index set I.A Lemma 4.8 corrected (D184). Lemma 5.6
moves the term to the right side through $Pu$, as I.A Lemma 4.8 does at fixed $\sigma$; Proposition 5.7 then needs no
sign of it.

(F7) The semiclassical scattering calculus with matrix-valued symbols and variable orders could not be READ (section 2);
it is proved in section 2. [Hin26c] (3.35) defines $H^{s,\mathsf r,\mathsf b}_{\mathrm{sc},h} = \rho^{\mathsf
r}h^{\mathsf b}H^s_{\mathrm{sc},h}$, which gives $\|u\| = h^{-\mathsf b}\|\langle hD\rangle^s(\langle x\rangle^{\mathsf
r}u)\|$ on $\mathbb R^n$; the parenthesis after it prints $\langle x\rangle^{-\mathsf r}u$. Part I.B uses $w_{\mathbf o}
= \langle\zeta\rangle^s\langle x\rangle^{\mathsf r}h^{-\mathsf b}$, as (3.35) does.

(F8) Changes of statement, all recorded in section 1: the regularity order is constant (I.A Remark 1.1); the orders are
required to be monotone on a neighbourhood of the characteristic set, not on it alone (section 1.4), because the weight
$\log\frac1h$ multiplies $\mathsf H\mathsf b$ on the whole support of a commutant (Proposition 4.5); and $\gamma_\pm$ are
the exact thresholds (F4) with $\gamma_-<0$ assumed (F5).

(F9) Changes of method, not of statement: one positive commutator scheme without regularisation, a priori estimates being
proved for Schwartz functions and extended by density (section 3); propagation with flow boxes depending on $z$, the
difference $\mathsf H_z-\mathsf H_{\mathrm{Re}\,z}$ absorbed by $\lambda\mathcal Q$ (Proposition 4.5), in place of
[Hin26c]'s three regimes (Propositions 9.19, 9.22, 9.23); one radial lemma for all three radial sets (Lemma 5.1); at
$R_{\mathrm{out}}$ the large imaginary part written as $W^*\tilde MW-g_{00}$, non-negative exactly (Lemma 5.4), which
needs the remainder $R_2$ of [Hin26c] (9.49) to be put into that form; matrix-valued defect measures, entering through
$\mathrm{tr}$ and $\lambda_{\max}$ (Lemma 6.2); the complex absorption written as $\hat Q_\flat(\bar\sigma)^*\hat
Q_\flat(\sigma)$, entire and of exact sign (section 6.5); a three lines lemma with its proof (Lemma 6.6) in place of
[DZ19] Lemma D.1; and the energy estimate at the artificial boundary for every $\mathrm{Im}\,z\ge0$ through the weight
$e^{\lambda r}$ (Proposition 7.1), in place of [Hin25a] Theorem 9.44 for bounded $h^{-1}\mathrm{Im}\,z$.

## Sources

[Hin26c] P. Hintz, *(Non-)linear waves on asymptotically flat spacetimes. II*, arXiv:2606.28008v1, section 9.3, read in
full in `vv/hin26c.txt` of the working notes; the statements cited are Theorem 9.16, Remark 9.17, Lemmas 9.13, 9.20,
9.21, 9.30-9.33, Propositions 9.19-9.27, 9.35, Theorem 9.28 and (9.49), (9.58)-(9.61), (9.77)-(9.83).
[HJS] A. Hassell, J. Jia, E. Sussman, arXiv:2604.18956 (READ in Part I.A).
[HV16] P. Hintz, A. Vasy, *Non-trapping estimates near normally hyperbolic trapping*, Math. Res. Lett. (2014); its
Theorem 4.7 is followed through [Hin26c]'s recollection of it, which is complete in [Hin26c].
[Dya16] S. Dyatlov, *Spectral gaps for normally hyperbolic trapping*, Ann. Inst. Fourier 66 (2016); its Lemma 2.3 and the
argument of its section 4 are followed through [Hin26c], which writes them out.
[DZ19], [Hin25a], [VZ00], [Zwo12]: cited by [Hin26c] for steps that are proved here instead (sections 2, 6.5, 7).
Part I.A: `PART-I-SPECTRAL.md`.
