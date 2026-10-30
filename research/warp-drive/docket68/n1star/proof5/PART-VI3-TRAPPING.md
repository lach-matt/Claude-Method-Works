# Part VI.B$'$: the trapped set and the global dynamics near $b_0$

*Status.* Written (D319); verified (D321: verifier 139's minor finding and thirteen notes repaired). This part proves
the remaining dynamical hypotheses for $g_b$, $b$ near $b_0$: the normally hyperbolic trapping (Γ.1)-(Γ.3) of (H7),
$r$-normal hyperbolicity (K3) with the uniformity (K4), and the global dynamics (H8), with the uniformity (H5) extended
to them (I.B section 1.5). With Part VI.A ((H6), (K1), and (Dyn) at $b_0$) and Part VI.B ((H3)-(H4) near $b_0$) this
completes (Dyn) near $b_0$ (Theorem 5.1). The tool is the separability of the null geodesic flow of five-dimensional
Myers-Perry. It holds in III.B's own Kerr-Schild coordinates, written in spheroidal form, with the Kerr-Schild time:
$\varrho^2g_b^{-1}$ is a function of the radial variables plus a function of the angular ones (Lemma 0.1). This plays
the part of Carter's constant in [Hin26c] section 4.2.3. It gives the trapped set and its stable and unstable
hypersurfaces in closed form, smooth in $b$, which a perturbation argument would give only with finite regularity
(finding (VI.B$'$2)). Every object is defined without choosing an eigenframe of $A$ (finding (VI.B$'$4)).
`checks/trap5.py` verifies the identities.

*Notation.* Some letters have two uses, kept apart by context: $b$ is the parameter and, in a frame, the second spin;
$\Psi$ is a momentum in a frame and $\Psi_b$ is VI.B's diffeomorphism; $F$ is the function of Lemma 3.1, the momentum
map in the proof of Lemma 3.2 and, in section 4, the shift $t-t_*$; $\Lambda$ is the invariant of section 1 and
$\Lambda_s$ a multiplier in Proposition 3.4; $\lambda$ is the positive factor of Lemma 3.3 and Proposition 3.4, and
$\lambda_b$ the scaling in $\iota_b$; $\beta$ is the coefficient of Lemma 0.1 (c) and $\beta_0$ the rate of (H3).

## 0. Spheroidal coordinates and the separation

Let $b = (\mu,A)$ with $|b-b_0|$ small, and use III.B's notation: $s = -\frac12\mathrm{tr}(A^2)$, $P(r) = r^4+sr^2+p^2$,
$\Delta_b = P-\mu r^2$, $r_A$, $\ell_A$, $H_{\mu,A}$ (III.B Lemma 3.1, Definition 3.2), $r_+(b)$ the largest root of
$\Delta_b$ (VI.B (1.1)). On $\{|x|\ge\frac12R_1\}$ write

$$x = (r^2I-A^2)^{1/2}\omega,\qquad r>0,\ \omega\in\mathbb S^3\subset\mathbb R^4.\tag{0.1}$$

As $x^T(r^2I-A^2)^{-1}x = |\omega|^2$, (0.1) is the equation $Q(r,x) = 0$ of $r_A$ (III.B Lemma 3.1 (a)), so $r =
r_A(x)$, and (0.1) is a diffeomorphism $(r,\omega)\mapsto x$, smooth in $A$, with no frame chosen. Since $\langle\omega,
d\omega\rangle = 0$ and $(r^2I-A^2)^{-1} = \mathsf M/P$ (III.B Lemma 3.1 (a)),
$$|dx|^2 = \frac{r^2\varrho^2}P\,dr^2+\langle(r^2I-A^2)\,d\omega,d\omega\rangle,\qquad\varrho^2 :=
r^2+s+\omega^TA^2\omega,$$
which is VI.B's $\varrho^2$. Write a covector as $\nu = -E\,dt+p_r\,dr+\eta$, $\eta\in T^*_\omega\mathbb S^3$, with $t$
the Kerr-Schild time, $|\eta|^2_{\mathbb S^3}$ its round norm and $|\eta|^2_{e,r}$ its norm for the second term of
$|dx|^2$. Put $Y_r := (r^2I-A^2)^{-1}A$ (antisymmetric, so $Y_r\omega\in T_\omega\mathbb S^3$), $\tilde E := E+\eta(Y_r
\omega)$, $\mathcal T := |\eta|^2_{\mathbb S^3}-\varrho^2|\eta|^2_{e,r}$, and

$$\mathfrak A := \frac P{r^2}p_r^2-r^2E^2-\mathcal T-\mu\big(\tilde E+p_r\big)^2,\qquad
\mathcal K := |\eta|^2_{\mathbb S^3}-(s+\omega^TA^2\omega)E^2.\tag{0.2}$$

*A frame.* Rotating, $A = aJ_{12}+bJ_{34}$ with $J_{12} = e_1e_2^T-e_2e_1^T$, $J_{34} = e_3e_4^T-e_4e_3^T$, and $\omega
= (\sin\theta\,e^{i\phi},\cos\theta\,e^{i\psi})$. Put $\Phi := \eta(J_{12}\omega)$, $\Psi := \eta(J_{34}\omega)$, the
generators of the two rotations (minus the momenta conjugate to $\phi$, $\psi$). Then $\varrho^2 = r^2+a^2\cos^2\theta+
b^2\sin^2\theta$ and
$$\mathcal K = p_\theta^2+\frac{\Phi^2}{\sin^2\theta}+\frac{\Psi^2}{\cos^2\theta}-(a^2\cos^2\theta+b^2\sin^2\theta)E^2,
\qquad\eta(Y_r\omega) = \frac{a\Phi}{r^2+a^2}+\frac{b\Psi}{r^2+b^2},$$
$$\mathcal T = (a^2-b^2)\Big(\frac{\Phi^2}{r^2+a^2}-\frac{\Psi^2}{r^2+b^2}\Big).\tag{0.3}$$
So $\mathfrak A$ depends on $(r,p_r,E,\Phi,\Psi)$ only, and $\mathcal K$ on $(\theta,p_\theta,E,\Phi,\Psi)$ only. The
frame is used only to compute; every statement below is about the frame-free functions (0.2).

**Lemma 0.1 (separation).** On $T^*(\mathbb R_t\times\{|x|\ge\frac12R_1\})$, with $\mathcal G := \mathfrak A+\mathcal
K$:

(a) $\varrho^2g_b^{-1}(\nu,\nu) = \mathcal G$.

(b) $E$, $\mathcal K$ and, in any frame, $\Phi$ and $\Psi$ are constant along the flow of $H_{\mathcal G}$, and they
Poisson-commute with each other.

(c) $\mathfrak A = \alpha p_r^2+2\beta p_r+\gamma$ with $\alpha := \Delta_b/r^2$, $\beta := -\mu\tilde E$, $\gamma :=
-r^2E^2-\mathcal T-\mu\tilde E^2$. With $\tilde p := \alpha p_r+\beta$ and the *radial function* $\mathcal R := \beta^2-
\alpha(\gamma+\mathcal K)$, $\alpha\,\mathcal G = \tilde p^2-\mathcal R$.

(d) $H_{\mathcal G}r = 2\tilde p$ and $H_{\mathcal G}\tilde p = \partial_r\mathcal R+(\alpha'/\alpha)(\tilde p^2-
\mathcal R)$, where $\partial_r$ is taken at fixed $(\omega,\eta)$. In a frame, $\mathcal R$, $\alpha$, $\beta$, $\tilde
p$ depend on $(\omega,\eta)$ only through $(\Phi,\Psi,\mathcal K)$, and $H_{\mathcal G}f = 0$ for every function $f$ of
$(E,\Phi,\Psi,\mathcal K)$.

*Proof.* (a) By III.B Lemma 3.3 (d), $g_b^{-1} = \eta_{\mathrm{Mink}}^{-1}-H_{\mu,A}k_A^\sharp\otimes k_A^\sharp$ with
$k_A^\sharp = -\partial_t+\ell_A^\sharp$. From $|dx|^2$, $\eta_{\mathrm{Mink}}^{-1}(\nu,\nu) = -E^2+\frac
P{r^2\varrho^2}p_r^2+|\eta|^2_{e,r}$. As $\partial_rx = r(r^2I-A^2)^{-1}x$ and $\ell_A = (r^2I-A^2)^{-1}(rI+A)x\cdot
dx$, $\nu(k_A^\sharp) = E+p_r+\zeta((r^2I-A^2)^{-1}Ax) = E+p_r+\eta(Y_r\omega)$, where $\zeta$ is the spatial part of
$\nu$ and the vector $(r^2I-A^2)^{-1}Ax = (r^2I-A^2)^{1/2}Y_r\omega$ is the image of $Y_r \omega$ under (0.1) at fixed
$r$. In a frame, $F_A = 1-\frac{a^2\sin^2\theta}{r^2+a^2}-\frac{b^2\cos^2\theta}{r^2+b^2} = r^2\varrho^2/P$ (III.B
Definition 3.2, with $\mathsf M/P = (r^2I-A^2)^{-1}$), so $H_{\mu,A} = \mu/\varrho^2$; both sides are
conjugation-covariant, so this holds for every $A$. Hence $\varrho^2g_b^{-1}(\nu,\nu) = \frac
P{r^2}p_r^2-\varrho^2E^2+\varrho^2|\eta|^2_{e,r}-\mu(\tilde E+p_r)^2$, and $\varrho^2E^2 = r^2E^2+(s+\omega^TA^2
\omega)E^2$ and $\varrho^2|\eta|^2_{e,r} = |\eta|^2_{\mathbb S^3}-\mathcal T$ give (a). In a frame, the dual of
$\varrho^2\big(\varrho^2d\theta^2+(r^2+a^2)\sin^2\theta\,d\phi^2+(r^2+b^2)\cos^2\theta\,d\psi^2\big)^{-1}$ with
$\varrho^2 = r^2+a^2-(a^2-b^2)\sin^2\theta = r^2+b^2+(a^2-b^2)\cos^2\theta$ gives (0.3). `checks/trap5.py` S1 checks (a)
and (0.3) against III.B's Cartesian formulas to 40 digits at random points. (b) $E$ is the momentum of the Killing field
$\partial_t$. In a frame, the coordinates $(t,r,\theta,\phi,\psi)$ and their conjugate momenta are canonical, and by
(0.3) $\mathfrak A$ and $\mathcal K$ share only the momenta of $\phi$ and $\psi$, whose coordinates appear in neither.
So $\{\mathfrak A,\mathcal K\} = 0$, hence $\{\mathcal G,\mathcal K\} = 0$, and $\Phi$, $\Psi$ Poisson-commute with
$\mathfrak A$, $\mathcal K$ and each other. (c) is algebra: $\frac P{r^2}-\mu = \alpha$, and $\alpha\mathfrak A =
(\alpha p_r+\beta)^2-\beta^2+\alpha\gamma$. (d) In a frame, $\mathcal K$ does not involve $(r,p_r)$ and $\tilde p$ is a
function of $(r,p_r,\Phi,\Psi)$, so $H_{\mathcal G}r = \partial_{p_r}\mathfrak A = 2\tilde p$ and $H_{\mathcal G}\tilde
p = H_{\mathfrak A}\tilde p$, which is the identity of S3 (sympy). The last claim is (b). $\square$

So on the characteristic set $\Sigma = \{\mathcal G = 0\}$ over $\{r>r_+\}$, where $\alpha>0$, $\tilde p^2 = \mathcal
R(r)$, with $\mathcal R$ evaluated at the constant values of $(E,\Phi,\Psi,\mathcal K)$ along the curve, and the pair
$(r,\tilde p)$ moves as a particle in the potential $-\mathcal R$: $H_{\mathcal G}r = 2\tilde p$, $H_{\mathcal G}\tilde
p = \partial_r\mathcal R$. For a covector $\nu = -z_0\,dt+\zeta$ of VI.A section 0, $E = z_0$; the flow of $G_{z_0} =
\varrho^{-2}\mathcal G$ on $\Sigma$ is $\varrho^{-2}H_{\mathcal G}$, and the future field on $\Sigma^\pm_{z_0}$ is
$\pm\varrho^{-2}H_{\mathcal G}$.

## 1. The radial function

Put $\Lambda := \mathcal K+sE^2 = |\eta|^2_{\mathbb S^3}+E^2|A\omega|^2\ge|\eta|^2_{\mathbb S^3}$, using $-\omega^T
A^2\omega = |A\omega|^2$. In a frame, $u := r^2$, the function $\mathcal P(u) := uP\mathcal R$ is
$$\mathcal P = \mu\big(PE+a\Phi(u+b^2)+b\Psi(u+a^2)\big)^2+\Delta_b\big(uPE^2+(a^2-b^2)(\Phi^2(u+b^2)-\Psi^2(u+a^2))-
\mathcal KP\big),\tag{1.1}$$
a polynomial of degree 5 in $u$ whose coefficients are polynomials in $(\mu,a,b,E,\Phi,\Psi,\Lambda)$ (S2). Then
$\mathcal Q(w) := w^5\mathcal P(w^{-1})$ is a polynomial in $w$ with $\mathcal Q(0) = E^2$, at $A = 0$
$$\mathcal Q = E^2-\Lambda w+\mu\Lambda w^2,\tag{1.2}$$
and $\mathcal R(r) = r^8\mathcal Q(r^{-2})/P(r)$, so $\mathcal R$ and $\mathcal Q(r^{-2})$ have the same sign and the
same zeros, with multiplicity, as $P>0$. $\mathcal R$ and $\mathcal Q$ are homogeneous of degree 2 in
$(E,\Phi,\Psi,\Lambda^{1/2})$, so their signs and zeros depend only on the normalised values in
$$\mathcal N := \{(E,\Phi,\Psi,\Lambda):E^2+\Lambda/\mu_0 = 1,\ (|\Phi|+|\Psi|)^2\le\Lambda\}.$$
Every covector with $E\ne0$ (as in every use below, where $E = z_0$) has its normalised values in $\mathcal N$:
$|\eta|^2_{\mathbb S^3}\ge\Phi^2/\sin^2\theta+\Psi^2/ \cos^2\theta\ge(|\Phi|+|\Psi|)^2$ by Cauchy-Schwarz.

**Lemma 1.1 (convexity).** There is $\epsilon_R>0$ such that for $|b-b_0|\le\epsilon_R$, in any frame, and every point
of $\mathcal N$, on $[0,2/\mu_0]$: if $\Lambda\ge\mu_0/6$, then $\mathcal Q''\ge\mu_0^2/12$; if $\Lambda<\mu_0/6$, then
$\mathcal Q\ge\frac12$.

*Proof.* At $A = 0$ and $|\mu-\mu_0|\le\frac12\mu_0$, (1.2) gives $\mathcal Q'' = 2\mu\Lambda\ge\mu_0^2/6$ when
$\Lambda\ge\mu_0/6$, and $\mathcal Q\ge E^2-\Lambda/(4\mu)\ge\frac56-\frac1{12} = \frac34$ when $\Lambda<\mu_0/6$. The
coefficients of $\mathcal Q$ at $(\mu,A)$ minus those at $(\mu,0)$ are polynomials in $(\mu,a,b,E,\Phi,\Psi,\Lambda)$
vanishing at $a = b = 0$, hence bounded by $C\|A\|$ on the compact set $\mathcal N\times\{|\mu-\mu_0|\le\frac12\mu_0\}$,
with $C$ independent of the frame ($|a|,|b|\le\|A\|$). So the difference is at most $C'\|A\|$ in $C^2([0,2/\mu_0])$,
which is below $\min(\mu_0^2/12,\frac14)$ for $\|A\|$ small. $\square$

S6 of `checks/trap5.py` samples the two bounds at $\|A\|\le0.02\mu_0^{1/2}$ on the face $(|\Phi|+|\Psi|)^2 = \Lambda$ of
$\mathcal N$, as an illustration only (the proof is the perturbation above): the minima found are $0.30\mu_0^2$ and
$0.80$.

**Corollary 1.2 (the radial structure).** Let $\epsilon_R$ also be so small that $r_+(b)^{-2}<2/\mu_0$, and let
$|b-b_0|\le\epsilon_R$ and $E\ne0$. Then on $(r_+,\infty)$: (a) $\mathcal R>0$ near $\infty$, and $\{r>r_+:\mathcal
R(r)<0\}$ is an interval, possibly empty. (b) A double zero $r_c$ of $\mathcal R$ in $(r_+,\infty)$ has $\partial_r^2
\mathcal R(r_c)>0$, and then $\mathcal R>0$ on $(r_+,\infty)\setminus\{r_c\}$. (c) For every $\delta>0$ there is
$\epsilon(\delta)\le\epsilon_R$ such that for $|b-b_0|\le\epsilon(\delta)$ every double zero has
$|r_c-(2\mu)^{1/2}|<\delta$ and $|\Lambda-4\mu E^2|<\delta E^2$.

*Proof.* In $w = r^{-2}\in(0,w_+)$, $w_+ := r_+^{-2}$, $\mathcal Q(0) = E^2>0$, and $\mathcal Q$ is either positive on
$[0,w_+]$ or strictly convex there (Lemma 1.1, after normalising). A strictly convex function is negative on an interval
and has a double zero only at its minimum, with $\mathcal Q''>0$; then it is positive elsewhere. As $\mathcal R =
r^8\mathcal Q(r^{-2})/P$ and $dw/dr\ne0$, this gives (a) and (b), with $\partial_r^2\mathcal R(r_c) = (r_c^8/P)\mathcal
Q''(w_c)(dw/dr)^2>0$. (c) Suppose $b_n\to b_0$ and normalised double zeros $(\pi_n,w_n)\in\mathcal N\times[0,2/\mu_0]$
have a limit $(\pi,w)$. By continuity it is a double zero of (1.2), $E^2-\Lambda w(1-\mu w) = 0 = -\Lambda(1-2\mu w)$.
$\Lambda = 0$ would give $E^2 = 1$, so $w = 1/(2\mu)$ and $\Lambda = 4\mu E^2$. Compactness gives (c). $\square$

## 2. The trapped set ((Γ.1)-(Γ.3) near $b_0$)

Fix $z_0\in\{1,-1\}$, so $E = z_0$ and $E^2 = 1$. Let $I := ((1.2\mu_0)^{1/2},(3\mu_0)^{1/2})$, which contains
$r_{\mathrm{ph}} = (2\mu_0)^{1/2}$ and lies in $(r_h,\frac74R_1)$, and $W := \{(\omega,\eta)\in T^*\mathbb
S^3:3\mu_0<|\eta|^2_{\mathbb S^3}<5\mu_0\}$.

**Lemma 2.1 (the critical radius).** There is $\epsilon_\Gamma\in(0,\epsilon_R]$ such that for
$|b-b_0|<\epsilon_\Gamma$: $\partial_r^2\mathcal R>0$ on $\bar I\times\bar W$; $\partial_r\mathcal R(\cdot;\omega,\eta)$
has a unique zero $r_c(\omega,\eta)\in I$; and with $m := \mathcal R(r_c)$ and $S := (\mathcal R-m)/(r-r_c)^2$, the
functions $r_c$, $m$ on $\bar W$ and $S$ on $\bar I\times\bar W$ are smooth in $(b,\cdot)$, $S>0$, and $dm\ne0$ on $\{m
= 0\}\cap\bar W\subset\{3.5\mu_0<|\eta|^2<4.5\mu_0\}$. In a frame they depend on $(\omega,\eta)$ only through
$(\Phi,\Psi,\mathcal K)$. At $b_0$, with $C = |\eta|^2$: $r_c^2 = C/2$, $m = C(\mu_0-C/4)$, $S = (r+r_c)^2$.

*Proof.* At $b_0$, $\mathcal R = r^4-C(r^2-\mu_0)$, so $\partial_r\mathcal R = 2r(2r^2-C)$ vanishes at $r^2 = C/2\in
(1.5\mu_0,2.5\mu_0)$, and $\partial_r^2\mathcal R = 12r^2-2C\ge14.4\mu_0-10\mu_0>0$ on $\bar I\times\bar W$. Then $m =
C(\mu_0-C/4)$ vanishes on $\bar W$ only at $C = 4\mu_0$, where $dm = (\mu_0-C/2)\,dC = -\mu_0\,dC\ne0$, and $\mathcal
R-m = (r^2-C/2)^2$ (S5). $\mathcal R$ is smooth in $(b,r,\omega,\eta)$ and $\bar I\times\bar W$ is compact, so $\mathcal
R_b\to\mathcal R_{b_0}$ in $C^3$ there. Hence for $b$ near $b_0$, $\partial_r^2\mathcal R>0$, $\partial_r\mathcal R$ has
exactly one zero in $I$, smooth in $(b,\omega,\eta)$ by the implicit function theorem, and the statements on $m$
persist. $S = \int_0^1(1-t)\,\partial_r^2\mathcal R(r_c+t(r-r_c))\,dt$ is smooth and positive. The frame statement holds
because it holds for $\mathcal R$ (Lemma 0.1 (d)). $\square$

On $O := \{(r,\omega;p_r,\eta):r\in I,(\omega,\eta)\in W\}$ define
$$\phi_\pm := \tilde p\mp(r-r_c)\sqrt S,\qquad T_\Gamma := \partial_r\big((r-r_c)\sqrt S\big),\qquad\Gamma_b :=
\Sigma_{z_0}\cap\{\phi_+ = \phi_- = 0\}\cap O.\tag{2.1}$$

**Proposition 2.2 ((Γ.1)-(Γ.3) near $b_0$).** Let $|b-b_0|<\epsilon_\Gamma$. In the variables of the Kerr-Schild time:

(a) $\Gamma_b = \{r = r_c,\ \tilde p = 0,\ m = 0\}\cap O$. It is a compact submanifold of codimension 2 of
$\Sigma_{z_0}$, invariant under the flow, and $\Gamma_{b_0}$ is VI.A's $\Gamma$.

(b) On $\Sigma_{z_0}\cap O$: $\phi_+\phi_- = m$, and the future field $\mathsf H := z_0\varrho^{-2}H_{\mathcal G}$
satisfies
$$\mathsf H\phi_+ = -2z_0\varrho^{-2}T_\Gamma\,\phi_+,\qquad\mathsf H\phi_- = 2z_0\varrho^{-2}T_\Gamma\,\phi_-,
\tag{2.2}$$
with $T_\Gamma = \sqrt S>0$ on $\Gamma_b$.

(c) (Γ.1)-(Γ.3) hold with $(\phi_u,\phi_s) := (\phi_+,\phi_-)$ for $z_0 = 1$ and $(\phi_-,-\phi_+)$ for $z_0 = -1$,
$\nu_u = \nu_s = 2\varrho^{-2}T_\Gamma$, and $\{\phi_u,\phi_s\} = 2\alpha\sqrt S>0$ on $\Gamma_b$. At $b_0$, $\nu_u =
\nu_s = 4(2\mu_0)^{-1/2}$ on $\Gamma$.

(d) The same holds for $\tilde g_b$ with the time function $\Psi_b^*t_*$, after the fibre translation of VI.A Lemma 0.1
from $t$ to $t_*$ and the cotangent lift of VI.B's $\Psi_b$. All the data are smooth in $b$ with values in $C^\infty$,
$\tilde\Gamma_b\subset T^*\{r_2<r<\rho_1^{-1}\}$, and $\nu_{\min}(b)$, $\beta_0(b) :=
\frac12\min_{\tilde\Gamma_b}|q_{z_0}|$ and $\max_{\tilde\Gamma_b}|q^\Gamma-4|$ tend to $4(2\mu_0)^{-1/2}$, $2$ and $0$
as $b\to b_0$.

*Proof.* (a) $\phi_+ = \phi_- = 0$ means $\tilde p = 0$ and $(r-r_c)\sqrt S = 0$, so $r = r_c$; on $\Sigma$, Lemma 0.1
(c) then gives $0 = \tilde p^2-\mathcal R = -m$. Conversely, $r = r_c$, $\tilde p = 0$, $m = 0$ give $\mathcal G =
\alpha^{-1}(\tilde p^2-\mathcal R) = 0$. By Lemma 2.1, $(\omega,\eta)$ ranges over the compact set $\{m = 0\}\cap\bar
W$, inside $W$, and $(r,p_r)$ is a smooth function of $(\omega,\eta)$ on it ($r = r_c$, $p_r = -\beta/\alpha$). So
$\Gamma_b$ is compact, and smooth of codimension 2 in $\Sigma$ by (c) below. It is invariant: on $\Gamma_b$,
$H_{\mathcal G}r = 2\tilde p = 0$ and $H_{\mathcal G}\tilde p = \partial_r\mathcal R(r_c) = 0$, while $r_c$ and $m$ are
constant along the flow (Lemma 0.1 (d)). At $b_0$, $\tilde p = (r^2-\mu_0)p_r-\mu_0E$, and the static time $t_s =
t-F_s$, $F_s' = \mu_0/(r^2-\mu_0)$, moves $p_r$ to $\xi_s = p_r-z_0F_s'$ (VI.A Lemma 0.1 (a)). So $\tilde p =
(r^2-\mu_0)\xi_s$, and $\{r = r_{\mathrm{ph}},\tilde p = 0,C = 4\mu_0\}$ is VI.A (3.1).

(b) On $\Sigma\cap O$, $\phi_+\phi_- = \tilde p^2-(r-r_c)^2S = \mathcal R-(r-r_c)^2S = m$. By Lemma 0.1 (d), on
$\Sigma$: $H_{\mathcal G}r = 2\tilde p$; $H_{\mathcal G}\tilde p = \partial_r\mathcal R =
2(r-r_c)S+(r-r_c)^2\partial_rS$, as $m$ does not depend on $r$; and $H_{\mathcal G}$ annihilates $r_c$ and $m$ and acts
on $S$ through $r$ only. Hence $H_{\mathcal G}((r-r_c)\sqrt S) = 2\tilde pT_\Gamma$. Substituting $\tilde p =
\phi_\pm\pm(r-r_c)\sqrt S$ and $2\sqrt S\,\partial_r\sqrt S = \partial_rS$ gives $H_{\mathcal G}\phi_\pm =
\mp2T_\Gamma\phi_\pm$ exactly (S4). Multiply by $z_0\varrho^{-2}$.

(c) (Γ.2) is (2.2), with the sign choices making $\phi_u$ decay and $\phi_s$ grow along $\mathsf H$; $\nu_{u/s}$ are
smooth and positive near $\Gamma_b$. For (Γ.1) and (Γ.3): at $\Gamma_b$, $d\mathcal G = \alpha^{-1}(2\tilde p\, d\tilde
p-d\mathcal R) = -\alpha^{-1}dm$, as $\tilde p = 0$, $\partial_r\mathcal R = 0$, and $d_{(\omega,\eta)}\mathcal R = dm$
at $r = r_c$ (since $\partial_r\mathcal R(r_c) = 0$). So $dG_{z_0} = \varrho^{-2}d\mathcal G\ne0$. At $\Gamma_b$,
$d\phi_\pm = d\tilde p\mp\sqrt S(dr-dr_c)$. Of the three covectors $d\phi_+$, $d\phi_-$, $dm$, only $d\tilde p$ has a
$dp_r$ component (it is $\alpha\ne0$), only $dr-dr_c$ has a $dr$ component, and $dm\ne0$ has neither; so they are
independent. Hence $\Gamma_u$, $\Gamma_s$ are smooth hypersurfaces of $\Sigma$ near $\Gamma_b$, meeting transversally in
$\Gamma_b$, and $\mathsf H$ is tangent to both by (2.2). For the bracket, $\{\phi_+,\phi_-\} = 2\{\tilde p,(r-r_c)\sqrt
S\}$, which at $r = r_c$ is $2\sqrt S(\{\tilde p,r\}-\{\tilde p,r_c\}) = 2\alpha\sqrt S$. Here $\{\tilde p,r\} =
\partial_{p_r}\tilde p = \alpha$, and $\{\tilde p,r_c\} = 0$ because, in a frame, $\tilde p$ is a function of
$(r,p_r,\Phi,\Psi)$ and $r_c$ of $(\Phi,\Psi,\mathcal K)$ (as in Lemma 0.1 (b)). $\alpha>0$ on $I$, as $I\subset
(r_+,\infty)$. For $z_0 = -1$, $\{\phi_-,-\phi_+\} = \{\phi_+,\phi_-\}$. At $b_0$, $\varrho^2 = r_{\mathrm{ph}}^2 =
2\mu_0$ and $\sqrt S = 2r_{\mathrm{ph}}$ on $\Gamma$, so $\nu = 4r_{\mathrm{ph}}/(2\mu_0) = 4(2\mu_0)^{-1/2}$, VI.A's
rate (S5).

(d) $dt$ and $dt_*$ are timelike for $g_b$ (III.B Lemma 3.3 (e) with $\beta = 0$, and Lemma 3.7 (a)). They are
co-oriented: $g_b^{-1}(dt,dt_*)$ cannot vanish where both are timelike, the region is connected, and near infinity it is
close to $\eta_{\mathrm{Mink}}^{-1}(dt,dt-d|x|) = -1$. $t-t_* = \psi-T_\mu$ is a function of $|x|$ (III.B (3.3), (3.6)).
So VI.A Lemma 0.1 (a)-(b) carries $\Gamma_b$, $\phi_{u/s}$, (Γ.1)-(Γ.3) and the future field to $t_*$, and the cotangent
lift of $\Psi_b$, a symplectomorphism intertwining the Hamilton fields, carries them to $\tilde g_b$. Everything in
(2.1) is built from frame-free functions smooth in $(b,\cdot)$, and so are the two maps. At $b_0$, $\Gamma\subset\{r =
r_{\mathrm{ph}}\}$ and $r_2<r_{\mathrm{ph}}<3R_1 = \rho_1^{-1}$; by continuity $\tilde\Gamma_b$ stays in
$T^*\{r_2<r<\rho_1^{-1}\}$. $q_{z_0}$ is continuous in $b$ and the point, and on $\Gamma_{b_0}$ it is $4z_0$ in $t_*$
(VI.A Theorem 6.1); so $\beta_0(b)\to2$ and $q^\Gamma\to4$ uniformly. In particular, after shrinking $O$ uniformly in
$b$, $z_0q_{z_0}>0$ on $\Sigma_{z_0}\cap O$, so there $\Sigma_{z_0}$ agrees with (H7)'s $\Sigma^\flat_{z_0} =
\Sigma^{z_0}_{z_0} = \Sigma_{z_0}\cap\{z_0q_{z_0}>0\}$ (I.B section 1), and the $\Gamma_{u/s}$ of (2.1) are (H7)'s. For
the continuity in $b$ that (H5) asks, $\phi_{u/s}$ are taken on a fixed neighbourhood of $\tilde\Gamma_{b_0}$ contained
in the transported $O_b$ for every $b$ near $b_0$. $\square$

## 3. $r$-normal hyperbolicity ((K3), (K4) near $b_0$)

(K3) concerns $z_0 = 1$ and $\mathsf V := q_1^{-1}H_{G_1}$ on $\Sigma^\flat_1$ near $\Gamma$. Its tangential bound, for
every $\epsilon>0$, is the substance; [Hin26c] Proposition 4.19 (3) proves it for Kerr from the integrable structure of
the flow on the trapped set, and so does this section, for the flow of $\mathcal K$ on $T^*\mathbb S^3$.

**Lemma 3.1 (the flow on $\Gamma_b$).** Let $|b-b_0|<\epsilon_\Gamma$ and $z_0 = 1$. The projection
$\pi:(r,\omega;p_r,\eta)\mapsto(\omega,\eta)$ restricts to a diffeomorphism of $\Gamma_b$ onto $\Gamma^{\mathbb S}_b :=
\{m = 0\}\cap W$, and $\pi_*(H_{\mathcal G}|_{\Gamma_b}) = H_h$ on $\Gamma^{\mathbb S}_b$, where $h := \mathcal
K+\mathfrak A(r_c,p_r^c;\cdot)$ on $W$, $p_r^c := -\beta(r_c)/\alpha(r_c)$. In a frame $h = F(\mathcal K,\Phi,\Psi)$ for
a smooth $F$, so $H_h = c_0H_{\mathcal K}+c_1H_\Phi+c_2H_\Psi$ with $c_i := \partial_iF$ constant along each orbit.

*Proof.* The inverse is $(\omega,\eta)\mapsto(r_c,\omega;p_r^c,\eta)$ (Proposition 2.2 (a)). The
$(\omega,\eta)$-components of $H_{\mathcal G} = H_{\mathfrak A}+H_{\mathcal K}$ are those of the Hamilton field on
$T^*\mathbb S^3$ of $\mathcal K+\mathfrak A(r,p_r;\cdot)$ with $(r,p_r)$ frozen. This differs from $H_h$ by $(\partial_r
\mathfrak A)H_{r_c}+(\partial_{p_r}\mathfrak A)H_{p_r^c}$. On $\Gamma_b$, $\partial_{p_r}\mathfrak A = 2\tilde p = 0$,
and $\partial_r\mathfrak A = -H_{\mathcal G}p_r = 0$ because $p_r = p_r^c$ there is a function of the conserved
$(\Phi,\Psi,\mathcal K)$ and $\Gamma_b$ is invariant. In a frame, $\mathfrak A(r,p_r;\cdot)$ depends on $(\omega,\eta)$
through $(\Phi,\Psi)$ and $r_c$, $p_r^c$ through $(\Phi,\Psi,\mathcal K)$ (Lemma 2.1). The $H$'s of $\mathcal K$,
$\Phi$, $\Psi$ commute (Lemma 0.1 (b)), so the $c_i$ are constant along orbits. $\square$

Let $Y := \{(\omega,\eta):3\mu_0\le\mathcal K\le5\mu_0\}\subset T^*\mathbb S^3$, compact and invariant under
$H_{\mathcal K}$, $H_\Phi$, $H_\Psi$; for $b$ near $b_0$ it contains $\Gamma^{\mathbb S}_b$. Fix any Riemannian metric
on $T^*\mathbb S^3$ for the norms.

**Lemma 3.2 (the flow of $\mathcal K$).** Let $\|A\|^2\le\mu_0/100$. For every $p\in Y$ there is $C_p$ with
$|D_pe^{sH_{\mathcal K}}v|\le C_p(1+|s|)|v|$ for all $v$ and $s\in\mathbb R$.

*Proof.* Work in a frame, with $F := (\mathcal K,\Phi,\Psi)$ and $X_0 := H_{\mathcal K}$, $X_1 := H_\Phi$, $X_2 :=
H_\Psi$, which commute. With $\Phi,\Psi$ fixed and $p_\theta = 0$, write $U(\theta) := \Phi^2/\sin^2\theta+
\Psi^2/\cos^2\theta-a^2+(a^2-b^2)\sin^2\theta$, so that $\mathcal K = p_\theta^2+U$ (with $E^2 = 1$). Then
$$U''\ge2\Phi^2/\sin^2\theta+2\Psi^2/\cos^2\theta-2|a^2-b^2|\tag{3.1}$$
(S6). On $Y$, wherever $p_\theta = 0$, $\Phi^2/\sin^2\theta+\Psi^2/\cos^2\theta = \mathcal
K+a^2-(a^2-b^2)\sin^2\theta\ge 3\mu_0-2\|A\|^2$, so $U''>0$ there.

*The singular set.* Let $Z := \{p\in Y:dF_0,dF_1,dF_2\text{ dependent at }p\}$. Where $\sin2\theta\ne0$,
$(\theta,\phi,\psi)$ and their momenta are canonical coordinates, $d\Phi$ and $d\Psi$ are independent, and $d\mathcal K
= 2p_\theta\,dp_\theta+U'\,d\theta+(\dots)d\Phi+(\dots)d\Psi$. So $p\in Z$ there iff $p_\theta = 0 = U'(\theta)$. If
$\Phi = 0$, then $U' = 2\sin\theta\cos\theta\,(\Psi^2/\cos^4\theta+a^2-b^2)>0$, since $\Psi^2/\cos^4\theta\ge
\Psi^2/\cos^2\theta\ge3\mu_0-2\|A\|^2$ there; likewise for $\Psi = 0$. So these points of $Z$ have $\Phi\Psi\ne0$ and
lie on $Z_1 := \{p_\theta = 0,\ \theta = \theta_0(\Phi,\Psi)\}$, $\theta_0$ a critical point of $U$: a family of
invariant 2-tori, one for each $(\Phi,\Psi)$ and $\theta_0$. Near $\omega_1 = 0$ use $y := \omega_1\in\mathbb
C\cong\mathbb R^2$, $\omega = (y,(1-|y|^2)^{1/2}e^{i\psi})$, with momenta $(\eta_y,\eta_\psi)$. There
$$\mathcal K = |\eta_y|^2-(y\cdot\eta_y)^2+\frac{\eta_\psi^2}{1-|y|^2}-a^2+(a^2-b^2)|y|^2,\tag{3.2}$$
$\Psi = \pm\eta_\psi$ and $\Phi = \pm(y_1\eta_2-y_2\eta_1)$. At $y = 0$, $d\Phi = \pm(\eta_2dy_1-\eta_1dy_2)$, $d\Psi =
\pm d\eta_\psi$ and $d\mathcal K = 2\eta_y\cdot d\eta_y+2\eta_\psi\,d\eta_\psi$. These are independent if $\eta_y\ne0$.
If $\eta_y = 0$, the point lies on $Z_2 := \{y = 0,\eta_y = 0\}$, a family of invariant circles, one for each
$\eta_\psi$ (by (3.2), $\dot y = \dot\eta_y = 0$ there). The same holds near $\omega_2 = 0$, with $a,b$ and $\Phi,\Psi$
exchanged, giving the family of circles $Z_2'$. So $Z = Z_1\cup Z_2\cup Z_2'$.

*The singular levels.* Every local maximum $\theta_m$ of $U$ has $U''(\theta_m)\le0$. By (3.1),
$\Phi^2/\sin^2\theta_m+\Psi^2/\cos^2\theta_m\le|a^2-b^2|$ there, so $U(\theta_m)\le2\|A\|^2<3\mu_0$. Hence for
$\Phi\Psi\ne0$ and $k\in[3\mu_0,5\mu_0]$, $\{U\le k\}$ is an interval, as $U\to\infty$ at both ends. If $k =
U(\theta_0)$ is a critical value, then $U''(\theta_0)>0$, $\theta_0$ is the unique minimum, and $F^{-1}(F(p))$ for $p\in
Z_1$ is the torus through $p$. For $p\in Z_2$, $F(p) = (\Psi_0^2-a^2,0,\Psi_0)$. A point with $\Phi = 0$, $\Psi =
\Psi_0$ and $\theta>0$ has $\mathcal K\ge U(\theta)$, and $U(\theta) =
\Psi_0^2/\cos^2\theta-a^2+(a^2-b^2)\sin^2\theta>\Psi_0^2-a^2$ because $\Psi_0^2\ge3\mu_0-\|A\|^2>|a^2-b^2|$. So
$F^{-1}(F(p))$ is the circle of $Z_2$ through $p$; likewise for $Z_2'$. Consequently, for $p\in Y\setminus Z$ the
connected component $L$ of $F^{-1}(F(p))\cap Y$ containing $p$ is compact and disjoint from $Z$.

*Regular orbits.* Let $p\notin Z$ and $N$ be a compact neighbourhood of $L$ in $Y\setminus Z$. On $N$ the $X_i$ are
independent and span $\bigcap_j\ker dF_j$ (each $X_i$ annihilates every $F_j$, and both spaces have dimension 3). Let
$Y_i := \sum_j(\Gamma^{-1})_{ij}\nabla F_j$, with $\Gamma_{ij} := \langle\nabla F_i,\nabla F_j\rangle$, so that
$dF_j(Y_i) = \delta_{ij}$; the $X_i$, $Y_i$ form a bounded frame on $N$. Since $dF_k$ is closed and $X_0F_k = 0$,
$dF_k([X_0,Y_i]) = X_0(dF_k(Y_i))-Y_i(X_0F_k) = 0$, so $[X_0,Y_i] = \sum_jd_{ij}X_j$ with $d_{ij}$ bounded on $N$. Let
$q_s := e^{sX_0}p$. Then $De^{sX_0}X_i(p) = X_i(q_s)$, and $W_i(s) := De^{-sX_0}Y_i(q_s)$ satisfies $W_i' =
\sum_jd_{ij}(q_s)X_j(p)$, so $De^{sX_0}Y_i(p) = Y_i(q_s)-\sum_jc_{ij}(s)X_j(q_s)$ with $c_{ij} =
\int_0^sd_{ij}(q_\sigma)\,d\sigma$, $|c_{ij}|\le C|s|$. Hence $|D_pe^{sX_0}|\le C_p(1+|s|)$.

*The tori $Z_1$.* On $Z_1$, $\sin2\theta_0\ne0$. Along the orbit the linearised equations, in the canonical coordinates,
are $\delta\dot\Phi = \delta\dot\Psi = 0$,
$$\frac d{ds}\binom{\delta\theta}{\delta p_\theta} = \begin{pmatrix}0&2\\-U''(\theta_0)&0\end{pmatrix}
\binom{\delta\theta}{\delta p_\theta}-\binom0{\partial_\Phi U'\,\delta\Phi+\partial_\Psi U'\,\delta\Psi},$$
with constant coefficients, and $\delta\dot\phi$, $\delta\dot\psi$ linear in $(\delta\theta,\delta\Phi,\delta\Psi)$ with
constant coefficients. As $U''(\theta_0)>0$ the matrix is invertible with imaginary eigenvalues, so $(\delta\theta,
\delta p_\theta)$ is bounded and $(\delta\phi,\delta\psi)$ grows at most linearly. *The circles $Z_2$, $Z_2'$.* By
(3.2), the Hessian of $\mathcal K$ at $Z_2$ has no terms mixing $(y,\eta_y)$ with $(\psi,\eta_\psi)$, so the
linearisation splits: $\delta\dot y = 2\delta\eta_y$, $\delta\dot\eta_y = -2(\Psi_0^2+a^2-b^2)\delta y$, an oscillator
since $\Psi_0^2+a^2-b^2>0$, and $\delta\dot\eta_\psi = 0$, $\delta\dot\psi = 2\delta\eta_\psi$. So growth is at most
linear. $\square$

**Lemma 3.3 (reparametrisation; cf. [Hin26c] Lemma 4.20).** Let $V_1$ be a smooth vector field, $\lambda>0$ smooth, $V_2
:= \lambda V_1$, and let the $V_2$-orbit of $p$ lie in a compact set on which $\lambda,1/\lambda,|d\lambda|\le
c_\lambda$. If $|D_pe^{sV_1}|\le c(1+|s|)^k$ for $s\in\mathbb R$, then $|D_pe^{sV_2}|\le c'(1+|s|)^{k+1}$.

*Proof.* $e^{sV_2}p = e^{\tau(s)V_1}p$ with $\tau' = \lambda(e^{sV_2}p)$, $\tau(0) = 0$, so $|\tau|\le c_\lambda|s|$.
Then $D_pe^{sV_2} = D_pe^{\tau V_1}+V_1\otimes D_p\tau$, and $\partial_sD_p\tau = d\lambda(D_pe^{\tau V_1})+(V_1\lambda)
D_p\tau$. Along the orbit, $V_1\lambda = \partial_s\log\lambda(e^{sV_2}p)$, so $\partial_s(D_p\tau/\lambda) =
d\lambda(D_pe^{\tau V_1})/\lambda$ and $|D_p\tau(s)|\le c_\lambda^3\int_0^{|s|}c(1+c_\lambda\sigma)^kd\sigma$. $\square$

**Proposition 3.4 ((K3) and (K4) near $b_0$).** There is $\epsilon_K\in(0,\epsilon_\Gamma]$ such that for
$|b-b_0|\le\epsilon_K$, (K3) holds for $\tilde g_b$ with $\Psi_b^*t_*$, and the splitting (1.1) of II.B and the
constants $\mu$, $C$, $C_\epsilon$ can be chosen continuous in $b$ and uniform, as (K4) asks.

*Proof.* *Tangential bound.* By Proposition 2.2 (d) it suffices to work in the Kerr-Schild variables of $g_b$. There, on
$\Sigma^\flat_1$ near $\Gamma_b$, the field $\mathsf V$ of $t_*$, transported by $T_F$, is $\lambda\,H_{\mathcal G}$
with $\lambda := (\varrho^2q_*)^{-1}$, where $q_*>0$ is $t_*$'s $q_1$; $\lambda$ is smooth and positive. Let
$p\in\Gamma_b$. By Lemma 3.1, $e^{sH_{\mathcal G}}|_{\Gamma_b}$ is conjugate by $\pi$ to $e^{sH_h} =
e^{sc_0X_0}e^{sc_1X_1}e^{sc_2X_2}$, the $c_i$ being constant along the orbit. Differentiating, $D_{\pi p}e^{sH_h} =
De^{sc_0X_0}De^{sc_1X_1}De^{sc_2X_2}+s\sum_iX_i\otimes dc_i$. Here $e^{tX_1}$, $e^{tX_2}$ are cotangent lifts of
rotations of $\mathbb S^3$ (the frame's $J_{12}$, $J_{34}$), with derivatives bounded uniformly in $t$ on $Y$. Lemma 3.2
enters at the rotated point $e^{sc_1X_1}e^{sc_2X_2}\pi p$; the rotations commute with $X_0$ and have derivatives bounded
on $Y$, so its constant there is at most $CC_{\pi p}$. Hence $|D_pe^{sH_{\mathcal G}}|_{T\Gamma_b}|\le C_p(1+|s|)^2$,
and by Lemma 3.3, $|D_pe^{s\mathsf V}|_{T\Gamma_b}|\le C'_p(1+|s|)^3$. Now let $\epsilon>0$. Identify $\Gamma_b$ with
$\Gamma_{b_0}$ smoothly in $b$ by $\iota_b(\omega,\eta) := (\omega,\lambda_b(\omega,\eta)\eta)$ on $\Gamma^{\mathbb
S}_{b_0}$, where $\lambda_b$ solves $m_b(\omega,\lambda_b\eta) = 0$ near 1 (Lemma 2.1: the radial derivative of $m$ is
$-8\mu_0^2\ne0$ at $b_0$), followed by $\pi^{-1}$. The set $\mathcal S := \{(b,p):|b-b_0|\le\epsilon_K,\
p\in\Gamma_b\}\cong\{|b-b_0|\le \epsilon_K\}\times\Gamma_{b_0}$ is compact. For each $(b,p)\in\mathcal S$ the polynomial
bound gives $T\ge1$ with $|D_pe^{\pm T\mathsf V_b}|_{T\Gamma_b}|\le e^{\epsilon T/2}$. By continuity in $(b,p)$, read
through $\iota_b$, the same $T$ gives $e^{\epsilon T}$ on a neighbourhood. Finitely many such neighbourhoods cover
$\mathcal S$, with times $T_j\le T_{\max}$. Composing the flow over successive times $T_j$ chosen at the current point
gives $|D_pe^{s\mathsf V_b}|_{T\Gamma_b}|\le C_\epsilon e^{\epsilon|s|}$ for all $(b,p)\in\mathcal S$, $s\in\mathbb R$,
with $C_\epsilon := \sup\{|De^{t\mathsf V_b}|:|t|\le T_{\max},(b,p)\in\mathcal S\}$.

*Splitting and normal rates.* On $\Gamma_b$, (2.2) gives $\mathsf V\phi_s = (\nu_s/q_1)\phi_s$ and $\mathsf V\phi_u =
-(\nu_u/q_1)\phi_u$, so $d\phi_s(De^{s\mathsf V}v) = \Lambda_s\,d\phi_s(v)$ for $v\in T\Gamma_u|_{\Gamma_b}$, with
$\Lambda_s := \exp\int_0^s(\nu_s/q_1)(e^{\sigma\mathsf V}p)\,d\sigma\ge e^{\nu's}$ for $s\ge0$. Here $\nu' :=
\inf\nu_s/q_1>0$ is uniform in $b$. Fix $\epsilon := \nu'/4$. Let $n_u$ be a smooth section of $T\Gamma_u|_{\Gamma_b}$
with $d\phi_s(n_u) = 1$, which exists by transversality. Write $De^{s\mathsf V}n_u(p) = \Lambda_s(p)n_u(e^{s\mathsf
V}p)+w_s(p)$ with $w_s(p)\in T\Gamma_b$. An invariant line $N^u = \mathrm{span}(n_u+h)$, $h$ a section of $T\Gamma_b$,
is a fixed point of $(\mathcal T_th)(e^{t\mathsf V}p) := \Lambda_t(p)^{-1}\big(De^{t\mathsf V}h(p)+w_t(p)\big)$. For $t$
so large that $C_\epsilon e^{\epsilon t}e^{-\nu't}\le\frac12$, $\mathcal T_t$ is a contraction on bounded continuous
sections, uniformly in $b$. So $h$ exists, is unique and continuous in $(b,p)$, and $\mathcal T_s h = h$ for all $s$ by
uniqueness. On $N^u$, $De^{s\mathsf V}$ is multiplication by $\Lambda_s$, so $|De^{s\mathsf V}v|\le Ce^{-\nu'|s|}|v|$
for $s\le0$. $N^s\subset T\Gamma_s$ is the same with time reversed. $T\Gamma_b$, $N^u$, $N^s$ span
$T_{\Gamma_b}\Sigma^\flat_1$: the dimensions are $5+1+1$, $N^u\not\subset T\Gamma_s$ as $d\phi_s(n_u+h) = 1$, and
$T\Gamma_u\cap T\Gamma_s = T\Gamma_b$. This is (1.1) with $\mu := \nu'$, continuous in $b$, with uniform constants.
$\square$

## 4. The global dynamics ((H8) near $b_0$)

**Proposition 4.1 ((H8) near $b_0$).** There is $\epsilon_8\in(0,\epsilon_K]$ such that for $|b-b_0|\le\epsilon_8$ and
$z_0\in\{1,-1\}$, (H8) (a) and (b) hold for $\tilde g_b$ with $\Psi_b^*t_*$, VI.A's radii and the trapped set of
Proposition 2.2, with $\bar\Gamma_{u/s}$ the global backward and forward trapped sets. The convergence in (a) is uniform
on compact sets of $(b,\text{initial point})$, as the extension of (H5) asks.

*Proof.* All the sets named in (H8) are carried by the cotangent lift of $\Psi_b$ to the corresponding sets for $g_b$
($\partial\mathcal R_\pm$ to the conormal of $\mathcal H_b$ at fibre infinity), and $\Psi_b$ is the identity on
$\{|x|\le\frac58R_1\}\supset\{r<r_0-\delta_0\}$ and on $\{|x|\ge\frac74R_1\}$ (VI.B Lemma 1.2; $r_0-\delta_0 =
\frac9{16}R_1$). So it suffices to prove (H8) for $g_b$, where the separation holds. The time function only translates
fibres (VI.A Lemma 0.1), so the projected curves, $r$, and the limits at fibre infinity do not depend on it. Limits over
$\partial X$ are read in $t_*$. Write $\gamma$ for a maximal integral curve of the future field in $\Sigma_{z_0}\cap
T^*\{r>r_0-2\delta_0\}$, parametrised by the rescaled field near fibre infinity (VI.A section 5).

*Outside the horizon.* On $\{r_A>r_+\}$, $(r,\tilde p)$ moves with $\tilde p^2 = \mathcal R(r)$, $\dot r =
\pm2\varrho^{-2}\tilde p$ and $\dot{\tilde p} = \pm\varrho^{-2}\partial_r\mathcal R$ (Lemma 0.1 (d)), the conserved
values of $(\Phi,\Psi,\mathcal K)$ fixed. By Corollary 1.2, either $\mathcal R$ has no double zero, or it has exactly
one, $r_c$, and then $m = 0$. In the first case $r$ is strictly monotone except at most one simple turning point, where
$\tilde p = 0\ne\partial_r\mathcal R$. Indeed $r$ cannot converge to a point $\bar r>r_+$: $\tilde p^2 = \mathcal R(\bar
r)>0$ would keep $|\dot r|$ bounded below, and a simple zero is passed in finite time. So at each end $r\to r_+$ or
$r\to\infty$, or the curve leaves $\{r_A>r_+\}$. In the second case $\mathcal R>0$ off $r_c$, the curve is $\Gamma_b$ or
lies on $\{\phi_+\phi_- = 0\}$, and $r$ is monotone, tending to $r_c$ at one end and to $r_+$ or $\infty$ at the other.
By Corollary 1.2 (c), with $\epsilon_8\le\epsilon(\delta)$ for a $\delta$ that places $r_c$ in $I$ and $(\omega,\eta)$
in $W$ ($|\eta|^2_{\mathbb S^3} = \Lambda-|A\omega|^2E^2$), and Lemma 2.1 (uniqueness of $r_c$ in $I$, with $\{m =
0\}\cap\bar W\subset W$), every double zero lies in $O$, so these curves are exactly those through $\{\phi_u =
0\}\cap\Sigma\cap O$ (backward asymptotic to $\Gamma_b$) or $\{\phi_s = 0\}\cap\Sigma\cap O$ (forward asymptotic),
extended by the flow.

*At infinity.* As $r\to\infty$, $\mathcal R = r^4E^2+O(r^2(1+\Lambda))$ and $\alpha = r^2+O(1)$, so $p_r = (\tilde
p-\beta)/\alpha = \mathrm{sgn}(\tilde p)+O((1+\Lambda)r^{-2})$; and $r_A = |x|(1+O(|x|^{-2}))$ (III.B Lemma 3.1 (b))
gives $\xi_t = p_r+O((1+\Lambda^{1/2})r^{-2})$ for the coefficient $\xi_t$ of $d|x|$, while $|\eta|/r\le
\Lambda^{1/2}r^{-1}$. Forward with $r\to\infty$, $\dot r>0$ forces $\mathrm{sgn}\,\tilde p = z_0$, so $\xi_t\to z_0$
and, with $t_* = t-F(|x|)$, $F := \psi-T_\mu$, $F' = 1+O(r^{-2})$ (III.B (3.3), Lemma 3.5 (a), (3.6)), $\xi_* =
\xi_t-z_0F'\to0$. Backward $\xi_*\to-2z_0$. The bounds are uniform for $\Lambda\le\Lambda_K$, so VI.A Proposition 5.1's
argument at infinity applies verbatim with $C$ replaced by $\Lambda$. This gives convergence to $R_{\mathrm{out}}$ and
$R_{z_0,\mathrm{in}}$, and the absorbing sets $A = \{r>R, |\xi_*|<\epsilon\}$ and $A' = \{r>R,|\xi_*+2z_0|<\epsilon\}$.

*Near the radial sets.* (H3) as proved in VI.B gives $\mathsf H_bq\ge\frac12\beta_0q$ on
$\partial\Sigma_0\cap\{q<\epsilon_q\}$ near $\partial\mathcal R_\pm$ (VI.B Proposition 2.2) and $\rho_\infty^{-1}\mathsf
H_b\rho_\infty\ge\frac12\beta_0$ at $\partial\mathcal R_\pm$. By continuity there is a neighbourhood $U_R$ of
$\partial\mathcal R_\pm$ in the compactified $\Sigma$, with compact closure and the same for all $b$ near $b_0$, on
which $\mathsf H_bq\ge\frac14\beta_0q-c\rho_\infty$ and $\mathsf H_b\rho_\infty\ge\frac14\beta_0\rho_\infty$, with $q$
extended as $|\eta/\xi|^2$. So $L := q+(8c/\beta_0)\rho_\infty$ has $\mathsf H_bL\ge\frac18\beta_0L$ on $U_R$. $L$
vanishes on $\partial\mathcal R_\pm$ and is positive on the rest of $U_R$: $\rho_\infty>0$ at finite covectors, and at
fibre infinity near $\partial\mathcal R_\pm$, $q = |\hat\eta|^2$ vanishes only on $\partial\mathcal R_\pm$ (VI.B
Proposition 2.2: there $\partial\Sigma_0$ is a graph over $(\omega,\hat\eta)$ and $\partial\mathcal R_\pm = \{\hat\eta =
0\}$). Fix $0<\delta_L<\min L$ over the boundary of $U_R$, and $N := \{L<\delta_L\}\cap U_R$, an open neighbourhood of
$\partial\mathcal R_\pm$. Backward along a curve in $U_R$, $L$ does not increase; so a curve in $N$ never reaches
$\{L\ge\delta_L\}$, which contains the boundary of $U_R$, and stays in $N$ backward, with $L$ decaying backward
exponentially at the uniform rate $\frac18\beta_0$.

*At the horizon.* $\mathcal H_b$ is a null hypersurface (VI.B Lemma 1.1), and $dr_A(w)<0$ for every future-directed
causal $w$ at $\mathcal H_b$ not tangent to its null generators. This set of $w$ is connected, $dr_A(w)$ vanishes on it
only for $w$ tangent to the generators, and the sign is that of $b_0$ (VI.A section 5) by continuity. The velocity of
$\gamma$ is a nonzero multiple of $\nu^\sharp$, and $\nu^\sharp$ tangent to a generator would make $\nu$ a multiple of
$dr_A$, so $\nu(\partial_t) = 0$, against $E = z_0$. So a curve meeting $\mathcal H_b$ at a finite covector crosses it
inward, transversally, and by continuity each finite covector $p_0$ over $\mathcal H_b$ has $\delta,T>0$ such that the
curve through any point within $\delta$ of $p_0$ is in $\{r_A<r_+\}$ a parameter $T$ later and in $\{r_A>r_+\}$ a
parameter $T$ earlier. Let $\gamma$ stay in $\{r_A>r_+\}$ on a forward or a backward half-line, with $r\to r_+$ along
it, and let $\mathcal L$ be its limit set at that end, in the compactified characteristic set: compact, invariant, over
$\mathcal H_b$, and approached by $\gamma$. $\mathcal L$ contains no finite covector $p_0$: $\gamma$ comes within
$\delta$ of $p_0$ arbitrarily far along the half-line, and is then in $\{r_A<r_+\}$ a parameter $T$ later, still on the
half-line. So $\mathcal L\subset\partial\Sigma_0$. A point of $\partial\Sigma_0\setminus\partial\mathcal R_\pm$ reaches
$\{r<r_h-\kappa\}$ forward in finite time (VI.B Proposition 2.2, (H4)), which an invariant set over $\mathcal H_b$
cannot contain; so $\mathcal L\subset\partial\mathcal R_\pm$, and $\gamma$ lies in $N$ near that end. Forward this is
impossible: $L>0$ along $\gamma$ does not decrease forward in $N$, so it cannot tend to $0$. Hence an exterior curve
with $r\to r_+$ forward leaves $\{r_A>r_+\}$, so meets $\mathcal H_b$ and crosses it inward; one with $r\to r_+$
backward tends backward to $\partial\mathcal R_\pm$. Inside, read for $\tilde g_b$ ($\Psi_b$ carries $\{r<r_h\}$ to the
inside of $\mathcal H_b$, VI.B Lemma 1.2), on $\{r_0-2\delta_0\le r<r_h\}$, $dr$ is timelike (VI.B Lemma 1.1 and
Proposition 2.2), so $r$ decreases strictly along $\gamma$. On compact subsets of the compactified
$\Sigma_{z_0}\cap\{r_0-\delta_0\le r\le r_1\}$, $r_1<r_h$, the rescaled $\dot r$ is bounded above by a negative
constant, so $\gamma$ reaches $\{r<r_0-\delta_0\}$ in finite time. Backward, $r$ increases strictly along an interior
curve. If the curve meets $\mathcal H_b$ backward, it crossed it inward there, and its earlier part is an exterior
curve, treated above. Otherwise $r\to\bar r\le r_h$ backward. $\bar r<r_h$ is impossible: with $r_1 := \bar r$, the
rescaled $\dot r$ is at most a negative constant on the compact part of the compactified $\Sigma_{z_0}$ over
$\{r(s_0)\le r\le\bar r\}$, so $r$ would grow without bound backward. If $\bar r = r_h$, a finite covector $p_0$ in the
backward limit set is impossible, since $\gamma$ would be outside $\mathcal H_b$ a parameter $T$ before passing within
$\delta$ of $p_0$, still on the backward half-line; so the limit set lies in $\partial\Sigma_0$ over $\mathcal H_b$,
hence in $\partial\mathcal R_\pm$ as above, and $\gamma$ tends backward to $\partial\mathcal R_\pm$.

*(a).* Combining: a curve not in $\bar\Gamma_u$ tends backward to $\partial\mathcal R_\pm$ or $R_{z_0,\mathrm{in}}$, and
a curve not in $\bar\Gamma_s$ tends forward to $R_{\mathrm{out}}$ or reaches $\{r<r_0-\delta_0\}$ in finite time.
*Uniformity.* With the absorbing sets $A$, $A'$, $N$ (in which $L$ decays backward at the uniform rate) and
$\{r<r_0-\delta_0\}$, VI.A Proposition 5.1's cover argument applies on compact subsets of $\{(b,p)\}$: the set of
$(b,p)$ whose curve enters the relevant absorbing set before parameter $T$ is open and increases with $T$, and these
sets cover by the pointwise statement.

*(b).* Within $O$, a point with $\phi_u = 0$ has $m = 0$ and lies on the branch on which $r\to r_c$, $\tilde p\to0$
backward, so its curve tends to $\Gamma_b$ backward. A point with $\phi_s = 0\ne\phi_u$ moves away from $r_c$ backward,
and a point with $m\ne0$ has no double zero. So $\bar\Gamma_u\cap O = \{\phi_u = 0\}\cap\Sigma\cap O = \Gamma_u$, and
likewise for $\bar\Gamma_s$. $\square$

## 5. The theorem

**Theorem 5.1 ((Dyn) near $b_0$).** There is $\epsilon_{\mathrm{VI}}>0$ such that on the compact parameter set $\mathcal
B_{\mathrm{VI}} := \{|b-b_0|\le\epsilon_{\mathrm{VI}}\}$, the metrics $\tilde g_b = \Psi_b^*g_b$ with the time function
$\Psi_b^*t_*$ and VI.A's radii satisfy (H3)'s dynamical conditions and (H4) (VI.B Proposition 2.2), (H6) and (K1) (VI.A
Lemma 1.1), (Γ.1)-(Γ.3) with $\nu_{\min}\to4(2\mu_0)^{-1/2}$, $\beta_0\to2$ and $q^\Gamma\to4$ as $b\to b_0$
(Proposition 2.2), (K3) and (K4) (Proposition 3.4), and (H8) (Proposition 4.1). All the data depend continuously on $b$
into $C^\infty$, with the constants uniform, as (H5), its extension in I.B section 1.5, and (K4) ask. These hold for
every operator with principal symbol $\tilde g_b^{-1}\otimes\mathrm{Id}$. The operator hypotheses (the threshold in (H3)
and (Γ.4)) are proved in III.D, III.F and Part IV$''''$, read through $\Psi_b$ (VI.B section 1).

*Proof.* $\epsilon_{\mathrm{VI}} := \min(\epsilon_1/2,\epsilon_8)$, with $\epsilon_1$ from VI.B Proposition 2.2.
$\square$

## 6. Findings, labels and sources

(VI.B$'$1) *Separation in the write-out's coordinates.* Five-dimensional Myers-Perry separates in III.B's Kerr-Schild
coordinates, written spheroidally by $x = (r^2I-A^2)^{1/2}\omega$, with the Kerr-Schild time, not only in
Boyer-Lindquist coordinates: $\varrho^2g_b^{-1} = \mathfrak A+\mathcal K$ (Lemma 0.1). The Kerr-Schild momentum $p_r$
and the Boyer-Lindquist one differ by a function of $r$ and the conserved momenta, and $\tilde p = \alpha p_r+\beta$ is
$\alpha$ times the latter. No change of coordinates is read.

(VI.B$'$2) *Smooth separatrices.* (H7) asks smooth $\phi_{u/s}$. A perturbation of VI.A's separatrices by the
persistence of normally hyperbolic manifolds gives $C^k$ for each $k$, on neighbourhoods shrinking with $k$. The
separation gives them in closed form, (2.1), smooth in $b$.

(VI.B$'$3) *The tangential bound.* At $b\ne b_0$ the flow on the trapped set is not periodic. The bound for every
$\epsilon$ comes from its integrable structure (Lemmas 3.1-3.2), as in [Hin26c] Proposition 4.19 (3). The singular
orbits are the 2-tori of $Z_1$ and the circles of $Z_2$, $Z_2'$, where Kerr has the equatorial set; all are elliptic
near $b_0$.

(VI.B$'$4) *No frame.* The eigenframe of $A$ is not continuous in $A$ at $A = 0$, nor where $a^2 = b^2$. Every object is
defined from $A$ directly ((0.1), (0.2), Lemma 2.1); frames are used only to compute and to compare with (0.3).

(VI.B$'$5) *The radial convexity holds near $b_0$ only.* [Hin26c] Lemma 4.12 proves its convexity for all subextremal
Kerr. Here convexity of $\mathcal Q$ in $w = r^{-2}$ (Lemma 1.1) is proved by perturbation from (1.2), which suffices
for $b$ near $b_0$.

*Labels.* Lemma 0.1: [Hin26c] (4.30)-(4.32) and Carter's constant, for Myers-Perry. Lemma 1.1 and Corollary 1.2:
[Hin26c] Lemmas 4.11-4.12. Lemma 2.1 and Proposition 2.2: [Hin26c] Lemmas 4.14-4.18, Definitions 4.13, 4.15, 4.17.
Lemmas 3.1-3.3 and Proposition 3.4: [Hin26c] Proposition 4.19 and Lemma 4.20. Proposition 4.1: [Hin26c] Proposition
4.24.

*Sources.* [Hin26c] pp. 85-95 (section 4.2.3: Lemmas 4.10-4.20, Proposition 4.19 and its proof), READ. Inputs: III.B
Lemmas 3.1, 3.3 (d)-(e), 3.7 (a), Definition 3.2, (3.3), Lemma 3.5 (a), (3.6); VI.A Lemma 0.1, Propositions 2.1, 3.1,
5.1, Theorem 6.1; VI.B Lemmas 1.1, 1.2, Proposition 2.2; I.B (H7), (H8); II.B (K3), (K4); `checks/trap5.py` S1-S6.
