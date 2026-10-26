# Part III.A. Technical prerequisites at n = 4 ([Hin26] sections 2.1-2.3)

*Status.* Verified. The ninety-third verifier's findings are seated (D226) and the ninety-fourth read and confirmed the
repairs; its one minor finding (Lemma 1.3's regularity count) and two nits are seated (D229) and are to be read. This
part carries [Hin26] sections 2.1-2.3 (pp. 44-63) to spatial dimension $n = 4$: manifolds with corners and blow-ups,
b-analysis and partial polyhomogeneity (Definitions 2.4-2.8, Lemmas 2.10-2.13, 2.15, Remark 2.14), the scattering, 3b-
and scattering-b-transition notions (Example 2.17, Definitions 2.16, 2.18, 2.19, (2.11)-(2.15), Lemma 2.20), extendible
and supported spaces (section 2.1.5), the integration of $x\partial_x$ and $x\partial_x-y\partial_y$ (section 2.2,
Lemmas 2.22-2.23), and the Fourier transform with partial expansions (section 2.3, Lemma 2.24, Proposition 2.25).
Section 2.4 is Part III.A$'$.

*What n = 4 changes.* Sections 2.1.1-2.1.2, 2.1.5 and 2.2 are stated by the source for manifolds with corners of any
dimension and carry over verbatim; their proofs are given here in full, because the source sketches two of them (Lemmas
2.13 and 2.15) and the others are short. Sections 2.1.3-2.1.4 are stated on $\mathbb R^{1+3}$ and are restated on
$\mathbb R^{1+4}$. Section 2.3 is stated for $X = \mathbb R^n_x$ with general $n$, but its inputs (2.25a)-(2.26b) are
[Hin26c] Propositions 13.9 and 13.11, which Part II.G$'$ proves at $n = 4$ (its Propositions 3.3 and 3.5, in
b-densities, so with the source's weights); Proposition 2.25 is proved here from them. Findings (L1)-(L7) are in section
7: two misprints in Proposition 2.25 that would make it false as printed, two harmless ones, a hypothesis of Lemma 2.23
that must be strengthened (L5), a step of Proposition 2.25's proof that gives a larger index set than stated (L6), and
two conventions the source leaves implicit (L7).

## 1. Manifolds with corners, blow-ups, b-analysis

We use, without change, the source's definitions on p. 44-48: manifolds with corners $M$ of any dimension, boundary
hypersurfaces $H$ (embedded, with defining functions $\rho_H$ and collar neighbourhoods $[0,\epsilon)_{\rho_H}\times
H$), local defining functions (Notation 2.1), the radial compactification $\overline{\mathbb R}^d$ (Example 2.2), real
blow-ups of boundary faces and of boundary submanifolds (Example 2.3, (2.1)), b-vector fields $\mathcal V_{\mathrm
b}(M)$, b-differential operators $\mathrm{Diff}^m_{\mathrm b}(M)$ and b-densities (Definition 2.4), the b-normal
operator $N(A)$, the indicial family $N(A,\lambda)$, indicial roots, the boundary spectrum $\mathrm{spec}_{\mathrm
b}(A)$ and simple indicial roots (Definition 2.5), conormal spaces $\mathcal A^{\vec\alpha}(M)$ and weighted b-Sobolev
spaces $H^{k,\vec\alpha}_{\mathrm b}(M)$ (Definition 2.6), index sets with $\min\mathrm{Re}\,E$, $\pi_1$, $k(E,z)$,
sums, the extended unions $E\bar\cup F$ and $E\bar\cup\{(z,k)\}$, and the special index sets $(z,k)$ (Definition 2.7,
(2.2)), and partially polyhomogeneous spaces $H^{k,(\vec E,\vec\alpha)}_{\mathrm b}(M)$, $\mathcal A^{(\vec
E,\vec\alpha)}(M)$ (Definition 2.8, (2.3); Notation 2.9). None of these mentions the dimension except as the generic $n$
of the model $[0,\infty)^k\times\mathbb R^{n-k}$.

Two facts used throughout are immediate from the definitions. (F1) A b-vector field $V$ maps
$H^{k,(\vec E,\vec\alpha)}_{\mathrm b}(M)$ to $H^{k-1,(\vec E,\vec\alpha)}_{\mathrm b}(M)$: in a collar of $H$,
$V = a\rho_H\partial_{\rho_H}+W$ with $W$ tangent to the slices, and
$V(\rho_H^z(\log\rho_H)^\ell u) = \rho_H^z(\log\rho_H)^\ell(az+W)u+\ell a\rho_H^z(\log\rho_H)^{\ell-1}u$ for $u$
independent of $\rho_H$ in the collar (as expansion coefficients are), and $a$ and $W$, which depend on $\rho_H$, are
re-expanded in their Taylor series at $\rho_H = 0$, adding terms at $z+1+\mathbb N_0$ with the same powers of
$\log\rho_H$, which (2.2) allows. (F2) Two memberships of the same function in spaces with the same data at a face $H$
and different data elsewhere combine by a partition of unity subordinate to neighbourhoods of the faces, as in Part
II.G$'$ Proposition 3.3's first paragraph.

A b-vector field $V$ is *b-normal at $H$* if $V-\chi(\rho_H)\rho_H\partial_{\rho_H}\in\rho_H\mathcal V_{\mathrm b}(M)$
for a collar $[0,\epsilon)_{\rho_H}\times H$ and $\chi\in C^\infty_c([0,\epsilon))$ equal to 1 near 0; the source's
local coordinate remark (p. 49) that $\rho_H\partial_{\rho_H}-\rho'_H\partial_{\rho'_H}\in\rho_H\mathcal V_{\mathrm b}$
for two collars makes the notion independent of the collar: if $\rho'_H = a\rho_H$ with $a>0$ smooth and
$(\rho_H,y)\mapsto(\rho'_H,y')$ the change of collar, then $\rho_H\partial_{\rho_H}$ applied to $\rho'_H$ gives
$\rho'_H(1+\rho_H\partial_{\rho_H}\log a)$ and to $y'$ gives $\rho_H\partial_{\rho_H}y'$, which vanishes at $\rho_H = 0$
since $y' = y$ there.

**Lemma 1.1 ([Hin26] Lemma 2.10, normal form).** Let $V$ be b-normal at the compact boundary hypersurface $H$. There are
a defining function $\rho_H$ and an adapted collar $[0,\epsilon)_{\rho_H}\times H$ in which $V =
\rho_H\partial_{\rho_H}$.

*Proof.* In a collar $[0,\epsilon')_x\times H$, $V = x\partial_x+x(a(x,y)x\partial_x+V_\partial(x))$ with $a$ smooth and
$V_\partial(x)$ a smooth family of b-vector fields on $H$; so $x^{-1}V = (1+ax)\partial_x+V_\partial(x)$ is smooth,
tangent to the boundary hypersurfaces $[0,\epsilon')\times\partial_jH$ (as $V_\partial(x)$ is tangent to $\partial H$)
and transversal to $H$. Its flow $\Phi(s,y) := e^{sx^{-1}V}(0,y)$ is defined for small $s\ge0$ (tangency keeps it inside
$M$), and $\Phi$ is a diffeomorphism from $[0,\epsilon'')_s\times H$ onto a neighbourhood of $H$, as $\Phi(0,y) = (0,y)$
and $\partial_s\Phi$ is transversal to $H$ there. In these coordinates $x^{-1}V = \partial_s$, so $V = x\partial_s =
(x/s)\,s\partial_s$, and $x/s = 1+sb(s,y)$ with $b$ smooth, as $x = s+O(s^2)$ ($\partial_sx = 1+ax = 1$ at $s = 0$). Put
$\rho_H := s(1+c(s,y))$ with $c$ smooth and $c(0,y) = 0$; then $s\partial_s = s(1+c+s\partial_sc)\partial_{\rho_H}$ at
fixed $y$, so $V = \frac{(1+sb)(1+c+s\partial_sc)}{1+c}\rho_H\partial_{\rho_H}$, which is $\rho_H\partial_{\rho_H}$ if
and only if $\partial_sc = -\frac{b(1+c)}{1+sb}$, an ordinary differential equation in $s$ with $y$ as a parameter,
solvable with $c(0,y) = 0$ for small $s$. Then $(s,y)\mapsto(\rho_H,y)$ is a diffeomorphism near $s = 0$, giving the
collar. $\square$

**Lemma 1.2 ([Hin26] Lemma 2.12, a Fuchsian ordinary differential equation).** On $[0,1)_x\times H$, $H$ a compact
manifold with corners, with b-Sobolev spaces defined by $x\partial_x$ and $|dx/x|$ in the first factor, let $\chi\in
C^\infty_c([0,\frac34))$ equal 1 on $[0,\frac12]$, $z\in\mathbb C$, $\alpha\ne\mathrm{Re}\,z$. If $(x\partial_x-z)u =
f\in H^{k,(E,\alpha),(\vec F,\vec\beta)}_{\mathrm b}$ and $(1-\chi(x))u\in H^{k,\infty,(\vec F,\vec\beta)}_{\mathrm b}$,
where $(E,\alpha)$ refers to $\{0\}\times H$ and $(\vec F,\vec\beta)$ to $[0,1)$ times the boundary hypersurfaces of
$H$, then $u\in H^{k,(E\bar\cup\{(z,0)\},\alpha),(\vec F,\vec\beta)}_{\mathrm b}$.

*Proof.* $x\partial_x(x^{-z}u) = x^{-z}f$, and multiplication by $x^{-z}$ shifts $(E,\alpha)$ to
$(E-z,\alpha-\mathrm{Re}\,z)$ and commutes with everything else; so let $z = 0$, $\alpha\ne0$. By
$$x\partial_x\big(x^w(\log x)^\ell v(y)\big) = wx^w(\log x)^\ell v(y)+\ell x^w(\log x)^{\ell-1}v(y)\tag{1.1}$$
a term $\chi(x)x^w(\log x)^\ell v$ of $f$ with $w\ne0$ is the image of $\chi(x)w^{-1}x^w(\log x)^\ell v$ up to a term
with one log fewer and a term $w^{-1}x^w(\log x)^\ell v\,x\partial_x\chi$ supported in $x\in[\frac12,\frac34]$;
descending in $\ell$ and ascending in $\mathrm{Re}\,w$ removes all terms of $f$ with $(w,\ell)\in E$, $w\ne0$,
$\mathrm{Re}\,w\le\alpha$, from the equation, the subtracted terms lying in $H^{k,(E,\alpha),(\vec F,\vec\beta)}$. A
term $\chi(x)\sum_{j\le\ell}(\log x)^jv_j$ (the exponent $w = 0$, present only if $0\in\pi_1E$ with
$\mathrm{Re}\,0\le\alpha$) is the image of $\chi(x)\sum_j\frac1{j+1}(\log x)^{j+1}v_j$ up to a term supported in
$[\frac12,\frac34]$; this raises the log power at $0$ by one, which is $E\bar\cup\{(0,0)\}$. It remains to treat $f\in
H^{k,\alpha,(\vec F,\vec\beta)}$ ($E = \emptyset$). Subtracting $\psi(x)u$, $\psi\in C^\infty_c((\frac34,1])$ equal to 1
near 1, which lies in $H^{k,\infty,(\vec F,\vec\beta)}$ by hypothesis, we may assume $u = f = 0$ near $x = 1$. The
operator $x\partial_x$ commutes with $x\partial_x$ and with b-derivatives on $H$, so the case $k = 0$ applied to
derivatives gives every $k$. The solution operators below act in $x$ alone, commute with multiplication by functions of
$y$ and with $\rho^w(\log\rho)^j$ for defining functions $\rho$ of the faces of $H$, and are bounded on $x^\alpha
L^2(|dx/x|;\mathcal H)$ for any Hilbert space $\mathcal H$; applied to the terms and the remainders of Definition 2.8's
expansions at the faces $[0,1)\times\partial_jH$ (inductively on the number of faces), they preserve $(\vec
F,\vec\beta)$. So we drop $y$. If $\alpha<0$: $u(x) = -\int_x^1f(s)\frac{ds}s$, and by Cauchy-Schwarz with
$\int_x^1s^\alpha\frac{ds}s\le|\alpha|^{-1}x^\alpha$ and $\int_0^sx^{-\alpha}\frac{dx}x = |\alpha|^{-1}s^{-\alpha}$,
$$\int_0^1x^{-2\alpha}|u|^2\frac{dx}x\le|\alpha|^{-1}\int_0^1x^{-\alpha}\int_x^1s^{-\alpha}|f(s)|^2\frac{ds}s\frac{dx}x
\le|\alpha|^{-2}\int_0^1s^{-2\alpha}|f(s)|^2\frac{ds}s.$$
If $\alpha>0$: $u(0) := -\int_0^1f\frac{ds}s$ converges absolutely ($|u(0)|^2\le(2\alpha)^{-1}\int
s^{-2\alpha}|f|^2\frac{ds}s$), $u(x)-u(0) = \int_0^xf\frac{ds}s$, and with $\int_0^xs^\alpha\frac{ds}s =
\alpha^{-1}x^\alpha$, $\int_s^1x^{-\alpha}\frac{dx}x\le\alpha^{-1}s^{-\alpha}$,
$$\int_0^1x^{-2\alpha}|u(x)-u(0)|^2\frac{dx}x\le\alpha^{-1}\int_0^1x^{-\alpha}\int_0^xs^{-\alpha}|f|^2\frac{ds}s
\frac{dx}x
\le\alpha^{-2}\int_0^1s^{-2\alpha}|f(s)|^2\frac{ds}s;\tag{1.2}$$
the constant $u(0)$ is the term $(0,0)$ of $E\bar\cup\{(0,0)\}$ (here $E = \emptyset$). $\square$

**Lemma 1.3 ([Hin26] Lemma 2.11, testing for partial polyhomogeneity).** In the notation of Definition 2.8, let $H$ be a
boundary hypersurface with $\alpha_H\notin\mathrm{Re}\,\pi_1E_H$, $V$ b-normal at $H$, $E_{H,\le} := \{(z,\ell)\in
E_H:\mathrm{Re}\,z\le\alpha_H\}$ (a finite set), and $\vec E'$ as in (2.3). If $(1-\chi(\rho_H))u\in H^{k,(\vec
E',\vec\alpha)}_{\mathrm b}(M)$ and
$$\Big(\prod_{(z,\ell)\in E_{H,\le}}(V-z)\Big)u\in H^{k,(\vec E',\vec\alpha)}_{\mathrm b}(M),\tag{1.3}$$
then $u\in H^{k,(\vec E,\vec\alpha)}_{\mathrm b}(M)$. Conversely, $u\in H^{k,(\vec E,\vec\alpha)}_{\mathrm b}$ implies
(1.3) with $k-|E_{H,\le}|$ in place of $k$.

*Proof.* By Lemma 1.1 take a collar with $V = \rho_H\partial_{\rho_H}$ near $H$ (the defining function changes by a
smooth positive factor, which by Definition 2.8's remark does not change the spaces). Conversely: by (1.1) the product
annihilates $\sum_{(z,\ell)\in E_{H,\le}}\rho_H^z(\log\rho_H)^\ell u^{(z,\ell)}$, the factor $V-z$ being taken once for
each $(z,\ell)$, $\ell\le k(E_H,z)$, so $k(E_H,z)+1$ times; derivatives falling on the cut-off are supported away from
$H$; and each factor costs one derivative (F1). Directly: order the factors as $(z_1,\ell_1),\dots,(z_N,\ell_N)$ with
$\mathrm{Re}\,z_1\ge\dots\ge\mathrm{Re}\,z_N$ and put $w_i := \prod_{j>i}(V-z_j)u$, so that $w_0$ is the left side of
(1.3), $w_N = u$ and $(V-z_i)w_i = w_{i-1}$. Apply Lemma 1.2 for $i = 1,\dots,N$, peeling the outermost factor first
(its hypothesis $\alpha_H\ne\mathrm{Re}\,z_i$ is ours): by Definition 2.7 (6) it raises the logarithmic order at $z_i$
by one and completes by (2.2), which adds pairs only at $z_i+m$, $m\ge1$. In this order those points have real part
above that of every later factor, so no later raise meets a completion; the count at each $z\in\pi_1E_{H,\le}$ starts at
$-1$ (the index set of $w_0$ at $H$, that of $\vec E'$, being empty) and is raised $k(E_H,z)+1$ times, to $k(E_H,z)$,
while completions reaching $z$ from $z-m$ carry at most $k(E_H,z-m)\le k(E_H,z)$. So the index set of $u$ at $H$ is
$E_{H,\le}$ completed by (2.2), contained in $E_H$, and the expansion terms with $\mathrm{Re}\,z>\alpha_H$ are absorbed
in the remainder. In another order a raise can meet a completion: for $V(V-1)$ with $V$ peeled first, the completion
$(1,0)$ of $(0,0)$ is then raised to $(1,1)$ (D226; finding (L7)). The a priori hypothesis of Lemma 1.2 holds for each
$w_i$ by (F1), but only at the order $k-(N-i)$, so this gives the index set with $u$ of order $k-N+1$. For the order
$k$: Lemma 1.2's solution operators act in $\rho_H$ alone, commute with derivatives along $H$ and preserve $H^k$, so
their composition applied to the left side of (1.3) gives $u_p$ of order $k$ with the same index set; $u-u_p$ is
annihilated by the product near $H$, so it is $\sum\rho_H^z(\log\rho_H)^\ell c_{z,\ell}$ there (the solutions of the
ordinary differential equation in $\rho_H$), and its coefficients are read off $u-u_p$ on $\{\rho_H\ge\frac34\}$, where
both are of order $k$, by pairing in $\rho_H$ against test functions, so $c_{z,\ell}\in H^k(H)$ (D229, the ninety-fourth
verifier's m1; the source's Lemma 2.11 has the same count). $\square$

### 1.1 Normal operator arguments

Let $\partial M$ be a compact manifold without boundary, $M := [0,\rho_0)_\rho\times\partial M$, with the b-density
$|d\rho/\rho|\otimes\mu$, $\mu$ a smooth positive density on $\partial M$. For $A\in\mathrm{Diff}^m_{\mathrm b}(M)$
elliptic near $\rho = 0$, $N(A,\lambda)$ is an elliptic operator on $\partial M$ depending holomorphically
(polynomially) on $\lambda$; we use two standard facts. (E1) *Large-parameter ellipticity:* for every strip
$\{c_1\le\mathrm{Re}\,\lambda\le c_2\}$ there is $R$ such that $N(A,\lambda)$ is invertible for
$|\mathrm{Im}\,\lambda|\ge R$ in the strip, with $\sum_{j\le m}|\lambda|^{m-j}\|N(A,\lambda)^{-1}g\|_{H^{s+j}(\partial
M)}\le C\|g\|_{H^s(\partial M)}$; this is the elliptic estimate with parameter for the operator family
$\sum_jA_j(0)\lambda^j$, whose joint symbol $\sum_j\sigma(A_j(0))(y,\eta)(i\xi)^j$ is invertible for real
$(\xi,\eta)\ne0$ by the b-ellipticity of $A$ (equivalently, the semiclassical elliptic estimate with $h
= |\mathrm{Im}\,\lambda|^{-1}$). (E2) *Analytic Fredholm theory:* $N(A,\lambda)^{-1}$ is then meromorphic in $\mathbb C$
with finite-rank Laurent coefficients mapping $C^\infty$ to $C^\infty$. Define
$$\mathrm{Spec}_{\mathrm b}(A) := \{(\lambda,k):N(A,\zeta)^{-1}\text{ has a pole of order }\ge k+1\text{ at }\zeta
= \lambda\}$$
(the source writes "of order $k+1$"; the set must contain all smaller $k$ to be an index set in the sense of (2.2), and
the smallest index set containing it, as Lemma 1.5 uses, is the same either way).

The Mellin transform is $\mathcal Mg(\lambda) := \int_0^\infty\rho^{-\lambda}g(\rho)\frac{d\rho}\rho$. In the variable
$s = -\log\rho$ it is the Fourier-Laplace transform $\int e^{\lambda s}g(e^{-s})\,ds$, so Plancherel's theorem gives
(M1): for $g$ supported in $\rho<\rho_0$, $g\in\rho^\gamma L^2(|d\rho/\rho|;\mathcal H)$ if and only if $\mathcal Mg$ is
holomorphic in $\mathrm{Re}\,\lambda<\gamma$ with $\sup_{c<\gamma}\int|\mathcal Mg(c+i\eta)|^2d\eta<\infty$, and then
$2\pi\|\rho^{-\gamma}g\|^2$ equals the integral on $\mathrm{Re}\,\lambda = \gamma$; $\mathcal M(\rho\partial_\rho g) =
\lambda\mathcal Mg$; and $g = \frac1{2\pi i}\int_{\mathrm{Re}\,\lambda = c}\rho^\lambda\mathcal Mg(\lambda)\,d\lambda$
for $c\le\gamma$. So $g\in H^{k,\gamma}_{\mathrm b}(M)$ if and only if $\sum_{j+|\beta|\le k}\int_{\mathrm{Re}\,\lambda
= \gamma}|\lambda|^{2j}\|\mathcal Mg(\lambda)\|^2_{H^{|\beta|}(\partial M)}\,|d\lambda|<\infty$ (with the same bound for
$\mathrm{Re}\,\lambda<\gamma$). (M2) ([Hin26] Remark 2.14) For $\chi\in C^\infty_c([0,1))$ equal to 1 near 0, $\mathcal
M(\chi\rho^z(\log\rho)^ka)(\lambda) = \frac{(-1)^kk!}{(z-\lambda)^{k+1}}a+e(\lambda)a$ with $e$ entire, since
$\int_0^1\rho^{w-\lambda}\frac{d\rho}\rho = (w-\lambda)^{-1}$ for $\mathrm{Re}\,\lambda<\mathrm{Re}\,w$ and $k$
derivatives in $w$ give the first term, while $(\chi-1_{[0,1]})\rho^z(\log\rho)^k$ is supported away from 0 and of
compact support. Hence for $g\in H^{\infty,(F,\beta)}_{\mathrm b}$ supported in $\rho<1$, $\mathcal Mg$ is holomorphic
in $\mathrm{Re}\,\lambda<\min(\beta,\min\mathrm{Re}\,F)$ and meromorphic in $\mathrm{Re}\,\lambda<\beta$ with poles only
at $\lambda\in\pi_1F$, of order at most $k(F,\lambda)+1$, and on vertical lines in $\mathrm{Re}\,\lambda<\beta$ away
from the poles $|\lambda|^N\|\mathcal Mg(\lambda)\|_{H^N(\partial M)}$ is square-integrable for every $N$, uniformly on
compact sets of real parts.

**Lemma 1.4 ([Hin26] Lemma 2.13, boundary spectrum and polyhomogeneity).** Let $\chi\in C^\infty_c([0,\frac12\rho_0))$
equal 1 on $[0,\frac14\rho_0]$ and $\tilde\chi\in C^\infty_c([0,\rho_0))$ equal 1 on $[0,\frac12\rho_0]$. Suppose
$\tilde\chi u\in H^{\infty,\alpha}_{\mathrm b}(M)$ and $\chi Au\in H^{\infty,(F,\beta)}_{\mathrm b}(M)$ with
$\beta\ne\mathrm{Re}\,\lambda$ for all $\lambda\in\mathrm{spec}_{\mathrm b}(A)$. Let $E(\alpha)$ be the smallest index
set containing the $(\lambda,k)\in\mathrm{Spec}_{\mathrm b}(A)$ with $\mathrm{Re}\,\lambda>\alpha$, $E_0 :=
E(\alpha)\bar\cup F$, $E_{k+1} := E(\alpha)\bar\cup(F\bar\cup(E_k+1))$, $E := \bigcup_kE_k$. Then $\tilde\chi u\in
H^{\infty,(E,\beta)}_{\mathrm b}(M)$.

*Proof.* If $\beta\le\alpha$ there is nothing to prove
($H^{\infty,\alpha}_{\mathrm b}\subset H^{\infty,(E,\beta)}_{\mathrm b}$), so let $\beta>\alpha$. If some exponent of
$F$ has real part $\beta$, remove those finitely many terms $\chi\rho^z(\log\rho)^jf_{z,j}$ of $\chi Au$ first:
$N(A,\cdot)^{-1}$ is holomorphic on $\mathrm{Re}\,\lambda = \beta$, so the circle integral (1.4) of Lemma 1.5 (whose
proof does not use the present lemma) gives $u_{z,j} = \rho^z\sum_{i\le j}(\log\rho)^iu_i$,
$u_i\in C^\infty(\partial M)$, with $N(A)u_{z,j} = \rho^z(\log\rho)^jf_{z,j}$; then $A(\chi u_{z,j})$ is that term up to
$(A-N(A))(\chi u_{z,j})$, whose exponents lie in $z+1+\mathbb N_0$, above $\beta$, and up to terms supported in
$\rho\ge\frac14\rho_0$. Replacing $u$ by $u-\sum\chi u_{z,j}$ keeps the hypotheses ($\mathrm{Re}\,z = \beta>\alpha$) and
the conclusion ($(z,j)\in F\subset E$) and removes these terms, so we may assume $\beta\notin\mathrm{Re}\,\pi_1F$ (D226;
the source leaves this case implicit, finding (L7)). Write $v := \tilde\chi u$ and
$N(A) = \sum_jA_j(0)(\rho\partial_\rho)^j$ in the collar. Then $N(A)v = f'$ with
$f' := \chi Au+(\tilde\chi-\chi)Au+[A,\tilde\chi]u-(A-N(A))v$; the second and third terms are supported in
$\rho\ge\frac14\rho_0$ (where $\tilde\chi u$ is all of the information: there $u$ is of class $H^\infty_{\mathrm{loc}}$
by ellipticity, so these terms are smooth with compact support in $(0,\rho_0)$ and have entire Mellin transforms
decaying on vertical lines), and $A-N(A)\in\rho\,\mathrm{Diff}^m_{\mathrm b}$ near $\rho = 0$, so
$f'\in H^{\infty,(F,\beta)}_{\mathrm b}+H^{\infty,\alpha+1}_{\mathrm b}$ after cutting off. Let
$\gamma := \min(\beta,\alpha+1)$, decreased slightly if necessary so that no $\mathrm{Re}\,\lambda$,
$\lambda\in\mathrm{spec}_{\mathrm b}(A)\cup\pi_1F$, equals $\gamma$ (possible as these are discrete in every strip;
$\beta$ itself is excluded, by the hypothesis and the reduction above, when $\gamma = \beta$). By (M1), $\mathcal Mv$ is
holomorphic in $\mathrm{Re}\,\lambda<\alpha$ and $N(A,\lambda)\mathcal Mv = \mathcal Mf'$ there; by (M2) and (E2),
$N(A,\lambda)^{-1}\mathcal Mf'$ is meromorphic in $\mathrm{Re}\,\lambda<\gamma$ and continues $\mathcal Mv$. Its poles
with $\mathrm{Re}\,\lambda<\alpha$ cancel (as $\mathcal Mv$ is holomorphic there), and there are none on
$\mathrm{Re}\,\lambda = \alpha$: a pole $\lambda_0$ there would make $\int|\mathcal Mv(c+i\eta)|^2d\eta$ grow at least
like $(\alpha-c)^{-1}$ as $c\uparrow\alpha$, against the uniform bound of (M1); at $\lambda$ with
$\alpha<\mathrm{Re}\,\lambda<\gamma$ the pole order is at most the order of $N(A,\cdot)^{-1}$ plus that of
$\mathcal Mf'$. Now $v = \frac1{2\pi i}\int_{\mathrm{Re}\,\lambda = c}\rho^\lambda\mathcal Mv\,d\lambda$ for $c<\alpha$,
and we move the contour to $\mathrm{Re}\,\lambda = \gamma$. This is justified by (E1) and (M2): on the horizontal
segments $\{c\le\mathrm{Re}\,\lambda\le\gamma,\ \mathrm{Im}\,\lambda = \pm T\}$, along a sequence $T\to\infty$,
$\int_c^\gamma\|N(A,s\pm iT)^{-1}\mathcal Mf'(s\pm iT)\|^2_{H^N}ds\to0$ for every $N$ (by Fubini, the
square-integrability in $\mathrm{Im}\,\lambda$ of $|\lambda|^{N'}\|\mathcal Mf'\|_{H^{N'}}$, uniform in the strip, makes
$T\mapsto\int_c^\gamma\|\mathcal Mf'(s\pm iT)\|^2_{H^{N'}}ds$ integrable, hence small along a sequence, which a diagonal
choice makes one for all $N$; (E1) bounds $N(A,\cdot)^{-1}$ there). This is a statement in $L^2$ on the segments, not a
pointwise one, and it is what the contour shift uses. The residues at the finitely many poles in
$\alpha<\mathrm{Re}\,\lambda<\gamma$ are of the form $\rho^\lambda\sum_{j\le p}(\log\rho)^ja_j$,
$a_j\in C^\infty(\partial M)$, with $p+1$ the pole order: by the order count these lie in
$H^{\infty,(E(\alpha)\bar\cup F,\gamma')}$ for every $\gamma'<\gamma$ (the extended union $\bar\cup$ of (5) of
Definition 2.7 is precisely the addition of pole orders, $(z,k+l+1)$ from orders $k+1$ and $l+1$). The integral on
$\mathrm{Re}\,\lambda = \gamma$ lies in $H^{\infty,\gamma}_{\mathrm b}$ by (M1), using (E1) for all $|\lambda|$-weighted
norms. So $v\in H^{\infty,(E_0,\gamma)}$ near $\rho = 0$. If $\gamma = \beta$ we are done. Otherwise $\gamma<\beta$ (and
$\gamma\le\alpha+1$); repeat with $\alpha$ replaced by $\gamma-\delta'$ for small $\delta'>0$ and the expansion found so
far moved into the right side: $(A-N(A))$ applied to $\rho^\lambda(\log\rho)^ja$ is, by Taylor expansion of the
coefficients $A_j(\rho)$ at $\rho = 0$, an expansion with exponents in $\lambda+1+\mathbb N_0$ and the same log powers,
which is $E_0+1$; so $f'\in H^{\infty,(F\bar\cup(E_0+1),\beta)}+H^{\infty,\gamma+1-\delta'}$, and the same argument
gives $E_1$ up to the weight $\min(\beta,\gamma+1-\delta')$. Each step raises the weight by almost 1 until $\beta$ is
reached; finitely many steps suffice, the index sets being contained in $E$. (The poles of $N(A,\cdot)^{-1}$ that enter
at a later step are those with real part above the previous weight, all in $E(\alpha)$.) $\square$

**Lemma 1.5 ([Hin26] Lemma 2.15, formal solutions).** Let $A\in\mathrm{Diff}^m_{\mathrm b}(M)$ be elliptic, $F$ an index
set, $\beta\in\mathbb R$, $\mathrm{ord}(z)$ the order of the pole of $N(A,\cdot)^{-1}$ at $z$ (0 if none), and $E :=
\{(\lambda+j,k+m'):(\lambda,k)\in F,\ j\in\mathbb N_0,\ m'\le\sum_{q=0}^j\mathrm{ord}(\lambda+q)\}$. There is a
continuous linear map $S = S_{A,F,\beta}:\mathcal A^F(M)\to\mathcal A^E(M)$, also bounded $H^{k,(F,\beta)}_{\mathrm
b}\to H^{k+m,(E,\beta)}_{\mathrm b}$ for every $k$, such that $f-ASf\in\mathcal A^G(M)$, $G := \{(\lambda,k)\in
E:\mathrm{Re}\,\lambda\ge\beta\}$, resp. $f-ASf\in H^{k,\beta}_{\mathrm b}$. If $A$ depends smoothly on $b\in\mathbb
R^N$ with $b$-independent $N(A)$, $S$ can be chosen smooth in $b$; for $\beta = \infty$ the statement on $\mathcal
A$-spaces holds with $S$ continuous but non-linear.

*Proof.* Consider one term $\chi(\rho)\rho^\lambda(\log\rho)^\ell f_0$ of $f$, $f_0\in H^k(\partial M)$, with
$\mathrm{Re}\,\lambda$ minimal and $\ell = k(F,\lambda)$. By Cauchy's formula $\rho^\lambda(\log\rho)^\ell =
\frac{\ell!}{2\pi i}\oint_\lambda\rho^\zeta(\zeta-\lambda)^{-\ell-1}d\zeta$ over a small circle around $\lambda$
enclosing no other pole of $N(A,\cdot)^{-1}$ (the source prints $\frac1{2\pi i\,\ell!}$; finding (L4)); put
$$u := \frac{\ell!}{2\pi i}\oint_\lambda\rho^\zeta(\zeta-\lambda)^{-\ell-1}N(A,\zeta)^{-1}f_0\,d\zeta.\tag{1.4}$$
As $N(A)(\rho^\zeta g) = \rho^\zeta N(A,\zeta)g$, $N(A)u = \rho^\lambda(\log\rho)^\ell f_0$ exactly. By the residue
theorem $u = \rho^\lambda\sum_{j\le\ell+p}(\log\rho)^ju_j$, $u_j\in H^{k+m}(\partial M)$ (the Laurent coefficients of
$N(A,\cdot)^{-1}$ gain $m$ derivatives), $p = \mathrm{ord}(\lambda)$. Then $\chi u\in H^{k+m,(\lambda,\ell+p)}$ and
$f-A(\chi u)$ has the term removed, up to $(A-N(A))(\chi u)$, an expansion with exponents in $\lambda+1+\mathbb N_0$ and
log powers $\le\ell+p$ (Taylor expansion of the coefficients; this term depends smoothly on $b$ when $A$ does), and up
to commutator terms supported away from $\rho = 0$, which are $\mathcal A^\infty$ near $\partial M$. Iterating over the
finitely many terms with $\mathrm{Re}\,\lambda\le\beta$ (new terms with exponents $\lambda+j$ and log powers raised by
the pole orders met, which is the definition of $E$) gives $u$ with $f-Au\in H^{k,\beta}_{\mathrm b}$ resp.
$\mathcal A^G$; for $\beta = \infty$, take an asymptotic (Borel) sum of the infinitely many terms, which is continuous
but not linear. Each step is a fixed linear operation, the circle integral (1.4) involving no choice (adding an indicial
solution $\rho^\lambda u_0\in\ker N(A)$ would be a choice); hence $S$ is linear, continuous, and smooth in $b$.
$\square$

## 2. Scattering and 3b-notions at n = 4

**Definition 2.1 ([Hin26] Definition 2.16, Example 2.17).** For $d\in\mathbb N$, ${}^{\mathrm{sc}}T^*\mathbb R^d :=
\overline{\mathbb R}^d\times\mathbb R^d$ with $(z,\zeta)$ the covector $\zeta_\mu dz^\mu$, and $\mathcal
V_{\mathrm{sc}}(\overline{\mathbb R}^d)$ the $C^\infty(\overline{\mathbb R}^d)$-span of
$\partial_{z^0},\dots,\partial_{z^{d-1}}$. In $\{z^0>0\}$, with $\rho_\infty := 1/z^0$ and $\hat z^j := z^j/z^0$,
$$\partial_{z^0} = -\rho_\infty\Big(\rho_\infty\partial_{\rho_\infty}+\sum_{j=1}^{d-1}\hat z^j\partial_{\hat z^j}\Big),
\qquad\partial_{z^j} = \rho_\infty\partial_{\hat z^j},$$
since $\partial_{z^0}\rho_\infty = -\rho_\infty^2$ and $\partial_{z^0}\hat z^j = -\rho_\infty\hat z^j$; so $\mathcal
V_{\mathrm{sc}}(\overline{\mathbb R}^d) = \rho_d\mathcal V_{\mathrm b}(\overline{\mathbb R}^d)$ for a boundary defining
function $\rho_d$. At $n = 4$ the Minkowski metric $\bar g = -dt^2+\sum_{j=1}^4(dx^j)^2$ is an element of
$C^\infty(\overline{\mathbb R}^5;S^2\,{}^{\mathrm{sc}}T^*\mathbb R^5)$.

**Definition 2.2 ([Hin26] (2.10) and Definition 2.18 at n = 4).** Write $\overline{\mathbb R}^5 = \overline{\mathbb
R^{1+4}_{t_*,x}}$, let $k_\pm\in\partial\overline{\mathbb R}^5$ be the limits of $(t_*,0)$ as $t_*\to\pm\infty$, and
$\tilde M_0 := [\overline{\mathbb R}^5;k_+,k_-]$, with boundary hypersurfaces $\mathrm{sf}$ (lift of
$\partial\overline{\mathbb R}^5$) and $K_\pm$ (lifts of $k_\pm$); $\rho_{\mathrm{sf}} := \langle x\rangle^{-1}$ and
$\rho_K := \langle x\rangle(1+t_*^2+|x|^2)^{-1/2}$ are defining functions. $\mathcal V_{3\mathrm{sc}}(\tilde M_0)$ is
the $C^\infty(\tilde M_0)$-span of $\partial_{t_*},\partial_{x^1},\dots,\partial_{x^4}$. (1) ${}^{3\mathrm b}T^*\tilde
M_0 := \tilde M_0\times\mathbb R^5$, $(t_*,x;\tau,\xi)$ being $\tau\frac{dt_*}{\langle
x\rangle}+\sum_{j=1}^4\xi_j\frac{dx^j}{\langle x\rangle}$; dually $(v,w)\mapsto v\langle
x\rangle\partial_{t_*}+\sum_{j=1}^4w^j\langle x\rangle\partial_{x^j}$. (2) $\mathcal V_{3\mathrm b}(\tilde M_0)$ is the
$C^\infty(\tilde M_0)$-span of $\langle x\rangle\partial_{t_*}$, $\langle x\rangle\partial_{x^j}$, $j = 1,\dots,4$,
equivalently $\rho_{\mathrm{sf}}^{-1}\mathcal V_{3\mathrm{sc}}(\tilde M_0)$. (3) $\mathrm{Diff}^m_{3\mathrm b}(\tilde
M_0)$ and $\mathrm{Diff}^{m,(\alpha_{\mathrm{sf}},\alpha_K)}_{3\mathrm b} :=
\rho_{\mathrm{sf}}^{-\alpha_{\mathrm{sf}}}\rho_K^{-\alpha_K}\mathrm{Diff}^m_{3\mathrm b}$, and
$H^{s,(\alpha_{\mathrm{sf}},\alpha_K)}_{3\mathrm b} =
\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}\rho_K^{\alpha_K}H^s_{3\mathrm b}$ (with variable orders as in Part II, which
carries [Hin26c] section 3 at $n = 4$).

A $t_*$-translation-invariant $A\in\mathrm{Diff}^{m,(\alpha_{\mathrm{sf}},0)}_{3\mathrm b}(\tilde M_0)$ has the form
$$A
= \sum_{j+|\alpha|\le m}\langle x\rangle^{\alpha_{\mathrm{sf}}}a_{j\alpha}(x)(\langle x\rangle\partial_{t_*})^j(
\langle x\rangle\partial_x)^\alpha,
\qquad a_{j\alpha}\in C^\infty(\overline{\mathbb R}^4),\tag{2.1}$$
$\alpha\in\mathbb N_0^4$, and its spectral family, with $(\mathcal Fu)(\sigma,x) := \int e^{i\sigma t_*}u(t_*,x)\,dt_*$,
is
$$\hat A(\sigma)
= \sum_{j+|\alpha|\le m}\langle x\rangle^{\alpha_{\mathrm{sf}}}a_{j\alpha}(x)(-i\sigma\langle x\rangle)^j(\langle x
\rangle\partial_x)^\alpha.\tag{2.2}$$
(The wave operator of a stationary metric of Part III.B is of this form with $m = 2$, $\alpha_{\mathrm{sf}} = -2$:
$\langle x\rangle^{-2}$ times a combination of $(\langle x\rangle\partial)^2$, as in II.C.)

**Definition 2.3 ([Hin26] Definition 2.19 at n = 4).** $\tilde X := \mathbb R^4$, $\tilde X_{\mathrm{sc}\text-\mathrm b}
:= [[0,1]_\varsigma\times\overline{\tilde X};\{0\}\times\partial\overline{\tilde X}]$ with faces scf, tf, zf as in the
source and, with $\rho := \langle x\rangle^{-1}$, the defining functions $\rho_{\mathrm{scf}} =
\frac\rho{\varsigma+\rho}$, $\rho_{\mathrm{tf}} = \varsigma+\rho$, $\rho_{\mathrm{zf}} =
\frac\varsigma{\varsigma+\rho}$. $\mathcal V_{\mathrm{sc}\text-\mathrm b}(\tilde X)$ is the $C^\infty(\tilde
X_{\mathrm{sc}\text-\mathrm b})$-span of $\rho_{\mathrm{scf}}\langle x\rangle\partial_{x^j}$, $j = 1,\dots,4$;
$\mathrm{Diff}^{m,(\alpha_{\mathrm{scf}},\alpha_{\mathrm{tf}},\alpha_{\mathrm{zf}})}_{\mathrm{sc}\text-\mathrm b} :=
\rho_{\mathrm{scf}}^{-\alpha_{\mathrm{scf}}}\rho_{\mathrm{tf}}^{-\alpha_{\mathrm{tf}}}\rho_{\mathrm{zf}}^{-\alpha_{
\mathrm{zf}}}\mathrm{Diff}^m_{\mathrm{sc}\text-\mathrm
b}$; and $\|u\|_{H^{m,(\alpha_{\mathrm{scf}},\alpha_{\mathrm{tf}},\alpha_{\mathrm{zf}})}_{\mathrm{sc}\text-\mathrm
b,\varsigma}} := \sum_{|\alpha|\le
m}\|\rho_{\mathrm{scf}}^{-\alpha_{\mathrm{scf}}}\rho_{\mathrm{tf}}^{-\alpha_{\mathrm{tf}}}\rho_{\mathrm{zf}}^{-
\alpha_{\mathrm{zf}}}(\rho_{\mathrm{scf}}\langle
x\rangle\partial_x)^\alpha u\|_{L^2(\tilde X,\mu)}$ for a fixed weighted b-density $\mu$ (below $\mu = |dx|$), with the
$b$-regularity variant $H^{(m;k)}$ as in the source. As $\varsigma\langle x\rangle =
\rho_{\mathrm{zf}}/\rho_{\mathrm{scf}}$ and $\langle x\rangle\partial_{x^j}\in\rho_{\mathrm{scf}}^{-1}\mathcal
V_{\mathrm{sc}\text-\mathrm b}$, (2.2) gives, for fixed $\hat\sigma$, $|\hat\sigma| = 1$, $\{\hat
A(\hat\sigma\varsigma)\}_{\varsigma\in[0,1]}\in\mathrm{Diff}^{m,(\alpha_{\mathrm{sf}}+m,\alpha_{\mathrm{sf}},0)}_{
\mathrm{sc}\text-\mathrm
b}(\tilde X)$, as at $n = 3$.

**Lemma 2.4 ([Hin26] Lemma 2.20 at n = 4).** For $u\in H^{m,(\alpha_{\mathrm{sf}},0)}_{3\mathrm b}(\tilde
M_0,|dt_*dx|)$,
$$\int_{-1}^1\|\hat u(\sigma)\|^2_{H^{m,(m+\alpha_{\mathrm{sf}},\alpha_{\mathrm{sf}},0)}_{\mathrm{sc}\text-\mathrm b,|
\sigma|}(\tilde X,|dx|)}\,
d\sigma\le
C\|u\|^2_{H^{m,(\alpha_{\mathrm{sf}},0)}_{3\mathrm b}(\tilde M_0,|dt_*dx|)},\tag{2.3}$$
and the reverse inequality holds if $\mathrm{supp}\,\hat u\subset[-1,1]$.

*Proof.* The norm on the right is equivalent to $\sum_{j+|\beta|\le m}\|\langle x\rangle^{\alpha_{\mathrm{sf}}}(\langle
x\rangle\partial_{t_*})^j(\langle x\rangle\partial_x)^\beta u\|_{L^2(|dt_*dx|)}$, the weight commuting with the fields
up to lower-order terms with bounded coefficients ($\langle x\rangle\partial_x\langle x\rangle^c = c\langle
x\rangle^c\frac x{\langle x\rangle}$), and the weight $\rho_K^0$ being trivial. By Plancherel in $t_*$ this is
$\sum_{j+|\beta|\le m}\int\|\langle x\rangle^{\alpha_{\mathrm{sf}}}(\sigma\langle x\rangle)^j(\langle
x\rangle\partial_x)^\beta\hat u(\sigma)\|^2_{L^2(dx)}\frac{d\sigma}{2\pi}$, up to constants. For $|\sigma|\le1$:
$\rho_{\mathrm{scf}}^{-\alpha_{\mathrm{sf}}}\rho_{\mathrm{tf}}^{-\alpha_{\mathrm{sf}}} = \rho^{-\alpha_{\mathrm{sf}}} =
\langle x\rangle^{\alpha_{\mathrm{sf}}}$, $\rho_{\mathrm{scf}}^{-1} = 1+|\sigma|\langle x\rangle$, and
$\rho_{\mathrm{scf}}^{-m}(\rho_{\mathrm{scf}}\langle x\rangle\partial_x)^\beta =
\rho_{\mathrm{scf}}^{-(m-|\beta|)}(\langle x\rangle\partial_x)^\beta$ modulo terms of the same form with fewer
derivatives and bounded coefficients ($\langle x\rangle\partial_x\log\rho_{\mathrm{scf}}$ is bounded); and
$(1+|\sigma|\langle x\rangle)^{m-|\beta|}$ is comparable to $\sum_{j\le m-|\beta|}|\sigma\langle x\rangle|^j$. So the
integrand of (2.3) is comparable to $\sum_{j+|\beta|\le m}\|\langle x\rangle^{\alpha_{\mathrm{sf}}}(\sigma\langle
x\rangle)^j(\langle x\rangle\partial_x)^\beta\hat u(\sigma)\|^2$ at each $|\sigma|\le1$, which gives both inequalities.
$\square$

*Normal operator at sf ([Hin26] (2.14)-(2.15) at n = 4).* For $A$ as in (2.1), with $a^\infty_{j\alpha}(\omega) :=
a_{j\alpha}|_{\partial\overline{\mathbb R}^4}$, $\omega = x/|x|\in\mathbb S^3$,
$$N_{\mathrm{sf}}(A) :
= r^{\alpha_{\mathrm{sf}}}\sum_{j+|\alpha|\le m}a^\infty_{j\alpha}(\omega)(r\partial_{t_*})^j(r\partial_x)^\alpha
\tag{2.4}$$
is homogeneous of degree $\alpha_{\mathrm{sf}}$ under $(t_*,x)\mapsto(\lambda t_*,\lambda x)$, and
$A-N_{\mathrm{sf}}(A)\in\mathrm{Diff}^{m,(\alpha_{\mathrm{sf}}-1,0)}_{3\mathrm b}$ on $\{r\ge1\}$, as
$a_{j\alpha}-a^\infty_{j\alpha}$ and $\langle x\rangle-r$ are $O(r^{-1})$ with all b-derivatives. In $\rho = r^{-1}$,
$\omega$, $v := \rho t_*$ (so $\mathrm{sf}^\circ = \mathbb R_v\times\mathbb S^3$),
$N_{\mathrm{sf}}(r^{-\alpha_{\mathrm{sf}}}A) = \sum
a_{jk\gamma}(\omega)\partial_v^j(\rho\partial_\rho+v\partial_v)^k\partial_\omega^\gamma$, since $\rho^{-1}\partial_{t_*}
= \partial_v$ and $\rho\partial_\rho|_{t_*} = \rho\partial_\rho|_v+v\partial_v$; and the Mellin transform in $\rho$
gives
$$N_{\mathrm{sf}}(r^{-\alpha_{\mathrm{sf}}}A,\rho^\lambda) :
= \sum_{j+k+|\gamma|\le m}a_{jk\gamma}(\omega)\partial_v^j(\lambda+v\partial_v)^k\partial_\omega^\gamma\in
\mathrm{Diff}^m_{\mathrm b}(\mathrm{sf}).\tag{2.5}$$
The only change from $n = 3$ is $\mathbb S^3$ in place of $\mathbb S^2$.

*Extendible and supported spaces ([Hin26] section 2.1.5, Notation 2.21).* We use the source's definitions unchanged
(they concern a compact submanifold with corners $\Omega$ of a compact manifold with corners and are dimension-free):
$\bar H^s_{\mathrm b}(\Omega)$ by restriction with the quotient norm, $\dot H^s_{\mathrm b}(\Omega)$ by support,
$H^s_{\mathrm b}(\Omega)^{\bullet,-}$ mixed through the $\delta$-enlargement $\Omega_\delta$, the same with weights and
partial expansions, and $H^s_{\mathrm b} := \bar H^s_{\mathrm b}$ when every face is extendible.

## 3. Integration along x d_x and x d_x - y d_y ([Hin26] section 2.2)

On $[0,2)_x\times[0,2)_y\times(-2,2)^d_q$ with the density $|\frac{dx}x\frac{dy}y\,dq|$, write
$H^{k,(E,\alpha),(F,\beta)}_{\mathrm b}$ for the b-Sobolev space with partial expansions at $x = 0$ and $y = 0$, and fix
$\chi\in C^\infty_c([0,\frac34))$ equal to 1 on $[0,\frac12]$ ((2.16)).

**Lemma 3.1 ([Hin26] Lemma 2.22).** Let $\mathrm{Re}\,z<\min(\alpha,\min\mathrm{Re}\,E)$ and $f\in
H^{k,(E,\alpha),(F,\beta)}_{\mathrm b}$. Then $(x\partial_x-z)u = f$ has a unique solution $u\in
H^{k,(E,\alpha),(F,\beta)}_{\mathrm b}$.

*Proof.* Multiplication by $x^{-z}$ reduces to $z = 0$, $\alpha>0$, $\min\mathrm{Re}\,E>0$. The terms $\chi(x)x^w(\log
x)^\ell v$ of $f$ with $\mathrm{Re}\,w\le\alpha$ have $w\ne0$ and are removed by (1.1) as in Lemma 1.2, by terms in
$H^{k,(E,\alpha),(F,\beta)}$. For $f\in H^{k,\alpha,(F,\beta)}$, $u(x) := \int_0^xf(s)\frac{ds}s$ solves the equation,
and (1.2) with $u$ in place of $u-u(0)$ shows $u\in H^{k,\alpha,(F,\beta)}$ ($y$, $q$ being parameters and the expansion
at $y = 0$ preserved as in Lemma 1.2). Uniqueness: a solution of $x\partial_xu = 0$ is a function $c(y,q)$ of the other
variables, which lies in $H^{k,(E,\alpha)}$ at $x = 0$ only if $c = 0$, as $\alpha>0$ and $(0,0)\notin E$. $\square$

**Lemma 3.2 ([Hin26] Lemma 2.23, with (L5) repaired).** Let $z\in\mathbb C$, $\alpha+\mathrm{Re}\,z>\beta$, and
$\mathrm{Re}(w+z)\ne\beta$ for all $(w,0)\in E$. If
$(x\partial_x-y\partial_y+z)u = f\in H^{k,(E,\alpha),(F,\beta)}_{\mathrm b}$ and
$(1-\chi(y))u\in H^{k,(E,\alpha),\infty}_{\mathrm b}$, then $u\in H^{k,(E,\alpha),((E+z)\bar\cup F,\beta)}_{\mathrm b}$.

*Proof.* $(x\partial_x-y\partial_y)(x^zu) = x^zf$; replacing $(u,f,E,\alpha)$ by $(x^zu,x^zf,E+z,\alpha+\mathrm{Re}\,z)$
reduces to $z = 0$ with $\alpha>\beta$, which is where $\alpha+\mathrm{Re}\,z>\beta$ is used (the source assumes
$\alpha>\beta$; finding (L5)).

*Step 1, at $x = 0$.* Let $(w,\ell)$, $\ell = k(E,w)$, with $\mathrm{Re}\,w = \min\mathrm{Re}\,E\le\alpha$, and
$x^w(\log x)^\ell v(y,q)$, $v\in H^{k,(F,\beta)}_{\mathrm b}([0,2)\times(-2,2)^d)$, the corresponding term of $f$. By
$$(x\partial_x-y\partial_y)\big(x^w(\log x)^\ell a(y,q)\big)
= x^w(\log x)^\ell(w-y\partial_y)a+\ell x^w(\log x)^{\ell-1}a,\tag{3.1}$$
the coefficient $a$ of $x^w(\log x)^\ell$ in $u$ on $\{y\ge\frac34\}$ (which exists by the a priori hypothesis) solves
$(w-y\partial_y)a = v$ there. Extend $a$ to $(0,2)$ by solving this equation; $(y\partial_y-w)a = -v$, and Lemma 1.2 in
the variable $y$, whose hypothesis $\beta\ne\mathrm{Re}\,w$ is ours, gives $a\in
H^{k,(F\bar\cup\{(w,0)\},\beta)}_{\mathrm b}$. Then $\tilde u := u-\chi(x)x^w(\log x)^\ell a$ satisfies the hypotheses
with $E$ replaced by $E\setminus\{(w,\ell)\}$ at $x = 0$ and $F$ by $F\bar\cup\{(w,0)\}$ at $y = 0$ (the cut-off
contributes terms supported in $x\in[\frac12,\frac34]$, where $u$'s and $f$'s spaces have no condition at $x = 0$).
Repeating over the finitely many $(w,\ell)\in E$ with $\mathrm{Re}\,w\le\alpha$ produces $u_0\in H^{k,E,(F\bar\cup
E,\beta)}_{\mathrm b}$ near $x = 0$ with
$$\tilde u := u-u_0:\quad(x\partial_x-y\partial_y)\tilde u =: \tilde f\in H^{k,\alpha,(E\bar\cup F,\beta)}_{\mathrm b},
\quad
(1-\chi(y))\tilde u\in H^{k,\alpha,\infty}_{\mathrm b}.\tag{3.2}$$

*Step 2, at $y = 0$.* For $(w,\ell)$, $\ell = k(E\bar\cup F,w)$, $\mathrm{Re}\,w\le\beta<\alpha$, let $y^w(\log y)^\ell
v(x,q)$, $v\in H^{k,\alpha}_{\mathrm b}$, be the term of $\tilde f$. As $(x\partial_x-y\partial_y)(y^w(\log y)^\ell
a(x,q)) = y^w(\log y)^\ell(x\partial_x-w)a-\ell y^w(\log y)^{\ell-1}a$, Lemma 3.1 ($\mathrm{Re}\,w<\alpha$, empty index
set at $x = 0$) gives $a\in H^{k,\alpha}_{\mathrm b}$ with $(x\partial_x-w)a = v$; subtract $\chi(y)y^w(\log y)^\ell a$,
descend in $\ell$ and ascend in $\mathrm{Re}\,w$. This produces $\tilde u_0\in H^{k,\alpha,(E\bar\cup F,\beta)}_{\mathrm
b}$ with $(1-\chi(y))\tilde u_0 = 0$ near $y\ge\frac34$ and $u^\flat := \tilde u-\tilde u_0$ satisfying
$$(x\partial_x-y\partial_y)u^\flat =: f^\flat\in H^{k,\alpha,\beta}_{\mathrm b},
\qquad(1-\chi(y))u^\flat\in H^{k,\alpha,\infty}_{\mathrm b}.\tag{3.3}$$

*Step 3, the remainder.* It suffices to show $u^\flat\in H^{k,\alpha,\beta}_{\mathrm b}$, and for $k = 0$:
$x\partial_x$, $y\partial_y$, $\partial_q$ commute with $x\partial_x-y\partial_y$. With $\psi\in C^\infty_c([0,1))$
equal to 1 on $[0,\frac34]$, $(x\partial_x-y\partial_y)(\psi(y)u^\flat) = \psi f^\flat+y\psi'(y)(1-\chi(y))u^\flat$
still lies in $H^{0,\alpha,\beta}$ and $\psi u^\flat$ vanishes near $y = 1$; and $(1-\psi)u^\flat\in
H^{0,\alpha,\infty}$. Multiplication by $(xy)^{-\alpha}$ commutes with $x\partial_x-y\partial_y$, so let $\alpha =
0>\beta$. Drop $q$. The solution vanishing near $y = 1$ is, by integration along the characteristics $xy = $ const,
$$u^\flat(x,y) = \int_y^1f^\flat\big(\tfrac{xy}s,s\big)\frac{ds}s$$
(indeed $x\partial_x$ and $y\partial_y$ of the integral agree except for the boundary term $-f^\flat(x,y)$ from
$y\partial_y$). By Cauchy-Schwarz with $\int_y^1s^\beta\frac{ds}s\le|\beta|^{-1}y^\beta$, then $t := xy/s$ at fixed
$(x,s)$ (so $y\in(0,s)$ becomes $t\in(0,x)$, $\frac{dy}y = \frac{dt}t$), and
$\int_t^2x^\beta\frac{dx}x\le|\beta|^{-1}t^\beta$:
$$\iint y^{-2\beta}|u^\flat|^2\frac{dx}x\frac{dy}y\le|\beta|^{-1}\iint s^{-\beta}\int_0^sy^{-\beta}\Big|f^\flat\big(
\tfrac{xy}s,
s\big)\Big|^2
\frac{dy}y\frac{ds}s\frac{dx}x$$
$$= |\beta|^{-1}\iint s^{-2\beta}\int_0^xt^{-\beta}x^\beta|f^\flat(t,s)|^2\frac{dt}t\frac{ds}s\frac{dx}x
\le|\beta|^{-2}\iint s^{-2\beta}|f^\flat(t,s)|^2\frac{dt}t\frac{ds}s,$$
with $x$ ranging over $(0,2)$ (the source writes $(0,1)$; nothing changes). $\square$

**Lemma 3.3 (a product of such operators; D226).** Let $z_1,\dots,z_N\in\mathbb C$, repetitions allowed, and let $Z$ be
the smallest index set with $k(Z,z)\ge\#\{j:z_j = z\}-1$ for every $z$. Let $E$ be an index set without logarithms
($k(E,w) = 0$ for $w\in\pi_1E$), and suppose $\alpha+\mathrm{Re}\,z_j>\beta$ and $\mathrm{Re}(w+z_j)\ne\beta$ for all
$w\in\pi_1E$ and all $j$. If
$$Pu = f\in H^{k,(E,\alpha),(F,\beta)}_{\mathrm b},\qquad(1-\chi(2y))u\in H^{k+N,(E,\alpha),\infty}_{\mathrm b},\qquad
P := \prod_{j=1}^N(x\partial_x-y\partial_y+z_j),\tag{3.4}$$
then $u\in H^{k,(E,\alpha),((E+Z)\bar\cup F,\beta)}_{\mathrm b}$, with $E+Z$ the sum of Definition 2.7 (4).

For $N = 1$ this is Lemma 3.2 for log-free $E$ ($Z = \{(z_1+m,0):m\in\mathbb N_0\}$ and $E+Z = E+z_1$). Iterating Lemma
3.2 instead loses: once $z$ and $z+1$ both occur, the factor $z+1$ meets the pair $(z+1,0)$ that $E+z$ has put into the
index set at $y = 0$ and returns $(z+1,1)$, which $(E+Z)\bar\cup F$ need not contain. The cure is to solve for each
coefficient in $x$ at once.

*Proof.* Order the factors so that $\mathrm{Re}\,z_1\ge\dots\ge\mathrm{Re}\,z_N$, and let $G := (E+Z)\bar\cup F$.

*Step 1, at $x = 0$, one coefficient at a time.* As $E$ has no logarithms, (3.1) gives
$P(x^wa(y,q)) = x^w\prod_j(w+z_j-y\partial_y)a$ exactly. For $w\in\pi_1E$ with $\mathrm{Re}\,w\le\alpha$, let
$v_w\in H^{k,(F,\beta)}_{\mathrm b}$ be the coefficient of $x^w$ in $f$, and $a_w$ that of $u$ on $\{y\ge\frac38\}$,
which lies in $H^{k+N}$ there by (3.4) and solves $\prod_j(w+z_j-y\partial_y)a_w = v_w$ there. Extend $a_w$ to
$y\in(0,2)$ as the solution of this ordinary differential equation (with constant coefficients in $\log y$, $q$ a
parameter). Put $b_N := a_w$ and $b_{i-1} := (w+z_i-y\partial_y)b_i$, so that $b_0 = v_w$ and
$(y\partial_y-(w+z_i))b_i = -b_{i-1}$. Apply Lemma 1.2 in $y$ for $i = 1,\dots,N$ in this order: its hypothesis
$\beta\ne\mathrm{Re}(w+z_i)$ is ours, and $(1-\chi(y))b_i\in H^k$ because $b_i$ is $N-i$ derivatives of $a_w$ on
$\{y\ge\frac38\}$. It gives $b_i\in H^{k,(G_i,\beta)}_{\mathrm b}$ with $G_0 := F$ and
$G_i := G_{i-1}\bar\cup\{(w+z_i,0)\}$ (Definition 2.7 (6)). The completion by (2.2) at step $i$ adds pairs only at
$w+z_i+m$, $m\ge1$, whose real parts exceed those of every later $w+z_{i'}$. So no later raise meets a completion: the
count at $c$ is raised from $k(F,c)$ once for each $j$ with $w+z_j = c$, to at most
$k(F,c)+k(Z+w,c)+1 = k((Z+w)\bar\cup F,c)$, and a completion reaching $c$ from $c-m$ carries at most the final count at
$c-m$. By induction on $\mathrm{Re}\,c$, $G_N\subset(Z+w)\bar\cup F\subset G$, the extended union being monotone in each
argument and $Z+w\subset E+Z$. Moreover $(y\partial_y)^ma_w$, $m\le N$, is a linear combination of $b_N,\dots,b_{N-m}$,
so it too lies in $H^{k,(G,\beta)}_{\mathrm b}$.

Let $u_0 := \sum_w\chi(x)x^wa_w$, summed over $w\in\pi_1E$ with $\mathrm{Re}\,w\le\alpha$; then
$u_0\in H^{k,(E,\alpha),(G,\beta)}_{\mathrm b}$ near $x = 0$, and
$Pu_0 = \sum_w\chi(x)x^wv_w+\sum_w[P,\chi(x)](x^wa_w)$. Each commutator term is supported in $x\in[\frac12,\frac34]$ and
applies at most $N-1$ of the fields $x\partial_x$, $y\partial_y$ to $x^wa_w$, so it lies in
$H^{k,\infty,(G,\beta)}_{\mathrm b}$ by the last remark. Hence $\tilde u := u-u_0$ satisfies
$P\tilde u =: \tilde f\in H^{k,\alpha,(G,\beta)}_{\mathrm b}$ ($f$ less its expansion at $x = 0$ lies in
$H^{k,\alpha,(F,\beta)}_{\mathrm b}$, and $F\subset G$), and
$(1-\chi(2y))\tilde u\in H^{k+N,\alpha,\infty}_{\mathrm b}$, since the $a_w$ are the coefficients of $u$ on
$\{y\ge\frac38\}$, and on $\{\frac14<y<\frac38\}$, where $1-\chi(2y)\ne0$ too, the coefficient of $u$ solves the same
equation and equals $a_w$ by uniqueness (D229).

*Step 2, the factors one at a time with nothing at $x = 0$.* Put $\tilde w_N := \tilde u$ and
$\tilde w_{i-1} := (x\partial_x-y\partial_y+z_i)\tilde w_i$, so that $\tilde w_0 = \tilde f$. For $i = 1,\dots,N$, Lemma
3.2 with the empty index set at $x = 0$ (its hypothesis on $E$ is then void, $\alpha+\mathrm{Re}\,z_i>\beta$ is ours,
and $(1-\chi(y))\tilde w_i\in H^{k,\alpha,\infty}_{\mathrm b}$ by the order $k+N$ in (3.4)) gives
$\tilde w_i\in H^{k,\alpha,(\emptyset\bar\cup G,\beta)}_{\mathrm b} = H^{k,\alpha,(G,\beta)}_{\mathrm b}$. So
$u = u_0+\tilde w_N\in H^{k,(E,\alpha),(G,\beta)}_{\mathrm b}$. $\square$

## 4. The Fourier transform with partial expansions ([Hin26] section 2.3 at n = 4)

Let $X := \mathbb R^4_x$ (radially compactified), $M := [\overline{\mathbb R}_{t_*}\times\bar
X;\{\pm\infty\}\times\partial\bar X]$ with faces $I$ (the source's $I^+$; lift of $\overline{\mathbb
R}\times\partial\bar X$), $\iota$ (front face) and $K$ (lift of $\partial\overline{\mathbb R}\times X$), the b-densities
$|\frac{dt_*}{\langle t_*\rangle}|$, $|\frac{dx}{\langle x\rangle^4}|$ and their product, and the spaces
$H^{k,(E_I,\beta_I),(E_\iota,\beta_\iota),(E_K,\beta_K)}_{\mathrm b}(M)$ ((2.21)); the testing fields are compositions
of $\partial_{t_*}$, $t_*\partial_{t_*}$, $\langle x\rangle\partial_{x^j}$, $j\le4$. These are Part II.G$'$ section
3.1's $M$ and spaces (there with $\mathscr I$ for $I$), at $n = 4$. At high frequencies $H^{k,\beta,\gamma}_{\mathrm
b+}(\pm[\frac12,\infty)\times X)$ is (2.22) = II.G$'$ section 3.1; at low frequencies $X^\pm_{\mathrm{sc}\text-\mathrm
b} := [\pm[0,1]_\sigma\times\bar X;\{0\}\times\partial\bar X]$ with faces scf, tf, zf and the spaces (2.24) with partial
expansions, as in II.G$'$ (3.2) and the space after it (index set $(0,0)$ at zf, coefficients in $H_{\mathrm b}(X)$).

*The inputs at n = 4.* The source's (2.25a)-(2.26b) are proved at $n = 4$ in Part II.G$'$:

(2.25a) and the matching statement of (2.25b) are II.G$'$ Proposition 3.3 (1): for $\beta_K\in(0,\infty)\setminus\mathbb
N$, $\epsilon\in(0,1)$, $\beta_I\ge\beta_\iota-\min(\beta_K,1-\epsilon)$ and $u\in
H^{k+1,(\beta_I,\beta_\iota,\beta_K)}_{\mathrm b}(M)$, $(\mathcal Fu)|_{\pm(0,1]}\in
H^{k,(\min(\beta_I,\beta_\iota)-\epsilon,\beta_\iota-1,((0,0),\beta_K-1))}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm
b})$, with the $\sigma$-Taylor coefficients of order $<\beta_K-1$ of the two signs equal.

(2.25b) is II.G$'$ Proposition 3.3 (2), with the explicit loss $\ell =
\lceil(\frac12-\min(\beta_K,\beta_\iota-\beta_I))_+\rceil$.

(2.26a) is II.G$'$ Proposition 3.5 (1): with $\ell :=
\lceil(\max(\beta_\iota-\beta_{\mathrm{scf}},\beta_K)+\epsilon-\frac12)_+\rceil$, if $v^\pm\in
H^{k+\ell,(\beta_{\mathrm{scf}},\beta_\iota-1,((0,0),\beta_K-1))}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$ have
the same $\sigma$-Taylor coefficients, then $\mathcal F^{-1}v\in
H^{k,(\min(\beta_{\mathrm{scf}},\beta_\iota)-\epsilon,\beta_\iota,\beta_K)}_{\mathrm b}(M)$, $v :=
\chi(\sigma)\sum_\pm1_{\pm\sigma>0}v^\pm$.

(2.26b) is II.G$'$ Proposition 3.5 (2), whose high-frequency space carries the weight $\delta-1$ where the source's
carries $\delta$ (II.G$'$ finding (J6)); the source's statement, with any $\delta$, follows by renaming $\delta$.

We also use, from the same proofs, that $\mathcal F\circ t_*\partial_{t_*} = (-\sigma\partial_\sigma-1)\circ\mathcal F$
(integration by parts: $\int e^{i\sigma t_*}t_*\partial_{t_*}u = -\int(i\sigma t_*+1)e^{i\sigma t_*}u$, and
$\partial_\sigma\mathcal Fu = \mathcal F(it_*u)$), and that $\mathcal F$ commutes with operators in $x$. As
$\sigma\partial_\sigma$ commutes with $1_{\pm\sigma>0}$ and $[\sigma\partial_\sigma,\chi(\sigma)] = \sigma\chi'(\sigma)$
is supported in $\frac12\le|\sigma|\le1$, we have, for $v$ as in (2.26a) and any $z$,
$$\mathcal F^{-1}\big((\sigma\partial_\sigma-(z-1))w\big) = (-t_*\partial_{t_*}-z)\mathcal F^{-1}w\tag{4.1}$$
for every tempered $w$, and
$(\sigma\partial_\sigma-(z-1))v = \chi(\sigma)\sum_\pm1_{\pm\sigma>0}(\sigma\partial_\sigma-(z-1))v^\pm+r$ with $r$
supported in $\frac12\le|\sigma|\le1$. Such an $r$, if of class $H^{k',\beta_{\mathrm{scf}}}$ there, has
$\mathcal F^{-1}r\in H^{k'-\ell',(\beta_{\mathrm{scf}}-\epsilon,N,N)}_{\mathrm b}(M)$ for every $N$, with a loss
$\ell' = \ell'(N)$ that grows with $N$ (II.G$'$ Proposition 3.5 (1)) and is finite for the finitely many $N$ used, by
(2.26a) with the tf- and zf-weights taken arbitrarily large (it vanishes near tf and zf); we call such terms *harmless*.

**Lemma 4.1 ([Hin26] Lemma 2.24).** Let $\chi\in C^\infty_c((-1,1))$ equal 1 near 0. The following are b-normal vector
fields: (1) $-t_*\partial_{t_*}$ at $K$; (2) $-t_*\partial_{t_*}-\chi(r^{-1})r\partial_r$ at $\iota$ (defined as
$-t_*\partial_{t_*}$ near $r = 0$); (3) $-\chi(r^{-1})r\partial_r$ at $I$; (4) $\sigma\partial_\sigma$ at zf; (5)
$\sigma\partial_\sigma+\chi(\rho)\rho\partial_\rho$ at tf; (6) $\chi(\rho)\rho\partial_\rho$ at scf; here $r = |x|$,
$\rho = |x|^{-1}$, $\omega = x/|x|\in\mathbb S^3$.

*Proof.* In $t_*>1$ let $\tau := t_*^{-1}$, so $-t_*\partial_{t_*} = \tau\partial_\tau$. Near $\iota\cap K$: $\rho_\iota
= \rho$, $\rho_K = \tau/\rho$; then $\tau\partial_\tau = \rho_K\partial_{\rho_K}$ and $\rho\partial_\rho =
\rho_\iota\partial_{\rho_\iota}-\rho_K\partial_{\rho_K}$, so $-t_*\partial_{t_*}-r\partial_r =
\tau\partial_\tau+\rho\partial_\rho = \rho_\iota\partial_{\rho_\iota}$, and near $K^\circ$ (coordinates $\tau$, $x$)
$-t_*\partial_{t_*} = \tau\partial_\tau$ with $\tau$ defining $K$. Near $\iota\cap I$: $\rho_\iota = \tau$, $\rho_I =
\rho/\tau$; $\tau\partial_\tau = \rho_\iota\partial_{\rho_\iota}-\rho_I\partial_{\rho_I}$, $\rho\partial_\rho =
\rho_I\partial_{\rho_I}$, so the field in (2) is $\rho_\iota\partial_{\rho_\iota}$ and $-r\partial_r =
\rho_I\partial_{\rho_I}$, and near $I^\circ$ (coordinates $t_*$, $\rho$, $\omega$) $-r\partial_r = \rho\partial_\rho$.
The same holds for $t_*<-1$. On $X^\pm_{\mathrm{sc}\text-\mathrm b}$ near zf$\cap$tf: $\rho_{\mathrm{zf}}
= |\sigma|/\rho$, $\rho_{\mathrm{tf}} = \rho$, and $\sigma\partial_\sigma =
\rho_{\mathrm{zf}}\partial_{\rho_{\mathrm{zf}}}$, $\rho\partial_\rho =
\rho_{\mathrm{tf}}\partial_{\rho_{\mathrm{tf}}}-\rho_{\mathrm{zf}}\partial_{\rho_{\mathrm{zf}}}$, so
$\sigma\partial_\sigma+\rho\partial_\rho = \rho_{\mathrm{tf}}\partial_{\rho_{\mathrm{tf}}}$; near zf$^\circ$,
$\sigma\partial_\sigma = \rho_{\mathrm{zf}}\partial_{\rho_{\mathrm{zf}}}$ with $\rho_{\mathrm{zf}} = |\sigma|$. Near
tf$\cap$scf: $\rho_{\mathrm{scf}} = \rho/|\sigma|$, $\rho_{\mathrm{tf}} = |\sigma|$; $\rho\partial_\rho =
\rho_{\mathrm{scf}}\partial_{\rho_{\mathrm{scf}}}$ and $\sigma\partial_\sigma =
\rho_{\mathrm{tf}}\partial_{\rho_{\mathrm{tf}}}-\rho_{\mathrm{scf}}\partial_{\rho_{\mathrm{scf}}}$, so (5) is
$\rho_{\mathrm{tf}}\partial_{\rho_{\mathrm{tf}}}$ there too, and (6) holds. In each case the field equals the normal
field of an adapted chart exactly, and the cut-offs act only away from the face. $\square$

**Proposition 4.2 ([Hin26] Proposition 2.25 at n = 4, with (L1)-(L2) repaired).** Let
$\beta_K\in(0,\infty)\setminus\mathbb N$, $\beta_I,\beta_\iota\in\mathbb R$, and $E_I,E_\iota,E_K$ index sets with
$\beta_I,\beta_\iota-1\notin\mathrm{Re}\,\pi_1E_I$, $\beta_\iota\notin\mathrm{Re}\,\pi_1E_\iota$,
$\beta_K\notin\mathrm{Re}\,\pi_1E_K$ and $\min\mathrm{Re}\,E_K>0$.

(1) (Fourier transform.) Suppose
$$\beta_I\ge\beta_\iota-\beta_K,\qquad\beta_I>\beta_\iota-\min(1,\min\mathrm{Re}\,E_K).\tag{4.2}$$
Let $\epsilon>0$ be small and $\tilde\beta_\iota := \min(\beta_\iota,\min\mathrm{Re}\,E_\iota-\epsilon)$. There is
$l\in\mathbb N_0$, depending only on the weights and index sets, such that for $u\in
H^{k+l,(E_I,\beta_I),(E_\iota,\beta_\iota),(E_K,\beta_K)}_{\mathrm b}(M)$,
$$(\mathcal Fu)|_{\sigma\in\pm[0,1]}\in H^{k,\ (E_I,\min(\beta_I,\tilde\beta_\iota)-\epsilon),\ ((E_\iota-1)\bar
\cup E_I,\beta_\iota-1),\ ((0,0)\bar\cup(E_K-1),\beta_K-1)}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b}).\tag{4.3}$$

(2) (Inverse Fourier transform.) Let $\chi\in C^\infty_c((-1,1))$ equal 1 near $[-\frac12,\frac12]$,
$\beta_{\mathrm{scf}}\in\mathbb R$, $\epsilon$ and $\tilde\beta_\iota$ as in (1). There is $l\in\mathbb N_0$ such that
if $v^\pm\in H^{k+l,\ \beta_{\mathrm{scf}},\ (E_\iota-1,\beta_\iota-1),\ ((0,0)\bar\cup(E_K-1),\beta_K-1)}_{\mathrm
b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$ satisfy, at zf,
$$(\sigma\partial_\sigma)^{\ell_j+1}\partial^j_\sigma v^- = (\sigma\partial_\sigma)^{\ell_j+1}\partial^j_\sigma v^+,
\qquad
j = 0,\dots,\lfloor\beta_K-1\rfloor,\quad\ell_j := k(E_K,j+1),\tag{4.4}$$
then for $v := \chi(\sigma)\sum_\pm1_{\pm\sigma>0}v^\pm$,
$$\mathcal F^{-1}v\in H^{k,\ \min(\beta_{\mathrm{scf}},\tilde\beta_\iota)-\epsilon,\ (E_\iota,\beta_\iota),\ (E_K,
\beta_K)}_{\mathrm b}(M).\tag{4.5}$$

(The source's (2.29) has $\ell = k(E_K,j)$; finding (L1). The meaning of (4.4): by
$(\sigma\partial_\sigma)\partial^j_\sigma = \partial^j_\sigma(\sigma\partial_\sigma-j)$, it says that the coefficient of
$\sigma^j$ in $(\sigma\partial_\sigma-j)^{\ell_j+1}v^\pm$, which is log-free, is the same for both signs. The factor
$\sigma\partial_\sigma-j$ occurs $k(E_K,j+1)+1$ times in $R_{\mathrm{zf}}$ below, as $(z,m)\in E_K$ with $z-1 = j$.)

*Proof.* We take $\epsilon$ so small, and decrease it if necessary, that none of
$\min(\beta_I,\tilde\beta_\iota)-\epsilon$, $\tilde\beta_K := \min(\beta_K,\min\mathrm{Re}\,E_K-\epsilon)$ and
$\min\mathrm{Re}\,E_\iota-\epsilon$ is an integer or the real part of an element of $\pi_1E_I$, $\pi_1E_K$ (finitely
many conditions below any bound). We write $E_{\iota,\le} := \{(z,m)\in E_\iota:\mathrm{Re}\,z\le\beta_\iota\}$ and
similarly $E_{K,\le}$, $E_{I,\le}$.

*Part (1), $E_I = \emptyset$.* Then $u\in H^{k+l,(\beta_I,\tilde\beta_\iota,\tilde\beta_K)}_{\mathrm b}(M)$, and the
hypotheses of (2.25a) hold for these weights: $\beta_I\ge\tilde\beta_\iota-\tilde\beta_K$ (if $\tilde\beta_K = \beta_K$
by (4.2), and otherwise because $\beta_I>\beta_\iota-\min\mathrm{Re}\,E_K\ge\tilde\beta_\iota-\tilde\beta_K-\epsilon$
strictly, so for small $\epsilon$), and $\beta_I\ge\tilde\beta_\iota-(1-\epsilon)$ for small $\epsilon$, as
$\beta_I>\beta_\iota-1$. They remain true when $\tilde\beta_K$ is increased up to $\beta_K$ or $\tilde\beta_\iota$ up to
$\beta_\iota$. So (2.25a) gives
$$\mathcal Fu\in H^{k,(\min(\beta_I,\tilde\beta_\iota)-\epsilon,\ \tilde\beta_\iota-1,\ ((0,0),\tilde\beta_K-1))}_{
\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b}).
\tag{4.6}$$
Let $R_\iota := \prod_{(z,m)\in E_{\iota,\le}}(-t_*\partial_{t_*}-\chi(r^{-1})r\partial_r-z)$. By Lemma 1.3's converse
at $\iota$ (Lemma 4.1 (2)) and (F1) at $I$ and $K$, $R_\iota u\in
H^{k+l-|E_{\iota,\le}|,(\beta_I,\beta_\iota,\tilde\beta_K)}_{\mathrm b}$, so for $l$ large (2.25a) gives $\mathcal
F(R_\iota u)\in H^{k,(\min(\beta_I,\beta_\iota)-\epsilon,\beta_\iota-1,((0,0),\tilde\beta_K-1))}$. As $\mathcal
F(-t_*\partial_{t_*}u) = (\sigma\partial_\sigma+1)\mathcal Fu$ and $-r\partial_r = \rho\partial_\rho$ commutes with
$\mathcal F$, $\mathcal F(R_\iota u) =
\prod_{E_{\iota,\le}}(\sigma\partial_\sigma+\chi(\rho)\rho\partial_\rho-(z-1))\mathcal Fu$. Weakening its scf-weight to
$\min(\beta_I,\tilde\beta_\iota)-\epsilon$, Lemma 1.3 at tf (Lemma 4.1 (5); its hypothesis is
$\beta_\iota-1\notin\mathrm{Re}\,\pi_1(E_\iota-1)$; its a priori hypothesis away from tf is (4.6)) gives
$$\mathcal Fu\in H^{k,(\min(\beta_I,\tilde\beta_\iota)-\epsilon,\ (E_\iota-1,\beta_\iota-1),\ ((0,0),\tilde
\beta_K-1))}_{\mathrm b}.\tag{4.7}$$
Now let $R_K := \prod_{(z,m)\in E_{K,\le}}(-t_*\partial_{t_*}-z)$. By Lemma 1.3's converse at $K$ (Lemma 4.1 (1)) and
(F1), $R_Ku\in H^{k+l-|E_{K,\le}|,(\beta_I,(E_\iota,\beta_\iota),\beta_K)}_{\mathrm b}$, with the full weight $\beta_K$
at $K$; (4.7) applied to it (with $\tilde\beta_K$ replaced by $\beta_K$, allowed above) gives
$$\prod_{(z,m)\in E_{K,\le}}(\sigma\partial_\sigma-(z-1))\,\mathcal Fu = \mathcal F(R_Ku)\in
H^{k,(\min(\beta_I,\tilde\beta_\iota)-\epsilon,\ (E_\iota-1,\beta_\iota-1),\ ((0,0),\beta_K-1))}_{\mathrm b}.$$
Apply in addition $\prod_{j\le\lfloor\beta_K-1\rfloor}(\sigma\partial_\sigma-j)$, which annihilates the zf-terms of
index set $(0,0)$ with real part $\le\beta_K-1$, so that the right side has empty index set at zf and weight
$\beta_K-1$; then integrate one factor at a time, in decreasing order of real part as in Lemma 1.3, by Lemma 1.2 at zf
(Lemma 4.1 (4); its hypotheses are $\beta_K-1\ne j$, true as $\beta_K\notin\mathbb N$, and
$\beta_K-1\ne\mathrm{Re}(z-1)$, true as $\beta_K\notin\mathrm{Re}\,\pi_1E_K$; the a priori hypothesis away from zf is
(4.7)). The index set obtained at zf is $(0,0)\bar\cup(E_K-1)$ (below the weight $\beta_K-1$): in this order each
exponent $c$ is raised once per factor, from $-1$ to $k((0,0),c)+k(E_K-1,c)+1$, and the completions by (2.2) stay below
that. Each one-factor step costs at most one derivative (as in Lemma 1.3), absorbed in $l$. With (4.7) at tf and scf
this is (4.3).

*Part (1), general $E_I$.* Let $\chi_K\in C^\infty(M)$ equal 1 near $K$ and 0 near $I$. $\chi_Ku$ vanishes near $I$, so
it lies in the space with $E_I = \emptyset$ and any $I$-weight $\beta'_I\ge\beta_I$; the case just proved, with
$\beta'_I$ so large that $\min(\beta'_I,\tilde\beta_\iota) = \tilde\beta_\iota$, gives (4.3) for it (its tf index set
$E_\iota-1$ lies in $(E_\iota-1)\bar\cup E_I$). So assume $u$ vanishes near $K$; then $E_K = \emptyset$ and the
$K$-weight is arbitrary: fix $\beta_K\notin\mathbb N$, at least its given value (so (4.2) persists), with
$\beta_K>\beta_\iota+\max(0,-\min\mathrm{Re}\,E_I)$, so that $\beta_K-1+\mathrm{Re}\,z>\beta_\iota-1$ for every
$z\in\pi_1E_I$, as Lemma 3.3 needs. Let $\tilde\chi\in C^\infty_c(X)$ equal 1 on $\{|x|\le8\}$. As $u$ vanishes near
$K$, $\tilde\chi u$ has compact support in $(t_*,x)$, so $\mathcal F(\tilde\chi u)$ is entire in $\sigma$ with values in
$H^{k+l}_{\mathrm b}$ of compact support in $x$: it lies in
$H^{k+l,(\infty,\infty,((0,0),\beta_K-1))}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$. Let
$R_I := \prod_{(z,m)\in E_{I,\le}}(-\chi(r^{-1})r\partial_r-z)$; by Lemma 1.3's converse at $I$ (Lemma 4.1 (3)) and
(F1), $R_Iu\in H^{k+l-|E_{I,\le}|,(\beta_I,(E_\iota,\beta_\iota),\beta_K)}_{\mathrm b}$, and the case $E_I = \emptyset$
gives
$$\prod_{(z,m)\in E_{I,\le}}(\chi(\rho)\rho\partial_\rho-z)\,\mathcal Fu
= \mathcal F(R_Iu)\in H^{k+l',\ (\min(\beta_I,\tilde\beta_\iota)-\epsilon,\ (E_\iota-1,\beta_\iota-1),\ ((0,0),
\beta_K-1))}_{\mathrm b},
\quad l' := l-|E_{I,\le}|-l_0,$$
$l_0$ the loss of the case $E_I = \emptyset$. Integrate from $\rho\ge\frac18$, where
$\mathcal Fu = \mathcal F(\tilde\chi u)$, towards $\rho = 0$. Near zf, in $\rho_{\mathrm{zf}} = |\sigma|/\rho$,
$\rho_{\mathrm{tf}} = \rho$, each factor $\rho\partial_\rho-z$ equals
$-(\rho_{\mathrm{zf}}\partial_{\rho_{\mathrm{zf}}}-\rho_{\mathrm{tf}}\partial_{\rho_{\mathrm{tf}}}+z)$, so the product
is $\pm$ the operator of Lemma 3.3 with $x = \rho_{\mathrm{zf}}$, $y = \rho_{\mathrm{tf}}$, one $z_j$ for each
$(z,m)\in E_{I,\le}$ (so $z$ occurs $k(E_I,z)+1$ times and $Z$ is $E_{I,\le}$ completed by (2.2), contained in $E_I$),
$(E,\alpha) = ((0,0),\beta_K-1)$, which has no logarithms, and $(F,\beta) = (E_\iota-1,\beta_\iota-1)$. Its hypotheses
hold: $\beta_K-1+\mathrm{Re}\,z>\beta_\iota-1$ by the choice of $\beta_K$; $\mathrm{Re}(w+z)\ne\beta_\iota-1$ for
$w\in\mathbb N_0$, as $\beta_\iota-1\notin\mathrm{Re}\,\pi_1E_I$ and index sets are closed under adding $\mathbb N_0$;
and on $\rho\ge\frac14$, where $1-\chi(2\rho)\ne0$, the a priori condition is $\mathcal Fu = \mathcal F(\tilde\chi u)$,
of order $k+l\ge k+l'+|E_{I,\le}|$. As $(0,0)+Z = Z$, Lemma 3.3 gives the index sets $((0,0),\beta_K-1)$ at zf and
$(Z\bar\cup(E_\iota-1),\beta_\iota-1)\subset(E_I\bar\cup(E_\iota-1),\beta_\iota-1)$ at tf. (Integrating one factor at a
time by Lemma 3.2, as the source does and as this proof did before D226, returns $(z+1,1)$ at tf whenever $z$ and $z+1$
both occur, a logarithm (4.3) does not contain; finding (L6).) Near scf, in $\rho_{\mathrm{scf}} = \rho/|\sigma|$,
$\rho_{\mathrm{tf}} = |\sigma|$, $\rho\partial_\rho-z = \rho_{\mathrm{scf}}\partial_{\rho_{\mathrm{scf}}}-z$, and Lemma
1.2 at scf, one factor at a time in decreasing order of $\mathrm{Re}\,z$ as in Lemma 1.3 (with
$\min(\beta_I,\tilde\beta_\iota)-\epsilon\ne\mathrm{Re}\,z$ by the choice of $\epsilon$; the a priori condition on
$\rho_{\mathrm{scf}}\ge\frac12$ holds in the zf chart, and the tf index set found there is carried as the data at the
other face), gives the index set $(E_I,\min(\beta_I,\tilde\beta_\iota)-\epsilon)$ there, the derivatives lost one factor
at a time absorbed in $l$. This is (4.3).

*Part (2), $E_K = \emptyset$.* Then (4.4) is the equality of the $\sigma$-Taylor coefficients of $v^\pm$ of orders
$\le\lfloor\beta_K-1\rfloor$ (as $\ell_j = -1$), and $v^\pm\in
H^{k+l,(\beta_{\mathrm{scf}},\tilde\beta_\iota-1,((0,0),\beta_K-1))}$, so (2.26a) gives
$$u := \mathcal F^{-1}v\in H^{k+l-l_1,(\beta'_I,\tilde\beta_\iota,\beta_K)}_{\mathrm b}(M),\qquad\beta'_I :
= \min(\beta_{\mathrm{scf}},\tilde\beta_\iota)-\epsilon,
\tag{4.8}$$
$l_1$ the loss of (2.26a). Let $R_{\mathrm{tf}} := \prod_{(z,m)\in
E_{\iota,\le}}(\sigma\partial_\sigma+\chi(\rho)\rho\partial_\rho-(z-1))$. By Lemma 1.3's converse at tf (Lemma 4.1 (5)),
$R_{\mathrm{tf}}v^\pm\in H^{k+l-|E_{\iota,\le}|,(\beta_{\mathrm{scf}},\beta_\iota-1,((0,0),\beta_K-1))}_{\mathrm b}$,
and the $\sigma$-Taylor coefficients of $R_{\mathrm{tf}}v^\pm$ still agree: near zf, $\sigma\partial_\sigma$ multiplies
the coefficient of $\sigma^j$ by $j$ and $\chi(\rho)\rho\partial_\rho$ acts on the coefficients in $x$, the same on both
sides. By (4.1), $\mathcal F^{-1}(R_{\mathrm{tf}}v) = \prod(-t_*\partial_{t_*}-\chi(r^{-1})r\partial_r-z)u$, while
$R_{\mathrm{tf}}v$ equals $\chi(\sigma)\sum_\pm1_{\pm\sigma>0}R_{\mathrm{tf}}v^\pm$ up to harmless terms; so (2.26a)
gives
$$\prod_{(z,m)\in E_{\iota,\le}}(-t_*\partial_{t_*}-\chi(r^{-1})r\partial_r-z)\,
u\in H^{k+l-|E_{\iota,\le}|-l_1,(\beta'_I,\beta_\iota,\beta_K)}_{\mathrm b}(M),$$
and Lemma 1.3 at $\iota$ (Lemma 4.1 (2); $\beta_\iota\notin\mathrm{Re}\,\pi_1E_\iota$; a priori hypothesis (4.8)) gives
(4.5) with $E_K = \emptyset$.

*Part (2), general $E_K$.* Weakening the zf data to $((0,0),\tilde\beta_K-1)$ (the terms of $E_K-1$, and their
$\bar\cup$ with $(0,0)$, have real part $\ge\min\mathrm{Re}\,E_K-1>\tilde\beta_K-1$) and using (4.4) for
$j\le\lfloor\tilde\beta_K-1\rfloor$, where it is the plain matching (as $j+1<\min\mathrm{Re}\,E_K$ gives $\ell_j = -1$),
the case just proved gives $u\in H^{k+l-l_2,(\beta'_I,(E_\iota,\beta_\iota),\tilde\beta_K)}_{\mathrm b}(M)$. Let
$R_{\mathrm{zf}} := \prod_{(z,m)\in E_{K,\le}}(\sigma\partial_\sigma-(z-1))$. It annihilates the zf-terms of $E_K-1$
below $\beta_K-1$, so $R_{\mathrm{zf}}v^\pm\in
H^{k+l-|E_{K,\le}|,(\beta_{\mathrm{scf}},(E_\iota-1,\beta_\iota-1),((0,0),\beta_K-1))}_{\mathrm b}$ (the source prints
the zf-weight $\beta_K$; finding (L2)). Its coefficient of $\sigma^j$, $j\le\lfloor\beta_K-1\rfloor$, is a nonzero
constant (the product of $j-(z-1)$ over the factors with $z-1\ne j$, the same for both signs) times the coefficient of
$\sigma^j$ in $(\sigma\partial_\sigma-j)^{\ell_j+1}v^\pm$, so (4.4) is exactly the matching of the Taylor coefficients
of $R_{\mathrm{zf}}v^\pm$. By (4.1) and the case $E_K = \emptyset$ (harmless terms aside),
$$\prod_{(z,m)\in E_{K,\le}}(-t_*\partial_{t_*}-z)\,u
= \mathcal F^{-1}(R_{\mathrm{zf}}v)\in H^{k',(\beta'_I,(E_\iota,\beta_\iota),\beta_K)}_{\mathrm b}(M),$$
and Lemma 1.3 at $K$ (Lemma 4.1 (1); $\beta_K\notin\mathrm{Re}\,\pi_1E_K$) gives the index set $(E_K,\beta_K)$ at $K$.
With $l$ the sum of the losses met, this is (4.5). $\square$

## 5. What is used later

Part III's later sections use: Lemma 1.3 (testing) and Lemma 1.2 (integration) to prove partial expansions at the faces
of $M$ and $X_{\mathrm{sc}\text-\mathrm b}$; Lemma 1.4 and Lemma 1.5 for normal-operator expansions at sf, where the
indicial roots are those of Part III.A$'$; Lemma 2.4 and (2.4)-(2.5) for the spectral families and the normal operator
at sf of the stationary operators of Part III.B at $n = 4$; Lemmas 3.1-3.3 for the integration of the transport
operators at $\iota$ and $I$; and Proposition 4.2 for the passage between the time and frequency sides. Every statement
here is in b-densities, so the numbers in the hypotheses ($\beta_\iota-1$, $\beta_K-1$, the conditions (4.2)) are those
of the source; the dimension enters only through the inputs from Part II.G$'$, which are proved at $n = 4$.

## 6. Labels

Proved here: Lemmas 1.1-1.5, 2.4, 3.1-3.3, 4.1 and Proposition 4.2, the identities in Definitions 2.1-2.3 and
(2.4)-(2.5). Proved in Part II.G$'$ at $n = 4$: the inputs (2.25a)-(2.26b). Standard facts used without proof, and
named: Plancherel's theorem; the elliptic estimate with a large parameter and analytic Fredholm theory for
$N(A,\lambda)$ (E1)-(E2); elliptic regularity in the interior; Cauchy's integral formula. Definitions are the source's,
read at source.

## 7. Findings and sources

### 7.1 Findings

(L1) *The matching condition (2.29).* The source requires $(\sigma\partial_\sigma)^{\ell+1}\partial^j_\sigma v^- =
(\sigma\partial_\sigma)^{\ell+1}\partial^j_\sigma v^+$ at zf with $\ell = k(E_K,j)$. The log terms of $v^\pm$ at
$\sigma^j$ come from $E_K-1$ at $j$, that is from $(j+1,\cdot)\in E_K$, and the operator $R_{\mathrm{zf}}$ of the proof
contains $\sigma\partial_\sigma-j$ exactly $k(E_K,j+1)+1$ times; so the condition must use $\ell_j = k(E_K,j+1)$. With
the printed $\ell$, already $E_K = (1,0)$ fails: $v^\pm$ then carries $a^\pm\log|\sigma|$ at zf, the printed condition
at $j = 0$ ($\ell = k(E_K,0) = -1$) is "$v^- = v^+$ at zf", which is meaningless for a logarithmically divergent
function, while the condition the proof needs is $a^- = a^+$. Repaired in (4.4).

(L2) *A weight in the proof of Proposition 2.25 (2).* The source states $R_{\mathrm{zf}}v^\pm\in
H^{\cdots,((0,0),\beta_K)}$; the zf-weight is $\beta_K-1$ (the factors annihilate the terms of $E_K-1$ below
$\beta_K-1$, nothing more), which is what the case $E_K = \emptyset$ needs to give the $K$-weight $\beta_K$. Harmless
once corrected.

(L3) *The commutator with the cut-off in $\sigma$.* The source's proof of Proposition 2.25 (2) applies $\mathcal
F^{-1}\circ(\sigma\partial_\sigma+1) = -t_*\partial_{t_*}\circ\mathcal F^{-1}$ to $v = \chi(\sigma)\sum_\pm
H(\pm\sigma)v^\pm$ without comment; $\sigma\partial_\sigma$ does not commute with $\chi(\sigma)$. The commutator is
supported in $\frac12\le|\sigma|\le1$ and its inverse transform is harmless ((4.1)); recorded, not a gap in the result.

(L4) *Cauchy's formula in Lemma 2.15.* The source prints $\rho^\lambda(\log\rho)^\ell = \frac1{2\pi
i\,\ell!}\oint\rho^\zeta(\zeta-\lambda)^{-\ell-1}d\zeta$; the constant is $\frac{\ell!}{2\pi i}$. Harmless (a constant).

(L5) *The hypothesis of Lemma 2.23.* The source assumes $\alpha>\beta$ and reduces to $z = 0$ by $u\mapsto x^zu$, which
turns $\alpha$ into $\alpha+\mathrm{Re}\,z$; the case $z = 0$ needs $\alpha+\mathrm{Re}\,z>\beta$, and the condition is
necessary: for $\alpha+\mathrm{Re}\,z<c<\beta$, $u := x^{-z}\chi(xy)(xy)^c$ solves $(x\partial_x-y\partial_y+z)u = 0$,
satisfies the a priori condition with $E = \emptyset$, and is not in $H^{k,\alpha,\beta}_{\mathrm b}$, being $y^c$ times
a smooth nonvanishing function near $y = 0$, $x = \frac12$. Repaired in Lemma 3.2. In Proposition 2.25 the weight
$\beta_K$ is free in the case where the condition is used (the function vanishes near $K$) and is taken large enough
(D226).

(L6) *The iteration in the proof of Proposition 2.25 (1).* For general $E_I$ the source integrates the factors of $R_I$
one at a time by Lemma 2.23 and states the tf index set $E_I\bar\cup(E_\iota-1)$. Each step adds $E+z = z+\mathbb N_0$
at tf ($E = (0,0)$ at zf), so once $z$ and $z+1$ both occur in $E_{I,\le}$, in either order of integration, the extended
union returns $(z+1,1)$, a logarithm the stated set need not contain; the proof as printed gives a strictly larger index
set. The stated set is right: it follows coefficient by coefficient in the zf variable (Lemma 3.3), which this part now
uses. Found by the ninety-third verifier (D226).

(L7) *Two conventions left implicit.* The source's Lemma 2.11 integrates one factor at a time in no stated order; by
Definition 2.7 (6) the result depends on the order (for $V(V-1)$, integrating $V$ first gives $(1,1)$), and decreasing
real part gives the stated set (Lemma 1.3). Its Lemmas 2.13 and 2.15 reach the weight $\beta$ only if no exponent of $F$
has real part $\beta$ or those terms are solved first (Lemmas 1.4, 1.5). Found by the ninety-third verifier (D226).

### 7.2 Sources

READ: [Hin26] pp. 44-63 (sections 2.1-2.3: Notation 2.1 to Proposition 2.25 with its proof), arXiv:2606.28253v2, full
text in the record's extraction. Part II.G$'$ (Propositions 3.3, 3.5, Lemma 3.1) for the inputs. Not read and not relied
on: [Mel93] Proposition 5.61 and Lemma 5.44, [Mel96], [Hin25a] Proposition 3.17, [Hin25c] Proposition 3.3, [Hin23d]
Proposition 2.28, [HV20] section 7 (the statements are proved here).
