# Part III.D‴. Generalized zero energy states of the gauge potential operator, at n = 4 ([Hin26] section 6.5.2)

*Status.* Written (D224). This part proves, at spatial dimension $n = 4$ and for the Myers-Perry metrics $g_b$, $b$ near
$b_0 = (\mu_0,0)$, what [Hin26] section 6.5.2 establishes (pp. 128-134): the generalized zero energy states of the gauge
potential wave operator -- polynomials in $t_*$ in its kernel -- built on the time translation, the translations and
boosts, the rotations, and on the indicial roots of the zero energy operator below $-1$, with their symmetric gradients
(Proposition 6.18 and Remark 6.19). Parts III.D$'$ and III.D$''$ are cited as III.D$'$, III.D$''$, the others as there.
Computations cited as *computed* are exact (sympy) and rerun by the instruments named (D224).

*What n = 4 changes.* The zero energy operator of $g_b$ differs from Minkowski's by $\rho^4\mathrm{Diff}^2_{\mathrm b}$
(III.D$''$ Lemma 2.1), one power more than in the source, so the correction to the leading term of every stationary
state lies two orders below it instead of one. The indicial roots of the classes move
($\lambda^\Upsilon_{\mathrm s0,2}$, $\lambda^\Upsilon_{\mathrm sl,l+1}$, $\lambda^\Upsilon_{\mathrm sl,l+2}$ of III.D
Lemma 4.1), and the resonance-free ranges are those of section 1 below. The leading terms are computed exactly on
Minkowski space. Part (1) carries no logarithm. Findings are in section 4.

## 1. Setting

$E_\Upsilon$, $b$, $\Box^\Upsilon_b$, $P_b := \widehat{\Box^\Upsilon_b}(0)$, the model $\bar g$, $\bar t = t_*+|x|$,
$\bar\Box^\Upsilon$, the unweighted b-density and the symmetric 1-forms $\omega^{(0)}_{b,\mathrm s0}$,
$\omega^{(0)}_{b,\mathrm s1}(S)$, $\breve\omega^{(0),1}_{b,\mathrm s1}(S)$, $\omega^{(-1)}_{b,\mathrm v1}(V)$ are those
of III.D$''$, with $z = 4e_\Upsilon\gamma_\Upsilon^2\in(0,\frac12]$. Near $\partial X$ write

$$\Box^\Upsilon_b = A_0+A_1\partial_{t_*}+A_2\partial_{t_*}^2,\qquad A_0 = P_b\in\rho^2\mathrm{Diff}^2_{\mathrm b},
\quad A_1\in\rho\,\mathrm{Diff}^1_{\mathrm b},\quad A_2 = -g_b^{00}\in\rho^2C^\infty,\tag{1.1}$$

and $\bar A_0,\bar A_1$ for the model ($\bar A_2 = 0$). By III.D Lemma 2.1 and III.D$''$ Lemma 2.1, $A_0-\bar
A_0\in\rho^4\mathrm{Diff}^2_{\mathrm b}$, $A_1-\bar A_1 = Q_b\in\rho^3\mathrm{Diff}^1_{\mathrm b}$, and
$A_0-A_0^{(\mu)}\in\rho^5\mathrm{Diff}^2_{\mathrm b}$, $A_1-A_1^{(\mu)}\in\rho^4\mathrm{Diff}^1_{\mathrm b}$ against the
non-rotating $g_\mu$. Also

$$\delta^*_{g_b} = \widehat{\delta^*_{g_b}}(0)+dt_*\otimes_s(\cdot),
\qquad\widehat{\delta^*_{g_b}}(0)\in\rho\,\mathrm{Diff}^1_{\mathrm b}.\tag{1.2}$$

*Generalized states.* For stationary 1-forms $\breve\omega^0 := \omega$, $\breve\omega^1,\dots,\breve\omega^K$ and $k\le
K$ put $\omega^{\le k} := \sum_{i=0}^k\frac{k!}{(k-i)!}t_*^{k-i}\breve\omega^i$ ([Hin26] (6.36a)). The coefficient of
$t_*^{k-j}$ in $\Box^\Upsilon_b\omega^{\le k}$ is
$\frac{k!}{(k-j)!}(A_0\breve\omega^j+A_1\breve\omega^{j-1}+A_2\breve\omega^{j-2})$ ($\breve\omega^{-1} =
\breve\omega^{-2} := 0$), so

$$\omega^{\le k}\in\ker\Box^\Upsilon_b\ \ (k\le K)\iff A_0\breve\omega^j = -A_1\breve\omega^{j-1}-A_2\breve\omega^{j-2}
\quad(0\le j\le K).\tag{1.3}$$

(The source's proof prints $A_0\breve\omega^{l-2}$ for $A_2\breve\omega^{l-2}$ in this recursion; finding (D$'''$1).) By
(1.2), $\delta^*_{g_b}\omega^{\le k} = \sum_{j=0}^k\frac{k!}{(k-j)!}t_*^{k-j}\breve h^j$ with

$$\breve h^j := \widehat{\delta^*_{g_b}}(0)\breve\omega^j+dt_*\otimes_s\breve\omega^{j-1},\tag{1.4}$$

so its constant coefficient is $k!\,\breve h^k$; and $\delta^*_{g_b}\omega^{\le k}$ lies in $\ker
D_{g_b}\mathrm{Ric}\cap\ker\delta_{g_b,E_\Upsilon}G_{g_b}$ whenever $\omega^{\le k}\in\ker\Box^\Upsilon_b$ (III.D$''$
(F2)).

*Exponents.* Let $\mathcal M$ be the finite set of real numbers in $[-10,10]$ of the form $\mathrm{Re}\,\lambda+j$,
$\lambda$ an indicial root of $P_b$ (III.D Lemma 4.1; they do not depend on $b$, and all are real) and $j\in\mathbb Z$,
and fix $\epsilon_{\mathrm{ind}}>0$ less than half the least distance between distinct points of $\mathcal M$ (this
implies the condition of III.D$''$ section 1). $\mathcal E_{\mathrm{ind}}$ denotes an index set with
$\min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}\ge\epsilon_{\mathrm{ind}}$, changing from line to line. Every exponent below
lies in $\mathcal M$.

*The class roots and the ranges* (computed; exact). For $0<z<4$:
(R1) $-1,-2,-3,-4$ are not s0 roots of $P_b$ (`genstates5.py` H1; $-2$ is one at $z = 4$).
(R2) $-2,-3,-4$ are not s1 roots for $0<z<\frac{20}3$ ($-2$ is one at $z = 0$; `genstates5.py` H2).
(R3) $-2,-3,-4$ are not v1 roots, for every $z$ (`genstates5.py` H3).
(R4) The class roots: $\mu_{\mathrm s0} := 1-\lambda^\Upsilon_{\mathrm s0,2}\in(-2,-1)$; for $l = 1,2,3$, $\mu_{l,0} :=
1-\lambda^\Upsilon_{\mathrm sl,l+1}\in(-l-1,-l)$ and $\mu_{l,1} := 1-\lambda^\Upsilon_{\mathrm sl,l+2}<-l-1$; the sl
roots $-l+1$, $2\le l\le5$; the vl roots $-l$, $2\le l\le4$. With the degree ranges $K = 2$ (s0 class and sl classes
$\mu_{l,j}$), $K = 5-l$ (sl roots $-l+1$) and $K = 4-l$ (vl roots $-l$): for each class root $\mu$ of type $\tau$,
neither $\mu+2$ nor $\mu-k$, $1\le k\le K$, is a type-$\tau$ root, and $\mu$ is a simple type-$\tau$ root
(`puregauge5.py` J2, J4).
(R5) $\widehat{\bar\delta^*}(0)$'s indicial family $N(\widehat{\bar\delta^*}(0),\lambda)$ is injective on each type
except at $\lambda = 0$ (s0, s1) and $\lambda = -1$ (v1) (III.A$'$ Lemma 2.4; `puregauge5.py` J3 at the class roots).

## 2. Solving with a prescribed leading term

**Lemma 2.1.** Let $m\in\mathcal M$, $m\le2$, and let $f$ be smooth on $X$ with $\rho^{-2}f\in\mathcal A^{\mathcal F}$
near $\partial X$, where $\mathcal F\subset\{(m,0)\}\cup\{\mathrm{Re}\ge m+\epsilon_{\mathrm{ind}}\}$, and suppose that
the $\rho^m$-coefficient $f_m$ of $\rho^{-2}f$ has components only of types $\tau$ for which $m$ is not a type-$\tau$
root. Then there is $u\in\mathcal A^{(m,0)\cup(m+\mathcal E_{\mathrm{ind}})}$, smooth on $X$, with $P_bu = f$ and
$\rho^m$-coefficient $u_m = N(\rho^{-2}P_b,m)^{-1}f_m$, of the types of $f_m$. If $f$ depends smoothly on $b$ (in the
topology of these spaces), $u$ can be chosen to.

*Proof.* Near $\partial X$, $A := \rho^{-2}P_b$ is an elliptic b-operator whose normal operator is the model's (III.D
Lemma 2.1 (3)) and so commutes with the rotations; its indicial family $N(A,\lambda)$ preserves the types, and on type
$\tau$ it is invertible exactly off the type-$\tau$ roots. So $w := N(A,m)^{-1}f_m$ is defined, smooth on $\mathbb S^3$,
of the types of $f_m$. With $\chi_\partial$ the cut-off of I.C, $u_0 := \chi_\partial\rho^mw$ has $P_bu_0 =
\chi_\partial\rho^{m+2}f_m+\rho^2(A-N(A))(\chi_\partial\rho^mw)+(\text{smooth, compactly supported})$, and
$A-N(A)\in\rho\,\mathrm{Diff}^2_{\mathrm b}$, so $f_1 := f-P_bu_0$ has $\rho^{-2}f_1\in\mathcal A^{\mathcal F_1}$ with
$\mathcal F_1\subset\{\mathrm{Re}\ge m+\epsilon_{\mathrm{ind}}\}$. III.A Lemma 1.5 (formal solutions; on the bundle, as
III.D$'$ (D$'$5) says of Lemma 1.4) with $\beta = 3$ gives $u_1\in\mathcal A^{\mathcal E_1}$ near $\partial X$,
$\mathcal E_1\subset\{\mathrm{Re}\ge m+\epsilon_{\mathrm{ind}}\}$ (its exponents are those of $\mathcal F_1$ plus
$\mathbb N_0$, with logarithms where they meet roots), such that $f_2 := f_1-P_b(\chi_\partial u_1)$ is smooth on $\bar
X$ with $\rho^{-2}f_2\in\mathcal A^{\mathcal G}$, $\mathcal G\subset\{\mathrm{Re}\ge3\}$. Finally $u_2 := P_b^{-1}f_2$
(III.D$'$ Lemma 5.1): $u_2\in\bigcap_s\bar H^{s,\alpha}_{\mathrm b}$ for every $\alpha<\lambda^\Upsilon_{\mathrm s1,2}$,
and III.A Lemma 1.4 with $\alpha$ just below $\lambda^\Upsilon_{\mathrm s1,2}$ (no root in between) gives
$u_2\in\mathcal A^{\mathcal E_2}$ with $\mathcal E_2\subset\{\mathrm{Re}\ge\lambda^\Upsilon_{\mathrm
s1,2}\}\subset\{\mathrm{Re}\ge m+\epsilon_{\mathrm{ind}}\}$, as $m\le2$ and $\lambda^\Upsilon_{\mathrm
s1,2}-2>2\epsilon_{\mathrm{ind}}$. Then $u := u_0+\chi_\partial u_1+u_2$. Smoothness in $b$: $w$ depends smoothly on $b$
(the normal operator does not depend on $b$, and $f_m$ does smoothly), Lemma 1.5 states smooth dependence for a smoothly
varying $A$, and III.D$''$ Lemma 2.2 covers $u_2$. $\square$

When the leading term of $f$ is that of a model source -- $f = \bar f+f'$ with $\rho^{-2}\bar f\in\rho^m C^\infty$ near
$\partial X$ the source of a model equation $\bar A_0\bar u = \bar f$ solved by a homogeneous $\bar u = \rho^m\bar w$,
and $f'$ two orders lower -- the leading term of $u$ is $\bar u$: indeed $f_m = \bar f_m$, and $N(A,m) = N(\rho^{-2}\bar
A_0,m)$, so $u_m = \bar w$.

## 3. The states ([Hin26] Proposition 6.18 at n = 4)

**Proposition 3.1.** Assume (Dyn), and let $E_\Upsilon$ and $b$ be as in section 1. All 1-forms below are stationary,
smooth on $X$, smooth in $b$, and linear in $S\in\mathcal S_l$, $V\in\mathcal V_l$; every $\omega^{\le k}$ lies in
$\ker\Box^\Upsilon_b$, and every symmetric gradient $\delta^*_{g_b}\omega^{\le k}$ in
$\ker D_{g_b}\mathrm{Ric}\cap\ker\delta_{g_b,E_\Upsilon}G_{g_b}$ (section 1).

(1) (*The time translation; the s0 root 0 of the linearised operator.*) Let $\bar W := |x|(-d\bar t+\beta_e\,d|x|)$,
$\beta_e := \frac{2-e_\Upsilon}{4e_\Upsilon}$. There are $\breve\omega^{(0),1}_{b,\mathrm s0}-\chi_\partial\bar
W\in\mathcal A^{(1,0)\cup(1+\mathcal E_{\mathrm{ind}})}$ and
$\breve\omega^{(0),k}_{b,\mathrm s0}\in\mathcal A^{(-k,0)\cup(-k+\mathcal E_{\mathrm{ind}})}$, $k = 2,3,4$, with scalar
type 0 leading terms, such that, with $\omega^{(0)}_{b,\mathrm s0}$ as the zeroth term,
$\omega^{(0),\le k}_{b,\mathrm s0}\in\ker\Box^\Upsilon_b$ for $k\le4$. The stationary tensor

$$h^{(0)}_{b,\mathrm s0} :
= \delta^*_{g_b}\omega^{(0),\le1}_{b,\mathrm s0}\in\mathcal A^{(0,0)\cup(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}
\tag{3.1}$$

has the leading term $\bar h^{(0)}_{\mathrm s0} := dt_*\otimes_s\bar\omega^{(0)}_{\mathrm
s0}+\widehat{\bar\delta^*}(0)\bar W\ne0$, homogeneous of degree 0 and of scalar type 0. For $k = 0,\dots,3$, $h^{(0),\le
k}_{b,\mathrm s0} := (k+1)^{-1}\delta^*_{g_b}\omega^{(0),\le k+1}_{b,\mathrm s0} = t_*^kh^{(0)}_{b,\mathrm
s0}+\sum_{i=1}^k\frac{k!}{(k-i)!}t_*^{k-i}\breve h^{(0),i}_{b,\mathrm s0}$ with

$$\breve h^{(0),i}_{b,\mathrm s0} :
= \widehat{\delta^*_{g_b}}(0)\breve\omega^{(0),i+1}_{b,\mathrm s0}+dt_*\otimes_s\breve\omega^{(0),i}_{b,\mathrm s0}\in
\mathcal A^{(-i,0)\cup(-i+\mathcal E_{\mathrm{ind}})}.\tag{3.2}$$

(2) (*The boosts to higher order; the s1 root $-1$.*) There are $\breve\omega^{(0),k}_{b,\mathrm s1}(S)\in\mathcal
A^{(-k,0)\cup(-k+\mathcal E_{\mathrm{ind}})}$, $k = 2,3,4$, with scalar type 1 leading terms, continuing
$\omega^{(0)}_{b,\mathrm s1}(S)$, $\breve\omega^{(0),1}_{b,\mathrm s1}(S)$ of III.D$''$, such that $\omega^{(0),\le
k}_{b,\mathrm s1}(S)\in\ker\Box^\Upsilon_b$ for $k\le4$; with (1.4), the constant coefficient of $h^{\le k}_{b,\mathrm
s1}(S) := \delta^*_{g_b}\omega^{(0),\le k}_{b,\mathrm s1}(S)$ is $k!\,\breve h^k_{b,\mathrm s1}(S)$, $\breve
h^k_{b,\mathrm s1}(S)\in\mathcal A^{(-k+1,0)\cup(-k+1+\mathcal E_{\mathrm{ind}})}$ ($k = 2,3,4$), and the leading term
$\bar h^2_{\mathrm s1}(S) := dt_*\otimes_s\breve{\bar\omega}^1_{\mathrm
s1}(S)+\widehat{\bar\delta^*}(0)\breve{\bar\omega}^2_{\mathrm s1}(S)$ of $\breve h^2_{b,\mathrm s1}(S)$, homogeneous of
degree $-1$, of scalar type 1, is nonzero for $S\ne0$; here $\breve{\bar\omega}^2_{\mathrm s1}(S)$ is the leading term
of $\breve\omega^{(0),2}_{b,\mathrm s1}(S)$, the model solution of $\bar A_0\breve{\bar\omega}^2 = -\bar
A_1\breve{\bar\omega}^1_{\mathrm s1}$.

(3) (*The rotations to higher order; the v1 root $-1$.*) There are $\breve\omega^{(-1),k}_{b,\mathrm v1}(V)\in\mathcal
A^{(-k-1,0)\cup(-k-1+\mathcal E_{\mathrm{ind}})}$, $k = 1,2,3$, with vector type 1 leading terms, the first being
$(1+\frac25\gamma_\Upsilon)|x|V$, such that $\omega^{(-1),\le k}_{b,\mathrm v1}(V)\in\ker\Box^\Upsilon_b$ for $k\le3$;
the constant coefficient of $h^{\le k}_{b,\mathrm v1}(V) := \delta^*_{g_b}\omega^{(-1),\le k}_{b,\mathrm v1}(V)$ is
$k!\,\breve h^k_{b,\mathrm v1}(V)$, $\breve h^k_{b,\mathrm v1}(V)\in\mathcal A^{(-k,0)\cup(-k+\mathcal
E_{\mathrm{ind}})}$, and the leading term of $\breve h^1_{b,\mathrm v1}(V)$ is, in the splitting of III.A$'$ section 2
(the source's (2.37b)),

$$\bar h^1_{\mathrm v1}(V) = \tfrac14\big(0,0,(1+\tfrac25\gamma_\Upsilon)V,0,(1-\tfrac25\gamma_\Upsilon)V,
0\big).\tag{3.3}$$

If $R_V$ is Killing for $g_b$ (at $A = 0$, every $V$), then $h^{\le1}_{b,\mathrm v1}(V) = \breve h^1_{b,\mathrm v1}(V)$
is stationary (Remark 6.19).

(4)-(7) (*The classes without symmetry.*) Let $\mu$ be a class root of (R4), of type $\tau\in\{\mathrm s0,\mathrm
sl,\mathrm vl\}$, $K$ its range, and $\bar\omega$ a nonzero indicial solution $\rho^\mu\bar w$ of the model of type
$\tau$ (given by $S\in\mathcal S_l$ or $V\in\mathcal V_l$). There are $\omega^{(\mu)}_b\in\mathcal
A^{(\mu,0)\cup(\mu+\mathcal E_{\mathrm{ind}})}$ with leading term $\bar\omega$ and
$\omega^{(\mu)}_b-\chi_\partial\bar\omega\in\mathcal A^{(\mu+2,0)\cup(\mu+2+\mathcal E_{\mathrm{ind}})}$,
$P_b\omega^{(\mu)}_b = 0$, and $\breve\omega^{(\mu),k}_b\in\mathcal A^{(\mu-k,0)\cup(\mu-k+\mathcal E_{\mathrm{ind}})}$,
$1\le k\le K$, with type-$\tau$ leading terms, such that $\omega^{(\mu),\le k}_b\in\ker\Box^\Upsilon_b$ for $k\le K$.
The symmetric gradient $h^{(\mu+1)}_b := \delta^*_{g_b}\omega^{(\mu)}_b\in\mathcal A^{(\mu+1,0)\cup(\mu+1+\mathcal
E_{\mathrm{ind}})}$ has the nonzero leading term $\widehat{\bar\delta^*}(0)\bar\omega$, of type $\tau$, and the constant
coefficient of $\delta^*_{g_b}\omega^{(\mu),\le k}_b$ is $k!\,\breve h^{(\mu),k}_b$, $\breve h^{(\mu),k}_b\in\mathcal
A^{(\mu+1-k,0)\cup(\mu+1-k+\mathcal E_{\mathrm{ind}})}$.

*Proof.* Each step solves an equation $A_0\breve\omega = f$ by Lemma 2.1; we name its $m$, the type of the leading
coefficient of $f$ and the root fact that applies, and identify the leading term by the remark after Lemma 2.1. *Types.*
At $b = (\mu,0)$ the operators are invariant under the rotations of $x$ (III.D$''$ section 1, with $c_\Upsilon$,
$c_{\Upsilon,H}$ radial), so every construction from $S\in\mathcal S_l$ (or $V\in\mathcal V_l$) stays in the
corresponding isotypic component, the type of the class (III.D$''$, proof of Proposition 3.1 (2)); for general $b$,
$A_i-A_i^{(\mu)}$ is one order lower than $A_i-\bar A_i$ (section 1), so leading coefficients are unchanged and keep
their types. *Model solutions.* The model leading terms named below solve the model equations exactly: computed on $4+1$
Minkowski space with $E_\Upsilon$ at the trace weight $\frac23$, by `genstates5.py` H1-H3 (the polynomials
$t_*\bar\omega_{\mathrm s0}+\bar W$, $t_*^2\bar\omega_{\mathrm s1}+2t_*\bar B+2\breve{\bar\omega}^2_{\mathrm s1}$,
$t_*V+(1+\frac25\gamma_\Upsilon)|x|V$ lie in $\ker\bar\Box^\Upsilon$) and `puregauge5.py` J5 (the classes, every degree
up to $K$).

*(1).* $\omega_{\mathrm s0} := \omega^{(0)}_{b,\mathrm s0}$ is Killing, so $A_0\omega_{\mathrm s0} = 0$ and
$A_1\omega_{\mathrm s0} = \Box^\Upsilon_b(t_*\omega_{\mathrm s0}) =
2\delta_{g_b,E_\Upsilon}G_{g_b}(dt_*\otimes_s\omega_{\mathrm s0})\in\rho C^\infty$. The model has $\bar A_0\bar W =
-\bar A_1\bar\omega_{\mathrm s0}$ (H1). So $\breve\omega^1 := \chi_\partial\bar W+\breve\omega'$ with $A_0\breve\omega'
= -(A_1\omega_{\mathrm s0}-\bar A_1\bar\omega_{\mathrm s0})-(A_0-\bar A_0)\bar W+(\text{compactly supported})$. Here
$A_1\omega_{\mathrm s0}-\bar A_1\bar\omega_{\mathrm s0} = Q_b\omega_{\mathrm s0}+\bar A_1(\omega_{\mathrm
s0}-\bar\omega_{\mathrm s0})\in\rho^3C^\infty$ (III.D$''$ (3.2)) and $(A_0-\bar A_0)\bar
W\in\rho^4\mathrm{Diff}^2_{\mathrm b}(\rho^{-1}C^\infty)\subset\rho^3C^\infty$, so Lemma 2.1 with $m = 1$ (no root)
gives $\breve\omega'\in\mathcal A^{(1,0)\cup(1+\mathcal E_{\mathrm{ind}})}$. (On Tangherlini the source
$\Box^\Upsilon(t_*\omega_{\mathrm s0})$ has its $\rho^1$ term equal to the model's and no $\rho^2$ term: computed, H1.)
Then $h^{(0)}_{b,\mathrm s0} = dt_*\otimes_s\omega_{\mathrm s0}+\widehat{\delta^*_{g_b}}(0)\breve\omega^1$, and
$h^{(0)}_{b,\mathrm s0}-\bar h^{(0)}_{\mathrm s0} = dt_*\otimes_s(\omega_{\mathrm s0}-\bar\omega_{\mathrm
s0})+(\widehat{\delta^*_{g_b}}(0)-\widehat{\bar\delta^*}(0))\bar
W+\widehat{\delta^*_{g_b}}(0)\breve\omega'\in\rho^2C^\infty+\rho^3\mathrm{Diff}^0_{\mathrm
b}(\rho^{-1}C^\infty)+\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}$, which is (3.1). $\bar h^{(0)}_{\mathrm s0}$
is stationary, homogeneous of degree 0 and nonzero, and lies in the kernels of $D_{\bar g}\mathrm{Ric}$ and
$\delta_{\bar g,\bar E}\bar G$ (computed, H1). For $k = 2,3,4$, (1.3) asks $A_0\breve\omega^k =
-A_1\breve\omega^{k-1}-A_2\breve\omega^{k-2}$; inductively the right side is in $\rho\,\mathrm{Diff}^1_{\mathrm
b}\mathcal A^{(-k+1,0)\cup(-k+1+\mathcal E_{\mathrm{ind}})}+\rho^2\mathcal A^{(-k+2,0)\cup\cdots}$, so $\rho^{-2}$ of it
has $m = -k$, its leading coefficient that of $-\bar A_1\breve{\bar\omega}^{k-1}$, of type s0, and $-k$ is no s0 root
(R1); Lemma 2.1 gives $\breve\omega^k\in\mathcal A^{(-k,0)\cup(-k+\mathcal E_{\mathrm{ind}})}$. The formula for
$h^{(0),\le k}$: by (1.4) with $\breve h'^j :=
\widehat{\delta^*_{g_b}}(0)\breve\omega^j+dt_*\otimes_s\breve\omega^{j-1}$, $\breve h'^0 = 0$ and $\breve h'^1 =
h^{(0)}_{b,\mathrm s0}$, $\delta^*_{g_b}\omega^{\le k+1} = \sum_{i=0}^k\frac{(k+1)!}{(k-i)!}t_*^{k-i}\breve h'^{i+1} =
(k+1)\sum_{i=0}^k\frac{k!}{(k-i)!}t_*^{k-i}\breve h'^{i+1}$, and $\breve h^{(0),i}_{b,\mathrm s0} = \breve h'^{i+1}$;
the orders follow from (1.2).

*(2).* Inductively, for $k = 2,3,4$, the right side of (1.3) is $-A_1\breve\omega^{k-1}-A_2\breve\omega^{k-2}$ with
$\breve\omega^1 = \breve\omega^{(0),1}_{b,\mathrm s1}\in\mathcal A^{(-1,0)\cup(1,0)\cup(1+\mathcal E_{\mathrm{ind}})}$
(III.D$''$ (3.2)); $\rho^{-2}$ of it has $m = -k$ and leading coefficient that of $-\bar A_1\breve{\bar\omega}^{k-1}$,
of scalar type 1, and $-k$ is no s1 root (R2). Lemma 2.1 gives $\breve\omega^k$, with leading term the model's
$\breve{\bar\omega}^k_{\mathrm s1}$. By (1.4), $\breve h^k =
\widehat{\delta^*_{g_b}}(0)\breve\omega^k+dt_*\otimes_s\breve\omega^{k-1}\in\mathcal A^{(-k+1,0)\cup\cdots}$. Its
$\rho^{-1}$ term at $k = 2$ is $\bar h^2_{\mathrm s1}(S)$, which is the symmetric gradient
$\bar\delta^*(t_*^2\bar\omega_{\mathrm s1}+2t_*\breve{\bar\omega}^1_{\mathrm s1}+2\breve{\bar\omega}^2_{\mathrm s1})$
halved, stationary because $t_*\bar\omega_{\mathrm s1}+\breve{\bar\omega}^1_{\mathrm s1}$ is a boost, and nonzero for
$S\ne0$ (computed, H2: the model state of degree 2 exists and its gradient is a nonzero stationary tensor of degree $-1$
in both kernels).

*(3).* For $k = 1$: $\omega_{\mathrm v1} := \omega^{(-1)}_{b,\mathrm v1}(V) = V+\mathcal A^{(2,0)\cup\cdots}$, and
$-A_1\omega_{\mathrm v1}$ has $\rho^{-2}$ of it with $m = -2$ and leading coefficient that of $-\bar A_1V$, of vector
type 1; $-2$ is no v1 root (R3), so Lemma 2.1 gives $\breve\omega^1$ with leading term the model's,
$(1+\frac25\gamma_\Upsilon)|x|V$ (H3: $t_*V+\kappa|x|V\in\ker\bar\Box^\Upsilon$ exactly for $\kappa =
1+\frac25\gamma_\Upsilon$). $k = 2,3$ as in (2), with $m = -k-1$ and (R3). $\breve h^1 =
\widehat{\delta^*_{g_b}}(0)\breve\omega^1+dt_*\otimes_s\omega_{\mathrm v1}$ has the leading term
$\widehat{\bar\delta^*}(0)((1+\frac25\gamma_\Upsilon)|x|V)+dt_*\otimes_sV$, which is (3.3) (computed, H3). If $R_V$ is
Killing for $g_b$, $\omega_{\mathrm v1} = g_b(R_V,\cdot)$ (III.D$''$ Proposition 3.1 (3)), so
$\delta^*_{g_b}\omega_{\mathrm v1} = 0$ and $h^{\le1}_{b,\mathrm v1} = \breve h^1_{b,\mathrm v1}$.

*(4)-(7).* $P_b(\chi_\partial\bar\omega) = \chi_\partial(A_0-\bar A_0)\bar\omega+(\text{compactly supported})$, and
$(A_0-\bar A_0)\bar\omega\in\rho^4\mathrm{Diff}^2_{\mathrm b}(\rho^\mu C^\infty)\subset\rho^{\mu+4}C^\infty$, whose
leading coefficient comes from $g_\mu-\bar g$ (the rotation enters one order lower) and so is of type $\tau$; Lemma 2.1
with $m = \mu+2\le2$ (no type-$\tau$ root, (R4)) gives $\omega'$ with $P_b\omega' = -P_b(\chi_\partial\bar\omega)$, and
$\omega^{(\mu)}_b := \chi_\partial\bar\omega+\omega'$. Its symmetric gradient:
$\widehat{\delta^*_{g_b}}(0)\omega^{(\mu)}_b =
\widehat{\bar\delta^*}(0)\bar\omega+(\widehat{\delta^*_{g_b}}(0)-\widehat{\bar\delta^*}(0))\bar\omega+\widehat{
\delta^*_{g_b}}(0)\omega'$, the last two in $\rho^{\mu+3}$; the first is
$\rho^{\mu+1}N(\rho^{-1}\widehat{\bar\delta^*}(0),\mu)\bar w$, nonzero by (R5), as $\mu\notin\{0,-1\}$. The recursion
(1.3): for $1\le k\le K$, the right side $-A_1\breve\omega^{k-1}-A_2\breve\omega^{k-2}$ has $\rho^{-2}$ of it with
$m = \mu-k$ and leading coefficient that of $-\bar A_1\breve{\bar\omega}^{k-1}$, of type $\tau$, while its other terms
are lower by at least $\epsilon_{\mathrm{ind}}$, which is all the identification of the leading coefficient needs
(D231): $(A_1-\bar A_1)\breve{\bar\omega}^{k-1}$ and $A_2\breve\omega^{k-2}$ are in $\rho^{\mu-k+4}$,
$\bar A_1(\breve\omega^{k-1}-\breve{\bar\omega}^{k-1})$ is in $\mathcal A^{\mu-k+2+\mathcal E_{\mathrm{ind}}}$ by Lemma
2.1, and $(A_0-\bar A_0)$ applied to the leading term to be found is in $\rho^{\mu-k+4}$. $\mu-k$ is no type-$\tau$ root
(R4), so Lemma 2.1 gives $\breve\omega^k$ with leading term the model's $\breve{\bar\omega}^k$ (computed, J5: the model
recursion $N_0(\mu-i)\breve{\bar\omega}^i = -N_1(\mu-i+1)\breve{\bar\omega}^{i-1}$ is solvable and the assembled
polynomial lies in $\ker\bar\Box^\Upsilon$). The corrections, lower by at least $\epsilon_{\mathrm{ind}}$, may meet
roots, and their logarithms are in $\mu-k+\mathcal E_{\mathrm{ind}}$. The statements about $\breve h^{(\mu),k}_b$ follow
from (1.4). $\square$

*Remarks.* (a) *What is deferred.* The source also states that the leading terms $\bar h^{(0)}_{\mathrm s0}$, $\bar
h^2_{\mathrm s1}(S)$, $\bar h^1_{\mathrm v1}(V)$ and $\widehat{\bar\delta^*}(0)\bar\omega$ span the kernels of the
indicial families of the linearised gauge-fixed Einstein operator's model at the corresponding roots, $N_\tau(\bar
L(0),\lambda)$, $\lambda = 0,-1,-1,\mu+1$. That is a statement about $\bar L$, whose indicial roots and kernels are
[Hin26] Lemma 8.4 at $n = 4$; it is proved with that lemma, in the part on [Hin26] section 8 (computed already:
supplement 10.24 (a)-(b), (iv), `lin5.py`). (b) *The window.* The classes and their degrees are the source's, chosen
there to capture the pure gauge contributions down to $t_*^{-4}$ in the late-time expansion at $n = 3$. Which window $n
= 4$ needs is decided by the decay proved in the parts on [Hin26] sections 11-12; if it is wider, the same construction
applies to the further roots, given the corresponding root facts. (c) *No logarithm in (1).* The source's
$\breve\omega^{(0),1}_{b,\mathrm s0}\in\mathcal A^{(-1,0)\cup(0,1)\cup(1+\mathcal E_{\mathrm{ind}})}$ carries $\log\rho$
at the s0 root 0, from the $\rho^2$ term of its source; at $n = 4$ that term vanishes.

## 4. Findings, labels and sources

### 4.1 Findings

(D$'''$1) *A misprint in the recursion.* The source's proof of Proposition 6.18 prints the $t_*^{j-l}$-coefficient as
$A_0\breve\omega^l+A_1\breve\omega^{l-1}+A_0\breve\omega^{l-2}$; it is $A_2\breve\omega^{l-2}$, as its own construction
of $\breve\omega^k$ two lines later uses ((1.3)).

(D$'''$2) *A normalisation in (6.39a).* The source defines $h^{(0),\le k}_{b,\mathrm s0} :=
\delta^*_{g_b}\omega^{(0),\le k+1}_{b,\mathrm s0}$ and writes it as $t_*^kh^{(0)}_{b,\mathrm s0}+\cdots$; the $t_*^k$
coefficient of $\delta^*_{g_b}\omega^{(0),\le k+1}_{b,\mathrm s0}$ is $(k+1)h^{(0)}_{b,\mathrm s0}$. Its (6.45) is
consistent with the factor $k$ it carries. Here $h^{(0),\le k}$ is normalised by $(k+1)^{-1}$; nothing changes.

(D$'''$3) *Two orders, one logarithm fewer.* The correction to the leading term of each state lies two orders below it
($\rho^{\mu+2}$ for the class states, $\rho^1$ against $\rho^{-1}$ in (1)), where the source has one (in the recursion
(1.3) the higher coefficients are shown, and needed, only to $\epsilon_{\mathrm{ind}}$ below their leading terms; D231);
part (1) has no logarithm; the leading terms are the source's in form, with the five-dimensional constants
$\beta_e = \frac{2-e_\Upsilon}{4e_\Upsilon}$ (source $\frac{2-e_\Upsilon}{3e_\Upsilon}$) and
$1\pm\frac25\gamma_\Upsilon$ in (3.3) (source $1\pm\frac12\gamma_\Upsilon$).

(D$'''$4) *The ranges.* Parts (1)-(3) need $0<z<4$ (s0) and $0<z<\frac{20}3$ (s1); the classes need $0<z<4$, sharp at
the s0 class ($\mu_{\mathrm s0}+2$ meets 0 at $z = 4$); all hold for $z\le\frac12$. $z>0$ is needed: at $z = 0$, $-2$ is
an s1 root and the sl class roots coincide with integers (supplement 10.30 (iv), (vi)).

(D$'''$5) *A tool for growing solutions.* Lemma 2.1 makes explicit the source's "using Lemmas 2.15 and 6.13 as usual": a
hand step for the leading term, the formal solution lemma for the intermediate terms, and the zero energy inverse for
the decaying remainder; and it needs the indicial roots only on the type of the leading coefficient.

(D$'''$6) *Tensor type.* $\hat L(0)$ at $n = 4$ has tensor-type roots ($-l$, $l+2$; supplement 10.24 (ii)), which the
source's three dimensions lack; 1-forms have no tensor type, so no pure gauge state belongs to them (supplement 10.30
(b)).

### 4.2 Labels

Proved here, assuming (Dyn) (Part VI): Lemma 2.1 and Proposition 3.1, except Remark (a)'s spanning statements, which are
proved with [Hin26] Lemma 8.4. Computed (exact; rerun D224): `genstates5.py` H1-H5, `puregauge5.py` J1-J6.

### 4.3 Sources

READ: [Hin26] pp. 128-134 (section 6.5.2: its introduction, the conventions (1)-(3), (6.36a)-(6.37), Proposition 6.18
with (6.38)-(6.42) and footnotes 74-76, the discussion after it, Remark 6.19 with (6.43), and the proof with
(6.44)-(6.46)), arXiv:2606.28253v2, full text. The record's supplement 10.29-10.30 (N1STAR-PROOF.md) for the computed
statements.
