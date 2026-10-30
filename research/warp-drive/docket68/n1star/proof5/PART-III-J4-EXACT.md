# Part III.J$'''$. Exact weights, n = 4 ([Hin26] Corollary 11.66 and Theorem 12.8 at fixed weights)

*Status.* Written (D293); verified (D295: verifier 127's findings seated); proved (D296: verifier 128 read the D295
repairs and found them correct; four nits seated). This part proves, at spatial
dimension $n = 4$ and $b = b_0$, that the solution map of III.I$''''''''''''''$ Theorem 3.1 and the right inverse of
III.J$'$ Theorem 2.1 lose nothing in the weights. A source at the fixed weights $(\ell_I+1,5+\epsilon_+,\alpha)$ at
$(\mathscr I^+,\iota^+,K^+)$ gives a solution at $(\ell_I,3+\epsilon_+,\alpha)$, with one fixed admissible $\alpha$.
This is how the source states its Corollary 11.66 (pp. 294-295) and Theorem 12.8 (p. 312), at
$(4+\epsilon_I,5+\epsilon_+,4+\epsilon_K)$ and $(3+\epsilon_I,3+\epsilon_+,4+\epsilon_K)$. With III.J$''$ this gives the
tame estimates on one pair of Banach scales (Corollary 6.6), and so discharges (J$''$4) of III.J$''$ at $b_0$. The
linear theory at $b\ne b_0$, (J$'$3), stays open.

*What n = 4 changes.* (1) *The losses are removed where they arise; nothing is improved after the fact.* Of the
statements of III.I-III.I$''''''''''''''$ that take a source at an exact weight and conclude an order "$w-$", only those
whose loss reaches a final weight matter: every other one feeds an open condition with fixed room. Those losses have
three roots. (a) At $K^+$, III.G$''$ Corollary 4.3 writes the $\iota^+$-terms in powers of $\log t_*$. At the corner
$t_*^{-1} = \rho_+\rho_K$, so each $\log t_*$ hides a $\log\rho_K$, and a logarithm times a conormal function of exact
weight lies in no weighted $L^2$-b space of that weight. In that convention Corollary 4.3 cannot be applied at the exact
weight, the two classes being incomparable (Remark 3.1). Written in
powers of $\log\rho_+$, the convention of [Hin26] Definition 2.8 in which the classes of the parts are defined, the same
construction is exact (Corollary 3.2). (b) III.I$''''''''''''$ Lemma 2.2 and Lemma 2.1 bound their outputs pointwise, at
$K^+$ and at the corner of $\iota^+$ and $K^+$, which gives only the $L^2$-weight $w-$; at the final weight they are
re-proved in $L^2$ (Lemmas 4.4, 4.5 and 4.7). The
Fourier characterization III.A Proposition 4.2 is itself exact and only transmits the loss of (a) (Proposition 4.1). (c)
At $\iota^+$, the level-2 margin $\eta_2<\epsilon_+$ of III.I$'''''''''''$ and the $5\epsilon$ of III.J$'$ Lemma 1.1 are
choices, not estimate losses: at the closed endpoint of (G$^+$) every map is exact (Proposition 4.3), as the source's
own run at these weights shows (pp. 289-291). At $\mathscr I^+$ every class and every main statement is already exact.
(2) *The $K^+$-weight is one fixed admissible $\alpha$*, not the numeral $4+\epsilon_K$; $\alpha = 4+\epsilon_K$ itself
is admissible off a finite set of $\epsilon_K$ (Definition 1.3, (A$_K$)). (3) *New conditions* (E2)-(E4), each
excluding finitely many values, of the kind of (G$^+$) and of admissibility; (E1) is (G$^+$) at its closed endpoint,
and (E5) is vacuous.

Notation: as in III.I$''''''''''''''$, III.J, III.J$'$ and III.J$''$; $w_+ := 5+\epsilon_+$; $\rho_+$, $\rho_K$ are the
defining functions of $\iota^+$ and $K^+$ near their corner, $\rho_+ = 1/r$, $\rho_K = R = r/t_*$, so $t_*^{-1} =
\rho_+\rho_K$ there (III.I$''$ section 1); $\mu$ runs over the indicial roots of $\widehat{L_{b_0}}(0)$ (III.F$'$
Proposition 2.3), and $-\mu$ is read as $-\mathrm{Re}\,\mu$; the non-real roots have real part below $-101$ or above 1,
outside every interval used. No instrument is used.

## 1. The exact classes and the exactness conditions

Throughout, $b = b_0$, and $\alpha$ is a fixed $K^+$-weight, admissible in the sense of III.I$''''''''''$ Definition
1.3, with $\alpha\in(4+\epsilon_K-\epsilon'_0,4+\epsilon_K]$, satisfying (A$_J$) of III.J and Definition 1.3 below.

**Definition 1.1 (exact classes).** Each class below is the class of the parts named after it with every order "$w-$"
replaced by $w$ and every index set unchanged:

- $\mathcal X^k_{J,\mathrm{ex}} := H^{k,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal
E_+,3+\epsilon_+),\alpha}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-}$ (III.J's $\mathcal X^k_J$);

- $\mathcal F^k_{\mathrm{ex}} := H^{k,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),w_+,\alpha}_{\mathrm
b}(\Omega_*;S^2T^*)^{\bullet,-}$, a plain weight at $\iota^+$ (III.J's $\mathcal F^k$);

- $\mathcal Y^0_{\mathrm{ex}}(\beta)$ and $\mathcal Y^\natural_{\mathrm{ex}}(\beta)$: III.I$''''''''''$'s $\mathcal
Y^0(\beta)$ and III.I$'''''''''''''$'s $\mathcal Y^\natural(\beta)$ with the $\iota^+$-weight $w_+-\epsilon$ replaced by
$w_+$ (their $K^+$-weight $\beta$ is exact already);

- $\mathcal Q_{\mathrm{ex}}$: III.I$''''''''''''''$'s $\mathcal Q$ ((1.1) there) with $S_{\mathrm{rem}}\in\dot
H^{\infty,\alpha-2}_{\mathrm b}$, $b_{\mathrm{rem}}\in\dot H^{\infty,\alpha-1}_{\mathrm b}$ and $Y_\rho\in\dot
H^{\infty,\mathcal Q(\mathcal E^\alpha_\rho,3+\epsilon_+-d_\rho)}_{\mathrm b}$;

- $\mathcal D^k_{\mathrm{ex}}$: III.J Definition 1.1 with $S_{\mathrm{rem}}\in\dot H^{k,\alpha-2}_{\mathrm b}$,
$b_{\mathrm{rem}}\in\dot H^{k,\alpha-1}_{\mathrm b}$, $Y_{\rho,\mathrm{rem}}\in\dot H^{k,3+\epsilon_+-d_\rho}_{\mathrm
b}$ and $\tilde h\in H^{k,(\langle\mathcal E^C_I\rangle,\ell_I),3+\epsilon_+,\alpha}_{\mathrm b}$, normed by its
components' norms at these fixed weights.

These are the source's classes (11.226) (p. 292), (11.227b) (p. 293), (11.233) (p. 294), (12.12c)-(12.12d) (p. 301) and
(12.31) (p. 310), with $(3+\epsilon_I,4+\epsilon_I)$ read as $(\ell_I,\ell_I+1)$ and $4+\epsilon_K$ as $\alpha$. Each
$\mathcal D^k_{\mathrm{ex}}$ and $\mathcal F^k_{\mathrm{ex}}$ is a Banach space.

**Remark 1.2 (inclusions).** Each exact class is continuously embedded in its "$w-$" class: same index sets, a larger
weight. And $\mathcal F_{\mathrm{ex}}\subset\mathcal Y^0_{\mathrm{ex}}(\alpha)$: a plain weight $w_+$ is the class
$(\mathcal E^0_{\mathrm{src}}+2,w_+)$ with vanishing coefficients, as III.J$'$ Theorem 2.1's Step 0 argues for the
"$w-$" classes. So every statement of the parts applies to exact inputs. Only statements whose output must lie in an
exact class are re-proved below.

**Definition 1.3 (the exactness conditions).** Besides admissibility and (A$_J$):

- (E1) (G$^+$) of III.J, used with its closed endpoint: no $\lambda\in\Lambda$ has real part in $(3,3+\epsilon_+]$,
that is, $\epsilon_+<\min\{\mathrm{Re}\,\lambda-3:\lambda\in\Lambda,\ \mathrm{Re}\,\lambda>3\}$, a smallness condition.
With III.I$''''''''''$ Lemma 1.2 (c) (every exponent produced with real part in $[2,3+\epsilon_+]$ lies in $\Lambda$), no
exponent produced has $u$-exponent of real part $3+\epsilon_+$.

- (E2) $3+\epsilon_+\notin\mathrm{Re}\,\pi_1\mathcal E^{\mathrm{tot}}_I\cup\{\lambda_\sharp\}$: the exclusions of
III.I$'$ Proposition 3.1 ($\mathrm{Re}\,\pi_1\mathcal E^C_I$ and $\lambda_\sharp$) and of III.I$'$ Proposition 2.1
($\mathrm{Re}\,\pi_1\mathcal E^{\mathrm{tot}}_I$) at the $\iota^+$-weight $3+\epsilon_+$; $\mathcal
E^{\mathrm{tot}}_I\supset\mathcal E^C_I$ (III.C (3.1)).

- (E3) No $K^+$-exponent at hand (of the pieces' coefficients, of the rows, and their $\mathbb N_0$-shifts, as in
III.I$''''''''''''''$ Lemma 2.5) has real part $\alpha-2$, $\alpha-1$ or $\alpha$. The first and last are admissibility
(III.I$''''''''''''''$ Lemma 2.5's proof); $\alpha-1$ is new.

- (E4) $\alpha-\mathrm{Re}\,\alpha_0\ne-\mu$ and $\alpha-1-\mathrm{Re}\,\alpha_0\ne-\mu$ for every root $\mu$ and the
finitely many tf-exponents $\alpha_0$ of levels 1-2 of III.I$'''''''''''$ Proposition 3.1: III.G$''''$ (4.2) at
$\ell_{\mathrm{zf}} = \alpha-2$ and $\alpha-3$.

- (E5) Vacuous (D295): III.I$''$ Lemma 4.2 excludes no real part; it asks only $\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}}
= \alpha_H+2\in(0,1)$. The label is kept.

- (A$_K$) (optional) $\alpha := 4+\epsilon_K$ is admissible and satisfies (A$_J$), (E3)-(E5).

**Lemma 1.4.** (E1) is a smallness condition on $\epsilon_+$, (E2) excludes finitely many $\epsilon_+$ in any bounded
range, (E3)-(E4) finitely many $\alpha$, (E5) nothing, and (A$_K$) finitely many $\epsilon_K$ at fixed $\epsilon_+$. So
admissible $\alpha$ with (E3)-(E5) exist in
$(4+\epsilon_K-\epsilon'_0,4+\epsilon_K]$, and $\epsilon_+$, $\epsilon_K$ may be decreased to meet (E1)-(E2) and
(A$_K$), as (G$^+$) and (G) already permit.

*Proof.* The excluded numbers are built from finitely many numbers that do not depend on $\alpha$, $\epsilon_+$ or
$\epsilon_K$ within the ranges used: the roots $\mu$, discrete with finitely many in any bounded set (III.F$'$
Proposition 2.3); $\Lambda$ and the tf-exponents $\alpha_0$ of levels 1-2, $\Lambda$-valued below 3 and finitely many
(III.I$''''''''''$ Lemma 1.2); the exponents at hand below $\alpha+1$, finitely many and $\Lambda$-generated
(III.I$''''''''''''''$ Lemma 2.5's proof); $\lambda_\sharp$; and $\mathrm{Re}\,\pi_1\mathcal E^{\mathrm{tot}}_I$, an
index set, finite below any bound. Each of (E2)-(E4) and (A$_K$) removes the values of $\alpha$, $\epsilon_+$ or
$\epsilon_K$ equal to one of finitely many such numbers; (E1) is (G$^+$) itself, an upper bound on $\epsilon_+$.
$\square$

## 2. Two elementary lemmas

**Lemma 2.1 (diagonal terms at $\iota^+\cap K^+$).** Near the corner let $a = t_*^{-c}G(t_*)$ with $G\in H_{\mathrm
b}([1,\infty),|dt_*/t_*|)$, and let $P$ be homogeneous of degree $-m$ in $r$. Then
$aP\in\rho_+^{c+m-\eta}\rho_K^cH_{\mathrm b}$ and $aP\in\rho_+^{c+m}\rho_K^{c-\eta}H_{\mathrm b}$ for every $\eta>0$,
while in general $aP\notin\rho_+^{c+m}\rho_K^cL^2_{\mathrm b}$.

*Proof.* With $t_*^{-1} = \rho_+\rho_K$ and $r^{-1} = \rho_+$, $\rho_+^{-a_+}\rho_K^{-a_K}aP =
\rho_+^{c+m-a_+}\rho_K^{c-a_K}G(1/(\rho_+\rho_K))P_0$, $P_0$ smooth on the sphere. In $s := -\log\rho_+$, $\sigma :=
-\log\rho_K$ the squared $L^2_{\mathrm b}$-norm at $(a_+,a_K) = (c+m,c)$ is $\int_0^\infty T|G(e^T)|^2\,dT$, $T =
s+\sigma$, which $G\in L^2(dT)$ does not bound; with the extra factor $e^{-2\eta s}$ or $e^{-2\eta\sigma}$ it is at most
$(2\eta)^{-1}\|G\|^2$. Derivatives are the same. $\square$

**Lemma 2.2 (circle integrals of bounded families).** Let $Z\hookrightarrow Z_-$ be a continuous injection of Hilbert
spaces, $\gamma$ a circle, and $F:\gamma\to Z_-$ continuous with $\sup_\gamma\|F\|_Z\le M$. Then $I := \int_\gamma
F\,d\lambda$ (in $Z_-$) lies in $Z$, and $\|I\|_Z\le|\gamma|M$.

*Proof.* The Riemann sums $S_n$ converge to $I$ in $Z_-$ and satisfy $\|S_n\|_Z\le|\gamma|M$. A subsequence converges
weakly in $Z$ to some $I'$; the injection is weakly continuous, so the subsequence converges weakly in $Z_-$ to $I'$.
Hence $I = I'$ and $\|I\|_Z\le\liminf\|S_n\|_Z$. $\square$

## 3. The graft at the exact $K^+$-weight

Fix $\varphi\in C^\infty((0,\infty))$, positive, with $\varphi(R) = R$ for $R\le\frac12$ and $\varphi = 1$ for $R\ge2$,
and put $\rho_+ := (t_*\varphi(R))^{-1}$ near $\iota^+$. Near $\iota^+\cap K^+$ it is $1/r$, near $\iota^+\cap\mathscr
I^+$ it is $1/t_*$ (III.I$''$ section 1); so it is a boundary defining function of $\iota^+$. The expansions of [Hin26]
Definition 2.8 (p. 48), in which the classes of the parts are defined (III.A), are in powers of $\rho_+$ and
$\log\rho_+$, with coefficients on $\iota^+$ that carry the weights of the adjacent faces. Near the corner $\log\rho_+ =
-\log t_*-\log\rho_K$, so
$$\rho_+^z(\log\rho_+)^\ell a = t_*^{-z}\sum_{j\le\ell}\tbinom\ell j(-1)^\ell(\log
t_*)^j(\log\rho_K)^{\ell-j}\rho_K^{-z}a.\tag{3.1}$$

**Remark 3.1 (the two conventions at the exact weight).** III.G$''$ Corollary 4.3 takes $f = \sum_{j\le k}\chi_\iota
t_*^{-\lambda_0-2}(\log t_*)^jf^{(j)}_++f'$ with $f^{(j)}_+\in\bigcap_\epsilon
H^{\infty,\ell_I+1,\ell_K-2-\epsilon}_{\mathrm b}(\iota^+)$, and concludes (4.5) at the $K^+$-weight
$\lambda_0+\ell_K-\epsilon$. By (3.1) a source of exact $K^+$-weight $\alpha$ in the sense of Definition 2.8 has
$t_*$-coefficients containing $(\log R)^{\ell-j}R^{-z}a_\ell$, which lie in $H^{\alpha-\mathrm{Re}\,z-\epsilon}$ for
every $\epsilon>0$ but in general not at $\epsilon = 0$:
$\|\rho^{-w+\epsilon}(\log\rho)^kg\|\le(k/e\epsilon)^k\|\rho^{-w}g\|$, and this is sharp. Conversely, for
$k = 1$, $f^{(0)} = 0$ and $f^{(1)} = g$ generic in $H^{\ell_K-2}$, the Definition 2.8 coefficient
$-(\log\varphi)\varphi^zg$ is not in $H^{\alpha}$. So for $k\ge1$ the two classes at the exact weight are incomparable
(for $k = 0$ they coincide), and Corollary 4.3 cannot be applied at $\epsilon = 0$ to a Definition 2.8 source; in its
convention it is stated with the minus, with constants of order $\epsilon^{-k}$. Whether an exact statement exists in
that convention is not decided here; none is needed. The source's Corollary 9.12 (p. 179) has the same minus; its
Proposition 11.34 states the exact weight after the same step ((11.120b), p. 254), which Corollary 3.2 justifies.

**Corollary 3.2 (III.G$''$ Corollary 4.3 at the exact $K^+$-weight).** Let $\mathrm{Re}\,\lambda_0>1$, let $l_0$ be the
order of the pole of $N_{\iota^+}(\bar L,\cdot)^{-1}$ at $\lambda_0$ ($0$ if none), let $\ell_I$ be as in III.G$''$
Theorem 4.2 with $\mathrm{Re}\,\lambda_0<\ell_I$, and let $\alpha\in\mathbb R$ with $\ell_K :=
\alpha-\mathrm{Re}\,\lambda_0\in(-1,\ell^{\max}_K)$, $\ell_K\ne-\mu$ for every root $\mu$, and
$\ell_K\notin\mathrm{Re}\,\pi_1\mathcal E_K$. Let $k\in\mathbb N_0$ and
$$f = \sum_{j\le k}\chi_\iota\rho_+^{\lambda_0+2}(\log\rho_+)^ja_j+f',\qquad a_j\in H^{\infty,\ell_I+1,\alpha}_{\mathrm
b}(\iota^+),\quad f'\in H^{\infty,\ell_I+1,\infty,\alpha}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-},\tag{3.2}$$
the weight $\alpha$ of $a_j$ being at $\iota^+\cap K^+$, as Definition 2.8 prescribes for a source of $K^+$-weight
$\alpha$. Then there are $u^{(j)}_{b,0}$ of the form of III.G$''$ (4.3), with $\lambda_0$ for $\lambda$ and a factor
$(\log t_*)^j$, and $v_m\in H^{\infty,(\langle\mathcal E^C_{\iota^+,\mathscr I}\rangle,\ell_I),\alpha}_{\mathrm
b}(\iota^+)$, $m\le k+l_0$, all linear in $(a_j,f')$, such that $u :=
\sum_j\chi_Ku^{(j)}_{b,0}+\sum_m\chi_\iota\rho_+^{\lambda_0}(\log\rho_+)^mv_m$ satisfies
$$f-L_bu\in H^{\infty,(\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}+2,\ell_I+1),\ \lambda_0+2+\mathcal
E_{\mathrm{ind}}+(0,k+l_0),\ \alpha}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-},\tag{3.3}$$
the $\iota^+$-index set taken with respect to $\rho_+$. For each $k'$ there are $d$ and $C$ bounding every order-$k'$
seminorm of $u$ and of $f-L_bu$ by $C(\sum_j\|a_j\|_{k'+d}+\|f'\|_{k'+d})$. By (3.1), (3.2) implies Corollary 4.3's
hypotheses and (3.3) implies its (4.5). For $k = l_0 = 0$ it is III.G$''$ Theorem 4.2 at $\lambda = \lambda_0$.

The proof uses a lemma on the family of Theorem 4.2 along a circle.

*The circle.* Choose $\delta\in(0,\frac14)$ with $\delta<\min(\mathrm{Re}\,\lambda_0-1,\ \ell_I-\mathrm{Re}\,\lambda_0,\
\ell^{\max}_K-\ell_K)$, such that $\bar D := \{|\lambda-\lambda_0|\le\delta\}$ meets $\mathrm{spec}_{\iota^+}(\bar L)$
at most in $\lambda_0$, and $J := [\ell_K-3\delta,\ell_K+\delta]\subset(-1,\ell^{\max}_K)$ contains no $-\mu$ and no
point of $\mathrm{Re}\,\pi_1\mathcal E_K$. This is possible, as the spectrum has finitely many points in each half plane
(III.G$'$ Lemma 4.2 (a)) and the roots and $\mathcal E_K$ are discrete. On $\partial D$, $\ell_K(\lambda) :=
\alpha-\mathrm{Re}\,\lambda\in J$, $\lambda\ne1$, $1<\mathrm{Re}\,\lambda<\ell_I$, and the window $\mathcal W(\ell)$ of
III.G$'$ Theorem 3.1 is the same for every $\ell\in J$. For $a\in H^{\infty,\ell_I+1,\alpha}_{\mathrm b}(\iota^+)$ put
$f_+(\lambda) := \varphi^{-\lambda-2}a$. Near $R = 0$, $|R^{-\lambda-2}| = R^{-\mathrm{Re}\,\lambda-2}$ and
$(R\partial_R)^iR^{-\lambda-2} = (-\lambda-2)^iR^{-\lambda-2}$, and $\varphi = 1$ near $\mathscr I^+$; so
$\|f_+(\lambda)\|_{H^{k',\ell_I+1,\ell_K(\lambda)-2}}\le C\|a\|_{H^{k',\ell_I+1,\alpha}}$ uniformly on $\bar D$.
III.G$''$ Theorem 4.2 at $\lambda\in\partial D$, with $\ell_K(\lambda)$ and the source $f_+(\lambda)$, gives $u(\lambda)
= \chi_Ku_{b,0}(\lambda)+\chi_\iota t_*^{-\lambda}\tilde u(\lambda)$ and the remainder $r(\lambda) := \chi_\iota
t_*^{-\lambda-2}f_+(\lambda)-L_bu(\lambda)$, whose $K^+$-weight in (4.4) there is $\mathrm{Re}\,\lambda+\ell_K(\lambda)
= \alpha$ for every $\lambda$. By the choice of $\rho_+$, $\chi_\iota t_*^{-\lambda-2}f_+(\lambda) =
\chi_\iota\rho_+^{\lambda+2}a$ and $t_*^{-\lambda}\tilde u(\lambda) = \rho_+^\lambda U(\lambda)$ with $U(\lambda) :=
\varphi^\lambda\tilde u(\lambda)$. Since $\partial_\lambda$ brings the factor $-\log\varphi$ and $R^\delta|\log R|$ is
bounded, $f_+$ is holomorphic near $\bar D$ with values in $H^{\ell_I+1,\ell_K-3\delta-2}$; at that fixed weight Theorem
4.2's family is holomorphic off the spectrum (III.G$''$, (9.42) of the source), so $u(\lambda)$ and $r(\lambda)$ are
holomorphic near $\partial D$, meromorphic in $D$ with at most a pole at $\lambda_0$, in spaces $Z_-$ of $K^+$-weight
$\alpha-4\delta$.

**Lemma 3.3 (exact bounds on the circle).** There are $d$ and $C$ such that for every $\lambda\in\partial D$
$$\|U(\lambda)\|_{H^{k',(\langle\mathcal E^C_{\iota^+,\mathscr I}\rangle,\ell_I),\alpha}_{\mathrm
b}(\iota^+)}+\sum|Y^{(\mu)}_\tau(\lambda)|\le C\|a\|_{k'+d},$$
and $r(\lambda) = \sum_{(e,p)}\chi\rho_+^{\lambda+2+e}(\log\rho_+)^pc_{e,p}(\lambda)+r_N(\lambda)$, a finite sum over
$(e,p)\in\mathcal E_{\mathrm{ind}}$ with $\mathrm{Re}\,e<N$, with each $c_{e,p}(\lambda)$ bounded by $C\|a\|_{k'+d}$ in
$H^{k',(\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}+2,\ell_I+1),\alpha}_{\mathrm b}(\iota^+)$ and $r_N(\lambda)$ in
the space of plain $\iota^+$-weight $\mathrm{Re}\,\lambda_0+2+N-\delta$ and $K^+$-weight $\alpha$.

*Proof.* (i) *At the lower weight.* III.G$'$ Theorem 3.1 (2) bounds $N_{\iota^+}(\lambda)^{-1}$ at the fixed weight
$\ell_K^- := \ell_K-3\delta$, locally uniformly in $\lambda$ off the poles, hence uniformly on the compact circle
$\partial D$; and the coefficients $Y^{(\mu)}_\tau$ are continuous linear functionals of $(u,f)$ there. So $Y(\lambda)$
and $\tilde u(\lambda)$ are bounded in $H^{\ell_K^-}$ uniformly on $\partial D$.

(ii) *Up to the exact weight, uniformly.* Near $R = 0$, III.G$'$ (1.3) gives $R^2N_{\iota^+}(\lambda) =
A_0+RA_1(\lambda)$ with $A_0 = \tilde L(0)(\omega,-R\partial_R,\partial_\omega)$ independent of $\lambda$, b-elliptic,
with boundary spectrum $\{-\mu\}$. With $\tilde u = u_+-\chi_Ku_0$ and $N_{\iota^+}(\lambda)u_+ = 2f_+$,
$$A_0(\chi\tilde u) = \chi\big[2R^2f_+(\lambda)-RA_1(\lambda)\tilde
u-R^2N_{\iota^+}(\lambda)(\chi_Ku_0(\lambda))\big]+[A_0,\chi]\tilde u =: g(\lambda).$$
Its terms lie in $R^{\ell_K(\lambda)}H_{\mathrm b}$ (the first), in $R^{\ell_K^-+1}H_{\mathrm b}\subset
R^{\ell_K(\lambda)}H_{\mathrm b}$ (the second, as $4\delta\le1$), in $R^{-\mu+k_\mu+1}C^\infty\subset R^3C^\infty$ (the
third, by the form of $u_0$, III.G$'$ (2.6) and Lemma 2.6), and have compact support in $R>0$ (the last); all uniformly
on $\partial D$, bounded by $C\|a\|$. The strip $\{\mathrm{Re}\,\zeta\in J\}$ avoids $\{-\mu\}$, so
$$K := \sup_{\mathrm{Re}\,\zeta\in J}\sum_{i\le2}|\zeta|^{2-i}\|N(A_0,\zeta)^{-1}\|_{H^s\to H^{s+i}}<\infty,$$
by the elliptic bound (E1) of III.A for $|\mathrm{Im}\,\zeta|$ large and by continuity on the compact rest of the strip.
Then the Mellin transform of $\chi\tilde u$ is $N(A_0,\cdot)^{-1}$ applied to that of $g$; it continues holomorphically
from $\mathrm{Re}\,\zeta<\ell_K^-$ to $\mathrm{Re}\,\zeta\le\ell_K(\lambda)$ with no pole in the strip; moving the line
as in III.A Lemma 1.4's proof and using Plancherel on $\mathrm{Re}\,\zeta = \ell_K(\lambda)$ gives
$$\|\chi\tilde u(\lambda)\|_{R^{\ell_K(\lambda)}H^{k'}_{\mathrm b}}\le
K'\|g(\lambda)\|_{R^{\ell_K(\lambda)}H^{k'-2}_{\mathrm b}}+C\|\tilde u(\lambda)\|_{R^{\ell_K^-}H^{k'}_{\mathrm b}},$$
with $K'$ depending only on $K$ and $J$. This is III.A Lemma 1.4 with its constant uniform over the weights in $J$,
which its Mellin proof gives. As $\varphi^\lambda$ is b-smooth with $|R^\lambda| = R^{\mathrm{Re}\,\lambda}$,
$\|U(\lambda)\|_\alpha\le C\|\tilde u(\lambda)\|_{\ell_K(\lambda)}$.

(iii) *The remainder.* Near the corner, where $\chi_K = \chi_\iota = 1$, III.G$''$ Lemma 4.1 for $t_*^{-\lambda}\tilde
u$ gives $r(\lambda) = \frac12t_*^{-\lambda-2}N_{\iota^+}(\lambda)u_0-L_bu_{b,0}-\frac12t_*^{-\lambda-4}v^2B\tilde u$.
The explicit part has $K^+$-exponents $\ge\lambda-\mu+k_\mu+1\ge\lambda+3$ and $\iota^+$-exponents in
$\lambda+2+\mathcal E_{\mathrm{ind}}$, with coefficients polynomial in $\lambda$ times $Y(\lambda)$; since
$\mathrm{Re}\,\lambda+3-\alpha\ge3-\ell_K-\delta>0$ it lies at $K^+$-weight $\alpha$ with uniform bounds, its
$\log\rho_K$ powers sitting strictly above $\alpha$. In the last term $t_*^{-\lambda-4}v^2 =
\rho_+^{\lambda+4}\varphi^{\lambda+2}\psi^2$, $\psi := \varphi/R$; Taylor expansion of $B$'s coefficients in $1/r =
\rho_+\psi$ gives terms $\rho_+^{\lambda+4+m}\psi^{m+2}\varphi^2B^\lambda_mU(\lambda)$ with $B^\lambda_m :=
\varphi^\lambda B_m\varphi^{-\lambda}$ polynomial in $\lambda$ and coefficients in $H^{\alpha+2}\subset H^\alpha$ at $R
= 0$. Near $K^+$ with $r$ bounded, $r(\lambda) = \chi_\iota\rho_+^{\lambda+2}a-L_b(\rho_+^\lambda
U(\lambda))-L_bu_{b,0}$ with $\rho_+ = 1/r$ smooth, and $L_b\in\mathrm{Diff}_{\mathrm b}$ there (III.I$''$ section 1),
so every term is at weight $\alpha$ uniformly. Away from $K^+$, the proof of III.G$''$ Theorem 4.2 applies verbatim with
$u_+(\lambda)$ uniformly bounded. This exhibits the decomposition of $r(\lambda)$ with the stated bounds. $\square$

*Proof of Corollary 3.2.* Since $\partial^j_\lambda\rho_+^{\lambda+2} = (\log\rho_+)^j\rho_+^{\lambda+2}$, Cauchy's
formula gives
$$\chi_\iota\rho_+^{\lambda_0+2}(\log\rho_+)^ja_j = \frac{j!}{2\pi i}\oint_{\partial
D}(\lambda-\lambda_0)^{-j-1}\chi_\iota t_*^{-\lambda-2}f_{+,j}(\lambda)\,d\lambda,\qquad f_{+,j}(\lambda) :=
\varphi^{-\lambda-2}a_j.$$
Put $u := \sum_j\frac{j!}{2\pi i}\oint(\lambda-\lambda_0)^{-j-1}\Phi_{\iota,b}(\lambda)f_{+,j}(\lambda)\,d\lambda$, an
integral in $Z_-$, with which $L_b$ commutes; then $f-L_bu = f'+\sum_j\frac{j!}{2\pi
i}\oint(\lambda-\lambda_0)^{-j-1}r_j(\lambda)\,d\lambda$. Expanding $\rho_+^{\lambda+c} =
\rho_+^{\lambda_0+c}\sum_m(\log\rho_+)^m(\lambda-\lambda_0)^m/m!$ pointwise, $u$'s $\iota^+$-part is
$\chi_\iota\rho_+^{\lambda_0}\sum_m(\log\rho_+)^mv_m$ with $v_m = \sum_j\frac{j!}{m!}\frac1{2\pi
i}\oint(\lambda-\lambda_0)^{m-j-1}U_j(\lambda)\,d\lambda$, which vanish for $m>k+l_0$ (Laurent order); the remainder's
coefficients are circle integrals of the $c_{e,p}(\lambda)$, which are polynomial in $\lambda$, $Y(\lambda)$ and
$U(\lambda)$, hence meromorphic in $D$ with pole order at most $l_0$, so the same Laurent cut-off applies to them, and
its rest the circle integral of $r_N(\lambda)$. Lemma 2.2, with $Z$ the space at the exact weight $\alpha$ (the
coefficient spaces on $\iota^+$, and the space of plain $\iota^+$-weight $\mathrm{Re}\,\lambda_0+2+N-\delta$) and $Z_-$
the same at $\alpha-4\delta$, with Lemma 3.3 bounding the integrands, gives $v_m\in H^{(\langle\mathcal
E^C\rangle,\ell_I),\alpha}(\iota^+)$, the coefficients of $f-L_bu$ in $H^{(\mathcal
E^{\mathrm{tot}}+2,\ell_I+1),\alpha}(\iota^+)$ with exponents in $\lambda_0+2+\mathcal E_{\mathrm{ind}}+(0,k+l_0)$, and
the rest at $K^+$-weight $\alpha$. As $N$ is arbitrary, this is (3.3). The $u_{b,0}$-part becomes
$\sum_j\chi_Ku^{(j)}_{b,0}$ with the Laurent coefficients of $Y(\lambda)$ (the form (4.3)). Linearity and the bounds,
with constants $C\delta^{-k-l_0-1}$, follow from Lemma 3.3. $\square$

**Proposition 3.4 (the graft's uses at the top level).** Let $f\in\mathcal Y^0_{\mathrm{ex}}(\alpha)$, with (E1)-(E3).
Then III.I$''''''''''$ Proposition 3.1 holds with: (a) $u_I$ of $\iota^+$-data $(\mathcal E_I,3+\epsilon_+)$; (b)
$K^+$-weight $\alpha-2$ in place of $\alpha-2-\epsilon$; (c) $f^\flat\in H^{\infty,\ell_I+1,(\mathcal
E^\flat+2,w_+),\alpha}_{\mathrm b}$. And III.I$''''''''''''$ Theorem 3.1's piece (ii), the graft remainder, has
$K^+$-order exactly $\alpha$.

*Proof.* (a) Step 1 of III.I$''''''''''$ Proposition 3.1 takes $\breve\ell_+ := w_+-2-\epsilon$ "off its exclusions for
all but finitely many $\epsilon$"; the exclusions are those of III.I$'$ Proposition 3.1 ($\mathrm{Re}\,\pi_1\mathcal
E^C_I$ and $\lambda_\sharp$) and of III.I$'$ Proposition 2.1 ($\mathrm{Re}\,\pi_1\mathcal E^{\mathrm{tot}}_I$), and by
(E2) $\breve\ell_+ := w_+-2 = 3+\epsilon_+$ is allowed. III.I$'$ Propositions 2.1 and 3.1 are exact at an allowed
weight; (E2) is used again in Step 2's $\mathscr I^+$-removals and in Proposition 4.3's $\mathscr I^+$-regularity
(III.I$'$ Proposition 2.1 at $\ell_+ = 3+\epsilon_+$). (c) At $K^+$: Step 2 takes $c_K := \alpha$ and applies
the graft to the coefficients of the current source, which lie in $H^{\infty,\ell_I+1,\alpha}_{\mathrm b}(\iota^+)$ with
respect to $\rho_+$ ($\mathcal Y^0(\alpha)$ is a Definition 2.8 class, exact at $K^+$); Corollary 3.2 replaces Corollary
4.3, and each graft error has the exact $K^+$-weight $\alpha$ by (3.3), so the iteration closes at $\alpha$. The part of
the source that does not reach $\iota^+$ near the corner (the difference between Definition 2.8's cut-off and
$\chi_\iota$) goes into $f'$. Step 1's "$K^+$-weight $\alpha-\epsilon$" is a free weakening ($f_1$ has $K^+$-weight
$\alpha$). At $\iota^+$: $f^\flat = f-L_{b_0}(u_I+u_\iota)$ with $f$ at $(\mathcal E^\flat+2,w_+)$, $L_{b_0}u_I$ at
$(\mathcal E_I+2,w_+)$ by (a), and $u_\iota$ a finite sum of single $\iota^+$-terms; by (E1) no exponent has real part
$w_+$, so the integrations of III.A Lemmas 1.2 and 1.4, which are exact at weights that are not exponents, are applied
at such a weight (Definition 2.8's class itself expands every exponent of real part at most the weight). (b) Its
$K^+$-ingredients are $u_\lambda$'s $\iota^+$-part, of $K^+$-weight $\alpha>\alpha-2$; the rows, identified up to
$K^+$-weight $\mathrm{Re}\,\lambda_0+1-\epsilon>\frac52>\alpha-2$; and the c-rows of rate $>2+\epsilon_K\ge\alpha-2$, of
weight their rate minus $\epsilon$, which exceeds $\alpha-2$ for $\epsilon$ small; each is strict. Piece (ii) of
III.I$''''''''''''$ Theorem 3.1 is the graft remainder $\chi_\iota\rho_+^{\lambda_0}(\log\rho_+)^mv_m$ of Corollary 3.2,
of $K^+$-order exactly $\alpha$. $\square$

## 4. The spectral construction at exact weights

**Proposition 4.1 (III.A Proposition 4.2 is exact at $K$ and zf).** For $\beta_K\in(0,\infty)\setminus(\mathbb
N\cup\mathrm{Re}\,\pi_1E_K)$, III.A Proposition 4.2 (1) maps the exact $K$-weight $\beta_K$ to the exact zf-weight
$\beta_K-1$ ((4.3) there) and (2) maps it back ((4.5) there); their $\epsilon$'s sit at $\mathscr I$ and scf only. The
constants are bounded for $\beta_K$ in compact subsets of $(0,\infty)\setminus(\mathbb N\cup\mathrm{Re}\,\pi_1E_K)$, the
other data fixed.

*Proof.* The chain below Proposition 4.2 is: II.G$'$ Lemma 2.2, Plancherel as an equivalence of norms at every weight;
II.G$'$ Proposition 2.8, which converts $H^{\beta-\frac12}$ into $|\sigma|^{\beta-1}L^2(|d\sigma/\sigma|)$ modulo the
Taylor polynomial, in both directions, for $\beta\in(0,\infty)\setminus\mathbb N$, losing derivatives only, through the
Hardy inequalities of its Lemma 2.3 (b)-(c), whose constants are built from $2^{\pm(\theta-\frac12)}$, $\theta$ the
fractional part of $\beta-\frac12$, and are bounded for $|\theta-\frac12|\ge c$, that is for $\beta$ away from $\mathbb
N$; and II.G$'$ Propositions 3.3 (1) and 3.5 (1), exact at $K$, whose $\epsilon$ is at scf. Proposition 4.2's proof
raises its auxiliary $\tilde\beta_K$ back to $\beta_K$ ("with the full weight $\beta_K$ at $K$") and integrates at zf by
III.A Lemma 1.2 at weights $\ne$ the exponents, with constant $|\alpha|^{-1}$ in (1.2), bounded away from them. The
derivative losses are piecewise constant in the weights. $\square$

At the weights used below, $\alpha$, $\alpha-1$, $\alpha-2$, the fractional part of $\beta-\frac12$ differs from
$\frac12$ by $\alpha-4\ge\epsilon_K-\epsilon'_0>0$.

**Lemma 4.2 (III.I$''''''''''$ Lemma 2.4 (b) without $\delta$).** Under the hypotheses of III.I$''''''''''$ Lemma 2.4,
(b) holds with $O(t^{-\beta-1})$ in place of $O(t^{-\beta-1+\delta})$, also after applying $(t\partial_t)^l$.

*Proof.* $\int_{|\sigma|<1/|t|}|\sigma|^\beta d\sigma = \frac2{\beta+1}|t|^{-\beta-1}$ ($\beta>-1$). On $(1/|t|,c)$,
integrate by parts $N := \lceil\beta\rceil+1$ times, using $|\partial^j_\sigma(\chi r^\pm)|\le C|\sigma|^{\beta-j}$
(from the hypothesis and $\partial^j_\sigma = \sigma^{-j}\sum_{i\le j}a_{ji}(\sigma\partial_\sigma)^i$): the boundary
terms at $|\sigma| = 1/|t|$ are $O(|t|^{-\beta-1})$, and the integral is at most
$|t|^{-N}\int_{1/|t|}^c\sigma^{\beta-N}d\sigma\le|t|^{-\beta-1}/(\lceil\beta\rceil-\beta)$, with
$\lceil\beta\rceil-\beta>0$ as $\beta\notin\mathbb N_0$. And $t\partial_t\mathcal F^{-1}v = \mathcal
F^{-1}(-(1+\sigma\partial_\sigma)v)$ preserves the hypothesis. $\square$

**Proposition 4.3 (III.I$'''''''''''$ Proposition 3.1 at exact weights).** Let $\alpha$ satisfy Definition 1.3, and let
$f^\flat$ and $u_I$ be as in Proposition 3.4. Run III.I$'''''''''''$ Proposition 3.1 with the zf-parameter $0$
(zf-weights $\ell_j := \alpha-1-j$, $\ell_3 := \alpha-4\in(0,\epsilon_K]$), the level-2 threshold
$\mathrm{Re}\,\alpha_0<2+\epsilon_+$, $\mu_2 := 2+\eta^0_2$ (the value fixed in III.I$'''''''''''$ section 1), $\mu' :=
2+\epsilon_+$, and the first level-3 tf-weight $\tau_3 := 1+\epsilon_+$. Then (3.1) of III.I$'''''''''''$ holds with
$\iota^+$-data $(\mathcal E_\iota,3+\epsilon_+)$ for $v_{\mathrm{low}}$ minus the constant columns and with $K^+$-weight
$\alpha-2$, with the same $S_\nu$; III.I$'''''''''''$ Lemma 3.2 (3.2) and Theorem 4.1 (4.2) hold at $K^+$-weight
$\alpha-2$; and all tensors are those of the present construction.

*Proof.* We follow III.I$'''''''''''$ Proposition 3.1's steps; only the weights change.

*Step 0.* III.I$''$ Lemma 4.1 with $\beta_K = \alpha\in(4,5)$, then III.A Proposition 4.2 (1) with $\beta_\iota = w_+$,
$E_\iota = \mathcal E^\flat+2$, $E_I = \emptyset$, $\beta_K = \alpha$, $E_K = \emptyset$; its hypotheses hold
($w_+\notin\mathrm{Re}\,\pi_1E_\iota$ by (E1); $\ell_I+1>w_+-1$ by (H4) of III.I$''''''''''$). By Proposition 4.1,
$g_0\in H^{\infty,(\frac52-\epsilon,(\mathcal E^\flat+1,w_+-1),((0,0),\alpha-1))}_{\mathrm b}$.

*Levels 0-1.* III.I$'''''''''''$ Lemma 2.1 at $\mu' = w_+-1$ and $3+\epsilon_+$ rests on III.A Lemma 1.4 at $\beta =
\mu'-2 = 2+\epsilon_+$, resp. $1+\epsilon_+$: not the real part of a root, since integer roots are excluded by
non-integrality and non-integer roots with $|\mu|\le50$ have $d(\mathrm{Re}\,\mu,\mathbb
Z)\ge\epsilon_{\mathrm{ind}}>\epsilon_+$ (III.F$'$ (2.2)). III.I$'''''''''''$ Lemma 2.2 lowers the tf-weight by 1 and
the zf-weight $((0,0),z)$ to $((0,0),z-1)$ exactly. III.G$''''$ Proposition 4.4 at level 1 with $\ell_{\mathrm{zf}} =
\alpha-2$: its conditions (4.2) hold ($-\epsilon_{\mathrm{ind}}<\alpha-\mathrm{Re}\,\alpha_0$;
$\alpha-2-\min(\mathrm{Re}\,\alpha_0-2,0)<3 = \ell^{\max}_K$ under (C5) of III.I$''''''''''$; $\alpha-2\notin\mathbb
N_0$; the root condition is (E4)), and its remainder keeps zf $((0,0),\alpha-2)$ exactly. So $g_1$, $g_2$ have
tf-weights $3+\epsilon_+$, $2+\epsilon_+$ and zf-weights $\alpha-2$, $\alpha-3$.

*Level 2.* The tf-exponents of the level-2 sources are $u$-exponents minus 1, $(\Lambda-1)$-valued; by (E1) none has
real part in $(2,2+\epsilon_+]$, so the threshold $2+\epsilon_+$ treats the same $(\alpha_0,k)$ as $2+\eta^0_2$, and
Proposition 4.4's conditions are those already met (with (E4) at $\ell_{\mathrm{zf}} = \alpha-3$). After the rounds the
zf-coefficient $F$ of the level-2 source lies in $H^{\infty,(E,2+\epsilon_+)}_{\mathrm b}(\bar X)$ with
$\min\mathrm{Re}\,E>2+\epsilon_+$. III.I$'''''''''''$ Lemma 2.1 with $\mu = \mu_2$, $\mu' = 2+\epsilon_+$:
$\mu_2\in(2,3)$, $\mu'\in(\mu_2,5]$, $\min\mathrm{Re}\,E>\mu$; III.H Proposition 3.2 at the interior weight $\mu_2-2 =
\eta^0_2\in(0,1)$; III.A Lemma 1.4 up to $\mu'-2 = \epsilon_+$, not a root, as no root has real part in $(0,1]$
(III.F$'$ Proposition 2.3 (a)). So $\hat u_2\in H^{\infty,\epsilon_+}_{\mathrm b}$, and Lemma 2.2 gives $g_3$ of
tf-weight exactly $1+\epsilon_+$, with no tf-exponent of real part $\le1+\epsilon_+$ (the exponents of $E-1$ exceed
$1+\epsilon_+$; those of $2+\mathcal E_{\mathrm{col}}$ are $\ge2$), and zf $((0,0),\ell_3)$.

*Level 3.* III.G$''''$ Proposition 5.1 at $\alpha_\tau = 1+\epsilon_+$, $\ell_{\mathrm{zf}} = \ell_3$:
$\alpha_\tau\in(1,2)$; $w := \ell_3-\alpha_\tau+2 = \ell_3+1-\epsilon_+\in(1-\epsilon_+,1)$, so
$-\epsilon_{\mathrm{ind}}<w<\ell^{\max}_K$; $\ell_3\notin\mathbb N_0$; $w\ne-\mu$ and $2-\alpha_\tau =
1-\epsilon_+\ne-\mu$, as both lie within $\epsilon_+<\epsilon_{\mathrm{ind}}$ of the integer 1 without being integers
(III.F$'$ (2.2)). Its proof uses the conditions $2-\alpha_\tau+j\ne-\mu$ only for $j\le\lfloor\ell_{\mathrm{zf}}\rfloor
= 0$. The output is exact at tf and zf: the piece $\sigma^3u$ has tf-weight $2+\epsilon_+$, zf $((0,0),\ell_3)$. Later
rounds start from tf-weights $\ge1+\epsilon_++\epsilon_{\mathrm{ind}}-\epsilon$, with fixed room above $2+\epsilon_+-1$;
their $\alpha_\tau$ may be lowered freely, so their conditions hold off a finite set of $\alpha_\tau$, and their
zf-weight $\ell_3$ is kept. The final zero-energy solve: III.I$''$ Lemma 4.2 with $\beta_{\mathrm{zf}} := \ell_3$
(III.I$''$ Lemma 4.2 puts no condition on $\beta_{\mathrm{zf}}$) and $\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}}\in(0,1)$
gives $\dot b_f$, $S_f\in H^{\infty,\ell_3}_{\mathrm b}$ and $\hat u_f$ with zf-weight $\ell_3$.

*Step 5.* Lemma 4.2 with $\beta := \alpha-3\notin\mathbb N_0$: the exponents with $\mathrm{Re}\,z<\alpha-3$ are in $E$,
those above in $r^\pm$, none at $\alpha-3$ by (E3); $r^\pm = O(|\sigma|^{\alpha-3})$ follows from the zf-weight
$\alpha-3$ of $\sigma^3\hat h^{\mathrm{aug}}(S_f)$ by the one-dimensional b-Sobolev embedding in $\log|\sigma|$. This
gives $O(t_*^{-\alpha+2})$ in $\{r\le R\}$; Step 6 needs only $o(t_*^{-2})$.

*Step 7.* The pieces have zf-data $((0,0)\bar\cup(E_K-1),\alpha-3)$ and tf-data $(E_{\mathrm{tf}},2+\epsilon_+)$ with
$E_{\mathrm{tf}}+1$ $\Lambda$-valued below $3+\epsilon_+$: the zero-energy pieces $\sigma^j\chi_{\mathrm{zf}}\hat u_j$
($j\le2$) at tf $2+\epsilon_+$; the tf-model pieces, polyhomogeneous at tf; the first level-3 round at $2+\epsilon_+$
and the later ones above. III.A Proposition 4.2 (2) with $\beta_\iota := 3+\epsilon_+$
($\notin\mathrm{Re}\,\pi_1E_\iota$ by (E1)) and $\beta_K := \alpha-2$ ($\notin\mathbb N\cup\mathrm{Re}\,\pi_1E_K$ by
admissibility) gives $v_{\mathrm{low}}$ minus the constant columns in
$H^{\infty,\frac32-4\epsilon,(E_\iota,3+\epsilon_+),(E_K,\alpha-2)}_{\mathrm b}$; the constant columns are
polyhomogeneous at $\iota^+$ with $\Lambda$-valued exponents, none at $3+\epsilon_+$. The matching (4.4) and the
coefficient identification are as there. III.I$'''''''''''$ Lemma 3.2 and Theorem 4.1 need only Step 0's count, which
has room ($w_0+a_K>\alpha$).

*Same tensors.* Moving $\mu'$ only moves where Lemma 1.4 stops; the level-2 solve is at $\mu_2$ as before (III.H
Proposition 3.2's inverses at two such weights agree); the threshold treats the same exponents; and Proposition 5.1
solves by Mellin inversion on $\mathrm{Re}\,\lambda = \alpha_\tau-2$, and moving that line from $\eta^0_2-1-2\epsilon$
to $\epsilon_+-1$ crosses no root (a root in $(-1,-1+\epsilon_+]$ would lie within $\epsilon_+<\epsilon_{\mathrm{ind}}$
of $-1$). $\square$

**Lemma 4.4 (III.I$''''''''''''$ Lemma 2.2 in $L^2$).** In III.I$''''''''''''$ Lemma 2.2 let $a>-1$ with
$a+2,a+3\notin\mathbb N$. Then $A\in\dot H^{\infty,a+2}_{\mathrm b}$, $B\in\dot H^{\infty,a+3}_{\mathrm b}$, and the
remainders $R_S$, $R_b$ have $K^+$-order $a+4$ in the $L^2$-b sense: $\chi_{\{r\le t_*/8\}}R_S\in
t_*^{-a-4}r^{-1}H^\infty_{\mathrm b}$ ($L^2$ in $|dt_*/t_*|$, locally in $x$, with b-derivatives), and likewise $R_b$.

*Proof.* $A$, $B$ are exact by II.G$'$ Proposition 2.8 (2) at the non-integer weights $a+2$, $a+3$ (zf-weights $a+1$,
$a+2$ of $-\chi\sigma S$ and $i\chi\sigma^2\dot b$, zero Taylor polynomial). With $a_0 := \mathcal F^{-1}[-\chi\sigma
S]\in H^{\infty,a+2}_{\mathrm b}(\mathbb R)$ and $\partial_t = t^{-1}(t\partial_t)$ on $t\ge1$, $a_0''\in
t^{-a-4}H^\infty_{\mathrm b}([1,\infty),|dt/t|)$. The remainder is $-h(S)\iint_0^1\tau^2\theta
a_0''(t-\theta\tau)\,d\theta\,\phi_x(\tau)\,d\tau$ plus the $\breve h$-term with $\tau a_0''$. On $\{r\le t/8,\
t\ge8\}$, $\mathrm{supp}\,\phi_x\subset[0,4\max(r,1)]\subset[0,t/2]$, so $t-\theta\tau\in[t/2,t]$, $t^{a+4}\le
C(t-\theta\tau)^{a+4}$ and $dt/t\le2\,d(t-\theta\tau)/(t-\theta\tau)$; Minkowski's inequality in $(\theta,\tau)$ bounds
$\|t^{a+4}\cdot\|_{L^2(|dt/t|)}$ by $C\max(r,1)^2\|a_0\|_{H^{2,a+2}_{\mathrm b}}$. $t\partial_t$ commutes with the
translation up to the factor $t/(t-\theta\tau)\in[1,2]$ and its derivatives, and the $x$-derivatives fall on $\phi_x$,
$h$, $\breve h$; with $|h|\lesssim r^{-3}$, $|\breve h|\lesssim r^{-2}$ this is $t^{-a-4}r^{-1}$ in $L^2$. $\square$

The same applies to the Taylor remainder of III.I$''''''''''''$ Theorem 3.1's piece (vii) ("$K^+$-order $\ge\alpha$"):
taking the Taylor order one higher makes its pointwise order strictly greater than $\alpha$, hence its $L^2$-order at
least $\alpha$.

**Lemma 4.5 (III.I$''''''''''''$ Lemma 2.1 (a) in $L^2$).** In III.I$''''''''''''$ Lemma 2.1 (a), if moreover
$w+1\notin\mathbb N$, then $\chi_+y\in\dot H^{\infty,w+1}_{\mathrm b}$ exactly.

*Proof.* The coefficient is $\chi_+\mathcal F^{-1}(\chi c)$ with $c$ of zf-weight $w$; II.G$'$ Proposition 2.8 (2), with
zero Taylor polynomial and $\beta = w+1\notin\mathbb N$, gives the exact weight. (The printed proof by symbol estimates
is pointwise and gives only the $L^2$-weight $(w+1)-$.) $\square$

**Proposition 4.6 (III.I$''''''''''''$ Theorem 3.1 at exact weights).** Let $\alpha$ satisfy Definition 1.3 and the
sources be as in Propositions 3.4 and 4.3. Then III.I$''''''''''''$ Theorem 3.1 holds with $\dot S_{\mathrm{rem}}\in\dot
H^{\infty,\alpha-2}_{\mathrm b}$, $\dot b_{\mathrm{rem}}\in\dot H^{\infty,\alpha-1}_{\mathrm b}$, $w_\rho :=
3+\epsilon_+-d_\rho$ with $\dot Y_\rho\in\dot H^{\infty,\mathcal Q(\mathcal
E_\sharp-d_\rho,3+\epsilon_+-d_\rho)}_{\mathrm b}$, and $\tilde u\in H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),(\mathcal E_\sharp,3+\epsilon_+),\alpha}_{\mathrm b}$.

*Proof.* *Step 0.* $f'$ has $K^+$-weight $\alpha$: $G(\vec W)\in\mathcal Y^0_{\mathrm{ex}}(\alpha)$; $(L-L_{b_0})u_0$
has $K^+$-weight $w_0-\epsilon+a_K>\alpha$ for small $\epsilon$ (the printed "$\ge\alpha-\epsilon$" is a free
weakening); the graft by Proposition 3.4; and $L_{b_0}m_\nu$ is of order $>\frac92>\alpha$. *Step 1.* (ii) by
Proposition 3.4. (vi), (viii): the zf-remainders have weight $\ell_{\mathrm{zf}}+j = \alpha-1$ by Proposition 4.3, and
III.A Proposition 4.2 (2) at $\beta_K = \alpha$ (its Taylor coefficients below $\alpha-1$ vanish on both sides) gives
$K^+$-order $\alpha$. (vii): after Lemma 4.4. (ix): $\sigma^3\hat u_f$ has zf-weight $\ell_3+3 = \alpha-1$, so
$K^+$-order $\alpha$, and Lemma 4.4 with $a = \ell_3$ gives $A\in\dot H^{\infty,\alpha-2}$, $B\in\dot
H^{\infty,\alpha-1}$ and $R_S$, $R_b$ of $L^2$-order $\alpha$. *Step 2.* $u$ has $K^+$-order $\alpha-2$ (Proposition
4.3); $\chi_KC$ has order $\ge\alpha-2$; the coefficient sections at exponents with real part $<\alpha-2$ vanish as
before, none at $\alpha-2$ by (E3). *Step 3.* III.I$''''''''''''$ Lemma 2.4 at $\beta := \alpha$, as it allows
($\beta\in(\alpha-1,\alpha]$): its three meetings of an exponent with the weight, at $\alpha$, $\alpha-2$ and
$\alpha-1$, are excluded by (E3). It gives $w''$ of $K^+$-order $\alpha$ and $a_{\mathrm s}$, $a_{\mathrm b}$ with
exponents of real part $>\alpha-2$, resp. $>\alpha-1$. *Step 4.* $\dot S_{\mathrm{rem}} = A+A_5+a_{\mathrm s}\in\dot
H^{\infty,\alpha-2}$ ($A_5$ at $2+\epsilon_+>\alpha-2$, exactly by Lemma 4.5 as $2+\epsilon_+\notin\mathbb N$); $\dot
b_{\mathrm{rem}} = B+a_{\mathrm b}\in\dot H^{\infty,\alpha-1}$; $\tilde u = w''+w'$ of $K^+$-order $\alpha$. *The
$\iota^+$-side.* The conormal tower coefficients $Y^c_\rho$ ($\mu_\rho\in(-1,0]$) come from
$\sigma^3|\sigma|^{\alpha_\tau-2-\mu}Y(\sigma)$, $Y\in H^{\infty,0}_{\mathrm b}$, of zf-weight $2+\epsilon_+-\mu$; Lemma
4.5 gives $\dot H^{\infty,3+\epsilon_+-\mu}$ exactly, as $3+\epsilon_+-\mu\in\mathbb N$ would need $\mu = \epsilon_+-1$,
excluded as in Proposition 4.3's level 3. No polyhomogeneous coefficient sits at $w_\rho$: an exponent $z$ of $a_\rho$
either falls under III.I$''''''''''''$ Lemma 2.4's clause on exponents, so that $z+d_\rho$ is $\Lambda$-valued and
$\ne3+\epsilon_+$ by (E1), or comes from a conormal profile at the edge ($\hat u_j$, $j\le2$, with degree
$\mu'_j-2\in\{2+\epsilon_+,1+\epsilon_+,\epsilon_+\}$, or $v_0$ with degree $\epsilon_+-1$), each with $z$ plus its
degree equal to $3+\epsilon_+$ and $d_\rho\in\{\mu,0,1\}$ different from that degree, so $z+d_\rho>3+\epsilon_+$.
*The corner (D295).* Near $\mathscr I^+$ and on $\{r\ge t_*/2\}$, $\chi_K = 0$ and $\tilde u = u$, exact at $\iota^+$
by Proposition 4.3 (with $u_I$ of Proposition 3.4). On the transition region $\{t_*/8<r<t_*/2\}$, away from the
corner, $\tilde u = u-\chi_Ku_{\exp}$ with both terms exact at $\iota^+$: $u$ by Proposition 4.3, and $u_{\exp}$ as a
sum of coefficients of exact order times homogeneous or exact-degree profiles, exact at $\iota^+$ where $r\sim t_*$
(D296). Near the corner of $\iota^+$ and $K^+$, $\tilde u$ is the sum over
the pieces of III.I$''''''''''''$ Theorem 3.1, Step 1, of each piece minus its part in $\chi_Ku_{\exp}$. Two kinds of
piece reach $\iota^+$-order exactly $3+\epsilon_+$. The first is the conormal parts of (v), and of the pieces of type
(v) inside (vi) and (viii). These come from III.I$''''''''''''$ Lemma 2.1 (b) with $c =
\sigma^j|\sigma|^k\mathrm{sgn}(\sigma)^\delta$ ($m = 0$) and a single profile, whose conormal part lies in the exact
space of its degree (Proposition 4.3). The second is the level-3 towers of (viii). These come from Lemma 2.1 (a) with
$w = \alpha_\tau+1-\mu$ and the tower's profiles, homogeneous of degree $d_\rho-j$ (III.I$''''''''''''$ section 1), so
$w+1+d_\rho = \alpha_\tau+2 = 3+\epsilon_+$. For each, the part in $\chi_Ku_{\exp}$ is the main term
$\chi_K\sum_j(\chi_+y)^{(j)}p_j$ of (2.1) there, and what is left in $\tilde u$ is its $R$. This is literal for the
conormal towers. For the pieces of type (v) the main terms are reorganised by III.I$''''''''''''$ Lemma 2.4 (Step 3),
and the coefficient sections at exponents below $\alpha$ are exactly sums of states (III.I$''''''''''''$ Lemma 2.3 (a)),
so again what is left is $R$ and terms of the kinds below; so the dichotomy below is exhaustive (D296). Lemma 4.7 puts
$R$ in $\rho_+^{3+\epsilon_+}\rho_K^NH^\infty_{\mathrm b}$ near the corner, for every $N$. Every other term of $\tilde
u$ there is exact at one face with room at the other ((J$'''$6)). It has $K^+$-order $\ge\alpha$ (Steps 0-4) and either
$\iota^+$-order $>3+\epsilon_+$, or is polyhomogeneous at $\iota^+$ with exponents in $\mathcal E_\sharp$, none of real
part $3+\epsilon_+$ (E1). So $\tilde u$ has $(\mathcal E_\sharp,3+\epsilon_+)$ at $\iota^+$ jointly with $\alpha$ at
$K^+$. $\square$

**Lemma 4.7 (III.I$''''''''''''$ Lemma 2.1 at the corner, in $L^2$; D295).** In III.I$''''''''''''$ Lemma 2.1, near the
corner of $\iota^+$ and $K^+$, on $\{r\ge2,\ t_*\ge8r\}$ with $\rho_+ = 1/r$ and $\rho_K = r/t_*$, and in the b-Sobolev
spaces of the density $\frac{dt_*}{t_*}\frac{dr}r\,d\omega$ (that of $\mu_{\mathrm b}$ there):

(a) in case (a), if $|(r\partial_r)^a\partial_\omega^\beta p_j|\lesssim r^{j-d}$ on $\{r\ge1\}$ for all $a,\beta$ (degree
exactly $d-j$, without logarithms), then $R\in\rho_+^{w+1+d}\rho_K^NH^\infty_{\mathrm b}$ for every $N$;

(b) in case (b) with $m = 0$, if $r^{d-j}p_j\in H^\infty_{\mathrm b}$ near $\partial X$ for the density
$|\frac{dr}r\,d\omega|$, then $R\in\rho_+^{\mathrm{Re}\,z+1+d}\rho_K^NH^\infty_{\mathrm b}$ for every $N$. Moreover, on
$\{r\ge2\}$ the left side of (2.1) is $\sum_jr^{-1-j-z}F_j(t_*/r)p_j(x)$, with
$F_j(s) := \frac1{2\pi}\int e^{-i\zeta s}\chi_0(|\zeta|)(-i\zeta)^j|\zeta|^z\mathrm{sgn}(\zeta)^\delta\,d\zeta$ smooth
and bounded with all its $s\partial_s$-derivatives on bounded sets.

*Proof.* Put $s := t_*/r\ge8$. Then $\frac{dt_*}{t_*}\frac{dr}r = \frac{ds}s\frac{dr}r$, and the b-vector fields
$t_*\partial_{t_*}$, $r\partial_r$ are $s\partial_s$ and $r\partial_r|_s-s\partial_s$. So it suffices to bound
$r^as^NR$, $a$ the stated $\iota^+$-weight, in $L^2(\frac{ds}s\frac{dr}r\,d\omega)$, and likewise after applying
$s\partial_s$, $r\partial_r|_s$ and $\partial_\omega$. As in the proof of III.I$''''''''''''$ Lemma 2.1, $R =
\sum_je_{j,r}(t_*)p_j(x)$ there, and $\sigma = \zeta/r$ gives
$$e_{j,r}(t_*) = r^{-1-j}\frac1{2\pi}\int e^{-i\zeta s}(-i\zeta)^j(\chi c)(\zeta/r)\big(\chi_0(|\zeta|)-1\big)\,d\zeta.$$
The amplitude vanishes for $|\zeta|\le c_0$ and for $|\zeta|\ge r$. Integrating by parts $M$ times gives $s^{-M}$ times
the integral of the $M$-th $\zeta$-derivative of the amplitude. A derivative falling on $(\chi c)(\zeta/r)$ gives
$\zeta^{-1}((\sigma\partial_\sigma)(\chi c))(\zeta/r)$, and one falling on $\chi_0(|\zeta|)-1$ gives a factor supported
in $\{c_0\le|\zeta|\le1\}$.

(a) Write $(\sigma\partial_\sigma)^l(\chi c) = |\sigma|^w\tilde c_l$ with $\tilde c_l\in H^\infty_{\mathrm
b}(\pm(0,1),|\frac{d\sigma}\sigma|)$. Then $|e_{j,r}(t_*)|\le
Cr^{-1-j-w}s^{-M}\sum_l\int_{|\zeta|\ge c_0}|\zeta|^{w+j-M}|\tilde c_l(\zeta/r)|\,d\zeta$. By Minkowski's inequality and
the dilation invariance of $\frac{dr}r$,
$$\Big\|\int_{|\zeta|\ge c_0}|\zeta|^{w+j-M}|\tilde c_l(\zeta/r)|\,d\zeta\Big\|_{L^2(\frac{dr}r)}\le\|\tilde
c_l\|_{L^2(\frac{d\sigma}\sigma)}\int_{|\zeta|\ge c_0}|\zeta|^{w+j-M}\,d\zeta<\infty$$
for $M>w+j+1$, uniformly in $s$. As $|r^{d-j}p_j|\le C$, $\|r^{w+1+d}s^NR\|_{L^2}\le C(\int_8^\infty
s^{2(N-M)}\frac{ds}s)^{1/2}<\infty$ for $M>N$. $s\partial_s$ acting on $e^{-i\zeta s}$ is $\zeta\partial_\zeta$, moved
onto the amplitude by parts; $r\partial_r|_s$ acting on $(\chi c)(\zeta/r)$ gives $-((\sigma\partial_\sigma)(\chi
c))(\zeta/r)$. Both keep the form above, and $(r\partial_r)^a\partial_\omega^\beta p_j$ keeps the bound.

(b) Here $(\chi c)(\zeta/r) = r^{-z}|\zeta|^z\mathrm{sgn}(\zeta)^\delta\chi(\zeta/r)$, and the derivatives of the
amplitude are $O(|\zeta|^{\mathrm{Re}\,z+j-M})$ uniformly in $r$ (a derivative of $\chi(\zeta/r)$ gives
$r^{-1}\le|\zeta|^{-1}$ on its support). So $e_{j,r}(t_*) = r^{-1-j-z}E_j(s,r)$ with
$|(s\partial_s)^a(r\partial_r|_s)^bE_j|\le
C_{ab}s^{-M}$ for $M>\mathrm{Re}\,z+j+1$, and
$$\|r^{\mathrm{Re}\,z+1+d}s^NR\|_{L^2}\le C\sum_j\Big(\int_8^\infty
s^{2(N-M)}\frac{ds}s\Big)^{1/2}\|r^{d-j}p_j\|_{L^2(\frac{dr}r\,d\omega)},$$
likewise with b-derivatives. For $r\ge2$, $\chi = 1$ on the support of $\chi_0(|\sigma|r)$, so the left side of (2.1)
is $\sum_j(y^{(j)}*k_r)(t_*)p_j(x)$, with $(y^{(j)}*k_r)(t_*) = r^{-1-j}\frac1{2\pi}\int
e^{-i\zeta s}\chi_0(|\zeta|)(-i\zeta)^jc(\zeta/r)\,d\zeta = r^{-1-j-z}F_j(s)$. $F_j$ is the inverse Fourier transform
of a compactly supported integrable function, as $\mathrm{Re}\,z+j>-1$, so it is smooth; and $s\partial_sF_j$ is the
same transform of $-\partial_\zeta(\zeta\,\cdot)$ of the amplitude, again integrable. $\square$

## 5. The theorems at exact weights

**Lemma 5.1 (III.J's Step $\lambda_0$ at the exact $K^+$-weight).** For each $\lambda_0\in\Lambda_*$ fix
$\delta_{\lambda_0}\in(0,\delta_1]$, $\delta_1 :=
\min(\min_\nu(\kappa_\nu-\epsilon),\mathrm{Re}\,\lambda_0+3)-\alpha>0$, such that no $-\mu$ and no point of
$\mathrm{Re}\,\pi_1\mathcal E_K$ lies in $(\ell_K(\lambda_0),\ell'_K]$, $\ell'_K :=
\ell_K(\lambda_0)+\delta_{\lambda_0}<3$. Then III.J's $[h]_{\lambda_0}$ has $K^+$-order exactly $\alpha$ (with room), in
place of "$\alpha-$".

*Proof.* The step source $f = -F_0(\lambda_0)-\bar LT(\lambda_0)$ has room: $F_0$ is compactly supported in
$(\iota^+)^\circ$ (III.J Lemma 2.1), and the coefficients of $\bar LT(\lambda_0)$ have $K^+$-order
$\ge\min(\kappa_\nu-\epsilon,\mathrm{Re}\,\lambda_0+3)>\alpha$, as $\kappa_\nu-\epsilon>\frac92$ and
$\mathrm{Re}\,\lambda_0+3\ge\lambda_\sharp+3>\frac92$; so its coefficients lie in $H^{\infty,\ell'_K-2}_{\mathrm b}$ at
$R = 0$. III.G$'''$ Corollary 3.1 (2) and Remark 3.3, for every solution of the form (3.2) there and every
$\ell_K<\ell^{\max}_K$, apply at $\ell'_K$ to the same $v = u_{\lambda_0}+\mathcal S_{\lambda_0}(f)$ (to $u_{\lambda_0}$
by III.J Lemma 1.2), giving $v = \chi_Kv'_0+\tilde v'$ with $\tilde v'\in\sum_jt_*^{-\lambda_0}(\log
t_*)^jH^{\infty,\ell'_K}(\iota^+)$. By the choice of $\delta_{\lambda_0}$, $v'_0$ has the same formal solutions as
$v_0$, all of rate $<\alpha$, which III.J's rows and towers remove. So $[h]_{\lambda_0} = \tilde v'$ plus terms of order
$\ge\mathrm{Re}\,\lambda_0+3>\alpha$; and a term $t_*^{-\lambda_0}(\log t_*)^jw$, $w\in\rho_K^{\ell'_K}H_{\mathrm b}$,
lies in $\rho_K^{\alpha+\delta_{\lambda_0}-\eta}H_{\mathrm b}$ for every $\eta>0$, hence in $\rho_K^\alpha H_{\mathrm
b}$, its $\iota^+$-factor being an index-set term. Here the room is real, so no circle family is needed. $\square$

**Proposition 5.2 (III.I$''''''''''''''$ Lemmas 2.2-2.4 with $q\in\mathcal Q_{\mathrm{ex}}$).** (a)
$h_{\mathrm{rem}}(q)$ has $K^+$-order exactly $\alpha-2$; (b) $L_bh_{b,\mathrm{rem}}(q)$ has $K^+$-order exactly
$\alpha$, smoothly in $b$; (c) at the top level of III.I$''''''''''''''$ Theorem 3.1, $R_qu\in\mathcal
Y^0_{\mathrm{ex},2}(\alpha)$ and $\Delta_q(b')\in\mathcal Y^\natural_{\mathrm{ex},2}(\alpha)$.

*Proof.* (a) $h^{\le1}(S_{\mathrm{rem}})$ and $\dot g(b_{\mathrm{rem}})$ are linear in $S_{\mathrm{rem}}$,
$b_{\mathrm{rem}}$ and their $t_*$-derivatives with stationary tensors, and $\partial_{t_*} =
t_*^{-1}(t_*\partial_{t_*})$ shifts an exact weight by exactly 1; the polyhomogeneous $Y_\rho$-terms have rates
$>2+\epsilon_K\ge\alpha-2$ and $Y^c_\rho$ the rate $3+\epsilon_+-d_\rho>\alpha-2$ (room). (b) $L_bh^{\le1}(S) =
S''(L_2h+L_1\breve h^1)+S'''L_2\breve h^1$ and $L_b\dot g(b) = b'L_1\dot g+b''L_2\dot g$ (III.I$''''''''''''''$ Lemma
2.2's proof), with $S''$, $b'$ exact at $\alpha$; the profiles' $\iota^+$-weights have room (Lemma 2.1) and the towers
give rates $\ge\lambda_\sharp+3>\alpha$. (c) $R_qu$: III.I$''''''''''''''$ Lemma 2.3's "every $\beta<w+\alpha-2$" is
used at the top level with $w>2$, so $\beta = \alpha$ is admitted strictly; its $\iota^+$-weight
$\beta'_++2+\lambda_\sharp-\epsilon>w_+$ has room. $\Delta_q(b')$: its first term is (b), exact at $\alpha$; its
products have factors of $K^+$-order $\alpha-2$ (exact) or $\alpha$, times $\partial_bh_{b,\mathrm{rem}}(q)b'$ of order
$>2$ strictly (rates of $q$: $\alpha-2>2$, $\alpha-1$, and $>2+\epsilon_K$), so each is at $K^+$-order $>\alpha$; at
$\iota^+$ the exponents are in $\Lambda$, none at $3+\epsilon_+$ by (E1), and the conormal parts at
$3+\epsilon_++\eta_E$ have room. $\square$

**Theorem 5.3 (III.I$''''''''''''''$ Theorem 3.1 at exact weights; the source's Corollary 11.66).** Assume Definition
1.3, (H2) read as $a_K = \alpha$ and (H5) as $a_+\le3+\epsilon_+$; let $h\in\mathcal X^\infty_{J,\mathrm{ex}}$, $\vec
p\in\mathcal P$ and $q\in\mathcal Q_{\mathrm{ex}}$ be small and $F\in\mathcal Y^\natural_{\mathrm{ex}}(\alpha)$. Then
the $\vec p\,'$ of III.I$''''''''''''''$ Theorem 3.1 is unchanged, the forward solution $u$ has $K^+$-weight $\alpha-2$
and every $\iota^+$-weight $\beta_+<\min(\frac32,\min\mathrm{Re}\,\mathcal E_+)$, and $u = h_{\mathrm{rem}}(q')+h'$ with
$q'\in\mathcal Q_{\mathrm{ex}}$ and
$$h'\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_\sharp,3+\epsilon_+),\alpha}_{\mathrm
b}(\Omega_*;S^2T^*)^{\bullet,-}.\tag{5.1}$$
The maps $F\mapsto(\vec p\,',q',h')$ are linear and bounded, uniformly for small background, between these fixed-weight
spaces.

*Proof.* III.I$''''''''''''''$ Theorem 3.1's Steps 0-1 and Step 2 at the levels below $\alpha$ are unchanged: their
inputs lie in the "$w-$" classes (Remark 1.2) and their outputs feed only open conditions. At the top level, $\tilde G =
F-\Delta_q(\vec p\,')-R_qu\in\mathcal Y^\natural_{\mathrm{ex}}(\alpha)$ by Proposition 5.2; $G'$ adds $f^S$, $f^b$,
$f^{\mathrm s1}$, linear in $h$ with stationary coefficients and so exact at $a_K = \alpha$ (III.I$'''''''''$ Lemma 2.6
(a)), and $r^\nu$ at $\mathrm{Re}\,e_\nu+\alpha-\epsilon>\alpha$. III.I$'''''''''''''$ at the level $\alpha$ runs
III.I$'''''''''''$-III.I$''''''''''''$ at that level, which Propositions 3.4, 4.3 and 4.6 make exact. Step 3 and its
uniqueness are unchanged ($\mathcal Z_{\mathrm{ex}}\subset\mathcal Z$); Step 4$'$ uses $\tilde G_0\in\mathcal
Y^\natural_{\mathrm{ex}}(\alpha)$ and its comparisons have room ($\delta' = \frac12\min(\epsilon_K,\alpha-4)$); Step 4
is Proposition 4.6. The coefficients killed by "rate $\le2<\alpha-2$" are killed as before. The tensors are those of
III.I$''''''''''''''$ Theorem 3.1; only the weights in which they are estimated change. $\square$

**Proposition 5.4 (III.J Theorem 2.4 and (2.5) at exact weights).** For $U\in\mathcal D^\infty_{\mathrm{ex}}$ small,
$\Phi(U)\in\mathcal X^\infty_{J,\mathrm{ex}}\times\mathcal P\times\mathcal Q_{\mathrm{ex}}$, and
$P_5(\Phi(U))\in\mathcal F^{k-2}_{\mathrm{ex}}$ for $U\in\mathcal D^{k+d}_{\mathrm{ex}}$; the same holds for $D_U\Phi$
and $D_{\Phi(U)}P_5\circ D_U\Phi$; and the tame bounds of III.J Theorem 2.4 and III.J$''$ Proposition 4.3 hold with
these norms. The forward map gains nothing in the weights.

*Proof.* We follow III.J Theorem 2.4's proof. *$h$.* At $\mathscr I^+$ as before. At $\iota^+$ the exponents lie in
$\mathcal E_\sharp\subset\mathcal E_+$ (III.J Lemma 2.3) and $\tilde h$ is at plain $3+\epsilon_+$; no exponent sits at
$3+\epsilon_+$ (E1). At $K^+$, each $\chi_\iota[h]_{\lambda_0}$ has order $\alpha$ by Lemma 5.1, and $\tilde h$ by
hypothesis. *$q$.* Its components are $S_{\mathrm{rem}}$, $b_{\mathrm{rem}}$, $Y_{\rho,\mathrm{rem}}$, exact, plus
polyhomogeneous coefficients with real parts below $3+\epsilon_+-d_\rho$ (III.J Lemma 2.3). *(2.5) at $\mathscr I^+$:*
III.I Corollary 4.2 as before; III.I (4.1) is exact. *At $\iota^+$:* the terms of $u$-exponent below $3+\epsilon_+$
vanish by the identity (2.3) of III.J; the quadratic part is at $(5+2\delta_\sharp)->w_+$; $L_{0,\vec p_{\le0}}\tilde h$
is exact at $w_+$ by III.I (4.1); the rows' terms of $u$-exponent $\ge3+\epsilon_+$ are in $\Lambda$, so above
$3+\epsilon_+$ by (E1), with defects at $a_++\mathrm{Re}\,\lambda+2-\epsilon\ge2\lambda_\sharp+2-\epsilon>w_+$; the
towers' conormal parts $T_\rho(Y^c_\rho)$ are diagonal terms of Lemma 2.1 ($c = 3+\epsilon_+-d_\rho$, $m = d_\rho$),
exact at $\iota^+$ with $K^+$-weight $c-\eta>\alpha-2$, and vanish near $\mathscr I^+$; $S_{\mathrm{rem}}$,
$b_{\mathrm{rem}}$ give $\iota^+$-orders above $3+\epsilon_+$ (Lemma 2.1 with their profiles); $P_4(0,\vec p_{\le0})$ is
compactly supported in $(\iota^+)^\circ$. So the result has the plain weight $w_+$. *At $K^+$:* $L_bh$ has order
$\alpha$ ($L_b$ stationary and a b-operator there, III.I section 4); the nonlinear part is $\ge2\alpha$; $P_5-P_4 =
L_bh_{b,\mathrm{rem}}(q)+\int(\dots)$, the first exact at $\alpha$ (Proposition 5.2 (b)), the integral
$\ge2\alpha-4>\alpha$; the rows enter through $\vartheta_{\nu,\sharp}$ at $\kappa_\nu-\epsilon>\alpha$, the rotation
rows at $\mathrm{Re}\,\lambda+4>\alpha$. Products of exact weights are exact (II.G Lemma 4.1 (2), $\rho^a\rho^b =
\rho^{a+b}$). *Linearization and tameness.* $\Phi = \Phi_0(U_0)+A(U_0)U_1$ (III.J (2.4)), and the $\delta_{\lambda_0}$
depend only on $\lambda_0$, so $D_U\Phi$ is the same construction with the same classes; III.J$''$ Proposition 4.3's
proof is unchanged with fixed weights. $\square$

**Theorem 5.5 (III.J$'$ Theorem 2.1 at exact weights; the source's Theorem 12.8).** There is $d$ such that for
$U\in\mathcal D^\infty_{\mathrm{ex}}$ with $b = b_0$, small in $\mathcal D^{d}_{\mathrm{ex}}$, and $f\in\mathcal
F^\infty_{\mathrm{ex}}$, there is $U'\in\mathcal D^\infty_{\mathrm{ex}}$ with (2.1) of III.J$'$, linear in $f$, with
$\|U'\|_{\mathcal D^k_{\mathrm{ex}}}\le C_k\|f\|_{\mathcal F^{k+d}_{\mathrm{ex}}}$.

*Proof.* Step 0: $\Phi(U)$ is admissible in Theorem 5.3 (Proposition 5.4), and $f\in\mathcal
F_{\mathrm{ex}}\subset\mathcal Y^0_{\mathrm{ex}}(\alpha)$ (Remark 1.2); Theorem 5.3 gives $(h',\vec p\,',q')$ in the
exact classes, with (H5) satisfied as $a_+ = 3+\epsilon_+$. Steps 1-2 subtract values of $D_U\Phi$, which lie in the
exact classes and whose images under $D_{\Phi(U)}P_5$ lie in $\mathcal F_{\mathrm{ex}}$ (Proposition 5.4); Step 2 reads
$g_j$ at $\ell_K(\lambda_0)-\epsilon$, a loss it tolerates, as it needs only the formal solutions of rate $<\alpha$ to
be visible below $\ell_K$. Step 3: after the subtractions $h'$ has no $\iota^+$-term below $3+\epsilon_+$, so its class
$(\mathcal E_\sharp,3+\epsilon_+)$ with vanishing coefficients is the plain weight $3+\epsilon_+$, and its $K^+$-weight
is $\alpha$; so $h'$ is in $\tilde h$'s exact class, and $q'$'s conormal parts have the exact orders. The bounds compose
finitely many bounded maps; the order $d$ is fixed by III.J$''$ Lemma 2.3. $\square$

The $\iota^+$-order of III.J$'$ Lemma 1.1 is thus exactly $3+\epsilon_+$ under (E1); its "$\eta_2 :=
\epsilon_+-3\epsilon$" and the resulting $5\epsilon$ are not needed.

## 6. Tame estimates on one pair of scales

**Corollary 6.6 (III.J$''$ Theorems 4.1-4.2 and Proposition 4.3 without loss in the weights).** Let $\mathcal D^k :=
\mathcal D^k_{\mathrm{ex}}$ and $\mathcal F^k := \mathcal F^k_{\mathrm{ex}}$. Then III.J$''$ Theorems 4.1 and 4.2 hold
with the input and output at the same fixed weights ($\epsilon' = \epsilon = 0$ in III.J$''$ section 1), and III.J$''$
Proposition 4.3 maps $\mathcal D$ to $\mathcal F$ on these scales: the right inverse and the forward map act on one pair
of Banach scales. So (J$''$4) is discharged at $b_0$.

*Proof.* III.J$''$'s calculus (section 1) and Lemma 2.3 are statements about graded Banach spaces; take the exact
spaces. Its elementary families are tame between fixed-weight spaces: the forward solutions (III.I Theorem 5.3, exact),
the background coefficients (products of exact weights, III.J$''$ Lemma 2.4), the finite-dimensional maps, the
integrations (III.A Lemmas 1.2 and 3.2, lossless at weights that are not exponents), and the model inverses, all stated
at fixed weights. The statements of this part are finite compositions of these families at fixed weights with fixed
losses: Corollary 3.2 is III.G$''$ Theorem 4.2 on a fixed circle with the Mellin inverse of Lemma 3.3 and the
Cauchy integrals of Lemma 2.2 (constants $C\delta^{-k-l_0-1}$, $\delta$ fixed); Propositions 3.4, 4.3 and
4.6 replace weights, not maps, in the rows of III.J$''$'s inventory; Lemmas 4.2, 4.4 and 4.5 are fixed maps; Lemma 5.1
and Propositions 5.2 and 5.4 are compositions of III.J's maps. The rows that this part leaves unchanged ((J$'''$7))
still run at "$w-$" weights, with the closed-graph input losses $\epsilon'(\epsilon,k)$ of III.J$''$ section 1; among
them are III.I$''''''''''''''$'s Steps 1-2 below $\alpha$, the spaces $Z_\beta$, and III.I$''''''''''''$ Lemma 3.2's
$\beta_+<\frac32$. They do no harm (D295, verifier 127). Every chain of the inventory starts from exact data (the source
in $\mathcal F_{\mathrm{ex}}$ and the background in its exact class), which lies in every lossy class, and ends in a
statement of this part at an exact weight. So for each $k$ the intermediate margins can be chosen backwards from the
output. This changes $C_k$ but not the derivative loss $d$, as the losses in derivatives are ceilings of continuous
functions of the weights and stay bounded as the margins shrink. So III.J$''$ Theorem 4.1's induction runs from exact
inputs to exact outputs, with losses independent of $k$, and the input loss $\epsilon'$ (whose independence of $k$
III.J$''$ section 1 could show only row by row, verifier 126) is $0$ for every $k$. This discharges III.J$''$ section 1's
"for the other rows it is part of (J$''$4)". The exactness of the outputs rests on Proposition 4.6, with Lemma 4.7.
III.J$''$ Theorem 4.2's proof then gives (4.2) with $\mathcal F^{k+d}_{\mathrm{ex}}$ and $\mathcal D^k_{\mathrm{ex}}$,
and Proposition 5.4 gives Proposition 4.3 on the same scales. $\square$

What remains of III.J$''$ Remark 4.4: (J$'$3), the linear theory and its tame form at $b\ne b_0$; the support conditions
of II.G Theorem 2.1; smoothing operators on $\mathcal D_{\mathrm{ex}}$ (II.G Proposition 3.1); and the exterior family
$h_{-S}$ (III.C$'$, III.C$''$).

## 7. Findings, labels and sources

(J$'''$1) *The loss at $K^+$ is a convention.* III.G$''$ Corollary 4.3 writes its $\iota^+$-terms in powers of $\log
t_*$; at the corner this hides $\log\rho_K$, and that convention's class and Definition 2.8's are incomparable at the
exact weight (Remark 3.1). In the
convention of Definition 2.8 the graft is exact (Corollary 3.2). The source has the same minus in its Corollary 9.12 and
states the exact weight after the step in Proposition 11.34 ((11.120b)).

(J$'''$2) *III.A Proposition 4.2 is exact at $K^+$* (Proposition 4.1); the $\epsilon$ of III.I$'''''''''''$ Proposition
3.1 at $K^+$ was transmitted from the graft, not produced there. The $\delta$ of III.I$''''''''''$ Lemma 2.4 (b) is a
free weakening (Lemma 4.2).

(J$'''$3) *Four pointwise proofs at the final weight* (III.I$''''''''''''$ Lemma 2.2; Lemma 2.1 (a) for $\chi_+y$; Lemma
2.1's bounds near $\iota^+$ and at the corner with $K^+$, missed at D293 and found by verifier 127; and the Taylor
remainder of Theorem 3.1's piece (vii)) give only "$w-$" in $L^2$; they are re-proved in $L^2$ (Lemmas 4.4, 4.5 and
4.7).

(J$'''$4) *At $\iota^+$ there is no loss.* The level-2 margin and the $5\epsilon$ of III.J$'$ Lemma 1.1 are choices; at
the closed endpoint of (G$^+$) every map is exact and the non-resonance conditions of level 3 hold automatically from
$\epsilon_+<\epsilon_{\mathrm{ind}}$ and III.F$'$ (2.2) (Proposition 4.3), as in the source's Part 4 of the proof of its
Theorem 11.59 (pp. 289-291). (H5) of III.I$''''''''''''''$ becomes $a_+\le3+\epsilon_+$.

(J$'''$5) *New conditions* (E2)-(E4), each a finite exclusion (Lemma 1.4); (E1) is (G$^+$) used at its closed
endpoint, and (E5) is vacuous. The $K^+$-weight is one fixed admissible
$\alpha$; $\alpha = 4+\epsilon_K$ is available under (A$_K$). No condition on $\mathrm{spec}_{\iota^+}(\bar L)$ beyond
(G$^+$) is needed, as no improvement after the fact is made.

(J$'''$6) *Diagonal terms at $\iota^+\cap K^+$* (Lemma 2.1) are exact at one face only with room at the other. Every
such term met here (the towers' conormal parts, the $q$-terms) has room at the other face.

(J$'''$7) *Statements left unchanged.* The intermediate statements of III.I-III.I$''''''''''''''$ whose losses feed open
conditions with room (among them III.I$''$ Proposition 5.1, III.I$'''$ Proposition 2.1, III.I$'''''$ Proposition 2.1 and
III.I$''''''''$'s lemmas below the top level) are not restated; the exact classes lie inside their classes (Remark 1.2).
III.G$''''$ Proposition 5.1's hypothesis "$2-\alpha+j\ne-\mu$" is used by its proof only for
$j\le\lfloor\ell_{\mathrm{zf}}\rfloor$.

*Labels.* Corollary 3.2 is the source's Corollary 9.12 in the convention of its Definition 2.8; Theorem 5.3 its
Corollary 11.66 with (11.234); Theorem 5.5 its Theorem 12.8; Definition 1.1 its (11.226), (11.227b), (11.233),
(12.12c)-(12.12d), (12.31). Definition 1.3, Lemma 1.4, Lemmas 2.1-2.2, Remark 3.1, Lemma 3.3, Propositions 3.4, 4.1,
4.3, 4.6, Lemmas 4.2, 4.4, 4.5, 4.7, 5.1, Propositions 5.2, 5.4 and Corollary 6.6 are new at $n = 4$.

*Sources.* [Hin26] p. 48 (Definition 2.8), pp. 178-179 ((9.42), Corollary 9.12), p. 248 ((11.102)), pp. 253-254
(Proposition 11.34, Step 2.2, (11.120b)), p. 267 (Proposition 2.25 (1) at $\beta_K = \alpha_K$), p. 278 (Theorem 11.59),
pp. 289-291 ((11.222), Part 4 of the proof of Theorem 11.59), pp. 292-295 ((11.226), (11.227b), Corollary 11.66), p. 301
((12.12c)-(12.12d)), p. 310 (Theorem 12.3, (12.31)), p. 312 (Theorem 12.8), read at source. Inputs: III.A (E1), Lemmas
1.2, 1.4, Proposition 4.2; III.F$'$ Proposition 2.3, (2.2); III.G$'$ (1.3), Lemma 4.2, Theorem 3.1; III.G$''$ (4.3),
Lemma 4.1, Theorem 4.2, Corollary 4.3; III.G$'''$ Corollary 3.1, Remark 3.3; III.G$''''$ Propositions 4.4, 5.1; III.H
Proposition 3.2; II.G Lemma 4.1; II.G$'$ Lemma 2.2, Proposition 2.8, Propositions 3.3, 3.5; III.I Theorem 5.3, (4.1),
Corollary 4.2; III.I$''$ Lemmas 4.1-4.2; III.I$'$ Proposition 3.1; III.I$'''''''''$ Lemma 2.6; III.I$''''''''''$
Definition 1.3, Lemmas 1.2, 2.4, Proposition 3.1; III.I$'''''''''''$ Lemmas 2.1-2.2, Proposition 3.1, Lemma 3.2, Theorem
4.1; III.I$''''''''''''$ Lemmas 2.1, 2.2, 2.4, Theorem 3.1; III.I$'''''''''''''$; III.I$''''''''''''''$ Definition 1.1,
Lemmas 2.2-2.5, Theorem 3.1; III.J Definition 1.1, Lemmas 1.2, 2.1, 2.3, Theorem 2.4, (2.3)-(2.5); III.J$'$ Lemma 1.1,
Theorem 2.1; III.J$''$ sections 1-4.
