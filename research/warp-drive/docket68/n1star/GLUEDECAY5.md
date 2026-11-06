# GLUEDECAY5 -- which decaying perturbations Theorem 4 (ii) reaches, directly or through gluing

*Status.* Written (this note); not yet read by a second reader. Labels: *proved* (an argument written out here, from the
results of the supplement named at each use), *computed* (`checks/gluedecay5.py`, E1-E6, with its `.out`; each check has
a mutation control that must fail and does), *READ* (verbatim from the source, with its printed page; only where
`proof5/` does not already state it). Results are numbered by the proposition they serve.

## 0. The item and the answer

The paper's section 8.7 (`paper/RESPONSE-HL-5D.md`:1141-1149) says that a perturbation that only decays faster than
r^(-3/2) can be glued far out to a boosted Myers-Perry metric by [CD03]'s gluing, so that "the gluing would at most show
that such a perturbation agrees on a large ball with one to which Theorem 4 (ii) applies, and that is not proved here:
the glued data's smallness in Hintz's weighted norm depends on the gluing radius". This note settles that statement for
perturbations $h$ of the data of (i) with $|\partial^kh|\le\epsilon r^{-a-k}$ (conormal of order $a$), in Hintz's class
or not.

**Answer.** The statement holds, for every such perturbation, exactly when $a>\ell_0$; then no gluing is needed. At and
below $\ell_0$ it holds exactly for the perturbations that are in Hintz's class, and for those Theorem 4 (ii) applies
directly. So the class in which Theorem 4 (ii)'s conclusion is reached is Hintz's, with or without gluing.

- **(A) Above the threshold** (proved, Proposition 1; computed, E1). If $a>\ell_0$, a conormal perturbation of order $a$
  lies in the class, its terms of orders $r^{-2}$, $r^{-3}$ being zero. Its norm is at most
  $C_1\epsilon(1+(a-\ell_0)^{-1/2})$, so Theorem 4 (ii) applies to it directly when this is below $\delta$. Theorem 4
  holds for every $\ell_0\in(3,4)$, so with $\ell_0\in(3,a)$ every such perturbation with $a>3$ is covered (Corollary
  1.1). At $a = \ell_0$ the weighted integral diverges logarithmically.
- **(B) The gluing statement is class membership** (proved, Proposition 2 and Corollary 2.1). Let $N_R$ be the least
  norm of data in the class that agree with the perturbation on $\{r<R\}$. Then $N_R$ is nondecreasing in $R$, its limit
  is at least the perturbation's own norm (infinite if it is not in the class at that regularity), and equality holds in
  the class. So "agrees on every large ball with data to which (ii) applies, uniformly in $R$ in every norm of the
  class" holds if and only if (ii) applies to the perturbation itself.
- **(C) The obstruction at every rate $a\le\ell_0$** (proved, Proposition 3; computed, E2-E3). For each
  $a\in(\frac32,\ell_0]$ there are vacuum perturbations of size $\epsilon$ outside the class: the data of (i) pulled
  back by the radial diffeomorphism $x\mapsto(1+\epsilon r^{-a}\cos\log r)x$ far out, so pure gauge and $G$-invariant.
  For these, *every* data set in the class that agrees with them on $\{r<R\}$ has norm at least $c_P\,\epsilon
  R^{\ell_0-a}$, and at least $c_P\,\epsilon(\log_2(R/R_P))^{1/2}$ at $a = \ell_0$. Here $c_P =
  (2\pi^2)^{1/2}((4-a)^2+1)^{1/2}\kappa(a,\ell_0)>0$, with $\kappa$ an explicit distance in $L^2(\frac12,1)$ (certified,
  E2).
- **(D) The gluing attains this order** (proved, Proposition 4 and Corollary 4.3; computed, E4-E5). Glue on the annulus
  $\{R<r<4R\}$, by Part V's proof of [CD03] Theorem 8.1 with the error terms of Part V Step 1 and Part VII Proposition
  2.2 (6). The target is the translated, rotated and boosted Myers-Perry data on Hintz's own surface (Lemma 4.1). Every
  perturbation of order $a\in(\frac32,\ell_0]$ and size $\epsilon\le\epsilon_0$ then gives glued data of norm at most
  $C\epsilon(1+R^{\ell_0-a})$, or $C\epsilon(1+\log R)^{1/2}$ at $a = \ell_0$. So for fixed $\epsilon$, the glued data
  are small enough for (ii) only on balls of radius up to a multiple of $(\delta/\epsilon)^{1/(\ell_0-a)}$, and this is
  sharp by (C). The glued data's development is not the perturbation's.

Two findings change what the gluing needs (section 7). (GD3): the Myers-Perry data on Part V's Kerr-Schild slices differ
from Tangherlini's data on Hintz's surface by a fixed term of order $r^{-3}$ in the second fundamental form, of size
$\mu_{\mathrm{end}}$. So the family must be taken on Hintz's surface, as Part VII Proposition 2.2 does in the class.
(GD4): mass and boost are fixed by the energy and momentum alone (Lemma 4.1 (c)). Without this the upper bound would be
$\epsilon R^{\ell_0-2}$ for $2<a\le3$.

## 1. Setting

*The data of (i).* Part VII Theorem 0.2 (the paper's Theorem 4) fixes $\ell_0\in(3,4)$ and $d_1$. For
$0<\lambda\le\lambda_1$ it gives $G$-invariant smooth vacuum data $(\gamma_\lambda,k_\lambda)$ on $\Sigma :=
\Sigma_{\mathrm{IVP}}$, equal to $(\gamma^{m_\lambda},k^{m_\lambda})$ on $\Sigma\cap\{r\ge4R_{\mathrm i}\}$, where
$R_{\mathrm i}$ is the gluing radius called $R$ there. It also gives the radius $\delta$ of (ii). We fix $\lambda$. For
$r\ge R_3$, $\Sigma$ is the graph $\{t_{\mathrm{KS}} = f(|x|)\}$ with $f = c_{\mathrm{IVP}}-T_{\mu_{\mathrm{end}}}$,
identified with $\{|x|>R_3\}\subset\mathbb R^4$ (Part VII section 2). There $f' =
2\mu_{\mathrm{end}}/(r^2-\mu_{\mathrm{end}})$ for $r\ge3R_1$ (III.B (3.3)), and $(\gamma^m,k^m)$ are the data that
$g^{\mathrm{KS}}_{m,0}$ induces on this graph. We write $r = |x|$, $\rho = r^{-1}$, $\omega = x/r\in S^3$ and $|S^3| =
2\pi^2$. Constants $c$, $C$ may depend on $\lambda$, $\ell_0$, $d_1$, $a$ and the data of (i), never on $R$, $\epsilon$
or the perturbation.

*READ* ([Hin26], arXiv:2606.28253v2, printed pages; read 2026-11-06). The class and its norm:

- p. 2, (1.4)-(1.5): the coefficients of the expansion "$\tilde\gamma^{(z,m)}_{ij}$, $\tilde k^{(z+1,m)}_{ij}\in
  C^\infty(S^2)$ are small in $H^d(S^2)$ and also $\|\tilde\gamma^\flat_{ij}\|^2_{H^{d,3+\epsilon_0}_b} :=
  \int_{m_0}^\infty\int_{S^2}|r^{3+\epsilon_0}(r\partial_x)^{\le d}\tilde\gamma^\flat_{ij}(r,\omega)|^2\,d\omega\,
  \frac{dr}r$".
- p. 2, footnote 1: "for structureless data, our result requires $O(r^{-3-\epsilon_0})$-decay."
- p. 47, Definition 2.6 (2): "Fixing a finite spanning set $\mathcal A\subset\mathrm{Diff}^k_b(M)$ of
  $\mathrm{Diff}^k_b(M)$ over $C^\infty(M)$, we define the norm $\|u\|_{H^{k,\vec\alpha}_b(M)} := \sum_{A\in\mathcal
  A}\|Au\|_{H^{0,\vec\alpha}_b(M)}$, $\|u\|_{H^{0,\vec\alpha}_b(M)} := \|\vec\rho^{-\vec\alpha}u\|_{L^2(M,\mu)}$"; and
  "different choices (defining functions, b-density, spanning set of $\mathrm{Diff}^k_b$) lead to equivalent norms."
- p. 48, Definition 2.8, (2.3): $u$ lies in $H^{k,(\vec E,\vec\alpha)}_b(M)$ if "there exist $u_{(z,\ell)}$ ... such
  that ... $u-\chi(\rho_H)\sum_{(z,\ell)\in E_H,\ \mathrm{Re}\,z\le\alpha_H}\rho_H^z(\log\rho_H)^\ell u_{(z,\ell)}\in
  H^{k,(\vec E',\vec\alpha)}_b(M)$".
- p. 318, Theorem 13.1, (13.1b) and footnote 146: the smallness is in
  $\|\gamma-\gamma_{b_0}\|_{H^{d,(E_0,3+\epsilon_0)}_b(\Sigma_{\mathrm{IVP}})}$, and "one identifies
  $\Sigma_{\mathrm{IVP}}$ with the complement of a ball in $\mathbb R^3_x$; the meaning of the conditions
  (13.1a)-(13.1b) is then that they hold for each component in the frame $\partial_{x^i}$".

In five dimensions the same definitions are used on $S^3$ with the b-density $\frac{dr}r\,d\omega$ (III.A section 1.1,
PART-III-A-PREREQ.md:142-143; the density for which Part VII Lemma 0.1 holds, `checks/support8b.py` M3). The exponents
below $\ell_0$ in $\mathcal E_0 = \{(j,0):j\ge2\}$ are 2 and 3, and those of $\mathcal E_0+1$ below $\ell_0+1$ are 3 and
4 (Part VII (0.1)).

**Definition 1.1 (the norm).** Fix $r_\chi\ge\max(R_3,4R_{\mathrm i})$ and $\chi\in C^\infty(\mathbb R)$ with $\chi(r) =
0$ for $r\le r_\chi$ and $\chi(r) = 1$ for $r\ge2r_\chi$. Let $\mathcal A_d$ be the compositions of at most $d$ of the
b-vector fields $r\partial_r$ and $\Omega_{ij} = x^i\partial_j-x^j\partial_i$, the empty composition included. For $w$
on $\{r>r_\chi\}$ put $\|w\|^2_{H^{d,\ell}_b} := \sum_{A\in\mathcal
A_d}\int_{r_\chi}^\infty\!\int_{S^3}r^{2\ell}|Aw|^2\, d\omega\,\frac{dr}r$. A symmetric 2-tensor $u$ on $\Sigma$ lies in
$\mathcal H^d_0$ if, on $\{r>r_\chi\}$,
$$u_{ij} = \chi(r)\big(\rho^2u^{(2)}_{ij}(\omega)+\rho^3u^{(3)}_{ij}(\omega)\big)+\tilde u_{ij},\qquad u^{(z)}_{ij}\in
H^d(S^3),\quad\tilde u_{ij}\in H^{d,\ell_0}_b,$$
and $u\in H^d(\Sigma\cap\{r\le2r_\chi\})$. Its norm is $\|u\|_{\mathcal H^d_0} :=
\sum_{i,j}(\|u^{(2)}_{ij}\|_{H^d(S^3)}+ \|u^{(3)}_{ij}\|_{H^d(S^3)}+\|\tilde
u_{ij}\|_{H^{d,\ell_0}_b})+\|u\|_{H^d(\Sigma\cap\{r\le2r_\chi\})}$. The space $\mathcal H^d_1$ is defined likewise with
$\rho^3$, $\rho^4$ and the weight $\ell_0+1$. For pairs, $\|(u,v)\|_d := \|u\|_{\mathcal H^d_0}+\|v\|_{\mathcal H^d_1}$,
and *the class* is $\mathcal H^\infty := \bigcap_d\mathcal H^d_0\times\mathcal H^d_1$.

This is the space and the norm of the READ, the components taken in the frame $\partial_{x^i}$. Other choices of
cut-off, spanning set or sum over components give the same spaces and equivalent norms (READ, p. 47). Theorem 4 (ii)
asks $(\gamma-\gamma_\lambda,k-k_\lambda)\in\mathcal H^\infty$ with $\|\cdot\|_{d_1}<\delta$ (Part VII Theorem 0.2
(ii)). We read $\delta$ for this norm; an equivalent norm changes $\delta$ and the constants below by fixed factors.

**Lemma 1.2 (the expansion is unique).** If $b_2,b_3\in L^2(S^3)$ and $\chi(\rho^2b_2+\rho^3b_3)\in H^{0,\ell_0}_b$,
then $b_2 = b_3 = 0$. So the coefficients $u^{(z)}_{ij}$ are determined by $u$, the norm is well defined, and $\mathcal
H^d_0$, $\mathcal H^d_1$ are reflexive Banach spaces. Each is a closed subspace of a product of Hilbert spaces (the two
descriptions agree on $\{r_\chi<r<2r_\chi\}$), with an equivalent norm.

*Proof.* For a.e. $\omega$ with $b_2(\omega)\ne0$, $r^{2\ell_0}|r^{-2}b_2+r^{-3}b_3|^2\ge\frac12r^{2\ell_0-4}|b_2|^2$
for $r$ large, and $\int^\infty r^{2\ell_0-4}\frac{dr}r = \infty$ as $2\ell_0-4>0$. Where $b_2 = 0\ne b_3$, the same
holds with $2\ell_0-6>0$, as $\ell_0>3$ (computed, E1). By Fubini the weighted integral is infinite unless $b_2 = b_3 =
0$ a.e. $\square$

**Definition 1.3 (perturbations of order $a$).** Let $a>\frac32$ and $\epsilon\in(0,1]$. A smooth vacuum data set
$(\gamma,k)$ on $\Sigma$ is a *perturbation of order $a$ and size $\epsilon$* if $h := \gamma-\gamma_\lambda$ and
$\kappa := k-k_\lambda$ satisfy, in the coordinates $x$ of $\Sigma$,
$$|\partial^\beta h|\le\epsilon\langle r\rangle^{-a-|\beta|},\qquad|\partial^\beta\kappa|\le\epsilon\langle
r\rangle^{-a-1-|\beta|}\qquad(|\beta|\le d_1+6),\tag{1.1}$$
and the same bounds with some constant $C_\beta$ in place of $\epsilon$ for every $\beta$ (conormality). Nothing is
assumed about expansions: such a perturbation may or may not lie in the class.

**Definition 1.4 (the gluing statement).** For $R\ge2r_\chi$, let $N^{(d)}_R(\gamma,k)$ be the infimum of
$\|(\gamma'-\gamma_\lambda,k'-k_\lambda)\|_d$ over smooth vacuum data $(\gamma',k')$ on $\Sigma$ with
$(\gamma'-\gamma_\lambda,k'-k_\lambda)\in\mathcal H^\infty$ and $(\gamma',k') = (\gamma,k)$ on $\Sigma\cap\{r<R\}$ (the
infimum of the empty set is $\infty$). The paper's "agrees on a large ball with one to which Theorem 4 (ii) applies,
with smallness uniform as $R\to\infty$" is

(S) there are $R_0$ and $M<\delta$ with $N^{(d_1)}_R(\gamma,k)\le M$ for every $R\ge R_0$.

(S$_\infty$) is (S) with, in addition, $\sup_{R\ge R_0}N^{(d)}_R(\gamma,k)<\infty$ for every $d$.

## 2. Above the threshold: $a>\ell_0$

**Proposition 1 (in the class without gluing).** Let $a>\ell_0$ and let $(\gamma,k)$ be a perturbation of order $a$ and
size $\epsilon$. Then $(h,\kappa)\in\mathcal H^\infty$, all its coefficients $u^{(z)}$ vanish, and
$$\|(h,\kappa)\|_{d_1}\le C_1\,\epsilon\,\big(1+(a-\ell_0)^{-1/2}\big),\tag{2.1}$$
with $C_1$ depending only on $d_1$, $r_\chi$ and Definition 1.1. So if $C_1\epsilon(1+(a-\ell_0)^{-1/2})<\delta$,
Theorem 4 (ii) applies to $(\gamma,k)$ itself, and (S$_\infty$) holds with $(\gamma',k') = (\gamma,k)$ for every $R$.

*Proof.* Each of $r\partial_r = x^i\partial_i$ and $\Omega_{ij}$ has coefficients linear in $x$. So an $A\in\mathcal
A_d$ is $\sum_{|\beta|\le d}c_\beta\partial^\beta$ with $c_\beta$ polynomials of degree at most $|\beta|$, and $|Ah|\le
C\sum_{|\beta|\le d}r^{|\beta|}|\partial^\beta h|\le C\epsilon r^{-a}$ on $\{r>r_\chi\}$ by (1.1), for $d\le d_1+6$.
Take the coefficients zero, so $\tilde h = h$. Then
$$\|r^{\ell_0}Ah\|^2_{L^2(\{r>r_\chi\},\frac{dr}rd\omega)}\le C^2\epsilon^2\,2\pi^2\int_{r_\chi}^\infty
r^{2(\ell_0-a)}\frac{dr}r = C^2\epsilon^2\,2\pi^2\,\frac{r_\chi^{2(\ell_0-a)}}{2(a-\ell_0)}$$
(computed, E1). For $\kappa$ the weight is $\ell_0+1$ and the order $a+1$, with the same integral. On $\{r\le2r_\chi\}$,
$\|(h,\kappa)\|_{H^{d_1}}\le C\epsilon$ by (1.1). With $C_\beta$ in place of $\epsilon$ the same argument gives every
$d$, so $(h,\kappa)\in\mathcal H^\infty$. $\square$

**Corollary 1.1 (every rate above 3).** Theorem 4 holds for every $\ell_0\in(3,4)$, its constants $\epsilon_K$,
$\lambda_1$, $\delta$ and its data of (i) depending on $\ell_0$ (its statement fixes $\ell_0$ first). Let $a>3$ and run
it with $\ell_0\in(3,\min(a,4))$. Then its (ii) covers every perturbation of order $a$ of its data of (i) with
$\epsilon$ below $\delta/(C_1(1+(a-\ell_0)^{-1/2}))$, at the rate $t_*^{-2-\epsilon'}$ for
$\epsilon'<\epsilon_K<\ell_0-3<a-3$ (Theorem 4's chain $\epsilon_K<\epsilon_+<\ell_I-3$, $\ell_I<\ell_0$). *Proof.*
Proposition 1 with that $\ell_0$. $\square$

This is the five-dimensional counterpart of the READ footnote 1 above, in four dimensions "for structureless data, our
result requires $O(r^{-3-\epsilon_0})$-decay". The threshold is sharp: at $a = \ell_0$ the integral is $\log(R/r_\chi)$
(E1), and Proposition 3 gives a perturbation of order $\ell_0$ outside the class.

## 3. The gluing statement is class membership

**Proposition 2.** Let $(\gamma,k)$ be smooth vacuum data on $\Sigma$, $(h,\kappa) := (\gamma-\gamma_\lambda,
k-k_\lambda)$, and $d\ge0$.

(a) $R\mapsto N^{(d)}_R(\gamma,k)$ is nondecreasing. Its limit is at least $\|(h,\kappa)\|_d$, which is read as $\infty$
when $(h,\kappa)\notin\mathcal H^d_0\times\mathcal H^d_1$.

(b) If $(h,\kappa)\in\mathcal H^\infty$, then $N^{(d)}_R(\gamma,k)\le\|(h,\kappa)\|_d$ for every $R$. So the limit
equals $\|(h,\kappa)\|_d$.

*Proof.* (a) Data equal to $(\gamma,k)$ on $\{r<R'\}$ are equal to it on $\{r<R\}$ for $R<R'$, so the infimum over the
smaller set is larger. Let $L := \lim_RN^{(d)}_R<\infty$. Choose $R_n\to\infty$ and admissible $(\gamma'_n,k'_n)$ with
$u_n := (\gamma'_n-\gamma_\lambda,k'_n-k_\lambda)$, $\|u_n\|_d\le L+\frac1n$. The space $\mathcal H^d_0\times\mathcal
H^d_1$ is reflexive (Lemma 1.2), so a subsequence converges weakly to some $u$, with $\|u\|_d\le L$, the norm being
convex and continuous. For a compact $K\subset\Sigma$ the restriction $\mathcal H^d_0\times\mathcal H^d_1\to L^2(K)$ is
continuous, the weights being bounded on $K$. So $u_n|_K\rightharpoonup u|_K$ in $L^2(K)$. But $u_n|_K = (h,\kappa)|_K$
once $R_n>\sup_Kr$. Hence $u = (h,\kappa)$ on every compact set, $(h,\kappa)\in\mathcal H^d_0\times\mathcal H^d_1$, and
$\|(h,\kappa)\|_d\le L$. (b) $(\gamma,k)$ itself is admissible for every $R$. $\square$

**Corollary 2.1.** (S) implies $(h,\kappa)\in\mathcal H^{d_1}_0\times\mathcal H^{d_1}_1$ with $\|(h,\kappa)\|_{d_1}\le
M<\delta$. (S$_\infty$) holds if and only if $(h,\kappa)\in\mathcal H^\infty$ with $\|(h,\kappa)\|_{d_1}<\delta$, that
is, if and only if Theorem 4 (ii) applies to $(\gamma,k)$ itself. *Proof.* Proposition 2 (a) at $d_1$, and at every $d$
for (S$_\infty$); the converse is Proposition 2 (b). $\square$

So whatever the decay rate, uniform gluing gives nothing beyond (ii) applied directly. Proposition 2 uses neither a
decay rate nor the vacuum condition of the competitors, only the norm.

## 4. The obstruction at every rate $a\le\ell_0$

**Lemma 3.1 (a positive distance).** Let $q\in\mathbb R$ and $p_1\ne p_2$ be real. On $(\frac12,1)$ with the measure
$\frac{ds}s$, the functions $s^q\cos\log s$, $s^q\sin\log s$, $s^{p_1}$ and $s^{p_2}$ are linearly independent. Hence
$$\kappa(q;p_1,p_2) := \min_{\theta\in\mathbb R}\ \mathrm{dist}_{L^2((\frac12,1),\frac{ds}s)}\big(s^q\cos(\log
s+\theta),\ \mathrm{span}(s^{p_1},s^{p_2})\big)>0,$$
and $\kappa^2$ is the least eigenvalue of the Schur complement $S = G_{11}-G_{12}G_{22}^{-1}G_{21}$ of their Gram
matrix, with block 1 the pair $(s^q\cos\log s,s^q\sin\log s)$. Write $\kappa(a,\ell_0) :=
\kappa(\ell_0-a;\ell_0-2,\ell_0-3)$.

*Proof.* With $u = \log s\in(-\log2,0)$, a real relation among the four is $\frac{\alpha-i\beta}2e^{(q+i)u}+
\frac{\alpha+i\beta}2e^{(q-i)u}+\gamma_1e^{p_1u}+\gamma_2e^{p_2u} = 0$. The exponents $q\pm i$, $p_1$, $p_2$ are
pairwise distinct, and the Wronskian of $e^{z_1u},\dots,e^{z_4u}$ is $e^{(z_1+\dots+z_4)u}\prod_{j<k}(z_k-z_j)\ne0$
(computed, E2, symbolic). So all coefficients vanish. Now $s^q\cos(\log s+\theta) = \cos\theta\,s^q\cos\log
s-\sin\theta\,s^q\sin \log s$ is a nonzero combination of the first two, hence not in the span. Its squared distance is
$v^TSv$ with $v = (\cos\theta,-\sin\theta)$ (least squares), and $S$ is positive definite since the Gram matrix is. The
minimum over the unit circle is $\lambda_{\min}(S)$. $\square$

*Computed* (E2): the Gram matrix in closed form, checked against sympy's exact integrals and quadrature. $\kappa$ is
certified positive by interval arithmetic at $\ell_0\in\{\frac{13}4,\frac72,\frac{15}4\}$ and
$a\in\{\frac85,2,\frac52,3,\frac{3+\ell_0}2,\ell_0\}$, the class exponents 2 and 3 included; for instance
$\kappa(\frac52,\frac72) = 7.655\times10^{-4}$ and $\kappa(\frac72,\frac72) = 1.737\times10^{-3}$. The constant is small
because the annulus $(\frac R2,R)$ is short; only its positivity is used.

**Proposition 3 (perturbations outside the class).** Let $\frac32<a\le\ell_0$. Put $r_2 := 2r_\chi$, and take a cut-off
$\chi_1(r)$ equal to 0 for $r\le r_2$ and to 1 for $r\ge2r_2$. Let
$$\phi_\epsilon(r) := r+\epsilon\chi_1(r)\,r^{1-a}\cos\log r,\qquad\Psi_\epsilon(x) := \phi_\epsilon(|x|)\frac x{|x|},
\qquad(\gamma_\epsilon,k_\epsilon) := \Psi_\epsilon^*(\gamma_\lambda,k_\lambda).$$

(a) There is $\epsilon_1>0$ such that for $0<\epsilon\le\epsilon_1$: $\Psi_\epsilon$ is an $O(4)$-equivariant
diffeomorphism of $\Sigma$, the identity on $\{r\le r_2\}$; and $(\gamma_\epsilon,k_\epsilon)$ is $G$-invariant smooth
vacuum data, isometric to $(\gamma_\lambda,k_\lambda)$, and a perturbation of order $a$ and size $C_P\epsilon$.

(b) There are $R_P$ and $c_P := (2\pi^2)^{1/2}A_a\,\kappa(a,\ell_0)$, with $A_a := ((4-a)^2+1)^{1/2}$, such that for
$0<\epsilon\le\epsilon_1$, $R\ge R_P$ and every $d$:
$$N^{(d)}_R(\gamma_\epsilon,k_\epsilon)\ge c_P\,\epsilon R^{\ell_0-a}\quad(a<\ell_0),\qquad
N^{(d)}_R(\gamma_\epsilon,k_\epsilon)\ge c_P\,\epsilon\,\big(\log_2(R/R_P)\big)^{1/2}\quad(a = \ell_0).\tag{4.1}$$

(c) Hence (S) fails for $(\gamma_\epsilon,k_\epsilon)$ at every $\epsilon\in(0,\epsilon_1]$. For $a<\ell_0$, once
$R>\max(R_P,(\delta/(c_P\epsilon))^{1/(\ell_0-a)})$, no data in the class that agree with it on $\{r<R\}$ have
$\|\cdot\|_{d_1}<\delta$; for $a = \ell_0$, once $R>R_P\,2^{(\delta/c_P\epsilon)^2}$.

*Proof.* (a) Put $v := r^{1-a}\cos\log r$. Then $|\partial_r^j(\chi_1v)|\le C_jr^{1-a-j}$, so $\phi_\epsilon'\ge\frac12$
for $\epsilon\le\epsilon_1 := (2\sup|(\chi_1v)'|)^{-1}$. Also $\phi_\epsilon(r) = r$ for $r\le r_2$ and
$\phi_\epsilon(r)\to\infty$. So $\phi_\epsilon$ is an increasing bijection and $\Psi_\epsilon$ a diffeomorphism, with
inverse $x\mapsto\phi_\epsilon^{-1}(|x|)x/|x|$, commuting with $O(4)$. The constraint map is natural, so the pull-back
is vacuum. It is $G$-invariant, as $(\gamma_\lambda,k_\lambda)$ is (Part VII Theorem 0.2 (i)) and $G\subset O(4)$. On
$\{r\ge r_2\}\subset\{r\ge4R_{\mathrm i}\}$ the data are $(\gamma^{m_\lambda},k^{m_\lambda})$, which are
$O(4)$-invariant (Part VII Lemma 2.1 (b)). An $O(4)$-invariant symmetric 2-tensor is $A(r)\hat x\hat x+B(r)(\delta-\hat
x\hat x)$: the stabiliser $O(3)$ of $\hat x$ acts irreducibly on $\hat x^\perp$ and fixes no vector there. By Part VII
Lemma 2.1 (a), $\alpha := A-1$ and $\beta := B-1$ lie in $\rho^2C^\infty$, and $k^{m_\lambda} = C\hat x\hat
x+D(\delta-\hat x\hat x)$ with $C,D\in\rho^3C^\infty$. For a radial map,
$$\Psi^*\big(A\hat x\hat x+B(\delta-\hat x\hat x)\big) = A(\phi)\phi'^2\,\hat x\hat x+B(\phi)\frac{\phi^2}{r^2}
(\delta-\hat x\hat x)\tag{4.2}$$
(computed, E3: generic $\phi,A,B$ at three points of $\mathbb R^4$). Hence $h = [A(\phi)\phi'^2-A]\hat x\hat
x+[B(\phi)\phi^2/r^2-B](\delta-\hat x\hat x)$ on $\{r\ge r_2\}$ and $h = 0$ inside, and likewise $\kappa$ with $(C,D)$.
Write $A(\phi)\phi'^2-A = (\phi'^2-1)+(\alpha(\phi)-\alpha)\phi'^2+\alpha(\phi'^2-1)$, with $\alpha(\phi)-\alpha =
\epsilon\chi_1v\int_0^1\alpha'(r+s\epsilon\chi_1v)\,ds$. Each term is conormal, with constants times $\epsilon$, of
order $a$, $a+2$ and $a+2$; the $B$ and $(C,D)$ terms likewise, of orders $a$ and $a+3$. The components $\hat x_i\hat
x_j$ lie in $C^\infty(\bar X)$. So (1.1) holds with $C_P\epsilon$ in place of $\epsilon$, and with $C_\beta\epsilon$ at
all orders.

(b) Let $R\ge4r_2$ and let $(\gamma',k')$ be admissible for $N^{(d)}_R$. Write $u := \gamma'-\gamma_\lambda$ as in
Definition 1.1, and $\Gamma := \{R/2<r<R\}$, contained in $\{\chi = 1\}\cap\{\chi_1 = 1\}\cap\{r<R\}$. On $\Gamma$, $u =
h$, so $\tilde u_{ij} = h_{ij}-\rho^2u^{(2)}_{ij}(\omega)-\rho^3u^{(3)}_{ij}(\omega)$, and
$$\|(u,\cdot)\|_d\ge\sum_{i,j}\|r^{\ell_0}\tilde u_{ij}\|_{L^2(\Gamma)}\ge\|r^{\ell_0}\textstyle\sum_i\tilde
u_{ii}\|_{L^2(\Gamma)},\qquad\sum_i\tilde u_{ii} = \tau(r)-\rho^2b_2(\omega)-\rho^3b_3(\omega),$$
with $\tau := \mathrm{tr}_\delta h$ (radial) and $b_z := \mathrm{tr}\,u^{(z)}$. Integrating first in $r$ at fixed
$\omega$,
$$\|r^{\ell_0}(\tau-\rho^2b_2-\rho^3b_3)\|_{L^2(\Gamma,\frac{dr}rd\omega)}\ge(2\pi^2)^{1/2}
\inf_{\beta_2,\beta_3\in\mathbb R}\|r^{\ell_0}(\tau-\beta_2r^{-2}-\beta_3r^{-3})\|_{L^2((\frac R2,R),\frac{dr}r)}.$$
By (4.2) with $\phi = r+\epsilon v$ on $\Gamma$, exactly (computed, E3),
$$\tau = (\phi'^2-1)+3\Big(\frac{\phi^2}{r^2}-1\Big)+e_{\alpha\beta} = 2\epsilon r^{-a}\big((4-a)\cos\log r-\sin\log
r\big)+\epsilon^2\Big(v'^2+3\frac{v^2}{r^2}\Big)+e_{\alpha\beta},$$
where $e_{\alpha\beta}$ collects the $\alpha$, $\beta$ terms. So $|e_{\alpha\beta}|\le C\epsilon r^{-2-a}$ and $\tau =
2\epsilon A_ar^{-a}\cos(\log r+\phi_a)+e$, with $\phi_a := \arctan\frac1{4-a}$ and $|e|\le C_e(\epsilon
r^{-2-a}+\epsilon^2r^{-2a})$. (E3 also checks, for $\alpha = \mu r^{-2}$, that $r^{2+a}\partial_\epsilon
e_{\alpha\beta}|_0 = -2\mu(a\cos\log r+\sin\log r)$ and that $r^{2+2a}\partial^2_\epsilon e_{\alpha\beta}|_0$ is
bounded.) Substitute $r = Rs$, so $\frac{dr}r = \frac{ds}s$ and $r^{\ell_0}\beta_zr^{-z} =
\beta_zR^{\ell_0-z}s^{\ell_0-z}$. The main term contributes
$$\inf_{\beta}\|r^{\ell_0}(2\epsilon A_ar^{-a}\cos(\log r+\phi_a)-\beta_2r^{-2}-\beta_3r^{-3})\| =
2\epsilon A_aR^{\ell_0-a}\,\mathrm{dist}\big(s^{\ell_0-a}\cos(\log s+\log R+\phi_a),\mathrm{span}(s^{\ell_0-2},
s^{\ell_0-3})\big)\ge2\epsilon A_a\kappa(a,\ell_0)R^{\ell_0-a}$$
by Lemma 3.1. On $(\frac R2,R)$, $\|r^{\ell_0}e\|_{L^2(\frac{dr}r)}\le(\log2)^{\frac12}C_e(2^{2+a}\epsilon
R^{\ell_0-2-a}+2^{2a}\epsilon^2R^{\ell_0-2a})$. For $R\ge R_P$ this is at most $\epsilon A_a\kappa R^{\ell_0-a}$,
uniformly in $\epsilon\le1$, since $R^{-2}$ and $R^{-a}$ tend to 0. This gives (4.1) for $a<\ell_0$. For $a = \ell_0$,
apply the same to the disjoint annuli $\Gamma_j := \{2^{-j-1}R<r<2^{-j}R\}$ with $2^{-j}R\ge R_P$. The coefficients are
common to all annuli, so the infimum over them is at least the sum of the separate infima, which gives $\|\tilde
u\|^2\ge\sum_j(c_P\epsilon)^2$ over $\lfloor\log_2(R/R_P)\rfloor+1$ annuli. (c) follows from (4.1) at $d = d_1$.
$\square$

*Computed* (E3), an instance: $(a,\ell_0) = (\frac52,\frac72)$ and $(\frac72,\frac72)$, $\epsilon = 10^{-2}$, with the
Tangherlini term $\alpha = r^{-2}$, at $R = 10^2,10^3,10^4$. By quadrature, $D_R/(\epsilon R^{\ell_0-a})$ is within
$10^{-2}$ of $2A_a\,\mathrm{dist}(\log R+\phi_a)$ and above $2A_a\kappa$, where $D_R$ is the least-squares remainder of
$r^{\ell_0}\tau$ on $(\frac R2,R)$ against $r^{\ell_0-2}$ and $r^{\ell_0-3}$. Here $\mathrm{dist}(\cdot)$ oscillates
with $\log R$ between $\kappa$ and its maximum.

*Remark 3.2 (what the examples show).* The examples are pure gauge. Their maximal developments are isometric to that of
the data of (i), so the obstruction lies in the norm of Theorem 4 (ii), which a diffeomorphism of the initial surface
does not preserve, and not in the geometry. They are radial, hence $G$-invariant: the obstruction persists in the
symmetry class of (i). Proposition 2 holds for every perturbation, gauge or not. The examples serve only to show that at
every rate $a\le\ell_0$ some vacuum perturbation lies outside the class.

## 5. The gluing attains the order: the upper bound

**Lemma 4.1 (the Myers-Perry data on Hintz's surface).** For $p = (\mu,A,w,c)$ in the range of Part V Definition 2.1,
let $G_p := \Phi_p^*g^{\mathrm{KS}}_{\mu,A}$ be Part V's metric, and let $(\tilde g_p,\tilde K_p)$ be the data that
$G_p$ induces on the graph $\{y^0 = f(|y|)\}$ over $\{|y|>R_F\}$, identified with $\Sigma\cap\{r>R_F\}$ by $x = y$.
Write $p_\lambda := (m_\lambda,0,0,0)$, $p_2 := (\mu,w)$ and $\Delta p := p-p_\lambda$. For $R_F$ large:

(a) $(\tilde g_p,\tilde K_p)$ are smooth vacuum data; $\tilde g_p-\delta\in\rho^2C^\infty$ and $\tilde K_p\in\rho^3
C^\infty$ of the compactified $\{r\ge R_F\}$, smoothly in $p$; and $(\tilde g_{p_\lambda},\tilde K_{p_\lambda}) =
(\gamma^{m_\lambda},k^{m_\lambda})$.

(b) The $\rho^2$ coefficient of $\tilde g_p$ and the $\rho^3$ coefficient of $\tilde K_p$ depend on $p$ only through
$p_2$. Hence $\tilde g_p-\gamma^{m_\lambda} = \rho^2a_2(p)+\rho^3a_3(p)+\rho^4\mathcal R_0(p)$, with
$|a_2|_{C^m(S^3)}\le C_m|\Delta p_2|$ and $|a_3|_{C^m}+\|\mathcal R_0\|_{C^m(\bar X)}\le C_m|\Delta p|$. The same holds
for $\tilde K_p-k^{m_\lambda}$ with $\rho^3,\rho^4,\rho^5$.

(c) The charge map $\tilde{\mathfrak q}(p) := (\mathfrak Q_X(\tilde g_p,\tilde K_p))_{X\in(0.4)}$ (Part V Proposition
1.3) is $C^1$, and $D\tilde{\mathfrak q}(p_\lambda)$ is invertible. Its degree-0 part $\tilde{\mathfrak q}_0 :=
(\mathfrak Q_{e_0},\mathfrak Q_{e_l})$, the energy and momentum, depends only on $p_2$, and $p_2\mapsto\tilde{\mathfrak
q}_0$ has invertible derivative at $(m_\lambda,0)$. So there are $r_U$, $r_V$ and $L$ with $|\Delta p|\le
L|\tilde{\mathfrak q}(p)-\tilde{\mathfrak q}(p_\lambda)|$ and $|\Delta p_2|\le L|\tilde{\mathfrak
q}_0(p)-\tilde{\mathfrak q}_0(p_\lambda)|$ for $|\Delta p|<r_U$. Moreover $\tilde{\mathfrak q}$ maps $\{|\Delta
p|<r_U\}$ homeomorphically onto a set containing the ball of radius $r_V$ about $\tilde{\mathfrak q}(p_\lambda)$; write
$p(Q)$ for the inverse.

(d) Part V's own members $(g_p,K_p)$, the data of $G_p$ on $\{y^0 = 0\}$, satisfy $\tilde g_p-g_p\in\rho^3C^\infty$ and
$\tilde K_p-K_p = \nabla^2f+\rho^4C^\infty$, where $\mathrm{tr}\,\nabla^2f = 2\mu_{\mathrm{end}}r^{-3}+O(r^{-5})$. In
particular $K_{p_\lambda}-k^{m_\lambda}$ has a $\rho^3$ coefficient of size $\mu_{\mathrm{end}}$, independent of any
perturbation.

*Proof.* (a) By Part V Lemma 2.2's proof, $G_p-\eta$ is a classical symbol of order $-2$ on $\{|y^0|\le\frac12|y|\}$,
smoothly in $p$, and $\Phi_p$ is affine. The graph lies in this region, as $f$ is bounded. On it, the spatial point is
$x(y) = L_wy+f(|y|)b_w+c$, where $L_w$ is invertible and $f\in C^\infty(\bar X)$ near infinity ($f'\in|x|^{-2}C^\infty$,
III.B Lemma 3.5 (a)). So $y\mapsto x(y)$ extends to a diffeomorphism near the boundary of $\bar X$ and preserves
$\rho^jC^\infty$ (`checks/mpdata5.py` B2-B3). The data of a graph are smooth functions of $G$, $\partial G$ at the graph
and of $\partial f\in\rho^2C^\infty$, $\partial^2f\in\rho^3C^\infty$, equal to $(\delta,0)$ at $G = \eta$ with $f$
constant (Part VII Lemma 2.1 (a)'s proof). For $R_F$ large the graph is spacelike, and $G_p$ is Ricci flat (III.B
Proposition 3.4). At $p_\lambda$, $\Phi_{p_\lambda} = \mathrm{id}$ and the data are $(\gamma^{m_\lambda},k^{m_\lambda})$
by definition.

(b) $g^{\mathrm{KS}}_{\mu,A}-g^{\mathrm{KS}}_{\mu,0}\in|x|^{-3}C^\infty$, since the spins enter $H_{\mu,A}$ at relative
order $|x|^{-2}$ and $\ell_A$ at order $|x|^{-1}$ (Part V Proposition 2.3's proof; computed, E5 (a)). A translation
changes a function of $\rho^2C^\infty$ by one of $\rho^3C^\infty$ (Taylor's formula; computed, E5 (b)). So
$G_p-G_{(\mu,0,w,0)}\in\rho^3C^\infty$ on the graph. On the graph, $\tilde g-\delta =
(G-\eta)_{ij}(f,y)+\rho^4C^\infty$, as the terms $G_{0(i}\partial_{j)}f$ and $G_{00}\partial_if\partial_jf$ lie in
$\rho^4C^\infty$. Also $(G-\eta)_{ij}(f,y)-(G-\eta)_{ij}(0,y) = f\int_0^1\partial_0G_{ij}(sf,y)\,ds\in\rho^3C^\infty$.
So the $\rho^2$ coefficient of $\tilde g_p$ is that of $(G_{(\mu,0,w,0)}-\eta)_{ij}(0,y)$. The $\rho^3$ coefficient of
$\tilde K_p$ is that of the linear part in $\partial G_{(\mu,0,w,0)}$ plus that of $\nabla^2f$, which does not depend on
$p$; a Cartesian derivative gains a power of $\rho$ (`checks/mpdata5.py` B3). The bounds follow by the mean value
theorem in $p$, the coefficients being smooth in $p$, vanishing at $p_\lambda$, with $a_2$ a function of $p_2$.

(d) Change to $y'^0 = y^0-f(y)$. Then $\beta' = \beta+G_{00}\partial f = \beta-\partial f+\rho^4C^\infty$,
$g'-g\in\rho^4C^\infty$ at fixed $y^0$, $N'-N\in\rho^4C^\infty$, and $G(f,y)-G(0,y) =
f_\infty\partial_0G(0,y)+\rho^4C^\infty$ with $\partial_0G_p = O(|w|\rho^3)$. Inserting these in Part V (0.2) gives the
two statements. At $w = 0$, $G_p$ does not depend on $y^0$ and $\tilde K_p-K_p-\nabla^2f\in\rho^5C^\infty$, a statement
used in (c). The trace: $f' = 2\mu_{\mathrm{end}}/ (r^2-\mu_{\mathrm{end}})$ gives $f''+3f'/r =
2\mu_{\mathrm{end}}r^{-3}+O(r^{-5})$ (computed, E5 (d)).

(c) $C^1$ and $O(4)$-equivariance follow as in Part V Proposition 2.3's proof, since (a) gives Lemma 2.2's bounds and
the graph is $O(4)$-invariant. By Schur's lemma, $D\tilde{\mathfrak q}(p_\lambda)$ has that proposition's form: scalars
$\tilde e$, $\tilde j$, and a matrix $\begin{pmatrix}\tilde a&\tilde b'\\\tilde c'&\tilde d\end{pmatrix}\otimes I_4$ on
$(w,c)$. Compare with Part V's $\mathfrak q$ through (d). A $\rho^3C^\infty$ change of $h$ and a $\rho^4C^\infty$ change
of $K$ do not change a degree-0 flux, since $\mathfrak b_X$ is linear and $\rho^4\cdot r^3\to0$. The term $\nabla^2f$
carries no momentum at any radius: $(\nabla^2f-\Delta f\,\delta)\hat x = -3\frac{f'}r\hat x$, which is odd (computed, E5
(c)). So $\tilde{\mathfrak q}_0 = \mathfrak q_0$ for every $p$, whence $\tilde e = e$, $\tilde a = a$ and $\tilde b' =
b' = 0$. By (b)'s argument on $\{y^0 = 0\}$, $g_p-g_{(\mu,0,w,0)}\in\rho^3C^\infty$ and
$K_p-K_{(\mu,0,w,0)}\in\rho^4C^\infty$, so $\mathfrak q_0(p) = \mathfrak q_0(\mu,0,w,0)$: the energy and momentum depend
only on $p_2$. At $w = 0$ the differences are $\rho^4C^\infty$ in $h$ (the graph terms) and $\nabla^2f+\rho^5C^\infty$
in $K$, smoothly in $(\mu,A,c)$. The term $\nabla^2f$ does not depend on $p$, and it carries no angular momentum: $(W
x)\cdot\nabla^2f\cdot x = 0$ (E5 (c)). The fluxes of degree 1 of $\partial_A$, $\partial_c$ of the rest tend to 0, as
$r\cdot\rho^5\cdot r^3\to0$ and $\rho^4\cdot r^3\to0$. So $\tilde j = j$ and $\tilde d = d$, and $\det D\tilde{\mathfrak
q}(p_\lambda) = \tilde e\,(\tilde a\tilde d)^4\tilde j^6 = \det D\mathfrak q(p_\lambda)\ne0$. Here Part V Proposition
2.3's values are taken at the base mass $m_\lambda$; its computation uses only that the base is Tangherlini. The
$p_2$-block is $\mathrm{diag}(e,aI_4)$, its off-diagonal blocks vanishing by Schur's lemma. The rest is the inverse
function theorem (cited). $\square$

**Lemma 4.2 (charges).** (a) For data $z_i = (\delta+h_i,K_i)$ with $|h_i|\le\frac12$, put $m(z) :=
\sum_{|\beta|\le2}r^{|\beta|}|\partial^\beta h|+\sum_{|\beta|\le1}r^{1+|\beta|}|\partial^\beta K|$. Then
$$|q_X(z_1)-q_X(z_2)|\le C(1+r)^{d(X)}r^{-2}\big(m(z_1)+m(z_2)\big)\,m(z_1-z_2).\tag{5.1}$$
(b) For a perturbation of order $a$ and size $\epsilon$, with $\Delta\mathfrak Q_X := \mathfrak Q_X(\gamma,k)-
\tilde{\mathfrak q}_X(p_\lambda)$: $\Delta\mathfrak Q_X = 0$ if $a>2+d(X)$, and $|\Delta\mathfrak Q_X|\le C_1'\epsilon$
in every case.

*Proof.* (a) By Part V Lemma 1.2's proof, $q_X$ is linear in $(N,Y)$, and for $|h|\le\frac12$ polynomial in $(\partial
h,\partial^2h,K,\partial K)$ with coefficients smooth in $h$. Each term is quadratic, counting $\partial h$, $K$ once
and $\partial^2h$, $\partial K$ twice, or a term linear in $\partial^2h$ or $\partial K$ whose coefficient vanishes at
$h = 0$. Telescoping each product and using the mean value theorem on the coefficients gives (5.1), with $|N|+|Y|\le
C(1+r)^d$. (b) $\mathfrak Q_X(\gamma,k)$ exists by Part V Proposition 1.3, with $\alpha = \min(a,2)>\frac32$. As
$\mathfrak b_X$ is linear, $\Delta\mathfrak Q_X = \lim_\rho\oint_{S_\rho}\mathfrak b_X(h,\kappa)$, and
$|\oint_{S_\rho}\mathfrak b_X(h,\kappa)|\le C\epsilon\rho^{2+d-a}$, which tends to 0 if $a>2+d$. In general, take
$R_\lambda := \max(r_\chi,R_F)$ and subtract Part V (1.1) for $(\gamma_\lambda,k_\lambda)$ on $\Gamma(R_\lambda,\rho)$
from (1.1) for $(\gamma,k)$. By (5.1), $|\Delta\mathfrak Q_X|\le C\epsilon
R_\lambda^{2+d-a}+C\epsilon\int_{R_\lambda}^\infty r^{d-2}(r^{-2}+\epsilon r^{-a})r^{-a}r^3dr$, and the integral
converges, since $d-a<0$ and $d+2-2a<0$ (computed, E4). $\square$

**Proposition 4 (gluing to the Myers-Perry data on Hintz's surface, with the error).** Let $\frac32<a\le\ell_0$ and $k
:= d_1+2$. There are $R_G$, $\epsilon_0$ and $C$ with the following property. For every perturbation $(\gamma,k)$ of
order $a$ and size $\epsilon\le\epsilon_0$, and every $R\ge R_G$, there are $p_R$ and smooth vacuum data
$(\hat\gamma_R,\hat k_R)$ on $\Sigma$, equal to $(\gamma,k)$ on $\{r\le R\}$ and to $(\tilde g_{p_R},\tilde K_{p_R})$ on
$\{r\ge4R\}$, with
$$|\Delta p_{R,2}|\le C\epsilon R^{\min(0,2-a)},\qquad|\Delta p_R|\le C\epsilon R^{\min(0,3-a)},\tag{5.2}$$
$$\sup_{R\le r\le4R}\Big(\sum_{|\beta|\le k-1}r^{|\beta|}|\partial^\beta(\hat\gamma_R-\gamma_\lambda)|+
\sum_{|\beta|\le k-2}r^{1+|\beta|}|\partial^\beta(\hat k_R-k_\lambda)|\Big)\le C\epsilon R^{-a}.\tag{5.3}$$

*Proof.* We follow Part V's proof of Theorem 3.1, with $k$ in place of 3 as in Part VII Proposition 2.2 (its Step 1
allows every $k>\frac n2$), and make six changes. Data with (1.1) have $|||(\gamma,k)|||_{\min(a,2),k+4}<\infty$.

(1) *The family and the box.* Lemma 4.1's members replace Part V's: (a) gives Lemma 2.2's bounds and (c) gives Corollary
2.4. In Step 2 let $Q$ range over the box $\bar B_R := \{Q:|Q_X-\tilde{\mathfrak q}_X(p_\lambda)|\le r_X\}$, with $r_X
:= C_0\epsilon R^{\min(0,2+d(X)-a)}$ and $C_0 := C_1'+1$. Then $\bar B_R$ lies in the ball of radius $r_V$ once
$\sqrt{15}\,C_0\epsilon_0<r_V$. For $Q\in\bar B_R$, Lemma 4.1 (c) gives $|\Delta p_2|\le\sqrt5LC_0\epsilon
R^{\min(0,2-a)}$ and $|\Delta p|\le\sqrt{15}LC_0\epsilon R^{\min(0,3-a)}$, where $\Delta p := p(Q)-p_\lambda$. The
exponents of the five degree-0 components are at most the first and those of the other ten at most the second.

(2) *The source in relative form.* Write $a_\sigma := \sigma_R(\gamma,k)$ and $b_Q := \sigma_R(\tilde g_{p(Q)}, \tilde
K_{p(Q)})$ on $M = \bar\Gamma(1,4)$. Both are vacuum (Part V Lemma 1.4), and $x_{Q,R} = b_Q+\chi(a_\sigma-b_Q)$. The
constraint map is smooth near flat data and vanishes at $b_Q$. So, as in Part VII Proposition 2.2 (6),
$\|(J,\rho)(x_{Q,R})\|_{C^{k+1}}\le C\|a_\sigma-b_Q\|_{C^{k+3}\times C^{k+4}}\le C\theta_R(Q)$, with
$$\theta_R(Q) := \epsilon R^{-a}+|\Delta p_2|R^{-2}+|\Delta p|R^{-3}\le C(1+C_0)\,\epsilon R^{-a}\tag{5.4}$$
by (1.1), Lemma 4.1 (b) with $(\tilde g_{p_\lambda},\tilde K_{p_\lambda}) = (\gamma_\lambda,k_\lambda)$ on $\{r\ge R\}$,
the scaling $\|\sigma_Ru\|_{C^m(M)}\le C\sup_{R\le r\le4R}\sum_{|\beta|\le m}r^{|\beta|}|\partial^\beta u|$ (one more
power of $r$ for $K$), and (1) (the inequality in (5.4): computed, E4). By Step 1's bound and Lemma 3.2, $\|\delta
x_{Q,R}\|_{C^{k-1}(M)}\le C\|\delta x_{Q,R}\|_{H^{k+2}(M)}\le C\theta_R(Q)$, continuously in $Q$. So the unscaled
$\hat{\mathfrak x}_Q := \sigma_R^{-1}(x_{Q,R}+\delta x_{Q,R})$ satisfies (5.3)'s bound by $C\theta_R(Q)$ against
$(\gamma_\lambda,k_\lambda)$. It is the sum of $\chi$ times the data's deviation, $(1-\chi)$ times the member's, and
$\delta x$. Part V's Step 1 hypotheses hold for $R$ large, as $x_{Q,R}$ is within $CR^{-2}+C\epsilon R^{-a}$ of flat
data.

(3) *Step 4 in relative form.* Lemma 1.4 and (1.1) of Part V give $G_R(Q)_X := R^{2+d(X)}F_R(Q)_X =
\oint_{S_{4R}}\mathfrak b_X(\hat{\mathfrak x}_Q)-\oint_{S_R}\mathfrak b_X(\hat{\mathfrak
x}_Q)+\int_{\Gamma(R,4R)}q_X(\hat{\mathfrak x}_Q)$. Near $S_{4R}$ the data are the member's, and near $S_R$ the
perturbation's. By the flux identity on the vacuum regions outside, $\oint_{S_{4R}} = Q_X+\int_{r>4R}q_X(\text{member})$
and $\oint_{S_R} = \mathfrak Q_X(\gamma,k)+\int_{r>R}q_X(\gamma,k)$. Subtract the trivial identity $0 =
\int_{r>4R}q_X-\int_{r>R}q_X+\int_{\Gamma(R,4R)}q_X$ for $(\gamma_\lambda,k_\lambda)$. Then
$$G_R(Q)_X = Q_X-\tilde{\mathfrak q}_X(p_\lambda)-\Delta\mathfrak Q_X+T_X(Q),$$
where $T_X$ is the sum of the three differences $\int_{r>4R}[q_X(\text{member})-q_X(\gamma_\lambda,k_\lambda)]$,
$-\int_{r>R}[q_X(\gamma,k)-q_X(\gamma_\lambda,k_\lambda)]$ and $\int_{\Gamma(R,4R)}[q_X(\hat{\mathfrak
x}_Q)-q_X(\gamma_\lambda,k_\lambda)]$. By (5.1), with $m\le Cr^{-2}$ for the reference, $m(\text{member}-\text{ref})\le
C(|\Delta p_2|r^{-2}+|\Delta p|r^{-3})$, $m(h,\kappa)\le\epsilon r^{-a}$ and (2) on the annulus,
$$|T_X(Q)|\le CR^{d}\big(|\Delta p_2|R^{-2}+|\Delta p|R^{-3}\big)+C\epsilon\big(R^{d-a}+\epsilon R^{d+2-2a}\big)+
CR^{d}\big(\theta_R+R^2\theta_R^2\big),\qquad d = d(X).$$
With (1) and (5.4), each term is $C(1+C_0)^2\epsilon$ times one of $R^{d-2+\min(0,2-a)}$, $R^{d-3+\min(0,3-a)}$,
$R^{d-a}$ and $R^{d+2-2a}$. Each exponent is strictly below $\min(0,2+d-a)$ (computed, E4: every vertex of the pieces of
$\{\frac32\le a\le\ell_0,\ 3\le\ell_0\le4\}$ cut at $a = 2,3$, on which the exponents are linear). So for $R\ge R_G$,
$|T_X(Q)|\le\epsilon R^{\min(0,2+d-a)}$ on $\bar B_R$.

(4) *The charges.* By Lemma 4.2 (b), $\Delta\mathfrak Q_X = 0$ if $a>2+d(X)$, and $|\Delta\mathfrak Q_X|\le
C_1'\epsilon$ otherwise.

(5) *A zero by Brouwer's theorem* (in place of Part V Lemma 3.3; cited, as there). Let $\Theta(Q) := \tilde{\mathfrak
q}(p_\lambda)+\Delta\mathfrak Q-T(Q)$. By (3) and (4), $|\Theta_X(Q)- \tilde{\mathfrak q}_X(p_\lambda)|\le r_X$ on $\bar
B_R$. If $a\le2+d$ this reads $C_1'\epsilon+\epsilon = C_0\epsilon$; if $a>2+d$, it reads $0+\epsilon R^{2+d-a}$.
$\Theta$ is continuous, by Part V Step 3 and Lemma 3.2, so it has a fixed point $Q_R$. Then $G_R(Q_R) = 0$, and by Part
V Step 3 the data $x_{Q_R,R}+\delta x_{Q_R,R}$ are vacuum.

(6) *Conclusion.* Part V Step 5 gives the smooth vacuum data with $p_R := p(Q_R)$. Then (5.2) is (1), and (5.3) is (2)
with (5.4). $\square$

**Corollary 4.3 (the norm of the glued data).** In Proposition 4, $(\hat\gamma_R-\gamma_\lambda,\hat k_R-k_\lambda)\in
\mathcal H^\infty$, and
$$\|(\hat\gamma_R-\gamma_\lambda,\hat k_R-k_\lambda)\|_{d_1}\le C\epsilon\big(1+R^{\ell_0-a}\big)\quad(a<\ell_0),\qquad
\le C\epsilon\,(1+\log R)^{1/2}\quad(a = \ell_0).\tag{5.5}$$
So Theorem 4 (ii) applies to the glued data when $C\epsilon(1+R^{\ell_0-a})<\delta$, and for each fixed
$\epsilon<\delta/ (2C)$ for $R$ up to $(\delta/(2C\epsilon))^{1/(\ell_0-a)}$. By Proposition 3 (c) this window is sharp
up to the constant, since no data in the class do better for the examples.

*Proof.* Membership: the data are smooth, and for $r\ge4R$ the difference is $(\tilde g_{p_R}-\gamma^{m_\lambda},\tilde
K_{p_R}-k^{m_\lambda})\in\rho^2C^\infty\times\rho^3C^\infty$, which lies in the class by Part VII Lemma 0.1. For the
norm let $u := \hat\gamma_R-\gamma_\lambda$, and use $|Au|\le C\sum_{|\beta|\le d_1}r^{|\beta|}|\partial^\beta u|$ as in
Proposition 1. The coefficients of $u$ are those of $\tilde g_{p_R}-\gamma^{m_\lambda}$ (Lemma 1.2), namely $a_2(p_R)$
and $a_3(p_R)$, of size at most $C|\Delta p_R|\le C\epsilon$ (Lemma 4.1 (b)). The remainder $\tilde u =
u-\chi(\rho^2a_2+\rho^3a_3)$ splits by region:

- $r\le2r_\chi$: $u = h$, norm $\le C\epsilon$.
- $r_\chi<r<R$: $\tilde u = h-\chi(\rho^2a_2+\rho^3a_3)$. Its norm is at most
  $C\epsilon\|r^{\ell_0-a}\|_{L^2((r_\chi,R), \frac{dr}r)}+C|\Delta p_2|\|r^{\ell_0-2}\|+C|\Delta p|\|r^{\ell_0-3}\|$,
  so at most $C\epsilon R^{\ell_0-a}$ (or $C\epsilon(\log R)^{1/2}$ at $a = \ell_0$), by (5.2):
  $\min(0,2-a)+\ell_0-2\le\ell_0-a$ and $\min(0,3-a)+\ell_0-3\le \ell_0-a$ (computed, E1 and E4).
- $R\le r\le4R$: $|A\tilde u|\le C\epsilon R^{-a}+C|\Delta p_2|R^{-2}+C|\Delta p|R^{-3}\le C\epsilon R^{-a}$ by (5.3)
  and (5.4), so the norm there is at most $C\epsilon R^{\ell_0-a}(\log4)^{1/2}$.
- $r\ge4R$: $\tilde u = \rho^4\mathcal R_0(p_R)$, so the norm is at most $C|\Delta
  p_R|(4R)^{\ell_0-4}(2(4-\ell_0))^{-1/2}\le C\epsilon$.

The same holds for $\hat k_R-k_\lambda$, with weight $\ell_0+1$, order $a+1$ and the exponents 3 and 4. $\square$

The record's estimate, "a bump of relative size $R^{-1}$ at radius $R$ costing about $R^{\ell_0-3}$"
(`checks/support8b.py` M3), is the annulus term of Corollary 4.3 at $a = 3$. Proposition 3 supplies the lower bound that
M3 does not, valid for every data set and not only the glued one.

## 6. The settlement

**Theorem 5.** Fix $\ell_0\in(3,4)$, $d_1$, $\lambda\le\lambda_1$, the data of (i) and $\delta$ as in Theorem 4, and let
$a>\frac32$.

(i) If $a>\ell_0$, every perturbation of order $a$ and size $\epsilon<\delta/(C_1(1+(a-\ell_0)^{-1/2}))$ lies in the
class with $\|\cdot\|_{d_1}<\delta$. So Theorem 4 (ii) applies to it directly, and (S) and (S$_\infty$) hold with the
perturbation itself as the data on every ball. Over Theorem 4's admissible $\ell_0$, this covers every $a>3$ (Corollary
1.1).

(ii) If $\frac32<a\le\ell_0$, the decay rate does not decide. (S$_\infty$) holds for a perturbation exactly when it lies
in the class with $\|\cdot\|_{d_1}<\delta$, and (S) only if it lies in the class at regularity $d_1$ (Corollary 2.1). At
every such $a$ and every $\epsilon\in(0,\epsilon_1]$, some perturbation of order $a$ and size $C_P\epsilon$ fails (S).
For it, every data set in the class agreeing with it on $\{r<R\}$ has norm at least $c_P\epsilon R^{\ell_0-a}$ (or
$c_P\epsilon(\log_2(R/R_P))^{1/2}$), Proposition 3. The gluing of Proposition 4 attains this order for every
perturbation of order $a$ (Corollary 4.3).

So "Theorem 4 (ii) applies up to the gluing" is false for fixed $\epsilon$ and large $R$ at every
$a\in(\frac32,\ell_0]$. Its uniform form is equivalent to (ii) applied directly, and the class in which Theorem 4 (ii)'s
conclusion is reached, directly or through gluing, is exactly Hintz's class. The development of glued data is not the
perturbation's: on $\{r>R\}$ the data differ, and the late-time solution near the hole depends on them (Part VII finding
(VII1)).

*Proof.* (i) is Proposition 1 with Corollary 1.1, and (ii) is Corollary 2.1 with Propositions 3 and 4 and Corollary 4.3.
$\square$

## 7. Findings, labels and sources

(GD1) *The reach of the settling statement.* The paper's "the gluing would at most show that such a perturbation agrees
on a large ball with one to which Theorem 4 (ii) applies" is, in its uniform form, equivalent to (ii) applied to the
perturbation itself (Corollary 2.1). The perturbations so reached are exactly those in Hintz's class.

(GD2) *The threshold.* At fixed $\ell_0$ the decay rate decides only above $\ell_0$ (Proposition 1). At every
$a\in(\frac32,\ell_0]$ there are $G$-invariant, pure-gauge vacuum perturbations outside the class (Proposition 3). Over
Theorem 4's $\ell_0\in(3,4)$ every $a>3$ is covered, the five-dimensional counterpart of [Hin26]'s footnote 1 (READ).
The glued norm is $\asymp\epsilon R^{\ell_0-a}$: the lower bound holds for every data set (Proposition 3) and the upper
bound for the gluing (Corollary 4.3).

(GD3) *The gluing family.* The Myers-Perry data on Part V's Kerr-Schild slices $\{y^0 = 0\}$ differ from Tangherlini's
data on Hintz's surface by $\nabla^2f$ in the second fundamental form, of trace $2\mu_{\mathrm{end}}r^{-3}$ (Lemma 4.1
(d)). Gluing to Part V's members therefore leaves an $O(\mu_{\mathrm{end}})$ coefficient of $\rho^3$ in $k$, and the
glued data are not small in the class even at $\epsilon = 0$. The family must be taken on Hintz's surface (Lemma 4.1),
as Part VII Proposition 2.2 does with Tangherlini in the class. The paper's "can be glued far out to such a metric" is
true with this family, whose charge map Lemma 4.1 (c) shows to be a local diffeomorphism.

(GD4) *Decoupling.* The energy and momentum of the family depend on mass and boost alone (Lemma 4.1 (c)). Without this,
the parameters of the glued metric would be known only to $O(\epsilon)$. The term $|\Delta p_2|R^{\ell_0-2}$ would then
exceed $\epsilon R^{\ell_0-a}$ for $2<a\le3$, which E4's control exhibits.

(GD5) *The record's bump estimate.* `checks/support8b.py` M3 computes one term of the upper bound at $a = 3$. The lower
bound, which decides the item, is Proposition 3.

*Labels.* Lemma 1.2, Propositions 1-4, Corollaries 1.1, 2.1, 4.3, Lemmas 3.1, 4.1, 4.2 and Theorem 5: proved, from the
inputs below. Every integral, exponent, identity and constant they use is computed in `checks/gluedecay5.py` E1-E6.
Brouwer's fixed point theorem and the inverse function theorem are cited, as in Part V.

*Sources.* READ: [Hin26] (arXiv:2606.28253v2) pp. 2 ((1.4)-(1.5), footnote 1), 47 (Definition 2.6 (2)), 48 (Definition
2.8, (2.3)), 318 (Theorem 13.1, (13.1b), footnote 146), read 2026-11-06. Nothing new from [CD03]: its estimates enter as
`proof5/PART-V-GLUING.md` states them (Step 1 with Proposition G.1's bound, Lemma 3.2, Steps 2-5, Lemma 1.2 with
(1.1)-(1.2), Proposition 1.3, Lemma 1.4, Definition 2.1, Lemma 2.2, Proposition 2.3, Corollary 2.4), together with
`proof5/PART-VII-ASSEMBLY.md` (Theorem 0.2, Lemma 0.1, Lemma 2.1, Proposition 2.2 (6), finding (VII1)). Also
`proof5/PART-III-B-FAMILY.md` ((3.3), Lemma 3.5 (a), Proposition 3.4), `proof5/PART-III-A-PREREQ.md` section 1.1, and
`checks/mpdata5.py` B2-B3. Nothing from outside `research/warp-drive/` other than [Hin26].

    python3 checks/gluedecay5.py   (about two minutes; output in checks/gluedecay5.out)

## 8. Proposed replacement for the paper

`paper/RESPONSE-HL-5D.md`, section 8.7, lines 1141-1149, from "a translation, and the structural step" to the end of the
paragraph. The old text occurs exactly once (computed, E6); the paper is not edited here.

Old:

```text
a translation, and the structural step that a Cartesian derivative gains a power of ρ). A perturbation that only decays,
faster than r^(−3/2), can be glued far out to such a metric by [CD03]'s gluing, which in five dimensions needs no parity
condition at that rate (section 8.6; supplement sections 10.63 and 10.66). But the glued data's development is not the
perturbation's: the solution near the hole at late times depends on the data near infinity. So the gluing would at most
show that such a perturbation agrees on a large ball with one to which Theorem 4 (ii) applies, and that is not proved
here: the glued data's smallness in Hintz's weighted norm depends on the gluing radius, a bump of relative size R^(−1) at
radius R costing about R^(ℓ0−3) there (deduced in supplement `docket68/n1star/proof5/PART-VII-ASSEMBLY.md` section 5;
computed for a bump of amplitude R^(−3), R^(−1) of the black hole's own deviation from flat space at R, in the norm's
b-density, `docket68/n1star/checks/support8b.py` M3).
```

New:

```text
a translation, and the structural step that a Cartesian derivative gains a power of ρ). It also contains every
perturbation conormal of an order a > ℓ0, with |∂^k h| ≤ ε r^(−a−k) in the metric and ε r^(−a−1−k) in the second
fundamental form. Such a perturbation has no terms of orders r^(−2) and r^(−3), and its norm is at most C ε (1 + (a −
ℓ0)^(−1/2)). Since Theorem 4 holds for every ℓ0 ∈ (3, 4), taking ℓ0 ∈ (3, a) covers every such perturbation with a > 3
(proved: supplement `docket68/n1star/GLUEDECAY5.md` Proposition 1 and Corollary 1.1). For 3/2 < a ≤ ℓ0 the decay rate
does not decide, and gluing does not help. A perturbation agrees on every ball r < R with data to which Theorem 4 (ii)
applies, uniformly in R in every norm of the class, if and only if Theorem 4 (ii) applies to the perturbation itself.
The least norm of data in the class that agree with it on r < R increases with R, to its own norm if it lies in the
class, and without bound if it does not lie in the class at the norm's regularity (proved: GLUEDECAY5.md Proposition 2
and Corollary 2.1). At every such a there are vacuum perturbations of size
ε outside the class: the data pulled back by the radial diffeomorphism x ↦ (1 + ε r^(−a) cos log r) x far out, pure
gauge and G-invariant. For these, every data set in the class that agrees with them on r < R has norm at least
c ε R^(ℓ0−a), and at least c ε (log R)^(1/2) at a = ℓ0 (proved: GLUEDECAY5.md Proposition 3). [CD03]'s gluing on the
annulus R < r < 4R attains this order, with no parity condition in five dimensions at these rates (section 8.6;
supplement sections 10.63 and 10.66). The target is the translated, rotated and boosted Myers–Perry data on Hintz's
surface itself (the data on the Kerr–Schild slices of supplement `docket68/n1star/proof5/PART-V-GLUING.md` differ from
them by a fixed term of order r^(−3) in the second fundamental form). Its glued data then have norm at most C ε R^(ℓ0−a)
(proved: GLUEDECAY5.md Proposition 4 and
Corollary 4.3, with the gluing's estimates as supplement `docket68/n1star/proof5/PART-V-GLUING.md` and
`PART-VII-ASSEMBLY.md` Proposition 2.2 state them). So for fixed ε the glued data are small enough for Theorem 4 (ii)
only for R up to a multiple of (δ/ε)^(1/(ℓ0−a)), and this is sharp. Their development is not the perturbation's: the
solution near the hole at late times depends on the data near infinity. The class in which Theorem 4 (ii)'s conclusion
is reached, directly or through gluing, is exactly Hintz's class (computed: every integral, exponent and constant,
`docket68/n1star/checks/gluedecay5.py` E1–E6).
```
