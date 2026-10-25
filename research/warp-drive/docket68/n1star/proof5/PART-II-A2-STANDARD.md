# Part II.A$'$. The standard estimates on e3b-spaces: coefficients of finite regularity, variable orders, at n = 4

*Status.* Written out in full (D193). Read line by line by the seventy-ninth verifier, whose major finding (the class of
symbols of finite regularity, and with it the square-root lemma) and seven minor findings and nits are seated (D195); the
eightieth verifier read those repairs and confirmed each, and its two minor findings and six nits are seated (D196); they
await the next reader. Nothing here is labelled proved. This part proves the two standing inputs (L3) and (L4) of Part
II.A (`PART-II-A-SETUP.md`, section 9.1): the elliptic and the real principal type estimates on e3b-spaces without
b-regularity, for operators whose coefficients have finite regularity, with variable orders and constants locally uniform
in the operator. They are [Hin26c] Propositions 3.23 and 3.24 at $k = 0$ (pp. 69-71), which the source proves by citation
to the standard arguments. The hypotheses of the latter are corrected (section 6, (G6)-(G7)). Part II.A is cited as II.A,
Part I.A (`PART-I-SPECTRAL.md`) as I.A.

*Method.* Nothing here depends on the dimension. The smooth calculus is the one READ in II.A section 3: (S1)-(S11) of
[SBG] = P. Hintz, *Pseudodifferential operators on manifolds with scaled bounded geometry*, arXiv:2408.06651v1. Its
operations are continuous on Fréchet spaces of symbols, so each of them is bounded by finitely many seminorms (section
2.1). A bound that holds for smooth symbols with finitely many seminorms passes to symbols of finite regularity by
mollification in the charts of the secondary structure and weak lower semicontinuity (section 2.2, as in II.A Lemma
8.5). This gives a calculus for symbols of finite regularity with explicit remainder bounds (Proposition 2.4). The
elliptic estimate then follows from a parametrix of finite regularity (section 3). The propagation estimate follows from
a positive commutator argument (section 4). Its commutant is built in flow-box coordinates of the exact Hamilton field,
which has finite regularity (section 5). Every square that the argument needs is an exact square of a symbol of finite
regularity, so no Gårding inequality is used.

*How it is organised.* Section 1: the setting and the statements. Section 2: the calculus of finite regularity. Section
3: Theorem 3.1, which is (L3). Section 4: the positive commutator lemma and its iteration. Section 5: Theorem 5.4, which
is (L4). Section 6: findings.

## 1. Setting and statements

### 1.1 The calculi

$\tilde M$ is the compactified spacetime of II.A section 1, with its scaled bounded geometry structure $\mathcal
B^\times$ of II.A section 4.1 and the secondary bounded geometry structure $\rho\mathcal B$ obtained by subdividing the
unit cells into $\rho$-cuboids ([Hin26c] (3.26); [SBG] section 3.2). $\rho\mathcal B$ is a scaled bounded geometry
structure with all scalings equal to 1. So everything READ in II.A section 3 holds for it. Its operator Lie algebra,
which is also its coefficient Lie algebra, is the large operator Lie algebra $\mathcal V' = C^\infty_{e3b}\mathcal
V_{e3b}$ of $\mathcal B^\times$ ([SBG] Proposition 3.3 and Remark 3.48). It defines the same Sobolev spaces as $\mathcal
V = C^\infty_b\mathcal V_{e3b}$: an elliptic element of $\Psi^{\mathsf s}_{\mathcal V}$ lies in $\Psi^{\mathsf
s}_{\mathcal V'}$ ([SBG] Remark 3.48) and is elliptic there, and each space is the set of $u$ that a fixed elliptic
operator maps into $L^2$. We write:

$\tilde S^m$ for the symbols of $\rho\mathcal B$ of order $m$. In each chart of $\rho\mathcal B$, with fibre coordinates
dual to the coordinate frame, these are the functions with $|\partial_x^\beta\partial_\xi^\gamma a|\le C_{\beta\gamma}
\langle\xi\rangle^{m-|\gamma|}$ uniformly ((S4)). This is a Fréchet space with the seminorms $\|a\|_{M;m}$, the largest
of these constants over $|\beta|+|\gamma|\le M$. By (S1)-(S4), $\tilde S^m$ is the class $C^\infty_{e3b}S^m$ of [Hin26c]
(3.26): symbols whose coefficients are bounded under any number of e3b-derivatives.

$\tilde\Psi^m := \Psi^m_{\rho\mathcal B}$, $\mathrm{Op} := \mathrm{Op}_{\rho\mathcal B}$, and $\tilde\Psi^{-\infty}$ for
its residual operators ((S4)). $C^\infty_b\Psi^m_{e3b}\subset\tilde\Psi^m$ ([SBG] Remark 3.48; II.A section 4.2). The
Sobolev spaces of $\rho\mathcal B$ are therefore the $H^{\mathsf s}_{e3b}$ of II.A.

The properties used, all READ: (S5) mapping properties, with operator norms bounded by a seminorm; compositions,
adjoints, principal symbols and commutators; the continuity of $\mathrm{Op}:\tilde S^m\to\tilde\Psi^m$, of composition
as a bilinear map and of the adjoint ([SBG] Remark 3.47, READ in (S5)); and the principal symbol sequence: $A\in
\tilde\Psi^m$ with vanishing principal symbol lies in $\tilde\Psi^{m-1}$. Also (S8) for variable orders, (S10) for
commutators with $\mathcal V_{b,[e3b]}$, and (S11) for weights.

*Left quantization.* In [SBG] (3.26) the local quantization is $(\mathrm{Op}_\beta(b)u)(x) = (2\pi)^{-n}\int e^{i(x-x')
\cdot\xi}\psi(x-x')b(x,\xi)u(x')\,dx'\,d\xi$. Since $\psi = 1$ near 0 ([SBG] p. 43) and the partition $\chi_\alpha$ of
[SBG] (3.28) sums to 1, $\mathrm{Op}(f)$ is multiplication by $f$ for a function $f$ of the base alone; in particular
$\mathrm{Op}(1) = I$. The symbol is evaluated at the left variable, so for every function $f$ of the base
$$f\cdot\mathrm{Op}(a) = \mathrm{Op}(fa).\tag{1.1}$$

*Variable orders.* Fix $\rho_\infty\in\tilde S^{-1}$, positive, equal to $(\sum_j\xi(V_{0,j})^2)^{-1/2}$ for $|\xi|\ge1$
(the $V_{0,j}$ of II.A Lemma 2.9), so $\rho_\infty$ is a defining function of fibre infinity ${}^{e3b}S^*\tilde M$.
Variable orders are functions $\mathsf k\in C^\infty({}^{e3b}S^*\tilde M)$, extended homogeneously of degree 0 near fibre
infinity. The class of (S8) is that of [SBG] Definition 4.6 (p. 66): for variable $\mathsf k$, $\tilde S^{\mathsf k}
:=\rho_\infty^{-\mathsf k}\bigcap_{\delta\in(0,\frac12)}\tilde S^0_{1-\delta,\delta}$, contained in $\bigcap_\delta\tilde
S^{\sup\mathsf k}_{1-\delta,\delta}$; the defining function of fibre infinity used there may be replaced by
$\rho_\infty$, their quotient being a positive symbol of order 0. Its operators map $H^{\mathsf t}_{e3b}$ to $H^{\mathsf
t-\mathsf k}_{e3b}$ for every variable order $\mathsf t$, without loss, and the calculus of [SBG] Theorem 3.51 (adjoints,
compositions, commutators) holds for them, with the principal symbols of compositions taken modulo $\bigcap_\delta\tilde
S^{\mathsf k_1+\mathsf k_2-1+2\delta}$. The source states that orders are additive under composition, gives this class of
principal symbols in its (4.10), and says that "Theorem 3.44 remains valid, mutatis mutandis". Its Theorem 3.44 is the
boundedness theorem; the context, composition, shows that the calculus of its Theorem 3.51 is meant as well. That reading
is a READ decision, recorded here (the eightieth verifier, D196). Derivatives of $\rho_\infty^{-\mathsf k}$ carry factors
$\log\rho_\infty$, as in I.A Remark 3.3, and the symbols of finite regularity below carry a counted number of such
factors (Definition 1.3). The class $\rho_\infty^{-\mathsf k}\tilde S^0$, with bounded derivatives, is too small for
them: the seventy-ninth verifier (D195) found symbols outside it used as if inside. We write "of order $\mathsf k-1+$"
for "of order $\mathsf k-1+\delta$ for every $\delta>0$", with constants depending on $\delta$.

### 1.2 Classical symbols and the locus of microlocalisation

Let ${}^{e3b}\overline T{}^*\tilde M$ be the radial compactification of the fibres of ${}^{e3b}T^*\tilde M$ over the
compact manifold with corners $\tilde M$. It is a compact manifold with corners, whose boundary at fibre infinity is
${}^{e3b}S^*\tilde M$.

**Lemma 1.1 (classical symbols).** Let $a\in C^\infty({}^{e3b}\overline T{}^*\tilde M)$. Then $a\in C^\infty_bS^0\subset
\tilde S^0$. Consequently $\rho_\infty^{-m}a\in C^\infty_bS^m$ and $\rho_\infty^{-\mathsf k}a\in\tilde S^{\mathsf k}$.

*Proof.* Use the global fibre coordinates $\zeta_j := \xi(V_{0,j})$, in which ${}^{e3b}T^*\tilde M = \tilde M\times
\mathbb R^N$ (a vector bundle map onto its image, of full rank, II.A Lemma 2.9). In a cell of $\mathcal B^\times$ with
coordinates $x$ and scalings $\rho_\alpha$, the fibre coordinates of (S4) are $\xi$ with
$\xi\cdot\frac{dx}{\rho_\alpha}$. They are related to $\zeta$ by $\zeta_j = \sum_iv^i_{\alpha,j}(x)\xi_i$, where
$(\phi_\alpha)_*V_{0,j} = \sum_iv^i_{\alpha,j} \rho_{\alpha,i}\partial_i$ with $v_\alpha$ uniformly bounded in
$C^\infty$ ((S1)). This map has a uniformly bounded inverse on its range, the $V_{0,j}$ spanning $\mathcal V$ uniformly
in each cell (II.A section 4.1). A smooth function on the compactified bundle has, in the coordinates $(x,\zeta)$,
$x$-derivatives along b-vector fields of $\tilde M$ bounded, and $\zeta$-derivatives of order $\gamma$ bounded by
$C\langle\zeta\rangle^{-|\gamma|}$ (radial compactification). The coordinate fields $\partial_{x^i}$ of a cell are
uniformly bounded combinations of b-vector fields, as the coefficient algebra is $C^\infty_b\mathcal V_b$ ((S1)). The
chain rule through $\zeta = v_\alpha(x)\xi$ then gives the estimates of (S4) uniformly in $\alpha$, with
$W$-derivatives, so $a\in C^\infty_bS^0$. The rest follows from (S8). $\square$

*Microsupport, ellipticity.* An operator $A\in\tilde\Psi^m$ is *microsupported* in a closed set $K\subset{}^{e3b}
\overline T{}^*\tilde M$ if $A = \mathrm{Op}(a)+R$ with $a\in\tilde S^m$, $\mathrm{supp}\,a\subset K$ and
$R\in\tilde\Psi^{-\infty}$. Following [Hin26c] p. 55, the locus of microlocal analysis is ${}^{e3b}S^*\tilde M$. If
$\mathrm{WF}'_{e3b}(A)\subset O$ with $O\subset{}^{e3b}S^*\tilde M$ open, then $A$ is microsupported in any closed
neighbourhood $K$ of $\mathrm{WF}'_{e3b}(A)$ in the compactified bundle with $K\cap{}^{e3b}S^*\tilde M\subset O$.
Indeed, if $\tilde\chi\in C^\infty({}^{e3b}\overline T{}^*\tilde M)$ equals 1 near $\mathrm{WF}'(A)$ and is supported in
$K$, then $A = \mathrm{Op}(\tilde\chi a)+\mathrm{Op}((1-\tilde\chi)a)+R$, and $(1-\tilde\chi)a$ is residual, by the
definition of the operator wave front set ((S5)). For $L$ as in section 1.3 with principal symbol $\ell$,
$\mathrm{Ell}(L)\subset{}^{e3b}S^* \tilde M$ is the set of points with a neighbourhood $U$ in the compactified bundle on
which $\ell$ is invertible with $|\ell^{-1}|\le C\rho_\infty^m$ for $|\xi|\ge1$. It is open, and $\mathrm{Char}(L)$ is
its complement.

**Lemma 1.2 (disjoint microsupports).** Let $K_1,K_2\subset{}^{e3b}\overline T{}^*\tilde M$ be disjoint closed sets.
Then the distance between $K_1$ and $K_2$ in the coordinates $(x,\zeta/|\zeta|,\log|\zeta|)$ of each chart of $\rho
\mathcal B$, for $|\zeta|\ge1$, is bounded below uniformly. For $a_i\in\tilde S^{m_i}$ supported in $K_i$,
$\mathrm{Op}(a_1) \mathrm{Op}(a_2)\in\tilde\Psi^{-\infty}$, and the map
$(a_1,a_2)\mapsto\mathrm{Op}(a_1)\mathrm{Op}(a_2)$, on the closed subspaces of symbols supported in $K_1$ and in $K_2$,
is continuous into $\tilde\Psi^{-N}$ for every $N$.

*Proof.* The charts of $\rho\mathcal B$ are, uniformly, rescalings of charts of the compact manifold with corners in
which cells near the boundary are magnified. Distances therefore do not shrink: a smooth metric on the compact
${}^{e3b}\overline T{}^*\tilde M$ is bounded by a constant times the Euclidean metric of each chart. So the symbols have
disjoint essential supports in [SBG]'s sense, being uniformly separated. The wave front set of the composition is empty
((S5)), so it is residual. The bilinear map is continuous into $\tilde\Psi^m$ ((S5)) and takes values in
$\tilde\Psi^{-N}$. Its graph in $\tilde\Psi^{-N}$ is closed, since convergence in $\tilde\Psi^{-N}$ implies convergence
in $\tilde\Psi^m$. So it is separately continuous into $\tilde\Psi^{-N}$ by the closed graph theorem, hence jointly
continuous on these Fréchet spaces. $\square$

### 1.3 The operators and the statements

**Definition 1.3.** Derivatives are taken in the coordinates $(x,\omega,\tau) = (x,\zeta/|\zeta|,\log|\zeta|)$ of Lemma
2.2 (for $|\zeta|\ge1$, and $(x,\zeta)$ near the zero section) in the charts of $\rho\mathcal B$, and
$\langle\log\rho_\infty\rangle := (1+(\log\rho_\infty)^2)^{1/2}$. For $M,\nu\in\mathbb N_0$ and a variable order $\mathsf
m$, $C^{(M)}_\nu\tilde S^{\mathsf m}$ is the space of $a = \rho_\infty^{-\mathsf m}a_0$ with $a_0$ a function on
${}^{e3b}T^*\tilde M$ whose derivatives of order $j\le M$ are bounded by $C\langle\log\rho_\infty\rangle^{\nu j}$,
uniformly in the charts; the norm $\|a\|_{(M);\nu,\mathsf m}$ is the least such $C$. $\tilde S^{\mathsf m}_\nu$ is the
space of smooth $a$ with $\|a\|_{(M);\nu,\mathsf m}<\infty$ for every $M$, a Fréchet space with these seminorms. The
index $\nu$ is dropped when $\nu = 0$. A class of index $\nu$ lies in those of larger index; products satisfy
$\|ab\|_{(M);\nu,\mathsf m_1+\mathsf m_2}\le C\|a\|_{(M);\nu,\mathsf m_1}\|b\|_{(M);\nu,\mathsf m_2}$ by Leibniz's rule.
As $\partial_\zeta$ is $e^{-\tau}$ times bounded combinations of $\partial_\omega$, $\partial_\tau$ (Lemma 2.2) and
$\langle\log\rho_\infty\rangle^{\nu j}\le C_\delta\rho_\infty^{-\delta j}$, $\tilde S^{\mathsf m}_\nu$ is contained,
continuously, in the class $\rho_\infty^{-\mathsf m}\bigcap_\delta\tilde S^0_{1-\delta,\delta}$ of (S8), also when
$\mathsf m$ is constant; for constant $\mathsf m = m$, $\tilde S^m_0$ is the class $\tilde S^m$ of (S4). The derivatives
of $\log\rho_\infty$ of positive order are bounded, as $\log\rho_\infty = -\tau$ near fibre infinity. For a finite set
$\mathcal P = \{P_1,\dots,P_J\}\subset C^\infty_b\Psi^m_{e3b}$ of operators localized near the diagonal (II.A section
8.3), with $P_j = \mathrm{Op}(p_j)+R_j$, $p_j\in C^\infty_bS^m$, $R_j\in\tilde\Psi^{-\infty}$, and $a_j\in C^{d_0}_{e3b}$
(II.A Definition 8.1), the operator $L = \sum a_jP_j$ satisfies, by (1.1),
$$L = \mathrm{Op}(\ell_f)+\sum_ja_jR_j,\qquad\ell_f := \sum_ja_jp_j\in C^{(d_0)}\tilde S^m,\tag{1.2}$$
with $\|\ell_f\|_{(d_0);m}\le C\max_j\|a_j\|_{C^{d_0}_{e3b}}$, as e3b-derivatives of the $a_j$ are the rescaled
coordinate derivatives in the charts. Its principal symbol is $\ell := \sum_ja_j\sigma(P_j)$, with $\sigma(P_j)$ a
representative of order $m$ of the principal symbol. On $\mathbb C^{N'}$-valued functions everything is matrix-valued.

The statements proved are the following. Here $B,E,G$ are carried by $\chi$ in the sense of II.A section 8.3, and the
estimates are in the strong sense: the left side is finite when the right side is.

(L3) = **Theorem 3.1.** Let $\mathsf s,N$ be given. There is $d_0 = d_0(m,\mathsf s,N)$ such that for every finite
$\mathcal P\subset C^\infty_b\Psi^m_{e3b}$, every $N'$, $L\in C^{d_0}_{e3b}\mathcal P$ on $\mathbb C^{N'}$, and $B,G$
with $\mathrm{WF}' (B)\subset\mathrm{Ell}(G)\cap\mathrm{Ell}(L)$,
$$\|Bu\|_{H^{\mathsf s}}\le C\big(\|GLu\|_{H^{\mathsf s-m}}+\|\chi u\|_{H^{-N}}\big).$$
$C$ depends on $L$ only through $\max_j\|a_j\|_{C^{d_0}_{e3b}}$ and a lower bound for the ellipticity of $\ell$ near
$\mathrm{WF}'(B)$, so it is locally uniform.

(L4) = **Theorem 5.4.** The real principal type estimate for $L = L_0+L_1+L_2$ as in II.A (L4), which carries the
corrections (G6)-(G7) (D194): $d_0$ is chosen before $L$, $\chi$ is supported away from $I^0\cup K^-$, and the hypothesis
on $\mathsf s$ is as corrected in (G6): $\mathsf H\mathsf s\le0$ on a neighbourhood of the backward segments of the
integral curves from $\mathrm{WF}'(B)\cap\mathrm{Char}(L)$ up to $\mathrm{Ell}(E)$. In (L4) the $P\in\mathcal P_m$ are
taken with principal symbols that are smooth and homogeneous near fibre infinity (classical), as the source's statement
presupposes when it asks for a homogeneous principal symbol and a Hamilton field continuous on ${}^{e3b}S^*\tilde M$.

## 2. The calculus of finite regularity

### 2.1 Seminorm bounds

**Lemma 2.1.** Let $X_1,\dots,X_r$ and $Y$ be Fréchet spaces and $T:X_1\times\dots\times X_r\to Y$ continuous and
multilinear. For every continuous seminorm $q$ on $Y$ there are continuous seminorms $p_i$ on $X_i$ and $C$ with
$q(T(x_1,\dots,x_r))\le C\prod_ip_i(x_i)$. A multilinear map between Fréchet spaces that is continuous in each variable
separately is continuous.

*Proof.* By continuity at 0 there are $p_i$ with $q(T(x))<1$ whenever $p_i(x_i)<1$ for all $i$. For general $x$ with
$p_i(x_i)\ne0$, apply this to $x_i/(2p_i(x_i))$ and use multilinearity, which gives $C = 2^r$. If some $p_i(x_i) = 0$,
then $tx_i$ satisfies $p_i(tx_i)<1$ for all $t$, so $q(T(x)) = 0$. The second statement is the theorem of Banach and
Steinhaus for separately continuous bilinear maps on Fréchet spaces, extended to $r$ factors by induction. $\square$

A map from a Fréchet space $X$ to a Banach space $Z$ that is linear with closed graph is continuous (closed graph
theorem). It is then bounded by $C$ times a seminorm of $X$. The seminorms of $\tilde S^m$ are increasing in $M$, so
such a bound has the form $C\|x\|_{M;m}$.

### 2.2 Mollification

**Lemma 2.2.** Let $a\in C^{(M)}_\nu\tilde S^{\mathsf m}$, $M\ge1$. There are $a_\epsilon\in\tilde S^{\mathsf m}_\nu$,
$\epsilon\in(0,1]$, such that (i) $\|a_\epsilon\|_{(M');\nu,\mathsf m}\le C\|a\|_{(M');\nu,\mathsf m}$ for $M'\le M$;
(ii) $a_\epsilon\to a$ pointwise, with $|a_\epsilon-a|\le C\epsilon\|a\|_{(1);\nu,\mathsf
m}\langle\log\rho_\infty\rangle^\nu\rho_\infty^{-\mathsf m}$, and $\|a_\epsilon-a\|_{(M-1);\nu,\mathsf m+\delta}\le
C_\delta\epsilon\|a\|_{(M);\nu,\mathsf m}$ for every $\delta>0$; (iii) if $a$ is supported in a closed set $K$ of the
compactified bundle, then $a_\epsilon$ is supported in the $\epsilon$-neighbourhood of $K$ in the coordinates of Lemma
1.2.

*Proof.* Write $a = \rho_\infty^{-\mathsf m}a_0$ and mollify $a_0$. In each chart $\psi_\beta$ of $\rho\mathcal B$, with
a uniformly smooth partition of unity $\theta_\beta$ (II.A Lemma 8.5), use coordinates $(x,\omega,\tau) :=
(x,\zeta/ |\zeta|,\log|\zeta|)$ for $|\zeta|\ge1$, and $(x,\zeta)$ near the zero section, glued by a fixed partition of
unity in $\zeta$. The estimates of $\tilde S^0$ for $a_0$ are equivalent, uniformly, to bounded derivatives in
$(x,\omega,\tau)$: $\partial_\zeta$ is $e^{-\tau}$ times a combination of $\partial_\omega$, $\partial_\tau$ with bounded
coefficients. Put $a_{0,\epsilon} := \sum_\beta(\theta_\beta a_0)*\eta_\epsilon$, the convolution taken in
$(x,\omega,\tau)$ (on the sphere, in a fixed finite atlas). Derivatives commute with convolution; the charts have
uniformly bounded transitions and finite multiplicity; and $\langle\log\rho_\infty\rangle$ changes by at most a bounded
factor over a unit ball in these coordinates, as $\log\rho_\infty = -\tau$. Hence (i). A derivative of $a_{0,\epsilon}$
of order $j>M$ puts $j-M$ derivatives on $\eta_\epsilon$, so $a_{0,\epsilon}$ satisfies the bounds of every order, with
constants depending on $\epsilon$: $a_\epsilon\in\tilde S^{\mathsf m}_\nu$. (ii) is the mean value theorem: a derivative
of order $j\le M-1$ of $a_{0,\epsilon}-a_0$ is bounded by $C\epsilon\langle\log\rho_\infty\rangle^{\nu(j+1)}$, the factor
$\rho_\infty^\delta\langle\log\rho_\infty\rangle^\nu$ is bounded, and the derivatives of $\rho_\infty^\delta$ are
$\rho_\infty^\delta$ times bounded functions. (iii) is the support of $\eta_\epsilon$. $\square$

### 2.3 Quantization and remainders

**Lemma 2.3 (density, and a regularising family).** (a) $C_c^\infty(\tilde M^\circ)$ is dense in $H^{\mathsf s}_{e3b}$
for every variable order $\mathsf s$. (b) Let $K\in\mathbb N$ and $T_t := \mathrm{Op}(\tau_t)$, $\tau_t := (1+t
\rho_\infty^{-1})^{-K}$, $t\in(0,1]$. Then $T_t$ is bounded in $\tilde\Psi^0$, lies in $\tilde\Psi^{-K}$ for each $t$,
and $T_t\to I$ strongly on every $H^{\mathsf s}_{e3b}$ as $t\to0$.

*Proof.* (a) If not, there is $0\ne w$ in the dual space $H^{-\mathsf s}$ ((S3), (S11)) annihilating $C_c^\infty$; then
$w = 0$ as a distribution, a contradiction. (b) $\tau_t$ is bounded in $\tilde S^0$: $\rho_\infty\partial_{\rho_\infty}$
of it is $K t\rho_\infty^{-1}(1+t\rho_\infty^{-1})^{-1}\tau_t$, bounded, and the other derivatives act on $\rho_\infty$
only through such factors. It lies in $\tilde S^{-K}$ for fixed $t>0$. Moreover
$|1-\tau_t|\le\min(1,Kt\rho_\infty^{-1})\le K (t\rho_\infty^{-1})^\delta$, and likewise for its derivatives, so
$\tau_t\to1$ in $\tilde S^\delta$ for every $\delta>0$. So $\|(T_t-I)v\|_{H^{\mathsf s}}\to0$ for $v\in H^{\mathsf
s+\delta}$, by (S5). $T_t$ is uniformly bounded on $H^{\mathsf s}$, and $C_c^\infty\subset H^{\mathsf s+\delta}$ is
dense by (a), so the convergence holds on all of $H^{\mathsf s}$. $\square$

For $a\in C^{(M)}_\nu\tilde S^{\mathsf m}$ and $u\in C_c^\infty(\tilde M^\circ)$, $\mathrm{Op}(a)u$ is defined by [SBG]
(3.26)-(3.28). The local quantization is $(2\pi)^{-n}\int e^{ix\cdot\xi}b(x,\xi)\mathcal F(\psi(x-\cdot)u)(\xi)\,d\xi$,
where the Fourier transform is rapidly decreasing in $\xi$, locally uniformly in $x$. So the integral converges
absolutely for any $b$ of polynomial growth, and only finitely many charts meet the support of $u$.

**Proposition 2.4 (finite regularity).** Let $\mathsf t$ be a variable order, $\nu\in\mathbb N_0$, and $\mathsf m,\mathsf
m_1,\mathsf m_2$ orders, constant or variable. There are $M$ and $C$, depending on these orders, on $\nu$ and on
$\delta>0$, with the following, for symbols in $C^{(M+2)}_\nu\tilde S$ of the stated orders (symbols of different indices
are taken in the largest). Throughout, "order $r$" means bounded from $H^{\mathsf t}$ to $H^{\mathsf t-r}$.

(a) $\mathrm{Op}(a)$ extends from $C_c^\infty$ to a bounded operator of order $\mathsf m$, without loss, with norm at
most $C\|a\|_{(M);\nu,\mathsf m}$.

(b) $\mathrm{Op}(a_1)\mathrm{Op}(a_2)-\mathrm{Op}(a_1a_2)$ has order $\mathsf m_1+\mathsf m_2-1+\delta$, with norm at
most $C\|a_1\|_{(M);\nu,\mathsf m_1}\|a_2\|_{(M);\nu,\mathsf m_2}$.

(c) $\mathrm{Op}(a)^*-\mathrm{Op}(\bar a)$ has order $\mathsf m-1+\delta$, with norm at most $C\|a\|_{(M);\nu,\mathsf
m}$. Here the adjoint is with respect to $L^2(|dt\,dx|)$, and matrix-valued symbols use the conjugate transpose.
$|dt\,dx|$ is a weight $w$ times an e3b-density, so this adjoint is $w^{-1}A^\star w$ with $A^\star$ the adjoint for that
density, and conjugation by a weight preserves the classes ((S11)).

(d) $i[\mathrm{Op}(a_1),\mathrm{Op}(a_2)]-\mathrm{Op}(H_{a_1}a_2)$ has order $\mathsf m_1+\mathsf m_2-2+\delta$, with
norm at most $C\|a_1\|_{(M+1);\nu,\mathsf m_1}\|a_2\|_{(M+1);\nu,\mathsf m_2}$. If one of $a_1$, $a_2$ is scalar and the
other matrix-valued, $H_{a_1}a_2$ is taken entrywise.

(e) If two of $a_1,\dots,a_r$ ($r\ge2$) are supported in disjoint closed sets of the compactified bundle, then
$\mathrm{Op}(a_1)\cdots\mathrm{Op}(a_r)$ has order $-N$ for every $N$, with norm at most $C_N$ times the product of the
$(M)$-norms, $M = M(N,r)$.

(f) (General principle.) Let $T(a_1,\dots,a_r)$ be a finite expression in the operators $\mathrm{Op}(a_i)$ and their
adjoints, formed by sums and compositions. Suppose that for smooth symbols it lies in the class of order $\mu$, by (S5)
and (S8): a difference of operators with the same principal symbol is one order lower, and a commutator is one order
lower than the product. Then for symbols of finite regularity the operator given by the same expression has order
$\mu+\delta$, or $\mu$ when all orders are constant and $\nu = 0$. Its norm is at most $C\prod_i\|a_i\|_{(M);\nu,\mathsf
m_i}$. In particular, for $a$ of constant order $m$ with $\nu = 0$ and a real symbol $\check a$ of order $\mathsf k$ and
any index: $D_a := \mathrm{Op}(a)^*-\mathrm{Op}(a^*)$ has order $m-1$, and $[D_a,\mathrm{Op}(\check a)]$ and
$[[D_a,\mathrm{Op}(\check a)],\mathrm{Op}(\check a)]$ have orders $m+\mathsf k-2+\delta$ and $m+2\mathsf k-3+\delta$.

The constants are uniform for symbols bounded in the stated norms. For (e) the supports are fixed, or vary within fixed
disjoint closed sets.

*Proof.* *Smooth symbols.* (a) For smooth $a\in\tilde S^{\mathsf m}_\nu$, $\mathrm{Op}(a)$ is bounded of order $\mathsf
m$, without loss ((S8) and Definition 1.3). The linear map $a\mapsto\mathrm{Op}(a)$ from the Fréchet space $\tilde
S^{\mathsf m}_\nu$ to the bounded operators $H^{\mathsf t}\to H^{\mathsf t-\mathsf m}$ has closed graph: if $a_j\to a$
and $\mathrm{Op}(a_j)\to T$, then $\mathrm{Op}(a_j)u\to\mathrm{Op}(a)u$ pointwise for $u\in C_c^\infty$, by the integral
above, so $T = \mathrm{Op}(a)$ on the dense set $C_c^\infty$ (Lemma 2.3 (a)). So it is continuous, and bounded by
$C\|a\|_{(M);\nu,\mathsf m}$ (section 2.1). (b) By (S5) and (S8), $\mathrm{Op}(a_1)\mathrm{Op}(a_2)$ has principal symbol
$a_1a_2$, as does $\mathrm{Op}(a_1a_2)$, so the difference lies in the class of order $\mathsf m_1+\mathsf m_2-1+\delta$.
The bilinear map into that class is separately continuous by the closed graph argument of Lemma 1.2, using the continuity
of composition into the class of order $\mathsf m_1+\mathsf m_2+\delta$. Lemma 2.1 then applies. (c) is the same, with
$\sigma(A^*) = \overline{\sigma(A)}$. (d) By (S5), $i[\mathrm{Op}(a_1),\mathrm{Op}(a_2)]$ has order $\mathsf m_1+\mathsf
m_2-1+\delta$ and principal symbol $H_{a_1}a_2$. Then $H_{a_1}a_2$ is a symbol of that order, and
$\mathrm{Op}(H_{a_1}a_2)$ has full symbol $H_{a_1}a_2$. So the difference has order one lower; continuity is as in (b).
Its norm involves one more derivative of each symbol, through $H_{a_1}a_2$. (e) Lemma 1.2, and its analogue for $r$
factors, with the same proof: the wave front set of the product is empty ((S5)).

*Finite regularity.* For each item, let $a_{i,\epsilon}$ be the mollifications of Lemma 2.2, with uniformly bounded
norms. For $u\in C_c^\infty$, $\mathrm{Op}(a_{i,\epsilon})u\to\mathrm{Op}(a_i)u$ pointwise and boundedly on compact sets,
by dominated convergence in the integral above; this is all (a) needs. In (b)-(f), (a) is available, $M$ being taken
large enough that (a) applies at the finitely many orders raised by $2\delta$: as $a_i\in C^{(M+2)}_\nu$, Lemma 2.2 (ii)
gives $a_{i,\epsilon}\to a_i$ in $C^{(M+1)}_\nu\tilde S^{\mathsf m_i+\delta}$, so $a_{1,\epsilon}a_{2,\epsilon}$, $\bar
a_{i,\epsilon}$ and $H_{a_{1,\epsilon}}a_{2,\epsilon}$ converge in the $(M)$-norms at orders raised by $2\delta$, and by
(a) every factor of every item converges in operator norm, with a loss of $2\delta$ in the order (the seventy-ninth
verifier: the factors vary with $\epsilon$, so convergence of the outer factors is needed and is given by this). So for
$u\in C_c^\infty$ the composite operators applied to $u$ converge in a Sobolev space of lower order, hence in $\mathcal
D'$. The smooth bounds hold uniformly in $\epsilon$. A bounded sequence in the Hilbert space $H^{\mathsf t-r}$ has weakly
convergent subsequences, whose limits are identified in $\mathcal D'$, and the norm is weakly lower semicontinuous. So
the bounds hold for $u\in C_c^\infty$ with the limit operators, and extend by density (Lemma 2.3 (a)). In (a) this
defines the extension. In (e), the supports of the mollified symbols stay in fixed disjoint closed neighbourhoods for
small $\epsilon$, by Lemma 2.2 (iii) and Lemma 1.2. (f) is proved as (b): for smooth symbols the multilinear map is
continuous into the class of order $\mu+\delta$. It is continuous into a larger class because compositions and adjoints
are continuous, and its graph in the smaller class is closed. Then Lemma 2.1 and the passage to finite regularity apply.
When all orders are constant and $\nu = 0$, the classes are those of (S5) without loss, and the same argument gives order
$\mu$. $\square$

**Lemma 2.5 (square roots).** Let $Q$ be a Hermitian matrix-valued function on a set $W$ of phase space with $Q\ge
c\,\mathrm{Id}$, $c>0$. Derivatives are in the coordinates of Lemma 2.2. (i) If $|\partial^\beta Q|\le
C_0\langle\log\rho_\infty\rangle^{\nu|\beta|}$ for $|\beta|\le M$, then $Q^{1/2}$ and $Q^{-1/2}$ satisfy the same bounds,
with constants depending on $c$, $C_0$, $M$, $\nu$. (ii) Let $Q = Q_0+\lambda\,\mathrm{Id}$, where $Q_0\ge c$ satisfies
the bounds of (i) and $\lambda\ge0$ is scalar with $|\partial^\beta\lambda|\le
C_0\langle\log\rho_\infty\rangle^{1+\nu|\beta|}$ for $|\beta|\le M$. Then for $|\beta|\le M$, with $C$ depending on $c$,
$C_0$, $M$, $\nu$,
$$|\partial^\beta Q^{-1/2}|\le C\langle\log\rho_\infty\rangle^{(\nu+1)|\beta|},\qquad|Q^{1/2}|\le C\langle\log\rho_\infty
\rangle^{\frac12},\qquad|\partial^\beta Q^{1/2}|\le C\langle\log\rho_\infty\rangle^{(\nu+1)|\beta|}\ (\beta\ne0).$$
So $Q^{-1/2}$ is in the class of index $\nu+1$ and order 0, and $Q^{1/2}$ in that of index $\nu+1$ and order $\delta$ for
every $\delta>0$. The index $\nu+1$ cannot be lowered to $\nu$: let $f\ge0$ be smooth, bounded with all derivatives, with
$f(y) = y^2$ near 0, and $Q := c+\langle\log\rho_\infty\rangle f(x\langle\log\rho_\infty\rangle^\nu)$, which satisfies
(ii) with index $\nu$; then $\partial_x^2Q^{1/2} = c^{-1/2}\langle\log\rho_\infty\rangle^{1+2\nu}$ at $x = 0$, beyond the
bound $\langle\log\rho_\infty\rangle^{2\nu}$ of index $\nu$ (the seventy-ninth verifier, D195, at $\nu = 0$, against an
earlier statement with bounded derivatives of $Q^{-1/2}$; the eightieth, D196, for every $\nu$).

*Proof.* (i) $Q^{\pm1/2} = \frac1{2\pi i}\oint_\gamma z^{\pm1/2}(z-Q)^{-1}dz$ for a fixed contour $\gamma$ in
$\{\mathrm{Re}\,z>0\}$ around $[c,C_0]$, at distance at least $c/2$ from it. A derivative $\partial^\beta(z-Q)^{-1}$ is a
sum of products $(z-Q)^{-1}\partial^{\beta_1}Q(z-Q)^{-1}\cdots\partial^{\beta_k}Q(z-Q)^{-1}$ with $\beta_1+\dots+\beta_k
= \beta$ and $|\beta_i|\ge1$, each bounded on $\gamma$ by $C\langle\log\rho_\infty\rangle^{\nu|\beta|}$. (ii) By the
spectral theorem, $Q^{-1/2} = \frac1\pi\int_0^\infty s^{-1/2}(s+Q)^{-1}ds$ and $Q^{1/2} = \frac1\pi\int_0^\infty
s^{-1/2}Q(s+Q)^{-1}ds$. As $Q(s+Q)^{-1} = I-s(s+Q)^{-1}$, for $\beta\ne0$ this gives $\partial^\beta Q^{1/2} =
-\frac1\pi\int_0^\infty s^{1/2}\partial^\beta(s+Q)^{-1}ds$. Now $Q\ge(c+\lambda)\mathrm{Id}$, so
$\|(s+Q)^{-1}\|\le(s+c+\lambda)^{-1}$, and $|\partial^{\beta_i}Q|\le2C_0\langle\log\rho_\infty\rangle^{1+\nu|\beta_i|}$.
Expanding $\partial^\beta(s+Q)^{-1}$ as in (i), a product with $k$ factors $\partial^{\beta_i}Q$ is bounded by
$C(s+c+\lambda)^{-k-1}\langle\log\rho_\infty\rangle^{k+\nu|\beta|}$, with $1\le k\le|\beta|$. Since $\int_0^\infty
s^{\mp\frac12}(s+c+\lambda)^{-k-1}ds = C_k(c+\lambda)^{\pm\frac12-k}\le C_kc^{\pm\frac12-k}$ for $k\ge1$, both derivative
bounds follow. Finally $|Q^{-1/2}|\le c^{-1/2}$ and
$|Q^{1/2}|\le|Q|^{1/2}\le(C_0+C_0\langle\log\rho_\infty\rangle)^{1/2}$. $\square$

**Lemma 2.6 (the supremum bound).** Let $z\in C^{(M)}_\nu\tilde S^0$, possibly matrix-valued, with $M$ large, and
$\eta>0$. Then for every $\delta>0$,
$\|\mathrm{Op}(z)v\|^2\le(\sup|z|^2+\eta)\|v\|^2+C_{\eta,\delta}\|v\|^2_{-\frac12+\delta}$, where $\sup|z|$ is the
supremum of the operator norm of $z$ over phase space.

*Proof.* Let $r := (\sup|z|^2+\eta-z^*z)^{1/2}$, a Hermitian symbol in $C^{(M)}_\nu\tilde S^0$ by Lemma 2.5 (i), as
$\sup|z|^2+\eta-z^*z\ge\eta$. By Proposition 2.4 (b), (c), $\mathrm{Op}(z)^*\mathrm{Op}(z)+\mathrm{Op}(r)^*\mathrm{Op}(r)
= \mathrm{Op}(z^*z+r^*r)+R = (\sup|z|^2+\eta)I+R$, with $R$ of order $-1+2\delta$ and $\mathrm{Op}(1) = I$ (section 1.1).
Pair with $v$: $|\langle Rv,v\rangle|\le C\|v\|^2_{-\frac12+\delta}$. $\square$

*The regulariser.* For $\kappa\in(0,\frac12]$ put $\varphi_\epsilon := (1+\epsilon\rho_\infty^{-1})^{-\kappa}$ and
$\theta_\epsilon := \epsilon\rho_\infty^{-1}(1+\epsilon\rho_\infty^{-1})^{-1}$, $\epsilon\in(0,1]$. For any vector field
$V$,
$$V(\rho_\infty^{-2\mathsf k}\varphi_\epsilon^2) = \rho_\infty^{-2\mathsf k}\varphi_\epsilon^2\big(-2(\mathsf k-\kappa
\theta_\epsilon)\rho_\infty^{-1}V\rho_\infty-2(V\mathsf k)\log\rho_\infty\big).\tag{2.1}$$
This is I.A (3.6) with the variable exponent. $\varphi_\epsilon$ is bounded in $\tilde S^0$, lies in $\tilde
S^{-\kappa}$ for each $\epsilon$, and tends to 1 in $\tilde S^\delta$ for every $\delta>0$ (proof of Lemma 2.3 (b)).
$\theta_\epsilon$ is bounded in $\tilde S^0$ with values in $[0,1)$.

## 3. The elliptic estimate

**Theorem 3.1 ((L3); [Hin26c] Proposition 3.23 at $k = 0$).** Statement as in section 1.3.

*Proof.* Let $K := \mathrm{WF}'(B)$, compact in the open set $O := \mathrm{Ell}(G)\cap\mathrm{Ell}(L)$. Fix $J\in
\mathbb N$, to be chosen, and closed sets $K_0\subset K_1\subset\dots\subset K_{J+2}$ of the compactified bundle, each a
neighbourhood of the previous, with $K\subset K_0^\circ$ and $K_{J+2}\cap{}^{e3b}S^*\tilde M\subset O$. They lie over
the interior of $\{\chi' = 1\}$ for a cut-off $\chi'$ carried by $\chi$ (section 8.3 of II.A), and in $\{|\xi|\ge1\}$
near fibre infinity: choose them inside a set $\{\rho_\infty\le r_0\}$ on which $\ell$ is invertible with
$|\ell^{-1}|\le C_\ell\rho_\infty^m$, as $\mathrm{Ell}(L)$ is defined by such a bound on a neighbourhood. Fix cut-offs
$\tilde\chi_i\in C^\infty({}^{e3b}\overline T{}^*\tilde M)$ with $\tilde\chi_i = 1$ near $K_{i-1}$ and
$\mathrm{supp}\,\tilde\chi_i\subset K_i$, multiplied by base cut-offs so that the operators are carried by $\chi$. Put
$G_i := \mathrm{Op}(\tilde\chi_i)$, $i\ge1$. By section 1.2, $B$ is microsupported in $K_0$: $B = \mathrm{Op}(b)+R_B$
with $\mathrm{supp}\,b\subset K_0$.

*One step.* Let $A$ be of order $\mathsf r$, microsupported in $K_i$, $A = \mathrm{Op}(a)+R_A$, $a\in\tilde S^{\mathsf
r}$ supported in $K_i$, and $i\le J$. Put $q := \tilde\chi_{i+1}a\,\ell^{-1}\in C^{(d_0)}\tilde S^{\mathsf r-m}$, defined
since $\ell$ is invertible on $K_{i+1}$; writing $\ell = \rho_\infty^{-m}\ell_0$, its norms are bounded by those of
$\ell$ and $C_\ell$, by $\partial(\ell_0^{-1}) = -\ell_0^{-1}(\partial\ell_0)\ell_0^{-1}$. By (1.2),
$$\mathrm{Op}(q)L = \mathrm{Op}(q)\mathrm{Op}(\ell_f)+\mathrm{Op}(q)\textstyle\sum_ja_jR_j = \mathrm{Op}(q\ell_f)+D_1+
\mathrm{Op}(q)\sum_ja_jR_j,$$
where $D_1$ has order $\mathsf r-1+\delta$ by Proposition 2.4 (b). Next, $q\ell_f =
\tilde\chi_{i+1}a+\tilde\chi_{i+1}a\ell^{-1} (\ell_f-\ell)$, and $\ell_f-\ell = \sum_ja_j(p_j-\sigma(P_j))\in
C^{(d_0)}\tilde S^{m-1}$. Also $\tilde\chi_{i+1}a = a$. So
$$A = \mathrm{Op}(q)L-E_A,\qquad E_A := D_1+\mathrm{Op}\big(\tilde\chi_{i+1}a\,\ell^{-1}(\ell_f-\ell)\big)+
\mathrm{Op}(q)\textstyle\sum_ja_jR_j-R_A.\tag{3.1}$$
It has order $\mathsf r-1+\delta$, and each of its terms is a composite with a factor whose symbol is supported in
$K_{i+1}$. The term $\mathrm{Op}(q)\sum a_jR_j$ has every order, by Proposition 2.4 (a) and II.A Lemma 8.5 (a) for the
multiplications. Apply (3.1) to $u$, with $\chi u\in H^{-N}$. By the support convention, $Au = A\chi u$, and all terms
make sense once $d_0$ is large for the finitely many orders involved.

$\mathrm{Op}(q)Lu$: write $\mathrm{Op}(q) = \mathrm{Op}(q)G_{i+2}+\mathrm{Op}(q)(I-G_{i+2})$. By Proposition 2.4 (e),
the second term has every order, its symbols being supported in $K_{i+1}$ and in the support of $1-\tilde\chi_{i+2}$,
which are disjoint. So
$$\|\mathrm{Op}(q)Lu\|_{\mathsf r'}\le C\|G_{i+2}Lu\|_{\mathsf r'+\mathsf r-m}+C\|\chi Lu\|_{-N-m},$$
for every order $\mathsf r'$. Further, $\|G_{i+2}Lu\|\le C(\|GLu\|+\|\chi Lu\|_{-N-m})$ by II.A Lemma 8.4 (c), as
$K_{i+2} \cap{}^{e3b}S^*\tilde M\subset\mathrm{Ell}(G)$. Finally $\|\chi Lu\|_{-N-m}\le C\|\chi u\|_{-N}$ by II.A Lemma
8.6 (a).

$E_Au$: in each term, insert $G_{i+2}$ in the same way after the factor supported in $K_{i+1}$; Proposition 2.4 (e) with
three factors bounds the remainder. So $\|E_Au\|_{\mathsf r'}\le C\|G_{i+2}u\|_{\mathsf r'+\mathsf r-1+\delta}+C\|\chi
u\|_{-N}$.

*Iteration.* Take $\delta = \frac12$, $\mathsf r = 0$ and $\mathsf r' = \mathsf s$ for $A = B$; then $A = G_{i+2}$,
$\mathsf r' = \mathsf s-\frac j2$ at step $j$, with $i = 2j$. After $J'$ steps the remaining term is
$\|G_{2J'}u\|_{\mathsf s-J'/2}\le C\|\chi u\|_{-N}$ once $J'/2\ge\sup\mathsf s+N$. Take $J := 2J'$. Summing,
$$\|Bu\|_{\mathsf s}\le C\big(\|GLu\|_{\mathsf s-m}+\|\chi u\|_{-N}\big).$$
The identities (3.1) hold for every $u$ with $\chi u\in H^{-N}$, and each term on the right is finite when the right
side of the estimate is. So the estimate holds in the strong sense. The constants depend on finitely many norms of the
$a_j$, through $\ell_f$, $\ell$ and $q$, and on $C_\ell$, the bound for $\ell^{-1}$ on $K_{J+2}$. For a perturbation of
$L$ that is small in these norms, $\ell$ stays invertible on $K_{J+2}$ with a comparable bound. On $\mathbb C^{N'}$,
$\ell^{-1}$ is the inverse matrix, and nothing else changes. Variable orders enter only through the spaces, on which the
operators of constant order act by Proposition 2.4 (a). $\square$

## 4. The positive commutator lemma

Let $L$ be of the form (1.2), possibly on $\mathbb C^{N'}$, with real scalar principal symbol $\ell$, so that
$\ell_f-\ell \in C^{(d_0)}\tilde S^{m-1}$ (matrix-valued). Put $L_R := \frac12(L+L^*)$ and $L_I := \frac1{2i}(L-L^*)$. By
Proposition 2.4 (c), $L_I$ has order $m-1+\delta$. For a real scalar symbol $\check a$ and $\check A :=
\mathrm{Op}(\check a)$, which need not be self-adjoint,
$$C_{\check a} := i(L^*\check A^*\check A-\check A^*\check AL) = i[L_R,\check A^*\check A]+L_I\check A^*\check A
+\check A^*\check AL_I,\qquad\langle C_{\check a}w,w\rangle = 2\,\mathrm{Im}\langle\check ALw,\check Aw\rangle\tag{4.1}$$
for $w\in H^{K'}_{e3b}$ with $K'$ as in Lemma 4.1 (iii) (algebra: $L = L_R+iL_I$ with $L_R$, $L_I$ formally
self-adjoint). In I.A (3.4) the commutant is self-adjoint and $\check A^*\check A = \check A^2$; here it is not, and
$\check A^2$ in place of $\check A^*\check A$ would make the identity false (the seventy-ninth verifier, D195). Let
$\mathsf s$ be a variable order and $\mathsf k := \mathsf s-\frac12 (m-1)$.

**Lemma 4.1 (one step).** Let $\kappa\in(0,\frac14]$, $\delta_0\in(0,\frac14]$, $\varsigma\in\{1,-1\}$, and let $G,E$ be
carried by $\chi$. Suppose that for $\epsilon\in(0,1]$ there are real scalar symbols $\check a_\epsilon$ and symbols
$b_\epsilon$, $e_\epsilon$, $z_\epsilon$, with the following properties.

(i) $\check a_\epsilon$ is bounded in $C^{(M)}_\nu\tilde S^{\mathsf k}$, lies in $C^{(M)}_\nu\tilde S^{\mathsf k-\kappa}$
for each $\epsilon$, and is supported in a closed set $K_1$ with $K_1\cap{}^{e3b}S^*\tilde M\subset\mathrm{Ell}(G)$. Here
$\nu\in\mathbb N_0$ is fixed, all classes below have index $\nu$, and $M$ is large for the orders involved.

(ii) $b_\epsilon$ is bounded in $C^{(M)}_\nu\tilde S^{\mathsf s+\delta}$ for every $\delta>0$, lies in $C^{(M)}_\nu\tilde
S^{\mathsf s-\kappa+\delta}$ for each $\epsilon$, and tends to $b_0$ pointwise with these bounds. $e_\epsilon$ is bounded
in $C^{(M)}_\nu\tilde S^{\mathsf s}$, lies in $C^{(M)}_\nu\tilde S^{\mathsf s-\kappa}$ for each $\epsilon$, and is
supported in a closed set $K_E\subset K_1$ with $K_E\cap{}^{e3b}S^*\tilde M\subset\mathrm{Ell}(E)$. $z_\epsilon$ is
bounded in $C^{(M)}_\nu\tilde S^{-\frac12(m-1)}$, and $\check a_\epsilon = z_\epsilon b_\epsilon$.

(iii) For every $w\in H^{K'}_{e3b}$ carried by $\chi$, where $K'\ge\sup|\mathsf s|+m+2$ is a fixed integer, with
$B_\epsilon := \mathrm{Op}(b_\epsilon)$, $E_\epsilon := \mathrm{Op}(e_\epsilon)$, $\check A_\epsilon :=
\mathrm{Op}(\check a_\epsilon)$ and a $G'$ carried by $\chi$ with $\mathrm{WF}'(G')\subset\mathrm{Ell}(G)$,
$$\varsigma\langle C_{\check a_\epsilon}w,w\rangle\le-\|B_\epsilon w\|^2+\|E_\epsilon w\|^2+C_0\big(\|G'w\|^2_{\mathsf
s-\frac12+\delta_0}+\|\chi w\|^2_{-N}\big),\tag{4.2}$$
with $C_0$ independent of $\epsilon$.

Then for every $u$ with $\chi u\in H^{-N}$, $Gu\in H^{\mathsf s-\kappa}$, $GLu\in H^{\mathsf s-m+1}$ and $Eu\in
H^{\mathsf s}$, we have $B_0u\in L^2$ and
$$\|B_0u\|^2\le C\big(\|GLu\|^2_{\mathsf s-m+1}+\|Eu\|^2_{\mathsf s}+
\|Gu\|^2_{\mathsf s-\frac12+\delta_0}+\|\chi u\|^2_{-N}
\big).\tag{4.3}$$

*Proof.* Norms are of $L^2$ and of $H^{\mathsf t}_{e3b}$; $C$ changes from line to line and does not depend on
$\epsilon$ or $t$.

*Step 0: microlocalisation.* Choose $\Phi = \mathrm{Op}(\phi)$, carried by $\chi$, with $\phi = 1$ near $K_1\cup K_E$ and
$\mathrm{supp}\,\phi$ in a closed set whose intersection with fibre infinity lies in $\mathrm{Ell}(G)$. Put $v := \Phi
u$. By II.A Lemma 8.4 (c), $\|v\|_{\mathsf t}\le C(\|Gu\|_{\mathsf t}+\|\chi u\|_{-N})$ for $\mathsf t\le\mathsf
s-\kappa$, and $\|\Phi Lu\|_{\mathsf s-m+1}\le C(\|GLu\|_{\mathsf s-m+1}+\|\chi u\|_{-N})$ (with II.A Lemma 8.6 (a) for
the error term). Now $Lv = \Phi Lu+[L,\Phi]u$, and $\check A_\epsilon[L,\Phi] = \check A_\epsilon(I-\Phi)L-\check
A_\epsilon L(I-\Phi)$. Both terms have every order, uniformly in $\epsilon$, by Proposition 2.4 (e) with $L =
\mathrm{Op}(\ell_f)+$ residual and $I-\Phi = \mathrm{Op}(1-\phi)$ (section 1.1), since $\check a_\epsilon$ and $1-\phi$
have disjoint supports. Hence, as $\check A_\epsilon$ is bounded of order $\mathsf k$ (Proposition 2.4 (a)),
$$\|\check A_\epsilon Lv\|_{\frac12(1-m)}\le C\big(\|GLu\|_{\mathsf s-m+1}+\|\chi u\|_{-N}\big).\tag{4.4}$$

*Step 1: the pairing at $v$.* Let $w_t := T_tv$, with $T_t$ from Lemma 2.3 (b) and $K\ge K'+\sup|\mathsf s|+1$, so that
$w_t\in H^{\mathsf s-\kappa+K}\subset H^{K'}$ for $t>0$ (carried by $\chi$ by the support convention, the kernels of
$T_t$ being supported near the diagonal). We show $\langle\check A_\epsilon Lw_t,\check A_\epsilon
w_t\rangle\to\langle\check A_\epsilon Lv,\check A_\epsilon v\rangle$ as $t\to0$, for fixed $\epsilon>0$. Symbols of
$C^{(M)}_\nu\tilde S^{\mathsf k}$ act with exact orders (Proposition 2.4 (a)), and only remainders lose $\delta$. So
$\check A_\epsilon$ has order $\mathsf k-\kappa$ for this $\epsilon$, and as $v\in H^{\mathsf s-\kappa}$, $\check
A_\epsilon w_t\to\check A_\epsilon v$ strongly in $H^{\frac12(m-1)}$. Next, $\check A_\epsilon Lw_t = \check A_\epsilon
T_tLv+\check A_\epsilon [L,T_t]v$. The first term tends to $\check A_\epsilon Lv$ in $H^{\frac12(1-m)}$: $T_t\to I$
strongly on $H^{\mathsf s-m+1}$, applied to $\Phi Lu$; the part with $[L,\Phi]u$ is handled as in Step 0, uniformly in
$t$. For the second, $L$ and $T_t$ have constant orders $m$ and 0. So Proposition 2.4 (d), with $a_1 = \ell_f$ and $a_2 =
\tau_t$ bounded in $\tilde S^0$, shows that $[L,T_t]$ is bounded of order $m-1$, uniformly in $t$; and it tends to 0 as
an operator of order $m-1+\delta$, since $\tau_t\to1$ in $\tilde S^\delta$. Hence $\check A_\epsilon[L,T_t]v$ is bounded
in $H^{\frac12(1-m)}$ uniformly in $t$ and tends to 0 in $\mathcal D'$, so weakly in $H^{\frac12(1-m)}$. A weakly null
sequence paired with a strongly convergent one tends to 0.

*Step 2: the inequality at $v$.* Apply (4.2) at $w = w_t$ and let $t\to0$. The pairing converges by Step 1. The other
terms converge: $E_\epsilon$ and $G'$ have orders at most $\mathsf s-\kappa$ and $\mathsf s-\frac12+\delta_0\le\mathsf
s-\kappa$, and $T_t\to I$ strongly. $B_\epsilon w_t\to B_\epsilon v$ in $H^{-\delta}$, $B_\epsilon$ having order
$\mathsf s-\kappa+\delta$ for this $\epsilon$. Since $\|B_\epsilon w_t\|^2$ is bounded by the convergent right side,
$B_\epsilon v\in L^2$, and by weak lower semicontinuity
$$\|B_\epsilon v\|^2\le-2\varsigma\,\mathrm{Im}\langle\check A_\epsilon Lv,\check A_\epsilon v\rangle+\|E_\epsilon v\|^2+
C_0\big(\|G'v\|^2_{\mathsf s-\frac12+\delta_0}+\|\chi v\|^2_{-N}\big).$$
(a) By Proposition 2.4 (b), $\check A_\epsilon = \mathrm{Op}(z_\epsilon)B_\epsilon+D_\epsilon$ with $D_\epsilon$ bounded
of order $\mathsf k-1+2\delta$. As $\mathrm{Op}(z_\epsilon)$ is bounded of order $-\frac12(m-1)$ without loss
(Proposition 2.4 (a)), $\|\check A_\epsilon v\|_{\frac12(m-1)}\le C\|B_\epsilon v\|+C\|v\|_{\mathsf s-1+2\delta}$. With
(4.4),
$$2|\langle\check A_\epsilon Lv,\check A_\epsilon v\rangle|\le\tfrac12\|B_\epsilon v\|^2+C\big(\|GLu\|^2_{\mathsf s-m+1}+
\|v\|^2_{\mathsf s-\frac12}+\|\chi u\|^2_{-N}\big).$$
(b) $E_\epsilon v = E_\epsilon u-E_\epsilon(I-\Phi)u$. The second term has every order, uniformly (Proposition 2.4 (e)).
For the first, $E$ is elliptic on $K_E\cap{}^{e3b}S^*\tilde M$, and $E_\epsilon$ is bounded of order $\mathsf s$ and
microsupported in $K_E$. So the iteration of the proof of Theorem 3.1, with $E$ in place of $L$ ($E$ smooth, of order
0), gives $\|E_\epsilon u\|\le C(\|Eu\|_{\mathsf s}+\|\chi u\|_{-N})$. (c) $\|G'v\|_{\mathsf s-\frac12+\delta_0}+\|\chi
v\|_{-N} \le C(\|Gu\|_{\mathsf s-\frac12+\delta_0}+\|\chi u\|_{-N})$. Absorbing $\frac12\|B_\epsilon v\|^2$, which is
finite,
$$\|B_\epsilon v\|^2\le C\big(\|GLu\|^2_{\mathsf s-m+1}+\|Eu\|^2_{\mathsf s}+\|Gu\|^2_{\mathsf s-\frac12+\delta_0}+\|\chi
u\|^2_{-N}\big)\quad\text{for all }\epsilon\in(0,1].$$

*Step 3: the limit.* $B_\epsilon v\to B_0v$ in $\mathcal D'$ (Proposition 2.4 (a) and the proof of its finite regularity
part, as $b_\epsilon\to b_0$ pointwise with uniform bounds in the class of order $\mathsf s+\delta$). $B_\epsilon v$ is
bounded in $L^2$, so $B_0v\in L^2$ with the same bound. Finally $B_0u = B_0v+B_0(I-\Phi)u$, and $B_0(I-\Phi)$ has every
order (Proposition 2.4 (e)). $\square$

The a priori hypothesis $Gu\in H^{\mathsf s-\kappa}$ is used only for the limits $t\to0$; the bound uses
$\|Gu\|_{\mathsf s-\frac12+\delta_0}$.

**Lemma 4.2 (iteration).** Let $\Gamma\subset{}^{e3b}S^*\tilde M$ be compact and $U_0$ an open neighbourhood. Suppose
that for every $\kappa\in(0,\frac14]$, every order $\mathsf s' = \mathsf s-\tau'$ with $0\le\tau'\le\tau$ ($\tau>0$ a
constant), and every open $U$ with $\Gamma\subset U\subset U_0$, the hypotheses of Lemma 4.1 hold for $(\mathsf
s',\kappa)$ with $K_1$ inside $U$ (near fibre infinity), with $E$-symbols supported in a closed set $K_E(U)$ whose
intersection with fibre infinity lies in $U\setminus\Gamma$, and with $b_0$ elliptic of order $\mathsf s'$ on an open
neighbourhood $U'$ of $\Gamma$: $b_0^{-1}\in C^{(M)}_\nu\tilde S^{-\mathsf s'}$ on $U'$ near fibre infinity. Let $G$ be
elliptic on $\bar U_0$. Then there are a neighbourhood $U_*$ of $\Gamma$ and a closed set $K_E^*$ missing $\Gamma$ such
that, for $E$ elliptic on $K_E^*$ and $B\in C^\infty_b\Psi^0_{e3b}$ carried by $\chi$ and microsupported in $U_*$, in the
strong sense,
$$\|Bu\|_{\mathsf s}\le C\big(\|GLu\|_{\mathsf s-m+1}+\|Eu\|_{\mathsf s}+\|Gu\|_{\mathsf s-\tau}+\|\chi u\|_{-N}\big).
\tag{4.5}$$

*Proof.* As I.A Lemma 3.2. Take an integer $J>4\tau$, $\kappa := \tau/J<\frac14$, and $\mathsf s_j := \mathsf
s-\tau+j\kappa$. Construct open sets $U_0\supset U_1\supset\dots\supset U_J\supset\Gamma$ with $\bar U_j\subset U'_j\cap
U_{j-1}$, where $U'_j$ is the $U'$ for $(\mathsf s_j,\kappa,U_{j-1})$, and let $K_E^* := \bigcup_jK_E(U_{j-1})$. Let $G_0
:= G$ and $G_j := \mathrm{Op}(g_j)$, carried by $\chi$, with $g_j$ smooth on the compactified bundle, equal to 1 near
$\bar U_j$ and supported in $U'_j\cap U_{j-1}$, where $b_0^{(j)}$ is elliptic and $G_{j-1}$ is elliptic (the eightieth
verifier: so $\mathrm{WF}'(G_j)\subset U_0\subset\mathrm{Ell}(G)$, which the step from $\|G_{j-1}Lu\|$ to $\|GLu\|$ and
the next step need). Then $\|G_ju\|_{\mathsf s_j}\le C(\|B_0^{(j)}u\|+\|\chi u\|_{-N})$. This is the parametrix argument
of Theorem 3.1 with $B_0^{(j)}$, of order $\mathsf s_j+\delta$, in place of $L$, and $\tilde\chi a(b_0^{(j)})^{-1}$ in
place of $\tilde\chi a\ell^{-1}$. $\mathrm{Op}(\tilde\chi a(b_0^{(j)})^{-1})$ has order $\mathsf r-\mathsf s_j$ without
loss (Proposition 2.4 (a)), and the remainders have order $\mathsf r-1+2\delta$, so with $\delta = \frac14$ the iteration
closes as there; $B_0^{(j)}u\in L^2$ enters without localization. (With an operator of order $-\mathsf s_j+\delta$ in
place of the parametrix, the conclusion would be $H^{\mathsf s_j-\delta}$ only; the seventy-ninth verifier, D195.) Lemma
4.1 at step $j$ needs $G_{j-1}u\in H^{\mathsf s_{j-1}}$, the conclusion of step $j-1$, and gives
$$\|B_0^{(j)}u\|\le C\big(\|G_{j-1}Lu\|_{\mathsf s_j-m+1}+\|Eu\|_{\mathsf s_j}+
\|G_{j-1}u\|_{\mathsf s_j-\frac12+\delta_0}+
\|\chi u\|_{-N}\big).$$
Take $\delta_0\le\frac14-\kappa$, which is positive as $J>4\tau$, so that $\mathsf s_j-\frac12+\delta_0\le\mathsf
s_{j-1}$. Lemma 4.1 at step $j$ applies with $G_{j-1}$ in the role of $G$, which is elliptic on $\bar U_{j-1}\supset
K_1\cup K_E$ near fibre infinity. Inducting on $j$ bounds $\|G_Ju\|_{\mathsf s}$, and (4.5) follows for $B$
microsupported in $U_* := U_J$ by II.A Lemma 8.4 (c). $\square$

## 5. Real principal type propagation

### 5.1 The operator and its Hamilton field

Let $L = L_0+L_1+L_2$ on $\mathbb C^{N'}$ as in II.A (L4). Here $L_0\in\mathrm{Diff}^m_{e3b}\otimes\mathrm{Id}$, and
$L_1 = \sum_qa_qP_q\otimes\mathrm{Id}$ with $a_q\in C^{d_0,(2\delta_w,\delta_w,\delta_w)}_{e3b}$, $\delta_w>0$, and
$P_q\in \mathcal P_m$ with classical principal symbols. $L_2\in C^{d_0}_{e3b}\mathcal
P_{m-1}\otimes\mathrm{End}\,\mathbb C^{N'}$. The scalar principal symbol $\ell = \ell_0+\ell_1$ is real, with $\ell_0 :=
\sigma(L_0)$ and $\ell_1 := \sum_qa_q\sigma(P_q)$ homogeneous of degree $m$. Put $\mathsf H := \rho_\infty^{m-1}H_\ell$,
homogeneous of degree 0, and $\mu := \rho_\infty^{-(m-1)}$, so that $H_\ell = \mu\mathsf H$ on functions homogeneous of
degree 0.

**Lemma 5.1.** (a) $\mathsf H$ induces a vector field on ${}^{e3b}S^*\tilde M$, tangent to its boundary faces, that is
continuous over $\tilde M\setminus(I^0\cup K^-)$. Over $\mathscr I^+\cup\iota^+\cup K^+$ it equals
$\rho_\infty^{m-1}H_{\ell_0}$. (b) In the charts of $\rho\mathcal B$, with coordinates $(x,\omega)$ on the cosphere
bundle, its coefficients have derivatives up to order $d_0-1$ bounded uniformly. (c) Over the interior its integral
curves are unique and exist for all times. Over $\tilde M\setminus(I^0\cup K^-)$ its integral curves are unique and
preserve the boundary faces, and its flow is continuous and depends continuously on the field: if such fields $\mathsf
H_n$ converge to $\mathsf H$ uniformly on compact sets there, their integral curves from points converging to $\beta$
converge to that of $\mathsf H$ from $\beta$, uniformly on compact time intervals on which it stays there. For $|t|\le
T_0$, the flow maps have derivatives up to order $d_0-1$ bounded in these charts, uniformly.

*Proof.* (a), (b). $\rho_\infty^{m-1}H_{\ell_0}$ is smooth on ${}^{e3b}S^*\tilde M$ and tangent to its faces: $\ell_0$ is
classical, and Hamilton fields of e3b-symbols are b-vector fields on the compactified bundle ([Hin26c] p. 71 and (2.39);
II.A section 2.5). Write $\ell_1 = w\tilde\ell_1$ with $w := x_I^{2\delta_w}\rho_+^{\delta_w}\rho_K^{\delta_w}$ and
$\tilde\ell_1 := \sum_q\tilde a_q\sigma(P_q)$, $\tilde a_q := w^{-1}a_q\in C^{d_0}_{e3b}$. Then $H_{\ell_1} =
wH_{\tilde\ell_1}+ \tilde\ell_1H_w$. Here $H_w$ is $w$ times a fibre vector field whose coefficients are e3b-derivatives
of $\log w$, which are smooth on $\tilde M$. In the charts of $\rho\mathcal B$ the coordinate fields are, uniformly,
bounded combinations of b-vector fields of the compact manifold. They are lifts of e3b-fields and fibre fields, magnified
at the boundary as in Lemma 1.2. So $\rho_\infty^{m-1}H_{\ell_1}$ is $w$ times a combination of b-vector fields of
${}^{e3b}S^*\tilde M$ with coefficients that are bounded with $d_0-1$ derivatives in those charts. As $w\to0$ at
$\mathscr I^+$, $\iota^+$ and $K^+$, this part tends to 0 there, and b-vector fields are tangent to the faces. At $I^0$
and $K^-$ the weight need not vanish, and $\mathsf H$ need not be continuous there. (c) In the charts of $\rho\mathcal B$
the field is uniformly $C^{d_0-1}$, hence uniformly Lipschitz, so its integral curves over the interior are unique. They
exist for all times, since in logarithmic coordinates the faces lie at infinity and the field is bounded there. On the
faces $\mathscr I^+$, $\iota^+$, $K^+$ the field is the smooth tangent field above. A curve $\gamma$ through a point of
such a face $F$ stays in $F$. For a defining function $\rho_F$, $\mathsf H\rho_F = \beta\rho_F$ with $\beta$ bounded near
$F$, both parts of $\mathsf H$ being combinations of b-vector fields with bounded coefficients. So $f :=
\rho_F\circ\gamma$ satisfies $|f'|\le C|f|$ and $f(0) = 0$, whence $f\equiv0$ by Gronwall's inequality. Within $F$, and
within each corner, the field is smooth, so curves through boundary points are unique too. The fields are bounded and
continuous over $\tilde M\setminus(I^0\cup K^-)$. By Arzelà and Ascoli, integral curves of fields $\mathsf H_n$ as in
(c), from points $\beta_n\to\beta$, have subsequences converging uniformly on compact time intervals, and the limits are
integral curves of $\mathsf H$ from $\beta$. They equal the unique one, so the whole sequence converges. The bounds on
derivatives of the flow maps follow from Gronwall's inequality applied to the variational equations, uniformly in the
charts. $\square$

**Lemma 5.2 (flow box).** Let $\gamma:[a,b]\to{}^{e3b}S^*\tilde M$ be an injective integral curve of $\mathsf H$ with
$\mathsf H\ne0$ on it. There are a neighbourhood $O$ of $\gamma([a,b])$ and functions $z,y_1,\dots,y_8$ on $O$ with
these properties. $(z,y)$ maps $O$ homeomorphically onto $(a-3\delta',b+3\delta')\times B$, where $B$ is a neighbourhood
of 0 in $\mathbb R^8$, intersected with a closed quadrant when $\gamma$ lies in boundary faces. Also $\mathsf Hz = 1$,
$\mathsf Hy_i = 0$ and $\gamma(t) = (t,0)$. On $O\cap{}^{e3b}S^*\tilde M^\circ$, $z$ and $y$ have derivatives up to
order $d_0-1$ bounded in the charts of $\rho\mathcal B$, uniformly. (${}^{e3b}S^*\tilde M$ has dimension $2\cdot5-1 =
9$.)

*Proof.* $\gamma$ extends to an integral curve on $[a-4\delta',b+4\delta']$. Choose a smooth function $\sigma$ near $p_0
:= \gamma(a-2\delta')$ with $\sigma(p_0) = 0$ and $\mathsf H\sigma(p_0)\ne0$, and smooth $\tilde y_1,\dots,\tilde y_8$
such that $(\sigma,\tilde y)$ is a chart of the compact manifold with corners at $p_0$, adapted to its faces. For $p$
near $\gamma$, let $z(p)$ be the time $t$ near the expected value with $\sigma(\exp(-(t-a+2\delta')\mathsf H)p) = 0$,
and $y(p) := \tilde y(\exp(-(z(p)-a+2\delta')\mathsf H)p)$. By continuity $\mathsf H\sigma\ge c>0$ near $p_0$. The
implicit function theorem then gives $z$ locally. The derivative of $z$ is $(d\sigma\cdot
D\exp\cdot\partial)/(d\sigma\cdot \mathsf H)$, and similarly for $y$. In the charts of $\rho\mathcal B$, $d\sigma$ and
$d\tilde y$ are bounded with all derivatives (smooth functions on the compact manifold, as in Lemma 1.1), and $D\exp$ is
bounded with $d_0-2$ further derivatives (Lemma 5.1 (c)). So $z$ and $y$ have $d_0-1$ bounded derivatives. Faces are
invariant, so $y$ maps them to coordinate faces. Injectivity of $(z,y)$ on a neighbourhood follows from the injectivity
of $\gamma$ and of $\tilde y$ on the slice $\{\sigma = 0\}$, by the usual compactness argument for a curve that meets
the slice once. $\mathsf Hz = 1$ and $\mathsf Hy = 0$ hold by construction. $\square$

### 5.2 Propagation along one curve

**Proposition 5.3.** Let $\varsigma\in\{1,-1\}$ and $\mathsf H_f := \varsigma\mathsf H$ (the forward field). Let
$\gamma:[0,T]\to{}^{e3b}S^*\tilde M$ be an injective integral curve of $\mathsf H_f$ with $\mathsf H_f\ne0$ on it (it
need not lie in $\mathrm{Char}(L)$; the proof does not use it). Let $\mathsf s$ be a variable order with $\mathsf
H_f\mathsf s\le0$ on a neighbourhood of $\gamma([0,T])$ in ${}^{e3b}S^* \tilde M$, and let $E$ be elliptic at
$\gamma(0)$. Then there are $B\in C^\infty_b\Psi^0_{e3b}$, elliptic on $\gamma([0,T])$, and $G$, both microsupported in
any given neighbourhood of $\gamma([0,T])$ (near fibre infinity, and carried by $\chi$), such that in the strong sense
$$\|Bu\|_{\mathsf s}\le C\big(\|GLu\|_{\mathsf s-m+1}+\|Eu\|_{\mathsf s}+\|\chi u\|_{-N}\big).\tag{5.1}$$
$C$ depends on $L$ only through finitely many norms of its coefficients and the geometry of the flow near $\gamma$. It
is uniform for perturbations of $L$ small in those norms, for which the hypotheses hold with the same
$\gamma$-neighbourhood.

*Proof.* Apply Lemma 5.2 to the curve $t\mapsto\gamma(\varsigma t)$ of $\mathsf H$, or equivalently use coordinates with
$\mathsf H_f = \partial_z$, $\gamma(t) = (t,0)$, on a neighbourhood $O$ of $\gamma([-4\delta',T+4\delta'])$. Extend $z,y$
to a conic neighbourhood in ${}^{e3b}T^*\tilde M$, homogeneously of degree 0. With the cut-off $\psi$ of I.A section 3
($\psi$ even, supported in $(-1,1)$, equal to 1 on $[-\frac12,\frac12]$, nonincreasing on $[0,\infty)$, with $-\psi\psi'$
the square of a smooth function on $[0,\infty)$), put $\chi_s(z) := \psi(-z/\delta)$ for $z\le0$ and $\chi_s(z) := 1$ for
$z\ge0$, and $\chi_e(z) := \psi((z-T)/\delta)$ for $z\ge T$ and $\chi_e(z) := 1$ for $z\le T$. These are smooth, as $\psi
= 1$ near 0, and $\chi_s = \chi_e = 1$ on $[0,T]$. So $\partial_z(\chi_s^2) = \frac2\delta(-\psi\psi')(-z/\delta)\ge0$ is
supported in $[-\delta,-\frac\delta2]$, and $-\partial_z(\chi_e^2)\ge0$ in $[T+\frac\delta2,T+\delta]$; both are squares
of smooth functions of $z$. (With $\psi$ even, $\psi(-z/\delta)$ alone vanishes for $z\ge\delta$, and neither statement
would hold; the seventy-ninth verifier, D195.) Put $\psi_y := \psi(|y|^2/\delta_1^2)$. Choose $\delta\le\delta'/2$ and
$\delta_1$ so small that $\{z\in[-2\delta,T+2\delta],|y|\le2\delta_1\}$ lies in the given neighbourhood, in $O$ and in
the set where $\mathsf H_f\mathsf s\le0$, and that $\{z\in[-2\delta,0],|y|\le2\delta_1\}\subset\mathrm{Ell}(E)$ (the
margin serves the uniformity below). Let $\chi_\infty$ be a function of $\rho_\infty$ equal to 1 near fibre infinity and
supported where $(z,y)$ are defined and in $\{\rho_\infty<1\}$, so that $\log\rho_\infty<0$ on its support. Its
derivatives are supported in a set compact in the fibres, where every symbol has order $-\infty$.

*Commutant.* With $\mathsf k := \mathsf s-\frac12(m-1)$ (the restriction to fibre infinity), the regulariser
$\varphi_\epsilon$ of section 2.3 with exponent $\kappa$, and a large constant $M$,
$$\check a_\epsilon := \chi_\infty\rho_\infty^{-\mathsf k}\varphi_\epsilon e^{-Mz}\chi_s(z)\chi_e(z)\psi_y.$$
Its factors other than $\rho_\infty^{-\mathsf k}\varphi_\epsilon$ have $d_0-1$ bounded derivatives (Lemma 5.2), so
$\check a_\epsilon$ is bounded in $C^{(d_0-1)}\tilde S^{\mathsf k}$ (index 0), and lies in $C^{(d_0-1)}\tilde S^{\mathsf
k-\kappa}$ for each $\epsilon$. Since $\mathsf H_fz = 1$ and $\mathsf H_f\psi_y = 0$, (2.1) gives, where $\chi_\infty =
1$,
$$\mathsf H_f(\check a_\epsilon^2) = \rho_\infty^{-2\mathsf k}\varphi_\epsilon^2\psi_y^2e^{-2Mz}
\Big[-\chi_s^2\chi_e^2Q_\epsilon+
\chi_e^2\partial_z(\chi_s^2)+\chi_s^2\partial_z(\chi_e^2)\Big],$$
$$Q_\epsilon := 2M+2\mathsf k_\epsilon\rho_\infty^{-1}\mathsf H_f\rho_\infty+
2(\mathsf H_f\mathsf k)\log\rho_\infty,\qquad
\mathsf k_\epsilon := \mathsf k-\kappa\theta_\epsilon.$$
On the support, $\mathsf H_f\mathsf k = \mathsf H_f\mathsf s\le0$ and $\log\rho_\infty<0$, so the last term of
$Q_\epsilon$ is nonnegative. Choose $M\ge1+\sup|2\mathsf k_\epsilon\rho_\infty^{-1}\mathsf H_f\rho_\infty|$, uniformly in
$\epsilon$ as $\mathsf k_\epsilon\in(\mathsf k-\kappa,\mathsf k]$. Then $Q_\epsilon\ge M$; $M$ will be enlarged once more
below. Write $Q_\epsilon = Q_{0,\epsilon}+\lambda$ with $Q_{0,\epsilon} := 2M+2\mathsf k_\epsilon\rho_\infty^{-1}\mathsf
H_f\rho_\infty\ge M$ and $\lambda := 2(\mathsf H_f\mathsf k)\log\rho_\infty\ge0$. $Q_{0,\epsilon}$ has $d_0-2$ bounded
derivatives, and $\lambda$ has $d_0-2$ derivatives bounded by $C\langle\log\rho_\infty\rangle$, uniformly in $\epsilon$
(Lemma 5.1 (b) and Definition 1.3). By Lemma 2.5 (ii) with $\nu = 0$, $Q_\epsilon^{-1/2}$ is bounded in
$C^{(d_0-2)}_1\tilde S^0$ and $Q_\epsilon^{1/2}$ in $C^{(d_0-2)}_1\tilde S^\delta$ for every $\delta>0$. Put
$$b_\epsilon := \mu^{\frac12}\rho_\infty^{-\mathsf k}\varphi_\epsilon\psi_ye^{-Mz}\chi_s\chi_e
Q_\epsilon^{1/2}\chi_\infty,
\qquad b_{e,\epsilon} := \mu^{\frac12}\rho_\infty^{-\mathsf k}\varphi_\epsilon\psi_ye^{-Mz}
\chi_s\big(-\partial_z(\chi_e^2)
\big)^{1/2}\chi_\infty,$$
$$e_\epsilon := \mu^{\frac12}\rho_\infty^{-\mathsf k}\varphi_\epsilon\psi_ye^{-Mz}\chi_e
\big(\partial_z(\chi_s^2)\big)^{1/2}
\chi_\infty,\qquad z_\epsilon := \mu^{-\frac12}Q_\epsilon^{-1/2}.$$
Then $\varsigma H_\ell(\check a_\epsilon^2) = \mu\mathsf H_f(\check a_\epsilon^2) =
-b_\epsilon^2-b_{e,\epsilon}^2+e_\epsilon^2$ modulo symbols of order $-\infty$ (from $\chi_\infty$), and $\check
a_\epsilon = z_\epsilon b_\epsilon$. $\mu\rho_\infty^ {-2\mathsf k}$ has order $2\mathsf s$. So, all with index 1 and
$d_0-2$ derivatives, $b_\epsilon$ is bounded in the class of order $\mathsf s+\delta$ for every $\delta>0$ (the factor
$Q_\epsilon^{1/2}$), $e_\epsilon$ and $b_{e,\epsilon}$ in that of order $\mathsf s$, and $z_\epsilon$ in that of order
$-\frac12(m-1)$, on which it acts without loss (Proposition 2.4 (a)). $e_\epsilon$ is supported in
$\{z\in[-\delta,-\frac\delta2]\}$, inside $\mathrm{Ell}(E)$ and away from $\gamma([0,T])$. $b_0$ is elliptic on
$\gamma([0,T])$, where $\chi_s = \chi_e = \psi_y = 1$ and $Q_0\ge M$: on the open set $U' :=
\{z\in(-\frac\delta2,T+\frac\delta2),|y|^2<\frac12\delta_1^2\}$, near fibre infinity, $b_0^{-1} = \rho_\infty^{\mathsf
s}e^{Mz}Q_0^{-1/2}$ lies in $C^{(d_0-2)}_1\tilde S^{-\mathsf s}$.

*The commutator.* Write $L = \mathrm{Op}(\ell_f)+R_L$ by (1.2), with $R_L$ of every order. Let $\ell_R := \frac12(\ell_f+
\ell_f^*)$ and $\ell_I := \frac1{2i}(\ell_f-\ell_f^*)$. Since $\ell$ is real and scalar, $\ell_R-\ell\,\mathrm{Id}$ and
$\ell_I$ have order $m-1$. Then $L_R = \mathrm{Op}(\ell_R)+D_R$ and $L_I = \mathrm{Op}(\ell_I)+D_I$, where $D_R$ and
$D_I$ are $\pm\frac12$, resp. $\pm\frac1{2i}$, times $D_{\ell_f}$ of Proposition 2.4 (f), plus the parts of $R_L$. So
$L_I$ has exact order $m-1$, and $[D_R,\check A]$, $[D_I,\check A]$ have order $m+\mathsf k-2+\delta$, with $\check A :=
\check A_\epsilon := \mathrm{Op}(\check a_\epsilon)$, uniformly in $\epsilon$. Now $i[L_R,\check A^2] = i[L_R,\check
A]\check A+\check A\,i[L_R,\check A]$, and by Proposition 2.4 (d) and the above, $i[L_R,\check A] =
\mathrm{Op}(H_{\ell_R}\check a)$ plus order $m+\mathsf k-2+\delta$. Next, $H_{\ell_R}\check a = H_\ell\check
a\,\mathrm{Id}+H_{\ell_R-\ell}\check a$, where the second term has order $m+\mathsf k-2$. With Proposition 2.4 (b),
$i[L_R,\check A^2]$ is $\mathrm{Op}(H_\ell(\check a^2))$ plus order $2\mathsf s-1+\delta$. Further, $\check A^*\check A =
\check A^2+D_{\check a}\check A$ with $D_{\check a} := \check A^*-\check A$ of order $\mathsf k-1+\delta$ (Proposition
2.4 (c), $\check a$ real), and $i[L_R,D_{\check a}\check A]$ has order $2\mathsf s-1+\delta$ by Proposition 2.4 (f). So
$$i[L_R,\check A^*\check A] = \mathrm{Op}(H_\ell(\check a^2))+R_1,\qquad R_1\text{ of order }2\mathsf s-1+\delta.$$
For $L_I$, formally self-adjoint: $\langle(L_I\check A^*\check A+\check A^*\check AL_I)w,w\rangle =
2\,\mathrm{Re}\langle\check AL_Iw,\check Aw\rangle = 2\,\mathrm{Re}\langle L_I\check Aw,\check
Aw\rangle+2\,\mathrm{Re}\langle\check A^*[\check A,L_I]w,w\rangle$, and $\check A^*[\check A,L_I]$ has order $2\mathsf
s-1+\delta$, by Proposition 2.4 (d) for $\mathrm{Op}(\ell_I)$ and (f) for $D_I$. Collecting, by (4.1), for $w\in H^{K'}$,
$$\varsigma\langle C_{\check a}w,w\rangle =
\mathrm{Re}\langle\mathrm{Op}(\varsigma H_\ell(\check a^2))w,w\rangle+2\varsigma\,
\mathrm{Re}\langle L_I\check Aw,\check Aw\rangle+\mathrm{Re}\langle R_2w,w\rangle,$$
where $|\langle R_2w,w\rangle|\le C\|G'w\|^2_{\mathsf s-\frac12+\delta}+C\|\chi w\|^2_{-N}$. Here $G'$ is microlocally
the identity on the support of $\check a$ and $\mathrm{WF}'(G')\subset\mathrm{Ell}(G)$. The microlocalisation of the
remainders is by Proposition 2.4 (e), all of them having a factor supported in the support of $\check a$.

*Positivity.* By Proposition 2.4 (b), (c), $\mathrm{Op}(b_\epsilon^2) = B_\epsilon^*B_\epsilon+$ order $2\mathsf s-1+
2\delta$, with $B_\epsilon := \mathrm{Op}(b_\epsilon)$; likewise for $b_{e,\epsilon}$ and $e_\epsilon$. So
$\mathrm{Re}\langle\mathrm{Op}(\varsigma H_\ell(\check a^2))w,w\rangle\le-\|B_\epsilon w\|^2+\|E_\epsilon
w\|^2+C(\|G'w\|^2 _{\mathsf s-\frac12+\delta}+\|\chi w\|^2_{-N})$, dropping $-\|B_{e,\epsilon}w\|^2\le0$. For the $L_I$
term, fix elliptic operators $\Lambda_{\pm}$ of orders $\pm\frac12(m-1)$ defining the norms of $H^{\pm\frac12(m-1)}$, and
let $C_I$ be the norm of $L_I$ between these spaces. It depends on finitely many norms of the coefficients and not on $M$
or $\epsilon$. Take $\Lambda_+ := \mathrm{Op}(\lambda_+)$ with $\lambda_+$ classical. Then $\Lambda_+\check A =
\mathrm{Op}(\lambda_+z_\epsilon)B_\epsilon+$ order $\mathsf s-1+2\delta$ (Proposition 2.4 (b)), where
$\lambda_+z_\epsilon\in C^{(d_0-2)}_1\tilde S^0$. Its supremum is at most $C_\Lambda M^{-1/2}$, with $C_\Lambda :=
\sup|\lambda_+\mu^{-1/2}|$, as $Q_\epsilon\ge M$. Lemma 2.6 with $\eta := M^{-1}$ and $\frac\delta2$ in place of
$\delta$, applied to $B_\epsilon w$, and $(a+b)^2\le2a^2+2b^2$ give $\|\check
Aw\|^2_{\frac12(m-1)}\le2(C_\Lambda^2+1)M^{-1}\|B_\epsilon w\|^2+C\|G'w\|^2_{\mathsf s-\frac12+\delta}+C\|\chi
w\|^2_{-N}$, where $\|B_\epsilon w\|_{-\frac12+\frac\delta2}$, with $b_\epsilon$ bounded in the class of order $\mathsf
s+\frac\delta2$, is bounded by the last two norms, $b_\epsilon$ being supported in the support of $\check a$ (Proposition
2.4 (e)). Enlarge $M$ so that $4C_I(C_\Lambda^2+1)M^{-1}\le\frac12$. Then
$$\varsigma\langle C_{\check a_\epsilon}w,w\rangle\le-\tfrac12\|B_\epsilon w\|^2+
\|E_\epsilon w\|^2+C\big(\|G'w\|^2_{\mathsf
s-\frac12+\delta}+\|\chi w\|^2_{-N}\big).$$
This is (4.2) for $2^{-1/2}b_\epsilon$, $e_\epsilon$ and $2^{\frac12}z_\epsilon$, with $\delta_0 := \delta$. The other
hypotheses of Lemma 4.1 hold by the construction, with $d_0$ large enough that the norms used are among those available:
$d_0-2\ge M_{2.4}+2$ for the $M_{2.4}$ of Proposition 2.4 at the orders involved and index 1.

*Conclusion.* The hypotheses of Lemma 4.2 hold with $\Gamma := \gamma([0,T])$. For each $U\supset\Gamma$ shrink $\delta$,
$\delta_1$ so that the support lies in $U$. The $E$-sets lie in $\{z\in[-\delta,-\frac\delta2],|y|\le\delta_1\}\subset
\mathrm{Ell}(E)$, which misses $\Gamma$. There is no threshold, so $\tau$ is arbitrary. Take $\tau\ge\sup\mathsf s+N$;
then $\|Gu\|_{\mathsf s-\tau}\le C\|\chi u\|_{-N}$, and (4.5) is (5.1), with any $B\in C^\infty_b\Psi^0_{e3b}$ carried by
$\chi$, microsupported in $U_*$ and elliptic on $\Gamma$. On $\mathbb C^{N'}$ the commutant is scalar and $L_I$ is
matrix-valued. Nothing above used a scalar $L_I$. The uniformity: all constants are bounded by finitely many norms of the
coefficients, by the bounds of Lemma 5.2, and by $M$, $\delta$, $\delta_1$. Let $L'$ be a perturbation small in
$C^{d_0}$, with field $\mathsf H'$, let $\gamma'$ be the integral curve of $\mathsf H'_f$ with $\gamma'(T) = \gamma(T)$,
and build the coordinates $(z',y')$ of Lemma 5.2 for $\mathsf H'$ with the same slice $\{\sigma = 0\}$ and the same
$\tilde y$, shifted so that $\gamma'(t) = (t,0)$. As $\mathsf H'\to\mathsf H$, the integral curves of $\mathsf H'$ from
points of the slice near $p_0$ converge to those of $\mathsf H$ uniformly on the compact time interval (Lemma 5.1 (c)).
So the compactness argument for the injectivity in Lemma 5.2 (a curve meets the slice once) holds uniformly: for $\mathsf
H'$ close to $\mathsf H$, $(z',y')$ is defined and injective on a fixed neighbourhood of
$\gamma([-3\delta',T+3\delta'])$, with the derivative bounds of Lemma 5.2 uniform, and $(z',y')\to(z,y)$ uniformly there.
The box $\{z'\in[-\delta,T+\delta],|y'|\le\delta_1\}$ then lies in the box of $\mathsf H$ with $2\delta$, $2\delta_1$,
which has the properties required above by the choice of the margin, given that $\mathsf H'_f\mathsf s\le0$ on the same
neighbourhood. With $M$ chosen with a margin too, as the bounds it must exceed depend continuously on the coefficients,
the same $\delta$, $\delta_1$, $M$ serve (the seventy-ninth verifier asked for the injectivity; D195). $\square$

### 5.3 The global estimate

**Theorem 5.4 ((L4), corrected; [Hin26c] Proposition 3.24 at $k = 0$).** Let $m\in\mathbb N_0$, $\mathsf s$ a variable
order and $N\in\mathbb R$. There is $d_0 = d_0(m,\mathsf s,N)$ with the following property. Let $L$ be as in section 5.1
with this $d_0$, for any $\delta_w>0$, any finite $\mathcal P_m$, $\mathcal P_{m-1}$ and any $N'$. Let $B,E,G\in
C^\infty_b\Psi^0_{e3b}$ be carried by $\chi$, with $\mathrm{supp}\,\chi$ disjoint from $I^0\cup K^-$ and
$\mathrm{WF}'(B)\subset\mathrm{Ell}(G)$. Suppose: (A) for every $\alpha\in\mathrm{WF}'(B)\cap\mathrm{Char}(L)$, the
backward integral curve of $\mathsf H$ from $\alpha$ reaches $\mathrm{Ell}(E)$ in a time at most $T_0$, remaining in
$\mathrm{Ell}(G)$; (B) $\mathsf H\mathsf s\le0$ on a neighbourhood in ${}^{e3b}S^*\tilde M$ of the union of these
backward segments. Then, in the strong sense,
$$\|Bu\|_{\mathsf s}\le C\big(\|GLu\|_{\mathsf s-m+1}+\|Eu\|_{\mathsf s}+\|\chi u\|_{-N}\big),$$
with $C$ locally uniform: uniform for perturbations of $L$ small in the norms of section 5.1, with real principal
symbols, for which (B) holds on the same neighbourhood.

*Proof.* Let $\alpha\in\mathrm{WF}'(B)\cap\mathrm{Char}(L)$ and $t_\alpha := \inf\{t\ge0:\exp(-t\mathsf H)\alpha\in
\mathrm{Ell}(E)\}\le T_0$. $\mathsf H\ne0$ along the backward curve, for a stationary point outside $\mathrm{Ell}(E)$
would never reach it. Take $t'_\alpha$ slightly larger than $t_\alpha$ with $\exp(-t'_\alpha\mathsf
H)\alpha\in\mathrm{Ell} (E)$. The curve $\gamma_\alpha(t) := \exp((t-t'_\alpha)\mathsf H)\alpha$, $t\in[0,t'_\alpha]$, is
injective, with $t'_\alpha$ taken below the infimum of periods if the orbit is periodic. Indeed, a self-intersection
would make the orbit periodic with period at most $t'_\alpha$, and then the backward curve would have entered
$\mathrm{Ell}(E)$ at an earlier time. It lies in $\mathrm{Char}(L)$, as $\ell$ is constant along the flow, and in
$\mathrm{Ell}(G)$. As the neighbourhood in (B) is open, $t'_\alpha$ can be chosen so that (B) holds on a neighbourhood of
$\gamma_\alpha([0,t'_\alpha])$. Proposition 5.3 with $\varsigma = 1$ gives $B_\alpha\in C^\infty_b\Psi^0_{e3b}$ elliptic
on $\gamma_\alpha([0,t'_\alpha])$, in particular near $\alpha$, and $G_\alpha$ microsupported in a neighbourhood inside
$\mathrm{Ell}(G)$. It also gives $\|B_\alpha u\|_{\mathsf s}\le C(\|G_\alpha Lu\|_{\mathsf s-m+1}+\|Eu\|_{\mathsf
s}+\|\chi u\|_{-N})$, and $\|G_\alpha Lu\|\le C(\|GLu\|+\|\chi u\|_{-N})$ by II.A Lemma 8.4 (c) and Lemma 8.6 (a). For
$\alpha\in\mathrm{WF}'(B)\setminus\mathrm{Char}(L)$, Theorem 3.1 gives any $B_\alpha\in C^\infty_b\Psi^0_{e3b}$ elliptic
near $\alpha$ and microsupported in $\mathrm{Ell}(G)\cap\mathrm{Ell}(L)$ with $\|B_\alpha u\|_{\mathsf s}\le
C(\|GLu\|_{\mathsf s-m}+\|\chi u\|_{-N})$. By compactness of $\mathrm{WF}'(B)$, finitely many $B_{\alpha_i}$ are jointly
elliptic on it: $\sum_iB_{\alpha_i}^*B_{\alpha_i}\in C^\infty_b\Psi^0_{e3b}$ is elliptic of order 0 there, the
$B_{\alpha_i}$ being smooth (the seventy-ninth verifier: II.A Lemma 8.4 (c) needs smooth operators). The elliptic
estimate (II.A Lemma 8.4 (c), or Theorem 3.1) bounds $\|Bu\|_{\mathsf s}$ by $C\sum_i\|B_{\alpha_i}u\|_{\mathsf
s}+C\|\chi u\|_{-N}$. The strong sense and the uniformity are those of Proposition 5.3 and Theorem 3.1. For a small
perturbation $L'$ the same $\alpha_i$ serve. If $\alpha_i\notin\mathrm{Char}(L)$, it lies in $\mathrm{Ell}(L')$ with a
comparable bound. If $\alpha_i\in\mathrm{Char}(L)$, Proposition 5.3, which does not ask its curve to be characteristic,
applies to the integral curve of $\mathsf H'$ ending at $\alpha_i$, with the same $\delta$, $\delta_1$, $M$ and the same
shrinkings in Lemma 4.2 (its proof, last paragraph). By Lemma 5.1 (c) that curve stays close to $\gamma_{\alpha_i}$, and
the sets on which its $b_0^{(j)}$ are elliptic contain fixed neighbourhoods of $\gamma_{\alpha_i}([0,t'_{\alpha_i}])$; a
$B_{\alpha_i}$ microsupported in these serves for $L'$ too. The resulting operators remain jointly elliptic on
$\mathrm{WF}'(B)$, once the $B_{\alpha_i}$ are chosen elliptic on open sets that still cover $\mathrm{WF}'(B)$ when
shrunk slightly. $\square$

## 6. What this part found

(G6) *The hypothesis on the order in [Hin26c] Proposition 3.24.* The source asks for $\mathsf H_\ell\mathsf s\le0$ only
"in a neighborhood of $\mathrm{WF}'_{e3b}(B)\cap\mathrm{Char}_{e3b}(L)$ within $\mathrm{Char}_{e3b}(L)$" (p. 70). This
does not suffice. A backward curve from $\mathrm{WF}'(B)$ may leave that neighbourhood and pass where $\mathsf s$
increases along it before reaching $\mathrm{Ell}(E)$. The estimate would then give $Bu\in H^{\mathsf s}$ at a point where
$\mathsf s$ exceeds its value at the curve's point in $\mathrm{Ell}(E)$. Propagation does not gain regularity, so this is
false in general: take $u$ with a conormal singularity along the curve of a fixed order between the two values. The
standard statement asks for monotonicity along the whole segments ([Vas18] Theorem 5.3; I.A Proposition 5.2 (d)). Theorem
5.4 asks for $\mathsf H\mathsf s\le0$ on a neighbourhood in phase space of the backward segments. The version within
$\mathrm{Char}(L)$ only would need $\mathsf s$ modified off $\mathrm{Char}(L)$, which is not done here. II.A (L4), and
Propositions 9.2 and 9.9 of II.A, which take their hypotheses from it, now carry the corrected hypothesis (D194). The
verifier of II.A found the same gap independently, with the example $L = D_t$ recorded in II.A section 10. Whether every
application of Proposition 3.24 in [Hin26c] meets the corrected hypothesis is checked where the applications are written
out (Parts II.B-II.F).

(G7) *Classical symbols in (L4), and where $\mathsf H$ is continuous.* The source's Hamilton field is taken on
${}^{e3b}S^*\tilde M$ ([Hin26c] pp. 55, 71). That presupposes principal symbols with a continuous extension there. (L4)
is therefore stated for $\mathcal P_m$ with classical principal symbols. (L3) needs no such restriction. The source also
takes $\mathsf H$ continuous on all of ${}^{e3b}S^*\tilde M$, because the coefficients of $L_1$ vanish at $\partial\tilde
M$ (p. 71). They vanish at the faces carrying the weight, $\mathscr I^+$, $\iota^+$ and $K^+$, and need not at $I^0$ and
$K^-$. (L4) is therefore stated for $\chi$ supported away from these, as near $\bar\Omega$ (II.A section 1). Lemma 5.1
(c) adds the uniqueness of integral curves at the faces, on which the continuity of the flow rests, since $\mathsf H$ is
only continuous there (D194).

*Changes of method, not of statement.* The finite-regularity calculus is proved from the smooth one by the closed graph
theorem and mollification (section 2), in classes that count the logarithmic factors each derivative may carry
(Definition 1.3). Square roots of the commutant's symbol cost one such factor per derivative (Lemma 2.5), and the classes
of [SBG] Definition 4.6 admit them without loss in the mapping order. The source cites the standard arguments and its
Lemma 3.5. The positive commutator uses the exact Hamilton field of the operator with finite regularity, through flow-box
coordinates of that regularity, so every positivity is an exact square. No sharp Gårding inequality is used. The
imaginary part is absorbed through the large constant $M$, by the supremum bound of Lemma 2.6.

## Sources

[Hin26c] P. Hintz, *(Non-)linear waves on asymptotically flat spacetimes. II*, arXiv:2606.28008v1. READ: pp. 55 (locus
of microlocalisation, variable orders), 68-71 (Definitions 3.19-3.20, Propositions 3.23-3.24 and their proofs, footnotes
36-38).

[SBG] as in Part II.A: (S1)-(S11); Proposition 3.3; Remarks 3.33, 3.47, 3.48; (3.26)-(3.28) and the cut-off $\psi$ before
them (p. 43); the paragraph before Definition 3.34; Definition 4.6 and the paragraph after it (p. 66).

Part I.A: Lemmas 3.1-3.2 and Proposition 5.2 (the structure of the commutator argument, here redone with operators of
finite regularity), section 3 (the cut-off $\psi$ and the regulariser). Part II.A: section 8.3 (cut-offs), Lemmas 8.2,
8.4-8.6.

Standard theorems used by name: the closed graph theorem and the theorem of Banach and Steinhaus (Fréchet spaces), Hahn
and Banach, the spectral theorem for Hermitian matrices, Gronwall's inequality, the implicit function theorem, and
existence, uniqueness and differentiable dependence for ordinary differential equations with $C^r$ right side.

[Vas18] A. Vasy, *A minicourse on microlocal analysis for wave propagation*, in: Asymptotic analysis in general
relativity, LMS Lecture Note Ser. 443 (2018). Cited in (G6) for the standard form of the hypothesis, as the source cites
it; not READ here, and nothing is taken from it.
