# Part III.J. Efficient parameterisation I: approximate solutions from data, n = 4 ([Hin26] section 12 to Remark 12.6)

*Status.* Written (D282); verified (D285: verifier 122's findings seated); proved (D287: verifier 123 read the D285
repairs, seven nits seated). This part proves, at spatial dimension $n = 4$, [Hin26] Definition 12.1, the construction
of section 12.2.1 with Lemma 12.2, Theorem 12.3 and Remarks 12.4-12.6 (pp. 296-311): a tuple of data (the final black
hole parameters, the boost and translation, the free $\iota^+$-data at each $\iota^+$-resonance, the conormal remainders
of the modification parameters and a remainder tensor) determines $(h,\vec p,q)$ at which the augmented operator $P_5$
of III.I$''''''''''''''$ vanishes at $\iota^+$ to the order $5+\epsilon_+$ and has the $K^+$-order $\alpha$ (Theorem
2.4). The source's map $\Psi$ with an initial solution ((12.33)-(12.34), Lemma 12.7) needs the exterior family $h_{-S}$
of Part III.C$'$ and is deferred; its Theorem 12.8, the description of linearised solutions, is the next part, III.J$'$.

*What n = 4 changes.* (1) *No step at $t_*^{-1}$.* The source's Step 1 solves the $t_*^{-1}$-term, from the resonance at
$\lambda = 1$ and the black hole's $t_*^{-1}$-tail. At $n = 4$ the least $\iota^+$-exponent is $\lambda_\sharp =
\frac32+(1-e_\Upsilon)\gamma_\Upsilon$, a simple pole with $\mathrm{Res}_{\iota^+}(\bar L,\lambda_\sharp) = \{0\}$
(III.G$'''$ Corollary 2.6, Remark 3.8), and the black hole parameters enter at $t_*^{-2}$. (2) *The $\iota^+$-series
below $3+\epsilon_+$ is linear.* Every product of two terms has $u$-exponent at least $2\lambda_\sharp =
3+2\delta_\sharp>3+\epsilon_+$, and the background's departure from Minkowski space shifts by at least 2; so each step
is one linear equation $\bar L\,G(\lambda_0) = -F_0(\lambda_0)$ with $F_0$ depending only on the black hole parameters
(Lemma 2.1), and $\Phi$ is affine in the infinite-dimensional data, which gives its tame bounds at once. (3) *The
modification parameters* are the rows of III.I$'''''''''$ (rates at most 2) with the rotation rows of
III.I$''''''''''''''$ Definition 1.3, and the tower coefficients of $q$ (III.I$''''''''''''''$ Definition 1.1, rates
above 2); the formal solutions at $\iota^+\cap K^+$ are matched to them by III.I$''''''''''$ Lemma 2.1 (Lemma 2.2). The
source's conormal $V_{1,\mathrm{rem}}$ of (12.11) has no counterpart: at $n = 4$ the v1 coefficient of $q$ has no
conormal part (III.I$''''''''''''$ Theorem 3.1). (4) *The resonances used* are those in $\pi_1\mathcal E_\sharp$: the
forward solutions of III.I$''''''''''''''$ Theorem 3.1 excite no other, so only these carry data. (5) *Orders.*
$K^+$-order $\alpha-$ with $\alpha$ as in III.I$''''''''''''''$, read as there ((H2) as "$\alpha-$",
III.I$''''''''''''''$ Remark 3.2); $\iota^+$-order $(3+\epsilon_+)-$ for the metric and $(5+\epsilon_+)-$ for $P_5$.
Notation: Parts II.G, III.A, III.D$'''$, III.F$'$, III.G$'$, III.G$''$, III.G$'''$, III.I, III.I$'$,
III.I$'''''''$-III.I$''''''''''''''$; no instrument is used.

## 1. Setting

Everything of III.I$''''''''''''''$ section 1 is kept, and through it III.I$''''''''$-III.I$'''''''''''''$: $\alpha$,
the constants $0<\epsilon_K<\epsilon_+<\min(\delta_\sharp,\epsilon_{\mathrm{ind}})$, $w_+ = 5+\epsilon_+$, $\eta_2$,
(H1)-(H5), (C5), (G), $\Lambda$, $K(\lambda)$, $L_0$, $l_*$, $N_*$, $\mathcal E_{\mathrm{par}}$, $\mathcal E_\sharp$,
$\mathcal M$, $\mathcal E_{++}$, $\mathcal G = (2,0)\cup(2+\mathcal E_{\mathrm{ind}})$, $\mathcal F = (0,0)\cup\mathcal
E_{\mathrm{ind}}$, the rows $\mathcal N$ with the rotation rows $\mathcal N_{\mathrm{rot}}$ and the enlarged $\mathcal
P$, the towers $T_{\rho,b}$, $\mathcal R$, $\mathcal R'$, $d_\rho$, $k_\mu$, $\mathcal Q$, $h_{b,\mathrm{rem}}(q)$ and
$P_5$; $b$ ranges near $b_0$, and $\vec p_{\le0} = (S,b-b_0,S^{(0)}_1)$, with $g_0 = g_{\vec p_{\le0}}$ (III.I$'''''''$
(1.3)). From III.G$'''$: the spaces (1.2)-(3.5), the inverse (2.2) of $N_{\iota^+}(\bar L,\cdot)$ on partially
polyhomogeneous spaces, $\mathrm{spec}^{<\ell_I}_{\iota^+}(\bar L,\mathcal E^C_I)$, Corollary 3.1,
$\mathrm{Res}^k_{\iota^+}(\bar L,\mathcal E^C_I,\lambda)$, $\mathrm{Res}_{\iota^+}(\bar L,\lambda)$ and the map (3.6);
$\ell_I$ is the class's, with $\ell_I>3+\epsilon_+$ (III.I$''''''''''$ (H4)), and III.G$'''$ (1.2) holds, $s_C$ being
large by (C1). $K_\iota(\lambda)$ denotes the order of the pole of (2.2) at $\lambda$ (III.G$'''$ Proposition 3.7's
$K(\lambda)$). From III.G$''$: Table 1.1, the Minkowski formal solutions (Definition 2.3), Theorem 3.1 and Lemma 4.1.
Two further conditions, each removing finitely many values:

(G$^+$) No $\lambda\in\Lambda$ has real part in $(3,3+\epsilon_+]$. $\Lambda$ does not depend on the constants
(III.I$''''''''''$ Lemma 1.2 (a)), so this holds after decreasing $\epsilon_+$ (with $\epsilon_K$, $\eta_1$, $\eta_2$);
every statement of III.I$''''''''$-III.I$''''''''''''''$ holds for the smaller values (III.I$'''''''''$ (1.1)), the
choices of III.I$''''''''''$-III.I$''''''''''''''$ ($\eta_1$, $\eta_2$, $\delta_+$, $\alpha$) being re-made.

(A$_J$) For every $\lambda_0\in\Lambda$ with $\mathrm{Re}\,\lambda_0<3+\epsilon_+$, $\ell_K(\lambda_0) :=
\alpha-\mathrm{Re}\,\lambda_0$ is not $-\mathrm{Re}\,\mu$ for a root $\mu$ of $\widehat{L_{b_0}}(0)$ and not in
$\mathrm{Re}\,\pi_1\mathcal E_K$. Then $\ell_K(\lambda_0)\in(\alpha-3-\epsilon_+,\alpha-\lambda_\sharp]\subset(0,3)$, as
$\epsilon_+<\frac14$, so $\ell_K(\lambda_0)$ is admissible in III.G$'''$ section 1 ($\ell^{\max}_K = 3$ under (C5),
III.G$''$ section 1). The admissible $\alpha$ meeting (A$_J$) are dense in $(4+\epsilon_K-\epsilon'_0,4+\epsilon_K]$.

*Classes.* For $k\in\mathbb N_0\cup\{\infty\}$ and orders read as "$w-$" (III.I$''''''''''''''$ section 1):
$$\mathcal X^k_J := H^{k,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_+,(3+\epsilon_+)-),\alpha-}_{\mathrm
b}(\Omega_*;S^2T^*)^{\bullet,-},\qquad\mathcal F^k := H^{k,(\langle\mathcal
E^C_I+1\rangle',\ell_I+1),(5+\epsilon_+)-,\alpha-}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-},$$
the latter with a plain weight at $\iota^+$; and $\mathcal Q^k_J$ the tuples
$(S_{\mathrm{rem}},b_{\mathrm{rem}},(Y_\rho)_{\rho\in\mathcal R'})$ with $S_{\mathrm{rem}}\in\dot
H^{k,(\alpha-2)-}_{\mathrm b}$, $b_{\mathrm{rem}}\in\dot H^{k,(\alpha-1)-}_{\mathrm b}$ and $Y_\rho\in\dot H^{k,\mathcal
Q(\mathcal E^\alpha_\rho,(3+\epsilon_+-d_\rho)-)}_{\mathrm b}$. Here $\mathcal E_+$ is as in III.I$''''''''''''''$
section 1 (it contains $\mathcal E_\sharp\cap\{\mathrm{Re}<3+\epsilon_+\}$). Since $3+\epsilon_+>3+\eta_2$, $\mathcal
Q^\infty_J\subset\mathcal Q$; and $\mathcal X^\infty_J$ is the class of III.I$''''''''''''''$ with $a_+ =
(3+\epsilon_+)-$ in place of (H5). The class used by III.I$''''''''''''''$ Theorem 3.1 is discussed in III.J$'$ ((J5)
below).

*Terms at $\iota^+$.* A tensor $w$ on $\Omega_*$ that is partially polyhomogeneous at $\iota^+$ has terms
$t_*^{-\lambda}(\log t_*)^kw_{\lambda,k}(R,\omega)$, quasi-homogeneous in the coordinates $(t_*,R,\omega)$ near
$\iota^+$; we write $[w]_\lambda := \sum_kt_*^{-\lambda}(\log t_*)^kw_{\lambda,k}$ for its *$t_*^{-\lambda}$-term*. A
term $t_*^{-\lambda-2}(\log t_*)^kf$ of a source is at the *$u$-exponent* $\lambda$, so $[f]_{\lambda+2}$ is the
$u$-exponent-$\lambda$ part. By III.G$''$ Lemma 4.1, $[L_bw]_{\lambda+2} = \bar L[w]_\lambda$ when $[w]_{\lambda'} = 0$
for $\mathrm{Re}\,\lambda'\le\mathrm{Re}\,\lambda-2$; here $2\bar L(t_*^{-\lambda}w) =
t_*^{-\lambda-2}N_{\iota^+}(\lambda)w$, and the cut-off region $\{|x|\le3R_1\}$ of III.G$''$ Lemma 4.1 lies, near
$\iota^+$, in every neighbourhood of $K^+$, where orders are $K^+$-orders.

**Definition 1.1 (the data space; [Hin26] Definition 12.1 at n = 4).** Let $\Sigma :=
\mathrm{spec}^{<3+\epsilon_+}_{\iota^+}(\bar L,\mathcal E^C_I)\cap\pi_1\mathcal E_\sharp$, a finite set, and $\mathcal
R'_0 := \{\rho = (\mu,\tau)\in\mathcal R':\mu\in(-1,0]\}$ (the rows s0 and s2 at the root 0 and the class rows c0, c1).
For $k\in\mathbb N_0\cup\{\infty\}$, $\mathcal D^k$ is the space of tuples
$$U = \Big(b-b_0,\ S,\ S^{(0)}_1,\ (u^0_\lambda,f_\lambda)_{\lambda\in\Sigma},\ S_{\mathrm{rem}},\ b_{\mathrm{rem}},\
(Y_{\rho,\mathrm{rem}})_{\rho\in\mathcal R'_0},\ \tilde h\Big)\tag{1.1}$$
with $b\in\mathfrak b$; $S,S^{(0)}_1\in\mathcal S_1$; $u^0_\lambda\in\mathrm{Res}_{\iota^+}(\bar L,\lambda)$ and
$f_\lambda\in\mathrm{Poly}^{K_\iota(\lambda)}(\mathbb C_z;H^{k,(\langle\mathcal E^C_I+1\rangle',\le\ell_I+1)}_{\mathrm
b})$ (III.G$'''$ (3.5)); $S_{\mathrm{rem}}\in\dot H^{k,(\alpha-2)-}_{\mathrm b}([1,\infty];\mathcal S_1)$,
$b_{\mathrm{rem}}\in\dot H^{k,(\alpha-1)-}_{\mathrm b}([1,\infty];\mathfrak b)$, $Y_{\rho,\mathrm{rem}}\in\dot
H^{k,(3+\epsilon_+-d_\rho)-}_{\mathrm b}([1,\infty];\mathcal Y_\rho)$; and $\tilde h\in H^{k,(\langle\mathcal
E^C_I\rangle,\ell_I),(3+\epsilon_+)-,\alpha-}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-}$. The components are real, except
$(u^0_\lambda,f_\lambda)$, which are conjugation-symmetric: $(u^0_{\bar\lambda},f_{\bar\lambda}) =
\overline{(u^0_\lambda,f_\lambda)}$. Put $u_\lambda :=
u^0_\lambda+\mathrm{res}_{z=\lambda}\big(t_*^{-z}N_{\iota^+}(z)^{-1}f_\lambda(z)\big)$, the image under (3.6) of
III.G$'''$; $U_0 := (b-b_0,S,S^{(0)}_1)$; and $U_1$ the remaining components. The seminorms are those of the components,
at every loss $\epsilon>0$ in the orders "$w-$".

**Lemma 1.2 (the data's exponents).** For $\lambda\in\Sigma$, $K_\iota(\lambda)\le2l_*+1$, and $u_\lambda =
\sum_{j<K_\iota(\lambda)}t_*^{-\lambda}(\log t_*)^ju^{(\lambda,j)}$ with $(\lambda,j)\in\mathcal E_\sharp$ for
$j<K_\iota(\lambda)$, $u^{(\lambda,j)}\in H^{k-l,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_K,\ell_K)}_{\mathrm
b}(\iota^+)$ for $\ell_K<\ell^{\max}_K$, $l$ of III.G$'''$ Proposition 3.7.

*Proof.* The order of the pole of (2.2) at $\lambda$ is at most the order of $\lambda$ in $\mathrm{Spec}_{\iota^+}(\bar
L)$ plus $k(\mathcal E^C_{I,\sharp},\lambda)+1$ (III.G$'''$ Proposition 2.4, the source's Proposition 9.15), and $l_*$
bounds both the orders of the poles of $N_{\iota^+}(\bar L,\cdot)^{-1}$ and the log orders of $\mathcal E^C_I$
(III.I$''''''''''$ Definition 1.1); so $K_\iota(\lambda)\le2l_*+1$, and the residue of a pole of order
$K_\iota(\lambda)$ has log powers below $K_\iota(\lambda)$ (as does $u^0_\lambda$, a residue of a pole of
$N_{\iota^+}(\bar L,\cdot)^{-1}$). For $\mathrm{Re}\,\lambda\ge2$: $\lambda\in\Lambda$ (as $\Sigma\subset\pi_1\mathcal
E_\sharp$) and $j\le2l_*<K(\lambda)$, so $(\lambda,j)\in\mathcal E_\sharp$. For $\mathrm{Re}\,\lambda<2$:
$\mathrm{spec}_{\iota^+}(\bar L)\subset\{\mathrm{Re}\ge2\}$ (III.G$'$ Lemma 4.2 (a)), so
$\lambda\in\{\lambda_\sharp\}\cup\pi_1\mathcal E^C_I$ (III.G$'''$ Corollary 2.6), with $K_\iota(\lambda_\sharp) = 1$ and
$K_\iota(z)\le k(\mathcal E^C_I,z)+1$ for $z\in\pi_1\mathcal E^C_I$, $z\ne\lambda_\sharp$ (the pole bound of III.G$'''$
Proposition 2.4, with $m_\iota = 0$ below 2); and $\mathcal E^\sharp_+$ contains $(\lambda_\sharp,0)$ and, for each
$z\in\pi_1\mathcal E^C_I$, the extended union taken $k(\mathcal E^C_I,z)+1$ times (III.I$'$ (3.2)), so
$(\lambda,j)\in\mathcal E^\sharp_+\cap\{\mathrm{Re}<2\}\subset\mathcal M$ (III.I$''''''''$ (1.1)-(1.2)). The regularity
is III.G$'''$ Proposition 3.7. $\square$

## 2. The construction

Let $U\in\mathcal D^\infty$ be small. The construction assigns to the exponents $\lambda_0\in\Lambda_* :=
\Lambda\cap\{\mathrm{Re}<3+\epsilon_+\}$, a finite set, in order of increasing real part (exponents of equal real part
together; their equations below are independent), a correction $h_{\lambda_0}$, quasi-homogeneous of degree $\lambda_0$
in $t_*^{-1}$, row coordinates $W_\nu$ for the rows $\nu = (\tau,\lambda_0,j)$ of $\mathcal N$ and
$(\mathrm{rot},\lambda_0,j)$ of $\mathcal N_{\mathrm{rot}}$, and the polyhomogeneous coefficients of $q$ at the
exponents $(\lambda_0-d_\rho,j)$; and then
$$h := \chi_\iota\sum_{\lambda\in\Sigma}u_\lambda+\tilde h+\chi_\iota\sum_{\lambda_0\in\Lambda_*}h_{\lambda_0},\quad\vec
p := (U_0,(W_\nu)),\quad q := \big(S_{\mathrm{rem}},b_{\mathrm{rem}},(Y_{\rho,\mathrm{rem}}\ (\rho\in\mathcal
R'_0))+(\text{the polyhomogeneous coefficients})\big),\tag{2.1}$$
$\chi_\iota$ the cut-off of III.G$''$ section 4. For $(h,\vec p,q)$ of the form (2.1), and for each $\lambda_0$, put
$$G(\lambda_0) := \Big[h+\sum_{\nu\in\mathcal N\sqcup\mathcal
N_{\mathrm{rot}}}m_\nu(W_\nu)+h_{b,\mathrm{rem}}(q)\Big]_{\lambda_0},\qquad F_0(\lambda_0) := \big[P_4(0,\vec
p_{\le0})\big]_{\lambda_0+2},$$
the latter with every row coordinate 0.

**Lemma 2.1 (the $\iota^+$-terms below $3+\epsilon_+$).** For $(h,\vec p,q)$ of the form (2.1), with $U$ small,
$P_5(h,\vec p,q)$ is partially polyhomogeneous at $\iota^+$ to the weight $(5+\epsilon_+)-$, with $u$-exponents in
$\Lambda$, and for $\lambda_0\in\Lambda_*$
$$\big[P_5(h,\vec p,q)\big]_{\lambda_0+2} = F_0(\lambda_0)+\bar L\,G(\lambda_0).\tag{2.2}$$
$F_0(\lambda_0)$ depends only on $\vec p_{\le0}$, smoothly; it vanishes unless $\lambda_0\in\pi_1\mathcal G$, and its
coefficients are compactly supported in $(\iota^+)^\circ$.

*Proof.* Write $P_5(h,\vec p,q) = P_4(h'',\vec p)$, $h'' := h+h_{b,\mathrm{rem}}(q)$, and Taylor-expand $P_4$ at
$(0,\vec p_{\le0}\oplus0)$ in $h''$ and in the row coordinates $W$:
$$P_4(h'',\vec p) = P_4(0,\vec p_{\le0})+L_{0,\vec p_{\le0}}h''+\sum_\nu D_{W_\nu}P_4(0,\vec p_{\le0})(W_\nu)+Q,$$
$Q$ at least quadratic in $(h'',W)$. Every term of $h''$ and every $h_\nu(W_\nu)$, $m_\nu(W_\nu)$ has $\iota^+$-order at
least $\lambda_\sharp$: $u_\lambda$ and $h_{\lambda_0}$ by $\Lambda\subset\{\mathrm{Re}\ge\lambda_\sharp\}$
(III.I$''''''''''$ Lemma 1.2 (a)); $\tilde h$ by its class; the rows by III.I$'''''''''$ Lemma 2.2 (b) (with
III.I$''''''''''''''$ Definition 1.3); the towers by III.I$''''''''''''''$ Lemma 2.2 (a). $Q$ is of order two in its
arguments and their first two derivatives, each derivative giving a factor $\rho_+$ at $\iota^+$, so its $u$-exponents
are at least $2\lambda_\sharp = 3+2\delta_\sharp>3+\epsilon_+$ ($\epsilon_+<\delta_\sharp$, III.I$'''''''''$ (1.1)), and
it has the weight $(5+2\delta_\sharp)->w_+$. $L_{0,\vec p_{\le0}} = L^{g_0+h_{\mathrm{tot}}(\vec p_{\le0}),g_0}$ differs
from $L_{b_0}$ by coefficients of $\iota^+$-order at least 2 ($g_0-g_{b_0}$ and $h_{\mathrm{tot}}(\vec p_{\le0})$ lie in
$\iota^+$-order $\ge2$: III.I$'''''''$ (1.3) and Lemma 2.2, III.I$'''''''''$ Lemma 2.5), and $L_{b_0}$ differs from
$\bar L$, near $\iota^+$ away from $K^+$, by the term $t_*^{-\lambda-4}v^2Bw$ of III.G$''$ (4.1); so for a term $w$ of
$\iota^+$-order $\ge\lambda_\sharp$, $[L_{0,\vec p_{\le0}}w]_{\lambda_0+2} = \bar L[w]_{\lambda_0}$ for
$\mathrm{Re}\,\lambda_0<\lambda_\sharp+2$, which contains $\Lambda_*$. Likewise $D_{W_\nu}P_4(0,\vec
p_{\le0})(W)-D_{W_\nu}P_4(0,0)(W)$ consists of terms bilinear in $(\vec p_{\le0},W)$ (through $g_0$,
$h_{\mathrm{tot}}(\vec p_{\le0})$ and $\delta^*_{g_0,E_C}$, III.I$'''''''''$ (2.3)) of $u$-exponent
$\ge\lambda_\sharp+2$, and $D_{W_\nu}P_4(0,0)(W) = L_{b_0}m_\nu(W)$ (III.I$'''''''''$ Lemma 2.4; for the rotation rows
III.I$''''''''''''''$ Definition 1.3), so its $u$-exponent-$\lambda_0$ term is $\bar L[m_\nu(W)]_{\lambda_0}$. Summing
gives (2.2). The conormal remainders: $\tilde h$ and the conormal parts of $q$ have $\iota^+$-order $(3+\epsilon_+)-$
(III.I$''''''''''''''$ Lemma 2.2 (a), with $3+\epsilon_+$ for $3+\eta_2$; $S_{\mathrm{rem}}$, $b_{\mathrm{rem}}$ give
$(\alpha+1)-$), which $L_{0,\vec p_{\le0}}$ maps to the weight $(5+\epsilon_+)-$; the rows' terms of $u$-exponent
$\ge3+\epsilon_+$ have the weight $w_+$ (III.I$'''''''''$ Lemma 2.6 (b): the plain weight
$a_++\mathrm{Re}\,\lambda+2-\epsilon$); and $P_4(0,\vec p_{\le0})$ is smooth in $\vec p_{\le0}$ and supported in
$\mathrm{supp}\,d\chi_K$: there $g_0$ is a pulled-back Myers-Perry metric, so $\mathrm{Ric}(g_0) = 0$ off
$\mathrm{supp}\,d\chi_K$ (III.I$'''''''$ (1.3)), and $h_{\mathrm{tot}}(\vec p_{\le0})$, $\vartheta_{\mathrm{tot}}(\vec
p_{\le0})$ are supported in $\mathrm{supp}\,d\chi_K$ (III.I$'''''''$ Definition 2.3), a set whose closure meets
$\iota^+$ in a compact subset of $(\iota^+)^\circ$ ($\chi_K$ is a function of $R$ near $\iota^+$, equal to 1 near $R =
0$ and to 0 near $\mathscr I^+$). Its $\iota^+$-exponents lie in $\mathcal G$ (III.I$'''''''$ Lemma 2.2,
III.I$'''''''''$ Lemma 2.5), and those of every other term lie in $\Lambda$ (Lemma 2.3, which (2.2) does not use).
$\square$

**Lemma 2.2 (rows and towers at $\iota^+$).** Let $\lambda_0\in\Lambda_*$ and $j\in\mathbb N_0$.

(a) For $\nu = (\tau,\lambda_0,j)$ (whose $\iota^+$-exponent is $\lambda_0$, III.I$'''''''''$ Lemma 2.2 (b)) with
$\tau\in\mathcal T\setminus\{\mathrm v1\}$, $\mu_{\mathrm s0} = \mu_{\mathrm s2} := 0$, $\mu_{\mathrm s1} := -1$,
$\mu_{\mathrm c0},\mu_{\mathrm c1}$ the class roots, and $W\in\mathcal W_{\tau,\mathbb C}$: $[m_\nu(W)]_{\lambda_0}$ is
$\chi_K$ times $t_*^{-\lambda_0}$ times a finite sum $\sum_{i\le j}(\log t_*)^i\phi_i$, whose $R\to0$ expansion is the
formal solution of III.G$''$ Theorem 3.1 of type $\tau$ at the root $\mu_\tau$ with coefficient $c_\tau(\lambda_0)W$ in
the top log power $j$, plus formal solutions of the same type with lower log powers, plus terms of $K^+$-order
$\ge\mathrm{Re}\,\lambda_0+3$. Here $c_{\mathrm s1}(\lambda_0) = \lambda_0(\lambda_0-1)$ and $c_\tau = 1$ otherwise. The
same holds for the rotation rows $\nu = (\mathrm{rot},\lambda_0,j)$, $(\lambda_0,j)\in\mathcal M_{\mathrm{rot}}$,
$W\in\mathcal V_{1,\mathbb C}$, with the v1 formal solution and $c_{\mathrm v1} = -\lambda_0$.

(b) For $\rho = (\mu,\tau)\in\mathcal R'$ and $Y\in\mathcal Y_\rho$, $[\chi_KT_{\rho,b}(t_*^{-(\lambda_0-d_\rho)}(\log
t_*)^jY)]_{\lambda_0}$ is $\chi_K$ times the formal solution of type $\tau$ at $\mu$ with coefficient $Y$ (and, for v1,
coefficient $-\lambda_0Y$) in the top log power, plus lower log powers, plus terms of $K^+$-order
$\ge\mathrm{Re}\,\lambda_0+3$; it does not depend on $b$.

*Proof.* (a) By III.I$''''''''''$ Lemma 2.1 (a), $m_\nu(W) = \chi_K\big(\sum_{i\le K_\tau}a_\nu^{(i)}\breve
h^i_\tau(W)+a_\nu^{(K_\tau+1)}dt_*\otimes_s\breve\omega^{K_\tau}_\tau(W)\big)$. The stationary tensors $\breve h^i_\tau$
are polyhomogeneous at $\partial X$ with leading terms homogeneous of degree $\mu_\tau-i$ (for s1 the leading orders are
$\rho^3$, $\rho^2$, then $\rho^{1-i}$ for $i\ge2$; for s0, $\breve h^0_{\mathrm s0} = 0$ and $\breve h^{i+1}_{\mathrm
s0}$ has degree $-i$), the Myers-Perry corrections being smaller by $\mathcal E_{\mathrm{ind}}$ (III.G$''$ section 2.2,
III.I$''''''''''$ Lemma 2.1 (b), III.I$'''''''''$ (2.1)), and $a_\nu^{(i)}$ is a combination of $t_*^{-e_\nu-i}(\log
t_*)^{i'}$, $i'\le j$. Near $\iota^+$, $r = Rt_*$, so $a^{(i)}_\nu\breve{\bar h}^i_\tau$ is quasi-homogeneous of degree
$\lambda_0$ in $t_*^{-1}$ (for s0, s2, c0, c1, $e_\nu+\mu_\tau = \lambda_0$, as $d_\tau = -\mu_\tau$; for s1, whose
$\breve{\bar h}^i$ has degree $1-i$, $e_\nu+1 = \lambda_0$; for v1, $e_\nu = \lambda_0$) and has $K^+$-order
$\mathrm{Re}\,e_\nu+i$; the corrections have $u$-exponents in $\lambda_0+\mathcal E_{\mathrm{ind}}$. For s1 the terms $i
= 0,1$ ($\rho^3$, $\rho^2$) have $u$-exponent $\lambda_0+2$, and the rest is $\sum_{i\ge2}a_\nu^{(i)}\breve{\bar
h}^i_{\mathrm s1} = \bar h^{\le K}_{\mathrm s1}(a_\nu'')$ (III.G$''$ (2.5)) with $a_\nu'' =
\lambda_0(\lambda_0-1)t_*^{-\lambda_0-1}(\log t_*)^j+\dots$; for s0, $\sum_{i\ge1}A_\nu^{(i)}\breve{\bar h}^i_{\mathrm
s0} = \sum_ir_\nu^{(i)}\breve{\bar h}^{i+1}_{\mathrm s0}$ with $r_\nu = t_*^{-\lambda_0}(\log t_*)^j$; for s2, c0, c1,
$\sum_ia_\nu^{(i)}\breve{\bar h}^i_\tau = \bar h^{(\mu_\tau),\le K_\tau}_\tau(a_\nu)$ with $a_\nu =
t_*^{-\lambda_0+\mu_\tau}(\log t_*)^j$. Comparing with III.G$''$ Theorem 3.1's (3.1) (and its $(\log t_*)^j$-version,
III.G$'''$ Corollary 3.1 (2)): the terms with $i\le k_{\mu_\tau}$ (for s1 the convention $\bar h^{\le3}_{\mathrm s1}$,
$i\le3$) are the formal solution, with coefficient $c_\tau(\lambda_0)W$ in the top log power; derivatives of $(\log
t_*)^j$ produce the lower powers; and the terms with $i>k_{\mu_\tau}$ and the $dt_*$-term have $K^+$-order
$\ge\mathrm{Re}\,e_\nu+k_{\mu_\tau}+1\ge\mathrm{Re}\,\lambda_0+3$ (III.G$''$ Table 1.1: $k_\mu\ge2+\mu$, and for s1 $k =
3$). For the rotation rows the same computation applies with $\breve h^0_{\mathrm v1} = h_{b_0,\mathrm v1} = 0$
(III.I$''''''''''''''$ Definition 1.3): $\sum_{i\ge1}a_\nu^{(i)}\breve{\bar h}^i_{\mathrm v1} = \bar h^{\le K}_{\mathrm
v1}(a_\nu')$ (III.G$''$ (2.5)), $a_\nu' = -\lambda_0t_*^{-\lambda_0-1}(\log t_*)^j+\dots$. (b) $T_{\rho,b} =
h^{(\mu),\le k_\mu}_{b,\tau}$ (III.G$''$ Definition 2.5), whose leading part at $\partial X$ is the Minkowski tower of
III.G$''$ Definition 2.3 and does not depend on $b$ (III.I$''''''''''''''$ Lemma 2.1); with $a =
t_*^{-\lambda_0+\mu}(\log t_*)^jY$ for $\rho$ other than v1, and for v1, $h^{\le2}_{b,\mathrm v1}(a)$ has the leading
part $\bar h^{\le2}_{\mathrm v1}(a')$, $a = t_*^{-\lambda_0}(\log t_*)^jY$ (III.G$''$ (2.5), (2.7); $h_{b,\mathrm
v1}\in\mathcal A^3$ contributes at $u$-exponent $\ge\lambda_0+3$). $\square$

**Step $\lambda_0$.** Suppose every choice for the exponents of real part below $\mathrm{Re}\,\lambda_0$ is made. Let
$T(\lambda_0) := G(\lambda_0)$ computed with these choices only (no data, correction, row or coefficient at $\lambda_0$
itself): the $t_*^{-\lambda_0}$-terms of the rows and towers already chosen, which arise from their Myers-Perry
corrections ($\lambda_0\in\lambda+\pi_1\mathcal E_{\mathrm{ind}}$). Put
$$f := -F_0(\lambda_0)-\bar L\,T(\lambda_0),\qquad v := u_{\lambda_0}+\mathcal S_{\lambda_0}(f),$$
with $u_{\lambda_0} := 0$ if $\lambda_0\notin\Sigma$, and $\mathcal S_{\lambda_0}(f)$ the solution of $\bar L\mathcal S
= f$ that III.G$'''$ Corollary 3.1 (1), which solves $2\bar Lu = \cdot$, gives for $2f$, with $\ell_K =
\ell_K(\lambda_0)$. By III.G$'''$ Corollary 3.1 (2) and Remark 3.3, $v = \chi_Kv_0+\tilde v$, with $v_0$ a sum of formal
solutions of III.G$''$ Theorem 3.1 (with $(\log t_*)^i$, $i\le J$) at the roots $\mu\in\mathcal W(\ell_K(\lambda_0))$
and $\tilde v$ a sum of terms $t_*^{-\lambda_0}(\log t_*)^iH^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\ell_K(\lambda_0)}_{\mathrm b}(\iota^+)$, so of $K^+$-order $\alpha-$. Each formal solution in
$v_0$, of type $\tau$ at the root $\mu$, has $K^+$-order $\mathrm{Re}(\lambda_0-\mu)<\alpha$, as
$-\mathrm{Re}\,\mu<\ell_K(\lambda_0)$, and is carried below by a row or tower, of rate $\mathrm{Re}(\lambda_0-\mu)$
except for the boost row s1 (rate $\mathrm{Re}\,\lambda_0-1$) and for v1 at a rotating $b$ (rate
$\mathrm{Re}\,\lambda_0$). We assign, top log power first:

(i) the terms of type $\tau\in\mathcal T\setminus\{\mathrm v1\}$ at $\mu_\tau$ whose row has rate
$\mathrm{Re}\,e_\nu\le2$ to the row $\nu = (\tau,\lambda_0,i)$, with $W_\nu := c_\tau(\lambda_0)^{-1}$ times the
coefficient; by (G) these are all the s1, s0, s2, c0, c1 terms of rate $\le2+\epsilon_K$, and the s1 terms
have $\mathrm{Re}\,\lambda_0\le3$;

(ii) the v1 terms with $\mathrm{Re}\,\lambda_0\le2$, whose exponents lie in $\mathcal M_{\mathrm{rot}}$ (Lemma 2.3;
III.I$''''''''''''''$ Definition 1.1), to the rotation row $(\mathrm{rot},\lambda_0,i)$, with $W := c_{\mathrm
v1}(\lambda_0)^{-1}$ times the coefficient;

(iii) every other term, of type $\tau$ at $\mu$ with rate in $(2,\alpha)$ (the s0, s2, c0, c1 terms of rate $>2$, the v1
terms with $\mathrm{Re}\,\lambda_0>2$, and the rows of Table 1.1 with $\mu\le-1$ other than s1 and v1, of rate
$\ge\mathrm{Re}\,\lambda_0+1>\frac52$), to the coefficient of $Y_\rho$, $\rho = (\mu,\tau)$, at the exponent
$(\lambda_0-d_\rho,i)$: the coefficient itself (for v1, $-\lambda_0^{-1}$ times it).

Since the lower log powers that each assignment produces (Lemma 2.2) are of the same type, the assignment proceeds
downward in the log power and is unique. Let $R(\lambda_0)$ be the sum of $[m_\nu(W_\nu)]_{\lambda_0}$ and
$[\chi_KT_{\rho,b}(\cdot)]_{\lambda_0}$ over the rows and coefficients just assigned, and put
$$h_{\lambda_0} := \mathcal S_{\lambda_0}(f)-R(\lambda_0).$$
Then $[h]_{\lambda_0} = u_{\lambda_0}+h_{\lambda_0} = v-R(\lambda_0)$ has, by Lemma 2.2, the same formal solutions
removed, so it is $\tilde v$ plus terms of $K^+$-order $\ge\mathrm{Re}\,\lambda_0+3>\alpha$: its $K^+$-order is
$\alpha-$. And $G(\lambda_0) = [h]_{\lambda_0}+R(\lambda_0)+T(\lambda_0) = v+T(\lambda_0)$, so by (2.2) and $\bar
Lu_{\lambda_0} = 0$
$$\big[P_5(h,\vec p,q)\big]_{\lambda_0+2} = F_0(\lambda_0)+\bar L\,\mathcal S_{\lambda_0}(f)+\bar L\,T(\lambda_0) =
0.\tag{2.3}$$
The choices at higher real part change no $t_*^{-\lambda_0}$-term: their own terms and their corrections have
$u$-exponents of larger real part.

The hypotheses of III.G$'''$ Corollary 3.1 hold: $\mathrm{Re}\,\lambda_0<3+\epsilon_+<\ell_I$; $\ell_K(\lambda_0)$ is
admissible by (A$_J$); and $f$ has no $\mathscr I^+$-expansion (it vanishes near $\mathscr I^+\cap\iota^+$: $F_0$ is
supported in $\mathrm{supp}\,d\chi_K$, the rows and towers in $\mathrm{supp}\,\chi_K$), and its coefficients have
$K^+$-order $\ge\alpha$, so lie in $H^{\infty,\ell_K(\lambda_0)-2}_{\mathrm b}$ at $R = 0$: $F_0$ is compactly supported
in $(\iota^+)^\circ$, and $\bar LT(\lambda_0) = [L_{b_0}\sum m_\nu+L_b\chi_K\sum T_{\rho,b}]_{\lambda_0+2}$ by Lemma
2.1's proof ($[L_bw]_{\lambda+2} = \bar L[w]_\lambda$ as for $L_{b_0}$, $L_b-\bar L$ raising the $u$-exponent by 2 near
$\iota^+$ away from $K^+$, III.G$''$ (4.1)), where $L_{b_0}m_\nu = f^\nu_{0,0}$ has $K^+$-weight
$\kappa_\nu-\epsilon>\frac92>\alpha$ (III.I$'''''''''$ Lemma 2.2 (d)) and $L_bT_{\rho,b}(a)$ consists of the terms with
$a^{(k_\mu+1)}$, $a^{(k_\mu+2)}$, of $K^+$-order $\ge\mathrm{Re}\,\lambda_0+3$ (III.G$''$ Lemma 2.6), the commutators
with $\chi_K$ being supported away from $K^+$. As $f$ has no $\mathscr I^+$-expansion, (2.2) acts on it as III.G$'$
Theorem 3.1 (2)'s inverse (III.G$'''$ Proposition 2.4's construction with $f$ of plain $\mathscr I^+$-weight), whose
poles lie in $\mathrm{spec}_{\iota^+}(\bar L)\subset\{\mathrm{Re}\ge2\}$: below 2, $\mathcal S_{\lambda_0}$ raises no
log power, and above 2 it raises it by at most $l_*$.

**Lemma 2.3 (the log count).** Every exponent $(\lambda_0,i)$ of the construction (of $[h]_{\lambda_0}$, of the rows
assigned and of the coefficients of $q$, shifted by $d_\rho$) lies in $\mathcal E_\sharp$; the rows assigned lie in
$\mathcal N\sqcup\mathcal N_{\mathrm{rot}}$, and the coefficients of $q$ in $\mathcal Q^\infty_J$.

*Proof.* By induction over $\Lambda_*$ in order of real part. The log powers at $\lambda_0$ come from: the data
$u_{\lambda_0}$, $\le2l_*$ (Lemma 1.2); $F_0(\lambda_0)$, $\le L_0$ ($\mathcal G$, III.I$''''''''''$ Definition 1.1);
the corrections of rows and towers chosen at $\lambda<\lambda_0$, $\le K(\lambda)+l_*$ by induction, as
$\lambda_0\in\lambda+\pi_1\mathcal E_{\mathrm{ind}}$ and the log orders of $\mathcal E_{\mathrm{ind}}$ are $\le l_*$;
and $\mathcal S_{\lambda_0}$ adds at most $l_*$ for $\mathrm{Re}\,\lambda_0\ge2$ and nothing below 2. For
$\mathrm{Re}\,\lambda_0\ge2$, $\lambda_0\in\Lambda$ has $n(\lambda_0)\ge n(\lambda)+1$ for each such $\lambda$, so
$K(\lambda_0)\ge K(\lambda)+(N_*+1)(l_*+1)\ge K(\lambda)+2l_*$ and $K(\lambda_0)\ge L_0+(N_*+1)(l_*+1)$: every log power
is $\le K(\lambda_0)$. Below 2: the data lie in $\mathcal M$ (Lemma 1.2), $F_0(\lambda_0) = 0$ ($\mathcal
G\subset\{\mathrm{Re}\ge2\}$), the corrections of terms at exponents in $\mathcal M$ lie in $\mathcal M+\mathcal
E_{\mathrm{ind}}$, which below 2 is in $\mathcal M$ (III.I$''''''''$ (1.1), III.I$''''''''''''$ section 1), and no log
is raised. So $(\lambda_0,i)\in\mathcal E_\sharp$. The rows: a row assigned in (i) is $(\tau,\lambda_0,i)$ with
$(\lambda_0,i)\in\mathcal E_\sharp$ and $\mathrm{Re}\,\lambda_0\le3$ (its rate $\mathrm{Re}\,\lambda_0+d_\tau\le2$,
$d_\tau\ge-1$), hence $(\lambda_0,i)\in\mathcal E_{\mathrm{par}}$ (III.I$''''''''''$ (1.2)) and $\nu\in\mathcal N$; the
rotation rows of (ii) are in $\mathcal N_{\mathrm{rot}}$, their exponents lying in $\mathcal
E_\sharp\cap\{\mathrm{Re}\le2\} = \mathcal M_{\mathrm{rot}}$. The coefficients of (iii):
$(\lambda_0-d_\rho,i)\in\mathcal E_\sharp-d_\rho$ with rate $>2$, which is $\mathcal E^\alpha_\rho$
(III.I$''''''''''''''$ Definition 1.1; for v1, $\mathrm{Re}\,\lambda_0>2$), and
$\mathrm{Re}(\lambda_0-d_\rho)<3+\epsilon_+-d_\rho$, below the conormal order of $\mathcal Q^\infty_J$. $\square$

**Theorem 2.4 ([Hin26] Theorem 12.3 at n = 4).** There are $d\in\mathbb N$ and $\epsilon_0>0$ such that for
$U\in\mathcal D^\infty$ with $\|U\|_{\mathcal D^d}<\epsilon_0$ the construction defines
$$\Phi(U) = (h,\vec p,q) = \Phi_0(U_0)+A(U_0)U_1\in\mathcal X^\infty_J\times\mathcal P\times\mathcal
Q^\infty_J,\tag{2.4}$$
with $\Phi_0$ smooth on $\{|U_0|<\epsilon_0\}$, $\Phi_0(0) = 0$, and $A(U_0)$ linear, smooth in $U_0$, and bounded from
the $U_1$-components of $\mathcal D^{k+d}$ to $\mathcal X^k_J\times\mathcal P\times\mathcal Q^k_J$ for every $k$, with
bounds uniform in $|U_0|<\epsilon_0$. So $\Phi$ extends continuously to $\mathcal D^{k+d}\to\mathcal X^k_J\oplus\mathcal
P\oplus\mathcal Q^k_J$, is smooth (in particular $N$-fold differentiable for every $N$), and is tame: $\|\Phi(U)\|_k\le
C_k\|U\|_{\mathcal D^{k+d}}$. Moreover
$$P_5(\Phi(U))\in\mathcal F^{k-2}\quad\text{for }U\in\mathcal D^{k+d},\tag{2.5}$$
and:

(1) the components $S$, $b-b_0$, $S^{(0)}_1$ of $\vec p$ are those of $U$;

(2) the components $S_{\mathrm{rem}}$, $b_{\mathrm{rem}}$ of $q$ are those of $U$, the conormal part of $Y_\rho$ is
$Y_{\rho,\mathrm{rem}}$ for $\rho\in\mathcal R'_0$ and 0 otherwise, and replacing $\tilde h$ by $\tilde h+\tilde h'$
replaces $h$ by $h+\tilde h'$;

(3) if $U$ and $U'$ differ only in $(u^0_{\lambda_0},f_{\lambda_0})$, by $(u'^0,f')$, and $u'_{\lambda_0}$ is the image
of $(u'^0,f')$ under (3.6) of III.G$'''$, then $(h',\vec p\,',q') := \Phi(U')-\Phi(U)$ has: $h'$ with $\iota^+$-terms
only at exponents of real part $\ge\mathrm{Re}\,\lambda_0$; no row or coefficient of $q$ at an exponent of real part
below $\mathrm{Re}\,\lambda_0$; and $[h']_{\lambda_0} = u'_{\lambda_0}-R'(\lambda_0)$, where $R'(\lambda_0)$, the
$t_*^{-\lambda_0}$-term of the rows and coefficients of $(\vec p\,',q')$ at $\lambda_0$, has the same formal solutions
at $R = 0$ as $u'_{\lambda_0}$ of rate below $\alpha$;

(4) $\Phi$ commutes with conjugation: $h$, $q$ are real and the row coordinates conjugation-symmetric.

*Proof.* The construction is well defined by Lemmas 2.1-2.3 and III.G$'''$ Corollary 3.1. *Membership.* $h$: its
$\mathscr I^+$-data are $(\langle\mathcal E^C_I\rangle,\ell_I)$ (the $u_\lambda$, $\mathcal S_{\lambda_0}(f)$ and
$\tilde h$; the $R(\lambda_0)$ vanish near $\mathscr I^+$); at $\iota^+$ it is partially polyhomogeneous with exponents
in $\mathcal E_\sharp\subset\mathcal E_+$ (Lemma 2.3) to the order $(3+\epsilon_+)-$ ($\tilde h$); at $K^+$ each
$[h]_{\lambda_0}$ has order $\alpha-$ (Step $\lambda_0$), so $\chi_\iota[h]_{\lambda_0}$ does, and $\tilde h$ does.
$\vec p\in\mathcal P$ and $q\in\mathcal Q^\infty_J$ by Lemma 2.3. *(2.5).* At $\iota^+$: by Lemma 2.1 and (2.3), every
$u$-exponent of real part below $3+\epsilon_+$ has vanishing term, so $P_5(\Phi(U))$ has the plain weight
$(5+\epsilon_+)-$. At $\mathscr I^+$: $h+h_{b,\mathrm{rem}}(q)+h_{\mathrm{tot}}(\vec p)$ is small in the class of III.I
(1.4) with the $\mathscr I^+$-data $(\langle\mathcal E^C_I\rangle,\ell_I)$, the rows and towers vanishing near $\mathscr
I^+$, so III.I Corollary 4.2 gives the $\mathscr I^+$-order $(\langle\mathcal E^C_I+1\rangle',\ell_I+1)$. At $K^+$: near
$K^+$, $g_0 = g_b$, the rows enter only through $\vartheta_{\nu,\sharp}$, of $K^+$-weight $\kappa_\nu-\epsilon>\alpha$
(III.I$'''''''''$ Lemma 2.2 (d); $h_\nu$ is supported in $\mathcal C$), and $P_5-P_4(h,\vec p) =
L_bh_{b,\mathrm{rem}}(q)+\int_0^1(L_{h+sh_{b,\mathrm{rem}}(q),\vec p}-L_b)h_{b,\mathrm{rem}}(q)\,ds$ with
$L_bh_{b,\mathrm{rem}}(q)$ of $K^+$-order $\alpha-$ (III.I$''''''''''''''$ Lemma 2.2 (b)) and the integral of
$K^+$-order $(2\alpha-4)->\alpha$ at every $b$ near $b_0$ (as in III.I$''''''''''''''$ Lemma 2.4 (c)'s proof):
$h_{b,\mathrm{rem}}(q)$ has $K^+$-order $(\alpha-2)-$ there, its v1 part included, whose exponents have real part $>2$,
hence $>2+\epsilon_K\ge\alpha-2$ by (G), even where $h_{b,\mathrm v1}$ does not vanish (III.I$''''''''''''''$ Definition
1.1; the v1 terms of real part $\le2$ are the rotation rows', which enter only through $h_\nu$ and $\vartheta_\nu$); and
$P_4(h,\vec p)$ near $K^+$ is $\mathrm{Ric}(g_b+h)-\delta^*_{g_b,E_C}(\Upsilon(g_b+h,g_b)-\vartheta_{\mathrm{tot}})$,
whose linear part $L_bh$ has $K^+$-order $\alpha-$ ($h$ has; $L_b$ is stationary), and whose nonlinear part has
$K^+$-order $\ge2(\alpha-)$. *Structure.* Given $U_0$, every map of the construction is linear in $U_1$: $F_0$ depends
on $U_0$ only (Lemma 2.1), and $T(\lambda_0)$, $\mathcal S_{\lambda_0}$, the coefficient functionals of III.G$''$
Theorem 3.1 and III.G$'''$ Corollary 3.1 (2), the assignment and $R(\lambda_0)$ are linear; the dependence on $U_0$ is
through $F_0$, smooth in $\vec p_{\le0}$, and through the towers $T_{\rho,b}$, smooth in $b$ (III.I$''''''''''''''$
Lemma 2.1). This is (2.4), $\Phi_0(U_0)$ being the construction with $U_1 = 0$. *Bounds.* There are finitely many steps;
each uses III.G$'''$ Corollary 3.1 on a strip containing $\lambda_0$, with a fixed loss of b-regularity (III.G$'''$
Proposition 2.4, (G$'''$4)), the functionals of III.G$''$ Theorem 3.1 (continuous on $H^{k+2}_{\mathrm b}$) and
III.G$'''$ Proposition 3.7 (loss $l$); $d$ is the sum of these losses plus 2. The bounds are uniform for $|U_0|$ small,
since $F_0$ and the towers are. As $U_0$ is finite-dimensional, $|U_0|\le C\|U\|_{\mathcal D^0}$, and the tame bound
follows from (2.4). *(1), (2)* hold by (2.1). *(3)* By linearity in $U_1$, $\Phi(U')-\Phi(U) =
A(U_0)(0,\dots,(u'^0,f'),\dots,0)$; in the construction with these data, every step below $\mathrm{Re}\,\lambda_0$ has
$u = 0$, $F_0 = 0$ and $T = 0$, so assigns nothing; at $\lambda_0$, $f = 0$ and $v = u'_{\lambda_0}$, so
$[h']_{\lambda_0} = u'_{\lambda_0}-R'(\lambda_0)$ with $R'(\lambda_0)$ removing exactly the formal solutions of
$u'_{\lambda_0}$. *(4)* $\bar L$, $\chi_K$, $\chi_\iota$, the states and the cut-offs are real, conjugation maps the
construction at $\lambda_0$ to that at $\bar\lambda_0$, and the data are conjugation-symmetric. $\square$

**Remark 2.5 (linearisation; the source's Remark 12.4).** Differentiating (2.5) in $U$: for $U'\in\mathcal D^\infty$,
$D_{\Phi(U)}P_5\big(D_U\Phi(U')\big)\in\mathcal F^\infty$, and $D_U\Phi(U') =
D\Phi_0(U_0)U'_0+\big(DA(U_0)U'_0\big)U_1+A(U_0)U'_1$; parts (1)-(4) hold for $D_U\Phi$ with the obvious changes. So
$D_U\Phi(U')$ is an approximate solution of the linearised equation at $\Phi(U)$, to the orders of $\mathcal F$.

**Remark 2.6 (interpretation and the forward problem; the source's Remarks 12.5-12.6).** By (3), each datum
$(u^0_\lambda,f_\lambda)$ enters $h$ as $u_\lambda$ minus the rows and tower coefficients that remove its expansion at
$K^+$ below the rate $\alpha$; the removed terms are pure gauge for the rows (types s1, v1, s0, s2, c0, c1 at rates
$\le2$) and zero energy towers for $q$. As in the source, the construction is much simpler than the forward problem of
III.I$''''''''$-III.I$''''''''''''''$: it uses only the Minkowski model at $\iota^+$ and the formal solutions at
$\iota^+\cap K^+$, whereas the forward solutions' $K^+$-expansion requires the full spectral analysis. At $n = 4$ it is
moreover linear below $3+\epsilon_+$, by the dimension count of (2) above.

## 3. Findings, labels and sources

(J1) *Linear below $3+\epsilon_+$.* At $n = 4$ the $\iota^+$-orders of the metric perturbation start at
$\lambda_\sharp>\frac32$, so the quadratic part of the gauge-fixed Einstein operator acts only at $u$-exponents
$\ge3+2\delta_\sharp>3+\epsilon_+$; the source's iteration, nonlinear at $n = 3$ (its terms of size $t_*^{-1}$
interact), is here a finite sequence of linear model problems. $\Phi$ is affine in the infinite-dimensional data, with
coefficients smooth in the black hole, boost and translation parameters, which makes its smoothness and tame bounds
immediate.

(J2) *The exponent $\lambda_\sharp$.* The step sources $f$ have no $\mathscr I^+$-expansion: $F_0$ is supported in
$\mathrm{supp}\,d\chi_K$ and the rows and towers in $\mathrm{supp}\,\chi_K$. So no step source carries the exceptional
term $v^{\lambda_\sharp+1}e_7$ at $\mathscr I^+\cap\iota^+$, and the pole of (2.2) at $\lambda_\sharp$ enters only
through the datum $f_{\lambda_\sharp}$. This settles, for the construction, the reading that III.G$'''$ (G$'''$1) left
to this part: section 12's linear grafting errors do not reach the frequency $\lambda_\sharp$ with an exceptional
$\mathscr I^+$-term.

(J3) *The resonances used.* Only the resonances in $\pi_1\mathcal E_\sharp$ carry data (Definition 1.1). The forward
solutions of III.I$''''''''''''''$ Theorem 3.1 have $\iota^+$-exponents in $\mathcal E_\sharp$, so the next part needs
no others; a pure $\iota^+$-resonance outside $\Lambda$ is excited by no source of the iteration.

(J4) *Rotation rows.* The v1 terms of the data of real part at most 2 (below 2, and at 2 for (2.5)) are assigned to the
rotation rows of III.I$''''''''''''''$ Definition 1.3, not to $q$, for the reason recorded there.

(J5) *For III.J$'$ (Theorem 12.8).* Two points must be settled there. (a) III.I$''''''''''''''$ Theorem 3.1 gives $h'$
the $\iota^+$-order $(3+\eta_2)-$, $\eta_2<\epsilon_+$ (it inherits III.I$''''''''''''$'s), while $\Phi$ and $\mathcal
F$ use $(3+\epsilon_+)-$ and $(5+\epsilon_+)-$; the linearised solution must reach $(3+\epsilon_+)-$, or the scheme must
absorb the difference. (b) The parts III.I$''''''''$-III.I$''''''''''''''$ are at $b = b_0$ ((I3) of III.I); $\Phi$ is
defined for $b$ near $b_0$, and the linear theory at $b\ne b_0$ is open there.

(J6) *Deferred.* The source's map $\Psi$ ((12.33)-(12.34), Lemma 12.7) adds an initial solution $h_{-S}$ in $t_*\le2$
and uses its Corollary 5.15 (1) near $\mathscr I^+$; it is deferred to after Part III.C$'$.

*Labels.* Definition 1.1 is the source's Definition 12.1; Lemma 2.1 and Step $\lambda_0$ its section 12.2.1 with Lemma
12.2 (at $n = 4$ the orders of $f$ at $R = 0$ are those of Step $\lambda_0$); Theorem 2.4 its Theorem 12.3; Remarks
2.5-2.6 its Remarks 12.4-12.6. Lemmas 1.2, 2.2, 2.3, conditions (G$^+$), (A$_J$) and the affine structure (2.4) are new
at $n = 4$.

*Sources.* [Hin26] pp. 296-311 (section 12 to Remark 12.6: Definition 12.1, (12.11)-(12.32), Lemma 12.2, Theorem 12.3,
Remarks 12.4-12.6), read at source. Inputs: III.D$'''$ (3); III.G$'$ Lemma 4.2; III.G$''$ Table 1.1, section 2.2,
Definitions 2.3, 2.5, Lemma 2.6, Theorem 3.1, section 4, Lemma 4.1; III.G$'''$ (1.2)-(3.6), Proposition 2.4, Corollaries
2.6, 3.1, Remarks 3.3, 3.8, Proposition 3.7; III.I (1.4), Corollary 4.2; III.I$'$ (3.2); III.I$'''''''$ (1.3),
Definition 2.3, Lemma 2.2; III.I$''''''''$ (1.1)-(1.2); III.I$'''''''''$ (1.1), (2.1), (2.3), Lemmas 2.2, 2.4-2.6;
III.I$''''''''''$ Definition 1.1, Lemma 1.2, Definition 1.3, Lemma 2.1; III.I$''''''''''''$ section 1;
III.I$''''''''''''''$ Definitions 1.1-1.3, Lemmas 2.1-2.2, 2.4, Remark 3.2.
