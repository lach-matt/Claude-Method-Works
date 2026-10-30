# Part VI.B: the horizon near $b_0$

*Status.* Written (D316). This part carries Part VI.A's horizon hypotheses, the dynamical parts of (H3) and all of (H4),
from $b_0$ to every $b$ near $b_0$, uniformly in $b$ as (H5) asks. (H6), (K1) and the first clause of (K4) hold for
every $b\in\mathcal B$ by VI.A Lemma 1.1. The trapped set and the global dynamics near $b_0$, (Γ.1)-(Γ.3), (K3) and
(H8), are Part VI.B$'$. The one new fact used is that the Myers-Perry horizon is the null hypersurface $\{r_A = r_+\}$
of III.B's Kerr-Schild form (Lemma 1.1). It is proved here by an exact identity. The rest is continuity on compact sets,
after a diffeomorphism that fixes the horizon (Lemma 1.2).

## 1. The horizon

For $b = (\mu,A)\in\mathcal B$ let $r_A$, $P$, $\mathsf M$, $\ell_A$, $F_A$, $H_{\mu,A}$ be as in III.B Lemma 3.1 and
Definition 3.2. In a frame where $A = aJ_{12}+bJ_{34}$, $P(r) = (r^2+a^2)(r^2+b^2)$ (III.B Lemma 3.1's proof). Let
$r_+(b)$ be the largest positive root of
$$\Delta_b(r) := P(r)-\mu r^2 = 0.\tag{1.1}$$
At $b_0$, $\Delta_{b_0} = r^2(r^2-\mu_0)$, so $r_+(b_0) = \mu_0^{1/2} = r_h$. There $\partial_r\Delta_{b_0} =
2\mu_0^{3/2}\ne0$, so $r_+$ is a simple root, smooth in $b$ near $b_0$ (implicit function theorem; $P$ depends on $A$
only through $s = a^2+b^2$ and $p^2 = a^2b^2$, which are smooth functions of $A$, III.B Lemma 3.1).

**Lemma 1.1 (the horizon is null).** On $\{|x|^2>s\}$,
$$g^{\mathrm{KS}}_{\mu,A}{}^{-1}(dr_A,dr_A) = \frac{\Delta_b(r_A)}{r_A^2\,\Sigma},\qquad\Sigma :=
r_A^2+a^2\cos^2\theta+b^2\sin^2\theta>0,\tag{1.2}$$
in the spheroidal parametrisation $x = (\sqrt{r_A^2+a^2}\sin\theta\,e^{i\phi},\sqrt{r_A^2+b^2}\cos\theta\,e^{i\psi})$ of
the level sets of $r_A$. Hence $\mathcal H_b := \{r_A = r_+(b)\}$ is a smooth null hypersurface invariant under
$\partial_t$. $dr_A$ is spacelike just outside it, and timelike just inside, where $\Delta_b<0$.

*Proof.* The parametrisation satisfies $x^T(r^2I-A^2)^{-1}x = 1$, which by III.B Lemma 3.1 (a) and its proof is $Q(r,x)
= 0$, the equation of $r_A$. With $\nabla r_A = -\nabla_xQ/(2r\,\partial_yQ)$ ($y = r^2$), III.B Lemma 3.3 (d) gives
$g^{-1}(dr_A,dr_A) = |\nabla r_A|^2-H_{\mu,A}(\ell_A\cdot\nabla r_A)^2$. Substituting the parametrisation, the
difference of the two sides of (1.2) simplifies to 0 (sympy, exact, in the rotated frame; `checks/horizon5.py`). Both
sides are conjugation covariant, so (1.2) holds for every $A$. $\Delta_b$ has a simple zero at $r_+$, so $\mathcal H_b$
is a smooth level set of $r_A$ with $dr_A\ne0$, and it is null. $t$-invariance holds as $g^{\mathrm{KS}}$ has
$t$-independent components. $\square$

(1.2) is the Boyer-Lindquist component $g^{rr} = \Delta/\Sigma$ of the Myers-Perry metric, written in III.B's
coordinates; the radius $r_A$ of the Kerr-Schild form is the Boyer-Lindquist $r$.

**Lemma 1.2 (fixing the horizon).** There are $\epsilon_H>0$ and diffeomorphisms $\Psi_b$ of $\{|x|\ge\frac12R_1\}$, for
$|b-b_0|<\epsilon_H$, smooth in $(b,x)$, with $\Psi_{b_0} = \mathrm{Id}$, $\Psi_b = \mathrm{Id}$ on $\{|x|\ge2R_1\}$ and
near $\{|x| = \frac12R_1\}$, and $\Psi_b(\{|x| = r_h\}) = \mathcal H_b$.

*Proof.* Let $\chi\in C^\infty_c((\frac58R_1,\frac74R_1))$ equal 1 near $[\frac34R_1,\frac32R_1]$. This interval
contains $r_h$, as $r_h\in(R_1/\sqrt2,\sqrt{3/2}R_1)$ (III.B Proposition 3.4). Put $\tilde r_b :=
\chi(|x|)\frac{r_h}{r_+(b)}r_A(x)+(1-\chi(|x|))|x|$. Then $\tilde r_{b_0} = |x|$ (as $r_0 = |x|$, III.B Lemma 3.1 (b)),
$\tilde r_b\to|x|$ in $C^\infty$ as $b\to b_0$, and $\mathcal H_b = \{\tilde r_b = r_h\}$ near $\{|x| = r_h\}$. Define
$\Psi_b(x) := \lambda\hat x$, with $\lambda = \lambda_b(x)$ solving $\tilde r_b(\lambda\hat x) = |x|$. As
$\partial_\lambda\tilde r_b(\lambda\hat x) = 1+O(|b-b_0|)$, the implicit function theorem gives a unique smooth
$\lambda$ near $|x|$, and $\Psi_b$ is a diffeomorphism. It is the identity where $\chi = 0$, and it maps $\{|x| = r_h\}$
onto $\{\tilde r_b = r_h\} = \mathcal H_b$. $\square$

Below, $\tilde g_b := \Psi_b^*g_b$, with the time function $\Psi_b^*t_*$. $d(\Psi_b^*t_*) = \Psi_b^*dt_*$ is timelike
for $\tilde g_b$, and the spectral families of $g_b$ and $\tilde g_b$ are conjugate by $\Psi_b$. Every hypothesis of
Parts I-II is invariant under such a conjugation, which is the identity near $\partial X$. Write $\tilde G_{0,b}$,
$\tilde\tau_{1,b}$ for $\tilde g_b$'s symbols, and keep VI.A's radii, $\rho_\infty = |\xi|^{-1}$, and $\mathcal R_\pm =
\{r = r_h,\eta = 0,\pm\xi>0\}$, now fixed sets.

## 2. (H3) and (H4) near $b_0$

**Lemma 2.1.** For $|b-b_0|<\epsilon_H$, $N^*\{r = r_h\}\setminus o\subset\{\tilde G_{0,b} = 0\}$, and $H_{\tilde
G_{0,b}}$ is tangent to it.

*Proof.* $\tilde G_{0,b}(\lambda\,dr) = \lambda^2\tilde g_b^{-1}(dr,dr) = 0$ on $\{r = r_h\}$, by Lemma 1.1 transported
by $\Psi_b$ ($dr$ has no $dt$-component). So the Lagrangian submanifold $N^*\{r = r_h\}$ lies in the level set $\{\tilde
G_{0,b} = 0\}$. For $v$ tangent to it, $\omega(H_{\tilde G_{0,b}},v) = d\tilde G_{0,b}(v) = 0$, so $H_{\tilde G_{0,b}}$
lies in the symplectic orthogonal of the tangent space, which is the tangent space itself. $\square$

**Proposition 2.2 ((H3) and (H4) near $b_0$).** There is $\epsilon_1\in(0,\epsilon_H]$ such that for
$|b-b_0|<\epsilon_1$, (H3)'s dynamical conditions and (H4) hold for $\tilde g_b$ with VI.A's radii, the sets $\mathcal
R_\pm$, $\rho_\infty$, and $q_{\pm,b} := |\eta/\xi|^2_{\slashed g}$ restricted to $\partial\tilde\Sigma_{0,b}$. Moreover
$\beta_0(b)\ge\frac12\beta_0(b_0)$, $\beta(b)\ge\frac12\beta(b_0)$, $\mathsf
H_bq_{\pm,b}\ge\frac12\beta_0(b_0)q_{\pm,b}$ near $\partial\mathcal R_\pm$, and the lengths in (H4) are bounded, all
uniformly in $b$. So (H5)'s uniformity holds for these data.

*Proof.* All symbols depend smoothly on $b$ in $C^\infty$, as $\Psi_b$ does. The future-directed rescaled field is
$\mathsf H_b := \mathrm{sgn}(\xi)\rho_\infty H_{\tilde G_{0,b}}$ near $\partial\mathcal R_\pm$, whose two components are
distinguished by $\mathrm{sgn}\,\xi$ for $b$ near $b_0$ by continuity.

*(H3).* By Lemma 2.1, $\partial\mathcal R_\pm$ are invariant compact sets for every $b$. $\beta_0(b) =
\rho_\infty^{-1}\mathsf H_b\rho_\infty$ and $\mp\beta_0^{-1}\rho_\infty\tilde\tau_{1,b}$ are continuous functions on the
fixed compact $\partial\mathcal R_\pm$, continuous in $b$, and their infima at $b_0$ are $2\mu_0^{-1/2}$ and
$\mu_0^{1/2}$ (VI.A Proposition 2.1). So they are at least half of that for $b$ near $b_0$. Next, $d\tilde G_{0,b}\ne0$
at $\partial\mathcal R_\pm$ (at $b_0$, $\partial_r(f\xi^2)\ne0$ there), so near $\partial\mathcal R_\pm$,
$\partial\tilde\Sigma_{0,b}$ is a smooth hypersurface of $S^*\tilde X$, a graph $r = r_b(\omega,\hat\eta)$ over the
coordinates $(\omega,\hat\eta := \eta/\xi)$, smooth in $b$ (implicit function theorem). In these coordinates
$\partial\mathcal R_\pm = \{\hat\eta = 0\}$ for every $b$, and $q_{\pm,b} = |\hat\eta|^2$ is a quadratic defining
function. $\mathsf H_b$ is tangent to $\{\hat\eta = 0\}$, so $\mathsf H_bq_{\pm,b} =
Q_b(\omega)(\hat\eta,\hat\eta)+O(|\hat\eta|^3)$, with the quadratic form $Q_b$ continuous in $b$ and the remainder
uniform. At $b_0$, $Q_{b_0} = 2\beta_0(b_0)|\hat\eta|^2$ (VI.A (2.1)ff.: $\mathsf Hq = 2q(f'-2r^{-3}q)$). So
$Q_b\ge\frac32\beta_0(b_0)|\hat\eta|^2$ for $b$ near $b_0$, and $\mathsf H_bq_{\pm,b}\ge\frac12\beta_0(b_0)q_{\pm,b}$ on
$\{q_{\pm,b}<\epsilon_q\}$ for a fixed $\epsilon_q>0$.

*(H4).* At $b_0$, $\partial\Sigma_0$ lies over $\{r\le r_h\}$, and $\tilde G_{0,b_0}\ge c>0$ on
$S^*\{r_h+\frac12\delta_0\le r\le\rho_1^{-1}\}$. Near $\partial X$, (H2) gives $G_0 =
\rho^2(\xi_b^2+|\eta_b|^2)(1+O(\rho))$ uniformly in $b$ (III.B (3.5)). So for $b$ near $b_0$,
$\partial\tilde\Sigma_{0,b}$ lies over $\{r<r_h+\frac12\delta_0\}\subset\{r\le r_e\}$. On $\{r_0-2\delta_0\le r\le
r_2\}$ the conditions "$\tilde G_{0,b}$ Lorentzian of signature $(1,3)$", "$\tilde G_{0,b}(dr)<0$" and "$\mathsf H_br<0$
on $\partial\tilde\Sigma_{0,b}$" are strict and hold at $b_0$ on a compact set, so they persist. For the flow, let $U :=
\{q_{\pm,b}<\epsilon_q\}$ near $\partial\mathcal R_\pm$. At $b_0$, $\partial\Sigma_0\setminus U$ lies over $\{r\le
r_h-\kappa\}$ for some $\kappa>0$ ($q = -fr^2$ there), where $\mathsf Hr = 2f\le-c'$. By continuity, for $b$ near $b_0$,
$\partial\tilde\Sigma_{0,b}\setminus U$ lies over $\{r\le r_h-\frac\kappa2\}$, where $\mathsf H_br\le-\frac{c'}2$. Let
$\gamma$ be a maximal curve of $\mathsf H_b$ in $\partial\tilde\Sigma_{0,b}\setminus\partial\mathcal R_\pm$. In $U$,
$q_{\pm,b}$ grows forward at the rate $\ge\frac12\beta_0(b_0)$, so $\gamma$ leaves $U$ forward in finite time. Outside
$U$, $r$ decreases at the rate $\ge\frac{c'}2$, so $\gamma$ never re-enters $U$, as that would need $r\ge
r_h-\frac\kappa2-o(1)$ after $r$ fell below the exit value. It reaches $\{r<r_0-\delta_0\}$ in finite time. Backward,
$r$ increases outside $U$, so $\gamma$ enters $U$ in finite time. In $U$, $q_{\pm,b}$ decreases exponentially backward,
so $\gamma(s)\to\partial\mathcal R_\pm$ as $s\to-\infty$. The times are bounded uniformly in $b$ on compact sets of
initial points away from $\partial\mathcal R_\pm$. $\square$

## 3. Findings, labels and sources

(VI.B1) *The horizon is computed in the write-out's own coordinates.* The record took the Myers-Perry horizon from
[ER08]'s Boyer-Lindquist form. Here (1.2) is proved in III.B's Kerr-Schild coordinates, where Parts III-IV work, so no
change of coordinates is read.

(VI.B2) *The radial set at $b\ne b_0$ is the conormal of a moving horizon.* (H3) is stated for $\mathcal H = \{r =
r_h\}$, and I.A's $r$ is $|x|$. The diffeomorphism $\Psi_b$ of Lemma 1.2 makes this literal: it is the identity outside
$\{|x|<2R_1\}$, so (H1)-(H2) and the structure at infinity are unchanged. (H5) already allows $\mathcal H$ to depend on
$b$, and this is how it does.

*Labels.* Lemma 1.1: [Hin26c] section 9.2.1's horizon, for Myers-Perry; Proposition 2.2: (H3)-(H4) near $b_0$, [Hin26]
Remark 1.4 (b)'s "non-degenerate source at the conormal bundle of the event horizon".

*Sources.* No new reading. Inputs: III.B Lemma 3.1, Definition 3.2, Lemma 3.3 (d), Propositions 3.4, 3.6, (3.5); VI.A
Lemma 1.1, Proposition 2.1 and (2.1); I.A (H2)-(H5).
