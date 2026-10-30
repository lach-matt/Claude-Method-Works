# Part V: gluing to the Myers-Perry family at n = 4 ([CD03] Theorem 8.1)

*Status.* Written (D313). This part proves [CD03] Theorem 8.1 at space dimension $n = 4$ for data whose Poincaré charges
lie near those of Tangherlini: smooth vacuum data on $\mathbb R^4\setminus B$ that decay at a rate
$\alpha\in(\frac32,2]$ are glued, on an annulus $\Gamma(R,4R)$, to the data of a translated, rotated and boosted
Myers-Perry metric, which they equal for $r\ge4R$ (Theorem 3.1). [CD03] Remark 8.2 names the one element missing above
$n = 3$: an equivalent of its Proposition F.1 for the Myers-Perry family. Here it is Proposition 2.3 and Corollary 2.4,
near Tangherlini, which is the case the route needs. The proof follows [CD03] section 8.1, with three changes made at $n
= 4$. First, the charges are defined and estimated directly from a linear flux identity (section 1). This replaces
Appendix E and needs no parity condition, since $2\alpha>n-1 = 3$. Second, the exponentially weighted spaces of [CD03]
Theorem 5.9 are used from the start, so the glued data are smooth. Third, the powers of $R$ are those of $n = 4$:
$R^{-2}$ for the energy and momentum, $R^{-3}$ for the angular momentum and the centre of mass. The inputs READ at
source are each stated in [CD03] for every $n\ge2$: (2.1), (2.4), Theorems 3.6 and 3.9, Theorem 5.9, Proposition 5.10,
Corollary 5.11 and Proposition G.1. Lemma 3.18 is proved again here. This part replaces N1STAR-PROOF.md 10.63 (a)-(c),
10.66 (a)-(e) and Proposition 10.47. The nonlinear step that the plan pairs with the gluing is III.K, and [HHV21]'s
perturbation arguments (record 10.68) are discussed in finding (V5). Verified (D315): verifier 136 read it in full,
found no step that uses an $n = 3$ fact, and three minor findings and seven nits, seated as findings (V6)-(V8) and in
the text; to be read.

## 0. Notation

$\mathbb R^4$ carries Cartesian coordinates $x$, with $r = |x|$, $\hat x = x/r$, $S_\rho := \{r = \rho\}$ with outward
unit normal $\nu = \hat x$ and Euclidean area element $dS$, and $\Gamma(a,b) := \{a<r<b\}$. Indices are raised and
traced with $\delta$ unless a metric is named. An *initial data set* is a pair $(g,K)$ of a Riemannian metric and a
symmetric 2-tensor. Its constraint map is [CD03] (2.1),
$$J(K,g)_i := 2\big(-\nabla^jK_{ij}+\nabla_i\,\mathrm{tr}_gK\big),\qquad\rho(K,g) :=
R(g)-|K|^2_g+(\mathrm{tr}_gK)^2,\tag{0.1}$$
"the general relativistic constraint equations whatever the space-dimension $n$" (p. 4). The data are *vacuum* where $J
= 0$ and $\rho = 0$; this condition is invariant under $K\mapsto-K$. For a Lorentzian metric $G =
-N^2dt^2+g_{ij}(dx^i+\beta^idt)(dx^j+\beta^jdt)$ the data on $\{t = 0\}$ are $g$ and
$$K_{ij} := \frac1{2N}\big(\partial_tg_{ij}-D_i\beta_j-D_j\beta_i\big),\tag{0.2}$$
where $D$ is the connection of $g$ and $\beta_i = G_{0i}$; Gauss-Codazzi makes them vacuum when $G$ is Ricci flat.

*Decay.* For $\alpha>0$, $m\in\mathbb N$ and data on $\{r>R_0\}$, put
$$|||(g,K)|||_{\alpha,m} := \sup_{r>R_0}\Big(\sum_{|\gamma|\le
m}r^{\alpha+|\gamma|}|\partial^\gamma(g-\delta)|+\sum_{|\gamma|\le m-1}r^{\alpha+1+|\gamma|}|\partial^\gamma
K|\Big),\tag{0.3}$$
the components taken in Cartesian coordinates. This is [CD03]'s $r^{-\alpha}W^{m,\infty}_r$-asymptotic flatness of $g$
with $K\in r^{-\alpha-1}W^{m-1,\infty}_r$ (section 7, (7.1)), at $m = k+4$.

*The KIDs of flat data.* Let $\mathcal K$ be the space of pairs $X = (Y,N)$ with $Y$ a Killing field of $(\mathbb
R^4,\delta)$ and $N$ an affine function, and fix the basis
$$e_0 := (0,1),\qquad e_l := (\partial_l,0),\qquad e_{ab} := (W_{ab}x,0),\qquad e'_l := (0,x^l),\tag{0.4}$$
for $1\le l\le4$ and $1\le a<b\le4$, with $W_{ab} := E_{ab}-E_{ba}$ and $E_{ab}$ the matrix units; so $\dim\mathcal K =
1+4+6+4 = 15 = (n+1)(n+2)/2$. Each basis element is homogeneous of a degree $d(X)$, meaning that $N(\lambda x) =
\lambda^dN(x)$ and $Y^i(\lambda x) = \lambda^dY^i(x)$: the degree is 0 for $e_0$, $e_l$ and 1 for $e_{ab}$, $e'_l$. The
group $O(4)$ acts on $\mathcal K$ by push-forward under $x\mapsto Rx$. As $O(4)$-representations, the four groups in
(0.4) are the trivial representation, the standard $\mathbb R^4$, $\Lambda^2\mathbb R^4$ (with $W\mapsto RWR^T$) and
$\mathbb R^4$.

## 1. KIDs, the flux identity and the charges

**Lemma 1.1 (the KIDs).** Let $\Omega\subset\mathbb R^4$ be open and connected. A smooth pair $(Y,N)$ on $\Omega$
satisfies $P^*_{(0,\delta)}(Y,N) = 0$ if and only if it is the restriction of an element of $\mathcal K$. Here $P^*$ is
the formal adjoint of the linearisation of (0.1).

*Proof.* At $K = 0$, $g = \delta$, [CD03] (2.4) gives $P^*(Y,N) =
\big(2(\partial_{(i}Y_{j)}-(\mathrm{div}\,Y)\delta_{ij}),\ -\Delta N\delta_{ij}+\partial_i\partial_jN\big)$. The trace
of the first component is $2(1-n)\,\mathrm{div}\,Y$, so $\mathrm{div}\,Y = 0$ and $\partial_{(i}Y_{j)} = 0$. The trace
of the second is $(1-n)\Delta N$, so $\Delta N = 0$ and $\partial_i\partial_jN = 0$, and $N$ is affine on the connected
$\Omega$. For a Killing field, $S_{ij} := \partial_iY_j$ is antisymmetric, so $\partial_k\partial_iY_j =
-\partial_k\partial_jY_i = -\partial_j\partial_kY_i = \partial_j\partial_iY_k = \partial_i\partial_jY_k =
-\partial_i\partial_kY_j = -\partial_k\partial_iY_j$, which therefore vanishes. So $Y$ is affine with antisymmetric
linear part. The converse is immediate. $\square$

**Lemma 1.2 (the flux identity).** Let $X = (Y,N)\in\mathcal K$, let $\Omega\subset\mathbb R^4$ be a bounded open set
with smooth boundary, and let $(g,K)$ be data on $\bar\Omega$ with $h := g-\delta$, $|h|\le\frac12$. Then
$$\int_\Omega(Y^iJ_i+N\rho)(K,g)\,d\mu_g = \oint_{\partial\Omega}\mathfrak b_X(h,K)+\int_\Omega q_X\,dx,\tag{1.1}$$
$$\mathfrak b_X(h,K) :=
\Big[N(\partial_jh_{ij}-\partial_i\mathrm{tr}\,h)
-(\partial_jN\,h_{ij}-\partial_iN\,\mathrm{tr}\,h)-2(Y^jK_{ij}-Y_i\mathrm{tr}\,K)\Big]\nu^i\,dS,$$
where $\nu$ and $dS$ are Euclidean, and $q_X$ is a smooth function of $(N,Y,h,\partial h,\partial^2h,K,\partial K)$,
linear in $(N,Y)$, with
$$|q_X|\le C(|N|+|Y|)\big(|h||\partial^2h|+|\partial h|^2+|h||\partial K|+|\partial h||K|+|K|^2\big).\tag{1.2}$$

*Proof.* Write $R(g) =
g^{ij}(\partial_k\Gamma^k_{ij}-\partial_j\Gamma^k_{ki})+g^{ij}(\Gamma^k_{kl}\Gamma^l_{ij}-\Gamma^k_{jl}\Gamma^l_{ik})$
with $\Gamma = \frac12g^{-1}\partial h$ and $g^{-1} = \delta+O(|h|)$. Then $R(g) =
\partial_i\partial_jh_{ij}-\Delta\,\mathrm{tr}\,h+\rho_2$, where $\rho_2$ is a sum of terms
$(g^{-1}-\delta)\partial^2h$, $\partial(g^{-1})\partial h$ and $g^{-1}g^{-1}\partial h\,\partial h$. So $|\rho_2|\le
C(|h||\partial^2h|+|\partial h|^2)$, and the $K$-terms of $\rho$ are bounded by $C|K|^2$. Likewise $J_i =
-2(\partial_jK_{ij}-\partial_i\mathrm{tr}\,K)+J_{2,i}$ with $|J_2|\le C(|h||\partial K|+|\partial h||K|)$, and $d\mu_g =
(1+O(|h|))\,dx$. So $q_X := (Y^iJ_i+N\rho)\sqrt{\det
g}-\big(-2Y^i(\partial_jK_{ij}-\partial_i\mathrm{tr}\,K)+N(\partial_i\partial_jh_{ij}-\Delta\,\mathrm{tr}\,h)\big)$
satisfies (1.2). For the linear part, integrate by parts:
$$\int_\Omega N(\partial_i\partial_jh_{ij}-\Delta\,\mathrm{tr}\,h) =
\oint\big[N(\partial_jh_{ij}-\partial_i\mathrm{tr}\,h)-(\partial_jN\,h_{ij}-\partial_iN\,\mathrm{tr}\,h)\big]\nu^i
+\int(\partial_i\partial_jN\,h_{ij}-\Delta N\,\mathrm{tr}\,h),$$
$$\int_\Omega Y^i(\partial_jK_{ij}-\partial_i\mathrm{tr}\,K) =
\oint(Y^jK_{ij}-Y_i\mathrm{tr}\,K)\nu^i-\int(\partial_jY_i\,K_{ij}-\mathrm{div}\,Y\,\mathrm{tr}\,K).$$
The last integrals vanish, because $\partial\partial N = 0$, $\partial_jY_i$ is antisymmetric, $K$ is symmetric and
$\mathrm{div}\,Y = 0$. $\square$

(1.1) is the content of [CD03] (E.15)-(E.16) and (E.27), here in its linear 3+1 form, written out because it is all that
is used.

**Proposition 1.3 (the charges).** Let $(g,K)$ be vacuum data on $\{r>R_0\}$ with $|||(g,K)|||_{\alpha,2}<\infty$,
$\alpha>\frac32$, and $|g-\delta|\le\frac12$. For $X$ in the basis (0.4), of degree $d$, the limit
$$\mathfrak Q_X(g,K) := \lim_{\rho\to\infty}\oint_{S_\rho}\mathfrak b_X(g-\delta,K)$$
exists, and
$$\Big|\mathfrak Q_X(g,K)-\oint_{S_\rho}\mathfrak b_X(g-\delta,K)\Big|\le
C\,|||(g,K)|||_{\alpha,2}^2\,\rho^{2+d-2\alpha}\qquad(\rho>R_0),\tag{1.3}$$
with $C$ depending only on $\alpha$ and $R_0$ (amended D315, finding (V6)). Moreover:

(a) $\mathfrak Q_X$ is continuous on such data for the norm $|||\cdot|||_{\alpha,2}$;

(b) for $R\in O(4)$, $\mathfrak Q_X(R^*(g,K)) = \mathfrak Q_{R\cdot X}(g,K)$, where $R\cdot X$ is the push-forward of
$X$ by $x\mapsto Rx$.

*Proof.* Apply (1.1) on $\Gamma(\rho_1,\rho_2)$, $R_0<\rho_1<\rho_2$, where $J = \rho = 0$:
$$\oint_{S_{\rho_2}}\mathfrak b_X-\oint_{S_{\rho_1}}\mathfrak b_X = -\int_{\Gamma(\rho_1,\rho_2)}q_X\,dx.$$
By (0.3) every term of (1.2) is at most $|||\cdot|||^2r^{-2\alpha-2}$, and $|N|+|Y|\le C(1+r)^d$. So the right side is
at most $C|||\cdot|||^2\int_{\rho_1}^\infty r^{d-2\alpha-2}r^3\,dr = C'|||\cdot|||^2\rho_1^{2+d-2\alpha}$, and
$2+d-2\alpha\le3-2\alpha<0$. So the flux is Cauchy as $\rho\to\infty$, and (1.3) follows. (a): for two such data sets,
$|\mathfrak Q_X(1)-\mathfrak Q_X(2)|\le|\oint_{S_\rho}\mathfrak b_X(h_1-h_2,K_1-K_2)|+C\rho^{2+d-2\alpha}$. Choose
$\rho$ large, then the data close in $C^1$ on $S_\rho$. (b): $\mathfrak b_X$ is built from $\delta$, the radial normal
and $X$, so a change of variables gives $\oint_{S_\rho}\mathfrak b_X(R^*h,R^*K) = \oint_{S_\rho}\mathfrak b_{R\cdot
X}(h,K)$, and $S_\rho$ is invariant. $\square$

The normalisation is that of a linear flux. In ADM units ($G = 1$) the energy is $\mathfrak Q_{e_0}/16\pi$, the momentum
$-\mathfrak Q_{e_l}/16\pi$ (as $-2(K-\mathrm{tr}\,K\,\delta) = -2\pi$ with $\pi$ the momentum density), and similarly
for the others. Only $\mathfrak Q$ is used below.

**Lemma 1.4 (scaling).** For $R>0$ and data $(g,K)$ on $\Gamma(R,4R)$, define $\sigma_R(g,K)$ on $\Gamma(1,4)$ by
$(\sigma_Rg)_{ij}(y) := g_{ij}(Ry)$ and $(\sigma_RK)_{ij}(y) := R\,K_{ij}(Ry)$. Then $(J,\rho)(\sigma_R(K,g))(y) =
R^2(J,\rho)(K,g)(Ry)$ componentwise, and for $X\in\mathcal K$ homogeneous of degree $d$,
$$\int_{\Gamma(1,4)}(Y^iJ_i+N\rho)(\sigma_R(K,g))\,d\mu_{\sigma_Rg} =
R^{-2-d}\int_{\Gamma(R,4R)}(Y^iJ_i+N\rho)(K,g)\,d\mu_g.\tag{1.4}$$

*Proof.* With $D_R(y) := Ry$, $\sigma_Rg = R^{-2}D_R^*g$ and $\sigma_RK = R^{-1}D_R^*K$. The constraint map is natural
under diffeomorphisms. It satisfies $\rho(c^{-1}K,c^{-2}g) = c^2\rho(K,g)$ and $J(c^{-1}K,c^{-2}g) = cJ(K,g)$, as
$g^{-1}$ scales by $c^2$ and $\nabla$ is unchanged. As $(D_R^*J)_i(y) = RJ_i(Ry)$, both components scale by $R^2$. In
(1.4) the left integrand at $y$ is $R^2(Y^i(y)J_i(Ry)+N(y)\rho(Ry))\sqrt{\det g(Ry)}$, with $Y^i(y) = R^{-d}Y^i(Ry)$ and
$N(y) = R^{-d}N(Ry)$, and $dy = R^{-4}dx$. $\square$

## 2. The Myers-Perry family and its charge map near Tangherlini

**Definition 2.1.** Let $\mu_0>0$ and $b_0 = (\mu_0,0)$ be III.B's parameters. For $p = (\mu,A,w,c)$ with
$|\mu-\mu_0|<\frac12\mu_0$, $A\in\mathfrak{so}(4)$, $w,c\in\mathbb R^4$ and $|A|,|w|,|c|<\epsilon_P$, put:

- $g^{\mathrm{KS}}_{\mu,A}$, the Myers-Perry metric in Kerr-Schild form (III.B Definition 3.2), on $\mathbb
R_t\times\{|x|\ge r_0\}$;

- $\Lambda_w := \exp(\sum_kw_kB_k)$, where $B_k$ is the linear map of $\mathbb R^{1+4}$ whose vector field is the boost
$Z_k := x^k\partial_t+t\partial_k$;

- $\Phi_p(y) := \Lambda_wy+(0,c)$ and $G_p := \Phi_p^*g^{\mathrm{KS}}_{\mu,A}$;

- $(g_p,K_p)$, the data (0.2) of $G_p$ on $\{y^0 = 0\}\cap\{|y|>R_P\}$, with $R_P := 100R_1$, with $R_1$ III.B's radius
(not the gluing radius $R_{\mathrm{gl}}$ of Theorem 3.1).

Write $p_0 := (\mu_0,0,0,0)$. $\mathbb A := \sum_{a<b}A_{ab}W_{ab}$ fixes the coordinates $A_{ab}$ on $\mathfrak{so}(4)$.

**Lemma 2.2 (the family's data).** For $\epsilon_P$ small: $(g_p,K_p)$ are smooth vacuum data on $\{|y|>R_P\}$, smooth
in $(p,y)$; for every $m$, $|||(g_p,K_p)|||_{2,m}\le C_m$; and every $p$-derivative of $(g_p-\delta,K_p)$ obeys the
bounds of (0.3) with $\alpha = 2$, uniformly in $p$.

*Proof.* $g^{\mathrm{KS}}_{\mu,A}-\eta = H_{\mu,A}k_A\otimes k_A$ with $H_{\mu,A}\in|x|^{-2}C^\infty(\bar X)$ and
$k_A-dt = \ell_A\in C^\infty(\bar X)$, smoothly in $(\mu,A)$ (III.B Lemma 3.1 (b) and Definition 3.2:
$r_A\in|x|(1+|x|^{-2}C^\infty(\bar X))$, $P = r_A^4(1+O(r_A^{-2}))$, $F_A = 1+O(|x|^{-2})$). So $G-\eta$ is independent
of $t$ and a classical symbol of order $-2$ in $x$: $|\partial_x^\gamma(G-\eta)|\le C|x|^{-2-|\gamma|}$. $\Phi_p$ is
affine with linear part near the identity. On $\{y^0 = 0\}$ the point $\Phi_p(0,y)$ has $|x|\ge\frac12|y|$ and
$|t|\le2|w||y|$, so $G_p-\eta = \Phi_p^*(G-\eta)$ obeys the same symbol bounds on $\{|y^0|\le\frac12|y|\}$, smoothly in
$p$ together with all $p$-derivatives. There $|G_p-\eta|\le C\mu_0R_P^{-2}$ is small, so $\{y^0 = 0\}$ is spacelike, $N$
is bounded below, and (0.2) expresses $(g_p,K_p)$ as smooth functions of $(G_p,\partial G_p)$ on the slice, vanishing at
$(\eta,0)$. This gives the bounds. $G_p$ is Ricci flat (III.B Proposition 3.4), so the data are vacuum. $\square$

**Proposition 2.3 (the charge map near Tangherlini; [CD03] Proposition F.1's equivalent).** The map
$$\mathfrak q:p\mapsto\big(\mathfrak Q_X(g_p,K_p)\big)_{X\in(0.4)}\in\mathbb R^{15}$$
is $C^1$. At $p_0$, $\mathfrak q(p_0) = (6\pi^2\mu_0,0,\dots,0)$, and $D\mathfrak q(p_0)$ is invertible. In the bases
(0.4) and $(\mu,A_{ab},w_k,c_k)$ it is block lower triangular, with diagonal blocks
$$\frac{\partial\mathfrak Q_{e_0}}{\partial\mu} = 6\pi^2,\quad\Big(\frac{\partial\mathfrak Q_{e_l}}{\partial w_k}\Big) =
-6\pi^2\mu_0I_4,\quad\Big(\frac{\partial\mathfrak Q_{e_{ab}}}{\partial A_{a'b'}}\Big) =
-4\pi^2\mu_0I_6,\quad\Big(\frac{\partial\mathfrak Q_{e'_l}}{\partial c_k}\Big) = -6\pi^2\mu_0I_4.\tag{2.1}$$
The block $(\partial\mathfrak Q_{e'_l}/\partial w_k)$ is not needed (the numerical check of finding (V2) finds it zero),
the other blocks off the diagonal vanish, and $\det D\mathfrak q(p_0) = 6\pi^2(6\pi^2\mu_0)^8(4\pi^2\mu_0)^6$.

*Proof.* *$C^1$.* For fixed $\rho$, $f_\rho(p) := \oint_{S_\rho}\mathfrak b_X(g_p-\delta,K_p)$ is $C^1$, with
$\partial_pf_\rho = \oint_{S_\rho}\mathfrak b_X(\partial_pg_p,\partial_pK_p)$, since $\mathfrak b_X$ is linear.
Differentiate in $p$ the identity of Proposition 1.3's proof, which holds for every $p$. The difference of
$\partial_pf_\rho$ at $\rho_2$ and $\rho_1$ is then $-\int\partial_p[q_X(g_p,K_p)]\,dx$. As $q_X$ vanishes to second
order in the jets, $|\partial_p[q_X]|\le
C(1+r)^d\,|\mathrm{jet}(g_p-\delta,K_p)|\,|\mathrm{jet}\,\partial_p(g_p,K_p)|\le Cr^{d-6}$ by Lemma 2.2. So
$\partial_pf_\rho$ converges uniformly in $p$, at the rate $\rho^{d-2}$, and $\mathfrak q$ is $C^1$ with $D\mathfrak
q(p) = \lim_\rho\oint_{S_\rho}\mathfrak b_X(\partial_p(g_p,K_p))$.

*Equivariance.* For $R\in O(4)$ let $\tilde R(t,x) := (t,Rx)$. By III.B Lemma 3.1, $r_A(Rx) = r_{R^TAR}(x)$, since $|Rx|
= |x|$, $|ARx| = |R^TARx|$ and $\mathrm{tr}\,A^2$, $\det A$ are conjugation invariant. The other ingredients of
Definition 3.2 are covariant in the same way, so $\tilde R^*g^{\mathrm{KS}}_{\mu,A} = g^{\mathrm{KS}}_{\mu,R^TAR}$. Also
$\Phi_p\circ\tilde R = \tilde R\circ\Phi_{p\cdot R}$ with $p\cdot R := (\mu,R^TAR,R^Tw,R^Tc)$, and $\tilde R$ preserves
$\{y^0 = 0\}$. So $(g_{p\cdot R},K_{p\cdot R}) = R^*(g_p,K_p)$, and Proposition 1.3 (b) gives $\mathfrak Q_X(g_{p\cdot
R},K_{p\cdot R}) = \mathfrak Q_{R\cdot X}(g_p,K_p)$. As $p_0\cdot R = p_0$, $D\mathfrak q(p_0)$ intertwines the
representations
$$\mathbb R\oplus\Lambda^2\oplus\mathbb R^4\oplus\mathbb R^4\ (\mu,A,w,c)\quad\longrightarrow\quad\mathbb R\oplus\mathbb
R^4\oplus\Lambda^2\oplus\mathbb R^4\ (\mathfrak Q_{e_0},\mathfrak Q_{e_l},\mathfrak Q_{e_{ab}},\mathfrak Q_{e'_l}),$$
the charges being linear functionals on $\mathcal K$, whose representation is self-dual. The trivial representation, the
standard $\mathbb R^4$ and $\Lambda^2\mathbb R^4$ of $O(4)$ are real irreducible and pairwise non-isomorphic (dimensions
1, 4, 6), each with commutant $\mathbb R$. For $\mathbb R^4$ this holds already for $SO(4)$. $\Lambda^2$ is the sum of
the self-dual and anti-self-dual parts, each irreducible of dimension 3 under $SO(4)$ (acting through $SO(3)\times
SO(3)$); a reflection exchanges them, so no proper nonzero subspace is $O(4)$-invariant. An $SO(4)$-equivariant
endomorphism is $a\oplus b$ on the two parts, and commuting with a reflection forces $a = b$. By Schur's lemma
$D\mathfrak q(p_0)$ is: a scalar $e$ from $\mu$ to $\mathfrak Q_{e_0}$; a scalar $j$ times $I_6$ from $A$ to $(\mathfrak
Q_{e_{ab}})$; on the two copies of $\mathbb R^4$, a matrix $\begin{pmatrix}a&b'\\c'&d\end{pmatrix}\otimes I_4$ from
$(w,c)$ to $(\mathfrak Q_{e_l},\mathfrak Q_{e'_l})$; and zero elsewhere. Likewise $\mathfrak q(p_0)$ is
$O(4)$-invariant, so only its trivial component $\mathfrak Q_{e_0}$ can be nonzero.

*The base.* On $\{t = 0\}$, $g^{\mathrm{KS}}_{\mu,0} = \eta+H(dt+dr)^2$ with $H = \mu r^{-2}$ (III.B Proposition 3.4)
has $h_0 = H\hat x\otimes\hat x$ exactly, $\beta_0 = H\hat x$, $G_{00} = -1+H$ and $N_0 = (1+H)^{-1/2}$. Its second
fundamental form $K_0 = -N_0^{-1}D_{(i}\beta_{j)}$ is $O(\mu r^{-3})$ with $\partial K_0 = O(\mu r^{-4})$. It is
invariant under $O(4)$, so $K_0 = a(r)\hat x\otimes\hat x+b(r)(\delta-\hat x\otimes\hat x)$.

*$e$.* $\partial_\mu h_0 = r^{-2}\hat x\otimes\hat x$, $h_{ij} = \mu x_ix_jr^{-4}$. So $\partial_jh_{ij} =
\mu(n+1-4)x_ir^{-4} = \mu x_ir^{-4}$ and $\partial_i\mathrm{tr}\,h = -2\mu x_ir^{-4}$, and $\mathfrak b_{e_0} = 3\mu
r^{-3}dS$. Integrating over $S_\rho$, of area $2\pi^2\rho^3$, gives $6\pi^2\mu$ at every radius: $\mathfrak
Q_{e_0}(g_{\mu,0},K_{\mu,0}) = 6\pi^2\mu$ and $e = 6\pi^2$. (In ADM units this is $\frac{3\pi\mu}8$, the mass of
five-dimensional Tangherlini.)

*$d$ and $b'$.* The translation in $c_k$ changes the data to $(h_0,K_0)(y+c)$, with derivative $\partial_k(h_0,K_0)$.
For $e'_l = (0,x^l)$: $x^l\partial_k(\partial_jh_{ij}-\partial_i\mathrm{tr}\,h)\nu^i = 3\mu x^l\partial_k(x_ir^{-4})\hat
x_i = -9\mu x^lx_kr^{-5}$, and $-(\delta_{lj}\partial_kh_{ij}-\delta_{li}\partial_k\mathrm{tr}\,h)\nu^i =
-\mu(\delta_{lk}r^{-3}-x_kx_lr^{-5})$. With $\int_{\mathbb S^3}\omega_k\omega_l = \frac{\pi^2}2\delta_{kl}$ the flux is
$-\frac92\pi^2\mu\delta_{lk}-\frac32\pi^2\mu\delta_{lk}$, so $d = -6\pi^2\mu_0$ at every radius. For $e_l$ the flux of
$\partial_kK_0 = O(r^{-4})$ is $O(\rho^{-1})$, so $b' = 0$.

*$a$.* $\partial_{w_k}G_p|_{p_0} = \mathcal L_{Z_k}g$ for $g := g^{\mathrm{KS}}_{\mu_0,0}$. As $\mathcal L_{Z_k}\eta =
0$ and $Z_k(H) = t\partial_kH$, $\mathcal L_{Z_k}(Hk\otimes k) = t\partial_kH\,k\otimes k+H(\mathcal L_{Z_k}k\otimes
k+k\otimes\mathcal L_{Z_k}k)$, with $k = dt+dr$ and $\mathcal L_{Z_k}k = d(x^k+t\hat x_k) = dx^k+\hat x_k\,dt+t\,d\hat
x_k$. At $t = 0$ this gives
$$\delta G_{00} = 2H\hat x_k,\quad\delta\beta_i = H(\hat x_k\hat x_i+\delta_{ik}),\quad\delta g_{ij} = H(\delta_{ik}\hat
x_j+\hat x_i\delta_{jk}),\quad\partial_t\delta g_{ij} = \partial_kH\,\hat x_i\hat x_j+H(\partial_i\hat x_k\,\hat
x_j+\hat x_i\,\partial_j\hat x_k).$$
Linearising (0.2), $\delta K = -\frac{\delta N}{N_0}K_0+\frac1{2N_0}(\partial_t\delta g-2\delta(D_{(i}\beta_{j)}))$.
Since $\delta N = O(r^{-2})$, $N_0-1 = O(r^{-2})$, $\Gamma_0\,\delta\beta = O(r^{-5})$ and $\delta\Gamma\,\beta_0 =
O(r^{-5})$, this is $\delta K_{ij} = \frac12(\partial_t\delta
g_{ij}-\partial_i\delta\beta_j-\partial_j\delta\beta_i)+O(r^{-5})$. The terms $H\partial\hat x_k$ cancel. With
$\partial_iH = -2H\hat x_i/r$ and $\partial_i\hat x_j = (\delta_{ij}-\hat x_i\hat x_j)/r$,
$$\delta K_{ij} = \frac Hr\big(2\hat x_i\hat x_j\hat x_k+\hat x_i\delta_{jk}+\hat x_j\delta_{ik}-\hat
x_k\delta_{ij}\big)+O(r^{-5}),\qquad\mathrm{tr}\,\delta K = \frac Hr(4-n)\hat x_k+O(r^{-5}) = O(r^{-5}).$$
For $e_l$, $\mathfrak b = -2(\delta K_{lj}\hat x_j-\hat x_l\mathrm{tr}\,\delta K)dS = -2\mu_0r^{-3}(2\hat x_l\hat
x_k+\delta_{lk})dS+O(r^{-5})dS$, whose integral tends to $-2\mu_0(\pi^2+2\pi^2)\delta_{lk}$. So $a = -6\pi^2\mu_0$; in
ADM units the momentum per unit rapidity is the energy.

*$j$.* At $A = 0$, $r_A = |x|+O(|A|^2)$, $H_{\mu,A} = H+O(|A|^2)$ (as $P$, $F_A$, $\mathrm{tr}\,A^2$ and $\det A$ are
even in $A$), and $\ell_A = (r^2I-A^2)^{-1}(rI+A)x\cdot dx = \hat x\cdot dx+r^{-2}(Ax)\cdot dx+O(|A|^2)$ (III.B Lemma
3.1 (a): $\mathsf M/P = (r^2I-A^2)^{-1}$). So the derivative in the direction $A = W_{ab}$ is $\delta G =
H(k\otimes\alpha+\alpha\otimes k)$, $\alpha := r^{-2}(Ax)\cdot dx$, $\alpha(\hat x) = 0$. Then $\delta G_{00} = 0$,
$\delta\beta = H\alpha = \mu_0r^{-4}(Ax)\cdot dx$, $\delta g = H(\hat x\otimes\alpha+\alpha\otimes\hat x)$ and
$\partial_t\delta g = 0$. Further $\delta(N^2) = -\delta G_{00}+2\beta_0^i\delta\beta_i-\beta_0^i\beta_0^j\delta g_{ij}
= 0$, as $\beta_0\parallel\hat x\perp\alpha$. The remaining terms other than $\partial\delta\beta$ are $O(r^{-6})$, so
$$\delta K_{ij} = -\partial_{(i}\delta\beta_{j)}+O(r^{-6}) =
2\mu_0r^{-6}\big(x_i(Ax)_j+x_j(Ax)_i\big)+O(r^{-6}),\qquad\mathrm{tr}\,\delta K = O(r^{-6}).$$
For $e_{a'b'} = (W'x,0)$ with $W' := W_{a'b'}$, as $(W'x)\cdot\hat x = 0$, $\mathfrak b = -2\delta K(W'x,\hat x)\,dS =
-4\mu_0r^{-5}(Ax)\cdot(W'x)\,dS+O(r^{-5})dS$. On $S_\rho$, $(Ax)\cdot(W'x) = \rho^2(A\omega)\cdot(W'\omega)$ and $dS =
\rho^3d\omega$, so the integral tends to $-4\mu_0\int_{\mathbb S^3}\omega^TA^TW'\omega\,d\omega =
-2\pi^2\mu_0\,\mathrm{tr}(A^TW')$, using $\int\omega_i\omega_j = \frac{\pi^2}2\delta_{ij}$. As
$\mathrm{tr}(W_{ab}^TW_{a'b'}) = 2\delta_{aa'}\delta_{bb'}$, $j = -4\pi^2\mu_0$; in ADM units the angular momentum is
$\frac{\pi\mu_0}4A_{ab}$, two thirds of the mass per unit spin.

So $D\mathfrak q(p_0)$ is as stated. Its determinant is $e\cdot(ad-b'c')^4\cdot j^6 =
6\pi^2(6\pi^2\mu_0)^8(4\pi^2\mu_0)^6\ne0$. $\square$

**Corollary 2.4.** There are neighbourhoods $U$ of $p_0$ and $V$ of $\mathfrak q(p_0)$ such that $\mathfrak q:U\to V$ is
a $C^1$ diffeomorphism (inverse function theorem, cited). For $Q\in V$, write $p(Q) := \mathfrak q|_U^{-1}(Q)$; then
$p(Q)$ is continuous and the data $(g_{p(Q)},K_{p(Q)})$ have charge vector exactly $Q$.

## 3. The gluing

**Theorem 3.1 ([CD03] Theorem 8.1 and Remark 8.4 at n = 4).** Let $(g,K)$ be smooth vacuum data on
$\{r>R_0\}\subset\mathbb R^4$ with $|||(g,K)|||_{\alpha,7}<\infty$ for some $\alpha\in(\frac32,2]$, and with charge
vector $\mathfrak Q^0 := (\mathfrak Q_X(g,K))_X\in V$. There is $R_{\mathrm{gl}}$ such that for every $R\ge
R_{\mathrm{gl}}$ there are $p_R\in U$ and smooth vacuum data $(\hat g_R,\hat K_R)$ on $\{r>R_0\}$ that equal $(g,K)$ on
$\{r\le R\}$ and $(g_{p_R},K_{p_R})$ on $\{r\ge4R\}$. Moreover $\mathfrak q(p_R)\to\mathfrak Q^0$ as $R\to\infty$.

Enlarging $R_0$, $|g-\delta|\le\frac12$ on $\{r>R_0\}$; this is assumed below. Fix $k := 3$, the least integer above
$\frac n2$. The proof has five steps.

*Step 1: the solvability statement read at source.* Let $M := \bar\Gamma(1,4)$, a compact manifold with boundary, and
let $x\in C^\infty(M)$ be a defining function of $\partial M$ with $0<x\le1$ in the interior that equals the distance to
$\partial M$ near it. The background is $(K_0,g_0) := (0,\delta)$. [CD03] Theorem 5.9 (READ, p. 25, for every $n$)
applies with any $s>0$ (fix $s := 1$) and this $k>\frac n2$. Its hypotheses hold: $g_0$ is smooth on $M$, so it has
$(W^{k+4,\infty}_{x^2},k+4)$-behaviour; $x^4|\mathrm{Ric}(g_0)| = 0$; $x|\nabla\nabla x|\to0$, $\nabla\nabla x$ being
bounded near $\partial M$; and $K_0 = 0$. The source prints $\varphi = x^2$, $\psi = e^{s/x}$ for its sources and
solutions (p. 25). Its $(Y,N)$-spaces are those of Theorem 3.9 with $\psi = e^{-s/x}$, as its solution $(\delta K,\delta
g) = e^{-2s/x}\Phi^2P^*(Y,N)$ shows, and $\psi^2H_{\varphi,\psi} = H_{\varphi,\psi^{-1}}$ ($x^2|d\psi|/\psi = s$ is
bounded). The kernel $\mathcal K_{g_0}$ is that of $\Phi P^*_{(0,\delta)}$ on $\mathring H^1\times\mathring H^2$
(Proposition 3.3, p. 11). By Lemma 1.1 and interior regularity it is $\mathcal K$ restricted to $M$: the 15 KIDs are
bounded, so they lie in these spaces, and every element of the kernel is smooth in $M^\circ$ and one of them. As in the
source (p. 11), $\pi = \pi_{g'}$ denotes the $L^2_\psi(g')$-orthogonal projection onto $\mathcal K^{\perp_{g_0}}$, $g'$
the current background metric; its kernel is $(\mathcal K^{\perp_{g_0}})^{\perp_{g'}} = M_{g'}^{-1}\mathcal K$, where
$\langle u,v\rangle_{L^2_\psi(g')} = \langle M_{g'}u,v\rangle_{L^2_\psi(g_0)}$, $M_{g'}$ the pointwise conversion by
$g'$ and $\sqrt{\det g'}$ (amended D315, finding (V7)). The theorem gives $\epsilon>0$ with the following property. For
$(K',g')$ with $\|K'\|_{C^{k+3}(M)}+\|g'-\delta\|_{C^{k+4}(M)}<\epsilon$, which bounds the norm of
$x^{-2}W^{k+3,\infty}_{x^2}\times W^{k+4,\infty}_{x^2}$ as $x\le1$, and for every $(\delta J,\delta\rho)\in
H^{k+1}_{x^2,e^{s/x}}\times H^k_{x^2,e^{s/x}}$ of norm $<\epsilon$, there is a solution $(\delta K,\delta g)\in
x^2H^{k+2}_{x^2,e^{s/x}}\times x^4H^{k+2}_{x^2,e^{s/x}}$ of
$$\pi\,e^{2s/x}\big\{(J,\rho)(K'+\delta K,g'+\delta g)-(J,\rho)(K',g')\big\} = \pi\,e^{2s/x}(\delta
J,\delta\rho).\tag{3.1}$$
It satisfies $\|(\delta K,\delta g)\|\le C\|(\delta J,\delta\rho)\|$, the bound of Proposition G.1 (pp. 77-78), through
which Theorem 5.9's proof runs (Theorems 3.9 and 3.7). The map $(Y,N)\mapsto$ left side of (3.1) is bijective from a
neighbourhood of zero onto one (Theorem 3.9). When $(K',g')\in C^\infty(M)$ and $(\delta J,\delta\rho)\in
C^\infty_c(M^\circ)$, Corollary 5.11 (READ, p. 27; its Proposition 5.10's hypotheses hold for $(0,\delta)$ as above)
gives $(\delta K,\delta g)\in C^\infty(M)$, extending smoothly by zero across $\partial M$. Finally,
$H^{k+2}_{x^2,e^{s/x}}\subset H^{k+2}(M)\subset C^2(M)$, as $x^{-4j}e^{-2s/x}$ is bounded and $k+2 = 5>\frac n2+2$. So
$\|(\delta K,\delta g)\|_{C^2(M)}\le C\|(\delta J,\delta\rho)\|$.

**Lemma 3.2 (continuity in the background).** In Step 1, the solution with $(Y,N)\in\mathcal K^{\perp_{g_0}}$ in the
neighbourhood of zero is unique, and it depends continuously on $((K',g'),(\delta J,\delta\rho))$.

*Proof.* Write $\Psi(x',z)$ for the left side of (3.1) as a function of the background $x' = (K',g')$ and of $z =
(Y,N)$. By Theorem 3.6 (READ, p. 13), $D_z\Psi(x',0)$ is an isomorphism, the norm of its inverse at most $C_1$
independently of $x'$ near $(0,\delta)$. Write $T_{x'}z := e^{-2s/x}\Phi^2P^*_{x'}z$, so that $\Psi(x',z) =
\pi_{g'}e^{2s/x}\{(J,\rho)(x'+T_{x'}z)-(J,\rho)(x')\}$. $T_{x'}$ is bounded from the $(Y,N)$-space to the solution
space, continuously in $x'$ in operator norm, its coefficients being polynomial in the 2-jet of $x'$ and in $g'^{-1}$.
The constraint map is a polynomial in the 2-jet of the data with coefficients rational in $g$. The spaces
$H^{k+2}_{x^2,e^{s/x}}$ with $k+2>\frac n2+1$ embed in $C^1(M)$ and are stable under products with each other and with
$C^{k+2}(M)$, by Sobolev's inequality on the scaled balls of [CD03] Appendix B. So $(x',\delta
x)\mapsto(J,\rho)(x'+\delta x)-(J,\rho)(x')$ is $C^2$ in $\delta x$ near zero, with derivatives continuous in $x'$ and
bounded uniformly, and $\|D_z\Psi(x',z_1)-D_z\Psi(x',z_2)\|\le C_3\|T\|^2\|z_1-z_2\|$ near zero; this is Proposition
G.1's hypothesis 3 transferred to $z$ (deduced, not read; finding (V8)). Write $C_3$ for $C_3\|T\|^2$ below. So for
$z_1,z_2$ in the ball of radius $(2C_1C_3)^{-1}$,
$$\|\Psi(x',z_1)-\Psi(x',z_2)\|\ge\|D_z\Psi(x',0)(z_1-z_2)\|
-C_3\max(\|z_1\|,\|z_2\|)\,\|z_1-z_2\|\ge(2C_1)^{-1}\|z_1-z_2\|.$$
This gives uniqueness in that ball. For continuity, let $z$ solve the equation for $(x',\delta f)$ and $\tilde z$ for
$(\tilde x',\tilde{\delta f})$, with $\delta f$ the right side of (3.1). Then $\|\tilde z-z\|\le2C_1\|\Psi(\tilde
x',\tilde z)-\Psi(\tilde x',z)\|\le2C_1(\|\tilde{\delta f}-\delta f\|+\|\Psi(x',z)-\Psi(\tilde x',z)\|)$. The last term
tends to zero as $\tilde x'\to x'$: at fixed $z$, $x'\mapsto T_{x'}z$ is continuous, the constraint map is continuous in
the background and the datum by the same product estimates, and $\pi_{g'}$ is continuous in $g'$ (deduced). $\square$

*Step 2: the approximate data.* Fix a radial $\chi\in C^\infty(\mathbb R^4)$ with $0\le\chi\le1$, $\chi = 1$ for $r\le2$
and $\chi = 0$ for $r\ge3$. Let $\bar B\subset V$ be a closed ball about $\mathfrak Q^0$. For $R\ge\max(2R_0,R_P)$ and
$Q\in\bar B$ put
$$x_{Q,R} := \chi\,\sigma_R(K,g)+(1-\chi)\,\sigma_R(K_{p(Q)},g_{p(Q)})\qquad\text{on }M.$$
Then:

(a) $\|K_{Q,R}\|_{C^{k+3}(M)}+\|g_{Q,R}-\delta\|_{C^{k+4}(M)}\le CR^{-\alpha}$, uniformly for $Q\in\bar B$, and
$Q\mapsto x_{Q,R}$ is continuous into $C^{k+3}\times C^{k+4}(M)$. Indeed $|\partial^\gamma_y(\sigma_Rg-\delta)(y)| =
R^{|\gamma|}|\partial^\gamma(g-\delta)(Ry)|\le CR^{-\alpha}$ and $|\partial^\gamma\sigma_RK|\le CR^{-\alpha}$ for
$|\gamma|\le k+4 = 7$ (resp. 6). The member's data obey the same bounds with $\alpha$ replaced by $2\ge\alpha$,
uniformly in $p$, and depend smoothly on $p$ (Lemma 2.2), and $p(Q)$ is continuous.

(b) $(J,\rho)(x_{Q,R})$ is supported in $\bar\Gamma(2,3)$, with $C^{k+2}$-norm at most $CR^{-\alpha}$. On $\Gamma(1,2)$
and $\Gamma(3,4)$ the data are rescaled vacuum data, hence vacuum by Lemma 1.4. The constraint map is a smooth function
of the 2-jet vanishing at $(0,\delta)$.

By (b), $(\delta J,\delta\rho) := -(J,\rho)(x_{Q,R})$ is smooth and supported in $\bar\Gamma(2,3)\subset M^\circ$, where
$x$ is bounded below, so its weighted norms are at most $C\|\cdot\|_{C^{k+1}}\le CR^{-\alpha}$. For $R\ge R_2$, Step 1
and Lemma 3.2 give a smooth $\delta x_{Q,R}$ on $M$ that extends by zero, with $\|\delta x_{Q,R}\|_{C^2(M)}\le
CR^{-\alpha}$, continuous in $Q$. Put $\hat x_{Q,R} := x_{Q,R}+\delta x_{Q,R}$; by (3.1),
$\pi_{g_{Q,R}}e^{2s/x}(J,\rho)(\hat x_{Q,R}) = 0$.

*Step 3: the obstruction is a pairing.* By Step 1, $\pi_{g'}z = 0$ iff $z\in M_{g'}^{-1}\mathcal K$, $g' := g_{Q,R}$, so
$(J,\rho)(\hat x_{Q,R}) = e^{-2s/x}\sum_ic_iM_{g'}^{-1}e_i$ on $M^\circ$, for some $c\in\mathbb R^{15}$; vectors and
covectors are identified by $\delta$. Let
$$F_R(Q)_j := \int_M(Y_j^iJ_i+N_j\rho)(\hat x_{Q,R})\,d\mu_{\hat g_{Q,R}},\qquad e_j = (Y_j,N_j).$$
Then $F_R(Q) = \mathcal G'c$ with $\mathcal G'_{ji} := \int_Me_j\cdot M_{g'}^{-1}e_i\,e^{-2s/x}d\mu_{\hat g}$. As $g'$,
$\hat g\to\delta$ in $C^0(M)$ uniformly on $\bar B$, $\mathcal G'\to\mathcal G$, $\mathcal G_{ji} := \int_Me_j\cdot
e_i\,e^{-2s/x}dx$, the Gram matrix of functions that are linearly independent on every open set, for a positive measure.
So $\mathcal G$ is positive definite, $\mathcal G'$ is invertible for $R$ large, and $(J,\rho)(\hat x_{Q,R}) = 0$ iff
$F_R(Q) = 0$. $F_R$ is continuous on $\bar B$, its integrand depending continuously on $\hat x_{Q,R}$ in $C^2$.

*Step 4: the pairing's asymptotics.* Let $\mathfrak x = (\hat K,\hat g) := \sigma_R^{-1}\hat x_{Q,R}$ on $\Gamma(R,4R)$.
By Lemma 1.4 and then (1.1),
$$F_R(Q)_j = R^{-2-d_j}\Big[\oint_{S_{4R}}\mathfrak b_{e_j}(\mathfrak x)-\oint_{S_R}\mathfrak b_{e_j}(\mathfrak
x)+\int_{\Gamma(R,4R)}q_{e_j}(\mathfrak x)\,dx\Big],\qquad d_j := d(e_j).$$
Near $S_{4R}$, $\mathfrak x$ is the member's data with all derivatives, since $\chi = 0$ for $r\ge3$ and $\delta
x_{Q,R}$ vanishes to infinite order at $\partial M$. So (1.3) with $\alpha = 2$ and Corollary 2.4 give
$\oint_{S_{4R}}\mathfrak b_{e_j} = Q_j+O(R^{d_j-2})$, uniformly on $\bar B$. Near $S_R$, $\mathfrak x = (g,K)$, so
$\oint_{S_R}\mathfrak b_{e_j} = \mathfrak Q^0_j+O(R^{2+d_j-2\alpha})$. On $\Gamma(R,4R)$, unscaling Step 2's bounds
gives $|\partial^\gamma(\hat g-\delta)|\le CR^{-\alpha-|\gamma|}$ ($|\gamma|\le2$) and $|\partial^\gamma\hat K|\le
CR^{-\alpha-1-|\gamma|}$ ($|\gamma|\le1$). With (1.2) and $|e_j|\le CR^{d_j}$, $\int|q_{e_j}|\le
CR^{d_j}R^{-2\alpha-2}R^4$. As $\alpha\le2$, $d_j-2\le2+d_j-2\alpha$, so
$$G_R(Q) := \big(R^{2+d_j}F_R(Q)_j\big)_j = Q-\mathfrak Q^0+O(R^{3-2\alpha})\qquad\text{uniformly on }\bar B,\tag{3.2}$$
and $3-2\alpha<0$. ([CD03] (8.7) prints $R^{-1}$ for every charge at $n = 3$; at $n = 4$ the powers are
$R^{-(n-2)-d_j}$.)

**Lemma 3.3 ([CD03] Lemma 3.18).** Let $U',V'\subset\mathbb R^m$ be open, $G:U'\to V'$ a homeomorphism, and
$G_\lambda:U'\to\mathbb R^m$ continuous with $G_\lambda\to G$ uniformly as $\lambda\to\infty$. For every $y\in V'$ and
every $\lambda$ large there is $x_\lambda\in U'$ with $G_\lambda(x_\lambda) = y$. If $\bar B(y,r')\subset V'$,
$x_\lambda$ can be taken in $G^{-1}(\bar B(y,r'))$.

*Proof.* $u_\lambda := \mathrm{Id}-G_\lambda\circ G^{-1}$ tends to $0$ uniformly on $\bar B(y,r')$. Once $\max_{\bar
B(y,r')}|u_\lambda|\le r'$, the map $z\mapsto y+u_\lambda(z)$ is continuous from $\bar B(y,r')$ to itself and has a
fixed point $y_\lambda$ by Brouwer's theorem (cited). Then $x_\lambda := G^{-1}(y_\lambda)$ satisfies
$G_\lambda(x_\lambda) = y_\lambda-u_\lambda(y_\lambda) = y$. $\square$

*Step 5: conclusion.* Apply Lemma 3.3 with $U'$ the interior of $\bar B$, $G(Q) := Q-\mathfrak Q^0$, $G_R$ from (3.2)
and $y = 0$. For every $r'>0$ below the radius of $\bar B$ there is $R(r')$ such that for $R\ge R(r')$ some $Q_R$ with
$|Q_R-\mathfrak Q^0|\le r'$ has $G_R(Q_R) = 0$; put $R_{\mathrm{gl}} := R(r'_0)$ for one such $r'_0$. Then $F_R(Q_R) =
0$ and, by Step 3, $(J,\rho)(\hat x_{Q_R,R}) = 0$. Put $p_R := p(Q_R)$, and let $(\hat g_R,\hat K_R)$ be $(g,K)$ on
$\{R_0<r\le R\}$, $\sigma_R^{-1}\hat x_{Q_R,R}$ on $\Gamma(R,4R)$ and $(g_{p_R},K_{p_R})$ on $\{r\ge4R\}$. These are
smooth, as $\chi$ is constant near $\partial M$ and $\delta x$ extends smoothly by zero. They are vacuum everywhere, and
$\hat g_R$ is Riemannian, being $C^0$-close to $\delta$ on $\Gamma(R,4R)$. Finally $\mathfrak q(p_R) = Q_R$, and
choosing $Q_R$ with the least admissible $r'$, $r'(R)\to0$, gives $\mathfrak q(p_R)\to\mathfrak Q^0$. $\square$

**Remark 3.4 (what Part VII takes from Theorem 3.1).** The data $(\hat g_R,\hat K_R)$ equal, for $r\ge4R$, the data that
$G_{p_R} = \Phi_{p_R}^*g^{\mathrm{KS}}_{\mu,A}$ induces on $\{y^0 = 0\}$. By uniqueness for the vacuum Cauchy problem,
their development contains the domain of dependence of $\{r>4R\}$ in $G_{p_R}$: a Poincaré transform of a Myers-Perry
metric with parameters near $b_0$. Part VII relates this transform to the boosts of III.B section 5 and the translations
of III.J, and checks that the data of the route have charges in $V$. Proposition 1.3 (a) reduces this to closeness to
Tangherlini's data in $|||\cdot|||_{\alpha,2}$.

## 4. Findings, labels and sources

(V1) *No parity condition at n = 4.* [CD03] (8.1) asks the parity condition (E.9) so that the angular momentum and
centre of mass converge and so that the errors of (8.6) lie below the main terms. At $n = 4$ with $\alpha>\frac32$ both
follow from the decay alone, since $2\alpha>n-1 = 3$ (Proposition 1.3, (3.2)). The record's reading of (8.1) with $k^+$
for $K^-$ and its change of slice to $\Sigma''$ (10.63 (b), D133) are therefore not needed for Theorem 3.1. The record
noted the decay alternative (10.66 (d), D143). The Myers-Perry members are taken in Kerr-Schild form, where the shift is
odd and of the same order as the metric, $r^{-2}$, which (E.9) would exclude.

(V2) *The family's charges are computed here.* Proposition 2.3 replaces Proposition 10.47 (`general5.py` G2) and the
readings of [ER08] (34) and [CD03] (E.14) used in 10.63 (a). Only the derivative at Tangherlini is needed: four scalars
computed by hand, and Schur's lemma for the zero blocks. In ADM units the values agree with Proposition 10.47: energy
$\frac{3\pi\mu}8$, momentum per unit rapidity equal to the energy, angular momentum $\frac{\pi\mu}4$ per unit spin,
centre of mass shifted by the translation. A numerical check of all 225 entries at large radius is `checks/jac5.py`.

(V3) *[CD03]'s indices at n = 4.* The convergence rate of (8.3) is $\beta = \min(\alpha,n-2)$, printed as
$\min(\alpha,1)$, and (8.7)'s $R^{-1}$ is $R^{-(n-2)-d}$. Theorem 5.6 states $s\ge n-2$ where its proof uses $s\ge n-1$,
and (8.5) prints $s = t-1$ where $s = t+n-2$ is the index (8.5) states (10.66 (c)). Both are avoided here by Theorem
5.9's exponentially weighted spaces, which [CD03] uses for smooth data (Proposition 5.10, Corollary 5.11).

(V4) *Continuity in the parameter.* [CD03] Theorem 3.19 applies Lemma 3.18 to $F_\lambda$, which must be continuous in
$Q$; the source leaves this implicit. It is Lemma 3.2 here. Uniqueness and continuity follow from the uniform bound of
Theorem 3.6 and from product estimates in the weighted spaces, which are deduced here (finding (V8)).

(V5) *Scope.* The Proposition F.1 equivalent is proved near Tangherlini only; its global form for the Myers-Perry family
is not attempted. Theorem 3.1 needs $\mathfrak Q^0\in V$, which is closeness to Tangherlini (Remark 3.4). The plan's row
V named [HHV21] beside [CD03] for its two perturbation arguments (record 10.68): the openness of invertibility (record
Lemma 10.52 (P1)) and the semicontinuity of the kernel ((P2)). Neither is used in this part. Where the write-out needs
the facts they give at $b$ near $b_0$, it proves them in place; for example the openness of invertibility uniformly in
$b$ is I.A Theorem 8.1, cited in III.F$''$.

(V6) *A normalisation* (verifier 136's V-m3). Proposition 1.3 assumed $|||(g,K)|||_{\alpha,2}\le1$, which the members of
the family need not satisfy, and Theorem 3.1 reached it by a rescaling that would move the charges out of $V$. The bound
is not used; it is dropped, and the rescaling with it.

(V7) *The projection* (verifier 136's V-m1). [CD03]'s projection is orthogonal in $L^2_\psi$ of the current metric, so
its kernel is the KIDs converted by $g'$, not the KIDs. Step 3 now pairs with the converted KIDs, whose Gram matrix
tends to the flat one.

(V8) *Continuity and the Lipschitz derivative* (verifier 136's V-m2). Lemma 3.2 had read both at p. 26, which states
differentiability only. They are deduced from the product estimates of the weighted spaces.

*Labels.*

| Here | [CD03] |
|---|---|
| (0.1) | (2.1) |
| Lemma 1.1 | (2.4); the KIDs of p. 36 |
| Lemma 1.2 | (E.15)-(E.16), (E.27), in linear 3+1 form |
| Proposition 1.3 | Proposition E.1, (E.17)-(E.20), without (E.9) |
| Lemma 1.4 | (8.2)-(8.3), (8.6) |
| Proposition 2.3, Corollary 2.4 | Proposition F.1 (its equivalent near Tangherlini, Remark 8.2) |
| Step 1 | Theorems 3.6, 3.9, 5.9, Corollary 5.11, Proposition G.1 |
| Lemma 3.2 | the continuity behind Theorem 3.19 |
| Lemma 3.3 | Lemma 3.18 |
| Theorem 3.1 | Theorem 8.1, Remarks 8.3-8.4 |

*Sources.* [CD03] (arXiv:gr-qc/0301073v2; printed page = PDF page): pp. 4-6 ((2.1)-(2.6), Lemma 2.3), 13-14 (Theorems
3.6, 3.7, 3.9, (3.9)-(3.14)), 18-19 ((3.28)-(3.29), Lemma 3.18, Theorem 3.19), 22-27 ((5.2), Theorems 5.4, 5.6, 5.9,
Proposition 5.10, Corollary 5.11), 35-38 (section 8.1, Theorem 8.1, Remarks 8.2-8.4, section 8.2), 71-77 (Appendices
E-F), 77-78 (Proposition G.1), read at source. Inputs: III.B section 3 (Lemma 3.1, Definition 3.2, Proposition 3.4, the
parameter set); N1STAR-PROOF.md 10.47, 10.63, 10.66, 10.68.
