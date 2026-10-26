# Part III.I$''''''''''$. Towers, row expansions and the spacetime phase, n = 4 ([Hin26] Theorem 11.59, first half)

*Status.* Written (D272); verified (D274: verifier 116's findings seated, to be read). This part and the next,
III.I$'''''''''''$, prove at spatial dimension $n = 4$ Parts 1-3 of the proof of [Hin26] Theorem 11.59 (pp. 278-289):
with the correction terms of III.I$'''''''''$ the forward solution can be made to decay at $K^+$ at the order
$2+\epsilon_K$ (the source's (11.222)). This part fixes the parameter exponents (section 1), proves the facts about
towers, row expansions and Fourier tails that both parts use (section 2), and carries out the part of the argument that
takes place in spacetime (section 3): the $\iota^+$-terms of the source of $u$-exponent below 2 are solved by the
$\iota^+$-normal operator up to the $K^+$-order $\alpha\le4+\epsilon_K$, and the $K^+$-terms this produces below
$\alpha-2$ are identified as rows of III.I$'''''''''$ (Proposition 3.1). What is left is a forward problem whose source
is partially polyhomogeneous at $\iota^+$ from the order 4 on; its $K^+$-expansion comes from the zero-energy structure,
and III.I$'''''''''''$ treats it and the elimination.

*What n = 4 changes.* (1) *The spacetime window.* Under (C5) the $K^+$-range of the $\iota^+$-normal operator is
$\ell^{\max}_K = 3$ (III.G$''$ (1.1)), so III.G$''$ Corollary 4.3 solves the term at the $u$-exponent $\lambda_0$,
$\mathrm{Re}\,\lambda_0<2$, with $\ell_K = \alpha-\mathrm{Re}\,\lambda_0$ for every $\alpha\le4+\epsilon_K$, not only
for $\alpha<3$ as in III.I$''''''''$; the source uses its Proposition 9.11 at $\lambda = 1$ only (Steps 2.A.2 and 4.1).
(2) *The rows it produces* are now all of the rows of III.I$'''''''''$ with $\mathrm{Re}\,\lambda<2$, with the first
companion of the boost tower, and are identified through the towers (Lemma 2.1). (3) *The parameter exponents* (the
source's $\tilde{\mathcal E}'_{++}$, built after its proof by the procedure of (11.186)) are fixed in advance
(Definition 1.1), with log orders that grow with the real part; the rows' own sources never pass through the
construction, as $f^\nu = Lm_\nu+r^\nu$ exactly (III.I$'''''''''$ Lemma 2.6), and this is how the self-consistency of
the source's Remark 11.62 enters. (4) Two further conditions: (H4) $\ell_I>3+\epsilon_+$, and the gap condition (G) on
$\epsilon_K$. Notation: Parts II.E, III.A, III.A$'$, III.D$''$, III.D$'''$, III.F$'$, III.F$'''$, III.G$'$, III.G$''$,
III.G$''''$, III.I-III.I$'''''''''$; no instrument is used.

## 1. Setting

Everything of III.I$'''''''''$ section 1 is kept: $b = b_0$, its enlarged $\mathcal E_{\mathrm{ind}}$, $\mathcal F =
(0,0)\cup\mathcal E_{\mathrm{ind}}$, $\mathcal E_{++}$, $\mathcal M$, $\mathcal G$, $\tilde{\mathcal E}_+$, $2\mathcal
E_+$, $\delta_\sharp\in(0,\frac14)$, the constants (1.1) there, $w_+ = 5+\epsilon_+$, (H1)-(H3), the rows $\mathcal T$,
$d_\tau$, $e_\nu$, $\mathcal N$, the coefficient spaces (with $\mathcal W_{\mathrm v1} = 0$ at $b_0$), $\mathcal
E_{\mathrm{rows}}$, $\mathcal E_{\mathrm{src}}$ with (1.3), and $\mathcal Y_1(\alpha)$, $\mathcal Y_2(\alpha)$,
$\mathcal Y(\alpha)$; and its section 2: $K_\tau$, $\breve\omega^i_\tau$, (2.1), the states $h_\tau$, $r_\nu$, $a_\nu$,
$m_\nu$, $h_\nu$, $\vartheta_\nu$, $P_4$, $L_{h,\vec p}$, $f^\nu_{h,\vec p}$ and $r^\nu_{h,\vec p}$. $\mathcal
E^\sharp_+$ is III.I$'$ Proposition 3.1's set (3.2), $\lambda_\sharp = \frac32+(1-e_\Upsilon)\gamma_\Upsilon$, $\mathcal
E^\iota_{\mathrm{ind}}$ the index set of III.G$''$ (4.4), and $\epsilon_{\mathrm{ind}}$ III.G$''''$ Proposition 5.1's.
Definition 2.1 and Lemma 2.2 (b), (e) of III.I$'''''''''$ extend verbatim to every triple $(\tau,\lambda,k)$ with
$\tau\in\mathcal T$, $\mathrm{Re}\,\lambda\ge\lambda_\sharp$, $k\in\mathbb N_0$, and $m_\nu$, $r_\nu$ denote these also
for $\nu\notin\mathcal N$. Two further hypotheses:

(C5) $\gamma_Cv_C\ge\frac12$ (III.G$''$ section 1), so that $\ell^{\max}_K = \min(3,2+2\gamma_Cv_C) = 3$ (III.G$''$
(1.1)).

(H4) $\ell_I>3+\epsilon_+$, with $\ell_I$ off the discrete exclusion sets of III.I$'$ Proposition 3.1 and III.G$''$
Theorem 4.2. As $\ell_I\le a_I$ (III.I$''''''''$ section 1; used in III.I$'''''''''$ Lemma 2.6 (a), which section 1
below uses), this asks $a_I>3+\epsilon_+$ of the class (the source's class has the $\mathscr I^+$-order $3+\epsilon_I$);
$\ell_I<\frac32+s_C$ (III.G$''$ Theorem 4.2) is no restriction, $s_C$ being large by (C1).

*The sources.* Fix $\mathcal E_{\mathrm{src}}$ as the least choice in III.I$'''''''''$ (1.3), and put
$$\mathcal E^0_{\mathrm{src}} := \tilde{\mathcal E}_+\cup2\mathcal E_+\cup\big(\mathcal
E_{\mathrm{rows}}\cap\{\mathrm{Re}<2\}\big),\qquad\mathcal E_{\mathrm{src}} = \mathcal E^0_{\mathrm{src}}\cup\mathcal
E_{\mathrm{rows}}.\tag{1.1}$$
$\mathcal Y^0_1(\alpha)$, $\mathcal Y^0_2(\alpha)$, $\mathcal Y^0(\alpha)$ are $\mathcal Y_1(\alpha)$, $\mathcal
Y_2(\alpha)$, $\mathcal Y(\alpha)$ with $\mathcal E^0_{\mathrm{src}}$ in place of $\mathcal E_{\mathrm{src}}$. They hold
the sources of the theorem (the $n = 4$ analogue of (11.195)) and the derivatives $f^S_{h,\vec p}$, $f^{\mathrm
s1}_{h,\vec p}$ ($\mathcal Y^0(\alpha)$) and $f^b_{h,\vec p}$ ($\mathcal Y^0_2(\alpha)$) of III.I$'''''''''$ Lemma 2.6
(a): the term $(\partial\delta^*_{g_0,E_C})\vartheta_{\mathrm{rows}}$ there has plain $\iota^+$-weight
$\lambda_\sharp+4>w_+$ (its proof), and the rest is III.I$'''''''$ Lemma 3.1's, with index sets $\tilde{\mathcal E}_+$
and $2\mathcal E_+$. The row exponents with real part at least 2 enter only through $f^\nu_{h,\vec p} = L_{h,\vec
p}m_\nu+r^\nu_{h,\vec p}$, where $r^\nu_{h,\vec p}$ has no index set (III.I$'''''''''$ (2.5)).

*The parameter exponents.*

**Definition 1.1.** Let $\Lambda\subset\mathbb C$ be the smallest set, closed under conjugation, that contains
$$\pi_1\big(\mathcal E_{++}\cup\mathcal G\cup\mathcal E^C_I\big)\cup\{\lambda_\sharp,3\}\cup\big(2+\pi_1\mathcal
E_{\mathrm{col}}\big)$$
and satisfies $\Lambda+w\subset\Lambda$ for $w\in\pi_1(\mathcal E_{\mathrm{ind}}\cup\mathcal
E^\iota_{\mathrm{ind}})\cup\{1\}$; here $\mathcal E_{++}$ is the least choice in III.I$''''''''$ (1.1), and $\mathcal
E_{\mathrm{col}}\subset\{\mathrm{Re}\ge0\}$ is the index set at $\partial X$ of the column terms at $b_0$
(III.I$'''''''''''$ Lemma 1.1). Let $\eta_0 := \min\big(\mathrm{Re}\,\pi_1(\mathcal E_{\mathrm{ind}}\cup\mathcal
E^\iota_{\mathrm{ind}})\cup\{1\}\big)>0$ and $N_* := \lceil5/\eta_0\rceil+2$; let $l_*\in\mathbb N_0$ bound, at real
part $\le5$, the log orders of $\mathcal E_{\mathrm{ind}}\cup\mathcal E^\iota_{\mathrm{ind}}\cup\mathcal E^C_I$, the
orders of the poles of $N_{\iota^+}(\bar L,\cdot)^{-1}$ (III.G$'$ Lemma 4.2) and the multiplicities of the indicial
roots of $\widehat{L_{b_0}}(0)$ (III.F$'$ Proposition 2.3); and let $L_0\in\mathbb N$ bound the log orders of $\mathcal
E^0_{\mathrm{src}}\cup\mathcal E_{++}\cup\mathcal G\cup(2+\mathcal E_{\mathrm{col}})$ at real part $<2\lambda_\sharp$,
and only there (Lemma 1.2 (b)). For $\lambda\in\Lambda$ let $n(\lambda)$ be the number of $\lambda'\in\Lambda$ with
$\mathrm{Re}\,\lambda'<\mathrm{Re}\,\lambda$, and $K(\lambda) := L_0+(N_*+1)(l_*+1)(n(\lambda)+1)$. Put
$$\mathcal E_{\mathrm{par}} := \mathcal M\cup\{(\lambda+j,k):\lambda\in\Lambda,\ 2\le\mathrm{Re}\,\lambda\le3,\ k\le
K(\lambda),\ j\in\mathbb N_0\}.\tag{1.2}$$

The number $3\in\Lambda$ is the $u$-exponent of the boost row that the zero-energy mass state produces
(III.I$'''''''''''$); the increment 1 accounts for the Taylor levels of the spectral construction there, and
$2+\pi_1\mathcal E_{\mathrm{col}}$ for the column terms at its first Taylor level.

**Lemma 1.2.** (a) $\Lambda\cap\{\mathrm{Re}\le R\}$ is finite for every $R$,
$\Lambda\subset\{\mathrm{Re}\ge\lambda_\sharp\}$, and $\Lambda\cap\{\mathrm{Re}<2\} = \pi_1\mathcal M$.

(b) $\mathcal E_{\mathrm{par}}$ is an index set, closed under conjugation, with III.I$'''''''''$ (1.2), and $\mathcal
E_{\mathrm{par}}\cap\{\mathrm{Re}\le3\} = \mathcal M\cup\{(\lambda,k):\lambda\in\Lambda,\ 2\le\mathrm{Re}\,\lambda\le3,\
k\le K(\lambda)\}$. $\mathcal E_{\mathrm{par}}$ does not depend on $\mathcal E_+$. Hence (H3), which asks $\mathcal
E_+\supset(\lambda,k)+\mathcal F$ for the rows, can be imposed on the class together with (H1): the $n = 4$ form of the
source's Remark 11.62.

(c) (*The log count.*) Applied to sources in $\mathcal Y^0(\alpha)$, the constructions of section 3 and of
III.I$'''''''''''$ change index sets only by: adding $(w,l)\in\mathcal E_{\mathrm{ind}}\cup\mathcal
E^\iota_{\mathrm{ind}}\cup\{(1,0)\}$ to an exponent; unions with the column exponents $(2+j,0)+\mathcal
E_{\mathrm{col}}$ at the Taylor level $j+1$ (III.I$'''''''''''$ Lemma 2.2), of log orders $\le L_0$; extended unions
with $\mathcal E^C_I$ (III.I$'$ (3.2)) or with the indicial roots (III.A Lemma 1.4), each raising the log order at one
exponent by at most $l_*+1$; and raising the log order at a treated exponent by a pole order of $N_{\iota^+}(\bar
L,\cdot)^{-1}$ (III.G$''$ Corollary 4.3) or by 1 (III.G$''''$ Proposition 4.4 at $\alpha_0 = 2$, its Remark 4.5). At an
exponent of real part $\le3+\epsilon_+$ at most $N_*$ such raises occur (each belongs to one window of section 3's
iteration, of width at least $\eta_0$ below 2, or to one Taylor level of III.I$'''''''''''$, of which there are four).
Hence every exponent $(\lambda,k)$ produced with $2\le\mathrm{Re}\,\lambda\le3+\epsilon_+$ has $\lambda\in\Lambda$ and
$k\le K(\lambda)$. These are all the exponents recorded: the $\iota^+$-data of $\mathcal Y^0(\alpha)$ stop at the weight
$w_+-\epsilon$, that is at the $u$-exponent $3+\epsilon_+-\epsilon$.

*Proof.* (a) The generators are index sets of real parts $\ge\lambda_\sharp$ ($\mathcal E_{++}\subset\mathcal E_+$ by
(H1); $\min\mathrm{Re}\,\mathcal E^C_I>\frac32+2\gamma_\Upsilon>\lambda_\sharp$, III.I$'''''$ Step 1), finitely many
below every bound, and the increments have real part $\ge\eta_0$; so below $R$ only sums with at most $R/\eta_0$
increments occur. Below 2 the generators lie in $\pi_1\mathcal E_{++}$: $\lambda_\sharp$ does, and so does every element
of $\pi_1\mathcal E^C_I$ below 2, as III.I$'$ (3.2) puts it into $\mathcal E^\sharp_+$ and $\mathcal
E_{++}\supset\mathcal E^\sharp_+\cap\{\mathrm{Re}<2\}$ ((H1)); $\mathcal G$, 3 and $2+\pi_1\mathcal E_{\mathrm{col}}$
have real part $\ge2$. And $\pi_1\mathcal E_{++}\cap\{\mathrm{Re}<2\}$ is closed under the increments below 2
(III.I$''''''''$ (1.1); $+1$ leaves $\{\mathrm{Re}<2\}$ as $\lambda_\sharp+1>2$). So $\Lambda\cap\{\mathrm{Re}<2\} =
\pi_1\mathcal M$.

(b) An index set: finitely many exponents below each bound by (a), finitely many logs at each, and closed under
$(z,k)\mapsto(z+1,k)$, as $\Lambda+1\subset\Lambda$, $K(\lambda+1)\ge K(\lambda)$ ($n(\lambda+1)>n(\lambda)$), and for
$(z,k)\in\mathcal M$, $z+1\in\Lambda$ has real part in $[2,3)$ and $k\le L_0\le K(z+1)$ ($\mathcal M\subset\mathcal
E_{++}$). The part below 3: if $\mathrm{Re}(\lambda+j)\le3$ with $j\ge1$, then $\mathrm{Re}\,\lambda = 2$, $j = 1$, and
$K(\lambda)\le K(\lambda+1)$. Conjugation: $\Lambda$ is closed under it and $n(\bar\lambda) = n(\lambda)$, $\mathcal M =
\bar{\mathcal M}$. III.I$'''''''''$ (1.2): $\min\mathrm{Re}\,\mathcal E_{\mathrm{par}}\ge\lambda_\sharp$, and $\mathcal
E_{\mathrm{par}}\cap\{\mathrm{Re}<2\} = \mathcal M$. *Independence of $\mathcal E_+$.* The increments have positive real
parts, so $\Lambda\cap\{\mathrm{Re}<R\}$ is determined by the generators of real part $<R$, and $\mathcal
E_{\mathrm{par}}$ by $\Lambda\cap\{\mathrm{Re}\le3\}$ and $L_0$. Below $2\lambda_\sharp = 3+2\delta_\sharp>3+\epsilon_+$
(III.I$'''''''''$ (1.1)) nothing used involves $\mathcal E_+$: $\mathcal G$, $\mathcal E^C_I$ and $\mathcal
E_{\mathrm{col}}$ do not; the parts of $\mathcal E^0_{\mathrm{src}}$ (and of $\mathcal E_{\mathrm{rows}}$) that involve
$\mathcal E_+$, namely $\mathcal E_++\mathcal G$, $2\mathcal E_+$ and $(\lambda,k)+\mathcal F+\mathcal E_+$, have real
part $\ge2\lambda_\sharp$ by (H1); and the least $\mathcal E_{++}$ of III.I$''''''''$ (1.1) agrees below
$2\lambda_\sharp$ with the least index set that contains $\mathcal E^\sharp_+\cap\{\mathrm{Re}<2\}$ and is closed under
$+(\mathcal E^\iota_{\mathrm{ind}}\cup\mathcal E_{\mathrm{ind}})$, since adding an element of $\mathcal E_+$ lands at
real part $\ge2\lambda_\sharp$. So $\Lambda\cap\{\mathrm{Re}\le3\}$, $L_0$ and $\mathcal E_{\mathrm{par}}$ do not depend
on $\mathcal E_+$, and the conditions on $\mathcal E_+$ ((H1); (H3), which gives $\mathcal E_+\supset\mathcal
E_{\mathrm{par}}+\mathcal F$ with III.I$''''''''$ (1.1); and $\mathcal E_+\supset\mathcal
E^\sharp_+\cap\{\mathrm{Re}<2\}$, $\mathcal E_++(\mathcal E^\iota_{\mathrm{ind}}\cup\mathcal
E_{\mathrm{ind}}\cup\mathcal E_+)\subset\mathcal E_+$ there) are conditions on $\mathcal E_+$ alone: the least index set
containing $\mathcal E_{\mathrm{par}}+\mathcal F$ and $\mathcal E^\sharp_+\cap\{\mathrm{Re}<2\}$ and closed under these
additions meets them, its exponents being sums of exponents of real part $\ge\lambda_\sharp$. (As first written, $L_0$
bounded the log orders up to the real part 5; then (H3) put $(2,K(2))$ into $\mathcal E_+$, hence $(4,K(2))$ into
$\mathcal E_++\mathcal G\subset\mathcal E^0_{\mathrm{src}}$, and $L_0\ge K(2)>L_0$: verifier 116's major finding.)

(c) The exponents produced lie in $\Lambda$, which contains the generators and is closed under the additions listed (the
exponent 4 of III.G$''''$ (4.3), at the Taylor level $j$ of III.I$'''''''''''$, is the $u$-exponent $3+j$). Log orders,
by induction on $n(\lambda)$: the log order at $\lambda$ is the largest over its contributions, each either a
generator's or a column exponent's ($\le L_0$, as $\mathrm{Re}\,\lambda\le3+\epsilon_+<2\lambda_\sharp$) or
$(\lambda',k')+(w,l)$ with $\mathrm{Re}\,\lambda'<\mathrm{Re}\,\lambda$, $k'\le K(\lambda')$ and $l\le l_*$, plus at
most $N_*(l_*+1)$ from the raises at $\lambda$. As $n(\lambda)\ge n(\lambda')+1$,
$K(\lambda)-K(\lambda')\ge(N_*+1)(l_*+1)\ge l_*+N_*(l_*+1)$, and $L_0+N_*(l_*+1)\le K(\lambda)$. $\square$

**Definition 1.3 (the gap and admissible orders).** (G) $\epsilon_K$ is so small that no $\lambda\in\Lambda$ has real
part in $(2,2+\epsilon_K]\cup(3,3+\epsilon_K]$, and no $\lambda+d_{\mathrm c0}$ or $\lambda+d_{\mathrm c1}$,
$\lambda\in\Lambda$, has real part in $(2,2+\epsilon_K]$. This is possible by Lemma 1.2 (a), as $\Lambda$ does not
depend on $\epsilon_K$; it implies $d_{\mathrm c0},d_{\mathrm c1}>\epsilon_K$ ($2\in\Lambda$). III.I$'''''''''$ (1.1)
may be kept, decreasing $\epsilon_K$. A number $\alpha\in(2,4+\epsilon_K]$ is *admissible* if: for $\alpha<3$, it is
admissible in the sense of III.I$''''''''$; for $\alpha\ge3$, $\alpha>4+\epsilon_K-\epsilon'_0$, with $\epsilon'_0 :=
\frac12\min(\epsilon_K,\epsilon_+-\epsilon_K)$, and $\alpha$ avoids the finite set of values for which
$\alpha-\mathrm{Re}\,\lambda_0$, $\lambda_0\in\Lambda$, $\mathrm{Re}\,\lambda_0<2$, equals $-\mathrm{Re}\,\mu$ for a
root $\mu$ of $\widehat{L_{b_0}}(0)$ or lies in $\mathrm{Re}\,\pi_1\mathcal E_K$ (III.G$'$ Lemma 1.3), and the finite
exclusion set of III.I$'''''''''''$ section 1.

For admissible $\alpha\ge3$ the rows of $K^+$-rate below $\alpha-2$ are exactly $\mathcal N$: a row with
$(\lambda,k)\in\mathcal E_{\mathrm{par}}$ has rate $\mathrm{Re}\,\lambda-1\le2$ (s1), $\mathrm{Re}\,\lambda$ (s0, s2) or
$\mathrm{Re}\,\lambda+d_\tau$ (c0, c1), and by (G) no such rate lies in $(2,2+\epsilon_K]\supset(2,\alpha-2)$.

## 2. Towers, row expansions and Fourier tails

**Lemma 2.1 (towers).** Let $\tau\in\mathcal T$, $W\in\mathcal W_{\tau,\mathbb C}$ and put $\breve h^i_\tau(W) :=
\widehat{\delta^*_{g_{b_0}}}(0)\breve\omega^i_\tau(W)+dt_*\otimes_s\breve\omega^{i-1}_\tau(W)$, $i\ge0$, with
$\breve\omega^{-1}_\tau := 0$ and $\breve\omega^i_\tau := 0$ for $i>K_\tau$.

(a) For every function $a = a(t_*)$ and $K\le K_\tau$,
$$\delta^*_{g_{b_0}}\Big(\sum_{i=0}^Ka^{(i)}\breve\omega^i_\tau(W)\Big) = \sum_{i=0}^Ka^{(i)}\breve
h^i_\tau(W)+a^{(K+1)}dt_*\otimes_s\breve\omega^K_\tau(W).\tag{2.1}$$
So $m_\nu(W) = \chi_K\big(\sum_{i\le K_\tau}a_\nu^{(i)}\breve
h^i_\tau(W)+a_\nu^{(K_\tau+1)}dt_*\otimes_s\breve\omega^{K_\tau}_\tau(W)\big)$ for $\nu = (\tau,\lambda,k)$, and $\breve
h^0_\tau = h_\tau$ for $\tau\ne\mathrm s0$, while $\breve h^0_{\mathrm s0} = 0$ and $\breve h^1_{\mathrm s0} =
h_{\mathrm s0}$.

(b) The towers of III.G$''$ Definition 2.5 at $b_0$ for the types of $\mathcal T$ are these: $h^{\le k}_{b_0,\mathrm
s1}(aS) = \sum_{i\le k}a^{(i)}\breve h^i_{\mathrm s1}(S)$, $h^{(0),\le k}_{b_0,\mathrm s0}(aY) = \sum_{i\le
k}a^{(i)}\breve h^{i+1}_{\mathrm s0}(Y)$, and $h^{(\mu),\le k}_{b_0,\tau}(aY) = \sum_{i\le k}a^{(i)}\breve h^i_\tau(Y)$
for $\tau = \mathrm s2,\mathrm c0,\mathrm c1$ (with $\mu = 0,\mu_{\mathrm c0},\mu_{\mathrm c1}$), for $k$ up to
III.G$''$ Table 1.1's $K$.

(c) Let $\lambda_0\in\mathbb C$, $\mathrm{Re}\,\lambda_0\ge\lambda_\sharp$, $j\in\mathbb N_0$, and let $u_{b_0,0}$ be
III.G$''$ (4.3) at $b_0$ with $\lambda_0$ for $\lambda$, a factor $(\log t_*)^j$ in each argument, and coefficients
$S^{(-1)}_1$, $V^{(-1)}_1$, $Y^{(\mu)}_\tau$. For $\tau\in\mathcal T\setminus\{\mathrm v1\}$ let $\nu_\tau :=
(\tau,\lambda_\tau,j)$ with $\lambda_\tau := \lambda_0$, and $W_{\mathrm s1} :=
(\lambda_0(\lambda_0-1))^{-1}S^{(-1)}_1$, $W_\tau := Y^{(\mu_\tau)}_\tau$ otherwise ($\mu_{\mathrm s0} = \mu_{\mathrm
s2} := 0$). Then
$$\chi_Ku_{b_0,0}-\sum_{\tau\in\mathcal T\setminus\{\mathrm v1\}}m_{\nu_\tau}(W_\tau)\ \text{has }K^+\text{-weight
}\mathrm{Re}\,\lambda_0+1-\epsilon\text{ for every }\epsilon>0.\tag{2.2}$$

(d) For a tempered $a$ with Fourier transform $\hat a(\sigma) = \int e^{i\sigma t_*}a\,dt_*$, the Fourier transform in
$t_*$ of $\delta^*_{g_{b_0}}\big(\sum_{i\le K}a^{(i)}\breve\omega^i_\tau(W)\big)$ is $\hat a(\sigma)T^K_\tau(\sigma,W)$,
with the polynomial
$$T^K_\tau(\sigma,W) := \sum_{i=0}^K(-i\sigma)^i\breve h^i_\tau(W)+(-i\sigma)^{K+1}dt_*\otimes_s\breve\omega^K_\tau(W) =
\widehat{\delta^*_{g_{b_0}}}(\sigma)\sum_{i=0}^K(-i\sigma)^i\breve\omega^i_\tau(W).\tag{2.3}$$

*Proof.* (a) $\delta^*_{g_{b_0}}(\varphi(t_*)v) = \varphi\,\widehat{\delta^*}(0)v+\varphi'\,dt_*\otimes_sv$ for
stationary $v$ (III.I$''''$ (1.2)); sum over $i$ and collect the terms with $a^{(i)}$. For s0, $\breve\omega^0_{\mathrm
s0}$ is Killing, so $\breve h^0_{\mathrm s0} = 0$, and $\breve h^1_{\mathrm s0} =
\delta^*(t_*\breve\omega^0+\breve\omega^1) = h_{\mathrm s0}$ (III.I$'''''''''$ section 2).

(b) III.G$''$ Table 1.1's state column takes the states and their companions from III.D$''$ Proposition 3.1 and
III.D$'''$ Proposition 3.1 (1)-(7), the same 1-form towers as III.I$'''''''''$ Definition 2.1 (whose list cites the same
items), under $\delta^*_{g_b}$: the tower of $L_b$-solutions $\delta^*\omega^{\le k}$, $\omega^{\le k} = \sum_{i\le
k}\frac{k!}{(k-i)!}t_*^{k-i}\breve\omega^i$, is by (2.1) with $a = t_*^k$ the polynomial $\sum_{i\le
k}\frac{k!}{(k-i)!}t_*^{k-i}\breve h^i$, which is III.G$''$ Lemma 2.1 (a)'s description of a tower with companions
$\breve h^i$; for s0 the state is $h^{(0)}_{b,\mathrm s0} = \breve h^1$ and the index is shifted by one.

(c) By (b), the term of $u_{b_0,0}$ of type $\tau$ is the sum over $i\le k_\tau$ (III.G$''$ Table 1.1's $k_\mu$: 3 for
s1, 2 for s0, s2, c0, c1) of $a^{(i)}$ times companions, with $a = c\,r_{\nu_\tau}$: for s1, $a_{\mathrm s1}(\log t_*)^j
= (\lambda_0(\lambda_0-1))^{-1}t_*^{-\lambda_0+1}(\log t_*)^j$ (III.G$''$ (4.2); $\lambda_0\ne1$); for s0, $s2$, c0, c1,
$t_*^{-\lambda_0+\mu}(\log t_*)^j = r_{\nu_\tau}$ (for s0, $a = r_\nu = A_\nu'$, III.I$'''''''''$ Definition 2.1). By
(a), $m_{\nu_\tau}(W_\tau)$ is the same sum with $K_\tau\ge k_\tau$ in place of $k_\tau$ plus
$a^{(K_\tau+1)}dt_*\otimes_s\breve\omega^{K_\tau}$ (for s0, $K_{\mathrm s0}-1 = 3\ge k_{\mathrm s0}$ after the shift of
index), times $\chi_K$. The difference carries only $a^{(i)}$ with $i\ge k_\tau+1\ge3$, of $K^+$-weight
$\mathrm{Re}\,e_{\nu_\tau}+3-\epsilon\ge\mathrm{Re}\,\lambda_0+2-\epsilon$. The v1 terms carry $a_{\mathrm v1}^{(i)}$
with $i\ge1$ ($h_{b_0,\mathrm v1}(V) = 0$, as every $V\in\mathcal V_1$ is Killing at $b_0$, III.I$'''''''''$ section 1),
of weight $\mathrm{Re}\,\lambda_0+1-\epsilon$; the rows of III.G$''$ (4.3) outside $\mathcal T$ have roots $\mu$ with
$\mathrm{Re}\,\mu\le-1$ and rate $\mathrm{Re}(\lambda_0-\mu)\ge\mathrm{Re}\,\lambda_0+1$. On compact spatial sets
$\chi_K = 1$ for large $t_*$, and the stationary companions are smooth there.

(d) $\int e^{i\sigma t}a^{(i)}dt = (-i\sigma)^i\hat a(\sigma)$, and (2.1). $\square$

**Lemma 2.2 (joint injectivity of the states).** For each $\tau\in\mathcal T\setminus\{\mathrm
v1\}$ let $W_\tau\in\mathcal W_{\tau,\mathbb C}$. If $\sum_\tau h_\tau(W_\tau) = 0$, then every $W_\tau = 0$.

*Proof.* At the static, spherically symmetric $b_0$, every construction of III.D$''$ and III.D$'''$ stays in its
isotypic component (III.D$'''$ Proposition 3.1's proof, *Types*), and $\breve\omega^0_\tau(W)$ is of scalar type of
degree $l_\tau$ (0 for s0 and c0, 1 for s1 and c1, 2 for s2; III.D$''$ Proposition 3.1, III.D$'''$ Proposition 3.1 (1),
(4)-(7)); for s0, whose state is $\delta^*(t_*\breve\omega^0+\breve\omega^1)$, $\breve\omega^1_{\mathrm s0}$ is of
degree 0 as well (III.D$'''$ Proposition 3.1 (1)). So $h_\tau(W)$ lies in the isotypic component of degree $l_\tau$, and
these components are independent. Degree 2: $h_{\mathrm s2}$ is injective (III.I$'''''''''$ Lemma 2.2 (f)). Degree 0:
$h_{\mathrm c0}(W_{\mathrm c0})\in\mathcal A^{(\mu_{\mathrm c0},0)+\mathcal F}$ has a nonzero $\rho^{\mu_{\mathrm
c0}}$-coefficient if $W_{\mathrm c0}\ne0$ (III.I$'''''''''$ Lemma 2.2 (f)'s proof), while $h_{\mathrm s0}(W_{\mathrm
s0})\in\mathcal A^{(0,0)+\mathcal F}$ (III.D$'''$ (3.1), with $(2,0)\in\mathcal E_{\mathrm{ind}}$, III.I$'''''''''$
section 1) and $\mu_{\mathrm c0}<0\le\min\mathrm{Re}\,\mathcal F$; so $W_{\mathrm c0} = 0$, and then $W_{\mathrm s0} =
0$. Degree 1: the same with $h_{\mathrm s1}(S)\in\mathcal A^{(3,0)\cup(3+\mathcal E_{\mathrm{ind}})}$ (III.F$'''$
Proposition 4.1 (4.2)) and $\mu_{\mathrm c1}<0$. $\square$

**Corollary 2.3 (uniqueness of row expansions).** Let $\mathcal N'$ be a finite set of rows $\nu = (\tau,\lambda,k)$,
$\tau\ne\mathrm v1$, and $W_\nu\in\mathcal W_{\tau,\mathbb C}$. If $\sum_{\nu\in\mathcal N'}m_\nu(W_\nu)$ has
$K^+$-weight $w>\max_{\mathcal N'}\mathrm{Re}\,e_\nu$, then every $W_\nu = 0$.

*Proof.* Suppose not, and let $e_0$ be the least real part of $e_\nu$ over the $\nu$ with $W_\nu\ne0$. By
III.I$'''''''''$ Lemma 2.2 (e), $m_\nu(W)-\chi_Kr_\nu h_\tau(W)$ has $K^+$-weight $\mathrm{Re}\,e_\nu+1-\epsilon$, so on
every compact spatial set, for large $t_*$,
$$\sum_{(e,k):\,\mathrm{Re}\,e = e_0}t_*^{-e}(\log t_*)^k\sum_{\tau}h_\tau(W_{(\tau,e-d_\tau,k)}) =
O(t_*^{-e_0-\delta})$$
for some $\delta>0$, the inner sum over the $\tau$ with $(\tau,e-d_\tau,k)\in\mathcal N'$. The functions $t_*^{-e}(\log
t_*)^k$, finitely many and distinct, with $\mathrm{Re}\,e = e_0$, are linearly independent modulo
$O(t_*^{-e_0-\delta})$: with $s = \log t_*$, a nonzero $\sum_{e,k}c_{e,k}s^ke^{-is\,\mathrm{Im}\,e}$ does not tend to 0
as $s\to\infty$. So each inner sum vanishes on $X^\circ$, and Lemma 2.2 gives $W_\nu = 0$ for those $\nu$, a
contradiction. $\square$

**Lemma 2.4 (forward tails).** Let $V$ be a Fréchet space, $\beta>-1$, $\beta\notin\mathbb N_0$, $E\subset\mathbb
C\times\mathbb N_0$ finite with $-1<\mathrm{Re}\,z<\beta$ for $(z,m)\in E$, $a^\pm_{z,m}\in V$ for $(z,m)\in E$, and
$r^\pm\in C^\infty(\pm(0,c];V)$ with $(\sigma\partial_\sigma)^jr^\pm = O(|\sigma|^\beta)$ for all $j$. Let $\chi\in
C^\infty_c((-c,c))$ equal 1 near 0,
$$v(\sigma) := \chi(\sigma)\sum_\pm1_{\pm\sigma>0}\Big(\sum_{(z,m)\in
E}|\sigma|^z(\log|\sigma|)^ma^\pm_{z,m}+r^\pm(\sigma)\Big),\qquad w := \mathcal F^{-1}v,$$
and suppose $w(t) = O(|t|^{-\beta-1})$ as $t\to-\infty$. Then:

(a) for $z\in\mathbb N_0$, with $M$ the largest $m$ such that $(z,m)\in E$: $a^-_{z,M} = (-1)^za^+_{z,M}$, that is, the
coefficients of $\sigma^z(\log|\sigma|)^M$ on the two sides agree; this is III.A Proposition 4.2's matching condition
(4.4) at $z$;

(b) as $t\to+\infty$, for every $\delta>0$,
$$w(t) = \sum_{(z,m)\in E}\sum_{j\le m}t^{-z-1}(\log t)^jb_{z,j}+O(t^{-\beta-1+\delta}),$$
where $b_{z,j}$ is a linear combination, with coefficients depending only on $z$, $m$, $j$, of the $a^+_{z,m'}$ with
$m'\ge j$, and with $m'\ge j+1$ if $z\in\mathbb N_0$; in particular the log-free terms $|\sigma|^za^\pm_{z,0}$ with
$z\in\mathbb N_0$ contribute nothing.

*Proof.* We use $\hat w(\sigma) = \int e^{i\sigma t}w\,dt$. For $\mathrm{Re}\,z>-1$ let $s^\pm_z := (\sigma\pm i0)^z$,
the boundary values from $\pm\mathrm{Im}\,\sigma>0$ of $\sigma^z$ (principal branch, $\arg\sigma\in(0,\pi)$ resp.
$(-\pi,0)$), and $s^\pm_{z,m} := \partial^m_zs^\pm_z = (\sigma\pm i0)^z(\log(\sigma\pm i0))^m$; on $\sigma>0$ both equal
$\sigma^z(\log\sigma)^m$, on $\sigma<0$ they equal $|\sigma|^z(\log|\sigma|\pm i\pi)^m e^{\pm i\pi z}$. As
$\int_0^\infty e^{i\sigma t}t^a\,dt = \Gamma(a+1)e^{i\pi(a+1)/2}(\sigma+i0)^{-a-1}$ for $\mathrm{Re}\,a>-1$, continued
analytically, $\mathcal F^{-1}s^+_z = c(z)t_+^{-z-1}$ with $c(z) := e^{i\pi z/2}/\Gamma(-z)$, entire, with simple zeros
exactly at $\mathbb N_0$ (where $s^+_z = s^-_z = \sigma^z$ is a polynomial), and $\mathcal F^{-1}s^-_z = \bar c(\bar
z)\,t_-^{-z-1}$ likewise, with $t_- := -t$ on $t<0$. Differentiating in $z$: $\mathcal F^{-1}s^+_{z,m} =
\partial^m_z(c(z)t_+^{-z-1})$, supported in $t\ge0$, equal for $t>0$ to $\sum_{j\le m}\binom mjc^{(m-j)}(z)(-\log
t)^jt^{-z-1}$; its top log power is $m$ with coefficient $(-1)^mc(z)\ne0$ if $z\notin\mathbb N_0$, and $m-1$ with
coefficient $(-1)^{m-1}mc'(z)\ne0$ if $z\in\mathbb N_0$, $m\ge1$. The same holds for $s^-_{z,m}$ on $t<0$ with $|t|$.
Multiplying by $\chi$ changes the inverse transforms by $\mathcal F^{-1}((1-\chi)s)$, smooth on $t\ne0$ and
$O(|t|^{-\infty})$, as $(1-\chi)s$ is smooth and a symbol in $\sigma$. And $\mathcal F^{-1}(\chi1_\pm r^\pm) =
O(|t|^{-\beta-1+\delta})$: on $|\sigma|<|t|^{-1}$ the integrand is $O(|\sigma|^\beta)$; on $|\sigma|>|t|^{-1}$ integrate
by parts $\lceil\beta\rceil+1$ times, using $|\partial^j_\sigma r^\pm|\le C|\sigma|^{\beta-j}$ (with the boundary terms
at $|\sigma| = |t|^{-1}$ of the same size).

Fix $z$ with $(z,m)\in E$ for some $m$ and let $M$ be the largest such $m$. If $z\notin\mathbb Z$, the $2(M+1)$
functions $1_{\pm\sigma>0}|\sigma|^z(\log|\sigma|)^m$, $m\le M$, and $s^\pm_{z,m}$, $m\le M$, span the same space: the
change of basis is block triangular in $m$ with diagonal blocks $\binom{1\ \ 1}{e^{i\pi z}\ e^{-i\pi z}}$, invertible as
$e^{2i\pi z}\ne1$. If $z\in\mathbb N_0$, $s^+_{z,0} = s^-_{z,0}$ and the space spanned by the
$1_{\pm\sigma>0}\sigma^z(\log|\sigma|)^m$, $m\le M$, is spanned by $\sigma^z$, the $s^\pm_{z,m}$ with $1\le m\le M$, and
$s^+_{z,M+1}-s^-_{z,M+1}$, which on $\sigma<0$ is $2\pi i(M+1)\sigma^z(\log|\sigma|)^M$ plus lower powers and vanishes
on $\sigma>0$; its coefficient in the expansion of $v$ is $((-1)^za^-_{z,M}-a^+_{z,M})/(2\pi i(M+1))$, the data on
$\sigma<0$ being $a^-_{z,M}|\sigma|^z = (-1)^za^-_{z,M}\sigma^z$. So
$$v = \chi\sum_z\Big(\sum_mB^+_{z,m}s^+_{z,m}+\sum_mB^-_{z,m}s^-_{z,m}\Big)+\chi\sum_\pm1_\pm r^\pm,$$
with $B^-_{z,M+1} = -B^+_{z,M+1} = (a^+_{z,M}-(-1)^za^-_{z,M})/(2\pi i(M+1))$ for $z\in\mathbb N_0$, the polynomial
$\sigma^z$ counted with $s^+$. As $t\to-\infty$ only the $s^-$-terms and $r^\pm$ contribute beyond $O(|t|^{-\infty})$:
$$w(t) = \sum_{z,m}B^-_{z,m}\partial^m_z\big(\bar c(\bar z)|t|^{-z-1}\big)+O(|t|^{-\beta-1+\delta}) =
O(|t|^{-\beta-1}).$$
The functions $|t|^{-z-1}(\log|t|)^j$, finitely many and distinct with $\mathrm{Re}\,z<\beta$, are independent modulo
$O(|t|^{-\beta-1+\delta})$ for $\delta$ small, and for each $z$ the top log powers computed above are strictly
increasing in $m$ (for $z\in\mathbb N_0$ from $m = 1$ on); so by descending induction on $m$ every $B^-_{z,m}$ with
$z\notin\mathbb N_0$, or $z\in\mathbb N_0$ and $m\ge1$, vanishes. For $z\in\mathbb N_0$ this includes $m = M+1$, which
is (a). On $\sigma>0$ the $s^+_{z,m}$ are $\sigma^z(\log\sigma)^m$, so $B^+_{z,m} = a^+_{z,m}$ for $m\ge1$, and for $m =
0$, $z\notin\mathbb N_0$; and (b) follows from the formula for $\mathcal F^{-1}s^+_{z,m}$ on $t>0$, $\sigma^z$
($z\in\mathbb N_0$) contributing $O(t^{-\infty})$. $\square$

The point of (b) is that a forward-supported function's tail is read off from the $\sigma>0$ side alone, and that the
log-free integer-degree pieces (jumps, and the $\rho$-dependent parts of the tf-model's solutions, in
III.I$'''''''''''$) do not reach $K^+$.

## 3. The spacetime phase ([Hin26] Theorem 11.59, Part 1, and Steps 2.A.1-2.A.2 and 4.1, at n = 4)

Let $\mathcal N_\iota := \{\nu\in\mathcal N:\lambda_\nu\in\pi_1\mathcal M\}$, the rows with $\mathrm{Re}\,\lambda<2$
(the s1 rows among them are III.I$''''''''$'s motions), and $\mathcal N_\sigma := \mathcal N\setminus\mathcal N_\iota$,
the rows with $2\le\mathrm{Re}\,\lambda\le3$: by section 1 these are the s1 rows with $(\lambda,k)\in\mathcal
E_{\mathrm{par}}$, $2\le\mathrm{Re}\,\lambda\le3$, the s0 and s2 rows with $\mathrm{Re}\,\lambda = 2$, and the v1 rows
with $\mathrm{Re}\,\lambda = 2$, which carry no parameter (by (G), a c-row with $\mathrm{Re}\,\lambda\ge2$ has rate
$\ge2+d_\tau>2+\epsilon_K$).

**Proposition 3.1 (the spacetime phase).** Let $\alpha\in(2,4+\epsilon_K]$ be admissible and $f = f_1+f_2$ with
$f_j\in\mathcal Y^0_j(\alpha)$, real, vanishing for $t_*<1$. There are real $u_I$, $u_\iota$, vanishing for $t_*<1$, and
$S_\nu\in\mathcal W_{\tau,\mathbb C}$, $\nu\in\mathcal N_\iota$, conjugation-symmetric, all linear and continuous in
$f$, such that:

(a) $u_I\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_I,3+\epsilon_+-\epsilon),\infty}_{\mathrm
b}(\Omega_*)^{\bullet,-}$ vanishes on $\{\rho_I>\frac12c_I\}$, so near $K^+$;

(b) $u_\iota-\sum_{\nu\in\mathcal N_\iota}m_\nu(S_\nu)\in\bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\lambda_\sharp-\epsilon,\alpha-2-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}$;

(c) $f^\flat := f-L_{b_0}(u_I+u_\iota)\in\bigcap_{\epsilon>0}H^{\infty,\ell_I+1,(\mathcal
E^\flat+2,w_+-\epsilon),\alpha-\epsilon}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-}$, vanishing for $t_*<1$, where
$\mathcal E^\flat$ is an index set with $\pi_1(\mathcal
E^\flat\cap\{\mathrm{Re}<3+\epsilon_+\})\subset\Lambda\cap\{\mathrm{Re}\ge2\}$ and log order at most $K(\lambda)$ at
$\lambda$, and $\mathcal E_I$ in (a) is one with $\pi_1(\mathcal E_I\cap\{\mathrm{Re}<3+\epsilon_+\})\subset\Lambda$.

For $\alpha<3$ this is III.I$''''''''$ Lemma 3.2's Steps 1-2 (with the $\iota^+$-expansion recorded to the weight
$w_+$); the new point is $\alpha\le4+\epsilon_K$.

*Proof.* The construction is III.I$'''''$'s Steps 1-2 ((2.3)-(2.5) there), as III.I$''''''''$ Lemmas 3.1-3.2 use it,
with three changes: the $\mathscr I^+$-step goes to $\breve\ell_+ := w_+-2-\epsilon = 3+\epsilon_+-\epsilon$; the
$K^+$-order of the $\iota^+$-steps is $c_K := \alpha$; and the identification of the $K^+$-terms below $\alpha-2$
includes all of $\mathcal T$.

*Step 1 ($\mathscr I^+$; the source's Step 2.A.1).* III.I$'$ Proposition 3.1 with $\breve{\mathcal E}_+ := (\mathcal
E^0_{\mathrm{src}})_{\ge2}$ (the $u$-exponents of $f_1$'s $\iota^+$-index set) and $\breve\ell_+ :=
3+\epsilon_+-\epsilon$ ($<\ell_I$ by (H4), off its exclusions for all but finitely many $\epsilon$) gives $u^{(0)}_I$,
vanishing on $\{t_*<1\}\cup\{\rho_I>\frac12c_I\}$, with $\mathscr I^+$-data $(\langle\mathcal E^C_I\rangle,\ell_I)$,
$\iota^+$-data $(\mathcal E^\sharp_+,\breve\ell_+)$ for this $\breve{\mathcal E}_+$, and $f_1-L_{b_0}u^{(0)}_I\in
H^{\infty,\ell_I+1,(\mathcal E^\sharp_++2,w_+-\epsilon)}_{\mathrm b}$; near $K^+$ it is $f_1$, of $K^+$-weight $\alpha$.
$f_2$ is supported in $\mathrm{supp}\,\chi^\sharp_K$, away from $\mathscr I^+$, with $\iota^+$-index set $\mathcal
E^0_{\mathrm{src}}+2$. So $f^{(0)} := f-L_{b_0}u^{(0)}_I$ has plain $\mathscr I^+$-weight $\ell_I+1$, $\iota^+$-index
set below $w_+-\epsilon$ with $u$-exponents in $\pi_1(\mathcal E^\sharp_+\cup\mathcal E^0_{\mathrm{src}})\subset\Lambda$
(III.I$'$ (3.2): $\pi_1\mathcal E^\sharp_+\subset\pi_1\breve{\mathcal E}_+\cup\{\lambda_\sharp\}\cup\pi_1\mathcal
E^C_I$; $\pi_1\mathcal E^0_{\mathrm{src}}\cap\{\mathrm{Re}\le3+\epsilon_+\}\subset\pi_1(\mathcal G\cup\mathcal M)$ by
Lemma 1.2 (b)'s proof), and $K^+$-weight $\alpha-\epsilon$.

*Step 2 ($\iota^+$, the $u$-exponents below 2; the source's Steps 2.A.2 and 4.1).* III.I$'''''$ Step 2 with $c_K :=
\alpha$, applied to the terms of $f^{(0)}$ of $u$-exponent $\lambda_0$, $\mathrm{Re}\,\lambda_0<2$, in increasing order
of real part, window by window. For each such $\lambda_0$, $\ell_K(\lambda_0) :=
\alpha-\mathrm{Re}\,\lambda_0\in(\alpha-2,\alpha-\lambda_\sharp]$; as $\alpha\le4+\epsilon_K<3+\lambda_\sharp$
($\epsilon_K<\delta_\sharp+\frac12$), $\ell_K(\lambda_0)<3 = \ell^{\max}_K$ by (C5), and $\ell_K(\lambda_0)>\alpha-2>0$;
it avoids the roots and $\mathrm{Re}\,\pi_1\mathcal E_K$ by admissibility. The other hypotheses of III.G$''$ Corollary
4.3 hold as there: $\mathrm{Re}\,\lambda_0\ge\lambda_\sharp>1$; $l_0 = 0$ ($\mathrm{spec}_{\iota^+}(\bar
L)\subset\{\mathrm{Re}\ge2\}$, III.G$'$ Lemma 4.2 (a)); $\ell_I<\frac32+s_C$, $\ell_I\notin\mathrm{Re}\,\pi_1\mathcal
E^{\mathrm{tot}}_{\iota^+,\mathscr I}$, $\mathrm{Re}\,\lambda_0<2<\ell_I$; and the coefficients at $\lambda_0$ have
$R$-weight $\ge\alpha-\epsilon-\mathrm{Re}\,\lambda_0-2 = \ell_K(\lambda_0)-2-\epsilon$, the current source having
$K^+$-weight $\alpha-\epsilon$ (each error of Corollary 4.3 has $K^+$-weight
$\mathrm{Re}\,\lambda_0+\ell_K(\lambda_0)-\epsilon = \alpha-\epsilon$, (4.5) there, and the $\mathscr I^+$-solutions
vanish near $K^+$). Corollary 4.3 gives $u_{\lambda_0} = \sum_{j\le k}\chi_Ku^{(j)}_{b_0,0}+\chi_\iota
t_*^{-\lambda_0}(\log t_*)^j\tilde u^{(j)}$, of $K^+$-index set $\mathcal E^{\mathrm{gr}}_K(\lambda_0)+(0,k)$ at weight
$\ell_K(\lambda_0)-\epsilon>\alpha-2$; and the error's $\mathscr I^+$-expansion is removed by III.I$'$ Proposition 3.1
as in III.I$'''''$ Step 2, whose solution $u'_{\lambda_0}$ vanishes near $K^+$ and whose new $\iota^+$-exponents lie in
$\lambda_0+\mathcal E^\iota_{\mathrm{ind}}+(0,k)$ or have real part $\ge\frac52$ (there: no $\rho_I^{z+1}$-term with
$\mathrm{Re}\,z<\frac52$). Every exponent created lies in $\Lambda$ with log order $\le K$ (Lemma 1.2 (c)), and the
exponents below 2 lie in $\pi_1\mathcal M$ with the log orders of $\mathcal E_{++}$ (III.I$''''''''$ (1.1), as in
III.I$''''''''$ Lemma 3.1). After finitely many windows no term of $u$-exponent below 2 is left. Put $u_I :=
u^{(0)}_I+\sum u'_{\lambda_0}$, $u_\iota := \sum u_{\lambda_0}$; then (a) and (c) hold, (c) with $\mathcal E^\flat$ the
remaining $u$-exponents ($\ge2$), and $u_I$ having $\iota^+$-exponents in $\Lambda$.

*The rows.* By Lemma 2.1 (c) with the $(\log t_*)^j$-versions, each $\chi_Ku^{(j)}_{b_0,0}$ equals
$\sum_{\tau\in\mathcal T\setminus\{\mathrm v1\}}m_{(\tau,\lambda_0,j)}(W^{(j)}_\tau)$ up to $K^+$-weight
$\mathrm{Re}\,\lambda_0+1-\epsilon>\alpha-2-\epsilon$ ($\lambda_\sharp+1>\frac52>2+\epsilon_K$). The rows
$(\tau,\lambda_0,j)$ so produced have $(\lambda_0,j)\in\mathcal M$; those of rate $\le2$ are in $\mathcal N_\iota$, and
by (G) the others (c0 and c1 with $\mathrm{Re}\,\lambda_0+d_\tau>2$) have rate $>2+\epsilon_K\ge\alpha-2$, so
$m_{(\tau,\lambda_0,j)}$ has $K^+$-weight $\ge\alpha-2-\epsilon$ (III.I$'''''''''$ Lemma 2.2 (e)) and joins the
remainder. The rest of $u_{\lambda_0}$ has $K^+$-weight $\ell_K(\lambda_0)-\epsilon>\alpha-2$. Summing, with $S_\nu$ the
sum of the $W^{(j)}_\tau$ for $\nu = (\tau,\lambda_0,j)$, gives (b); the $\iota^+$-weight $\lambda_\sharp-\epsilon$
holds for $u_\iota$ and, by III.I$'''''''''$ Lemma 2.2 (b), for each $m_\nu$. *Reality and linearity.* Every map used is
linear and continuous; $f$ and $L_{b_0}$ are real, and conjugation maps the construction for $\lambda_0$ to that for
$\bar\lambda_0$, so $u_I$, $u_\iota$ are real (or replace them by their real parts, which satisfy (a)-(c) with the real
parts of the identities) and the $S_\nu$ conjugation-symmetric ($m_{\bar\nu}(\bar W) = \overline{m_\nu(W)}$). $\square$

So for $f\in\mathcal Y^0(\alpha)$ the forward solution $u$ of $L_{b_0}u = f$ is $u = \sum_{\nu\in\mathcal
N_\iota}m_\nu(S_\nu)+u_{\mathrm{rem}}+v$, with $u_{\mathrm{rem}}$ of $K^+$-weight $\alpha-2-\epsilon$ and $v$ the
forward solution of $L_{b_0}v = f^\flat$, a source partially polyhomogeneous at $\iota^+$ from the order 4 on, with
plain $\mathscr I^+$-weight $\ell_I+1$. III.I$'''''''''''$ expands $v$ at $K^+$: its terms of rate below $\alpha-2$ are
the rows of $\mathcal N_\sigma$.

## 4. Findings, labels and sources

(II$''''''''''$1) *The spacetime window.* With (C5), III.G$''$ Corollary 4.3 at $c_K = \alpha$ treats every
$\iota^+$-term of $u$-exponent below 2 for all $\alpha\le4+\epsilon_K$ ($\ell_K = \alpha-\mathrm{Re}\,\lambda_0<3$);
without (C5), $\ell^{\max}_K = 2+2\gamma_Cv_C$ could fall below $\alpha-\lambda_\sharp\approx\frac52$. The terms of
$u$-exponent $\ge2$ are left to the spectral side, as in the source; there III.I$'$'s re-solves at $\mathscr I^+$ create
$\iota^+$-exponents of $\mathcal E^C_I$ with real part $\ge\frac52$ that a spacetime treatment would have to revisit.

(II$''''''''''$2) *The parameter exponents* (the source's $\tilde{\mathcal E}'_{++}$, Definition 11.56 and (11.186)) are
fixed in Definition 1.1 before the construction. They do not depend on $\mathcal E_+$ (Lemma 1.2 (b)): every exponent
that involves $\mathcal E_+$ beyond $\mathcal E_{++}$ has real part $\ge2\lambda_\sharp>3+\epsilon_+$, and $L_0$ bounds
log orders only below $2\lambda_\sharp$ (bounding them up to the real part 5, as first written, made $L_0\ge K(2)>L_0$
under (H3); verifier 116). So (H3) is consistent: the content of the source's Remark 11.62 at $n = 4$. Their log orders
grow with the real part ($K(\lambda) = L_0+L_1(n(\lambda)+1)$, $L_1 := (N_*+1)(l_*+1)$), which makes the count of Lemma
1.2 (c) close.

(II$''''''''''$3) *The rows' sources are not constructed through.* $f^\nu_{h,\vec p} = L_{h,\vec p}m_\nu+r^\nu_{h,\vec
p}$ exactly, with $r^\nu$ of no index set, so the sources that pass through Proposition 3.1 and III.I$'''''''''''$ are
those of $\mathcal Y^0(\alpha)$ (1.1); otherwise a row's own exponent would come back with a raised log order (III.G$''$
Corollary 4.3's $l_0$, III.G$''''$ Proposition 4.4 at $\alpha_0 = 2$) outside $\mathcal E_{\mathrm{par}}$.

(II$''''''''''$4) *(H4).* The $\mathscr I^+$-step must reach the $\iota^+$-weight $w_+-2 = 3+\epsilon_+$ (Step 1), and
the Fourier transform of $f^\flat$ in III.I$'''''''''''$ needs III.A Proposition 4.2's (4.2), $\ell_I+1>w_+-1$; both are
$\ell_I>3+\epsilon_+$, and with $\ell_I\le a_I$ this asks $a_I>3+\epsilon_+$. The source's class has $\mathscr
I^+$-order $3+\epsilon_I$ for $h$.

(II$''''''''''$5) *The gap (G).* At $n = 4$ the row rates $\lambda-1$, $\lambda$, $\lambda+d_\tau$ are spread over
$\Lambda$; $\epsilon_K$ must avoid them so that the remainder order $2+\epsilon_K$ is reached with the rows of $\mathcal
N$ alone (rate $\le2$). The source's $\epsilon_K<\epsilon_{\mathrm{ind}}$ does this at $n = 3$, where the rates near 2
are integers plus elements of $\mathcal E_{\mathrm{ind}}$.

(II$''''''''''$6) *Joint injectivity* (Lemma 2.2, Corollary 2.3) replaces the source's statement in Step 2.B that the
coefficients are a perturbation of $\pm$ the identity: rows of different types at one rate are told apart by the degree
of their spherical type and, within a degree, by the order of their states at $\partial X$.

*Labels.* Lemma 1.2, Definition 1.3, Lemmas 2.1-2.2, Corollary 2.3 and Lemma 2.4 are new at $n = 4$ (Lemma 2.4 is
classical); Proposition 3.1 is the source's Part 1, Step 2.A.1 and the spacetime half of Steps 2.A.2 and 4.1, at $n = 4$.

*Sources.* [Hin26] pp. 278-289 (Theorem 11.59, Remarks 11.60-11.62, the proof's Parts 1-3), read at source. Inputs: II.E
Proposition 3.4; III.A Proposition 4.2, Lemma 1.4; III.A$'$ Lemma 1.6; III.D$''$ Proposition 3.1; III.D$'''$ Proposition
3.1; III.F$'''$ Proposition 4.1; III.G$'$ Lemmas 1.3, 4.2; III.G$''$ (1.1), Table 1.1, Lemma 2.1, Definition 2.5,
(4.2)-(4.4), Theorem 4.2, Corollary 4.3; III.G$''''$ Propositions 4.4, 5.1; III.I section 3; III.I$'$ Proposition 3.1;
III.I$''''$ (1.2); III.I$'''''$ Steps 1-2; III.I$'''''''$ Lemma 3.1; III.I$''''''''$ (1.1), Lemmas 3.1-3.2;
III.I$'''''''''$ sections 1-2.
