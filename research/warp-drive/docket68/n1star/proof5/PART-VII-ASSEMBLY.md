# Part VII: Theorem 4 assembled

*Status.* Written (D322); verified (D323: verifier 140's three minor findings and twelve notes repaired). This part
proves the paper's Theorem 4 (RESPONSE-HL-5D.md section 8.8) from Parts III-VI and the record, in the form of Theorem
0.2. In (i), the data of the record's solution after the shell, on III.K's initial surface, are continued
G-equivariantly to exact Tangherlini data far out (section 2). Their development is G-invariant and settles to
Tangherlini, by III.K run in the class (section 3). In (ii), every perturbation of those data that is small in III.K's
data class has a development settling to a Myers-Perry metric (III.K Theorem 4.3). Five findings change what the paper
states (section 5). (VII1): (ii) is stated for perturbations in III.K's data class. The record's gluing of a general
decaying perturbation (10.63) replaces its data near infinity, and the late-time solution near the hole depends on those
data. (VII2): III.K's data weight must exceed $3+\epsilon_+$; VI.C's rows d1-d2 omitted this, and they are repaired.
(VII3): the initial surface is III.K's $\Sigma_{\mathrm{IVP}}$, not the record's $\tau$-slice, so no Cauchy stability
argument is needed. (VII4): the rate is $t_*^{-(\alpha-2)+\epsilon}$, slightly below the paper's $t_*^{-2-\epsilon_K}$,
and the record's solution and the settling development are related through their common data on a ball. (VII5): the
class run needs the choices of Parts III-IV made O(4)-equivariant, which is possible (Lemma 3.1): cut-offs and gauge
1-forms are radial, and linear maps and families given by existence statements are averaged. The inputs are III.K
Theorem 4.3, Part V's gluing lemmas, VI.C Theorem 2.1, II.G Theorem 2.1, and from the record sections 0-2, 10.50 (a) and
the dependence of Theorem E on its order (written out in Lemma 1.1).

## 0. Setting and statement

*The record.* We use N1STAR-PROOF.md's coordinates $(\tau,x)$ of its section 0.1, with $r = |x|$ and $v = \tau+r$, and
its Vaidya background $g_0 = \eta+(\mu(v)/r^2)\,dv\,dv$, where $\mu = \mu_{\mathrm{end}}$ for $v\ge v_{\mathrm{end}}$.
Also its domain $\Omega$ (1.1), with constants $(T,\delta_0)$ and $a = q_0-\delta_0$, and the solution $g_\lambda$ of
its Theorem E on $\Omega$, the paper's Theorem 1. For $v\ge v_{\mathrm{end}}$, $g_0 =
\eta+(\mu_{\mathrm{end}}/r^2)(d\tau+dr)^2$ is III.B's Kerr-Schild Tangherlini metric
$g^{\mathrm{KS}}_{\mu_{\mathrm{end}},0}$, with Kerr-Schild time $\tau$.

*The group.* $G := O(2)\times O(2)$ acts on $\mathbb R^4 = \mathbb R^2\times\mathbb R^2$ by the rotations of the planes
$(x^1,x^2)$ and $(x^3,x^4)$ and the reflections $x^2\mapsto-x^2$, $x^4\mapsto-x^4$; on spacetime it acts by
$(t,x)\mapsto(t,\sigma x)$. This is the record's $T^2\times\mathbb Z_2\times\mathbb Z_2$, and $g_0$ and $g_\lambda$ are
$G$-invariant (record sections 0.2 and 0.7). Every element of $O(4)$, acting so, is an isometry of every
$g^{\mathrm{KS}}_{m,0}$ and fixes every function of $(t,|x|)$. The fixed spaces are $(\mathbb R^4)^G = 0$ and
$\mathfrak{so}(4)^G = 0$. Indeed, $T^2$ fixes in $\mathbb R^4$ only 0, and in $\mathfrak{so}(4)$ exactly
$\mathrm{span}(W_{12},W_{34})$, while $x^2\mapsto-x^2$ reverses $W_{12}$ and $x^4\mapsto-x^4$ reverses $W_{34}$.

*III.K's setting.* Put $b_0 := (\mu_{\mathrm{end}},0)$. So III.B's $\mu_0$ is $\mu_{\mathrm{end}}$, $R_1 =
\mu_{\mathrm{end}}^{1/2}$ and $r_0 = \frac12R_1$. III.B's coordinates $(t,x)$ have $g_{b_0} =
\Phi_{\mu_{\mathrm{end}}}^*g^{\mathrm{KS}}_{\mu_{\mathrm{end}},0}$, that is $t =
t_{\mathrm{KS}}+T_{\mu_{\mathrm{end}}}(|x|)$ (III.B (3.3)). $t_*$, $t_{\mathrm{IVP}}$, $\Sigma_{\mathrm{IVP}}$,
$\Omega_*$, $\mathcal D$, $\chi_K$ and the boosts $\phi_S$ are those of III.K section 0. The parameters are those of
VI.C Theorem 2.1, with its step (3) (the data classes, which precede the weights since D323) taken as
$$\mathcal E_0 := \{(j,0):j\in\mathbb N,\ j\ge2\},\qquad\ell_0\in(3,4),\qquad\ell_I\in(3,
\ell_0).\tag{0.1}$$
Row d1 holds. $\min\mathrm{Re}\,\mathcal E_0 = 2>\frac32+2\gamma_\Upsilon$, since $\gamma_\Upsilon<\frac14$ (VI.C step
(2)); $\mathcal E_0$ is closed under sums and positive multiples; and $\ell_0>\frac32$ with $\ell_0\notin\mathbb N$. Row
d2 holds as amended (D323): $\ell_I\in(3,\min(\ell_0,\frac32+s_C))$, nonempty as $s_C>100$, off the discrete exclusion
sets of row d2 and of (H4). VI.C's step (4) then takes $\epsilon_+<\ell_I-3$, so (H4) of III.I$''''''''''$ holds
(finding (VII2)). Then $\epsilon$ and $d_1$ are those of III.K Theorem 4.3 (VI.C step (6)). For a pair
$(\tilde\gamma,\tilde k)$ of symmetric 2-tensors on $\Sigma_{\mathrm{IVP}}$, $\|(\tilde\gamma,\tilde k)\|_{d_1}$ is the
norm in which III.K Theorem 4.3 measures $(\gamma-\gamma_{b_0},k-k_{b_0})$: $H^{d_1}$ of $H^{\infty,(\mathcal
E_0,\ell_0)}_{\mathrm b}\times H^{\infty,(\mathcal E_0+1,\ell_0+1)}_{\mathrm b}$, infinite outside these spaces.

**Lemma 0.1 (what lies in the class).** Let $\rho := |x|^{-1}$, and let $\tilde\gamma$, $\tilde k$ be smooth symmetric
2-tensors on $\Sigma_{\mathrm{IVP}}$ whose Cartesian components lie, on $\{r\ge R'\}$, in $\rho^2C^\infty$ and
$\rho^3C^\infty$ of the radial compactification. Then $\|(\tilde\gamma,\tilde k)\|_{d_1}$ is finite, and it is bounded
by $C_{R'}$ times the sum of: the $C^{d_1+3}$-norms of the components on $\{r\le2R'\}$, and finitely many
$C^\infty$-seminorms of $\rho^{-2}\tilde\gamma$ and $\rho^{-3}\tilde k$ on the compactified $\{r\ge R'\}$.

*Proof.* Near $\rho = 0$, Taylor's formula in $\rho$ writes a function of $\rho^2C^\infty$ as
$\rho^2a_2(\omega)+\rho^3a_3(\omega)+\rho^4C^\infty$. The $a_j$ are smooth on $\mathbb S^3$, and the seminorms of the
remainder are bounded by those of $\rho^{-2}\tilde\gamma$. The exponents $(2,0)$ and $(3,0)$ lie in $\mathcal E_0$ below
$\ell_0$, and $\rho^4C^\infty\subset\rho^{\ell_0}H^\infty_{\mathrm b}$ as $\ell_0<4$. Likewise $\rho^3C^\infty =
\rho^3a_3+\rho^4a_4+\rho^5C^\infty$, with $(3,0)$ and $(4,0)$ in $\mathcal E_0+1$ below $\ell_0+1<5$. On $\{r\le2R'\}$
the weights are bounded above and below. $\square$

**Theorem 0.2 (Theorem 4).** Let $A$ and the envelope be fixed. For every $\epsilon_m>0$ there are $R$, a domain
$\Omega'$ of the record's form (1.1), $\lambda_1>0$ and $\delta>0$ such that the following holds for
$0<\lambda\le\lambda_1$. Here $g_\lambda$ is the solution of Theorem E on $\Omega'$, and $\Sigma_{\mathrm{IVP}}$ is
placed in the record's chart by Lemma 1.2.

(i) *In the class.* There are $G$-invariant smooth vacuum data $(\gamma_\lambda,k_\lambda)$ on $\Sigma_{\mathrm{IVP}}$
that equal the data of $g_\lambda$ on $\Sigma_{\mathrm{IVP}}\cap\{r\le R\}$, and the data of
$g^{\mathrm{KS}}_{m_\lambda,0}$ on $\Sigma_{\mathrm{IVP}}\cap\{r\ge4R\}$, with $|m_\lambda-\mu_{\mathrm{end}}|\le
C\lambda$ and $\|(\gamma_\lambda-\gamma_{b_0},k_\lambda-k_{b_0})\|_{d_1}\le C\lambda$. There are also $m'$ with
$|m'-\mu_{\mathrm{end}}|<\epsilon_m$, and a $G$-invariant metric $g$ on $\Omega_*\cup\mathcal D_0$ ($\mathcal
D_0\subset\mathcal D$, III.K Proposition 1.2) with $\mathrm{Ric}(g) = 0$ inducing $(\gamma_\lambda,k_\lambda)$ on
$\Sigma_{\mathrm{IVP}}$, such that where $\chi_K = 1$
$$g-g_{(m',0)} = h_{\mathrm{rem}}(q)+h,\qquad h\in\mathcal X^\infty_{J,\mathrm{ex}},
\quad q\in\mathcal Q_{\mathrm{ex}},$$
III.K Theorem 4.3 (3)-(4) with $b = (m',0)$ and $S = 0$; its term $h_{\mathrm{tot}}(\vec p)$ vanishes where $\chi_K =
1$, each of its terms carrying a factor $d\chi_K$ (PART-III-I5-UNBOOST.md:107-108, PART-III-I8-UNPARAM.md:139-141,
PART-III-I9-COMMOTION.md:81-82, PART-III-I10-CORR4.md:172-173). In particular, for every $R'$, $\epsilon'>0$ and
$i,\beta$ there are $C$ and $T'$ with
$$|(t_*\partial_{t_*})^i\partial^\beta_x(g-g_{(m',0)})|\le Ct_*^{-(\alpha-2)+
\epsilon'}\quad\text{on }\{r_0\le r\le R',\ t_*\ge T'\},\tag{0.2}$$
where $\alpha-2>2+\epsilon_K-\epsilon'_0>2$ (VI.C row w2), and $\alpha$ may be chosen as close to $4+\epsilon_K$ as
desired. On $\Sigma_{\mathrm{IVP}}\cap\{r<R\}$, $g$ and $g_\lambda$ induce the same data.

(ii) *Without symmetry.* Let $(\gamma,k)$ be smooth vacuum data on $\Sigma_{\mathrm{IVP}}$ with
$(\gamma-\gamma_\lambda,k-k_\lambda)\in H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}\times H^{\infty,(\mathcal
E_0+1,\ell_0+1)}_{\mathrm b}$ and $\|(\gamma-\gamma_\lambda,k-k_\lambda)\|_{d_1}<\delta$. Then there are $b\in\mathcal
B_*$ with $|b-b_0|<\epsilon_m$, $S\in\mathcal S_1$ with $|S|<\epsilon_m$, and a metric $g$ on $\Omega_*\cup\mathcal
D_{-S}$ with $\mathrm{Ric}(g) = 0$ inducing $(\phi_{-S}|)^*(\gamma,k)$ on $\phi_{-S}^{-1}(\Sigma_{\mathrm{IVP}})$, such
that where $\chi_K = 1$, $g-g_b = h_{\mathrm{rem}}(q)+h$ with the classes of (i). So $g$ settles to the Myers-Perry
metric $g_b$ at the rates (0.2).

## 1. The record's solution after the shell

**Lemma 1.1 (after the shell).** Let $\Omega'$ be a domain of the record's form (1.1) with constants $(T',\delta'_0)$,
and let $J\ge2$ be an integer. Put $k := K := J+4$ and $N := K+3$, and build $g_\lambda$ on $\Omega'$ with these orders
(record Theorems A, D and E). There are $C_J$ and $\lambda_1$ such that for $\lambda\le\lambda_1$, on $\Omega'_+ :=
\Omega'\cap\{v\ge v_{\mathrm{end}}+1\}$, $g_\lambda$ is $G$-invariant and vacuum, and its Cartesian components satisfy
$$|\partial^j(g_\lambda-g^{\mathrm{KS}}_{\mu_{\mathrm{end}},0})|\le C_J\lambda\qquad(j\le J),\tag{1.1}$$
with $\partial^j$ any $j$ derivatives in $(\tau,x)$.

*Proof.* *Theorem E at order $k$.* The record states Theorem E at $k = 6$ (its section 0.4). Its section 4 uses $k$ only
through Sobolev indices, in Steps 1, 4 and 8. Step 1's scaled bound $\|\partial^iw\|_\infty\le C\lambda^{-3-i}\mathcal
N$ needs $i+3\le k+1$. Step 4 splits its commutator terms $\partial^ig\cdot\partial^{j-i+1}\partial h$ at $i = k-2$
instead of $i = 4$, so the $L^\infty$ factor needs at most $k+1$ derivatives of $\mathcal N$'s quantities. Its nonlinear
terms use $|\partial w\,\partial w|_k\le C_k\lambda^{-3}|\partial w|_k^2$, the scaled product bound of the record's
Lemma 2.1, valid for every $k\ge3$. Step 8 uses [DS23] Theorem 2.4 with $r = k>3$. Steps 2, 5, 6 and 7 do not use $k$.
The bootstrap closes when $2K-5\ge K+1$, that is $K\ge6$, whatever $k$ is, with constants depending on $k$. Its inputs
at order $k$ hold. (E3): Theorem A's residual is $\lambda^N$ times a profile bounded with all its derivatives (record
(5.4)), so $|\mathrm{Ric}^H(g_{\mathrm{app}})|_k\le C_k\lambda^N$. (E4): the record's Proposition 6.5 bounds the
correction at every order with $\lambda_0$ independent of the order, so the data are $O(\lambda^{N-3}) = O(\lambda^K)$
at order $k$. So $\mathcal N_k\le M_k\lambda^K$ on $\Omega'$. (This is the record's 10.51, carried here into the proof.)

*After the shell.* $\mu' = \frac29A^2\mathrm{env}^2$ (record (0.5)) and $\mathrm{env} = 0$ for $v\ge v_{\mathrm{end}}$,
so $\mu = \mu_{\mathrm{end}}$ there, and the leading wave, proportional to the envelope, vanishes on
$\{v>v_{\mathrm{end}}\}$. That set is a union of generators of $\ell$, as $L_0(v) = 0$. By the record's Lemma 6.2, the
oscillating stage data are $-\mathrm{Pol}^+$ of terms bilinear in $\partial_\theta W$ or built from earlier oscillating
quantities. By its Lemma 5.3 (c), each oscillating profile solves a transport along $\ell$ whose source has an
oscillating factor in every term. By induction on the stage, every oscillating profile vanishes on
$\{v>v_{\mathrm{end}}\}$. So there $g_{\mathrm{app}} = g_0+\sum_{j=1}^N\lambda^jm_j$, with $g_0 =
g^{\mathrm{KS}}_{\mu_{\mathrm{end}},0}$ and $m_j$ smooth and independent of $\lambda$ (record 10.50 (a)), and $w =
h+\phi[\partial_\theta g_1] = h$ (record section 0.4).

*Bounds.* $\mathcal N_k\le M_k\lambda^K$ gives the unscaled bounds $\|\partial^i\partial h(\tau)\|\le M_k\lambda^{K-i}$
for $i\le k$, and $\|h(\tau)\|\le M_k\lambda^{K-1}$ (record section 0.4 and 10.51 (d)). Sobolev's inequality on the
slices $A(\tau)$ (the record's Lemma 2.1, $\|f\|_\infty\le C\sum_{i\le3}\|\partial^i_xf\|$, uniformly in $\tau$) gives
$|\partial^jh|\le C_k\lambda^{K-j-3}$ for $j\le k-3$. With $K = J+4$, this is at most $C\lambda$ for $j\le J$, and so
are the derivatives of $\sum_j\lambda^jm_j$ on the compact $\Omega'_+$. The vacuum equations and $G$-invariance are the
record's section 0.7. $\square$

**Lemma 1.2 (placing $\Sigma_{\mathrm{IVP}}$).** Let $R\ge R_3$, the radius beyond which $\psi_{\mathrm{IVP}}$ is
constant (III.B Lemma 3.7 (b)). There are $c_0\in\mathbb R$ and a domain $\Omega'$ of the record's form (1.1), with $a'
= q_0-\delta'_0<\frac12r_0$, such that in the chart $(t,x) := (\tau+T_{\mu_{\mathrm{end}}}(|x|)+c_0,x)$: (a) $g_0 =
g_{b_0}$ on $\Omega'\cap\{v\ge v_{\mathrm{end}},\ |x|\ge r_0\}$, where $g_{b_0}$ is defined; (b)
$\Sigma_{\mathrm{IVP}}\cap\{r_0\le r\le4R\}$ lies in the interior of $\Omega'_+$. The chart change commutes with $G$,
and $\Sigma_{\mathrm{IVP}}$ is $G$-invariant.

*Proof.* (a) There $g_0 = g^{\mathrm{KS}}_{\mu_{\mathrm{end}},0}$ in $(\tau,x)$, which does not depend on $\tau$, and
$g_{b_0} = \Phi^*g^{\mathrm{KS}}_{\mu_{\mathrm{end}},0}$ with $\Phi(t,x) = (t-T_{\mu_{\mathrm{end}}}(|x|),x)$. (b) On
$\Sigma_{\mathrm{IVP}}$, $t = \psi_{\mathrm{IVP}}(|x|)$, so $\tau = \theta(r)-c_0$ with $\theta :=
\psi_{\mathrm{IVP}}-T_{\mu_{\mathrm{end}}}$, continuous on $[r_0,4R]$. Take $c_0 :=
\min\theta-\max(\tau_0+1,v_{\mathrm{end}}+2-r_0)$. Then $\tau\ge\tau_0+1$ and $v = \tau+r\ge v_{\mathrm{end}}+2$ there,
and $\tau\le\tau_{\mathrm{top}} := \max\theta-c_0$. Take $\delta'_0\in(0,q_0)$ with $q_0-\delta'_0<\frac12r_0$, and $T'$
so large that $V' := v_{\mathrm{end}}+T'\ge\tau_{\mathrm{top}}+2R+q_{\mathrm{end}}+1$, where $q_{\mathrm{end}} :=
r_q(\mu_{\mathrm{end}})$ bounds $r_q(v)$, $\mu$ being nondecreasing. Then $\tau'_{\mathrm{end}} = \max_{v\le
V'}(v-r_q(v))\ge V'-q_{\mathrm{end}}\ge\tau_{\mathrm{top}}+1$, and
$v+(\tau-\tau'_{\mathrm{end}})\le2\tau_{\mathrm{top}}+4R+q_{\mathrm{end}}-V'<V'+1$. With $r\ge r_0>a'$, the defining
inequalities of $\Omega'_+$ hold strictly. $\tau_0$ is the record's. The last sentence holds as $T_{\mu_{\mathrm{end}}}$
and $\psi_{\mathrm{IVP}}$ are functions of $|x|$. $\square$

## 2. The data of (i): gluing in the class

For $r\ge R_3$, $\Sigma_{\mathrm{IVP}} = \{t = c_{\mathrm{IVP}}\}$ with $c_{\mathrm{IVP}}$ the constant value of
$\psi_{\mathrm{IVP}}$, that is $\{t_{\mathrm{KS}} = f(|x|)\}$ with $f := c_{\mathrm{IVP}}-T_{\mu_{\mathrm{end}}}$. For
$m\in I_\mu := [\frac34\mu_{\mathrm{end}},\frac54\mu_{\mathrm{end}}]$, let $(\gamma^m,k^m)$ be the data that
$g^{\mathrm{KS}}_{m,0}$ induces on this graph over $\{|x|>R_3\}$, as tensors on $\{|x|>R_3\}$. At $m =
\mu_{\mathrm{end}}$ they are $(\gamma_{b_0},k_{b_0})$.

**Lemma 2.1 (Tangherlini on $\Sigma_{\mathrm{IVP}}$).** (a) $\gamma^m-\delta\in\rho^2C^\infty$ and
$k^m\in\rho^3C^\infty$ on the compactified $\{|x|>R_3\}$, smoothly in $m\in I_\mu$, and $\gamma^m-\gamma_{b_0}$,
$k^m-k_{b_0}$ have seminorms $O(|m-\mu_{\mathrm{end}}|)$. In particular Part V's $|||(\gamma^m,k^m)|||_{2,j}$ is bounded
for every $j$, uniformly in $m$. (b) $(\gamma^m,k^m)$ are vacuum and $O(4)$-invariant. (c) Their charges (Part V
Proposition 1.3) are $\mathfrak Q_{e_0} = 6\pi^2m$ and $\mathfrak Q_X = 0$ for $X$ in the other three groups of Part V
(0.4).

*Proof.* (a) $g^{\mathrm{KS}}_{m,0}-\eta = (m/r^2)\ell\otimes\ell$ with $\ell = dt_{\mathrm{KS}}+\hat x\cdot dx$,
independent of $t_{\mathrm{KS}}$ and a classical symbol of order $-2$ in $x$, smoothly in $m$, and
$f'\in|x|^{-2}C^\infty$ near infinity (III.B Lemma 3.5 (a)). The induced metric
$g_{ij}+2g_{t(i}\partial_{j)}f+g_{tt}\partial_if\partial_jf$ and the second fundamental form (Part V (0.2) for the
graph) are smooth functions of the components of $g^{\mathrm{KS}}_{m,0}$ at $(f(x),x)$, which do not depend on the first
argument, and of $(\partial f,\partial^2f)$. They equal $(\delta,0)$ at $g = \eta$, $f$ constant. This gives the symbol
classes, and the $m$-derivatives are symbols of the same orders. (b) $g^{\mathrm{KS}}_{m,0}$ is Ricci flat (III.B
Proposition 3.4), and $O(4)$ acts by its isometries, preserving the graph. (c) The charges are limits of the fluxes
$\oint_{S_\rho}\mathfrak b_X$ of Part V (1.1). The flux integrand is natural for the Euclidean structure, so on
$O(4)$-invariant data $X\mapsto\mathfrak Q_X$ is an $O(4)$-invariant linear form on $\mathcal K$. It therefore vanishes
on the summands $\mathbb R^4$, $\Lambda^2\mathbb R^4$, $\mathbb R^4$, which are irreducible and nontrivial. $\mathfrak
b_{e_0} = (\partial_jh_{ij}-\partial_i\mathrm{tr}\,h)\nu^idS$ involves only $h = \gamma-\delta$. On the graph,
$\gamma^m_{ij}$ differs from the metric induced on $\{t_{\mathrm{KS}} = 0\}$ by
$2g_{t(i}\partial_{j)}f+g_{tt}\partial_if\partial_jf = O(r^{-4})$, with first derivatives $O(r^{-5})$, as $g_{ti} =
(m/r^2)\hat x_i$. So the two fluxes over $S_\rho$ differ by $O(\rho^{-2})$, and $\mathfrak Q_{e_0}$ is that of
$\{t_{\mathrm{KS}} = 0\}$, which is $6\pi^2m$ by Part V Proposition 2.3 at $p = (m,0,0,0)$. $\square$

**Proposition 2.2 (gluing in the class; [CD03] Theorem 8.1 with $G$).** Write $\bar\mu := \mu_{\mathrm{end}}$ and fix
$k\ge3$, the order of the gluing (not Theorem E's order of Lemma 1.1). There are $R_{\mathrm{gl}}$, $\eta_0$ and $C$
such that for $R\ge\max(R_{\mathrm{gl}},R_3)$ the following holds. Let $(g,K)$ be $G$-invariant smooth vacuum data on
$\Sigma_{\mathrm{IVP}}\cap\{r_0\le r\le3R\}$ with
$$\eta := \sup_{R\le r\le3R}\Big(\sum_{|\beta|\le k+4}r^{2+|\beta|}|\partial^\beta(g-\gamma^{\bar\mu})|+
\sum_{|\beta|\le k+3}r^{3+|\beta|}|\partial^\beta(K-k^{\bar\mu})|\Big)\le\eta_0.\tag{2.1}$$
Then there are $m$ with $|m-\bar\mu|\le C\eta$, and $G$-invariant smooth vacuum data $(\hat g,\hat K)$ on
$\Sigma_{\mathrm{IVP}}$, equal to $(g,K)$ on $\{r\le R\}$ and to $(\gamma^m,k^m)$ on $\{r\ge4R\}$, with
$$\sup_{R\le r\le4R}\Big(\sum_{|\beta|\le k-1}r^{2+|\beta|}|\partial^\beta(\hat g-\gamma^{\bar\mu})|+
\sum_{|\beta|\le k-2}r^{3+|\beta|}|\partial^\beta(\hat K-k^{\bar\mu})|\Big)\le C\eta.\tag{2.2}$$

*Proof.* Part V's proof of Theorem 3.1, with $k$ in place of 3 (its Step 1 allows any $k>\frac n2$) and seven changes.

(1) *The data used.* Steps 2-5 use $(g,K)$ only on $\Gamma(R,3R)$ (in Step 2, $\chi = 0$ for $r\ge3$), and through
$\mathfrak Q^0$ in Step 4. Replace $\mathfrak Q^0$ by the fluxes $\mathfrak Q^0_R := (\oint_{S_R}\mathfrak
b_{e_j}(g-\delta,K))_j$; Step 4's term at $S_R$ is then exactly $\mathfrak Q^0_R$.

(2) *The family.* Replace the members by $(\gamma^m,k^m)$, $m\in I_\mu$. Lemma 2.1 (a) gives Step 2 (a)'s bounds, with
$\alpha = 2$, and continuity in $m$. Step 1's smallness holds for $R\ge R_{\mathrm{gl}}$: the rescaled $x_{m,R}$ is
within $C(\bar\mu+\eta_0)R^{-2}$ of $(0,\delta)$.

(3) *Equivariance.* $G$ acts on data on $M = \bar\Gamma(1,4)$ by pull-back, commuting with the rescaling $\sigma_R$. For
$G$-invariant $x' = (K',g')$, the map $\Psi(x',\cdot)$ of Part V Lemma 3.2 is $G$-equivariant. Indeed, the constraint
map is natural, $x$ and the weights $e^{\pm s/x}$, $x^2$ are radial, $T_{x'}$ is natural, and $\pi_{g'}$ commutes with
$G$, as $\mathcal K$ and the $L^2_\psi(g')$ inner product are $G$-invariant. The norms of Step 1 are $G$-invariant. So
the solution of (3.1) in Part V Lemma 3.2's ball is unique, hence $G$-invariant when $x'$ and the source are, and $\hat
x_{m,R} := x_{m,R}+\delta x_{m,R}$ is $G$-invariant.

(4) *A one-dimensional obstruction.* By Step 3, $(J,\rho)(\hat x_{m,R}) = e^{-2s/x}\sum_ic_iM^{-1}_{g'}e_i$, which is
$G$-invariant. $M_{g'}$ commutes with $G$, so $\sum_ic_ie_i\in\mathcal K^G = \mathrm{span}(e_0)$ (section 0). Hence
$(J,\rho)(\hat x_{m,R}) = 0$ if and only if $c_0 = 0$, if and only if $F_R(m)_0 = \mathcal G'_{00}c_0 = 0$, where
$\mathcal G'_{00}>0$ for $R$ large (Step 3).

(5) *A zero.* Step 4 at $j = 0$ with $\alpha = 2$ gives $G_R(m) := R^2F_R(m)_0 = 6\pi^2m-\mathfrak Q^0_{R,0}+O(R^{-1})$,
uniformly on $I_\mu$. By (2.1) and Lemma 2.1, $\mathfrak Q^0_{R,0} = 6\pi^2\bar\mu+O(\eta)+O(R^{-2})$. So for $R$ large
and $\eta_0$ small, $G_R(\frac34\bar\mu)<0<G_R(\frac54\bar\mu)$. $G_R$ is continuous (Step 3), so it has a zero $m$, by
the intermediate value theorem in place of Part V Lemma 3.3.

(6) *The mass bound (new).* At $m$ the data $\hat x$ are vacuum. Part V Lemma 1.2 with $X = e_0$ on $\Gamma(R,4R)$,
unscaled, gives
$$\oint_{S_{4R}}\mathfrak b(\gamma^m,k^m)-\oint_{S_R}\mathfrak b(g,K)+\int_{\Gamma(R,4R)}q_{e_0}(\hat x)\,dx = 0.$$
The same lemma on $\Gamma(4R,\rho)$ for $(\gamma^m,k^m)$, and on $\Gamma(R,\rho)$ for $(\gamma^{\bar\mu},k^{\bar\mu})$,
with $\rho\to\infty$ (Lemma 2.1 (c); $|q|\le Cr^{-6}$ is integrable), gives $\oint_{S_{4R}}\mathfrak b(\gamma^m,k^m) =
6\pi^2m+\int_{r>4R}q(\gamma^m)$ and $\oint_{S_R}\mathfrak b(\gamma^{\bar\mu},k^{\bar\mu}) =
6\pi^2\bar\mu+\int_{r>R}q(\gamma^{\bar\mu})$. By (2.1), $\oint_{S_R}\mathfrak b(g,K)$ differs from the latter flux by at
most $C\eta$. Hence
$$6\pi^2(m-\bar\mu) = \int_{\Gamma(R,4R)}\big(q(\gamma^{\bar\mu})-q(\hat x)\big)+
\int_{r>4R}\big(q(\gamma^{\bar\mu})-q(\gamma^m)\big)+O(\eta).$$
Write $a := \sigma_R(g,K)$ and $b := \sigma_R(\gamma^m,k^m)$; both are vacuum and $x_{m,R} = b+\chi(a-b)$. The
constraint map is smooth near flat data and vanishes at $b$. So the source of Step 1 has
$\|(J,\rho)(x_{m,R})\|_{C^{k+1}}\le C\|a-b\|_{C^{k+3}\times C^{k+4}}\le C(\eta+|m-\bar\mu|)R^{-2}$. By Step 1's bound,
$\delta x_{m,R}$ is of the same size in $H^{k+2}(M)\subset C^{k-1}(M)$. Unscaled, $\hat x-(\gamma^{\bar\mu},k^{\bar\mu})
= \chi(a-\sigma_R(\gamma^{\bar\mu},k^{\bar\mu}))+(1-\chi)(\cdots)+\delta x$ has $|h|\le C(\eta+|m-\bar\mu|)R^{-2}$, with
each derivative, and $K$, a further factor $R^{-1}$. Both $\hat x$ and $(\gamma^{\bar\mu},k^{\bar\mu})$ have $|h|\le
CR^{-2}$ with the same scaling. $q_{e_0}$ is a smooth function of $(h,\partial h,\partial^2h,K,\partial K)$ vanishing to
second order at 0 (Part V Lemma 1.2's proof), with the quadratic bound (1.2). So $|q(\hat x)-q(\gamma^{\bar\mu})|\le
C(\eta+|m-\bar\mu|)R^{-6}$ on $\Gamma(R,4R)$, and $|q(\gamma^m)-q(\gamma^{\bar\mu})|\le C|m-\bar\mu|r^{-6}$.
Integrating, $6\pi^2|m-\bar\mu|\le C(\eta+|m-\bar\mu|)R^{-2}+C\eta$, so $|m-\bar\mu|\le C\eta$ for $R$ large.

(7) *The bound (2.2) and the conclusion.* $\hat x-(\gamma^{\bar\mu},k^{\bar\mu})$ is the sum of $\chi$ times the data's
deviation, $(1-\chi)(\gamma^m-\gamma^{\bar\mu},k^m-k^{\bar\mu})$ and $\delta x$. These are bounded in (2.2)'s norm by
$\eta$, by $C|m-\bar\mu|\le C\eta$ (Lemma 2.1 (a)), and by $C\eta$ (from (6), rescaled). The glued data are smooth,
vacuum and Riemannian as in Part V's Step 5, and $G$-invariant by (3). $\square$

**Corollary 2.3 (the data of (i)).** Let $k\ge3$ and $R\ge\max(R_{\mathrm{gl}},R_3)$, and let $c_0$ and $\Omega'$ be as
in Lemma 1.2. Take $J := k+5$ in Lemma 1.1, and let $(g,K)$ be the data of $g_\lambda$ on
$\Sigma_{\mathrm{IVP}}\cap\{r_0\le r\le4R\}$. Then (2.1) holds with $\eta\le C_R\lambda$, and for $\lambda$ small
Proposition 2.2 gives $(\gamma_\lambda,k_\lambda) := (\hat g,\hat K)$ and $m_\lambda := m$, with
$|m_\lambda-\mu_{\mathrm{end}}|\le C_R\lambda$. If $k\ge d_1+5$, then also
$\|(\gamma_\lambda-\gamma_{b_0},k_\lambda-k_{b_0})\|_{d_1}\le C_R\lambda$.

*Proof.* The data a metric induces on a fixed spacelike slice are smooth functions of its components and their first
derivatives at the slice. By Lemma 1.2 the slice piece lies in $\Omega'_+$, where $g_0 = g_{b_0}$, so by Lemma 1.1 the
data of $g_\lambda$ differ from $(\gamma_{b_0},k_{b_0}) = (\gamma^{\bar\mu},k^{\bar\mu})$ by $C\lambda$ in $C^{k+4}$
there. With the weights $r^{2+|\beta|}\le(3R)^{k+6}$, $\eta\le C_R\lambda$. The data are $G$-invariant ($g_\lambda$ and
$\Sigma_{\mathrm{IVP}}$ are, Lemmas 1.1 and 1.2) and vacuum. For the last claim apply Lemma 0.1 with $R' = 4R$: on
$\{r\le8R\}$ the deviation is $C_R\lambda$ in $C^{d_1+3}$, by Lemma 1.1, (2.2) and Lemma 2.1 (a), and on $\{r\ge4R\}$ it
is $(\gamma^m-\gamma_{b_0},k^m-k_{b_0})$, whose seminorms are $O(|m-\mu_{\mathrm{end}}|) = O(\lambda)$. $\square$

## 3. III.K in the class

$O(4)$ acts on $M$ by $(t,x)\mapsto(t,\sigma x)$ and on tensors by $\sigma_* := (\sigma^{-1})^*$. On the components of
$\mathcal D_{\mathrm{ex}}$ (III.J$'''$ Definition 1.1; III.J Definition 1.1) it acts as follows. On $b =
(\mu,A)\in\mathfrak b$ by $(\mu,\sigma A\sigma^{-1})$; on $\mathcal S_1\ni S_w$ by $S_w\mapsto S_{\sigma w}$; on the
coefficient spaces $\mathcal W_\tau$, $\mathcal Y_\rho$ (harmonics of III.A$'$ section 2, $\mathcal S_1$, and $\mathcal
V' = 0$) by their representations; and on the tensor and function components ($u^0_\lambda$, $f_\lambda$, $\tilde h$,
and the values of the $q$-tails) by $\sigma_*$.

**Lemma 3.1 (naturality).** Make the following choices $O(4)$-equivariant.

(C1) *Cut-offs:* $\chi^\flat_K,\chi_K,\chi^\sharp_K,\chi_{\mathrm{IVP}},\chi^\sharp_{\mathrm{IVP}}$
(PART-III-B-FAMILY.md:345-349, [Hin26] Definition 3.17 with $m_0 = R_1$), $\chi_r$ (:353), $\chi_\infty$ (:165),
$\chi_\iota$, $\chi_-$, $\chi_9$ (III.K sections 0 and 3), $\Theta$ (III.I$''''$), and the cut-offs inside $t^\flat_*$
(II.C Lemma 3.2). Every set in their conditions (the values 0 and 1, the supports, and the nesting of
PART-III-B-FAMILY.md:345-349, each later function equal to 1 near the support of the earlier) is defined by
$(t,t_*,t_{\mathrm{IVP}},t^\flat_*,|x|)$, hence $O(4)$-invariant. So they are chosen directly, in nesting order, as
smooth functions of these and of $|x|^2$: each is a cut-off between an invariant closed set and the interior of a larger
invariant set. No averaging is used; averaging separately could break the nesting.

(C2) *Gauge 1-forms:* $c_\Upsilon$, $c_{\Upsilon,H}$, $c_C$ (III.B Definition 6.1, PART-III-B-FAMILY.md:430-433;
PART-III-E-CONSTRAINT.md:19-21). They are stationary, lie in $|x|^{-1}C^\infty$ or are supported in $\{|x|<5R_1\}$, and
equal $|x|^{-1}dt$ or $|x|^{-1}(dt-v_C\,d|x|)$ for large $|x|$. The proofs use the specific forms $c_\Upsilon =
\zeta(|x|)|x|^{-1}dt$, $c_{\Upsilon,H} = -\frac12\chi(|x|)\,d|x|$ (PART-III-D3-SYMSTATES.md:30-32) and $c_C$ of
PART-IV5-CDMODES.md:36-38, which are $O(4)$-invariant; no averaging is needed.

(C3) *Linear maps given by existence statements:* $\omega_{\mathrm s1}(S)$ and $\breve\omega(S)$ (III.D$''$ Proposition
3.1 at $b_0$, linear in $S\in\mathcal S_1$; PART-III-I5-UNBOOST.md:63-66); the states and towers of III.G$''$ Table 1.1,
as linear maps of the coefficient spaces $\mathcal Y_\tau$ (PART-III-G3-GRAFT.md:40-80, 179-182); and the solution
operators $\mathcal S_{\lambda_0}$ (III.G$'''$ Corollary 3.1; PART-III-J-PARAM.md:225-227). Each is a linear map
$L:V\to\mathcal T$ from an $O(4)$-representation into tensors. Its conditions are linear in $L$ and $O(4)$-invariant:
equations with natural operators of $g_{b_0}$, and asymptotic or support conditions at faces fixed by $O(4)$. So
$L^{O(4)} := \int_{O(4)}\sigma_*\circ L\circ\sigma^{-1}\,d\sigma$ meets them, with the same bounds.

(C3$'$) *Families in $b$:* the towers and states at $b$ used in $h_{b,\mathrm{rem}}(q)$, namely $T_{\rho,b}$,
$h^{\le1}_{b,\mathrm s1}$, $h_{b,\mathrm v1}$ and $h^{\le2}_{b,\mathrm v1}$, chosen smooth in $b$ by
PART-III-I15-AUGMENT5.md Lemma 2.1 (:118-122). Replace a family $L_b$ by $L^{O(4)}_b := \int_{O(4)}\sigma_*\circ
L_{\sigma^{-1}\cdot b}\circ\sigma^{-1}\,d\sigma$. Then $\sigma_*\circ L^{O(4)}_b\circ\sigma^{-1} = L^{O(4)}_{\sigma\cdot
b}$, and the average keeps the tower relations for $L_b$ (natural, given (C2)), smoothness in $b$, the $b$-independent
leading terms, and the value at $b_0$ once (C3) is applied there.

(C4) *The complement $\mathcal V'$* of PART-III-I10-CORR4.md:89-91, which is 0 at $b_0$ (:93-94).

Then, for every closed subgroup $G'$ of $O(4)$, every $G'$-invariant data $(\gamma,k)$, every $\sigma\in G'$ and every
small $U\in\mathcal D_{\mathrm{ex}}$, $\Phi(\sigma\cdot U) = \sigma\cdot\Phi(U)$, $\Psi(\sigma\cdot U) =
\sigma_*\Psi(U)$ and $P_5(\Psi(\sigma\cdot U)) = \sigma_*P_5(\Psi(U))$. The proofs of Parts III-IV use the objects of
(C3) and (C3$'$) only through the conditions stated at the sites listed (finding (VII5)), so the averaged choices are
admissible.

*Proof.* By induction along the definitions; each object is natural, given (C1)-(C4) and (C3$'$).

- $g_b = \Phi_\mu^*g^{\mathrm{KS}}_{\mu,A}$. III.B Definition 3.2 builds $r_A$, $\ell_A = \mathsf M(rI+A)x/P\cdot dx$
and $H_{\mu,A}$ from $(\mu,A,x)$ by matrix operations, so $\sigma_*g_{(\mu,A)} = g_{(\mu,\sigma A\sigma^{-1})}$;
$\Phi_\mu$ and $T_\mu$ are radial. So $g_{b_0,\sigma\cdot b,-\sigma\cdot S} = \sigma_*g_{b_0,b,-S}$ (III.I (1.1)), given
the next item.

- $\phi_S = \exp V(S_w)$ with $V(S_w) = \frac12\chi_r\chi^\sharp_{\mathrm{IVP}}(1-\chi^\flat_K)X_w$ and $X_w =
t\,w\cdot\partial_x+(w\cdot x)\partial_t$ (PART-III-B-FAMILY.md:340-359). So $\sigma_*X_w = X_{\sigma w}$ and
$\sigma\phi_{S_w}\sigma^{-1} = \phi_{S_{\sigma w}}$.

- $t_*$, $t_{\mathrm{IVP}}$ are functions of $(t,|x|)$, and $t^\flat_*$ is a function of $(t_*,r)$: $C'(t_*+\tilde
R(r))$ and $t_*F(t_*/r)$ (PART-II-C-OPERATORS.md:443-444), given (C1).

- $E^\Upsilon_{g_0}$, $E^C_g$, $\Upsilon^{E_\Upsilon}(g,g_0) = \Upsilon^0(g,g_0)-E^\Upsilon_{g_0}G_{g_0}(g-g_0)$ and
$\delta^*_{g,E_C}$ (III.B Definition 6.1) are natural in $(g,g_0)$ and the forms of (C2). So are $P$ and $P_2$-$P_5$
(PART-III-I8-UNPARAM.md (2.2), PART-III-I15-AUGMENT5.md (1.3)).

- $\dot\omega_b(\dot b) = -\widehat{\Box^\Upsilon_b}(0)^{-1}\eta_b(\dot b)$ and $\dot g^\Upsilon_b$ (PART-III-F4-ZERO.md
(2.1)) are natural, the inverse being unique. $w(S) = g_{b_0}(X_S,\cdot)$ is natural.

- $h_{\mathrm{tot}}$ and $\vartheta_{\mathrm{tot}}$ (PART-III-I8-UNPARAM.md Definition 2.3, PART-III-I9-COMMOTION.md
Definition 2.1, PART-III-I10-CORR4.md Definitions 2.1 and 2.3) are built from $\chi_K$, $\delta^*_{g_{b_0}}$ and
commutators with $\chi_K$, the maps of (C3), $w(S)$, $\Theta$ and functions of $t_*$. $h_{\mathrm{rem}}(q)$
(PART-III-I15-AUGMENT5.md Definition 1.2) is $\chi_K$ times $h^{\le1}_{b,\mathrm s1}$, $\dot g_b$ and the towers of
(C3$'$).

- $\Phi$ (III.J (2.1), (2.4)) is built from $\chi_\iota$, $u_\lambda =
u^0_\lambda+\mathrm{res}_{z=\lambda}(t_*^{-z}N_{\iota^+}(z)^{-1}f_\lambda(z))$, with $N_{\iota^+}$ the normal operator
of a natural operator, $\tilde h$, and $h_{\lambda_0} = \mathcal S_{\lambda_0}(f)-R(\lambda_0)$.

- $h_{-S}$ (III.K Proposition 1.2) is the unique solution of (1.2) with data $h_{S,0}$, $h_{S,1}$, the pull-backs by
$\phi_S$ of III.C$''$ Proposition 4.1's $h_0$, $h_1$. That proof builds these from $(\tilde\gamma,\tilde k)$ and
$g_{b_0}$ by setting $h_0 := \tilde\gamma$ with $h_0(\nu_{b_0},\cdot) := 0$, and by solving tensorial linear equations
for $\tilde h_1$, uniquely (PART-III-C3-BOOSTDATA.md:174-196). So for $G'$-invariant data and $\sigma\in G'$, $h_{\sigma
S,j} = \sigma_*h_{S,j}$, and $h_{\sigma S} = \sigma_*h_S$ by uniqueness.

So $\Psi(U) = (\chi_-h_{-S},0,0)+\Phi(U)$ (III.K (2.1)) and $P_5\circ\Psi$ are equivariant. $\square$

**Proposition 3.2 (III.K Theorem 4.3 in the class).** Make the choices of Lemma 3.1 equivariant. If the data
$(\gamma,k)$ of III.K Theorem 4.3 are $G$-invariant, its conclusion holds with $U$ fixed by $G$, $b = (m',0)$, $S = 0$
and $g$ $G$-invariant.

*Proof.* *The action.* $G\subset O(4)$ acts on $M$ by diffeomorphisms that are smooth on the compactification, preserve
each boundary hypersurface (the defining functions of III.B (2.2) are functions of $(t,|x|)$), and fix $t$, $t_*$,
$t_{\mathrm{IVP}}$ and $t^\flat_*$. So it preserves $\Sigma_{\mathrm{IVP}}$, $\Omega_*$, $\mathcal D$, the classes
$B^k$, $B^k_\eta$, $F^k$, $F^\infty_\eta$ of III.K section 3, and the collar of III.K Lemma 3.1. Its action on each
$\mathcal D^k_{\mathrm{ex}}$ and $\mathcal F^k_{\mathrm{ex}}$ is bounded uniformly in $\sigma$, $G$ being compact and
acting smoothly. Replace each norm $|\cdot|_k$ by $\sup_{\sigma\in G}|\sigma\cdot(\cdot)|_k$, an equivalent norm. Then
$G$ acts isometrically, and every estimate used below holds with changed constants.

*Fixed spaces.* Let $B^{k,G}$, $B^{k,G}_\eta$, $F^{k,G}$ and $F^{\infty,G}_\eta$ be the $G$-fixed elements. They are
closed, and $\Pi := \int_G\sigma\,d\sigma$ (Haar probability measure) is a projection onto them of norm at most 1 that
preserves every support class.

*II.G Theorem 2.1 on the fixed spaces.* (i) $\Pi S_\theta$, with $S_\theta$ of III.K Lemma 3.1, maps
$B^{\infty,G}_{\theta^{-1/2}}$ into $B^{\infty,G}$ and $B^{\infty,G}_\eta$ into $B^{\infty,G}_{\eta-\theta^{-1/2}}$, and
satisfies II.G (2.1) with the constants of the $G$-sup norms. (ii) By Lemma 3.1, $U\mapsto P_5(\Psi(U))$ maps the fixed
part of III.K Theorem 3.2's domain into $F^{\infty,G}$, and $B^{\infty,G}_\eta$ into $F^{\infty,G}_\eta$.
Differentiability and II.G (2.2)-(2.3) hold by restriction. (iii) For $U\in B^{\infty,G}$, differentiating
$P_5(\Psi(\sigma\cdot V)) = \sigma_*P_5(\Psi(V))$ at $V = U$ gives $D_U(P_5\circ\Psi)\circ\sigma = \sigma_*\circ
D_U(P_5\circ\Psi)$. So $\Psi^G_{\mathrm{NM}}(U) := \Pi\Psi_{\mathrm{NM}}(U)$ on $F^{\infty,G}$ satisfies
$D_U(P_5\circ\Psi)\Psi^G_{\mathrm{NM}}(U)f = \Pi D_U(P_5\circ\Psi)\Psi_{\mathrm{NM}}(U)f = \Pi f = f$. It maps
$F^{\infty,G}_\eta$ into $B^{\infty,G}_\eta$ for $U\in B^G_\eta$, and inherits II.G (2.4). So II.G Theorem 2.1 holds on
the fixed spaces with its own threshold $\epsilon^G_{\mathrm{NM}}$, computed from the constants of the $G$-sup norms;
section 4 takes the data small for it as well. So II.G Theorem 2.1 on the fixed spaces gives $U\in B^{\infty,G}_{1/2}$
with $P_5(\Psi(U)) = 0$ on $\Omega_*$.

*The metric.* III.K Proposition 4.2 builds $g$ from $(h,\vec p,q) = \Phi(U)$, $h_{-S}$ and $g_{b_0,b,-S}$. By Lemma 3.1
every ingredient is equivariant and $U$ is fixed, so $g$ is $G$-invariant. $U_0 = (b-b_0,S,S^{(0)}_1)$ is fixed: by
section 0, $\mathfrak b^G = \mathbb R\times\{0\}$ and $\mathcal S_1^G = 0$, $\mathcal S_1$ being $\mathbb R^4$ as a
representation. So $b = (m',0)$ and $S = S^{(0)}_1 = 0$, and III.K Theorem 4.3 (1)-(5) hold with these values. $\square$

## 4. Proof of Theorem 0.2

Given $\epsilon_m>0$, fix the parameters by VI.C Theorem 2.1 with (0.1). In III.K Theorem 3.2's proof, apply II.G
Theorem 2.1 with its radius $\delta$ replaced by $\min(\delta,\epsilon_m)$: its hypotheses restrict to the smaller set,
and its $\epsilon_{\mathrm{NM}}$ then depends on $\epsilon_m$. This gives III.K Theorem 4.3 with
$|b-b_0|\le|U|_{3d}<\epsilon_m$ and $|S|<\epsilon_m$ (III.K Lemma 2.3's proof), for data of norm below some $\epsilon =
\epsilon(\epsilon_m)$, with $d_1$ as before. In (i), $\epsilon$ is moreover taken below the threshold for which
Proposition 3.2's run of II.G Theorem 2.1 applies (through the equivalence of the norms). Take $k := d_1+5$ in
Proposition 2.2, then $R\ge\max(R_{\mathrm{gl}},R_3)$, then $c_0$ and $\Omega'$ by Lemma 1.2, $J := k+5$ in Lemma 1.1,
and $\lambda_1$ so small that $C_R\lambda_1<\frac12\epsilon$. Put $\delta := \frac12\epsilon$.

*(i).* Corollary 2.3 gives $(\gamma_\lambda,k_\lambda)$, $G$-invariant, smooth and vacuum, with
$\|(\gamma_\lambda-\gamma_{b_0},k_\lambda-k_{b_0})\|_{d_1}<\frac12\epsilon$. By Lemma 0.1 the differences lie in
$H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}\times H^{\infty,(\mathcal E_0+1,\ell_0+1)}_{\mathrm b}$, since they vanish
beyond $4R$ up to $(\gamma^m-\gamma_{b_0},k^m-k_{b_0})$ (Lemma 2.1 (a)). Proposition 3.2 gives $U$, $b = (m',0)$ with
$|m'-\mu_{\mathrm{end}}|<\epsilon_m$, $S = 0$, and a $G$-invariant $g$ with III.K Theorem 4.3 (1)-(5). By (2), $g$
induces $(\gamma_\lambda,k_\lambda)$ on $\Sigma_{\mathrm{IVP}}$, which on $\{r<R\}$ are $g_\lambda$'s data.

*The rate (0.2).* Where $\chi_K = 1$, $g-g_{(m',0)} = h_{\mathrm{tot}}(\vec p)+h_{\mathrm{rem}}(q)+h$ (III.K Theorem 4.3
(4)). $h_{\mathrm{tot}}(\vec p)$ is supported in $\mathcal C$, whose closure is disjoint from $K^+$
(PART-III-I8-UNPARAM.md Lemma 2.2). So it vanishes on $\{r\le R'\}$ for $t_*$ large, as does $1-\chi_K$; indeed it
vanishes wherever $\chi_K = 1$ (statement (i)). $h\in\mathcal X^\infty_{J,\mathrm{ex}}$ has $K^+$-order $\alpha-$, and
$h_{\mathrm{rem}}(q)$ has $K^+$-order $(\alpha-2)-$ (PART-III-I15-AUGMENT5.md Lemma 2.2 (a) at $b_0$; at $b$ near $b_0$,
the rates of its (1.1), :61-65, which exceed $\alpha-2$, with its Lemma 2.1). Near the interior of $K^+$, $\rho_K =
t_0^{-1}$ with $t_0 = t-|x|$ (III.B (2.2), (4.1)), comparable to $t_*$ on $\{r\le R'\}$, and the b-vector fields there
are spanned by $t_*\partial_{t_*}$ and $\partial_x$. By b-Sobolev embedding (III.C$'$ section 0: a weight is the
pointwise order), $(t_*\partial_{t_*})^i\partial^\beta_x$ of a function of $K^+$-order $w-$ is $O(t_*^{-w+\epsilon'})$
for every $\epsilon'>0$. With $w = \alpha-2$ this is (0.2). By VI.C row w2, $\alpha$ is admissible in
$(4+\epsilon_K-\epsilon'_0,4+\epsilon_K]$, a dense set.

*(ii).* The difference $(\gamma-\gamma_{b_0},k-k_{b_0}) =
(\gamma-\gamma_\lambda,k-k_\lambda)+(\gamma_\lambda-\gamma_{b_0},k_\lambda-k_{b_0})$ lies in the class with norm below
$\delta+\frac12\epsilon = \epsilon$. So III.K Theorem 4.3 applies, with $|b-b_0|<\epsilon_m$ and $|S|<\epsilon_m$, and
the rate follows as in (i) with $g_b$. $\square$

*Remark 4.1 (the record's solution and $g$).* $g$ and $g_\lambda$ are vacuum metrics inducing the same data on
$\Sigma_{\mathrm{IVP}}\cap\{r<R\}$, in different gauges. That the domain of dependence of this set in
$(\Omega',g_\lambda)$ embeds isometrically into $(\Omega_*\cup\mathcal D,g)$ would follow from a change of gauge on a
compact region, where both metrics are $C^k$-close to $g_{b_0}$. That argument is not written here, and nothing in
Theorem 0.2 uses it (finding (VII4)).

## 5. Findings, labels and sources

(VII1) *Theorem 4 (ii) and the gluing.* The paper's (ii), from the record's 10.63 (c)-(d), glues a perturbation, small
in 10.62 (d)'s norms with parity or decay faster than $r^{-3/2}$, to a translated, rotated and boosted Myers-Perry
metric, and concludes that "the maximal vacuum development" settles. The gluing replaces the data near infinity, and the
solution near the hole at late times depends on those data: $K^+$ at late times is not in the domain of dependence of
any bounded part of the slice. So the conclusion holds for the glued data, not for the perturbation. Theorem 0.2 (ii)
takes the perturbation in III.K's own class. With (0.1) that class has polyhomogeneous terms of orders 2 and 3 at
spatial infinity and a conormal remainder of order $\ell_0\in(3+\epsilon_+,4)$. By Lemma 0.1 it contains every
perturbation that is, outside a compact set, a symbol of orders $-2$ (metric) and $-3$ (second fundamental form), for
instance the data of a nearby translated, rotated and boosted Myers-Perry metric. III.K needs no gluing in (ii), and no
parity condition. Part V's gluing is used in (i) in its class form (Proposition 2.2). For a merely decaying
perturbation, the gluing would give only that it agrees on a large ball with one to which (ii) applies. That statement
is not made here.

(VII2) *The data weight.* III.C$'$ Theorem 3.1 asks $\ell_I<\ell_0$, and (H4) of III.I$''''''''''$
(PART-III-I11-SPACETIME.md:45) asks $\ell_I>3+\epsilon_+$; III.K uses one $\ell_I$ for both
(PART-III-K-NONLINEAR.md:56-57). So $\ell_0>3+\epsilon_+$. VI.C's row d2 listed only $\frac32<\ell_I$, and row d1 only
$\ell_0>\frac32$. Both are repaired in VI.C (D322), and its order is corrected (D323): the data classes come first (step
(3)), since $\Lambda$ contains $\pi_1\mathcal E^C_I$, which depends on $\ell_I$, and then $\epsilon_+<\ell_I-3$ (step
(4)).

(VII3) *The initial surface.* The paper's $\Sigma''$ was the record's $\tau$-slice near the hole and a static slice far
out, from which the data were carried to Hintz's surface. Here the record's domain is enlarged (Lemma 1.2) so that it
contains III.K's $\Sigma_{\mathrm{IVP}}$ near the hole, and the record's data are read there directly. The gluing is
done on $\Sigma_{\mathrm{IVP}}$ itself, whose far part is a slice of III.B's time $t$, and the class family is
Tangherlini's data on that slice (Lemma 2.1). The record's 10.50 (c) used Cauchy stability over $[\tau_0,\tau_1]$;
nothing of the kind is used here.

(VII4) *The rate, and what is said of $g_\lambda$.* The slowest term at $K^+$ is $h_{\mathrm{rem}}(q)$, of order
$(\alpha-2)-$, so (0.2) gives $t_*^{-2-\epsilon''}$ for every $\epsilon''<\alpha-4$, which can be any number below
$\epsilon_K$ by the choice of $\alpha$. The paper's $O(t_*^{-2-\epsilon_K})$ holds with $\epsilon_K$ replaced by such an
$\epsilon''$. The paper's "contains $g_\lambda$ on $\Omega$" is replaced by the equality of data on
$\Sigma_{\mathrm{IVP}}\cap\{r<R\}$ (Remark 4.1).

(VII5) *Equivariant choices.* The class run needs $P_5\circ\Psi$ equivariant. The construction makes choices: cut-offs,
three stationary 1-forms, linear maps given by existence statements, and one complement. The cut-offs and the gauge
1-forms are chosen radial directly (the proofs already use radial forms; averaging cut-offs separately could break their
nesting). The linear maps given by existence statements, and their families in $b$, are averaged, which keeps the
conditions stated at their sites (Lemma 3.1, (C3) and (C3$'$); verifier 140's A-m2, A-m3). That no proof in Parts III-IV
uses more than those conditions is checked at the sites listed; a reader of Lemma 3.1 should confirm it. Every other
ingredient is natural or the unique solution of a natural problem. III.C$''$ Proposition 4.1's data and the boosts
$\phi_S$ are among the natural ones.

(VII6) *Part V in the class.* Proposition 2.2 adds to Part V's proof the equivariance of its Step 1, a one-dimensional
obstruction, and an a priori bound $|m-\bar\mu|\le C\eta$ from the flux identity. The bound makes the glued data
$O(\lambda)$-close to Tangherlini at a fixed gluing radius, which III.K's weighted norm needs: a bump of relative size
$R^{-1}$ at radius $R$ costs about $R^{\ell_0-3}$ in that norm, which grows with $R$.

*Labels.* Lemma 1.1: the record's 10.50 (a) and 10.51. Proposition 2.2: [CD03] Theorem 8.1 in the class (Part V, Theorem
3.1). Proposition 3.2: [Hin26] Theorem 13.1 in the class (the record's 10.49). Theorem 0.2: the paper's Theorem 4.

*Sources.* No new reading. Inputs: III.K Theorem 4.3, Proposition 1.2, Lemmas 2.2-2.3, 3.1, Theorem 3.2, Proposition
4.2; II.G Theorem 2.1; Part V Lemmas 1.2, 3.2, 3.3, Propositions 1.3, 2.3 and the proof of Theorem 3.1; III.B
Definitions 3.2, 6.1, Lemmas 3.5, 3.7, 5.1, Proposition 3.4, (2.2), (3.3), (4.1); III.C$''$ Proposition 4.1;
PART-III-I8-UNPARAM.md Lemma 2.2; PART-III-I11-SPACETIME.md (H4); PART-III-I15-AUGMENT5.md Lemma 2.2; III.J (2.1),
(2.4); PART-III-I15-AUGMENT5.md (1.1) and Lemma 2.1; PART-III-D3-SYMSTATES.md:30-32; PART-IV5-CDMODES.md:36-38; VI.C
Theorem 2.1; the record's sections 0-2, 4-6, 10.50 (a), 10.51.
