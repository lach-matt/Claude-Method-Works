# Part III.K. The nonlinear stability theorem, n = 4 ([Hin26] section 13.1)

*Status.* Written (D300); verified (D304: verifier 132's findings seated, to be read). This part proves [Hin26] Theorem
13.1 at spatial dimension $n = 4$, near the Schwarzschild-Tangherlini parameter $b_0 = (\mu_0,0)$ (III.B section 3), by
assembling Part III's linear theory with the Nash-Moser theorem of II.G. Two of its inputs are outputs of Part IV
([Hin23a] section 3 at $n = 4$, to be written): III.C$'$ Theorem 2.1 in the cut-off gauge (III.C$''$ (C$''$2)), which
this part also needs on a slab near $\mathscr I^+$ (finding (K2)), and III.E Theorem 1.1. Theorem 4.3 is proved here
conditionally on Part IV, as III.C$'$ is. It also uses III.I$'''''''''''''''$ Corollary 3.2, verified (D299), whose
repairs are being read. Verifier 133's findings seated (D309): the support classes, $\chi_-$, $\mathcal D$ and the
collar are again defined by $t^\flat_*$ (B-M1); to be read. Verifier 134 read the D309 repairs (D311): correct, but the
restriction $r\ge R_9$ of the slab could give it a timelike side; repaired by $c\le1/R_9$ (D-m1), with one nit (D-n1);
to be read. Proved (D312): verifier 135 read the D311 repair, correct.

The source's proof has four steps: the parameters, the solution up to $t_* = 2$, the Nash-Moser iteration, and
constraint propagation ([Hin26] pp. 320-323). Section 0 fixes the parameters, section 1 builds the initial family,
section 2 the map $\Psi$ and its right inverses, section 3 runs II.G Theorem 2.1, and section 4 propagates the
constraints and states the theorem. At $n = 4$ the source's argument needs three changes, recorded in section 5: a
cut-off gauge that equals the cone's gauge on $\Omega_*$ ((K1)), support classes on every component of supported
character ((K4)), and right inverses for $\Psi$ in which the boost direction carries the initial family ((K3)).

## 0. Setting

*Notation.* $t_* = t-\psi(|x|)$ is III.B (3.6), and $t_{\mathrm{IVP}} = t-\psi_{\mathrm{IVP}}(|x|)$ is III.B Lemma 3.7
(b), with $\Sigma_{\mathrm{IVP}} := t_{\mathrm{IVP}}^{-1}(0)$. $t^\flat_*$ is II.C Lemma 3.2's function ($\ell =
\frac12$), with $C_\flat t_*\le t^\flat_*\le t_*$ there ((b); II.C writes $C'$ for $C_\flat\in(0,1)$, the letter $C'$
being III.B (3.6)'s constant here); $\Omega_* := \mathrm{cl}_M\{t^\flat_*\ge1\}$ (III.I$'$-III.I$''''''''''''''$, III.I
section 1). Put $\hat T := 2/C_\flat\ge2$, so $\{t^\flat_*\ge\hat T\}\subset\Omega_*$. $t^\flat_*$ is defined on
$\{t_*\ge\frac12\}$ (II.C Lemma 3.2; II.E Lemma 1.2 (iv)); a sublevel set $\{t^\flat_*\le c\}$, $c\ge1$, means the
complement of $\{t^\flat_*>c\}$, which lies in $\{t_*>c\}$. Every level used below, the top of $\mathcal D$ and those of
the support classes, lies at $t^\flat_*\ge\hat T\ge2$ (verifier 134's D-n1). The cut-off $\chi_-$, the region $\mathcal
D$ and the support classes of section 3 are defined by $t^\flat_*$. Its differential is past timelike for every
$g_{b_0}+h$ with $h$ small in $\tilde{\mathcal G}^{0,(1,0,0)}_{\mathrm{e3b}}$ (II.C Lemma 3.2 (2)), a margin that
survives the perturbations used below, while $dt_*$'s margin near $\mathscr I^+$ is only $O(\mu_0r^{-2})$ (finding (K9),
amended D309). $t^\flat_*$ is smooth on $M_{1/2}$ near $\mathscr I^+$ (II.C Lemma 3.2 (a)) and equals $t_*$ on $\mathscr
I^+$. Put $T_\iota := (\hat T+2)/C_\flat$ and $T_K := \max(10,T_\iota+2)$. The cut-off $\chi_K$ satisfies
$\mathrm{supp}\,\chi_K\subset\{t^\flat_*\ge T_K\}$ (III.I (1.2), which allows any large threshold); so $\chi_K = 0$ on
$\{t_*<T_K\}$, as $t^\flat_*\le t_*$. $\mathcal S_1$ and the boosts $\phi_S$ are those of III.B section 5,
$g_{b_0,b,-S}$ is III.I (1.1), and $P_5$ is III.I$''''''''''''''$ (1.3). $\Phi$, $\mathcal D$, $\mathcal F$ and
$\mathcal X_J$ are III.J's (Definition 1.1, Theorem 2.4), and $\mathcal D_{\mathrm{ex}}$, $\mathcal F_{\mathrm{ex}}$,
$\mathcal X_{J,\mathrm{ex}}$, $\mathcal Q_{\mathrm{ex}}$ are III.J$'''$ Definition 1.1's exact classes.

*The two time functions.* Put $F(r) := t_{\mathrm{IVP}}-t_* = \psi(r)-\psi_{\mathrm{IVP}}(r)$. By III.B Lemma 3.7 (b),
$\psi_{\mathrm{IVP}} = \psi$ on $[r_0,5R_1]$ and $0\le\psi_{\mathrm{IVP}}'\le\psi'$ beyond, so $F\ge0$, $F' \ge 0$, and
$F = 0$ on $[r_0,5R_1]$; so $t_*\le t_{\mathrm{IVP}}$. For $r\ge R_5 := \max(R_3,3R_1)$, $\psi(r) =
r-C_\psi+8\mu_0r^{-1}$ (III.B after (3.6), $C_\psi$ the constant there) and $\psi_{\mathrm{IVP}}(r) = c_{\mathrm{IVP}}$
is constant, so $F(r) = r-C_\psi-c_{\mathrm{IVP}}+8\mu_0r^{-1}$. Let $R_6 := \max(R_5,2(|C_\psi|+c_{\mathrm{IVP}}))$;
then $F(r)\ge\frac r4$ for $r\ge R_6$.

*Parameters* (the source's Step 1). $E_C$ is given by III.E Theorem 1.1 with $v_C = \frac12$, $C_0 = 100$ and $\gamma_C$
large, so that $(1-e_C)(1-v_C)\gamma_C>100$. $E_\Upsilon =
(c_\Upsilon,e_\Upsilon,\gamma_\Upsilon;c_{\Upsilon,H},\gamma_{\Upsilon,H})$ has $c_\Upsilon$ and $c_{\Upsilon,H}$ as in
III.D and III.D$''$ (III.D$''$ Lemma 3.1), and $\gamma_{\Upsilon,H}$, $e_\Upsilon$, $\gamma_\Upsilon$ small enough for
the mode stability of III.D$''$ Proposition 4.1 and the tf-admissibility of III.F$'$ Proposition 3.3. The data index set
$\mathcal E_0$ and weight $\ell_0$ satisfy the hypotheses of III.C$'$ Theorem 3.1: $\min\mathrm{Re}\,\mathcal
E_0>\frac32+2\gamma_\Upsilon$, $j\mathcal E_0\subset\mathcal E_0$, $\ell_0>\frac32$,
$\ell_0\notin\mathrm{Re}\,\pi_1\mathcal E_0$; with (H4) of III.I$''''''''''$, $\ell_0>3$ as well (VI.C row d1, finding
(VI.C4); amended D323). $\mathcal E^C_I$ and $\ell_I$ are then those of III.C$'$ Theorem 3.1. The weights $\ell_I$,
$\epsilon_+$, $\epsilon_K$, $\alpha$ of the cone are those of III.I-III.J$'''$; the source's $3+\epsilon_0$ and
$1+\epsilon_0$ are $\ell_0$ and $\frac32+\epsilon_0$ in the normalisation of III.C (weights shifted by $\frac12$ at null
infinity, III.C$'$ (1.1)).

*The cut-off $\chi_\iota$.* We take the cut-off $\chi_\iota = \chi(t_*)$ of III.G$''$ section 4 with $\chi = 0$ on
$(-\infty,T_\iota]$ and $\chi = 1$ on $[T_\iota+1,\infty)$, so that $\chi_\iota = 0$ on $\{t_*\le
T_\iota\}\supset\{t^\flat_*\le\hat T+2\}$ (as $C_\flat t_*\le t^\flat_*$), and
$\mathrm{supp}\,d\chi_\iota\subset\{T_\iota\le t_*\le T_\iota+1\}$ is disjoint from $\mathrm{supp}\,\chi_K$, as
$T_K>T_\iota+1$ (as in III.G$''$). III.G$''$ section 4 and III.J use of $\chi_\iota$ only that it is a function of
$t_*$, equal to 1 near $\iota^+$ and supported in $\Omega_*$, with derivatives supported in a compact $t_*$-interval
(finding (K8)).

## 1. The initial family

**Lemma 1.1 (the cut-off of the gauge).** Let $\chi_\natural\in C^\infty(\mathbb R)$ equal 0 on $(-\infty,\frac12]$ and
1 on $[1,\infty)$, $\chi_0$ the cut-off of III.C$''$ section 2, and
$$\chi^\natural_0 := 1-(1-\chi_0)\big(1-\chi_\natural(t_*)\big).\tag{1.1}$$
Then: (a) $\chi^\natural_0\in C^\infty(M)$; (b) $\chi^\natural_0 = 1$ on $\{t_*\ge1\}\supset\Omega_*$; (c)
$\chi^\natural_0 = \chi_0$ on $\{t_*\le\frac12\}$, and on $\Omega_{\mathrm{ext},r_1}$ for $r_1\ge R_6$; (d)
$\chi^\natural_0 = 0$ near $\Sigma_{\mathrm{IVP}}$ and near $\phi_{\pm S}(\Sigma_{\mathrm{IVP}})$ for $|S|$ small.

*Proof.* (a) $\chi_0\in C^\infty(M)$ (III.C$''$ section 2). Near $\mathscr I^+$, $t_*$ is a smooth function on $M$
(III.B after (3.6)); near $I_0$ and near the corner $I_0\cap\mathscr I^+$, $t_*\to-\infty$, so $\chi_\natural(t_*) = 0$;
near $\iota^+$ and $K^+$, $t_*\to+\infty$, so $\chi_\natural(t_*) = 1$. (b) There $\chi_\natural(t_*) = 1$, and
$t^\flat_*\le t_*$. (c) The first claim is clear. On $\Omega_{\mathrm{ext},r_1}\cap\{t_*>\frac12\}$, $r\ge r_1\ge R_6$,
so $t_{\mathrm{IVP}} = t_*+F(r)>\frac r4$, where $\chi_0 = 1$ (III.C$''$ section 2); both cut-offs are 1 there. (d) On
$\Sigma_{\mathrm{IVP}}$, $t_* = -F\le0$. Let $\nu_0 := \min(\frac14,\frac{r_0}8)$, $r_0$ the inner radius (III.B (3.6)).
On $\{|t_{\mathrm{IVP}}|<\nu_0\}$, a neighbourhood of $\Sigma_{\mathrm{IVP}}$, $t_*\le t_{\mathrm{IVP}}<\frac14$, so
$\chi_\natural(t_*) = 0$, and $|t_{\mathrm{IVP}}|<\frac r8$ as $r\ge r_0$, so $\chi_0 = 0$; hence $\chi^\natural_0 = 0$
there. Near $\phi_{\pm S}(\Sigma_{\mathrm{IVP}})\cap\{r\ge r_1\}$, $\chi_0 = 0$ (III.C$''$ (C$''$1), for $\pm S$), so
$|t_{\mathrm{IVP}}|<\frac r4$ there, and for $r\ge r_1\ge R_6$ this gives $t_*<\frac r4-F(r)\le0$. On the compact set
$\{r\le r_1+1\}$, $\phi_{\pm S}\to\mathrm{id}$ smoothly as $S\to0$ (III.B section 5), so $\phi_{\pm
S}(\Sigma_{\mathrm{IVP}})\cap\{r\le r_1+1\}\subset\{|t_{\mathrm{IVP}}|<\nu_0\}$ for $|S|$ small, depending on the fixed
$r_1$, and $\chi^\natural_0 = 0$ there as just shown. $\square$

Let $P^\natural(g,g_0) := \mathrm{Ric}(g)-\delta^*_{g_0,E_C}\Upsilon^{\chi^\natural_0E_\Upsilon}(g,g_0)$, III.C$''$
(2.1) with $\chi^\natural_0$ in place of $\chi_0$.

**Proposition 1.2 (the initial family; [Hin26] (13.5) and (12.33)).** Let $\gamma = \gamma_{b_0}+\tilde\gamma$ and $k =
k_{b_0}+\tilde k$ be data on $\Sigma_{\mathrm{IVP}}$ satisfying the constraint equations, with $\tilde\gamma\in
H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}$ and $\tilde k\in H^{\infty,(\mathcal E_0+1,\ell_0+1)}_{\mathrm b}$, small
in $H^{d_1}$ of these classes for a $d_1$ fixed below. Let $\mathring h_0,\mathring h_1$ be the Cauchy data of III.C$''$
Proposition 4.1 (there written $h_0,h_1$; $h_0$ below is the solution at $S = 0$). For $S\in\mathcal S_1$ small let
$h_{S,0}$, $h_{S,1}$ be III.C$''$'s pulled-back data, now on all of $\Sigma_{\mathrm{IVP}}$. Let $N :=
\{t_{\mathrm{IVP}}\ge-\nu(r)\}$, with $\nu$ smooth and non-decreasing, $\nu = 0$ on $[0,R_\nu]$, $R_\nu :=
\frac12(r_0+R)$ ($r_0$ the inner radius, $R$ III.B section 5's radius inside which $\phi_{\pm S}$ is the identity),
$\nu>0$ on $(R_\nu,\infty)$, $0\le\nu'\le\frac1{32}$, and $\nu(r) = \frac r{64}$ for $r\ge16R_8$ ($R_8\ge\max(2r_1,8,R)$
is fixed in the proof). Such $\nu$ exists, as $\frac{16R_8}{64}\le\frac{16R_8-R_\nu}{32}$; and
$\nu(r)\le\frac{r-R_\nu}{32}\le\frac r{32}$. So $\{t_{\mathrm{IVP}} = -\nu\}$ is spacelike, and $N =
\{t_{\mathrm{IVP}}\ge0\}$ near $\{r = r_0\}$, which is an inflow boundary for a backward problem (verifier 133's B-m1,
B-m2); and
$$\mathcal D := N\cap\{t^\flat_*\le\hat T+3\},\qquad\mathcal D_S :=
\phi_S^{-1}\big(\{t_{\mathrm{IVP}}\ge0\}\big)\cap\{t^\flat_*\le\hat T+2\}.$$
For $|S|$ small, $\mathcal D_S\subset\mathcal D$, and $\phi_S$ maps a neighbourhood of
$\Sigma_{\mathrm{IVP}}\cup\phi_S^{-1}(\Sigma_{\mathrm{IVP}})$ into $N$: near $|x| = r$, $\phi_S$ moves
$t_{\mathrm{IVP}}$ by at most $C|S|r$ (III.B Lemma 5.2) and not at all for $r\le R$, while $\nu(r)\ge c_\nu r$ on
$[R,\infty)$ with $c_\nu := \min(\nu(R)/(16R_8),\frac1{64})>0$; so $C|S|\le\frac12c_\nu$ suffices. ($\phi_S^{-1}$, not
$\phi_S$: $\phi_S^*h_0$ at $p$ needs $h_0$ at $\phi_S(p)$; verifier 132's A-M2.) There is a unique $h_S$ on $\mathcal D$
with
$$P^\natural\big(\phi_S^*g_{b_0}+h_S,\phi_S^*g_{b_0}\big) = 0,\qquad h_S = h_{S,0},\ \ r\mathcal
L_{\partial_{t_{\mathrm{IVP}}}}h_S = h_{S,1}\ \text{on }\Sigma_{\mathrm{IVP}},\tag{1.2}$$
and:

(1) $h_S = \phi_S^*h_0$ on a neighbourhood of $\Sigma_{\mathrm{IVP}}\cup\phi_S^{-1}(\Sigma_{\mathrm{IVP}})$ in $\mathcal
D$, where $h_0 := h_S|_{S=0}$ on $\mathcal D$, a two-sided neighbourhood of $\Sigma_{\mathrm{IVP}}$ (so $\phi_S^*h_0$ is
defined there); so $\phi_S^*g_{b_0}+h_S = \phi_S^*(g_{b_0}+h_0)$ there;

(2) $\mathrm{Ric}(\phi_S^*g_{b_0}+h_S) = 0$ and
$\Upsilon^{\chi^\natural_0E_\Upsilon}(\phi_S^*g_{b_0}+h_S,\phi_S^*g_{b_0}) = 0$ on $\mathcal D$; on $\mathcal
D\cap\Omega_*$ the gauge 1-form is $\Upsilon^{E_\Upsilon}$ (Lemma 1.1 (b)), which is (12.33b) of the source;

(3) on $\mathcal D\cap\Omega_*$, $h_S\in\bar H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I)}_{\mathrm b}$ (orders at
$\mathscr I^+$; the set is bounded in $t_*$); $h_S$ is $C^l$ in $S$ with values in each $H^k$ of this class, for data of
regularity depending on $k$ and $l$ (III.C$''$ Theorem 3.1 (2)); and for each $k$ there are $k'$ and $C_k$ with
$\|h_S\|_{H^k}+\|\partial_Sh_S\|_{H^k}+\|\partial^2_Sh_S\|_{H^k}\le C_k\|(\tilde\gamma,\tilde k)\|_{H^{k+k'}}$.

*Proof.* *The cover.* Let $r_1\ge R_6$ be as in III.C$''$ Theorem 3.1 ($r_1 = 2r_0$, $r_0$ there being III.C$''$'s
exterior radius, not the inner radius of III.B (3.6)), $R_8\ge\max(2r_1,8,R)$, $T'' := (\hat T+3)/C_\flat+\max(0,-C')+2$
with $C'$ III.B (3.6)'s constant, and, with III.C's chart (1.2) translated in $t$ ($g_{b_0}$ is stationary), $\rho'_I :=
(T''-x^1)/|x|$ near infinity. On $\mathcal D$ near infinity $t_*\le t^\flat_*/C_\flat\le(\hat T+3)/C_\flat$ (II.C Lemma
3.2 (b)), so $x^1 = t_*-C'+8\mu_0|x|^{-1}\le T''-1$ and $\rho'_I>0$ there (verifier 133's B-n2). Fix $c\in(0,\frac12]$
as in Part IV$''$ Lemma 2.1. $\mathcal D$ is covered by three sets, solved in this order.

- The exterior domain
$\Omega_{\mathrm{ext},r_1}$, with its past slab $\{-\frac{r-r_1}{12}\le t_{\mathrm{IVP}}\le0\}$, which contains
$\mathcal D\cap\{t_{\mathrm{IVP}}<0,\ r\ge R_8\}$, as $\nu(r)\le\frac r{32}\le\frac{r-r_1}{12}$ for $r\ge R_8\ge2r_1$
(verifier 132's A-m2 (i)).

- The compact part $\mathcal K := \mathcal D\setminus(\Omega_{\mathrm{ext},r_1}\cup\mathcal S)$, with $\mathcal S :=
\mathcal D\cap\{\rho'_I<c,\ r\ge R_9\}\setminus\Omega_{\mathrm{ext},r_1}$, $R_9\ge\max(R_5,4R_1,4|C''|)$, and
$c\le\min(\frac12,1/R_9)$ (Part IV$''$ Lemma 2.1 asks only that $c$ be small, and nothing chosen before $c$ depends on
it). As $x^1\le T''-1$ on $\mathcal D$, $\rho'_I<c$ forces $|x|>1/c\ge R_9$ there, so the clause $r\ge R_9$ is vacuous
and $\mathcal S$ has no side $\{r = R_9\}$ (amended D311, verifier 134's D-m1). On $\{r\ge R_9\}$, $\rho'_I$ is defined
and $t_{\mathrm{IVP}} = t-C''$ (verifier 133's B-n5). On $\mathcal K$ near infinity, above $\Sigma_{\mathrm{fut},r_1}$,
$x^1\ge C''-r_1-2$ (III.C$'$ Lemma 1.1: there $t_{\mathrm{IVP}}\ge r+2r^{1-\ell^\flat_I}-(r_1+2r_1^{1-\ell^\flat_I})$,
and $t_{\mathrm{IVP}} = t-C''$) and $\rho'_I\ge c$, so $|x|\le(T''+r_1+2-C'')/c$; with $t^\flat_*\le\hat T+3$ and
$t_{\mathrm{IVP}}\ge-\nu$ on $\mathcal K\setminus\Omega_{\mathrm{ext},r_1}$, $\mathcal K$ is compact. Its boundary
consists of the part of $\Sigma_{\mathrm{IVP}}$ in it, $\{t_{\mathrm{IVP}} = -\nu\}$ (for the backward problem),
$\Sigma_{\mathrm{fut},r_1}\cap\{\rho'_I\ge c\}$ (data from the exterior), and $\{\rho'_I = c\}$, $\{t^\flat_* = \hat
T+3\}$, $\{r = r_0\}$, spacelike with $\mathcal K$ to their past (Part IV$''$ Lemma 1.1 (a) in the translated chart;
II.C Lemma 3.2 (2) for $t^\flat_*$, which applies to $\phi_S^*g_{b_0}+h_S$ for $|S|$ and the data small; II.C Lemma 3.2
(1) for $r$). So $\Omega_{\mathrm{ext},r_1}\cup\mathcal K$ is closed under past causal curves within $\mathcal D$, and
$\mathcal K$ is the domain of dependence of the past part of its boundary.

- The slab $\mathcal S$ near $\mathscr I^+$, to the future of $\{\rho'_I = c\}\cup\Sigma_{\mathrm{fut},r_1}$ up to
$\{t^\flat_* = \hat T+3\}$; there $x^1$ is bounded, so $\mathcal S$ lies near the interior of $\mathscr I^+$. Its points
near $\mathscr I^+$ depend on all of $\Sigma_{\mathrm{IVP}}$, so it is posed after $\mathcal K$ (verifier 132's A-m2
(ii); Part IV$''$ (IV$''$2)).

*Exterior.* By Lemma 1.1 (c), $P^\natural = P^{\chi_0}$ on $\Omega_{\mathrm{ext},r_1}$, so III.C$''$ Theorem 3.1 gives
$h_S$ there, smooth in $S$, with (2) there by its (3); its hypotheses (the constraints and $\Upsilon^0 = 0$ at
$\Sigma_{\mathrm{IVP}}$) are III.C$''$ Proposition 4.1 (1)-(2).

*Slab.* On $\mathcal S$ the solution is the output of Part IV ((K2) (b); Part IV$'''$ Theorem 2.2, which poses it on
$\Omega_{\mathrm{ext},r_1}\cup\mathcal S$ from $\Sigma_{\mathrm{IVP},r_1}$ and $\{\rho'_I = c\}\cap\partial\mathcal S$,
so that no data sit on $\Sigma_{\mathrm{fut},r_1}$ near $\mathscr I^+$): the continuation near the interior of $\mathscr
I^+$ from the spacelike $(\{\rho'_I = c\}\cup\Sigma_{\mathrm{fut},r_1})\cap\partial\mathcal S$, with the data that
$\mathcal K$ and the exterior give there, to $\{t^\flat_* = \hat T+3\}$, small with the orders $(\langle\mathcal
E^C_I\rangle,\ell_I)$ at $\mathscr I^+$ (III.C$'$ Theorem 3.1). Here $\chi^\natural_0 = 1$: on $\mathcal S$, $\rho'_I<c$
gives $t>(1-c)|x|+T''$, so $t_{\mathrm{IVP}}\ge\frac r4$, and $\chi_0 = 1$ there.

*Compact part.* On $\mathcal K$, (1.2) is a quasilinear wave equation for $h_S$: $P^\natural(g,g_0) =
-\frac12\Box_g(g-g_0)+\ldots$ in the gauge's normal form, with principal part $-\frac12 g^{-1}(\zeta,\zeta)$. Its data
on the part of $\Sigma_{\mathrm{IVP}}$ in $\mathcal K$ are small and smooth, and on
$\Sigma_{\mathrm{fut},r_1}\cap\partial\mathcal K$ the exterior solution gives them. $dt_{\mathrm{IVP}}$ is timelike
(III.B Lemma 3.7 (b)), and the inner boundary $\{r = r_0\}$ is spacelike with $dr$ future timelike (II.C Lemma 3.2 (1)).
So the standard local theory for quasilinear wave equations with small smooth data on the compact domain of dependence
$\mathcal K$ (existence, uniqueness by II.F Lemma 1.3, and Cauchy stability) gives $h_S$ there, forward from
$\Sigma_{\mathrm{IVP}}$ and backward to $\{t_{\mathrm{IVP}} = -\nu\}$, small in every $H^k$ in terms of the data, and
smooth in $S$ as its data are. The source cites the same theory as "standard local well-posedness results" (p. 320). By
II.F Lemma 1.3 (with $\tau := t_{\mathrm{IVP}}$) the three solutions agree on overlaps.

*(2)* is III.C$''$ Theorem 3.1 (3)'s argument on $\mathcal D$. The data satisfy the constraints and
$\Upsilon^{\chi^\natural_0E_\Upsilon} = \Upsilon^0 = 0$ at $\Sigma_{\mathrm{IVP}}$ (Lemma 1.1 (d); III.C$''$ Proposition
4.1 (2)). The second Bianchi identity gives $\delta_gG_g\delta^*_{g_0,E_C}\Upsilon = 0$, a wave equation, whose solution
vanishes by II.F Lemma 1.3 once its Cauchy data vanish. They do: $\Upsilon = 0$ at $\Sigma_{\mathrm{IVP}}$, and the
constraints give $(G_g\delta^*_{g_0,E_C}\Upsilon)(\nu,\cdot) = 0$ there, which with $\Upsilon = 0$ gives
$\partial_\nu\Upsilon = 0$ (Lemma 4.1 below). The proof of III.C$''$ Theorem 3.1 (3) uses no property of the cut-off but
its smoothness.

*(1)*: the order is that of III.C$''$ Theorem 3.1's proof: first $S = 0$, which defines $h_0$ on $\mathcal D$, a
two-sided neighbourhood of $\Sigma_{\mathrm{IVP}}$ (the backward part lying in $N$); then $S\ne0$, which uses $h_0$ at
$\phi_S(p)$ for $p$ near $\Sigma_{\mathrm{IVP}}\cup\phi_S^{-1}(\Sigma_{\mathrm{IVP}})$. III.C$''$ Theorem 3.1 (1) on
$\Omega_{\mathrm{ext},r_1}$. On $\mathcal K$, $\phi_S$ is the identity near $\{r\le R\}$ (III.B section 5), where the
data agree; elsewhere it is (1) of III.C$''$. Both use that the gauge is $\Upsilon^0$, which is natural (III.C$''$
(2.2)), near $\Sigma_{\mathrm{IVP}}$ and near $\phi_{\pm S}(\Sigma_{\mathrm{IVP}})$ (Lemma 1.1 (d)).

*(3)*: the exterior part is III.C$'$ (3.2) and III.C$''$ Theorem 3.1 (2); the slab part is Part IV's output; the compact
part is Cauchy stability. For the $S$-derivatives, $\partial^j_Sh_S$ solves the linearised equation with data
$\partial^j_S(h_{S,0},h_{S,1})$, which are pullbacks of $h_0$ and its derivatives, and so small with $h_0$; its equation
also has the source from varying the background $\phi_S^*g_{b_0}$, which carries a factor of $h_S$ (III.C$''$ Theorem
3.1 (2)'s proof) and is small too. $\square$

## 2. The map $\Psi$

**Definition 2.1 (the source's (12.34)).** Let $\chi_-\in C^\infty(\mathbb R)$ equal 1 on $(-\infty,\hat T+\frac74]$ and
0 on $[\hat T+2,\infty)$. For $U\in\mathcal D^\infty_{\mathrm{ex}}$ small, with second component $S$,
$$\Psi(U) := \big(\chi_-(t^\flat_*)h_{-S},0,0\big)+\Phi(U).\tag{2.1}$$

The first component is defined on $\Omega_*\cap\{t^\flat_*\le\hat T+2\}\subset\mathcal D_{-S}$, and extended by 0.

**Lemma 2.2 (III.J Theorem 2.4 for $\Psi$; the source's Lemma 12.7).** For $U\in\mathcal D^\infty_{\mathrm{ex}}$ small
in $\mathcal D^d_{\mathrm{ex}}$:

(a) $\Psi(U)-\Phi(U)$ is supported in $\{t^\flat_*\le\hat T+2\}$, and $P_5(\Psi(U)) = P_5(\Phi(U))$ on $\{t^\flat_*>\hat
T+2\}$;

(b) if the tail $\tilde h$ of $U$ vanishes on $\{t^\flat_*<c\}$, $c\in[\hat T,\hat T+\frac74]$, then $P_5(\Psi(U)) = 0$
on $\Omega_*\cap\{t^\flat_*<c\}$;

(c) $P_5(\Psi(U))\in\mathcal F^\infty_{\mathrm{ex}}$, and $U\mapsto P_5(\Psi(U))$ satisfies III.J$''$ Proposition 4.3 on
the scales of III.J$'''$ Corollary 6.6, with constants depending on the data through finitely many norms of
$(\tilde\gamma,\tilde k)$;

(d) $P_5(\Psi(0))$ is supported in $\{\hat T+\frac74\le t^\flat_*\le\hat T+2\}$, and $\|P_5(\Psi(0))\|_{\mathcal
F^k_{\mathrm{ex}}}\le C_k\|(\tilde\gamma,\tilde k)\|_{H^{k+k''}}$.

*Proof.* On $\{t^\flat_*<\hat T+2\}$, $\chi_K = 0$ (section 0, $T_K>\hat T+2$), so $g_{b_0,b,-S} = \phi_{-S}^*g_{b_0}$.
Also $h_{\mathrm{tot}}(\vec p)$ and $\vartheta_{\mathrm{tot}}(\vec p)$ vanish there, being supported in $\mathcal
C\subset\mathrm{supp}\,\chi_K$ (III.I$'''''''$ Lemma 2.2, III.I$'''''''''$ Definition 2.3), and so does
$h_{\mathrm{rem}}(q)$, which carries $\chi_K$ (III.I$''''''''''''''$ (1.2)). By III.J (2.1), the metric component of
$\Phi(U)$ is $\chi_\iota\sum_\lambda u_\lambda+\tilde h+\chi_\iota\sum_{\lambda_0}h_{\lambda_0}$, which is $\tilde h$ on
$\{t^\flat_*\le\hat T+2\}$, as $\chi_\iota = 0$ there (section 0).

So on $\Omega_*\cap\{t^\flat_*<\hat T+2\}$,
$$P_5(\Psi(U)) = P\big(\phi_{-S}^*g_{b_0}+\chi_-h_{-S}+\tilde h,\ \phi_{-S}^*g_{b_0}\big),\qquad P(g,g_0) :=
\mathrm{Ric}(g)-\delta^*_{g_0,E_C}\Upsilon^{E_\Upsilon}(g,g_0)$$
(III.I$'''''''''$ (2.3)).

(a) holds as $\chi_- = 0$ on $\{t^\flat_*\ge\hat T+2\}$ and $P_5$ is a differential operator.

(b) On $\Omega_*\cap\{t^\flat_*<c\}$, $\chi_- = 1$ and $\tilde h = 0$, so $P_5(\Psi(U)) =
P(\phi_{-S}^*g_{b_0}+h_{-S},\phi_{-S}^*g_{b_0})$. This is $0-\delta^*0 = 0$ by Proposition 1.2 (2) with $-S$, as
$\Omega_*\subset\{t_*\ge1\}$.

(c) Near $\mathscr I^+\cap\{t^\flat_*\le\hat T+2\}$, III.C Corollary 5.3 applies with $g_0 = \phi_{-S}^*g_{b_0}$ (in
$\mathcal G$, $\mathrm{Ric}(g_0) = 0$) and $h = \chi_-h_{-S}+\tilde h$, which has the orders $(\langle\mathcal
E^C_I\rangle,\ell_I)$ at $\mathscr I^+$ (Proposition 1.2 (3), III.J$'''$ Definition 1.1). So $P_5(\Psi(U))$ has the
orders $(\langle\mathcal E^C_I+1\rangle',\ell_I+1)$ of $\mathcal F_{\mathrm{ex}}$ there. On $\{t^\flat_*>\hat T+2\}$ it
is $P_5(\Phi(U))\in\mathcal F^\infty_{\mathrm{ex}}$ (III.J$'''$ Corollary 6.6). Supported character: for $U$ whose tail
vanishes on $\{t^\flat_*<\hat T\}$ (the class $B^\infty$ of section 3), $P_5(\Psi(U))$ vanishes there by (b); and on
$\{t^\flat_*<\hat T+\frac74\}$,
$$P_5(\Psi(U)) = \int_0^1L_{G_S+s\tilde h,\phi_{-S}^*g_{b_0}}\tilde h\,ds,\qquad G_S := \phi_{-S}^*g_{b_0}+h_{-S},$$
as $P(G_S,\phi_{-S}^*g_{b_0}) = 0$. This is a differential operator applied to $\tilde h$, which has supported
character. The bounds of III.J$''$ Proposition 4.3 hold for $\Phi$. The added terms are $\chi_-h_{-S}$, a fixed tensor
smooth in the finite-dimensional $S$ (Proposition 1.2 (3)), and its products with $\tilde h$ in $P$ on the compact
$t^\flat_*$-range $[1,\hat T+2]$ (verifier 133's B-n3). The Moser estimates of III.J$''$ section 1 bound them with
constants depending on finitely many norms of $h_{-S}$ and $\partial^j_Sh_{-S}$, $j\le2$.

(d) At $U = 0$, $\tilde h = 0$ and $S = 0$, so $P_5(\Psi(0)) = P(g_{b_0}+\chi_-h_0,g_{b_0})$ on
$\Omega_*\cap\{t^\flat_*<\hat T+2\}$ by the display above, and $P_5(\Psi(0)) = P_5(\Phi(0)) = P(g_{b_0},g_{b_0}) = 0$ on
$\{t^\flat_*>\hat T+2\}$ by (a). So it vanishes outside $\mathrm{supp}\,d\chi_-$, is a smooth function of $h_0$
vanishing at $h_0 = 0$, and so is bounded by Proposition 1.2 (3). $\square$

**Lemma 2.3 (right inverses for $\Psi$; III.J$'$ Theorem 2.1 for $\Psi$, the source's Theorem 12.8, last paragraph).**
There are $d$, $\epsilon_0$ such that for $U\in\mathcal D^\infty_{\mathrm{ex}}$ with $\|U\|_{\mathcal
D^d_{\mathrm{ex}}}<\epsilon_0$ there is a linear map $\mathcal R(U):\mathcal F^\infty_{\mathrm{ex}}\to\mathcal
D^\infty_{\mathrm{ex}}$ with $D_U(P_5\circ\Psi)(\mathcal R(U)f) = f$. It satisfies the tame estimate of III.J$''$
Theorem 4.2 on the exact scales (III.J$'''$ Corollary 6.6). If the tail $\tilde h$ of $U$ and $f$ vanish on
$\{t^\flat_*<c\}$, $c\in[\hat T,\hat T+\frac74]$, then so does the tail $\tilde h'$ of $\mathcal R(U)f$.

*Proof.* *The base point.* $\Psi(U) = (h+\chi_-h_{-S},\vec p,q)$ with $(h,\vec p,q) = \Phi(U)$. Its parameter $b$ lies
in $\mathcal B_*$, as $|b-b_0|\le\|U\|_{\mathcal D^d}$. Its metric component $h+\chi_-h_{-S}$ lies in III.I's background
class $\mathcal X^\infty$ (III.I (1.4), which has no support condition) and is small there (Proposition 1.2 (3)).
III.I$''''''''''''''$ Theorem 3.1 (at $b$: III.I$'''''''''''''''$ Proposition 2.5) and III.J$''$ Theorem 4.1 take the
base point only through such a class and its smallness. III.J$'$ Theorem 2.1's proof takes it only through these and
through $D_U\Phi$ at $U$, which depends on $U$ only through $U_0 = (b-b_0,S,S^{(0)}_1)$ (III.J Theorem 2.4: $\Phi$ is
affine in $U_1$).

*The boost direction.* $D_U\Psi(U') = D_U\Phi(U')+(\chi_-\partial_Sh_{-S}(S'),0,0)$, so
$$D_U(P_5\circ\Psi)(U') = D_{\Psi(U)}P_5\big(D_U\Phi(U')\big)+D_hP_5(\Psi(U))\big(\chi_-\partial_Sh_{-S}(S')\big).$$
In III.J$'$ Theorem 2.1's construction, $D_{\Psi(U)}P_5(D_U\Phi(U'))$ enters III.I$''''''''''''''$ (3.1) through
$D_{\vec p}P_5(\vec p\,')$. The boost component $S'$ enters there through its row and its defect $f^S_{h,\vec p}(S')$
(III.I$''''''''''''''$ Step 2). Replace that defect by
$$f^S_\Psi(S') := f^S_{h,\vec p}(S')+e_S(S'),\qquad e_S(S') := \big(D_{\vec p}P_5|_{\Psi(U)}-D_{\vec
p}P_5|_{\Phi(U)}\big)(S')+D_hP_5(\Psi(U))\big(\chi_-\partial_Sh_{-S}(S')\big).$$
$e_S(S')$ is supported in $\Omega_*\cap\{t^\flat_*\le\hat T+2\}$: the two base points differ by $\chi_-h_{-S}$, and
$D_{\vec p}P_5$ is local. On $\{t^\flat_*<\hat T+\frac74\}$, $e_S(S') = f^S_\Psi(S')-f^S_{h,\vec p}(S')$, and both terms
are $O(\tilde h)$: where $\tilde h$ vanishes, $P_5$ vanishes identically in $S$ along both families (Lemma 2.2 (b) for
$\Psi$; $P(\phi_{-S}^*g_{b_0},\phi_{-S}^*g_{b_0}) = 0$ for $\Phi$), the boost row is supported in
$\mathrm{supp}\,\chi_K$, and so both defects vanish there; in general each is an integral of $\tilde h$ as in Lemma 2.2
(c). So for $U$ whose tail vanishes on $\{t^\flat_*<\hat T\}$, $e_S(S')$ vanishes there, and it lies in $\mathcal
F^\infty_{\mathrm{ex}}$, at $\mathscr I^+$ by III.C Corollary 5.3 as in Lemma 2.2 (c). Its bound is tame, $e_S$
involving $\tilde h$ through $D_hP_5$ at $\Psi(U)$: $\|e_S(S')\|_{\mathcal F^k_{\mathrm{ex}}}\le
C_k\big(\|(\tilde\gamma,\tilde k)\|_{H^{k+k''}}+\|(\tilde\gamma,\tilde k)\|_{H^{k''}}\|U\|_{\mathcal
D^{k+d}_{\mathrm{ex}}}\big)|S'|$, by Proposition 1.2 (3) and the Moser estimates of III.J$''$ section 1.

So III.I$''''''''''''''$ Theorem 3.1 at the base point $\Psi(U)$, with the boost defect $f^S_\Psi$, is
III.I$''''''''''''''$ Theorem 3.1 with one more term $e_S(S')$ in Step 2's $G'$. This term is small with the data, and
linear in the finite-dimensional $S'$; it enters Step 3's $A_k$ as $\Delta_q$ does (III.I$''''''''''''''$ Lemma 2.4),
and it perturbs Step 1, the determination of $\vec p\,'_{\le0}$, by a term of the same kind, small with the data. So the
elimination runs unchanged for data small, and III.J$'$'s construction of $U'$, III.J$''$ Theorem 4.2 and III.J$'''$
Corollary 6.6 follow as for $\Phi$. At a rotating $b$, III.I$'''''''''''''''$ Corollary 3.2 provides them.

*Supports.* Let $\tilde h$ and $f$ vanish on $\{t^\flat_*<c\}$, $c\in[\hat T,\hat T+\frac74]$. There $\chi_\iota$,
$\chi_K$ and the corrections vanish, as in Lemma 2.2, and $\chi_- = 1$; so $P_5\circ\Psi = Q(S,\tilde h) := P(G_S+\tilde
h,\phi_{-S}^*g_{b_0})$ there, with $G_S = \phi_{-S}^*g_{b_0}+h_{-S}$. As $Q(S,0) = 0$ for every $S$ (Proposition 1.2 (2)
with $-S$), $\partial_SQ(S,0) = 0$, and on $\{t^\flat_*<c\}$ $$D_U(P_5\circ\Psi)(U') = \partial_SQ(S,0)(S')+D_{\tilde
h}Q(S,0)\tilde h' = L_{G_S,\phi_{-S}^*g_{b_0}}\tilde h';$$ the boost component $S'$ of $U'$ enters only through the
first term, which vanishes. So $L_{G_S,\phi_{-S}^*g_{b_0}}\tilde h' = f = 0$ on $\{t^\flat_*<c\}$. Within the
construction, $\tilde h'$ is the forward solution's remainder there: the rows and towers are supported in
$\mathrm{supp}\,\chi_K$, and the $\iota^+$-terms carry $\chi_\iota$. So $\tilde h' = 0$ on $\{t^\flat_*<c\}$ by II.F
Lemma 1.3 with $\tau := t^\flat_*$, whose differential is past timelike for $G_S$ there, $G_S-g_{b_0}$ being small in
$\tilde{\mathcal G}^{0,(1,0,0)}_{\mathrm{e3b}}$ on $\Omega_*\cap\{t^\flat_*\le\hat T+2\}$ (II.C Lemma 3.2 (2);
Proposition 1.2 (3), III.B Lemma 5.2; finding (K9), verifier 133's B-M1). Without the hypothesis on $\tilde h$,
$D_U(P_5\circ\Psi)(U')$ contains $\partial_SQ(S,\tilde h)(S')$, which need not vanish there (verifier 132's A-M1, a gap
also of the source's Step 3 (3)); II.G Theorem 2.1 (iii) asks the support property only at $U\in B^\infty_\eta$ (amended
in D304), which is how Theorem 3.2 uses it. $\square$

## 3. The Nash-Moser iteration

*The scales.* Let $c_1\in(0,1]$ and $c_0 := \frac18c_1$ be as in II.G Proposition 3.1 for $t := t^\flat_*-\hat T$ on
$M_{1/2}$. (T1)-(T3) hold for it as for $t^\flat_*-1$ in II.G Example 3.2, the level only moving: $t^\flat_*$ is smooth
on $M_{1/2}$ with $dt^\flat_*|_{T\mathscr I^+} = dt_*|_{T\mathscr I^+}\ne0$, and $\{|t|\le2c_1\}$ is bounded in $t_*$,
so meets neither $\iota^+$ nor $K^+$ (finding (K9); verifier 133's B-n1). The weighted b-Sobolev spaces on $M$ and on
$M_{1/2}$ coincide, their b-vector fields being the same. Fix $\chi_9\in C^\infty(\mathbb R)$ equal to 0 on
$(-\infty,\frac{17}2]$ and 1 on $[9,\infty)$. For $\eta\in[0,1]$ and $k\in\mathbb N_0\cup\{\infty\}$ let
$$B^k := \{U\in\mathcal D^k_{\mathrm{ex}}:\ S_{\mathrm{rem}},\,b_{\mathrm{rem}},\,Y_{\rho,\mathrm{rem}}\ \text{supported
in}\ \{t_*\ge8\},\ \mathrm{supp}\,\tilde h\subset\{t^\flat_*\ge\hat T\}\},$$
$$B^k_\eta := \{U\in B^k:\ \mathrm{supp}\,\tilde h\subset\{t^\flat_*\ge\hat T+c_0\eta\},\ \text{the }q\text{-tails
supported
in }\{t_*\ge8+c_0\eta\}\},$$
$$F^k := \{f\in\mathcal F^k_{\mathrm{ex}}:\mathrm{supp}\,f\subset\{t^\flat_*\ge\hat T\}\},\qquad F^\infty_\eta := \{f\in
F^\infty:\mathrm{supp}\,f\subset\{t^\flat_*\ge\hat T+c_0\eta\}\},$$
with the norms of $\mathcal D^k_{\mathrm{ex}}$ and $\mathcal F^k_{\mathrm{ex}}$. $B^k_\eta$ is closed in $B^k$ (support
conditions are closed), non-increasing in $\eta$, and $B^k_0 = B^k$; $F^k$ is closed in $\mathcal F^k_{\mathrm{ex}}$.

**Lemma 3.1 (smoothing on $\mathcal D_{\mathrm{ex}}$; the source's Step 3 (4)).** For $\theta>1$ there are linear maps
$S_\theta:B^\infty_{\theta^{-1/2}}\to B^\infty$ with $S_\theta(B^\infty_\eta)\subset B^\infty_{\eta-\theta^{-1/2}}$ for
$\eta\in[\theta^{-1/2},1]$, satisfying II.G (2.1) with constants independent of $\theta$.

*Proof.* Componentwise; the norm of $\mathcal D^k_{\mathrm{ex}}$ is the sum of its components' norms (III.J$'''$
Definition 1.1), so (2.1) for each component gives it for the sum. - *Finite-dimensional components:* $b-b_0$, $S$,
$S^{(0)}_1$ and $u^0_\lambda$. Here $S_\theta := \mathrm{id}$. - *$f_\lambda$:* a polynomial in $z$ of bounded degree
with coefficients in a partially polyhomogeneous b-Sobolev space on a compact manifold with boundary, with no support
condition. Smooth each expansion coefficient and the remainder by II.G's operator $\tilde S_\theta$, the smoothing on
all of $w\bar H^0_{\mathrm b}$ with no condition on supports (II.G section 3, Step 4), applied on the manifold carrying
it; then reassemble. - *The $q$-tails* $S_{\mathrm{rem}}$, $b_{\mathrm{rem}}$, $Y_{\rho,\mathrm{rem}}$: weighted
b-Sobolev functions of $t_*\in[1,\infty]$. Use II.G Proposition 3.1 on the one-dimensional manifold $[1,\infty]$ with $t
:= t_*-8$, for which (T1)-(T3) hold trivially (the set $\{|t|<2c_1\}$ lies in the interior). This gives the support
behaviour. - *$\tilde h$:* partially polyhomogeneous at $\mathscr I^+$ with index set collection $\langle\mathcal
E^C_I\rangle$ and remainder of order $\ell_I$ (III.C (3.3), in the splitting III.C (1.6)). By the definition of these
spaces, $\tilde h$ is in one-to-one correspondence with its expansion coefficients $a_{z,j}$ (functions on $\mathscr
I^+\cap\Omega_*$) and its remainder, and the norm is the sum of their norms. Put
$$S_\theta\tilde h := \sum_{(z,j)}\chi_I\rho_I^z(\log\rho_I)^j\,S^{\mathscr I}_\theta(a_{z,j})+S_\theta(\tilde
h_{\mathrm{rem}}).$$
Here $S^{\mathscr I}_\theta$ is II.G Proposition 3.1 on $\mathscr I^+$ with $t|_{\mathscr I^+}$ ($= t^\flat_*-\hat T$
there), and $S_\theta(\tilde h_{\mathrm{rem}})$ is II.G Proposition 3.1 on $M_{1/2}$ with $t = t^\flat_*-\hat T$. The
expansion is taken with a collar of $\mathscr I^+$ whose fibres lie in the level sets of $(t^\flat_*,\omega)$ on
$\{t^\flat_*\le\hat T+2\}$, and any b-smooth collar beyond; $E(a)$ is constant along the fibres.
$(t^\flat_*,x_I,\omega)$ are smooth coordinates on $M_{1/2}$ near $\mathscr I^+$, so the fibres are smooth curves in
$M_{1/2}$ transversal to $\mathscr I^+$, and a function constant along them is smooth on $M_{1/2}$: on $M$ it is
polyhomogeneous at $\mathscr I^+$ with index set $\frac12\mathbb N_0$, without logarithms. So passing from a smooth
collar of $M$ to this one changes $\chi_I\rho_I^z(\log\rho_I)^jE(a)$ by terms $\rho_I^{z+k/2}(\log\rho_I)^j$ times
smooth functions, $k\ge1$. These stay in the class: each slot's index set $\mathcal E_s$ in III.C (3.3) is $\mathcal
E^C_I$ together with points of $\mathcal E^{\mathrm{tot}}_I$ (III.C (3.2)), so $\mathcal E_s+\frac12\subset\mathcal
E^C_I\subset\mathcal E_s$ by III.C Lemma 3.2 (a), logarithmic orders included. The terms of order below $\ell_I$ join
the expansion and the others the remainder, so the space and its norm are unchanged up to equivalence. For $U\in B_\eta$
the coefficients vanish on $\{t^\flat_*<\hat T+c_0\eta\}\cap\mathscr I^+$, as $\tilde h$ does near it; so each term
$\chi_I\rho_I^z(\log\rho_I)^jE(a_{z,j})$, and hence the remainder, is supported in $\{t^\flat_*\ge\hat T+c_0\eta\}$, the
fibres preserving $t^\flat_*$. II.G's operators preserve the support classes. (Verifier 132's A-M3 asked that the collar
follow the levels of the function defining the classes; verifier 133's B-M1, that this function have a robust timelike
margin. $t^\flat_*$ meets both, at the cost of the half-integer powers just absorbed.) $\square$

**Theorem 3.2 (the solution of the gauge-fixed equation in the cone; the source's Step 3).** There are $d_1$ and
$\epsilon>0$ such that, if $\|(\tilde\gamma,\tilde k)\|_{H^{d_1}}<\epsilon$, there is $U\in B^\infty_{1/2}$, small in
$\mathcal D^{3d}_{\mathrm{ex}}$, with $P_5(\Psi(U)) = 0$ on $\Omega_*$. Its tail $\tilde h$ is supported in
$\{t^\flat_*\ge\hat T+\frac12c_0\}$.

*Proof.* Apply II.G Theorem 2.1 with $B^k$, $B^k_\eta$, $F^k$ and $F^\infty_\eta$ as above, $\eta_0 := 1$, and the map
$U\mapsto P_5(\Psi(U))$ on $\{U\in B^\infty:|U|_{3d}<\delta\}$.

*(i)* is Lemma 3.1.

*(ii)* For $U\in B_\eta$, $\eta\le1$, the tail vanishes on $\{t^\flat_*<\hat T+c_0\eta\}$, and $\hat T+c_0\eta\le\hat
T+\frac18<\hat T+\frac74$. So $P_5(\Psi(U))\in F^\infty_\eta$ by Lemma 2.2 (b)-(c). The map is twice differentiable in
II.G's sense, with (2.2)-(2.3), by Lemma 2.2 (c). Its $q$-tails enter only through $h_{\mathrm{rem}}(q)$, whose factor
$\chi_K$ vanishes on $\{t_*<10\}$ (III.I$''''''''''''''$ (1.2) and section 0, $T_K\ge10$). They also enter through the
iteration of III.J, whose sources involve them only through $h_{\mathrm{rem}}(q)$ (III.J Theorem 2.4 (2)). So the map
depends on the $q$-tails only through their values on $\{t_*\ge10\}$.

*(iii)* For $U$ in the domain, put $\Psi_{\mathrm{NM}}(U) := Z\mathcal R(U)$, with $\mathcal R(U)$ from Lemma 2.3 and
$Z$ the multiplication of the $q$-tails by $\chi_9(t_*)$. By (ii)'s last sentence, $D_U(P_5\circ\Psi)(Z U') =
D_U(P_5\circ\Psi)(U')$, as $\chi_9 = 1$ on $\{t_*\ge9\}$. So $\Psi_{\mathrm{NM}}(U)$ is a right inverse. $Z$ is bounded
on every $\mathcal D^k_{\mathrm{ex}}$ ($\chi_9(t_*)$ is smooth and constant near $t_* = \infty$), so (2.4) holds by
Lemma 2.3. $Z$ maps into $B^\infty_1$ as far as the $q$-tails are concerned: their support lies in
$\{t_*\ge\frac{17}2\}\subset\{t_*\ge8+c_0\}$. For $U\in B_\eta$ in the domain and $f\in F_\eta$, the tails of $U$ and
$f$ vanish on $\{t^\flat_*<\hat T+c_0\eta\}$, so the tail of $\mathcal R(U)f$ does (Lemma 2.3), and
$\Psi_{\mathrm{NM}}(U)(F^\infty_\eta)\subset B^\infty_\eta$; at $\eta = 0$ this says that $\Psi_{\mathrm{NM}}(U)$ maps
$F^\infty$ into $B^\infty$. This is II.G Theorem 2.1 (iii) in its form amended in D304, for $u\in U\cap B^\infty_\eta$,
which is all its proof uses; the form for every $u$ in the domain does not hold here (Lemma 2.3's proof).

*Smallness.* Let $N := 21d+6$. The constants $C_k$ ($k\le N$), $C_1$, $C_2$ and $\delta$ depend on the data only through
$\|(\tilde\gamma,\tilde k)\|_{H^{N+k''}}$ (Lemmas 2.2 (c), 2.3); they are bounded once that norm is at most 1. So II.G
Theorem 2.1's $\epsilon_{\mathrm{NM}}$ is uniform, and $\|P_5(\Psi(0))\|_{\mathcal
F^{2d}_{\mathrm{ex}}}<\epsilon_{\mathrm{NM}}$ for data small in $H^{d_1}$, $d_1 := N+k''$, by Lemma 2.2 (d). II.G
Theorem 2.1 gives $U\in B^\infty_{1/2}$ with $|U|_{3d}<\delta$ and $P_5(\Psi(U)) = 0$. $\square$

## 4. Constraint propagation and the theorem

**Lemma 4.1 (the normal derivative; the source's "short calculation", in any dimension).** Let $g$ be a Lorentzian
metric, $\Sigma$ a spacelike hypersurface with unit normal $\nu$, $\eta$ a 1-form with $\eta|_\Sigma = 0$, and
$\delta^*_{g_0,E_C}$ as in III.B Definition 6.1. If $(G_g\delta^*_{g_0,E_C}\eta)(\nu,\cdot) = 0$ on $\Sigma$, then
$\partial_\nu\eta = 0$ on $\Sigma$.

*Proof.* On $\Sigma$, the tangential derivatives of $\eta$ vanish, and the zeroth-order part of $\delta^*_{g_0,E_C}$
vanishes as $\eta = 0$ (III.B Definition 6.1: $\delta^*_{g_0,E_C}-\delta^*_{g_0}$ is of order 0, and
$\delta^*_{g_0}-\delta^*_g$ is of order 0). So $k := \delta^*_{g_0,E_C}\eta = \frac12(\nu^\flat\otimes
w+w\otimes\nu^\flat)$ with $w := \partial_\nu\eta$, $\nu^\flat := g(\nu,\cdot)$, $g(\nu,\nu) = -1$. Then $\mathrm{tr}_gk
= w(\nu)$, and $(G_gk)(\nu,X) = k(\nu,X)-\frac12g(\nu,X)w(\nu)$. For $X$ tangent to $\Sigma$: $k(\nu,X) = -\frac12w(X)$
and $g(\nu,X) = 0$, so $w(X) = 0$. For $X = \nu$: $k(\nu,\nu) = -w(\nu)$, so $(G_gk)(\nu,\nu) = -w(\nu)+\frac12w(\nu) =
-\frac12w(\nu)$, and $w(\nu) = 0$. So $w = 0$. $\square$

**Proposition 4.2 (the metric and the constraints).** Let $U$ be given by Theorem 3.2, $(h,\vec p,q) := \Phi(U)$, $S$
its boost and $b$ its black hole parameter. Define
$$g := \begin{cases}g_{b_0,b,-S}+h_{\mathrm{tot}}(\vec p)+h_{\mathrm{rem}}(q)+\chi_-(t^\flat_*)h_{-S}+h & \text{on
}\Omega_*,\\ \phi_{-S}^*g_{b_0}+h_{-S} & \text{on }\mathcal D_{-S}\cap\{t^\flat_*\le\hat T+\frac14c_0\},\end{cases}$$
$$\eta := \begin{cases}\Upsilon^{E_\Upsilon}(g,g_{b_0,b,-S})-\vartheta_{\mathrm{tot}}(\vec p) & \text{on }\Omega_*,\\
\Upsilon^{\chi^\natural_0E_\Upsilon}(g,\phi_{-S}^*g_{b_0}) & \text{on }\mathcal D_{-S}\cap\{t^\flat_*\le\hat
T+\frac14c_0\}.\end{cases}$$
The two definitions agree on the overlap $\Omega_*\cap\{t^\flat_*\le\hat T+\frac14c_0\}$, and $\mathrm{Ric}(g) = 0$,
$\eta = 0$ on the union.

*Proof.* *Overlap.* There $\chi_K = 0$, so $g_{b_0,b,-S} = \phi_{-S}^*g_{b_0}$; $h_{\mathrm{tot}}$, $h_{\mathrm{rem}}$
and $\vartheta_{\mathrm{tot}}$ vanish; $h = \tilde h = 0$ (Lemma 2.2's proof, and $\mathrm{supp}\,\tilde
h\subset\{t^\flat_*\ge\hat T+\frac12c_0\}$); $\chi_- = 1$; and $\chi^\natural_0 = 1$ (Lemma 1.1 (b)). So both lines of
each definition coincide.

*The equation.* On $\Omega_*$, $P_5(\Psi(U)) = 0$ reads $\mathrm{Ric}(g)-\delta^*_{g_0,E_C}\eta = 0$ with $g_0 :=
g_{b_0,b,-S}$. This is III.I$'''''''''$ (2.3) with $g' = g$, and III.I$''''''''''''''$ (1.3): $P_5(h',\vec p,q) =
P_4(h'+h_{\mathrm{rem}}(q),\vec p)$ with $h' := h+\chi_-h_{-S}$. Below, $\mathrm{Ric}(g) = 0$ and $\eta = 0$ by
Proposition 1.2 (2) with $-S$.

*Propagation.* On $\Omega_*$ the second Bianchi identity $\delta_gG_g\mathrm{Ric}(g) = 0$ gives
$\delta_gG_g\delta^*_{g_0,E_C}\eta = 0$. The operator $\delta_gG_g\delta^*_{g_0,E_C}$ has the principal symbol of
$\delta_gG_g\delta^*_g$, which is $\frac12g^{-1}(\zeta,\zeta)$ times the identity up to the sign convention of III.B:
$\delta^*_{g_0,E_C}-\delta^*_g$ is of order 0. $\eta$ vanishes on $\Omega_*\cap\{t^\flat_*\le\hat T+\frac14c_0\}$, which
contains $\Omega_*\cap\{t^\flat_*\le2\}$ ($\hat T\ge2$). II.F Lemma 1.3 on $\Omega^\circ_*$,
with $\tau := t^\flat_*$ and $c := \frac32$, gives $\eta = 0$. Its compactness hypothesis is checked in II.F section 7.4
for metrics with $dt^\flat_*$ past timelike, and $g$ is one by II.C Lemma 3.2 (2): $g-g_{b_0}$ is small in its class, by
III.H$''$ (B2) and the smallness of $U$, $h_{-S}$. So $\mathrm{Ric}(g) =
\delta^*_{g_0,E_C}0 = 0$. $\square$

The source propagates the constraints from $\phi_S(\Sigma_{\mathrm{IVP}})$, using Lemma 4.1 there. Here $\eta$ already
vanishes on an open slab of $\Omega_*$ (Proposition 1.2 (2)), and Lemma 4.1 enters only through Proposition 1.2's proof.

**Theorem 4.3 ([Hin26] Theorem 13.1 at n = 4; conditional on Part IV).** Let $b_0 = (\mu_0,0)$, and let $\mathcal E_0$,
$\ell_0$ be as in section 0. There are $\epsilon>0$ and $d_1$ such that the following holds. Let $(\gamma,k)$ be initial
data on $\Sigma_{\mathrm{IVP}}$ satisfying the constraint equations, with
$$\gamma-\gamma_{b_0}\in H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}(\Sigma_{\mathrm{IVP}}),\qquad k-k_{b_0}\in
H^{\infty,(\mathcal E_0+1,\ell_0+1)}_{\mathrm b}(\Sigma_{\mathrm{IVP}}),$$
of norm $<\epsilon$ in $H^{d_1}$ of these classes. Then there are a Myers-Perry parameter $b\in\mathcal B_*$ and
$S\in\mathcal S_1$, with $|b-b_0|$ and $|S|$ small, and a Lorentzian metric $g$ on $\Omega_*\cup\mathcal D_{-S}$ with:

(1) $\mathrm{Ric}(g) = 0$;

(2) $g = \phi_{-S}^*(g_{b_0}+h_0)$ near $\phi_{-S}^{-1}(\Sigma_{\mathrm{IVP}})$, so $g$ induces on
$\phi_{-S}^{-1}(\Sigma_{\mathrm{IVP}})$ the data $(\phi_{-S}|)^*(\gamma,k)$;

(3) on $\Omega_*\cap\{t^\flat_*\ge\hat T+2\}$,
$$g = g_{b_0,b,-S}+h_{\mathrm{tot}}(\vec p)+h_{\mathrm{rem}}(q)+h,\qquad(h,\vec p,q) = \Phi(U),\ U\in\mathcal
D^\infty_{\mathrm{ex}},$$
with $h\in\mathcal X^\infty_{J,\mathrm{ex}}$ (orders $(\langle\mathcal E^C_I\rangle,\ell_I)$ at $\mathscr I^+$,
$(\mathcal E_+,3+\epsilon_+)$ at $\iota^+$, $\alpha$ at $K^+$), $q\in\mathcal Q_{\mathrm{ex}}$, and $\vec p$ with the
components $b-b_0$, $S$, $S^{(0)}_1$ of $U$ (III.J Theorem 2.4 (1)-(2));

(4) where $\chi_K = 1$, $g_{b_0,b,-S} = g_b$, so $g-g_b = h_{\mathrm{tot}}(\vec p)+h_{\mathrm{rem}}(q)+h$ there: $g$
settles to the Myers-Perry metric $g_b$ at $\iota^+$ and $K^+$ at the orders of these classes;

(5) the gauge condition $\eta = 0$ of Proposition 4.2 holds on $\Omega_*\cup\mathcal D_{-S}$.

*Proof.* Theorem 3.2 and Proposition 4.2. (2) is Proposition 1.2 (1) with $-S$: there $g = \phi_{-S}^*g_{b_0}+h_{-S} =
\phi_{-S}^*(g_{b_0}+h_0)$. (3) holds as $\chi_- = 0$ on $\{t^\flat_*\ge\hat T+2\}$, with III.J$'''$ Corollary 6.6 for
the exact classes. (4) is III.I (1.1). $\square$

**Remark 4.4 (the source's Remark 13.4 and Theorem 1.1).** (3) is the source's Remark 13.4 (1). As in the source, the
slowest terms at $\iota^+$ come from $h_{\mathrm{tot}}(\vec p)$, which is supported in $\mathcal C$; at $n = 4$ their
orders are those of III.I$'''''''$-III.I$'''''''''$. The source deduces its Theorem 1.1 by pulling back along a
diffeomorphism of $M$ that is the identity near $\mathscr I^+\cup\iota^+\cup K^+$, which changes nothing above.

## 5. Findings, labels and sources

(K1) *The cut-off gauge and the cone's gauge.* The source's initial family solves the cut-off gauge
$\Upsilon^{\chi_0E_\Upsilon}$ ((13.5)), while (12.33b) and $P$ in the cone use $\Upsilon^{E_\Upsilon}$. On $\{1\le
t_*\le2\}$ these agree only where $\chi_0 = 1$. $\chi_0 = 1-\check\chi_0(t_{\mathrm{IVP}}/r)$ need not be 1 at bounded
$r$ with $t_{\mathrm{IVP}}<\frac r4$, a region that $\{1\le t_*\le2\}$ can meet. The cut-off $\chi^\natural_0$ of Lemma
1.1 equals 1 on $\Omega_*$ and equals $\chi_0$ on the exterior domain, so III.C$''$ applies unchanged.

(K2) *What Part IV must deliver here.* (a) III.C$'$ Theorem 2.1 in the cut-off gauge, as III.C$''$ (C$''$2) records. (b)
Its continuation on the slab $\mathcal S$ of Proposition 1.2's proof, near $\mathscr I^+$, from $(\{\rho'_I =
c\}\cup\Sigma_{\mathrm{fut},r_1})\cap\partial\mathcal S$ to $\{t^\flat_* = \hat T+3\}$, posed after the compact part
(D304: the earlier slab between $\Sigma_{\mathrm{fut},r_1}$ and $\{t^\flat_* = 3\}$ had the timelike side $\{r = R_8\}$,
and its points near $\mathscr I^+$ depend on all of $\Sigma_{\mathrm{IVP}}$; Part IV$''$ (IV$''$2)). The exterior domain
reaches $\mathscr I^+$ only up to a finite cross-section, and the slab beyond is a region bounded in $t_*$ that reaches
$\mathscr I^+$; the source covers it in one sentence ("for globally small initial data, $h_S$ thus exists ... on
$\phi_S(\{t_{\mathrm{IVP}}\ge0\})\cap\{t_*\le2\}$", p. 321). (c) III.E Theorem 1.1 (constraint damping), which III.E
states as proved in Part IV. Theorem 4.3 is conditional on these.

(K3) *Right inverses for $\Psi$.* The source says the arguments are identical (Theorem 12.8, last paragraph). Lemma 2.3
is the right inverse that findings (I14 4) of the cone's augmentation (there with $h_{-S} := 0$) and (J6) of III.J defer
to. Here the boost direction carries the initial family: its defect gains $e_S$, supported in
$\Omega_*\cap\{t^\flat_*\le\hat T+2\}$ (verifier 133's B-n4), small with the data, and absorbed in the elimination like
$\Delta_q$ (Lemma 2.3).

(K4) *Support classes.* II.G Theorem 2.1 needs closed classes $B_\eta$ with support conditions on every component of
supported character, since its smoothing is defined only with a margin. The $q$-tails enter only through
$h_{\mathrm{rem}}(q)$, which vanishes on $\{t_*<10\}$, so they are cut off to $\{t_*\ge8\}$ by $Z$ at no cost. The
source uses smoothing with small support growth ([Hin24a] Lemma 6.12, Corollary 6.14) for the same purpose.

(K5) *Smoothing on partially polyhomogeneous spaces*: coefficient by coefficient, and on the remainder, as the source
says (Lemma 3.1).

(K6) *Constraint propagation.* The gauge 1-form vanishes on an open slab of $\Omega_*$ above its initial surface, so
uniqueness for the forward problem suffices on $\Omega_*$ (Proposition 4.2). The source's calculation at
$\phi_S(\Sigma_{\mathrm{IVP}})$ is Lemma 4.1, written out in every dimension and used in Proposition 1.2.

(K7) *Base points.* The Nash-Moser iterates move the black hole parameter. The right inverses at $b\ne b_0$ are
III.I$'''''''''''''''$ Corollary 3.2 (verified D299, repairs being read).

(K8) *The cut-off $\chi_\iota$* is taken to vanish on $\{t^\flat_*\le\hat T+2\}$, so that $\Phi$'s $\iota^+$-terms do not
reach the initial family's region. III.G$''$ section 4 and III.J use only its qualitative properties, so the choice is
free: III.G$''$ is insensitive to the transition interval (verifier 132's A-m4). To keep $\mathrm{supp}\,d\chi_\iota$
and $\mathrm{supp}\,\chi_K$ disjoint, as in III.G$''$, $\chi_K$'s threshold is raised to $T_K$ (section 0).

(K9) *Verifier 132 (D304).* Three structural repairs, each an inherited gap of the source. (i) Lemma 2.3's support claim
holds only for base points whose tail vanishes below the level, so II.G Theorem 2.1 (iii) is weakened to $u\in U\cap
B^\infty_\eta$, which its proof uses (II.G (H10)). (ii) $\mathcal D_S$ is
$\phi_S^{-1}(\{t_{\mathrm{IVP}}\ge0\})\cap\ldots$, and $h_S$ lives on the $S$-independent $\mathcal D$, a two-sided
neighbourhood of $\Sigma_{\mathrm{IVP}}$ (source: Step 2 against Step 4, pp. 321-322). (iii) Proposition 1.2's cover is
re-posed (the compact part as a domain of dependence, the slab after it) and Lemma 1.1 (d)'s proof completed. *Verifier
133 (D309).* D304 had moved the support classes, $\chi_-$, $\mathcal D$ and the collar from $t^\flat_*$ to $t_*$. But
II.F Lemma 1.3 needs its $\tau$ to be a time function for $G_S$, and $dt_*$'s timelike margin for $g_{b_0}$ near
$\mathscr I^+$ is only $O(\mu_0r^{-2})$ ($g_{b_0}^{-1}(dt_*,dt_*) = -18\mu_0r^{-2}+O(r^{-4})$, verifier 133), which a
perturbation $h_{00}$ of order $\rho_I^z$, $\mathrm{Re}\,z<2$, can overturn (B-M1). They are restored to $t^\flat_*$,
whose margin is robust (II.C Lemma 3.2 (2)), with the collar along the levels of $(t^\flat_*,\omega)$; the half-integer
powers this produces at $\mathscr I^+$ lie in the classes (III.C Lemma 3.2 (a); Lemma 3.1). The scales use
$t^\flat_*-\hat T$ on $M_{1/2}$, for which (T1)-(T3) are II.G Example 3.2's checks, and II.F Lemma 1.3's hypotheses for
$\tau = t^\flat_*$ are checked in II.F section 7.4 (as Proposition 4.2 uses). $\nu$ vanishes near $\{r = r_0\}$, an
inflow boundary for the backward problem (B-m1, B-m2), and $\mathcal D$'s top $\{t^\flat_* = \hat T+3\}$ is spacelike
for every metric of the construction (B-m3).

*Labels.* Lemma 1.1, Proposition 1.2 (the source's Step 2 and (13.5)), Definition 2.1 ((12.34)), Lemma 2.2 (Lemma 12.7),
Lemma 2.3 (Theorem 12.8 for $\Psi$), Lemma 3.1 (Step 3 (4)), Theorem 3.2 (Step 3), Lemma 4.1, Proposition 4.2 (Step 4),
Theorem 4.3 (Theorem 13.1) and Remark 4.4 (Remark 13.4).

*Sources.* [Hin26] pp. 311-312 ((12.33)-(12.34), Lemma 12.7, Theorem 12.8 and its last paragraph), pp. 318-323 (section
13.1: Theorem 13.1, Remarks 13.2-13.4, the proof's Steps 1-4), read at source; Corollary 5.15 read at source. Inputs:
II.C Lemma 3.2; II.F Lemma 1.3 and section 7.4; II.G Theorem 2.1, Proposition 3.1 and Example 3.2; III.B (3.6), Lemma
3.7, section 5, Definition 6.1; III.C (1.6), (3.2)-(3.3), Lemma 3.2 (a), Corollary 5.3; III.C$'$ Theorems 2.1, 3.1,
Lemma 1.1; III.C$''$ section 2, Theorem 3.1, Proposition 4.1, (C$''$1)-(C$''$2); III.D$''$ Lemma 3.1, Proposition 4.1;
III.E Theorem 1.1; III.F$'$ Proposition 3.3; III.G$''$ section 4; III.H$''$ (B2); III.I (1.1), (1.2), (1.4);
III.I$'''''''$ Lemma 2.2; III.I$'''''''''$ Definition 2.3, (2.3); III.I$''''''''''''''$ (1.2)-(1.3), Theorem 3.1, Lemma
2.4; III.I$'''''''''''''''$ Proposition 2.5, Corollary 3.2; III.J Definition 1.1, Theorem 2.4, (2.1); III.J$'$ Theorem
2.1; III.J$''$ section 1, Theorem 4.2, Proposition 4.3; III.J$'''$ Definition 1.1, Corollary 6.6; Part IV (to be
written).
