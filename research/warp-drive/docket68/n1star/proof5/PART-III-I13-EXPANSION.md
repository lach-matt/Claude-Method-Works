# Part III.I$''''''''''''$. The expansion at $K^+$ to the order $4+\epsilon_K$, n = 4 ([Hin26] Theorem 11.59, Part 4)

*Status.* Written (D276); verified (D277: verifier 118's findings seated, to be read). This part proves, at spatial
dimension $n = 4$, Part 4 of the proof of [Hin26] Theorem 11.59 (pp. 289-292) and the $\iota^+$-part of its (11.222):
the forward solution $u$ of III.I$'''''''''''$ Theorem 4.1, which decays at $K^+$ at the order $\alpha-2$, is a sum of
towers of the zero-energy states of III.G$''$ Table 1.1, with coefficients that are functions of $t_*$, modulo a
remainder of $K^+$-order $\alpha$ (Theorem 3.1, the $n = 4$ form of (11.196)); the coefficients are partially
polyhomogeneous, except for a conormal boost coefficient $\dot S_{\mathrm{rem}}$ of order $\alpha-2$ and a conormal
parameter $\dot b_{\mathrm{rem}}$ of order $\alpha-1$; and $u$ is partially polyhomogeneous at $\iota^+$ with an index
set $\mathcal E_\sharp$ to the order $3+\eta_2$, $\eta_2<\epsilon_+$ as close to $\epsilon_+$ as desired.

*What n = 4 changes.* (1) *The spacetime phase reaches the order $\alpha$ at once.* The $\iota^+$-terms of $u$-exponent
$\lambda_0<2$ are solved by III.G$''$ Corollary 4.3 with $\ell_K = \alpha-\mathrm{Re}\,\lambda_0<3$ (III.I$''''''''''$
section 3), and its remainder $\chi_\iota t_*^{-\lambda_0}\tilde u$ has $K^+$-order
$\mathrm{Re}\,\lambda_0+\ell_K-\epsilon = \alpha-\epsilon$ (III.G$''$ Theorem 4.2's proof, *Near $K^+$*); so the
source's Step 4.1 needs no further work. (2) *The rows.* The towers are those of III.G$''$ Table 1.1, roots
$\mu\in(-3,0]$; the physical states at $\mu = -2$ (III.F$''''$ Proposition 5.1) enter with rates $\lambda_0+2<\alpha$
only for $\lambda_0\le2$, and nothing at $\mu\le-3$ is needed. (3) *From the spectral side to spacetime.* The pieces of
III.I$'''''''''''$ Proposition 3.1 are towers in $\sigma$ times scalar functions of $\sigma$, cut off by
$\chi_{\mathrm{zf}}(|\sigma|r)$; the cut-off is an approximate identity with vanishing moments (Lemma 2.1), so each
piece is, near $K^+$, the spacetime tower of the inverse transform of its scalar coefficient, up to terms rapidly
decaying at $K^+$. (4) *No logarithmic column term*, as in III.I$'''''''''''$ (I$'''''''''''$4); the columns at the last
level give the conormal $\dot S_{\mathrm{rem}}$ and $\dot b_{\mathrm{rem}}$ (Lemma 2.2). Notation: Parts II.G$'$, III.A,
III.D$'''$, III.F$'$, III.F$'''$, III.F$''''$, III.G$''$, III.G$''''$, III.H, III.I-III.I$'''''''''''$; no instrument is
used.

## 1. Setting

Everything of III.I$'''''''''''$ sections 1-4 is kept: $\alpha\in(4,4+\epsilon_K]$ admissible, $\ell_3 =
\alpha-4-\epsilon$, $\eta_1<\eta_2$ in $(\epsilon_K,\epsilon_+)$, $\mathcal E_{\mathrm{col}}$, the pieces of its
Proposition 3.1, Lemma 3.2 and Theorem 4.1. We take $\eta_2\in(\epsilon_+-\delta_+,\epsilon_+)$ for a
$\delta_+\in(0,\epsilon_+-\epsilon_K)$ fixed in advance (III.I$'''''''''''$ allows any
$\eta_2\in(\epsilon_K,\epsilon_+)$ off a finite set), so that the $\iota^+$-order $3+\eta_2-2\epsilon$ below is as close
to $3+\epsilon_+$ as desired. Let $F\in\mathcal Y^0(\alpha)$, $(h,\vec p)$ small, $\vec p\,'$ as in III.I$'''''''''''$
Theorem 4.1 and $u$ the forward solution of $L_{h,\vec p}u = F-D_{\vec p}P_4(h,\vec p)(\vec p\,')$.

**Definition 1.1 (coefficients; the source's Definition 11.58).** For an index set $E\subset\mathbb C\times\mathbb N_0$,
$w\in\mathbb R$ and a finite-dimensional space $\mathcal Y$, $\dot H^{\infty,\mathcal Q(E,w)}_{\mathrm
b}([1,\infty];\mathcal Y)$ is the space of $a\in C^\infty(\mathbb R;\mathcal Y)$ supported in $[1,\infty)$ with
$$a-\chi_+(t_*)\sum_{(z,k)\in E,\ \mathrm{Re}\,z<w}c_{z,k}\,t_*^{-z}(\log t_*)^k\in t_*^{-w}H^\infty_{\mathrm
b}([1,\infty),|\tfrac{dt_*}{t_*}|;\mathcal Y),\qquad c_{z,k}\in\mathcal Y,\tag{1.1}$$
$\chi_+\in C^\infty(\mathbb R)$ vanishing on $(-\infty,1]$ and equal to 1 on $[2,\infty)$; $\dot H^{\infty,w}_{\mathrm
b} := \dot H^{\infty,\mathcal Q(\emptyset,w)}_{\mathrm b}$. As $t_*\partial_{t_*}$ preserves these spaces,
$a^{(j)}\in\dot H^{\infty,\mathcal Q(E+j,w+j)}_{\mathrm b}$.

*Towers.* The rows of III.G$''$ Table 1.1 are $\rho = (\mu,\tau)$ with roots $\mu\in(-3,0]$ and harmonics $\mathcal
Y_\rho$; let $\mathcal R$ be the set of these rows, $\mathcal R'$ the set without the boost row $(-1,\mathrm s1)$. For
$a$ valued in $\mathcal Y_\rho$ let $T_\rho(a) := h^{(\mu),\le k_\mu}_{b_0,\tau}(a)$ (III.G$''$ Definition 2.5), with
$h^{\le2}_{b_0,\mathrm v1}$ for the rotations; and $h^{\le1}_{b_0,\mathrm s1}(a) = h_{b_0,\mathrm s1}(a)+\breve
h^1_{b_0,\mathrm s1}(a')$ for the boosts. The *spectral tower* of $\rho$ is $T_\rho(\sigma)Y := \sum_{j\le
k_\mu}(-i\sigma)^j\breve h^{(\mu),j}_{b_0,\tau}(Y)$, so that $\mathcal F(T_\rho(a)) = T_\rho(\sigma)\hat a(\sigma)$ for
$a$ independent of $x$. By III.G$''$ section 2, $\breve h^{(\mu),j}_{b_0,\tau}$ is polyhomogeneous at $\partial X$ with
leading order $\rho^{\mu-j}$ (it grows like $r^{j-\mu}$), the Myers-Perry corrections being smaller by
$\min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}>0$; for the boosts $h_{b_0,\mathrm s1}\in\mathcal A^3$ and $\breve
h^1_{b_0,\mathrm s1}\in\mathcal A^2$ (III.H section 2), and $\breve h^j_{b_0,\mathrm s1}$, $j\ge2$, has leading order
$\rho^{1-j}$; for the rotations $h_{b_0,\mathrm v1} = 0$ and $\breve h^j_{b_0,\mathrm v1}$ has leading order
$\rho^{-j}$. We write $d_\rho := \mu$ for the rows other than the boosts and rotations, $d_{\mathrm v1} := 0$, and
$d_{\mathrm s1} := 1$ for $h^{\le k}_{b_0,\mathrm s1}$, $k\ge2$: then for $a = t_*^{-z}$ the leading part of $T_\rho(a)$
is homogeneous of degree $-z-d_\rho$ in $(t_*,r)$, so that its $K^+$-rate is $z$ (for v1, $z+1$, as $h_{b_0,\mathrm v1}
= 0$) and its order at $\iota^+$ is $z+d_\rho$; for $h^{\le1}_{b_0,\mathrm s1}(a)$ the order at $\iota^+$ is $z+3$.

*Rates.* For $a\in\dot H^{\infty,w}_{\mathrm b}$ and $\rho\ne\mathrm v1$, $\chi_KT_\rho(a)$ has $K^+$-order $w$ and the
term with $a^{(j)}$ has $K^+$-order $w+j$; so the terms with $j\ge2$ of a coefficient of order $>\alpha-2$ are of order
$>\alpha$, and the lengths $k_\mu$ are immaterial for the statements below (the source's Remark 11.60 (2)).

*The index set at $\iota^+$.* Let $\mathcal E_\sharp := \{(\lambda,k):\lambda\in\Lambda,\ k\le K(\lambda)\}\cup\mathcal
M$ (III.I$''''''''''$ Definition 1.1), an index set closed under conjugation with $\min\mathrm{Re}\,\mathcal
E_\sharp\ge\lambda_\sharp$; by III.I$''''''''''$ Lemma 1.2 (b) its part of real part $<3+\epsilon_+$ does not depend on
$\mathcal E_+$, so $\mathcal E_+\supset\mathcal E_\sharp\cap\{\mathrm{Re}<3+\epsilon_+\}$ can be required with (H1)-(H3)
(the source's Remark 11.62).

## 2. Lemmas

Let $\chi\in C^\infty_c((-1,1))$ be the low-frequency cut-off of III.I$'''''''''''$ (equal to 1 near
$[-\frac12,\frac12]$), and $\chi_{\mathrm{zf}} = \chi_0(\hat r)$ with $\chi_0\in C^\infty_c([0,1))$ equal to 1 near 0,
so that $k := \mathcal F^{-1}[\chi_0(|\zeta|)]$ is a Schwartz function with $\int k = 1$ and $\int s^mk(s)\,ds = 0$ for
$m\ge1$ (the derivatives at 0 of $\chi_0(|\zeta|)$, which is 1 near 0). A *profile* of *degree* $d$ is a section $p$ on
$X$, conormal at $\partial X$, with $|p|\lesssim r^{-d}\langle\log r\rangle^l$ for $r\ge1$ and some $l$, with
b-derivatives; it is *polyhomogeneous* if it is so at $\partial X$, with leading order $\rho^d$. The profiles of Theorem
3.1 are in general only polyhomogeneous to a finite order (for instance $\hat u_2$, $\hat u_3$ of III.I$'''''''''''$
Proposition 3.1, and $v_0$ below), and some carry a factor $\log r$.

**Lemma 2.1 (the cut-off as an approximate identity).** Let $p_0,\dots,p_k$ be profiles of degrees $d_j\ge d-j$,
$P(\sigma,x) := \sum_j(-i\sigma)^jp_j(x)$, and let $c = \sum_\pm1_{\pm\sigma>0}c^\pm$ with either (a) $c^\pm\in
H^{\infty,w}_{\mathrm b}(\pm(0,1),|\frac{d\sigma}\sigma|)$, $w>-1$, or (b) $c
= |\sigma|^z(\log|\sigma|)^m\mathrm{sgn}(\sigma)^\delta$, $\mathrm{Re}\,z>-1$ (then $w := \mathrm{Re}\,z$). Put $y :=
\mathcal F^{-1}(\chi c)$. Then on $\{t_*\ge1\}$
$$\mathcal F^{-1}\big[\chi(|\sigma|)\chi_{\mathrm{zf}}(|\sigma|r)c(\sigma)P(\sigma,x)\big] =
\chi_K\sum_j(\chi_+y)^{(j)}(t_*)\,p_j(x)+R,\tag{2.1}$$
where $R$ has $K^+$-order $\infty$ (for every $N$, $|R|\lesssim(r/t_*)^Nt_*^{-w-1}\langle r\rangle^{-d}$ on $\{r\le
t_*/8\}$ (up to logarithms), with b-derivatives) and, near $\iota^+$, order $w+1+d$; in case (b), if the $p_j$ are
polyhomogeneous, $R$ and $\chi_K\sum_j(\chi_+y)^{(j)}p_j$ are polyhomogeneous at $\iota^+$, with exponents $z+1+d$ plus
those of the expansions of the $p_j$ (and logs up to $m$), and if $p_j = p_j^{\mathrm{ph}}+p_j^{\mathrm c}$ with
$p_j^{\mathrm{ph}}$ polyhomogeneous and $p^{\mathrm c}_j$ of degree $\ge d'-j$, the part from the $p^{\mathrm c}_j$ has
order $\mathrm{Re}\,z+1+d'$ at $\iota^+$; $\chi_+y\in\dot H^{\infty,\mathcal Q((z+1,m),\infty)}_{\mathrm b}$. In case
(a), $\chi_+y\in\dot H^{\infty,w+1}_{\mathrm b}$.

*Proof.* $y$ satisfies the symbol estimates $|(t\partial_t)^ly^{(j)}(t)|\lesssim\langle t\rangle^{-w-1-j}$ (II.G$'$
(2.26a) for (a); in case (b) $y$ is $c_\pm|t|^{-z-1}$ times polynomials in $\log|t|$ plus a Schwartz function, as
$t\to\pm\infty$), so $\chi_+y$ lies in the stated classes. For every $x$ the left side of (2.1) is
$\sum_j(y^{(j)}+e_{j,r})(t_*)p_j(x)$ (as $\mathcal F(a') = -i\sigma\hat a$), with $e_{j,r} := \mathcal
F^{-1}[(-i\sigma)^j\chi c\,(\chi_0(|\sigma|r)-1)]$. Let $\chi_0 = 1$ on $[0,c_0]$. The symbol of $e_{j,r}$ vanishes for
$|\sigma|\le c_0/r$, so $e_{j,r} = 0$ for $r<c_0$; for $r\ge c_0$ it satisfies $|\partial^l_\sigma[(-i\sigma)^j\chi
c(\chi_0(|\sigma|r)-1)]|\lesssim|\sigma|^{j+w-l}$ on its support, as $\partial^l_\sigma[\chi_0(|\sigma|r)] =
r^l\chi_0^{(l)}(|\sigma|r)\mathrm{sgn}(\sigma)^l$ lives where $|\sigma|r\le1$, and the jump of $c$ at $\sigma = 0$ lies
outside the support. Integrating by parts $M>j+w+1$ times,
$$|e_{j,r}(t)|\lesssim|t|^{-M}\int_{|\sigma|\ge c_0/r}|\sigma|^{j+w-M}\,d\sigma\lesssim|t|^{-M}r^{M-j-w-1} =
(r/|t|)^{M-j-w-1}|t|^{-j-w-1},$$
and likewise with b-derivatives ($t\partial_t$ and $r\partial_r$ preserve this symbol class). On $\{r\le t_*/8\}$, where
$\chi_K = \chi_+ = 1$ for $t_*\ge2$, $R = \sum_je_{j,r}p_j$ for $t_*\ge2$; with $|p_j|\lesssim\langle r\rangle^{j-d}$
(up to logarithms) this gives $|R|\lesssim(r/t)^Nt^{-w-1}\langle r\rangle^{-d}$ for every $N$, the b-derivatives alike.
For $r\ge2$, $\chi = 1$ on the support of $\chi_0(|\sigma|r)$, and the left side is $\sum_j(y^{(j)}*k_r)(t_*)p_j(x)$,
$k_r(s) := r^{-1}k(s/r)$. On $\{r\ge t_*/8\}$, $r\ge2$: $\sigma = \zeta/r$ gives $(y^{(j)}*k_r)(t) = r^{-1-j}\int
e^{-i\zeta t/r}\chi_0(|\zeta|)(-i\zeta)^jc(\zeta/r)\frac{d\zeta}{2\pi}$, of size $r^{-1-j-w}$ uniformly in $t/r$ (symbol
estimates of $c$), so the left side is $O(r^{-1-w-d})$ there, and so is $\chi_K\sum_j(\chi_+y)^{(j)}p_j$ ($\chi_K$
vanishes for $r\ge t_*/2$, and $|y^{(j)}p_j|\lesssim t^{-w-1-j}r^{j-d}$); this is the order $w+1+d$ at $\iota^+$. In
case (b) the left side is, for $r\ge2$, $r^{-1-z}$ times a smooth function of $t/r$ (with $\log r$-factors up to $m$)
times the $p_j$ (the conormal parts $p^{\mathrm c}_j$ giving the order $\mathrm{Re}\,z+1+d'$), and
$\chi_K\sum_j(\chi_+y)^{(j)}p_j$ is a function of $t_*$, polyhomogeneous at $t_*=\infty$, times $\chi_c(r/t_*)$ and the
$p_j$; both are polyhomogeneous at $\iota^+$ (coordinates $t_*^{-1}$, $r/t_*$) with the stated exponents. $\square$

**Lemma 2.2 (the columns at the last level).** Let $a>-1$, $S\in H^{\infty,a}_{\mathrm
b}(\pm(0,1),|\frac{d\sigma}\sigma|;\mathcal S_{1,\mathbb C})$, $\dot b\in H^{\infty,a}_{\mathrm
b}(\pm(0,1),|\frac{d\sigma}\sigma|;\mathfrak b_{\mathbb C})$, and put $A := \chi_+\mathcal F^{-1}[-\chi\sigma S]\in\dot
H^{\infty,a+2}_{\mathrm b}$, $B := \chi_+\mathcal F^{-1}[i\chi\sigma^2\dot b]\in\dot H^{\infty,a+3}_{\mathrm b}$. Then
on $\{t_*\ge1\}$
$$\mathcal F^{-1}\big[\chi\sigma^3\hat h^{\mathrm{aug}}(\sigma)(S)\big] = \chi_Kh^{\le1}_{b_0,\mathrm
s1}(A)+R_S,\qquad\mathcal F^{-1}\big[\chi\sigma^3\hat g^{\mathrm{aug}}(\sigma)(\dot b)\big] = \chi_K\dot
g(B)+R_b,\tag{2.2}$$
with $R_S$, $R_b$ of $K^+$-order $a+4$ and order $a+5$ at $\iota^+$.

*Proof.* By III.H (2.6), $\sigma^3\hat h^{\mathrm{aug}}(S) = -\sigma\Psi
h(S)+\sigma^2(\partial_\sigma\Psi)h(S)+i\sigma^2\Psi\breve h(S)$ and $\sigma^3\hat g^{\mathrm{aug}}(\dot b) =
i\sigma^2\Psi\dot g(\dot b)$, where $\Psi(\sigma,x) = \int e^{i\sigma t}\phi_x(t)\,dt$, $\phi_x :=
\partial_{t_*}\chi_K(\cdot,x)$, $\int\phi_x = 1$; for $r\ge1$, $\phi_x(t) = r^{-1}\phi(t/r)$ with $\phi(s) =
\partial_s[\chi_c(1/s)]$ supported in $[2,4]$ (III.H Lemma 2.5 (b)), and for $r\le1$, $\phi_x$ is supported in $[1,4]$.
Products with $\Psi$ and $\partial_\sigma\Psi$ are convolutions in $t$ with $\phi_x$ and with $it\phi_x(t)$. With $a_0
:= \mathcal F^{-1}[-\chi\sigma S]$ (so $\mathcal F^{-1}[\chi\sigma^2S] = -ia_0'$), the first identity's left side is
$$h(S)\Big(\int\big(a_0(t-\tau)+\tau a_0'(t-\tau)\big)\phi_x(\tau)\,d\tau\Big)+\breve h(S)\Big(\int
a_0'(t-\tau)\phi_x(\tau)\,d\tau\Big),$$
($S$ applied to the scalar coefficients). By Taylor's formula $a_0(t-\tau)+\tau a_0'(t-\tau) =
a_0(t)-\tau^2\int_0^1\theta a_0''(t-\theta\tau)\,d\theta$ (the first moments cancel) and $a_0'(t-\tau) =
a_0'(t)-\tau\int_0^1a_0''(t-\theta\tau)\,d\theta$; as $\tau\le4\max(r,1)$ on $\mathrm{supp}\,\phi_x$, on $\{r\le
t_*/8\}$ the remainder is bounded by $\max(r,1)^2t^{-a-4}|h|+\max(r,1)t^{-a-4}|\breve h|\lesssim t^{-a-4}r^{-1}$
($h\in\mathcal A^3$, $\breve h\in\mathcal A^2$), with b-derivatives: $K^+$-order $a+4$. On $\{r\ge t_*/8\}$, $r\ge2$,
the right side is $O(t^{-a-2}r^{-3}+t^{-a-3}r^{-2})$ ($\chi_K$ vanishes for $r\ge t_*/2$), and the left side is
$O(r^{-a-5})$: for $r\ge1$, $\Psi = \Phi(\sigma r)$ and $\partial_\sigma\Psi = r\Phi'(\sigma r)$ with $\Phi$ Schwartz
(III.H Lemma 2.5 (b)), and $\sigma = \zeta/r$ gives $\mathcal F^{-1}[\chi\sigma\Phi(\sigma r)S],\ \mathcal
F^{-1}[\chi\sigma^2r\Phi'(\sigma r)S] = O(r^{-2-a})$ and $\mathcal F^{-1}[\chi\sigma^2\Phi(\sigma r)S] = O(r^{-3-a})$
uniformly in $t/r$ (the symbol estimates of $S$, as in Lemma 2.1's proof), with $h\in\mathcal A^3$, $\breve h\in\mathcal
A^2$: order $a+5$ at $\iota^+$. Replacing $a_0$ by $A = \chi_+a_0$ changes the right side only for $t_*\le2$, where
$\chi_K$ is supported in $\{r\le1\}$. The second identity is the same computation with $b_0 := \mathcal
F^{-1}[i\chi\sigma^2\dot b]$ and $\dot g\in\mathcal A^2$: $\int b_0(t-\tau)\phi_x(\tau)\,d\tau =
b_0(t)-\int\tau\int_0^1b_0'(t-\theta\tau)\,d\theta\,\phi_x(\tau)\,d\tau$, the remainder $O(\max(r,1)t^{-a-4}r^{-2})$,
and $\mathcal F^{-1}[i\chi\sigma^2\Phi(\sigma r)\dot b] = O(r^{-3-a})$ on $\{r\ge t_*/8\}$. $\square$

*Stationary solutions.* $L_0 := \widehat{L_{b_0}}(0)$, $L_1 = [L_{b_0},t_*]$, $L_2 = \frac12[[L_{b_0},t_*],t_*]$
(III.I$''''''$ section 1), so that $L_{b_0}(a(t_*)p) = aL_0p+a'L_1p+a''L_2p$ for stationary $p$, and a tower
$\sum_ja^{(j)}\breve h^j$ satisfies $L_0\breve h^m+L_1\breve h^{m-1}+L_2\breve h^{m-2} = 0$ for $m$ up to its length
(III.G$''$ (2.2)). In particular the bottom $\breve h^{(\mu),0}_{b_0,\tau}(Y)$ of each row of $\mathcal R'$ other than
v1 lies in $\ker L_0$, and so do $h_{b_0,\mathrm s1}(S)$, $\breve h^1_{b_0,\mathrm v1}(V)$ ($h_{b_0,\mathrm v1} = 0$)
and $\dot g(\dot b)$.

**Lemma 2.3 (stationary solutions of moderate growth).** Let $\mathcal G$ be the space of sections on $X$ that are
conormal at $\partial X$ of some order $>-3$ (in $\mathcal A^a$, $a>-3$); write $h := h_{b_0,\mathrm s1}$, $\breve h^j
:= \breve h^j_{b_0,\mathrm s1}$.

(a) If $p\in\mathcal G$ and $L_0p = 0$, then $p = \sum_\rho\breve h^{(\mu_\rho),0}_{b_0,\tau_\rho}(Y_\rho)+\breve
h^1_{b_0,\mathrm v1}(V)+\dot g(\dot b)+h(S)$, the sum over the rows of $\mathcal R'$ other than v1, with unique
coefficients; the rows with $\mu_\rho<-q$ do not occur if $p = O(r^q)$.

(b) If $X\in\mathcal G$, $\dot b\in\mathfrak b_{\mathbb C}$, $S\in\mathcal S_{1,\mathbb C}$ and $L_0X = L_1\dot g(\dot
b)+L_1\breve h^1(S)+L_2h(S)$, then $\dot b = 0$, and the s1-component of the $\rho^{-1}$-coefficient of the reduced
section (below: $X$ after the subtraction of the states of lower root) is that of $\breve h^2(-S)$. In particular
$L_1\dot g(\dot b)\in L_0(\mathcal G)$ only for $\dot b = 0$, and the reduction of an element of $\ker L_0\cap\mathcal
G$ subtracts no growing boost section $\breve h^2(S')$, $S'\ne0$.

*Proof.* *The reduction.* Let $X\in\mathcal G$ with $L_0X\in\mathcal A^3$. As $L_0 = \rho^2A$ with $A$ b-elliptic
(III.F$'$ section 2) and $\rho^{-2}L_0X\in\mathcal A^1$, III.A Lemma 1.4 makes $X$ polyhomogeneous modulo $\mathcal
A^1$, with exponents at the indicial roots of real part in $(a,1)$ (without logarithms, the roots being simple and the
source conormal). Let $\mu_0$ be the least real part of an exponent of $X$, and suppose $\mu_0\le0$. As every indicial
root is simple (III.G$''$ section 1), the argument of III.G$''$ Theorem 3.1's proof (*The lowest term*) applies: the top
logarithm at $\mu_0$ vanishes, $\mu_0$ is a root in $\mathcal W$ (real), and the $\rho^{\mu_0}$-coefficient is
$\sum_\tau\bar h_\tau(Y_\tau)$ (III.G$''$ Lemma 1.2). Subtract, for every type, the element of $\ker L_0$ listed above
with this leading term (for v1 at $-1$, $\breve h^1_{b_0,\mathrm v1}(V)$), and for s1 at $-1$ the section $\breve
h^2(S')$, $\bar h_{\mathrm s1}(S')$ being the s1-component; then $\mu_0$ rises (the corrections of the states are
smaller by $\min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}$), and $L_0$ of the new section is the old one plus $L_1\breve
h^1(S')+L_2h(S')$ (the tower relation $L_0\breve h^2+L_1\breve h^1+L_2h = 0$). After finitely many steps all exponents
have real part $>0$; as there are no roots in $(0,1]$ (III.F$'$ Proposition 2.3 (a)) and $\rho^{-2}L_0X\in\mathcal A^1$,
the result lies in $\mathcal A^1$.

(b) By the reduction, $X = X_1+(\text{elements of }\ker L_0\cap\mathcal G)+\breve h^2(S')$ with $X_1\in\mathcal A^1$ and
$L_0X_1 = L_1\dot g(\dot b)+L_1\breve h^1(S+S')+L_2h(S+S')$, $\bar h_{\mathrm s1}(S')$ the s1-component of the
$\rho^{-1}$-coefficient of the section reached at the root $-1$. By III.H (2.2), $\hat f_{\dot b}(0) = L_1\dot g(\dot
b)+L_0w_{\dot b}$ and $\hat f_{S''}(0) = L_2h(S'')+L_1\breve h^1(S'')+L_0w_{S''}$ with $w_{\dot b},w_{S''}\in\mathcal
A^1$ (III.H Lemma 2.3); so $\hat f_{\dot b}(0)+\hat f_{S+S'}(0) = L_0Q$, $Q := X_1+w_{\dot b}+w_{S+S'}\in\mathcal A^1$,
which lies in III.H's $\mathcal X_0$ (conormal order $\mu-2\in(0,1)$). Choose $u_e\in\ker L_0\cap\mathcal X_0$ with
$r(u_e) = -r(Q)$ (possible by the normalisation III.H (3.1) of the rows $f^*_1$, $f^*_2$ of $\tilde L_{b_0}(0)$). Then
$\tilde L_{b_0}(0)(-Q-u_e,\dot b,S+S') = (0,0)$, and III.H Proposition 3.2 gives $\dot b = 0$ and $S' = -S$.

(a) The reduction of $p$ ends in $p_1\in\mathcal A^1\cap\ker L_0$ once $S' = 0$, which is (b) with $\dot b = 0$, $S =
0$. Then $p_1\in\mathcal A^{2-}$ (the next roots are $\ge2$) lies in the domain of III.F$'''$ Proposition 4.1 for small
$\alpha$, whose nullspace (1) is spanned by $\dot g(\dot b)$ and $h(S)$. Uniqueness: $Y\mapsto\bar h_\tau(Y)$ is
injective (III.G$''$ Lemma 1.2) and that nullspace is eleven-dimensional. The last statement: a state of root $\mu$
grows like $r^{-\mu}$. $\square$

**Lemma 2.4 (formal solutions at $K^+$).** Let $\beta\in(\alpha-1,\alpha]$ and
$$w = \chi_K\sum_{i\in I}y_i(t_*)p_i(x)+w',\tag{2.3}$$
$I$ finite, with profiles $p_i\in\mathcal G$ of degrees $d_i$, $y_i\in\dot H^{\infty,\mathcal Q(E_i,\infty)}_{\mathrm
b}$ with every $(z,k)\in E_i$ satisfying $\mathrm{Re}\,z\ge\beta-2$ and $\mathrm{Re}\,z+d_i\ge\lambda_\sharp$
(*compatibility*), and $w'$ of $K^+$-order $\beta$. If $L_{b_0}w$ has $K^+$-order $\beta$, then
$$\chi_K\sum_iy_ip_i = \chi_K\Big(\sum_{\rho\in\mathcal R'}T_\rho(a_\rho)+h^{\le1}_{b_0,\mathrm s1}(a_{\mathrm s})+\dot
g(a_{\mathrm b})\Big)+w'',\tag{2.4}$$
where $a_\rho,a_{\mathrm s},a_{\mathrm b}$ are finite sums of terms $\chi_+t_*^{-z}(\log t_*)^k$, with exponents in
$\bigcup_iE_i+\mathbb N_0$ (for $a_{\mathrm v1}$, $\bigcup_iE_i+\mathbb N_0-1$), those of $a_\rho$ satisfying
$\mathrm{Re}\,z+d_\rho\ge\lambda_\sharp$, those of $a_{\mathrm b}$ of real part $\ge\beta-1$, and $w''$ has $K^+$-order
$\beta$; all are linear in $(y_i)$. *Exponents.* Let $\mathcal I$ be the set of $(z+e,k+l)$, $(z,k)\in E_i$, $(e,l)$ an
exponent of the polyhomogeneous part of $p_i$ ($i\in I$). For every exponent $(z,k)$ of $a_\rho$ with
$\mathrm{Re}(z+d_\rho)$ below the order at $\partial X$ (plus $\mathrm{Re}\,z$) of the non-polyhomogeneous parts of the
$p_i$, $(z+d_\rho,k)$ is an element of $\mathcal I$ plus finitely many elements of $\mathcal E_{\mathrm{ind}}$.

*Proof.* We remove the pairs $(z,k)$ with $\mathrm{Re}\,z<\beta$ one at a time, in order of increasing real part and, at
equal exponent, decreasing $k$. Let $(z_0,k_0)$ be the first pair whose coefficient section $P :=
\sum_ic^{(i)}_{z_0,k_0}p_i$ is non-zero, $c^{(i)}_{z,k}$ the coefficient of $t_*^{-z}(\log t_*)^k$ in $y_i$. In $\{r\le
R\}$, for large $t_*$, $\chi_K = 1$ and $L_{b_0}(yp) = yL_0p+y'L_1p+y''L_2p$, and $y',y''$ have the exponents
$(z+1,\cdot)$, $(z+2,\cdot)$; so the coefficient of $t_*^{-z_0}(\log t_*)^{k_0}$ in $L_{b_0}w$ is $L_0P$, which
vanishes, $L_{b_0}w$ and $w'$ being of $K^+$-order $\beta>\mathrm{Re}\,z_0$ on every $\{r\le R\}$. By compatibility $P =
O(r^{\mathrm{Re}\,z_0-\lambda_\sharp})$, $\mathrm{Re}\,z_0-\lambda_\sharp<\beta-\lambda_\sharp<3$, so Lemma 2.3 (a)
gives $P = \sum_\rho\breve h^{(\mu_\rho),0}(Y_\rho)+\breve h^1_{b_0,\mathrm v1}(V)+\dot g(\dot b)+h_{b_0,\mathrm s1}(S)$
with only rows $\mu_\rho\ge\lambda_\sharp-\mathrm{Re}\,z_0$.

*If $\mathrm{Re}\,z_0+1<\beta$, then $\dot b = 0$.* The coefficient of $t_*^{-z_0-1}(\log t_*)^{k_0}$ in $L_{b_0}w$ is
$L_0P_1-z_0L_1P$, $P_1$ the coefficient section of $(z_0+1,k_0)$ (the pairs $(z_0,k)$, $k>k_0$, have zero coefficient,
and none has real part below $\mathrm{Re}\,z_0$), and it vanishes. With the tower relations $L_1\breve h^{(\mu),0} =
-L_0\breve h^{(\mu),1}$, $L_1h_{b_0,\mathrm s1} = -L_0\breve h^1_{b_0,\mathrm s1}$ and $L_1\breve h^1_{b_0,\mathrm v1} =
-L_0\breve h^2_{b_0,\mathrm v1}$ (all these rows have $k_\mu\ge1$, below), $z_0L_1\dot g(\dot b)\in L_0(\mathcal G)$,
and $z_0\ne0$; Lemma 2.3 (b) gives $\dot b = 0$.

*Subtraction.* Let $a := \chi_+t_*^{-z_0}(\log t_*)^{k_0}$ and $\tilde a$ the polyhomogeneous antiderivative with
$\tilde a' = a$ on $[2,\infty)$ (exponents $(z_0-1,\le k_0)$; $z_0\ne1$ as $\mathrm{Re}\,z_0\ge\beta-2>1$), and subtract
$$w_1 := \chi_K\Big(\sum_\rho T_\rho(aY_\rho)+T_{\mathrm v1}(\tilde aV)+h^{\le1}_{b_0,\mathrm s1}(aS)+\dot g(a\dot
b)\Big).$$
Then $w-w_1$ is again of the form (2.3): the pair $(z_0,k_0)$ is gone, and the new terms $a^{(j)}\breve h^{(\mu),j}$,
$j\ge1$, have exponents $(z_0+j,\le k_0)$, later in the order, and are compatible ($z_0+j$ with degree $\mu-j$;
$h_{b_0,\mathrm s1}$, $\breve h^1_{b_0,\mathrm s1}$ have degrees 3, 2). And $L_{b_0}w_1$ has $K^+$-order $\beta$: by the
tower relations, $L_{b_0}T_\rho(aY)$ consists of the terms with $a^{(k_\mu+1)}$ and $a^{(k_\mu+2)}$ (III.G$''$ Lemma
2.6), of $K^+$-order $\mathrm{Re}\,z_0+k_\mu+1$; the rows with $\mu>-2$ have $k_\mu\ge1$ (III.G$''$ Table 1.1), and
$\mathrm{Re}\,z_0+2\ge\beta$; rows with $\mu\le-2$ occur only if $\mathrm{Re}\,z_0\ge\lambda_\sharp+2>\beta-1$;
$L_{b_0}h^{\le1}_{b_0,\mathrm s1}(aS)$ and $L_{b_0}T_{\mathrm v1}(\tilde aV)$ involve $a''$ and higher; $L_{b_0}\dot
g(a\dot b) = a'L_1\dot g+a''L_2\dot g$, with $\dot b = 0$ unless $\mathrm{Re}\,z_0+1\ge\beta$; and $[L_{b_0},\chi_K]$ is
supported in $\{t_*/4\le r\le t_*/2\}$, away from $K^+$. There are finitely many pairs with real part $<\beta$, so the
process ends; collecting the subtracted coefficients gives (2.4). *Exponents:* the $\rho^{\mu_\rho}$-coefficient of $P$
is that of $\sum_ic^{(i)}_{z_0,k_0}p_i$ less the corrections of the states of lower root removed in Lemma 2.3's
reduction, which lie at those roots plus elements of $\mathcal E_{\mathrm{ind}}$; so $(z_0+\mu_\rho,k_0)$ is
$(z_0+e,k_0)$ for an exponent $e$ of some $p_i$, or of a companion subtracted earlier, plus elements of $\mathcal
E_{\mathrm{ind}}$ (a companion $a^{(j)}\breve h^{(\mu),j}$ has the exponent $z+j$ and the degree $\mu-j$, so the same
sum $z+\mu$); for v1 the exponent of $\tilde a$ is $z_0-1$ and $d_{\mathrm v1} = 0$, $\mu_{\mathrm v1} = -1$. $\square$

## 3. The expansion ([Hin26] Theorem 11.59, Part 4, (11.196), and the $\iota^+$-part of (11.222), at n = 4)

**Theorem 3.1.** In the setting of section 1, for every small $\epsilon>0$,
$$u = \chi_Ku_{\exp}+\tilde u,\qquad u_{\exp} = h^{\le1}_{b_0,\mathrm s1}\big(\dot S_{\mathrm{rem}}\big)+\dot g\big(\dot
b_{\mathrm{rem}}\big)+\sum_{\rho\in\mathcal R'}T_\rho\big(\dot Y_\rho\big),\tag{3.1}$$
with
$$\dot S_{\mathrm{rem}}\in\dot H^{\infty,\alpha-2-\epsilon}_{\mathrm b}([1,\infty];\mathcal S_{1,\mathbb C}),\quad\dot
b_{\mathrm{rem}}\in\dot H^{\infty,\alpha-1-\epsilon}_{\mathrm b}([1,\infty];\mathfrak b_{\mathbb C}),\quad\dot
Y_\rho\in\dot H^{\infty,\mathcal Q(\mathcal E_\sharp-d_\rho,\,w_\rho)}_{\mathrm b}([1,\infty];\mathcal
Y_\rho),\tag{3.2}$$
$w_\rho := 3+\eta_2-2\epsilon-d_\rho$ for every $\rho\in\mathcal R'$ ($d_{\mathrm v1} = 0$), and
$$\tilde u\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal
E_\sharp,3+\eta_2-2\epsilon),\alpha-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}.\tag{3.3}$$
The coefficients are conjugation-symmetric (real $u$), linear and continuous in $F$, with bounds uniform for $(h,\vec
p)$ small. Each term of $\chi_Ku_{\exp}$ has $K^+$-order $\ge\alpha-2-\epsilon$, so (3.1) contains III.I$'''''''''''$
Theorem 4.1's $u = O(t_*^{-\alpha+2+\epsilon})$ in compact sets, and $L_{b_0}(\chi_Ku_{\exp})$ has $K^+$-order
$\alpha-\epsilon$ (the source's Remark 11.60 (1) and (11.232)).

The polyhomogeneous parts of the $\dot Y_\rho$ come from the $\iota^+$-terms of $u$: an $\iota^+$-exponent $\lambda$
gives the coefficient $t_*^{-\lambda+d_\rho}$ (Lemma 2.1 (b), III.G$''$ (4.3)), hence the index set $\mathcal
E_\sharp-d_\rho$; their conormal parts, present only for the rows with $\mu\in(-1,0]$ ($d_\rho = \mu$), come from the
last Taylor level and have order $\ge3+\eta_2-2\epsilon-\mu$; the boosts and the black hole parameters carry only
conormal coefficients, of orders $\alpha-2-\epsilon$ and $\alpha-1-\epsilon$, as in the source. The coefficients of v1
and of the rows with $\mu\le-1$ are finite sums of terms $\chi_+t_*^{-z}(\log t_*)^k$, so they lie in these spaces for
every $w_\rho$; the choice of $w_\rho$ makes the $\iota^+$-order of every $\chi_KT_\rho(\dot Y_\rho)$ at least
$3+\eta_2-2\epsilon$, as in the source's (11.227b).

*Proof.* *Step 0 (the decomposition).* As in III.I$'''''''''''$ Theorem 4.1's proof, $u = u_0-\sum_\nu m_\nu(S_\nu)$,
where $u_0$ is the forward solution of $L_{h,\vec p}u_0 = G(\vec W)\in\mathcal Y^0(\alpha)$ and $S_\nu$ are its
coefficients of III.I$'''''''''''$ Lemma 3.2 (the $C_\nu$ vanish). By that lemma's proof, $u_0 = u_I+u_\iota+v$
(III.I$''''''''''$ Proposition 3.1 for $f' := G(\vec W)-(L_{h,\vec p}-L_{b_0})u_0$, which lies in $\mathcal Y^0(\alpha)$
with $K^+$-order $\alpha-\epsilon$), $L_{b_0}v = f^\flat$, and $v = v_{\mathrm{hi}}+v_{\mathrm{low}}$ with $\hat v$ on
$0<|\sigma|\le c$ the sum of the pieces of III.I$'''''''''''$ Proposition 3.1, in which $S_0 = 0$, $\dot b_0 = 0$ and
$S_1 = 0$ (its Steps 1 and 6). Moreover $L_{b_0}u = f'-\sum_\nu L_{b_0}m_\nu(S_\nu)$ has $K^+$-order $\alpha-\epsilon$:
by the tower relations $L_{b_0}m_\nu$ consists, near $K^+$, of terms with $a_\nu^{(K_\tau+1)}$, $a_\nu^{(K_\tau+2)}$, of
$K^+$-order $\ge\mathrm{Re}\,e_\nu+K_\tau+1$ (III.I$'''''''''$ section 2 and Lemma 2.2, III.G$''$ Lemma 2.6), which is
$>\frac92>\alpha$: for s1, $K_\tau\ge k_{\mathrm s1} = 3$ (III.I$''''''''''$ Lemma 2.1 (c)) and
$\mathrm{Re}\,e_\nu\ge\lambda_\sharp-1>\frac12$; for the other rows the rate is $\ge\lambda_\sharp>\frac32$ and
$K_\tau\ge2$.

*Step 1 (the pieces near $K^+$).* We write each part of $u$, on $\{t_*\ge1\}$, as $\chi_K$ times (polyhomogeneous
coefficients times profiles) plus (conormal towers) plus a term of $K^+$-order $\alpha-\epsilon$ whose order at
$\iota^+$ is $\ge3+\eta_2-2\epsilon$ or which is polyhomogeneous there with exponents in $\mathcal E_\sharp$.

(i) $u_I$, which contains the $\mathscr I^+$-solutions $u'_{\lambda_0}$ of III.I$''''''''''$ Proposition 3.1's Step 2,
vanishes near $K^+$ (III.I$''''''''''$ Proposition 3.1 (a)).

(ii) $u_\iota = \sum_{\lambda_0}\sum_j\big(\chi_Ku^{(j)}_{b_0,0}+\chi_\iota t_*^{-\lambda_0}(\log t_*)^j\tilde
u^{(j)}\big)$; $u^{(j)}_{b_0,0}$ is III.G$''$ (4.3) at $\lambda_0$, a sum of towers with coefficients
$t_*^{-\lambda_0+\mu}(\log t_*)^j$ (and $a_{\mathrm s1}$, $a_{\mathrm v1}$), and $\chi_\iota t_*^{-\lambda_0}\tilde
u^{(j)}$ has $K^+$-order $\mathrm{Re}\,\lambda_0+\ell_K(\lambda_0)-\epsilon = \alpha-\epsilon$ (III.G$''$ Theorem 4.2's
proof, *Near $K^+$*: $t_*^{-\lambda}R^{\ell_K} = t_*^{-\lambda-\ell_K}r^{\ell_K}$).

(iii) $m_\nu(S_\nu) = \chi_KT_\nu(a_\nu S_\nu)$ up to $K^+$-order $\ge\mathrm{Re}\,e_\nu+k_\mu+1>\alpha$
(III.I$'''''''''$ Definition 2.1, III.I$''''''''''$ Lemma 2.1 (c)).

(iv) $v_{\mathrm{hi}}$ has $K^+$- and $\iota^+$-order $N$ (III.I$''$ Lemma 4.1).

(v) The zero-energy pieces $\sigma^j\chi_{\mathrm{zf}}\hat u_j^\pm$, $j\le3$: by Lemma 2.1 (b) with $c =
\sigma^j\mathrm{sgn}(\sigma)^\delta$ (the sign-even and sign-odd parts of $\hat u_j^\pm$) and the single profile $\hat
u_{j,e}$ or $\hat u_{j,o}$; for $\delta = 0$, $y$ is Schwartz at $+\infty$. III.I$'''''''''''$ Lemma 2.1 makes $\hat
u_j$ polyhomogeneous only to a finite order ($\hat u_2$ to $\epsilon_+-\epsilon$, $\hat u_3$ conormal); its
polyhomogeneous part gives $\iota^+$-exponents in $\Lambda$ (Lemma 2.1 (b)), and its conormal part $\iota^+$-order at
least $3+\eta_2-2\epsilon$ ($3+\epsilon_+-\epsilon$ at levels 0-2, $\tau+2$ at level 3).

(vi) The pieces of III.G$''''$ Proposition 4.4 at levels 1 and 2: $\sigma^j\chi_{\mathrm{zf}}|\sigma|^{\alpha_0-2}u_b$
is by III.G$''''$ (4.4) a finite sum of terms $c(\sigma)P(\sigma,x)$ with $c$ homogeneous and $P$ a spectral tower
($G_{\mu,\tau}$, $G_{\mathrm s1}$, $G^{\mathrm{exc}}_{\mathrm s1}$) or a tower whose profiles are multiplied by
$r^\beta$ or $\log r$ (from $l_\beta(\hat r) = (|\sigma|^\beta r^\beta-1)/\beta$), to which Lemma 2.1 (b) applies;
$\chi_{\mathrm{tf}}\rho^{\alpha_0-2}_{\mathrm{tf}}u_{\mathrm{tf}}$ does not vanish near zf: $\chi_{\mathrm{tf}} =
\chi_2(\rho+|\sigma|)$ is 1 at $\mathrm{tf}\cap\mathrm{zf}$ and non-zero at zf over $\{r>2/\rho_0\}$ (III.G$''''$
section 1), $\rho_{\mathrm{tf}} = |\sigma|+\langle x\rangle^{-1}$ (III.H section 1), and $u_{\mathrm{tf}}$ has the
zf-class $((0,0),\ell_{\mathrm{zf}})$ (III.G$''''$ Proposition 4.4). We expand
$\sigma^j\chi_{\mathrm{tf}}\rho^{\alpha_0-2}_{\mathrm{tf}}u_{\mathrm{tf}}$ at zf to the order $\ell_{\mathrm{zf}}+j$,
the zf-exponents being $j$ plus $\mathbb N_0$ (from $\chi_2$ and $\rho_{\mathrm{tf}}$, in $|\sigma|$): its zf-terms
$\sigma^j|\sigma|^kc^\pm_k(x)$ are pieces of type (v) (Lemma 2.1 (b) with $c =
\sigma^j|\sigma|^k\mathrm{sgn}(\sigma)^\delta$ and the single profile $c_{k,e}$ or $c_{k,o}$), and the zf-remainder, of
weight $\ell_{\mathrm{zf}}+j = \alpha-1-\epsilon$ (the level's choice in III.I$'''''''''''$ Proposition 3.1), has
$K^+$-order $\alpha-\epsilon$ (III.A Proposition 4.2 (2)), with $\iota^+$-exponents of the tf-index set plus 1.

(vii) The columns at levels 1-3 with constant data ($\dot b_1^\pm$, $\dot b_j^\pm$, $S_j^\pm$, $j = 2,3$): $\sigma^j\hat
g^{\mathrm{aug}}(\dot b) = i\sigma^{j-1}\Psi\dot g(\dot b)$ and $\sigma^j\hat h^{\mathrm{aug}}(S) =
-\sigma^{j-2}G_2(\sigma)(S)$ are, as in Lemma 2.2's proof, convolutions in $t_*$ of $\mathcal
F^{-1}[\chi\sigma^m\mathrm{sgn}(\sigma)^\delta]$ with $\phi_x$ and $t\phi_x$; Taylor's formula to order $L$ writes them
as finitely many terms $y(t_*)\,r^l\dot g$, $y\,r^lh$, $y\,r^l\breve h$ ($y$ polyhomogeneous, from the moments of
$\phi$) plus a remainder of $K^+$-order $\ge\alpha$. Near $\iota^+$, where $\chi_K = 0$ for $r\ge t_*/2$, the piece
itself is what is recorded: for $r\ge1$, $\Psi = \Phi(\sigma r)$ and $\partial_\sigma\Psi = r\Phi'(\sigma r)$ (III.H
Lemma 2.5 (b)), and $\sigma = \zeta/r$ gives $\mathcal F^{-1}[\chi\sigma^m\mathrm{sgn}(\sigma)^\delta\Phi(\sigma r)] =
r^{-1-m}G(t_*/r)+O(r^{-\infty})$ with $G$ smooth (and likewise with $r\Phi'(\sigma r)$), so each piece is
polyhomogeneous at $\iota^+$ with exponent $m+1$ plus the degree of the state ($\dot g$: 2 or 3; $h$: 3; $\breve h$: 2)
and its expansion's exponents, for instance 3 or 4 at level 1; these lie in $\Lambda$ ($3\in\Lambda$,
$\Lambda+1\subset\Lambda$, $\Lambda+\mathcal E_{\mathrm{ind}}\subset\Lambda$).

(viii) The pieces of III.G$''''$ Proposition 5.1 at level 3: $\sigma^3\chi_{\mathrm{zf}}u_b$ is by III.G$''''$ (5.2) a
sum of spectral towers times conormal scalars $\sigma^3|\sigma|^{\alpha_\tau-3}S(\sigma)$,
$\sigma^3|\sigma|^{\alpha_\tau-2}V(\sigma)$, $\sigma^3|\sigma|^{\alpha_\tau-2-\mu}Y(\sigma)$ of zf-weights
$\alpha_\tau$, $\alpha_\tau+1$, $\alpha_\tau+1-\mu$; Lemma 2.1 (a) gives conormal towers with coefficients of orders
$\alpha_\tau+1$ (boosts, tower $h^{\le3}_{b_0,\mathrm s1}$), $\alpha_\tau+2$ (rotations, tower rate
$\alpha_\tau+3>\alpha$) and $\alpha_\tau+2-\mu$, the last of $K^+$-order $>\alpha$ unless $\mu\in(-1,0]$; their order at
$\iota^+$ is $\alpha_\tau+2\ge\tau_3+2 = 3+\eta_2-2\epsilon$. In the boost tower the terms with $a''$, $a'''$ have
$K^+$-order $\alpha_\tau+3>\alpha$, and it is truncated to $h^{\le1}_{b_0,\mathrm s1}$.
$\sigma^3\chi^\sharp_{\mathrm{tf}}\tilde u$: III.G$''''$ Proposition 5.1 gives $\tilde u$ the zf-class
$((k_0,0),\ell_{\mathrm{zf}})$ with $k_0 = 0$, its proof putting $\chi_{\mathrm{zf}}\chi_{\mathrm{tf}}v_0$ into $\tilde
u$ with $v_0$ stationary and conormal of order $\alpha_\tau-2\in(-1,0)$; so $\sigma^3\chi^\sharp_{\mathrm{tf}}\tilde u$
is $\sigma^3\chi^\sharp_{\mathrm{tf}}\chi_{\mathrm{zf}}\chi_{\mathrm{tf}}v_0^\pm$, expanded at zf as in (vi) into pieces
of type (v) with the single profiles $v_{0,e}$, $v_{0,o}$ (degree $\alpha_\tau-2$; their sign-odd parts reach the
$K^+$-exponent 4), plus a zf-remainder of weight $\ell_3+3 = \alpha-1-\epsilon$, of $K^+$-order $\alpha-\epsilon$ (III.A
Proposition 4.2 (2)).

(ix) The last level: $\sigma^3\hat u_f$ has zf-weight $\ell_3+3$ and tf-weight $\tau+1-\epsilon$, so $K^+$-order
$\alpha-\epsilon$ and $\iota^+$-order $\tau+2-\epsilon>4$ (III.A Proposition 4.2 (2)); the columns give
$\chi_Kh^{\le1}_{b_0,\mathrm s1}(A)+\chi_K\dot g(B)$ with $A\in\dot H^{\infty,\alpha-2-\epsilon}_{\mathrm b}$, $B\in\dot
H^{\infty,\alpha-1-\epsilon}_{\mathrm b}$, up to $K^+$-order $\ell_3+4 = \alpha-\epsilon$ (Lemma 2.2 with $a = \ell_3$).

*Step 2 (assembly).* By Step 1, on $\{t_*\ge1\}$,
$$u = \chi_K\sum_{i\in I}y_ip_i+\chi_KC+w',\tag{3.4}$$
where $C$ consists of the conormal towers of (viii) (the truncated boost tower $h^{\le1}_{b_0,\mathrm s1}(A_5)$,
$A_5\in\dot H^{\infty,\alpha_\tau+1}_{\mathrm b}$, and $T_\rho(Y^c_\rho)$ for the rows with $\mu\in(-1,0]$, $Y^c_\rho$
of order $\ge3+\eta_2-2\epsilon-\mu$) and of (ix) ($h^{\le1}_{b_0,\mathrm s1}(A)+\dot g(B)$), $w'$ has $K^+$-order
$\alpha-\epsilon$, and the $y_ip_i$ are the polyhomogeneous terms of (ii), (iii), (v)-(viii) (with the zf-terms of (vi)
and (viii)). Every exponent $(z,k)$ of $y_i$ satisfies $\mathrm{Re}\,z+d_i\ge\lambda_\sharp$: $z+d_i$ is the leading
$\iota^+$-exponent of the piece (Lemma 2.1 (b); III.G$''$ (4.3) for (ii)), and these lie in $\mathcal E_\sharp$
(III.I$''''''''''$ Lemma 1.2 (c) and Proposition 3.1, III.I$'''''''''''$ Lemma 2.1: all exponents produced are
$\Lambda$-valued with log orders $\le K$). As $u$ (III.I$'''''''''''$ Theorem 4.1) and $\chi_KC$ have $K^+$-order
$\ge\alpha-2-\epsilon$, so has $\chi_K\sum_iy_ip_i$; in $\{r\le R\}$ its lowest term dominates, so the coefficient
section $\sum_ic^{(i)}_{z,k}p_i$ of every exponent with $\mathrm{Re}\,z<\alpha-2-\epsilon$ vanishes, and we drop these
exponents from the $y_i$ (the sum is unchanged).

*Step 3 (formal solutions).* Lemma 2.4 applies to $w := u-\chi_KC$ with $\beta := \alpha-\epsilon$: the hypotheses on
the $y_i$ are those of Step 2; $L_{b_0}u$ has $K^+$-order $\alpha-\epsilon$ (Step 0); and $L_{b_0}(\chi_KC)$ has
$K^+$-order $\alpha-\epsilon$, as by the tower relations it consists of $[L_{b_0},\chi_K]C$ (supported away from $K^+$)
and terms with $A_5''$ (order $\alpha_\tau+3>\alpha$), $(Y^c_\rho)^{(3)}$ (order $>3+\eta_2-\mu+2>\alpha$), $A''$ and
$B'$ (order $\alpha-\epsilon$). It gives (2.4) with $a_{\mathrm b}$ of exponents $\ge\alpha-1-\epsilon$.

*Step 4 (the coefficients).* Put $\dot S_{\mathrm{rem}} := A+A_5+a_{\mathrm s}$, $\dot b_{\mathrm{rem}} := B+a_{\mathrm
b}$, $\dot Y_\rho := a_\rho+Y^c_\rho$ (with $Y^c_\rho := 0$ unless $\mu_\rho\in(-1,0]$). Then $\dot
S_{\mathrm{rem}}\in\dot H^{\infty,\alpha-2-\epsilon}_{\mathrm b}$ ($\alpha_\tau+1\ge2+\eta_2-2\epsilon>\alpha-2$;
$a_{\mathrm s}$ has exponents of real part $\ge\alpha-2-\epsilon$), $\dot b_{\mathrm{rem}}\in\dot
H^{\infty,\alpha-1-\epsilon}_{\mathrm b}$, and $\dot Y_\rho\in\dot H^{\infty,\mathcal Q(\mathcal
E_\sharp-d_\rho,w_\rho)}_{\mathrm b}$: $a_\rho$ is a finite sum of terms $\chi_+t_*^{-z}(\log t_*)^k$; those with
$\mathrm{Re}\,z<w_\rho$ have $(z+d_\rho,k)\in\mathcal E_\sharp$, by Lemma 2.4 (*Exponents*), as the polyhomogeneous
parts of the pieces have their $\iota^+$-exponents in $\mathcal E_\sharp$ (Step 2) and their conormal parts order
$\ge3+\eta_2-2\epsilon$ ((v)), while $\Lambda+\mathcal E_{\mathrm{ind}}\subset\Lambda$ and $K(\lambda+w)\ge
K(\lambda)+l_*$ for $(w,l)\in\mathcal E_{\mathrm{ind}}$ (III.I$''''''''''$ Lemma 1.2 (c)'s proof); those with
$\mathrm{Re}\,z\ge w_\rho$, and $Y^c_\rho$, lie in $t_*^{-w_\rho}H^\infty_{\mathrm b}$. So $\tilde u := u-\chi_Ku_{\exp}
= w''+w'$ has $K^+$-order $\alpha-\epsilon$.

*Step 5 ($\mathscr I^+$ and $\iota^+$).* Near $\mathscr I^+$, $\chi_K = 0$ and $\tilde u = u$, which has the $\mathscr
I^+$-data of III.I$'''''''''''$ (4.2). Near $\iota^+$, $u$ is partially polyhomogeneous with the index set $\mathcal
E_\sharp$ up to the order $3+\eta_2-2\epsilon$: $u_I$, $u_\iota$ by III.I$''''''''''$ Proposition 3.1 (a)-(b) (index
sets $\Lambda$-valued below $3+\epsilon_+$, log orders $\le K$, the term $\chi_\iota t_*^{-\lambda_0}(\log t_*)^j\tilde
u^{(j)}$ being the $\iota^+$-term $(\lambda_0,j)$ itself, with $\mathscr I^+$-weight $\ell_I$ on $\iota^+$, III.G$''$
Corollary 4.3); the $m_\nu$, with exponents in $\mathcal E_{\mathrm{par}}\subset\mathcal E_\sharp$; the pieces
(v)-(vii), polyhomogeneous with exponents the tf-exponents plus 1 (Lemma 2.1 (b); (vii) as stated there) up to the order
$3+\eta_2-2\epsilon$, in $\mathcal E_\sharp$; the pieces (viii)-(ix), of order $\ge3+\eta_2-2\epsilon$ (Lemma 2.1 (a),
Lemma 2.2, and the tf-weights $\alpha_\tau+1$, $\tau+1-\epsilon$); and $v_{\mathrm{hi}}$. The same holds for
$\chi_Ku_{\exp}$: its polyhomogeneous coefficients give the exponents $z+d_\rho\in\mathcal E_\sharp$ plus those of the
profiles' expansions ($\Lambda$ is closed under $+\mathcal E_{\mathrm{ind}}$, and $K(\lambda+w)\ge K(\lambda)+l_*$), and
its conormal coefficients have order $\ge3+\eta_2-2\epsilon$ at $\iota^+$ ($\alpha_\tau+2$ for (viii);
$\ge\alpha+1-\epsilon$ for $h^{\le1}_{b_0,\mathrm s1}(\dot S_{\mathrm{rem}})$ and $\dot g(\dot b_{\mathrm{rem}})$, as
$h_{b_0,\mathrm s1}\in\mathcal A^3$, $\breve h^1_{b_0,\mathrm s1},\dot g\in\mathcal A^2$). So $\tilde u$ satisfies (3.3).

*Step 6 (the rest).* Every map used is linear and bounded, uniformly for $(h,\vec p)$ small (III.I$'''''''''''$ Lemma
3.2 and Theorem 4.1, Lemmas 2.1-2.4); reality: $u$ is real and the towers are real ($\overline{T_\rho(Y)} = T_\rho(\bar
Y)$), so replacing every coefficient and $\tilde u$ by their real parts keeps (3.1)-(3.3), $\mathcal E_\sharp$ being
closed under conjugation. $L_{b_0}(\chi_Ku_{\exp})$ has $K^+$-order $\alpha-\epsilon$ by the tower relations, as in
Step 3. $\square$

## 4. Findings, labels and sources

(I$''''''''''''$1) *The spacetime phase needs no Part 4 work at n = 4.* The $\iota^+$-terms of $u$-exponent
$\lambda_0<2$ are grafted with $\ell_K = \alpha-\mathrm{Re}\,\lambda_0<3 = \ell^{\max}_K$, and the graft's remainder has
$K^+$-order $\mathrm{Re}\,\lambda_0+\ell_K-\epsilon$; III.G$''$ Theorem 4.2 states the weaker $K^+$-weight $\ell_K$ for
$u$ in its last sentence, while its proof (*Near $K^+$*) gives $\lambda_0+\ell_K$, which is what is used here.

(I$''''''''''''$2) *Why the towers.* The source identifies the $K^+$-terms piece by piece and argues that sign-dependent
singular terms "cannot be cancelled" by later ones. At $n = 4$ the conormal coefficients of the last Taylor level have
$K^-$-tails of order $\alpha-2$, which could mask such terms of order 3 and 4; Lemma 2.4 instead uses the equation:
below the order $\alpha$ every coefficient section is a stationary solution of moderate growth (Lemma 2.3), so the
polyhomogeneous part of $u$ at $K^+$ is a sum of towers whatever the individual pieces are.

(I$''''''''''''$3) *No growing boost state and no early $\dot g$.* No element of $\ker L_0$ of moderate growth has an
s1-component at $\rho^{-1}$, and $L_1\dot g(\dot b)$ is not in the range of $L_0$ on such sections unless $\dot b = 0$
(Lemma 2.3 (b)); both follow from the invertibility of $\tilde L_{b_0}(0)$ with III.H (2.2). Hence the black hole
parameters enter $u_{\exp}$ only from the order $\alpha-1-\epsilon$ on, as the source's $\dot b_{\mathrm{rem}}\in\dot
H^{\infty,3+\epsilon_K}_{\mathrm b}$.

(I$''''''''''''$4) *The $\iota^+$-order.* The $\iota^+$-index set is recorded to $3+\eta_2-2\epsilon$, with
$\eta_2<\epsilon_+$ as close to $\epsilon_+$ as desired, not to the source's $3+\epsilon_+$: the level-3 sources are
treated conormally from the tf-weight $1+\eta_2-2\epsilon$ on.

*Labels.* Lemmas 2.1-2.4 are new at $n = 4$; Theorem 3.1 is the source's Part 4 ((11.196) with Remark 11.60 (1)) and the
$\iota^+$-part of (11.222) at $n = 4$.

*Sources.* [Hin26] pp. 278-292 (Theorem 11.59, Remarks 11.60-11.62, the proof's Part 4), read at source. Inputs: II.G$'$
(2.26a); III.A Proposition 4.2; III.F$'$ section 2, Proposition 2.3; III.F$'''$ Proposition 4.1, Corollary 4.2;
III.G$''$ section 1, Table 1.1, Lemma 1.2, Definition 2.5, (2.2), Lemma 2.4, Lemma 2.6, Theorem 3.1's proof, Theorem
4.2, Corollary 4.3; III.G$''''$ (4.4), (5.2), Propositions 4.4, 5.1; III.H (1.2), (2.2), (2.6), Lemmas 2.3, 2.5,
Proposition 3.2; III.I$''$ Lemma 4.1; III.I$''''''$ section 1; III.I$'''''''''$ section 2, Lemma 2.2, Definition 2.1;
III.I$''''''''''$ Definition 1.1, Lemmas 1.2, 2.1, Proposition 3.1; III.I$'''''''''''$ Lemma 2.1, Proposition 3.1, Lemma
3.2, Theorem 4.1.
