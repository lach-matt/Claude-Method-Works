# Part III.J$'$. Efficient parameterisation II: linear forward solutions, n = 4 ([Hin26] Theorem 12.8)

*Status.* Written (D283); verified (D285: verifier 122's findings seated); proved (D287: verifier 123 read the D285
repairs, seven nits seated). This part proves, at spatial dimension $n = 4$ and at the black hole parameter $b_0$,
[Hin26] Theorem 12.8 and Remark 12.9 (pp. 312-318): every solution of the linearised equation that III.I$''''''''''''''$
Theorem 3.1 produces, for a source of the class $\mathcal F$ of III.J, is $D_U\Phi(U')$ for data $U'$, so that the map
$\Phi$ of III.J describes the linear forward solutions exactly (Theorem 2.1). The tame form of the estimates (the
source's $\|U'\|_k\le C_k(\|f\|_{k+d}+\|U\|_{k+d}\|f\|_d)$) and the parameters $b\ne b_0$ were recorded as open
((J$'$2)-(J$'$3)); III.J$''$ and III.I$'''''''''''''''$ Corollary 3.2 have since closed them (D330, verifier 148's n5).

*What n = 4 changes.* (1) *The $\iota^+$-order of the linear solutions.* III.I$'''''''''''$-III.I$''''''''''''''$ give
the solutions the $\iota^+$-order $(3+\eta_2)-$ with $\eta_2<\epsilon_+$, while $\Phi$ and $\mathcal F$ use
$(3+\epsilon_+)-$ and $(5+\epsilon_+)-$ (III.J (J5) (a)). Under III.J's (G$^+$) no exponent lies between, the
construction does not depend on $\eta_2$ in that window, and the order is $(3+\epsilon_+)-$ (Lemma 1.1). (2) *No step at
$t_*^{-1}$.* The source's Step 1 (the $t_*^{-3}$-terms) becomes, at $n = 4$, the removal of the parameters $\vec
p\,'_{\le0}$ first, and every exponent is then treated by the source's Step 2. (3) *Linearity.* As in III.J, the
equation at each $u$-exponent below $3+\epsilon_+$ involves only the $t_*^{-\lambda_0}$-terms at that exponent.
Notation: Parts III.G$'''$, III.I$'''''''''''$-III.I$''''''''''''''$, III.J; no instrument is used.

## 1. Setting and the $\iota^+$-order

Everything of III.J is kept: $\alpha$ with (A$_J$), (G$^+$), the classes $\mathcal X_J$, $\mathcal F$, $\mathcal Q_J$,
the data space $\mathcal D$ with $\Sigma$ and $\mathcal R'_0$, $\Lambda_* = \Lambda\cap\{\mathrm{Re}<3+\epsilon_+\}$,
the $t_*^{-\lambda}$-terms $[\cdot]_\lambda$ and the map $\Phi$ of Theorem 2.4 there. $\Lambda_* = \pi_1\mathcal
E_\sharp\cap\{\mathrm{Re}<3+\epsilon_+\}$ (III.I$''''''''''$ Lemma 1.2 (a), III.I$''''''''''''$ section 1). The
parameters are at $b = b_0$ unless said otherwise ($\vec p\,'$ may still have a component $b'$, the direction of the
derivative).

**Lemma 1.1 (the $\iota^+$-order under (G$^+$)).** Under (G$^+$), III.I$'''''''''''$ Proposition 3.1,
III.I$''''''''''''$ Theorem 3.1 and III.I$''''''''''''''$ Theorem 3.1 hold with $\eta_2$ replaced by $\epsilon_+$ in
their $\iota^+$-orders: in III.I$''''''''''''$ (3.2)-(3.3), $w_\rho = (3+\epsilon_+-d_\rho)-$ and $\tilde u$ has the
$\iota^+$-data $(\mathcal E_\sharp,(3+\epsilon_+)-)$; in III.I$''''''''''''''$ (3.2), $h'$ has the $\iota^+$-data
$(\mathcal E_\sharp,(3+\epsilon_+)-)$, and $q'\in\mathcal Q^\infty_J$.

*Proof.* In III.I$'''''''''''$ Proposition 3.1, $\eta_2$ enters as the threshold of level 2 (Step 3: the tf-exponents
$\alpha_0$ of $g_2$ with $\mathrm{Re}\,\alpha_0<2+\eta_2$ are treated), as the order $\mu_2 = 2+\eta_2$ of the
zero-energy solve there (III.I$'''''''''''$ Lemma 2.1 with $\mu' = 2+\epsilon_+-\epsilon$), and through the resulting
tf-weight $\tau_3 = 1+\eta_2-2\epsilon$ of $g_3$, a lower bound; with the conditions $\eta_2\in(\epsilon_K,\epsilon_+)$,
$\eta_2>\eta_1$, no $\lambda\in\Lambda$ of real part $3+\eta_2$, and $2\epsilon<\epsilon_+-\eta_2$. The tf-exponents of
the level-2 sources (of $g_2$ and of the remainders $\alpha_0+\mathcal E_{\mathrm{ind}}$ of the rounds) are
$u$-exponents minus 1, so they lie in $\Lambda-1$ (at level 2 the tf-exponent $\alpha_0$ is the $u$-exponent
$\alpha_0+1$, III.I$'''''''''''$ section 3; III.I$''''''''''$ Lemma 1.2 (c)); by (G$^+$) none has real part in
$(2,2+\epsilon_+]$. So for every $\eta_2$ in $(\eta^0_2,\epsilon_+)$, $\eta^0_2$ the value fixed in III.I$''''''''''''$
section 1, level 2 treats the same exponents. Lemma 2.1 there applies $\tilde L_{b_0}(0)^{-1}$ at the weight $\mu_2-4$,
and moving $\mu_2$ within $(2+\eta^0_2,2+\epsilon_+)$ crosses neither an exponent of its source (those exceed
$2+\epsilon_+$, again by (G$^+$), as its last sentence records them $\Lambda$-valued) nor an indicial root (none has
real part in $(0,1)$, III.F$'$ Proposition 2.3); so its output is the same (III.H Proposition 3.2's inverses on two such
weights agree). Hence $g_3$ is one tensor for all these $\eta_2$, and has the tf-weight $1+\eta_2-2\epsilon$ for each of
them with $2\epsilon<\epsilon_+-\eta_2$: given $\epsilon$, take $\eta_2 := \epsilon_+-3\epsilon$, so $g_3$ has the
tf-weight $\tau_3 := 1+\epsilon_+-5\epsilon$. Step 4 (level 3) and everything after it in
III.I$'''''''''''$-III.I$''''''''''''''$ use $\tau_3$ only as a lower bound on $g_3$'s tf-weight, through:
$\alpha_\tau\ge\tau_3>1+\ell_3$ (true, $\epsilon_+>\epsilon_K>\ell_3$); the zf-weight $\alpha_\tau\ge\tau_3$ of the
level-3 pieces, so their $K^+$-weight $\ge2+\epsilon_+-5\epsilon>\alpha-2$; their $\iota^+$-order
$\alpha_\tau+2\ge3+\epsilon_+-5\epsilon$ (III.I$''''''''''''$ Step 2, (viii)); and $w_\rho$, chosen in
III.I$''''''''''''$ as the $\iota^+$-order of the level-3 pieces minus $d_\rho$. With $\tau_3 = 1+\epsilon_+-5\epsilon$
these give the $\iota^+$-order $3+\epsilon_+-5\epsilon$ and $w_\rho = 3+\epsilon_+-5\epsilon-d_\rho$, for every small
$\epsilon$; the polyhomogeneous parts are unchanged below $3+\epsilon_+$, there being no exponent in
$[3+\eta^0_2,3+\epsilon_+]$. The $\epsilon$-independence of the decomposition is III.I$''''''''''''''$ Lemma 2.5, whose
level-3 parameters now are $\tau_i(\epsilon) = 1+\epsilon_++i\epsilon_{\mathrm{ind}}-(5+i)\epsilon$, stable in the same
way. III.I$''''''''''''''$ Theorem 3.1 takes its $\iota^+$-orders from III.I$''''''''''''$ Theorem 3.1 (its Step 4), and
its intermediate levels do not enter $h'$, $q'$. So $h'$ has $(\mathcal E_\sharp,(3+\epsilon_+)-)$ at $\iota^+$, and
$q'\in\mathcal Q^\infty_J$: its polyhomogeneous parts are those of III.I$''''''''''''''$ Definition 1.1 (exponents below
$3+\epsilon_+-d_\rho$), its conormal parts $\dot S_{\mathrm{rem}}$, $\dot b_{\mathrm{rem}}$ and $Y^c_\rho$
($\rho\in\mathcal R'_0$ only, III.I$''''''''''''$ Step 4) have the orders $(\alpha-2)-$, $(\alpha-1)-$,
$(3+\epsilon_+-d_\rho)-$. $\square$

## 2. Linear forward solutions

**Theorem 2.1 ([Hin26] Theorem 12.8 at n = 4, at $b_0$).** There is $d$ such that for $U\in\mathcal D^\infty$ with $b =
b_0$, small in $\mathcal D^d$, and $(h,\vec p,q) := \Phi(U)$, the following holds. For every $f\in\mathcal F^\infty$
there is $U'\in\mathcal D^\infty$ with
$$D_{(h,\vec p,q)}P_5\big(D_U\Phi(U')\big) = f.\tag{2.1}$$
$U'$ is linear in $f$, and for every $k$ there are $d_k$ and $C_k$ with $\|U'\|_{\mathcal D^k}\le C_k\|f\|_{\mathcal
F^{k+d_k}}$ for $U$ small in $\mathcal D^{d_k}$.

*Proof.* *Step 0 (the solution of III.I$''''''''''''''$).* $(h,\vec p,q) = \Phi(U)$ is admissible in
III.I$''''''''''''''$ Theorem 3.1: $h\in\mathcal X^\infty_J$ is in the class $\mathcal X$ of III.I$''''''''''''''$
section 1 with (H2) read as "$\alpha-$" (III.I$''''''''''''''$ Remark 3.2 (2)) and $a_+$ any value below $3+\epsilon_+$
((H5) for $\eta_2$ close to $\epsilon_+$, Lemma 1.1); $\vec p\in\mathcal P$ at $b_0$; $q\in\mathcal
Q^\infty_J\subset\mathcal Q$; all small with $U$. And $f\in\mathcal F^\infty\subset\mathcal Y^0(\alpha-)$: $\mathcal F$
has the $\mathscr I^+$-data of $\mathcal Y^0_1$, a plain $\iota^+$-weight $(5+\epsilon_+)-$, which $\mathcal Y^0_1$'s
$(\mathcal E^0_{\mathrm{src}}+2,w_+-\epsilon)$ contains, and the $K^+$-order $\alpha-$. III.I$''''''''''''''$ Theorem
3.1 with Lemma 1.1 gives $\vec p\,'\in\mathcal P$, $q'\in\mathcal Q^\infty_J$ and $h'$ with the $\iota^+$-data
$(\mathcal E_\sharp,(3+\epsilon_+)-)$, the $\mathscr I^+$-data $(\langle\mathcal E^C_I\rangle,\ell_I)$ and the
$K^+$-order $\alpha-$, such that
$$D_{(h,\vec p,q)}P_5(h',\vec p\,',q') = f.\tag{2.2}$$
We now subtract from $(h',\vec p\,',q')$ values of $D_U\Phi$, each time keeping (2.2) with a new $f$ in $\mathcal
F^\infty$ (III.J Remark 2.5), until nothing is left but conormal remainders.

*Step 1 (the parameters $\vec p\,'_{\le0}$).* Let $U'_0 := \vec p\,'_{\le0} = (S',b',S^{(0)\prime}_1)$ and replace
$(h',\vec p\,',q')$ by $(h',\vec p\,',q')-D_U\Phi(U'_0\oplus0)$. By III.J Theorem 2.4 (1), linearised, the new $\vec
p\,'_{\le0}$ vanishes. This is the source's Step 1, which at $n = 4$ has no $t_*^{-1}$-term to treat: the parameters
$\vec p_{\le0}$ enter at the $u$-exponents of $\mathcal G\subset\{\mathrm{Re}\ge2\}$ (III.J Lemma 2.1).

*Step 2 (the exponents of $\Lambda_*$).* Suppose $\vec p\,'_{\le0} = 0$ and that for every $\lambda\in\Lambda_*$ with
$\mathrm{Re}\,\lambda<\mathrm{Re}\,\lambda_0$ the term $[h']_\lambda$, the rows $W'_\nu$ with $\nu = (\tau,\lambda,k)$
or $(\mathrm{rot},\lambda,k)$, and the polyhomogeneous coefficients of $q'$ at the exponents $(\lambda-d_\rho,k)$
vanish. Put
$$G'(\lambda_0) := \Big[h'+\sum_{\nu\in\mathcal N\sqcup\mathcal
N_{\mathrm{rot}}}m_\nu(W'_\nu)+h_{b_0,\mathrm{rem}}(q')\Big]_{\lambda_0}.$$
Differentiating III.J Lemma 2.1 at $(h,\vec p,q)$ in the direction $(h',\vec p\,',q')$: the quadratic part contributes
at $u$-exponents $\ge2\lambda_\sharp>3+\epsilon_+$, the dependence of $F_0$ and of $L_{0,\vec p_{\le0}}$ on $\vec
p_{\le0}$ drops out as $\vec p\,'_{\le0} = 0$, and the terms below $\lambda_0$ vanish; so
$$\big[D_{(h,\vec p,q)}P_5(h',\vec p\,',q')\big]_{\lambda_0+2} = \bar L\,G'(\lambda_0),$$
and as $f$ has no $\iota^+$-term below $(5+\epsilon_+)-$, $\bar LG'(\lambda_0) = 0$. Now $G'(\lambda_0) =
\sum_{j}t_*^{-\lambda_0}(\log t_*)^jg_j$ with $g_j\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal
E_K,\ell_K)}_{\mathrm b}(\iota^+)$, $\ell_K := \ell_K(\lambda_0)-\epsilon$: $[h']_{\lambda_0}$ has these $\mathscr
I^+$-data and, from the $K^+$-order $\alpha-$ of $h'$, the weight $\ell_K$ at $R = 0$; the rows and towers are supported
in $\mathrm{supp}\,\chi_K$, away from $\mathscr I^+$, and at $R = 0$ consist of formal solutions of III.G$''$ (exponents
$-\mu+i\ge0$, in $\mathcal E_K$ below $\ell_K$, III.G$''$ Corollary 3.2) and terms of $K^+$-order
$\ge\mathrm{Re}\,\lambda_0+3$ (III.J Lemma 2.2). So $G'(\lambda_0)\in\mathrm{Res}^\infty_{\iota^+}(\bar L,\mathcal
E^C_I,\lambda_0)$ (III.G$'''$ Definition 3.2).

*Case A: $\lambda_0$ is not a pole of (2.2).* Then $\mathrm{Res}^\infty_{\iota^+}(\bar L,\mathcal E^C_I,\lambda_0) = 0$
(III.G$'''$ Lemma 3.5: its elements are residues of $t_*^{-z}N_{\iota^+}(z)^{-1}f(z)$ with $f$ polynomial), so
$G'(\lambda_0) = 0$. The coefficients of $q'$ have rate $<\alpha$ (III.I$''''''''''''$ Lemma 2.4's proof removes only
the pairs below $\beta = \alpha-\epsilon$; III.I$''''''''''''''$ Step 4), and so do those of $D_U\Phi$ (III.J Step
$\lambda_0$ (iii)), the rows having rate $\le3$ (for s1 the formal solution's order is $\mathrm{Re}\,\lambda_0+1\le4$);
so every row and coefficient at $\lambda_0$ carries a formal solution of $K^+$-order below
$\mathrm{Re}\,\lambda_0+\ell_K(\lambda_0) = \alpha$, visible below $\ell_K$. Then the rows and coefficients at
$\lambda_0$ vanish: the expansion of $G'(\lambda_0)$ at $R = 0$ below $\ell_K$ is the sum of the formal solutions that
the rows and coefficients at $\lambda_0$ carry (III.J Lemma 2.2), as $[h']_{\lambda_0} = O(R^{\ell_K})$; the
coefficients of III.G$''$ Theorem 3.1 are determined by the tensor (III.G$''$ Theorem 3.1, Lemma 1.2: distinct rows have
independent, injective leading terms), and III.J Lemma 2.2 expresses them through the rows and coefficients triangularly
in the log power, with the non-zero factors $c_\tau(\lambda_0)$; so, downward in the log power, every row and
coefficient at $\lambda_0$ is 0. Then $[h']_{\lambda_0} = G'(\lambda_0) = 0$.

*Case B: $\lambda_0$ is a pole of (2.2).* Then $\lambda_0\in\mathrm{spec}^{<3+\epsilon_+}_{\iota^+}(\bar L,\mathcal
E^C_I)\cap\Lambda_*\subset\Sigma$. By III.G$'''$ Proposition 3.7 (its right inverse at $k = \infty$), $G'(\lambda_0) =
u^0_{\lambda_0}+\mathrm{res}_{z=\lambda_0}(t_*^{-z}N_{\iota^+}(z)^{-1}f_{\lambda_0}(z))$ for some
$(u^0_{\lambda_0},f_{\lambda_0})$ in the domain of (3.6), linear and continuous in $G'(\lambda_0)$
(conjugation-symmetric, as $G'(\lambda_0)$ and $G'(\bar\lambda_0)$ are conjugate; at real $\lambda_0$, (3.6) being real,
the real part of the right inverse's output is taken). Let $U'_{\lambda_0}\in\mathcal D^\infty$ have these data at
$\lambda_0$ and $\bar\lambda_0$ and all else 0. By III.J Theorem 2.4 (3), linearised, $D_U\Phi(U'_{\lambda_0})$ has no
term, row or coefficient below $\mathrm{Re}\,\lambda_0$, and its total $t_*^{-\lambda_0}$-term is
$u_{\lambda_0}-R'(\lambda_0)+R'(\lambda_0) = G'(\lambda_0)$. Replacing $(h',\vec p\,',q')$ by $(h',\vec
p\,',q')-D_U\Phi(U'_{\lambda_0})$ makes the new $G'(\lambda_0)$ zero and leaves the lower terms zero; Case A's argument
then makes every term, row and coefficient at $\lambda_0$ vanish.

Exponents of equal real part are treated together, independently. After the finitely many exponents of $\Lambda_*$:
$\vec p\,' = 0$ (every row $(\tau,\lambda,k)$ or $(\mathrm{rot},\lambda,k)$ of $\mathcal N\sqcup\mathcal
N_{\mathrm{rot}}$ has $\lambda\in\Lambda_*$, as $\mathrm{Re}\,\lambda\le3$; $\vec p\,'_{\le0} = 0$ by Step 1); $q'$ has
no polyhomogeneous part (each has $\iota^+$-exponent $z+d_\rho\in\Lambda_*$, III.I$''''''''''''''$ Definition 1.1 and
Lemma 1.1); and $h'$ has no $\iota^+$-term below $3+\epsilon_+$, so $h'\in H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),(3+\epsilon_+)-,\alpha-}_{\mathrm b}(\Omega_*)^{\bullet,-}$, the class of $\tilde h$ in III.J
Definition 1.1.

*Step 3 (conclusion).* Now $q' = (S'_{\mathrm{rem}},b'_{\mathrm{rem}},(Y'^c_\rho)_{\rho\in\mathcal R'_0})$ with the
orders of III.J Definition 1.1 (Lemma 1.1), and $(h',0,q') = D_U\Phi(U'_{\mathrm c})$ with $U'_{\mathrm c} :=
(0,0,0,(0,0),S'_{\mathrm{rem}},b'_{\mathrm{rem}},(Y'^c_\rho),h')$: these components enter $\Phi$ additively (III.J
Theorem 2.4 (2)) and contribute to no $t_*^{-\lambda_0}$-term with $\lambda_0\in\Lambda_*$ (their $\iota^+$-orders are
$(3+\epsilon_+)-$ and $(\alpha+1)-$), so they enter no step of the construction. Summing, $U' :=
U'_0\oplus\sum_{\lambda_0}U'_{\lambda_0}+U'_{\mathrm c}$ satisfies $(h',\vec p\,',q')_{\text{Step 0}} = D_U\Phi(U')$,
and (2.2) is (2.1). *Linearity and bounds.* III.I$''''''''''''''$ Theorem 3.1's solution is linear in $f$ with bounds
uniform for $(h,\vec p,q)$ small; each subtraction is $D_U\Phi$ (bounded, III.J Theorem 2.4) of data that are continuous
linear functions of the current $(h',\vec p\,',q')$ (III.G$'''$ Proposition 3.7 with loss $l$; finitely many steps).
$\square$

**Remark 2.2 (non-uniqueness; the source's Remark 12.9).** Neither $D_{(h,\vec p,q)}P_5$ nor $D_U\Phi$ is injective: a
part of $b'_{\mathrm{rem}}$ of order $\alpha$ can be moved into $h'$, and the conormal parts of the data overlap with
$\tilde h$ in the same way. Theorem 2.1 asserts that the particular solution of III.I$''''''''''''''$ Theorem 3.1 is of
the form $D_U\Phi(U')$, with $U'$ obtained constructively from it, so $U'$ inherits its bounds.

## 3. Findings, labels and sources

(J$'$1) *The $\iota^+$-order.* III.I$'''''''''''$ fixed $\eta_2<\epsilon_+$ so that level 2 treats only exponents below
the source's expansion limit; under (G$^+$), which empties $(3,3+\epsilon_+]$ of $\Lambda$, the threshold can approach
$\epsilon_+$ without changing the construction, and the linear solutions have the $\iota^+$-order $(3+\epsilon_+)-$ of
the nonlinear class (Lemma 1.1). Without this the scheme would lose $\epsilon_+-\eta_2$ at $\iota^+$ at every step.

(J$'$2) *Tame estimates.* The source states $\|U'\|_k\le C_k(\|f\|_{k+d}+\|U\|_{k+d}\|f\|_d)$, taking them from its
Corollary 11.66 (its Remark 11.13). At $n = 4$, III.I$''''''''$-III.I$''''''''''''''$ state their bounds as uniform for
the background small, and the tame form, with the background's high norms entering linearly, is not yet proved for them;
Theorem 2.1 records the non-tame bound, and the tame form is an obligation for the part that writes [Hin26] section 13
(II.G$'$ Nash-Moser needs it). The construction of $U'$ from $(h',\vec p\,',q')$ (Steps 1-3) is linear with fixed losses
and coefficients depending on $U$ only through finitely many derivatives at the exponents of $\Lambda_*$, so it is tame
once III.I$''''''''''''''$ Theorem 3.1 is.

(J$'$3) *$b\ne b_0$.* Theorem 2.1 is at $b_0$, as III.I$''''''''$-III.I$''''''''''''''$ are ((I3) of III.I); the
nonlinear iteration moves $b$, and the linear theory at $b$ near $b_0$ is open. D297: III.I$'''''''''''''''$ supplies it
(Corollary 3.2), proved D311; its census is now the base-point ledger (D329-D330, verifier 148's n5).

(J$'$4) *$\Psi$.* The version with an initial solution (the source's Theorem 12.8 for $\Psi$) waits for Part III.C$'$,
as in III.J (J6).

*Labels.* Theorem 2.1 is the source's Theorem 12.8 at $b_0$ without the tame form; Steps 1-2 its Steps 1-2 (Cases A-B),
Step 3 its Step 3; Remark 2.2 its Remark 12.9. Lemma 1.1 is new at $n = 4$.

*Sources.* [Hin26] pp. 312-318 (Theorem 12.8, Remark 12.9 and the proof of Theorem 12.8), read at source. Inputs:
III.F$'$ Proposition 2.3; III.G$''$ Lemma 1.2, Theorem 3.1, Corollary 3.2; III.G$'''$ (2.2), Definition 3.2, Lemma 3.5,
Proposition 3.7; III.H Proposition 3.2; III.I$''''''''''$ Lemma 1.2; III.I$'''''''''''$ Proposition 3.1 with Lemma 2.1;
III.I$''''''''''''$ section 1, Theorem 3.1; III.I$''''''''''''''$ Definitions 1.1-1.3, Lemma 2.5, Theorem 3.1, Remark
3.2; III.J Definition 1.1, Lemmas 2.1-2.2, Theorem 2.4, Remark 2.5.
