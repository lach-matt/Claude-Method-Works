# Part II.D. Microlocal regularity on spacetime: radial sets, trapping and the global estimate, at n = 4

*Status.* Proved (D326: verifier 142 read the D204 repairs, correct; one nit seated), with one repair to be read (D328:
verifier 144 found the setting of section 4 still on $\{t_*>1\}$ after II.C$'$'s start time moved; it is now on
$\{t_*>T_\flat\}$). Verified. Written out in full (D202). Read line by line by the eighty-fourth verifier, which
re-derived every threshold, sign and dynamical claim and confirmed (D1)-(D4) at source; its two minor findings (the
comparison of norms in Step 3 of Proposition 4.2, and the support of the time cut-off's term in Proposition 3.6) and its
nits are seated (D204). The part is labelled proved once the next reader has confirmed them; verifier 142 did (D326),
and verifier 143 confirmed the D326 repairs, its two nits seated (D327). This part proves, at spatial dimension $n = 4$,
[Hin26c] section 7.1 (pp. 114-127): the global edge-3b regularity estimate, its Proposition 7.1, with the ingredients it
combines, the radial point estimates (Propositions 7.4 and 7.6-7.9, Remark 7.5) and the estimate at the trapped set
(Proposition 7.10). Section 7.2 of the source, b-regularity and estimates tame in it, is Part II.D$'$. The source is
[Hin26c] = P. Hintz, arXiv:2606.28008v1 (printed page numbers). Part I.A (`PART-I-SPECTRAL.md`) is cited as I.A, Part
I.B (`PART-I-B-HIGHENERGY.md`) as I.B, Part II.A (`PART-II-A-SETUP.md`) as II.A, Part II.A$'$ (`PART-II-A2-STANDARD.md`)
as II.A$'$, Part II.B (`PART-II-B-DYNAMICS.md`) as II.B, Part II.C (`PART-II-C-OPERATORS.md`) as II.C and Part II.C$'$
(`PART-II-C2-TRAPPING.md`) as II.C$'$.

*Method.* Every estimate here is a positive commutator estimate. II.A$'$ section 4 provides the machinery with
coefficients of finite regularity: one step with a regulariser (its Lemma 4.1) and the iteration in the order (its Lemma
4.2). Two additions are made in section 2: a term $JL$ in the commutator inequality, which a cut-off to the
characteristic set produces (Lemma 2.1), and bounds of microlocal norms through symbols (Lemmas 2.4-2.5), with which the
norms produced by different commutators are compared. With these, each radial estimate is a computation of symbols at a
radial set of II.B. Weights and fibre inner products enter through the subprincipal symbol of a conjugated operator
(Lemma 1.1), and the thresholds are those of II.C and I.A. At $\mathscr I^+$ the subprincipal symbol is computed in Lemma
3.4, which is [Hin26c] (7.22) at $n = 4$: the constant $3 = n-1$ of II.C Lemma 3.4 is exactly the one that makes the
leading part of the operator symmetric for $|dt\,dx|$. The source quotes its estimate at the trapped set from [Hin21]
Theorem 3.9 (P. Hintz, *Normally hyperbolic trapping on asymptotically stationary spacetimes*, arXiv:1811.07843v1), whose
proof writes out the regularisation of its first step and sketches that of the others. Section 4 proves the estimate in
full in the present calculus, from the hypersurfaces of II.C$'$: an equation with damping for the unstable defining
function, two quantitative propagation estimates, and their combination, all with one regulariser and by induction on the
order in half steps.

*How it is organised.* Section 1: the setting and the statement, Theorem 1.2. Section 2: the commutator lemmas. Section
3: the radial point estimates. Section 4: the estimate at the trapped set. Section 5: the proof of Theorem 1.2. Section
6: findings.

## 1. Setting

### 1.1 The operators

$g_0$ is the stationary metric of II.B section 1.1, which satisfies (K1)-(K4) together with Part I's (H1)-(H8), and $P_0$
is a stationary wave-type operator for $g_0$ (II.C Definition 1.1). Fix $\ell_I\in(0,\frac12]$, $\ell_+\in(0,1]$ and
$\ell_K>0$. $P$ is a weakly admissible wave-type operator relative to $P_0$ of class $((d_0;0),(2\ell_I,\ell_+,\ell_K))$
(II.C Definition 3.3), and $\epsilon_P := \|P-P_0\|_{(d_0;0),(2\ell_I,\ell_+,\ell_K)}$ (II.C Definition 3.6). Only
$\ell_I\in(0,\frac12]$, $\ell_+>0$, $\ell_K>0$ are used: the conditions (5.23) of the source play no part in microlocal
regularity ([Hin26c] p. 115). The metric $g = g_0+h$ of $P$ has $\|h\|\le C\epsilon_P$ (II.C Lemma 3.7). So, for
$\epsilon_P$ small, the time function $t^\flat_*$ of II.C Lemma 3.2 and the domain $\Omega_* :=
\mathrm{cl}_M\{t^\flat_*\ge1\}$ (II.C section 3), the global dynamics of II.C section 4 and the hypersurfaces of II.C$'$
Proposition 3.4 are available (the norm of $h$ in $\tilde{\mathcal G}^{d_0,(0,0,\ell_K)}_{e3b}$ is at most a constant
times $\epsilon_P$). Over $\mathscr I^+$, $t^\flat_* = t_*$ (II.C Lemma 3.2 (a)). $d_0$ is taken large where needed,
depending only on the orders.

Put $W := x_I^2\rho_+^2$ and $L := W^{-1}P$. By II.C Lemma 1.4 (b) and (3.2), $L = L_0+L_1+L_2$ is of the form of II.A$'$
section 5.1 with $m = 2$: $L_0$ is the scalar part of $W^{-1}P_0$, $L_1$ the second-order part of $W^{-1}\tilde P$, whose
coefficients lie in $C^{d_0,(2\ell_I,\ell_+,\ell_K)}_{e3b}$, and $L_2$ is of first order. $L_2$ contains the first-order
part of $W^{-1}P_0$, the terms $\chi_I(\tilde p_1(x_I\partial_{x_I}-2\rho_+\partial_{\rho_+})+\frac12p_0)$ of II.C (3.2),
whose coefficients need not decay at $\mathscr I^+$, and the rest of $W^{-1}\tilde P$. The principal symbol of $L$ is
$\ell := W^{-1}G = G_{e3b}$, real and scalar, and $\mathsf H := \rho_\infty H_\ell$ is the field $\mathsf H_G$ of II.C
(4.2).

Near a set $O$ where another positive weight $W'$ has $W/W'$ and $W'/W$ smooth with bounded e3b-derivatives, we use $L'
:= W'^{-1}P = (W/W')L$ in place of $L$. For $G$ microsupported over $O$, $\|GL'u\|_{\mathsf t}$ and $\|GLu\|_{\mathsf t}$
then differ by lower-order terms only. We take $W' = 1$ near the horizon and the trapped set, over $(K^+)^\circ$, where
$W$ is smooth and positive; $W' = \rho_+^2 = r^{-2}$ near $\partial K^+$, where $x_I$ is smooth and positive; and $W' =
W$ near $\mathscr I^+$. The rescaled fields $\rho H_{W'^{-1}G}$ are then those of II.B: $\rho_\infty H_G$ with
$\rho_\infty$ of (H3) near the horizon (II.B section 4), $\sigma^{-1}H_G$ near the trapped set (II.B section 5),
$-\sigma_{3b}^{-1}H_{G_{3b}}$ near $\partial K^+$ (II.B (3.3)-(3.4)), and $\sigma_{eb}^{-1}H_{G_{eb}}$ near $\mathscr
I^+$ (II.B (7.3)-(7.4)).

### 1.2 Weights, inner products and the conjugated operator

For weights $(\alpha_I,\alpha_+,\alpha_K)$ put $w := x_I^{2\alpha_I}\rho_+^{\alpha_+}\rho_K^{\alpha_K}$; then $H^{\mathsf
s,(2\alpha_I,\alpha_+,\alpha_K)}_{e3b} = wH^{\mathsf s}_{e3b}$, with $H^{\mathsf s}_{e3b}$ based on $L^2(|dt\,dx|)$ (II.A
section 4.2). Near $\partial K^+$ we use $\rho_K = r/t_*$ and $\rho_+ = r^{-1}$, near $(K^+)^\circ$ $\rho_K = t_*^{-1}$,
and near $\mathscr I^+$ $\rho_+ = t_*^{-1}$ (II.B section 3.1). A fibre inner product $h$ on $\mathbb C^N$ over a set
$O$, smooth with bounded e3b-derivatives, is written $h(v,v') = \langle A^{-1}v,A^{-1}v'\rangle$ with $A := \mathsf
G^{-1/2}$, $\mathsf G$ the Gram matrix of $h$. Adjoints and $\mathrm{Im}_h$ are taken for $|dt\,dx|$ (II.C section 1.1).

**Lemma 1.1 (the conjugated operator).** Let $W'$ be a weight as in section 1.1 on $O$, $L' := W'^{-1}P$, $\ell' :=
W'^{-1}G$, and $L'' := A^{-1}w^{-1}L'wA$. (a) $L''$ is of the form of II.A$'$ section 5.1 on $O$, with principal symbol
$\ell'$ and coefficient norms bounded by those of $L'$ times constants depending only on $w$ and $A$. (b)
$\sigma_1(\mathrm{Im}\,L'') = A^{-1}\big(\sigma_1(\mathrm{Im}_hL')-H_{\ell'}\log w\big)A$, where $\mathrm{Im}$ is taken
for the standard inner product. (c) $\sigma_1(\mathrm{Im}_hL') = W'^{-1}\sigma_1(\mathrm{Im}_hP)-\frac12H_{\ell'}\log
W'$. Hence, for any positive $\rho$ homogeneous of degree $-1$, with $\mathsf H' := \rho H_{\ell'}$ and $\mathfrak p' :=
\rho W'^{-1}\sigma_1(\mathrm{Im}_hP)$,
$$\rho\,\sigma_1(\mathrm{Im}\,L'') = A^{-1}\big(\mathfrak p'-\tfrac12\mathsf H'\log W'-\mathsf H'\log w\big)A.\tag{1.1}$$

*Proof.* (a) $w^{-1}Vw = V+V(\log w)$ for a vector field $V$, and for $V\in\mathcal V_{e3b}\subset\mathcal V_b$, $V\log
w$ is smooth with bounded e3b-derivatives, $w$ being a product of powers of boundary defining functions; likewise for
$A$. So the coefficients of $L''$ are those of $L'$ multiplied and differentiated as stated, and its second-order part is
$L'$'s. (b) $w^{-1}L'w = L'+w^{-1}[L',w]$, and $[L',w]$ is of first order with principal symbol $-iH_{\ell'}w$; so
$w^{-1}L'w = L'-iX$ modulo order 0, with $X$ of real principal symbol $H_{\ell'}\log w$. As $w$ is real and scalar,
$(w^{-1}L'w)^{*h} = wL'^{*h}w^{-1} = L'^{*h}+iX'$ modulo order 0, with $\sigma(X') = H_{\ell'}\log w$, since
$\sigma([L'^{*h},w^{-1}]) = -iH_{\ell'}w^{-1} = iw^{-2}H_{\ell'}w$. Hence $\sigma_1(\mathrm{Im}_h(w^{-1}L'w)) =
\sigma_1(\mathrm{Im}_hL')-H_{\ell'}\log w$. Next, for any operator $M$, $M^{*h} = \mathsf G^{-1}M^*\mathsf G$ with
$\mathsf G = A^{-*}A^{-1}$, so $A^{-1}M^{*h}A = A^*M^*A^{-*} = (A^{-1}MA)^*$, and $\mathrm{Im}(A^{-1}MA) =
A^{-1}(\mathrm{Im}_hM)A$ exactly. (c) $\mathrm{Im}_h(fP) = f\,\mathrm{Im}_hP-\frac1{2i}[P^{*h},f]$ for a real function
$f$, and $\sigma([P^{*h},f]) = -iH_Gf$, so $\sigma_1(\mathrm{Im}_h(fP)) = f\sigma_1(\mathrm{Im}_hP)+\frac12H_Gf$. With $f
= W'^{-1}$, $\frac12H_GW'^{-1} = -\frac12W'^{-1}H_G\log W'$, and $W'^{-1}H_G\log W' = H_{\ell'}\log W'$ exactly, as
$H_{\ell'} = W'^{-1}H_G+GH_{W'^{-1}}$ and the Hamilton field of a function of the base annihilates functions of the base.
(1.1) follows on multiplying by $\rho$. $\square$

The estimates for $L''$ on $\tilde u := A^{-1}w^{-1}u$ in unweighted spaces are estimates for $u$ in the weighted spaces:
for $B\in C^\infty_b\Psi^0_{e3b}$, $w^{-1}Bw$ and $A^{-1}BA$ differ from $B$ by operators of order $-1$ ((S11) of II.A,
and II.A$'$ Proposition 2.4), and $A^{-1}w^{-1}W'^{-1}Pu = L''\tilde u$.

### 1.3 The radial sets and the standing choices

On $\partial\Sigma^+$ the future field is $\mathsf H$, on $\partial\Sigma^-$ it is $-\mathsf H$ (II.C section 2.3). We
use the sets of II.B: the horizon radial set $\partial R_{\mathcal H^+}$ (Definition 4.1), the radial sets $\partial
R_{\partial K^+,\mathrm{in/out}}$ over $\partial K^+$ (Definition 3.1), $\partial R_{\mathscr I^+,\mathrm{in},+}$ and
$\partial R_{\mathscr I^+,\mathrm{out}}$ (Definition 7.1), the trapped set $\partial\Gamma_{K^+}$ and the stable and
unstable sets $\Gamma^{u/s}_{K^+}$, $\partial\bar\Gamma^{u/s}_{K^+}$ (Definition 5.1), and $\partial W_{\mathrm{in/out}}$
over $\iota^+$ (Lemmas 3.2-3.3). By II.C Lemma 4.1, the characteristic set and $\mathsf H$ of $P$ agree with those of
$P_0$ over $\partial M$, and near it $\mathsf H_G-\mathsf H_{G_0}\in\epsilon_PwC^{d_0-1}\mathcal V_b$ with $w =
x_I^{2\ell_I}\rho_+^{\ell_+}\rho_K^{\ell_K}$.

Fix, as in [Hin26c] (7.1)-(7.2), radii $r_0<r_1<r_1^+<r^\natural$, with $r^\natural = \frac12(r_0+r_2)$ of II.C Lemma
3.2, so that $dr$ is future timelike on $\{r_0\le r\le r^\natural\}$, and $\chi\in C^\infty(\Omega_*)$ with
$$\chi = 0\ \text{on}\ (t^\flat_*)^{-1}([1,2])\cup r^{-1}([r_0,r_1]),\qquad\chi =
1\ \text{on}\ \{t^\flat_*\ge3\}\cap\{r\ge r_1^+\}.\tag{1.2}$$
Fix weights ([Hin26c] (7.3))
$$\alpha_I<-\tfrac12+\bar p_1,\qquad\alpha_+<\alpha_I-\tfrac12,\qquad\alpha_K\in\mathbb R,\tag{1.3}$$
with $\bar p_1$ of II.C Definition 3.5, and order functions $\mathsf s_0<\mathsf s$, admissible for $P_0$ with weights
$\alpha_+$, $\alpha_K$ and margin 0 (II.C Definition 5.2, produced by its Proposition 5.1). In particular $\mathsf s$ and
$\mathsf s_0$ are constant near each radial set and near the trapped set (II.C Definition 2.4 (3)-(6) and Proposition 5.1
(5)), and they satisfy there the thresholds of II.C Definition 2.4 with margin 0.

**Theorem 1.2 ([Hin26c] Proposition 7.1 at $n = 4$).** There is $C$ such that
$$\|\chi u\|_{H^{\mathsf s,(2\alpha_I,\alpha_+,\alpha_K)}_{e3b}}
\le C\Big(\|Pu\|_{H^{\mathsf s,(2\alpha_I+2,\alpha_++2,\alpha_K)}_{e3b}(\Omega_*;E)^{\bullet,-}}+
\|u\|_{H^{\mathsf s_0,(2\alpha_I,\alpha_+,\alpha_K)}_{e3b}(\Omega_*;E)^{\bullet,-}}\Big)\tag{1.4}$$
for $P = P_0$, in the strong sense: if the right side is finite, so is the left, and (1.4) holds. There is $d_0$,
depending only on $\mathsf s_0$ and $\mathsf s$, such that (1.4) holds also for every weakly admissible wave-type
operator $P$ relative to $P_0$ with $\epsilon_P$ small, with $C$ uniform.

The estimate loses one derivative: $Pu$ is measured in $H^{\mathsf s}$, where real principal type propagation would need
only $H^{\mathsf s-1}$. The loss comes from the trapped set (Proposition 4.2). The spaces are those of II.A section 7:
$u$ is supported at the initial hypersurface $\{t^\flat_* = 1\}$ and extendible at the final one in $\{r = r_0\}$.
Extended by zero, $u$ is a distribution on $M$ supported in $\{t^\flat_*\ge1\}$, and so is $Pu$.

*Remark 1.3 ([Hin26c] Remark 7.2).* The constants below depend on the stationary model only through finitely many norms
of its coefficients and through the dynamical constants of II.B and II.C$'$, which are uniform for the stationary models
of parameters $b$ near $b_0$ (II.B Remark 8.3, II.C Proposition 5.1 (4), II.C$'$ Proposition 3.4). So (1.4) holds
uniformly also when $P_0$ is replaced by those models, or perturbed within the stationary wave-type operators. The
source's Remark 7.3, on large perturbations of $P_0$, is not used and not proved here.

## 2. Commutator lemmas

In this section $L$ is any operator of the form of II.A$'$ section 5.1, possibly on $\mathbb C^{N'}$, with real scalar
principal symbol $\ell$ of order $m$. $L_R$, $L_I$ and $C_{\check a}$ are those of II.A$'$ (4.1), $\ell_I$ is the
principal symbol of $L_I$ (an Hermitian matrix of order $m-1$), norms are those of $H^{\mathsf t}_{e3b}$, and $B,E,G,J$
are carried by $\chi$ (II.A section 8.3). For a positive symbol $\rho$, homogeneous of degree $-1$ near fibre infinity,
and $\kappa>0$, the regulariser is $\varphi_\epsilon := (1+\epsilon\rho^{-1})^{-\kappa}$, $\epsilon\in(0,1]$, and
$\theta_\epsilon := \epsilon\rho^{-1}(1+\epsilon\rho^{-1})^{-1}$; II.A$'$ (2.1) holds with $\rho$ in place of
$\rho_\infty$, and $\varphi_\epsilon$ has the properties stated after it.

**Lemma 2.1 (one step with a characteristic cut-off).** Let (i)-(ii) of II.A$'$ Lemma 4.1 hold, and in place of its (iii)
the following: there are real scalar symbols $j_\epsilon$, bounded in $C^{(M)}_\nu\tilde S^{2\mathsf s-m}$ and, for each
$\epsilon$, in $C^{(M)}_\nu\tilde S^{2\mathsf s-m-2\kappa}$, supported in $K_1$, such that for every $w\in H^{K'}_{e3b}$
carried by $\chi$, with $J_\epsilon := \mathrm{Op}(j_\epsilon)$,
$$\varsigma\langle C_{\check a_\epsilon}w,w\rangle\le-\|B_\epsilon w\|^2+\|E_\epsilon w\|^2+2\,
\mathrm{Re}\langle J_\epsilon Lw,w\rangle+C_0\big(\|G'w\|^2_{\mathsf s-\frac12+\delta_0}+
\|\chi w\|^2_{-N}\big).\tag{2.1}$$
Then the conclusion (4.3) of II.A$'$ Lemma 4.1 holds.

*Proof.* As II.A$'$ Lemma 4.1, with two additions. In Step 1, for fixed $\epsilon$, $\langle J_\epsilon
Lw_t,w_t\rangle\to\langle J_\epsilon Lv,v\rangle$ as $t\to0$: $w_t\to v$ in $H^{\mathsf s-\kappa}$, so $Lw_t\to Lv$ in
$H^{\mathsf s-\kappa-m}$, and $J_\epsilon^*w_t\to J_\epsilon^*v$ in $H^{-\mathsf s+m+\kappa}$, $J_\epsilon^*$ having
order $2\mathsf s-m-2\kappa$ for this $\epsilon$ without loss (II.A$'$ Proposition 2.4 (a), (c)). In Step 2 the new term
is bounded at $v = \Phi u$: $Lv = \Phi Lu+[L,\Phi]u$, and $J_\epsilon[L,\Phi]$ has every order uniformly, by Proposition
2.4 (e), as in Step 0; and $|\langle\Phi Lu,J_\epsilon^*v\rangle|\le\|\Phi Lu\|_{\mathsf
s-m+1}\|J_\epsilon^*v\|_{-\mathsf s+m-1}$. $J_\epsilon^*$ is uniformly of order $2\mathsf s-m+\delta$ for every
$\delta>0$ and microsupported in $K_1$, so $\|J_\epsilon^*v\|_{-\mathsf s+m-1}\le C(\|Gu\|_{\mathsf s-1+\delta}+\|\chi
u\|_{-N})$. With $\delta\le\frac12$ and Step 0, $2|\langle J_\epsilon Lv,v\rangle|\le C(\|GLu\|^2_{\mathsf
s-m+1}+\|Gu\|^2_{\mathsf s-\frac12+\delta_0}+\|\chi u\|^2_{-N})$, which is of the form of the right side of (4.3).
$\square$

**Lemma 2.2 (iteration).** II.A$'$ Lemma 4.2 holds with Lemma 2.1 in place of II.A$'$ Lemma 4.1, with the same proof.
$\square$

**Lemma 2.3 (from a symbol identity to (2.1)).** Let $s$ be a constant order, $k := s-\frac12(m-1)$, $\check a\in
C^{(M+2)}\tilde S^k$ real and scalar, supported in a compact set $K_1$ near fibre infinity, and $\check a_\epsilon :=
\varphi_\epsilon\check a$. Suppose that near fibre infinity
$$\varsigma\big(H_\ell(\check a_\epsilon^2)+2\check a_\epsilon^2\ell_I\big) =
-b_\epsilon^*b_\epsilon-\sum_jb'^*_{j,\epsilon}b'_{j,\epsilon}+\sum_ie^*_{i,\epsilon}e_{i,\epsilon}+j_\epsilon\ell+
f_\epsilon,\tag{2.2}$$
with matrix symbols $b_\epsilon$, $b'_{j,\epsilon}$, $e_{i,\epsilon}$ bounded in $C^{(M+2)}\tilde S^s$ and lying in
$C^{(M+2)}\tilde S^{s-\kappa}$ for each $\epsilon$, scalar $j_\epsilon$ as in Lemma 2.1 (with $\nu = 0$), and
$f_\epsilon$ bounded in $C^{(M+2)}\tilde S^{2s-1}$, all supported in $K_1$. Then (2.1) holds with $B_\epsilon :=
\mathrm{Op}(b_\epsilon)$, $E_\epsilon := \mathrm{Op}(e_\epsilon)$ for the column $e_\epsilon$ of the $e_{i,\epsilon}$,
$J_\epsilon := \frac12\mathrm{Op}(j_\epsilon)$ and $\delta_0 = 0$; $C_0$ depends on finitely many norms of the symbols.

*Proof.* With constant orders and index 0, the remainders of II.A$'$ Proposition 2.4 (b)-(f) have exact orders. As in the
paragraph *The commutator* of the proof of II.A$'$ Proposition 5.3, $i[L_R,\check A_\epsilon^*\check A_\epsilon] =
\mathrm{Op}(H_\ell(\check a_\epsilon^2))+R_1$ with $R_1$ of order $2s-1$. The operator $L_I\check A_\epsilon^*\check
A_\epsilon+\check A_\epsilon^*\check A_\epsilon L_I-\mathrm{Op}(2\check a_\epsilon^2\ell_I)$ is an expression in
quantisations whose principal symbol vanishes at order $2s$, $\check a_\epsilon$ being scalar. So by Proposition 2.4 (f)
it has order $2s-1$. Hence $\varsigma C_{\check a_\epsilon}$ is the quantisation of the right side of (2.2) plus an
operator of order $2s-1$. By Proposition 2.4 (b), (c), $\mathrm{Op}(b^*b) = \mathrm{Op}(b)^*\mathrm{Op}(b)$ modulo order
$2s-1$, and $\mathrm{Op}(j\ell) = \mathrm{Op}(j)L$ modulo order $2s-1$, as $L = \mathrm{Op}(\ell_f)+R_L$ with
$\ell_f-\ell$ of order $m-1$. All remainders are uniform in $\epsilon$ and have a factor supported in $K_1$, so paired
with $w$ they are at most $C(\|G'w\|^2_{s-\frac12}+\|\chi w\|^2_{-N})$ (Proposition 2.4 (e)). $\langle C_{\check
a_\epsilon}w,w\rangle$ is real, so taking real parts and dropping $-\sum_j\|\mathrm{Op}(b'_j)w\|^2$ gives (2.1).
$\square$

**Lemma 2.4 (norms through symbols).** Let $q\in C^{(M)}\tilde S^0$ be matrix-valued and supported in a compact set $K_1$
near fibre infinity, and $M_q := \sup|q|$, the supremum of the operator norm. For every $\eta>0$ there is $C_\eta$,
depending on $q$ through finitely many norms, such that for $w\in L^2$ carried by $\chi$
$$\|\mathrm{Op}(q)w\|\le(M_q+\eta)\|w\|+C_\eta\big(\|G'w\|_{-\frac12}+\|\chi w\|_{-N}\big),\tag{2.3}$$
with $G'$ elliptic on $K_1$.

*Proof.* $(M_q+\eta)^2-q^*q\ge\eta^2$, so its positive square root $c$ lies in $C^{(M)}\tilde S^0$ (II.A$'$ Lemma 2.5
(i), for positive definite matrices), and $c-(M_q+\eta)$ is supported in $K_1$. By II.A$'$ Proposition 2.4 (b), (c),
$\mathrm{Op}(c)^*\mathrm{Op}(c) = (M_q+\eta)^2-\mathrm{Op}(q)^*\mathrm{Op}(q)+R$, with $R$ of order $-1$ and
microsupported in $K_1$, as every symbol involved is constant off $K_1$ and the quantisation of a constant is the
identity modulo operators of every order. Hence $\|\mathrm{Op}(q)w\|^2\le(M_q+\eta)^2\|w\|^2+|\langle Rw,w\rangle|$, and
$|\langle Rw,w\rangle|\le C_\eta(\|G'w\|^2_{-\frac12}+\|\chi w\|^2_{-N})$. $\square$

The pairing identities used below hold at the distributions considered: if $G'v\in H^{s-\frac12}$, $G'Lv\in
H^{s-m+\frac12}$ for $G'$ elliptic on $K_1$ and $\chi v\in H^{-N}$, and $\kappa\ge2$, then $\langle C_{\check
a_\epsilon}v,v\rangle = 2\,\mathrm{Im}\langle\check A_\epsilon Lv,\check A_\epsilon v\rangle$ for each $\epsilon>0$, by
Step 1 of the proof of II.A$'$ Lemma 4.1 (the regularised commutant has order $k-\kappa\le k-2$).

**Lemma 2.5 (comparison of norms).** Let $\mathsf t$ be a constant and $z,x_1,\dots,x_m\in C^{(M)}\tilde S^0$
matrix-valued and supported in a compact set $K_1$ near fibre infinity, and suppose that $z = \sum_iq_ix_i$ on a
neighbourhood of $\mathrm{supp}\,z$, with $q_i\in C^{(M)}\tilde S^0$ and $M_i := \sup|q_i|$. This holds with $M_i =
c_*^{-1/2}$ if $|z|\le1$ and $\sum_ix_i^*x_i\ge c_*>0$ on a neighbourhood $V$ of $\mathrm{supp}\,z$. Then for every
$\eta>0$ there is $C_\eta$, independent of $\epsilon\in(0,1]$ and depending on the symbols through finitely many norms,
such that for $w\in H^{K'}_{e3b}$ carried by $\chi$
$$\|\mathrm{Op}(\rho^{-\mathsf t}\varphi_\epsilon z)w\|\le\sum_i(M_i+
\eta)\|\mathrm{Op}(\rho^{-\mathsf t}\varphi_\epsilon x_i)w\|+C_\eta\big(\|G'w\|_{\mathsf t-\frac12}+\|\chi w\|_{-N}\big),
\tag{2.4}$$
with $G'$ elliptic on $K_1$. If $\kappa\ge\frac12$, (2.4) holds also for $w$ with $G'w\in H^{\mathsf t-\frac12}$ and
$\chi w\in H^{-N}$: for fixed $\epsilon$ both sides are then finite and continuous in $w$, and II.A$'$ Lemma 2.3 (b)
approximates $w$.

*Proof.* Replacing $q_i$ by $\zeta q_i$, with $\zeta$ equal to 1 near $\mathrm{supp}\,z$ and supported in the
neighbourhood, $z = \sum_iq_ix_i$ everywhere. By II.A$'$ Proposition 2.4 (b), $\mathrm{Op}(\rho^{-\mathsf
t}\varphi_\epsilon z) = \sum_i\mathrm{Op}(q_i)\mathrm{Op}(\rho^{-\mathsf t}\varphi_\epsilon x_i)+R_\epsilon$, with
$R_\epsilon$ uniformly of order $\mathsf t-1$ and microsupported in $K_1$. Lemma 2.4 applied to $\mathrm{Op}(q_i)$ and
$\mathrm{Op}(\rho^{-\mathsf t}\varphi_\epsilon x_i)w$ gives (2.4), as $\|G'\mathrm{Op}(\rho^{-\mathsf t}\varphi_\epsilon
x_i)w\|_{-\frac12}\le C(\|G''w\|_{\mathsf t-\frac12}+\|\chi w\|_{-N})$. In the particular case put $X := \sum_jx_j^*x_j$
and $q_i := \zeta zX^{-1}x_i^*$ with $\zeta$ supported in $V$. Then $\sum_iq_ix_i = \zeta z = z$ and $\sum_iq_iq_i^* =
\zeta^2zX^{-1}z^*\le c_*^{-1}$, so $|q_i|\le c_*^{-1/2}$. $\square$

In Lemma 2.3 and in II.A$'$ Lemmas 4.1-4.2, $L$ enters only through $L = \mathrm{Op}(\ell_f)+R_L$, with $\ell_f\in
C^{(d_0)}\tilde S^m$ (matrix-valued, with real scalar principal part $\ell$) and $R_L$ bounded of every order. So they
hold for operators of that form, such as $L$ plus the quantisation of a first-order symbol of finite regularity. We use
this in section 4.

The iteration of II.A$'$ Lemma 4.2 uses its hypotheses only at the orders $\mathsf s_j = \mathsf s-\tau+j\kappa$ with the
exponent $\kappa = \tau/J$, for which the effective orders $\mathsf s_j-\kappa\theta_\epsilon$ of the regularised
commutant lie in $[\mathsf s-\tau,\mathsf s]$. So in Lemma 2.2 it suffices that the hypotheses hold for orders $\mathsf
s'$ and exponents $\kappa$ with $\mathsf s-\tau\le\mathsf s'-\kappa$ and $\mathsf s'\le\mathsf s$. This is what makes
thresholds compatible with the regularisation.

## 3. Radial point estimates

Each estimate below is proved by the same steps; we write them once.

*The pattern.* (1) Near the radial set $R$, a local operator $L' := W'^{-1}P$ (section 1.1) is conjugated to $L'' :=
A^{-1}w^{-1}L'wA$ (Lemma 1.1), acting on $\tilde u := A^{-1}w^{-1}u$, with $A$ the frame of a fibre inner product chosen
for $R$. (2) The commutant is $\check a := \rho^{-s+\frac12}\Psi\chi_\infty$, with $s$ the (constant) order, $\rho$ the
function of section 1.1 for $R$, $\Psi$ a product of cut-offs, and $\chi_\infty$ a function of $\rho$ equal to 1 near
fibre infinity and supported where the coordinates are defined, whose derivatives are of order $-\infty$ and are put into
$f_\epsilon$; it is regularised by $\varphi_\epsilon$ with the same $\rho$. (3) With $s_\epsilon :=
s-\kappa\theta_\epsilon\in[s-\kappa,s]$, II.A$'$ (2.1) and (1.1) give, where $\chi_\infty = 1$,
$$H_\ell(\check a_\epsilon^2)+2\check a_\epsilon^2\ell_I = \rho^{-2s}\varphi_\epsilon^2\big(-\Psi^2Q_\epsilon+
\mathsf H(\Psi^2)\big),\qquad Q_\epsilon :=
(2s_\epsilon-1)\rho^{-1}\mathsf H\rho-2A^{-1}\big(\mathfrak p'-\tfrac12\mathsf H\log W'-\mathsf H\log w\big)A,\tag{3.1}$$
with $\ell = W'^{-1}G$, $\mathsf H = \rho H_\ell$ and $\mathfrak p' = \rho W'^{-1}\sigma_1(\mathrm{Im}_hP)$. Indeed
$H_\ell = \rho^{-1}\mathsf H$, $\mathsf H(\rho^{-2s+1}\varphi_\epsilon^2) =
-(2s_\epsilon-1)\rho^{-2s+1}\varphi_\epsilon^2\rho^{-1}\mathsf H\rho$, and $2\rho\ell_I = 2A^{-1}(\cdots)A$ by (1.1). (4)
At $R$, $Q_\epsilon\ge2c$ for some $c>0$ and all $s_\epsilon$ in the range of the iteration, by the threshold; so
$Q_\epsilon\ge c$ on $\mathrm{supp}\,\Psi$ once the cut-offs are localised close to $R$, and
$-\Psi^2Q_\epsilon\rho^{-2s}\varphi_\epsilon^2 = -b_\epsilon^*b_\epsilon$ with $b_\epsilon :=
\rho^{-s}\varphi_\epsilon\Psi Q_\epsilon^{1/2}$ (II.A$'$ Lemma 2.5 (i)), and $\check a_\epsilon = z_\epsilon b_\epsilon$,
$z_\epsilon := \rho^{\frac12}Q_\epsilon^{-1/2}$ (with $Q_\epsilon$ replaced by $c$, smoothly, off a neighbourhood of
$\mathrm{supp}\,\Psi$). (5) $\mathsf H(\Psi^2)$ is a sum of terms $2\mathfrak M\psi\psi'(\mathfrak Mf)\,\mathsf
Hf\cdot(\text{other factors})^2$, one for each factor $\psi(\mathfrak Mf)$ of $\Psi$, where $\psi$ is the cut-off of
II.A$'$ section 5.2: even, supported in $(-1,1)$, equal to 1 on $[-\frac12,\frac12]$, non-increasing on $[0,\infty)$,
with $-\psi\psi'$ the square of a smooth function on $[0,\infty)$. Where $\mathsf Hf>0$ on the support of
$\psi'(\mathfrak Mf)$ the term is $-b'^*b'$; where $\mathsf Hf<0$ it is $+e^*e$, and its support determines $E$. A factor
$\psi(\mathfrak M_\Sigma\rho^2\ell)$, a cut-off to the characteristic set, contributes $j_\epsilon\ell$, since $\mathsf
H(\rho^2\ell) = 2(\rho^{-1}\mathsf H\rho)\rho^2\ell$, $\mathsf H\ell$ being 0. (6) Lemma 2.3 gives (2.1) for $L''$,
Lemmas 2.1-2.2 give the estimate for $\tilde u$ with $\Gamma := R$ and $\tau := s-s_0$, and section 1.2 returns it to
$u$.

The constants depend on $P$ through finitely many norms of the coefficients of $L''$, and through $c$ and the signs in
(5). These hold with margins at $R$, where the quantities are those of the normal form of $P$ (the second-order part of
$P-P_0$ vanishes at the face containing $R$), and near $R$ they change by $O(\epsilon_P)$ (II.C Lemma 4.1). So the
cut-offs chosen for $P_0$ serve for every $P$ with $\epsilon_P$ small, and the estimates hold uniformly, with $d_0$ fixed
by the regularity that Lemmas 2.1-2.3 and II.A$'$ Proposition 2.4 need at the orders involved. We prove the estimates on
$\partial\Sigma^+$. On $\partial\Sigma^-$ the future field is $-\mathsf H$, $\varsigma = -1$, and the antipodal map
exchanges the two components. $G$ is even, and $\sigma_1(\mathrm{Im}_hP)$ is odd in the covector, so $\varsigma\mathfrak
p'$ and every threshold are the same there. Throughout, $B,E,G\in C^\infty_b\Psi^0_{e3b}$ are carried by $\chi$, and
"strong sense" means: if the right side is finite, so is the left, and the estimate holds.

**Proposition 3.1 ([Hin26c] Proposition 7.4 at $n = 4$; the horizon).** There are $B,E,G$ such that (1) their operator
wave front sets lie in any fixed neighbourhood $U$ of $\partial R_{\mathcal H^+}$; (2) their Schwartz kernels are
supported in $K\times K$ for any fixed compact neighbourhood $K\subset M$ of $\mathcal H^+\cap K^+ = \{r = r_h,\rho_K =
0\}$; (3) $B$ is elliptic at $\partial R_{\mathcal H^+}$; (4) the Schwartz kernel of $E$ is supported in $(K\setminus
K^+)^2$; and such that for all constants $s>s_0>\frac12+\vartheta_{\mathcal H}$ (I.A (1.5)), $\alpha_K\in\mathbb R$, and
$\tilde\chi\in C^\infty(M)$ supported near $K$ and equal to 1 near $K$,
$$\|Bu\|_{H^{s,\alpha_K}}\le C\big(\|GPu\|_{H^{s-1,\alpha_K}}+\|Eu\|_{H^{s,\alpha_K}}+
\|\tilde\chi u\|_{H^{s_0,\alpha_K}}\big)\tag{3.2}$$
in the strong sense, for $P = P_0$ and every $P$ with $\epsilon_P$ small, with $d_0$ depending only on $s,s_0$. Here
$H^{s,\alpha_K} := H^{s,(2\alpha_I,\alpha_+,\alpha_K)}_{e3b}$ over $K$, where $x_I$ and $\rho_+$ are smooth and positive,
so that $\alpha_I,\alpha_+$ do not matter.

*Proof.* $W' := 1$, $\rho$ the function of (H3) (extended positive, even and homogeneous of degree $-1$), $\mathsf H =
\rho H_G$, $w := \rho_K^{\alpha_K}$ with $\rho_K = t_*^{-1}$, and $A$ the frame of an inner product for which
$\vartheta_{\mathcal H}$ of I.A (1.5) is attained ($\vartheta_{\mathcal H}$ is the supremum of
$\lambda_{\max}(\beta_0^{-1}p_{1,+}(0))$ over $\partial\mathcal R_+$, with $p_{1,+}(0) = \rho\sigma_1(\mathrm{Im}_h\hat
P(0))$). $\partial R_{\mathcal H^+}$ lies over $K^+$ in $\{\sigma = 0\}$, where $\sigma_1(\mathrm{Im}_hP_0) =
\sigma_1(\mathrm{Im}_h\hat P(0))$ (II.C section 2.3), and $P-P_0$ has coefficients vanishing at $K^+$; so $\mathfrak p' =
p_{1,+}(0)$ there. By II.B (4.1), $\rho^{-1}\mathsf H\rho = \beta_0$ and $\rho_K^{-1}\mathsf H\rho_K =
\rho_K(\rho_K^{-2}\mathsf H\rho_K) = 0$ at $\partial R_{\mathcal H^+}$. So at $\partial R_{\mathcal H^+}$, as
$A^{-1}\mathfrak p'A$ has the eigenvalues of the $h$-self-adjoint $\mathfrak p'$,
$$Q_\epsilon = (2s_\epsilon-1)\beta_0-2A^{-1}\mathfrak p'A\ge(2s_\epsilon-1-2\vartheta_{\mathcal H})\beta_0
\ge(2s_0-1-2\vartheta_{\mathcal H})\inf\beta_0 =: 2c>0$$
for $s_\epsilon\ge s_0$, which is the range of the iteration (Lemma 2.2 and the remark after Lemma 2.5).

Let $F = \tilde q+K\hat\sigma^2$ be the quadratic defining function of II.B Lemma 4.2, with $\mathsf HF\ge c_FF$ on a
neighbourhood $W$ of $\partial R_{\mathcal H^+}$ in ${}^{3b}S^*_{(K^+)^\circ}M_0$. $F$ does not depend on $t_*$, and the
field of $P_0$ is invariant under $t_*$-translations, so $\mathsf H_{P_0}F\ge c_FF$ on $W\times\{\rho_K\le\rho_0\}$. For
$P$, $\mathsf H-\mathsf H_{P_0} = O(\epsilon_P\rho_K^{\ell_K})$ in $C^{d_0-1}$, and $|dF|\le CF^{1/2}$, so $\mathsf
HF\ge\frac12c_FF$ where $F\ge(2\mathfrak M_R)^{-1}$ and $\rho_K\le\mathfrak M^{-1}$, for $\mathfrak M$ large given
$\mathfrak M_R$. As $F$ is defined only on $W$, extend it to a smooth $t_*$-independent function bounded below by a
positive constant outside a smaller $t_*$-invariant neighbourhood $W'$ of $\partial R_{\mathcal H^+}$ with closure in
$W$; for $\mathfrak M_R$ large, $\psi(\mathfrak M_RF)$ is then a symbol supported in $W'$ (the eighty-fourth verifier,
D204). Put $\Psi := \psi(\mathfrak M_RF)\psi(\mathfrak M\rho_K)$. Then
$$\mathsf H(\Psi^2) = 2\mathfrak M_R(\psi\psi')(\mathfrak M_RF)\,\mathsf HF\,\psi(\mathfrak M\rho_K)^2+
2\mathfrak M(\psi\psi')(\mathfrak M\rho_K)\,\mathsf H\rho_K\,\psi(\mathfrak M_RF)^2.$$
The first term is $\le0$ and is $-b'^*b'$ with $b' := \rho^{-s}\varphi_\epsilon\theta(\mathfrak M_RF)(2\mathfrak
M_R\mathsf HF)^{1/2}\psi(\mathfrak M\rho_K)$, $\theta := (-\psi\psi')^{1/2}$, smooth as $\mathsf HF\ge c_F/(4\mathfrak
M_R)$ on the support of $\theta(\mathfrak M_RF)$. In the second, $\mathsf H\rho_K = \rho_K^2(\rho_K^{-2}\mathsf
H\rho_K)\le-\frac12\beta\beta_0\rho_K^2<0$ near $\partial R_{\mathcal H^+}$ (II.B (4.1)), so it is $+e^*e$ with $e :=
\rho^{-s}\varphi_\epsilon\theta(\mathfrak M\rho_K)(-2\mathfrak M\mathsf H\rho_K)^{1/2}\psi(\mathfrak M_RF)$, supported in
$\{\rho_K\ge(2\mathfrak M)^{-1}\}$, away from $K^+$; so $E$ can be chosen with Schwartz kernel in $(K\setminus K^+)^2$,
as (4) requires. Choosing $\mathfrak M_R$ and then $\mathfrak M$ large, $\mathrm{supp}\,\Psi$ lies in $U$, in $W$ and in
$\{Q_\epsilon\ge c\}$. No cut-off to the characteristic set is needed, as the signs hold on a full neighbourhood of
$\partial R_{\mathcal H^+}$ (II.B Lemma 4.2); so (2.2) holds with $j_\epsilon = 0$. The pattern (6) gives (3.2), with
$\|\chi\tilde u\|_{-N}\le C\|\tilde\chi u\|_{H^{s_0,\alpha_K}}$. $\square$

**Proposition 3.2 ([Hin26c] Proposition 7.6 at $n = 4$; the incoming radial set over $\partial K^+$).** There are $B,E,G$
with (1) operator wave front sets in any fixed neighbourhood of $\partial R_{\partial K^+,\mathrm{in}}$; (2) Schwartz
kernels in $K\times K$ for any fixed compact neighbourhood $K$ of $\partial K^+$; (3) $B$ elliptic at $\partial
R_{\partial K^+,\mathrm{in}}$; (4) the Schwartz kernel of $E$ supported in $(K\setminus K^+)^2$; such that for all
constants $s>s_0$, $\alpha_+$, $\alpha_K$ with
$$s_0+\alpha_+>\tfrac12\big(-1+\vartheta^{3b}_{\mathrm{in}}\big)+\alpha_K\tag{3.3}$$
(II.C (2.1)), and $\tilde\chi$ as before,
$$\|Bu\|_{H^{s,(\alpha_+,\alpha_K)}}\le C\big(\|GPu\|_{H^{s-1,(\alpha_++2,\alpha_K)}}+\|Eu\|_{H^{s,(\alpha_+,\alpha_K)}}+
\|\tilde\chi u\|_{H^{s_0,(\alpha_+,\alpha_K)}}\big)\tag{3.4}$$
in the strong sense, for $P = P_0$ and every $P$ with $\epsilon_P$ small, $d_0$ depending only on $s,s_0$. Near $\partial
K^+$, $x_I$ is smooth and positive, so the weights are $(\alpha_+,\alpha_K)$.

*Proof.* $W' := \rho_+^2$, with $\rho_+ = r^{-1}$ and $\rho_K = r/t_*$; $\ell = \rho_+^{-2}G = G_{3b}$ (II.B (3.2));
$\rho := -\sigma_{3b}^{-1}$, $\hat\xi$, $\hat\eta$ as in II.B (3.3), so $\mathsf H$ is the field of II.B (3.4); $w :=
\rho_+^{\alpha_+}\rho_K^{\alpha_K}$; $A$ the frame of an inner product attaining $\vartheta^{3b}_{\mathrm{in}}$. Then
$\mathfrak p' = \rho\sigma^1_{3b}(r^2\mathrm{Im}_hP)$, which at $R := \partial R_{\partial K^+,\mathrm{in}}$ is that of
$P_0$, the coefficients of $P-P_0$ vanishing at $\partial K^+$ (and the terms with $\chi_I$ in II.C (3.2) vanishing near
$\partial K^+$). At $R$, $\mathsf H = 0$ and, by II.B (3.4) and its linearisation, $\rho^{-1}\mathsf H\rho = 2$,
$\rho_+^{-1}\mathsf H\rho_+ = 2$, $\rho_K^{-1}\mathsf H\rho_K = -2$. So, at $R$,
$$Q_\epsilon = 2(2s_\epsilon-1)-2A^{-1}\mathfrak p'A+2\cdot2+2(2\alpha_+-2\alpha_K)\ge4\Big(s_\epsilon+\alpha_+
-\alpha_K-\tfrac12\big(-1+\vartheta^{3b}_{\mathrm{in}}\big)\Big),$$
which is at least $2c>0$ for $s_\epsilon\ge s_0$, by (3.3).

Put $q := |\hat\eta|^2+(\hat\xi-2)^2$ and $\Psi := \psi(\mathfrak M_Rq)\psi(\mathfrak M\rho_+)\psi(\mathfrak M\rho_K)$.
Over $\iota^+$, where $\mathsf H = \bar{\mathsf H}$, II.B (3.4) gives $\bar{\mathsf H}\hat\xi = -2(2-\hat\xi)\hat\xi$ and
$\bar{\mathsf H}|\hat\eta|^2 = -4(1-\hat\xi)|\hat\eta|^2$ (the terms with $\partial_\omega|\hat\eta|^2$ and $\bar{\mathsf
H}\omega$ cancel, the Hamilton field of $|\hat\eta|^2$ on $T^*\mathbb S^3$ preserving it). Hence ([Hin26c] p. 120)
$$\bar{\mathsf Hq} = 4(\hat\xi-1)|\hat\eta|^2+4\hat\xi(\hat\xi-2)^2\ge2q\quad\text{for }|\hat\xi-2|\le\tfrac12,$$
on the full phase space over $\iota^+$, not only on the characteristic set. $\mathsf H-\bar{\mathsf H}\in\rho_+^2\mathcal
V_b$ plus $O(\epsilon_P\rho_+^{\ell_+}\rho_K^{\ell_K})$ (II.B section 3.1, II.C Lemma 4.1), so $\mathsf Hq\ge(2\mathfrak
M_R)^{-1}$ on $\mathrm{supp}\,\psi'(\mathfrak M_Rq)\cap\mathrm{supp}\,\psi(\mathfrak M\rho_+)\psi(\mathfrak M\rho_K)$ for
$\mathfrak M$ large given $\mathfrak M_R$. Near $R$, $\rho_+^{-1}\mathsf H\rho_+\ge1$ and $\rho_K^{-1}\mathsf
H\rho_K\le-1$. So in (5) of the pattern, the factors $\psi(\mathfrak M_Rq)$ and $\psi(\mathfrak M\rho_+)$ give $-b'^*b'$
terms, and $\psi(\mathfrak M\rho_K)$ gives $+e^*e$, supported in $\{\rho_K\ge(2\mathfrak M)^{-1}\}$, away from $K^+$, as
(4) requires; $j_\epsilon = 0$. The pattern gives (3.4). $\square$

**Proposition 3.3 ([Hin26c] Proposition 7.7 at $n = 4$; the outgoing radial set over $\partial K^+$).** There are $B,E,G$
with (1)-(3) as in Proposition 3.2 with $\partial R_{\partial K^+,\mathrm{out}}$ in place of $\partial R_{\partial
K^+,\mathrm{in}}$, and (4) the operator wave front set of $E$ disjoint from $\partial W_{\mathrm{out}} = \{\rho_+ =
0,\hat\xi = 0,\hat\eta = 0\}$, the unstable manifold of $\partial R_{\partial K^+,\mathrm{out}}$ over $\iota^+$ (II.B
Lemma 3.3 (4)); such that for all constants $s>s_0$, $\alpha_+,\alpha_K$ with
$$s+\alpha_+<\tfrac12\big(-1+\vartheta_{\mathrm{out}}\big)+\alpha_K\tag{3.5}$$
(II.C (2.1)), (3.4) holds in the strong sense, for $P = P_0$ and every $P$ with $\epsilon_P$ small.

*Proof.* As for Proposition 3.2, with $A$ the frame of the inner product of II.C Lemma 2.5, for which $-A^{-1}\mathfrak
p'A\ge\vartheta_{\mathrm{out}}$ at $R := \partial R_{\partial K^+,\mathrm{out}}$ (II.C Lemma 2.6: there $-\mathfrak p' =
S+S^{*h}$). At $R$, $\rho^{-1}\mathsf H\rho = -2$, $\rho_+^{-1}\mathsf H\rho_+ = -2$, $\rho_K^{-1}\mathsf H\rho_K = 2$
(II.B (3.4) at $\hat\xi = 0$). So at $R$
$$Q_\epsilon = -2(2s_\epsilon-1)-2A^{-1}\mathfrak p'A-4+2(-2\alpha_++2\alpha_K)\ge4\Big(\tfrac12\big(-1+
\vartheta_{\mathrm{out}}\big)+\alpha_K-\alpha_+-s_\epsilon\Big),$$
at least $2c>0$ for $s_\epsilon\le s$, by (3.5): the threshold is an upper bound, met by every order of the iteration.
Put $q := |\hat\eta|^2+\hat\xi^2$; by II.B (3.4), over $\iota^+$,
$$\bar{\mathsf H}q = -4(1-\hat\xi)|\hat\eta|^2-4(2-\hat\xi)\hat\xi^2\le-2q\quad\text{for }|\hat\xi|\le\tfrac12,$$
which is [Hin26c] (7.18). With $\Psi := \psi(\mathfrak M_Rq)\psi(\mathfrak M\rho_+)\psi(\mathfrak M\rho_K)$, now
$\psi(\mathfrak M\rho_K)$ gives a $-b'^*b'$ term ($\rho_K^{-1}\mathsf H\rho_K\ge1$ near $R$), while $\psi(\mathfrak
M_Rq)$ and $\psi(\mathfrak M\rho_+)$ give $+e^*e$ terms ($\mathsf Hq<0$ on $\mathrm{supp}\,\psi'(\mathfrak M_Rq)$,
$\rho_+^{-1}\mathsf H\rho_+\le-1$). These are supported in $\{q\ge(2\mathfrak M_R)^{-1}\}$, disjoint from $\{\hat\xi =
\hat\eta = 0\}\supset\partial W_{\mathrm{out}}$, and in $\{\rho_+\ge(2\mathfrak M)^{-1}\}$, away from
$\iota^+\supset\partial W_{\mathrm{out}}$. So $E$ can be chosen elliptic on both with $\mathrm{WF}'(E)\cap\partial
W_{\mathrm{out}} = \emptyset$, and these sets meet fibre infinity in $U\setminus R$, as Lemma 2.2 requires. $\square$

**Lemma 3.4 ([Hin26c] (7.22) at $n = 4$).** Near $\mathscr I^+\cap\Omega$, with $\rho_+ = t_*^{-1}$, $x_I =
(t_*/r)^{1/2}$, $\omega$, the eb-momenta of II.B section 7 and $\rho := \sigma_{eb}^{-1}$, $\hat\xi :=
\xi_{eb}/\sigma_{eb}$, $\mathsf H := \rho H_{G_{eb}}$, let $h$ be a smooth fibre inner product with Gram matrix $\mathsf
G$, and $\mathfrak p := \rho x_I^{-2}\rho_+^{-2}\sigma_1(\mathrm{Im}_hP)$. Then over $\mathscr I^+$
$$\mathfrak p = (\mathrm{Re}_hp_1)(\hat\xi-2)+\tfrac12\mathsf G^{-1}\mathsf H\mathsf G,\qquad\mathrm{Re}_hp_1 :=
\tfrac12(p_1+p_1^{*h}),\tag{3.6}$$
with $p_1 = S|_{\partial X}+\tilde p_1$ of II.C Definition 3.3. In particular $\mathfrak p = 0$ at $\partial R_{\mathscr
I^+,\mathrm{in},+}$ and $\mathfrak p = -2\,\mathrm{Re}_hp_1$ at $\partial R_{\mathscr I^+,\mathrm{out}}$, where $\mathsf
H = 0$.

*Proof.* *The density.* With $t_* = \rho_+^{-1}$ and $r = \rho_+^{-1}x_I^{-2}$, $|dt\,dx| = r^3|dt_*\,dr\,d\omega| =
2\rho_+^{-5}x_I^{-8}|\frac{d\rho_+}{\rho_+}\frac{dx_I}{x_I}d\omega|$, $d\omega$ the round density of $\mathbb S^3$ (as
$|dt_*\wedge dr| = 2\rho_+^{-3}x_I^{-3}|d\rho_+\wedge dx_I|$; II.A Lemma 6.1). For it, $(x_I\partial_{x_I})^* =
-x_I\partial_{x_I}+8$, $(\rho_+\partial_{\rho_+})^* = -\rho_+\partial_{\rho_+}+5$, $\Delta_{\mathbb S^3}$ is symmetric,
and so are multiplications by real functions.

*The operator.* Put $X_1 := x_I\partial_{x_I}-2\rho_+\partial_{\rho_+}$, $X_2 := x_I\partial_{x_I}$, $W :=
x_I^2\rho_+^2$. By II.C Lemma 3.4, $P = P_s+Wp_1X_1+\frac12W(p_0+R)$ with $P_s :=
\frac12W\big(-(X_2-3)X_1+2x_I^2\Delta_{\mathbb S^3}\big)\otimes\mathrm{Id}$ and $R\in
C^{(d_0;0),(2\ell_I,0)}_{eb}\mathrm{Diff}^2_{eb}$.

(i) $P_s$ is symmetric for the standard inner product. $X_1^* = -X_1-2$ and $(X_2-3)^* = -(X_2-5)$, so $(W(X_2-3)X_1)^* =
(X_1+2)(X_2-5)W$. As $X_2W = W(X_2+2)$ and $X_1W = W(X_1-2)$, this is $WX_1(X_2-3) = W(X_2-3)X_1$, $X_1$ and $X_2$
commuting. And $(Wx_I^2\Delta)^* = \Delta x_I^2W = Wx_I^2\Delta$. With $h$, $P_s^{*h} = \mathsf G^{-1}P_s\mathsf G =
P_s+\mathsf G^{-1}[P_s,\mathsf G]$, so $\sigma_1(\mathrm{Im}_hP_s) = \frac12\mathsf G^{-1}H_{\sigma_2(P_s)}\mathsf G$.
Here $\sigma_2(P_s) = W(G_{eb}+O(x_I^{2\ell_I}))$, and $H_{WG_{eb}}\mathsf G = WH_{G_{eb}}\mathsf G$ as $\mathsf G$ and
$W$ are functions of the base.

(ii) $(Wp_1X_1)^{*h} = \mathsf G^{-1}X_1^*p_1^*W\mathsf G$, and $\sigma(X_1) = i(\xi_{eb}-2\sigma_{eb})$, so
$\sigma_1(\mathrm{Im}_h(Wp_1X_1)) = W\,\mathrm{Re}_hp_1\,(\xi_{eb}-2\sigma_{eb})$, as $\mathsf G^{-1}p_1^*\mathsf G =
p_1^{*h}$.

(iii) $p_0$ is of order 0. $R$ has real scalar principal symbol and coefficients in $x_I^{2\ell_I}C^{(d_0;0)}_{eb;b}$, a
class preserved by eb-derivatives, so $\sigma_1(\mathrm{Im}_hR)$ is $O(x_I^{2\ell_I})$.

Multiplying by $\rho W^{-1}$ and setting $x_I = 0$ gives (3.6). $\square$

At $n = 3$ the source's density is $r^2|dt_*\,dr\,d\slashed g| = 2\rho_+^{-4}x_I^{-6}|\cdots|$, for which
$\frac12x_I^2\rho_+^2(x_I\partial_{x_I}-2)(x_I\partial_{x_I}-2\rho_+\partial_{\rho_+})$ is symmetric. At $n = 4$ the
density $r^3$ and the constant 3 of II.C Lemma 3.4 match in the same way, so (7.22) holds with the same form. With a
varying inner product, the term $\frac12\mathsf G^{-1}\mathsf H\mathsf G$ appears, and it vanishes at the radial sets.

**Proposition 3.5 ([Hin26c] Proposition 7.8 at $n = 4$; the incoming radial set at $\mathscr I^+\cap\iota^+$).** There
are $B,E,G$ with (1) operator wave front sets in any fixed neighbourhood of $\partial R_{\mathscr I^+,\mathrm{in},+}$;
(2) Schwartz kernels in $K\times K$ for any fixed compact neighbourhood $K$ of $\mathscr I^+\cap\iota^+$; (3) $B$
elliptic at $\partial R_{\mathscr I^+,\mathrm{in},+}$; (4) the Schwartz kernel of $E$ supported in
$(K\setminus\iota^+)^2$; such that for all constants $s>s_0$ and $\alpha_I,\alpha_+$ with
$$\alpha_+<\alpha_I-\tfrac12,\tag{3.7}$$
and $\tilde\chi$ as before,
$$\|Bu\|_{H^{s,(2\alpha_I,\alpha_+)}}\le C\big(\|GPu\|_{H^{s-1,(2\alpha_I+2,\alpha_++2)}}+
\|Eu\|_{H^{s,(2\alpha_I,\alpha_+)}}+\|\tilde\chi u\|_{H^{s_0,(2\alpha_I,\alpha_+)}}\big)\tag{3.8}$$
in the strong sense, for $P = P_0$ and every $P$ with $\epsilon_P$ small. Near $\mathscr I^+\cap\iota^+$, $\rho_K$ is
smooth and positive, so the weights are $(2\alpha_I,\alpha_+)$.

*Proof.* $W' := W = x_I^2\rho_+^2$, $\ell = G_{eb}$, $\rho := \sigma_{eb}^{-1}$, $\mathsf H$ the field of II.B
(7.3)-(7.4), $w := x_I^{2\alpha_I}\rho_+^{\alpha_+}$, $A := \mathrm{Id}$. At $R := \partial R_{\mathscr
I^+,\mathrm{in},+} = \{\rho_+ = x_I = 0,\hat\xi = 2,\hat\eta = 0\}$, $\mathsf H = 0$, and by II.B (7.4),
$\rho^{-1}\mathsf H\rho = 0$, $x_I^{-1}\mathsf Hx_I = \hat\xi-1 = 1$, $\rho_+^{-1}\mathsf H\rho_+ = -\hat\xi = -2$; and
$\mathfrak p' = 0$ by Lemma 3.4. So at $R$, independently of $s_\epsilon$,
$$Q_\epsilon = 0+\mathsf H\log W+2\mathsf H\log w = 2\cdot1+2\cdot(-2)+2(2\alpha_I\cdot1+\alpha_+\cdot(-2)) =
4\big(\alpha_I-\alpha_+-\tfrac12\big)\ge2c>0$$
by (3.7). Near $R$, $\rho^{-1}\mathsf H\rho = O(x_I^2)+O(\epsilon_Px_I^{2\ell_I})$, as $\mathsf H^0\rho = 0$ exactly; so
the term $(2s_\epsilon-1)\rho^{-1}\mathsf H\rho$ is small on $\mathrm{supp}\,\Psi$, uniformly for $s_\epsilon$ in the
range of the iteration, and $Q_\epsilon\ge c$ there.

Put $q := (\hat\xi-2)^2+|\hat\eta|^2$ and $\Psi := \psi(\mathfrak M_\Sigma\rho^2\ell)\psi(\mathfrak M_Rq)\psi(\mathfrak
Mx_I)\psi(\mathfrak M\rho_+)$. Over $\mathscr I^+$, $\mathsf H = \mathsf H^0$ of II.B (7.4), with $\mathsf H^0\hat\xi =
-2|\hat\eta|^2$ and $\mathsf H^0|\hat\eta|^2 = 2(\hat\xi-1)|\hat\eta|^2$ (the angular motion stops at $x_I = 0$). On the
characteristic set over $\mathscr I^+$, $|\hat\eta|^2 = \frac12\hat\xi(2-\hat\xi)$ (II.B Lemma 7.2 (1)), so
$$\mathsf H^0q = -4(\hat\xi-2)|\hat\eta|^2+2(\hat\xi-1)|\hat\eta|^2 = 2\hat\xi(2-\hat\xi)^2+2(\hat\xi-1)|\hat\eta|^2
\ge q\quad\text{for }|\hat\xi-2|\le\tfrac12,$$
which is [Hin26c] (7.21). Off the characteristic set, $|\hat\eta|^2 = \frac12\hat\xi(2-\hat\xi)+\rho^2G^0_{eb}$, and
$\rho^2(\ell-G^0_{eb}) = O(x_I^2)+O(\epsilon_Px_I^{2\ell_I})$; so $\mathsf Hq\ge(4\mathfrak M_R)^{-1}$ on
$\mathrm{supp}\,\psi'(\mathfrak M_Rq)$ within the support of the other factors, for $\mathfrak M_\Sigma,\mathfrak M$
large given $\mathfrak M_R$. Near $R$, $x_I^{-1}\mathsf Hx_I\ge\frac12$ and $\rho_+^{-1}\mathsf H\rho_+\le-1$, on the
full phase space. So in (5) of the pattern: $\psi(\mathfrak M_Rq)$ and $\psi(\mathfrak Mx_I)$ give $-b'^*b'$;
$\psi(\mathfrak M\rho_+)$ gives $+e^*e$, supported in $\{\rho_+\ge(2\mathfrak M)^{-1}\}$, away from $\iota^+$, as (4)
requires; $\psi(\mathfrak M_\Sigma\rho^2\ell)$ gives $j_\epsilon\ell$, with $j_\epsilon$ of order $2s-2$. The pattern
gives (3.8). $\square$

**Proposition 3.6 ([Hin26c] Proposition 7.9 at $n = 4$; the outgoing radial set over $\mathscr I^+$).** Let
$t_{*,-}\in\mathbb R$. There are $B,E,G$ with (1) operator wave front sets in any fixed neighbourhood of $\partial
R_{\mathscr I^+,\mathrm{out}}\cap\{t^\flat_*\ge t_{*,-}\}$; (2) Schwartz kernels in $K\times K$ for any fixed compact
neighbourhood $K\subset\tilde M$ of $\mathrm{cl}(\mathscr I^+\cap\{t_*\ge t_{*,-}\})$; (3) $B$ elliptic at $\partial
R_{\mathscr I^+,\mathrm{out}}\cap\{t^\flat_*\ge t_{*,-}\}$; (4) $\mathrm{WF}'(E)\cap\partial R_{\mathscr
I^+,\mathrm{out}}\subset\{t^\flat_*\le t_{*,-}-\frac14\}$; such that for all constants $s>s_0$ and $\alpha_I,\alpha_+$
with
$$\alpha_I<-\tfrac12+\bar p_1\tag{3.9}$$
($\bar p_1$ of II.C Definition 3.5, for $P$), (3.8) holds in the strong sense, for $P = P_0$ and every $P$ with
$\epsilon_P$ small.

*Proof.* $W'$, $\ell$, $\rho$, $\mathsf H$, $w$ as in Proposition 3.5. Let $\delta' := \frac14(\bar
p_1-\frac12-\alpha_I)>0$, and let $h_I$ be a smooth fibre inner product near $\mathrm{cl}(\mathscr I^+\cap\Omega)$ with
$\mathrm{Re}_{h_I}p_1\ge\bar p_1-\delta'$ there. It is constructed as in II.C Lemma 2.5: $p_1$ is continuous on the
compact closure of $\mathscr I^+\cap\Omega$ (with $\tilde p_1\in\rho_+^{\ell_+}C_b$ tending to 0 at $\iota^+$), so Jordan
scalings at points, continuity and a smooth partition of unity apply verbatim; $h_I$ is extended independently of $x_I$.
$A$ is its frame. At $R := \partial R_{\mathscr I^+,\mathrm{out}} = \{x_I = 0,\hat\xi = 0,\hat\eta = 0\}$, over all of
$\mathscr I^+$, $\mathsf H = 0$; $\rho^{-1}\mathsf H\rho = 0$, $x_I^{-1}\mathsf Hx_I = -1$, $\rho_+^{-1}\mathsf H\rho_+ =
-\hat\xi = 0$ (II.B (7.4)); and $\mathfrak p' = -2\,\mathrm{Re}_{h_I}p_1$ (Lemma 3.4). So at $R$
$$Q_\epsilon = 4A^{-1}(\mathrm{Re}_{h_I}p_1)A-2+2\cdot2\alpha_I\cdot(-1)
\ge4\big(\bar p_1-\delta'-\tfrac12-\alpha_I\big) = 12\delta' =: 2c>0,$$
by (3.9), independently of $s_\epsilon$; near $R$, $\rho^{-1}\mathsf H\rho$ is small as before.

Put $q := \hat\xi^2+|\hat\eta|^2$, fix $\eta_t\in C^\infty(\mathbb R)$ with $\eta_t = 0$ on $(-\infty,-\frac12]$,
$\eta_t = 1$ on $[-\frac14,\infty)$, $\eta_t'\ge0$ and $(\eta_t\eta_t')^{1/2}$ smooth, and $\psi_- :=
\eta_t(t^\flat_*-t_{*,-})$, which equals 1 for $t^\flat_*\ge t_{*,-}-\frac14$. Put $\Psi := \psi(\mathfrak
M_\Sigma\rho^2\ell)\psi(\mathfrak M_Rq)\psi(\mathfrak Mx_I)\psi_-$. On the characteristic set over $\mathscr I^+$, with
$|\hat\eta|^2 = \frac12\hat\xi(2-\hat\xi)$,
$$\mathsf H^0q = -4\hat\xi|\hat\eta|^2+2(\hat\xi-1)|\hat\eta|^2 = -2(2-\hat\xi)\hat\xi^2-2(1-\hat\xi)|\hat\eta|^2
\le-q\quad\text{for }|\hat\xi|\le\tfrac12,$$
and off it, as in Proposition 3.5, $\mathsf Hq\le-(4\mathfrak M_R)^{-1}$ on $\mathrm{supp}\,\psi'(\mathfrak M_Rq)$
within the support of the other factors. (The source prints $-4(2-\hat\xi)\hat\xi^2$ for the first term; section 6,
(D3).) Near $R$, $x_I^{-1}\mathsf Hx_I\le-\frac12$. So $\psi(\mathfrak M_Rq)$ and $\psi(\mathfrak Mx_I)$ give $+e^*e$
terms, supported in $\{q\ge(2\mathfrak M_R)^{-1}\}$ and $\{x_I\ge(2\mathfrak M)^{-1}\}$, both disjoint from $R$;
$\psi(\mathfrak M_\Sigma\rho^2\ell)$ gives $j_\epsilon\ell$. The factor $\psi_-$ gives $2\eta_t\eta_t'\,\mathsf
Ht^\flat_*\cdot(\text{other factors})^2$. Whatever its sign, with $C_t := 1+\sup|\mathsf Ht^\flat_*|$ over the support,
it is $e_-^*e_--b_-'^*b'_-$ with $e_-^2 := 2C_t\eta_t\eta_t'(\cdots)^2$ and $b_-'^2 := 2(C_t-\mathsf
Ht^\flat_*)\eta_t\eta_t'(\cdots)^2$, both smooth squares. Its support lies in
$\{t^\flat_*\in[t_{*,-}-\frac12,t_{*,-}-\frac14]\}$, which gives (4); so it misses $\partial R_{\mathscr
I^+,\mathrm{out}}\cap\{t^\flat_*\ge t_{*,-}\}$, where $B$ is to be elliptic, as Lemma 2.2 requires of the $E$-sets.
(With $\eta_t = 1$ only on $[0,\infty)$ the two could touch at $t^\flat_* = t_{*,-}$; the eighty-fourth verifier, D204.)
On the characteristic set over $\Omega^\circ$, $\mathsf Ht^\flat_*>0$ (II.C Lemma 3.2 (2)), and $e_-$ is the a priori
term at earlier times; off it the sign of $\mathsf Ht^\flat_*$ is not used. The other $E$-sets are disjoint from $R$.
The pattern gives (3.8). Here $\mathrm{supp}\,\Psi$ is not compact in $t^\flat_*$, but it is compact in $\tilde M$, its
closure meeting $\mathscr I^+\cap\iota^+$, where II.B (7.4) holds uniformly. $\square$

In both uses below, $t_{*,-}\le\frac12$. The kernel of $E$ near its $e_-$-set can then be supported in
$\{t^\flat_*<1\}^2$, where the $u$ of Theorem 1.2 vanishes, so that this part of $\|Eu\|$ is zero. The source states the
estimate for $t_*\in[t_{*,-},t_{*,+}]$ with $t_{*,+}\le\infty$. For finite $t_{*,+}$ its proof uses $H_Gt_*\ge0$ on the
support of the commutant, which fails off the characteristic set near $R$: at $x_I = 0$, $\mathsf Ht^\flat_* =
t_*\hat\xi$, and $\hat\xi<0$ occurs there. The case $t_{*,+}<\infty$ serves in the source only for control near $R$ at
finite times in its Step 1, which the proof in section 5 does without (section 6, (D2)).

*Remark 3.7 ([Hin26c] Remark 7.5).* Propositions 3.1-3.6 hold for $P+\tilde P$, with $\tilde P$ a first-order operator of
the form $\mathrm{Op}(\tilde p)$, $\tilde p\in C^{(d_0)}\tilde S^1$ (or a finite combination of $C^{d_0}_{e3b}$
coefficients and smooth first-order operators). The thresholds are then computed with $\sigma_1(\mathrm{Im}_h(P+\tilde
P))$ at $R$, where this symbol is continuous. The proofs use $\tilde P$ only through $\ell_I$ in $Q_\epsilon$, and Lemmas
2.1-2.3 hold for such operators (the remark after Lemma 2.5). The constants are locally uniform in $\tilde p$. This is
used in Part II.D$'$.

## 4. The estimate at the trapped set

*Setting.* Near the trapped set $W' = 1$ (section 1.1). Over $D = \{t_*>T_\flat,\ r_{\Gamma,-}<r<r_{\Gamma,+}\}$ of
II.C$'$ section 3.2 ($T_\flat = 2/C'$ there; D328) the e3b-structure is spanned by $\partial_{t_*}$ and $\partial_x$,
and ${}^{e3b}T^*_DM = T^*D$ with covectors $-\sigma\,dt_*+\zeta$. There $\rho_K = t_*^{-1}$, while $x_I$ and $\rho_+$
are smooth and positive, so only the weight $\alpha_K$ enters, and we write $H^{\mathsf t,\alpha_K} := H^{\mathsf
t,(2\alpha_I,\alpha_+,\alpha_K)}_{e3b}$. We work on $\partial\Sigma^+$, near the trapped set $\Gamma =
\Gamma_1\subset\Sigma^\flat_1$ of (H7) at $z_0 = 1$, where $\sigma>0$. The slice coordinates $(t_*,x,z)$, $z =
\zeta/\sigma$, of II.C$'$ section 3.2 identify ${}^{e3b}S^*_DM\cap\{\sigma>0\}$ with $(T_\flat,\infty)\times
T^*\{r_{\Gamma,-}<r<r_{\Gamma,+}\}$, and $\partial\Gamma_0 := \{t_*>T_\flat\}\times\Gamma$. Put $\rho := \sigma^{-1}$
there, extended to a positive symbol of degree $-1$ near fibre infinity (section 2). Then $\mathsf H := \rho H_G$ is the
field $\hat W$ of II.C$'$ (3.2) with $p = G$, and $\rho^2G = G(t_*,x;-dt_*+z)$. Three facts are used throughout.

(T1) $\mathsf Ht_*\ge\frac12\beta_0$ on a neighbourhood of $\partial\Gamma_0$ in the full phase space, for $\epsilon_P$
small (II.C$'$, the paragraph after Lemma 3.3). So $\mathsf H\rho_K = -\rho_K^2\,\mathsf Ht_*<0$ there.

(T2) $\rho^{-1}\mathsf H\rho = H_G(\sigma^{-1}) = -\sigma^{-2}\partial_{t_*}G$, as $H_G\sigma = \partial_{t_*}G$,
$\sigma$ being minus the momentum of $t_*$. It vanishes for $P_0$, and for $P$ it is $O(\epsilon_P\rho_K^{\ell_K})$ near
$\partial\Gamma_0$, by the bounds on $g^{-1}-g_0^{-1}$ before II.C$'$ (3.1).

(T3) Let $h_\Gamma$ be a fibre inner product as in II.C Definition 2.1 for $z_0 = 1$ (it exists by II.C Lemma 2.2 (a)),
extended to be stationary and homogeneous of degree 0, and $\mathfrak p' := \rho\,\sigma_1(\mathrm{Im}_{h_\Gamma}P)$. At
$\partial\Gamma_{K^+}$, $\mathfrak p' = p_1(1)$, by II.C Lemma 2.2 (b), the coefficients of $P-P_0$ vanishing at $K^+$.
So $\vartheta_\Gamma := \sup_{\partial\Gamma_{K^+}}\lambda_{\max}(\mathfrak p')<\frac12\nu_{\min}$.

**Lemma 4.1 (the hypersurfaces as defining functions).** Let $d_0\ge5$, let $\phi^u,\phi^s$ be the functions of II.C$'$
Proposition 3.4 for the metric $g$ of $P$, on the neighbourhood $U$ of $\partial\Gamma_0$ there, let $O$ be as in (H7)
and $O'\Subset O$ an open neighbourhood of $\Gamma$. For $\delta>0$ let
$$U(\delta) := \{\rho_K\le\delta,\ |\phi^u|\le\delta,\ |\phi^s|\le\delta,\ |\rho^2G|\le\delta,\ (x,z)\in\bar O'\},$$
a subset of fibre infinity over $\{\sigma>0\}$, closed in the compactified bundle, which includes $\rho_K = 0$. There is
$\delta_U\in(0,\frac12C')$, with $C'$ of II.C Lemma 3.2, such that the following hold ($\rho_K\le\delta<\frac12C'$
places $U(\delta)$ over $\{t_*>T_\flat\}$, where $\phi^{u/s}$ are defined, II.C$'$ Proposition 3.4; D327).

(a) For $\delta\le\delta_U$, $U(\delta)$ is a compact neighbourhood of $\partial\Gamma_{K^+}$, contained in $\{(x,z)\in
O''\}$ for an open $O''\Subset O'$ independent of $\delta$, and $\bigcap_{\delta>0}U(\delta) = \partial\Gamma_{K^+}$.
Moreover $\Gamma^u_{K^+}\cap U(\delta_U) = U(\delta_U)\cap\{\rho_K = 0,\ \phi^u = 0,\ \rho^2G = 0\}$.

(b) On a neighbourhood of $U(\delta_U)$ there are real functions $w_u,r_u\in C^{d_0-3}$ and $w_s,r_s\in C^{d_0-4}$,
homogeneous of degree 0, with bounded derivatives along $\partial_{t_*},\partial_x$ and the fibres up to these orders,
and continuous up to $\rho_K = 0$, such that
$$\mathsf H\phi^u = -w_u\phi^u+r_u\rho^2G,\qquad\mathsf H\phi^s = w_s\phi^s+r_s\rho^2G.\tag{4.1}$$

(c) $w_u = \nu_u$ and $w_s = \nu_s$ on $\partial\Gamma_{K^+}$, so $w_{u/s}\ge\nu_{\min}$ there.

(d) $c_{us} := \rho^{-1}\{\phi^u,\phi^s\}$ is continuous up to $\rho_K = 0$, and on $\partial\Gamma_{K^+}$ it equals
$\{\phi_u,\phi_s\}>0$, the bracket of $T^*\tilde X^\circ$ in (Γ.3).

*Proof.* At $\rho_K = 0$ every function involved is that of the stationary model: $\tilde\phi^{u/s}\to0$ with their
derivatives (II.C$'$ Proposition 3.4); $\rho^2G-G_1 = \tilde g = O(\epsilon_P\rho_K^{\ell_K})$ with $d_0$ derivatives
(II.C$'$ (3.1)); and $\phi_0^{u/s} = \phi_{u/s}\circ w$ is independent of $t_*$ and equal to $\phi_{u/s}$ on $Y = \{G_1 =
0\}\cap O_0$, $w$ being the projection along $N$ of II.C$'$ section 3.3.

(a) On $\{G_1 = 0\}\cap O$, $\phi_0^{u/s} = \phi_{u/s}$, and $\Gamma_u\cap\Gamma_s = \Gamma$ by (Γ.1); so $\{\phi_0^u =
\phi_0^s = G_1 = 0\}\cap\bar O' = \Gamma$. By compactness of $\bar O'$ there are $O''\Subset O'$ and $\delta'>0$ with
$\{|\phi_0^u|,|\phi_0^s|,|G_1|\le2\delta'\}\cap\bar O'\subset O''$, and these sets shrink to $\Gamma$ as $\delta'\to0$.
For $\rho_K\le\delta$ the functions defining $U(\delta)$ differ from these by $O(\delta^{\ell_K})$. So for
$\delta\le\delta_U$ small, $U(\delta)\subset\{(x,z)\in O''\}$ and $\bigcap_\delta U(\delta) = \{\rho_K = 0\}\times\Gamma
= \partial\Gamma_{K^+}$. $U(\delta)$ contains the set where the four inequalities are strict, which is open and contains
$\partial\Gamma_{K^+}$. The last assertion is II.C$'$ Proposition 3.4 with its Remark (b), as $\partial\Sigma^+ =
\{\rho^2G = 0\}$ near $\partial\Gamma_0$.

(b) $d\phi_u$, $d\phi_s$ and $dG_1$ are linearly independent at $\Gamma$ (the proof of II.C$'$ Lemma 3.1 (i)). On $Y$,
$d(\phi_{u/s}\circ w) = d\phi_{u/s}-(N\phi_{u/s})\,dG_1$, as $d(\phi\circ w)$ vanishes on $N$ and equals $d\phi$ on $TY =
\ker dG_1$. So $d\phi_0^u$, $d\phi_0^s$, $dG_1$ are independent at $\Gamma$, hence near it, and together with $dt_*$ near
$\partial\Gamma_0$ for the stationary model. For $\rho_K\le\delta_U$ the perturbations are $O(\delta_U^{\ell_K})$ in
$C^1$, so the independence persists, with uniform bounds. Near each point of $U(\delta_U)$ we can therefore complete $y_1
:= \phi^u$, $y_2 := \rho^2G$ by $t_*$ and smooth $t_*$-independent functions $y''$ to coordinates of class $C^{d_0-1}$,
with bounds uniform in $t_*$. $f := \mathsf H\phi^u$ lies in $C^{d_0-2}$, as $\mathsf H$ has coefficients in $C^{d_0-1}$,
and $f = 0$ on $\{y_1 = y_2 = 0\}$, as $\mathsf H$ is tangent to $\Gamma^u = \partial\Sigma^+\cap U\cap\{\phi^u = 0\}$
(II.C$'$ Proposition 3.4). Taylor's formula $f(y) = \sum_{i = 1,2}y_i\int_0^1(\partial_{y_i}f)(\theta y_1,\theta
y_2,y'')\,d\theta$, in coordinate boxes convex in $(y_1,y_2)$, gives $f = -w_uy_1+r_uy_2$ locally with $w_u,r_u\in
C^{d_0-3}$, and a partition of unity in $(x,z)$, independent of $t_*$, patches them. The integral formula preserves the
bounds along $\partial_{t_*},\partial_x$ and the fibres, and the convergence as $\rho_K\to0$. For $\phi^s\in C^{d_0-2}$
the same argument loses one more derivative.

(c) At $\rho_K = 0$, on $\{y_2 = 0\} = \{G_1 = 0\}$, $\mathsf H = q_1\partial_{t_*}+H_{G_1}$ (II.C$'$, after Lemma 3.2)
and $\phi^u = \phi_u$, so $f = H_{G_1}\phi_u = -\nu_u\phi_u$ by (Γ.2). Thus $w_u = \nu_u$ on $\{y_2 = 0\}$ where
$\phi_u\ne0$, hence on all of it by continuity, as $d\phi_u\ne0$ there. Likewise $w_s = \nu_s$.

(d) For functions $F,F'$ of $(x,z) = (x,\zeta/\sigma)$ alone, not depending on $t_*$, $\{F,F'\} =
\sigma^{-1}\{F,F'\}_{(x,z)}$, the terms with $t_*$ vanishing. $\phi^u$ and $\phi^s$ depend on $t_*$ off $\rho_K = 0$,
through $\tilde\phi^{u/s}$, and the formula is used only at $\rho_K = 0$, where $\tilde\phi^{u/s}$ and its derivatives
vanish; so there $c_{us} = \{\phi_0^u,\phi_0^s\}_{(x,z)}$. At $\Gamma$, by the formula for
$d(\phi\circ w)$, this is $\{\phi_u,\phi_s\}-(N\phi_s)\{\phi_u,G_1\}-(N\phi_u)\{G_1,\phi_s\}$, and $\{\phi_u,G_1\} =
-H_{G_1}\phi_u = \nu_u\phi_u = 0$, $\{G_1,\phi_s\} = \nu_s\phi_s = 0$ on $\Gamma$. Continuity up to $\rho_K = 0$ is as in
(b). $\square$

**Proposition 4.2 ([Hin26c] Proposition 7.10 at $n = 4$).** There are $B,E,G\in C^\infty_b\Psi^0_{e3b}$ such that (1)
their operator wave front sets lie in any fixed neighbourhood $U_\Gamma$ of $\partial\Gamma_{K^+}$ in ${}^{e3b}S^*M$; (2)
their Schwartz kernels are supported in $K\times K$ for any fixed compact neighbourhood $K\subset M$ of the base
projection of $U_\Gamma$; (3) $B$ is elliptic at $\partial\Gamma_{K^+}$; (4) $\mathrm{WF}'(E)\cap\Gamma^u_{K^+} =
\emptyset$; and such that for all constants $s>s_0$ and $\alpha_K\in\mathbb R$, and $\tilde\chi\in C^\infty(M)$ supported
near $K$ and equal to 1 near $K$,
$$\|Bu\|_{H^{s,\alpha_K}}\le C\big(\|GPu\|_{H^{s,\alpha_K}}+\|Eu\|_{H^{s+1,\alpha_K}}+
\|\tilde\chi u\|_{H^{s_0,\alpha_K}}\big)\tag{4.2}$$
in the strong sense, for $P = P_0$ and every $P$ with $\epsilon_P$ small, with $d_0$ depending only on $s,s_0$. Here
$\partial\Gamma_{K^+}$ and $\Gamma^u_{K^+}$ have one component over each of $\partial\Sigma^\pm$, and within $\Phi_1(O)$,
which contains $U_\Gamma$ when $U_\Gamma$ is small, $\Gamma^u_{K^+}$ is the global unstable set
$\partial\bar\Gamma^u_{K^+}$ (II.B Lemma 5.2 (b)).

Against Propositions 3.1-3.6 the estimate loses one derivative: $Pu$ is measured in $H^s$, not $H^{s-1}$, and the a
priori term in $H^{s+1}$. The proof is the positive commutator form of I.B section 6.4, whose defect measures are
replaced by commutators with a common regulariser: an equation with damping for $\Phi_uu$ (Step 1, I.B's (6.8)), a
commutator with $\Phi_u$ that bounds $u$ near $\{\phi^s = 0\}$ by $\sqrt\delta$ (Step 2, I.B's (6.9)), a propagation
estimate with the weight $|\phi^s|^{-\beta}$ (Step 3, I.B's Step 3), and their combination, which closes because
$\beta<\frac12$ (Step 4).

*Proof.* We prove the estimate at the component over $\partial\Sigma^+$; over $\partial\Sigma^-$ the proof is the same
with $z_0 = -1$, $\varsigma = -1$ and the future field $-\mathsf H$ (section 3); $c_{us}>0$ there too, as (Γ.3) of I.B
holds for both $z_0 = \pm1$. After Step 0 (a) norms are those of $H^{\mathsf t}_{e3b}$ without weights. $C$ denotes
constants independent of $\epsilon$ and, from Step 2 on, of $\delta$; $C_\delta$ may depend on $\delta$. Neither depends
on $u$.

*Step 0: reductions and choices.* (a) As in section 1.2 with $W' = 1$, $w := \rho_K^{\alpha_K}$ and $A$ the frame of
$h_\Gamma$, we replace $P$ by $L'' = A^{-1}w^{-1}PwA$ and $u$ by $A^{-1}w^{-1}u$, and keep the names $P$, $u$. The
principal symbol is $G$, and by (1.1) and (T1)
$$\mathfrak p := \rho\,\sigma_1(\mathrm{Im}\,P) = A^{-1}\big(\mathfrak p'+\alpha_K\rho_K\,\mathsf Ht_*\big)A,$$
as $\mathsf H\log w = \alpha_K\rho_K^{-1}\mathsf H\rho_K = -\alpha_K\rho_K\,\mathsf Ht_*$. $\mathfrak p$ is Hermitian and
continuous up to $\rho_K = 0$, and $\lambda_{\max}(\mathfrak p)\le\vartheta_\Gamma$ on $\partial\Gamma_{K^+}$, since
$A^{-1}\mathfrak p'A$ has the eigenvalues of the $h_\Gamma$-self-adjoint $\mathfrak p'$.

(b) Constants. Fix $\beta<\frac12$ with $\max(\vartheta_\Gamma,0)<\beta\nu_{\min}$, possible by (T3), and
$\eta_0\in(0,\frac1{10}\nu_{\min}]$ with $c_0 := \beta(\nu_{\min}-\eta_0)-\vartheta_\Gamma-2\eta_0>0$. By Lemma 4.1,
(T1)-(T2) and continuity there is $\delta_1\in(0,\delta_U]$ such that on $U(\delta_1)$: $w_u,w_s\ge\nu_{\min}-\eta_0$;
$\lambda_{\max}(\mathfrak p)\le\vartheta_\Gamma+\eta_0$; $c_{us}\ge c_\Gamma := \frac12\min_\Gamma\{\phi_u,\phi_s\}$;
(T1) holds; and $|2\mathsf t-1|\,|\rho^{-1}\mathsf H\rho|\le\eta_0$ for all $\mathsf t\in[s_0-3,s+3]$. Then on
$U(\delta_1)$, for such $\mathsf t$, as Hermitian matrices,
$$(2\mathsf t-1)\rho^{-1}\mathsf H\rho-2(\mathfrak p-w_u)\ge\tfrac12\nu_{\min},
\qquad(2\mathsf t-1)\rho^{-1}\mathsf H\rho-2\mathfrak p+2\beta w_s\ge2c_0:\tag{4.3}$$
the left side of the first is at least $2(\nu_{\min}-\vartheta_\Gamma)-5\eta_0>\nu_{\min}-5\eta_0$, and that of the
second at least $2(c_0+\eta_0)-\eta_0$.

(c) Cut-offs and regulariser. $\psi$ is the cut-off of the pattern (5) in section 3, and $\theta := (-\psi\psi')^{1/2}$
on $[0,\infty)$, extended evenly; so $\psi\psi'(y)\,y = -\theta(y)^2|y|$. All cut-offs below are functions of
$\phi^u,\phi^s,\rho^2G,\rho_K$ on $\{(x,z)\in O'\}$, and their products are supported in some $U(\delta)$ with
$\delta\le\delta_1$, hence in $\{(x,z)\in O''\}$ by Lemma 4.1 (a); extended by zero, they are symbols in
$C^{(d_0-4)}\tilde S^0$, after multiplication by the function $\chi_\infty$ of the pattern (2), whose derivatives are of
order $-\infty$ and are put into the remainders without comment. The regulariser is $\varphi_\epsilon$ of section 2 with
$\kappa := 2$, and $\Lambda_\epsilon := \frac12(\mathrm{Op}(\varphi_\epsilon)+\mathrm{Op}(\varphi_\epsilon)^*)$, bounded
of order 0 uniformly and of order $-2$ for each $\epsilon$. For a symbol $x$ of order $\mathsf t$,
$\mathrm{Op}(x)\Lambda_\epsilon-\mathrm{Op}(x\varphi_\epsilon)$ is uniformly of order $\mathsf t-1$ (II.A$'$ Proposition
2.4 (b)); this is used without comment.

(d) Half steps. Let $J_0 := 5$, the number of steps that II.A$'$ Lemma 4.2 takes for $\tau = 1$ with $\kappa\le\frac14$.
For $\delta_2\in(0,2^{-J_0-4}\delta_1]$ let $\mathcal A(\delta_2) :=
U(2^{J_0+2}\delta_2)\cap(\{|\phi^u|\ge\delta_2/16\}\cup\{\rho_K\ge\delta_2/16\})$, a closed set disjoint from
$\Gamma^u_{K^+}$ by Lemma 4.1 (a). We show:

(★) Let $s'\in[s_0,s]$ and $\delta_2$ be as above, $G'$ elliptic on $U(2^{J_0+3}\delta_2)$ and microsupported in
$U(\delta_1/4)$, and $E'$ elliptic on $\mathcal A(\delta_2)$ and microsupported in
$U(\delta_1/4)\cap(\{|\phi^u|\ge\delta_2/32\}\cup\{\rho_K\ge\delta_2/32\})$. If $G'u\in H^{s'-\frac12}$, $G'Pu\in
H^{s'}$, $E'u\in H^{s'+1}$ and $\chi u\in H^{-N}$, then $B'u\in H^{s'}$ for every $B'$ microsupported in $U(2\delta_2)$,
and
$$\|B'u\|_{s'}\le C\mathcal K,\qquad\mathcal K := \|G'Pu\|_{s'}+\|E'u\|_{s'+1}+\|G'u\|_{s'-\frac12}+\|\chi u\|_{-N}.$$

Proposition 4.2 follows. Let $J := \lceil2(s-s_0)\rceil$ and $s_j := s_0+j(s-s_0)/J$, so $s_j-s_{j-1}\le\frac12$. Choose
$\delta_2^{(1)}$ so small that $U(2^{J_0+4}\delta_2^{(1)})\subset U_\Gamma$, lies in the region where $\tilde\chi = 1$
and $W' = 1$, and the kernels are carried by $\chi$ in $K\times K$; and $\delta_2^{(j)} := 2^{-J_0-3}\delta_2^{(j-1)}$,
so that $U(2^{J_0+4}\delta_2^{(j)})\subset U(2\delta_2^{(j-1)})$. Step $j$ of (★), at the order $s_j$, has its hypothesis
$G'u\in H^{s_j-\frac12}$ from step $j-1$ (from $\tilde\chi u\in H^{s_0}$ for $j = 1$), as $s_j-\frac12\le s_{j-1}$. Take
$B := B'$ of step $J$, $G$ elliptic on $U(2^{J_0+4}\delta_2^{(1)})$ and microsupported in $U_\Gamma$, and $E$ elliptic on
$\bigcup_j\mathrm{WF}'(E'^{(j)})$, a closed set disjoint from $\Gamma^u_{K^+}$, with $\mathrm{WF}'(E)$ still disjoint
from it. The norms of each step are bounded by the right side of (4.2), with $\|\chi u\|_{-N}\le C\|\tilde\chi
u\|_{s_0}$, and section 1.2 returns the estimate to the weighted spaces. The constants depend on $P$ only through
finitely many norms and the constants of (b) and of II.C$'$ Proposition 3.4, which are uniform for $\epsilon_P$ small
(Remark 1.3); $d_0$ is fixed by the regularity the symbol classes need at the orders in $[s_0-3,s+3]$, plus 4 for Lemma
4.1.

It remains to prove (★). Fix $s'$, $\delta_2$, $G'$, $E'$ and $u$ as there.

*Step 1: the equation for $\Phi_uu$.* Let $\chi_1$ be a cut-off equal to 1 on $U(\delta_1/2)$ and supported in
$U(\delta_1)$, and $\Phi_u := \frac12(\mathrm{Op}(\chi_1\phi^u)+\mathrm{Op}(\chi_1\phi^u)^*)$, scalar, self-adjoint and
of order 0. Put $W_u := \mathrm{Op}(\chi_1w_u\rho^{-1})$ and $R_u := \mathrm{Op}(\chi_1r_u\rho)$. By II.A$'$ Proposition
2.4 (b), (d), (f), $[P,\Phi_u]$ has order 1 and principal symbol $-iH_G(\chi_1\phi^u) = -i\rho^{-1}\mathsf
H(\chi_1\phi^u)$, the commutator of the matrix-valued first-order part of $P$ with the scalar $\Phi_u$ having order 0. By
(4.1) this equals the principal symbol of $iW_u\Phi_u-iR_uP$ on $U(\delta_1/2)$. Hence
$$[P,\Phi_u] = iW_u\Phi_u-iR_uP+R_2+R_2^\flat,\tag{4.4}$$
with $R_2$ of order 0 and $R_2^\flat = \mathrm{Op}(r^\flat)$, $r^\flat\in C^{(d_0-4)}\tilde S^1$ vanishing on
$U(\delta_1/2)$. With $f := Pu$,
$$P'\Phi_uu = (\Phi_u-iR_u)f+R_2u+R_2^\flat u,\qquad P' := P-iW_u.\tag{4.5}$$
$P'$ is $P$ plus the quantisation of a first-order symbol (the remark after Lemma 2.5), and
$\rho\,\sigma_1(\mathrm{Im}\,P') = \mathfrak p-\chi_1w_u$. So for $P'$ the quantity $Q_\epsilon$ of (3.1), with $W' = 1$,
$w = 1$, $A = \mathrm{Id}$ and $\mathfrak p$ for $A^{-1}(\cdots)A$, is $Q'_\epsilon = (2\mathsf
t_\epsilon-1)\rho^{-1}\mathsf H\rho-2(\mathfrak p-w_u)\ge\frac12\nu_{\min}$ on $U(\delta_1/2)$, for every order whose
regularised values $\mathsf t_\epsilon$ lie in $[s_0-3,s+3]$, by (4.3). There is no threshold: the damping $W_u$ makes
$\partial\Gamma_{K^+}$ behave for $P'$ like a radial set above threshold at every order.

(1a) For $\epsilon'\in(0,\delta_1/2]$ let $\Psi_{\epsilon'} :=
\psi(\phi^u/\epsilon')\psi(\phi^s/\epsilon')\psi(\rho^2G/\epsilon')\psi(\rho_K/\epsilon')$, supported in $U(\epsilon')$
and equal to 1 on $U(\epsilon'/2)$. We apply the pattern of section 3 to $P'$ with $\check a := \rho^{-\mathsf
t+\frac12}\Psi_{\epsilon'}$ at an order $\mathsf t$. In $\mathsf H(\Psi_{\epsilon'}^2)$ the factor in $\phi^u$ gives, by
(4.1), $2\theta(\phi^u/\epsilon')^2w_u|\phi^u|/\epsilon'\ge0$ times the squares of the other factors, plus a multiple of
$\rho^2G$; it is a term $+e^*e$, supported in $\{|\phi^u|\ge\epsilon'/2\}$. The factor in $\phi^s$ gives
$-2\theta(\phi^s/\epsilon')^2w_s|\phi^s|/\epsilon'$ times the same, plus a multiple of $\rho^2G$: a term $-b'^*b'$. The
factor in $\rho^2G$ gives a multiple of $G$, as $\mathsf H(\rho^2G) = 2(\rho^{-1}\mathsf H\rho)\rho^2G$. The factor in
$\rho_K$ gives $2\theta(\rho_K/\epsilon')^2(-\mathsf H\rho_K)/\epsilon'$ times the same, $\ge0$ by (T1): a term $+e^*e$,
supported in $\{\rho_K\ge\epsilon'/2\}$. Multiples of $G$ are $j_\epsilon\ell$. So (2.2) holds with $b_\epsilon :=
\rho^{-\mathsf t}\varphi_\epsilon\Psi_{\epsilon'}Q'^{1/2}_\epsilon$ and $E$-symbols supported in
$\{|\phi^u|\ge\epsilon'/2\}\cup\{\rho_K\ge\epsilon'/2\}$. Lemmas 2.1-2.3, and Lemma 2.2 with the interiors of the sets
$U(2^{-j}\cdot2^{J_0+2}\delta_2)$, $0\le j\le J_0$, in the proof of II.A$'$ Lemma 4.2 (which needs open sets), and with
$\epsilon' := 2^{J_0+3-j}\delta_2$ at its step $j\ge1$, so that the commutant is supported in the $(j-1)$st set and
equals 1 on the $j$th while its $E$-sets, in $\{|\phi^u|\ge4\delta_2\}\cup\{\rho_K\ge4\delta_2\}$, miss $U(2\delta_2)$,
give, in the strong sense,
$$\|B_1v\|_{\mathsf t}\le C\big(\|G_1P'v\|_{\mathsf t-1}+\|E_1v\|_{\mathsf t}+\|G_1v\|_{\mathsf t-1}+
\|\chi v\|_{-N}\big),$$
with $B_1$ elliptic on $U(2\delta_2)$, $G_1$ elliptic on $U(2^{J_0+2}\delta_2)$ and microsupported in
$U(2^{J_0+3}\delta_2)$, and $E_1$ microsupported in $\mathcal A(\delta_2)$, where $|\phi^u|\ge\delta_2$ or
$\rho_K\ge\delta_2$ on the $E$-sets used. Apply this with $v := \Phi_uu$ and $\mathsf t := s'+\frac12$. By (4.5),
$G_1R_2^\flat$ having every order, $\|G_1P'v\|_{s'-\frac12}\le C(\|G'f\|_{s'}+\|G'u\|_{s'-\frac12}+\|\chi u\|_{-N})$;
$\|G_1v\|_{s'-\frac12}\le C(\|G'u\|_{s'-\frac12}+\|\chi u\|_{-N})$; and
$\|E_1v\|_{s'+\frac12}\le\|\Phi_uE_1u\|_{s'+\frac12}+\|[E_1,\Phi_u]u\|_{s'+\frac12}\le C(\|E'u\|_{s'+1}+\|\chi
u\|_{-N})$, the commutator having order $-1$ and $E'$ being elliptic on $\mathrm{WF}'(E_1)$. Hence
$$\|B_1\Phi_uu\|_{s'+\frac12}\le C\mathcal K.\tag{4.6}$$

(1b) Now take $\epsilon' := \delta_2$, $\Psi := \Psi_{\delta_2}$, $\mathsf t := s'+1$ and the regulariser: $\check
a_\epsilon := \varphi_\epsilon\rho^{-s'-\frac12}\Psi$, $b_\epsilon := \rho^{-s'-1}\varphi_\epsilon\Psi
Q'^{1/2}_\epsilon$, $B_\epsilon := \mathrm{Op}(b_\epsilon)$. Lemma 2.3 gives (2.1) for $P'$ at the order $s'+1$. By (4.6)
and (4.5), $G''v\in H^{s'+\frac12}$ and $G''P'v\in H^{s'-\frac12}$ for $G''$ elliptic on $U(\delta_2)$ and microsupported
in $U(2\delta_2)$. So (2.1) holds at $v = \Phi_uu$, by the approximation of Steps 1-2 of the proof of II.A$'$ Lemma 4.1
(for fixed $\epsilon$ every operator in (2.1) has its order lowered by $\kappa = 2$), and the pairing identity at the end
of section 2 applies. Thus
$$\|B_\epsilon v\|^2\le2|\langle\check A_\epsilon P'v,\check A_\epsilon v\rangle|+\|E_\epsilon v\|^2+
2|\langle J_\epsilon P'v,v\rangle|+C\big(\|G''v\|^2_{s'+\frac12}+\|\chi v\|^2_{-N}\big).$$
We bound the terms. (i) As in (a) of Step 2 of the proof of II.A$'$ Lemma 4.1, $\|\check A_\epsilon v\|_{\frac12}\le
C\|B_\epsilon v\|+C\|G''v\|_{s'+\frac12}$. (ii) $\check A_\epsilon-\mathrm{Op}(\rho^{-s'-\frac12}\Psi)\Lambda_\epsilon$
is uniformly of order $s'-\frac12$, so $\|\check A_\epsilon P'v\|_{-\frac12}\le C(\|G''\Lambda_\epsilon
P'v\|_{s'}+\|G''P'v\|_{s'-1}+\|\chi u\|_{-N})$. In (4.5), $\Lambda_\epsilon R_2 =
R_2\Lambda_\epsilon+[\Lambda_\epsilon,R_2]$ with the commutator uniformly of order $-1$ (II.A$'$ Proposition 2.4 (d)),
and $G''R_2^\flat$ has every order. So
$$\|G''\Lambda_\epsilon P'v\|_{s'}\le C\big(\|G'f\|_{s'}+X_\epsilon+\|G'u\|_{s'-\frac12}+\|\chi u\|_{-N}\big),
\qquad X_\epsilon := \|\mathrm{Op}(\rho^{-s'}\varphi_\epsilon g_0)u\|,$$
with $g_0$ a cut-off equal to 1 on $U(2\delta_2)$ and supported in $U(4\delta_2)$. (iii) $\|E_\epsilon v\|\le
C(\|E'u\|_{s'+1}+\|\chi u\|_{-N})$ as in (b) there, the $E$-symbols being supported in
$\{|\phi^u|\ge\delta_2/2\}\cup\{\rho_K\ge\delta_2/2\}$, inside $\mathcal A(\delta_2)$. (iv) $J_\epsilon$ is uniformly of
order $2s'$, so $|\langle J_\epsilon P'v,v\rangle|\le C\|G''P'v\|_{s'-\frac12}\|G''v\|_{s'+\frac12}+C\|\chi u\|^2_{-N}\le
C\mathcal K^2$ by (4.6). (v) The last term is at most $C\mathcal K^2$ by (4.6). Absorbing $\frac12\|B_\epsilon v\|^2$,
which is finite for $\epsilon>0$,
$$\|B_\epsilon\Phi_uu\|\le C(X_\epsilon+\mathcal K)\qquad\text{for all }\epsilon\in(0,1].\tag{4.7}$$

*Step 2: concentration at $\{\phi^s = 0\}$.* Let $\delta_4 := \delta_2/4$ and $\delta\in(0,\delta_4/16]$, fixed in
Step 4. Let $\Theta\in C^\infty(\mathbb R)$ be non-decreasing, with $\Theta = 0$ on $(-\infty,-8]$, $\Theta = 1$ on
$[8,\infty)$, $\Theta'>0$ on $(-8,8)$, $\Theta(y) = c_1e^{-1/(y+8)}$ near $-8$ and $1-\Theta(y) = c_2e^{-1/(8-y)}$ near
$8$; such $\Theta$ exist for $c_1+c_2<e$: with $T_\mp$ the two prescribed tails, put $\Theta' :=
\varkappa_-T_-'+m\varkappa_0+\varkappa_+T_+'$ on $(-8,8)$, for a partition of unity $\varkappa_-+\varkappa_0+\varkappa_+
= 1$ there with $\varkappa_\mp = 1$ near $\mp8$ and supported within distance 1 of $\mp8$, and $m>0$ fixed by
$\int\Theta' = 1$, possible as the two tail terms contribute at most $(c_1+c_2)e^{-1}<1$; and $\check\Theta :=
\Theta^{1/2}$ and $\theta_\Theta := \Theta'^{1/2}$ are smooth. Let $c_\Theta := \min_{[-4,4]}\Theta'>0$. Put
$$\psi_\delta(y) := \Theta(y/\delta)\,\psi(y/\delta_4)^2,\qquad\bar\chi :=
\psi(\phi^u/\delta_4)\psi(\rho^2G/\delta_4)\psi(\rho_K/\delta_4),$$
$\tilde a := \rho^{-2s'-1}\psi_\delta(\phi^s)\bar\chi^2$, $\tilde A := \frac12(\mathrm{Op}(\tilde a)+\mathrm{Op}(\tilde
a)^*)$ and $A_\epsilon := \Lambda_\epsilon\tilde A\Lambda_\epsilon$. $\psi_\delta(\phi^s)\bar\chi$ is supported in
$U(\delta_4)\cap\{\phi^s\ge-8\delta\}$, where $\chi_1 = 1$ and $\Psi = 1$. As $\delta\le\delta_4/16$, $\psi(y/\delta_4) =
1$ on $\mathrm{supp}\,\Theta'(\cdot/\delta)\subset[-8\delta,8\delta]$, and on
$\mathrm{supp}\,\psi'(\cdot/\delta_4)\subset\{\frac12\delta_4\le|y|\le\delta_4\}$, $\Theta(y/\delta)$ is 1 for $y>0$ and
0 for $y<0$. Hence
$$\psi_\delta'(y) = \delta^{-1}\theta_\Theta(y/\delta)^2-2\delta_4^{-1}\theta(y/\delta_4)^2\,1_{y>0}.\tag{4.8}$$

*The identity.* For fixed $\epsilon$, $A_\epsilon$ has order $2s'-3$, so both sides of
$2\,\mathrm{Im}\langle\Phi_uu,A_\epsilon u\rangle = \langle i[\Phi_u,A_\epsilon]u,u\rangle$ are continuous for $u$ with
$G'u\in H^{s'-\frac12}$ and $\chi u\in H^{-N}$, and the identity, which holds for smooth $u$ as $\Phi_u$ and $A_\epsilon$
are self-adjoint, holds at our $u$. By II.A$'$ Proposition 2.4 (b), (d), $i[\Phi_u,A_\epsilon] =
\mathrm{Op}(H_{\phi^u}(\varphi_\epsilon^2\tilde a))+R_{\epsilon,\delta}$, with $R_{\epsilon,\delta}$ uniformly of order
$2s'-1$. By II.A$'$ (2.1) with $V = H_{\phi^u}$, by $H_{\phi^u}\phi^u = 0$ and by (4.8), near fibre infinity,
$$H_{\phi^u}(\varphi_\epsilon^2\tilde a) =
\rho^{-2s'}\varphi_\epsilon^2\Big(\delta^{-1}\theta_\Theta(\phi^s/\delta)^2c_{us}\bar\chi^2+
\psi_\delta(\phi^s)k_\epsilon\Big)+\rho^{-2s'}\varphi_\epsilon^2\Big(-2\delta_4^{-1}\theta(\phi^s/\delta_4)^2\,
1_{\phi^s>0}\,c_{us}\bar\chi^2\Big),\tag{4.9}$$
with $k_\epsilon := \rho^{-1}H_{\phi^u}(\bar\chi^2)-(2s'+1-2\kappa\theta_\epsilon)(\rho^{-2}H_{\phi^u}\rho)\bar\chi^2$.
$k_\epsilon$ is bounded with its derivatives independently of $\epsilon$ and $\delta$, $\rho^{-2}H_{\phi^u}\rho$ being
homogeneous of degree 0; in $\rho^{-1}H_{\phi^u}(\bar\chi^2)$ only the factors in $\rho^2G$ and $\rho_K$ are
differentiated. Let
$$B_\delta^\epsilon := \mathrm{Op}\big(\rho^{-s'}\varphi_\epsilon\theta_\Theta(\phi^s/\delta)c_{us}^{1/2}\bar\chi\big),
\quad E_2^\epsilon :=
\mathrm{Op}\big(\rho^{-s'}\varphi_\epsilon\theta(\phi^s/\delta_4)1_{\phi^s>0}c_{us}^{1/2}\bar\chi\big),
\quad Z^\epsilon := \mathrm{Op}\big(\rho^{-s'}\varphi_\epsilon\check\Theta(\phi^s/\delta)\psi(\phi^s/\delta_4)g_1\big),$$
with $g_1$ a cut-off equal to 1 on $\mathrm{supp}\,\bar\chi$, supported in $\{|\phi^u|,|\rho^2G|,\rho_K\le2\delta_4\}$.
Quantising (4.9) by II.A$'$ Proposition 2.4 (b), (c), with $\psi_\delta k_\epsilon = (\check\Theta\psi)^2g_1k_\epsilon
g_1$,
$$\delta^{-1}\|B_\delta^\epsilon u\|^2 = 2\,\mathrm{Im}\langle\Phi_uu,A_\epsilon u\rangle+
2\delta_4^{-1}\|E_2^\epsilon u\|^2-\langle\mathrm{Op}(k_\epsilon)Z^\epsilon u,Z^\epsilon u\rangle+
O(C_\delta\mathcal K^2),\tag{4.10}$$
the remainders being uniformly of order $2s'-1$ and so bounded by $C_\delta(\|G'u\|^2_{s'-\frac12}+\|\chi u\|^2_{-N})$.

*The pairing.* $\tilde A =
\mathrm{Op}(\rho^{-s'-1}\check\Theta\psi\bar\chi)^*\mathrm{Op}(\rho^{-s'}\check\Theta\psi\bar\chi)+R$, with $R$ of order
$2s'$ (here $\check\Theta\psi$ is evaluated at $\phi^s$, with the arguments of the definition). As $\Lambda_\epsilon$ is
self-adjoint, $\langle\Phi_uu,A_\epsilon u\rangle = \langle\Lambda_\epsilon\Phi_uu,\tilde A\Lambda_\epsilon u\rangle$,
and $|\langle\Lambda_\epsilon\Phi_uu,R\Lambda_\epsilon u\rangle|\le
C_\delta\|G''\Phi_uu\|_{s'+\frac12}\|G'u\|_{s'-\frac12}+C\|\chi u\|^2_{-N}\le C_\delta\mathcal K^2$ by (4.6). So
$$2|\langle\Phi_uu,A_\epsilon u\rangle|\le2\|\mathrm{Op}(\rho^{-s'-1}\varphi_\epsilon\check\Theta\psi\bar\chi)\Phi_uu\|\,
\|\mathrm{Op}(\rho^{-s'}\varphi_\epsilon\check\Theta\psi\bar\chi)u\|+C_\delta\mathcal K^2.$$
On the support of $\check\Theta\psi\bar\chi$, $\Psi = 1$ and $Q'_\epsilon\ge\frac12\nu_{\min}$, so Lemma 2.5 with (4.6)
and (4.7) bounds the first factor by $C\|B_\epsilon\Phi_uu\|+C_\delta\mathcal K\le C(X_\epsilon+\mathcal
K)+C_\delta\mathcal K$, and, with $q_1 := \bar\chi$, it bounds the second by $2\|Z^\epsilon u\|+C_\delta\mathcal K$.
(2.3) gives $|\langle\mathrm{Op}(k_\epsilon)Z^\epsilon u,Z^\epsilon u\rangle|\le C\|Z^\epsilon u\|^2+C_\delta\mathcal
K^2$. With (4.10),
$$\|B_\delta^\epsilon u\|^2\le C\delta\big((X_\epsilon+\mathcal K)\|Z^\epsilon u\|+\|E_2^\epsilon u\|^2+
\|Z^\epsilon u\|^2\big)+C_\delta\mathcal K^2.\tag{4.11}$$
This is the commutator form of I.B (6.9): $u$ is small near $\{\phi^s = 0\}$, by the factor $\sqrt\delta$, because
$\Phi_uu$ is one order smoother than $u$ (Step 1) and $H_{\phi^u}$ crosses $\{\phi^s = 0\}$ transversally, at the rate
$c_{us}$.

*Step 3: propagation away from $\{\phi^s = 0\}$.* Let $R_3 := \delta_3 := 16\delta_2$, and for $t\ge0$ let $F(t) :=
\Upsilon(t/\delta)\psi(t/R_3)$ with $\Upsilon(\tau) := \Theta(32\tau-24)$: $\Upsilon = 0$ on $[0,\frac12]$, $\Upsilon =
1$ on $[1,\infty)$, and $\Upsilon\Upsilon' = 32(\check\Theta\theta_\Theta)^2(32\tau-24)$. Let $\bar\chi_3 :=
\psi(\phi^u/\delta_3)\psi(\rho^2G/\delta_3)\psi(\rho_K/\delta_3)$ and $\check a := \rho^{-s'+\frac12}\Psi_3$, $\Psi_3
:= |\phi^s|^{-\beta}F(|\phi^s|)\bar\chi_3$, which is smooth because $F(|\phi^s|)$ vanishes for $|\phi^s|\le\delta/2$. We
apply the pattern (3.1) to $P$ at the order $s'$, with $W' = 1$, $w = 1$, $A = \mathrm{Id}$, so $Q_\epsilon =
(2s'_\epsilon-1)\rho^{-1}\mathsf H\rho-2\mathfrak p$. By (4.1), off $\{\phi^s = 0\}$, $\mathsf H(|\phi^s|^{-2\beta}) =
-2\beta|\phi^s|^{-2\beta}(w_s+r_s\rho^2G/\phi^s)$ and $\mathsf H(F(|\phi^s|)^2) =
2FF'(|\phi^s|)(|\phi^s|w_s+\mathrm{sgn}(\phi^s)r_s\rho^2G)$. As $\delta<R_3/2$, $\psi(\cdot/R_3) = 1$ on
$\mathrm{supp}\,\Upsilon'(\cdot/\delta)\subset[\frac\delta2,\delta]$, and $\Upsilon(\cdot/\delta) = 1$ on
$\mathrm{supp}\,\psi'(\cdot/R_3)$; so $2FF'(t)\,t\,w_s = e_3(t)^2-b_3(t)^2$ with
$$e_3(t)^2 := 64\,(t/\delta)\,(\check\Theta\theta_\Theta)^2(32t/\delta-24)\,w_s,\qquad b_3(t)^2 := 2\,(t/R_3)\,
\theta(t/R_3)^2\,w_s.$$
Hence
$$-\Psi_3^2Q_\epsilon+\mathsf H(\Psi_3^2) = -\Psi_3^2(Q_\epsilon+2\beta w_s)+
\bar\chi_3^2|\phi^s|^{-2\beta}\big(e_3^2-b_3^2\big)(|\phi^s|)+F^2|\phi^s|^{-2\beta}\,\mathsf H(\bar\chi_3^2)+j\,\rho^2G,
$$
with $j$ smooth, and $Q_\epsilon+2\beta w_s\ge2c_0$ on the support by (4.3). In $\mathsf H(\bar\chi_3^2)$, as in Step 1,
the factor in $\phi^u$ gives a nonnegative square supported in $\{|\phi^u|\ge\delta_3/2\}$ plus a multiple of $\rho^2G$,
the factor in $\rho_K$ a nonnegative square supported in $\{\rho_K\ge\delta_3/2\}$, and the factor in $\rho^2G$ a
multiple of $G$. So (2.2) holds with $b_\epsilon := \rho^{-s'}\varphi_\epsilon\Psi_3(Q_\epsilon+2\beta w_s)^{1/2}$, one
$b'$-term $\rho^{-s'}\varphi_\epsilon|\phi^s|^{-\beta}\bar\chi_3b_3(|\phi^s|)$, the $e$-term
$\rho^{-s'}\varphi_\epsilon|\phi^s|^{-\beta}\bar\chi_3e_3(|\phi^s|)$, $e$-terms supported in
$\{|\phi^u|\ge\delta_3/2\}\cup\{\rho_K\ge\delta_3/2\}$, and $j_\epsilon$ collecting the multiples of $G$. By Lemma 2.3,
(2.1) holds, and it holds at $u$ by the approximation of Step 1, as $G'u\in H^{s'-\frac12}$ and $G'Pu\in H^{s'}$. In it,
$\check A_\epsilon$ is uniformly of order $s'-\frac12$, so $2|\langle\check A_\epsilon Pu,\check A_\epsilon
u\rangle|\le2\|\check A_\epsilon Pu\|_{\frac12}\|\check A_\epsilon u\|_{-\frac12}\le
C_\delta(\|G'Pu\|_{s'}\|G'u\|_{s'-1}+\|\chi u\|^2_{-N})$. This is where $Pu\in H^{s'}$, one order more than real
principal type needs, is used. $|\langle J_\epsilon Pu,u\rangle|\le C_\delta\mathcal K^2$, as $J_\epsilon$ is uniformly
of order $2s'-2$. The $e$-terms in $\{|\phi^u|\ge\delta_3/2\}\cup\{\rho_K\ge\delta_3/2\}$ lie in $\mathcal A(\delta_2)$
and are at most $C_\delta(\|E'u\|_{s'}+\|\chi u\|_{-N})$. So, with $B_3^\epsilon := \mathrm{Op}(b_\epsilon)$ and
$E_3^\epsilon := \mathrm{Op}(\rho^{-s'}\varphi_\epsilon|\phi^s|^{-\beta}\bar\chi_3e_3(|\phi^s|))$,
$$\|B_3^\epsilon u\|^2\le\|E_3^\epsilon u\|^2+C_\delta\mathcal K^2.\tag{4.12}$$
Let $M^\epsilon := \mathrm{Op}(\rho^{-s'}\varphi_\epsilon F(|\phi^s|)\bar\chi_3)$. After the factor
$\rho^{-s'}\varphi_\epsilon$ its symbol is $z := F(|\phi^s|)\bar\chi_3$, and that of $B_3^\epsilon$ is $x_1 :=
\Psi_3(Q_\epsilon+2\beta w_s)^{1/2}$. Let $\zeta$ be a cut-off equal to 1 near $\mathrm{supp}\,z$ and supported in
$\{\frac\delta4<|\phi^s|<2R_3\}$ and in a neighbourhood of $\mathrm{supp}\,\bar\chi_3\cap\{|\phi^s|\le2R_3\}$ inside the
interior of $U(\delta_1)$, where (4.3) holds (D327), so that $Q_\epsilon+2\beta w_s\ge c_0$ on $\mathrm{supp}\,\zeta$
(D326), and $q_1 := \zeta|\phi^s|^\beta(Q_\epsilon+2\beta w_s)^{-1/2}$. Then $z = q_1x_1$ near $\mathrm{supp}\,z$, and
$\sup|q_1|\le (2R_3)^\beta c_0^{-1/2}$, independently of $\delta$ and $\epsilon$; so Lemma 2.5 in its general form gives
$\|M^\epsilon u\|\le CR_3^\beta\|B_3^\epsilon u\|+C_\delta\mathcal K$, $\delta$ entering through the derivatives of
$|\phi^s|^\beta$ near $|\phi^s| = \frac\delta4$. Its particular case does not apply, as $x_1$ vanishes where $z$ does
(the eighty-fourth verifier, D204). The symbol of $E_3^\epsilon$ is supported in
$\{\frac\delta2\le|\phi^s|\le\delta\}\cap\mathrm{supp}\,\bar\chi_3$, where $|\phi^s|^{-\beta}e_3\le C\delta^{-\beta}$:
the propagation runs from the shell $|\phi^s|\sim\delta$ outward, along which $|\phi^s|$ grows, and the weight
$|\phi^s|^{-\beta}$ costs $\delta^{-\beta}$.

*Step 4: conclusion.* Put $\mathcal N_\epsilon := \|B_\delta^\epsilon u\|+\|M^\epsilon u\|$, finite for each
$\epsilon>0$, as for fixed $\epsilon$ these operators have order $s'-2$. The symbol of $B_\delta^\epsilon$ is at least
$(c_\Theta c_\Gamma)^{1/2}\rho^{-s'}\varphi_\epsilon$ on $\mathcal U_B :=
\{|\phi^s|\le4\delta,\ |\phi^u|,|\rho^2G|,\rho_K\le\delta_4/2\}$, and that of $M^\epsilon$ equals
$\rho^{-s'}\varphi_\epsilon$ on $\mathcal U_M :=
\{\delta\le|\phi^s|\le8\delta_2,\ |\phi^u|,|\rho^2G|,\rho_K\le8\delta_2\}$. $E'$ is elliptic on $\mathcal A(\delta_2)$,
which contains $U(16\delta_2)\cap(\{|\phi^u|\ge\delta_4/4\}\cup\{\rho_K\ge\delta_4/4\})$, and $P$ is elliptic on
$\{|\rho^2G|\ge\delta_4/4\}$. A point of $U(16\delta_2)$ with $|\phi^s|\ge\delta$ and
$|\phi^s|,|\phi^u|,|\rho^2G|,\rho_K\le8\delta_2$ lies in $\mathcal U_M$; one with $|\phi^s|<2\delta$ lies in $\mathcal
U_B$ or has one of $|\phi^u|,\rho_K,|\rho^2G|$ above $\delta_4/2$. So these four sets cover, with room, $U(8\delta_2)$
and $U(16\delta_2)\cap\{|\phi^s|\le\delta\}$, and on each the corresponding symbol is bounded below independently of
$\delta$. Lemma 2.5, with the elliptic estimates $\|\mathrm{Op}(\rho^{-s'}\varphi_\epsilon e')u\|\le
C(\|E'u\|_{s'}+\|\chi u\|_{-N})$ for $e'$ supported in $\mathrm{Ell}(E')$, and $\|\mathrm{Op}(\rho^{-s'}\varphi_\epsilon
e'')u\|\le C(\|G'Pu\|_{s'-2}+\|G'u\|_{s'-1}+\|\chi u\|_{-N})$ for $e''$ supported in $\mathrm{Ell}(P)$ (II.A$'$ Theorem
3.1 for $\Lambda_\epsilon u$, $[P,\Lambda_\epsilon]$ being uniformly of order 1), gives
$$\|\mathrm{Op}(\rho^{-s'}\varphi_\epsilon z)u\|\le C(\mathcal N_\epsilon+\mathcal K)+C_\delta\mathcal K\tag{4.13}$$
for every symbol $z$ with $|z|\le1$ supported in $U(4\delta_2)$, with $C$ independent of $\delta$; and, for $z$ supported
in $U(16\delta_2)\cap\{|\phi^s|\le\delta\}$, which needs only $\mathcal U_B$ and the last two sets, the same with
$\|B_\delta^\epsilon u\|$ in place of $\mathcal N_\epsilon$. The first form applies to $X_\epsilon$, to $Z^\epsilon$ and
to $E_2^\epsilon$ (supported in $U(\delta_2/2)$), the second to $\delta^\beta E_3^\epsilon$. So by (4.11),
$\|B_\delta^\epsilon u\|\le C\delta^{\frac12}(\mathcal N_\epsilon+\mathcal K)+C_\delta\mathcal K$. By the second form,
$\|E_3^\epsilon u\|\le C\delta^{-\beta}(\|B_\delta^\epsilon u\|+\mathcal K)+C_\delta\mathcal K$, so by Step 3 and (4.12),
$\|M^\epsilon u\|\le CR_3^\beta\|B_3^\epsilon u\|+C_\delta\mathcal K\le CR_3^\beta\delta^{-\beta}\|B_\delta^\epsilon
u\|+C_\delta\mathcal K$. Together,
$$\mathcal N_\epsilon\le C_9\big(\delta^{\frac12}+R_3^\beta\delta^{\frac12-\beta}\big)(\mathcal N_\epsilon+\mathcal K)+
C_\delta\mathcal K,$$
with $C_9$ independent of $\delta$ and $\epsilon$. Since $\beta<\frac12$, we can fix $\delta\in(0,\delta_4/16]$ with
$C_9(\delta^{\frac12}+R_3^\beta\delta^{\frac12-\beta})\le\frac12$, and then $\mathcal N_\epsilon\le C\mathcal K$ for all
$\epsilon\in(0,1]$. By (4.13) with $z = g_0$, $X_\epsilon\le C\mathcal K$ for all $\epsilon$. As in Step 3 of the proof
of II.A$'$ Lemma 4.1, $\mathrm{Op}(\rho^{-s'}\varphi_\epsilon g_0)u\to\mathrm{Op}(\rho^{-s'}g_0)u$ in $\mathcal D'$ while
staying bounded in $L^2$, so $\mathrm{Op}(\rho^{-s'}g_0)u\in L^2$ with norm at most $C\mathcal K$. $g_0 = 1$ on
$U(2\delta_2)$, so the elliptic estimate gives (★) for $B'$ microsupported in $U(2\delta_2)$. $\square$

The constant $\vartheta_\Gamma<\frac12\nu_{\min}$ enters twice, as in I.B section 6.4: in Step 1, through
$\nu_{\min}-\vartheta_\Gamma>0$, and in Step 4, through $\beta<\frac12$ with $\beta\nu_{\min}>\vartheta_\Gamma$, which is
what lets the loss $\delta^{-\beta}$ of Step 3 be paid by the gain $\delta^{1/2}$ of Step 2.

## 5. Proof of Theorem 1.2

Let $u$ be as in Theorem 1.2 with the right side of (1.4) finite, and write $\mathcal R$ for that right side. Extended by
zero, $u$ and $Pu$ are supported in $\{t^\flat_*\ge1\}$ (section 1.1). Below, $\|\cdot\|_{\mathsf t}$ is the norm of
$H^{\mathsf t,(2\alpha_I,\alpha_+,\alpha_K)}_{e3b}$, and $Pu$ is measured in $H^{\mathsf
t,(2\alpha_I+2,\alpha_++2,\alpha_K)}_{e3b}$, which is the measure of $Lu = W^{-1}Pu$ in $H^{\mathsf t}$ with the weights
of $u$ (section 1.1). We say $u$ is *controlled at order* $\mathsf t$ on an open set $V\subset{}^{e3b}S^*M$ if
$\|Bu\|_{\mathsf t}\le C\mathcal R$, in the strong sense, for every $B\in C^\infty_b\Psi^0_{e3b}$ carried by $\chi$ with
$\mathrm{WF}'(B)\subset V$. Off the characteristic set $u$ is controlled at every order up to $\mathsf s+1$ (II.A$'$
Theorem 3.1), so only $\partial\Sigma^\pm$ matter. We treat $\partial\Sigma^+$; on $\partial\Sigma^-$ the future field is
$-\mathsf H$, and the same steps apply to the antipodal images of the sets below, for which sections 3 and 4 prove the
same estimates.

Three facts are used throughout. (P1) *Propagation.* II.A$'$ Theorem 5.4, for $L$ and with the weights put into the
operator as in section 1.2: control at order $\mathsf t$ on an open set $V$ gives control at order $\mathsf t$ at every
$\varpi$ whose backward $\mathsf H$-curve enters $V$ in finite time, provided $\mathsf H\mathsf t\le0$ along it and $Pu$
is in $H^{\mathsf t-1}$ near it; for a compact set of such $\varpi$ the entrance times are bounded, the flow being
continuous on the compactified bundle. The orders $\mathsf s$ and $\mathsf s+1$ are non-increasing along the future flow
on $\partial\Sigma^+$ for $P$ (II.C Proposition 5.1 (2)). (P2) *Initial surface.* As $u = 0$ in $\{t^\flat_*<1\}$, $u$ is
controlled at every order there. (P3) *Dynamics.* Over $M^\circ$ every backward curve in $\partial\Sigma^+$ reaches
$\{t^\flat_* = 1\}$ at a finite parameter (II.C Proposition 4.2); over $\partial M$ the curves are those of $P_0$ (II.C
Lemma 4.1), described by II.B Proposition 8.1, whose table we use with its notation $R_{\mathcal H}$,
$R^I_{\mathrm{in}}$, $R^K_{\mathrm{in}}$, $\Gamma_K$, $R^K_{\mathrm{out}}$, $R^I_{\mathrm{out}}$.

*Step 1: finite times.* Let $t^\sharp\in(1,\infty)$ and $\mathcal V_{\mathrm{out}}$ a neighbourhood of $\partial
R_{\mathscr I^+,\mathrm{out}}$. Then $u$ is controlled at order $\mathsf s+1$ on a neighbourhood of every compact subset
of $\partial\Sigma^+$ over $\Omega_*\cap\{t^\flat_*\le t^\sharp\}$ disjoint from $\mathcal V_{\mathrm{out}}$, with $C$
depending on $t^\sharp$ and $\mathcal V_{\mathrm{out}}$. Indeed, a point over $M^\circ$ has its backward curve reach
$\{t^\flat_*<1\}$ by (P3). A point over $\mathscr I^+$ at finite $t_*$, not in $\partial R_{\mathscr I^+,\mathrm{out}}$,
lies on a curve of the first row of the table, which reaches $\{t_* = 1\}$ backward, and $t^\flat_* = t_*$ there (II.C
Lemma 3.2 (a)). (P1) at order $\mathsf s+1$, with $Pu\in H^{\mathsf s}$, and (P2) give the claim. Points of $\partial
R_{\mathscr I^+,\mathrm{out}}$ are fixed by the flow and are left to Step 6. The source propagates into them already
here, by its Proposition 7.9 with finite $t_{*,+}$; section 6, (D2).

*Step 2: the horizon and $\partial R_{\mathscr I^+,\mathrm{in},+}$.* Proposition 3.1 with the orders $(\mathsf
s+1,\mathsf s_0)$, which are constant near $\partial R_{\mathcal H^+}$, with $\mathsf s_0>\frac12+\vartheta_{\mathcal H}$
as $\mathsf s_0$ is admissible (II.C Definition 2.4 (4)), and Proposition 3.5 with the same orders, whose condition (3.7)
is (1.3), have their $E$ supported at finite times: in $\{\rho_K\ge(2\mathfrak M)^{-1}\}$, resp. $\{\rho_+\ge(2\mathfrak
M)^{-1}\}$. The $E$ of Proposition 3.5 is microsupported near $\hat\xi = 2$, so away from $\partial R_{\mathscr
I^+,\mathrm{out}} = \{\hat\xi = 0\}$, and that of Proposition 3.1 lies over a neighbourhood of the horizon, away from
$\mathscr I^+$. So Step 1, with $t^\sharp$ large and $\mathcal V_{\mathrm{out}}$ small, bounds $\|Eu\|_{\mathsf s+1}$,
and $u$ is controlled at order $\mathsf s+1$ on neighbourhoods $V_{\mathcal H}$ of $\partial R_{\mathcal H^+}$ and $V_I$
of $\partial R_{\mathscr I^+,\mathrm{in},+}$.

*Step 3: $\partial R_{\partial K^+,\mathrm{in}}$.* Proposition 3.2 with the orders $(\mathsf s+1,\mathsf s_0)$, where
(3.3) holds as $\mathsf s_0$ is admissible (II.C Definition 2.4 (6)). Its $E$ has kernel supported away from $K^+$, near
$\partial K^+$, and is microsupported in a small neighbourhood of $\partial R_{\partial K^+,\mathrm{in}}$ where
$\rho_K^{-1}\mathsf H\rho_K\le-1$. Let $\varpi\in\mathrm{WF}'(E)\cap\partial\Sigma^+$. Over $M^\circ$, its backward curve
reaches $\{t^\flat_*<1\}$ (P3). Over $(\iota^+)^\circ$, $\rho_K$ increases backward from $\varpi$, and it keeps
increasing: a backward critical point of $\rho_K$ with $\rho_K>0$ would be a local maximum along the curve, against
$\mathsf H^2\rho_K>0$ there (II.B Lemma 3.3 (3)). So the curve does not tend to $R^K_{\mathrm{out}}$ backward, where
$\rho_K = 0$, and by the table over $(\iota^+)^\circ$ it tends to $R^I_{\mathrm{in}}$, entering $V_I$. Points over
$\mathscr I^+$ do not occur, $\partial K^+$ being away from $\mathscr I^+$. (P1) at order $\mathsf s+1$ from $V_I$ and
(P2) bound $\|Eu\|_{\mathsf s+1}$, and $u$ is controlled at order $\mathsf s+1$ on a neighbourhood $V_K$ of $\partial
R_{\partial K^+,\mathrm{in}}$.

*Step 4: the trapped set.* Proposition 4.2 with the orders $(\mathsf s,\mathsf s_0)$, constant over $\{r\le r_\Gamma\}$
(II.C Definition 2.4 (3)), with $U_\Gamma\subset\Phi_1(O)$ small and $Pu\in H^{\mathsf s}$. Let
$\varpi\in\mathrm{WF}'(E)\cap\partial\Sigma^+$. Over $M^\circ$, its backward curve reaches $\{t^\flat_*<1\}$. Over
$(K^+)^\circ$, $\varpi\notin\Gamma^u_{K^+}$, so $\varpi$ is not in the global unstable set $\partial\bar\Gamma^u_{K^+}$,
as $\partial\bar\Gamma^u_{K^+}\cap\Phi_1(O) = \Gamma^u_{K^+}$ (II.B Lemma 5.2 (b), from the no-return condition (H8)
(b)); by II.B Proposition 6.1 (2) its curve tends backward to $\partial R_{\mathcal H^+}$ or $\partial R_{\partial
K^+,\mathrm{in}}$, entering $V_{\mathcal H}\cup V_K$. As $\mathrm{WF}'(E)$ is compact and the entrance times are locally
bounded, (P1) at order $\mathsf s+1$ and (P2) bound $\|Eu\|_{\mathsf s+1}$. So $u$ is controlled at order $\mathsf s$ on
a neighbourhood $V_\Gamma$ of $\partial\Gamma_{K^+}$. This is the step that needs $Pu$ in $H^{\mathsf s}$, and the reason
Steps 1-3 work at the order $\mathsf s+1$.

*Step 5: $\partial R_{\partial K^+,\mathrm{out}}$.* Proposition 3.3 with the orders $(\mathsf s,\mathsf s_0)$, with (3.5)
from II.C Definition 2.4 (5), at the order $\mathsf s$ itself, the threshold being an upper bound. Its $E$ is
microsupported near $\partial R_{\partial K^+,\mathrm{out}}$ with $\mathrm{WF}'(E)\cap\partial W_{\mathrm{out}} =
\emptyset$. Let $\varpi\in\mathrm{WF}'(E)\cap\partial\Sigma^+$. Over $\partial K^+$ its curve is of type
$(R^K_{\mathrm{in}},R^K_{\mathrm{out}})$ and enters $V_K$ backward. Over $(K^+)^\circ$, of type $(A,R^K_{\mathrm{out}})$
with $A\in\{R_{\mathcal H},R^K_{\mathrm{in}},\Gamma_K\}$, it enters $V_{\mathcal H}\cup V_K\cup V_\Gamma$. Over
$(\iota^+)^\circ$, $A\ne R^K_{\mathrm{out}}$ as $\varpi\notin\partial W_{\mathrm{out}}$, the unstable manifold of
$\partial R_{\partial K^+,\mathrm{out}}$ over $\iota^+$ (II.B Lemma 3.3 (4)), so by the table $A = R^I_{\mathrm{in}}$,
and the curve enters $V_I$. Over $M^\circ$, it reaches $\{t^\flat_*<1\}$. (P1) at order $\mathsf s$ bounds
$\|Eu\|_{\mathsf s}$, and $u$ is controlled at order $\mathsf s$ on a neighbourhood $V_{K,\mathrm{out}}$ of $\partial
R_{\partial K^+,\mathrm{out}}$.

*Step 6: $\partial R_{\mathscr I^+,\mathrm{out}}$.* Proposition 3.6 with $t_{*,-} := \frac12$, the orders $(\mathsf
s,\mathsf s_0)$, constant near $\partial R_{\mathscr I^+,\mathrm{out}}$ (II.C Proposition 5.1 (5)), and (3.9) from (1.3).
Its $B$ is elliptic on $\partial R_{\mathscr I^+,\mathrm{out}}\cap\{t^\flat_*\ge\frac12\}$, which contains all of it over
$\Omega_*$. The part of $E$ from the cut-off $\psi_-$ has kernel in $\{t^\flat_*<1\}^2$, where $u = 0$ (the paragraph
after Proposition 3.6). The rest of $E$ is microsupported in a punctured neighbourhood of $\partial R_{\mathscr
I^+,\mathrm{out}}$. Let $\varpi$ be a point of it in $\partial\Sigma^+$. Over $(\mathscr I^+)^\circ$, its curve reaches
$\{t_* = 1\}$ backward (first row of the table). Over $\mathscr I^+\cap\iota^+$ it is of type
$(R^I_{\mathrm{in}},R^I_{\mathrm{out}})$, and over $(\iota^+)^\circ$ of type $(R^I_{\mathrm{in}},\cdot)$ or
$(R^K_{\mathrm{out}},R^I_{\mathrm{out}})$; it enters $V_I\cup V_{K,\mathrm{out}}$. Over $M^\circ$, it reaches
$\{t^\flat_*<1\}$. (P1) at order $\mathsf s$ bounds $\|Eu\|_{\mathsf s}$, and $u$ is controlled at order $\mathsf s$ on a
neighbourhood $V_{I,\mathrm{out}}$ of $\partial R_{\mathscr I^+,\mathrm{out}}\cap\{t^\flat_*\ge\frac12\}$.

*Conclusion.* Let $\varpi\in\partial\Sigma^+$ over $\mathrm{supp}\,\chi$. If $\varpi$ lies over $M^\circ$ or over
$\mathscr I^+$ at finite $t_*$, it is controlled at order $\mathsf s$ by Step 1 when $\varpi\notin\mathcal
V_{\mathrm{out}}$, with $t^\sharp>t^\flat_*(\varpi)$, and by Step 6 when $\varpi\in V_{I,\mathrm{out}}$, choosing
$\mathcal V_{\mathrm{out}}$ inside $V_{I,\mathrm{out}}$. If $\varpi$ lies over $K^+\cup\iota^+$, it lies in one of the
sets of Steps 2-6 or on a curve of the table, whose backward end $A$ is $\{t_* = 1\}$ or one of $R_{\mathcal H}$,
$R^I_{\mathrm{in}}$, $R^K_{\mathrm{in}}$, $\Gamma_K$, $R^K_{\mathrm{out}}$, each of which has a controlled neighbourhood.
This includes the curves inside the black hole, from $\partial R_{\mathcal H^+}$ to $\{r<r_0-\delta_0\}$ (II.B
Proposition 6.1), which reach $\mathrm{supp}\,\chi\subset\{r\ge r_1\}$; (P1) at order $\mathsf s$ applies. By compactness
of the cosphere bundle over $\mathrm{supp}\,\chi$, finitely many such $B$, with elliptic estimates off $\Sigma$, are
jointly elliptic there, and the elliptic estimate (II.A Lemma 8.4 (c)), with the a priori term $\|\chi
u\|_{-N}\le\|u\|_{\mathsf s_0}$, gives (1.4), in the strong sense since every step propagates regularity.

*Uniformity.* Each estimate used holds uniformly for $P$ with $\epsilon_P$ small (Propositions 3.1-3.6 and 4.2, II.A$'$
Theorems 3.1 and 5.4). The flow of $P$ agrees with that of $P_0$ over $\partial M$, and over $M^\circ$ it differs by
$O(\epsilon_P)$ in $C^1$ (II.C Lemma 4.1 (a)), so the finitely many backward segments used above, which enter open sets
in bounded times, have nearby segments for $P$ with the same properties. $d_0$ is the largest of those required by the
steps, at the orders $\mathsf s_0$, $\mathsf s$ and $\mathsf s+1$. With Remark 1.3 this proves Theorem 1.2. $\square$

## 6. What this part found

(D1) *The trapping estimate is proved in full.* The source quotes it from [Hin21] Theorem 3.9, whose proof writes out the
regularisation of its first step and sketches that of the others. Section 4 proves it in the present calculus with
coefficients of finite regularity, as the positive commutator form of the defect-measure proof of I.B section 6.4: one
regulariser, $\kappa = 2$, common to all steps; an induction on the order in half steps, so that every lower-order
remainder is bounded by the norm at the previous step; exact squares, by cut-offs built from functions $e^{-1/y}$; and
Lemmas 2.4-2.5, which compare norms through symbols. The dynamical input is II.C$'$ Proposition 3.4, made into defining
functions with the equations (4.1) by Lemma 4.1.

(D2) *[Hin26c] Proposition 7.9.* (a) Its time cut-offs $\psi_- = \eta(\mathfrak M(t_{*,-}-t_*))$ and $\psi_+ =
\eta(\mathfrak M(t_*-t_{*,+}))$ have their arguments reversed: with $\eta = 0$ on $(-\infty,-\frac12]$ and $\eta = 1$ on
$[0,\infty)$ they equal 1 before $t_{*,-}$ and after $t_{*,+}$. (b) Its statement (4), $\mathrm{WF}'(E)\cap\partial
R_{\mathscr I^+,\mathrm{out}} = \emptyset$, fails, as the term $e_-$ lies on $\partial R_{\mathscr I^+,\mathrm{out}}$
near $t_* = t_{*,-}$; Proposition 3.6 (4) restricts it to $\{t^\flat_*\le t_{*,-}-\frac14\}$. (c) For finite $t_{*,+}$
the proof needs $H_Gt_*\ge0$ on the support of the commutant, for the symbol $b_+$ to be real. The cut-off $\psi_\Sigma$
localises only to a neighbourhood of the characteristic set, and off it, at $x_I = 0$, $\mathsf Ht^\flat_* = t_*\hat\xi$
takes negative values, as $\hat\xi<0$ occurs there. Proposition 3.6 is stated for $t_{*,+} = \infty$ only. The case of
finite $t_{*,+}$ served in the source's Step 1, and section 5 does without it: finite times are controlled away from
$\partial R_{\mathscr I^+,\mathrm{out}}$, and Step 6 controls all of it at once.

(D3) *Two slips at $\mathscr I^+$.* In the proof of [Hin26c] Proposition 7.9 the equality $-4|\hat\eta|^2\hat\xi =
-4(2-\hat\xi)\hat\xi^2$ should read $-2(2-\hat\xi)\hat\xi^2$, as $|\hat\eta|^2 = \frac12\hat\xi(2-\hat\xi)$ on the
characteristic set. In (7.21) the middle expression $-2|\hat\eta|^2(\hat\xi-2)$ should read $-4|\hat\eta|^2(\hat\xi-2)$.
In both, the final inequality, $\le-q$ resp. $\ge q$, holds as printed (Propositions 3.5 and 3.6).

(D4) *[Hin26c] (7.22) at $n = 4$* (Lemma 3.4). The density $r^3|dt_*\,dr\,d\omega|$ and the constant $3 = n-1$ of II.C
Lemma 3.4 are exactly matched, as $r^2$ and $2$ are at $n = 3$, so the formula keeps its form. With a fibre inner product
varying near $\mathscr I^+$, the term $\frac12\mathsf G^{-1}\mathsf H\mathsf G$ appears; it vanishes at the radial sets,
where $\mathsf H = 0$.

(D5) *The horizon threshold* is I.A's $\vartheta_{\mathcal H}$ of (1.5), computed with the function $\rho$ of (H3) and
with $W' = 1$, $L = P$ near the horizon; no other weight enters there, $x_I$ and $\rho_+$ being smooth and positive
(Proposition 3.1).

(D6) *Characteristic cut-offs.* The source's cut-off $\psi_\Sigma$ is not needed at the horizon or at $\partial
R_{\partial K^+,\mathrm{in/out}}$, as the dynamical signs hold on a full neighbourhood (II.B Lemma 4.2 and (3.4)). It is
needed at $\mathscr I^+$, where it produces the term $JL$ of Lemma 2.1.

(D7) *Finite regularity at the trapped set.* $\phi^u\in C^{d_0-1}$ and $\phi^s\in C^{d_0-2}$ (II.C$'$ (C$'$2)), and the
coefficients of (4.1) lie in $C^{d_0-3}$ and $C^{d_0-4}$; the symbols of section 4 have this regularity, and $d_0$ is
chosen accordingly. The source's statement of cusp-regularity $C^{d_0-1,\ell_K}_{cu}$ for both is not used.

(D8) *Uniform constants.* The estimates are uniform for $P$ near $P_0$ and for the stationary models of nearby parameters
(Remark 1.3), as each constant depends only on finitely many coefficient norms and on the dynamical constants of II.B,
II.C and II.C$'$. The source's Remark 7.3, on large perturbations, is not proved.

## Sources

[Hin26c] P. Hintz, arXiv:2606.28008v1. READ: pp. 114-127 (section 7.1: (7.1)-(7.26), Propositions 7.1, 7.4 and 7.6-7.10,
Remarks 7.2-7.3 and 7.5, the proof of Proposition 7.1); p. 141 ((7.68), for the form of the trapping estimate).

[Hin21] P. Hintz, *Normally hyperbolic trapping on asymptotically stationary spacetimes*, Probab. Math. Phys. 2 (2021)
71-126, arXiv:1811.07843v1. READ: Theorem 3.9 and its proof. No statement of [Hin21] is used as an input; section 4
replaces it.

Part I.A: (1.5), Lemma 4.1. Part I.B: sections 1.5 ((H7)-(H8), (Γ.1)-(Γ.4)) and 6.4. Part II.A: sections 4.2, 6, 7, 8.3,
Lemma 8.4. Part II.A$'$: sections 2-5 (Proposition 2.4, Lemmas 2.3, 2.5, 4.1, 4.2, Theorems 3.1, 5.4). Part II.B:
sections 3-8 (Definitions 3.1, 4.1, 5.1, 7.1, Lemmas 3.2, 3.3, 4.2, 5.2, 7.2, Propositions 6.1, 8.1). Part II.C:
Definitions 1.1, 2.1, 2.4, 3.3, 3.5, 3.6, 5.2, Lemmas 1.4, 2.2, 2.5, 2.6, 3.2, 3.4, 3.7, 4.1, Propositions 4.2, 5.1. Part
II.C$'$: section 3 (Lemmas 3.1-3.3, Proposition 3.4).
