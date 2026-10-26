# Part III.G$''$. Formal solutions at $K^+$ and grafting at n = 4 ([Hin26] sections 9.1.1-9.1.2)

*Status.* Written (D239). This part proves, at spatial dimension $n = 4$, [Hin26] Definitions 9.8 and 9.10, Proposition
9.9, Proposition 9.11 and Corollary 9.12 (pp. 172-179). Proposition 9.9 describes the solutions of III.G$'$ at
$\iota^+\cap K^+$, term by term, as formal solutions built from zero energy states. Proposition 9.11 grafts such a
solution into spacetime as an approximate solution on the Myers-Perry family, accurate at $\iota^+$ and at $K^+$.
Corollary 9.12 does the same for sources with logarithms in $t_*$ and at $\iota^+$-resonances. Parts are cited as
before; the source is [Hin26] = P. Hintz, arXiv:2606.28253v2 (printed page numbers).

*What n = 4 changes: the window.* The source expands at $R = 0$ up to $R^{\ell_K}$ with
$\ell_K<3+\epsilon_{\mathrm{ind}}$. That keeps the indicial roots in $[-3,0]$, each with generalised companions to the
orders of his (9.32), because the smallest $\iota^+$-order he grafts is $\lambda = 1$ and the remainder must have
$K^+$-order $\lambda+\ell_K>4$. At $n = 4$ every $\iota^+$-order to be grafted exceeds 1. The pure $\iota^+$ resonances
have real part at least 2 (III.G Theorem 5.1 (2)), and the source's Corollary 9.12 asks $\mathrm{Re}\,\lambda_0>1$ in
any case. So $\ell_K<3$ suffices: for every $\lambda>1$ some $\ell_K\in(4-\lambda,3)$ is admissible. This window
$(-3,0]$ needs no state at $-3$, and every state it needs has been constructed: in III.D$''$, III.D$'''$ and
III.F$''''$, with at least the companions required (Table 1.1). The record's own estimate of the window (N1STAR-PROOF.md
10.35 (c), $[\alpha_5-4,0]$ with $\alpha_5\in(1,2]$) lies inside it, and its value of $\alpha_5$ is not needed here.

## 1. Hypotheses, the roots in the window, and their states

Throughout we assume (Dyn) (III.D), the parameters of III.F$'$ Proposition 3.3 with
$\gamma_\Upsilon<\min(\frac12s_C,\frac38)$ (III.G$'$ Lemma 1.1), (C1) (III.F$'$), and (C2)-(C3) with
$z_\Upsilon := 4e_\Upsilon\gamma_\Upsilon^2$ (III.D's $z$) not in $Z_{\mathrm{exc}}$, so that every indicial root of
$\widehat{L_b}(0)$ is simple (III.F$'$ Proposition 2.3 (e)). We fix
$$\ell_K^{\max} := \min(3,\ 2+2\gamma_Cv_C),\tag{1.1}$$
so that the vector type 1 root $-2-2\gamma_Cv_C$ of III.F$'$ Proposition 2.3 lies below the window. The other roots from
$\Box^C$ with real part $\le0$ lie below $-101$ (there, (d)). Under (C5) below, $\ell_K^{\max} = 3$:

(C5) $\gamma_Cv_C\ge\frac12$, an obligation for Part VI at the record's parameters.

For $\ell_K<\ell_K^{\max}$ let $\mathcal W(\ell_K)$ be the set of indicial roots $\mu$ of $\widehat{L_b}(0)$ (III.F$'$
Proposition 2.3) with $-\ell_K<\mathrm{Re}\,\mu\le0$. All are real (III.G$'$ Lemma 1.3 (c)). For a root $\mu$ of type
$\tau$ and degree $l$, let $\mathcal Y_\tau$ be the space of harmonics of III.A$'$ section 2 parametrising that type:
$\mathcal S_l$ for scalar, $\mathcal V_l$ for vector and $\mathcal T_l$ for tensor types.

**Table 1.1 (the roots of $\mathcal W(\ell_K)$, $\ell_K<3$, and their states).** For each root: its type, its origin in
the factorisation III.F$'$ (2.1), the state whose leading term spans its indicial solutions (Lemma 1.2), the number $K$
of generalised companions constructed, and the number $k_\mu$ used below.

| root $\mu$ | types | origin | state | $K$ | $k_\mu$ |
|---|---|---|---|---|---|
| $0$ | s0 | $\Box^\Upsilon$'s s0 root | time translation $h^{(0)}_{b,\mathrm s0}$, III.D$'''$ Proposition 3.1 (1) | 3 | 2 |
| $0$ | s2 | $\Box^\Upsilon$'s sl root $-l+1$, $l = 2$ | III.D$'''$ (4)-(7) | 3 | 2 |
| $-1$ | s1 | the boosts | $h^{\le k}_{b,\mathrm s1}$, III.D$''$ Proposition 3.1, III.D$'''$ (2) | 4 | 3 (special) |
| $-1$ | v1 | the rotations | $h^{\le k}_{b,\mathrm v1}$, III.D$''$ Proposition 3.1, III.D$'''$ (3) | 3 | 2 (special) |
| $-1$ | s3, v2 | $\Box^\Upsilon$'s $-l+1$ ($l = 3$), $-l$ ($l = 2$) | III.D$'''$ (4)-(7) | 2, 2 | 1 |
| $-2$ | s4, v3 | $\Box^\Upsilon$'s $-l+1$ ($l = 4$), $-l$ ($l = 3$) | III.D$'''$ (4)-(7) | 1, 1 | 0 |
| $-2$ | s2, v2, t2 | the physical factor $\lambda+l$ | $h^{(-2)}_{b,\tau}$, III.F$''''$ Proposition 5.1 | 0 | 0 |
| $2-\lambda^\Upsilon_{\mathrm s0,2}\in[-\frac{z_\Upsilon}3,0)$ | s0 | class root | III.D$'''$ (4)-(7) | 2 | 2 |
| $2-\lambda^\Upsilon_{\mathrm s1,2}\in(-\frac14,0)$ | s1 | class root | III.D$'''$ (4)-(7) | 2 | 2 |
| $2-\lambda^\Upsilon_{\mathrm sl,l+1}\in(-\frac54,-1)$, $l = 2$; $2-\lambda^\Upsilon_{\mathrm s1,3}\in(-\frac54,-1)$ | s2; s1 | class roots | III.D$'''$ (4)-(7) | 2 | 1 |
| $2-\lambda^\Upsilon_{\mathrm s2,4}$, $2-\lambda^\Upsilon_{\mathrm s3,4}\in(-\frac94,-2)$ | s2, s3 | class roots | III.D$'''$ (4)-(7) | 2 | 0 |

A root $\mu$ of III.D$'''$'s $\Box^\Upsilon$-list is a root of $\widehat{L_b}(0)$ shifted by one: the state is
$h^{(\mu)}_b := \delta^*_{g_b}\omega^{(\mu-1)}_b$, whose leading term $\widehat{\bar\delta^*}(0)\bar\omega$ is of degree
$\mu$ (III.D$'''$ (4)-(7)). Roots $\mu\in\mathcal W(\ell_K)$ with $-\mathrm{Re}\,\mu\ge\ell_K$ do not occur, and only
rows with $-\mu<\ell_K$ are used.

*Completeness of the table.* The roots of III.F$'$ Proposition 2.3 with real part in $(-3,0]$ are those listed and the
excluded ones. Excluded: the $\lambda^C_{\cdot,\ll,\cdot}-1$ (real part $<-101$); $-2-2\gamma_Cv_C$ (below
$-\ell_K^{\max}$); and $-l$, $2-l$, $1-l$ and $2-\lambda^\Upsilon_{\mathrm sl,l+j}$ with real part $\le-3$. With III.D
Lemma 4.1's ranges, $\lambda^\Upsilon_{\mathrm sl,l+j}-2\in(l+j-2,l+j-\frac74)$ is $<3$ only for $l+j\le4$; and
$\lambda^\Upsilon_{\mathrm s0,2}-2\in(0,\frac{z_\Upsilon}3]$.

**Lemma 1.2 (the indicial solutions are the states' leading terms).** For every $\mu\in\mathcal W(\ell_K)$ and every
type $\tau$ at which $\mu$ is a root, the kernel of the indicial family $N_\tau(\widehat{\bar L}(0),\mu)$ on the
type-$\tau$ sections of degree $l$ is $\{\bar h_\tau(Y):Y\in\mathcal Y_\tau\}$. Here $\bar h_\tau(Y)$ is the
$\rho^\mu$-leading term of the state of Table 1.1 (for s1 and v1 at $-1$, of $\breve h^2_{b,\mathrm s1}(S)$ and
$\breve h^1_{b,\mathrm v1}(V)$), and $Y\mapsto\bar h_\tau(Y)$ is injective.

*Proof.* On the type-$\tau$ sections given by a harmonic $Y$, the indicial family is a matrix polynomial in $\mu$ whose
determinant has $\mu$ as a simple zero (the hypothesis on $z_\Upsilon$). So its kernel is one-dimensional for each $Y$
in a basis of $\mathcal Y_\tau$, and depends linearly on $Y$. The state's leading term $\bar h = \rho^\mu\phi(\omega)$
lies in the kernel. It satisfies $\widehat{\bar L}(0)\bar h = 0$: for the base of a chain this is the leading order of
(2.1) at $m = 0$, since $\widehat{L_b}(0)-\widehat{\bar L}(0)\in\rho^4\mathrm{Diff}^2_{\mathrm b}$ (III.F Lemma 2.1
(3)); for s1 and v1 it is (2.4) of Lemma 2.2 below at the first index of the chain. As
$\widehat{\bar L}(0) = \rho^2\tilde L(0)(\omega,\rho\partial_\rho,\partial_\omega)$ is dilation invariant, this is
$N(\widehat{\bar L}(0),\mu)\phi = 0$. It is non-zero for $Y\ne0$: for the $\Box^\Upsilon$-roots, by (R5) of III.D$'''$,
as $N(\widehat{\bar\delta^*}(0),\mu-1)$ is injective on these types at $\mu-1\notin\{0,-1\}$, or (at s0, s2 with
$\mu = 0$) by III.F$'$ Lemma 2.5; for the boosts and rotations, by III.D$'''$ (2)-(3); and for the physical states, by
III.F$''''$ Proposition 5.1, whose leading terms span the kernel.

$\square$

This closes, for the window, the item III.D$'''$ deferred to section 8: that the leading terms of its states span the
kernels of $\widehat{\bar L}(0)$'s indicial families.

## 2. Formal solutions

### 2.1 Towers

Let $L$ be a stationary operator, of order at most 2 in $\partial_{t_*}$:
$L(a(t_*)h) = a\hat L(0)h+a'[L,t_*]h+\frac12a''[[L,t_*],t_*]h$ for stationary $h$ and functions $a$ of $t_*$.

**Lemma 2.1 (towers).** (a) For stationary $\breve h^0,\dots,\breve h^K$, the following are equivalent:
$L\big(\sum_{i=0}^k\frac{k!}{(k-i)!}t_*^{k-i}\breve h^i\big) = 0$ for $k = 0,\dots,K$; and
$$\hat L(0)\breve h^m+[L,t_*]\breve h^{m-1}+\tfrac12[[L,t_*],t_*]\breve h^{m-2} = 0,\qquad m = 0,\dots,K\tag{2.1}$$
($\breve h^{-1} = \breve h^{-2} = 0$). (b) If (2.1) holds, then for $k\le K$ and every smooth $a$,
$$L\Big(\sum_{j=0}^ka^{(j)}(t_*)\breve h^j\Big) = a^{(k+1)}\big([L,t_*]\breve h^k
+\tfrac12[[L,t_*],t_*]\breve h^{k-1}\big)+\tfrac12a^{(k+2)}[[L,t_*],t_*]\breve h^k.\tag{2.2}$$

*Proof.* (b) Expanding by the rule for $L(a h)$, the coefficient of $a^{(m)}$ is the left side of (2.1) for $m\le k$.
For $m = k+1,k+2$ it is what remains. (a) With $a = t_*^k/k!$, (2.2) shows that (2.1) implies the polynomial identities.
Conversely, by induction on $k$: the identity for $k$ minus $t_*$ times the one for $k-1$ (multiplied by $k$) leaves the
$t_*^0$-coefficient, which is $k!$ times the left side of (2.1) at $m = k$, plus terms vanishing by (2.1) at smaller
$m$. $\square$

For $L = L_b$, III.F Lemma 2.1 (3) gives near infinity
$$[L_b,t_*] = -\rho\big(\rho\partial_\rho-\tfrac32-\bar S\big)-g_b^{00}\partial_{t_*}+\tfrac12Q_b,\qquad[[L_b,t_*],t_*]
 = -g_b^{00}\in\rho^2C^\infty,\tag{2.3}$$
and for $\bar L$ (III.F (2.2), no $\partial_{t_*}^2$ term) $[\bar L,t_*] = -\rho(\rho\partial_\rho-\frac32-\bar S)$ and
$[[\bar L,t_*],t_*] = 0$.

The states of Table 1.1 satisfy (2.1) for $L = L_b$. III.D$'''$ Proposition 3.1 gives
$\omega^{\le k}\in\ker\Box^\Upsilon_b$ as polynomials in $t_*$, so $\delta^*_{g_b}\omega^{\le k}\in\ker
D_{g_b}\mathrm{Ric}\cap\ker\delta_{g_b,E_\Upsilon}G_{g_b}\subset\ker L_b$. Here
$D_{g_b}\mathrm{Ric}(\mathcal L_Xg_b) = \mathcal L_X\mathrm{Ric}(g_b) = 0$ and
$2\delta_{g_b,E_\Upsilon}G_{g_b}\delta^*_{g_b} = \Box^\Upsilon_b$. The physical states lie in $\ker\widehat{L_b}(0)$
($K = 0$).

### 2.2 The Minkowski formal solutions ([Hin26] Definition 9.8 at $n = 4$)

Let $(\breve h^i_b)_{i\le K}$ be a tower of Table 1.1 for $L_b$, with
$\breve h^i_b\in\mathcal A^{(\mu-i,0)\cup(\mu-i+\mathcal E_{\mathrm{ind}})}$ and
$\min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}>0$, and with $\rho^{\mu-i}$-leading terms $\breve{\bar h}^i$, homogeneous of
degree $\mu-i$. For s1 and v1 the source's indexing is used. The s1 tower is
$h_{b,\mathrm s1}\in\mathcal A^{(3,0)\cup\ldots}$, $\breve h^1_{b,\mathrm s1}\in\mathcal A^{(2,0)\cup\ldots}$, then
$\breve h^k_{b,\mathrm s1}\in\mathcal A^{(-k+1,0)\cup\ldots}$ for $k\ge2$, and its homogeneous part starts at
$\breve{\bar h}^2_{\mathrm s1} =: \bar h^2_{\mathrm s1}$, of degree $-1$. The v1 tower is
$h_{b,\mathrm v1}\in\mathcal A^{(3,0)\cup\ldots}$, then $\breve h^k_{b,\mathrm v1}\in\mathcal A^{(-k,0)\cup\ldots}$ for
$k\ge1$, starting at $\bar h^1_{\mathrm v1}$, of degree $-1$ (III.D$''$ (3.4), III.D$'''$ (2)-(3)).

**Lemma 2.2 (the Minkowski towers).** The leading terms satisfy (2.1) for $\bar L$:
$$\widehat{\bar L}(0)\breve{\bar h}^m+[\bar L,t_*]\breve{\bar h}^{m-1} = 0,\tag{2.4}$$
for the s1 chain from $m = 2$ and for the v1 chain from $m = 1$ (the earlier terms omitted).

*Proof.* Under the dilations $(t_*,x)\mapsto(st_*,sx)$, $t_*^{k-i}\breve h^i$ has leading degree $k-\mu$ for every $i$
(for s1, $k-1$ for $i\ge2$ and $k-3$ for $i = 0,1$; for v1, $k$ for $i\ge1$ and $k-3$ for $i = 0$). $\bar L$ is
homogeneous of degree $-2$. $L_b-\bar L = -\frac12g_b^{00}\partial_{t_*}^2+\frac12Q_b\partial_{t_*}+\frac12R_b$ (III.F
(2.3)) lowers the degree by at least 2, and the corrections $\breve h^i_b-\chi\breve{\bar h}^i$ by
$\min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}>0$. So the top-degree part of
$L_b(\sum\frac{k!}{(k-i)!}t_*^{k-i}\breve h^i_b) = 0$ is $\bar L(\sum\frac{k!}{(k-i)!}t_*^{k-i}\breve{\bar h}^i) = 0$,
over the indices of top degree. Lemma 2.1 (a) for $\bar L$, with $[[\bar L,t_*],t_*] = 0$, gives (2.4). $\square$

**Definition 2.3 ([Hin26] Definition 9.8 at $n = 4$).** For a function $a = a(t_*)$ (valued in $\mathcal Y_\tau$ where
the state is linear in $Y$) and $k\le K$:
$$\bar h^{(\mu),\le k}(a) := \sum_{j=0}^ka^{(j)}(t_*)\breve{\bar h}^{(\mu),j},\qquad\bar h^{\le k}_{\mathrm s1}(a) :
 = \sum_{j=2}^{k}\breve{\bar h}^j_{\mathrm s1}(a^{(j-2)}),\qquad\bar h^{\le k}_{\mathrm v1}(a) :
 = \sum_{j=1}^k\breve{\bar h}^j_{\mathrm v1}(a^{(j-1)}).\tag{2.5}$$

**Lemma 2.4 ([Hin26] (9.28)-(9.31) at $n = 4$).** (a)
$\bar L\,\bar h^{(\mu),\le k}(a) = a^{(k+1)}[\bar L,t_*]\breve{\bar h}^{(\mu),k}$, and likewise for s1 (with
$a^{(k-1)}$, $\breve{\bar h}^k_{\mathrm s1}$) and v1 (with $a^{(k)}$, $\breve{\bar h}^k_{\mathrm v1}$).

(b) For $a = t_*^{-\lambda+\mu}$ (for s1 $a = t_*^{-\lambda-1}$, for v1 $a = t_*^{-\lambda-1}$), the tensor
$t_*^\lambda\bar h^{(\mu),\le k}(a)$ is independent of $t_*$ in the coordinates $(t_*,R,\omega)$, $R = (\rho t_*)^{-1}$.
It is a finite sum $\sum_jc_jR^{-\mu+j}\phi_j(\omega)$, without logarithms. Moreover
$$t_*^\lambda t_*^2\bar L\big(\bar h^{(\mu),\le k}(t_*^{-\lambda+\mu})\big)\in R^{-\mu+k
-1}C^\infty([0,1)_R\times\mathbb S^3)\tag{2.6}$$
is independent of $t_*$. The same holds for s1 with $R^{k-2}$ and for v1 with $R^{k-1}$ in place of $R^{-\mu+k-1}$.

*Proof.* (a) is (2.2) for $\bar L$ with $[[\bar L,t_*],t_*] = 0$, by Lemma 2.2. (b) $a^{(j)} = c_jt_*^{-\lambda+\mu-j}$
and $\breve{\bar h}^j = \rho^{\mu-j}\phi_j(\omega)$, so
$t_*^\lambda a^{(j)}\breve{\bar h}^j = c_j(\rho t_*)^{\mu-j}\phi_j = c_jR^{-\mu+j}\phi_j$. By (a) and
$[\bar L,t_*] = -\rho(\rho\partial_\rho-\frac32-\bar S)$, the left side of (2.6) is
$t_*^{\lambda+2}c_{k+1}t_*^{-\lambda+\mu-k-1}\rho^{1+\mu-k}\psi(\omega) = c_{k+1}(\rho t_*)^{1+\mu-k}\psi =
c_{k+1}R^{k-1-\mu}\psi$. For s1, $a^{(k-1)} = ct_*^{-\lambda-k}$ and $\breve{\bar h}^k_{\mathrm s1}$ has degree $1-k$,
giving $R^{k-2}$; for v1, $a^{(k)} = ct_*^{-\lambda-1-k}$ and degree $-k$ give $R^{k-1}$. $\square$

### 2.3 The Myers-Perry formal solutions ([Hin26] Definition 9.10 at $n = 4$)

**Definition 2.5.** With the towers of Table 1.1 for $L_b$:
$$h^{(\mu),\le k}_b(a) := \sum_{j=0}^ka^{(j)}(t_*)\breve h^{(\mu),j}_b,\qquad h^{\le k}_{b,\mathrm s1}(a) :
 = h_{b,\mathrm s1}(a)+\sum_{j=1}^k\breve h^j_{b,\mathrm s1}(a^{(j)}),\qquad h^{\le k}_{b,\mathrm v1}(a) :
 = h_{b,\mathrm v1}(a)+\sum_{j=1}^k\breve h^j_{b,\mathrm v1}(a^{(j)}).\tag{2.7}$$

**Lemma 2.6 ([Hin26] (9.37) at $n = 4$).** $L_bh^{(\mu),\le k}_b(a)$ is given by (2.2) with
$\breve h^j = \breve h^{(\mu),j}_b$, and likewise for s1 and v1. For $a = t_*^{-\lambda+\mu}$, near $K^+$ (bounded $r$),
it is $O(t_*^{-\lambda+\mu-k-1})$ with all stationary derivatives: of $K^+$-order $\lambda-\mu+k+1$. For s1 with
$a = a_{\mathrm s1}$ of (4.2) the order is $\lambda+k$, and for v1 with $a = a_{\mathrm v1}$ it is $\lambda+k+1$. With
$k = k_\mu$ of Table 1.1, every one of these orders is $\ge\lambda+3$.

*Proof.* (2.2) and the tower property (section 2.1). The coefficients $[L_b,t_*]\breve h^k_b$ and
$[[L_b,t_*],t_*]\breve h^{k-1}_b$ are stationary and smooth. $a^{(k+1)}\sim t_*^{-\lambda+\mu-k-1}$, and for s1
$a_{\mathrm s1}^{(k+1)}\sim t_*^{-\lambda-k}$, for v1 $a^{(k+1)}_{\mathrm v1}\sim t_*^{-\lambda-k-1}$. The bound
$\lambda-\mu+k_\mu+1\ge\lambda+3$ is $k_\mu\ge2+\mu$, which Table 1.1's $k_\mu$ satisfy: $k_\mu = 2+\mu$ at the integer
roots; at the class roots $\mu\in(-\frac14,0)$, $(-\frac54,-1)$, $(-\frac94,-2)$, $k_\mu = 2,1,0$; and for s1, $k = 3$;
for v1, $k = 2$.

$\square$

## 3. The expansion at $K^+$ ([Hin26] Proposition 9.9 at $n = 4$)

**Theorem 3.1.** Let $\lambda\in\mathbb C$, $k\in\mathbb N_0$, $\ell_K<\ell_K^{\max}$ with $\ell_K\ne-\mathrm{Re}\,\mu$
for every root $\mu$, and $\alpha\in(-1,0)$. Suppose $N_{\iota^+}(\lambda)u = f$ on $[0,1)_R\times\mathbb S^3$, with
$f\in H^{k,\ell_K-2}_{\mathrm b}$ and $u\in H^{k+2,\alpha}_{\mathrm b}$ (the b-density $|\frac{dR}Rd\slashed g|$). Then
$u = u_0+\tilde u$, $\tilde u\in H^{k+2,\ell_K}_{\mathrm b}$, with
$$u_0 = \sum_{\mu\in\mathcal W(\ell_K)}\ \sum_\tau t_*^\lambda\,\bar h^{(\mu),\le k_\mu}_\tau\big(t_*^{-\lambda
+\mu}Y^{(\mu)}_\tau\big),\tag{3.1}$$
for suitable $Y^{(\mu)}_\tau\in\mathcal Y_\tau$. The sum runs over the types of Table 1.1 at which $\mu$ is a root. At
$\mu = -1$ the s1 and v1 terms are $t_*^\lambda\bar h^{\le3}_{\mathrm s1}(t_*^{-\lambda-1}S^{(-1)}_1)$ and
$t_*^\lambda\bar h^{\le2}_{\mathrm v1}(t_*^{-\lambda-1}V^{(-1)}_1)$. Each term is a $t_*$-independent function of
$(R,\omega)$ (Lemma 2.4 (b)) and is free of logarithms. The coefficients $Y^{(\mu)}_\tau$ are continuous linear
functionals of $(u,f)$ in these spaces.

*Proof.* (3.1) is the source's (9.32) at $n = 4$, with the window $\mathcal W(\ell_K)$ and the orders $k_\mu$ of Table
1.1. By (1.3) of III.G$'$, $R^2N_{\iota^+}(\lambda) = A_0+RA_1$ with
$A_0 = \tilde L(0)(\omega,-R\partial_R,\partial_\omega)$ b-elliptic. So
$$A_0u = R^2f-RA_1u.\tag{3.2}$$
By III.A Lemma 1.4 (its proof at finite order, as in III.G$'$ Step 5 (iv)),
$u\in H^{k+2,(\mathcal E,\ell_K)}_{\mathrm b}$ with $\mathcal E$ generated by $\mathrm{Spec}_{\mathrm b}(A_0)$ above
$\alpha$. So $u$ is a finite sum of terms $R^z(\log R)^jc_{z,j}(\omega)$, $\mathrm{Re}\,z<\ell_K$, plus an element of
$H^{k+2,\ell_K}_{\mathrm b}$. We remove the terms in order of increasing real part.

*The lowest term.* Suppose some coefficient is non-zero, and let $z_0$ be the least real part of an exponent present. In
(3.2) the right side has exponents of real part $\ge\min(\ell_K,z_0+1)>z_0$. So the terms of $A_0u$ at real part $z_0$
vanish: for each $z$ with $\mathrm{Re}\,z = z_0$ and $J$ the top power of $\log R$, $N(A_0,z)c_{z,J} = 0$, and
$N(A_0,z)c_{z,J-1}+J\,\partial_zN(A_0,z)c_{z,J} = 0$. Hence $z = -\mu$ for a root $\mu$, which is real, so $z = z_0$. As
$\mu$ is a simple root, $\partial_zN(A_0,z)$ maps $\ker N(A_0,z)$ injectively into a complement of the range of
$N(A_0,z)$. So $Jc_{z,J} = 0$, $J = 0$, and $c := c_{z,0}\in\ker N(A_0,-\mu) = \ker N(\widehat{\bar L}(0),\mu)$. The
kernel is finite dimensional ($A_0$ elliptic on $\mathbb S^3$) and splits by type and harmonic. By Lemma 1.2,
$c = \sum_\tau\bar h_\tau(Y_\tau)$ with unique $Y_\tau\in\mathcal Y_\tau$, and $\mu\in\mathcal W(\ell_K)$ as
$z_0<\ell_K$.

*Subtraction.* Let $w := \sum_\tau t_*^\lambda\bar h^{(\mu),\le k_\mu}_\tau(t_*^{-\lambda+\mu}Y_\tau)$, a function of
$(R,\omega)$ (Lemma 2.4 (b)). Its $R^{-\mu}$-coefficient is $c$, since
$t_*^\lambda a\breve{\bar h}^0 = R^{-\mu}\bar h_\tau(Y)$; for s1 and v1 the lowest terms are
$R^1\bar h^2_{\mathrm s1}(S)$ and $R^1\bar h^1_{\mathrm v1}(V)$. Its other terms have exponents $-\mu+j$, $j\ge1$. By
(2.6) and the definition (III.G$'$ (1.1)) $N_{\iota^+}(\lambda) = t_*^{\lambda+2}\bar Lt_*^{-\lambda}$ on
$t_*$-independent functions,
$$N_{\iota^+}(\lambda)w\in R^{-\mu+k_\mu-1}C^\infty\subset H^{\infty,\ell_K-2}_{\mathrm b}\quad\text{near }R = 0,$$
as $-\mu+k_\mu-1\ge1>\ell_K-2$ (Lemma 2.6). The same holds for s1 and v1, with $R^{1}$. So $u' := u-w$ satisfies the
hypotheses with $f' := f-N_{\iota^+}(\lambda)w$, and has no term $R^{-\mu}$ of the types removed. Doing this for every
type and root at real part $z_0$, the least real part of an exponent of $u'$ exceeds $z_0$. By the first step, every new
least exponent is $-\mu'$ for a root $\mu'$ with $-\mu'\in(z_0,\ell_K)$. There are finitely many such roots, so after
finitely many steps no term remains, and $\tilde u := u-u_0\in H^{k+2,\ell_K}_{\mathrm b}$. Each $Y_\tau$ is read off
from the coefficient $c$, which is a continuous functional of $(u,f)$ (III.A Lemma 1.5's circle integrals), and the
subtractions are continuous. $\square$

**Corollary 3.2 (the index set at $K^+$, precisely).** In III.G$'$ Theorem 3.1, below the order $\ell_K^{\max}$, the
expansion of $h$ at $R = 0$ has no logarithms. Its exponents are $-\mu+j$ ($\mu\in\mathcal W(\ell_K)$,
$0\le j\le k_\mu$, with the s1 and v1 conventions). So $h\in\mathcal A^{(\langle\mathcal E^C_{\iota^+,\mathscr
I}\rangle,\ell_I),(\mathcal E^\flat_K,\ell_K)}$ for every $\ell_K<\ell_K^{\max}$, with
$\mathcal E^\flat_K := \bigcup_{\mu\in\mathcal W(\ell_K^{\max})}\bigcup_{j\le k_\mu}(-\mu+j,0)$. This is the $n = 4$
counterpart of the source's $\mathcal E_K$ ((G$'$2) of III.G$'$).

*Proof.* Theorem 3.1 with $f = R^2\cdot$(rapidly vanishing) and $u = h$ near $R = 0$. $\square$

## 4. Grafting ([Hin26] Proposition 9.11 and Corollary 9.12 at $n = 4$)

Let $\mathcal M$ be the compactified spacetime of III.B (the source's (3.3)) with its faces $\mathscr I^+$, $\iota^+$,
$K^+$. Let $\Omega_* := \mathrm{cl}_{\mathcal M}\{t_*\ge1\}$ (the source's (9.38)), and let the b-spaces on $\Omega_*$
carry three orders, listed for $\mathscr I^+$, $\iota^+$, $K^+$ (III.A Definitions 2.6-2.8). Let
$\chi_K\in C^\infty(\mathcal M)$ equal 1 near $K^+$ and 0 near $t_*^{-1}(1)\cup\mathscr I^+$. Let
$\chi_\iota := \chi(t_*)$, with $\chi\in C^\infty(\mathbb R)$ equal to 0 on $(-\infty,1]$ and 1 on $[2,\infty)$; it
equals 1 near $\iota^+$ and is supported in $\Omega_*$.

**Lemma 4.1 ($\bar L$ is the $\iota^+$-normal operator of $L_b$).** For $w = w(R,\omega)$ conormal on $\iota^+$ near
$\{R>0\}$ (equivalently $w(v,\omega)$, $v = R^{-1}$), on $\{|x|>3R_1\}$:
$$L_b\big(t_*^{-\lambda}w\big) = t_*^{-\lambda-2}N_{\iota^+}(\lambda)w+t_*^{-\lambda-4}v^2Bw,\tag{4.1}$$
with $B$ a second-order b-operator in $(v\partial_v,\partial_\omega)$ whose coefficients are smooth functions of
$(\rho,\omega) = (v/t_*,\omega)$.

*Proof.* $\bar L(t_*^{-\lambda}w) = t_*^{-\lambda-2}N_{\iota^+}(\lambda)w$ is the definition of $N_{\iota^+}$ (III.G$'$
(1.1)). For the rest use III.F (2.3), with
$\partial_{t_*}(t_*^{-\lambda}w(\rho t_*)) = t_*^{-\lambda-1}(v\partial_v-\lambda)w$ and
$\rho\partial_\rho = v\partial_v$ at fixed $t_*$. $g_b^{00}\partial_{t_*}^2$ gives
$\rho^2t_*^{-\lambda-2}(\ldots)w = t_*^{-\lambda-4}v^2(\ldots)w$. $Q_b\partial_{t_*}$ gives
$\rho^3t_*^{-\lambda-1}(\ldots)$, and $R_b$ gives $\rho^4(\ldots)$; both are $t_*^{-\lambda-4}v^2$ times $v$ or $v^2$.
$\square$

**Theorem 4.2 ([Hin26] Proposition 9.11 at $n = 4$).** Let $\lambda\notin\mathrm{spec}_{\iota^+}(\bar L)$ with
$\mathrm{Re}\,\lambda>0$. Let $\ell_K<\ell_K^{\max}$, $\ell_K\ne-\mathrm{Re}\,\mu$ for all roots, and
$\ell_K\notin\mathrm{Re}\,\pi_1\mathcal E_K$. Let $\ell_I<\frac32+s_C$,
$\ell_I\notin\mathrm{Re}\,\pi_1\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}$, and $\mathrm{Re}\,\lambda<\ell_I$. Let
$f_+\in H^{\infty,\ell_I+1,\ell_K-2}_{\mathrm b}(\iota^+;S^2T^*)$ and $u_+ := N_{\iota^+}(\lambda)^{-1}f_+$ (III.G$'$
Theorem 3.1 (2), extended holomorphically to $\lambda\notin\mathrm{spec}_{\iota^+}$). Write
$u_+ = \chi_K|_{\iota^+}u_0+\tilde u$ by Theorem 3.1, with $\tilde u\in H^{\infty,(\langle\mathcal E^C_{\iota^+,\mathscr
I}\rangle,\ell_I),\ell_K}_{\mathrm b}(\iota^+)$. Define
$$a_{\mathrm s1}(t_*) := \begin{cases}\frac1{\lambda(\lambda-1)}t_*^{-\lambda+1},&\lambda\ne1,\\-\log t_*,&\lambda
 = 1,\end{cases}\qquad a_{\mathrm v1}(t_*) := -\frac1\lambda t_*^{-\lambda},\tag{4.2}$$
and let $u_{b,0}$ be (3.1) with every Minkowski formal solution replaced by its Myers-Perry version (Definition 2.5), at
the same orders, and with the s1 and v1 terms $h^{\le3}_{b,\mathrm s1}(a_{\mathrm s1}S^{(-1)}_1)$ and
$h^{\le2}_{b,\mathrm v1}(a_{\mathrm v1}V^{(-1)}_1)$:
$$u_{b,0} := h^{\le3}_{b,\mathrm s1}(a_{\mathrm s1}S^{(-1)}_1)+h^{\le2}_{b,\mathrm v1}(a_{\mathrm v1}V^{(-1)}_1)
+\sum_{\mu,\tau}{}'\,h^{(\mu),\le k_\mu}_{b,\tau}\big(t_*^{-\lambda+\mu}Y^{(\mu)}_\tau\big),\tag{4.3}$$
the primed sum over the other rows. Let $u := \chi_Ku_{b,0}+\chi_\iota t_*^{-\lambda}\tilde u$. Then
$$\chi_\iota t_*^{-\lambda-2}f_+-L_bu\in H^{\infty,(\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}+2,\ \ell_I
+1),\ \lambda+2+\mathcal E_{\mathrm{ind}},\ \lambda+\ell_K}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-}\tag{4.4}$$
for an index set $\mathcal E_{\mathrm{ind}}$ with $\min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}>0$ depending only on
$\bar L$. Moreover $(t_*^\lambda u)|_{\iota^+} = u_+$, and $u\in H^{\infty,(\langle\mathcal E^C_{\iota^+,\mathscr
I}\rangle,\ell_I),(\lambda,0)\cup(\lambda+\mathcal E_{\mathrm{ind}}),(\mathcal
E^{\mathrm{gr}}_K(\lambda),\ell_K)}_{\mathrm b}(\Omega_*)^{\bullet,-}$. Here $\mathcal E^{\mathrm{gr}}_K(\lambda)$
contains the index sets of $a_{\mathrm s1}$, $a_{\mathrm v1}$ and $(\kappa,0)$ for every exponent $\kappa$ of $t_*^{-1}$
in (4.3).

*Proof.* *The restriction.* At $(\iota^+)^\circ$, $\rho\sim t_*^{-1}$. The leading term at $\rho = 0$ of each
Myers-Perry tensor is the Minkowski one. So $t_*^\lambda h^{(\mu),\le k}_b(t_*^{-\lambda+\mu}Y)\to t_*^\lambda\bar
h^{(\mu),\le k}(t_*^{-\lambda+\mu}Y)$ at $\iota^+$, and the corrections are
$O(t_*^{-\min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}})$ there. In the s1 and v1 terms,
$h_{b,\mathrm s1}(a_{\mathrm s1}S)$, $\breve h^1_{b,\mathrm s1}(a'_{\mathrm s1}S)$ and
$h_{b,\mathrm v1}(a_{\mathrm v1}V)$ are of size $\rho^3t_*^{-\lambda+1}$ (or $\rho^3\log t_*$), $\rho^2t_*^{-\lambda}$
and $\rho^3t_*^{-\lambda}$ (III.D$''$ (3.4)). These are $O(t_*^{-\lambda-2})$ at $(\iota^+)^\circ$. The next terms
reproduce the Minkowski ones. The coefficient of $\breve h^2_{b,\mathrm s1}$ is $a''_{\mathrm s1}S = t_*^{-\lambda-1}S$,
and that of $\breve h^1_{b,\mathrm v1}$ is $a'_{\mathrm v1}V = t_*^{-\lambda-1}V$, as in Theorem 3.1. With
$\chi_K|_{\iota^+}$ and $\chi_\iota = 1$ near $\iota^+$, $(t_*^\lambda u)|_{\iota^+} = \chi_Ku_0+\tilde u = u_+$.

*Away from $K^+$.* Near $\iota^+$, $u = t_*^{-\lambda}u_+$ up to terms supported near $K^+$. Lemma 4.1 gives
$t_*^{-\lambda-2}f_+-L_b(t_*^{-\lambda}u_+) = -t_*^{-\lambda-4}v^2Bu_+$. As
$u_+\in\mathcal A^{(\langle\mathcal E^C_{\iota^+,\mathscr I}\rangle,\ell_I)}$ at $v = 0$ (III.G$'$ Theorem 3.1),
$v^2Bu_+$ has $\mathscr I^+$-index set in $\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}+2$ to order $\ell_I+2$. Its
$\iota^+$-orders are $\lambda+4+\mathbb N_0$, from the Taylor expansion of the coefficients in $\rho = v/t_*$. The
commutator $[L_b,\chi_\iota] = \chi'(t_*)[L_b,t_*]+\frac12\chi''(t_*)[[L_b,t_*],t_*]$ is supported in
$\{1\le t_*\le2\}$. By (2.3), at fixed $t_*$ (where $\rho = v/t_*$ and $\rho\partial_\rho = v\partial_v$), its main part
on $t_*^{-\lambda}\tilde u$ is $-\chi't_*^{-\lambda-1}v(v\partial_v-\frac32-\bar S)\tilde u$. Near $\mathscr I^+$,
$\tilde u = u_+$, and $(v\partial_v-\frac32-\bar S)u_+\in H^{\infty,(\mathcal E^C_{\iota^+,\mathscr I},\ell_I)}_{\mathrm
b}$ by III.G$'$ Theorem 3.1 (2). So this part has $\mathscr I^+$-index set
$\mathcal E^C_{\iota^+,\mathscr I}+1 = \mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}+2$ to order $\ell_I+1$, which is
the order (4.4) asks. The other parts carry $\rho^2 = v^2t_*^{-2}$ or $\rho^3$ and give
$\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}+2$ as well.

*Near $K^+$.* Each term of (4.4) has $K^+$-order at least $\lambda+\ell_K$: $\chi_\iota t_*^{-\lambda-2}f_+$, as $f_+$
has weight $\ell_K-2$ at $R = 0$ and $t_*^{-\lambda-2}R^{\ell_K-2} = t_*^{-\lambda-\ell_K}r^{\ell_K-2}$; -
$L_b(\chi_\iota t_*^{-\lambda}\tilde u)$, as $\tilde u$ has weight $\ell_K$, $L_b$ is stationary, and $\partial_{t_*}$
only adds decay; $[L_b,\chi_K]u_{b,0}$, supported away from $K^+$; and $L_bu_{b,0}$ on $\operatorname{supp}\chi_K$: by
Lemma 2.6 each term has $K^+$-order $\ge\lambda+3>\lambda+\ell_K$.

*The $\iota^+$-order of the remainder near $K^+\cap\iota^+$.* $t_*^{\lambda+2}L_bu$ restricted to $\iota^+$ is
$N_{\iota^+}(\lambda)u_+ = f_+$, by Lemma 4.1 and $(t_*^\lambda u)|_{\iota^+} = u_+$. The Myers-Perry corrections in
$u_{b,0}$ and the terms of Lemma 4.1 contribute at $\iota^+$-orders in $\lambda+2+\mathcal E_{\mathrm{ind}}$, with
$\mathcal E_{\mathrm{ind}}$ collecting the states' index sets of III.D$''$, III.D$'''$, III.F$''''$ and $2+\mathbb N_0$.
So the remainder's $\iota^+$-index set is $\lambda+2+\mathcal E_{\mathrm{ind}}$. The membership of $u$ follows term by
term: $t_*^{-\lambda}\tilde u$ and (4.3), whose $t_*$-exponents are those collected in
$\mathcal E^{\mathrm{gr}}_K(\lambda)$. $\square$

As in the source, an $O(t_*^{-\lambda-2})$ source can set the black hole in motion. The s1 term is a centre-of-mass
motion of size $O(t_*^{-\lambda+1})$, or $O(\log t_*)$ at $\lambda = 1$; at $n = 4$ there are four directions. The v1
term is invisible at $\iota^+$ and non-zero only for $A\ne0$ (III.D$''$ Proposition 3.1 (3)); it is an $O(|A|)$ change
of the rotation in $\mathfrak{so}(4)$.

For fixed $\epsilon>0$ and $\lambda$ near $\lambda_0$, $\lambda\notin\mathrm{spec}_{\iota^+}(\bar L)$, Theorem 4.2
defines $\Phi_{\iota,b}(\lambda)f_+ := u$ and
$F_{\iota,b}(\lambda)f_+ := \chi_\iota t_*^{-\lambda-2}f_+-L_b\Phi_{\iota,b}(\lambda)f_+$ on
$H^{\infty,\ell_I+1,\ell_K-2}_{\mathrm b}(\iota^+)$. These are holomorphic, with values in $H^{\infty,(\langle\mathcal
E^C_{\iota^+,\mathscr I}\rangle,\ell_I),\lambda_0-\epsilon,\lambda_0-1-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}$ and
$H^{\infty,(\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}+2,\ell_I+1),\lambda_0+2+\min\mathrm{Re}\,\mathcal
E_{\mathrm{ind}}-\epsilon,\lambda_0+\ell_K-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}$ (the source's (9.42a)-(9.42b)).
Holomorphy holds because $f_+\mapsto u_+$ is (III.G$'$ Theorem 3.1 (2)), the coefficients $Y^{(\mu)}_\tau$ are
continuous functionals of $u_+$ (Theorem 3.1), $t_*^{-\lambda}$ and $a_{\mathrm s1}$, $a_{\mathrm v1}$ are holomorphic
in $\lambda$ with values in these weighted spaces, and the states do not depend on $\lambda$.

**Corollary 4.3 ([Hin26] Corollary 9.12 at $n = 4$).** Let $\mathrm{Re}\,\lambda_0>1$. Let $l_0$ be the order of the
pole of $N_{\iota^+}(\bar L,\cdot)^{-1}$ at $\lambda_0$ ($l_0 = 0$ if $\lambda_0\notin\mathrm{spec}_{\iota^+}(\bar L)$).
Let $\ell_K$ and $\ell_I$ be as in Theorem 4.2, with $\mathrm{Re}\,\lambda_0<\ell_I$. Let $k\in\mathbb N_0$ and $f\in
H^{\infty,\ell_I+1,(\lambda_0+2,k),\lambda_0+\ell_K-\epsilon}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-}$ for all
$\epsilon>0$. Then there are $u^{(j)}_{b,0}$ of the form (4.3), with $\lambda_0$ for $\lambda$ and a factor
$(\log t_*)^j$ in each argument, and $\tilde u^{(j)}\in\bigcap_\epsilon H^{\infty,(\langle\mathcal E^C_{\iota^+,\mathscr
I}\rangle,\ell_I),\ell_K-\epsilon}_{\mathrm b}(\iota^+)$, $j = 0,\dots,k+l_0$, such that
$u := \sum_j\chi_Ku^{(j)}_{b,0}+\chi_\iota t_*^{-\lambda_0}(\log t_*)^j\tilde u^{(j)}$ satisfies
$$f-L_bu\in\bigcap_{\epsilon>0}H^{\infty,(\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}+2,\ell_I+1),\ \lambda_0+2
+\mathcal E_{\mathrm{ind}},\ \lambda_0+\ell_K-\epsilon}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-}.\tag{4.5}$$

*Proof.* As in the source. Write $f = \sum_{j\le k}\chi_\iota t_*^{-\lambda_0-2}(\log t_*)^jf^{(j)}_+$, up to a
remainder of $\iota^+$-order $\infty$ and $K^+$-order $\lambda_0+\ell_K-\epsilon$, with
$f^{(j)}_+\in\bigcap_\epsilon H^{\infty,\ell_I+1,\ell_K-2-\epsilon}_{\mathrm b}(\iota^+)$. Then $f = \frac1{2\pi
i}\oint\sum_j(-1)^jj!(\lambda-\lambda_0)^{-j-1}\chi_\iota t_*^{-\lambda-2}f^{(j)}_+\,d\lambda$, over a small circle
around $\lambda_0$ on which $\lambda\notin\mathrm{spec}_{\iota^+}(\bar L)$. Put $u := \frac1{2\pi
i}\oint\sum_j(-1)^jj!(\lambda-\lambda_0)^{-j-1}\Phi_{\iota,b}(\lambda)f^{(j)}_+\,d\lambda$. Then $f-L_bu$ is the same
integral of $F_{\iota,b}(\lambda)f^{(j)}_+$, of the stated orders by the holomorphy above. Expanding in $t_*$ gives the
polyhomogeneity: the power of $\log t_*$ is at most the order of the pole of the integrand at $\lambda_0$ minus 1, that
is $k+l_0$. $\square$

## 5. Findings

(G$''$1) *The window at $n = 4$ is $\ell_K<3$ (with (C5), or $\ell_K<2+2\gamma_Cv_C$ without it).* Every $\iota^+$-order
grafted exceeds 1, so the remainder's $K^+$-order $\lambda+\ell_K$ can exceed 4 with $\ell_K<3$. Then no state at $-3$
is needed: neither the physical s3, v3, t3 nor the pure gauge s5, v4. Neither are the companions of the physical states
at $-2$, which III.F$''''$ (F$''''$3) left unconstructed. The record's estimate $[\alpha_5-4,0]$ (10.35 (c)) lies inside
this window, and its reading of $\alpha_5$ is not needed.

(G$''$2) *The v1 root of $\Box^C$*, $-2-2\gamma_Cv_C$, is the one root from the constraint operator that can enter the
window. It is excluded by (C5), $\gamma_Cv_C\ge\frac12$, an obligation for Part VI. Without (C5) the window is
$\ell_K<2+2\gamma_Cv_C$, which still serves every $\lambda>2-2\gamma_Cv_C$.

(G$''$3) *The spanning statement* deferred by III.D$'''$ is proved for the window (Lemma 1.2), from simplicity of the
roots ((C2)-(C3), $z\notin Z_{\mathrm{exc}}$), (R5) and III.F$''''$ Proposition 5.1.

(G$''$4) *The expansion's lowest term* is identified from the equation (Theorem 3.1's first step), so the source's
ordering of the iteration (the s0 and s2 roots first, then "two types of indicial roots") is replaced by an induction on
the least exponent. The expansion is log-free below $\ell_K^{\max}$ (Corollary 3.2). This gives the $n = 4$ index set at
$K^+$ that III.G$'$ (G$'$2) left to this part.

(G$''$5) *The source's Proposition 9.11 does not state $\mathrm{Re}\,\lambda<\ell_I$*, which its use of Proposition 9.4
(2) (finite decay at $\mathscr I^+$) needs; Corollary 9.12 states it. Theorem 4.2 assumes it.

(G$''$6) *The $\iota^+$-normal operator.* The source's step "$L_b\in\rho_I\rho_+^2\mathrm{Diff}^2_{\mathrm b}$, then the
first term of (8.3b) via (9.17)" is replaced by the exact identity (4.1). With it, the remainder near $\iota^+$ away
from $K^+$ is $t_*^{-\lambda-4}v^2Bu_+$, with $\mathscr I^+$-index set $\mathcal E^{\mathrm{tot}}+2$. (9.17) enters only
through the commutator with $\chi_\iota$, which is taken to be a function of $t_*$, and only to the finite order that
III.G$'$ (3.2) gives (III.G$'$ (G$'$4)).

(G$''$7) *At $n = 4$ the boost and rotation states decay one order faster* ($\rho^3$, $\rho^2$, $\rho^3$ against the
source's $\rho^2$, $\rho$, $\rho$; III.D$''$ (3.4)), so their invisibility at $\iota^+$ holds with room.