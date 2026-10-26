# Part III.I$'''''''''''''$. The expansion at every level, n = 4 ([Hin26] Theorem 11.59, Parts 2-3)

*Status.* Written (D278); verified (D280: verifier 119's findings seated, to be read). This part extends, at spatial
dimension $n = 4$, the expansion of forward solutions at $K^+$ (III.I$'''''''''''$ Proposition 3.1 and Lemma 3.2) from
the levels $\alpha\in(4+\epsilon_K-\epsilon'_0,4+\epsilon_K]$ to every level $\beta\in(3,4+\epsilon_K]$, and, together
with III.I$'''''''''''$ Theorem 4.1 and III.I$''''''''''''$ Theorem 3.1, to sources whose $\iota^+$-index set carries
the further exponents that the linearisation in the black hole parameters of section 11.8.3 produces. The source reaches
the order $4+\epsilon_K$ level by level (Parts 2 and 3 of the proof of Theorem 11.59, the latter "a routine
repetition"), and its Remark 11.61 records that only $2+\epsilon_K$ orders of $K^+$-decay of $h$ are used.
III.I$'''''''''''$ instead reached the order $\alpha>4$ in one step from an admissible $\alpha'\in(2,3)$, which needs
$a_K\ge4+\epsilon_K$ (III.I$'''''''''''$ (I$'''''''''''$5)). Section 11.8.3 at $n = 4$ linearises at $h$ and carries the
difference to the background $h+h_{b,\mathrm{rem}}(q)$, of $K^+$-order only $\alpha-2-\epsilon$, as a source, so it has
to pass through every level in steps shorter than $\alpha-4$ (III.I$''''''''''''''$ Theorem 3.1, ROUTES-OPEN
4.201-4.203); this part supplies those levels.

*What n = 4 changes.* (1) *The last Taylor level below the order 4.* At a level $\beta<4$ the level-3 source has the
zf-weight $\ell_3 = \beta-4-\epsilon\in(-1,0)$: it has no zf-coefficient to remove, so there is no zero-energy solve at
level 3; III.G$''''$ Proposition 5.1 applies with $w = \ell_3-\alpha_\tau+2>-\epsilon_{\mathrm{ind}}$, which it allows,
and III.I$''$ Lemma 4.2 with the zf-weight $\ell_3$, which it allows. (2) *The rows.* At the level $\beta$ the rows to
be extracted are those of $K^+$-rate below $\beta-2$, a subset $\mathcal N_\beta$ of $\mathcal N$; the others join the
remainder. (3) *Sources.* The class $\mathcal Y^\natural(\beta)$ (Definition 1.2) admits $\iota^+$-exponents of
$\mathcal E_\sharp$ shifted by the increments of $\Lambda$; the log count of III.I$''''''''''$ Lemma 1.2 (c) admits them
(Lemma 1.3). Notation: Parts III.A, III.G$''$, III.G$''''$, III.H, III.I$''$, III.I$''''''''$, III.I$'''''''''$,
III.I$''''''''''$, III.I$'''''''''''$, III.I$''''''''''''$; no instrument is used.

## 1. Setting

Everything of III.I$'''''''''''$ section 1 is kept except its constant $\alpha$: (H1)-(H4), (C5), $\Lambda$,
$K(\lambda)$, $\mathcal E_{\mathrm{par}}$, (G), $\mathcal E^0_{\mathrm{src}}$, $\mathcal Y^0(\cdot)$, the rows $\mathcal
N = \mathcal N_\iota\cup\mathcal N_\sigma$, the spectral notation and the dictionary; $\mathcal E_\sharp$ is
III.I$''''''''''''$'s. The *rate* of a triple $(\tau,\lambda,k)$, $\tau\in\mathcal T$, $\lambda\in\Lambda$, is
$\lambda-1$ (s1), $\lambda$ (s0, s2, v1) or $\lambda+d_\tau$ (c0, c1) (III.I$'''''''''$ section 1); by III.I$''''''''''$
Lemma 1.2 (a) the real parts of the rates form a discrete set.

**Definition 1.1 (admissible levels).** A level $\beta\in(3,4+\epsilon_K]$ is *admissible* if (a) $\beta-2$ is not the
real part of a rate; (b) $\beta$ avoids the finite set of III.I$''''''''''$ Definition 1.3, the values for which
$\beta-\mathrm{Re}\,\lambda_0$, $\lambda_0\in\Lambda$, $\mathrm{Re}\,\lambda_0<2$, equals $-\mathrm{Re}\,\mu$ for a root
$\mu$ of $\widehat{L_{b_0}}(0)$ or lies in $\mathrm{Re}\,\pi_1\mathcal E_K$; and (c) $\beta$ avoids the exclusion set of
III.I$'''''''''''$ section 1 with $\beta$ in place of $\alpha$: the values for which a condition (4.2) of III.G$''''$
Proposition 4.4 fails at the levels 1 and 2 with $\ell_{\mathrm{zf}} = \beta-1-j-\epsilon$, a condition of its
Proposition 5.1 fails at level 3, or a value excluded in III.I$''$ Lemma 4.2 or III.H (1.1) is met at level 3 (for
$\beta>4$ as in III.I$'''''''''''$; for $\beta<4$ by $\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}} = \tau-\beta+2+\epsilon$,
$\tau$ the final tf-weight of Proposition 2.1's Step 4), with $\epsilon$ taken small and off a finite set as there. In
particular $\beta\ne4$, by (a), as $2\in\Lambda$ is the rate of $(\mathrm{s0},2,0)$. The small $\epsilon$ is moreover
taken with $\epsilon<\beta-3$, with $\epsilon<\beta-4$ if $\beta>4$, and with no rate of real part in
$[\beta-2-3\epsilon,\beta-2)$. For $\beta\in(2,3)$, admissibility is III.I$''''''''$'s. The excluded values near any
level are finitely many, so the admissible levels are dense in $(3,4+\epsilon_K]$; and every admissible $\alpha\ge3$ of
III.I$''''''''''$ Definition 1.3 is admissible here, as by (G) no rate has real part in
$(2+\epsilon_K-\epsilon'_0,2+\epsilon_K]$. Put $\mathcal N_\beta := \{\nu\in\mathcal N:\mathrm{Re}\,e_\nu<\beta-2\}$;
$\mathcal N_\beta = \mathcal N$ for $\beta>4$, as every row of $\mathcal N$ has rate at most 2.

**Definition 1.2 (the enlarged sources).** Let $\mathcal E^\natural$ be the set of the pairs
$(\lambda+w_1+\dots+w_m,\,k+l_1+\dots+l_m)$ with $m\ge1$, $(\lambda,k)\in\mathcal E_\sharp$ and $(w_i,l_i)\in\mathcal
E_{\mathrm{ind}}\cup\mathcal E^\iota_{\mathrm{ind}}\cup\{(1,0)\}$, of real part $<3+\epsilon_+$. For
$\beta\in(2,4+\epsilon_K]$, $\mathcal Y^\natural_2(\beta)$ is the space of sections supported in
$\mathrm{supp}\,\chi^\sharp_K$ (III.I (1.2)) lying in $\bigcap_\epsilon H^{\infty,\infty,((\mathcal
E^0_{\mathrm{src}}\cup\mathcal E^\natural)+2,\,w_+-\epsilon),\beta}_{\mathrm b}(\Omega_*;S^2T^*)$, and $\mathcal
Y^\natural(\beta) := \mathcal Y^0(\beta)+\mathcal Y^\natural_2(\beta)$, real sections.

**Lemma 1.3 (the log count for the enlarged sources).** (a) $\pi_1(\mathcal E^\natural)\subset\Lambda$; at $\lambda' :=
\lambda+w_1+\dots+w_m$ the log order $k+l_1+\dots+l_m$ is at most $K(\lambda')-N_*(l_*+1)-1$; and $\mathcal
E^\natural\cap\{\mathrm{Re}<2\}\subset\mathcal E_{++}$.

(b) III.I$''''''''''$ Lemma 1.2 (c) holds for sources in $\mathcal Y^\natural(\beta)$: every exponent $(\lambda,k)$
produced with $2\le\mathrm{Re}\,\lambda\le3+\epsilon_+$ has $\lambda\in\Lambda$ and $k\le K(\lambda)$, and those below 2
lie in $\mathcal E_{++}$.

*Proof.* (a) $\Lambda+w\subset\Lambda$ for the increments (III.I$''''''''''$ Definition 1.1), and $\pi_1\mathcal
E_\sharp\subset\Lambda\cup\pi_1\mathcal M\subset\Lambda$ (III.I$''''''''''$ Lemma 1.2 (a)). The increments have real
part $\ge\eta_0>0$, so $\lambda,\lambda+w_1,\dots,\lambda'$ are $m+1$ elements of $\Lambda$ with increasing real parts
and $n(\lambda')\ge n(\lambda)+m$; hence $K(\lambda')-K(\lambda)\ge m(N_*+1)(l_*+1)$, while $k\le K(\lambda)$ (for
$(\lambda,k)\in\mathcal M$, $k\le L_0\le K(\lambda)$) and $l_i\le l_*$; so $k+\sum l_i\le K(\lambda')-m(N_*(l_*+1)+1)$.
Below 2: $\mathcal E_\sharp\cap\{\mathrm{Re}<2\} = \mathcal M\subset\mathcal E_{++}$ (III.I$''''''''''''$ section 1,
where $\mathcal E_\sharp$ is $\mathcal M$ below 2, with the log orders of $\mathcal E_{++}$), the pairs from $\mathcal
E_\sharp\cap\{\mathrm{Re}\ge2\}$ stay above 2, $\mathcal E_{++}$ is closed under $+(\mathcal
E_{\mathrm{ind}}\cup\mathcal E^\iota_{\mathrm{ind}})$ below 2 (III.I$''''''''$ (1.1)), and $+1$ leaves
$\{\mathrm{Re}<2\}$ ($\lambda_\sharp+1>2$).

(b) In the induction of III.I$''''''''''$ Lemma 1.2 (c)'s proof the log order at $\lambda$ is the largest over its
contributions plus at most $N_*(l_*+1)$ from the raises at $\lambda$. A source exponent of $\mathcal E^\natural$ is a
further contribution, of log order at most $K(\lambda)-N_*(l_*+1)-1$ by (a); so the bound $K(\lambda)$ survives, and the
induction runs as there. Below 2 the source's exponents lie in $\mathcal E_{++}$ by (a), as III.I$''''''''$ (1.1) and
III.I$''''''''''$ Proposition 3.1's Step 2 require. $\square$

The constructions of III.I$''''''''''$, III.I$'''''''''''$ and III.I$''''''''''''$ see the $\iota^+$-index set of a
source only through this count, the plain weight $w_+-\epsilon$ and, for the part not supported in
$\mathrm{supp}\,\chi^\sharp_K$, the $\mathscr I^+$-step (III.I$''''''''''$ Proposition 3.1's Step 1, which acts on
$f_1\in\mathcal Y^0_1$ only; a section of $\mathcal Y^\natural_2$ enters there as $f_2$ does, being supported away from
$\mathscr I^+$). This is used in Proposition 2.4.

## 2. The expansion at every level

**Proposition 2.1 (III.I$'''''''''''$ Proposition 3.1 at every level).** Let $\beta\in(3,4+\epsilon_K]$ be admissible,
$f\in\mathcal Y^\natural(\beta)$, and let $f^\flat$ and $v$ be as in III.I$'''''''''''$ section 1 with $\beta$ in place
of $\alpha$ ($f^\flat$ is III.I$''''''''''$ Proposition 3.1 (c)'s source for $f$, and $v$ the forward solution of
$L_{b_0}v = f^\flat$, with $K^+$-weight $w_v>0$). Then there are $S_\nu\in\mathcal W_{\tau,\mathbb C}$, $\nu\in\mathcal
N_\sigma\cap\mathcal N_\beta$, linear and continuous in $f$, with
$$v-\sum_{\nu\in\mathcal N_\sigma\cap\mathcal N_\beta}m_\nu(S_\nu)\in\bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\beta'_+,\beta-2-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}.\tag{2.1}$$

*Proof.* III.I$''''''''''$ Proposition 3.1 holds at the admissible $\beta$ as stated: its proof uses of $\alpha$ only
$\alpha\le4+\epsilon_K$ (for $\ell_K(\lambda_0)<3$), $\ell_K(\lambda_0) = \alpha-\mathrm{Re}\,\lambda_0>\alpha-2>0$, the
conditions of Definition 1.1 (b), and (G) for the rows of $\mathcal N_\iota$, all of which hold for $\beta$; for
$f\in\mathcal Y^\natural(\beta)$ by Lemma 1.3. Then III.I$'''''''''''$ Proposition 3.1's proof applies with $\beta$ in
place of $\alpha$ and these changes.

*Constants.* $\ell_j := \beta-1-j-\epsilon$ at the level $j\in\{1,2,3\}$, so $\ell_1\in(1,2+\epsilon_K)$,
$\ell_2\in(0,1+\epsilon_K)$ and $\ell_3\in(-1,\epsilon_K)$; $\eta_1$, $\eta_2$ as there.

*Steps 0-3* are unchanged. Step 0 uses $\beta_K = \beta-\epsilon$. At level 1, III.G$''''$ Proposition 4.4's conditions
(4.2) hold for $2\le\mathrm{Re}\,\alpha_0<2+\eta_1$ and $\ell_{\mathrm{zf}} = \ell_1$:
$\ell_1-\mathrm{Re}\,\alpha_0+2>\beta-2-\eta_1-\epsilon>0$ and $\ell_1<3$, the rest by Definition 1.1 (c). At level 2,
for $1+\eta_1\le\mathrm{Re}\,\alpha_0<2+\eta_2$ and $\ell_{\mathrm{zf}} = \ell_2$:
$\ell_2-\mathrm{Re}\,\alpha_0+2>\beta-3-\eta_2-\epsilon>-\epsilon_{\mathrm{ind}}$
($\eta_2+\epsilon<\epsilon_{\mathrm{ind}}$) and $\ell_2-\min(\mathrm{Re}\,\alpha_0-2,0)<\ell_2+1-\eta_1<3$; the
remainder exponents $\alpha_0+\mathcal E_{\mathrm{ind}}$ are treated in turn as there. III.I$'''''''''''$ Lemma 2.2 at
level 2 needs only the zf-weight $\ell_2>0$ of $g_2$, and gives $g_3$ the zf-weight $\ell_3$.

*Step 4 for $\ell_3>0$* ($\beta>4$, where $\ell_3 = \beta-4-\epsilon>0$ by Definition 1.1) is III.I$'''''''''''$'s. *For
$\ell_3<0$* ($\beta<4$), $g_3$ has no zf-term to remove, and the zero-energy solve of level 3 (III.I$'''''''''''$ Lemma
2.1 with $\mu_3$) is omitted. While the tf-weight $\tau$ of the current level-3 source is at most $\beta-2 =
2+\ell_3+\epsilon$, apply III.G$''''$ Proposition 5.1 with $\alpha_\tau := \tau\in(1,2)$ ($\tau\ge\tau_3 =
1+\eta_2-2\epsilon>1$ and $\tau\le\beta-2<2$), $\ell_{\mathrm{zf}} := \ell_3\notin\mathbb N_0$, $k_0 := 0$ and $w =
\ell_3-\tau+2\in[-\epsilon,1)\subset(-\epsilon_{\mathrm{ind}},\ell^{\max}_K)$; its conditions $w\ne-\mu$,
$2-\tau+j\ne-\mu$ hold for $\epsilon$ off a finite set, the values of $\tau$ being
$\tau_3+i(\epsilon_{\mathrm{ind}}-\epsilon)$. Each round leaves a remainder of tf-weight
$\tau+\epsilon_{\mathrm{ind}}-\epsilon$ and pieces $\sigma^3u$; after finitely many rounds $\tau>\beta-2$, and, lowering
$\tau$ if necessary, $\tau\in(\beta-2,\beta-1-\epsilon)$. The rest, $g_J$ (the level-3 source after the rounds), lies in
$H^{\infty,(\frac52-\epsilon,\tau,\ell_3)}_{\mathrm b}$ and is inverted by III.I$''$ Lemma 4.2 with
$\beta_{\mathrm{scf}} := \frac32-2\epsilon$, $\beta_{\mathrm{tf}} := \tau-2$, $\beta_{\mathrm{zf}} := \ell_3$,
$\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}} = \tau-\beta+2+\epsilon\in(0,1)$ ($\epsilon$ off a finite set, Definition 1.1
(c)): $\hat u_f\in H^{\infty,(\frac32-3\epsilon,\tau-2,\ell_3)}_{\mathrm b}$, $\dot b_f,S_f\in
H^{\infty,\ell_3}_{\mathrm b}(\pm(0,c],|\frac{d\sigma}\sigma|)$, with $\ell_3>-1$.

*Step 5.* The matching and the sorting are unchanged. In (iii), $\sigma^3\hat u_f$ has zf-weight $\ell_3+3 =
\beta-1-\epsilon$, and $\sigma^3\hat g^{\mathrm{aug}}(\dot b_f)$, $\sigma^3\hat h^{\mathrm{aug}}(S_f)$ give the
$K^+$-weights $\ell_3+3$ and $\ell_3+2 = \beta-2-\epsilon$ (III.I$'''''''''''$ Lemma 2.4 with $a = \ell_3>-1$); the
level-3 pieces of Step 4 have zf-weight $\ge\alpha_\tau>1$, so $K^+$-weight $>2\ge\beta-2$ for $\beta\le4$ (and as there
for $\beta>4$). III.I$''''''''''$ Lemma 2.4 applies with $\beta_{\mathrm{tail}} :=
\beta-3-2\epsilon\in(-1,1+\epsilon_K)$, not in $\mathbb N_0$ for $\epsilon$ off a finite set, and (iii) contributes
$O(t_*^{-\beta+2+3\epsilon})$, as $\sigma^3\hat h^{\mathrm{aug}}(S_f)$ has zf-weight $\ell_3+1 =
\beta-3-\epsilon>\beta_{\mathrm{tail}}$.

*Step 6.* The stationary columns vanish as there ($w_v>0$). Of the towers listed there, those of rate below $\beta-2$
are the rows of $\mathcal N_\sigma\cap\mathcal N_\beta$: for $\beta\le4$ the s0 and s2 towers of rate
$\mathrm{Re}\,\alpha_0\ge2\ge\beta-2$ are not among them; every tower of rate at least $\beta-2$ has rate $>\beta-2$
(Definition 1.1 (a)), so is $O(t_*^{-\beta+2+3\epsilon})$; and the identification with $m_\nu(S_\nu)$ holds up to terms
of rate $\ge\mathrm{Re}\,e_\nu+3>\beta-2$.

*Step 7* is unchanged, with $\beta$ in place of $\alpha$; it gives (2.1). $\square$

**Lemma 2.2 (III.I$'''''''''''$ Lemma 3.2 at every level).** Let $\beta\in(3,4+\epsilon_K]$ be admissible, $\vec
p\in\mathcal P$ ($b = b_0$) and $h\in\mathcal X^\infty$ small, and $G\in\mathcal Y^\natural(\beta)$. Suppose the forward
solution $u$ of $L_{h,\vec p}u = G$ lies in $\bigcap_\epsilon H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\beta'_+,w_0-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}$ with $w_0>0$, $w_0+a_K>\beta$ and
$\beta'_+\in(\frac32-(\delta_\sharp-\epsilon_+),\frac32)$. Then
$$u = \sum_{\nu\in\mathcal N_\beta}m_\nu(S_\nu)+\tilde u,\qquad\tilde u\in\bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\beta_+,\beta-2-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}\tag{2.2}$$
for every $\beta_+<\min(\frac32,\min\mathrm{Re}\,\mathcal E_+)$, with $S_\nu = S^{h,\vec p,\beta}_\nu(G)\in\mathcal
W_{\tau,\mathbb C}$ determined by $u$, conjugation-symmetric, linear and continuous in $G$, with bounds uniform for
$(h,\vec p)$ small. For $\beta\in(2,3)$, III.I$''''''''$ Lemma 3.2 holds for $F\in\mathcal Y^\natural(\beta)$.

*Proof.* III.I$'''''''''''$ Lemma 3.2's proof, with III.I$''''''''''$ Proposition 3.1 at $\beta$ (as in Proposition
2.1's proof) and Proposition 2.1 for III.I$'''''''''''$ Proposition 3.1. Step 0 gives $f'\in\mathcal Y^\natural(\beta)$
($G$'s $\mathcal Y^\natural_2$-part is untouched, and $(L-L_{b_0})u$ lies in $\mathcal Y^0(\beta)$ as there). The rows
of $\mathcal N_\iota$ of rate at least $\beta-2$ have rate $>\beta-2$ (Definition 1.1 (a)), so their $m_\nu(S_\nu)$ have
$K^+$-weight $\ge\beta-2-\epsilon$ (III.I$'''''''''$ Lemma 2.2 (e)) and join $\tilde u$. *Determination:* by
III.I$''''''''''$ Corollary 2.3 on $\mathcal N_\beta$, all rates there being below $\beta-2$. For $\beta\in(2,3)$:
III.I$''''''''$'s $\mathcal Y(\beta)$ records the $\iota^+$-exponents below 4 in $\mathcal E_{++}+2$ and has the plain
weight $4-\epsilon$ above, and $\mathcal Y^\natural_2(\beta)$ lies in it by Lemma 1.3 (a). $\square$

**Lemma 2.3 (III.I$'''''''''''$ Lemma 3.3 at every level).** In Lemma 2.2, if $(h_j,\vec p_j)\to(0,0)$, $G_j\to G$ in
$\mathcal Y^\natural(\beta)$ and the forward solutions $u_j$ of $L_{h_j,\vec p_j}u_j = G_j$ and $u$ of $L_{b_0}u = G$
satisfy Lemma 2.2's hypothesis with uniform bounds, then $S^{h_j,\vec p_j,\beta}_\nu(G_j)\to S^{0,0,\beta}_\nu(G)$.

*Proof.* III.I$'''''''''''$ Lemma 3.3's proof, with Lemma 2.2 for III.I$'''''''''''$ Lemma 3.2. $\square$

**Proposition 2.4 (the enlarged sources at the top level).** III.I$'''''''''''$ Theorem 4.1 and III.I$''''''''''''$
Theorem 3.1 hold with $F\in\mathcal Y^\natural(\alpha)$ in place of $F\in\mathcal Y^0(\alpha)$, with the same
conclusions.

*Proof.* Their proofs use $F$ through III.I$''''''''''$ Proposition 3.1, III.I$'''''''''''$ Proposition 3.1 and Lemmas
3.2-3.3, III.I$''''''''$ Proposition 4.1 at a level $\alpha'\in(2,3)$, and, in III.I$''''''''''''$ Theorem 3.1's Steps 2
and 5, the statement that the $\iota^+$-exponents produced lie in $\mathcal E_\sharp$; each holds for $F\in\mathcal
Y^\natural$ by Lemma 1.3, Proposition 2.1 and Lemma 2.2 (with $\beta = \alpha$), and III.I$''''''''$'s class contains
$\mathcal Y^\natural(\alpha')$ (Lemma 2.2's last sentence). $\square$

## 3. Findings, labels and sources

(I$'''''''''''''$1) *Every level is needed.* III.I$'''''''''''$ reaches the order $\alpha>4$ in one step from a level
below 3, which needs the background's $K^+$-order $a_K\ge4+\epsilon_K$. The source's Remark 11.61 uses only
$2+\epsilon_K$, at the price of passing through every level (its Parts 2-3), and section 11.8.3 at $n = 4$ meets a
background of $K^+$-order $\alpha-2-\epsilon$, which III.I$''''''''''''''$ carries as a source at $h$. The levels
$(3,4+\epsilon_K]$ that III.I$''''''''''$ Definition 1.3 set aside are supplied here.

(I$'''''''''''''$2) *A negative zf-weight at the last level.* Below the order 4 the level-3 source has the zf-weight
$\beta-4-\epsilon\in(-1,0)$; the zero-energy solve of level 3 drops out, and III.G$''''$ Proposition 5.1 and III.I$''$
Lemma 4.2 accept the weight as they stand.

(I$'''''''''''''$3) *The enlarged sources.* The towers of section 11.8.3 depend on the black hole parameters through the
corrections of their profiles at $\partial X$, so the derivative of the operator in those parameters has
$\iota^+$-exponents $\mathcal E_\sharp$ plus the increments of $\Lambda$; they fit the log count with room to spare
(Lemma 1.3).

*Labels.* Proposition 2.1 and Lemmas 2.2-2.3 are III.I$'''''''''''$ Proposition 3.1 and Lemmas 3.2-3.3 at every level,
the source's Parts 2-3; Definitions 1.1-1.2, Lemma 1.3 and Proposition 2.4 are new at $n = 4$.

*Sources.* [Hin26] pp. 278-289 (Theorem 11.59 and the plan of its proof, Remark 11.61) and pp. 292-295 (section 11.8.3:
Definition 11.63, Lemma 11.65, Corollary 11.66, on which Definition 1.2 and (I$'''''''''''''$3) rest), read at source.
Inputs: III.A Proposition 4.2; III.G$''''$ Propositions 4.4 (with (4.2)), 5.1; III.H (1.1); III.I (1.2); III.I$''$ Lemma
4.2; III.I$''''''''$ (1.1), Lemma 3.2, Proposition 4.1; III.I$'''''''''$ section 1, Lemma 2.2; III.I$''''''''''$
Definitions 1.1, 1.3, Lemma 1.2, Corollary 2.3, Lemma 2.4, Proposition 3.1; III.I$'''''''''''$ section 1, Lemmas
2.1-2.4, Proposition 3.1, Lemmas 3.2-3.3, Theorem 4.1; III.I$''''''''''''$ Theorem 3.1.
