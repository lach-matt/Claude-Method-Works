# Part III.I$''''''$. Black hole parameters and centre-of-mass shift, n = 4 ([Hin26] section 11.6.1)

*Status.* Proved (D268: verifier 113 read the D266 repairs). Verified (D266: the hundred-and-twelfth verifier; no major
finding, three minor ones and eight nits seated, to be read). Written (D264). This part proves, at spatial dimension $n
= 4$, [Hin26] section 11.6.1 (pp. 252-256): for sources with a little more than $t_*^{-2}$-decay at $K^+$, a forward
solution with no boost term is a cut-off linearised Myers-Perry metric, a cut-off constant centre-of-mass shift, and a
remainder that decays at $K^+$ (Proposition 11.34).

*What n = 4 changes.* The scheme is the source's: the step at null infinity and at $\iota^+$, the zero energy inversion,
a sub-leading zero energy inversion after one order is gained at tf, the rest by the low-energy estimate, and one
integration in $t_*$. Three things differ. There is no logarithmic centre-of-mass term: the source's comes from the
exponent $(1,0)$ at $\iota^+$ (its Proposition 9.11 at $\lambda = 1$, where $a_{\mathrm s1}$ is a logarithm), while at
$n = 4$ the $\iota^+$-exponents begin at $\lambda_\sharp = \frac32+(1-e_\Upsilon)\gamma_\Upsilon$ and give centre-of-mass
motions $t_*^{-\lambda+1}$ that decay. At zero energy the source's Step 3.2 (its Proposition 9.30) is not needed (Part
III.I$'''''$ (I$'''''$3)); its Step 3.2's second half, the tf-improvement by its Proposition 9.35, is, at $n = 4$ by
III.G$''''$ Proposition 5.1. And that proposition's solution has a term $|\sigma|^{\alpha-3}h(S)$, singular at zf, which
the augmented operator's rows see; it is moved into the $\mathcal S_1$-column exactly (Lemma 1.4), which the source does
not discuss. Everything is at $b = b_0$. Notation: Parts I.A, II.E, II.G$'$, III.A, III.F$'$, III.F$'''$, III.G$''$,
III.G$''''$, III.H, III.H$'$ and III.I-III.I$'''''$; no instrument is used.

## 1. Setting and four lemmas

$L = L_{h,S}$, $\chi_K$, $\ell_I$ (III.I$'''''$ (1.2)), $\lambda_\sharp$ and (III.I$''''$ (2.4)) $2+\mathcal
E_{\mathrm{ind}}\subset\mathcal E_+$ are as in Part III.I$'''''$ section 1. On the spectral side, $\widehat{L_b}(\sigma)
= L_0-i\sigma L_1-\sigma^2L_2$ with $L_0 = \widehat{L_b}(0)$, $L_1 = [L_b,t_*]$, $L_2 = \frac12[[L_b,t_*],t_*]$
stationary (III.H section 1); near $\partial\bar X$, $L_1\in\rho\mathrm{Diff}^1_{\mathrm b}$ and $L_2\in C^\infty$
(Cartesian derivatives lie in $\rho\mathcal V_{\mathrm b}$, and $L_2$ is of order 0), as in III.I$'''$ Lemma 1.2.
$\tilde L_b(\sigma)$ is III.H Definition 3.1's augmented operator, with rows $r(u) := (\langle u,f^*_1\rangle,\langle
u,f^*_2\rangle)$, $f^*_j\in C^\infty_c(X^\circ)$ subject to III.H (3.1), and columns $\hat f_{\dot b}(\sigma) =
\widehat{L_b}(\sigma)\hat g^{\mathrm{aug}}(\sigma)(\dot b)$, $\hat f_S(\sigma) = \widehat{L_b}(\sigma)\hat
h^{\mathrm{aug}}(\sigma)(S)$ (III.H Lemma 2.5 (c)), where
$$\hat g^{\mathrm{aug}}(\sigma)(\dot b) = i\sigma^{-1}\Psi\dot g(\dot b),\qquad\hat h^{\mathrm{aug}}(\sigma)(S) =
\partial_\sigma(\sigma^{-1}\Psi)h(S)+i\sigma^{-1}\Psi\breve h(S)\tag{1.1}$$
(III.H (2.6)), $\Psi(\sigma,x) = \Phi(\sigma r)$ for $r\ge1$, $\Phi(0) = 1$ (III.H Lemma 2.5 (b)), and $\dot g(\dot b)$,
$h(S)$, $\breve h(S)$ the states of III.H section 1. $G_1(\sigma)(\dot b) := \Psi\dot g(\dot b) = -i\sigma\hat
g^{\mathrm{aug}}(\sigma)(\dot b)$ and $G_2(\sigma)(S) := (\Psi-\sigma\partial_\sigma\Psi)h(S)-i\sigma\Psi\breve h(S) =
-\sigma^2\hat h^{\mathrm{aug}}(\sigma)(S)$ are III.I$''$ (4.1)'s. The constant $c$ and the cut-off $\chi$ are fixed per
order $k$ as in III.I$''$ section 4, and memberships of the spectral pieces below hold at order $k$ for that $c$
(III.I$''$ section 4).

*Expansions at zf to first order.* For $\gamma\in(1,2)$,
$H^{k,(\beta_{\mathrm{scf}},\beta_{\mathrm{tf}},((0,0),\gamma))}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$ is the
space of $\chi_{\mathrm{zf}}v_0+\sigma\chi_{\mathrm{zf}}v_1+\tilde v$, $v_0\in H^{k,\beta_{\mathrm{tf}}}_{\mathrm
b}(X)$, $v_1\in H^{k,\beta_{\mathrm{tf}}-1}_{\mathrm b}(X)$, $\tilde v\in
H^{k,(\beta_{\mathrm{scf}},\beta_{\mathrm{tf}},\gamma)}_{\mathrm b}$: II.G$'$ section 3.1's space with the index set
$(0,0)$ at zf, written with $\sigma = \pm\rho_{\mathrm{tf}}\rho_{\mathrm{zf}}$ in place of powers of
$\rho_{\mathrm{zf}}$, $v_0$ and $v_1$ being the $\sigma$-Taylor coefficients of II.G$'$ Proposition 3.3 (1) ((2.25a)).

**Lemma 1.1 (first-order expansions).** Let $a\in(0,1)$ and $u_0\in H^{\infty,a}_{\mathrm b}(X)$.

(a) $(\widehat{L_b}(\sigma)-L_0)(\chi_{\mathrm{zf}}u_0) = -i\sigma\chi_{\mathrm{zf}}L_1u_0+R$, with $L_1u_0\in
H^{\infty,a+1}_{\mathrm b}(X)$ and $R\in H^{\infty,(\infty,a+2,\gamma)}_{\mathrm b}$ for every $\gamma<2$.

(b) For the source terms $f$ of III.H Lemma 2.2 ($f = f_{\dot b}$ or $f_S$), $\hat f(\sigma)-\chi_{\mathrm{zf}}\big(\hat
f(0)+\sigma\hat f'(0)\big)\in H^{\infty,(N,3-\epsilon,2-\epsilon)}_{\mathrm b}$ for all $N$, $\epsilon>0$, with $\hat
f'(0) := \partial_\sigma\hat f(0) = i\int t_*f\,dt_*\in H^{\infty,2-\epsilon}_{\mathrm b}(X)$.

*Proof.* (a) $(\widehat{L_b}(\sigma)-L_0)(\chi_{\mathrm{zf}}u_0) =
-i\sigma\chi_{\mathrm{zf}}L_1u_0-i\sigma[L_1,\chi_{\mathrm{zf}}]u_0-\sigma^2\chi_{\mathrm{zf}}L_2u_0$. By III.I$'''$
Lemma 1.1 (b) ($P = L_1$, $p = 1$), $\sigma[L_1,\chi_{\mathrm{zf}}]u_0\in H^{\infty,(\infty,a+2,\infty)}_{\mathrm b}$
(the factor $\sigma$ adds 1 at tf and zf); by its (a) ($P = L_2$, $p = 0$, $j = 2$),
$\sigma^2\chi_{\mathrm{zf}}L_2u_0\in H^{\infty,(\infty,a+2,\gamma)}_{\mathrm b}$, $\gamma<2$. (b) III.H Lemma 2.4 (a):
$\hat f = \hat f_c+\hat f_\infty$ with $\hat f_c$ entire in $\sigma$, supported in $\{r\le2\}$, where
$\chi_{\mathrm{zf}} = 1$ for $|\sigma|\le c$ (III.I$'''$ section 1), so its Taylor remainder is $O(\sigma^2)$ in
$C^\infty$: zf-weight $2-\epsilon$, no condition at tf or scf. And $\hat f_\infty = r^{-3}G(\sigma r,x)$ on $\{r\ge1\}$
with $G$ entire and $|(\zeta\partial_\zeta)^j(r\partial_r)^a\partial^\beta_\omega G|\le C\langle\zeta\rangle^{-N}$; with
$\hat r = |\sigma|r$, $r^{-3}(G(\sigma r)-\chi_1(\hat r)(G(0)+\sigma rG'(0)))$ is $r^{-3}$ times a function of $(\sigma
r,x)$ that is $O(\hat r^2)$ for $\hat r\le\frac18$ and $O(\langle\hat r\rangle^{-N}+\hat r\,1_{\hat r\le\frac14})$
beyond, with the same derivative bounds. In III.I$'''$ Lemma 1.2 (b)'s Fubini count ($\rho_{\mathrm{zf}}\sim\hat r$ and
$\rho_{\mathrm{tf}}\sim r^{-1}$ near zf, $\rho_{\mathrm{scf}}\sim\hat r^{-1}$ near scf) this gives the weights
$(N,3-\epsilon,2-\epsilon)$; there the $O(\hat r)$ remainder gave $1-\epsilon$. $\hat f'(0) = \partial_\sigma\hat
f_c(0)+r^{-2}\partial_\zeta G(0,x)$ is smooth and in $\mathcal A^2\subset H^{\infty,2-\epsilon}_{\mathrm b}$ near
$\partial X$. $\square$

**Lemma 1.2 (conormal sections are admissible).** Let $\sigma\in\mathbb R\setminus0$ be small and $v$ smooth on
$X^\circ$ and b-conormal at $\partial X$ of $\mu_{\mathrm b}$-weight $a$. Then $v$ lies in the space $\mathcal
X'_\sigma$ built as $\mathcal X_\sigma$ but with an admissible order family (I.A section 7) lowered near
$R_{\mathrm{out}}$, the zero section over $\partial X$ (I.A (4.6)), and unchanged near $R_{\mathrm{in}}$; $\mathcal
X'_\sigma\supset\mathcal X_\sigma$, $\mathcal Y'_\sigma\supset\mathcal Y_\sigma$, and on $\mathcal Y_\sigma$ the
inverses of $\widehat{L_b}(\sigma)$, and of $\tilde L_b(\sigma)$, on the two spaces agree.

*Proof.* Every part of $\widehat{L_b}(\sigma)$ maps $\mathcal A^a$ to $\mathcal A^{a+1}$ (I.A Theorem 7.2 (5)'s proof),
so $\widehat{L_b}(\sigma)v\in\mathcal A^{a+1}$. $R_{\mathrm{out}}$ lies in the characteristic set, and the admissibility
conditions there ask the order to be constant near $R_{\mathrm{out}}$ and below a threshold ((O2)-(O3) of I.A section
7); so $\mathsf r' := \mathsf r-\varphi$, with $\varphi\ge0$ constant near $R_{\mathrm{out}}$, zero near
$R_{\mathrm{in}}$ and nondecreasing along the flow (I.A Lemma 7.1's construction with a smaller value at
$R_{\mathrm{out}}$), is admissible, and $\varphi$ can be taken with $\mathsf r'+\alpha_+<a-2$ near $R_{\mathrm{out}}$.
By I.A Lemma 7.4 (a), $v\in\bar H^{s,\mathsf r'+\alpha_+}$ and $\widehat{L_b}(\sigma)v\in\mathcal A^{a+1}\subset\bar
H^{s-1,\mathsf r'+\alpha_++1}$ for every $s$, so $v\in\mathcal X'_\sigma$; the inclusions hold as $\mathsf r'\le\mathsf
r$. $\widehat{L_b}(\sigma)$ is Fredholm of index 0 on both spaces (III.H, (H1)-(H5) at $\sigma\ne0$), and its kernel
does not depend on the admissible order: by I.A Theorem 7.2 (5) and its proof a kernel element lies in
$\bigcap_\epsilon\mathcal A^{\frac32+\bar S-\epsilon}$, and such sections lie in every admissible space. So it is
injective on $\mathcal X'_\sigma$ as on $\mathcal X_\sigma$ (III.F$''$), hence invertible on both, and the inverses
agree on $\mathcal Y_\sigma$. $\tilde L_b(\sigma)$ is a finite-rank augmentation of it with as many rows as columns, so
Fredholm of index 0 on both spaces; if $(u,\dot b,S)$ lies in its kernel on the larger one, then
$\widehat{L_b}(\sigma)\big(u+\hat g^{\mathrm{aug}}(\sigma)(\dot b)+\hat h^{\mathrm{aug}}(\sigma)(S)\big) = 0$, so $u =
-\hat g^{\mathrm{aug}}(\sigma)(\dot b)-\hat h^{\mathrm{aug}}(\sigma)(S)\in\mathcal X_\sigma$ (III.H Lemma 2.5 (b)), and
$(u,\dot b,S)$ lies in the kernel on $\mathcal X_\sigma$, which is trivial for $|\sigma|$ small (III.H Theorem 4.1). So
$\tilde L_b(\sigma)$ is invertible on both, and the inverses agree. $\square$

**Lemma 1.3 (row data).** For $e = (e_1,e_2)\in\mathfrak b_{\mathbb C}\oplus\mathcal S_{1,\mathbb C}$ put $w_e :=
\chi_{\mathrm{zf}}(\dot g(e_1)+h(e_2))$. Then $r(w_e) = e$, and for $0<|\sigma|\le c$
$$\tilde L_b(\sigma)^{-1}(0,e) = (w_e,0,0)-\tilde L_b(\sigma)^{-1}\big(\widehat{L_b}(\sigma)w_e,0,0\big),$$
whose $\mathfrak b$- and $\mathcal S_1$-components are $O(|\sigma|^{1-\epsilon})$ and whose first component lies in
$H^{\infty,(\frac32-\epsilon,1-\epsilon,0)}_{\mathrm b}$ uniformly in $|e|\le1$, for every $\epsilon>0$.

*Proof.* $\chi_{\mathrm{zf}} = 1$ on $\mathrm{supp}\,f^*_j$ for $|\sigma|\le c$ (III.I$'''$ section 1), so $r(w_e) = e$
by III.H (3.1); $w_e$ has compact support for $\sigma\ne0$, so it lies in $\mathcal X_\sigma$ and $\tilde
L_b(\sigma)(w_e,0,0) = (\widehat{L_b}(\sigma)w_e,e)$, which is the identity. $\dot g(e_1)+h(e_2)\in\mathcal A^2\subset
H^{\infty,2-\epsilon}_{\mathrm b}(X)$ lies in the kernel of $L_0$, so $\widehat{L_b}(\sigma)w_e =
[L_0,\chi_{\mathrm{zf}}](\cdot)+(\widehat{L_b}(\sigma)-L_0)(\chi_{\mathrm{zf}}\,\cdot)\in
H^{\infty,(\infty,4-\epsilon,\gamma)}_{\mathrm b}$, $\gamma<1$ (III.I$'''$ Lemmas 1.1 (a)-(b) with $a = 2-\epsilon$).
III.I$''$ Lemma 4.2 with $\beta_{\mathrm{scf}} := \frac32-\epsilon$, $\beta_{\mathrm{zf}} := 1-2\epsilon$,
$\beta_{\mathrm{tf}} := 1-\epsilon$ ($\alpha+2 = \epsilon\in(0,1)$) gives the claim; $w_e$ itself has zf-weight 0 and
tf-weight $2-\epsilon$. $\square$

At $\sigma = 0$ the identity reads $\tilde L_b(0)^{-1}(0,e) = (\dot g(e_1)+h(e_2),0,0)$: row data are answered by the
nullspace, with no column.

**Lemma 1.4 (the boost-type term of III.G$''''$ Proposition 5.1).** Let $\alpha\in(1,2)$ and $S'\in
H^{\infty,0}_{\mathrm b}(\pm[0,1)_\sigma,|\frac{d\sigma}\sigma|;\mathcal S_1)$, and put $\Sigma(\sigma) :=
-\sigma^2|\sigma|^{\alpha-3}S'(\sigma)$. Then on $\{r\le R\}$, for each $R$,
$$\chi_{\mathrm{zf}}h^{\le3}_{b_0,\mathrm s1}\big(\sigma,|\sigma|^{\alpha-3}S'(\sigma)\big)-\hat
h^{\mathrm{aug}}(\sigma)(\Sigma(\sigma)) = O(|\sigma|^{\alpha-2})\quad\text{in }C^\infty,\tag{1.2}$$
and near zf the difference has zf-weight $\alpha-2$; $\hat h^{\mathrm{aug}}(\sigma)(\Sigma(\sigma))$ has tf-weight
$\alpha-\epsilon$ for every $\epsilon>0$ (b-Sobolev; III.I$''$ Lemma 4.3 with $a = \alpha-3$) and is rapidly decaying at
scf.

*Proof.* By (1.1), $\hat h^{\mathrm{aug}}(\sigma)(\Sigma) = |\sigma|^{\alpha-3}\big(\Psi h(S')-\sigma\partial_\sigma\Psi
h(S')-i\sigma\Psi\breve h(S')\big)$, and $h^{\le3}_{b_0,\mathrm s1}(\sigma,S) = h(S)-i\sigma\breve h^{\le3}_{b_0,\mathrm
s1}(\sigma,S)$ (III.G$''''$ Proposition 5.1). The difference is $|\sigma|^{\alpha-3}(1-\Psi)h(S')$ plus
$\sigma|\sigma|^{\alpha-3}$ times bounded terms; near zf$\cap$tf the term
$\sigma|\sigma|^{\alpha-3}\chi_{\mathrm{zf}}\breve h^{\le3}_{b_0,\mathrm s1}(\sigma,S')$ is controlled by III.G$''''$
Lemma 4.3 ($\breve h^{\le3}_{b_0,\mathrm s1}$ polyhomogeneous at tf with index set $(0,0)\cup\mathcal
E_{\mathrm{ind}}$), which gives it zf- and tf-weight $\alpha-2$. On $\{r\le R\}$, $|\Psi-1|\le C|\sigma|$ and
$|\partial_\sigma\Psi|\le C$ (III.H Lemma 2.5 (d)), with derivatives; for $r\ge1$, $1-\Psi = 1-\Phi(\sigma r) =
O(|\sigma|r)$ and $h(S')\in\mathcal A^3$, so $|\sigma|^{\alpha-3}(1-\Psi)h(S')$ is $|\sigma|^{\alpha-2}$ times
$O(r^{-2})$ near zf. At tf ($\sigma r\sim1$), $|\sigma|^{\alpha-3}\Phi(\sigma r)r^{-3}\sim|\sigma|^\alpha$ (tf-weight
$\alpha-\epsilon$ in $H_{\mathrm b}$); at scf $\Phi$ decays rapidly. $\square$

## 2. Extraction of the parameters ([Hin26] Proposition 11.34 at n = 4)

**Proposition 2.1 ([Hin26] Proposition 11.34 at n = 4, at $b_0$).** Let
$\alpha_K\in(2,\min(a_K,2+\epsilon_{\mathrm{ind}},\frac52))$, $\epsilon_{\mathrm{ind}}$ that of III.G$''''$ Proposition
5.1, and let $f\in\bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),4-\epsilon,\alpha_K}_{\mathrm
b}(\Omega_*;S^2T^*)^{\bullet,-}$ be real, with $\dot S(f) = 0$ (III.I$''''$ Proposition 4.1 (1)). Then the forward
solution of $Lu = f$ is
$$u = \chi_K\dot g(\dot b)+\chi_Kh(\dot S^{(0)}_1)+\tilde u,\qquad\dot b\in\mathfrak b,\ \dot S^{(0)}_1\in\mathcal
S_1,\quad\tilde u\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta_+,\alpha_K-2}_{\mathrm
b}(\Omega_*)^{\bullet,-}\tag{2.1}$$
for every $\beta_+<\min(\frac32,\min\mathrm{Re}\,\mathcal E_+)$, with $\dot b$, $\dot S^{(0)}_1$ and $\tilde u$
depending continuously on $f$. $\tilde u$ decays at $K^+$, as $\alpha_K-2>0$.

The source's (11.117) has a third term $\chi_Kh^{\le4}_{b,\mathrm s1}(\dot S^{(0,1)}_1\log t_*)$, the logarithmic
centre-of-mass motion, $\iota^+$-weight $1-\epsilon$, and $\alpha_K\in(2,2+\epsilon_K)$ with
$\epsilon_K<\epsilon_{\mathrm{ind}}$; the cap $\frac52$ here is used only in Steps 1-2, through $c_K<\lambda_\sharp+1$.
Its (11.116) also has a second class $f_2$ with $\iota^+$-index set $\tilde{\mathcal E}_++2$; at $n = 4$ the terms of
that kind have $\iota^+$-order 4, so one class suffices, as in Part III.I$'''''$.

*Proof.* *Step 0 (the source's start).* III.I$'''''$ Proposition 2.1 (with any $\alpha_+\in(\alpha'_K,2)$; $f$ has
$\iota^+$-weight $4-\epsilon$) gives $u\in H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\beta'_+,\alpha'_K-2}_{\mathrm b}$ for every $\alpha'_K<2$ and
$\beta'_+<\min(\frac32,\min\mathrm{Re}\,\mathcal E_+)$. Fix $\alpha'_K\in(\max(1,\alpha_K+2-a_K),2)$, possible as
$\alpha_K<a_K$, and $\beta'_+\in(1,\min(\frac32,\min\mathrm{Re}\,\mathcal E_+))$. III.I Proposition 4.1 (4.2) gives
$(L-L_b)u$ the $\iota^+$-weight $\beta'_++2+m_+-\epsilon\ge4-\epsilon$ ($\beta'_++m_+>2$) and the $K^+$-weight
$\alpha'_K-2+a_K>\alpha_K$, so
$$L_bu = f' := f-(L-L_b)u\in\bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal
E^C_I+1\rangle',\ell_I+1),4-\epsilon,\alpha_K}_{\mathrm b}(\Omega_*)^{\bullet,-}.$$

*Steps 1-2 (null infinity and $\iota^+$; the source's (11.118)-(11.120)).* III.I$'''''$ Proposition 2.1's Steps 1-2 with
$\alpha^\sharp_+ := 2-\epsilon$ ($\epsilon$ small, $2-\epsilon$ off III.I$'''''$ (2.3)'s excluded set, which is finite
below 2), $K^+$-weight $\alpha_K$ in place of $\tilde\alpha_K$, and $c_K\in(\alpha_K,\lambda_\sharp+1)$ (nonempty, as
$\alpha_K<\frac52<\lambda_\sharp+1$) off the finitely many excluded values, so that $\ell_K(\lambda_0) =
c_K-\mathrm{Re}\,\lambda_0\in(c_K-2,1)$ (there $\epsilon_{\mathrm{ind}}$ is $\min\mathrm{Re}\,\mathcal
E^\iota_{\mathrm{ind}}$, not III.G$''''$'s): the errors of III.G$''$ Corollary 4.3 have $K^+$-weight
$c_K-\epsilon>\alpha_K$, so the source keeps $K^+$-weight $\alpha_K$, and each $u_{\lambda_0}$ has $K^+$-weight
$\min(\mathrm{Re}\,\lambda_0-1,\ell_K(\lambda_0))-\epsilon\ge c'_K := \min(\lambda_\sharp-1,c_K-2)-\epsilon>\alpha_K-2$
for $\epsilon<\min(c_K-\alpha_K,\lambda_\sharp+1-\alpha_K)$. This gives $u_I$, $u_\iota\in H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\lambda_\sharp-\epsilon,c'_K}_{\mathrm b}(\Omega_*)^{\bullet,-}$ ($u_I$ supported near $\mathscr
I^+$) and
$$u^\flat := u-u_I-u_\iota:\qquad L_bu^\flat =
f^\flat\in H^{\infty,\ell_I+1,4-\epsilon,\alpha_K}_{\mathrm b}(\Omega_*)^{\bullet,-},\tag{2.2}$$
$u^\flat$ the forward solution (II.E Proposition 3.4). From here on $\epsilon>0$ is fixed, small as above; the
parameters $\dot b$, $\dot S^{(0)}_1$ found below are the $(0,0)$-coefficient of $u$ at $K^+$ (its limit as
$t_*\to\infty$ in compact spatial sets, as $\tilde u$ tends to 0 there), so they and $\tilde u$ do not depend on
$\epsilon$, and (2.1) holds for every $\beta_+$. There is no logarithmic term: the least $\iota^+$-exponent is
$\lambda_\sharp$, and III.G$''$ (4.2)'s $a_{\mathrm s1} = \frac1{\lambda_0(\lambda_0-1)}t_*^{-\lambda_0+1}$ is a power
for $\mathrm{Re}\,\lambda_0>1$ ((I$''''''$1)).

*Step 3 (the decomposition).* As in III.I$''$ section 4, $u^\flat = u_{\mathrm{hi}}+u_{\mathrm{reg}}+u_{\mathrm{sing}}$,
with $(\hat u_1,\hat b_1,\hat S_1) := \tilde L_b(\sigma)^{-1}(\hat f^\flat(\sigma),0,0)$, $\mathcal Fu_{\mathrm{reg}} =
\chi(|\sigma|)\hat u_1$, and $\mathcal F(\partial_{t_*}u_{\mathrm{sing}}) = \chi(|\sigma|)\big(G_1(\sigma)(\hat
b_1)+i\sigma^{-1}G_2(\sigma)(\hat S_1)\big)$ for $\sigma\ne0$ (III.I$''$ (4.1);
$\partial^2_{t_*}\leftrightarrow-\sigma^2$). III.I$''$ Lemma 4.1 ($\beta^f_I = \ell_I$, $\beta_\iota = 2-\epsilon$,
$\beta_K = \alpha_K\in(2,3)$; $\ell_I+1\ge4-\epsilon-(1-\epsilon_1)$ as $\ell_I\ge2$, $\epsilon_1\le\epsilon$) gives
$u_{\mathrm{hi}}\in H^{\infty,(\frac32-\epsilon,N,N)}_{\mathrm b}(M')$. (2.25a) ($\beta_K = \alpha_K\in(2,3)$) gives
$$\hat f^\flat|_{\pm(0,c]}\in H^{\infty,(3-2\epsilon,3-\epsilon,((0,0),\alpha_K-1))}_{\mathrm b},\qquad\hat f^\flat =
\chi_{\mathrm{zf}}\hat f^\flat(0)+\sigma\chi_{\mathrm{zf}}\hat f^\flat_1+\cdots,\tag{2.3}$$
$\hat f^\flat(0) = \int f^\flat\,dt_*\in H^{\infty,3-\epsilon}_{\mathrm b}(X)$, $\hat f^\flat_1 = i\int
t_*f^\flat\,dt_*\in H^{\infty,2-\epsilon}_{\mathrm b}(X)$, the same for both signs.

*Step 3.1 (zero energy; the source's (11.123)).* III.H Proposition 3.2 at the weight $\alpha+2 = 1-\epsilon$ ($\mathcal
Y_0$ is the $\mu_{\mathrm b}$-weight $3-\epsilon$, III.I$'''$ Step 3.1) gives $(\hat u_0,\dot b_0,S_0) := \tilde
L_b(0)^{-1}(\hat f^\flat(0),0,0)$, $\hat u_0\in H^{\infty,1-\epsilon}_{\mathrm b}(X)$. $S_0 = 0$: $f^\flat$ lies in the
space of III.I$'''''$ Proposition 2.1's Step 3 for every $\tilde\alpha_K<2$ and $\alpha^\sharp_+<2-\epsilon$, and III.H
Proposition 3.2's inverses at the weights $1-\epsilon$ and $\alpha^\sharp_+-1\le1-\epsilon$ agree on $\hat f^\flat(0)$
(nested spaces, both invertible). So that Step gives $u^\flat-\chi^H_Kt_*h(S_0)$ of $K^+$-weight $\tilde\alpha_K-2>-1$,
and $u$, $u_I$, $u_\iota$ have $K^+$-weight $>-1$. So $h(S_0) = 0$ and $S_0 = 0$ (III.F$'''$ Proposition 4.1 (1)). As in
III.I$'''$ (2.5), $\tilde L_b(\sigma)(\chi_{\mathrm{zf}}\hat u_0,\dot b_0,0) = (\hat f^\flat(\sigma)-\hat
f_2(\sigma),0,0)$ with
$$\hat f_2 := \big(\hat f^\flat-\chi_{\mathrm{zf}}\hat f^\flat(0)\big)-[L_0,\chi_{\mathrm{zf}}]\hat
u_0-(\widehat{L_b}(\sigma)-L_0)(\chi_{\mathrm{zf}}\hat u_0)-\big(\hat f_{\dot b_0}(\sigma)-\chi_{\mathrm{zf}}\hat
f_{\dot b_0}(0)\big).$$
By (2.3), III.I$'''$ Lemma 1.1 (b) ($[L_0,\chi_{\mathrm{zf}}]\hat u_0\in H^{\infty,(\infty,3-\epsilon,\infty)}_{\mathrm
b}$) and Lemma 1.1 (a)-(b),
$$\hat f_2 = \sigma\chi_{\mathrm{zf}}F_1+R_2,\qquad F_1 := \hat f^\flat_1+iL_1\hat u_0-\hat f'_{\dot b_0}(0)\in
H^{\infty,2-\epsilon}_{\mathrm b}(X),\quad R_2\in H^{\infty,(\frac52-\epsilon,3-\epsilon,\alpha_K-1)}_{\mathrm
b},\tag{2.4}$$
$F_1$ the same for both signs (the remainder zf-weights $\alpha_K-1$, $\gamma<2$ and $2-\epsilon$ are at least
$\alpha_K-1$, as $\alpha_K<3-\epsilon$).

*Step 3.2 (one order at tf; the source's (11.124)-(11.126)).* Put $\tilde g := \sigma^{-1}\hat f_2$; as $|\sigma| =
\rho_{\mathrm{tf}}\rho_{\mathrm{zf}}$, $\tilde g\in H^{\infty,(\frac52-\epsilon,2-\epsilon,((0,0),\alpha_K-2))}_{\mathrm
b}$ with zf-coefficient $F_1$. Its tf-weight $2-\epsilon$ is too low for III.H Proposition 3.2 at the next order (it
would need $\alpha+2 = -\epsilon$). III.G$''''$ Proposition 5.1 on $X^\pm_{\mathrm{sc}\text-\mathrm b}$ separately, with
$\alpha := 2-\epsilon$, $\ell_{\mathrm{scf}} := \frac32-\epsilon$, $\ell_{\mathrm{zf}} := \alpha_K-2\notin\mathbb N_0$,
$k_0 := 0$ and $w = \alpha_K-2+\epsilon\in(-\epsilon_{\mathrm{ind}},\ell^{\max}_K)$ ($\epsilon$ chosen with $w$ and
every $\epsilon+j$, $j\in\mathbb N_0$, off the set of the $-\mu$, which is real and discrete, III.G$''''$), gives $\hat
u_3^\pm = \chi_{\mathrm{zf}}u_b+\chi^\sharp_{\mathrm{tf}}\tilde u$ in
$H^{\infty,(\frac32-2\epsilon,-\epsilon,-1-\epsilon)}_{\mathrm b}$ with
$$\hat f_4 := \tilde g-\widehat{L_b}(\sigma)\hat u_3\in
H^{\infty,(\frac52-\epsilon,2+\epsilon_{\mathrm{ind}}-2\epsilon,((0,0),\alpha_K-2))}_{\mathrm b},\tag{2.5}$$
with zf-coefficients $F_4^\pm\in H^{\infty,2+\epsilon_{\mathrm{ind}}-2\epsilon}_{\mathrm b}(X)$, possibly different for
the two signs. In $u_b$ (III.G$''''$ (5.2)) the term $h^{\le3}_{b_0,\mathrm s1}(\sigma,|\sigma|^{\alpha-3}S'(\sigma))$,
$S' := S^{(-1)}_1$, is the only one of zf-weight below $\alpha-2$; the others carry $|\sigma|^{\alpha-2}$ or
$|\sigma|^{\alpha-2-\mu}$, $\mu\le0$. With $\Sigma_3 := -\sigma^2|\sigma|^{\alpha-3}S'$ of Lemma 1.4 put
$$\hat u'_3 := \hat u_3-\hat h^{\mathrm{aug}}(\sigma)(\Sigma_3):\qquad\widehat{L_b}(\sigma)\hat u'_3+\hat
f_{\Sigma_3}(\sigma) = \widehat{L_b}(\sigma)\hat u_3\tag{2.6}$$
(III.H Lemma 2.5 (c)). By Lemma 1.4, $\hat u'_3\in H^{\infty,(\frac32-2\epsilon,-\epsilon,-\epsilon)}_{\mathrm b}$ near
zf and tf ($\chi^\sharp_{\mathrm{tf}}$ vanishes near zf, Lemma 1.4's difference has zf-weight $\alpha-2$), and $r(\hat
u'_3) = O(|\sigma|^{-\epsilon})$ (on $\mathrm{supp}\,f^*_j$, (1.2) and $|\sigma|^{\alpha-2}$ for the other terms of
$u_b$). $\Sigma_3 = O(|\sigma|^{1-\epsilon})$.

*Step 3.3 (the sub-leading zero energy piece; the source's Step 4).* III.H Proposition 3.2 at the weight $\alpha+2 =
\epsilon_{\mathrm{ind}}-2\epsilon\in(0,1)$ ($\epsilon<\frac12\epsilon_{\mathrm{ind}}$) gives $(\hat u_4,\hat b_4,\hat
S_4)^\pm := \tilde L_b(0)^{-1}(F_4^\pm,0,0)$, $\hat u_4\in H^{\infty,\epsilon_{\mathrm{ind}}-2\epsilon}_{\mathrm b}(X)$.
As in Step 3.1 (with III.I$'''$ Lemma 1.1, Lemma 1.2 (a) and (b) there, for the zf-weight $\gamma<1$ and the columns
$(N,3-\epsilon,1-\epsilon)$),
$$\hat f_5 := \hat f_4-\widehat{L_b}(\sigma)(\chi_{\mathrm{zf}}\hat u_4)-\hat f_{\hat b_4}(\sigma)-\hat f_{\hat
S_4}(\sigma)\in H^{\infty,(\frac52-\epsilon,2+\epsilon_{\mathrm{ind}}-2\epsilon,\alpha_K-2)}_{\mathrm b},\tag{2.7}$$
the zf-coefficient cancelling by the choice of $(\hat u_4,\hat b_4,\hat S_4)$, and $r(\chi_{\mathrm{zf}}\hat u_4) =
r(\hat u_4) = 0$.

*Step 3.4 (the rest; the source's Step 5).* III.I$''$ Lemma 4.2 with $\beta_{\mathrm{scf}} := \frac32-2\epsilon$,
$\beta_{\mathrm{tf}} := \epsilon_{\mathrm{ind}}-2\epsilon$, $\beta_{\mathrm{zf}} := \alpha_K-2$, $\alpha+2 :=
\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}}\in(0,1)$ ($\alpha_K-2<\epsilon_{\mathrm{ind}}-2\epsilon$ for $\epsilon$ small)
gives $(\hat u_5,\hat b_5,\hat S_5) := \tilde L_b(\sigma)^{-1}(\hat f_5,0,0)$ with $\hat u_5\in
H^{\infty,(\frac32-3\epsilon,\epsilon_{\mathrm{ind}}-2\epsilon,\alpha_K-2)}_{\mathrm b}$ and $\hat b_5,\hat S_5\in
H^{\infty,\alpha_K-2}_{\mathrm b}(\pm(0,c],|\frac{d\sigma}\sigma|)$.

*Step 3.5 (assembly).* For $0<\pm\sigma\le c$ let $(U_r,B_r,\Sigma_r) := \tilde L_b(\sigma)^{-1}(0,\sigma r(\hat
u'_3))$. Then
$$(\hat u_1,\hat b_1,\hat S_1) = (\chi_{\mathrm{zf}}\hat u_0,\dot b_0,0)+\sigma\Big[(\hat
u'_3,0,\Sigma_3)+(\chi_{\mathrm{zf}}\hat u_4,\hat b_4,\hat S_4)+(\hat u_5,\hat b_5,\hat
S_5)\Big]-(U_r,B_r,\Sigma_r).\tag{2.8}$$
Indeed, apply $\tilde L_b(\sigma)$ to the right side. The first components add up, by the definitions of $\hat f_2$,
$\tilde g$, $\hat f_4$, $\hat f_5$, (2.6) and the first component of $\tilde L_b(\sigma)(\hat u_5,\hat b_5,\hat S_5) =
(\hat f_5,0,0)$, to $(\hat f^\flat-\hat f_2)+(\hat f_2-\sigma\hat f_4)+\sigma(\hat f_4-\hat f_5)+\sigma\hat f_5 = \hat
f^\flat$; the rows are $0+\sigma(r(\hat u'_3)+0+0)-\sigma r(\hat u'_3) = 0$. Every first component lies in the space
$\mathcal X'_\sigma$ of Lemma 1.2 (which contains $\mathcal X_\sigma$): $\chi_{\mathrm{zf}}\hat u_0$,
$\chi_{\mathrm{zf}}\hat u_4$ and $\chi_{\mathrm{zf}}u_b$ have compact support for $\sigma\ne0$; $\hat h^{\mathrm{aug}}$
by III.H Lemma 2.5 (b); $\hat u_5$ and $U_r$ by construction; and $\chi^\sharp_{\mathrm{tf}}\tilde u$ by Lemma 1.2,
being b-conormal of weight $\frac32-2\epsilon$ at $\partial X$. So (2.8) follows from the injectivity of $\tilde
L_b(\sigma)$ (Lemma 1.2). By Lemma 1.3, $B_r,\Sigma_r = O(|\sigma|^{1-\epsilon})\cdot O(|\sigma|^{1-\epsilon}) =
O(|\sigma|^{2-2\epsilon})$ and $U_r\in H^{\infty,(\frac32-\epsilon,2-2\epsilon,1-2\epsilon)}_{\mathrm b}$ (with $\sigma
r(\hat u'_3) = O(|\sigma|^{1-\epsilon})$ and $\sigma\partial_\sigma$-regular).

Consequently, with all weights for $\epsilon$ small:
$$\hat u_1\in H^{\infty,(\frac32-3\epsilon,1-2\epsilon,((0,0),\alpha_K-2))}_{\mathrm b},\ \text{zf-coefficient }\hat
u_0;\quad\hat b_1-\dot b_0,\ \sigma^{-1}\hat S_1-\hat S_4^\pm\in H^{\infty,\alpha_K-2}_{\mathrm
b}(\pm(0,c],|\tfrac{d\sigma}\sigma|),\tag{2.9}$$
since $\sigma\hat u'_3$, $\sigma\chi_{\mathrm{zf}}\hat u_4$, $\sigma\hat u_5$ and $U_r$ have zf-weight at least
$1-2\epsilon>\alpha_K-2$ and tf-weight at least $1-2\epsilon$, $\sigma(\hat b_4+\hat b_5)-B_r = O(|\sigma|)$, and
$\sigma^{-1}\hat S_1-\hat S_4 = \Sigma_3+\hat S_5-\sigma^{-1}\Sigma_r = O(|\sigma|^{\alpha_K-2})$ with
$\sigma\partial_\sigma$-regularity.

*Step 4 (the regular part).* By (2.26a) (II.G$'$ Proposition 3.5 (1)) with $\beta_K := \alpha_K-1\in(1,2)$, the one
Taylor coefficient (order $0<\alpha_K-2$) being $\hat u_0$ for both signs, $u_{\mathrm{reg}}\in
H^{\infty,(\frac32-4\epsilon,2-2\epsilon,\alpha_K-1)}_{\mathrm b}(M')$.

*Step 5 (the singular part; the source's (11.130)-(11.133)).* By (2.9), III.I$'''$ Lemma 1.3 (for $G_1(\sigma)(\dot
b_0)$, $G_2(\sigma)(\hat S_4^\pm)$) and III.I$''$ Lemma 4.3 with $a = \alpha_K-2$ (for $G_1(\sigma)(\hat b_1-\dot b_0)$
and $G_2(\sigma)(\sigma^{-1}\hat S_1-\hat S_4)$),
$$\mathcal F(\partial_{t_*}u_{\mathrm{sing}}) = \chi\big(G_1(\sigma)(\hat b_1)+iG_2(\sigma)(\sigma^{-1}\hat S_1)\big)\in
H^{\infty,(N,2-\epsilon,((0,0),\alpha_K-2))}_{\mathrm b},\tag{2.10}$$
with zf-coefficients $\dot g(\dot b_0)+h(i\hat S_4^\pm)$. The distribution $\mathcal F(\partial_{t_*}u_{\mathrm{sing}})$
is bounded near $\sigma = 0$, and its difference from the right side of (2.10), a bounded function with compact support,
is supported at $\{0\}$; so the inverse transform of the difference is a polynomial in $t_*$, which the decay of both as
$t_*\to-\infty$ ($\partial_{t_*}u_{\mathrm{sing}} = -\partial_{t_*}(u_{\mathrm{hi}}+u_{\mathrm{reg}})$ for $t_*<1$,
below; the other by the Riemann-Lebesgue lemma) forces to vanish, and (2.10) holds as distributions. *Matching.* If the
two differed, $\mathcal F(\partial_{t_*}u_{\mathrm{sing}})$ would be $c\,1_{\sigma>0}\chi(|\sigma|)$, $c\ne0$ a section
of $X$, plus a function to which (2.26a) applies; the inverse transform of the first is $c\cdot(2\pi
i)^{-1}t_*^{-1}(1+o(1))$ as $t_*\to-\infty$, of $K^-$-weight below 1 in spatially compact sets, while that of the second
has $K^-$-weight $\alpha_K-1>1$. But $\partial_{t_*}u_{\mathrm{sing}} =
-\partial_{t_*}(u_{\mathrm{hi}}+u_{\mathrm{reg}})$ for $t_*<1$ ($u^\flat = 0$ there), of $K^-$-weight $\alpha_K>1$ (Step
4, $\partial_{t_*}\in\rho_\iota\rho_K\mathcal V_{\mathrm b}$). So $\hat S_4^+ = \hat S_4^-$ ($h$ injective), and we drop
the sign. Now (2.26a) with $\beta_K := \alpha_K-1$ gives $\partial_{t_*}u_{\mathrm{sing}}\in
H^{\infty,(3-2\epsilon,3-\epsilon,\alpha_K-1)}_{\mathrm b}(M')$, and III.I$''$ Lemma 2.1 (1) with $\mathcal E_K =
\emptyset$, $\beta_K := \alpha_K-2\ne0$, the a priori bound on $\Omega_-$ being that of
$u_{\mathrm{hi}}+u_{\mathrm{reg}}$, gives
$$u_{\mathrm{sing}}\in H^{\infty,\frac32-4\epsilon,\frac32-5\epsilon,((0,0),\alpha_K-2)}_{\mathrm b}(M').$$
The $(0,0)$-coefficient at $K^+$ is $\lim_{t_*\to\infty}u_{\mathrm{sing}}(t_*,x) = \int_{\mathbb
R}\partial_{t_*}u_{\mathrm{sing}}\,dt_* = \mathcal F(\partial_{t_*}u_{\mathrm{sing}})(0) = \dot g(\dot b_0)+h(i\hat
S_4)$ ($u_{\mathrm{sing}}\to0$ as $t_*\to-\infty$, $K^-$-weight $\alpha_K-1>0$; integrable, $K$-weights $>1$). Replacing
the cut-off of the $(0,0)$-term by $\chi_K$ changes $u_{\mathrm{sing}}$ by a term supported away from $K^+$ and
$\mathscr I^+$ near $(\iota^+)^\circ$, of $\iota^+$-order 2 ($\dot g,h\in\mathcal A^2$). So, with
$$\dot b := \dot b_0,\qquad\dot S^{(0)}_1 := i\hat S_4\tag{2.11}$$
(the source's (11.133)), $u_{\mathrm{sing}}-\chi_K\big(\dot g(\dot b)+h(\dot S^{(0)}_1)\big)\in
H^{\infty,\frac32-4\epsilon,\frac32-5\epsilon,\alpha_K-2}_{\mathrm b}(M')$. Their reality is shown after Step 6.

*Step 6 (null infinity).* $\tilde u := u-\chi_K(\dot g(\dot b)+h(\dot S^{(0)}_1)) =
u_I+u_\iota+u_{\mathrm{hi}}+u_{\mathrm{reg}}+(u_{\mathrm{sing}}-\chi_K(\cdots))$ has $K^+$-weight $\alpha_K-2$ (Steps
1-5; $c'_K$, $N$, $\alpha_K-1$ are larger) and $\iota^+$-weight $\ell'_+ := \frac32-5\epsilon$. Near $\mathscr I^+$,
$\chi_K = 0$ and $L\tilde u = f$; III.I$'$ Proposition 2.1 with $\ell_+ := \min(\ell'_+,\min\mathrm{Re}\,\mathcal
E_+-\epsilon)$, as in III.I$'''$ Step 4, gives the $\mathscr I^+$-data $(\langle\mathcal E^C_I\rangle,\ell_I)$. This is
(2.1). *Reality.* $u$ is real, as $f$ and $L$ are and forward solutions are unique; $\dot g$ and $h$ are real on real
arguments, so $\chi_K\big(\dot g(\mathrm{Im}\,\dot b)+h(\mathrm{Im}\,\dot S^{(0)}_1)\big) = -\mathrm{Im}\,\tilde u$ has
$K^+$-weight $\alpha_K-2>0$. A stationary tensor of positive $K^+$-weight vanishes on $X^\circ$, so $\dot
g(\mathrm{Im}\,\dot b)+h(\mathrm{Im}\,\dot S^{(0)}_1) = 0$, and $\mathrm{Im}\,\dot b = 0$, $\mathrm{Im}\,\dot S^{(0)}_1
= 0$ by the rows of III.H (3.1). *Continuity:* every map above is linear and bounded between the spaces stated (III.H
Proposition 3.2, III.G$''''$ Proposition 5.1's construction, III.I$''$ Lemma 4.2, Lemmas 1.1-1.4, (2.25a), (2.26a), and
Steps 0-2 as in III.I$'''''$). $\square$

## 3. Findings, labels and sources

### 3.1 Findings

(I$''''''$1) *No logarithmic centre-of-mass motion.* The source's $\dot S^{(0,1)}_1$ term, $\chi_Kh^{\le4}_{b,\mathrm
s1}(\dot S^{(0,1)}_1\log t_*)$, comes from the exponent $(1,0)$ at $\iota^+$ and its Proposition 9.11 at $\lambda = 1$.
At $n = 4$ the least $\iota^+$-exponent is $\lambda_\sharp>\frac32$, and the grafted solutions carry $a_{\mathrm
s1}\propto t_*^{-\lambda_0+1}$, centre-of-mass motions that decay at $K^+$; they are part of $\tilde u$ here, and of the
next step's polynomially decaying motions.

(I$''''''$2) *The boost-type term at tf.* III.G$''''$ Proposition 5.1's solution contains
$|\sigma|^{\alpha-3}h(S^{(-1)}_1)$, a translation state with a coefficient singular at $\sigma = 0$. The augmented
operator's rows see it, and left in the first component it would give a row correction of size $|\sigma|^{-\epsilon}$ in
the $\mathcal S_1$-component, which the integration in $t_*$ turns into growth. Lemma 1.4 moves it into the $\mathcal
S_1$-column with coefficient $-\sigma^2|\sigma|^{\alpha-3}S^{(-1)}_1 = O(|\sigma|^{1-\epsilon})$, and Lemma 1.3 shows
the remaining row data are answered by the nullspace with columns $O(|\sigma|^{1-\epsilon})$. The source's
(11.125)-(11.130) assemble $\hat u_{\mathrm{lo}}$ without this bookkeeping.

(I$''''''$3) *What the source needs and n = 4 does not.* Its Step 3.2 with Proposition 9.30 and the expansion (11.107b)
of the zero energy solution are not needed (III.I$'''''$ (I$'''''$3)); its tf-improvement by Proposition 9.35 is
(III.G$''''$ Proposition 5.1), because the first moment $\int t_*f^\flat\,dt_*$ has the borderline weight 2. The range
$\alpha_K-2<\epsilon_{\mathrm{ind}}$ is the source's.

(I$''''''$4) *Admissibility of conormal sections.* The identification (2.8) needs every piece in $\mathcal X_\sigma$;
the conormal piece of III.G$''''$ Proposition 5.1's solution lies in it for an order family lowered near
$R_{\mathrm{out}}$, the zero section over $\partial X$ (a radial set, where only an upper threshold applies), and the
inverses on the two spaces agree, as the kernels do not depend on the order (Lemma 1.2). The source uses the
identification without comment.

### 3.2 Labels

Proved: Lemmas 1.1-1.4 and Proposition 2.1, given the parts cited. Comparisons with the source are commentary. READ: the
source's statements quoted from pp. 252-256. Inputs: I.A (4.6), section 7, Lemmas 7.1, 7.4 (a), Theorem 7.2 (5) and its
proof; III.G$''''$ Lemma 4.3; III.H (3.1), Lemma 2.5 (b), Theorem 4.1; III.I$'''$ section 1; II.E Proposition 3.4;
II.G$'$ section 3.1, Propositions 3.3 (1), 3.5 (1) ((2.25a), (2.26a)); III.F$''$ (mode stability); III.F$'''$
Proposition 4.1 (1); III.G$''$ (4.2), Corollary 4.3; III.G$''''$ Proposition 5.1; III.H section 1, (2.6), (3.1),
Definitions 2.1, 3.1, Lemmas 2.2, 2.4 (a), 2.5 (b)-(d), Proposition 3.2, Theorem 4.1; III.I Proposition 4.1; III.I$'$
Proposition 2.1; III.I$''$ section 4, (4.1), Lemmas 2.1, 4.1-4.3; III.I$'''$ Lemmas 1.1-1.3, Proposition 2.1's proof;
III.I$''''$ (2.4), Lemma 2.5, Proposition 4.1; III.I$'''''$ section 1, Proposition 2.1 and its proof.

### 3.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 11.6.1 (pp. 252-256:
Proposition 11.34, Remark 11.35, (11.116)-(11.133)). N1STAR-PROOF.md 10.45 (b) and 10.61 (b) (the deductions this part
replaces).
