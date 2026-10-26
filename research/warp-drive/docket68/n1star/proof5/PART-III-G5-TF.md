# Part III.G$''''$. The transition face and grafting on the spectral side at n = 4 ([Hin26] section 9.2)

*Status.* Written (D246). This part proves, at spatial dimension $n = 4$, [Hin26] section 9.2 (pp. 186-199): the formal
solutions at ztf ((9.57)-(9.61), Definition 9.25), the expansion at $\hat r = 0$ of the inverse of the tf-normal
operator (Lemma 9.26, Remarks 9.27-9.28), the grafting of tf-solutions into the low-energy space (Definition 9.29,
(9.72), Proposition 9.30, Remarks 9.31-9.34), and its conormal version (Proposition 9.35). The source uses these results
from its section 11.5 on. As there, only infinite b-regularity is stated; finite b-regularity loses fixed amounts. Parts
are cited as before; the source is [Hin26] = P. Hintz, arXiv:2606.28253v2 (printed page numbers).

*What n = 4 changes.* (a) The tf-normal operator carries $-\hat r\partial_{\hat r}-\frac32-\bar S$ in its first-order
part, and its inverse is III.F$'$ Corollary 3.4, with the sctf weight below $\frac32$ (the source's 1) and the ztf
weight in $[-1,0)$ (the source's $(-\epsilon_{\mathrm{ind}},0)$). (b) The expansion at $\hat r = 0$ runs over the window
$(-3,0]$ of III.G$''$ Table 1.1, with its states and their companions: the class roots are
$2-\lambda^\Upsilon_{\mathrm sl,l+j}$ with $l+j\le4$, the physical roots at $-2$ include the tensor type t2, and no root
at $-3$ enters. (c) So the condition $\ell_{\mathrm{zf}}-\min(\mathrm{Re}\,\alpha_0-2,0)<\ell_K^{\max}\le3$ replaces the
source's $3+\epsilon_{\mathrm{ind}}$ ((G$''''$2)). (d) The spectral family differs from the tf model by
$\rho_{\mathrm{scf}}^2\rho_{\mathrm{tf}}^4\mathrm{Diff}^2_{\mathrm b}$ (Lemma 1.2), the source's $\rho_{\mathrm{tf}}^3$,
as the mass enters at $\rho^2$. (e) Three points of the source are corrected: its (9.59) prints $\rho^{-\lambda-j}$ for
$\rho^{-\lambda+j}$, its (9.58) is the operator of $2\bar L$ ((G$''''$1)), and the first step of its proof of
Proposition 9.35 needs a dilation-invariant inverse in place of a pointwise one ((G$''''$3)).

## 1. Setting

*The space.* For $\sigma\in\pm[0,1]$,
$X^\pm_{\mathrm{sc}\text-\mathrm b} := [\pm[0,1]_\sigma\times\bar X;\{0\}\times \partial\bar X]$, with faces scf, tf, zf
and the defining functions of II.G$'$ (3.2),
$$\rho_{\mathrm{scf}} = \frac\rho{\rho+|\sigma|},\qquad\rho_{\mathrm{tf}} = \rho+|\sigma|,\qquad\rho_{\mathrm{zf}} =
\frac{|\sigma|}{\rho+|\sigma|},\tag{1.1}$$
$\rho = r^{-1}$ near $\partial\bar X = \mathbb S^3$, $X$ the spatial slice of III.B. All spaces on
$X^\pm_{\mathrm{sc}\text-\mathrm b}$ are b-Sobolev and partially polyhomogeneous spaces for a b-density
($|d\sigma/\sigma|$ times a b-density on $X$; III.A section 1, the source's Definitions 2.6-2.8), with orders listed for
scf, tf, zf. Let $\hat r := |\sigma|r = |\sigma|/\rho$. Then $\mathrm{tf} = [0,\infty]_{\hat r}\times\mathbb S^3$ with
faces $\mathrm{ztf} = \{\hat r = 0\} = \mathrm{tf}\cap\mathrm{zf}$ and
$\mathrm{sctf} = \{\hat r = \infty\} = \mathrm{tf}\cap \mathrm{scf}$, $\rho_{\mathrm{sctf}} := (1+\hat r)^{-1}$,
$\rho_{\mathrm{ztf}} := \hat r/(1+\hat r)$, the b-density $|\frac{d\hat r}{\hat r}d\slashed g|$ and $H^{k,a,c}_{\mathrm
b}(\mathrm{tf}) := \rho_{\mathrm{sctf}}^a \rho_{\mathrm{ztf}}^cH^k_{\mathrm b}(\mathrm{tf})$ (I.C section 4.1; III.F$'$
Corollary 3.4). On $\{\rho<\rho_0\}$ the functions $(\sigma,\hat r,\omega)$ are coordinates, in which
$\rho_{\mathrm{scf}} = \rho_{\mathrm{sctf}}$ and $\rho_{\mathrm{zf}} = \rho_{\mathrm{ztf}}$ are functions of $\hat r$
alone, $|\sigma| = \rho_{\mathrm{tf}} \rho_{\mathrm{zf}}$, and the b-vector fields are spanned by
$\sigma\partial_\sigma|_{\hat r}$, $\hat r\partial_{\hat r}|_\sigma$ and $\partial_\omega$ (from
$\sigma\partial_\sigma|_x = \sigma\partial_\sigma|_{\hat r}+\hat r\partial_{\hat r}$ and
$\rho\partial_\rho|_\sigma = -\hat r\partial_{\hat r}$). Near tf $\cap$ zf also $(\rho,\hat r,\omega)$ are coordinates,
with $\rho_{\mathrm{tf}}\sim\rho$ and $\rho_{\mathrm{zf}}\sim\hat r$. Fix $\chi_1\in C^\infty([0,\infty))$ equal to 1 on
$[0,\frac18]$ and 0 on $[\frac14,\infty)$, $\chi_{\mathrm{zf}} := \chi_1(\hat r)$ (1 near zf, 0 near scf; II.G$'$),
$\chi_{\mathrm{ztf}} := \chi_{\mathrm{zf}}|_{\mathrm{tf}}$, and $\chi_{\mathrm{tf}} := \chi_2(\rho+|\sigma|)$ with
$\chi_2\in C^\infty_c([0,\frac12\rho_0))$ equal to 1 near 0.

*The operator.* $L_b$ is the linearised gauge-fixed Einstein operator of III.F, with the parameters and hypotheses of
III.G$''$ section 1; in particular $z_\Upsilon\notin Z_{\mathrm{exc}}$, so that every indicial root of
$\widehat{L_b}(0)$ is simple (III.F$'$ Proposition 2.3 (e)). With $(\mathcal Fu)(\sigma) = \int e^{i\sigma t_*}u\,dt_*$
(III.A (2.2)), so that $\partial_{t_*}$ becomes $-i\sigma$, III.F Lemma 2.1 (2) gives exactly
$$\widehat{\bar L}(\sigma) = i\sigma\rho\big(\rho\partial_\rho-\tfrac32-\bar S\big)+\rho^2\mathcal N,\qquad\mathcal N :=
\rho^{-2}\widehat{\bar L}(0),\tag{1.2}$$
where $\mathcal N$ is a dilation-invariant b-operator in $(\rho\partial_\rho,\partial_\omega)$ (III.F$'$ section 1) and
$\bar S$ a bundle endomorphism depending on $\omega$ alone. Write $\mathcal N(\lambda)$ for its indicial family,
$\mathcal N(\rho^\lambda\phi) = \rho^\lambda\mathcal N(\lambda)\phi$; its roots are the indicial roots of
$\widehat{L_b}(0)$ (III.F$'$ Proposition 2.3). For $\pm\sigma>0$ the tf-normal operator is
$$N_{\mathrm{tf}} := N_{\mathrm{tf}}(\widehat{L_b},\pm1) = \hat r^{-2}N_0+\hat r^{-1}N_1,\qquad N_0 := \mathcal
N(-\hat r\partial_{\hat r}),\quad N_1 := \pm i\big(-\hat r\partial_{\hat r}-\tfrac32-\bar S\big),\tag{1.3}$$
on sections over tf of $\pi_{\mathrm{tf}}^*(S^2T^*X|_{\partial X})$; $P := \hat r^2N_{\mathrm{tf}} = N_0+\hat rN_1$ is a
b-operator at ztf.

**Lemma 1.1 (the tf model).** (1) For $\sigma = \pm|\sigma|\ne0$, $\widehat{\bar L}(\sigma) = |\sigma|^2N_{\mathrm{tf}}$
on $\{\rho<\rho_0\}$, in the coordinates $(\sigma,\hat r,\omega)$ (with $N_{\mathrm{tf}}$ acting at fixed $\sigma$). (2)
$N_0(\hat r^z\phi) = \hat r^z\mathcal N(-z)\phi$. So the Mellin family of $N_0$ (with
$\hat u(\lambda) := \int\hat r^{-\lambda}u\,\frac{d\hat r}{\hat r}$) is $N_0(\lambda) = \mathcal N(-\lambda)$, its roots
are $-\mu$ for the roots $\mu$ of $\widehat{L_b}(0)$, and at each $-\mu$ the inverse $N_0(\lambda)^{-1}$ has a simple
pole whose residue $\Pi_\mu$ has range $\ker\mathcal N(\mu)$. (3)
$N_{\mathrm{tf}}(\widehat{2L_b},\pm1) = 2N_{\mathrm{tf}}$ (I.C (4.1)).

*Proof.* (1) Both sides are b-operators in $(\rho\partial_\rho,\partial_\omega)$ whose coefficients depend on $\omega$
alone, so it suffices to compare them on $\rho^a\phi(\omega)$, $a\in\mathbb C$. By (1.2), $\widehat{\bar
L}(\sigma)(\rho^a\phi) = i\sigma\rho^{a+1}(a-\frac32-\bar S)\phi+\rho^{a+2}\mathcal N(a)\phi$, and with
$\rho = |\sigma|\hat r^{-1}$, $i\sigma = \pm i|\sigma|$, this is
$|\sigma|^{a+2}(\pm i\hat r^{-a-1}(a-\frac32-\bar S)+\hat r^{-a-2}\mathcal N(a))\phi$. And
$|\sigma|^2N_{\mathrm{tf}}(|\sigma|^a\hat r^{-a}\phi)$ is the same, as
$-\hat r\partial_{\hat r}\hat r^{-a} = a\hat r^{-a}$. (`tfgraft5.py` T1 (a).) (2) The first statement is the definition.
The roots are simple, so on each isotypic component (type and harmonic) the determinant of the matrix polynomial
$\mathcal N(\lambda)$ has a simple zero at $\mu$, and
$\mathcal N(\lambda)^{-1} = \mathrm{adj}\,\mathcal N(\lambda)/\det\mathcal N(\lambda)$ has a simple pole with residue
$\mathrm{adj}\,\mathcal N(\mu)/(\det\mathcal N)'(\mu)$. Its range lies in $\ker\mathcal N(\mu)$, as
$\mathcal N(\mu)\,\mathrm{adj}\,\mathcal N(\mu) = 0$, and it is non-zero, as the kernel is one-dimensional, so
$\mathrm{adj}\,\mathcal N(\mu)\ne0$; hence its range is the kernel. Only finitely many components have $\mu$ as a root
(III.F$'$ Proposition 2.3 (f)). Then $\Pi_\mu = -\mathrm{res}_{x = \mu}\mathcal N(x)^{-1}$. (3) I.C (4.1) at
$\hat\sigma = \pm1$ for $\widehat{2L_b}$, with $S_0 = \bar S$ and $N(P^{(0)}) = 2\mathcal N$. $\square$

**Lemma 1.2 ([Hin26] (8.2b), (8.4), (8.15) at n = 4).** On $\{\rho<\rho_0\}$,
$\widehat{L_b}(\sigma)\in\rho_{\mathrm{scf}}\rho_{\mathrm{tf}}^2\mathrm{Diff}^2_{\mathrm
b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$ and $\widehat{L_b}(\sigma)-\widehat{\bar
L}(\sigma)\in\rho_{\mathrm{scf}}^2\rho_{\mathrm{tf}}^4\mathrm{Diff}^2_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$.
On all of $X$, $\widehat{L_b}(\sigma)$ is a differential operator polynomial in $\sigma$ (of degree 2) with smooth
stationary coefficients.

*Proof.* $\rho\partial_\rho$ at fixed $\sigma$ and $\partial_\omega$ lift to b-vector fields (section 1), and smooth
functions of $(\rho,\omega)$ to smooth functions. In (1.2),
$\sigma\rho = \rho_{\mathrm{scf}}\rho_{\mathrm{tf}}^2 \rho_{\mathrm{zf}}$ (up to sign) and
$\rho^2 = \rho_{\mathrm{scf}}^2\rho_{\mathrm{tf}}^2$. By III.F Lemma 2.1 (3),
$2(L_b-\bar L) = -g^{00}_b\partial_{t_*}^2+Q_b\partial_{t_*}+R_b$ with $g^{00}_b\in\rho^2C^\infty$,
$Q_b\in\rho^3\mathrm{Diff}^1_{\mathrm b}$, $R_b\in\rho^4\mathrm{Diff}^2_{\mathrm b}$, so
$2(\widehat{L_b}(\sigma)-\widehat{\bar L}(\sigma)) = \sigma^2g^{00}_b-i\sigma Q_b+R_b$, and $\sigma^2\rho^2$,
$\sigma\rho^3$, $\rho^4$ are $\rho_{\mathrm{scf}}^2\rho_{\mathrm{tf}}^4$ times $\rho_{\mathrm{zf}}^2$,
$\rho_{\mathrm{scf}}\rho_{\mathrm{zf}}$, $\rho_{\mathrm{scf}}^2$. The last statement is III.F Lemma 2.1 (1). $\square$

*The window and the states.* For $w<\ell_K^{\max}$ (III.G$''$ (1.1)) let $\mathcal W(w)$ be the set of roots $\mu$ of
$\widehat{L_b}(0)$ with $-w<\mu\le0$ (all real, III.G$'$ Lemma 1.3 (c)); they and their states are III.G$''$ Table 1.1.
For $\mu\in\mathcal W$ at a type $\tau$ (harmonics $\mathcal Y_\tau$) the tower
$(\breve h^{(\mu),j}_{b,\tau}(Y))_{j\le K_\mu}$ of Table 1.1 has Minkowski leading terms
$\breve{\bar h}^{(\mu),j}_\tau(Y) = \rho^{\mu-j}\phi^{(\mu,\tau)}_j(\omega; Y)$ (III.G$''$ section 2.2), and
$Y\mapsto\phi^{(\mu,\tau)}_0(Y)$ maps $\mathcal Y_\tau$ isomorphically onto the type-$\tau$ part of
$\ker\mathcal N(\mu)$ (III.G$''$ Lemma 1.2). For s1 and v1 at $\mu = -1$ we re-index, with
$\phi^{(-1,\mathrm s1)}_j := (\rho^{1+j}\breve{\bar h}^{j+2}_{\mathrm s1})|_{\partial X}$ and
$\phi^{(-1,\mathrm v1)}_j := (\rho^{1+j}\breve{\bar h}^{j+1}_{\mathrm v1})|_{\partial X}$, $j\ge0$; these chains then
satisfy III.G$''$ (2.4) as the generic ones do with $\mu = -1$ (III.G$''$ Lemma 2.2). Let
$$c_\mu := 2-\lfloor-\mu\rfloor,\qquad\{-\mu\} := -\mu-\lfloor-\mu\rfloor.\tag{1.4}$$
So $c_\mu = 2+\mu$ at the integer roots, and $c_\mu = 2,1,0$ at the class roots in $(-\frac14,0)$, $(-\frac54,-1)$,
$(-\frac94,-2)$; these are Table 1.1's $k_\mu$ (for s1 and v1, $c_{-1}+2 = 3$ and $c_{-1}+1 = 2$), so $c_\mu\le K_\mu$,
resp. $c_{-1}+2\le4$ and $c_{-1}+1\le3$. And $\lfloor-\mu\rfloor+c_\mu+1 = 3$. The fractional part $\{-\mu\}$ is 0 at
the integer roots. At a class root $\mu = 2-\lambda^\Upsilon_{\mathrm sl,l+j}$, $-\mu\in(l+j-2,l+j-\frac74)$ (III.F$'$
Proposition 2.3's bounds; $(0,\frac{z_\Upsilon}3]$ for $(l,l+j) = (0,2)$), so $\{-\mu\}\in(0,\frac14)$, and
$\{-\mu\}\ge\epsilon_{\mathrm{ind}}$ by III.F$'$ (2.2). (`tfgraft5.py` T3.)

## 2. Formal solutions at ztf ([Hin26] (9.57)-(9.61) and Definition 9.25 at n = 4)

**Definition 2.1.** For $\mu\in\mathcal W$, a type $\tau$ at which $\mu$ is a root, $Y\in\mathcal Y_\tau$ and
$k\le K_\mu$ (resp. $K-2$, $K-1$ for s1, v1),
$$\bar h^{(\mu),\le k}_\tau(\pm\hat r,Y) :
 = \sum_{j=0}^k(\mp i\hat r)^j\hat r^{-\mu}\phi^{(\mu,\tau)}_j(\omega;Y),\tag{2.1}$$
a function on tf with values in $\pi^*_{\mathrm{tf}}(S^2T^*X|_{\partial X})$, and
$H_{\mu,\tau}(Y) := \bar h^{(\mu),\le c_\mu}_\tau(\pm\hat r,Y)$. For s1 and v1 these are, in the source's indexing,
$\bar h^{\le3}_{\mathrm s1}(\pm\hat r,S) = \sum_{j=0}^1(\mp i\hat r)^j\hat r(\rho^{1+j}\breve{\bar h}^{2+j}_{\mathrm
s1}(S))|_{\partial X}$ and $\bar h^{\le2}_{\mathrm v1}(\pm\hat r,V) = \sum_{j=0}^1(\mp i\hat r)^j\hat
r(\rho^{1+j}\breve{\bar h}^{1+j}_{\mathrm v1}(V))|_{\partial X}$.

The source's (9.59) prints $\rho^{-\lambda-j}\bar h^{(\lambda),j}$; its companions have degree $\lambda-j$ (its (9.37)
and (9.57), where $\rho^j\breve{\bar h}^{(0),j}$ appears), so the restriction to $\partial X$ needs $\rho^{-\lambda+j}$.

**Lemma 2.2 ([Hin26] (9.57), (9.60) at n = 4).** (1) For $\sigma = \pm|\sigma|\ne0$ and $\hat r = |\sigma|r$,
$\sum_{j=0}^k(-i\sigma)^j\breve{\bar h}^{(\mu),j}_\tau(Y) = |\sigma|^\mu\bar h^{(\mu),\le k}_\tau(\pm\hat r,Y)$, with
the re-indexed chains for s1 and v1. (2) Exactly,
$$N_{\mathrm{tf}}\bar h^{(\mu),\le k}_\tau(\pm\hat r,Y) = (\mp i)^{k+1}\hat r^{k-1-\mu}\psi^{(\mu,\tau)}_k(\omega;Y),
\qquad\psi_k := -\big(\mu-k-\tfrac32-\bar S\big)\phi_k.\tag{2.2}$$
In particular $PH_{\mu,\tau}(Y) = (\mp i)^{c_\mu+1}\hat r^{3+\{-\mu\}}\psi_{c_\mu}$, as $c_\mu+1-\mu = 3+\{-\mu\}$.

*Proof.* (1) $(-i\sigma)^j\rho^{\mu-j} = (\mp i)^j|\sigma|^j\rho^{\mu-j} = (\mp i)^j|\sigma|^\mu\hat r^{j-\mu}$. (2) By
III.G$''$ Lemma 2.4 (a) with $a = e^{-i\sigma t_*}$, $\bar L(e^{-i\sigma t_*}\sum_{j\le k}(-i\sigma)^j\breve{\bar h}^j)
= (-i\sigma)^{k+1}e^{-i\sigma t_*}[\bar L,t_*]\breve{\bar h}^k$, and
$[\bar L,t_*] = -\rho(\rho\partial_\rho-\frac32- \bar S)$ (III.G$''$ (2.3)) gives
$[\bar L,t_*](\rho^{\mu-k}\phi_k) = \rho^{\mu-k+1}\psi_k$. So by (1) $\widehat{\bar L}(\sigma)(|\sigma|^\mu\bar h^{\le
k}) = (-i\sigma)^{k+1}\rho^{\mu-k+1}\psi_k = (\mp i)^{k+1}|\sigma|^{\mu+2}\hat r^{k-1-\mu}\psi_k$, and Lemma 1.1 (1)
divides by $|\sigma|^{\mu+2}$. For s1 and v1, III.G$''$ Lemma 2.4 (a) is stated with $a^{(k-1)}$ and $a^{(k)}$ in the
source's indexing, which is the same statement after the re-indexing. `tfgraft5.py` T1 (b) checks (2.2) for $k\le3$ on a
scalar model with $\mu$, $\bar S$ and a second root symbolic, and fails when the sign of $N_1$ is flipped. $\square$

(2.2) is an identity; the source's (9.60) records the membership in $\hat r^{-\lambda+k-1}C^\infty$. It is exact because
$\bar L$ is homogeneous and the chains are the Minkowski ones.

**Definition 2.3 ([Hin26] (9.61)).** $l_\beta(\hat r) := (\hat r^\beta-1)/\beta$ for $\beta\ne0$, and
$l_0(\hat r) := \log\hat r$.

**Lemma 2.4.** (1) $[\hat r\partial_{\hat r},l_\beta(\hat r)] = \hat r^\beta$. For a polynomial $p$ of degree $d$ with
coefficients in $\mathrm{Diff}(\mathbb S^3)$,
$[p(\hat r\partial_{\hat r}),l_\beta] = \hat r^\beta q_\beta(\hat r\partial_{\hat r})$, with $q_\beta$ of degree $d-1$
and coefficients polynomial in $\beta$. (2) For $C_0\in\mathbb R$ and $\chi\in C^\infty_c([0,1))$,
$\beta\mapsto\chi l_\beta$ is holomorphic on $\{\mathrm{Re}\,\beta>C_0\}$ with values in
$H^{\infty,c}_{\mathrm b}([0,1)_{\hat r})$ for every $c<\min(0,C_0)$, including at $\beta = 0$. (3) For $t>0$,
$l_\beta(\hat r)-l_\beta(t) = t^\beta l_\beta(\hat r/t)$. (4) $(\hat r^z-\hat r^m)/(z-m) = \hat r^ml_{z-m}(\hat r)$.

*Proof.* (1) $\hat r\partial_{\hat r}l_\beta = \hat r^\beta$ for every $\beta$. With $D := \hat r\partial_{\hat r}$,
$D(l_\beta g) = l_\beta Dg+\hat r^\beta g$ and $D(\hat r^\beta g) = \hat r^\beta(D+\beta)g$, so by induction
$D^m(l_\beta g) = l_\beta D^mg+\hat r^\beta\sum_{i<m}(D+\beta)^{m-1-i}D^ig$. (2)
$l_\beta(\hat r) = \log\hat r\int_0^1\hat r^{s\beta}ds$ is entire in $\beta$ for $\hat r>0$, and
$|\hat r^{s\beta}|\le\hat r^{\min(0,\mathrm{Re} \,\beta)}$ for $\hat r\le1$, $s\in[0,1]$. Differentiating under the
integral, $|\partial^p_\beta l_\beta|\le C_p|\log\hat r|^{p+1}\hat r^{\min(0,\mathrm{Re}\,\beta)}$, and for $m\ge1$,
$D^ml_\beta = \beta^{m-1}\hat r^\beta$, whose $\beta$-derivatives are bounded by
$C|\log\hat r|^p\hat r^{\mathrm{Re}\,\beta}(1+|\beta|)^m$. These bounds are locally uniform on
$\{\mathrm{Re}\,\beta>C_0\}$, and $\chi|\log\hat r|^N\hat r^{\min(0,C_0)} \in H^{0,c}_{\mathrm b}$ for $c<\min(0,C_0)$;
so difference quotients converge in $H^{\infty,c}_{\mathrm b}$ by dominated convergence. (3), (4) are algebra. $\square$

The coefficients $\pm\beta^{-1}$ of $\hat r^\beta$ and $\hat r^0$ in $l_\beta$ have a pole at $\beta = 0$, while
$l_\beta$ itself, as a conormal function, does not: this is the point of writing the expansions below with $l_\beta$.

## 3. The expansion at $\hat r = 0$ ([Hin26] Lemma 9.26 and Remarks 9.27-9.28 at n = 4)

*Hypotheses.* Let $\alpha_0\in\mathbb C$ and $\ell_{\mathrm{scf}},\ell_{\mathrm{zf}}\in\mathbb R$ with
$$\mathrm{Re}\,\alpha_0\in(1,2+\epsilon_{\mathrm{ind}}),\quad\ell_{\mathrm{scf}}<\tfrac32,\quad w_0 :=
\ell_{\mathrm{zf}}-\mathrm{Re}\,\alpha_0+2\in(-\epsilon_{\mathrm{ind}},\ell^{\max}_K),\quad\ell_{\mathrm{zf}}<3,\quad
w_0\ne-\mu\tag{3.1}$$
for every root $\mu$ of $\widehat{L_b}(0)$, with $\epsilon_{\mathrm{ind}}$ of III.F$'$ Proposition 2.3 (f). For $\alpha$
near $\alpha_0$ put $w(\alpha) := \ell_{\mathrm{zf}}-\mathrm{Re}\,\alpha+2$ and
$$\beta_\mu(\alpha) := 2-\alpha-\{-\mu\},\qquad z_j(\alpha) := 2-\alpha+j,\quad j\in\mathbb N_0,\tag{3.2}$$
so that $z_{\lfloor-\mu\rfloor}(\alpha)+\mu = \beta_\mu(\alpha)$.

*Holomorphic families.* For a disc $D$ around $\alpha_0$, a family
$a(\alpha)\in H^{\infty,((0,0),\ell)}_{\mathrm b}([0,1)_{\hat r}\times\mathbb S^3)$ is holomorphic if
$a = \sum_{j<\ell}\chi_{\mathrm{ztf}}\hat r^ja_j(\alpha)+a'(\alpha)$ with $a_j$ holomorphic in $C^\infty(\mathbb S^3)$
and $a'$ holomorphic in $H^{\infty,\ell}_{\mathrm b}$. Here and below the spaces on $[0,1)_{\hat r}\times\mathbb S^3$
impose their conditions near $\hat r = 0$ only: $u$ belongs if $u\in H^\infty_{\mathrm{loc}}$ on
$(0,1)\times\mathbb S^3$ and $\chi u$ belongs to the b-space for one, hence every, $\chi\in C^\infty_c([0,1))$ equal to
1 near 0; so functions smooth on $(0,1)$ and vanishing near 0 lie in all of them. Let $\mathfrak F_D$ be the space of
$\hat r^{2-\alpha}a(\alpha)$ with $a$ such a family for $\ell = \ell_{\mathrm{zf}}$.

**Theorem 3.1 ([Hin26] Lemma 9.26 at n = 4).** Assume (3.1). Let
$f_0\in H^{\infty,\ell_{\mathrm{scf}}+1,((0,0),\ell_{\mathrm{zf}})}_{\mathrm b}(\mathrm{tf})$ and, for $\alpha$ near
$\alpha_0$, $u_\alpha := N_{\mathrm{tf}}^{-1}(\rho_{\mathrm{ztf}}^{-\alpha}f_0)$ by III.F$'$ Corollary 3.4, with
$\beta_{\mathrm{sctf}} = \ell_{\mathrm{scf}}$ and $\beta_{\mathrm{ztf}}\in(-1,\min(0,2-\mathrm{Re}\,\alpha_0,w_0))$.
Then $u_\alpha$ does not depend on the choice of $\beta_{\mathrm{ztf}}$, is holomorphic in $\alpha$ with values in
$H^{\infty,\ell_{\mathrm{scf}}-\epsilon,\beta_{\mathrm{ztf}}}_{\mathrm b}(\mathrm{tf})$ for every $\epsilon>0$, and
$$u_\alpha = \chi_{\mathrm{ztf}}\big(u_{\alpha,0}+\hat r^{2-\alpha}u_{\alpha,1}\big)+(1-\chi_{\mathrm{ztf}})u_{\alpha,
\infty},\tag{3.3}$$
where $u_{\alpha,\infty}\in H^{\infty,\ell_{\mathrm{scf}}-\epsilon,0}_{\mathrm b}(\mathrm{tf})$ and
$u_{\alpha,1}\in H^{\infty,0,((0,0),\ell_{\mathrm{zf}})}_{\mathrm b}(\mathrm{tf})$ are holomorphic in $\alpha$ near
$\alpha_0$ (the latter in the sense above, its remainder at exactly $\ell_{\mathrm{zf}}$ for every $\alpha$), and
$$u_{\alpha,0} = \sum_{\mu\in\mathcal W(w_0)}\sum_\tau l_{\beta_\mu(\alpha)}(\hat r)\,H_{\mu,\tau}\big(Y^{(\mu)}_\tau
(\alpha)\big)\tag{3.4}$$
with $Y^{(\mu)}_\tau(\alpha)\in\mathcal Y_\tau$ holomorphic in $\alpha$. Written out, with the terms with $-\mu\ge w_0$
omitted, (3.4) is
$$\begin{aligned}u_{\alpha,0} ={}& l_{2-\alpha}(\hat r)\Big(\bar h^{\le3}_{\mathrm s1}(\pm\hat r,S^{(-1)}_1)+\bar
h^{\le2}_{\mathrm v1}(\pm\hat r,V^{(-1)}_1)+\bar h^{(0),\le2}_{\mathrm s0}(\pm\hat r,S^{(0)}_0)+\bar
h^{(0),\le2}_{\mathrm s2}(\pm\hat r,S^{(0)}_2)\\&+\bar h^{(-1),\le1}_{\mathrm s3}(\pm\hat r,S^{(-1)}_3)+\bar
h^{(-1),\le1}_{\mathrm v2}(\pm\hat r,V^{(-1)}_2)+\bar h^{(-2)}_{\mathrm s4}(\pm\hat r,S^{(-2)}_4)+\bar
h^{(-2)}_{\mathrm v3}(\pm\hat r,V^{(-2)}_3)\\&+\bar h^{(-2)}_{\mathrm s2,\mathrm{ph}}(\pm\hat r,S^{(-2)}_2)+\bar
h^{(-2)}_{\mathrm v2,\mathrm{ph}}(\pm\hat r,V^{(-2)}_2)+\bar h^{(-2)}_{\mathrm t2}(\pm\hat r,T^{(-2)}_2)\Big)\\&
+\sum_{(l,l+j)}l_{2-\alpha-\{\lambda^\Upsilon_{\mathrm sl,l+j}\}}(\hat r)\,\bar h^{(2-\lambda^\Upsilon_{\mathrm
sl,l+j}),\le c}_{\mathrm sl}(\pm\hat r,S_{l,l+j}),\end{aligned}\tag{3.5}$$
the last sum over $(l,l+j)\in\{(0,2),(1,2),(1,3),(2,3),(2,4),(3,4)\}$ with $c = 2,2,1,1,0,0$; "ph" marks the physical
states of III.F$''''$ Proposition 5.1, the other terms at $0,-1,-2$ the $\Box^\Upsilon$-states and the boosts and
rotations of Table 1.1.

The proof uses three lemmas, with $P = N_0+\hat rN_1$ of (1.3).

**Lemma 3.2.** $P$ maps $\mathfrak F_D$ into $\mathfrak F_D$.

*Proof.* $P(\hat r^za) = \hat r^zP_za$ with $P_z := \hat r^{-z}P\hat r^z$, a b-operator with smooth coefficients
polynomial in $z$, and b-operators with smooth coefficients preserve $H^{\infty,((0,0),\ell)}_{\mathrm b}$ with
holomorphic dependence (III.A (F1); the coefficient maps are polynomial in $z = 2-\alpha$). $\square$

**Lemma 3.3 (the formal terms).** Let $\mu\in\mathcal W(w_0)$, $\tau$ a type at which $\mu$ is a root and $Y(\alpha)$
holomorphic. Then $P\big(l_{\beta_\mu(\alpha)}H_{\mu,\tau}(Y(\alpha))\big)\in\mathfrak F_D$ for a small disc $D$.

*Proof.* $P(l_\beta H) = l_\beta PH+[P,l_\beta]H$. By Lemma 2.2 (2),
$l_\beta PH = (\mp i)^{c_\mu+1}l_\beta\hat r^{3+\{-\mu\}}\psi_{c_\mu}$, which by Lemma 2.4 (2) is holomorphic in
$H^{\infty,c}_{\mathrm b}$ for every
$c<3+\{-\mu\}+\min(0,\mathrm{Re}\,\beta_\mu) = \min(3+\{-\mu\},5-\mathrm{Re}\,\alpha)$. Both exceed $w(\alpha)$, as
$w(\alpha)<3$ and $5-\mathrm{Re}\,\alpha-w(\alpha) = 3-\ell_{\mathrm{zf}}>0$; so for $D$ small this term is
$\hat r^{2-\alpha}$ times a holomorphic family in $H^{\infty,\ell_{\mathrm{zf}}+\delta}_{\mathrm b}$, $\delta>0$. By
Lemma 2.4 (1), $[P,l_\beta] = \hat r^\beta Q_\beta$ with $Q_\beta$ a b-operator of order 1 polynomial in $\beta$, and
$H\in\hat r^{-\mu}C^\infty([0,1)\times\mathbb S^3)$ is a polynomial in $\hat r$; so
$[P,l_\beta]H\in\hat r^{\beta_\mu- \mu}C^\infty = \hat r^{2-\alpha+\lfloor-\mu\rfloor}C^\infty$, holomorphically, which
lies in $\mathfrak F_D$ as $\lfloor-\mu\rfloor\in\mathbb N_0$. $\square$

**Lemma 3.4 (one step).** Let $b\in(-1,w_0)$, with $b$ not the real part of a root $-\mu$ or of a $z_j(\alpha_0)$. Let
$R(\alpha)\in H^{\infty,b}_{\mathrm b}([0,1)\times\mathbb S^3)$ be holomorphic on a disc $D$, with $PR\in\mathfrak F_D$.
Let $\tilde b := \min(w_0,b+1)$, decreased slightly when $\tilde b<w_0$ so that it is not the real part of a root or of
a $z_j(\alpha_0)$. Then, after shrinking $D$,
$$R = \sum_{\mu:\ b<-\mu<\tilde b}\ \sum_\tau l_{\beta_\mu}H_{\mu,\tau}(Y_{\mu,\tau})+U+\tilde R,\tag{3.6}$$
with $Y_{\mu,\tau}(\alpha)$ holomorphic, $U\in\mathfrak F_D$, and $\tilde R$ holomorphic in
$H^{\infty,\tilde b}_{\mathrm b}$. If $\tilde b = w_0$, the remainder may be taken with $\hat r^{\alpha-2}\tilde R$
holomorphic in $H^{\infty,\ell_{\mathrm{zf}}}_{\mathrm b}$.

*Proof.* We use the Mellin transform $\mathcal M$ and the contour shift exactly as in the proof of III.A Lemma 1.4, with
its facts (M1)-(M2) on the Mellin transforms of b-Sobolev and polyhomogeneous functions and (E1)-(E2) on the inverse of
an elliptic indicial family ($P$ is elliptic, I.C section 4.1 (b)); all bounds there are locally uniform in the
holomorphic parameter $\alpha$. Fix $\chi\in C^\infty_c([0,1))$ equal to 1 near 0; then $(1-\chi)R$ vanishes near 0 and
is smooth, and $P(\chi R) = \chi PR+[P,\chi]R\in\mathfrak F_D$, so we may replace $R$ by $\chi R$, supported in $[0,1)$,
and put $(1-\chi)R$ into $\tilde R$ at the end. Write
$PR = \hat r^{2-\alpha}(\sum_{j<\ell_{\mathrm{zf}}}\chi_{\mathrm{ztf}}\hat r^ja_j+a')$. Since $\int\hat
r^{-\zeta}\chi_{\mathrm{ztf}}\frac{d\hat r}{\hat r} = \zeta^{-1}\int\hat r^{-\zeta}\chi'_{\mathrm{ztf}}d\hat r =
-\zeta^{-1}+(\text{entire})$,
$$\mathcal M(PR)(\lambda) = -\sum_j\frac{a_j(\alpha)}{\lambda-z_j(\alpha)}+G(\lambda),\tag{3.7}$$
with $G$ holomorphic in $\{\mathrm{Re}\,\lambda<w(\alpha)\}$ ($G$ collects the entire parts and
$\mathcal M(\hat r^{2-\alpha}a')(\lambda) = (\mathcal Ma')(\lambda+\alpha-2)$). From $N_0R = PR-\hat rN_1R$ and
$\mathcal M(\hat rN_1R)(\lambda) = N_1(\lambda-1)\mathcal MR(\lambda-1)$, with
$N_1(\lambda) = \pm i(-\lambda-\frac32- \bar S)$ and $\mathcal MR$ holomorphic in $\{\mathrm{Re}\,\lambda<b\}$ (M1),
$$\mathcal MR(\lambda) = N_0(\lambda)^{-1}\Phi(\lambda),\qquad\Phi(\lambda) := \mathcal M(PR)(\lambda)-N_1(\lambda-1)
\mathcal MR(\lambda-1),\tag{3.8}$$
continues $\mathcal MR$ meromorphically to $\{\mathrm{Re}\,\lambda<\tilde b\}$. In the strip
$\{b<\mathrm{Re}\,\lambda<\tilde b\}$, of width at most 1, the poles are at the roots $-\mu$ in it (Lemma 1.1 (2)) and
at the at most one $z_j(\alpha)$ in it, all simple; for $D$ small none is on the boundary lines. Moving the contour from
$\{\mathrm{Re}\,\lambda = b-\delta\}$ to $\{\mathrm{Re}\,\lambda = \tilde b\}$,
$$R = -\sum_p\mathrm{res}_{\lambda = p}\big(\hat r^\lambda\mathcal MR(\lambda)\big)+\tilde R,\qquad\tilde R :
 = \frac1{2\pi
i}\int_{\mathrm{Re}\,\lambda = \tilde b}\hat r^\lambda\mathcal MR(\lambda)\,d\lambda\in H^{\infty,\tilde b}_{\mathrm
b},\tag{3.9}$$
holomorphic in $\alpha$, as the integrand is and the bounds are locally uniform.

*The pairing.* If $z_j(\alpha_0) = -\mu$ for a root, then $2-\alpha_0 = -\mu-j\in(-\epsilon_{\mathrm{ind}},1)$; as
$\{-\mu\}$ is 0 or in $[\epsilon_{\mathrm{ind}},1-\epsilon_{\mathrm{ind}}]$, this forces $j = \lfloor-\mu\rfloor$ and
$\beta_\mu(\alpha_0) = 0$. So at most one root of the strip, $-\mu_*$, can meet the pole $z := z_{\lfloor-\mu_*\rfloor}$
as $\alpha$ varies, and the other roots and $z_j$ stay apart on $D$ small. (`tfgraft5.py` T2: for
$j\ne\lfloor-\mu \rfloor$, $|z_j(\alpha)+\mu|\ge\min(1-x,x+\epsilon_{\mathrm{ind}})$, $x = \mathrm{Re}(2-\alpha)$.)

*The residues.* (i) At a root $-\mu$ apart from the $z_j$: $-\mathrm{res} = -\hat r^{-\mu}\Pi_\mu\Phi(-\mu)$, a kernel
term $\hat r^{-\mu}\sum_\tau\phi^{(\mu,\tau)}_0(Y_\tau)$ with $Y_\tau(\alpha)$ holomorphic (Lemma 1.1 (2) and the
isomorphism $Y\mapsto\phi_0(Y)$). (ii) At a $z_j$ apart from the roots: $-\mathrm{res} = \hat r^{z_j}N_0(z_j)^{-1}a_j$,
of the form $\hat r^{2-\alpha+j}c(\alpha)$ with $c$ holomorphic in $C^\infty(\mathbb S^3)$ ($N_0(z_j)^{-1}$ is
invertible and elliptic for $\alpha\in D$). (iii) At the pair: near $-\mu_*$ write
$N_0(\lambda)^{-1} = \frac{\Pi}{\lambda+\mu_*}+\tilde I(\lambda)$ and
$\Phi(\lambda) = -\frac a{\lambda-z}+\tilde \Phi(\lambda)$, with $\tilde I$, $\tilde\Phi$ holomorphic and
$a = a_{\lfloor-\mu_*\rfloor}$. By partial fractions, $\frac{\Pi a}{(\lambda+\mu_*)(\lambda-z)} = \frac{\Pi
a}{z+\mu_*}\big(\frac1{\lambda-z}-\frac1{\lambda+\mu_*}\big)$, and the residues of $\hat r^\lambda N_0^{-1}\Phi$ at
$-\mu_*$ and $z$ sum to $-\Pi a\frac{\hat r^z-\hat r^{-\mu_*}}{z+\mu_*}+\hat r^{-\mu_*}\Pi\tilde\Phi(-\mu_*)-\hat
r^z\tilde I(z)a$. By Lemma 2.4 (4) and $z+\mu_* = \beta_{\mu_*}$, the contribution to $R$ is
$$\Pi a\,\hat r^{-\mu_*}l_{\beta_{\mu_*}}(\hat r)-\hat r^{-\mu_*}\Pi\tilde\Phi(-\mu_*)+\hat r^z\tilde I(z)a,\tag{3.10}$$
each term holomorphic in $\alpha\in D$, also where $\beta_{\mu_*} = 0$ ($z = -\mu_*$, a double pole, giving
$\log\hat r$). For $z\ne-\mu_*$ (3.10) is the sum of (i) and (ii), so it holds on all of $D$.

*Normal form.* A kernel term is converted by Lemma 2.4 (4) with $z = \beta_\mu-\mu$: $\hat r^{-\mu}\phi_0(Y) =
l_{\beta_\mu}\hat r^{-\mu}\phi_0(-\beta_\mu Y)+\hat r^{2-\alpha+\lfloor-\mu\rfloor}\phi_0(Y)$, the second term of the
form (ii). So $R = \sum_\mu l_{\beta_\mu}\hat r^{-\mu}\sum_\tau\phi_0(Y_{\mu,\tau})+U_0+\tilde R$ with $U_0$ a finite
sum of terms (ii) and $Y_{\mu,\tau}$ holomorphic. Now replace $\hat r^{-\mu}\phi_0$ by $H_{\mu,\tau}$:
$H_{\mu,\tau}-\hat r^{-\mu}\phi_0 = \sum_{1\le i\le c_\mu}(\mp i\hat r)^i\hat r^{-\mu}\phi_i$. If $\mu = \mu_*$,
$l_\beta\hat r^{i-\mu}$ lies in $H^{\infty,c}_{\mathrm b}$ for $c<\min(i-\mu,i+\mathrm{Re}\,z)$ (Lemma 2.4 (2)), and
$-\mu$, $\mathrm{Re}\,z>b$ give $c$ up to $b+1\ge\tilde b$ with room; otherwise $\beta_\mu$ stays away from 0 on $D$ and
$l_\beta\hat r^{i-\mu} = \beta^{-1}(\hat r^{2-\alpha+\lfloor-\mu\rfloor+i}-\hat r^{i-\mu})$, a term (ii) plus an element
of $H^{\infty,c}_{\mathrm b}$ with $c<i-\mu$, and $i-\mu>b+1\ge\tilde b$. This gives (3.6) on $(0,1)$, with $U$ the sum
of $U_0$ and these type-(ii) parts, in $\mathfrak F_D$.

*The last step.* If $\tilde b = w_0$, shift the contour instead to $\{\mathrm{Re}\,\lambda = w(\alpha)\}$, which depends
on $\alpha$: for $D$ small no root lies near it ($w_0\ne-\mu$), and the $z_j$ with $j<\ell_{\mathrm{zf}}$ have
$\mathrm{Re}\,z_j\le w(\alpha)-\delta_\ell$,
$\delta_\ell := \ell_{\mathrm{zf}}-\max\{j\in\mathbb N_0:j<\ell_{\mathrm{zf}}\}>0$. With $\lambda = \zeta+2-\alpha$,
$\hat r^{\alpha-2}\tilde R = \frac1{2\pi i}\int_{\mathrm{Re}\,\zeta = \ell_{\mathrm{zf}}}\hat r^\zeta\mathcal
MR(\zeta+2-\alpha)\,d\zeta$, an integral over a fixed line of an integrand holomorphic in $\alpha$, with values in
$H^{\infty,\ell_{\mathrm{zf}}}_{\mathrm b}$ by (M1). $\square$

*Proof of Theorem 3.1.* *Corollary 3.4's hypotheses.* At sctf, $\rho_{\mathrm{ztf}}\sim1$ and
$\rho_{\mathrm{ztf}}^{-\alpha}f_0$ has weight $\ell_{\mathrm{scf}}+1 = \beta_{\mathrm{sctf}}+1$. At ztf,
$f_0\in H^{\infty,c}_{\mathrm b}$ for $c<\min(0,\ell_{\mathrm{zf}})$, so $\rho_{\mathrm{ztf}}^{-\alpha}f_0$ has every
weight below $\min(-\mathrm{Re}\,\alpha,\ell_{\mathrm{zf}}-\mathrm{Re}\,\alpha)$, which exceeds $\beta_{\mathrm{ztf}}-2$
for $\alpha$ near $\alpha_0$; and $\beta_{\mathrm{ztf}}\in[-1,0)$. The map
$\alpha\mapsto\rho_{\mathrm{ztf}}^{-\alpha}f_0$ is holomorphic into that domain, so $u_\alpha$ is holomorphic. Two
choices of $\beta_{\mathrm{ztf}}$ give two solutions in the space with the smaller weight, on which $N_{\mathrm{tf}}$ is
injective (Corollary 3.4); so they agree. *Away from ztf.*
$(1-\chi_{\mathrm{ztf}})u_\alpha = (1-\chi_{\mathrm{ztf}})u_{\alpha,\infty}$ with $u_{\alpha,\infty} := \chi'u_\alpha$,
$\chi'$ equal to 1 on $\mathrm{supp}(1-\chi_{\mathrm{ztf}})$ and 0 near ztf; it is in
$H^{\infty,\ell_{\mathrm{scf}}-\epsilon,0}_{\mathrm b}$, holomorphically. *Near ztf.* Let $v := u_\alpha$ on
$(0,1)_{\hat r}$, in $H^{\infty,b_0}_{\mathrm b}([0,1)\times\mathbb S^3)$, $b_0 := \beta_{\mathrm{ztf}}$. Then $Pv =
\hat r^2\rho_{\mathrm{ztf}}^{-\alpha}f_0 = \hat r^{2-\alpha}(1+\hat r)^\alpha f_0\in\mathfrak F_D$. Put $R_0 := v$,
$T_0 := U_0 := 0$. Inductively, if $v = T_i+U_i+R_i$ with $T_i$ a sum of terms $l_{\beta_\mu}H_{\mu,\tau}(Y)$ over the
roots with $-\mu<b_i$, $U_i\in\mathfrak F_D$ and $R_i\in H^{\infty,b_i}_{\mathrm b}$, then $PR_i\in\mathfrak F_D$ by
Lemmas 3.2-3.3, and Lemma 3.4 (with $b_i$ decreased slightly if it is a forbidden real part,
$H^{\infty,b}_{\mathrm b}\subset H^{\infty,b-\delta}_{\mathrm b}$) gives the data at $b_{i+1} := \tilde b_i$. Each step
raises the weight by almost 1, so after at most five steps $b_i = w_0$, the last step taken as in Lemma 3.4's last
paragraph. As $b_0<0$ and no root has $-\mu\in[-1,0)$ (III.F$'$ Proposition 2.3 (a)), the roots met are exactly those
with $0\le-\mu<w_0$, that is $\mathcal W(w_0)$, each in one step. On
$\mathrm{supp}\,\chi_{\mathrm{ztf}}\subset\{\hat r<1\}$, $u_\alpha = v$; so (3.3) holds with
$u_{\alpha,0} := \sum l_{\beta_\mu}H_{\mu,\tau}(Y)$ and $u_{\alpha,1} := \hat r^{\alpha-2}(U+R)$ near ztf. (3.5) is
(3.4) written out over Table 1.1's rows with $c_\mu$ of (1.4); the multiplicities are one per type, as each root is
simple. $\square$

**Remark 3.5 ([Hin26] Remark 9.27 at n = 4).** (1) Expanding $l_\beta$, the coefficients of
$\hat r^{z_{\lfloor-\mu \rfloor}}$ and $\hat r^{-\mu}$ in $u_{\alpha,0}$ are $\pm\beta_\mu(\alpha)^{-1}\phi_0(Y)$:
meromorphic, with simple poles where $\beta_\mu(\alpha) = 0$, that is at $2-\alpha = 0$ (the integer roots) and at
$2-\alpha = \lambda^\Upsilon_{\mathrm sl,l+j}-(l+j)$ for the six class roots of (3.5). These are exactly the $\alpha$ at
which a source exponent $2-\alpha+j$ meets a root $-\mu$ of $N_0$ (the pairing in Lemma 3.4's proof), and there
$u_{\alpha,0}$ has $\log\hat r$ terms. (2) For other $\alpha$ one may replace $l_{\beta_\mu}H$ by $-\beta_\mu^{-1}H$,
the term $\beta_\mu^{-1}\hat r^{\beta_\mu}H = \beta_\mu^{-1}\hat r^{2-\alpha+\lfloor-\mu\rfloor}(\ldots)$ being absorbed
into $\hat r^{2-\alpha}u_{\alpha,1}$; this is not regular as $\beta_\mu\to0$. (3) $\chi_{\mathrm{ztf}}u_{\alpha,0}$ is
holomorphic in $\alpha$ with values in $H^{\infty,c}_{\mathrm b}$ near ztf for every
$c<\min(0,2-\mathrm{Re}\,\alpha_0)$: by Lemma 2.4 (2), $l_{\beta_\mu}H_{\mu,\tau}$ has every weight below
$-\mu+\min(0,\mathrm{Re}\,\beta_\mu) =
\min(-\mu,2-\mathrm{Re}\,\alpha+\lfloor-\mu\rfloor)\ge\min(0,2-\mathrm{Re}\,\alpha)$.

**Remark 3.6 ([Hin26] Remark 9.28 at n = 4).** For $\alpha_0 = 2$ the source $f_0$ may have a non-trivial smooth
expansion at $\hat r = 0$, unlike the right-hand sides of III.G$''$ Theorem 3.1, which have none at $R = 0$. Such $f_0$
arise as restrictions to tf of Fourier transforms of functions with good decay at $K^+$, which is high regularity, not
vanishing, at zf (III.A Proposition 4.2, the source's Proposition 2.25 at $n = 4$).

## 4. Grafting into the low-energy space ([Hin26] Definition 9.29, (9.72), Proposition 9.30, Remarks 9.31-9.34)

**Definition 4.1 ([Hin26] Definition 9.29 at n = 4).** For a generic row $(\mu,\tau)$ of $\mathcal W$,
$Y\in\mathcal Y_\tau$ and $k\le K_\mu$,
$h^{(\mu),\le k}_{b,\tau}(\sigma,Y) := \sum_{j=0}^k(-i\sigma)^j\breve h^{(\mu),j}_{b,\tau}(Y)$, $\breve h^{(\mu),0}_b$
being the state. For s1 and v1, in the source's indexing, $\breve h^{\le k}_{b,\mathrm s1}(\sigma,S) :=
\sum_{j=1}^k(-i\sigma)^{j-1}\breve h^j_{b,\mathrm s1}(S)$ (without $h_{b,\mathrm s1}$, as the source's (9.71)) and
$h^{\le k}_{b,\mathrm v1}(\sigma,V) := h_{b,\mathrm v1}(V)+\sum_{j=1}^k (-i\sigma)^j\breve h^j_{b,\mathrm v1}(V)$. These
are polynomials in $\sigma$ with smooth stationary coefficients.

**Lemma 4.2 ([Hin26] (9.72) at n = 4).** With the stationary tensors
$E_k := [L_b,t_*]\breve h^{(\mu),k}_b+\frac12[[L_b,t_*],t_*]\breve h^{(\mu),k-1}_b$ and
$E'_k := \frac12[[L_b,t_*],t_*]\breve h^{(\mu),k}_b$ ($\breve h^{(\mu),-1}_b := 0$),
$$\widehat{L_b}(\sigma)h^{(\mu),\le k}_{b,\tau}(\sigma,Y) = (-i\sigma)^{k+1}E_k(Y)+(-i\sigma)^{k+2}E'_k(Y),\tag{4.1}$$
and the same holds for $h_{b,\mathrm s1}(S)-i\sigma\breve h^{\le k}_{b,\mathrm s1}(\sigma,S)$ and for
$h^{\le k}_{b,\mathrm v1}(\sigma,V)$, with the towers of III.G$''$ Definition 2.5. So each lies in
$|\sigma|^{k+1}C^\infty(\pm[0,1)_\sigma\times X^\circ)$; for s1 with $k = 4$ this is the source's (9.72).

*Proof.* III.G$''$ Lemma 2.6: $L_bh^{\le k}_b(a)$ is given by III.G$''$ (2.2). Take $a = e^{-i\sigma t_*}$, so
$a^{(j)} = (-i\sigma)^je^{-i\sigma t_*}$, and use $L_b(e^{-i\sigma t_*}w) = e^{-i\sigma t_*}\widehat{L_b}(\sigma)w$ for
stationary $w$. For s1, $h^{\le k}_{b,\mathrm s1}(e^{-i\sigma t_*}S) = e^{-i\sigma t_*}(h_{b,\mathrm
s1}(S)-i\sigma\breve h^{\le k}_{b,\mathrm s1}(\sigma,S))$. $\square$

**Lemma 4.3 (restrictions to tf).** For a generic row let
$G_{\mu,\tau}(\sigma,Y) := |\sigma|^{-\mu}h^{(\mu),\le c_\mu}_{b,\tau}(\sigma,Y)$; for v1,
$G_{\mathrm v1}(\sigma,V) := |\sigma|i\sigma^{-1}h^{\le2}_{b,\mathrm v1}(\sigma,V)$; for s1,
$G_{\mathrm s1}(\sigma,S) := |\sigma|i\sigma^{-1}\breve h^{\le3}_{b,\mathrm s1}(\sigma,S)$ and
$G^{\mathrm{exc}}_{\mathrm s1}(\sigma,S) := -|\sigma|\sigma^{-2}h_{b,\mathrm s1}(S)$. Near tf each is polyhomogeneous,
with tf-index set $(0,0)\cup\mathcal E_{\mathrm{ind}}$, where $\mathcal E_{\mathrm{ind}}$ collects the index sets of the
states' corrections ($\min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}\ge\epsilon_{\mathrm{ind}}$, III.D$'''$'s convention)
and $(2,0)$, and $G|_{\mathrm{tf}} = H_{\mu,\tau}(Y)$, $\bar h^{\le2}_{\mathrm v1}(\pm\hat r,V)$,
$\bar h^{\le3}_{\mathrm s1}(\pm\hat r,S)$ respectively; $G^{\mathrm{exc}}_{\mathrm s1}$ vanishes at tf to order 2.

*Proof.* Write $\breve h^{(\mu),j}_b = \chi\breve{\bar h}^{(\mu),j}+e_j$ with
$e_j\in\mathcal A^{\mu-j+\mathcal E_{\mathrm{ind}}}$ (III.G$''$ section 2.2). By Lemma 2.2 (1),
$|\sigma|^{-\mu}(-i\sigma)^j\breve{\bar h}^{(\mu),j} = (\mp i\hat r)^j\hat r^{-\mu}\phi_j$, a function of
$(\hat r,\omega)$ alone, so smooth at tf. And $|\sigma|^{-\mu}(-i\sigma)^je_j$ is $\hat r^{j-\mu}$ times
$\rho^{-\mu+j}e_j$, polyhomogeneous with index set $\mathcal E_{\mathrm{ind}}$ in
$\rho = \rho_{\mathrm{scf}}\rho_{\mathrm{tf}}$, so it vanishes at tf. For v1,
$h_{b,\mathrm v1}\in\mathcal A^{(3,0)\cup\ldots}$ (III.D$'''$ (3.4)) gives $|\sigma|\sigma^{-1}\rho^3$, of tf-order 3,
and the terms $j\ge1$ give $|\sigma|i\sigma^{-1}(-i\sigma)^j\rho^{-j}\phi^{(-1,\mathrm v1)}_{j-1} = (\mp i\hat
r)^{j-1}\hat r\phi^{(-1,\mathrm v1)}_{j-1}$ (as $i(-i) = 1$), that is $\bar h^{\le2}_{\mathrm v1}$. For s1,
$\breve h^1_{b,\mathrm s1}\in\mathcal A^{(2,0)\cup\ldots}$ gives $|\sigma|\sigma^{-1}\rho^2$, of tf-order 2, and the
terms $j\ge2$ give $|\sigma|i\sigma^{-1}(-i\sigma)^{j-1}\rho^{1-j}\phi^{(-1,\mathrm s1)}_{j-2} = (\mp i\hat r)^{j-2}\hat
r\phi^{(-1,\mathrm s1)}_{j-2}$, that is $\bar h^{\le3}_{\mathrm s1}$; and $|\sigma|\sigma^{-2}h_{b,\mathrm
s1}\in|\sigma|^{-1}\rho^3\mathcal A^0 = \rho_{\mathrm{tf}}^2\rho_{\mathrm{zf}}^{-1} \rho_{\mathrm{scf}}^3\mathcal A^0$.
$\square$

*Hypotheses.* Let $\alpha_0\in\mathbb C$ with $\mathrm{Re}\,\alpha_0\in(1,2+\epsilon_{\mathrm{ind}})$,
$k\in\mathbb N_0$, $\ell_{\mathrm{scf}}<\frac32$, and
$$-\epsilon_{\mathrm{ind}}<\ell_{\mathrm{zf}}-\mathrm{Re}\,\alpha_0+2,\qquad\ell_{\mathrm{zf}}
-\min(\mathrm{Re}\,\alpha_0-
2,0)<\ell^{\max}_K,\qquad\ell_{\mathrm{zf}}-\mathrm{Re}\,\alpha_0+2\ne-\mu\tag{4.2}$$
for every root $\mu$. These imply (3.1): if $\mathrm{Re}\,\alpha_0\ge2$, $w_0\le\ell_{\mathrm{zf}}<\ell_K^{\max}\le3$;
if $\mathrm{Re}\,\alpha_0<2$, $w_0<\ell^{\max}_K$ and $\ell_{\mathrm{zf}}<\ell^{\max}_K+\mathrm{Re}\,\alpha_0-2<3$.

**Proposition 4.4 ([Hin26] Proposition 9.30 at n = 4).** Assume (4.2) and let $f\in
H^{\infty,\ell_{\mathrm{scf}}+1,(\alpha_0,k),((0,0),\ell_{\mathrm{zf}})}_{\mathrm b}(X^\pm_{\mathrm{sc}\text- \mathrm
b};S^2T^*X)$.

(1) There is $u\in\bigcap_{\epsilon>0}H^{\infty,\ell_{\mathrm{scf}}-\epsilon,\alpha_0-2-\epsilon,\min(-1,\alpha_0-3)-
\epsilon}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$, smooth in the Myers-Perry parameters $b$ near $b_0$, with
$$f-\widehat{L_b}(\sigma)u\in H^{\infty,\ell_{\mathrm{scf}}+1,(\alpha_0,k)+\mathcal E_{\mathrm{ind}},((0,0),
\ell_{\mathrm{zf}})}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b}),\tag{4.3}$$
where $\mathcal E_{\mathrm{ind}}$, an index set with
$\min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}\ge\epsilon_{\mathrm{ind}}$ not depending on $b$, $\alpha_0$, $k$, is that of
Lemma 4.3 together with $(1,0)$.

(2) For $k = 0$ one can take $u = \chi_{\mathrm{zf}}|\sigma|^{\alpha_0-2}u_b+\chi_{\mathrm{tf}}\rho_{\mathrm{tf}}^{
\alpha_0-2}u_{\mathrm{tf}}$ with $u_{\mathrm{tf}}\in H^{\infty,\ell_{\mathrm{scf}}-\epsilon,((0,0),\ell_{\mathrm{zf}}
)}_{\mathrm b}(\mathrm{tf})$ and
$$u_b = l_{2-\alpha_0}(|\sigma|)G^{\mathrm{exc}}_{\mathrm s1}(\sigma,S^{(-1)}_1)+l_{2-\alpha_0}(\hat r)\big(G_{\mathrm
s1}(\sigma,S^{(-1)}_1)+G_{\mathrm v1}(\sigma,V^{(-1)}_1)\big)+{\sum_{\mu,\tau}}'\,l_{\beta_\mu(\alpha_0)}(\hat r)G_{\mu,
\tau}(\sigma,Y^{(\mu)}_\tau),\tag{4.4}$$
the primed sum over the other rows of $\mathcal W(w_0)$, as in (3.5); that is, with the source's notation,
$-l_{2-\alpha_0}(|\sigma|)|\sigma|\sigma^{-2}h_{b,\mathrm s1}(S)+l_{2-\alpha_0}(\hat r)|\sigma|i\sigma^{-1}(\breve
h^{\le3}_{b,\mathrm s1}(\sigma,S)+h^{\le2}_{b,\mathrm v1}(\sigma,V))+\ldots$, and
$l_{\beta_\mu}(\hat r)|\sigma|^{-\mu}h^{(\mu),\le c_\mu}_{b,\tau}(\sigma,Y)$ for the others. For general $k$, $u$ is a
sum of terms of this form and of up to $k$-fold derivatives of such terms in $\alpha_0$.

*Proof.* It suffices to solve away one term
$\chi_{\mathrm{tf}}\rho_{\mathrm{tf}}^{\alpha_0}(\log\rho_{\mathrm{tf}}) ^kf_0(\hat r,\omega)$,
$f_0\in H^{\infty,\ell_{\mathrm{scf}}+1,((0,0),\ell_{\mathrm{zf}})}_{\mathrm b}(\mathrm{tf})$, of the expansion of $f$
at tf: $f$ is a sum of $k+1$ such terms (with coefficients in that space, the restrictions to tf of the coefficients of
its partial expansion) and a remainder of tf-index set $(\alpha_0+1,k)\subset(\alpha_0,k)+ \mathcal E_{\mathrm{ind}}$,
as $(1,0)\in\mathcal E_{\mathrm{ind}}$; and terms with lower log powers are treated the same way.

*Step 1: no logarithms.* For $\alpha$ near $\alpha_0$ let
$u_{\mathrm{tf},\alpha} := N_{\mathrm{tf}}^{-1} (\rho_{\mathrm{ztf}}^{-\alpha}f_0)$, written as (3.3) by Theorem 3.1
(with $\chi_{\mathrm{ztf}} = \chi_{\mathrm{zf}} |_{\mathrm{tf}}$), and let $u_{b,\alpha}$ be (4.4) with $\alpha$ for
$\alpha_0$ and Theorem 3.1's coefficients. Put
$$u_\alpha := |\sigma|^{\alpha-2}W_\alpha,\qquad W_\alpha := \chi_{\mathrm{zf}}u_{b,\alpha}+\chi_{\mathrm{tf}}
\big(\chi_{\mathrm{zf}}\hat r^{2-\alpha}u_{\alpha,1}+(1-\chi_{\mathrm{zf}})u_{\alpha,\infty}\big).\tag{4.5}$$
The functions $l_\beta(\hat r)$, $l_\beta(|\sigma|)$ and $|\sigma|^{\alpha-2}$ are holomorphic in $\alpha$ with values
in the conormal spaces of Lemma 2.4 (2), and the states do not depend on $\alpha$; so $u_\alpha$ is holomorphic in
$\alpha$ with values in
$H^{\infty,\ell_{\mathrm{scf}}-\epsilon,\mathrm{Re}\,\alpha_0-2-\epsilon,\min(-1,\mathrm{Re}\,\alpha_0
-3)-\epsilon}_{\mathrm b}$ (the zf-weight from $l_{2-\alpha}(|\sigma|)|\sigma|^{\alpha-3}h_{b,\mathrm s1}$, of order
$\mathrm{Re}\,\alpha-3+\min(0,2-\mathrm{Re}\,\alpha)$; every other term is better, as
$\mathrm{Re}\,\alpha-2-\mu+\min(0, \mathrm{Re}\,\beta_\mu)\ge\min(\mathrm{Re}\,\alpha-2,0)$).

*Step 1.1: the restriction.* $W_\alpha$ is polyhomogeneous at tf with index set $(0,0)\cup\mathcal E_{\mathrm{ind}}$,
and $W_\alpha|_{\mathrm{tf}} = u_{\mathrm{tf},\alpha}$. Indeed
$\chi_{\mathrm{zf}}|_{\mathrm{tf}} = \chi_{\mathrm{ztf}}$, $\chi_{\mathrm{tf}} = 1$ near tf, the functions of
$(\hat r,\omega)$ are smooth at tf, and by Lemma 4.3
$(\chi_{\mathrm{zf}}u_{b,\alpha})|_{\mathrm{tf}} = \chi_{\mathrm{ztf}}u_{\alpha,0}$: the term
$l_{2-\alpha}(|\sigma|)G^{\mathrm{exc}}_{\mathrm s1}$ vanishes at tf, to order
$2+\min(0,2-\mathrm{Re}\,\alpha)-\epsilon>1$.

*Step 1.2: the error.* Let $F_\alpha := \chi_{\mathrm{tf}}\rho_{\mathrm{tf}}^\alpha f_0-\widehat{L_b}(\sigma)u_\alpha$.
We show $F_\alpha\in H^{\infty,\ell_{\mathrm{scf}}+1,\alpha+\mathcal
E_{\mathrm{ind}},((0,0),\ell_{\mathrm{zf}})}_{\mathrm b}$, holomorphically in $\alpha$ as an element of
$H^{\infty,\ell_{\mathrm{scf}}+1,\mathrm{Re}\,\alpha_0+
\epsilon_{\mathrm{ind}}-\epsilon,((0,0),\ell_{\mathrm{zf}})}_{\mathrm b}$.

(i) *tf.* As $\widehat{L_b}(\sigma)$ has no $\sigma$-derivatives,
$\widehat{L_b}(\sigma)u_\alpha = |\sigma|^{\alpha-2}\widehat{L_b}(\sigma)W_\alpha$. View $u_{\mathrm{tf},\alpha}$ as a
function of $(\hat r,\omega)$ near tf. By Lemma 1.1 (1), $|\sigma|^{\alpha-2}\widehat{\bar
L}(\sigma)u_{\mathrm{tf},\alpha} = |\sigma|^\alpha N_{\mathrm{tf}}u_{\mathrm{tf},\alpha}
= |\sigma|^\alpha\rho_{\mathrm{ztf}}^{-\alpha}f_0 = \rho_{\mathrm{tf}}^\alpha f_0$, since
$\rho_{\mathrm{zf}} = \rho_{\mathrm{ztf}}$ as functions of $\hat r$ and
$|\sigma| = \rho_{\mathrm{tf}} \rho_{\mathrm{zf}}$. So near tf,
$$F_\alpha = -|\sigma|^{\alpha-2}\widehat{\bar L}(\sigma)(W_\alpha-u_{\mathrm{tf},\alpha})-|\sigma|^{\alpha-2}
\big(\widehat{L_b}(\sigma)-\widehat{\bar L}(\sigma)\big)W_\alpha.$$
By Lemma 1.2 and Step 1.1, the first term has tf-index set $\alpha-2+2+\mathcal E_{\mathrm{ind}}$ (b-operators preserve
index sets, III.A (F1)) and the second
$\alpha+2+((0,0)\cup\mathcal E_{\mathrm{ind}})\subset\alpha+\mathcal E_{\mathrm{ind}}$, as
$(2,0)\in\mathcal E_{\mathrm{ind}}$. Away from tf there is nothing to show at tf.

(ii) *scf.* Near scf, $\chi_{\mathrm{zf}} = 0$ and $W_\alpha = \chi_{\mathrm{tf}}u_{\alpha,\infty}$, with sctf-weight
$\ell_{\mathrm{scf}}-\epsilon$; near sctf, $u_{\mathrm{tf},\alpha} = u_{\alpha,\infty}$. Where $\chi_{\mathrm{tf}} = 1$,
(i) gives $F_\alpha = -|\sigma|^{\alpha-2}(\widehat{L_b}-\widehat{\bar L})u_{\alpha,\infty}$, of scf-order
$\ell_{\mathrm{scf}}+2-\epsilon$ by Lemma 1.2. Elsewhere add
$-|\sigma|^{\alpha-2}[\widehat{L_b}(\sigma), \chi_{\mathrm{tf}}]u_{\alpha,\infty}$:
$\rho\partial_\rho\chi_2(\rho+|\sigma|) = \rho\chi_2'$ carries $\rho = \rho_{\mathrm{scf}}\rho_{\mathrm{tf}}$, so the
commutator lies in $\rho_{\mathrm{scf}}^2\rho_{\mathrm{tf}}^3 \mathrm{Diff}^1_{\mathrm b}$, and this term too has
scf-order $\ell_{\mathrm{scf}}+2-\epsilon\ge\ell_{\mathrm{scf}}+1$.

(iii) *zf.* We read the zf-index sets at zf$^\circ$, where $|\sigma|$ defines zf and $x$ ranges over compact sets of
$X^\circ$. Near tf $\cap$ zf every term of $F_\alpha$ is a finite sum of products of jointly polyhomogeneous factors
(powers of $|\sigma|$, $\rho$, $\hat r$, the functions $l_\beta(\hat r)$, $l_\beta(|\sigma|)$, and the states'
expansions at $\rho = 0$) and of the remainder $\hat r^{2-\alpha}u_{\alpha,1}$ with its own zf-structure; for such a
product the zf-exponents do not depend on the point of zf, so they are those read at zf$^\circ$. There
$\chi_{\mathrm{zf}} = 1$, and $F_\alpha$ is $\chi_{\mathrm{tf}}\rho_{\mathrm{tf}}^\alpha f_0$ (whose zf-structure is
$f_0$'s at ztf, as $\hat r = |\sigma|r$) minus the following. (a) $\widehat{L_b}(\sigma)(|\sigma|^{\alpha-2}
\chi_{\mathrm{tf}}\hat r^{2-\alpha}u_{\alpha,1}) =
\widehat{L_b}(\sigma)(\rho^{\alpha-2}\chi_{\mathrm{tf}}u_{\alpha,1}( |\sigma|r,\omega))$, of zf-class
$((0,0),\ell_{\mathrm{zf}})$, as $\widehat{L_b}(\sigma)$ is a differential operator in
$x$ polynomial in $\sigma$. (b) A generic term: $\widehat{L_b}(\sigma)(|\sigma|^{\alpha-2-\mu}l_\beta(\hat r)h^{\le
c_\mu}_b) = |\sigma|^{\alpha-2-\mu}(l_\beta\widehat{L_b}(\sigma)h^{\le c_\mu}_b+[\widehat{L_b}(\sigma),l_\beta] h^{\le
c_\mu}_b)$. As $l_\beta(|\sigma|r)\in\mathcal A^{\min(0,\mathrm{Re}\,\beta)-\epsilon}$ in $|\sigma|$ and Lemma 4.2 gives
$|\sigma|^{c_\mu+1}$, the first part has zf-order $\mathrm{Re}\,\alpha-2-\mu+\min(0,\mathrm{Re}\,
\beta_\mu)+c_\mu+1-\epsilon = \min(\mathrm{Re}\,\alpha+1+\{-\mu\},3)-\epsilon>\ell_{\mathrm{zf}}$, by (4.2) and $\alpha$
near $\alpha_0$. For the second, $\partial_x(l_\beta(|\sigma|r)) = (|\sigma|r)^\beta\partial_x\log r$ (the source's
(9.82)), so $[\widehat{L_b}(\sigma),l_\beta(\hat r)] = \hat r^\beta D_\beta(\sigma)$ with $D_\beta(\sigma)$ a
first-order operator on $X^\circ$ with coefficients smooth in $x$ ($r$ is bounded below on $X$), polynomial in $\sigma$
and $\beta$; and $|\sigma|^{\alpha-2-\mu}\hat r^{\beta_\mu} = |\sigma|^{\lfloor-\mu\rfloor}r^{\beta_\mu}$, so this part
is smooth in $\sigma$ at $\sigma = 0$, of zf-class $(0,0)$. (c) The s1 terms, the source's (9.83): with
$\beta := 2- \alpha$,
$$\begin{aligned}&|\sigma|^{\alpha-2}\widehat{L_b}(\sigma)\big(-l_\beta(|\sigma|)|\sigma|\sigma^{-2}h_{b,\mathrm s1}
+l_\beta(\hat r)|\sigma|i\sigma^{-1}\breve h^{\le3}_{b,\mathrm s1}\big) = -|\sigma|^{\alpha-2}l_\beta(|\sigma|)|\sigma|
\sigma^{-2}\widehat{L_b}(\sigma)\big(h_{b,\mathrm s1}-i\sigma\breve h^{\le3}_{b,\mathrm s1}\big)\\&\quad+|\sigma|^{
\alpha-2}\big(l_\beta(\hat r)-l_\beta(|\sigma|)\big)|\sigma|i\sigma^{-1}\widehat{L_b}(\sigma)\breve h^{\le3}_{b,\mathrm
s1}+|\sigma|^{\alpha-2}[\widehat{L_b}(\sigma),l_\beta(\hat r)]|\sigma|i\sigma^{-1}\breve h^{\le3}_{b,\mathrm
s1}.\end{aligned}$$
By Lemma 4.2 the first line has zf-order $\mathrm{Re}\,\alpha-2+\min(0,\mathrm{Re}\,\beta)+1-2+4-\epsilon = \min(
\mathrm{Re}\,\alpha+1,3)-\epsilon>\ell_{\mathrm{zf}}$. By Lemma 2.4 (3),
$l_\beta(\hat r)-l_\beta(|\sigma|) = |\sigma|^\beta l_\beta(r)$, so the second term is
$\pm i\,l_\beta(r)\widehat{L_b}(\sigma)\breve h^{\le3}_{b,\mathrm s1}$, smooth in $\sigma$; and the third is
$\pm ir^\beta D_\beta(\sigma)\breve h^{\le3}_{b,\mathrm s1}$, smooth in $\sigma$. (d) The v1 term likewise: Lemma 4.2
gives zf-order $\mathrm{Re}\,\alpha-2+\min(0,\mathrm{Re}\,\beta)+3-\epsilon = \min( \mathrm{Re}\,\alpha+1,3)-\epsilon$,
and its commutator part is smooth in $\sigma$. (e) The commutators with the cut-offs: $\chi_{\mathrm{zf}} = 1$ near
zf$^\circ$; $[\widehat{L_b}(\sigma),\chi_{\mathrm{tf}}]$ acts only on the term of (a) ($\chi_{\mathrm{tf}}$ does not
multiply $u_{b,\alpha}$ in (4.5)), with the same conclusion. So $F_\alpha$ has zf-class $((0,0),\ell_{\mathrm{zf}})$.
Holomorphy in $\alpha$ holds term by term.

*Step 2: logarithms.* The term is $\partial_\alpha^k(\chi_{\mathrm{tf}}\rho_{\mathrm{tf}}^\alpha f_0)|_{\alpha_0}$. Let
$u := \partial^k_\alpha u_\alpha|_{\alpha_0}$. By the holomorphy in Step 1.2,
$\chi_{\mathrm{tf}}\rho_{\mathrm{tf}}^{\alpha_0}(\log\rho_{\mathrm{tf}})^kf_0-\widehat{L_b}(\sigma)u = \partial^k_\alpha
F_\alpha|_{\alpha_0}$ lies in $H^{\infty,\ell_{\mathrm{scf}}+1,\mathrm{Re}\,\alpha_0+\epsilon_{\mathrm{ind}}-\epsilon,
((0,0),\ell_{\mathrm{zf}})}_{\mathrm b}$, and differentiating (4.5) term by term shows that it is polyhomogeneous at tf
with index set $(\alpha_0,k)+\mathcal E_{\mathrm{ind}}$. The membership of $u$ is that of $u_\alpha$, with logarithmic
factors absorbed by $\epsilon$. *Parameters.* $N_{\mathrm{tf}}$ does not depend on $b$, the states depend smoothly on
$b$ (III.D$''$, III.D$'''$, III.F$''''$), and so does $u$. $\square$

**Remark 4.5 ([Hin26] Remarks 9.31-9.33 at n = 4).** (1) $u$ solves $f$ away to leading order at tf without creating
zf-error terms worse than those of $f$. For $\mathrm{Re}\,\alpha_0\le2$ the restriction of $f$ to zf ($k = 0$) is of
class $\mathcal A^{\alpha_0}(X)$, and the source notes that this weight lies outside the range where the zero energy
operator (or an augmentation of it) is inverted, which is why the tf-model is inverted instead; the $n = 4$ range is
that of Part III.F's counterpart of the source's Corollary 8.13 and is not restated here. (2) The weaker the tf-order of
$f$, the more singular $u$ at zf: the dominant term is $l_{2-\alpha_0}(|\sigma|)G^{\mathrm{exc}}_{\mathrm s1}$, of order
$\min(-1,\alpha_0-3)$. The time-translation term contributes $|\sigma|^{\alpha_0-2}h^{(0),\le2}_{b,\mathrm s0}$ and, for
$\alpha_0\ne2$, a smooth term $h^{(0),\le2}_{b,\mathrm s0}$; as $\alpha_0\to2$ they combine into
$(\log|\sigma|)h^{(0),\le2}_{b,\mathrm s0}$, and likewise $|\sigma|^2h^{(-2)}_{b,\mathrm s2,\mathrm{ph}}$. The mechanism
is the indicial root 0 of the tf-model, as for the flat Laplacian, in any dimension. (3) A tf-order $\alpha_0$
corresponds to an $\iota^+$-order $\alpha_0+1$ (III.A Proposition 4.2), and the term
$t_*^{-\alpha_0+1}h^{(0)}_{b,\mathrm s0}$ of III.G$''$ Theorem 4.2 is, on the Fourier side, essentially
$|\sigma|^{\alpha_0-2}h^{(0)}_{b,\mathrm s0}$.

**Remark 4.6 ([Hin26] Remark 9.34 at n = 4).** Had $l_{2-\alpha_0}(\hat r)$ been used for the $h_{b,\mathrm s1}$-term,
the s1 computation would gain $-|\sigma|^{\alpha_0-2}[\widehat{L_b}(\sigma),l_{2-\alpha_0}(\hat r)]|\sigma|\sigma^{-2}
h_{b,\mathrm s1} = -|\sigma|^{-1}r^{2-\alpha_0}D_{2-\alpha_0}(\sigma)h_{b,\mathrm s1}$ (Step 1.2 (b)), of class
$|\sigma|^{-1}C^\infty$, singular at $\sigma = 0$.

## 5. Conormal sources at tf ([Hin26] Proposition 9.35 at n = 4)

**Proposition 5.1 ([Hin26] Proposition 9.35 at n = 4).** Let $\alpha\in(1,2)$, $\ell_{\mathrm{scf}}<\frac32$, and
$-\epsilon_{\mathrm{ind}}<w := \ell_{\mathrm{zf}}-\alpha+2<\ell^{\max}_K$, with $2-\alpha+j\ne-\mu$ and $w\ne-\mu$ for
all $j\in\mathbb N_0$ and all roots $\mu$ of $\widehat{L_b}(0)$. Let $k_0\in\mathbb N_0$ and $f\in
H^{\infty,\ell_{\mathrm{scf}}+1,\alpha,((k_0,0),\ell_{\mathrm{zf}})}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b};
S^2T^*X)$. Then there is $u\in\bigcap_{\epsilon>0}H^{\infty,\ell_{\mathrm{scf}}-\epsilon,\alpha-2,\alpha-3}_{\mathrm
b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$ with
$$f-\widehat{L_b}(\sigma)u\in\bigcap_{\epsilon>0}H^{\infty,\ell_{\mathrm{scf}}+1,\alpha+\epsilon_{\mathrm{ind}}-\epsilon,
((k_0,0),\ell_{\mathrm{zf}})}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b}).\tag{5.1}$$
One can take $u = \chi_{\mathrm{zf}}u_b+\chi_{\mathrm{tf}}\tilde u$, with $\tilde u\in H^{\infty,\ell_{\mathrm{scf}}-
\epsilon,\alpha-2,((k_0,0),\ell_{\mathrm{zf}})}_{\mathrm b}$ and
$$u_b = h^{\le3}_{b,\mathrm s1}\big(\sigma,|\sigma|^{\alpha-3}S^{(-1)}_1(\sigma)\big)+h^{\le2}_{b,\mathrm
v1}\big(\sigma, |\sigma|^{\alpha-2}V^{(-1)}_1(\sigma)\big)+{\sum_{\mu,\tau}}'\,h^{(\mu),\le
c_\mu}_{b,\tau}\big(\sigma,|\sigma|^{\alpha-2
-\mu}Y^{(\mu)}_\tau(\sigma)\big),\tag{5.2}$$
where $h^{\le3}_{b,\mathrm s1}(\sigma,S) := h_{b,\mathrm s1}(S)-i\sigma\breve h^{\le3}_{b,\mathrm s1}(\sigma,S)$ and the
coefficients lie in $H^{\infty,0}_{\mathrm b}(\pm[0,1)_\sigma,|\frac{d\sigma}\sigma|;\mathcal Y_\tau)$. As $\alpha<2$,
$\ell_{\mathrm{zf}} = w+\alpha-2<3$. The point is that (5.1) vanishes to higher order at tf than $f$.

*Proof.* Replacing $f$ by $\chi_{\mathrm{tf}}f$ costs $(1-\chi_{\mathrm{tf}})f$, which is supported away from tf and has
zf-class $((k_0,0),\ell_{\mathrm{zf}})$, so it is of the form (5.1).

*Step 1: the zf-expansion near the corner.* Near tf $\cap$ zf, in $(\rho,\hat r,\omega)$, the partial expansion of $f$
at zf reads $f = \sum_{k_0\le j<\ell_{\mathrm{zf}}}|\sigma|^j\rho^{\alpha-j}f^{(j)}(\rho,\omega)+f'$ with
$f^{(j)}\in H^{\infty,0}_{\mathrm b}([0,\rho_0)_\rho\times\mathbb S^3)$ and $f'$ of zf-weight $\ell_{\mathrm{zf}}$: the
coefficients are functions on zf $\cong\bar X$, and $|\sigma|^j\rho^{\alpha-j} = \rho_{\mathrm{tf}}^\alpha
\rho_{\mathrm{zf}}^j\rho_{\mathrm{scf}}^{\alpha-j}$ carries $f$'s tf-weight. Each term is $|\sigma|^j$ times a
stationary function. For $j = k_0,k_0+1,\ldots,\lfloor\ell_{\mathrm{zf}}\rfloor$ in turn, let $v_j$ solve
$$\mathcal Nv_j = \rho^{\alpha-2-j}\chi_3(\rho)f^{(j)}\quad\text{on }(0,\infty)_\rho\times\mathbb S^3,\qquad v_j\in
H^{\infty,\alpha-2-j}_{\mathrm b},\tag{5.3}$$
($\chi_3\in C^\infty_c([0,\rho_0))$ equal to 1 near $\mathrm{supp}\,\chi_{\mathrm{tf}}$): $\mathcal N$ is elliptic and
dilation invariant, and $\alpha-2-j$ is not the real part of a root ($2-\alpha+j\ne-\mu$, the roots being real), so its
Mellin family is invertible on that line, with the bounds (E1), and (5.3) is solved by Mellin inversion on
$\{\mathrm{Re}\,\lambda = \alpha-2-j\}$ (Plancherel). Then $U_j := \chi_{\mathrm{zf}}\chi_{\mathrm{tf}}|\sigma|^jv_j$
satisfies, by (1.2) and Lemma 1.2, $\widehat{L_b}(\sigma)U_j = |\sigma|^j\rho^{\alpha-j}f^{(j)}+e_j$ on
$\mathrm{supp}\,\chi_{\mathrm{tf}}$ (where $\chi_3 = 1$), where $e_j$ consists of three kinds of terms. First,
$\chi_{\mathrm{zf}}\chi_{\mathrm{tf}}|\sigma|^{j+1}\rho^{\alpha-j-1}g_{j+1}$ with $g_{j+1} := \pm
i\rho^{j+1-\alpha}\rho(\rho\partial_\rho-\frac32-\bar S)v_j\in H^{\infty,0}_{\mathrm b}$, from the $i\sigma\rho$-term of
(1.2): a term of the same form at $j+1$. Second, terms of tf-order $\alpha+2$, from
$\widehat{L_b}(\sigma)- \widehat{\bar L}(\sigma)$ (Lemma 1.2), of zf-class $(k_0,0)$. Third, commutators with
$\chi_{\mathrm{zf}}\chi_{\mathrm{tf}}$; those with $\chi_{\mathrm{tf}}$ are supported away from tf and have zf-class
$(k_0,0)$, and those with $\chi_{\mathrm{zf}} = \chi_1(\hat r)$ are supported in $\{\frac18\le\hat r\le\frac14\}$, away
from zf and scf. Subtracting $g_{j+1}$ from $f^{(j+1)}$ (or setting $f^{(j+1)} := -g_{j+1}$ when
$j+1\ge\ell_{\mathrm{zf}}$) and proceeding, we obtain
$u_0 := \sum_jU_j\in H^{\infty,\infty,\alpha-2,(k_0,0)}_{\mathrm b}$ with
$$\chi_{\mathrm{tf}}f-\widehat{L_b}(\sigma)u_0 = f_1+f_2,\qquad f_1\in H^{\infty,\ell_{\mathrm{scf}}+1,\alpha,
\ell_{\mathrm{zf}}}_{\mathrm b},\tag{5.4}$$
with $f_2$ the sum of an element of $H^{\infty,\ell_{\mathrm{scf}}+1,\alpha+2,((k_0,0),\ell_{\mathrm{zf}})}_{\mathrm b}$
and of terms supported away from tf of zf-class $((k_0,0),\ell_{\mathrm{zf}})$, so of the form (5.1); $f_1$ collects
$f'$, the commutators with $\chi_{\mathrm{zf}}$, and the term of form $\lfloor\ell_{\mathrm{zf}}\rfloor+1$, of zf-order
$>\ell_{\mathrm{zf}}$. Here the source takes instead
$u^{(0)}_0(\rho,\cdot) := \tilde L(0)(\omega,\alpha-2,\partial_\omega)^{-1}f^{(0)}_0(\rho,\cdot)$ pointwise in $\rho$
and asserts that the terms in which $\hat r\partial_{\hat r}$ falls on $u^{(0)}_0(|\sigma|/\hat r,\omega)$ carry a
factor $\rho$. They carry $\rho\partial_\rho u^{(0)}_0$, which for a conormal $f^{(0)}_0$ is of the size of $u^{(0)}_0$:
for $f^{(0)}_0 = \rho^{i\eta}\phi$ the pointwise error is
$(\mathcal N(\alpha-2+i\eta)\mathcal N(\alpha-2)^{-1}-1)\rho^{i\eta}\phi$, with no factor $\rho$, while (5.3) leaves no
error ((G$''''$3); `tfgraft5.py` T4). The source's version is correct for $f^{(0)}_0$ smooth in $\rho$.

*Step 2: solving away $f_1$.* Let $\chi^\sharp_{\mathrm{tf}}$ be a cut-off of the same kind, equal to 1 on the supports
in Step 1, so $f_1 = \chi^\sharp_{\mathrm{tf}}f_1$. In $(\sigma,\hat r,\omega)$, with
$\rho_{\mathrm{scf}} = (1+\hat r)^{-1}$ and $\rho_{\mathrm{zf}} = \hat r/(1+\hat r)$ on $\{\rho<\rho_0\}$ (section 1),
and the b-density $|\frac{d\sigma}\sigma||\frac{d\hat r}{\hat r}d\slashed g|$, $|\sigma|^{-\alpha}f_1$ lies in
$H^{\infty,0}_{\mathrm b}(\pm[0,1)_\sigma;H^{\infty,\ell_{\mathrm{scf}}+1,\ell_{\mathrm{zf}}-\alpha}_{\mathrm b}(\mathrm
{tf}))$, extended by 0 to $\{\hat r\le|\sigma|/\rho_0\}$. Let
$u_1(\sigma) := N_{\mathrm{tf}}^{-1}(|\sigma|^{-\alpha} f_1(\sigma))$ by III.F$'$ Corollary 3.4, with
$\beta_{\mathrm{sctf}} = \ell_{\mathrm{scf}}$ and $\beta_{\mathrm{ztf}}\in (-1,\min(0,w))$: as $N_{\mathrm{tf}}$ does
not depend on $\sigma$ (only on its sign), it commutes with $\sigma\partial_\sigma$, and $u_1\in H^{\infty,0}_{\mathrm
b}(\pm[0,1)_\sigma;H^{\infty,\ell_{\mathrm{scf}}-\epsilon, \beta_{\mathrm{ztf}}}_{\mathrm b}(\mathrm{tf}))$. Its
expansion at ztf follows as in Theorem 3.1, with $\sigma$ as a parameter and without source terms ($Pu_1$ has no
expansion at ztf, its weight being $w$): Lemma 3.4 with no $z_j$ gives only kernel terms
$\hat r^{-\mu}\phi_0(Y(\sigma))$, replaced by $H_{\mu,\tau}(Y(\sigma))$ at the cost of terms of weight $1-\mu>\tilde b$,
and $PH_{\mu,\tau} = (\mp i)^{c_\mu+1}\hat r^{3+\{-\mu\}}\psi$ has weight $3+\{-\mu\}>w$. So
$$u_1 = \chi_{\mathrm{ztf}}\sum_{\mu\in\mathcal W(w)}\sum_\tau H_{\mu,\tau}(Y^{(\mu)}_\tau(\sigma))+\tilde u_1,
\qquad\tilde u_1\in H^{\infty,0}_{\mathrm b}\big(\pm[0,1)_\sigma;H^{\infty,\ell_{\mathrm{scf}}-\epsilon,w}_{\mathrm
b}(\mathrm{tf})\big),\tag{5.5}$$
the coefficients $Y(\sigma)$ continuous linear functionals of the data (the residues $\Pi_\mu$ applied to Mellin
transforms), hence in $H^{\infty,0}_{\mathrm b}$ in $\sigma$. Put
$$u_2 := |\sigma|^{\alpha-2}\chi_{\mathrm{zf}}\Big(G^{\mathrm{exc}}_{\mathrm s1}+G_{\mathrm s1}+G_{\mathrm v1}
+{\sum}'G_{\mu,
\tau}\Big)\big(\sigma,Y(\sigma)\big)+|\sigma|^{\alpha-2}\chi^\sharp_{\mathrm{tf}}\tilde u_1(\sigma,|\sigma|/\rho,
\omega),\tag{5.6}$$
the source's (9.92) at $n = 4$, with no functions $l_\beta$ (no exponent of a source meets a root). *tf.* By Lemma 4.3,
$|\sigma|^{2-\alpha}u_2 = u_1+e$ near tf, with $e$ of tf-weight $\epsilon_{\mathrm{ind}}$ (the coefficients $Y(\sigma)$
are conormal of weight 0), so by Lemmas 1.1-1.2, $\widehat{L_b}(\sigma)u_2 = |\sigma|^\alpha
N_{\mathrm{tf}}u_1+|\sigma|^{\alpha-2}(\widehat{L_b}-\widehat{\bar L})u_1+|\sigma|^{\alpha-2}\widehat{L_b}(\sigma)e =
f_1+O(\rho_{\mathrm{tf}}^{\alpha+2})+O(\rho_{\mathrm{tf}}^{\alpha+\epsilon_{\mathrm{ind}}-\epsilon})$ there. *scf.* As
in Proposition 4.4 (ii): scf-order $\ell_{\mathrm{scf}}+2-\epsilon$. *zf.* $|\sigma|^{\alpha-2}\tilde u_1$ has zf-weight
$\alpha-2+w = \ell_{\mathrm{zf}}$, preserved by $\widehat{L_b}(\sigma)$; at zf$^\circ$, by Lemma 4.2, the generic terms
give $|\sigma|^{\alpha-2-\mu}|\sigma|^{c_\mu+1}Y(\sigma)$, of zf-weight $\alpha+1+\{-\mu\}$, and the s1 and v1 terms
$|\sigma|^{\alpha+1}$; all exceed $\ell_{\mathrm{zf}}$, as $\ell_{\mathrm{zf}}<\alpha+1$ ($w<3$). So
$f_1-\widehat{L_b}(\sigma)u_2$ is of the form (5.1). With $u := u_0+u_2$ and
$\tilde u := |\sigma|^{\alpha-2}\tilde u_1+\chi_{\mathrm{zf}}\sum|\sigma|^jv_j$, (5.1)-(5.2) hold, the $|\sigma|$-powers
of (5.2) absorbing the signs and factors $\pm i$; the zf-weight $\alpha-3$ of (5.2) is that of
$|\sigma|^{\alpha-3}h_{b,\mathrm s1}$. $\square$

## 6. Findings, labels and sources

### 6.1 Findings

(G$''''$1) *Normalisation and a misprint.* The source's (9.58) has first-order coefficient $\mp i\tilde{\bar L}_1$ with
$\tilde{\bar L}_1(\rho\partial_\rho) = -2(\rho\partial_\rho-1-\bar S)$, which is the $\partial_{t_*}$-coefficient of
$2\bar L$, not of $\bar L$ (whose wave part is $\frac12\bar\Box = -\partial_{t_*}\rho(\rho\partial_\rho-1)+\ldots$ at
$n = 3$); the same factor 2 as III.G$''$'s Lemma 4.1 finding for $N_{\iota^+}$. Here
$N_{\mathrm{tf}} := N_{\mathrm{tf}}(\widehat{L_b},\pm1)$ throughout (Lemma 1.1 (3)), matching III.F$'$ Corollary 3.4.
The source's (9.59) prints $\rho^{-\lambda-j}$ where its companions' degree $\lambda-j$ needs $\rho^{-\lambda+j}$.

(G$''''$2) *The window.* At $n = 4$ the expansions run over $(-3,0]$ with $c_\mu = 2-\lfloor-\mu\rfloor$ companions, and
Theorem 3.1 needs $w_0<\ell^{\max}_K$ and $\ell_{\mathrm{zf}}<3$ (Proposition 4.4:
$\ell_{\mathrm{zf}}-\min(\mathrm{Re}\,\alpha_0-2,0)<\ell^{\max}_K$), where the source has $3+\epsilon_{\mathrm{ind}}$.
The bound $\ell_{\mathrm{zf}}<3$ is used in Lemma 3.3: with $c_\mu$ companions the remainder
$l_\beta\hat r^{3+\{-\mu\}}$ has weight $\min(3+\{-\mu\},5-\mathrm{Re}\,\alpha)$, and $5-\mathrm{Re}\,\alpha>w$ is
$\ell_{\mathrm{zf}}<3$ (`tfgraft5.py` T3 fails when $\ell_{\mathrm{zf}}$ is allowed up to
$3+\frac12\epsilon_{\mathrm{ind}}$). A larger $\ell_{\mathrm{zf}}$ would need one more companion at the physical roots
$-2$ ($K = 0$) and at the class roots in $(-\frac14,0)$ ($K = 2$), which Table 1.1 does not provide. Whether the
source's sections 11.5-12 at $n = 4$ need $\ell_{\mathrm{zf}}\ge3$ (a $K^+$-order $\ell_{\mathrm{zf}}+1\ge4$ of the
remainder) is for Parts III.I-III.J; it is the spectral counterpart of III.G$''$'s conditional window ((G$''$1)).

(G$''''$3) *Proposition 9.35's first step.* The source inverts the indicial operator pointwise in $\rho$ and asserts a
factor $\rho$ in the error; for conormal coefficients the error is of the size of the source term (`tfgraft5.py` T4).
Inverting the dilation-invariant operator $\mathcal N$ on the weight line $\alpha-2-j$ (5.3) removes the zf-terms
exactly, and the step then gives what the source's second step needs: a zf-free $f_1$ and an acceptable $f_2$.

(G$''''$4) *Uniform treatment.* The source treats two summands of (9.62c) and (9.75b) and calls the rest analogous, and
splits Lemma 9.26's proof into a case without and a case with integer coincidences. Here one argument covers every row
of the window: the merged residue (3.10) gives $l_{\beta_\mu}$ uniformly across coincidences, the pairing
($j = \lfloor-\mu\rfloor$) is proved from $\mathrm{Re}(2-\alpha_0)\in(-\epsilon_{\mathrm{ind}},1)$ and III.F$'$ (2.2),
and (2.2) is an identity.

(G$''''$5) *Weights.* (a) Theorem 3.1's remainder has weight exactly $\ell_{\mathrm{zf}}$ for every $\alpha$ near
$\alpha_0$, by the $\alpha$-dependent contour of Lemma 3.4's last step. (b) The sctf weight is
$\ell_{\mathrm{scf}}<\frac32$ and the ztf weight $\beta_{\mathrm{ztf}}\in(-1,0)$ (III.F$'$ Corollary 3.4). (c) The
tf-model error is $\rho_{\mathrm{scf}}^2\rho_{\mathrm{tf}}^4\mathrm{Diff}^2_{\mathrm b}$ (Lemma 1.2), so the scf-order
of the errors is $\ell_{\mathrm{scf}}+2-\epsilon$, as in the source. (d) The source determines zf-orders at zf$^\circ$
only; Proposition 4.4 (iii) records why that suffices (joint polyhomogeneity of the products). (e)
$\mathcal E_{\mathrm{ind}}$ must contain $(1,0)$ for the reduction to single terms and $(2,0)$ for Lemma 1.2; both are
allowed.

(G$''''$6) *The exceptional s1 term at $n = 4$.* $G^{\mathrm{exc}}_{\mathrm s1} = -|\sigma|\sigma^{-2}h_{b,\mathrm s1}$
vanishes at tf to order 2 (the source's 1), as $h_{b,\mathrm s1}\in\mathcal A^3$ at $n = 4$ (III.D$'''$ (3.4)); its
zf-order, which sets $\min(-1,\alpha_0-3)$ in Proposition 4.4 (1), is unchanged.

### 6.2 Labels

Proved: Lemmas 1.1-1.2, 2.2, 2.4, 3.2-3.4, 4.2-4.3, Theorem 3.1, Propositions 4.4 and 5.1, Remarks 3.5 and 4.6, given
the parts cited. Remark 3.6 and Remark 4.5 are commentary, partly READ (Remark 4.5 (1) is the source's, with its $n = 4$
range left to Part III.F). Computed (exact): `tfgraft5.py` T1-T4, each with controls. READ: the source's statements
quoted from pp. 186-199. Inputs: III.A (F1), Lemma 1.4's proof with (M1)-(M2), (E1)-(E2), Proposition 4.2; III.F Lemma
2.1; III.F$'$ (2.2), Proposition 2.3, Corollary 3.4; III.G$'$ Lemma 1.3; III.G$''$ (1.1), Table 1.1, Lemmas 1.2, 2.2,
2.4, 2.6, Definition 2.5; III.D$''$, III.D$'''$ (3.4) and III.F$''''$ Proposition 5.1 (the states); I.C section 4.1 and
(4.1); II.G$'$ (3.2).

### 6.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 9.2, pp. 186-199
((9.57)-(9.92), Definitions 9.25 and 9.29, Lemma 9.26, Remarks 9.27-9.28 and 9.31-9.34, Propositions 9.30 and 9.35).
`tfgraft5.py` (this part).