# Part III.I$'''''''''''''''$. The linear theory at base points near $b_0$, n = 4 ([Hin26] sections 11.2-12 at black
hole parameters $b\ne b_0$)

*Status.* Written (D297); verified (D299, D302: verifiers 130-131's findings seated, to be read). The parts
III.I$'$-III.I$''''''''''''''$ and III.J-III.J$'''$ prove the linear theory at base points whose black hole parameter is
$b = b_0$, with derivatives in $b$ taken at $b_0$; III.I Remark 5.4 and (I3) of III.I recorded why. III.H$''$ supplied
the two inputs that were missing for $b\ne b_0$ (its Corollary 5.1) and recorded the rest as (H$''$5). This part proves
that rest. At every base point $(h,\vec p)$, or $(h,\vec p,q)$, or $U$, whose black hole parameter is $b\in\mathcal B_*$
($\mathcal B_*$ of III.H$''$), the statements of those parts hold with constants uniform in $b$. *The statement at $b$*
of each of them is obtained as follows: $L_{b_0}$, $g_{b_0}$ near $K^+$, the states, towers and companions at $b_0$, and
the index set $\mathcal E_{\mathrm{ind}}$ are replaced by those at $b$; derivatives in $b$ are taken at $b$; and the v1
terms are treated by section 2. This closes (J$'$3) of III.J$'$, and with it (I3) and (H$''$5).

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

(P6) *Rows at $b$, corrections at $b_0$.* The rows and towers are built at the base point's $b$ (the towers $T_{\rho,b}$
of III.I$''''''''''''''$ Definition 1.2, smooth in $b$ by (P3)); the corrections #1-#4 (III.I$'''''''$ Definition 2.1,
III.I$'''''''''$ Definition 2.1) and their counterterms are the tensors built from $b_0$-objects, as the source builds
them ([Hin26] p. 275, Definition 11.55; its operator is at $b$, Definition 11.56). At a base point $(h,\vec p)$ with
parameter $b$,
$$D_{\vec p}P_4(h,\vec p)(W_\nu = W) = L_{h,\vec p}m_\nu(W)+r^\nu_{h,\vec p}(W)+E^\nu_{h,\vec p}(W).\tag{1.1}$$
Here $f^\nu_b := L_{h,\vec p}m_\nu+r^\nu_{h,\vec p}$ is III.I$'''''''''$ Lemma 2.6 (c) at $b$, with every object (rows,
corrections, counterterms) built at $b$, in the classes of III.I$'''''''''$ (2.5) uniformly in $b$. And
$$E^\nu_{h,\vec p}(W) := L_{h,\vec
p}\big(h^{b_0}_\nu-h^b_\nu\big)(W)+\delta^*_{g_0,E_C}\big(\vartheta^{b_0}_{\nu,\sharp}-\vartheta^b_{\nu,\sharp}\big)(W),$$
the difference between the corrections and counterterms built at $b_0$ and at $b$, lies in $\mathcal
Y^\natural_2(\alpha-)\cap\mathcal Y(\alpha_1)$, with norm $O(|b-b_0||W|)$. Its support is in $\mathrm{supp}\,\chi_K$,
its $K^+$-weight is $\kappa_\nu-\epsilon>\alpha$, and its $\iota^+$-exponents below $w_+$ lie in $\mathcal E^\natural+2$
(III.I$'''''''''''''$ Definition 1.2).

*Proof.* (P1)-(P4) are the cited statements. (P5): $g_b$ is stationary. (P6): $f^\nu_b$ is III.I$'''''''''$ Lemma 2.6
(c)'s computation at $b$. Its errors near $K^+$ are $L_{h,\vec p}-L_b$, which gains $a_K$ there, $g_0 = g_b$ near $K^+$
(III.I Lemma 3.6); its objects are smooth in $b$ (P3), so the bounds are uniform. For $E^\nu$ (verifier 131's m1 and
section B): - The differences $h^{b_0}_\nu-h^b_\nu$ and $\vartheta^{b_0}_{\nu,\sharp}-\vartheta^b_{\nu,\sharp}$ are
$b$-differences of the 1-form towers and of their commutators with $\chi_K$, so $O(|b-b_0|)$ by (P3), and supported in
$\mathrm{supp}\,\chi_K$. - Near $K^+$ the corrections vanish (they are supported in $\mathcal C$), but the counterterms
do not: there $\vartheta_{\nu,\sharp} = \frac12\Box\omega_\nu$ (III.I$'''''''''$ section 2). Their difference has the
$K^+$-weight $\kappa_\nu$ of the tops of the towers (III.I$'''''''''$ Lemma 2.2 (a), (d), and (P3)). So $E^\nu$ has
$K^+$-weight $\kappa_\nu-\epsilon>\alpha$. - At $\iota^+$, the $b$-differences of the towers have exponents
$\lambda_\nu+\mathcal E_{\mathrm{ind}}$ (for v1 also $\lambda_\nu+3$; III.I$''''''''''''''$ Lemma 2.1), with
$\lambda_\nu$ the row's $\iota^+$-exponent in $\mathcal E_{\mathrm{par}}\cap\{\mathrm{Re}\le3\}\subset\mathcal
E_\sharp$. $L$ and $\delta^*$ add 2 and increments, and the parts of $L_{h,\vec p}-L_b$ from $h$ and $h_{\mathrm{tot}}$
gain $\rho_+^{\lambda_\sharp}$. So below $w_+$ the exponents lie in $\mathcal E^\natural+2$ (III.I$'''''''''''''$
Definition 1.2), with log orders bounded by III.I$'''''''''''''$ Lemma 1.3 (a), and above it the plain weight is
$\mathrm{Re}\,\lambda+2+\lambda_\sharp>w_+$. - So $E^\nu\in\mathcal Y^\natural_2(\alpha-)$, and $E^\nu\in\mathcal
Y(\alpha_1)$ as $\mathcal E^\natural\cap\{\mathrm{Re}<2\}\subset\mathcal E_{++}$ (III.I$'''''''''''''$ Lemma 1.3 (a)).
$\square$

The source makes the same choice: its corrections are built at $b_0$, its operator is at $b$ (Definition 11.56), and its
expansion's towers are those of $L_b$ (Theorem 11.59). Rows built at $b_0$ would leave $(L_b-L_{b_0})m^{b_0}_\nu$ near
$K^+$, of $K^+$-order only $\mathrm{Re}\,e_\nu+2$. Rows at $b$ move the mismatch into the $b$-differences of the
corrections and counterterms, which near $K^+$ enter only through the counterterms, at the weight $\kappa_\nu$ (verifier
130's m2, 131's m1). Corrections #1-#3 are commutator terms in $\mathrm{supp}\,d\chi_K$ (III.I$''''$), so $f^S$ and
$f^{\mathrm s1}$ vanish near $K^+$, and their $b_0/b$ mismatch lies at $\iota^+$ only, with the gain $\rho_+^2$ of
$g_b-g_{b_0}$ (verifier 131's n8). At $b_0$, $E^\nu = 0$ and (1.1) is III.I$'''''''''$'s identity.

**Lemma 1.2 (joint injectivity at $b$).** Shrinking $\mathcal B_*$, III.I$''''''''''$ Lemma 2.2 and Corollary 2.3 hold
at every $b\in\bar{\mathcal B}_*$, for the states at $b$: if $\sum_{\tau\ne\mathrm v1}h_{b,\tau}(W_\tau) = 0$ then every
$W_\tau = 0$; and a finite sum of rows $\nu\ne\mathrm v1$ at $b$ with $K^+$-weight above the largest of their rates
vanishes. Moreover, there are a compact $\mathcal K_0\subset X^\circ$ and $c>0$, independent of $b$, with
$\sup_{\mathcal K_0}|\sum_\tau h_{b,\tau}(W_\tau)|\ge c\sum_\tau|W_\tau|$.

*Proof.* The space $\mathcal W := \bigoplus_{\tau\ne\mathrm v1}\mathcal W_{\tau,\mathbb C}$ is finite-dimensional. At
$b_0$ the map $\Theta_{b_0}: W\mapsto\sum_\tau h_{b_0,\tau}(W_\tau)$ is injective (III.I$''''''''''$ Lemma 2.2). Each
nonzero element of its range is a nonzero smooth tensor on $X^\circ$, nonzero on an open set, so by compactness of the
unit sphere of $\mathcal W$ there is a compact $\mathcal K_0\subset X^\circ$ on which $\sup_{\mathcal
K_0}|\Theta_{b_0}W|\ge2c|W|$. $\Theta_b$ depends continuously on $b$ in $C^0(\mathcal K_0)$ (P3), so the bound with $c$
holds for $b$ near $b_0$. Corollary 2.3's proof uses only Lemma 2.2 and III.I$'''''''''$ Lemma 2.2 (e), the $K^+$-weight
$\mathrm{Re}\,e_\nu+1-\epsilon$ of $m_\nu(W)-\chi_Kr_\nu h_\tau(W)$, which is a computation with the tower relations and
holds at $b$ (P3). $\square$

v1 stays excluded at $b$, as at $b_0$, for a quantitative reason. At $b$, $h_{b,\mathrm v1}(V)$ is $\delta^*_{g_b}$ of a
1-form in $\ker\Box^\Upsilon_b$ (III.D$''$ (3.4)), so it lies in $\ker\widehat{L_b}(0)$ in III.H's space $\mathcal X_0$,
and it is $O(|b-b_0||V|)$ (P3). Near $b_0$ that nullspace has the dimension it has at $b_0$, with the continuous basis
$\dot g_b(\dot b)$, $h_b(S)$ (III.H Proposition 3.2's proof: the matrix $B(b)$ is invertible). So $h_{b,\mathrm v1}(V) =
\dot g_b(\dot b_V)+h_b(S_V)$ with $|\dot b_V|+|S_V| = O(|b-b_0||V|)$. A $K^+$-extraction that read a v1 coefficient
beside the $b$- and $S$-coefficients would invert a map that degenerates as $b\to b_0$ (verifier 130's m4). This is why
the v1 coefficients are assigned in section 2, not read from the $K^+$-expansion.

## 2. The rotation rows at $b$

Let $\mathcal N_{\mathrm{rot}}$, $\mathcal M_{\mathrm{rot}} = \mathcal E_\sharp\cap\{\mathrm{Re}\le2\}$ and the rotation
rows $m_\nu$, $\nu = (\mathrm{rot},\lambda,k)$, be those of III.I$''''''''''''''$ Definitions 1.1 and 1.3, with the v1
tower $T_{\mathrm v1,b}$ at the base point's $b$: $m_\nu(W) = \chi_KT_{\mathrm v1,b}(a_\nu W)$, $a_\nu =
t_*^{-\lambda}(\log t_*)^k$, $W\in\mathcal V_{1,\mathbb C}$.

**Lemma 2.1 (rotation rows at $b$).** At $b\in\bar{\mathcal B}_*$, $m_\nu(W)$ has $K^+$-weight
$\mathrm{Re}\,\lambda-\epsilon$ (its bottom $a_\nu h_{b,\mathrm v1}(W)$, of size $O(|b-b_0||W|)$), and
$m_\nu(W)-\chi_Ka_\nu h_{b,\mathrm v1}(W)$ has $K^+$-weight $\mathrm{Re}\,\lambda+1-\epsilon$. III.I$'''''''''$ Lemmas
2.2 (a)-(e) and 2.4-2.6 hold for $\nu$ at $b$, with $e_\nu = \lambda$ and $\kappa_\nu = \mathrm{Re}\,\lambda+4$; in
particular $f^\nu_{h,\vec p}(W) := D_{\vec p}P_4(h,\vec p)(W_\nu = W) = f^\nu_b(W)+E^\nu_{h,\vec p}(W)$ as in (1.1),
with $f^\nu_b(W) = L_{h,\vec p}m_\nu(W)+r^\nu_{h,\vec p}(W)\in\mathcal Y_2(\alpha)$ uniformly in $b$, and $E^\nu_{h,\vec
p}(W)\in\mathcal Y^\natural_2(\alpha-)\cap\mathcal Y(\alpha_1)$ of size $O(|b-b_0||W|)$.

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
up to $K^+$-weight $\mathrm{Re}\,\lambda_0+1-\epsilon$. Here $V^{(j)}$ is the graft's v1 coefficient of
$t_*^{-\lambda_0}(\log t_*)^j$, read from the $\iota^+$-data $u_+$ by III.G$''$ Theorem 3.1, in the normalisation of
III.I$''''''''''$'s rows, in which a $(\log t_*)^j$-term keeps the prefactor of the term $j = 0$ (verifier 130's n1);
for $j = 0$ it is $-\lambda_0^{-1}V^{(-1)}_1$, by $a_{\mathrm v1} = -\lambda_0^{-1}t_*^{-\lambda_0}$ (III.G$''$ (4.2)).
It is linear and continuous in the source, uniformly in $b$. $(\lambda_0,j)\in\mathcal M\subset\mathcal
M_{\mathrm{rot}}$, so the rotation row exists. So III.I$''''''''''$ Proposition 3.1 (b) holds at $b$ with the rows
$\mathcal N_\iota\sqcup\mathcal N_{\iota,\mathrm{rot}}$ and these coefficients.

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

**Definition 2.3 (the assigned rotation coordinates).** Let $(h,\vec p)$ be a base point with parameter
$b\in\bar{\mathcal B}_*$, and $G\in\mathcal Y^\natural(\beta)$, $\beta>3$. The *assigned rotation coordinates*
$A_{b,\nu}(G)\in\mathcal V_{1,\mathbb C}$, $\nu\in\mathcal N_{\mathrm{rot}}$, are the coefficients of the rotation rows
that Proposition 2.2 (a)-(b) produces in the forward solution of $L_{h,\vec p}u = G$: the graft's v1 coefficients at the
exponents of $\mathcal M$ (spacetime phase), and the spectral level-1 coefficients at the exponents of real part 2. They
do not depend on $\beta$. $A_b := (A_{b,\nu})_\nu$ is linear and continuous on $\mathcal Y^\natural(\beta)$, uniformly
in $b$ and in $(h,\vec p)$ small, (Proposition 2.2, (P2), (P4)). No continuity in $b$ is claimed or needed (Proposition
2.5's Step 3). It is defined at $b_0$ by the same formulas.

**Lemma 2.4 (III.I$'''''''''''''$ Lemmas 2.2-2.3 at $b$).** Let $\beta\in(3,4+\epsilon_K]$ be admissible, $(h,\vec p)$ a
base point with parameter $b\in\bar{\mathcal B}_*$ and $h\in\mathcal X^\infty$ small, $G\in\mathcal Y^\natural(\beta)$,
and let the forward solution $u$ of $L_{h,\vec p}u = G$ satisfy the hypothesis of III.I$'''''''''''''$ Lemma 2.2. Then
$$u = \sum_{\nu\in\mathcal N_\beta}m_\nu(S_\nu)+\sum_{\nu\in\mathcal
N^{<\beta}_{\mathrm{rot}}}m_\nu\big(A_{b,\nu}(G)\big)+\tilde u,\qquad\mathcal N^{<\beta}_{\mathrm{rot}} :=
\{\nu\in\mathcal N_{\mathrm{rot}}:\mathrm{Re}\,\lambda_\nu<\beta-2\},\tag{2.1}$$
with $\tilde u$ in the class of III.I$'''''''''''''$ (2.2) and $S_\nu = S^{h,\vec p,\beta}_\nu(G)$ determined by
$u-\sum_{\mathcal N^{<\beta}_{\mathrm{rot}}}m_\nu(A_{b,\nu}(G))$, conjugation-symmetric, linear and continuous in $G$,
uniformly. At a fixed $b$: if $(h_j,\vec p_j)\to(0,\vec p_b)$, with $\vec p_b$ the parameter whose only nonzero
component is $b-b_0$, and $G_j\to G$ in $\mathcal Y^\natural(\beta)$, with the hypothesis of III.I$'''''''''''''$ Lemma
2.3, then $S^{h_j,\vec p_j,\beta}_\nu(G_j)\to S^{0,\vec p_b,\beta}_\nu(G)$. At $b_0$ the second sum in (2.1) is absent
(the rotation rows' rates there are $\mathrm{Re}\,\lambda+1>\alpha-2\ge\beta-2$), and (2.1) is III.I$'''''''''''''$
(2.2). For $\beta<3$ no rotation row has rate below $\beta-2$ ($\mathrm{Re}\,\lambda-\epsilon>1$, Lemma 2.1), and
III.I$''''''''$ Lemma 3.2 holds at $b$ as at $b_0$.

*Proof.* III.I$'''''''''''''$ Lemma 2.2's proof builds the expansion from the pieces of III.I$''''''''''$ Proposition
3.1 (the spacetime phase), III.I$'''''''''''$ Proposition 3.1 and Theorem 4.1 (the spectral phase), III.I$''''''''''''$
Theorem 3.1 and III.I$'''''''''''''$ Proposition 2.1, and reads the coefficients by III.I$''''''''''$ Corollary 2.3. At
$b$ these hold with the model objects at $b$ ((P1)-(P6)), except the v1 pieces of exponent in $\mathcal
M_{\mathrm{rot}}$. By Proposition 2.2 (a)-(c) those are the rotation rows with the coefficients $A_{b,\nu}(G)$, up to
$K^+$-weight $\mathrm{Re}\,\lambda+1-\epsilon>\beta-2$, which goes into $\tilde u$. The rows other than v1 are then read
from $u-\sum m_\nu(A_{b,\nu}(G))$, uniquely, by Corollary 2.3 at $b$ (Lemma 1.2). For the continuity at fixed $b$,
III.I$'''''''''''''$ Lemma 2.3's proof runs with $L_{0,\vec p_b}$ in place of $L_{b_0}$. Its remainder $(L_{h_j,\vec
p_j}-L_{0,\vec p_b})u_j$ gains $a_K$ near $K^+$, where both backgrounds equal $g_b$ (III.I Lemma 3.6). Continuity across
$b$ is not claimed: the proofs perturb from a reference operator, and $L_b-L_{b_0}$ gains only 2 at $K^+$ (verifier
131's M1). $\square$

**Proposition 2.5 (III.I$''''''''''''''$ Theorem 3.1 at $b$).** Let $h\in\mathcal X^\infty$, $\vec p\in\mathcal P$ with
parameter $b\in\bar{\mathcal B}_*$, and $q\in\mathcal Q$ be small, and $F\in\mathcal Y^\natural(\alpha-)$. For $\vec
p\,'\in\mathcal P$ let $u(\vec p\,')$ be the forward solution of III.I$''''''''''''''$ (3.1), and (III.I$''''''''''''''$
Step 2, with (1.1))
$$G'(\vec p\,') := \tilde G-f^S_{h,\vec p}(S')-f^b_{h,\vec p}(b')-f^{\mathrm s1}_{h,\vec
p}(S^{(0)\prime}_1)-\sum_{\nu\in\mathcal N\sqcup\mathcal N_{\mathrm{rot}}}\big(r^\nu_{h,\vec p}+E^\nu_{h,\vec
p}\big)(W'_\nu),\qquad\tilde G := F-\Delta_q(\vec p\,')-R_qu(\vec p\,').$$
There is a unique $\vec p\,'\in\mathcal P$ with
$$W'_\nu = A_{b,\nu}\big(G'(\vec p\,')\big)\qquad(\nu\in\mathcal N_{\mathrm{rot}})\tag{2.2}$$
such that $u(\vec p\,')$ satisfies the conclusions of III.I$''''''''''''''$ Theorem 3.1: (3.1)-(3.2), and $u =
h_{\mathrm{rem}}(q')+h'$ with $q'\in\mathcal Q$. $\vec p\,'$, $q'$ and $h'$ are linear in $F$, with bounds uniform for
$(h,\vec p,q)$ small, $b$ included. At $b_0$, (2.2) is III.I$''''''''''''''$ Step 4$'$'s condition $C^{\mathrm{rot}} =
0$, and $\vec p\,'$ is that of III.I$''''''''''''''$ Theorem 3.1.

*Proof.* *Steps 0-1* are III.I$''''''''''''''$'s at $b$, by (P1)-(P6). $E^\nu\in\mathcal
Y^\natural(\alpha-)\subset\mathcal Y(\alpha_1)$ joins the terms of Step 1. The rotation rows, of $K^+$-weight
$\mathrm{Re}\,\lambda-\epsilon>1>\alpha_1-2$ (Lemma 2.1), lie above the base level.

*Step 2 at $b$.* Let $u := u(\vec p\,')\in\mathcal Z_{\beta_k}$. As in III.I$''''''''''''''$ Step 2, by (1.1), $u_0 :=
u+\sum_{\mathcal N\sqcup\mathcal N_{\mathrm{rot}}}m_\nu(W'_\nu)$ solves $L_{h,\vec p}u_0 = G'(\vec p\,')\in\mathcal
Y^\natural(\beta_{k+1})$ (resp. $\mathcal Y^\natural(\alpha-)$ for $k+1 = K$). Lemma 2.4 gives, for $\beta_{k+1}>3$
(below 3, III.I$''''''''$ Lemma 3.2 as in III.I$''''''''''''''$ Step 2),
$$u = \sum_{\nu\in\mathcal N_{\beta_{k+1}}\sqcup\mathcal N^{<\beta_{k+1}}_{\mathrm{rot}}}m_\nu\big(C^{k+1}_\nu(\vec
p\,')\big)+\tilde u,\qquad\tilde u\in\mathcal Z_{\beta_{k+1}},\tag{2.3}$$
with $C^{k+1}_\nu := S^{h,\vec p,\beta_{k+1}}_\nu(G'(\vec p\,'))-W'_\nu$ for $\nu\in\mathcal N_{\beta_{k+1}}$, and
$C^{k+1}_\nu := A_{b,\nu}(G'(\vec p\,'))-W'_\nu$ for $\nu\in\mathcal N^{<\beta_{k+1}}_{\mathrm{rot}}$. The
$m_\nu(W'_\nu)$ of the other rows, of $K^+$-weight above $\beta_{k+1}-2$, are part of $\tilde u$. The *new rows* of the
level are those of $\mathcal N_{\beta_{k+1}}$ of rate in $[\beta_k-2,\beta_{k+1}-2)$, as at $b_0$, and the rotation rows
of $\mathcal N^{<\beta_{k+1}}_{\mathrm{rot}}\setminus\mathcal N^{<\beta_k}_{\mathrm{rot}}$. If the conditions of the
lower levels hold, then the coefficients of the old rows vanish. For a rotation row, $C^{k+1}_\nu$ is the same function
of $\vec p\,'$ at every level, $A_b$ not depending on $\beta$. For the other rows, $\sum_{\mathcal
N_{\beta_k}}m_\nu(C^{k+1}_\nu)\in\mathcal Z_{\beta_k}$, so they vanish by Lemma 1.2. Hence $u\in\mathcal
Z_{\beta_{k+1}}$ if $C^{k+1}_\nu(\vec p\,') = 0$ for the new rows. The converse is not claimed for the rotation rows
(Remark 2.6).

*Step 3 at $b$.* Let $\mathcal P_k$ be the set of $\vec p\,'\in\mathcal P_0$ with $C^j_\nu(\vec p\,') = 0$ for the new
rows of every level $j\le k$; by Step 2, $u(\vec p\,')\in\mathcal Z_{\beta_k}$ on $\mathcal P_k$. As in
III.I$''''''''''''''$ Step 3, $\mathcal P_k$ is, by induction, the graph of an affine map from the coordinates of the
rows of rate $\ge\beta_k-2$ to the others. The rotation rows enter by their rates $\mathrm{Re}\,\lambda$ at $b$. On
$\mathcal P_k$, $C^{k+1}$ restricted to the new coordinates is $-\mathrm{id}+A_k$, with $A_k\to0$ as $(h,\vec
p,q)\to(0,0,0)$, the parameter of $\vec p$ tending to $b_0$. The bound on $A_k$ is direct, with no continuity in $b$. By
Step 2, $C^{k+1}_\nu(\vec p\,') = S^{h,\vec p,\beta_{k+1}}_\nu(G'(\vec p\,'))-W'_\nu$, resp. $A_{b,\nu}(G'(\vec
p\,'))-W'_\nu$, and $G'$ is affine in $\vec p\,'$. Its dependence on the coordinates $W'_\nu$ of the rows of $\mathcal
N\sqcup\mathcal N_{\mathrm{rot}}$ is through: - $(r^\nu_{h,\vec p}+E^\nu_{h,\vec p})(W'_\nu)$. At the base point
$(0,\vec p_b)$ the identity of III.I$'''''''''$ Lemma 2.4 at $b$ gives $f^\nu_b = L_{0,\vec p_b}m_\nu$ up to the
$O(|b-b_0|)$ mixing of $g_{b_0,b,0}$ in $\mathcal C$. So $r^\nu_{h,\vec p}+E^\nu_{h,\vec p}$ has norm $O(\|h\|+|\vec
p-\vec p_b|+|b-b_0|)$ in $\mathcal Y^\natural_2(\alpha-)$ (III.I$'''''''''$ Lemma 2.6's bounds at $b$, and (P6)). -
$\Delta_q(\vec p\,')$ and $R_qu(\vec p\,')$, of norm $O(\|q\|)$ (III.I$''''''''''''''$ Lemmas 2.3-2.4).

The motion coordinates enter through $f^S$, $f^b$, $f^{\mathrm s1}$, but they lie at the base level, below every new
row. On $\mathcal P_k$ the lower coordinates are, by the induction, affine functions of the free ones with coefficients
of the same smallness. $S^{h,\vec p,\beta}$ and $A_b$ are bounded uniformly in $b$ and $(h,\vec p)$ small (Lemma 2.4,
Definition 2.3). So in the new coordinates $C^{k+1} = -\mathrm{id}+A_k$ with $|A_k|\le C(\|h\|+|\vec p-\vec
p_b|+\|q\|+|b-b_0|)$, $C$ uniform in $b$ (verifier 131's M1, by the direct bound). At the base level and the levels
below 3, the continuity statements that III.I$''''''''''''''$ Step 3 cites (III.I$''''''''$ Proposition 4.1 (ii) and
Lemma 3.3, III.I$'''''''''''$ Lemma 3.3, III.I$'''''''''''''$ Lemma 2.3) are used at fixed $b$, with $(0,\vec p_b)$ in
place of $(0,0)$, as in Lemma 2.4's proof.

So $-\mathrm{id}+A_k$ is invertible for $(h,\vec p,q)$ small, and $\mathcal P_{k+1}$ is a graph. At $k = K$ every row
has rate below $\alpha-2$ (the rotation rows at $b$: $\mathrm{Re}\,\lambda\le2<\alpha-2$), so $\mathcal P_K$ is one
point $\vec p\,'$. It satisfies (2.2), and $u(\vec p\,')\in\mathcal Z_\alpha$ with no rotation-row content. The rest of
III.I$''''''''''''''$'s proof, the splitting $u = h_{b,\mathrm{rem}}(q')+h'$ by III.I$''''''''''''$ Theorem 3.1 at $b$,
then applies. The v1 coefficient of $q'$ has no term at $\mathcal M_{\mathrm{rot}}$. $\vec p\,'$ is affine in $F$, which
enters through $\tilde G$ only, and linear since it vanishes at $F = 0$. Uniqueness: any $\vec p\,''$ satisfying (2.2)
with $u(\vec p\,'')\in\mathcal Z_\alpha$ lies in $\mathcal P_0$ (III.I$''''''''''''''$ Step 1's uniqueness). Its
non-rotation coefficients vanish level by level by Lemma 1.2, since (2.2) removes the rotation rows from (2.3). So $\vec
p\,''\in\mathcal P_K$.

*At $b_0$.* At $b_0$ the v1 coefficient of $u = u_0-\sum m_\nu(W'_\nu)$ at $\mathcal M_{\mathrm{rot}}$ is
$A_{b_0}(G')-\vec W'^{\mathrm{rot}}$. The v1 pieces of $u_0$ are the construction's, with the coefficients $A_{b_0}(G')$
(Proposition 2.2 at $b_0$). On $\mathcal P_K$ the coefficients of the rows of $\mathcal N$ vanish, and
III.I$''''''''''''''$ Step 4$'$'s functional $\ell$, applied to $u = u_0-\sum m_\nu(W'_\nu)$, returns its v1 coefficient
uniquely; by Proposition 2.2 (c) and Definition 2.3 it is $A_{b_0}(G')-\vec W'^{\mathrm{rot}}$ (verifier 131's n3), and
$m_\nu(W)$, $\nu\in\mathcal N_{\mathrm{rot}}$, has v1 coefficient $a_\nu W$. So $C^{\mathrm{rot}} = 0$ is (2.2) (with
the sign of Step 4$'$'s derivative $-\mathrm{id}$; verifier 130's m1 corrects D297's sign). The $\vec p\,'$ of
III.I$''''''''''''''$ Theorem 3.1 satisfies the level conditions and (2.2), so it is the point $\mathcal P_K$. $\square$

**Remark 2.6 (uniqueness at $b$).** At a rotating $b$, the $\vec p\,'$ of Proposition 2.5 is unique only together with
(2.2). The bottom of $m_\nu(W)$, $\nu\in\mathcal N_{\mathrm{rot}}$, is $a_\nu h_{b,\mathrm v1}(W) = a_\nu(\dot g_b(\dot
b_W)+h_b(S_W))$, with coefficients $O(|b-b_0||W|)$ (Lemma 1.2's remark). The $K^+$-expansion does not separate it from
the $b$- and $S$-rows, so the conditions $u\in\mathcal Z_{\beta_k}$ alone are not shown to fix $\vec W'^{\mathrm{rot}}$
(verifier 131's n5). The later parts use only the constructed map $F\mapsto(\vec p\,',q',h')$:

- III.J$'$ Theorem 2.1 builds $U'$ from it; its Remark 2.2 records that $D_U\Phi$ is not injective.

- III.J$''$ Theorem 4.1 estimates it.

- III.J$'''$ cites "Step 3 and its uniqueness" to identify the exact and the lossy solutions (its paragraph on
III.I$''''''''''''''$ Theorem 3.1 at exact weights). At $b$, Proposition 2.5's constrained uniqueness serves there:
$A_b$ does not depend on the loss, being computed from $\iota^+$- and tf-data, which the exact and the lossy classes
share.

## 3. The parts at $b$

**Theorem 3.1 (the linear theory at base points near $b_0$).** For base points with black hole parameter
$b\in\bar{\mathcal B}_*$, the statements at $b$ of the following hold, with constants and smallness conditions uniform
in $b$:

- III.I$'$-III.I$''''''$ (the parts below level 3; III.I$'''$'s background $g_S := g_{b_0,b_0,-S}$ becomes
$g_{b_0,b,-S}$, and the corrections #1-#3 stay the tensors built at $b_0$, (P6));

- III.I$'''''''$ Lemmas 1.3, 2.4, 2.5, Corollary 4.6;

- III.I$''''''''$ Proposition 4.1 and its lemmas;

- III.I$'''''''''$ section 2;

- III.I$''''''''''$ Proposition 3.1;

- III.I$'''''''''''$ Proposition 3.1, Lemmas 3.2-3.3 (at fixed $b$, Lemma 2.4's proof), and Theorem 4.1 only inside
Lemma 2.4 and Proposition 2.5: at a rotating $b$ its parameter space lacks the rotation rows, and Proposition 2.5 with
$q = 0$ is its form there (verifier 131's m2);

- III.I$''''''''''''$ Theorem 3.1;

- III.I$'''''''''''''$ Proposition 2.1, Lemmas 2.2-2.3 in the form of Lemma 2.4, and Proposition 2.4 only inside
Proposition 2.5, as for III.I$'''''''''''$ Theorem 4.1;

- III.I$''''''''''''''$ Lemmas 2.2-2.5, and Theorem 3.1 in the form of Proposition 2.5 (unique among the $\vec p\,'$
with the assigned rotation coordinates);

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

(v) The joint injectivity: III.I$''''''''''$ Lemma 2.2 and Corollary 2.3 at $b$ by Lemma 1.2, III.I$''''''''''''''$ Step
4$'$ is not used at $b$, Proposition 2.5 replacing it.

(vi) The v1 terms: III.I$'''''''''$ section 1 ($\mathcal W_{\mathrm v1} = \mathcal V' = 0$, kept at every $b$),
III.I$''''''''''$ Lemma 2.1 and Proposition 3.1, III.I$'''''''''''$ Lemma 2.3, III.I$''''''''''''$ section 1, and
III.I$''''''''''''''$ Definitions 1.1, 1.3, Steps 2-3 and 4$'$. These are section 2: Proposition 2.2, Lemma 2.4 and
Proposition 2.5.

(vii) The time translation as a Killing field: (P5).

(viii) III.J-III.J$'''$: their base points $U$ map by $\Phi$ to $(h,\vec p,q)$ with parameter $b$ (III.J Theorem 2.4),
and their proofs use III.I$''''''''''''''$ Theorem 3.1 and the maps of III.J at that base point, by (i)-(vii).
III.J$''$'s tame calculus (section 1, Lemmas 2.1-2.4) has constants that depend on the base point through finitely many
seminorms, continuous in $b$; III.J$'''$'s exact classes and conditions (E1)-(E5) do not involve $b$ ((P2)-(P3): the
exponents, roots and index sets are those at $b_0$). III.J$''$ Theorem 4.1's solution maps of III.I-III.I$'''''''''''''$
are read at $b$ as in Lemma 2.4 and Proposition 2.5. The new objects enter III.J$''$ Lemma 2.1 (c)'s inventory (verifier
131's m3): $A_b$ is bounded by a fixed low seminorm of $G$, as it reads the $\iota^+$-data $u_+$ and the tf-data
(Proposition 2.2); $E^\nu$ is bounded by $C|b-b_0||W|$ in a fixed seminorm ((P6)); the rotation rows enter
$-\mathrm{id}+A_k$ as the other rows do; and $d_*$ includes their orders.

The constants: every constant above is a finite combination of constants of (P1)-(P4), of Lemma 1.2, of Lemma 2.1 and of
the maps of Proposition 2.2, each uniform on $\bar{\mathcal B}_*$. The continuity statements (III.I$''''''''$
Proposition 4.1 (ii) and Lemma 3.3, III.I$'''''''''''$ Lemma 3.3, III.I$'''''''''''''$ Lemma 2.3 in Lemma 2.4) are used
at fixed $b$ only. The smallness of the elimination, across $b$, comes from the direct bound of Proposition 2.5's Step
3, through (P6) and Definition 2.3 (verifier 131's M1 and n2). $\mathcal B_*$ is shrunk, beyond III.H$''$ (B5), so that
Lemma 1.2's bound holds and the maps $-\mathrm{id}+A_k$ of Proposition 2.5 are invertible on it (verifier 130's m3).
$\square$

**Corollary 3.2 ((J$'$3) closed).** III.J$'$ Theorem 2.1 and its tame and exact forms (III.J$''$ Theorem 4.2, III.J$'''$
Corollary 6.6) hold at every base point $U\in\mathcal D^\infty$ small in $\mathcal D^d$, with black hole parameter
$b\in\mathcal B_*$, which smallness of $U$ in $\mathcal D^d$ ensures, with constants uniform in $U$; at a rotating $b$
the right inverse is the one constructed by Proposition 2.5. These are the right inverses that II.G Theorem 2.1 (iii)
asks for at every $u\in U$.

## 4. Findings, labels and sources

(I$'''''''''''''''$1) *The rotation rows are new rows at $b$.* At a rotating base point, the v1 terms of exponent of
real part at most 2 decay one order less at $K^+$ than at $b_0$, and they fall below the levels. They are new rows of
the levels at which their rates lie, with coefficients assigned from the construction (Definition 2.3): the graft's
$\iota^+$-data and the spectral pieces' tf-data. So the rotation coordinates are fixed level by level inside the
elimination (Proposition 2.5), not at the end as by III.I$''''''''''''''$ Step 4$'$. This is the source's
"$V'\approx\dot V$" (pp. 279-280). Verifier 130's M1 found that D297's text had left them to the end.

(I$'''''''''''''''$2) *v1 is not separable at $b$.* $h_{b,\mathrm v1}(V)$ is a combination of $\dot g_b$ and $h_b(S)$
with coefficients $O(|b-b_0||V|)$ (Lemma 1.2's remark). So a $K^+$-reading of v1 degenerates as $b\to b_0$, and the
coefficients are assigned.

(I$'''''''''''''''$3) *Corrections at $b_0$, rows at $b$.* As in the source, the corrections #1-#4 and their
counterterms are built at $b_0$, while the rows and towers are built at the base point's $b$ ((P6), (1.1)). The mismatch
$E^\nu$ is the $b$-difference of the corrections and counterterms: supported in $\mathrm{supp}\,\chi_K$, of $K^+$-weight
$\kappa_\nu-\epsilon>\alpha$, and $O(|b-b_0|)$. Its $\iota^+$-exponents lie in $\mathcal E^\natural+2$, so
$E^\nu\in\mathcal Y^\natural_2(\alpha-)\cap\mathcal Y(\alpha_1)$. Settled in D302 (verifier 131's section B); verifier
130's m2 had left it open.

(I$'''''''''''''''$4) *Uniqueness at $b$ only with the assigned coordinates* (Remark 2.6).

(I$'''''''''''''''$5) *The census.* Theorem 3.1 rests on a search of the parts for the uses of $b_0$ and of the
symmetries of $b_0$. A use that the search does not see would be a gap in this part, for instance an argument at $b_0$
that does not name it.

*Labels.* Lemmas 1.1, 1.2, 2.1, 2.4, Propositions 2.2, 2.5, Definition 2.3, Remark 2.6, Theorem 3.1 and Corollary 3.2
are new at $n = 4$; Theorem 3.1 is what the source states throughout its sections 11.2-12 by taking its base points with
$|b-b_0|$ small.

*Sources.* [Hin26] pp. 275 (Definition 11.55), 278-280 (Theorem 11.59's statement, the v1 elimination
"$V^{(1,0)\prime}\approx\dot V$"), 293 ((11.228)-(11.229)), read at source. Inputs: II.C Lemma 1.4; III.D$''$ (3.4),
Proposition 3.1; III.D$'''$ Proposition 3.1; III.E$'$; III.F Lemma 2.1; III.F$'$ Proposition 2.3; III.F$'''$ Proposition
2.2; III.F$''''$ Proposition 5.1; III.G$'$ Theorem 3.1; III.G$''$ Table 1.1, (4.2)-(4.3), Theorems 3.1, 4.2, Corollary
4.3; III.G$''''$ Lemma 1.1, Propositions 4.4, 5.1; III.H Proposition 3.2, Corollaries 4.2-4.4; III.H$'$ Theorem 1.3;
III.H$''$ Lemma 3.2, Theorem 2.1, Corollary 5.1; III.I Lemma 3.6, Theorem 5.3, Remark 5.4;
III.I$'$-III.I$''''''''''''''$ as listed in Theorem 3.1; III.J Theorem 2.4; III.J$'$ Theorem 2.1; III.J$''$; III.J$'''$.
