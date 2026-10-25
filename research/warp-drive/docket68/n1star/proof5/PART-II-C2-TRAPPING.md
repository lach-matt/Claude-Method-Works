# Part II.C$'$. The stable and unstable trapped sets of perturbed metrics, at n = 4

*Status.* Written out in full (D199). Not yet read by an independent verifier; nothing here is labelled proved. This part
proves, at spatial dimension $n = 4$, [Hin26c] Proposition 6.3 (pp. 112-113): for a metric that decays in time to the
stationary model, there are hypersurfaces, close to the stable and unstable manifolds of the stationary trapped set and
converging to them, to which the null-bicharacteristic flow is tangent. The source is [Hin26c] = P. Hintz,
arXiv:2606.28008v1. Part I.B (`PART-I-B-HIGHENERGY.md`) is cited as I.B, Part II.A (`PART-II-A-SETUP.md`) as II.A, Part
II.B (`PART-II-B-DYNAMICS.md`) as II.B and Part II.C (`PART-II-C-OPERATORS.md`) as II.C.

*Method.* The source reduces the statement to a theorem on decaying perturbations of a flow with normally hyperbolic
trapping, [Hin21] Theorem 2.6 (P. Hintz, *Normally hyperbolic trapping on asymptotically stationary spacetimes*, Probab.
Math. Phys. 2 (2021), arXiv:1811.07843v1), and reads the uniformity of the result in the perturbation from that theorem's
proof. That theorem is stated for closed manifolds and smooth invariant splittings, and its statement is not
quantitative. Here the theorem needed is proved in full (section 2), quantitatively, from what Part I assumes: the
defining functions of (Γ.1)-(Γ.3), with their exact equations (Γ.2), and the tangential growth bound of (K3). The proof
is the graph transform in its simplest form. The hypersurfaces have codimension one, and (Γ.2) gives the normal dynamics
in closed form, so each step of the transform solves one scalar equation by monotonicity, and the tangential dynamics
enters only through the norm of a time-$T$ map, made small against the normal rates by taking $T$ large. Section 3
carries out the reduction of [Hin26c] p. 113 (graphing the perturbed characteristic set over the stationary one and
pulling back the flow) in full.

*How it is organised.* Section 1: the persistence theorem. Section 2: its proof. Section 3: [Hin26c] Proposition 6.3 at
$n = 4$. Section 4: what this part found.

## 1. The persistence theorem

**Theorem 1.1.** Let $Y$ be a smooth manifold with a Riemannian metric, $V_0$ a smooth vector field on $Y$,
$\Gamma\subset Y$ a compact smooth submanifold, $O\subset Y$ an open neighbourhood of $\Gamma$ with compact closure, and
$\phi_u,\phi_s,\nu_u,\nu_s\in C^\infty(\bar O)$ real, such that:

(i) $\Gamma = \{\phi_u = \phi_s = 0\}\cap O$, and $d\phi_u$, $d\phi_s$ are linearly independent at every point of
$\Gamma$;

(ii) $V_0\phi_u = -\nu_u\phi_u$ and $V_0\phi_s = \nu_s\phi_s$ on $O$, with $\nu_u,\nu_s\ge\nu>0$ on $O$;

(iii) $\Gamma$ is invariant under the flow of $V_0$, and for every $\varepsilon>0$ there is $C_\varepsilon$ with
$|De^{sV_0}v|\le C_\varepsilon e^{\varepsilon|s|}|v|$ for $v\in T\Gamma$, $s\in\mathbb R$.

Let $k\ge2$, $\ell>0$, $T_0\ge1$ and $\rho(t) := t^{-\ell}$. Then there are a neighbourhood $O'\subset O$ of $\Gamma$,
$\epsilon_0>0$ and $C$ such that the following holds for every vector field $\tilde V$ on $[T_0,\infty)\times O$, tangent
to the slices $\{t\}\times O$, of class $C^k$ in $(t,y)$ jointly, with
$$\|\tilde V\| := \sup_{t\ge T_0}\rho(t)^{-1}\|\tilde V\|_{C^k([t,t+1]\times O)}\le\epsilon\le\epsilon_0.\tag{1.1}$$
The vector field $V := \partial_t+V_0+\tilde V$ is tangent to the hypersurfaces
$$W^u := \{\phi_u+\psi_u = 0\},\qquad W^s := \{\phi_s+\psi_s = 0\}\quad\text{of}\ [T_0,\infty)\times O',\tag{1.2}$$
where $\psi_u\in C^k$, $\psi_s\in C^{k-1}$, and $|\partial^\alpha\psi_u(t,y)|\le C\epsilon\rho(t)$ for $|\alpha|\le k$,
$|\partial^\alpha\psi_s(t,y)|\le C\epsilon\rho(t)$ for $|\alpha|\le k-1$, derivatives in $(t,y)$ in fixed charts. $W^u$
meets $\{t = T_0\}$ in $\{\phi_u = 0\}$. The constants $O'$, $\epsilon_0$, $C$ depend only on $k$, $\ell$, $\nu$,
$C_\varepsilon$ for $\varepsilon := \nu/(2k)$, the $C^{k+1}$-norms of $V_0,\phi_u,\phi_s,\nu_u,\nu_s$ on $O$ in a fixed
finite atlas, and the choices of section 2.1; not on $T_0$ or $\tilde V$.

$C^k$-norms on $[t,t+1]\times O$ are taken in the charts of a fixed finite atlas of a neighbourhood of $\bar O$, in which
the metric is uniformly comparable to the Euclidean one.

*Remarks.* (a) (iii) is the tangential half of $r$-normal hyperbolicity for every $r$ ([HPS77] Definition 4); the normal
half is (ii), in which the normal dynamics is linear in $\phi_u$, $\phi_s$. No invariant splitting of $T_\Gamma Y$ is
used. (b) $W^s$ is the analogue of the stable manifold and is determined by $V$; $W^u$, the analogue of the unstable
manifold, depends on its initial slice, here $\{\phi_u = 0\}$ at $t = T_0$ ([Hin21] footnote 1). In the application, with
time running forward, $W^u$ is the backward-trapped hypersurface and $W^s$ the forward-trapped one.

## 2. Proof of Theorem 1.1

### 2.1 Coordinates

Let $\pi:O_1\to\Gamma$ be a smooth retraction of a neighbourhood $O_1\subset O$ of $\Gamma$ ($\pi|_\Gamma = \mathrm{id}$;
e.g. the projection of a tubular neighbourhood), and $\Psi_0 := (\pi,\phi_u,\phi_s):O_1\to\Gamma\times\mathbb R^2$.

*$\Psi_0$ is a local diffeomorphism near $\Gamma$.* At $p\in\Gamma$, $\ker d\phi_u\cap\ker d\phi_s$ has codimension 2 by
(i) and contains $T_p\Gamma$ (as $\phi_{u/s} = 0$ on $\Gamma$), which has codimension 2; so they are equal. If
$d\Psi_0(v) = 0$, then $v\in T_p\Gamma$ and $d\pi(v) = v = 0$. *It is injective near $\Gamma$.* Otherwise there are
$p_n\ne q_n$ with $\Psi_0(p_n) = \Psi_0(q_n)$ and $\mathrm{dist}(p_n,\Gamma),\mathrm{dist}(q_n,\Gamma)\to0$; for a
subsequence $p_n\to p$, $q_n\to q$ in $\Gamma$, and $\Psi_0(p) = \Psi_0(q)$ gives $p = q$ ($\Psi_0(p) = (p,0,0)$ on
$\Gamma$), contradicting injectivity near $p$ (inverse function theorem). So $\Psi_0$ is a diffeomorphism from a
neighbourhood of $\Gamma$ onto an open set containing $\Gamma\times\{0\}$, hence, $\Gamma$ being compact, containing
$\Gamma\times[-\delta_1,\delta_1]^2$ for some $\delta_1>0$. Put $O_2 := \Psi_0^{-1}(\Gamma\times(-\delta_1,\delta_1)^2)$.

In the coordinates $(y,a,b) := \Psi_0$ on $O_2$, by (ii),
$$V_0 = Y_0(y,a,b)-\nu_u(y,a,b)\,a\,\partial_a+\nu_s(y,a,b)\,b\,\partial_b,\tag{2.1}$$
with $Y_0$ tangent to $\Gamma$ (the $y$-component) and $Y_0(\cdot,0,0) = V_0|_\Gamma$, and $\tilde V = (\tilde Y,\tilde
A,\tilde B)$ with $C^k$-norms bounded by $C\epsilon\rho(t)$. Fix a finite atlas of $\Gamma$, charts
$\kappa_i:U_i\to\mathbb R^{m}$, compact $K_i\subset U_i$ covering $\Gamma$, and a Lebesgue number $\lambda>0$ (every ball
of radius $\lambda$ lies in some $U_i$), and let $C_{\mathrm{at}}\ge1$ bound the distortion between the Euclidean norms
of the charts and the metric of $\Gamma$ on the $U_i$. For functions on $\Gamma\times I$, $I$ an interval,
$\|D^jf\|_\infty$ is the supremum over $i$ and over $K_i\times I$ of the $j$-th derivatives in the chart
$\kappa_i\times\mathrm{id}$.

### 2.2 Time-$T$ maps

Let $\Phi^0_\tau$ be the time-$\tau$ map of $V_0$ and, for $t\ge T_0$, $\Phi_{t,\tau}$ the spatial part of the
time-$\tau$ map of $V$ from the slice $\{t\}$ ($\tau$ of either sign). By (2.1), along an integral curve of $V_0$ in
$O_2$, $a(\tau) = a(0)\exp(-\int_0^\tau\nu_u)$ and $b(\tau) = b(0)\exp\int_0^\tau\nu_s$; so for $\tau\ge0$
$$\Phi^0_\tau(y,a,b) = \big(f_\tau(y,a,b),\ a\,m^u_\tau(y,a,b),\ b\,m^s_\tau(y,a,b)\big),\qquad m^u_\tau\le e^{-\nu\tau},
\quad m^s_\tau\ge e^{\nu\tau},\tag{2.2}$$
with $m^{u/s}_\tau\in[e^{-C_\nu\tau},e^{C_\nu\tau}]$, $C_\nu := \sup_O(\nu_u+\nu_s)$, as long as the curve stays in
$O_2$; and similarly for $\tau\le0$ with the roles of $a$ and $b$ exchanged.

Fix $T\ge1$, to be chosen in section 2.3, and then $\delta\in(0,\frac14\delta_1]$ with $e^{2C_\nu
T}\delta\le\frac14\delta_1$, and put $B := \Gamma\times[-\delta,\delta]^2$. For $\epsilon_0$ small (depending on $T$,
$\delta$), $\Phi_{t,\tau}$ is defined on $B$ for $|\tau|\le2T$ with $t+\tau\ge T_0$, with values in
$\Gamma\times(-\frac12\delta_1,\frac12\delta_1)^2$, and:

(T1) $\{|a|\le\delta\}$ is forward invariant and $\{|b|\le\delta\}$ backward invariant for $V$ within $O_2$: $\frac
d{d\tau}|a|\le-\nu|a|+|\tilde A|<0$ at $|a| = \delta$ when $C\epsilon_0<\nu\delta$, and likewise for $b$ backward.

(T2) $\|\Phi_{t,\tau}-\Phi^0_\tau\|_{C^k}\le C_T\epsilon\rho(t)$ on $B$, derivatives in $(t,y,a,b)$, and
$\|\Phi_{t,\tau}\|_{C^{k}}\le C_T$. This is Grönwall's inequality for the equation and its variational equations up to
order $k$, whose source is $\tilde V$ and its derivatives at the times between $t$ and $t+\tau$. By (1.1) these are at
most $\epsilon\rho(s)$ on each window $[s,s+1]$ with $s\ge\min(t,t+\tau)\ge T_0\ge1$, and
$\rho(s)\le\rho(\min(t,t+\tau))\le(1+2T)^\ell\rho(t)$, because $t/(t+\tau)\le1+2T$ when $\tau<0$ and $t+\tau\ge1$; the
factor $(1+2T)^\ell$ and the number $4T+1$ of windows go into $C_T$.

(T3) *The tangential rate.* With $\varepsilon := \nu/(2k)$, $|Df_\tau(y,0,0)|_{T_y\Gamma}|\le C_\varepsilon
e^{\varepsilon|\tau|}$ by (iii), as $f_\tau(\cdot,0,0)$ is the flow of $V_0|_\Gamma$.

(T4) *The cross terms.* $|\partial_af_\tau(y,0,0)|\le C_*C_\varepsilon e^{\varepsilon\tau}$ for $\tau\ge0$, and
$|\partial_bf_\tau(y,0,0)|\le C_*C_\varepsilon e^{\varepsilon|\tau|}$ for $\tau\le0$, with $C_* :=
\nu^{-1}\sup|\partial_{a,b}Y_0|$. Indeed, linearising (2.1) at $(y,0,0)$ in the direction $\partial_a$: $\delta
b\equiv0$, $\delta a(\sigma) = m^u_\sigma(y,0,0)\le e^{-\nu\sigma}$, and $\delta y' = D_yY_0\,\delta
y+\partial_aY_0\,\delta a$, so $\delta y(\tau) = \int_0^\tau J(\tau,\sigma)\partial_aY_0\,\delta a(\sigma)\,d\sigma$ with
$J(\tau,\sigma) = De^{(\tau-\sigma)V_0}|_{T\Gamma}$ at $f_\sigma(y,0,0)$, bounded by $C_\varepsilon
e^{\varepsilon(\tau-\sigma)}$; hence $|\delta y(\tau)|\le C_\varepsilon\sup|\partial_aY_0|\int_0^\tau
e^{\varepsilon(\tau-\sigma)-\nu\sigma}d\sigma\le C_*C_\varepsilon e^{\varepsilon\tau}$. Backward, $b$ contracts and the
same computation applies.

(T5) On $B$, every first derivative of $\Phi^0_\tau$ differs from its value at $(y,0,0)$ by at most $C_T\delta$; and
$\partial_y(a m^u_\tau)$, $\partial_b(am^u_\tau)$, $\partial_y(bm^s_\tau)$, $\partial_a(bm^s_\tau)$ are $O(C_T\delta)$ on
$B$, carrying the factor $a$ or $b$.

Let $\Lambda_\tau := C_{\mathrm{at}}(C_*+2)C_\varepsilon e^{\varepsilon|\tau|}$. By (T3)-(T5) and (T2), for
$0\le\tau\le2T$ the block $D_{(y,a)}(\Phi_y,\Phi_a)$ of $D\Phi_{t,\tau}$ has norm at most
$\Lambda_\tau+C_T(\delta+\epsilon_0)$ in the chart norms ($|(v,s)| := |v|+|s|$), and for $-2T\le\tau\le0$ the block
$D_{(y,b)}(\Phi_y,\Phi_b)$ likewise. We use $C_T$ for constants depending on $T$ and the data, and fix $T$ so large that
$$e^{-\nu T}(2\Lambda_T)^k(1+2T)^\ell\le\tfrac14,\tag{2.3}$$
which is possible as $k\varepsilon = \frac\nu2<\nu$; then $\delta$ as above, small also against $C_T$ where stated; and
finally $\epsilon_0$ small against $\delta$ and $C_T$.

### 2.3 One step of the graph transform

For $t\ge T_0$ and $\tau\in[0,2T]$ let $\Phi := \Phi_{t,\tau}$, and $K_a := \Gamma\times[-\delta,\delta]_a$. For
$\beta:K_a\to\mathbb R$ with $|\beta|\le\frac14\delta$ and $\mathrm{Lip}\,\beta\le\theta_0 := (4C_T)^{-1}$ (in the chart
norms) define $\mathcal S_\Phi\beta:K_a\to\mathbb R$ by
$$\Phi_b\big(y,a,\mathcal S_\Phi\beta(y,a)\big) = \beta\big(\Phi_y(y,a,\mathcal S_\Phi\beta(y,a)),\Phi_a(y,a,
\mathcal S_\Phi\beta(y,a))\big):\tag{2.4}$$
$\mathrm{graph}(\mathcal S_\Phi\beta)$ is the set of points of $B$ that $\Phi$ maps into $\mathrm{graph}(\beta)$.

**Lemma 2.1.** For $(y,a)\in K_a$, (2.4) has exactly one solution $b\in[-\delta,\delta]$, and:

(S1) $|\mathcal S_\Phi\beta|\le e^{-\nu\tau}(|\beta|_\infty+C_T\epsilon\rho(t))$;

(S2) $|\mathcal S_\Phi\beta-\mathcal S_\Phi\tilde\beta|_\infty\le
e^{-\nu\tau}(1-2C_T\delta)^{-1}|\beta-\tilde\beta|_\infty$ for two such $\beta,\tilde\beta$;

(S3) if $\beta\in C^k$ and $\|D^j\beta\|_\infty\le M_j\epsilon\rho(t)$ for $1\le j\le k$, then $\mathcal S_\Phi\beta\in
C^k$ and, for $1\le i\le k$,
$$\|D^i\mathcal S_\Phi\beta\|_\infty\le e^{-\nu\tau}(1-2C_T\delta)^{-1}(2\Lambda_\tau)^i\|D^i\beta\|_\infty+C(T,M_1,
\dots,M_{i-1})\,\epsilon\rho(t).\tag{2.5}$$

*Proof.* Fix $(y,a)$ and put $h(b) := \Phi_b(y,a,b)-\beta(\Phi_y,\Phi_a)(y,a,b)$. By (T1) the point $(\Phi_y,\Phi_a)$
lies in $K_a$, so $h$ is defined on $[-\delta,\delta]$. By (2.2), (T2) and (T5), $\partial_b\Phi_b =
m^s_\tau+b\,\partial_bm^s_\tau+O(C_T\epsilon\rho)\ge e^{\nu\tau}(1-C_T\delta)-C_T\epsilon_0$, and
$|\partial_b(\Phi_y,\Phi_a)|\le C_T$, so $h'(b)\ge e^{\nu\tau}(1-2C_T\delta)>0$ after the choices of section 2.2. At $b =
\pm\delta$, $\pm\Phi_b\ge\delta m^s_\tau(1-C_T\delta)-C_T\epsilon\rho\ge\frac34\delta>|\beta|$, so $h$ changes sign: a
unique zero. (S1): at the zero, $b\,m^s_\tau(y,a,b) = \beta(\cdots)-(\Phi_b-\Phi^0_{\tau,b})$, and $m^s_\tau\ge
e^{\nu\tau}$. (S2): with $b$, $\tilde b$ the two zeros, $h(\tilde b) = h(\tilde b)-\tilde h(\tilde b) =
-(\beta-\tilde\beta)(\cdots)$, so $|b-\tilde b|\le|\beta-\tilde\beta|_\infty/\inf h'$. (S3): $\mathcal S_\Phi\beta\in
C^k$ by the implicit function theorem, $H(w,b) := \Phi_b(w,b)-\beta((\Phi_y,\Phi_a)(w,b))$, $w = (y,a)$, being $C^k$ with
$\partial_bH\ge e^{\nu\tau}(1-2C_T\delta)$. Fix $p\in K_i\times[-\delta,\delta]$; as $(\Phi_y,\Phi_a)$ has Lipschitz
constant at most $2\Lambda_\tau$, it maps the ball of radius $\lambda/(2\Lambda_{2T})$ about $p$ into a ball of radius
$\lambda$, which lies in some chart $U_l$; differentiate $H(w,\mathcal S_\Phi\beta(w)) = 0$ $i$ times at $p$ in the
charts $i$ and $l$. The result is $\partial_bH\cdot D^i\mathcal S_\Phi\beta =
-D^i\beta\big[(D_w(\Phi_y,\Phi_a)+\partial_b(\Phi_y,\Phi_a)D\mathcal S_\Phi\beta)^{\otimes i}\big]+R_i$, where $R_i$ is a
sum of products of: derivatives of order $\le i$ of $\beta$ and of order $\le i-1$ of $\mathcal S_\Phi\beta$, and
derivatives of order $\le i+1$ of $\Phi$ (bounded by $C_T$). Every product in $R_i$ contains a factor
$O(\epsilon\rho(t))$: either $D^j\beta$, $j\ge1$; or $D^j\mathcal S_\Phi\beta$ with $1\le j\le i-1$, bounded inductively;
or a pure $w$-derivative of $\Phi_b$, which is $b\,D^j_wm^s_\tau+D^j_w(\Phi_b-\Phi^0_{\tau,b})$ at $b = \mathcal
S_\Phi\beta = O(\epsilon\rho)$ by (S1) and (T2). In the leading term,
$|D_w(\Phi_y,\Phi_a)|\le\Lambda_\tau+C_T(\delta+\epsilon_0)$ and $|\partial_b(\Phi_y,\Phi_a)D\mathcal S_\Phi\beta|\le
C_T\cdot C\epsilon_0$, together at most $2\Lambda_\tau$. Dividing by $\partial_bH$ gives (2.5). $\square$

*The backward step.* For $\tau\in[0,2T]$ and $t\ge T_0+\tau$ let $\Phi^- := \Phi_{t,-\tau}$, the map back to the slice
$t-\tau$, and $K_b := \Gamma\times[-\delta,\delta]_b$. For $\alpha:K_b\to\mathbb R$ with $|\alpha|\le\frac14\delta$,
$\mathrm{Lip}\,\alpha\le\theta_0$, define $\mathcal U_{\Phi^-}\alpha$ by $\Phi^-_a(y,\mathcal U\alpha(y,b),b) =
\alpha(\Phi^-_y,\Phi^-_b)(y,\mathcal U\alpha(y,b),b)$: $\mathrm{graph}(\mathcal U\alpha)$ is the set of points of $B$
that the backward map sends into $\mathrm{graph}(\alpha)$, which is the image of $\mathrm{graph}(\alpha)$ under the
forward map, within $B$. Lemma 2.1 holds verbatim for $\mathcal U$, with $(a,b)$ exchanged, $\Phi$ replaced by $\Phi^-$,
and $\rho(t)$ by $\rho(t-\tau)\le(1+2T)^\ell\rho(t)$ in (S1) and (2.5): backward, $a$ is multiplied by $(m^u)^{-1}\ge
e^{\nu\tau}$, $\{|b|\le\delta\}$ is invariant by (T1), and the block $D_{(y,b)}(\Phi^-_y,\Phi^-_b)$ is bounded by
$\Lambda_\tau+C_T(\delta+\epsilon_0)$ by (T3)-(T5).

### 2.4 The stable hypersurface

Let $t_j := T_0+jT$, $j\ge0$, and $\mathcal S_j := \mathcal S_{\Phi_{t_j,T}}$. Choose $M_0 := 2C_T$ and then,
inductively, $M_i\ge2C(T,M_1,\dots,M_{i-1})$, $1\le i\le k$, and let $\epsilon_0$ be so small that
$M_0\epsilon_0\le\frac14\delta$ and $M_1\epsilon_0\le\theta_0$. Let $\mathfrak B$ be the set of sequences $\beta =
(\beta_j)_{j\ge0}$ of $C^k$ functions on $K_a$ with $\|D^i\beta_j\|_\infty\le M_i\epsilon\rho(t_j)$ for $0\le i\le k$,
and $(\mathcal T\beta)_j := \mathcal S_j\beta_{j+1}$.

*$\mathcal T$ maps $\mathfrak B$ into itself.* As $\rho(t_{j+1})\le\rho(t_j)$, (S1) gives $|\mathcal S_j\beta_{j+1}|\le
e^{-\nu T}(M_0+C_T)\epsilon\rho(t_j)\le M_0\epsilon\rho(t_j)$, and (2.5) with (2.3) gives $\|D^i\mathcal
S_j\beta_{j+1}\|_\infty\le\frac12M_i\epsilon\rho(t_j)+C(T,M_1,\dots,M_{i-1})\epsilon\rho(t_j)\le M_i\epsilon\rho(t_j)$.

*$\mathcal T$ is a contraction* for $d(\beta,\tilde\beta) := \sup_j\rho(t_j)^{-1}|\beta_j-\tilde\beta_j|_\infty$, by (S2)
and $\rho(t_j)^{-1}\le\rho(t_{j+1})^{-1}$, with factor $e^{-\nu T}(1-2C_T\delta)^{-1}\le\frac12$.

So $\beta^{(n)} := \mathcal T^n(0)\in\mathfrak B$ is Cauchy for $d$, and $\beta^{(n)}_j\to\beta_j$ uniformly. Bounded in
$C^k$ on the compact $K_a$, the $D^{k-1}\beta^{(n)}_j$ are equicontinuous, so (Arzelà-Ascoli) every subsequence has a
further subsequence converging in $C^{k-1}$, necessarily to $\beta_j$: $\beta^{(n)}_j\to\beta_j$ in $C^{k-1}$,
$\|D^i\beta_j\|_\infty\le M_i\epsilon\rho(t_j)$ for $i\le k-1$, and $D^{k-1}\beta_j$ is Lipschitz with constant $\le
CM_k\epsilon\rho(t_j)$. By (S2), $\mathcal T$ is continuous for $d$ on sequences with $|\beta_j|\le\frac14\delta$,
$\mathrm{Lip}\le\theta_0$, so $\mathcal T\beta = \beta$: $\beta_j = \mathcal S_j\beta_{j+1}$ for all $j$.

*All times.* For $t\in[t_j,t_{j+1}]$ put $\beta(t,\cdot) := \mathcal S_{\Phi_{t,t_{j+1}-t}}\beta_{j+1}$; at $t = t_{j+1}$
($\Phi = \mathrm{id}$) this is $\beta_{j+1}$, and at $t = t_j$ it is $\mathcal S_j\beta_{j+1} = \beta_j$. For
$t\in[t_{j-1},t_j]$, by the cocycle property $\Phi_{t,t_{j+1}-t} = \Phi_{t_j,T}\circ\Phi_{t,t_j-t}$ and uniqueness in
Lemma 2.1 (applied with $\tau = t_{j+1}-t\le2T$, and with (T1)), $\mathcal S_{\Phi_{t,t_j-t}}\beta_j = \mathcal
S_{\Phi_{t,t_{j+1}-t}}\beta_{j+1}$: a point is mapped into $\mathrm{graph}(\beta_j)$ at time $t_j$ if and only if it is
mapped into $\mathrm{graph}(\beta_{j+1})$ at time $t_{j+1}$. So on $[t_{j-1},t_{j+1}]$, $\beta(t,\cdot)$ is given by the
single equation $H(t,w,b) := \Phi_{t,t_{j+1}-t,b}(w,b)-\beta_{j+1}(\Phi_{t,t_{j+1}-t,ya}(w,b)) = 0$, with $H\in C^{k-1}$
in $(t,w,b)$ (the flow map from time $t$ to $t_{j+1}$ is $C^k$ in $(t,w,b)$, $\beta_{j+1}\in C^{k-1}$) and
$\partial_bH\ge\frac12$. By the implicit function theorem, $\beta\in C^{k-1}([t_{j-1},t_{j+1}]\times K_a)$, and
differentiating the equation as in (S3) bounds its derivatives of order $\le k-1$ by $C\epsilon\rho(t_{j-1})\le
C(1+2T)^\ell\epsilon\rho(t)$. Hence $\beta\in C^{k-1}([T_0,\infty)\times K_a)$ with $|\partial^\alpha\beta|\le
C\epsilon\rho(t)$, $|\alpha|\le k-1$.

*Tangency.* Let $W^s := \{(t,y,a,b): b = \beta(t,y,a)\}\subset[T_0,\infty)\times B$, a $C^{k-1}$ hypersurface. If
$(t,x)\in W^s$ with $t\in[t_{j-1},t_{j+1})$, then for small $\sigma>0$,
$\Phi_{t+\sigma,t_{j+1}-t-\sigma}(\Phi_{t,\sigma}(x)) = \Phi_{t,t_{j+1}-t}(x)\in\mathrm{graph}(\beta_{j+1})$, and
$\Phi_{t,\sigma}(x)\in B$ by (T1) and $|b|\le C\epsilon_0<\delta$ along $W^s$; so $\Phi_{t,\sigma}(x)\in W^s(t+\sigma)$,
and the integral curve of $V$ through $(t,x)$ stays in $W^s$ for small forward times. Hence $V$ is tangent to $W^s$.

### 2.5 The unstable hypersurface

Put $\alpha_0 := 0$ on $K_b$ and $\alpha_{j+1} := \mathcal U_{\Phi_{t_{j+1},-T}}\alpha_j$: $\mathrm{graph}(\alpha_{j+1})$
is the image of $\mathrm{graph}(\alpha_j)$ under $\Phi_{t_j,T}$, within $B$. With $M'_0 := 2C_T(1+2T)^\ell$ and
$M'_i\ge2C(T,M'_1,\dots,M'_{i-1})(1+2T)^\ell$, induction on $j$ gives $\|D^i\alpha_j\|_\infty\le M'_i\epsilon\rho(t_j)$
for $i\le k$: by the backward form of (S1) and (2.5), with $\rho(t_j)\le(1+T)^\ell\rho(t_{j+1})$ and (2.3),
$\|D^i\alpha_{j+1}\|_\infty\le e^{-\nu T}(2\Lambda_T)^i(1-2C_T\delta)^{-1}M'_i\epsilon\rho(t_j)+C\epsilon\rho(t_j) \le
\frac12M'_i\epsilon\rho(t_{j+1}) +\frac12M'_i\epsilon\rho(t_{j+1})$. No limit is taken, and $\alpha_j\in C^k$. For
$t\in[t_j,t_{j+1}]$, $\alpha(t,\cdot) := \mathcal U_{\Phi_{t,-(t-t_j)}}\alpha_j$, whose graph is the image of
$\mathrm{graph}(\alpha_j)$ under $\Phi_{t_j,t-t_j}$; on $[t_j,t_{j+2}]$ the same formula with $\alpha_j$ holds by the
cocycle property, so $\alpha\in C^k([T_0,\infty)\times K_b)$ by the implicit function theorem (now with $C^k$ data), with
$|\partial^\alpha\alpha|\le C\epsilon\rho(t)$ for $|\alpha|\le k$. $W^u := \{a = \alpha(t,y,b)\}$ is a union of forward
orbit segments of $V$ starting on $\{t = T_0,a = 0\}$, within $B$; so $V$ is tangent to it, as in section 2.4.

### 2.6 The defining functions

Let $O' := \Psi_0^{-1}(\Gamma\times(-\delta,\delta)^2)$ and, for $(t,x)\in[T_0,\infty)\times O'$,
$$\psi_s(t,x) := -\beta(t,\pi(x),\phi_u(x)),\qquad\psi_u(t,x) := -\alpha(t,\pi(x),\phi_s(x)).$$
Then $\{\phi_s+\psi_s = 0\} = W^s$ and $\{\phi_u+\psi_u = 0\} = W^u$ in $[T_0,\infty)\times O'$, and the bounds follow by
the chain rule, $\pi$, $\phi_{u/s}$ being smooth. $W^u\cap\{t = T_0\} = \{\phi_u = 0\}$ as $\alpha(T_0,\cdot) = \alpha_0
= 0$. The constants depend only on the quantities listed in Theorem 1.1. $\square$

## 3. [Hin26c] Proposition 6.3 at $n = 4$

### 3.1 The stationary data

Let $\Gamma := \Gamma_1\subset\Sigma^\flat_1\subset T^*\tilde X^\circ$ be the trapped set of (H7) at $z_0 = 1$, with $O$,
$\phi_u$, $\phi_s$, $\nu_u$, $\nu_s$ as there, $q_1 = 2g_0^{-1}(-dt_*+\zeta,dt_*)$ (I.B Lemma 1.1, II.B (K3)), and
$\mathsf V := q_1^{-1}H_{G_1}$ on $\Sigma^\flat_1$ near $\Gamma$, where $G_1(x,\zeta) := G_0(-dt_*+\zeta)$, $G_0(\nu) =
g_0^{-1}(\nu,\nu)$. $dG_1\ne0$ near $\Gamma$ (Γ.3), so $Y := \Sigma^\flat_1\cap O_0$, for a small neighbourhood $O_0$ of
$\Gamma$, is a smooth hypersurface of $T^*\tilde X^\circ$; $q_1\ge2\beta_0>0$ on $\Gamma$ (Γ.4), hence on $O_0$.

**Lemma 3.1.** $Y$, $V_0 := \mathsf V$, $\Gamma$ and the restrictions of $\phi_u,\phi_s$ and of $\nu_u/q_1,\nu_s/q_1$ to
$Y$ satisfy (i)-(iii) of Theorem 1.1, after shrinking $O_0$, with $\nu := \nu_{\min}/(4\sup_{O_0}q_1)$; and the constants
are uniform in the parameter $b$ of (H5), (K4).

*Proof.* (ii): (Γ.2) gives $H_{G_1}\phi_u = -\nu_u\phi_u$ and $H_{G_1}\phi_s = \nu_s\phi_s$ on $\Sigma^\flat_1\cap O$, so
$\mathsf V\phi_u = -(\nu_u/q_1)\phi_u$ and $\mathsf V\phi_s = (\nu_s/q_1)\phi_s$; $\nu_{u/s}\ge\frac12\nu_{\min}$ near
$\Gamma$ by continuity. (i): $\Gamma = \Gamma_u\cap\Gamma_s$ within $O$ by (Γ.1). Suppose at $p\in\Gamma$ that
$a\,d\phi_u+b\,d\phi_s$ vanishes on $T_pY$ for some $(a,b)\ne0$; as $T_pY = \ker dG_1$, $a\,d\phi_u+b\,d\phi_s = c\,dG_1$
at $p$. Take the Poisson bracket with $\phi_s$: $a\{\phi_u,\phi_s\} = c\{G_1,\phi_s\} = c\,H_{G_1}\phi_s = c\,\nu_s\phi_s
= 0$ at $p$, so $a = 0$ by (Γ.3); with $\phi_u$ likewise $b = 0$. (iii): $\Gamma$ is invariant, $\mathsf V$ being tangent
to $\Gamma_u$ and $\Gamma_s$ (Γ.1); the bound is the tangential part of (K3) for $\mathsf V$. Uniformity: (H5) extended
to (H6)-(H8) in I.B and (K4) give continuity in $b$ of $\Gamma$, $\phi_{u/s}$, $\nu_{u/s}$, $q_1$ into $C^\infty$ and
uniform $\nu_{\min}$, $\beta_0$, $C_\varepsilon$; the choices of section 2.1 can then be made uniformly for $b$ near any
$b_0$, and $\mathcal B$ is compact. $\square$

### 3.2 The slice and the projected flow

Near $(K^+)^\circ$, over $D := \{t_*>1,\ r_{\Gamma,-}<r<r_{\Gamma,+}\}$ with
$[r_{\Gamma,-},r_{\Gamma,+}]\subset(r_2,\rho_1^{-1})$ containing the projection of $\Gamma$, the e3b-structure is spanned
by $\partial_{t_*},\partial_x$ (II.A section 2.1), and ${}^{e3b}T^*_DM = T^*D$ with covectors $-\sigma\,dt_*+\zeta$. On
$\{\sigma>0\}$ use the slice coordinates $(t_*,x,z)$, $z := \zeta/\sigma$, which identify
$\{\sigma>0\}\cap{}^{e3b}S^*_DM$ with $(1,\infty)\times T^*\{r_{\Gamma,-}<r<r_{\Gamma,+}\}$; at $\rho_K = t_*^{-1} = 0$
this is the map $\Phi_1$ of II.B Definition 2.2. Let $g = g_0+h$ with $h\in\tilde{\mathcal G}^{d_0,(0,0,\ell_K)}_{e3b}$,
$d_0\ge3$, $\ell_K>0$, and $\|h\|\le\epsilon$. Over $D$, $x_I$ and $\rho_+$ are bounded above and below and $\rho_K\sim
t_*^{-1}$, so the components of $g^{-1}-g_0^{-1}$ in the frame $\partial_{t_*},\partial_x$ have derivatives of order $\le
d_0$ along $\partial_{t_*},\partial_x$ bounded by $C\epsilon t_*^{-\ell_K}$ (Neumann series, II.A Lemma 8.2). Put
$$p_1(t_*,x,z) := G(t_*,x;-dt_*+z),\qquad\tilde g := p_1-G_1 = (g^{-1}-g_0^{-1})(-dt_*+z,-dt_*+z),\tag{3.1}$$
so $\tilde g$ is quadratic in $z$, with $|\partial^\alpha\tilde g|\le C\epsilon t_*^{-\ell_K}$, $|\alpha|\le d_0$, on
compact $z$-sets.

**Lemma 3.2.** For $p := G$ (homogeneous of degree 2 on $T^*D$), $\sigma^{-1}H_p$ descends to
$\{\sigma>0\}\cap{}^{e3b}S^*_DM$, and in the slice coordinates
$$\hat W := \sigma^{-1}H_p = \big(z\cdot\partial_zp_1-2p_1\big)\partial_{t_*}+
\partial_zp_1\cdot\partial_x-\partial_xp_1\cdot\partial_z-(\partial_{t_*}p_1)\,z\cdot\partial_z.\tag{3.2}$$
$\hat W$ is tangent to $\{p_1 = 0\}$, and on $\{p_1 = 0\}$ it is a positive multiple of the field $\mathsf H_G$ of II.C
(4.2) where $z\cdot\partial_zp_1>0$.

*Proof.* With $\tau := -\sigma$, $p = \tau^2p_1(t_*,x,-\zeta/\tau)$, so $\partial_\tau p =
\sigma(z\cdot\partial_zp_1-2p_1)$, $\partial_\zeta p = \sigma\partial_zp_1$, $\partial_{t_*}p =
\sigma^2\partial_{t_*}p_1$, $\partial_xp = \sigma^2\partial_xp_1$; and for $f = f(t_*,x,z)$, $\partial_\tau f =
\sigma^{-1}z\cdot\partial_zf$, $\partial_\zeta f = \sigma^{-1}\partial_zf$. Inserting into $H_p = \partial_\tau
p\,\partial_{t_*}+\partial_\zeta p\cdot\partial_x-\partial_{t_*}p\,\partial_\tau-\partial_xp\cdot\partial_\zeta$ gives
(3.2). $\hat Wp_1 = -2p_1\partial_{t_*}p_1$, which vanishes on $\{p_1 = 0\}$. On the characteristic set, $\mathsf H_G =
\rho_\infty H_{G_{e3b}} = \rho_\infty fH_G$ with $f = x_I^{-2}\rho_+^{-2}>0$, so $\mathsf H_G = \rho_\infty f\sigma\hat
W$. $\square$

For $g = g_0$, (3.2) on $\{G_1 = 0\}$ is $q_1\partial_{t_*}+H_{G_1}$, as $z\cdot\partial_zG_1 = q_1$ there (II.B Lemma
5.2 (d)): the stationary field of II.B section 2.

### 3.3 Graphing the perturbed characteristic set

Let $N$ be a smooth vector field on a neighbourhood $O_N$ of $\Gamma$ in $T^*\tilde X^\circ$ with $NG_1 = 1$ there ($N :=
\nabla G_1/|\nabla G_1|^2$ for a Riemannian metric, as $dG_1\ne0$). Shrinking, $\hat\Psi_0(f,w) := e^{fN}(w)$ is a
diffeomorphism from $(-c,c)\times Y$ onto a neighbourhood of $Y$, and $G_1(e^{fN}w) = f$, as $\frac d{df}G_1(e^{fN}w) =
(NG_1)(e^{fN}w) = 1$. Write $w(x,z)$ and $f(x,z)$ for the inverse.

**Lemma 3.3.** For $\epsilon$ small there is $F\in C^{d_0}((1,\infty)\times Y)$, $|\partial^\alpha F|\le C\epsilon
t_*^{-\ell_K}$ for $|\alpha|\le d_0$, with $\{p_1(t_*,\cdot) = 0\}\cap\hat\Psi_0((-c,c)\times Y) = \{e^{F(t_*,w)N}w: w\in
Y\}$. The map $\hat\Psi(t_*,f,w) := (t_*,e^{(f+F(t_*,w))N}w)$ is a $C^{d_0}$ diffeomorphism onto a neighbourhood of the
perturbed characteristic set near $\Gamma$, with $\|\hat\Psi-\hat\Psi_0\|_{C^{d_0}}\le C\epsilon t_*^{-\ell_K}$
($\hat\Psi_0(t_*,f,w) := (t_*,e^{fN}w)$), and it maps $\{f = 0\}$ onto the perturbed characteristic set.

*Proof.* At $e^{fN}w$, $p_1 = f+\tilde g(t_*,e^{fN}w)$. The map $f\mapsto-\tilde g(t_*,e^{fN}w)$ sends $[-\frac c2,\frac
c2]$ into itself and has Lipschitz constant $\sup|N\tilde g|\le C\epsilon<1$, so it has a unique fixed point $F(t_*,w)$,
$|F|\le C\epsilon t_*^{-\ell_K}$. $\partial_f(f+\tilde g(t_*,e^{fN}w)) = 1+N\tilde g\ge\frac12$, so $F\in C^{d_0}$ by the
implicit function theorem, and each derivative of order $\le d_0$ of the identity $F+\tilde g(t_*,e^{FN}w) = 0$ expresses
$\partial^\alpha F$ through derivatives of $\tilde g$, each $O(\epsilon t_*^{-\ell_K})$, and lower derivatives of $F$.
$\hat\Psi$ is then $C^{d_0}$-close to $\hat\Psi_0$, hence a diffeomorphism near $f = 0$. $\square$

On $\{p_1\ne0\}$ near $\Gamma$, $\hat Wt_* = z\cdot\partial_zp_1-2p_1$, which is $\ge\beta_0$ near $\Gamma$ for
$\epsilon$ small (it is $q_1-2G_1$ at $\epsilon = 0$). Put $V^h := \hat W/(\hat Wt_*)$, a $C^{d_0-1}$ vector field near
$(1,\infty)\times\Gamma$ with $V^ht_* = 1$, tangent to $\{p_1 = 0\}$ (Lemma 3.2), and $V^0 := \hat W_0/(\hat W_0t_*) =
\partial_{t_*}+H_{G_1}/(q_1-2G_1)$ for $g_0$ (where $\partial_{t_*}G_1 = 0$). By (3.1)-(3.2), $V^h-V^0$ has coefficients
with derivatives of order $\le d_0-1$ bounded by $C\epsilon t_*^{-\ell_K}$. Let $V := \hat\Psi^*V^h$ restricted to $\{f =
0\} = (1,\infty)\times Y$, which is tangent to it since $V^h$ is tangent to the characteristic set; $Vt_* = 1$, as
$\hat\Psi$ preserves $t_*$. As $\hat\Psi_0^*V^0$ restricted to $\{f = 0\}$ is $\partial_{t_*}+q_1^{-1}H_{G_1} =
\partial_{t_*}+\mathsf V$, and $\hat\Psi-\hat\Psi_0$, $V^h-V^0$ are $O(\epsilon t_*^{-\ell_K})$ in $C^{d_0}$, resp.
$C^{d_0-1}$,
$$V = \partial_{t_*}+\mathsf V+\tilde V,\qquad\tilde V(t_*,\cdot)\ \text{tangent to}\ Y,\qquad|\partial^\alpha\tilde V|
\le C\epsilon t_*^{-\ell_K},\ |\alpha|\le d_0-1.\tag{3.3}$$

### 3.4 The statement

**Proposition 3.4 ([Hin26c] Proposition 6.3 at $n = 4$).** Let $d_0\ge3$, $\ell_K>0$ and $g = g_0+h$ with
$h\in\tilde{\mathcal G}^{d_0,(0,0,\ell_K)}_{e3b}$ of sufficiently small norm $\epsilon$. Let $\partial\Gamma_0 :=
\{t_*>1\}\times\Gamma$ in the slice coordinates (the stationary extension of $\partial\Gamma_{K^+}$, II.B Definition
5.1), and $U$ a small conic neighbourhood of it in ${}^{e3b}S^*_DM$. There are functions $\phi_0^{u/s}\in C^\infty(U)$,
independent of $t_*$, with $\phi_0^{u/s} = \phi_{u/s}(x,z)$ on the stationary characteristic set, and $\tilde\phi^u\in
C^{d_0-1}(U)$, $\tilde\phi^s\in C^{d_0-2}(U)$, with
$$|\partial^\alpha\tilde\phi^u|\le C\epsilon t_*^{-\ell_K}\ (|\alpha|\le d_0-1),\qquad|\partial^\alpha\tilde\phi^s|
\le C\epsilon t_*^{-\ell_K}\ (|\alpha|\le d_0-2),$$
derivatives along $\partial_{t_*},\partial_x$ and the fibres, such that, with $\phi^{u/s} :=
\phi_0^{u/s}+\tilde\phi^{u/s}$, the field $\mathsf H_G$ is tangent to $\Gamma^{u/s} := \partial\Sigma^+\cap
U\cap(\phi^{u/s})^{-1}(0)$. For $\epsilon\le\epsilon_1$ the norms are at most 1. The same holds, with uniform constants,
for the stationary models of parameters $b$ near $b_0$ (K4).

*Proof.* By Lemma 3.1 and (3.3), Theorem 1.1 applies on $Y$ with $V_0 = \mathsf V$, $k := d_0-1\ge2$, $\ell := \ell_K$,
$T_0 := 1$ (or any $T_0>1$, for the open set $t_*>1$), giving $\psi_u\in C^{d_0-1}$, $\psi_s\in C^{d_0-2}$ on
$(1,\infty)\times O'$ with $V$ tangent to $W^{u/s} = \{\phi_{u/s}+\psi_{u/s} = 0\}$. For $(t_*,x,z)$ in $U$, write $(x,z)
= e^{fN}w$ ($w = w(x,z)\in Y$) and put
$$\phi_0^{u/s}(x,z) := \phi_{u/s}(w(x,z)),\qquad\tilde\phi^{u/s}(t_*,x,z) := \psi_{u/s}(t_*,w(x,z)),$$
extended homogeneously of degree 0 in $(\sigma,\zeta)$. On the perturbed characteristic set, $(x,z) = e^{F(t_*,w)N}w$
(Lemma 3.3) and $w(x,z) = w$, so $\phi^{u/s}(t_*,x,z) = (\phi_{u/s}+\psi_{u/s})(t_*,w)$, and $\Gamma^{u/s} = \hat\Psi(\{f
= 0\}\cap W^{u/s})$. $V^h = \hat\Psi_*V$ is tangent to $\hat\Psi(W^{u/s})$, as $V$ is to $W^{u/s}$; $\hat W$ and $\mathsf
H_G$ are positive multiples of $V^h$ on the characteristic set (Lemma 3.2 and $\hat Wt_*>0$). The bounds follow by the
chain rule, $w(x,z)$ being smooth and $t_*$-independent. Uniformity: Lemma 3.1 and the explicit dependence of the
constants in Theorem 1.1. $\square$

*Remarks.* (a) $\phi_0^{u/s}$ agrees with I.B's $\phi_{u/s}$ on the stationary characteristic set; off it the two may
differ, which is immaterial for $\Gamma^{u/s}$. (b) The intersections of $\Gamma^{u/s}$ with the stationary face $\{t_* =
\infty\}$ are $\partial\Gamma^{u/s}_{K^+}$, as $\tilde\phi^{u/s}\to0$. (c) $W^u$ at $t_* = 1$ is the stationary unstable
hypersurface, the source's choice ([Hin26c] p. 113: "$\Gamma^u = \bigcup_{s\ge0}e^{sV}(\Gamma^u_0\cap\{\rho_K = 1\})$").

## 4. What this part found

(C$'$1) *[Hin26c] Proposition 6.3's proof* rests on [Hin21] Theorem 2.6 (READ, pp. 13-25 of arXiv:1811.07843v1). That
theorem is stated for a closed manifold, a $C^\infty$ invariant splitting (its (I.3); the relaxation to continuous
splittings is its footnote 8, "not stated in this generality"), and a fixed perturbation; the uniformity in the
perturbation, which the source asserts ("the claimed uniform boundedness ... follows from the uniformity of all estimates
in the proof of [Hin21, Theorem 2.3]"), is a reading of that proof. Theorem 1.1 proves what is needed directly, with
explicit dependence of the constants, from (Γ.1)-(Γ.3) and the tangential half of (K3); II.B's (K3), which states a
continuous splitting, is therefore enough, and the splitting is not used.

(C$'$2) *Change of statement.* The source states $\tilde\phi^{u/s}\in C^{d_0-1,\ell_K}_{cu}$ on all of ${}^{cu}S^*D$.
Here $\tilde\phi^u\in C^{d_0-1}$ and $\tilde\phi^s\in C^{d_0-2}$, on a neighbourhood $U$ of $\partial\Gamma_0$: the
stable hypersurface is obtained as a limit and loses one derivative. $d_0$ is a free parameter, taken large wherever
Proposition 3.4 is used (Part II.D), and only a neighbourhood of the trapped set enters the trapping estimates.

(C$'$3) *The reduction.* The source's graphing of the characteristic set ([Hin26c] p. 113,
"$x_0+\rho_K^{\ell_K}q_0(\rho_K,x_0,x') = 0$" with $q\in C^{d_0}_{cu}([0,1)\times(-1,1)\times\mathbb R^5)$) is Lemma 3.3
here, with the projected field computed (Lemma 3.2); the source's $\mathbb R^5$ is the five-dimensional characteristic
set of Kerr at fibre infinity over $(K^+)^\circ$, which at $n = 4$ is seven-dimensional.

## Sources

[Hin26c] P. Hintz, arXiv:2606.28008v1. READ: pp. 110-113 (section 6, (6.3)-(6.7), Proposition 6.3 and its proof).

[Hin21] P. Hintz, *Normally hyperbolic trapping on asymptotically stationary spacetimes*, Probab. Math. Phys. 2 (2021)
71-126, arXiv:1811.07843v1. READ: pp. 1-2, 7, 13-25 (section 2.3-2.4: assumptions (I.1)-(I.4), (II.1)-(II.2), Theorem
2.3, Remark 2.4, its proof's outline, (2.44), Theorem 2.5, assumptions (I$_F$.1)-(II$_F$.2), Theorem 2.6). No statement
of [Hin21] is used as an input; Theorem 1.1 replaces it.

[HPS77] M. W. Hirsch, C. C. Pugh, M. Shub, *Invariant manifolds*, Lecture Notes in Math. 583 (1977); cited for the
terminology of Remark (a) only.

Part I.B: sections 1.3, 1.5 ((H7), (Γ.1)-(Γ.4), Lemma 1.1). Part II.A: sections 2.1, 8 (Lemma 8.2). Part II.B: sections
1.1 ((K3), (K4)), 2, 5 (Definition 5.1, Lemma 5.2 (d)). Part II.C: section 4 ((4.2)).
