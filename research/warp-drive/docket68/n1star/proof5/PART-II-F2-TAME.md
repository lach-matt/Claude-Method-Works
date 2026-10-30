# Part II.F$'$. Forward solutions of admissible wave-type operators, and tame estimates, at n = 4

*Status.* Verified. Written out in full (D210) and read line by line by the eighty-eighth verifier (D212): one major
finding, that the uniqueness class of Theorem 1.1 was too large for the smallness assumed, repaired by restricting it;
one minor finding and two notes, seated (section 8.4). The part is labelled proved once the next reader has confirmed
the repairs. This part
proves, at spatial dimension $n = 4$, [Hin26c] section 11 (pp. 227-233): Theorem 11.1, which solves forward problems for
admissible wave-type operators $P$ on b-Sobolev spaces with decay at $\mathscr I^+$, $\iota^+$ and $K^+$, with estimates
tame in the b-regularity, and its Remarks 11.2-11.4. The source is [Hin26c] = P. Hintz, arXiv:2606.28008v1 (printed page
numbers). Parts II.A (`PART-II-A-SETUP.md`), II.A$'$, II.C, II.D, II.D$'$, II.E (`PART-II-E-ENERGY.md`) and II.F
(`PART-II-F-IOTA.md`) are cited as II.A, II.A$'$, II.C, II.D, II.D$'$, II.E and II.F.

*Method.* As in the source, the forward solution of $Pu = f$ is the weak limit of the forward solutions of operators
$P_\epsilon$ that equal $P$ up to a time of order $\epsilon^{-1}$ and the stationary model $P_0$ after it. The a priori
estimate for $P_\epsilon$, uniform in $\epsilon$, joins the global estimate of II.E Theorem 6.1 to the forward solution
estimate for $P_0$ of II.F Theorem 8.1; the error $(P_\epsilon-P_0)u$ is small near $\iota^+\cup K^+$, where the weights
gain, and is controlled at bounded times by the energy estimates on slabs of II.E. Three points that the source passes
over are written out here. The order function is taken with margin $3+\delta+\aleph$: with the source's
$2+\delta+\max(1,\aleph)$ the order two below it does not meet the hypotheses of II.F Theorem 8.1 when $\aleph\ge1$
(section 2.3). The cut-offs are functions of the time function $t^\flat$ of II.C Lemma 3.2, whose level sets carry the
slabs on which forward solutions are unique; the source's cut-offs in $t_*$ do not keep the supports apart (section 2.6).
And the tame bound on the error needs a single extension across the artificial boundary $\{r = r_0\}$ that is bounded at
every order of b-regularity at once; it is constructed where the order function is a constant integer (sections 2.4-2.5).

*Organisation.* Section 1: the spaces, the statement (Theorem 1.1), its form with unweighted b-densities (Corollary 1.2),
and what is not carried. Section 2: the threshold for perturbations, uniqueness, the orders, two lemmas on variable
orders and extensions, the family $P_\epsilon$, cut-offs, the tame bound on $P_\epsilon-P_0$, and forward solutions of
$P_\epsilon$. Section 3: small b-regularity orders. Section 4: large b-regularity orders and the tame estimate. Section
5: pure b-estimates; the proofs of Theorem 1.1 and Corollary 1.2. Section 6: continuous dependence. Section 7: Remarks
11.2-11.4 at $n = 4$. Section 8: findings, and the sources.

## 1. Setting and statement

### 1.1 Domains, weights and spaces

$P_0$ is a stationary wave-type operator on the bundle $E$ (II.C Definition 1.1), in the setting of II.D section 1.1,
with $\bar S = \inf_{\partial X}\min\mathrm{Re}\,\mathrm{spec}\,S$ ((5.2) of the source; II.C Definition 3.5 with $\tilde
p_1 = 0$). $t^\flat := t^\flat_*$ is the time function of II.C Lemma 3.2, defined on $\Omega^\circ$ and, by II.E Lemma
1.2 (iv), on $\{r\ge r^\sharp,\ t_*\ge\frac12\}$, and
$$\Omega_* := \mathrm{cl}_M\{t^\flat\ge1\}\subset\Omega = \mathrm{cl}_M\{t_*\ge1,\ r\ge r_0\}$$
(II.C Lemma 3.2 (b): $C't_*\le t^\flat\le t_*$). For $T>1$ the *slab* $\Omega_{1,T} := \Omega_*\cap\{t^\flat\le T\}$ is
that of II.E section 1.1. On $\Omega$ we use the defining functions of II.A section 1 (II.A Lemma 8.8),
$$x_I^2 = \rho_I = \frac{t_*}{t_*+r},\qquad\rho_+ = \frac{t_*+r}{t_*r},\qquad\rho_K = \frac r{t_*+r},\qquad\rho_+
\rho_K = t_*^{-1},\tag{1.1}$$
of $\mathscr I^+$, $\iota^+$ and $K^+$; the formulae define smooth positive functions on $\{r>0,\ t_*>0\}$, and we use
them also on the extension region $\{r^\sharp\le r\le r_0\}$. For an order function $\mathsf t$, $k\in\mathbb N_0$ and
weights, $H^{(\mathsf t;k),(2\alpha_I,\alpha_+,\alpha_K)}_{e3b;b}(\Omega_*;E)^{\bullet,-}$ is the space of restrictions
to $\{r>r_0\}$ of elements of $H^{(\mathsf t;k),(2\alpha_I,\alpha_+,\alpha_K)}_{e3b;b}$ (II.A section 4.2) supported in
$\{t^\flat\ge1\}$, with the quotient norm (II.A section 7, II.D section 1.1). Following the source ((11.1)), the
*b-spaces* carry powers of $\rho_I = x_I^2$ at $\mathscr I^+$:
$$H^{k,(\alpha_I,\alpha_+,\alpha_K)}_b := \rho_I^{\alpha_I}\rho_+^{\alpha_+}\rho_K^{\alpha_K}H^k_b = H^{(0;k),(2\alpha_I,
\alpha_+,\alpha_K)}_{e3b;b}\tag{1.2}$$
(II.A Lemma 8.4 (d)), with the density $|dt\,dx|$, and $H^{k,(\alpha_I,\alpha_+,\alpha_K)}_b(\Omega_*;E)^{\bullet,-}$
likewise. On $\Omega$, $t_*\partial_{t_*}$ and $r\partial_x$ span $\mathcal V_b$ (II.C section 2.4). $C^\infty_b$ denotes
the functions on a neighbourhood of $\Omega_*$ in $M$ that are bounded with all their b-derivatives. Multiplication by an
element of $C^\infty_b$ is bounded on every $H^{(\mathsf t;k),w}_{e3b;b}$, with norm bounded by finitely many of its
$C^\infty_b$-seminorms (II.A, after (8.1)): the e3b-vector fields are combinations of b-vector fields with smooth
coefficients (II.A Lemma 2.9), so b-smoothness gives uniform smoothness on the e3b unit cells, and the b-derivatives of
an element of $C^\infty_b$ lie in $C^\infty_b$. By acting on extensions it is bounded on the spaces
$(\Omega_*)^{\bullet,-}$. Powers $\rho^a$, $a\ge0$, of the functions (1.1) lie in $C^\infty_b$.

### 1.2 The statement

**Theorem 1.1 ([Hin26c] Theorem 11.1 at $n = 4$).** Let $P_0$ be $\aleph$-admissible with sf-weight $\alpha_+$ and
sf-loss $\delta$ (II.C Definition 2.7), let
$$\alpha_I<-\tfrac12+\bar S,\qquad\alpha_+<\alpha_I-\tfrac12,\tag{1.3}$$
and let $\ell_I\in(0,\frac12]$, $\ell_+\in(\delta,1]$, $\ell_K>\aleph$. There are $\epsilon_0>0$ and $d\in\mathbb N$ such
that the following holds for every $k\in\mathbb N_0$ and every $P$ admissible relative to $P_0$ of class
$((0;k+d),(2\ell_I,\ell_+,\ell_K))$ (II.C Definition 3.3) with $\|P-P_0\|_{(0;d),(2\ell_I,\ell_+,\ell_K)}<\epsilon_0$
(II.C Definition 3.6, over $\Omega_*$). For every
$$f\in H^{k+d,(\alpha_I+1,\alpha_++2,0)}_b(\Omega_*;E)^{\bullet,-}\tag{1.4}$$
there is exactly one $u$ in $\bigcup_{s'\ge s_{\mathrm u},\ \beta_+,\beta_K\in
\mathbb R}H^{s',(2\alpha_I,\beta_+,\beta_K)}_{e3b}(\Omega_*;E)^{\bullet,-}$ with $Pu = f$, the *forward solution*; here
$s_{\mathrm u} := \inf\mathsf s-2$ for the order $\mathsf s$ of section 3.1, which depends only on $P_0$ and the
weights (D212). It lies in
$H^{k,(\alpha_I,\alpha_+-\delta,-\aleph)}_b(\Omega_*;E)^{\bullet,-}$, and
$$\|u\|_{H^{k,(\alpha_I,\alpha_+-\delta,-\aleph)}_b}\le C_k\Big(\|f\|_{H^{k+d,(\alpha_I+1,\alpha_++2,0)}_b}+\|P-P_0
\|_{(0;k+d),(2\ell_I,\ell_+,\ell_K)}\|f\|_{H^{d,(\alpha_I+1,\alpha_++2,0)}_b}\Big),\tag{1.5}$$
the norms over $\Omega_*$, with $C_k$ independent of $P$ and $f$. For $k\ge1$ the map $(P,f)\mapsto u$ is continuous from
the set of such $P$, with the norm $\|P-P_0\|_{(0;k+d),(2\ell_I,\ell_+,\ell_K)}$, times the space (1.4), to
$H^{k-1,(\alpha_I-\varsigma,\alpha_+-\delta-\varsigma,-\aleph-\varsigma)}_b(\Omega_*;E)^{\bullet,-}$, for every
$\varsigma>0$.

The source states the theorem with $\ell_+>\delta$; the class of II.C Definition 3.1 has $\ell_+\le1$. The source's
conditions are those of (1.3), and the argument at $n = 4$ is the source's except at the points listed in section 8; the
dimension enters through the densities (Corollary 1.2) and through the indicial gap (section 7).

**Corollary 1.2 ([Hin26c] (11.4)-(11.7) at $n = 4$).** Put $\mu_b := |dt_*\,dx|/(t_*\langle x\rangle^4)$, a smooth
positive b-density on $\tilde M$ near $\bar\Omega$ (II.A Lemma 8.8), and
$$b_I := \alpha_I+2,\qquad b_+ := \alpha_++\tfrac52.\tag{1.6}$$
Then (1.3) reads $b_I<\frac32+\bar S$ and $b_+<b_I$, and $P_0$ is $\aleph$-admissible with sf-weight $b_+-\frac52$. With
$\mu_b$, (1.5) reads
$$\|u\|_{H^{k,(b_I,b_+-\delta,-\aleph+\frac12)}_b(\Omega_*,\mu_b)}\le C_k\Big(\|f\|_{H^{k+d,(b_I+1,b_++2,\frac12)}_b(
\Omega_*,\mu_b)}+\|P-P_0\|_{(0;k+d),(2\ell_I,\ell_+,\ell_K)}\|f\|_{H^{d,(b_I+1,b_++2,\frac12)}_b(\Omega_*,\mu_b)}\Big),
\tag{1.7}$$
In terms of integrals, the square of the left side of (1.7) is equivalent to
$\iint_{\Omega_*}|\rho_I^{-b_I}\rho_+^{-b_++\delta}\rho_K^{\aleph-\frac12}(t_*\partial_{t_*},r\partial_x)^{\le
k}u|^2\,dt_*\,dx/(t_*r^4)$, the power meaning all products of at most $k$ of the fields, with the weights (1.1); the
norms of $f$ likewise. This is the source's (11.6b), with $r^4$ for $r^3$. Pointwise, for $k\ge3$, on
$\Omega_*\cap\{r>r_0\}$,
$$\big|(t_*\partial_{t_*},r\partial_x)^{\le k-3}u\big|\le C_k\,(\text{right side of (1.5)})\,\rho_I^{b_I}\rho_+^{b_+-
\delta}\rho_K^{-\aleph+\frac12}.\tag{1.8}$$

At $n = 3$ the source has $b_I = \alpha_I+\frac32$, $b_+ = \alpha_++2$, the density $|dt_*\,dx|/(t_*r^3)$ and the
conditions $b_I<1+\bar S$, $b_+<b_I$ ((11.5)-(11.7)).

### 1.3 What is not carried

(a) The source adds that, if the principal part of $P$ is that of $P_0$, the theorem holds with $\Omega =
\mathrm{cl}_M\{t_*\ge1\}$ in place of $\Omega_*$, by local solvability between $\{t_* = 1\}$ and $\{t^\flat = 1\}$. That
region meets $\mathscr I^+$ only at $\{t_* = 1\}$, where its two boundary hypersurfaces meet, and the energy estimates of
II.E are not proved on it. The statement is not proved here, and is not used by the later parts of this write-out, whose
operators are quasilinear (their principal parts vary).

(b) The source allows $P_0$ to vary among small stationary perturbations of an $\aleph$-admissible $P_1$, and among the
stationary models of nearby parameters, with uniform constants. II.E Theorem 6.1 is uniform in this sense (its last
sentence), but II.F Theorem 8.1 and the $\aleph$-admissibility estimate (II.C (2.2)) are proved, resp. assumed, for one
$P_0$. Here $P_0$ is fixed. The uniform version is recorded as open, to be proved before a later part uses it (section 8,
(F'11)).

## 2. Preliminaries

Throughout, $\alpha_I$, $\alpha_+$, $\ell_I$, $\ell_+$, $\ell_K$, $\aleph$ and $\delta$ are as in Theorem 1.1, and
$$\delta' := \min(\ell_+-\delta,\ \ell_K-\aleph)>0.\tag{2.1}$$
For an order function $\mathsf t$ and $k\in\mathbb N_0$ we write, all over $\Omega_*$ with the spaces
$(\Omega_*;E)^{\bullet,-}$ of section 1.1,
$$X(\mathsf t;k) := H^{(\mathsf t;k),(2\alpha_I,\alpha_+-\delta,-\aleph)}_{e3b;b},\qquad Y(\mathsf t;k) := H^{(
\mathsf t;k),(2\alpha_I+2,\alpha_++2,0)}_{e3b;b},$$
$$Y'(\mathsf t;k) := H^{(\mathsf t;k),(2\alpha_I+2,\alpha_+-\delta+2,-\aleph)}_{e3b;b},\qquad Z(\mathsf t;k) := H^{(
\mathsf t;k),(2\alpha_I,\alpha_+-\ell_+,-\ell_K)}_{e3b;b}.\tag{2.2}$$
As $\rho_+$, $\rho_K$ are bounded on $\Omega$, $\|\cdot\|_{Y'}\le C\|\cdot\|_Y$ and $\|\cdot\|_Z\le C\|\cdot\|_X$ (the
weights of $Y$ and $X$ are the larger at every face, $\delta<\ell_+$ and $\aleph<\ell_K$). These are Hilbert spaces: each
is a quotient of a closed subspace of a Hilbert space, the norm (II.A (8.1)) being equivalent to the Hilbert norm of
(S3).

### 2.1 The threshold for perturbations

**Lemma 2.1 (the threshold at $\mathscr I^+$).** Let $\delta_S := \frac14(\bar S-\frac12-\alpha_I)>0$. Let $h_S$ be a
fibre inner product on $\mathbb C^N$ with $\lambda_{\min}(\frac12(S+S^{*h_S}))\ge\bar S-\frac12\delta_S$ on $\partial X$
(II.C Lemma 2.5), pulled back to $\mathscr I^+$ along its fibration over $\partial X$ and extended independently of
$x_I$, as the data of II.C Definition 3.3 (2) are. There is $\epsilon_1>0$ such that, for every operator $P$ with (1) and
(2) of II.C Definition 3.3 and $\sup_{\mathscr I^+\cap\Omega}|\tilde p_1|_{h_S}\le\epsilon_1$ (in particular if
$\|P-P_0\|_{(0;0),(2\ell_I,\ell_+,\ell_K)}$ is small), and for every $\alpha\le\alpha_I$:

(a) $\mathrm{Re}_{h_S}p_1\ge\bar S-\delta_S$ on $\mathrm{cl}(\mathscr I^+\cap\Omega)$, and the same holds for the
extension $P^{\mathrm{ext}}$ of II.E Lemma 1.2 on $t_*\in[1-\eta_0,1]$; hence $\bar p_1\ge\bar S-\delta_S$ and
$\alpha<-\frac12+\bar p_1$;

(b) the statements of II.D, II.D$'$ and II.E that assume $\alpha<-\frac12+\bar p_1$ at the weight $\alpha$ at $\mathscr
I^+$ (II.D (1.3) and (3.9); II.E Lemma 2.5, Proposition 2.7, Propositions 3.2, 3.4, 4.3, 4.4 and Theorem 6.1) hold for
$P$, with constants depending on $P$ only through the norms named in them, $h_S$ and $\delta_S$; and condition (3) of
II.C Definition 3.3 is not needed for them.

*Proof.* (a) $S|_{\partial X}$ is independent of $t_*$ and of $x_I$ in the extension, so $\mathrm{Re}_{h_S}S\ge\bar
S-\frac12\delta_S$ on a neighbourhood of $\mathrm{cl}(\mathscr I^+\cap\Omega)$, where $p_1 = S|_{\partial X}+\tilde p_1$.
As $|\mathrm{Re}_{h_S}\tilde p_1|\le|\tilde p_1|_{h_S}$, and the Seeley extension of II.E Lemma 1.2 multiplies sup norms
by at most $c_\Sigma := \sum_l|c_l|$, $\epsilon_1 := \delta_S/(2+2c_\Sigma)$ gives both claims. Every eigenvalue $\mu$ of
$p_1$ has an eigenvector $v$, and $\mathrm{Re}\,\mu\,h_S(v,v) = \mathrm{Re}\,h_S(p_1v,v)\ge(\bar S-\delta_S)h_S(v,v)$; so
$\bar p_1\ge\bar S-\delta_S$, and $\bar p_1-\frac12-\alpha\ge\bar S-\delta_S-\frac12-\alpha_I = 3\delta_S>0$.

(b) The proofs use $\bar p_1$ only through a fibre inner product $h_I$ with $\mathrm{Re}_{h_I}p_1\ge\bar p_1-\delta'_I$,
$\delta'_I := \frac14(\bar p_1-\frac12-\alpha)$ (II.D Proposition 3.6; II.E (1.2), with Lemma 1.2 (iii) for
$2\delta'_I$), and they use that inequality only through its consequence
$$4\,\mathrm{Re}_{h_I}p_1-2-4\alpha\ge12\delta'_I>0\tag{2.3}$$
at the radial set $R = \partial R_{\mathscr I^+,\mathrm{out}}$ (II.D Proposition 3.6, where $Q_\epsilon\ge4(\bar
p_1-\delta'_I-\frac12-\alpha_I) = 12\delta'_I$; II.E Lemma 2.5, where the coefficient of $\tau_0^2$ is
$-2(2\alpha+1)+4(\bar p_1-\delta'_I) = 12\delta'_I$; II.E Proposition 3.2, where
$4A^{-1}(\mathrm{Re}_{h_I}p_1)A-2-4\alpha\ge8\delta'_I$ with $2\delta'_I$; and II.E section 7, (E2), which records that
nothing else of $p_1$, $p_0$ is used). The commuted systems of II.D$'$ and II.E section 4 have the same $p_1$ (II.E (4.1)
and the paragraph after it), at the weights $\alpha-\frac j2\le\alpha$. By (a), $h_S$ in place of $h_I$ and $\delta_S$ in
place of $\delta'_I$ satisfy (2.3) with $12\delta_S$, for every $\alpha\le\alpha_I$, so the proofs run verbatim with
$(h_S,\delta_S)$, and their constants depend on these instead of on $(h_I,\delta'_I)$. A search of Parts II.C-II.E for
the use of II.C Definition 3.3 (3), the triangular structure of $p_1$ and $p_0$, finds only the fibre inner product,
which (a) replaces (II.E section 7, (E2), records that the source's use of (3), to make $\mathrm{Im}\,p_1$ and $p_0$
small, is not needed). $\square$

Below, "admissible" for $P$ and for the operators $P_\epsilon$ of section 2.6 means (1) and (2) of II.C Definition 3.3
together with the smallness of Lemma 2.1, and every citation of II.D, II.D$'$ or II.E is in the sense of Lemma 2.1 (b).

### 2.2 Uniqueness

**Lemma 2.2 (uniqueness on $\Omega_*$).** Let $P$ be $P_0$, or admissible with $\|P-P_0\|_{(d_0;0)}$ small (Lemma 2.1,
and the smallness of II.E Proposition 3.4, $d_0$ depending on $s'$), and let $\alpha\le\alpha_I$,
$s',\beta_+,\beta_K\in\mathbb R$. If $u\in H^{s',(2\alpha,\beta_+,\beta_K)}_{e3b}(\Omega_*;E)^{\bullet,-}$ and $Pu = 0$,
then $u = 0$. The same holds on a slab $\Omega_{1,T}$ for $u$ in its space $H^{s',2\alpha}(\Omega_{1,T})^{\bullet,-}$
(II.E section 1.1).

*Proof.* The second claim is II.E Proposition 3.4 (i), with Lemma 2.1 (b). For the first, let $T>2$ and $\phi =
\phi(t^\flat)\in C^\infty(\mathbb R)$ equal to 1 on $(-\infty,T+1]$ and to 0 on $[T+2,\infty)$; $\phi(t^\flat) =
\tilde\phi(1/t^\flat)$ with $\tilde\phi(y) := \phi(1/y)$, $\tilde\phi'\in C^\infty_c((0,\infty))$, so $\phi(t^\flat)\in
C^\infty_b$ by Lemma 2.6 (a) below (with $\epsilon = 1$; its proof uses nothing from this section); the same holds for
every function of $t^\flat$ used below. If $\tilde u$ extends $u$ with support in $\{t^\flat\ge1\}$, then $\phi\tilde u$
is supported in $\{1\le t^\flat\le T+2\}$, where $t_*\le(T+2)/C'$, so $\rho_+$, $\rho_K$ are bounded below there by
(1.1), and $\phi\tilde u\in H^{s',(2\alpha,0,0)}_{e3b}$. It extends $u|_{\Omega_{1,T}}$, which therefore lies in
$H^{s',2\alpha}(\Omega_{1,T})^{\bullet,-}$ and solves $Pu = 0$ there. So $u = 0$ on $\{t^\flat<T,\ r>r_0\}$, for every
$T$. $\square$

### 2.3 The orders

Write $T_{\mathcal H} := \frac12+\vartheta_{\mathcal H}$, $T_{\mathrm{out}} := \frac12(-1+\vartheta_{\mathrm{out}})$ and
$T_{\mathrm{in}} := \frac12(-1+\vartheta^{3b}_{\mathrm{in}})$ for the thresholds of II.C Definition 2.4, each in the
fibre inner product chosen for its radial set. An order function is admissible for $P_0$ with weights $a_+$, $a_K$ and
margin $\eta$ (II.C Definition 5.2) if it has (2)-(5) of II.C Proposition 5.1, which do not involve the weights, and,
near the three radial sets over $K^+$,
$$\mathsf t>T_{\mathcal H}+\eta,\qquad\mathsf t+a_+-a_K<T_{\mathrm{out}}-\eta,\qquad\mathsf t+a_+-a_K>T_{\mathrm{in}}+
\eta,\tag{2.4}$$
by II.C Definition 2.4 (1)-(6) with $\alpha_{\mathrm{sf}} = a_+$, $\alpha_K = a_K$ (the order being constant near each
radial set).

**Lemma 2.3 (the orders).** Let $m_0 := 3+\delta+\aleph$. There is $\mathsf s\in C^\infty({}^{e3b}S^*_\Omega M)$,
admissible for $P_0$ with weights $\alpha_+-\delta$, $-\aleph$ and margin $m_0$, and an integer $s_{\mathrm{in}}\ge4$,
such that $\mathsf s = s_{\mathrm{in}}$ over
$$\Omega_\natural := \{t_*\ge\tfrac12,\ r_0-2\delta_0<r\le r_0+4\}\tag{2.5}$$
(with the extension of II.E section 3.2 below $r = r_0$), and $\mathsf s\le s_{\mathrm{in}}$ everywhere. Put $\mathsf s_0
:= \mathsf s-2$. Then:

(a) $\mathsf s_0<\mathsf s$ are admissible for $P_0$ with weights $\alpha_+-\delta$, $-\aleph$ and margin 0 (the
hypothesis of II.E Theorem 6.1 at the weights $\alpha_+-\delta$, $-\aleph$);

(b) $\mathsf s_0$ and $\mathsf s$ are each admissible for $P_0$ with weights $\alpha_+$, $-\aleph$ and margin 0, and with
weights $\alpha_+$, 0 and margin 1 (the hypotheses of II.F Theorem 8.1);

(c) $\mathsf s$ and $\mathsf s+1$ are slab orders (II.E section 3.2).

*Proof.* II.C Proposition 5.1 with $\eta := m_0$ and the weights $\alpha_+-\delta$, $-\aleph$ is proved by the
construction of II.C section 5.2, $\mathsf s = s_{\mathrm{in}}-(s_{\mathrm{in}}-s_{\mathrm{out}})\chi$ with
$0\le\chi\le1$, in which $s_{\mathrm{in}}$ is any constant above a stated bound and the small constants $\epsilon_I$,
$\epsilon_\iota$ may be decreased before the others are chosen. Take $s_{\mathrm{in}}\in\mathbb N$,
$s_{\mathrm{in}}\ge4$, and $\epsilon_I^2<(2r_0+9)^{-1}$, $(\epsilon_\iota\delta_\iota)^{-1}>r_0+4$, where $\delta_\iota$
is the constant called $\delta$ in II.C section 5.2. Then $\mathsf s\le s_{\mathrm{in}}$. On $\Omega_\natural\cap\{r\ge
r_0\}$, $x_I^2 = t_*/(t_*+r)\ge\frac12/(\frac12+r_0+4)>\epsilon_I^2$, so $\psi_0(x_I) = 0$, and
$r<(\epsilon_\iota\delta_\iota)^{-1}$, so $\chi_\iota = 0$ there ($\chi_\iota$ is supported in
$\{\varrho<\epsilon_\iota\delta_\iota\}$, $\varrho = r^{-1}$); hence $\chi = 0$ and $\mathsf s = s_{\mathrm{in}}$. Below
$r = r_0$, $\mathsf s = s_{\mathrm{in}}$ by its extension (II.C section 5.2, last lines of *Values*; II.E section 3.2).

(a), (b): (2)-(5) of II.C Proposition 5.1 hold for $\mathsf s-j$, $j\in\mathbb Z$, as for $\mathsf s$ (a constant shift
changes no derivative and no constancy). For (2.4), let $\mathsf s$ satisfy it with $(a_+,a_K) =
(\alpha_+-\delta,-\aleph)$ and $\eta = m_0$. Then $\mathsf s-j$ satisfies it with weights $(a'_+,a'_K)$ and the margins
$$m_0-j\ \ \text{at}\ \mathcal H^+,\qquad m_0+j-(a'_+-\alpha_++\delta)+(a'_K+\aleph)\ \ \text{at}\ R_{\mathrm{out}},
\qquad m_0-j+(a'_+-\alpha_++\delta)-(a'_K+\aleph)\ \ \text{at}\ R_{\mathrm{in}}.$$
For $(a'_+,a'_K) = (\alpha_+-\delta,-\aleph)$ these are $m_0-j$, $m_0+j$, $m_0-j$, all $\ge0$ for $j\in\{0,2\}$: (a). For
$(\alpha_+,-\aleph)$ they are $m_0-j$, $m_0+j-\delta = 3+\aleph+j$, $m_0-j+\delta$, all $\ge0$ for $j\in\{0,2\}$. For
$(\alpha_+,0)$ they are $m_0-j = 3+\delta+\aleph-j$, $m_0+j-\delta+\aleph = 3+2\aleph+j$ and $m_0-j+\delta-\aleph =
3+2\delta-j$, all $\ge1$ for $j\in\{0,2\}$: (b).

(c) Admissible order functions are slab orders, and $\mathsf s+1$ has the same monotonicity and constancy (II.E section
3.2). $\square$

With the source's margin $2+\delta+\max(1,\aleph)$ the last margin for $\mathsf s_0$ is $\max(1,\aleph)-\aleph+2\delta$,
which is less than 1 when $\aleph\ge1$ and $\delta<\frac12$ (section 8, (F'1)).

Fix $\mathsf s$, $s_{\mathrm{in}}$ and $\mathsf s_0$ as in Lemma 2.3. Only $\mathsf s$, $\mathsf s_0$ and $\mathsf s+1$
occur below; each equals a nonnegative integer over $\Omega_\natural$.

### 2.4 Variable orders that agree on a set

**Lemma 2.4 (pseudolocality of the order).** Let $\mathsf t_1$, $\mathsf t_2$ be order functions (II.A (S8)) and
$U\subset\tilde M$ open with $\mathsf t_1 = \mathsf t_2$ over $U$, and let $K\subset U$ be closed with $\phi\in
C^\infty_b$, $\mathrm{supp}\,\phi\subset U$, $\phi = 1$ near $K$. For every $j\in\mathbb N_0$, $N$ and weight $w$ there
is $C$ with
$$\|v\|_{H^{(\mathsf t_2;j),w}_{e3b;b}}\le C\big(\|v\|_{H^{(\mathsf t_1;j),w}_{e3b;b}}+\|v\|_{H^{(-N;j),w}_{e3b;b}}
\big)$$
for every $v$ supported in $K$.

*Proof.* Weights are removed by conjugation (II.A, after (8.1)). Let $A_i\in\Psi^{\mathsf t_i}_{e3b}$ be elliptic, so
that $\|v\|_{(\mathsf t_i;j)}$ is equivalent to $\|A_iv\|_{(0;j)}+\|v\|_{(-N;j)}$ ((S8); for the b-derivatives, (S10) and
II.A Lemma 8.4 (a)). Let $B\in\Psi^{-\mathsf t_1}_{e3b}$ with $BA_1 = I-R$, $R\in\Psi^{-N'}_{e3b}$, $N'$ large (the
finite parametrix of II.A Lemma 7.1's proof, at variable orders by (S8)). As $v = \phi v$,
$$A_2v = (A_2\phi B)A_1v+A_2\phi Rv.$$
$Q := A_2\phi B\in\Psi^{\mathsf t_2-\mathsf t_1}_{e3b}$ has $\mathrm{WF}'(Q)\subset\mathrm{WF}'(\phi)$, over
$\mathrm{supp}\,\phi$ ((S5)). Let $\phi_1\in C^\infty_b$ with $\mathrm{supp}\,\phi_1\subset U$ and $\phi_1 = 1$ near
$\mathrm{supp}\,\phi$. Then $(1-\phi_1)Q$ has empty operator wave front set, so it is residual; and $\phi_1Q$ is the left
quantization multiplied by $\phi_1$, whose symbol is $\phi_1q$ with $q$ the symbol of $Q$, of order $\mathsf t_2-\mathsf
t_1 = 0$ on $\mathrm{supp}\,\phi_1$, so $\phi_1q\in\bigcap_\delta S^0_{1-\delta,\delta}$ ((S8)), and $\phi_1Q$ is bounded
on $H^{(0;j)}$ ((S8), (S10)). Hence $\|A_2v\|_{(0;j)}\le C\|A_1v\|_{(0;j)}+C\|v\|_{(-N;j)}$, $A_2\phi R$ being of order
$\sup\mathsf t_2-N'\le-N$. $\square$

### 2.5 An extension across $\{r = r_0\}$ at every order of b-regularity

The quotient norm of $H^{(\mathsf t;k)}(\Omega_*)^{\bullet,-}$ is attained by an extension that depends on $k$. A tame
estimate bounds a low and a high norm of one function, and so needs one extension that is nearly minimal for both. Away
from $\{r = r_0\}$ a cut-off provides it (II.E Lemma 4.1 (b)); at $\{r = r_0\}$, where $\Omega_*$ ends and no room is
available, the following lemma does.

Fix $\kappa\in(0,\frac14]$ with $r_0-2\kappa>r^\sharp$ and $r_0+4\kappa\le r^\natural$ (II.E Lemma 1.2, II.D (1.2)). On
$N_\kappa := \{t_*>\frac12,\ r_0-2\kappa<r<r_0+4\kappa\}$, $t^\flat = C'(t_*+\tilde R(r))$ with $\tilde R = r'_0$ or
$\tilde R' \in[0,1]$ (II.C Lemma 3.2 (c) and its proof; II.E Lemma 1.2 (iv)), so $(t^\flat,r,\omega)$ are coordinates on
$N_\kappa$, and $C't_*\le t^\flat\le t_*$ there. In them the e3b-vector fields over $N_\kappa$ are spanned by
$\partial_{t^\flat}$, $\partial_r$, $\partial_\omega$ and the b-vector fields by $t^\flat\partial_{t^\flat}$,
$\partial_r$, $\partial_\omega$, with coefficients in $C^\infty_b$: near $K^+$ the e3b-fields are spanned by
$\partial_{t_*}$, $\partial_x$ and the b-fields by $t_*\partial_{t_*}$, $\partial_x$ (II.E section 5.1), and
$\partial_{t_*} = C'\partial_{t^\flat}$, $\partial_r|_{t_*} = \partial_r|_{t^\flat}+C'\tilde R'\partial_{t^\flat}$,
$t_*\partial_{t_*} = (C't_*/t^\flat)\,t^\flat\partial_{t^\flat}$, with $C't_*/t^\flat = t_*/(t_*+\tilde R)$ and $C'\tilde
R'/t^\flat$ in $C^\infty_b$ (b-derivatives in $t^\flat\partial_{t^\flat}$ of functions of $t_*/t^\flat$ and of
$(t^\flat)^{-1}$ are bounded). On $N_\kappa$ the weights $x_I^{2a}\rho_+^b\rho_K^c$ are $(t^\flat)^{-c}$ times smooth
positive functions with bounded b-derivatives, and $|dt\,dx|$ is a smooth positive multiple of $|dt^\flat\,dr\,d\omega|$.

Let $c_l$, $\epsilon_l = 3^{-l}$ be the constants of Seeley's operator (II.E Lemma 1.3 (b):
$\sum_l|c_l|\epsilon_l^{-q}<\infty$ and $\sum_lc_l(-\epsilon_l^{-1})^q = 1$ for all $q\in\mathbb N_0$). For $w$ on
$\{r>r_0\}\cap N_\kappa$ supported in $\{r<r_0+2\kappa\}$ put $E_rw := w$ on $\{r>r_0\}$ and
$$(E_rw)(t^\flat,r,\omega) := \sum_lc_l\,w\big(t^\flat,r_0+(r_0-r)/\epsilon_l,\omega\big),\qquad r<r_0,\tag{2.6}$$
which vanishes for $r\le r_0-2\kappa$.

**Lemma 2.5 (a simultaneous extension).** Let $\mathsf t$ be an order function equal to a constant $m\in\mathbb N_0$ over
$\Omega_\natural$ (as $\mathsf s+j$, $j\ge-s_{\mathrm{in}}$, is), and $w$ a weight $x_I^{2a}\rho_+^b\rho_K^c$. There is a
linear map $E$, defined on $\bigcup_jH^{(\mathsf t;j),w}(\Omega_*;E)^{\bullet,-}$, with $Eu$ supported in
$\{t^\flat\ge1\}$, $Eu = u$ on $\{r>r_0\}$, and, for every $j\in\mathbb N_0$,
$$\|Eu\|_{H^{(\mathsf t;j),w}_{e3b;b}}\le C_j\|u\|_{H^{(\mathsf t;j),w}(\Omega_*;E)^{\bullet,-}}.\tag{2.7}$$

*Proof.* Let $\psi = \psi(r)$ equal 1 for $r\le r_0+\kappa$ and 0 for $r\ge r_0+2\kappa$, and $\theta = \theta(r)$ equal
1 for $r\ge r_0$ and 0 for $r\le r_0-\kappa$. For $u$ with an extension $\tilde u$ supported in $\{t^\flat\ge1\}$ put
$$Eu := (1-\psi)\tilde u+E_r(\psi u).$$
The first term does not depend on $\tilde u$: two extensions differ by a distribution supported in $\{r\le r_0\}$, where
$1-\psi = 0$. The second uses only $u$ on $\{r>r_0\}$. So $E$ is well defined and linear, and $Eu = (1-\psi)u+\psi u = u$
on $\{r>r_0\}$. Supports: $(1-\psi)\tilde u$ is supported in $\{t^\flat\ge1\}$; $\psi u$ is supported in
$\{t^\flat\ge1\}\cap N_\kappa$ (as $t^\flat\ge1$ implies $t_*\ge1$), and $E_r$ acts at fixed $t^\flat$, so $E_r(\psi u)$
is supported in $\{t^\flat\ge1,\ r_0-2\kappa\le r\le r_0+2\kappa\}$.

*The first term.* $\|(1-\psi)\tilde u\|_{(\mathsf t;j),w}\le C_j\|\tilde u\|_{(\mathsf t;j),w}$ for every extension
$\tilde u$; the left side being independent of $\tilde u$, it is at most $C_j\|u\|_{(\mathsf t;j),w}$, at every $j$ at
once.

*The second term.* For $v$ supported in the compact-in-$r$ set $K_\kappa := \{t^\flat\ge1,\ r_0-2\kappa\le r\le
r_0+2\kappa\}$, Lemma 2.4 (with $U$ the interior of $\Omega_\natural$, which contains $K_\kappa$ with a neighbourhood
$\phi$ as required, and $\mathsf t$ against the constant $m$, both ways) gives $\|v\|_{(\mathsf
t;j),w}\sim\|v\|_{(m;j),w}$, the terms $\|v\|_{(-N;j)}$ being bounded by either side as $m\ge0\ge-N$. As $m\in\mathbb
N_0$, the norm of (S3) is, on such $v$, equivalent to the differential norm
$$D_{m,j}(v) := \sum_{i+|\alpha|\le j}\ \sum_{p+|\beta|\le m}\big\|(t^\flat)^c(t^\flat\partial_{t^\flat})^i
\partial^\alpha_{r,\omega}\partial^p_{t^\flat}\partial^\beta_{r,\omega}v\big\|_{L^2(|dt^\flat\,dr\,d\omega|)}:$$
the $H^m(\mathbb R^5)$-norm in each scaled chart is the sum of the $L^2$-norms of up to $m$ derivatives, the scaled
coordinate fields and the frame above span the same module over $C^\infty_b$, the derivatives falling on the partition
functions $\chi_\alpha$ give lower-order terms with bounded coefficients, and the weight and density are as described
above (the mixed norm being II.A (8.1)). $E_r$ commutes with $\partial_{t^\flat}$, $t^\flat\partial_{t^\flat}$,
$\partial_\omega$ and with multiplication by functions of $t^\flat$; $\partial_r^qE_rw =
\sum_lc_l(-\epsilon_l^{-1})^q(\partial_r^qw)(t^\flat,r_0+(r_0-r)/\epsilon_l,\omega)$ on $\{r<r_0\}$, whose $L^2$-norm
there is at most $\sum_l|c_l|\epsilon_l^{\frac12-q}\|\partial_r^qw\|_{L^2(\{r>r_0\})}$; and for $w$ smooth up to $\{r =
r_0\}$ the derivatives of $E_rw$ of every order match across $\{r = r_0\}$, since $\sum_lc_l(-\epsilon_l^{-1})^q = 1$, so
that $E_rw$ has no distributional jump terms there. By density of such $w$ in the norm $D_{m,j}$ on $\{r>r_0\}$,
$$D_{m,j}(E_rw)\le C_{m,j}D^+_{m,j}(w),$$
$D^+_{m,j}$ denoting $D_{m,j}$ with the integrals over $\{r>r_0\}$. For any extension $\tilde u$, $\theta\psi\tilde u =
\psi u$ on $\{r>r_0\}$ and $\theta\psi\tilde u$ is supported in $K_\kappa$, so
$$D^+_{m,j}(\psi u)\le D_{m,j}(\theta\psi\tilde u)\le C\|\theta\psi\tilde u\|_{(m;j),w}\le C\|\theta\psi\tilde u\|_{(
\mathsf t;j),w}\le C_j\|\tilde u\|_{(\mathsf t;j),w}.$$
Taking the infimum over $\tilde u$ at each $j$ separately, and using $\|E_r(\psi u)\|_{(\mathsf t;j),w}\le C\|E_r(\psi
u)\|_{(m;j),w}\le CD_{m,j}(E_r(\psi u))$, gives (2.7). $\square$

### 2.6 The family $P_\epsilon$

Fix $\chi_0\in C^\infty_c([0,2))$ with $0\le\chi_0\le1$ and $\chi_0 = 1$ on $[0,\frac32]$. For $\epsilon\in(0,1]$ put
$$\chi_\epsilon := \chi_0\Big(\frac1{\epsilon t^\flat}\Big),\qquad\theta_\epsilon := 1-\chi_\epsilon,
\qquad P_\epsilon := \chi_\epsilon P_0+\theta_\epsilon P = P_0+\theta_\epsilon(P-P_0),\tag{2.8}$$
on $\{r\ge r^\sharp,\ t_*\ge\frac12\}$ (with $P^{\mathrm{ext}}$ of II.E Lemma 1.2 for $P$ there).

**Lemma 2.6.** (a) $\chi_\epsilon = 0$ on $\{t^\flat\le\frac1{2\epsilon}\}$ and $\chi_\epsilon = 1$ on
$\{t^\flat\ge\frac2{3\epsilon}\}$. So $P_\epsilon = P$ on $\{t^\flat<\frac1{2\epsilon}\}$ and $P_\epsilon = P_0$ on
$\{t^\flat>\frac2{3\epsilon}\}$, open sets. Every function $\phi(1/(\epsilon t^\flat))$ with $\phi\in C^\infty(\mathbb
R)$, $\phi'\in C^\infty_c((0,\infty))$, lies in $C^\infty_b$ with seminorms bounded uniformly in $\epsilon\in(0,1]$; in
particular $\chi_\epsilon$, $\theta_\epsilon$ do.

(b) $P_\epsilon$ satisfies (1) and (2) of II.C Definition 3.3, and for all $d_0$, $j$
$$\|P_\epsilon-P_0\|_{(d_0;j),(2\ell_I,\ell_+,\ell_K)}\le C_j\|P-P_0\|_{(d_0;j),(2\ell_I,\ell_+,\ell_K)},\qquad\sup|
\tilde p^\epsilon_1|\le\sup|\tilde p_1|,\tag{2.9}$$
with $C_j$ independent of $\epsilon$ and $P$ (and depending on $d_0$). In particular $P_\epsilon$ is admissible in the
sense of section 2.1 when $P$ is, with the same bounds.

*Proof.* (a) The first claims are $\frac1{\epsilon t^\flat}\ge2$, resp. $\le\frac32$. Let $V$ be a b-vector field and
$\varsigma := 1/(\epsilon t^\flat)$; then $V\varsigma = -\varsigma\,V\log t^\flat$. On $\{r\ge r^\sharp,\
t_*\ge\frac12\}$, $\log t^\flat = \log t_*+\log(t^\flat/t_*)$, $\log t_* = -\log\rho_+-\log\rho_K$ by (1.1), and
$t^\flat/t_*\in[C',1]$ has bounded b-derivatives: near $\mathscr I^+$ it is $1-(t_*/r)^{\ell_I}$ with $(t_*/r)^{\ell_I} =
(x_I^2/(1-x_I^2))^{\ell_I}$ conormal, in the transition region a smooth function of $t_*/r$ on a compact range, and near
$K^+$ it is $C'(1+\tilde R(r)\rho_+\rho_K)$ (II.C Lemma 3.2 and its proof). So $V\log t^\flat\in C^\infty_b$, and by
induction $V_1\cdots V_q\varsigma$ is $\varsigma$ times an element of $C^\infty_b$ independent of $\epsilon$. The
b-derivatives of $\phi(\varsigma)$ are sums of $\phi^{(i)}(\varsigma)\varsigma^{i}$ times such elements, $i\ge1$, and
$\phi^{(i)}(\varsigma)\varsigma^i$ is bounded as $\phi^{(i)}$ has compact support in $(0,\infty)$.

(b) *The metric.* $\sigma_2(P_\epsilon) = \chi_\epsilon G_0+\theta_\epsilon G$, so $g_\epsilon^{-1} :=
g_0^{-1}+\theta_\epsilon(g^{-1}-g_0^{-1})$, with $g^{-1}-g_0^{-1}\in
x_I^2\rho_+^2C^{(d_0;j),(2\ell_I,\ell_+,\ell_K)}_{e3b;b}$ of norm $\le C\|P-P_0\|$ (proof of II.C Lemma 3.7). By (a) and
II.A Lemma 8.2 (c)-(d), $\theta_\epsilon(g^{-1}-g_0^{-1})$ has norm $\le C_j\|P-P_0\|_{(d_0;j)}$, and the Neumann series
of II.C Lemma 3.7 gives $g_\epsilon\in\mathcal G^{(d_0;j),(2\ell_I,\ell_+,\ell_K)}_{e3b;b}$ with $\|g_\epsilon-g_0\|\le
C_j\|P-P_0\|_{(d_0;j)}$: (1).

*The data at $\mathscr I^+$.* On $\mathscr I^+$, $t^\flat = t_*$ (II.C Lemma 3.2 (a)), and $\theta_\epsilon|_{\mathscr
I^+}$ is bounded in $C^\infty_b(\mathscr I^+\cap\Omega)$ uniformly in $\epsilon$. Put $p^\epsilon_0 :=
\theta_\epsilon|_{\mathscr I^+}p_0$, $\tilde p^\epsilon_1 := \theta_\epsilon|_{\mathscr I^+}\tilde p_1$, in
$\rho_+^{\ell_+}C^{j+d_0}_b(\mathscr I^+\cap\Omega)$ with norms $\le C_j$ times those of $p_0$, $\tilde p_1$, and
$|\tilde p_1^\epsilon|\le|\tilde p_1|$ as $0\le\theta_\epsilon\le1$. Let $\pi$ be the projection of the product structure
$[0,\epsilon)_{x_I}\times\mathscr I^+$ in which II.C Definition 3.3 (2) extends the data independently of $x_I$; near
$\mathscr I^+\cap\iota^+$ it is compatible with the corner, the coordinates on $\mathscr I^+$ including $\rho_+$, so that
$\rho_+\circ\pi/\rho_+$ is smooth and positive. Then
$$P_\epsilon-\Big[P_0+\chi_I\tfrac12x_I^2\rho_+^2\big(2\tilde p^\epsilon_1A+p^\epsilon_0\big)\Big] = \theta_\epsilon
\tilde P+\chi_I\tfrac12x_I^2\rho_+^2\,\delta_\epsilon\big(2\tilde p_1A+p_0\big),\qquad\delta_\epsilon := \theta_\epsilon-
\theta_\epsilon|_{\mathscr I^+}\circ\pi,\tag{2.10}$$
with $A := x_I\partial_{x_I}-2\rho_+\partial_{\rho_+}$ and $\tilde P$ as in II.C (3.2). We show $\delta_\epsilon\in
x_I^{2\ell_I}C^\infty_b$ uniformly in $\epsilon$. Let $L := -\log t^\flat$ and $L_I := L|_{\mathscr I^+}\circ\pi$. With
$\varsigma_\vartheta := \epsilon^{-1}e^{L_I+\vartheta(L-L_I)}$,
$$\delta_\epsilon = \chi_0\big(\epsilon^{-1}e^{L_I}\big)-\chi_0\big(\epsilon^{-1}e^{L}\big) = -(L-L_I)\int_0^1\chi_0'(
\varsigma_\vartheta)\varsigma_\vartheta\,d\vartheta,$$
and the integral lies in $C^\infty_b$ uniformly in $\epsilon$, by the argument of (a). Near $\mathscr I^+$, $-L = \log
t_*+\log(1-(t_*/r)^{\ell_I})$; the second term is $(t_*/r)^{\ell_I}$ times an element of $C^\infty_b$, so it lies in
$x_I^{2\ell_I}C^\infty_b$. The first is $-\log\rho_+-\log(1-x_I^2)$ near $\mathscr I^+\cap\iota^+$ (by (1.1), $\rho_K =
1-x_I^2$) and a smooth function at finite times; so $\log t_*-(\log t_*)|_{\mathscr I^+}\circ\pi$ is smooth (as
$\log(\rho_+/\rho_+\circ\pi)$ is) and vanishes at $x_I = 0$, hence lies in $x_IC^\infty_b\subset
x_I^{2\ell_I}C^\infty_b$, as $2\ell_I\le1$. So $\delta_\epsilon\in x_I^{2\ell_I}C^\infty_b$ uniformly. $A$ is an
e3b-vector field near $\mathscr I^+$: it is a b-vector field tangent to the fibres of $\mathscr I^+$, the curves of
constant $\omega$ (II.A Definition 2.8). The extended $\tilde p_1$, $p_0$ lie in $\rho_+^{\ell_+}C^{(d_0;j)}_{e3b;b}$
near $\mathscr I^+$, b-regularity of order $j+d_0$ giving e3b-regularity of order $d_0$ and b-regularity of order $j$
(II.A Lemma 2.9), and $\chi_I$ is supported where $\rho_K$ is bounded below. By II.A Lemma 8.2 (c)-(d), the right side of
(2.10) lies in $x_I^2\rho_+^2C^{(d_0;j),(2\ell_I,\ell_+,\ell_K)}_{e3b;b}\mathrm{Diff}^2_{e3b}$, with a representation of
norm $\le C_j\|P-P_0\|_{(d_0;j)}$: (2) and (2.9). $\square$

Condition (3) of II.C Definition 3.3 may fail for $P_\epsilon$: the diagonal blocks of $S|_{\partial
X}+\theta_\epsilon\tilde p_1$ need not have real spectrum when those of $S|_{\partial X}$ and $S|_{\partial X}+\tilde
p_1$ do. By Lemma 2.1 (b) it is not used.

### 2.7 Cut-offs, slabs and the weights at late times

**Lemma 2.7.** (a) Let $T\ge2$, $\phi\in C^\infty_b$ with $\phi = 0$ on $\{t^\flat\ge T-1\}$, and $\mathsf t$, $\alpha$,
$\beta_+$, $\beta_K$ given. For $u$ in the slab space $H^{(\mathsf t;k),2\alpha}(\Omega_{1,T};E)^{\bullet,-}$, $\phi u$
(extended by 0 to $\{t^\flat\ge T\}$) lies in $H^{(\mathsf
t;k),(2\alpha,\beta_+,\beta_K)}_{e3b;b}(\Omega_*;E)^{\bullet,-}$, with norm at most $C\|u\|_{H^{(\mathsf
t;k),2\alpha}(\Omega_{1,T})^{\bullet,-}}$, $C$ depending on $T$, $\phi$ and the orders and weights.

(b) For $u\in H^{(\mathsf t;k),(2\alpha,\beta_+,\beta_K)}_{e3b;b}(\Omega_*;E)^{\bullet,-}$,
$\|u|_{\Omega_{1,T}}\|_{H^{(\mathsf t;k),2\alpha}(\Omega_{1,T})^{\bullet,-}}\le C_T\|u\|_{H^{(\mathsf
t;k),(2\alpha,\beta_+,\beta_K)}_{e3b;b}(\Omega_*)^{\bullet,-}}$.

(c) For $\eta\in(0,1]$ let $\chi_\eta := \chi_0(1/(\eta t^\flat))$ as in (2.8). Then $\|\chi_\eta v\|\le C\|v\|$ in each
of the spaces (2.2), and
$$\|\chi_\eta u\|_{Z(\mathsf t;k)}\le C_k\eta^{\delta'}\|u\|_{X(\mathsf t;k)},\tag{2.11}$$
with $C$, $C_k$ independent of $\eta$.

*Proof.* (a) Let $\tilde v$ extend $u$, supported in $\{t^\flat\ge1\}$, in $H^{(\mathsf t;k)}_{e3b;b}$ with the weight
$x_I^{2\alpha}$ only (II.E section 1.1). Then $\phi\tilde v$ is supported in $\{1\le t^\flat\le T-1\}$, where
$t_*\le(T-1)/C'$, so by (1.1) $\rho_+^{-\beta_+}\rho_K^{-\beta_K}\phi$ lies in $C^\infty_b$ and $\phi\tilde v$ lies in
the weighted space with norm $\le C\|\tilde v\|$. On $\{r>r_0\}$, $\phi\tilde v = \phi u$: the difference of $\tilde v$
and any extension of $u$ to $\Omega_*$ vanishes on $\{t^\flat<T,\ r>r_0\}$, and $\phi$ vanishes on a neighbourhood of
$\{t^\flat\ge T\}$. Take the infimum over $\tilde v$. (b) Multiply an extension by $\phi(t^\flat)$ equal to 1 on
$\{t^\flat\le T+1\}$ and 0 on $\{t^\flat\ge T+2\}$, as in Lemma 2.2. (c) The first claim is Lemma 2.6 (a). For (2.11):
with the weights (1.1), $\|v\|_{Z(\mathsf t;k)} = \|mv\|_{X(\mathsf t;k)}$ for $m :=
\rho_+^{\ell_+-\delta}\rho_K^{\ell_K-\aleph}$, as the weights of $Z$ and $X$ differ by these powers. On
$\mathrm{supp}\,\chi_\eta$, $t^\flat\ge\frac1{2\eta}$, and by (1.1), $\rho_+\rho_K = t_*^{-1}$,
$$m\chi_\eta = \eta^{\delta'}\cdot\rho_+^{\ell_+-\delta-\delta'}\rho_K^{\ell_K-\aleph-\delta'}\cdot(\eta t_*)^{-\delta'}
\chi_\eta.$$
The exponents are $\ge0$ by (2.1), so the middle factor is in $C^\infty_b$; and $(\eta t_*)^{-\delta'}\chi_\eta$ is in
$C^\infty_b$ uniformly in $\eta$: $\eta t_*\ge\eta t^\flat\ge\frac12$ on its support, $V(\eta t_*)^{-\delta'} =
-\delta'(\eta t_*)^{-\delta'}V\log t_*$ with $V\log t_*\in C^\infty_b$, and $\chi_\eta$ is as in Lemma 2.6 (a). $\square$

### 2.8 The tame bound for $P_\epsilon-P_0$ on $\Omega_*$

By II.C Definition 3.6 and II.A section 8.2, $P-P_0 = \chi_I\frac12x_I^2\rho_+^2(2\tilde p_1A+p_0)+\tilde P$ with $\tilde
P = x_I^2\rho_+^2\sum_qb_qQ_q$, $Q_q$ in a fixed finite subset of $\mathrm{Diff}^2_{e3b}$ and $b_q\in
C^{(d_0;j),(2\ell_I,\ell_+,\ell_K)}_{e3b;b}$. Dropping the factor $x_I^{2\ell_I}$ of the $b_q$ (bounded) and dividing by
$\rho_K^{\ell_K}$ on $\mathrm{supp}\,\chi_I$ (where $\rho_K$ is bounded below),
$$P_\epsilon-P_0 = x_I^2\rho_+^{2+\ell_+}\rho_K^{\ell_K}\sum_q(\theta_\epsilon a_q)Q'_q,\qquad\|\theta_\epsilon a_q
\|_{C^{(d_0;j)}_{e3b;b}}\le C_j\,e_j,\qquad e_j := \|P-P_0\|_{(d_0;j),(2\ell_I,\ell_+,\ell_K)},\tag{2.12}$$
with $Q'_q$ in a fixed finite subset of $C^\infty_b\mathrm{Diff}^2_{e3b}$ (the $Q_q$, $\chi_IA$ and $\chi_I$), $C_j$
independent of $\epsilon$ (II.A Lemma 8.2 (c), Lemma 2.6 (a)).

**Lemma 2.8.** Let $\mathsf t$ be an order function equal to an integer $m\ge2$ over $\Omega_\natural$. There are $d_0$
and $\tilde d$, depending only on $\mathsf t$, such that for all $k$, $\epsilon$ and $v\in Z(\mathsf t;k)$,
$$\|(P_\epsilon-P_0)v\|_{Y(\mathsf t-2;k)}\le C_k\big(e_{\tilde d}\|v\|_{Z(\mathsf t;k)}+e_k\|v\|_{Z(\mathsf t;\tilde d)}
\big),\qquad\|(P_\epsilon-P_0)v\|_{Y(\mathsf t-2;k)}\le C_ke_k\|v\|_{Z(\mathsf t;k)},\tag{2.13}$$
with $e_j$ of (2.12) and $C_k$ independent of $\epsilon$ and $P$.

*Proof.* Extend each $a_q$ across $\{r = r_0\}$ by Seeley's operator in $r-r_0$ (with $(t_*,\omega)$ as parameters),
which is bounded on $C^{(d_0;j)}_{e3b;b}$ for every $d_0$, $j$ at once (II.E Lemma 1.2 (ii) and Lemma 4.1 (a)'s proof),
and multiply by $\psi_\Omega\in C^\infty_b$ equal to 1 near $\{t^\flat\ge1,\ r\ge r_0-2\kappa\}$ and supported in
$\{t_*>\frac12,\ r>r^\sharp\}$; call the result $a^\sharp_q$, and $A^\sharp :=
x_I^2\rho_+^{2+\ell_+}\rho_K^{\ell_K}\sum_q(\theta_\epsilon a^\sharp_q)Q'_q$, an operator on $\tilde M$. With $E$ of
Lemma 2.5 for the weights of $Z$, $A^\sharp Ev$ is supported in $\{t^\flat\ge1\}$ and equals $(P_\epsilon-P_0)v$ on
$\{r>r_0\}$, so it is an extension of it. The weight $x_I^2\rho_+^{2+\ell_+}\rho_K^{\ell_K}$ takes the weights
$(2\alpha_I,\alpha_+-\ell_+,-\ell_K)$ of $Z$ to $(2\alpha_I+2,\alpha_++2,0)$, those of $Y$. II.A Corollary 9.7, on
$\tilde M$ with $\chi' = \chi = 1$ and on weighted spaces (II.A, after (8.1)), with $d_0$, $\tilde d$ of II.A Proposition
9.6 for the orders $\mathsf t-2$, gives
$$\|A^\sharp Ev\|_{(\mathsf t-2;k)}\le C_k\big(\max_q\|\theta_\epsilon a^\sharp_q\|_{(d_0;\tilde d)}\|Ev\|_{(
\mathsf t;k)}+\max_q\|\theta_\epsilon a^\sharp_q\|_{(d_0;k)}\|Ev\|_{(\mathsf t;\tilde d)}\big),$$
the norms of $Ev$ with the weights of $Z$. By (2.7) at $j = k$ and $j = \tilde d$ and (2.12), this is the first bound of
(2.13). The second is the same with II.A Lemma 8.6 (a) in place of Corollary 9.7 (no tame structure being needed, any
extension of $v$ may be used). $\square$

### 2.9 Forward solutions of $P_\epsilon$

**Lemma 2.9.** Let $k\in\mathbb N_0$, $\epsilon\in(0,1]$ and $f\in Y(\mathsf s;k)$, and let $P$ be admissible, of class
$((d_0;k),(2\ell_I,\ell_+,\ell_K))$ with $\|P-P_0\|_{(d_0;d)}$ below the threshold of II.E Proposition 4.4 for the slab
order $\mathsf s+1$ ($d_0$, $d$ being its constants; by (2.9) the same then holds for $P_\epsilon$). There is
$u_\epsilon\in X(\mathsf s;k)$ with $P_\epsilon u_\epsilon = f$; by Lemma 2.2 it is the forward solution.

*Proof.* Let $T := 4/\epsilon$ and $\chi' := \chi_{\epsilon/4} = \chi_0(4/(\epsilon t^\flat))$, which is 0 on
$\{t^\flat\le\frac2\epsilon\}$ and 1 on $\{t^\flat\ge\frac8{3\epsilon}\}$. By Lemma 2.7 (b), $f|_{\Omega_{1,T}}\in
H^{(\mathsf s;k),2\alpha_I+2}(\Omega_{1,T})^{\bullet,-}$. By II.E Proposition 4.4 for $P_\epsilon$ at the slab order
$\mathsf s+1$ (Lemma 2.3 (c), Lemma 2.6 (b); its smallness condition is on $\|P_\epsilon-P_0\|_{(d_0;d)}$ only), the
forward solution $u_{\mathrm{ini}}$ of $P_\epsilon u_{\mathrm{ini}} = f$ on $\Omega_{1,T}$ lies in $H^{(\mathsf
s+1;k),2\alpha_I}(\Omega_{1,T})^{\bullet,-}$. As $1-\chi' = 0$ on $\{t^\flat\ge T-1\}$, Lemma 2.7 (a) puts
$(1-\chi')u_{\mathrm{ini}}$ in $H^{(\mathsf
s+1;k),(2\alpha_I,\alpha_+-\delta,-\aleph)}_{e3b;b}(\Omega_*)^{\bullet,-}\subset X(\mathsf s;k)$. The commutator
$[P_0,\chi'] = x_I^2\rho_+^2[L_0,\chi']$ ($L_0 := x_I^{-2}\rho_+^{-2}P_0\in\mathrm{Diff}^2_{e3b}$ on $\Omega$, II.C Lemma
1.4 (b)) is a first-order e3b-operator whose coefficients are e3b-derivatives of $\chi'$, in $C^\infty_b$ and supported
in $\{\frac2\epsilon\le t^\flat\le\frac8{3\epsilon}\}$; by Lemma 2.7 (a) (with $\phi$ equal to 1 there and 0 on
$\{t^\flat\ge T-1\}$),
$$g := \chi'f+[P_0,\chi']u_{\mathrm{ini}}\in Y(\mathsf s;k),\qquad\mathrm{supp}\,g\subset\{t^\flat\ge\tfrac2\epsilon\}.$$
By II.F Theorem 8.1 at the order $\mathsf s$ (Lemma 2.3 (b)), the forward solution $v$ of $P_0v = g$ on $\Omega_*$ lies
in $X(\mathsf s;k)$. On the slab $\Omega_{1,2/\epsilon}$, $P_0v = g = 0$, so $v = 0$ on $\{t^\flat<\frac2\epsilon\}$ by
Lemma 2.2. As $P_\epsilon-P_0 = \theta_\epsilon(P-P_0)$ has coefficients vanishing on the open set
$\{t^\flat>\frac2{3\epsilon}\}$, which contains $\mathrm{supp}\,v$, $P_\epsilon v = P_0v = g$. On $\{t^\flat<T\}$,
$P_\epsilon u_{\mathrm{ini}} = f$, and $[P_\epsilon,\chi'] = [P_0,\chi']$ as
$\mathrm{supp}\,d\chi'\subset\{t^\flat>\frac2{3\epsilon}\}$; so
$$P_\epsilon\big((1-\chi')u_{\mathrm{ini}}\big) = (1-\chi')f-[P_0,\chi']u_{\mathrm{ini}},$$
and $u_\epsilon := (1-\chi')u_{\mathrm{ini}}+v\in X(\mathsf s;k)$ satisfies $P_\epsilon u_\epsilon = f$. $\square$

## 3. Small b-regularity orders ([Hin26c] Step 1 of the proof of Theorem 11.1)

### 3.1 The constants

b-regularity controls e3b-regularity: as $\mathrm{Diff}^{d_0}_{e3b}\subset C^\infty(\tilde M)\mathrm{Diff}^{d_0}_b$
(II.A Lemma 2.9) and by II.A Lemma 8.2 (a), $\|a\|_{C^{(d_0;j)}_{e3b;b}}\le C\|a\|_{C^{(0;j+d_0)}_{e3b;b}}$, with
weights; the data $p_0$, $\tilde p_1$ carry $j+d_0$ b-derivatives in both classes. Hence, for $P$ of class
$((0;j+d_0),\cdot)$,
$$e_j = \|P-P_0\|_{(d_0;j),(2\ell_I,\ell_+,\ell_K)}\le C\|P-P_0\|_{(0;j+d_0),(2\ell_I,\ell_+,\ell_K)}.\tag{3.1}$$
Let $d^E_0$, $d^E$ be the $d_0$ and $d$ of II.E Theorem 6.1 for $(\mathsf s_0,\mathsf s)$ at the weights
$\alpha_+-\delta$, $-\aleph$; $d^S_0$, $d^S$ the largest of those of II.E Propositions 3.4, 4.3 and 4.4 for the slab
orders $\mathsf s$ and $\mathsf s+1$; $d^T_0$, $\tilde d$ those of Lemma 2.8 for $\mathsf t = \mathsf s$; and $d^U_0$
the $d_0$ of II.E Proposition 3.4 (i) at $s' = s_{\mathrm u} := \inf\mathsf s-2$. Put
$$D_0 := \max(d^E_0,d^S_0,d^T_0,d^U_0),\qquad D_1 := \max(d^E,d^S,\tilde d),\qquad e_j := \|P-P_0\|_{(D_0;j),
(2\ell_I,\ell_+,\ell_K)},\tag{3.2}$$
$$d := D_0+D_1+d'+d'',\qquad d' := \max(0,\lceil-\inf\mathsf s\rceil),\qquad d'' := s_{\mathrm{in}}\ (= \max(0,\lceil\sup
\mathsf s\rceil)).\tag{3.3}$$
Choose $\epsilon_0>0$ so small that $\|P-P_0\|_{(0;d)}<\epsilon_0$ makes $e_j$, $j\le D_1$, and hence (by (2.9)) the
corresponding norms of every $P_\epsilon$, smaller than the thresholds of Lemma 2.1, of II.C Lemma 3.2 (through II.C
Lemma 3.7), of II.E Theorem 6.1 at $k\le D_1$ and at $d^E$, of II.E Propositions 3.4, 4.3 at $k\le D_1$ and 4.4 at
$d^S$, and of II.E Proposition 3.4 (i) at $s' = s_{\mathrm u}$ (Lemma 2.2). Then $e_{D_1}\le C\epsilon_0\le1$ for every
such $P$. All constants below depend on $P$ only through $\epsilon_0$, unless $e_k$ appears explicitly.

### 3.2 The uniform a priori estimate

**Proposition 3.1 ([Hin26c] (11.15)).** For every $k\le D_1$ there are $\eta_k\in(0,1]$ and $C_k$ such that for every
$\epsilon\in(0,\eta_k/8]$ and every $u\in X(\mathsf s;k)$ with $P_\epsilon u\in Y(\mathsf s;k)$,
$$\|u\|_{X(\mathsf s;k)}\le C_k\|P_\epsilon u\|_{Y(\mathsf s;k)}.\tag{3.4}$$

*Proof.* *(i) The global estimate.* By II.E Theorem 6.1, (6.1), for $P_\epsilon$ at the weights $\alpha_+-\delta$,
$-\aleph$ with the orders $\mathsf s_0<\mathsf s$ (Lemma 2.3 (a); Lemmas 2.1 and 2.6 (b) for the hypotheses on
$P_\epsilon$; [Hin26c] (11.10)),
$$\|u\|_{X(\mathsf s;k)}\le C_k\big(\|P_\epsilon u\|_{Y'(\mathsf s;k)}+\|u\|_{X(\mathsf s_0;k)}\big)\le C_k\big(
\|P_\epsilon u\|_{Y(\mathsf s;k)}+\|u\|_{X(\mathsf s_0;k)}\big).\tag{3.5}$$

*(ii) Inversion of $P_0$.* By Lemma 2.8, second bound of (2.13) with $\mathsf t = \mathsf s$, $(P_\epsilon-P_0)u\in
Y(\mathsf s_0;k)$, as $u\in X(\mathsf s;k)\subset Z(\mathsf s;k)$ and $\mathsf s-2 = \mathsf s_0$. So $P_0u = P_\epsilon
u-(P_\epsilon-P_0)u\in Y(\mathsf s_0;k)$. Let $v$ be the forward solution of $P_0v = P_0u$ given by II.F Theorem 8.1 at
the order $\mathsf s_0$ (Lemma 2.3 (b)); $u-v\in X(\mathsf s_0;k)$ and $P_0(u-v) = 0$, so $u = v$ by Lemma 2.2, and
([Hin26c] (11.11))
$$\|u\|_{X(\mathsf s_0;k)}\le C_k\|P_0u\|_{Y(\mathsf s_0;k)}\le C_k\big(\|P_\epsilon u\|_{Y(\mathsf s;k)}+
\|(P_\epsilon-P_0)u\|_{Y(\mathsf s_0;k)}\big).\tag{3.6}$$

*(iii) The error near $\iota^+\cup K^+$.* With $\chi_\eta$ of Lemma 2.7 (c), by (2.13) and (2.11) ([Hin26c]
(11.13)-(11.14)),
$$\|(P_\epsilon-P_0)\chi_\eta u\|_{Y(\mathsf s_0;k)}\le C_ke_k\|\chi_\eta u\|_{Z(\mathsf s;k)}\le C^{(1)}_k\epsilon_0
\eta^{\delta'}\|u\|_{X(\mathsf s;k)},\tag{3.7}$$
with $C^{(1)}_k$ independent of $\eta$ and $\epsilon$.

*(iv) The error at bounded times.* Let $T_\eta := 2/\eta$. $1-\chi_\eta$ vanishes on
$\{t^\flat\ge\frac2{3\eta}\}\supset\{t^\flat\ge T_\eta-1\}$. For $\epsilon\le\eta/8$,
$\frac1{2\epsilon}\ge\frac4\eta>T_\eta$, so $P_\epsilon = P$ on $\Omega_{1,T_\eta}$ (Lemma 2.6 (a)), and
$u|_{\Omega_{1,T_\eta}}$, which lies in the slab space by Lemma 2.7 (b), is the forward solution of $Pu = P_\epsilon u$
there (Lemma 2.2). By (2.13), Lemma 2.7 (a), II.E Proposition 4.3 for $P$ at the slab order $\mathsf s$ ([Hin26c]
Proposition 8.6) and Lemma 2.7 (b),
$$\|(P_\epsilon-P_0)(1-\chi_\eta)u\|_{Y(\mathsf s_0;k)}\le C_k\|(1-\chi_\eta)u\|_{Z(\mathsf s;k)}\le C_{k,\eta}\|u
\|_{H^{(\mathsf s;k),2\alpha_I}(\Omega_{1,T_\eta})}\le C_{k,\eta}\|P_\epsilon u\|_{Y(\mathsf s;k)}.\tag{3.8}$$

*(v) Absorption.* Inserting (3.6)-(3.8) in (3.5),
$$\|u\|_{X(\mathsf s;k)}\le C^{(2)}_k\epsilon_0\eta^{\delta'}\|u\|_{X(\mathsf s;k)}+C_{k,\eta}\|P_\epsilon u\|_{Y(
\mathsf s;k)},$$
$C^{(2)}_k$ independent of $\eta$. Fix $\eta_k\in(0,1]$ with $C^{(2)}_k\epsilon_0\eta_k^{\delta'}\le\frac12$. As
$\|u\|_{X(\mathsf s;k)}<\infty$, it is absorbed. $\square$

### 3.3 The forward solution at small orders

**Proposition 3.2 ([Hin26c] (11.16)-(11.17)).** Let $k\le D_1$ and $f\in Y(\mathsf s;k)$. The forward solution $u$ of $Pu
= f$ exists, lies in $X(\mathsf s;k)$, and $\|u\|_{X(\mathsf s;k)}\le C_k\|f\|_{Y(\mathsf s;k)}$.

*Proof.* For $\epsilon\in(0,\eta_k/8]$ let $u_\epsilon\in X(\mathsf s;k)$ be the forward solution of $P_\epsilon
u_\epsilon = f$ (Lemma 2.9). By (3.4), $\|u_\epsilon\|_{X(\mathsf s;k)}\le C_k\|f\|_{Y(\mathsf s;k)}$. $X(\mathsf s;k)$
is a Hilbert space (section 2), so a sequence $u_{\epsilon_j}$, $\epsilon_j\downarrow0$, converges weakly to some $u\in
X(\mathsf s;k)$, and $\|u\|\le C_k\|f\|$ (weak lower semicontinuity of the Hilbert norm, equivalent to the norm used).
For $\varphi\in C^\infty_c(M^\circ\cap\{r>r_0\})$, $w\mapsto\langle w,\varphi\rangle$ is continuous on $X(\mathsf s;k)$
(pair any extension with $\varphi$; the result does not depend on the extension, II.A Lemma 7.3).
$\mathrm{supp}\,\varphi$ is compact in $M^\circ$, so $t^\flat$ is bounded on it, and $P_{\epsilon_j}^*\varphi =
P^*\varphi$ for $j$ large (Lemma 2.6 (a)), $P^*$ the formal adjoint, whose coefficients involve at most two derivatives
of those of $P$ ($d\ge2$). Hence
$$\langle u,P^*\varphi\rangle = \lim_j\langle u_{\epsilon_j},P^*_{\epsilon_j}\varphi\rangle = \lim_j\langle P_{
\epsilon_j}u_{\epsilon_j},\varphi\rangle = \langle f,\varphi\rangle,$$
so $Pu = f$ on $\{r>r_0\}$, both sides supported in $\{t^\flat\ge1\}$. By Lemma 2.2, $u$ is the forward solution.
$\square$

## 4. Large b-regularity orders and the tame estimate ([Hin26c] Step 2)

**Proposition 4.1 ([Hin26c] (11.19)).** For every $k\in\mathbb N_0$ there are $\eta_k\in(0,1]$ and $C_k$ such that for
every $\epsilon\in(0,\min(\eta_k,\eta_{D_1})/8]$, every $P$ as in Theorem 1.1 and every $u\in X(\mathsf s;k)$ with
$P_\epsilon u\in Y(\mathsf s;k)$,
$$\|u\|_{X(\mathsf s;k)}\le C_k\big(\|P_\epsilon u\|_{Y(\mathsf s;k)}+e_k\|P_\epsilon u\|_{Y(\mathsf s;D_1)}\big),
\tag{4.1}$$
with $e_k$ of (3.2).

*Proof.* For $k\le D_1$ this is (3.4). Let $k>D_1$, and write $A_j := \|u\|_{X(\mathsf s;j)}$, $B_j := \|P_\epsilon
u\|_{Y(\mathsf s;j)}$; $A_k$, $B_k$ are finite. By Proposition 3.1 at $D_1$ (as $\epsilon\le\eta_{D_1}/8$), $A_j\le
A_{D_1}\le CB_{D_1}$ for $j\le D_1$.

*(i) The tame global estimate.* By II.E Theorem 6.1, (6.2), for $P_\epsilon$ (its $d = d^E\le D_1$, and
$\|P_\epsilon-P_0\|_{(d^E_0;d^E)}$ small), with (2.9) and $\|\cdot\|_{Y'}\le C\|\cdot\|_Y$,
$$A_k\le C_k\big(B_k+\|u\|_{X(\mathsf s_0;k)}+e_k(B_{D_1}+A_{D_1})\big)\le C_k\big(B_k+\|u\|_{X(
\mathsf s_0;k)}+e_kB_{D_1}\big).\tag{4.2}$$

*(ii) Inversion of $P_0$.* As in Proposition 3.1 (ii), $\|u\|_{X(\mathsf s_0;k)}\le
C_k(B_k+\|(P_\epsilon-P_0)u\|_{Y(\mathsf s_0;k)})$.

*(iii) The error, tamely.* With $\chi_\eta$ of Lemma 2.7 (c), the first bound of (2.13) (with $e_{\tilde d}\le e_{D_1}\le
C\epsilon_0$) and (2.11),
$$\|(P_\epsilon-P_0)\chi_\eta u\|_{Y(\mathsf s_0;k)}\le C_k\big(\epsilon_0\eta^{\delta'}A_k+e_k\|\chi_\eta u\|_{Z(
\mathsf s;\tilde d)}\big)\le C^{(1)}_k\epsilon_0\eta^{\delta'}A_k+C_ke_kB_{D_1},$$
using $\|\chi_\eta u\|_{Z(\mathsf s;\tilde d)}\le CA_{\tilde d}\le CB_{D_1}$. With $T_\eta := 2/\eta$ as in Proposition
3.1 (iv), and II.E Proposition 4.4 for $P$ on $\Omega_{1,T_\eta}$ ([Hin26c] Proposition 8.9) in place of Proposition 4.3,
$$\|(1-\chi_\eta)u\|_{Z(\mathsf s;j)}\le C_{j,\eta}\|u\|_{H^{(\mathsf s;j),2\alpha_I}(\Omega_{1,T_\eta})}\le C_{j,\eta}
\big(B_j+e_jB_{D_1}\big)$$
for every $j$ (Lemma 2.7, and $\|P_\epsilon u\|_{H^{(\mathsf s-1;d^S),2\alpha_I+2}(\Omega_{1,T_\eta})}\le CB_{D_1}$); so,
by (2.13),
$$\|(P_\epsilon-P_0)(1-\chi_\eta)u\|_{Y(\mathsf s_0;k)}\le C_k\big(\epsilon_0\|(1-\chi_\eta)u\|_{Z(\mathsf s;k)}+e_k\|(1-
\chi_\eta)u\|_{Z(\mathsf s;\tilde d)}\big)\le C_{k,\eta}\big(B_k+e_kB_{D_1}\big).$$

*(iv) Absorption.* Collecting,
$$A_k\le C^{(2)}_k\epsilon_0\eta^{\delta'}A_k+C_{k,\eta}\big(B_k+e_kB_{D_1}\big),$$
with $C^{(2)}_k$ independent of $\eta$; fix $\eta_k$ with $C^{(2)}_k\epsilon_0\eta_k^{\delta'}\le\frac12$ and absorb.
$\square$

**Proposition 4.2.** For every $k\in\mathbb N_0$, every $P$ as in Theorem 1.1 and every $f\in Y(\mathsf s;k)$, the
forward solution $u$ of $Pu = f$ lies in $X(\mathsf s;k)$, and
$$\|u\|_{X(\mathsf s;k)}\le C_k\big(\|f\|_{Y(\mathsf s;k)}+e_k\|f\|_{Y(\mathsf s;D_1)}\big).\tag{4.3}$$

*Proof.* As Proposition 3.2, with Lemma 2.9 at the level $k$ (which needs only the smallness of
$\|P_\epsilon-P_0\|_{(d^S_0;d^S)}$) and (4.1) for $\epsilon\le\min(\eta_k,\eta_{D_1})/8$; the right side of (4.1) with
$P_\epsilon u_\epsilon = f$ does not depend on $\epsilon$. $\square$

## 5. Pure b-estimates, and the proofs of Theorem 1.1 and Corollary 1.2 ([Hin26c] Step 3)

*The embeddings.* By II.A Lemma 8.7, with weights, $H^{(\mathsf s;j+d')}_{e3b;b}\subset H^j_b$, $d' =
\max(0,\lceil-\inf\mathsf s\rceil)$. By II.A Lemma 8.4 (d), applied $d''$ times, and $\mathsf s\le s_{\mathrm{in}} =
d''$, $H^{j+d''}_b = H^{(0;j+d'')}_{e3b;b}\subset H^{(d'';j)}_{e3b;b}\subset H^{(\mathsf s;j)}_{e3b;b}$, with weights.
Both inclusions preserve supports, so they hold for the spaces $(\Omega_*)^{\bullet,-}$ with the same constants (an
extension in the smaller space is one in the larger). With (1.2),
$$\|u\|_{H^{k,(\alpha_I,\alpha_+-\delta,-\aleph)}_b(\Omega_*)}\le C\|u\|_{X(\mathsf s;k+d')},\qquad\|f\|_{Y(\mathsf s;j)}
\le C\|f\|_{H^{j+d'',(\alpha_I+1,\alpha_++2,0)}_b(\Omega_*)}.\tag{5.1}$$

*Proof of Theorem 1.1.* Let $\epsilon_0$, $d$ be as in (3.3) and section 3.1, $k\in\mathbb N_0$, $P$ and $f$ as in the
theorem. By (5.1), $f\in Y(\mathsf s;k+d')$, as $k+d'+d''\le k+d$. By Proposition 4.2 at the level $k+d'$ (for which $P$
is of class $((D_0;k+d'),\cdot)$, as $k+d'+D_0\le k+d$), the forward solution $u$ lies in $X(\mathsf s;k+d')$ and
$$\|u\|_{H^{k,(\alpha_I,\alpha_+-\delta,-\aleph)}_b}\le C\|u\|_{X(\mathsf s;k+d')}\le C_k\big(\|f\|_{Y(
\mathsf s;k+d')}+e_{k+d'}\|f\|_{Y(\mathsf s;D_1)}\big)\le C_k\big(\|f\|_{H^{k+d}_b}+\|P-P_0\|_{(0;k+d)}\|f\|_{H^d_b}
\big),$$
the b-norms with the weights of (1.5), by (5.1) ($D_1+d''\le d$) and (3.1) ($k+d'+D_0\le k+d$). Uniqueness in the stated
class is Lemma 2.2 at $s' = s_{\mathrm u}$, whose smallness is among those fixing $\epsilon_0$ (section 3.1): an element
of the class lies in the space with $s' = s_{\mathrm u}$, and $P$, of class $((d^U_0;0),\cdot)$ by (3.1) as $k+d\ge
D_0\ge d^U_0$, acts on it as II.E Proposition 3.4 (i) at $s' = s_{\mathrm u}$ requires (D213). Below $s_{\mathrm u}$ the
smallness of II.E Proposition 3.4 (i), whose $d_0$ depends on $s'$, is not implied by that of $\|P-P_0\|_{(0;d)}$, and
$Pu$ need not be defined; the source's "the unique forward solution" names no class (D212: the eighty-eighth verifier's
Major 1). The continuity is section 6. $\square$

*Proof of Corollary 1.2.* By II.A Lemma 8.8's proof, $|dt\,dx| = c\,x_I^{-8}\rho_+^{-5}\rho_K^{-1}\mu_b$ near $\Omega$
with $c$ smooth and positive, so $L^2(|dt\,dx|) = \rho_I^2\rho_+^{5/2}\rho_K^{1/2}L^2(\mu_b)$ and
$H^{k,(a_I,a_+,a_K)}_b(|dt\,dx|) = H^{k,(a_I+2,a_++\frac52,a_K+\frac12)}_b(\mu_b)$ with equivalent norms (b-derivatives
of the weights being the weights times smooth functions). This turns (1.5) into (1.7); $\alpha_I<-\frac12+\bar S$ is
$b_I<\frac32+\bar S$, and $\alpha_+<\alpha_I-\frac12$ is $b_+<b_I$. Writing out the norms with the frame
$t_*\partial_{t_*}$, $r\partial_x$ of $\mathcal V_b$ on $\Omega$, and $\langle x\rangle\sim r$ on $\Omega$, gives the
integrals. (1.8) is II.A Lemma 8.8, (8.2), with $d = k-3$, applied to an extension of $u$ and restricted to $\{r>r_0\}$:
its left side is the $C^{k-3}_b$-norm with the weight
$x_I^{2(\alpha_I+2)}\rho_+^{\alpha_+-\delta+\frac52}\rho_K^{-\aleph+\frac12} =
\rho_I^{b_I}\rho_+^{b_+-\delta}\rho_K^{-\aleph+\frac12}$. $\square$

## 6. Continuous dependence ([Hin26c] Step 4)

**Lemma 6.1 (compactness).** Let $k\ge1$, $w = (\alpha_I,\alpha_+,\alpha_K)$, $\varsigma>0$ and $w' :=
(\alpha_I-\varsigma,\alpha_+-\varsigma,\alpha_K-\varsigma)$. The inclusion
$H^{k,w}_b(\Omega_*;E)^{\bullet,-}\hookrightarrow H^{k-1,w'}_b(\Omega_*;E)^{\bullet,-}$ is compact.

*Proof.* Extend $w$ to the other boundary hypersurfaces of $\tilde M$ by the exponent 0, and let $w''$ be $w$ lowered by
$\varsigma$ at every boundary hypersurface; near $\mathscr I^+\cup\iota^+\cup K^+$ it is $w'$. The b-Sobolev spaces are
those of the b.g. structure of b-vector fields on $\tilde M^\circ$, with the weights $\rho^w$ as weight functions, and
$\rho^w/\rho^{w''} = \rho_{\mathrm{tot}}^{\varsigma}\to0$ at infinity ($\rho_{\mathrm{tot}}$ a total boundary defining
function); so $H^{k,w}_b(\tilde M)\hookrightarrow H^{k-1,w''}_b(\tilde M)$ is compact by (S3). Given a bounded sequence
$u_j$ in $H^{k,w}_b(\Omega_*)^{\bullet,-}$, take extensions $\tilde u_j$ supported in $\{t^\flat\ge1\}$ with $\|\tilde
u_j\|\le2\|u_j\|$. A subsequence converges in $H^{k-1,w''}_b(\tilde M)$. The closure of $\{t^\flat\ge1\}$ meets
$\partial\tilde M$ only in $\mathscr I^+\cup\iota^+\cup K^+$ (II.E section 1.1); multiplying by a cut-off in $C^\infty_b$
equal to 1 near $\{t^\flat\ge1,\ r\ge r_0\}$ and supported where $w'' = w'$, the restrictions converge in
$H^{k-1,w'}_b(\Omega_*)^{\bullet,-}$. $\square$

*Proof of the continuity in Theorem 1.1.* Let $P^{(j)}\to P$ and $f^{(j)}\to f$ in the stated norms, with
$\|P^{(j)}-P_0\|_{(0;d)}<\epsilon_0$, and let $u^{(j)}$, $u$ be the forward solutions. By (1.5), uniformly in $j$ as its
constant does not depend on the operator and $\|P^{(j)}-P_0\|_{(0;k+d)}$ is bounded, the $u^{(j)}$ are bounded in the
Hilbert space $H^{k,(\alpha_I,\alpha_+-\delta,-\aleph)}_b(\Omega_*)^{\bullet,-}$. Let $\tilde u$ be the weak limit of a
subsequence. For $\varphi\in C^\infty_c(M^\circ\cap\{r>r_0\})$, $P^{(j)*}\varphi\to P^*\varphi$ in $L^2$, as the
coefficients converge in $C^2$ on $\mathrm{supp}\,\varphi$ ($k+d\ge2$), and the $u^{(j)}$ are bounded in $L^2$ there; so
$\langle\tilde u,P^*\varphi\rangle = \lim\langle u^{(j)},P^{(j)*}\varphi\rangle = \lim\langle f^{(j)},\varphi\rangle =
\langle f,\varphi\rangle$, and $P\tilde u = f$. As $\tilde u\in H^{k}_b\subset H^{0,(2\alpha_I,\cdot,\cdot)}_{e3b}$,
Lemma 2.2 gives $\tilde u = u$. Every subsequence having a further subsequence converging weakly to $u$,
$u^{(j)}\rightharpoonup u$; by Lemma 6.1, a weakly convergent sequence converges in norm in
$H^{k-1,(\alpha_I-\varsigma,\alpha_+-\delta-\varsigma,-\aleph-\varsigma)}_b$ (each subsequence has a norm-convergent
subsequence, whose limit is the weak limit $u$). $\square$

## 7. Remarks 11.2-11.4 at $n = 4$

**Remark 7.1 ([Hin26c] Remark 11.2; relaxed $\aleph$-admissibility).** Let $P_0$ be $\aleph$-admissible with margin
$d_\aleph\ge0$ (the relaxed version after II.C Definition 2.7). Then Theorem 1.1 holds with $d$ increased by $\lceil
d_\aleph\rceil$. Indeed, take $\mathsf s$ as in Lemma 2.3 with the margin $m_0+2d_\aleph$ and $\mathsf s_0 := \mathsf
s-2-d_\aleph$. The margins of section 2.3 (with $m_0+2d_\aleph$ for $m_0$) show: $\mathsf s_0<\mathsf s$ meet the
hypotheses of II.E Theorem 6.1; $\mathsf s-2 = \mathsf s_0+d_\aleph$ is admissible with weights $\alpha_+$, $-\aleph$ and
margin $d_\aleph$ and with weights $\alpha_+$, 0 and margin $1+d_\aleph$, so II.F Remark 8.2 gives $\|u\|_{X(\mathsf
s_0;k)}\le C\|P_0u\|_{Y(\mathsf s-2;k)}$, which replaces (3.6), the error $(P_\epsilon-P_0)u$ lying in $Y(\mathsf s-2;k)$
by (2.13); and $\mathsf s+d_\aleph$ is admissible with the same two pairs of weights and margins $d_\aleph$, $1+d_\aleph$
(its upper margin at $R_{\mathrm{out}}$ with weights $\alpha_+$, 0 being
$m_0+2d_\aleph-d_\aleph-\delta+\aleph\ge1+d_\aleph$), so Lemma 2.9 holds for $f\in Y(\mathsf s+d_\aleph;k)$, with
$u_{\mathrm{ini}}$ of order $\mathsf s+d_\aleph+1$ and $v\in X(\mathsf s;k)$ by II.F Remark 8.2. The absorption in
Proposition 3.1 is unchanged, as $\mathsf s_0+d_\aleph+2 = \mathsf s$. In section 5, $f\in Y(\mathsf s+d_\aleph;k+d')$
needs $k+d'+d''+\lceil d_\aleph\rceil\le k+d$. The source raises the margin by $d_\aleph$ and passes over the existence
step (Lemma 2.9 here, its (11.16)), where Theorem 10.1 loses $d_\aleph$ (section 8, (F'8)).

**Remark 7.2 ([Hin26c] Remark 11.3).** The absorption in Propositions 3.1 and 4.1 uses that II.E Theorem 6.1 is lossless
in the b-regularity: both $u$ and $P_\epsilon u$ carry $k$ b-derivatives. If it needed $k+1$ on $P_\epsilon u$, the error
$(P_\epsilon-P_0)\chi_\eta u$ would be needed in $Y(\mathsf s_0;k+1)$, which (2.13) bounds by $u$ in $Z(\mathsf s;k+1)$,
and (3.7) could not be absorbed. Once (1.5) holds, b-regularity alone describes the solution, which is how the later
sections of the source use it.

**Remark 7.3 ([Hin26c] Remark 11.4 at $n = 4$).** (1.3) gives $\alpha_+<\alpha_I-\frac12<-1+\bar S$, and tf-admissibility
puts $\alpha_++2$ in the indicial gap $(\beta_-,\beta_+)$ of $\hat P_0(0)$ (II.C Definition 2.7 (2); at $n = 3$ the
source has $\alpha_++\frac32$). So Theorem 1.1 requires $\beta_-<\alpha_++2<1+\bar S$, in particular $\beta_-<1+\bar S$
(the source's $\beta_-<\frac12+\bar S$). For the scalar wave operator, $S = 0$ and the gap is $(0,2)$ (II.C section 2.4),
so $\alpha_+\in(-2,-1)$ and $\alpha_I\in(\alpha_++\frac12,-\frac12)$: $\alpha_I = -\frac12-\epsilon_I$, $\alpha_+ =
-1-\epsilon_+$ with $0<\epsilon_I<\epsilon_+<1$. (The source's (12.7) at $n = 3$ prints
$0<\epsilon_+<\epsilon_I<\frac12$, which contradicts $\alpha_+<\alpha_I-\frac12$; with $\alpha_I = -\frac12-\epsilon_I$
and $\alpha_+ = -1-\epsilon_+$ the condition is $\epsilon_+>\epsilon_I$. This belongs to [Hin26c] section 12 and is
recorded for Part II.G.)

## 8. Findings, and the sources

### 8.1 Findings against the source

Each item records a place where [Hin26c] section 11, read at $n = 4$, prints something other than what its argument gives
or needs. None changes the statement of Theorem 11.1 except (F'9)-(F'11), which concern what is proved here.

(F'1) *The margin.* The proof takes $\mathsf s$ admissible with weights $\alpha_+-\delta$, $-\aleph$ and margin
$2+\delta+\max(1,\aleph)$, and $\mathsf s_0 := \mathsf s-2$, and footnote 91 states that margin $\max(1,\aleph)$ with
weights $\alpha_+$, $-\aleph$ gives the hypotheses of Theorem 10.1. The incoming threshold at $\partial K^+$, $\mathsf
s+\alpha_{\mathrm{sf}}>\frac12(-1+\vartheta^{3b}_{\mathrm{in}})+\alpha_K+\eta$, loses $\aleph$ of its margin when
$\alpha_K$ passes from $-\aleph$ to 0, so the margin with weights $\alpha_+$, 0 is $\max(1,\aleph)-\aleph+2\delta$, less
than the required 1 when $\aleph\ge1$ and $\delta<\frac12$. Margin $3+\delta+\aleph$ suffices (Lemma 2.3).

(F'2) *The weight at $\iota^+$ of $P_0u$.* (11.11), (11.13), (11.15) and (11.17) print the weight $\alpha_+$ at $\iota^+$
on $P_0u$, $(P_\epsilon-P_0)u$, $P_\epsilon u$ and $f$; Theorem 10.1, the mapping property of $P_\epsilon-P_0$ (which
gains $\rho_+^{2+\ell_+}$ on $u$ with the weight $\alpha_+-\ell_+$) and (11.2) give $\alpha_++2$, which (11.19) prints in
its first term and not in its second.

(F'3) (11.16) prints $u_\epsilon\in H^{(\mathsf s;k),(2\alpha_I,\alpha_+-\delta,\aleph)}$; the weight at $K^+$ is
$-\aleph$.

(F'4) *Cut-offs in $t_*$.* The source's $\chi_\epsilon = \chi_0(1/(\epsilon t_*))$ and the identity $u_\epsilon =
(1-\chi_{\epsilon/2})u^\epsilon_{\mathrm{ini}}+P_0^{-1}(\cdots)$ need $P_\epsilon = P_0$ on the support of the second
term. That support is controlled by uniqueness on the slabs, whose faces are level sets of $t^\flat$, not of $t_*$
($t^\flat\ge C't_*$ only), and $\chi_0 = 1$ only on $[0,1]$ leaves no room at the edge. Here the cut-offs are functions
of $t^\flat$ with $\chi_0 = 1$ on $[0,\frac32]$ (sections 2.6, 2.9). The identity can also be rescued as II.F Theorem
8.1, Step 2, does, by the domain of dependence for $P_0$ from $\{t_*>1/\epsilon\}$; the finding concerns the argument as
written, which rests on slab uniqueness alone.

(F'5) *The domain of Theorem 10.1.* The source applies Theorem 10.1, stated on $\Omega = \{t_*\ge1\}$, to functions on
$\Omega_*$, noting $\Omega_*\subset\Omega$. The norms on $\Omega$ and $\Omega_*$ are quotient norms over different sets
of extensions, and the identification of the solution uses uniqueness on slabs of $\Omega_*$; II.F Theorem 8.1 is used
here as stated and proved on $\Omega_*$ (II.F section 8).

(F'6) *The extension at $\{r = r_0\}$.* The bound (11.18), "completely analogous" to the proofs of Propositions 7.11 and
8.9 with Lemma 8.8 near the initial and final boundary hypersurfaces, needs at the final face $\{r = r_0\}$ an extension
that is nearly minimal at the low and the high b-regularity at once, and $\Omega_*$ provides no room there. Lemma 2.5
constructs one where the order function is a constant integer, which the order functions of II.C section 5.2 can be made
to be near $\{r\le r_0\}$ (Lemma 2.3). The same extension is needed in II.E Proposition 4.4 at its $r$-face and in II.E
Proposition 5.6 (b) at $\{r = a\}$, whose proofs take "the minimal extension" of the source term (section 8.2).

(F'7) *The threshold for $P_\epsilon$.* "$P_\epsilon$ ... satisfies the same assumptions as $P$ itself": (1) and (2) of
Definition 5.18 hold uniformly (Lemma 2.6, which also handles the extension of the data at $\mathscr I^+$ independently
of $x_I$, the cut-off not being independent of $x_I$), but (3), the triangular structure with diagonal blocks of real
spectrum, need not, and $\bar p_1$ varies with $\epsilon$. Lemma 2.1 shows that neither matters: the estimates use only a
fibre inner product making $\mathrm{Re}\,p_1$ large, and one adapted to $S$ serves all small perturbations, with the
threshold $\alpha_I<-\frac12+\bar S$ of the theorem.

(F'8) *Remark 11.2.* With relaxed $\aleph$-admissibility, Theorem 10.1 loses $d_\aleph$ also in the existence step
(11.16), which the remark does not address; Remark 7.1 raises the margin by $2d_\aleph$ and $d$ by $\lceil
d_\aleph\rceil$.

(F'9) (11.12) states $P_\epsilon-P_0\in x_I^2\rho_+^2C^{(\tilde
d_0;k),(2\ell_I,\ell_+,\ell_K)}_{e3b;b}\mathrm{Diff}^2_{e3b}$; the terms $\chi_I\frac12x_I^2\rho_+^2(2\tilde p_1A+p_0)$
of $P-P_0$ do not decay at $\mathscr I^+$, so the weight there is 0, as (11.13) in fact uses (the weight $2\alpha_I$ on
both sides).

(F'10) *The statement on $\Omega$.* The penultimate statement of Theorem 11.1 (principal part of $P$ equal to that of the
Kerr wave operator, $\Omega$ for $\Omega_*$) is not proved here (section 1.3 (a)).

(F'11) *Uniformity in $P_0$.* The source allows $P_0$ to vary near $P_1$; this needs II.F Theorem 8.1 and the
$\aleph$-admissibility estimate uniformly in $P_0$, which are not proved or assumed here (section 1.3 (b)). Open until a
later part needs it. For the family $P_0 = 2L_b$, $b$ near $b_0$, III.H$''$ (D294) proves both and Theorem 1.1
uniformly, with continuity in $b$ (its Theorems 3.1 and 4.1), to be verified.

(F'12) Remark 11.4 at $n = 4$ reads $\beta_-<1+\bar S$; and the source's (12.7) prints $\epsilon_+<\epsilon_I$ where
$\alpha_+<\alpha_I-\frac12$ needs $\epsilon_+>\epsilon_I$ (Remark 7.3; for Part II.G).

### 8.2 Consequences for earlier parts

(a) II.F Theorem 8.1 is used on $\Omega_*$ (F'5); II.F section 8 states and proves it there.

(b) II.E Propositions 4.4 and 5.6 (b) are tame estimates whose proofs extend the source term across the final face $\{r =
r_0\}$, resp. $\{r = a\}$, by "the minimal extension", which is minimal for one norm only. With the order constant and a
nonnegative integer near $\{r\le r_0\}$, which is the case for the orders used here (Lemma 2.3), the extension $E$ of
Lemma 2.5 serves at every level at once, and the proofs go through with it; for other admissible or slab orders the
tame bounds are not proved, and II.E now states (6.2), (4.4) and (5.6) under that hypothesis (D212: the eighty-eighth
verifier's Minor 3); the source term's extension
across the time-final face of a slab is a restriction from a larger slab wherever the propositions are applied (II.E
Theorem 6.1 (A), section 4 here, II.F Step 0). This is recorded in II.E (D209).

### 8.3 Sources

[Hin26c] P. Hintz, *(Non-)linear waves on asymptotically flat spacetimes. II*, arXiv:2606.28008v1, section 11 (pp.
227-233) and (12.7) (p. 235), read in full in the record's text extraction.

[SBG] arXiv:2408.06651v1, as READ in II.A section 3: (S3) for the integer-order and compactness statements, (S5), (S8)
and (S10) for Lemma 2.4.

The earlier parts are cited as in the header.

### 8.4 The verifier's findings, and the repairs (D212)

The eighty-eighth verifier read this part line by line, re-derived the density identity of Corollary 1.2, the margins of
Lemma 2.3 and the constants of section 5 by machine, and confirmed (F'1)-(F'12) at source. One major finding: Theorem 1.1
claimed uniqueness in $H^{s',(2\alpha_I,\beta_+,\beta_K)}_{e3b}$ for every $s'$, while Lemma 2.2 needs the smallness of
II.E Proposition 3.4 (i), whose $d_0$ depends on $s'$ and is not implied by $\|P-P_0\|_{(0;d)}<\epsilon_0$, and for $s'$
far below $-d$ the product $Pu$ is not defined. The class is restricted to $s'\ge s_{\mathrm u} = \inf\mathsf s-2$,
which is all the proof uses, and that smallness is added to section 3.1. One minor finding, on (E14): the extension of
Lemma 2.5 needs the order constant and integer near $\{r\le r_0\}$, which holds for the orders used here and not for
every admissible order; II.E now states its tame bounds under that hypothesis, and section 8.2 (b) says so. Two notes:
(F'4) records that the source's identity can also be rescued by the domain of dependence, and Lemma 2.2's reference to
Lemma 2.6 (a) is marked as not circular.
