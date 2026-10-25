# Part I.C. The spectral family at zero and low frequencies, at n = 4, on bundles

*Status.* Written out in full (D190). Not yet read by an independent verifier; nothing here is labelled proved. This
part replaces, for the statements it covers, the deductions of `../N1STAR-PROOF.md` 10.20 (a), (b) and (d) and the use
of [Hin26c] Theorem 9.41 in 10.20 (e), which read [Hin26c] sections 9.4-9.6 at n = 4 with $\alpha+2$ for
$\alpha+\frac32$ and cited the proofs. The source is [Hin26c] = P. Hintz, arXiv:2606.28008v1 (printed page = PDF page
$-4$). Parts I.A and I.B are `PART-I-SPECTRAL.md` and `PART-I-B-HIGHENERGY.md`, cited as I.A and I.B.

*What is proved here.* Theorem 3.1: [Hin26c] Theorem 9.36 at $n = 4$ on $E$ (the zero energy operator). Theorem 4.3:
Theorem 9.38 (the transition face normal operator). Corollary 5.2 and Proposition 5.3: Corollary 9.39 and Proposition
9.40. Theorem 6.4: Theorem 9.41 (uniform low-energy estimates), with Remark 9.42's augmentations and with an adjoint
estimate that the source does not state; its smallness may depend on the b-regularity order (Remark 6.7). Corollary 6.6:
Corollary 9.43. Section 7: uniformity in the operator. Every input is proved here or in Parts I.A-I.B, from the classical
facts of section 2.1, the scattering calculus of [HJS] that Part I.A READ, and the facts about Hankel functions READ in
[DLMF] (section 5.2).

*The changes at n = 4.* The shift of [Hin26c] Lemma 3.11 is $\frac n2 = 2$, so $\alpha+\frac32$ becomes $\alpha+2$ in
Theorems 9.36 and 9.41 and in Corollary 9.43, and $H^{\infty,\beta-\frac32}_b$ becomes $H^{\infty,\beta-2}_b$; in section
9.5, which the source states for every $n$, $\frac{n-1}2 = \frac32$, $\frac n2 = 2$ and $-n+2+\beta = -2+\beta$; the
Bessel order in Proposition 9.40 is $\ell+1$ and its weights are $(0,2)$. Seven findings against the source are listed in
section 8. None changes a statement; one (F6) is a gap in the proof of Corollary 9.43, which the adjoint estimate of
Theorem 6.4 closes.

*How it is organised.* Section 1 fixes the setting and the hypotheses. Section 2 proves the b-analysis used at the two
conic ends, at infinity and at the origin of the transition face. Section 3 proves Theorem 9.36, section 4 Theorem 9.38,
section 5 Corollary 9.39 and Proposition 9.40, section 6 the low-energy theorem and Corollary 9.43, section 7 their
uniformity. Section 8 lists the findings.

## 1. Setting and hypotheses

### 1.1 Data from Parts I.A and I.B

Everything of I.A section 1 is kept: $\bar X$, $\partial X$, $\partial_\sharp X$, $\tilde X$, the trivial bundle $E =
\tilde X\times\mathbb C^N$, fibre inner products $h$ (matrices $H$), the family $\hat P(\sigma) = \hat P(0)+\sigma T+
\sigma^2P_2$, the hypotheses (H1)-(H5), the thresholds $\bar S$, $\vartheta_{\mathcal H}$, $\vartheta_{\mathrm{in}}$, the
order pairs and the spaces $\bar H^{s,\mathsf r}$, $\dot H^{s,\mathsf r}$, $\mathcal X_\sigma$, $\mathcal Y_\sigma$,
$\mathcal X^*_\sigma$ of I.A Theorem 7.2. By I.A (1.1)-(1.2), on $\{\rho<\rho_1\}$,

$$\hat P(\sigma) = 2i\sigma\rho\big(\rho\partial_\rho-\tfrac32-S\big)+\rho^2P^{(0)}-i\sigma Q+\sigma^2g_{00},
\tag{1.1}$$

which is [Hin26c] (9.4) and (5.10) at $n = 4$. Every b-differential operator with coefficients smooth up to $\rho = 0$
can be written as a polynomial in $\rho\partial_\rho$ with coefficients that are operators on $\mathbb S^3$; for
$P^{(0)}$,

$$P^{(0)} = \sum_{j=0}^2A_j(\rho)(\rho\partial_\rho)^j,\qquad A_j\in C^\infty\big([0,\rho_1);\mathrm{Diff}^{2-j}(\mathbb
S^3;\mathrm{End}\,\mathbb C^N)\big).\tag{1.2}$$

By (H2), $P^{(0)}-((\rho D_\rho)^2+\Delta_{\mathbb S^3})\mathrm{Id}\in\mathrm{Diff}^1_b+\rho\,\mathrm{Diff}^2_b$, and the
second summand vanishes at $\rho = 0$, so $A_2(0) = -\mathrm{Id}$, $A_1(0) =: a\in C^\infty(\mathbb S^3;\mathrm{End}\,
\mathbb C^N)$ is of order 0, and $A_0(0) = \Delta_{\mathbb S^3}\mathrm{Id}+V+b$ with $V\in\mathrm{Diff}^1(\mathbb S^3;
\mathrm{End}\,\mathbb C^N)$ of order 1 and $b\in C^\infty$. The *normal operator* and the *indicial family* are

$$N(P^{(0)}) := \sum_jA_j(0)(\rho\partial_\rho)^j,\qquad I(\lambda) := \sum_jA_j(0)\lambda^j = -\lambda^2+a\lambda+
\Delta_{\mathbb S^3}+V+b,\qquad\lambda\in\mathbb C.\tag{1.3}$$

Then $N(P^{(0)})(\rho^\lambda v) = \rho^\lambda I(\lambda)v$ for $v\in C^\infty(\mathbb S^3;\mathbb C^N)$, and
$P^{(0)}-N(P^{(0)})\in\rho\,\mathrm{Diff}^2_b$. We write $S_0 := S(0,\cdot)$ and $H_0 := H(0,\cdot)$.

**Definition 1.1 (indicial roots and gaps, [Hin26c] Definition 3.12).** $\mathrm{spec}_b := \{\lambda\in\mathbb C:
\ker I(\lambda)\cap C^\infty(\mathbb S^3;\mathbb C^N)\ne0\}$, the *indicial roots* of $\hat P(0)$ (those of $\rho^{-2}
\hat P(0) = P^{(0)}$, as [Hin26c] defines them for $\rho^2\mathrm{Diff}^2_b$). An *indicial gap* is an open interval
$(\beta_-,\beta_+)\subset\mathbb R$, $-\infty\le\beta_-<\beta_+\le\infty$, containing no $\mathrm{Re}\,\lambda$ with
$\lambda\in\mathrm{spec}_b$.

By Lemma 2.4 below, $\mathrm{spec}_b$ is discrete with finitely many points in each vertical strip, so every real number
that is not the real part of a root lies in an indicial gap ([Hin26c] Remark 3.13).

### 1.2 The hypotheses of this part

(G) (*The gap.*) $\alpha\in\mathbb R$, and $\alpha+2$ lies in an indicial gap $I = (\beta_-,\beta_+)$ of $\hat P(0)$.

(Z) (*Zero energy.*) $\hat P(0):\mathcal X_0\to\mathcal Y_0$ of (3.1) below is invertible.

(TF) (*Transition face.*) $\hat P$ is tf-admissible with weight $\alpha+2$ (Definition 5.1).

The regularity order is a constant $s>\frac12+\vartheta_{\mathcal H}$ throughout (I.A Remark 1.1).

*Remarks.* (a) (G) is [Hin26c]'s "$\alpha+\frac32$ lies in an indicial gap" at $n = 4$: by Lemma 2.2 below,
$\bar H^{0,\alpha}_b = \rho^\alpha L^2(|dx|) = \rho^{\alpha+2}L^2(\mu_b)$, so the b-weight is $\alpha+2$, as the
record's 10.20 (iii) computed. (b) Which of the record's operators satisfy (G), (Z) and (TF), with which weights, is
computed in the record (10.15 for the indicial roots, kernels and cokernels; 10.17 and 10.23 for the transition face) and
is checked in Part VI; it is not repeated here. (c) Only (H1)-(H2) near $\partial X$ enter sections 4 and 5; (H3)-(H4)
enter through the interior estimates of section 3 and the low-energy argument of section 6; (H5) enters in section 7.

## 2. b-analysis at a conic end

### 2.1 What is used, and where it is stated

(K1) *Fourier analysis on $\mathbb R^m$.* $H^s(\mathbb R^m) := \{w:\langle\zeta\rangle^s\hat w\in L^2\}$. Three facts,
each proved here in a line. (i) For $\varphi\in\mathcal S(\mathbb R^m)$, $\|\varphi w\|_{H^s}\le(2\pi)^{-m}2^{|s|/2}
\|\langle\cdot\rangle^{|s|}\hat\varphi\|_{L^1}\|w\|_{H^s}$, by Peetre's inequality $\langle\zeta\rangle^s\le2^{|s|/2}
\langle\zeta-\eta\rangle^{|s|}\langle\eta\rangle^s$ and Young's inequality for $\widehat{\varphi w} =
(2\pi)^{-m}\hat\varphi*\hat w$; so the norm of multiplication by $\varphi$ is bounded by finitely many derivatives of
$\varphi$, if $\varphi$ is supported in a fixed compact set. (ii) For $\lambda>0$, $(w(\lambda\cdot))\hat{}\,(\zeta) =
\lambda^{-m}\hat w(\zeta/\lambda)$, so $\|w(\lambda\cdot)\|_{H^s}\le\lambda^{-m/2}\max(\lambda,\lambda^{-1})^{|s|}
\|w\|_{H^s}$. (iii) For $s>d+\frac m2$, $\sup_{|\beta|\le d}|\partial^\beta w|\le(2\pi)^{-m}\|\langle\zeta\rangle^{d-s}
\|_{L^2}\|w\|_{H^s}$, by Cauchy-Schwarz on $\hat w$.

(K2) *Interior elliptic estimates, uniformly.* Let $\mathcal F$ be a family of second-order operators on a neighbourhood
$\Omega'$ of a compact set $K\subset\mathbb R^4$, with $\mathrm{End}\,\mathbb C^N$-valued coefficients bounded in
$C^\infty(\bar\Omega')$ and principal symbols $p\,\mathrm{Id}$ with $|p(x,\zeta)|\ge c|\zeta|^2$. For $\varphi\in
C_c^\infty( \mathrm{int}\,K)$, $\tilde\varphi\in C_c^\infty(\Omega')$ equal to 1 near $K$, all $s$ and $N$, there is $C$
with $\|\varphi u\|_{H^s}\le C(\|\tilde\varphi Lu\|_{H^{s-2}}+\|\tilde\varphi u\|_{H^{-N}})$ for all $L\in\mathcal F$.
This is I.A Proposition 5.1 over a compact set, where the scattering calculus is the classical one (I.A section 2.1, last
paragraph), with I.A Theorem 8.1 for the uniformity: by Arzelà-Ascoli the closure of $\mathcal F$ in the coefficient
topology is compact, the coefficients depend continuously on its points, and the ellipticity bound persists.

(K3) *Rellich.* [HJS] Proposition 3.13 (I.A (C4)): for distributions supported in a fixed compact set and $s'>s$, the
inclusion $H^{s'}\hookrightarrow H^s$ is compact.

(K4) *The sphere.* $L^2(\mathbb S^3) = \bigoplus_{\ell\ge0}\mathcal H_\ell$, $\mathcal H_\ell$ the finite-dimensional
spaces of spherical harmonics of degree $\ell$, on which $\Delta_{\mathbb S^3} = \ell(\ell+2)$. For integers $m\ge0$,
$\|(1+\Delta)^{m/2}w\|_{L^2}$ is equivalent to the $H^m(\mathbb S^3)$ norm, and $H^{-m}(\mathbb S^3)$ is the dual of
$H^m(\mathbb S^3)$. Distributional solutions of elliptic equations with smooth coefficients on $\mathbb S^3$ with smooth
right side are smooth. These are (K2) in charts, with a partition of unity.

(K5) *Analytic Fredholm theorem* ([RS1] Theorem VI.14). If $D\subset\mathbb C$ is open and connected and $F:D\to \mathcal
L(\mathcal H)$ is analytic with compact values, and $\mathrm{Id}+F(\lambda_0)$ is invertible for one $\lambda_0$, then
$(\mathrm{Id}+F(\lambda))^{-1}$ exists for $\lambda$ off a discrete set $S\subset D$, and is meromorphic on $D$ with
finite-rank residues.

(K6) *Plancherel on $\mathbb R$ and Cauchy's theorem.* $\mathcal F_tw(\tau) := \int e^{-it\tau}w(t)\,dt$, so
$\|\mathcal F_tw\|^2 = 2\pi\|w\|^2$ for $L^2(\mathbb R;\mathcal H)$-valued $w$, $\mathcal H$ a Hilbert space.

### 2.2 Ends and dyadic pieces

An *end* is a neighbourhood of $\infty$ or of $0$ in $\mathbb R^4$, with *decay variable* $\varrho := |x|^{-1}$ (the end
at $\infty$, where $\varrho = \rho$) or $\varrho := |x|$ (the end at 0, used at the face ztf in section 4). Put $t :=
-\log\varrho$, so $t\to+\infty$ at the end, $\omega := x/|x|\in\mathbb S^3$, and $\mu_b := |d\varrho/\varrho\,d\omega| =
|dt\,d\omega|$. The b-vector fields are spanned over $C^\infty_b$ (below) by $\varrho\partial_\varrho = -\partial_t$ and
a fixed frame $Z_1,\dots,Z_6$ of vector fields on $\mathbb S^3$; they are dilation invariant.

Fix $\psi\in C_c^\infty((-1,1))$, $0\le\psi\le1$, with $\sum_{k\in\mathbb Z}\psi(\cdot-k) = 1$ on $\mathbb R$, and put
$\psi_k := \psi(t-k)$, $A := \{e^{-1}<|y|<e\}$, and $\Phi_k$ the dilation of $\mathbb R^4$ by $e^k$ (end at $\infty$) or
$e^{-k}$ (end at 0), which maps $A$ onto $\{k-1<t<k+1\}$. For a distribution $v$ supported in $\{t>t_0\}$ let $v_k :=
(\psi_kv)\circ\Phi_k$, supported in $\bar A$.

**Definition 2.1.** For $s,c\in\mathbb R$ and $v$ supported in $\{t>t_0\}$,
$$\|v\|^2_{H^s_{b,c}} := \sum_{k\ge\lfloor t_0\rfloor}e^{2ck}\|v_k\|^2_{H^s(\mathbb R^4)}.$$
$c$ is the *b-weight*: at $s = 0$ the norm is equivalent to $\|\varrho^{-c}v\|_{L^2(\mu_b)}$, because $\mu_b =
|y|^{-4}|dy|$ on $A$ pulls back under $\Phi_k$ to itself, $\varrho^{-c} = e^{ct}$ lies between $e^{c(k-1)}$ and
$e^{c(k+1)}$ on the $k$-th piece, and $\sum_k\psi_k = 1$ with at most two pieces overlapping. $C^\infty_b$ denotes the
functions $f$ with $(\varrho\partial_\varrho)^jZ^\alpha f$ bounded for all $j,\alpha$ (equivalently, $f\circ\Phi_k$
bounded in $C^\infty$ on a neighbourhood of $\bar A$ uniformly in $k$); it contains the functions smooth in
$(\varrho,\omega)$ up to $\varrho = 0$. $\mathrm{Diff}^m_b$ denotes the operators $\sum_{j+|\alpha|\le m}f_{j\alpha}
(\varrho\partial_\varrho)^jZ^\alpha$ with $f_{j\alpha}\in C^\infty_b$, $\mathrm{End}\,\mathbb C^N$-valued. $\mathcal A^c
:= \varrho^cC^\infty_b$.

**Lemma 2.2.** Let $s,c\in\mathbb R$; all distributions are supported in $\{t>t_0\}$.
(a) Another choice of $\psi$ gives an equivalent norm.
(b) For $f\in C^\infty_b$, $\|fv\|_{H^s_{b,c}}\le C\|v\|_{H^s_{b,c}}$, $C$ depending on finitely many seminorms of $f$;
and $\|\varrho^\gamma v\|_{H^s_{b,c+\gamma}}$ and $\|v\|_{H^s_{b,c}}$ are equivalent.
(c) $B\in\mathrm{Diff}^m_b$ maps $H^s_{b,c}$ to $H^{s-m}_{b,c}$, with norm bounded by finitely many seminorms of its
coefficients.
(d) The pairing $\langle v,w\rangle_{\mu_b} := \int\langle v,w\rangle_{\mathbb C^N}\,\mu_b$ extends continuously to
$H^s_{b,c}\times H^{-s}_{b,-c}$ and identifies $H^{-s}_{b,-c}$ with the dual of $H^s_{b,c}$; $C_c^\infty$ is dense in
both.
(e) For $s'>s$ and $c'>c$ the inclusion $H^{s'}_{b,c'}\hookrightarrow H^s_{b,c}$ is compact.
(f) For $s>d+2$, $|(\varrho\partial_\varrho)^jZ^\alpha v|\le C\varrho^c\|v\|_{H^s_{b,c}}$ for $j+|\alpha|\le d$. Hence
$H^\infty_{b,c} := \bigcap_sH^s_{b,c}\subset\mathcal A^c$; conversely $\mathcal A^c\subset H^\infty_{b,c-\epsilon}$ for
every $\epsilon>0$.
(g) For every $K\ge0$ and $N$, $\|v\|_{H^s_{b,c-1}}\le e^{-K}\|v\|_{H^s_{b,c}}+C_{K,N}\|v\|_{H^s_{b,-N}}$.
(h) For integers $m\ge0$, $\|v\|^2_{H^m_{b,c}}$ is equivalent to $\sum_{j+|\alpha|\le m}\|e^{ct}\partial_t^jZ^\alpha
v\|^2_{L^2(\mu_b)}$, and to $\int_{\mathbb R}\|\mathcal F_t(e^{ct}v)(\tau)\|^2_{H^m_{\langle\tau\rangle}}d\tau$, where
$\|w\|^2_{H^m_\mu} := \|(1+\mu^2+\Delta_{\mathbb S^3})^{m/2}w\|^2_{L^2(\mathbb S^3)}$. For $m<0$ the second equivalence
holds with $H^m_{b,c}$ normed as the dual of $H^{-m}_{b,-c}$.

*Proof.* (a) For a second choice $\psi'$, $(\psi'_kv)\circ\Phi_k = \sum_{|j-k|\le2}(\psi'_k\circ\Phi_k)(\psi_jv)\circ
\Phi_k$ and $(\psi_jv)\circ\Phi_k = v_j\circ(\Phi_j^{-1}\Phi_k)$, a dilation by $e^{\pm(k-j)}$, $|k-j|\le2$; (K1)
(i)-(ii) bound each term by $C\|v_j\|_{H^s}$, uniformly, and the weights $e^{2ck}$, $e^{2cj}$ are comparable. (b) Let
$\tilde\chi\in C_c^\infty(\{e^{-2}<|y|<e^2\})$ equal 1 near $\bar A$. Then $(fv)_k = \tilde\chi(f\circ\Phi_k)v_k$, and
$\tilde\chi(f\circ\Phi_k)$ is bounded in $C_c^\infty$ uniformly in $k$, so (K1) (i) applies. For $\varrho^\gamma$,
$\varrho^\gamma\circ\Phi_k = e^{-\gamma k}|y|^{\mp\gamma}$, and $|y|^{\mp\gamma}$ is smooth near $\bar A$. (c) The
operators $\varrho\partial_\varrho$ and $Z_i$ commute with the dilations, so $(Bv)_k = \sum_{|j-k|\le1}(\psi_k\circ
\Phi_k)\,B^{(k)}\big(v_j\circ\Phi_j^{-1}\Phi_k\big)$ with $B^{(k)}$ the operator with coefficients $f_{j\alpha}\circ
\Phi_k$, bounded in $C^\infty$ near $\bar A$ uniformly in $k$; a differential operator of order $m$ with such
coefficients maps compactly supported elements of $H^s$ to $H^{s-m}$ boundedly, by (K1) (i) and
$\|\partial_iw\|_{H^{s-1}} \le\|w\|_{H^s}$. (d) Let $J:v\mapsto(e^{ck}v_k)_k$, an isometry of $H^s_{b,c}$ into
$\ell^2(\mathbb Z;H^s)$, and $L: (w_k)_k\mapsto\sum_k e^{-ck}(\tilde\chi w_k)\circ\Phi_k^{-1}$. Then $LJ = \mathrm{Id}$
(as $\tilde\chi = 1$ on the support of $v_k$ and $\sum_k\psi_k = 1$), and $L$ is bounded from $\ell^2(H^s)$ to
$H^s_{b,c}$ by (a)-(b), as each point lies in at most three supports. The pairing: $\langle v,w\rangle_{\mu_b} =
\sum_k\langle\psi_kv,w\rangle_{\mu_b} = \sum_k\int\langle v_k,(\tilde\chi w)\circ\Phi_k\rangle|y|^{-4}dy$, and
$\|(\tilde\chi w)\circ\Phi_k\|_{H^{-s}}\le C\sum_{|j-k|\le2}\|w_j\|_{H^{-s}}$, so Cauchy-Schwarz gives $|\langle
v,w\rangle_{\mu_b}|\le C\|v\|_{H^s_{b,c}}\|w\|_{ H^{-s}_{b,-c}}$. Conversely a bounded functional $\ell$ on $H^s_{b,c}$
gives the functional $\ell\circ L$ on $\ell^2(H^s)$, represented by $(g_k)\in\ell^2(H^{-s})$; then $\ell(v) = \ell(LJv) =
\langle v,w\rangle_{\mu_b}$ with $w := \sum_k e^{ck}(|y|^4\tilde\chi g_k)\circ\Phi_k^{-1}$, and $\|w\|_{H^{-s}_{b,-c}}\le
C\|(g_k)\|$ by the same estimate. Density: truncate the sum over $k$ and mollify each piece. (e) For $K\in\mathbb N$, the
pieces with $k\le K$ form a compact map by (K3); for the rest, $\sum_{k>K}e^{2ck}\|v_k\|^2_{H^s}\le
e^{-2(c'-c)K}\|v\|^2_{H^{s'}_{b,c'}}$. A norm-limit of compact maps is compact. (f) (K1) (iii) on each piece gives
$|\partial_y^\beta v_k|\le Ce^{-ck}\|v\|$, and on $A$ the fields $\varrho\partial_\varrho$, $Z_i$ are combinations of
$\partial_{y_j}$ with smooth coefficients, the same for every $k$; $\varrho^c$ is comparable to $e^{-ck}$ there.
Conversely, for $v\in\mathcal A^c$, $\|v_k\|_{H^m}\le C_me^{-ck}$, and $\sum_ke^{2(c-\epsilon)k}e^{-2ck}<\infty$. (g)
Split the sum at $k = K$: for $k\ge K$, $e^{2(c-1)k}\le e^{-2K}e^{2ck}$; the finitely many $k<K$ give $e^{2(c-1)k}\le
C_{K,N}e^{-2Nk}$. (h) On each piece, $\|w\|_{H^m(\mathbb R^4)}$ is equivalent to $\sum_{|\beta|\le m}\|\partial_y^\beta
w\|_{L^2}$, and on $A$ the coordinate change $y\mapsto(t,\omega)$ is a fixed diffeomorphism, which with Leibniz's rule
for $\psi_k$ gives the first equivalence. For the second, by Plancherel in $t$ (K6) and (K4) on $\mathbb S^3$,
$\sum_{j+|\alpha|\le m}\|\partial_t^jZ^\alpha u\|^2$ is equivalent to $\int\sum_\ell(1+\tau^2+\ell(\ell+2))^m \|(\mathcal
F_tu)_\ell(\tau)\|^2d\tau$, $(\cdot)_\ell$ the projection to $\mathcal H_\ell$, with $u := e^{ct}v$ and
$[\partial_t,e^{ct}] = ce^{ct}$; and $(1+\tau^2+\lambda)^m$ is equivalent to $\sum_{j\le m}\tau^{2j}(1+\lambda)^{m-j}$.
For $m<0$ both sides are the dual norms of the case $-m$, by (d) and Plancherel. $\square$

### 2.3 The Mellin transform

For $v$ supported in $\{t>t_0\}$ with $e^{c_0t}v\in L^2(\mu_b)$ define the $L^2(\mathbb S^3)$-valued function
$$(\mathcal Mv)(\lambda) := \int_{\mathbb R}e^{\lambda t}v(t,\cdot)\,dt = \int_0^\infty\varrho^{-\lambda}v\,
\frac{d\varrho}\varrho.$$
For $\mathrm{Re}\,\lambda<c_0$ the integral converges absolutely (Cauchy-Schwarz with $e^{(\mathrm{Re}\lambda-c_0)t}\in
L^2((t_0,\infty))$), and $\mathcal Mv$ is holomorphic there. On the line $\mathrm{Re}\,\lambda = x\le c_0$,
$\mathcal Mv(x+i\tau) = \mathcal F_t(e^{xt}v)(-\tau)$, so by (K6)

$$\int_{\mathbb R}\|\mathcal Mv(x+i\tau)\|^2d\tau = 2\pi\|e^{xt}v\|^2\le2\pi e^{2(x-c_0)t_0}\|e^{c_0t}v\|^2,\qquad
x\le c_0,\tag{2.1}$$

the last bound because $e^{xt}\le e^{(x-c_0)t_0}e^{c_0t}$ for $t>t_0$. As $x\uparrow c_0$, $e^{xt}v\to e^{c_0t}v$ in
$L^2$ by dominated convergence, so the values on $\mathrm{Re}\,\lambda = c_0$ are the $L^2$ limits of those on nearby
lines. Integration by parts gives $\mathcal M((\varrho\partial_\varrho)v) = \mathcal M(-\partial_tv) = \lambda\,\mathcal
Mv$, and operators on $\mathbb S^3$ commute with $\mathcal M$. By Lemma 2.2 (h), for integers $m$,

$$\|v\|^2_{H^m_{b,c}}\ \text{is equivalent to}\ \int_{\mathbb R}\|\mathcal
Mv(c+i\tau)\|^2_{H^m_{\langle\tau\rangle}}d\tau.
\tag{2.2}$$

**Lemma 2.3 (moving the line).** Let $v$ be supported in $\{t>t_0\}$, $e^{c_0t}v\in L^2$, and suppose that $\mathcal Mv$
extends holomorphically from $\{\mathrm{Re}\,\lambda<c_0\}$ to $\{\mathrm{Re}\,\lambda<c_1\}$, $c_1>c_0$, with
$K := \sup_{c_0\le x<c_1}\int\|\mathcal Mv(x+i\tau)\|^2d\tau<\infty$. Then $e^{c_1t}v\in L^2$ and
$\|e^{c_1t}v\|^2\le K/2\pi$.

*Proof.* The extension is continuous on $\mathrm{Re}\,\lambda = c_0$, so it agrees there with the $L^2$ limits above. Let
$\varphi\in C_c^\infty(\mathbb R\times\mathbb S^3)$ and $\Psi(\lambda) := \int e^{-\lambda t}\bar\varphi(t,\cdot)\,dt$,
entire, with $\|\Psi(x+i\tau)\|_{L^2(\mathbb S^3)}\le C_X\langle\tau\rangle^{-2}$ for $|x|\le X$ (integrate by parts
twice in $t$). Put $g(\lambda) := \int_{\mathbb S^3}\langle\mathcal
Mv(\lambda),\overline{\Psi(\lambda)}\rangle\,d\omega$, holomorphic on $\{\mathrm{Re}\,\lambda<c_1\}$. For $x\le c_0$,
Parseval for $e^{xt}v$ and $e^{-xt}\varphi$ gives $\langle v,\varphi\rangle_{\mu_b} = \frac1{2\pi}\int_{\mathbb
R}g(x+i\tau)\,d\tau$. Fix $x_0<c_0$ and $x_1\in[c_0,c_1)$. $\int_{x_0}^{x_1}\int_{\mathbb R}|g(s+iT)|\,dT\,ds<\infty$ by
Cauchy-Schwarz, (2.1) and the definition of $K$, so there are $T_j\to+\infty$ and $T'_j\to-\infty$ with
$\int_{x_0}^{x_1}|g(s+iT_j)|\,ds\to0$, and likewise at $T'_j$. Cauchy's theorem on the rectangles
$[x_0,x_1]\times[T'_j,T_j]$ then gives $\int g(x_1+i\tau)\,d\tau = \int g(x_0+i\tau)\,d\tau$, so $|\langle
v,\varphi\rangle_{\mu_b}|\le\frac1{2\pi}\big(\int\|\mathcal Mv(x_1+i\tau)\|^2d\tau\big)^{1/2}\big(\int
\|\Psi(x_1+i\tau)\|^2d\tau\big)^{1/2}\le(K/2\pi)^{1/2}\|e^{-x_1t}\varphi\|$, by (K6) for $\Psi(x_1+i\cdot) =
\overline{\mathcal F_t(e^{-x_1t}\varphi)}$ up to reflection. So $\|e^{x_1t}v\|^2\le K/2\pi$; let $x_1\uparrow c_1$
(monotone convergence on $\{t>0\}$, dominated convergence on $\{t_0<t\le0\}$). $\square$

### 2.4 The indicial family

**Lemma 2.4.** Let $J(\lambda) = -\lambda^2+a_J\lambda+\Delta_{\mathbb S^3}+V_J+b_J$, with $a_J,b_J\in C^\infty(\mathbb
S^3;\mathrm{End}\,\mathbb C^N)$ and $V_J\in\mathrm{Diff}^1(\mathbb S^3;\mathrm{End}\,\mathbb C^N)$, and let $m$ be an
integer.
(a) For $X>0$ there is $\mu_0$ such that for $|\mathrm{Re}\,\lambda|\le X$ and $|\mathrm{Im}\,\lambda|\ge\mu_0$,
$J(\lambda):H^m(\mathbb S^3)\to H^{m-2}(\mathbb S^3)$ is invertible with $\|J(\lambda)^{-1}\|_{H^{m-2}_\mu\to
H^m_\mu}\le2$, $\mu := \mathrm{Im}\,\lambda$.
(b) $\mathrm{spec}_J := \{\lambda:\ker J(\lambda)\cap C^\infty\ne0\}$ is discrete, with finitely many points in each
strip $\{|\mathrm{Re}\,\lambda|\le X\}$; off it $J(\lambda):H^m\to H^{m-2}$ is invertible, and $J^{-1}$ is meromorphic on
$\mathbb C$.
(c) If $[x_0,x_1]\cap\mathrm{Re}\,\mathrm{spec}_J = \emptyset$, then $\sup\{\|J(\lambda)^{-1}\|_{H^{m-2}_\mu\to
H^m_\mu}:x_0\le\mathrm{Re}\,\lambda\le x_1\}<\infty$, $\mu = \mathrm{Im}\,\lambda$.

*Proof.* (a) Write $\lambda = x+i\mu$, so $-\lambda^2 = \mu^2-x^2-2ix\mu$ and $J(\lambda) = (1+\mu^2+\Delta)+R$ with $R
:= -1-x^2-2ix\mu+a_J(x+i\mu)+V_J+b_J$. By (K4) and the spectral theorem, $1+\mu^2+\Delta$ is an isometry $H^m_\mu\to
H^{m-2}_\mu$, and $\|w\|_{H^{m-j}_\mu}\le(1+\mu^2)^{-j/2}\|w\|_{H^m_\mu}$ for $j\ge0$. Multiplication by a smooth
function is bounded on $H^k_\mu$ uniformly in $\mu$, for every integer $k$: for $k\ge0$ because $\|w\|^2_{H^k_\mu}$ is
equivalent, uniformly, to $\sum_{j\le k}\mu^{2(k-j)}\|w\|^2_{H^j}$, by Leibniz's rule; for $k<0$ by duality. Likewise
$V_J$ maps $H^k_\mu$ to $H^{k-1}_\mu$ boundedly, uniformly in $\mu$ (for $k\ge1$ directly, for $k\le0$ by duality with
$V_J^*$). So $\|Rw\|_{H^{m-2}_\mu}\le C(1+|\mu|)\|w\|_{H^{m-2}_\mu}+C\|w\|_{H^{m-1}_\mu}\le
C'(1+|\mu|)^{-1}\|w\|_{H^m_\mu}$, and a Neumann series inverts $J(\lambda)$ with the stated bound once
$C'(1+|\mu|)^{-1}\le\frac12$. (b) $J(\lambda) = (1+\Delta)(\mathrm{Id}+F(\lambda))$ on $H^m$, with $F(\lambda) :=
(1+\Delta)^{-1}(J(\lambda)-1-\Delta)$ compact on $H^m$ (it maps $H^m$ to $H^{m+1}$, and (K3)-(K4) give compactness on
$\mathbb S^3$) and polynomial in $\lambda$. By (a), $\mathrm{Id}+F(\lambda)$ is invertible for some $\lambda$, so (K5)
applies on $D = \mathbb C$. $\mathrm{Id}+F(\lambda)$ is Fredholm of index 0, so it fails to be invertible exactly when it
has a kernel; a kernel element of $J(\lambda)$ in $H^m$ is smooth by (K4), so the exceptional set is $\mathrm{spec}_J$
for every $m$. In a strip it lies in $\{|\mathrm{Im}\, \lambda|\le\mu_0\}$ by (a), a compact set, which meets the
discrete set in finitely many points. (c) On the part with $|\mathrm{Im}\,\lambda|\ge\mu_0$ the bound is 2. The rest is
compact, $J^{-1}$ is continuous there, and the $\mu$-weighted norms are equivalent to the unweighted ones for
$|\mu|\le\mu_0$. $\square$

For the end at $\infty$ the operator is $P^{(0)}$, with $\varrho\partial_\varrho = \rho\partial_\rho$, and $\mathcal M$
turns $N(P^{(0)})$ into multiplication by $I(\lambda)$, of the form of Lemma 2.4 with $\mathrm{spec}_I =
\mathrm{spec}_b$.

### 2.5 The model estimates

Let $L = \sum_{j=0}^2B_j(\varrho)(\varrho\partial_\varrho)^j$ on $\{t>t_0\}$, $B_j\in C^\infty([0,e^{-t_0});\mathrm{Diff}
^{2-j}(\mathbb S^3;\mathrm{End}\,\mathbb C^N))$, with *normal operator* $N(L) := \sum_jB_j(0)(\varrho\partial_\varrho)^j$
whose Mellin symbol $J(\lambda) := \sum_jB_j(0)\lambda^j$ has the form of Lemma 2.4. Then $L\in\mathrm{Diff}^2_b$ and
$L-N(L)\in\varrho\,\mathrm{Diff}^2_b$. Assume $L$ is *b-elliptic*: in the coordinates $(t,\omega)$ its principal symbol
is $p\,\mathrm{Id}$ with $|p|\ge c|(\tau,\eta)|^2$ on $\{t>t_0\}$, uniformly. (For $N(L)$ the principal symbol is that of
$-\partial_t^2+\Delta_{\mathbb S^3}$.) Cut-offs below are functions of $t$, with $\tilde\chi = 1$ near the support of
$\chi$.

**Lemma 2.5 (the b-elliptic estimate).** For all $s$, $c$, $N$ there is $C$ with
$\|\chi v\|_{H^s_{b,c}}\le C(\|\tilde\chi Lv\|_{H^{s-2}_{b,c}}+\|\tilde\chi v\|_{H^{-N}_{b,c}})$.

*Proof.* Under $\Phi_k$ the operator $L$ becomes $L^{(k)}$ on a neighbourhood of $\bar A$, with coefficients bounded in
$C^\infty$ uniformly in $k$ and principal symbols elliptic with a uniform bound, as $\varrho\partial_\varrho$ and $Z_i$
are dilation invariant and on $A$ they are combinations of $\partial_{y_j}$ with fixed smooth coefficients. (K2) applied
to the family $\{L^{(k)}\}$, with $\varphi := \psi_k\circ\Phi_k$ (supported in $\bar A$) and $\tilde\varphi$ equal to 1
near $\bar A$, bounds $\|(\psi_k\chi v)\circ\Phi_k\|_{H^s}$ by the corresponding pieces of $Lv$ and of $v$ on the
neighbouring $k$, uniformly. Multiply by $e^{2ck}$ and sum; the commutators of $L$ with $\chi$ are absorbed into the
$\tilde\chi$ terms, as $\tilde\chi = 1$ near $\mathrm{supp}\,\chi$ and Lemma 2.2 (a)-(c) holds. $\square$

**Lemma 2.6 (the normal operator estimate, [Hin26c] (3.47)).** Let $c\notin\mathrm{Re}\,\mathrm{spec}_J$ and $m\in\mathbb
Z$. Then $\|v\|_{H^m_{b,c}}\le C\|N(L)v\|_{H^{m-2}_{b,c}}$ for $v$ supported in $\{t>t_0\}$, and
$$\|\chi v\|_{H^m_{b,c}}\le C\big(\|\tilde\chi Lv\|_{H^{m-2}_{b,c}}+\|\tilde\chi v\|_{H^m_{b,c-1}}\big).\tag{2.3}$$

*Proof.* By (2.2), Lemma 2.2 (h) and $\mathcal M(N(L)v)(c+i\tau) = J(c+i\tau)\mathcal Mv(c+i\tau)$, the first estimate is
Lemma 2.4 (c) with $x_0 = x_1 = c$. For (2.3) apply it to $\chi v$: $N(L)\chi v = \chi Lv+[L,\chi]v+(N(L)-L)\chi v$. The
commutator has coefficients supported in $\mathrm{supp}\,d\chi$, a compact set of $t$, where all weights are equivalent;
$N(L)-L\in\varrho\,\mathrm{Diff}^2_b$ maps $H^m_{b,c-1}$ to $H^{m-2}_{b,c}$ by Lemma 2.2 (b)-(c). $\square$

**Lemma 2.7 (improving the weight).** Let $(c_-,c_+)$ contain no real part of a point of $\mathrm{spec}_J$, $c\in
(c_-,c_+)$, and suppose $\tilde\chi v\in H^\infty_{b,c}$ and $\tilde\chi Lv\in H^\infty_{b,c'}$ for every $c'<c_+$. Then
$\chi v\in H^\infty_{b,c'}$ for every $c'<c_+$, so $\chi v\in\bigcap_{c'<c_+}\mathcal A^{c'}$.

*Proof.* Take nested cut-offs $\tilde\chi = \chi_0,\chi_1,\dots,\chi_M = \chi$, each equal to 1 near the support of the
next. Suppose $\chi_iv\in H^\infty_{b,c_i}$ with $c_i\in(c_-,c_+)$, and fix $x_1<\min(c_i+1,c_+)$. Then $f :=
N(L)\chi_{i+1} v = \chi_{i+1}Lv+[L,\chi_{i+1}]v+(N(L)-L)\chi_{i+1}v$ lies in $H^\infty_{b,c''}$ with $c'' :=
\min(c_i+1,\frac12(x_1+c_+))> x_1$: the first term by hypothesis, the second because it is supported in a compact set of
$t$ inside $\{\chi_i = 1\}$, the third by Lemma 2.2 (b)-(c). So $\mathcal Mf$ is holomorphic on
$\{\mathrm{Re}\,\lambda<c''\}$ with line norms bounded by (2.1), and $J(\lambda)\mathcal M(\chi_{i+1}v)(\lambda) =
\mathcal Mf(\lambda)$ for $\mathrm{Re}\,\lambda<c_i$. The strip $\{c_i-\epsilon\le\mathrm{Re}\,\lambda\le x_1'\}$,
$x_1<x_1'<c''$, contains no root for $\epsilon$ small, so $J^{-1}\mathcal Mf$ is holomorphic on its interior, agrees with
$\mathcal M(\chi_{i+1}v)$ near $\mathrm{Re}\,\lambda = c_i-\epsilon$, and has line norms bounded by Lemma 2.4 (c) and
(2.1). Lemma 2.3, with $c_0 := c_i-\epsilon$ and $c_1 := x_1'$, gives $\chi_{i+1}v\in H^0_{b,x_1}$; Lemma 2.5 at the
weight $x_1$, with $Lv\in H^\infty_{b,x_1}$ on the support of $\chi_{i+1}$, gives $\chi_{i+2}v\in H^\infty_{b,x_1}$. Each
two steps raise the weight by any amount less than $\min(1,c_+-c_i)$, so finitely many reach every $c'<c_+$. The last
claim is Lemma 2.2 (f). $\square$

### 2.6 The spaces on $\bar X$

Fix $R_1>r_e+1$ so large that $\{r\ge R_1\}\subset\{\rho<\rho_1\}$ and $P^{(0)}$ is b-elliptic on $\{r\ge\frac12R_1\}$
(possible by (H2), its b-principal symbol being that of $(\rho D_\rho)^2+\Delta_{\mathbb S^3}$ plus $O(\rho)$), and
$\chi_\partial = \chi_\partial(r)$ with $\chi_\partial = 0$ on $\{r\le R_1\}$ and $\chi_\partial = 1$ on $\{r\ge2R_1\}$.

**Definition 2.8 ([Hin26c] (3.72)'s spaces at $n = 4$).** For $s,a\in\mathbb R$,
$$\|u\|^2_{\bar H^{s,a}_b} := \|(1-\chi_\partial)u\|^2_{\bar H^s}+\|\chi_\partial u\|^2_{H^s_{b,a+2}},$$
with $\bar H^s$ extendible at $\partial_\sharp X$ (I.A section 6.1) and $H^s_{b,a+2}$ of Definition 2.1 at the end at
$\infty$; $\dot H^{s,a}_b$ is defined with $\dot H^s$ (supported at $\partial_\sharp X$) in the first term. $\bar
H^{(s;k),a}_b := \bar H^{s+k,a}_b$ (for b-spaces, b-regularity is regularity).

By Lemma 2.2, near $\partial X$ the norm is that of $\rho^aH^s_b(|dx|) = \rho^{a+2}H^s_b(\mu_b)$, as $|dx| =
\rho^{-4}\mu_b$; the b-weight is $a+2$. The space does not depend on $R_1$ or $\chi_\partial$, up to equivalent norms.

**Lemma 2.9.** (a) The $L^2(|dx|)$ pairing identifies the dual of $\bar H^{s,a}_b$ with $\dot H^{-s,-a}_b$. (b) For
$s'>s$, $a'>a$, $\bar H^{s',a'}_b\hookrightarrow\bar H^{s,a}_b$ is compact. (c) ([Hin26c] (3.72) at $n = 4$.) $\bar
H^{d+3,a}_b\subset\rho^{a+2}C^d_b$ near $\partial X$; in particular $\bar H^{\infty,\beta-2}_b\subset\mathcal A^\beta$
near $\partial X$, and $\mathcal A^\beta\subset\bar H^{\infty,\beta-2-\epsilon}_b$ near $\partial X$ for $\epsilon>0$.
(d) $\hat P(0)$ maps $\bar H^{s,a}_b$ to $\bar H^{s-2,a+2}_b$ and $\dot H^{s,a}_b$ to $\dot H^{s-2,a+2}_b$.

*Proof.* (a) Near $\partial X$, $\langle u,v\rangle_{|dx|} = \langle u,\rho^{-4}v\rangle_{\mu_b}$, and
$v\mapsto\rho^{-4}v$ maps $H^{-s}_{b,-a+2}$ (the b-weight of $\dot H^{-s,-a}_b$) onto $H^{-s}_{b,-a-2}$, the dual of
$H^s_{b,a+2}$ (Lemma 2.2 (b), (d)); in the interior it is I.A Lemma 6.1 (b); glue with $\chi_\partial$. (b) Lemma 2.2 (e)
and (K3). (c) Lemma 2.2 (f) with $d+3>d+2$. (d) Near $\partial X$, $\hat P(0) = \rho^2P^{(0)}$ and Lemma 2.2 (b)-(c).
$\square$

## 3. The zero energy operator ([Hin26c] Theorem 9.36 at $n = 4$)

With $s$ and $\alpha$ as in section 1.2 let

$$\mathcal X_0 := \{u\in\bar H^{s,\alpha}_b:\hat P(0)u\in\bar H^{s-1,\alpha+2}_b\},\qquad\mathcal Y_0 := \bar
H^{s-1,\alpha+2}_b,\qquad\mathcal X^*_0 := \{v\in\dot H^{1-s,-\alpha-2}_b:\hat P(0)^{*h}v\in\dot H^{-s,-\alpha}_b\},
\tag{3.1}$$

Hilbert spaces with the graph norms; $\mathcal X_0\to\mathcal Y_0$ is [Hin26c] (9.108), and $\mathcal Y_0^* = \dot
H^{1-s,-\alpha-2}_b$ by Lemma 2.9 (a).

**Theorem 3.1 ([Hin26c] Theorem 9.36 at $n = 4$, on $E$).** Assume (H1)-(H4) and (G), with $s>\frac12+
\vartheta_{\mathcal H}$ constant.

(1) (*Fredholm estimates.*) For every $N$ there is $C$ with

$$\|u\|_{\bar H^{s,\alpha}_b}\le C\big(\|\hat P(0)u\|_{\bar H^{s-1,\alpha+2}_b}+\|u\|_{\bar H^{-N,-N}_b}\big),\qquad
u\in\mathcal X_0,\tag{3.2}$$

$$\|v\|_{\dot H^{1-s,-\alpha-2}_b}\le C\big(\|\hat P(0)^{*h}v\|_{\dot H^{-s,-\alpha}_b}+\|v\|_{\dot H^{-N,-N}_b}
\big),\qquad v\in\mathcal X^*_0.\tag{3.3}$$

$\hat P(0):\mathcal X_0\to\mathcal Y_0$ is Fredholm, and the annihilator of its range in $\mathcal Y_0^*$ is $\ker_{
\mathcal X^*_0}\hat P(0)^{*h}$.

(2) (*Kernel.*) Every $u\in\bar H^{s,\alpha}_b$ with $\hat P(0)u = 0$ is smooth up to $\partial_\sharp X$ and lies in
$\mathcal A^\beta$ near $\partial X$ for every $\beta<\beta_+$.

(3) (*Independence.*) The kernel and the annihilator of the range do not depend on $s>\frac12+\vartheta_{\mathcal H}$
nor on $\alpha$ with $\alpha+2\in I$; nor, therefore, does the index.

(4) (*Invertibility.*) If (Z) holds for one such pair $(s,\alpha)$, it holds for all, and then (3.2)-(3.3) hold without
their last terms.

The weight on $\hat P(0)^{*h}v$ in (3.3) is $-\alpha$, the dual of the weight $\alpha$ of the domain; [Hin26c] (9.107)
prints $-\alpha-2$ (section 8, (F3)).

### 3.1 Proof of (1)

*The interior.* Let $\chi$, $\chi_1$, $b'<b''$ be as in I.A Corollary 6.5, $\chi_{\mathrm{far}} := 1-\chi$, and
$\varphi_j\in C_c^\infty(\{r<jR_1\})$ equal to 1 on $\{r\le(j-1)R_1\}$, $j = 3,4,5$. Run the pieces (A), (B) and (F) of
I.A section 7.1 at $\sigma = 0$ for $\varphi_3\chi_{\mathrm{far}}u$: Proposition 4.2 (1) at the horizon ($\sigma = 0$
lies in its compact sets $\mathcal D\subset\{\mathrm{Im}\,\sigma\ge0\}$), Proposition 5.2 along the curves of (H4), which
lie over $\{r\le r_e\}$, and Proposition 5.1 on the rest of fibre infinity over $\{r<3R_1\}$; at finite frequencies over
a compact set every operator of order $-\infty$ is bounded by $\|u\|_{H^{-N}}$ there. With I.A (6.1) at $\sigma = 0$ for
$\chi u$ this gives, with $s>s_0>\frac12+\vartheta_{\mathcal H}$,

$$\|(1-\chi_\partial)u\|_{\bar H^s}\le C\big(\|\hat P(0)u\|_{\bar H^{s-1}(\{r<4R_1\})}+\|\varphi_4u\|_{\bar H^{s_0}}+
\|\varphi_4u\|_{\bar H^{-N}}\big),$$

as $1-\chi_\partial = (1-\chi_\partial)(\chi+\varphi_3\chi_{\mathrm{far}})$. By (K3) and Ehrling's lemma,
$\|\varphi_4u\|_{\bar H^{s_0}}\le\delta\|\varphi_5u\|_{\bar H^s}+C_\delta\|\varphi_5u\|_{\bar H^{-N}}$, and over
$\{r<5R_1\}$ the norms of $\bar H^{s,\alpha}_b$ and $\bar H^s$ are equivalent. So

$$\|(1-\chi_\partial)u\|_{\bar H^s}\le C\|\hat P(0)u\|_{\bar H^{s-1,\alpha+2}_b}+C\delta\|u\|_{\bar H^{s,\alpha}_b}+
C_\delta\|u\|_{\bar H^{-N,-N}_b}.\tag{3.4}$$

*Near $\partial X$.* Let $\tilde\chi_\partial$ be supported in $\{r>\frac12R_1\}$ and equal to 1 near
$\mathrm{supp}\,\chi_\partial$. Lemma 2.5 for $L = P^{(0)}$ at the b-weight $\alpha+2$, with $\tilde\chi_\partial
P^{(0)}u = \tilde\chi_\partial\rho^{-2}\hat P(0)u$, gives

$$\|\chi_\partial u\|_{H^s_{b,\alpha+2}}\le C\big(\|\hat P(0)u\|_{\bar H^{s-2,\alpha+2}_b}+\|\tilde\chi_\partial u\|_{
H^{-N}_{b,\alpha+2}}\big),$$

the b-weight of $\bar H^{s-2,\alpha+2}_b$ being $\alpha+4$ and Lemma 2.2 (b) moving $\rho^{-2}$. Choose $N\in\mathbb N$.
By Lemma 2.6 at $c = \alpha+2$ (not a real part of a root, by (G)), with cut-offs $\tilde\chi_\partial$ and
$\tilde\chi'$, and Lemma 2.2 (g),

$$\|\tilde\chi_\partial u\|_{H^{-N}_{b,\alpha+2}}\le C\|\hat P(0)u\|_{\bar H^{-N-2,\alpha+2}_b}+Ce^{-K}\|\tilde\chi'u\|_{
H^{-N}_{b,\alpha+2}}+C_K\|\tilde\chi'u\|_{H^{-N}_{b,-N}}.$$

Here $\tilde\chi'-\tilde\chi_\partial$ has compact support in $\{r>\frac14R_1\}$, where all weights are equivalent, so
$\|\tilde\chi'u\|_{H^{-N}_{b,\alpha+2}}\le\|\tilde\chi_\partial u\|_{H^{-N}_{b,\alpha+2}}+C\|u\|_{\bar H^{-N,-N}_b}$, and
$\|\tilde\chi'u\|_{H^{-N}_{b,-N}}\le C\|u\|_{\bar H^{-N,-N}_b}$. Take $K$ with $Ce^{-K}\le\frac12$; the left side is
finite because $u\in\bar H^{s,\alpha}_b$, so it absorbs the middle term. With (3.4), and $\delta$ small, this proves
(3.2).

*The adjoint.* Let $v\in\mathcal X^*_0$. In the interior run the adjoint chain of I.A section 7.1 at $\sigma = 0$ over
$\{r<4R_1\}$: (6.2) at the artificial boundary, which needs nothing but $\hat P(0)^{*h}v$; (B*), Proposition 5.2 for
$\hat P(0)^{*h}$ with the backward field from there to the horizon; (A*), Proposition 4.2 (2), whose $E$-term lies in the
region of (B*); and (F). No a priori term arises. Near $\partial X$, $\rho^{-2}\hat P(0)^{*h} = H^{-1}\rho^2P^{(0)
\dagger_b}\rho^{-2}H$, where $\dagger_b$ is the adjoint for $\mu_b$ and the standard inner product, because
$(\rho^2P^{(0)})^\dagger = \rho^4P^{(0)\dagger_b}\rho^{-2}$ for $|dx| = \rho^{-4}\mu_b$. It is b-elliptic, with
$(\rho\partial_\rho)^{\dagger_b} = -\rho\partial_\rho$, and its normal operator has the Mellin symbol

$$I^\sharp(\lambda) := H_0^{-1}I(2-\bar\lambda)^\dagger H_0 = -\lambda^2+(4-a^{*h})\lambda+\Delta_{\mathbb S^3}+V^{*h}+
b^{*h}+2a^{*h}-4,\tag{3.5}$$

of the form of Lemma 2.4 (up to a first-order term from $H_0^{-1}\Delta H_0$), with $\mathrm{spec}_{I^\sharp} =
\{2-\bar\mu:\mu\in\mathrm{spec}_b\}$: conjugation by $\rho^{\pm2}$ shifts the roots by 2, and the $\dagger_b$-adjoint
reflects them. (The formula was checked with sympy for scalar operators, `checks_c.py` in the working notes.) $v$ has
b-weight $-\alpha-2+2 = -\alpha$, and $-\alpha\notin\mathrm{Re}\,\mathrm{spec}_{I^\sharp}$ if and only if $\alpha+2\notin
\mathrm{Re}\,\mathrm{spec}_b$, which (G) gives. Lemmas 2.5-2.6 and 2.2 (g) for this operator, as above, give (3.3), the
target weight being $-\alpha$: $\rho^{-2}\hat P(0)^{*h}v\in H^{-1-s}_{b,-\alpha}$ is $\hat P(0)^{*h}v$ in the b-weight
$-\alpha+2$, which is that of $\dot H^{-s,-\alpha}_b$.

*Fredholm.* By Lemma 2.9 (b) the inclusion $\mathcal X_0\hookrightarrow\bar H^{-N,-N}_b$ is compact for
$N>\max(-s,-\alpha)$, so (3.2) gives a finite-dimensional kernel and closed range (Peetre's lemma), and (3.3) does the
same for $\hat P(0)^{*h}$ on $\mathcal X^*_0$. *Green's formula*: $\langle\hat P(0)u,v\rangle = \langle u,\hat
P(0)^{*h}v\rangle$ for $u\in\mathcal X_0$, $v\in\mathcal X^*_0$, with the $h$-weighted $L^2(|dx|)$ pairings of I.A
section 7.3. Split with $\chi_\partial$. For $(1-\chi_\partial)u$ it is I.A section 7.3's proof. Near $\partial X$, Lemma
2.5 gives $\chi_\partial u\in H^{s+1}_{b,\alpha+2}$ and $\tilde\chi_\partial v\in H^{2-s}_{b,-\alpha}$; both sides of the
formula are continuous in $\chi_\partial u\in H^{s+1}_{b,\alpha+2}$ for fixed $v$ (Lemma 2.9 (a), (d)), and for
$\chi_\partial u\in C_c^\infty$ the formula is the definition of $\hat P(0)^{*h}v$ as a distribution; Lemma 2.2 (d) gives
the density. *Cokernel*: an element of $\mathcal Y_0^*$ annihilating the range annihilates $\hat P(0)C_c^\infty(\bar
X^\circ)$, so it solves $\hat P(0)^{*h}v = 0$ and lies in $\mathcal X^*_0$; conversely use Green's formula. $\square$

### 3.2 Proof of (2)

Let $u\in\bar H^{s,\alpha}_b$ with $\hat P(0)u = 0$. In the interior the estimates of section 3.1 hold in the strong
sense (I.A Remark 7.3: Propositions 4.2 (1), 5.1, 5.2 and Corollary 6.5 do), with the a priori term at the horizon given
by $u$'s own order $s$, so $u\in\bar H^{s'}$ on $\{r<3R_1\}$ for every $s'$: $u$ is smooth up to $\partial_\sharp X$.
Near $\partial X$, Lemma 2.5 at every order gives $\chi_\partial u\in H^\infty_{b,\alpha+2}$, and Lemma 2.7 for $L =
P^{(0)}$, with $(c_-,c_+) = I$ and $c = \alpha+2$, gives $\chi_\partial u\in\mathcal A^\beta$ for every $\beta<\beta_+$.
This is the source's contour shift through (9.109), done here by Lemmas 2.3 and 2.7. $\square$

### 3.3 Proof of (3) and (4)

*Kernel.* By (2), every kernel element $u$ for $(s,\alpha)$ is smooth up to $\partial_\sharp X$ and in $\mathcal A^\beta$
near $\partial X$ for all $\beta<\beta_+$; by Lemma 2.9 (c) it lies in $\bar H^{s',\alpha'}_b$ for every $s'$ and every
$\alpha'$ with $\alpha'+2<\beta_+$, so it is a kernel element for every pair $(s',\alpha')$.

*Annihilator.* Let $v\in\ker_{\mathcal X^*_0}\hat P(0)^{*h}$ for $(s,\alpha)$. Near $\partial X$, Lemma 2.5 gives
$\tilde\chi_\partial v\in H^\infty_{b,-\alpha}$, and Lemma 2.7 for $\rho^{-2}\hat P(0)^{*h}$, whose gap containing
$-\alpha$ is $(2-\beta_+,2-\beta_-)$, gives $\chi_\partial v\in H^\infty_{b,c'}$ for every $c'<2-\beta_-$; this is the
b-weight $-\alpha'$ of $\dot H^{1-s',-\alpha'-2}_b$ whenever $\alpha'+2>\beta_-$. In the interior, the adjoint estimates
of section 3.1 hold in the strong sense (I.A Remark 7.3) at every order $1-s'$ with $s'>\frac12+\vartheta_{\mathcal H}$:
at the horizon the adjoint estimate is below threshold and needs no a priori condition beyond $v\in H^{-N}$, and (6.2)
and propagation hold at every order. So $v$ is an annihilator for every pair $(s',\alpha')$.

So kernels and annihilators do not depend on the pair, and neither does the index. (4) follows: if one pair has trivial
kernel and annihilator, all do. Without the last terms: if $\|u_j\|_{\bar H^{s,\alpha}_b} = 1$ and $\|\hat
P(0)u_j\|\to0$, then by Lemma 2.9 (b) a subsequence converges in $\bar H^{-N,-N}_b$, by (3.2) it is Cauchy in $\mathcal
X_0$, and its limit is a kernel element of norm 1, a contradiction; likewise for (3.3). $\square$

*Remark 3.2 ([Hin26c] Remark 9.37).* The source notes that the error term of (3.2) may be taken at orders $s^\flat<s$,
$\alpha^\flat<\alpha$ with $\alpha^\flat+2$ in the same gap, and that the kernel is polyhomogeneous; neither is used
below, and neither is proved here.

## 4. The transition face normal operator ([Hin26c] Theorem 9.38 at $n = 4$)

### 4.1 The face and the operator

The interior of the transition face is $\mathrm{tf}^\circ := \mathbb R^4_{\hat x}\setminus0$, with $\hat r := |\hat x|$,
$\hat\rho := \hat r^{-1}$, $\omega := \hat x/\hat r$; $\mathrm{tf}$ is its compactification at both ends, $\mathrm{sctf}$
at $\hat r = \infty$ and $\mathrm{ztf}$ at $\hat r = 0$, with $\rho_{\mathrm{sctf}} := \hat\rho/(1+\hat\rho) = (1+\hat
r)^{-1}$ and $\rho_{\mathrm{ztf}} := (1+\hat\rho)^{-1} = \hat r/(1+\hat r)$. Each end is an end in the sense of section
2.2: sctf with $\varrho = \hat\rho$, ztf with $\varrho = \hat r$. $C^\infty_b(\mathrm{tf})$ is the space of smooth
functions on $\mathrm{tf}^\circ$ with all b-derivatives ($\hat r\partial_{\hat r}$, $Z_i$) bounded, and $\mathcal
A^{a,b}(\mathrm{tf}) := \rho_{\mathrm{sctf}}^a\rho_{\mathrm{ztf}}^bC^\infty_b(\mathrm{tf})$. For $\hat\sigma\in\mathbb
C$,

$$N_{\mathrm{tf}}(\hat\sigma) :=
2i\hat\sigma\hat\rho\big(\hat\rho\partial_{\hat\rho}-\tfrac32-S_0\big)+\hat\rho^2N(P^{(0)}),
\tag{4.1}$$

with $\rho\partial_\rho$ read as $\hat\rho\partial_{\hat\rho}$ in $N(P^{(0)})$; this is [Hin26c] (9.110) at $n = 4$. It
is the spectral family of the *model* $\hat P_{\mathrm{mod}}(\sigma) :=
2i\sigma\rho(\rho\partial_\rho-\frac32-S_0)+\rho^2 N(P^{(0)})$ on $\mathbb R^4\setminus0$, written in $\hat x$. For
$\varsigma>0$ let $(S_\varsigma u)(\hat x) := u(\hat x/\varsigma)$. Since $\rho = \varsigma\hat\rho$ and
$\rho\partial_\rho = \hat\rho\partial_{\hat\rho}$ under $\hat x = \varsigma x$,

$$S_\varsigma\hat P_{\mathrm{mod}}(\sigma)S_\varsigma^{-1} =
\varsigma^2N_{\mathrm{tf}}(\sigma/\varsigma),\qquad\varsigma>0,
\tag{4.2}$$

which is [Hin26c] (5.13): $N_{\mathrm{tf}}(\hat\sigma) = \varsigma^{-2}S_\varsigma\hat
P_{\mathrm{mod}}(\hat\sigma\varsigma) S_\varsigma^{-1}$ for every $\varsigma$.

*Structure.* (a) On $\{\hat r>1\}$, $N_{\mathrm{tf}}(\hat\sigma)$ is an operator of the form (1.1) at $\sigma =
\hat\sigma$, with $S = S_0$, $P^{(0)} = N(P^{(0)})$, $Q = 0$, $g_{00} = 0$, $P_2 = 0$, so it satisfies (H1)-(H2) on
$\{\hat\rho<1\}$; its thresholds $\bar S$ and $\vartheta_{\mathrm{in}}$, computed with the fibre inner product
$H_0(\omega)$ extended to be independent of $\hat\rho$ (or the inner product of I.A Lemma 2.4 frozen at $\rho = 0$), are
those of $\hat P$, because they depend only on the coefficients at $\rho = 0$: $\bar S$ on $S_0$, and $p_{\mathrm{in}}$
on the boundary symbol of $\rho^{-1}\mathrm{Im}_h\hat P(0)\in\rho\,\mathrm{Diff}^1_b$, which is that of the same
expression for $\rho^2N(P^{(0)})$ and $H_0$, as $P^{(0)}-N(P^{(0)})\in\rho\,\mathrm{Diff}^2_b$ and $H-H_0\in\rho
C^\infty$. (b) On $\mathrm{tf}^\circ$, $N_{\mathrm{tf}}(\hat\sigma)$ is elliptic at fibre infinity: its principal symbol
is $\hat\rho^2$ times that of $(\hat\rho D_{\hat\rho})^2+\Delta_{\mathbb S^3}$, which is $|\hat\zeta|^2\mathrm{Id}$ in
$\hat x$. (c) Near ztf, with $\varrho = \hat r$ and $\hat\rho\partial_{\hat\rho} = -\varrho\partial_\varrho$,

$$\hat r^2N_{\mathrm{tf}}(\hat\sigma) = N(P^{(0)})|_{\rho\partial_\rho\to-\varrho\partial_\varrho}+2i\hat\sigma\hat r
\big(-\varrho\partial_\varrho-\tfrac32-S_0\big),$$

an operator $L$ as in section 2.5 at the end at 0, b-elliptic on $\{\hat r<2\}$, whose Mellin symbol is $J(\lambda) =
I(-\lambda)$, with $\mathrm{spec}_J = -\mathrm{spec}_b$. Its adjoint for $|d\hat x| = \hat r^4\mu_b$ and $H_0$ satisfies
$\hat r^2N_{\mathrm{tf}}(\hat\sigma)^{*h} = H_0^{-1}\hat r^{-2}L^{\dagger_b}\hat r^2H_0$, with Mellin symbol
$H_0^{-1}I(\bar\lambda+2)^\dagger H_0$ and roots $\{\bar\mu-2:\mu\in\mathrm{spec}_b\}$: $L^{\dagger_b}$ has the roots
$\{\bar\mu\}$, and conjugation by $\hat r^{\mp2}$ shifts them by $-2$. This is [Hin26c]'s "$-n+2+\bar\lambda$" at $n =
4$.

### 4.2 The spaces on the face

Let $\varphi_\infty\in C^\infty(\mathrm{tf})$ be a function of $\hat r$ with $\varphi_\infty = 0$ on $\{\hat r\le1\}$ and
$\varphi_\infty = 1$ on $\{\hat r\ge2\}$.

**Definition 4.1 ([Hin26c] (3.44) at $n = 4$).** For $s,q\in\mathbb R$, $k\in\mathbb N_0$ and a decay order $\mathsf r$
on the scattering phase space of $\mathbb R^4_{\hat x}$ (as in I.A section 1.4),
$$\|w\|^2_{H^{(s;k),(\mathsf r,q)}_{\mathrm{sc},b;b}(\mathrm{tf})} := \|\varphi_\infty w\|^2_{H^{(s;k),\mathsf
r}_{\mathrm{sc}}
(\mathbb R^4)}+\|(1-\varphi_\infty)w\|^2_{H^{s+k}_{b,q-2}},$$
with $H^{(s;k),\mathsf r}_{\mathrm{sc}}$ the space of I.A section 4.6 ($k$ further b-derivatives) and $H^{s+k}_{b,q-2}$
the space of Definition 2.1 at the end at 0. $k = 0$ is written $H^{s,(\mathsf r,q)}_{\mathrm{sc},b}(\mathrm{tf})$.

Near ztf, $\rho_{\mathrm{ztf}}^qL^2(|d\hat x|) = \hat r^{q-2}L^2(\mu_b)$ as $|d\hat x| = \hat r^4\mu_b$, so the b-weight
is $q-2$, and the norm is that of $\rho_{\mathrm{sctf}}^{\mathsf r}\rho_{\mathrm{ztf}}^qH^s_{\mathrm{sc},b}(\mathrm{tf})$
for the Euclidean density, as in [Hin26c]. By (C3)-(C4), (C6) of I.A and Lemma 2.2: the $L^2(|d\hat x|)$ pairing
identifies the dual of $H^{s,(\mathsf r,q)}_{\mathrm{sc},b}$ with $H^{-s,(-\mathsf r,-q)}_{\mathrm{sc},b}$ (near ztf,
$\hat r^{-4}$ maps b-weight $-q+2-2$ to $-q-2-2$... precisely: the pairing is $\langle w,\hat r^4v\rangle_{\mu_b}$, and
$v\mapsto\hat r^4v$ maps the b-weight $-q-2$ of the second space onto $-(q-2)$, the dual of $q-2$); the inclusion is
compact when all three orders drop, the decay order by a positive constant; and $N_{\mathrm{tf}}(\hat\sigma)$ maps
$H^{(s;k),(\mathsf r,q)}_{\mathrm{sc},b}$ to $H^{(s-2;k),(\mathsf r,q-2)}_{\mathrm{sc},b}$, by (a) and (c) of section 4.1
(near sctf it lies in $\Psi^{2,0}_{\mathrm{sc}}$, with commutators with b-vector fields of the same class).

### 4.3 The theorem

*Orders.* Let $J_\pm := \{\sigma_0:|\sigma_0\mp1|<\frac14\}$, and let $\mathsf r_\pm$ be an order pair's decay order that
is admissible, with weight $\alpha_+$, for every $\sigma_0\in J_\pm$ (I.A Lemma 7.1 at $\sigma_* = \pm1$, which concerns
only the boundary face; its order is a function of $\xi$ and $|\eta|^2$, so it is invariant under rotations). Let
$\Theta_\pm := \{\theta\in[0,\pi]:|e^{i\theta}\mp1|\le\frac12\}$; for $\theta\in\Theta_\pm$,
$\pm\cos\theta\ge\frac78$, so $\mathrm{Re}\,e^{i\theta}\in J_\pm$. For orders and $q$ put

$$\mathcal X_{\mathrm{tf},\theta} := \{w\in H^{s,(\mathsf r+\alpha_+,q)}_{\mathrm{sc},b}:N_{\mathrm{tf}}(e^{i\theta})w\in
\mathcal Y_{\mathrm{tf},\theta}\},\qquad\mathcal Y_{\mathrm{tf},\theta} := H^{s-2,(\mathsf r+\alpha_++1,q-2)}_{
\mathrm{sc},b},$$

$$\mathcal X^*_{\mathrm{tf},\theta} := \{w\in H^{-s+2,(-\mathsf r-\alpha_+-1,-q+2)}_{\mathrm{sc},b}:N_{\mathrm{tf}}
(e^{i\theta})^{*h}w\in H^{-s,(-\mathsf r-\alpha_+,-q)}_{\mathrm{sc},b}\},$$

the adjoint taken for $|d\hat x|$ and $H_0$; $\mathcal X_{\mathrm{tf},\theta}\to\mathcal Y_{\mathrm{tf},\theta}$ is
[Hin26c] (9.112).

**Theorem 4.3 ([Hin26c] Theorem 9.38 at $n = 4$, on $E$).** Assume (H1)-(H2). Let $q\in\mathbb R$ with $-q+2$ in an
indicial gap $(\beta_-,\beta_+)$ of $\hat P(0)$, and let $\alpha_+,s,N\in\mathbb R$.

(1) (*Fredholm estimates, I.*) For $\theta\in\Theta_\pm$ and $\mathsf r = \mathsf r_\pm$ there is $C$, uniform in
$\theta\in\Theta_\pm$, with

$$\|w\|_{H^{s,(\mathsf r+\alpha_+,q)}_{\mathrm{sc},b}}\le C\big(\|N_{\mathrm{tf}}(e^{i\theta})w\|_{H^{s-2,(\mathsf r+
\alpha_++1,q-2)}_{\mathrm{sc},b}}+\|w\|_{H^{-N,(-N,-N)}_{\mathrm{sc},b}}\big),\qquad w\in\mathcal X_{\mathrm{tf},\theta},
\tag{4.3}$$

$$\|w\|_{H^{-s+2,(-\mathsf r-\alpha_+-1,-q+2)}_{\mathrm{sc},b}}\le C\big(\|N_{\mathrm{tf}}(e^{i\theta})^{*h}w\|_{
H^{-s,(-\mathsf r-\alpha_+,-q)}_{\mathrm{sc},b}}+\|w\|_{H^{-N,(-N,-N)}_{\mathrm{sc},b}}\big),\qquad w\in\mathcal
X^*_{\mathrm{tf},\theta}.\tag{4.4}$$

(2) (*Fredholm estimates, II.*) Let $I\subset(0,\pi)$ be compact and $\mathsf r$ constant near $R_{\mathrm{out}}$ with
$\mathsf r+\alpha_+<-\frac12+\bar S$ there. Then (4.3)-(4.4) hold uniformly for $\theta\in I$.

(3) (*Fredholm property.*) In the settings of (1) and (2), $N_{\mathrm{tf}}(e^{i\theta}):\mathcal X_{\mathrm{tf},\theta}
\to\mathcal Y_{\mathrm{tf},\theta}$ is Fredholm, and the annihilator of its range is $\ker_{\mathcal X^*_{\mathrm{tf},
\theta}}N_{\mathrm{tf}}(e^{i\theta})^{*h}$. The kernel and the annihilator do not depend on $q$ with $-q+2\in(\beta_-,
\beta_+)$, on $s$, or on the orders allowed in (1)-(2); the index does not depend on $\theta\in[0,\pi]$ either.

(4) (*Higher b-regularity.*) If $w\in\mathcal X_{\mathrm{tf},\theta}$ and $N_{\mathrm{tf}}(e^{i\theta})w\in
H^{(s-2;k),(\mathsf r+\alpha_++1,q-2)}_{\mathrm{sc},b;b}$, then $w\in H^{(s;k),(\mathsf r+\alpha_+,q)}_{\mathrm{sc},b;b}$
and

$$\|w\|_{H^{(s;k),(\mathsf r+\alpha_+,q)}_{\mathrm{sc},b;b}}\le C\big(\|N_{\mathrm{tf}}(e^{i\theta})w\|_{H^{(s-2;k),
(\mathsf r+\alpha_++1,q-2)}_{\mathrm{sc},b;b}}+\|w\|_{H^{s,(\mathsf r+\alpha_+,q)}_{\mathrm{sc},b}}\big).\tag{4.5}$$

(5) (*Kernel.*) In the settings of (1) and (2), every $w\in\ker_{\mathcal X_{\mathrm{tf},\theta}}N_{\mathrm{tf}}
(e^{i\theta})$ lies in $\mathcal A^{\frac32+\bar S-\epsilon,-\beta}(\mathrm{tf})$ for every $\epsilon>0$ and $\beta\in
(\beta_-,\beta_+)$. Conversely $\bigcap_{\epsilon>0}\mathcal A^{\frac32+\bar S-\epsilon,-\beta_--\epsilon}(\mathrm{tf})
\subset\mathcal X_{\mathrm{tf},\theta}$.

[Hin26c] Theorem 9.38 (5) also states (9.115), that the annihilator lies in $e^{-2i/\rho_{\mathrm{sctf}}}\mathcal
A^{a,-2+\beta}(\mathrm{tf})$ (at $n = 4$). Its proof conjugates the scattering calculus by $e^{2i\hat r}$, which is not
among the statements READ in I.A, and uses (9.117), whose printed proof drops a term (section 8, (F4)). Nothing here
uses (9.115): tf-admissibility is stated in section 5 on the spaces of this theorem. It is not proved here.

### 4.4 Proof

*Near sctf, (1)-(2).* Let $N^\flat$ be an operator on $\mathbb R^4$ equal to $N_{\mathrm{tf}}(e^{i\theta})$ on $\{\hat
r>\frac12\}$ and of the class of (a) of section 4.1 on $\{\hat\rho<2\}$. The estimates of I.A at the boundary face hold
for it: Lemmas 4.4-4.5, Propositions 4.6 and 4.9 and the pieces (C), (D), (E), (F) of I.A section 7.1 (with section 7.2
for (2)) use only (H1)-(H2) on $\{\rho<\rho_1\}$, their commutants being microsupported at the boundary face, and
Proposition 5.1 is the elliptic estimate. Apply them to $\varphi_\infty w$, which is supported in $\{\hat r\ge1\}$: at
fibre infinity everything is elliptic by (b), so the regularity loss is 2, and at the boundary face the radial estimates
gain one order of decay, as in I.A (7.1). With $\theta\in\Theta_\pm$ the orders $\mathsf r_\pm$ are admissible for
$\mathrm{Re}\,e^{i\theta}$, uniformly (I.A Theorem 7.2 (1), whose constants are uniform for $\sigma_0$ in compact subsets
of $J_\pm$ and $\mathrm{Im}\,\sigma\in[0,1]$); for $\theta\in I\subset(0,\pi)$, $\mathrm{Im}\,e^{i\theta}$ is bounded
below and I.A Theorem 7.2 (2) applies. The a priori term at $R_{\mathrm{in}}$ is absorbed by Ehrling's lemma as in I.A
section 7.1. This gives, with $\varphi'$ a cut-off to $\{\frac12<\hat r<4\}$ and the commutator $[N^\flat,
\varphi_\infty]$ supported in $\{1\le\hat r\le2\}$,

$$\|\varphi_\infty w\|_{H^{s,\mathsf r+\alpha_+}_{\mathrm{sc}}}\le C\big(\|N_{\mathrm{tf}}w\|_{\mathcal Y_{\mathrm{tf},
\theta}}+\|\varphi'w\|_{H^{s-1}}+\|w\|_{H^{-N,(-N,-N)}_{\mathrm{sc},b}}\big).$$

*The interior.* (K2) on $\{\frac14<\hat r<8\}$ bounds $\|\varphi'w\|_{H^{s-1}}\le\|\varphi'w\|_{H^s}$ by
$\|N_{\mathrm{tf}} w\|$ there plus $\|w\|_{H^{-N}}$ there.

*Near ztf.* Lemma 2.5 for $L = \hat r^2N_{\mathrm{tf}}(e^{i\theta})$ at the b-weight $q-2$ (with $\hat r^{-2}$ moved by
Lemma 2.2 (b), so that $N_{\mathrm{tf}}w\in H^{s-2}_{b,q-4}$ is the target's weight $q-2$) bounds
$\|(1-\varphi_\infty)w\|_{H^s_{b,q-2}}$ by $\|N_{\mathrm{tf}}w\|_{\mathcal Y_{\mathrm{tf},\theta}}$ plus $\|\tilde\chi
w\|_{H^{-N}_{b,q-2}}$, $\tilde\chi$ a cut-off to $\{\hat r<3\}$. Then Lemma 2.6 at $c = q-2$, which is not a real part of
a root of $J$ because $-(q-2)$ lies in the gap, and Lemma 2.2 (g) give $\|\tilde\chi w\|_{H^{-N}_{b,q-2}}\le
C\|N_{\mathrm{tf}}w\|+Ce^{-K}\|\tilde\chi'w\|_{H^{-N}_{b,q-2}}+C_K\|w\|_{H^{-N,(-N,-N)}_{\mathrm{sc},b}}$, and the middle
term is absorbed as in section 3.1. This is [Hin26c]'s improvement of the error term from $(-N,q)$ to $(-N,q-1)$ and then
to $(-N,-N)$. Summing gives (4.3).

*The adjoint.* The same, with the adjoint chain of I.A section 7.1 at the boundary face ((E*), (D*), (C*) and (F),
the a priori term at $R_{\mathrm{out}}$ absorbed as there), (K2) in the interior, and near ztf Lemmas 2.5-2.6 for the
adjoint's normal operator, whose roots $\bar\mu-2$ avoid the real part $-q$ (the b-weight of $-q+2$) exactly when $-q+2$
avoids $\mathrm{Re}\,\mathrm{spec}_b$. This gives (4.4).

*(3).* The inclusion $\mathcal X_{\mathrm{tf},\theta}\hookrightarrow H^{-N,(-N,-N)}_{\mathrm{sc},b}$ is compact for $N$
large, so (4.3)-(4.4) give the Fredholm property, by Peetre's lemma, as in I.A section 7.3. Green's formula
$\langle N_{\mathrm{tf}}w,v\rangle = \langle w,N_{\mathrm{tf}}^{*h}v\rangle$ for $w\in\mathcal X_{\mathrm{tf},\theta}$,
$v\in\mathcal X^*_{\mathrm{tf},\theta}$: near sctf by I.A section 7.3's proof (the regularising family $T_t$ of (C8),
there being no artificial boundary); near ztf as in section 3.1, by Lemma 2.5 and density (Lemma 2.2 (d)). So the
annihilator of the range is the kernel of the adjoint on $\mathcal X^*_{\mathrm{tf},\theta}$. *Independence.* Kernel
elements are independent of $q$, $s$ and the orders by (5) and its converse. For the annihilator: near ztf, Lemma 2.5 and
Lemma 2.7 for the adjoint, with roots $\bar\mu-2$ and gap $(\beta_--2,\beta_+-2)$ containing $-q$, put $v$ in
$H^\infty_{b,c'}$ for every $c'<\beta_+-2$, which is the b-weight $-q'$ of $\mathcal X^*_{\mathrm{tf},\theta}$ for every
$q'>2-\beta_+$; near sctf, the strong forms of the adjoint estimates put it in the space of any other allowed order and
any $s$ (I.A section 7.3, *Independence of the orders*). *The index in $\theta$.* As in I.A section 7.3, *Local constancy
of the index*: at $\theta_*\in[0,\pi]$ fix orders allowed near $\theta_*$ ($\mathsf r_\pm$ near $\Theta_\pm$, a constant
order of (2) in $(0,\pi)$), augment with $E_{01},E_{10}$ built from $C_c^\infty(\mathrm{tf}^\circ)$, and run the
contradiction argument with $\theta_j\to\theta_*$ using the uniform estimates (4.3)-(4.4) and the compact inclusion. The
index is locally constant, the kernels and annihilators do not depend on the allowed orders, and $[0,\pi]$ is connected.

*(4).* Near sctf, the proof of I.A Theorem 7.2 (4), with Proposition 4.9 (3) and Lemma 4.10, applies to $N^\flat$; near
ztf, b-regularity is regularity in $H_{b,q-2}$, and Lemma 2.5 at the order $s+k$ gives it; in the interior, (K2).

*(5).* Let $w$ be in the kernel. Near sctf, the first paragraph of the proof of I.A Theorem 7.2 (5) (Remark 7.3, (4) with
$f = 0$, and Lemma 7.4 (b)) gives $\varphi_\infty w\in\rho_{\mathrm{sctf}}^{\frac32+\bar S-\epsilon}C^\infty_b$. In the
interior $w$ is smooth by (K2). Near ztf, Lemma 2.5 gives $\tilde\chi w\in H^\infty_{b,q-2}$, and Lemma 2.7 with $J =
I(-\cdot)$, $(c_-,c_+) = (-\beta_+,-\beta_-)\ni q-2$ and $Lw = 0$ gives $(1-\varphi_\infty)w\in\mathcal A^{c'}$ near ztf
for every $c'<-\beta_-$, that is, in $\rho_{\mathrm{ztf}}^{-\beta}C^\infty_b$ for every $\beta>\beta_-$. Conversely, for
$w\in\bigcap_\epsilon\mathcal A^{\frac32+\bar S-\epsilon,-\beta_--\epsilon}$: near sctf, I.A Lemma 7.4 (a) and the
mapping of $\mathcal A^a$ to $\mathcal A^{a+1}$ by $N_{\mathrm{tf}}$ there (the converse in I.A section 7.5) give
membership in the sctf part of $\mathcal X_{\mathrm{tf},\theta}$; near ztf, $\mathcal A^{-\beta_--\epsilon}\subset
H^\infty_{b, -\beta_--2\epsilon}\subset H^s_{b,q-2}$ by Lemma 2.2 (f), as $q-2<-\beta_-$, and $N_{\mathrm{tf}}w\in\hat
r^{-2} \mathcal A^{-\beta_--\epsilon}\subset H^{s-2}_{b,q-4}$ likewise. $\square$

## 5. tf-admissibility

### 5.1 The definition and its consequences

**Definition 5.1 (tf-admissibility at $n = 4$).** $\hat P$ is *tf-admissible with weight* $\beta$ if (i) $\beta$ lies in
an indicial gap $(\beta_-,\beta_+)$ of $\hat P(0)$; and, with $q := 2-\beta$ and $s$, $\alpha_+$, $\mathsf r_\pm$ as in
Theorem 4.3, (ii) $N_{\mathrm{tf}}(e^{i\theta}):\mathcal X_{\mathrm{tf},\theta}\to\mathcal Y_{\mathrm{tf},\theta}$ is
injective for every $\theta\in[0,\pi]$, and (iii) $N_{\mathrm{tf}}(1)^{*h}$ is injective on $\mathcal
X^*_{\mathrm{tf},0}$ (with $\mathsf r = \mathsf r_+$). By Theorem 4.3 (3), (ii) and (iii) do not depend on the choices of
$s$, $\alpha_+$, $\mathsf r_\pm$, or on $q$ with $-q+2$ in the gap.

*Relation to [Hin26c] Definition 5.10* (with Corollary 9.39's $-n+2+\beta = -2+\beta$). There, (ii) is the triviality of
the kernel of $N_{\mathrm{tf}}(e^{i\theta})$ on $\mathcal A^{a,-\beta}(\mathrm{tf})$ for every $a$, which implies (ii)
here by Theorem 4.3 (5); and (iii) is its triviality on $e^{-2i/\rho_{\mathrm{sctf}}}\mathcal
A^{a,-2+\beta}(\mathrm{tf})$ for every $a$, which implies (iii) here when (9.115) holds. So the source's tf-admissibility
implies this one, given (9.115), which is not proved here (section 4.3). Corollary 5.2 needs only Definition 5.1, and
Proposition 5.3 verifies Definition 5.1 directly.

**Corollary 5.2 ([Hin26c] Corollary 9.39 at $n = 4$).** Let $\hat P$ be tf-admissible with weight $\beta_0\in(\beta_-,
\beta_+)$. Then:
(a) $N_{\mathrm{tf}}(e^{i\theta}):\mathcal X_{\mathrm{tf},\theta}\to\mathcal Y_{\mathrm{tf},\theta}$ is invertible for
every $\theta\in[0,\pi]$, every $q\in(2-\beta_+,2-\beta_-)$ and the orders of Theorem 4.3 (1)-(2), and so is
$N_{\mathrm{tf}}(e^{i\theta})^{*h}:\mathcal X^*_{\mathrm{tf},\theta}\to H^{-s,(-\mathsf r-\alpha_+,-q)}_{\mathrm{sc},b}$.
(b) Let $\Sigma_+ := [0,\frac\pi4]$, $\Sigma_m := [\frac\pi4,\frac{3\pi}4]$, $\Sigma_- := [\frac{3\pi}4,\pi]$, with
orders $\mathsf r_{\Sigma_\pm} := \mathsf r_\pm$ and $\mathsf r_{\Sigma_m} := \mathsf r_{\mathrm{mid}}$, a constant with
$\mathsf r_{\mathrm{mid}}+\alpha_+<-\frac12+\bar S$. For each sector $\Sigma$ and $k\in\mathbb N_0$, uniformly in
$\theta\in\Sigma$, with $\mathsf r := \mathsf r_\Sigma$,

$$\|w\|_{H^{(s;k),(\mathsf r+\alpha_+,q)}_{\mathrm{sc},b;b}}\le C_k\|N_{\mathrm{tf}}(e^{i\theta})w\|_{H^{(s-2;k),
(\mathsf r+\alpha_++1,q-2)}_{\mathrm{sc},b;b}},\tag{5.1}$$

$$\|w\|_{H^{-s+2,(-\mathsf r-\alpha_+-1,-q+2)}_{\mathrm{sc},b}}\le C\|N_{\mathrm{tf}}(e^{i\theta})^{*h}w\|_{H^{-s,
(-\mathsf r-\alpha_+,-q)}_{\mathrm{sc},b}}.\tag{5.2}$$

(c) $\hat P$ is tf-admissible with every weight in $(\beta_-,\beta_+)$.

*Proof.* (a) At $\theta = 0$ the kernel is trivial by (ii) and the annihilator of the range by (iii) and Theorem 4.3 (3),
so the index there is 0, and by Theorem 4.3 (3) it is 0 for every $\theta$ and $q$. By (ii) and Theorem 4.3 (3) the
kernel is trivial for every $\theta$ and $q$, so the operator is invertible, and its adjoint, whose kernel is the
annihilator of the range, is injective with closed range of codimension equal to the dimension of the kernel, which is 0.
(b) Each sector is covered by the settings of Theorem 4.3: $\Sigma_+$ by (1) on $\Theta_+ = [0,\theta_1]$, $\theta_1 :=
2\arcsin\frac14<\frac\pi4$, and by (2) on $[\frac{\theta_1}2,\frac\pi4]$ with the order $\mathsf r_+$, which is constant
near $R_{\mathrm{out}}$ with the threshold there; $\Sigma_-$ likewise; $\Sigma_m$ by (2). So (4.3) holds uniformly on
$\Sigma$. If (5.1) failed at $k = 0$ there would be $\theta_j\to\theta_*\in\Sigma$ and $w_j$ with norm 1 and
$\|N_{\mathrm{tf}}(e^{i\theta_j})w_j\|\to0$; by (4.3) and the compact inclusion a subsequence converges in
$H^{-N,(-N,-N)}$ to some $w\ne0$ (as the left side of (4.3) is 1), with $N_{\mathrm{tf}}(e^{i\theta_*})w = 0$ as a
distribution and, by (4.3) at $\theta_*$ applied to differences, $w\in\mathcal X_{\mathrm{tf},\theta_*}$; this
contradicts (a). For $k\ge1$ combine (4.5) with the case $k = 0$; (5.2) is the same argument with (4.4). (c) Let
$\beta\in(\beta_-, \beta_+)$ and $q := 2-\beta$. (i) holds, and (ii)-(iii) at $q$ hold by (a). $\square$

### 5.2 Hankel functions

READ in [DLMF] (Digital Library of Mathematical Functions, release 1.2.8 of 2026-09-15): (10.7.7) "$H^{(1)}_\nu(z)\sim-
H^{(2)}_\nu(z)\sim-(i/\pi)\Gamma(\nu)(\frac12z)^{-\nu}$, $\Re\nu>0$", as $z\to0$; and Hankel's expansions (10.17.5)
"$H^{(1)}_\nu(z)\sim(\frac2{\pi z})^{\frac12}e^{i\omega}\sum_{k=0}^\infty i^k\frac{a_k(\nu)}{z^k}$,
$-\pi+\delta\le\mathrm{ph} \,z\le2\pi-\delta$" and (10.17.6) "$H^{(2)}_\nu(z)\sim(\frac2{\pi
z})^{\frac12}e^{-i\omega}\sum_{k=0}^\infty(-i)^k\frac{ a_k(\nu)}{z^k}$, $-2\pi+\delta\le\mathrm{ph}\,z\le\pi-\delta$",
with $\omega = z-\frac12\nu\pi-\frac14\pi$ (10.17.2), $a_0 = 1$, as $|z|\to\infty$ in the closed sectors. $H^{(1)}_\nu$
and $H^{(2)}_\nu$ are solutions of Bessel's equation $z^2w''+zw'+(z^2-\nu^2)w = 0$, holomorphic in $\mathbb
C\setminus(-\infty,0]$ (their definition, [DLMF] section 10.2 (ii)).

**Lemma 5.4.** Let $\ell\in\mathbb N_0$, $\nu := \ell+1$, $\hat\sigma = e^{i\theta}$, $\theta\in[0,\pi]$.
(a) The solutions on $(0,\infty)$ of $-u''-\frac3{\hat r}u'+\frac{\ell(\ell+2)}{\hat r^2}u-\hat\sigma^2u = 0$ are the
combinations of $f_j(\hat r) := \hat r^{-1}H^{(j)}_\nu(\hat\sigma\hat r)$, $j = 1,2$, which are linearly independent.
(b) For $\theta = 0$, $g_1 := e^{-i\hat r}f_1$ and $g_2 := e^{i\hat r}f_2$ satisfy, for $\hat r\ge1$ and every $k$,
$|(\hat r\partial_{\hat r})^k(g_j-c_j\hat r^{-3/2})|\le C_k\hat r^{-5/2}$ with $c_j := (\frac2\pi)^{1/2}e^{\mp i(\frac12
\nu\pi+\frac14\pi)}\ne0$; in particular $g_j\in\mathcal A^{3/2}$ near sctf.
(c) For $\theta\in(0,\pi)$, $|f_1(\hat r)|\le Ce^{-\hat r\sin\theta}$ and $|f_2(\hat r)|\ge c\,\hat r^{-3/2}e^{\hat
r\sin\theta}$ for $\hat r\ge R$.
(d) As $\hat r\to0$, $|f_j(\hat r)|\ge c\,\hat r^{-2-\ell}$.

*Proof.* (a) With $z := \hat\sigma\hat r$ and $u = \hat r^{-1}Z(z)$, $-u''-\frac3{\hat r}u'+\frac{\ell(\ell+2)}{\hat
r^2}u- \hat\sigma^2u = -\hat r^{-3}\big(z^2Z''+zZ'+(z^2-(\ell+1)^2)Z\big)$, as $1+\ell(\ell+2) = (\ell+1)^2$ (checked
with sympy, `checks_c.py`). The equation is second order with smooth coefficients on $(0,\infty)$, so its solutions form
a two-dimensional space; $f_1$, $f_2$ are independent because on the ray $\mathrm{ph}\,z = \theta$ their leading terms
$e^{\pm iz}$ in (10.17.5)-(10.17.6) are, $e^{2iz}$ not tending to a constant. (b) The remainders after the first term in
(10.17.5)-(10.17.6) are $O(|z|^{-3/2})$ uniformly in closed subsectors; $e^{\mp iz}z^{1/2}H^{(j)}_\nu(z)$ is holomorphic
on $\{|\mathrm{ph}\,z|<\frac\pi2\}$, and for real $x\ge1$ the disc of radius $x/2$ about $x$ lies in $\{|\mathrm{ph}\,
z|\le\frac\pi6\}$, so Cauchy's estimates give $|x^k\partial_x^k(\cdot)|\le C_k$ times the bound on the disc, for the
expansion's remainder as well as for each term. With $(\hat r\partial_{\hat r})^k$ a combination of $\hat r^i\partial^i$
this gives (b). (c) On the ray $z = e^{i\theta}\hat r$, $\theta\in(0,\pi)$ fixed, (10.17.5)-(10.17.6) apply, $|e^{iz}| =
e^{-\hat r\sin\theta}$ and $|e^{-iz}| = e^{\hat r\sin\theta}$. (d) (10.7.7) with $|z| = \hat r$ and $\Gamma(\nu)\ne0$.
$\square$

**Lemma 5.5 (spherical waves).** Let $\kappa\in\mathbb R$, $g\in C^\infty([1,\infty))$ with $|\partial^k g|\le C_k
\hat r^{-\gamma-k}$, $Y\in C^\infty(\mathbb S^3;\mathbb C^N)$, $\chi_\infty$ a cut-off to $\{\hat r\ge2\}$, and $v :=
\chi_\infty e^{i\kappa\hat r}g(\hat r)Y(\omega)$. Then $v\in H^{m,l}_{\mathrm{sc}}$ for all $m$ and $l<\gamma-2$, and
$Qv\in H^{\infty,\infty}_{\mathrm{sc}}$ for every $Q\in\Psi^{0,0}_{\mathrm{sc}}$ microsupported, at the boundary face
over sctf, away from $\{\xi = \kappa,\ \eta = 0\}$.

*Proof.* Derivatives $\partial_{\hat x}$ of $v$ are bounded by $C\hat r^{-\gamma}$, so $v\in H^{m,l}$ for $l<\gamma-2$,
as $\int^\infty\hat r^{2l-2\gamma}\hat r^3\,d\hat r<\infty$. Let $A := \chi(D_{\hat r}-\kappa)^*(D_{\hat r}-\kappa)\chi+
\sum_i(\chi\hat r^{-1}Z_i)^*(\chi\hat r^{-1}Z_i)+(1-\chi^2)$, $\chi$ a cut-off to $\{\hat r\ge1\}$ equal to 1 near the
support of $\chi_\infty$, adjoints for $|d\hat x|$: a scattering differential operator of order $(2,0)$ whose principal
symbol at the boundary face is $(\xi-\kappa)^2+|\eta|^2$ (I.A Lemma 4.4 (a): $D_{\hat r}$ has symbol $\xi$, and $\hat
r^{-1}Z_i$ that of a component of $\eta$), and which is elliptic at fibre infinity. It is elliptic at the boundary face
off $\{\xi = \kappa,\eta = 0\}$. $(D_{\hat r}-\kappa)(e^{i\kappa\hat r}gY) = e^{i\kappa\hat r}(D_{\hat r}g)Y$ and $\hat
r^{-1}Z_i(e^{i\kappa\hat r}gY) = e^{i\kappa\hat r}\hat r^{-1}gZ_iY$, and $(D_{\hat r}-\kappa)^* = D_{\hat r}-\kappa-
\frac{3i}{\hat r}$; so $A^jv$ has the form of $v$ with $\gamma$ replaced by $\gamma+2j$, plus a smooth compactly
supported term, and lies in $H^{m,l}$ for $l<\gamma+2j-2$. The microlocal elliptic estimate ((C5) of I.A: [HJS]
Propositions 4.9-4.10) for $A^j$, elliptic of order $(2j,0)$ on $\mathrm{WF}'(Q)$, gives $Qv\in H^{m,l}$ for
$l<\gamma+2j-2$, every $j$. $\square$

### 5.3 The asymptotically Minkowski case

**Lemma 5.6 (frames).** Let $\Theta\in C^\infty(\mathbb S^3;GL(N,\mathbb C))$. Replacing $S_0$, $N(P^{(0)})$ and $H_0$
by $\Theta^{-1}S_0\Theta$, $\Theta^{-1}N(P^{(0)})\Theta$ and $\Theta^*H_0\Theta$ (a change of frame of $E$ that does not
depend on $\rho$) preserves the class of (1.1) at $\rho = 0$, the indicial roots, and tf-admissibility with each weight.

*Proof.* $\Theta(\omega)$ commutes with $\rho\partial_\rho$ and $\hat\rho$, so $\Theta^{-1}N_{\mathrm{tf}}\Theta$ is
(4.1) for the new data, $\Theta^{-1}\Delta_{\mathbb S^3}\Theta-\Delta_{\mathbb S^3}$ being first order on $\mathbb S^3$;
$I(\lambda)$ becomes $\Theta^{-1}I(\lambda)\Theta$. Multiplication by $\Theta$ and $\Theta^{-1}$ is bounded on every
space of Definition 4.1 ($\Theta$ is homogeneous of degree 0, so a symbol of order $(0,0)$ near sctf, and in $C^\infty_b$
near ztf), and the adjoint for $\Theta^*H_0\Theta$ of $\Theta^{-1}N\Theta$ is $\Theta^{-1}N^{*h}\Theta$. So kernels
correspond, on spaces that correspond. $\square$

**Proposition 5.3 ([Hin26c] Proposition 9.40 at $n = 4$).** Suppose that, in some frame $\Theta$ as in Lemma 5.6, $S_0 =
0$, $N(P^{(0)}) = (-(\rho\partial_\rho)^2+2\rho\partial_\rho+\Delta_{\mathbb S^3})\mathrm{Id}$ and $H_0 = \mathrm{Id}$:
the data of the wave operator of 4+1 Minkowski space acting componentwise, as for the scalar and the tensor wave
operators in the Cartesian frame $dt, dx^1,\dots,dx^4$, and so for an asymptotically Minkowski operator whose data at
$\rho = 0$ are these. Then $\hat P$ is tf-admissible with every weight $\beta\in(0,2)$.

*Proof.* By Lemma 5.6 take $\Theta = \mathrm{Id}$, and as the data act componentwise take $N = 1$. *The roots.*
$I(\lambda) = -\lambda^2+2\lambda+\Delta_{\mathbb S^3}$ is $-(\lambda+\ell)(\lambda-\ell-2)$ on $\mathcal H_\ell$, so
$\mathrm{spec}_b = \{-\ell,\ell+2:\ell\ge0\}$ and $(0,2)$ is an indicial gap (sympy, `checks_c.py`). *The operator.*
$N_{\mathrm{tf}}(\hat\sigma) = e^{-i\hat\sigma\hat r}(\Delta_e-\hat\sigma^2)e^{i\hat\sigma\hat r}$, $\Delta_e\ge0$ the
Euclidean Laplacian on $\mathbb R^4$: $e^{-i\hat\sigma\hat r}\Delta_ee^{i\hat\sigma\hat r} = \Delta_e-2i\hat\sigma
(\partial_{\hat r}+\frac3{2\hat r})+\hat\sigma^2$, $\partial_{\hat r} = -\hat\rho^2\partial_{\hat\rho}$, and $\hat r^2
\Delta_e = -(\hat\rho\partial_{\hat\rho})^2+2\hat\rho\partial_{\hat\rho}+\Delta_{\mathbb S^3}$, which is (4.1) with $S_0
= 0$. (This is the record's 10.17 (i).) $N_{\mathrm{tf}}(\hat\sigma)$ commutes with rotations, so with the projections
$\Pi_\ell$ onto $\mathcal H_\ell$ in $\omega$, which are averages of rotations against the character of $\mathcal H_\ell$
and so bounded on every space of Definition 4.1 whose order $\mathsf r$ is rotation-invariant (the rotations act
isometrically on them, strongly continuously); the orders $\mathsf r_\pm$ are, and $\mathsf r_{\mathrm{mid}}$ is
constant. For a distribution $w$ on $\mathrm{tf}^\circ$, $\Pi_\ell w = \sum_mw_m(\hat r)Y_m(\omega)$ with $(Y_m)$ an
orthonormal basis of $\mathcal H_\ell$ and $w_m$ distributions on $(0,\infty)$.

*(ii).* Let $w\in\ker_{\mathcal X_{\mathrm{tf},\theta}}N_{\mathrm{tf}}(e^{i\theta})$, $\beta\in(0,2)$. By Theorem 4.3 (5)
(with $\bar S = 0$), $w\in\mathcal A^{\frac32-\epsilon,-\beta'}(\mathrm{tf})$ for all $\epsilon>0$, $\beta'\in(0,2)$; so
are its components $w_m$, and $u_m := e^{i\hat\sigma\hat r}w_m$ solves the equation of Lemma 5.4 (a), weakly and hence
classically, so $u_m = c_1f_1+c_2f_2$. If $\theta\in(0,\pi)$, $|u_m|\le Ce^{-\hat r\sin\theta}\hat r^{-1}$, so $c_2 = 0$
by Lemma 5.4 (c). If $\theta = 0$, $w_m = c_1g_1+c_2e^{-2i\hat r}g_2$ with $g_1,g_2\in\mathcal A^{3/2}$ (Lemma 5.4 (b));
then $c_2e^{-2i\hat r}g_2 = w_m-c_1g_1$ is conormal, while $\hat r\partial_{\hat r}(e^{-2i\hat r}g_2) = e^{-2i\hat
r}(-2i\hat rg_2+\hat r\partial_{\hat r}g_2)$ has size $2|c_2|\hat r^{-1/2}(1+o(1))$, not $O(\hat r^{-3/2+\epsilon})$; so
$c_2 = 0$. If $\theta = \pi$, $\hat\sigma^2 = 1$ again and $w_m = e^{i\hat r}u_m = c_1e^{2i\hat r}g_1+c_2g_2$, and the
same argument gives $c_1 = 0$. In each case one coefficient remains, and by Lemma 5.4 (d) $|w_m|\ge c\,\hat r^{-2-\ell}$
as $\hat r\to0$ unless it vanishes, while $w_m = O(\hat r^{-\beta'})$ with $\beta'<2\le2+\ell$. So $w = 0$.

*(iii).* Take $s := 2$ (allowed by Theorem 4.3 (3)), so that $\mathcal X^*_{\mathrm{tf},0}\subset H^{0,(-\mathsf r_+-
\alpha_+-1,-q+2)}_{\mathrm{sc},b}$, $q = 2-\beta\in(0,2)$. Here $N_{\mathrm{tf}}(1)^{*h} = N_{\mathrm{tf}}(1)$, because
$e^{\mp i\hat r}$ are adjoint to each other and $\Delta_e-1$ is symmetric for $|d\hat x|$. Let $v$ be in the kernel; then
$u := e^{i\hat r}v$ solves $(\Delta_e-1)u = 0$, so $\Pi_\ell v = \sum_m(c_{1m}e^{-i\hat r}f_1+c_{2m}e^{-i\hat r}f_2)Y_m =
\sum_m(c_{1m}g_1+c_{2m}e^{-2i\hat r}g_2)Y_m$, with $f_j$ at $\theta = 0$. *At sctf.* Near $R_{\mathrm{out}}$, the zero
section, the decay order of $\mathcal X^*_{\mathrm{tf},0}$ is the constant $\mathsf r'_0 := -(\mathsf r_++\alpha_+)
(R_{\mathrm{out}})-1>-\frac12$, as $\mathsf r_++\alpha_+<-\frac12$ there ($\bar S = 0$). Let
$Q\in\Psi^{0,0}_{\mathrm{sc}}$ be the identity microlocally near the zero section over sctf and microsupported where that
order is constant. By Lemma 5.5 with $\kappa = -2$, $Q(\chi_\infty e^{-2i\hat r}g_2Y_m)\in H^{\infty,\infty}$; with
$\kappa = 0$, $(I-Q)(\chi_\infty g_1Y_m) \in H^{\infty,\infty}$. Since $Q\chi_\infty\Pi_\ell v\in H^{0,\mathsf r'_0}$, it
follows that $\chi_\infty\sum_mc_{1m} g_1Y_m\in H^{0,\mathsf r'_0}$, that is, $\int^\infty|g_1|^2\hat r^{2\mathsf
r'_0}\hat r^3\,d\hat r\cdot\sum_m|c_{1m}|^2< \infty$. By Lemma 5.4 (b), $|g_1|\ge\frac12|c_1|\hat r^{-3/2}$ for $\hat r$
large, and $\int^\infty\hat r^{2\mathsf r'_0} d\hat r = \infty$ as $\mathsf r'_0>-\frac12$. So all $c_{1m} = 0$. *At
ztf.* Then $\Pi_\ell v = \sum_mc_{2m}e^{-i\hat r} f_2Y_m$, which by Lemma 5.4 (d) has size at least
$c\,(\sum_m|c_{2m}|^2)^{1/2}\hat r^{-2-\ell}$ as $\hat r\to0$, while $\mathcal X^*_{\mathrm{tf},0}$ has b-weight $-q$ at
ztf: $\int_0\hat r^{2(q-2-\ell)}\frac{d\hat r}{\hat r}<\infty$ would need $q>2+\ell$, false as $q<2$. So $c_{2m} = 0$,
and $v = 0$. $\square$

The proof is [Hin26c]'s, run on the spaces of Theorem 4.3 for (iii); his (iii), on $e^{-2i/\rho_{\mathrm{sctf}}}\mathcal
A^{a,-2+\beta}$, is the same computation. The range $(0,2)$ is sharp at $\ell = 0$, as the record's 10.20 (b) notes.

## 6. Low energies ([Hin26c] Theorem 9.41 and Corollary 9.43 at $n = 4$)

For $\sigma\ne0$ with $\mathrm{Im}\,\sigma\ge0$ write $\varsigma := |\sigma|$, $\theta := \arg\sigma\in[0,\pi]$ and
$\hat\sigma := \sigma/\varsigma = e^{i\theta}$. $S_\varsigma$ is the dilation of section 4.1, $(S_\varsigma w)(\hat x) =
w(\hat x/\varsigma)$, applied to functions supported in $\{\rho<\rho_1\}$, so that $\hat\rho = \rho/\varsigma$ and $\hat
r = \varsigma r$. The spaces on tf are those of Definition 4.1, and $\varphi_\infty$ is its cut-off, which vanishes on
$\{\hat\rho\ge1\}$ (section 4.4). $\rho = 1/r$ is a function on all of $\bar X$, and $\chi_\partial$ is that of section
2.6.

### 6.1 The spaces

**Definition 6.1 (the low-energy spaces).** Let $s\in\mathbb R$, $k\in\mathbb N_0$, $\mathsf r$ a decay order as in
Definition 4.1, $l,q\in\mathbb R$ and $\varsigma\in(0,1]$. For $u$ on $\bar X$, extendible at $\partial_\sharp X$, put

$$\|u\|^2_{(s;k),(\mathsf r,l,q),\varsigma} := \varsigma^{-2q}\|(1-\chi_\partial)u\|^2_{\bar H^{s+k}}+\varsigma^{-2(l+2)}
\|S_\varsigma(\chi_\partial u)\|^2_{H^{(s;k),(\mathsf r,q-l)}_{\mathrm{sc},b;b}},\tag{6.1}$$

and let $\mathcal H^{(s;k),(\mathsf r,l,q)}_\varsigma$ be the space of those $u$ for which it is finite; $\dot{\mathcal
H}^{(s;k),(\mathsf r,l,q)}_\varsigma$ is defined with $\dot H^{s+k}$ in the first term. $k = 0$ is omitted from the
notation.

The three orders sit at the three faces of the low-energy picture: $\mathsf r$ at sctf, as a function of the frequencies
of tf; $l$ at tf; $q$ at zf. Near zf the norm is a b-norm on $\bar X$ with weight $l-q$, near tf it is the norm of tf
with weight $q-l$ at ztf, and the powers of $\varsigma$ make the two agree where they overlap (Lemma 6.2 (a)). This is
the form [Hin26c] (3.46) gives the norm of $H^{(s;k),(\mathsf r,l,q)}_{(\mathrm{sc}\text{-}b,\varsigma);b}$ near zf and
near tf, at $n = 4$; below, only Definition 6.1 is used, and no other description of these spaces is claimed.

The dilation acts on frequencies by $(\xi,\eta)\mapsto(\xi/\varsigma,\eta/\varsigma)$: a scattering covector $\xi\,dr+
r\eta$ at $x$ is $\hat\xi\,d\hat r+\hat r\hat\eta$ at $\hat x = \varsigma x$ with $\hat\xi = \xi/\varsigma$, $\hat\eta =
\eta/\varsigma$. For a decay order $\mathsf r$ on the boundary face over sctf put

$$\mathsf r_\varsigma(\omega,\xi,\eta) := \mathsf r(\omega,\xi/\varsigma,\eta/\varsigma),$$

an order on the boundary face over $\partial X$ (the dilation of the fibres extends to their radial compactification).

**Lemma 6.2.** Let $s,k,\mathsf r,l,q$ be as in Definition 6.1. There is $\varsigma_1>0$ such that the following hold for
$\varsigma\in(0,\varsigma_1]$, with constants independent of $\varsigma$, and likewise for the dotted spaces.

(a) (*Near zf.*) If $u$ is supported in $\{\rho\ge\varsigma\}$, then $\|u\|_{(s;k),(\mathsf r,l,q),\varsigma}$ is
equivalent to $\varsigma^{-q}\|u\|_{\bar H^{s+k,l-q}_b}$. If $u$ is supported in $\{\rho\ge\rho_*\}$ for a fixed
$\rho_*>0$, it is equivalent to $\varsigma^{-q}\|u\|_{\bar H^{s+k}}$, with constants depending on $\rho_*$ (and
$\varsigma\le\rho_*$).

(b) (*Multipliers.*) Let $\phi\in C^\infty([0,\infty))$ be constant on $[0,a]$ and on $[M,\infty)$, $0<a<M$, and let
$\rho_c\in(0,\frac1{2R_1}]$. Multiplication by $\phi(\rho/\varsigma)$ and by $\phi(\rho/\rho_c)$ is bounded on
$\mathcal H^{(s;k),(\mathsf r,l,q)}_\varsigma$, for $\varsigma\le\varsigma_1(a,M,\rho_c)$.

(c) (*Fixed $\varsigma$.*) $\mathcal H^{(s;k),(\mathsf r,l,q)}_\varsigma = \bar H^{(s;k),\mathsf r_\varsigma}$ (I.A
section 4.6), with equivalent norms (the constants depending on $\varsigma$); the weights $l,q$ do not enter. If $\mathsf
r$ is admissible with weight $\alpha_+$ for every $\sigma_0$ in a set $J\subset\mathbb R\setminus0$, then $\mathsf
r_\varsigma$ is admissible with weight $\alpha_+$ for every $\sigma_0\in\varsigma J$; and if $\mathsf r$ is constant near
$R_{\mathrm {out}}$ with $\mathsf r+\alpha_+<-\frac12+\bar S$ there, so is $\mathsf r_\varsigma$.

(d) (*Orders.*) The norm increases with $s$, $k$ and $\mathsf r$. For $\eta\in[0,1]$:
(d1) $\|u\|_{(s;k),(\mathsf r,l,q-\eta),\varsigma}\le\|u\|_{(s;k),(\mathsf r,l,q),\varsigma}$;
(d2) if $u$ is supported in $\{\rho\ge\rho_*\}$, $\|u\|_{(s;k),(\mathsf r,l,q-\eta),\varsigma}\le
C_{\rho_*}\varsigma^\eta \|u\|_{(s;k),(\mathsf r,l,q),\varsigma}$;
(d3) if $u$ is supported in $\{\rho\le M\varsigma\}$, $\|u\|_{(s;k),(\mathsf r,l,q),\varsigma}\le C_M\|u\|_{(s;k),
(\mathsf r,l,q-\eta),\varsigma}$.

(e) (*Trading b-regularity.*) For $m\in\mathbb N_0$, $\|u\|_{(s+m;k),(\mathsf r,l,q),\varsigma}\le C\|u\|_{(s;k+m),
(\mathsf r,l,q),\varsigma}$.

*Proof.* Take $\varsigma_1\le\frac1{4R_1}$, so that $\{\rho\ge\varsigma\}$ contains $\mathrm{supp}(1-\chi_\partial)$.

(a) $S_\varsigma(\chi_\partial u)$ is supported in $\{\hat\rho\ge1\}$, where $\varphi_\infty = 0$, so the second term of
(6.1) is $\varsigma^{-(l+2)}\|S_\varsigma(\chi_\partial u)\|_{H^{s+k}_{b,q-l-2}}$, with the b-space of Definition 2.1 at
the end at 0 of tf, $\varrho = \hat r$ (Definition 4.1; b-regularity is regularity there). Both this space and the
b-space at the end at $\infty$ of $\bar X$ ($\varrho = \rho$) are spaces of functions on the cylinder $(0,\infty)_r\times
\mathbb S^3$, and $S_\varsigma$ is $r\mapsto\varsigma r$. In $t := \log r$ the two ends use $-\log\hat r = -\log\varsigma
-t$ and $-\log\rho = t$: the dyadic pieces of one are translates of reflections of the pieces of the other, and the
charts differ by the inversion $y\mapsto y/|y|^2$ of a fixed neighbourhood of $\bar A$, which is bounded on $H^{s+k}$ of
functions supported there. By Lemma 2.2 (a), whose constants depend only on finitely many derivatives of the cut-offs and
on their overlap and are therefore uniform over translates, the two norms agree up to constants independent of
$\varsigma$ once the weights match. At order 0 they do:
$\|\hat r^{-(q-l-2)}S_\varsigma w\|_{L^2(\mu_b)} = \varsigma^{-(q-l-2)}\|\rho^{q-l-2}w\|_{L^2(\mu_b)}$, as $\mu_b$ is
dilation invariant. So the second term is equivalent to $\varsigma^{-(l+2)}\varsigma^{-(q-l-2)}\|\chi_\partial
u\|_{H^{s+k}_{b,l-q+2}} = \varsigma^{-q}\|\chi_\partial u\|_{H^{s+k}_{b,l-q+2}}$, and with the first term this is
$\varsigma^{-q}$ times the norm of Definition 2.8 with $a = l-q$. On $\{\rho\ge\rho_*\}$ the b-weights are bounded above
and below and $\bar H^{s+k,a}_b$ is $\bar H^{s+k}$ there.

(b) Both functions commute with $\chi_\partial$. On $\mathrm{supp}(1-\chi_\partial)\subset\{\rho\ge\frac1{2R_1}\}$,
$\phi(\rho/\varsigma) = \phi(M)$ once $\varsigma\le\frac1{2R_1M}$, and $\phi(\rho/\rho_c)$ is a fixed smooth function.
On tf, $\phi(\rho/\varsigma) = \phi(\hat\rho)$, which is smooth on $\mathrm{tf} = [0,\infty]_{\hat\rho}\times\mathbb S^3$
and constant near both ends, hence a multiplier of the sc-b;b spaces; and $\phi(\rho/\rho_c) = \phi(\varsigma\hat\rho/
\rho_c)$ is constant on $\{\hat\rho\le1\}$ once $\varsigma\le a\rho_c$, while $(\hat\rho\partial_{\hat\rho})^j\phi
(\varsigma\hat\rho/\rho_c) = ((t\partial_t)^j\phi)(\varsigma\hat\rho/\rho_c)$ is bounded, so Lemma 2.2 (b) applies near
ztf, uniformly in $\varsigma$.

(c) Away from $\partial X$ both norms are that of $\bar H^{s+k}$. For fixed $\varsigma$, $S_\varsigma(\chi_\partial u)$
is supported in $\{\hat\rho\le\rho_1/\varsigma\}$, on which $\rho_{\mathrm{ztf}}$ is bounded below, so near ztf the norm
is that of $H^{s+k}$ on a compact set and $l$, $q$ only change constants. Near sctf, for $A = \mathrm{Op}(a)$,

$$S_\varsigma\,\mathrm{Op}(a)\,S_\varsigma^{-1} = \mathrm{Op}(a_\varsigma),\qquad a_\varsigma(\hat x,\hat\zeta) :=
a(\hat x/\varsigma,\varsigma\hat\zeta),$$

exactly (substitute $y = \hat y/\varsigma$, $\zeta = \varsigma\hat\zeta$ in the oscillatory integral). If $a$ is an
elliptic symbol of order $(s,\mathsf r_\varsigma)$, then $a_\varsigma$ is one of order $(s,\mathsf r)$, as $(\hat x,\hat
\zeta)\mapsto(\hat x/\varsigma,\varsigma\hat\zeta)$ extends to a diffeomorphism of the compactified phase space. So
$S_\varsigma$ maps $H^{s,\mathsf r_\varsigma}_{\mathrm{sc}}$ isomorphically onto $H^{s,\mathsf r}_{\mathrm{sc}}$ ([HJS]
Definition 10.2), and the same holds with $k$ b-derivatives, since $S_\varsigma\langle x\rangle D_xS_\varsigma^{-1} =
\langle\hat x/\varsigma\rangle\varsigma D_{\hat x}$ lies in the span of the fields $\langle\hat x\rangle D_{\hat x}$ over
$C^\infty(\overline{\mathbb R^4})$. For admissibility, let $D_\varsigma(\omega,\xi,\eta) := (\omega,\varsigma\xi,
\varsigma\eta)$ on the boundary face, so $\mathsf r_\varsigma = \mathsf r\circ D_\varsigma^{-1}$. With $G_{\sigma_0} =
2\sigma_0\xi+\xi^2+|\eta|^2$ (I.A Lemma 4.4), $G_{\varsigma\sigma_0}\circ D_\varsigma = \varsigma^2G_{\sigma_0}$, so
$D_\varsigma$ maps $\Sigma^\partial_{\sigma_0}$, $R_{\sigma_0,\mathrm{in}} = \{\xi = -2\sigma_0,\eta = 0\}$ and
$R_{\mathrm{out}}$ onto $\Sigma^\partial_{\varsigma\sigma_0}$, $R_{\varsigma\sigma_0,\mathrm{in}}$ and
$R_{\mathrm{out}}$; and in (4.4) of I.A each of $\partial_\xi p\,(\rho\partial_\rho+\eta\cdot\partial_\eta)$,
$(\eta\cdot\partial_\eta p) \partial_\xi$ and $H^{\mathbb S^3}_p$ scales so that $(D_\varsigma)_*\mathsf V_{G_{\sigma_0}}
= \varsigma^{-1}\mathsf V_{G_{\varsigma\sigma_0}}$. Hence (O2) for $\mathsf r$ at $\sigma_0$ is (O2) for $\mathsf
r_\varsigma$ at $\varsigma \sigma_0$ ($\mathrm{sgn}\,\varsigma\sigma_0 = \mathrm{sgn}\,\sigma_0$), and (O1), (O3) involve
only the values at the radial sets and quantities on $\partial X$.

(d) Monotonicity in $s,k,\mathsf r$ holds for each term. (d1): $\varsigma^{\eta-q}\le\varsigma^{-q}$, and the order
$q-\eta-l$ at ztf is weaker than $q-l$. (d2) is (a). (d3): for $\varsigma<\frac1{2R_1M}$ the first term vanishes, and
on $\{\hat\rho\le M\}$, $\rho_{\mathrm{ztf}}\ge(1+M)^{-1}$.

(e) The first term and the part near ztf are norms of $H^{s+k+m}$ on both sides. Near sctf it suffices, by induction, to
take $m = 1$ and show $H^{(s;k+1),\mathsf r}\subset H^{(s+1;k),\mathsf r}$ (I.A section 4.6) on $\mathbb R^4_{\hat x}$,
which does not involve $\varsigma$. Let $V_j := \langle x\rangle D_{x_j}$ and $w := V^\beta u$, $|\beta|\le k$. Then
$w$ and every $V_jw$ lie in $H^{s,\mathsf r}$, since $V_jV^\beta$ is a combination of the $V^\gamma$, $|\gamma|\le
k+1$, with coefficients in $C^\infty(\overline{\mathbb R^4})$. Off the zero section of the boundary face the system
$(V_j)$ is elliptic in $\Psi^{1,1}$ (proof of I.A Lemma 4.10), so $w\in H^{s+1,\mathsf r+1}\subset H^{s+1,\mathsf r}$
microlocally there (I.A (C5)); near the zero section, at finite frequencies, $B\in\Psi^{-\infty,0}$ maps $H^{s,\mathsf
r}$ to $H^{s+1,\mathsf r}$. With the norms, this is the claim. $\square$

### 6.2 The model at tf

On $\{\rho<\rho_1\}$ let

$$\hat P_{\mathrm{mod}}(\sigma) := 2i\sigma\rho\big(\rho\partial_\rho-\tfrac32-S_0\big)+\rho^2N(P^{(0)}),\qquad E_\sigma
:= \hat P(\sigma)-\hat P_{\mathrm{mod}}(\sigma) = \rho^2\big(P^{(0)}-N(P^{(0)})\big)-2i\sigma\rho(S-S_0)-i\sigma Q+
\sigma^2g_{00},\tag{6.2}$$

by (1.1). By (4.2), $S_\varsigma\hat P_{\mathrm{mod}}(\sigma)S_\varsigma^{-1} = \varsigma^2N_{\mathrm{tf}}(\hat\sigma)$.
Let $H_0$ also denote the matrix $H(0,\omega)$, extended to $\{\rho<\rho_1\}$ independently of $\rho$, and $\hat
P_{\mathrm{mod}}(\sigma)^{*h_0}$ the adjoint for $|dx|$ and $H_0$. Since $\|S_\varsigma w\|_{L^2(|d\hat x|)} =
\varsigma^2\|w\|_{L^2(|dx|)}$ and $H_0$ does not depend on $\rho$, $S_\varsigma\hat P_{\mathrm{mod}}(\sigma)^{*h_0}
S_\varsigma^{-1} = \varsigma^2N_{\mathrm{tf}}(\hat\sigma)^{*h}$, the adjoint of Theorem 4.3. Put $E^*_\sigma := \hat
P(\sigma)^{*h}-\hat P_{\mathrm{mod}}(\sigma)^{*h_0}$.

**Lemma 6.3.** Let $s,k,\mathsf r,q$ be given. There is $C$ such that for $\rho_c\in(0,\frac{\rho_1}2]$, $\varsigma\in
(0,1]$, $\theta\in[0,\pi]$ and $u$ supported in $\{\rho\le\rho_c\}$,

$$\varsigma^{-2}\|S_\varsigma E_\sigma u\|_{H^{(s-2;k),(\mathsf r+1,q-2)}_{\mathrm{sc},b;b}}\le C(\rho_c+\varsigma)
\|S_\varsigma u\|_{H^{(s;k),(\mathsf r,q)}_{\mathrm{sc},b;b}},\tag{6.3}$$

and (6.3) holds for $E^*_\sigma$ with the orders $(s,\mathsf r,q)$ and $(s-2,\mathsf r+1,q-2)$ replaced by $(-s+2,
-\mathsf r-1,-q+2)$ and $(-s,-\mathsf r,-q)$.

*Proof.* Write $P^{(0)}-N(P^{(0)}) = \rho B_1$, $S-S_0 = \rho S_1$, $Q = \rho^3\tilde Q$ and $g_{00} = \rho^2\tilde g$,
with $B_1\in\mathrm{Diff}^2_b$, $\tilde Q\in\mathrm{Diff}^1_b$ and $S_1$, $\tilde g$ smooth (section 1.1 and (H2)).
Since $\rho = \varsigma\hat\rho$, $\sigma = \varsigma\hat\sigma$ and $\rho\partial_\rho = \hat\rho\partial_{\hat\rho}$,

$$\varsigma^{-2}S_\varsigma E_\sigma S_\varsigma^{-1} = \hat\rho^2\rho B_1-2i\hat\sigma\hat\rho\,\rho S_1-i\hat\sigma
\hat\rho\,\rho^2\tilde Q+\varsigma^2\hat\sigma^2\hat\rho^2\tilde g,$$

where $\rho$ stands for $\varsigma\hat\rho$ and every coefficient is a smooth function of $(\varsigma\hat\rho,\omega)$.
Such a function has $(\hat\rho\partial_{\hat\rho})^j\partial_\omega^\gamma f(\varsigma\hat\rho,\omega) = ((\rho\partial
_\rho)^j\partial^\gamma_\omega f)(\varsigma\hat\rho,\omega)$, bounded independently of $\varsigma$, and on $\{\hat\rho
\le2\}$ its $\hat\rho$-derivatives carry powers of $\varsigma$; so the operators $B_1$, $\tilde Q$, $S_1$, $\tilde g$ lie
in bounded sets of their classes, both near ztf (b-operators) and near sctf (smooth up to $\hat\rho = 0$). Split
$S_\varsigma u = \varphi_\infty S_\varsigma u+(1-\varphi_\infty)S_\varsigma u$, and note that the operator is
differential.

*Near sctf*, on $\{\hat\rho\le2\}$, write $\rho = \varsigma\hat\rho$: the four terms are $\varsigma\hat\rho\cdot\hat
\rho^2B_1$, $\varsigma\hat\rho\cdot(-2i\hat\sigma\hat\rho S_1)$, $\varsigma^2\hat\rho^2\cdot(-i\hat\sigma\hat\rho\tilde
Q)$ and $\varsigma^2\hat\rho^2\cdot\hat\sigma^2\tilde g$. Near sctf $\hat\rho^2\mathrm{Diff}^2_b\subset\mathrm{Diff}^2_{
\mathrm{sc}}$ and $\hat\rho\,\mathrm{Diff}^1_b\subset\mathrm{Diff}^1_{\mathrm{sc}}$, these classes map $H^{(s;k),\mathsf
r}_{\mathrm{sc}}$ to $H^{(s-2;k),\mathsf r}_{\mathrm{sc}}$ (I.A section 4.6: the commutators of $\langle\hat x\rangle
D_{\hat x}$ with $\mathrm{Diff}^{m,0}_{\mathrm{sc}}$ lie in $\mathrm{Diff}^{m,0}_{\mathrm{sc}}$), and each factor
$\hat\rho$ raises the decay order by one. So this part is bounded by $C\varsigma$.

*Near ztf*, on $\{\hat\rho\ge\frac12\}$, the operator is $\hat\rho^2$ times $\rho
B_1-2i\hat\sigma(\rho/\hat\rho)S_1-i\hat \sigma(\rho^2/\hat\rho)\tilde Q+\varsigma^2\hat\sigma^2\tilde g$. On the support
of $u$, $\rho\le\rho_c$; replacing $\rho$ by $\rho\tilde\chi(\rho/\rho_c)$, with $\tilde\chi = 1$ on $[0,1]$ and $0$ on
$[2,\infty)$, does not change the operator there, and $\rho\tilde\chi(\rho/\rho_c)$ has all b-derivatives bounded by
$C\rho_c$. Also $\rho/\hat\rho = \varsigma$. So the bracket is a b-operator of order 2 with coefficients bounded by
$C(\rho_c+\varsigma)$ in $C^\infty_b$, which maps $H^{s+k}_{b,q-2}$ to $H^{s+k-2}_{b,q-2}$ with that norm (Lemma 2.2
(c)), and $\hat\rho^2$ maps the ztf order $q$ to $q-2$ (Lemma 2.2 (b)).

*The adjoint.* $E^*_\sigma = E_\sigma^{*h}+(\hat P_{\mathrm{mod}}(\sigma)^{*h}-\hat P_{\mathrm{mod}}(\sigma)^{*h_0})$.
The adjoint of each term of (6.2) for $|dx| = \rho^{-5}d\rho\,d\omega$ and $H$ is of the same form
($\rho^a\mathrm{Diff}^m_b$ is preserved, and $\sigma$ becomes $\bar\sigma$; I.A section 1.3, Remark (a)). Writing $H =
H_0(I+\rho K)$ with $K$ smooth,

$$A^{*h}-A^{*h_0} = (I+\rho K)^{-1}A^{*h_0}(I+\rho K)-A^{*h_0} = (I+\rho K)^{-1}[A^{*h_0},\rho K],\qquad A := \hat
P_{\mathrm{mod}}(\sigma),$$

and $[\rho^2N(P^{(0)})^{*h_0},\rho K]\in\rho^3\mathrm{Diff}^1_b$, $[\sigma\rho(\rho\partial_\rho)^{*h_0},\rho K]\in\sigma
\rho^2C^\infty$: the forms of the first two terms of (6.2). The two estimates above then hold with the dual orders.
$\square$

### 6.3 The theorem

For $\sigma\ne0$ with $\mathrm{Im}\,\sigma\ge0$ let $\Sigma$ be a sector of Corollary 5.2 (b) containing $\arg\sigma$
($\Sigma_+ = [0,\frac\pi4]$, $\Sigma_m$, $\Sigma_-$; either one at $\frac\pi4$, $\frac{3\pi}4$), and $\mathsf r :=
\mathsf r_\Sigma$, with the weight $\alpha_+$ of Corollary 5.2. Put

$$\mathcal X_\sigma := \{u\in\mathcal H^{s,(\mathsf r+\alpha_+,\alpha,0)}_\varsigma:\hat P(\sigma)u\in\mathcal
Y_\sigma\},
\quad\mathcal Y_\sigma := \mathcal H^{s-1,(\mathsf r+\alpha_++1,\alpha+2,0)}_\varsigma,\quad\mathcal X^*_\sigma := \{v
\in\dot{\mathcal H}^{1-s,(-\mathsf r-\alpha_+-1,-\alpha-2,0)}_\varsigma:\hat P(\sigma)^{*h}v\in\dot{\mathcal H}^{-s,
(-\mathsf r-\alpha_+,-\alpha,0)}_\varsigma\}.\tag{6.4}$$

By Lemma 6.2 (c) these are, at each $\sigma$, the spaces $\mathcal X_\sigma$, $\mathcal Y_\sigma$, $\mathcal X^*_\sigma$
of I.A Theorem 7.2 with the decay order $\mathsf r_\varsigma$, and I.A Theorem 7.2 applies to them: for $\theta\in
\Theta_\pm$, $\mathsf r_{\pm,\varsigma}$ is admissible for $\mathrm{Re}\,\sigma = \varsigma\cos\theta\in\varsigma J_\pm$
(section 4.3), and (1) of I.A Theorem 7.2 applies; for $\theta\in(0,\pi)$, $\mathsf r_\varsigma$ is constant near
$R_{\mathrm{out}}$ with the threshold, $\mathrm{Im}\,\sigma>0$, and (2) applies.

*Augmentations* ([Hin26c] Remark 9.42). Let $m_1,m_2\in\mathbb N_0$ and $\psi_1,\dots,\psi_{m_1}$, $\phi_1,\dots,
\phi_{m_2}\in C_c^\infty(X^\circ;E)$, $X^\circ := \{r>r_0\}$, and

$$\mathcal P(\sigma)(u,c) := \Big(\hat P(\sigma)u+\sum_ic_i\psi_i,\ \big(\langle u,\phi_j\rangle_h\big)_j\Big),\qquad
\mathcal P(\sigma)^*(v,d) := \Big(\hat P(\sigma)^{*h}v+\sum_jd_j\phi_j,\ \big(\langle v,\psi_i\rangle_h\big)_i\Big),
\tag{6.5}$$

with $\langle\cdot,\cdot\rangle_h$ the $h$-weighted $L^2(|dx|)$ pairing, on $\mathcal X_\sigma\oplus\mathbb C^{m_1}\to
\mathcal Y_\sigma\oplus\mathbb C^{m_2}$ and $\mathcal X^*_\sigma\oplus\mathbb C^{m_2}\to\dot{\mathcal H}^{-s,(-\mathsf r-
\alpha_+,-\alpha,0)}_\varsigma\oplus\mathbb C^{m_1}$. Norms on the sums add $|c|$, $|d|$. The case $m_1 = m_2 = 0$ is
$\hat P(\sigma)$ itself. In place of (Z) we then assume

(Z$_{\mathcal P}$) $\mathcal P(0):\mathcal X_0\oplus\mathbb C^{m_1}\to\mathcal Y_0\oplus\mathbb C^{m_2}$ is invertible,

with $\mathcal X_0$, $\mathcal Y_0$ of (3.1); for $m_1 = m_2 = 0$ this is (Z).

**Theorem 6.4 ([Hin26c] Theorem 9.41 at $n = 4$, on $E$, with Remark 9.42).** Assume (H1)-(H4), (G), (Z$_{\mathcal P}$)
and (TF), with $s>\frac12+\vartheta_{\mathcal H}$ constant, and let $\alpha_+\in\mathbb R$.

(1) (*Uniform estimates.*) For every $k\in\mathbb N_0$ there are $c_k>0$, non-increasing in $k$, and $C_k$ such that for
$0<|\sigma|\le c_k$ with $\mathrm{Im}\,\sigma\ge0$, and $(u,c)\in\mathcal X_\sigma\oplus\mathbb C^{m_1}$ with $\mathcal
P(\sigma)(u,c) = (f,e)$,

$$\|u\|_{(s;k),(\mathsf r+\alpha_+,\alpha,0),\varsigma}+|c|\le C_k\big(\|f\|_{(s-1;k),(\mathsf r+\alpha_++1,\alpha+2,
0),\varsigma}+|e|\big),\tag{6.6}$$

in the strong sense: if the right side is finite, so is the left.

(2) (*The adjoint.*) There is $C$ such that for $0<|\sigma|\le c_0$ with $\mathrm{Im}\,\sigma\ge0$, and $(v,d)\in
\mathcal X^*_\sigma\oplus\mathbb C^{m_2}$ with $\mathcal P(\sigma)^*(v,d) = (g,b)$,

$$\|v\|_{(1-s),(-\mathsf r-\alpha_+-1,-\alpha-2,0),\varsigma}+|d|\le C\big(\|g\|_{(-s),(-\mathsf r-\alpha_+,-\alpha,0),
\varsigma}+|b|\big).\tag{6.7}$$

(3) (*Invertibility.*) For $0<|\sigma|\le c_0$ with $\mathrm{Im}\,\sigma\ge0$, $\mathcal P(\sigma):\mathcal X_\sigma
\oplus\mathbb C^{m_1}\to\mathcal Y_\sigma\oplus\mathbb C^{m_2}$ is invertible.

(4) (*Derivatives in $\sigma$; $m_1 = m_2 = 0$.*) For $j,k\in\mathbb N_0$ there are $c_{j,k}\in(0,c_0]$ and $C$ such that
for $0<|\sigma|\le c_{j,k}$ with $\mathrm{Im}\,\sigma\ge0$,

$$\|(\sigma\partial_\sigma)^j\hat P(\sigma)^{-1}f\|_{(s+j;k),(\mathsf r+\alpha_+,\alpha,0),\varsigma}\le C\|f\|_{(s-1;
k+j),(\mathsf r+\alpha_++1,\alpha+2,0),\varsigma}.\tag{6.8}$$

Here $(\sigma\partial_\sigma)^j\hat P(\sigma)^{-1}$ is the derivative of I.A Theorem 7.2 (6), defined on $\bar H^{(s+
\epsilon-1;j),\mathsf r_\varsigma+\epsilon+\alpha_++1}$ and extended to the space on the right by (6.8).

(5) (*Other weights.*) (1)-(4) hold for every $\alpha$ with $\alpha+2\in(\beta_-,\beta_+)$, the gap of (G): there (Z)
holds by Theorem 3.1 (4), and (TF) with weight $\alpha+2$ by Corollary 5.2 (c).

(G) is the gap hypothesis of section 1.2. (6.6) is [Hin26c] (9.119) and (6.8) is (9.120), on the spaces of Definition
6.1. Remark 6.7 lists what differs from the source.

### 6.4 Proof of (1)

Fix $k$. Constants $C$ do not depend on $\varsigma$, on $\theta$, or on $\rho_c$ below, unless written $C_{\rho_c}$.
Let $\phi_z\in C^\infty([0,\infty))$ vanish on $[0,2]$ and equal 1 on $[4,\infty)$, $\chi_0\in C^\infty([0,\infty))$
equal 1 on $[0,\frac12]$ and vanish on $[1,\infty)$, and

$$\chi_{\mathrm{zf}} := \phi_z(\rho/\varsigma),\qquad\chi_{\mathrm{tf}} := \chi_0(\rho/\rho_c),\qquad0<\rho_c\le\rho_c^0
:= \min\big(\tfrac1{2R_1},\tfrac{\rho_1}2,\tfrac1{2R}\big),$$

where $\mathrm{supp}\,\psi_i\cup\mathrm{supp}\,\phi_j\subset\{r\le R\}$. Then $\chi_\partial = 1$ on $\mathrm{supp}\,
\chi_{\mathrm{tf}}$, $\chi_{\mathrm{tf}}\psi_i = 0 = \chi_{\mathrm{tf}}\phi_j$, and for $\varsigma\le\rho_c/8$,
$\chi_{\mathrm{zf}} = 1$ on $\mathrm{supp}(1-\chi_{\mathrm{tf}})$ and on $\mathrm{supp}\,\psi_i\cup\mathrm{supp}\,
\phi_j$. Write $\|\cdot\|_{(l,q)}$ for $\|\cdot\|_{(s;k),(\mathsf r+\alpha_+,l,q),\varsigma}$ and $\|\cdot\|'_{(l,q)}$
for $\|\cdot\|_{(s-1;k),(\mathsf r+\alpha_++1,l,q),\varsigma}$.

*Finiteness.* Let $\mathcal P(\sigma)(u,c) = (f,e)$ with the right side of (6.6) finite. Then $\hat P(\sigma)u = f-\sum
c_i\psi_i\in\bar H^{(s-1;k),\mathsf r_\varsigma+\alpha_++1}$, so $u\in\bar H^{(s;k),\mathsf r_\varsigma+\alpha_+}$ by I.A
Theorem 7.2 (4), and $\|u\|_{(\alpha,0)}<\infty$ by Lemma 6.2 (c). This is what makes the absorptions below legitimate.

*Step 1 (zf).* For $\varsigma$ small, $\chi_{\mathrm{zf}}u$ is supported in $\{\rho\ge2\varsigma\}$, a compact subset of
$\bar X\setminus\partial X$ for fixed $\varsigma$, so $\chi_{\mathrm{zf}}u\in\bar H^{s+k}$ with compact support, and
$(\chi_{\mathrm{zf}}u,c)\in\mathcal X_0\oplus\mathbb C^{m_1}$ at the regularity $s+k$. (Z$_{\mathcal P}$) holds at the
regularity $s+k$ as well: the kernel of $\mathcal P(0)$ there lies in the kernel at $s$, and the index of $\mathcal
P(0)$, which is that of $\hat P(0)$ plus $m_1-m_2$, does not depend on the regularity by Theorem 3.1 (3). So by Lemma 6.2
(a), the bounded inverse of $\mathcal P(0)$ at $s+k$, and $\langle\chi_{\mathrm{zf}}u,\phi_j\rangle_h = \langle u,\phi_j
\rangle_h$,

$$\|\chi_{\mathrm{zf}}u\|_{(\alpha,0)}+|c|\le C\|\chi_{\mathrm{zf}}u\|_{\bar H^{s+k,\alpha}_b}+|c|\le C\big(\|\hat P(0)
(\chi_{\mathrm{zf}}u)+\textstyle\sum c_i\psi_i\|_{\bar H^{s+k-1,\alpha+2}_b}+|e|\big).$$

Since $\chi_{\mathrm{zf}}\psi_i = \psi_i$,

$$\hat P(0)(\chi_{\mathrm{zf}}u)+\textstyle\sum c_i\psi_i = \chi_{\mathrm{zf}}f-\chi_{\mathrm{zf}}(\sigma T+\sigma^2P_2)u
+[\hat P(0),\chi_{\mathrm{zf}}]u.$$

(i) By Lemma 6.2 (a), (b), $\|\chi_{\mathrm{zf}}f\|_{\bar H^{s+k-1,\alpha+2}_b}\le
C\|\chi_{\mathrm{zf}}f\|'_{(\alpha+2,0)} \le C\|f\|'_{(\alpha+2,0)}$.

(ii) Let $\chi'_{\mathrm{zf}} := \phi'(\rho/\varsigma)$ with $\phi' = 0$ on $[0,1]$, $1$ on $[2,\infty)$; it is 1 near
$\mathrm{supp}\,\chi_{\mathrm{zf}}$, so $\chi_{\mathrm{zf}}(\sigma T+\sigma^2P_2)u = \chi_{\mathrm{zf}}(\sigma T+\sigma^2
P_2)\chi'_{\mathrm{zf}}u$. On $\{\rho<\rho_1\}$, $\sigma T+\sigma^2P_2 = \sigma\rho B_T+\sigma^2\rho^2\tilde g$ with $B_T
:= 2i(\rho\partial_\rho-\frac32-S)-i\rho^{-1}Q\in\mathrm{Diff}^1_b$ by (1.1); $\rho B_T$ maps $\bar H^{s+k,\alpha+1}_b$
to $\bar H^{s+k-1,\alpha+2}_b$, and $\rho^2$ maps $\bar H^{s+k,\alpha}_b\supset\bar H^{s+k,\alpha+1}_b$ to $\bar H^{s+k,
\alpha+2}_b$. On $\{\rho\ge\frac{\rho_1}2\}$, $\sigma T+\sigma^2P_2$ is $\sigma$ times a first-order operator. So, by
Lemma 6.2 (a) with $q = -1$ and then (b), (d1),

$$\|\chi_{\mathrm{zf}}(\sigma T+\sigma^2P_2)u\|_{\bar H^{s+k-1,\alpha+2}_b}\le C\varsigma\|\chi'_{\mathrm{zf}}u\|_{\bar
H^{s+k,\alpha+1}_b}\le C\|\chi'_{\mathrm{zf}}u\|_{(\alpha,-1)}\le C\|u\|_{(\alpha,-\eta)},\qquad\eta\in(0,1].$$

(iii) $[\hat P(0),\chi_{\mathrm{zf}}] = \rho^2[P^{(0)},\chi_{\mathrm{zf}}]$ is $\rho^2$ times a first-order b-operator
whose coefficients, made of b-derivatives of $\phi_z(\rho/\varsigma)$, are bounded in $C^\infty_b$ independently of
$\varsigma$ and supported in $\{2\varsigma\le\rho\le4\varsigma\}$. With $\chi''_{\mathrm{zf}} := \phi''(\rho/\varsigma)$,
$\phi''\in C_c^\infty((1,8))$ equal to 1 on $[2,4]$, Lemma 6.2 (a), (d3) and (b) give

$$\|[\hat P(0),\chi_{\mathrm{zf}}]u\|_{\bar H^{s+k-1,\alpha+2}_b}\le C\|\chi''_{\mathrm{zf}}u\|_{\bar H^{s+k,\alpha}_b}
\le C\|\chi''_{\mathrm{zf}}u\|_{(\alpha,0)}\le C\|\chi''_{\mathrm{zf}}u\|_{(\alpha,-\eta)}\le C\|u\|_{(\alpha,-\eta)}.$$

(iv) $(1-\chi_{\mathrm{zf}})u$ is supported in $\{\rho\le4\varsigma\}$, so by (d3) and (b) $\|(1-\chi_{\mathrm{zf}})u\|
_{(\alpha,0)}\le C\|u\|_{(\alpha,-\eta)}$.

Together, for every $\eta\in(0,1]$ ([Hin26c] (9.121)),

$$\|u\|_{(\alpha,0)}+|c|\le C\big(\|f\|'_{(\alpha+2,0)}+|e|+\|u\|_{(\alpha,-\eta)}\big).\tag{6.9}$$

*Step 2 (tf).* By (G), fix $\eta\in(0,1]$ with $\beta_-<\alpha+2-\eta$ and $\alpha+2+\eta<\beta_+$, and put $q_\eta :=
-\alpha-\eta$, so that $2-q_\eta = \alpha+2+\eta$ lies in the gap and Corollary 5.2 (b) applies at $q = q_\eta$. Split
$u = \chi_{\mathrm{tf}}u+(1-\chi_{\mathrm{tf}})u$.

(v) $(1-\chi_{\mathrm{tf}})u$ is supported in $\{\rho\ge\rho_c/2\}$, so by (d2) and (b), $\|(1-\chi_{\mathrm{tf}})u\|
_{(\alpha,-\eta)}\le C_{\rho_c}\varsigma^\eta\|u\|_{(\alpha,0)}$.

(vi) Since $\chi_\partial = 1$ on $\mathrm{supp}\,\chi_{\mathrm{tf}}$, $\|\chi_{\mathrm{tf}}u\|_{(\alpha,-\eta)} =
\varsigma^{-(\alpha+2)}\|w\|_{H^{(s;k),(\mathsf r+\alpha_+,q_\eta)}_{\mathrm{sc},b;b}}$ with $w :=
S_\varsigma(\chi_{\mathrm {tf}}u)$. By (5.1), with $C_T$ its constant, uniform in $\theta\in\Sigma$,

$$\|w\|_{H^{(s;k),(\mathsf r+\alpha_+,q_\eta)}_{\mathrm{sc},b;b}}\le C_T\|N_{\mathrm{tf}}(\hat\sigma)w\|_{H^{(s-2;k),
(\mathsf r+\alpha_++1,q_\eta-2)}_{\mathrm{sc},b;b}},\qquad\varsigma^2N_{\mathrm{tf}}(\hat\sigma)w = S_\varsigma\big(
\chi_{\mathrm{tf}}f+[\hat P(\sigma),\chi_{\mathrm{tf}}]u-E_\sigma\chi_{\mathrm{tf}}u\big),$$

using $\chi_{\mathrm{tf}}\psi_i = 0$. The three terms, multiplied by $\varsigma^{-(\alpha+2)}\varsigma^{-2}$:

The first gives the tf part of $\|\chi_{\mathrm{tf}}f\|_{(s-2;k),(\mathsf r+\alpha_++1,\alpha+2,-\eta),\varsigma}$ (the
order at ztf is $-\eta-(\alpha+2) = q_\eta-2$), which by Lemma 6.2 (b), (d) is at most $C\|f\|'_{(\alpha+2,0)}$.

The second: $[\hat P(\sigma),\chi_{\mathrm{tf}}]$ is a first-order operator with coefficients supported in $\{\frac{\rho
_c}2\le\rho\le\rho_c\}$ and bounded, with their derivatives, by $C_{\rho_c}$ for $|\sigma|\le1$. As $\chi_\partial = 1$
there, the term is the full norm $\|[\hat P(\sigma),\chi_{\mathrm{tf}}]u\|_{(s-2;k),(\mathsf
r+\alpha_++1,\alpha+2,-\eta), \varsigma}$, which by Lemma 6.2 (a) with $q = -\eta$ is at most
$C_{\rho_c}\varsigma^\eta\|\tilde\chi u\|_{\bar H^{s+k-1}}$, $\tilde\chi$ a cut-off to
$\{\frac{\rho_c}4\le\rho\le2\rho_c\}$, and so by (a) and (b) at most $C_{\rho_c} \varsigma^\eta\|u\|_{(\alpha,0)}$.

The third, by Lemma 6.3, is at most $C(\rho_c+\varsigma)\varsigma^{-(\alpha+2)}\|w\|$.

Fix $\rho_c\le\rho^0_c$ with $C_TC\rho_c\le\frac14$, and let $\varsigma\le\rho_c/8$ with $C_TC\varsigma\le\frac14$. Then
the third term is absorbed, $\|w\|$ being finite, and

$$\|u\|_{(\alpha,-\eta)}\le C\|f\|'_{(\alpha+2,0)}+C_{\rho_c}\varsigma^\eta\|u\|_{(\alpha,0)}.$$

Inserted in (6.9) this gives $\|u\|_{(\alpha,0)}+|c|\le C(\|f\|'_{(\alpha+2,0)}+|e|)+C'_{\rho_c}\varsigma^\eta\|u\|
_{(\alpha,0)}$, and for $\varsigma\le c'_k$ with $C'_{\rho_c}(c'_k)^\eta\le\frac12$ the last term is absorbed. With
$c_k := \min_{k'\le k}c'_{k'}$ this is (6.6). $\square$

The argument is [Hin26c]'s: the zero energy estimate near zf, the tf estimate (9.118) near tf, and absorption through
the factor $\varsigma^\eta$; the source uses no symbolic estimate here, and neither does this proof. One step differs:
the source absorbs the model error $\hat P(\sigma)-\varsigma^2N_{\mathrm{tf}}$ through its vanishing at tf, (9.122), and
here it is absorbed through the factor $\rho_c+\varsigma$ of Lemma 6.3, with $\rho_c$ fixed small first.

### 6.5 Proof of (2) and (3)

*(2).* The proof of (1) at $k = 0$ applies to $(v,d)$ with $\mathcal P(\sigma)^*(v,d) = (g,b)$; $\|v\|_{(1-s),(-\mathsf
r-\alpha_+-1,-\alpha-2,0),\varsigma}$ is finite as $v\in\mathcal X^*_\sigma$. The changes are these.

In Step 1, in place of the bounded inverse of $\mathcal P(0)$: for $v\in\mathcal X^*_0$ and $d\in\mathbb C^{m_2}$,

$$\|v\|_{\dot H^{1-s,-\alpha-2}_b}+|d|\le C\big(\|\mathcal P(0)^*(v,d)\|_{\dot H^{-s,-\alpha}_b\oplus\mathbb C^{m_1}}
\big).\tag{6.10}$$

Indeed $\mathcal P(0)$ is invertible, so its Banach adjoint is, and by Green's formula of section 3.1, $\langle\mathcal
P(0)(u,c),(v,d)\rangle = \langle(u,c),\mathcal P(0)^*(v,d)\rangle$ for $u\in\mathcal X_0$; as $\|u\|_{\mathcal X_0}\ge
\|u\|_{\bar H^{s,\alpha}_b}$ and $\dot H^{-s,-\alpha}_b$ is the dual of $\bar H^{s,\alpha}_b$ (Lemma 2.9 (a)), the norm
of the functional $(u,c)\mapsto\langle\mathcal P(0)(u,c),(v,d)\rangle$ on $\mathcal X_0\oplus\mathbb C^{m_1}$ is at most
the right side of (6.10), and $\|v\|_{\dot H^{1-s,-\alpha-2}_b}$ is the norm of $v$ in $\mathcal Y_0^*$. The terms
(i)-(iv) are as before with $\hat P(0)^{*h}$, $\bar\sigma T^{*h}+\bar\sigma^2P_2$ (and $T^{*h}\in\rho\,\mathrm{Diff}^1_b$
near $\partial X$, $P_2^{*h} = P_2$) and $[\hat P(0)^{*h},\chi_{\mathrm{zf}}]\in\rho^2\mathrm{Diff}^1_b$, the weights
being those of (6.7) and the regularity $1-s$, resp. $-s$.

In Step 2 the weight moves the other way. Put $q^*_\eta := \eta-\alpha$; then $2-q^*_\eta = \alpha+2-\eta$ lies in the
gap by the choice of $\eta$, and $\|\chi_{\mathrm{tf}}v\|_{(1-s),(-\mathsf r-\alpha_+-1,-\alpha-2,-\eta),\varsigma} =
\varsigma^\alpha\|w^*\|_{H^{1-s,(-\mathsf r-\alpha_+-1,-q^*_\eta+2)}_{\mathrm{sc},b}}$ with $w^* :=
S_\varsigma(\chi_{\mathrm {tf}}v)$, the order at ztf being $-\eta+\alpha+2$. (5.2) at $q = q^*_\eta$ bounds the stronger
norm $\|w^*\|_{H^{-s+2, (-\mathsf r-\alpha_+-1,-q^*_\eta+2)}_{\mathrm{sc},b}}$ by
$C_T\|N_{\mathrm{tf}}(\hat\sigma)^{*h}w^*\|_{H^{-s,(-\mathsf r- \alpha_+,-q^*_\eta)}_{\mathrm{sc},b}}$, whose order at
ztf, $\alpha-\eta$, is that of $\dot{\mathcal H}^{-s,(-\mathsf r- \alpha_+,-\alpha,-\eta)}_\varsigma$, and where
$\varsigma^2N_{\mathrm{tf}}(\hat\sigma)^{*h}w^* = S_\varsigma(\chi_{\mathrm{tf}}g+[\hat
P(\sigma)^{*h},\chi_{\mathrm{tf}}]v -E^*_\sigma\chi_{\mathrm{tf}}v)$ (section 6.2; $\chi_{\mathrm{tf}}\phi_j = 0$). The
term with $E^*_\sigma$ is absorbed at the regularity $2-s$, by the adjoint form of Lemma 6.3, before passing to $1-s$.
This gives (6.7).

*(3).* $\mathcal P(\sigma)$ is $\hat P(\sigma)\oplus0$ plus an operator of finite rank, so it is Fredholm by I.A Theorem
7.2 (3), and by (6.6) at $k = 0$ it is injective. Let $(v,d)\in\mathcal Y^*_\sigma\oplus\mathbb C^{m_2}$ annihilate its
range. Taking $c = 0$ and $u\in C_c^\infty(\mathbb R^4)|_X$ (which lies in $\mathcal X_\sigma$), $\langle u,\hat
P(\sigma)^{*h} v+\sum_jd_j\phi_j\rangle_h = 0$ by I.A Lemma 6.1 (d), so $\hat P(\sigma)^{*h}v = -\sum_jd_j\phi_j$ as a
supported distribution; this lies in $\dot H^{-s,-\mathsf r_\varsigma-\alpha_+}$, so $v\in\mathcal X^*_\sigma$ (with
$\mathcal Y^*_\sigma = \dot{\mathcal H}^{1-s,(-\mathsf r-\alpha_+-1,-\alpha-2,0)}_\varsigma$ at fixed $\varsigma$, by
Lemma 6.2
(c) and I.A Lemma 6.1 (b)). Taking $u = 0$ gives $\langle v,\psi_i\rangle_h = 0$. So $\mathcal P(\sigma)^*(v,d) = 0$,
and $(v,d) = 0$ by (6.7). The range is closed and has trivial annihilator, so $\mathcal P(\sigma)$ is onto. $\square$

The source derives the invertibility in Theorem 9.41 from the injectivity given by (9.119) and the index 0 of (9.18).
That route is not available for an augmented operator, whose index is $m_1-m_2$ plus that of $\hat P(\sigma)$, which is
what Corollary 9.43 is about; (2) is the uniform estimate it needs (section 8, (F6)).

### 6.6 Proof of (4) and (5)

**Lemma 6.5 ([Hin26c] proof of (9.120)).** For $i\ge1$, $A_i := (\sigma\partial_\sigma)^i\hat P(\sigma) = \sigma T+2^i
\sigma^2P_2$. For $s',l,q\in\mathbb R$ and $k'\in\mathbb N_0$ there is $C$ with

$$\|A_iu\|_{(s';k'),(\mathsf r+1,l+2,q),\varsigma}\le C\|u\|_{(s';k'+1),(\mathsf r,l,q),\varsigma},\qquad\varsigma\in(0,
\varsigma_1].$$

*Proof.* $(1-\chi_\partial)A_iu = A_i(1-\chi_\partial)u+[A_i,\chi_\partial]u$. $A_i$ is $\sigma$ times a first-order
operator on $\mathrm{supp}(1-\chi_\partial)$, and $[A_i,\chi_\partial] = \sigma[T,\chi_\partial]$ is of order 0 with
coefficients supported in $\{R_1\le r\le2R_1\}$; with Lemma 6.2 (a) for the latter, the first term of the left side is at
most $C\varsigma$ times the right side. For the second, $\chi_\partial A_iu = A_i(\chi_\partial u)-[A_i,\chi_\partial]u$,
the commutator again handled by Lemma 6.2 (a). By (1.1), with $Q = \rho^3\tilde Q$ and $g_{00} = \rho^2\tilde g$,

$$\varsigma^{-2}S_\varsigma A_iS_\varsigma^{-1} = 2i\hat\sigma\hat\rho\big(\hat\rho\partial_{\hat\rho}-\tfrac32-S\big)-i
\hat\sigma\varsigma^2\hat\rho^3\tilde Q+2^i\varsigma^2\hat\sigma^2\hat\rho^2\tilde g,$$

coefficients smooth in $(\varsigma\hat\rho,\omega)$ as in Lemma 6.3. Near sctf, $\hat\rho\partial_{\hat\rho}$ uses one
b-derivative and each factor $\hat\rho$ raises the decay order by one, so the operator maps $H^{(s';k'+1),\mathsf r}_{
\mathrm{sc}}$ to $H^{(s';k'),\mathsf r+1}_{\mathrm{sc}}$. Near ztf, $\hat\rho = \hat r^{-1}$ lowers the b-weight by one,
and $H^{s'+k'}_{b,c-1}\subset H^{s'+k'}_{b,c-2}$ there ($\hat r\le2$); and $\varsigma^2\hat\rho^3 =
\hat\rho^2\cdot\varsigma \rho$ with $\rho\le\rho_1$. So it maps the ztf order $q-l$ to $q-l-2$, and
$\varsigma^{-(l+4)}\|S_\varsigma A_i\chi _\partial u\|\le C\varsigma^{-(l+2)}\|S_\varsigma\chi_\partial u\|$ in the norms
of (6.1). $\square$

*Proof of (4).* Let $R(\sigma) := \hat P(\sigma)^{-1}$, $0<|\sigma|\le c_0$, and fix $\sigma_*$ there. By I.A Theorem 7.2
(6), for $f$ in $D := \bar H^{(s+\epsilon-1;j),\mathsf r_{\varsigma_*}+\epsilon+\alpha_++1}$, $\sigma\mapsto R(\sigma)f$
is $j$ times differentiable near $\sigma_*$ in $Z := \bar H^{(s-\epsilon;0),\mathsf r_{\varsigma_*}-\epsilon+\alpha_+}$,
on which $\hat P(\sigma)$ is injective (its kernel does not depend on the admissible orders, I.A Theorem 7.2 (3), for
$\epsilon$ below the margins). Applying $(\sigma\partial_\sigma)^i$ to $\hat P(\sigma)R(\sigma)f = f$,
$\sigma\partial_\sigma$ being a derivation,

$$(\sigma\partial_\sigma)^iR(\sigma)f = -R(\sigma)\sum_{i'<i}\binom i{i'}A_{i-i'}(\sigma\partial_\sigma)^{i'}R(\sigma)f,
\qquad1\le i\le j,\tag{6.11}$$

at $\sigma = \sigma_*$, as soon as the sum lies in $\mathcal Y_{\sigma_*}$ (then both sides are elements of $Z$ with the
same image under the injective $\hat P(\sigma_*)$). We show by induction on $i$ that, for $|\sigma_*|\le c_{j,k} :=
\min_{i\le j}c_{k+j-i}(s+i)$, with $c_{k'}(s')$ the constant of (1) at the regularity $s'$ (all hypotheses hold at
every $s'\ge s$, (Z$_{\mathcal P}$) by Theorem 3.1 (4)),

$$\|(\sigma\partial_\sigma)^iR(\sigma_*)f\|_{(s+i;k+j-i),(\mathsf r+\alpha_+,\alpha,0),\varsigma_*}\le C\|f\|_{(s-1;k+j),
(\mathsf r+\alpha_++1,\alpha+2,0),\varsigma_*}.$$

$i = 0$ is (1) at the regularity $s$ and b-order $k+j$. For $i\ge1$, by the induction hypothesis and Lemma 6.5 the term
$i'$ of the sum lies in $\mathcal H^{(s+i';k+j-i'-1),(\mathsf r+\alpha_++1,\alpha+2,0)}_{\varsigma_*}$, which by Lemma
6.2
(e) lies in $\mathcal H^{(s+i-1;k+j-i),(\mathsf r+\alpha_++1,\alpha+2,0)}_{\varsigma_*}$, as $i'\le i-1$; (1) at the
regularity $s+i$ and b-order $k+j-i$ then gives the bound. At $i = j$ this is (6.8) for $f\in D$. $D$ contains
$C_c^\infty(\mathbb R^4)|_X$, which is dense in $\bar H^{(s-1;k+j),\mathsf r_{\varsigma_*}+\alpha_++1}$, and by (6.11)
and the bounds the derivatives extend continuously; this is the extension in (4), and it agrees with that of I.A
(7.6). $\square$

*Proof of (5).* For $\alpha'$ with $\alpha'+2\in(\beta_-,\beta_+)$, (Z) at $\alpha'$ holds by Theorem 3.1 (4) and (TF) at
$\alpha'+2$ by Corollary 5.2 (c). For an augmented operator, (Z$_{\mathcal P}$) at $\alpha'$: the kernel of $\mathcal
P(0)$ and the annihilator of its range, which is the kernel of $\mathcal P(0)^*$ on $\mathcal X^*_0\oplus\mathbb C^{m_2}$
(as in the proof of (3)), consist of $(u,c)$ with $\hat P(0)u = -\sum c_i\psi_i$, resp. $(v,d)$ with $\hat P(0)^{*h}v =
-\sum d_j\phi_j$, which vanish near $\partial X$; so the proof of Theorem 3.1 (2)-(3) shows that they do not depend on
$\alpha'$, and $\mathcal P(0)$ stays invertible. The proof of (1)-(4) used no other property of $\alpha$. $\square$

### 6.7 Corollary 9.43

**Corollary 6.6 ([Hin26c] Corollary 9.43 at $n = 4$, on $E$).** Assume (H1)-(H4), (G) and (TF), with $s>\frac12+
\vartheta_{\mathcal H}$, and that the index of $\hat P(\sigma):\mathcal X_\sigma\to\mathcal Y_\sigma$ at $\sigma\ne0$,
$\mathrm{Im}\,\sigma\ge0$, which does not depend on $\sigma$ (I.A Theorem 7.2 (3)), is 0; under the hypotheses of I.B
this is I.B Theorem 1.3 (3). Then $\hat P(0):\mathcal X_0\to\mathcal Y_0$ has index 0.

*Proof.* Let $d_0$ and $d_1$ be the dimensions of the kernel $K$ of $\hat P(0)$ on $\mathcal X_0$ and of $W :=
\ker_{\mathcal X^*_0}\hat P(0)^{*h}$, the annihilator of its range (Theorem 3.1 (1)). An element of $K$ that vanishes on
$X^\circ$ is 0, as extendible distributions are restrictions to $X^\circ$. An element $w$ of $W$ that vanishes on
$X^\circ$ is supported on $\partial_\sharp X$, and then I.A Corollary 6.5, (6.2), at $\sigma = 0$ gives $w = 0$ on a
slab $\Omega_{r_0,b''}$, so $w = 0$. So the pairings with $C_c^\infty(X^\circ;E)$ separate the points of $K$ and of $W$,
and there are $\phi_1,\dots,\phi_{d_0}$ and $\psi_1,\dots,\psi_{d_1}$ in $C_c^\infty(X^\circ;E)$ with $(\langle
k_a,\phi_j \rangle_h)$ and $(\langle\psi_i,w_b\rangle_h)$ invertible, for bases $(k_a)$ of $K$ and $(w_b)$ of $W$. With
these, $m_1 := d_1$ and $m_2 := d_0$, $\mathcal P(0)$ of (6.5) is invertible: if $\hat P(0)u+\sum c_i\psi_i = 0$ and
$\langle u, \phi_j\rangle_h = 0$ for all $j$, pairing with $w_b$ gives $c = 0$, then $u\in K$ and $u = 0$; and given
$(f,e)$, choose $c$ with $f-\sum c_i\psi_i$ annihilated by $W$, hence $= \hat P(0)u_0$ (the range is closed), and then
$k\in K$ with $\langle u_0+k,\phi_j\rangle_h = e_j$. So (Z$_{\mathcal P}$) holds, and Theorem 6.4 (3) gives that
$\mathcal P(\sigma)$ is invertible for $0<|\sigma|\le c_0$. Its index is that of $\hat P(\sigma)$ plus $m_1-m_2$, that
is $d_1-d_0$, and it is 0. So $d_0 = d_1$. $\square$

The proof is the source's, with Theorem 6.4 (2)-(3) supplying the invertibility of the augmented operator (section 8,
(F6)), and with the choice of $\psi_i$, $\phi_j$ in $C_c^\infty(X^\circ;E)$ justified.

**Remark 6.7 (what differs from [Hin26c]).** (a) The smallness $c_k$ in (1) may depend on $k$. The source removes the
dependence by applying Theorem 9.5 (4) for $|\sigma|\in[\delta_k,\delta_0]$. Here that would need I.A Theorem 7.2 (4)
with constants uniform for $\sigma$ in a compact set and the orders $\mathsf r_\varsigma$, which depend on $|\sigma|$;
I.A states uniformity only for orders that depend on $\mathrm{Re}\,\sigma$ (Theorem 7.2 (1)). So Theorem 6.4 is stated
with $c_k$, and $c_{j,k}$ in (4). (b) The source asserts the conclusions uniformly for $\alpha$ in compact subintervals
of the gap; (5) is stated for each $\alpha$, and the uniformity is not proved here. (c) (4) is stated for $\hat
P(\sigma)$: for an augmented operator it would need the analogue of I.A Theorem 7.2 (6), which I.A does not state. (d)
The regularity order is constant (I.A Remark 1.1).

## 7. Uniformity in the operator

**Theorem 7.1.** Assume (H1)-(H5), and let $b_*\in\mathcal B$ be such that (G), (Z$_{\mathcal P}$) and (TF) hold for
$\hat P^{b_*}$ with the weight $\alpha$ and fixed $\psi_i$, $\phi_j$. Then:

(1) (G), (Z$_{\mathcal P}$) and (TF) hold for $\hat P^b$, with the same $\alpha$, for $b$ near $b_*$;

(2) the constants in Theorem 3.1 (1), (4), Theorem 4.3 (1), (2), (4), Corollary 5.2 (b) and Theorem 6.4 (1), (2), (4),
and $c_k$, $c_{j,k}$, can be chosen uniform for $b$ near $b_*$;

(3) the index of $\hat P^b(0):\mathcal X_0\to\mathcal Y_0$ is locally constant in $b$.

*Proof.* (G): let $[\alpha+2-\epsilon,\alpha+2+\epsilon]$ contain no real part of a root at $b_*$. By Lemma 2.4 (c),
$I^{b_*}(\lambda)^{-1}$ is bounded from $H^{m-2}_\mu$ to $H^m_\mu$, $\mu = \mathrm{Im}\,\lambda$, uniformly on the strip
$|\mathrm{Re}\,\lambda-\alpha-2|\le\epsilon$. $I^b(\lambda)-I^{b_*}(\lambda) = (a^b-a^{b_*})\lambda+(V^b-V^{b_*})+(b^b-
b^{b_*})$ has coefficients that tend to 0 in $C^\infty$ as $b\to b_*$, by (H5), and maps $H^m_\mu$ to $H^{m-2}_\mu$ with
norm at most $\epsilon_b(1+|\mathrm{Re}\,\lambda|)\to0$ uniformly on the strip, as
$\langle\mu\rangle\|v\|_{H^{m-2}_\mu}\le \|v\|_{H^{m-1}_\mu}$ and as in the proof of Lemma 2.4 (a) for the first-order
part. A Neumann series gives that $I^b(\lambda)$ is invertible on the strip, so $\alpha+2$ lies in a gap at $b$.

(2) for the estimates with error terms ((3.2)-(3.3), (4.3)-(4.5)): their constants are produced by finitely many
seminorms of the coefficients and by positivity margins, as in I.A Theorem 8.1, and by the bounds of $J(\lambda)^{-1}$ on
the lines used in Lemmas 2.6-2.7, which are uniform near $b_*$ by the Neumann series above; the coefficients depend
continuously on $b$ by (H5).

(Z$_{\mathcal P}$) and the estimates without error terms: suppose $b_j\to b_*$ and $(u_j,c_j)$ have $\|u_j\|_{\bar H^{s,
\alpha}_b}+|c_j| = 1$ and $\mathcal P^{b_j}(0)(u_j,c_j)\to0$. By (3.2), uniformly in $j$, $\|u_j\|_{\bar H^{s,\alpha}_b}
\le C(\|\mathcal P^{b_j}(0)(u_j,c_j)\|+|c_j|+\|u_j\|_{\bar H^{-N,-N}_b})$, so a subsequence converges weakly in $\bar
H^{s,\alpha}_b$ and strongly in $\bar H^{-N,-N}_b$ (Lemma 2.9 (b)) to $u$, with $c_j\to c$ and $(u,c)\ne0$. Since $\hat
P^{b_j}(0)u_j\to\hat P^{b_*}(0)u$ in distributions, $\hat P^{b_*}(0)u = -\sum c_i\psi_i$, so $u\in\mathcal X_0$ and
$\mathcal P^{b_*}(0)(u,c) = 0$, contradicting (Z$_{\mathcal P}$) at $b_*$. So the estimate $\|u\|+|c|\le C\|\mathcal
P^b(0)(u,c)\|$ holds uniformly near $b_*$. The same argument with (3.3) for $\mathcal P^{b}(0)^*$ shows that its kernel,
the annihilator of the range, is trivial near $b_*$, so $\mathcal P^b(0)$ is onto.

(TF) and Corollary 5.2 (b): the proof of Corollary 5.2 (b) by contradiction runs with sequences $(\theta_j,b_j)\to
(\theta_*,b_*)$, using (4.3) uniformly and $N^{b_j}_{\mathrm{tf}}(e^{i\theta_j})w_j\to N^{b_*}_{\mathrm{tf}}(e^{i
\theta_*})w$ in distributions; at $b_*$, Corollary 5.2 (a) gives injectivity for every $\theta$. The same argument with a
sequence of kernel elements shows that Definition 5.1 (ii) and (iii) hold near $b_*$ (for (iii), with (4.4) and the
adjoint for $H^b_0$).

Theorem 6.4: its constants are those of Theorem 3.1 (4) (for $\mathcal P$), of (5.1)-(5.2), and of Lemmas 6.2, 6.3 and
6.5, which are uniform by the above and by (H5); $c_k$ and $c_{j,k}$ are chosen from them. (3): augment $\hat P^{b_*}(0)$
as in the proof of Corollary 6.6; by (1), $\mathcal P^b(0)$ is invertible near $b_*$, so the index of $\hat P^b(0)$ is
$m_2-m_1$ there. $\square$

(Z) and (TF) are therefore open conditions in the operator, which is how Part VI uses them: it checks them for the
record's operator at one point of the family and propagates them to nearby ones.

## 8. What this part found against the source

Seven findings. None changes a statement of [Hin26c]; (F6) is a gap in a proof, closed here. Pages are printed pages.

(F1) *Two signs in [Hin26c] section 3.2.3 (p. 61), which cancel.* The Mellin transform there is $(\mathcal Mu)(\sigma) =
\int_0^\infty\rho^{i\sigma}u\,\frac{d\rho}\rho$, so $\rho\partial_\rho$ becomes $-i\sigma$, and the indicial roots are
$\lambda = -i\sigma$ at the poles of $N(A,\sigma)^{-1}$ (Definition 3.12). For $u\in\rho^\beta L^2(\frac{d\rho}\rho)$ the
Plancherel line is then $\mathrm{Im}\,\sigma = \beta$, while Lemma 3.11 integrates over $\sigma-i(\alpha+\frac32)$, that
is $\mathrm{Im}\,\sigma = -(\alpha+\frac32)$; and the proof of (3.47) uses that $N(A,-i\nu+\lambda)$, $\lambda\in\mathbb
R$, is invertible when $\nu$ lies in an indicial gap, whereas the poles on that line are the roots with real part $-\nu$.
With both signs reversed the argument is unchanged, and (3.47) holds as stated. Lemmas 2.3 and 2.6 use $\mathcal
Mv(\lambda) = \int e^{\lambda t}v\,dt$, $t = -\log\varrho$, for which the line of the b-weight $c$ is
$\mathrm{Re}\,\lambda = c$.

(F2) *A power in [Hin26c] (3.46) (p. 60), which cancels.* The second equivalence is printed with the factor
$|\sigma|^{\frac32-l}$, justified by $r^2|dr\,d\slashed g| = (|\sigma|^{\frac32})^2\hat r^2|d\hat r\,d\slashed g|$. With
$\hat r = r|\sigma|$, $r^2dr = |\sigma|^{-3}\hat r^2d\hat r$, so the factor is $|\sigma|^{-\frac32}$ and the power
$|\sigma|^{-\frac32-l}$; at $n = 4$ it is $\varsigma^{-2-l}$, as in (6.1). The power enters both sides of the tf step of
the proof of Theorem 9.41 and cancels there.

(F3) *The adjoint weight in [Hin26c] (9.107) (p. 194).* The adjoint estimate bounds $\|u^*\|_{\dot
H^{-s_0+1,-\alpha-2}_b}$ by $\|\hat P_0(0)^*u^*\|_{\dot H^{-s_0,-\alpha-2}_b}$. $\hat P_0(0)^*\in\rho^2\mathrm{Diff}^2_b$
raises the weight by 2, and the space of $\hat P_0(0)^*u^*$ is dual to that of the domain, $\bar H^{s_0,\alpha}_b$; the
weight there is $-\alpha$, as in (3.3).

(F4) *A dropped term in the proof of [Hin26c] (9.117) (p. 196).* The proof expands
$-\hat\rho^2(\hat\rho\partial_{\hat\rho} -n+2+2i\hat\rho^{-1})^2$ as
$-\hat\rho^2(\hat\rho\partial_{\hat\rho}-n+2)^2-2i\hat\rho(\hat\rho\partial_{\hat\rho}-n+1) +4$. Of the two cross
products, $(\hat\rho\partial_{\hat\rho}-n+2)\,2i\hat\rho^{-1} = 2i\hat\rho^{-1}(\hat\rho\partial_{\hat \rho}-n+1)$ and
$2i\hat\rho^{-1}(\hat\rho\partial_{\hat\rho}-n+2)$, the second is missing: the middle term is $-2i\hat\rho
(2\hat\rho\partial_{\hat\rho}-2n+3)$. With it, the coefficient of $\hat\rho\cdot\hat\rho\partial_{\hat\rho}$ in the sum
is $-2i$, as (9.117) states (without it, 0), and $\tilde S = S^*+n-2-a^*$ in the scalar model $P^{(0)} = -(\rho\partial_
\rho)^2+a\rho\partial_\rho+b$, checked symbolically. (9.117) holds. It serves only (9.115), which is not used here
(section 4.3).

(F5) *A sign in [Hin26c] Theorem 9.38 (1) (p. 195).* It takes $\theta$ with $|e^{i\theta}\pm1|\le\frac12$ and $\mathsf r
= \mathsf r_\pm$. The orders $\mathsf r_\pm$ are those for frequencies near $\pm1$ (Theorem 9.41 uses $\mathsf r_+$ for
$\arg\sigma\in[0,\frac\pi4]$), so the condition is $|e^{i\theta}\mp1|\le\frac12$, as in $\Theta_\pm$ of section 4.3.

(F6) *A gap in the proof of [Hin26c] Corollary 9.43 (p. 200).* The proof augments $\hat P_0(0)$ by $E_{01}:\mathbb
C^{d_1}\to C_c^\infty(X^\circ)$ and $E_{10}:\mathcal X_0\to\mathbb C^{d_0}$, says that Theorem 9.41 applies to the
augmented operator and gives its invertibility at $\sigma = i\epsilon$, and concludes $d_0 = d_1$ from the index 0 of
(9.18). The proof of Theorem 9.41 gives the direct estimate (9.119), hence injectivity, and for $\hat P_0(\sigma)$ itself
invertibility then follows from the index 0 of (9.18). For the augmented operator the index is $d_1-d_0$, which is what
the corollary asserts to vanish; injectivity gives only $d_1\le d_0$. Surjectivity needs an estimate for the adjoint of
the augmented operator, uniform as $\sigma\to0$, which the source does not state. Theorem 6.4 (2) is that estimate and
(3) the invertibility, proved for augmented operators; with them Corollary 6.6 is the source's proof. The statement
stands.

(F7) *Slips of the pen.* In the proof of Theorem 9.41 (p. 198), the zero energy step writes the error and target norms
with tf orders $\alpha_+$ and $\alpha_++2$, as $H^{s,(-N,\alpha_+,-\eta)}$ and $H^{s-1,(-N,\alpha_++2,0)}$, where the
orders are $\alpha$ and $\alpha+2$, as in (9.121) a few lines later; and a parenthesis is missing in
$H^{s-2,(\mathsf r+\alpha_++1,\alpha+2,-\eta}$. In Theorem 9.38 (3) (p. 195), $N_{\mathrm{tf}}(P_0,e^{i\theta}u)$ stands
for $N_{\mathrm{tf}}(P_0,e^{i\theta})u$.

*Not proved here, and not used here.* (9.115) and the conjugation behind it (section 4.3); the improvements of Remark
9.37 (Remark 3.2); in Theorem 9.41, a smallness independent of $k$, uniformity in $\alpha$, and (9.120) for augmented
operators (Remark 6.7). Part I.C states tf-admissibility on the Fredholm spaces (Definition 5.1), which the source's
Definition 5.10 implies given (9.115) (section 5.1); Proposition 5.3 verifies Definition 5.1 directly. Where a later part
uses one of the items above, it says so there.

## Sources

[Hin26c] P. Hintz, *(Non-)linear waves on asymptotically flat spacetimes. II*, arXiv:2606.28008v1. READ: pp. 55-62
(sections 3.2.2-3.2.3: (3.29)-(3.47), Lemma 3.11, Definition 3.12, Remark 3.13), p. 69 ((3.72)), p. 104 (Definition
5.10), pp. 193-200 (sections 9.4-9.6: Theorem 9.36, Remark 9.37, Theorem 9.38, Corollary 9.39, Proposition 9.40, Theorem
9.41, Remark 9.42, Corollary 9.43). Printed page numbers; PDF page = printed page + 4.

[HJS] The scattering calculus READ in I.A (Hassell-Jia-Sussman, arXiv:2604.18956), as cited there.

[DLMF] NIST Digital Library of Mathematical Functions, release 1.2.8: section 10.2, 10.7.7, 10.17.2, 10.17.5 and 10.17.6
(READ in section 5.2).

[RS1] M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Theorem VI.14 (the
analytic Fredholm theorem), used in Lemma 2.4.

I.A = `PART-I-SPECTRAL.md` (proved, D189); I.B = `PART-I-B-HIGHENERGY.md` (seated, D189).
