# Part IV$''''''$. Constraint damping III: the transition face model and tf-admissibility, n = 4 ([Hin26a] Appendix B;
[Hin26] Theorem 7.1 (4))

*Status.* Written (D310). This part proves III.E Theorem 1.1 (4) at $n = 4$: $\Box^C_b$ is tf-admissible (I.C Definition
5.1) with every weight in $[-C_0,2)$. It does so through [Hin26a] Theorem B.1 at $n = 4$ (Theorem 3.1 below), the
invertibility of the spectral family of the dilation-invariant model on 4+1 Minkowski space, which is $\Box^C_b$'s
transition face normal operator. The proof follows the source's three steps. Verified (D312): verifier 135 read it in
full; three minor findings and six nits, seated as findings (IV$''''''$6)-(IV$''''''$7) and in the text; to be read.
Proved (D315): verifier 136 read the D312 repairs, correct.

- The Fredholm property and index 0 (section 1), by radial estimates and Melrose's relative index theorem, sector by
sector on $\mathbb S^3$.

- Solvability on edge-b spaces (section 2), by the arguments of Part IV$'''''$.

- The kernel argument of the source's section B.4 (section 3).

Section 4 identifies the spaces with I.C's and verifies Definition 5.1. The inputs where $n$ enters are the record's
exact computations: the dilation structure, the weight range at the origin, the thresholds at the cone face, the matrix
$-\frac12r^2\ell(dr/r)$, section B.4's numbers and the free indicial roots (record 10.20, `tface5.py` F1-F5), the
indicial roots and their counts (Part IV$''''$ Lemma 1.3), and the 1-form's positivity (Part IV$''''$ Lemma 1.4; Part
IV$'''''$ Lemma 0.5). Source: [Hin26a] (arXiv:2606.27658v2) pp. 85-98 (Appendix B), read at source.

## 0. The model at n = 4

Let $v := \frac12$ and $e := \frac1{102400}$, $h\in(0,10^{-6}]$, $\gamma_C = h^{-1}$, and $C_0\in[\frac32,100]$. On
Minkowski space $\mathbb R_t\times\mathbb R^4_x$, $\eta = -dt^2+dr^2+r^2\slashed g$ with $\slashed g$ the round metric
of $\mathbb S^3$. Let $c := r^{-1}(dt-v\,dr)$ (the source's (B.1)) and $\Box^C := 2\delta_\eta
G_\eta(\delta^*_\eta+E^C)$, with $E^C$ the modification of Part IV$''''$ section 0 (trace weight $\frac23$). As there,
$h^2\Box^C = 2h^2\delta G\delta^*-iL_h$, with $L_h = 4ih\,\delta(c\otimes_s\cdot)+2ihe\,d\iota_{c^\sharp}$, the source's
(3.2). Let $M := [\overline{\mathbb R^{1+4}};\{r = 0\}]$ (the source's (B.3)), with faces $\mathrm{sf}$ (the lift of
$\partial\overline{\mathbb R^{1+4}}$) and $\mathrm{cf}$ (the lift of $\{r = 0\}$). Let $\mathcal T^*$ be the pullback of
the scattering cotangent bundle, with frame $dt,dx^1,\dots,dx^4$. Let $X := [\overline{\mathbb R^4};\{0\}] =
[0,\infty]_\rho\times\mathbb S^3$, $\rho = r^{-1}$, and $\mathcal T^*_X := \mathcal T^*|_X$. In $t_* := t-r$, the
spectral family is
$$\widehat{\Box^C}(\sigma) := e^{i\sigma t_*}\Box^Ce^{-i\sigma t_*}\ \text{on stationary
sections},\qquad\sigma\in\mathbb C\setminus0,\ \mathrm{Im}\,\sigma\ge0.\tag{0.1}$$

**Lemma 0.1 (the structure; the source's (B.7)-(B.12) at n = 4).**

(a) $\Box^C$ is homogeneous of degree $-2$ under $(t,x)\mapsto(\lambda t,\lambda x)$, the components of a section being
taken in the frame $dt,dx^i$; so $r^2\widehat{\Box^C}(0)\in\mathrm{Diff}^2_{\mathrm b}(X;\mathcal T^*_X)$ is dilation
invariant.

(b) In the splitting $\mathcal T^*_X\cong\bar{\mathbb R}\oplus\bar{\mathbb R}\oplus T^*\mathbb S^3$ (by $dt$, $dr$ and
$r\,d\omega$),
$$\widehat{\Box^C}(\sigma) = 2i\sigma\rho\big(\rho\partial_\rho-\tfrac32-h^{-1}\bar
S\big)+\widehat{\Box^C}(0),\qquad\widehat{\Box^C}(0)\in\rho^2\mathrm{Diff}^2_{\mathrm b}(X;\mathcal T^*_X),\tag{0.2}$$
where $\bar S$ is constant, lower block-triangular, with diagonal $2(1-v)$, $(1-e)(1-v)$ and
$(1-v)\mathrm{Id}_{T^*\mathbb S^3}$; it is diagonalisable with spectrum $\{2(1-v),(1-e)(1-v),1-v\}$, the last three
times.

(c) $\widehat{\Box^C}(\sigma)\in\rho_{\mathrm b}^{-2}\mathrm{Diff}^2_{\mathrm{sc,b}}(X;\mathcal T^*_X)$, with
$\rho_{\mathrm{sc}} := \rho/(\rho+1)$ and $\rho_{\mathrm b} := r/(r+1)$. The b-principal symbol of
$r^2\widehat{\Box^C}(\sigma)$ near $r = 0$ is $\xi_{\mathrm b}^2+|\eta_{\mathrm b}|^2$, and the scattering principal
symbol near $\rho = 0$ is $G_\sigma(\xi,\eta) = -2\sigma\xi+\xi^2+|\eta|^2$.

(d) $\widehat{\Box^C}(\sigma)$ is the transition face normal operator of $\Box^C_b$ for every $b$ near $b_0$:
$N_{\mathrm{tf}}(\hat\sigma) = \widehat{\Box^C}(\hat\sigma)$ in I.C (4.1), with $S_0 = h^{-1}\bar S = \bar S^C$ and
$N(P^{(0)})$ the normal operator of $\rho^{-2}\widehat{\Box^C}(0)$.

*Proof.* (a) is computed: in $t_*$ and Cartesian $x$, the coefficient of every $k$-th order derivative of $\Box^C$ is
homogeneous of degree $k-2$ in $x$, on each of its 147 terms (record Proposition 10.20 (i), `tface5.py` F1, exact). (b)
The form (0.2), with $\bar S$, is Part IV$''''$ Lemma 1.2's (1.1) on the model, where $\tilde S$, $Q$ and $R$ vanish ($g
= \eta$, $c$ exactly $r^{-1}(dt-v\,dr)$; record Proposition 10.18 (i), `cpmodes5.py` K1). The $\frac32 = \frac{n-1}2$ is
the shift that makes $i(\rho^2\partial_\rho-k\rho)$ symmetric on $L^2(\rho^{-4}\frac{d\rho}\rho)$. Integrating by parts,
$i(\rho^2\partial_\rho-k\rho)$ has adjoint $i(\rho^2\partial_\rho+(1-m+k)\rho)$ on $L^2(\rho^{-m}\frac{d\rho}\rho)$,
symmetric iff $k = \frac{m-1}2$, and here $m = 4$. Diagonalisability: the $2\times2$ block has the distinct eigenvalues
$2(1-v)\ne(1-e)(1-v)$, and the angular block is scalar. (c) The memberships follow from (0.2) and (a). The symbols are
those of the source, computed from $\rho^2(\rho\partial_\rho)^2$, $\rho^2\Delta_{\mathbb S^3}$ and
$2i\sigma\rho^2\partial_\rho$: $\mathrm{Diff}^1_{\mathrm b}$-terms of $\widehat{\Box^C}(0)$ are subprincipal at both
ends. (d) I.C (4.1) defines $N_{\mathrm{tf}}$ from the data of $\hat P$ at $\rho = 0$, namely $S_0$ and $N(P^{(0)})$.
Part IV$''''$ Lemma 1.2 gives these for $\Box^C_b$ as $\bar S^C = h^{-1}\bar S$ and the normal operator of the model,
independent of $b$ ($g_b-\eta\in\rho^2C^\infty$, $c_C$ minus the model's 1-form in $\rho^3C^\infty$, Part IV$''''$ Lemma
1.3's proof). The model's spectral family is (0.2), so the two agree. $t_*$ differs from Part IV$''''$'s $t-\psi(|x|)$
by a constant plus $O(\rho)$, which does not change the data at $\rho = 0$. $\square$

*Spaces.* $H^{s,(\ell,\beta)}_{\mathrm{sc,b}} := \rho_{\mathrm{sc}}^\ell\rho_{\mathrm b}^\beta
H^s_{\mathrm{sc,b}}(X;\mathcal T^*_X)$, with $L^2$ taken for the Euclidean density $r^3|dr\,d\slashed g| =
\rho^{-4}\frac{d\rho}\rho|d\slashed g|$ (the source's $r^2|dr\,d\slashed g|$) and a fibre inner product fixed below.
$\ell$ may be a variable order on ${}^{\mathrm{sc}}T^*_{\partial_{\mathrm{sc}}X}X$. Near $r = 0$, $H^{s,\beta}_{\mathrm
b}(r^3dr) = H^{s,\beta-2}_{\mathrm b}(\frac{dr}r)$: the b-weight is $\beta-2$ (record Proposition 10.20 (ii)). The
radial sets over $\rho = 0$ for $\sigma = \pm1$ are $R_{\mathrm{out}} := \{\xi = \eta = 0\}$ (the zero section) and
$R_{\mathrm{in}} :=
\{\xi = 2\sigma,\eta = 0\}$, and for $\mathrm{Im}\,\sigma>0$ the characteristic set over $\rho = 0$ is
$R_{\mathrm{out}}$ (the source's (B.15)-(B.18), free of $n$).

**Definition 0.2 (admissible orders; the source's (B.13) at n = 4).** $(s,\ell,\beta)$ is *admissible at $\sigma$* if
$\beta\in(0,2+C_0]$, $\ell<-\frac12+h^{-1}(1-e)(1-v)$ at $R_{\mathrm{out}}$, and, when $\sigma = \pm1$,
$\ell>-\frac12-h^{-1}(1-e)(1+v)$ at $R_{\mathrm{in}}$, with $\ell$ constant near $R_{\mathrm{in}}$, $R_{\mathrm{out}}$
and non-increasing along $\sigma H_{G_\sigma}$.

## 1. Fredholm property and index 0 ([Hin26a] Proposition B.2 at n = 4)

**Proposition 1.1.** For $(s,\ell,\beta)$ admissible at $\sigma\in e^{i[0,\pi]}$,
$$\widehat{\Box^C}(\sigma):\{\omega\in H^{s,(\ell,\beta)}_{\mathrm{sc,b}}:\widehat{\Box^C}(\sigma)\omega\in
H^{s-2,(\ell+1,\beta-2)}_{\mathrm{sc,b}}\}\to H^{s-2,(\ell+1,\beta-2)}_{\mathrm{sc,b}}\tag{1.1}$$
is Fredholm of index 0, and its nullspace and the annihilator of its range do not depend on the admissible
$(s,\ell,\beta)$. The estimates
$$\|\omega\|_{H^{s,(\ell,\beta)}_{\mathrm{sc,b}}}\le
C\big(\|\widehat{\Box^C}(\sigma)\omega\|_{H^{s-2,(\ell+1,\beta-2)}_{\mathrm{sc,b}}}
+\|\omega\|_{H^{s_0,(\ell_0,\beta_0)}_{\mathrm{sc,b}}}\big)\tag{1.2}$$
(for admissible $s_0<s$, $\ell_0<\ell$, $\beta_0<\beta$, in the strong sense) and its dual (the source's (B.28)) hold
uniformly for $\sigma$ in $e^{i[0,\pi-\delta]}$ near $1$ and in $e^{i[\delta,\pi]}$ near $-1$, for fixed orders
admissible there.

*Proof.* *Real $\sigma$*, say $\sigma = 1$ ($\sigma = -1$ by reversing the propagation). Off the characteristic set the
operator is elliptic, by Lemma 0.1 (c). Over $\rho = 0$:

- *Sink $R_{\mathrm{out}}$.* With the commutant (B.21), $a =
\rho^{-\ell-\frac12}\chi_0(\rho)\chi_1(|\eta|^2)\chi_2(\xi)$, the principal symbol of $\frac
i2[\widehat{\Box^C}(\sigma),A^2]$ is (B.23). That of
$\frac1{2i}(\widehat{\Box^C}(\sigma)-\widehat{\Box^C}(\sigma)^*)A^2$ adds at the zero section the shift (B.24). By Lemma
0.1 the shift comes only from $-2i\sigma\rho h^{-1}\bar S$.
$\widehat{\Box^C}(0)-\widehat{\Box^C}(0)^*\in\rho^2\mathrm{Diff}^1_{\mathrm b}$, whose quotient by $\rho$ has scattering
symbol vanishing at $(\xi,\eta) = 0$. $2i\sigma(\rho^2\partial_\rho-\frac32\rho)$ is symmetric on
$L^2(\rho^{-4}\frac{d\rho}\rho)$ (Lemma 0.1 (b)), so its imaginary part lies in $\rho^2C^\infty$ for any fibre inner
product. Taking the fibre inner product for which an eigenbasis of $\bar S$ is orthonormal (Lemma 0.1 (b)), the shift is
$-2h^{-1}\bar S$, which gives (B.25). The main term $(2\ell+1)(\sigma-\xi)-2h^{-1}\bar S$ is negative near the zero
section iff $\ell<-\frac12+h^{-1}\min\mathrm{spec}\,\bar S = -\frac12+h^{-1}(1-e)(1-v)$; this is (B.26).

- *Source $R_{\mathrm{in}}$.* The isometry $t\mapsto-t$ of $\eta$ pulls $c_v := r^{-1}(dt-v\,dr)$ back to $-c_{-v}$, so
it conjugates $\Box^C$ with $(c_v,h^{-1})$ to the operator with $(c_{-v},-h^{-1})$. On stationary sections, $e^{2i\sigma
r}\widehat{\Box^C}(\sigma)e^{-2i\sigma r}$ is the pullback of the spectral family at $-\sigma$ of that operator, by the
source's identity after (B.27), which is free of $n$. With an eigenbasis of $\bar S_{-v}$ orthonormal, the shift at
$R_{\mathrm{in}}$ is $(-1)(-2(-h^{-1})\bar S_{-v})$. $\bar S_{-v}$ has spectrum $\{2(1+v),(1-e)(1+v),1+v\}$, with bottom
$(1-e)(1+v)$. The threshold is $\ell>-\frac12-h^{-1}(1-e)(1+v)$ (record Proposition 10.20 (iv): the bottom
$S_{\mathrm{in}}$ of the adjoint's $\tilde S$, the same number).

- In between, real principal type propagation applies along $\mathrm{Char}_\sigma$, which flows from $R_{\mathrm{in}}$
to $R_{\mathrm{out}}$ by (B.16).

The regularisation argument gives the strong form, and this proves (B.20), whose error term carries the b-weight
$\beta$. Near $r = 0$ the operator $r^2\widehat{\Box^C}(\sigma)$ is b-elliptic (Lemma 0.1 (c)), with Mellin transformed
normal operator that of $r^2\widehat{\Box^C}(0)$. By (a) and the inversion $\rho = r^{-1}$, its indicial roots at $r =
0$ are $-\mu$, with $\mu$ running over those of Part IV$''''$ Lemma 1.3 at infinity. These have
$\mathrm{Re}\,\mu\notin[-100,\frac{19}{10}]$, and only $\mu = 2$ in $[-100,2]$. So no root at $0$ has real part in
$(-2,100]$, and the b-weight $\beta-2\in(-2,C_0]$ is root-free. With $[\beta_0-2,\beta-2]$ root-free as well, the
inverse Mellin transform of the normal operator gives (1.2) from (B.20) (record Proposition 10.20 (ii); the source's
argument on p. 89). The dual estimate is the same with the propagation reversed.

*Complex $\sigma$.* Only $R_{\mathrm{out}}$ is characteristic. Write $\sigma^{-1}\widehat{\Box^C}(\sigma) = P-iQ$ as in
(B.29), with $Q_0 = 2\rho h^{-1}\bar S$, $P_1 = \mathrm{Re}\,2i(\rho^2\partial_\rho-\frac32\rho)$, and $Q_3 =
(\mathrm{Im}\,\sigma)\mathrm{Re}\,\widehat{\Box^C}(0)$ a nonnegative absorption. With the same commutant, the
zero-section symbol is $(2\ell+1-2h^{-1}\bar S)\rho^{-2\ell}$. $-AQ_3A$ has the main term's sign, because the
b-principal symbol of $\widehat{\Box^C}(0)$ is $\xi_{\mathrm b}^2+|\eta_{\mathrm b}|^2$, so $\widehat{\Box^C}(0) =
\sum_jT_j^*T_j+R$ with $T_j\in\rho\mathrm{Diff}^1_{\mathrm b}$ and $R\in\rho^2\mathrm{Diff}^1_{\mathrm b}$. The rest is
subprincipal or elliptic, as in the source's p. 90. *Uniformity* in $\sigma$ near $\pm1$ is the limiting absorption
principle: the full Hamilton field on the cut-offs keeps the sign structure of (B.23), as the source notes on p. 91.

So (1.1) is Fredholm, and by (1.2) and elliptic and propagation regularity its nullspace consists of elements in every
admissible space; it is the same for every admissible $(s,\ell,\beta)$. The annihilator of the range is the nullspace of
the adjoint on the dual spaces; by the dual estimate (B.28) and the adjoint's propagation regularity it too consists of
elements of every dual space, so it does not depend on the orders either, as in I.C Theorem 4.3 (3)'s proof. Hence the
index does not depend on the admissible orders (amended D312, finding (IV$''''''$6)).

*Index 0.* $\widehat{\Box^C}(\sigma)$ commutes with the rotations of $\mathbb S^3$, and with the dilations up to the
factor of (a). Decompose sections of $\mathcal T^*_X$ by harmonics on $\mathbb S^3$ (III.A$'$): scalar type of degree
$l\ge0$ (three components for $l\ge1$, the $dt$, $dr$ and gradient parts; two for $l = 0$), and vector type of degree
$l\ge1$ (one component, the co-closed 1-forms on $\mathbb S^3$). The projections onto a type and degree are bounded on
the spaces with rotation-invariant orders (I.C Proposition 5.3's proof), and $\widehat{\Box^C}(\sigma)$ commutes with
them. So (1.1) is the direct sum of its restrictions to the sectors. Each restriction is Fredholm, and only finitely
many have nonzero kernel or cokernel, the total ones being finite-dimensional. Fix a sector and write $I$ for its index
on (1.1), with $\ell$ a variable order $>-\frac12$ at $R_{\mathrm{in}}$ and $<-\frac12$ at $R_{\mathrm{out}}$. Take for
$\ell$ I.C's order for the free operator at this $\sigma = e^{i\theta}$: I.A Lemma 7.1's with $\theta_{\mathrm{in}} = 0$
and $\bar S = 0$ for $\theta\in\{0,\pi\}$, or $r_{\mathrm{mid}}$ for $\theta\in(0,\pi)$. It is invariant under the
rotations of $\mathbb S^3$, $>-\frac12$ at $R_{\mathrm{in}}$ and $<-\frac12$ at $R_{\mathrm{out}}$, so it is admissible
for every $h^{-1}\ge0$; as the index does not depend on the admissible orders, $I$ is the sector's index for all of them
(verifier 135's A-m2).

(i) *Lowering $\beta$.* In the sector, $\widehat{\Box^C}(0)$ has finitely many indicial roots at $r = 0$, continuous in
$h^{-1}\in[0,h_{\mathrm f}^{-1}]$, $h_{\mathrm f}\in(0,10^{-6}]$ the value at hand (verifier 135's A-m1) ((0.2): they
are the roots of the sector's indicial polynomial, whose coefficients are polynomial in $h^{-1}$ with leading
coefficient free of it). Fix $\beta_1$ below all of them for all such $h^{-1}$. Moving the weight from $\beta$ to
$\beta_1$ raises the index by the number of roots, with multiplicity, whose real part lies in $[\beta_1-2,\beta-2)$.
This is Melrose's relative index theorem ([Mel93] Theorem 6.5, cited by the source on p. 91 for this step; a theorem on
b-operators in every dimension, not re-read here). These are the roots $-\mu$ with $\mathrm{Re}\,\mu\ge2$: two in the
scalar sector $l = 0$, three in each scalar sector $l\ge1$, one in each vector sector (Part IV$''''$ Lemma 1.3 (a): as
many roots have real part $\ge2$ as below $-100$, three, two or one per type and degree). The index becomes $I+m$, with
$m = 2,3,1$.

(ii) *Removing the damping.* Deform $h^{-1}$ to $0$ at the weight $\beta_1$. The family is continuous in operator norm
between the fixed spaces, as the $h^{-1}$-terms ($2i\sigma\rho h^{-1}\bar S$, and the first-order part
$h^{-1}\rho^2\tilde Q$ of $\widehat{\Box^C}(0)$ from $L_h$) map $H^{s,(\ell,\beta_1)}$ boundedly to
$H^{s-2,(\ell+1,\beta_1-2)}$. It stays Fredholm, by the estimates above, whose thresholds hold for every $h^{-1}\ge0$
with this $\ell$ and whose weight $\beta_1$ stays root-free. So the index $I+m$ is kept at $h^{-1} = 0$. There the
operator is $2\delta_\eta G_\eta\delta^*_\eta = \Box_\eta$ on 1-forms ($\mathrm{Ric}(\eta) = 0$), acting componentwise
in the frame $dt,dx^i$.

(iii) *Raising $\beta$ for the free operator.* Its roots at $r = 0$ are $-3,-2\,|\,0,1$ in the scalar sector $l = 0$,
$-l-3,-l-2,-l-1\,|\,l-1,l,l+1$ in the scalar sector $l\ge1$, and $-l-2\,|\,l$ in the vector sector (record Proposition
10.20 (v), `tface5.py` F5, from `gaugepot5.py`'s indicial determinants at $\gamma = 0$, each simple). The window between
the groups contains $(-2,0)$. Raising $\beta_1$ to $\beta_2$ with $\beta_2-2\in(-2,0)$ crosses $2$, $3$ or $1$ roots and
lowers the index by as many, to $I$. On these spaces $\widehat{\Box_\eta}(\sigma)$ is invertible: it is
$N_{\mathrm{tf}}$ of the free operator, which is tf-admissible with every weight in $(0,2)$ (I.C Proposition 5.3, whose
data are those of $\Box_\eta$ componentwise). By I.C Corollary 5.2 (a) it is invertible on I.C's spaces with
$q\in(0,2)$, the free gap being $(0,2)$, and these are the spaces here with $\beta = q$ and $\ell$ the order fixed above
(section 4's identification, which uses only the definitions); take $\beta_2 := q$. So $I = 0$ in every sector, and the
index of (1.1) is $0$. $\square$

## 2. Solvability on edge-b spaces ([Hin26a] Theorem B.4 at n = 4)

On $M$ the edge-b vector fields are spanned by $r\partial_t$, $r\partial_{x^i}$. Unit cells
$(2^j(k-2),2^j(k+2))_t\times(2^{j-2},2^{j+2})_r\times\slashed U_\beta$, with $\slashed U_\beta$ charts of $\mathbb S^3$,
give the parameterised scaled bounded geometry. On it $P_h := h^2\Box^C = \Box_h-iL_h\in
r^{-2}\mathrm{Diff}^2_{\mathrm{eb},\hbar}(M;\mathcal T^*)$ has principal symbol $G-i\ell$ (Part IV$'''''$ Lemma 0.2 (d)
on the model). $H^{s,(\alpha_{\mathrm{sf}},\alpha_{\mathrm{cf}})}_{\mathrm{eb},h}$ is weighted with $L^2(|dg|)$, $|dg|
= |dt\,dx| = r^4|dt\,\frac{dr}r\,d\slashed g|$, and the fibre inner product $B$ of Part IV$'''''$ Lemma 0.4. $\Omega :=
\{t\ge0\}$, $X_0 := \{t = 0\}$ and $\tau := t/r$.

**Theorem 2.1 ([Hin26a] Theorem B.4 at n = 4).** Let $\alpha_{\mathrm{sf}}<b^*-1$ and $\alpha_{\mathrm{cf}}>1-b^*$, with
$b^* = 0.99340731\ldots$ the smaller root of $204795d^2-409605d+204801$ (record Proposition 10.20 (iii)), and $C_1>0$.
There is $h_0>0$ such that for $h\in(0,h_0)$:

(1) for $s\in[-C_1,C_1]$ the forcing problem $\Box^C\omega = f\in\dot
H^{s-1,(\alpha_{\mathrm{sf}}+2,\alpha_{\mathrm{cf}}-2)}_{\mathrm{eb}}(\Omega)$ has a solution $\omega\in\dot
H^{s,(\alpha_{\mathrm{sf}},\alpha_{\mathrm{cf}})}_{\mathrm{eb}}(\Omega)$. It is unique among solutions whose
restrictions to $\Omega_{\le t_0} := \Omega\cap\{t\le t_0\}$ lie in
$H^{-N,(-N,\alpha_{\mathrm{cf}})}_{\mathrm{eb}}(\Omega_{\le t_0})^{\bullet,-}$ for all $t_0$ and some $N\le C_1$;

(2) the initial value problem with $f\in\bar
H^{0,(\alpha_{\mathrm{sf}}+2,\alpha_{\mathrm{cf}}-2)}_{\mathrm{eb}}(\Omega,|dg|)$ and
$$(\omega,r\mathcal L_{\partial_t}\omega)|_{X_0}\in\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}+\frac12}
\rho_{\mathrm{cf}}^{\alpha_{\mathrm{cf}}-\frac12}
\big(\bar H^1_{\mathrm b}\oplus\bar H^0_{\mathrm b}\big)(X_0,r^3|dr\,d\slashed g|)\tag{2.1}$$
has a solution $\omega\in\bar H^{1,(\alpha_{\mathrm{sf}},\alpha_{\mathrm{cf}})}_{\mathrm{eb}}(\Omega)$, unique among
solutions whose restrictions to every $\Omega_{\le t_0}$ lie in $\bar H^{1,(-N,\alpha_{\mathrm{cf}})}_{\mathrm{eb}}$ for
some $N$.

*Proof.* The proof is Part IV$'''''$'s for Theorem 7.3, on $M$ instead of $M^\flat$, with these differences.

*Energy near $X_0$.* $\eta = r^2(-d\tau^2-2\tau\,d\tau\frac{dr}r+(1-\tau^2)\frac{dr^2}{r^2}+\slashed g)$ is a weighted
b-metric on $(-1,1)_\tau\times[0,\infty]_r\times\mathbb S^3$. Here $r^2\eta^{-1}(d\tau,d\tau) = -(1-\tau^2)$, and
b-norms on $\{t/r\in I\}$ are edge-b norms. Part IV$'''''$ Proposition 6.1's proof (Lemma 5.14 and Corollary 5.15 of the
source, stated in every dimension, with charts on $\mathbb S^3$ and level-set density $r^4|dr\,d\slashed g|$) gives the
source's (B.34) and (B.35) at $T := \frac12$, with $\rho_{\mathrm{sf}} = (1+r)^{-1}$ and $\rho_{\mathrm{cf}} =
r(1+r)^{-1}$ there.

*Nonzero and infinite frequencies.* (B.37) is Part IV$'''''$ Proposition 1.3 with the cut-offs $\chi_j(\tau)$ of (B.36)
and no cut-off in $r$. There is no $E_r$ term; the $E_\tau$ term is a negative square because $\pm H_G\tau>0$ at future,
resp. past, lightlike covectors, $d\tau$ being past timelike on $\mathrm{supp}\,\chi'_1$.

*The source at $\mathrm{cf}$.* Use $\mathcal L_h := -i(1+iCL^*_hr^2)P_h = -L_h+J-iQ$ as in Part IV$'''''$ (2.1), with
$r^{-1}$ for $\rho_{\mathrm{sf}}$. In $t\ge-\frac r2$ let $\rho_{\mathrm{sf}} := (t+r+1)^{-1}$ and $\rho_{\mathrm{cf}}
:= r(t+r+1)^{-1}$. Take the commutant $a = w^{-1}\chi_{\mathrm{cf}}(\mathfrak X\rho_{\mathrm{cf}})\chi_0(\mathfrak
X|\zeta|)\chi_1(t/r)$, $w := \rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}+1}\rho_{\mathrm{cf}}^{\alpha_{\mathrm{cf}}-1}$.
The symbol identity is (B.38): $aH_{-\ell+j}a-Sa^2 = -c_0r^{-2}a^2-b_0^2-b_{\mathrm{cf}}^2+e_\tau^2+f$. Since
$\frac{dw}w\equiv(\alpha_{\mathrm{cf}}-1)\frac{dr}r$ modulo $\rho_{\mathrm{cf}}C^\infty(M;{}^{\mathrm{eb}}T^*M)$, the
square roots exist for the following reasons.

- $b_0$: $r^2(-\ell(dw/w)+S)$ at $\rho_{\mathrm{cf}} = 0$ is the record's $T$ at $\rho_K = 0$ with $d =
1-\alpha_{\mathrm{cf}}$. It is positive definite iff $d<b^*$, that is $\alpha_{\mathrm{cf}}>1-b^*$ (record Proposition
10.20 (iii), `cform5.py` C7, exact: positive definite at $d = 0.9934$ and not at $0.9935$). Positivity extends to
$\mathrm{supp}\,a$ for $\mathfrak X$ large, and $w^{-1}H_jw$ vanishes at $o$.

- $b_{\mathrm{cf}}$: $-\frac12r^2\ell(dr/r)$ has characteristic polynomial
$(\lambda-v)^3(\lambda^2-(3-e)v\lambda+(2-e)v^2-e)$. At $(v,e) = (\frac12,\frac1{102400})$ its roots are positive
(record Proposition 10.20 (iii), F3). It is $B$-self-adjoint (Part IV$'''''$ Lemma 0.4, his Lemma 3.3), so it is
$B$-positive definite. $d\rho_{\mathrm{cf}}/\rho_{\mathrm{cf}}\equiv dr/r$ modulo $\rho_{\mathrm{cf}}$, and
$-\chi_{\mathrm{cf}}\chi'_{\mathrm{cf}}\ge0$.

- $e_\tau$: $d(t/r)$ is past timelike on $\mathrm{supp}\,\chi'_1$, so $r^2\ell(d(t/r))$ is negative definite (Part
IV$'''''$ Lemma 0.4).

- $f$ is elliptic.

This gives (B.39), whose a priori term lies in $\tau\le\frac{2.75}{10}T$, covered by (B.34); and (B.40) for $P^*_h$
likewise.

*The other zero-section estimates.* The model is stationary and dilation invariant (Lemma 0.1 (a)). So each rescaled
symbol of the commutator arguments at a point of $\Omega^\circ$, such as $r^2\ell(d(r/t))$ or $r^2S$, is a function of
$s := r/t$ and $\omega$; the derivatives of the weights enter only through bounded terms, which the escape terms
dominate. The 1-form is the Minkowski model's, for which Part IV$'''''$ Lemma 0.5 (4)-(6) are computed at $\mathrm{sf}$
(10.14 (iv), `cform5.py` C5, C7). At $s\to0$, $-r^2\ell(ds) = 2s\,(-\frac12r^2\ell(dr/r))+O(s^2)$ is positive by the
$b_{\mathrm{cf}}$ positivity, so $\delta_r$ may be shrunk. Fix $\delta_r>0$ so small that the $b_0$ positivity at
$\mathrm{cf}$ holds on $\{\rho_{\mathrm{cf}}\le4\delta_r\}$ (it is constant along $\mathrm{cf}$, and
$\mathrm{cf}\cap\Omega$ is a product $[0,\infty]_t\times\mathbb S^3$ up to the dilations), and that (6) holds on
$\mathrm{sf}\cap\{s\in[\delta_r,v(1-\delta_{\mathrm{sf}})]\}$. Then:

(a) (B.39) and (B.40) hold on $\{\rho_{\mathrm{cf}}\le4\delta_r\}\cap\{\tau\ge\frac T{40}\}$, globally in $t$, with a
priori sets in $\{\tau\le\frac{2.75}{10}T\}$ and in $\{\frac52\delta_r\le\rho_{\mathrm{cf}}\le4\delta_r\}$ respectively.

(b) Part IV$'''''$ Proposition 5.2 (b)-(c) hold with $s = r/t$ near $\mathrm{sf}$ on
$[\delta_r,v(1-\delta_{\mathrm{sf}})]$ and $[v(1+\delta_{\mathrm{sf}}),10]$, and Proposition 4.1 at the sink $s = v$
(with $\alpha_{\mathrm{sf}}<b^*-1$), by their proofs, which use only these signs. For $\eta$, $\langle c,ds\rangle =
(s-v)/(rt)$, so the flow of $-rc^\sharp$ moves $s$ towards $v$ from both sides.

(c) Part IV$'''''$ Proposition 5.3 (1)-(2) hold on compact subsets of $\Omega\cap\{\rho_{\mathrm{cf}}\ge2\delta_r\}$,
with the escape functions $t+\kappa r$ and $t$ and the cut-off $t-\kappa r$ ($d(t-\beta r)$ is past timelike for
$|\beta|<1$ on $\eta$). The cut-off $\chi_r(r)$ at $\Sigma^\sharp$ is replaced by $f(\rho_{\mathrm{cf}}/(2\delta_r))$,
with $f$ non-decreasing, $0$ near $[0,\frac12]$ and $1$ on $[1,\infty)$. Its term is
$f'\cdot(-\ell(d\rho_{\mathrm{cf}}))/(2\delta_r)\ge0$, as $-\ell(d\rho_{\mathrm{cf}})>0$ near $\mathrm{cf}$
($d\rho_{\mathrm{cf}}/\rho_{\mathrm{cf}}\equiv dr/r$, the $b_{\mathrm{cf}}$ positivity). So it needs a priori control on
$\{\delta_r\le\rho_{\mathrm{cf}}\le2\delta_r\}$ in the forward direction and has the main term's sign in the adjoint one.

*Combination.* *Forward*:

- (B.34) on $\{\tau\le\frac12\}$ and (B.37);

- (a) forward;

- (c) (1) on every compact subset of $\Omega\cap\{\rho_{\mathrm{cf}}\ge2\delta_r\}$, from (B.34) and (a), with
$\epsilon_X\le\delta_rT$ so that its set $\{\frac12\epsilon_X\le t\le\epsilon_X\}$ lies under (B.34), as
$\tau\le\epsilon_X/\delta_r$ on $\{\rho_{\mathrm{cf}}\ge\delta_r\}$ (verifier 135's A-n6);

- (b) along $\mathrm{sf}$ from $s\in[2\delta_r,3\delta_r]$ (by (a), as $\rho_{\mathrm{cf}} =
s/(1+s)+O(\rho_{\mathrm{sf}})$ near $\mathrm{sf}$) and from $s\in[5,10]$ (by (B.34)), their interior a priori sets by
(c);

- the sink, its a priori sets by (b) and (c).

These cover a neighbourhood of $o$ over $\Omega$: near $\mathrm{cf}$ by (a) and (B.34), near $\mathrm{sf}$ by (a), (b),
the sink and (B.34), and the compact rest by (c). This gives the source's (B.41) at the Sobolev order 1, and at every
order $\ge1$ by extension and restriction. *Adjoint*:

- the sink (free);

- (b) (2) outward along $\mathrm{sf}$, the sf-cut-off terms having the good sign;

- (c) (2) on compact subsets of $\Omega\cap\{\rho_{\mathrm{cf}}\ge2\delta_r\}\cap\{\tau>\kappa\}$, the set of Part
IV$'''''$ Proposition 7.2 (viii) ($t-\kappa r>0$; there $t\ge2t_1$ once $t_1<\delta_r/9$, as
$\rho_{\mathrm{cf}}\ge2\delta_r$ gives $r\ge2\delta_r$), which contains the a priori set of (B.40), its $\chi_2(\tau)$
being supported in $\tau\ge\frac{2.25}{10}T>\kappa$ (amended D312, finding (IV$''''''$7)); its late set (large $t$,
$r\le(t+c_1)/\kappa$, $\rho_{\mathrm{cf}}\ge\delta_r$) lies near $\mathrm{sf}$ with $s\in[\delta_r,10]$, by $\kappa =
\frac19$, covered by the previous two steps;

- (a) adjoint, i.e. (B.40), its a priori set $\{\frac52\delta_r\le\rho_{\mathrm{cf}}\le4\delta_r\}$ covered by (c) (2)
and, near $\mathrm{sf}$, by (b) (2);

- (B.35), its a priori set $\tau^{-1}([\frac T2,T])$ covered by the steps before.

Each step's a priori set lies in an earlier step's controlled set, as in Part IV$'''''$ Propositions 7.1-7.2. Duality,
extension and restriction, and the initial value problem are Part IV$'''''$ Theorem 7.3's arguments with these
estimates. The data weights in (2.1) follow because $|dg| = r^4|dt\,\frac{dr}r\,d\slashed g| = r\,|d\tau|\otimes
r^3|dr\,d\slashed g|$ on $\{t/r\in I\}$, so the weights shift by $\frac12$ at both faces (record Proposition 10.20 (iv)).

*Strong uniqueness.* By finite speed of propagation for wave equations with smooth coefficients in $\{r>0\}$, a solution
vanishing on $\{t\le0\}$ vanishes on $\{0\le t\le1,r>t\}$. On $\Omega' := \mathrm{cl}\{0\le t\le1,r\le1-t\}$ the a
priori estimate $\|\omega\|_{\rho_{\mathrm{cf}}^{\alpha_{\mathrm{cf}}}H^s_{\mathrm{eb},h}(\Omega')^{\bullet,-}}\le
Ch^{-1}\|P_h\omega\|_{\rho_{\mathrm{cf}}^{\alpha_{\mathrm{cf}}-2}H^{s-1}_{\mathrm{eb},h}(\Omega')^{\bullet,-}}$ holds.
It is proved by the energy estimates near $X_0$ and near the final surface $\{r = 1-t\}$ (spacelike, with $d(1-t-r)$
past timelike; localisation in $(t-1)/r$), together with (B.37) and (B.39). So a solution with zero source that is
supported in $\{t\ge0\}$ and lies in that space vanishes on $\Omega'$, hence on $\{0\le t\le\frac12\}$. Translating in
$t$, which commutes with $\Box^C$, and iterating gives vanishing for all $t$. $\square$

## 3. The kernel and [Hin26a] Theorem B.1 at n = 4

**Theorem 3.1 ([Hin26a] Theorem B.1 at n = 4).** There is $h_{\mathrm{tf}}>0$ such that for $h\in(0,h_{\mathrm{tf}})$,
every $\sigma\in e^{i[0,\pi]}$ and every $(s,\ell,\beta)$ admissible at $\sigma$, the map (1.1) is invertible, with
inverse bounded uniformly for $\sigma$ in each sector where fixed orders are admissible (Proposition 1.1).

*Proof.* By Proposition 1.1 it suffices to show that the nullspace is trivial for one admissible choice. Take $\ell :=
-\frac12$ and $\beta := \frac72$, admissible as $C_0\ge\frac32$ (record Proposition 10.20 (iv): $-\frac12$ lies in every
window, and $\frac72\in(0,2+C_0]$). Apply Theorem 2.1 with $(\alpha_{\mathrm{sf}},\alpha_{\mathrm{cf}}) :=
(-\frac52,\frac52)$, which satisfy $\alpha_{\mathrm{sf}}<b^*-1$ and $\alpha_{\mathrm{cf}}>1-b^*$. Let $h_{\mathrm{tf}}$
be Theorem 2.1's $h_0$ for these weights and $C_1 = 1$, with $h_{\mathrm{tf}}\le10^{-6}$.

Let $\omega_0\in H^{1,(\ell,\beta)}_{\mathrm{sc,b}}$ with $\widehat{\Box^C}(\sigma)\omega_0 = 0$. Then $\omega :=
e^{-i\sigma(t-r)}\omega_0$ solves $\Box^C\omega = 0$, with data $(\omega^{(0)},\omega^{(1)}) := (e^{i\sigma
r}\omega_0,-i\sigma re^{i\sigma r}\omega_0)$ at $t = 0$ (the source's (B.44)). As $\mathrm{Im}\,\sigma\ge0$,
$|e^{i\sigma r}|\le1$, and the scattering derivatives $\rho^2\partial_\rho$, $\rho\partial_\omega$ cost one power
against the b-derivatives. So $\omega^{(0)}\in\rho_{\mathrm{sc}}^{\ell-1}\rho_{\mathrm b}^\beta\bar H^1_{\mathrm b}$ and
$\omega^{(1)}\in\rho_{\mathrm{sc}}^{\ell-1}\rho_{\mathrm b}^\beta\bar H^0_{\mathrm b}$, for $r^3|dr\,d\slashed g|$. On
$X_0$, $\rho_{\mathrm{sf}}$ and $\rho_{\mathrm{cf}}$ are $\rho_{\mathrm{sc}}$ and $\rho_{\mathrm b}$. Both data lie in
(2.1)'s spaces, since $\ell-1 = -\frac32\ge\alpha_{\mathrm{sf}}+\frac12 = -2$ and $\beta =
\frac72\ge\alpha_{\mathrm{cf}}-\frac12 = 2$ (record Proposition 10.20 (iv)). Theorem 2.1 (2) gives a solution
$\omega'\in\rho_{\mathrm{sf}}^{-5/2}\rho_{\mathrm{cf}}^{5/2}\bar H^1_{\mathrm{eb}}(\Omega)$. On each $\Omega_{\le t_0}$,
$\omega$ lies in $\bar H^{1,(-N,\alpha_{\mathrm{cf}})}_{\mathrm{eb}}$: near $\mathrm{cf}$ at bounded $t$, $\omega$ is
$\omega_0$ times a smooth bounded factor, and $\omega_0\in\rho_{\mathrm b}^{7/2}H^1$ with edge-b derivatives
$r\partial_t$, $r\partial_x$; near $\mathrm{sf}$ at bounded $t$, the weight $-N$ absorbs the loss
$\rho_{\mathrm{sc}}^{-3/2}$, the edge-b derivative of $e^{i\sigma r}$ costing a further $\rho^{-1}$. So $\omega' =
\omega$ by Theorem 2.1 (2)'s uniqueness.

Suppose $\omega_0\ne0$: then $|\omega_0|\ge c>0$ on an open $U$ with $\bar U\subset\mathbb R^4\setminus0$ compact. In
$t\ge1$, $r\le t$, take $\rho_{\mathrm{cf}} = r/t$ and $\rho_{\mathrm{sf}} = 1/t$. With $T := \max(1,\sup_Ur)$,
$|\omega|\ge e^{-(\mathrm{Im}\,\sigma)r}|\omega_0|$, and
$$\int_U\int_T^\infty\rho_{\mathrm{sf}}^{-2\alpha_{\mathrm{sf}}}
\rho_{\mathrm{cf}}^{-2\alpha_{\mathrm{cf}}}|\omega|^2\,dt\,dx
\ge c'\int_U r^{-5}\,dx\int_T^\infty t^{2(\alpha_{\mathrm{sf}}+\alpha_{\mathrm{cf}})}dt = \infty,$$
as $2(\alpha_{\mathrm{sf}}+\alpha_{\mathrm{cf}}) = 0$ (record Proposition 10.20 (iv)). This contradicts
$\omega\in\rho_{\mathrm{sf}}^{-5/2}\rho_{\mathrm{cf}}^{5/2}L^2(|dg|)$. So the nullspace is trivial, and (1.1) is
invertible at $(\ell,\beta) = (-\frac12,\frac72)$, hence at every admissible choice. The uniform bound on the inverse
follows from the uniform estimate (1.2) and invertibility by the compactness argument of I.C Corollary 5.2 (b). $\square$

## 4. tf-admissibility: III.E Theorem 1.1 (4)

**Theorem 4.1 (III.E Theorem 1.1 (4) at n = 4).** For $b$ near $b_0$, $h\in(0,\min(h_*,h_{\mathrm{tf}}))$ with $h_*$ of
Part IV$''''$ (0.1), and $C_0\in[\frac32,100]$, $\Box^C_b$ is tf-admissible (I.C Definition 5.1) with every weight
$\beta_{\mathrm{tf}}\in[-C_0,2)$.

*Proof.* We check (i)-(iii) of I.C Definition 5.1.

(i) By Part IV$''''$ Lemma 1.6, $(\beta_-,2)$ with $\beta_-<-100\le-C_0$ is an indicial gap of $\widehat{\Box^C_b}(0)$,
and it contains $\beta_{\mathrm{tf}}$.

*The spaces.* Put $q := 2-\beta_{\mathrm{tf}}\in(0,2+C_0]$. I.C's spaces are $H^{s,(\mathsf
r+\alpha_+,q)}_{\mathrm{sc},b}(\mathrm{tf})$ of Definition 4.1, normed with the Euclidean density $|d\hat x|$ near both
ends. These are the spaces $H^{s,(\ell,\beta)}_{\mathrm{sc,b}}$ of section 0 with $\ell := \mathsf r+\alpha_+$ and
$\beta := q$: $X$ is $\mathrm{tf}$, $\rho_{\mathrm{sc}}$ and $\rho_{\mathrm b}$ are $\rho_{\mathrm{sctf}}$ and
$\rho_{\mathrm{ztf}}$, and the density is $r^3|dr\,d\slashed g|$ in both. I.C's $\mathcal
X_{\mathrm{tf},\theta}\to\mathcal Y_{\mathrm{tf},\theta}$ is then (1.1) at $\sigma = e^{i\theta}$, by Lemma 0.1 (d).
These orders are admissible in the sense of Definition 0.2:

- $q = \beta\in(0,2+C_0]$;

- the orders $\mathsf r_\pm$ with weight $\alpha_+$ are those of I.A Lemma 7.1 at $\sigma_* = \pm1$, constant near the
radial sets and monotone along the flow, functions of $\xi$ and $|\eta|^2$;

- their thresholds are I.A's for $\widehat{\Box^C_b}$, which are $\Box^C_b$'s data at $\rho = 0$ (I.C section 4.1 (a)):
$-\frac12+\min\mathrm{spec}\,\bar S^C$ at $R_{\mathrm{out}}$, and at $R_{\mathrm{in}}$ the bound
$-\frac12-S_{\mathrm{in}}$ with $S_{\mathrm{in}} = h^{-1}(1-e)(1+v)$ (record Proposition 10.20 (iv), section 10.21 K2).
These are Definition 0.2's.

(ii) By Theorem 3.1, $N_{\mathrm{tf}}(e^{i\theta})$ is invertible, so injective, on $\mathcal X_{\mathrm{tf},\theta}$
for every $\theta\in[0,\pi]$.

(iii) By Theorem 3.1 at $\theta = 0$, $N_{\mathrm{tf}}(1)$ is onto $\mathcal Y_{\mathrm{tf},0}$. By I.C Theorem 4.3 (3),
the annihilator of its range is $\ker_{\mathcal X^*_{\mathrm{tf},0}}N_{\mathrm{tf}}(1)^{*h}$, so this kernel is trivial.

So $\Box^C_b$ is tf-admissible with weight $\beta_{\mathrm{tf}}$. $\square$

The source's proof of [Hin26] Theorem 7.1 (4) applies Theorem B.1 at $\beta' = -\beta+\frac32-\epsilon$, with the kernel
taken on the conormal spaces $\mathcal A^{a,-\beta}(\mathrm{tf})$ of [Hin26c] Definition 5.10, and the adjoint half
through [Hin26c] (9.115). I.C Definition 5.1 is posed on the Sobolev spaces of I.C Theorem 4.3 and needs neither: $q =
2-\beta_{\mathrm{tf}}$ exactly, the $\frac32$ becoming $\frac n2 = 2$, with no $\epsilon$ (record 10.23 (e) took the
source's route).

## 5. Findings, labels and sources

(IV$''''''$1) *The adjoint half without (9.115).* The record's 10.23 (e) improved a kernel element of the adjoint at ztf
and at $R_{\mathrm{in}}$ to reach Theorem B.1's dual spaces. The thirty-second verifier noted that one comparison there,
at ztf, was not computed. Theorem 4.1 avoids it: on I.C's Sobolev spaces the adjoint's kernel is the annihilator of the
range (I.C Theorem 4.3 (3)), which Theorem 3.1's surjectivity makes trivial.

(IV$''''''$2) *The index argument at n = 4.* The source's relative index step crosses three roots in the scalar sector
$l\ge1$. At $n = 4$ it crosses two, three and one in the scalar sectors $l = 0$, $l\ge1$ and the vector sectors, both
for the damped operator (Part IV$''''$ Lemma 1.3's counts) and for the free one (record Proposition 10.20 (v)). The
counts match, which is what makes the index 0. Melrose's relative index theorem is taken as cited by the source; it is
the one input of this part not read at source.

(IV$''''''$3) *The range of $C_0$.* The source's "without loss $C_0\ge2$" becomes $C_0\ge\frac32$ (so that $\beta =
\frac72$ is admissible), and the record's computations bound $C_0\le100$. Theorem 4.1 holds for $C_0\in[\frac32,100]$.
As tf-admissibility with weight $\beta$ implies it for every weight in the gap (I.C Corollary 5.2 (c)), smaller $C_0$
follow.

(IV$''''''$4) *Thresholds.* At $n = 4$ the model's weight range at the origin is $(0,2+C_0]$, the source's being
$(\frac12,\frac32+C_0]$. The cone-face threshold is $\alpha_{\mathrm{cf}}>1-b^*$ and the sink's is
$\alpha_{\mathrm{sf}}<b^*-1$, against the source's $\frac12$ and $-\frac12$. The $l$-window keeps the source's form with
$n = 4$'s $\bar S$. All are computed (record 10.20).

(IV$''''''$5) *$h$.* Part IV$''''$'s $\mathsf H$ is to be read with $h_*$ also below $h_{\mathrm{tf}}$ (amended there,
D310).

(IV$''''''$6) *The index for every order* (verifier 135's A-m2). The index was computed for one class of orders and only
the nullspace was shown independent of them; the annihilator of the range is now shown independent too, and the sector
computation is run at I.C's order for the free operator, which is the one I.C Corollary 5.2 (a) uses.

(IV$''''''$7) *A strip in the adjoint chain* (verifier 135's A-m3). The adjoint step (c) (2) was stated on
$\{\tau\ge\frac T4\}$, which misses the strip $\frac{2.25}{10}T\le\tau<\frac T4$ of (B.40)'s a priori set; it is stated
on $\{\tau>\kappa\}$.

*Labels.* The labels map to the source as follows:

| Here | Source |
|---|---|
| Lemma 0.1 | [Hin26a] (B.7)-(B.12) |
| Definition 0.2 | (B.13) |
| Proposition 1.1 | Proposition B.2 |
| Theorem 2.1 | Theorem B.4 |
| Theorem 3.1 | Theorem B.1 with section B.4 |
| Theorem 4.1 | [Hin26] Theorem 7.1 (4), III.E Theorem 1.1 (4) |

*Sources.* [Hin26a] pp. 85-98 (Appendix B: (B.1)-(B.45), Theorem B.1, Proposition B.2 and its proof, Definition B.3,
Theorem B.4 and its proof, section B.4), read at source. Inputs:

- record sections 10.12, 10.14 (iv), 10.21 (K1-K2) and Propositions 10.18 (i), 10.20 (i)-(v) (the record's Proposition
numbers are not its section numbers: Proposition 10.20 is in section 10.23);

- Part IV$''''$ Lemmas 1.2, 1.3, 1.6;

- Part IV$'''''$ Lemmas 0.2, 0.4, 0.5, Propositions 1.3, 4.1, 5.2, 6.1, Theorem 7.3;

- I.A Lemma 7.1; I.C section 4.1, Definition 4.1, Theorem 4.3, Definition 5.1, Corollary 5.2, Proposition 5.3; III.A$'$.

[Mel93] Theorem 6.5 is cited, as the source cites it.
