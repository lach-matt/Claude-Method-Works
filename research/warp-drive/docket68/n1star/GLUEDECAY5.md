# GLUEDECAY5 -- which decaying perturbations Theorem 4 (ii) reaches, directly or through gluing

*Status.* Written (this note); not yet read by a second reader. Labels: *proved* (an argument written out here, from the
results of the supplement named at each use), *computed* (`checks/gluedecay5.py`, E1-E6, with its `.out`; each check has
a mutation control that must fail and does), *READ* (verbatim from the source, with its printed page; only where
`proof5/` does not already state it). Results are numbered by the proposition they serve.

[R2.0: read by an independent verifier, who found the mathematics to hold; its findings are re-derived and seated in
section R2.0, with bracketed notes at each place they change, and section 8.2 is the current proposal for the paper.]

[R4.0: the status above is stale. The note has been read by three readers, one per round (rounds 2-4); the mathematics
was found to hold each time, and their findings are seated in sections R2.0, R3.0 and R4.0. Section 8.4 is the current
proposal for the paper; sections 8.1-8.3 are superseded.]

[Proved (2026-11-06): round 5's seating was confirmed by the round-3/4 reader with no new major or minor finding; the
whole of `checks/gluedecay5.py` exits 0 with all 21 mutants failing on the paper as it stands and on a seated copy.
Section 8.5 is the current proposal; sections 8.1-8.4 are superseded. Two optional nits seated with this note.]

[R5.0: four readings now (rounds 2-5), the mathematics found to hold each time; section 8.5 is the current proposal and
sections 8.1-8.4 are superseded.]

## 0. The item and the answer

The paper's section 8.7 (`paper/RESPONSE-HL-5D.md`:1141-1149) says that a perturbation that only decays faster than
r^(-3/2) can be glued far out to a boosted Myers-Perry metric by [CD03]'s gluing, so that "the gluing would at most show
that such a perturbation agrees on a large ball with one to which Theorem 4 (ii) applies, and that is not proved here:
the glued data's smallness in Hintz's weighted norm depends on the gluing radius". This note settles that statement for
perturbations $h$ of the data of (i) with $|\partial^kh|\le\epsilon r^{-a-k}$ (conormal of order $a$), in Hintz's class
or not.

**Answer.** The statement holds for every such perturbation of small size exactly when $a>\ell_0$, and then no gluing is
needed. At and below $\ell_0$ it holds exactly for the perturbations that are in Hintz's class, and for those Theorem 4
(ii) applies directly. So the class in which Theorem 4 (ii)'s conclusion is reached is Hintz's, with or without gluing.

[R2.0, Minor 3: "the class in which Theorem 4 (ii)'s conclusion is reached is Hintz's" overclaims. The pure-gauge
examples of (C) lie outside the class, yet their developments are isometric to that of (i) (Remark 3.2). Read: the
perturbations to which Theorem 4 (ii) applies, directly or through gluing uniformly in $R$, are exactly those small in
Hintz's class.]

- **(A) Above the threshold** (proved, Proposition 1; computed, E1). If $a>\ell_0$, a conormal perturbation of order $a$
  lies in the class, its terms of orders $r^{-2}$, $r^{-3}$ being zero. Its norm is at most
  $C_1\epsilon(1+(a-\ell_0)^{-1/2})$, so Theorem 4 (ii) applies to it directly when this is below $\delta$. Theorem 4
  holds for every $\ell_0\in(3,4)$, so with $\ell_0\in(3,\min(a,4))$ every such perturbation with $a>3$ is covered
  (Corollary 1.1). At $a = \ell_0$ the weighted integral diverges logarithmically.
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

[R2.0. (A), Minor 2: the data of (i), $\lambda_1$ and $\delta$ are those of the theorem run with that $\ell_0$;
$\epsilon$ is below $\delta/(C_1(1+(a-\ell_0)^{-1/2}))$; and the rate is $t_*^{-2-\epsilon'}$ with
$\epsilon'<\epsilon_K<\ell_0-3$ (Corollary 1.1). (B), nit: $N_R$ is an infimum. (C), nits: the examples have size
$C_P\epsilon$ and need $\epsilon\le\epsilon_1$, and the bounds hold for $R\ge R_P$. (D), Minor 1: "only ... and this is
sharp" overclaims. Corollary 4.3 is a sufficient condition for every perturbation, sharpness is shown only for the
examples of (C), and at $a = \ell_0$ the exponent $1/(\ell_0-a)$ is undefined. Read: for $a<\ell_0$ the glued data are
guaranteed small enough for (ii) for $R_G\le R<(\delta/(2C\epsilon))^{1/(\ell_0-a)}$, a range that is nonempty when
$2C\epsilon R_G^{\ell_0-a}<\delta$; for the examples of (C), no data in the class agreeing with them on $\{r<R\}$ do
better than (C)'s lower bound.]

[R3.0, nit 3: in (A), "its terms of orders $r^{-2}$, $r^{-3}$ being zero" is for the metric. In the second fundamental
form the orders are $r^{-3}$ and $r^{-4}$, and these vanish too, as Proposition 1 states for all the coefficients
$u^{(z)}$.]

Two findings change what the gluing needs (section 7). (GD3): the Myers-Perry data on Part V's Kerr-Schild slices differ
from Tangherlini's data on Hintz's surface by a fixed term of order $r^{-3}$ in the second fundamental form, of size
$\mu_{\mathrm{end}}$. So the family must be taken on Hintz's surface, as Part VII Proposition 2.2 does in the class.
(GD4): mass and boost are fixed by the energy and momentum alone (Lemma 4.1 (c)). Without this the upper bound would be
$\epsilon R^{\ell_0-2}$ for $2<a\le3$.

[R2.0, nit: precisely, $\tilde K_p-K_p = \nabla^2f+\rho^4C^\infty$ at the same $p$, and $K_{p_\lambda}-k^{m_\lambda} =
-\nabla^2f+\rho^5C^\infty$ (Lemma 4.1 (d)). GD3 constrains this note's Proposition 4 only. It is no defect of Part V:
its Theorem 3.1 is about abstract data, and Part VII uses its proof only in class form, with Tangherlini members on
$\Sigma_{\mathrm{IVP}}$ (Part VII Proposition 2.2, findings (VII1), (VII3)). Part V's Remark 3.4, stale on how Part VII
uses Theorem 3.1, is amended (R2.0).]

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

[R2.0, Minor 5: round 1's E2 checked four of the ten entries and asserted no value of $\kappa$. E2 now checks all ten
against sympy's exact integrals and quadrature, and asserts $\kappa(\frac52,\frac72)$ against a direct quadrature of the
Gram matrix in $s$ and against the verifier's $7.6546\times10^{-4}$.]

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

[R2.0, nit: $R_P\ge4r_2$ is taken, as the proof of (b) uses: its annuli lie in $\{\chi_1 = 1\}$.]

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
order $a$, $a+2$ and $a+2$; the $B$ terms likewise, and the $(C,D)$ terms are of order $a+3$. The components $\hat
x_i\hat x_j$ lie in $C^\infty(\bar X)$. So (1.1) holds with $C_P\epsilon$ in place of $\epsilon$, and with
$C_\beta\epsilon$ at all orders.

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

[R2.0, Minor 5: round 1's E3 test that $r^{2+2a}\partial^2_\epsilon e_{\alpha\beta}|_0$ is bounded was vacuous: it
substituted $r = e^t$ before testing for $r$. E3 now checks the exact identity $r^{2+2a}\partial^2_\epsilon
e_{\alpha\beta}|_0 = \mu(2w^2-8cw+6c^2)$, $w = (1-a)c-s$, $c = \cos\log r$, $s = \sin\log r$, which is bounded; and it
checks the Tangherlini term of the instance pointwise, which round 1's quadrature did not test.]

*Computed* (E3), an instance: $(a,\ell_0) = (\frac52,\frac72)$ and $(\frac72,\frac72)$, $\epsilon = 10^{-2}$, with the
Tangherlini term $\alpha = r^{-2}$, at $R = 10^2,10^3,10^4$. By quadrature, $D_R/(\epsilon R^{\ell_0-a})$ is within a
relative $10^{-2}$ of $2A_a\,\mathrm{dist}(\log R+\phi_a)$ and above $2A_a\kappa$, where $D_R$ is the least-squares
remainder of $r^{\ell_0}\tau$ on $(\frac R2,R)$ against $r^{\ell_0-2}$ and $r^{\ell_0-3}$. Here $\mathrm{dist}(\cdot)$
oscillates with $\log R$ between $\kappa$ and its maximum.

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

**Proposition 4 (gluing to the Myers-Perry data on Hintz's surface, with the error).** Let $\frac32<a\le\ell_0$ and
$k_{\mathrm g} := d_1+2$, the order of the gluing. There are $R_G$, $\epsilon_0$ and $C$ with the following property.
For every perturbation $(\gamma,k)$ of order $a$ and size $\epsilon\le\epsilon_0$, and every $R\ge R_G$, there are $p_R$
and smooth vacuum data $(\hat\gamma_R,\hat k_R)$ on $\Sigma$, equal to $(\gamma,k)$ on $\{r\le R\}$ and to $(\tilde
g_{p_R},\tilde K_{p_R})$ on $\{r\ge4R\}$, with
$$|\Delta p_{R,2}|\le C\epsilon R^{\min(0,2-a)},\qquad|\Delta p_R|\le C\epsilon R^{\min(0,3-a)},\tag{5.2}$$
$$\sup_{R\le r\le4R}\Big(\sum_{|\beta|\le k_{\mathrm g}-1}r^{|\beta|}|\partial^\beta(\hat\gamma_R-\gamma_\lambda)|+
\sum_{|\beta|\le k_{\mathrm g}-2}r^{1+|\beta|}|\partial^\beta(\hat k_R-k_\lambda)|\Big)\le C\epsilon R^{-a}.\tag{5.3}$$

*Proof.* We follow Part V's proof of Theorem 3.1, with $k_{\mathrm g}$ in place of 3 as in Part VII Proposition 2.2 (its
Step 1 allows every order above $\frac n2$), and make six changes. Data with (1.1) have
$|||(\gamma,k)|||_{\min(a,2),k_{\mathrm g}+4}<\infty$.

(1) *The family and the box.* Lemma 4.1's members replace Part V's: (a) gives Lemma 2.2's bounds and (c) gives Corollary
2.4. In Step 2 let $Q$ range over the box $\bar B_R := \{Q:|Q_X-\tilde{\mathfrak q}_X(p_\lambda)|\le r_X\}$, with $r_X
:= C_0\epsilon R^{\min(0,2+d(X)-a)}$ and $C_0 := C_1'+1$. Then $\bar B_R$ lies in the ball of radius $r_V$ once
$\sqrt{15}\,C_0\epsilon_0<r_V$. The five degree-0 radii are $C_0\epsilon R^{\min(0,2-a)}$, and the ten others
$C_0\epsilon R^{\min(0,3-a)}$, the larger. So for $Q\in\bar B_R$, Lemma 4.1 (c) gives $|\Delta p_2|\le\sqrt5LC_0\epsilon
R^{\min(0,2-a)}$ and $|\Delta p|\le\sqrt{15}LC_0\epsilon R^{\min(0,3-a)}$, where $\Delta p := p(Q)-p_\lambda$.

(2) *The source in relative form.* Write $a_\sigma := \sigma_R(\gamma,k)$ and $b_Q := \sigma_R(\tilde g_{p(Q)}, \tilde
K_{p(Q)})$ on $M = \bar\Gamma(1,4)$. Both are vacuum (Part V Lemma 1.4), and $x_{Q,R} = b_Q+\chi(a_\sigma-b_Q)$. The
constraint map is smooth near flat data and vanishes at $b_Q$. So, as in Part VII Proposition 2.2 (6),
$\|(J,\rho)(x_{Q,R})\|_{C^{k_{\mathrm g}+1}}\le C\|a_\sigma-b_Q\|_{C^{k_{\mathrm g}+3}\times C^{k_{\mathrm g}+4}}\le
C\theta_R(Q)$, with
$$\theta_R(Q) := \epsilon R^{-a}+|\Delta p_2|R^{-2}+|\Delta p|R^{-3}\le C(1+C_0)\,\epsilon R^{-a}\tag{5.4}$$
by (1.1), Lemma 4.1 (b) with $(\tilde g_{p_\lambda},\tilde K_{p_\lambda}) = (\gamma_\lambda,k_\lambda)$ on $\{r\ge R\}$,
the scaling $\|\sigma_Ru\|_{C^m(M)}\le C\sup_{R\le r\le4R}\sum_{|\beta|\le m}r^{|\beta|}|\partial^\beta u|$ (one more
power of $r$ for $K$), and (1) (the inequality in (5.4): computed, E4). By Step 1's bound and Lemma 3.2, $\|\delta
x_{Q,R}\|_{C^{k_{\mathrm g}-1}(M)}\le C\|\delta x_{Q,R}\|_{H^{k_{\mathrm g}+2}(M)}\le C\theta_R(Q)$, continuously in
$Q$. So the unscaled $\hat{\mathfrak x}_Q := \sigma_R^{-1}(x_{Q,R}+\delta x_{Q,R})$ satisfies (5.3)'s bound by
$C\theta_R(Q)$ against $(\gamma_\lambda,k_\lambda)$. It is the sum of $\chi$ times the data's deviation, $(1-\chi)$
times the member's, and $\delta x$. Part V's Step 1 hypotheses hold for $R$ large, as $x_{Q,R}$ is within
$CR^{-2}+C\epsilon R^{-a}$ of flat data.

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

[R2.0, nit and Minor 1: as $1+R^{\ell_0-a}\le2R^{\ell_0-a}$ for $R\ge1$ and Proposition 4 needs $R\ge R_G$, the window
is $R_G\le R<(\delta/(2C\epsilon))^{1/(\ell_0-a)}$, nonempty when $2C\epsilon R_G^{\ell_0-a}<\delta$. At $a = \ell_0$ it
is $R_G\le R$ with $\log R<(\delta/(C\epsilon))^2-1$. "Sharp" holds for the examples of Proposition 3, not for every
perturbation.]

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

[R3.0, A: Corollary 4.3 bounds the glued norm by this order from above for every perturbation of order $a$. The order is
attained, with the matching lower bound, for the examples of Proposition 3, and at $a = \ell_0$ the order is
$\epsilon(\log R)^{1/2}$. Read "does no worse than this order for every perturbation of order $a$, and attains it for
the examples" (Minor 1).]

So "Theorem 4 (ii) applies up to the gluing" is false for fixed $\epsilon$ and large $R$ at every
$a\in(\frac32,\ell_0]$. Its uniform form is equivalent to (ii) applied directly, and the class in which Theorem 4 (ii)'s
conclusion is reached, directly or through gluing, is exactly Hintz's class. The development of glued data is not the
perturbation's: on $\{r>R\}$ the data differ, and the late-time solution near the hole depends on them (Part VII finding
(VII1)).

[R2.0, Minor 3: read "the perturbations to which Theorem 4 (ii) applies, directly or through gluing uniformly in $R$,
are exactly those small in Hintz's class". Settling itself is not confined to the class: the examples of Proposition 3
have developments isometric to that of (i) (Remark 3.2).]

*Proof.* (i) is Proposition 1 with Corollary 1.1, and (ii) is Corollary 2.1 with Propositions 3 and 4 and Corollary 4.3.
$\square$

## 7. Findings, labels and sources

(GD1) *The reach of the settling statement.* The paper's "the gluing would at most show that such a perturbation agrees
on a large ball with one to which Theorem 4 (ii) applies" is, in its uniform form, equivalent to (ii) applied to the
perturbation itself (Corollary 2.1). The perturbations so reached are exactly those in Hintz's class.

[R2.0, Minor 3: "so reached" means reached by Theorem 4 (ii), directly or through gluing uniformly in $R$; see the note
to section 0.]

(GD2) *The threshold.* At fixed $\ell_0$ the decay rate decides only above $\ell_0$ (Proposition 1). At every
$a\in(\frac32,\ell_0]$ there are $G$-invariant, pure-gauge vacuum perturbations outside the class (Proposition 3). Over
Theorem 4's $\ell_0\in(3,4)$ every $a>3$ is covered, the five-dimensional counterpart of [Hin26]'s footnote 1 (READ).
The glued norm is $\asymp\epsilon R^{\ell_0-a}$: the lower bound holds for every data set (Proposition 3) and the upper
bound for the gluing (Corollary 4.3).

[R3.0, A: "$\asymp\epsilon R^{\ell_0-a}$" repeats M1's error at $a = \ell_0$, where the order is $\epsilon(\log
R)^{1/2}$ by (4.1) and (5.5), and it overclaims as Minor 1 did. Read: for the examples of Proposition 3, the least norm
of data in the class agreeing on $\{r<R\}$, and the glued norm, are $\asymp\epsilon R^{\ell_0-a}$ for $a<\ell_0$ and
$\asymp\epsilon(\log R)^{1/2}$ at $a = \ell_0$, with $\epsilon\le\epsilon_1$ and $R\ge\max(R_P,R_G)$. For every
perturbation of order $a$ only the upper bound holds (Corollary 4.3).]

[R4.0, nit 2: the two-sided bound for the examples also needs Proposition 4 to apply to them, so their size
$C_P\epsilon\le\epsilon_0$ as well as $\epsilon\le\epsilon_1$. And "the least norm of data in the class agreeing on
$\{r<R\}$" is the infimum $N_R$ of Definition 1.4.]

[R2.0, Minor 2: for that $\ell_0$, with the data of (i), $\lambda_1$ and $\delta$ taken for it, $\epsilon$ below
$\delta/(C_1(1+(a-\ell_0)^{-1/2}))$, and the rate $t_*^{-2-\epsilon'}$, $\epsilon'<\epsilon_K<\ell_0-3$ (Corollary
1.1).]

(GD3) *The gluing family.* The Myers-Perry data on Part V's Kerr-Schild slices $\{y^0 = 0\}$ differ from Tangherlini's
data on Hintz's surface by $\nabla^2f$ in the second fundamental form, of trace $2\mu_{\mathrm{end}}r^{-3}$ (Lemma 4.1
(d)). Gluing to Part V's members therefore leaves an $O(\mu_{\mathrm{end}})$ coefficient of $\rho^3$ in $k$, and the
glued data are not small in the class even at $\epsilon = 0$. The family must be taken on Hintz's surface (Lemma 4.1),
as Part VII Proposition 2.2 does with Tangherlini in the class. The paper's "can be glued far out to such a metric" is
true with this family, whose charge map Lemma 4.1 (c) shows to be a local diffeomorphism.

[R2.0, nit: "differ by $\nabla^2f$" means $\tilde K_p-K_p = \nabla^2f+\rho^4C^\infty$ at the same $p$, and
$K_{p_\lambda}-k^{m_\lambda} = -\nabla^2f+\rho^5C^\infty$. And GD3 is no defect of Part V (note to section 0; R2.0).]

(GD4) *Decoupling.* The energy and momentum of the family depend on mass and boost alone (Lemma 4.1 (c)). Without this,
mass and boost would be bounded only as the degree-1 charges are, by $\epsilon R^{\min(0,3-a)}$. The term $|\Delta
p_2|R^{\ell_0-2}$ would then exceed $\epsilon R^{\ell_0-a}$ for $2<a\le3$, which E4's control exhibits.

(GD5) *The record's bump estimate.* `checks/support8b.py` M3 computes one term of the upper bound at $a = 3$. The lower
bound, which decides the item, is Proposition 3.

*Labels.* Lemma 1.2, Propositions 1-4, Corollaries 1.1, 2.1, 4.3, Lemmas 3.1, 4.1, 4.2 and Theorem 5: proved, from the
inputs below. Every integral, exponent, identity and constant they use is computed in `checks/gluedecay5.py` E1-E6.
Brouwer's fixed point theorem and the inverse function theorem are cited, as in Part V.

[R2.0, Minor 4: "every ... constant ... computed" overstates. Of the constants only $\kappa$ is computed (E2), and with
it $c_P$. $C_1$, $C_1'$, $C_0$, $C_P$, $R_P$, $R_G$, $L$, $\epsilon_0$, $\epsilon_1$ and the $C$ of Corollary 4.3 are
proved to exist, not computed.]

*Sources.* READ: [Hin26] (arXiv:2606.28253v2) pp. 2 ((1.4)-(1.5), footnote 1), 47 (Definition 2.6 (2)), 48 (Definition
2.8, (2.3)), 318 (Theorem 13.1, (13.1b), footnote 146), read 2026-11-06. Nothing new from [CD03]: its estimates enter as
`proof5/PART-V-GLUING.md` states them (Step 1 with Proposition G.1's bound, Lemma 3.2, Steps 2-5, Lemma 1.2 with
(1.1)-(1.2), Proposition 1.3, Lemma 1.4, Definition 2.1, Lemma 2.2, Proposition 2.3, Corollary 2.4), together with
`proof5/PART-VII-ASSEMBLY.md` (Theorem 0.2, Lemma 0.1, Lemma 2.1, Proposition 2.2 (6), finding (VII1)). Also
`proof5/PART-III-B-FAMILY.md` ((3.3), Lemma 3.5 (a), Proposition 3.4), `proof5/PART-III-A-PREREQ.md` section 1.1, and
`checks/mpdata5.py` B2-B3. No file outside `research/warp-drive/` is cited.

    python3 checks/gluedecay5.py   (about ninety seconds; output in checks/gluedecay5.out)

## 8. Proposed replacement for the paper

[R2.0: section 8.2 is the current proposal. Section 8.1, round 1's, is kept as written and is superseded.]

[R3.0: section 8.3 is now the current proposal; section 8.2, round 2's, is kept as written and is superseded.]

[R4.0: section 8.4 is now the current proposal; section 8.3, round 3's, is kept as written and is superseded.]

[R5.0: section 8.5 is now the current proposal; section 8.4, round 4's, is kept as written and is superseded.]

### 8.1 Round 1 (superseded)

`paper/RESPONSE-HL-5D.md`, section 8.7, lines 1141-1149, from "a translation, and the structural step" to the end of the
paragraph. The old text occurs exactly once (computed, E6); the paper is not edited here.

Old (round 1):

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

New (round 1, superseded):

```text
a translation, and the structural step that a Cartesian derivative gains a power of ρ). It also contains every
perturbation conormal of an order a > ℓ0, with |∂^k h| ≤ ε r^(−a−k) in the metric and ε r^(−a−1−k) in the second
fundamental form. Such a perturbation has no terms of orders r^(−2) and r^(−3), and its norm is at most C ε (1 + (a −
ℓ0)^(−1/2)). Since Theorem 4 holds for every ℓ0 ∈ (3, 4), taking ℓ0 ∈ (3, min(a, 4)) covers every such perturbation with
a > 3 (proved: supplement `docket68/n1star/GLUEDECAY5.md` Proposition 1 and Corollary 1.1). For 3/2 < a ≤ ℓ0 the decay
rate does not decide, and gluing does not enlarge the class. A perturbation agrees on every ball r < R with data to
which Theorem 4 (ii) applies, uniformly in R in every norm of the class, if and only if Theorem 4 (ii) applies to the
perturbation itself: the least norm of data in the class that agree with it on r < R increases with R, to its own norm
if it lies in the class, and without bound if it does not lie in the class at the norm's regularity (proved:
GLUEDECAY5.md Proposition 2 and Corollary 2.1). At every such a there are vacuum perturbations of size ε outside the
class, the data pulled back by the radial diffeomorphism x ↦ (1 + ε r^(−a) cos log r) x far out, which are pure gauge
and G-invariant. For these, every data set in the class that agrees with them on r < R has norm at least c ε R^(ℓ0−a),
with c > 0, and at least c ε (log R)^(1/2) at a = ℓ0 (proved: GLUEDECAY5.md Proposition 3). [CD03]'s gluing on the
annulus R < r < 4R, which in five dimensions needs no parity condition at these rates (section 8.6; supplement sections
10.63 and 10.66), attains this order when its target is the family of translated, rotated and boosted Myers–Perry data
on Hintz's surface itself: the glued data then have norm at most C ε R^(ℓ0−a) (proved: GLUEDECAY5.md Proposition 4 and
Corollary 4.3, with the gluing's estimates as supplement `docket68/n1star/proof5/PART-V-GLUING.md` and
`PART-VII-ASSEMBLY.md` Proposition 2.2 state them; the data on PART-V-GLUING.md's Kerr–Schild slices differ from that
family by a fixed term of order r^(−3) in the second fundamental form). So for fixed ε the glued data are small enough
for Theorem 4 (ii) only for R up to a multiple of (δ/ε)^(1/(ℓ0−a)), and this is sharp. Their development is not the
perturbation's: the solution near the hole at late times depends on the data near infinity. The class in which Theorem 4
(ii)'s conclusion is reached, directly or through gluing, is exactly Hintz's class (computed: every integral, exponent
and constant, `docket68/n1star/checks/gluedecay5.py` E1–E6).
```

[R2.0: superseded. At $a = \ell_0$ its upper bound "C ε R^(ℓ0−a)" contradicts its own lower bound (M1); "only ... and
this is sharp" (Minor 1), the dropped dependence on ℓ0 (Minor 2), "the class in which ... is reached" (Minor 3) and
"every integral, exponent and constant" (Minor 4) overclaim; and its first line keeps the Kerr–Schild slices of
:1138-1141 (Minor 6).]

### 8.2 Round 2 (superseded by 8.3)

Two blocks of `paper/RESPONSE-HL-5D.md`, section 8.7, applied together: (a) lines 1138-1140, from "theorem applies
directly" to "a boost and"; (b) lines 1141-1149, round 1's old text, to the end of the paragraph. Each old block occurs
exactly once, and (a) is immediately followed by (b) (computed, E6). The paper is not edited here. The text writes η for
this note's ε, the size of the perturbation, since Theorem 4 already uses ε for its rate.

Old (round 2, a):

```text
theorem applies directly to perturbations of these data in his data class, which contains the data of every nearby
translated, rotated and boosted Myers–Perry metric (computed: their Cartesian components lie in ρ²C^∞ and ρ³C^∞ of the
radial compactification, `docket68/n1star/checks/mpdata5.py`, exact series at three points of S³ with spins, a boost and
```

New (round 2, a):

```text
theorem applies directly to perturbations of these data in his data class, which contains the data that every nearby
translated, rotated and boosted Myers–Perry metric induces on Hintz's surface (computed: on Kerr–Schild slices their
Cartesian components lie in ρ²C^∞ and ρ³C^∞ of the radial compactification, `docket68/n1star/checks/mpdata5.py`, exact
series at three points of S³ with spins, a boost and
```

Old (round 2, b):

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

New (round 2, b):

```text
a translation, and the structural step that a Cartesian derivative gains a power of ρ; on Hintz's surface the same holds
by the graph map, proved in supplement `docket68/n1star/GLUEDECAY5.md` Lemma 4.1 (a)). The class also contains every
perturbation conormal of an order a > ℓ0, with |∂^k h| ≤ η r^(−a−k) in the metric and η r^(−a−1−k) in the second
fundamental form. Such a perturbation has no terms of orders r^(−2) and r^(−3), and its norm is at most C η (1 + (a −
ℓ0)^(−1/2)). Theorem 4 holds for every ℓ0 ∈ (3, 4), with the data of (i), λ1 and δ taken for that ℓ0. So with ℓ0 ∈ (3,
min(a, 4)) its (ii) covers every such perturbation with a > 3 and η below δ/(C (1 + (a − ℓ0)^(−1/2))), at the rate
t*^(−2−ε) with ε < ε_K < ℓ0 − 3 (proved: GLUEDECAY5.md Proposition 1 and Corollary 1.1). For 3/2 < a ≤ ℓ0 the decay rate
does not decide, and gluing does not enlarge the class. A perturbation agrees on every ball r < R with data to which
Theorem 4 (ii) applies, uniformly in R in every norm of the class, if and only if Theorem 4 (ii) applies to the
perturbation itself. Indeed the infimum of the norms of data in the class that agree with it on r < R is nondecreasing
in R, and tends to its own norm if it lies in the class and to infinity if it does not lie in the class at the norm's
regularity (proved: GLUEDECAY5.md Proposition 2 and Corollary 2.1). At every such a and every η ≤ η1 there are vacuum
perturbations of size C_P η outside the class: the data of (i) pulled back by the radial diffeomorphism x ↦ (1 + η
r^(−a) cos log r) x far out, which are pure gauge and G-invariant. For R ≥ R_P, every data set in the class that agrees
with one of them on r < R has norm at least c η R^(ℓ0−a), with c > 0, and at least c η (log2(R/R_P))^(1/2) at a = ℓ0
(proved: GLUEDECAY5.md Proposition 3). [CD03]'s gluing on the annulus R < r < 4R, which in five dimensions needs no
parity condition at these rates (section 8.6; supplement sections 10.63 and 10.66), attains this order when its target
is the family of translated, rotated and boosted Myers–Perry data on Hintz's surface. For η ≤ η0 and R ≥ R_G the glued
data have norm at most C η (1 + R^(ℓ0−a)), and C η (1 + log R)^(1/2) at a = ℓ0 (proved: GLUEDECAY5.md Proposition 4 and
Corollary 4.3, with the gluing's estimates as supplement `docket68/n1star/proof5/PART-V-GLUING.md` and
`PART-VII-ASSEMBLY.md` Proposition 2.2 state them; the Myers–Perry data on PART-V-GLUING.md's Kerr–Schild slices differ
from that family by a fixed term of order r^(−3) in the second fundamental form). So for a < ℓ0 the glued data are
guaranteed small enough for Theorem 4 (ii) for R from R_G up to a multiple of (δ/η)^(1/(ℓ0−a)), a range that is nonempty
for η small, and for the pulled-back examples no data in the class that agree with them on r < R do better. The
development of the glued data is not the perturbation's: the solution near the hole at late times depends on the data
near infinity. The perturbations to which Theorem 4 (ii) applies, directly or through gluing uniformly in R, are exactly
those small in Hintz's class; the pulled-back examples lie outside it, and their developments are isometric to that of
the data of (i) (computed: the integrals, the exponents, the fluxes and the distance behind c,
`docket68/n1star/checks/gluedecay5.py` E1–E6; the constants C, C_P, R_P, R_G, η0 and η1 are proved to exist, not
computed).
```

[R3.0: superseded. Applied verbatim it would drop section 8's only citation of support8b.py M3, leaving Appendix C's row
for the bump's cost without a claim, and it would leave gluedecay5.py and this note out of section 9, Appendix A,
Appendix C and Appendix D. Its η also denotes the Minkowski metric elsewhere in the paper, and its first line left a
short line at the join. Section 8.3 repairs these.]

### 8.3 Round 3 (superseded by 8.4)

Eight blocks of `paper/RESPONSE-HL-5D.md`, to be applied together. (a) and (b) are one paragraph of section 8.7, wrapped
together, so the join leaves no short line; the other six are the companion edits that keep the paper's apparatus
consistent: section 9's computational-support list, Appendix A, Appendix C (the source map) and Appendix D (the run
list, the imports and the md5 table). Each old block occurs exactly once, the blocks are disjoint, and (a) is
immediately followed by (b). Applied to a copy of the paper, section 8.7 still cites support8b.py M3 (Appendix C's row
for the bump's cost keeps its claim) and every place carries gluedecay5.py and this note (computed, E6). The paper is
not edited here. The size of the perturbation is written ϰ, a letter the paper does not use; η is its Minkowski metric
(:180, :1063, :2115), and the rate's ε is not written, so :1133's ε for a deviation keeps its one meaning in the
paragraph. In (h), the md5 of gluedecay5.py, gluedecay5.out and PART-V-GLUING.md are those of this round's files.
GLUEDECAY5.md's own row carries zeros, since it cannot record its own md5: `python3 response5.py --update-md5` fills it,
and the others if they change, after seating (R9).

(a) section 8.7, lines 1138-1140.

Old (round 3, a):

```text
theorem applies directly to perturbations of these data in his data class, which contains the data of every nearby
translated, rotated and boosted Myers–Perry metric (computed: their Cartesian components lie in ρ²C^∞ and ρ³C^∞ of the
radial compactification, `docket68/n1star/checks/mpdata5.py`, exact series at three points of S³ with spins, a boost and
```

New (round 3, a):

```text
theorem applies directly to perturbations of these data in his data class, which contains the data that every nearby
translated, rotated and boosted Myers–Perry metric induces on Hintz's surface (computed: on Kerr–Schild slices their
Cartesian components lie in ρ²C^∞ and ρ³C^∞ of the radial compactification, `docket68/n1star/checks/mpdata5.py`, exact
series at three points of S³ with spins, a boost and a translation, and the structural step that a Cartesian derivative
```

(b) section 8.7, lines 1141-1149, to the end of the paragraph.

Old (round 3, b):

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

New (round 3, b):

```text
gains a power of ρ; on Hintz's surface the same holds by the graph map, proved in supplement
`docket68/n1star/GLUEDECAY5.md` Lemma 4.1 (a)). The class also contains every perturbation conormal of an order a > ℓ0,
with |∂^k h| ≤ ϰ r^(−a−k) in the metric and ϰ r^(−a−1−k) in the second fundamental form. Such a perturbation has no
terms of orders r^(−2) and r^(−3) in the metric, nor of orders r^(−3) and r^(−4) in the second fundamental form, and its
norm is at most C ϰ (1 + (a − ℓ0)^(−1/2)). Theorem 4 holds for every ℓ0 ∈ (3, 4), with the data of (i), λ1 and δ taken
for that ℓ0. So with ℓ0 ∈ (3, min(a, 4)) its (ii) covers every such perturbation with a > 3 and ϰ below δ/(C (1 + (a −
ℓ0)^(−1/2))), at the rate of Theorem 4, its ε_K then below ℓ0 − 3 (proved: GLUEDECAY5.md Proposition 1 and Corollary
1.1). For 3/2 < a ≤ ℓ0 the decay rate does not decide, and gluing does not enlarge the class. A perturbation agrees on
every ball r < R with data to which Theorem 4 (ii) applies, uniformly in R in every norm of the class, if and only if
Theorem 4 (ii) applies to the perturbation itself. Indeed the infimum of the norms of data in the class that agree with
it on r < R is nondecreasing in R, and tends to its own norm if it lies in the class and to infinity if it does not lie
in the class at the norm's regularity (proved: GLUEDECAY5.md Proposition 2 and Corollary 2.1). At every such a and every
ϰ ≤ ϰ1 there are vacuum perturbations of size C_P ϰ outside the class: the data of (i) pulled back by the radial
diffeomorphism x ↦ (1 + ϰ r^(−a) cos log r) x far out, which are pure gauge and G-invariant. For R ≥ R_P, every data set
in the class that agrees with one of them on r < R has norm at least c ϰ R^(ℓ0−a), with c > 0, and at least c ϰ
(log2(R/R_P))^(1/2) at a = ℓ0 (proved: GLUEDECAY5.md Proposition 3). [CD03]'s gluing on the annulus R < r < 4R, which in
five dimensions needs no parity condition at these rates (section 8.6; supplement sections 10.63 and 10.66), does no
worse when its target is the family of translated, rotated and boosted Myers–Perry data on Hintz's surface: for every
such perturbation, with ϰ ≤ ϰ0 and R ≥ R_G, the glued data have norm at most C ϰ (1 + R^(ℓ0−a)), and C ϰ (1 + log
R)^(1/2) at a = ℓ0. At a = 3 the term from the annulus is the cost R^(ℓ0−3) of a bump of amplitude R^(−3) at radius R,
`docket68/n1star/checks/support8b.py` M3 (proved: GLUEDECAY5.md Proposition 4 and Corollary 4.3, with the gluing's
estimates as supplement `docket68/n1star/proof5/PART-V-GLUING.md` and `PART-VII-ASSEMBLY.md` Proposition 2.2 state them;
the Myers–Perry data on PART-V-GLUING.md's Kerr–Schild slices differ from that family by a fixed term of order r^(−3) in
the second fundamental form). So for a < ℓ0 the glued data are guaranteed small enough for Theorem 4 (ii) for R from R_G
up to a multiple of (δ/ϰ)^(1/(ℓ0−a)), a range that is nonempty for ϰ small, and for the pulled-back examples no data in
the class that agree with them on r < R do better. The development of the glued data is not the perturbation's: the
solution near the hole at late times depends on the data near infinity. The perturbations to which Theorem 4 (ii)
applies, directly or through gluing uniformly in R, are exactly those small in Hintz's class; the pulled-back examples
lie outside it, and their developments are isometric to that of the data of (i) (computed: the integrals, the exponents,
the fluxes and the distance behind c, `docket68/n1star/checks/gluedecay5.py` E1–E6; the constants C, C_P, R_P, R_G, ϰ0
and ϰ1 are proved to exist, not computed).
```

(c) section 9, the computational-support item, lines 1552-1564.

Old (round 3, c):

```text
  `checks/support8b.py`, `checks/support8c.py`, `checks/flux5.py`, `checks/mpdata5.py`, `checks/kirecon5.py`,
  `checks/hclass5.py`, `checks/re813.py`, `checks/eindcert5.py`, `checks/vii5census.py`, `checks/vii5read.py` and
  `checks/census9.py`, and for section 9 `checks/support9.py`, `checks/charge5.py`, `checks/eqlayer5.py`,
  `checks/e2lower5.py`, `checks/twodomainx5.py`, `checks/level2loop5.py`, `checks/lambdacount5.py`,
  `checks/twodomain5.py`, `checks/r0census5.py` and `checks/excise5.py`. A census of the deduced claims in sections 1–9
  (103 claims, of which 27 named no program for the step) left none without one but the analytic estimates named below,
  the settling write-out and one step resting on a reading at source; where a check stops short of the step (an order λ¹
  structure computed to order λ² in place of every order, a scan to a finite l) its entry in Appendix A says so.
  The analytic estimates themselves (the energy estimate and the bootstrap's analysis, the mollifier's Bernstein- and
  Friedrichs-type bounds, the Nash–Moser scheme, the settling write-out) are proved in the supplement and read by
  independent verifiers, not computed (deduced). The two-dust background's convergence on a rectangle reaching Σ_τ0 is
  computed for one choice of the outgoing family's characteristic data, those data themselves being among the items left
  open above.
```

New (round 3, c):

```text
  `checks/support8b.py`, `checks/support8c.py`, `checks/flux5.py`, `checks/mpdata5.py`, `checks/gluedecay5.py`,
  `checks/kirecon5.py`, `checks/hclass5.py`, `checks/re813.py`, `checks/eindcert5.py`, `checks/vii5census.py`,
  `checks/vii5read.py` and `checks/census9.py`, and for section 9 `checks/support9.py`, `checks/charge5.py`,
  `checks/eqlayer5.py`, `checks/e2lower5.py`, `checks/twodomainx5.py`, `checks/level2loop5.py`,
  `checks/lambdacount5.py`, `checks/twodomain5.py`, `checks/r0census5.py` and `checks/excise5.py`. A census of the
  deduced claims in sections 1–9 (103 claims, of which 27 named no program for the step) left none without one but the
  analytic estimates named below, the settling write-out and one step resting on a reading at source; where a check
  stops short of the step (an order λ¹ structure computed to order λ² in place of every order, a scan to a finite l) its
  entry in Appendix A says so. The analytic estimates themselves (the energy estimate and the bootstrap's analysis, the
  mollifier's Bernstein- and Friedrichs-type bounds, the Nash–Moser scheme, the settling write-out) are proved in the
  supplement and read by independent verifiers, not computed (deduced). The two-dust background's convergence on a
  rectangle reaching Σ_τ0 is computed for one choice of the outgoing family's characteristic data, those data themselves
  being among the items left open above.
```

(d) Appendix A, the entries of mpdata5.py and flux5.py, lines 2180-2190, and a new entry.

Old (round 3, d):

```text
- `checks/mpdata5.py` B1–B4: the data of translated, rotated and boosted Myers–Perry metrics lie in the class of
  supplement Part VII Lemma 0.1, ρ²C^∞ and ρ³C^∞ of the radial compactification. Controls: a mass term falling as ρ (B1,
  B4); a split-signature form, which vanishes on the sphere (B2); the projection term dropped (B3). Exact series; about
  four minutes.
- `checks/flux5.py` F1–F4: the flux 6π²m of the Kerr–Schild slice (F1–F2), the glued mass bound's ingredients (F3: R⁶
  q_2 = −10294529/36000, the annulus volume 255π²R⁴/2, |δm| ≤ C η (R² + 1)/(6π²R² − C) for C < 6π²R²) and step (6)'s
  bilinear difference bound (F4: for generic data of size B and a deviation of size ε, both at the annulus scaling, the
  remainder's difference has no term linear in the data, its quadratic part is R⁻⁶ times ε B and ε² and its cubic part
  R⁻⁸ times ε B², ε² B and ε³, so it is at most C ε (|B| + ε) R⁻⁶ + C ε R⁻⁸) (supplement Part VII Lemma 2.1 (c),
  Proposition 2.2 step (6)). Controls: the flux with the trace term's sign reversed; the curvature without its Γ·Γ terms
  (F3); the remainder without its linear part (F4). Exact; about twenty minutes.
```

New (round 3, d):

```text
- `checks/mpdata5.py` B1–B4: the data of translated, rotated and boosted Myers–Perry metrics on Kerr–Schild slices lie
  in the class of supplement Part VII Lemma 0.1, ρ²C^∞ and ρ³C^∞ of the radial compactification; on Hintz's surface the
  same holds by the graph map (supplement GLUEDECAY5.md Lemma 4.1 (a)). Controls: a mass term falling as ρ (B1, B4); a
  split-signature form, which vanishes on the sphere (B2); the projection term dropped (B3). Exact series; about four
  minutes.
- `checks/flux5.py` F1–F4: the flux 6π²m of the Kerr–Schild slice (F1–F2), the glued mass bound's ingredients (F3: R⁶
  q_2 = −10294529/36000, the annulus volume 255π²R⁴/2, |δm| ≤ C η (R² + 1)/(6π²R² − C) for C < 6π²R²) and step (6)'s
  bilinear difference bound (F4: for generic data of size B and a deviation of size ε, both at the annulus scaling, the
  remainder's difference has no term linear in the data, its quadratic part is R⁻⁶ times ε B and ε² and its cubic part
  R⁻⁸ times ε B², ε² B and ε³, so it is at most C ε (|B| + ε) R⁻⁶ + C ε R⁻⁸) (supplement Part VII Lemma 2.1 (c),
  Proposition 2.2 step (6)). Controls: the flux with the trace term's sign reversed; the curvature without its Γ·Γ terms
  (F3); the remainder without its linear part (F4). Exact; about twenty minutes.
- `checks/gluedecay5.py` E1–E6: section 8.7's reach of Theorem 4 (ii), directly or through gluing (supplement
  GLUEDECAY5.md). E1, the weighted integrals: a conormal perturbation of order a has its remainder in r^(−ℓ0) H_b
  exactly when a > ℓ0, logarithmically divergent at a = ℓ0. E2, the distance κ(a, ℓ0) > 0 behind the lower bound, from
  the Gram matrix in closed form, certified by interval arithmetic on a grid of a and ℓ0; κ(5/2, 7/2) = 7.6546 × 10⁻⁴
  against a direct quadrature. E3, the pulled-back examples: the pull-back of a radial tensor, the exact trace, the
  Tangherlini term, and an instance of the lower bound c ϰ R^(ℓ0−a) by quadrature. E4, the exact fluxes 6π², 3π², 3π²/2
  and 2π² of order-a profiles, and the exponents of the gluing's error terms and of the glued norm. E5, the spin and a
  translation entering the metric at r^(−3), the Hessian of Hintz's height function carrying no momentum or angular
  momentum, and its trace 2μ r^(−3). E6, these replacements, applied to a copy of the paper. Controls: nineteen mutants
  of the program, among them the Lebesgue density, the class profile without its oscillation, the three-dimensional
  coefficient 3 − a, mass and boost not decoupled, and a mass change in place of the spins. Exact, with κ certified and
  the instance by quadrature; about ninety seconds.
```

(e) Appendix C (the source map), line 2604.

Old (round 3, e):

```text
| section 8.7: Myers–Perry data in the class | `docket68/n1star/checks/mpdata5.py` B1–B4 |
```

New (round 3, e):

```text
| section 8.7: Myers–Perry data in the class, on Kerr–Schild slices | `docket68/n1star/checks/mpdata5.py` B1–B4 |
| section 8.7: Myers–Perry data on Hintz's surface; the class above ℓ0 | supplement GLUEDECAY5.md, sections 2, 5 |
| section 8.7: uniform gluing is membership; the examples; the glued norm | supplement GLUEDECAY5.md, sections 3–5 |
| section 8.7: their integrals, exponents, fluxes and κ | `docket68/n1star/checks/gluedecay5.py` E1–E6 |
```

(f) Appendix D, the run list, line 2732.

Old (round 3, f):

```text
    python3 checks/flux5.py                              # about twenty minutes
```

New (round 3, f):

```text
    python3 checks/flux5.py                              # about twenty minutes
    python3 checks/gluedecay5.py                         # about ninety seconds
```

(g) Appendix D, the import paragraph, lines 2653-2661.

Old (round 3, g):

```text
`lead5.py`, `past5.py` and `mass5.py`, `checks/support8b.py` imports `checks/mpdata5.py`, `checks/ledger5.py` imports
`checks/support5.py`, `checks/support5c.py` imports `horizon5.py` and `lead5.py`, `checks/lambdacount5.py` imports
`checks/level2loop5.py`, `checks/support8c.py` imports `damping5.py`, `hthresh5.py`, `iplus5.py`, `lhor5.py`, `sbar5.py`
and `scri5.py`, `checks/gauge5.py` imports `data5.py`, `lead5.py` and `paper/response5.py`, `checks/excise5.py` imports
`growth5.py`, `checks/stage5.py` imports `lead5.py`, `checks/stage5b.py` imports `lead5.py` and `checks/stage5.py`,
`secondzero5.py` and `resid5.py` import `bondisph5.py`, which imports `sectexp5.py`, `resid5.py` and `szrun5.py` import
`dnsolve5.py`, `checks/support9.py` imports `lead5.py`, `checks/charge5.py` imports `checks/prop31loss5.py` and
`checks/dg5.py`, `checks/twodomainx5.py` imports `checks/twodomain5.py`, `checks/vii5read.py` imports
`checks/vii5census.py`; the others import nothing from the research tree:
```

New (round 3, g):

```text
`lead5.py`, `past5.py` and `mass5.py`, `checks/support8b.py` and `checks/gluedecay5.py` import `checks/mpdata5.py`,
`checks/ledger5.py` imports `checks/support5.py`, `checks/support5c.py` imports `horizon5.py` and `lead5.py`,
`checks/lambdacount5.py` imports `checks/level2loop5.py`, `checks/support8c.py` imports `damping5.py`, `hthresh5.py`,
`iplus5.py`, `lhor5.py`, `sbar5.py` and `scri5.py`, `checks/gauge5.py` imports `data5.py`, `lead5.py` and
`paper/response5.py`, `checks/excise5.py` imports `growth5.py`, `checks/stage5.py` imports `lead5.py`,
`checks/stage5b.py` imports `lead5.py` and `checks/stage5.py`, `secondzero5.py` and `resid5.py` import `bondisph5.py`,
which imports `sectexp5.py`, `resid5.py` and `szrun5.py` import `dnsolve5.py`, `checks/support9.py` imports `lead5.py`,
`checks/charge5.py` imports `checks/prop31loss5.py` and `checks/dg5.py`, `checks/twodomainx5.py` imports
`checks/twodomain5.py`, `checks/vii5read.py` imports `checks/vii5census.py`; the others import nothing from the research
tree:
```

(h) Appendix D, the md5 table, line 2913.

Old (round 3, h):

```text
| `docket68/n1star/checks/flux5.out` | `75c4e28d932ef8895941c219012badf7` |
```

New (round 3, h):

```text
| `docket68/n1star/checks/flux5.out` | `75c4e28d932ef8895941c219012badf7` |
| `docket68/n1star/checks/gluedecay5.py` | `5419ce724e8f46273130375f29e02ede` |
| `docket68/n1star/checks/gluedecay5.out` | `1ff0477a7b1c4008f114e13d8b7bb342` |
| `docket68/n1star/GLUEDECAY5.md` | `00000000000000000000000000000000` |
| `docket68/n1star/proof5/PART-V-GLUING.md` | `df25f8231e6af8cc1cfd08069d2700aa` |
```

[R4.0: superseded. Its (d) said that E1 finds a perturbation's remainder in the class exactly when a > ℓ0, which is
false in the 'only when' direction; E1 computes the integral of the bound. Its E6 failed after seating, so the pinned
.out could not be reproduced. Its (b) placed '(proved: ...)' after the M3 sentence, and its (e) cited the note as
'supplement' and named κ, which section 8.7 does not define. Its size letter ϰ is a glyph variant of κ, the paper's
second fundamental form at :605-606. Section 8.4 repairs these.]

### 8.4 Round 4 (superseded by 8.5)

Eight blocks of `paper/RESPONSE-HL-5D.md`, to be applied together, as in section 8.3 but for round 4's repairs: (b)
labels the glued-norm bound (proved) and M3 (computed) where each stands, (d)'s entry for E1 states the bound's
membership and its entry for E6 the two states, (e) cites the note by path and names no κ, and the size of the
perturbation is Ξ, a letter the paper does not use in either case (ξ occurs only in two quotations, :538 and :582, as a
frequency). Each old block occurs exactly once, the blocks are disjoint, (a) is immediately followed by (b), and with
all eight applied to a copy of the paper every place carries the change (computed, E6).

*Seating, and the re-pin.* E6 accepts both states of the paper and names the one it found. So after the blocks are
seated, run from `docket68/n1star/`: `python3 checks/gluedecay5.py > checks/gluedecay5.out`. It exits 0, and its E6 line
now names the seated state, so the .out changes. Then run `cd ../../paper && python3 response5.py --update-md5`, which
rewrites the md5 column. That fills (h)'s zero row for GLUEDECAY5.md, refreshes gluedecay5.out's row, and refreshes the
18 rows the round-3 reader found stale from other workstreams. R9 then passes. In (h), the md5 of gluedecay5.py,
gluedecay5.out and PART-V-GLUING.md are those of this round's files before seating.

(a) section 8.7, lines 1138-1140.

Old (round 4, a):

```text
theorem applies directly to perturbations of these data in his data class, which contains the data of every nearby
translated, rotated and boosted Myers–Perry metric (computed: their Cartesian components lie in ρ²C^∞ and ρ³C^∞ of the
radial compactification, `docket68/n1star/checks/mpdata5.py`, exact series at three points of S³ with spins, a boost and
```

New (round 4, a):

```text
theorem applies directly to perturbations of these data in his data class, which contains the data that every nearby
translated, rotated and boosted Myers–Perry metric induces on Hintz's surface (computed: on Kerr–Schild slices their
Cartesian components lie in ρ²C^∞ and ρ³C^∞ of the radial compactification, `docket68/n1star/checks/mpdata5.py`, exact
series at three points of S³ with spins, a boost and a translation, and the structural step that a Cartesian derivative
```

(b) section 8.7, lines 1141-1149, to the end of the paragraph.

Old (round 4, b):

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

New (round 4, b):

```text
gains a power of ρ; on Hintz's surface the same holds by the graph map, proved in supplement
`docket68/n1star/GLUEDECAY5.md` Lemma 4.1 (a)). The class also contains every perturbation conormal of an order a > ℓ0,
with |∂^k h| ≤ Ξ r^(−a−k) in the metric and Ξ r^(−a−1−k) in the second fundamental form. Such a perturbation has no
terms of orders r^(−2) and r^(−3) in the metric, nor of orders r^(−3) and r^(−4) in the second fundamental form, and its
norm is at most C Ξ (1 + (a − ℓ0)^(−1/2)). Theorem 4 holds for every ℓ0 ∈ (3, 4), with the data of (i), λ1 and δ taken
for that ℓ0. So with ℓ0 ∈ (3, min(a, 4)) its (ii) covers every such perturbation with a > 3 and Ξ below δ/(C (1 + (a −
ℓ0)^(−1/2))), at the rate of Theorem 4, its ε_K then below ℓ0 − 3 (proved: GLUEDECAY5.md Proposition 1 and Corollary
1.1). For 3/2 < a ≤ ℓ0 the decay rate does not decide, and gluing does not enlarge the class. A perturbation agrees on
every ball r < R with data to which Theorem 4 (ii) applies, uniformly in R in every norm of the class, if and only if
Theorem 4 (ii) applies to the perturbation itself. Indeed the infimum of the norms of data in the class that agree with
it on r < R is nondecreasing in R, and tends to its own norm if it lies in the class and to infinity if it does not lie
in the class at the norm's regularity (proved: GLUEDECAY5.md Proposition 2 and Corollary 2.1). At every such a and every
Ξ ≤ Ξ1 there are vacuum perturbations of size C_P Ξ outside the class: the data of (i) pulled back by the radial
diffeomorphism x ↦ (1 + Ξ r^(−a) cos log r) x far out, which are pure gauge and G-invariant. For R ≥ R_P, every data set
in the class that agrees with one of them on r < R has norm at least c Ξ R^(ℓ0−a), with c > 0, and at least c Ξ
(log2(R/R_P))^(1/2) at a = ℓ0 (proved: GLUEDECAY5.md Proposition 3). [CD03]'s gluing on the annulus R < r < 4R, which in
five dimensions needs no parity condition at these rates (section 8.6; supplement sections 10.63 and 10.66), does no
worse when its target is the family of translated, rotated and boosted Myers–Perry data on Hintz's surface: for every
such perturbation, with Ξ ≤ Ξ0 and R ≥ R_G, the glued data have norm at most C Ξ (1 + R^(ℓ0−a)), and C Ξ (1 + log
R)^(1/2) at a = ℓ0 (proved: GLUEDECAY5.md Proposition 4 and Corollary 4.3, with the gluing's estimates as supplement
`docket68/n1star/proof5/PART-V-GLUING.md` and `PART-VII-ASSEMBLY.md` Proposition 2.2 state them; the Myers–Perry data on
PART-V-GLUING.md's Kerr–Schild slices differ from that family by a fixed term of order r^(−3) in the second fundamental
form). At a = 3 the term from the annulus is the cost R^(ℓ0−3) of a bump of amplitude R^(−3) at radius R (computed:
`docket68/n1star/checks/support8b.py` M3). So for a < ℓ0 the glued data are guaranteed small enough for Theorem 4 (ii)
for R from R_G up to a multiple of (δ/Ξ)^(1/(ℓ0−a)), a range that is nonempty for Ξ small, and for the pulled-back
examples no data in the class that agree with them on r < R do better. The development of the glued data is not the
perturbation's: the solution near the hole at late times depends on the data near infinity. The perturbations to which
Theorem 4 (ii) applies, directly or through gluing uniformly in R, are exactly those small in Hintz's class; the
pulled-back examples lie outside it, and their developments are isometric to that of the data of (i) (computed: the
integrals, the exponents, the fluxes and the distance behind c, `docket68/n1star/checks/gluedecay5.py` E1–E6; the
constants C, C_P, R_P, R_G, Ξ0 and Ξ1 are proved to exist, not computed).
```

(c) section 9, the computational-support item, lines 1552-1564.

Old (round 4, c):

```text
  `checks/support8b.py`, `checks/support8c.py`, `checks/flux5.py`, `checks/mpdata5.py`, `checks/kirecon5.py`,
  `checks/hclass5.py`, `checks/re813.py`, `checks/eindcert5.py`, `checks/vii5census.py`, `checks/vii5read.py` and
  `checks/census9.py`, and for section 9 `checks/support9.py`, `checks/charge5.py`, `checks/eqlayer5.py`,
  `checks/e2lower5.py`, `checks/twodomainx5.py`, `checks/level2loop5.py`, `checks/lambdacount5.py`,
  `checks/twodomain5.py`, `checks/r0census5.py` and `checks/excise5.py`. A census of the deduced claims in sections 1–9
  (103 claims, of which 27 named no program for the step) left none without one but the analytic estimates named below,
  the settling write-out and one step resting on a reading at source; where a check stops short of the step (an order λ¹
  structure computed to order λ² in place of every order, a scan to a finite l) its entry in Appendix A says so.
  The analytic estimates themselves (the energy estimate and the bootstrap's analysis, the mollifier's Bernstein- and
  Friedrichs-type bounds, the Nash–Moser scheme, the settling write-out) are proved in the supplement and read by
  independent verifiers, not computed (deduced). The two-dust background's convergence on a rectangle reaching Σ_τ0 is
  computed for one choice of the outgoing family's characteristic data, those data themselves being among the items left
  open above.
```

New (round 4, c):

```text
  `checks/support8b.py`, `checks/support8c.py`, `checks/flux5.py`, `checks/mpdata5.py`, `checks/gluedecay5.py`,
  `checks/kirecon5.py`, `checks/hclass5.py`, `checks/re813.py`, `checks/eindcert5.py`, `checks/vii5census.py`,
  `checks/vii5read.py` and `checks/census9.py`, and for section 9 `checks/support9.py`, `checks/charge5.py`,
  `checks/eqlayer5.py`, `checks/e2lower5.py`, `checks/twodomainx5.py`, `checks/level2loop5.py`,
  `checks/lambdacount5.py`, `checks/twodomain5.py`, `checks/r0census5.py` and `checks/excise5.py`. A census of the
  deduced claims in sections 1–9 (103 claims, of which 27 named no program for the step) left none without one but the
  analytic estimates named below, the settling write-out and one step resting on a reading at source; where a check
  stops short of the step (an order λ¹ structure computed to order λ² in place of every order, a scan to a finite l) its
  entry in Appendix A says so. The analytic estimates themselves (the energy estimate and the bootstrap's analysis, the
  mollifier's Bernstein- and Friedrichs-type bounds, the Nash–Moser scheme, the settling write-out) are proved in the
  supplement and read by independent verifiers, not computed (deduced). The two-dust background's convergence on a
  rectangle reaching Σ_τ0 is computed for one choice of the outgoing family's characteristic data, those data themselves
  being among the items left open above.
```

(d) Appendix A, the entries of mpdata5.py and flux5.py, lines 2180-2190, and a new entry.

Old (round 4, d):

```text
- `checks/mpdata5.py` B1–B4: the data of translated, rotated and boosted Myers–Perry metrics lie in the class of
  supplement Part VII Lemma 0.1, ρ²C^∞ and ρ³C^∞ of the radial compactification. Controls: a mass term falling as ρ (B1,
  B4); a split-signature form, which vanishes on the sphere (B2); the projection term dropped (B3). Exact series; about
  four minutes.
- `checks/flux5.py` F1–F4: the flux 6π²m of the Kerr–Schild slice (F1–F2), the glued mass bound's ingredients (F3: R⁶
  q_2 = −10294529/36000, the annulus volume 255π²R⁴/2, |δm| ≤ C η (R² + 1)/(6π²R² − C) for C < 6π²R²) and step (6)'s
  bilinear difference bound (F4: for generic data of size B and a deviation of size ε, both at the annulus scaling, the
  remainder's difference has no term linear in the data, its quadratic part is R⁻⁶ times ε B and ε² and its cubic part
  R⁻⁸ times ε B², ε² B and ε³, so it is at most C ε (|B| + ε) R⁻⁶ + C ε R⁻⁸) (supplement Part VII Lemma 2.1 (c),
  Proposition 2.2 step (6)). Controls: the flux with the trace term's sign reversed; the curvature without its Γ·Γ terms
  (F3); the remainder without its linear part (F4). Exact; about twenty minutes.
```

New (round 4, d):

```text
- `checks/mpdata5.py` B1–B4: the data of translated, rotated and boosted Myers–Perry metrics on Kerr–Schild slices lie
  in the class of supplement Part VII Lemma 0.1, ρ²C^∞ and ρ³C^∞ of the radial compactification; on Hintz's surface the
  same holds by the graph map (supplement GLUEDECAY5.md Lemma 4.1 (a)). Controls: a mass term falling as ρ (B1, B4); a
  split-signature form, which vanishes on the sphere (B2); the projection term dropped (B3). Exact series; about four
  minutes.
- `checks/flux5.py` F1–F4: the flux 6π²m of the Kerr–Schild slice (F1–F2), the glued mass bound's ingredients (F3: R⁶
  q_2 = −10294529/36000, the annulus volume 255π²R⁴/2, |δm| ≤ C η (R² + 1)/(6π²R² − C) for C < 6π²R²) and step (6)'s
  bilinear difference bound (F4: for generic data of size B and a deviation of size ε, both at the annulus scaling, the
  remainder's difference has no term linear in the data, its quadratic part is R⁻⁶ times ε B and ε² and its cubic part
  R⁻⁸ times ε B², ε² B and ε³, so it is at most C ε (|B| + ε) R⁻⁶ + C ε R⁻⁸) (supplement Part VII Lemma 2.1 (c),
  Proposition 2.2 step (6)). Controls: the flux with the trace term's sign reversed; the curvature without its Γ·Γ terms
  (F3); the remainder without its linear part (F4). Exact; about twenty minutes.
- `checks/gluedecay5.py` E1–E6: section 8.7's reach of Theorem 4 (ii), directly or through gluing (supplement
  GLUEDECAY5.md). E1, the weighted integrals: the bound of a conormal perturbation of order a lies in r^(−ℓ0) H_b
  exactly when a > ℓ0, its integral diverging logarithmically at a = ℓ0. E2, the distance κ(a, ℓ0) > 0 behind the lower
  bound, from the Gram matrix in closed form, certified by interval arithmetic on a grid of a and ℓ0; κ(5/2, 7/2) =
  7.6546 × 10⁻⁴ against a direct quadrature. E3, the pulled-back examples: the pull-back of a radial tensor, the exact
  trace, the Tangherlini term, and an instance of the lower bound c Ξ R^(ℓ0−a) by quadrature. E4, the exact fluxes 6π²,
  3π², 3π²/2, (3/2)(a + 1)π² and 2π² of order-a profiles, and the exponents of the gluing's error terms and of the glued
  norm. E5, the spin and a translation entering the metric at r^(−3), the Hessian of Hintz's height function carrying no
  momentum or angular momentum, and its trace 2μ r^(−3). E6, these replacements: before seating it applies them to a
  copy of the paper and checks that copy, after seating it checks them in place, and it names the state it found.
  Controls: twenty-one mutants of the program, among them the Lebesgue density, the class profile without its
  oscillation, the three-dimensional coefficient 3 − a, mass and boost not decoupled, and a mass change in place of the
  spins. Exact, with κ certified and the instance by quadrature; about seventy seconds.
```

(e) Appendix C (the source map), line 2604.

Old (round 4, e):

```text
| section 8.7: Myers–Perry data in the class | `docket68/n1star/checks/mpdata5.py` B1–B4 |
```

New (round 4, e):

```text
| section 8.7: Myers–Perry data in the class, on Kerr–Schild slices | `docket68/n1star/checks/mpdata5.py` B1–B4 |
| section 8.7: Myers–Perry data on Hintz's surface; the class above ℓ0 | `docket68/n1star/GLUEDECAY5.md` sections 2, 5 |
| section 8.7: uniform gluing is membership; examples; the glued norm | `docket68/n1star/GLUEDECAY5.md` sections 3–5 |
| section 8.7: the integrals, exponents, fluxes, the distance behind c | `docket68/n1star/checks/gluedecay5.py` E1–E6 |
```

(f) Appendix D, the run list, line 2732.

Old (round 4, f):

```text
    python3 checks/flux5.py                              # about twenty minutes
```

New (round 4, f):

```text
    python3 checks/flux5.py                              # about twenty minutes
    python3 checks/gluedecay5.py                         # about seventy seconds
```

(g) Appendix D, the import paragraph, lines 2653-2661.

Old (round 4, g):

```text
`lead5.py`, `past5.py` and `mass5.py`, `checks/support8b.py` imports `checks/mpdata5.py`, `checks/ledger5.py` imports
`checks/support5.py`, `checks/support5c.py` imports `horizon5.py` and `lead5.py`, `checks/lambdacount5.py` imports
`checks/level2loop5.py`, `checks/support8c.py` imports `damping5.py`, `hthresh5.py`, `iplus5.py`, `lhor5.py`, `sbar5.py`
and `scri5.py`, `checks/gauge5.py` imports `data5.py`, `lead5.py` and `paper/response5.py`, `checks/excise5.py` imports
`growth5.py`, `checks/stage5.py` imports `lead5.py`, `checks/stage5b.py` imports `lead5.py` and `checks/stage5.py`,
`secondzero5.py` and `resid5.py` import `bondisph5.py`, which imports `sectexp5.py`, `resid5.py` and `szrun5.py` import
`dnsolve5.py`, `checks/support9.py` imports `lead5.py`, `checks/charge5.py` imports `checks/prop31loss5.py` and
`checks/dg5.py`, `checks/twodomainx5.py` imports `checks/twodomain5.py`, `checks/vii5read.py` imports
`checks/vii5census.py`; the others import nothing from the research tree:
```

New (round 4, g):

```text
`lead5.py`, `past5.py` and `mass5.py`, `checks/support8b.py` and `checks/gluedecay5.py` import `checks/mpdata5.py`,
`checks/ledger5.py` imports `checks/support5.py`, `checks/support5c.py` imports `horizon5.py` and `lead5.py`,
`checks/lambdacount5.py` imports `checks/level2loop5.py`, `checks/support8c.py` imports `damping5.py`, `hthresh5.py`,
`iplus5.py`, `lhor5.py`, `sbar5.py` and `scri5.py`, `checks/gauge5.py` imports `data5.py`, `lead5.py` and
`paper/response5.py`, `checks/excise5.py` imports `growth5.py`, `checks/stage5.py` imports `lead5.py`,
`checks/stage5b.py` imports `lead5.py` and `checks/stage5.py`, `secondzero5.py` and `resid5.py` import `bondisph5.py`,
which imports `sectexp5.py`, `resid5.py` and `szrun5.py` import `dnsolve5.py`, `checks/support9.py` imports `lead5.py`,
`checks/charge5.py` imports `checks/prop31loss5.py` and `checks/dg5.py`, `checks/twodomainx5.py` imports
`checks/twodomain5.py`, `checks/vii5read.py` imports `checks/vii5census.py`; the others import nothing from the research
tree:
```

(h) Appendix D, the md5 table, line 2913.

Old (round 4, h):

```text
| `docket68/n1star/checks/flux5.out` | `75c4e28d932ef8895941c219012badf7` |
```

New (round 4, h):

```text
| `docket68/n1star/checks/flux5.out` | `75c4e28d932ef8895941c219012badf7` |
| `docket68/n1star/checks/gluedecay5.py` | `94a241bad02fb734d68615e85ac06544` |
| `docket68/n1star/checks/gluedecay5.out` | `59b4aa002c4c196b846474f34a51e3c2` |
| `docket68/n1star/GLUEDECAY5.md` | `00000000000000000000000000000000` |
| `docket68/n1star/proof5/PART-V-GLUING.md` | `df25f8231e6af8cc1cfd08069d2700aa` |
```

[R5.0: superseded. Run against a seated copy of the paper, its E6 passed but four of its mutants survived, since they
acted only on the text before seating, so the program exited 1 there. Its (d) and (f) gave a run time different from
section 7's and the program's. Section 8.5 repairs both; its blocks are these but for (d)'s entry for E6 and the run
time in (d) and (f).]

### 8.5 Round 5 (current)

Eight blocks of `paper/RESPONSE-HL-5D.md`, to be applied together. They are section 8.4's but for (d)'s entry for E6,
which now describes the check in both states, and the run time in (d) and (f), now one figure with section 7 and the
program. Each old block occurs exactly once, the blocks are disjoint, (a) is immediately followed by (b), and with all
eight applied every place carries the change (computed, E6).

*Seating, and the re-pin.* E6 checks both states of the paper in every run. It rebuilds the state the paper is not in
from the one it finds, and it names the state it found. The whole program exits 0 on the paper before seating and on a
seated copy: `python3 checks/gluedecay5.py --paper PATH`. After the blocks are seated, run from `docket68/n1star/`:
`python3 checks/gluedecay5.py > checks/gluedecay5.out`. Its E6 line then names the seated state, so the .out changes.
Then run `cd ../../paper && python3 response5.py --update-md5`. That fills (h)'s zero row for GLUEDECAY5.md, refreshes
gluedecay5.out's row, and refreshes the 18 rows stale from other workstreams; R9 then passes. In (h), the md5 of
gluedecay5.py, gluedecay5.out and PART-V-GLUING.md are those of this round's files before seating.

(a) section 8.7, lines 1138-1140.

Old (a):

```text
theorem applies directly to perturbations of these data in his data class, which contains the data of every nearby
translated, rotated and boosted Myers–Perry metric (computed: their Cartesian components lie in ρ²C^∞ and ρ³C^∞ of the
radial compactification, `docket68/n1star/checks/mpdata5.py`, exact series at three points of S³ with spins, a boost and
```

New (a):

```text
theorem applies directly to perturbations of these data in his data class, which contains the data that every nearby
translated, rotated and boosted Myers–Perry metric induces on Hintz's surface (computed: on Kerr–Schild slices their
Cartesian components lie in ρ²C^∞ and ρ³C^∞ of the radial compactification, `docket68/n1star/checks/mpdata5.py`, exact
series at three points of S³ with spins, a boost and a translation, and the structural step that a Cartesian derivative
```

(b) section 8.7, lines 1141-1149, to the end of the paragraph.

Old (b):

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

New (b):

```text
gains a power of ρ; on Hintz's surface the same holds by the graph map, proved in supplement
`docket68/n1star/GLUEDECAY5.md` Lemma 4.1 (a)). The class also contains every perturbation conormal of an order a > ℓ0,
with |∂^k h| ≤ Ξ r^(−a−k) in the metric and Ξ r^(−a−1−k) in the second fundamental form. Such a perturbation has no
terms of orders r^(−2) and r^(−3) in the metric, nor of orders r^(−3) and r^(−4) in the second fundamental form, and its
norm is at most C Ξ (1 + (a − ℓ0)^(−1/2)). Theorem 4 holds for every ℓ0 ∈ (3, 4), with the data of (i), λ1 and δ taken
for that ℓ0. So with ℓ0 ∈ (3, min(a, 4)) its (ii) covers every such perturbation with a > 3 and Ξ below δ/(C (1 + (a −
ℓ0)^(−1/2))), at the rate of Theorem 4, its ε_K then below ℓ0 − 3 (proved: GLUEDECAY5.md Proposition 1 and Corollary
1.1). For 3/2 < a ≤ ℓ0 the decay rate does not decide, and gluing does not enlarge the class. A perturbation agrees on
every ball r < R with data to which Theorem 4 (ii) applies, uniformly in R in every norm of the class, if and only if
Theorem 4 (ii) applies to the perturbation itself. Indeed the infimum of the norms of data in the class that agree with
it on r < R is nondecreasing in R, and tends to its own norm if it lies in the class and to infinity if it does not lie
in the class at the norm's regularity (proved: GLUEDECAY5.md Proposition 2 and Corollary 2.1). At every such a and every
Ξ ≤ Ξ1 there are vacuum perturbations of size C_P Ξ outside the class: the data of (i) pulled back by the radial
diffeomorphism x ↦ (1 + Ξ r^(−a) cos log r) x far out, which are pure gauge and G-invariant. For R ≥ R_P, every data set
in the class that agrees with one of them on r < R has norm at least c Ξ R^(ℓ0−a), with c > 0, and at least c Ξ
(log2(R/R_P))^(1/2) at a = ℓ0 (proved: GLUEDECAY5.md Proposition 3). [CD03]'s gluing on the annulus R < r < 4R, which in
five dimensions needs no parity condition at these rates (section 8.6; supplement sections 10.63 and 10.66), does no
worse when its target is the family of translated, rotated and boosted Myers–Perry data on Hintz's surface: for every
such perturbation, with Ξ ≤ Ξ0 and R ≥ R_G, the glued data have norm at most C Ξ (1 + R^(ℓ0−a)), and C Ξ (1 + log
R)^(1/2) at a = ℓ0 (proved: GLUEDECAY5.md Proposition 4 and Corollary 4.3, with the gluing's estimates as supplement
`docket68/n1star/proof5/PART-V-GLUING.md` and `PART-VII-ASSEMBLY.md` Proposition 2.2 state them; the Myers–Perry data on
PART-V-GLUING.md's Kerr–Schild slices differ from that family by a fixed term of order r^(−3) in the second fundamental
form). At a = 3 the term from the annulus is the cost R^(ℓ0−3) of a bump of amplitude R^(−3) at radius R (computed:
`docket68/n1star/checks/support8b.py` M3). So for a < ℓ0 the glued data are guaranteed small enough for Theorem 4 (ii)
for R from R_G up to a multiple of (δ/Ξ)^(1/(ℓ0−a)), a range that is nonempty for Ξ small, and for the pulled-back
examples no data in the class that agree with them on r < R do better. The development of the glued data is not the
perturbation's: the solution near the hole at late times depends on the data near infinity. The perturbations to which
Theorem 4 (ii) applies, directly or through gluing uniformly in R, are exactly those small in Hintz's class; the
pulled-back examples lie outside it, and their developments are isometric to that of the data of (i) (computed: the
integrals, the exponents, the fluxes and the distance behind c, `docket68/n1star/checks/gluedecay5.py` E1–E6; the
constants C, C_P, R_P, R_G, Ξ0 and Ξ1 are proved to exist, not computed).
```

(c) section 9, the computational-support item, lines 1552-1564.

Old (c):

```text
  `checks/support8b.py`, `checks/support8c.py`, `checks/flux5.py`, `checks/mpdata5.py`, `checks/kirecon5.py`,
  `checks/hclass5.py`, `checks/re813.py`, `checks/eindcert5.py`, `checks/vii5census.py`, `checks/vii5read.py` and
  `checks/census9.py`, and for section 9 `checks/support9.py`, `checks/charge5.py`, `checks/eqlayer5.py`,
  `checks/e2lower5.py`, `checks/twodomainx5.py`, `checks/level2loop5.py`, `checks/lambdacount5.py`,
  `checks/twodomain5.py`, `checks/r0census5.py` and `checks/excise5.py`. A census of the deduced claims in sections 1–9
  (103 claims, of which 27 named no program for the step) left none without one but the analytic estimates named below,
  the settling write-out and one step resting on a reading at source; where a check stops short of the step (an order λ¹
  structure computed to order λ² in place of every order, a scan to a finite l) its entry in Appendix A says so.
  The analytic estimates themselves (the energy estimate and the bootstrap's analysis, the mollifier's Bernstein- and
  Friedrichs-type bounds, the Nash–Moser scheme, the settling write-out) are proved in the supplement and read by
  independent verifiers, not computed (deduced). The two-dust background's convergence on a rectangle reaching Σ_τ0 is
  computed for one choice of the outgoing family's characteristic data, those data themselves being among the items left
  open above.
```

New (c):

```text
  `checks/support8b.py`, `checks/support8c.py`, `checks/flux5.py`, `checks/mpdata5.py`, `checks/gluedecay5.py`,
  `checks/kirecon5.py`, `checks/hclass5.py`, `checks/re813.py`, `checks/eindcert5.py`, `checks/vii5census.py`,
  `checks/vii5read.py` and `checks/census9.py`, and for section 9 `checks/support9.py`, `checks/charge5.py`,
  `checks/eqlayer5.py`, `checks/e2lower5.py`, `checks/twodomainx5.py`, `checks/level2loop5.py`,
  `checks/lambdacount5.py`, `checks/twodomain5.py`, `checks/r0census5.py` and `checks/excise5.py`. A census of the
  deduced claims in sections 1–9 (103 claims, of which 27 named no program for the step) left none without one but the
  analytic estimates named below, the settling write-out and one step resting on a reading at source; where a check
  stops short of the step (an order λ¹ structure computed to order λ² in place of every order, a scan to a finite l) its
  entry in Appendix A says so. The analytic estimates themselves (the energy estimate and the bootstrap's analysis, the
  mollifier's Bernstein- and Friedrichs-type bounds, the Nash–Moser scheme, the settling write-out) are proved in the
  supplement and read by independent verifiers, not computed (deduced). The two-dust background's convergence on a
  rectangle reaching Σ_τ0 is computed for one choice of the outgoing family's characteristic data
  (`checks/twodomainx5.py`); for the data the supplement states, explicit Vaidya data on two null cones, the background
  on the whole domain is deduced (More families, above; supplement `docket68/n1star/FAMILIES5-FULL.md` Part I).
```

[final-pass 2026-11-13: the paper carries this text after the final pass, whose editorial block DR-g restated the
two-dust sentence (the background on the whole domain is deduced for the stated data, FAMILIES5-FULL Part I). The text
this block held before, kept:]

~~~text
  `checks/support8b.py`, `checks/support8c.py`, `checks/flux5.py`, `checks/mpdata5.py`, `checks/gluedecay5.py`,
  `checks/kirecon5.py`, `checks/hclass5.py`, `checks/re813.py`, `checks/eindcert5.py`, `checks/vii5census.py`,
  `checks/vii5read.py` and `checks/census9.py`, and for section 9 `checks/support9.py`, `checks/charge5.py`,
  `checks/eqlayer5.py`, `checks/e2lower5.py`, `checks/twodomainx5.py`, `checks/level2loop5.py`,
  `checks/lambdacount5.py`, `checks/twodomain5.py`, `checks/r0census5.py` and `checks/excise5.py`. A census of the
  deduced claims in sections 1–9 (103 claims, of which 27 named no program for the step) left none without one but the
  analytic estimates named below, the settling write-out and one step resting on a reading at source; where a check
  stops short of the step (an order λ¹ structure computed to order λ² in place of every order, a scan to a finite l) its
  entry in Appendix A says so. The analytic estimates themselves (the energy estimate and the bootstrap's analysis, the
  mollifier's Bernstein- and Friedrichs-type bounds, the Nash–Moser scheme, the settling write-out) are proved in the
  supplement and read by independent verifiers, not computed (deduced). The two-dust background's convergence on a
  rectangle reaching Σ_τ0 is computed for one choice of the outgoing family's characteristic data, those data themselves
  being among the items left open above.
~~~

(d) Appendix A, the entries of mpdata5.py and flux5.py, lines 2180-2190, and a new entry.

Old (d):

```text
- `checks/mpdata5.py` B1–B4: the data of translated, rotated and boosted Myers–Perry metrics lie in the class of
  supplement Part VII Lemma 0.1, ρ²C^∞ and ρ³C^∞ of the radial compactification. Controls: a mass term falling as ρ (B1,
  B4); a split-signature form, which vanishes on the sphere (B2); the projection term dropped (B3). Exact series; about
  four minutes.
- `checks/flux5.py` F1–F4: the flux 6π²m of the Kerr–Schild slice (F1–F2), the glued mass bound's ingredients (F3: R⁶
  q_2 = −10294529/36000, the annulus volume 255π²R⁴/2, |δm| ≤ C η (R² + 1)/(6π²R² − C) for C < 6π²R²) and step (6)'s
  bilinear difference bound (F4: for generic data of size B and a deviation of size ε, both at the annulus scaling, the
  remainder's difference has no term linear in the data, its quadratic part is R⁻⁶ times ε B and ε² and its cubic part
  R⁻⁸ times ε B², ε² B and ε³, so it is at most C ε (|B| + ε) R⁻⁶ + C ε R⁻⁸) (supplement Part VII Lemma 2.1 (c),
  Proposition 2.2 step (6)). Controls: the flux with the trace term's sign reversed; the curvature without its Γ·Γ terms
  (F3); the remainder without its linear part (F4). Exact; about twenty minutes.
```

New (d):

```text
- `checks/mpdata5.py` B1–B4: the data of translated, rotated and boosted Myers–Perry metrics on Kerr–Schild slices lie
  in the class of supplement Part VII Lemma 0.1, ρ²C^∞ and ρ³C^∞ of the radial compactification; on Hintz's surface the
  same holds by the graph map (supplement GLUEDECAY5.md Lemma 4.1 (a)). Controls: a mass term falling as ρ (B1, B4); a
  split-signature form, which vanishes on the sphere (B2); the projection term dropped (B3). Exact series; about four
  minutes.
- `checks/flux5.py` F1–F4: the flux 6π²m of the Kerr–Schild slice (F1–F2), the glued mass bound's ingredients (F3: R⁶
  q_2 = −10294529/36000, the annulus volume 255π²R⁴/2, |δm| ≤ C η (R² + 1)/(6π²R² − C) for C < 6π²R²) and step (6)'s
  bilinear difference bound (F4: for generic data of size B and a deviation of size ε, both at the annulus scaling, the
  remainder's difference has no term linear in the data, its quadratic part is R⁻⁶ times ε B and ε² and its cubic part
  R⁻⁸ times ε B², ε² B and ε³, so it is at most C ε (|B| + ε) R⁻⁶ + C ε R⁻⁸) (supplement Part VII Lemma 2.1 (c),
  Proposition 2.2 step (6)). Controls: the flux with the trace term's sign reversed; the curvature without its Γ·Γ terms
  (F3); the remainder without its linear part (F4). Exact; about twenty minutes.
- `checks/gluedecay5.py` E1–E6: section 8.7's reach of Theorem 4 (ii), directly or through gluing (supplement
  GLUEDECAY5.md). E1, the weighted integrals: the bound of a conormal perturbation of order a lies in r^(−ℓ0) H_b
  exactly when a > ℓ0, its integral diverging logarithmically at a = ℓ0. E2, the distance κ(a, ℓ0) > 0 behind the lower
  bound, from the Gram matrix in closed form, certified by interval arithmetic on a grid of a and ℓ0; κ(5/2, 7/2) =
  7.6546 × 10⁻⁴ against a direct quadrature. E3, the pulled-back examples: the pull-back of a radial tensor, the exact
  trace, the Tangherlini term, and an instance of the lower bound c Ξ R^(ℓ0−a) by quadrature. E4, the exact fluxes 6π²,
  3π², 3π²/2, (3/2)(a + 1)π² and 2π² of order-a profiles, and the exponents of the gluing's error terms and of the glued
  norm. E5, the spin and a translation entering the metric at r^(−3), the Hessian of Hintz's height function carrying no
  momentum or angular momentum, and its trace 2μ r^(−3). E6, these replacements, checked in both states of the paper,
  before seating and seated, the state it is not in rebuilt from the one it finds, which it names (`--paper PATH` checks
  another copy). Controls: twenty-one mutants of the program, among them the Lebesgue density, the class profile without
  its oscillation, the three-dimensional coefficient 3 − a, mass and boost not decoupled, and a mass change in place of
  the spins. Exact, with κ certified and the instance by quadrature; about ninety seconds.
```

(e) Appendix C (the source map), line 2604.

Old (e):

```text
| section 8.7: Myers–Perry data in the class | `docket68/n1star/checks/mpdata5.py` B1–B4 |
```

New (e):

```text
| section 8.7: Myers–Perry data in the class, on Kerr–Schild slices | `docket68/n1star/checks/mpdata5.py` B1–B4 |
| section 8.7: Myers–Perry data on Hintz's surface; the class above ℓ0 | `docket68/n1star/GLUEDECAY5.md` sections 2, 5 |
| section 8.7: uniform gluing is membership; examples; the glued norm | `docket68/n1star/GLUEDECAY5.md` sections 3–5 |
| section 8.7: the integrals, exponents, fluxes, the distance behind c | `docket68/n1star/checks/gluedecay5.py` E1–E6 |
```

(f) Appendix D, the run list, line 2732.

Old (f):

```text
    python3 checks/flux5.py                              # about twenty minutes
```

New (f):

```text
    python3 checks/flux5.py                              # about twenty minutes
    python3 checks/gluedecay5.py                         # about ninety seconds
```

(g) Appendix D, the import paragraph, lines 2653-2661.

Old (g):

```text
`lead5.py`, `past5.py` and `mass5.py`, `checks/support8b.py` imports `checks/mpdata5.py`, `checks/ledger5.py` imports
`checks/support5.py`, `checks/support5c.py` imports `horizon5.py` and `lead5.py`, `checks/lambdacount5.py` imports
`checks/level2loop5.py`, `checks/support8c.py` imports `damping5.py`, `hthresh5.py`, `iplus5.py`, `lhor5.py`, `sbar5.py`
and `scri5.py`, `checks/gauge5.py` imports `data5.py`, `lead5.py` and `paper/response5.py`, `checks/excise5.py` imports
`growth5.py`, `checks/stage5.py` imports `lead5.py`, `checks/stage5b.py` imports `lead5.py` and `checks/stage5.py`,
`secondzero5.py` and `resid5.py` import `bondisph5.py`, which imports `sectexp5.py`, `resid5.py` and `szrun5.py` import
`dnsolve5.py`, `checks/support9.py` imports `lead5.py`, `checks/charge5.py` imports `checks/prop31loss5.py` and
`checks/dg5.py`, `checks/twodomainx5.py` imports `checks/twodomain5.py`, `checks/vii5read.py` imports
`checks/vii5census.py`; the others import nothing from the research tree:
```

New (g):

```text
`lead5.py`, `past5.py` and `mass5.py`, `checks/support8b.py` and `checks/gluedecay5.py` import `checks/mpdata5.py`,
`checks/ledger5.py` imports `checks/support5.py`, `checks/support5c.py` imports `horizon5.py` and `lead5.py`,
`checks/lambdacount5.py` imports `checks/level2loop5.py`, `checks/support8c.py` imports `damping5.py`, `hthresh5.py`,
`iplus5.py`, `lhor5.py`, `sbar5.py` and `scri5.py`, `checks/gauge5.py` imports `data5.py`, `lead5.py` and
`paper/response5.py`, `checks/excise5.py` imports `growth5.py`, `checks/stage5.py` imports `lead5.py`,
`checks/stage5b.py` imports `lead5.py` and `checks/stage5.py`, `secondzero5.py` and `resid5.py` import `bondisph5.py`,
which imports `sectexp5.py`, `resid5.py` and `szrun5.py` import `dnsolve5.py`, `checks/support9.py` imports `lead5.py`,
`checks/charge5.py` imports `checks/prop31loss5.py` and `checks/dg5.py`, `checks/twodomainx5.py` imports
`checks/twodomain5.py`, `checks/vii5read.py` imports `checks/vii5census.py`, `checks/axhier5.py` imports
`checks/axisbianchi5.py`, `checks/axis5.py` imports `dnull5.py` and `checks/linest5.py`, `checks/blocks5.py` imports
`checks/linest5.py`, `checks/classm5.py` imports `checks/stage1cap5.py`, `checks/cont5.py` imports `checks/null3.py`,
`checks/cp3grid5.py` imports `checks/cpaxis5.py` and `checks/cpsolve5.py`, `checks/cpaxis5.py` imports
`checks/cpsolve5.py`, `checks/cpsolve5.py` imports `dnsolve5.py`, `checks/d0count5.py` imports `checks/ordcensus5.py`,
`checks/dceiling5.py` imports `checks/dweights5.py`, `checks/lambdagen5.py` and `checks/prop31loss5.py`,
`checks/dnumber5.py` imports `checks/dceiling5.py`, `checks/dweights5.py`, `checks/eflat5.py`, `checks/lambdagen5.py` and
`checks/prop31loss5.py`, `checks/dweights5.py` imports `checks/prop31loss5.py`, `checks/eflat5.py` imports
`checks/dceiling5.py`, `checks/dweights5.py` and `checks/iotapoles5.py`, `checks/inverse6_5.py` imports `strap5.py`,
`checks/inverse6_5m.py` imports `gmodes5.py`, `modes5.py` and `checks/e2certify5.py`, `checks/iotaind5.py` imports
`checks/dceiling5.py` and `checks/eflat5.py`, `checks/iotapoles5.py` imports `damping5.py`, `iota5.py`, `lin5.py` and
`checks/dceiling5.py`, `checks/lam0data5.py` imports `data5.py` and `checks/stage1rate5.py`, `checks/lambdagen5.py`
imports `checks/dweights5.py` and `checks/prop31loss5.py`, `checks/lev1_5.py` imports `checks/linest5.py` and
`checks/wgron5.py`, `checks/linest5.py` imports `dnsolve5.py` and `checks/null3.py`, `checks/logind5.py` imports
`checks/dnumber5.py`, `checks/dweights5.py` and `checks/eflat5.py`, `checks/lzerotrace5.py` imports
`checks/envelope5.py`, `checks/lzeroconst5.py` and `checks/stage0bd5.py`, `checks/m22evol5.py` imports
`checks/lam0data5.py`, `checks/modcount5.py` imports `checks/d0count5.py`, `checks/dnumber5.py`, `checks/dweights5.py`
and `checks/prop31loss5.py`, `checks/rcert5.py` imports `checks/bondisph5.py` and `checks/resid5.py`, `checks/rcert5c.py`
imports `checks/rcert5.py`, `checks/rcert5d.py` imports `checks/rcert5.py`, `checks/reduce5.py` imports `dnull5.py`,
`checks/rich5.py` imports `checks/rcert5.py` and `checks/rcert5d.py`, `checks/rootavoid5.py` imports `damping5.py`,
`checks/dweights5.py`, `checks/lambdagen5.py` and `checks/prop31loss5.py`, `checks/scalarblock5.py` imports
`damping5.py`, `checks/stage0bd5.py` imports `lead5.py`, `checks/envelope5.py` and `checks/lzeroconst5.py`,
`checks/stage1cap5.py` imports `checks/lzeroconst5.py` and `checks/lzerotrace5.py`, `checks/symbol5.py` imports
`dnsolve5.py`, `checks/symbol5s.py` imports `checks/symbol5.py`, `checks/szconv5.py` imports `checks/secondzero5.py`,
`checks/tensorzero5.py` imports `class5.py` and `checks/zeroext5.py`, `checks/thetain5.py` imports `sbar5.py`,
`checks/wgron5.py` imports `checks/linest5.py`, `checks/x7indep5.py` imports `checks/dnumber5.py` and
`checks/dweights5.py` (and `checks/blockw5.py` reads `checks/blocks5.out` and `checks/wgron5.out`, `checks/d0count5.py`
reads `checks/thetain5.out`, `checks/inverse6_5a.py` reads `EFFECTIVE-CONSTANTS.md` and `CONSTANTS5.md`,
`checks/l2par5.py` reads `checks/dnumber5.out`, `checks/logind5.py` reads `checks/dnumber5.out`, `checks/modcount5.py`
reads `checks/dnumber5.out`, `checks/dweights5.out`, `checks/lambdagen5.out` and `checks/rootavoid5.out`,
`checks/mtrunc5.py` reads `checks/cpaxis5_a5.out`, `checks/cpaxis5_a5_m48.out` and `checks/cpaxis5_a5_m56.out`,
`checks/rootavoid5.py` reads `checks/lambdagen5.out`, `checks/scalarblock5.py` reads `checks/scalarblock5_block.txt`);
the others import nothing from the research tree:
```

[final-pass 2026-11-13: the paper carries this text after the final pass, which merged into it the imports of
CONSTANTS5 R15.7 pair 5 and CERTIFY-10L5-RESULT 12.4 D2 (the same paragraph). The text this block held before, kept:]

~~~text
`lead5.py`, `past5.py` and `mass5.py`, `checks/support8b.py` and `checks/gluedecay5.py` import `checks/mpdata5.py`,
`checks/ledger5.py` imports `checks/support5.py`, `checks/support5c.py` imports `horizon5.py` and `lead5.py`,
`checks/lambdacount5.py` imports `checks/level2loop5.py`, `checks/support8c.py` imports `damping5.py`, `hthresh5.py`,
`iplus5.py`, `lhor5.py`, `sbar5.py` and `scri5.py`, `checks/gauge5.py` imports `data5.py`, `lead5.py` and
`paper/response5.py`, `checks/excise5.py` imports `growth5.py`, `checks/stage5.py` imports `lead5.py`,
`checks/stage5b.py` imports `lead5.py` and `checks/stage5.py`, `secondzero5.py` and `resid5.py` import `bondisph5.py`,
which imports `sectexp5.py`, `resid5.py` and `szrun5.py` import `dnsolve5.py`, `checks/support9.py` imports `lead5.py`,
`checks/charge5.py` imports `checks/prop31loss5.py` and `checks/dg5.py`, `checks/twodomainx5.py` imports
`checks/twodomain5.py`, `checks/vii5read.py` imports `checks/vii5census.py`; the others import nothing from the research
tree:
~~~

(h) Appendix D, the md5 table, line 2913.

Old (h):

```text
| `docket68/n1star/checks/flux5.out` | `75c4e28d932ef8895941c219012badf7` |
```

New (h):

```text
| `docket68/n1star/checks/flux5.out` | `75c4e28d932ef8895941c219012badf7` |
| `docket68/n1star/checks/gluedecay5.py` | `8ddfeffaf348e934726e5616e1dc9807` |
| `docket68/n1star/checks/gluedecay5.out` | `a1cdd9849ccc53d3f6f60ffecdac5891` |
| `docket68/n1star/GLUEDECAY5.md` | `00000000000000000000000000000000` |
| `docket68/n1star/proof5/PART-V-GLUING.md` | `df25f8231e6af8cc1cfd08069d2700aa` |
```

## R2.0 Round 2 (2026-11-06): the verifier's reading, re-derived and seated

*The reading.* An independent verifier read the note in full. It recomputed $\kappa$, Lemma 4.1 (d) and the exponent
inequalities by its own scripts, checked the READ quotes at source, and applied 22 mutations to the program. Its
verdict: the mathematics holds; GD3 is right but is no defect in Part V; and $\ell_0$ is fixed consistently (the paper
:1153 and :1027, Part VII (0.1), PART-VI4-PARAMS.md row d1). Each finding below was re-derived here before it was
seated. The text above is kept as written, with a bracketed note at each place it changes.

(M1) *The upper bound at $a = \ell_0$.* Round 1's new text bounded the glued norm by "C ε R^(ℓ0−a)", which at $a =
\ell_0$ is $C\epsilon$ for every $R$. But Proposition 3's examples of order $\ell_0$ are perturbations to which
Proposition 4 applies (size $C_P\epsilon\le\epsilon_0$ for $\epsilon$ small), and every data set agreeing with them has
norm at least $c_P\epsilon(\log_2(R/R_P))^{1/2}$, unbounded in $R$. So that bound is false at $a = \ell_0$; the proved
one is (5.5). Section 8.2 (b) states (5.5), with its hypotheses $\epsilon\le\epsilon_0$, $R\ge R_G$.

(Minor 1) *"Only ... sharp".* Corollary 4.3 bounds the glued norm for every perturbation, so it gives a range of $R$ on
which (ii) is guaranteed. "Only up to" would need a lower bound for every perturbation, and that is false: in the class,
$N_R$ stays below the perturbation's own norm (Proposition 2 (b)). The lower bound is proved for the examples of
Proposition 3 alone. At $a = \ell_0$ the range is $\log R<(\delta/(C\epsilon))^2-1$, not a power. Seated at (D), at
Corollary 4.3 and in section 8.2 (b).

(Minor 2) *The dependence on $\ell_0$.* Theorem 4 fixes $\ell_0$ first. Its $\lambda_1$, $\delta$, $d_1$, gluing order
and radius, and so its data of (i), depend on $\ell_0$ (Part VII section 4). Its chain
$\epsilon_K<\epsilon_+<\ell_I-3<\ell_0-3$ bounds the rate (the paper's Theorem 4). Corollary 1.1 said so, but (A), GD2
and round 1's new text did not. Seated there.

(Minor 3) *What is reached.* By Remark 3.2, $\Psi_\epsilon^*(\gamma_\lambda,k_\lambda)$ has a development isometric to
that of $(\gamma_\lambda,k_\lambda)$, which settles by Theorem 0.2 (i). So settling, as a statement about the geometry,
is not confined to the class. What is exact is the reach of (ii): it applies, directly or through gluing uniformly in
$R$, to exactly the perturbations small in Hintz's class (Corollary 2.1). Seated in section 0, Theorem 5, GD1 and
section 8.2 (b).

(Minor 4) *What is computed.* E1-E6 compute the integrals, the exponents, the fluxes, the identities and $\kappa$, and
hence $c_P$. The constants $C_1$, $C_1'$, $C_0$, $C_P$, $R_P$, $R_G$, $L$, $\epsilon_0$, $\epsilon_1$ and Corollary
4.3's $C$ are proved to exist and are not computed. Seated at the labels and in section 8.2 (b).

(Minor 5) *The program.* Re-derived from round 1's source:
- E2 compared only the entries cc, cs, g1c and g2s with sympy and quadrature.
- E2 printed $\kappa$ without asserting it.
- E3's second-order test substituted $r = e^{t}$ after $\log r\to t$, so `.has(r)` was always False.
- E4's "the flux vanishes iff $a>2+d$" compared an inequality with itself.
- E5's control returned False on any failed series, so a broken series counted as the control failing.

Changes, each now in `checks/gluedecay5.py`:
- E2 checks all ten Gram entries against sympy's exact integrals and quadrature.
- E2 asserts $\kappa(\frac52,\frac72)$: the closed forms against a direct quadrature of the Gram matrix in $s$ (no
  closed form), to $10^{-25}$, and against the verifier's $7.6546\times10^{-4}$, to $10^{-8}$.
- E3 checks the exact second-order identity and an $r$-free test after $\log r\to t$ alone. It also checks the
  Tangherlini term of the instance pointwise, at $r = 10^2,10^3$: $(\tau_\mu-\tau_0)r^{2+a}/(\epsilon\mu)$ is within
  $10^{-3}$ of $-2(a\cos\log r+\sin\log r)$.
- E4 computes, exactly, the fluxes over $S_\rho$ of explicit order-$a$ profiles, with exact moments on $S^3$. Each is
  $c_d(a)\rho^{2+d-a}$, with $c_d = 6\pi^2$ (energy), $3\pi^2$ (momentum), $\frac32\pi^2$ (centre of mass) and $2\pi^2$
  (angular momentum). The limits are taken at six values of $a$.
- E4 adds the condition that the box does not decay where a charge of the perturbation need not vanish, $a\le2+d$.
- E5 raises on a failed series instead of returning False.
- E6 checks both blocks of section 8.2, and that (a) is immediately followed by (b) in the paper.

Every check now runs against named mutants of the code under test, each of which must fail:
- E1: 'lebesgue';
- E2: 'no_osc', 'ss_sign', 'lam_max';
- E3: 'coef3', 'second_r3', 'mu0';
- E4: 'no_decouple', 'box_strong';
- E5: 'mass', 'dim3';
- E6: 'char_a', 'char_b'.

The verifier's five surviving mutations were the sign of ss, $\lambda_{\max}$ for $\lambda_{\min}$, the second-order
expression times $r^3$, $\mu = 0$, and the box exponent $\min(0,1+d-a)$. All five are now among the mutants, and all
five fail.

On the last one the verifier noted that the stronger box is true as an inequality on $T_X$. Re-derived, it breaks the
fixed-point step all the same. For $a\le2+d$ the charge difference $\Delta\mathfrak Q_X$ is $O(\epsilon)$ and need not
vanish: a nearby member of Lemma 4.1's family differs from $(\gamma^{m_\lambda},k^{m_\lambda})$ at order 2 with
different charges, and E4's fluxes at $a = 2+d$ are nonzero. A box of radius $C_0\epsilon R^{1+d-a}\to0$ cannot contain
such a difference for $a>1+d$.

[R3.0, nit 8: a tighter argument replaces the last paragraph's support, since a nearby member of the family is not a
perturbation on $\Sigma$ and E4's profiles are not vacuum. For $d = 1$ pull the data of (i) back by $x\mapsto
x+\chi_1(r)c$, a constant translation far out. This is a vacuum perturbation, pure gauge, of order 3 = 2 + d, since
$\gamma^{m_\lambda}(x+c)-\gamma^{m_\lambda}(x)$ is conormal of order 3. It moves the centre of mass by the energy times
$c$: Part V Proposition 2.3's $d = -6\pi^2\mu_0$ per unit translation, at the base mass $m_\lambda$. So $\Delta\mathfrak
Q_{e'_l} = -6\pi^2m_\lambda c_l+O(|c|^2)\ne0$ does not depend on $R$. Then $Q_R-\tilde{\mathfrak
q}(p_\lambda)\to\Delta\mathfrak Q$, since $T_X\to0$, and a box of radius tending to 0 excludes it.]

(Minor 6) *The paper's :1137-1140.* `checks/mpdata5.py` B2 and B4 compute at $t' = 0$, on Kerr-Schild slices (its
docstring). The data that matter for (ii) are those on Hintz's surface: by GD3 the slice data lie in the class but are
not near the data of (i). On Hintz's surface membership is Lemma 4.1 (a), by the graph map. Section 8.2 (a) states "on
Hintz's surface", and (b) cites Lemma 4.1 (a).

(Nits)
- GD3, precisely: $\tilde K_p-K_p = \nabla^2f+\rho^4C^\infty$ at the same $p$, and $K_{p_\lambda}-k^{m_\lambda} =
  -\nabla^2f+\rho^5C^\infty$. Lemma 4.1 (d)'s proof gives both. The verifier's independent computation agrees: the graph
  minus the slice, minus $\nabla^2f$, is $(8,-3)\mu^2r^{-5}$ in the components $(\hat x\hat x,\delta-\hat x\hat x)$,
  with equal metrics.
- $N_R$ is an infimum.
- The examples have size $C_P\epsilon$ and need $\epsilon\le\epsilon_1$, and their lower bounds hold for $R\ge R_P$.
- Corollary 4.3's window is $R_G\le R<(\delta/(2C\epsilon))^{1/(\ell_0-a)}$, nonempty when $2C\epsilon
  R_G^{\ell_0-a}<\delta$.
- Proposition 3 takes $R_P\ge4r_2$.

Each is seated where it occurs.

*GD3 and Part V.* Re-derived from Part V Definition 2.1 (members on $\{y^0 = 0\}$) and Theorem 3.1 (abstract data on
$\{r>R_0\}\subset\mathbb R^4$, nothing about $\Sigma_{\mathrm{IVP}}$ or the class). Its proof uses only Lemma 2.2's
bounds and Corollary 2.4. Part VII uses that proof only in class form, with the members replaced by $(\gamma^m,k^m)$ on
the graph (Proposition 2.2 (2); findings (VII1), (VII3)). So GD3 constrains Proposition 4 here, which uses Lemma 4.1's
family, and Part V needs no repair.

Its Remark 3.4 is stale: Part VII neither relates the transform to III.B's boosts or III.J's translations nor checks
charges in $V$. It is amended in `proof5/PART-V-GLUING.md` by a bracketed note after the remark, the remark kept as
written.

*The paper.* Section 8.2 replaces round 1's block (section 8.1, kept) by two adjacent blocks, (a) at lines 1138-1140 and
(b) at lines 1141-1149. Each old block occurs exactly once, and (a) is immediately followed by (b) (E6).

*Ledger.* `checks/gluedecay5.py` E1-E6: all PASS, and all 13 mutants fail as they must; output in
`checks/gluedecay5.out`. The verifier's report and scripts stay in its scratch space, outside the repository. Open:
nothing.

## R3.0 Round 3 (2026-11-06): the confirming reading, re-derived and seated

*The reading.* A confirming reader checked round 2's seating. It found every finding correctly seated and no new
mathematical error, and it raised the items below, each re-derived here before it was seated. The text above is kept as
written, with bracketed notes where it changes.

(A) *GD2 and Theorem 5 (ii).* GD2's "$\asymp\epsilon R^{\ell_0-a}$" holds for every $a\in(\frac32,\ell_0]$ only as an
upper bound, by Corollary 4.3. Two-sided, it holds for Proposition 3's examples, and at $a = \ell_0$ the order is
$\epsilon(\log R)^{1/2}$, by (4.1) and (5.5): M1's error and Minor 1's overclaim in one more place. Theorem 5 (ii)'s
"attains this order for every perturbation" likewise. Both are noted where they stand.

[R4.0, nit 2: "for every $a\in(\frac32,\ell_0]$ only as an upper bound" is false at $a = \ell_0$, where the upper bound
is $\epsilon(\log R)^{1/2}$, not $\epsilon R^{0}$. Read $a\in(\frac32,\ell_0)$, with $a = \ell_0$ as the next sentence
states it.]

(B) *The paper's apparatus.* Round 2's blocks, applied verbatim, would have removed section 8.7's only citation of
`checks/support8b.py` M3 and of the bump. Appendix C's row "sections 8.1–8.8: … the bump's cost | support8b.py M1–M3"
would then have mapped to nothing in section 8. They also cited GLUEDECAY5.md and `checks/gluedecay5.py`, which section
9's computational-support list, Appendix A, the source map and Appendix D did not carry.

Both were checked against the paper:
- Section 8 cites M3 only at :1149.
- Section 9's list (:1548-1564), Appendix A, Appendix C (:2489 on) and Appendix D (the run list at :2731-2732, the
  import paragraph at :2653-2661, the md5 table) name neither file.
- R9 checks every md5 row, and `response5.py --update-md5` rewrites the 32-hex column of every row matching `| \`file\`
  | \`md5\` |` (response5.py:439-499), new rows included.

Section 8.3 now gives eight blocks to be applied together:
- (a) and (b): section 8.7, which keeps M3 as the annulus term at $a = 3$;
- (c): section 9's list;
- (d): Appendix A, with mpdata5.py's entry worded for the Kerr-Schild slices and Hintz's surface (nit 4), and an entry
  for gluedecay5.py;
- (e): three rows of the source map;
- (f) and (g): Appendix D's run list and imports;
- (h): four md5 rows.

E6 applies all eight to a copy of the paper and checks each place.

(Nits)

- (1) *The letter.* η is the Minkowski metric at paper :180, :1063 and :2115 (checked), and :1133 uses ε for a
  deviation. Section 8.3 writes the size as ϰ, which the paper does not use (counted: ϰ occurs 0 times; ς, ϱ, ϵ and ϕ
  are also free). It also writes no ε for the rate ("its ε_K then below ℓ0 − 3"), so :1133's ε keeps its one meaning.
- (2) *The join.* (a) and (b) are wrapped as one paragraph and split after four lines, so no short line is left
  mid-paragraph.
- (3) *The orders.* "No terms of orders r^(−2) and r^(−3)" holds for the metric. In the second fundamental form the
  orders are r^(−3) and r^(−4) (Theorem 4 (ii), :1166-1167), and those vanish too, since Proposition 1 makes every
  coefficient zero. Fixed in (b), and noted at section 0's (A).
- (4) *mpdata5.py's entry.* Appendix A's wording is now that of section 8.3 (d).
- (5) *The flux constants.* E4 asserts $c_d = 6\pi^2, 3\pi^2, \frac32\pi^2, 2\pi^2$, recomputed by hand in round 2's
  review: energy $3r^{-a-1}$ times $2\pi^2$; momentum $6r^{-a-1}\omega_1\omega_l$, $\int\omega_1^2 = \frac{\pi^2}2$;
  centre of mass $3x_1^2r^{-a-2}$; angular momentum $2(x_1^2+x_2^2)r^{-a-2}$.
- (6) *The exponents of (5.2).* E4 derives them from the box radii at every vertex: $|\Delta p_2|$ from the five
  degree-0 radii, so p2exp = box(d = 0); $|\Delta p|$ from all fifteen, so p3exp = max_d box(d). These are Proposition 4
  (1)'s two Lipschitz steps.
- (7) *The definitional check.* "box ≥ 0 where a ≤ 2+d" holds by the definition of the box, and is relabelled as such
  ("def."). It stays because it pins the mutant box_strong; the reason it matters is nit 8.
- (8) *The tighter argument.* Noted at R2.0. The pure-gauge translation $x\mapsto x+\chi_1c$ is a vacuum perturbation of
  order 3 that moves the centre of mass by $-6\pi^2m_\lambda c$, a charge difference independent of $R$, which a
  decaying box excludes.
- (9) *Part V's amendment.* $f$ is the height function of the graph $\Sigma_{\mathrm{IVP}} = \{t_{\mathrm{KS}} = f\}$
  far out; the time function is III.B's $t$. Corrected in place in PART-V-GLUING.md's bracketed note, marked as
  corrected.
- (10) *The run time.* About ninety seconds, measured: 88 s here with this round's nineteen mutants (the reader measured
  68.5 s for round 2's thirteen). The docstring, section 7 and section 8.3's (d) and (f) now agree.

*The program.* E4 and E6 are changed as above. The reader's four surviving mutations are now mutation controls, and all
four fail:
- 'energy_trsign': the trace term's sign in the energy flux;
- 'mom_drop_x': the trace subtracted on the wrong index;
- 'p3_strong': p3exp = min(0, 2 − a);
- 'box_weak': the box exponent min(0, 3 + d − a).

E6 adds 'drop_c' (block (c) not applied) and 'drop_m3' (block (b) without M3). That makes nineteen mutants in all, each
failing. The reader's expected survivor 'e6_adj_any' is a deliberate weakening and is not a control.

*Ledger.* `checks/gluedecay5.py` E1-E6: all PASS, with nineteen mutants failing; output in `checks/gluedecay5.out`.
Open: nothing. The md5 row of GLUEDECAY5.md in section 8.3 (h) is filled on seating by `--update-md5`.


[R4.0, Minor 2: the seating step was incomplete: after seating, round 3's E6 failed and the .out could not be
reproduced. Section 8.4 names the step, and E6 now accepts the seated state.]

## R4.0 Round 4 (2026-11-06): the third reading, re-derived and seated

*The reading.* The third reader re-checked the note in full: the lemmas, propositions, corollaries and theorem, with
$\kappa$ recomputed by its own minimisation over $\theta$. It found every round-2 finding seated and no mathematical
error. It applied the eight blocks of section 8.3 to a scratch copy of the paper and ran `--update-md5` and
`response5.py --selftest` there, and it raised two minors and six nits, all in the paper's apparatus or in wording. Each
is re-derived below and seated, with the old text kept and bracketed notes where it changes. The paper and
N1STAR-PROOF.md are not edited.

(Minor 1) *Appendix A's entry for E1.* Section 8.3 (d) said that a conormal perturbation of order $a$ has its remainder
in $r^{-\ell_0}H_b$ exactly when $a>\ell_0$. The "if" holds (Proposition 1). The "only if" fails: a perturbation of
order $a\le\ell_0$ can lie in the class, for instance the data of a nearby boosted Myers-Perry metric on Hintz's
surface, which are of order 2 (Lemma 4.1 (a)). That is why section 8.7 says the rate does not decide. E1 computes the
integral of the bound $\epsilon r^{-a}$. Section 8.4 (d) now reads: "the bound of a conormal perturbation of order a
lies in r^(−ℓ0) H_b exactly when a > ℓ0, its integral diverging logarithmically at a = ℓ0".

[R5.0, nit 2: the example above, "the data of a nearby boosted Myers-Perry metric on Hintz's surface", conflicts with
R3.0's nit 8, by which a nearby member of the family is not a perturbation on $\Sigma$. Read instead: the data of (i)
pulled back by $x\mapsto x+\chi_1(r)c$, a vacuum perturbation of order $3\le\ell_0$ whose difference from
$(\gamma_\lambda,k_\lambda)$ lies in $\rho^3C^\infty\times\rho^4C^\infty$ (Lemma 4.1 (b)'s proof), so in the class.
Corollary 4.3's glued data, of order 2 and in the class, are another example.]

(Minor 2) *E6 after seating.* Round 3's E6 required each old block exactly once, so after seating it found old (a)-(e)
and (g) zero times and failed. Appendix D's run would then exit 1, and the .out pinned in (h) could not be reproduced.
Re-derived on the blocks: the old texts of (f) and (h) are prefixes of their new texts and survive seating, and the
others do not. E6 now recognises the paper's state, with md5 digits blanked so that a refreshed column still matches:
- *before seating:* each old block once and no new block; the old blocks disjoint and (a) immediately followed by (b);
  all eight applied to a copy, and the places checked there;
- *seated:* each new block once, disjoint, (a) immediately followed by (b), and the old texts of (a)-(e) and (g) absent;
  the places checked in the paper itself.

[R5.0, Minor: E6 was only half repaired. On a seated copy of the paper it read 'seated' and passed, but its mutants
char_a, char_b, drop_c and seated_keep_old_a acted only on the text before seating and survived there, so the whole
program exited 1. See R5.0.]

It names the state it found, and before seating it also runs the seated check on the applied copy, its zero md5 replaced
as `--update-md5` would replace it. So both paths are computed in every run, and the mutant 'seated_keep_old_a' (old (a)
left in the copy) must fail them. The re-pin step is named in section 8.4: rerun the program to its .out, then
`--update-md5`. Tested once directly as well, on scratch copies of the paper outside the repository: with all eight
blocks applied and the md5 column refreshed, E6 names the state 'seated' and passes; with only (a) applied it names
'neither' and fails.

(Nits)

- (1) *Block (b)'s labels.* "(proved: GLUEDECAY5.md Proposition 4 and Corollary 4.3, ...)" now follows the glued-norm
  bound it labels, and the M3 sentence carries "(computed: `docket68/n1star/checks/support8b.py` M3)".
- (2) *GD2's R3.0 note and R3.0 (A).*
  - For the two-sided bound on the examples, Proposition 4 must apply to them, which needs $C_P\epsilon\le\epsilon_0$ as
    well as $\epsilon\le\epsilon_1$.
  - "The least norm" is the infimum $N_R$.
  - R3.0 (A)'s interval is $(\frac32,\ell_0)$, open at $\ell_0$, where the bound is $\epsilon(\log R)^{1/2}$.
  - Noted where they stand.
- (3) *Block (e).* Appendix C cites notes by path (for example `docket68/n1star/LOSS-D.md`), and "supplement" means
  N1STAR-PROOF.md there. The rows now cite `docket68/n1star/GLUEDECAY5.md`, and the program's row says "the distance
  behind c", as section 8.7 does, in place of κ.
- (4) *The letter.* ϰ (U+03F0) is a glyph variant of κ, which the paper uses for the second fundamental form (:605-606).
  Counted in the paper:
  - lowercase Greek letters at zero occurrences: only ι and υ, which read as i and the paper's v;
  - capitals: Δ, Λ and Ξ, whose lowercase forms are in use;
  - ξ: only in two quotations, as a frequency (:538, :582).

  The size is now Ξ, with Ξ0 and Ξ1.
- (5) *E4's centre of mass.* For $h = x_1\,x\otimes x\,r^{-a-3}$, the terms of $\mathfrak b_{e'_1}$ with the gradient of
  $N = x_1$ cancel: $h_{i1}x_i = x_1^2r^{-a-1} = x_1\,\mathrm{tr}\,h$. So dropping them could not be caught. E4 adds $h
  = x_1\delta\,r^{-a-1}$, of order $a$. By hand:
  - $\partial_jh_{ij}-\partial_i\mathrm{tr}\,h = -3\delta_{i1}r^{-a-1}+3(a+1)x_1x_ir^{-a-3}$, so the $N$ part is
    $3a\,x_1^2r^{-a-2}$;
  - the gradient part is $-(h_{i1}-\delta_{i1}\mathrm{tr}\,h)\hat x_i = 3x_1^2r^{-a-2}$;
  - the flux is therefore $\frac32(a+1)\pi^2\rho^{3-a}$, against $\frac32a\pi^2\rho^{3-a}$ without the gradient terms.

  E4 asserts $\frac32(a+1)\pi^2$, nonzero at the three sample orders it checks ($a = \frac74,\frac52,\frac72$). The
  reader's control (iv) is the mutant 'drop_lapse', and it fails.
- (6) *The header.* Line 3's "not yet read by a second reader" and the R2.0 note's "section 8.2 is the current proposal"
  are now noted as stale.

*The program.* E4 and E6 are as above. The mutants are 21 in all, each failing:
- E1: lebesgue;
- E2: no_osc, ss_sign, lam_max;
- E3: coef3, second_r3, mu0;
- E4: no_decouple, box_strong, energy_trsign, mom_drop_x, p3_strong, box_weak, drop_lapse;
- E5: mass, dim3;
- E6: char_a, char_b, drop_c, drop_m3, seated_keep_old_a.

The program was run in full with `nice -n 10`.

*Ledger.* `checks/gluedecay5.py` E1-E6: all PASS, with all 21 mutants failing; output in `checks/gluedecay5.out`; E6
reports the paper before seating. Section 8.4 (h) carries the md5 of this round's gluedecay5.py, gluedecay5.out and
PART-V-GLUING.md, and zeros for GLUEDECAY5.md. The step after seating is named in section 8.4. Open: nothing.

## R5.0 Round 5 (2026-11-06): the fourth reading, re-derived and seated

*The reading.* The fourth reader found round 4's Minor 1 and all six nits seated, and the new flux right. It found Minor
2 only half repaired, and raised three nits. Each is re-derived and seated below, with the old text kept and bracketed
notes where it changes. The paper and N1STAR-PROOF.md are not edited.

(Minor) *E6 in the seated state.* Re-derived from round 4's E6. Its mutants changed the old blocks (char_a, char_b), the
applying step (drop_c) or the applied copy (seated_keep_old_a). All of these sit on the path taken before seating. On a
seated paper E6 took the other path, and those four mutants left it unchanged, so they survived and the whole program
exited 1 there. Only drop_m3, which changes a new block, was caught.

The repair:
- *Both texts in every run.* E6 builds the state the paper is not in from the one it finds, and checks both, naming the
  state it found. Before seating, it applies all eight blocks and fills the zero md5. Seated, it replaces every new
  block by its old, the md5 digits blanked so that a refreshed column still matches.
- *Mutants on both texts.*
  - char_a and char_b change one character of both the old and the new block.
  - drop_c puts old (c) back in place of new (c) in the seated text.
  - seated_keep_old_a appends old (a) to the seated text.
  - drop_m3 removes M3 from new (b).

  Each therefore acts in either state.
- *`--paper PATH`.* The program checks another copy of the paper, so a reader can run it against a seated copy without
  copying the tree.

Run in full under `nice -n 10`:
- on the unmodified paper: exit 0; E1-E6 PASS and all 21 mutants fail; E6 names the state "before seating";
- on a seated scratch copy (all eight blocks of section 8.5 applied by an independent script, the zero md5 filled): exit
  0; E1-E6 PASS and all 21 mutants fail, the same 21; E6 names the state "seated".

The scratch copy and its output are outside the repository.

(Nit 1) *The run time.* Section 8.4's (d) and (f) said "about seventy seconds", and section 7 and the docstring "about
ninety". The program alone takes about 75-95 s wall on the loaded machine (the reader: 94 s and 85 s; here 73-88 s), and
133 s when the two states are run at once. Section 8.5's (d) and (f), section 7 and the docstring now say "about ninety
seconds".

(Nit 2) *R4.0's example.* "The data of a nearby boosted Myers-Perry metric on Hintz's surface" is not a perturbation on
$\Sigma$ (R3.0's nit 8). The example is now the translation pull-back $x\mapsto x+\chi_1(r)c$: vacuum, of order
$3<\ell_0$, its difference in $\rho^3C^\infty\times\rho^4C^\infty$ by Lemma 4.1 (b)'s proof, and so in the class. Noted
at R4.0's Minor 1.

(Nit 3) *R4.0's formatting.*
- Its nit list had sub-bullets run into the text of items (2), (4) and (5), and two paragraphs at column 0 that broke
  the list. They are now nested bullets and indented paragraphs, with the text unchanged.
- The missing blank line before "## R4.0" is restored.
- In every superseded section the block tags were renamed, so that E6 finds only the current ones: section 8.2's to
  "(round 2, x)", 8.3's to "(round 3, x)" and 8.4's to "(round 4, x)".

*Ledger.* `checks/gluedecay5.py` E1-E6: all PASS on the paper before seating and on a seated copy, with all 21 mutants
failing in each state. The output on the paper is in `checks/gluedecay5.out`, byte-identical on rerun. Section 8.5 (h)
carries the md5 of this round's gluedecay5.py, gluedecay5.out and PART-V-GLUING.md, and zeros for GLUEDECAY5.md. The
step after seating is named in section 8.5. Open: nothing.
