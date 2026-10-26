# Part III.J$''$. Tame estimates, n = 4 ([Hin26] Remark 11.13; the tame forms of Corollary 11.66 and Theorem 12.8)

*Status.* Written (D286). This part proves, at spatial dimension $n = 4$ and at the black hole parameters $b_0$, the
tame estimates that [Hin26] asserts in Remark 11.13 (p. 226), states for Corollary 11.66 (pp. 294-295) and Theorem 12.8
(p. 312) without proof, and uses in section 13 (p. 321, Step 3 (2)-(3)): the tame form of III.I$''''''''''''''$ Theorem
3.1 (Theorem 4.1) and of III.J$'$ Theorem 2.1 (Theorem 4.2), and the tame bounds of the map $U\mapsto P_5(\Phi(U))$
(Proposition 4.3). It discharges (J$'$2) of III.J$'$ at $b_0$; (J$'$3), the linear theory at $b\ne b_0$, stays open.

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
of the remainder; finite-dimensional spaces ($E^k = E$); and direct sums. Each statement of those parts is made in
$E^\infty$, at a loss $\epsilon>0$ in the orders read "$w-$" that is fixed in it; its order-$k$ space is meant below.

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

*Proof.* (a) is immediate, the norms being non-decreasing in $k$. (b) By (1.1) for $S$ and then for $T$,
$$\|S_\beta T_\beta e\|_k\le C_k\big(\|T_\beta e\|_{k+d'}+\|\beta\|_{k+d'}\|T_\beta e\|_{d'}\big)\le
C_k\big(\|e\|_{k+d+d'}+\|\beta\|_{k+d+d'}\|e\|_d+\|\beta\|_{k+d'}(\|e\|_{d+d'}+\|\beta\|_{d+d'}\|e\|_d)\big),$$
and $\|\beta\|_{d+d'}\le\|\beta\|_{d_0}<1$, $\|\beta\|_{k+d'}\le\|\beta\|_{k+d+d'}$ and $\|e\|_d\le\|e\|_{d+d'}$ give
(1.1) with loss $d+d'$. (c) $\|\sum_i(\ell_\beta e)_iv^i_\beta\|_k\le C\|e\|_d\sum_i\|v^i_\beta\|_k\le
C_k\|e\|_d(1+\|\beta\|_{k+d})$, which is at most the right side of (1.1). (d) is (1.1) without its second term. (e)
follows from (b) by induction. $\square$

## 2. The elementary families

**Lemma 2.1 (the elementary tame families).** For $d_0$ large and $\delta_0$ small the following are tame, with losses
independent of $k$.

(a) (*Forward solutions.*) The forward solution operators of the operators $L^{g,g_0}$, $g = g_0+\tilde h$, used in
III.I-III.I$''''''''''''''$: $\tilde h = h$ (III.I Theorem 5.3), $\tilde h = h+h^{(-1)}(S)$ and $h+h_{\mathrm{tot}}(\vec
p)$ with the gauge modifications $\delta^*_{g_0,E_C}\vartheta_{\mathrm{tot}}(\vec p)$ ($L_{h,S}$ of III.I$''''$,
$L_{h,\vec p}$ of III.I$'''''''$-III.I$'''''''''$), and $\tilde h = h+h_{\mathrm{rem}}(q)+h_{\mathrm{tot}}(\vec p)$
(III.I$''''''''''''''$ Theorem 3.1, Step 0), between the spaces of III.I (5.1) and its target. For $\tilde h = h$ this
is III.I (5.2). In general $\tilde h$ lies in the class of III.I Theorem 5.3 ($h_{\mathrm{rem}}(q)$ has $K^+$-order
$(\alpha-2)->2$, III.I$''''''''''''''$ Remark 3.2 (1)), with $\|\tilde h\|_{\mathcal X^k}\le C_k\|\beta\|_{k+d}$
(III.I$''''$ Lemma 2.5, III.I$'''''''$ Lemma 2.5, III.I$''''''''$ Lemma 2.5, III.I$'''''''''$ Lemma 2.5, and
III.I$''''''''''''''$ Definition 1.2 with the towers fixed), and the gauge terms add to $P-P_0$ coefficients smooth in
$\vec p$; so III.I Theorem 5.3's proof gives $\|P-P_0\|_{(0;k+d)}\le C_k\|\beta\|_{k+d+5}$ and (5.2) with $\|\beta\|$
for $\|h\|$.

(b) (*Background coefficients.*) $u\mapsto(L^{g,g_0}-L_{b_0})u$, $u\mapsto R_qu$, $\Delta_q$, the sources $f^S_{h,\vec
p}$, $f^b_{h,\vec p}$, $f^{\mathrm s1}_{h,\vec p}$, $f^\nu_{h,\vec p}$, $r^\nu_{h,\vec p}$, $L_bh_{\mathrm{rem}}(q)$ and
the remainder $\tilde L$ of III.I$'$ Lemma 1.1, between the weighted spaces of III.I Proposition 4.1 (4.2),
III.I$'''''''''$ Lemma 2.6 and III.I$''''''''''''''$ Lemmas 2.2-2.4. Each is a b-differential operator of order at most
2 whose coefficients are polynomial in the background, $g^{-1}$ and their derivatives (or such a coefficient applied to
a fixed section); by II.A Corollary 9.7 and Lemma 9.5, with II.G Lemma 4.1 for the nonlinear functions of the
background, $\|Au\|_k\le C_k(\|u\|_{k+2}+\|\beta\|_{k+d}\|u\|_{d})$ for $\|\beta\|_{d_0}$ small, the weights adding as
in the cited membership statements.

(c) (*Finite-dimensional algebra and coefficients.*) The inverses $(S^{(-1)}_{h,S})^{-1}$ (III.I$''''$ Corollary 4.3),
$(S^{(-1)}_{h,\vec p})^{-1}$ (III.I$'''''''$ Corollary 4.6), $T_{h,\vec p}^{-1}$ (III.I$''''''''$ Proposition 4.1,
III.I$'''''''''''$ Theorem 4.1), $(-\mathrm{id}+A_k)^{-1}$ and the inverse of $C^{\mathrm{rot}}$ in $\vec
W'^{\mathrm{rot}}$ (III.I$''''''''''''''$ Theorem 3.1, Steps 3 and 4'), and $(z-\frac32-\bar A)^{-1}$ (III.I$'$
Proposition 3.1): bounded on $\mathcal B$ by the cited statements (close to $\pm\mathrm{id}$, or fixed). The coefficient
functionals ($\dot S$, $S_\nu$, $C^{k+1}_\nu$, $C^{\mathrm{rot}}$, the dual functionals of III.I$''''''''''''''$ Step
4', the $t_*$-coefficients at $K^+$): bounded by a fixed low norm of the solution they are applied to, by the cited
statements and III.I$''''''''''''$ Lemma 2.3 (a). The finite-dimensional states, rows $m_\nu$, towers $T_{\rho,b_0}$ and
states of III.I$''''''''''''''$ Lemma 2.1 they are paired with are fixed smooth sections. So, composed with tame
families, they give tame families by Lemma 1.2 (b)-(c).

(d) (*Integrations along faces.*) III.A Lemmas 1.2 and 3.2 and III.I$''$ Lemma 2.1: order $k$ to order $k$ (loss 0), as
stated; III.I$''$ Lemma 3.1: loss $\ell$, independent of $k$, as stated.

(e) (*Transforms and the low and middle frequencies.*) III.A Proposition 4.2 (1) (Fourier transform, loss $l$), II.G$'$
Proposition 3.3 (1) (loss 1), Proposition 3.5 (loss $\ell$) and Corollary 4.2 (2) (loss $j+\ell$ for
$\partial^j_\sigma$, $j$ fixed by the weights), III.H Proposition 3.2 ($\widetilde{L_b}(0)^{-1}$, loss 1), III.H
Corollary 4.2 (on $|\sigma|<c_k$, no loss) and III.I$''$ Lemma 4.2 (loss $\ell$): as stated, at every order with the
loss independent of the order.

(f) (*High frequencies.*) II.G$'$ Corollary 4.5 loses $\lceil k\delta\rceil+\ell$, $\delta = \delta_\Gamma(-\eta)$, with
$\ell$ fixed before $k$. At $b_0$, $2L_{b_0}$ is strongly trapping admissible (III.F Proposition 4.1): for every $k$ the
trapping data can be chosen with $(k+1)\delta_\Gamma(-\eta)\le1$ (III.H$'$ (H$'$3), II.G$'$ after Proposition 4.4), and
then the loss at the order $k$ is at most $\ell+1$. III.I$''$ Lemma 4.1 composes this with (e) and the invertibility of
III.H Corollary 4.4 on the middle frequencies; it has loss at most $\ell+1$ plus the losses of (e).

(g) (*Model inverses stated at order $\infty$.*) Each of the following holds at every order $k$ with a loss independent
of $k$, by its own proof, read at the order $k$:

- III.G$'$ Theorem 3.1 (2): $N_{\iota^+}(\lambda)^{-1}$ has the loss $d$ at every $k$, as stated, finite-meromorphic in
$\lambda$ with principal parts independent of $k$. III.G$''$ Theorem 4.2 and Corollary 4.3 compose it with a contour
integral over a fixed circle on which $\lambda\notin\mathrm{spec}_{\iota^+}(\bar L)$ (bounded at each order, uniformly
on the circle), with the towers at $b_0$ (fixed sections paired with finitely many coefficients) and with $L_b$ (loss
2): loss $d+2$. The same holds for III.G$'''$ Corollary 3.1, Proposition 2.4 and Proposition 3.7, whose fixed losses
III.J's proof of Theorem 2.4 records ((GIII.G$'''$4), loss $l$). - III.F$'$ Corollary 3.4:
$N_{\mathrm{tf}}(\widehat{L_b},\pm1)^{-1}$ has the loss $\ell$ at every $k$, as stated. III.G$''''$ Theorem 3.1 and
Propositions 4.4 and 5.1 compose it with $\widetilde{L_b}(0)^{-1}$ ((e)), cut-offs, a Mellin inversion on a fixed
vertical line not crossing a root (bounded at each order), and finitely many rounds whose number is fixed by the weights
(each raises the order by at least $\epsilon_{\mathrm{ind}}-\epsilon$): fixed loss. - III.I$'$ Propositions 2.1 and 3.1:
compositions of (d), of $(z-\frac32-\bar A)^{-1}$ ((c)) and of $\tilde L$ ((b), loss 2), in finitely many steps whose
number is fixed by $\ell_I$, $\ell_+$ and the index sets: fixed loss. - III.I$''$ Lemma 4.3: $\hat b\mapsto\chi G_1(\hat
b)$, $\hat S\mapsto\chi G_2(\hat S)$ multiply finite-dimensional data by fixed sections built from the states: loss 0.

*Proof.* (a)-(c) are proved in their statements. (d) and (e) are the cited statements, each of which is stated at every
order with the loss independent of it. (f): II.G$'$ Corollary 4.5 fixes $\ell$ before $k$; III.H$'$ (H$'$3) states that
$(k+1)\delta_\Gamma(-\epsilon)\le1$ is what the order $k$ needs, and that at $b_0$ it can be met for every $k$ (strong
trapping admissibility, III.F Proposition 4.1); II.G$'$'s remark after Proposition 4.4 records the same for
$\gamma_+\le0$. (g): each statement is a finite composition of maps of (b)-(e) and of the two face inverses cited, at a
fixed number of steps; Lemma 1.2 (e) applies with $\beta$ absent. $\square$

**Remark 2.2 (choices that depend on the order).** In (e)-(f) two choices depend on $k$: the radius $c_k$ of the
low-energy cut-off, and the trapping data. Both enter only decompositions $u =
u_{\mathrm{hi}}+u_{\mathrm{reg}}+u_{\mathrm{sing}}$ (and their analogues) of a solution $u$ that does not depend on
them, used to show that $u$ lies in a better-weighted space; at the order $k$ the decomposition made with the order-$k$
choices gives the order-$k$ bound. So the choices change the constants $C_k$, which may depend on $k$, and not the
losses.

## 3. The inventory

Each construction of III.I-III.I$''''''''''''''$ and of III.J$'$ is a composition, in a fixed number of steps, of the
families of Lemma 2.1; the table lists them. FWD is Lemma 2.1 (a), BG (b), FIN (c), INT (d), MOD (e)-(g); a loop's
length is fixed by the weights and orders of the statement, never by $k$.

| Part | statement | maps used | steps |
|---|---|---|---|
| III.I | Theorem 5.3 | FWD (II.F$'$ Corollary 1.2) | 1 |
| III.I | Remark 5.5 | FWD, BG ((4.2)), MOD (the stationary inverses below) | the rewritings $L_bu = f-(L^{g,g_0}-L_b)u$, finitely many |
| III.I$'$ | Propositions 2.1, 3.1 | INT, FIN, BG ($\tilde L$) | finitely many, fixed by $\ell_I$, $\ell_+$ |
| III.I$''$ | Proposition 5.1 | FWD (III.I), BG, MOD (III.I$'$ Proposition 3.1; Lemmas 2.1, 3.1, 4.1-4.3) | rounds raising $\alpha'_K$ by $\min(a_K-2,\alpha_K-\alpha'_K)$ |
| III.I$'''$ | Proposition 2.1 | FWD (III.I$''$), BG, MOD (III.I$'$ Propositions 2.1, 3.1; III.H Proposition 3.2; III.I$''$ Lemmas 3.1, 4.1-4.3), FIN (the coefficient $S_0$) | 1 |
| III.I$''''$ | Proposition 4.1, Lemma 4.2, Corollary 4.3 | FWD (III.I$'''$), BG ($h^{(-1)}(S)$, $f_{h,S}$), FIN ($\dot S = \Pi f'$, $(S^{(-1)}_{h,S})^{-1}$) | 1 |
| III.I$'''''$ | Proposition 2.1, Corollary 2.2 | FWD (III.I$''''$), BG, MOD (III.I$'$; III.G$''$ Corollary 4.3; III.H Proposition 3.2), FIN | exponents in a window, and rounds raising $\alpha'_K$ to $\alpha_K$ |
| III.I$''''''$ | Lemmas 1.2-1.4, Proposition 2.1 | FWD (III.I$'''''$), MOD (III.A Proposition 4.2; $\widetilde{L_b}(\sigma)^{-1}$ by III.I$''$ Lemma 4.2; III.H Proposition 3.2; III.G$''''$ Proposition 5.1; II.G$'$ Proposition 3.5 (1)), FIN | 1 |
| III.I$'''''''$ | Lemmas 4.1, 4.3, 4.5, Corollary 4.6 | FWD, BG, FIN | 1 |
| III.I$''''''''$ | Lemmas 3.1-3.3, Proposition 4.1 | FWD, BG, MOD (III.I$'$; III.G$''$ Corollary 4.3; III.G$''''$ Proposition 5.1; III.H Proposition 3.2), FIN | levels $\alpha_0<\dots<\alpha_N$ (fixed by $\alpha$, $a_K$); tf rounds $i_0$ |
| III.I$'''''''''$ | Definition 2.1, Lemmas 2.4, 2.6 | BG ($m_\nu$, $h_\nu$, $\vartheta_\nu$, $f^\nu$, $r^\nu$), FWD of $L_{b_0}$ | none |
| III.I$''''''''''$ | Proposition 3.1 | FWD (III.I$'$ Proposition 3.1), MOD (III.G$''$ Corollary 4.3), FIN | windows, at most $N_*$ |
| III.I$'''''''''''$ | Lemmas 2.1-2.5, Proposition 3.1, Lemma 3.2, Theorem 4.1 | MOD ($\widetilde{L_{b_0}}(0)^{-1}$; III.G$''''$ Propositions 4.4, 5.1; III.I$''$ Lemma 4.2; III.A Proposition 4.2), BG (columns), FIN, FWD | rounds rising by $\epsilon_{\mathrm{ind}}$; the level-3 loop |
| III.I$''''''''''''$ | Lemmas 2.1-2.4, Theorem 3.1 | FWD, MOD (as III.I$'''''''''''$), BG, FIN | pairs removed, finitely many |
| III.I$'''''''''''''$ | Proposition 2.1, Lemma 2.2 | as III.I$'''''''''''$-III.I$''''''''''''$ at each level $\beta$ | as there |
| III.I$''''''''''''''$ | Theorem 3.1 | FWD ($L_{h+h_{\mathrm{rem}}(q),\vec p}$), BG ($R_q$, $\Delta_q$), FIN, and III.I$''''''''$, III.I$'''''''''''$-III.I$'''''''''''''$ | levels $\beta_0<\dots<\beta_K$ (fixed by $\alpha$, $\alpha_1$) |
| III.J$'$ | Theorem 2.1 | III.I$''''''''''''''$ Theorem 3.1 at $\Phi(U)$; MOD (III.G$'''$ Proposition 3.7; the $t_*^{-\lambda_0}$-terms); BG ($D_U\Phi$) | the exponents of $\Lambda_*$, finitely many |

## 4. The theorems

**Theorem 4.1 (the tame form of III.I$''''''''''''''$ Theorem 3.1; the source's Corollary 11.66, its tame estimate).**
There are $d,d_0\in\mathbb N$ and $\delta_0>0$ such that for $b = b_0$ and $(h,\vec p,q)$ with $\|h\|_{\mathcal
X^{d_0}}+|\vec p|+\|q\|_{\mathcal Q^{d_0}}<\delta_0$ the maps $F\mapsto(h',\vec p\,',q')$ of III.I$''''''''''''''$
Theorem 3.1 satisfy, for every $k\in\mathbb N_0$,
$$\|h'\|_k+|\vec p\,'|+\|q'\|_k\le C_k\Big(\|F\|_{k+d}+\big(\|h\|_{k+d}+|\vec p|+\|q\|_{k+d}\big)\|F\|_d\Big),\tag{4.1}$$
with $\|h'\|_k$ the norm of the order-$k$ space of III.I$''''''''''''''$ (3.2), $\|q'\|_k$ that of $\mathcal Q^k$
(III.I$''''''''''''''$ (1.1)) and $\|F\|_{k}$ that of the order-$k$ version of $\mathcal Y^\natural(\alpha-)$. The same
holds for the solution maps of III.I-III.I$'''''''''''''$ in their spaces.

*Proof.* By induction over the parts in their order. Each part's solution map is, by the table of section 3, a
composition of a fixed number of the families of Lemma 2.1 and of the solution maps of earlier parts, which are tame by
the induction; each loop has a length fixed independently of $k$. Lemma 1.2 (b)-(e) gives a tame family with a loss $d$
equal to the sum of the losses, independent of $k$, for $d_0\ge d$ and $\delta_0$ small. For III.I$''''''''''''''$
Theorem 3.1 the background is $\beta = (h,\vec p,q)$, and (1.1) is (4.1). $\square$

**Theorem 4.2 (the tame form of III.J$'$ Theorem 2.1; the source's Theorem 12.8, its estimate).** There are $d,d_0$ and
$\epsilon_0>0$ such that for $U\in\mathcal D^\infty$ with $b = b_0$ and $\|U\|_{\mathcal D^{d_0}}<\epsilon_0$, the
solution $U'$ of III.J$'$ (2.1) satisfies, for every $k$,
$$\|U'\|_{\mathcal D^k}\le C_k\big(\|f\|_{\mathcal F^{k+d}}+\|U\|_{\mathcal D^{k+d}}\|f\|_{\mathcal F^d}\big).\tag{4.2}$$

*Proof.* Step 0 of III.J$'$ applies Theorem 4.1 at the background $\Phi(U)$, with $\|\Phi(U)\|_k\le C_k\|U\|_{\mathcal
D^{k+d}}$ (III.J Theorem 2.4) and $\|\Phi(U)\|_{d_0}$ small for $\|U\|_{\mathcal D^{d_0+d}}$ small; composed with
$U\mapsto\Phi(U)$, (4.1) has the form (1.1) in the background $U$. Steps 1-3 subtract $D_U\Phi(U'_\bullet)$ for finitely
many $U'_\bullet$: the finite-dimensional data of Step 1 and of Case B of Step 2 (bounded by a low norm of $(h',\vec
p\,',q')$, Lemma 2.1 (c), with the fixed right inverse of III.G$'''$ Proposition 3.7 on the finitely many
$\lambda_0\in\Lambda_*$, Lemma 2.1 (g)), and the conormal remainders of Step 3 (extracted by fixed maps). $D_U\Phi(U') =
D\Phi_0(U_0)U'_0+(DA(U_0)U'_0)U_1+A(U_0)U'_1$ (III.J Remark 2.5): the first and third terms are tame in $U'$, uniformly
in $U_0$ small (III.J Theorem 2.4), and the second is bounded by $C|U'_0|\|U_1\|_{\mathcal D^{k+d}}$, of the form (1.1)
as $|U'_0|$ is bounded by a low norm of $f$. Lemma 1.2 gives (4.2). $\square$

**Proposition 4.3 (the forward map; the source's section 13.1, Step 3 (2)).** There are $d$ and $\epsilon_0$ such that
for $b$ near $b_0$ and $U\in\mathcal D^\infty$ with $\|U\|_{\mathcal D^{3d}}<\epsilon_0$, $\|P_5(\Phi(U))\|_{\mathcal
F^k}\le C_k(1+\|U\|_{\mathcal D^{k+d}})$ for $k\ge d$, and the first and second derivatives of $U\mapsto P_5(\Phi(U))$
satisfy II.G (2.3) with the norms of $\mathcal D^{3d}$ and $\mathcal F^{2d}$.

*Proof.* $\Phi$ is affine in $U_1$ with coefficients smooth in the finite-dimensional $U_0$, and tame (III.J Theorem
2.4). $P_5(h,\vec p,q) = P_4(h+h_{b,\mathrm{rem}}(q),\vec p)$ is $\mathrm{Ric}-\delta^*\Upsilon$ of a metric that is a
smooth function of $\vec p$ plus $h+h_{b,\mathrm{rem}}(q)$, so a smooth function of $(h,\partial h,\partial^2h)$ and of
$q$ with coefficients smooth in $\vec p$; II.G Lemma 4.1 (with II.A Lemma 9.5) bounds it and its first two derivatives
tamely in the b-Sobolev norms. The weights are those of III.J (2.5), which holds at every $b$ near $b_0$ (D285): the
terms of $u$-exponent below $3+\epsilon_+$ cancel identically (III.J (2.3)), and every remaining term is a product of
factors each bounded tamely in its weighted norm, the weights adding as in the proof of (2.5); the second derivative is
bilinear with two factors at the low norm. $\square$

**Remark 4.4 (what remains for section 13).** II.G Theorem 2.1 asks (i) smoothing operators on the spaces of $\mathcal
D$ (II.G Proposition 3.1 and the source's p. 322), (ii) the tame forward map (Proposition 4.3) and (iii) tame right
inverses (Theorem 4.2) for every $U$ in a neighbourhood of 0, so at $b\ne b_0$ too. Theorem 4.2 is at $b_0$: (J$'$3)
remains, together with the exterior family $h_{-S}$ (III.C$'$).

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

*Labels.* Theorem 4.1 is the source's tame estimate of Corollary 11.66; Theorem 4.2 that of Theorem 12.8; Proposition
4.3 its section 13.1, Step 3 (2); section 1, Lemma 2.1, Remark 2.2 and section 3 are new at $n = 4$ (the source's Remark
11.13 in proved form).

*Sources.* [Hin26] p. 226 (Remark 11.13), pp. 294-295 (Corollary 11.66 and its tame estimate), p. 312 (Theorem 12.8),
pp. 321-322 (section 13.1, Step 3 (1)-(4)), read at source. Inputs: II.A Lemma 9.5, Corollary 9.7; II.F$'$ Corollary
1.2; II.G Remark 2.2, Theorem 2.1, Proposition 3.1, Lemma 4.1; II.G$'$ Propositions 3.3, 3.5, 4.4, Corollaries 4.2, 4.5;
III.A Lemmas 1.2, 3.2, Proposition 4.2; III.F Proposition 4.1; III.F$'$ Corollary 3.4; III.G$'$ Theorem 3.1; III.G$''$
Theorem 4.2, Corollary 4.3; III.G$'''$ Proposition 2.4, Corollary 3.1, Proposition 3.7; III.G$''''$ Theorem 3.1,
Propositions 4.4, 5.1; III.H Proposition 3.2, Corollaries 4.2, 4.4; III.H$'$ (H$'$3); III.I Propositions 3.4, 4.1,
Theorem 5.3, Remark 5.5; III.I$'$-III.I$''''''''''''''$ as in section 3; III.J Theorem 2.4, Remark 2.5; III.J$'$ Theorem
2.1.
