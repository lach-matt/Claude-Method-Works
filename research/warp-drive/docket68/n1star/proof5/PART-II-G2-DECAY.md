# Part II.G$'$. Improving decay: Fourier transforms, resolvent bounds and the radiation field, at n = 4

*Status.* Verified (D216). Written out in full (D214) and read line by line by the ninetieth verifier, which found no
major gap; its two minor findings and eleven nits are seated (section 7.3). Nothing here is labelled proved until a
reader has read those repairs. This part proves, at spatial dimension $n = 4$, the tools of [Hin26c] section 13 (pp.
243-260) by which forward solutions are shown to decay faster than Theorem 11.1 alone gives: the Fourier transform in
time on weighted b-Sobolev spaces, on the line and on the resolved product spaces (the source's 13.1); the translation
of Part I's resolvent estimates at nonzero, high and low frequencies into b-Sobolev spaces with a loss of b-regularity
independent of the order (13.2); and the radiation field at null infinity (13.3). The source is [Hin26c] = P. Hintz,
arXiv:2606.28008v1 (printed page numbers). Parts I.A (`PART-I-SPECTRAL.md`), I.B (`PART-I-B-HIGHENERGY.md`), I.C
(`PART-I-C-LOWENERGY.md`), II.A (`PART-II-A-SETUP.md`), II.C (`PART-II-C-OPERATORS.md`) and II.F$'$
(`PART-II-F2-TAME.md`) are cited as I.A, I.B, I.C, II.A, II.C and II.F$'$.

*Method.* The source's section 13.1 states its results for every $n$; they are proved here, at $n = 4$, with one change
of route. The facts on the line that the source draws from [Tay11a] and from complex interpolation are proved instead
from the Gagliardo seminorm and two Hardy inequalities, by a dyadic argument (section 2). Doing so shows that the
source's Lemma 13.4, with the weight at both ends as it insists, fails at $\sigma = \infty$, and that its spaces
(13.7)-(13.8) as printed carry no Taylor terms; neither affects Corollary 13.7, the lossy form which is all that is used
later, and which is proved here directly (Proposition 2.8). In section 4 the dimension enters through the density, which
shifts weights by $\frac n2 = 2$ where the source has $\frac32$, and through the threshold $\frac32+\bar S$ of I.A
Theorem 7.2 (5) where the source has $1+\bar S$. The high-energy bound, which the source states without proof, is proved
from I.B Theorem 1.3 with a comparison lemma in I.B's semiclassical calculus. In section 5 the indicial root at null
infinity is $\frac32 = \frac{n-1}2$, so the radiation field is the coefficient of $r^{-3/2}$; the two ordinary
differential equation lemmas that the source takes from [Hin26b] are proved here (Lemmas 3.2 and 5.3).

*Organisation.* Section 1: scope and the changes at $n = 4$. Section 2: the line. Section 3: the resolved product
spaces. Section 4: resolvent bounds. Section 5: the radiation field. Section 6: what is not carried. Section 7: findings
and sources.

## 1. Scope, and what n = 4 changes

[Hin26c] section 13, "Improving decay", has four subsections. Its subsections 13.1-13.3 are general tools and are
carried here: the Fourier transform on the line (Lemmas 13.2, 13.4, 13.6, Corollaries 13.3, 13.5, 13.7) and on the
resolved spaces (Lemma 13.8, Propositions 13.9 and 13.11, Lemma 13.10, Remark 13.12); the resolvent bounds (Lemma 13.13,
Corollary 13.14, Proposition 13.16, Corollary 13.17, the bounds (13.30), Proposition 13.18); and the radiation field
(Definition 13.19, Proposition 13.20). Its subsection 13.4 (Theorem 13.21 and Remark 13.22) is a model application to
the scalar wave equation on Kerr and is not carried (section 6). The route uses these tools in Part III, where the decay
of solutions of the linearised gauge-fixed Einstein equations is improved beyond Theorem 11.1 as the source's section 14
does for its 1-form example.

At $n = 4$ the statements change as follows; each change is derived where the statement is proved.

(a) *Densities.* On $X$, $\mu := |dx|$ and $\mu_b := |dx|/\langle x\rangle^4$, so $L^2(X,\mu) = \rho^2L^2(X,\mu_b)$,
$\rho := \langle x\rangle^{-1}$: a scattering decay order $\mathsf r$ is a b-weight $\mathsf r+2$. The source's shifts
$\frac52$ and $\frac32$ in (13.23a)-(13.23b) become $3$ and $2$, and its $\frac52$, $\frac72$, $\frac32$ in (13.30)
become $3$, $4$, $2$.

(b) *Thresholds.* The source's $\beta_{\mathrm{scf}}<1+\bar S$ (Corollaries 13.14, 13.17, Propositions 13.16, 13.18) is
$\beta_{\mathrm{scf}}<\frac32+\bar S$, the threshold at the outgoing radial set $\mathsf r<-\frac12+\bar S$ of I.A (1.5)
read as a b-weight.

(c) *The zero energy gap.* The gap condition of Proposition 13.18 is on the b-weight for $\mu_b$, as in I.C (G):
$\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}}$ lies in an indicial gap of $\hat P(0)$.

(d) *The radiation field.* Near $\mathscr I^+\cap\iota^+$ the stationary model has the form
$\frac12\rho_I^{-1}\rho_+^{-2}P_0 =
-(\rho_I\partial_{\rho_I}-\frac32)(\rho_I\partial_{\rho_I}-\rho_+\partial_{\rho_+})+\tilde P$ (Lemma 5.1), where the
source's (13.32) has $\rho_I\partial_{\rho_I}-1$; the radiation field is the coefficient of $\rho_I^{3/2}$, that is of
$r^{-3/2}$ at bounded $t_*$, and Proposition 13.20 holds with $\frac32$ in place of 1 (Proposition 5.4).

Throughout, $\mathbb N_0 = \{0,1,2,\dots\}$, $\mathcal H$ denotes a separable Hilbert space, functions may be $\mathcal
H$-valued, and $|\cdot|$ is the norm of $\mathcal H$. Constants $C$ may change from line to line and depend only on the
quantities named. For the bundle $E$ of I.A section 1.2 every space is taken componentwise.

## 2. The Fourier transform on the line

### 2.1 Conventions

$(\mathcal Fu)(\sigma) := \int e^{i\sigma t}u(t)\,dt$ and $(\mathcal F^{-1}v)(t) := \frac1{2\pi}\int e^{-i\sigma
t}v(\sigma)\,d\sigma$, as in the source. Plancherel's theorem $\|\mathcal Fu\|_{L^2(d\sigma)} =
(2\pi)^{1/2}\|u\|_{L^2(dt)}$ holds for $\mathcal H$-valued functions (componentwise in an orthonormal basis). $\mathcal
F(\partial_tu) = -i\sigma\mathcal Fu$ and $\mathcal F(tu) = D_\sigma\mathcal Fu$, $D_\sigma := -i\partial_\sigma$. For
$\gamma\in\mathbb R$ let $H^\gamma(\mathbb R_\sigma;\mathcal H) := \{v\in\mathcal S':\langle t\rangle^\gamma\mathcal
F^{-1}v\in L^2(dt)\}$, $\|v\|_{H^\gamma} := (2\pi)^{1/2}\|\langle t\rangle^\gamma\mathcal F^{-1}v\|_{L^2}$; as
$(\mathcal F^{-1}v)(t) = \frac1{2\pi}\hat v(t)$ with $\hat v(\tau) := \int e^{-i\sigma\tau}v(\sigma)\,d\sigma$, this is
the usual Sobolev space, with the usual norm $(2\pi)^{-1/2}\|\langle\tau\rangle^\gamma\hat v\|$.

**Definition 2.1 ([Hin26c] 13.1.1).** For $k\in\mathbb N_0$ and $\beta\in\mathbb R$, $H^{k,\beta}_b(\mathbb R;\mathcal
H)$ is the space of $u\in\mathcal S'$ with $\langle t\rangle^{\beta-\frac12}\partial_t^p(t\partial_t)^qu\in L^2(\mathbb
R,dt;\mathcal H)$ for $p+q\le k$, normed by the sum of these norms.

This is the source's $\langle t\rangle^{-\beta}H^k_b(\mathbb R,|\frac{dt}{\langle t\rangle}|)$: $\langle
t\rangle^{-\beta}L^2(\frac{dt}{\langle t\rangle}) = \langle t\rangle^{-\beta+\frac12}L^2(dt)$, and the b-vector fields
of the radial compactification, spanned by $\langle t\rangle\partial_t$ over its smooth functions, are spanned by
$\partial_t = \langle t\rangle^{-1}\cdot\langle t\rangle\partial_t$ and $t\partial_t = \frac t{\langle t\rangle}\langle
t\rangle\partial_t$, as $\langle t\rangle\partial_t = \langle t\rangle^{-1}\partial_t+\frac t{\langle
t\rangle}t\partial_t$; the words of length $\le k$ in $\partial_t$, $t\partial_t$ span the same space as the ordered
products $\partial_t^p(t\partial_t)^q$, as $[\partial_t,t\partial_t] = \partial_t$.

**Lemma 2.2 ([Hin26c] (13.1)).** $u\in H^{k,\beta}_b(\mathbb R;\mathcal H)$ if and only if
$\sigma^p(\sigma\partial_\sigma)^q\mathcal Fu\in H^{\beta-\frac12}(\mathbb R;\mathcal H)$ for all $p+q\le k$, with
equivalent norms.

*Proof.* $\mathcal F(t\partial_tu) = D_\sigma(-i\sigma\mathcal Fu) = -(1+\sigma\partial_\sigma)\mathcal Fu$, so
$\mathcal F(\partial_t^p(t\partial_t)^qu) = (-i\sigma)^p(-1-\sigma\partial_\sigma)^q\mathcal Fu$. The operators
$\sigma^p(1+\sigma\partial_\sigma)^q$, $p+q\le k$, and $\sigma^p(\sigma\partial_\sigma)^q$, $p+q\le k$, are related by a
triangular matrix with ones on the diagonal (binomial expansion), so they span the same space. And $\|\langle
t\rangle^{\beta-\frac12}w\|_{L^2} = (2\pi)^{-1/2}\|\mathcal Fw\|_{H^{\beta-\frac12}}$ by definition. $\square$

### 2.2 The Gagliardo seminorm and two Hardy inequalities

For $\theta\in(0,1)$ and $g\in L^2(\mathbb R;\mathcal H)$ let $[g]_\theta^2 :=
\iint|g(x)-g(y)|^2|x-y|^{-1-2\theta}\,dx\,dy\in[0,\infty]$.

**Lemma 2.3.** Let $\theta\in(0,1)$.

(a) $[g]_\theta^2 = c_\theta\frac1{2\pi}\int|\xi|^{2\theta}|\hat g(\xi)|^2\,d\xi$ with $c_\theta :=
\int|e^{is}-1|^2|s|^{-1-2\theta}\,ds\in(0,\infty)$. So $\|g\|_{L^2}^2+[g]_\theta^2$ is equivalent to
$\|g\|^2_{H^\theta}$, and for $\psi\in C_c^\infty(\mathbb R)$ and $\varepsilon>0$, $[\psi(\cdot/\varepsilon)]_\theta^2 =
\varepsilon^{1-2\theta}[\psi]_\theta^2$.

(b) If $\theta<\frac12$, then $\int_{-1}^1|x|^{-2\theta}|g|^2\,dx\le C_\theta(\|g\|^2_{L^2(-1,1)}+[g]_\theta^2)$.

(c) If $\theta>\frac12$ and $g\in H^\theta$, then $g$ is continuous, and if $g(0) = 0$ then
$\int_{-1}^1|x|^{-2\theta}|g|^2\,dx\le C_\theta[g]_\theta^2$.

(d) If $\theta<\frac12$ and $w\in L^1_{\mathrm{loc}}$ is supported in $[-1,1]$ with $|x|^\theta w\in L^2$, then $w\in
H^{-\theta}$ and $\|w\|_{H^{-\theta}}\le C_\theta\||x|^\theta w\|_{L^2}$.

*Proof.* (a) For fixed $h$, $\int|g(x+h)-g(x)|^2dx = \frac1{2\pi}\int|e^{ih\xi}-1|^2|\hat g(\xi)|^2d\xi$ by Plancherel.
Integrating against $|h|^{-1-2\theta}dh$ (Tonelli) and substituting $s = h\xi$ gives the identity; $c_\theta<\infty$ as
$|e^{is}-1|^2\le\min(s^2,4)$, and $c_\theta>0$. Then $1+c_\theta|\xi|^{2\theta}$ is comparable to
$\langle\xi\rangle^{2\theta}$. The scaling follows by substituting $x = \varepsilon x'$, $y = \varepsilon y'$.

(b), (c). By symmetry consider $(0,1]$. Let $I_k := [2^{-k-1},2^{-k}]$, $k\ge0$, $a_k := 2^{k+1}\int_{I_k}g$, and
$$E_k := \iint_{I_k\times I_k}\frac{|g(x)-g(y)|^2}{|x-y|^{1+2\theta}}\,dx\,dy,\qquad E'_k :=
\iint_{I_k\times I_{k+1}}\frac{|g(x)-g(y)|^2}{|x-y|^{1+2\theta}}\,dx\,dy,$$
so $\sum_k(E_k+E'_k)\le2[g]_\theta^2$, the regions being disjoint. By Jensen's inequality,
$|g(x)-a_k|^2\le2^{k+1}\int_{I_k}|g(x)-g(y)|^2dy$, and $|x-y|\le2^{-k-1}$ on $I_k\times I_k$, so
$\int_{I_k}|g-a_k|^2\le2^{-2\theta(k+1)}E_k$. Likewise $|a_k-a_{k+1}|^2\le2^{2k+3}\iint_{I_k\times
I_{k+1}}|g(x)-g(y)|^2$, and $|x-y|\le2^{-k}$ there, so $|a_k-a_{k+1}|^2\le8\cdot2^{k(1-2\theta)}E'_k$. Hence
$$\int_0^1x^{-2\theta}|g|^2\le\sum_k2^{2\theta(k+1)}\cdot2\Big(\int_{I_k}|g-a_k|^2+2^{-k-1}|a_k|^2\Big)\le2\sum_kE_k+
2^{2\theta}\sum_kb_k^2,\qquad b_k := 2^{k(\theta-\frac12)}|a_k|.$$
For (b), $\theta<\frac12$: $|a_k|\le|a_0|+\sum_{j<k}|a_{j+1}-a_j|$, so with $q := 2^{\theta-\frac12}<1$ and $e_j :=
E'^{1/2}_j$, $b_k\le q^k|a_0|+\sqrt8\sum_{j<k}q^{k-j}e_j$. By Cauchy-Schwarz $(\sum_{j<k}q^{k-j}e_j)^2\le\frac
q{1-q}\sum_{j<k}q^{k-j}e_j^2$, and summing over $k$, $\sum_kb_k^2\le\frac2{1-q^2}|a_0|^2+16(\frac q{1-q})^2\sum_je_j^2$;
finally $|a_0|^2\le2\|g\|^2_{L^2(I_0)}$. For (c), $\theta>\frac12$: $\hat g\in L^1$ as $\int|\hat
g|\le\|\langle\xi\rangle^\theta\hat g\|\|\langle\xi\rangle^{-\theta}\|$, so $g$ is continuous; if $g(0) = 0$ then
$a_k\to0$, so $a_k = \sum_{j\ge k}(a_j-a_{j+1})$, and with $q := 2^{\frac12-\theta}<1$, $b_k\le\sqrt8\sum_{j\ge
k}q^{j-k}e_j$, whence $\sum_kb_k^2\le8(1-q)^{-2}\sum_je_j^2$ in the same way.

(d) For $\varphi\in\mathcal S$, $|\int\langle w,\varphi\rangle_{\mathcal H}|\le\||x|^\theta
w\|_{L^2}\||x|^{-\theta}\varphi\|_{L^2(-1,1)}\le C\||x|^\theta w\|_{L^2}\|\varphi\|_{H^\theta}$ by (b) and (a), and
$H^{-\theta}$ is the dual of $H^\theta$ for the $L^2$ pairing. $\square$

### 2.3 Taylor expansions at $\sigma = 0$

For $\gamma>-\frac12$ let $n_0(\gamma)$ be the number of $\ell\in\mathbb N_0$ with $\ell<\gamma-\frac12$.

**Lemma 2.4 (the content of [Hin26c] Corollary 13.3 and Lemma 13.4 that is used).** Let
$\gamma\in(0,\infty)\setminus(\frac12+\mathbb N_0)$, $n_0 := n_0(\gamma)$ and $g\in H^\gamma(\mathbb R;\mathcal H)$.
Then $g\in C^{n_0-1}$ (no condition if $n_0 = 0$), $|g^{(\ell)}(0)|\le C\|g\|_{H^\gamma}$ for $\ell<n_0$, and with
$P_g(\sigma) := \sum_{\ell<n_0}g^{(\ell)}(0)\sigma^\ell/\ell!$,
$$\||\sigma|^{-\gamma}(g-P_g)\|_{L^2(-1,1)}\le C\|g\|_{H^\gamma}.\tag{2.1}$$

*Proof.* For $\ell<\gamma-\frac12$, $\int|\tau|^\ell|\hat g(\tau)|\,d\tau\le\|\langle\tau\rangle^\gamma\hat
g\|\|\langle\tau\rangle^{\ell-\gamma}\|_{L^2}$, which gives the continuity of $g^{(\ell)}$ and the bound. Write $\gamma
= p+\theta$, $p\in\mathbb N_0$, $\theta\in[0,1)\setminus\{\frac12\}$.

If $\theta\in[0,\frac12)$, then $n_0 = p$. Put $f := g^{(p)}$, so $\|f\|_{H^\theta}\le\|g\|_{H^\gamma}$, and
$\||\sigma|^{-\theta}f\|_{L^2(-1,1)}\le C\|g\|_{H^\gamma}$: for $\theta = 0$ trivially, for $\theta>0$ by Lemma 2.3 (a),
(b).

If $\theta\in(\frac12,1)$, then $n_0 = p+1$. Put $f := g^{(p)}-g^{(p)}(0)$. With $\psi\in C_c^\infty((-2,2))$ equal to 1
on $[-1,1]$, $\psi f = \psi g^{(p)}-g^{(p)}(0)\psi\in H^\theta$ with norm $\le C\|g\|_{H^\gamma}$ and $(\psi f)(0) = 0$,
so $\||\sigma|^{-\theta}f\|_{L^2(-1,1)}\le C\|g\|_{H^\gamma}$ by Lemma 2.3 (c).

In both cases, if $p = 0$ then $g-P_g = f$ on $(-1,1)$ and (2.1) is the bound on $f$. If $p\ge1$, Taylor's formula with
integral remainder ($g^{(p-1)}$ is absolutely continuous, as $g\in H^p_{\mathrm{loc}}$) gives $g(\sigma)-P_g(\sigma) =
\sigma^p\int_0^1f(s\sigma)\frac{(1-s)^{p-1}}{(p-1)!}\,ds$; for $\theta>\frac12$ this uses $\int_0^\sigma
g^{(p)}(0)\frac{(\sigma-\tau)^{p-1}}{(p-1)!}d\tau = g^{(p)}(0)\frac{\sigma^p}{p!}$. By Minkowski's inequality and
$\||s\sigma|^{-\theta}f(s\sigma)\|_{L^2(-1,1;d\sigma)} = s^{-\frac12}\||\tau|^{-\theta}f\|_{L^2(-s,s)}$,
$$\||\sigma|^{-\gamma}(g-P_g)\|_{L^2(-1,1)}\le
\int_0^1s^{\theta-\frac12}\frac{(1-s)^{p-1}}{(p-1)!}\,ds\;\||\tau|^{-\theta}f\|_{L^2(-1,1)},$$
and $\theta-\frac12>-1$. $\square$

**Lemma 2.5 (Taylor coefficients under $\sigma^j(\sigma\partial_\sigma)^l$).** Let $n_0\ge1$, $J\in\{(-1,1),(0,1)\}$,
$R\in C^{n_0-1}(\bar J\cap(-1,1);\mathcal H)$ with $R^{(i)}(0) = 0$ for $i<n_0$ (one-sided derivatives if $J = (0,1)$),
and $j,l\in\mathbb N_0$. If the distribution $G := \sigma^j(\sigma\partial_\sigma)^lR$ on $J$ extends to an element of
$C^{n_0-1}(\bar J\cap(-1,1))$, then $G^{(i)}(0) = 0$ for $i<n_0$.

*Proof.* Fix $i<n_0$. The moments $m_{i'}(\varphi) := \int s^{i'}\varphi(s)\,ds$, $i'<n_0$, are linearly independent
functionals on $C_c^\infty((1,2))$, so there is $\varphi$ with $m_{i'}(\varphi) = \delta_{ii'}\,i!$. By Taylor's formula
with Peano remainder, $G(\varepsilon s) = \sum_{i'<n_0}G^{(i')}(0)(\varepsilon s)^{i'}/i'!+o(\varepsilon^{n_0-1})$
uniformly for $s\in[1,2]$, so $\varepsilon^{-1-i}\int G(\sigma)\varphi(\sigma/\varepsilon)\,d\sigma\to G^{(i)}(0)$ as
$\varepsilon\to0$. On the other hand, as $(\sigma\partial_\sigma)^T = -1-\sigma\partial_\sigma$ and
$\sigma\partial_\sigma$ commutes with dilations, $\int G\varphi(\sigma/\varepsilon)\,d\sigma = \int
R(\sigma)\,\varepsilon^j\Phi(\sigma/\varepsilon)\,d\sigma$ with $\Phi := (-1-s\partial_s)^l(s^j\varphi)\in
C_c^\infty((1,2))$, and this is $\varepsilon^{j+1}\int R(\varepsilon s)\Phi(s)\,ds =
\varepsilon^{j+1}o(\varepsilon^{n_0-1})$. So $\varepsilon^{-1-i}\int G\varphi(\sigma/\varepsilon)\,d\sigma =
o(\varepsilon^{j+n_0-1-i})\to0$. $\square$

**Lemma 2.6 (gluing).** Let $\gamma\in(-\frac12,\infty)\setminus(\frac12+\mathbb N_0)$ and $m := \lceil\gamma_+\rceil$.
Let $w$ be a function on $\mathbb R\setminus\{0\}$, vanishing for $|\sigma|\ge2$, with
$(\sigma\partial_\sigma)^lw\in|\sigma|^\gamma L^2(\pm(0,\infty);\mathcal H)$ on each side for $l\le m$, and $N(w) :=
\sum_{l\le m}\||\sigma|^{-\gamma}(\sigma\partial_\sigma)^lw\|_{L^2(\mathbb R\setminus0)}$. Then $w\in
L^1_{\mathrm{loc}}(\mathbb R)$ and, as a distribution on $\mathbb R$, $w\in H^\gamma(\mathbb R;\mathcal H)$ with
$\|w\|_{H^\gamma}\le CN(w)$.

*Proof.* $|\sigma|^\gamma L^2\subset L^1_{\mathrm{loc}}$ near 0 as $\gamma>-\frac12$. If $\gamma\in(-\frac12,0)$ this is
Lemma 2.3 (d) with $\theta = -\gamma$ (scaled to $[-2,2]$); if $\gamma = 0$ it is trivial. Let $\gamma>0$, $\gamma =
p+\theta$ as before. On each side $\partial_\sigma^lw = \sigma^{-l}\sum_{i\le l}a_{li}(\sigma\partial_\sigma)^iw$ with
constants $a_{li}$, so $\partial_\sigma^lw\in|\sigma|^{\gamma-l}L^2$ on each side for $l\le m$, with norm $\le CN(w)$.

*No distributions at 0.* For $\ell<\gamma-\frac12$ we have $\ell+1\le m$, and
$\partial^{\ell+1}w\in|\sigma|^{\gamma-\ell-1}L^2\subset L^1$ near 0 on each side ($\gamma-\ell-1>-\frac12$), so
$\partial^\ell w$ has one-sided limits at 0; as $\partial^\ell w\in|\sigma|^{\gamma-\ell}L^2$ with
$\gamma-\ell>\frac12$, they vanish. A function that is $W^{1,1}$ on each side of 0 near 0 and continuous at 0 has as
distributional derivative its pointwise derivative. Inductively the distributional derivatives $\partial^iw$, $i\le
n_0(\gamma)$, are the functions $\partial^iw$ on $\mathbb R\setminus0$. As $n_0(\gamma)\ge p$, $w\in H^p$ with norm $\le
CN(w)$ ($\gamma-i\ge0$ for $i\le p$, and the support is compact). If $\theta = 0$ we are done.

*The fractional part.* Let $\theta\in(0,1)$ and $G := \partial^pw$, so $G\in|\sigma|^\theta L^2$ and
$G'\in|\sigma|^{\theta-1}L^2$ on each side (as $m = p+1$). Let $A := \{(x,y):|x-y|\le|x|/2\}$; on $A$, $x$ and $y$ have
the same sign. With $J_k := [2^{-k},2^{-k+1}]$, $k\in\mathbb Z$, and $J_k^* := [2^{-k-1},3\cdot2^{-k}]$, for
$|h|\le2^{-k}$ we have $G(x+h)-G(x) = h\int_0^1G'(x+sh)\,ds$ and so $\int_{J_k}|G(x+h)-G(x)|^2dx\le
h^2\int_{J^*_k}|G'|^2$. Hence
$$\iint_{A\cap\{x>0\}}\frac{|G(x)-G(y)|^2}{|x-y|^{1+2\theta}}\le
\sum_k\int_{|h|\le2^{-k}}|h|^{1-2\theta}dh\int_{J^*_k}|G'|^2\le C\sum_k\int_{J^*_k}|x|^{2-2\theta}|G'|^2\le
C\||\sigma|^{1-\theta}G'\|^2,$$
as $\theta<1$, $|x|\sim2^{-k}$ on $J_k^*$ and the $J_k^*$ overlap boundedly; likewise for $x<0$. On the complement of
$A$, $|G(x)-G(y)|^2\le2|G(x)|^2+2|G(y)|^2$; $\int_{|x-y|>|x|/2}|x-y|^{-1-2\theta}dy = C|x|^{-2\theta}$, and for fixed
$y$ the set of $x$ with $|x-y|>|x|/2$ lies in $\{|x-y|\ge|y|/4\}$ (if $|x-y|<|y|/4$ then $|x|>\frac34|y|$ and
$|x-y|<\frac13|x|$), so $\int|x-y|^{-1-2\theta}dx\le C|y|^{-2\theta}$ there. So $[G]^2_\theta\le
C\||\sigma|^{-\theta}G\|^2+C\||\sigma|^{1-\theta}G'\|^2\le CN(w)^2$, $G\in H^\theta$ by Lemma 2.3 (a), and $w\in
H^{p+\theta}$, as $\langle\tau\rangle^{2\gamma}\le C(1+|\tau|^{2p}\langle\tau\rangle^{2\theta})$. $\square$

### 2.4 The lossy Fourier transform

Fix $\chi\in C_c^\infty((-2,2))$, even, equal to 1 on $[-1,1]$.

**Definition 2.7.** For $a\in(-1,\infty)\setminus\mathbb N_0$ and $k\in\mathbb N_0$, $X^{k,a}(\mathcal H)$ is the space
of pairs $(v_-,v_+)$ of functions on $(-\infty,0)$ and $(0,\infty)$ of the form $v_\pm = \chi P+w_\pm$, with $P$ a
polynomial of degree $<a$ with coefficients in $\mathcal H$, the same for both signs, and
$\sigma^j(\sigma\partial_\sigma)^lw_\pm\in|\sigma|^{a+\frac12}L^2(\pm(0,\infty);\mathcal H)$ for $j+l\le k$; the norm is
the sum of the norms of the coefficients of $P$ and of
$\||\sigma|^{-a-\frac12}\sigma^j(\sigma\partial_\sigma)^lw_\pm\|$.

The decomposition is unique: a polynomial of degree $<a$ that lies in $|\sigma|^{a+\frac12}L^2$ near 0 vanishes (its
lowest term would not). Its elements are locally integrable on $\mathbb R$ ($a>-1$) and of polynomial growth in $L^2$ at
infinity, so $v := v_-$ on $(-\infty,0)$, $v_+$ on $(0,\infty)$ is a tempered distribution.
$|\sigma|^{a+\frac12}L^2(d\sigma) = |\sigma|^aL^2(|\frac{d\sigma}\sigma|)$, so $X^{k,a}$ is the space of the source's
Corollary 13.7, with the Taylor polynomial carried by $v$ and the b-regularity by the remainder (section 7, (J2)).

**Proposition 2.8 ([Hin26c] Corollary 13.7).** Let $\beta\in(0,\infty)\setminus\mathbb N$, $\gamma := \beta-\frac12$,
$\ell_\pm(\beta) := \lceil\gamma_\pm\rceil$ and $k\in\mathbb N_0$.

(1) If $u\in H^{k+\ell_-(\beta),\beta}_b(\mathbb R;\mathcal H)$, then $(\mathcal Fu|_{(-\infty,0)},\mathcal
Fu|_{(0,\infty)})\in X^{k,\beta-1}$, with norm $\le C\|u\|$.

(2) If $(v_-,v_+)\in X^{k+\ell_+(\beta),\beta-1}$, then $\mathcal F^{-1}v\in H^{k,\beta}_b(\mathbb R;\mathcal H)$, with
norm $\le C\|(v_-,v_+)\|$.

*Proof.* (1) Let $v := \mathcal Fu$ and $F_{jl} := \sigma^j(\sigma\partial_\sigma)^lv$; by Lemma 2.2, $F_{jl}\in
H^\gamma$ for $j+l\le k+\ell_-$.

*Case $\gamma>0$*, so $\ell_- = 0$. Let $n_0 := n_0(\gamma)$ and $P := P_v$ (Lemma 2.4), of degree $<n_0$, that is
$<\gamma-\frac12 = \beta-1$. Fix $j+l\le k$. If $n_0\ge1$, $R := v-P\in C^{n_0-1}$ with $R^{(i)}(0) = 0$ for $i<n_0$,
and $\sigma^j(\sigma\partial_\sigma)^lR = F_{jl}-\sigma^j(\sigma\partial_\sigma)^lP$ is $C^{n_0-1}$ (Lemma 2.4 for
$F_{jl}$); by Lemma 2.5 its derivatives of order $<n_0$ at 0 vanish, so $P_{F_{jl}}$ is the part of
$\sigma^j(\sigma\partial_\sigma)^lP$ of degree $<n_0$. On $(-1,1)\setminus0$, where $\chi = 1$,
$$\sigma^j(\sigma\partial_\sigma)^l(v-\chi P) =
(F_{jl}-P_{F_{jl}})-\big(\sigma^j(\sigma\partial_\sigma)^lP-P_{F_{jl}}\big),$$
the first term in $|\sigma|^\gamma L^2(-1,1)$ by (2.1), the second a polynomial whose terms have degree $\ge
n_0>\gamma-\frac12$, hence also in $|\sigma|^\gamma L^2(-1,1)$; the bounds are by $\|F_{jl}\|_{H^\gamma}$ and the
coefficients of $P$, so by $C\|u\|$. If $n_0 = 0$, $P = 0$ and this is (2.1) for $F_{jl}$. On $|\sigma|\ge1$,
$\sigma^j(\sigma\partial_\sigma)^l(v-\chi P) = F_{jl}$ minus a smooth function supported in $|\sigma|\le2$, and
$F_{jl}\in L^2\subset|\sigma|^\gamma L^2$ there. So $w_\pm := (v-\chi P)|_{\pm(0,\infty)}$ satisfy Definition 2.7 with
$a = \beta-1$ ($|\sigma|^{a+\frac12} = |\sigma|^\gamma$).

*Case $\gamma = 0$*: $P = 0$ ($a = -\frac12$), and $F_{jl}\in L^2$.

*Case $\gamma\in(-\frac12,0)$*, so $\ell_- = 1$ and $P = 0$. Fix $j+l\le k$ and let $F := F_{jl}$, $G := \sigma F =
F_{j+1,l}\in H^\gamma$. Then $\partial_\sigma G = (1+j)F+F_{j,l+1}\in H^\gamma$, so $G\in H^{\gamma+1}$ with norm $\le
C\|u\|$. By Lemma 2.4 at $\gamma+1\in(\frac12,1)$, $G$ is continuous and $G-G(0)\in|\sigma|^{\gamma+1}L^2(-1,1)$. We
show $G(0) = 0$. Let $\psi\in C_c^\infty((1,2))$ with $\int\psi(s)\frac{ds}s = 1$ and $\psi_\varepsilon :=
\psi(\cdot/\varepsilon)$. On $(0,\infty)$, $F = G/\sigma$, so $\int F\psi_\varepsilon =
G(0)+\int(G-G(0))\psi_\varepsilon\frac{d\sigma}\sigma$, and the last term is at most
$\||\sigma|^{-\gamma-1}(G-G(0))\|\||\sigma|^\gamma\psi_\varepsilon\|_{L^2} = O(\varepsilon^{\gamma+\frac12})\to0$. But
$|\int F\psi_\varepsilon|\le\|F\|_{H^\gamma}\|\psi_\varepsilon\|_{H^{-\gamma}}$, and by Lemma 2.3 (a) with $\theta =
-\gamma$, $\|\psi_\varepsilon\|^2_{H^{-\gamma}}\le
C(\varepsilon\|\psi\|^2+\varepsilon^{1+2\gamma}[\psi]^2_{-\gamma})\to0$. So $G(0) = 0$, and on $(-1,1)\setminus0$, $F =
G/\sigma\in|\sigma|^\gamma L^2$; on $|\sigma|\ge1$, $F = G/\sigma\in|\sigma|^{-1}L^2\subset|\sigma|^\gamma L^2$.

(2) Write $v = \chi P+w$, $w := w_\pm$ on $\pm(0,\infty)$. $\sigma^p(\sigma\partial_\sigma)^q(\chi P)\in\mathcal
S\subset H^\gamma$. *Distributional derivatives.* If $f$ is a function on $\mathbb R\setminus0$ with $f$ and
$\sigma\partial_\sigma f$ integrable near 0 on both sides, then $\sigma f$ is absolutely continuous on each side near 0,
with one-sided limits at 0 that vanish (else $|f|\ge c/|\sigma|$ near 0); so $\sigma f$ is continuous, its
distributional derivative is $f+\sigma\partial_\sigma f$, and the distributional $\sigma\partial_\sigma f =
\partial_\sigma(\sigma f)-f$ is the function $\sigma\partial_\sigma f$. Applied repeatedly (each
$\sigma^{j}(\sigma\partial_\sigma)^lw$ lies in $|\sigma|^{a+\frac12}L^2\subset L^1_{\mathrm{loc}}$, $a+\frac12 =
\gamma>-\frac12$), $W := \sigma^p(\sigma\partial_\sigma)^qw$, $p+q\le k$, is the same whether computed on $\mathbb R$ or
on each side. As $\sigma^j(\sigma\partial_\sigma)^l\sigma^p(\sigma\partial_\sigma)^q =
\sigma^{j+p}(\sigma\partial_\sigma+p)^l(\sigma\partial_\sigma)^q$, $\sigma^j(\sigma\partial_\sigma)^lW\in|\sigma|^\gamma
L^2$ on each side for $j+l\le\ell_+$, with norm $\le C\|(v_-,v_+)\|$. Let $\psi\in C_c^\infty((-2,2))$ equal 1 on
$[-1,1]$. Then $(\sigma\partial_\sigma)^l(\psi W)\in|\sigma|^\gamma L^2$ for $l\le m := \lceil\gamma_+\rceil = \ell_+$,
so $\psi W\in H^\gamma$ by Lemma 2.6. If $\gamma\le0$, $(1-\psi)W\in|\sigma|^\gamma L^2\subset L^2\subset H^\gamma$ on
$|\sigma|\ge1$. If $\gamma>0$: for $i\le m$, $\partial^i_\sigma W = \sigma^{-i}\sum_{i'\le
i}a_{ii'}(\sigma\partial_\sigma)^{i'}W$, and $\sigma^{m-i'}(\sigma\partial_\sigma)^{i'}W\in|\sigma|^\gamma L^2$ gives
$\sigma^{-i}(\sigma\partial_\sigma)^{i'}W\in|\sigma|^{\gamma-m+i'-i}L^2\subset L^2$ on $|\sigma|\ge1$, as $\gamma\le m$
and $i'\le i$; so $(1-\psi)W\in H^m\subset H^\gamma$. Hence $\sigma^p(\sigma\partial_\sigma)^qv\in H^\gamma$ for $p+q\le
k$, and Lemma 2.2 gives the claim. $\square$

*Remark 2.9 (what of [Hin26c] 13.1.1 is not carried as stated).* Lemma 13.2 (supported and extendible spaces) and Lemma
13.6 (the lossless transform) are not used later and are not carried; Lemma 2.3 (d) and Lemma 2.6 contain what the proof
of Proposition 2.8 needs of them. Lemma 13.4 is carried only in the form of Lemma 2.4, for the weight at $\sigma = 0$;
with the weight at $\sigma = \infty$ as well, which the source insists on after Corollary 13.5, it fails (section 7,
(J1)).

## 3. The Fourier transform on the resolved product spaces

### 3.1 The spaces

$X := \mathbb R^4$, $\bar X$ its radial compactification, $\rho := \langle x\rangle^{-1}$ and $\mu_X := |dx|/\langle
x\rangle^4$, a b-density. $H^{k,\gamma}_b(X;\mathcal H)$ is the space of $u$ with $\rho^{-\gamma}(\langle
x\rangle\partial_x)^\alpha u\in L^2(\mu_X)$ for $|\alpha|\le k$; the fields $\langle x\rangle\partial_{x^i}$ span
$\mathcal V_b(\bar X)$ (I.A section 4.6).

$M := [\overline{\mathbb R}_{t_*}\times\bar X;\partial\overline{\mathbb R}\times\partial\bar X]$ ([Hin26c] (13.9)), with
the defining functions of $\mathscr I$, $\iota$ and $K$ ([Hin26c] (13.10))
$$\rho_I := \frac{\langle t_*\rangle}{\langle t_*\rangle+\langle x\rangle},\qquad\rho_\iota :=
\frac{\langle t_*\rangle+\langle x\rangle}{\langle t_*\rangle\langle x\rangle},\qquad\rho_K :=
\frac{\langle x\rangle}{\langle t_*\rangle+\langle x\rangle},\qquad\rho_I\rho_\iota = \langle x\rangle^{-1},\quad
\rho_\iota\rho_K = \langle t_*\rangle^{-1},\tag{3.1}$$
and the b-density $\mu_M := |dt_*/\langle t_*\rangle|\,\mu_X$. For weights $\beta = (\beta_I,\beta_\iota,\beta_K)$ and
$w_\beta := \rho_I^{\beta_I}\rho_\iota^{\beta_\iota}\rho_K^{\beta_K}$, $H^{k,\beta}_b(M;\mathcal H)$ is the space of $u$
with $w_\beta^{-1}(\langle t_*\rangle\partial_{t_*})^j(\langle x\rangle\partial_x)^\alpha u\in L^2(\mu_M;\mathcal H)$
for $j+|\alpha|\le k$. These fields are b-vector fields on $M$ and span $\mathcal V_b(M)$, the blow-up of a
codimension-two corner being a b-blow-up, and the derivatives of $\log\rho_I$, $\log\rho_\iota$, $\log\rho_K$ along them
are bounded with all their derivatives (for instance $\langle t_*\rangle\partial_{t_*}\log(\langle t_*\rangle+\langle
x\rangle) = t_*/(\langle t_*\rangle+\langle x\rangle)$), so weights and derivatives may be taken in either order, with
equivalent norms; this is the source's (13.11).

For $c\in(0,1]$, $X^\pm_{\mathrm{sc}\text{-}b} := [\pm[0,c]_\sigma\times\bar X;\{0\}\times\partial\bar X]$ ([Hin26c]
(13.12); $c = 1$ there), with the defining functions of the faces scf, tf, zf ([Hin26c] (13.13))
$$\rho_{\mathrm{scf}} := \frac\rho{\rho+|\sigma|},\qquad\rho_{\mathrm{tf}} := |\sigma|+\rho,\qquad
\rho_{\mathrm{zf}} := \frac{|\sigma|}{\rho+|\sigma|},\qquad\rho_{\mathrm{scf}}\rho_{\mathrm{tf}} = \rho,\quad
\rho_{\mathrm{tf}}\rho_{\mathrm{zf}} = |\sigma|,\tag{3.2}$$
and the b-density $|d\sigma/\sigma|\,\mu_X$. For $\gamma =
(\gamma_{\mathrm{scf}},\gamma_{\mathrm{tf}},\gamma_{\mathrm{zf}})$,
$H^{k,\gamma}_b(X^\pm_{\mathrm{sc}\text{-}b};\mathcal H)$ is the space of $u$ on $\pm(0,c]\times X$ with
$w_\gamma^{-1}(\sigma\partial_\sigma)^j(\langle x\rangle\partial_x)^\alpha u\in L^2(|d\sigma/\sigma|\mu_X)$ for
$j+|\alpha|\le k$ (the source's (13.14); the face at $|\sigma| = c$ is an extendible end, at which nothing is asked).
Let $\hat r := |\sigma|\langle x\rangle$, a defining function of zf near zf, and $\chi_{\mathrm{zf}} := \chi_1(\hat r)$
with $\chi_1\in C^\infty([0,\infty))$ equal to 1 on $[0,\frac18]$ and to 0 on $[\frac14,\infty)$; $\chi_{\mathrm{zf}}$
and its derivatives along $\sigma\partial_\sigma$, $\langle x\rangle\partial_x$ are bounded ($\sigma\partial_\sigma\hat
r = \hat r$, $\langle x\rangle\partial_x\hat r = \hat r\,x/\langle x\rangle$). For
$\gamma_{\mathrm{zf}}\in(-1,\infty)\setminus\mathbb N_0$ let ([Hin26c] (13.15) with $\zeta = 0$)
$$H^{k,(\gamma_{\mathrm{scf}},\gamma_{\mathrm{tf}},((0,0),\gamma_{\mathrm{zf}}))}_b(X^\pm_{\mathrm{sc}\text{-}b}) :=
\Big\{\chi_{\mathrm{zf}}\sum_{\ell\in\mathbb N_0,\ \ell<\gamma_{\mathrm{zf}}}\hat r^\ell v_\ell+\tilde u:v_\ell\in
H^{k,\gamma_{\mathrm{tf}}}_b(X),\ \tilde u\in H^{k,\gamma}_b(X^\pm_{\mathrm{sc}\text{-}b})\Big\},$$
normed by $\sum\|v_\ell\|+\|\tilde u\|$; the decomposition is unique (Lemma 3.1 (c) below and the uniqueness after
Definition 2.7). As $\hat r^\ell v_\ell = (\pm\sigma)^\ell\langle x\rangle^\ell v_\ell(x)$ on the side $\pm$, we call
$c^\pm_\ell := (\pm1)^\ell\langle x\rangle^\ell v^\pm_\ell$ the $\sigma$-Taylor coefficients. The source writes
$\rho_{\mathrm{zf}}^\ell u_\ell(x)$ with $\rho_{\mathrm{zf}} = \hat r/(1+\hat r)$; Taylor expansion of $(1+\hat
r)^{-\ell}$ at $\hat r = 0$ turns one form into the other, the remainders lying in $\tilde u$'s space.

At high frequencies ([Hin26c] (13.16)): for $c>0$, $H^{k,\beta,\gamma}_{b+}(\pm[c,\infty)\times X;\mathcal H)$ is the
space of $v$ with $|\sigma|^\gamma\sigma^j(\sigma\partial_\sigma)^lv\in
L^2(\pm[c,\infty),|d\sigma/\sigma|;H^{k-j-l,\beta}_b(X;\mathcal H))$ for $j+l\le k$; the powers of $\sigma$ stand on the
same footing as the b-derivatives, and $H^{k+N,\beta,\gamma}_{b+}\subset H^{k,\beta,\gamma+N}_{b+}$ for $N\in\mathbb
N_0$.

**Lemma 3.1 ([Hin26c] Lemma 13.8).** For $k\in\mathbb N_0$ and $\beta,\gamma\in\mathbb R$, with equivalent norms,

(a) $H^{k,(\gamma,\beta+\gamma,\beta)}_b(M;\mathcal H) = \bigcap_{j=0}^kH^{j,\beta}_b(\mathbb
R;H^{k-j,\gamma}_b(X;\mathcal H))$;

(b) $H^{k,(\gamma,\beta+\gamma,\beta)}_b(X^\pm_{\mathrm{sc}\text{-}b};\mathcal H) =
\bigcap_{j=0}^kH^{j,\beta}_b(\pm(0,c];H^{k-j,\gamma}_b(X;\mathcal H))$, where $H^{j,\beta}_b(\pm(0,c];\mathcal H)$ is
the space of $v$ with $|\sigma|^{-\beta}(\sigma\partial_\sigma)^iv\in L^2(|d\sigma/\sigma|;\mathcal H)$, $i\le j$;

(c) for $u$ supported in $\{\hat r\le\frac12\}$, in the coordinates $(\hat r,x)\in(0,\frac12]\times X$,
$\|u\|_{H^{k,\gamma}_b(X^\pm_{\mathrm{sc}\text{-}b})}$ is equivalent to the norm of $\bigcap_{j\le
k}H^{j,\gamma_{\mathrm{zf}}}_b((0,\frac12]_{\hat r};H^{k-j,\gamma_{\mathrm{tf}}}_b(X))$, the order
$\gamma_{\mathrm{scf}}$ playing no role.

*Proof.* (a) By (3.1), $\rho_I^\gamma\rho_\iota^{\beta+\gamma}\rho_K^\beta = \langle t_*\rangle^{-\beta}\langle
x\rangle^{-\gamma}$, a product. The norm on the left is equivalent to $\sum_{j+|\alpha|\le k}\|\langle
t_*\rangle^\beta\langle x\rangle^\gamma(\langle t_*\rangle\partial_{t_*})^j(\langle x\rangle\partial_x)^\alpha
u\|_{L^2(\mu_M)}$, the two families of fields acting on different variables, and by Fubini this is the norm on the right
(with $\langle t\rangle^\beta L^2(dt/\langle t\rangle) = \langle t\rangle^{\beta-\frac12}L^2(dt)$ and the equivalence
after Definition 2.1). (b) Likewise, with
$\rho_{\mathrm{scf}}^\gamma\rho_{\mathrm{tf}}^{\beta+\gamma}\rho_{\mathrm{zf}}^\beta = \rho^\gamma|\sigma|^\beta$ by
(3.2). (c) On $\{\hat r\le\frac12\}$, $\rho_{\mathrm{scf}} = (1+\hat r)^{-1}\in[\frac23,1]$, $\rho_{\mathrm{tf}} =
\rho(1+\hat r)$ and $\rho_{\mathrm{zf}} = \hat r/(1+\hat r)$; at fixed $x$, $\sigma\partial_\sigma = \hat
r\partial_{\hat r}$ and $|d\sigma/\sigma| = |d\hat r/\hat r|$; and $\langle x\rangle\partial_x$ at fixed $\sigma$ is
$\langle x\rangle\partial_x$ at fixed $\hat r$ plus $\frac x{\langle x\rangle}\hat r\partial_{\hat r}$. $\square$

### 3.2 A b-ordinary differential equation

**Lemma 3.2.** Let $\mathcal H$ be a Hilbert space, $d,c\in\mathbb R$, $c\ne d$, and let $W\in
L^2_{\mathrm{loc}}((0,1);\mathcal H)$ satisfy $(s\partial_s-d)W = h$ on $(0,1)$ with $h\in s^cL^2((0,1),|ds/s|;\mathcal
H)$. Let $\chi\in C^\infty([0,1))$ equal 1 on $[0,\frac14]$ and 0 on $[\frac12,1)$. Write $\|\cdot\|$ for the norm of
$L^2((0,1),|ds/s|;\mathcal H)$ and $\|\cdot\|'$ for that over $(\frac14,\frac12)$.

(a) If $c>d$, then $L := \lim_{s\to0}s^{-d}W(s)$ exists in $\mathcal H$, $|L|\le C(\|W\|'+\|s^{-c}h\|)$, and $W_1 :=
\chi(W-s^dL)$ satisfies $\|s^{-c}W_1\|\le C(\|W\|'+\|s^{-c}h\|)$.

(b) If $c<d$, then $W_1 := \chi W$ satisfies $\|s^{-c}W_1\|\le C(\|W\|'+\|s^{-c}h\|)$.

(c) If moreover $(s\partial_s)^ih\in s^cL^2$ for $i\le k$, then $\|s^{-c}(s\partial_s)^iW_1\|\le C\sum_{i'\le
i}(\|(s\partial_s)^{i'}W\|'+\|s^{-c}(s\partial_s)^{i'}h\|)$ in both cases.

*Proof.* In $\tau := \log s\in(-\infty,0)$, $|ds/s| = d\tau$, and $s\partial_s(s^{-d}W) = s^{-d}h$ says
$\partial_\tau(e^{-d\tau}W) = e^{-d\tau}h$ in distributions, so $e^{-d\tau}W$ is absolutely continuous. (a) $e^{-d\tau}h
= e^{(c-d)\tau}e^{-c\tau}h$ is integrable on $(-\infty,\tau_0)$ by Cauchy-Schwarz, as $c>d$, so $L$ exists and
$e^{-d\tau}W(\tau) = L+\int_{-\infty}^\tau e^{-d\tau'}h(\tau')\,d\tau'$. Averaging this over
$\tau\in(\log\frac14,\log\frac12)$ bounds $|L|$. And $e^{-c\tau}(W-e^{d\tau}L) = \int_{-\infty}^\tau
e^{-(c-d)(\tau-\tau')}e^{-c\tau'}h(\tau')\,d\tau'$, a convolution with $e^{-(c-d)\tau}1_{\tau>0}$, whose $L^1$ norm is
$(c-d)^{-1}$; Young's inequality bounds it in $L^2(d\tau)$, and multiplying by $\chi$ costs nothing. (b)
$(s\partial_s-d)(\chi W) = \chi h+(s\partial_s\chi)W =: \tilde h$, with $\|s^{-c}\tilde h\|\le\|s^{-c}h\|+C\|W\|'$.
$\chi W$ vanishes near $\tau = \log\frac12$, so $e^{-d\tau}\chi W(\tau) = -\int_\tau^{\log\frac12}e^{-d\tau'}\tilde
h(\tau')\,d\tau'$, and $e^{-c\tau}\chi W$ is the convolution of $e^{-c\tau'}\tilde h$ with $-e^{(d-c)\tau}1_{\tau<0}$,
of $L^1$ norm $(d-c)^{-1}$. (c) $W_1$ satisfies $(s\partial_s-d)W_1 = \chi h+(s\partial_s\chi)(W-s^dL)$ in case (a) (as
$(s\partial_s-d)s^d = 0$), resp. $\tilde h$ in case (b), so $s\partial_sW_1 = dW_1+(\ldots)$, and induction on $i$; the
derivatives of $W$ on $(\frac14,\frac12)$ enter through the terms with $s\partial_s\chi$. $\square$

### 3.3 The Fourier transform of b-Sobolev functions

**Proposition 3.3 ([Hin26c] Proposition 13.9).** Let $\beta = (\beta_I,\beta_\iota,\beta_K)$ and $u\in
H^{k+\ell,\beta}_b(M;\mathcal H)$, with $\ell$ as below.

(1) (*Low energies.*) Let $\beta_K\in(0,\infty)\setminus\mathbb N$, $\epsilon\in(0,1)$ and
$\beta_I\ge\beta_\iota-\min(\beta_K,1-\epsilon)$, and $\ell = 1$. Then
$$(\mathcal Fu)|_{\sigma\in\pm(0,1]}\in H^{k,(\min(\beta_I,\beta_\iota)-\epsilon,\ \beta_\iota-1,
\ ((0,0),\beta_K-1))}_b(X^\pm_{\mathrm{sc}\text{-}b};\mathcal H),$$
with norm $\le C\|u\|$, and the $\sigma$-Taylor coefficients $c^\pm_\ell$, $\ell<\beta_K-1$, of the two signs agree.

(2) (*High energies.*) Let $\ell := \lceil(\frac12-\min(\beta_K,\beta_\iota-\beta_I))_+\rceil$. Then $(\mathcal
Fu)|_{\sigma\in\pm[\frac12,\infty)}\in H^{k,\beta_I,0}_{b+}(\pm[\frac12,\infty)\times X;\mathcal H)$, with norm $\le
C\|u\|$.

Here $\mathcal F$ acts in $t_*$; by Lemma 3.1 (a) and Lemma 2.2, $u$ is a tempered distribution in $t_*$ with values in
$H^{k,\gamma}_b(X)$ for suitable $\gamma$.

*Proof.* Lowering a weight is a bounded inclusion, as $\rho_I,\rho_K\le1$ and $\rho_\iota\le2$; and two memberships with
the same tf-weight combine: if $v$ lies in $H^{k,(a,b,c)}_b$ and in $H^{k,(a',b,c')}_b$ on
$X^\pm_{\mathrm{sc}\text{-}b}$, then $v\in H^{k,(a,b,c')}_b$, by the partition $1 = \chi_1(2\hat r)+(1-\chi_1(2\hat
r))$, whose first term is supported away from scf and the second away from zf (and likewise on $M$, with a partition
into neighbourhoods of $\mathscr I$ and of $K$). This is used twice below and in Proposition 3.5.

(1), *the case $\beta_K\in(0,1)$.* For $\eta\ge0$ with $\beta_K-\eta>0$ and $\beta_I\ge\beta_\iota-\beta_K+\eta$, $u\in
H^{k+1,(\beta_\iota-\beta_K+\eta,\beta_\iota,\beta_K-\eta)}_b(M)$, so by Lemma 3.1 (a) $u\in\bigcap_{j\le
k}H^{j+1,\beta_K-\eta}_b(\mathbb R;\mathcal H_j)$ with $\mathcal H_j := H^{k-j,\beta_\iota-\beta_K+\eta}_b(X)$. As
$\beta_K-\eta\in(0,1)$, $\ell_-(\beta_K-\eta)\le1$, and Proposition 2.8 (1) (with $\mathcal H_j$-values; no Taylor
terms, as $\beta_K-\eta-1<0$) gives $(\sigma\partial_\sigma)^i\mathcal
Fu\in|\sigma|^{\beta_K-\eta-1}L^2(|d\sigma/\sigma|;\mathcal H_j)$ on each side, $i\le j$. Restricted to $|\sigma|\le1$
this is, by Lemma 3.1 (b),
$$\mathcal Fu\in H^{k,(\beta_\iota-\beta_K+\eta,\ \beta_\iota-1,\ \beta_K-\eta-1)}_b(X^\pm_{\mathrm{sc}\text{-}b}).$$
With $\eta = 0$ the zf-weight is $\beta_K-1$; with $\eta := \max(0,\min(\beta_K,\beta_I-\beta_\iota+\beta_K)-\epsilon)$
the scf-weight is $\ge\min(\beta_I,\beta_\iota)-\epsilon$ (if the maximum is 0 then
$\min(\beta_K,\beta_I-\beta_\iota+\beta_K)\le\epsilon$, and $\beta_\iota-\beta_K\ge\min(\beta_I,\beta_\iota)-\epsilon$).
Combining the two gives the claim; the matching statement is empty.

(1), *the case $\beta_K\in(b,b+1)$, $b\in\mathbb N$.* (i) Applying the first case to $u\in
H^{k+1,(\beta_I,\beta_\iota,1-\epsilon)}_b(M)$ (its hypothesis $\beta_I\ge\beta_\iota-(1-\epsilon)$ is ours, as
$\min(\beta_K,1-\epsilon) = 1-\epsilon$) gives $V := \mathcal Fu\in
H^{k,(\min(\beta_I,\beta_\iota)-\epsilon,\beta_\iota-1,-\epsilon)}_b(X^\pm_{\mathrm{sc}\text{-}b})$. (ii) $t_*^bu\in
H^{k+1,(\beta_I,\beta_\iota-b,\beta_K-b)}_b(M)$, as $t_*^b = (t_*/\langle t_*\rangle)^b(\rho_\iota\rho_K)^{-b}$, and
$\beta_K-b\in(0,1)$ with $\beta_I\ge\beta_\iota-1+\epsilon\ge(\beta_\iota-b)-\min(\beta_K-b,1-\epsilon)$; so by the
first case $\mathcal F(t_*^bu)\in H^{k,(a,\beta_\iota-b-1,\beta_K-b-1)}_b$ for some $a$. As $\partial_\sigma\mathcal Fu
= i\mathcal F(t_*u)$ and $|\sigma|^b = \rho_{\mathrm{tf}}^b\rho_{\mathrm{zf}}^b$,
$$h := \sigma^b\partial_\sigma^bV = (i\sigma)^b\mathcal F(t_*^bu)\in
H^{k,(a,\beta_\iota-1,\beta_K-1)}_b(X^\pm_{\mathrm{sc}\text{-}b}).\tag{3.3}$$
(iii) On $Z := \{\hat r<\frac12\}$ use the coordinates $(\hat r,x)$ of Lemma 3.1 (c), in which $\sigma = \pm\hat
r/\langle x\rangle$, so $\sigma^b\partial_\sigma^b = \hat r^b\partial_{\hat r}^b$ at fixed $x$. By (i), (3.3) and Lemma
3.1 (c), with $\mathcal H_j := H^{k-j,\beta_\iota-1}_b(X)$, $V\in\bigcap_jH^{j,-\epsilon}_b((0,\frac12)_{\hat
r};\mathcal H_j)$ and $h\in\bigcap_jH^{j,\beta_K-1}_b((0,\frac12);\mathcal H_j)$. As $\beta_K-1-b>-1$, $\hat
r^{-b}h\in\hat r^{\beta_K-1-b}L^2(|d\hat r/\hat r|;\mathcal H_0)$ is integrable near $\hat r = 0$. Let
$$R(\hat r) := \frac1{(b-1)!}\int_0^{\hat r}\tau^{-b}h(\tau)(\hat r-\tau)^{b-1}\,d\tau =
\frac1{(b-1)!}\int_0^1s^{-b}h(s\hat r)(1-s)^{b-1}\,ds,$$
the $b$-fold iterated integral of $\hat r^{-b}h$ from 0, so that $\partial^b_{\hat r}R = \hat r^{-b}h = \partial^b_{\hat
r}V$ on $(0,\frac12)$. Dilations $\hat r\mapsto s\hat r$ commute with $\hat r\partial_{\hat r}$ and with $\langle
x\rangle\partial_x$ at fixed $\hat r$, and preserve $|d\hat r/\hat r|$, so by Minkowski's inequality
$$\|\hat r^{1-\beta_K}(\hat r\partial_{\hat r})^jR\|_{L^2(\mathcal H_j)}\le
\frac1{(b-1)!}\int_0^1s^{\beta_K-1-b}(1-s)^{b-1}\,ds\;
\|\hat r^{1-\beta_K}(\hat r\partial_{\hat r})^jh\|_{L^2(\mathcal H_j)},$$
finite as $\beta_K-1-b>-1$. $V-R$ is an $\mathcal H_0$-valued distribution on $(0,\frac12)$ with $\partial^b_{\hat
r}(V-R) = 0$, hence a polynomial $\sum_{d<b}\hat r^dv_d$; each $v_d$ is a fixed linear combination of the averages
$\int(V-R)\hat r^{d'}\varphi(\hat r)\,d\hat r$, $d'<b$, with $\varphi\in C_c^\infty((\frac14,\frac12))$ (the monomials
being linearly independent there), so $v_d\in\mathcal H_0 = H^{k,\beta_\iota-1}_b(X)$ with norm $\le C(\|V\|+\|h\|)$. So
on $Z$, $V = \sum_{d<b}\hat r^dv_d+R$ with $R\in\hat r^{\beta_K-1}$ and the full b-regularity $k$, and the $d<b$ are
exactly the $\ell<\beta_K-1$. With $\chi_{\mathrm{zf}}$ (supported in $\{\hat r\le\frac14\}$), $V =
\chi_{\mathrm{zf}}\sum_d\hat r^dv_d+\tilde V$, where $\tilde V = \chi_{\mathrm{zf}}R+(1-\chi_{\mathrm{zf}})V$; the first
term has tf-weight $\beta_\iota-1$ and zf-weight $\beta_K-1$ and is supported away from scf, and the second is supported
away from zf, where (i) gives the scf-weight $\min(\beta_I,\beta_\iota)-\epsilon$ and the tf-weight $\beta_\iota-1$.
This proves the first claim.

*Matching.* On $\{|x|<R\}$, $\rho_K\sim\langle t_*\rangle^{-1}$ and the weights at $\mathscr I$, $\iota$ are irrelevant,
so $u\in H^{k+1,\beta_K}_b(\mathbb R;L^2(\{|x|<R\}))$, and $\mathcal Fu\in H^{\beta_K-\frac12}(\mathbb
R;L^2(\{|x|<R\}))$ by Lemma 2.2. As $\beta_K-\frac12>\frac12$, Lemma 2.4 makes $\mathcal Fu$ of class $C^\ell$ in
$\sigma$ across $\sigma = 0$ for $\ell<\beta_K-1$, with $\mathcal Fu-P_{\mathcal Fu}\in|\sigma|^{\beta_K-\frac12}L^2$
near 0. On the other hand, on $\{|x|<R\}$ the expansion gives $\mathcal Fu =
\sum_{\ell<\beta_K-1}c^\pm_\ell\sigma^\ell+O_{L^2}(|\sigma|^{\beta_K-\frac12})$ on each side, as $\hat
r^{\beta_K-1}L^2(|d\hat r/\hat r|) = |\sigma|^{\beta_K-\frac12}L^2(d\sigma)$ locally in $x$. A polynomial of degree
$<\beta_K-1$ in $|\sigma|^{\beta_K-\frac12}L^2$ near 0 vanishes, so $c^\pm_\ell = \partial^\ell_\sigma\mathcal
Fu(0)/\ell!$ on $\{|x|<R\}$ for both signs; $R$ is arbitrary.

(2) Let $\beta'_K := \min(\beta_K,\beta_\iota-\beta_I)$. Then $u\in H^{k+\ell,(\beta_I,\beta_I+\beta'_K,\beta'_K)}_b(M)
= \bigcap_jH^{j,\beta'_K}_b(\mathbb R;H^{k+\ell-j,\beta_I}_b(X))$, so by Lemma 2.2 $F_{pq} :=
\sigma^p(\sigma\partial_\sigma)^q\mathcal Fu\in H^{\beta'_K-\frac12}(\mathbb R;H^{k+\ell-p-q,\beta_I}_b(X))$ for $p+q\le
k+\ell$. Let $\psi\in C^\infty(\mathbb R)$ vanish on $[-\frac14,\frac14]$ and equal 1 outside $(-\frac12,\frac12)$. For
$p+q\le k$ and $i\le\ell$, $\partial^i_\sigma(\psi F_{pq})$ is a combination of
$\psi_{i'}(\sigma)\,\sigma^{-i'}(\sigma\partial_\sigma)^{i'}F_{pq}$, $i'\le i$, with $\psi_{i'}$ smooth, supported in
$|\sigma|\ge\frac14$ and bounded with all derivatives, multiplication by which is bounded on $H^{\beta'_K-\frac12}$ (I.C
(K1) (i), or Peetre's inequality); $\sigma^{-i'}$ is such a multiplier on $|\sigma|\ge\frac14$. So $\psi F_{pq}\in
H^{\beta'_K-\frac12+\ell}\subset L^2$, as $\ell\ge\frac12-\beta'_K$, with values in $H^{k-p-q,\beta_I}_b(X)$ (the
b-derivatives $(\sigma\partial_\sigma)^{i'}$ used, $i'\le\ell$, cost $\ell$ of the $X$-regularity). On
$\pm[\frac12,\infty)$, $L^2(d\sigma)\subset L^2(|d\sigma/\sigma|)$, which is the claim. $\square$

**Lemma 3.4 ([Hin26c] Lemma 13.10).** Let $\gamma\in\mathbb R$ and $v_0\in H^{k,\gamma}_b(X;\mathcal H)$. Then $v(t_*,x)
:= v_0(x)$ lies in $H^{k,(\gamma-\epsilon,\gamma,-\epsilon)}_b(M;\mathcal H)$ for every $\epsilon>0$.

*Proof.* $\langle t_*\rangle\partial_{t_*}v = 0$, and the $\langle x\rangle\partial_x$-derivatives fall on $v_0$, so it
suffices to show $\|w_\beta^{-1}f\|_{L^2(\mu_M)}\le C_\epsilon\|\rho^{-\gamma}f\|_{L^2(\mu_X)}$ for $t_*$-independent
$f$, $\beta = (\gamma-\epsilon,\gamma,-\epsilon)$. By (3.1), $w_\beta = \langle
x\rangle^{-\gamma}(\rho_I\rho_K)^{-\epsilon}$, and $\rho_I\rho_K = T\langle x\rangle/(T+\langle x\rangle)^2$ with $T :=
\langle t_*\rangle$. As $\int(T\langle x\rangle/(T+\langle x\rangle)^2)^{2\epsilon}\frac{dt_*}{\langle
t_*\rangle}\le2\sqrt3+\frac4{\sqrt3}\int_0^\infty(\frac\varsigma{(1+\varsigma)^2})^{2\epsilon}\frac{d\varsigma}\varsigma
=: C_\epsilon<\infty$ (the integrand is at most 1, and $\{T\le2\}$ has $t_*$-length $2\sqrt3$; on $\{T\ge2\}$, $T\,dT
= |t_*|dt_*$ gives $\frac{dt_*}{\langle t_*\rangle} = \frac{dT}{(T^2-1)^{1/2}}\le\frac2{\sqrt3}\frac{dT}T$ on each
half-line, and $T = \langle x\rangle\varsigma$), uniformly in $x$, the claim follows by Fubini. $\square$

**Proposition 3.5 ([Hin26c] Proposition 13.11).** Let $\beta_K\in(0,\infty)\setminus\mathbb N$,
$\beta_\iota,\beta_{\mathrm{scf}},\beta_I,\delta\in\mathbb R$, $\epsilon\in(0,1)$, and $\chi\in C_c^\infty((-1,1))$
equal to 1 near $[-\frac12,\frac12]$.

(1) (*Low energies.*) Let $\ell := \lceil(\max(\beta_\iota-\beta_{\mathrm{scf}},\beta_K)+\epsilon-\frac12)_+\rceil$. If
$v_\pm\in H^{k+\ell,(\beta_{\mathrm{scf}},\beta_\iota-1,((0,0),\beta_K-1))}_b(X^\pm_{\mathrm{sc}\text{-}b};\mathcal H)$
($c = 1$) have the same $\sigma$-Taylor coefficients, then for $v := \chi(\sigma)\sum_\pm1_{\pm\sigma>0}v_\pm$,
$$\mathcal F^{-1}v\in H^{k,(\min(\beta_{\mathrm{scf}},\beta_\iota)-\epsilon,\ \beta_\iota,\ \beta_K)}_b(M;\mathcal H),$$
with norm $\le C\sum_\pm\|v_\pm\|$.

(2) (*High energies.*) Let $\beta' := \max(\beta_K,\beta_\iota-\beta_I)$ and $\ell :=
\lceil(\frac32-\delta)_+\rceil+\lceil(\beta'-\frac12)_+\rceil$. If $v_\pm\in
H^{k+\ell,\beta_I,\delta-1}_{b+}(\pm[\frac12,\infty)\times X;\mathcal H)$, then $\mathcal F^{-1}((1-\chi)v_\pm)\in
H^{k,(\beta_I,\beta_\iota,\beta_K)}_b(M;\mathcal H)$, with norm $\le C\|v_\pm\|$.

*Proof.* (1) *The expansion.* For each $\ell<\beta_K-1$ (here $\ell$ indexes the expansion, not the loss), by the
matching, the terms of index $\ell$ of the two signs add up to $\chi(\sigma)\chi_1(|\sigma|\langle x\rangle)\sigma^\ell
c_\ell(x) = \phi_\ell(\sigma\langle x\rangle)v_\ell(x)$, where $c_\ell = \langle x\rangle^\ell v_\ell$ is the common
coefficient, $v_\ell\in H^{k,\beta_\iota-1}_b(X)$, and $\phi_\ell(s) := \chi_1(|s|)s^\ell\in
C_c^\infty((-\frac14,\frac14))$; $\chi(\sigma) = 1$ where $\chi_1(|\sigma|\langle x\rangle)\ne0$, as
$|\sigma|\le\frac14$ there. Substituting $s = \sigma\langle x\rangle$,
$$\mathcal F^{-1}\big(\phi_\ell(\sigma\langle x\rangle)\big)(t_*) = \rho\,\check\phi_\ell(\rho t_*),\qquad
\check\phi_\ell(\tau) := \frac1{2\pi}\int e^{-is\tau}\phi_\ell(s)\,ds\in\mathcal S(\mathbb R).$$
$\langle\rho t_*\rangle$ is comparable to $\rho_K^{-1} = (\langle t_*\rangle+\langle x\rangle)/\langle x\rangle$, and
$\langle t_*\rangle\partial_{t_*}$, $\langle x\rangle\partial_x$ map $\check\phi_\ell(\rho t_*)$ to $\frac{\langle
t_*\rangle}{\langle x\rangle}\check\phi'_\ell(\rho t_*)$ and $-\frac x{\langle x\rangle}(\rho t_*)\check\phi'_\ell(\rho
t_*)$, with $\langle t_*\rangle/\langle x\rangle\le C\langle\rho t_*\rangle$; so $\rho_K^{-N}\check\phi_\ell(\rho t_*)$
is bounded with all its b-derivatives, for every $N$. With $\rho = \rho_I\rho_\iota$ and Lemma 3.4 for $v_\ell$, the
inverse transform of the expansion lies in $H^{k,(\beta_\iota-\epsilon,\beta_\iota,N)}_b(M)$ for every $N$.

*The remainder.* Let $\tilde v_\pm\in H^{k+\ell,(\gamma,\beta_\iota-1,\beta_K-1)}_b(X^\pm_{\mathrm{sc}\text{-}b})$,
$\gamma := \beta_{\mathrm{scf}}$, and split $\tilde v_\pm = w_1+w_2$ with $w_2 := \chi_1(\frac{\hat r}4)\tilde v_\pm$,
supported in $\{\hat r\le1\}$, away from scf, and $w_1$ supported in $\{\hat r\ge\frac12\}$, away from zf. We treat the
side $+$; the function $\chi w_i$ on $(0,1)$, extended by 0 to $\sigma<0$, has the pair $(0,\chi w_i)$ with zero Taylor
polynomial.

For $w_1$: for $\eta\ge0$, $w_1\in H^{k+\ell,(\gamma-\eta,\beta_\iota-1,\beta_\iota-1-\gamma+\eta)}_b$ (lowering scf;
the zf-weight is free away from zf), so by Lemma 3.1 (b) $\chi
w_1\in\bigcap_jH^{j+\ell,a}_b((0,1);H^{k-j,\gamma-\eta}_b(X))$, $a := \beta_\iota-1-\gamma+\eta$; the powers $\sigma^j$,
$|\sigma|\le1$, are harmless, so $(0,\chi w_1)\in X^{j+\ell,a}$ with values in $H^{k-j,\gamma-\eta}_b(X)$. If $\beta :=
a+1 = \beta_\iota-\gamma+\eta\in(0,\infty)\setminus\mathbb N$ and $\ell\ge\ell_+(\beta)$, Proposition 2.8 (2) and Lemma
3.1 (a) give
$$\mathcal F^{-1}(\chi w_1)\in\bigcap_jH^{j,\beta_\iota-\gamma+\eta}_b(\mathbb R;H^{k-j,\gamma-\eta}_b(X)) =
H^{k,(\gamma-\eta,\ \beta_\iota,\ \beta_\iota-\gamma+\eta)}_b(M).$$
Take $\eta_0 := \max(0,\gamma-\beta_\iota)+\epsilon'$ and $\eta_1 := \max(0,\beta_K-\beta_\iota+\gamma)+\epsilon'$,
$\epsilon'\in(0,\epsilon]$ chosen so that neither $\beta_\iota-\gamma+\eta_i$ is an integer. With $\eta_0$, $\beta>0$
and the $\mathscr I$-weight is $\min(\gamma,\beta_\iota)-\epsilon'$; with $\eta_1\ge\eta_0$ the $K$-weight is
$\ge\beta_K$. The larger loss is $\ell_+(\beta_\iota-\gamma+\eta_1) =
\lceil(\max(\beta_\iota-\gamma,\beta_K)+\epsilon'-\frac12)_+\rceil\le\ell$ (the source's (13.22)). Combining the two
memberships (same $\iota$-weight) gives $\mathcal F^{-1}(\chi w_1)\in
H^{k,(\min(\gamma,\beta_\iota)-\epsilon,\beta_\iota,\beta_K)}_b(M)$. (The source applies (13.22) with $\eta =
\max(\eta_0,\eta_1)$ and states the $\mathscr I$-weight obtained with $\eta_0$; the combination is needed; section 7,
(J5).)

For $w_2$: for $\eta\ge0$ with $\beta_K-\eta\in(0,\infty)\setminus\mathbb N$, $w_2\in
H^{k+\ell,(\beta_\iota-\beta_K+\eta,\beta_\iota-1,\beta_K-1-\eta)}_b$ (the scf-weight is free away from scf), so as
before $\mathcal F^{-1}(\chi w_2)\in H^{k,(\beta_\iota-\beta_K+\eta,\beta_\iota,\beta_K-\eta)}_b(M)$, with loss
$\ell_+(\beta_K-\eta)\le\lceil(\beta_K-\frac12)_+\rceil\le\ell$. With $\eta = 0$ the $K$-weight is $\beta_K$; with $\eta
:= \beta_K-\epsilon$ the $\mathscr I$-weight is $\beta_\iota-\epsilon$. Combining gives
$H^{k,(\beta_\iota-\epsilon,\beta_\iota,\beta_K)}_b(M)$. The three pieces give (1).

(2) $w := (1-\chi)v_\pm$, extended by 0, vanishes on $(-\frac12,\frac12)$. By Lemma 3.1 (a),
$H^{k,(\beta_I,\beta_I+\beta',\beta')}_b(M)\subset H^{k,(\beta_I,\beta_\iota,\beta_K)}_b(M)$, and by Lemma 2.2 it
suffices to show $W := \sigma^p(\sigma\partial_\sigma)^qw\in H^{\beta'-\frac12}(\mathbb R;H^{k-j,\beta_I}_b(X))$ for
$p+q\le j\le k$. Let $m := \lceil(\beta'-\frac12)_+\rceil$ and $N := \lceil(\frac32-\delta)_+\rceil$, so $\ell = N+m$.
The hypothesis says $\sigma^{a}(\sigma\partial_\sigma)^bv_\pm\in|\sigma|^{1-\delta}L^2(|d\sigma/\sigma|)
= |\sigma|^{\frac32-\delta}L^2(d\sigma)$, with values in $H^{k+\ell-a-b,\beta_I}_b(X)$, for $a+b\le k+\ell$. For $i\le
m$, $\partial^i_\sigma W = \sigma^{-i}\sum_{i'\le i}a_{ii'}(\sigma\partial_\sigma)^{i'}W$ on $|\sigma|\ge\frac12$, and
$(\sigma\partial_\sigma)^{i'}W$ is a combination of $\sigma^p(\sigma\partial_\sigma)^{q+i''}w$, $i''\le i'$; writing
$\sigma^p = \sigma^{-N}\sigma^{p+N}$, each lies in $|\sigma|^{\frac32-\delta-N}L^2\subset L^2(d\sigma)$ on
$|\sigma|\ge\frac12$, with values in $H^{k+\ell-p-N-q-i'',\beta_I}_b(X)\subset H^{k-j,\beta_I}_b(X)$, as $p+N+q+i''\le
j+N+m = j+\ell$. The derivatives of $1-\chi$ are smooth and compactly supported in $\frac12\le|\sigma|\le1$. So $W\in
H^m\subset H^{\beta'-\frac12}$ (if $\beta'\le\frac12$, $m = 0$ and $W\in L^2\subset H^{\beta'-\frac12}$). $\square$

*Remark 3.6 ([Hin26c] Remark 13.12).* The losses of b-regularity in Propositions 3.3 and 3.5 depend only on the weights,
not on $k$. Proposition 3.5 (2) is proved directly from Lemma 2.2; its loss $\ell$ differs from the source's
$\lceil2\ell'+\delta\rceil$, whose $\ell'$ is printed with an unbalanced bracket and whose first step, the trade of
b$+$-regularity for decay into the space $H^{\cdot,((0,0),\delta+\ell'-1)}_{b+}$, needs $\ell'\ge1-\delta$ in addition
(section 7, (J6)).

*Remark 3.7 (the exterior $\bar X$).* Sections 4-5 use $\bar X := \{|x|\ge r_0\}\cup\partial\bar X$ of I.A section 1.1,
with spaces extendible at $\{|x| = r_0\}$. Every statement of this section holds with $X$ replaced by $\bar X$ and the
b-spaces in $x$ by their extendible versions (quotient norms of restrictions): apply it to $\mathcal Eu$ and restrict,
where $\mathcal E$ is Seeley's extension in $|x|$ across $|x| = r_0$ (the operator with infinitely many reflections
written out in the proof of II.E Lemma 1.3 (b), as in II.F$'$ Lemma 2.5). $\mathcal E$ acts in $x$ alone, near $|x| =
r_0$ where the weights are bounded above and below; it commutes with $t_*$, with $\mathcal F$ in $t_*$ and with
$\sigma\partial_\sigma$, and is bounded on the extendible b-spaces of every order at once, so the norms of
$\bigcap_jH^{j,\beta}_b(\mathbb R;\bar H^{k-j,\gamma}_b(\bar X))$ and of the restrictions of
$H^{k,(\gamma,\beta+\gamma,\beta)}_b(M)$ are equivalent, as in Lemma 3.1.

## 4. Resolvent bounds at n = 4

### 4.1 Fixed frequencies

On $\bar X$, $\mu = |dx|$ and $\mu_b = |dx|/\langle x\rangle^4$. The spaces $\bar H^{(s;k),\mathsf r}$ are those of I.A
section 4.6 (scattering regularity $s$, decay order $\mathsf r$, $k$ b-derivatives, for $\mu$). For a constant decay
order and $s = 0$, $\bar H^{(0;k),\beta-2} = \bar H^{k,\beta}_b(\bar X,\mu_b)$, the b-Sobolev space with weight $\beta$
for $\mu_b$, as $\langle x\rangle^{-\beta+2}L^2(\mu) = \langle x\rangle^{-\beta}L^2(\mu_b)$; and I.C's $\bar H^{s,a}_b$
(I.C Definition 2.8) is $\bar H^{s,a+2}_b(\bar X,\mu_b)$. $R_{\mathrm{out}}$ is the zero section of the boundary face
over $\partial X$ (I.A (4.6)).

**Lemma 4.1 ([Hin26c] Lemma 13.13 at $n = 4$).** Let $s\in\mathbb R$ be constant and $\mathsf r$ a decay order (I.A
section 1.4) equal to the constant $\mathsf r_{\mathrm{out}}$ on a neighbourhood of $R_{\mathrm{out}}$. Let
$\alpha\in\mathbb R$, $k\in\mathbb N_0$, $\epsilon>0$, and
$$\ell := \max\big(\lceil\sup\mathsf r-\mathsf r_{\mathrm{out}}\rceil,\lceil(s-1)_+\rceil\big),\qquad\tilde\ell :=
\max\big(\lceil\mathsf r_{\mathrm{out}}-\inf\mathsf r\rceil,\lceil(-s)_+\rceil\big).$$
Then there are continuous inclusions
$$\bar H^{k+\ell,\mathsf r_{\mathrm{out}}+\alpha+3+\epsilon}_b(\bar X,\mu_b)\hookrightarrow
\bar H^{(s-1;k),\mathsf r+\alpha+1},\tag{4.1a}$$
$$\bar H^{(s;k),\mathsf r+\alpha}\hookrightarrow
\bar H^{k-\tilde\ell,\mathsf r_{\mathrm{out}}+\alpha+2-\epsilon}_b(\bar X,\mu_b)\qquad(k\ge\tilde\ell),\tag{4.1b}$$
and likewise on $\mathbb R^4$ without the artificial boundary.

The source's (13.23a)-(13.23b) have $\frac52$ and $\frac32$ in place of $3$ and $2$, and allow a variable regularity
order and a decay order that is not constant near $R_{\mathrm{out}}$ (with its supremum, resp. infimum, there); Part I's
orders have constant regularity order (I.A Remark 1.1) and decay orders constant near $R_{\mathrm{out}}$ (I.A (O2)).

*Proof.* It suffices to prove the inequalities for distributions on $\mathbb R^4$: for the extendible spaces, apply them
to an extension of almost minimal norm and restrict. We use the scattering calculus with variable orders of I.A section
2 (boundedness $\Psi^{m,l}:H^{s,\mathsf r}\to H^{s-m,\mathsf r-l}$, microlocality, composition) and I.A Lemma 4.10. Let
$q_0$ be a symbol of order $(0,0)$, equal to 1 near $R_{\mathrm{out}}$ and supported in a neighbourhood $U$ of it, at
finite frequencies, on which $\mathsf r = \mathsf r_{\mathrm{out}}$; $Q_0 := \mathrm{Op}(q_0)$ and $Q_1 := I-Q_0$, so
$\mathrm{WF}'(Q_1)\cap R_{\mathrm{out}} = \emptyset$. For $V^\alpha := (\langle x\rangle D_x)^\alpha$, as $\langle
x\rangle D_{x_j}\in\Psi^{1,1}$ and commutators with elements of $\Psi^{0,0}$ lie in $\Psi^{0,0}$, $V^\alpha Q_0 =
\sum_{\beta\le\alpha}Q_{\alpha\beta}V^\beta$ with $Q_{\alpha\beta}\in\Psi^{0,0}$ microsupported in $\mathrm{WF}'(Q_0)$.

(4.1b): put $k' := k-\tilde\ell$. On $\mathrm{WF}'(Q_{\alpha\beta})\subset U$ the frequencies are finite and $\mathsf
r+\alpha\ge\mathsf r_{\mathrm{out}}+\alpha-\epsilon$, so $Q_{\alpha\beta}$ maps $H^{s,\mathsf r+\alpha}$ to
$H^{0,\mathsf r_{\mathrm{out}}+\alpha-\epsilon}$ (its symbol lies in the class of order $(-N,\mathsf r-\mathsf
r_{\mathrm{out}}+\epsilon)$ for every $N$), and $\|Q_0u\|_{(0;k'),\mathsf r_{\mathrm{out}}+\alpha-\epsilon}\le
C\|u\|_{(s;k'),\mathsf r+\alpha}$. For $Q_1$, I.A Lemma 4.10 and its converse give
$$\|Q_1u\|_{(0;k'),\mathsf r_{\mathrm{out}}+\alpha-\epsilon}\le
C\big(\|Q_1u\|_{k',\mathsf r_{\mathrm{out}}+\alpha-\epsilon+k'}+\|u\|_{-N,-N}\big)\le
C\big(\|Q_1u\|_{s+k,\mathsf r+\alpha+k}+\|u\|_{-N,-N}\big)\le C\|u\|_{(s;k),\mathsf r+\alpha},$$
the middle inequality as $k'\le s+k$ and $\mathsf r_{\mathrm{out}}-\epsilon+k'\le\inf\mathsf r+k$ (both by the choice of
$\tilde\ell$), the last as $Q_1$ is bounded on $H^{(s;k),\mathsf r+\alpha}$ (commute $V^\alpha$ through it as above).
With $\bar H^{(0;k'),\mathsf r_{\mathrm{out}}+\alpha-\epsilon} = \bar H^{k',\mathsf
r_{\mathrm{out}}+\alpha+2-\epsilon}_b(\mu_b)$ this is (4.1b).

(4.1a): for $f$ in the space on the left, $f\in H^{(0;k+\ell),\mathsf r_{\mathrm{out}}+\alpha+1+\epsilon}$. On
$\mathrm{WF}'(Q_{\alpha\beta})$, $\mathsf r+\alpha+1 = \mathsf r_{\mathrm{out}}+\alpha+1$, so $\|Q_0f\|_{(s-1;k),\mathsf
r+\alpha+1}\le C\|f\|_{(0;k),\mathsf r_{\mathrm{out}}+\alpha+1+\epsilon}$. And $\|Q_1f\|_{(s-1;k),\mathsf r+\alpha+1}\le
C(\|Q_1f\|_{s-1+k,\mathsf r+\alpha+1+k}+\|f\|_{-N,-N})\le C(\|Q_1f\|_{k+\ell,\mathsf
r_{\mathrm{out}}+\alpha+1+\epsilon+k+\ell}+\|f\|_{-N,-N})\le C\|f\|_{(0;k+\ell),\mathsf
r_{\mathrm{out}}+\alpha+1+\epsilon}$, as $s-1\le\ell$ and $\sup\mathsf r\le\mathsf r_{\mathrm{out}}+\ell$. $\square$

**Corollary 4.2 ([Hin26c] Corollary 13.14 at $n = 4$).** Assume (H1)-(H4) of I.A, and let
$\beta_{\mathrm{scf}}<\frac32+\bar S$ and $\epsilon\in(0,1)$. There is $\ell\in\mathbb N_0$, depending only on $\hat P$
and $\beta_{\mathrm{scf}}$, such that:

(1) if $\sigma_0\ne0$, $\mathrm{Im}\,\sigma_0\ge0$, and $\hat P(\sigma_0):\mathcal X_{\sigma_0}\to\mathcal Y_{\sigma_0}$
is invertible (I.A Theorem 7.2; this does not depend on the admissible orders), then for $j,k\in\mathbb N_0$
$$\partial^j_\sigma\hat P(\sigma_0)^{-1}:\bar H^{k+j+\ell,\beta_{\mathrm{scf}}+1}_b(\bar X,\mu_b)\to
\bar H^{k,\beta_{\mathrm{scf}}-\epsilon}_b(\bar X,\mu_b)\ \text{is bounded};$$

(2) if $I\subset\mathbb R$ is a bounded open interval with $0\notin\bar I$ and $\hat P(\sigma)$ is invertible for every
$\sigma\in\bar I$, then $\hat P^{-1}:\hat f\mapsto(\sigma\mapsto\hat P(\sigma)^{-1}\hat f(\sigma))$ is bounded from
$\bar H^{k+\ell,\beta_{\mathrm{scf}}+1}_b(I\times\bar X)$ to $\bar H^{k,\beta_{\mathrm{scf}}-\epsilon}_b(I\times\bar
X)$, where $\|v\|^2_{\bar H^{k,\beta}_b(I\times\bar X)} := \sum_{k'\le k}\int_I\|\partial^{k'}_\sigma
v(\sigma)\|^2_{\bar H^{k-k',\beta}_b(\bar X,\mu_b)}\,d\sigma$.

The source asks in (2) only that $\hat P(\sigma)$ be invertible on the open interval $I$; uniform constants need it on
$\bar I$ (section 7, (J8)).

*Proof.* *Orders.* Let $\mathsf r_{\mathrm{out}} := \beta_{\mathrm{scf}}-2-\frac\epsilon2$, which is $<-\frac12+\bar S$,
the threshold at $R_{\mathrm{out}}$ of I.A (1.5) with weight $\alpha_+ = 0$; $\mathsf r_{\mathrm{in}} := \max(\mathsf
r_{\mathrm{out}},\frac12(-1+\vartheta_{\mathrm{in}})+1)$; and $s := s_c$ a fixed constant $>\frac12+\vartheta_{\mathcal
H}$. If $\mathrm{Re}\,\sigma_0\ne0$, I.A Lemma 7.1 at $\sigma_* := \mathrm{Re}\,\sigma_0$ gives an order pair
$(s,\mathsf r)$ admissible for every real part near $\sigma_*$, with $\mathsf r = \mathsf r_{\mathrm{out}}+(\mathsf
r_{\mathrm{in}}-\mathsf r_{\mathrm{out}})\Theta\chi_c$ taking values in $[\mathsf r_{\mathrm{out}},\mathsf
r_{\mathrm{in}}]$ and equal to $\mathsf r_{\mathrm{out}}$ near $R_{\mathrm{out}}$ ($\Theta = 0$ near $\xi = 0$). If
$\mathrm{Re}\,\sigma_0 = 0$, then $\mathrm{Im}\,\sigma_0>0$ and the constant order $\mathsf r\equiv\mathsf
r_{\mathrm{out}}$ is allowed by I.A Theorem 7.2 (2). In both cases Lemma 4.1 applies with $\ell_a :=
\max(\lceil(\frac12(-1+\vartheta_{\mathrm{in}})+\frac72-\beta_{\mathrm{scf}})_+\rceil,\lceil(s-1)_+\rceil)$, which is at
least $\lceil\mathsf r_{\mathrm{in}}-\mathsf r_{\mathrm{out}}\rceil$ for every $\epsilon\in(0,1)$ (Lemma 4.1 holds with
any larger loss), so that $\ell$ does not depend on $\epsilon$ and $\tilde\ell := \lceil(-s)_+\rceil$; put $\ell :=
\ell_a+\tilde\ell$.

(1) By I.A Theorem 7.2 (6), (7.6), with $\alpha_+ = 0$ (at $\mathrm{Re}\,\sigma_0 = 0$ the proof of (7.6) in I.A uses
only Theorem 7.2 (4) and the invertibility at the orders $(s+\ell,\mathsf r)$, which hold with the constant order):
$\partial^j_\sigma\hat P(\sigma_0)^{-1}:\bar H^{(s-1;k+\tilde\ell+j),\mathsf r+1}\to\bar H^{(s+j;k+\tilde\ell),\mathsf
r}\subset\bar H^{(s;k+\tilde\ell),\mathsf r}$. Precompose with (4.1a) at $\alpha = 0$, $\frac\epsilon2$ and order
$k+\tilde\ell+j$, whose source space is $\bar H^{k+j+\ell,\beta_{\mathrm{scf}}+1}_b$ as $\mathsf
r_{\mathrm{out}}+3+\frac\epsilon2 = \beta_{\mathrm{scf}}+1$, and compose with (4.1b) at $\frac\epsilon2$ and order
$k+\tilde\ell$, whose target is $\bar H^{k,\beta_{\mathrm{scf}}-\epsilon}_b$.

(2) For $\sigma_*\in\bar I$, the orders chosen at $\sigma_*$ serve for all $\sigma$ near $\sigma_*$ (I.A Lemma 7.1,
resp. Theorem 7.2 (2)), and by I.A Theorem 7.2 (6) the estimates (7.1), (7.3) hold there without their last terms
uniformly, so $\hat P(\sigma)^{-1}$ is bounded uniformly near $\sigma_*$; as $\partial_\sigma\hat P^{-1} = -\hat
P^{-1}(\partial_\sigma\hat P)\hat P^{-1}$, the bounds (7.6) for $\partial^j_\sigma\hat P^{-1}$ are uniform near
$\sigma_*$ too. By compactness of $\bar I$, finitely many such neighbourhoods cover it, and (1) holds with constants
uniform in $\sigma\in\bar I$. For $\hat f$ smooth in $\sigma$, $\partial^{k'}_\sigma(\hat P^{-1}\hat f) = \sum_{k''\le
k'}\binom{k'}{k''}(\partial^{k''}_\sigma\hat P^{-1})(\partial^{k'-k''}_\sigma\hat f)$ by the strong differentiability of
I.A Theorem 7.2 (6), and (1) with $k-k'$ in place of $k$ and $j = k''$ bounds the $k''$-th term in $\bar
H^{k-k',\beta_{\mathrm{scf}}-\epsilon}_b$ by $C\|\partial^{k'-k''}_\sigma\hat f(\sigma)\|_{\bar
H^{k-k'+k''+\ell,\beta_{\mathrm{scf}}+1}_b}$, a term of the norm of $\hat f$ in $\bar
H^{k+\ell,\beta_{\mathrm{scf}}+1}_b(I\times\bar X)$; such $\hat f$ are dense. $\square$

### 4.2 High frequencies

The semiclassical spaces and the norms $\|\cdot\|_{(s;k),\mathsf r,\mathsf b;+}$ are those of I.B (1.5), with the
quantisation $\mathrm{Op}_h$ of I.B section 2. For constant orders $(0,\mathsf r',0)$, $H^{0,\mathsf r',0}_h = \langle
x\rangle^{-\mathsf r'}L^2$ for every $h$ (I.B section 2.3), so
$$\|v\|_{(0;k),\mathsf r',0;+} = \sum_{j\le k}h^{-j}\|v\|_{\bar H^{k-j,\mathsf r'+2}_b(\bar X,\mu_b)},\tag{4.2}$$
which at $h = |\sigma|^{-1}$ is the norm at fixed $\sigma$ of the spaces (13.16) (section 3.1).

*Admissible orders.* For $z_0\in\{1,-1\}$ and constants $\mathsf r_{\mathrm{out}}<-\frac12+\bar S$, $\mathsf
r_{\mathrm{in}}\ge\mathsf r_{\mathrm{out}}$ with $\mathsf r_{\mathrm{in}}>\frac12(-1+\vartheta_{\mathrm{in}})$, the
order $\mathsf r := \mathsf r_{\mathrm{out}}+(\mathsf r_{\mathrm{in}}-\mathsf
r_{\mathrm{out}})\Theta(\xi)\chi_c(\xi^2+|\eta|^2)$ of I.A Lemma 7.1 at $\sigma_* := z_0$, read in the semiclassical
frequency $\zeta = (\xi,\eta)$ on the face over $\partial X$ and extended off it independently of $\rho$, is admissible
for $z_0$ with weight 0 in the sense of I.B section 1.4. It is constant near $R_{z_0,\mathrm{in}} = \{\xi = -2z_0,\eta =
0\}$ and near $R_{\mathrm{out}}$. By I.A (4.5), $\mathsf H_{z_0}\xi = 2|\eta|^2$ on the whole face, $\mathsf H_{z_0}$
being, up to a positive factor, the field of I.A (4.5) there (I.B Lemma 4.1); so on $W := \{\chi_c = 1\}^\circ$, a
neighbourhood of $\Sigma^\partial_{z_0}$ in the face, $\mathsf H_{z_0}\mathsf r = 2(\mathsf r_{\mathrm{in}}-\mathsf
r_{\mathrm{out}})\Theta'(\xi)|\eta|^2$. On $\mathrm{supp}\,\Theta'$, $\varepsilon_*\xi\in[-\frac32,-\frac12]$
($\varepsilon_* = z_0$), and $q = -2\xi$ there (I.B Lemma 4.1 (b)), so $\mathrm{sgn}\,\hat q_{z_0} = z_0$ and $\mathsf
H^\natural\mathsf r = z_0\mathsf H_{z_0}\mathsf r\le0$, as $z_0\Theta'\le0$. The semiclassical order $\mathsf b\equiv0$
is admissible (constant orders are). Below, $(s,\mathsf r,\mathsf b)$ are these orders, with $s := s_c$.

**Lemma 4.3 (b-spaces and semiclassical spaces).** Let $z_0$ and $(s,\mathsf r,\mathsf b)$ be as above, $\mathsf b$
being any order constant near $R_{\mathrm{out}}$, and $\epsilon>0$. There are $\ell_1,\ell_2,N\in\mathbb N_0$, depending
only on the orders, such that for $h\in(0,h_0]$ and $k\in\mathbb N_0$
$$\|f\|_{(s-1;k),\mathsf r+1,\mathsf b;+}\le C_kh^{-N}\|f\|_{(0;k+\ell_1),\mathsf r_{\mathrm{out}}+1+\epsilon,0;+},
\tag{4.3a}$$
$$\|u\|_{(0;k),\mathsf r_{\mathrm{out}}-\epsilon,0;+}\le C_kh^{-N}\|u\|_{(s;k+\ell_2),\mathsf r,\mathsf b;+}.\tag{4.3b}$$

*Proof.* As in Lemma 4.1 it suffices to work on $\mathbb R^4$, with the b-derivatives $V := \langle x\rangle D_x$ (I.B
section 5.5: on $\bar X$ they and I.B's $V$'s span the b-vector fields, with equivalent norms). By I.B (5.9),
$\|u\|_{(s;k),\mathsf r,\mathsf b;+}$ is equivalent, uniformly in $h$, to $h^{-k}\|u\|_{\mathbf o;k}$ with
$\|u\|_{\mathbf o;k} := \sum_{|\alpha|\le k}\|(hV)^\alpha u\|_{\mathbf o}$, $\mathbf o := (s,\mathsf r,\mathsf b)$. The
operators $hV_j$ have scalar symbols $\langle x\rangle\zeta_j$, of order $(1,1,0)$, and by I.B (2.5) their commutators
with $Q\in\Psi^0$ lie in $\Psi^{(0,0,-1)+\epsilon'\mathbf 1}$, microsupported in $\mathrm{WF}'_h(Q)$; inductively
$(hV)^\alpha Q = \sum_{\beta\le\alpha}Q_{\alpha\beta}(hV)^\beta$ with $Q_{\alpha\beta}\in\Psi^{\epsilon'\mathbf 1}$
microsupported in $\mathrm{WF}'_h(Q)$. Choose $c,\rho_*\in(0,1)$ such that $\mathsf r$ and $\mathsf b$ are constant
($\mathsf r_{\mathrm{out}}$, $\mathsf b_{\mathrm{out}}$) on $U_0 := \{\rho<2\rho_*,\ |\zeta|<2c\}$, and functions
$\phi_0,\phi_1,\phi_2$ on $\mathcal P$ with $\phi_0+\phi_1+\phi_2 = 1$, $\mathrm{supp}\,\phi_0\subset U_0$,
$\mathrm{supp}\,\phi_1\subset\{|\zeta|>c\}$, $\mathrm{supp}\,\phi_2\subset\{|\zeta|<2c,\ \rho>\rho_*\}$; $Q_i :=
\mathrm{Op}_h(\phi_i)$, $\sum Q_i = I$.

(4.3b): let $\mathbf o_t := (0,\mathsf r_{\mathrm{out}}-\epsilon,0)$; we show $\|u\|_{\mathbf o_t;k}\le
Ch^{-N}\|u\|_{\mathbf o;k+\ell_2}$, which with I.B (5.9) and (4.2) gives (4.3b). On $U_0$, $w_{\mathbf o_t}w_{\mathbf
o}^{-1} = \langle\zeta\rangle^{-s}\langle x\rangle^{-\epsilon}h^{\mathsf b_{\mathrm{out}}}\le Ch^{\mathsf
b_{\mathrm{out}}}$, and on $\mathrm{supp}\,\phi_2$, where $x$ ranges over a compact set and $\zeta$ is bounded,
$w_{\mathbf o_t}w_{\mathbf o}^{-1}\le Ch^{\inf\mathsf b}$; so for $i = 0,2$, $W_{\mathbf o_t}Q_{i,\alpha\beta}W_{\mathbf
o}^{-1}$ has a symbol bounded by $Ch^{\min(\mathsf b_{\mathrm{out}},\inf\mathsf b)-2\epsilon'}$ times a symbol of order
0, and by I.B Theorem 2.7 and Proposition 2.8, $\|(hV)^\alpha Q_iu\|_{\mathbf o_t}\le Ch^{-N_0}\|u\|_{\mathbf
o;|\alpha|}+C\|u\|_{-K\mathbf 1}$, $N_0 := \lceil(-\min(\mathsf b_{\mathrm{out}},\inf\mathsf b))_++1\rceil$. For $i =
1$: $(hV)^\alpha\in\Psi^{|\alpha|(1,1,0)}$, so by I.B Proposition 2.8 $\|(hV)^\alpha Q_1u\|_{\mathbf o_t}\le
C\|Q_1u\|_{\mathbf o_t+k(1,1,0)}$ for $|\alpha|\le k$. With $\ell_2 := \max(\lceil(-s)_+\rceil,\lceil\mathsf
r_{\mathrm{out}}-\inf\mathsf r\rceil)$, $m := k+\ell_2$ and $N_1 := \lceil(-\inf\mathsf b)_+\rceil$, $\mathbf
o_t+k(1,1,0)\le\mathbf o+m(1,1,0)+(0,0,N_1)$ componentwise, so $\|Q_1u\|_{\mathbf o_t+k(1,1,0)}\le C\|Q_1u\|_{\mathbf
o+m(1,1,0)+(0,0,N_1)} = Ch^{-N_1}\|Q_1u\|_{\mathbf o+m(1,1,0)}$. Finally $A := \sum_{|\alpha| =
m}((hV)^\alpha)^*(hV)^\alpha\in\Psi^{2m(1,1,0)}$ has principal symbol $\sum_{|\alpha| = m}|\langle
x\rangle^m\zeta^\alpha|^2\ge c'\langle x\rangle^{2m}\langle\zeta\rangle^{2m}$ on $\{|\zeta|\ge c\}$, so it is elliptic
on $\mathrm{WF}'_h(Q_1)$ (I.B section 8.5 (ii)), and I.B Proposition 2.10 gives $\|Q_1u\|_{\mathbf o+m(1,1,0)}\le
C(\|Au\|_{\mathbf o-m(1,1,0)}+\|u\|_{-K\mathbf 1})\le C(\|u\|_{\mathbf o;m}+\|u\|_{-K\mathbf 1})$, by Proposition 2.8
for $((hV)^\alpha)^*\in\Psi^{m(1,1,0)}$. As $\|u\|_{-K\mathbf 1}\le C\|u\|_{\mathbf o}$, (4.3b) holds with $N :=
\max(N_0,N_1)$.

(4.3a) is proved in the same way, with $\mathbf o_s := (0,\mathsf r_{\mathrm{out}}+1+\epsilon,0)$ as the source orders
and $\mathbf o' := (s-1,\mathsf r+1,\mathsf b)$ as the target: $w_{\mathbf o'}w_{\mathbf o_s}^{-1}\le Ch^{-\mathsf
b_{\mathrm{out}}}$ on $U_0$ and $\le Ch^{-\sup\mathsf b}$ on $\mathrm{supp}\,\phi_2$; and $\mathbf o'+k(1,1,0)\le\mathbf
o_s+(k+\ell_1)(1,1,0)+(0,0,N_1)$ with $\ell_1 := \max(\lceil(s-1)_+\rceil,\lceil\sup\mathsf r-\mathsf
r_{\mathrm{out}}\rceil)$ and $N_1 := \lceil(\sup\mathsf b)_+\rceil$. $\square$

**Proposition 4.4 ([Hin26c] Proposition 13.16 at $n = 4$).** Assume (H1)-(H8) of I.B, and let $C_0$ be as in I.B Theorem
1.3 (3). Let $\beta_{\mathrm{scf}}<\frac32+\bar S$, $\epsilon\in(0,1)$, $\eta>0$, $\delta_1,\delta_2\in\mathbb R$, and
$\delta := \delta_\Gamma(-\eta)$ (I.B (1.4)). There is $\ell\in\mathbb N_0$ such that for all $k\in\mathbb N_0$, $\hat
P^{-1}:\hat f\mapsto(\sigma\mapsto\hat P(\sigma)^{-1}\hat f(\sigma))$ is bounded
$$H^{k+\lceil k\delta\rceil+\ell,\ \beta_{\mathrm{scf}}+1,\ \delta_1}_{b+}(\pm[C_0,\infty)\times\bar X)\to
H^{k,\ \beta_{\mathrm{scf}}-\epsilon,\ \delta_2}_{b+}(\pm[C_0,\infty)\times\bar X),\tag{4.4}$$
the spaces (13.16) of section 3.1 with $\bar X$ and $\mu_b$.

The source writes the loss as $k(1+\delta_\Gamma(-\epsilon))+\ell$, which need not be an integer. It also notes that the
loss in $k$ is harmless for strongly trapping admissible operators with $\epsilon = 1/k$. Here, in I.B's terms: if
$\gamma_+<0$ in I.B (1.4), then $\delta_\Gamma(-\eta) = 0$ for $\eta<-\gamma_+$; if $\gamma_+ = 0$, then
$\delta_\Gamma(-\eta) = \eta/(-\gamma_-)$ and $\lceil k\delta_\Gamma(-1/k)\rceil = \lceil1/(-\gamma_-)\rceil$ for every
$k$. The source states this proposition without proof ("we obtain").

*Proof.* Take $z_0 := \pm1$, $h := |\sigma|^{-1}$ (so $z = h\sigma = z_0$ for real $\sigma$), $\alpha_+ := 0$, and the
orders above with $\mathsf r_{\mathrm{out}} := \beta_{\mathrm{scf}}-2-\frac\epsilon2$, $\mathsf b\equiv0$; let
$\ell_1,\ell_2,N$ be those of Lemma 4.3 with $\frac\epsilon2$. For $\pm\sigma\ge C_0$, $\hat P(\sigma)$ is invertible
(I.B Theorem 1.3 (3)), and I.B (1.8) reads
$$\|(\sigma\partial_\sigma)^j\hat P(\sigma)^{-1}g\|_{(s+j;m),\mathsf r,0;+}\le
C|\sigma|^{-1+(j+1)\delta}\|g\|_{(s-1;m+j),\mathsf r+1,0;+}.$$
By (4.2) at $h = |\sigma|^{-1}$, the norm of $v := \hat P^{-1}\hat f$ in the target of (4.4) is equivalent to
$(\sum_{l\le k}\int|\sigma|^{2\delta_2}\|(\sigma\partial_\sigma)^lv\|^2_{(0;k-l),\mathsf
r_{\mathrm{out}}-\frac\epsilon2,0;+}\,|d\sigma/\sigma|)^{1/2}$, as $\beta_{\mathrm{scf}}-\epsilon-2 = \mathsf
r_{\mathrm{out}}-\frac\epsilon2$. By Leibniz' rule (first for $\hat f$ in the dense subspace of functions smooth in
$\sigma$, as in Corollary 4.2 (2), then by continuity), $(\sigma\partial_\sigma)^lv$ is a combination of
$((\sigma\partial_\sigma)^{l'}\hat P^{-1})g_{l'}$, $g_{l'} := (\sigma\partial_\sigma)^{l-l'}\hat f$, $l'\le l$ (I.B
Theorem 1.3 (5) gives the differentiability), and by (4.3b), (1.8) and (4.3a), at fixed $\sigma$,
$$\|((\sigma\partial_\sigma)^{l'}\hat P^{-1})g\|_{(0;k-l),\mathsf r_{\mathrm{out}}-\frac\epsilon2,0;+}\le
C|\sigma|^{2N-1+(l'+1)\delta}\|g\|_{(0;K),\mathsf r_{\mathrm{out}}+1+\frac\epsilon2,0;+},\qquad K := k-l+l'+\ell_1+
\ell_2,$$
and $2N-1+(l'+1)\delta\le2N+k\delta$ as $l'\le k$, $\delta\le1$, $|\sigma|\ge1$. By (4.2), as $\mathsf
r_{\mathrm{out}}+1+\frac\epsilon2+2 = \beta_{\mathrm{scf}}+1$, the last norm is $\sum_{j\le K}|\sigma|^j\|g\|_{\bar
H^{K-j,\beta_{\mathrm{scf}}+1}_b}$. Let $M := 2N+\lceil k\delta\rceil+\lceil(\delta_2-\delta_1)_+\rceil$, so
$|\sigma|^{\delta_2}|\sigma|^{2N+k\delta}|\sigma|^j\le|\sigma|^{\delta_1}|\sigma|^{j+M}$. The function
$\sigma^{j+M}(\sigma\partial_\sigma)^{l-l'}\hat f$ with values in $\bar H^{K-j,\beta_{\mathrm{scf}}+1}_b$ is a term of
the norm of $\hat f$ in $H^{k',\beta_{\mathrm{scf}}+1,\delta_1}_{b+}$ with $k' = (j+M)+(l-l')+(K-j) =
k+M+\ell_1+\ell_2$. So (4.4) holds with $\ell := \ell_1+\ell_2+2N+\lceil(\delta_2-\delta_1)_+\rceil$. $\square$

**Corollary 4.5 ([Hin26c] Corollary 13.17 at $n = 4$).** Assume (H1)-(H8) of I.B for the spectral family $\hat P$ of a
stationary wave-type operator $P_0$ (II.C Lemma 1.2), let $C_0\ge1$ be as in I.B Theorem 1.3 (3) (enlarged if necessary,
which preserves invertibility), $\chi\in C_c^\infty(\mathbb R)$ equal to 1 on $[-C_0,C_0]$, and $\chi_T\in
C^\infty(\mathbb R)$ equal to 0 on $(-\infty,1]$ and to 1 on $[2,\infty)$. Let
$\beta_I,\beta_\iota,\beta_K,\beta'_\iota,\beta'_K\in\mathbb R$, $\beta'_I<\min(\beta_I,\frac32+\bar S)$, $\eta>0$ and
$\delta := \delta_\Gamma(-\eta)$. There is $\ell\in\mathbb N_0$ such that for every $k$ and every $f\in H^{k+\lceil
k\delta\rceil+\ell,(\beta_I+1,\beta_\iota+2,\beta_K)}_b(M;E)$ ($M$ over $\bar X$, Remark 3.7), $u := \mathcal
F^{-1}\big((1-\chi(\sigma))\hat P(\sigma)^{-1}\hat f(\sigma)\big)$ lies in
$H^{k,(\beta'_I,\beta'_\iota,\beta'_K)}_b(M;E)$, with norm $\le C_k\|f\|$. If $f\in H^{k+\lceil
k\delta\rceil+\ell,(\beta_I+1,\beta_\iota+2,\beta_K)}_b(\Omega;E)^{\bullet,-}$ (extended by 0 to $t_*<1$), then
$\chi_T(t_*)u\in H^{k,(\beta'_I,\beta'_\iota,\beta'_K)}_b(\Omega;E)^{\bullet,-}$.

Here, as in the source's section 13, the b-spaces on $\Omega$ are those of II.F$'$ (1.2) with the unweighted b-density
$\mu_b$ of II.F$'$ Corollary 1.2; on $\Omega$ the defining functions (3.1) and those of II.F$'$ (1.1) ($\rho_I$,
$\rho_+$, $\rho_K$ for $\mathscr I^+$, $\iota^+$, $K^+$) are comparable with ratios bounded with all their
b-derivatives, and $\mu_M$ and $\mu_b$ likewise, so these spaces are restrictions of those on $M$.

*Proof.* By Proposition 3.3 (2) with the weights $(\beta_I+1,\beta_\iota+2,\beta_K)$, $\hat f|_{\pm[\frac12,\infty)}\in
H^{K-\ell_5,\beta_I+1,0}_{b+}$, $K$ the order of $f$ and $\ell_5 :=
\lceil(\frac12-\min(\beta_K,\beta_\iota+1-\beta_I))_+\rceil$. Let $\beta_{\mathrm{scf}} := \beta'_I+\epsilon$ with
$\epsilon>0$ so small that $\beta_{\mathrm{scf}}<\min(\beta_I,\frac32+\bar S)$; then
$H^{\cdot,\beta_I+1,\cdot}_{b+}\subset H^{\cdot,\beta_{\mathrm{scf}}+1,\cdot}_{b+}$. Let $\ell_3 :=
1+\lceil(\max(\beta'_K,\beta'_\iota-\beta'_I)-\frac12)_+\rceil$, the loss of Proposition 3.5 (2) with $\delta = 1$ and
the weights $(\beta'_I,\beta'_\iota,\beta'_K)$, and $\ell_4$ that of Proposition 4.4 with $\delta_1 = 0 = \delta_2$. By
Proposition 4.4 at the order $k+\ell_3$ (and $\lceil(k+\ell_3)\delta\rceil\le\lceil k\delta\rceil+\ell_3$), $\hat
P^{-1}\hat f\in H^{k+\ell_3,\beta'_I,0}_{b+}(\pm[C_0,\infty)\times\bar X)$ when $K\ge k+\lceil
k\delta\rceil+2\ell_3+\ell_4+\ell_5$. Multiplied by $1-\chi$, which vanishes on $[-C_0,C_0]$ and is smooth with bounded
$\sigma\partial_\sigma$-derivatives, and extended by 0, it lies in
$H^{k+\ell_3,\beta'_I,0}_{b+}(\pm[\frac12,\infty)\times\bar X)$ and vanishes near $[-\frac12,\frac12]$; Proposition 3.5
(2) (with $\delta-1 = 0$) gives $u\in H^{k,(\beta'_I,\beta'_\iota,\beta'_K)}_b(M)$. So $\ell := 2\ell_3+\ell_4+\ell_5$.
Finally $\chi_T(t_*)$ is smooth with bounded b-derivatives on $M$, and $\chi_T(t_*)u$ is supported in $\{t_*\ge1\}$, so
its restriction lies in the space on $\Omega$. $\square$

### 4.3 Low frequencies

For $\varsigma>0$ and weights $\beta = (\beta_{\mathrm{scf}},\beta_{\mathrm{tf}},\beta_{\mathrm{zf}})$, let
$w_\beta(\varsigma)$ be the product of $\rho_{\mathrm{scf}}^{\beta_{\mathrm{scf}}}$,
$\rho_{\mathrm{tf}}^{\beta_{\mathrm{tf}}}$ and $\rho_{\mathrm{zf}}^{\beta_{\mathrm{zf}}}$ of (3.2) at $|\sigma| =
\varsigma$, a function of $x$, and $\|u\|_{H^{k,\beta}_{b,\varsigma}} := \|w_\beta(\varsigma)^{-1}u\|_{\bar H^k_b(\bar
X,\mu_b)}$ ([Hin26c] after (13.30a)). The b-derivatives of $\log w_\beta(\varsigma)$ in $x$ are bounded uniformly in
$\varsigma$, so weights and derivatives may be ordered either way, and the norm of
$H^{k,\beta}_b(X^\pm_{\mathrm{sc}\text{-}b})$ is equivalent to $(\sum_{k'\le
k}\int\|(\sigma\partial_\sigma)^{k'}u(\sigma)\|^2_{H^{k-k',\beta}_{b,|\sigma|}}|d\sigma/\sigma|)^{1/2}$, as
$\sigma\partial_\sigma\log w_\beta$ is bounded too. The norms $\|\cdot\|_{(s;k),(\mathsf r,l,q),\varsigma}$ are those of
I.C Definition 6.1, with a decay order $\mathsf r$ on the scattering face of tf, and $\varsigma_1$ that of I.C Lemma
6.2.

**Lemma 4.6 ([Hin26c] (13.30a)-(13.30b) at $n = 4$).** Let $(s,\mathsf r)$ be an order pair with $s$ constant and
$\mathsf r$ equal to $\mathsf r_{\mathrm{out}}$ near the zero section over the scattering face of tf, let $\ell$,
$\tilde\ell$ be as in Lemma 4.1, and $l\in\mathbb R$, $k\in\mathbb N_0$, $\epsilon>0$. Uniformly in
$\varsigma\in(0,\varsigma_1]$,
$$\|u\|_{(s-1;k),(\mathsf r+1,l+2,0),\varsigma}\le
C\|u\|_{H^{k+\ell,(\mathsf r_{\mathrm{out}}+3+\epsilon,\ l+4,\ 0)}_{b,\varsigma}},\tag{4.5a}$$
$$\|u\|_{H^{k-\tilde\ell,(\mathsf r_{\mathrm{out}}+2-\epsilon,\ l+2,\ 0)}_{b,\varsigma}}\le
C\|u\|_{(s;k),(\mathsf r,l,0),\varsigma}\qquad(k\ge\tilde\ell).\tag{4.5b}$$

The source's (13.30a)-(13.30b) have $\frac52$, $\frac72$ and $\frac32$, $\frac32$ in place of $3$, $4$ and $2$, $2$ (the
shift $\frac n2$), and are written with $\alpha_+$, $\alpha_{\mathrm{tf}}$ (here absorbed in $\mathsf r$ and $l$).

*Proof.* By I.C Definition 6.1, $\|u\|^2_{(s;k),(\mathsf r,l,0),\varsigma} = \|(1-\chi_\partial)u\|^2_{\bar
H^{s+k}}+\varsigma^{-2(l+2)}\|S_\varsigma(\chi_\partial u)\|^2_{H^{(s;k),(\mathsf
r,-l)}_{\mathrm{sc},b;b}(\mathrm{tf})}$, and by I.C Lemma 6.2 (b) multiplication by $\chi_\partial$ is bounded uniformly
on both sides. *The interior.* On $\mathrm{supp}(1-\chi_\partial)$, a compact set, $\rho_{\mathrm{tf}}$ and
$\rho_{\mathrm{scf}}$ are bounded above and below and $\rho_{\mathrm{zf}}^{\beta_{\mathrm{zf}}} = 1$
($\beta_{\mathrm{zf}} = 0$), so the norms on the right of (4.5a) and the left of (4.5b) are equivalent to $\bar
H^{k+\ell}$, resp. $\bar H^{k-\tilde\ell}$, there, and $k+\ell\ge s-1+k$, $k-\tilde\ell\le s+k$. *Near $\partial X$.*
Let $\hat x := \varsigma x$ and $\hat\rho := \langle x\rangle^{-1}/\varsigma$; then $\rho_{\mathrm{scf}} =
\hat\rho/(1+\hat\rho)$, $\rho_{\mathrm{tf}} = \varsigma(1+\hat\rho)$ and $\rho_{\mathrm{zf}} = (1+\hat\rho)^{-1}$
exactly, so $w_\beta(\varsigma) = \varsigma^{\beta_{\mathrm{tf}}}W_\beta(\hat\rho)$ with $W_\beta(\hat\rho) :=
(\frac{\hat\rho}{1+\hat\rho})^{\beta_{\mathrm{scf}}}(1+\hat\rho)^{\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}}}$, independent
of $\varsigma$. On $\mathrm{supp}\,\chi_\partial$ ($|x|\ge R_1$) the dilation $S_\varsigma$ preserves $\mu_b$ and maps
the b-fields $\langle x\rangle\partial_x$ to fields spanning, with bounded coefficients, the b-fields of tf (I.C section
4: $\hat r\partial_{\hat x}$ near ztf, $\langle\hat x\rangle\partial_{\hat x}$ near sctf). Hence $\|\chi_\partial
u\|_{H^{k,\beta}_{b,\varsigma}}$ is equivalent, uniformly in $\varsigma$, to
$\varsigma^{-\beta_{\mathrm{tf}}}\|W_\beta^{-1}S_\varsigma(\chi_\partial u)\|_{H^k_b(\mathrm{tf},\mu_b)}$, a b-norm on
tf with the weight $\hat\rho^{\beta_{\mathrm{scf}}}$ at sctf ($\hat\rho\to0$) and $\hat
r^{\beta_{\mathrm{zf}}-\beta_{\mathrm{tf}}}$, $\hat r = |\hat x|$, at ztf. For (4.5b), $\beta = (\mathsf
r_{\mathrm{out}}+2-\epsilon,l+2,0)$: the powers $\varsigma^{-(l+2)}$ agree; at ztf both norms are b-norms (I.C
Definition 4.1: b-regularity is regularity there) with the b-weight $-l-2$ for $\mu_b$; at sctf the tf norm is that of
$H^{(s;k),\mathsf r}_{\mathrm{sc}}(\mathbb R^4_{\hat x})$ and the b-norm has the scattering decay order $\mathsf
r_{\mathrm{out}}-\epsilon$ (I.C Definition 4.1 and the density shift), and Lemma 4.1 (4.1b) on $\mathbb R^4_{\hat x}$,
with $\alpha = 0$, compares them; in between, on compact subsets of $\mathrm{tf}^\circ$, both are standard Sobolev norms
of orders $s+k\ge k-\tilde\ell$. (4.5a) is the same with $\beta = (\mathsf r_{\mathrm{out}}+3+\epsilon,l+4,0)$: the
powers are $\varsigma^{-(l+4)}$ on both sides (the I.C norm has $l+2$ in place of $l$), the b-weight at ztf is $-l-4$ on
both sides ($q-(l+2)-2$ with $q = 0$), and at sctf (4.1a) compares the decay orders $\mathsf
r_{\mathrm{out}}+1+\epsilon$ and $\mathsf r+1$. $\square$

**Proposition 4.7 ([Hin26c] Proposition 13.18 at $n = 4$).** Assume (H1)-(H4) of I.A and (G), (Z) and (TF) of I.C with
the weight $\alpha$ ($\alpha+2$ in an indicial gap of $\hat P(0)$, for $\mu_b$). Let $\beta_{\mathrm{scf}}<\frac32+\bar
S$ and $\epsilon\in(0,1)$. There is $\ell\in\mathbb N_0$, depending only on $\hat P$ and $\beta_{\mathrm{scf}}$, and for
each $k\in\mathbb N_0$ there is $c_k>0$ such that, with $X^\pm_{\mathrm{sc}\text{-}b}$ built on $\pm[0,c_k]$, for all
$\beta_{\mathrm{tf}},\beta_{\mathrm{zf}}$ with $\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}} = \alpha+2$,
$$\hat P^{-1}:
H^{k+\ell,(\beta_{\mathrm{scf}}+1,\ \beta_{\mathrm{tf}}+2,\ \beta_{\mathrm{zf}})}_b(X^\pm_{\mathrm{sc}\text{-}b})\to
H^{k,(\beta_{\mathrm{scf}}-\epsilon,\ \beta_{\mathrm{tf}},\ \beta_{\mathrm{zf}})}_b(X^\pm_{\mathrm{sc}\text{-}b})
\ \text{is bounded}.\tag{4.6}$$

The source fixes one $c$ for all $k$; I.C Theorem 6.4 (4) gives $c_{j,k}$ depending on $j,k$ (I.C Remark 6.7 (a)), so
here $c_k$ depends on $k$ (section 7, (J10)). The gap condition is on the b-weight for $\mu_b$, as in I.C (G). As I.C
Theorem 6.4 (5) gives its conclusions at every weight of the gap ((Z) by I.C Theorem 3.1 (4), (TF) by I.C Corollary 5.2
(c)), and $\ell = \ell_a+\tilde\ell$ does not depend on $\alpha$, the proposition holds for every
$\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}}$ in the gap with one $\ell$, as the source's (13.31) states; only $c_k$ and the
constants depend on the weight.

*Proof.* As $|\sigma|^{\beta_{\mathrm{zf}}} =
\rho_{\mathrm{tf}}^{\beta_{\mathrm{zf}}}\rho_{\mathrm{zf}}^{\beta_{\mathrm{zf}}}$ is scalar in $\sigma$, commutes with
$\hat P(\sigma)^{-1}$, and $\sigma\partial_\sigma|\sigma|^{\beta_{\mathrm{zf}}} =
\beta_{\mathrm{zf}}|\sigma|^{\beta_{\mathrm{zf}}}$, dividing by it reduces to $\beta_{\mathrm{zf}} = 0$,
$\beta_{\mathrm{tf}} = \alpha+2$. Take $\alpha_+ := 0$, $\mathsf r_{\mathrm{out}} :=
\beta_{\mathrm{scf}}-2-\frac\epsilon2$, $\mathsf r_{\mathrm{in}}$ and $s$ as in Corollary 4.2, and the decay orders
$\mathsf r_\pm$ of I.C section 4.3 built from them (I.A Lemma 7.1 at $\sigma_* = \pm1$), which equal $\mathsf
r_{\mathrm{out}}$ near the zero section over sctf; let $\ell_a$, $\tilde\ell$ be those of Lemma 4.1 for them and $\ell
:= \ell_a+\tilde\ell$. By I.C Theorem 6.4 (4) (with $m_1 = m_2 = 0$, which (Z) allows) and (5), for $0<|\sigma|\le
c_{j,m}$, $\mathrm{Im}\,\sigma\ge0$,
$$\|(\sigma\partial_\sigma)^j\hat P(\sigma)^{-1}g\|_{(s+j;m),(\mathsf r,\alpha,0),\varsigma}\le
C\|g\|_{(s-1;m+j),(\mathsf r+1,\alpha+2,0),\varsigma},\qquad\varsigma = |\sigma|.$$
Let $c_k := \min(\varsigma_1,\min\{c_{j,m}:j\le k,\ m\le k+\tilde\ell\})$. For $k'\le k$, Leibniz' rule (first for $\hat
f$ in the dense subspace of functions smooth in $\sigma$, as in Corollary 4.2 (2), then by continuity) writes
$(\sigma\partial_\sigma)^{k'}(\hat P^{-1}\hat f)$ as a combination of $((\sigma\partial_\sigma)^{k''}\hat P^{-1})g$, $g
:= (\sigma\partial_\sigma)^{k'-k''}\hat f$, and at fixed $\sigma$, by (4.5b) with $l = \alpha$ and $\frac\epsilon2$, the
estimate above with $m = k-k'+\tilde\ell$, and (4.5a) with $l = \alpha$ and $\frac\epsilon2$,
$$\|((\sigma\partial_\sigma)^{k''}\hat P^{-1})g\|_{H^{k-k',(\beta_{\mathrm{scf}}-\epsilon,\alpha+2,0)}_{b,\varsigma}}\le
C\|g\|_{H^{k-k'+k''+\ell,(\beta_{\mathrm{scf}}+1,\alpha+4,0)}_{b,\varsigma}},$$
as $\mathsf r_{\mathrm{out}}+2-\frac\epsilon2 = \beta_{\mathrm{scf}}-\epsilon$ and $\mathsf
r_{\mathrm{out}}+3+\frac\epsilon2 = \beta_{\mathrm{scf}}+1$. The total order $(k'-k'')+(k-k'+k''+\ell) = k+\ell$ is that
of the source space, so integrating in $|d\sigma/\sigma|$ gives (4.6). $\square$

## 5. The radiation field at n = 4

### 5.1 The normal form near null infinity

We use the defining functions of II.F$'$ (1.1), $\rho_I = t_*/(t_*+r)$ and $\rho_+ = (t_*+r)/(t_*r)$, of $\mathscr I^+$
and $\iota^+$. On $\{t_*>0,\ r>0\}$ the map $(t_*,r)\mapsto(\rho_I,\rho_+)$ is a diffeomorphism onto $\{0<\rho_I<1,\
\rho_+>0\}$, with inverse $t_* = (\rho_+(1-\rho_I))^{-1}$, $r = (\rho_I\rho_+)^{-1}$, and $\rho_K = 1-\rho_I$. For
$c_0\in(0,\frac14]$ let
$$\mathcal C := \{0\le\rho_I<c_0,\ 0\le\rho_+<4\}\times\mathbb S^3,\qquad\mathcal C_a := \mathcal C\cap\{\rho_I<
a\}\quad(0<a\le c_0),$$
a neighbourhood of $\mathscr I^+\cap\{t_*>\frac14\}$ (including its corner with $\iota^+$) in the compactified
spacetime, on which $r>1/(4c_0)$. On $\mathcal C$ the b-vector fields are spanned by $\rho_I\partial_{\rho_I}$,
$\rho_+\partial_{\rho_+}$ and the vector fields on $\mathbb S^3$, and $\mu_{\mathcal C}
:= |\frac{d\rho_I}{\rho_I}\frac{d\rho_+}{\rho_+}d\omega|$ is a b-density equivalent to $\mu_b = |dt_*\,dx|/(t_*\langle
x\rangle^4)$: in logarithmic coordinates the Jacobian of $(\log\rho_I,\log\rho_+)\mapsto(\log t_*,\log r)$ has
determinant $(1-\rho_I)^{-1}\in[1,\frac43]$. $H^{k,(b_I,b_+)}_b(\mathcal C_a) := \rho_I^{b_I}\rho_+^{b_+}H^k_b(\mathcal
C_a,\mu_{\mathcal C})$; near $\mathscr I^+$ these are the spaces of Corollary 4.5 and of II.F$'$ (1.2) with $\mu_b$, the
weight at $K^+$ being irrelevant ($\rho_K\ge\frac34$ on $\mathcal C$). Let
$$\mathsf W := \rho_I\partial_{\rho_I}-\rho_+\partial_{\rho_+},$$
which commutes with $\rho_I\partial_{\rho_I}$, $\rho_+\partial_{\rho_+}$ and the fields on $\mathbb S^3$. On
$\{t_*,r>0\}$, with $\rho := r^{-1}$,
$$t_*\partial_{t_*}|_r = (1-\rho_I)\mathsf W,\qquad\rho\partial_\rho|_{t_*} = \rho_I\partial_{\rho_I}-\rho_I\mathsf W,
\qquad\rho\,t_*^{-1} = \rho_I\rho_+^2(1-\rho_I).\tag{5.1}$$
(Direct computation: $t_*\partial_{t_*}\rho_I = \rho_I(1-\rho_I)$, $t_*\partial_{t_*}\rho_+ = -\rho_+(1-\rho_I)$,
$\rho\partial_\rho\rho_I = \rho_I(1-\rho_I)$, $\rho\partial_\rho\rho_+ = \rho_I\rho_+$; checked by machine, scratchpad
a sympy check run with D214 (a scratch script, not kept; the identities are derived in the text).)

**Lemma 5.1 (the normal form at $n = 4$; [Hin26c] (13.32)).** Let $P_0$ be a stationary wave-type operator (II.C
Definition 1.1) with $S\in\rho C^\infty(\bar X;\mathrm{End}\,\mathbb C^N)$, that is $S|_{\partial X} = 0$. If $c_0$ is
small, then on $\mathcal C$
$$\tfrac12\rho_I^{-1}\rho_+^{-2}P_0 = -(\rho_I\partial_{\rho_I}-\tfrac32)\mathsf W+\tilde P,\qquad\tilde P\in
\rho_I\mathrm{Diff}^2_b(\mathcal C),\tag{5.2}$$
with coefficients smooth on $\bar{\mathcal C}$. If $S|_{\partial X}\ne0$, the left side differs from
$-(\rho_I\partial_{\rho_I}-\frac32)\mathsf W$ by $S|_{\partial X}\mathsf W$ modulo $\rho_I\mathrm{Diff}^2_b$, and (5.2)
fails.

*Proof.* Choose $c_0$ so small that $\rho<\rho_1$ on $\mathcal C$, where II.C (1.1) holds: $P_0 =
-2\partial_{t_*}\rho(\rho\partial_\rho-\frac32-S)+\hat P_0(0)+Q\partial_{t_*}-g_{00}\partial_{t_*}^2$, all coefficients
$t_*$-independent and smooth in $(\rho,\omega)$, so smooth in $(\rho_I,\rho_+,\omega)$ as $\rho = \rho_I\rho_+$. By
(5.1), as $\rho$ does not depend on $t_*$,
$$-2\partial_{t_*}\rho(\rho\partial_\rho-\tfrac32) = -2\rho t_*^{-1}(t_*\partial_{t_*})(\rho\partial_\rho-\tfrac32) =
-2\rho_I\rho_+^2(1-\rho_I)^2\mathsf W(\rho_I\partial_{\rho_I}-\rho_I\mathsf W-\tfrac32),$$
so $\frac12\rho_I^{-1}\rho_+^{-2}$ times it is $-(1-\rho_I)^2\mathsf
W(\rho_I\partial_{\rho_I}-\frac32)+(1-\rho_I)^2\mathsf W\rho_I\mathsf W$; as $(1-\rho_I)^2-1\in\rho_IC^\infty$ and
$\mathsf W\rho_I = \rho_I(\mathsf W+1)$, this is $-(\rho_I\partial_{\rho_I}-\frac32)\mathsf W$ modulo
$\rho_I\mathrm{Diff}^2_b$. The other terms, times $\frac12\rho_I^{-1}\rho_+^{-2}$: $2\partial_{t_*}\rho S = 2\rho
t_*^{-1}S\,t_*\partial_{t_*}$ gives $(1-\rho_I)^2S\mathsf W$, in $\rho_I\mathrm{Diff}^1_b$ as $S\in\rho C^\infty =
\rho_I\rho_+C^\infty$; $\hat P_0(0)\in\rho^2\mathrm{Diff}^2_b(\bar X)$ gives $\frac12\rho_I\mathrm{Diff}^2_b$, the
b-fields $\rho\partial_\rho$, $\partial_\omega$ of $\bar X$ being b-fields on $\mathcal C$ by (5.1); $Q\partial_{t_*}$,
$Q\in\rho^3\mathrm{Diff}^1_b$, gives $\rho^3t_*^{-1}\rho_I^{-1}\rho_+^{-2} = \rho_I^2\rho_+^2(1-\rho_I)$ times
b-operators; and $g_{00}\partial^2_{t_*} = g_{00}t_*^{-2}((t_*\partial_{t_*})^2-t_*\partial_{t_*})$,
$g_{00}\in\rho^2C^\infty$ (II.C Remark (a)), gives $\rho_I\rho_+^2(1-\rho_I)^2$ times b-operators. If $S|_{\partial
X}\ne0$, the term $(1-\rho_I)^2S\mathsf W$ contributes $S|_{\partial X}\mathsf W$ at $\rho_I = 0$. $\square$

At $n = 4$ the stationary models of II.C have coefficients in $C^\infty(\bar X)$, so the remainder gains a full power of
$\rho_I$; the source's (13.32) allows $\tilde P\in\rho_I^{1/2}\mathrm{Diff}^2_b$, for coefficients smooth in $x_I =
\rho_I^{1/2}$, and notes the gain $\rho_I$ for Kerr. Proposition 5.4 is stated for $\tilde
P\in\rho_I^\kappa\mathrm{Diff}^2_b(\mathcal C)$, $\kappa\in(0,1]$, with coefficients bounded with all their
b-derivatives. II.C's remark (C4) records that $S = 0$ for the record's (K1)-metrics in the coordinate frame; which
operators of Part III satisfy $S|_{\partial X} = 0$ is checked there.

**Definition 5.2 ([Hin26c] Definition 13.19).** Let $\chi_I\in C^\infty([0,\infty))$ equal 1 on $[0,\frac14]$ and 0 on
$[\frac12,\infty)$. For $a\in(0,c_0]$, $\zeta,b_I,b_+\in\mathbb R$ with $\zeta<b_I$ and $k\in\mathbb N_0$,
$$H^{k,(((\zeta,0),b_I),b_+)}_b(\mathcal C_a) := \big\{\chi_I(\rho_I/a)\rho_I^\zeta u_0+\tilde u:u_0\in
H^{k,b_+}_b(\mathscr I^+),\ \tilde u\in H^{k,(b_I,b_+)}_b(\mathcal C_a)\big\},$$
normed by $\|u_0\|+\|\tilde u\|$, where $H^{k,b_+}_b(\mathscr I^+) := \rho_+^{b_+}H^k_b([0,4)\times\mathbb
S^3,|\frac{d\rho_+}{\rho_+}d\omega|)$ and $u_0(\rho_+,\omega)$ is extended to $\mathcal C_a$ as a function independent
of $\rho_I$. If $\zeta\ge b_I$, the space is $H^{k,(b_I,b_+)}_b(\mathcal C_a)$ (take $u_0 = 0$). For $\zeta = \frac32$
and bounded $t_*$, $\rho_I^{3/2}u_0 = (t_*/r)^{3/2}(1+O(t_*/r))u_0(\rho_+,\omega)$ with $\rho_+ = t_*^{-1}+O(r^{-1})$:
the leading term is $r^{-\frac32}$ times a function of $(t_*,\omega)$, the radiation field.

The decomposition is unique when $\zeta<b_I$, as $\rho_I^\zeta\notin\rho_I^{b_I}L^2(d\rho_I/\rho_I)$ near 0. The source
leaves the extension of $u_{(1,0)}$ off $\mathscr I^+$ unstated (section 7, (J13)).

### 5.2 Transport along $\mathsf W$

In the coordinates $p := -\log\rho_I$, $q := -\log\rho_+$, $\mu_{\mathcal C} = |dp\,dq\,d\omega|$ and $\mathsf W =
-\partial_p+\partial_q$; with $c := p+q = \log r$, $\mathsf W = \partial_q$ at fixed $c$. So the integral curves of
$\mathsf W$ are the curves $\{r = \mathrm{const},\ \omega = \mathrm{const}\}$, run towards $\iota^+$ ($\rho_+$
decreasing, $\rho_I$ increasing).

**Lemma 5.3 (transport; replaces [Hin26b] Lemma 2.23).** Let $a\in(0,c_0]$, $b,b_+\in\mathbb R$, $b\ne b_+$,
$K\in\mathbb N_0$, and let $u\in L^2_{\mathrm{loc}}(\mathcal C_a)$ with $\mathsf Wu = w\in H^{K,(b,b_+)}_b(\mathcal
C_a)$, and $(\rho_I\partial_{\rho_I})^i(\rho_+\partial_{\rho_+})^jZ^\alpha u\in L^2_{\mathrm{loc}}$ for $i+j+|\alpha|\le
K$ ($Z$ the fields on $\mathbb S^3$).

(a) If $b>b_+$ and $u = 0$ on $\{\rho_+>2\}$, then $u\in H^{K,(b,b_+)}_b(\mathcal C_a)$, with $\|u\|\le C\|w\|$.

(b) If $b<b_+$ and $u\in H^{K,(b_0,b_+)}_b(\mathcal C_a\cap\{\rho_I>\frac a2\})$ for some (any) $b_0$, then $u\in
H^{K,(b,b_+)}_b(\mathcal C_{a/2})$, with $\|u\|\le C(\|w\|+\|u\|_{H^{K,(b_0,b_+)}_b(\mathcal C_a\cap\{\rho_I>a/2\})})$.

*Proof.* The fields $\partial_p$, $\partial_q$, $Z$ commute with $\mathsf W$ and preserve the hypotheses, so it suffices
to take $K = 0$ and apply the result to the derivatives. In the coordinates $(c,q,\omega)$ the region $\mathcal C_a$ is
$\{q>-\log4,\ q<c-p_a\}$, $p_a := -\log a$, the weight is $\rho_I^{-b}\rho_+^{-b_+} = e^{bp+b_+q} = e^{bc+(b_+-b)q}$,
and $\partial_qu = w$ in distributions, so for almost every $(c,\omega)$, $q\mapsto u(c,q,\omega)$ is absolutely
continuous.

(a) $u = 0$ for $q<-\log2$, so $u(c,q) = \int_{-\log2}^qw(c,q')\,dq'$ and
$$e^{bc+(b_+-b)q}u(c,q) = \int_{-\log2}^qe^{-(b-b_+)(q-q')}\big[e^{bc+(b_+-b)q'}w(c,q')\big]\,dq'.$$
The kernel $e^{-(b-b_+)s}1_{s>0}$ has $L^1$ norm $(b-b_+)^{-1}$; Young's inequality in $q$, then integration over
$(c,\omega)$, gives $\|u\|\le(b-b_+)^{-1}\|w\|$.

(b) For $(c,q)$ in $\mathcal C_{a/2}$, that is $c-q>p_a+\log2$, let $J_c := (c-p_a-\log2,c-p_a)$, the values $q'$ with
$\rho_I\in(\frac a2,a)$ on the same curve; $q'>q$ there. Averaging $u(c,q) = u(c,q')-\int_q^{q'}w(c,q'')\,dq''$ over
$q'\in J_c$,
$$u(c,q) = \frac1{\log2}\int_{J_c}u(c,q')\,dq'-\frac1{\log2}\int_{J_c}\int_q^{q'}w(c,q'')\,dq''\,dq'.$$
On $J_c$, $e^{b_+q'}$ is comparable to $e^{b_+(c-p_a)}$ and $e^{b_0p'}$ to a constant, so the first term is at most
$Ce^{-b_+c}U(c)$, $U(c)^2 := \int_{J_c}|e^{b_0p'+b_+q'}u(c,q')|^2dq'$; times the weight it is at most
$Ce^{(b-b_+)(c-q)}U(c) = Ce^{(b-b_+)p}U(c)$, whose $L^2$ norm over $p>p_a+\log2$ is at most $CU(c)$, as $b<b_+$; and
$\int U(c)^2\,dc$ is the norm of $u$ on the strip. In the second term, for each $q'$, $e^{bc+(b_+-b)q}\int_q^{q'}w =
\int_q^{q'}e^{-(b_+-b)(q''-q)}e^{bc+(b_+-b)q''}w(c,q'')\,dq''$, and the kernel $e^{-(b_+-b)s}1_{s>0}$ has $L^1$ norm
$(b_+-b)^{-1}$; Minkowski's inequality over $q'$ and Young's inequality bound it by $(b_+-b)^{-1}\|e^{bc+(b_+-b)q}w\|$.
$\square$

### 5.3 The radiation field

**Proposition 5.4 ([Hin26c] Proposition 13.20 at $n = 4$).** Suppose that on $\mathcal C$,
$\frac12\rho_I^{-1}\rho_+^{-2}P_0 = -(\rho_I\partial_{\rho_I}-\frac32)\mathsf W+\tilde P$ with $\tilde
P\in\rho_I^\kappa\mathrm{Diff}^2_b(\mathcal C)$, $\kappa\in(0,1]$ (by Lemma 5.1, $\kappa = 1$ when $S|_{\partial X} =
0$). Let $\beta_I,\beta_+,\beta'_I\in\mathbb R$ with
$$\beta_+\ne\tfrac32,\qquad\beta'_I<\tfrac32+\kappa,\qquad\beta'_I\notin\{\tfrac32,\beta_+\}.$$
There are $\ell\in\mathbb N_0$ and $a\in(0,c_0]$, depending only on $\beta_I$, $\beta'_I$, $\kappa$ and $c_0$, such
that: if $u\in H^{k+\ell,(\beta_I,\beta_+)}_b(\mathcal C)$ vanishes on $\{t_*<1\}$ and $P_0u\in
H^{k+\ell,(\beta'_I+1,\beta_++2)}_b(\mathcal C)$, then
$$u\in H^{k,(((\frac32,0),\beta'_I),\beta_+)}_b(\mathcal C_a).\tag{5.3}$$

So $u$ has a radiation field $\rho_I^{3/2}u_0$, the coefficient of $r^{-3/2}$, plus a remainder with the weight of
$P_0u$ at $\mathscr I^+$, shifted by the factor $\rho_I\rho_+^2$ of (5.2). At $n = 3$ the source has the exponent 1, the
condition $1\ne\beta_+<\beta_I$, and $\beta'_I<\frac32 = 1+\frac12$ ($\kappa = \frac12$); here the hypothesis
$\beta_+<\beta_I$ is not used.

*Proof.* If $\beta_I\ge\beta'_I$ there is nothing to prove ($u_0 = 0$). Otherwise we improve the weight at $\mathscr
I^+$ in steps. On $\mathcal C$, $\{\rho_+>2\}\subset\{t_*<1\}$ (as $1-\rho_I\ge\frac34$), so $u = 0$ there.

*The step.* Suppose $u\in H^{K,(((\frac32,0),b),\beta_+)}_b(\mathcal C_{a'})$ with $K\ge2$ and $b<\beta'_I$, $u =
\chi_I(\rho_I/a')\rho_I^{3/2}u_0+\tilde u$ (with $u_0 = 0$ if $b\le\frac32$). Let $b''\in(b,\min(b+\kappa,\beta'_I)]$,
with $b'' = \beta'_I$ if $b+\kappa\ge\beta'_I$ and $b''\ge b+\frac\kappa2$ otherwise, chosen outside
$\{\frac32,\beta_+\}$. We show $u\in H^{K-2,(((\frac32,0),b''),\beta_+)}_b(\mathcal C_{a'/8})$.

(i) Let $h := \tilde Pu-\frac12\rho_I^{-1}\rho_+^{-2}P_0u$, so that $(\rho_I\partial_{\rho_I}-\frac32)\mathsf Wu = h$.
$\tilde P$ maps $\chi_I\rho_I^{3/2}u_0$ into $H^{K-2,(\frac32+\kappa-\epsilon,\beta_+)}_b$ for every $\epsilon>0$
($\rho_I^{3/2}$ lies in $\rho_I^{3/2-\epsilon}L^2(d\rho_I/\rho_I)$ near 0), hence into $H^{K-2,(b'',\beta_+)}_b$ as
$b''\le\beta'_I<\frac32+\kappa$; it maps $\tilde u$ into $H^{K-2,(b+\kappa,\beta_+)}_b\subset H^{K-2,(b'',\beta_+)}_b$;
and $\frac12\rho_I^{-1}\rho_+^{-2}P_0u\in H^{K,(\beta'_I,\beta_+)}_b$. So $h\in H^{K-2,(b'',\beta_+)}_b(\mathcal
C_{a'})$.

(ii) Let $w := \mathsf Wu\in H^{K-1,(\cdot,\beta_+)}_b$. In the product $\mathcal C_{a'} =
[0,a')_{\rho_I}\times([0,4)\times\mathbb S^3)$, apply Lemma 3.2 in $s := \rho_I/a'$ to $(s\partial_s-\frac32)w = h$,
with values in $\mathcal H_j := H^{K-2-j,\beta_+}_b([0,4)\times\mathbb S^3)$ and $s$-regularity $j$, $j\le K-2$ (the
fields in $(\rho_+,\omega)$ commute with $\rho_I\partial_{\rho_I}$, and $w$ has $K-1$ b-derivatives on the annulus). If
$b''>\frac32$, Lemma 3.2 (a) gives, on $\mathcal C_{a'/4}$, $w = \rho_I^{3/2}w_0+\tilde w$ with $w_0\in
H^{K-2,\beta_+}_b(\mathscr I^+)$ and $\tilde w\in H^{K-2,(b'',\beta_+)}_b$; $w_0 = 0$ on $\{\rho_+>2\}$, as $w$ vanishes
there. If $b''<\frac32$, Lemma 3.2 (b) gives $w\in H^{K-2,(b'',\beta_+)}_b(\mathcal C_{a'/4})$.

(iii) *Transport.* Write $a_1 := a'/4$. *If $b''<\frac32$:* if $b''>\beta_+$, Lemma 5.3 (a) on $\mathcal C_{a_1}$ gives
$u\in H^{K-2,(b'',\beta_+)}_b(\mathcal C_{a_1})$; if $b''<\beta_+$, Lemma 5.3 (b), with the a priori bound on the strip
$\{\rho_I\in(\frac{a_1}2,a_1)\}$ from $u\in H^{K,(b,\beta_+)}_b$ there, gives it on $\mathcal C_{a_1/2}$. As
$b''<\frac32$ this is (5.3)'s space at $b''$.

*If $b''>\frac32$ and $b''>\beta_+$:* the backward integral curve of $\mathsf W$ from a point of $\mathcal C_{a_1}$
stays in $\mathcal C_{a_1}$ until $\rho_+ = 2$, where $u = 0$. Let
$$u_0^{\mathrm v}(\rho_+) := \rho_+^{3/2}\int_{\rho_+}^2s^{-3/2}w_0(s)\,\frac{ds}s,$$
which vanishes for $\rho_+\ge2$ and satisfies $(\frac32-\rho_+\partial_{\rho_+})u_0^{\mathrm v} = w_0$, so $\mathsf
W(\rho_I^{3/2}u_0^{\mathrm v}) = \rho_I^{3/2}w_0$. Then $u-\rho_I^{3/2}u_0^{\mathrm v}$ vanishes on $\{\rho_+>2\}$ and
$\mathsf W(u-\rho_I^{3/2}u_0^{\mathrm v}) = \tilde w$, so by Lemma 5.3 (a), $u-\rho_I^{3/2}u_0^{\mathrm v}\in
H^{K-2,(b'',\beta_+)}_b(\mathcal C_{a_1})$. If $\beta_+<\frac32$, then $u_0^{\mathrm v}\in H^{K-2,\beta_+}_b(\mathscr
I^+)$: in $\log\rho_+$, $\rho_+^{-\beta_+}u_0^{\mathrm v}$ is the convolution of $s^{-\beta_+}w_0$ with the kernel
$(\rho_+/s)^{\frac32-\beta_+}1_{s>\rho_+}$, of $L^1(ds/s)$ norm $(\frac32-\beta_+)^{-1}$, and $\rho_+\partial_{\rho_+}$
commutes with it. If $\beta_+>\frac32$, then $L := \int_0^2s^{-3/2}w_0(s)\frac{ds}s$ converges (Cauchy-Schwarz,
$\beta_+>\frac32$) and $u_0^{\mathrm v} = \rho_+^{3/2}L-u_0^{(0)}$ with $u_0^{(0)}(\rho_+) :=
\rho_+^{3/2}\int_0^{\rho_+}s^{-3/2}w_0\frac{ds}s\in H^{K-2,\beta_+}_b(\mathscr I^+)$, by the same convolution with the
kernel $(\rho_+/s)^{\frac32-\beta_+}1_{s<\rho_+}$. On $\{\rho_I\in(\frac{a_1}4,\frac{a_1}2)\}$, $u$,
$u-\rho_I^{3/2}u_0^{\mathrm v}$ and $\rho_I^{3/2}u_0^{(0)}$ lie in $\rho_+^{\beta_+}L^2(\mu_{\mathcal C})$, hence so
does $\rho_I^{3/2}\rho_+^{3/2}L(\omega)$; as $\int_0^4\rho_+^{2(\frac32-\beta_+)}\frac{d\rho_+}{\rho_+} = \infty$, $L =
0$, and $u_0^{\mathrm v} = -u_0^{(0)}\in H^{K-2,\beta_+}_b(\mathscr I^+)$. In both cases $u = \rho_I^{3/2}u_0^{\mathrm
v}+(u-\rho_I^{3/2}u_0^{\mathrm v})$ is in (5.3)'s space at $b''$ on $\mathcal C_{a_1/2}$ (replacing
$\rho_I^{3/2}u_0^{\mathrm v}$ by $\chi_I(\rho_I/(a_1/2))\rho_I^{3/2}u_0^{\mathrm v}$ changes it by a function supported
in $\{\rho_I\ge a_1/8\}$, in every $\rho_I$-weight).

*If $b''>\frac32$ and $b''<\beta_+$* (so $\beta_+>\frac32$): let $u_0 := -u_0^{(0)}\in H^{K-2,\beta_+}_b(\mathscr I^+)$
(as above), which satisfies $(\frac32-\rho_+\partial_{\rho_+})u_0 = w_0$, and $U := \chi_I(4\rho_I/a_1)\rho_I^{3/2}u_0$,
supported in $\{\rho_I<a_1/8\}$. Then $\mathsf W(u-U) = \tilde
w+\rho_I^{3/2}(1-\chi_I(4\rho_I/a_1))w_0-(\rho_I\partial_{\rho_I}\chi_I(4\rho_I/a_1))\rho_I^{3/2}u_0\in
H^{K-2,(b'',\beta_+)}_b(\mathcal C_{a_1})$, the last two terms being supported in $\{\rho_I\ge a_1/16\}$; and $u-U = u$
on $\{\rho_I>a_1/2\}$. Lemma 5.3 (b) gives $u-U\in H^{K-2,(b'',\beta_+)}_b(\mathcal C_{a_1/2})$.

*Iteration.* Each step raises $b$ by at least $\frac\kappa2$ until $b = \beta'_I$, costs two b-derivatives, and shrinks
the region by a factor 8. Starting from $b := \beta_I$ (with $u_0 = 0$), after $n_s :=
\lceil2(\beta'_I-\beta_I)/\kappa\rceil$ steps $b = \beta'_I$; so (5.3) holds with $\ell := 2n_s$ and $a := c_08^{-n_s}$.
$\square$

*Remark 5.5.* With Lemma 5.1, the proposition applies at $n = 4$ with $\kappa = 1$ to stationary wave-type operators
with $S|_{\partial X} = 0$, for $\beta'_I<\frac52$; at the level of $P_0u\in\rho_I^{\beta'_I+1}$, the remainder of $u$
after its radiation field $r^{-3/2}u_I$ decays like $\rho_I^{\beta'_I}$. The source's proof integrates the equation by
citing [Hin26b] Lemmas 2.12 and 2.23 (not read); Lemmas 3.2 and 5.3 replace them, and the case distinction in step (iii)
follows the source's ($b''$ against $\beta_+$, and the transport of the radiation field to a term $\rho_+^{3/2}$ at
$\iota^+$, which the a priori decay at $\iota^+$ excludes).

## 6. What is not carried, and uniformity in the operator

### 6.1 Not carried

(a) Remark 13.1 (nonlinear variants) describes how stronger decay of the source term can be fed back through the inverse
of the linear operator. It states nothing to prove. The route improves decay at the level of the linearised equations
(Part III), which is the alternative the remark recommends.

(b) Remark 13.15 (losses in b-regularity) explains why section 4 proves its bounds on variable order spaces before
passing to b-spaces: a lossy b-estimate on $\hat P(\sigma)^{-1}$, iterated for $\partial^j_\sigma\hat P(\sigma)^{-1}$,
would lose a number of b-derivatives growing with $j$, which tame estimates do not tolerate. Lemma 4.1, Corollary 4.2
and Proposition 4.7 follow that plan, with a loss depending only on the weights (Remark 3.6). The remark itself states
nothing to prove.

(c) Theorem 13.21 (small data global existence for $\Box_gu = f+u^3$ on Kerr) and Remark 13.22 (almost $t_*^{-2}$ decay
of linear scalar waves on Kerr) are model applications on the four-dimensional Kerr spacetime. They rest on the
0-admissibility of $\Box_g$ on Kerr ([Hin26c] Theorem 12.2) and on the proof of Theorem 12.9, neither of which is
carried (II.G section 5.2 (a), (c)). They are read, are not used by the route, and their weights at $n = 4$ are not
derived.

(d) Lemma 13.2, Lemma 13.6, and the parts of Lemma 13.4 and Corollary 13.5 beyond Lemma 2.4: Remark 2.9 and (J1).

(e) Figures 13.1 and 13.2 illustrate the spaces $M$ and $X^\pm_{\mathrm{sc}\text{-}b}$ and the weights in Propositions
13.9 (1) and 13.11 (1). They carry no statement and are not reproduced.

(f) The commentary after Proposition 13.18 (inputs with weight $-\frac12$ at zf, and the decay they give in (11.7))
states nothing to prove.

### 6.2 Uniformity in the operator

Sections 2 and 3 involve no operator. In section 4, Lemmas 4.1, 4.3 and 4.6 depend on the orders alone; the orders
depend on $\hat P$ only through the quantities of I.A that fix them ($\bar S$, $\vartheta_{\mathrm{in}}$,
$\vartheta_{\mathcal H}$ and the data of I.A Lemma 7.1). Corollary 4.2, Proposition 4.4, Corollary 4.5 and Proposition
4.7 depend on $\hat P$ further only through the constants of the estimates they cite: I.A Theorem 7.2, I.B Theorem 1.3
with the constant $C_0$ and the function $\delta_\Gamma$, and I.C Theorem 6.4 with its radii $c_{j,k}$. In section 5,
Proposition 5.4 depends on $P_0$ only through $\kappa$, $c_0$, the coordinates of $\mathcal C$ and finitely many
seminorms of the coefficients of $\tilde P$ in (5.2), as a b-differential operator on $\bar{\mathcal C}$, the number of
seminorms depending on $k$ and $\ell$.

So every bound of this part, and every loss $\ell$ and radius $c_k$, is uniform over any family of operators for which
these quantities are uniform. I.A section 8, I.B section 9 and I.C section 7 give conditions under which the cited
estimates are uniform over a family of operators. Whether the family the route needs satisfies them is the matter
recorded in II.F$'$ (F'11), which stays open; this part adds no condition to it.

## 7. Findings, and the sources

### 7.1 Findings

The findings are against [Hin26c] section 13 as printed, except (J3), (J7) and (J12), which record changes of route or
of dimension. None of them changes what Part III uses: Corollary 13.7, Propositions 13.9 and 13.11, the resolvent bounds
and Proposition 13.20, in the forms proved here.

(J1) *Lemma 13.4 at $\sigma = \infty$.* Lemma 13.4 states $\dot
H^s([0,\infty))\cong\sigma^{s-\frac12}H^s_b([0,\infty),|\frac{d\sigma}\sigma|)$ for $s>-\frac12$, and the text after
Corollary 13.5 insists that the weight is at $\sigma = 0$ and at $\sigma = \infty$. At $\sigma = \infty$ the inclusion
of the b-space in $\dot H^s$ fails. For $s = 1$ let $u := (1-\chi)\sigma^{2/5}$ with $\chi\in C_c^\infty([0,2))$ equal
to 1 on $[0,1]$. Then $\sigma^{-1}u$, $\partial_\sigma u$ and $\sigma^{-1}\sigma\partial_\sigma u$ lie in
$L^2(d\sigma)$, so $u\in\sigma H^1_b([0,\infty),|d\sigma|) = \sigma^{\frac12}H^1_b([0,\infty),|\frac{d\sigma}\sigma|)$;
but $u\notin L^2(d\sigma)$, so $u\notin\dot H^1$. The proof's first inclusion,
$H^{s,s}_b([0,\infty),|d\sigma|)\hookrightarrow\dot H^s$ from $\partial_\sigma = \sigma^{-1}\sigma\partial_\sigma$,
controls the derivatives but not $u$ itself, whose weight $\sigma^s$ is weaker than $L^2$ at $\infty$. The same $u$ lies
in $H^{1,((0,0),\frac12)}_b([0,\infty))$ and not in $\bar H^1((0,\infty))$, so Corollary 13.5 fails as printed as well.
The example concerns $\sigma = \infty$ only; what is used, at $\sigma = 0$, is carried by Lemma 2.4. Lemma 13.6 is
stated with these spaces and fails at $\sigma = \infty$ for the same reason (take the inverse transform of the same
example, extended by 0); it is not used later and not carried.

(J2) *The Taylor terms of (13.7)-(13.8).* (13.7) defines $H^{s,((0,0),\beta)}_b([0,\infty))$ with the sum
$\sum_{\ell=0}^{\lfloor s-\frac12\rfloor}$, indexed by the regularity $s$ ("the sum is empty for $s<\frac12$"), and
(13.8) defines $H^{k,((0,0),\beta)}_{b+}$ through $H^{0,((0,0),\beta)}_b$, where $\lfloor0-\frac12\rfloor = -1$ and the
sum is empty. As printed, the target $X^{k,\beta-1}$ of Corollary 13.7 carries no Taylor terms. Then Corollary 13.7 (1)
fails for $\beta>1$: for $u\in C_c^\infty(\mathbb R)$ with $\int u\ne0$, $u$ lies in every $H^{k,\beta}_b$, while
$\mathcal Fu(0)\ne0$ and $\mathcal Fu\notin|\sigma|^{\beta-1}L^2(|\frac{d\sigma}\sigma|)$ near 0. The matching condition
$v_-^{(l)}(0) = v_+^{(l)}(0)$, $l<\beta-1$, in the definition of $X^{k,\beta-1}$ presupposes Taylor terms of degree
$<\beta-1$, indexed by the weight. That is the reading of Definition 2.7, under which Corollary 13.7 holds (Proposition
2.8).

(J3) *Route on the line.* The source proves Lemma 13.2 from [Tay11a] (Chapter 4, Proposition 5.3: multiplication by the
Heaviside function on $H^s$, $0\le s<\frac12$) and duality, and Lemma 13.4 for real $s$ by complex interpolation.
Neither source was read. Section 2 proves what is used from the Gagliardo seminorm and two dyadic Hardy inequalities
(Lemmas 2.3-2.6).

(J4) *The loss in Proposition 13.9 (2).* The source takes $\ell = (\frac12-\min(\beta_K,\beta_\iota-\beta_I))_+$, which
need not be an integer, while $\ell\in\mathbb N_0$ is required (the statement's "$\ell\in\mathbb N_0$ is specified
later", and integer b-regularity). Proposition 3.3 (2) takes the ceiling.

(J5) *Combination in Proposition 13.11 (1).* For $w_1$ the source takes $\eta = \max(\eta_0,\eta_1)$ in (13.22) and
states the $\mathscr I$-weight $\min(\gamma,\beta_\iota)-\epsilon$, which is the weight obtained with $\eta_0$. One
$\eta$ gives the $\mathscr I$-weight $\gamma-\eta$ and the $K$-weight $\beta_\iota-\gamma+\eta$; with $\eta_1$ the first
may be smaller than $\min(\gamma,\beta_\iota)-\epsilon$. The two memberships, at $\eta_0$ and at $\eta_1$, have the same
$\iota$-weight and combine by a partition of unity (proof of Proposition 3.3). The proof of Proposition 3.5 (1) does
this.

(J6) *Proposition 13.11 (2).* The source prints $\ell' =
\max(\lceil\delta_-+\epsilon,\beta_\iota-\beta_I-\delta,\beta_K-\delta)$, with an unbalanced bracket, and $\ell =
\lceil2\ell'+\delta\rceil$. Its first step trades $\ell'$ orders of $b+$-regularity for decay, from the space of
(13.16), whose weight $\delta-1$ means
$\sigma^j(\sigma\partial_\sigma)^lv\in|\sigma|^{1-\delta}L^2(|\frac{d\sigma}\sigma|)$, into the space of (13.8) with
weight $\delta+\ell'-1$, which means $|\sigma|^{\delta+\ell'-1}L^2(|\frac{d\sigma}\sigma|)$. The trade gives
$|\sigma|^{1-\delta-\ell'}L^2$ near $\infty$, which is contained in $|\sigma|^{\delta+\ell'-1}L^2$ there only if
$\ell'\ge1-\delta$. For $\delta = -\frac12$, $\beta_\iota-\beta_I\le\frac12$ and $\beta_K\le\frac12$, the printed
$\ell'$ is 1, less than $1-\delta = \frac32$, and the step fails: from $\sigma^{k+\ell}v\in|\sigma|^{\frac32}L^2$ it
asks $\sigma^{k+\ell-1}v\in|\sigma|^{-\frac12}L^2$. Proposition 3.5 (2) is proved directly from Lemma 2.2, with the loss
$\lceil(\frac32-\delta)_+\rceil+\lceil(\beta'-\frac12)_+\rceil$, $\beta' := \max(\beta_K,\beta_\iota-\beta_I)$, which is
not sharp. The source's final loss is not shown insufficient; only its intermediate step is.

(J7) *The numerals of Lemma 13.13 and (13.30) at $n = 4$.* With $\mu_b = |dx|/\langle x\rangle^4$, $L^2(\mu) =
\rho^2L^2(\mu_b)$, so a scattering decay order $\mathsf r$ is the b-weight $\mathsf r+2$. The source's shifts $\frac52$
and $\frac32$ in (13.23a)-(13.23b) become 3 and 2 (Lemma 4.1), its $\frac52$, $\frac72$, $\frac32$ in (13.30) become 3,
4, 2 (Lemma 4.6), and its threshold $\beta_{\mathrm{scf}}<1+\bar S$ becomes $\beta_{\mathrm{scf}}<\frac32+\bar S$. This
is a change of dimension, not a finding against the source.

(J8) *Corollary 13.14 (2).* The source asks that $\hat P(\sigma)$ be invertible on the open interval $I$. The bound on
$I\times\bar X$ needs constants uniform in $\sigma\in I$, which the cited estimates give on a compact set of invertible
$\sigma$; so Corollary 4.2 (2) asks for invertibility on $\bar I$. (On a bounded open $I$ with $\hat P(\sigma)$
invertible on $I$ but not at an endpoint, the norm of $\hat P(\sigma)^{-1}$ may be unbounded on $I$.)

(J9) *Proposition 13.16.* The source states it without proof ("we obtain"). Its loss
$k(1+\delta_\Gamma(-\epsilon))+\ell$ need not be an integer. Proposition 4.4 proves it from I.B Theorem 1.3 and Lemma
4.3, with the loss $k+\lceil k\delta\rceil+\ell$, $\delta = \delta_\Gamma(-\eta)$.

(J10) *Proposition 13.18.* (a) The source fixes one $c>0$ for all $k$. I.C Theorem 6.4 (4) gives radii $c_{j,k}$
depending on $j$ and $k$ (I.C Remark 6.7 (a)), so Proposition 4.7 has $c_k$ depending on $k$. (b) The source assumes
tf-admissibility at the one weight $\alpha+\frac32$ in the gap $(\beta_-,\beta_+)$ and states (13.31) for every
$\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}}$ in the gap with one $\ell$. This holds here too: I.C Theorem 6.4 (5) gives the
hypotheses at every weight of the gap and $\ell$ does not depend on the weight (the remark after Proposition 4.7); only
$c_k$ and the constants do.

(J11) *Proposition 13.20, the integration.* The source integrates by [Hin26b] Lemmas 2.12 and 2.23, which were not read;
Lemmas 3.2 and 5.3 replace them. The source's $h$ carries a term in
$H^{k+\ell-2,(((\frac32,0),\beta_I+\frac12),\beta_+)}_b$, which it then places in a space with $\mathscr I^+$-weight
$\beta''_I<\frac32$, where the $\rho_I^{3/2}$ term is already in the remainder; the expansion of $h$ is superfluous. In
Proposition 5.4 the term $\tilde P(\chi_I\rho_I^{3/2}u_0)$ lies in $H^{K-2,(b'',\beta_+)}_b$ as
$b''\le\beta'_I<\frac32+\kappa$.

(J12) *Proposition 13.20 at $n = 4$.* The indicial root at $\mathscr I^+$ is $\frac32 = \frac{n-1}2$ in place of 1, the
condition $\beta'_I<\frac32$ (that is $1+\kappa$ with $\kappa = \frac12$) becomes $\beta'_I<\frac32+\kappa$, and the
loss depends on $\kappa$ as well as on $\beta_I$, $\beta'_I$. The source's hypothesis $\beta_+<\beta_I$ is not used in
the proof of Proposition 5.4.

(J13) *Definition 13.19.* $u_{(1,0)}\in H^{k,\beta_+}_b(\mathscr I^+\cap\{t_*\ge1\})$ is a function on $\mathscr I^+$,
and $\chi_I\rho_I^\zeta u_{(1,0)}$ requires an extension of it off $\mathscr I^+$, which the source leaves unstated.
Definition 5.2 extends it independently of $\rho_I$ in the coordinates of $\mathcal C$.

### 7.3 The ninetieth verifier (D216)

The ninetieth verifier read sections 2-7 line by line with sympy checks ((5.1), the remainder of (5.2), (J1), (J2),
(J6), the Hardy chains of Lemma 2.3, Proposition 5.4's identities, Lemma 2.2). No major finding. Minor 1: in the proof
of Lemma 3.4 the inequality $dt_*/\langle t_*\rangle\le dT/T$ was reversed; replaced by the bound on $\{T\le2\}$ and
$\{T\ge2\}$, the conclusion unchanged. Minor 2: in the proof of (4.1b) the order of $Q_{\alpha\beta}$ is $(-N,\mathsf
r-\mathsf r_{\mathrm{out}}+\epsilon)$. Nits seated: the factor $1+j$ in Proposition 2.8 (1); $\ell$ in Corollary 4.2
made independent of $\epsilon$; the case $\mathrm{Re}\,\sigma_0 = 0$ of Corollary 4.2 (1); $C_0\ge1$ in Corollary 4.5;
the density step for Leibniz' rule; Proposition 4.7 at every weight of the gap, and (J10) (b) accordingly; (J6)'s scope
and the loss of Proposition 3.5 (2) not sharp; $\rho_+$ in the remark after Definition 5.2; the reference to a scratch
script; and (J1)'s last sentence (Lemma 13.6 fails at $\sigma = \infty$ as well). Nit 10, on the $\epsilon$ of
Proposition 3.3 (1)'s first case, needs no change: the case is invoked with the same $\epsilon$. The D213 repairs of
Part II.G were confirmed.

### 7.2 Sources

[Hin26c] P. Hintz, *(Non-)linear waves on asymptotically flat spacetimes. II*, arXiv:2606.28008v1, section 13 (pp.
243-260), read in the record's text extraction; with (13.16) for the spaces $H_{b+}$ and the statements of section 9
that section 13 cites, as carried in Parts I.A-I.C.

[Tay11a] cited by the source for Lemma 13.2 (Chapter 4, Proposition 5.3): not read, and not used.

[Li25] cited by the source for a direct proof of Lemma 13.4 when $|s|<\frac12$ (Lemma 3.12): not read, and not used.

[Hin26b] cited by the source for the integration of ordinary differential equations in the proof of Proposition 13.20
(sections 2.1-2.2, Lemmas 2.12 and 2.23): not read, and not used; Lemmas 3.2 and 5.3 are proved here.

[HV20] cited by the source for the extraction of radiation fields: not read, and not used.

[LX24] cited in Remark 13.1, and [Tat13], [Hin22a] in Remark 13.22: not read, and not used.

Parts I.A, I.B, I.C, II.A, II.C, II.E, II.F$'$ and II.G are cited by their sections, lemmas and equation numbers.
