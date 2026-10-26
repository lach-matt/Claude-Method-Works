# Part III.I$'''$. The boost parameter, n = 4 ([Hin26] section 11.4.1)

*Status.* Verified (D259: the hundred-and-ninth verifier; no major finding, three minor ones and seven nits seated, to
be read). Written (D257). This part proves, at spatial dimension $n = 4$, [Hin26] section 11.4.1 (pp. 238-241): for
sources with more than one order of decay at $K^+$, the forward solution of $L^{g,g_0}u = f$ is $\chi_Kh^{\le1}(\dot
S)$, a cut-off generalised zero energy state of the boosts, plus a remainder of $K^+$-weight $\alpha_K-2>-1$
(Proposition 11.20), with the description of the augmented operator near zero energy that it uses (Lemma 11.21).

*What n = 4 changes.* The scheme is the source's: Proposition 11.17 and the forward mapping put $L_bu$ one order better
at $K^+$; null infinity is solved away (Proposition 11.16); at low frequencies the zero energy part of the source is
inverted by the augmented operator at $\sigma = 0$, its zf-leading term subtracted, and the rest inverted as in
section 11.3; two integrations in $t_*$ leave a term linear in $t_*$ at $K^+$, whose coefficient is $h(\hat S_1(0))$.
At $n = 4$ three steps simplify. The formal solution at null infinity has $\iota^+$-index set starting at
$\frac32+(1-e_\Upsilon)\gamma_\Upsilon$ (III.I$'$ Proposition 3.1), above the weight used, so the source's Step 2 (its
Proposition 9.11 at $\lambda = 1$, removing a $t_*^{-3}$ term at $\iota^+$) is not needed. The zero energy window is
$(0,1)$, III.H (1.1)'s window inside the gap of $\widehat{L_b}(0)$ (III.F$'$ Proposition 2.3 (a)), where the source's is
$(0,\epsilon_{\mathrm{ind}})$. And the remainder keeps the $\iota^+$-weight
$\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal E_+)-\epsilon$, where the source's is $1-\epsilon$, "limited by 1 due
to transport from $\mathscr I^+$" (its p. 238). Everything is at $b = b_0$, as in III.I Theorem 5.3. Notation: Parts
II.G$'$, III.A, III.H, III.H$'$, III.I, III.I$'$ and III.I$''$, whose section 1 is the setting here; no instrument is
used.

## 1. Profiles at zero energy ([Hin26] Lemma 11.21 at n = 4)

On $X^\pm_{\mathrm{sc}\text-\mathrm b}$ over $\pm[0,c]$ the weights are II.G$'$ (3.2)'s, with $\rho = \langle
x\rangle^{-1}$, and $\chi_{\mathrm{zf}} := \chi_1(\hat r)$, $\hat r := |\sigma|\langle x\rangle$, is II.G$'$ section
3.1's cut-off (1 for $\hat r\le\frac18$, 0 for $\hat r\ge\frac14$). The space $H^{k,(\gamma_{\mathrm{scf}},\gamma
_{\mathrm{tf}},((0,0),\gamma_{\mathrm{zf}}))}_{\mathrm b}$, $\gamma_{\mathrm{zf}}\in(0,1)$, is that of $\chi_{\mathrm
{zf}}v_0+\tilde u$ with $v_0\in H^{k,\gamma_{\mathrm{tf}}}_{\mathrm b}(X)$ (its zf-coefficient, the same for both signs
when so stated) and $\tilde u\in H^{k,\gamma}_{\mathrm b}$ (II.G$'$ section 3.1). Throughout, $c\le\frac1{8\sqrt5}$, so
that $\chi_{\mathrm{zf}} = 1$ on $\{r\le2\}$ for $|\sigma|\le c$, and $c$ is also below the $k$-independent bound of
(2.4) ($\chi_{\mathrm{zf}} = 1$ on $\mathrm{supp}\,f^*_j$).

**Lemma 1.1 (profiles independent of $\sigma$).** Let $a\in\mathbb R$, $P\in\rho^p\mathrm{Diff}^m_{\mathrm b}(\bar X)$
with smooth coefficients, $p\ge0$, $j\in\mathbb N_0$, and $u_0\in H^{\infty,a}_{\mathrm b}(X)$. Then

(a) $\sigma^j\chi_{\mathrm{zf}}Pu_0\in H^{\infty,(\infty,a+p+j,\gamma_{\mathrm{zf}})}_{\mathrm
b}(X^\pm_{\mathrm{sc}\text-
\mathrm b})$ for every $\gamma_{\mathrm{zf}}<j$;

(b) $[P,\chi_{\mathrm{zf}}]u_0$ (for $m\ge1$) and $(\chi'-\chi_{\mathrm{zf}})u_0$, $\chi'$ any other function of $\hat
r$ equal to 1 near 0 and with compact support, lie in $H^{\infty,(\infty,a+p,\infty)}_{\mathrm b}$, resp.
$H^{\infty,(\infty,a,\infty)}_{\mathrm b}$.

*Proof.* On $\mathrm{supp}\,\chi_{\mathrm{zf}}$, $|\sigma|\le\rho/4$, so by (3.2) of II.G$'$
$\rho_{\mathrm{tf}}\sim\rho$, $\rho_{\mathrm{zf}}\sim\hat r = |\sigma|/\rho$ and $\rho_{\mathrm{scf}}\sim1$, and the
weight is $w_\gamma\sim
\rho^{\gamma_{\mathrm{tf}}-\gamma_{\mathrm{zf}}}|\sigma|^{\gamma_{\mathrm{zf}}}$. (a) By Fubini,
$$\iint|\sigma|^{2j}|Pu_0|^2\rho^{-2(\gamma_{\mathrm{tf}}-\gamma_{\mathrm{zf}})}|\sigma|^{-2\gamma_{\mathrm{zf}}}
1_{|\sigma|\le\rho/4}\,|\tfrac{d\sigma}\sigma|\,\mu_X = C\int|Pu_0|^2\rho^{-2(\gamma_{\mathrm{tf}}-j)}\mu_X,$$
the inner integral $\int_0^{\rho/4}\sigma^{2(j-\gamma_{\mathrm{zf}})}\frac{d\sigma}\sigma$ converging as $\gamma_{\mathrm
{zf}}<j$; this is finite for $\gamma_{\mathrm{tf}}\le a+p+j$, as $Pu_0\in H^{\infty,a+p}_{\mathrm b}(X)$. The fields
$\sigma\partial_\sigma$ and $\langle x\rangle\partial_x$ fall on $\sigma^j$, on $\chi_{\mathrm{zf}}$ (bounded
derivatives, II.G$'$ section 3.1) and on $Pu_0$, with the same bound. (b) The coefficients of $[P,\chi_{\mathrm{zf}}]$
and $\chi'-\chi_{\mathrm{zf}}$ are supported in $\hat r\in[\delta,\delta^{-1}]$, a compact subset of the interior of tf,
where $w_\gamma\sim\rho^{\gamma_{\mathrm{tf}}}$; Fubini with $\int_{\delta\rho}^{\rho/\delta}\frac{d\sigma}\sigma =
2\log\delta^{-1}$ gives the norm $C\|\rho^{-\gamma_{\mathrm{tf}}}\cdot\|_{L^2(\mu_X)}$ of $Pu_0$-type terms, finite for
$\gamma_{\mathrm{tf}}\le a+p$, resp. $a$. $\square$

**Lemma 1.2 ([Hin26] Lemma 11.21 at n = 4: the augmented operator near zero energy).** For $u_0\in H^{\infty,a}_{\mathrm
b}(X)$ and $|\sigma|\le c$:

(a) $(\widehat{L_b}(\sigma)-\widehat{L_b}(0))(\chi_{\mathrm{zf}}u_0)\in H^{\infty,(\infty,a+2,\gamma_{\mathrm{zf}})}
_{\mathrm b}$ for every $\gamma_{\mathrm{zf}}<1$;

(b) for $\dot b\in\mathfrak b$, $S\in\mathcal S_1$ and the columns $\hat f_{\dot b}$, $\hat f_S$ of III.H Definition 2.1,
$\hat f_{\dot b}(\sigma)-\chi_{\mathrm{zf}}\hat f_{\dot b}(0)$ and $\hat f_S(\sigma)-\chi_{\mathrm{zf}}\hat f_S(0)$ lie
in $H^{\infty,(N,3-\epsilon,1-\epsilon)}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$ for every $N$ and $\epsilon>0$,
and $\hat f_{\dot b}(0),\hat f_S(0)\in\mathcal A^3\subset H^{\infty,3-\epsilon}_{\mathrm b}(X)$.

The source's (11.64) has $\rho_{\mathrm{tf}}^2\rho_{\mathrm{zf}}\mathrm{Diff}^1_{\mathrm b}$ for (a) and
$H^{k,3-\epsilon, 2+\epsilon_{\mathrm{ind}}-\epsilon,1-\epsilon}$ for the columns, from its Lemma 10.5; at $n = 4$ the
columns are one order better at tf and the rows of $\tilde L_b(\sigma)$ do not depend on $\sigma$ (III.H Definition 3.1).

*Proof.* (a) $\widehat{L_b}(\sigma)-\widehat{L_b}(0) = -i\sigma L_1-\sigma^2L_2$ with $L_1\in\rho\,\mathrm{Diff}^1
_{\mathrm b}$, $L_2\in\rho^2C^\infty$ near $\partial X$ and smooth coefficients on compact sets (III.H section 1). Write
$L_1\chi_{\mathrm{zf}} = \chi_{\mathrm{zf}}L_1+[L_1,\chi_{\mathrm{zf}}]$: Lemma 1.1 (a) with $(p,j) = (1,1)$ and $(2,2)$
gives $\sigma\chi_{\mathrm{zf}}L_1u_0$ and $\sigma^2\chi_{\mathrm{zf}}L_2u_0$ in the space stated, and Lemma 1.1 (b)
gives $[L_1,\chi_{\mathrm{zf}}]u_0\in H^{\infty,(\infty,a+1,\infty)}_{\mathrm b}$, which $\sigma$ (of tf-order 1 on the
interior of tf) brings to $a+2$. (b) By III.H Lemma 2.4 (a), $\hat f = \hat f_c+\hat f_\infty$ with $\hat f_c$ entire in
$\sigma$ and supported in $\{r\le2\}$, and $\hat f_\infty = r^{-3}G(\sigma r,x)$ on $\{r\ge1\}$, $G$ entire with
$|(\zeta\partial_\zeta)^j(r\partial_r)^a\partial^\beta_\omega G|\le C\langle\zeta\rangle^{-N}$ for $\mathrm{Im}\,\zeta
\ge0$. For $|\sigma|$ small, $\chi_{\mathrm{zf}} = 1$ on $\{r\le2\}$, so $\hat f_c(\sigma)-\chi_{\mathrm{zf}}\hat f_c(0)
= \hat f_c(\sigma)-\hat f_c(0) = O(|\sigma|)$ in $C^\infty$, supported in $\{r\le2\}$, where
$\rho_{\mathrm{zf}}\sim|\sigma|$: weight $1-\epsilon$ at zf, and no condition at tf or scf. On $\{r\ge1\}$, $H :=
G(\sigma r,x)-\chi_1(|\sigma|
\langle x\rangle)G(0,x)$ satisfies $|VH|\le C\min(|\sigma|r,1)\langle\sigma r\rangle^{-N}$ for products $V$ of
$\sigma\partial_\sigma$, $r\partial_r$, $\partial_\omega$ ($G(\zeta)-G(0) = O(|\zeta|)$ where $\chi_1 = 1$; rapid decay
where $\chi_1 = 0$; $|\sigma|\langle x\rangle\sim|\sigma|r$ in between). With $w_\gamma\sim\rho^{\gamma_{\mathrm{tf}}-
\gamma_{\mathrm{zf}}}|\sigma|^{\gamma_{\mathrm{zf}}}$ on $\{\hat r\le1\}$, Fubini bounds that part of the squared norm of
$r^{-3}H$ by $C\int\langle x\rangle^{-4+2(\gamma_{\mathrm{tf}}-\gamma_{\mathrm{zf}})}\int_0^{1/\langle x\rangle}
\sigma^{2-2\gamma_{\mathrm{zf}}}\frac{d\sigma}\sigma\,\mu_X = C'\int\langle
x\rangle^{2\gamma_{\mathrm{tf}}-6}\mu_X<\infty$ for $\gamma_{\mathrm{zf}}<1$, $\gamma_{\mathrm{tf}}<3$; on $\{\hat
r\ge1\}$ the rapid decay in $\hat r$ and $r^{-3}\le (\rho_{\mathrm{scf}}\rho_{\mathrm{tf}})^3$ give the bound as in
III.H Lemma 2.4 (b)'s proof. $\hat f(0)\in\mathcal A^3$ is III.H Lemma 2.3. $\square$

**Lemma 1.3 (the cut-off states near zero energy).** With $G_1$, $G_2$ of III.I$''$ (4.1) and $\chi$ the cut-off of
III.I$''$ section 4: for $\dot b_0\in\mathfrak b$ and $S_0\in\mathcal S_1$,
$$\chi(|\sigma|)G_1(\sigma)(\dot b_0)-\chi_{\mathrm{zf}}\dot g(\dot b_0)\in H^{\infty,(N,2-\epsilon,1-\epsilon)}_{\mathrm
b},\qquad\chi(|\sigma|)G_2(\sigma)(S_0)-\chi_{\mathrm{zf}}h(S_0)\in H^{\infty,(N,3-\epsilon,1-\epsilon)}_{\mathrm b}$$
for every $N$ and $\epsilon>0$; and $\dot g(\dot b_0)\in H^{\infty,2-\epsilon}_{\mathrm b}(X)$, $h(S_0)\in
H^{\infty,3-\epsilon}_{\mathrm b}(X)$.

*Proof.* As Lemma 1.2 (b): for $r\ge1$, $\Psi = \Phi(\sigma r)$ with $\Phi(0) = 1$ (III.H Lemma 2.5 (b)), so $G_1
(\dot b_0)-\chi_{\mathrm{zf}}\dot g = (\Phi(\sigma r)-\chi_1(|\sigma|\langle x\rangle))\dot g$ and
$G_2(S_0)-\chi_{\mathrm {zf}}h = ((\Phi-\zeta\Phi')(\zeta)-\chi_1)h-i\zeta\Phi(\zeta)r^{-1}\breve h$, $\zeta = \sigma
r$, both $O(\min(|\zeta|,1)
\langle\zeta\rangle^{-N})$ times states in $\mathcal A^2$, resp. $\mathcal A^3$ (III.H section 1; $r^{-1}\breve h\in
\mathcal A^3$); for $r\le1$, $\Psi-1 = O(|\sigma|)$ with derivatives (III.H Lemma 2.5 (d) and its proof); and
$\chi(|\sigma|)-1$ vanishes for $|\sigma|\le\frac c2$, where on $\mathrm{supp}\,\chi_{\mathrm{zf}}$ the remaining term
is supported in a compact set of $x$ away from tf and zf. The Fubini count of Lemma 1.2 (b) with $\langle x\rangle^{-2}$
in place of $\langle x\rangle^{-3}$ gives $\gamma_{\mathrm{tf}}<2$ for $G_1$. $\square$

## 2. The boost parameter ([Hin26] Proposition 11.20 at n = 4)

Let $h^{\le1}(S) = t_*h(S)+\breve h(S)$ be III.H section 1's generalised state of the boosts ($h(S) = h_{b_0,\mathrm
s1}(S)$, the source's $h^{\le1}_{b,\mathrm s1}$ of its (6.37), (6.32b)) and $\chi_K$ the cut-off of III.H (1.2).

**Proposition 2.1 ([Hin26] Proposition 11.20 at n = 4, at $b_0$).** Let $\ell_I$ satisfy III.I$''$ (5.1), $\alpha_K\in
(1,\min(a_K-1,\frac32))$ and $\alpha_+>\alpha_K$. For $f\in H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),
\alpha_++2,\alpha_K}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-}$, the forward solution of $Lu = f$ is
$$u = \chi_Kh^{\le1}(\dot S)+\tilde u,\qquad\dot S\in\mathcal S_1,\quad\tilde u\in H^{\infty,(\langle\mathcal E^C_I
\rangle,\ell_I),\beta_+,\alpha_K-2}_{\mathrm b}(\Omega_*)^{\bullet,-}\ \text{for every }\beta_+<\min(\alpha_+,\tfrac32,
\min\mathrm{Re}\,\mathcal E_+),\tag{2.1}$$
with $\dot S$ and $\tilde u$ depending continuously on $f$.

$\dot S$ is determined by $u$: $\tilde u$ has $K^+$-weight $\alpha_K-2>-1$, so $h(\dot S)$ is the coefficient of $t_*$
in $u$ at $K^+$, and $S\mapsto h(S)$ is injective (III.F$'''$ Proposition 4.1 (1)). The source's (11.63) has
$\iota^+$-weight $1-\epsilon$ and $\alpha_K\in(1,1+\epsilon_K)$.

*Proof.* *Step 0 (the source's (11.65)).* Fix $\alpha'_K\in[\frac12,1)$ with $\alpha'_K\ge\alpha_K-(a_K-2)$, possible as
$\alpha_K<a_K-1$, and $\beta'_+\in(1,\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal E_+))$. III.I$''$ Proposition 5.1
(with $\alpha'_K$ for $\alpha_K$; $\alpha_+>\alpha'_K$) gives $u\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),
\beta'_+,\alpha'_K-2}_{\mathrm b}$, and III.I Proposition 4.1 (4.2) ($\frac32<\ell_I<a_I+\frac12$, $\beta'_+<\min\mathrm
{Re}\,\mathcal E_+$) gives $(L-L_b)u$ the $\iota^+$-weight $\beta'_++2+m_+-\epsilon>4$ (no expansion term, as $\beta'_++
m_+<2\min\mathrm{Re}\,\mathcal E_+$) and the $K^+$-weight $\alpha'_K-2+a_K\ge\alpha_K$. Fix
$$\alpha^\sharp_+\in\big(\alpha_K,\ \min(\alpha_+,\tfrac32+(1-e_\Upsilon)\gamma_\Upsilon)\big),\tag{2.2}$$
with $\alpha^\sharp_+\ge\min(\alpha_+,\frac32)-\epsilon$ for a given small $\epsilon>0$; then
$\alpha^\sharp_+\in(1,\frac74)\subset(1,2)$ (as $\gamma_\Upsilon<\frac14$, III.C (1.1)), $\alpha^\sharp_+-1\in(0,1)$ and
$\alpha^\sharp_+-\alpha_K\in(0,1)$. So
$$L_bu = f' := f-(L-L_b)u\in H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),\alpha^\sharp_++2,\alpha_K}_{\mathrm
b}(\Omega_*)^{\bullet,-}.$$

*Step 1 (null infinity; the source's (11.66a)).* III.I$'$ Proposition 3.1 with $\breve{\mathcal E}_+ := \emptyset$,
$\breve\ell_+ := \alpha^\sharp_+$ ($\alpha^\sharp_+<\frac32+(1-e_\Upsilon)\gamma_\Upsilon<\min\mathrm{Re}\,\mathcal
E^C_I$ by III.C Definition 3.1 (2), so $\alpha^\sharp_+\notin\mathrm{Re}\,\pi_1\mathcal E^C_I$ and
$\alpha^\sharp_+\ne\frac32+(1-e_\Upsilon)\gamma_\Upsilon$) gives $u_I$, supported near $\mathscr I^+$ and vanishing for
$t_*<1$, with $\iota^+$-data $(\mathcal E^\sharp_+,\alpha^\sharp_+)$ and $f'-L_bu_I\in H^{\infty,\ell_I+1,(\mathcal
E^\sharp_++2,\alpha^\sharp_++2),\alpha_K}_{\mathrm b}$. As $\min\mathrm{Re}\,\mathcal E^\sharp_+ = \frac32+(1-e_\Upsilon)
\gamma_\Upsilon>\alpha^\sharp_+$ (III.I$'$ (3.2) with $\breve{\mathcal E}_+ = \emptyset$; $\min\mathrm{Re}\,\mathcal
E^C_I$ is larger), both are plain weights:
$$u^\flat := u-u_I:\qquad L_bu^\flat = f^\flat := f'-L_bu_I\in H^{\infty,\ell_I+1,\alpha^\sharp_++2,\alpha_K}_{\mathrm b}
(\Omega_*)^{\bullet,-}.$$
The source's $\mathcal E^\sharp_+$ contains $(1,0)$, which leaves a $t_*^{-3}$ term at $\iota^+$ in $f^\flat$ that its
Step 2 removes by its Proposition 9.11 at $\lambda = 1$; at $n = 4$ there is no such term, and no Step 2 ((I$'''$1)).
$u^\flat$ vanishes for $t_*<1$, so it is the forward solution of $L_bu^\flat = f^\flat$ (II.E Proposition 3.4).

*Step 2 (the decomposition).* As in III.I$''$ section 4, $u^\flat = u_{\mathrm{hi}}+u_{\mathrm{reg}}+u_{\mathrm{sing}}$.
The memberships (2.3)-(2.13) are read as there: at order $k$, with the $c$ of that order and of III.H's weight $\alpha$,
$\alpha+2 = \alpha^\sharp_+-\alpha_K$; $u$, $u_I$, $u^\flat$, $\dot S = S_0$ (from $\tilde L_b(0)^{-1}$) and $\tilde u$
do not depend on $c$, so their memberships hold at every order. III.I$''$ Lemma 4.1 ($\beta^f_I = \ell_I$, $\beta_\iota
= \alpha^\sharp_+$, $\beta_K = \alpha_K\in(1,2)$; $\ell_I+1\ge
\alpha^\sharp_++2-(1-\epsilon_1)$ as $\ell_I\ge2$) gives $u_{\mathrm{hi}}\in H^{\infty,(\frac32-\epsilon,N,N)}_{\mathrm
b}(M')$. (2.25a) (II.G$'$ Proposition 3.3 (1), with $\beta_K = \alpha_K\in(1,2)$) gives
$$\hat f^\flat|_{\pm(0,c]}\in H^{\infty,(3-\epsilon,\alpha^\sharp_++1,((0,0),\alpha_K-1))}_{\mathrm b}
(X^\pm_{\mathrm{sc}\text-\mathrm b}),\tag{2.3}$$
(its scf-weight is $\min(\ell_I+1,\alpha^\sharp_++2)-\epsilon\ge3-\epsilon$), with zf-coefficient $\hat f^\flat(0) =
\int f^\flat\,dt_*\in H^{\infty,\alpha^\sharp_++1}_{\mathrm b}(X)$, the same for both signs ($f^\flat(\cdot,x)$ is
integrable, its $K^+$-weight being $\alpha_K>1$).

*Step 3.1 (zero energy; the source's (11.68)-(11.70)).* By III.H Proposition 3.2 at the weight $\alpha :=
\alpha^\sharp_+-3$ ($\alpha+2 = \alpha^\sharp_+-1\in(0,1)$; $\mathcal Y_0 = \bar H^{s-1,\alpha+2}_{\mathrm b}$ is the
$\mu_{\mathrm b}$-weight $\alpha^\sharp_++1$, II.G$'$ section 4.1), at every regularity $s$ (III.H, after Proposition
3.2),
$$(\hat u_0,\dot b_0,S_0) := \tilde L_b(0)^{-1}(\hat f^\flat(0),0,0),\qquad\hat u_0\in H^{\infty,\alpha^\sharp_+-1}
_{\mathrm b}(X),\quad\dot b_0\in\mathfrak b,\quad S_0\in\mathcal S_1.\tag{2.4}$$
The rows of $\tilde L_b(\sigma)$ do not depend on $\sigma$, and $\langle\chi_{\mathrm{zf}}\hat u_0,f^*_j\rangle =
\langle\hat u_0,f^*_j\rangle = 0$ once $c$ is so small that $\chi_{\mathrm{zf}} = 1$ on $\mathrm{supp}\,f^*_j$; and
$\chi_{\mathrm{zf}}\hat u_0\in\mathcal X_\sigma$ for $\sigma\ne0$ (compact support in $x$). So, for $0<|\sigma|\le c$,
$$\tilde L_b(\sigma)\big(\chi_{\mathrm{zf}}\hat u_0,\dot b_0,S_0\big) = \big(\hat f^\flat(\sigma)-\hat f_2(\sigma),0,0
\big),\tag{2.5}$$
$$\hat f_2 := \big(\hat f^\flat-\chi_{\mathrm{zf}}\hat f^\flat(0)\big)-[\widehat{L_b}(0),\chi_{\mathrm{zf}}]\hat u_0-
\big(\widehat{L_b}(\sigma)-\widehat{L_b}(0)\big)(\chi_{\mathrm{zf}}\hat u_0)-\big(\hat f_{\dot b_0}(\sigma)-\chi
_{\mathrm{zf}}\hat f_{\dot b_0}(0)\big)-\big(\hat f_{S_0}(\sigma)-\chi_{\mathrm{zf}}\hat f_{S_0}(0)\big),$$
using $\widehat{L_b}(0)\hat u_0+\hat f_{\dot b_0}(0)+\hat f_{S_0}(0) = \hat f^\flat(0)$ (2.4). The terms: the first lies
in $H^{\infty,(3-\epsilon,\alpha^\sharp_++1,\alpha_K-1)}_{\mathrm b}$ by (2.3) and the definition of the space; the
second in $H^{\infty,(\infty,\alpha^\sharp_++1,\infty)}_{\mathrm b}$ (Lemma 1.1 (b), $p = 2$, $a =
\alpha^\sharp_+-1$); the third in $H^{\infty,(\infty,\alpha^\sharp_++1,\gamma_{\mathrm{zf}})}_{\mathrm b}$ for every
$\gamma_{\mathrm{zf}}<1$ (Lemma 1.2 (a)); the last two in $H^{\infty,(N,3-\epsilon,1-\epsilon)}_{\mathrm b}$ (Lemma 1.2
(b)). As $\alpha^\sharp_+<2-\epsilon$ and $\alpha_K-1<1-\epsilon$ for $\epsilon$ small,
$$\hat f_2|_{\pm(0,c]}\in H^{\infty,(\frac52-\epsilon,\alpha^\sharp_++1,\alpha_K-1)}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-
\mathrm b}).\tag{2.6}$$

*Step 3.2 (the rest; the source's (11.71)).* By (2.5), $(\hat u_{\mathrm{reg},1},\hat b_1,\hat S_1) := \tilde L_b(\sigma)
^{-1}(\hat f^\flat(\sigma),0,0) = (\chi_{\mathrm{zf}}\hat u_0,\dot b_0,S_0)+\tilde L_b(\sigma)^{-1}(\hat f_2(\sigma),0,
0)$. III.I$''$ Lemma 4.2 with $\beta_{\mathrm{scf}} := \frac32-\epsilon$, $\beta_{\mathrm{tf}} := \alpha^\sharp_+-1$,
$\beta_{\mathrm{zf}} := \alpha_K-1$ ($\alpha+2 := \alpha^\sharp_+-\alpha_K\in(0,1)$) applies to (2.6), so
$$\hat u_{\mathrm{reg},1}\in H^{\infty,(\frac32-2\epsilon,\alpha^\sharp_+-1,((0,0),\alpha_K-1))}_{\mathrm b},\qquad
\hat b_1\in H^{\infty,((0,0),\alpha_K-1)}_{\mathrm b}(\pm(0,c],|\tfrac{d\sigma}\sigma|;\mathfrak b),\quad\hat S_1\in
H^{\infty,((0,0),\alpha_K-1)}_{\mathrm b}(\pm(0,c],|\tfrac{d\sigma}\sigma|;\mathcal S_1),\tag{2.7}$$
with the coefficients $\hat u_0$, $\dot b_0$, $S_0$ at $\sigma = 0$, the same for both signs ($\hat u_0\in H^{\infty,
\alpha^\sharp_+-1}_{\mathrm b}(X)$ being the zf-coefficient of the tf-weight $\alpha^\sharp_+-1$). By (2.26a) (applied
to $\chi(|\sigma|)\hat u_{\mathrm{reg},1}$, supported where II.G$'$ Proposition 3.5's cut-off is 1, $c\le\frac12$;
$\beta_K = \alpha_K\in(1,2)$; the one Taylor coefficient, of order $0<\alpha_K-1$, agrees for the two signs),
$$u_{\mathrm{reg}}\in H^{\infty,(\min(\frac32,\alpha^\sharp_+)-3\epsilon,\alpha^\sharp_+,\alpha_K)}_{\mathrm b}(M').
\tag{2.8}$$

*Step 3.3 (the singular part; the source's (11.72)-(11.74)).* By III.I$''$ (4.1), Lemma 1.3 and III.I$''$ Lemma 4.3
(with $a = \alpha_K-1$, for $\hat b_1-\dot b_0$ and $\hat S_1-S_0$),
$$\mathcal F(\partial_{t_*}\dot g)\in H^{\infty,(N,2-\epsilon,((0,0),\alpha_K-1))}_{\mathrm b},\qquad\mathcal F(\partial
^2_{t_*}h_{\mathrm s1})\in H^{\infty,(N,3-\epsilon,((0,0),\alpha_K-1))}_{\mathrm b},$$
with zf-coefficients $\dot g(\dot b_0)$ and $h(S_0)$; the tf-weights $\alpha_K+1-\epsilon$, $\alpha_K+2-\epsilon$ of the
remainders exceed $2-\epsilon$, $3-\epsilon$, and $1-\epsilon>\alpha_K-1$. Multiplication by $-i\sigma$ takes the first
to $H^{\infty,(N,3-\epsilon,\alpha_K-1)}_{\mathrm b}$ with zero zf-coefficient (Lemma 1.1 (a) with $j = 1$ for
$\sigma\chi_{\mathrm{zf}}\dot g(\dot b_0)$; $\alpha_K-1<1$), so
$$\mathcal F(\partial^2_{t_*}u_{\mathrm{sing}})\in H^{\infty,(N,3-\epsilon,((0,0),\alpha_K-1))}_{\mathrm b}(X^\pm
_{\mathrm{sc}\text-\mathrm b}),\quad\text{with zf-coefficient }h(S_0),\ \text{the same for both signs}.\tag{2.9}$$
(This is the source's (11.72a)-(11.72b), with the tf-weight $3-\epsilon$ for its $2-\epsilon$.) As $u^\flat = 0$ for
$t_*<1$, $u_{\mathrm{sing}} = -(u_{\mathrm{hi}}+u_{\mathrm{reg}})$ there, so by (2.8)
$$u_{\mathrm{sing}}|_{\Omega_-}\in\bar H^{\infty,\min(\frac32,\alpha^\sharp_+)-3\epsilon,\alpha^\sharp_+,\alpha_K}
_{\mathrm b},\qquad\partial_{t_*}u_{\mathrm{sing}}|_{\Omega_-}\in\bar H^{\infty,\min(\frac32,\alpha^\sharp_+)-3\epsilon,
\alpha^\sharp_++1,\alpha_K+1}_{\mathrm b}.\tag{2.10}$$
*First integration.* III.I$''$ Lemma 3.1 for $v := \partial_{t_*}u_{\mathrm{sing}}$ with $\beta_I := \frac32$,
$\beta_\iota := \alpha^\sharp_++1$, $\beta_K := \alpha_K-1\in(0,\frac12)$: $\beta_\iota>\beta_I$; $\beta_K\le\beta_\iota-
\beta_I = \alpha^\sharp_+-\frac12$ (as $\alpha^\sharp_+>\alpha_K$); $\beta_K\in(-1,1)\setminus\{0\}$; the zf-restrictions
of the two signs agree (2.9); $v|_{\Omega_<}$ has weights at least $(\infty,\beta_\iota,\beta_K)$ by (2.10); $\mathcal
Fv$ is supported in a compact subset of $(-c,c)$, $c\le\frac12$, as III.I$''$ Lemma 3.1 asks (III.I$''$ Step 2b's
reason); and (2.9)'s tf-weight $3-\epsilon$ is at least $\beta_\iota =
\alpha^\sharp_++1$. So
$$\partial_{t_*}u_{\mathrm{sing}}\in H^{\infty,\frac32,\alpha^\sharp_++1-\epsilon,((0,0),\alpha_K-1)}_{\mathrm b}(M').
\tag{2.11}$$
*Second integration.* III.I$''$ Lemma 2.1 (1) for $u_{\mathrm{sing}}$ with $(\beta_I,\beta_\iota,\beta_K) :=
(\min(\frac32,\alpha^\sharp_+)-3\epsilon,\alpha^\sharp_+-\epsilon,\alpha_K-2)$ and $\mathcal E_K := \{(-1,0)\}$, so that
$\mathcal E_K+1 = \{(0,0)\}$ ($\alpha_K-2\in(-1,-\frac12)$, $\ne0$); the hypotheses are (2.10) (at $K^-$ the weight
$\alpha_K$, with no expansion) and (2.11). So
$$u_{\mathrm{sing}}\in H^{\infty,\min(\frac32,\alpha^\sharp_+)-3\epsilon,\min(\frac32,\alpha^\sharp_+)-4\epsilon,
(\{(-1,0),(0,0)\},\alpha_K-2)}_{\mathrm b}(M'),\tag{2.12}$$
in which only $(-1,0)$ lies below the weight $\alpha_K-2\in(-1,-\frac12)$: $u_{\mathrm{sing}} = t_*\chi_Ku_{K^+}+
O(\alpha_K-2)$ at $K^+$ for some $u_{K^+}$ on $K^+$.

*Step 3.4 (the coefficient; the source's (11.75)).* $u_{K^+}$ is the $(0,0)$-coefficient of $\partial_{t_*}u_{\mathrm
{sing}}$ at $K^+$ in (2.11), that is, $\lim_{t_*\to\infty}\partial_{t_*}u_{\mathrm{sing}}(t_*,x)$. As $\partial_{t_*}
u_{\mathrm{sing}}$ tends to 0 as $t_*\to-\infty$ (its $K^-$-weight $\alpha_K+1>0$) and $\partial^2_{t_*}u_{\mathrm{sing}}
(\cdot,x)$ is integrable (its $K^+$-weight is $\alpha_K>1$ by (2.9) and (2.26a), and $\langle t_*\rangle^{-\alpha_K}L^2(
\frac{dt_*}{\langle t_*\rangle})\subset L^1$ for $\alpha_K>1$), $u_{K^+} = \int_{\mathbb
R}\partial^2_{t_*}u_{\mathrm{sing}}
\,dt_* = \mathcal F(\partial^2_{t_*}u_{\mathrm{sing}})(0) = h(S_0)$ by (2.9). So, with $\dot S := S_0 = \hat S_1(0)$,
$$u_{\mathrm{sing}}-\chi_Kt_*h(\dot S)\in H^{\infty,\min(\frac32,\alpha^\sharp_+)-3\epsilon,\min(\frac32,\alpha^\sharp_+)
-4\epsilon,\alpha_K-2}_{\mathrm b}(M'),\tag{2.13}$$
$\chi_Kt_*h(\dot S)$ itself being $\rho_K^{-1}\rho_\iota^2$ times a bounded conormal function near $\iota^+\cap K^+$
($h\in\mathcal A^3$; $\chi_K = 0$ near $\mathscr I^+$), so of $\iota^+$-weight $2-\epsilon$. Replacing $t_*h$ by
$h^{\le1} = t_*h+\breve h$ changes this by $\chi_K\breve h(\dot S)$, of weights $(\infty,2-\epsilon,-\epsilon)$ ($\breve
h\in\mathcal A^2$, stationary), within (2.13) as $\alpha_K-2<-\epsilon$. In the source, (10.13) identifies the total
integral of $\partial^2_{t_*}h^{\le1,\mathrm{aug}}_{b,\mathrm s1}$ with $h_{b,\mathrm s1}$; here $h^{\mathrm{aug}}(S) =
\chi_Kh^{\le1}(S)$ (III.H Definition 2.1), so $G_2(0)(S) = \Psi(0,\cdot) h(S) = h(S)$ directly.

*Step 4 (null infinity; the source's Step 4).* So $u = \chi_Kh^{\le1}(\dot S)+\tilde u$ with $\tilde u := u_I+u_{\mathrm
{hi}}+u_{\mathrm{reg}}+(u_{\mathrm{sing}}-\chi_Kh^{\le1}(\dot S))$ of $\iota^+$-weight $\ell'_+ :=
\min(\frac32,\alpha^\sharp_+)-4\epsilon$ and $K^+$-weight $\alpha_K-2$ (Steps 1-3; $u_I$ is supported near $\mathscr
I^+$). Near $\mathscr I^+$, $\chi_K = 0$ ($\chi_K$ vanishes for $|x|\ge t_*/2$), so $L\tilde u = f$ there, and III.I$'$
Proposition 2.1 with $\ell_+ := \min(\ell'_+,\min\mathrm{Re}\,\mathcal E_+-\epsilon)$, $\epsilon$ chosen with
$\ell_+\notin\mathrm{Re}\,\pi_1\mathcal E_+$ (lowering the a priori weight is free;
$\frac32<\ell_I<\min(a_I+\frac12,\ell_I^{\max})$ by III.I$''$ (5.1); $\ell_+<\min(\ell_I,a_++\min\mathrm{Re}\,\mathcal
E_+)$; $\ell_+$ below $\min\mathrm{Re}\,\mathcal E_+$, so that $(\mathcal E_+,\ell_+)$ is the weight $\ell_+$, and below
$\min\mathrm{Re}\,\mathcal E^{\mathrm{tot}}_I = \frac32$) gives the $\mathscr I^+$-data $(\langle\mathcal
E^C_I\rangle,\ell_I)$. As $\alpha^\sharp_+\ge\min(\alpha_+,\frac32)-
\epsilon$ and $\epsilon$ is arbitrary, (2.1) holds for every $\beta_+<\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal
E_+)$; $\dot S$ does not depend on these choices, being determined by $u$.

*Continuity.* $f'$ depends continuously on $f$ (III.I$''$ Proposition 5.1 and (4.2)), and $u_I$, $\hat f^\flat(0)$,
$(\hat u_0,\dot b_0,S_0)$, $\hat f_2$, the pieces of Step 2 and the integrations are linear maps bounded between the
spaces above (III.I$'$ Proposition 3.1's construction, III.H Proposition 3.2, Lemmas 1.1-1.3, III.I$''$ Lemmas 2.1, 3.1,
4.1-4.3, (2.25a), (2.26a)). So $\dot S = S_0$ and $\tilde u$ depend continuously on $f$; Step 4 by the closed graph
theorem ($L$ being fixed), or by III.I$'$ Proposition 2.1's constructive bound. $\square$

## 3. Findings, labels and sources

### 3.1 Findings

(I$'''$1) *No $\iota^+$ step.* The source's formal solution at null infinity has $(1,0)$ in its $\iota^+$-index set,
from the radiation coupling, and its Step 2 removes the resulting $t_*^{-3}$ term of the source at $\iota^+$ by its
Proposition 9.11 at $\lambda = 1$. At $n = 4$ the formal solution's $\iota^+$-index set begins at $\frac32+(1-e_\Upsilon)
\gamma_\Upsilon$ (III.I$'$ (I$'$1)), above the weight $\alpha^\sharp_+$ chosen in (2.2), and that step does not occur.

(I$'''$2) *The $\iota^+$-weight.* The remainder keeps $\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal E_+)-\epsilon$,
where the source's is $1-\epsilon$; the cap $\frac32$ is again the transport of the radiation order from $\mathscr I^+$
(III.I$''$ (I$''$1)).

(I$'''$3) *The window.* The zero energy inversion needs $\alpha^\sharp_+-1$ in the gap of $\widehat{L_b}(0)$ and the
remainder $\alpha^\sharp_+-\alpha_K$ in it too: III.H (1.1)'s window $(0,1)$ at $n = 4$, inside the gap (III.F$'$
Proposition 2.3 (a)), for the source's $(0,\epsilon_{\mathrm{ind}})$
("$\alpha_+\in(\alpha_K,1+\epsilon_{\mathrm{ind}})$"). The source's columns (its Lemma 10.5) are of tf-order
$2+\epsilon_{\mathrm{ind}}-\epsilon$, and its (11.70a) needs $\alpha_+<1+\epsilon _{\mathrm{ind}}$ for that reason too;
at $n = 4$ the columns have tf-order $3-\epsilon$ (Lemma 1.2 (b)), and $\alpha^\sharp_+<2$ suffices.

(I$'''$4) *The $K^+$-range.* $\alpha_K<a_K-1$ is needed for (4.2) to reach $K^+$-weight $\alpha_K$ from Proposition
11.17's $\alpha'_K<1$ (the source's $a_K = 2+\epsilon_K$ gives its $\alpha_K<1+\epsilon_K$); $\alpha_K<\frac32$ suffices
for $\alpha_K<\alpha^\sharp_+$ in (2.2), which needs $\alpha_K<\min(\alpha_+,\frac32+(1-e_\Upsilon)\gamma_\Upsilon)$,
and gives $\alpha_K-1<\frac12$.

### 3.2 Labels

Proved: Lemmas 1.1-1.3 and Proposition 2.1, given the parts cited. Comparisons with the source are commentary. READ:
the source's statements quoted from pp. 238-241. Inputs: II.E Proposition 3.4; II.G$'$ section 3.1, section 4.1,
Proposition 3.3 (1); III.A section 4 ((2.25a), (2.26a)); III.C (1.1), Definition 3.1; III.F$'$ Proposition 2.3;
III.F$'''$ Proposition 4.1; III.H section 1, (1.2), Definitions 2.1, 3.1, Lemmas 2.3-2.5, Proposition 3.2; III.I
Proposition 4.1; III.I$'$ (3.2), Propositions 2.1, 3.1; III.I$''$ section 1, (4.1), (5.1), Lemmas 2.1, 3.1, 4.1-4.3,
Proposition 5.1.

### 3.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 11.4.1 (pp. 238-241:
Proposition 11.20, Lemma 11.21, (11.63)-(11.75)). N1STAR-PROOF.md 10.45 (b) and 10.61 (b) (the deductions this part
replaces).
