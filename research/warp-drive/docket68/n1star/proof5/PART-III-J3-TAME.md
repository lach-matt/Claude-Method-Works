# Part III.J$''$. Tame estimates, n = 4 ([Hin26] Remark 11.13; the tame forms of Corollary 11.66 and Theorem 12.8)

*Status.* Written (D286); verified (D290: verifier 124's findings seated; D292: verifier 126 read the repairs, three
minor findings seated); proved (D295: verifier 127 read the D292 repairs and found them resolved).
This part proves, at spatial
dimension $n = 4$ and at the black hole parameters $b_0$, the tame estimates that [Hin26] asserts in Remark 11.13 (p.
226), states for Corollary 11.66 (pp. 294-295) and Theorem 12.8 (p. 312) without proof, and uses in section 13 (pp.
321-322, Step 3 (2)-(3)): the tame form of III.I$''''''''''''''$ Theorem 3.1 (Theorem 4.1) and of III.J$'$ Theorem 2.1
(Theorem 4.2), and the tame bounds of the map $U\mapsto P_5(\Phi(U))$ (Proposition 4.3). It discharges (J$'$2) of
III.J$'$ at $b_0$ in the b-regularity, with the background small in one fixed norm (Lemma 2.3). Two things stay open:
the weights ((J$''$4): the inverse is shown to map a source at the loss $\epsilon'$ to a solution at the loss
$\epsilon\ge\epsilon'$, while II.G needs $\epsilon' = \epsilon$, which the source states), and (J$'$3), the linear
theory at $b\ne b_0$.

*What n = 4 changes.* (1) *The argument is written out.* The source states that "the tameness of the initial tame
estimate (11.23) will propagate throughout all of our arguments" and omits the intermediate tame statements. Here: a
calculus of tame families (section 1); the elementary families, with the finite-order forms of the model statements that
III.I-III.I$''''''''''''''$ state at b-regularity $\infty$ (section 2); the inventory of every construction of
III.I-III.I$''''''''''''''$ and III.J$'$ (section 3); and the theorems (section 4). (2) *One model map loses
b-regularity growing with the order*: II.G$'$ Corollary 4.5 (high frequencies), with the loss $\lceil
k\delta\rceil+\ell$, $\delta = \delta_\Gamma(-\eta)$. At $b_0$ the operator is strongly trapping admissible (III.F
Proposition 4.1), so for each order $k$ the trapping data can be taken with $(k+1)\delta_\Gamma\le1$ (III.H$'$ (H$'$3)),
and the loss is at most $\ell+1$ at every $k$ (Lemma 2.1 (f)). (3) *Choices that depend on the order* (that cut-off
radius, and the low-energy radius $c_k$ of III.H Corollary 4.2) enter only decompositions of a solution that does not
depend on them, so they cost constants, not derivatives (Remark 2.2).

## 1. Tame families

Throughout $b = b_0$. A *background* is $\beta = (h,\vec p,q)$ with $h\in\mathcal X^\infty$, $\vec p\in\mathcal P$ and
$q\in\mathcal Q^\infty$ in the classes of the part at hand (III.I section 1 for $h$ alone; III.I$''''''''''''''$ section
1, with $\mathcal P$ enlarged by the rotation rows; for III.J$'$, $\beta = \Phi(U)$), and $\|\beta\|_k :=
\|h\|_{\mathcal X^k}+|\vec p|+\|q\|_{\mathcal Q^k}$. A *graded space* is a family of Banach spaces $E^k$, $k\in\mathbb
N_0$, with continuous inclusions $E^{k+1}\hookrightarrow E^k$ of norm at most 1 (II.G Remark 2.2), and $E^\infty :=
\bigcap_kE^k$. The spaces of III.I-III.I$''''''''''''''$ and III.J$'$ are of this kind: weighted b-Sobolev spaces of
b-regularity $k$; partially polyhomogeneous ones, normed by the order-$k$ norms of their finitely many coefficients and
of the remainder; finite-dimensional spaces ($E^k = E$); and direct sums. Several of those spaces carry orders read
"$w-$" (III.I$''''''''''''''$ section 1, III.J Definition 1.1): they are intersections over a loss $\epsilon>0$, and
their order-$k$ spaces are Fréchet, not Banach. Such a space is taken here at a fixed loss: $E^k_\epsilon$ is the Banach
space with every order $w-$ replaced by $w-\epsilon$, and $E^\infty_\epsilon := \bigcap_kE^k_\epsilon$. A statement of
III.I-III.I$''''''''''''''$ or III.J$'$ from a "$w-$" space to a "$w-$" space is a continuous linear map between Fréchet
spaces (closed graph theorem), so for every loss $\epsilon$ of the output and every order $k$ there is a loss
$\epsilon'(\epsilon,k)\in(0,\epsilon]$ of the input at which it is bounded. That $\epsilon'$ can be taken independent of
$k$ is read off the proofs, each step choosing its margins from the loss its output is to have: in the rows read for it,
III.I$''$ Proposition 5.1, III.I$''''''$, III.I$'''''''''''$'s level-3 loop (the margin
$\epsilon_{\mathrm{ind}}-\epsilon$), III.I$''''''''''''''$'s levels $\beta_k$, III.J$'$ Lemma 1.1 ($\eta_2 :=
\epsilon_+-3\epsilon$, which gives the $\iota^+$-order $3+\epsilon_+-5\epsilon$) and II.G$'$ Corollary 4.5
($\beta_{\mathrm{scf}} := \beta'_I+\epsilon$), no margin depends on $k$; for the other rows it is part of (J$''$4), and
it becomes moot once $\epsilon' = \epsilon$ is shown. Below, $\epsilon\in(0,\epsilon_1]$ is fixed, every output space is
taken at the loss $\epsilon$ and every input space at the loss $\epsilon'$ that the statement assigns; whether
$\epsilon' = \epsilon$ can be taken is (J$''$4).

**Definition 1.1 (tame families).** Let $E$, $G$ be graded spaces, $d_0,d\in\mathbb N$, $\delta_0>0$, and $\mathcal B :=
\{\beta:\|\beta\|_{d_0}<\delta_0\}$. A family $(T_\beta)_{\beta\in\mathcal B}$ of linear maps $E^\infty\to G^\infty$ is
*tame with loss $d$* if for every $k\in\mathbb N_0$ there is $C_k$ with
$$\|T_\beta e\|_{G^k}\le C_k\big(\|e\|_{E^{k+d}}+\|\beta\|_{k+d}\|e\|_{E^d}\big),\qquad\beta\in\mathcal B,\ e\in
E^\infty.\tag{1.1}$$
A family $(v_\beta)$ in $G^\infty$ is *tame with loss $d$* if $\|v_\beta\|_{G^k}\le C_k(1+\|\beta\|_{k+d})$ for every
$k$.

**Lemma 1.2 (closure).** Let $\delta_0\le1$.

(a) Sums of families tame with loss $d$ are tame with loss $d$; a family tame with loss $d$ is tame with every loss
$d'\ge d$.

(b) If $(T_\beta)$, $E\to G$, is tame with loss $d$, $(S_\beta)$, $G\to H$, with loss $d'$, and $d_0\ge d+d'$, then
$(S_\beta T_\beta)$ is tame with loss $d+d'$.

(c) (*Finite rank.*) If $\ell_\beta:E^\infty\to\mathbb C^N$ satisfies $|\ell_\beta e|\le C\|e\|_{E^d}$ on $\mathcal B$,
and $v^1_\beta,\dots,v^N_\beta$ are tame with loss $d$, then $e\mapsto\sum_i(\ell_\beta e)_iv^i_\beta$ is tame with loss
$d$. In particular a family of linear maps between finite-dimensional spaces, bounded on $\mathcal B$, is tame with loss
0.

(d) (*Fixed maps.*) A linear map $T$ independent of $\beta$ that is bounded $E^{k+d}\to G^k$ for every $k$ is tame with
loss $d$.

(e) A composition of $N$ families, each tame with loss at most $d$, is tame with loss $Nd$ if $d_0\ge Nd$; $N$ is fixed,
independent of $k$.

(f) (*Regularity statements.*) If a statement takes $e\in E$ and an a priori solution $u$ in a space $E'$ to $u\in G$,
and the family $(e,u)\mapsto u$, $E\oplus E'\to G$, is tame with loss $d$, then for $(S_\beta)$, $E\to E'$, tame with
loss $d'$, $e\mapsto u = S_\beta e$ into $G$ is tame with loss $d+d'$. A statement of this kind independent of $\beta$
that is a membership statement between Banach spaces at each order $k$ has, by the closed graph theorem, the bound
$\|u\|_{G^k}\le C_k(\|e\|_{E^{k+d}}+\|u\|_{E'^{k+d}})$, and is then tame with loss $d$.

(g) Definition 1.1 asks one bound for each $k$: a family whose order-$k$ bound is proved with choices made for the order
$k$ (Remark 2.2) is tame with loss $d$ if each of these bounds has the loss at most $d$.

*Proof.* (a) is immediate, the norms being non-decreasing in $k$. (b) By (1.1) for $S$ and then for $T$,
$$\|S_\beta T_\beta e\|_k\le C_k\big(\|T_\beta e\|_{k+d'}+\|\beta\|_{k+d'}\|T_\beta e\|_{d'}\big)\le
C_k\big(\|e\|_{k+d+d'}+\|\beta\|_{k+d+d'}\|e\|_d+\|\beta\|_{k+d'}(\|e\|_{d+d'}+\|\beta\|_{d+d'}\|e\|_d)\big),$$
and $\|\beta\|_{d+d'}\le\|\beta\|_{d_0}<1$, $\|\beta\|_{k+d'}\le\|\beta\|_{k+d+d'}$ and $\|e\|_d\le\|e\|_{d+d'}$ give
(1.1) with loss $d+d'$. (c) $\|\sum_i(\ell_\beta e)_iv^i_\beta\|_k\le C\|e\|_d\sum_i\|v^i_\beta\|_k\le
C_k\|e\|_d(1+\|\beta\|_{k+d})$, which is at most the right side of (1.1). (d) is (1.1) without its second term. (e)
follows from (b) by induction. (f): $e\mapsto(e,S_\beta e)$ is tame with loss $d'$ by (a), and (b) applies. (g) is
Definition 1.1. $\square$

## 2. The elementary families

**Lemma 2.1 (the elementary tame families).** For $d_0$ large and $\delta_0$ small the following are tame, with losses
independent of $k$.

(a) (*Forward solutions.*) The forward solution operators of the operators $L^{g,g_0}$, $g = g_0+\tilde h$, used in
III.I-III.I$''''''''''''''$: $\tilde h = h$ (III.I Theorem 5.3), $\tilde h = h+h^{(-1)}(S)$ and $h+h_{\mathrm{tot}}(\vec
p)$ ($L_{h,S}$ of III.I$''''$, $L_{h,\vec p}$ of III.I$'''''''$-III.I$'''''''''$; the gauge modifications
$\delta^*_{g_0,E_C}\vartheta_{\mathrm{tot}}(\vec p)$ do not enter them, $D_h$ removing them, III.I$''''$ Lemma 2.5,
III.I$'''''''$ Lemma 2.5 (a)), and $\tilde h = h+h_{\mathrm{rem}}(q)+h_{\mathrm{tot}}(\vec p)$ (III.I$''''''''''''''$
Theorem 3.1, Step 0), between the spaces of III.I (5.1) and its target. For $\tilde h = h$ this is III.I (5.2). In
general $\tilde h$ lies in the class of III.I Theorem 5.3 ($h_{\mathrm{rem}}(q)$ has $K^+$-order $(\alpha-2)->2$,
III.I$''''''''''''''$ Remark 3.2 (1)), with $\|\tilde h\|_{\mathcal X^k}\le C_k\|\beta\|_{k+d}$ (III.I$''''$ Lemma 2.5,
III.I$'''''''$ Lemma 2.5, III.I$''''''''$ Lemma 2.5, III.I$'''''''''$ Lemma 2.5, and III.I$''''''''''''''$ Definition
1.2 with the towers fixed), and the background $g_0$ ($g_S$, or $g_{\vec p}$, smooth in $\vec p$) and
$h_{\mathrm{tot}}(\vec p)$ add to $P-P_0$ coefficients smooth in $\vec p$; so III.I Theorem 5.3's proof gives
$\|P-P_0\|_{(0;k+d)}\le C_k\|\beta\|_{k+d+5}$ and (5.2) with $\|\beta\|$ for $\|h\|$.

(b) (*Background coefficients.*) $u\mapsto(L^{g,g_0}-L_{b_0})u$, $u\mapsto R_qu$, $\Delta_q$, the sources $f^S_{h,\vec
p}$, $f^b_{h,\vec p}$, $f^{\mathrm s1}_{h,\vec p}$, $f^\nu_{h,\vec p}$, $r^\nu_{h,\vec p}$, $L_bh_{\mathrm{rem}}(q)$ and
the remainder $\tilde L$ of III.I$'$ Lemma 1.1, between the weighted spaces of III.I Proposition 4.1 (4.2),
III.I$'''''''''$ Lemma 2.6 and III.I$''''''''''''''$ Lemmas 2.2-2.4. Each is a b-differential operator of order at most
2 whose coefficients are polynomial in the background, $g^{-1}$ and their derivatives (or such a coefficient applied to
a fixed section); by II.A Corollary 9.7 and Lemma 9.5, with II.G Lemma 4.1 for the nonlinear functions of the
background, $\|Au\|_k\le C_k(\|u\|_{k+2}+\|\beta\|_{k+d}\|u\|_{d})$ for $\|\beta\|_{d_0}$ small, the weights adding as
in the cited membership statements (Lemma 2.4 in the partially polyhomogeneous spaces).

(c) (*Finite-dimensional algebra and coefficients.*) The inverses $(S^{(-1)}_{h,S})^{-1}$ (III.I$''''$ Corollary 4.3),
$(S^{(-1)}_{h,\vec p})^{-1}$ (III.I$'''''''$ Corollary 4.6), $T_{h,\vec p}^{-1}$ (III.I$''''''''$ Proposition 4.1,
III.I$'''''''''''$ Theorem 4.1), $(-\mathrm{id}+A_k)^{-1}$ and the inverse of $C^{\mathrm{rot}}$ in $\vec
W'^{\mathrm{rot}}$ (III.I$''''''''''''''$ Theorem 3.1, Steps 3 and 4'), and $(z-\frac32-\bar A)^{-1}$ (III.I$'$
Proposition 3.1): bounded on $\mathcal B$ by the cited statements (close to $\pm\mathrm{id}$, or fixed). The coefficient
functionals ($\dot S$, $S_\nu$, $C^{k+1}_\nu$, $C^{\mathrm{rot}}$, the dual functionals of III.I$''''''''''''''$ Step
4', the $t_*$-coefficients at $K^+$): bounded by a fixed low norm of the solution they are applied to, by the cited
statements and III.I$''''''''''''$ Lemma 2.3 (a). The finite-dimensional states, rows $m_\nu$, towers $T_{\rho,b_0}$ and
states of III.I$''''''''''''''$ Lemma 2.1 they are paired with are fixed smooth sections. So, composed with tame
families, they give tame families by Lemma 1.2 (b)-(c). The conormal components $\dot S_{\mathrm{rem}}$, $\dot
b_{\mathrm{rem}}$, $\dot Y_\rho$ of $q'$ are not finite-dimensional: they are functions of $t_*$ that
III.I$''''''''''''$ Theorem 3.1 assembles in its Step 4 ($\dot S_{\mathrm{rem}} := A+A_5+a_{\mathrm s}$, $\dot
b_{\mathrm{rem}} := B+a_{\mathrm b}$, $\dot Y_\rho := a_\rho+Y^c_\rho$) from the outputs of its Steps 1-3, so they are
outputs of a composition of the families of its row in section 3, tame with a fixed loss by Lemma 1.2 (e).

(d) (*Integrations along faces.*) III.A Lemmas 1.2 and 3.2 (membership statements, which take the a priori norm of the
solution as an input: Lemma 1.2 (f)) and III.I$''$ Lemma 2.1: order $k$ to order $k$ (loss 0); III.I$''$ Lemma 3.1: loss
$\ell$, independent of $k$, as stated.

(e) (*Transforms and the low and middle frequencies.*) III.A Proposition 4.2 (1) (Fourier transform, loss $l$), II.G$'$
Proposition 3.3 (1) (loss 1), Proposition 3.5 (loss $\ell$) and Corollary 4.2 ((1): loss $j+\ell$ for
$\partial^j_\sigma$, $j$ fixed by the weights; (2): loss $\ell$), III.H Proposition 3.2 ($\widetilde{L_b}(0)^{-1}$, loss
1), III.H Corollary 4.2 (on $|\sigma|<c_k$, no loss) and III.I$''$ Lemma 4.2 (loss $\ell$): as stated, at every order
with the loss independent of the order.

(f) (*High frequencies.*) II.G$'$ Corollary 4.5 loses $\lceil k\delta\rceil+\ell$, $\delta = \delta_\Gamma(-\eta)$ (I.B
(1.4)), where $\ell = 2\ell_3+\ell_4+\ell_5$ (the proof of II.G$'$ Corollary 4.5, with its Lemma 4.3 and Propositions
3.3 and 3.5) depends only on the orders and the weights, not on $\eta$, the trapping data or the constant $C_0$. At
$b_0$, $2L_{b_0}$ is strongly trapping admissible (III.F Proposition 4.1): for every $k$ the trapping data and $\eta$
can be chosen with $(k+1)\delta_\Gamma(-\eta)\le1$ (III.H$'$ (H$'$3); the proof below), and then the loss at the order
$k$ is at most $\ell+1$. III.I$''$ Lemma 4.1 composes this with (e) and the invertibility of III.H Corollary 4.4 on the
middle frequencies; it has loss at most $\ell+1$ plus the losses of (e).

(g) (*Model inverses stated at order $\infty$.*) Each of the following holds at every order $k$ with a loss independent
of $k$, by its own proof, read at the order $k$:

- III.G$'$ Theorem 3.1 (2): $N_{\iota^+}(\lambda)^{-1}$ has the loss $d$ at every $k$, as stated, finite-meromorphic in
$\lambda$ with principal parts independent of $k$. III.G$''$ Theorem 4.2 and Corollary 4.3 compose it with a contour
integral over a fixed circle on which $\lambda\notin\mathrm{spec}_{\iota^+}(\bar L)$ (bounded at each order, uniformly
on the circle), with the towers at $b_0$ (fixed sections paired with finitely many coefficients) and with $L_b$ (loss
2): loss $d+2$. The same holds for III.G$'''$ Corollary 3.1, Proposition 2.4 and Proposition 3.7, whose fixed losses
III.J's proof of Theorem 2.4 records ((G$'''$4), loss $l$).

- III.F$'$ Corollary 3.4:
$N_{\mathrm{tf}}(\widehat{L_b},\pm1)^{-1}$ has the loss $\ell$ at every $k$, as stated. III.G$''''$ Theorem 3.1 and
Propositions 4.4 and 5.1 compose it with $\widetilde{L_b}(0)^{-1}$ ((e)), cut-offs, a Mellin inversion on a fixed
vertical line not crossing a root (bounded at each order), and finitely many rounds whose number is fixed by the weights
(each raises the order by at least $\epsilon_{\mathrm{ind}}-\epsilon$): fixed loss.

- III.I$'$ Propositions 2.1 and 3.1: compositions of (d), of $(z-\frac32-\bar A)^{-1}$ ((c)) and of $\tilde L$ ((b),
loss 2, its coefficients depending on $h$); Proposition 2.1 is a regularity statement, the family $(f,u)\mapsto u$ with
the a priori norm of $u$ as an input (Lemma 1.2 (f)), as is III.A Lemma 3.2 within it; in finitely many steps whose
number is fixed by $\ell_I$, $\ell_+$ and the index sets: fixed loss.

- III.I$''$ Lemma 4.3: $\hat b\mapsto\chi G_1(\hat
b)$, $\hat S\mapsto\chi G_2(\hat S)$ multiply finite-dimensional data by fixed sections built from the states: loss 0.

*Proof.* (a)-(c) are proved in their statements. (d) and (e) are the cited statements, each of which is stated at every
order with the loss independent of it. (f): that $\ell$ depends only on the orders and the weights is read off from the
proof of II.G$'$ Corollary 4.5 ($\ell_4 = \ell_1+\ell_2+2N+\lceil(\delta_2-\delta_1)_+\rceil$ there; $\ell_3$, $\ell_5$
from its Lemma 4.3 and Propositions 3.3 and 3.5). For $\delta$: in I.B (1.4) the function $f$ is Lipschitz with the
constant $\sup_\Gamma q^\Gamma$ and decreases at the rate at least $2\beta_0$ ($q^\Gamma\ge2\beta_0$), with $f(\gamma_+)
= 0$ and $f(\gamma_-) = \frac12\nu_{\min}$; hence $\gamma_+-\gamma_-\ge\nu_{\min}/(2\sup_\Gamma q^\Gamma)$ and
$\gamma_+\le\max(f(0),0)/(2\beta_0)$. Strong trapping admissibility (III.F Proposition 4.1) gives trapping data with
$f(0)<\epsilon$ for any $\epsilon>0$, while $\beta_0$, $\nu_{\min}$ and $q^\Gamma$ do not depend on them. So
$\delta_\Gamma(-\eta)\le(\epsilon/(2\beta_0)+\eta)\cdot2\sup_\Gamma q^\Gamma/\nu_{\min}$, and $\epsilon$, $\eta$ of the
order of $1/(k+1)$ give $(k+1)\delta_\Gamma(-\eta)\le1$, so $\lceil k\delta\rceil\le1$; this is the bound III.H$'$
(H$'$3) states for the order $k$. (II.G$'$'s remark after Proposition 4.4 treats only $\gamma_+\le0$, with the loss
$\lceil1/(-\gamma_-)\rceil$ at $\gamma_+ = 0$, and is not used.) (g): each statement is a finite composition of maps of
(b)-(e) and of the two face inverses cited, at a fixed number of steps; Lemma 1.2 (e)-(f) applies, $\beta$ entering only
through the families of (b) (in III.I$'$ Propositions 2.1 and 3.1, through $\tilde L$). $\square$

**Remark 2.2 (choices that depend on the order).** In (e)-(f) two choices depend on $k$: the radius $c_k$ of the
low-energy cut-off, and the trapping data. Both enter only decompositions $u =
u_{\mathrm{hi}}+u_{\mathrm{reg}}+u_{\mathrm{sing}}$ (and their analogues) of a solution $u$ that does not depend on
them, used to show that $u$ lies in a better-weighted space; at the order $k$ the decomposition made with the order-$k$
choices gives the order-$k$ bound. So the choices change the constants $C_k$, which may depend on $k$, and not the
losses (Lemma 1.2 (g)).

**Lemma 2.3 (smallness in one norm).** There is $d_*$ such that every smallness condition on the background in
III.I-III.I$''''''''''''''$ and III.J$'$ is smallness of $\|h\|_{\mathcal X^{d_*}}+|S|+|\vec p|+\|q\|_{\mathcal
Q^{d_*}}$, and every statement there that a finite-dimensional map is close to $\pm\mathrm{id}$, or that a family is
continuous at the background 0, holds in the topology of this norm. Hence Lemma 2.1 and section 3 hold with $d_0 :=
d_*+D$, $D$ the total loss of the compositions of section 3 (the $d$ of Theorem 4.1), and one $d_0$ serves every order
$k$.

*Proof.* III.I Theorem 5.3 asks $\|h\|_{\mathcal X^{d_T}}<\epsilon_0$, $d_T$ fixed, and II.F$'$ Theorem 1.1 asks
$\|P-P_0\|_{(0;d),(2\ell_I,\ell_+,\ell_K)}<\epsilon_0$, which Lemma 2.1 (a) bounds by $C\|\beta\|_{d+d'+5}$. III.I$''''$
Lemma 4.2 (b) proves the continuity of $(h,S)\mapsto\dot S_{h,S}$ with $h$ in the $\mathcal X^d$-topology, $d\ge
k_1+d_T+7$, whence $S^{(-1)}_{h,S}$ is close to the identity (its proof). III.I$'''''''$ fixes "$h$ small" as small in
$\mathcal X^d$, $d$ fixed, for its Lemmas 2.5, 3.1 (c), 4.1, 4.3, 4.5 and Corollary 4.6; III.I$''''''''$ takes the same
convention for Proposition 4.1 and $T_{h,\vec p}$, and III.I$'''''''''''$ Theorem 4.1 takes the continuity of $T_{h,\vec
p}$ from III.I$''''''''$ Proposition 4.1 (ii). III.I$''''''''''''''$ fixes "$q$ small" as small in one fixed seminorm of
large order, so that
$h+h_{\mathrm{rem}}(q)$ is small in III.I$''''''''$'s $\mathcal X^d$ (equivalently III.I$'''''''$'s, III.I$''''''''$
taking III.I$'''''''$'s convention). Its Steps 3 and 4' take $A_k\to0$ and the derivative of $C^{\mathrm{rot}}$ at 0
also from III.I$''''''''$ Lemma 3.3, III.I$'''''''''$ Lemma 2.6, III.I$'''''''''''$ Lemma 3.3, III.I$'''''''''''''$
Lemma 2.3 and its own Lemmas 2.3-2.4. Of these, III.I$'''''''''$ Lemma 2.6 is continuous with $h\in\mathcal X^k$,
$k\ge5$, under III.I$''''''''$'s convention for "small"; III.I$''''''''''''''$ Lemmas 2.3-2.4 bound $R_q$ and $\Delta_q$
by $C\|q\|$ in the one fixed seminorm of $q$; and III.I$''''''''$ Lemma 3.3, III.I$'''''''''''$ Lemma 3.3 and
III.I$'''''''''''''$ Lemma 2.3 (by III.I$'''''''''''$ Lemma 3.3's proof) state $(h_j,\vec p_j)\to(0,0)$ without naming a
topology, but their proofs give $S^{h_j,\vec p_j}_\nu(G_j)-S^{0,0}_\nu(G) = S^{0,0}_\nu(R_j)$, $R_j :=
G_j-G-(L_j-L_{b_0})u_j$, with $S^{0,0}_\nu$ bounded by one fixed seminorm (Lemma 2.1 (c)), so they need $R_j\to0$ only
in that seminorm: $G_j\to G$ there, and $(L_j-L_{b_0})u_j\to0$ there, which holds for $h_j\to0$ in $\mathcal X^{d'}$,
$d'$ fixed (Lemma 2.1 (b) at that order), with $u_j$ bounded at a fixed order. Step 4' needs $R\to0$ only at one loss
$\epsilon$ and one order. None of these orders depends on $k$, and $d_*$ is their maximum. For III.J$'$,
$\|\Phi(U)\|_{d_*}\le C\|U\|_{\mathcal D^{d_*+d}}$ (III.J Theorem 2.4). $\square$

**Lemma 2.4 (tame products in partially polyhomogeneous spaces).** Let $E$, $E'$ be partially polyhomogeneous spaces of
section 1 at one or more faces, at the loss $\epsilon$, and $G$ the space that the membership statements (III.C Lemma
2.1) give to products. There is $d_1$ with $\|uv\|_{G^k}\le
C_k(\|u\|_{E^k}\|v\|_{E'^{d_1}}+\|u\|_{E^{d_1}}\|v\|_{E'^k})$; and if the exponents of $E$ have positive real parts, as
those of the background do, then for a smooth $\Theta$, depending also on the point (through $g_0$, $g_0^{-1}$ and their
derivatives), with $\Theta(\cdot,0) = 0$ and $\|u\|_{E^{d_1}}\le1$,
$\|\Theta(u)\|_{G^k}\le C_k\|u\|_{E^k}$, $G$ the space of $\Theta(u)$ by the same statements.

*Proof.* The coefficient of $uv$ at an exponent is a finite sum of products of coefficients of $u$ and of $v$, functions
on the face bounded by II.G Lemma 4.1 (2) there; a product with a remainder factor is bounded by II.G Lemma 4.1 (2) in
the weighted b-Sobolev space, the weights adding (II.A Corollary 9.7); a term whose exponent lies beyond the remainder's
weight is put in the remainder with the same bound. For $\Theta$: Taylor's formula to an order $N$, fixed by the
weights, at which $N$ times the least real part of the exponents exceeds the remainder's weight; the polynomial part by
the product bound, the Taylor remainder by II.G Lemma 4.1 in the weighted b-Sobolev space. $\square$

## 3. The inventory

Each construction of III.I-III.I$''''''''''''''$ and of III.J$'$ is a composition, in a fixed number of steps, of the
families of Lemma 2.1; the table lists them. FWD is Lemma 2.1 (a), BG (b), FIN (c), INT (d), MOD (e)-(g); a loop's
length is fixed by the weights and orders of the statement, never by $k$.

| Part | statement | maps used | steps |
|---|---|---|---|
| III.I | Theorem 5.3 | FWD (II.F$'$ Corollary 1.2) | 1 |
| III.I | Remark 5.5 | FWD, BG ((4.2)), MOD (the stationary inverses below) | the rewritings $L_bu = f-(L^{g,g_0}-L_b)u$, finitely many |
| III.I$'$ | Propositions 2.1, 3.1 | INT, FIN, BG ($\tilde L$) | finitely many, fixed by $\ell_I$, $\ell_+$ |
| III.I$''$ | Proposition 5.1 | FWD (III.I), BG, MOD (III.I$'$ Propositions 2.1, 3.1; Lemmas 2.1, 3.1, 4.1-4.3; II.G$'$ Propositions 3.3, 3.5; III.A Lemma 1.2) | rounds raising $\alpha'_K$ by $\min(a_K-2,\alpha_K-\alpha'_K)$ |
| III.I$'''$ | Proposition 2.1 | FWD (III.I$''$), BG, MOD (III.I$'$ Propositions 2.1, 3.1; III.H Proposition 3.2; III.I$''$ Lemmas 3.1, 4.1-4.3), FIN (the coefficient $S_0$) | 1 |
| III.I$''''$ | Proposition 4.1, Lemma 4.2, Corollary 4.3 | FWD (III.I$'''$), BG ($h^{(-1)}(S)$, $f_{h,S}$), FIN ($\dot S = \Pi f'$, $(S^{(-1)}_{h,S})^{-1}$) | 1 |
| III.I$'''''$ | Proposition 2.1, Corollary 2.2 | FWD (III.I$''''$), BG, MOD (III.I$'$; III.G$''$ Corollary 4.3; III.H Proposition 3.2), FIN | exponents in a window, and rounds raising $\alpha'_K$ to $\alpha_K$ |
| III.I$''''''$ | Lemmas 1.2-1.4, Proposition 2.1 | FWD (III.I$'''''$), BG ($(L-L_b)u$, III.I Proposition 4.1 (4.2)), MOD (III.A Proposition 4.2; $\widetilde{L_b}(\sigma)^{-1}$ by III.I$''$ Lemma 4.2; III.I$''$ Lemmas 2.1, 4.1, 4.3; III.I$'$ Proposition 2.1; III.I$'''$ Lemma 1.3; III.H Proposition 3.2; III.G$''$ Corollary 4.3; III.G$''''$ Proposition 5.1; II.G$'$ Propositions 3.3, 3.5 (1)), FIN | 1 |
| III.I$'''''''$ | Lemmas 4.1, 4.3, 4.5, Corollary 4.6 | FWD, BG, FIN | 1 |
| III.I$''''''''$ | Lemmas 3.1-3.3, Proposition 4.1 | FWD, BG, MOD (III.I$'$; III.G$''$ Corollary 4.3; III.G$''''$ Proposition 5.1; III.H Proposition 3.2), FIN | levels $\alpha_0<\dots<\alpha_N$ (fixed by $\alpha$, $a_K$); tf rounds $i_0$ |
| III.I$'''''''''$ | Definition 2.1, Lemmas 2.4, 2.6 | FIN ($m_\nu$, $h_\nu$, $\vartheta_\nu$: fixed sections times $W$), BG ($f^\nu$, $r^\nu$), FWD of $L_{b_0}$ | none |
| III.I$''''''''''$ | Lemma 2.1, Corollary 2.3, Proposition 3.1 | MOD (III.I$'$ Proposition 3.1, formal solutions for $L_b$; III.G$''$ Corollary 4.3), FIN | windows, at most $N_*$ |
| III.I$'''''''''''$ | Lemmas 2.1-2.5, Proposition 3.1, Lemmas 3.2, 3.3, Theorem 4.1 | MOD ($\widetilde{L_{b_0}}(0)^{-1}$; III.G$''''$ Propositions 4.4, 5.1; III.I$''$ Lemma 4.2; III.A Proposition 4.2), BG (columns), FIN, FWD | rounds rising by $\epsilon_{\mathrm{ind}}$; the level-3 loop |
| III.I$''''''''''''$ | Lemmas 2.1-2.4, Theorem 3.1 | FWD, MOD (as III.I$'''''''''''$), BG, FIN | pairs removed, finitely many |
| III.I$'''''''''''''$ | Proposition 2.1, Lemmas 2.2, 2.3, Proposition 2.4 | as III.I$'''''''''''$-III.I$''''''''''''$ at each level $\beta$ | as there |
| III.I$''''''''''''''$ | Theorem 3.1 | FWD ($L_{h+h_{\mathrm{rem}}(q),\vec p}$), BG ($R_q$, $\Delta_q$), FIN, and III.I$''''''''$, III.I$'''''''''''$-III.I$'''''''''''''$ | levels $\beta_0<\dots<\beta_K$ (fixed by $\alpha$, $\alpha_1$) |
| III.J$'$ | Theorem 2.1 | III.I$''''''''''''''$ Theorem 3.1 at $\Phi(U)$; MOD (III.G$'''$ Proposition 3.7; the $t_*^{-\lambda_0}$-terms); BG ($D_U\Phi$) | the exponents of $\Lambda_*$, finitely many |

## 4. The theorems

**Theorem 4.1 (the tame form of III.I$''''''''''''''$ Theorem 3.1; the source's Corollary 11.66, its tame estimate).**
Let $\epsilon\in(0,\epsilon_1]$, and $\epsilon'\in(0,\epsilon]$ the input loss that III.I$''''''''''''''$ Theorem 3.1
assigns to the output loss $\epsilon$ (section 1). There are $d,d_0\in\mathbb N$ and $\delta_0>0$ such that for $b =
b_0$ and $(h,\vec p,q)$ with $\|h\|_{\mathcal X^{d_0}}+|\vec p|+\|q\|_{\mathcal Q^{d_0}}<\delta_0$ the maps
$F\mapsto(h',\vec p\,',q')$ of III.I$''''''''''''''$ Theorem 3.1 satisfy, for every $k\in\mathbb N_0$,
$$\|h'\|_k+|\vec p\,'|+\|q'\|_k\le C_k\Big(\|F\|_{k+d}+\big(\|h\|_{k+d}+|\vec p|+\|q\|_{k+d}\big)\|F\|_d\Big),\tag{4.1}$$
with $\|h'\|_k$ and $\|q'\|_k$ the norms of the order-$k$ spaces of III.I$''''''''''''''$ (3.2) and of $\mathcal Q^k$
(III.I$''''''''''''''$ (1.1)) at the loss $\epsilon$, the background norms at the loss $\epsilon$, and $\|F\|_k$ the
norm of $\mathcal Y^\natural(\alpha-)$ at the loss $\epsilon'$. The same holds for the solution maps of
III.I-III.I$'''''''''''''$ in their spaces, and for III.I$''''''''''''''$ Theorem 3.1 with $\eta_2$ replaced by
$\epsilon_+$ (III.J$'$ Lemma 1.1).

*Proof.* By induction over the parts in their order. Each part's solution map is, by the table of section 3, a
composition of a fixed number of the families of Lemma 2.1 and of the solution maps of earlier parts, which are tame by
the induction; each loop has a length fixed independently of $k$. Lemma 1.2 (b)-(g) gives a tame family with a loss $d$
equal to the sum of the losses, independent of $k$, for $d_0\ge d$ and $\delta_0$ small (Lemma 2.3); the weights compose
in the same way, each family taking its input at the loss its statement assigns (section 1). For III.I$''''''''''''''$
Theorem 3.1 the background is $\beta = (h,\vec p,q)$, and (1.1) is (4.1). $\square$

**Theorem 4.2 (the tame form of III.J$'$ Theorem 2.1; the source's Theorem 12.8, its estimate).** Let $\epsilon$ and
$\epsilon'$ be as in Theorem 4.1, for III.J$'$ Theorem 2.1. There are $d,d_0$ and $\epsilon_0>0$ such that for
$U\in\mathcal D^\infty_\epsilon$ with $b = b_0$ and $\|U\|_{\mathcal D^{d_0}_\epsilon}<\epsilon_0$, the solution $U'$ of
III.J$'$ (2.1) satisfies, for every $k$,
$$\|U'\|_{\mathcal D^k_\epsilon}\le C_k\big(\|f\|_{\mathcal F^{k+d}_{\epsilon'}}+\|U\|_{\mathcal
D^{k+d}_\epsilon}\|f\|_{\mathcal F^d_{\epsilon'}}\big).\tag{4.2}$$
The smallness is in one norm for every $k$ (Lemma 2.3), which replaces the orders $d_k$ of III.J$'$ Theorem 2.1.

*Proof.* Step 0 of III.J$'$ applies Theorem 4.1 at the background $\Phi(U)$, with $\|\Phi(U)\|_k\le C_k\|U\|_{\mathcal
D^{k+d}}$ (III.J Theorem 2.4) and $\|\Phi(U)\|_{d_0}$ small for $\|U\|_{\mathcal D^{d_0+d}}$ small; composed with
$U\mapsto\Phi(U)$, (4.1) has the form (1.1) in the background $U$. Steps 1-3 subtract $D_U\Phi(U'_\bullet)$ for finitely
many $U'_\bullet$: the finite-dimensional data of Step 1 (bounded by a low norm of $(h',\vec p\,',q')$, Lemma 2.1 (c));
the data of Case B of Step 2, $f_{\lambda_0}\in\mathrm{Poly}^K(C;H^{k,\dots})$ and $G'(\lambda_0)\in\mathrm{Res}^k$,
which are not finite-dimensional and are mapped by the right inverse of III.G$'''$ Proposition 3.7, independent of $U$
with the loss $l$, on the finitely many $\lambda_0\in\Lambda_*$ (Lemma 2.1 (g), Lemma 1.2 (d)); and the conormal
remainders of Step 3 (the conormal components of $q'$, Lemma 2.1 (c)). $D_U\Phi(U') =
D\Phi_0(U_0)U'_0+(DA(U_0)U'_0)U_1+A(U_0)U'_1$ (III.J Remark 2.5): the first and third terms are tame in $U'$, uniformly
in $U_0$ small (III.J Theorem 2.4), and the second is bounded by $C|U'_0|\|U_1\|_{\mathcal D^{k+d}}$, of the form (1.1)
as $|U'_0|$ is bounded by a low norm of $f$. Lemma 1.2 gives (4.2). $\square$

**Proposition 4.3 (the forward map; the source's section 13.1, Step 3 (2)).** There are $d$ and $\epsilon_0$ such that
for $b$ near $b_0$, $\epsilon\in(0,\epsilon_1]$ and $U\in\mathcal D^\infty_\epsilon$ with $\|U\|_{\mathcal
D^{3d}_\epsilon}<\epsilon_0$, $\|P_5(\Phi(U))\|_{\mathcal F^k_\epsilon}\le C_k(1+\|U\|_{\mathcal D^{k+d}_\epsilon})$ for
$k\ge d$, and the first and second derivatives of $U\mapsto P_5(\Phi(U))$ satisfy II.G (2.3) with the norms of $\mathcal
D^{3d}_\epsilon$ and $\mathcal F^{2d}_\epsilon$. The map gains nothing in the weights: it takes $\mathcal D_\epsilon$ to
$\mathcal F_\epsilon$.

*Proof.* $\Phi$ is affine in $U_1$ with coefficients smooth in the finite-dimensional $U_0$, and tame (III.J Theorem
2.4). $P_5(h,\vec p,q) = P_4(h+h_{b,\mathrm{rem}}(q),\vec p)$ is $\mathrm{Ric}-\delta^*\Upsilon$ of a metric that is a
smooth function of $\vec p$ plus $h+h_{b,\mathrm{rem}}(q)$, so a smooth function of $(h,\partial h,\partial^2h)$ and of
$q$ with coefficients smooth in $\vec p$; II.G Lemma 4.1 (with II.A Lemma 9.5) bounds it and its first two derivatives
tamely in the b-Sobolev norms. The weights are those of III.J (2.5), which holds at every $b$ near $b_0$ (D285): the
cancellation enters only qualitatively: the terms of $u$-exponent below $3+\epsilon_+$ cancel identically (III.J (2.3)),
so $P_5(\Phi(U))$ lies in the partially polyhomogeneous space with exponents in $\Lambda+2$ whose coefficients below
$5+\epsilon_+$ vanish, and its $\mathcal F^k_\epsilon$-norm is the sum of the norms of the remaining coefficients and of
the remainder, each a finite sum of products bounded by Lemma 2.4, the weights adding as in the proof of (2.5). The
linear terms $L_bh$ keep the loss of $h$, which is why no weight is gained. The second derivative is bilinear with two
factors at the low norm. $\square$

**Remark 4.4 (what remains for section 13).** II.G Theorem 2.1 asks, on one pair of Banach scales: (i) smoothing
operators on the spaces of $\mathcal D$ (II.G Proposition 3.1 and the source's p. 322); (ii) the tame forward map
(Proposition 4.3) with $\Phi(U\cap B_\eta)\subset F_\eta$; and (iii) tame right inverses (Theorem 4.2) for every $U$ in
a neighbourhood of 0, so at $b\ne b_0$ too, with $\Psi(u)F_\eta\subset B_\eta$ for $u\in U\cap B^\infty_\eta$ (II.G
Theorem 2.1 (ii)-(iii) as amended in D304, (H10), in its notation; the source meets these support conditions by finite
speed of propagation, Step 3 (3), p. 322). Remaining: one pair of scales, Proposition 4.3 mapping $\mathcal D_\epsilon$
to $\mathcal F_\epsilon$ and Theorem 4.2 mapping $\mathcal F_{\epsilon'}$ to $\mathcal D_\epsilon$ ((J$''$4)); (J$'$3),
the linear theory and its tame form at $b\ne b_0$; the support conditions; the smoothing operators; and the exterior
family $h_{-S}$ (III.C$'$).

## 5. Findings, labels and sources

(J$''$1) *The propagation of tameness is proved, not asserted.* The source's Remark 11.13 asserts it, and Corollary
11.66 and Theorem 12.8 state the tame estimate without proof. Here the calculus of section 1, the finite-order forms of
section 2 and the inventory of section 3 prove it at $b_0$.

(J$''$2) *Two model maps need care at finite order.* II.G$'$ Corollary 4.5 loses $\lceil k\delta\rceil+\ell$; the loss
is bounded in $k$ only through strong trapping admissibility, which at $n = 4$ is proved at $b_0$ (III.F Proposition
4.1). Near $b_0$ it holds on a neighbourhood that shrinks with $k$ (III.H$'$ (H$'$3)), so the tame form at $b\ne b_0$ is
part of (J$'$3). III.H Corollary 4.2 holds on $|\sigma|<c_k$ with $c_k$ depending on $k$; Remark 2.2 shows this costs
only constants.

(J$''$3) *Nine model statements are stated at order $\infty$*: III.G$''$ Theorem 4.2 and Corollary 4.3, III.G$''''$
Theorem 3.1 and Propositions 4.4 and 5.1, III.I$'$ Propositions 2.1 and 3.1, and III.I$''$ Lemmas 4.1 and 4.3. Their
finite-order forms (Lemma 2.1 (f)-(g)) rest on the finite-order statements III.G$'$ Theorem 3.1 (2), III.F$'$ Corollary
3.4, III.A Lemmas 1.2 and 3.2, II.G$'$ Corollaries 4.2 and 4.5, and III.H Proposition 3.2.

(J$''$4) *The weights need one pair of scales.* The spaces of III.I$''''''''''''''$ and III.J are "$w-$" spaces,
intersections over a loss. At a fixed loss the solution maps are shown to take the source at a loss $\epsilon'$ to the
solution at the loss $\epsilon\ge\epsilon'$ (section 1; III.J$'$ Lemma 1.1 records $5\epsilon$ at $\iota^+$ from its
level-2 margin $\epsilon$). The forward map takes $\mathcal D_\epsilon$ to $\mathcal F_\epsilon$ and gains nothing in
the weights (Proposition 4.3), so II.G Theorem 2.1, which asks one pair of Banach scales, needs
$\epsilon' = \epsilon$ for one $\epsilon$ and every $k$ (II.G (2.1) admits no loss varying with $k$): the inverse
without loss in the weights. The source states exactly this: its Theorem 12.8 (p. 312) takes $f$ at the
fixed weights $(4+\epsilon_I,5+\epsilon_+,4+\epsilon_K)$, and its proof takes $h'$ from Corollary 11.66 at
$(3+\epsilon_I,3+\epsilon_+,4+\epsilon_K)$. At $n = 4$ this is open. The route proposed for the next part is an
improvement to exact weights after the fact: at $\iota^+$ through $N_{\iota^+}$ on a line free of
$\mathrm{spec}_{\iota^+}$ (III.G$'$ Theorem 3.1 (2)) with the gap that (G$^+$) leaves about $3+\epsilon_+$; at $\mathscr
I^+$ through III.A Lemma 1.2 at weights that are not exponents; at $K^+$ through the low-energy estimates. Before the
$K^+$ step each minus at $K^+$ ($\alpha-$, $(\alpha-2)-$, $(\alpha-1)-$, and the $(3+\eta_2-2\epsilon-d_\rho)$ of
$Y_{\rho,\mathrm{rem}}$) is to be classified as a margin or a logarithm at the weight, and for a logarithm the shifted
weight named to which the source's fixed $4+\epsilon_K$ corresponds (verifier 126).
III.J$'''$ (D293) takes another route: each loss that reaches a final weight is removed where it arises, none is
improved after the fact, and its Corollary 6.6 discharges (J$''$4) at $b_0$ (proved, D296).

(J$''$5) *Smallness in one norm.* Every "small" of III.I-III.I$''''''''''''''$ is smallness in one fixed norm (Lemma
2.3); the orders $d_k$ of III.J$'$ Theorem 2.1 are not needed.

*Labels.* Theorem 4.1 is the source's tame estimate of Corollary 11.66; Theorem 4.2 that of Theorem 12.8; Proposition
4.3 its section 13.1, Step 3 (2); section 1, Lemmas 2.1, 2.3 and 2.4, Remark 2.2 and section 3 are new at $n = 4$ (the
source's Remark 11.13 in proved form).

*Sources.* [Hin26] p. 226 (Remark 11.13), pp. 294-295 (Corollary 11.66 and its tame estimate), p. 312 (Theorem 12.8),
pp. 321-322 (section 13.1, Step 3 (1)-(4)), read at source. Inputs: I.B (1.4); II.A Lemma 9.5, Corollary 9.7; II.F$'$
Theorem 1.1, Corollary 1.2; II.G Remark 2.2, Theorem 2.1, Proposition 3.1, Lemma 4.1; II.G$'$ Propositions 3.3, 3.5,
4.4, Corollaries 4.2, 4.5; III.A Lemmas 1.2, 3.2, Proposition 4.2; III.F Proposition 4.1; III.F$'$ Corollary 3.4;
III.G$'$ Theorem 3.1; III.G$''$ Theorem 4.2, Corollary 4.3; III.G$'''$ Proposition 2.4, Corollary 3.1, Proposition 3.7;
III.G$''''$ Theorem 3.1, Propositions 4.4, 5.1; III.H Proposition 3.2, Corollaries 4.2, 4.4; III.H$'$ (H$'$3); III.I
Propositions 3.4, 4.1, Theorem 5.3, Remark 5.5; III.I$'$-III.I$''''''''''''''$ as in section 3; III.J Theorem 2.4,
Remark 2.5; III.J$'$ Theorem 2.1.
