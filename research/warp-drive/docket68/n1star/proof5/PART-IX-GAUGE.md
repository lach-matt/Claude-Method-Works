# Part IX: the linear solution is unique up to a linearised diffeomorphism, n = 4

*Status.* Written (D345); to be read.

Part VIII Remark 2.4 (a) records what Theorem 2.2 there does not assert: that a linearised solution given in another
gauge differs from $\dot g$ by a linearised diffeomorphism. This part proves it, on the Cauchy development of
$\Sigma_{\mathrm{IVP}}$ in the region where $\dot g$ lives, which contains its whole future (Lemma 1.2). Every
linearised vacuum solution whose data agree with $(\dot\gamma,\dot k)$ up to a linearised diffeomorphism is $\dot
g+\mathcal L_Xg$ for a vector field $X$ (Corollary 2.3). So the linear stability of Part VIII holds in every gauge,
modulo a linearised diffeomorphism. Nothing is asserted about the size or decay of $X$ (Remark 2.4).

The argument is the standard one: put the difference into the linearised harmonic gauge by solving a linear wave
equation for $X$, show that the result has vanishing Cauchy data, and conclude by uniqueness for a linear wave
equation. The only inputs beyond Part VIII are the Cauchy problem for normally hyperbolic operators on globally
hyperbolic manifolds ([BGP], READ) and the pointwise identities of Lemma 2.1 (`checks/ix5.py`).

## 0. Setting and conventions

- *The spacetime.* $g := g_{b_0}$ on $M$, the region $\{|x|\ge r_0\}$ in the coordinates $(t,x)$ of III.B, and $M^\circ
  := \{|x|>r_0\}$. $t_{\mathrm{IVP}}$ is III.B Lemma 3.7 (b)'s function and $\Sigma_{\mathrm{IVP}} :=
  t_{\mathrm{IVP}}^{-1}(0)$; $\nu(r)$ is III.K Proposition 1.2's, positive, and $N := \{t_{\mathrm{IVP}}\ge-\nu(|x|)\}$
  as in Part VIII section 0. Put $N^\circ := \{t_{\mathrm{IVP}}>-\nu(|x|)\}\cap M^\circ$ and $\Sigma^\circ :=
  \Sigma_{\mathrm{IVP}}\cap M^\circ\subset N^\circ$.

- *$\dot g$ lives on $N$.* $\Omega_*\cup\mathcal D = N$. Indeed $\Omega_* = \mathrm{cl}_M\{t^\flat_*\ge1\}$ (III.K
  section 0) lies in $N$, as $t_{\mathrm{IVP}}\ge t_*\ge t^\flat_*$ (Part VIII section 0; III.B Lemma 3.7, II.C Lemma
  3.2 (b)); and a point of $N$ has either $t^\flat_*>\hat T+3\ge1$, so lies in $\Omega_*$, or lies in $\mathcal D =
  N\cap\{t^\flat_*\le\hat T+3\}$. So Part VIII Theorem 2.2's $\dot g$ is a smooth symmetric 2-tensor on $N$ with
  $D\mathrm{Ric}(\dot g) = 0$ there.

- *Time orientation.* As in II.B, $dt_*$ is past timelike. $dt_{\mathrm{IVP}}$ is timelike for $g$ on $M$ (III.B Lemma
  3.7 (b)) and past timelike: both $dt_*$ and $dt_{\mathrm{IVP}}$ are $dt-\phi'(|x|)\,d|x|$ with $\beta := \phi'-T'_\mu$
  in $(-1,1]$ (III.B Lemma 3.7's proof), so are all their convex combinations, which are therefore timelike, and the two
  covectors lie in the same cone. So $t_{\mathrm{IVP}}$ is a time function on $M^\circ$ ([BGP] p. 18, as II.F section 1.4
  uses the term): it is strictly increasing along future directed causal curves. Hence $\Sigma^\circ$ is a smooth
  spacelike hypersurface of $M^\circ$, acausal in every open subset of $M^\circ$.

- *Operators.* For a 1-form $w$ and a symmetric 2-tensor $k$: $(\delta_gk)_\mu := -\nabla^\alpha k_{\alpha\mu}$,
  $G_gk := k-\frac12g\,\mathrm{tr}_gk$, $\delta^*_gw := \frac12(\nabla w+(\nabla w)^T)$, so that $\mathcal L_Xg =
  2\delta^*_gX^\flat$, and $\Theta(k) := \delta_gG_gk$, the linearised harmonic gauge 1-form. $D\mathrm{Ric}$ is as in
  Part VIII section 0. Put
  $$L^0 := D\mathrm{Ric}+\delta^*_g\Theta.\tag{0.1}$$

- *Linearised data.* As in Part VIII Lemma 1.1 (1): a symmetric 2-tensor $k$, defined near a piece of
  $\Sigma_{\mathrm{IVP}}$, *induces* the linearised data $(\dot\gamma,\dot K)$, the $s$-derivatives at $s = 0$ of the
  first and second fundamental forms of $\Sigma_{\mathrm{IVP}}$ for $g+sk$, with $K(X,Y) := g(\nabla_X\nu,Y)$ and $\nu$
  the future unit normal. They are linear in $k$ and depend only on its 1-jet at $\Sigma_{\mathrm{IVP}}$; $\dot\gamma$ is
  the restriction of $k$ to $T\Sigma_{\mathrm{IVP}}$.

- *[BGP] (READ), C. Bär, N. Ginoux, F. Pfäffle, arXiv:0806.1036v1, book page numbers.*
  - Normally hyperbolic operators (section 1.5, p. 33): second-order operators with principal symbol
    $-\langle\xi,\xi\rangle\,\mathrm{id}$. As II.F Lemma 1.3's proof records, an operator with principal symbol
    $g^{-1}(\zeta,\zeta)\,\mathrm{Id}$ has $P$ or $-P$ normally hyperbolic; replacing $P$ by $-P$ and $f$ by $-f$ changes
    nothing below.
  - Corollary 3.2.4 (p. 76): on a globally hyperbolic manifold with a smooth spacelike Cauchy hypersurface $S$, a
    smooth $u$ with $Pu = 0$, $u|_S = 0$ and $\nabla_nu|_S = 0$ vanishes. No support condition is imposed.
  - Theorem 3.2.11 (p. 85): there, for compactly supported smooth $u_0,u_1$ on $S$ and $f$ on the manifold, there is a
    unique smooth $u$ with $Pu = f$, $u|_S = u_0$, $\nabla_nu|_S = u_1$, and $\mathrm{supp}\,u\subset J(K)$, $K :=
    \mathrm{supp}\,u_0\cup\mathrm{supp}\,u_1\cup\mathrm{supp}\,f$.
  - In that theorem's proof (pp. 85-86): the manifold is isometric to $\mathbb R\times S$ with metric $-\beta
    dt^2+g_t$, each $S_t := \{t\}\times S$ a smooth spacelike Cauchy hypersurface (Theorem 1.3.13); $([a,b]\times S)\cap
    J(K)$ is compact for compact $K$ (Lemma A.5.4, as applied there); and each slab $(a,b)\times S$ is a globally
    hyperbolic manifold in its own right, to which Corollary 3.2.4 applies.
  - Lemma A.5.9 (p. 176, as II.F section 1.4 reads it): for an acausal hypersurface $S$ of a time-oriented Lorentzian
    manifold, its Cauchy development $D(S)$ is open and globally hyperbolic, and $S$ is a Cauchy hypersurface of $D(S)$.

## 1. The Cauchy problem, and the domain

**Lemma 1.1 ([BGP] Theorem 3.2.11 for data without compact support).** Let $(Y,g)$ be globally hyperbolic, $S$ a smooth
spacelike Cauchy hypersurface, $n$ its future unit normal, and $P$ a normally hyperbolic operator on a vector bundle
$E$. For every $u_0,u_1\in C^\infty(S;E)$ and $f\in C^\infty(Y;E)$ there is a unique $u\in C^\infty(Y;E)$ with $Pu =
f$, $u|_S = u_0$, $\nabla_nu|_S = u_1$.

*Proof.* Uniqueness is [BGP] Corollary 3.2.4. For existence, write $Y = \mathbb R\times S$ with $S = S_0$, $t$ the first
coordinate. Choose a locally finite partition of unity $(\phi_j)$ on $S$ with compact supports, and a locally finite
partition of unity $(\psi_i)$ on $Y$ with compact supports, each $\mathrm{supp}\,\psi_i$ in a slab $[a_i,a_i+1]\times
S$. By [BGP] Theorem 3.2.11 let $u_j$ solve $Pu_j = 0$ with data $(\phi_ju_0,\phi_ju_1)$, and $v_i$ solve $Pv_i =
\psi_if$ with zero data; $\mathrm{supp}\,u_j\subset J(\mathrm{supp}\,\phi_j)$ and $\mathrm{supp}\,v_i\subset
J(\mathrm{supp}\,\psi_i)$.

- *Sources away from $S$.* If $a_i\ge0$, then $v_i = 0$ on $(-R,a_i)\times S$ for every $R>0$: there $Pv_i = 0$ and
  $v_i$ has zero data on $S$, and Corollary 3.2.4 applies on that slab. So $v_i = 0$ where $t<a_i$. Likewise, if
  $a_i+1\le0$, $v_i = 0$ where $t>a_i+1$.

- *Local finiteness.* Let $C\subset[-T,T]\times S$ be compact. $u_j\ne0$ somewhere on $C$ only if
  $\mathrm{supp}\,\phi_j$ meets $J(C)\cap S$, which is compact (Lemma A.5.4 with the slab $[-1,1]$): finitely many $j$.
  If $a_i\ge0$, $v_i\ne0$ somewhere on $C$ only if $a_i\le T$ and $\mathrm{supp}\,\psi_i$ meets $([0,T+1]\times S)\cap
  J(C)$, which is compact: finitely many $i$. The case $a_i+1\le0$ is symmetric. If $a_i<0<a_i+1$, then
  $\mathrm{supp}\,\psi_i\subset[-1,1]\times S$ meets the compact set $([-1,1]\times S)\cap J(C)$: finitely many $i$.

So $u := \sum_ju_j+\sum_iv_i$ is a locally finite sum of smooth sections, $Pu = \sum_i\psi_if = f$, $u|_S =
\sum_j\phi_ju_0 = u_0$ and $\nabla_nu|_S = u_1$. $\square$

**Lemma 1.2 (the domain).** $N^{\mathcal D} := D_{N^\circ}(\Sigma^\circ)$, the Cauchy development of $\Sigma^\circ$ in
$N^\circ$, is open and globally hyperbolic, with smooth spacelike Cauchy hypersurface $\Sigma^\circ$. It contains
$N^\circ\cap\{t_{\mathrm{IVP}}\ge0\}$. More generally, for every open $U\subset N^\circ$, $D_U(\Sigma_{\mathrm{IVP}}\cap
U)$ is open and globally hyperbolic with smooth spacelike Cauchy hypersurface $\Sigma_{\mathrm{IVP}}\cap U$.

*Proof.* $\Sigma_{\mathrm{IVP}}\cap U$ is a smooth hypersurface of $U$, as $dt_{\mathrm{IVP}}\ne0$, spacelike and
acausal in $U$ (section 0). [BGP] Lemma A.5.9 gives the first and last assertions. Let $p\in N^\circ$ with
$t_{\mathrm{IVP}}(p)\ge0$.

- *A compact set.* Along a past directed causal curve from $p$ in $M^\circ$:
  - $t_{\mathrm{IVP}}$ decreases (section 0), and $t = t_{\mathrm{IVP}}+\psi_{\mathrm{IVP}}(|x|)$ with
    $0\le\psi_{\mathrm{IVP}}\le C_3 := \max\psi_{\mathrm{IVP}}$, finite as $\psi_{\mathrm{IVP}}$ is constant on
    $[R_3,\infty)$ (III.B Lemma 3.7 (b) and its proof).
  - $|x|$ stays $\ge\min(|x(p)|,r^\natural)$, $r^\natural>r_0$: $dr$ is future timelike for $g$ on $\{r_0\le r\le
    r^\natural\}$ (II.C Lemma 3.2 (1) at $h = 0$), so $r$ strictly increases towards the past there.
  - On $\{|x|\ge3R_1\}$, $d(t+|x|)$ is past timelike. By III.B (3.5), $g^{-1} = \bar
    g^{-1}-\mu_0|x|^{-2}(\partial_t+\partial_{|x|})^{\otimes2}$ there, so $g^{-1}(d(t+|x|),d(t+|x|)) =
    -4\mu_0|x|^{-2}<0$. With $dt_* = dt-\psi'd|x|$, $g^{-1}(d(t+|x|),dt_*) = -1-\psi'-2\mu_0|x|^{-2}(1-\psi')<0$, as
    $-1<\psi'<1$ there (III.B (3.6): $\psi' = 1-8\mu_0\rho^{-2}$ for $\rho\ge3R_1$). So $d(t+|x|)$ and $dt_*$ lie in
    the same cone, and $t+|x|$ decreases towards the past there.

  Let $q\in J^-_{M^\circ}(p)\cap\{t_{\mathrm{IVP}}\ge0\}$ with $|x(q)|\ge3R_1$, reached along a past directed causal
  curve from $p$. Its last segment in $\{|x|\ge3R_1\}$ starts at $p$ or at a point $q_0$ with $|x(q_0)| = 3R_1$ and
  $t(q_0)\le t_{\mathrm{IVP}}(p)+C_3$, so $t(q)+|x(q)|\le B_p := \max\big(t(p)+|x(p)|,t_{\mathrm{IVP}}(p)+C_3+3R_1\big)$.
  As $t(q)\ge t_{\mathrm{IVP}}(q)\ge0$, $|x(q)|\le B_p$. Hence
  $$J^-_{M^\circ}(p)\cap\{t_{\mathrm{IVP}}\ge0\}\subset L_p := \{0\le t_{\mathrm{IVP}}\le t_{\mathrm{IVP}}(p),\
  \min(|x(p)|,r^\natural)\le|x|\le\max(B_p,3R_1)\},$$
  a compact subset of $N^\circ$ (closed and bounded in $(t,x)$, with $t\in[0,t_{\mathrm{IVP}}(p)+C_3]$; $|x|>r_0$ and
  $t_{\mathrm{IVP}}\ge0>-\nu$ on it).

- *Every inextendible causal curve through $p$ meets $\Sigma^\circ$.* Let $\gamma$ be one, in $N^\circ$. If
  $t_{\mathrm{IVP}}>0$ along its whole past half, that half lies in $L_p$. II.F Lemma 1.3's proof shows that a past
  inextendible causal curve along which a time function is bounded below, and which lies in a compact set, extends
  continuously to a past end point: its tangent, normalised by $dt_{\mathrm{IVP}} = 1$, ranges in a compact set over
  $L_p$, so the curve is Lipschitz in $t_{\mathrm{IVP}}$ and converges in $L_p\subset N^\circ$. That contradicts
  inextendibility in $N^\circ$. So $t_{\mathrm{IVP}}$ reaches 0 on $\gamma$, and $\gamma$ meets $\Sigma^\circ$, once by
  acausality. Hence $p\in N^{\mathcal D}$. $\square$

## 2. The comparison

**Lemma 2.1 (pointwise identities).** At the Ricci-flat $g$:

(a) $2L^0$ and $2\delta_gG_g\delta^*_g$ have principal part $-g^{\alpha\beta}\partial_\alpha\partial_\beta\otimes
\mathrm{id}$, so principal symbol $g^{-1}(\zeta,\zeta)\,\mathrm{Id}$ (`ix5.py` X1, X2: in local coordinates the
principal parts are the flat ones with $\eta$ replaced by $g$, the Christoffel symbols entering only lower order).

(b) $D\mathrm{Ric}(\mathcal L_Xg) = 0$ for every smooth vector field $X$: with $\phi_s$ its local flow,
$\mathrm{Ric}(\phi_s^*g) = \phi_s^*\mathrm{Ric}(g) = 0$, and $\frac{d}{ds}\phi_s^*g|_{s=0} = \mathcal L_Xg$; the
derivative is pointwise (`ix5.py` X6 at Tangherlini for $X$ in the $(t,r)$ plane).

(c) If $k = 0$ on $\Sigma_{\mathrm{IVP}}$, then $\dot K = \frac12(\nabla_\nu k)|_{T\Sigma_{\mathrm{IVP}}}$. Indeed
$\dot\nu = 0$ (it is linear in $k(\nu,\cdot)$), the variation of $g$ multiplies $k = 0$, and the variation of $\nabla$ is
$C(X,Y) = \frac12g^{-1}\big(\nabla_Xk(Y,\cdot)+\nabla_Yk(X,\cdot)-\nabla_\cdot k(X,Y)\big)$, whose tangential
derivatives vanish on $\Sigma_{\mathrm{IVP}}$; so $\dot K(e_i,e_j) = g(C(e_i,\nu),e_j) = \frac12(\nabla_\nu k)(e_i,e_j)$
(`ix5.py` X3, on a curved metric with $g_{0i}\ne0$).

(d) If $k = 0$ on $\Sigma_{\mathrm{IVP}}$, then in an orthonormal frame $(\nu,e_i)$ there, with $k' := \nabla_\nu k$:
$\Theta(k)(e_j) = k'(\nu,e_j)$ and $\Theta(k)(\nu) = \frac12k'(\nu,\nu)+\frac12\sum_ik'(e_i,e_i)$ (only normal
derivatives survive, $g^{\nu\nu} = -1$; `ix5.py` X4).

(e) If $X = 0$ on $\Sigma_{\mathrm{IVP}}$ and $\nabla_\nu X = Y$ there, then on $\Sigma_{\mathrm{IVP}}$, as
$\nabla_{e_i}X = 0$ and $(\mathcal L_Xg)(a,b) = g(\nabla_aX,b)+g(a,\nabla_bX)$: $(\mathcal L_Xg)(e_i,e_j) = 0$,
$(\mathcal L_Xg)(\nu,e_j) = g(Y,e_j)$ and $(\mathcal L_Xg)(\nu,\nu) = 2g(Y,\nu)$. For $k$ with $k(e_i,e_j) = 0$ on
$\Sigma_{\mathrm{IVP}}$, the vector $Y := \sum_jk(\nu,e_j)e_j-\frac12k(\nu,\nu)\nu$, i.e. $Y^\flat =
k(\nu,\cdot)+\frac12k(\nu,\nu)\nu^\flat$, gives $\mathcal L_Xg = k$ on $\Sigma_{\mathrm{IVP}}$ (`ix5.py` X5).

(f) If $X = 0$ on $\Sigma_{\mathrm{IVP}}$, then $\mathcal L_Xg$ induces zero linearised data. Its flow fixes
$\Sigma_{\mathrm{IVP}}$ pointwise, so $\phi_s$ is an isometry from $(M,\phi_s^*g)$ to $(M,g)$ that is the identity on
$\Sigma_{\mathrm{IVP}}$ and preserves the future normal for small $|s|$. So $\phi_s^*g$ induces exactly $(\gamma,K)$ on
$\Sigma_{\mathrm{IVP}}$ for every small $s$. The induced data are smooth functions of the 1-jet of the metric at
$\Sigma_{\mathrm{IVP}}$, whose $s$-derivative at 0 is that of $\mathcal L_Xg$. So the derivative of the data, which is
the data induced by $\mathcal L_Xg$, vanishes. $\square$

**Theorem 2.2 (linearised vacuum solutions with gauge-equivalent data are gauge-equivalent).** Let $U\subset N^\circ$ be
open, $\Sigma_U := \Sigma_{\mathrm{IVP}}\cap U$, and $\Omega' := D_U(\Sigma_U)$. Let $k$ be a smooth symmetric 2-tensor
on $\Omega'$ with $D\mathrm{Ric}(k) = 0$, inducing on $\Sigma_U$ the linearised data that $\mathcal L_Zg$ induces, for a
smooth vector field $Z$ on a neighbourhood of $\Sigma_U$ in $\Omega'$ ($Z = 0$: zero data). Then there is a smooth
vector field $X$ on $\Omega'$ with
$$k = \mathcal L_Xg\quad\text{on }\Omega'.$$
$X$ is unique up to a Killing field of $g$ on $\Omega'$.

*Proof.* $\Omega'$ is globally hyperbolic with smooth spacelike Cauchy hypersurface $\Sigma_U$ (Lemma 1.2). Uniqueness
up to Killing fields is $\mathcal L_{X-X'}g = 0$.

*Step 0 (zero data).* Let $\psi\in C^\infty(\Omega')$ equal 1 near $\Sigma_U$ and vanish outside the neighbourhood
where $Z$ is defined ($\Sigma_U$ is closed in $\Omega'$). $k_0 := k-\mathcal L_{\psi Z}g$ has $D\mathrm{Ric}(k_0) = 0$
(Lemma 2.1 (b)), and it induces zero data: those of $\mathcal L_{\psi Z}g$ and $\mathcal L_Zg$ agree, as $\psi Z = Z$
near $\Sigma_U$. If $k_0 = \mathcal L_{X_0}g$, then $k = \mathcal L_{X_0+\psi Z}g$. So assume $Z = 0$.

*Step 1 (the gauge vector field).* Zero data means $k(e_i,e_j) = 0$ on $\Sigma_U$ ($\dot\gamma = 0$) and $\dot K =
0$. Let $Y$ be Lemma 2.1 (e)'s vector field on $\Sigma_U$, smooth, as $Y^\flat = k(\nu,\cdot)+\frac12k(\nu,\nu)
\nu^\flat$. By Lemma 1.1, with $P := 2\delta_gG_g\delta^*_g$ or its negative (Lemma 2.1 (a)), there is a smooth 1-form
$w$ on $\Omega'$ with
$$2\delta_gG_g\delta^*_gw = \Theta(k),\qquad w|_{\Sigma_U} = 0,\qquad\nabla_\nu w|_{\Sigma_U} = Y^\flat.$$
Put $X := w^\sharp$. Then $\Theta(\mathcal L_Xg) = \Theta(2\delta^*_gw) = \Theta(k)$, and $X = 0$, $\nabla_\nu X = Y$
on $\Sigma_U$.

*Step 2 (the difference has vanishing Cauchy data).* Let $h := k-\mathcal L_Xg$.

- $h = 0$ on $\Sigma_U$, by Lemma 2.1 (e).

- $h$ induces zero linearised data: $k$ does by assumption, and $\mathcal L_Xg$ does by Lemma 2.1 (f). So by Lemma 2.1
  (c), $(\nabla_\nu h)(e_i,e_j) = 2\dot K(e_i,e_j) = 0$.

- $\Theta(h) = 0$ on $\Omega'$ by Step 1. At $\Sigma_U$, Lemma 2.1 (d) with $h' := \nabla_\nu h$ and $h'(e_i,e_i) = 0$
  gives $h'(\nu,e_j) = 0$ and $h'(\nu,\nu) = 0$.

So $h|_{\Sigma_U} = 0$ and $\nabla_\nu h|_{\Sigma_U} = 0$.

*Step 3 (it vanishes).* $D\mathrm{Ric}(h) = D\mathrm{Ric}(k)-D\mathrm{Ric}(\mathcal L_Xg) = 0$ (Lemma 2.1 (b)), and
$\Theta(h) = 0$, so $L^0h = 0$ by (0.1). $2L^0$ or its negative is normally hyperbolic (Lemma 2.1 (a)). [BGP] Corollary
3.2.4 on $\Omega'$ gives $h = 0$. $\square$

**Corollary 2.3 (Part VIII's solution in any gauge).** Let $(\dot\gamma,\dot k)$, $\dot g$, $S'$, $\dot b$ and $U'$ be
as in Part VIII Theorem 2.2, $U\subset N^\circ$ open and $\Omega' := D_U(\Sigma_U)$. Let $\dot g'$ be a smooth
symmetric 2-tensor on $\Omega'$ with $D\mathrm{Ric}(\dot g') = 0$ that induces on $\Sigma_U$ the data
$(\dot\gamma,\dot k)$ plus those of $\mathcal L_Zg$, for a smooth $Z$ near $\Sigma_U$. Then
$$\dot g' = \dot g+\mathcal L_Xg\quad\text{on }\Omega'$$
for a smooth vector field $X$ on $\Omega'$. In particular, where $\chi_K = 1$ in $\Omega'$,
$$\dot g'-\mathcal L_Xg-\partial_bg_b|_{b=b_0}(\dot b) = h_{b_0,\mathrm{rem}}(q')+h',$$
with the rate of Part VIII (2.3): every linearised vacuum solution with these data settles, up to a linearised
diffeomorphism, to a linearised Myers-Perry metric. With $U = N^\circ$, $\Omega'$ contains $N^\circ\cap
\{t_{\mathrm{IVP}}\ge0\}$ (Lemma 1.2).

*Proof.* $\dot g$ is smooth on $N\supset\Omega'$ with $D\mathrm{Ric}(\dot g) = 0$ (section 0; Part VIII Theorem 2.2
(1)). Near $\Sigma_{\mathrm{IVP}}$ in $N$, $\dot g = \dot h+\dot g_{S'}$ with $\dot g_{S'} = -\mathcal L_{V(S')}g$:
the set $\mathcal D' = \mathcal D\setminus\{t^\flat_*\ge\hat T+\frac74\}$ of Part VIII Theorem 2.2 (2) contains
$N\cap\{t_{\mathrm{IVP}}<\hat T+\frac74\}$, as $t^\flat_*\le t_*\le t_{\mathrm{IVP}}$ where $t^\flat_*$ is defined. $\dot
h$ induces $(\dot\gamma,\dot k)$ (Part VIII Lemma 1.1 (1), Proposition 1.2's data). So $k := \dot g'-\dot g$ has
$D\mathrm{Ric}(k) = 0$ on $\Omega'$ and induces the data of $\mathcal L_{Z+V(S')}g$. Theorem 2.2 gives $k = \mathcal
L_Xg$. The second display is Part VIII (2.2) with $\dot g = \dot g'-\mathcal L_Xg$. $\square$

**Remark 2.4 (what is and is not asserted).** (a) The statement is the linear counterpart of the gauge comparison that
Part VII Remark 4.1 leaves to the nonlinear theory; it is proved here for the linearisation only. (b) Nothing is
asserted about the size or decay of $X$: $X$ solves a linear wave equation with source $\Theta(k)$ and its own Cauchy
data, and its behaviour at $\mathscr I^+$ and $K^+$ depends on the gauge of $\dot g'$. So the paper's section 8.2
routes keep their status: a solution in the Regge-Wheeler-type gauge or in the harmonic gauge with the same data is
$\dot g+\mathcal L_Xg$ on its Cauchy development (Corollary 2.3), which settles modulo $\mathcal L_Xg$; the decay *in
those gauges* is the decay of $\mathcal L_Xg$ there, which is what the deduced routes argue and is not proved here.
(c) In the class of Part VII, if $\dot g'$ and $Z$ are $G$-invariant, $X$ may be taken $G$-invariant: average Step 1's
data and source over $G$, which commutes with $\Theta$, $\delta^*_g$ and the Cauchy problem (Part VIII Corollary 2.3's
proof), and Lemma 1.1's uniqueness.

## 3. Findings, labels and sources

- (IX1) $\Omega_*\cup\mathcal D = N$: Part VIII's $\dot g$ lives on all of $N$ (section 0). Recorded because Part VIII
  states its domain as $\Omega_*\cup\mathcal D$.

- (IX2) [BGP] Theorem 3.2.11 is stated for compactly supported data; the extension to smooth data without support
  conditions (Lemma 1.1) is written out, using only Corollary 3.2.4, Theorem 3.2.11 and the facts used in its proof.

- (IX3) The domain of the comparison is a Cauchy development, $D_U(\Sigma_U)$; for $U = N^\circ$ it contains the
  whole future $N^\circ\cap\{t_{\mathrm{IVP}}\ge0\}$ (Lemma 1.2), where the settling statement lives.

Labels: proved here from the cited parts and [BGP] (READ); Lemma 2.1's identities are derived in the text and computed
in `checks/ix5.py` (X1-X6, with controls).

Sources: Part VIII (PART-VIII-LINEAR.md) section 0, Lemma 1.1, Proposition 1.2, Theorem 2.2, Corollary 2.3, Remark 2.4;
III.B (PART-III-B-FAMILY.md) (3.5), (3.6), Lemma 3.7; II.C (PART-II-C-OPERATORS.md) Lemma 3.2; II.F (PART-II-F-IOTA.md)
section 1.4, Lemma 1.3 and its proof; III.K (PART-III-K-NONLINEAR.md) section 0 and Proposition 1.2; [BGP]
arXiv:0806.1036v1, section 1.5 (p. 33), Corollary 3.2.4 (p. 76), Theorem 3.2.11 with its proof (pp. 85-86), Lemma
A.5.9 (p. 176).
