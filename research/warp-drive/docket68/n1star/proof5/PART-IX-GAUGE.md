# Part IX: the linear solution is unique up to a linearised diffeomorphism, n = 4

*Status.* Written (D345). Verified (D347): verifier 162 found no blocking or major gap; its minor findings M1-M4 and
nits N1-N5 are seated (finding (IX4)). Repaired (D610): a later reading found that $\nu$ vanishes near $\{r = r_0\}$, so
that $\Sigma_{\mathrm{IVP}}$ is there the boundary of the region where $\dot g$ lives; the comparison is now posed on the
future half of a Cauchy development that extends past $\Sigma_{\mathrm{IVP}}$ (finding (IX5)). Repair read (D611: no
major gap; m1, m2, n1-n6 seated). Proved (D617): a full line-by-line re-read found no major gap; its minor findings m1,
m2 and nits n1-n8 are seated (finding (IX6)).

Part VIII Remark 2.4 (a) records what Theorem 2.2 there does not assert: that a linearised solution given in another
gauge differs from $\dot g$ by a linearised diffeomorphism. This part proves it, on the whole future of
$\Sigma_{\mathrm{IVP}}$ in $\{r>r_0\}$ (Lemma 1.2), the future half of a Cauchy development of $\Sigma_{\mathrm{IVP}}$.
Every linearised vacuum solution ($D\mathrm{Ric} = 0$) given on the future half $\Omega'_+$ of a Cauchy development,
smooth up to the initial surface, whose data agree with $(\dot\gamma,\dot k)$ up to a linearised diffeomorphism is
$\dot g+\mathcal L_Xg$ there for a vector field $X$ (Corollary 2.3). So the linear stability of Part VIII holds in
every gauge, modulo a linearised diffeomorphism. Nothing is asserted about the size or decay of $X$ (Remark 2.4).

The argument is the standard one: put the difference into the linearised harmonic gauge by solving a linear wave
equation for $X$, show that the result has vanishing Cauchy data, and conclude by uniqueness for a linear wave
equation. The only inputs beyond Part VIII are the Cauchy problem for normally hyperbolic operators on globally
hyperbolic manifolds ([BGP], READ) and the pointwise identities of Lemma 2.1 (`checks/ix5.py`).

## 0. Setting and conventions

- *The spacetime.* $g := g_{b_0}$ on $M$, the region $\{|x|\ge r_0\}$ in the coordinates $(t,x)$ of III.B, and $M^\circ
  := \{|x|>r_0\}$. $t_{\mathrm{IVP}}$ is III.B Lemma 3.7 (b)'s function and $\Sigma_{\mathrm{IVP}} :=
  t_{\mathrm{IVP}}^{-1}(0)$; $\nu(r)$ is III.K Proposition 1.2's, smooth and non-decreasing with $\nu = 0$ on
  $[0,R_\nu]$, $R_\nu := \frac12(r_0+R)$ (III.K Proposition 1.2's statement), so $\nu\ge0$ but $\nu$ is not positive; and
  $N := \{t_{\mathrm{IVP}}\ge-\nu(|x|)\}$ as in Part VIII section 0. On $\{|x|\le R_\nu\}$, then, $N$ ends at
  $\Sigma_{\mathrm{IVP}}$, which is there part of its boundary, and $\dot g$ is not defined to its past. So the
  comparison is posed in a region that extends past $\Sigma_{\mathrm{IVP}}$, where only $g$ is used, and the tensors
  compared live on its future half. Put
  $$U^\sharp := M^\circ\cap\{t_{\mathrm{IVP}}>-1\},\qquad\Sigma^\circ := \Sigma_{\mathrm{IVP}}\cap M^\circ\subset
  U^\sharp,\qquad N^+ := M^\circ\cap\{t_{\mathrm{IVP}}\ge0\}\subset N,$$
  the inclusion as $\nu\ge0$. For an open $U\subset U^\sharp$ put $\Sigma_U := \Sigma_{\mathrm{IVP}}\cap U$ and $U_+ :=
  U\cap\{t_{\mathrm{IVP}}\ge0\}$.

- *Smooth up to $\Sigma_U$.* $U_+$ is a manifold with boundary $\Sigma_U$, as $dt_{\mathrm{IVP}}\ne0$. A tensor on $U_+$
  is *smooth up to $\Sigma_U$* if it is smooth on $U\cap\{t_{\mathrm{IVP}}>0\}$ and, in coordinates
  $(t_{\mathrm{IVP}},y)$ near $\Sigma_U$, every derivative of its components extends continuously to $\Sigma_U$. Such a
  tensor is the restriction to $U_+$ of a smooth tensor on an open neighbourhood of $U_+$ in $U$ (Seeley's extension
  theorem [See64] in each chart $\{t_{\mathrm{IVP}}\ge0\}$, patched with a partition of unity subordinate to a cover of
  $\Sigma_U$ by such charts). The restriction of Part VIII's $\dot g$ to $N^+$ is smooth up to $\Sigma^\circ$. Where
  $\nu>0$, $\Sigma^\circ$ lies in the interior of $N$, where $\dot g$ is smooth. Where $\nu = 0$, $\Sigma^\circ$ is part
  of the boundary of $N$. Such points have $r\le R_\nu<r_1$: $R_\nu = \frac12(r_0+R)$ with $R\le5R_1$, $\phi_S$ being
  the identity on $\{|x|\le5R_1\}$, and $r_1\ge R_6\ge R_3>5R_1$, as $\psi_{\mathrm{IVP}}' = \psi'>0$ at $5R_1$ and
  $\psi_{\mathrm{IVP}}' = 0$ on $[R_3,\infty)$ (III.B Lemma 3.7 (b); III.K section 0). So of Part VIII's cover of
  $\mathcal D$ only the compact part $\mathcal K$ reaches them: $\Omega_{\mathrm{ext},r_1}\subset\{r\ge r_1\}$, and the
  slab $\mathcal S$ lies in $\{|x|>R_9\}$, $R_9\ge R_3>5R_1>R_\nu$, and does not meet $\Sigma_{\mathrm{IVP}}$, as
  $t_{\mathrm{IVP}}\ge\frac r4>0$ on $\mathcal S$ (III.K Proposition 1.2's proof, line 178); a half-ball
  $\{t_{\mathrm{IVP}}\ge0\}$ about each such point lies in $\mathcal K$ (these readings checked by the verifier of
  D610's repair and, with the slab's clause restated, by the re-read of D617). There $\dot g = \dot h+\dot g_{S'}$
  (Part VIII Theorem 2.2 (2)), $\dot g_{S'} = -\mathcal L_{V(S')}g$ is smooth across, and $\dot h$ lies in every $H^k$
  of the interior of $\mathcal K$, bounded up to $\Sigma_{\mathrm{IVP}}$, where Part VIII Proposition 1.2's proof
  solves it by energy estimates ("bounded in every $H^k$ by finitely many norms of the data"). In a chart
  $\{t_{\mathrm{IVP}}\ge0\}$ near such a point, $H^k$ for every $k$ gives every derivative continuous up to
  $\Sigma^\circ$ (Sobolev embedding on a half-space, through its extension operator). Deduced from those readings;
  neither Part states smoothness up to the boundary in these words.

- *$\dot g$ lives on $N$.* $\Omega_*\cup\mathcal D = N$. Indeed $\Omega_* = \mathrm{cl}_M\{t^\flat_*\ge1\}$ (III.K
  section 0) lies in $N$, as $t_{\mathrm{IVP}}\ge t_*\ge t^\flat_*$ (Part VIII section 0; III.B Lemma 3.7, II.C Lemma
  3.2 (b)); and a point of $N$ has either $t^\flat_*>\hat T+3\ge1$, so lies in $\Omega_*$, or lies in $\mathcal D =
  N\cap\{t^\flat_*\le\hat T+3\}$, with III.K section 0's convention that $\{t^\flat_*\le c\}$ is the
  complement of $\{t^\flat_*>c\}$, so that points where $t^\flat_*$ is undefined lie in it. So Part VIII Theorem
  2.2's $\dot g$ is a smooth symmetric 2-tensor on the interior of $N$, smooth up to $\Sigma^\circ$ (above), with
  $D\mathrm{Ric}(\dot g) = 0$ there.

- *Time orientation.* As in II.B, $dt_*$ is past timelike. $dt_{\mathrm{IVP}}$ is timelike for $g$ on $M$ (III.B Lemma
  3.7 (b)) and past timelike: both $dt_*$ and $dt_{\mathrm{IVP}}$ are $dt-\phi'(|x|)\,d|x|$ with $\beta := \phi'-T'_\mu$
  in $(-1,1]$ (III.B Lemma 3.7's proof), so are all their convex combinations, which are therefore timelike, and the two
  covectors lie in the same cone. So $t_{\mathrm{IVP}}$ is a time function on $M^\circ$ in the sense II.F section 1.4
  uses: it is strictly increasing along future directed causal curves (the property [BGP] p. 24 records of a Cauchy
  time-function; $t_{\mathrm{IVP}}$ is not claimed to be one). Hence $\Sigma^\circ$ is a smooth spacelike hypersurface
  of $M^\circ$, acausal in every open subset of $M^\circ$.

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
    dt^2+g_t$, each $S_t := \{t\}\times S$ a smooth spacelike Cauchy hypersurface (Theorem 1.3.13), the given $S$
    corresponding to $\{0\}\times S$; $([a,b]\times S)\cap J(K)$ is compact for compact $K$ (Corollary A.5.4, p. 174, as
    applied there); and each slab $(a,b)\times S$ is a globally hyperbolic manifold in its own right, to which Corollary
    3.2.4 applies.
  - Lemma A.5.9 (p. 176, as II.F section 1.4 reads it): for an acausal hypersurface $S$ of a time-oriented Lorentzian
    manifold, its Cauchy development $D(S)$ is open and globally hyperbolic, and $S$ is a Cauchy hypersurface of $D(S)$.
  - In the proof of Proposition 3.2.5 (p. 81): a section smooth on the whole manifold (there $P\hat u-f$) and vanishing
    to infinite order along $S$ is restricted to one side of $S$ and extended by $0$. Theorem 2.2's Step 3 below uses the
    device
    for a section given on one side only, and shows the zero extension smooth directly.
  - Connectedness. [BGP]'s globally hyperbolic manifolds are connected (Definition 1.3.8, p. 23). A Cauchy development
    below may have several connected components, and every statement taken from [BGP] is applied on each component
    $C$, with Cauchy hypersurface $S\cap C$: components of an open set are open and closed in it, so an inextendible
    causal curve of $C$ is one of $D(S)$ and meets $S$, and it does so in $C$.

## 1. The Cauchy problem, and the domain

**Lemma 1.1 ([BGP] Theorem 3.2.11 for data without compact support).** Let $(Y,g)$ be globally hyperbolic, $S$ a smooth
spacelike Cauchy hypersurface, $n$ its future unit normal, and $P$ a normally hyperbolic operator on a vector bundle
$E$, $\nabla$ the connection on $E$ with which [BGP] Theorem 3.2.11 poses the data. For every $u_0,u_1\in C^\infty(S;E)$
and $f\in C^\infty(Y;E)$ there is a unique $u\in C^\infty(Y;E)$ with $Pu = f$, $u|_S = u_0$, $\nabla_nu|_S = u_1$. (In
every use below $u_0 = 0$, and then $\nabla_nu|_S$ does not depend on the connection.)

*Proof.* Uniqueness is [BGP] Corollary 3.2.4. For existence, write $Y = \mathbb R\times S$ with $S = S_0$, $t$ the first
coordinate. Choose a locally finite partition of unity $(\phi_j)$ on $S$ with compact supports, and a locally finite
partition of unity $(\psi_i)$ on $Y$ with compact supports, each $\mathrm{supp}\,\psi_i$ in a slab $[a_i,a_i+1]\times
S$. By [BGP] Theorem 3.2.11 let $u_j$ solve $Pu_j = 0$ with data $(\phi_ju_0,\phi_ju_1)$, and $v_i$ solve $Pv_i =
\psi_if$ with zero data; $\mathrm{supp}\,u_j\subset J(\mathrm{supp}\,\phi_j)$ and $\mathrm{supp}\,v_i\subset
J(\mathrm{supp}\,\psi_i)$.

- *Sources away from $S$.* If $a_i>0$, then $v_i = 0$ on $(-R,a_i)\times S$ for every $R>0$: that slab contains
  $S = S_0$, there $Pv_i = 0$ and $v_i$ has zero data on $S$, and Corollary 3.2.4 applies on it. So $v_i = 0$ where
  $t<a_i$. Likewise, if $a_i+1<0$, $v_i = 0$ where $t>a_i+1$. The remaining $i$ have $-1\le a_i\le0$ (verifier 162's
  M1: the cases $a_i = 0$ and $a_i+1 = 0$ are among them).

- *Local finiteness.* Let $C\subset[-T,T]\times S$ be compact. $u_j\ne0$ somewhere on $C$ only if
  $\mathrm{supp}\,\phi_j$ meets $J(C)\cap S$, which is compact (Corollary A.5.4, p. 174, with $S = \{0\}\times S$, as
  applied in Theorem 3.2.11's proof): finitely many $j$. If $a_i>0$, $v_i\ne0$ somewhere on $C$ only if $a_i\le T$ and
  $\mathrm{supp}\,\psi_i$ meets $([0,T+1]\times S)\cap J(C)$, which is compact: finitely many $i$. The case $a_i+1<0$ is
  symmetric. If $-1\le a_i\le0$, then $\mathrm{supp}\,\psi_i\subset[-1,1]\times S$ meets the compact set $([-1,1]\times
  S)\cap J(C)$: finitely many $i$.

So $u := \sum_ju_j+\sum_iv_i$ is a locally finite sum of smooth sections, $Pu = \sum_i\psi_if = f$, $u|_S =
\sum_j\phi_ju_0 = u_0$ and $\nabla_nu|_S = u_1$. $\square$

**Lemma 1.2 (the domain).** For every open $U\subset U^\sharp$, $D_U(\Sigma_U)$, the Cauchy development of $\Sigma_U$
in $U$, is open and globally hyperbolic (on each component, section 0), with smooth spacelike Cauchy hypersurface
$\Sigma_U$. $\Omega^\sharp := D_{U^\sharp}(\Sigma^\circ)$ contains $N^+ = M^\circ\cap\{t_{\mathrm{IVP}}\ge0\}$, so that
$\Omega^\sharp_+ := \Omega^\sharp\cap\{t_{\mathrm{IVP}}\ge0\} = N^+$.

*Proof.* $\Sigma_U$ is a smooth hypersurface of $U$, as $dt_{\mathrm{IVP}}\ne0$, spacelike and acausal in $U$ (section
0). [BGP] Lemma A.5.9 gives the first assertion. Let $p\in M^\circ$ with $t_{\mathrm{IVP}}(p)\ge0$; then $p\in
U^\sharp$.

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
  a compact subset of $U^\sharp$ (closed and bounded in $(t,x)$, with $t\in[0,t_{\mathrm{IVP}}(p)+C_3]$; $|x|>r_0$ and
  $t_{\mathrm{IVP}}\ge0>-1$ on it).

- *Every inextendible causal curve through $p$ meets $\Sigma^\circ$.* Let $\gamma$ be one, in $U^\sharp$. If
  $t_{\mathrm{IVP}}>0$ along its whole past half, that half lies in $L_p$. II.F Lemma 1.3's proof shows that a past
  inextendible causal curve along which a time function is bounded below, and which lies in a compact set, extends
  continuously to a past end point: its tangent, normalised by $dt_{\mathrm{IVP}} = 1$, ranges in a compact set over
  $L_p$, so the curve is Lipschitz in $t_{\mathrm{IVP}}$ and converges in $L_p\subset U^\sharp$. That contradicts
  inextendibility in $U^\sharp$. So $t_{\mathrm{IVP}}$ reaches 0 on $\gamma$, and $\gamma$ meets $\Sigma^\circ$, once by
  acausality. Hence $p\in\Omega^\sharp$, and $N^+\subset\Omega^\sharp_+$; the reverse inclusion holds as $\Omega^\sharp
  \subset U^\sharp\subset M^\circ$. $\square$

The region $U^\sharp$ reaches to $t_{\mathrm{IVP}} = -1$ only so that $\Sigma^\circ$ lies inside it; nothing below uses
$\Omega^\sharp\cap\{t_{\mathrm{IVP}}<0\}$ beyond the background $g$, the extension of a source in Theorem 2.2's Step 1
with that step's solution $w$ and field $X := w^\sharp$, which live on all of $\Omega'$, and the zero extension in its
Step 3.

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
the data induced by $\mathcal L_Xg$, vanishes (`ix5.py` X7). $\square$

**Theorem 2.2 (linearised vacuum solutions with gauge-equivalent data are gauge-equivalent).** Let $U\subset U^\sharp$
be open, $\Omega' := D_U(\Sigma_U)$ and $\Omega'_+ := \Omega'\cap\{t_{\mathrm{IVP}}\ge0\}$, a manifold with boundary
$\Sigma_U$. Let $k$ be a symmetric 2-tensor on $\Omega'_+$, smooth up to $\Sigma_U$ (section 0), with $D\mathrm{Ric}(k)
= 0$, inducing on $\Sigma_U$ the linearised data that $\mathcal L_Zg$ induces, for a vector field $Z$ on a
neighbourhood of $\Sigma_U$ in $\Omega'_+$, smooth up to $\Sigma_U$ ($Z = 0$: zero data). Then there is a vector field
$X$ on $\Omega'_+$, smooth up to $\Sigma_U$, with
$$k = \mathcal L_Xg\quad\text{on }\Omega'_+.$$
$X$ is unique up to a Killing field of $g$ on $\Omega'_+$.

*Proof.* $\Omega'$ is globally hyperbolic with smooth spacelike Cauchy hypersurface $\Sigma_U$ (Lemma 1.2), and the
data of a tensor smooth up to $\Sigma_U$ are defined from one side (Part VIII Lemma 1.1 allows this). Uniqueness up to
Killing fields is $\mathcal L_{X-X'}g = 0$.

*Step 0 (zero data).* Let $W = \tilde W\cap\Omega'_+$, $\tilde W$ open in $\Omega'$, be the neighbourhood of
$\Sigma_U$ where $Z$ is defined, and $\tilde\psi\in C^\infty(\Omega')$ equal 1 near $\Sigma_U$ with
$\mathrm{supp}_{\Omega'}\tilde\psi\subset\tilde W$ (smooth Urysohn: $\Sigma_U$ is closed in $\Omega'$); $\psi :=
\tilde\psi|_{\Omega'_+}$. $k_0 := k-\mathcal L_{\psi Z}g$ has $D\mathrm{Ric}(k_0) = 0$ (Lemma 2.1 (b)), and it induces
zero data: those of $\mathcal L_{\psi Z}g$ and $\mathcal L_Zg$ agree, as $\psi Z = Z$ near $\Sigma_U$. If $k_0 =
\mathcal L_{X_0}g$, then $k = \mathcal L_{X_0+\psi Z}g$. So assume $Z = 0$.

*Step 1 (the gauge vector field).* Zero data means $k(e_i,e_j) = 0$ on $\Sigma_U$ ($\dot\gamma = 0$) and $\dot K =
0$. Let $Y$ be Lemma 2.1 (e)'s vector field on $\Sigma_U$, smooth, as $Y^\flat = k(\nu,\cdot)+\frac12k(\nu,\nu)
\nu^\flat$. $\Theta(k)$ is a 1-form on $\Omega'_+$, smooth up to $\Sigma_U$. Let $F$ be a smooth 1-form on $\Omega'$
with $F = \Theta(k)$ on $\Omega'_+$: section 0 extends $\Theta(k)$ to an open neighbourhood $V$ of $\Omega'_+$ in
$\Omega'$, and a smooth function equal to 1 on the closed set $\Omega'_+$ with support in $V$ (smooth Urysohn) extends
it by 0 beyond. By Lemma 1.1 on $\Omega'$, with $P := 2\delta_gG_g\delta^*_g$ or its negative (Lemma 2.1 (a)), there is
a smooth 1-form $w$ on $\Omega'$ with
$$2\delta_gG_g\delta^*_gw = F,\qquad w|_{\Sigma_U} = 0,\qquad\nabla_\nu w|_{\Sigma_U} = Y^\flat.$$
Put $X := w^\sharp$, a smooth vector field on $\Omega'$; the theorem's $X$ is its restriction to $\Omega'_+$, and Lemma
2.1 (f) applies to it as it stands. Then $\Theta(\mathcal L_Xg) = \Theta(2\delta^*_gw) = F = \Theta(k)$ on
$\Omega'_+$, and $X = 0$, $\nabla_\nu X = Y$ on $\Sigma_U$.

*Step 2 (the difference has vanishing Cauchy data).* Let $h := k-\mathcal L_Xg$.

- $h = 0$ on $\Sigma_U$, by Lemma 2.1 (e).

- $h$ induces zero linearised data: $k$ does by assumption, and $\mathcal L_Xg$ does by Lemma 2.1 (f). So by Lemma 2.1
  (c), $(\nabla_\nu h)(e_i,e_j) = 2\dot K(e_i,e_j) = 0$.

- $\Theta(h) = 0$ on $\Omega'_+$ by Step 1. At $\Sigma_U$, Lemma 2.1 (d) with $h' := \nabla_\nu h$ and $h'(e_i,e_i) =
  0$ gives $h'(\nu,e_j) = 0$ and $h'(\nu,\nu) = 0$.

So $h|_{\Sigma_U} = 0$ and $\nabla_\nu h|_{\Sigma_U} = 0$.

*Step 3 (it vanishes).* $D\mathrm{Ric}(h) = D\mathrm{Ric}(k)-D\mathrm{Ric}(\mathcal L_Xg) = 0$ (Lemma 2.1 (b)), and
$\Theta(h) = 0$, so $L^0h = 0$ on $\Omega'_+$ by (0.1); $h$ is smooth up to $\Sigma_U$.

- *$h$ vanishes to infinite order along $\Sigma_U$.* Work in coordinates $(t_{\mathrm{IVP}},y)$ near a point of
  $\Sigma_U$. As $h = 0$ on $\Sigma_U$, $\nabla_\nu h = \nu^{t}\partial_{t_{\mathrm{IVP}}}h$ there, with $\nu^t :=
  d t_{\mathrm{IVP}}(\nu)>0$; so $\partial_{t_{\mathrm{IVP}}}h = 0$ on $\Sigma_U$. Suppose
  $\partial^j_{t_{\mathrm{IVP}}}h = 0$ on $\Sigma_U$ for $j<m$, some $m\ge2$, so that every derivative of $h$ of order
  below $m$ vanishes there. By Lemma 2.1 (a), $2L^0 = -g^{-1}(dt_{\mathrm{IVP}},dt_{\mathrm{IVP}})
  \partial^2_{t_{\mathrm{IVP}}}+R$, with $R$ of second order and at most first order in $\partial_{t_{\mathrm{IVP}}}$,
  and $g^{-1}(dt_{\mathrm{IVP}},dt_{\mathrm{IVP}})<0$ as $dt_{\mathrm{IVP}}$ is timelike: $\Sigma_U$ is
  noncharacteristic.
  Apply $\partial^{m-2}_{t_{\mathrm{IVP}}}$ to $2L^0h = 0$ and restrict to $\Sigma_U$: every term but
  $-g^{-1}(dt_{\mathrm{IVP}},dt_{\mathrm{IVP}})\partial^m_{t_{\mathrm{IVP}}}h$ is a derivative of order below $m$, or of
  order $m$ with at most $m-1$ derivatives in $t_{\mathrm{IVP}}$ (a tangential derivative of a vanishing normal one),
  so it vanishes; hence $\partial^m_{t_{\mathrm{IVP}}}h = 0$ on $\Sigma_U$. `ix5.py` X8 computes the leading
  coefficient: for $h = f(t)H$ on a curved metric, $f$ arbitrary, no derivative of $f$ above the second occurs in
  $L^0h$ and the coefficient of $f''$ is $-\frac12g^{tt}H$, so with $f = t^m$ the coefficient of $t^{m-2}$ at $t = 0$
  is $-\frac12m(m-1)g^{tt}H$ for every $m\ge2$; the ungauged $D\mathrm{Ric}$ fails both.

- *Extension by zero.* Put $\tilde h := h$ on $\Omega'_+$ and $\tilde h := 0$ on $\Omega'\cap\{t_{\mathrm{IVP}}<0\}$.
  Every derivative of $h$ tends to 0 at $\Sigma_U$, so $\tilde h$ is smooth on $\Omega'$: each derivative of $\tilde h$
  off $\Sigma_U$ extends continuously by 0 across $\Sigma_U$, and a continuous function on $\Omega'$ that is $C^1$ off
  the hypersurface $\Sigma_U$, with first derivatives extending continuously across it, is $C^1$ (the mean value theorem
  along curves transverse to $\Sigma_U$); induction on the order gives every $C^j$ ([BGP] p. 81's device, section 0,
  shown directly). $L^0\tilde h$ is smooth and vanishes off $\Sigma_U$, so everywhere; and $\tilde h|_{\Sigma_U} = 0$,
  $\nabla_\nu \tilde h|_{\Sigma_U} = 0$.

$2L^0$ or its negative is normally hyperbolic (Lemma 2.1 (a)). [BGP] Corollary 3.2.4 on $\Omega'$, on each component,
gives $\tilde h = 0$, so $h = 0$ on $\Omega'_+$. $\square$

**Corollary 2.3 (Part VIII's solution in any gauge).** Let $(\dot\gamma,\dot k)$, $\dot g$, $S'$, $\dot b$ and $U'$ be
as in Part VIII Theorem 2.2, $U\subset U^\sharp$ open, $\Omega' := D_U(\Sigma_U)$ and $\Omega'_+ :=
\Omega'\cap\{t_{\mathrm{IVP}}\ge0\}\subset N^+\subset N$. Let $\dot g'$ be a symmetric 2-tensor on $\Omega'_+$, smooth
up to $\Sigma_U$, with $D\mathrm{Ric}(\dot g') = 0$, that induces on $\Sigma_U$ the data $(\dot\gamma,\dot k)$ plus
those of $\mathcal L_Zg$, for a vector field $Z$ near $\Sigma_U$ in $\Omega'_+$, smooth up to $\Sigma_U$. Then
$$\dot g' = \dot g+\mathcal L_Xg\quad\text{on }\Omega'_+$$
for a vector field $X$ on $\Omega'_+$, smooth up to $\Sigma_U$. In particular, where $\chi_K = 1$ in $\Omega'_+$,
$$\dot g'-\mathcal L_Xg-\partial_bg_b|_{b=b_0}(\dot b) = h_{b_0,\mathrm{rem}}(q')+h',$$
with $q'$ and $h'$ the components of $D_0\Phi(U') = (h',\vec p\,',q')$ named in Part VIII Theorem 2.2 (3), as in its
(2.2). For $U = U^\sharp$, $\Omega'_+ = N^+ = M^\circ\cap\{t_{\mathrm{IVP}}\ge0\}$ (Lemma 1.2). The region where Part
VIII (2.3) is stated has $t_{\mathrm{IVP}}\ge t_*\ge T'\ge0$ ((2.3) holds with $T'$ enlarged, so take $T'\ge0$), so its
part in $\{r>r_0\}$ lies in $N^+$, and there the remainder has the rate of Part VIII (2.3): every linearised vacuum
solution with these data settles, up to the linearised diffeomorphism $\mathcal L_Xg$, to a linearised Myers-Perry
metric, with $X$ itself not controlled (Remark 2.4 (b)). For a general open $U$ this holds only on the part of that
region which $\Omega'_+$ contains (verifier 162's M3).

*Proof.* $\dot g$ is smooth on the interior of $N$ with $D\mathrm{Ric}(\dot g) = 0$ (section 0; Part VIII Theorem 2.2
(1)), and its restriction to $N^+\supset\Omega'_+$ is smooth up to $\Sigma^\circ$ (section 0). Near
$\Sigma_{\mathrm{IVP}}$ in $N$, $\dot g = \dot h+\dot g_{S'}$ with $\dot g_{S'} = -\mathcal L_{V(S')}g$: the set
$\mathcal D' = \mathcal D\setminus\{t^\flat_*\ge\hat T+\frac74\}$ of Part VIII Theorem 2.2 (2) contains
$N\cap\{t_{\mathrm{IVP}}<\hat T+\frac74\}$, as $t^\flat_*\le t_*\le t_{\mathrm{IVP}}$ where $t^\flat_*$ is defined.
$\dot h$ induces $(\dot\gamma,\dot k)$ (Part VIII Lemma 1.1 (1), which allows a tensor given on one side up to
$\Sigma_{\mathrm{IVP}}$; Proposition 1.2's data). So $k := \dot g'-\dot g$ is smooth up to $\Sigma_U$ on $\Omega'_+$,
has $D\mathrm{Ric}(k) = 0$ there, and induces the data of $\mathcal L_{Z+V(S')}g$. Theorem 2.2 gives $k = \mathcal
L_Xg$. The second display is Part VIII (2.2) with $\dot g = \dot g'-\mathcal L_Xg$. $\square$

**Remark 2.4 (what is and is not asserted).** (a) The statement is the linear counterpart of the gauge comparison that
Part VII Remark 4.1 leaves to the nonlinear theory; it is proved here for the linearisation only. (b) Nothing is
asserted about the size or decay of $X$: $X$ solves a linear wave equation with source $\Theta(k)$ and its own Cauchy
data, and its behaviour at $\mathscr I^+$ and $K^+$ depends on the gauge of $\dot g'$. So the paper's section 8.2 routes
keep their status: a solution in the Regge-Wheeler-type gauge or in the harmonic gauge with the same data, given on that
region and smooth up to the initial surface, is $\dot g+\mathcal L_Xg$ on the future of $\Sigma_{\mathrm{IVP}}$ in
$\{r>r_0\}$ (Corollary 2.3), which settles modulo $\mathcal L_Xg$; the decay *in those gauges* is the decay of $\mathcal
L_Xg$ there, which is what the deduced routes argue and is not proved here. (c) In the class of Part VII, if $U$ is
$G$-invariant (for instance $U = U^\sharp$: $G$ preserves $t_{\mathrm{IVP}}$ and $|x|$), so that $\Omega'$ and
$\Omega'_+$ are $G$-stable, the data $(\dot\gamma,\dot k)$ are in the class of Part VIII Corollary 2.3, and $\dot g'$
is $G$-invariant, then $X$ may be taken $G$-invariant ($Z$'s invariance is not needed; only $k$'s is used). $G$ is
compact and acts by isometries of $g$ (Part VIII Corollary 2.3's proof); $\dot g$ is $G$-invariant by that Corollary,
so $k = \dot g'-\dot g$ is; and the Haar average $X_G := \int_G\sigma_*X\,d\sigma$ has $\mathcal L_{X_G}g =
\int_G\sigma_*(\mathcal L_Xg)\,d\sigma = k$ (verifier 162's M4).

## 3. Findings, labels and sources

- (IX1) $\Omega_*\cup\mathcal D = N$: Part VIII's $\dot g$ lives on all of $N$ (section 0). Recorded because Part VIII
  states its domain as $\Omega_*\cup\mathcal D$.

- (IX2) [BGP] Theorem 3.2.11 is stated for compactly supported data; the extension to smooth data without support
  conditions (Lemma 1.1) is written out, using only Corollary 3.2.4, Theorem 3.2.11 and the facts used in its proof.

- (IX3) The domain of the comparison is the future half $\Omega'_+$ of a Cauchy development $D_U(\Sigma_U)$; for $U =
  U^\sharp$ it is the whole future $N^+ = M^\circ\cap\{t_{\mathrm{IVP}}\ge0\}$ (Lemma 1.2), where the settling
  statement lives (amended D610, finding (IX5)).

- (IX4) Verifier 162 (D347): no blocking or major gap. M1, Lemma 1.1's case split at $a_i = 0$, $a_i+1 = 0$; M2, X5
  tested a two-dimensional family of the three-dimensional space it claims, now the full family, with a tangential
  control; M3, Corollary 2.3's settling clause restricted to where $\Omega'$ reaches; M4, Remark 2.4 (c) needs $U$
  $G$-invariant, and averages $X$ itself. Nits: III.K's sublevel convention cited (N1); Step 0's support (N2); Lemma
  2.1 (f) now computed, X7 (N3); X1's flat $D\mathrm{Ric}$ tied to X6's (N4); the connection of Lemma 1.1 (N5). All
  seated.

- (IX5) A later reading (D610) found a major gap: section 0 called $\nu$ positive, but III.K Proposition 1.2 sets $\nu =
  0$ on $[0,R_\nu]$, so $N = \{t_{\mathrm{IVP}}\ge0\}$ near $\{r = r_0\}$ and $\Sigma^\circ$ was not inside the old
  $N^\circ := \{t_{\mathrm{IVP}}>-\nu\}\cap M^\circ$; the old Lemma 1.2's first two claims failed there, and with them
  the domain of Theorem 2.2 and Corollary 2.3. Repair: the Cauchy development is taken in $U^\sharp :=
  M^\circ\cap\{t_{\mathrm{IVP}}>-1\}$, which contains $\Sigma^\circ$ and where only $g$ is used; Theorem 2.2 is stated
  on its future half for tensors smooth up to $\Sigma_U$; Step 1 extends $\Theta(k)$ across $\Sigma_U$ (Seeley); Step 3
  shows $h$ vanishes to infinite order at the noncharacteristic $\Sigma_U$ (`ix5.py` X8) and extends it by 0, so that
  [BGP] Corollary 3.2.4 applies. Section 0 records why $\dot g$ restricted to $N^+$ is smooth up to $\Sigma^\circ$
  (deduced from Part VIII's $H^k$ bounds). Nits seated at the same time: the term "time function" is now II.F's, with
  [BGP] p. 24's Cauchy time-function named for the property; [BGP] Lemma A.5.4 corrected to Corollary A.5.4 (p. 174),
  with $S = \{0\}\times S$; [BGP]'s connectedness handled per component; $k$'s $G$-invariance in Remark 2.4 (c) traced
  to Part VIII Corollary 2.3; $q'$ and $h'$ named in Corollary 2.3; `ix5.py`'s X5 comment corrected; `checks/ix5.out`
  recorded. The objects $N^\circ$ and $N^{\mathcal D}$ are withdrawn; a text that cites them reads $U^\sharp$,
  $\Omega^\sharp$ and $N^+$ in their place. The verifier of the repair (D611) found no major gap. Seated: section 0
  states why only $\mathcal K$ is involved where $\nu = 0$ (m2); BEYOND5-R0-PROOF.md section 11 is marked as the text of
  before D610; GAUGEDECAY5.md Proposition 2.1 (a) and Theorem 1.5 (d), which still used $N^{\mathcal D}$ and $N^\circ$,
  are restated in its round 3 with the source extended as in Step 1 and the result stated on $N^+$ (m1). Nits: Corollary
  A.5.4 at the local-finiteness step; [BGP] p. 81's device as [BGP] applies it, and the zero extension's smoothness
  shown in Step 3; Theorem 1.3.13 among the sources; Remark 2.4 (b) and the paper say the other solution is given on
  that region and smooth up to the initial surface; Step 1's $w$ and $X$ among the uses of
  $\Omega^\sharp\cap\{t_{\mathrm{IVP}}<0\}$; III.K's \"two-sided neighbourhood\" qualified where $\nu = 0$.

- (IX6) A full line-by-line re-read (D617), for the promotion to proved, found no major gap and checked every step and
  every citation into other parts and into [BGP] at source. Seated: section 0's slab clause, which said $\rho'_I>1$ on
  $\Sigma_{\mathrm{IVP}}$ (true only if $T''>C''$, which nothing bounds), now uses $R_9>R_\nu$ and $t_{\mathrm{IVP}}\ge
  r/4$ on $\mathcal S$ (m1); [BGP] p. 81's device is a section vanishing to infinite order along $S$, not on one side
  (m2, D611's n2 completed). Nits: Lemma 2.1 (f) cites X7; the status line records D611; the introduction states
  Corollary 2.3's hypotheses; $\dot g$ is smooth on the interior of $N$ and up to $\Sigma^\circ$; $T'\ge0$ in Corollary
  2.3; $R_\nu$ is in III.K Proposition 1.2's statement; Remark 2.4 (c) needs only $k$'s $G$-invariance; outside this
  part, `checks/ix5.out.tmp` removed, GAUGEDECAY5's line references and D611's log entry corrected. `ix5.py` rerun to the
  byte-identical `checks/ix5.out` (X1-X8 pass, every control false), and each check fails under a mutation of the code it
  tests; the noncharacteristic coefficient recomputed independently at m = 2 and m = 3. With these seated, Part IX is
  proved.

Labels: proved here from the cited parts and [BGP] (READ); Lemma 2.1's identities and Step 3's leading coefficient are
derived in the text and computed in `checks/ix5.py` (X1-X8, with controls). [See64] is cited, not read here. The [BGP]
readings were not re-read by verifier 162 (arXiv refused the fetch); D610's repair cites [BGP] pp. 23, 24, 81 and 174
from the text the session holds; the verifier of the repair re-read them at source (arXiv:0806.1036v1, through a
paper-reading tool): Definition 1.3.8 (p. 23), Corollary 1.3.12 and the Cauchy time-function (p. 24), Corollary 3.2.4
(p. 76), the device of p. 81 (applied there to a section smooth on the whole manifold), Theorem 3.2.11's proof (pp.
85-86), Corollary A.5.4 (p. 174) and Lemma A.5.9 (p. 176), each as cited; the re-read of D617 read them again at source
and found p. 81 misread (finding (IX6)).

Sources: Part VIII (PART-VIII-LINEAR.md) section 0, Lemma 1.1, Proposition 1.2, Theorem 2.2, Corollary 2.3, Remark 2.4;
III.B (PART-III-B-FAMILY.md) (3.5), (3.6), Lemma 3.7; II.C (PART-II-C-OPERATORS.md) Lemma 3.2; II.F (PART-II-F-IOTA.md)
section 1.4, Lemma 1.3 and its proof; III.K (PART-III-K-NONLINEAR.md) section 0 and Proposition 1.2; [BGP]
arXiv:0806.1036v1, Definition 1.3.8 (p. 23), Corollary 1.3.12, Theorem 1.3.13 and the term Cauchy time-function (p. 24),
section 1.5 (p. 33), Corollary 3.2.4 (p. 76), Proposition 3.2.5's proof (p. 81), Theorem 3.2.11 with its proof (pp.
85-86), Corollary A.5.4 (p. 174), Lemma A.5.9 (p. 176). [See64] R. T. Seeley, Extension of $C^\infty$ functions defined
in a half space, Proc. Amer. Math. Soc. 15 (1964) 625-626, doi:10.1090/s0002-9939-1964-0165392-8.
