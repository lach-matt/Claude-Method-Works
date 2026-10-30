# Part III.I$'''''''''''''''$. The linear theory at base points near $b_0$, n = 4 ([Hin26] sections 11.2-12 at black
hole parameters $b\ne b_0$)

*Status.* Written (D297). The parts III.I$'$-III.I$''''''''''''''$ and III.J-III.J$'''$ prove the linear theory at base
points whose black hole parameter is $b = b_0$, with derivatives in $b$ taken at $b_0$; III.I Remark 5.4 and (I3) of
III.I recorded why. III.H$''$ supplied the two inputs that were missing for $b\ne b_0$ (its Corollary 5.1) and recorded
the rest as (H$''$5). This part proves that rest. At every base point $(h,\vec p)$, or $(h,\vec p,q)$, or $U$, whose
black hole parameter is $b\in\mathcal B_*$ ($\mathcal B_*$ of III.H$''$), the statements of those parts hold with
constants uniform in $b$. *The statement at $b$* of each of them is obtained as follows: $L_{b_0}$, $g_{b_0}$ near
$K^+$, the states, towers and companions at $b_0$, and the index set $\mathcal E_{\mathrm{ind}}$ are replaced by those
at $b$; derivatives in $b$ are taken at $b$; and the v1 terms are treated by section 2. This closes (J$'$3) of III.J$'$,
and with it (I3) and (H$''$5).

*What n = 4 changes.* At $b_0$ every rotation is Killing. At a rotating $b$ only the rotations commuting with the spin
are, and the rotation state $h_{b,\mathrm v1}$ is $O(|b-b_0|)$ but not zero (III.E$'$). The v1 terms of exponent of real
part at most 2 then decay at $K^+$ one order less than at $b_0$, below the levels' target $\alpha-2$. An elimination
through their $K^+$-coefficients would invert $V\mapsto h_{b,\mathrm v1}(V)$, a map that degenerates as $b\to b_0$. As
in the source ([Hin26] pp. 279-280, "for a suitable $V^{(1,0)\prime}\approx\dot V$"), they are assigned directly: the
coefficient of the rotation row is read from the construction that produced the term, the $\iota^+$-data of the graft or
the tf-data of the spectral pieces. No $K^+$-coefficient is inverted (Proposition 2.2). The rotation rows of
III.I$''''''''''''''$ Definition 1.3, whose coefficient space is all of $\mathcal V_1$, are what makes this possible;
III.I$''''''''''''''$ introduced them for the same reason (its "What n = 4 changes" (3)). The rest transfers by
continuity in $b$, and the joint injectivity of the states, proved at $b_0$ by spherical symmetry, by perturbation
(Lemma 1.2).

## 1. The model at $b$

**Lemma 1.1 (the model objects at $b$).** For $b\in\bar{\mathcal B}_*$, uniformly in $b$:

(P1) III.I Theorem 5.3 holds at $b$, with continuity in $(b,S,h)$ (III.H$''$ Corollary 5.1), and so do III.I
Propositions 3.3-3.4, 4.1, Corollaries 4.2, 5.2 and Lemma 3.6, which are stated for $g_0 = g_{b_0,b,-S}$ with $|b-b_0|$
small.

(P2) $N_{\iota^+}(2L_b) = N_{\iota^+}(2\bar L)$ (III.H$''$ Lemma 3.2), so $\mathrm{spec}_{\iota^+}$, III.G$'$ Theorem
3.1 and III.G$'''$ do not depend on $b$; III.G$''$ Theorem 4.2 and Corollary 4.3 are stated for general $b$ (with the
$K^+$-towers of $L_b$); the tf-normal operator does not depend on $b$ (III.G$''''$ Lemma 1.1); and the indicial roots of
III.F$'$ Proposition 2.3 do not depend on $b$, the normal operator of $\widehat{L_b}(0)$ at $\partial X$ being that of
$2\bar L$ (III.F Lemma 2.1 (3)).

(P3) The states of III.G$''$ Table 1.1 for $L_b$, their companions, the 1-form towers of III.D$'''$, the physical states
of III.F$''''$ and $\dot g_b$ are smooth in $b$, with leading terms at $\partial X$ that do not depend on $b$ and with
index sets in $(\mu-j)+\mathcal E_{\mathrm{ind}}$, $\mathcal E_{\mathrm{ind}}$ independent of $b$; the rotation state
$h_{b,\mathrm v1}\in\mathcal A^3$ is smooth in $b$ and vanishes at $b_0$ (III.I$''''''''''''''$ Lemma 2.1).

(P4) III.H Corollaries 4.2-4.4 and III.H$'$ Theorem 1.3 hold at $b$ (III.H$''$ Theorem 2.1 and its compactness
paragraph), and III.G$''''$'s propositions hold at $b$, their inputs being the tf-normal operator (P2), the zero energy
states (P3) and III.H.

(P5) The time translation $\partial_{t_*}$ is Killing for $g_b$, so every statement that uses only that the s0 gauge
1-form $\omega^{(0)}_{b,\mathrm s0}$ is Killing (as III.I$'''''''''$ section 2 and III.I$''''''''''$ Lemma 2.1 do) holds
at $b$.

(P6) The corrections #4 of III.I$'''''''''$ Definition 2.1 are built from the 1-forms at $b_0$, as the source's
Definition 11.55 builds them ([Hin26] p. 275), at every base point; the row identities of III.I$'''''''''$ Lemmas
2.2-2.6 hold with $L_{h,\vec p}$ at a base point with parameter $b$, their errors $L_{h,\vec p}-L_{b_0}$ near $K^+$
being replaced by $L_{h,\vec p}-L_b$, which vanishes near $K^+$ to the order of $h$ (there $g_0 = g_b$, III.I Lemma
3.6), plus $(L_b-L_{b_0})$ applied to $b_0$-tensors, of size $O(|b-b_0|)$ and of the $K^+$-order of those tensors plus 2.

*Proof.* (P1)-(P4) are the cited statements. (P5): $g_b$ is stationary. (P6): the corrections are fixed tensors built at
$b_0$, and the identities of III.I$'''''''''$ section 2 are computations with $L_{h,\vec p}$ applied to them; at a base
point with parameter $b$, $L_{h,\vec p} = L_b+(L_{h,\vec p}-L_b)$ near $K^+$, and $L_b-L_{b_0}$ is a stationary operator
with coefficients $O(|b-b_0|)$ that gains two orders at $K^+$ relative to the order of its argument, as $L_b$ and
$L_{b_0}$ are both 3b-operators of weight $\rho_K^2$ there (II.C Lemma 1.4 (b) for the stationary models). $\square$

The last clause of (P6) needs a remark. A correction of III.I$'''''''''$ is a stationary or polynomial-in-$t_*$ tensor
near $K^+$, cut off by $\chi_K$; $L_b$ applied to a $b_0$-tower is not small at $K^+$ relative to the tower, only
$O(|b-b_0|)$ times it. The source makes the same choice (its corrections are at $b_0$, its operator at $b$) and accounts
for the difference as a source term of the order of the tower plus 2. Where III.I$'''''''''$-III.I$''''''''''''''$ use
that the source term $L_{h,\vec p}m_\nu$ of a row has $K^+$-order above the target, the row is built at the base point's
$b$ (the towers $T_{\rho,b}$ of III.I$''''''''''''''$ Definition 1.2, smooth in $b$ by (P3)); where they use a
correction built at $b_0$, its error at $b$ is $L_b$ of a tower of the same exponent, which lies in the same classes as
at $b_0$ with an extra factor $O(|b-b_0|)$. The row identities of III.I$'''''''''$ Lemma 2.6 at $b$ are stated with the
rows $m_\nu$ at $b$, and the corrections $h_\nu$, $\vartheta_\nu$ at $b_0$, as the source does.

**Lemma 1.2 (joint injectivity at $b$).** Shrinking $\mathcal B_*$, III.I$''''''''''$ Lemma 2.2 and Corollary 2.3 hold
at every $b\in\bar{\mathcal B}_*$, for the states at $b$: if $\sum_{\tau\ne\mathrm v1}h_{b,\tau}(W_\tau) = 0$ then every
$W_\tau = 0$; and a finite sum of rows $\nu\ne\mathrm v1$ at $b$ with $K^+$-weight above their rates vanishes. Moreover,
there are a compact $\mathcal K_0\subset X^\circ$ and $c>0$, independent of $b$, with $\sup_{\mathcal K_0}|\sum_\tau
h_{b,\tau}(W_\tau)|\ge c\sum_\tau|W_\tau|$.

*Proof.* The space $\mathcal W := \bigoplus_{\tau\ne\mathrm v1}\mathcal W_{\tau,\mathbb C}$ is finite-dimensional. At
$b_0$ the map $\Theta_{b_0}: W\mapsto\sum_\tau h_{b_0,\tau}(W_\tau)$ is injective (III.I$''''''''''$ Lemma 2.2). Each
nonzero element of its range is a nonzero smooth tensor on $X^\circ$, nonzero on an open set, so by compactness of the
unit sphere of $\mathcal W$ there is a compact $\mathcal K_0\subset X^\circ$ on which $\sup_{\mathcal
K_0}|\Theta_{b_0}W|\ge2c|W|$. $\Theta_b$ depends continuously on $b$ in $C^0(\mathcal K_0)$ (P3), so the bound with $c$
holds for $b$ near $b_0$. Corollary 2.3's proof uses only Lemma 2.2 and III.I$'''''''''$ Lemma 2.2 (e), the $K^+$-weight
$\mathrm{Re}\,e_\nu+1-\epsilon$ of $m_\nu(W)-\chi_Kr_\nu h_\tau(W)$, which is a computation with the tower relations and
holds at $b$ (P3). $\square$

v1 stays excluded at $b$, as at $b_0$. At a rotating $b$, $h_{b,\mathrm v1}(V)$ is a nonzero element of
$\ker\widehat{L_b}(0)$ in III.H's space $\mathcal X_0$ (it is $\delta^*_{g_b}$ of a 1-form in $\ker\Box^\Upsilon_b$,
III.D$''$ (3.4)). The nullspace has the same dimension near $b_0$ as at $b_0$ (III.H Proposition 3.2's proof: the matrix
$B(b)$ of the nullspace in continuous bases is invertible), so $h_{b,\mathrm v1}(V)$ lies in the span of the continuous
basis: the v1 states are not independent of the others at $b$. This is why their coefficients are assigned in section 2
and not read from the $K^+$-expansion.

## 2. The rotation rows at $b$

Let $\mathcal N_{\mathrm{rot}}$, $\mathcal M_{\mathrm{rot}} = \mathcal E_\sharp\cap\{\mathrm{Re}\le2\}$ and the rotation
rows $m_\nu$, $\nu = (\mathrm{rot},\lambda,k)$, be those of III.I$''''''''''''''$ Definitions 1.1 and 1.3, with the v1
tower $T_{\mathrm v1,b}$ at the base point's $b$: $m_\nu(W) = \chi_KT_{\mathrm v1,b}(a_\nu W)$, $a_\nu =
t_*^{-\lambda}(\log t_*)^k$, $W\in\mathcal V_{1,\mathbb C}$.

**Lemma 2.1 (rotation rows at $b$).** At $b\in\bar{\mathcal B}_*$, $m_\nu(W)$ has $K^+$-weight
$\mathrm{Re}\,\lambda-\epsilon$ (its bottom $a_\nu h_{b,\mathrm v1}(W)$, of size $O(|b-b_0||W|)$), and
$m_\nu(W)-\chi_Ka_\nu h_{b,\mathrm v1}(W)$ has $K^+$-weight $\mathrm{Re}\,\lambda+1-\epsilon$. III.I$'''''''''$ Lemmas
2.2 (a)-(e) and 2.4-2.6 hold for $\nu$ at $b$, with $e_\nu = \lambda$ and $\kappa_\nu = \mathrm{Re}\,\lambda+4$; in
particular $f^\nu_{h,\vec p}(W) := D_{\vec p}P_4(h,\vec p)(W_\nu = W) = L_{h,\vec p}m_\nu(W)+r^\nu_{h,\vec p}(W)$ lies
in $\mathcal Y_2(\alpha)$, uniformly in $b$.

*Proof.* As III.I$''''''''''''''$ Definition 1.3 states for $b_0$: the proofs of III.I$'''''''''$ Lemmas 2.2 (a)-(e) and
2.4-2.6 use the tower relations and not the coefficient space, and hold at $b$ by (P3) and (P6). The only change is the
bottom, which at $b_0$ vanishes and at $b$ is $a_\nu h_{b,\mathrm v1}(W)$; it has $K^+$-weight
$\mathrm{Re}\,\lambda-\epsilon$ and is $O(|b-b_0||W|)$ by (P3). The source term $L_{h,\vec p}m_\nu(W)$ involves only the
top of the tower, as $T_{\mathrm v1,b}$ solves $L_b$ to its length (the tower relations), so its $K^+$-order is
unchanged. $\square$

**Proposition 2.2 (the v1 terms are rotation rows with assigned coefficients).** Let $b\in\bar{\mathcal B}_*$ be the
black hole parameter of the base point.

(a) *The spacetime phase.* In III.I$''''''''''$ Proposition 3.1 at $b$, for each $u$-exponent $\lambda_0$ with
$\mathrm{Re}\,\lambda_0<2$ the graft's tower part $\chi_Ku^{(j)}_{b,0}$ (III.G$''$ (4.3) at $b$) equals
$$\sum_{\tau\in\mathcal T\setminus\{\mathrm
v1\}}m_{(\tau,\lambda_0,j)}(W^{(j)}_\tau)+m_{(\mathrm{rot},\lambda_0,j)}(V^{(j)})$$
up to $K^+$-weight $\mathrm{Re}\,\lambda_0+1-\epsilon$. Here $V^{(j)} := -\lambda_0^{-1}V^{(-1),(j)}_1$ is the graft's
v1 coefficient with the normalisation $a_{\mathrm v1} = -\lambda_0^{-1}t_*^{-\lambda_0}$ of III.G$''$ (4.2) (for the
$(\log t_*)^j$-versions, its $\lambda_0$-derivatives), read from the $\iota^+$-data $u_+$ by III.G$''$ Theorem 3.1. It
is linear and continuous in the source, uniformly in $b$. $(\lambda_0,j)\in\mathcal M\subset\mathcal M_{\mathrm{rot}}$,
so the rotation row exists. So III.I$''''''''''$ Proposition 3.1 (b) holds at $b$ with the rows $\mathcal
N_\iota\sqcup\mathcal N_{\iota,\mathrm{rot}}$ and these coefficients.

(b) *The spectral phase.* In III.I$'''''''''''$ Proposition 3.1 at $b$, the v1 term of III.I$'''''''''''$ Lemma 2.3's
(2.2), $c_{\mathrm v1}(\sigma)T_{\mathrm v1,b}(\sigma)$, now has the bottom $c_{\mathrm v1}(\sigma)h_{b,\mathrm v1}(Y)$,
and its rate is $\alpha_0$ (at $b_0$, $\alpha_0+1$). At level 1 ($2\le\mathrm{Re}\,\alpha_0<2+\eta_1$) this is below
$\alpha-2$ only for $\mathrm{Re}\,\alpha_0 = 2$ (by (G), no rate lies in $(2,2+\epsilon_K]$). Those exponents lie in
$\mathcal E_\sharp\cap\{\mathrm{Re} = 2\}\subset\mathcal M_{\mathrm{rot}}$, and the term is, by III.I$''''''''''''$
Lemma 2.1 (b), $m_{(\mathrm{rot},\alpha_0,k)}(Y')$ up to $K^+$-weight $\mathrm{Re}\,\alpha_0+1-\epsilon$, with $Y'$ the
coefficient that III.I$'''''''''''$ Lemma 2.3 gives the v1 tower: $Y$ times the constant of $c_{\mathrm v1}$, read from
the tf-data. It is linear and continuous in the source, uniformly in $b$ by (P2) and (P4). At level 2 the v1 rate is
$\alpha_0+1\ge2+\eta_1>2+\epsilon_K\ge\alpha-2$, as for the s0 and s2 towers there. So III.I$'''''''''''$ Proposition
3.1 holds at $b$ with the rows $\mathcal N_\sigma\sqcup\mathcal N_{\sigma,\mathrm{rot}}$ and these coefficients.

(c) *No other v1 term.* Every v1 coefficient of the expansion has its exponents in $\mathcal E_\sharp$
(III.I$''''''''''''$ Theorem 3.1: an $\iota^+$-exponent $\lambda$ of $u$ gives the coefficient $t_*^{-\lambda+d_\rho}$,
$d_{\mathrm v1} = 0$). So it either has real part at most 2, and is one of (a)-(b), or real part above
$2+\epsilon_K\ge\alpha-2$, and is carried by $q$ (III.I$''''''''''''''$ Definition 1.1, whose rates at a rotating $b$
are $\mathrm{Re}\,z>2+\epsilon_K$).

*Proof.* (a) At $b$, III.G$''$ Theorem 4.2 gives the v1 term $h^{\le2}_{b,\mathrm v1}(a_{\mathrm v1}V^{(-1)}_1)$ of
(4.3), with $V^{(-1)}_1$ from $u_+$, which does not depend on $b$ ((P2): $u_+ = N_{\iota^+}(\lambda)^{-1}(2f_+)$, and
III.G$''$ Theorem 3.1's decomposition is of $u_+$ on $\iota^+$). By (4.2), $a_{\mathrm v1} =
-\lambda_0^{-1}t_*^{-\lambda_0}$, so $\chi_Kh^{\le2}_{b,\mathrm v1}(a_{\mathrm v1}V) =
m_{(\mathrm{rot},\lambda_0,0)}(-\lambda_0^{-1}V)$ up to the tower terms of order $\ge3$, of $K^+$-weight
$\mathrm{Re}\,\lambda_0+3-\epsilon$ (III.I$''''''''''''''$ Definition 1.3, the rotation rows using $h^{\le2}$ and the
tower of III.I$'''''''''$). The other rows are identified as in III.I$''''''''''$ Proposition 3.1 at $b$, by
III.I$''''''''''$ Lemma 2.1 (c) at $b$ (P3). (b) The proof of III.I$'''''''''''$ Lemma 2.3 at $b$ is unchanged except
that the v1 tower $T_{\mathrm v1,b}(\sigma) = \sum_i(-i\sigma)^i\breve h^i_{b,\mathrm v1}(Y)$ has $\breve h^0_{b,\mathrm
v1} = h_{b,\mathrm v1}\ne0$. Its contribution with $c_{\mathrm v1}$ is a piece of type (b) of III.I$''''''''''''$ Lemma
2.1, a tower with polyhomogeneous coefficient. Its rate is that of $\mathcal F^{-1}(\chi c_{\mathrm v1})$, which at
level 1 is $\alpha_0$ (the piece is $\sigma u_{(\alpha_0,k)}$, and $c_{\mathrm v1}$ contributes $|\sigma|^{\alpha_0-1}$
to it). The level-2 count is III.I$'''''''''''$'s, with the rate lowered by 1. (c) As stated. $\square$

**Definition 2.3 (the rotation coordinates at $b$).** At a base point with parameter $b$, the coefficients of the
rotation rows produced by Proposition 2.2 (a)-(b) are called the *assigned rotation coordinates* of the source. In the
theorems of III.I$'''''''''''$-III.I$''''''''''''''$ at $b$, the rotation rows enter with these coordinates, and the
elimination of III.I$'''''''''''$ section 4 runs over the rows $\mathcal N'$ (no v1, as at $b_0$) for $u$ minus the
assigned rotation rows.

**Proposition 2.4 (the rotation coordinates of III.I$''''''''''''''$ Theorem 3.1 at $b$).** At a base point with
parameter $b\in\bar{\mathcal B}_*$, the rotation coordinates $\vec W'^{\mathrm{rot}}$ of III.I$''''''''''''''$ Theorem
3.1 are the negatives of the assigned rotation coordinates of the source $\tilde G_0$ (the sum over the phases). With
this choice, $u$ has no v1 term of exponent in $\mathcal M_{\mathrm{rot}}$, so $C^{\mathrm{rot}}(\vec p\,') = 0$. At
$b_0$ this agrees with III.I$''''''''''''''$ Step 4'.

*Proof.* By Lemma 2.1, the rotation row sources $f^\nu(W')$ lie in $\mathcal Y_2(\alpha)$, so (3.5) of
III.I$''''''''''''''$ holds at $b$ with $\tilde G_0 := \tilde G-\sum_{\nu\in\mathcal N_{\mathrm{rot}}}f^\nu_{h,\vec
p}(W'_\nu)$. The forward solution of the problem with source $f^\nu(W')$ is $-m_\nu(W')$ plus the solution for $r^\nu$,
of $K^+$-weight $>\alpha$ (III.I$'''''''''$ Lemma 2.6 (c) at $b$). By Proposition 2.2, the v1 terms of exponent in
$\mathcal M_{\mathrm{rot}}$ of the solution for $\tilde G$ are $\sum_\nu m_\nu(\text{assigned coordinate})$. With
$W'_\nu$ equal to the assigned coordinates, they cancel. The map from the source to the assigned coordinates is linear
and continuous, uniformly in $b$, and is not the inverse of a degenerate map. At $b_0$ the assigned coordinates are
those that Step 4' extracts through $\ell$ (both are the coefficients of the v1 terms of exponent in $\mathcal
M_{\mathrm{rot}}$, which the construction determines), and the uniqueness of Step 4' gives the same $\vec
W'^{\mathrm{rot}}$. $\square$

## 3. The parts at $b$

**Theorem 3.1 (the linear theory at base points near $b_0$).** For base points with black hole parameter
$b\in\bar{\mathcal B}_*$, the statements at $b$ of the following hold, with constants and smallness conditions uniform
in $b$:

- III.I$'$-III.I$''''''$ (the parts below level 3, whose base points are $(h,S)$ with $g_0 = g_{b_0,b,-S}$);

- III.I$'''''''$ Lemmas 1.3, 2.4, 2.5, Corollary 4.6;

- III.I$''''''''$ Proposition 4.1 and its lemmas;

- III.I$'''''''''$ section 2;

- III.I$''''''''''$ Proposition 3.1;

- III.I$'''''''''''$ Proposition 3.1, Lemma 3.2, Theorem 4.1;

- III.I$''''''''''''$ Theorem 3.1;

- III.I$'''''''''''''$ Propositions 2.1, 2.4;

- III.I$''''''''''''''$ Lemmas 2.2-2.5, Theorem 3.1;

- III.J Theorem 2.4;

- III.J$'$ Theorem 2.1;

- III.J$''$ Theorems 4.1-4.2, Proposition 4.3;

- III.J$'''$ Corollary 6.6.

*Proof.* The census. A search of these parts for every occurrence of $b_0$, $L_{b_0}$, $g_{b_0}$ and of the symmetries
(static, spherical, isotypic, Killing, $SO(4)$) gives the uses listed below. Each is one of (P1)-(P6), Lemma 1.2, or
section 2.

(i) The forward solutions: III.I$'$-III.I$''''''''''''''$ solve with $L^{g,g_0}$ at the base point through III.I Theorem
5.3 and its corollaries (P1). The splitting $L_{h,\vec p} = L_{b_0}+(L_{h,\vec p}-L_{b_0})$ near $K^+$, used to move a
perturbation into the source (III.I$''''''''$-III.I$''''''''''''$, for instance III.I$''''''''''''$ Step 0), becomes
$L_{h,\vec p} = L_b+(L_{h,\vec p}-L_b)$. This has the same $K^+$-gain, $g_0 = g_b$ near $K^+$ (III.I Lemma 3.6).

(ii) The model at $\iota^+$ and at tf: III.G-III.G$''''$ through (P2), (P4).

(iii) The states, towers and index sets: III.I$''''$, III.I$'''''''$, III.I$''''''''$, III.I$'''''''''$ use the index
sets of III.D$''$, III.D$'''$ and III.F$'''$ "at $b_0$". They are independent of $b$ (P3), so the index sets $\mathcal
E_{\mathrm{ind}}$, $\mathcal E_\sharp$, $\mathcal E_+$ of these parts serve at every $b$.

(iv) The derivatives in $b$, taken at $b_0$ in III.I$'''''''$ Corollary 4.6 and III.I$''''''''''''''$ Lemma 2.4 (c): at
$b$, the $b$-column $\dot g_b$ (P3). III.I$''''''''''''''$ Lemma 2.4 (c)'s proof is written for every $b$ near $b_0$; it
uses that every coefficient of $q$ has rate $>2$ at every such $b$. The point of III.I$''''''''''''''$ Theorem 3.1's
Step 1 that uses $\widehat{L_{b_0}}(0)\partial_bh_{b,\mathrm v1} = 0$ needs only that the $q$-terms have $K^+$-order
above $\alpha_1$. At $b$, $\widehat{L_b}(0)\partial_bh_{b,\mathrm v1} = -(\partial_b\widehat{L_b}(0))h_{b,\mathrm v1}$
need not vanish, but $q$'s v1 coefficients have rate $>2+\epsilon_K>\alpha_1$ (Definition 1.1, (G)), so the $K^+$-order
of $L(\partial_bh_{b,\mathrm{rem}}(q)b')$ is still $>2+\epsilon_K>\alpha_1$.

(v) The joint injectivity: III.I$''''''''''$ Lemma 2.2 and Corollary 2.3 at $b$ by Lemma 1.2, and III.I$''''''''''''''$
Step 4''s compact set $\mathcal K_0$ likewise.

(vi) The v1 terms: III.I$'''''''''$ section 1 ($\mathcal W_{\mathrm v1} = \mathcal V' = 0$, kept at every $b$),
III.I$''''''''''$ Lemma 2.1 and Proposition 3.1, III.I$'''''''''''$ Lemma 2.3, III.I$''''''''''''$ section 1, and
III.I$''''''''''''''$ Definitions 1.1, 1.3 and Step 4'. These are section 2.

(vii) The time translation as a Killing field: (P5).

(viii) III.J-III.J$'''$: their base points $U$ map by $\Phi$ to $(h,\vec p,q)$ with parameter $b$ (III.J Theorem 2.4),
and their proofs use III.I$''''''''''''''$ Theorem 3.1 and the maps of III.J at that base point, by (i)-(vii).
III.J$''$'s tame calculus (section 1, Lemmas 2.1-2.4) has constants that depend on the base point through finitely many
seminorms, continuous in $b$; III.J$'''$'s exact classes and conditions (E1)-(E5) do not involve $b$ ((P2)-(P3): the
exponents, roots and index sets are those at $b_0$).

The constants: every constant above is a finite combination of constants of (P1)-(P4), of Lemma 1.2, of Lemma 2.1 and of
the maps of Proposition 2.2, each uniform on $\bar{\mathcal B}_*$. $\square$

**Corollary 3.2 ((J$'$3) closed).** III.J$'$ Theorem 2.1 and its tame and exact forms (III.J$''$ Theorem 4.2, III.J$'''$
Corollary 6.6) hold at every base point $U\in\mathcal D^\infty$ small in $\mathcal D^d$, whatever its black hole
parameter, with constants uniform in $U$. These are the right inverses that II.G Theorem 2.1 (iii) asks for at every
$u\in U$.

## 4. Findings, labels and sources

(I$'''''''''''''''$1) *Direct assignment of the rotation coordinates.* At a rotating base point the v1 terms of exponent
of real part at most 2 decay one order less at $K^+$ than at $b_0$. Their coefficients are assigned from the
construction (the graft's $\iota^+$-data, the spectral pieces' tf-data), not read from the $K^+$-expansion. This is the
source's "$V'\approx\dot V$" (pp. 279-280), carried by III.I$''''''''''''''$'s rotation rows (Proposition 2.2).

(I$'''''''''''''''$2) *The v1 states are not independent at $b$.* At a rotating $b$, $h_{b,\mathrm v1}(V)$ lies in
$\ker\widehat{L_b}(0)$, whose dimension does not jump (III.H Proposition 3.2). So it lies in the span of the continuous
basis, and v1 stays excluded from the $K^+$-extraction (Lemma 1.2's remark).

(I$'''''''''''''''$3) *Corrections at $b_0$, rows at $b$.* The corrections #4 are built at $b_0$, as in the source; the
rows and towers at the base point's $b$ (P6).

(I$'''''''''''''''$4) *The census.* Theorem 3.1 rests on a search of the parts for the uses of $b_0$ and of the
symmetries of $b_0$. A use that the search does not see, for instance an argument at $b_0$ that does not name it, would
be a gap in this part.

*Labels.* Lemmas 1.1, 1.2, 2.1, Propositions 2.2, 2.4, Definition 2.3, Theorem 3.1 and Corollary 3.2 are new at $n = 4$;
Theorem 3.1 is what the source states throughout its sections 11.2-12 by taking its base points with $|b-b_0|$ small.

*Sources.* [Hin26] pp. 275 (Definition 11.55), 278-280 (Theorem 11.59's statement, the v1 elimination
"$V^{(1,0)\prime}\approx\dot V$"), 293 ((11.228)-(11.229)), read at source. Inputs: II.C Lemma 1.4; III.D$''$ (3.4),
Proposition 3.1; III.D$'''$ Proposition 3.1; III.E$'$; III.F Lemma 2.1; III.F$'$ Proposition 2.3; III.F$'''$ Proposition
2.2; III.F$''''$ Proposition 5.1; III.G$'$ Theorem 3.1; III.G$''$ Table 1.1, (4.2)-(4.3), Theorems 3.1, 4.2, Corollary
4.3; III.G$''''$ Lemma 1.1, Propositions 4.4, 5.1; III.H Proposition 3.2, Corollaries 4.2-4.4; III.H$'$ Theorem 1.3;
III.H$''$ Lemma 3.2, Theorem 2.1, Corollary 5.1; III.I Lemma 3.6, Theorem 5.3, Remark 5.4;
III.I$'$-III.I$''''''''''''''$ as listed in Theorem 3.1; III.J Theorem 2.4; III.J$'$ Theorem 2.1; III.J$''$; III.J$'''$.
